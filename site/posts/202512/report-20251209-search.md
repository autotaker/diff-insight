---
date: '2025-12-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bedb028...MicrosoftDocs:7bfe620
summary: この変更では、「検索関連性の概要」記事が更新され、Azure AI Searchにおける検索結果の関連性を高めるための新しい戦略や手法が追加されました。ユーザーは関連性の評価方法やランキングアルゴリズムについて深く理解できるようになります。新たに紹介された「ハイブリッド検索」と「エージェンティック検索」は、複数の検索技術を組み合わせたり、ユーザーの意図に基づく関連性の高い結果を提供する方法です。検索クエリに対するランキングアルゴリズムや検索スコアの説明が詳細に説明され、開発者やエンジニアにとって有益なリソースとなることを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bedb028...MicrosoftDocs:7bfe620){target="_blank"}

# ハイライト

この変更では、「検索関連性の概要」記事が更新され、Azure AI Searchにおいて検索結果の関連性を高めるための新たな戦略や手法の説明が追加されました。この更新により、ユーザーは検索関連性の評価方法やランキングアルゴリズムについて理解を深めることができます。

## 新機能

- 関連性向上のための新しい戦略として「ハイブリッド検索」と「エージェンティック検索」が紹介されました。
- 検索クエリに対するランキングアルゴリズムの詳細が追加されました。

## 破壊的変更

- 特に破壊的な変更は行われていません。

## その他の更新

- 記事の説明が改訂され、関連性の重要性について強調されました。
- 検索スコアの意味とその測定方法についての説明が追加されました。

# インサイト

このアップデートでは、Azure AI Searchのユーザーが検索結果の関連性をどのように高めるかを具体的に学べるよう、ドキュメントが強化されています。特に「ハイブリッド検索」と「エージェンティック検索」が新たに紹介された点は、ユーザーが検索における関連性を最適化するための有効な手段となります。ハイブリッド検索では、複数の検索技術を組み合わせてより精度の高い結果が得られるようにする手法を指します。一方、エージェンティック検索は、ユーザーの意図や文脈に基づいた関連性の高い結果を提供するアプローチです。

また、検索クエリに対するランキングアルゴリズムの動作や、検索スコアの意味がより詳細に解説されています。これにより、エンドユーザーがどのように検索エンジンが結果を評価しているのかを理解し、自らの検索システムを改善するためのインサイトを得ることができます。

全体として、この文書の更新は、Azure AI Searchを利用する開発者やエンジニアにとって、有益なリソースとなる内容へと進化しており、システム設計や最適化の際に役立つでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-relevance-overview.md](#item-cb0e09) | minor update | 検索関連性の概要の更新 | modified | 23 | 4 | 27 | 


# Modified Contents
## articles/search/search-relevance-overview.md{#item-cb0e09}

<details>
<summary>Diff</summary>
````diff
@@ -1,19 +1,38 @@
 ---
 title: Relevance
 titleSuffix: Azure AI Search
-description: Describes how the scoring and ranking algorithms work in Azure AI Search and how to use them together.
+description: Describe strategies for producing relevant results  in Azure AI Search and explain how the scoring and ranking algorithms work and how to use them together.
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 12/04/2025
+ms.date: 12/08/2025
 ms.update-cycle: 180-days
 ---
 
 # Relevance in Azure AI Search
 
-In a query operation, the relevance of any given result is determined by a ranking algorithm that evaluates the strength of a match based on how closely the query corresponds to content in the search corpus. When a match is found, an algorithm assigns a score, and results are ranked by that score and the topmost results are returned in the response. 
+The true measure of relevance is *how well* a retrieved set of results meets your customer and user information needs. In this article, learn about:
+
++ The main strategies for producing relevant results in Azure AI Search
++ The mechanics of how relevance is measured
++ The actions you can take to improve relevance
+
+## Strategies for highly relevant results
+
+In Azure AI Search, two main strategies have emerged as the best approaches for producing highly relevant results.
+
++ Hybrid search with semantic reranker
++ Agentic retrieval (preview) with LLM-assisted query planning and answer formulation
+
+[Hybrid search](hybrid-search-overview.md) delivers on relevance by combining the precision of keyword search and the semantic similarity of vector search in a search request targeting a single index. Keyword search operates over a verbatim query. Vector search gets a vectorized version of the same query. The queries run in parallel, looking for precise and semantically similar matches. Results are merged, ranked, and then rescored using a semantic ranker that promotes the most relevant matches. Using keyword and vector search *together* offsets the weaknesses of each approach as a standalone solution. Semantic reranker is an extra component that contributes to a better outcome.
+
+[Agentic retrieval (preview)](agentic-retrieval-overview.md) delivers on relevance through smart integration with LLMs and a knowledge base that defines a search domain and returns output that's designed for LLM consumption. The LLM can analyze and transform queries. It can decompose complex questions into targeted subqueries, refine vague requests, or generalize narrow ones for broader scope. In most agentic retrieval workloads, the LLM answers the question using context from chat history, retrieval instructions, and a response that includes retrieved content, citations, and an activity log. This combination of LLM-assisted query planning, multi-source knowledge base search, and LLM-ready response formatting is how agentic retrieval returns highly relevant results.
+
+## How relevance is measured
+
+Regardless of how content is retrieved, the relevance of any given result is determined by a ranking algorithm that evaluates the strength of a match based on how closely the query corresponds to content in the search corpus. When a match is found, an algorithm assigns a score, and results are ranked by that score and the topmost results are returned in the response. 
 
 Ranking occurs whenever the query request is for agentic retrieval and classic search for keyword, vector, and hybrid queries. It doesn't occur if the query invokes strict pattern matching, such as a filter-only query or a specialized query form like autocomplete, suggestions, geospatial search, fuzzy search, or regular expression search. A uniform search score of 1.0 indicates the absence of a ranking algorithm.
 
@@ -104,7 +123,7 @@ POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/d
 }
 ```
 
-A response for the above query includes the original RRF `@search.core` and the `@search.rerankerScore`.
+A response for the previous query includes the original RRF `@search.core` and the `@search.rerankerScore`.
 
 ```json
   "value": [
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索関連性の概要の更新"
}
```

### Explanation
この変更は、Azure AI Searchの検索関連性に関する文書を更新するもので、新しい戦略や手法についての説明を追加しています。具体的には、結果がどのように関連性を持つかを評価する方法や、ランキングアルゴリズムについての詳細が強調されています。

変更点には、まず記事の説明が改訂され、Azure AI Searchでの関連性の重要性についての内容が強化されています。また、検索結果の関連性を高めるための主な戦略として「ハイブリッド検索」と「エージェンティック検索」が紹介されています。これにより、ユーザーはより関連性の高い結果を得るための具体的な方法を理解できるようになります。

さらに、関連性の測定方法についての詳細が追記され、検索クエリに対するランキングアルゴリズムの働きや、検索スコアの意味が説明されています。全体として、文書はより包括的で分かりやすい内容にアップデートされ、Azure AI Searchを利用する際の参考としての価値が向上しています。


