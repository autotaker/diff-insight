---
date: '2024-09-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e3ea9cd...MicrosoftDocs:beebdfc
summary: このドキュメントの変更点は、主に「セマンティックランキング」という用語を「セマンティックランカー」に統一することに焦点を当てており、スコアリングプロファイルに関する重大な更新やファイアウォール設定、接続文字列プレースホルダーの改善も含まれています。新しいビジュアルコンテンツも追加され、特にスコアリングプロファイルの適用方法が視覚的に示されています。これにより、ユーザーは技術用語を一貫して理解しやすくなり、設定ミスが減るなど、ドキュメントの使い勝手が向上しています。全体として、これらのアップデートはAzure
  AI Searchの機能を最大限に活用するために必要な情報を提供し、理解しやすさと一貫性を高めるための重要な修正が含まれています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e3ea9cd...MicrosoftDocs:beebdfc){target="_blank"}

# Highlights
このドキュメントの変更点は、主に「セマンティックランキング」という用語を「セマンティックランカー」に統一することに焦点を当てています。また、スコアリングプロファイルに関する重大な更新と、ファイアウォール設定や接続文字列プレースホルダーの改善も含まれています。

## New features
- 新しいビジュアルコンテンツが追加されました（scoring-over-ranked-results.png）。

## Breaking changes
- スコアリングプロファイルのセクションが大幅に見直されたことによる重大な変更。

## Other updates
- 用語の一貫性を保つために「セマンティックランキング」を「セマンティックランカー」に変更。
- ファイアウォールの設定に関するIPアドレス情報や接続文字列プレースホルダーの更新。
- 日付の更新と細かい文言修正。

# Insights
このドキュメントの変更点は、主に用語の整合性と情報の明瞭化を目的としたものです。特に「セマンティックランキング」から「セマンティックランカー」への変更が多数のセクションで行われていますが、これによりユーザーが技術用語を一貫して理解しやすくなります。以下、具体的な変更点について解説します。

まず、重要な修正点としてスコアリングプロファイルの文書が挙げられます。このセクションは大幅に見直され、新しい機能やパラメータが詳細に説明されています。これによって、ユーザーはスコアリングプロファイルの定義や使用方法をより深く理解し、実際のクエリロジックへの応用がしやすくなっています。

次に、特定のドキュメントやサンプルコードでの接続文字列やIPアドレスのプレースホルダーがより直感的な形式に変更されました。例えば、`<YOUR-ACCOUNT-NAME>`のような形式に統一されており、ユーザーが具体的な値を置き換えやすくなっています。これにより設定ミスが減り、初学者にもわかりやすいドキュメントになっています。

また、ファイアウォール設定に関してIPアドレス情報が追加され、これにより異なるクラウド環境でアクセス設定を行う際に役立つ具体的なドメイン情報が提供されました。

最後に、更新されたドキュメントには新しいビジュアルコンテンツが追加されており、特にスコアリングプロファイルがどのように適用されるかを視覚的に示すものです。これは、理論的な説明だけでなく視覚的な理解も助けるため、ユーザーの学習効果を高めます。

総じて、この一連のアップデートはAzure AI Searchの機能を最大限に活用するために必要な情報をユーザーに提供するものであり、理解しやすさと整合性を高めるための重要な修正が含まれています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [hybrid-search-how-to-query.md](#item-345ce6) | minor update | ハイブリッド検索のクエリ方法に関するドキュメントの修正 | modified | 5 | 5 | 10 | 
| [hybrid-search-overview.md](#item-6987b4) | minor update | ハイブリッド検索の概要に関する文書の修正 | modified | 2 | 2 | 4 | 
| [hybrid-search-ranking.md](#item-dad887) | minor update | ハイブリッド検索ランキングに関する文書の修正 | modified | 2 | 2 | 4 | 
| [dotnet-semantic.md](#item-2d423d) | minor update | セマンティック検索のクイックスタートに関する修正 | modified | 1 | 1 | 2 | 
| [python-semantic.md](#item-4cc2ee) | minor update | Pythonによるセマンティック検索のクイックスタートに関する修正 | modified | 1 | 1 | 2 | 
| [index-add-scoring-profiles.md](#item-bf4f02) | breaking change | スコアリングプロファイルの追加と大幅な内容変更 | modified | 54 | 82 | 136 | 
| [knowledge-store-create-portal.md](#item-9b92e5) | minor update | 知識ストア作成ドキュメントの接続文字列の表記修正 | modified | 1 | 1 | 2 | 
| [scoring-over-ranked-results.png](#item-bee24f) | new feature | スコアリングプロファイルのビジュアル追加 | added | 0 | 0 | 0 | 
| [query-lucene-syntax.md](#item-736436) | minor update | Lucene構文に関する例の参照更新 | modified | 1 | 1 | 2 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | セマンティックランキングの名称変更 | modified | 2 | 2 | 4 | 
| [samples-dotnet.md](#item-12f3fa) | minor update | セマンティックランキングの表現変更 | modified | 2 | 2 | 4 | 
| [samples-python.md](#item-d2bf09) | minor update | セマンティックランキングの表現変更 | modified | 1 | 1 | 2 | 
| [search-api-migration.md](#item-07297b) | minor update | セマンティックランカーの表現変更 | modified | 5 | 5 | 10 | 
| [search-create-service-portal.md](#item-f90159) | minor update | セマンティックランカーの表現変更 | modified | 2 | 2 | 4 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | セマンティックランカーの表現変更 | modified | 2 | 2 | 4 | 
| [search-get-started-rag.md](#item-05ff0e) | minor update | セマンティックランカーの用語更新 | modified | 3 | 3 | 6 | 
| [search-get-started-semantic.md](#item-2b3902) | minor update | セマンティックランカーへの用語変更 | modified | 7 | 7 | 14 | 
| [search-get-started-vector.md](#item-4984d9) | minor update | セマンティックランカーへの用語変更 | modified | 1 | 1 | 2 | 
| [search-indexer-tutorial.md](#item-a3e3ff) | minor update | 接続文字列のプレースホルダーを更新 | modified | 3 | 3 | 6 | 
| [search-manage-rest.md](#item-405ec7) | minor update | セマンティックランカーの呼称変更 | modified | 4 | 6 | 10 | 
| [search-manage.md](#item-4043d7) | minor update | セマンティックランカーへの用語変更 | modified | 3 | 3 | 6 | 
| [search-pagination-page-layout.md](#item-115902) | minor update | セマンティックランカーへの用語変更 | modified | 1 | 1 | 2 | 
| [search-region-support.md](#item-25b0f1) | minor update | セマンティックランキングの用語変更 | modified | 8 | 23 | 31 | 
| [search-security-manage-encryption-keys.md](#item-db3487) | minor update | 暗号化キーのサンプル設定のプレースホルダー更新 | modified | 44 | 44 | 88 | 
| [search-semi-structured-data.md](#item-d3388d) | minor update | 検索サービス名のプレースホルダーの変更 | modified | 4 | 4 | 8 | 
| [semantic-answers.md](#item-c3fee9) | minor update | セマンティックレンカーへの表記変更 | modified | 2 | 2 | 4 | 
| [semantic-how-to-configure.md](#item-7a92a6) | minor update | セマンティックランキングの呼称変更 | modified | 1 | 1 | 2 | 
| [semantic-how-to-enable-disable.md](#item-71ac1e) | minor update | セマンティックランキングの呼称変更 | modified | 6 | 6 | 12 | 
| [semantic-how-to-query-request.md](#item-85530d) | minor update | セマンティックランキングの呼称変更 | modified | 5 | 5 | 10 | 
| [semantic-search-overview.md](#item-b7497b) | minor update | セマンティックランキングの用語変更 | modified | 12 | 12 | 24 | 
| [service-configure-firewall.md](#item-75be3f) | minor update | ファイアウォール設定のためのIPアドレス情報の追加 | modified | 6 | 3 | 9 | 
| [speller-how-to-add.md](#item-9b4502) | minor update | セマンティックランキングの用語変更 | modified | 2 | 2 | 4 | 
| [toc.yml](#item-c4768f) | minor update | セマンティックレンカーの用語変更 | modified | 4 | 4 | 8 | 
| [tutorial-csharp-search-query-integration.md](#item-8ad6b5) | minor update | Search APIリファレンスのリンク更新 | modified | 4 | 4 | 8 | 
| [tutorial-rag-build-solution-pipeline.md](#item-25ce01) | minor update | セマンティックランキング用語の修正 | modified | 1 | 1 | 2 | 
| [vector-search-how-to-query.md](#item-9bb93c) | minor update | ドキュメントの日付更新と内容の修正 | modified | 3 | 3 | 6 | 
| [vector-search-integrated-vectorization-ai-studio.md](#item-353fcc) | minor update | プレースホルダーの形式修正 | modified | 13 | 13 | 26 | 
| [vector-store.md](#item-db9b8c) | minor update | 文書の表現の微修正 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-fa71b4) | minor update | 用語の微調整 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/search/hybrid-search-how-to-query.md{#item-345ce6}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ To improve relevance, use these parameters:
 
 + A search index containing `searchable` vector and nonvector fields. See [Create an index](search-how-to-create-search-index.md) and [Add vector fields to a search index](vector-search-how-to-create-index.md).
 
-+ (Optional) If you want [semantic ranking](semantic-how-to-configure.md), your search service must be Basic tier or higher, with [semantic ranking enabled](semantic-how-to-enable-disable.md).
++ (Optional) If you want the [semantic ranker](semantic-search-overview.md), your search service must be Basic tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
 + (Optional) If you want text-to-vector conversion of a query string, [create and assign a vectorizer](vector-search-how-to-configure-vectorizer.md) to vector fields in the search index.
 
@@ -167,7 +167,7 @@ api-key: {{admin-api-key}}
 
 ## Semantic hybrid search
 
-Assuming that you [enabled semantic ranking](semantic-how-to-enable-disable.md) and your index definition includes a [semantic configuration](semantic-how-to-query-request.md), you can formulate a query that includes vector search and keyword search, with semantic ranking over the merged result set. Optionally, you can add captions and answers. 
+Assuming that you [enabled semantic ranker](semantic-how-to-enable-disable.md) and your index definition includes a [semantic configuration](semantic-how-to-query-request.md), you can formulate a query that includes vector search and keyword search, with semantic ranking over the merged result set. Optionally, you can add captions and answers. 
 
 ```http
 POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-07-01
@@ -200,7 +200,7 @@ api-key: {{admin-api-key}}
 
 **Key points:**
 
-+ Semantic ranking accepts up to 50 results from the merged response.
++ Semantic ranker accepts up to 50 results from the merged response.
 
 + "queryType" and "semanticConfiguration" are required.
 
@@ -353,9 +353,9 @@ Both "k" and "top" are optional. Unspecified, the default number of results in a
 > [!NOTE]
 > The semantic ranker can take up to 50 results. 
 
-If you're using semantic ranking in 2024-05-01-preview API, it's a best practice to set "k" and "maxTextRecallSize" to sum to at least 50 total.  You can then restrict the results returned to the user with the "top" parameter. 
+If you're using semantic ranker in 2024-05-01-preview API, it's a best practice to set "k" and "maxTextRecallSize" to sum to at least 50 total.  You can then restrict the results returned to the user with the "top" parameter. 
 
-If you're using semantic ranking in previous APIs do the following:
+If you're using semantic ranker in previous APIs do the following:
 
 + if doing keyword-only search (no vector) set "top" to 50
 + if doing hybrid search set "k" to 50, to ensure that the semantic ranker gets at least 50 results. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索のクエリ方法に関するドキュメントの修正"
}
```

### Explanation
この更新は、ハイブリッド検索に関するドキュメント内の用語の一貫性を高めるためのマイナーな修正です。具体的には、「セマンティックランク」および「セマンティックランキング」の用語の使い方を明確にし、より一貫性のある表現に変更しました。

主な変更点には以下が含まれます：
- "semantic ranking" を "semantic ranker" に置き換え、セマンティックランカーの機能や要件が明確に示されるようにしました。
- セマンティックランカーが有効であることや、検索サービスが基本ティア以上である必要がある旨を繰り返し強調しました。
- 説明の一部にテキストからベクトルへの変換に関する情報を追加し、ベクトライザーの設定手順を明記しました。
  
これにより、読者はハイブリッド検索の使用方法についてより具体的な情報を得ることができ、理解が深まることを目指しています。

## articles/search/hybrid-search-overview.md{#item-6987b4}

<details>
<summary>Diff</summary>
````diff
@@ -68,7 +68,7 @@ Key points include:
 + `select` specifies which fields to return in results, which can be text fields that are human readable.
 + `filters` can specify geospatial search or other include and exclude criteria, such as whether parking is included. The geospatial query in this example finds hotels within a 300-kilometer radius of Washington D.C.
 + `facets` can be used to compute facet buckets over results that are returned from hybrid queries.
-+ `queryType=semantic` invokes semantic ranking, applying machine reading comprehension to surface more relevant search results.
++ `queryType=semantic` invokes semantic ranker, applying machine reading comprehension to surface more relevant search results.
 
 Filters and facets target data structures within the index that are distinct from the inverted indexes used for full text search and the vector indexes used for vector search. As such, when filters and faceted operations execute, the search engine can apply the operational result to the hybrid search results in the response.
 
@@ -124,7 +124,7 @@ A response from the above query might look like this:
 
 Hybrid search combines the strengths of vector search and keyword search. The advantage of vector search is finding information that's conceptually similar to your search query, even if there are no keyword matches in the inverted index. The advantage of keyword or full text search is precision, with the ability to apply semantic ranking that improves the quality of the initial results. Some scenarios - such as querying over product codes, highly specialized jargon, dates, and people's names - can perform better with keyword search because it can identify exact matches.
 
-Benchmark testing on real-world and benchmark datasets indicates that hybrid retrieval with semantic ranking offers significant benefits in search relevance.
+Benchmark testing on real-world and benchmark datasets indicates that hybrid retrieval with semantic ranker offers significant benefits in search relevance.
 
 The following video explains how hybrid retrieval gives you optimal grounding data for generating useful AI responses.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索の概要に関する文書の修正"
}
```

### Explanation
この変更は、ハイブリッド検索に関する文書の一部で用語の一貫性を高めるためのマイナーな修正を行ったものです。「セマンティックランキング」から「セマンティックランカー」への用語の変更が主な内容です。

具体的な変更点は以下の通りです：
- "semantic ranking" を "semantic ranker" に置き換えることで、セマンティック検索の機能に関する用語を統一しました。これにより、読者が用語の意味をより正確に理解できるようにしています。
- 追加されたコンテンツでは、クエリのキー要素についての説明がわかりやすくなっており、特に `queryType=semantic` がどのようにセマンティックランカーを呼び出すかが明確になっています。

この修正により、ハイブリッド検索技術の重要な概念がより一貫して説明され、理解を促進することが期待されています。

## articles/search/hybrid-search-ranking.md{#item-dad887}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 06/12/2024
+ms.date: 09/24/2024
 ---
 
 # Relevance scoring in hybrid search using Reciprocal Rank Fusion (RRF)
@@ -55,7 +55,7 @@ The following chart identifies the scoring property returned on each match, algo
 | hybrid search | `@search.score` | RRF algorithm | Upper limit is bounded by the number of queries being fused, with each query contributing a maximum of approximately 1 to the RRF score. For example, merging three queries would produce higher RRF scores than if only two search results are merged. |
 | semantic ranking | `@search.rerankerScore` | Semantic ranking | 0.00 - 4.00 |
 
-Semantic ranking doesn't participate in RRF. Its score (`@search.rerankerScore`) is always reported separately in the query response. Semantic ranking can rerank full text and hybrid search results, assuming those results include fields having semantically rich content.
+Semantic ranking occurs after RRF merging of results. Its score (`@search.rerankerScore`) is always reported separately in the query response. Semantic ranker can rerank full text and hybrid search results, assuming those results include fields having semantically rich content. It can rerank pure vector queries if the search documents include text fields that contain semantically relevant content.
 
 ## Weighted scores
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索ランキングに関する文書の修正"
}
```

### Explanation
この変更は、ハイブリッド検索における関連性スコアリングに関する文書に対するマイナーな修正であり、主に語句の明確化を目的としています。

具体的な変更点は以下の通りです：
- 文書内の日付が「2024年6月12日」から「2024年9月24日」に更新されました。これは情報の正確性を保つための更新です。
- セマンティックランキングの説明において、セマンティックランキングがRRF（逆数ランク融合）の結果の後に行われることが明確にされました。また、セマンティックスコアが常にクエリ応答の中で個別に報告されることも強調されています。
- セマンティックランカーが純粋なベクトルクエリを再ランク付けできる条件についても強調され、文書の明瞭さが向上しました。

これにより、読者はハイブリッド検索のスコアリングメカニズムについて、より理解しやすく、正確な情報を得ることができるようになります。

## articles/search/includes/quickstarts/dotnet-semantic.md{#item-2d423d}

<details>
<summary>Diff</summary>
````diff
@@ -115,7 +115,7 @@ Azure AI Search searches over content stored in the service. The code for upload
 
 #### Search an index
 
-Here's a query that invokes semantic ranking, with search options for specifying parameters:
+Here's a query that invokes semantic ranker, with search options for specifying parameters:
 
 ```csharp
 Console.WriteLine("Example of a semantic query.");
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティック検索のクイックスタートに関する修正"
}
```

### Explanation
この変更は、.NETを用いたセマンティック検索に関するクイックスタートドキュメントの用語に関するマイナーな修正です。

具体的な変更点は以下の通りです：
- 説明文における「semantic ranking」（セマンティックランキング）が「semantic ranker」（セマンティックランカー）に変更されました。この修正により、セマンティック検索機能に関する用語の一貫性が高まります。

この変更は、ユーザーがセマンティックランカーの機能と用途をより正確に理解できるように配慮されたものです。全体として、文書の明瞭さと正確性の向上に寄与しています。

## articles/search/includes/quickstarts/python-semantic.md{#item-4cc2ee}

<details>
<summary>Diff</summary>
````diff
@@ -285,7 +285,7 @@ for result in results:
 
 In this final query, return semantic answers.
 
-Semantic ranking can generate answers to a query string that has the characteristics of a question. The generated answer is extracted verbatim from your content. To get a semantic answer, the question and answer must be closely aligned, and the model must find content that clearly answers the question. If potential answers fail to meet a confidence threshold, the model doesn't return an answer. For demonstration purposes, the question in this example is designed to get a response so that you can see the syntax.
+Semantic ranker can generate answers to a query string that has the characteristics of a question. The generated answer is extracted verbatim from your content. To get a semantic answer, the question and answer must be closely aligned, and the model must find content that clearly answers the question. If potential answers fail to meet a confidence threshold, the model doesn't return an answer. For demonstration purposes, the question in this example is designed to get a response so that you can see the syntax.
 
 ```python
 # Run a semantic query that returns semantic answers  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonによるセマンティック検索のクイックスタートに関する修正"
}
```

### Explanation
この変更は、Pythonを用いたセマンティック検索のクイックスタートドキュメントに関するマイナーな用語の修正です。

具体的な変更点は以下の通りです：
- 「semantic ranking」（セマンティックランキング）の表現が「semantic ranker」（セマンティックランカー）に変更されました。この変更により、セマンティック検索機能に対するより正確な表現が提供されています。

この修正は、読者がセマンティックランカーの機能を理解する上での明瞭さを向上させ、用語の一貫性を保つために重要です。全体として、ドキュメントの内容がより理解しやすくなっています。

## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -10,22 +10,34 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 11/06/2023
+ms.date: 09/23/2024
 ---
 
 # Add scoring profiles to boost search scores
 
-In this article, you'll learn how to define a scoring profile. A scoring profile is critera for boosting a search score based on parameters that you provide. For example, you might want matches found in a "tags" field to be more relevant than the same match found in "descriptions". Criteria can be a weighted field (such as the "tags" example) or a function. 
+Scoring profiles allow you to boost the ranking of matching documents based on criteria. In this article, learn how to specify and assign a scoring profile that boosts a search score based on parameters that you provide. 
 
-Scoring profiles are defined in a search index and invoked on non-vector fields in query requests. You can create multiple profiles and then modify query logic to choose which one is used.
+You can use scoring profiles for [keyword search](search-lucene-query-architecture.md), [vector search](vector-search-overview.md), and [hybrid search](hybrid-search-overview.md). However, scoring profiles only apply to nonvector fields, so make sure your index has text or numeric fields that can be used in a scoring profile. Scoring profile support for vector and hybrid search is available in 2024-05-01-preview and 2024-07-01 REST APIs and in Azure SDK packages that targeting those releases.
+
+## Key points about scoring profiles
+
+Scoring profile parameters are either:
+
++ Weighted fields, where a match is found in a specific string field. For example, you might want matches found in a "summary" field to be more relevant than the same match found in a "content" field.
+
++ Functions for numeric data, including dates, ranges, and geographic coordinates. There's also a Tags function that operates on a field providing an arbitrary collection of strings. You can choose this approach over weighted fields if you want to boost a score based on whether a match is found in a tags field.
+
+You can create multiple profiles and then modify query logic to choose which one is used.
+
+You can have up to 100 scoring profiles within an index (see [service Limits](search-limits-quotas-capacity.md)), but you can only specify one profile at time in any given query.
 
 > [!NOTE]
-> Unfamiliar with relevance concepts? The following [video segment on YouTube](https://www.youtube.com/embed/Y_X6USgvB1g?version=3&start=463&end=970) fast-forwards to how scoring profiles work in Azure AI Search. You can also visit [Relevance and scoring in Azure AI Search](index-similarity-and-scoring.md) for more background.
+> Unfamiliar with relevance concepts? Visit [Relevance and scoring in Azure AI Search](index-similarity-and-scoring.md) for background. You can also watch this [video segment on YouTube](https://www.youtube.com/embed/Y_X6USgvB1g?version=3&start=463&end=970) for scoring profiles over BM25-ranked results.
 >
 
 ## Scoring profile definition
 
-A scoring profile is named object defined in an index schema. A profile can be composed of weighted fields, functions, and parameters.
+A scoring profile is named object defined in an index schema. A scoring profile is composed of weighted fields, functions, and parameters.
 
 The following definition shows a simple profile named "geo". This example boosts results that have the search term in the hotelName field. It also uses the `distance` function to favor results that are within 10 kilometers of the current location. If someone searches on the term 'inn', and 'inn' happens to be part of the hotel name, documents that include hotels with 'inn' within a 10 KM radius of the current location will appear higher in the search results.  
 
@@ -73,52 +85,45 @@ POST /indexes/hotels/docs&api-version=2024-07-01
 
 This query searches on the term "inn" and passes in the current location. Notice that this query includes other parameters, such as scoringParameter. Query parameters, including "scoringParameter", are described in [Search Documents (REST API)](/rest/api/searchservice/documents/search-post).  
 
-See the [Extended example](#bkmk_ex) to review a more detailed example of a scoring profile.  
-
-<a name=what-is-default-scoring></a>
-
-## How scores are computed
-
-Scores are computed for full text search queries. Matches are scored based on how relevant the match is, and the highest scoring matches are returned in the query response. The overall score for each document is an aggregation of the individual scores for each field, where the individual score of each field is computed based on the term frequency and document frequency of the searched terms within that field (known as [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) or term frequency-inverse document frequency). 
+See the [Extended example for vector and hybrid search](#extended-example-for-vector-and-hybrid-search) and [Extended example for keyword search](#extended-example-for-keyword-search) for more scenarios.
 
-You can use the [featuresMode (preview)](index-similarity-and-scoring.md#featuresmode-parameter-preview) parameter to request extra scoring details with the search results (including the field level scores).
+## How search scoring works in Azure AI Search
 
-## When to add scoring logic
+Scoring profiles supplement the default scoring algorithm by boosting the scores of matches that meet the profile's criteria. Scoring functions apply to keyword search, pure vector queries, and on hybrid queries. 
 
-You should create one or more scoring profiles when the default ranking behavior doesn’t go far enough in meeting your business objectives. For example, you might decide that search relevance should favor newly added items. Likewise, you might have a field that contains profit margin, or some other field indicating revenue potential. Boosting results that are more meaningful to your users or the business is often the deciding factor in adoption of scoring profiles.
+When you use scoring profiles or any other boosting features in Azure AI Search, the [Reciprocal Ranking Function (RRF)](hybrid-search-ranking.md) algorithm assigns the score, including for standalone text and vector queries. Post-RRF, all scoring/boosting, [semantic ranking](semantic-search-overview.md), and [vector weighting](vector-search-how-to-query.md#vector-weighting) adjustments occur.
 
-Relevancy-based ordering in a search page is also implemented through scoring profiles. Consider search results pages you’ve used in the past that let you sort by price, date, rating, or relevance. In Azure AI Search, scoring profiles can be used to drive the ‘relevance’ option. The definition of relevance is user-defined, predicated on business objectives and the type of search experience you want to deliver.  
+:::image type="content" source="media/scoring-profiles/scoring-over-ranked-results.png" alt-text="Diagram showing which fields have a scoring profile and when ranking occurs.":::
 
-## Steps for adding a scoring profile
+> [!TIP]
+> You can use the [featuresMode (preview)](index-similarity-and-scoring.md#featuresmode-parameter-preview) parameter to request extra scoring details with the search results (including the field level scores).
 
-To implement custom scoring behavior, add a scoring profile to the schema that defines the index. You can have up to 100 scoring profiles within an index (see [Service Limits](search-limits-quotas-capacity.md)), but you can only specify one profile at time in any given query.
+## Add a scoring profile to a search index
 
-1. Start with an index definition. You can add and update scoring profiles on an existing index without having to rebuild it. Use an [Update Index](/rest/api/searchservice/indexes/create-or-update) request to post your revision.
+1. Start with an [index definition](/rest/api/searchservice/indexes/create). You can add and update scoring profiles on an existing index without having to rebuild it. Use an [Create or Update Index](/rest/api/searchservice/indexes/create-or-update) request to post a revision.
 
-1. Paste in the [Template](#bkmk_template) provided in this article.  
+1. Paste in the [template](#template) provided in this article.  
 
-1. Provide a name. Scoring profiles are optional, but if you add one, the name is required. Be sure to follow Azure AI Search [naming conventions](/rest/api/searchservice/naming-rules) for fields (starts with a letter, avoids special characters and reserved words).  
+1. Provide a name that adheres to [naming conventions](/rest/api/searchservice/naming-rules).
 
-1. Specify boosting criteria. A single profile can contain [weighted fields](#weighted-fields), [functions](#functions), or both. 
+1. Specify boosting criteria. A single profile can contain [text weighted fields](#use-text-weighted-fields), [functions](#use-functions), or both. 
 
 You should work iteratively, using a data set that will help you prove or disprove the efficacy of a given profile.
 
 Scoring profiles can be defined in Azure portal as shown in the following screenshot, or programmatically through [REST APIs](/rest/api/searchservice/indexes/create-or-update) or in Azure SDKs, such as the [ScoringProfile](/dotnet/api/azure.search.documents.indexes.models.scoringprofile) class in the Azure SDK for .NET.
 
    :::image type="content" source="media/scoring-profiles/portal-add-scoring-profile-small.png" alt-text="Add scoring profiles page" lightbox="media/scoring-profiles/portal-add-scoring-profile.png" border="true":::
 
-<a name="weighted-fields"></a>
+## Use text-weighted fields
 
-### Using weighted fields
+Use text-weighted fields when field context is important and queries include `searchable` string fields. For example, if a query includes the term "airport", you might want "airport" in the Description field to have more weight than in the HotelName. 
 
-Use weighted fields when field context is important and queries are full text search. For example, if a query includes the term "airport", you might want "airport" in the Description field to have more weight than in the HotelName. 
-
-Weighted fields are composed of a searchable field and a positive number that is used as a multiplier. If the original field score of HotelName is 3, the boosted score for that field becomes 6, contributing to a higher overall score for the parent document itself.
+Weighted fields are name-value pairs composed of a `searchable` field and a positive number that is used as a multiplier. If the original field score of HotelName is 3, the boosted score for that field becomes 6, contributing to a higher overall score for the parent document itself.
 
 ```json
 "scoringProfiles": [  
     {  
-      "name": "boostKeywords",  
+      "name": "boostSearchTerms",  
       "text": {  
         "weights": {  
           "HotelName": 2,  
@@ -129,30 +134,27 @@ Weighted fields are composed of a searchable field and a positive number that is
 ]
 ```
 
-<a name="functions"></a>
-
-### Using functions
+## Use functions
 
 Use functions when simple relative weights are insufficient or don't apply, as is the case of distance and freshness, which are calculations over numeric data. You can specify multiple functions per scoring profile. For more information about the EDM data types used in Azure AI Search, see [Supported data types](/rest/api/searchservice/supported-data-types).
 
-| Function | Description |
+| Function | Description | Use cases |
 |-|-|
-| "freshness" | Boosts by values in a datetime field (`Edm.DateTimeOffset`). This function has a "boostingDuration" attribute so that you can specify a value representing a timespan over which boosting occurs. | 
-| "magnitude" | Boosts based on how high or low a numeric value is. Scenarios that call for this function include boosting by profit margin, highest price, lowest price, or a count of downloads. This function can only be used with `Edm.Double` and `Edm.Int` fields. For the magnitude function, you can reverse the range, high to low, if you want the inverse pattern (for example, to boost lower-priced items more than higher-priced items). Given a range of prices from $100 to $1, you would set "boostingRangeStart" at 100 and "boostingRangeEnd" at 1 to boost the lower-priced items. | 
-| "distance"  | Boosts by proximity or geographic location. This function can only be used with `Edm.GeographyPoint` fields. | 
-| "tag"  | Boosts by tags that are common to both search documents and query strings. Tags are provided in a "tagsParameter". This function can only be used with search fields of type `Edm.String` and `Collection(Edm.String)`. | 
+| distance  | Boost by proximity or geographic location. This function can only be used with `Edm.GeographyPoint` fields. | Use for "find near me" scenarios. |
+| freshness | Boost by values in a datetime field (`Edm.DateTimeOffset`). [Set boostingDuration](#set-boostingduration-for-freshness-function) to specify a value representing a timespan over which boosting occurs. | Use when you want to boost by newer or older dates. Rank items like calendar events with future dates such that items closer to the present can be ranked higher than items further in the future. One end of the range is fixed to the current time. To boost a range of times in the past, use a positive boostingDuration. To boost a range of times in the future, use a negative boostingDuration. |
+| magnitude | Alter rankings based on the range of values for a numeric field. The value must be an integer or floating-point number. For star ratings of 1 through 4, this would be 1. For margins over 50%, this would be 50. This function can only be used with `Edm.Double` and `Edm.Int` fields. For the magnitude function, you can reverse the range, high to low, if you want the inverse pattern (for example, to boost lower-priced items more than higher-priced items). Given a range of prices from $100 to $1, you would set `boostingRangeStart` at 100 and `boostingRangeEnd` at 1 to boost the lower-priced items. | Use when you want to boost by profit margin, ratings, clickthrough counts, number of downloads, highest price, lowest price, or a count of downloads. When two items are relevant, the item with the higher rating will be displayed first. |
+| tag  | Boost by tags that are common to both search documents and query strings. Tags are provided in a `tagsParameter`. This function can only be used with search fields of type `Edm.String` and `Collection(Edm.String)`. | Use when you have tag fields. If a given tag within the list is itself a comma-delimited list, you can [use a text normalizer](search-normalizers.md) on the field to strip out the commas at query time (map the comma character to a space). This approach will "flatten" the list so that all terms are a single, long string of comma-delimited terms. | 
 
 ### Rules for using functions
 
-+ Functions can only be applied to fields that are attributed as filterable.
++ Functions can only be applied to fields that are attributed as `filterable`.
 + Function type ("freshness", "magnitude", "distance", "tag") must be lower case.
 + Functions can't include null or empty values.
-
-<a name="bkmk_template"></a>
++ Functions can only have a single field per function definition. To use magnitude twice in the same profile, provide two definitions magnitude, one for each field.
 
 ## Template
 
- This section shows the syntax and template for scoring profiles. Refer to [Property reference](#bkmk_indexref) in the next section for descriptions of the scoring profile attributes.  
+ This section shows the syntax and template for scoring profiles. For a description of properties, see the [REST API reference](/rest/api/searchservice/indexes/create?view=rest-searchservice-2024-07-01&preserve-view=true#scoringfunctionaggregation).
 
 ```json
 "scoringProfiles": [  
@@ -201,54 +203,22 @@ Use functions when simple relative weights are insufficient or don't apply, as i
   }   
 ],   
 "defaultScoringProfile": (optional) "...", 
-```  
-
-<a name="bkmk_indexref"></a> 
-
-## Property reference
-
-|Attribute|Description|  
-|---------------|-----------------|  
-| name | Required. This is the name of the scoring profile. It follows the same naming conventions of a field. It must start with a letter, can't contain dots, colons or @ symbols, and can't start with the phrase azureSearch (case-sensitive).|  
-| text | Contains the weights property.|  
-| weights | Optional. Name-value pairs that specify a searchable field and a positive integer or floating-point number by which to boost a field's score. The positive integer or number becomes a multiplier for the original field score generated by the ranking algorithm. For example, if a field score is 2 and the weight value is 3, the boosted score for the field becomes 6. Individual field scores are then aggregated to create a document field score, which is then used to rank the document in the result set. |  
-| functions | Optional. A scoring function can only be applied to fields that are filterable.|  
-| functions > type | Required for scoring functions. Indicates the type of function to use. Valid values include magnitude, freshness, distance, and tag. You can include more than one function in each scoring profile. The function name must be lower case.|  
-| functions > boost | Required for scoring functions. A positive number used as multiplier for raw score. It can't be equal to 1.|  
-| functions > fieldname | Required for scoring functions. A scoring function can only be applied to fields that are part of the field collection of the index, and that are filterable. In addition, each function type introduces additional restrictions (freshness is used with datetime fields, magnitude with integer or double fields, and distance with location fields). You can only specify a single field per function definition. For example, to use magnitude twice in the same profile, you would need to include two definitions magnitude, one for each field.|  
-| functions > interpolation | Required for scoring functions. Defines the slope for which the score boosting increases from the start of the range to the end of the range. Valid values include Linear (default), Constant, Quadratic, and Logarithmic. See [Set interpolations](#bkmk_interpolation) for details.|  
-| functions > magnitude | The magnitude scoring function is used to alter rankings based on the range of values for a numeric field. Some of the most common usage examples of this are: </br></br>"Star ratings:" Alter the scoring based on the value within the "Star Rating" field. When two items are relevant, the item with the higher rating will be displayed first. </br>"Margin:" When two documents are relevant, a retailer may wish to boost documents that have higher margins first. </br>"Click counts:" For applications that track click through actions to products or pages, you could use magnitude to boost items that tend to get the most traffic. </br>"Download counts:" For applications that track downloads, the magnitude function lets you boost items that have the most downloads.|  
-| functions > magnitude > boostingRangeStart | Sets the start value of the range over which magnitude is scored. The value must be an integer or floating-point number. For star ratings of 1 through 4, this would be 1. For margins over 50%, this would be 50.|  
-| functions > magnitude > boostingRangeEnd | Sets the end value of the range over which magnitude is scored. The value must be an integer or floating-point number. For star ratings of 1 through 4, this would be 4.|  
-| functions > magnitude > constantBoostBeyondRange | Valid values are true or false (default). When set to true, the full boost will continue to apply to documents that have a value for the target field that’s higher than the upper end of the range. If false, the boost of this function won’t be applied to documents having a value for the target field that falls outside of the range.|  
-| functions > freshness | The freshness scoring function is used to alter ranking scores for items based on values in DateTimeOffset fields. For example, an item with a more recent date can be ranked higher than older items. </br></br>It's also possible to rank items like calendar events with future dates such that items closer to the present can be ranked higher than items further in the future. </br></br>In the current service release, one end of the range will be fixed to the current time. The other end is a time in the past based on the boostingDuration. To boost a range of times in the future, use a negative boostingDuration. </br></br>The rate at which the boosting changes from a maximum and minimum range is determined by the Interpolation applied to the scoring profile (see the figure below). To reverse the boosting factor applied, choose a boost factor of less than 1.|  
-| functions > freshness > boostingDuration | Sets an expiration period after which boosting will stop for a particular document. See [Set boostingDuration](#bkmk_boostdur) in the following section for syntax and examples.|  
-| functions > distance | The distance scoring function is used to affect the score of documents based on how close or far they're relative to a reference geographic location. The reference location is given as part of the query in a parameter (using the scoringParameter query parameter) as a `lon,lat` argument.|  
-|functions >  distance > referencePointParameter | A parameter to be passed in queries to use as reference location (using the scoringParameter query parameter). |  
-| functions > distance > boostingDistance | A number that indicates the distance in kilometers from the reference location where the boosting range ends.|  
-| functions > tag | The tag scoring function is used to affect the score of documents based on tags in documents and search queries. Documents that have tags in common with the search query will be boosted. The tags for the search query are provided as a scoring parameter in each search request (using the scoringParameter query parameter). |  
-| functions > tag > tagsParameter | A parameter to be passed in queries to specify tags for a particular request (using the scoringParameter query parameter). The parameter consists of a comma-delimited list of whole terms. If a given tag within the list is itself a comma-delimited list, you can [use a text normalizer](search-normalizers.md) on the field to strip out the commas at query time (map the comma character to a space). This approach will "flatten" the list so that all terms are a single, long string of comma-delimited terms. |  
-| functionAggregation | Optional. Applies only when functions are specified. Valid values include: sum (default), average, minimum, maximum, and firstMatching. A search score is single value that is computed from multiple variables, including multiple functions. This attribute indicates how the boosts of all the functions are combined into a single aggregate boost that then is applied to the base document score. The base score is based on the [tf-idf](https://wikipedia.org/wiki/Tf%E2%80%93idf) value computed from the document and the search query.|  
-| defaultScoringProfile | When executing a search request, if no scoring profile is specified, then default scoring is used ([tf-idf](https://wikipedia.org/wiki/Tf%E2%80%93idf) only). </br></br>You can override the built-in default, substituting a custom profile as the one to use when no specific profile is given in the search request.|  
-
-<a name="bkmk_interpolation"></a> 
+```
 
 ## Set interpolations
 
-Interpolations allow you to set the shape of the slope used for scoring. Because scoring is high to low, the slope is always decreasing, but the interpolation determines the curve of the downward slope. The following interpolations can be used:  
+Interpolations set the shape of the slope used for scoring. Because scoring is high to low, the slope is always decreasing, but the interpolation determines the curve of the downward slope. The following interpolations can be used:  
 
 | Interpolation | Description |  
 |-|-|  
-|`linear`|For items that are within the max and min range, the boost applied to the item will be done in a constantly decreasing amount. Linear is the default interpolation for a scoring profile.|  
-|`constant`|For items that are within the start and ending range, a constant boost will be applied to the rank results.|  
-|`quadratic`|In comparison to a Linear interpolation that has a constantly decreasing boost, Quadratic will initially decrease at smaller pace and then as it approaches the end range, it decreases at a much higher interval. This interpolation option isn't allowed in tag scoring functions.|  
-|`logarithmic`|In comparison to a Linear interpolation that has a constantly decreasing boost, Logarithmic will initially decrease at higher pace and then as it approaches the end range, it decreases at a much smaller interval. This interpolation option isn't allowed in tag scoring functions.|  
+|`linear`|For items that are within the max and min range, boosting is applied in a constantly decreasing amount. Linear is the default interpolation for a scoring profile.|  
+|`constant`|For items that are within the start and ending range, a constant boost is applied to the rank results.|  
+|`quadratic`|In comparison to a linear interpolation that has a constantly decreasing boost, Quadratic initially decreases at smaller pace and then as it approaches the end range, it decreases at a much higher interval. This interpolation option isn't allowed in tag scoring functions.|  
+|`logarithmic`|In comparison to a linear interpolation that has a constantly decreasing boost, logarithmic initially decreases at higher pace and then as it approaches the end range, it decreases at a much smaller interval. This interpolation option isn't allowed in tag scoring functions.|  
 
  ![Constant, linear, quadratic, log10 lines on graph](media/scoring-profiles/azuresearch_scorefunctioninterpolationgrapht.png "AzureSearch_ScoreFunctionInterpolationGrapht")  
 
-<a name="bkmk_boostdur"></a> 
-
-## Set boostingDuration
+## Set boostingDuration for freshness function
 
 `boostingDuration` is an attribute of the `freshness` function. You use it to set an expiration period after which boosting will stop for a particular document. For example, to boost a product line or brand for a 10-day promotional period, you would specify the 10-day period as "P10D" for those documents.  
 
@@ -263,11 +233,13 @@ The following table provides several examples.
 |15 minutes|"PT15M"|  
 |30 days, 5 hours, 10 minutes, and 6.334 seconds|"P30DT5H10M6.334S"|  
 
-For more examples, see [XML Schema: Datatypes (W3.org web site)](https://www.w3.org/TR/xmlschema11-2/#dayTimeDuration).  
+For more examples, see [XML Schema: Datatypes (W3.org web site)](https://www.w3.org/TR/xmlschema11-2/#dayTimeDuration).
+
+## Extended example for vector and hybrid search
 
-<a name="bkmk_ex"></a>
+See this [blog post](https://farzzy.hashnode.dev/enhance-azure-ai-search-document-boosting) and [notebook](https://github.com/farzad528/azure-ai-search-python-playground/blob/main/azure-ai-search-document-boosting.ipynb) for a demonstration of using scoring profiles and document boosting in vector and generative AI scenarios.
 
-## Extended example
+## Extended example for keyword search
 
 The following example shows the schema of an index with two scoring profiles (`boostGenre`, `newAndHighlyRated`). Any query against this index that includes either profile as a query parameter will use the profile to score the result set. 
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "スコアリングプロファイルの追加と大幅な内容変更"
}
```

### Explanation
この変更は、Azure AI Searchのスコアリングプロファイルに関する文書の内容を大幅に更新し、情報を整理、拡充したものです。

具体的な変更点は以下の通りです：
- 文書内の内容が大幅に見直され、スコアリングプロファイルの定義、使用方法、機能、及びそれに付随する注意点がより詳しく説明されています。
- スコアリングプロファイルのパラメータのセクションが追加され、重み付けフィールドや関数に関する具体的な例（距離、鮮度など）が説明されています。
- スコアリングプロファイルがどのようにクエリロジックに影響を与えるか、具体的な使用例や手順が整理され、より実用的な情報が提供されています。
- 以前のバージョンからの変更ポイントが多数あり、特に「semantic ranking」から「semantic ranker」への表現の変更に似て、用語の一貫性向上が図られています。
- スコアリングプロファイルの使用に関する注意点やベストプラクティスも詳しく言及され、特にフィルタ可能なフィールドやスコア計算の細かいアルゴリズムが説明されています。

全体として、この変更はユーザーがAzure AI Searchにおけるスコアリングプロファイルをより効果的に使用できるように設計されています。文書の明瞭さや具体性が向上しており、技術的な理解を深めるための重要なリソースとなっています。

## articles/search/knowledge-store-create-portal.md{#item-9b92e5}

<details>
<summary>Diff</summary>
````diff
@@ -61,7 +61,7 @@ Because the data is multiple rows in one CSV file, set the *parsing mode* to get
 
    A connection string can be full access, having the following format: `DefaultEndpointsProtocol=https;AccountName=<YOUR-ACCOUNT-NAME>;AccountKey=<YOUR-ACCOUNT-KEY>;EndpointSuffix=core.windows.net`
 
-   Or, a connection string can reference a managed identity, assuming it's [configured and assigned a role](search-howto-managed-identities-data-sources.md) in Azure Storage: `ResourceId=/subscriptions/{YOUR-SUBSCRIPTION-ID}/resourceGroups/{YOUR-RESOURCE-GROUP-NAME}/providers/Microsoft.Storage/storageAccounts/{YOUR-ACCOUNT-NAME};`
+   Or, a connection string can reference a managed identity, assuming it's [configured and assigned a role](search-howto-managed-identities-data-sources.md) in Azure Storage: `ResourceId=/subscriptions/<YOUR-SUBSCRIPTION-ID>/resourceGroups/<YOUR-RESOURCE-GROUP-NAME>/providers/Microsoft.Storage/storageAccounts/<YOUR-ACCOUNT-NAME>;`
 
 1. In **Containers**, enter the name of the blob container holding the data ("hotel-reviews").
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ストア作成ドキュメントの接続文字列の表記修正"
}
```

### Explanation
この変更は、「知識ストアの作成に関するポータル」ドキュメント内の接続文字列に関する表記を修正したものです。

具体的な変更点は以下の通りです：
- 接続文字列の例で `<YOUR-ACCOUNT-NAME>` などのプレースホルダー部分が、具体的なフィールドの構文になりました。この修正により、ユーザーが必要な情報を挿入しやすくなり、説明が明瞭化されています。
- 具体的には、元のテキストの「`<YOUR-ACCOUNT-NAME>`」が「`<YOUR-ACCOUNT-NAME>`」に変更され、プレースホルダーがより明確に示されるようになりました。

この更新は、ユーザーが接続文字列をより正確に設定できるようにするもので、ドキュメントの理解性を向上させるための配慮が反映されています。全体として、文書の質とユーザーの利便性を高める重要な変更です。

## articles/search/media/scoring-profiles/scoring-over-ranked-results.png{#item-bee24f}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "スコアリングプロファイルのビジュアル追加"
}
```

### Explanation
この変更は、Azure AI Searchにおけるスコアリングプロファイルに関するビジュアルコンテンツを新たに追加したものです。

具体的には、以下の点が挙げられます：
- 新たに追加された画像「scoring-over-ranked-results.png」は、スコアリングプロファイルがどのように適用されるかを視覚的に示すものです。
- このビジュアルは、検索結果がどのようにスコアリングプロファイルによって影響を受けるかを解説する際に役立ちます。
- 特に、スコアリングの効果を視覚的に理解するための重要なリソースとなり、ユーザーにとって有用な情報を提供するものです。

この画像の追加は、ドキュメント全体の理解を深め、ユーザーがスコアリングプロファイルの概念をより簡単に認識できるようにするための重要な補完です。

## articles/search/query-lucene-syntax.md{#item-736436}

<details>
<summary>Diff</summary>
````diff
@@ -130,7 +130,7 @@ Proximity searches are used to find terms that are near each other in a document
 
 Term boosting refers to ranking a document higher if it contains the boosted term, relative to documents that don't contain the term. This differs from scoring profiles in that scoring profiles boost certain fields, rather than specific terms.  
 
-The following example helps illustrate the differences. Suppose that there's a scoring profile that boosts matches in a certain field, say *genre* in the  [musicstoreindex example](index-add-scoring-profiles.md#bkmk_ex). Term boosting could be used to further boost certain search terms higher than others. For example, `rock^2 electronic` boosts documents that contain the search terms in the genre field higher than other searchable fields in the index. Further, documents that contain the search term *rock* are ranked higher than the other search term *electronic* as a result of the term boost value (2).  
+The following example helps illustrate the differences. Suppose that there's a scoring profile that boosts matches in a certain field, say *genre* in the  [musicstoreindex example](index-add-scoring-profiles.md#extended-example-for-keyword-search). Term boosting could be used to further boost certain search terms higher than others. For example, `rock^2 electronic` boosts documents that contain the search terms in the genre field higher than other searchable fields in the index. Further, documents that contain the search term *rock* are ranked higher than the other search term *electronic* as a result of the term boost value (2).  
 
  To boost a term, use the caret, `^`, symbol with a boost factor (a number) at the end of the term you're searching. You can also boost phrases. The higher the boost factor, the more relevant the term is relative to other search terms. By default, the boost factor is 1. Although the boost factor must be positive, it can be less than 1 (for example, 0.20).  
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Lucene構文に関する例の参照更新"
}
```

### Explanation
この変更は、「Lucene構文」に関するドキュメント内の特定の例の参照を更新したものです。

具体的な変更点は以下の通りです：
- 例文での参照先が変更され、元の「musicstoreindex example」から「extended-example-for-keyword-search」に更新されました。これにより、ユーザーはより詳細で拡張された例にアクセスできるようになりました。
- ドキュメントの内容自体は変更されていませんが、例の参照更新により、実際の使用方法やコンテキストがより明確になり、読者が関連する情報を見つけやすくなります。

この更新は、情報の正確性と関連性を高め、ユーザーが適切な文脈で知識を得る手助けをするためのものです。結果として、Luceneの特定の機能や構文に関する理解が深まる期待があります。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -116,7 +116,7 @@ There's no query type in Azure AI Search - not even semantic or vector search -
 |---------------|---------|------------|
 | [Simple or full Lucene syntax](search-query-create.md) | Query execution over text and nonvector numeric content | Full text search is best for exact matches, rather than similar matches. Full text search queries are ranked using the [BM25 algorithm](index-similarity-and-scoring.md) and support relevance tuning through scoring profiles. It also supports filters and facets. |
 | [Filters](search-filters.md) and [facets](search-faceted-navigation.md) | Applies to text or numeric (nonvector) fields only. Reduces the search surface area based on inclusion or exclusion criteria. | Adds precision to your queries. |
-| [Semantic ranking](semantic-how-to-query-request.md) | Re-ranks a BM25 result set using semantic models. Produces short-form captions and answers that are useful as LLM inputs. | Easier than scoring profiles, and depending on your content, a more reliable technique for relevance tuning. |
+| [Semantic ranker](semantic-how-to-query-request.md) | Re-ranks a BM25 result set using semantic models. Produces short-form captions and answers that are useful as LLM inputs. | Easier than scoring profiles, and depending on your content, a more reliable technique for relevance tuning. |
   [Vector search](vector-search-how-to-query.md) | Query execution over vector fields for similarity search, where the query string is one or more vectors. | Vectors can represent all types of content, in any language. |
 | [Hybrid search](hybrid-search-how-to-query.md) | Combines any or all of the above query techniques. Vector and nonvector queries execute in parallel and are returned in a unified result set. | The most significant gains in precision and recall are through hybrid queries. |
 
@@ -145,7 +145,7 @@ Here are some tips for maximizing relevance and recall:
 
   + [Scoring profiles](index-add-scoring-profiles.md) that boost the search score if matches are found in a specific search field or on other criteria.
 
-  + [Semantic ranking](semantic-ranking.md) that re-ranks an initial results set, using semantic models from Bing to reorder results for a better semantic fit to the original query.
+  + [Semantic ranker](semantic-ranking.md) that re-ranks an initial results set, using semantic models from Bing to reorder results for a better semantic fit to the original query.
 
   + Query parameters for fine-tuning. You can [bump up the importance of vector queries](vector-search-how-to-query.md#vector-weighting) or [adjust the amount of BM25-ranked results](vector-search-how-to-query.md#maxtextsizerecall-for-hybrid-search-preview) in a hybrid query. You can also [set minimum thresholds to exclude low scoring results](vector-search-how-to-query.md#set-thresholds-to-exclude-low-scoring-results-preview) from a vector query.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランキングの名称変更"
}
```

### Explanation
この変更は、「リトリーバル拡張生成の概要」に関するドキュメント内で、セマンティックランキングの名称を「セマンティックランカー」に変更したものです。

具体的な変更点は以下の通りです：
- ドキュメント内の「Semantic ranking」を「Semantic ranker」に変更しました。この名称変更は、技術的な用語の正確さを向上させ、関連する概念を明確にすることを目的としています。
- この変更は、内容自体には大きな影響を与えず、既存の情報を維持しつつ、機能の理解を助けるためのものです。名称の変更により、使用者が関連するリソースをより見つけやすくなります。

このマイナーな更新は、ドキュメントの一貫性を高め、ユーザーがAzure AI Searchの機能をより良く理解するための手助けをします。

## articles/search/samples-dotnet.md{#item-12f3fa}

<details>
<summary>Diff</summary>
````diff
@@ -39,7 +39,7 @@ Code samples from the Azure SDK development team demonstrate API usage. You can
 | [Indexing documents (push model)](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample05_IndexingDocuments.md) | "Push" model indexing, where you send a JSON payload to an index on a service.   |
 | [Encryption key sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample06_EncryptedIndex.md) | Demonstrates using a customer-managed encryption key to add an extra layer of protection over sensitive content.  |
 | [Vector search sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample07_VectorSearch.md) | Shows you how to index a vector field and perform vector search using the Azure SDK for .NET. |
-| [Semantic ranking sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample08_SemanticSearch.md) | Shows you how to configure semantic ranking in an index and invoke semantic queries using the Azure SDK for .NET. |
+| [Semantic ranking sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample08_SemanticSearch.md) | Shows you how to configure semantic ranker in an index and invoke semantic queries using the Azure SDK for .NET. |
 
 ## Doc samples
 
@@ -52,7 +52,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. A
 |-------------|------------------|---------|
 | [create-mvc-app](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/create-mvc-app) |  [Tutorial: Add search to an ASP.NET Core (MVC) app](tutorial-csharp-create-mvc-app.md) | While most samples are console applications, this MVC sample uses a web page to front the sample Hotels index, demonstrating basic search, pagination, and other server-side behaviors.|
 | [quickstart](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/v11) | [Quickstart: Full text search using the Azure SDKs](search-get-started-text.md) | Covers the basic workflow for creating, loading, and querying a search index in C# using sample data. |
-| [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-search/) | [Quickstart: Semantic ranking using the Azure SDKs](search-get-started-semantic.md) | Shows the index schema and query request for invoking semantic ranking. |
+| [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-search/) | [Quickstart: Semantic ranking using the Azure SDKs](search-get-started-semantic.md) | Shows the index schema and query request for invoking semantic ranker. |
 | [search-website](https://github.com/Azure-Samples/azure-search-static-web-app) | [Tutorial: Add search to web apps](tutorial-csharp-overview.md) | Demonstrates an end-to-end search app that includes bulk upload using the push APIs and a rich client for hosting the app and handling search requests.|
 | [tutorial-ai-enrichment](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/tutorial-ai-enrichment)  | [Tutorial: AI-generated searchable content from Azure blobs](cognitive-search-tutorial-blob-dotnet.md) | Shows how to configure an indexer and skillset. |
 | [multiple-data-sources](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources)  | [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md). | Merges content from two data sources into one search index.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランキングの表現変更"
}
```

### Explanation
この変更は、「.NETサンプル」に関するドキュメント内で「セマンティックランキング」に関する表現を少し変更したものです。具体的には、「semantic ranking」という用語を「semantic ranker」という用語に変更しています。

具体的な変更点は以下の通りです：
- サンプルリスト内で、セマンティックランキングの設定とクエリの実行に関する部分を、「semantic ranking sample」から「semantic ranker」に変更しました。この表現の変更により、セマンティックランキングの機能やコンセプトがより正確に反映されます。
- 他の項目に対しても同様の表現変更が適用されています。

この修正は内容自体に大きな影響を及ぼさないものの、ユーザーにとっての理解を深めるためのものであり、関連する用語の一貫性を高めることを目的としています。このような微調整により、Azure SDK for .NETの使い方が一層明確になることが期待されます。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -39,7 +39,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. M
 | [Tutorial-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Tutorial-RAG) | Source code for the Python portion of [How to build a RAG solution using Azure AI Search](tutorial-rag-build-solution.md).|
 | [Quickstart](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart) | Source code for the Python portion of [Quickstart: Full text search using the Azure SDKs](search-get-started-text.md). This article covers the basic workflow for creating, loading, and querying a search index using sample data. |
 | [Quickstart-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-RAG) | Source code for the Python portion of [Quickstart: Generative search (RAG) with grounding data from Azure AI Search](search-get-started-rag.md). |
-| [Quickstart-Semantic-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) | Source code for the Python portion of [Quickstart: Semantic ranking using the Azure SDKs](search-get-started-semantic.md). It shows the index schema and query request for invoking semantic ranking. |
+| [Quickstart-Semantic-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) | Source code for the Python portion of [Quickstart: Semantic ranking using the Azure SDKs](search-get-started-semantic.md). It shows the index schema and query request for invoking semantic ranker. |
 | [bulk-insert](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/bulk-insert) | Source code for the Python example of how to [use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
 | [azure-function-search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/azure-function-search) | Source code for the Python example of an Azure function that sends queries to a search service. You can substitute this Python version of the `api` code used in the [Add search to web sites](tutorial-csharp-overview.md) C# sample. |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランキングの表現変更"
}
```

### Explanation
この変更は、「Pythonサンプル」に関するドキュメント内で、セマンティックランキングに関する用語を更新したものです。具体的には、「semantic ranking」という用語を「semantic ranker」に変更しています。

具体的な変更点は以下の通りです：
- サンプルリスト内で、セマンティックランキングに関するエントリーが「Quickstart-Semantic-Search」として変更され、説明文中の「semantic ranking」の部分が「semantic ranker」に更新されました。これにより、Azure SDKを使用してセマンティック検索を構成する方法がより明確に表現されています。

この修正により、内容の明瞭さが改善され、ユーザーが関連するリソースをより理解しやすくなることが期待されます。特に、セマンティックランキングに関連する技術用語の一貫性を高めることで、これを利用する開発者のための情報提供が充実しています。

## articles/search/search-api-migration.md{#item-07297b}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ We recommend upgrading API versions in succession, working through each version
 
 Azure AI Search breaks backward compatibility as a last resort. Upgrade is necessary when:
 
-+ Your code references a retired or unsupported API version and is subject to one or more breaking changes. You must address breaking changes if your code targets [`2023-07-10-preview`](#code-upgrade-for-vector-indexes-and-queries) for vectors, [`2020-06-01-preview`](#breaking-change-for-semantic-ranking) for semantic ranking, and [`2019-05-06`](#upgrade-to-2019-05-06) for obsolete skills and workarounds. 
++ Your code references a retired or unsupported API version and is subject to one or more breaking changes. You must address breaking changes if your code targets [`2023-07-10-preview`](#code-upgrade-for-vector-indexes-and-queries) for vectors, [`2020-06-01-preview`](#breaking-change-for-semantic-ranker) for semantic ranker, and [`2019-05-06`](#upgrade-to-2019-05-06) for obsolete skills and workarounds. 
 
 + Your code fails when unrecognized properties are returned in an API response. As a best practice, your application should ignore properties that it doesn't understand.
 
@@ -63,13 +63,13 @@ Effective March 29, 2024 and applicable to all [supported REST APIs](/rest/api/s
 
 + If you need to retrieve connection strings of another Azure resource such as Azure Storage or Azure Cosmos DB, use the APIs of that resource and published guidance to obtain the information. 
 
-## Breaking change for semantic ranking
+## Breaking change for semantic ranker
 
-[Semantic ranking](semantic-search-overview.md) is generally available in `2023-11-01`. Here are the breaking changes for semantic ranking from earlier releases:
+[Semantic ranker](semantic-search-overview.md) is generally available in `2023-11-01`. Here are the breaking changes for semantic ranker from earlier releases:
 
 + In all versions after `2020-06-01-preview`: `semanticConfiguration` replaces `searchFields` as the mechanism for specifying which fields to use for L2 ranking.
 
-+ For all API versions, updates on July 14, 2023 to the Microsoft-hosted semantic models made semantic ranking language-agnostic, effectively decommissioning the `queryLanguage` property. There's no "breaking change" in code, but the property is ignored.
++ For all API versions, updates on July 14, 2023 to the Microsoft-hosted semantic models made semantic ranker language-agnostic, effectively decommissioning the `queryLanguage` property. There's no "breaking change" in code, but the property is ignored.
 
 See [Migrate from preview version](semantic-how-to-configure.md#migrate-from-preview-versions) to transition your code to use `semanticConfiguration`.
 
@@ -103,7 +103,7 @@ If you're upgrading from `2023-10-01-preview`, there are no breaking changes. Ho
 
 ## Upgrade to 2023-11-01
 
-[`2023-11-01`](/rest/api/searchservice/search-service-api-versions#2023-11-01) is a general release. The former preview features are now generally available: semantic ranking, vector index and query support.
+[`2023-11-01`](/rest/api/searchservice/search-service-api-versions#2023-11-01) is a general release. The former preview features are now generally available: semantic ranker, vector index and query support.
 
 There are no breaking changes from `2023-10-01-preview`, but there are multiple breaking changes from `2023-07-01-preview` to `2023-11-01`. For more information, see [Upgrade from 2023-07-01-preview](#upgrade-from-2023-07-01-preview).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーの表現変更"
}
```

### Explanation
この変更は、「検索API移行」に関するドキュメントの内容を一部更新したもので、主に「セマンティックランキング」に関連する表現を「セマンティックランカー」に修正しています。この変更により、用語の一貫性が強化され、最新のAPI仕様に沿った情報が提供されます。

具体的な変更点は以下の通りです：
- セマンティックランキングに関する部分が「セマンティックランカー」に改訂されています。この修正により、APIの機能とその使用方法がより明確になります。
- APIのバージョンに関する記述も更新され、特定のバージョンでのブレイキングチェンジに関する情報が明確化されています。

全体として、この変更は、開発者がAPIのアップグレード時に注意すべき点をより明確にすることを目的としており、ユーザーが変化を理解しやすくするための重要な更新です。特に、セマンティックランカーに関連する情報の整理がなされ、新しい用語に対応した内容が反映されています。

## articles/search/search-create-service-portal.md{#item-f90159}

<details>
<summary>Diff</summary>
````diff
@@ -30,15 +30,15 @@ A few service properties are fixed for the lifetime of the service. Before creat
 
 + [Service name](#name-the-service) becomes part of the URL endpoint. The name must be unique and it must conform to naming rules.
 
-+ [Region](search-region-support.md) determines data residency and the availability of certain features. Semantic ranking and Azure AI integration come with region requirements. Make sure your region of choice supports the features you need.
++ [Region](search-region-support.md) determines data residency and the availability of certain features. Semantic ranker and Azure AI integration come with region requirements. Make sure your region of choice supports the features you need.
 
 + [Service tier](search-sku-tier.md) determines infrastructure, service limits, and billing. Some features aren't available on lower or specialized tiers.
 
 ## Subscribe (free or paid)
 
 Paid (or billable) search occurs when you choose a billable tier (Basic or higher) when creating the resource on a billable Azure subscription.
 
-To try Azure AI Search for free, [open a trial subscription](https://azure.microsoft.com/pricing/free-trial/?WT.mc_id=A261C142F) and then create your search service by choosing the **Free** tier. You can have one free search service per Azure subscription. Free search services are intended for short-term evaluation of the product for nonproduction applications. Generally, you can complete all of the quickstarts and most tutorials, except for those featuring semantic ranking (it requires a billable service).
+To try Azure AI Search for free, [open a trial subscription](https://azure.microsoft.com/pricing/free-trial/?WT.mc_id=A261C142F) and then create your search service by choosing the **Free** tier. You can have one free search service per Azure subscription. Free search services are intended for short-term evaluation of the product for nonproduction applications. Generally, you can complete all of the quickstarts and most tutorials, except for those featuring semantic ranker (it requires a billable service).
 
 Alternatively, you can use free credits to try out paid Azure services. With this approach, you can create your search service at **Basic** or higher to get more capacity. Your credit card is never charged unless you explicitly change your settings and ask to be charged. Another approach is to [activate Azure credits in a Visual Studio subscription](https://azure.microsoft.com/pricing/member-offers/msdn-benefits-details/?WT.mc_id=A261C142F). A Visual Studio subscription gives you credits every month you can use for paid Azure services. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーの表現変更"
}
```

### Explanation
この変更は、「サービスポータルでの検索サービスの作成」に関するドキュメントの内容を一部更新したもので、特に「セマンティックランキング」に関する表現を「セマンティックランカー」に修正しています。これにより、用語の一貫性が強化され、最新の情報に基づいた説明が提供されています。

具体的な変更点は以下の通りです：
- "Semantic ranking"の表現が"Semantic ranker"に置き換えられ、最新のAPIに対応した内容に更新されました。
- サービスの各プロパティについての説明において、URLエンドポイントやリージョン、サービスティアに関する情報が明確にされています。
- 無料のAzure AI Searchを試す方法についての記述も、セマンティックランカーに関連する制限が強調されています。

このような変更により、ユーザーは検索サービスの作成プロセスに関する理解をより深めることができ、最新のサービス機能に関する正確な情報を得ることができます。全体として、開発者やユーザーが必要とする情報の明瞭性を高めることを目的とした更新です。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -77,9 +77,9 @@ For more secure connections:
 
 If you're starting with the free service, you're limited to 3 indexes, data sources, skillsets, and indexers. Basic limits you to 15. Make sure you have room for extra items before you begin. This quickstart creates one of each object.
 
-### Check for semantic ranking
+### Check for semantic ranker
 
-The wizard supports semantic ranking, but only on the Basic tier and higher, and only if semantic ranking is already [enabled on your search service](semantic-how-to-enable-disable.md). If you're using a billable tier, check whether semantic ranking is enabled.
+The wizard supports semantic ranking, but only on the Basic tier and higher, and only if semantic ranker is already [enabled on your search service](semantic-how-to-enable-disable.md). If you're using a billable tier, check whether semantic ranker is enabled.
 
 ## Prepare sample data
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーの表現変更"
}
```

### Explanation
この更新は、「ポータルからベクトルをインポートする方法」に関するドキュメントの一部を修正したもので、主に「セマンティックランキング」についての表現を「セマンティックランカー」に変更しています。この変更によって、最新の用語に基づいた理解が促進されます。

具体的な変更点は以下の通りです：
- "Check for semantic ranking"という見出しが"Check for semantic ranker"に改訂され、用語の一貫性が強化されています。
- ウィザードがサポートする機能に関する説明でも「セマンティックランカー」が使用されるようになり、特定のサービスティアに基づく制限についても明確に記されています。

このような変更により、ユーザーはセマンティックランカーに関連する正確で一貫した情報を得ることができ、サービスの機能に関する理解を深めやすくなります。また、用語の統一が図られることで、文書全体の明瞭さが向上します。全体として、これはユーザーエクスペリエンスの向上を目的とした重要な更新です。

## articles/search/search-get-started-rag.md{#item-05ff0e}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ This quickstart shows you how to send queries to a Large Language Model (LLM) fo
 
 - An Azure subscription. [Create one for free](https://azure.microsoft.com/free/).
 
-- [Azure AI Search](search-create-service-portal.md), Basic tier or higher so that you can [enable semantic ranking](semantic-how-to-enable-disable.md). Region must be the same one used for Azure OpenAI.
+- [Azure AI Search](search-create-service-portal.md), Basic tier or higher so that you can [enable semantic ranker](semantic-how-to-enable-disable.md). Region must be the same one used for Azure OpenAI.
 
 - [Azure OpenAI](https://aka.ms/oai/access) resource with a deployment of `gpt-35-turbo`, `gpt-4`, or equivalent model, in the same region as Azure AI Search.
 
@@ -124,7 +124,7 @@ We recommend the hotels-sample-index, which can be created in minutes and runs o
 
 1. Run the following query in [Search Explorer](search-explorer.md) to test your index: `hotels near the ocean with beach access and good views`.
 
-   Output should look similar to the following example. Results that are returned directly from the search engine consist of fields and their verbatim values, along with metadata like a search score and a semantic ranking score and caption if you use semantic ranking.
+   Output should look similar to the following example. Results that are returned directly from the search engine consist of fields and their verbatim values, along with metadata like a search score and a semantic ranking score and caption if you use semantic ranker.
 
    ```
       "@search.score": 5.600783,
@@ -183,7 +183,7 @@ This section uses Visual Studio Code and Python to call the chat completion APIs
     AZURE_DEPLOYMENT_MODEL: str = "gpt-35-turbo"
    ```
 
-1. Run the following code to set query parameters. The query is a keyword search using semantic ranking. In a keyword search, the search engine returns up to 50 matches, but only the top 5 are provided to the model. If you can't [enable semantic ranking](semantic-how-to-enable-disable.md) on your search service, set the value to false.
+1. Run the following code to set query parameters. The query is a keyword search using semantic ranking. In a keyword search, the search engine returns up to 50 matches, but only the top 5 are provided to the model. If you can't [enable semantic rankersemantic-how-to-enable-disable.md) on your search service, set the value to false.
 
    ```python
    # Set query parameters for grounding the conversation on your search index
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーの用語更新"
}
```

### Explanation
この変更は、「RAG（リトリーバー・アグリゲーター・ジェネレーター）を使用したクイックスタート」に関するドキュメントの内容を更新し、特に「セマンティックランキング」に関する用語を「セマンティックランカー」に統一するための修正です。これにより、用語の一貫性が強化され、最新の情報に基づいた理解が得られやすくなります。

具体的な変更点は以下の通りです：
- Azure AI Searchに関連する文言が、「セマンティックランキング」から「セマンティックランカー」へ変更され、正確な用語が一貫して使用されるようになっています。
- 出力例の説明文中では、検索エンジンから返される結果のメタデータに「セマンティックランキングスコア」と「キャプション」が含まれる場合の記述が更新され、用語を一貫させています。
- クエリパラメータの設定に関する説明でも、セマンティックランカーに関する情報が追加され、情報が明確にされました。

これらの変更により、ユーザーはこのドキュメントで示されている機能を利用する際、より正確な用語を通じて理解を深めることができます。全体として、これはユーザーに対する明瞭さと最新の情報提供を目的とした重要な更新です。

## articles/search/search-get-started-semantic.md{#item-2b3902}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: 'Quickstart: semantic ranking'
 titleSuffix: Azure AI Search
-description: Change an existing index to use semantic ranking.
+description: Change an existing index to use semantic ranker.
 author: HeidiSteen
 manager: nitinme
 ms.author: heidist
@@ -16,9 +16,9 @@ ms.date: 03/11/2024
 
 # Quickstart: Semantic ranking with .NET or Python
 
-In Azure AI Search, [semantic ranking](semantic-search-overview.md) is query-side functionality that uses machine reading comprehension from Microsoft to rescore search results, promoting the most semantically relevant matches to the top of the list. Depending on the content and the query, semantic ranking can [significantly improve search relevance](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-outperforming-vector-search-with-hybrid/ba-p/3929167), with minimal work for the developer.
+In Azure AI Search, [semantic ranker](semantic-search-overview.md) is query-side functionality that uses machine reading comprehension from Microsoft to rescore search results, promoting the most semantically relevant matches to the top of the list. Depending on the content and the query, semantic ranking can [significantly improve search relevance](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-outperforming-vector-search-with-hybrid/ba-p/3929167), with minimal work for the developer.
 
-This quickstart walks you through the index and query modifications that invoke semantic ranking.
+This quickstart walks you through the index and query modifications that invoke semantic ranker.
 
 > [!NOTE]
 > Looking for an Azure AI Search solution with ChatGPT interaction? See [this demo](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md) or [this accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator) for details.
@@ -27,7 +27,7 @@ This quickstart walks you through the index and query modifications that invoke
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/).
 
-+ Azure AI Search, at Basic tier or higher, with [semantic ranking enabled](semantic-how-to-enable-disable.md).
++ Azure AI Search, at Basic tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
 + An API key and search service endpoint. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
 
@@ -39,11 +39,11 @@ This quickstart walks you through the index and query modifications that invoke
 
 ## Add semantic ranking
 
-To use semantic ranking, add a *semantic configuration* to a search index, and add parameters to a query. If you have an existing index, you can make these changes without having to reindex your content because there's no impact on the structure of your searchable content.
+To use semantic ranker, add a *semantic configuration* to a search index, and add parameters to a query. If you have an existing index, you can make these changes without having to reindex your content because there's no impact on the structure of your searchable content.
 
 + A semantic configuration sets a priority order for fields that contribute a title, keywords, and content used in semantic reranking. Field prioritization allows for faster processing.
 
-+ Queries that invoke semantic ranking include parameters for query type and whether captions and answers are returned. You can add these parameters to your existing query logic. There's no conflict with other parameters.
++ Queries that invoke semantic ranker include parameters for query type and whether captions and answers are returned. You can add these parameters to your existing query logic. There's no conflict with other parameters.
 
 ### [**.NET**](#tab/dotnet)
 
@@ -63,7 +63,7 @@ You can find and manage resources in the portal, using the **All resources** or
 
 ## Next steps
 
-In this quickstart, you learned how to invoke semantic ranking on an existing index. We recommend trying semantic ranking on your own indexes as a next step. However, if you want to continue with demos, visit the following link.
+In this quickstart, you learned how to invoke semantic ranker on an existing index. We recommend trying semantic ranker on your own indexes as a next step. However, if you want to continue with demos, visit the following link.
 
 > [!div class="nextstepaction"]
 > [Tutorial: Add search to web apps](tutorial-csharp-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーへの用語変更"
}
```

### Explanation
この変更は、「セマンティックランキング」に関するクイックスタートドキュメントを更新し、用語を「セマンティックランカー」に統一することを目的としています。この変更により、用語の一貫性が維持され、最新の技術用語が適切に反映されることになります。

具体的な変更点は以下の通りです：
- ドキュメントの概要や説明文中における「セマンティックランキング」という用語が、「セマンティックランカー」に改訂されています。これにより、Azure AI Searchの機能についての理解がより明確になります。
- クイックスタートの説明が、インデックスやクエリの変更に関連する内容においても新しい用語を採用しています。
- ユーザーが「セマンティックランカー」を使用するための前提条件に関する記述も変更され、最新の情報が盛り込まれています。

この変更によって、ユーザーはこのドキュメントを通じて、セマンティックランカーに関する正確で一貫した情報を受け取ることができ、実装に向けた理解が深まることが期待されます。全体として、これは用語の更新とドキュメント改善を目的とした重要な修正です。

## articles/search/search-get-started-vector.md{#item-4984d9}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,7 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 
   Most existing services support vector search. For a small subset of services created prior to January 2019, an index that contains vector fields fails on creation. In this situation, a new service must be created.
 
-- Optionally, to run the query example that invokes [semantic reranking](semantic-search-overview.md), your search service must be the Basic tier or higher, with [semantic ranking enabled](semantic-how-to-enable-disable.md).
+- Optionally, to run the query example that invokes [semantic reranking](semantic-search-overview.md), your search service must be the Basic tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
 - Optionally, an [Azure OpenAI](https://aka.ms/oai/access) resource with a deployment of `text-embedding-ada-002`. The source `.rest` file includes an optional step for generating new text embeddings, but we provide pregenerated embeddings so that you can omit this dependency.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーへの用語変更"
}
```

### Explanation
この変更は、「ベクター検索」に関するクイックスタートドキュメントにおいて、用語を「セマンティックランキング」から「セマンティックランカー」に変更することを目的としています。この更新により、用語の一貫性が保たれ、読者が使用する用語を最新のものに合わせることができます。

具体的な変更点は以下の通りです：
- クエリの例がされている部分で、検索サービスを利用する際の要件説明において、従来の「セマンティックランキング」という用語が新しい「セマンティックランカー」に更新されています。
- この変更は、サービスの基本プラン以上で動作することを条件としており、検索機能の情報を正確に伝えることによって、ユーザーが適切に設定を行えるようにサポートしています。

この修正により、ユーザーは最新の技術用語を通じて、Azure AI Searchの機能を理解しやすくなることが期待されます。全体として、これは用語の一貫性を確保するための重要なマイナーアップデートです。

## articles/search/search-indexer-tutorial.md{#item-a3e3ff}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: tutorial
-ms.date: 01/18/2024
+ms.date: 09/23/2024
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
@@ -87,7 +87,7 @@ If you have an existing Azure SQL Database resource, you can add the hotels tabl
 1. Copy the ADO.NET connection string for the database. Under **Settings** > **Connection Strings**, copy the ADO.NET connection string, similar to the example below.
 
     ```sql
-    Server=tcp:{your_dbname}.database.windows.net,1433;Initial Catalog=hotels-db;Persist Security Info=False;User ID={your_username};Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;
+    Server=tcp:<YOUR-DATABASE-NAME>.database.windows.net,1433;Initial Catalog=hotels-db;Persist Security Info=False;User ID=<YOUR-USER-NAME>;Password=<YOUR-PASSWORD>;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;
     ```
 
 You'll need this connection string in the next exercise, setting up your environment.
@@ -114,7 +114,7 @@ API calls require the service URL and an access key. A search service is created
 
 1. For `SearchServiceEndPoint`, if the full URL on the service overview page is "https://my-demo-service.search.windows.net", then the value to provide is the entire URL.
 
-1. For `AzureSqlConnectionString`, the string format is similar to this: `"Server=tcp:{your_dbname}.database.windows.net,1433;Initial Catalog=hotels-db;Persist Security Info=False;User ID={your_username};Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"`
+1. For `AzureSqlConnectionString`, the string format is similar to this: `"Server=tcp:<your-database-name>.database.windows.net,1433;Initial Catalog=hotels-db;Persist Security Info=False;User ID=<your-user-name>;Password=<your-password>;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"`
 
     ```json
     {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "接続文字列のプレースホルダーを更新"
}
```

### Explanation
この変更は、「インデクサーチュートリアル」に関する文書において、接続文字列の例示をより明確にするためにプレースホルダーを更新することを目的としています。この更新により、ユーザーが接続文字列を設定する際に、より理解しやすくなります。

具体的な変更点は以下の通りです：
- ドキュメント内の接続文字列の例が、具体的なプレースホルダーから `<YOUR-DATABASE-NAME>`、`<YOUR-USER-NAME>`、`<YOUR-PASSWORD>` という形式に変更されています。これにより、ユーザーは実際の値を挿入する際の形式をより直感的に理解できるようになります。
- 日付の更新もあり、ドキュメント作成日が「2024年1月18日」から「2024年9月23日」に変更されています。これにより、ユーザーは文書の新しさを認識し、最新の情報をもとに手続きを行うことができます。

この修正は、接続に関する情報をより正確かつ使いやすくするための重要なマイナーアップデートであり、ユーザーの利便性を向上させることを目指しています。

## articles/search/search-manage-rest.md{#item-405ec7}

<details>
<summary>Diff</summary>
````diff
@@ -27,7 +27,7 @@ The Management REST API is available in stable and preview versions. Be sure to
 > * [Create or update a service](#create-or-update-a-service)
 > * [Enable Azure role-based access control for data plane](#enable-rbac)
 > * [Enforce a customer-managed key policy](#enforce-cmk)
-> * [Disable semantic ranking](#disable-semantic-search)
+> * [Disable semantic ranker](#disable-semantic-ranker)
 > * [Disable workloads that push data to external resources](#disable-external-access)
 > * [Create a query key](#create-query-api-keys)
 > * [Regenerate an admin key](#regenerate-admin-api-keys)
@@ -228,14 +228,12 @@ PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegrou
     }
 ```
 
-<a name="disable-semantic-search"></a>
+## Disable semantic ranker
 
-## Disable semantic ranking
-
-Although [semantic ranking isn't enabled](semantic-how-to-enable-disable.md) by default, you could lock down the feature at the service level.
+Although [semantic ranker isn't enabled](semantic-how-to-enable-disable.md) by default, you could lock down the feature at the service level for greater certainty it can't be used.
 
 ```http
-### disable semantic ranking
+### disable semantic ranker
 PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2023-11-01 HTTP/1.1
      Content-type: application/json
      Authorization: Bearer {{token}}
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーの呼称変更"
}
```

### Explanation
この変更は、「管理REST API」に関連する文書において、セマンティック検索の用語を「セマンティックランキング」から「セマンティックランカー」に変更することを目的としています。これにより、用語の一貫性が向上し、ユーザーがこの機能について正しく理解できるようになります。

具体的な変更点は以下の通りです：
- セマンティックランキングを無効にする関連の説明見出しや、関連するリンクにおいて、用語が「セマンティックランカー」に更新されています。この変更は、ドキュメント内での用語の整合性を保つことを意図しています。
- また、セマンティック検索機能がデフォルトで無効になっていることに関する説明文も修正され、より明確な表現に進化しています。この変更により、ユーザーはこの機能に対する理解が深まります。

この修正は、セマンティック検索に関する情報の精度を高め、ユーザーが技術的な内容にアクセスしやすくするための、重要なマイナーアップデートとなります。

## articles/search/search-manage.md{#item-4043d7}

<details>
<summary>Diff</summary>
````diff
@@ -94,7 +94,7 @@ By default, a search service is created in a minimum configuration of one replic
 Some features add to the cost of running the service:
 
 + [How you're charged for Azure AI Search](search-sku-manage-costs.md#how-youre-charged-for-azure-ai-search) explains which features have billing impact.
-+ [(Optional) disable semantic ranking](semantic-how-to-enable-disable.md) at the service level to prevent usage of the feature.
++ [(Optional) disable semantic ranker](semantic-how-to-enable-disable.md) at the service level to prevent usage of the feature.
 
 ### Enable diagnostic logging
 
@@ -107,9 +107,9 @@ Internally, Microsoft collects telemetry data about your service and the platfor
 > [!NOTE]
 > See the ["Data residency"](search-security-overview.md#data-residency) section of the security overview article for more information about data location and privacy.
 
-### Enable semantic ranking
+### Enable semantic ranker
 
-Semantic ranking is free for the first 1,000 requests per month, but you must opt in to get the free quota. 
+Semantic ranker is free for the first 1,000 requests per month, but you must opt in to get the free quota. 
 
 In Azure portal, under **Settings** on the leftmost pane, select **Semantic ranker** and then choose the Free plan. For more information, see [Enable semantic ranker](semantic-how-to-enable-disable.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーへの用語変更"
}
```

### Explanation
この変更は、文書内での用語を「セマンティックランキング」から「セマンティックランカー」に統一することを目的としています。この修正により、用語の整合性が保たれ、ユーザーが該当機能をより正確に理解できるようになります。

具体的な変更点は以下の通りです：
- サービスレベルでのオプション機能に関する記述が更新され、「セマンティックランカー」を無効にする方法が強調されています。この用語の変更は、ドキュメント全体で一貫性を持たせ、読者にとって情報がより明確に伝わるように配慮されています。
- また、セマンティックランカーが月に最初の1,000リクエストに対して無料である旨の説明も修正され、言い回しが簡潔になっています。

この修正は、文書の技術的な正確性を向上させ、ユーザーがAzure AI Searchサービスの管理機能をよりスムーズに理解できるようにするための重要なマイナーアップデートです。

## articles/search/search-pagination-page-layout.md{#item-115902}

<details>
<summary>Diff</summary>
````diff
@@ -165,7 +165,7 @@ For either algorithm, a "@search.score" equal to 1.00 indicates an unscored or u
 
 ### Order by the semantic reranker
 
-If you're using [semantic ranking](semantic-search-overview.md), the "@search.rerankerScore" determines the sort order of your results. 
+If you're using [semantic ranker](semantic-search-overview.md), the "@search.rerankerScore" determines the sort order of your results. 
 
 The "@search.rerankerScore" range is 1 to 4.00, where a higher score indicates a stronger semantic match.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーへの用語変更"
}
```

### Explanation
この変更は、ドキュメント内の用語を「セマンティックランキング」から「セマンティックランカー」に統一することを目的としています。この修正により、用語の一貫性が向上し、ユーザーが機能についてより正確に理解できるようになります。

具体的な変更点は以下の通りです：
- 文書内でセマンティックランキングを使用している箇所が、セマンティックランカーに変更されています。この用語の更新は、読者がAzureの検索機能に関する情報をより明確に把握できるようにするために重要です。
- "@search.rerankerScore"に関連する説明部分はそのまま維持されており、スコアの範囲が1から4.00であること、そして高いスコアが強いセマンティックマッチを意味することが記載されています。

このマイナーアップデートは、文書全体の技術的整合性を高め、ユーザーがセマンティックランカー機能を利用する際の理解を促進することを目指しています。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -27,30 +27,15 @@ This article identifies the cloud regions in which Azure AI Search is available.
 | [Azure OpenAI integration](vector-search-integrated-vectorization.md)  | Refers to skills and vectorizers that make internal calls to deployed embedding and chat models on Azure OpenAI. Check [Azure OpenAI model region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability) for the most current list of regions for each embedding and chat model. Specific Azure OpenAI models are in fewer regions, so be sure to check for joint regional availability before installing.|
 | [Azure AI Studio integration](vector-search-integrated-vectorization-ai-studio.md) | Refers to skills and vectorizers that make internal calls to the models hosted in the model catalog. Check [Azure AI Studio region availability](/azure/ai-studio/reference/region-support) for the most current list of regions. |
 | [Azure AI Vision 4.0 multimodal APIs for image vectorization](search-get-started-portal-image-search.md) | Refers to skills and vectorizers that call the multimodal embedding API. Check the [Azure AI Vision region list](/azure/ai-services/computer-vision/overview-image-analysis#region-availability) for joint regional availability. |
-| [Semantic ranking](semantic-search-overview.md) | Takes a dependency on Microsoft-hosted models in specific regions. Regional support is noted in this article. |
-
-<!-- Each cloud region noted in this article includes a column indicating support for the following features.
-
-- [Semantic ranking](semantic-search-overview.md) depends on models hosted in specific regions.
-- [AI enrichment](cognitive-search-concept-intro.md) refers to skills and vectorizers that make internal calls to Azure AI and Azure OpenAI. Integration requires that Azure AI Search coexist with an [Azure AI multi-service account](/azure/ai-services/multi-service-resource) in the same physical region.
-- [Availability zones](search-reliability.md#availability-zone-support) are an Azure platform capability that divides a region's data centers into distinct physical location groups to provide high-availability, within the same region.
-
-We recommend that you check [Azure AI Studio region availability](/azure/ai-studio/reference/region-support) and [Azure OpenAI model region availability](/azure/reliability/availability-zones-service-support#azure-regions-with-availability-zone-support) for the most current list of regions for those features. 
-
-Also, if you plan to use Azure AI Vision 4.0 multimodal APIs for image vectorization, it's available in a reduced list of regions. [Check the Azure AI Vision region list for multimodal embeddings](/azure/ai-services/computer-vision/overview-image-analysis#region-availability) and be sure to create both your Azure AI multi-service account and Azure AI Search service in one of those supported regions.
-
-> [!NOTE]
-> Higher capacity partitions became available in selected regions starting in April 2024. A second wave of higher capacity partitions released in May 2024. Currently, there are just a few regions that *don't* offer higher capacity patitions, and those are indicated in footnotes.
->
-> If you're using an older search service, consider creating a new search service in a supported region to benefit from more capacity at the same billing rate as before. For more information, see [Service limits](search-limits-quotas-capacity.md#service-limits) and [How to check service creation date](vector-search-index-size.md#how-to-check-service-creation-date). -->
+| [Semantic ranker](semantic-search-overview.md) | Takes a dependency on Microsoft-hosted models in specific regions. Regional support is noted in this article. |
 
 ## Azure Public regions
 
 You can create an Azure AI Search resource in any of the following Azure public regions. Almost all of these regions support [higher capacity tiers](search-limits-quotas-capacity.md#service-limits). Exceptions are noted where they apply.
 
 ### Americas
 
-| Region | AI integration | Semantic ranking | Availability zones |
+| Region | AI integration | Semantic ranker | Availability zones |
 |--|--|--|--|
 | Brazil South​​ ​ | ✅ | ✅ | |
 | Canada Central​​ | ✅ | ✅ | ✅ |
@@ -71,7 +56,7 @@ You can create an Azure AI Search resource in any of the following Azure public
 
 ### Europe
 
-| Region | AI integration | Semantic ranking | Availability zones |
+| Region | AI integration | Semantic ranker | Availability zones |
 |--|--|--|--|
 | North Europe​​ | ✅ | ✅ | ✅ |
 | West Europe​​ <sup>1, 2</sup>| ✅ | ✅ | ✅ |
@@ -93,7 +78,7 @@ You can create an Azure AI Search resource in any of the following Azure public
 
 ### Middle East
 
-| Region | AI integration | Semantic ranking | Availability zones |
+| Region | AI integration | Semantic ranker | Availability zones |
 |--|--|--|--|
 | Israel Central​ <sup>2</sup> |  |  | ✅  |
 | Qatar Central​ <sup>1, 2</sup> |  |  | ✅ |
@@ -105,13 +90,13 @@ You can create an Azure AI Search resource in any of the following Azure public
 
 ### Africa
 
-| Region | AI integration | Semantic ranking | Availability zones |
+| Region | AI integration | Semantic ranker | Availability zones |
 |--|--|--|--|
 | South Africa North​ | ✅ |  | ✅ |
 
 ### Asia Pacific
 
-| Region | AI integration | Semantic ranking | Availability zones |
+| Region | AI integration | Semantic ranker | Availability zones |
 |--|--|--|--|
 | Australia East​ ​ | ✅ | ✅ | ✅ |
 | Australia Southeast​​​ |  | ✅ |  |
@@ -131,7 +116,7 @@ You can create an Azure AI Search resource in any of the following Azure public
 
 ## Azure Government regions
 
-| Region | AI integration | Semantic ranking | Availability zones |
+| Region | AI integration | Semantic ranker | Availability zones |
 |--|--|--|--|
 | Arizona | ✅ | ✅  | |
 | Texas |  |  |  |
@@ -141,7 +126,7 @@ You can create an Azure AI Search resource in any of the following Azure public
 
 ## Azure operated by 21Vianet
 
-| Region | AI integration | Semantic ranking | Availability zones |
+| Region | AI integration | Semantic ranker | Availability zones |
 |--|--|--|--|
 | China East |  |  |  |
 | China East 2 <sup>1</sup> | ✅  | | |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランキングの用語変更"
}
```

### Explanation
この修正では、ドキュメント内の用語を「セマンティックランキング」から「セマンティックランカー」に変更しています。この変更の目的は、用語の一貫性を持たせることで、読み手に対してより正確で明確な情報を提供することです。

主な変更点は以下の通りです：
- セマンティックランキングに関連するすべての表現が、セマンティックランカーに置き換えられています。これにより、ドキュメントが最新の用語に即した内容になり、読者がAzure AI Search機能をより理解しやすくなっています。
- アメリカ、ヨーロッパ、中東、アフリカ、アジア太平洋、政府、そして21Vianetオペレーションに関連する地域でのAI統合やセマンティックランカーのサポート状況が表形式で記載されています。この更新により、各地域の機能のサポート状況が明確に示されています。

このマイナーアップデートは、ドキュメント全体の技術的な整合性を向上させつつ、Azureの各機能とその地域的サポートについての情報をよりわかりやすく提供することを目指しています。

## articles/search/search-security-manage-encryption-keys.md{#item-db3487}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: how-to
-ms.date: 08/05/2024
+ms.date: 09/23/2024
 ms.custom:
   - references_regions
   - ignite-2023
@@ -207,19 +207,19 @@ Conditions that prevent you from adopting this approach include:
     Content-Type: application/json
 
     {
-      "location": "[region]",
+      "location": "<your-region>",
       "sku": {
-        "name": "[sku]"
+        "name": "<your-sku>"
       },
       "properties": {
-        "replicaCount": [replica count],
-        "partitionCount": [partition count],
+        "replicaCount": <your-replica-count>,
+        "partitionCount": <your-partition count>,
         "hostingMode": "default"
       },
       "identity": {
         "type": "UserAssigned",
         "userAssignedIdentities": {
-          "/subscriptions/[subscription ID]/resourcegroups/[resource group name]/providers/Microsoft.ManagedIdentity/userAssignedIdentities/[managed identity name]": {}
+          "/subscriptions/<your-subscription-ID>/resourcegroups/<your-resource-group-name>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<your-managed-identity-name>": {}
         }
       }
     } 
@@ -230,12 +230,12 @@ Conditions that prevent you from adopting this approach include:
     ```json
     {
       "encryptionKey": {
-        "keyVaultUri": "https://[key vault name].vault.azure.net",
-        "keyVaultKeyName": "[key vault key name]",
-        "keyVaultKeyVersion": "[key vault key version]",
+        "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
+        "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
+        "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
         "identity" : { 
             "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
-            "userAssignedIdentity" : "/subscriptions/[subscription ID]/resourceGroups/[resource group name]/providers/Microsoft.ManagedIdentity/userAssignedIdentities/[managed identity name]"
+            "userAssignedIdentity" : "/subscriptions/<your-subscription-ID>/resourceGroups/<your-resource-group-name>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<your-managed-identity-name>"
         }
       }
     }
@@ -312,9 +312,9 @@ Encryption keys are added when you create an object. To add a customer-managed k
     ```json
     {
       "encryptionKey": {
-        "keyVaultUri": "https://demokeyvault.vault.azure.net",
-        "keyVaultKeyName": "myEncryptionKey",
-        "keyVaultKeyVersion": "eaab6a663d59439ebb95ce2fe7d5f660"
+        "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
+        "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
+        "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>"
       }
     }
     ```
@@ -324,12 +324,12 @@ Encryption keys are added when you create an object. To add a customer-managed k
     ```json
     {
       "encryptionKey": {
-        "keyVaultUri": "https://demokeyvault.vault.azure.net",
-        "keyVaultKeyName": "myEncryptionKey",
-        "keyVaultKeyVersion": "eaab6a663d59439ebb95ce2fe7d5f660",
+        "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
+        "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
+        "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
         "accessCredentials": {
-          "applicationId": "00000000-0000-0000-0000-000000000000",
-          "applicationSecret": "myApplicationSecret"
+          "applicationId": "<YOUR-APPLICATION-ID>",
+          "applicationSecret": "<YOUR-APPLICATION-SECRET>"
         }
       }
     }
@@ -363,7 +363,7 @@ In this section, you set the policy that defines a CMK standard for your search
 1. Call the [Services - Update API](/rest/api/searchmanagement/services/update) to enable CMK policy enforcement at the service level.
 
 ```http
-PATCH https://management.azure.com/subscriptions/[subscriptionId]/resourceGroups/[resourceGroupName]/providers/Microsoft.Search/searchServices/[serviceName]?api-version=2023-11-01
+PATCH https://management.azure.com/subscriptions/<your-subscription-Id>/resourceGroups/<your-resource-group-name>/providers/Microsoft.Search/searchServices/<your-search-service-name>?api-version=2023-11-01
 
 {
     "properties": {
@@ -399,12 +399,12 @@ The details of creating a new index via the REST API could be found at [Create I
   {"name": "Location", "type": "Edm.GeographyPoint", "filterable": true, "sortable": true}
  ],
   "encryptionKey": {
-    "keyVaultUri": "https://demokeyvault.vault.azure.net",
-    "keyVaultKeyName": "myEncryptionKey",
-    "keyVaultKeyVersion": "eaab6a663d59439ebb95ce2fe7d5f660",
+    "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
+    "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
+    "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
     "accessCredentials": {
-      "applicationId": "00000000-0000-0000-0000-000000000000",
-      "applicationSecret": "myApplicationSecret"
+      "applicationId": "<YOUR-APPLICATION-ID>",
+      "applicationSecret": "<YOUR-APPLICATION-SECRET>"
     }
   }
 }
@@ -423,12 +423,12 @@ Create an encrypted synonym map using the [Create Synonym Map Azure AI Search RE
   "synonyms" : "United States, United States of America, USA\n
   Washington, Wash. => WA",
   "encryptionKey": {
-    "keyVaultUri": "https://demokeyvault.vault.azure.net",
-    "keyVaultKeyName": "myEncryptionKey",
-    "keyVaultKeyVersion": "eaab6a663d59439ebb95ce2fe7d5f660",
+    "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
+    "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
+    "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
     "accessCredentials": {
-      "applicationId": "00000000-0000-0000-0000-000000000000",
-      "applicationSecret": "myApplicationSecret"
+      "applicationId": "<YOUR-APPLICATION-ID>",
+      "applicationSecret": "<YOUR-APPLICATION-SECRET>"
     }
   }
 }
@@ -449,12 +449,12 @@ Create an encrypted data source using the [Create Data Source (REST API)](/rest/
   },
   "container" : { "name" : "containername" },
   "encryptionKey": {
-    "keyVaultUri": "https://demokeyvault.vault.azure.net",
-    "keyVaultKeyName": "myEncryptionKey",
-    "keyVaultKeyVersion": "eaab6a663d59439ebb95ce2fe7d5f660",
+    "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
+    "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
+    "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
     "accessCredentials": {
-      "applicationId": "00000000-0000-0000-0000-000000000000",
-      "applicationSecret": "myApplicationSecret"
+      "applicationId": "<YOUR-APPLICATION-ID>",
+      "applicationSecret": "<YOUR-APPLICATION-SECRET>"
     }
   }
 }
@@ -473,12 +473,12 @@ Create an encrypted skillset using the [Create Skillset REST API](/rest/api/sear
     "cognitiveServices": { omitted for brevity },
       "knowledgeStore":  { omitted for brevity  },
     "encryptionKey": (optional) { 
-        "keyVaultKeyName": "myEncryptionKey",
-        "keyVaultKeyVersion": "eaab6a663d59439ebb95ce2fe7d5f660",
-        "keyVaultUri": "https://demokeyvault.vault.azure.net",
+        "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
+        "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
+        "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
         "accessCredentials": {
-            "applicationId": "00000000-0000-0000-0000-000000000000",
-            "applicationSecret": "myApplicationSecret"}
+          "applicationId": "<YOUR-APPLICATION-ID>",
+          "applicationSecret": "<YOUR-APPLICATION-SECRET>"
     }
 }
 ```
@@ -500,12 +500,12 @@ Create an encrypted indexer using the [Create Indexer REST API](/rest/api/search
       }
   },
   "encryptionKey": {
-    "keyVaultUri": "https://demokeyvault.vault.azure.net",
-    "keyVaultKeyName": "myEncryptionKey",
-    "keyVaultKeyVersion": "eaab6a663d59439ebb95ce2fe7d5f660",
+    "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
+    "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
+    "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
     "accessCredentials": {
-      "applicationId": "00000000-0000-0000-0000-000000000000",
-      "applicationSecret": "myApplicationSecret"
+      "applicationId": "<YOUR-APPLICATION-ID>",
+      "applicationSecret": "<YOUR-APPLICATION-SECRET>"
     }
   }
 }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "暗号化キーのサンプル設定のプレースホルダー更新"
}
```

### Explanation
この変更は、暗号化キーに関連するサンプル設定のプレースホルダーを更新することを目的としています。これにより、ユーザーが必要な情報を明確に理解し、正確に設定できるようにすることがサポートされています。

主な変更点は以下の通りです：
- 文書内のサンプルコードに含まれる具体的な値がプレースホルダー形式に変更されました。例えば、「`[region]`」や「`[sku]`」などの値が「`<your-region>`」や「`<your-sku>`」に変更されています。これにより、ユーザーが自身の環境に合わせて必要な情報を挿入しやすくなります。
- 複数のコードスニペット内で、暗号化キーの設定に関するプロパティ（`keyVaultUri`、`keyVaultKeyName`、`keyVaultKeyVersion`など）が、具体的な値からプレースホルダーに変更されました。
- 更新日が2024年9月23日に変更され、最新の情報を反映するようにされています。

このマイナーアップデートは、ドキュメントの使用性を向上させ、ユーザーがAzureの暗号化キー管理に関する設定を容易に行えるようにすることを目指しています。

## articles/search/search-semi-structured-data.md{#item-d3388d}

<details>
<summary>Diff</summary>
````diff
@@ -165,7 +165,7 @@ HTTP/1.1 201 Created
 Transfer-Encoding: chunked
 Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
 ETag: "0x8DC43A5FDB8448F"
-Location: https://free-demo-search-svc.search.windows.net:443/datasources('ny-philharmonic-ds')?api-version=2024-07-01
+Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net:443/datasources('ny-philharmonic-ds')?api-version=2024-07-01
 Server: Microsoft-IIS/10.0
 Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
 Preference-Applied: odata.include-annotations="*"
@@ -176,7 +176,7 @@ Date: Wed, 13 Mar 2024 21:38:58 GMT
 Connection: close
 
 {
-  "@odata.context": "https://free-demo-search-svc.search.windows.net/$metadata#datasources/$entity",
+  "@odata.context": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/$metadata#datasources/$entity",
   "@odata.etag": "\"0x8DC43A5FDB8448F\"",
   "name": "ny-philharmonic-ds",
   "description": null,
@@ -308,7 +308,7 @@ Date: Wed, 13 Mar 2024 22:09:59 GMT
 Connection: close
 
 {
-  "@odata.context": "https://free-demo-search-svc.search.windows.net/indexes('ny-philharmonic-index')/$metadata#docs(*)",
+  "@odata.context": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes('ny-philharmonic-index')/$metadata#docs(*)",
   "@odata.count": 1521,
   "@search.nextPageParameters": {
     "search": "*",
@@ -317,7 +317,7 @@ Connection: close
   },
   "value": [
   ],
-  "@odata.nextLink": "https://free-demo-search-svc.search.windows.net/indexes/ny-philharmonic-index/docs/search?api-version=2024-07-01"
+  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/ny-philharmonic-index/docs/search?api-version=2024-07-01"
 }
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービス名のプレースホルダーの変更"
}
```

### Explanation
この変更では、Azureの検索サービスに関連するサンプルコード内の具体的なサービス名をプレースホルダー形式に更新しています。この修正により、ユーザーが自身の環境に適切なサービス名を簡単に挿入できるようになっています。

主な変更点は以下の通りです：
- サンプルコードに含まれる「`Location`」や「`@odata.context`」、「`@odata.nextLink`」などのURLが「`https://free-demo-search-svc.search.windows.net`」から「`https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net`」に変更されました。これにより、ユーザーは自身の検索サービス名を入力することで、具体的な設定を行いやすくなります。
- この変更は複数の箇所で行われており、各リクエストの応答データに対するリファレンスが更新されています。

このマイナーアップデートは、ユーザーがドキュメントを利用する際に、特定のサービス名を挿入することを容易にし、最終的にはドキュメントの使用性を向上させることを目的としています。

## articles/search/semantic-answers.md{#item-c3fee9}

<details>
<summary>Diff</summary>
````diff
@@ -128,7 +128,7 @@ Within @search.answers:
 
 + **"score"** is a confidence score that reflects the strength of the answer. If there are multiple answers in the response, this score is used to determine the order. Top answers and top captions can be derived from different search documents, where the top answer originates from one document, and the top caption from another, but in general the same documents appear in the top positions within each array.
 
-Answers are followed by the **"value"** array, which always includes scores, captions, and any fields that are retrievable by default. If you specified the select parameter, the "value" array is limited to the fields that you specified. See [Configure semantic ranking](semantic-how-to-configure.md) for details.
+Answers are followed by the **"value"** array, which always includes scores, captions, and any fields that are retrievable by default. If you specified the select parameter, the "value" array is limited to the fields that you specified. See [Configure semantic ranker](semantic-how-to-configure.md) for details.
 
 ## Tips for producing high-quality answers
 
@@ -144,4 +144,4 @@ For best results, return semantic answers on a document corpus having the follow
 
 + [Semantic ranking overview](semantic-search-overview.md)
 + [Configure BM25 ranking](index-ranking-similarity.md)
-+ [Configure semantic ranking](semantic-how-to-configure.md)
++ [Configure semantic ranker](semantic-how-to-configure.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックレンカーへの表記変更"
}
```

### Explanation
この変更は、ドキュメント内の「セマンティックランキング」に関する表現を「セマンティックレンカー」に変更することを目的としています。この修正により、用語の一貫性が保たれ、理解が明確になります。

主な変更点は以下の通りです：
- 「**"score"**」に関する説明が追加され、回答の信頼度を示すスコアがどのように特定の回答の順序を決定するかが詳しく述べられています。この情報は、複数の回答が存在する場合の動作をユーザーに明確にします。
- 「**"value"**」配列に関する説明が若干変更されており、「セマンティックランキング」という用語が「セマンティックレンカー」に修正されています。これにより、用語の統一性が向上します。
- 最後に、参照されている章の名称も同様に変更され、タイトルの一致が確保されています。

このマイナーアップデートは、読者にとっての理解を助けるために、専門用語の使用を一貫性のあるものにすることを目指しています。

## articles/search/semantic-how-to-configure.md{#item-7a92a6}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ ms.topic: how-to
 ms.date: 08/05/2024
 ---
 
-# Configure semantic ranking and return captions in search results
+# Configure semantic ranker and return captions in search results
 
 This article explains how to configure a search index for semantic reranking. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランキングの呼称変更"
}
```

### Explanation
この変更では、タイトルに含まれる「セマンティックランキング」という用語が「セマンティックレンカー」に変更されています。この修正により、用語の一貫性が向上し、ユーザーが理解しやすくなっています。

主な変更点は以下の通りです：
- タイトルの文言が「Configure semantic ranking and return captions in search results」から「Configure semantic ranker and return captions in search results」に修正されました。この変更により、文書全体で用語の統一性が確保され、特にセマンティックに関連する機能についての認識が明確になります。
- 変更されたタイトルは、記事がセマンティックなリランキング機能を設定する方法を説明することを示しており、ユーザーが必要な情報を見つけやすくなっています。

このマイナーアップデートは、ドキュメントの品質向上と専門用語の理解向上を目的としています。

## articles/search/semantic-how-to-enable-disable.md{#item-71ac1e}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ Semantic ranker is a premium feature that's billed by usage. By default, semanti
 
 Check the [Products Available by Region](https://azure.microsoft.com/global-infrastructure/services/?products=search) page on the Azure web site to see if your region is listed.
 
-## Enable semantic ranking
+## Enable semantic ranker
 
 Follow these steps to enable [semantic ranker](semantic-search-overview.md) at the service level. Once enabled, it's available to all indexes. You can't turn it on or off for specific indexes.
 
@@ -41,7 +41,7 @@ The free plan is capped at 1,000 queries per month. After the first 1,000 querie
 
 ### [**REST**](#tab/enable-rest)
 
-To enable semantic ranking using the REST API, you can use the [Create or Update Service API](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2023-11-01&tabs=HTTP#searchsemanticsearch&preserve-view=true).
+To enable semantic ranker using the REST API, you can use the [Create or Update Service API](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2023-11-01&tabs=HTTP#searchsemanticsearch&preserve-view=true).
 
 Management REST API calls are authenticated through Microsoft Entra ID. See [Manage your Azure AI Search service with REST APIs](search-manage-rest.md) for instructions on how to authenticate.
 
@@ -63,9 +63,9 @@ PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegrou
 
 ---
 
-## Disable semantic ranking using the REST API
+## Disable semantic ranker using the REST API
 
-To reverse feature enablement, or for full protection against accidental usage and charges, you can disable semantic ranking using the [Create or Update Service API](/rest/api/searchmanagement/services/create-or-update#searchsemanticsearch) on your search service. After the feature is disabled, any requests that include the semantic query type will be rejected.
+To reverse feature enablement, or for full protection against accidental usage and charges, you can disable semantic ranker using the [Create or Update Service API](/rest/api/searchmanagement/services/create-or-update#searchsemanticsearch) on your search service. After the feature is disabled, any requests that include the semantic query type will be rejected.
 
 Management REST API calls are authenticated through Microsoft Entra ID. See [Manage your Azure AI Search service with REST APIs](search-manage-rest.md) for instructions on how to authenticate.
 
@@ -78,8 +78,8 @@ PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegrou
     }
 ```
 
-To re-enable semantic ranking, rerun the above request, setting "semanticSearch" to either "free" (default) or "standard".
+To re-enable semantic ranker, rerun the above request, setting "semanticSearch" to either "free" (default) or "standard".
 
 ## Next steps
 
-[Configure semantic ranking](semantic-how-to-configure.md) so that you can test out semantic ranking on your content.
+[Configure semantic ranker](semantic-how-to-configure.md) so that you can test out semantic ranking on your content.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランキングの呼称変更"
}
```

### Explanation
この変更では、ドキュメント内の「セマンティックランキング」という用語が「セマンティックレンカー」に変更されています。この修正により、用語の一貫性が向上し、ユーザーが理解しやすくなっています。

主な変更点は以下の通りです：
- 「Enable semantic ranking」という見出しが「Enable semantic ranker」に変更され、ランキング機能の名称が統一されました。
- REST APIに関する説明でも、「semantic ranking」を「semantic ranker」に修正し、関連する手順や説明が一貫性を持つように調整されています。
- 説明の内容に関しては、機能を有効化および無効化する方法に変化はありませんが、用語の変更により、全体的な文書の整合性が強化されています。

このマイナーアップデートは、専門用語の使用に関しての一貫性を保ち、読者にとっての理解を高めることを目的としています。

## articles/search/semantic-how-to-query-request.md{#item-85530d}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Add semantic ranking
 titleSuffix: Azure AI Search
-description: Set a semantic query type to attach the deep learning models of semantic ranking.
+description: Set a semantic query type to attach the deep learning models of semantic ranker.
 
 manager: nitinme
 author: HeidiSteen
@@ -17,11 +17,11 @@ ms.date: 07/24/2024
 
 This article explains how to invoke the semantic ranker on queries. You can apply semantic ranking to text queries, hybrid queries, and vector queries if your search documents contain string fields and the [vector query has a text representation](vector-search-how-to-query.md#query-with-integrated-vectorization).
 
-Semantic ranking iterates over an initial result set, applying an L2 ranking methodology that promotes the most semantically relevant results to the top of the stack. You can also get semantic captions, with highlights over the most relevant terms and phrases, and [semantic answers](semantic-answers.md).
+Semantic ranker iterates over an initial result set, applying an L2 ranking methodology that promotes the most semantically relevant results to the top of the stack. You can also get semantic captions, with highlights over the most relevant terms and phrases, and [semantic answers](semantic-answers.md).
 
 ## Prerequisites
 
-+ A search service, basic tier or higher, with [semantic ranking enabled](semantic-how-to-enable-disable.md).
++ A search service, basic tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
 + An existing search index with a [semantic configuration](semantic-how-to-configure.md) and rich text content.
 
@@ -136,7 +136,7 @@ The following example in this section uses the [hotels-sample-index](search-get-
 
 ### [**.NET SDK**](#tab/dotnet-query)
 
-Use QueryType or SemanticQuery to invoke semantic ranking on a semantic query. The [following example](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample08_SemanticSearch.md) is from the Azure SDK team.
+Use QueryType or SemanticQuery to invoke semantic ranker on a semantic query. The [following example](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample08_SemanticSearch.md) is from the Azure SDK team.
 
 ```csharp
 SearchResults<Hotel> response = await searchClient.SearchAsync<Hotel>(
@@ -237,4 +237,4 @@ If you anticipate consistent throughput requirements near, at, or higher than th
 Semantic ranking can be used in hybrid queries that combine keyword search and vector search into a single request and a unified response.
 
 > [!div class="nextstepaction"]
-> [Hybrid query with semantic ranking](hybrid-search-how-to-query.md#semantic-hybrid-search)
\ No newline at end of file
+> [Hybrid query with semantic ranker](hybrid-search-how-to-query.md#semantic-hybrid-search)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランキングの呼称変更"
}
```

### Explanation
この変更では、文書内の「セマンティックランキング」という用語が「セマンティックレンカー」に変更されています。この修正により、用語の一貫性が向上し、ユーザーの理解を助けることを目的としています。

主な変更点は以下の通りです：
- ドキュメントの説明欄が「Set a semantic query type to attach the deep learning models of semantic ranking」から「Set a semantic query type to attach the deep learning models of semantic ranker」に変更され、用語が統一されました。
- 主要な説明部分でも「Semantic ranking」が「Semantic ranker」に修正され、ランキング機能に関する文書全体で用語の一貫性が強化されています。
- 必要条件のセクションにおいても、ランキング機能に関する表現が更新され、より明瞭な表記が採用されています。
- 例として示される.NET SDKに関する記述も同様に修正が行われています。

これらの変更は、ドキュメントの明確性を向上させ、ユーザーが意図された機能を理解しやすくすることを目的としています。

## articles/search/semantic-search-overview.md{#item-b7497b}

<details>
<summary>Diff</summary>
````diff
@@ -15,20 +15,20 @@ ms.date: 06/12/2024
 
 # Semantic ranking in Azure AI Search
 
-In Azure AI Search, *semantic ranking* is a feature that measurably improves search relevance by using Microsoft's language understanding models to rerank search results. This article is a high-level introduction. The section at the end covers [availability and pricing](#availability-and-pricing).
+In Azure AI Search, *semantic ranker* is a feature that measurably improves search relevance by using Microsoft's language understanding models to rerank search results. This article is a high-level introduction. The section at the end covers [availability and pricing](#availability-and-pricing).
 
 Semantic ranker is a premium feature, billed by usage. We recommend this article for background, but if you'd rather get started, follow these steps:
 
 > [!div class="checklist"]
 > * [Check regional availability](search-region-support.md)
 > * [Sign in to Azure portal](https://portal.azure.com) to verify your search service is Basic or higher
-> * [Enable semantic ranking and choose a pricing plan](semantic-how-to-enable-disable.md)
-> * [Set up a semantic configuration in a search index](semantic-how-to-configure.md)
+> * [Enable semantic ranker and choose a pricing plan](semantic-how-to-enable-disable.md)
+> * [Configure semantic ranker in a search index](semantic-how-to-configure.md)
 > * [Set up queries to return semantic captions and highlights](semantic-how-to-query-request.md)
 > * [Optionally, return semantic answers](semantic-answers.md)
 
 > [!NOTE]
-> Semantic ranking doesn't use generative AI or vectors. If you're looking for vector support and similarity search? See [Vector search in Azure AI Search](vector-search-overview.md) for details.
+> Semantic ranker doesn't use generative AI or vectors. If you're looking for vector support and similarity search? See [Vector search in Azure AI Search](vector-search-overview.md) for details.
 
 ## What is semantic ranking?
 
@@ -42,7 +42,7 @@ Here are the capabilities of the semantic reranker.
 
 | Feature | Description |
 |---------|-------------|
-| Semantic ranking | Uses the context or semantic meaning of a query to compute a new relevance score over preranked results. |
+| Semantic ranker | Uses the context or semantic meaning of a query to compute a new relevance score over preranked results. |
 | [Semantic captions and highlights](semantic-how-to-query-request.md) | Extracts verbatim sentences and phrases from a document that best summarize the content, with highlights over key passages for easy scanning. Captions that summarize a result are useful when individual content fields are too dense for the search results page. Highlighted text elevates the most relevant terms and phrases so that users can quickly determine why a match was considered relevant. |
 | [Semantic answers](semantic-answers.md) | An optional and extra substructure returned from a semantic query. It provides a direct answer to a query that looks like a question. It requires that a document has text with the characteristics of an answer. |
 
@@ -62,7 +62,7 @@ There are two steps to semantic ranking: summarization and scoring. Outputs cons
 
 In semantic ranking, the query subsystem passes search results as an input to summarization and ranking models. Because the ranking models have input size constraints and are processing intensive, search results must be sized and structured (summarized) for efficient handling.
 
-1. Semantic ranking starts with a [BM25-ranked result](index-ranking-similarity.md) from a text query or an [RRF-ranked result](hybrid-search-ranking.md) from a hybrid query. Only text fields are used in the reranking exercise, and only the top 50 results progress to semantic ranking, even if results include more than 50. Typically, fields used in semantic ranking are informational and descriptive.
+1. Semantic ranker starts with a [BM25-ranked result](index-ranking-similarity.md) from a text query or an [RRF-ranked result](hybrid-search-ranking.md) from a hybrid query. Only text fields are used in the reranking exercise, and only the top 50 results progress to semantic ranking, even if results include more than 50. Typically, fields used in semantic ranking are informational and descriptive.
 
 1. For each document in the search result, the summarization model accepts up to 2,000 tokens, where a token is approximately 10 characters. Inputs are assembled from the "title", "keyword", and "content" fields listed in the [semantic configuration](semantic-how-to-configure.md). 
 
@@ -111,11 +111,11 @@ Semantic ranker is a newer technology so it's important to set expectations abou
 
 * Find strings to use as captions and answers. Captions and answers are returned in the response and can be rendered on a search results page.
 
-What semantic ranking *can't* do is rerun the query over the entire corpus to find semantically relevant results. Semantic ranking reranks the existing result set, consisting of the top 50 results as scored by the default ranking algorithm. Furthermore, semantic ranking can't create new information or strings. Captions and answers are extracted verbatim from your content so if the results don't include answer-like text, the language models won't produce one.
+What semantic ranker *can't* do is rerun the query over the entire corpus to find semantically relevant results. Semantic ranking reranks the existing result set, consisting of the top 50 results as scored by the default ranking algorithm. Furthermore, semantic ranker can't create new information or strings. Captions and answers are extracted verbatim from your content so if the results don't include answer-like text, the language models won't produce one.
 
-Although semantic ranking isn't beneficial in every scenario, certain content can benefit significantly from its capabilities. The language models in semantic ranking work best on searchable content that is information-rich and structured as prose. A knowledge base, online documentation, or documents that contain descriptive content see the most gains from semantic ranking capabilities.
+Although semantic ranking isn't beneficial in every scenario, certain content can benefit significantly from its capabilities. The language models in semantic ranker work best on searchable content that is information-rich and structured as prose. A knowledge base, online documentation, or documents that contain descriptive content see the most gains from semantic ranker capabilities.
 
-The underlying technology is from Bing and Microsoft Research, and integrated into the Azure AI Search infrastructure as an add-on feature. For more information about the research and AI investments backing semantic ranking, see [How AI from Bing is powering Azure AI Search (Microsoft Research Blog)](https://www.microsoft.com/research/blog/the-science-behind-semantic-search-how-ai-from-bing-is-powering-azure-cognitive-search/).
+The underlying technology is from Bing and Microsoft Research, and integrated into the Azure AI Search infrastructure as an add-on feature. For more information about the research and AI investments backing semantic ranker, see [How AI from Bing is powering Azure AI Search (Microsoft Research Blog)](https://www.microsoft.com/research/blog/the-science-behind-semantic-search-how-ai-from-bing-is-powering-azure-cognitive-search/).
 
 The following video provides an overview of the capabilities.
 
@@ -132,10 +132,10 @@ When you enable semantic ranker, choose a pricing plan for the feature:
 
 The [Azure AI Search pricing page](https://azure.microsoft.com/pricing/details/search/) shows you the billing rate for different currencies and intervals.
 
-Charges for semantic ranking are levied when query requests include `queryType=semantic` and the search string isn't empty (for example, `search=pet friendly hotels in New York`). If your search string is empty (`search=*`), you aren't charged, even if the queryType is set to semantic.
+Charges for semantic ranker are levied when query requests include `queryType=semantic` and the search string isn't empty (for example, `search=pet friendly hotels in New York`). If your search string is empty (`search=*`), you aren't charged, even if the queryType is set to semantic.
 
 ## See also
 
-* [Enable semantic ranking](semantic-how-to-enable-disable.md)
-* [Configure semantic ranking](semantic-how-to-query-request.md)
+* [Enable semantic ranker](semantic-how-to-enable-disable.md)
+* [Configure semantic ranker](semantic-how-to-query-request.md)
 * [Blog: Outperforming vector search with hybrid retrieval and ranking capabilities](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-outperforming-vector-search-with-hybrid/ba-p/3929167)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランキングの用語変更"
}
```

### Explanation
この変更では、文書内の「セマンティックランキング」という表現が「セマンティックレンカー」に修正されています。この修正により、用語が統一され、全体的な文書の明瞭性が向上しました。

具体的な変更内容は次の通りです：
- イントロダクション部分で「semantic ranking」が「semantic ranker」に変更され、その後の説明や手順のセクションでも同様に用語が修正されています。
- 手順のリストでは、「Enable semantic ranking and choose a pricing plan」が「Enable semantic ranker and choose a pricing plan」に修正され、また「Set up a semantic configuration in a search index」が「Configure semantic ranker in a search index」に変更されています。
- 注意点のセクションでも同様に、用語が修正され、「Semantic ranking doesn't use generative AI or vectors」が「Semantic ranker doesn't use generative AI or vectors」に変更されています。
- システムの機能説明に関しても、セカンドセクションの要件が同様に更新され、より一貫した表現が使用されています。

これらの変更は、ドキュメントの整合性を高め、ユーザーにとっての理解を促進することを目的としています。

## articles/search/service-configure-firewall.md{#item-75be3f}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 06/27/2024
+ms.date: 09/24/2024
 ---
 
 # Configure network access and firewall rules for Azure AI Search
@@ -96,9 +96,12 @@ When IP rules are configured, some features of the Azure portal are disabled. Yo
 
 You can restore portal access to the full range of search service operations by adding the portal IP address.
 
-To get the portal's IP address, perform `nslookup` (or `ping`) on `stamp2.ext.search.windows.net`, which is the domain of the traffic manager. For nslookup, the IP address is visible in the "Non-authoritative answer" portion of the response.
+To get the portal's IP address, perform `nslookup` (or `ping`) on:
 
-In the following example, the IP address that you should copy is `52.252.175.48`.
++ `stamp2.ext.search.windows.net`, which is the domain of the traffic manager for the Azure public cloud.
++ `stamp2.ext.search.azure.us` for Azure Government cloud.
+
+For nslookup, the IP address is visible in the "Non-authoritative answer" portion of the response. In the following example, the IP address that you should copy is `52.252.175.48`.
 
 ```bash
 $ nslookup stamp2.ext.search.windows.net
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイアウォール設定のためのIPアドレス情報の追加"
}
```

### Explanation
この変更では、Azure AI Searchのファイアウォールに関するドキュメントに対して、IPアドレスに関する情報が追加されました。新しい情報により、ユーザーが異なるクラウド環境でのアクセスを設定しやすくなることを目指しています。

具体的な変更内容は以下の通りです：
- ドキュメントの日付が「06/27/2024」から「09/24/2024」に更新され、最新の情報を反映しています。
- ポータルのIPアドレスを取得する際の手順において、対象のドメインが具体的に記載されるようになりました。具体的には、Azureパブリッククラウド用のドメイン「stamp2.ext.search.windows.net」に加えて、Azure政府クラウド用として「stamp2.ext.search.azure.us」の記載も追加されました。
- `nslookup` コマンドや `ping` コマンドの使用によるIPアドレスの取得方法がより明確になり、それぞれのクラウド環境におけるドメインの情報がユーザーに提供されています。

これにより、Azureの異なる環境でファイアウォール設定を行う際の指針が強化され、利用者が求める情報に簡単にアクセスできるようになっています。

## articles/search/speller-how-to-add.md{#item-9b4502}

<details>
<summary>Diff</summary>
````diff
@@ -77,7 +77,7 @@ POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/
 
 ## Spell correction with semantic ranking
 
-This query, with typos in every term except one, undergoes spelling corrections to return relevant results. To learn more, see [Configure semantic ranking](semantic-how-to-query-request.md).
+This query, with typos in every term except one, undergoes spelling corrections to return relevant results. To learn more, see [Configure semantic ranker](semantic-how-to-query-request.md).
 
 ```http
 POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2024-05-01-preview    
@@ -105,7 +105,7 @@ Valid values for `queryLanguage` can be found in the following table, copied fro
 | Dutch [NL] | NL, NL-BE, NL-NL (default) |
 
 > [!NOTE]
-> Previously, while semantic ranking was in public preview, the `queryLanguage` parameter was also used for semantic ranking. Semantic ranking is now language-agnostic.
+> Previously, while semantic ranker was in public preview, the `queryLanguage` parameter was also used for semantic ranking. Semantic ranker is now language-agnostic.
 
 ### Language analyzer considerations
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランキングの用語変更"
}
```

### Explanation
この変更では、文書内にある「セマンティックランキング」という用語が「セマンティックレンカー」に統一される形で修正されました。この更新は、用語の一貫性を保ち、読者に対する理解を向上させることを目的としています。

具体的な修正箇所は以下の通りです：
- スペル修正に関するセクションで、「Configure semantic ranking」が「Configure semantic ranker」に変更され、これにより用語の整合性が強化されました。
- 注意書きの部分でも、「semantic ranking」が「semantic ranker」に変更されています。これにより、以前はセマンティックランキングが公開プレビュー中に使用されていた `queryLanguage` パラメータについての記述が、最新の名詞形で更新されています。

このように、用語の変更は文書全体の可読性と整合性を高め、ユーザーが情報をより迅速かつ正確に理解できるようにします。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -407,16 +407,16 @@ items:
     href: hybrid-search-how-to-query.md
   - name: Ranking and relevance
     items:
-    - name: Enable or disable semantic ranking
+    - name: Enable or disable semantic ranker
       href: semantic-how-to-enable-disable.md      
-    - name: Configure semantic ranking
+    - name: Configure semantic ranker
       href: semantic-how-to-configure.md
-    - name: Configure BM25 ranking
-      href: index-ranking-similarity.md
     - name: Add semantic ranking to queries
       href: semantic-how-to-query-request.md
     - name: Add a scoring profile
       href: index-add-scoring-profiles.md
+    - name: Configure BM25 ranking
+      href: index-ranking-similarity.md
   - name: Security
     items:
     - name: Configure network access
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックレンカーの用語変更"
}
```

### Explanation
この変更では、ドキュメントの目次ファイル（toc.yml）内で「セマンティックランキング」という用語が「セマンティックレンカー」に置き換えられました。これにより、用語の一貫性が統一され、読者が内容をより理解しやすくなります。

具体的な変更点は以下の通りです：
- 「Enable or disable semantic ranking」が「Enable or disable semantic ranker」に変更されました。
- 「Configure semantic ranking」が「Configure semantic ranker」に変更され、同様に整合性が保たれました。
- また、「Configure BM25 ranking」とその関連項目の位置が調整され、文書の構成が明確化されています。

これらの修正により、関連するトピックが分かりやすく整理され、ユーザーが各機能の理解を深めやすくなっています。この変更は、情報の明確さと検索機能の価値を向上させることを目指しています。

## articles/search/tutorial-csharp-search-query-integration.md{#item-8ad6b5}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ The function app authenticates through the SDK to the cloud-based Azure AI Searc
 
 ## Azure Function: Search the catalog
 
-The [Search API](https://github.com/Azure-Samples/azure-search-static-web-app/api/Search.cs) takes a search term and searches across the documents in the search index, returning a list of matches. 
+The [Search API](https://github.com/Azure-Samples/azure-search-static-web-app/blob/main/api/Search.cs) takes a search term and searches across the documents in the search index, returning a list of matches. 
 
 The Azure function pulls in the search configuration information, and fulfills the query.
 
@@ -48,9 +48,9 @@ Call the Azure Function in the React client with the following code.
 
 ## Azure Function: Suggestions from the catalog
 
-The [Suggest API](https://github.com/Azure-Samples/azure-search-static-web-app/api/Suggest.cs) takes a search term while a user is typing and suggests search terms such as book titles and authors across the documents in the search index, returning a small list of matches. 
+The [Suggest API](https://github.com/Azure-Samples/azure-search-static-web-app/blob/main/api/Suggest.cs) takes a search term while a user is typing and suggests search terms such as book titles and authors across the documents in the search index, returning a small list of matches. 
 
-The search suggester, `sg`, is defined in the [schema file](https://github.com/Azure-Samples/azure-search-static-web-app/bulk-insert/BookSearchIndex.cs) used during bulk upload.
+The search suggester, `sg`, is defined in the [schema file](https://github.com/Azure-Samples/azure-search-static-web-app/blob/main/bulk-insert/BookSearchIndex.cs) used during bulk upload.
 
 :::code language="csharp" source="~/azure-search-static-web-app/api/Suggest.cs"  :::
 
@@ -62,7 +62,7 @@ The Suggest function API is called in the React app at `\client\src\components\S
 
 ## Azure Function: Get specific document 
 
-The [Document Lookup API](https://github.com/Azure-Samples/azure-search-static-web-app/api/Lookup.cs) takes an ID and returns the document object from the Search Index. 
+The [Document Lookup API](https://github.com/Azure-Samples/azure-search-static-web-app/blob/main/api/Lookup.cs) takes an ID and returns the document object from the Search Index. 
 
 :::code language="csharp" source="~/azure-search-static-web-app/api/Lookup.cs"  :::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Search APIリファレンスのリンク更新"
}
```

### Explanation
この変更では、C#を用いたAzure Searchのチュートリアル文書において、各APIへのリンクが更新され、より正確なURL形式に改訂されました。この修正により、リンク先が正しいファイルを指すようになり、ユーザーにとって使いやすくなっています。

具体的な変更点は以下の通りです：
- Search API、Suggest API、およびDocument Lookup APIに関連するリンクが、GitHubリポジトリの正しいパスに更新されました。特に、`api/Suggest.cs`や`api/Lookup.cs`といったファイルは、`blob/main`ディレクトリを伴う形式で修正されています。
- 文中の説明テキストは変わらず、APIの機能に関する情報はそのまま維持されています。

これにより、読者は最新のコードを確実に参照できるようになり、ドキュメントの信頼性が向上しました。この修正は、よりスムーズなワークフローを提供するための重要なステップとなります。

## articles/search/tutorial-rag-build-solution-pipeline.md{#item-25ce01}

<details>
<summary>Diff</summary>
````diff
@@ -344,7 +344,7 @@ summer thaw. Nonetheless, this July 2001 image shows plenty of surface vegetatio
 shrubs, and grasses. The abundant fresh water also means the area is teeming with flies and mosquitoes.
 ```
 
-With this example, it's easier to spot how chunks are returned verbatim, and how keyword and similarity search identify top matches. This specific chunk definitely has information about water and coverage over the earth, but it's not exactly relevant to the query. Semantic ranking would find a better answer, but as a next step, let's see how to connect Azure AI Search to an LLM for conversational search.
+With this example, it's easier to spot how chunks are returned verbatim, and how keyword and similarity search identify top matches. This specific chunk definitely has information about water and coverage over the earth, but it's not exactly relevant to the query. Semantic ranker would find a better answer, but as a next step, let's see how to connect Azure AI Search to an LLM for conversational search.
 
 <!-- Objective:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランキング用語の修正"
}
```

### Explanation
この変更では、Azure AI Searchに関するチュートリアル文書内の用語が修正されました。具体的には、「セマンティックランキング」という用語が「セマンティックレンカー」に変更され、説明の一貫性が向上しています。

変更内容は以下の通りです：
- 「Semantic ranking」が「Semantic ranker」に置き換えられました。この修正により、セマンティックな手法が強調され、機能に関連する正しい用語を使用していることが明示されます。

この簡単な変更は、専門用語を正確に使用し、読者が技術的な内容をより正確に理解できるようにサポートしています。全体として、文書の整合性と明確さが向上しています。

## articles/search/vector-search-how-to-query.md{#item-9bb93c}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: cognitive-search
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 08/19/2024
+ms.date: 09/24/2024
 ---
 
 # Create a vector query in Azure AI Search
@@ -463,8 +463,6 @@ Weights are used when calculating the [reciprocal rank fusion](hybrid-search-ran
 
 The following example is a hybrid query with two vector query strings and one text string. Weights are assigned to the vector queries. The first query is 0.5 or half the weight, reducing its importance in the request. The second vector query is twice as important. 
 
-Text queries have no weight parameters, but you can increase or decrease their importance by setting [maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview).
-
 ```http
 POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?api-version=2024-07-01
 
@@ -489,6 +487,8 @@ POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?
     } 
 ```
 
+Vector weighting applies to vectors only. The text query in this example ("hello world") has an implicit weight of 1.0 or neutral weight. However, in a hybrid query, you can increase or decrease the importance of text fields by setting [maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview).
+
 ## Set thresholds to exclude low-scoring results (preview)
 
 Because nearest neighbor search always returns the requested `k` neighbors, it's possible to get multiple low scoring matches as part of meeting the `k` number requirement on search results. To exclude low-scoring search result, you can add a `threshold` query parameter that filters out results based on a minimum score. Filtering occurs before [fusing results](hybrid-search-ranking.md) from different recall sets. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントの日付更新と内容の修正"
}
```

### Explanation
この変更では、Azure AI Searchに関するドキュメントにおいて、日付の更新と内容の修正が行われました。具体的には、ドキュメントの最終更新日が2024年8月19日から2024年9月24日に変更され、いくつかの文が調整されています。

変更点は次の通りです：
- ドキュメントの日付が更新され、最新のリリース情報を反映するようになりました。
- ベクトルクエリの重み付けに関する説明が明確化され、新たに「ベクトル重み付けはベクトルのみに適用される」との記述が追加され、テキストクエリに対する暗黙の重みが1.0であることが明示されています。
- テキストクエリの重要度を増減する方法についての説明が強化され、`maxTextRecallSize`の設定についても参照が追加されています。
- 新しいセクション「スコアの低い結果を除外するための閾値を設定する（プレビュー）」が追加され、低スコアの検索結果を除外する方法が説明されています。

これらの修正により、読者は最新の情報にアクセスし、より具体的かつ明確な指示を得ることができるようになり、使いやすさが向上しています。

## articles/search/vector-search-integrated-vectorization-ai-studio.md{#item-353fcc}

<details>
<summary>Diff</summary>
````diff
@@ -71,8 +71,8 @@ The URI and key are generated when you deploy the model from the catalog. For mo
 {
   "@odata.type": "#Microsoft.Skills.Custom.AmlSkill",
   "context": "/document/pages/*",
-  "uri": "{YOUR_MODEL_URL_HERE}",
-  "key": "{YOUR_MODEL_KEY_HERE}",
+  "uri": "<YOUR_MODEL_URL_HERE>",
+  "key": "<YOUR_MODEL_KEY_HERE>",
   "inputs": [
     {
       "name": "input_data",
@@ -118,8 +118,8 @@ The URI and key are generated when you deploy the model from the catalog. For mo
 {
   "@odata.type": "#Microsoft.Skills.Custom.AmlSkill",
   "context": "/document/normalized_images/*",
-  "uri": "{YOUR_MODEL_URL_HERE}",
-  "key": "{YOUR_MODEL_HERE}",
+  "uri": "<YOUR_MODEL_URL_HERE>",
+  "key": "<YOUR_MODEL_HERE>",
   "inputs": [
     {
       "name": "input_data",
@@ -165,8 +165,8 @@ The URI and key are generated when you deploy the model from the catalog. For mo
 {
   "@odata.type": "#Microsoft.Skills.Custom.AmlSkill",
   "context": "/document/pages/*",
-  "uri": "{YOUR_MODEL_URL_HERE}/v1/embed",
-  "key": "{YOUR_MODEL_KEY_HERE}",
+  "uri": "<YOUR_MODEL_URL_HERE>/v1/embed",
+  "key": "<YOUR_MODEL_KEY_HERE>",
   "inputs": [
     {
       "name": "texts",
@@ -202,7 +202,7 @@ If you selected a different `embedding_types` in your skill definition that you
 "indexProjections": {
   "selectors": [
     {
-      "targetIndexName": "{YOUR_TARGET_INDEX_NAME_HERE}",
+      "targetIndexName": "<YOUR_TARGET_INDEX_NAME_HERE>",
       "parentKeyFieldName": "ParentKey", // Change this to the name of the field in your index definition where the parent key will be stored
       "sourceContext": "/document/pages/*",
       "mappings": [
@@ -230,12 +230,12 @@ For Cohere models, you should NOT add the `/v1/embed` path to the end of your UR
 ```json
 "vectorizers": [
     {
-        "name": "{YOUR_VECTORIZER_NAME_HERE}",
+        "name": "<YOUR_VECTORIZER_NAME_HERE>",
         "kind": "aml",
         "amlParameters": {
-            "uri": "{YOUR_URL_HERE}",
-            "key": "{YOUR_PRIMARY_KEY_HERE}",
-            "modelName": "{YOUR_MODEL_ID_HERE}"
+            "uri": "<YOUR_URL_HERE>",
+            "key": "<YOUR_PRIMARY_KEY_HERE>",
+            "modelName": "<YOUR_MODEL_ID_HERE>"
         },
     }
 ]
@@ -246,8 +246,8 @@ For Cohere models, you should NOT add the `/v1/embed` path to the end of your UR
 If you can't use key-based authentication, you can instead configure the AML skill and AI Studio vectorizer connection for [token authentication](../machine-learning/how-to-authenticate-online-endpoint.md) via role-based access control on Azure. The search service must have a [system or user-assigned managed identity](search-howto-managed-identities-data-sources.md), and the identity must have Owner or Contributor permissions for your AML project workspace. You can then remove the key field from your skill and vectorizer definition, replacing it with the resourceId field. If your AML project and search service are in different regions, also provide the region field.
 
 ```json
-"uri": "{YOUR_URL_HERE}",
-"resourceId": "subscriptions/{YOUR_SUBSCRIPTION_ID_HERE/resourceGroups/{YOUR_RESOURCE_GROUP_NAME_HERE}/providers/Microsoft.MachineLearningServices/workspaces/{YOUR_AML_WORKSPACE_NAME_HERE}/onlineendpoints/{YOUR_AML_ENDPOINT_NAME_HERE}",
+"uri": "<YOUR_URL_HERE>",
+"resourceId": "subscriptions/<YOUR_SUBSCRIPTION_ID_HERE>/resourceGroups/<YOUR_RESOURCE_GROUP_NAME_HERE>/providers/Microsoft.MachineLearningServices/workspaces/<YOUR_AML_WORKSPACE_NAME_HERE>/onlineendpoints/<YOUR_AML_ENDPOINT_NAME_HERE>",
 "region": "westus", // Only need if AML project lives in different region from search service
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレースホルダーの形式修正"
}
```

### Explanation
この変更では、Azure AI Searchに関連するドキュメントにおいて、URIやキーのプレースホルダーの形式が修正されました。具体的には、プレースホルダーの記述が波括弧 `{}` から角括弧 `<>` に変更され、ユーザーにとっての視認性が向上しています。

変更点は以下の通りです：
- プレースホルダーとして使用されるモデルのURIやキー、インデックス名、ボキャブラリー名などの項目が、`{YOUR_MODEL_URL_HERE}`などから`<YOUR_MODEL_URL_HERE>`の形式に変更されました。
- これにより、ユーザーが実際の値を挿入する際の指示がより明確になり、誤解を招く恐れが薄れてきました。
- 文書の他の部分でも同様に、プレースホルダーを一貫した形式に統一することにより、全体の整合性が向上しています。

この更新により、読者はより簡単に必要な情報を挿入できるようになり、ドキュメントの利用が直接的かつ明確になっています。

## articles/search/vector-store.md{#item-db9b8c}

<details>
<summary>Diff</summary>
````diff
@@ -86,7 +86,7 @@ We recommend the [Import and vectorize data wizard](search-get-started-portal-im
 
 The bias of this schema is that search documents are built around data chunks. If a language model formulates the response, as is typical for RAG apps, you want a schema designed around data chunks. 
 
-Data chunking is necessary for staying within the input limits of language models, but it also improves precision in similarity search when queries can be matched against smaller chunks of content pulled from multiple parent documents. Finally, if you're using semantic ranking, the semantic ranker also has token limits, which are more easily met if data chunking is part of your approach.
+Data chunking is necessary for staying within the input limits of language models, but it also improves precision in similarity search when queries can be matched against smaller chunks of content pulled from multiple parent documents. Finally, if you're using semantic ranker, the semantic ranker also has token limits, which are more easily met if data chunking is part of your approach.
 
 In the following example, for each search document, there's one chunk ID, chunk, title, and vector field. The chunkID and parent ID are populated by the wizard, using base 64 encoding of blob metadata (path). Chunk and title are derived from blob content and blob name. Only the vector field is fully generated. It's the vectorized version of the chunk field. Embeddings are generated by calling an Azure OpenAI embedding model that you provide.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書の表現の微修正"
}
```

### Explanation
この変更では、Azure AI Searchに関するドキュメントのテキストが微調整され、表現が改善されています。具体的には、「semantic ranker」の前に「the」が追加され、文章の流れがより自然になっています。

変更点は以下の通りです：
- 元のテキストでは「if you're using semantic ranking」という表現が、「if you're using semantic ranker」に変更されました。この修正により、言語モデルが使用する際の一貫性が向上します。
- 文の流れが改善され、読者にとっての理解がしやすくなりました。

この更新により、ドキュメントの質が向上し、読者が検討している内容をより効果的に把握できるようになります。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -90,12 +90,12 @@ ms.custom:
 | Month | Type | Announcement |
 |-------|------|-------------|
 | November | Feature | [**Vector search, generally available**](vector-search-overview.md). The previous restriction on customer-managed keys (CMK) is now lifted. [Prefiltering](vector-search-how-to-query.md) and [exhaustive K-nearest neighbor algorithm](vector-search-ranking.md) are also now generally available. |
-| November | Feature | [**Semantic ranking, generally available**](semantic-search-overview.md)|
+| November | Feature | [**Semantic ranker, generally available**](semantic-search-overview.md)|
 | November | Feature | [**Integrated vectorization (preview)**](vector-search-integrated-vectorization.md) adds data chunking and text-to-vector conversions during indexing, and also adds text-to-vector conversions at query time. |
 | November | Feature | [**Import and vectorize data wizard (preview)**](search-get-started-portal-import-vectors.md) automates data chunking and vectorization. It targets the [2023-10-01-Preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2023-10-01-preview&preserve-view=true) REST API. | 
 | November | Feature | [**Index projections (preview)**](index-projections-concept-intro.md) defines the shape of a secondary index, used for a one-to-many index pattern, where content from an enrichment pipeline can target multiple indexes. | 
 | November | API | [**2023-11-01 Search REST API**](/rest/api/searchservice/search-service-api-versions#2023-11-01) is stable version of the Search REST APIs for [vector search](vector-search-overview.md) and [semantic ranking](semantic-how-to-query-request.md). See [Upgrade REST APIs](search-api-migration.md) for migration steps to generally available features.|
-| November | API | [**2023-11-01 Management REST API**](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2023-11-01&preserve-view=true) adds APIs that [enable or disable semantic ranking](/rest/api/searchmanagement/services/create-or-update#searchsemanticsearch). |
+| November | API | [**2023-11-01 Management REST API**](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2023-11-01&preserve-view=true) adds APIs that [enable or disable semantic ranker](/rest/api/searchmanagement/services/create-or-update#searchsemanticsearch). |
 | November | Skill | [**Azure OpenAI Embedding skill (preview)**](cognitive-search-skill-azure-openai-embedding.md) connects to a deployed embedding model on your Azure OpenAI resource to generate embeddings during skillset execution.|
 | November | Skill | [**Text Split skill (preview)**](cognitive-search-skill-textsplit.md) updated in [2023-10-01-Preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2023-10-01-preview&preserve-view=true) to support native data chunking. |
 | November | Video | [**How vector search and semantic ranking improve your GPT prompts**](https://www.youtube.com/watch?v=Xwx1DJ0OqCk) explains how hybrid retrieval gives you optimal grounding data for generating useful AI responses and enables search over both concepts and keywords. |
@@ -139,4 +139,4 @@ This service has had multiple names over the years. Here they are in reverse chr
 
 ## Feature rename
 
-Semantic search was renamed to [semantic ranking](semantic-search-overview.md) in November 2023 to better describe the feature, which provides L2 ranking of an existing result set.
+Semantic search was renamed to [semantic ranker](semantic-search-overview.md) in November 2023 to better describe the feature, which provides L2 ranking of an existing result set.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の微調整"
}
```

### Explanation
この変更では、Azure AI Searchに関する「What's New」ドキュメント内で、用語が微調整されています。具体的には、特徴の名称が「Semantic ranking」から「Semantic ranker」に変更され、統一感と明確性が向上しています。

変更点は以下の通りです：
- 「Semantic ranking」が「Semantic ranker」に修正され、機能の目的をより正確に反映するようになりました。
- この変更は、ドキュメントの複数の場所で発生しており、機能の説明やAPIのバージョン情報などに影響を与えています。

こうした用語の修正は、読者が機能の内容を理解しやすくし、全体の文書の一貫性を保つことに寄与しています。特に、新しい機能が導入される際に、正しい用語を使用することは重要であり、ユーザーが必要な情報を迅速に見つけられるようになります。


