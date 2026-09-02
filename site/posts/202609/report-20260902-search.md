---
date: '2026-09-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8e2ab63...MicrosoftDocs:e6461f7
summary: このコードの変更は、Azure AI Searchに関する技術文書の一貫性と正確性を高めるためのさまざまなマイナーな更新を含んでいます。特に、移行ガイドではAzure
  Search SDK バージョン 11への重要な変更があり、他の文書では表現の明確化が行われています。新しい機能として同義語マップのフィールド名の更新や、移行に対する明確なガイドラインが提供されました。また、Azure.Search.Documentsクライアントライブラリの導入により、一部の互換性が失われているため、開発者は新しいAPIに従う必要があります。文書の日時や文言の修正も行われ、エラーメッセージやフィルタリング条件の説明が改善され、技術文書の精度が向上しました。これにより、著者や開発者は最新の技術環境に適応しやすくなり、専門知識を持たない読者でも理解しやすい内容となっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8e2ab63...MicrosoftDocs:e6461f7){target="_blank"}

<format>
# Highlights
このコードの変更は多くの記事にわたって行われたマイナーな更新を中心に、Azure AI Searchに関連した技術的ドキュメントの一貫性や正確性を高めることを目的としています。特に、移行ガイドではAzure Search SDK バージョン 11への重要な変更があり、その他のドキュメントでは主に表現の明確化が行われています。

## New features
- 同義語マップのリソース表現をより包括的にするためにフィールド名を更新。
- Azure Search SDK バージョン11への移行にあたっての明確なガイドラインの提供。

## Breaking changes
- 「Azure.Search.Documents」クライアントライブラリの導入に際し、前バージョンからの互換性が維持されていないため、開発者は新しいAPIに従う必要があります。

## Other updates
- 文書の日付のアップデートと文言の修正が多くのドキュメントにわたり行われました。
- 特定の表記やフィールド名がより整合性のある形に統一され、技術文書の精度が向上。
- エラーメッセージやフィルタリング条件の説明が改善され、Azure AI Searchの仕様理解が容易になっています。

# Insights
この一連の更新では、主にAzure AI Searchの技術文書が対象となっているため、日付の変更によりドキュメントが最新であることを反映すると共に、用語やフィールド名の統一により、読者に対して情報が間違いなく伝達されるように工夫されています。特に、Azure Search SDK バージョン 11への移行ガイドでは、非互換性が生じる大きな変更としてクライアントライブラリの刷新があり、開発者にとって重要な指針となっています。また、コラムの更新やAPI名の細かな調整により、正確で一貫した情報提供を目指す意図が明確です。

これにより、著者や開発者は最新の技術環境に適応しやすくなり、Azure AI Searchを効果的に活用するための糧となるドキュメントとなっています。特に、ドキュメントを用いる際に技術的なバックグラウンドを持たない場合でも、このシリーズの更新を読むことで専門的な知識を簡単に吸収することができると言えます。特にAPI仕様やフィールド名の整合性が保たれているため、実装時の混乱や誤解を減らし、実作業への迅速な反映が可能です。正確で一貫した技術情報は読者にとっての利用価値を高める重要な要素であり、今回の変更がそれをしっかり担っていることが窺えます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-index.md](#item-3fbd2e) | minor update | 同義語マップのリソース名の更新 | modified | 2 | 2 | 4 | 
| [cognitive-search-concept-annotations-syntax.md](#item-705b63) | minor update | ドキュメント内の表現の明確化 | modified | 4 | 4 | 8 | 
| [cognitive-search-concept-troubleshooting.md](#item-0d85b0) | minor update | トラブルシューティングガイドの更新 | modified | 8 | 10 | 18 | 
| [hybrid-search-overview.md](#item-6987b4) | minor update | ハイブリッド検索のドキュメント更新 | modified | 6 | 6 | 12 | 
| [knowledge-store-create-rest.md](#item-2643dd) | minor update | 知識ストア作成ガイドの修正 | modified | 9 | 5 | 14 | 
| [search-blob-metadata-properties.md](#item-2137f3) | minor update | Blobメタデータプロパティの記事更新 | modified | 1 | 1 | 2 | 
| [search-dotnet-sdk-migration-version-11.md](#item-5ca9e8) | breaking change | Azure Search SDK バージョン 11 への移行ガイドの更新 | modified | 19 | 18 | 37 | 
| [search-how-to-index-azure-data-lake-storage.md](#item-faca23) | minor update | Azure Data Lake Storage Gen2 インデクサー設定の更新 | modified | 5 | 5 | 10 | 
| [search-how-to-index-azure-tables.md](#item-c8a1d1) | minor update | Azure Table インデクサー設定の更新 | modified | 6 | 6 | 12 | 
| [search-how-to-index-cosmosdb-gremlin.md](#item-e5e93d) | minor update | Azure Cosmos DB Gremlin インデクサー設定の更新 | modified | 9 | 11 | 20 | 
| [search-how-to-index-cosmosdb-mongodb.md](#item-b5aa9f) | minor update | Azure Cosmos DB for MongoDB インデクサー設定の更新 | modified | 9 | 10 | 19 | 
| [search-how-to-index-cosmosdb-sql.md](#item-2e888b) | minor update | Azure Cosmos DB NoSQL インデクサー設定の更新 | modified | 11 | 11 | 22 | 
| [search-how-to-index-sql-database.md](#item-86d873) | minor update | Azure SQL インデクサー設定の更新 | modified | 48 | 42 | 90 | 
| [search-howto-managed-identities-azure-functions.md](#item-2f13c4) | minor update | Azure Functions におけるマネージド ID の設定方法の更新 | modified | 4 | 4 | 8 | 
| [search-index-access-control-lists-and-rbac-push-api.md](#item-45e71e) | minor update | インデックスのアクセス制御リストと RBAC に関する更新 | modified | 1 | 1 | 2 | 
| [search-indexer-securing-resources.md](#item-c075c4) | minor update | リソース保護に関するインデクサーの更新 | modified | 1 | 1 | 2 | 
| [search-language-support.md](#item-a7979b) | minor update | 言語サポートに関するドキュメントの更新 | modified | 8 | 8 | 16 | 
| [search-pagination-page-layout.md](#item-115902) | minor update | ページネーションおよび結果のレイアウトに関するドキュメントの更新 | modified | 7 | 7 | 14 | 
| [search-query-overview.md](#item-dcd5d6) | minor update | 検索クエリ概要に関するドキュメントの更新 | modified | 15 | 15 | 30 | 
| [search-query-troubleshoot-collection-filters.md](#item-abeca4) | minor update | コレクションフィルタのトラブルシューティングに関するドキュメントの更新 | modified | 3 | 3 | 6 | 
| [search-query-understand-collection-filters.md](#item-32c01a) | minor update | コレクションフィルタの理解に関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [tutorial-create-custom-analyzer.md](#item-ad5520) | minor update | カスタムアナライザー作成に関するチュートリアルの更新 | modified | 6 | 6 | 12 | 
| [tutorial-multiple-data-sources.md](#item-71558f) | minor update | 複数のデータソースからのデータインポートチュートリアルの更新 | modified | 5 | 5 | 10 | 
| [tutorial-optimize-indexing-push-api.md](#item-ef0e96) | minor update | インデックス作成の最適化に関するチュートリアルの更新 | modified | 9 | 18 | 27 | 
| [vector-search-index-size.md](#item-bb2846) | minor update | ベクトル検索インデックスサイズに関する記事の更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-index.md{#item-3fbd2e}

<details>
<summary>Diff</summary>
````diff
@@ -318,14 +318,14 @@ Analyzers are defined within a search index and assigned to fields. The [fields
 
 [Synonym maps](search-synonyms.md) expand queries by adding synonyms for named terms. For example, you might have scientific or medical terms for common terms.
 
-Synonym maps are defined as a top-level resource on a search index and assigned to fields. The [fields collection example](#example-index-definition) doesn't include a synonym map, but the following example shows how a synonym map with variant spellings of country names might be assigned to a hypothetical "locations" field.
+Synonym maps are defined as a top-level resource on a search index and assigned to fields. The [fields collection example](#example-index-definition) doesn't include a synonym map, but the following example shows how a synonym map with variant spellings of country/region names might be assigned to a hypothetical "locations" field.
 
 ```json
 {
     "name":"locations",
     "type":"Edm.String",
     "searchable":true,
-    "synonymMaps":[ "country-synonyms" ]
+    "synonymMaps":[ "country-region-synonyms" ]
 }
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "同義語マップのリソース名の更新"
}
```

### Explanation
この変更は、同義語マップに関連するリソース名の一部を更新するマイナーな改訂です。具体的には、国名の変種の綴りを含む同義語マップのフィールド名が「country-synonyms」から「country-region-synonyms」に変更されました。この変更により、リソースの表現がより正確になり、地域の名前を包括的に扱うことが可能になります。また、関連する例文もこれに応じて更新されています。

## articles/search/cognitive-search-concept-annotations-syntax.md{#item-705b63}

<details>
<summary>Diff</summary>
````diff
@@ -5,12 +5,12 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ---
 
-# Reference a path to enriched nodes using context and source properties an Azure AI Search skillset
+# Reference a path to enriched nodes by using context and source properties in an Azure AI Search skillset
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
@@ -105,13 +105,13 @@ To invoke the right number of iterations, set the context as `"/document/people/
     "outputs": [
       {
         "name": "lastname",
-        "targetName": "last"
+        "targetName": "lastname"
       }
     ]
   }
 ```
 
-When annotations are arrays or collections of strings, you might want to target specific members rather than the array as a whole. The previous example generates an annotation called `"last"` under each node represented by the context. If you want to refer to this family of annotations, you could use the syntax `"/document/people/*/last"`. If you want to refer to a particular annotation, you could use an explicit index: `"/document/people/1/last`" to reference the last name of the first person identified in the document. Notice that in this syntax arrays are "0 indexed".
+When annotations are arrays or collections of strings, you might want to target specific members rather than the array as a whole. The previous example generates an annotation called `"lastname"` under each node represented by the context. If you want to refer to this family of annotations, use the syntax `"/document/people/*/lastname"`. If you want to refer to a particular annotation, use an explicit index (`"/document/people/1/lastname"`) to reference the last name of the first person identified in the document. Notice that in this syntax, arrays are zero indexed.
 
 <a name="example-3"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメント内の表現の明確化"
}
```

### Explanation
この変更は、Azure AI Search スキルセットに関するドキュメントの表現を明確化するためのマイナーな更新です。具体的には、日付が「07/21/2026」から「08/31/2026」へ変更され、ドキュメント内のいくつかのフレーズが改善されました。たとえば、"by using"が文中に追加され、より明確な表現になりました。また、注釈に関する説明も更新され、呼び出しの際に参照するフィールド名が「last」から「lastname」に修正されました。これにより、利用者が具体的な情報をより分かりやすく理解できるようになっています。

## articles/search/cognitive-search-concept-troubleshooting.md{#item-0d85b0}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: best-practice
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ---
@@ -30,12 +30,10 @@ To ignore errors during development, set `maxFailedItems` and `maxFailedItemsPer
 
 ```json
 {
-  // rest of your indexer definition
-   "parameters":
-   {
-      "maxFailedItems":-1,
-      "maxFailedItemsPerBatch":-1
-   }
+  "parameters": {
+    "maxFailedItems": -1,
+    "maxFailedItemsPerBatch": -1
+  }
 }
 ```
 
@@ -44,11 +42,11 @@ To ignore errors during development, set `maxFailedItems` and `maxFailedItemsPer
 
 ## Tip 3: Use Debug session to troubleshoot problems
 
-[**Debug session**](./cognitive-search-debug-session.md) is a visual editor that shows a skillset's dependency graph, inputs and outputs, and definitions. It works by loading a single document from your search index, with the current indexer and skillset configuration. You can then run the entire skillset, scoped to a single document. Within a debug session, you can identify and resolve errors, validate changes, and commit changes to a parent skillset. For a walkthrough, see [Tutorial: debug sessions](./cognitive-search-tutorial-debug-sessions.md).
+[**Debug session**](./cognitive-search-debug-session.md) is a visual editor that shows a skillset's dependency graph, inputs and outputs, and definitions. It loads a single source document from the indexer data source with the current indexer and skillset configuration. You can then run the entire skillset, scoped to that document. Within a debug session, you can identify and resolve errors, validate changes, and commit changes to a parent skillset. For a walkthrough, see [Tutorial: debug sessions](./cognitive-search-tutorial-debug-sessions.md).
 
 ## Tip 4: Expected content doesn't appear
 
-If content is missing, check for dropped documents in the Azure portal. In the search service page, open **Indexers** and look at the **Docs succeeded** column. Select it to view indexer execution history and review specific errors. 
+If content is missing, check for dropped documents in the Azure portal. On the search service page, open **Indexers**, select the indexer, and then select a run's **Status** value to view execution details and errors.
 
 If the problem is related to file size, you might see an error like this: "The blob \<file-name>" has the size of \<file-size> bytes, which exceeds the maximum size for document extraction for your current service tier." For more information on indexer limits, see [Service limits](search-limits-quotas-capacity.md).
 
@@ -58,7 +56,7 @@ A second reason for content failing to appear might be related to input/output m
 
 Image analysis is computationally intensive for even simple cases, so when images are especially large or complex, processing times can exceed the maximum time allowed.
 
-For indexers that have skillsets, skillset execution is [capped at 2 hours for most tiers](search-limits-quotas-capacity.md#indexer-limits). If skillset processing fails to complete within that period, you can put your indexer on a 2-hour recurring schedule to have the indexer pick up processing where it left off. 
+For indexers that have skillsets, skillset execution is [capped at 2 hours for most tiers](search-limits-quotas-capacity.md#indexer-limits). If skillset processing fails to complete within that period, schedule the indexer to run every five minutes so it can resume processing from the last known good document.
 
 Scheduled indexing resumes at the last known good document. On a recurring schedule, the indexer can work its way through the image backlog over a series of hours or days, until all unprocessed images are processed. For more information on schedule syntax, see [Schedule an indexer](search-howto-schedule-indexers.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トラブルシューティングガイドの更新"
}
```

### Explanation
この変更は、Azure AI Search のトラブルシューティングガイドに対するマイナーな更新です。主な変更点として、日付が「07/21/2026」から「08/31/2026」に変更され、いくつかの表現が改善されています。特に、エラーハンドリングに関するJSONのパラメータ設定が整理され、書式が一貫性を持つように更新されました。

また、デバッグセッションに関する説明が強化され、ソースドキュメントからインデクサーデータソースの読み込み方法がより明確になりました。さらに、Azureポータルでドロップされたドキュメントを確認する手順も具体化されており、ユーザーがインデクサーの実行詳細やエラーをより簡単にレビューできるようになっています。最後に、インデクサーのスケジュール設定に関する推奨事項が追加され、プロセスの再開方法がより具体的に示されています。

## articles/search/hybrid-search-overview.md{#item-6987b4}

<details>
<summary>Diff</summary>
````diff
@@ -5,17 +5,17 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ai-usage: ai-assisted
 ---
 
-# Hybrid search using vectors and full text in Azure AI Search
+# Hybrid search using vectors and full-text search in Azure AI Search
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 Hybrid search is a single query request configured for both full-text and vector queries. It runs against a search index that contains searchable, plain-text content and generated embeddings. For query purposes, hybrid search:
 
-+ Is a single query request that includes both `search` and `vectors` query parameters.
++ Is a single query request that includes both `search` and `vectorQueries` query parameters.
 + Runs full-text search and vector search in parallel.
 + Merges results from each query by using [Reciprocal Rank Fusion (RRF)](hybrid-search-ranking.md).
 
@@ -57,15 +57,15 @@ content-type: application/JSON
     "vectorQueries": [
         {
             "kind": "vector",
-            "vector": [ <array of embeddings> ]
+            "vector": [ <array of embeddings> ],
             "k": 50,
             "fields": "DescriptionVector",
             "exhaustive": true,
             "oversampling": 20
         },
         {
             "kind": "vector",
-            "vector": [ <array of embeddings> ]
+            "vector": [ <array of embeddings> ],
             "k": 50,
             "fields": "Description_frVector",
             "exhaustive": false,
@@ -85,7 +85,7 @@ content-type: application/JSON
 + `search` specifies a single full-text search query.
 + `vectorQueries` specifies vector queries, which can be multiple, targeting multiple vector fields. If the embedding space includes multilingual content, vector queries can find the match with no language analyzers or translation required. If you're using semantic ranker, set `k` to 50 to maximize its inputs.
 + `select` specifies which fields to return in results, which should be human-readable text fields if you're showing them to users or sending them to a large language model (LLM).
-+ `filters` can specify geospatial search or other inclusion and exclusion criteria, such as whether parking is included. The geospatial query in this example finds hotels within a 300-kilometer radius of Washington D.C. You can apply the filter at the beginning or end of query processing. If you're using semantic ranker, you probably want post-filtering as the last step, but you should test to confirm which behavior is best for your queries.
++ `filter` can specify geospatial search or other inclusion and exclusion criteria, such as whether parking is included. The geospatial query in this example finds hotels within a 300-kilometer radius of Washington, D.C. You can apply the filter at the beginning or end of query processing. If you're using semantic ranker, you probably want post-filtering as the last step, but you should test to confirm which behavior is best for your queries.
 + `facets` can be used to compute facet buckets over results that are returned from hybrid queries.
 + `queryType=semantic` invokes [semantic ranker](semantic-search-overview.md), applying machine reading comprehension to surface more relevant search results. Semantic ranking is optional. If you aren't using this feature, remove the last three lines of the hybrid query.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索のドキュメント更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるハイブリッド検索の概要に関するドキュメントに対するマイナーな更新です。主な変更点は、日付の更新（「07/21/2026」から「08/31/2026」）といくつかの表現の改善です。具体的には、「full-text search」が「full-text search」に修正され、クエリパラメータに関する記述で「vectors」が「vectorQueries」と改められ、一貫性のある表現となっています。

さらに、パラメータの説明が一部進化しており、特に`filters`パラメータが`filter`に変更されました。また、地理空間検索やその他のフィルタリング基準の明示的な説明が保たれており、ユーザーがクエリ処理の開始または終了時にフィルタを適用できることが示されています。全体を通して、トピックの明晰さを高めるための表現が改善されており、ハイブリッド検索の機能や使い方についての理解が深まる内容となっています。

## articles/search/knowledge-store-create-rest.md{#item-2643dd}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Create a Knowledge Store Using REST
 description: Use the REST APIs to create an Azure AI Search knowledge store for persisting AI enrichments from a skillset.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ai-usage: ai-assisted
 ms.custom:
   - ignite-2023
@@ -70,7 +70,7 @@ In this example, REST calls require the search service endpoint and use an API k
 
    :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
 
-A valid API key establishes trust, on a per request basis, between the application sending the request and the search service handling it.
+A valid API key establishes trust, on a per-request basis, between the application sending the request and the search service handling it.
 
 ## Create an index
 
@@ -313,7 +313,7 @@ A skillset defines enrichments (skills) and your knowledge store. [Create Skills
 
 + The [Shaper skill](cognitive-search-skill-shaper.md) is important to knowledge store definition. It specifies how the data flows into the tables of the knowledge store. The inputs are the parts of the enriched document that you want to store. The output is a consolidation of the nodes into a single structure. 
 
-+ Projections specify the tables, objects, and blobs of your knowledge store. Each projection item specifies the `"name"` of column or field to create in Azure Storage. The `"source"` specifies which part of the shaper output is assigned to that field or column.
++ Projections specify the tables, objects, and blobs in your knowledge store. A table projection specifies `tableName`, `generatedKeyName`, and either `source` or `sourceContext` with `inputs`. The `source` and `sourceContext` properties identify the enriched content to store.
 
 ## Create an indexer
 
@@ -367,7 +367,7 @@ A skillset defines enrichments (skills) and your knowledge store. [Create Skills
 
 ## Check status
 
-After you send each request, the search service should respond with a 201 success message.
+Check the indexer status to confirm that the skillset completed successfully.
 
 ```http
 ### Get Indexer Status (wait several minutes for the indexer to complete)
@@ -376,7 +376,9 @@ GET {{baseUrl}}/indexers/hotel-reviews-kstore-idxr/status?api-version=2026-04-01
   api-key: {{apiKey}}
 ```
 
-After several minutes, you can query the index to inspect the content. Even if you're not using the index, this step is a convenient way to confirm that the skillset produced the expected output.
+The request returns `200 OK`. Wait until `lastResult.status` is `success` before you query the index.
+
+Query the index to inspect the content. Even if you're not using the index, this step is a convenient way to confirm that the skillset produced the expected output.
 
 ```http
 ### Query the index (indexer status must be "success" before querying the index)
@@ -391,6 +393,8 @@ POST {{baseUrl}}/indexes/hotel-reviews-kstore-idx/docs/search?api-version=2026-0
   }
 ```
 
+The request returns `200 OK` and includes the selected enriched fields.
+
 ## Check tables in Azure portal
 
 In the Azure portal, switch to your Azure Storage account and use **Storage Browser** to view the new tables. You should see six tables, one for each projection defined in the skillset.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ストア作成ガイドの修正"
}
```

### Explanation
この変更は、Azure AI Searchの「RESTを使用して知識ストアを作成する」ガイドに対するマイナーな更新です。主な変更点として、日付が「07/21/2026」から「08/31/2026」に変更され、一部の文言が明確化されています。

具体的には、APIキーに関する説明が改善され、リクエストごとに信頼を確立することが強調されています。さらに、プロジェクションの定義についても内容が改訂され、テーブルプロジェクションが`tableName`、`generatedKeyName`、および`source`または`sourceContext`と`inputs`の組み合わせからなることが示されています。

また、インデクサーのステータス確認に関する文が更新され、インデクサーの処理が成功したことを確認してからインデックスをクエリすることが推奨されています。これにより、ユーザーはスキルセットが期待通りの出力を生成したことを確認するためにインデックスをクエリする便利な手順を踏むことができます。全体的に、操作手順の明瞭さが向上しており、ユーザーが理解しやすい内容に改訂されています。

## articles/search/search-blob-metadata-properties.md{#item-2137f3}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ai-usage: ai-assisted
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blobメタデータプロパティの記事更新"
}
```

### Explanation
この変更は、Azure AI Searchに関する「Blobメタデータプロパティ」に関する記事に対するマイナーな更新を含んでいます。具体的には、文書の日付が「07/21/2026」から「08/31/2026」に変更されており、これにより新しいリリース日が反映されています。この更新は、文書の最新性を保つことを目的としており、他のコンテンツには影響を与えない小規模な修正です。全体的に、記事は引き続きBlobメタデータプロパティの概念を扱っており、最新の日付に更新されることで読者に対する信頼性が向上しています。

## articles/search/search-dotnet-sdk-migration-version-11.md{#item-5ca9e8}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Migrate your search application code from older SDK versions to the
 ms.service: azure-ai-search
 ms.devlang: csharp
 ms.topic: upgrade-and-migration-article
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ms.custom:
@@ -17,17 +17,18 @@ ms.custom:
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-If you built your search solution on the [**Azure SDK for .NET**](/dotnet/azure/), this article helps you migrate your code from earlier versions of [**Microsoft.Azure.Search**](/dotnet/api/overview/azure/search) to version 11, the new [**Azure.Search.Documents**](/dotnet/api/overview/azure/search.documents-readme) client library. Version 11 is a fully redesigned client library, released by the Azure SDK development team (previous versions were produced by the Azure AI Search development team).
+If you built your search solution on the [**Azure SDK for .NET**](/dotnet/azure/), this article helps you migrate your code from earlier versions of [**Microsoft.Azure.Search**](/dotnet/api/overview/azure/search) to version 11 of the [**Azure.Search.Documents**](/dotnet/api/overview/azure/search.documents-readme) client library. Version 11 is a fully redesigned client library produced by the Azure SDK development team. Previous versions were produced by the Azure AI Search development team.
 
 All features from version 10 are implemented in version 11. Key differences include:
 
 + One package (**Azure.Search.Documents**) instead of four
 + Three clients instead of two: SearchClient, SearchIndexClient, SearchIndexerClient
 + Naming differences across a range of APIs and small structural differences that simplify some tasks
 
-The client library's [Change Log](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) has an itemized list of updates. You can review a [summarized version](#WhatsNew) in this article.
+The client library's [changelog](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) has an itemized list of updates. You can review a [summarized version](#WhatsNew) in this article.
 
-All C# code samples and snippets in the Azure AI Search product documentation have been revised to use the new **Azure.Search.Documents** client library.
+> [!IMPORTANT]
+> This article provides version 10-to-version 11 API mappings. For new development, use the current stable version of **Azure.Search.Documents**.
 
 ## Why upgrade?
 
@@ -37,7 +38,7 @@ The benefits of upgrading are summarized as follows:
 
 + Consistency with other Azure client libraries. **Azure.Search.Documents** takes a dependency on [Azure.Core](/dotnet/api/azure.core) and [System.Text.Json](/dotnet/api/system.text.json), and follows conventional approaches for common tasks such as client connections and authorization.
 
-**Microsoft.Azure.Search** is officially retired. If you're using an old version, we recommend upgrading to the next higher version, repeating the process in succession until you reach version 11 and **Azure.Search.Documents**. An incremental upgrade strategy makes it easier to find and fix blocking issues. See [Previous version docs](/previous-versions/azure/search/) for guidance.
+**Microsoft.Azure.Search** is officially retired. Migrate to **Azure.Search.Documents**. If you're moving across several legacy versions, update incrementally to help identify and resolve blocking issues. For guidance, see [Previous version docs](/previous-versions/azure/search/).
 
 ## Package comparison
 
@@ -53,18 +54,18 @@ Where applicable, the following table maps the client libraries between the two
 
 | Client operations | Microsoft.Azure.Search&nbsp;(v10) | Azure.Search.Documents&nbsp;(v11) |
 |---------------------|------------------------------|------------------------------|
-| Targets the documents collection of an index (queries and data import) | [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient) | [SearchClient](/dotnet/api/azure.search.documents.searchclient) |
+| Targets the documents collection of an index (queries and data import) | [SearchIndexClient](/dotnet/api/microsoft.azure.search.searchindexclient) | [SearchClient](/dotnet/api/azure.search.documents.searchclient) |
 | Targets index-related objects (indexes, analyzers, synonym maps | [SearchServiceClient](/dotnet/api/microsoft.azure.search.searchserviceclient) | [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient) |
 | Targets indexer-related objects (indexers, data sources, skillsets) | [SearchServiceClient](/dotnet/api/microsoft.azure.search.searchserviceclient) | [SearchIndexerClient (**new**)](/dotnet/api/azure.search.documents.indexes.searchindexerclient) |
 
-> [!Caution]
-> Notice that SearchIndexClient exists in both versions, but targets different operations. In version 10, SearchIndexClient creates indexes and other objects. In version 11, SearchIndexClient works with existing indexes, targeting the documents collection with query and data ingestion APIs. To avoid confusion when updating code, be mindful of the order in which client references are updated. Following the sequence in [Steps to upgrade](#UpgradeSteps) should help mitigate any string replacement issues.
+> [!CAUTION]
+> `SearchIndexClient` exists in both versions but targets different operations. In version 10, it targets the documents collection. In version 11, it creates indexes and other schema objects. To avoid confusion when updating code, update client references in the sequence in [Steps to upgrade](#UpgradeSteps).
 
 <a name="naming-differences"></a>
 
 ## Naming and other API differences
 
-Besides the client differences (noted previously and thus omitted here), multiple other APIs have been renamed and in some cases redesigned. Class name differences are summarized in the following sections. This list isn't exhaustive but it does group API changes by task, which can be helpful for revisions on specific code blocks. For an itemized list of API updates, see the [change log](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) for `Azure.Search.Documents` on GitHub.
+Besides the client differences (noted previously and thus omitted here), multiple other APIs have been renamed and in some cases redesigned. The following sections summarize class name differences. This list isn't exhaustive, but it groups API changes by task, which can be helpful for revisions on specific code blocks. For an itemized list of API updates, see the [changelog](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) for `Azure.Search.Documents` on GitHub.
 
 ### Authentication and encryption
 
@@ -91,14 +92,14 @@ Besides the client differences (noted previously and thus omitted here), multipl
 
 Field definitions are streamlined: [SearchableField](/dotnet/api/azure.search.documents.indexes.models.searchablefield), [SimpleField](/dotnet/api/azure.search.documents.indexes.models.simplefield), [ComplexField](/dotnet/api/azure.search.documents.indexes.models.complexfield) are new APIs for creating field definitions.
 
-### Indexers, datasources, skillsets
+### Indexers, data sources, and skillsets
 
 | Version 10 | Version 11 equivalent |
 |------------|-----------------------|
 | [Indexer](/dotnet/api/microsoft.azure.search.models.indexer) | [SearchIndexer](/dotnet/api/azure.search.documents.indexes.models.searchindexer) |
 | [DataSource](/dotnet/api/microsoft.azure.search.models.datasource) | [SearchIndexerDataSourceConnection](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) |
 | [Skill](/dotnet/api/microsoft.azure.search.models.skill) | [SearchIndexerSkill](/dotnet/api/azure.search.documents.indexes.models.searchindexerskill) |
-| [Skillset](/dotnet/api/microsoft.azure.search.models.skillset) | [SearchIndexerSkillset](/dotnet/api/azure.search.documents.indexes.models.searchindexerskill) |
+| [Skillset](/dotnet/api/microsoft.azure.search.models.skillset) | [SearchIndexerSkillset](/dotnet/api/azure.search.documents.indexes.models.searchindexerskillset) |
 | [DataSourceType](/dotnet/api/microsoft.azure.search.models.datasourcetype) | [SearchIndexerDataSourceType](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourcetype) |
 
 ### Data import
@@ -158,7 +159,7 @@ If you're using Newtonsoft.Json for JSON serialization, you can pass in global n
 
 ## Inside v11
 
-Each version of an Azure AI Search client library targets a corresponding version of the REST API. The REST API is considered foundational to the service, with individual SDKs wrapping a version of the REST API. As a .NET developer, it can be helpful to review the more verbose [REST API documentation](/rest/api/searchservice/) for more in depth coverage of specific objects or operations. Version 11 targets the [2020-06-30 search service specification](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/search/data-plane/Search/stable/2020-06-30). 
+Each version of an Azure AI Search client library targets a corresponding version of the REST API. The REST API is foundational to the service, with individual SDKs wrapping a version of the REST API. As a .NET developer, it can be helpful to review the more verbose [REST API documentation](/rest/api/searchservice/) for more in-depth coverage of specific objects or operations. Version 11 targets the [2020-06-30 search service specification](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/search/data-plane/Search/stable/2020-06-30).
 
 Version 11.0 fully supports the following objects and operations:
 
@@ -169,20 +170,20 @@ Version 11.0 fully supports the following objects and operations:
 + Skillset creation and management
 + All query types and syntax
 
-Version 11.1 additions ([change log](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1110-2020-08-11) details):
+Version 11.1 additions ([changelog](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1110-2020-08-11) details):
 
 + [FieldBuilder](/dotnet/api/azure.search.documents.indexes.fieldbuilder) (added in 11.1)
 + [Serializer property](/dotnet/api/azure.search.documents.searchclientoptions.serializer) (added in 11.1) to support custom serialization
 
-Version 11.2 additions ([change log](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1120-2021-02-10) details):
+Version 11.2 additions ([changelog](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1120-2021-02-10) details):
 
 + [EncryptionKey](/dotnet/api/azure.search.documents.indexes.models.searchindexer.encryptionkey) property added indexers, data sources, and skillsets
 + [IndexingParameters.IndexingParametersConfiguration](/dotnet/api/azure.search.documents.indexes.models.indexingparametersconfiguration) property support
 + [Geospatial types](/dotnet/api/azure.search.documents.indexes.models.searchfielddatatype.geographypoint) are natively supported in [FieldBuilder](/dotnet/api/azure.search.documents.indexes.fieldbuilder.build). [SearchFilter](/dotnet/api/azure.search.documents.searchfilter) can encode geometric types from Microsoft.Spatial without an explicit assembly dependency.
 
   You can also continue to explicitly declare a dependency on [Microsoft.Spatial](https://www.nuget.org/packages/Microsoft.Spatial/). Examples of this technique are available for [System.Text.Json](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Microsoft.Azure.Core.Spatial/README.md) and [Newtonsoft.Json](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Microsoft.Azure.Core.Spatial.NewtonsoftJson/README.md).
 
-Version 11.3 additions ([change log](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1130-2021-06-08) details):
+Version 11.3 additions ([changelog](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1130-2021-06-08) details):
 
 + [KnowledgeStore](/dotnet/api/azure.search.documents.indexes.models.knowledgestore)
 + Added support for Azure.Core.GeoJson types in [SearchDocument](/dotnet/api/azure.search.documents.models.searchdocument), [SearchFilter](/dotnet/api/azure.search.documents.searchfilter) and [FieldBuilder](/dotnet/api/azure.search.documents.indexes.fieldbuilder).
@@ -226,7 +227,7 @@ The following steps get you started on a code migration by walking through the f
    SearchIndexClient indexClient = new SearchIndexClient(endpoint, credential);
    ```
 
-1. Add new client references for indexer-related objects. If you're using indexers, datasources, or skillsets, change the client references to [SearchIndexerClient](/dotnet/api/azure.search.documents.indexes.searchindexerclient). This client is new in version 11 and has no antecedent.
+1. Add new client references for indexer-related objects. If you're using indexers, data sources, or skillsets, change the client references to [SearchIndexerClient](/dotnet/api/azure.search.documents.indexes.searchindexerclient). This client is new in version 11 and has no antecedent.
 
 1. Revise collections and lists. In the new SDK, all lists are read-only to avoid downstream issues if the list happens to contain null values. The code change is to add items to a list. For example, instead of assigning strings to a Select property, you would add them as follows:
 
@@ -252,7 +253,7 @@ The following steps get you started on a code migration by walking through the f
 
 1. Update client references for index, synonym map, and analyzer objects. Instances of [SearchServiceClient](/dotnet/api/microsoft.azure.search.searchserviceclient) should be changed to [SearchIndexClient](/dotnet/api/microsoft.azure.search.searchindexclient). 
 
-1. For the remainder of your code, update classes, methods, and properties to use the APIs of the new library. The [naming differences](#naming-differences) section is a place to start but you can also review the [change log](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md).
+1. For the remainder of your code, update classes, methods, and properties to use the APIs of the new library. The [naming differences](#naming-differences) section is a place to start, but you can also review the [changelog](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md).
 
    If you have trouble finding equivalent APIs, we suggest logging an issue on [https://github.com/MicrosoftDocs/azure-docs/issues](https://github.com/MicrosoftDocs/azure-docs/issues) so that we can improve the documentation or investigate the problem.
 
@@ -262,7 +263,7 @@ The following steps get you started on a code migration by walking through the f
 
 ## Breaking changes
 
-Given the sweeping changes to libraries and APIs, an upgrade to version 11 is non-trivial and constitutes a breaking change in the sense that your code will no longer be backward compatible with version 10 and earlier. For a thorough review of the differences, see the [change log](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) for `Azure.Search.Documents`.
+Given the sweeping changes to libraries and APIs, an upgrade to version 11 is non-trivial and constitutes a breaking change in the sense that your code is no longer backward compatible with version 10 and earlier. For a thorough review of the differences, see the [changelog](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) for `Azure.Search.Documents`.
 
 In terms of service version updates, where code changes in version 11 relate to existing functionality (and not just a refactoring of the APIs), you'll find the following behavior changes:
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azure Search SDK バージョン 11 への移行ガイドの更新"
}
```

### Explanation
この変更は、「Azure Search SDK バージョン 11 への移行」に関する記事の大幅な更新を反映しています。主に、文書の日付が「07/21/2026」から「08/31/2026」に変更されており、移行プロセスが一層明確化されています。

記事では、古いバージョンから新しい「Azure.Search.Documents」クライアントライブラリへの移行をサポートする内容が含まれています。特に、バージョン 11は完全に再設計されたクライアントライブラリであり、以前のバージョンはAzure AI Search開発チームによって制作されていた点が強調されているほか、クライアント数やAPIの命名規則、構造に関する変更も詳述されています。

また、移行時の注意点や、バージョン 10 から 11 への新しい API マッピングを提供する重要な情報が追加され、開発者が混乱を避けるための具体的な手順が示されています。「Microsoft.Azure.Search」が正式に廃止された旨も触れられており、ユーザーには新しいクライアントの利用を推奨しています。

全体として、この更新はバージョン 11 への移行過程が明確に示され、開発者が新しいライブラリへの順応をスムーズに行えるように配慮されています。これは、非互換性を伴う重大な変更であり、開発者に対してより明確なガイダンスを提供することを目的としています。

## articles/search/search-how-to-index-azure-data-lake-storage.md{#item-faca23}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +1,10 @@
 ---
 title: Azure Data Lake Storage Gen2 Indexer
-description: Set up an Azure Data Lake Storage (ADLS) Gen2 indexer to automate indexing of content and metadata for full text search in Azure AI Search.
+description: Set up an Azure Data Lake Storage (ADLS) Gen2 indexer to automate indexing of content and metadata for full-text search in Azure AI Search.
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/08/2026
+ms.date: 08/31/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ms.custom: [ignite-2023, sfi-ropc-nochange, doc-kit-assisted]
@@ -146,7 +146,7 @@ Indexers can connect to a blob container using the following connections.
 |`{ "connectionString" : "ResourceId=/subscriptions/<your subscription ID>/resourceGroups/<your resource group name>/providers/Microsoft.Storage/storageAccounts/<your storage account name>/;" }`|
 |This connection string doesn't require an account key, but you must have previously configured a search service to [connect using a managed identity](search-how-to-managed-identities.md).|
 
-| Storage account shared access signature** (SAS) connection string |
+| Storage account shared access signature (SAS) connection string |
 |-------------------------------------------------------------------|
 | `{ "connectionString" : "BlobEndpoint=https://<your account>.blob.core.windows.net/;SharedAccessSignature=?sv=2016-05-31&sig=<the signature>&spr=https&se=<the validity end time>&srt=co&ss=b&sp=rl;" }` |
 | The SAS should have the list and read permissions on containers and objects (blobs in this case). |
@@ -160,7 +160,7 @@ In a [search index](search-what-is-an-index.md), add fields to accept the conten
 
 1. [Create or update an index](/rest/api/searchservice/indexes/create) to define search fields that store blob content and metadata:
 
-    ```http
+    ```json
     {
         "name" : "my-search-index",
         "fields": [
@@ -195,7 +195,7 @@ Once the index and data source have been created, you're ready to create the ind
 
 1. [Create or update an indexer](/rest/api/searchservice/indexers/create) by giving it a name and referencing the data source and target index:
 
-    ```http
+    ```json
     {
       "name" : "my-adlsgen2-indexer",
       "dataSourceName" : "my-adlsgen2-datasource",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Data Lake Storage Gen2 インデクサー設定の更新"
}
```

### Explanation
この変更は、「Azure Data Lake Storage Gen2 インデクサー設定」に関する記事のマイナーな更新を反映しています。主な修正内容として、以下の点が挙げられます。

1. 記事の説明文が、「フルテキスト検索のためにコンテンツとメタデータを自動的にインデックス化する Azure Data Lake Storage (ADLS) Gen2 インデクサーを設定します。」から、「フルテキスト検索のためにコンテンツとメタデータを自動的にインデックス化する Azure Data Lake Storage (ADLS) Gen2 インデクサーを設定します。」に変更されています。具体的には、「full text search」が「full-text search」に修正され、間隔が適切に設定されています。

2. 記事の日付が「08/08/2026」から「08/31/2026」に更新され、内容の最新性が確保されています。

3. インデクサーが接続する際の接続文字列部分において、少なからず文言の修正が行われています。「Storage account shared access signature** (SAS) connection string」という表記から、余分なアスタリスクが削除され、「Storage account shared access signature (SAS) connection string」となっています。

4. コードブロックの形式が「http」から「json」に変更され、より正確なフォーマットが提供されています。

これらの変更により、記事はより正確で、明確な情報を提供することを目指しており、開発者がAzure Data Lake Storage Gen2インデクサーを使用する際の理解を深化させることが期待されています。

## articles/search/search-how-to-index-azure-tables.md{#item-c8a1d1}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +1,10 @@
 ---
 title: Azure Table Indexer
-description: Set up a search indexer to index data stored in Azure Table Storage for vector and full text search in Azure AI Search.
+description: Set up a search indexer to index data stored in Azure Table Storage for vector and full-text search in Azure AI Search.
 ms.reviewer: magottei
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ms.custom:
@@ -57,7 +57,7 @@ Use these instructions to create a table in Azure Storage for testing purposes.
 
 You should have 50 hotel records in the table with an autogenerated partitionKey, rowKey, and timestamp. You can now use this content for indexing in the Azure portal, REST client, or an Azure SDK.
 
-The Description field provides the most verbose content. You should target this field for full text search and optional vector queries.
+The Description field provides the most verbose content. You should target this field for full-text search and optional vector queries.
 
 ## Use the Azure portal
 
@@ -73,7 +73,7 @@ You can use the **Import data** wizard to automate indexing from a SQL database
 
 1. Specify an authentication method, either a managed identity or built-in API key. If you don't specify a managed identity connection, the Azure portal uses the key.
 
-   If you [configure Azure AI Search to use a managed identity](search-how-to-managed-identities.md), and you create a role assignment on Azure Storage that grants **Reader and Data Access** permissions to the identity, your indexer can connect to table storage using Microsoft Entra ID and roles.
+   If you [configure Azure AI Search to use a managed identity](search-how-to-managed-identities.md), and create a role assignment on Azure Storage that grants the identity the **Storage Table Data Reader** role, your indexer can connect to table storage using Microsoft Entra ID.
 
 1. You can specify options for deletion detection.
 
@@ -138,7 +138,7 @@ Indexers can connect to a table using the following connections.
 |`{ "connectionString" : "ResourceId=/subscriptions/<your subscription ID>/resourceGroups/<your resource group name>/providers/Microsoft.Storage/storageAccounts/<your storage account name>/;" }`|
 |This connection string doesn't require an account key, but you must have previously configured a search service to [connect using a managed identity](search-how-to-managed-identities.md).|
 
-| Storage account shared access signature** (SAS) connection string |
+| Storage account shared access signature (SAS) connection string |
 |-------------------------------------------------------------------|
 | `{ "connectionString" : "BlobEndpoint=https://<your account>.blob.core.windows.net/;SharedAccessSignature=?sv=2016-05-31&sig=<the signature>&spr=https&se=<the validity end time>&srt=co&ss=b&sp=rl;" }` |
 | The SAS should have the list and read permissions on tables and entities. |
@@ -254,7 +254,7 @@ An indexer runs automatically when it's created. You can prevent this by setting
 
 ## Check indexer status
 
-To monitor the indexer status and execution history, check the indexer execution history in the Azure portal, or send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) REST APIrequest
+To monitor the indexer status and execution history, check the indexer execution history in the Azure portal, or send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) REST API request.
 
 ### [**Portal**](#tab/portal-check-indexer)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Table インデクサー設定の更新"
}
```

### Explanation
この変更は、「Azure Table インデクサー設定」に関する記事のマイナーな更新を反映しています。主な修正内容は以下の通りです。

1. 記事の説明文が、「フルテキスト検索のために Azure Table Storage に保存されたデータをインデックス化する検索インデクサーを設定します。」から「フルテキスト検索のために Azure Table Storage に保存されたデータをインデックス化する検索インデクサーを設定します。」に変更され、用語「full text search」が「full-text search」に修正されています。

2. 記事の日付も「07/21/2026」から「08/31/2026」に更新され、より最新の情報が提供されています。

3. 「Description」フィールドに関する文言が修正され、こちらも「full text search」が「full-text search」に変更されています。

4. インデクサーが接続する場合の接続文字列の説明において、「Storage account shared access signature** (SAS) connection string」という表記から、余分なアスタリスクが削除され、「Storage account shared access signature (SAS) connection string」となっています。

5. 「Get Indexer Status」REST API リクエストについても、文末に「request」のスペースが追加され、文がより明確になっています。

これらの変更によって、記事はより正確で、一貫した内容を提供し、読者にとってわかりやすくなっています。Azure Table Storageを使用する際の開発者が必要とする情報を強化したことが期待されます。

## articles/search/search-how-to-index-cosmosdb-gremlin.md{#item-e5e93d}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +1,10 @@
 ---
 title: Azure Cosmos DB Gremlin Indexer
-description: Set up an Azure Cosmos DB indexer to automate indexing of Apache Gremlin content for full text search in Azure AI Search. This article explains how index data using the Azure Cosmos DB for Apache Gremlin protocol.
+description: Set up an Azure Cosmos DB indexer to automate indexing of Apache Gremlin content for full-text search in Azure AI Search. This article explains how index data using the Azure Cosmos DB for Apache Gremlin protocol.
 ms.reviewer: magottei
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ms.custom:
@@ -73,7 +73,6 @@ For this call, specify a preview REST API version to create a data source that c
       "encryptionKey": null,
       "identity": null
     }
-    }
    ```
 
 1. Set "type" to `"cosmosdb"` (required).
@@ -96,7 +95,7 @@ Avoid port numbers in the endpoint URL. If you include the port number, the conn
 
 | Full access connection string |
 |-----------------------------------------------|
-|`{ "connectionString" : "AccountEndpoint=https://<Cosmos DB account name>.documents.azure.com;AccountKey=<Cosmos DB auth key>;Database=<Cosmos DB database id>;ApiKind=MongoDb" }` |
+|`{ "connectionString" : "AccountEndpoint=https://<Cosmos DB account name>.documents.azure.com;AccountKey=<Cosmos DB auth key>;Database=<Cosmos DB database id>;ApiKind=Gremlin" }` |
 | You can get the connection string from the Azure Cosmos DB account page in Azure portal by selecting **Keys** in the left pane. Make sure to select a full connection string and not just a key.  |
 
 | Managed identity connection string |
@@ -131,7 +130,6 @@ In a [search index](search-what-is-an-index.md), add fields to accept the source
             "searchAnalyzer": null,
             "synonymMaps": [],
             "fields": []
-        },{
         }, {
             "name": "label",
             "type": "Edm.String",
@@ -258,10 +256,10 @@ For Azure Cosmos DB indexers, the only supported policy is the [`HighWaterMarkCh
 
 The following example shows a [data source definition](#define-the-data-source) with a change detection policy:
 
-```http
+```json
 "dataChangeDetectionPolicy": {
     "@odata.type": "#Microsoft.Azure.Search.HighWaterMarkChangeDetectionPolicy",
-"  highWaterMarkColumnName": "_ts"
+    "highWaterMarkColumnName": "_ts"
 },
 ```
 
@@ -271,8 +269,8 @@ The following example shows a [data source definition](#define-the-data-source)
 
 When graph data is deleted, you might want to delete its corresponding document from the search index as well. The purpose of a data deletion detection policy is to efficiently identify deleted data items and delete the full document from the index. The data deletion detection policy isn't meant to delete partial document information. Currently, the only supported policy is the `Soft Delete` policy (deletion is marked with a flag of some sort), which is specified in the data source definition as follows:
 
-```http
-"dataDeletionDetectionPolicy"": {
+```json
+"dataDeletionDetectionPolicy": {
     "@odata.type" : "#Microsoft.Azure.Search.SoftDeleteColumnDeletionDetectionPolicy",
     "softDeleteColumnName" : "the property that specifies whether a document was deleted",
     "softDeleteMarkerValue" : "the value that identifies a document as deleted"
@@ -314,13 +312,13 @@ Even if you enable deletion detection policy, deleting complex (`Edm.ComplexType
 
 The Azure Cosmos DB for Apache Gremlin indexer automatically maps a couple pieces of graph data:
 
-1. The indexer maps `_rid` to an `rid` field in the index if it exists, and Base64 encodes it.
+1. The indexer maps `_rid` to a `rid` field in the index if it exists, and Base64 encodes it.
 
 1. The indexer maps `_id` to an `id` field in the index if it exists.
 
 1. When querying your Azure Cosmos DB database by using the Azure Cosmos DB for Apache Gremlin, you might notice that the JSON output for each property has an `id` and a `value`. The indexer automatically maps the property's `value` into a field in your search index that has the same name as the property if it exists. In the following example, 450 is mapped to a `pages` field in the search index.
 
-```http
+```json
     {
         "id": "Cookbook",
         "label": "book",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Cosmos DB Gremlin インデクサー設定の更新"
}
```

### Explanation
この変更は、「Azure Cosmos DB Gremlin インデクサー設定」に関する記事のマイナーな更新を反映しています。主な修正内容として、以下の点が挙げられます。

1. 記事の説明文が、「Apache Gremlin コンテンツのフルテキスト検索を自動化する Azure Cosmos DB インデクサーを設定します。この文書では、Azure Cosmos DB for Apache Gremlin プロトコルを使用してデータをインデックス化する方法について説明します。」から、「Apache Gremlin コンテンツのフルテキスト検索を自動化する Azure Cosmos DB インデクサーを設定します。この文書では、Azure Cosmos DB for Apache Gremlin プロトコルを使用してデータをインデックス化する方法について説明します。」に変更されており、「full text search」が「full-text search」に修正されています。

2. 記事の日付が「07/21/2026」から「08/31/2026」に更新されています。

3. 接続文字列の詳細部分で、「AccountEndpoint」の下にある「ApiKind」が「MongoDb」から「Gremlin」に変更され、Cosmos DB Gremlin に対応する内容が明確となっています。

4. いくつかのコードブロックが「http」フォーマットから「json」フォーマットに変更され、より正確な表記がなされています。

5. データ変更検出ポリシーやデータ削除検出ポリシーに関する例にも、同様にフォーマットの変更がされており、文書全体の一貫性と明確性が向上しています。

これらの更新により、記事はより明確で、技術的な正確性が向上しており、開発者が Azure Cosmos DB Gremlin を使用する際のガイダンスを強化しています。読者に対して、インデクサーを使ったデータ管理が円滑に行えることを目的としています。

## articles/search/search-how-to-index-cosmosdb-mongodb.md{#item-b5aa9f}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +1,10 @@
 ---
 title: Indexing with Azure Cosmos DB for MongoDB
-description: Set up a search indexer to index data stored in Azure Cosmos DB for full text search in Azure AI Search. This article explains how index data in Azure Cosmos DB for MongoDB.
+description: Set up a search indexer to index data stored in Azure Cosmos DB for full-text search in Azure AI Search. This article explains how index data in Azure Cosmos DB for MongoDB.
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ms.custom:
@@ -74,8 +74,7 @@ For this call, specify a preview REST API version to create a data source that c
         "connectionString": "AccountEndpoint=https://[cosmos-account-name].documents.azure.com;AccountKey=[cosmos-account-key];Database=[cosmos-database-name];ApiKind=MongoDb;"
       },
       "container": {
-        "name": "[cosmos-db-collection]",
-        "query": null
+        "name": "[cosmos-db-collection]"
       },
       "dataChangeDetectionPolicy": {
         "@odata.type": "#Microsoft.Azure.Search.HighWaterMarkChangeDetectionPolicy",
@@ -261,10 +260,10 @@ For Azure Cosmos DB indexers, the only supported policy is the [`HighWaterMarkCh
 
 The following example shows a [data source definition](#define-the-data-source) with a change detection policy:
 
-```http
+```json
 "dataChangeDetectionPolicy": {
     "@odata.type": "#Microsoft.Azure.Search.HighWaterMarkChangeDetectionPolicy",
-"  highWaterMarkColumnName": "_ts"
+    "highWaterMarkColumnName": "_ts"
 },
 ```
 
@@ -274,8 +273,8 @@ The following example shows a [data source definition](#define-the-data-source)
 
 When rows are deleted from the collection, you normally want to delete those rows from the search index as well. The purpose of a data deletion detection policy is to efficiently identify deleted data items. Currently, the only supported policy is the `Soft Delete` policy (deletion is marked with a flag of some sort), which is specified in the data source definition as follows:
 
-```http
-"dataDeletionDetectionPolicy"": {
+```json
+"dataDeletionDetectionPolicy": {
     "@odata.type" : "#Microsoft.Azure.Search.SoftDeleteColumnDeletionDetectionPolicy",
     "softDeleteColumnName" : "the property that specifies whether a document was deleted",
     "softDeleteMarkerValue" : "the value that identifies a document as deleted"
@@ -292,10 +291,10 @@ Content-Type: application/json
 api-key: [Search service admin key]
 
 {
-    "name": ["my-cosmosdb-mongodb-ds]",
+    "name": "my-cosmosdb-mongodb-ds",
     "type": "cosmosdb",
     "credentials": {
-        "connectionString": "AccountEndpoint=https://[cosmos-account-name].documents.azure.com;AccountKey=[cosmos-account-key];Database=[cosmos-database-name];ApiKind=MongoDB"
+        "connectionString": "AccountEndpoint=https://[cosmos-account-name].documents.azure.com;AccountKey=[cosmos-account-key];Database=[cosmos-database-name];ApiKind=MongoDb"
     },
     "container": { "name": "[my-cosmos-collection]" },
     "dataChangeDetectionPolicy": {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Cosmos DB for MongoDB インデクサー設定の更新"
}
```

### Explanation
この変更は、「Azure Cosmos DB for MongoDB インデクサー設定」に関する記事のマイナーな更新を反映しています。主な修正内容は以下の通りです。

1. 記事の説明文が、「フルテキスト検索を実施するために Azure Cosmos DB に保存されたデータをインデックス化する検索インデクサーを設定します。この文書では、Azure Cosmos DB for MongoDB におけるデータのインデックス化方法を説明します。」から「フルテキスト検索を実施するために Azure Cosmos DB に保存されたデータをインデックス化する検索インデクサーを設定します。この文書では、Azure Cosmos DB for MongoDB におけるデータのインデックス化方法を説明します。」に変更されており、「full text search」が「full-text search」に修正されています。

2. 記事の日付が「07/21/2026」から「08/31/2026」に更新されています。

3. データソース定義において、コレクション名の行から「query: null」が削除され、簡素化されています。

4. データ変更検出ポリシーやデータ削除検出ポリシーに関するコードブロックが、「http」フォーマットから「json」フォーマットに変更され、内容の整合性が維持されています。また、削除検出ポリシーの背景説明も正確に更新されています。

5. 一部のコード行において、配列の指定方法が修正され、より適切な形式の表記が強調されています（例えば、データソース名が配列から単一の文字列に変更されています）。

これらの変更により、記事は技術的な正確性と明瞭さが向上しており、Azure Cosmos DB for MongoDB を使用する際のより良いガイドとして機能することが期待されます。読者は、インデクサーの設定方法を理解しやすくなっています。

## articles/search/search-how-to-index-cosmosdb-sql.md{#item-2e888b}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +1,10 @@
 ---
 title: Azure Cosmos DB NoSQL Indexer
-description: Set up a search indexer to index data stored in Azure Cosmos DB for vector and full text search in Azure AI Search. This article explains how index data using the NoSQL API protocol.
+description: Set up a search indexer to index data stored in Azure Cosmos DB for vector and full-text search in Azure AI Search. This article explains how index data using the NoSQL API protocol.
 ms.reviewer: magottei
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ms.custom:
@@ -48,7 +48,7 @@ Use these instructions to create a container and database in Cosmos DB for testi
 
 1. Sign in to the Azure portal and [create an account, database, and container](/azure/cosmos-db/nosql/quickstart-portal) on Cosmos DB. 
 
-1. In Cosmos DB, select **Data Explorer**  for the new container, provide the following values.
+1. In Cosmos DB, select **Data Explorer** and, for the new container, provide the following values.
 
     | Property | Value |
     |----------|-------|
@@ -70,7 +70,7 @@ Use these instructions to create a container and database in Cosmos DB for testi
 
 Now that you have a container, you can use the Azure portal, REST client, or an Azure SDK to index your data.
 
-The Description field provides the most verbose content. You should target this field for full text search and optional vector queries.
+The Description field provides the most verbose content. You should target this field for full-text search and optional vector queries.
 
 ## Use the Azure portal
 
@@ -124,7 +124,7 @@ The data source definition specifies the data to index, credentials, and policie
         },
         "dataChangeDetectionPolicy": {
           "@odata.type": "#Microsoft.Azure.Search.HighWaterMarkChangeDetectionPolicy",
-        "  highWaterMarkColumnName": "_ts"
+          "highWaterMarkColumnName": "_ts"
         },
         "dataDeletionDetectionPolicy": null,
         "encryptionKey": null,
@@ -173,7 +173,7 @@ In the "query" property under "container", you can specify a SQL query to flatte
 
 Example document:
 
-```http
+```json
     {
         "userId": 10001,
         "contact": {
@@ -316,7 +316,7 @@ An indexer runs automatically when it's created. You can prevent this by setting
 
 ## Check indexer status
 
-To monitor the indexer status and execution history, check the indexer execution history in the Azure portal, or send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) REST APIrequest
+To monitor the indexer status and execution history, check the indexer execution history in the Azure portal, or send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) REST API request.
 
 ### [**Portal**](#tab/portal-check-indexer)
 
@@ -383,10 +383,10 @@ For Azure Cosmos DB indexers, the only supported policy is the [`HighWaterMarkCh
 
 The following example shows a [data source definition](#define-the-data-source) with a change detection policy:
 
-```http
+```json
 "dataChangeDetectionPolicy": {
     "@odata.type": "#Microsoft.Azure.Search.HighWaterMarkChangeDetectionPolicy",
-"  highWaterMarkColumnName": "_ts"
+    "highWaterMarkColumnName": "_ts"
 },
 ```
 
@@ -417,8 +417,8 @@ To specify this hint, [create or update your indexer definition](#configure-and-
 
 When rows are deleted from the collection, you normally want to delete those rows from the search index as well. The purpose of a data deletion detection policy is to efficiently identify deleted data items. Currently, the only supported policy is the `Soft Delete` policy (deletion is marked with a flag of some sort), which is specified in the data source definition as follows:
 
-```http
-"dataDeletionDetectionPolicy"": {
+```json
+"dataDeletionDetectionPolicy": {
     "@odata.type" : "#Microsoft.Azure.Search.SoftDeleteColumnDeletionDetectionPolicy",
     "softDeleteColumnName" : "the property that specifies whether a document was deleted",
     "softDeleteMarkerValue" : "the value that identifies a document as deleted"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Cosmos DB NoSQL インデクサー設定の更新"
}
```

### Explanation
この変更は、「Azure Cosmos DB NoSQL インデクサー設定」に関する記事のマイナーな更新を反映しています。主な修正内容は以下のとおりです。

1. 記事の説明文が、「フルテキスト検索およびベクトル検索を実施するために Azure Cosmos DB に保存されたデータをインデックス化する検索インデクサーを設定します。この文書では、NoSQL API プロトコルを使用してデータをインデックス化する方法を説明します。」から「フルテキスト検索およびベクトル検索を実施するために Azure Cosmos DB に保存されたデータをインデックス化する検索インデクサーを設定します。この文書では、NoSQL API プロトコルを使用してデータをインデックス化する方法を説明します。」に変更されており、「full text search」が「full-text search」に修正されています。

2. 記事の日付が「07/21/2026」から「08/31/2026」に更新されています。

3. コンテナの作成手順において、手順の文が「**Data Explorer** の新しいコンテナを選択し、次の値を提供します。」から「**Data Explorer** を選択し、新しいコンテナに対して次の値を提供します。」に修正され、文の流れが改善されています。

4. データソース定義の一部コンテンツが修正され、「高水準マーク列名」の定義や、データ削除検出ポリシーの指定に関する説明がより整然とした形式に変更され、コードブロックが「http」から「json」に変わり、より一貫性のあるフォーマットが採用されています。

5. インデクサーの状態をモニタリングする手順説明の一部が整えられ、文法の誤りが修正されました。特に、APIリクエストに関する文において、誤っていたスペースが削除されています。

これらの変更により、記事は技術的な正確性の向上と明瞭さが強化され、Azure Cosmos DB NoSQL インデクサーを使用する際のガイダンスがより効果的になります。読者は、インデクサーの設定と管理について理解しやすくなります。

## articles/search/search-how-to-index-sql-database.md{#item-86d873}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +1,9 @@
 ---
 title: Azure SQL Indexer
-description: Set up a search indexer to index tables in Azure SQL Database for vector and full text search in Azure AI Search.
+description: Set up a search indexer to index tables in Azure SQL Database for vector and full-text search in Azure AI Search.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 180-days
 ai-usage: ai-assisted
 ms.custom:
@@ -69,7 +69,7 @@ Use these instructions to create and load a table in Azure SQL Database for test
    CREATE TABLE tbl_hotels
     (
         Id TINYINT PRIMARY KEY NONCLUSTERED,
-        Modified DateTime NULL DEFAULT '0000-00-00 00:00:00',
+        Modified DateTime NULL DEFAULT CURRENT_TIMESTAMP,
         IsDeleted TINYINT,
         HotelName VARCHAR(40),
         Category VARCHAR(20),
@@ -108,7 +108,7 @@ Use these instructions to create and load a table in Azure SQL Database for test
 
    :::image type="content" source="media/search-how-to-index-sql-database/tsql-query-results.png" alt-text="Screenshot of query results showing the description field.":::
 
-The Description field provides the most verbose content. You should target this field for full text search and optional vectorization.
+The Description field provides the most verbose content. You should target this field for full-text search and optional vectorization.
 
 Now that you have a database table, you can use the Azure portal, REST client, or an Azure SDK to index your data.
 
@@ -174,10 +174,9 @@ The data source definition specifies the data to index, credentials, and policie
         "description" : "A database for testing Azure AI Search indexes.",
         "type" : "azuresql",
         "credentials" : { "connectionString" : "Server=tcp:<your server>.database.windows.net,1433;Database=<your database>;User ID=<your user name>;Password=<your password>;Trusted_Connection=False;Encrypt=True;Connection Timeout=30;" },
-        "container" : { 
-            "name" : "name of the table or view that you want to index",
-            "query" : null (not supported in the Azure SQL indexer)
-            },
+        "container" : {
+            "name" : "name of the table or view that you want to index"
+        },
         "dataChangeDetectionPolicy": null,
         "dataDeletionDetectionPolicy": null,
         "encryptionKey": null,
@@ -187,7 +186,7 @@ The data source definition specifies the data to index, credentials, and policie
 
 1. Provide a unique name for the data source that follows Azure AI Search [naming conventions](/rest/api/searchservice/naming-rules).
 
-1. Set "type" to `"azuresql"` (required).
+1. Set `type` to `"azuresql"` (required) and set `container.name` to the table or view that you want to index. Azure SQL indexers don't support `container.query`.
 
 1. Set "credentials" to a connection string:
 
@@ -410,7 +409,7 @@ When using SQL integrated change tracking policy, don't specify a separate data
 
 ### High water mark change detection policy
 
-This change detection policy relies on a "high water mark" column in your table or view that captures the version or time when a row was last updated. If you're using a view, you must use a high water mark policy. 
+This change detection policy relies on a "high water mark" column in your table or view that captures the version or time when a row was last updated. If you're using a view, you must use a high water mark policy.
 
 The high water mark column must meet the following requirements:
 
@@ -445,50 +444,58 @@ api-key: admin-key
 
 <a name="convertHighWaterMarkToRowVersion"></a>
 
-##### convertHighWaterMarkToRowVersion
+#### convertHighWaterMarkToRowVersion
 
-If you're using a [rowversion](/sql/t-sql/data-types/rowversion-transact-sql) data type for the high water mark column, consider setting the `convertHighWaterMarkToRowVersion` property in indexer configuration. Setting this property to true results in the following behaviors: 
+If you're using a [rowversion](/sql/t-sql/data-types/rowversion-transact-sql) data type for the high water mark column, consider setting the `convertHighWaterMarkToRowVersion` property in indexer configuration. Setting this property to true results in the following behaviors:
 
 + Uses the rowversion data type for the high water mark column in the indexer SQL query. Using the correct data type improves indexer query performance.
 
 + Subtracts one from the rowversion value before the indexer query runs. Views with one-to-many joins might have rows with duplicate rowversion values. Subtracting one ensures the indexer query doesn't miss these rows.
 
-To enable this property, create or update the indexer with the following configuration:
+To enable this property, add the following `parameters` property when you create or update the indexer:
 
-```http
-    {
-      ... other indexer definition properties
-     "parameters" : {
-            "configuration" : { "convertHighWaterMarkToRowVersion" : true } }
+```json
+{
+    "parameters": {
+        "configuration": {
+            "convertHighWaterMarkToRowVersion": true
+        }
     }
+}
 ```
 
 <a name="queryTimeout"></a>
 
-##### queryTimeout
+#### queryTimeout
 
-If you encounter timeout errors, set the `queryTimeout` indexer configuration setting to a value higher than the default 5-minute timeout. For example, to set the timeout to 10 minutes, create or update the indexer with the following configuration:
+If you encounter timeout errors, set the `queryTimeout` indexer configuration setting to a value higher than the default 5-minute timeout. For example, to set the timeout to 10 minutes, add the following `parameters` property when you create or update the indexer:
 
-```http
-    {
-      ... other indexer definition properties
-     "parameters" : {
-            "configuration" : { "queryTimeout" : "00:10:00" } }
+```json
+{
+    "parameters": {
+        "configuration": {
+            "queryTimeout": "00:10:00"
+        }
     }
+}
 ```
 
 <a name="disableOrderByHighWaterMarkColumn"></a>
 
-##### disableOrderByHighWaterMarkColumn
+#### disableOrderByHighWaterMarkColumn
 
-You can also disable the `ORDER BY [High Water Mark Column]` clause. However, this isn't recommended because if the indexer execution is interrupted by an error, the indexer has to reprocess all rows if it runs later, even if the indexer has already processed almost all the rows at the time it was interrupted. To disable the `ORDER BY` clause, use the `disableOrderByHighWaterMarkColumn` setting in the indexer definition:  
+You can also disable the `ORDER BY [High Water Mark Column]` clause. However, this action isn't recommended because if the indexer execution is interrupted by an error, the indexer has to reprocess all rows if it runs later, even if the indexer already processed almost all the rows at the time it was interrupted.
 
-```http
-    {
-     ... other indexer definition properties
-     "parameters" : {
-            "configuration" : { "disableOrderByHighWaterMarkColumn" : true } }
+To disable the `ORDER BY` clause, add the following `parameters` property when you create or update the indexer:
+
+```json
+{
+    "parameters": {
+        "configuration": {
+            "disableOrderByHighWaterMarkColumn": true
+        }
     }
+}
 ```
 
 ### Soft delete column deletion detection policy
@@ -497,17 +504,16 @@ When rows are deleted from the source table, you probably want to delete those r
 
 If the rows are physically removed from the table, Azure AI Search has no way to infer the presence of records that no longer exist. However, you can use the “soft-delete” technique to logically delete rows without removing them from the table. Add a column to your table or view and mark rows as deleted using that column.
 
-When using the soft-delete technique, you can specify the soft delete policy as follows when creating or updating the data source:
+When you use the soft-delete technique, add the following `dataDeletionDetectionPolicy` property when you create or update the data source:
 
-```http
-    {
-        …,
-        "dataDeletionDetectionPolicy" : {
-           "@odata.type" : "#Microsoft.Azure.Search.SoftDeleteColumnDeletionDetectionPolicy",
-           "softDeleteColumnName" : "[a column name]",
-           "softDeleteMarkerValue" : "[the value that indicates that a row is deleted]"
-        }
+```json
+{
+    "dataDeletionDetectionPolicy": {
+        "@odata.type": "#Microsoft.Azure.Search.SoftDeleteColumnDeletionDetectionPolicy",
+        "softDeleteColumnName": "[a column name]",
+        "softDeleteMarkerValue": "[the value that indicates that a row is deleted]"
     }
+}
 ```
 
 The **softDeleteMarkerValue** must be a string in the JSON representation of your data source. Use the string representation of your actual value. For example, if you have an integer column where deleted rows are marked with the value 1, use `"1"`. If you have a BIT column where deleted rows are marked with the Boolean true value, use the string literal `"True"` or `"true"`, the case doesn't matter.
@@ -534,7 +540,7 @@ It depends. For full indexing of a table or view, you can use a secondary replic
 
 For incremental indexing, Azure AI Search supports two change detection policies: SQL integrated change tracking and High Water Mark.
 
-On read-only replicas, SQL Database doesn't support integrated change tracking. Therefore, you must use High Water Mark policy. 
+On read-only replicas, SQL Database doesn't support integrated change tracking. Therefore, you must use the High Water Mark policy.
 
 Our standard recommendation is to use the rowversion data type for the high water mark column. However, using rowversion relies on the `MIN_ACTIVE_ROWVERSION` function, which isn't supported on read-only replicas. Therefore, you must point the indexer to a primary replica if you're using rowversion.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure SQL インデクサー設定の更新"
}
```

### Explanation
この変更は、「Azure SQL インデクサー設定」に関する記事のマイナーな更新を反映しています。主な修正内容は以下の通りです。

1. 記事の説明文が、「フルテキスト検索およびベクトル検索を実施するために Azure SQL Database のテーブルをインデックス化する検索インデクサーを設定します。」から「フルテキスト検索およびベクトル検索を実施するために Azure SQL Database のテーブルをインデックス化する検索インデクサーを設定します。」に変更されており、「full text search」が「full-text search」に修正されています。

2. 記事の日付が「07/21/2026」から「08/31/2026」に更新されています。

3. データベーステーブルの作成手順において、`Modified`列のデフォルト値が`'0000-00-00 00:00:00'`から`CURRENT_TIMESTAMP`に変更され、より適切なデフォルト値が設定されています。

4. コンテナのデータソース定義での`query`フィールドが削除され、明確にインデクサーではサポートされていないことを示しています。

5. データ削除検出ポリシーや高水準マークポリシーに関する情報が更新され、関連する設定をJSON形式で記載するように改善されています。これにより、ユーザーはより直感的に設定内容を理解しやすくなっています。

6. ソフト削除ポリシーに関するセクションがより明確に記載され、`dataDeletionDetectionPolicy`のプロパティがJSON形式で示され、その利用方法も具体的に説明されています。

全体的に、これらの変更により、記事は技術的な明瞭さと正確性が向上しており、Azure SQL Database におけるインデクサーの設定方法について読者が理解しやすくなっています。

## articles/search/search-howto-managed-identities-azure-functions.md{#item-2f13c4}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how to set up an indexer connection to an Azure Function usin
 ms.reviewer: arjagann
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 180-days
 ai-usage: ai-assisted
 ms.custom:
@@ -105,7 +105,7 @@ Depending on whether you choose to connect using a system-assigned identity or u
 
 ### Use a system-assigned identity
 
-Here's an example to call into a function named `test` for the sample Azure Function app, where the system assigned identity of the search service is allowed to authenticate via "Easy Auth".
+Here's an example to call a function named `test` for the sample Azure Function app, where the system-assigned identity of the search service is allowed to authenticate via "Easy Auth".
 
 ```json
 "uri": "https://contoso-function-app.azurewebsites.net/api/test?",
@@ -114,7 +114,7 @@ Here's an example to call into a function named `test` for the sample Azure Func
 
 ### Use a user-assigned identity
 
-Here's an example to call into the same function, where the specific user assigned identity is allowed to authenticate via "Easy Auth". You're expected to specify the resource ID of the exact user assigned identity to use in the `identity` property of the configuration.
+Here's an example to call into the same function, where the specific user-assigned identity is allowed to authenticate via "Easy Auth". You need to specify the resource ID of the exact user-assigned identity to use in the `identity` property of the configuration.
 
 ```json
 "uri": "https://contoso-function-app.azurewebsites.net/api/test?",
@@ -126,7 +126,7 @@ Here's an example to call into the same function, where the specific user assign
 ```
 
 >[!NOTE]
-> This user assigned identity should actually be assigned to the Azure AI Search service for it to be specified in the Custom Web skill/vectorizer definition.
+> Before you specify a user-assigned identity in a Custom Web API skill or vectorizer definition, assign the identity to the Azure AI Search service.
 
 ## Run the indexer/vectorizer to verify permissions
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Functions におけるマネージド ID の設定方法の更新"
}
```

### Explanation
この変更は、「Azure Functions におけるマネージド ID の設定方法」に関する記事のマイナーな更新を反映しています。主な修正内容は以下の通りです。

1. 記事の日付が「07/21/2026」から「08/31/2026」に更新され、コンテンツが最新の情報を反映しています。

2. システム割り当て ID を使用した認証に関する説明文が、呼び方が適切になるように修正され、「call into a function named `test`」から「call a function named `test`」に変更されています。この変更は文の簡潔さを向上させています。

3. ユーザー割り当て ID を使用した認証に関する説明文で、「You're expected to specify」が「You need to specify」に変更され、表現がより明確で直接的に修正されています。

4. 重要な注意事項部分において、ユーザー割り当て ID を指定する際の注意点が「This user assigned identity should actually be assigned to the Azure AI Search service」から「Before you specify a user-assigned identity in a Custom Web API skill or vectorizer definition, assign the identity to the Azure AI Search service.」に変更され、文の構成が整理され、より明確な指示が与えられています。

これらの変更により、記事は技術的な細部が改善され、読者はマネージド ID の設定方法に関してより理解しやすくなります。これにより、Azure AI Search サービスと Azure Functions の連携がスムーズに行えるよう支援されます。

## articles/search/search-index-access-control-lists-and-rbac-push-api.md{#item-45e71e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how to use the REST API for indexing documents with ACLs and
 ms.reviewer: admayber
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ai-usage: ai-assisted
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスのアクセス制御リストと RBAC に関する更新"
}
```

### Explanation
この変更は、「インデックスのアクセス制御リストと RBAC に関する API の使用方法」に関する記事のマイナーな更新を反映しています。主な修正内容は以下の通りです。

1. 記事の日付が「07/21/2026」から「08/31/2026」に更新され、最新の情報を提供しています。

この変更は、ドキュメントの適切なバージョン管理を促進し、Azure AI Search に関する最新の利用情報を反映させるための重要な修正です。他に大きな内容の追加や削除はありませんが、日付更新により読者は情報が最新であることを確認できます。このように、技術ドキュメントにおける日付の更新は、信頼性と正確性を保つために重要です。

## articles/search/search-indexer-securing-resources.md{#item-c075c4}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソース保護に関するインデクサーの更新"
}
```

### Explanation
この変更は、「リソースを保護するためのインデクサー」に関する記事のマイナーな更新を反映しています。主な修正内容は以下の通りです。

1. 記事の日付が「07/21/2026」から「08/31/2026」に変更され、より最新の情報を提供しています。

この更新により、記事はテクニカルドキュメントとしての信頼性を高め、ユーザーはコンテンツが最新のものであることを確認できます。具体的な内容の追加や削除は行われていませんが、日付の修正は重要なバージョン管理の一環として機能します。このように、ドキュメントの日付更新は、特に技術情報において重要です。

## articles/search/search-language-support.md{#item-a7979b}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ---
@@ -22,7 +22,7 @@ In Azure AI Search, the two patterns for supporting multiple languages include:
 
 + Create language-specific indexes where all of the human readable content is in the same language, and all searchable string fields are attributed to use the same [language analyzer](index-add-language-analyzers.md).
 
-+ Create a blended index with language-specific versions of each field (for example, description_en, description_fr, description_ko), and then constrain full text search to just those fields at query time. This approach is useful for scenarios where language variants are only needed on a few fields, like a description.
++ Create a blended index with language-specific versions of each field (for example, description_en, description_fr, description_ko), and then constrain full-text search to just those fields at query time. This approach is useful for scenarios where language variants are only needed on a few fields, like a description.
 
 This article focuses on steps and best practices for configuring and querying language-specific fields in a blended index:
 
@@ -98,7 +98,7 @@ Parameters on the query are used to limit search to specific fields and then tri
 
 | Parameters | Purpose |
 |-----------|--------------|
-| `searchFields` | Limits full text search to the list of named fields. |
+| `searchFields` | Limits full-text search to the list of named fields. |
 | `select` | Trims the response to include only the fields you specify. By default, all retrievable fields are returned. The `select` parameter lets you choose which ones to return. |
 
 Given a goal of constraining search to fields containing French strings, you would use `searchFields` to target the query at fields containing strings in that language.
@@ -107,19 +107,19 @@ Specifying the analyzer on a query request isn't necessary. A language analyzer
 
 By default, a search returns all fields that are marked as retrievable. As such, you might want to exclude fields that don't conform to the language-specific search experience you want to provide. Specifically, if you limited search to a field with French strings, you probably want to exclude fields with English strings from your results. Using the `select` query parameter gives you control over which fields are returned to the calling application.
 
-#### Example in REST
+### Example in REST
 
 ```http
 POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2026-04-01
 {
     "search": "animaux acceptés",
     "searchFields": "Tags, Description_fr",
     "select": "HotelName, Description_fr, Address/City, Address/StateProvince, Tags",
-    "count": "true"
+    "count": true
 }
 ```
 
-#### Example in C#
+### Example in C#
 
 ```csharp
 private static void RunQueries(SearchClient srchclient)
@@ -169,14 +169,14 @@ POST /indexes/hotels/docs/search?api-version=2026-04-01
   "searchFields": "Tags, Description_fr",
   "select": "HotelName, Tags, Description_fr",
   "scoringProfile": "frenchFirst",
-  "count": "true"
+  "count": true
 }
 ```
 
 ## Next steps
 
 + [Add a language analyzer](index-add-language-analyzers.md)
-+ [How full text search works in Azure AI Search](search-lucene-query-architecture.md)
++ [How full-text search works in Azure AI Search](search-lucene-query-architecture.md)
 + [Search Documents REST API](/rest/api/searchservice/documents/search-post)
 + [AI enrichment overview](cognitive-search-concept-intro.md)
 + [Skillsets overview](cognitive-search-working-with-skillsets.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サポートに関するドキュメントの更新"
}
```

### Explanation
この変更は、「Azure AI Search における言語サポート」に関する記事のマイナーな更新を表しています。主な修正内容は以下の通りです。

1. 記事の日付が「07/21/2026」から「08/31/2026」に変更され、最新の情報を反映しています。
2. いくつかの文の表現が改善され、より明確な説明が行われています。例えば、`full-text search` や `blended index` に関連する表現が一貫性を持つように修正されています。
3. コードの例において、一部のパラメータ（例えば `count`）のフォーマットが適切に修正され、正しいJSON形式になっています。
4. いくつかの見出しが簡潔に変更され、読みやすさが向上しています。

この更新により、ドキュメントの正確性と明瞭さが増し、ユーザーに最新の実装ガイドラインを提供することができます。特に技術文書では、正確な情報の伝達が重要であり、このようなマイナー更新が全体の品質向上に寄与します。

## articles/search/search-pagination-page-layout.md{#item-115902}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ---
@@ -14,7 +14,7 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-This article explains search results composition and how to shape full text search results to fit your scenarios. Search results are returned in a query response. The shape of a response is determined by parameters in the query itself. These parameters include:
+This article explains search results composition and how to shape full-text search results to fit your scenarios. Search results are returned in a query response. The shape of a response is determined by parameters in the query itself. These parameters include:
 
 + Number of matches found in the index (`count`)
 + Number of matches returned in the response (50 by default, configurable through `top`) or per page (`skip` and `top`)
@@ -87,7 +87,7 @@ The default page size is 50, while the maximum page size is 1,000. If you specif
 "@odata.nextLink": "https://contoso-search-eastus.search.windows.net/indexes/hotels-sample/docs/search?api-version=2026-04-01"
 ```
 
-The top matches are determined by search score, assuming the query is full text search or semantic. Otherwise, the top matches are an arbitrary order for exact match queries (where uniform `@search.score=1.0` indicates arbitrary ranking).
+The top matches are determined by search score, assuming the query is full-text search or semantic. Otherwise, the top matches are an arbitrary order for exact match queries (where uniform `@search.score=1.0` indicates arbitrary ranking).
 
 Set `top` to override the default of 50. In newer preview APIs, if you're using a hybrid query, you can [specify maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) to return up to 10,000 documents.
 
@@ -177,7 +177,7 @@ In this workaround, sort and filter are applied to a document ID field or anothe
           "search": "divine secrets",
           "top": 50,
           "orderby": "id asc",
-          "filter": "id ge 50"
+          "filter": "id gt 50"
         }
     ```
 
@@ -188,7 +188,7 @@ In this workaround, sort and filter are applied to a document ID field or anothe
 
 ## Ordering results
 
-In a full text search query, results can be ranked by:
+In a full-text search query, results can be ranked by:
 
 + a search score
 + a semantic reranker score
@@ -198,7 +198,7 @@ You can also boost any matches found in specific fields by adding a scoring prof
 
 ### Order by search score
 
-For full text search queries, results are automatically [ranked by a search score](index-similarity-and-scoring.md) using a BM25 algorithm, calculated based on term frequency, document length, and average document length.
+For full-text search queries, results are automatically [ranked by a search score](index-similarity-and-scoring.md) using the BM25 algorithm, which considers term frequency, document length, and average document length to determine relevance.
 
 The `@search.score` range is either unbounded, or 0 up to (but not including) 1.00 on older services. 
 
@@ -247,7 +247,7 @@ Hit highlighting instructions are provided on the [query request](/rest/api/sear
 
 To return highlighted terms, include the highlight parameter in the query request. The parameter is set to a comma-delimited list of fields. 
 
-By default, the format mark up is `<em>`, but you can override the tag using `highlightPreTag` and `highlightPostTag` parameters. Your client code handles the response (for example, applying a bold font or a yellow background).
+By default, the markup format is `<em>`, but you can override the tag by using the `highlightPreTag` and `highlightPostTag` parameters. Your client code handles the response (for example, by applying a bold font or a yellow background).
 
 ```http
 POST /indexes/good-books/docs/search?api-version=2026-04-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ページネーションおよび結果のレイアウトに関するドキュメントの更新"
}
```

### Explanation
この変更は、「検索のページネーションおよび結果のレイアウト」に関する記事のマイナーな更新を示しています。主な変更点は以下の通りです。

1. 記事の日付が「07/21/2026」から「08/31/2026」に変更され、最新の状態が反映されています。
2. 「full text search」という用語が「full-text search」に統一され、文書内の一貫性が向上しました。
3. 一部のフィールドに関する説明がより明瞭に書き直され、具体的にはフィルタの条件を示す文が明確になりました（例: `filter: "id gt 50"`）。
4. ハイライト機能の説明も若干修正があり、マークアップのデフォルト形式やクライアントコードに責任があることがより明確に説明されています。

これらの変更により、ドキュメントは読みやすく、理解しやすくなっており、ユーザーが検索結果のページネーションと表示整形に関する情報をより効果的に活用できるようになっています。特に、技術文書においては用語の一貫性と明瞭な説明が重要であり、この更新がそれを実現しています。

## articles/search/search-query-overview.md{#item-dcd5d6}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Query Types
 description: Learn about query types in Azure AI Search, including full-text, vector, hybrid, filter, autocomplete, and geospatial queries for building search experiences.
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ---
@@ -20,10 +20,10 @@ Azure AI Search supports query constructs for a broad range of scenarios, from f
 
 | Query form | Searchable content | Description |
 |------------|--------------------|-------------|
-| [Full text search](search-lucene-query-architecture.md) | Inverted indexes of tokenized terms. | Full text queries iterate over inverted indexes that are structured for fast scans, where a match can be found in potentially any field, within any number of search documents. Text is analyzed and tokenized for full text search.|
+| [Full-text search](search-lucene-query-architecture.md) | Inverted indexes of tokenized terms. | Full-text queries iterate over inverted indexes that are structured for fast scans, where a match can be found in potentially any field, within any number of search documents. Text is analyzed and tokenized for full-text search.|
 | [Vector search](vector-search-overview.md) | Vector indexes of generated embeddings. | Vector queries iterate over vector fields in a search index. |
-| [Hybrid search](hybrid-search-overview.md) | All of the above, in a single search index. | Combines text search and vector search in a single query request. Text search works on plain text content in "searchable" and "filterable" fields. Vector search works on content in vector fields. |
-| [Agentic retrieval (preview)](agentic-retrieval-overview.md) | All of the above, in a single search index. | This is an alternative retrieval path on Azure AI Search that leverages large language models for query planning. The response is designed for agent consumption, where the agent rather than search app client code coordinates the response delivered to the user. |
+| [Hybrid search](hybrid-search-overview.md) | All of the above in a single search index. | Combines text search and vector search in a single query request. Text search works on plain-text content in searchable fields. Filters apply to filterable fields. Vector search works on vector fields. |
+| [Agentic retrieval (preview)](agentic-retrieval-overview.md) | All of the above in a single search index. | This is an alternative retrieval path on Azure AI Search that leverages large language models for query planning. The response is designed for agent consumption, where the agent rather than search app client code coordinates the response delivered to the user. |
 | Others | Plain text and human-readable content.| Raw content, extracted verbatim from source documents, supporting filters and pattern matching queries like geo-spatial search, fuzzy search, and fielded search. |
 
 The remainder of this article brings focus to the last category: classic queries that work on plain text and human-readable content, extracted intact from original source, used for filters and other specialized query forms. If you're creating a traditional search application that isn't using AI, this section explains the query methods that you can implement in your client code.
@@ -40,7 +40,7 @@ You might also need filters to invoke a specialized query form, as described in
 
 | Filter scenario | Description |
 |-----------------|-------------|
-| Range filters | In Azure AI Search, range queries are built using the filter parameter. For more information and examples, see [Range filter example](search-query-simple-examples.md#example-5-range-filters). |
+| Range filters | In Azure AI Search, range queries are built using the `filter` parameter. For more information and examples, see [Range filter example](search-query-simple-examples.md#example-5-range-filters). |
 | Faceted navigation | In [faceted navigation](search-faceted-navigation.md) tree, users can select facets. When backed by filters, search results narrow on each click. Each facet is backed by a filter that excludes documents that no longer match the criteria provided by the facet. |
 
 > [!NOTE]
@@ -50,9 +50,9 @@ You might also need filters to invoke a specialized query form, as described in
 
 Geospatial search matches on a location's latitude and longitude coordinates for "find near me" or map-based search experience. In Azure AI Search, you can implement geospatial search by following these steps:
 
-+ Define a filterable field of one of these types: [Edm.GeographyPoint, Collection(Edm.GeographyPoint, Edm.GeographyPolygon)](/rest/api/searchservice/supported-data-types).
-+ Verify the incoming documents include the appropriate coordinates.
-+ After indexing is complete, build a query that uses a filter and a [geo-spatial function](search-query-odata-geo-spatial-functions.md). 
+1. Define a filterable field of type [Edm.GeographyPoint or Collection(Edm.GeographyPoint)](/rest/api/searchservice/supported-data-types).
+1. Verify the incoming documents include the appropriate coordinates.
+1. After indexing is complete, build a query that uses a filter and a [geo-spatial function](search-query-odata-geo-spatial-functions.md).
 
 Geospatial search uses kilometers for distance. Coordinates are specified in this format: `(longitude, latitude`).
 
@@ -83,16 +83,16 @@ An advanced query form depends on the Full Lucene parser and operators that trig
 | Query type | Usage | Examples and more information |
 |------------|--------|------------------------------|
 | [Fielded search](query-lucene-syntax.md#bkmk_fields) | **`search`**  parameter, **`queryType=full`**  | Build a composite query expression targeting a single field. <br/>[Fielded search example](search-query-lucene-examples.md#example-1-fielded-search) |
-| [fuzzy search](query-lucene-syntax.md#bkmk_fuzzy) | **`search`** parameter, **`queryType=full`** | Matches on terms having a similar construction or spelling. <br/>[Fuzzy search example](search-query-lucene-examples.md#example-2-fuzzy-search) |
-| [proximity search](query-lucene-syntax.md#bkmk_proximity) | **`search`** parameter, **`queryType=full`** | Finds terms that are near each other in a document. <br/>[Proximity search example](search-query-lucene-examples.md#example-3-proximity-search) |
-| [term boosting](query-lucene-syntax.md#bkmk_termboost) | **`search`** parameter, **`queryType=full`** | Ranks a document higher if it contains the boosted term, relative to others that don't. <br/>[Term boosting example](search-query-lucene-examples.md#example-4-term-boosting) |
-| [regular expression search](query-lucene-syntax.md#bkmk_regex) | **`search`** parameter, **`queryType=full`** | Matches based on the contents of a regular expression. <br/>[Regular expression example](search-query-lucene-examples.md#example-5-regex) |
-|  [wildcard or prefix search](query-lucene-syntax.md#bkmk_wildcard) | **`search`** parameter with ***`~`** or **`?`**, **`queryType=full`**| Matches based on a prefix and tilde (`~`) or single character (`?`). <br/>[Wildcard search example](search-query-lucene-examples.md#example-6-wildcard-search) |
+| [Fuzzy search](query-lucene-syntax.md#bkmk_fuzzy) | **`search`** parameter, **`queryType=full`** | Match terms with similar construction or spelling. <br/>[Fuzzy search example](search-query-lucene-examples.md#example-2-fuzzy-search) |
+| [Proximity search](query-lucene-syntax.md#bkmk_proximity) | **`search`** parameter, **`queryType=full`** | Find terms that are near each other in a document. <br/>[Proximity search example](search-query-lucene-examples.md#example-3-proximity-search) |
+| [Term boosting](query-lucene-syntax.md#bkmk_termboost) | **`search`** parameter, **`queryType=full`** | Rank a document higher if it contains the boosted term, relative to others that don't. <br/>[Term boosting example](search-query-lucene-examples.md#example-4-term-boosting) |
+| [Regular expression search](query-lucene-syntax.md#bkmk_regex) | **`search`** parameter, **`queryType=full`** | Match based on the contents of a regular expression. <br/>[Regular expression example](search-query-lucene-examples.md#example-5-regex) |
+| [Wildcard or prefix search](query-lucene-syntax.md#bkmk_wildcard) | **`search`** parameter with **`*`** or **`?`**, **`queryType=full`** | Match based on a prefix, multiple characters (`*`), or one character (`?`). <br/>[Wildcard search example](search-query-lucene-examples.md#example-6-wildcard-search) |
 
 ## Next steps
 
-For a closer look at query implementation, review the examples for each syntax. If you're new to full text search, a closer look at what the query engine does might be an equally good choice.
+For a closer look at query implementation, review the examples for each syntax. If you're new to full-text search, you might also want to learn more about what the query engine does.
 
 + [Simple query examples](search-query-simple-examples.md)
 + [Lucene syntax query examples for building advanced queries](search-query-lucene-examples.md)
-+ [How full text search works in Azure AI Search](search-lucene-query-architecture.md)
++ [How full-text search works in Azure AI Search](search-lucene-query-architecture.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索クエリ概要に関するドキュメントの更新"
}
```

### Explanation
この変更は、「検索クエリの概要」に関する記事のマイナーな更新を示しています。主な変更点は以下の通りです。

1. 記事の日付が「07/21/2026」から「08/31/2026」に変更され、最新の情報が反映されています。
2. 「full text search」という用語が「full-text search」に統一され、用語の一貫性が向上しました。
3. 説明文や項目の内容がより明確に記述されるよう変更され、特にハイブリッド検索やエージェントリトリーバルに関する文が改善されています。
4. フィルタの説明において、`filter` パラメータを強調するためにバッククオートが追加され、プログラムコードを明確に示しています。
5. 次のステップにおいて、新たに提案するリソースの紹介も若干調整され、読者が関連情報にアクセスしやすくなっています。

これにより、ユーザーは検索クエリのさまざまなタイプとその使用方法をより理解しやすくなり、ドキュメント全体の明瞭性と信頼性が向上しています。技術ドキュメントにおける用語の統一と説明の明確化は、読者にとって非常に重要な要素であり、今回の変更がその目的に寄与しています。

## articles/search/search-query-troubleshoot-collection-filters.md{#item-abeca4}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ---
@@ -29,7 +29,7 @@ The following table lists errors that you might encounter when trying to execute
 | Invalid lambda expression. Found an unsupported form of complex Boolean expression. For 'any', use expressions that are 'ORs of ANDs', also known as Disjunctive Normal Form. For example: `(a and b) or (c and d)` where a, b, c, and d are comparison or equality subexpressions. For 'all', use expressions that are 'ANDs of ORs', also known as Conjunctive Normal Form. For example: `(a or b) and (c or d)` where a, b, c, and d are comparison or inequality subexpressions. Examples of comparison expressions: 'x gt 5', 'x le 2'. Example of an equality expression: 'x eq 5'. Example of an inequality expression: 'x ne 5'. | Filtering on fields of type `Collection(Edm.DateTimeOffset)`, `Collection(Edm.Double)`, `Collection(Edm.Int32)`, or `Collection(Edm.Int64)` | [Rules for filtering comparable collections](#bkmk_comparables) |
 | Invalid lambda expression. Found an unsupported use of geo.distance() or geo.intersects() in a lambda expression that iterates over a field of type Collection(Edm.GeographyPoint). For 'any', make sure you compare geo.distance() using the 'lt' or 'le' operators and make sure that any usage of geo.intersects() isn't negated. For 'all', make sure you compare geo.distance() using the 'gt' or 'ge' operators and make sure that any usage of geo.intersects() is negated. | Filtering on a field of type `Collection(Edm.GeographyPoint)` | [Rules for filtering GeographyPoint collections](#bkmk_geopoints) |
 | Invalid lambda expression. Complex Boolean expressions aren't supported in lambda expressions that iterate over fields of type Collection(Edm.GeographyPoint). For 'any', join subexpressions with 'or'; 'and' isn't supported. For 'all', join subexpressions with 'and'; 'or' isn't supported. | Filtering on fields of type `Collection(Edm.String)` or `Collection(Edm.GeographyPoint)` | [Rules for filtering string collections](#bkmk_strings) <br/><br/> [Rules for filtering GeographyPoint collections](#bkmk_geopoints) |
-| Invalid lambda expression. Found a comparison operator (one of 'lt', 'le', 'gt', or 'ge'). Only equality operators are allowed in lambda expressions that iterate over fields of type Collection(Edm.String). For 'any', se expressions of the form 'x eq y'. For 'all', use expressions of the form 'x ne y' or 'not (x eq y)'. | Filtering on a field of type `Collection(Edm.String)` | [Rules for filtering string collections](#bkmk_strings) |
+| Invalid lambda expression. Found a comparison operator (one of 'lt', 'le', 'gt', or 'ge'). Only equality operators are allowed in lambda expressions that iterate over fields of type Collection(Edm.String). For 'any', use expressions of the form 'x eq y'. For 'all', use expressions of the form 'x ne y' or 'not (x eq y)'. | Filtering on a field of type `Collection(Edm.String)` | [Rules for filtering string collections](#bkmk_strings) |
 
 <a name="bkmk_examples"></a>
 
@@ -175,7 +175,7 @@ However, there are limitations on how such comparison expressions can be combine
     - `ratings/all(r: r gt 2 and r le 5)`
     - `ratings/all(r: r le 5 or r gt 7)`
   - Comparison expressions combined with `or` (disjunctions) can be further combined using `and`. This form is known in Boolean logic as "[Conjunctive Normal Form](https://en.wikipedia.org/wiki/Conjunctive_normal_form)" (CNF). For example:
-    - `ratings/all(r: (r le 2 or gt 5) and (r lt 7 or r ge 10))`
+    - `ratings/all(r: (r le 2 or r gt 5) and (r lt 7 or r ge 10))`
 
 <a name="bkmk_complex"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コレクションフィルタのトラブルシューティングに関するドキュメントの更新"
}
```

### Explanation
この変更は、「コレクションフィルタのトラブルシューティング」に関する記事のマイナーな更新を示しています。主な変更点は以下の通りです。

1. 記事の日付が「07/21/2026」から「08/31/2026」に変更され、最新の情報が反映されています。
2. エラーメッセージや説明の内容に微修正が加えられ、特にフィルタリングに関する条件の表現がより明確かつ一貫性を持つように調整されています。
3. 特定の例における条件式において、記述の統一性が向上しており、「>`」や「`<`」が適切に使われるようになっています。
4. 複雑なブール式に関する例も同様に、表現がより明確になり、誤解を生む可能性が低くなっています。

これらの更新により、ユーザーはコレクションフィルターに関連するエラー状況やその解決方法について、より明確に理解できるようになっています。特に技術的なドキュメントにおいては、正確な情報の提供と文の正確さが重要であり、今回の変更がその目的を果たしています。

## articles/search/search-query-understand-collection-filters.md{#item-32c01a}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ---
@@ -29,7 +29,7 @@ At least that's how it works conceptually. In reality, Azure AI Search implement
 There are three underlying reasons why filter features aren't fully supported for all types of collections:
 
 1. Only certain operators are supported for certain data types. For example, it doesn't make sense to compare the Boolean values `true` and `false` by using comparison operators such as `lt` and `gt`.
-1. Azure AI Search doesn't support *correlated search* on fields of type `Collection(Edm.ComplexType)`.
+1. Azure AI Search supports correlated filters on fields of type `Collection(Edm.ComplexType)`, but fielded full-text search over those fields is uncorrelated.
 1. Azure AI Search uses inverted indexes to execute filters over all types of data, including collections.
 
 The first reason is just a consequence of how the OData language and EDM type system are defined. The last two are explained in more detail in the rest of this article.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コレクションフィルタの理解に関するドキュメントの更新"
}
```

### Explanation
この変更は、「コレクションフィルタの理解」に関する記事のマイナーな更新を示しています。主な変更点は以下の通りです。

1. 記事の日付が「07/21/2026」から「08/31/2026」に変更され、最新の情報が反映されています。
2. コレクションフィルタに関する内容が改訂され、特にAzure AI Searchが`Collection(Edm.ComplexType)`のフィールドに対してどう扱うかという点について文言が変更されています。具体的には、相関フィルタがサポートされていることが明確にされ、これによって読者はフィルタの使用条件をより理解しやすくなっています。
3. フィルタリング機能が異なるデータ型にどのように適用されるかに関する説明もより丁寧にまとめられ、混乱を招かないよう配慮されています。この情報は、Azure AI Searchの機能を活用する際に重要です。

これにより、ユーザーはAzure AI Searchのコレクションフィルタに関してより明確な理解を深めることができ、実際の使用において効率的に活用できるようになります。技術文書における正確性と明瞭性の向上は、利用者にとって非常に価値のある改善です。

## articles/search/tutorial-create-custom-analyzer.md{#item-ad5520}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: tutorial
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ai-usage: ai-assisted
 ---
 
@@ -17,7 +17,7 @@ ai-usage: ai-assisted
 
 In search solutions, strings that have complex patterns or special characters can be challenging to work with because the [default analyzer](search-analyzers.md) strips out or misinterprets meaningful parts of a pattern. This results in a poor search experience where users can't find the information they expect. Phone numbers are a classic example of strings that are difficult to analyze. They come in various formats and include special characters that the default analyzer ignores.
 
-With phone numbers as its subject, this tutorial uses the [Search Service REST APIs](/rest/api/searchservice/) to solve patterned data problems using a [custom analyzer](index-add-custom-analyzers.md). This approach can be used as is for phone numbers or adapted for fields with the same characteristics (patterned with special characters), such as URLs, emails, postal codes, and dates.
+By using phone numbers as an example, this tutorial shows how to use the [Search Service REST APIs](/rest/api/searchservice/) to solve patterned data problems by using a [custom analyzer](index-add-custom-analyzers.md). You can use this approach as-is for phone numbers or adapt it for fields with the same characteristics (patterned with special characters), such as URLs, emails, postal codes, and dates.
 
 In this tutorial, you:
 
@@ -580,7 +580,7 @@ To prevent false positives, create a separate analyzer for querying. This analyz
     {
       "@odata.type": "#Microsoft.Azure.Search.CustomAnalyzer",
       "name": "phone_analyzer_search",
-      "tokenizer": "custom_tokenizer_phone",
+      "tokenizer": "keyword_v2",
       "tokenFilters": [],
       "charFilters": [
         "phone_char_mapping"
@@ -607,11 +607,11 @@ With this change, you're all set. Here are your next steps:
 
 1. Delete the index.
 
-1. Recreate the index after you add the new custom analyzer (`phone_analyzer-search`) and assign that analyzer to the `phone-number` field's `searchAnalyzer` property.
+1. Recreate the index after you add the `phone_analyzer_search` analyzer and assign it to the `phone_number` field's `searchAnalyzer` property.
 
 1. Reload the data.
 
-1. Retest the queries to verify that the search works as expected. If you're using the sample file, this step creates the third index named `phone-number-index-3`.
+1. Retest the queries to verify that the search works as expected. If you're using the sample file, this step creates the third index named `phone-numbers-index-3`.
 
 <a name="Alternate"></a>
 
@@ -652,7 +652,7 @@ Given an input of `14255550100`, the analyzer can't logically chunk the phone nu
 ]
 ```
 
-In the following example, the phone number is split into the chunks you normally expect a user to be search for.
+In the following example, the phone number is split into the chunks a user normally searches for.
 
 |Input|Output|  
 |-|-|  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムアナライザー作成に関するチュートリアルの更新"
}
```

### Explanation
この変更は、「カスタムアナライザー作成に関するチュートリアル」のマイナーな更新を示しています。主な変更点は以下の通りです。

1. 記事の日付が「07/21/2026」から「08/31/2026」に変更され、最新の情報が反映されています。
2. チュートリアルの内容において、電話番号を例にした説明文が改善され、より明確で自然な表現に修正されています。具体的には、電話番号の解析に関する部分が「電話番号を使用して、このチュートリアルは…」から「電話番号を例に使い、このチュートリアルは…」に変更され、流れが滑らかになっています。
3. アナライザーの記述として、従来の「phone_analyzer_search」から新しい名称「phone_analyzer_search」に変更され、より一貫した命名規則が反映されています。
4. インデックスのリクリエイトに関する手順の説明も見直され、具体的なフィールド名の変更が反映されています。「phone-number」から「phone_number」への変更など、正確な指定が求められる点で、利用者にとっての利便性が向上しました。

これらの更新により、ユーザーはカスタムアナライザーを使用して複雑なデータパターンを処理する方法をより明確に理解できるようになり、検索ソリューションの改善に直結する情報が提供されています。

## articles/search/tutorial-multiple-data-sources.md{#item-71558f}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how to import data from multiple data sources into a single A
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: tutorial
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ai-usage: ai-assisted
 ms.custom:
   - devx-track-csharp
@@ -173,7 +173,7 @@ When the data and configuration settings are in place, the sample program in `Az
 
 This simple C#/.NET console app performs the following tasks:
 
-* Creates a new index based on the data structure of the C# Hotel class, which also references the Address and Room classes.
+* Creates a new index based on the data structure of the C# `Hotel` class, which also references the `Address` and `Room` classes.
 * Creates a new data source and an indexer that maps Azure Cosmos DB data to index fields. These are both objects in Azure AI Search.
 * Runs the indexer to load hotel data from Azure Cosmos DB.
 * Creates a second data source and an indexer that maps JSON blob data to index fields.
@@ -350,11 +350,11 @@ await indexerClient.CreateOrUpdateIndexerAsync(blobIndexer);
 try
 {
     // Run the indexer.
-    await searchService.Indexers.RunAsync(blobIndexer.Name);
+    await indexerClient.RunIndexerAsync(blobIndexer.Name);
 }
-catch (CloudException e) when (e.Response.StatusCode == (HttpStatusCode)429)
+catch (RequestFailedException ex) when (ex.Status == 429)
 {
-    Console.WriteLine("Failed to run indexer: {0}", e.Response.Content);
+    Console.WriteLine("Failed to run indexer: {0}", ex.Message);
 }
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "複数のデータソースからのデータインポートチュートリアルの更新"
}
```

### Explanation
この変更は、「複数のデータソースからのデータインポート」に関するチュートリアルのマイナーな更新を示しています。主な変更点は以下の通りです。

1. 記事の日付が「07/21/2026」から「08/31/2026」に変更され、最新の情報が反映されています。
2. 中で言及されたクラス名が引用符で強調表示されるよう修正されました。具体的には、C#の`Hotel`クラスの表記が強調され、`Address`および`Room`クラスの参照も同様に変更されました。
3. インデクサーの実行に関するコード行の一部が変更され、より正確なクラス名やメソッド名が使用されています。特に、`searchService.Indexers.RunAsync`から`indexerClient.RunIndexerAsync`への変更は、コードの整合性を保ち、最新のAPIに適合させるためのものであります。
4. エラーハンドリングにおける例外のクラス名も更新され、`CloudException`から`RequestFailedException`へ変更があり、これによりエラーメッセージの取得方法が明確化されています。

これらの更新によって、チュートリアルはより現代的で正確な情報を提供し、ユーザーが複数のデータソースからデータをインポートする際の理解を深める手助けとなります。

## articles/search/tutorial-optimize-indexing-push-api.md{#item-ef0e96}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: tutorial
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ai-usage: ai-assisted
 ms.custom:
   - devx-track-csharp
@@ -211,20 +211,8 @@ Because not all documents are the same size (although they are in this sample),
 // Returns size of object in MB
 public static double EstimateObjectSize(object data)
 {
-    // converting object to byte[] to determine the size of the data
-    BinaryFormatter bf = new BinaryFormatter();
-    MemoryStream ms = new MemoryStream();
-    byte[] Array;
-
-    // converting data to json for more accurate sizing
-    var json = JsonSerializer.Serialize(data);
-    bf.Serialize(ms, json);
-    Array = ms.ToArray();
-
-    // converting from bytes to megabytes
-    double sizeInMb = (double)Array.Length / 1000000;
-
-    return sizeInMb;
+    byte[] json = JsonSerializer.SerializeToUtf8Bytes(data);
+    return json.Length / 1_000_000d;
 }
 ```
 
@@ -277,7 +265,7 @@ IndexDocumentsResult result = null;
 
 // Define parameters for exponential backoff
 int attempts = 0;
-TimeSpan delay = delay = TimeSpan.FromSeconds(2);
+TimeSpan delay = TimeSpan.FromSeconds(2);
 int maxRetryAttempts = 5;
 ```
 
@@ -292,7 +280,10 @@ do
     try
     {
         attempts++;
-        result = await searchClient.IndexDocumentsAsync(batch).ConfigureAwait(false);
+        Response<IndexDocumentsResult> response = await searchClient
+            .IndexDocumentsAsync(batch)
+            .ConfigureAwait(false);
+        result = response.Value;
 
         var failedDocuments = result.Results.Where(r => r.Succeeded != true).ToList();
 
@@ -344,7 +335,7 @@ From here, wrap the exponential backoff code into a function so it can be easily
 Another function is then created to manage the active threads. For simplicity, that function isn't included here but can be found in *ExponentialBackoff.cs*. You can call the function using the following command, where `hotels` is the data we want to upload, `1000` is the batch size, and `8` is the number of concurrent threads.
 
 ```csharp
-await ExponentialBackoff.IndexData(indexClient, hotels, 1000, 8);
+await ExponentialBackoff.IndexDataAsync(searchClient, hotels, 1000, 8);
 ```
 
 When you run the function, you should see an output similar to the following example:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス作成の最適化に関するチュートリアルの更新"
}
```

### Explanation
この変更は、「インデックス作成の最適化に関するチュートリアル」のマイナーな更新を示しています。主な変更点は以下の通りです。

1. 記事の日付が「07/21/2026」から「08/31/2026」に変更され、最新の情報が反映されています。
2. オブジェクトサイズを推定するメソッドにおいて、実装が簡素化され、可読性が向上しました。以前は、データをバイナリ形式にシリアライズしてサイズを計算していましたが、新しい実装では`JsonSerializer.SerializeToUtf8Bytes`を使用して直接バイト配列を取得し、その長さをMB単位で返すように変更されています。
3. エクスポネンシャルバックオフの設定に関連するコードに冗長な部分があったが、これが改善され、より洗練された表現に修正されています。特に、Delayの初期化行が簡略化され、重複したコードが排除されました。
4. インデックス作成の結果を取得する手順において、レスポンスの処理が更新され、`Response<IndexDocumentsResult>`型を使用することで、非同期メソッドの呼び出し結果が明確になりました。これにより、結果の取得が一貫した形で行われるようになりました。
5. 最後の関数呼び出しにおいて、メソッド名が`IndexData`から`IndexDataAsync`に変更され、非同期処理であることが明示されています。

これらの更新によって、チュートリアルは、より効率的で理解しやすい内容に生まれ変わり、インデックス作成の最適化を学ぶユーザーにとっての便益が増しています。

## articles/search/vector-search-index-size.md{#item-bb2846}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.reviewer: robertlee
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: concept-article
-ms.date: 07/21/2026
+ms.date: 08/31/2026
 ai-usage: ai-assisted
 ms.custom:
   - build-2024
@@ -89,7 +89,7 @@ Quotas for both storage and vector index size increase or decrease as you add or
 
 Data plane REST APIs (all newer APIs provide vector usage statistics):
 
-+ [GET Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics) returns quota and usage for the search service all-up.
++ [GET Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics) returns overall quota and usage for the search service.
 + [GET Index Statistics](/rest/api/searchservice/indexes/get-statistics) returns usage for a given index.
 
 Usage and quota are reported in bytes.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索インデックスサイズに関する記事の更新"
}
```

### Explanation
この変更は、「ベクトル検索インデックスサイズ」に関する記事のマイナーな更新を示しています。主な変更点は以下の通りです。

1. 記事の日付が「07/21/2026」から「08/31/2026」に変更され、最新の情報が反映されています。
2. APIの説明において、`GET Service Statistics`の文言が若干修正されました。具体的には、「search service all-up」という表現が「overall quota and usage for the search service」に変更され、より明確で簡潔な表現に改善されています。この修正により、APIの機能が理解しやすくなりました。
3. その他の小さな文言変更もあり、全体的な可読性が向上するように調整されています。

これらの更新によって、記事はより正確でユーザーにとってわかりやすい内容になり、ベクトル検索インデックスサイズに関する理解を深める助けとなるでしょう。


