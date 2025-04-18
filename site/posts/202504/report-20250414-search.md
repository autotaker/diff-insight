---
date: '2025-04-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:83f1d3d...MicrosoftDocs:f2cba99
summary: この報告は、`semantic-search-overview.md` ファイル内のセマンティックランカーに関する説明が改善されたことを示しています。主な変更点は、文章の流れと明確さが向上し、冗長な表現が削除されたことです。また、セマンティックランカーの機能について具体例を交えた親しみやすい表現に刷新され、クエリのリライト機能に関する記述も簡潔になりました。この改訂により、読者はセマンティックランカーの機能をより良く理解し、実際に応用する能力が高まります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:83f1d3d...MicrosoftDocs:f2cba99){target="_blank"}

# ハイライト

- **新機能**: なし
- **Breaking changes**: なし
- **その他の更新**: `semantic-search-overview.md` ファイル内のセマンティックランカーの機能に関連する説明が改善され、文章の流れと明確さが向上しました。

## インサイト

このコード変更は、ファイル `semantic-search-overview.md` におけるセマンティックランカーに関する説明を微修正しています。特に以下のポイントで改善されています。

### テキストの流れとクリアさ

変更の目的は、セマンティックランカーがクエリ実行パイプラインをどのように拡張するかについて、よりクリアな説明を提供することにあります。具体的には、冗長な表現が削除され、一貫性を持った文章に生まれ変わりました。これにより、読者に対してより簡潔で理解しやすい情報が提供されることになります。

### 機能に関する説明の修正

セマンティックランカーの機能が検索結果に与える影響について、具体的な例や具体性を持たせる表現に刷新され、説明がより親しみやすくなりました。また、クエリのリライト機能に関する記述も簡潔になっており、機能の意図や内容を素早く把握できるようになっています。

この改訂により、`semantic-search-overview.md` を読むことでセマンティックランカーの機能についての理解度が向上し、読者がこの記事で提起された概念を効果的に応用できる可能性が高まります。セマンティックランカーの役割やその利便性に対するユーザーの認識を強化するものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [semantic-search-overview.md](#item-b7497b) | minor update | セマンティックランカーの概要の更新 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/search/semantic-search-overview.md{#item-b7497b}

<details>
<summary>Diff</summary>
````diff
@@ -24,13 +24,13 @@ Semantic ranker is a premium feature, billed by usage. We recommend this article
 
 ## What is semantic ranking?
 
-Semantic ranker calls LLMs at query time. LLms are used to improve the quality of an initial [BM25-ranked](index-similarity-and-scoring.md) or [RRF-ranked](hybrid-search-ranking.md) search result for text-based queries, the text portion of vector queries, and hybrid queries. Semantic ranking extends the query execution pipeline in three ways:
+Semantic ranker is a collection of query-side capabilities that improve the quality of an initial [BM25-ranked](index-similarity-and-scoring.md) or [RRF-ranked](hybrid-search-ranking.md) search result for text-based queries, the text portion of vector queries, and hybrid queries. Semantic ranking extends the query execution pipeline in three ways:
 
 * First, it always adds secondary ranking over an initial result set that was scored using BM25 or Reciprocal Rank Fusion (RRF). This secondary ranking uses multi-lingual, deep learning models adapted from Microsoft Bing to promote the most semantically relevant results.
 
 * Second, it returns captions and optionally extracts answers in the response, which you can render on a search page to improve the user's search experience.
 
-* Third, if you enable query rewrite, it calls an LLM to expand an initial query string into multiple semantically similar query strings. 
+* Third, if you enable query rewrite, it expands an initial query string into multiple semantically similar query strings. 
 
 Secondary ranking and "answers" apply to the query response. Query rewrite is part of the query request.
 
@@ -41,7 +41,7 @@ Here are the capabilities of the semantic reranker.
 | L2 ranking | Uses the context or semantic meaning of a query to compute a new relevance score over preranked results. |
 | [Semantic captions and highlights](semantic-how-to-query-request.md) | Extracts verbatim sentences and phrases from fields that best summarize the content, with highlights over key passages for easy scanning. Captions that summarize a result are useful when individual content fields are too dense for the search results page. Highlighted text elevates the most relevant terms and phrases so that users can quickly determine why a match was considered relevant. |
 | [Semantic answers](semantic-answers.md) | An optional and extra substructure returned from a semantic query. It provides a direct answer to a query that looks like a question. It requires that a document has text with the characteristics of an answer. |
-| [Query rewrite](semantic-how-to-query-rewrite.md) | Using text queries or the text portion of a vector query, semantic ranker creates up to 10 variants of the query, perhaps correcting typos or spelling errors, or rephrasing a query using synonyms generated by the LLM. The rewritten query runs on the search engine. The results are scored using BM25 or RRF scoring, and then rescored by semantic ranker.  |
+| [Query rewrite](semantic-how-to-query-rewrite.md) | Using text queries or the text portion of a vector query, semantic ranker creates up to 10 variants of the query, perhaps correcting typos or spelling errors, or rephrasing a query using generated synonyms. The rewritten query runs on the search engine. The results are scored using BM25 or RRF scoring, and then rescored by semantic ranker.  |
 
 ## How semantic ranker works
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーの概要の更新"
}
```

### Explanation
この変更は、`semantic-search-overview.md` ファイルにおけるセマンティックランカーの機能に関連する説明の微修正を含んでいます。主に文の表現がクリアにされ、テキストの流れが向上しています。

具体的には、セマンティックランカーがクエリ実行パイプラインをどのように拡張するかについての説明が改善されました。一部の冗長な表現が削除され、内容が明確に伝わるように整理されています。

1. セマンティックランカーの機能が初期の検索結果を改善する方法に関する文が修正され、説明がより一貫性を持つようになりました。
2. クエリのリライト機能に関する説明も簡潔になり、理解しやすさが向上しました。

全体として、この記事はよりユーザーフレンドリーになり、セマンティックランカーの機能についての理解を深めやすくなっています。


