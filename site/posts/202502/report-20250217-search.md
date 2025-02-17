---
date: '2025-02-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1cff62f...MicrosoftDocs:caf7737
summary: |-
  この変更に関する概要は、主に情報の明確化に焦点を当てています。新機能は特に追加されていませんが、既存の情報に対する説明がより分かりやすくなりました。APIリクエストの方法についても、明確な指示が提供されています。

  この更新は、Azureの検索APIのドキュメントを直感的にし、技術者が迅速に最新の推奨事項を把握できることを目的としています。具体的には、`listQueryKeys`に関する用語が明確化され、インデックススキーマの詳細な説明と、Azure OpenAIの推奨が追加されました。このようにして、情報へのアクセスのしやすさと技術的な精度の向上を図っています。技術者にとって重要な情報が含まれており、特にAzure AIや検索に関わる方々にとって有益です。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1cff62f...MicrosoftDocs:caf7737){target="_blank"}

# Highlights

## 新機能
特に新機能は追加されていませんが、既存の情報に関する説明が明確化されたことが挙げられます。

## 破壊的変更
破壊的な変更はありませんが、使用するAPIリクエストの方法に関する明示的な説明があります。

## その他の更新
- `listQueryKeys`に関する用語の明確化とリンク追加。
- インデックススキーマの説明が向上。
- ベクトルコンテンツに関するAzure OpenAIの推奨が具体化。

# Insights
この更新は、Azureの検索APIのマイグレーションとベクトル検索インデックス作成に関するドキュメントを、より直感的で理解しやすいものにすることを目的としています。ここで重要なのは、技術的な正確性と情報へのアクセスのしやすさを改善することにより、開発者が最新の推奨事項を迅速に把握できるようにしている点です。

まず、検索APIのドキュメントでは、`listQueryKeys`に関する説明が更新されました。特に、推奨される最新のドキュメントへのリンクを追加することで、開発者が最新情報を用いた適切なAPI使用をサポートしています。さらに、リクエストの方法が`GET`から`POST`に変わることを明示し、誤った理解を防いでいます。

次に、ベクトル検索のインデックス作成に関する記述では、インデックススキーマについての具体的な説明が増加しました。このような情報の提供により、開発者は自らのプロジェクトに最適なベクトル配置やアルゴリズムの選択が可能になっています。また、Azure OpenAIの埋め込みモデルに関する具体的な推奨を示すことで、ベクトルコンテンツの取り扱いにおいて一貫したアプローチを採用できるよう配慮されています。

これらの更新は、技術者が最新のベストプラクティスを効率的に取り入れられるようにし、最終的には開発の迅速化と精度の向上を実現するものです。特にAzure AIや検索に関わる技術者には重要な情報が多数含まれており、このドキュメント改訂に注目する価値があります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-api-migration.md](#item-07297b) | minor update | 検索APIマイグレーションに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [vector-search-how-to-create-index.md](#item-97c769) | minor update | ベクトル検索インデックス作成に関するドキュメントの更新 | modified | 7 | 7 | 14 | 


# Modified Contents
## articles/search/search-api-migration.md{#item-07297b}

<details>
<summary>Diff</summary>
````diff
@@ -429,11 +429,11 @@ You can update flat indexes to the new format with the following steps using API
 
 **Applies to:** `2014-07-31-Preview`, `2015-02-28`, and `2015-08-19`
 
-The `listQueryKeys` GET request on older Search Management API versions is now deprecated. We recommend migrating to the most recent stable control plane API version to use the `listQueryKeys` POST request.
+The `listQueryKeys` GET request on older Search Management API versions is now deprecated. We recommend migrating to the most recent stable control plane API version to use the [`listQueryKeys` POST request](/rest/api/searchmanagement/query-keys/list-by-search-service).
 
 1. In existing code, change the `api-version` parameter to the most recent version (`2023-11-01`).
 
-1. Refactor the request from `GET` to `POST`:
+1. Reframe the request from `GET` to `POST`:
 
    ```http
    POST https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}/listQueryKeys?api-version=2023-11-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索APIマイグレーションに関するドキュメントの更新"
}
```

### Explanation
この変更は、検索APIのマイグレーションに関するドキュメントにおける用語の明確化と誤解を招かないようにするための軽微な更新です。具体的には、`listQueryKeys`のリクエストに関する部分が修正されており、POSTリクエストに関するリンクが追加されました。これにより、読者は推奨される最新のAPIドキュメントに直接アクセスできるようになっています。また、`GET`から`POST`にリクエストの処理方法が変更されることを示す文言も若干の文面変更が行われました。このような更新は、APIの使用方法をより理解しやすくし、適切な実装を促すことを目的としています。

## articles/search/vector-search-how-to-create-index.md{#item-97c769}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.date: 02/14/2025
 
 # Create a vector index
 
-In Azure AI Search, you can store vectors in a search index and send vector queries to match on semantic similarity. A vector store in Azure AI Search has an index schema that defines both vector and nonvector fields. It also has a vector configuration for algorithms used to create and compress the embedding space.
+In Azure AI Search, you can store vectors in a search index and send vector queries to match on semantic similarity. A vector store in Azure AI Search is defined by an index schema that has both vector and nonvector fields. The schema also has a vector configuration for specifying the algorithms used to create and compress the embedding space.
 
 [Create or Update Index API](/rest/api/searchservice/indexes/create-or-update) creates the vector store. Follow these steps to index vectors in Azure AI Search:
 
@@ -49,13 +49,13 @@ For search services created before January 2019, there's a small subset that can
 
 Before indexing, assemble a document payload that includes fields of vector and nonvector data. The document structure must conform to the index schema. 
 
-Make sure your documents provide the following content:
+Make sure your source documents provide the following content:
 
 | Content | Description |
 |---------|-------------|
 | Unique identifier | A field or a metadata property that uniquely identifies each document. All search indexes require a document key. To satisfy document key requirements, a source document must have one field or property uniquely identifies it in the index. If you're indexing blobs, it might be the metadata_storage_path that uniquely identifies each blob. If you're indexing from a database, it might be primary key. This source field must be mapped to an index field of type `Edm.String` and `key=true` in the search index.|
 | Non-vector content | Provide other fields with human-readable content. Human readable content is useful for the query response, and for hybrid query scenarios that include full text search or semantic ranking in the same request. If you're using a chat completion model, most models like ChatGPT don't accept raw vectors as input. |
-| Vector content| A vectorized version of your non-vector content. A vector is an array of single-precision floating point numbers generated by an embedding model. Each vector field contains an array generated by an embedding model, one embedding per field, where the field is a top-level field (not part of a nested or complex type). For the simplest integration, we recommend the embedding models in [Azure OpenAI](https://aka.ms/oai/access), such as an **text-embedding-3** model for text documents or the [Image Retrieval REST API](/rest/api/computervision/image-retrieval/vectorize-image) for images. <br><br>If you can take a dependency on indexers and skillsets, consider using [integrated vectorization](vector-search-integrated-vectorization.md) that encodes images and textual content during indexing. Your field definitions are for vector fields, but incoming source data can be text or images, which are converted to vector arrays during indexing. |
+| Vector content| A vectorized version of your non-vector content. A vector is an array of single-precision floating point numbers generated by an embedding model. Each vector field contains an array generated by an embedding model, one embedding per field, where the field is a top-level field (not part of a nested or complex type). For the simplest integration, we recommend the embedding models in [Azure OpenAI](https://aka.ms/oai/access), such as a **text-embedding-3** model for text documents or the [Image Retrieval REST API](/rest/api/computervision/image-retrieval) for images and multimodal embeddings. <br><br>If you can take a dependency on indexers and skillsets, consider using [integrated vectorization](vector-search-integrated-vectorization.md) that encodes images and textual content during indexing. Your field definitions are for vector fields, but incoming source data can be text or images, which are converted to vector arrays during indexing. |
 
 Your search index should include fields and content for all of the query scenarios you want to support. Suppose you want to search or filter over product names, versions, metadata, or addresses. In this case, vector similarity search isn't especially helpful. Keyword search, geo-search, or filters would be a better choice. A search index that includes a comprehensive collection of both vector and nonvector fields provides maximum flexibility for query construction and response composition.
 
@@ -84,7 +84,7 @@ POST https://[servicename].search.windows.net/indexes?api-version=[api-version]
 
 ## Add a vector search configuration
 
-Next, add a vector search configuration to your schema. Configuration occurs before field definitions because you specify one on each field as part of its definition. In the schema, vector configuration is typically added after the fields collection, perhaps after `"suggesters"`, `"scoringProfiles"`, or `"analyzers"`.
+Next, add a vector search configuration (profile) to your schema. Configuration occurs before field definitions because you specify a profile on each field as part of its definition. In the schema, vector configuration is typically added after the fields collection, perhaps after `"suggesters"`, `"scoringProfiles"`, or `"analyzers"`.
 
 A vector configuration specifies the parameters used during indexing to create "nearest neighbor" information among the vector nodes. Algorithms include:
 
@@ -175,15 +175,15 @@ Be sure to have a strategy for [vectorizing your content](vector-search-how-to-g
 
    + Names for each configuration of compression, algorithm, and profile must be unique for its type within the index.
 
-   + `vectorSearch.compressions.kind` can be `scalarQuantization` or `binaryQuantization`.
+   + `vectorSearch.compressions` can be `scalarQuantization` or `binaryQuantization`. Scalar quantization compresses float values into narrower data types. Binary quantization converts floats into binary 1 bit values.
 
    + `vectorSearch.compressions.rerankWithOriginalVectors` uses the original, uncompressed vectors to recalculate similarity and rerank the top results returned by the initial search query. The uncompressed vectors exist in the search index even if `stored` is false. This property is optional. Default is true.
 
    + `vectorSearch.compressions.defaultOversampling` considers a broader set of potential results to offset the reduction in information from quantization. The formula for potential results consists of the `k` in the query, with an oversampling multiplier. For example, if the query specifies a `k` of 5, and oversampling is 20, then the query effectively requests 100 documents for use in reranking, using the original uncompressed vector for that purpose. Only the top `k` reranked results are returned. This property is optional. Default is 4.
 
    + `vectorSearch.compressions.scalarQuantizationParameters.quantizedDataType` must be set to `int8`. This is the only primitive data type supported at this time. This property is optional. Default is `int8`.
 
-   + `vectorSearch.algorithms.kind` are either `"hnsw"` or `"exhaustiveKnn"`. These are the Approximate Nearest Neighbors (ANN) algorithms used to organize vector content during indexing.
+   + `vectorSearch.algorithms` are either `"hnsw"` or `"exhaustiveKnn"`. These are the Approximate Nearest Neighbors (ANN) algorithms used to organize vector content during indexing.
 
    + `vectorSearch.algorithms.m` is the bi-directional link count. Default is 4. The range is 4 to 10. Lower values should return less noise in the results.
  
@@ -290,7 +290,7 @@ For more information about new preview features, see [What's new in Azure AI Sea
 
 ## Add a vector field to the fields collection
 
-The fields collection must include a field for the document key, vector fields, and any other fields that you need for hybrid search scenarios.
+Once you have a vector configuration, you can add a vector field to the fields collection. Recall that the fields collection must include a field for the document key, vector fields, and any other non-vector fields that you need for hybrid search scenarios or chat model completion in [RAG workloads](retrieval-augmented-generation-overview.md).
 
 Vector fields are characterized by [their data type](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields), a `dimensions` property based on the embedding model used to output the vectors, and a vector profile that you created in a previous step.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索インデックス作成に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるベクトル検索インデックスの作成方法に関するドキュメントを更新するための軽微な修正です。主な変更点は、用語の明確化と正確な説明の強化です。特に、インデックススキーマに関する記述が改善され、ベクトル配置やアルゴリズムの指定方法がより具体的に述べられています。

さらに、文中の「文書」が「ソース文書」に修正され、ソースデータやハイブリッド検索シナリオに必要なフィールドについての説明も強化されました。また、ベクトルコンテンツの取得に関して、Azure OpenAIの埋め込みモデルの推奨が具体化され、情報の一貫性と理解のしやすさが向上しています。このような更新により、開発者は最新のベクトル検索機能を利用する際の注意事項や推奨事項をよりよく理解できるようになります。


