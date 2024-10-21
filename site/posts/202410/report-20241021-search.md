---
date: '2024-10-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:418033b...MicrosoftDocs:96dd444
summary: この更新により、Azure AI サーチの使用に関する2つのガイドが改訂されました。1つは画像検索ポータルの開始ガイドで、もう1つはベクターインポートのガイドです。主な変更点には、日付の更新、新しいフィールドマッピングの情報追加、およびサポートされるデータソースの説明が含まれています。また、画像検索ガイドに新しいフィールドマッピングのセクションが追加され、ベクターインポートガイドには新しい埋め込みモデルのサポート情報が含まれています。今回の更新は、ユーザーがAzure
  AI サーチをより効果的に利用できるよう、具体的なガイドラインと詳細な情報を提供することに焦点を当てています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:418033b...MicrosoftDocs:96dd444){target="_blank"}

# ハイライト

これらの更新では、Azure AI サーチの利用に関する2つのガイドが更新されました。1つは画像検索機能のポータル開始ガイド、もう1つはベクターのインポートに関するガイドです。主な変更点としては、日付の更新、新しいフィールドマッピングの詳細、およびサポートされるデータソースの情報の追加があります。

## 新機能

- 画像検索ガイドに新しいフィールドのマッピングに関するセクションが追加され、ユーザーが追加フィールドをオプションで追加できるようになった。
- ベクターのインポートガイドにおいて、新しい埋め込みモデルのサポート情報が追加され、Azure OpenAIやAzure AI Studioモデルカタログの使用が明確化された。

## 破壊的変更

- 特に記載なし。ただし、従来の機能を変更または削除せず、新しいオプションや情報を追加する形での更新が行われている。

## その他の更新

- 日付が2024年10月18日に更新された。
- 画像検索ガイドとベクターのインポートガイドに、Azure Blob Storageとその他のデータソースの説明が明示された。
- インデクススケジュール設定とフィールド生成に関する情報が更新されて、より詳細な説明が追加された。

# インサイト

今回の変更は、Azure AI サーチポータルの利用をさらにスムーズにするための情報を提供することにフォーカスしています。特に、ユーザーが具体的にどのようにシステムを利用できるかについての明確なガイドラインが追加されています。

まず、画像検索ガイドでは、フィールドの追加とそのマッピングについての情報が強化されました。これにより、ユーザーは検索結果をカスタマイズしやすく、特定のニーズに合わせたフィールドを設計できます。また、Azure Blob Storageをデータソースとして利用する際のメタデータフィールドについても具体的な情報が提供されており、ユーザーはより計画的にデータインデクスを設計できます。

ベクターのインポートガイドでは、新たにサポートされる埋め込みモデルが記載され、ユーザーが最先端のAI機能を適用しやすくなっています。さらに、新しいデータソースのサポートに関する詳細も追加され、ユーザーは柔軟に様々なデータ形式を取り扱えるようになっています。

これらの変更は、Azure AI サーチ機能の効果的な利用法をユーザーに提供し、よりエキスパートな活用を促進するものです。新しく追加されたフィールドとモデルサポートにより、ユーザーは多様なデータセットを最大限に活用でき、これにより検索精度と効率が向上します。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | 画像検索のポータル開始ガイドの更新 | modified | 25 | 2 | 27 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | ベクターのインポートに関するポータル開始ガイドの更新 | modified | 43 | 15 | 58 | 


# Modified Contents
## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 08/05/2024
+ms.date: 10/18/2024
 ms.custom:
   - references_regions
 ---
@@ -112,6 +112,29 @@ The inclusion of plain text in the `chunk` field is useful if you want to use re
 
 1. Select **Next**.
 
+## Map new fields
+
+On the **Advanced settings** page, you can optionally add new fields. By default, the wizard generates the following fields with these attributes:
+
+| Field | Applies to | Description |
+|-------|------------|-------------|
+| chunk_id | Text and image vectors | Generated string field. Searchable, retrievable, sortable. This is the document key for the index. |
+| text_parent_id | Image vectors | Generated string field. Retrievable, filterable. Identifies the parent document from which the chunk originates. |
+| image_parent_id | Image vectors | Generated string field. Retrievable, filterable. Identifies the parent document from which the image originates. |
+| chunk | Text and image vectors | String field. Human readable version of the data chunk. Searchable and retrievable, but not filterable, facetable, or sortable. |
+| title | Text and image vectors | String field. Human readable document title or page title or page number. Searchable and retrievable, but not filterable, facetable, or sortable. |
+| image_vector | Image vectors | Collection(Edm.single). Vector representation of the image.  Searchable and retrievable, but not filterable, facetable, or sortable.|
+
+You can't modify the generated fields or their attributes, but you can add new fields if your data source provides them. For example, Azure Blob Storage provides a collection of metadata fields.
+
+1. Select **Add new**.
+
+1. Choose a source field from the list of available fields, provide a field name for the index, and accept the default data type or override as needed.
+
+   Metadata fields are searchable, but not retrievable, filterable, facetable, or sortable. 
+
+1. Select **Reset** if you want to restore the schema to its original version.
+
 ## Schedule indexing
 
 1. On the **Advanced settings** page, under **Schedule indexing**, specify a [run schedule](search-howto-schedule-indexers.md) for the indexer. We recommend **Once** for this exercise. For data sources where the underlying data is volatile, you can schedule indexing to pick up the changes.
@@ -132,7 +155,7 @@ When the wizard completes the configuration, it creates the following objects:
 
 + An indexer that drives the indexing pipeline.
 
-+ A data source connection to Blob Storage.
++ A data source connection to Azure Blob Storage.
 
 + An index with vector fields, text fields, vectorizers, vector profiles, and vector algorithms. You can't modify the default index during the wizard workflow. Indexes conform to the [2024-05-01-preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true) so that you can use preview features.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像検索のポータル開始ガイドの更新"
}
```

### Explanation
この変更では、Azure AI サーチのポータルに関するチュートリアル記事に対して、いくつかの重要な更新が加えられました。具体的には、2024年10月18日に日付が更新され、新しいフィールドに関する情報が追加されました。

新しいフィールドのマッピングに関するセクションが含まれ、ユーザーが追加フィールドをオプションで追加できることが詳述されています。デフォルトで生成されるフィールドとその属性についての詳細な表も含まれており、ユーザーがどのようにフィールドを追加できるかについての手順が説明されています。さらに、Azure Blob Storage をデータソースとして利用する場合のメタデータフィールドについても情報が提供されています。

また、インデクスのスケジュール設定に関する部分も強調され、設定完了後に作成されるオブジェクトについての情報が更新されました。特に、データソース接続に関する記述が「Azure Blob Storage」に明確化されています。これにより、ユーザーは最新の情報に基づいて、画像検索機能を適切に利用できるようになります。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: quickstart
-ms.date: 10/17/2024
+ms.date: 10/18/2024
 ---
 
 # Quickstart: Vectorize text and images by using the Azure portal
@@ -17,15 +17,19 @@ This quickstart helps you get started with [integrated vectorization](vector-sea
 
 Key points about the wizard:
 
-+ Source data is either Azure Blob Storage, Azure Data Lake Storage (ADLS) Gen2, or OneLake files and shortcuts.
-+ Document parsing mode is the default (one search document per blob or file).
-+ Index schema is nonconfigurable. It provides vector and nonvector fields for chunked data.
++ Supported data sources are Azure Blob Storage, Azure Data Lake Storage (ADLS) Gen2, or OneLake files and shortcuts.
++ Supported embedding models are hosted on Azure OpenAI, Azure AI Studio model catalog, Azure AI Vision multimodal.
++ Index schema provides vector and nonvector fields for chunked data. 
++ You can add fields, but you can't delete or modify generated fields.
++ Document parsing mode creates chunks (one search document per chunk).
 + Chunking is nonconfigurable. The effective settings are:
 
   ```json
-  textSplitMode: "pages",
-  maximumPageLength: 2000,
-  pageOverlapLength: 500
+   "textSplitMode": "pages",
+   "maximumPageLength": 2000,
+   "pageOverlapLength": 500,
+   "maximumPagesToTake": 0, #unlimited
+   "unit": "characters",
   ```
 
 ## Prerequisites
@@ -78,7 +82,7 @@ For more secure connections:
 
 ### Check for space
 
-If you're starting with the free service, you're limited to 3 indexes, data sources, skillsets, and indexers. Basic limits you to 15. Make sure you have room for extra items before you begin. This quickstart creates one of each object.
+If you're starting with the free service, you're limited to three indexes, data sources, skillsets, and indexers. Basic limits you to 15. Make sure you have room for extra items before you begin. This quickstart creates one of each object.
 
 ### Check for semantic ranker
 
@@ -88,7 +92,7 @@ The wizard supports semantic ranking, but only on the Basic tier and higher, and
 
 This section points you to data that works for this quickstart.
 
-### [Azure Blob storage](#tab/sample-data-storage)
+### [Azure Blob Storage](#tab/sample-data-storage)
 
 1. Sign in to the [Azure portal](https://portal.azure.com/) with your Azure account, and go to your Azure Storage account.
 
@@ -228,7 +232,7 @@ The wizard supports Azure, Cohere, and Facebook embedding models in the Azure AI
 
 The next step is to connect to a data source to use for the search index.
 
-### [Azure Blob storage](#tab/connect-data-storage)
+### [Azure Blob Storage](#tab/connect-data-storage)
 
 1. On the **Set up your data connection** page, select **Azure Blob Storage**.
 
@@ -351,17 +355,41 @@ Azure AI Search and your Azure AI resource must be in the same region.
 
 1. Select **Next**.
 
-## Choose advanced settings
+## Add semantic ranking
 
-1. On the **Advanced settings** page, you can optionally add [semantic ranking](semantic-search-overview.md) to rerank results at the end of query execution. Reranking promotes the most semantically relevant matches to the top.
+On the **Advanced settings** page, you can optionally add [semantic ranking](semantic-search-overview.md) to rerank results at the end of query execution. Reranking promotes the most semantically relevant matches to the top.
 
-1. Optionally, specify a [run schedule](search-howto-schedule-indexers.md) for the indexer.
+## Map new fields
 
-1. Select **Next**.
+On the **Advanced settings** page, you can optionally add new fields. By default, the wizard generates the following fields with these attributes:
+
+| Field | Applies to | Description |
+|-------|------------|-------------|
+| chunk_id | Text and image vectors | Generated string field. Searchable, retrievable, sortable. This is the document key for the index. |
+| parent_id | Text vectors | Generated string field. Retrievable, filterable. Identifies the parent document from which the chunk originates. |
+| chunk | Text and image vectors | String field. Human readable version of the data chunk. Searchable and retrievable, but not filterable, facetable, or sortable. |
+| title | Text and image vectors | String field. Human readable document title or page title or page number. Searchable and retrievable, but not filterable, facetable, or sortable. |
+| text_vector | Text vectors | Collection(Edm.single). Vector representation of the chunk.  Searchable and retrievable, but not filterable, facetable, or sortable.|
+
+You can't modify the generated fields or their attributes, but you can add new fields if your data source provides them. For example, Azure Blob Storage provides a collection of metadata fields.
+
+1. Select **Add new**.
+
+1. Choose a source field from the list of available fields, provide a field name for the index, and accept the default data type or override as needed.
+
+   Metadata fields are searchable, but not retrievable, filterable, facetable, or sortable. 
+
+1. Select **Reset** if you want to restore the schema to its original version.
+
+## Schedule indexing
+
+On the **Advanced settings** page, you can optionally specify a [run schedule](search-howto-schedule-indexers.md) for the indexer.
+
+1. Select **Next** when you're done with the **Advanced settings** page.
 
 ## Finish the wizard
 
-1. On the **Review your configuration** page, specify a prefix for the objects that the wizard will create. A common prefix helps you stay organized.
+1. On the **Review your configuration** page, specify a prefix for the objects that the wizard creates. A common prefix helps you stay organized.
 
 1. Select **Create**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクターのインポートに関するポータル開始ガイドの更新"
}
```

### Explanation
この変更では、Azure ポータルを使用してテキストと画像をベクター化する際のクイックスタートガイドに対する更新が行われました。主な変更点は、日付の更新（2024年10月18日）、サポートされるデータソースの情報の追加、今後のフィールドのマッピングに関する詳細が含まれています。

具体的には、サポートされるデータソースとして Azure Blob Storage、Azure Data Lake Storage (ADLS) Gen2、および OneLake のファイルとショートカットが明示され、新しい埋め込みモデル（Azure OpenAI、Azure AI Studio モデルカタログ、Azure AI Vision）のサポートに関する情報も追加されました。また、インデックススキーマでは生成されたフィールドの削除や変更はできないが、新しいフィールドを追加できることが強調されています。

さらに、「高度な設定」セクションには、新しいフィールドのマッピングやインデクシングのスケジュール設定に関する具体的な手順が詳述されています。全体として、ユーザーがベクターインポートをより効果的に行うための具体的な指示と最新の情報が提供されています。


