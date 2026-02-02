---
date: '2026-02-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8ef275a...MicrosoftDocs:00bac45
summary: このドキュメントの変更ポイントは、Azure AI Searchのインデックスプロジェクションと文書のチャンク処理に関するもので、親子関係の処理方法についての具体的な説明が追加され、チャンク処理に関連する文書のタイトルが明確に変更されています。新機能として、親ドキュメントとチャンクドキュメントのマッピング方法が詳細に説明され、インデックス設計のアプローチが分かりやすく整理されています。特に破壊的な変更はなく、文書のタイトル更新や日付の最新化も行われました。この更新により、ユーザーはAzure
  AI Searchのインデックス設計をより効率的に行えるようになり、検索プロセスも理解しやすくなります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8ef275a...MicrosoftDocs:00bac45){target="_blank"}

# ハイライト

このドキュメントの変更ポイントは、Azure AI Searchに関連したインデックスプロジェクションと文書のチャンク処理に関するものです。インデックスプロジェクションの定義が明確になり、親子関係の処理方法についての具体的な説明が追加されました。また、チャンク処理に関連する文書のタイトルがよりわかりやすく変更されています。

## 新機能

- インデックスプロジェクションにおいて、親ドキュメントとチャンクドキュメントのマッピング方法が詳細に説明されました。
- インデックス設計のアプローチが表形式で整理され、異なるアプローチの手法が分かりやすくなりました。

## 破壊的変更

- 特に破壊的な変更は示されていません。

## その他の更新

- 「エージェンティック検索とベクター検索のための大きな文書をチャンク化」というタイトルが「RAGおよびベクター検索のための大きな文書をチャンク化」に変更されました。
- Documentの日付とサイクルが最新のものに更新されました。

# 洞察

Azure AI Searchのドキュメント更新は、インデックスプロジェクションとチャンク処理の理解を深めるためのものです。従来のガイドラインに対し、具体的な親ドキュメントからチャンクドキュメントへのマッピング法を追加し、スタンドアロンのドキュメントとしてインデックス化するかを選べる選択肢が示されました。これにより、ユーザーはより賢明で効率的なインデックス設計が可能になります。

また、文書のタイトル更新では、RAG（Retrieval Augmented Generation）としての役割が強調されており、その観点での検索プロセスを理解しやすくしています。タイトルの修正によって文書の内容が一目で分かりやすくなるため、読者が迅速に必要な情報を見つけられることにつながるでしょう。

こうした詳細の追加とタイトルの修正は、新機能や概念を容易にユーザーが活用し、効果的にAzure AI Searchを用いるためのサポートを目指しています。これにより、プロジェクトの実装と管理がよりスムーズになると期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-how-to-define-index-projections.md](#item-a7e2c5) | minor update | インデックスプロジェクションの定義に関する更新 | modified | 146 | 128 | 274 | 
| [vector-search-how-to-chunk-documents.md](#item-b79133) | minor update | 文書のチャンク処理に関するタイトルの修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/search-how-to-define-index-projections.md{#item-a7e2c5}

<details>
<summary>Diff</summary>
````diff
@@ -8,62 +8,83 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 01/26/2026
+ms.date: 01/30/2026
 ms.update-cycle: 180-days
 ---
 
 # Define an index projection for parent-child indexing
 
-If you're chunking content for either a RAG pattern or vectorization, you can specify an *index projection* to control whether elements of the parent document, such as a file name or creation date, repeat for each child (chunk) or are indexed as standalone search documents in a second index.
+If you're chunking content for either a RAG pattern or vectorization, you can specify an **index projection** to control *one-to-many indexing*, where source content (one) is projected to one or more indexes (many). The intent of an index projection is to control whether elements of the parent document, such as a file name or creation date:
 
-We recommend repeating fields in a single index because splitting content into two indexes can be difficult to query, especially in classic search where index joins aren't supported.
+- Repeat for each child (chunk) in a single index
+- Are indexed as standalone search documents in the same index
+- Or, are ingested into separate indexes
 
-In Azure AI Search, chunking is performed by skills and thus depends on indexers. To define an index projection, specify it in a [skillset](cognitive-search-working-with-skillsets.md). 
+We recommend repeating parent fields in a single index because having different document shapes or splitting content into two indexes can be difficult to query, especially in classic search where index joins aren't supported.
+
+In Azure AI Search, chunking is performed by skills and thus depends on indexers. To define an index projection, specify it in a [skillset](cognitive-search-working-with-skillsets.md).
 
 ## Prerequisites
 
-- An [indexer-based indexing pipeline](search-indexer-overview.md).
+- Azure AI Search, any tier or region.
 
-- An index (one or more) that accepts the output of the indexer pipeline.
+- An [indexer-based indexing pipeline](search-indexer-overview.md).
 
 - A [supported data source](search-indexer-overview.md#supported-data-sources) having content that you want to chunk.
 
-- A skill that splits content into chunks, either the [Text Split skill](cognitive-search-skill-textsplit.md) or a custom skill that provides equivalent functionality. 
+- An index (one or many) that accepts the output of the indexer pipeline.
+
+- A skill that [chunks content](vector-search-how-to-chunk-documents.md), such as the [Text Split skill](cognitive-search-skill-textsplit.md). 
 
 The skillset contains the indexer projection that shapes the data for one-to-many indexing. A skillset could also have other skills, such as an embedding skill like [AzureOpenAIEmbedding](cognitive-search-skill-azure-openai-embedding.md) if your scenario includes integrated vectorization.
 
-### Choose an approach
+## Choose an approach
+
+Index projections generate "child" documents (chunks) for each "parent" document. Choose how to handle parent content:
 
-Through an index projection, you can send content to:
+| Approach | Description | Configuration |
+|----------|-------------|---------------|
+| **Single index, repeating parent fields** (recommended) | Parent fields repeat for each chunk. All documents have a uniform shape. | Set both indexer `targetIndexName` and index projection `targetIndexName` to the same index. Set `projectionMode` to `skipIndexingParentDocuments`. |
+| **Single index, mixed document shapes** | Parent documents and chunk documents coexist. Parent documents have null chunk fields. | Set both `targetIndexName` values to the same index. Set `projectionMode` to `includeIndexingParentDocuments` (or omit, as it's the default). |
+| **Two or more separate indexes** | Parent index for metadata lookups, child index for search. No query-time joins. | Set indexer `targetIndexName` to parent index. Set index projection `targetIndexName` to child index. The `selectors` array determines the quantity and composition of the child index. |
 
-- A single index, where the parent fields repeat for each chunk, but the grain of the index is at the chunk level. The [classic RAG example](https://github.com/Azure-Samples/azure-search-classic-rag/blob/main/README.md) shows this approach.
+For most RAG scenarios, use the first approach. See the [classic RAG example](https://github.com/Azure-Samples/azure-search-classic-rag/blob/main/README.md).
 
-- Two or more indexes, where the parent index has fields related to the parent document, and the child index is organized around chunks. The child index is the primary search corpus, but the parent index could be used for [lookup queries](/rest/api/searchservice/documents/get) when you want to retrieve the parent fields of a particular chunk, or for independent queries.
+### Implementation steps for the recommended approach
 
-Most implementations are a single index organized around chunks with parent fields, such as the document filename, repeating for each chunk. However, the system is designed to support separate and multiple child indexes if that's your requirement. Azure AI Search doesn't support index joins so your application code must handle which index to use.
+1. [Create an index](#create-an-index-for-one-to-many-indexing) designed for chunks, with parent fields included.
+1. [Create a skillset](#add-index-projections-to-a-skillset) with a chunking skill and `indexProjections`.
+1. [Create an indexer](search-how-to-create-indexers.md) pointing to your [supported data source](search-indexer-overview.md#supported-data-sources).
+
+If your data source supports change tracking, the indexer synchronizes changes automatically.
 
 ## Create an index for one-to-many indexing
 
-Whether you create one index for chunks that repeat parent values, or separate indexes for parent-child field placement, the primary index used for searching is designed around data chunks. It must have the following fields:
+Whether you create one index for chunks that repeat parent values, or separate indexes for parent-child field placement, the primary index used for searching is designed around data chunks. The index schema must have the following fields:
 
 - A document key field uniquely identifying each document. It must be defined as type `Edm.String` with the `keyword` analyzer.
 
 - A field associating each chunk with its parent. It must be of type `Edm.String`. It can't be the document key field, and must have `filterable` set to true. It's referred to as parent_id in the examples and as a [projected key value](#projected-key-value) in this article.
 
 - Other fields for content, such as text or vectorized chunk fields.
 
-An index must exist on the search service before you create the skillset or run the indexer.
+An index must exist on the search service before you create the skillset or run the indexer. The `selectors` you define in the skillset should include these fields.
 
 ### Single index schema inclusive of parent and child fields
 
 A single index designed around chunks with parent content repeating for each chunk is the predominant pattern for RAG and vector search scenarios. The ability to associate the correct parent content with each chunk is enabled through index projections.
 
-The following schema is an example that meets the requirements for index projections. In this example, parent fields are the parent_id and the title. Child fields are the vector and nonvector vector chunks. The chunk_id is the document ID of this index. The parent_id and title repeat for every chunk in the index.
+The following schema is an example that meets the requirements for index projections. In this example:
+
+- Parent fields are the parent_id and the title, and they repeat for each chunk
+- Child fields are the vector and nonvector vector chunks. The chunk_id is the document ID of this index.
 
 You can use the Azure portal, REST APIs, or an Azure SDK to [create an index](search-how-to-load-search-index.md).
 
 #### [**REST**](#tab/rest-create-index)
 
+Use a REST client or the Azure portal **Add index** action and JSON option to create the index.
+
 ```json
 {
     "name": "my_consolidated_index",
@@ -75,8 +96,8 @@ You can use the Azure portal, REST APIs, or an Azure SDK to [create an index](se
         {"name": "chunk_vector", "type": "Collection(Edm.Single)", "searchable": true, "retrievable": false, "stored": false, "dimensions": 1536, "vectorSearchProfile": "hnsw"}
     ],
     "vectorSearch": {
-        "algorithms": [{"name": "hsnw", "kind": "hnsw", "hnswParameters": {}}],
-        "profiles": [{"name": "hsnw", "algorithm": "hnsw"}]
+        "algorithms": [{"name": "hnsw", "kind": "hnsw", "hnswParameters": {}}],
+        "profiles": [{"name": "hnsw", "algorithm": "hnsw"}]
     }
 }
 ```
@@ -134,8 +155,6 @@ This example is similar to the [classic RAG example](https://github.com/Azure-Sa
 
 Index projections are defined inside a skillset definition and are primarily defined as an array of `selectors`, where each selector corresponds to a different target index on the search service. This section starts with syntax and examples for context, followed by [parameter reference](#parameter-reference). 
 
-Choose a tab for the various API syntax. There's currently no portal support for setting up projections, other than editing the skillset JSON definition. Refer to the REST example for JSON.
-
 #### [**REST**](#tab/rest-create-index-projection)
 
 Index projections are generally available. We recommend the most recent stable API:
@@ -213,57 +232,43 @@ For .NET developers, use the [IndexProjections Class](/dotnet/api/azure.search.d
 
 | Index projection parameters | Definition |
 |----------------------------|------------|
-| `selectors` | Parameters for the main search corpus, usually the one designed around chunks. |
-| `projectionMode` | An optional parameter providing instructions to the indexer. The only valid value for this parameter is `skipIndexingParentDocuments`, and it's used when the chunk index is the primary search corpus and you need to specify whether parent fields are indexed as extra search documents within the chunked index. If you don't set `skipIndexingParentDocuments`, you get extra search documents in your index that are null for chunks, but populated with parent fields only. For example, if five documents contribute 100 chunks to the index, then the number of documents in the index is 105. The five documents created or parent fields have nulls for chunk (child) fields, making them substantially different from the bulk of the documents in the index. We recommend `projectionMode` set to `skipIndexingParentDocument`. |
+| `selectors` | An array with parameters for the main search corpus, usually the index designed around chunks. You can send content to multiple child indexes by specifying multiple selectors. The index schemas must exist on the search service before you run the indexer. |
+| `parameters` | A parameter dictionary of index projection-specific configuration properties. |
 
-Selectors have the following parameters as part of their definition.
+Parameters have the following elements as part of their definition.
 
-| Selector parameters | Definition |
+| Parameters | Definition |
+|----------------------------|------------|
+| `parameters.projectionMode` | An optional parameter providing instructions to the indexer. Valid values include `includeIndexingParentDocuments` and `skipIndexingParentDocuments`. <br><br>The best value for this parameter is `skipIndexingParentDocuments`. You should use it when chunked documents are the primary search target. <br><br>If you don't set `skipIndexingParentDocuments` for `projectionMode`, you get `includeIndexingParentDocuments` automatically because it's the default. It adds extra search documents in your index that are null for chunks, but populated with parent-specific content. For example, if five PDFs contribute 100 chunks to the index, then the number of documents in the index is 105. The five documents created for parent fields have nulls for chunk (child) fields, making them substantially different from the bulk of the documents in the index. For this reason, we recommend `projectionMode` set to `skipIndexingParentDocuments`. |
+
+Selectors have the following elements as part of their definition.
+
+| Selectors | Definition |
 |-----------|------------|
-| `targetIndexName` | The name of the index into which index data is projected. It's either the single chunked index with repeating parent fields, or it's the child index if you're using [separate indexes](#example-of-separate-parent-child-indexes) for parent-child content. |
-| `parentKeyFieldName` | The name of the field providing the key for the parent document.|
-| `sourceContext` | The enrichment annotation that defines the granularity at which to map data into individual search documents. For more information, see [Skill context and input annotation language](cognitive-search-skill-annotation-language.md). |
-| `mappings` | An array of mappings of enriched data to fields in the search index. Each mapping consists of: <br>`name`: The name of the field in the search index that the data should be indexed into. <br>`source`: The enrichment annotation path that the data should be pulled from. <br><br>Each `mapping` can also recursively define data with an optional `sourceContext` and `inputs` field, similar to the [knowledge store](knowledge-store-concept-intro.md) or [Shaper Skill](cognitive-search-skill-shaper.md). Depending on your application, these parameters allow you to shape data into fields of type `Edm.ComplexType` in the search index. Some LLMs don't accept a complex type in search results, so the LLM you're using determines whether a complex type mapping is helpful or not.|
+| `selectors.targetIndexName` | The name of the index into which index data is projected. It's either the single chunked index with repeating parent fields, or it's the child index if you're using [separate indexes](#example-of-separate-parent-child-indexes) for parent-child content. |
+| `selectors.parentKeyFieldName` | The name of the field providing the key for the parent document.|
+| `selectors.sourceContext` | The enrichment annotation that defines the granularity at which to map data into individual search documents. For more information, see [Skill context and input annotation language](cognitive-search-skill-annotation-language.md). |
+| `selectors.mappings` | An array of mappings of enriched data to fields in the search index. Each mapping consists of: <br>`name`: The name of the field in the search index that the data should be indexed into. <br>`source`: The enrichment annotation path that the data should be pulled from. <br><br>Each `mapping` can also recursively define data with an optional `sourceContext` and `inputs` field, similar to the [knowledge store](knowledge-store-concept-intro.md) or [Shaper Skill](cognitive-search-skill-shaper.md). Depending on your application, these parameters allow you to shape data into fields of type `Edm.ComplexType` in the search index. Some LLMs don't accept a complex type in search results, so the LLM you're using determines whether a complex type mapping is helpful or not.|
 
 The `mappings` parameter is important. You must explicitly map every field in the child index, except for the ID fields such as document key and the parent ID. 
 
 This requirement is in contrast with other field mapping conventions in Azure AI Search. For some data source types, the indexer can implicitly map fields based on similar names, or known characteristics (for example, blob indexers use the unique metadata storage path as the default document key). However, for indexer projections, you must explicitly specify every field mapping on the "many" side of the relationship.
 
-Do not create a field mapping for the parent key field. Doing so disrupts change tracking and synchronized data refresh.
-
-## Handling parent documents
-
-Now that you've seen several patterns for one-to-many indexings, lets compare key differences about each option. Index projections effectively generate "child" documents for each "parent" document that runs through a skillset. You have several choices for handling the "parent" documents.
-
-- To send parent and child documents to separate indexes, set the `targetIndexName` for your indexer definition to the parent index, and set the `targetIndexName` in the index projection selector to the child index.
-
-- To keep parent and child documents in the same index, set the indexer `targetIndexName` and the index projection `targetIndexName` to the same index.
-
-- To avoid creating parent search documents and ensuring the index contains only child documents of a uniform grain, set the `targetIndexName` for both the indexer definition and the selector to the same index, but add an extra `parameters` object after `selectors`, with a `projectionMode` key set to `skipIndexingParentDocuments`, as shown here:
-
-   ```json
-   "indexProjections": {
-       "selectors": [
-           ...
-       ],
-       "parameters": {
-           "projectionMode": "skipIndexingParentDocuments"
-       }
-   }
-   ```
+> [!IMPORTANT]
+> Don't create a field mapping for the parent key field. Doing so disrupts change tracking and synchronized data refresh.
 
 ## Review field mappings
 
 Indexers are affiliated with three different types of field mappings. Before you run the indexer, check your field mappings and know when to use each type.
 
 [Field mappings](search-indexer-field-mappings.md) are defined in an indexer and used to map a source field to an index field. Field mappings are used for data paths that lift data from the source and pass it in for indexing, with no intermediate skills processing step. Typically, an indexer can automatically map fields that have the same name and type. Explicit field mappings are only required when there's discrepancies. In one-to-many indexing and the patterns discussed thus far, you might not need field mappings.
 
-[Output field mappings](cognitive-search-output-field-mapping.md) are defined in an indexer and used to map enriched content generated by a skillset to a field into the main index. In the one-to-many patterns covered in this article, it is a single index schema that includes parent and child fields. The parent index is sparse, with just a title field. The title field isn't populated with content from the skillset processing, so we don't need an output field mapping.
+[Output field mappings](cognitive-search-output-field-mapping.md) are defined in an indexer and used to map enriched content generated by a skillset to a field into the main index. Chunks are considered enriched content due to creation by a skill (Text Split), but you don't need an output field mapping for chunks, or for index projections that are defined by a selector mapping.
 
-Indexer projection field mappings are used to map skillset-generated content to fields in the child index. In cases where the child index also includes parent fields (as in the [consolidated index solution](#single-index-schema-inclusive-of-parent-and-child-fields)), you should set up field mappings for every field that has content, including the parent-level title field, assuming you want the title to show up in each chunked document. If you're using [separate parent and child indexes](#example-of-separate-parent-child-indexes), the indexer projections should have field mappings for just the child-level fields.
+[Selectors.mappings](#parameter-reference) are defined in a skillset and map to fields in the child index. In cases where the child index also includes parent fields (as in the [consolidated index solution](#single-index-schema-inclusive-of-parent-and-child-fields)), you should set up field mappings for every field that has content, including the parent-level title field, assuming you want the title to show up in each chunked document. If you're using [separate parent and child indexes](#example-of-separate-parent-child-indexes), the selector should have field mappings for just the child-level fields.
 
 > [!NOTE]
-> Both output field mappings and indexer projection field mappings accept enriched document tree nodes as source inputs. Knowing how to specify a path to each node is essential to setting up the data path. To learn more about path syntax, see [Reference a path to enriched nodes](cognitive-search-concept-annotations-syntax.md) and [skillset definition](cognitive-search-working-with-skillsets.md#skillset-definition) for examples.
+> Both output field mappings and selector mappings accept enriched document tree nodes as source inputs. Knowing how to specify a path to each node is essential to setting up the data path. To learn more about path syntax, see [Reference a path to enriched nodes](cognitive-search-concept-annotations-syntax.md) and [skillset definition](cognitive-search-working-with-skillsets.md#skillset-definition) for examples.
 
 ## Run the indexer
 
@@ -292,7 +297,7 @@ Some data sources like [Azure Storage](search-how-to-index-azure-blob-changed-de
 
 If the source content no longer exists (for example, if text is shortened to have fewer chunks), the corresponding child document in the search index is deleted. The remaining child documents also get their key updated to include a new hash value, even if their content didn't otherwise change.
 
-If a parent document is completely deleted from the datasource, the corresponding child documents only get deleted if the deletion is detected by a `dataDeletionDetectionPolicy` defined on the datasource definition. If you don't have a `dataDeletionDetectionPolicy` configured and need to delete a parent document from the datasource, then you should manually delete the child documents if they're no longer wanted.
+If a parent document is completely deleted from the datasource, the corresponding child documents only get deleted if the deletion is detected by a `dataDeletionDetectionPolicy` defined on the datasource definition. If you don't have a `dataDeletionDetectionPolicy` configured and need to delete a parent document from the datasource, then you should [manually delete the child documents](search-how-to-delete-documents.md) if they're no longer wanted.
 
 ### Projected key value
 
@@ -302,7 +307,7 @@ A projected key value is a unique identifier that the indexer generates for each
 
 - A random hash to guarantee uniqueness. This hash changes if the parent document is updated on subsequent indexer runs.
 - The parent document's key.
-- The enrichment annotation path that identifies the context that that document was generated from.
+- The enrichment annotation path that identifies the context for the generated document.
 
 For example, if you split a parent document with key value "aa1b22c33" into four pages, and then each of those pages is projected as its own document via index projections:
 
@@ -315,85 +320,98 @@ If the parent document is updated in the source data, perhaps resulting in more
 
 ## Example of separate parent-child indexes
 
-This section shows examples for separate parent and child indexes. It's an uncommon pattern, but it's possible you might have application requirements that are best met using this approach. In this scenario, you're projecting parent-child content into two separate indexes.
+This section shows an example for separate parent and child indexes. It's an uncommon pattern, but it's possible you might have application requirements that are best met using this approach. In this scenario, you're projecting parent-child content into two separate indexes.
 
-Each schema has the fields for its particular grain, with the parent ID field common to both indexes for use in a [lookup query](/rest/api/searchservice/documents/get). The primary search corpus is the child index, but then issue a lookup query to retrieve the parent fields for each match in the result. Azure AI Search doesn't support joins at query time, so your application code or orchestration layer would need to merge or collate results that can be passed to an app or process.
+1. Create two index schemas.
 
-The parent index has a parent_id field and title. The parent_id is the document key. You don't need vector search configuration unless you want to vectorize fields at the parent document level.
+   Each schema has the fields for its particular grain, with the parent ID field common to both indexes for use in a [lookup query](/rest/api/searchservice/documents/get). The primary search corpus is the child index, but you can issue a lookup query to retrieve the parent fields for each match in the result. Azure AI Search doesn't support joins at query time, so your application code or orchestration layer would need to merge or collate results that can be passed to an app or process.
 
-```json
-{
-    "name": "my-parent-index",
-    "fields": [
-
-        {"name": "parent_id", "type": "Edm.String", "filterable": true},
-        {"name": "title", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "retrievable": true},
-    ]
-}
-```
-
-The child index has the chunked fields, plus the parent_id field. If you're using integrated vectorization, scoring profiles, semantic ranker, or analyzers you would set these in the child index.
-
-```json
-{
-    "name": "my-child-index",
-    "fields": [
-        {"name": "chunk_id", "type": "Edm.String", "key": true, "filterable": true, "analyzer": "keyword"},
-        {"name": "parent_id", "type": "Edm.String", "filterable": true},
-         {"name": "chunk", "type": "Edm.String","searchable": true,"retrievable": true},
-        {"name": "chunk_vector", "type": "Collection(Edm.Single)", "searchable": true, "retrievable": false, "stored": false, "dimensions": 1536, "vectorSearchProfile": "hnsw"}
-    ],
-    "vectorSearch": {
-        "algorithms": [{"name": "hsnw", "kind": "hnsw", "hnswParameters": {}}],
-        "profiles": [{"name": "hsnw", "algorithm": "hnsw"}]
-    },
-    "scoringProfiles": [],
-    "semanticConfiguration": [],
-    "analyzers": []
-}
-```
-
-Here's an example of an index projection definition that specifies the data path the indexer should use to index content. It specifies the child index name in the index projection definition, and it specifies the mappings of every child or chunk-level field. This is the only place the child index name is specified. 
-
-```json
-"indexProjections": {
-    "selectors": [
-        {
-            "targetIndexName": "my-child-index",
-            "parentKeyFieldName": "parent_id",
-            "sourceContext": "/document/pages/*",
-            "mappings": [
-                {
-                    "name": "chunk",
-                    "source": "/document/pages/*",
-                    "sourceContext": null,
-                    "inputs": []
-                },
-                {
-                    "name": "chunk_vector",
-                    "source": "/document/pages/*/chunk_vector",
-                    "sourceContext": null,
-                    "inputs": []
-                }
-            ]
-        }
-    ]
-}
-```
+    The parent index has a parent_id field and title. The parent_id is the document key. You don't need vector search configuration unless you want to vectorize fields at the parent document level.
+    
+    ```json
+    {
+        "name": "my-parent-index",
+        "fields": [
+    
+            {"name": "parent_id", "type": "Edm.String", "key":true, "filterable": true},
+            {"name": "title", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "retrievable": true}
+        ]
+    }
+    ```
+    
+    The child index has the chunked fields, plus the parent_id field. If you're using integrated vectorization, scoring profiles, semantic ranker, or analyzers you would set these in the child index.
+    
+    ```json
+    {
+        "name": "my-child-index",
+        "fields": [
+            {"name": "chunk_id", "type": "Edm.String", "key": true, "filterable": true, "analyzer": "keyword"},
+            {"name": "parent_id", "type": "Edm.String", "filterable": true},
+             {"name": "chunk", "type": "Edm.String","searchable": true,"retrievable": true},
+            {"name": "chunk_vector", "type": "Collection(Edm.Single)", "searchable": true, "retrievable": false, "stored": false, "dimensions": 1536, "vectorSearchProfile": "hnsw"}
+        ],
+        "vectorSearch": {
+            "algorithms": [{"name": "hsnw", "kind": "hnsw", "hnswParameters": {}}],
+            "profiles": [{"name": "hsnw", "algorithm": "hnsw"}]
+        },
+        "scoringProfiles": [],
+        "semanticConfiguration": [],
+        "analyzers": []
+    }
+    ```
+
+1. Update the indexer to specify parent-index as the target.
+
+    The indexer definition specifies the components of the pipeline. In the indexer definition, the index name to provide is the parent index. If you need field mappings for the parent-level fields, define them in outputFieldMappings. For one-to-many indexing that uses separate indexes, the indexer definition might look like the following example. 
+    
+    ```json
+    {
+      "name": "my-indexer",
+      "dataSourceName": "my-ds",
+      "targetIndexName": "my-parent-index",
+      "skillsetName" : "my-skillset",
+      "parameters": { },
+      "fieldMappings": (optional) Maps fields in the underlying data source to fields in an index,
+      "outputFieldMappings" : (required) Maps skill outputs to fields in an index,
+    }
+    ```
+
+1. Add `indexProjections` to the skillset.
+
+    Here's an example of an index projection definition that specifies the data path the indexer should use to index content. It specifies the child index name in the index projection definition, and it specifies the mappings of every child or chunk-level field. This is the only place the child index name is specified.
+
+    Notice that `parameters` is null and is using the default `includeIndexingParentDocuments`. The indexer populates the parent index. The `selectors` array is used to project the chunk documents to the child index. 
+    
+    ```json
+    "indexProjections": {
+        "selectors": [
+            {
+                "targetIndexName": "my-child-index",
+                "parentKeyFieldName": "parent_id",
+                "sourceContext": "/document/pages/*",
+                "mappings": [
+                    {
+                        "name": "chunk",
+                        "source": "/document/pages/*",
+                        "sourceContext": null,
+                        "inputs": []
+                    },
+                    {
+                        "name": "chunk_vector",
+                        "source": "/document/pages/*/chunk_vector",
+                        "sourceContext": null,
+                        "inputs": []
+                    }
+                ]
+            }
+        ],
+        "parameters": {}
+    }
+    ```
 
-The indexer definition specifies the components of the pipeline. In the indexer definition, the index name to provide is the parent index. If you need field mappings for the parent-level fields, define them in outputFieldMappings. For one-to-many indexing that uses separate indexes, the indexer definition might look like the following example. 
+1. [Run the indexer](search-howto-run-reset-indexers.md). If you previously ran the indexer, remember to reset it first.
 
-```json
-{
-  "name": "my-indexer",
-  "dataSourceName": "my-ds",
-  "targetIndexName": "my-parent-index",
-  "skillsetName" : "my-skillset"
-  "parameters": { },
-  "fieldMappings": (optional) Maps fields in the underlying data source to fields in an index,
-  "outputFieldMappings" : (required) Maps skill outputs to fields in an index,
-}
-```
+   You should have two indexes populated with the appropriate content. Query the indexes in Search Explorer to verify each one has the correct content.
 
 ## Next step
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスプロジェクションの定義に関する更新"
}
```

### Explanation
この変更では、Azure AI Searchにおけるインデックスプロジェクションの定義に関するドキュメントが更新されました。文書には、親子関係のインデックス作成や、コンテンツのチャンク処理に関して、より明確な説明が追加されています。

具体的には、以下のポイントが改善されました：
- インデックスプロジェクションの目的が説明され、親ドキュメントからチャンクドキュメントへのマッピングの方法が詳述されています。特に、親の要素をチャンクごとに繰り返すか、スタンドアロンの検索ドキュメントとしてインデックス化するかの選択肢が強調されています。
- さまざまなインデックス設計のアプローチが表形式で整理され、どのように親コンテンツを処理するかに関する具体的な手法が提供されています。また、インデックスプロジェクションに関連するフィールドマッピングや構成についても言及されています。
- 更新された日付とサイクルも含まれており、文書が最新の内容に基づいていることが示されています。

全体として、これらの変更は、ユーザーがインデックスプロジェクションの設定とその利点をより良く理解できるようにすることを目的としています。

## articles/search/vector-search-how-to-chunk-documents.md{#item-b79133}

<details>
<summary>Diff</summary>
````diff
@@ -12,11 +12,11 @@ ms.topic: concept-article
 ms.date: 10/30/2025
 ---
 
-# Chunk large documents for agentic retrieval and vector search in Azure AI Search
+# Chunk large documents for RAG and vector search in Azure AI Search
 
 Partitioning large documents into smaller chunks can help you stay under the maximum token input limits of chat completion and  embedding models. For example, the maximum length of input text for the [Azure OpenAI](/azure/ai-services/openai/how-to/embeddings) text-embedding-3-small model is 8,191 tokens. Given that each token is around four characters of text for common OpenAI models, this maximum limit is equivalent to around 6,000 words of text. If you're using these models to generate embeddings, it's critical that the input text stays under the limit. 
 
-Chat completion models have the same input token restrictions, so chunking is helpful for retrieval augmented generation (RAG) or agentic retrieval as well. Partitioning your content into chunks helps you meet input token requirements and prevents data loss due to truncation.
+Chat completion models have the same input token restrictions, so chunking is helpful for [retrieval augmented generation (RAG)](retrieval-augmented-generation-overview.md) or [agentic retrieval](agentic-retrieval-overview.md) as well. Partitioning your content into chunks helps you meet input token requirements and prevents data loss due to truncation.
 
 Azure AI Search has built-in solutions for chunking content, and also for vectorizing chunked content if you're using vector search. The built-in approach takes a dependency on [built-in indexers](search-indexer-overview.md) and [skillsets](vector-search-integrated-vectorization.md) that enable text splitting and embeddings generation. If you can't use integrated vectorization, this article describes some alternative approaches for chunking your content.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書のチャンク処理に関するタイトルの修正"
}
```

### Explanation
この変更では、Azure AI Searchに関する文書のタイトルが更新され、コンテンツのチャンク処理に関連する表現が改善されました。具体的には、「エージェンティック検索とベクター検索のための大きな文書をチャンク化」というタイトルが「RAGおよびベクター検索のための大きな文書をチャンク化」という表現に変更されました。

この修正により、文書の主題がより明確になり、特に「RAG（Retrieval Augmented Generation）」の観点が強調されています。また、チャンク化の目的や重要性について説明するテキストに変更はありませんが、改良されたタイトルがより正確な内容を反映するようになっています。全体として、この更新は、読者が文書の内容を迅速に理解しやすくすることを目的としています。


