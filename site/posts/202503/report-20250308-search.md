---
date: '2025-03-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4d90f76...MicrosoftDocs:c05f6ab
summary: これらの変更は、ハイブリッド検索とベクトル検索に関する技術的な説明をより明確にし、正確な利用ガイダンスを提供することを目的としています。主な内容としては、ハイブリッド検索のRRFアルゴリズムにおけるスコア計算の訂正、新しいストレージオプションやインデックスサイズに関する情報の追加があります。また、特に開発者やデータエンジニアに対し、リソース管理やコスト削減の最適化に関する有益な指針を提供しています。全体的に、Azureプラットフォーム上での検索機能の効率を向上させるための取り組みです。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4d90f76...MicrosoftDocs:c05f6ab){target="_blank"}

# Highlights

これらの変更は、ハイブリッド検索及びベクトル検索における技術的な説明を明確化し、より正確な利用ガイダンスを提供することを目的としています。特に、ハイブリッド検索のRRFアルゴリズムのスコア計算方法の訂正、ベクトル検索のストレージオプションおよびインデックスサイズに関する情報の追加と修正が行われています。

## New features
- ベクトル検索における新しいストレージオプション
- APIバージョン2024-11-01-previewを用いたストレージコスト削減の説明
- ベクトル圧縮技術に関する新たな情報

## Breaking changes
- 特になし

## Other updates
- ハイブリッド検索におけるRRFアルゴリズムの解釈の訂正
- ベクトル検索のストレージオプションにおける詳細な説明と新セクション追加
- インデックスサイズの計算方法と効率的なリソース管理に関する情報の追加

# Insights

これらの変更は、主にAzure AI Searchを用いる開発者やデータエンジニアに対して、より精密な技術指針を提供するために実施されたものです。ハイブリッド検索では、RRF（Rank-Rank Fusion）アルゴリズムのスコア計算における誤解を訂正し、それぞれのクエリが具体的にどの程度スコアに影響を与えるのかを正しく説明することで、開発者がアルゴリズムをより効果的に活用できるよう支援しています。

一方、ベクトル検索に関しては、ストレージの選択肢とその影響を扱った内容が強化されました。特に新しいAPIバージョンに関連したストレージコストの最適化や圧縮技術についての情報が追加され、これによりストレージ資源の効率が向上する可能性が示されています。

また、ベクトル検索のインデックスサイズについての詳細な記述により、HNSWアルゴリズムのメモリオーバーヘッドやベクトル圧縮がどのようにインデックスサイズに影響するかが明確になり、これにより開発者はデプロイ時のパフォーマンスとリソース管理においてより賢明な選択を行うことが可能となります。

このように、これらの修正と追加情報は、Azureプラットフォーム上での検索機能の利用効率を向上させるものです。特に大規模なデータセットを扱う際、コストとパフォーマンスを最適化するための有益な指針を提供しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [hybrid-search-ranking.md](#item-dad887) | minor update | ハイブリッド検索のRRFアルゴリズムに関する説明の修正 | modified | 1 | 1 | 2 | 
| [vector-search-how-to-storage-options.md](#item-ee1680) | minor update | ベクトル検索のストレージオプションに関する詳細の追加 | modified | 12 | 5 | 17 | 
| [vector-search-index-size.md](#item-bb2846) | minor update | ベクトル検索インデックスサイズに関する詳細なガイダンスの更新 | modified | 20 | 17 | 37 | 


# Modified Contents
## articles/search/hybrid-search-ranking.md{#item-dad887}

<details>
<summary>Diff</summary>
````diff
@@ -55,7 +55,7 @@ The following chart identifies the scoring property returned on each match, algo
 |---------------|-----------|-------------------|-------|
 | full-text search | `@search.score` | BM25 algorithm | No upper limit. |
 | vector search | `@search.score` | HNSW algorithm, using the similarity metric specified in the HNSW configuration. | 0.333 - 1.00 (Cosine), 0 to 1 for Euclidean and DotProduct. | 
-| hybrid search | `@search.score` | RRF algorithm | Upper limit is bounded by the number of queries being fused, with each query contributing a maximum of approximately 1 to the RRF score. For example, merging three queries would produce higher RRF scores than if only two search results are merged. |
+| hybrid search | `@search.score` | RRF algorithm | Upper limit is bounded by the number of queries being fused, with each query contributing a maximum of approximately `1/k` to the RRF score (this is the `k` parameter in the RRF algorithm, not the vector query). For example, merging three queries would produce higher RRF scores than if only two search results are merged. |
 | semantic ranking | `@search.rerankerScore` | Semantic ranking | 0.00 - 4.00 |
 
 Semantic ranking occurs after RRF merging of results. Its score (`@search.rerankerScore`) is always reported separately in the query response. Semantic ranker can rerank full text and hybrid search results, assuming those results include fields having semantically rich content. It can rerank pure vector queries if the search documents include text fields that contain semantically relevant content.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索のRRFアルゴリズムに関する説明の修正"
}
```

### Explanation
この変更は、ハイブリッド検索のRRFアルゴリズムに関する文書の一部であり、具体的にはRRFスコアに関する情報の修正を含みます。元の記述では、各クエリがRRFスコアにおいて最大約1を寄与すると説明されていましたが、新しい説明では、各クエリがRRFスコアに最大で約`1/k`を寄与することが正確に示されています。この`k`はRRFアルゴリズムに特有のパラメータであり、ベクトルクエリとは関連がありません。また、三つのクエリを結合することが、二つの検索結果を結合するよりも高いRRFスコアを生むことの例も提供されています。この小さな変更は、ハイブリッド検索の機能をより正確に理解するために重要です。

## articles/search/vector-search-how-to-storage-options.md{#item-ee1680}

<details>
<summary>Diff</summary>
````diff
@@ -26,13 +26,20 @@ For every vector field, there could be three copies of the vectors, each serving
 
 | Instance | Usage | Controlled using |
 |----------|-------|------------|
-| Source vectors which store the JSON that was received during document indexing | Used for incremental data refresh with `merge` or `mergeOrUpload` during document indexing. Also used if you want "retrievable" vectors returned in the query response. | `stored` property on vector fields |
-| Original full-precision vectors | In existing indexes, these are used for internal index operations and for exhaustive KNN search. For vectors using compression, it's also used for rescoring (if enabled) on an oversampled candidate set of results from ANN search on vector fields using [scalar or binary quantization](vector-search-how-to-quantization.md) compression. | `rescoringOptions.rescoreStorageMethod` property in `vectorSearch.compressions`. For *uncompressed* vector fields on indexes created with `2024-11-01-Preview` API versions and later, this will be omitted by default with no impact on search activities nor quality. |
-| Vectors in the [HNSW graph for Approximate Nearest Neighbors (ANN) search](vector-search-overview.md) | Used for ANN query execution. Consists of either full-precision vectors (when no compression is applied) or quantized vectors (when compression is applied) | Only applies to HNSW. These data structures are required for efficient ANN search. |
+| Source vectors which store the JSON that was received during document indexing (JSON data) | Used for incremental data refresh with `merge` or `mergeOrUpload` during document indexing. Also used if you want "retrievable" vectors returned in the query response. | `stored` property on vector fields |
+| Original full-precision vectors (binary data) | In existing indexes, these are used for internal index operations and for exhaustive KNN search. For vectors using compression, it's also used for rescoring (if enabled) on an oversampled candidate set of results from ANN search on vector fields using [scalar or binary quantization](vector-search-how-to-quantization.md) compression. | `rescoringOptions.rescoreStorageMethod` property in `vectorSearch.compressions`. For *uncompressed* vector fields on indexes created with `2024-11-01-Preview` API versions and later, this will be omitted by default with no impact on search activities nor quality. |
+| Vectors in the [HNSW graph for Approximate Nearest Neighbors (ANN) search](vector-search-overview.md) (HNSW graph) | Used for ANN query execution. Consists of either full-precision vectors (when no compression is applied) or quantized vectors (when compression is applied) | Only applies to HNSW. These data structures are required for efficient ANN search. |
 
-You can set properties that permanently discard the first two instances from vector storage.
+You can set properties that permanently discard the first two instances (JSON data and binary data) from vector storage.
 
-The last instance (vectors and graph) is required for ANN vector query execution. If any compression techniques such as [scalar or binary quantization](vector-search-how-to-quantization.md) are used, they would be applied to this set of data. If you want to offset lossy compression, you should keep the second instance for rescoring purposes to improve ANN search quality.
+The last instance (HNSW graph) is required for ANN vector query execution. If any compression techniques such as [scalar or binary quantization](vector-search-how-to-quantization.md) are used, they are applied to this set of data. If you want to offset lossy compression, you should keep the second instance (binary data) for rescoring purposes to improve ANN search quality.
+
+### Indexes created on or after 2024-11-01-preview API version
+For indexes created with the 2024-11-01-preview API version with uncompressed vector fields, the second and third instances (binary data and HNSW graph) are combined as part of our cost reduction investments, reducing overall storage. The same index created with the 2024-11-01-preview API is functionally equivalent but uses less storage compared to identical indexes created with earlier API versions. Physical data structures are established on a Create Index request, so you must delete and recreate the index to realize the storage reductions.
+
+If you choose to use [vector compression](vector-search-how-to-configure-compression-storage.md), we compress (quantize) the in-memory portion of the vector index. Since memory is often a primary constraint for vector indexes, this allows storing more vectors within the same search service. However, lossy compression results in some information loss, which can impact search quality.
+
+To mitigate this, enabling "rescoring" and "oversampling" helps maintain accuracy. This retrieves a larger set of candidate documents from the compressed index and then recomputes similarity scores using the original vectors, which must be retained in storage. As a result, while quantization reduces memory usage (vector index size usage), it slightly increases storage requirements since both compressed and original vectors are stored. The additional storage is approximately equal to the size of the compressed index.
 
 ## Set the `stored` property
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のストレージオプションに関する詳細の追加"
}
```

### Explanation
この変更は、ベクトル検索のストレージオプションに関する文書の改善を目的としています。主に、ストレージの各インスタンスに関連する詳細が追加され、より明確な説明が提供されています。具体的には、ソースベクトルの形式（JSONデータおよびバイナリデータ）、元のフルプレシジョンベクトル、HNSWグラフの役割が強調されています。また、2024年11月1日以降に作成されたインデックスに関する情報や、圧縮ベクトルに関する新しいセクションも追加されています。

新しい情報には、特にAPIバージョン2024-11-01-previewを使用して作成されたインデックスでは、ストレージのコスト削減が図られ、物理データ構造の削減が行われることが説明されています。さらに、ベクトル圧縮とリスコアリングに関する内容も追加されており、メモリの使用量が削減される一方で、オリジナルのベクトルを保持する必要性も指摘されています。このように、ストレージオプションの機能とそれに伴う利点・欠点についての理解が深まる内容となっています。

## articles/search/vector-search-index-size.md{#item-bb2846}

<details>
<summary>Diff</summary>
````diff
@@ -21,17 +21,18 @@ For each vector field, Azure AI Search constructs an internal vector index using
 > A note about terminology. Internally, the physical data structures of a search index include raw content (used for retrieval patterns requiring non-tokenized content), inverted indexes (used for searchable text fields), and vector indexes (used for searchable vector fields). This article explains the limits for the internal vector indexes that back each of your vector fields.
 
 > [!TIP]
-> [Vector optimization techniques](vector-search-how-to-configure-compression-storage.md) are now generally available. Use capabilities like narrow data types, scalar and binary quantization, and elimination of redundant storage to stay under vector quota and storage quota.
+> [Vector optimization techniques](vector-search-how-to-configure-compression-storage.md) are now generally available. Use capabilities like narrow data types, scalar and binary quantization, and elimination of redundant storage to reduce your vector quota and storage quota consumption.
+
+> [!NOTE]
+> Not all algorithms consumes vector index size quota. Vector quotas are established based on memory requirements of approximate nearest neighbor search. Vector fields created with the Hierarchical Navigable Small World (HNSW) algorithm need to reside in memory during query execution because of the random-access nature of graph-based traversals. Vector fields using exhaustive KNN algorithm are loaded into memory dynamically in pages during query execution, and as a result do not consume vector quota.
 
 ## Key points about quota and vector index size
 
 + Vector index size is measured in bytes.
 
-+ Vector quotas are based on memory constraints. For vector indexes created using the Hierarchical Navigable Small World (HNSW) algorithm, searchable vector indexes reside in memory. At the same time, there must also be sufficient memory for other runtime operations. Vector quotas exist to ensure that the overall system remains stable and balanced for all workloads. If you use exhaustive KNN algorithm, indexes are loaded into memory only at query time.
++ The total storage of your service contains all of your vector index files. Azure AI Search maintains different copies of vector index files for different purposes. We offer additional options to reduce the [storage overhead of vector indexes](vector-search-how-to-storage-options.md) by eliminating some of these copies.
 
-+ Vector indexes are also subject to disk quota, in the sense that all indexes are subject disk quota. There's no separate disk quota for vector indexes.
-
-+ Vector quotas are enforced on the search service as a whole, per partition, meaning that if you add partitions, vector quota goes up. Per-partition vector quotas are higher on newer services. For more information, see [Vector index size limits](search-limits-quotas-capacity.md#vector-index-size-limits).
++ Vector quotas are enforced on the search service as a whole, per partition. If you add partitions, vector quota also increases. Per-partition vector quotas are higher on newer services. For more information, see [Vector index size limits](search-limits-quotas-capacity.md#vector-index-size-limits).
 
 ## How to check partition size and quantity
 
@@ -197,23 +198,25 @@ The storage size of one vector is determined by its dimensionality. Multiply the
   
 Every approximate nearest neighbor (ANN) algorithm generates extra data structures in memory to enable efficient searching. These structures consume extra space within memory.  
   
-**For the HNSW algorithm, the memory overhead ranges between 1% and 20%.**  
+**For the HNSW algorithm, the memory overhead ranges between 1% and 20% for uncompressed float32 (Edm.Single) vectors.**  
   
-The memory overhead is lower for higher dimensions because the raw size of the vectors increases, while the extra data structures remain a fixed size since they store information on the connectivity within the graph. Consequently, the contribution of the extra data structures constitutes a smaller portion of the overall size.  
+As dimensionality increases, the memory overhead percentage decreases. This occurs because the raw size of the vectors increases in size while the additional data structures, which store graph connectivity information, remain a fixed size for a given `m`. As a result, the relative impact of these extra data structures diminishes in relation to the overall vector size.
   
-The memory overhead is higher for larger values of the HNSW parameter `m`, which determines the number of bi-directional links created for every new vector during index construction. This is because `m` contributes approximately 8 bytes to 10 bytes per document multiplied by `m`.  
+The memory overhead increases with larger values of the HNSW parameter `m`, which specifies the number of bi-directional links created for each new vector during index construction. This happens because each link contributes approximately 8 to 10 bytes per document, and the total overhead scales proportionally with `m`.
   
-The following table summarizes the overhead percentages observed in internal tests:  
+The following table summarizes the overhead percentages observed in internal tests for *uncompressed* vector fields:  
   
 | Dimensions | HNSW Parameter (m) | Overhead Percentage |  
-|-------------------|--------------------|---------------------|
-| 96                | 4                  | 20%              |
-| 200               | 4                  | 8%               |  
-| 768               | 4                  | 2%               |  
-| 1536              | 4                  | 1%               |
-| 3072              | 4                  | 0.5%             |
+|------------|--------------------|---------------------|
+| 96         | 4                  | 20%                 |
+| 200        | 4                  | 8%                  |  
+| 768        | 4                  | 2%                  |  
+| 1536       | 4                  | 1%                  |
+| 3072       | 4                  | 0.5%                |
+
+These results demonstrate the relationship between dimensions, HNSW parameter `m`, and memory overhead for the HNSW algorithm.
 
-These results demonstrate the relationship between dimensions, HNSW parameter `m`, and memory overhead for the HNSW algorithm.  
+For vector fields which use compression techniques, such as [scalar or binary quantization](vector-search-how-to-quantization.md), the overhead percentage appears to consume a greater percentage of the total vector index size. As the size of the data decreases, the relative impact of the fixed-size data structures used to store graph connectivity information becomes more significant.
 
 ### Overhead from deleting or updating documents within the index
 
@@ -237,4 +240,4 @@ To obtain the **vector index size**, multiply this **raw_size** by the **algorit
 
 ## How vector fields affect disk storage
 
-Most of this article provides information about the size of vectors in memory. If you want to know about vector size on disk, the disk consumption for vector data is roughly three times the size of the vector index in memory. For example, if your `vectorIndexSize` usage is at 100 megabytes (10 million bytes), you would have used least 300 megabytes of `storageSize` quota to accommodate your vector indexes.
+Most of this article provides information about the size of vectors in memory. Read more about the [storage overhead of vector indexes](vector-search-how-to-storage-options.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索インデックスサイズに関する詳細なガイダンスの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるベクトル検索インデックスのサイズに関する記事の内容を更新したものです。主な修正点は、ベクトルインデックスのサイズとストレージクオータに関する情報の明確化と拡充です。特に、HNSWアルゴリズムに関するメモリオーバーヘッドの範囲が明示され、未圧縮のfloat32（Edm.Single）ベクトルに特有の記述が追加されています。

新たに、ベクトルフィールドの作成に伴うストレージコストの削減方法や、特定のアルゴリズムがインデックスサイズクオータにどのように影響するかについてのノートが設けられています。また、ベクトル圧縮技術に関連する説明が追加され、サイズが小さいベクトルでの相対的なオーバーヘッドの影響が強調されています。

全体として、この更新はベクトル検索におけるインデックスのサイズ、メモリ使用量、データ構造に関する理解を深め、利用者がより効率的にリソースを管理できるよう手助けすることを目的としています。


