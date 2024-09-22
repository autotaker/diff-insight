{-# LANGUAGE OverloadedStrings #-}
module Main where

import           Control.Monad            (forM, forM_)
import           Data.Function            (on, (&))
import           Data.List                (groupBy, sortBy, sortOn)
import           Data.Maybe               (fromMaybe)
import           Data.Ord
import           Hakyll
import           Text.Pandoc
import           Text.Pandoc.Highlighting (pygments, styleToCss)

pivotBy :: (MonadMetadata m, Ord a) => (Item b -> m a) -> [Item b] -> m [(a, [Item b])]
pivotBy f items = do
    items' <- mapM (\item -> do
        key <- f item
        pure (key, item)) items
    let pivot = items'
                & groupBy ((==) `on` fst)
                & map (\group -> (fst $ head group, map snd group))
                & sortOn fst
    pure pivot

getDate :: MonadMetadata m => Item a -> m (Down String)
getDate item = do
    metadata <- getMetadata $ itemIdentifier item
    let date = lookupString "date" metadata
    pure $ Down $ fromMaybe "0000-00-00" date

main :: IO ()
main = hakyll $ do
    match "templates/*" $ compile templateCompiler
    create ["css/syntax.css"] $ do
        route idRoute
        compile $ do
            makeItem $ styleToCss pygments
    create ["index.html"] $ do
        route idRoute
        compile $ do
            posts <- loadAll "posts/**"
            let postsByDate = do
                    groups <- take 5 <$> pivotBy getDate posts
                    forM groups $ \(Down date, items) -> do
                        let context = listField "posts" defaultContext (pure items) <>
                                      constField "date" date <>
                                      defaultContext
                        makeItem ""
                            >>= loadAndApplyTemplate "templates/post-list-by-date.html" context
                            >>= relativizeUrls
            let indexCtx = listField "posts" defaultContext postsByDate <>
                           constField "title" "Home" <>
                           defaultContext
            makeItem ""
                >>= loadAndApplyTemplate "templates/index.html" indexCtx
                >>= loadAndApplyTemplate "templates/default.html" indexCtx
                >>= relativizeUrls
    forM_ ["openai", "search", "misc"] $ \category -> do
        create [fromFilePath $ "categories/" ++ category ++ ".html"] $ do
            route idRoute
            compile $ do
                posts <- loadAll (fromGlob $ "posts/**/*-" ++ category ++ ".md")
                    >>= recentFirst
                let compilePosts = do
                        forM posts $ \item -> do
                            Down date <- getDate item
                            let context = listField "posts" defaultContext (pure [item]) <>
                                          constField "date" date <>
                                          defaultContext
                            makeItem ""
                                >>= loadAndApplyTemplate "templates/post-list-by-date.html" context
                                >>= relativizeUrls
                let categoryCtx = listField "posts" defaultContext compilePosts <>
                                  constField "title" (category ++ " posts") <>
                                  constField "category" category <>
                                  defaultContext
                makeItem ""
                    >>= loadAndApplyTemplate "templates/category.html" categoryCtx
                    >>= loadAndApplyTemplate "templates/default.html" categoryCtx
                    >>= relativizeUrls
    match "posts/**.md" $ do
        route $ setExtension "html"
        let ropts = defaultHakyllReaderOptions {
            readerExtensions = enableExtension Ext_hard_line_breaks $
                               readerExtensions defaultHakyllReaderOptions
        }
        let wopts = defaultHakyllWriterOptions
        let myPandocTransform = id
        compile $ pandocCompilerWithTransform ropts wopts myPandocTransform
            >>= loadAndApplyTemplate "templates/post.html" defaultContext
            >>= loadAndApplyTemplate "templates/default.html" defaultContext
            >>= relativizeUrls
