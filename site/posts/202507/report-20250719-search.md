---
date: '2025-07-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d29c020...MicrosoftDocs:1217e71
summary: この度のドキュメント更新では、Azure AI Search における役割ベースのアクセス制御（RBAC）とアクセス制御リスト（ACL）、およびインデキサーに関する情報が強化されました。特に
  ADLS Gen2 との統合において、認証と認可のプロセスが明確になり、ユーザーはより安全にこの機能を利用できるようになりました。また、セキュリティフィルターやクエリエンフォースメントの詳細も追加され、柔軟なアクセス制御が可能になっています。互換性のない変更はなく、リンクや文法の修正、C#
  アプリケーションに関する文書の明確さも向上しています。これにより、Azure AI Search の利用がさらに促進されることが期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d29c020...MicrosoftDocs:1217e71){target="_blank"}

<format>
# ハイライト
この一連のドキュメントの更新では、Azure AI Search の役割ベースのアクセス制御（RBAC）とアクセス制御リスト（ACL）、またインデキサーに関するガイドが強化されました。それに伴い、ADLS Gen2 と Azure の統合面や、セキュリティフィルター、クエリエンフォースメントに関する情報も詳細化され、ユーザーがより安心して利用できるようになっています。

## 新機能
- ADLS Gen2 との認証と認可の詳細化によって、RBAC と ACL の統合がより明確になりました。
- Azure AI Search のセキュリティフィルターとクエリエンフォースメントの方法が詳細化され、柔軟なアクセス制御が可能になりました。

## 互換性のない変更
- なし

## その他の更新
- ドキュメントのリンクや文法の修正、および最新のサービス情報の追加が行われています。
- C# アプリケーションおよびチュートリアルに関する文書の明確性が向上し、実装手順がより理解しやすくなっています。

# 洞察
Azure AI Search を取り巻くドキュメントはこの更新により、役割ベースのアクセス制御（RBAC）と ACL の詳細を改め、多くの技術的な改善と情報追加がなされています。特に ADLS Gen2 においては、Microsoft Entra ID による認証プロセスや、それに基づくアクセス設定が詳細に書かれるようになっています。この改善により、Azure AI Search の利用者は、ドキュメントレベルのセキュリティをより具体的に理解し、実装する際の支援を受けやすくなりました。

これまでのセキュリティ設定では不足していた細かい操作法や構造理解が補われ、特定の ID に基づくリソースへのアクセス許可が明確化されました。また、セキュリティフィルターの使用による結果のトリミング技法も強化され、データが守られた状態でどのようにインデクシングされ、またクエリが行われるのかがクリアになっています。

これらのようなディテールの充実によって、特に組織内での厳密なセキュリティポリシーを必要とするユーザーに対して、Azure AI Search を利用しやすくする大きな進展が期待されます。この差別化された情報は、Azure AI Search の選択肢を広げ、ユーザーのニーズにより細かく対応できるようになるでしょう。

全体的に見て、これらの改訂はドキュメントの有用性と精確性を高め、Azure AI Search が持つ強力な機能をより多くのユーザーにとって理解しやすいものとするプロセスの一環と言えるでしょう。新しいドキュメントは、情報の精度が高く、柔軟性と簡潔な仕様が備わっているため、開発者により安心感を与え、効果的なアプリケーション開発を促進します。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-blob-indexer-role-based-access.md](#item-887e42) | minor update | Blob インデクサーの RBAC スコープに関する説明の更新 | modified | 34 | 20 | 54 | 
| [search-document-level-access-overview.md](#item-4bb055) | minor update | ドキュメントレベルアクセス制御の今後の機能の更新 | modified | 16 | 7 | 23 | 
| [search-howto-run-reset-indexers.md](#item-fb10c8) | minor update | ADLS Gen2 における再インデックス処理のリンク修正 | modified | 1 | 1 | 2 | 
| [search-index-access-control-lists-and-rbac-push-api.md](#item-45e71e) | minor update | インデクサーを使用した ACL および RBAC メタデータのインデックス処理の更新 | modified | 8 | 8 | 16 | 
| [search-indexer-access-control-lists-and-role-based-access.md](#item-67b42f) | minor update | ADLS Gen2 と Azure AI Search の ACL および RBAC に関する情報更新 | modified | 18 | 21 | 39 | 
| [search-query-access-control-rbac-enforcement.md](#item-d24df7) | minor update | Azure AI Search におけるクエリ時の ACL と RBAC 機能の更新 | modified | 23 | 16 | 39 | 
| [search-security-trimming-for-azure-search.md](#item-d8ae51) | minor update | Azure AI Search におけるセキュリティフィルターに関する更新 | modified | 4 | 6 | 10 | 
| [search-what-is-azure-search.md](#item-93853a) | minor update | Azure AI Search の概要に関する更新 | modified | 49 | 32 | 81 | 
| [tutorial-adls-gen2-indexer-acls.md](#item-6881a0) | minor update | ADLS Gen2 インデクサー ACLs に関するチュートリアルの修正 | modified | 2 | 2 | 4 | 
| [tutorial-csharp-create-mvc-app.md](#item-608a5d) | minor update | C# MVC アプリケーションチュートリアルの修正 | modified | 19 | 19 | 38 | 
| [tutorial-csharp-overview.md](#item-57fa0d) | minor update | C# 検索チュートリアルの概要修正 | modified | 5 | 5 | 10 | 


# Modified Contents
## articles/search/search-blob-indexer-role-based-access.md{#item-887e42}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +1,10 @@
 ---  
 title: Use a Blob indexer to ingest RBAC scopes metadata
 titleSuffix: Azure AI Search  
-description: Learn how to configure Azure AI Search indexers for ingesting Azure Role-Based Access (RBAC) metadata on Azure Blobs.
+description: Learn how to configure Azure AI Search indexers for ingesting Azure Role-Based Access (RBAC) metadata on Azure blobs.
 ms.service: azure-ai-search  
 ms.topic: how-to
-ms.date: 07/07/2025  
+ms.date: 07/16/2025
 author: vaishalishah
 ms.author: vaishalishah
 ---  
@@ -13,35 +13,41 @@ ms.author: vaishalishah
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-Starting in 2025-05-01-preview, you can now include RBAC scope alongside document ingestion in Azure AI Search and use those permissions to control access to search results.
+Azure Storage allows for role-based access on containers in blob storage, where roles like **Storage Blob Data Reader** or **Storage Blob Data Contributor** determine whether someone has access to content. Starting in 2025-05-01-preview, you can now include RBAC scope alongside document ingestion in Azure AI Search and use those permissions to control access to search results. If you have rights to the content, you can see those results in a search query. If you don't have rights (or more specifically, a role assignment on the blob container), you *can't* see those results even if you personally have a **Search Index Data Reader** assignment on the index.
 
-You can use the push APIs to upload and index content and permission metadata manually see [Indexing Permissions using the push REST API](search-index-access-control-lists-and-rbac-push-api.md), or you can use an indexer to automate data ingestion. This article focuses on the indexer approach.
+RBAC scope is set at the container level and flows to all blobs (documents) through permission inheritance. RBAC scope is captured during indexing as permission metadata, You can use the push APIs to upload and index content and permission metadata manually see [Indexing Permissions using the push REST API](search-index-access-control-lists-and-rbac-push-api.md), or you can use an indexer to automate data ingestion. This article focuses on the indexer approach.
+
+At query time, the identity of the caller is included in the request header via the `x-ms-query-source-authorization` parameter. The identity must match the permission metadata on documents if the user is to see the search results.
 
 The indexer approach is built on this foundation:
 
 + [Role-based access control (Azure RBAC)](/azure/storage/blobs/data-lake-storage-access-control-model#role-based-access-control-azure-rbac). There's no support for Attribute-based access control (Azure ABAC).
 
-+ [An Azure AI Search indexer for Blob](search-howto-indexing-azure-blob-storage.md) that retrieves and ingests data and metadata, including permission filters. To get permission filter support, you must use the 2025-05-01-preview REST API or a prerelease package of an Azure SDK that supports the feature.
++ [An Azure AI Search indexer for blobs](search-howto-indexing-azure-blob-storage.md) that retrieves and ingests data and metadata, including permission filters. To get permission filter support, you must use the 2025-05-01-preview REST API or a preview package of an Azure SDK that supports the feature.
 
-+ [An index in Azure AI Search](search-how-to-create-search-index.md) containing the ingested documents and corresponding permissions. Permission metadata is stored as fields in the index. To set up queries that respect the permission filters, you must use the 2025-05-01-preview REST API or a prerelease package of an Azure SDK that supports the feature.
++ [An index in Azure AI Search](search-how-to-create-search-index.md) containing the ingested documents and corresponding permissions. Permission metadata is stored as fields in the index. To set up queries that respect the permission filters, you must use the 2025-05-01-preview REST API or a preview package of an Azure SDK that supports the feature. 
 
 ## Prerequisites
 
-+ [Microsoft Entra ID authentication and authorization](/entra/identity/authentication/overview-authentication). Services and apps must be in the same tenant. Role assignments are used for each authenticated connection.
++ [Microsoft Entra ID authentication and authorization](/entra/identity/authentication/overview-authentication). Services and apps must be in the same tenant. Users can be in different tenants as long as all of the tenants are Microsoft Entra ID. Role assignments are used for each authenticated connection.
 
 + Azure AI Search, any region, but you must have a billable tier (basic and higher) see [Service limits](search-limits-quotas-capacity.md) for managed identity support. The search service must be [configured for role-based access](search-security-enable-roles.md) and it must [have a managed identity (either system or user)](search-howto-managed-identities-data-sources.md).
 
-## Limitations
+## Configure Blob storage
+
+Verify your blob container uses role-based access.
+
+1. Sign in to the Azure portal and find your storage account.
 
-+ The following indexer features don't support permission preservation capabilities but are otherwise operational for Azure Blob content-only indexing:
-  + One-to-many [parsing modes](/rest/api/searchservice/indexers/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true#blobindexerparsingmode), such as: `delimitedText`, `jsonArray`, `jsonLines`, and `markdown` with sub-mode `oneToMany`
+1. Expand **containers** and select the container that has the blobs you want to index.
 
+1. Select **Access Control (IAM)** to check role assignments. Users and groups with **Storage Blob Data Reader** or **Storage Blob Data Contributor** will have access to search documents in the index after the container is indexed.
 
 ### Authorization
 
-For indexer execution, your search service identity must have **Storage Blob Data Reader** permission see [Connect to Azure Storage using a managed identity](search-howto-managed-identities-storage.md).
+For indexer execution, your search service identity must have **Storage Blob Data Reader** permission. For more information, see [Connect to Azure Storage using a managed identity](search-howto-managed-identities-storage.md).
 
-## Configure Azure AI Search for indexing permission filters
+## Configure Azure AI Search
 
 Recall that the search service must have:
 
@@ -52,14 +58,16 @@ Recall that the search service must have:
 
 For indexer execution, the client issuing the API call must have **Search Service Contributor** permission to create objects, **Search Index Data Contributor** permission to perform data import, and **Search Index Data Reader** to query an index see [Connect to Azure AI Search using roles](search-security-rbac.md).
 
-## Indexing permission metadata
+## Configure indexing
 
 In Azure AI Search, configure an indexer, data source, and index to pull permission metadata from blobs.
 
-### Configure the data source
+### Create the data source
 
 + Data Source type must be `azureblob`.
 
++ Data source parsing mode must be the default.
+
 + Data source must have `indexerPermissionOptions` with `rbacScope`.
 
   + For `rbacScope`, configure the [connection string](search-howto-index-azure-data-lake-storage.md#supported-credentials-and-connection-strings) with managed identity format.
@@ -78,8 +86,8 @@ JSON example with system managed identity:
     "connectionString": "ResourceId=/subscriptions/<your subscription ID>/resourceGroups/<your resource group name>/providers/Microsoft.Storage/storageAccounts/<your storage account name>/;"
     },
     "container": {
-        "name": "<your container name>",
-        "query": "<optional-query>"
+        "name": "<your-container-name>",
+        "query": "<optional-query-used-for-selecting-specific-blobs>"
     }
 }
 ```
@@ -95,8 +103,8 @@ JSON schema example with a user-managed identity in the connection string:
     "connectionString": "ResourceId=/subscriptions/<your subscription ID>/resourceGroups/<your resource group name>/providers/Microsoft.Storage/storageAccounts/<your storage account name>/;"
     },
     "container": {
-        "name": "<your container name>",
-        "query": "<optional-query>"
+        "name": "<your-container-name>",
+        "query": "<optional-query-used-for-selecting-specific-blobs>"
     },
     "identity": {
         "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
@@ -116,7 +124,7 @@ Recommended schema attributes RBAC Scope:
 + Use string fields for permission metadata
 + Set `filterable` to true on all fields.
 
-Notice that `retrievable` is false. You can set it true during development to verify permissions are present, but remember to set to back to false before deploying to a production environment.
+Notice that `retrievable` is false. You can set it true during development to verify permissions are present, but remember to set to back to false before deploying to a production environment so that security principal identities aren't visible in results.
 
 JSON schema example:
 
@@ -139,7 +147,7 @@ JSON schema example:
 
 ### Configure the indexer
 
-Field mappings within an indexer set the data path to fields in an index. Target and destination fields that vary by name or data type require an explicit field mapping. The following metadata fields in Azure Blob might need field mappings if you vary the field name:
+Field mappings within an indexer set the data path to fields in an index. Target and destination fields that vary by name or data type require an explicit field mapping. The following metadata fields in Azure Blob Storage might need field mappings if you vary the field name:
 
 + **metadata_rbac_scope** (`Edm.String`) - the container RBAC scope.
 
@@ -160,3 +168,9 @@ JSON schema example:
 
 To effectively manage blob deletion, ensure that you have enabled [deletion tracking](search-howto-index-changed-deleted-blobs.md) before your indexer runs for the first time. This feature allows the system to detect deleted blobs from your source and have them deleted from the index.  
 
+## Related content
+
++ [Search over Azure Blob Storage content](search-blob-storage-integration.md)
++ [Configure a blob indexer](search-howto-indexing-azure-blob-storage.md)
++ [Change and delete detection using indexers for Azure Storage](search-howto-index-changed-deleted-blobs.md)
++ [Connect to Azure AI Search using roles](search-security-rbac.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blob インデクサーの RBAC スコープに関する説明の更新"
}
```

### Explanation
この修正では、Azure AI Search における Blob インデクサーの役割ベースのアクセスポリシー（RBAC）に関する説明が更新されました。主に、RBAC スコープの設定やそれに関連したコンテナのアクセス制御の概念が強化されています。

具体的には、RBAC スコープはコンテナレベルで設定され、すべての Blob に対して権限の継承が行われることが明記されています。また、インデクサーによるドキュメントの取り込み時に、これらの権限メタデータが取得されることが強調されています。さらに、呼び出し元のユーザーの権限を確認する方法として、リクエストヘッダーに`x-ms-query-source-authorization`パラメーターを含めることが説明されています。

修正後には、インデクサーの実行に必要な権限や、Azure ポータルでの Blob コンテナの設定手順も追加されており、ユーザーが RBAC を正しく設定するためのガイダンスが強化されています。また、データソースやインデクサーの設定方法の詳細も更新され、より明確に理解できるようにされています。これにより、ユーザーは Azure AI Search のインデクサーを使用して、RBAC を活用したセキュアなデータ取り込みを実現するための情報が得やすくなります。

## articles/search/search-document-level-access-overview.md{#item-4bb055}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Conceptual overview of document-level permissions in Azure AI Search.
 author: gmndrg
 ms.author: gimondra
-ms.date: 07/03/2025
+ms.date: 07/16/2025
 ms.service: azure-ai-search
 ms.update-cycle: 90-days
 ms.topic: conceptual
@@ -21,37 +21,46 @@ Azure AI Search supports document-level access control, enabling organizations t
 | Approach | Description |
 |----------|-------------|
 | Security filters | String comparison. Your application passes in a user or group identity as a string, which populates a filter on a query, excluding any documents that don't match on the string. <br><br>Security filters are a technique for achieving document-level access control. This approach isn't bound to an API so you can use any version or package. |
-| ACLs / RBAC scopes (preview) | Microsoft Entra ID security principal behind the query token is compared to the permission metadata of documents returned in search results, excluding any documents that don't match on permissions. <br><br>Built-in support for preserving Access Control Lists (ACLs) and Azure Data Lake Storage (ADLS) Gen2 Role-Based Access Control (RBAC) container scopes at the file level for security principals is in preview, available in REST APIs and prerelease Azure SDK packages that provide the feature. |
+| ACLs / RBAC scopes (preview) | Microsoft Entra ID security principal behind the query token is compared to the permission metadata of documents returned in search results, excluding any documents that don't match on permissions. Access Control Lists (ACL) permissions apply to Azure Data Lake Storage (ADLS) Gen2 directories and files. Role-based access control (RBAC) scopes apply to ADLS Gen2 content and to Azure blobs. <br><br>Built-in support for identity-based access at the document level is in preview, available in REST APIs and prerelease Azure SDK packages that provide the feature. Be sure to check the [SDK package change log](#retrieve-permissions-metadata-during-data-ingestion-process) for evidence of feature support.|
 
 ## Pattern for security trimming using filters  
 
-For scenarios where native ACL/RBAC scopes integration isn't viable, we recommend security filters for trimming results based on exclusion criteria. The pattern includes the following components:
+For scenarios where native ACL/RBAC scopes integration isn't viable, we recommend security string filters for trimming results based on exclusion criteria. The pattern includes the following components:
 
 - Create a string field in the index to store strings of user or group identities.
 - Load the index with source documents that include a field containing the identities.
 - Include a filter expression in your query logic for matching on the string.
 - At query time, get the identity of the caller.
 - Pass in the identity of the caller as the filter string.
+- Results are trimmed to exclude any matches that fail to include the user or group identity string,
 
 You can use push or pull model APIs. Because this approach is API agnostic, you just need to ensure that the index and query have valid strings (identities) for the filtration step.
 
 This approach is useful for systems with custom access models or non-Microsoft security frameworks. For more information this approach, see [Security filters for trimming results in Azure AI Search](search-security-trimming-for-azure-search.md).
 
 ## Pattern for native support for POSIX-like ACL and RBAC scope permissions (preview)
 
-Native support is based on Microsoft Entra ID user and group access IDs affiliated with documents that you want to index and query. ADLS container RBAC scopes preservation at document level is also supported. 
+Native support is based on Microsoft Entra ID user and group access IDs affiliated with documents that you want to index and query. 
 
-For ACLs, we recommend group access IDs for ease of management. The pattern includes the following components:
+Azure Data Lake Storage (ADLS) Gen2 containers support ACLs on the container and on files. For ADLS Gen2, RBAC scope preservation at document level is natively supported when you use the [ADLS Gen2 indexer](search-howto-index-azure-data-lake-storage.md) and a preview API to ingest content. For Azure blobs using the [Azure blob indexer](search-blob-indexer-role-based-access.md), RBAC scope preservation is at the container level.
+
+For ACL-secured content, we recommend group access IDs over user access IDs for ease of management. The pattern includes the following components:
 
 - Start with documents or files that have ACL assignments.
 - [Enable permission filters](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true#searchindexpermissionfilteroption) in the index.
 - [Add a permission filter](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true#permissionfilter) to a string field in an index.
 - Load the index with source documents having associated ACLs.
 - Query the index, [adding `x-ms-query-source-authorization`](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-05-01-preview&preserve-view=true#request-headers) in the request header.
 
-You can use the push model API, pushing any JSON documents to the search index, where the payload includes a string field providing POSIX-like ACLs for each document.
+Your client app has read permissions to the index via **Search Index Data Reader**, but user or group permission metadata on indexed content determines access at query time. Queries that include a permission filter pass a user or group token as `x-ms-query-source-authorization` in the request header. When you use permission filters at query time, Azure AI Search checks for 2 things:
+
+- First, it checks for **Search Index Data Reader** permission that allows your client application to access the index.
+
+-Second, given the extra token on the request, it checks for user or group permissions on documents that are returned in search results, excluding any that don't match.
+
+To get permission metadata into the index, you can use the push model API, pushing any JSON documents to the search index, where the payload includes a string field providing POSIX-like ACLs for each document. The important difference between this approach and security trimming is that the permission filter metadata in the index and query is recognized as Microsoft Entra ID authentication, whereas the security trimming workaround is simple string comparison. Also, you can use the Graph SDK to retrieve the identities.
 
-Or, use the pull model (indexer) APIs if the data source is [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/data-lake-storage-introduction).  
+You can also use the pull model (indexer) APIs if the data source is [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/data-lake-storage-introduction) and your code calls a preview API for indexing.
   
 ### Retrieve permissions metadata during data ingestion process
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントレベルアクセス制御の今後の機能の更新"
}
```

### Explanation
この変更は、Azure AI Search におけるドキュメントレベルのアクセス制御についての説明を更新しています。主な変更点は、セキュリティフィルター、アクセス制御リスト（ACL）、および役割ベースのアクセス制御（RBAC）のスコープについての詳細な情報の追加です。

特に、Microsoft Entra ID に基づくユーザーおよびグループのアクセスIDがドキュメントのインデックス付けやクエリに関連付けられることを明確にし、ADLS Gen2 のコンテナや Blob における RBAC スコープの維持がサポートされていることが強調されています。また、セキュリティフィルターを用いたトリミング手法の推奨が更新され、より具体的なフィルター適用の仕組みや手順が説明されています。

さらに、クエリ実行時には、クライアントアプリがインデックスへのアクセス許可を持っているかどうかを確認し、追加トークンを使用してドキュメントのユーザーまたはグループ権限の検証が行われることが示されています。このように、更新された内容は、Azure AI Search のセキュリティ機能を利用した柔軟なアクセス制御の実現に役立つ情報を提供しています。

## articles/search/search-howto-run-reset-indexers.md{#item-fb10c8}

<details>
<summary>Diff</summary>
````diff
@@ -211,7 +211,7 @@ The [Indexers - Reset Docs](/rest/api/searchservice/indexers/reset-docs?view=res
 
 On a per-document basis, all fields in the search document are refreshed with values and metadata from the data source. You can't pick and choose which fields to refresh. 
 
-If the data source is Azure Data Lake Storage (ADLS) Gen2, and the blobs are associated with permission metadata, those permissions are also re-ingested in the search index if permissions change in the underlying data. For more information, see [Re-indexing ACL and RBAC scope with ADLS Gen2 indexers](search-indexer-access-control-lists-and-role-based-access.md#keep-aclrbac-metadata-in-sync-with-the-data-source).
+If the data source is Azure Data Lake Storage (ADLS) Gen2, and the blobs are associated with permission metadata, those permissions are also re-ingested in the search index if permissions change in the underlying data. For more information, see [Re-indexing ACL and RBAC scope with ADLS Gen2 indexers](search-indexer-access-control-lists-and-role-based-access.md#synchronize-permissions-between-indexed-and-source-content).
 
 If the document is enriched through a skillset and has cached data, the  skillset is invoked for just the specified documents, and the cache is updated for the reprocessed documents.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ADLS Gen2 における再インデックス処理のリンク修正"
}
```

### Explanation
この修正では、Azure Data Lake Storage (ADLS) Gen2 における再インデックス処理に関する説明のリンクが更新されました。具体的には、ADLS Gen2 のデータソースからの権限メタデータの再取り込みに関する情報へのリンクが、より正確な表現に修正されています。

元々のリンクは「ACL と RBAC スコープの再インデックス処理」と記載されていましたが、修正後は「インデックスされたコンテンツとソースコンテンツ間の権限の同期」という文言に変更されています。この変更により、ユーザーが ADLS Gen2 のインデクサーを使用して権限をどう同期するかについての情報をより明確に理解できるようになります。全体として、修正は文書の正確性と情報提供の質を向上させるものです。

## articles/search/search-index-access-control-lists-and-rbac-push-api.md{#item-45e71e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn how to use the REST API for indexing documents with ACLs and RBAC metadata.  
 ms.service: azure-ai-search  
 ms.topic: how-to 
-ms.date: 05/19/2025  
+ms.date: 07/16/2025 
 author: admayber
 ms.author: admayber  
 ---  
@@ -13,7 +13,7 @@ ms.author: admayber
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-Indexing documents, along with their associated [Access Control Lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control) and container [Role-Based Access Control (RBAC) roles](/azure/role-based-access-control/overview), into an Azure AI Search index via the [push REST APIs](/rest/api/searchservice/documents/?view=rest-searchservice-2025-05-01-preview&preserve-view=true) offers fine-grained control over the indexing pipeline. This approach enables the inclusion of document entries with precise, document-level permissions directly within the index. 
+Indexing documents, along with their associated [Access Control Lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control) and container [Role-Based Access Control (RBAC) roles](/azure/role-based-access-control/overview), into an Azure AI Search index via the [push REST APIs](/rest/api/searchservice/documents/?view=rest-searchservice-2025-05-01-preview&preserve-view=true) preserves document-level permission on indexed content at query time. 
 
 Key features include:
 
@@ -27,9 +27,9 @@ This article explains how to use the push REST API to index document-level permi
 
 - Content with ACL metadata from [Microsoft Entra ID](/entra/fundamentals/whatis) or another POSIX-style ACL system. 
 
-- Preview API version [2025-05-01-preview](/rest/api/searchservice/documents/?view=rest-searchservice-2025-05-01-preview&preserve-view=true) or a prerelease Azure SDK package providing equivalent features.
+- Preview REST API version [2025-05-01-preview](/rest/api/searchservice/documents/?view=rest-searchservice-2025-05-01-preview&preserve-view=true) or a preview Azure SDK package providing equivalent features.
 
-- An index schema with a `permissionFilterOption` defined to hold the RBAC or ACL metadata.
+- An index schema with a `permissionFilterOption` enabled, plus `permissionFilter` field attributes that store the permissions associated with the document.
 
 ## Limitations
 
@@ -39,15 +39,15 @@ This article explains how to use the push REST API to index document-level permi
 
 - A preexisting field can't be converted into a `permissionFilter` field type for use with built-in ACLs or RBAC metadata filtering. To enable filtering on an existing index, new fields must be created with the correct permission filter type.
 
-- Only one field of each `permissionFilter` type such as `groupIds`, `usersIds`, and `rbacScope`, can exist in an index.
+- Only one field of each `permissionFilter` type (one each of `groupIds`, `usersIds`, and `rbacScope`) can exist in an index.
 
 ## Create an index with permission filter fields
 
 Indexing document ACLs and RBAC metadata with the REST API requires setting up an index schema that enables permission filters and has fields with permission filter assignments.
 
 Permission filter field types can be added to an existing index on new fields. The value of `permissionFilterOption` can be set to either `enabled` or `disabled` while indexing documents. However, setting it to `disabled` turns off the permission filter functionality.
 
-Here's a basic example schema that includes both user and group ACLs and RBAC metadata:
+Here's a basic example schema that includes all `permissionFilter` types:
 
 ```json  
 {  
@@ -63,7 +63,7 @@ Here's a basic example schema that includes both user and group ACLs and RBAC me
 
 ## REST API indexing example
 
-Once you have an index with the desired permission filter fields, you can populate those values using the Indexing Push API as with any other document fields. Here's an example using the specified index schema.
+Once you have an index with the desired permission filter fields, you can populate those values using the indexing push API as with any other document fields. Here's an example using the specified index schema.
 
 ```https
 POST https://exampleservice.search.windows.net/indexes('indexdocumentsexample')/docs/search.index?api-version=2025-05-01-preview
@@ -110,7 +110,7 @@ Because a user needs to match only one field type, the special value "all" grant
 
 ### Access control example
 
-This example illustrates how the document access rules are resolved based on the specific document ACL field values. For readability, this scenario uses ACL aliases such as "user1," "group1," etc., instead of GUIDs.
+This example illustrates how the document access rules are resolved based on the specific document ACL field values. For readability, this scenario uses ACL aliases such as "user1," "group1," instead of GUIDs.
 
 | Document # | userIds | groupIds | RBAC Scope | Permitted users list | Note |
 | --- | --- | --- | --- | --- | --- |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーを使用した ACL および RBAC メタデータのインデックス処理の更新"
}
```

### Explanation
この変更は、Azure AI Search のドキュメントにおける ACL（アクセス制御リスト）および RBAC（役割ベースのアクセス制御）メタデータをインデックスする際の REST API の使い方に関する説明を更新しています。主な変更点として、ドキュメントのインデックス処理に関する文言が明確に修正され、特にドキュメントレベルの権限がクエリ時に保たれることが強調されています。

具体的には、以下のような更新が含まれています：
- 日付の更新（2025年5月19日から2025年7月16日へ）。
- ACL および RBAC メタデータのインデックス処理における機能の説明が明確化され、役割ベースのアクセス制御がインデックス内容に正確に適用される様子が強調されています。
- 記述が簡潔になり、インデクサーに使用するフィールドのタイプや制限に関する部分も改善されています。

これにより、ユーザーは ACL と RBAC メタデータを使用して、より適切にドキュメントのインデックスを操作することができるようになり、インデックスの処理に関する理解が深まることが期待されます。

## articles/search/search-indexer-access-control-lists-and-role-based-access.md{#item-67b42f}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ This article supplements [**Index data from ADLS  Gen2**](search-howto-index-azu
 
 ## Prerequisites
 
-+ Microsoft Entra ID authentication and authorization. Services and apps must be in the same tenant. Role assignments are used for each authenticated connection.
++ [Microsoft Entra ID authentication and authorization](/entra/identity/authentication/overview-authentication). Services and apps must be in the same tenant. Users can be in different tenants as long as all of the tenants are Microsoft Entra ID. Role assignments are used for each authenticated connection.
 
 + Azure AI Search, any region, but you must have a billable tier (basic and higher) for managed identity support. The search service must be [configured for role-based access](search-security-enable-roles.md) and it must [have a managed identity (either system or user)](search-howto-managed-identities-data-sources.md).
 
@@ -45,14 +45,24 @@ This article supplements [**Index data from ADLS  Gen2**](search-howto-index-azu
 
 + The `owning users`, `owning groups` and `Other` [ACL identities categories](/azure/storage/blobs/data-lake-storage-access-control#users-and-identities) are not supported during public preview. Use `named users` and `named groups` assignments instead.
   
-+ The following indexer features don't support permission preservation capabilities but are otherwise operational for ADLS Gen2 content-only indexing:
++ The following indexer features don't support permission inheritance in indexed documents originating from ADLS Gen2. If you're using any of these features in a skillset or indexer, document-level permissions won't be present in the indexed content:
 
   + [Custom Web API skill](cognitive-search-custom-skill-web-api.md)
   + [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md)
   + [Knowledge store](knowledge-store-concept-intro.md)
   + [Indexer enrichment cache](search-howto-incremental-index.md)
   + [Debug sessions](cognitive-search-debug-session.md)
-  + One-to-many [parsing modes](/rest/api/searchservice/indexers/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true#blobindexerparsingmode), such as: `delimitedText`, `jsonArray`, `jaonLines`, and `markdown` with sub-mode `oneToMany`
+
+## Support for the permission model
+
+This section compares document-level access control features between ADLS Gen2 and Azure AI Search. It highlights which ADLS Gen2 access control mechanisms are supported or mapped when integrating with AI Search, helping you understand how permissions are enforced at the document level.
+
+| ADLS Gen2 Feature | Description | Supported | Notes |
+|-|-|-|-|
+| [RBAC](/azure/storage/blobs/data-lake-storage-access-control-model#role-based-access-control-azure-rbac) | Coarse-grained access at container level | Yes | AI Search honors RBAC for access to all documents in the entire container. |
+| [ABAC](/azure/storage/blobs/data-lake-storage-access-control-model#attribute-based-access-control-azure-abac) | Attribute-based conditions on top of RBAC | No | AI Search does not evaluate ABAC conditions for document-level access. |
+| [ACL](/azure/storage/blobs/data-lake-storage-access-control-model#access-control-lists-acls) | Fine-grained permissions at directory/file (document) level  | Yes | AI Search uses document-level ACLs for [permission filters](./search-query-access-control-rbac-enforcement.md). |
+| [Security Groups](/azure/storage/blobs/data-lake-storage-access-control-model#security-groups) | Group-based permission assignments  | Yes  | Supported if security groups are mapped inside the document-level ACL. |
 
 ## About ACL hierarchical permissions
 
@@ -73,7 +83,7 @@ The indexer fetches ACLs from each container and directory, resolves them into t
       => Data.txt effective access
 ```
 
-## Configure ADLS Gen2 for indexing permission filters
+## Configure ADLS Gen2
 
 An indexer can retrieve ACLs on a storage account if the following criteria are met. For more information about ACL assignments, see [ADLS Gen2 ACL assignments](/azure/storage/blobs/data-lake-storage-access-control#how-to-set-acls).
 
@@ -111,7 +121,7 @@ Here's a diagram of the ACL assignment structure for the [fictitious directory h
 
 Over time, as any new ACL assignments are added or modified, repeat the above steps to ensure proper propagation and permissions alignment. Updated permissions in ADLS Gen2 are updated in the search index when you re-ingest the content using the indexer.
 
-## Configure Azure AI Search for indexing permission filters
+## Configure Azure AI Search
 
 Recall that the search service must have:
 
@@ -124,11 +134,11 @@ For indexer execution, the client issuing the API call must have **Search Servic
 
 If you're testing locally, you should have the same role assignments. For more information, see [Connect to Azure AI Search using roles](search-security-rbac.md).
 
-## Indexing permission metadata
+## Configure indexing
 
 In Azure AI Search, configure an indexer, data source, and index to pull permission metadata from ADLS Gen2 blobs.
 
-### Configure the data source
+### Create the data source
 
 This section supplements  [**Index data from ADLS  Gen2**](search-howto-index-azure-data-lake-storage.md) with information that's specific to ingesting permissions alongside document content into an Azure AI Search index.
 
@@ -238,8 +248,7 @@ JSON schema example:
 
 + Organize identities into groups and use groups whenever possible, rather than granting access directly to individual users. Continuously adding individual users instead of applying groups increases the number of access control entries that must be tracked and evaluated. Not following this best practice can lead to more frequent security metadata updates required to the index as this metadata changes, causing increased delays and inefficiencies in the refresh process.
 
-
-## Keep ACL/RBAC metadata in sync with the data source 
+## Synchronize permissions between indexed and source content
 
 Enabling ACL or RBAC enrichment on an indexer works automatically only in two situations: 
 
@@ -249,7 +258,6 @@ Enabling ACL or RBAC enrichment on an indexer works automatically only in two si
 
 Any permission change made after a document has already been indexed (for example, adding a user to an ACL or changing a role assignment) will not appear in the search index unless you explicitly point the indexer to crawl the document permission metadata again. 
 
-
 Choose one of the following mechanisms, depending on how many items changed: 
 
 | **Scope of your change**       | **Best trigger**                                            | **What gets refreshed on the next run**                    |  
@@ -286,18 +294,7 @@ Choose one of the following mechanisms, depending on how many items changed:
 > If you change permissions on already-indexed documents and do not trigger one of the mechanisms above, the search index will keep serving stale ACL/RBAC data.
 > New documents continue to be indexed automatically; no manual trigger is needed for them. 
 
-
 ## Deletion tracking 
 
 To effectively manage blob deletion, ensure that you have enabled [deletion tracking](search-howto-index-changed-deleted-blobs.md) before your indexer runs for the first time. This feature allows the system to detect deleted blobs from your source and have them deleted from the index.
 
-## Supported ADLS Gen2 permission features
-
-This section compares document-level access control features between ADLS Gen2 and Azure AI Search. It highlights which ADLS Gen2 access control mechanisms are supported or mapped when integrating with AI Search, helping you understand how permissions are enforced at the document level.
-
-| ADLS Gen2 Feature | Description | Supported | Notes |
-|-|-|-|-|
-| [RBAC](/azure/storage/blobs/data-lake-storage-access-control-model#role-based-access-control-azure-rbac) | Coarse-grained access at container level | Yes | AI Search honors RBAC for access to all documents in the entire container. |
-| [ABAC](/azure/storage/blobs/data-lake-storage-access-control-model#attribute-based-access-control-azure-abac) | Attribute-based conditions on top of RBAC | No | AI Search does not evaluate ABAC conditions for document-level access. |
-| [ACL](/azure/storage/blobs/data-lake-storage-access-control-model#access-control-lists-acls) | Fine-grained permissions at directory/file (document) level  | Yes | AI Search uses document-level ACLs for [permission filters](./search-query-access-control-rbac-enforcement.md). |
-| [Security Groups](/azure/storage/blobs/data-lake-storage-access-control-model#security-groups) | Group-based permission assignments  | Yes  | Supported if security groups are mapped inside the document-level ACL. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ADLS Gen2 と Azure AI Search の ACL および RBAC に関する情報更新"
}
```

### Explanation
この変更は、Azure AI Search における ADLS Gen2 の ACL（アクセス制御リスト）および RBAC（役割ベースのアクセス制御）についての情報を最新のものに更新しています。主に以下の点が改善されています：

1. **認証と認可の明確化**: Microsoft Entra ID 認証と認可に関する情報が具体的に記載され、サービスやアプリが同じテナント内にある必要性が強調されています。

2. **ACL と RBAC のサポート状況**: ADLS Gen2 の機能と Azure AI Search におけるサポート状況を比較する新しいセクションが追加され、RBAC、ABAC、ACL のそれぞれがどのようにサポートされるのかが明確に示されています。この情報により、ユーザーはドキュメントレベルでのアクセス制御がどのように機能するかを理解しやすくなります。

3. **項目のリファクタリング**: 設定方法に関するセクションが整理され、インデックス作成に必要な設定内容がより分かりやすくなりました。特に、ACL や RBAC メタデータの同期や、インデクサー実行のための条件に関する部分が強化されています。

4. **権限の同期についての具体性**: 権限変更の管理や、ドキュメントが既にインデックスされている場合に新しい権限が反映されるメカニズムについての説明が充実しており、ユーザーは適切に設定を行うことで最新の状態を保つことができるようになります。

このように、修正は文書の整合性とユーザーへの情報提供の質を向上させるものであり、Azure AI Search と ADLS Gen2を利用する際の指針となる内容へと昇華されています。

## articles/search/search-query-access-control-rbac-enforcement.md{#item-d24df7}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn how query-time ACL and RBAC enforcement ensures secure document retrieval in Azure AI Search for indexes containing permission filters from Azure Data Lake Storage (ADLS) Gen2 data sources.  
 ms.service: azure-ai-search  
 ms.topic: conceptual  
-ms.date: 05/15/2025  
+ms.date: 07/16/2025  
 author: mattgotteiner  
 ms.author: magottei 
 ---  
@@ -13,25 +13,27 @@ ms.author: magottei
 
 Query-time access control ensures that users only retrieve search results they're authorized to access, based on their identity, group memberships, roles, or attributes. This functionality is essential for secure enterprise search and compliance-driven workflows. 
 
-Azure Data Lake Storage (ADLS) Gen2 provides an access model that makes fine-grained access control easier to implement, but you can use other data sources, providing you use the push APIs and you send documents that include permission metadata alongside other indexable fields.
+Azure Data Lake Storage (ADLS) Gen2 provides an access model that makes fine-grained access control easier to implement, but you can use other data sources, providing you [use the push APIs](search-index-access-control-lists-and-rbac-push-api.md) and you send documents that include permission metadata alongside other indexable fields.
+
+This article explains how to set up queries that use permission metadata to filter results.
 
 ## Requirements
 
 - Permission metadata must be in `filterable` string fields. You won't use the filter in your queries, but the search engine builds a filter internally to exclude unauthorized content.
 
 - Permission metadata must consist of either POSIX-style permissions that identify the level of access and the group or user ID, or the resource ID of the container in ADLS Gen2 if you're using RBAC scope.
 
-- For ADLS Gen2 data sources, you must have configured Access Control Lists (ACLs) and/or Azure role-based access control (RBAC) roles at the container level. You can use a [built-in indexer](search-indexer-access-control-lists-and-role-based-access.md) or [Push APIs](search-index-access-control-lists-and-rbac-push-api.md) to index permission metadata in your index.
+- For ADLS Gen2 data sources, you must have configured Access Control Lists (ACLs) and/or Azure role-based access control (RBAC) roles at the container level. For blob data sources, your have role assignments on the container. You can use a [built-in indexer](search-indexer-access-control-lists-and-role-based-access.md) or [Push APIs](search-index-access-control-lists-and-rbac-push-api.md) to index permission metadata in your index.
 
-- Use the 2025-05-01-preview REST API or a prerelease package of an Azure SDK to query the index. This API version supports internal queries that filter out unauthorized results.
+- Use the 2025-05-01-preview REST API or a preview package of an Azure SDK to query the index. This API version supports internal queries that filter out unauthorized results.
 
 ## How query-time enforcement works
 
 This section lists the order of operations for ACL enforcement at query time. Operations vary depending on whether you use Azure RBAC scope or Microsoft Entra ID group or user IDs.
 
 ### 1. User permissions input
 
-The end-user application sends user permission as part of the search query request. The following table lists the source of the user permissions Azure AI Search uses for ACL enforcement:
+The end-user application includes a query access token as part of the search query request, and that access token is typically the identity of the user. The following table lists the source of the user permissions supported by Azure AI Search for ACL enforcement:
 
 | Permission type | Source |
 | - | - |
@@ -41,29 +43,30 @@ The end-user application sends user permission as part of the search query reque
 
 ### 2. Security filter construction
 
-Azure AI Search dynamically constructs security filters based on the user permissions provided. These security filters are automatically appended to any filters that might come in with the query if the index has the permission filter option enabled.
+Internally, Azure AI Search dynamically constructs security filters based on the user permissions provided. These security filters are automatically appended to any filters that might come in with the query if the index has the permission filter option enabled.
 
-For Azure RBAC, permissions are lists of resource ID strings. There must be an Azure role assignment (Storage Blob Data Reader) on the data the source that grants access to the security principal token in the authorization header. The filter excludes documents if there's no role assignment for the principal behind the access token on the request.
+For Azure RBAC, permissions are lists of resource ID strings. There must be an Azure role assignment (Storage Blob Data Reader) on the data source that grants access to the security principal token in the authorization header. The filter excludes documents if there's no role assignment for the principal behind the access token on the request.
 
 ### 3. Results filtering
   
-The security filter efficiently matches the userIds, groupIds, and rbacScope from the user against each list of ACLs in every document in the search index to limit the results returned to ones the user has access to. It's important to note that each filter is applied independently and a document is considered authorized if any filter succeeds. For example, if a user has access to a document through userIds but not through groupIds, the document is still considered valid and returned to the user.
+The security filter efficiently matches the userIds, groupIds, and rbacScope from the request against each list of ACLs in every document in the search index to limit the results returned to ones the user has access to. It's important to note that each filter is applied independently and a document is considered authorized if any filter succeeds. For example, if a user has access to a document through userIds but not through groupIds, the document is still considered valid and returned to the user.
 
 ## Limitations
 
-- If ACL evaluation fails (for example, Graph API is unavailable), the service returns **5xx** and does **not** return a partially filtered result set.
+- If ACL evaluation fails (for example, the Graph API is unavailable), the service returns **5xx** and does **not** return a partially filtered result set.
+
 - Document visibility requires both:
-  - the calling application’s RBAC role (Authorization header), and  
-  - the user identity carried by **x-ms-query-source-authorization**.
+  - the calling application’s RBAC role (Authorization header)  
+  - the user identity carried by **x-ms-query-source-authorization**
 
 ## Query example
 
-Here's an example of a query request from [sample code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-ACL). The query token is passed in the request header.
+Here's an example of a query request from [sample code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-ACL). The query token is passed in the request header. The query token is the personal access token of a user or a group identity behind the request.
 
 ```http
 POST  {{endpoint}}/indexes/stateparks/docs/search?api-version=2025-05-01-preview
-Authorization: Bearer {{search-token}}
-x-ms-query-source-authorization: {{search-token}}
+Authorization: Bearer {{query-token}}
+x-ms-query-source-authorization: {{query-token}}
 Content-Type: application/json
 
 {
@@ -75,6 +78,10 @@ Content-Type: application/json
 
 ## Related content
 
-- [Tutorial: Index ADLS Gen2 permission metadata](tutorial-adls-gen2-indexer-acls.md) provides a detailed walkthrough of how to set up an index with ACLs using Azure Search indexers.
+- [Tutorial: Index ADLS Gen2 permission metadata](tutorial-adls-gen2-indexer-acls.md) 
+
+- [Indexing ACLs and RBAC using the push API in Azure AI Search](search-index-access-control-lists-and-rbac-push-api.md)
+
+- [Use an ADLS Gen2 indexer to ingest permission metadata and filter search results based on user access rights](search-indexer-access-control-lists-and-role-based-access.md) 
 
-- [Indexing ACLs and RBAC using Push API in Azure AI Search](search-index-access-control-lists-and-rbac-push-api.md) provides a walkthrough of how to set up an index with ACLs using the push indexing approach with the REST APIs.
+- [Use a Blob indexer to ingest RBAC scopes metadata](search-blob-indexer-role-based-access.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search におけるクエリ時の ACL と RBAC 機能の更新"
}
```

### Explanation
この変更は、Azure AI Search におけるクエリ時の ACL（アクセス制御リスト）および RBAC（役割ベースのアクセス制御） enforcement に関するドキュメントを更新しています。主な変更点は以下の通りです：

1. **日付の更新**: ドキュメントの最終更新日が2025年5月15日から2025年7月16日に変更されました。

2. **アクセス制御メタデータの記述の明確化**: 新たに、ADLS Gen2 からのデータソースを用いた場合の権限メタデータのフォーマット要件が簡潔に記述されています。具体的には、フィルタブルな文字列フィールドであることが強調されています。

3. **クエリエンforcementの手順に関する詳細が充実**: ユーザーのアクセス権限を基にしたセキュリティフィルタの構築手順が明確化され、Azure RBACの役割割り当てに関する説明も改善されています。

4. **制限事項の明確化**: セキュリティフィルタの結果が失敗した場合の動作や、ドキュメントの可視性に必要な条件が詳細に述べられています。

5. **関連コンテンツの更新**: チュートリアルや他のドキュメントへのリンクが更新され、ユーザーがアクセス制御とインデクシングに関するリソースを簡単に見つけられるような変更が加えられています。

これにより、ユーザーはアクセス制御を効果的に実施し、クエリがどのように設計されるかをよりよく理解できるようになります。全体として、この変更はドキュメントの有用性を向上させ、Azure AI Search を利用する際の指針となる内容に一層磨きをかけるものです。

## articles/search/search-security-trimming-for-azure-search.md{#item-d8ae51}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 06/06/2025
+ms.date: 07/16/2025
 ---
 
 # Security filters for trimming results in Azure AI Search
@@ -21,18 +21,16 @@ For search solutions that can't use the [built-in access control list (ACL) supp
 This article describes a pattern for security filtering having the following steps:
 
 > [!div class="checklist"]
-> * Assemble source documents with the required content
-> * Create a field for the principal identifiers 
+> * Assemble source documents with the required content, including a string for storing an identity
+> * Create a field  in the search index for the principal identifiers 
 > * Push the documents to the search index for indexing
 > * Query the index with the `search.in` filter function
 
 It concludes with links to demos and examples that provide hands-on learning. We recommend reviewing this article first to understand the pattern.
 
 ## About the security filter pattern
 
-Although Azure AI Search doesn't integrate with security subsystems for access to content within an index, many customers who have document-level security requirements find that filters can meet their needs.
-
-In Azure AI Search, a security filter is a regular OData filter that includes or excludes a search result based on a string consisting of a security principal. There's no authentication or authorization through the security principal. The principal is just a string, used in a filter expression, to include or exclude a document from the search results.
+The security filter pattern simulates document-level authorization by using a regular OData filter that includes or excludes a search result based on a string consisting of a security principal. There's no authentication or authorization through the security principal. The principal is just a string, used in a filter expression, to include or exclude a document from the search results.
 
 There are several ways to achieve security filtering. One way is through a complicated disjunction of equality expressions: for example, `Id eq 'id1' or Id eq 'id2'`, and so forth. This approach is error-prone, difficult to maintain, and in cases where the list contains hundreds or thousands of values, slows down query response time by many seconds. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search におけるセキュリティフィルターに関する更新"
}
```

### Explanation
この変更は、Azure AI Search におけるセキュリティフィルターの使用に関するドキュメントを更新しています。変更点は以下の通りです：

1. **日付の更新**: ドキュメントの最終更新日が2025年6月6日から2025年7月16日に変更されました。

2. **セキュリティフィルターの説明の明確化**: セキュリティフィルターのパターンに関する記述が改善され、特にドキュメントレベルの権限をシミュレートする方法についての説明が強化されています。具体的には、ODataフィルターを使用して結果を含めたり除外したりする方法が詳述されています。

3. **手順の修正**: ソースドキュメントを構成する際に必要なコンテンツに「アイデンティティを格納するための文字列」を含めることが明示され、フィールドの作成に関する記述が追加されています。これにより、ユーザーがセキュリティフィルターに必要な情報をより明確に理解できるようになります。

4. **フィルターの適用手順の整理**: セキュリティフィルターを適用するための手順が整理され、推奨されるプロセスが分かりやすく示されています。

全体として、この変更はユーザーにとっての情報の明瞭性を高め、Azure AI Search を利用する際のセキュリティフィルターの実装方法をより理解しやすくすることを目的としています。ドキュメントの内容は、セキュリティ要件を満たすための実用的な指針となるでしょう。

## articles/search/search-what-is-azure-search.md{#item-93853a}

<details>
<summary>Diff</summary>
````diff
@@ -11,25 +11,35 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: overview
-ms.date: 05/15/2025
+ms.date: 07/18/2025
 ---
 
 # What's Azure AI Search?
 
-Azure AI Search ([formerly known as "Azure Cognitive Search"](whats-new.md#new-service-name)) is an enterprise-ready information retrieval system for your heterogeneous content that you ingest into a search index, and surface to users through queries and apps. It comes with a comprehensive set of advanced search technologies, built for high-performance applications at any scale.
+Azure AI Search is a scalable search infrastructure that indexes heterogeneous content and enables retrieval through APIs, applications, and AI agents. The platform provides native integrations with Azure's AI stack (OpenAI, AI Foundry, Machine Learning) and supports extensible architectures for third-party and open-source model integration.
+
+The service handles both traditional search workloads and modern RAG (retrieval-augmented generation) patterns for conversational AI applications. This makes it suitable for enterprise search scenarios as well as AI-powered customer experiences that require dynamic content generation through chat completion models.
+
+<!-- Azure AI Search is a knowledge retrieval platform that consolidates and organizes information across different types of content. You add your content to a search index. Users, agents, and bots retrieve your content through queries and apps.
+Indexing and query workloads support native integration with AI models from Azure OpenAI, Azure AI Foundry, and Azure Machine Learning. By leveraging an extensibility layer, you can connect workloads to third-party and open-source AI models and tools.
+
+You can use Azure AI Search for regular search needs (like searching through catalogs or documents) or for AI-powered search that can have conversations with users and generate answers based on your content. -->
+
+<!-- Azure AI Search ([formerly known as "Azure Cognitive Search"](whats-new.md#new-service-name)) is an enterprise-ready information retrieval system for your heterogeneous content that you ingest into a search index, and surface to users through queries and apps. It comes with a comprehensive set of advanced search technologies, built for high-performance applications at any scale.
 
 Azure AI Search is the recommended retrieval system for building agent-to-agent (A2A) and RAG-based applications on Azure, with native LLM integrations between Azure OpenAI in Azure AI Foundry Models and Azure Machine Learning, with mechanisms for integrating third-party and open-source models and processes.
 
-Azure AI Search can be used in both traditional and generative search scenarios. Common use cases include catalog or document search, information discovery (data exploration), and  retrieval-augmented generation (RAG) for conversational search.  
+Azure AI Search can be used for both traditional search as well as modern information retrieval. Common use cases include catalog or document search, information discovery (data exploration), and  retrieval-augmented generation (RAG) for conversational search.  
+ -->
 
 When you create a search service, you work with the following capabilities:
 
-+ A search engine for [vector search](vector-search-overview.md) and [full text](search-lucene-query-architecture.md) and [hybrid search](hybrid-search-overview.md) over a search index.
-+ Rich indexing with the ability to content transformation. This includes [integrated data chunking and vectorization](vector-search-integrated-vectorization.md) for RAG, [lexical analysis](search-analyzers.md) for text, and [optional applied AI](cognitive-search-concept-intro.md) for content extraction and enrichment.
-+ Rich query syntax for [vector queries](vector-search-how-to-query.md), text search, [hybrid queries](hybrid-search-how-to-query.md), fuzzy search, autocomplete, geo-search and others.
-+ Relevance and query performance tuning with [semantic ranking](semantic-search-overview.md), [scoring profiles](index-add-scoring-profiles.md), [quantization for vector queries](vector-search-how-to-quantization.md), and parameters for controlling query behaviors at runtime.
++ A search engine for [agentic search](search-agentic-retrieval-concept.md), [vector search](vector-search-overview.md), [full text](search-lucene-query-architecture.md), [multimodal search](multimodal-search-overview.md), or [hybrid search](hybrid-search-overview.md).
++ Content processing during indexing that can add structure and transformations.
++ Extensive query syntax for agents, vectors, text, hybrid, and multimodal queries.
++ Smart results through semantic ranking, scoring profiles, and parameterized queries.
 + Azure scale, security, and reach.
-+ Azure integration at the data layer, machine learning layer, Azure AI services and Azure OpenAI.
++ Azure integration at the data layer, machine learning layer, Azure AI services, and Azure OpenAI.
 
 > [!div class="nextstepaction"]
 > [Create a search service](search-create-service-portal.md)
@@ -38,45 +48,41 @@ Architecturally, a search service sits between the external data stores that con
 
 ![Azure AI Search architecture](media/search-what-is-azure-search/azure-search.svg "Azure AI Search architecture")
 
-In your client app, the search experience is defined using APIs from Azure AI Search, and can include relevance tuning, semantic ranking, autocomplete, synonym matching, fuzzy matching, pattern matching, filter, and sort.
+On the indexing side, if your content is on Azure, you can used indexers and skillsets for automated and AI-enriched indexing. Or, create a logic app workflow for equivalent automation over an even broader set of supported data sources. 
+
+On the retrieval side, your app can be an agent or tool, a bot, or any client that sends requests to a search index or knowledge agent.
 
-Across the Azure platform, Azure AI Search can integrate with other Azure services in the form of *indexers* that automate data ingestion/retrieval from Azure data sources, and *skillsets* that incorporate consumable AI from Azure AI services, such as image and natural language processing, or custom AI that you create in Azure Machine Learning or wrap inside Azure Functions.
+Within Azure AI Search, the indexing and query engine is the same component operating in read-write and read-only modes, but we split it up in this diagram to indicate the type of work being performed.
 
 ## Inside a search service
 
 On the search service itself, the two primary workloads are *indexing* and *querying*. 
 
-+ [**Indexing**](search-what-is-an-index.md) is an intake process that loads content into your search service and makes it searchable. Internally, inbound text is processed into tokens and stored in inverted indexes, and inbound vectors are stored in vector indexes. The document format that Azure AI Search can index is JSON. You can upload JSON documents that you've assembled, or use an indexer to retrieve and serialize your data into JSON. 
++ [**Indexing**](search-what-is-an-index.md) is an intake process that loads content into your search service and makes it searchable. Internally, inbound text is processed into tokens and stored in inverted indexes, and inbound vectors are stored in vector indexes. The document format that Azure AI Search can index is JSON. You can upload JSON documents, or use an indexer or a logic app workflow to retrieve and serialize your data into JSON. 
 
-  [Applied AI](cognitive-search-concept-intro.md) through a [skillset](cognitive-search-working-with-skillsets.md) extends indexing with image and language models. If you have images or large unstructured text in source document, you can attach skills that perform OCR, analyze and describe images, infer structure, translate text, and more. Output is text that can be serialized into JSON and ingested into a search index.
+  [AI enrichment](cognitive-search-concept-intro.md) is through a [skillset](cognitive-search-working-with-skillsets.md) that extends indexing with image and language models. If you have images or large unstructured text in source document, you can attach skills that chunk and vectorize content. If you have image content, you can use LLMs to summarize content, generate descriptions, or perform OCR and image analysis. Skills can also infer structure, translate text, and more. Output is text or vectors that can be serialized into JSON and ingested into a search index.
 
-  Skillsets can also perform [data chunking and vectorization during indexing](vector-search-integrated-vectorization.md). Skills that attach to Azure OpenAI, the model catalog in [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs), or custom skills that attach to any external chunking and embedding model can be used during indexing to create vector data. Output is chunked vector content that can be ingested into a search index.
-
-+ [**Querying**](search-query-overview.md) can happen once an index is populated with searchable content, when your client app sends query requests to a search service and handles responses. All query execution is over a search index that you control.
-
-  [Semantic ranking](semantic-search-overview.md) is an extension of query execution. It adds secondary ranking, using language understanding to reevaluate a result set, promoting the most semantically relevant results to the top.
-
-  [Integrated vectorization](vector-search-integrated-vectorization.md) is also an extension of query execution. If you have vector fields in your search index, you can submit raw vector queries or text that's vectorized at query time.
++ [**Querying**](search-query-overview.md) can happen once an index is populated with searchable content, when your client app sends query requests to a search service and handles responses. All query execution is over a search index that you control. In your code, set up a search client to handle query requests for [agentic queries](search-agentic-retrieval-how-to-retrieve.md), [vector queries](vector-search-how-to-query.md), [text search](search-query-create.md), [hybrid queries](hybrid-search-how-to-query.md), fuzzy search, autocomplete, geo-search, and others.
 
 ## Why use Azure AI Search?
 
-Azure AI Search is well suited for the following application scenarios:
+Azure AI Search offloads indexing and query workloads onto a dedicated search service. It's well suited for the following application scenarios:
+
++ Use it for empowering agents and bots with grounding data based on your content.
 
 + Use it for traditional full text search and next-generation vector similarity search. Back your generative AI apps with information retrieval that leverages the strengths of both keyword and similarity search. Use both modalities to retrieve the most relevant results.
 
 + Consolidate heterogeneous content into a user-defined and populated search index composed of vectors and text. You maintain ownership and control over what's searchable.
 
-+ [Integrate data chunking and vectorization](vector-search-integrated-vectorization.md) for generative AI and RAG apps.
++ Transform large undifferentiated text or image files, or application files stored in Azure Blob Storage or Azure Cosmos DB, into searchable chunks. This is achieved during indexing through [AI skills](cognitive-search-concept-intro.md) that add external processing from Azure AI.
 
-+ [Apply granular access control](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/access-control-in-generative-ai-applications-with-azure/ba-p/3956408) at the document level.
++ [Integrate data chunking and vectorization](vector-search-integrated-vectorization.md) for generative AI and RAG apps.
 
-+ Offload indexing and query workloads onto a dedicated search service.
++ Add linguistic or custom text analysis for keyword search. If you have non-English content, Azure AI Search supports both Lucene analyzers and Microsoft's natural language processors. You can also configure analyzers to achieve specialized processing of raw content, such as filtering out diacritics, or recognizing and preserving patterns in strings.
 
 + Easily implement search-related features: relevance tuning, faceted navigation, filters (including geo-spatial search), synonym mapping, and autocomplete.
 
-+ Transform large undifferentiated text or image files, or application files stored in Azure Blob Storage or Azure Cosmos DB, into searchable chunks. This is achieved during indexing through [AI skills](cognitive-search-concept-intro.md) that add external processing from Azure AI.
-
-+ Add linguistic or custom text analysis. If you have non-English content, Azure AI Search supports both Lucene analyzers and Microsoft's natural language processors. You can also configure analyzers to achieve specialized processing of raw content, such as filtering out diacritics, or recognizing and preserving patterns in strings.
++ [Apply granular access control](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/access-control-in-generative-ai-applications-with-azure/ba-p/3956408) at the document level.
 
 For more information about specific functionality, see [Features of Azure AI Search](search-features-list.md)
 
@@ -88,14 +94,25 @@ Functionality is exposed through the Azure portal, simple [REST APIs](/rest/api/
 
 An end-to-end exploration of core search features can be accomplished in four steps:
 
-1. [**Decide on a tier**](search-sku-tier.md) and region. One free search service is allowed per subscription. All quickstarts can be completed on the free tier. For more capacity and capabilities, you'll need a [billable tier](https://azure.microsoft.com/pricing/details/search/).
+1. [**Decide on a tier**](search-sku-tier.md) and region. One free search service is allowed per subscription. Most quickstarts can be completed on the free tier. For more capacity and capabilities, you need a [billable tier](https://azure.microsoft.com/pricing/details/search/).
 
 1. [**Create a search service**](search-create-service-portal.md) in the Azure portal.
 
 1. [**Start with Import data wizard**](search-get-started-portal.md). Choose a built-in sample or a supported data source to create, load, and query an index in minutes. 
 
 1. [**Finish with Search Explorer**](search-explorer.md), using a portal client to query the search index you just created.
 
+### Check out samples
+
+We maintain an inventory of samples that use the REST APIs and the Azure SDK programming languages supported by Azure AI Search:
+
++ [REST samples](/azure/search/samples-rest)
++ [Python samples](/azure/search/samples-python)
++ [C# samples](/azure/search/samples-dotnet)
++ [Java samples](/azure/search/samples-java)
++ [JavaScript/TypeScript samples](/azure/search/samples-javascript)
++ [Vector samples](https://github.com/Azure/azure-search-vector-samples)
+
 ### Use APIs
 
 Alternatively, you can create, load, and query a search index in atomic steps:
@@ -110,20 +127,20 @@ Alternatively, you can create, load, and query a search index in atomic steps:
 
 Or, try solution accelerators:
 
-+ [**Chat with your data** solution accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator) helps you create a custom RAG solution over your content.
++ [**Chat with your data solution accelerator**](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator) helps you create a custom RAG solution over your content.
 
-+ [**Conversational Knowledge Mining** solution accelerator](https://github.com/microsoft/Customer-Service-Conversational-Insights-with-Azure-OpenAI-Services) helps you create an interactive solution to extract actionable insights from post-contact center transcripts.
++ [**Conversational Knowledge Mining solution accelerator**](https://github.com/microsoft/Customer-Service-Conversational-Insights-with-Azure-OpenAI-Services) helps you create an interactive solution to extract actionable insights from post-contact center transcripts.
 
 + [**Document Knowledge Mining accelerator**](https://github.com/microsoft/Document-Knowledge-Mining-Solution-Accelerator) helps you process and extract summaries, entities, and metadata from unstructured, multimodal documents.
 
-+ [**Build your own copilot** solution accelerator](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator), leverages Azure OpenAI, Azure AI Search and Microsoft Fabric, to create custom copilot solutions.
++ [**Build your own copilot solution accelerator**](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator), leverages Azure OpenAI, Azure AI Search and Microsoft Fabric, to create custom copilot solutions.
 
-  + [Generic copilot](https://github.com/microsoft/Generic-Build-your-own-copilot-Solution-Accelerator) helps you build your own copilot to identify relevant documents, summarize unstructured information, and generate Word document templates using your own data.
+<!--   + [Generic copilot](https://github.com/microsoft/Generic-Build-your-own-copilot-Solution-Accelerator) helps you build your own copilot to identify relevant documents, summarize unstructured information, and generate Word document templates using your own data.
 
   + [Client Advisor](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator) all-in-one custom copilot empowers Client Advisor to harness the power of generative AI across both structured and unstructured data. Help our customers to optimize daily tasks and foster better interactions with more clients
 
   + [Research Assistant](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator) helps build your own AI Assistant to identify relevant documents, summarize and categorize vast amounts of unstructured information, and accelerate the overall document review and content generation.
-
+ -->
 > [!TIP]
 > For help with complex or custom solutions, [**contact a partner**](https://partner.microsoft.com/partnership/find-a-partner) with deep expertise in Azure AI Search technology.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search の概要に関する更新"
}
```

### Explanation
この変更は、Azure AI Search に関する概要ドキュメントを更新し、サービスの機能と特長を明確にしています。主な変更点は以下の通りです：

1. **日付の更新**: ドキュメントの最終更新日が2025年5月15日から2025年7月18日に変更されました。

2. **サービスの説明の更新**: Azure AI Search の説明が更新され、スケーラブルな検索インフラストラクチャとして、異種コンテンツをインデックスし、APIやアプリケーション、AIエージェントを通じて情報を取得する機能が強調されています。特に、Azure の AI スタックとの統合が説明されています。

3. **新しい使用ケースの強調**: モダンな情報検索パターンである RAG（情報取得拡張生成）の適用が追加され、特に対話型 AI アプリケーションに対しての適用が説明されています。

4. **インデクシングおよびクエリ機能の詳細**: インデクシングプロセスやクエリの実行に関する詳細が述べられ、AI による強化処理やデータチャンク化についての説明も充実しています。

5. **機能の強化**: 詳細なクエリ構文、スマートな結果、拡張性のあるアーキテクチャなどの機能が追加され、より多様な検索ニーズに対応するための情報が提供されています。

6. **サンプルとソリューションアクセラレーターの追加**: REST API や SDK を使用したサンプルが明記され、ユーザーが実際にどのように Azure AI Search を活用できるかに関する情報が増強されています。

これにより、Azure AI Search の機能と適用範囲がより明確になり、利用者にとって有用な参考資料となることを目指しています。全体として、この変更はユーザーが Azure AI Search の利点を理解し、実際のアプリケーションに活用する手助けをすることを意図しています。

## articles/search/tutorial-adls-gen2-indexer-acls.md{#item-6881a0}

<details>
<summary>Diff</summary>
````diff
@@ -131,7 +131,7 @@ For demo purposes, the permission field has `retrievable` enabled so that you ca
 
 ## Create a data source
 
-Modify [data source configuration](search-indexer-access-control-lists-and-role-based-access.md#configure-the-data-source) to specify indexer permission ingestion and the types of permission metadata that you want to index.
+Modify [data source configuration](search-indexer-access-control-lists-and-role-based-access.md#create-the-data-source) to specify indexer permission ingestion and the types of permission metadata that you want to index.
 
 A data source needs `indexerPermissionOptions`.
 
@@ -154,7 +154,7 @@ In this tutorial, use a system-assigned managed identity for the authenticated c
 
 ## Create and run the indexer
 
-Indexer configuration for permission ingestion is primarily about defining `fieldMappings` from [permission metadata](search-indexer-access-control-lists-and-role-based-access.md#indexing-permission-metadata).
+Indexer configuration for permission ingestion is primarily about defining `fieldMappings` from [permission metadata](search-indexer-access-control-lists-and-role-based-access.md#).
 
 ```json
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ADLS Gen2 インデクサー ACLs に関するチュートリアルの修正"
}
```

### Explanation
この変更は、ADLS Gen2 インデクサーのアクセス制御リスト（ACL）に関するチュートリアルドキュメントの内容を小幅に修正しています。具体的な変更点は以下の通りです：

1. **リンクの修正**: 「データソースの構成」に関するリンク先が更新され、「#configure-the-data-source」から「#create-the-data-source」に変更されました。これにより、データソース構成に関する正確な情報へのナビゲーションが確保されています。

2. **メタデータのリンクの簡略化**: インデクサーの権限取り込みに関する設定の説明で、権限メタデータに関連するリンクが「#indexing-permission-metadata」から「#」に簡略化されています。これにより、リンク先がシンプルになり、適切な参照が維持されるよう配慮されています。

全体として、この修正はドキュメントのリンクの正確性を向上させ、利用者がADLS Gen2のインデクサーを正確に理解できるようにすることを目的としています。これにより、チュートリアルがより使いやすく、情報のナビゲーションがしやすくなることが期待されます。

## articles/search/tutorial-csharp-create-mvc-app.md{#item-608a5d}

<details>
<summary>Diff</summary>
````diff
@@ -17,16 +17,16 @@ ms.date: 07/10/2025
 
 # Create a search app in ASP.NET Core
 
-In this tutorial, create a basic ASP.NET Core (Model-View-Controller) app that runs in localhost and connects to the hotels-sample-index on your search service. In this tutorial, learn how to:
+In this tutorial, you create a basic ASP.NET Core (Model-View-Controller) app that runs in localhost and connects to the hotels-sample-index on your search service. You learn how to:
 
 > [!div class="checklist"]
 > + Create a basic search page
 > + Filter results
 > + Sort results
 
-This tutorial puts the focus on server-side operations called through the [Search APIs](/dotnet/api/overview/azure/search.documents-readme). Although it's common to sort and filter in client-side script, knowing how to invoke these operations on the server gives you more options when designing the search experience.
+This tutorial focuses on server-side operations called through the [Search APIs](/dotnet/api/overview/azure/search.documents-readme). Although it's common to sort and filter in client-side script, knowing how to invoke these operations on the server gives you more options when designing the search experience.
 
-Sample code for this tutorial can be found in the [azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/create-mvc-app) repository on GitHub. 
+You can find sample code for this tutorial in the [azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/create-mvc-app) repository on GitHub. 
 
 ## Prerequisites
 
@@ -43,21 +43,21 @@ Sample code for this tutorial can be found in the [azure-search-dotnet-samples](
 
 1. Select **ASP.NET Core Web App (Model-View-Controller)**, and then select **Next**.
 
-1. Provide a project name, and then select **Next**.
+1. Enter a project name, and then select **Next**.
 
 1. On the next page, select **.NET 9.0**.
 
-1. Accept the defaults.
+1. Accept the default settings.
 
 1. Select **Create**.
 
 ### Add NuGet packages
 
-1. On Tools, select **NuGet Package Manager** > **Manage NuGet Packages for the solution**.
+1. On the **Tools** menu, select **NuGet Package Manager** > **Manage NuGet Packages for the solution**.
 
 1. Browse for `Azure.Search.Documents` and install the latest stable version.
 
-1. Browse for and install the `Microsoft.Spatial` package. The sample index includes a GeographyPoint data type. Installing this package avoids run time errors. Alternatively, remove the "Location" field from the Hotels class if you don't want to install the package. That field isn't used in this tutorial.
+1. Browse for and install the `Microsoft.Spatial` package. The sample index includes a `GeographyPoint` data type. Installing this package avoids run time errors. Alternatively, remove the "Location" field from the `Hotels` class if you don't want to install the package. That field isn't used in this tutorial.
 
 ### Add service information
 
@@ -74,13 +74,13 @@ Modify `appsettings.json` to specify your search service and [query API key](sea
 
 You can get the service URL and API key from the Azure portal. Because this code is querying an index and not creating one, you can use a query key instead of an admin key.
 
-Make sure to specify a search service that has the hotels-sample-index.
+Make sure to specify a search service that has the `hotels-sample-index`.
 
 ## Add models
 
-In this step, create models that represent the schema of the hotels-sample-index.
+In this step, you create models that represent the schema of the hotels-sample-index.
 
-1. In Solution explorer, right-select **Models** and add a new class named "Hotel" for the following code:
+1. In Solution Explorer, right-select **Models** and add a new class named "Hotel" for the following code:
 
    ```csharp
     using Azure.Search.Documents.Indexes.Models;
@@ -218,9 +218,9 @@ In this step, create models that represent the schema of the hotels-sample-index
 
 For this tutorial, modify the default `HomeController` to contain methods that execute on your search service.
 
-1. In Solution explorer under **Models**, open `HomeController`.
+1. In Solution Explorer under **Models**, open `HomeController`.
 
-1. Replace the default with the following content:
+1. Replace the default content with the following code:
 
    ```csharp
    using Azure;
@@ -322,9 +322,9 @@ For this tutorial, modify the default `HomeController` to contain methods that e
 
 ## Modify the view
 
-1. In Solution explorer under **Views** > **Home**, open `index.cshtml`.
+1. In Solution explorer, under **Views** > **Home**, open `index.cshtml`.
 
-1. Replace the default with the following content:
+1. Replace the default content with the following code:
 
     ```razor
     @model HotelDemoApp.Models.SearchData;
@@ -393,7 +393,7 @@ For this tutorial, modify the default `HomeController` to contain methods that e
 
 ## Run the sample
 
-1. Press **F5** to compile and run the project. The app runs on local host and opens in your default browser.
+1. Press **F5** to compile and run the project. The app runs on localhost and opens in your default browser.
 
 1. Select **Search** to return all results.
 
@@ -405,7 +405,7 @@ In the next several sections, modify the **RunQueryAsync** method in the `HomeCo
 
 Index field attributes determine which fields are searchable, filterable, sortable, facetable, and retrievable. In the hotels-sample-index, filterable fields include Category, Address/City, and Address/StateProvince. This example adds a [$Filter](search-query-odata-filter.md) expression on Category.
 
-A filter always executes first, followed by a query assuming one is specified.
+A filter always executes first, followed by a query, assuming you specify one.
 
 1. Open the `HomeController` and find the **RunQueryAsync** method. Add [Filter](/dotnet/api/azure.search.documents.searchoptions.filter) to `var options = new SearchOptions()`:
 
@@ -444,7 +444,7 @@ For more information about filter expressions, see [Filters in Azure AI Search](
 
 In the hotels-sample-index, sortable fields include Rating and LastRenovated. This example adds an [$OrderBy](/dotnet/api/azure.search.documents.searchoptions.orderby) expression to the Rating field.
 
-1. Open the `HomeController` and replace **RunQueryAsync** method with the following version:
+1. Open the `HomeController` and replace the **RunQueryAsync** method with the following version:
 
    ```csharp
     private async Task<ActionResult> RunQueryAsync(SearchData model)
@@ -478,6 +478,6 @@ For more information about sorting, see [OData $orderby syntax in Azure AI Searc
 
 ## Next step
 
-In this tutorial, you created an ASP.NET Core (MVC) project that connected to a search service and called Search APIs for server-side filtering and sorting.
+In this tutorial, you created an ASP.NET Core (MVC) project that connects to a search service and calls Search APIs for server-side filtering and sorting.
 
-To add client-side code that responds to user actions, use a React template in your solution: [C# Tutorial: Add search to a website with .NET](tutorial-csharp-overview.md)
+To add client-side code that responds to user actions, use a React template in your solution: [C# Tutorial: Add search to a website with .NET](tutorial-csharp-overview.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# MVC アプリケーションチュートリアルの修正"
}
```

### Explanation
この変更は、C# を使用した ASP.NET Core MVC アプリケーションの作成に関するチュートリアルドキュメントの内容を更新しています。主な修正点は以下の通りです：

1. **文体の改善**: 文章をより明確かつ一貫性のある文体に修正しました。具体的には、「このチュートリアルでは、あなたが基本的な ASP.NET Core アプリを作成する方法を学びます」といった形式に変えられ、内容がより親しみやすくなっています。

2. **手順の表現変更**: 手順の説明において、「提供する」から「入力する」など、用語の改善がなされています。これにより、ユーザーが手順をより理解しやすくなります。

3. **セクション見出しの明確化**: 特にプログラミングの手順に関する節の表現を改善し、より分かりやすい表現にされています。

4. **コードサンプルに関連する説明の更新**: コードサンプルに関する説明が改善され、参照が適切に強調されています。特に、`GeographyPoint` データ型およびフィールドについての説明が明確化されています。

5. **ローカルホストの表現の統一**: 「localhost」という用語の表現を統一し、誤解を避けるために正確な表記に揃えました。

全体として、この変更は文書の明確性と一貫性を向上させ、読者がチュートリアルの内容をより理解しやすくなることを目的としています。また、具体的な手順や注意点についての表現を改善することで、実際にアプリケーションを構築する際の参考しやすさが向上しています。

## articles/search/tutorial-csharp-overview.md{#item-57fa0d}

<details>
<summary>Diff</summary>
````diff
@@ -18,11 +18,11 @@ ms.devlang: csharp
 
 # Step 1 - Overview of adding search to a static web app with .NET
 
-This tutorial builds a website to search through a catalog of books and then deploys the website to an Azure static web app. 
+This tutorial builds a website that searches through a catalog of books and then deploys the website to an Azure Static Web App. 
 
 ## What does the sample do?
 
-This sample website provides access to a catalog of 10,000 books. You can search the catalog by entering text in the search bar. While you enter text, the website uses the search index's suggestion feature to autocomplete the text. Once the query finishes, the list of books is displayed with a portion of the details. You can select a book to see all the details, stored in the search index, of the book. 
+This sample website provides access to a catalog of 10,000 books. You can search the catalog by entering text in the search bar. While you enter text, the website uses the search index's suggestion feature to autocomplete the text. When the query finishes, the website displays the list of books with a portion of the details. You can select a book to see all the details, stored in the search index, of the book. 
 
 :::image type="content" source="media/tutorial-csharp-overview/cognitive-search-enabled-book-website-2.png" alt-text="Screenshot of the sample app in a browser window.":::
 
@@ -55,11 +55,11 @@ Create services and install the following software for your local development en
 - [C# Dev Tools extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)
 - [Azure Static Web App extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurestaticwebapps) 
 
-This tutorial doesn't run the Azure Function API locally but if you intend to run it locally, install [azure-functions-core-tools](/azure/azure-functions/functions-run-local?tabs=linux%2ccsharp%2cbash#install-the-azure-functions-core-tools).
+This tutorial doesn't run the Azure Function API locally. If you want to run it locally, install [azure-functions-core-tools](/azure/azure-functions/functions-run-local?tabs=linux%2ccsharp%2cbash#install-the-azure-functions-core-tools).
 
 ## Fork and clone the search sample with git
 
-Forking the sample repository is critical to be able to deploy the Static Web App. The web apps determine the build actions and deployment content based on your own GitHub fork location. Code execution in the Static Web App is remote, with Azure Static Web Apps reading from the code in your forked sample.
+To deploy the Static Web App, you need to fork the sample repository. The web apps use your GitHub fork location to decide the build actions and deployment content. Code execution in the Static Web App happens remotely, with Azure Static Web Apps reading the code from your forked sample.
 
 1. On GitHub, fork the [azure-search-static-web-app repository](https://github.com/Azure-Samples/azure-search-static-web-app). 
 
@@ -79,7 +79,7 @@ Forking the sample repository is critical to be able to deploy the Static Web Ap
     cd azure-search-static-web-app
     ```
 
-1. Use the Visual Studio Code command, `code .` to open your forked repository. The remaining tasks are accomplished from Visual Studio Code, unless specified.
+1. Use the Visual Studio Code command, `code .` to open your forked repository. You accomplish the remaining tasks from Visual Studio Code, unless specified.
 
     ```bash
     code .
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# 検索チュートリアルの概要修正"
}
```

### Explanation
この変更は、C# を使用した静的 Web アプリに検索機能を追加するチュートリアルの概要部分に関する文言を修正しています。主な修正点は以下の通りです：

1. **文法の改善**: 「this tutorial builds a website to search through a catalog of books」という表現が「this tutorial builds a website that searches through a catalog of books」に修正され、文法的により正確な表現となりました。

2. **言葉の統一**: 「Azure static web app」という表現が「Azure Static Web App」に修正され、正式名称が一貫して使用されています。

3. **能動的な文体の適用**: 「you can select a book to see all the details, stored in the search index, of the book」という文の文体が、「you can select a book to see all the details, stored in the search index, of the book」に微調整され、読みやすさが向上しています。

4. **手順の明確化**: いくつかの手順が明確化されています。「このチュートリアルでは Azure Function API をローカルで実行しませんが、ローカルで実行する場合は…」という部分が改訂され、言い回しが簡素化されています。

5. **フォークの重要性の強調**: リポジトリをフォークする必要性の説明が明確になり、「This tutorial doesn’t run the Azure Function API locally but if you intend to run it locally, install...」という部分が改善されています。

全体として、この変更は文書の明確性と流暢さを向上させるものであり、チュートリアルを読むユーザーが手順をより容易に理解できるように工夫されています。この更新により、静的 Web アプリに検索機能を追加する際の理解が深まることが期待されます。


