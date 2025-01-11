---
date: '2025-01-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1227d31...MicrosoftDocs:28bc1fd
summary: この変更では、ベクトル検索のインデックスサイズとインデックス作成に関連する機能が追加され、文書が更新されました。新たにアルゴリズム別のインデックスサイズを示す画像「vector-index-size-by-algorithm.png」が追加され、関連するドキュメントの内容が最新化され、より明確で一貫性のあるものとなりました。破壊的変更はありません。これにより、ユーザーはベクトル検索機能を効果的に利用でき、リソースの管理が向上することが期待されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1227d31...MicrosoftDocs:28bc1fd){target="_blank"}

# ハイライト

この変更では、ベクトル検索のインデックスサイズおよびインデックス作成に関連する新機能とマイナーなドキュメントの更新が行われました。新しい画像「vector-index-size-by-algorithm.png」が追加され、ベクトル検索の方法に関するドキュメント（「vector-search-how-to-create-index.md」と「vector-search-index-size.md」）の情報が最新化されました。

## 新機能
- 新しい画像「vector-index-size-by-algorithm.png」を追加し、アルゴリズムによるベクトル検索インデックスサイズを視覚的に示しています。

## 破壊的変更
- 破壊的変更は特にありません。

## その他の更新
- ベクトル検索インデックス作成に関するドキュメントが更新され、内容がより明確で一貫性のあるものになりました。
- ベクトルインデックスのサイズと関連制約についてのドキュメントが改善されました。

# インサイト

この変更は、ベクトル検索におけるインデックスサイズおよびインデックス作成プロセスに関する明確な情報を提供することを目的としています。特に、アルゴリズム別のインデックスサイズを示す新しい画像の追加により、ユーザーは視覚的に情報を理解しやすくなります。画像は、技術的な概念を簡単に伝えるための有用なツールであり、このような追加はしばしば複雑な情報を直感的に理解するのに役立ちます。

ドキュメントの更新部分では、主にMDS（Minimum Data Set）に関する情報や技術的説明が見直されています。ベクトル検索は、高度な検索機能を提供するため、適切なインデックス管理が重要です。新しい情報に基づいて、インデックスがどのようにメモリやディスクに影響を与えるのか、また使用するアルゴリズムによって異なる点がどのように管理されるのかが明確化されました。例えば、HNSWアルゴリズムに関する説明の追加は、ユーザーが実際にシステムがどのようにリソースを使用するかを理解するのに役立ちます。

全体として、この一連の更新は、ユーザーが効果的にベクトル検索機能を利用し、リソースをより賢く管理するための重要なガイドラインを提供しています。これにより、開発者や技術者がより良い意思決定を行いやすくなることが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [vector-index-size-by-algorithm.png](#item-45e62a) | new feature | ベクトル検索インデックスサイズのアルゴリズムに関する画像の追加 | added | 0 | 0 | 0 | 
| [vector-search-how-to-create-index.md](#item-97c769) | minor update | ベクトル検索のインデックス作成に関するドキュメントの更新 | modified | 7 | 7 | 14 | 
| [vector-search-index-size.md](#item-bb2846) | minor update | ベクトル検索インデックスサイズに関するドキュメントの更新 | modified | 16 | 3 | 19 | 


# Modified Contents
## articles/search/media/vector-search-index-size/vector-index-size-by-algorithm.png{#item-45e62a}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ベクトル検索インデックスサイズのアルゴリズムに関する画像の追加"
}
```

### Explanation
このコードの変更は、新しい画像ファイルの追加を示しています。ファイル名は「vector-index-size-by-algorithm.png」であり、リポジトリ内の特定のパスに追加されました。この画像は、ベクトル検索のインデックスサイズに関連する情報を視覚的に提供するために使用される可能性があります。この変更には、他のコードやファイルの追加、削除、変更は含まれていません。新しい画像を追加することにより、リーダーが概念をより理解しやすくなることが期待されます。

## articles/search/vector-search-how-to-create-index.md{#item-97c769}

<details>
<summary>Diff</summary>
````diff
@@ -30,13 +30,13 @@ This article explains the workflow and uses REST for illustration. Once you unde
 
 ## Prerequisites
 
-+ Azure AI Search, in any region and on any tier. Most existing services support vector search. For services created before January 2019, there's a small subset that can't create a vector index. In this situation, a new service must be created. If you're using integrated vectorization (skillsets that call Azure AI), Azure AI Search must be in the same region as Azure OpenAI or Azure AI services.
++ Azure AI Search, in any region and on any tier. On services created before January 2019, there's a small subset that can't create a vector index. If this applies to you, create a new service to use vectors. For indexing workloads that include integrated vectorization (skillsets that call Azure AI), Azure AI Search must be in the same region as Azure OpenAI or Azure AI services.
 
-+ [Pre-existing vector embeddings](vector-search-how-to-generate-embeddings.md) or use [integrated vectorization](vector-search-integrated-vectorization.md), where embedding models are called from the indexing pipeline.
++ You must have [pre-existing vector embeddings](vector-search-how-to-generate-embeddings.md) to upload to the index, or you can use [integrated vectorization](vector-search-integrated-vectorization.md), where embedding models are called from a skillset in an indexer pipeline.
 
-+ You should know the dimensions limit of the model used to create the embeddings. Valid values are 2 through 3072 dimensions. In Azure OpenAI, for **text-embedding-ada-002**, the length of the numerical vector is 1536. For **text-embedding-3-small** or **text-embedding-3-large**, the vector length is 3072. 
++ You should know the dimensions limit of the model used to create the embeddings so that you can assign that limit to the vector field. Integrated vectorization supports a finite number of embedding models. For **text-embedding-ada-002**, dimensions are fixed at 1536. For **text-embedding-3-small** or **text-embedding-3-large**, the vector length ranges from 1 to 1536 and 3072, respectively. 
 
-+ You should also know what the supported similarity metrics are. For Azure OpenAI, similarity is [computed using `cosine`](/azure/ai-services/openai/concepts/understand-embeddings#cosine-similarity). 
++ You should also know what similarity metric to use. For embedding models on Azure OpenAI, similarity is [computed using `cosine`](/azure/ai-services/openai/concepts/understand-embeddings#cosine-similarity). 
 
 + You should be familiar with [creating an index](search-how-to-create-search-index.md). The schema must include a field for the document key, other fields you want to search or filter, and other configurations for behaviors needed during indexing and queries. 
 
@@ -50,9 +50,9 @@ Make sure your documents:
 
 1. Provide vector data (an array of single-precision floating point numbers) in source fields.
 
-   Vector fields contain an array generated by embedding models, one embedding per field, where the field is a top-level field (not part of a nested or complex type). For the simplest integration, we recommend the embedding models in [Azure OpenAI](https://aka.ms/oai/access), such as **text-embedding-ada-002** for text documents or the [Image Retrieval REST API](/rest/api/computervision/2023-02-01-preview/image-retrieval/vectorize-image) for images.
+   Vector fields contain an array generated by embedding models, one embedding per field, where the field is a top-level field (not part of a nested or complex type). For the simplest integration, we recommend the embedding models in [Azure OpenAI](https://aka.ms/oai/access), such as a **text-embedding-3** model for text documents or the [Image Retrieval REST API](/rest/api/computervision/2023-02-01-preview/image-retrieval/vectorize-image) for images.
 
-   If you can take a dependency on indexers and skillsets, consider using [integrated vectorization](vector-search-integrated-vectorization.md) that encodes images and textual content during indexing. Your field definitions are for vector fields, but incoming source data can be text or images, represented as vector arrays created during indexing.
+   If you can take a dependency on indexers and skillsets, consider using [integrated vectorization](vector-search-integrated-vectorization.md) that encodes images and textual content during indexing. Your field definitions are for vector fields, but incoming source data can be text or images, which are converted to vector arrays during indexing.
 
 1. Provide other fields with human-readable content for the query response, and for hybrid query scenarios that include full text search or semantic ranking in the same request. 
 
@@ -69,7 +69,7 @@ A vector configuration specifies the parameters used during indexing to create "
 
 If you choose HNSW on a field, you can opt in for exhaustive KNN at query time. But the other direction doesn’t work: if you choose exhaustive, you can’t later request HNSW search because the extra data structures that enable approximate search don’t exist.
 
-A vector configuration also specifies quantization methods for reducing vector size:
+Optionally, a vector configuration also specifies quantization methods for reducing vector size:
 
 + Scalar
 + Binary (available in 2024-07-01 only and in newer Azure SDK packages)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のインデックス作成に関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、「vector-search-how-to-create-index.md」というドキュメントの修正を示しています。具体的には、追加された点が7つ、削除された点も7つあり、合計14の変更が行われました。この更新では、主にインデックス作成に関する前提条件や技術的な説明が見直され、より明確で一貫性のある表現に改善されています。

変更内容の一部には、旧サービスに関する情報の簡略化、新しいサービス作成の必要性に関する説明の再構成、埋め込みモデルの詳細情報の更新が含まれています。具体的には、埋め込みモデルの次元数や使用する類似性メトリックについての説明が更新されました。また、インデックスの作成方法に関する内容も追加され、読者が理解しやすいように工夫されています。

全体として、このドキュメントはベクトル検索のインデックス作成に関するガイドラインを最新の情報に基づいて改善し、ユーザーがより効果的にこの機能を利用できるようにしています。

## articles/search/vector-search-index-size.md{#item-bb2846}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: conceptual
-ms.date: 09/19/2024
+ms.date: 01/09/2025
 ---
 
 # Vector index size and staying under limits
@@ -27,7 +27,7 @@ For each vector field, Azure AI Search constructs an internal vector index using
 
 + Vector index size is measured in bytes.
 
-+ Vector quotas are based on memory constraints. All searchable vector indexes must be loaded into memory. At the same time, there must also be sufficient memory for other runtime operations. Vector quotas exist to ensure that the overall system remains stable and balanced for all workloads.
++ Vector quotas are based on memory constraints. For vector indexes created using the Hierarchical Navigable Small World (HNSW) algorithm, searchable vector indexes reside in memory. At the same time, there must also be sufficient memory for other runtime operations. Vector quotas exist to ensure that the overall system remains stable and balanced for all workloads. If you use exhaustive KNN algorithm, indexes are loaded into memory only at query time.
 
 + Vector indexes are also subject to disk quota, in the sense that all indexes are subject disk quota. There's no separate disk quota for vector indexes.
 
@@ -67,11 +67,24 @@ A request for vector metrics is a data plane operation. You can use the Azure po
 
 ### [**Portal**](#tab/portal-vector-quota)
 
-Usage information can be found on the **Overview** page's **Usage** tab. Portal pages refresh every few minutes so if you recently updated an index, wait a bit before checking results.
+#### Vector size per index
+
+To get vector index size per index, select **Search management** > **Indexes** to view a list of indexes and the document count, the size of in-memory vector indexes, and total index size as stored on disk.
+
+Recall that vector quota is based on memory constraints. For vector indexes created using the HNSW algorithm, all searchable vector indexes are permanently loaded into memory. For indexes created using the exhaustive KNN algorithm, vector indexes are loaded in chunks, sequentially, during query time. There's no memory residency requirement for exhaustive KNN indexes. The lifetime of the loaded pages in memory is similar to text search and there are no other metrics applicable to exhaustive KNN indexes other than total storage. 
+
+The following screenshot shows two versions of the same vector index. One version is created using HNSW algorithm, where the vector graph is memory resident. Another version is created using exhaustive KNN algorithm. With exhaustive KNN, there's no specialized in-memory vector index, so the portal shows 0 MB for vector index size. Those vectors still exist and are counted in overall storage size, but they don’t occupy the in-memory resource that the vector index size metric is tracking.
+
+:::image type="content" source="media/vector-search-index-size/vector-index-size-by-algorithm.png" lightbox="media/vector-search-index-size/vector-index-size-by-algorithm.png" alt-text="Screenshot of the index portal page showing vector index size based on different algorithms.":::
+
+#### Vector size per service
+
+To get vector index size for the search service as a whole, select the **Overview** page's **Usage** tab. Portal pages refresh every few minutes so if you recently updated an index, wait a bit before checking results.
 
 The following screenshot is for an older Standard 1 (S1) search service, configured for one partition and one replica. 
 
 + Storage quota is a disk constraint, and it's inclusive of all indexes (vector and nonvector) on a search service.
+
 + Vector index size quota is a memory constraint. It's the amount of memory required to load all internal vector indexes created for each vector field on a search service. 
 
 The screenshot indicates that indexes (vector and nonvector) consume almost 460 megabytes of available disk storage. Vector indexes consume almost 93 megabytes of memory at the service level. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索インデックスサイズに関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、「vector-search-index-size.md」というドキュメントの修正を示しており、合計で16か所の追加、3か所の削除が行われました。変更の主な内容は、ベクトルインデックスのサイズと関連する制約に関する説明を最新の情報に基づいて改善することです。

具体的には、ベクトルインデックスのサイズがバイト単位で測定されることが明確にされ、HNSWアルゴリズムを使用して作成されたインデックスがメモリに常駐することや、高忠実度のKNNアルゴリズムではクエリ時にのみインデックスがメモリに読み込まれることが説明されています。また、ベクトルインデックスがディスクのクォータに影響を受けることも記載され、メモリとディスクの制約が明確に示されています。

さらに、インデックスのサイズに関するポータルでの情報取得方法や、異なるアルゴリズムでのベクトルインデックスのサイズの違いについての具体的な説明が追加されています。この更新により、ユーザーはベクトルインデックスの制約やサイズの管理がより理解しやすくなり、適切にリソースを計画できるようになります。


