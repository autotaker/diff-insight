---
date: '2025-01-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0fcd6d7...MicrosoftDocs:1d7cc3c
summary: この更新では、Azure AI Searchのドキュメントに対して複数のマイナーアップデートが行われました。主な変更内容には、新機能の追加やドキュメントの日付の更新、説明の明確化が含まれています。特に、ハイブリッド検索とベクトル検索に関する設定方法が改善され、ユーザー体験の向上に寄与しています。新たに導入された`threshold`機能により、低スコアの検索結果が除外されるようになり、また、`maxTextRecallSize`および`countAndFacetMode`により結果数の制御が可能になっています。既存の設定やリンクが更新されたため、それに伴う理解の見直しも必要です。多くのドキュメントの日付が更新され、コンテンツの最新性も保たれています。このアップデートは、ユーザーがAzure
  AI Searchをより効果的に活用できるようサポートすることを目的としており、特にセキュリティや検索精度の向上に貢献しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0fcd6d7...MicrosoftDocs:1d7cc3c){target="_blank"}

<format>
# Highlights
この更新では、Azure AI Searchのドキュメントに対する複数のマイナーアップデートが行われています。主な変更点として、新機能の追加、ドキュメントの日付更新、説明の明確化が含まれています。特にハイブリッド検索とベクトル検索における`maxTextRecallSize`の設定方法に関する情報提供が改善されています。

## New features
- `threshold`の追加により、ベクトル検索で低スコアの結果を除外する機能が導入されました。
- 新機能の`MaxTextRecallSize`と`countAndFacetMode`が強調され、ハイブリッド検索での結果数制御が可能となっています。

## Breaking changes
- 特記すべき破壊的変更はありませんが、既存の設定やリンクが更新されており、それに伴う理解の再確認が必要です。

## Other updates
- ドキュメントの日付が多く更新され、コンテンツの最新性が保たれています。
- APIキーに関するセキュリティ設定と関連するベストプラクティスが明確化されています。
- C# チュートリアルで使用される.NETバージョンが更新され、.NET 6から.NET 9にアップデートされています。

# Insights
このドキュメントのマイナーアップデートは、Azure AI Searchにおけるユーザー体験を向上させるための戦略的な改善です。特に、ユーザーがAPIを効果的に活用するためのガイダンスが強化されています。

例えば、`maxTextRecallSize`パラメータに関する更新は、ハイブリッド検索における検索結果の精度向上を目指したものであり、開発者がシステムのパフォーマンスと結果の関連性をより細かく制御できるようにしています。これにより、適切なチューニングが可能となり、期待される検索結果を得ることが容易になります。

ベクトル検索での`threshold`の追加により、低関連スコアの結果を排除し、ユーザーに提供される検索結果の質を向上させる取り組みも見られます。これらの機能拡張は、特に大量のデータを扱う企業にとって、結果の精度を高めるための重要なアプローチとなるでしょう。

また、APIキーやセキュリティに関するドキュメントの見直しは、クラウド環境でのセキュリティ強化に対する関心の高まりを反映したものです。ロールベースのアクセス制御やMicrosoft Entra IDの利用が推奨される背景には、クラウドサービスにおけるセキュリティの重要性の再認識があります。

このように、アップデートによって、Azure AI Searchを活用する技術者は、より実用的でセキュアな方法でシステムを構築できるようになっています。日付やリンクの更新は、信頼性を確保するための標準的なメンテナンスであり、常に最新の情報にアクセスすることの重要性を再確認させます。これらすべての改良が、開発者の生産性向上と、より優れた検索ソリューションの提供に結びつくでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [hybrid-search-how-to-query.md](#item-345ce6) | minor update | ハイブリッド検索におけるテキストリコールサイズの設定に関する文書の更新 | modified | 6 | 4 | 10 | 
| [hybrid-search-ranking.md](#item-dad887) | minor update | ハイブリッド検索のランキングに関するドキュメントの微修正 | modified | 1 | 1 | 2 | 
| [index-add-custom-analyzers.md](#item-11325e) | minor update | カスタムアナライザーのドキュメントの更新 | modified | 18 | 18 | 36 | 
| [index-add-language-analyzers.md](#item-004ac0) | minor update | 言語アナライザーのドキュメント日付の更新 | modified | 1 | 1 | 2 | 
| [index-similarity-and-scoring.md](#item-75603d) | minor update | 類似性およびスコアリングに関するドキュメントの更新 | modified | 4 | 2 | 6 | 
| [search-analyzers.md](#item-9dccd9) | minor update | 検索アナライザーに関するドキュメントの更新 | modified | 3 | 3 | 6 | 
| [search-api-preview.md](#item-511f5d) | minor update | 検索APIプレビューに関するドキュメントの更新 | modified | 1 | 1 | 2 | 
| [search-api-versions.md](#item-69ca3e) | minor update | Azure AI Search APIバージョンに関するドキュメントの更新 | modified | 17 | 19 | 36 | 
| [search-faceted-navigation.md](#item-f29d1e) | minor update | ファセットナビゲーションに関するドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [search-faq-frequently-asked-questions.yml](#item-eab2ba) | minor update | FAQドキュメントの内容更新と日付変更 | modified | 6 | 6 | 12 | 
| [search-howto-concurrency.md](#item-863358) | minor update | 同時実行性に関するドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [search-howto-index-json-blobs.md](#item-b8230c) | minor update | JSON Blobインデクシングに関するドキュメントの日付更新と文言修正 | modified | 3 | 5 | 8 | 
| [search-howto-managed-identities-storage.md](#item-8209c4) | minor update | マネージドアイデンティティに関するドキュメントの更新 | modified | 9 | 9 | 18 | 
| [search-indexer-troubleshooting.md](#item-087365) | minor update | インデクサートラブルシューティングに関するドキュメントの更新 | modified | 14 | 4 | 18 | 
| [search-pagination-page-layout.md](#item-115902) | minor update | ページネーションに関するドキュメントのリンク更新 | modified | 1 | 1 | 2 | 
| [search-performance-analysis.md](#item-5032b3) | minor update | パフォーマンス分析に関するドキュメントの更新 | modified | 11 | 11 | 22 | 
| [search-security-api-keys.md](#item-d8c908) | minor update | API キーによる認証に関するドキュメントの更新 | modified | 13 | 12 | 25 | 
| [search-security-enable-roles.md](#item-4985c4) | minor update | ロールベースのアクセス制御に関するドキュメントの更新 | modified | 11 | 15 | 26 | 
| [search-security-rbac.md](#item-a5d129) | minor update | 役割ベースのアクセス制御に関する制限事項の削除 | modified | 0 | 6 | 6 | 
| [tutorial-csharp-create-load-index.md](#item-0a6ffd) | minor update | C# チュートリアルの更新日付の変更 | modified | 1 | 1 | 2 | 
| [tutorial-csharp-deploy-static-web-app.md](#item-a2300f) | minor update | C# チュートリアルの更新日付の変更 | modified | 1 | 1 | 2 | 
| [tutorial-csharp-overview.md](#item-57fa0d) | minor update | C# チュートリアルのバージョンアップデート | modified | 2 | 2 | 4 | 
| [tutorial-csharp-search-query-integration.md](#item-8ad6b5) | minor update | C# 検索クエリ統合チュートリアルの日付更新 | modified | 1 | 1 | 2 | 
| [vector-search-how-to-query.md](#item-9bb93c) | minor update | ベクトル検索クエリ統合チュートリアルの文書更新 | modified | 4 | 4 | 8 | 
| [whats-new.md](#item-fa71b4) | minor update | 新機能および改善点の追加 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/hybrid-search-how-to-query.md{#item-345ce6}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,7 @@ In this article, learn how to:
 
 + [vector.queries.weight](vector-search-how-to-query.md#vector-weighting) lets you set the relative weight of the vector query. This feature is particularly useful in complex queries where two or more distinct result sets need to be combined, as is the case for hybrid search. This feature is generally available.
 
-+ [hybridsearch.maxTextRecallSize and countAndFacetMode (preview)](#set-maxtextrecallsize-and-countandfacetmode-preview) give you more control over text inputs into a hybrid query. This feature requires a preview API version.
++ [hybridsearch.maxTextRecallSize and countAndFacetMode (preview)](#set-maxtextrecallsize-and-countandfacetmode) give you more control over text inputs into a hybrid query. This feature requires a preview API version.
  -->
 ## Prerequisites
 
@@ -44,7 +44,7 @@ In this article, learn how to:
 
 + Search Explorer in the Azure portal (supports both stable and preview API search syntax) has a JSON view that lets you paste in a hybrid request.
 
-+ [**2024-07-01**](/rest/api/searchservice/documents/search-post) stable version or a recent preview API version if you're using preview features like [maxTextRecallSize and countAndFacetMode(preview)](#set-maxtextrecallsize-and-countandfacetmode-preview).
++ [**2024-07-01**](/rest/api/searchservice/documents/search-post) stable version or a recent preview API version if you're using preview features like [maxTextRecallSize and countAndFacetMode(preview)](#set-maxtextrecallsize-and-countandfacetmode).
 
   For readability, we use REST examples to explain how the APIs work. You can use a REST client like Visual Studio Code with the REST extension to build hybrid queries. For more information, see [Quickstart: Vector search using REST APIs](search-get-started-vector.md).
 
@@ -310,7 +310,9 @@ api-key: {{admin-api-key}}
 
 + Postfilter is applied after query execution. If k=50 returns 50 matches on the vector query side, followed by a post-filter applied to the 50 matches, your results are reduced by the number of documents that meet filter criteria. This leaves you with fewer than 50 documents to pass to semantic ranker. Keep this in mind if you're using semantic ranking. The semantic ranker works best if it has 50 documents as input.
 
-## Set maxTextRecallSize and countAndFacetMode (preview)
+## Set maxTextRecallSize and countAndFacetMode
+
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
 This section explains how to adjust the inputs to a hybrid query by controlling the amount BM25-ranked results that flow to the hybrid ranking model. Controlling over the BM25-ranked input gives you more options for relevance tuning in hybrid scenarios.
 
@@ -407,7 +409,7 @@ A query might match to any number of documents, as many as all of them if the se
 Both "k" and "top" are optional. Unspecified, the default number of results in a response is 50. You can set "top" and "skip" to [page through more results](search-pagination-page-layout.md#paging-results) or change the default.
 
 > [!NOTE]
-> If you're using hybrid search in 2024-05-01-preview API, you can control the number of results from the keyword query using [maxTextRecallSize](#set-maxtextrecallsize-and-countandfacetmode-preview). Combine this with a setting for "k" to control the representation from each search subsystem (keyword and vector).
+> If you're using hybrid search in 2024-05-01-preview API, you can control the number of results from the keyword query using [maxTextRecallSize](#set-maxtextrecallsize-and-countandfacetmode). Combine this with a setting for "k" to control the representation from each search subsystem (keyword and vector).
 
 #### Semantic ranker results
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索におけるテキストリコールサイズの設定に関する文書の更新"
}
```

### Explanation
この変更は、ハイブリッド検索に関するドキュメント内でのいくつかのマイナーな修正を示しています。具体的には、`maxTextRecallSize` や `countAndFacetMode` の分野における操作を説明するセクションが更新され、プレビューや安定版のAPIバージョンに関する情報が整理されました。また、セクション見出しやリンク先の変更が反映され、説明がより明確になります。

さらに、ハイブリッド検索に関連する特徴や機能についての文言を改善し、ユーザーがAPIの使用方法を理解しやすくしています。その結果、ドキュメントの全体的な可読性と利便性が向上しています。これにより、開発者が特定の機能を効果的に活用できるようになります。

## articles/search/hybrid-search-ranking.md{#item-dad887}

<details>
<summary>Diff</summary>
````diff
@@ -135,7 +135,7 @@ In this example, the @search.score (weighted) values are passed to the RRF ranki
 
 By default, if you aren't using pagination, the search engine returns the top 50 highest ranking matches for full text search, and the most similar `k` matches for vector search. In a hybrid query, `top` determines the number of results in the response. Based on defaults, the top 50 highest ranked matches of the unified result set are returned. 
 
-Often, the search engine finds more results than `top` and `k`. To return more results, use the paging parameters `top`, `skip`, and `next`. Paging is how you determine the number of results on each logical page and navigate through the full payload. You can set `maxTextRecallSize` to larger values (the default is 1,000) to return more results from the text side of hybrid query.
+Often, the search engine finds more results than `top` and `k`. To return more results, use the paging parameters `top`, `skip`, and `next`. Paging is how you determine the number of results on each logical page and navigate through the full payload. You can [set `maxTextRecallSize`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) to larger values (the default is 1,000) to return more results from the text side of hybrid query.
 
 By default, full text search is subject to a maximum limit of 1,000 matches (see [API response limits](search-limits-quotas-capacity.md#api-response-limits)). Once 1,000 matches are found, the search engine no longer looks for more.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索のランキングに関するドキュメントの微修正"
}
```

### Explanation
この変更は、ハイブリッド検索のランキングに関するドキュメントの一部に対するマイナーな修正を示しています。具体的には、`maxTextRecallSize` の設定方法に関する情報がリンク形式で追加され、ユーザーがこの機能に関する詳細を容易に参照できるようになりました。

変更された内容の要点は、検索エンジンがデフォルトで返す結果の数に関する説明が強調されている点です。特に、`maxTextRecallSize` を設定することで、ハイブリッドクエリからより多くの結果を取得できることが明記されています。この修正により、ユーザーはハイブリッド検索の機能をより効果的に活用できるようになります。全体として、情報の明確性とユーザビリティの向上が図られています。

## articles/search/index-add-custom-analyzers.md{#item-11325e}

<details>
<summary>Diff</summary>
````diff
@@ -9,20 +9,20 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 05/23/2024
+ms.date: 01/16/2025
 ---
 
 # Add custom analyzers to string fields in an Azure AI Search index
 
-A *custom analyzer* is a user-defined combination of one tokenizer, one or more token filters, and one or more character filters. A custom analyzer is specified within a search index, and then referenced by name on field definitions that require custom analysis. A custom analyzer is invoked on a per-field basis. Attributes on the field will determine whether it's used for indexing, queries, or both.
+A *custom analyzer* is a component of lexical analysis over plain text content. It's a user-defined combination of one tokenizer, one or more token filters, and one or more character filters. A custom analyzer is specified within a search index, and then referenced by name on field definitions that require custom analysis. A custom analyzer is invoked on a per-field basis. Attributes on the field determine whether it's used for indexing, queries, or both.
 
-In a custom analyzer, character filters prepare the input text before it's processed by the tokenizer (for example, removing markup). Next, the tokenizer breaks text into tokens. Finally, token filters modify the tokens emitted by the tokenizer. For concepts and examples, see [Analyzers in Azure AI Search](search-analyzers.md).
+In a custom analyzer, character filters prepare the input text before it's processed by the tokenizer (for example, removing markup). Next, the tokenizer breaks text into tokens. Finally, token filters modify the tokens emitted by the tokenizer. For concepts and examples, see [Analyzers in Azure AI Search](search-analyzers.md) and [Tutorial: Create a custom analyzer for phone numbers](tutorial-create-custom-analyzer.md).
 
 ## Why use a custom analyzer?
 
-A custom analyzer gives you control over the process of converting text into indexable and searchable tokens by allowing you to choose which types of analysis or filtering to invoke, and the order in which they occur. 
+A custom analyzer gives you control over the process of converting plain text into indexable and searchable tokens by allowing you to choose which types of analysis or filtering to invoke, and the order in which they occur. 
 
-Create and assign a custom analyzer if none of default (Standard Lucence), built-in, or language analyzers are sufficient for your needs. You might also create a custom analyzer if you want to use a built-in analyzer with custom options. For example, if you wanted to change the maxTokenLength on Standard, you would create a custom analyzer, with a user-defined name, to set that option.
+Create and assign a custom analyzer if none of default (Standard Lucene), built-in, or language analyzers are sufficient for your needs. You might also create a custom analyzer if you want to use a built-in analyzer with custom options. For example, if you wanted to change the `maxTokenLength` on Standard Lucene, you would create a custom analyzer, with a user-defined name, to set that option.
 
 Scenarios where custom analyzers can be helpful include:
 
@@ -39,15 +39,15 @@ Scenarios where custom analyzers can be helpful include:
 - ASCII folding. Add the Standard ASCII folding filter to normalize diacritics like ö or ê in search terms.  
 
 > [!NOTE]  
-> Custom analyzers aren't exposed in the Azure portal. The only way to add a custom analyzer is through code that defines an index. 
+> Custom analyzers aren't exposed in the Azure portal. The only way to add a custom analyzer is through code that [creates an index schema](/rest/api/searchservice/indexes/create-or-update).
 
 ## Create a custom analyzer
 
 To create a custom analyzer, specify it in the `analyzers` section of an index at design time, and then reference it on searchable, `Edm.String` fields using either the `analyzer` property, or the `indexAnalyzer` and `searchAnalyzer` pair.
 
 An analyzer definition includes a name, type, one or more character filters, a maximum of one tokenizer, and one or more token filters for post-tokenization processing. Character filters are applied before tokenization. Token filters and character filters are applied from left to right.
 
-- Names in a custom analyzer must be unique and can't be the same as any of the built-in analyzers, tokenizers, token filters, or characters filters. Names consist of letters, digits, spaces, dashes or underscores. Names must start and end with plain text characters. Names must be under 128 characters in length.
+- Names in a custom analyzer must be unique and can't be the same as any of the built-in analyzers, tokenizers, token filters, or characters filters. Names consist of letters, digits, spaces, dashes, or underscores. Names must start and end with plain text characters. Names must be under 128 characters in length.
 
 - Type must be #Microsoft.Azure.Search.CustomAnalyzer.
 
@@ -224,7 +224,7 @@ Azure AI Search supports character filters in the following list. More informati
 |[mapping](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/charfilter/MappingCharFilter.html)|MappingCharFilter|A char filter that applies mappings defined with the mappings option. Matching is greedy (longest pattern matching at a given point wins). Replacement is allowed to be the empty string.  <br><br>**Options**  <br><br> mappings (type: string array) - A list of mappings of the following format: `a=>b` (all occurrences of the character `a` are replaced with character `b`). Required.|  
 |[pattern_replace](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/pattern/PatternReplaceCharFilter.html)|PatternReplaceCharFilter|A char filter that replaces characters in the input string. It uses a regular expression to identify character sequences to preserve and a replacement pattern to identify characters to replace. For example, input text = `aa  bb aa bb`, pattern=`(aa)\\\s+(bb)` replacement=`$1#$2`, result = `aa#bb aa#bb`.  <br><br>**Options**  <br><br>pattern (type: string) - Required.  <br><br>replacement (type: string) - Required.|  
 
- <sup>1</sup> Char Filter Types are always prefixed in code with `#Microsoft.Azure.Search` such that `MappingCharFilter` would actually be specified as `#Microsoft.Azure.Search.MappingCharFilter`. We removed the prefix to reduce the width of the table, but please remember to include it in your code. Notice that char_filter_type is only provided for filters that can be customized. If there are no options, as is the case with html_strip, there's no associated #Microsoft.Azure.Search type.
+ <sup>1</sup> Char Filter Types are always prefixed in code with `#Microsoft.Azure.Search` such that `MappingCharFilter` would actually be specified as `#Microsoft.Azure.Search.MappingCharFilter`. We removed the prefix to reduce the width of the table, but remember to include it in your code. Notice that char_filter_type is only provided for filters that can be customized. If there are no options, as is the case with html_strip, there's no associated #Microsoft.Azure.Search type.
 
 <a name="tokenizers"></a>
 
@@ -237,40 +237,40 @@ Azure AI Search supports tokenizers in the following list. More information abou
 |**tokenizer_name**|**tokenizer_type** <sup>1</sup>|**Description and Options**|  
 |------------------|-------------------------------|---------------------------|  
 |[classic](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/standard/ClassicTokenizer.html)|ClassicTokenizer|Grammar based tokenizer that is suitable for processing most European-language documents.  <br><br>**Options**  <br><br>maxTokenLength (type: int) - The maximum token length. Default: 255, maximum: 300. Tokens longer than the maximum length are split.|  
-|[edgeNGram](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ngram/EdgeNGramTokenizer.html)|EdgeNGramTokenizer|Tokenizes the input from an edge into n-grams of given size(s).  <br><br> **Options**  <br><br>minGram (type: int) - Default: 1, maximum: 300.  <br><br>maxGram (type: int) - Default: 2, maximum: 300. Must be greater than minGram.  <br><br>tokenChars (type: string array) - Character classes to keep in the tokens. Allowed values: <br>`letter`, `digit`, `whitespace`, `punctuation`, `symbol`. Defaults to an empty array - keeps all characters. |  
+|[edgeNGram](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ngram/EdgeNGramTokenizer.html)|EdgeNGramTokenizer|Tokenizes the input from an edge into n-grams of given sizes.  <br><br> **Options**  <br><br>minGram (type: int) - Default: 1, maximum: 300.  <br><br>maxGram (type: int) - Default: 2, maximum: 300. Must be greater than minGram.  <br><br>tokenChars (type: string array) - Character classes to keep in the tokens. Allowed values: <br>`letter`, `digit`, `whitespace`, `punctuation`, `symbol`. Defaults to an empty array - keeps all characters. |  
 |[keyword_v2](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/core/KeywordTokenizer.html)|KeywordTokenizerV2|Emits the entire input as a single token.  <br><br>**Options**  <br><br>maxTokenLength (type: int) - The maximum token length. Default: 256, maximum: 300. Tokens longer than the maximum length are split.|  
 |[letter](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/core/LetterTokenizer.html)|(type applies only when options are available)  |Divides text at non-letters. Tokens that are longer than 255 characters are split.|  
 |[lowercase](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/core/LowerCaseTokenizer.html)|(type applies only when options are available)  |Divides text at non-letters and converts them to lower case. Tokens that are longer than 255 characters are split.|  
 | microsoft_language_tokenizer| MicrosoftLanguageTokenizer| Divides text using language-specific rules.  <br><br>**Options**  <br><br>maxTokenLength (type: int) - The maximum token length, default: 255, maximum: 300. Tokens longer than the maximum length are split. Tokens longer than 300 characters are first split into tokens of length 300 and then each of those tokens is split based on the maxTokenLength set.  <br><br>isSearchTokenizer (type: bool) - Set to true if used as the search tokenizer, set to false if used as the indexing tokenizer. <br><br>language (type: string) - Language to use, default `english`. Allowed values include: <br>`bangla`, `bulgarian`, `catalan`, `chineseSimplified`,  `chineseTraditional`, `croatian`, `czech`, `danish`, `dutch`, `english`,  `french`, `german`, `greek`, `gujarati`, `hindi`, `icelandic`, `indonesian`, `italian`, `japanese`, `kannada`, `korean`, `malay`, `malayalam`, `marathi`, `norwegianBokmaal`, `polish`, `portuguese`, `portugueseBrazilian`, `punjabi`, `romanian`, `russian`, `serbianCyrillic`, `serbianLatin`, `slovenian`, `spanish`, `swedish`, `tamil`, `telugu`, `thai`, `ukrainian`, `urdu`, `vietnamese` |
 | microsoft_language_stemming_tokenizer | MicrosoftLanguageStemmingTokenizer| Divides text using language-specific rules and reduces words to their base forms. This tokenizer performs lemmatization. <br><br>**Options** <br><br>maxTokenLength (type: int) - The maximum token length, default: 255, maximum: 300. Tokens longer than the maximum length are split. Tokens longer than 300 characters are first split into tokens of length 300 and then each of those tokens is split based on the maxTokenLength set. <br><br> isSearchTokenizer (type: bool) - Set to true if used as the search tokenizer, set to false if used as the indexing tokenizer. <br><br>language (type: string) - Language to use, default `english`. Allowed values include: <br>`arabic`, `bangla`, `bulgarian`, `catalan`, `croatian`, `czech`, `danish`, `dutch`, `english`, `estonian`, `finnish`, `french`, `german`, `greek`, `gujarati`, `hebrew`, `hindi`, `hungarian`, `icelandic`, `indonesian`, `italian`, `kannada`, `latvian`, `lithuanian`, `malay`, `malayalam`, `marathi`, `norwegianBokmaal`, `polish`, `portuguese`, `portugueseBrazilian`, `punjabi`, `romanian`, `russian`, `serbianCyrillic`, `serbianLatin`, `slovak`, `slovenian`, `spanish`, `swedish`, `tamil`, `telugu`, `turkish`, `ukrainian`, `urdu` |
-|[nGram](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ngram/NGramTokenizer.html)|NGramTokenizer|Tokenizes the input into n-grams of the given size(s). <br><br>**Options** <br><br>minGram (type: int) - Default: 1, maximum: 300. <br><br>maxGram (type: int) - Default: 2, maximum: 300. Must be greater than minGram. <br><br>tokenChars (type: string array) - Character classes to keep in the tokens. Allowed values: `letter`, `digit`, `whitespace`, `punctuation`, `symbol`. Defaults to an empty array - keeps all characters. |  
+|[nGram](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ngram/NGramTokenizer.html)|NGramTokenizer|Tokenizes the input into n-grams of the given sizes. <br><br>**Options** <br><br>minGram (type: int) - Default: 1, maximum: 300. <br><br>maxGram (type: int) - Default: 2, maximum: 300. Must be greater than minGram. <br><br>tokenChars (type: string array) - Character classes to keep in the tokens. Allowed values: `letter`, `digit`, `whitespace`, `punctuation`, `symbol`. Defaults to an empty array - keeps all characters. |  
 |[path_hierarchy_v2](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/path/PathHierarchyTokenizer.html)|PathHierarchyTokenizerV2|Tokenizer for path-like hierarchies. **Options** <br><br>delimiter (type: string) - Default: '/. <br><br>replacement (type: string) - If set, replaces the delimiter character. Default same as the value of delimiter. <br><br>maxTokenLength (type: int) -  The maximum token length. Default: 300, maximum: 300. Paths longer than maxTokenLength are ignored. <br><br>reverse (type: bool) - If true, generates token in reverse order. Default: false. <br><br>skip (type: bool) - Initial tokens to skip. The default is 0.|  
 |[pattern](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/pattern/PatternTokenizer.html)|PatternTokenizer|This tokenizer uses regex pattern matching to construct distinct tokens. <br><br>**Options** <br><br> [pattern](https://docs.oracle.com/javase/6/docs/api/java/util/regex/Pattern.html) (type: string) - Regular expression pattern to match token separators. The default is `\W+`, which matches non-word characters. <br><br>[flags](https://docs.oracle.com/javase/6/docs/api/java/util/regex/Pattern.html#field_summary) (type: string) - Regular expression flags. The default is an empty string. Allowed values: CANON_EQ, CASE_INSENSITIVE, COMMENTS, DOTALL, LITERAL, MULTILINE, UNICODE_CASE, UNIX_LINES <br><br>group (type: int) - Which group to extract into tokens. The default is -1 (split).|
 |[standard_v2](https://lucene.apache.org/core/6_6_1/core/org/apache/lucene/analysis/standard/StandardTokenizer.html)|StandardTokenizerV2|Breaks text following the [Unicode Text Segmentation rules](https://unicode.org/reports/tr29/). <br><br>**Options** <br><br>maxTokenLength (type: int) - The maximum token length. Default: 255, maximum: 300. Tokens longer than the maximum length are split.|  
 |[uax_url_email](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/standard/UAX29URLEmailTokenizer.html)|UaxUrlEmailTokenizer|Tokenizes urls and emails as one token. <br><br>**Options** <br><br> maxTokenLength (type: int) - The maximum token length. Default: 255, maximum: 300. Tokens longer than the maximum length are split.|  
 |[whitespace](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/core/WhitespaceTokenizer.html)|(type applies only when options are available) |Divides text at whitespace. Tokens that are longer than 255 characters are split.|  
 
- <sup>1</sup> Tokenizer Types are always prefixed in code with `#Microsoft.Azure.Search` such that  `ClassicTokenizer` would actually be specified as `#Microsoft.Azure.Search.ClassicTokenizer`. We removed the prefix to reduce the width of the table, but please remember to include it in your code. Notice that tokenizer_type is only provided for tokenizers that can be customized. If there are no options, as is the case with the letter tokenizer, there's no associated #Microsoft.Azure.Search type.
+ <sup>1</sup> Tokenizer Types are always prefixed in code with `#Microsoft.Azure.Search` such that  `ClassicTokenizer` would actually be specified as `#Microsoft.Azure.Search.ClassicTokenizer`. We removed the prefix to reduce the width of the table, but remember to include it in your code. Notice that tokenizer_type is only provided for tokenizers that can be customized. If there are no options, as is the case with the letter tokenizer, there's no associated #Microsoft.Azure.Search type.
 
 <a name="TokenFilters"></a>
 
 ## Token filters
 
 A token filter is used to filter out or modify the tokens generated by a tokenizer. For example, you can specify a lowercase filter that converts all characters to lowercase. You can have multiple token filters in a custom analyzer. Token filters run in the order in which they're listed.
 
-In the table below, the token filters that are implemented using Apache Lucene are linked to the Lucene API documentation.
+In the following table, the token filters that are implemented using Apache Lucene are linked to the Lucene API documentation.
 
 |**token_filter_name**|**token_filter_type** <sup>1</sup>|**Description and Options**|  
 |-|-|-|  
 |[arabic_normalization](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ar/ArabicNormalizationFilter.html)|(type applies only when options are available)  |A token filter that applies the Arabic normalizer to normalize the orthography.|  
 |[apostrophe](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/tr/ApostropheFilter.html)|(type applies only when options are available)  |Strips all characters after an apostrophe (including the apostrophe itself). |  
 |[asciifolding](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/miscellaneous/ASCIIFoldingFilter.html)|AsciiFoldingTokenFilter|Converts alphabetic, numeric, and symbolic Unicode characters which aren't in the first 127 ASCII characters (the `Basic Latin` Unicode block) into their ASCII equivalents, if one exists.<br><br> **Options**<br><br> preserveOriginal (type: bool) - If true, the original token is kept. The default is false.|  
 |[cjk_bigram](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/cjk/CJKBigramFilter.html)|CjkBigramTokenFilter|Forms bigrams of CJK terms that are generated from StandardTokenizer.<br><br> **Options**<br><br> ignoreScripts (type: string array) - Scripts to ignore. Allowed values include: `han`, `hiragana`, `katakana`, `hangul`. The default is an empty list.<br><br> outputUnigrams (type: bool) - Set to true if you always want to output both unigrams and bigrams. The default is false.|  
-|[cjk_width](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/cjk/CJKWidthFilter.html)|(type applies only when options are available)  |Normalizes CJK width differences. Folds full width ASCII variants into the equivalent basic latin and half-width Katakana variants into the equivalent kana. |  
+|[cjk_width](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/cjk/CJKWidthFilter.html)|(type applies only when options are available)  |Normalizes CJK width differences. Folds full width ASCII variants into the equivalent basic Latin and half-width Katakana variants into the equivalent kana. |  
 |[classic](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/standard/ClassicFilter.html)|(type applies only when options are available)  |Removes the English possessives, and dots from acronyms. |  
 |[common_grams](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/commongrams/CommonGramsFilter.html)|CommonGramTokenFilter|Construct bigrams for frequently occurring terms while indexing. Single terms are still indexed too, with bigrams overlaid.<br><br> **Options**<br><br> commonWords (type: string array) - The set of common words. The default is an empty list. Required.<br><br> ignoreCase (type: bool) - If true, matching is case insensitive. The default is false.<br><br> queryMode (type: bool) - Generates bigrams then removes common words and single terms followed by a common word. The default is false.|  
 |[dictionary_decompounder](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/compound/DictionaryCompoundWordTokenFilter.html)|DictionaryDecompounderTokenFilter|Decomposes compound words found in many Germanic languages.<br><br> **Options**<br><br> wordList (type: string array) - The list of words to match against. The default is an empty list. Required.<br><br> minWordSize (type: int) - Only words longer than this will be processed. The default is 5.<br><br> minSubwordSize (type: int) - Only subwords longer than this will be outputted. The default is 2.<br><br> maxSubwordSize (type: int) - Only subwords shorter than this will be outputted. The default is 15.<br><br> onlyLongestMatch (type: bool) - Add only the longest matching subword to output. The default is false.|  
-|[edgeNGram_v2](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ngram/EdgeNGramTokenFilter.html)|EdgeNGramTokenFilterV2|Generates n-grams of the given size(s) from starting from the front or the back of an input token.<br><br> **Options**<br><br> minGram (type: int) - Default: 1, maximum: 300.<br><br> maxGram (type: int) - Default: 2, maximum 300. Must be greater than minGram.<br><br> side (type: string) - Specifies which side of the input the n-gram should be generated from. Allowed values: `front`, `back` |  
+|[edgeNGram_v2](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ngram/EdgeNGramTokenFilter.html)|EdgeNGramTokenFilterV2|Generates n-grams of the given sizes from starting from the front or the back of an input token.<br><br> **Options**<br><br> minGram (type: int) - Default: 1, maximum: 300.<br><br> maxGram (type: int) - Default: 2, maximum 300. Must be greater than minGram.<br><br> side (type: string) - Specifies which side of the input the n-gram should be generated from. Allowed values: `front`, `back` |  
 |[elision](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/util/ElisionFilter.html)|ElisionTokenFilter|Removes elisions. For example, `l'avion` (the plane) is converted to `avion` (plane).<br><br> **Options**<br><br> articles (type: string array) - A set of articles to remove. The default is an empty list. If there's no list of articles set, by default all French articles are removed.|  
 |[german_normalization](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/de/GermanNormalizationFilter.html)|(type applies only when options are available)  |Normalizes German characters according to the heuristics of the [German2 snowball algorithm](https://snowballstem.org/algorithms/german2/stemmer.html) .|  
 |[hindi_normalization](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/hi/HindiNormalizationFilter.html)|(type applies only when options are available)  |Normalizes text in Hindi to remove some differences in spelling variations. |  
@@ -282,7 +282,7 @@ In the table below, the token filters that are implemented using Apache Lucene a
 |[length](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/miscellaneous/LengthFilter.html)|LengthTokenFilter|Removes words that are too long or too short.<br><br> **Options**<br><br> min (type: int) - The minimum number. Default: 0, maximum: 300.<br><br> max (type: int) - The maximum number. Default: 300, maximum: 300.|  
 |[limit](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/miscellaneous/LimitTokenCountFilter.html)|Microsoft.Azure.Search.LimitTokenFilter|Limits the number of tokens while indexing.<br><br> **Options**<br><br> maxTokenCount (type: int) - Max number of tokens to produce. The default is 1.<br><br> consumeAllTokens (type: bool) - Whether all tokens from the input must be consumed even if maxTokenCount is reached. The default is false.|  
 |[lowercase](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/core/LowerCaseFilter.html)|(type applies only when options are available)  |Normalizes token text to lower case. |  
-|[nGram_v2](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ngram/NGramTokenFilter.html)|NGramTokenFilterV2|Generates n-grams of the given size(s).<br><br> **Options**<br><br> minGram (type: int) - Default: 1, maximum: 300.<br><br> maxGram (type: int) - Default: 2, maximum 300. Must be greater than minGram.|  
+|[nGram_v2](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ngram/NGramTokenFilter.html)|NGramTokenFilterV2|Generates n-grams of the given sizes.<br><br> **Options**<br><br> minGram (type: int) - Default: 1, maximum: 300.<br><br> maxGram (type: int) - Default: 2, maximum 300. Must be greater than minGram.|  
 |[pattern_capture](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/pattern/PatternCaptureGroupTokenFilter.html)|PatternCaptureTokenFilter|Uses Java regexes to emit multiple tokens, one for each capture group in one or more patterns.<br><br> **Options**<br><br> patterns (type: string array) - A list of patterns to match against each token. Required.<br><br> preserveOriginal (type: bool) - Set to true to return the original token even if one of the patterns matches, default: true |  
 |[pattern_replace](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/pattern/PatternReplaceFilter.html)|PatternReplaceTokenFilter|A token filter which applies a pattern to each token in the stream, replacing match occurrences with the specified replacement string.<br><br> **Options**<br><br> pattern (type: string) - Required.<br><br> replacement (type: string) - Required.|  
 |[persian_normalization](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/fa/PersianNormalizationFilter.html)|(type applies only when options are available) |Applies normalization for Persian. |  
@@ -291,20 +291,20 @@ In the table below, the token filters that are implemented using Apache Lucene a
 |[reverse](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/reverse/ReverseStringFilter.html)|(type applies only when options are available)  |Reverses the token string. |  
 |[scandinavian_normalization](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/miscellaneous/ScandinavianNormalizationFilter.html)|(type applies only when options are available)  |Normalizes use of the interchangeable Scandinavian characters. |  
 |[scandinavian_folding](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/miscellaneous/ScandinavianFoldingFilter.html)|(type applies only when options are available)  |Folds Scandinavian characters `åÅäæÄÆ`into `a` and `öÖøØ`into `o`. It also discriminates against use of double vowels `aa`, `ae`, `ao`, `oe` and `oo`, leaving just the first one. |  
-|[shingle](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/shingle/ShingleFilter.html)|ShingleTokenFilter|Creates combinations of tokens as a single token.<br><br> **Options**<br><br> maxShingleSize (type: int) - Defaults to 2.<br><br> minShingleSize (type: int) - Defaults to 2.<br><br> outputUnigrams (type: bool) - if true, the output stream contains the input tokens (unigrams) as well as shingles. The default is true.<br><br> outputUnigramsIfNoShingles (type: bool) - If true, override the behavior of outputUnigrams==false for those times when no shingles are available. The default is false.<br><br> tokenSeparator (type: string) - The string to use when joining adjacent tokens to form a shingle. The default is a single empty space ` `. <br><br> filterToken (type: string) - The string to insert for each position for which there is no token. The default is `_`.|  
+|[shingle](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/shingle/ShingleFilter.html)|ShingleTokenFilter|Creates combinations of tokens as a single token.<br><br> **Options**<br><br> maxShingleSize (type: int) - Defaults to 2.<br><br> minShingleSize (type: int) - Defaults to 2.<br><br> outputUnigrams (type: bool) - if true, the output stream contains the input tokens (unigrams) as well as shingles. The default is true.<br><br> outputUnigramsIfNoShingles (type: bool) - If true, override the behavior of outputUnigrams==false for those times when no shingles are available. The default is false.<br><br> tokenSeparator (type: string) - The string to use when joining adjacent tokens to form a shingle. The default is a single empty space ` `. <br><br> filterToken (type: string) - The string to insert for each position for which there's no token. The default is `_`.|  
 |[snowball](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/snowball/SnowballFilter.html)|SnowballTokenFilter|Snowball Token Filter.<br><br> **Options**<br><br> language (type: string) - Allowed values include: `armenian`, `basque`, `catalan`, `danish`, `dutch`, `english`, `finnish`, `french`, `german`, `german2`, `hungarian`, `italian`, `kp`, `lovins`, `norwegian`, `porter`, `portuguese`, `romanian`, `russian`, `spanish`, `swedish`, `turkish`|  
 |[sorani_normalization](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ckb/SoraniNormalizationFilter.html)|SoraniNormalizationTokenFilter|Normalizes the Unicode representation of `Sorani` text.<br><br> **Options**<br><br> None.|  
 |stemmer|StemmerTokenFilter|Language-specific stemming filter.<br><br> **Options**<br><br> language (type: string) - Allowed values include: <br> -   [`arabic`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ar/ArabicStemmer.html)<br>-   [`armenian`](https://snowballstem.org/algorithms/armenian/stemmer.html)<br>-   [`basque`](https://snowballstem.org/algorithms/basque/stemmer.html)<br>-   [`brazilian`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/br/BrazilianStemmer.html)<br>-   `bulgarian`<br>-   [`catalan`](https://snowballstem.org/algorithms/catalan/stemmer.html)<br>-   [`czech`](https://portal.acm.org/citation.cfm?id=1598600)<br>-   [`danish`](https://snowballstem.org/algorithms/danish/stemmer.html)<br>-   [`dutch`](https://snowballstem.org/algorithms/dutch/stemmer.html)<br>-   [`dutchKp`](https://snowballstem.org/algorithms/kraaij_pohlmann/stemmer.html)<br>-   [`english`](https://snowballstem.org/algorithms/porter/stemmer.html)<br>-   [`lightEnglish`](https://ciir.cs.umass.edu/pubfiles/ir-35.pdf)<br>-   [`minimalEnglish`](https://www.researchgate.net/publication/220433848_How_effective_is_suffixing)<br>-   [`possessiveEnglish`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/en/EnglishPossessiveFilter.html)<br>-   [`porter2`](https://snowballstem.org/algorithms/english/stemmer.html)<br>-   [`lovins`](https://snowballstem.org/algorithms/lovins/stemmer.html)<br>-   [`finnish`](https://snowballstem.org/algorithms/finnish/stemmer.html)<br>-   `lightFinnish`<br>-   [`french`](https://snowballstem.org/algorithms/french/stemmer.html)<br>-   [`lightFrench`](https://dl.acm.org/citation.cfm?id=1141523)<br>-   [`minimalFrench`](https://dl.acm.org/citation.cfm?id=318984)<br>-   `galician`<br>-   `minimalGalician`<br>-   [`german`](https://snowballstem.org/algorithms/german/stemmer.html)<br>-   [`german2`](https://snowballstem.org/algorithms/german2/stemmer.html)<br>-   [`lightGerman`](https://dl.acm.org/citation.cfm?id=1141523)<br>-   `minimalGerman`<br>-   [`greek`](https://sais.se/mthprize/2007/ntais2007.pdf)<br>-   `hindi`<br>-   [`hungarian`](https://snowballstem.org/algorithms/hungarian/stemmer.html)<br>-   [`lightHungarian`](https://dl.acm.org/citation.cfm?id=1141523&dl=ACM&coll=DL&CFID=179095584&CFTOKEN=80067181)<br>-   [`indonesian`](https://eprints.illc.uva.nl/741/2/MoL-2003-03.text.pdf)<br>-   [`irish`](https://snowballstem.org/algorithms/irish/stemmer.html)<br>-   [`italian`](https://snowballstem.org/algorithms/italian/stemmer.html)<br>-   [`lightItalian`](https://www.ercim.eu/publication/ws-proceedings/CLEF2/savoy.pdf)<br>-   [`sorani`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ckb/SoraniStemmer.html)<br>-   [`latvian`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/lv/LatvianStemmer.html)<br>-   [`norwegian`](https://snowballstem.org/algorithms/norwegian/stemmer.html)<br>-   [`lightNorwegian`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/no/NorwegianLightStemmer.html)<br>-   [`minimalNorwegian`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/no/NorwegianMinimalStemmer.html)<br>-   [`lightNynorsk`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/no/NorwegianLightStemmer.html)<br>-   [`minimalNynorsk`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/no/NorwegianMinimalStemmer.html)<br>-   [`portuguese`](https://snowballstem.org/algorithms/portuguese/stemmer.html)<br>-   [`lightPortuguese`](https://dl.acm.org/citation.cfm?id=1141523&dl=ACM&coll=DL&CFID=179095584&CFTOKEN=80067181)<br>-   [`minimalPortuguese`](https://web.archive.org/web/20230425141918/https://www.inf.ufrgs.br/~buriol/papers/Orengo_CLEF07.pdf)<br>-   [`portugueseRslp`](https://web.archive.org/web/20230422082818/https://www.inf.ufrgs.br/~viviane/rslp/index.htm)<br>-   [`romanian`](https://snowballstem.org/otherapps/romanian/)<br>-   [`russian`](https://snowballstem.org/algorithms/russian/stemmer.html)<br>-   [`lightRussian`](https://doc.rero.ch/lm.php?url=1000%2C43%2C4%2C20091209094227-CA%2FDolamic_Ljiljana_-_Indexing_and_Searching_Strategies_for_the_Russian_20091209.pdf)<br>-   [`spanish`](https://snowballstem.org/algorithms/spanish/stemmer.html)<br>-   [`lightSpanish`](https://www.ercim.eu/publication/ws-proceedings/CLEF2/savoy.pdf)<br>-   [`swedish`](https://snowballstem.org/algorithms/swedish/stemmer.html)<br>-   `lightSwedish`<br>-   [`turkish`](https://snowballstem.org/algorithms/turkish/stemmer.html)|  
 |[stemmer_override](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/miscellaneous/StemmerOverrideFilter.html)|StemmerOverrideTokenFilter|Any dictionary-Stemmed terms are marked as keywords, which prevents stemming down the chain. Must be placed before any stemming filters.<br><br> **Options**<br><br> rules (type: string array) - Stemming rules in the following format `word => stem` for example `ran => run`. The default is an empty list.  Required.|  
 |[stopwords](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/core/StopFilter.html)|StopwordsTokenFilter|Removes stop words from a token stream. By default, the filter uses a predefined stop word list for English.<br><br> **Options**<br><br> stopwords (type: string array) - A list of stopwords. Can't be specified if a stopwordsList is specified.<br><br> stopwordsList (type: string) - A predefined list of stopwords. Can't be specified if `stopwords` is specified. Allowed values include:`arabic`, `armenian`, `basque`, `brazilian`, `bulgarian`, `catalan`, `czech`, `danish`, `dutch`, `english`, `finnish`, `french`, `galician`, `german`, `greek`, `hindi`, `hungarian`, `indonesian`, `irish`, `italian`, `latvian`, `norwegian`, `persian`, `portuguese`, `romanian`, `russian`, `sorani`, `spanish`, `swedish`, `thai`, `turkish`, default: `english`. Can't be specified if `stopwords` is specified. <br><br> ignoreCase (type: bool) - If true, all words are lower cased first. The default is false.<br><br> removeTrailing (type: bool) - If true, ignore the last search term if it's a stop word. The default is true.
-|[synonym](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/synonym/SynonymFilter.html)|SynonymTokenFilter|Matches single or multi word synonyms in a token stream.<br><br> **Options**<br><br> synonyms (type: string array) - Required. List of synonyms in one of the following two formats:<br><br> -incredible, unbelievable, fabulous => amazing - all terms on the left side of => symbol are replaced with all terms on its right side.<br><br> -incredible, unbelievable, fabulous, amazing - A comma-separated list of equivalent words. Set the expand option to change how this list is interpreted.<br><br> ignoreCase (type: bool) - Case-folds input for matching. The default is false.<br><br> expand (type: bool) - If true, all words in the list of synonyms (if => notation is not used) map to one another. <br>The following list: incredible, unbelievable, fabulous, amazing is equivalent to: incredible, unbelievable, fabulous, amazing => incredible, unbelievable, fabulous, amazing<br><br>- If false, the following list: incredible, unbelievable, fabulous, amazing are equivalent to: incredible, unbelievable, fabulous, amazing => incredible.|  
+|[synonym](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/synonym/SynonymFilter.html)|SynonymTokenFilter|Matches single or multi word synonyms in a token stream.<br><br> **Options**<br><br> synonyms (type: string array) - Required. List of synonyms in one of the following two formats:<br><br> -incredible, unbelievable, fabulous => amazing - all terms on the left side of => symbol are replaced with all terms on its right side.<br><br> -incredible, unbelievable, fabulous, amazing - A comma-separated list of equivalent words. Set the expand option to change how this list is interpreted.<br><br> ignoreCase (type: bool) - Case-folds input for matching. The default is false.<br><br> expand (type: bool) - If true, all words in the list of synonyms (if => notation isn't used) map to one another. <br>The following list: incredible, unbelievable, fabulous, amazing is equivalent to: incredible, unbelievable, fabulous, amazing => incredible, unbelievable, fabulous, amazing<br><br>- If false, the following list: incredible, unbelievable, fabulous, amazing are equivalent to: incredible, unbelievable, fabulous, amazing => incredible.|  
 |[trim](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/miscellaneous/TrimFilter.html)|(type applies only when options are available)  |Trims leading and trailing whitespace from tokens. |  
 |[truncate](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/miscellaneous/TruncateTokenFilter.html)|TruncateTokenFilter|Truncates the terms into a specific length.<br><br> **Options**<br><br> length (type: int) - Default: 300, maximum: 300. Required.|  
 |[unique](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/miscellaneous/RemoveDuplicatesTokenFilter.html)|UniqueTokenFilter|Filters out tokens with same text as the previous token.<br><br> **Options**<br><br> onlyOnSamePosition (type: bool) - If set, remove duplicates only at the same position. The default is true.|  
 |[uppercase](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/core/UpperCaseFilter.html)|(type applies only when options are available)  |Normalizes token text to upper case. |  
 |[word_delimiter](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/miscellaneous/WordDelimiterFilter.html)|WordDelimiterTokenFilter|Splits words into subwords and performs optional transformations on subword groups.<br><br> **Options**<br><br> generateWordParts (type: bool) - Causes parts of words to be generated, for example `AzureSearch` becomes `Azure` `Search`. The default is true.<br><br> generateNumberParts (type: bool) - Causes number subwords to be generated. The default is true.<br><br> catenateWords (type: bool) - Causes maximum runs of word parts to be catenated, for example `Azure-Search` becomes `AzureSearch`. The default is false.<br><br> catenateNumbers (type: bool) - Causes maximum runs of number parts to be catenated, for example `1-2` becomes `12`. The default is false.<br><br> catenateAll (type: bool) - Causes all subword parts to be catenated, e.g `Azure-Search-1` becomes `AzureSearch1`. The default is false.<br><br> splitOnCaseChange (type: bool) - If true, splits words on caseChange, for example `AzureSearch` becomes `Azure` `Search`. The default is true.<br><br> preserveOriginal - Causes original words to be preserved and added to the subword list. The default is false.<br><br> splitOnNumerics (type: bool) - If true, splits on numbers, for example `Azure1Search` becomes `Azure` `1` `Search`. The default is true.<br><br> stemEnglishPossessive (type: bool) - Causes trailing `'s` to be removed for each subword. The default is true.<br><br> protectedWords (type: string array) - Tokens to protect from being delimited. The default is an empty list.|  
 
- <sup>1</sup> Token Filter Types are always prefixed in code with `#Microsoft.Azure.Search` such that  `ArabicNormalizationTokenFilter` would actually be specified as `#Microsoft.Azure.Search.ArabicNormalizationTokenFilter`.  We removed the prefix to reduce the width of the table, but please remember to include it in your code.  
+ <sup>1</sup> Token Filter Types are always prefixed in code with `#Microsoft.Azure.Search` such that  `ArabicNormalizationTokenFilter` would actually be specified as `#Microsoft.Azure.Search.ArabicNormalizationTokenFilter`.  We removed the prefix to reduce the width of the table, but remember to include it in your code.  
 
 ## See also
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムアナライザーのドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるカスタムアナライザーのドキュメントの一部を更新した内容です。主に、コンテンツの表現を改善し、新しいリファレンスリンクを追加することで、情報の明確性を向上させています。

具体的には、カスタムアナライザーの定義に関する説明が少し拡張され、特にその目的や使用法に関する情報が強化されました。新たに、カスタムアナライザーを使用するための具体的なチュートリアルへのリンクも追加され、ユーザーが実践的に学べるように配慮されています。

また、文書の日付も更新され、最新の情報を反映しています。これにより、開発者がカスタムアナライザーを効果的に使用できるようになり、ドキュメント全体の信頼性と使いやすさが向上しています。

## articles/search/index-add-language-analyzers.md{#item-004ac0}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 05/23/2024
+ms.date: 01/16/2025
 ---
 
 # Add language analyzers to string fields in an Azure AI Search index
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語アナライザーのドキュメント日付の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける言語アナライザーを文字列フィールドに追加する方法についてのドキュメントの日付を更新したものです。具体的には、ドキュメントの日付が2024年5月23日から2025年1月16日に変更されています。

このような日付の更新は、ドキュメントの最新性を保つために重要であり、利用者が提供された情報が最新であることを確認できるようにしています。また、今後の利用者にとって、アナライザーの機能や使い方が現在の状況を反映したものであることを示す助けにもなります。全体として、文書の信頼性と関連性が向上したと言えます。

## articles/search/index-similarity-and-scoring.md{#item-75603d}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 12/10/2024
+ms.date: 01/17/2025
 ---
 
 # Relevance in keyword search (BM25 scoring)
@@ -117,7 +117,7 @@ POST https://[service name].search.windows.net/indexes/hotels/docs/search?api-ve
 As long as the same `sessionId` is used, a best-effort attempt is made to target the same replica, increasing the consistency of results your users will see. 
 
 > [!NOTE]
-> Reusing the same `sessionId` values repeatedly can interfere with the load balancing of the requests across replicas and adversely affect the performance of the search service. The value used as sessionId cannot start with a '_' character.
+> Reusing the same `sessionId` values repeatedly can interfere with the load balancing of the requests across replicas and adversely affect the performance of the search service. The value used as sessionId can't start with a '_' character.
 
 ## Relevance tuning
 
@@ -172,6 +172,8 @@ The featuresMode parameter isn't documented in the REST APIs, but you can use it
 
 By default, if you aren't using pagination, the search engine returns the top 50 highest ranking matches for full text search. You can use the `top` parameter to return a smaller or larger number of items (up to 1,000 in a single response). You can use `skip` and `next` to page results. Paging determines the number of results on each logical page and supports content navigation. For more information, see [Shape search results](search-pagination-page-layout.md).
 
+If your full text query is part of a [hybrid query](hybrid-search-how-to-query.md), you can [set `maxTextRecallSize`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) to increase or decrease the number of results from the text side of the query.
+
 Full text search is subject to a maximum limit of 1,000 matches (see [API response limits](search-limits-quotas-capacity.md#api-response-limits)). Once 1,000 matches are found, the search engine no longer looks for more.
 
 ## See also
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "類似性およびスコアリングに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchの「類似性とスコアリング」に関するドキュメントに対するもので、主に以下の点が更新されています。

1. ドキュメントの日付が2024年12月10日から2025年1月17日に変更され、情報の最新性が保たれています。
2. `sessionId`に関する注意事項が強調され、一部の表現が言い換えられていますが、内容は変わっていません。これにより、ユーザーが`sessionId`の使用法をより理解しやすくなっています。
3. 新たに、フルテキスト検索がハイブリッドクエリの一部である場合に`maxTextRecallSize`というパラメータを設定することで、検索結果の数を調整できるという情報が追加されました。

これらの変更は、Azure AI Searchの利用者が検索の精度を考慮しながら機能を最大限に活用できるようにするためのものであり、全体としてドキュメントの明確性と有用性を向上させています。

## articles/search/search-analyzers.md{#item-9dccd9}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 05/23/2024
+ms.date: 01/16/2025
 ms.custom:
   - devx-track-csharp
   - ignite-2023
@@ -22,9 +22,9 @@ An *analyzer* is a component of the [full text search engine](search-lucene-quer
 + Lower-case any upper-case words
 + Reduce words into primitive root forms for storage efficiency and so that matches can be found regardless of tense
 
-Analysis applies to `Edm.String` fields that are marked as "searchable", which indicates full text search. 
+The output of a lexical analyzer is a sequence of [tokens](https://suif.stanford.edu/dragonbook/lecture-notes/Stanford-CS143/03-Lexical-Analysis.pdf).
 
-For fields of this configuration, analysis occurs during indexing when tokens are created, and then again during query execution when queries are parsed and the engine scans for matching tokens. A match is more likely to occur when the same analyzer is used for both indexing and queries, but you can set the analyzer for each workload independently, depending on your requirements.
+Lexical analysis applies to `Edm.String` fields that are marked as "searchable", which indicates full text search. For fields of this configuration, analysis occurs during indexing when tokens are created, and then again during query execution when queries are parsed and the engine scans for matching tokens. A match is more likely to occur when the same analyzer is used for both indexing and queries, but you can set the analyzer for each workload independently, depending on your requirements.
 
 Query types that are *not* full text search, such as filters or fuzzy search, don't go through the analysis phase on the query side. Instead, the parser sends those strings directly to the search engine, using the pattern that you provide as the basis for the match. Typically, these query forms require whole-string tokens to make pattern matching work. To ensure whole term tokens are preserved during indexing, you might need [custom analyzers](index-add-custom-analyzers.md). For more information about when and why query terms are analyzed, see [Full text search in Azure AI Search](search-lucene-query-architecture.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索アナライザーに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける検索アナライザーに関するドキュメントの更新です。主に次のような修正が行われました。

1. ドキュメントの日付が2024年5月23日から2025年1月16日に変更され、情報が最新のものとなっています。
2. `analyzer`に関連する説明の内容が一部修正されました。具体的には、レキシカルアナライザーの出力が「トークンのシーケンス」であるという情報が追加され、アナライザーについての理解が深まるように書き直されています。
3. `Edm.String`フィールドにおける分析の適用についての表現も整理され、分析がインデックス作成時とクエリ実行時の両方で行われることが明確化されています。

これらの変更により、検索アナライザーの動作や設定の重要性がよりわかりやすく説明され、ユーザーが検索機能を適切に活用するための情報が強化されています。全体として、ドキュメントの品質と信頼性が向上しています。

## articles/search/search-api-preview.md{#item-511f5d}

<details>
<summary>Diff</summary>
````diff
@@ -50,7 +50,7 @@ Preview features are removed from this list if they're retired or transition to
 | [**Normalizers**](search-normalizers.md) | Query |  Normalizers provide simple text preprocessing: consistent casing, accent removal, and ASCII folding, without invoking the full text analysis chain.| [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
 | [**featuresMode parameter**](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true) | Relevance (scoring) | BM25 relevance score expansion to include details: per field similarity score, per field term frequency, and per field number of unique tokens matched. You can consume these data points in [custom scoring solutions](https://github.com/Azure-Samples/search-ranking-tutorial). | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true).|
 | [**vectorQueries.threshold parameter**](vector-search-how-to-query.md#vector-weighting) | Relevance (scoring)  | Exclude low-scoring search result based on a minimum score. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
-| [**hybridSearch.maxTextRecallSize and countAndFacetMode parameters**](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview) | Relevance (scoring)  |  adjust the inputs to a hybrid query by controlling the amount BM25-ranked results that flow to the hybrid ranking model.  | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
+| [**hybridSearch.maxTextRecallSize and countAndFacetMode parameters**](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) | Relevance (scoring)  |  adjust the inputs to a hybrid query by controlling the amount BM25-ranked results that flow to the hybrid ranking model.  | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
 | [**moreLikeThis**](search-more-like-this.md) | Query | Finds documents that are relevant to a specific document. This feature has been in earlier previews. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
 
 ## Control plane preview features
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索APIプレビューに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける検索APIプレビューに関するドキュメントの一部修正で、主に以下の点が更新されています。

1. `hybridSearch.maxTextRecallSize`および`countAndFacetMode`パラメータの説明に対する修正が行われ、ハイブリッド検索での入力の調整に関する情報が整備されています。特に、説明文が明確化され、より正確な情報を提供するようになっています。
2. 文中でのパラメータリンクの修正が行われ、ドキュメントとしての整合性が保たれています。

これにより、利用者が検索APIをより理解しやすくなり、ハイブリッドクエリにおける設定の重要性が強調されています。この変更は、ユーザーが機能を効果的に活用するための情報を提供し、ドキュメント全体の質の向上に寄与しています。

## articles/search/search-api-versions.md{#item-69ca3e}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: conceptual
-ms.date: 06/24/2024
+ms.date: 01/16/2025
 ---
 
 # API versions in Azure AI Search
@@ -57,33 +57,31 @@ Support for the above-listed versions ended on October 15, 2020. If you have cod
 
 The following  table provides links to more recent SDK versions. 
 
-| SDK version | Status | Description |
-|-------------|--------|------------------------------|
-| [Azure.Search.Documents 11](/dotnet/api/overview/azure/search.documents-readme) | Active | New client library from the Azure .NET SDK team, initially released July 2020. See the [Change Log](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Search.Documents_11.3.0/sdk/search/Azure.Search.Documents/CHANGELOG.md) for information about minor releases. |
-| [Microsoft.Azure.Search 10](https://www.nuget.org/packages/Microsoft.Azure.Search/) | Retired | Released May 2019. This is the last version of the Microsoft.Azure.Search package and it's now deprecated. It's succeeded by Azure.Search.Documents. |
-| [Microsoft.Azure.Management.Search 4.0.0](https://www.nuget.org/packages/Microsoft.Azure.Management.Search/4.0.0) | Active | Targets the Management REST api-version=2020-08-01. |
-| [Microsoft.Azure.Management.Search 3.0.0](https://www.nuget.org/packages/Microsoft.Azure.Management.Search/3.0.0) | Retired | Targets the Management REST api-version=2015-08-19.  |
+| SDK version | Status | Change log | Description |
+|-------------|--------|------------ |-----------------|
+| [Azure.Search.Documents 11](/dotnet/api/overview/azure/search.documents-readme) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | APIs for data plane operations on a service, such as read-write operations on content and objects. |
+| [Azure.ResourceManager.Search](https://www.nuget.org/packages/Microsoft.Azure.Management.Search/4.0.0) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.ResourceManager.Search/CHANGELOG.md) | APIs for control plane operations on the search service. |
 
 ## Azure SDK for Java
 
-| SDK version | Status | Description  |
-|-------------|--------|------------------------------|
-| [Java azure-search-documents 11](/java/api/overview/azure/search-documents-readme) | Active | Use the `azure-search-documents` client library for data plane operations. |
-| [Java Management Client 1.35.0](/java/api/overview/azure/search/management) | Active | Use the `azure-mgmt-search` client library for control plane operations. |
+| SDK version | Status | Change log | Description |
+|-------------|--------|------------|-----------------|
+| [azure-search-documents 11](/java/api/overview/azure/search-documents-readme) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) Use the `azure-search-documents` client library for data plane operations. |
+| [azure-resourcemanager-search 2](/java/api/overview/azure/resourcemanager-search-readme) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/resourcemanager/azure-resourcemanager-search/CHANGELOG.md) | Use the `azure-resourcemanager-search` client library for control plane operations. |
 
 ## Azure SDK for JavaScript
 
-| SDK version | Status | Description  |
-|-------------|--------|------------------------------|
-| [JavaScript @azure/search-documents 11.0](/javascript/api/overview/azure/search-documents-readme) | Active | Use the `@azure/search-documents` client library for data plane operations. |
-| [JavaScript @azure/arm-search](https://www.npmjs.com/package/@azure/arm-search) | Active | Use the `@azure/arm-search` client library for control plane operations. |
+| SDK version | Status | Change log | Description |
+|-------------|--------|------------|------------------|
+| [@azure/search-documents 12](/javascript/api/overview/azure/search-documents-readme) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | Use the `@azure/search-documents` client library for data plane operations. |
+| [@azure/arm-search 4](/javascript/api/overview/azure/arm-search-readme) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/arm-search/CHANGELOG.md) | Use the `@azure/arm-search` package for control plane operations. |
 
 ## Azure SDK for Python
 
-| SDK version | Status | Description  |
-|-------------|--------|------------------------------|
-| [Python azure-search-documents 11.0](/python/api/azure-search-documents) | Active | Use the `azure-search-documents` client library for data plane operations. |
-| [Python azure-mgmt-search 8.0](https://pypi.org/project/azure-mgmt-search/) | Active | Use the `azure-mgmt-search` client library for control plane operations. |
+| SDK version | Status | Change log | Description |
+|-------------|--------|------------|------------------|
+| [azure-search-documents 11](/python/api/overview/azure/search-documents-readme) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | Use the `azure-search-documents` client library for data plane operations. |
+| [azure-mgmt-search 9](https://pypi.org/project/azure-mgmt-search/) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-mgmt-search/CHANGELOG.md) | Use the `azure-mgmt-search` client library for control plane operations. |
 
 ## All Azure SDKs
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search APIバージョンに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI SearchのAPIバージョンに関するドキュメントの修正で、主に以下のポイントが更新されています。

1. ドキュメントの日付が2024年6月24日から2025年1月16日に変更され、最新情報が反映されています。
2. SDKバージョンの情報が整理され、各SDKに対するリンクが更新され、変更履歴（Change Log）へのリンクが追加されています。これにより、ユーザーは新しいクライアントライブラリやその変更履歴に簡単にアクセスできるようになっています。
3. 各SDKの説明が見直され、よりわかりやすい内容に修正されています。特にデータプレーンとコントロールプレーンの操作に関する情報が明確になり、ユーザーがそれぞれのSDKの機能を理解しやすくなっています。

これらの更新により、Azure AI Searchの利用者が最新のSDK情報を容易に取得し、快適に開発を進めることが可能となっています。全体として、ドキュメントの信頼性と有用性が向上しています。

## articles/search/search-faceted-navigation.md{#item-f29d1e}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 10/31/2024
+ms.date: 01/16/2025
 ---
 
 # Add faceted navigation to a search app
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファセットナビゲーションに関するドキュメントの日付更新"
}
```

### Explanation
この変更は、ファセットナビゲーションに関するドキュメントの最終更新日を変更するもので、具体的には次の点が修正されています。

1. ドキュメントの日付が2024年10月31日から2025年1月16日に更新されました。この変更は、情報の新しさを反映し、利用者に最新の情報を提供することを目的としています。

全体として、この変更は式用情報に対する信頼性を向上させ、ユーザーがより正確な日時に基づいて参照できるようになっています。ファセットナビゲーションの具体的な内容や使い方は変更されていないものの、ドキュメントの整合性が保たれています。

## articles/search/search-faq-frequently-asked-questions.yml{#item-eab2ba}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ metadata:
   ms.author: heidist
   ms.service: azure-ai-search
   ms.topic: faq
-  ms.date: 05/28/2024
+  ms.date: 01/16/2025
 title: Azure AI Search Frequently Asked Questions
 summary:  Find answers to commonly asked questions about Azure AI Search.
 
@@ -36,7 +36,7 @@ sections:
         answer: |
           For vectors, the embedding models you use determines the linguistic experience. 
           
-          For nonvector strings and numbers, the default analyzer used for tokenization is standard Lucene and it is language agnostic. Otherwise, language support is expressed through [language analyzers](index-add-language-analyzers.md#supported-language-analyzers) that apply linguistic rules to inbound (indexing) and outbound (queries) content. Some features, such as [speller](speller-how-to-add.md#supported-languages), are limited to a subset of languages.
+          For nonvector strings and numbers, the default analyzer used for tokenization is standard Lucene and it's language agnostic. Otherwise, language support is expressed through [language analyzers](index-add-language-analyzers.md#supported-language-analyzers) that apply linguistic rules to inbound (indexing) and outbound (queries) content. Some features, such as [speller](speller-how-to-add.md#supported-languages) and [query rewrite](semantic-how-to-query-rewrite.md), are limited to a subset of languages.
 
       - question: |
           How do I integrate search into my solution?
@@ -101,12 +101,12 @@ sections:
       - question: |
           Does Azure AI Search support vector search?
         answer: |
-          Azure AI Search supports vector indexing and retrieval. It can vectorize query strings and content if you use the preview and beta libraries. 
+          Azure AI Search supports vector indexing and retrieval. It can chunk and vectorize query strings and content if you use [integrated vectorization](vector-search-integrated-vectorization.md) and take a dependency on indexers and skillsets. 
 
       - question: |
           How does vector search work in Azure AI Search?
         answer: |
-          With standalone vector search, you first use an embedding model to transform content into a vector representation within an embedding space. You can then provide these vectors in a document payload to the search index for indexing. To serve search requests, you use the same deep neural network (DNN) from indexing to transform the search query into a vector representation, and vector search finds the most similar vectors and return the corresponding documents.
+          With standalone vector search, you first use an embedding model to transform content into a vector representation within an embedding space. You can then provide these vectors in a document payload to the search index for indexing. To serve search requests, you use the same embedding model to transform the search query into a vector representation, and vector search finds the most similar vectors and return the corresponding documents.
           
           In Azure AI Search, you can index vector data as fields in documents alongside textual and other types of content. There are [multiple data types](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields) for vector fields. 
           
@@ -130,7 +130,7 @@ sections:
       - question: |
           Why do I see different vector index size limits between my new search services and existing search services?
         answer: |
-          We're rolling out improved vector index size limits worldwide for new search services, but we're still building out infrastructure capacity in certain regions. New search services created in supported regions will see increased vector index size limits. Unfortunately, we can't migrate existing services to the new limits.
+          Azure AI Search rolled out improved vector index size limits worldwide for new search services, but [some regions experience capacity constraints](search-region-support.md), and some regions don't have the required infrastructure. New search services created in supported regions should see increased vector index size limits. Unfortunately, we can't migrate existing services to the new limits. Also, only vector indexes that use the Hierarchical Navigable Small World (HNSW) algorithm report on vector index size in the Azure portal. If your index uses exhaustive KNN, vector index size is reported as zero, even though the index contains vectors. 
 
       - question: |
           How do I enable vector search on a search index?
@@ -141,7 +141,7 @@ sections:
           
           * Add a "vectorSearch" section to the index schema specifying the configuration used by vector search fields, including the parameters of the Approximate Nearest Neighbor algorithm used, like HNSW.
           
-          * Use the latest stable version[**2024-07-01**](/rest/api/searchservice), or an Azure SDK to create or update the index, load documents, and issue queries.
+          * Use the latest stable version[**2024-07-01**](/rest/api/searchservice), or an Azure SDK to create or update the index, load documents, and issue queries. For more information, see [Create a vector index](vector-search-how-to-create-index.md).
 
   - name: Queries
     questions:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQドキュメントの内容更新と日付変更"
}
```

### Explanation
この変更は、Azure AI Searchに関するよくある質問（FAQ）を含むドキュメントの修正で、以下の主なポイントが更新されています。

1. **更新日付の変更**: ドキュメントの最終更新日が2024年5月28日から2025年1月16日に更新され、情報の鮮度が保持されています。

2. **内容の修正**: 
   - 特定の質問への回答において、`speller`や`query rewrite`のような機能が含まれていることに言及し、それぞれの機能が特定の言語に制限されていることを明確化しました。
   - ベクター検索に関連する質問の回答で、`integrated vectorization`への言及が追加され、どのようにベクターデータが処理されるかに関する詳細が強化されました。
   - もう一つの修正では、ベクターインデックスのサイズ制限について、地域によるインフラ制約に関する詳しい説明が追加されています。

これにより、ユーザーはAzure AI Searchの仕組みやベクター検索に関する最新情報をより深く理解できるようになります。また、FAQが執筆された時期に関する信頼性が向上し、利用者に対して有用なリソースとなることが期待されます。

## articles/search/search-howto-concurrency.md{#item-863358}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 04/23/2024
+ms.date: 01/16/2025
 ms.custom:
   - devx-track-csharp
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "同時実行性に関するドキュメントの日付更新"
}
```

### Explanation
この変更は、同時実行性に関するドキュメントの日付を更新するもので、以下のポイントが含まれています。

1. **更新日付の変更**: ドキュメントの最終更新日が2024年4月23日から2025年1月16日へと変更されました。この更新は、ユーザーに最新の情報を提供し、文書がより新しい状態であることを保証します。

この変更は、技術的な内容は変更されていないものの、ドキュメントの整合性と信頼性を向上させ、利用者が最新の情報を基にアクセスできるようにするための重要な更新です。同時実行性に関する情報が引き続き有用であることを示しています。

## articles/search/search-howto-index-json-blobs.md{#item-b8230c}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 06/25/2024
+ms.date: 01/16/2025
 ---
 
 # Index JSON blobs and files in Azure AI Search
@@ -39,7 +39,6 @@ Within the indexer definition, you can optionally set [field mappings](search-in
 > [!NOTE]
 > When a JSON parsing mode is used, Azure AI Search assumes that all blobs use the same parser (either for **`json`**, **`jsonArray`** or **`jsonLines`**). If you have a mix of different file types in the same data source, consider using [file extension filters](search-blob-storage-integration.md#controlling-which-blobs-are-indexed) to control which files are imported.
 
-
 The following sections describe each mode in more detail. If you're unfamiliar with indexer clients and concepts, see [Create a search indexer](search-howto-create-indexers.md). You should also be familiar with the details of [basic blob indexer configuration](search-howto-indexing-azure-blob-storage.md), which isn't repeated here.
 
 <a name="parsing-single-blobs"></a>
@@ -76,8 +75,7 @@ api-key: [admin key]
 ```
 
 > [!NOTE]
-> As with all indexers, if fields do not clearly match, you should expect to explicitly specify individual [field mappings](search-indexer-field-mappings.md) unless you are using the implicit fields mappings available for blob content and metadata, as described in [basic blob indexer configuration](search-howto-indexing-azure-blob-storage.md).
-
+> As with all indexers, if fields don't clearly match, you should expect to explicitly specify individual [field mappings](search-indexer-field-mappings.md) unless you're using the implicit fields mappings available for blob content and metadata, as described in [basic blob indexer configuration](search-howto-indexing-azure-blob-storage.md).
 
 ### json example (single hotel JSON files)
 
@@ -208,7 +206,7 @@ You can also refer to individual array elements by using a zero-based index. For
 ```
 
 > [!NOTE]
-> If "sourceFieldName" refers to a property that doesn't exist in the JSON blob, that mapping is skipped without an error. This behavior allows indexing to continue for JSON blobs that have a different schema (which is a common use case). Because there is no validation check, check the mappings carefully for typos so that you aren't losing documents for the wrong reason.
+> If "sourceFieldName" refers to a property that doesn't exist in the JSON blob, that mapping is skipped without an error. This behavior allows indexing to continue for JSON blobs that have a different schema (which is a common use case). Because there's no validation check, check the mappings carefully for typos so that you aren't losing documents for the wrong reason.
 >
 
 ## Next steps
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JSON Blobインデクシングに関するドキュメントの日付更新と文言修正"
}
```

### Explanation
この変更は、Azure AI SearchにおけるJSON Blobのインデクシングに関するドキュメントに対する微調整で、以下の内容が含まれています。

1. **更新日付の変更**: ドキュメントの最終更新日が2024年6月25日から2025年1月16日に変更され、ユーザーに新しい情報を提供することが目的です。

2. **文言の修正**:
   - 特定の注意書きの表現が一貫して改善され、より自然な言い回しに変更されました。例えば、`"you should expect to explicitly specify individual field mappings"`の部分が、`"you're using the implicit fields mappings"`という表現に更新されました。
   - 一部の文章から不要な改行を削除し、全体的な文章の流れを滑らかにしています。

これにより、ドキュメントはより読みやすくなり、ユーザーはJSON Blobのインデクシングに関する情報を効率的に得られるようになります。この更新は技術文書の整合性と分かりやすさを向上させるための重要な手段です。

## articles/search/search-howto-managed-identities-storage.md{#item-8209c4}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ manager: nitinme
 
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/03/2024
+ms.date: 01/16/2025
 ms.custom:
   - subject-rbac-steps
   - ignite-2023
@@ -43,9 +43,9 @@ You can use a system-assigned managed identity or a user-assigned managed identi
    | ADLS Gen2 indexing using an indexer | Add **Storage Blob Data Reader** |
    | Table indexing using an indexer | Add **Reader and Data Access** |
    | File indexing using an indexer | Add **Reader and Data Access** |
-   | Write to a knowledge store | Add **Storage Blob DataContributor** for object and file projections, and **Reader and Data Access** for table projections. |
-   | Write to an enrichment cache | Add **Storage Blob Data Contributor**  |
-   | Save debug session state | Add **Storage Blob Data Contributor**  |
+   | Write to a [knowledge store](knowledge-store-concept-intro.md) | Add **Storage Blob Data Contributor** for object and file projections, and **Reader and Data Access** for table projections. |
+   | Write to an [enrichment cache](cognitive-search-incremental-indexing-conceptual.md) | Add **Storage Blob Data Contributor**  |
+   | Save [debug session state](cognitive-search-debug-session.md) | Add **Storage Blob Data Contributor**  |
 
 1. Select **Next**.
 
@@ -59,7 +59,7 @@ You can use a system-assigned managed identity or a user-assigned managed identi
 
 Once you have a role assignment, you can set up a connection to Azure Storage that operates under that role.
 
-Indexers use a data source object for connections to an external data source. This section explains how to specify a system-assigned managed identity or a user-assigned managed identity on a data source connection string. You can find more [connection string examples](search-howto-managed-identities-data-sources.md#connection-string-examples) in the managed identity article.
+[Indexers](search-indexer-overview.md) use a data source object for connections to an external data source. This section explains how to specify a system-assigned managed identity or a user-assigned managed identity on a data source connection string. You can find more [connection string examples](search-howto-managed-identities-data-sources.md#connection-string-examples) in the managed identity article.
 
 > [!TIP]
 > You can create a data source connection to Azure Storage in the Azure portal, specifying either a system or user-assigned managed identity, and then view the JSON definition to see how the connection string is formulated.
@@ -70,7 +70,7 @@ You must have a [system-assigned managed identity already configured](search-how
 
 For connections made using a system-assigned managed identity, the only change to the [data source definition](/rest/api/searchservice/data-sources/create) is the format of the `credentials` property. 
 
-Provide a `ResourceId` that has no account key or password. The `ResourceId` must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name.
+Provide a connection string that contains a `ResourceId`, with no account key or password. The `ResourceId` must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name.
 
 ```http
 POST https://[service name].search.windows.net/datasources?api-version=2024-07-01
@@ -91,11 +91,11 @@ POST https://[service name].search.windows.net/datasources?api-version=2024-07-0
 
 You must have a [user-assigned managed identity already configured](search-howto-managed-identities-data-sources.md) and associated with your search service, and the identity must have a role-assignment on Azure Storage. 
 
-Connections made through user-assigned managed identities use the same credentials as a system-assigned managed identity, plus an extra identity property that contains the collection of user-assigned managed identities. Only one user-assigned managed identity should be provided when creating the data source. Set `userAssignedIdentity` to the user-assigned managed identity.
+Connections made through user-assigned managed identities use the same credentials as a system-assigned managed identity, plus an extra identity property that contains the collection of user-assigned managed identities. Only one user-assigned managed identity should be provided when creating the data source. 
 
-Provide a `ResourceId` that has no account key or password. The `ResourceId` must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name.
+Provide a connection string that contains a `ResourceId`, with no account key or password. The `ResourceId` must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name.
 
-Provide an `identity` using the syntax shown in the following example.
+Provide an `identity` using the syntax shown in the following example. Set `userAssignedIdentity` to the user-assigned managed identity.
 
 ```http
 POST https://[service name].search.windows.net/datasources?api-version=2024-07-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージドアイデンティティに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるマネージドアイデンティティのストレージ設定に関するドキュメントの更新であり、以下の内容が含まれています。

1. **更新日付の変更**: ドキュメントの最終更新日が2024年6月3日から2025年1月16日に変更され、最新の情報を反映させています。

2. **文言の修正**:
   - 手順や説明文中の一部の用語が具体化され、情報の明確化が図られています。例えば、「Write to a knowledge store」に関するセクションでは、リンクが追加され、関連する情報へのアクセスが容易になっています。
   - "ResourceId"に関連する説明が、「Provide a connection string that contains a `ResourceId`」という形で具体的に更新され、より正確な情報を提供しています。
   - 他のセクションでも文を整理し、変数名や説明が統一されることで、読みやすさが向上しています。

これにより、ユーザーはマネージドアイデンティティを使用したAzure Storageの接続設定に関する手順をより容易に理解でき、関連情報へのリンクを通じて必要なリソースにアクセスしやすくなります。この更新は、文書全体の整合性と明確性を向上させるための重要な改善です。

## articles/search/search-indexer-troubleshooting.md{#item-087365}

<details>
<summary>Diff</summary>
````diff
@@ -25,6 +25,16 @@ Occasionally, indexers run into problems that don't produce errors or that occur
 
 For data sources under Azure network security, indexers are limited in how they make the connection. Currently, indexers can access restricted data sources [behind an IP firewall](search-indexer-howto-access-ip-restricted.md) or on a virtual network through a [private endpoint](search-indexer-howto-access-private.md) using a shared private link.
 
+### Error connecting to Azure AI services on a private connection
+
+If you get an error code 403 with the following message, you might have a problem with how the resource endpoint is specified in a skillset:
+
+* `"A Virtual Network is configured for this resource. Please use the correct endpoint for making requests. Check https://aka.ms/cogsvc-vnet for more details."`
+
+This error occurs if you have [configured a shared private link](search-indexer-howto-access-private.md) for connections to Azure AI multi-service, and the endpoint is missing a custom subdomain. A custom subdomain is the first part of the endpoint (for example, `http://my-custom-subdomain.cognitiveservices.azure.com`). A custom domain might be missing if you created the resource in Azure AI Foundry.
+
+If the Azure AI multi-service account isn't in the same region as Azure AI Search, [use a keyless connection](cognitive-search-attach-cognitive-services.md) when attaching a billable Azure AI resource.
+
 ### Firewall rules
 
 Azure Storage, Azure Cosmos DB and Azure SQL provide a configurable firewall. There's no specific error message when the firewall blocks the request. Typically, firewall errors are generic. Some common errors include:
@@ -167,7 +177,7 @@ To update the policy and allow indexer access to the document library:
 
 If you're indexing content from Azure Blob Storage, and the container includes blobs of an [unsupported content type](search-howto-indexing-azure-blob-storage.md#SupportedFormats), the indexer skips that document. In other cases, there might be problems with individual documents. 
 
-In this situation, you can [set configuration options](search-howto-indexing-azure-blob-storage.md#DealingWithErrors) to allow indexer processing to continue in the event of problems with individual documents.
+In this situation, you can [set configuration options](search-howto-indexing-azure-blob-storage.md#DealingWithErrors) to allow indexer processing to continue if there are problems with individual documents.
 
 ```http
 PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2024-07-01
@@ -190,7 +200,7 @@ Indexers extract documents or rows from an external [data source](/rest/api/sear
 * Change tracking values are erroneous or prerequisites are missing. If your high watermark value is a date set to a future time, then any documents that have an earlier date are skipped by the indexer. You can determine your indexer's change tracking state using the 'initialTrackingState' and 'finalTrackingState' fields in the [indexer status](/rest/api/searchservice/indexers/get-status). Indexers for Azure SQL and MySQL must have an index on the high water mark column of the source table, or queries used by the indexer might time out. 
 
 > [!TIP]
-> If documents are missing, check the [query](/rest/api/searchservice/documents/search-post) you are using to make sure it isn't excluding the document in question. To query for a specific document, use the [Lookup Document REST API](/rest/api/searchservice/documents/get?).
+> If documents are missing, check the [query](/rest/api/searchservice/documents/search-post) you're using to make sure it isn't excluding the document in question. To query for a specific document, use the [Lookup Document REST API](/rest/api/searchservice/documents/get?).
 
 ## Missing content from Blob Storage
 
@@ -268,9 +278,9 @@ In practice, this scenario only happens when on-demand indexers are manually inv
 
 ## Parallel indexing
 
-When multiple indexers are operating simultaneously, it's typical for some to enter a queue, waiting for available resources to begin execution. The number of indexers that can run concurrently depends on several factors. If the indexers are not linked with [skillsets](cognitive-search-working-with-skillsets.md), the capacity to run in parallel relies on the number of [replicas and partitions](search-capacity-planning.md#concepts-search-units-replicas-partitions) set up in the AI Search service.
+When multiple indexers are operating simultaneously, it's typical for some to enter a queue, waiting for available resources to begin execution. The number of indexers that can run concurrently depends on several factors. If the indexers aren't linked with [skillsets](cognitive-search-working-with-skillsets.md), the capacity to run in parallel relies on the number of [replicas and partitions](search-capacity-planning.md#concepts-search-units-replicas-partitions) set up in the AI Search service.
 
-On the other hand, if an indexer is associated with a skillset, it operates within the AI Search's internal clusters. The ability to run concurrently in this case is determined by the complexity of the skillset and whether other skillsets are running simultaneously. Built-in indexers are designed to reliably extract data from the source, so no data is missed if running on a schedule. However, it is expected that the indexer processes of parallelization and scaling out may require some time. 
+On the other hand, if an indexer is associated with a skillset, it operates within the AI Search's internal clusters. The ability to run concurrently in this case is determined by the complexity of the skillset and whether other skillsets are running simultaneously. Built-in indexers are designed to reliably extract data from the source, so no data is missed if running on a schedule. However, it's expected that the indexer processes of parallelization and scaling out require some time to complete. 
 
 ## Indexing documents with sensitivity labels
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサートラブルシューティングに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるインデクサートラブルシューティングに関するドキュメントの更新で、以下の重要な内容が含まれています。

1. **新しいエラーメッセージの追加**: プライベート接続でのAzure AIサービスへの接続に関するエラーを詳細に説明するセクションが追加されました。このセクションでは、エラーコード403が表示されるシナリオと、問題の原因や解決策が提供されています。

2. **文言の修正**: 
   - いくつかの文がよりクリアに表現され、リーダビリティが向上しました。特に、個々のドキュメントに問題がある場合のインデクサの処理継続に関する文が修正されました。
   - 一部の文中の「youが使っている」という表現が「you’re」に修正され、文法的な一貫性が強化されています。

3. **文章の整頓**: ドキュメント全体が整理され、特に情報源やリンクが整然と提示されることによって、必要な情報にアクセスしやすくなっています。

これらの更新は、ユーザーがインデクサのトラブルシューティングを行う際に、より理解しやすく、具体的な指針が示されることを目的としています。全体として、ドキュメントの質が向上し、ユーザーにとっての実用性が増しています。

## articles/search/search-pagination-page-layout.md{#item-115902}

<details>
<summary>Diff</summary>
````diff
@@ -90,7 +90,7 @@ The default page size is 50, while the maximum page size is 1,000. If you specif
 
 The top matches are determined by search score, assuming the query is full text search or semantic. Otherwise, the top matches are an arbitrary order for exact match queries (where uniform `@search.score=1.0` indicates arbitrary ranking).
 
-Set `top` to override the default of 50. In newer preview APIs, if you're using a hybrid query, you can [specify maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview) to return up to 10,000 documents.
+Set `top` to override the default of 50. In newer preview APIs, if you're using a hybrid query, you can [specify maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) to return up to 10,000 documents.
 
 To control the paging of all documents returned in a result set, use `top` and `skip` together. This query returns the first set of 15 matching documents plus a count of total matches.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ページネーションに関するドキュメントのリンク更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるページネーションに関するドキュメントの更新で、主に以下の内容が修正されています。

1. **リンクの修正**: 
   - hybrid queryに関する部分のリンクが更新されました。具体的には、「maxTextRecallSize」を指定するためのリンクが、より正確な情報を提供する新しいパスに変更されています。

2. **文の内容が整った**: 
   - 残りの文はそのままですが、リンクの変更により、最新の情報を反映する形になっています。これにより、ユーザーは関連する機能や設定について正確にアクセスできるようになっています。

全体として、この更新は文書の信頼性を高め、ユーザーが新しいAPIや設定を理解しやすくすることを目的としています。ページネーションに関する情報が最新のものであることは、開発者にとって重要な要素であり、この変更により利用者の利便性が向上しています。

## articles/search/search-performance-analysis.md{#item-5032b3}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: mattgotteiner
 ms.author: magottei
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 06/06/2024
+ms.date: 01/16/2025
 ---
 
 # Analyze performance in Azure AI Search
@@ -17,7 +17,7 @@ This article describes the tools, behaviors, and approaches for analyzing query
 
 In any large implementation, it's critical to do a performance benchmarking test of your Azure AI Search service before you roll it into production. You should test both the search query load that you expect, but also the expected data ingestion workloads (if possible, run both workloads simultaneously). Having benchmark numbers helps to validate the proper [search tier](search-sku-tier.md), [service configuration](search-capacity-planning.md), and expected [query latency](search-performance-analysis.md#average-query-latency).
 
-To develop benchmarks, we recommend the [azure-search-performance-testing (GitHub)](https://github.com/Azure-Samples/azure-search-performance-testing) tool.
+<!-- To develop benchmarks, we recommend the [azure-search-performance-testing (GitHub)](https://github.com/Azure-Samples/azure-search-performance-testing) tool. -->
 
 To isolate the effects of a distributed service architecture, try testing on service configurations of one replica and one partition.
 
@@ -59,8 +59,8 @@ AzureDiagnostics
 Examining throttling over a specific time period can help you identify the times where throttling might occur more frequently. In the below example, a time series chart is used to show the number of throttled queries that occurred over a specified time frame. In this case, the throttled queries correlated with the times in with the performance benchmarking was performed.
 
 ```kusto
-let ['_startTime']=datetime('2021-02-25T20:45:07Z');
-let ['_endTime']=datetime('2021-03-03T20:45:07Z');
+let ['_startTime']=datetime('2024-02-25T20:45:07Z');
+let ['_endTime']=datetime('2024-03-03T20:45:07Z');
 let intervalsize = 1m; 
 AzureDiagnostics 
 | where TimeGenerated > ago(7d)
@@ -122,8 +122,8 @@ In the below query, an interval size of 1 minute is used to show the average lat
 
 ```kusto
 let intervalsize = 1m; 
-let _startTime = datetime('2021-02-23 17:40');
-let _endTime = datetime('2021-02-23 18:00');
+let _startTime = datetime('2024-02-23 17:40');
+let _endTime = datetime('2024-02-23 18:00');
 AzureDiagnostics
 | where TimeGenerated between(['_startTime']..['_endTime']) // Time range filtering
 | summarize AverageQueryLatency = avgif(DurationMs, OperationName in ("Query.Search", "Query.Suggest", "Query.Lookup", "Query.Autocomplete"))
@@ -139,8 +139,8 @@ The following query looks at the average number of queries per minute to ensure
 
 ```kusto
 let intervalsize = 1m; 
-let _startTime = datetime('2021-02-23 17:40');
-let _endTime = datetime('2021-02-23 18:00');
+let _startTime = datetime('2024-02-23 17:40');
+let _endTime = datetime('2024-02-23 18:00');
 AzureDiagnostics
 | where TimeGenerated between(['_startTime'] .. ['_endTime']) // Time range filtering
 | summarize QueriesPerMinute=bin(countif(OperationName in ("Query.Search", "Query.Suggest", "Query.Lookup", "Query.Autocomplete"))/(intervalsize/1m), 0.01)
@@ -158,8 +158,8 @@ From this insight, we can see that it took about 3 minutes for the search servic
 
 ```kusto
 let intervalsize = 1m; 
-let _startTime = datetime('2021-02-23 17:40');
-let _endTime = datetime('2021-02-23 18:00');
+let _startTime = datetime('2024-02-23 17:40');
+let _endTime = datetime('2024-02-23 18:00');
 AzureDiagnostics
 | where TimeGenerated between(['_startTime'] .. ['_endTime']) // Time range filtering
 | summarize IndexingOperationsPerSecond=bin(countif(OperationName == "Indexing.Index")/ (intervalsize/1m), 0.01)
@@ -171,7 +171,7 @@ AzureDiagnostics
 
 ## Background service processing
 
-It isn't unusual to see periodic spikes in query or indexing latency. Spikes might occur in response to indexing or high query rates, but could also occur during merge operations. Search indexes are stored in chunks - or shards. Periodically, the system merges smaller shards into large shards, which can help optimize service performance. This merge process also cleans up documents that have previously been marked for deletion from the index, resulting in the recovery of storage space. 
+It's common to see occasional spikes in query or indexing latency. Spikes might occur in response to indexing or high query rates, but could also occur during merge operations. Search indexes are stored in chunks - or shards. Periodically, the system merges smaller shards into large shards, which can help optimize service performance. This merge process also cleans up documents that have previously been marked for deletion from the index, resulting in the recovery of storage space. 
 
 Merging shards is fast, but also resource intensive and thus has the potential to degrade service performance. If you notice short bursts of query latency, and those bursts coincide with recent changes to indexed content, you can assume the latency is due to shard merge operations. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "パフォーマンス分析に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるパフォーマンス分析に関するドキュメントの更新で、主に以下の点が修正されています。

1. **日付の更新**: 最初に表示されていた日付が2024年6月6日から2025年1月16日に変更されました。これはドキュメントの作成または更新の日付を反映しています。

2. **コードのサンプルにおける日時の変更**: 
   - いくつかのKustoクエリのサンプル内の日時が2021年から2024年に更新されました。この変更により、サンプルが現在の文脈に適したものであることが示されています。

3. **コメントの追加**: 一つの文がコメントアウトされており、ベンチマークの開発に関する推奨ツール（azure-search-performance-testing）のリンクが見えなくなっています。これは、現在の文脈では表示したくない情報として扱われた可能性があります。

4. **文言の微調整**: 一部の文が軽微に修正され、「It isn't unusual to see periodic spikes」という表現が「It's common to see occasional spikes」に変更されました。これにより、表現がより自然になっています。

全体として、この更新はドキュメントを最新の情報に保ち、読者がより正確にパフォーマンス分析を行えるようにサポートすることを目指しています。特に、サンプルコードの日時の更新は、実際のデータやトレンドを反映するために重要です。

## articles/search/search-security-api-keys.md{#item-d8c908}

<details>
<summary>Diff</summary>
````diff
@@ -2,24 +2,23 @@
 title: Connect using API keys
 titleSuffix: Azure AI Search
 description: Learn how to use an admin or query API key for inbound access to an Azure AI Search service endpoint.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 10/30/2024
+ms.date: 1/16/2025
+#customer intent: I want to learn how to connect to Azure AI Search using API keys so that I can authenticate inbound requests to my search service.
 ---
 
 # Connect to Azure AI Search using keys
 
-Azure AI Search offers key-based authentication for connections to your search service. An API key is a unique string composed of 52 randomly generated numbers and letters. In your source code, you can specify it as an [environment variable](/azure/ai-services/cognitive-services-environment-variables) or as an app setting in your project, and then reference the variable on the request. A request made to a search service endpoint is accepted if both the request and the API key are valid.
-
-Key-based authentication is the default. 
+Azure AI Search supports both keyless and key-based authentication for connections to your search service. An API key is a unique string composed of 52 randomly generated numbers and letters. In your source code, you can specify it as an [environment variable](/azure/ai-services/cognitive-services-environment-variables) or as an app setting in your project, and then reference the variable on the request. A request made to a search service endpoint is accepted if both the request and the API key are valid.
 
-You can replace it with [role-based access](search-security-enable-roles.md), which eliminates the need for hardcoded keys in your codebase.
+> [!IMPORTANT]
+> When you create a search service, key-based authentication is the default, but it's not the most secure option. We recommend that you replace it with [role-based access](search-security-enable-roles.md).
 
 ## Types of API keys
 
@@ -36,11 +35,11 @@ Visually, there's no distinction between an admin key or query key. Both keys ar
 
 ## Use API keys on connections
 
-API keys are used for data plane (content) requests, such as creating or accessing an index or, any other request that's represented in the [Search REST APIs](/rest/api/searchservice/). Upon service creation, an API key is the only authentication mechanism for data plane operations, but you can replace or supplement key authentication with [Azure roles](search-security-rbac.md) if you can't use hard-coded keys in your code.
-
-Admin keys are used for creating, modifying, or deleting objects. Admin keys are also used to GET object definitions and system information.
+API keys are used for data plane (content) requests, such as creating or accessing an index or, any other request that's represented in the [Search REST APIs](/rest/api/searchservice/). 
 
-Query keys are typically distributed to client applications that issue queries.
+You can use either an API key or [Azure roles](search-security-rbac.md) for management plane (service) requests. When you use an API key:
+- Admin keys are used for creating, modifying, or deleting objects. Admin keys are also used to GET object definitions and system information.
+- Query keys are typically distributed to client applications that issue queries.
 
 ### [**REST API**](#tab/rest-use)
 
@@ -241,11 +240,13 @@ It's not possible to use [customer-managed key encryption](search-security-manag
 
 ## Best practices
 
++ For production workloads, switch to [Microsoft Entra ID and role-based access](keyless-connections.md). Or, if you want to continue using API keys, be sure to always monitor [who has access to your API keys](#secure-api-keys) and [regenerate API keys](#regenerate-admin-keys) on a regular cadence.
+
 + Only use API keys if data disclosure isn't a risk (for example, when using sample data) and if you're operating behind a firewall. Exposure of API keys is a risk to both data and to unauthorized use of your search service. 
 
-+ Always check code, samples, and training material before publishing to make sure you didn't leave valid API keys behind.
++ If you use an API key, store it securely somewhere else, such as in [Azure Key Vault](/azure/key-vault/general/overview). Don't include the API key directly in your code, and never post it publicly.
 
-+ For production workloads, switch to [Microsoft Entra ID and role-based access](keyless-connections.md). Or, if you want to continue using API keys, be sure to always monitor [who has access to your API keys](#secure-api-keys) and [regenerate API keys](#regenerate-admin-keys) on a regular cadence.
++ Always check code, samples, and training material before publishing to make sure you don't inadvertently expose an API key.
 
 ## See also
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "API キーによる認証に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI SearchにおけるAPIキーを使用した接続方法に関するドキュメントの更新で、以下の主要なポイントが修正されています。

1. **日付の更新**: ドキュメントの日付が2024年10月30日から2025年1月16日に変更され、最新の情報であることが示されています。

2. **認証方式の明確化**: 
   - 認証方式の説明が更新され、Azure AI Searchが「キーなし」および「キーあり」の認証をサポートすることが明確に記載されました。これにより、ユーザーがオプションを理解しやすくなっています。
   - キーについての注意事項として、デフォルトの設定はキーによる認証であり、これは必ずしも最も安全とは限らないため、ロールベースのアクセスに切り替えることが推奨されています。

3. **文言の改良と構造化**: 
   - 一部のセクションが整理され、APIキーの使用方法や管理方法に関する情報がより明確に分かるように構造が改善されています。
   - 特に、APIキーの種類（管理者キーとクエリーキー）やそれぞれの用途についての説明が強化され、視覚的に分かりやすいフォーマットが採用されています。

4. **ベストプラクティスの追加**: 
   - APIキーを使用する際のベストプラクティスが追加され、セキュアな保管方法や、公開コードにAPIキーが残らないようにすることの重要性が強調されています。また、Microsoft Entra IDやロールベースのアクセスへの移行が推奨されています。

これらの更新は、ユーザーがAPIキーを用いた接続のセキュリティや管理についてより良い理解を持てるようにすることを目的としています。また、文書全体の信頼性と有用性を向上させる効果があります。

## articles/search/search-security-enable-roles.md{#item-4985c4}

<details>
<summary>Diff</summary>
````diff
@@ -2,19 +2,21 @@
 title: Enable role-based access control
 titleSuffix: Azure AI Search
 description: Enable or disable role-based access control for token authentication using Microsoft Entra ID on Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 10/30/2024
-
+ms.date: 1/16/2025
+#customer intent: As a developer, I want to enable role-based access control for token authentication using Microsoft Entra ID on Azure AI Search so that I can secure my search service.
 ---
 
 # Enable or disable role-based access control in Azure AI Search
 
-Azure AI Search uses [key-based authentication](search-security-api-keys.md) by default, but it fully supports Microsoft Entra ID authentication and authorization for all control plane and data plane operations through Azure role-based access control (RBAC).
+Azure AI Search supports both keyless and [key-based authentication](search-security-api-keys.md) for for all control plane and data plane operations. You can use Microsoft Entra ID authentication and authorization for all control plane and data plane operations through Azure role-based access control (RBAC).
+
+> [!IMPORTANT]
+> When you create a search service, key-based authentication is the default, but it's not the most secure option. We recommend that you replace it with role-based access as described in this article.
 
 Before you can assign roles for authorized data plane access to Azure AI Search, you must enable role-based access control on your search service. Roles for service administration (control plane) are built in and can't be enabled or disabled. 
 
@@ -37,18 +39,18 @@ The default failure mode for unauthorized requests is `http401WithBearerChalleng
 
 ### [**Azure portal**](#tab/config-svc-portal)
 
-1. Sign in to the [Azure portal](https://portal.azure.com) and open the search service page.
+1. Sign in to the [Azure portal](https://portal.azure.com) and navigate to your search service.
 
 1. Select **Settings** and then select **Keys** in the left navigation pane.
 
    :::image type="content" source="media/search-security-rbac/search-security-enable-roles.png" lightbox="media/search-security-rbac/search-security-enable-roles.png" alt-text="Screenshot of the keys page with authentication options." border="true":::
 
-1. Choose **Role-based control** or **Both** if you're currently using keys and need time to transition clients to role-based access control. 
+1. Choose **Role-based control**. Only choose **Both** if you're currently using keys and need time to transition clients to role-based access control. 
 
    | Option | Description |
    |--------|--------------|
-   | API Key | (default). Requires [API keys](search-security-api-keys.md) on the request header for authorization. |
-   | Role-based access control | Requires membership in a role assignment to complete the task. It also requires an authorization header on the request. |
+   | API Key (default) | Requires [API keys](search-security-api-keys.md) on the request header for authorization. |
+   | Role-based access control (recommended) | Requires membership in a role assignment to complete the task. It also requires an authorization header on the request. |
    | Both | Requests are valid using either an API key or role-based access control, but if you provide both in the same request, the API key is used. |
 
 1. As an administrator, if you choose a roles-only approach, [assign data plane roles](search-security-rbac.md) to your user account to restore full administrative access over data plane operations in the Azure portal. Roles include Search Service Contributor, Search Index Data Contributor, and Search Index Data Reader. You need the first two roles if you want equivalent access.
@@ -140,7 +142,7 @@ All calls to the Management REST API are authenticated through Microsoft Entra I
 
 It's possible to disable role-based access control for data plane operations and use key-based authentication instead. You might do this as part of a test workflow, for example to rule out permission issues.
 
-Reverse the steps you followed previously to enable role-based access.
+To disable role-based access control in the Azure portal:
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and open the search service page.
 
@@ -221,12 +223,6 @@ To re-enable key authentication, set "disableLocalAuth" to false. The search ser
 
 ---
 
-## Effects of role-based access control
-
-+ Role-based access control can increase the latency of some requests. Each unique combination of service resource (index, indexer, skillsets and so forth) and service principal triggers an authorization check. These authorization checks can add up to 200 milliseconds of latency per request. 
-
-+ In rare cases where requests originate from a high number of different service principals, all targeting different service resources (indexes, indexers, and so forth), it's possible for the authorization checks to result in throttling. Throttling would only happen if hundreds of unique combinations of search service resource and service principal were used within a second.
-
 ## Next steps
 
 > [!div class="nextstepaction"]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ロールベースのアクセス制御に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるロールベースのアクセス制御（RBAC）の有効化または無効化に関するドキュメントの更新で、主に以下のポイントが修正されています。

1. **日付の更新**: ドキュメントの日付が2024年10月30日から2025年1月16日に更新され、最新の情報であることが示されています。

2. **認証方式の改善**:
   - 役割ベースのアクセス制御がサポートされることの重要性を強調し、デフォルトのキーによる認証が最も安全な選択肢ではないことを明記しました。
   - 標準的な認証方法が強調され、「キーなし」および「キーあり」の認証がすべての操作に対応していることが記載されています。

3. **手順の明確化**:
   - Azureポータルでのロールの設定手順が明確化され、ナビゲーションの変更が反映されています。また、APIキーまたはロールベースのアクセス制御の選択に関する説明も改善されています。
   - ロール管理に関する指示が、役割のみのアプローチを選択した場合のデータプレーン権限の割り当てに触れています。

4. **決定と注意事項**:
   - ロールベースのアクセス制御の無効化手順が追加され、必要な手続きを説明しています。
   - また、ロールベースのアクセス制御が遅延を引き起こす可能性に関する情報が削除され、より簡潔で焦点が絞られた内容になっています。

これらの変更は、開発者がAzure AI Searchのセキュリティを強化し、ユーザーがより安全にサービスを利用できるようにすることを目的としています。また、文書全体の信頼性と有用性を向上させ、市場や技術の進化に合わせた最新の情報を提供することを目指しています。

## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -606,12 +606,6 @@ To enable a Conditional Access policy for Azure AI Search, follow these steps:
 > [!IMPORTANT]
 > If your search service has a managed identity assigned to it, the specific search service will show up as a cloud app that can be included or excluded as part of the Conditional Access policy. Conditional Access policies can't be enforced on a specific search service. Instead make sure you select the general **Azure AI Search** cloud app.
 
-## Limitations
-
-+ Role-based access control can increase the latency of some requests. Each unique combination of service resource (index, indexer, etc.) and service principal triggers an authorization check. These authorization checks can add up to 200 milliseconds of latency per request. 
-
-+ In rare cases where requests originate from a high number of different service principals, all targeting different service resources (indexes, indexers, etc.), it's possible for the authorization checks to result in throttling. Throttling would only happen if hundreds of unique combinations of search service resource and service principal were used within a second.
-
 ## Troubleshooting role-based access control issues
 
 When developing applications that use role-based access control for authentication, some common issues might occur:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "役割ベースのアクセス制御に関する制限事項の削除"
}
```

### Explanation
この変更は、Azure AI Searchにおける役割ベースのアクセス制御（RBAC）に関するドキュメントの更新で、主に以下のポイントが修正されています。

1. **制限事項の削除**: 
   - 役割ベースのアクセス制御に関連する制限事項が削除されました。具体的には、RBACが一部のリクエストのレイテンシを増加させる可能性や、異なるサービスプリンシパルからのリクエストによるスロットリングの可能性についての説明が削除されています。

2. **重要な注意事項の保持**: 
   - 条件付きアクセスポリシーに関する重要な情報や注意事項は、引き続き文書内に残されています。この内容は、学習者がRBACを適切に利用するための参考となるでしょう。

この変更により、ユーザーがRBACの理解を深める際に、潜在的な制限に関する情報が含まれないため、混乱を避けることができます。また、役割ベースのアクセスに関する情報がより明確であることを目指しています。これにより、Azure AI Searchの利用者が適切なアクセス制御を実施しやすくなることを目的としています。

## articles/search/tutorial-csharp-create-load-index.md{#item-0a6ffd}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: diberry
 ms.author: diberry
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 08/16/2024
+ms.date: 01/17/2025
 ms.custom:
   - devx-track-csharp
   - devx-track-azurecli
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# チュートリアルの更新日付の変更"
}
```

### Explanation
この変更は、Azure AI Searchに関するC#チュートリアルのドキュメント更新に関して、以下のポイントが修正されています。

1. **日付の変更**: 
   - ドキュメントの日付が2024年8月16日から2025年1月17日に変更され、内容の更新や新しい情報の提供を反映させています。これは、ユーザーに対して最新のチュートリアルであることを示すための重要な修正です。

この変更は、ユーザーが最新の情報を基に学習および実装を進めることができるようにすることを目的としています。また、ドキュメントの信頼性を高め、技術の進歩に伴った適切なリソースを提供することに寄与しています。

## articles/search/tutorial-csharp-deploy-static-web-app.md{#item-a2300f}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: diberry
 ms.author: diberry
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 08/16/2024
+ms.date: 01/17/2025
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# チュートリアルの更新日付の変更"
}
```

### Explanation
この変更は、Azure AI Searchに関するC#チュートリアル「静的Webアプリのデプロイ」について、主に以下のポイントが修正されています。

1. **日付の変更**:
   - ドキュメントの日付が2024年8月16日から2025年1月17日に変更されました。これにより、最新の情報が反映されていることを示し、ユーザーに対して更新された内容を提供しています。

この変更は、チュートリアルの信頼性を向上させ、ユーザーが最新の手順やガイダンスに基づいて構築を進められるようにするためのものです。また、技術の進展や更新に対応するために、このようなリソースの日付管理は重要となります。

## articles/search/tutorial-csharp-overview.md{#item-57fa0d}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: diberry
 ms.author: diberry
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 10/21/2024
+ms.date: 01/17/2025
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
@@ -48,7 +48,7 @@ The [sample code](https://github.com/Azure-Samples/azure-search-static-web-app)
 Create services and install the following software for your local development environment. 
 
 - [Azure AI Search](search-create-service-portal.md), any region or tier
-- [.NET 6](https://dotnet.microsoft.com/download/dotnet/6.0) or later
+- [.NET 9](https://dotnet.microsoft.com/download/dotnet) or latest version
 - [Git](https://git-scm.com/downloads)
 - [Visual Studio Code](https://code.visualstudio.com/)
 - [C# Dev Tools extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# チュートリアルのバージョンアップデート"
}
```

### Explanation
この変更は、Azure AI Searchに関連するC#チュートリアルの概要に対する更新であり、主に以下のポイントが修正されています。

1. **日付の変更**:
   - ドキュメントの日付が2024年10月21日から2025年1月17日に変更されました。この変更により、最新の情報に基づいていることが示されます。

2. **ソフトウェアバージョンの更新**:
   - 開発環境に必要なソフトウェアのバージョンが更新され、.NET 6から最新の.NET 9に変更されました。これにより、ユーザーは最新の開発ツールに基づいて作業できるようになります。

この変更は、ユーザーに最新の情報や適切なライブラリを提供し、チュートリアルの有用性を高めることを目的としています。適切なソフトウェアを使用することにより、開発環境の整備やチュートリアルに従った実装がよりスムーズに進むことが期待されます。

## articles/search/tutorial-csharp-search-query-integration.md{#item-8ad6b5}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: diberry
 ms.author: diberry
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 08/16/2024
+ms.date: 01/17/2025
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# 検索クエリ統合チュートリアルの日付更新"
}
```

### Explanation
この変更は、C#を使用した検索クエリ統合に関するチュートリアルの更新であり、以下の点が修正されています。

1. **日付の変更**:
   - ドキュメントの日付が2024年8月16日から2025年1月17日に変更されました。これにより、コンテンツが最新の状態であることが示されており、ユーザーは新しい情報を参照することができます。

このような更新は、技術文書が常に最新の知識やベストプラクティスを反映するように保つために重要です。ユーザーは、この情報を使用して、検索機能の統合を効果的に行うことが期待されます。

## articles/search/vector-search-how-to-query.md{#item-9bb93c}

<details>
<summary>Diff</summary>
````diff
@@ -136,7 +136,7 @@ api-key: {{admin-api-key}}
 This preview adds:
 
 + [`threshold`](#set-thresholds-to-exclude-low-scoring-results-preview) for excluding low scoring results.
-+ [`Hybridsearch.MaxTextRecallSize`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview) for more control over the inputs to a [hybrid query](hybrid-search-how-to-query.md).
++ [`Hybridsearch.MaxTextRecallSize`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) for more control over the inputs to a [hybrid query](hybrid-search-how-to-query.md).
 
 In the following example, the vector is a representation of this string: "what Azure services support full text search". The query targets the `contentVector` field. The query returns `k` results. The actual vector has 1536 embeddings, so it's trimmed in this example for readability.
 
@@ -489,7 +489,7 @@ POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?
     } 
 ```
 
-Vector weighting applies to vectors only. The text query in this example ("hello world") has an implicit weight of 1.0 or neutral weight. However, in a hybrid query, you can increase or decrease the importance of text fields by setting [maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview).
+Vector weighting applies to vectors only. The text query in this example ("hello world") has an implicit weight of 1.0 or neutral weight. However, in a hybrid query, you can increase or decrease the importance of text fields by setting [maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode).
 
 ## Set thresholds to exclude low-scoring results (preview)
 
@@ -522,13 +522,13 @@ POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?
  <!-- Keep H2 as-is. Direct link from a blog post. Bulk of maxtextsizerecall has moved to hybrid query doc-->
 ## MaxTextSizeRecall for hybrid search (preview)
 
-Vector queries are often used in hybrid constructs that include nonvector fields. If you discover that BM25-ranked results are over or under represented in a hybrid query results, you can [set `maxTextRecallSize`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview) to increase or decrease the BM25-ranked results provided for hybrid ranking.
+Vector queries are often used in hybrid constructs that include nonvector fields. If you discover that BM25-ranked results are over or under represented in a hybrid query results, you can [set `maxTextRecallSize`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) to increase or decrease the BM25-ranked results provided for hybrid ranking.
 
 You can only set this property in hybrid requests that include both "search" and "vectorQueries" components.
 
 This parameter is still in preview. We recommend preview REST API version [2024-05-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true).
 
-For more information, see [Set maxTextRecallSize - Create a hybrid query](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview).
+For more information, see [Set maxTextRecallSize - Create a hybrid query](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode).
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索クエリ統合チュートリアルの文書更新"
}
```

### Explanation
この変更は、ベクトル検索に関するクエリ統合のチュートリアルについての更新であり、以下の主な点が修正されています。

1. **プレビュー機能の追加**:
   - 新たに `threshold` が追加され、低スコア結果を除外するための機能について言及されています。この更新により、ユーザーはクエリの結果をより制御できるようになります。

2. **文書のリンク修正**:
   - `Hybridsearch.MaxTextRecallSize` に関するリンクのプレビュー識別子が削除され、直接最新の情報を指すように更新されました。これにより、ユーザーが常に正確な情報にアクセスできるようになります。

3. **テキストリコールサイズの設定**:
   - テキストリコールサイズの設定に関する説明が更新され、ハイブリッドクエリにおける重要性の調整についての詳細がより明確に示されています。

この変更は、ドキュメントの一貫性を保ち、ユーザーが機能を効果的に利用できるようにするための重要な更新です。ユーザーは、この情報を活用して、ベクトル検索やハイブリッド検索での結果を最適化することが期待されます。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -89,7 +89,7 @@ ms.custom:
 |-----------------------------|------|--------------|
 | [Higher capacity and more vector quota at every tier (same billing rate)](search-limits-quotas-capacity.md#service-limits) | Infrastructure | For most regions, partition sizes are now even larger for Standard 2 (S2), Standard 3 (S3), and Standard 3 High Density (S3 HD) for services created after April 3, 2024. To get the larger partitions, create a new service in a [region that provides newer infrastructure](search-region-support.md). <br><br>Storage Optimized tiers (L1 and L2) also have more capacity. L1 and L2 customers must create a new service to benefit from the higher capacity. There's no in-place upgrade at this time. <br><br>Extra capacity is now available in [more regions](search-limits-quotas-capacity.md#service-limits): Germany North​, Germany West Central​, South Africa North​, Switzerland West​, and Azure Government (Texas, Arizona, and Virginia).|
 | [OneLake integration (preview)](search-how-to-index-onelake-files.md) | Feature | New indexer for OneLake files and OneLake shortcuts. If you use Microsoft Fabric and OneLake for data access to Amazon Web Services (AWS) and Google data sources, use this indexer to import external data into a search index. This indexer is available through the Azure portal, the [2024-05-01-preview REST API](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true), and Azure SDK beta packages. |
-| [Vector relevance](vector-search-how-to-query.md) <br>[hybrid query relevance](hybrid-search-how-to-query.md) | Feature | Four enhancements improve vector and hybrid search relevance. <br><br>First, you can now set thresholds on vector search results to exclude low-scoring results. <br><br>Second, changes in the query architecture apply scoring profiles at the end of the query pipeline for every query type. Document boosting is a common scoring profile, and it now works as expected on vector and hybrid queries.<br><br>Third, you can set `MaxTextRecallSize` and `countAndFacetMode` in hybrid queries to control the quantity of BM25-ranked search results that flow into the hybrid ranking model. <br><br>Fourth, for vector and hybrid search, you can weight a vector query to have boost or diminish its importance in a multiquery request. |
+| [Vector relevance](vector-search-how-to-query.md) <br>[hybrid query relevance](hybrid-search-how-to-query.md) | Feature | Four enhancements improve vector and hybrid search relevance. <br><br>First, you can now set thresholds on vector search results to exclude low-scoring results. <br><br>Second, changes in the query architecture apply scoring profiles at the end of the query pipeline for every query type. Document boosting is a common scoring profile, and it now works as expected on vector and hybrid queries.<br><br>Third, you can set [`MaxTextRecallSize` and `countAndFacetMode`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) in hybrid queries to control the quantity of BM25-ranked search results that flow into the hybrid ranking model. <br><br>Fourth, for vector and hybrid search, you can weight a vector query to have boost or diminish its importance in a multiquery request. |
 | [Binary vectors support](/rest/api/searchservice/supported-data-types) | Feature | `Collection(Edm.Byte)` is a new supported data type. This data type opens up integration with the [Cohere v3 binary embedding models](https://cohere.com/blog/int8-binary-embeddings) and custom binary quantization. Narrow data types lower the cost of large vector datasets. See [Index binary data for vector search](vector-search-how-to-index-binary-data.md) for more information.| 
 | [Azure AI Vision multimodal embeddings skill (preview)](cognitive-search-skill-vision-vectorize.md) | Skill | New skill that's bound to the [multimodal embeddings API of Azure AI Vision](/azure/ai-services/computer-vision/concept-image-retrieval). You can generate embeddings for text or images during indexing. This skill is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true).|
 | [Azure AI Vision vectorizer (preview)](vector-search-vectorizer-ai-services-vision.md) | Vectorizer | New vectorizer connects to an Azure AI Vision resource using the [multimodal embeddings API](/azure/ai-services/computer-vision/concept-image-retrieval) to generate embeddings at query time. This vectorizer is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能および改善点の追加"
}
```

### Explanation
この変更は、Azureの検索機能に関する「新着情報」セクションの更新であり、以下の主要なポイントが修正されています。

1. **新機能の追加**:
   - `MaxTextRecallSize` および `countAndFacetMode` に関連する詳細が明確に示され、ハイブリッドクエリにおけるBM25ランク結果の量を制御する方法が強調されています。これにより、ユーザーは検索結果の質をより効果的に調整できます。

2. **文の一貫性**:
   - ベクトル検索とハイブリッド検索の関連性向上に関する機能説明の文が更新され、より明確で正確な表現に修正されています。特に、ベクトルクエリの重要性を調整する方法についての説明が改善されました。これにより、ユーザーは新しい機能を効果的に利用できるようになります。

これらの更新は、最新の機能とその使用方法についての理解を深め、ユーザーが検索機能を最大限に活用することをサポートするために重要です。


