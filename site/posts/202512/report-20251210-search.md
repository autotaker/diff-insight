---
date: '2025-12-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7bfe620...MicrosoftDocs:2bf50f0
summary: このレポートでは、Azureの検索サービスに関するドキュメントが改善されたことが述べられています。具体的には、地域サポート文書にサービスティアの情報が追加され、検索関連性の説明がハイブリッド検索とエージェント型検索の観点から明確化されました。また、新機能は特に追加されていないものの、説明がより具体的で理解しやすくなるように修正されています。破壊的な変更はなく、主にドキュメントの改良が行われています。この改善により、ユーザーは検索結果の精度向上や必要なデータの準備に関する理解を深め、より適切にサービスを活用できるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7bfe620...MicrosoftDocs:2bf50f0){target="_blank"}

<format>
# ハイライト
- 地域サポート文書における具体的なサービスティア情報の追加。
- 検索関連性の概要において、ハイブリッド検索とエージェント型検索の説明が明確化。

## 新機能
特定の新機能は追加されていませんが、既存の説明に具体性を持たせ、理解を深める修正が行われました。

## 破壊的変更
特に破壊的な変更はありません。ドキュメントの改良が中心です。

## その他の更新
- Azure検索サービスの地域サポートに関し、特定のティアの制約についての明確化。
- 検索関連性について、ハイブリッド検索とエージェント型検索の説明が改良され、新しい用語が導入。

# インサイト
このコードの変更では、Azureの検索サービスに関するドキュメントが改善され、ユーザーがより適切にサービスを活用できるよう配慮されています。地域サポートに関するセクションでは、特に容量制約に関して、具体的なティア「Basic」および「S1」の情報が追加されたことで、ユーザーは選択肢をより緻密に判断できます。このようなクリアな情報提供は、ユーザーが不必要なトラブルを避け、ニーズに応じたサービスを利用するために重要です。

さらに、検索関連性に関する文書では、検索アルゴリズムの運用方法について、ハイブリッド検索とエージェント型検索の説明がわかりやすくなっています。特に、ハイブリッド検索での「キーワードクエリ」と「ベクトルクエリ」の組み合わせや、エージェント型検索におけるLLMとの統合が解説されたことで、実際の活用方法が具体的に示されています。これにより、ユーザーは検索結果の精度を高めるための最良のアプローチを理解できるでしょう。また、基盤データの質と量が検索の効果に影響することが明記されたことで、ユーザーは準備すべきデータについて考慮することができるようになります。このような詳細な説明は、ユーザーが検索戦略を効果的に実施し、ビジネスニーズに最も合った結果を引き出すための手助けとなるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-region-support.md](#item-25b0f1) | minor update | 検索地域サポートに関する文章の更新 | modified | 1 | 1 | 2 | 
| [search-relevance-overview.md](#item-cb0e09) | minor update | 検索関連性の概要に関する文章の更新 | modified | 4 | 2 | 6 | 


# Modified Contents
## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -57,7 +57,7 @@ You can create an Azure AI Search service in any of the following Azure public r
 
 <sup>1</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
 
-<sup>2</sup> This region is experiencing capacity constraints that prevent the creation of new search services and might present failures for scale operations. Please choose a different region.
+<sup>2</sup> This region is experiencing capacity constraints that prevent the creation of new search services for Basic and S1 tiers. Please choose a different region.
 
 <sup>3</sup> This region doesn't have indexer support for [Microsoft Purview sensitivity labels](search-indexer-sensitivity-labels.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索地域サポートに関する文章の更新"
}
```

### Explanation
この変更は、`articles/search/search-region-support.md`ファイルに対するマイナーな更新です。具体的には、Azureの検索サービスに関する地域サポートに関する文言が修正されました。修正前の文では、「新しい検索サービスの作成を妨げる容量制約」が説明されていましたが、修正後は「BasicおよびS1ティアの新しい検索サービスの作成が妨げられている」という具体的な情報が追加されました。この変更は、利用者に対して特定のサービスティアに関する明確な情報を提供し、適切な選択を促すためのアップデートです。

## articles/search/search-relevance-overview.md{#item-cb0e09}

<details>
<summary>Diff</summary>
````diff
@@ -26,9 +26,11 @@ In Azure AI Search, two main strategies have emerged as the best approaches for
 + Hybrid search with semantic reranker
 + Agentic retrieval (preview) with LLM-assisted query planning and answer formulation
 
-[Hybrid search](hybrid-search-overview.md) delivers on relevance by combining the precision of keyword search and the semantic similarity of vector search in a search request targeting a single index. Keyword search operates over a verbatim query. Vector search gets a vectorized version of the same query. The queries run in parallel, looking for precise and semantically similar matches. Results are merged, ranked, and then rescored using a semantic ranker that promotes the most relevant matches. Using keyword and vector search *together* offsets the weaknesses of each approach as a standalone solution. Semantic reranker is an extra component that contributes to a better outcome.
+[Hybrid search](hybrid-search-overview.md) delivers on relevance by combining the precision of keyword queries and the semantic similarity of vector queries in a search request targeting a single index. Keyword search operates over a verbatim query. Vector search runs an identical query using a vectorized version of the same string. The queries execute in parallel, looking for precise and semantically similar matches. Results are merged, ranked, and then rescored using a semantic ranker that promotes the most relevant matches. Using keyword and vector search *together* offsets the weaknesses of each approach as a standalone solution. Semantic reranker is an extra component that contributes to a better outcome.
 
-[Agentic retrieval (preview)](agentic-retrieval-overview.md) delivers on relevance through smart integration with LLMs and a knowledge base that defines a search domain and returns output that's designed for LLM consumption. The LLM can analyze and transform queries. It can decompose complex questions into targeted subqueries, refine vague requests, or generalize narrow ones for broader scope. In most agentic retrieval workloads, the LLM answers the question using context from chat history, retrieval instructions, and a response that includes retrieved content, citations, and an activity log. This combination of LLM-assisted query planning, multi-source knowledge base search, and LLM-ready response formatting is how agentic retrieval returns highly relevant results.
+[Agentic retrieval (preview)](agentic-retrieval-overview.md) delivers on relevance through smart integration with LLMs and a knowledge base that defines an entire search domain. The LLM can analyze and transform queries for more effective retrieval. It can decompose complex questions into targeted subqueries, refine vague requests, or generalize narrow ones for broader scope. In a typical agentic retrieval workload, the LLM answers the question using its reasoning power, context from chat history, and retrieval instructions to extract the very best content and use it to best advantage. This combination of LLM-assisted query planning, multi-source knowledge base search, and LLM reasoning is how agentic retrieval returns highly relevant results.
+
+Relevance also depends on having grounding data of sufficient quantity and quality. In agentic retrieval, you can list multiple knowledge sources to expand the scope of what's searchable and provide logic for selecting specific ones.
 
 ## How relevance is measured
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索関連性の概要に関する文章の更新"
}
```

### Explanation
この変更は、`articles/search/search-relevance-overview.md`ファイルに対するマイナーなアップデートです。修正内容は、検索の関連性に関する2つの主要な戦略に関する説明に加筆と修正が加えられました。具体的には、ハイブリッド検索とエージェント型検索のそれぞれの説明をより明確にし、効果的な検索を実現するための具体的なプロセスが強調されています。

ハイブリッド検索については、キーワード検索とベクトル検索の組み合わせの重要性が際立たされ、新たに「キーワードクエリ」と「ベクトルクエリ」という用語が導入されました。また、エージェント型検索に関しては、LLM（大規模言語モデル）とのスマートな統合について詳述され、クエリの変換や効果的な情報取得のためのプロセスが説明されています。さらに、関連性を高めるためには、十分な量と質の基盤データが重要であることが明記され、新しい文が追加されました。このアップデートは、利用者が検索戦略の効果をより理解しやすくするために行われました。


