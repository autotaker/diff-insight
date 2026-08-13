---
date: '2026-08-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4bb9e7f...MicrosoftDocs:4f575cb
summary: 今回の変更では、Azure AI Searchに関する記事が更新され、特にインデクサや知識ソースの制限に関する情報が強調されました。新しい「doc-kit-assisted」タグが追加され、プレビューモードやSharePointのトラブルシューティングに関する記事も新たに登場しました。具体的には、プレビューモードの機能と条件の説明や、SharePoint権限フィルタリング問題への対処法が具体化されています。破壊的な変更は報告されていませんが、データアクセスに関する詳細が追加されており、新たな要件が生じる可能性もあります。全体的に、今回のアップデートはAzure
  AI Searchの機能向上とユーザーの理解促進を目指したものです。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4bb9e7f...MicrosoftDocs:4f575cb){target="_blank"}

<format>
# ハイライト
今回の変更では、Azure AI Search関連の記事がマイナーな更新や新機能の追加により改善されています。特に、各記事に「doc-kit-assisted」タグが追加され、インデクサや知識ソースの制限に関する詳細な情報が一層強調されています。また、新しい記事がいくつか追加され、特にプレビューモードやSharePointのトラブルシューティングについての内容が強化されました。

## 新機能
- Azure AI Searchのプレビューモードに関する新しい記事が追加されました。プレビューモードにおける機能と条件について説明されています。
- 新しいトラブルシューティングガイド「SharePoint権限フィルタリングのトラブルシューティング」が追加されました。これにより、SharePointの権限関連問題への対処方法が具体化されています。

## 破壊的変更
- 破壊的な変更は特に報告されていませんが、複数の記事においてデータアクセスに関する詳細が追加されており、新たな要件が生じている可能性があります。

## その他の更新
- 大半の記事の日付が更新され、新しい「doc-kit-assisted」タグが追加されています。
- 各種インデクサに対し、より細かい制限や設定方法が明確化されました。
- セキュリティポリシーに関連するリンクが更新され、正確性が向上しています。

# インサイト
今回の更新は、Azure AI Searchの機能とユーザーの理解を促進するために行われた一連の有用なマイナーアップデートです。特に、インデクサや知識ソースに関連する制限事項が強調されており、ユーザーがより適切にサービスの利用を計画できるようになっています。たとえば、Blobやファイルインデクサにおいては、データのサイズ制限や他の処理ステージにおける可能な制限についての情報が詳細に記述されています。これにより、ユーザーはより現実的なデータ処理の境界を理解し、適切にスケール可能なアプリケーション設計ができるでしょう。

新たに追加されたプレビューモードに関する記事やトラブルシューティングガイドは、機能の向上と問題解決のための手助けとして非常に役立ちます。特に、プレミアムサービスの前提としてプレビューモードの正確な理解と、トラブルシューティングガイドを利用した即応性のある問題解決が期待されます。全体として、今回の改訂により、Azure AI Searchの利用における信頼性と効率性の向上が図られることが示唆されています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-blob.md](#item-ac6c8a) | minor update | エージェント知識ソースのためのBlobの作成に関する記事の更新 | modified | 4 | 1 | 5 | 
| [agentic-knowledge-source-how-to-file.md](#item-88f720) | minor update | エージェント知識ソースのためのファイル作成に関する記事の更新 | modified | 4 | 1 | 5 | 
| [agentic-knowledge-source-how-to-onelake.md](#item-ec7a80) | minor update | エージェント知識ソースのためのインデックス付きOneLakeの作成に関する記事の更新 | modified | 4 | 5 | 9 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed.md](#item-fe72fc) | minor update | インデックス付きSharePoint知識ソースの作成に関する記事の更新 | modified | 9 | 2 | 11 | 
| [cognitive-search-common-errors-warnings.md](#item-a5c854) | minor update | インデクサのエラーと警告に関する記事の更新 | modified | 22 | 10 | 32 | 
| [cognitive-search-skill-content-understanding.md](#item-c7787e) | minor update | コンテンツ理解スキルに関する記事の更新 | modified | 11 | 14 | 25 | 
| [cognitive-search-skill-document-extraction.md](#item-072b72) | minor update | ドキュメント抽出スキルに関する記事の更新 | modified | 5 | 1 | 6 | 
| [cognitive-search-skill-document-intelligence-layout.md](#item-62c06f) | minor update | ドキュメントインテリジェンスレイアウトスキルに関する記事の更新 | modified | 4 | 1 | 5 | 
| [search-document-level-access-overview.md](#item-4bb055) | minor update | ドキュメントレベルアクセス制御に関する記事の更新 | modified | 5 | 28 | 33 | 
| [search-file-storage-integration.md](#item-d20e26) | minor update | Azure Filesインデクサに関する記事の更新 | modified | 5 | 5 | 10 | 
| [search-how-to-index-azure-blob-storage.md](#item-353b6b) | minor update | Azure Blob Storageインデクサに関する記事の更新 | modified | 5 | 1 | 6 | 
| [search-how-to-index-azure-data-lake-storage.md](#item-faca23) | minor update | Azure Data Lake Storageインデクサに関する記事の更新 | modified | 4 | 4 | 8 | 
| [search-how-to-index-onelake-files.md](#item-95f3db) | minor update | OneLakeファイルインデクサに関する記事の更新 | modified | 5 | 2 | 7 | 
| [search-how-to-index-sharepoint-online.md](#item-8c099c) | minor update | SharePoint Onlineインデクサに関する記事の更新 | modified | 24 | 21 | 45 | 
| [search-indexer-high-density-serverless-overview.md](#item-2bc606) | minor update | サーバーレスおよびS3 HDインデクサに関する記事の更新 | modified | 11 | 9 | 20 | 
| [search-indexer-sharepoint-access-control-lists.md](#item-532a24) | minor update | SharePointアクセス制御リストに関する記事の更新 | modified | 16 | 1 | 17 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索制限とクォータに関する記事の更新 | modified | 24 | 8 | 32 | 
| [search-preview-terms.md](#item-4fe0af) | new feature | Azure AI Searchのプレビューモードに関する記事の追加 | added | 43 | 0 | 43 | 
| [search-query-access-control-rbac-enforcement.md](#item-d24df7) | minor update | クエリ時のACLおよびRBAC強制に関する記事の更新 | modified | 7 | 2 | 9 | 
| [security-controls-policy.md](#item-0e5774) | minor update | セキュリティコントロールポリシーに関するリンクの修正 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c4768f) | minor update | 目次に新しい項目を追加 | modified | 4 | 0 | 4 | 
| [troubleshoot-sharepoint-query-permission-filtering.md](#item-85cf41) | new feature | SharePoint権限フィルタリングのトラブルシューティングガイドの追加 | added | 117 | 0 | 117 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-blob.md{#item-ac6c8a}

<details>
<summary>Diff</summary>
````diff
@@ -3,8 +3,9 @@ title: Create a Blob Knowledge Source for Agentic Retrieval
 description: Learn how to create a blob knowledge source in Azure AI Search that ingests content from Azure Blob Storage or ADLS Gen2 for agentic retrieval.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/04/2026
+ms.date: 08/08/2026
 ai-usage: ai-assisted
+ms.custom: doc-kit-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
 
@@ -34,6 +35,8 @@ When you create a blob knowledge source, you specify an external data source, mo
 + An index that stores enriched content and meets the criteria for agentic retrieval.
 + An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
 
+The generated indexer conforms to the *blob indexer*, whose prerequisites, supported document formats, and limitations also apply to blob knowledge sources. For more information, see the [blob indexer documentation](search-how-to-index-azure-blob-storage.md) and [indexer limits](search-limits-quotas-capacity.md#indexer-limits). If the generated skillset calls an external service, that skill's input and service limits also apply.
+
 > [!NOTE]
 > If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata](search-indexer-access-control-lists-and-role-based-access.md) or [Blob RBAC scopes](search-blob-indexer-role-based-access.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースのためのBlobの作成に関する記事の更新"
}
```

### Explanation
この変更は、Azure AI SearchにおけるBlob知識ソースの作成方法に関する記事のマイナーな更新です。具体的には、記事内の日付が2026年6月4日から2026年8月8日に変更され、記事の内容に新たに「doc-kit-assisted」というカスタムタグが追加されました。また、Blob知識ソースの作成に関する説明が強化され、インデクサの要件や外部サービスに関連する制限に関する注意書きが補足されています。これにより、ユーザーはBlobのインデクサに関する具体的な情報を得ることができ、エージェントリトリーバルのために必要な条件をより良く理解できるようになります。

## articles/search/agentic-knowledge-source-how-to-file.md{#item-88f720}

<details>
<summary>Diff</summary>
````diff
@@ -3,8 +3,9 @@ title: Create a File Knowledge Source for Agentic Retrieval
 description: Learn how to create a file knowledge source in Azure AI Search, upload files directly, and use the processed content in a knowledge base.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/20/2026
+ms.date: 08/08/2026
 ai-usage: ai-assisted
+ms.custom: doc-kit-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
 
@@ -80,6 +81,8 @@ The following limits apply to file knowledge sources.
 | Maximum file size per upload | 50 MB |
 | Maximum files per file knowledge source | 100 |
 
+If you configure the file knowledge source to chunk or vectorize uploaded content, model and downstream processing limits also apply.
+
 > [!NOTE]
 > + Uploading the same file name doesn't replace an existing file. For more information, see [Upload files](#upload-files).
 > + The generated search index stores the uploaded content. For total storage limits by pricing tier, see [Service limits](search-limits-quotas-capacity.md#service-limits).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースのためのファイル作成に関する記事の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるファイル知識ソースの作成方法に関する記事に対するマイナーな更新です。特に、記事の日付が2026年7月20日から2026年8月8日に変更され、「doc-kit-assisted」という新たなカスタムタグが追加されました。また、ファイル知識ソースに関連する制限事項が明確化され、アップロードされたコンテンツをチャンクまたはベクトル化するための設定が行われた場合のモデルや後処理の制限についての重要な情報が追加されました。さらに、同じファイル名のファイルをアップロードする際に既存のファイルが置き換えられないことについての注意書きも加えられています。これにより、ユーザーはファイル知識ソースの設定と制限についてより良い理解を得ることができるようになります。

## articles/search/agentic-knowledge-source-how-to-onelake.md{#item-ec7a80}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,10 @@
 ---
 title: Create an Indexed OneLake Knowledge Source for Agentic Retrieval
-description: Learn how to create an indexed OneLake knowledge source in Azure AI Search. An indexed OneLake knowledge source specifies a lakehouse, models, and properties that create an enrichment pipeline for agentic retrieval workloads.
+description: Learn how to create an indexed OneLake knowledge source that defines a lakehouse, models, and enrichment pipeline for agentic retrieval in Azure AI Search.
 ms.service: azure-ai-search
-ms.custom:
-  - ignite-2025
+ms.custom: [ignite-2025, doc-kit-assisted]
 ms.topic: how-to
-ms.date: 06/02/2026
+ms.date: 08/08/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
@@ -36,7 +35,7 @@ When you create an indexed OneLake knowledge source, you specify an external dat
 + An index that stores enriched content and meets the criteria for agentic retrieval.
 + An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
 
-The generated indexer conforms to the *OneLake indexer*, whose prerequisites, supported tasks, supported document formats, supported shortcuts, and limitations also apply to OneLake knowledge sources. For more information, see the [OneLake indexer documentation](search-how-to-index-onelake-files.md).
+The generated indexer conforms to the *OneLake indexer*, whose prerequisites, supported tasks, supported document formats, supported shortcuts, and limitations also apply to OneLake knowledge sources. For more information, see the [OneLake indexer documentation](search-how-to-index-onelake-files.md) and [indexer limits](search-limits-quotas-capacity.md#indexer-limits). If the generated skillset calls an external service, that skill's input and service limits also apply.
 
 ### Usage support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースのためのインデックス付きOneLakeの作成に関する記事の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるインデックス付きOneLake知識ソースの作成方法に関する記事に対するマイナーな更新です。具体的には、記事の説明文がより明確に改訂され、知識ソースが湖水箱、モデル、およびエンリッチメントパイプラインを定義することが強調されています。また、カスタム情報に「doc-kit-assisted」が追加され、記事の日付が2026年6月2日から2026年8月8日に変更されました。さらに、生成されたインデクサに関する説明が拡充され、インデクサの制限についての情報が追加されています。これにより、ユーザーはOneLake知識ソースの作成と関連するインデクサの条件について、より詳細な理解を得られるようになります。

## articles/search/agentic-knowledge-source-how-to-sharepoint-indexed.md{#item-fe72fc}

<details>
<summary>Diff</summary>
````diff
@@ -3,8 +3,9 @@ title: Create a SharePoint (Indexed) Knowledge Source
 description: Learn how to create an indexed SharePoint knowledge source, which ingests content from SharePoint sites into a searchable index on Azure AI Search.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/04/2026
+ms.date: 08/08/2026
 ai-usage: ai-assisted
+ms.custom: doc-kit-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
 
@@ -29,11 +30,13 @@ An *indexed SharePoint knowledge source* (preview) ingests SharePoint content in
 
 When you create an indexed SharePoint knowledge source, you specify a SharePoint connection string, models, and properties to automatically generate the following Azure AI Search objects:
 
-+ A data source that points to SharePoint sites.
++ A data source that points to SharePoint sites and uses the connection string unchanged. The generated data source follows the SharePoint indexer's [`TenantId` rules](search-how-to-index-sharepoint-online.md#connection-string-format).
 + A skillset that chunks and optionally vectorizes multimodal content.
 + An index that stores enriched content and meets the criteria for agentic retrieval.
 + An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
 
+The generated indexer conforms to the *SharePoint in Microsoft 365 indexer*, whose prerequisites, supported document formats, and limitations also apply to indexed SharePoint knowledge sources. For more information, see the [SharePoint indexer documentation](search-how-to-index-sharepoint-online.md) and [indexer limits](search-limits-quotas-capacity.md#indexer-limits). If the generated skillset calls an external service, that skill's input and service limits also apply.
+
 ### Usage support
 
 | [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
@@ -301,6 +304,8 @@ After the knowledge base is configured, [call the retrieve action or MCP endpoin
 
 To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time (preview)](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time-preview).
 
+For missing, unexpected, or failed results from an indexed SharePoint permission query, see [Troubleshoot SharePoint permission filtering](troubleshoot-sharepoint-query-permission-filtering.md).
+
 ### Surface document-embedded images
 
 To surface document-embedded images (such as diagrams or scans) in answer synthesis responses, configure `assetStore` on this knowledge source, and then enable image serving on the knowledge base. For more information, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
@@ -311,6 +316,8 @@ To surface document-embedded images (such as diagrams or scans) in answer synthe
 
 ## Known errors
 
+The generated SharePoint data source and indexer use the same Microsoft Entra tenant validation and authentication behavior as directly configured SharePoint indexers. For tenant-related failures, review the [generated indexer's status and execution history](search-monitor-indexers.md), and then follow the [`Invalid AAD tenant` remediation](cognitive-search-common-errors-warnings.md#error-invalid-aad-tenant).
+
 When you create this knowledge source with `contentExtractionMode` set to `standard`, you might get the following error.
 
 ```json
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス付きSharePoint知識ソースの作成に関する記事の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるインデックス付きSharePoint知識ソースの作成方法に関する記事に対するマイナーな更新です。主な改訂点として、記事の日付が2026年6月4日から2026年8月8日に変更され、カスタム情報に「doc-kit-assisted」が追加されました。また、生成されるデータソースに関する説明が強化され、SharePointインデクサの「TenantId」ルールに言及が追加されています。さらに、生成されるインデクサに関する情報が詳細化され、外部サービスを呼び出すスキルセットに関連する入力とサービスの制限についての注意事項が含まれました。加えて、ユーザーサポートのリンクが提供され、インデックス付きSharePointの権限クエリに関するトラブルシューティングのセクションが追加されることで、ユーザーが直面する可能性のある問題への対応策が明確になりました。これらの変更により、ユーザーはSharePoint知識ソースの作成と運用に関する重要な情報をよりよく理解しやすくなります。

## articles/search/cognitive-search-common-errors-warnings.md{#item-a5c854}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,13 @@
 ---
 title: Indexer Errors and Warnings
-description: This article provides information and solutions to common errors and warnings you might encounter during AI enrichment in Azure AI Search.
+description: Learn how to troubleshoot common errors and warnings you might encounter during indexing AI enrichment in Azure AI Search.
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
+  - doc-kit-assisted
 ms.topic: error-reference
-ms.date: 04/23/2026
+ms.date: 08/08/2026
+ai-usage: ai-assisted
 ms.update-cycle: 180-days
 ---
 
@@ -15,14 +17,10 @@ ms.update-cycle: 180-days
 
 This article provides information and solutions to common errors and warnings you might encounter during indexing and AI enrichment in Azure AI Search.
 
-Indexing stops when the error count exceeds ['maxFailedItems'](cognitive-search-concept-troubleshooting.md#tip-2-see-what-works-even-if-there-are-some-failures). 
-
-If you want indexers to ignore these errors (and skip over "failed documents"), consider updating the `maxFailedItems` and `maxFailedItemsPerBatch` as described [here](/rest/api/searchservice/indexers/create#indexingparameters).
+Indexing stops when the error count exceeds [maxFailedItems](cognitive-search-concept-troubleshooting.md#tip-2-see-what-works-even-if-there-are-some-failures). To let indexers skip failed documents, configure [maxFailedItems` and `maxFailedItemsPerBatch](/rest/api/searchservice/indexers/create#indexingparameters).
 
 > [!NOTE]
-> Each failed document along with its document key (when available) will show up as an error in the indexer execution status. You can utilize the [index api](/rest/api/searchservice/documents) to manually upload the documents at a later point if you have set the indexer to tolerate failures.
-
-The error information in this article can help you resolve errors, allowing indexing to continue.
+> Each failed document and its document key, when available, appear as an error in the indexer execution status. If you configure the indexer to tolerate failures, you can use [Documents - Index](/rest/api/searchservice/documents/index) to upload the documents later.
 
 Warnings don't stop indexing, but they do indicate conditions that could result in unexpected outcomes. Whether you take action or not depends on the data and your scenario.
 
@@ -422,7 +420,7 @@ For example, if the column used for change detection is of type datetime, but th
 
 Check the data type for the 'High Water Mark' column in the source and update the indexer configuration accordingly. Once verified and updated, reset and rerun the indexer to process the column values.
 
-## `Error: Access denied to Virtual Network/Firewall rules.`
+## `Error: Access denied to Virtual Network/Firewall rules`
 
 This error typically occurs due to one of the following:
 - Firewall restrictions on Azure resources required by your indexer, depending on your configuration. These resources may include: the [data source](search-data-sources-gallery.md#generally-available-data-sources-by-azure-ai-search), Azure Storage account (used for [debug sessions](cognitive-search-debug-session.md), [incremental enrichment](cognitive-search-incremental-indexing-conceptual.md) or [knowledge store](knowledge-store-concept-intro.md)), Azure Function (used for [web API custom skills](cognitive-search-custom-skill-web-api.md)), or Microsoft Foundry deployments used during [AI enrichment](cognitive-search-concept-intro.md).
@@ -432,7 +430,7 @@ Ensure that the indexer has access to your setup components by reviewing your re
 - [Firewall and IP restriction settings](search-indexer-howto-access-ip-restricted.md)
 - [Shared private link setup](search-indexer-howto-access-private.md)
 
-## `Error: Credentials provided in the connection string are invalid or have expired.`
+## `Error: Credentials provided in the connection string are invalid or have expired`
 
 This error occurs when the Azure AI Search indexer cannot authenticate using the provided connection string or it has issues accessing the storage account to verify the credentials. 
 
@@ -443,6 +441,20 @@ This error occurs when the Azure AI Search indexer cannot authenticate using the
 | Network/firewall blocks identity access | The resource contacted is configured to restrict network access. | Configure [network settings](search-indexer-howto-access-ip-restricted.md) to allow Azure AI Search access. |
 | Key authorization has been disabled | Shared key access removed on the source, but the Search service data source configuration still uses key-based authentication. | Use [managed identity](search-how-to-managed-identities.md) authentication and ensure role-based permissions are in place. From an Azure Storage perspective, this means that [shared key authorization functionality is blocked](/azure/storage/common/shared-key-authorization-prevent), either from the storage account itself, or enforced through enterprise-level Azure Policies. |
 
+## `Error: Invalid AAD tenant`
+
+This message can appear when a SharePoint in Microsoft 365 indexer can't authenticate to the Microsoft Entra tenant that owns the SharePoint site. `TenantId` is optional in the SharePoint data source connection string, but any value you provide must be the Microsoft Entra tenant ID (GUID) for that site. This tenant isn't necessarily the Microsoft Entra tenant associated with your search service.
+
+Use the following guidance to resolve the error:
+
++ For a cross-tenant SharePoint connection, include the SharePoint site's Microsoft Entra tenant ID as `TenantId` in the connection string.
++ For a connection within the same Microsoft Entra tenant, either include the SharePoint site's tenant ID or enable the search service's system-assigned managed identity. When you omit `TenantId`, the indexer uses the Microsoft Entra resource tenant associated with that identity.
++ If neither an explicit `TenantId` nor the resource tenant is available, the indexer reports: `Ensure service managed identity is enabled for your service, or TenantId is specified in your connection string.`
+
+A malformed value that isn't a GUID can cause failure when you create or update the data source. A well-formed ID for the wrong Microsoft Entra tenant can pass data source validation but fail when the indexer authenticates. For execution failures, go to the search service in the Azure portal, select **Search Management** > **Indexers**, select the indexer, and review its **Execution History** and status details.
+
+For connection string formats and instructions to find the SharePoint site's Microsoft Entra tenant ID, see [Configure the SharePoint in Microsoft 365 indexer](search-how-to-index-sharepoint-online.md#configure-the-sharepoint-in-microsoft-365-indexer).
+
 ## `Error: Error detecting index schema from data source`
 
 The Azure portal experience used to configure the indexer was unable to retrieve schema information from the data source. This can happen due to transient connectivity issues or network configuration restrictions that prevent Azure AI Search from accessing the source.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサのエラーと警告に関する記事の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるインデクサのエラーと警告に関する情報を提供する記事に対するマイナーな更新です。主な改訂点として、記事の説明が「AIエンリッチメント中に遭遇する可能性のある一般的なエラーと警告のトラブルシューティング方法」に変更され、見出しの日付が2026年4月23日から2026年8月8日に変更されました。また、カスタム情報に「doc-kit-assisted」が追加され、AI使用情報が明記されました。

内容の改訂としては、エラー処理やインデクサの設定に関する具体的な指示が強化され、特に「maxFailedItems」や「maxFailedItemsPerBatch」の設定方法に関する表現が改善されています。新たに追加された「Invalid AAD tenant」エラーに関するセクションでは、Microsoft Entraテナントに関連する問題を解決する方法が具体的に説明されており、ユーザーが直面する可能性のある認証の問題に対して従うべきガイダンスが示されています。

これらの変更により、読者はエラーと警告のトラブルシューティングを行い、インデクサが効果的に動作するためのサポート情報をより簡単に得ることができるようになります。

## articles/search/cognitive-search-skill-content-understanding.md{#item-c7787e}

<details>
<summary>Diff</summary>
````diff
@@ -7,8 +7,9 @@ ms.custom:
   - references_regions
   - ignite-2025
   - build-2026
+  - doc-kit-assisted
 ms.topic: reference
-ms.date: 06/02/2026
+ms.date: 08/08/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ---
@@ -18,13 +19,7 @@ ai-usage: ai-assisted
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+> Features, capabilities, or properties marked (preview) aren't covered by a service-level agreement, aren't recommended for production workloads, and might change or be constrained before they become generally available. If you choose to use preview functionality, whether it's standalone or part of a generally available feature, you're responsible for data handling, data access, responsible AI use, and other obligations described in the [Azure AI Search preview terms](search-preview-terms.md).
 
 The **Azure Content Understanding** skill uses [document analyzers](/azure/ai-services/content-understanding/document/overview) from [Azure Content Understanding in Foundry Tools](/azure/ai-services/content-understanding/overview) to analyze unstructured documents and other content types, generating organized, searchable outputs that can be integrated into automation workloads. This skill extracts both text and images, including location metadata that preserves each image's position within the document. Image proximity to related content is especially useful for [multimodal search](multimodal-search-overview.md), [agentic retrieval](agentic-retrieval-overview.md), and [retrieval-augmented generation](retrieval-augmented-generation-overview.md) (RAG).
 
@@ -42,7 +37,7 @@ You can use the Azure Content Understanding skill for both content extraction an
 
 + Azure Content Understanding can generate AI-based descriptions for images, charts, diagrams, and embedded figures. Embedded figure descriptions are incorporated directly into markdown content generated for retrieval. These descriptions are searchable and can improve RAG grounding and multimodal retrieval quality. 
 
-The Azure Content Understanding skill is generally available in the [`2026-04-01` REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true). Starting with the [`2026-05-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true), the skill optionally generates AI-based descriptions for document-embedded images, charts, and diagrams. To enable descriptions, you must deploy an Azure OpenAI chat completion model in the Foundry resource attached to the skillset. This API version also adds *semantic* chunking, a layout-aware option that respects paragraph boundaries and measures chunk length in tokens. Both capabilities require opt-in. When the new parameters are omitted, the skill behaves the same as in the stable `2026-04-01` API version.
+The Azure Content Understanding skill is generally available in the [`2026-04-01` REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true). Starting with the [`2026-05-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true), the skill optionally generates AI-based descriptions for document-embedded images, charts, and diagrams. To enable descriptions, you must deploy an Azure OpenAI chat completion model in the Foundry resource attached to the skillset. This API version also adds *semantic* chunking (preview), a layout-aware option that respects paragraph boundaries and measures chunk length in tokens. Both capabilities require opt-in. When the new parameters are omitted, the skill behaves the same as in the stable `2026-04-01` API version.
 
 ## Limitations
 
@@ -101,14 +96,14 @@ Parameters are case sensitive.
 | Parameter name | Allowed values | Description |
 |--------------------|----------------|-------------|
 | `extractionOptions` |`["images"]`, `["images", "locationMetadata"]`, `["locationMetadata"]` | Identify any extra content extracted from the document. Define an array of enums that correspond to the content to be included in the output. For example, if `extractionOptions` is `["images", "locationMetadata"]`, the output includes images and location metadata that provides page location and visual information related to where the content was extracted.  |
-| `modelName` | String, such as `"gpt-4.1"`. | Optional. Available starting with the `2026-05-01-preview` REST API. The name of the Azure OpenAI chat completion model used to generate descriptions of embedded images, charts, and diagrams. Image description is independent of `extractionOptions` and can be enabled without extracting images. Must be specified together with `modelDeployment`. For a list of supported models, see [Supported generative models](/azure/ai-services/content-understanding/service-limits#supported-generative-models). |
-| `modelDeployment` | String. | Optional. Available starting with the `2026-05-01-preview` REST API. The deployment name of the Azure OpenAI model in the Foundry resource that's attached to the skillset. Must be specified together with `modelName`. |
+| `modelName` (preview) | String, such as `"gpt-4.1"`. | Optional. Available starting with the `2026-05-01-preview` REST API. The name of the Azure OpenAI chat completion model used to generate descriptions of embedded images, charts, and diagrams. Image description is independent of `extractionOptions` and can be enabled without extracting images. Must be specified together with `modelDeployment`. For a list of supported models, see [Supported generative models](/azure/ai-services/content-understanding/service-limits#supported-generative-models). |
+| `modelDeployment` (preview) | String. | Optional. Available starting with the `2026-05-01-preview` REST API. The deployment name of the Azure OpenAI model in the Foundry resource that's attached to the skillset. Must be specified together with `modelName`. |
 | `chunkingProperties` | See the following table. | Options that encapsulate how to chunk text content. |
 
 | `chunkingProperties` parameters | Allowed values | Description |
 |--------------------|-------------|-------------|
-| `method` | `fixedSize` (default) or `semantic`. Available starting with the `2026-05-01-preview` REST API. | The chunking strategy. `fixedSize` uses character-based windowed chunking. `semantic` uses layout-aware chunking that respects paragraph boundaries and intelligently handles large tables that span chunk boundaries. |
-| `unit` | `characters` (with `fixedSize`) or `tokens` (with `semantic`, available starting with the `2026-05-01-preview` REST API). | Controls the cardinality of the chunk unit. Only the `fixedSize` + `characters` and `semantic` + `tokens` combinations are supported. If `unit` is omitted, it's inferred from `method`. |
+| `method` | `fixedSize` (default) or `semantic` (preview). Available starting with the `2026-05-01-preview` REST API. | The chunking strategy. `fixedSize` uses character-based windowed chunking. `semantic` uses layout-aware chunking that respects paragraph boundaries and intelligently handles large tables that span chunk boundaries. |
+| `unit` | `characters` (with `fixedSize`) or `tokens` (preview, with `semantic`, available starting with the `2026-05-01-preview` REST API). | Controls the cardinality of the chunk unit. Only the `fixedSize` + `characters` and `semantic` + `tokens` combinations are supported. If `unit` is omitted, it's inferred from `method`. |
 | `maximumLength` | When `unit` is `characters`, an integer between 300 and 50,000. When `unit` is `tokens`, an integer between 100 and 8,000. Default is 500. | The maximum chunk length, measured in the configured `unit`. |
 | `overlapLength` | Integer. The value must be less than half of `maximumLength`. | The length of overlap between two text chunks. Applies only when `method` is `fixedSize`. Must be omitted or set to `0` when `method` is `semantic`. |
 
@@ -142,6 +137,8 @@ The file reference object can be generated in one of following ways:
 
 + Setting the `allowSkillsetToReadFileData` parameter on your indexer definition to `true`. This setting creates a `/document/file_data` path that's an object representing the original file data downloaded from your blob data source. This parameter only applies to files in Azure Blob Storage.
 
+  `allowSkillsetToReadFileData` makes the downloaded file data available to the skill. It doesn't increase the [blob indexer limits](search-limits-quotas-capacity.md#indexer-limits) or the Content Understanding service limits described in [Data limits](#data-limits).
+
 + Having a custom skill returning a JSON object definition that provides `$type`, `data`, or `url` and `sastoken`. The `$type` parameter must be set to `file`, and  `data` must be the base 64-encoded byte array of the file content. The `url` parameter must be a valid URL with access to download the file at that location.
 
 ## Skill outputs
@@ -268,7 +265,7 @@ The first example uses fixed-size chunking and demonstrates how to output text c
 
 `imagePath` represents the relative path of a stored image. If the knowledge store file projection is configured in the skillset, this path matches the relative path of the image stored in the knowledge store.
 
-### Example 2: Semantic chunking with image description
+### Example 2: Semantic chunking with image description (preview)
 
 This example, available starting with the `2026-05-01-preview` REST API, uses semantic chunking and produces AI-generated descriptions of embedded images, charts, and diagrams. The Foundry resource attached to the skillset must have the chat completion model identified by `modelName` and the deployed `modelDeployment`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツ理解スキルに関する記事の更新"
}
```

### Explanation
この変更は、Azureのコンテンツ理解スキルに関する記事に対するマイナーな更新です。主な改訂点には、記事の日付が2026年6月2日から2026年8月8日に変更され、新たに「doc-kit-assisted」がカスタム情報として追加されました。また、プレビュー機能に関する警告が強調され、ユーザーがプレビュー機能を使用する際の責任について明確なガイダンスが提供されています。

具体的には、インデクサが利用するAIベースの説明生成機能や新たに導入された「セマンティックチャンクニング」のオプションに関する情報が改訂されています。「セマンティックチャンクニング」は、段落の境界を尊重し、大きな表を適切に処理するレイアウト意識のある分割方式を提供します。これにより、文書に埋め込まれた画像や図表の説明がAIによって生成され、情報検索の質を向上させる可能性が強調されています。

さらに、スキルの出力や設定オプションに関する具体的な情報も改善されており、ユーザーがこれらの機能を効果的に活用するためのサポートが強化されています。この更新により、ユーザーは新しい機能を正しく理解し、効果的に実装するための助けを得られます。

## articles/search/cognitive-search-skill-document-extraction.md{#item-072b72}

<details>
<summary>Diff</summary>
````diff
@@ -5,9 +5,11 @@ ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
+  - doc-kit-assisted
 ms.topic: reference
-ms.date: 01/07/2026
+ms.date: 08/08/2026
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Document Extraction cognitive skill
@@ -82,6 +84,8 @@ The file reference object can be generated one of three ways:
 
 + Setting the `allowSkillsetToReadFileData` parameter on your indexer definition to "true".  This creates a path `/document/file_data` that is an object representing the original file data downloaded from your blob data source. This parameter only applies to files in Blob storage.
 
+  `allowSkillsetToReadFileData` makes the downloaded file data available to the skill. It doesn't increase the [blob indexer file-size or extracted-content limits](search-limits-quotas-capacity.md#indexer-limits).
+
 + Setting the `imageAction` parameter on your indexer definition to a value other than `none`.  This creates an array of images  that follows the required convention for input to this skill if passed individually (that is, `/document/normalized_images/*`).
 
 + Having a custom skill return a json object defined EXACTLY as above.  The `$type` parameter must be set to exactly `file` and the `data` parameter must be the base 64 encoded byte array data of the file content, or the `url` parameter must be a correctly formatted URL with access to download the file at that location.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメント抽出スキルに関する記事の更新"
}
```

### Explanation
この変更は、Azureのドキュメント抽出に関するスキルに関する記事のマイナーな更新です。主な改訂点には、記事の日付が2026年1月7日から2026年8月8日に変更され、「doc-kit-assisted」というカスタム情報が追加されました。また、「ai-usage」フィールドが導入され、AI支援の使用についても言及されています。

具体的には、インデクサ定義における「allowSkillsetToReadFileData」パラメータに関する情報が強化され、この設定を有効にすることでBlobストレージからダウンロードされたファイルデータへのアクセスが可能になることが説明されています。このパラメータは、Blobインデクサーのファイルサイズや抽出されたコンテンツの制限を増加させないことも明記されています。

さらに、「imageAction」パラメータの設定が追加されており、指定した値に応じて画像の配列を生成し、このスキルに必要な形式で画像を入力する方法が説明されています。これらの変更により、ユーザーはドキュメント抽出スキルの利用方法をより良く理解し、適切な設定を行うための重要な情報を得ることができるようになります。

## articles/search/cognitive-search-skill-document-intelligence-layout.md{#item-62c06f}

<details>
<summary>Diff</summary>
````diff
@@ -6,8 +6,9 @@ ms.service: azure-ai-search
 ms.custom:
   - references_regions
   - ignite-2024
+  - doc-kit-assisted
 ms.topic: reference
-ms.date: 04/22/2026
+ms.date: 08/08/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ---
@@ -122,6 +123,8 @@ The file reference object can be generated in one of following ways:
 
 + Setting the `allowSkillsetToReadFileData` parameter on your indexer definition to true. This setting creates a path `/document/file_data` that's an object representing the original file data downloaded from your blob data source. This parameter only applies to files in Azure Blob storage.
 
+  `allowSkillsetToReadFileData` makes the downloaded file data available to the skill. It doesn't increase the [blob indexer limits](search-limits-quotas-capacity.md#indexer-limits) or the Document Intelligence limits described in [Data limits](#data-limits).
+
 + Having a custom skill returning a JSON object definition that provides `$type`, `data`, or `url` and `sastoken`. The `$type` parameter must be set to `file`, and  `data` must be the base 64-encoded byte array of the file content. The `url` parameter must be a valid URL with access for downloading the file at that location.
 
 ## Skill outputs
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスレイアウトスキルに関する記事の更新"
}
```

### Explanation
この変更は、Azureのドキュメントインテリジェンスレイアウトスキルに関する記事のマイナーな更新です。主な改訂点には、記事の日付が2026年4月22日から2026年8月8日に変更され、新たに「doc-kit-assisted」というカスタム情報が追加されました。また、「ai-usage」フィールドが設けられ、AI支援の使用に関する情報が提供されています。

具体的には、インデクサ定義における「allowSkillsetToReadFileData」パラメータに関しての情報が明確化され、これを設定することでBlobストレージからダウンロードされたファイルデータへのアクセスが可能になることが示されています。このパラメータは、Blobインデクサーの制限やドキュメントインテリジェンスの制限を増加させないことも強調されています。

さらに、カスタムスキルが特定のJSONオブジェクトを生成する方法についての明確なガイドラインが追加されました。このJSONオブジェクトには、ファイルデータを含むための `$type`、`data`、および `url` と `sastoken` パラメータが含まれ、ファイルコンテンツの取り扱いに関する重要な情報が提供されています。これにより、ユーザーはドキュメントインテリジェンスレイアウトスキルの設定や利用において、より具体的で実践的な情報を得られるようになります。

## articles/search/search-document-level-access-overview.md{#item-4bb055}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,13 @@
 ---
 title: Document-Level Access Control
 description: Learn how Azure AI Search enforces document-level access control with security filters, ACLs, RBAC scopes, SharePoint permissions, and Purview sensitivity labels.
-ms.date: 08/05/2026
+ms.date: 08/08/2026
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: concept-article
 ms.custom:
   - build-2025
+  - doc-kit-assisted
 ai-usage: ai-assisted
 ---
 
@@ -36,7 +37,7 @@ Azure AI Search provides four primary approaches to enforce document-level permi
 | Security filters | String comparison. Your application passes in a user or group identity as a string, which populates a filter on a query, excluding any documents that don't match on the string. <br><br>Security filters are a technique for achieving document-level access control. This approach isn't bound to an API so you can use any version or package. |
 | POSIX-like ACL / RBAC scopes (preview) | The Microsoft Entra security principal behind the query token is compared to the permission metadata of documents returned in search results, excluding any documents that don't match on permissions. Access control lists (ACL) permissions apply to Azure Data Lake Storage (ADLS) Gen2 directories and files. Role-based access control (RBAC) scopes apply to ADLS Gen2 content and to Azure blobs. <br><br>Built-in support for identity-based access at the document level is in preview, available in REST APIs and preview Azure SDK packages that provide the feature. For evidence of feature support, check the [SDK version support details](#retrieve-acl-permissions-metadata-during-data-ingestion-process-preview). |
 | Microsoft Purview sensitivity labels (preview) | Indexer extracts sensitivity labels defined in Microsoft Purview from supported data sources (Azure Blob Storage, ADLS Gen2, SharePoint in Microsoft 365, OneLake). These labels are stored as metadata and evaluated at query time to enforce user access based on Microsoft Entra tokens and Purview policy assignments. Labels are also surfaced through [knowledge sources](agentic-knowledge-source-overview.md) and the [agentic retrieval response](agentic-retrieval-how-to-retrieve.md#inspect-sensitivity-label-metadata-in-the-response-preview), allowing AI agents and chat apps consuming a knowledge base to receive the same label-aware filtering. This approach aligns Azure AI Search authorization with your enterprise's Microsoft Information Protection model.|
-| SharePoint in Microsoft 365 ACLs (preview) | When configured, Azure AI Search indexers extract SharePoint document, list item, and ASPX site page permissions directly from Microsoft 365 ACLs. Starting in the 2026-05-01-preview REST API, ACL changes for items with unique permissions are also picked up incrementally on each successful indexer run. Access checks use Microsoft Entra user and group memberships, with SharePoint site groups also supported in the same preview (subject to extra configuration). Requires Microsoft Graph `Sites.FullControl.All` (to read SharePoint content and ACLs) on the app registration; `User.Read.All` is additionally required when you index list items or ASPX site pages (to resolve the email addresses returned by the SharePoint REST API into Microsoft Entra object IDs). For the full per-scenario permission matrix, including minimum-permission combinations, see [Permissions by ACL scenario](search-indexer-sharepoint-access-control-lists.md#permissions-by-acl-scenario). |
+| SharePoint in Microsoft 365 ACLs (preview) | Azure AI Search indexers extract permission metadata from supported SharePoint content and use it for query-time access checks. For supported content, principals, group relationships, synchronization behavior, and permissions, see [Use a SharePoint indexer to ingest permission metadata](search-indexer-sharepoint-access-control-lists.md). |
 
 ## Choose an approach
 
@@ -49,8 +50,6 @@ Use the following criteria to identify the approach that best fits your data sou
 | Enterprise content already governed by Microsoft Purview information protection policies. | Microsoft Purview sensitivity labels | Reuses centralized classification and policy assignments across Azure AI Search. |
 | Content sourced from SharePoint in Microsoft 365 (libraries, lists, ASPX site pages). | SharePoint in Microsoft 365 ACLs | Honors native SharePoint permissions, including SharePoint site groups. |
 
-For a side-by-side feature comparison (supported principals, item types, sync behavior, and API surface), see the linked pattern sections later in this article and [How to index SharePoint in Microsoft 365 document-level permissions (preview)](search-indexer-sharepoint-access-control-lists.md).
-
 ## Pattern for security trimming using filters
 
 For scenarios where native ACL/RBAC scopes integration isn't viable, use security string filters to trim results based on exclusion criteria. The pattern includes the following components:
@@ -116,31 +115,9 @@ If your skillset chunks documents, such as with the Text Split skill for integra
 
 ## Pattern for SharePoint in Microsoft 365 basic ACL permissions ingestion (preview)
 
-For SharePoint in Microsoft 365 content, Azure AI Search can apply document-level permissions based on SharePoint ACLs. With this integration, only users or groups that have access to the source item in SharePoint can retrieve it from search results. The match takes effect after the ACL metadata is written to the index by the next successful [scheduled indexer](search-howto-schedule-indexers.md) runs that follow the source change. ACL ingestion applies to documents in libraries, items in [SharePoint lists](search-how-to-index-sharepoint-online.md#index-sharepoint-lists), and [ASPX site pages](search-how-to-index-sharepoint-online.md#index-aspx-site-pages).
-
-SharePoint ACL support is available in preview through the SharePoint indexer using the [2026-05-01-preview REST API](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true) or supported SDK.
-
-This pattern includes the following components:
-
-- Use the SharePoint in Microsoft 365 indexer with application permissions to read SharePoint site content and full permissions to read ACLs. Follow the [SharePoint indexer ACL configuration steps](search-indexer-sharepoint-access-control-lists.md#configure-your-search-service-for-acl-ingestion-and-query-time-enforcement) for enablement and limitations.
-- During initial indexing, SharePoint ACL entries (users and groups) are stored as permission metadata in the search index.
-- Starting in the 2026-05-01-preview REST API, SharePoint ACL synchronization follows this model:
-  - Changes on items with unique permissions are detected and refreshed on each successful indexer run.
-  - Changes inherited from parent scopes (site, library, list, or folder) require an explicit refresh, such as `/resync` with `options: ["permissions"]` or `/resetdocs`. For more information, see [Synchronize permissions between indexed and source content](search-indexer-sharepoint-access-control-lists.md#synchronize-permissions-between-indexed-and-source-content).
-
-- At query time, Azure AI Search checks the Microsoft Entra principal in the query token against SharePoint ACL metadata stored in the index. It excludes any items the caller isn't authorized to access.
-
-During the preview, the following principal types are supported in SharePoint ACLs:
-
-- Microsoft Entra user accounts
-- Microsoft Entra security groups
-- Microsoft 365 groups
-- Mail-enabled security groups
-- SharePoint site groups (preview, starting in the 2026-05-01-preview REST API). Requires extra index configuration. For more information, see [Configure SharePoint groups support](search-indexer-sharepoint-access-control-lists.md#configure-sharepoint-groups-support).
-
-[SharePoint Information Management policies](/sharepoint/intro-to-info-mgmt-policies) that gate user access aren't evaluated, ingested, or honored at query time.
+For indexed SharePoint content, Azure AI Search can store source permissions as metadata and use them to filter query results. You can access this capability in preview through the SharePoint in Microsoft 365 indexer and the `2026-05-01-preview` REST API or an equivalent preview SDK package.
 
-For configuration details and full limitations, see [How to index SharePoint in Microsoft 365 document-level permissions (preview)](search-indexer-sharepoint-access-control-lists.md). For an end-to-end configuration walkthrough including SharePoint site group support, see [Configure SharePoint groups support](search-indexer-sharepoint-access-control-lists.md#configure-sharepoint-groups-support).
+For permission requirements, supported group relationships, permission synchronization, and limitations, see [Use a SharePoint indexer to ingest permission metadata](search-indexer-sharepoint-access-control-lists.md).
 
 If your skillset chunks documents (for example, with the Text Split skill for integrated vectorization), the ACL fields move from indexer field mappings to index projections. See [Choose where to populate ACL fields](search-indexer-sharepoint-access-control-lists.md#choose-where-to-populate-acl-fields).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントレベルアクセス制御に関する記事の更新"
}
```

### Explanation
この変更は、Azureのドキュメントレベルアクセス制御に関する記事のマイナーな更新です。主な改訂点は、記事の日付が2026年8月5日から2026年8月8日に変更され、「doc-kit-assisted」というカスタム情報が追加されたことです。また、AI支援の使用についての情報も含まれています。

具体的には、文書のアクセス制御のための4つの主なアプローチが紹介されています。これには、セキュリティフィルタ、POSIXに似たACL/RBACスコープ、Microsoft Purviewの感度ラベル、そしてMicrosoft 365 SharePointのACLが含まれています。特に、SharePointのACLの説明が修正され、通常のフィルタリングを使用して文書アクセスを制御する方法が強調されています。

また、記事から削除された多くの行により、内容が整理され、より明確で簡潔な情報が提供されるようになりました。これにより、ユーザーはそれぞれのアプローチの利点や制限、関連する設定手順をより簡単に理解できるようになります。全体として、これらの変更により、ドキュメントレベルアクセス制御に関する理解を深めるための重要な情報が提供されています。

## articles/search/search-file-storage-integration.md{#item-d20e26}

<details>
<summary>Diff</summary>
````diff
@@ -4,12 +4,10 @@ description: Set up an Azure Files indexer to automate indexing of file shares i
 ms.reviewer: magottei
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 01/23/2026
+ms.date: 08/08/2026
 ms.update-cycle: 180-days
-ms.custom:
-  - ignite-2023
-  - ignite-2024
-  - sfi-ropc-nochange
+ai-usage: ai-assisted
+ms.custom: [ignite-2023, ignite-2024, sfi-ropc-nochange, doc-kit-assisted]
 ---
 
 # Index data from Azure Files (preview)
@@ -41,6 +39,8 @@ To configure and run the indexer, you can use:
 
 + Files containing text. If you have binary data, you can include [AI enrichment](cognitive-search-concept-intro.md) for image analysis.
 
++ Source files processed by the Azure Files indexer use the [shared source-file size and extracted-character limits for blob-like indexers](search-limits-quotas-capacity.md#indexer-limits).
+
 + Read permissions on Azure Storage. A "full access" connection string includes a key that grants access to the content.
 
 + Use a [REST client](search-get-started-text.md) to formulate REST calls similar to the ones shown in this article.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Filesインデクサに関する記事の更新"
}
```

### Explanation
この変更は、Azure Filesインデクサに関する記事のマイナーな更新です。主な改訂点として、記事の日付が2026年1月23日から2026年8月8日に変更されました。また、「ai-usage」フィールドが追加され、AI支援に関する情報が明確にされたことも特筆すべき点です。

さらに、記事の内容が一部整理され、新たに「ファイルがテキストを含むと、バイナリデータがある場合にはAI強化を利用して画像分析ができる」との具体的な説明が追加されました。これにより、ユーザーはファイルストレージの統合方法について、より実用的で有用な情報を得ることができます。また、Azure Filesインデクサによって処理されるソースファイルの制限についても、新たに言及されるようになり、ユーザーが使用する際の注意点を理解する上で役立つ内容となっています。

全体として、これらの変更により、Azure Filesインデクサの設定および使用に関する内容がより明確になり、読者が最新の情報に基づいて行動できるよう配慮されています。

## articles/search/search-how-to-index-azure-blob-storage.md{#item-353b6b}

<details>
<summary>Diff</summary>
````diff
@@ -4,13 +4,15 @@ description: Learn how to set up a blob indexer to automate indexing of Azure Bl
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/10/2026
+ms.date: 08/08/2026
 ms.update-cycle: 180-days
+ai-usage: ai-assisted
 ms.custom:
   - ignite-2023
   - ignite-2024
   - sfi-ropc-nochange
   - ai-assisted
+  - doc-kit-assisted
 ---
 
 # Index data from Azure Blob Storage
@@ -42,6 +44,8 @@ This article uses the [Search Service REST APIs](/rest/api/searchservice) to dem
 
 + Blobs providing text content and metadata. If blobs contain binary content or unstructured text, consider adding [AI enrichment](cognitive-search-concept-intro.md) for image and natural language processing. Blob content can't exceed the [indexer limits](search-limits-quotas-capacity.md#indexer-limits) for your pricing tier.
 
+  The blob indexer limits cover the maximum blob size and the number of characters that Azure AI Search extracts from a blob. If you use a skillset, each skill's input or service limit applies separately after document cracking.
+
 + A supported network configuration and data access. At a minimum, you need read permissions in Azure Storage. A storage connection string that includes an access key gives you read access to storage content. If instead you're using Microsoft Entra logins and roles, make sure the [search service's managed identity](search-how-to-managed-identities.md) has **Storage Blob Data Reader** permissions.
 
   By default, both search and storage accept requests from public IP addresses. If network security isn't an immediate concern, you can index blob data using just the connection string and read permissions. When you're ready to add network protections, see [Indexer access to content protected by Azure network security features](search-indexer-securing-resources.md) for guidance about data access.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Blob Storageインデクサに関する記事の更新"
}
```

### Explanation
この変更は、Azure Blob Storageインデクサに関する記事のマイナーな更新です。主な改訂点として、記事の日付が2026年6月10日から2026年8月8日に変更されました。また、「ai-usage」というフィールドが新たに追加され、AI支援の利用に関する情報が明確にされました。

記事の内容においては、Blobがテキストコンテンツやメタデータを提供する場合の注意点が強調され、バイナリコンテンツや非構造化テキストが含まれている場合にはAI強化を追加することを考慮するように案内されています。さらに、Blobインデクサの制限についても具体的な情報が追加され、データのサイズや抽出できる文字数に関する制約が説明されています。

また、Azure Storageへのデータアクセスに関連するネットワーク構成についての説明も改訂され、Microsoft Entraのログインやロールを使用する場合は、検索サービスのマネージドIDが「Storage Blob Data Reader」権限を持っている必要があることが明記されています。

全体として、これらの変更により、Azure Blob Storageインデクサの設定や使用に関する重要な情報が更新され、読者がより効果的にこのサービスを活用できるようになっています。

## articles/search/search-how-to-index-azure-data-lake-storage.md{#item-faca23}

<details>
<summary>Diff</summary>
````diff
@@ -4,12 +4,10 @@ description: Set up an Azure Data Lake Storage (ADLS) Gen2 indexer to automate i
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/21/2026
+ms.date: 08/08/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
-ms.custom:
-  - ignite-2023
-  - sfi-ropc-nochange
+ms.custom: [ignite-2023, sfi-ropc-nochange, doc-kit-assisted]
 ---
 
 # Index data from Azure Data Lake Storage Gen2
@@ -40,6 +38,8 @@ For a code sample in C#, see [Index Data Lake Gen2 using Microsoft Entra ID](htt
 
 + Blobs containing text. If you have binary data, you can include [AI enrichment](cognitive-search-concept-intro.md) for image analysis. Blob content can't exceed the [indexer limits](search-limits-quotas-capacity.md#indexer-limits) for your search service tier.
 
+  Treat source indexing and AI enrichment as separate processing stages. A skill or external service can have a lower input limit than the amount of content the indexer can extract. Check the [reference article for each skill](cognitive-search-predefined-skills.md) in your skillset.
+
 + Read permissions on Azure Storage. A "full access" connection string includes a key that grants access to the content, but if you're using Azure roles instead, make sure the [search service managed identity](search-how-to-managed-identities.md) has **Storage Blob Data Reader** permissions.
 
 + Use a [REST client](search-get-started-text.md) to formulate REST calls similar to the ones shown in this article.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Data Lake Storageインデクサに関する記事の更新"
}
```

### Explanation
この変更は、Azure Data Lake Storage (ADLS) Gen2インデクサに関する記事のマイナーな更新です。主な改訂点として、記事の日付が2026年7月21日から2026年8月8日に変更されました。また、AI支援の利用が明示される「ai-usage」というフィールドが新たに追加されました。

記事の内容には、テキストを含むBlobに関する情報が追加され、バイナリデータがある場合にはAI強化を通じて画像分析を使用することが推奨されています。さらに、ソースインデクシングとAI強化を別の処理ステージとして扱うことの重要性が強調されており、スキルや外部サービスがインデクサが抽出できるコンテンツの量よりも低い入力制限を持つ可能性があることが説明されています。

加えて、Azure Storageに対する読み取り権限についての詳細も改訂され、「フルアクセス」の接続文字列にはキーが含まれ、コンテンツへのアクセスを許可することが明記されています。また、Azureロールを使用する場合には、「検索サービスのマネージドID」が「Storage Blob Data Reader」権限を有する必要があることも説明されています。

全体として、これらの変更により、Azure Data Lake Storage Gen2のインデクサを設定し使用する際に考慮すべき重要な情報が更新され、読者がこの技術をより効果的に活用できるよう配慮されています。

## articles/search/search-how-to-index-onelake-files.md{#item-95f3db}

<details>
<summary>Diff</summary>
````diff
@@ -4,13 +4,14 @@ description: Set up a OneLake indexer to automate indexing of content and metada
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/04/2026
+ms.date: 08/08/2026
 ai-usage: ai-assisted
 ms.custom:
   - build-2024
   - ignite-2024
   - sfi-image-nochange
   - sfi-ropc-nochange
+  - doc-kit-assisted
 ---
 
 # Index data from OneLake files and shortcuts
@@ -24,7 +25,7 @@ ms.custom:
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-In this article, learn how to configure a OneLake files indexer for extracting searchable data and metadata data from a [lakehouse](/fabric/onelake/create-lakehouse-onelake) on top of [Microsoft OneLake](/fabric/onelake/onelake-overview).
+In this article, you learn how to configure a OneLake files indexer for extracting searchable data and metadata from a [lakehouse](/fabric/onelake/create-lakehouse-onelake) on top of [Microsoft OneLake](/fabric/onelake/onelake-overview).
 
 To configure and run the indexer, you can use:
 
@@ -42,6 +43,8 @@ This article uses the REST APIs to illustrate each step.
 
 + Textual data. If you have binary data, you can use [AI enrichment](cognitive-search-concept-intro.md) image analysis to extract text or generate descriptions of images. File content can't exceed the [indexer limits](search-limits-quotas-capacity.md#indexer-limits) for your search service tier.
 
+  Source-file processing and AI enrichment have separate limits. A downstream skill or external service can accept less data than the indexer extracts, so check the [reference article for each skill](cognitive-search-predefined-skills.md) in your skillset.
+
 + Unstructured content in the **Files** location of your lakehouse. You can add data by:
 
   + [Upload into a lakehouse directly](/fabric/onelake/create-lakehouse-onelake#load-data-into-a-lakehouse)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLakeファイルインデクサに関する記事の更新"
}
```

### Explanation
この変更は、OneLakeファイルのインデクサに関する記事のマイナーな更新です。主な改訂点として、記事の日付が2026年8月4日から2026年8月8日に変更され、AI支援の利用を示す「ai-usage」というフィールドが含まれています。

記事の内容には、OneLakeファイルインデクサを構成する方法についての情報が含まれており、検索可能なデータとメタデータをMicrosoft OneLakeのレイクハウスから抽出する手順が紹介されています。また、文章の表現が一部修正され、より明確な情報提供が行われています。

さらに、テキストデータに関する章が追加され、バイナリデータがある場合にはAI強化を利用して画像のテキストを抽出したり、説明を生成したりすることが推奨されています。ソースファイルの処理とAI強化には別々の制限があることにも言及され、ダウンストリームスキルや外部サービスがインデクサが抽出するデータよりも少ないデータしか受け取れない場合があることが説明されています。

最後に、レイクハウスの「Files」場所にある非構造化コンテンツにデータを追加する方法についても具体的な手順が提供されています。

これらの変更により、OneLakeファイルインデクサに関する記事がより正確で役立つ情報を提供するようアップデートされ、読者がこの機能を活用する際の手助けとなることが期待されます。

## articles/search/search-how-to-index-sharepoint-online.md{#item-8c099c}

<details>
<summary>Diff</summary>
````diff
@@ -4,12 +4,13 @@ description: Set up a SharePoint in Microsoft 365 indexer to automate indexing o
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/23/2026
+ms.date: 08/08/2026
 ai-usage: ai-assisted
 ms.custom:
   - ignite-2025
   - sfi-image-nochange
   - sfi-ropc-nochange
+  - doc-kit-assisted
 ---
 
 # Index content from SharePoint in Microsoft 365 (preview)
@@ -61,23 +62,19 @@ In Azure AI Search, an indexer extracts searchable data and metadata from a data
 
 ## Choose your permissions setup
 
-
 Before you create the app registration in [Step 3](#step-3-create-a-microsoft-entra-application-registration), identify your scenario in the following table. Note the required Microsoft Graph permissions, SharePoint API permissions, and credential type. Then, follow the linked steps later in this article to apply them.
 
 | Scenario | Microsoft Graph permissions | SharePoint API permissions | Credential | Apply in |
 |---|---|---|---|---|
 | Index document libraries only, no ACL ingestion | `Files.Read.All`, `Sites.Read.All` (application) or delegated equivalents | None | Client secret (application) or device code (delegated) | [Step 3](#step-3-create-a-microsoft-entra-application-registration), [Step 6](#step-6-create-an-indexer) |
 | Index lists, ASPX pages, or mixed content (no ACL ingestion) | `Files.Read.All`, `Sites.Read.All` (application) | None | Client secret or federated credential | [Step 3](#step-3-create-a-microsoft-entra-application-registration) |
-| Document library ACL ingestion, Microsoft Entra users and standard groups only | `Files.Read.All`, `Sites.FullControl.All` (or `Sites.Selected`) | None | Client secret or federated credential | [Step 3](#step-3-create-a-microsoft-entra-application-registration), [Permissions by ACL scenario](search-indexer-sharepoint-access-control-lists.md#permissions-by-acl-scenario) |
-| ACL ingestion on lists, ASPX pages, or document libraries when SharePoint site groups must be honored | `Files.Read.All`, `Sites.FullControl.All` (or `Sites.Selected`) | `Sites.FullControl.All` (or `Sites.Selected`) | Federated credential (required) | [Configuring the registered application with a managed identity](#configuring-the-registered-application-with-a-managed-identity), [Permissions by ACL scenario](search-indexer-sharepoint-access-control-lists.md#permissions-by-acl-scenario) |
-| Query-time resolution of SharePoint site groups | No additional Microsoft Graph permissions (inherits from the prior row when also indexing document libraries, lists, or ASPX pages) | `User.Read.All` | Federated credential | [Configure SharePoint groups support](search-indexer-sharepoint-access-control-lists.md#configure-sharepoint-groups-support) |
+| ACL ingestion or query-time resolution of SharePoint site groups | [See the ACL permission matrix](search-indexer-sharepoint-access-control-lists.md#permissions-by-acl-scenario). | [See the ACL permission matrix](search-indexer-sharepoint-access-control-lists.md#permissions-by-acl-scenario). | [See the ACL permission matrix](search-indexer-sharepoint-access-control-lists.md#permissions-by-acl-scenario). | [Permissions by ACL scenario](search-indexer-sharepoint-access-control-lists.md#permissions-by-acl-scenario) |
 
 When setting up permissions, consider the following information:
 
 - Delegated permissions are only viable for small testing and don't support ACL ingestion.
 - Federated credential is the recommended secretless authentication. It covers both indexer authentication and query-time SharePoint group resolution.
 - When you use `Sites.Selected`, grant the app explicit access to each target SharePoint site before indexing. Admin consent for `Sites.Selected` in Microsoft Entra ID doesn't by itself authorize the app to access site content. You must also assign a permission on each target site. If you add a site to the data source without an explicit site permission grant, the indexer fails. See [Grant site access when using `Sites.Selected`](#grant-site-access-when-using-sitesselected).
-- This matrix is the entry-point summary. For ACL-specific scenario details, see [Permissions by ACL scenario](search-indexer-sharepoint-access-control-lists.md#permissions-by-acl-scenario) in the SharePoint ACL configuration article.
 
 ## Supported document formats
 
@@ -119,15 +116,17 @@ Here are some considerations when using this feature:
   
 Regardless of the approach you choose, whether building a custom connector with SharePoint webhooks or creating an Azure Logic Apps workflow, be sure to implement robust security measures. These measures include configuring shared private links, setting up firewalls, and preserving user permissions from the source and honoring those permissions at query time. You should also regularly audit and monitor your pipeline.
 
+If you index SharePoint ACLs, review the [supported group relationships](search-indexer-sharepoint-access-control-lists.md#supported-group-relationships). Microsoft Entra groups nested within SharePoint groups aren't expanded.
+
 ## Configure the SharePoint in Microsoft 365 indexer
 
 To set up the SharePoint in Microsoft 365 indexer, use a preview REST API. This section provides the steps. 
 
 ### (Optional) Step 1: Enable a system-assigned managed identity
 
-Enable a [system-assigned managed identity](search-how-to-managed-identities.md#create-a-system-managed-identity) to automatically detect the tenant in which the search service is provisioned. 
+Enable a [system-assigned managed identity](search-how-to-managed-identities.md#create-a-system-managed-identity) to automatically detect the Microsoft Entra tenant in which the search service is provisioned.
 
-Perform this step if the SharePoint site is in the same tenant as the search service. Skip this step if the SharePoint site is in a different tenant. The identity is used for tenant detection. You can also skip this step if you want to put the tenant ID in the [connection string](#connection-string-format). To use system-assigned or user-assigned managed identity for secretless indexing, configure the [application permissions with secretless authentication](#using-secretless-authentication-to-obtain-application-tokens).
+Perform this step if the SharePoint site and search service are in the same Microsoft Entra tenant. Skip this step if they're in different Microsoft Entra tenants. The identity is used for tenant detection. You can also skip this step if you want to put the Microsoft Entra tenant ID in the [connection string](#connection-string-format). To use system-assigned or user-assigned managed identity for secretless indexing, configure the [application permissions with secretless authentication](#using-secretless-authentication-to-obtain-application-tokens).
 
 :::image type="content" source="media/search-howto-index-sharepoint-online/enable-managed-identity.png" alt-text="Screenshot showing how to enable system assigned managed identity.":::
 
@@ -144,7 +143,7 @@ For the decision matrix that covers ACL and non-ACL scenarios, see [Choose your
 
 ### Step 3: Create a Microsoft Entra application registration
 
-The SharePoint in Microsoft 365 indexer uses a Microsoft Entra application for authentication. Create the application registration in the same tenant as Azure AI Search.
+The SharePoint in Microsoft 365 indexer uses a Microsoft Entra application for authentication. Create the application registration before you configure its permissions and credentials.
 
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
@@ -342,23 +341,23 @@ The format of the connection string changes based on whether the indexer is usin
 
 + Delegated API permissions connection string format
 
-    `SharePointOnlineEndpoint=[SharePoint site url];ApplicationId=[Azure AD App ID];TenantId=[SharePoint site tenant id]`
+    `SharePointOnlineEndpoint=[SharePoint site URL];ApplicationId=[Microsoft Entra application ID];TenantId=[SharePoint site's Microsoft Entra tenant ID]`
 
 + Application API permissions with application secret connection string format
 
-    `SharePointOnlineEndpoint=[SharePoint site url];ApplicationId=[Azure AD App ID];ApplicationSecret=[Azure AD App client secret];TenantId=[SharePoint site tenant id]`
+    `SharePointOnlineEndpoint=[SharePoint site URL];ApplicationId=[Microsoft Entra application ID];ApplicationSecret=[Microsoft Entra application client secret];TenantId=[SharePoint site's Microsoft Entra tenant ID]`
 
 + Application API permissions with secretless (federated identity credential) connection string format:
 
-    `SharePointOnlineEndpoint=[SharePoint site url];ApplicationId=[Azure AD App ID];FederatedCredentialApplicationId=[managed identity's application (client) ID];TenantId=[SharePoint site tenant id]`
+    `SharePointOnlineEndpoint=[SharePoint site URL];ApplicationId=[Microsoft Entra application ID];FederatedCredentialApplicationId=[managed identity's application (client) ID];TenantId=[SharePoint site's Microsoft Entra tenant ID]`
 
 The following table describes each connection string field.
 
 | Field | Required | Description |
 |---|---|---|
 | `SharePointOnlineEndpoint` | Yes | SharePoint site URL (for example, `https://[your-tenant-name].sharepoint.com`). |
 | `ApplicationId` | Yes | Microsoft Entra application (client) ID of the ingestion app. Must be a valid GUID. |
-| `TenantId` | Optional | Microsoft Entra tenant GUID. Required when the SharePoint site is in a different tenant from the search service. |
+| `TenantId` | Optional | Microsoft Entra tenant ID (GUID) for the tenant that owns the SharePoint site. This tenant isn't necessarily the Microsoft Entra tenant associated with the search service. Required when the SharePoint site and search service are in different Microsoft Entra tenants. |
 | `ApplicationSecret` | Conditional | Client secret of the ingestion app. Use for secret-based authentication. |
 | `FederatedCredentialApplicationId` | Conditional (federated identity credential) | Microsoft Entra application (client) ID used to validate the managed identity. Must be a valid GUID. For a system-assigned managed identity, use the identity's application (client) ID. For a user-assigned managed identity, use the identity's own application (client) ID. For a cross-tenant user-assigned managed identity with `federatedIdentityClientId` set in the `identity` block, use the multi-tenant app's client ID. |
 
@@ -368,12 +367,12 @@ The following table describes each connection string field.
 When setting up permissions, consider the following information:
 > For backward compatibility, the SharePoint indexer still accepts `FederatedCredentialObjectId` (the object/principal ID of the federated identity credential on the ingestion app) in the connection string, so existing data sources keep working without changes. Use `FederatedCredentialApplicationId` for new and updated data sources.
 
-You can get `tenantId` from the **Overview** page in the Microsoft Entra admin center in your Microsoft 365 subscription.
+To get `TenantId`, open the Microsoft Entra admin center for the tenant that owns the SharePoint site, and copy the **Tenant ID** from **Overview**.
 
 You can get the managed identity `object (principal) ID` from the [Configuring the registered application with a managed identity](#configuring-the-registered-application-with-a-managed-identity) section.
 
 When setting up permissions, consider the following information:
-> If the SharePoint site is in the same tenant as the search service and system-assigned managed identity is enabled, `TenantId` doesn't have to be included in the connection string. If the SharePoint site is in a different tenant from the search service, `TenantId` must be included.
+> If the SharePoint site and search service are in the same Microsoft Entra tenant and system-assigned managed identity is enabled, you don't have to include `TenantId` in the connection string. If they're in different Microsoft Entra tenants, you must include `TenantId`.
 
 The following examples show data sources created with `FederatedCredentialApplicationId`:
 
@@ -388,7 +387,7 @@ api-key: [admin key]
   "name": "sharepoint-ds",
   "type": "sharepoint",
   "credentials": {
-    "connectionString": "SharePointOnlineEndpoint=https://[your-tenant-name].sharepoint.com;ApplicationId=[Azure AD App ID];TenantId=[SharePoint site tenant id];FederatedCredentialApplicationId=[system-assigned managed identity's application (client) ID]"
+    "connectionString": "SharePointOnlineEndpoint=https://[your-tenant-name].sharepoint.com;ApplicationId=[Microsoft Entra application ID];TenantId=[SharePoint site's Microsoft Entra tenant ID];FederatedCredentialApplicationId=[system-assigned managed identity's application (client) ID]"
   },
   "container": { "name": "defaultSiteLibrary" }
 }
@@ -401,7 +400,7 @@ api-key: [admin key]
   "name": "sharepoint-uami-fed",
   "type": "sharepoint",
   "credentials": {
-    "connectionString": "SharePointOnlineEndpoint=https://[your-tenant-name].sharepoint.com;ApplicationId=[Azure AD App ID];TenantId=[SharePoint site tenant id];FederatedCredentialApplicationId=[user-assigned managed identity application (client) ID]"
+    "connectionString": "SharePointOnlineEndpoint=https://[your-tenant-name].sharepoint.com;ApplicationId=[Microsoft Entra application ID];TenantId=[SharePoint site's Microsoft Entra tenant ID];FederatedCredentialApplicationId=[user-assigned managed identity application (client) ID]"
   },
   "container": { "name": "defaultSiteLibrary" },
   "identity": {
@@ -416,14 +415,14 @@ api-key: [admin key]
 
 **Cross-tenant user-assigned managed identity with federated credential (advanced):**
 
-Before using this configuration, ensure your user-assigned managed identity is configured with a federated identity credential that trusts the multi-tenant Entra app. For setup steps, see [Configuring the registered application with a managed identity](#configuring-the-registered-application-with-a-managed-identity).
+Before using this configuration, ensure your user-assigned managed identity is configured with a federated identity credential that trusts the multitenant Microsoft Entra app. For setup steps, see [Configuring the registered application with a managed identity](#configuring-the-registered-application-with-a-managed-identity).
 
 ```json
 {
   "name": "sharepoint-uami-crosstenantfed",
   "type": "sharepoint",
   "credentials": {
-    "connectionString": "SharePointOnlineEndpoint=https://[your-tenant-name].sharepoint.com;ApplicationId=[Azure AD App ID];TenantId=[SharePoint site tenant id];FederatedCredentialApplicationId=[multi-tenant app client ID]"
+    "connectionString": "SharePointOnlineEndpoint=https://[your-tenant-name].sharepoint.com;ApplicationId=[Microsoft Entra application ID];TenantId=[SharePoint site's Microsoft Entra tenant ID];FederatedCredentialApplicationId=[multitenant app client ID]"
   },
   "container": { "name": "defaultSiteLibrary" },
   "identity": {
@@ -434,7 +433,7 @@ Before using this configuration, ensure your user-assigned managed identity is c
 }
 ```
 
-Use the cross-tenant user-assigned managed identity configuration when the user-assigned managed identity itself federates to a multi-tenant Entra app. In this case, set `federatedIdentityClientId` in the `identity` block to the multi-tenant app's client ID, and set `FederatedCredentialApplicationId` in the connection string to the **same** multi-tenant app's client ID. Setting `FederatedCredentialApplicationId` to the user-assigned managed identity's own client ID in this scenario fails validation.
+Use the cross-tenant user-assigned managed identity configuration when the user-assigned managed identity itself federates to a multitenant Microsoft Entra app. In this case, set `federatedIdentityClientId` in the `identity` block to the multitenant app's client ID, and set `FederatedCredentialApplicationId` in the connection string to the **same** multitenant app's client ID. Setting `FederatedCredentialApplicationId` to the user-assigned managed identity's own client ID in this scenario fails validation.
 
 If your indexer uses [SharePoint ACL configuration (preview)](search-indexer-sharepoint-access-control-lists.md) or [preserves and honors Microsoft Purview sensitivity labels (preview)](search-indexer-sensitivity-labels.md), review the related articles before you create the indexer. Each feature has specific data source, index, and skillset configuration steps.
 
@@ -742,6 +741,8 @@ When setting up permissions, consider the following information:
 
 ## Handle errors
 
+For an `Invalid AAD tenant` message, a missing Microsoft Entra tenant ID, or a tenant mismatch that appears in indexer execution history, see [Troubleshoot common indexer errors and warnings](cognitive-search-common-errors-warnings.md#error-invalid-aad-tenant).
+
 By default, the SharePoint in Microsoft 365 indexer stops as soon as it encounters a document with an unsupported content type, such as an image. Use the `excludedFileNameExtensions` parameter to skip certain content types. However, you might need to index documents without knowing all the possible content types in advance. To continue indexing when the indexer encounters an unsupported content type, set the `failOnUnsupportedContentType` configuration parameter to false:
 
 ```http
@@ -761,12 +762,14 @@ For some documents, Azure AI Search is unable to determine the content type or c
 "parameters" : { "configuration" : { "failOnUnprocessableDocument" : false } }
 ```
 
-Azure AI Search limits the size of documents that it indexes. These limits are documented in [Service Limits in Azure AI Search](./search-limits-quotas-capacity.md). By default, oversized documents are treated as errors. However, you can still index storage metadata of oversized documents if you set the `indexStorageMetadataOnlyForOversizedDocuments` configuration parameter to true:
+SharePoint source files use the [shared source-file size and extracted-character limits for blob-like indexers](search-limits-quotas-capacity.md#indexer-limits). By default, oversized documents are treated as errors. However, you can still index storage metadata of oversized documents if you set the `indexStorageMetadataOnlyForOversizedDocuments` configuration parameter to true:
 
 ```http
 "parameters" : { "configuration" : { "indexStorageMetadataOnlyForOversizedDocuments" : true } }
 ```
 
+If you add a skillset, check each skill's input and downstream service limits separately. A skill can accept less data than the SharePoint indexer extracts.
+
 You can also continue indexing if errors happen at any point of processing, either while parsing documents or while adding documents to an index. To ignore a specific number of errors, set the `maxFailedItems` and `maxFailedItemsPerBatch` configuration parameters to the desired values. For example:
 
 ```http
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint Onlineインデクサに関する記事の更新"
}
```

### Explanation
この変更は、SharePoint Onlineインデクサに関する記事のマイナーな更新です。主な改訂点として、記事の日付が2026年7月23日から2026年8月8日に変更され、新たに「doc-kit-assisted」というAI支援のフィールドが加わっています。

記事内容では、Microsoft 365におけるSharePointのインデクサの設定方法に関する詳細が説明され、アクセス許可の設定に関するセクションが強化されています。具体的に、Microsoft Graph APIやSharePoint APIの権限に関する明確なテーブルが追加され、インデクサの作成に必要な権限を簡単に確認できるようになっています。

さらに、接続文字列のフォーマットに関する文言が修正され、特にMicrosoft EntraのアプリケーションIDやテナントIDに関する説明が明確化されています。また、前のバージョンの接続方式との互換性を保つための注意点も記載されています。

エラー処理やドキュメントのサイズ制限に関するセクションも充実し、具体的な設定パラメータを示しながら、インデクサが遭遇する可能性のあるエラーや問題についての対処法が詳述されています。

全体として、これらの変更によって、SharePoint Onlineインデクサに関する記事がより使いやすく、実用的な情報を提供できるものになっており、特に開発者や管理者にとって役立つリソースとなっています。

## articles/search/search-indexer-high-density-serverless-overview.md{#item-2bc606}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,12 @@
 ﻿---
 title: Indexer Execution on Serverless and S3 HD
-description: Learn how Azure AI Search runs indexers on Serverless and S3 High Density (S3 HD) search services.
-author: gmndrg
-ms.author: gimondra
+description: Learn how Azure AI Search runs indexers, applies daily runtime quotas, and reports remaining capacity on Serverless and S3 HD services.
+ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 06/02/2026
+ms.date: 08/08/2026
 ai-usage: ai-assisted
+ms.custom: doc-kit-assisted
 ---
 
 # Indexer execution on Serverless and Standard 3 High Density (S3 HD)
@@ -18,17 +18,17 @@ This article describes the indexer execution model that Azure AI Search uses for
 > [!IMPORTANT]
 > The capabilities described in this article are in preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> + Indexer support on S3 HD requires the [`2026-05-01-preview` REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) or later.
+> + Indexer support on S3 HD requires the [`2025-11-01-preview` REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) or later.
 > + Serverless indexer support requires the [`2026-05-01-preview` REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) or later.
 
 ## Where it applies
 
 The execution model in this article applies to:
 
-+ Serverless search services that run indexers using the `2026-05-01-preview` REST API or later.
-+ S3 HD search services that run indexers using the `2026-05-01-preview` REST API or later.
++ [Serverless search services](serverless-cost-optimization.md) that run indexers by using the `2026-05-01-preview` REST API or later.
++ S3 HD search services that run indexers by using the `2025-11-01-preview` REST API or later.
 
-Existing indexer definitions, data sources, skillsets, and knowledge sources work without modification on both options.
+Supported indexer definitions, data sources, skillsets, and indexer-backed knowledge sources work without modification on both options. File knowledge sources aren't supported on Serverless.
 
 ## Execution model
 
@@ -156,10 +156,12 @@ During the preview, Serverless indexers are designed to simplify ingestion for r
 
 For indexer limits on Serverless and S3 HD, see [Indexer limits](search-limits-quotas-capacity.md#indexer-limits).
 
+The service-level runtime quota and indexer limits don't replace the input, request, or processing limits of skills and external services in a skillset. Check each skill reference separately when you size an enrichment pipeline.
+
 ## Related content
 
 + [Indexers in Azure AI Search](search-indexer-overview.md)
 + [Run or reset indexers](search-howto-run-reset-indexers.md)
-+ [Monitor indexer status and results](search-howto-monitor-indexers.md)
++ [Monitor indexer status and results](search-monitor-indexers.md)
 + [Knowledge sources](agentic-knowledge-source-overview.md)
 + [Service limits in Azure AI Search](search-limits-quotas-capacity.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスおよびS3 HDインデクサに関する記事の更新"
}
```

### Explanation
この変更は、Azure AI SearchのサーバーレスおよびS3高密度（S3 HD）サービス上でのインデクサの実行に関する記事のマイナーな更新です。主な改訂内容には、記事の説明文が改訂され、インデクサの実行モデルに関する情報がより詳細に追加されています。これにより、日次の実行クォータや残りの容量についての報告方法が明確化しています。

また、REST APIのバージョンに関する情報が更新され、S3 HDにおいては、以前のバージョンから最新の`2025-11-01-preview` REST APIを使用する必要があることが強調されています。サーバーレスインデクサに関しては、依然として`2026-05-01-preview` REST APIを使用し続ける必要があります。

「適用対象」セクションでは、サーバーレス検索サービスおよびS3 HDサービスでのインデクサの実行モデルに関する詳細が提供され、必要なインデクサ定義やデータソース、スキルセット、ノウハウソースのサポートに関する情報が整理されています。特に、ファイルノウハウソースがサーバーレスではサポートされていないことも明記されています。

最後に、インデクサの実行に関する新しい関係性のコンテンツリンクが追加され、ユーザーが関連情報をより容易に見つけられるように改善されています。このように、全体的に記事がより実用的かつ情報豊かになるようにアップデートされています。

## articles/search/search-indexer-sharepoint-access-control-lists.md{#item-532a24}

<details>
<summary>Diff</summary>
````diff
@@ -4,8 +4,9 @@ description: Learn how to configure Azure AI Search indexers for ingesting Acces
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/30/2026
+ms.date: 08/08/2026
 ai-usage: ai-assisted
+ms.custom: doc-kit-assisted
 ---
 
 # Use a SharePoint indexer to ingest permission metadata and filter search results based on user access rights (preview)
@@ -86,6 +87,18 @@ This preview supports basic ACLs for documents, list items, and modern ASPX site
 | Information Management policies | Policies to define specific permissions requirements. | ❌ | Not supported in preview. |
 | Purview sensitivity labels  | Document-level security for privacy, categorization, permissions, and encryption  | ❌ | Supported via a separate feature: [preserving and honoring sensitivity labels](search-indexer-sensitivity-labels.md). |
 
+### Supported group relationships
+
+Microsoft Entra group transitivity applies within Microsoft Entra. It doesn't expand Microsoft Entra groups that are members of SharePoint groups.
+
+| Permission relationship | Supported | Guidance |
+|---|---|---|
+| User or Microsoft Entra group assigned directly to the SharePoint item | Yes | The indexer stores the user or Microsoft Entra group object ID in the item's permission metadata. |
+| User reaches an assigned Microsoft Entra group through transitive Microsoft Entra group nesting | Yes | Query-time Microsoft Graph resolution expands the user's transitive Microsoft Entra group memberships. |
+| User assigned directly to a SharePoint site group that has access to the item | Yes | Configure [SharePoint groups support](#configure-sharepoint-groups-support). |
+| Microsoft Entra group nested within a SharePoint group | No | SharePoint group resolution doesn't expand the nested Microsoft Entra group. Results that depend on this relationship are filtered out. Add users directly to the SharePoint group or grant permission through a supported Microsoft Entra group assignment. |
+| Other mixed SharePoint and Microsoft Entra nesting directions | Not specified | Don't infer support from Microsoft Entra transitivity. This preview limitation is scoped to Microsoft Entra groups nested within SharePoint groups. |
+
 ## How hierarchical permissions are evaluated
 
 SharePoint permissions inherit the hierarchy of Site → Library → Folder → File, unless inheritance is broken.
@@ -419,6 +432,8 @@ After indexing your data and ACLs, you can [query the index](search-query-access
 | `federatedCredentialId` is rejected when configuring `sharePointConnectorAppRegistration` | Use the ID (GUID) of the federated identity credential on the app registration, not the app object ID or the managed identity principal ID. |
 | The indexer returns `401 Unauthorized` and `FederatedCredentialApplicationId` is set | Verify you used the managed identity's Application ID (found in **Enterprise applications**), not the app registration's Application (client) ID or any Object ID. For a user-assigned managed identity, use the **Client ID** from the managed identity resource's **Properties** page. See [Find the correct Microsoft Entra identifiers](#find-the-correct-microsoft-entra-identifiers). |
 
+For missing, unexpected, or failed query-time results after ACL metadata is indexed, see [Troubleshoot SharePoint permission filtering](troubleshoot-sharepoint-query-permission-filtering.md).
+
 ## Related content
 
 + [Index SharePoint content in Azure AI Search (preview)](search-how-to-index-sharepoint-online.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointアクセス制御リストに関する記事の更新"
}
```

### Explanation
この変更は、Azure AI SearchにおけるSharePointのアクセス制御リスト（ACL）の取り扱いに関する記事のマイナーな更新です。主な内容として、記事の日付が2026年7月30日から2026年8月8日に変更され、AI支援に関する「doc-kit-assisted」という新しいメタデータが追加されています。

更新された内容では、Microsoft Entraグループの関係性についての新しいセクションが追加され、ACLのサポートに関する詳細情報が提供されています。このセクションでは、SharePointアイテムに割り当てられたユーザーやMicrosoft Entraグループの直接的な関係、トランジティブなグループメンバーシップの解決方法、SharePointサイトグループに対する直接的な割り当て、入れ子になったグループの未解決などが詳述されています。

特に、Microsoft EntraグループがSharePointグループの一部である場合には、そのグループが拡張されず、関連する結果がフィルタリングされることに留意が必要です。この制限により、ユーザーはSharePointグループに直接追加するか、サポートされるMicrosoft Entraグループの割り当てを行う必要があります。

その他、問い合わせ時のACLメタデータのインデックス後に予期しない結果が得られた場合のトラブルシューティングガイドへのリンクも追加され、関連文書へのリンクも強化されています。これにより、ユーザーが情報を迅速に調査し、問題解決を図ることができるようになっています。全体的に、記事はより実用的かつ役立つ情報を提供する内容に改善されています。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -5,11 +5,12 @@ author: mattwojo
 ms.author: mattwoj
 ms.service: azure-ai-search
 ms.topic: limits-and-quotas
-ms.date: 08/04/2026
+ms.date: 08/08/2026
 ms.update-cycle: 180-days
 ai-usage: ai-assisted
 ms.custom:
   - references_regions
+  - doc-kit-assisted
 #customer intent: As a developer making decisions about the infrastructure we use, planning to optimize for usage need, capacity, and cost, I want to understand the limits, quotas, and capacities associated with Azure AI Search services, detailing how these factors depend on the chosen pricing tier.
 ---
 
@@ -217,6 +218,7 @@ Maximum running times exist to provide balance and stability to the service as a
 > [!NOTE]
 > In the Serverless pricing model, indexer behavior differs from Dedicated services. Capacity isn't defined by replicas or partitions. Instead, per-service object limits, per-index storage caps, and service-level throttling govern indexing limits. As a result, some limits, such as maximum execution time, aren't fixed values.
 
+### Indexer object and throughput limits
 
 | Resource | Free&nbsp;<sup>1</sup> | Basic&nbsp;<sup>2</sup> | S1 | S2 | S3 | S3&nbsp;HD&nbsp;<sup>3</sup> | L1 | L2 | Serverless Developer |
 | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
@@ -226,8 +228,6 @@ Maximum running times exist to provide balance and stability to the service as a
 | Maximum indexing load per invocation | 10,000 docs | Limited only by max docs | Limited only by max docs | Limited only by max docs | Limited only by max docs | N/A | No limit | No limit | Limited only by max docs |
 | Minimum schedule | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min |
 | Maximum running time <sup>5</sup> | 1-3 or 3-10 min | 2 or 24 hours | 2 or 24 hours | 2 or 24 hours | 2 or 24 hours | N/A | 2 or 24 hours | 2 or 24 hours | 2 hours |
-| Blob indexer <sup>7</sup>: maximum blob size, MB | 16 | 16 | 128 | 256 | 256 | N/A  | 256 | 256 | 256 |
-| Blob indexer: maximum characters of content extracted from a blob <sup>6</sup> <sup>8</sup> | 256,000 | 512,000 | 4&nbsp;mil | 8&nbsp;mil | 16&nbsp;mil | N/A | 4&nbsp;mil | 4&nbsp;mil | 16&nbsp;mil |
 
 <sup>1</sup> Free services have indexer maximum execution time of 3 minutes for blob sources and 1 minute for all other data sources. Indexer invocation is once every 180 seconds. For AI indexing that calls Foundry Tools, free services are limited to 20 free transactions per indexer per day, where a transaction is defined as a document that successfully passes through the enrichment pipeline. (Tip: You can reset an indexer to reset its count.)
 
@@ -239,12 +239,28 @@ Maximum running times exist to provide balance and stability to the service as a
 
 <sup>5</sup> Regarding the 2 or 24 hour maximum duration for indexers: a 2-hour maximum is the most common and it's what you should plan for. It refers to indexers that run in the [public environment](search-howto-run-reset-indexers.md#indexer-execution-environment), which offloads computationally intensive processing and leaves more resources for queries. The 24-hour limit applies if you configure the indexer to run in a private environment using only the infrastructure that's allocated to your search service. Some older indexers are incapable of running in the public environment, and those indexers always have a 24-hour processing range. If you have unscheduled indexers that run continuously for 24 hours, you can assume those indexers couldn't be migrated to the newer infrastructure. As a general rule, for indexing jobs that can't finish within two hours, put the indexer on a [5-minute schedule](search-howto-schedule-indexers.md) so that the indexer can quickly pick up where it left off. On the Free tier, the 3-10 minute maximum running time is for indexers with skillsets.
 
-<sup>6</sup> The maximum number of characters is based on Unicode code units, specifically UTF-16.
+### Source-file limits for blob-like indexers
 
-<sup>7</sup> When using `delimitedText` parsing mode for CSV files, a buffer size limit of 10MB per file row applies.
+File processing happens in stages, and each stage has its own limits:
 
-<sup>8</sup> When using `delimitedText` parsing mode for CSV files, the “maximum extracted content size” limit doesn't apply.
+1. A data source connector downloads a source item, subject to source-specific connector limits.
+1. Azure AI Search extracts the item's content, subject to the maximum source-file size and extracted-character limits in the following table.
+1. Optionally, a skillset sends that content to downstream services, where an individual skill's input limit can be smaller than what the indexer extracts.
 
+The maximum source-file size and extracted-character limits in the following table apply to the Azure Blob Storage, ADLS Gen2, SharePoint in Microsoft 365, OneLake, and Azure Files indexers. For per-skill limits, check the [reference article for each skill](cognitive-search-predefined-skills.md) in your skillset.
+
+| Resource | Free | Basic | S1 | S2 | S3 | S3&nbsp;HD | L1 | L2 | Serverless Developer |
+| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
+| Maximum source-file size, MB <sup>2</sup> <sup>4</sup> | 16 | 16 | 128 | 256 | 256 | N/A | 256 | 256 | 256 |
+| Maximum characters extracted from a source file <sup>1</sup> <sup>3</sup> <sup>4</sup> | 256,000 | 512,000 | 4&nbsp;mil | 8&nbsp;mil | 16&nbsp;mil | N/A | 4&nbsp;mil | 4&nbsp;mil | 16&nbsp;mil |
+
+<sup>1</sup> The maximum number of characters is based on Unicode code units, specifically UTF-16.
+
+<sup>2</sup> When using `delimitedText` parsing mode for CSV files, a buffer size limit of 10MB per file row applies.
+
+<sup>3</sup> When using `delimitedText` parsing mode for CSV files, the “maximum extracted content size” limit doesn't apply.
+
+<sup>4</sup> Blob-like indexers include the Azure Blob Storage indexer (blob indexer), ADLS Gen2 indexer, SharePoint in Microsoft 365 indexer, OneLake indexer, and Azure Files indexer. The direct-upload file knowledge source doesn't use an indexer and has [separate limits](agentic-knowledge-source-how-to-file.md#supported-formats-and-limits).
 
 ## Shared private link resource limits
 
@@ -320,9 +336,9 @@ Per-knowledge-base limits on knowledge sources depend on the API version used to
 
 ## Data limits (AI enrichment)
 
-Data limits apply to an [AI enrichment pipeline](cognitive-search-concept-intro.md) that makes calls to Azure Language in Foundry Tools for [entity recognition](cognitive-search-skill-entity-recognition-v3.md), [entity linking](cognitive-search-skill-entity-linking-v3.md), [key phrase extraction](cognitive-search-skill-keyphrases.md), [sentiment analysis](cognitive-search-skill-sentiment-v3.md), [language detection](cognitive-search-skill-language-detection.md), and [personal-information detection](cognitive-search-skill-pii-detection.md).
+Data limits apply to an [AI enrichment pipeline](cognitive-search-concept-intro.md) that calls Azure Language in Foundry Tools. The maximum input is 50,000 characters, as measured by [`String.Length`](/dotnet/api/system.string.length), for the [Entity Recognition skill](cognitive-search-skill-entity-recognition-v3.md#data-limits), [Entity Linking skill](cognitive-search-skill-entity-linking-v3.md#data-limits), [Key Phrase Extraction skill](cognitive-search-skill-keyphrases.md#data-limits), [Language Detection skill](cognitive-search-skill-language-detection.md#data-limits), and [PII Detection skill](cognitive-search-skill-pii-detection.md#data-limits). The [Sentiment skill](cognitive-search-skill-sentiment-v3.md#data-limits) has a 5,000-character maximum.
 
-The maximum size of a record is 50,000 characters as measured by [`String.Length`](/dotnet/api/system.string.length). If you need to break up your data before sending it to the sentiment analyzer, use the [Text Split skill](cognitive-search-skill-textsplit.md).
+Use the [Text Split skill](cognitive-search-skill-textsplit.md) when you need to divide larger text before downstream processing.
 
 These limits apply to both Dedicated and Serverless pricing models.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索制限とクォータに関する記事の更新"
}
```

### Explanation
この変更は、Azure AI Searchの制限およびクォータに関する記事のマイナーな更新を含んでいます。具体的には、記事の日付が2026年8月4日から2026年8月8日に更新され、AI支援に関する新しいメタデータ「doc-kit-assisted」が追加されました。また、開発者がAzure AI Searchサービスの限界、クォータ、キャパシティについて理解するための意図が明確化されています。

変更の内容には、インデクサーオブジェクトとスループットの制限に関する詳細な情報が新たにセクションとして追加され、多様なプラン（無料、基本、S1〜S3 HD）におけるリソース制限が表形式で示されています。特に、最大インデキシング負荷や最大実行時間に関する新しいガイドラインが満載で、どのレベルのサービスがどの程度のデータを処理できるのかが具体的に記載されています。

さらに、blobタイプのインデクサーに関するソースファイルの制限に関する詳細が追加され、Azure Blob StorageやADLS Gen2、SharePoint in Microsoft 365、OneLake、Azure Filesインデクサーについての制限が明示されています。これにより、ユーザーはデータソースのサイズや抽出された文字の制限を把握しやすくなり、スキルの入力制限に関する注意点も強調されています。

最後に、AI強化パイプラインに関連するデータ制限についても説明が更新されており、特にエンティティ認識や感情分析などのスキルが考慮されています。これにより、ユーザーは自分のデータ処理の計画をより効果的に行えるようになっています。全体として、この記事は有用な情報が整理され、ユーザーにとって理解しやすく改善されています。

## articles/search/search-preview-terms.md{#item-4fe0af}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,43 @@
+---
+title: Azure AI Search Preview Terms
+description: Review the supplemental preview terms that apply to features, capabilities, and properties marked (preview) in the Azure AI Search documentation.
+ms.service: azure-ai-search
+ms.topic: legal
+ms.date: 07/29/2026
+ai-usage: ai-assisted
+---
+
+# Azure AI Search preview terms
+
+[!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
+
+Azure AI Search releases some features, capabilities, and properties in preview. In the documentation, this functionality is marked (preview). Preview functionality, whether standalone or part of a generally available feature, isn't covered by a service-level agreement, isn't recommended for production workloads, and might change or be constrained before it becomes generally available.
+
+The terms in this article are based on the most recent data plane preview, the `2026-05-01-preview` [Search Service REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true). Depending on the preview version and functionality, some terms might not apply. Nevertheless, you're still responsible for complying with all applicable terms.
+
+## Licensing and preview terms
+
+Preview features and functionality are licensed to you as part of your Azure subscription and are subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+
+## Connections to other services
+
+Some preview features support connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+
+It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
+
+## Access and permissions
+
+Preview features can't modify access permissions that were set outside of Azure AI Search. If you use one of these features with access- or permission-restricted content, a timing lag will occur before Azure AI Search recognizes changes to those access or permission restrictions.
+
+## Cross-origin resource sharing (CORS)
+
+You can use some preview features to enable CORS, which allows browser-based applications to request data directly from the service. Depending on your CORS configuration, external webpages might access or invoke the service and its data by using the user's browser context, which can create security risks. Enabling CORS is at your own risk.
+
+## Responsible AI and application testing
+
+You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+
+## Related content
+
++ [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/)
++ [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Searchのプレビューモードに関する記事の追加"
}
```

### Explanation
この変更は、Azure AI Searchのプレビューモードに関する新しい記事が追加されたことを示しています。新しいページでは、プレビューモードでリリースされる機能、能力、およびプロパティに関連する補足的なプレビューベースの条件について説明しています。これらの機能は、ドキュメント内で「（プレビュー）」と表示され、サービスレベルアグリーメントには含まれず、実稼働のワークロードに対して推奨されないことが明記されています。

記事は、2026年の最新のデータプレーンプレビューに基づいており、リリースされている機能に関連するライセンス条項や、他のMicrosoftサービスおよびサードパーティサービスとの接続に関する注意点が記載されています。これにより、ユーザーはプレビューモードの使用に関連するリスクや責任を理解することができます。

特に、アクセスポリシーと権限の管理、クロスオリジンリソース共有（CORS）、および責任あるAIの実装に関する重要な注意事項が強調されています。これには、ユーザー自身がアプリケーションやデータの安全性を確保し、適切な品質基準を維持するための追加の措置が求められます。また、関連するコンテンツへのリンクも提供されており、ユーザーがより詳細な情報を得られるように配慮されています。

全体として、この新しいページは、Azure AI Searchのプレビューモードに関する理解を深め、利用者が安全かつ効果的に機能を利用できるようにサポートしています。

## articles/search/search-query-access-control-rbac-enforcement.md{#item-d24df7}

<details>
<summary>Diff</summary>
````diff
@@ -2,10 +2,11 @@
 title: Query-Time ACL and RBAC Enforcement
 description: Learn how query-time ACL and RBAC enforcement ensures secure document retrieval in Azure AI Search for indexes containing permission filters from data sources such as Azure Data Lake Storage (ADLS) Gen2 and SharePoint in Microsoft 365.
 ms.reviewer: magottei
-ms.date: 06/08/2026
+ms.date: 08/08/2026
 ms.service: azure-ai-search
 ms.topic: concept-article
 ai-usage: ai-assisted
+ms.custom: doc-kit-assisted
 ---
 
 # Query-time ACL and RBAC enforcement in Azure AI Search (preview)
@@ -59,6 +60,8 @@ This article explains how to set up queries that use permission metadata to filt
 
 - Initial ACL-based queries might experience higher latency compared to subsequent requests, due to caching and permission resolution overhead.
 
+- For indexed SharePoint content, a Microsoft Entra group nested within a SharePoint group isn't expanded. Microsoft Entra transitive group resolution doesn't support this mixed relationship. See [Supported group relationships](search-indexer-sharepoint-access-control-lists.md#supported-group-relationships).
+
 ## ACL entry limits per data source
 
 Access control list (ACL) entry limits define how many distinct permission records can be associated with a file, folder, or item within a connected data source. Each entry represents a single user or group identity and the access rights granted to that identity (for example, Read, Write, or Execute).
@@ -109,6 +112,8 @@ At query time, Azure AI Search uses the registered application and the site URL
 
 For configuration details and limitations, see [Configure SharePoint groups support](search-indexer-sharepoint-access-control-lists.md#configure-sharepoint-groups-support).
 
+If SharePoint permission filtering returns missing or unexpected results, see [Troubleshoot SharePoint permission filtering](troubleshoot-sharepoint-query-permission-filtering.md).
+
 ### Example: Query with SharePoint site group enforcement
 
 The request is identical to the standard ACL-enforced query. The search service uses the index's `sharePointConnectorAppRegistration` to resolve SharePoint group membership on the caller's behalf. Include `GroupIds` in the `select` clause to see `spg:`-prefixed values in the response.
@@ -128,7 +133,7 @@ Content-Type: application/json
 
 ## Query example
 
-Here's an example of a query request from [sample code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/acl). The query token is passed in the request header. The query token is the personal access token of a user or a group identity behind the request.
+Here's an example of a query request from [sample code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/acl). The query token is a Microsoft Entra access token for the querying user.
 
 ```http
 POST  {{endpoint}}/indexes/stateparks/docs/search?api-version=2026-05-01-preview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリ時のACLおよびRBAC強制に関する記事の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるクエリ時のアクセス制御リスト（ACL）およびロールベースのアクセス制御（RBAC）の強制に関する記事のマイナーな更新を示しています。具体的な修正内容には、記事の日付が2026年6月8日から2026年8月8日に更新されたこと、AI支援メタデータとして「doc-kit-assisted」が追加されたことが含まれています。

さらに、SharePointグループに関連する重要な注意事項が新たに追加されており、Microsoft EntraグループがSharePointグループ内でネストされている場合、その解決を行わないことが明記されています。これは、異なる関係におけるMicrosoft Entraの推移グループ解決の制限に関する情報としてユーザーに重要です。

また、SharePointの権限フィルタリングにおいて予期しない結果が生じた場合のトラブルシューティングガイドへのリンクも追加され、ユーザーが問題解決のための情報を容易に参照できるようになっています。

最後に、クエリリクエストに関する説明も微調整され、従来の記述に対して、クエリーを行うユーザーのMicrosoft Entraアクセス トークンが利用されることが明確に示されています。このようにして、記事はユーザーに対し、より正確でコンテキストに即した情報を提供することを目的としています。全体として、この更新は文書の正確性と有用性を向上させています。

## articles/search/security-controls-policy.md{#item-0e5774}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ page lists the **compliance domains** and **security controls** for Azure AI Sea
 assign the built-ins for a **security control** individually to help make your Azure resources
 compliant with the specific standard.
 
-[!INCLUDE [azure-policy-compliancecontrols-introwarning](~/azure-docs-pr-policy-includes/includes/policy/standards/intro-warning.md)]
+[!INCLUDE [azure-policy-compliancecontrols-introwarning](~/reusable-content/ce-skilling/azure/includes/policy/standards/intro-warning.md)]
 
 [!INCLUDE [azure-policy-compliancecontrols-search](~/azure-policy-autogen-docs/includes/policy/standards/byrp/microsoft.search.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セキュリティコントロールポリシーに関するリンクの修正"
}
```

### Explanation
この変更は、Azure AI Searchにおけるセキュリティコントロールポリシーに関連する記事のマイナーな更新を示しています。具体的には、含まれている警告メッセージへのリンクが変更されました。元のリンクは「azure-docs-pr-policy-includes」にありましたが、新しいリンクは「reusable-content/ce-skilling/azure/includes」に更新されています。 

この修正によって、ユーザーがより正確で新しい情報にアクセスできるようになり、コンテンツが最新の状態に保たれることを意図しています。また、全体的なコンテンツの整合性を向上させ、読者が必要とするリソースや警告情報に対して適切にアクセスできるようにする役割も果たしています。このようにして、記事はユーザーのニーズに応じた情報を提供するために改善されています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -10,6 +10,8 @@ items:
     href: whats-new.md
   - name: Features
     href: search-features-list.md
+  - name: Preview terms
+    href: search-preview-terms.md
   - name: FAQ
     href: search-faq-frequently-asked-questions.yml
   - name: Try for free
@@ -606,6 +608,8 @@ items:
         href: tutorial-adls-gen2-indexer-acls.md
       - name: Query with permission filters
         href: search-query-access-control-rbac-enforcement.md
+      - name: Troubleshoot SharePoint permission filtering
+        href: troubleshoot-sharepoint-query-permission-filtering.md
     - name: Microsoft Purview sensitivity labels (preview)
       items:
       - name: Pull sensitivity labels into an index
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次に新しい項目を追加"
}
```

### Explanation
この変更は、Azure AI Searchに関連する目次ファイル（toc.yml）のマイナーな更新を反映しています。具体的には、目次に新しいセクションやリンクが追加されました。

- "Preview terms"というセクションが新たに追加され、関連するページ「search-preview-terms.md」へのリンクが設けられています。
- "Troubleshoot SharePoint permission filtering"という項目も追加され、「troubleshoot-sharepoint-query-permission-filtering.md」へのリンクが設定されています。

これにより、ユーザーは新しい情報やトピックに迅速にアクセスできるようになり、Azure AI Searchの機能や問題解決に関するリソースがより包括的に提供されています。この更新は、情報を整理し、ナビゲーションをスムーズにすることで、全体的なユーザー体験を向上させることを目的としています。

## articles/search/troubleshoot-sharepoint-query-permission-filtering.md{#item-85cf41}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,117 @@
+---
+title: Troubleshoot SharePoint Permission Filtering
+description: Diagnose missing, unexpected, or failed query results when Azure AI Search applies permission filters to indexed SharePoint content.
+ms.reviewer: gimondra
+ms.service: azure-ai-search
+ms.topic: troubleshooting-general
+ms.date: 08/08/2026
+ai-usage: ai-assisted
+ms.custom: doc-kit-assisted
+---
+
+# Troubleshoot SharePoint permission filtering in Azure AI Search
+
+[!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
+
+Use this article if query-time permission filtering for indexed SharePoint content returns missing or unexpected results, or if a permission-filtered query fails.
+
+## Prerequisites
+
++ An index populated by the [SharePoint in Microsoft 365 indexer](search-how-to-index-sharepoint-online.md) with [ACL ingestion configured](search-indexer-sharepoint-access-control-lists.md).
++ Query-time permission filtering configured as described in [Query-time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md).
++ REST API version `2026-05-01-preview` or an equivalent preview SDK package when you use SharePoint site groups.
++ Access to the index definition, generated or explicit indexer status, and the SharePoint permissions for a test user.
++ **Search Index Data Contributor** or equivalent elevated-read permission if you need to compare filtered and unfiltered results.
+
+## Follow the troubleshooting decision tree
+
+Complete these checks in order. Stop when the observed result identifies the configuration or permission that needs correction.
+
+### 1. Confirm the failure occurs at query time
+
+This article covers permission filtering after SharePoint content and ACL metadata are indexed.
+
++ If data source creation or an indexer run reports `Invalid AAD tenant`, follow the [Microsoft Entra tenant remediation](cognitive-search-common-errors-warnings.md#error-invalid-aad-tenant).
++ If you need to correct `TenantId`, authentication, or the data source connection string, see [Configure the SharePoint in Microsoft 365 indexer](search-how-to-index-sharepoint-online.md#configure-the-sharepoint-in-microsoft-365-indexer).
++ If `UserIds`, `GroupIds`, or `SharePointSiteUrl` are missing during indexing, use the [ACL ingestion troubleshooting table](search-indexer-sharepoint-access-control-lists.md#troubleshooting).
+
+Continue here only when indexed permission metadata exists and the symptom occurs when you query it.
+
+### 2. Identify the three identities
+
+Record which identity fills each role. Don't substitute one identifier for another.
+
+| Identity | Purpose | Where to verify it |
+|---|---|---|
+| Querying user | The delegated user token in `x-ms-query-source-authorization` determines which protected documents the user can retrieve. | Your application authentication flow and the query request. |
+| SharePoint connector app registration | The `sharePointConnectorAppRegistration` on the index lets Azure AI Search resolve the querying user's SharePoint site group memberships. | The index definition and the app registration described in [Configure SharePoint groups support](search-indexer-sharepoint-access-control-lists.md#configure-sharepoint-groups-support). |
+| Azure AI Search request identity | The Microsoft Entra bearer token in the `Authorization` header, or the API key in the `api-key` header, authenticates the request to the search service. The identity must have permission to query the index. | Your query client and [Azure AI Search data plane role assignment](search-security-rbac.md#built-in-roles). |
+
+### 3. Check the permission-filter configuration
+
+Compare the index, indexer, and generated objects against their owner articles.
+
+1. Confirm the index has `permissionFilterOption` set to `enabled`.
+1. Confirm `UserIds` and `GroupIds` have the correct `permissionFilter` values.
+1. For SharePoint site groups, confirm the index has `sharePointConnectorAppRegistration` and a `SharePointSiteUrl` field with `sharepointSiteUrl: true`.
+1. Confirm every indexed document or chunk carries the applicable permission fields. If the skillset uses index projections, verify the ACL fields are in `indexProjections.mappings`.
+
+If any value is absent, return to [Configure your search service for ACL ingestion and query-time enforcement](search-indexer-sharepoint-access-control-lists.md#configure-your-search-service-for-acl-ingestion-and-query-time-enforcement).
+
+### 4. Check the query token safely
+
+Never log, paste into a support request, or share a full access token. Decode only the token payload locally, and sanitize identifiers before you capture diagnostic output.
+
+1. Confirm the request includes `x-ms-query-source-authorization` with a current delegated token for the test user.
+1. Decode the payload locally and confirm the `oid` identifies the intended test user. Record a sanitized value such as `<test-user-object-id>`.
+1. Reauthenticate the user and retry if the token is missing or expired.
+
+If the user token is omitted, permission-protected content isn't returned. The `Authorization` header alone doesn't replace `x-ms-query-source-authorization`.
+
+### 5. Check Microsoft Entra permissions
+
+1. Confirm the indexed `UserIds` or `GroupIds` contain the expected Microsoft Entra object ID. Use an [elevated-read query](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results) only for this diagnostic comparison.
+1. Confirm the test user has a direct assignment or reaches the assigned Microsoft Entra group through transitive Microsoft Entra group membership.
+1. If the Microsoft Entra group is nested within a SharePoint group, change the assignment. This mixed relationship isn't expanded and can cause missing results. Add the user directly to the SharePoint group, or grant permission through a supported Microsoft Entra group assignment.
+
+For the exact support boundary, see [Supported group relationships](search-indexer-sharepoint-access-control-lists.md#supported-group-relationships).
+
+### 6. Check SharePoint site group permissions
+
+Complete this step when the document ACL depends on an Owners, Members, Visitors, or custom SharePoint site group.
+
+1. Use an elevated-read query to confirm `GroupIds` contains the expected `spg:`-prefixed group ID and `SharePointSiteUrl` identifies the source site.
+1. Confirm the test user is a direct member of that SharePoint group.
+1. Confirm the index's `sharePointConnectorAppRegistration` uses the identifiers and permissions required by [SharePoint groups support](search-indexer-sharepoint-access-control-lists.md#configure-sharepoint-groups-support).
+
+If the indexed fields are empty or stale, fix ingestion or [synchronize the SharePoint permissions](search-indexer-sharepoint-access-control-lists.md#synchronize-permissions-between-indexed-and-source-content) before you retest the query.
+
+### 7. Check the query request
+
+1. Use REST API version `2026-05-01-preview` or an equivalent preview SDK package for SharePoint site-group permission filters.
+1. Confirm `Authorization` authenticates a principal that can query the index.
+1. Confirm `x-ms-query-source-authorization` contains the delegated test-user token.
+1. Retry the same query without unrelated filters or ranking changes so you can isolate permission behavior.
+
+Use the [general query example](search-query-access-control-rbac-enforcement.md#query-example) as the request-shape owner. Don't include full tokens in saved requests or logs.
+
+### 8. Compare expected and actual results
+
+1. Choose one document the test user can access and one document the user can't access in SharePoint.
+1. Run the permission-filtered query as the test user and record only document keys or other nonsecret identifiers.
+1. Run an elevated-read query and compare the stored `UserIds`, `GroupIds`, and `SharePointSiteUrl` values with the source permissions.
+1. If elevated read returns the expected document but the user query doesn't, focus on the user token and group resolution. If elevated read also misses it, focus on ingestion, mappings, and ACL synchronization.
+
+Elevated read is for investigation. Don't use it to return unrestricted results to end users.
+
+### 9. Capture request correlation details
+
+If the query still fails, capture the API version, UTC timestamp, sanitized request body, HTTP status, response headers, and any request or correlation ID returned by the service. Include the index name and whether the same document appears under elevated read.
+
+Remove access tokens, API keys, secrets, user names, and tenant-specific URLs before you share diagnostics with [Microsoft Support](https://azure.microsoft.com/support).
+
+## Related content
+
++ [Query-time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md)
++ [Use a SharePoint indexer to ingest permission metadata](search-indexer-sharepoint-access-control-lists.md)
++ [Configure the SharePoint in Microsoft 365 indexer](search-how-to-index-sharepoint-online.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "SharePoint権限フィルタリングのトラブルシューティングガイドの追加"
}
```

### Explanation
この変更は、Azure AI SearchにおけるSharePointの権限フィルタリングに関連する新しいドキュメント「トラブルシューティングSharePoint権限フィルタリング.md」を追加したことを示しています。このドキュメントは、Azure AI SearchがインデックスされたSharePointコンテンツに対して権限フィルタを適用した際に、欠落や予期しない結果が発生した場合や、権限フィルタが適用されたクエリが失敗した場合の診断方法を提供しています。

具体的には、次の内容が含まれています：

- 権限フィルタリングの前提条件についての説明。
- トラブルシューティングの流れを示すチェックリスト。
- 権限フィルタの設定や確認すべきアイデンティティについての詳細。
- SharePointグループの権限やクエリリクエストのチェック方法。

この新しいセクションは、ユーザーがAzure AI Searchの機能を最大限に活用し、権限関連の問題を効率的に解決できるようサポートすることを目的としています。全体として、このドキュメントはユーザーにとって便利なリソースを提供し、フィルタリングに関する問題解決の手助けをします。


