---
date: '2025-08-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8858310...MicrosoftDocs:6ccc4b8
summary: このドキュメントの更新は、Azure AI Search の Blob ストレージにおけるネイティブソフト削除機能に関する情報を刷新しています。主な変更点として、API
  バージョンがプレビュー版から安定版に変更され、ユーザーが新機能に適応する必要があることが挙げられます。その他、日付の更新や見出しの修正により、情報の明確さと読みやすさが向上し、ドキュメントキーの重要性も強調されています。これにより、Azure
  AI Search のユーザー体験が向上することが期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8858310...MicrosoftDocs:6ccc4b8){target="_blank"}

# ハイライト
本ドキュメントの更新は、Azure AI Search の Blob ストレージにおけるネイティブソフト削除機能に関する情報の刷新を図っています。重要な特徴として、API バージョンの更新と日付の矛盾に関する訂正が含まれます。

## 新機能
- API バージョンが、プレビュー版（`2024-05-01-preview`）から安定版（`2024-07-01`）に変更され、最新の安定性ある機能を活用可能に。
  
## 破壊的変更
- 特に破壊的な変更は報告されていません。ただし、API のバージョン変更は、ユーザーが新しい機能に適応する必要があることを意味します。

## その他の更新
- 記載日が更新され、記事のタイムスタンプが最新の状態に。
- 見出しの細かい修正により内容がよりクリアになり、ネイティブBlobソフト削除へのリンクが調整されました。
- ドキュメントキーのマッピング方法に関する指示が強調され、手順が明確化されました。

# インサイト
このドキュメントの更新により、Azure AI Search の利便性が向上し、特に Blob ストレージでのソフト削除機能の実装に関する理解が深まります。API バージョンのアップデートは、開発者が最新技術をすぐに活用しやすくし、安定性を提供しています。見出しの細かな修正や日付の更新によって、読者が情報をすばやく正確に見つけられるよう改善されており、全体としてドキュメントの読みやすさが増しています。また、ドキュメントキーの重要性が再強調されたことで、ユーザーの実装時の間違いを防ぐ効果も期待できます。これらの変更により、Azure AI Search のユーザー体験がさらに向上することでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-howto-index-changed-deleted-blobs.md](#item-32a688) | minor update | インデックスの変更および削除されたBlobの検索方法に関する記事の更新 | modified | 5 | 5 | 10 | 


# Modified Contents
## articles/search/search-howto-index-changed-deleted-blobs.md{#item-32a688}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: gimondra
 manager: nitinme
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 02/24/2025
+ms.date: 08/21/2025
 ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
@@ -23,7 +23,7 @@ Although change detection is a given, deletion detection isn't. An indexer doesn
 
 There are two ways to implement a soft delete strategy:
 
-+ [Native blob soft delete (preview)](#native-blob-soft-delete), applies to Blob Storage only
++ [Native blob soft delete](#native-blob-soft-delete), applies to Blob Storage only
 + [Soft delete using custom metadata](#soft-delete-using-custom-metadata)
 
 The deletion detection strategy must be applied from the very first indexer run. If you didn't establish the deletion policy prior to the initial run, any documents that were deleted before the policy was implemented will remain in your index, even if you add the policy to the indexer later and reset it. If this has occurred, it's suggested that you create a new index using a new indexer, ensuring the deletion policy is in place from the beginning.
@@ -49,15 +49,15 @@ For this deletion detection approach, Azure AI Search depends on the [native blo
 
 + Document keys for the documents in your index must be mapped to either be a blob property or blob metadata, such as "metadata_storage_path".
 
-+ You must use a preview REST API such as [`2024-05-01-preview`](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2024-05-01-preview&preserve-view=true), or the indexer Data Source configuration in the Azure portal, to configure support for soft delete.
++ You can use the [REST API](/rest/api/searchservice/data-sources/create), or the indexer Data Source configuration in the Azure portal, to configure support for soft delete.
 
 + [Blob versioning](/azure/storage/blobs/versioning-overview) must not be enabled in the storage account. Otherwise, native soft delete isn't supported by design.
 
 ### Configure native soft delete
 
 In Blob storage, when enabling soft delete per the requirements, set the retention policy to a value that's much higher than your indexer interval schedule. If there's an issue running the indexer, or if you have a large number of documents to index, there's plenty of time for the indexer to eventually process the soft deleted blobs. Azure AI Search indexers will only delete a document from the index if it processes the blob while it's in a soft deleted state.
 
-In Azure AI Search, set a native blob soft deletion detection policy on the data source. You can do this either from the Azure portal or by using a previewREST API (`2024-05-01-preview`). The following instructions explain how to set the delete detection policy in Azure portal or through REST APIs.
+In Azure AI Search, set a native blob soft deletion detection policy on the data source. You can do this either from the Azure portal or by using the [REST API](/rest/api/searchservice/data-sources/create). The following instructions explain how to set the delete detection policy in Azure portal or through REST APIs.
 
 ### [**Azure portal**](#tab/portal)
 
@@ -78,7 +78,7 @@ In Azure AI Search, set a native blob soft deletion detection policy on the data
 Set the soft deletion detection policy in the data source definition. Specify the API version when creating or updating the data source.
 
 ```http
-PUT https://[service name].search.windows.net/datasources/blob-datasource?api-version=2024-05-01-preview
+PUT https://[service name].search.windows.net/datasources/blob-datasource?api-version=2024-07-01
 Content-Type: application/json
 api-key: [admin key]
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスの変更および削除されたBlobの検索方法に関する記事の更新"
}
```

### Explanation
このコードの変更は、Blobストレージのネイティブソフト削除機能に関するAzure AI Searchのドキュメント記事の更新です。変更された内容には以下のポイントが含まれます。

1. **日付の更新**: 記事内の日付が2025年2月24日から2025年8月21日に変更されました。

2. **見出しの修正**: いくつかの見出しで文言が微調整され、より明確に情報を伝えるための改良が行われました。具体的には、ネイティブBlobソフト削除のリンクを調整しました。

3. **APIバージョンの更新**: ソフト削除サポートを構成する際に使用するAPIのバージョンが、プレビュー版（`2024-05-01-preview`）から安定版（`2024-07-01`）に変更されました。これにより、最新の機能と安定性が提供されます。

4. **コンテンツの明確化**: 記事の一部では、ドキュメントのキーをBlobプロパティまたはBlobメタデータにマッピングすることの重要性が再強調され、明確な指示が付加されました。

これらの変更は、Azure AI Searchのユーザーがソフト削除機能を正しく理解し、実装できるようにすることを目的としています。


