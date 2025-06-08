---
date: '2025-06-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b06c631...MicrosoftDocs:0565698
summary: この変更は、Azure AI Searchに関する複数の記事で加えられたもので、主に構造の整理と内容の明確化に焦点を当てています。主なアップデートには、ドキュメントレベルのアクセス制御やセキュリティフィルタリングに関する理解を容易にする詳細なテーブルの追加、ACLやRBACのインデックスガイドの更新が含まれます。破壊的な変更はなく、目次ファイルの更新や記事の日付の更新も行われました。これにより、ユーザーは検索ソリューションの安全性を高めるための情報をより効果的に活用できるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b06c631...MicrosoftDocs:0565698){target="_blank"}

<format>
# ハイライト
この変更は、Azure AI Searchに関する複数の記事で加えられたもので、主に構造の整理と内容の明確化に焦点を当てています。ドキュメントレベルのアクセス制御とセキュリティフィルタリングおよびインデックス作成のためのACLやRBACのガイドの更新が中心です。

## 新機能
- 詳細なテーブル追加と情報の明確化により、ユーザーがドキュメントレベルのアクセス制御やセキュリティフィルタリングをより理解しやすくなりました。
- ACLやRBACのインデックスガイドに、新しいプラクティスと具体的な使用例が追加されました。

## 破壊的変更
- 特に破壊的な変更はなく、内容の改善および整理が主な目的です。

## その他の更新
- 目次ファイルが更新され、新しいカテゴリとリンクが追加されました。
- 記事の日付が新しく更新されました。

# 洞察
Azure AI Searchのドキュメント更新は、ユーザーに高度な理解を促進するための重要なステップです。ドキュメントレベルのアクセス制御とセキュリティフィルタリングは、検索ソリューションの安全性を高める鍵となりますが、今回の更新により、これらの機能の利用がさらに容易になっています。

特に、アクセス制御リスト（ACL）とロールベースのアクセス制御（RBAC）のインデックス作成ガイドにおける更新は、開発者が検索インデックスのセキュリティを強化しながら効率的にシステムを運用するために必要な情報を提供しています。具体的な例とプラクティスが追加されたことで、実際のシナリオに基づいた理解が深まり、より現実的な使用に即しています。

目次の更新は、情報を探しやすくするだけでなく、Azure Searchに関する全体的な読者体験を向上させる重要な役割を果たすでしょう。特に、ネットワークアクセスや認証と認可に関する新しいセクションは、Azureプラットフォームを利用する際のセキュリティの計画に役立つでしょう。

これらの変更がユーザーに対する利便性を高め、Azure AI Searchの効果的かつ安全な活用を助けることが期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-document-level-access-overview.md](#item-4bb055) | minor update | ドキュメントレベルのアクセス制御の概要に関する更新 | modified | 68 | 33 | 101 | 
| [search-index-access-control-lists-and-rbac-push-api.md](#item-45e71e) | minor update | ACLおよびRBACのインデックス作成に関するガイドの更新 | modified | 36 | 23 | 59 | 
| [search-security-trimming-for-azure-search.md](#item-d8ae51) | minor update | Azure AI Searchにおけるセキュリティフィルタリングの改善 | modified | 2 | 2 | 4 | 
| [toc.yml](#item-c4768f) | minor update | Azure Searchの目次の更新 | modified | 38 | 34 | 72 | 


# Modified Contents
## articles/search/search-document-level-access-overview.md{#item-4bb055}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Conceptual overview of document-level permissions in Azure AI Search.
 author: gmndrg
 ms.author: gimondra
-ms.date: 05/10/2025
+ms.date: 06/06/2025
 ms.service: azure-ai-search
 ms.topic: conceptual
 ms.custom:
@@ -13,35 +13,70 @@ ms.custom:
   
 # Document-level access control in Azure AI Search  
   
-Azure AI Search offers support for document-level access control, enabling organizations to enforce fine-grained permissions seamlessly, from data ingestion through query execution. This capability is essential for building secure AI agentic systems grounding data, Retrieval-Augmented Generation (RAG) applications, and enterprise search solutions while maintaining compliance and user trust.  
+Azure AI Search supports document-level access control, enabling organizations to enforce fine-grained permissions at the document level, from data ingestion through query execution. This capability is essential for building secure AI agentic systems grounding data, Retrieval-Augmented Generation (RAG) applications, and enterprise search solutions that require authorization checks at the document level.  
   
-Document-level access helps restrict content visibility to authorized users, based on predefined access rules. Azure AI Search supports this functionality through multiple approaches, providing flexibility for integration. 
-  
-## Feature overview
-  
-Azure AI Search provides two approaches for document-level access control: native support for permission inheritance (applies to Azure Data Lake Storage (ADLS) Gen2) and security trimming.
+## Approaches for document-level access control
 
-### Security trimming via filters  
+| Approach | Description |
+|----------|-------------|
+| Security filters | String comparison. Your application passes in a user or group identity as a string, which populates a filter on a query, excluding any documents that don't match on the string. <br><br>Security filters are a technique for achieving document-level access control. This approach isn't bound to an API so you can use any version or package. |
+| ACLs (preview) | Microsoft Entra ID security principal behind the query token is compared to the permission metadata of documents returned in search results, excluding any documents that don't match on permissions. <br><br>Built-in access control list (ACL) support for principals is in preview, available in REST APIs and prerelease Azure SDK packages that provide the feature. |
 
-For scenarios where native ACL and RBAC integration isn't supported, Azure AI Search enables [security trimming using query filters](search-security-trimming-for-azure-search.md). By creating a field in the index to represent user or group identities, you can use the filters to include or exclude documents from query results based on those identities. This approach is useful for systems with custom access models or non-Microsoft Entra-based security frameworks.
+## Pattern for security trimming using filters  
 
-### Native support for POSIX-like ACL permissions (preview)
+For scenarios where native ACL integration isn't viable, we recommend security filters for trimming results based on exclusion criteria. The pattern includes the following components:
 
-Through Microsoft Entra ID, the [ADLS Gen2 access control model](/azure/storage/blobs/data-lake-storage-access-control-model) supports both Azure role-based access control (Azure RBAC) and POSIX-like access control lists (ACLs). In Azure AI Search using the newest preview APIs, you can flow these permission through to a search index and queries. 
+- Create a string field in the index to store strings of user or group identities.
+- Load the index with source documents that include a field containing the identities.
+- Include a filter expression in your query logic for matching on the string.
+- At query time, get the identity of the caller.
+- Pass in the identity of the caller as the filter string.
 
-ADLS Gen2 provides ACLs in a format that works well for this approach, but you can use any data source that provides permission data in the same format.
-  
-#### Retrieve permissions metadata during data ingestion process
+You can use push or pull model APIs. Because this approach is API agnostic, you just need to ensure that the index and query have valid strings (identities) for the filtration step.
 
-Azure AI Search enables you to push document permissions directly into the search index alongside the content, enabling consistent application of access rules at query time. This capability is achieved in two ways:  
-  
-- Use the [REST API](/rest/api/searchservice/operation-groups) or supported SDKs to [push documents and their associated permission metadata](search-index-access-control-lists-and-rbac-push-api.md) into the search index. This approach is ideal for systems with [Microsoft Entra](/Entra/fundamentals/what-is-Entra)-based [Access Control Lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control) and [Role-based access control (RBAC) roles](/azure/role-based-access-control/overview), such as [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/data-lake-storage-introduction). By embedding ACLs and RBAC container metadata within the index, developers can reduce the need for custom security trimming logic during query execution.
+This approach is useful for systems with custom access models or non-Microsoft security frameworks. For more information this approach, see [Security filters for trimming results in Azure AI Search](search-security-trimming-for-azure-search.md).
+
+## Pattern for native support for POSIX-like ACL permissions (preview)
+
+Native support is based on Microsoft Entra ID user and group access IDs affiliated with documents that you want to index and query. We recommend group access IDs for ease of management. The pattern includes the following components:
 
-- For [built-in ADLS Gen2 indexers](search-indexer-access-control-lists-and-role-based-access.md), you can use the preview REST API with the permission filter options to flow existing ACLs and RBAC permissions to your search index. This indexer pulls ACLs and RBAC roles at container level during the data ingestion process, enabling a low/no-code workflow for managing document-level permissions.  
+- Start with documents or files that have ACL assignments.
+- [Enable permission filters](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true#searchindexpermissionfilteroption) in the index.
+- [Add a permission filter](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true#permissionfilter) to a string field in an index.
+- Load the index with source documents having associated ACLs.
+- Query the index, [adding `x-ms-query-source-authorization`](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-05-01-preview&preserve-view=true#request-headers) in the request header.
+
+You can use the push model API, pushing any JSON documents to the search index, where the payload includes a string field providing POSIX-like ACLs for each document.
+
+Or, use the pull model (indexer) APIs if the data source is [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/data-lake-storage-introduction).  
   
-#### Enforce document-level permissions at query time
+### Retrieve permissions metadata during data ingestion process
+
+How you retrieve permissions varies depending on whether you're pushing a documents payload or using the ADLS Gen2 indexer.
+
+Start with a preview API that provides the feature:
+
+- [2025-05-01 preview REST API](/rest/api/searchservice/documents/?view=rest-searchservice-2025-05-01-preview&preserve-view=true)
+- [Azure SDK for Python prerelease package](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md#1160b12-2025-05-14)
+- [Azure SDK for .NET prerelease package](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1170-beta4-2025-05-14)
+- [Azure SDK for Java prerelease package](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md#1180-beta7-2025-05-16)
 
-With native [token-based querying](https://aka.ms/azs-query-preserving-permissions), Azure AI Search validates a user's [Microsoft Entra token](/Entra/identity/devices/concept-tokens-microsoft-Entra-id) to enforce ACLs and RBAC roles automatically. This functionality helps trim result sets to include only documents the user is authorized to access. You can achieve automatic trimming by attaching the user's Microsoft Entra token to your query request. For more information, see [Query-Time ACL and RBAC enforcement in Azure AI Search](search-query-access-control-rbac-enforcement.md).
+For the [push model approach](search-index-access-control-lists-and-rbac-push-api.md):
+
+1. Ensure your index schema is also created with a preview or prerelease SDK and that the schema has permission filters.
+1. Consider using the Microsoft Graph SDK to get group or user IDs.
+1. Use the [Index Documents](/rest/api/searchservice/documents/?view=rest-searchservice-2025-05-01-preview&preserve-view=true#indexdocumentsresult) or equivalent Azure SDK API to push documents and their associated permission metadata into the search index. 
+
+For the [pull model ADLS Gen2 indexer approach](search-indexer-access-control-lists-and-role-based-access.md):
+
+1. Verify that files in the directory are secured using the [ADLS Gen2 access control model](/azure/storage/blobs/data-lake-storage-access-control-model).
+1. Use the [Create Indexer](/rest/api/searchservice/indexers/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true) or equivalent Azure SDK API to create the indexer, index, and data source. 
+
+### Enforce document-level permissions at query time
+
+With native [token-based querying](https://aka.ms/azs-query-preserving-permissions), Azure AI Search validates a user's [Microsoft Entra token](/Entra/identity/devices/concept-tokens-microsoft-Entra-id), trimming result sets to include only documents the user is authorized to access. 
+
+You can achieve automatic trimming by attaching the user's Microsoft Entra token to your query request. For more information, see [Query-Time ACL and RBAC enforcement in Azure AI Search](search-query-access-control-rbac-enforcement.md).
 
 ## Benefits of document-level access control  
   
@@ -51,17 +86,17 @@ By offloading permission enforcement to Azure AI Search, developers can focus on
 
 Document-level permissions in Azure AI Search provide a structured framework for enforcing access controls that align with organizational policies. By using Microsoft Entra-based ACLs and RBAC roles, organizations can create systems that support robust compliance and promote trust among users. These built-in capabilities reduce the need for custom coding, offering a standardized approach to document-level security.  
 
-## Reference documents  
+## Tutorials and samples
   
-To help you dive deeper into document-level access control in Azure AI Search, here are more articles and samples:  
-  
-| Functionality                                   | Reference |  Sample |
-|---|---|---|
-| **Index permissions using Push APIs**           | [How to index permissions using REST API](search-index-access-control-lists-and-rbac-push-api.md)  |  [azure-search-rest-samples/Quickstart-ACL](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-ACL) or [azure-search-python-samples/Quickstart-Document-Permissions-Push-API](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Document-Permissions-Push-API) |
-| **Index ADLS Gen2 permissions metadata using built-in indexers** | [How to index permissions using ADLS Gen2 indexer](search-indexer-access-control-lists-and-role-based-access.md) and [Tutorial: Index ADLS Gen2 permissions metadata using an indexer](tutorial-adls-gen2-indexer-acls.md) |  [azure-search-python-samples/Quickstart-Document-Permissions-Pull-API](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Document-Permissions-Pull-API) |
-| **Query using Microsoft Entra token-based permissions** | [How to query using Microsoft Entra token-based permissions](https://aka.ms/azs-query-preserving-permissions) | See previous samples. |
-| **Security trimming via filters**              | [Security trimming via filters](search-security-trimming-for-azure-search.md)               |  Not available. |
-
-## Next steps  
-  
-- [Tutorial: Index ADLS Gen2 permissions metadata](tutorial-adls-gen2-indexer-acls.md)  
+Take a closer look at document-level access control in Azure AI Search with more articles and samples.
+
+- [Tutorial: Index ADLS Gen2 permissions metadata using an indexer](tutorial-adls-gen2-indexer-acls.md)
+- [azure-search-rest-samples/Quickstart-ACL](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-ACL)
+- [azure-search-python-samples/Quickstart-Document-Permissions-Push-API](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Document-Permissions-Push-API)
+- [azure-search-python-samples/Quickstart-Document-Permissions-Pull-API](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Document-Permissions-Pull-API)
+
+## Related content
+
+- [How to index document-level permissions using push API](search-index-access-control-lists-and-rbac-push-api.md)
+- [How to index document-level permissions using the ADLS Gen2 indexer](search-indexer-access-control-lists-and-role-based-access.md)
+- [How to query using Microsoft Entra token-based permissions](https://aka.ms/azs-query-preserving-permissions)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントレベルのアクセス制御の概要に関する更新"
}
```

### Explanation
この変更は、Azure AI Searchのドキュメントレベルアクセス制御に関する指針を更新するもので、主に説明の明確化と構造の整理が行われています。具体的には、ドキュメントレベルでのアクセス制御の機能に関する説明が改善され、アプローチの詳細なテーブルが追加されました。これにより、ユーザーが必要な情報を容易に見つけられるようになっています。また、日付の更新やいくつかの段落の再構成も行われ、文書全体の一貫性と分かりやすさが向上しました。さらに、関連するチュートリアルやサンプルへのリンクも再整理され、読者がさらに深く学習できることを目的としています。

## articles/search/search-index-access-control-lists-and-rbac-push-api.md{#item-45e71e}

<details>
<summary>Diff</summary>
````diff
@@ -1,43 +1,51 @@
 ---  
-title: Indexing ACLs and RBAC using REST API in Azure AI Search  
+title: Indexing ACLs using the push REST API
 titleSuffix: Azure AI Search  
 description: Learn how to use the REST API for indexing documents with ACLs and RBAC metadata.  
 ms.service: azure-ai-search  
-ms.topic: conceptual  
+ms.topic: how-to 
 ms.date: 05/19/2025  
 author: admayber
 ms.author: admayber  
 ---  
 
-# Indexing Access Control Lists (ACLs) and Role-Based Access Control (RBAC) using REST APIs in Azure AI Search  
+# Indexing document Access Control Lists (ACLs) using the push REST APIs
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-Indexing documents, along with their associated [Access Control Lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control) and container [Role-Based Access Control (RBAC) roles](/azure/role-based-access-control/overview), into an Azure AI Search index via the [REST API](/rest/api/searchservice/) offers fine-grained control over the indexing pipeline. This approach enables the inclusion of document entries with precise, document-level permissions directly within the index. This article explains how to use the REST API to index document-level permissions' metadata in Azure AI Search. This process prepares your index to query and enforce end-user permissions.
+Indexing documents, along with their associated [Access Control Lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control) and container [Role-Based Access Control (RBAC) roles](/azure/role-based-access-control/overview), into an Azure AI Search index via the [push REST APIs](/rest/api/searchservice/documents/?view=rest-searchservice-2025-05-01-preview&preserve-view=true) offers fine-grained control over the indexing pipeline. This approach enables the inclusion of document entries with precise, document-level permissions directly within the index. 
 
-## Supported scenarios  
-- Indexing ACLs metadata from [ENTRA-based](/entra/fundamentals/whatis), POSIX-style ACL systems, such as [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/data-lake-storage-introduction)
-- Indexing RBAC container metadata from ADLS Gen2.
+Key features include:
+
+- Flexible control over ingestion pipelines.
+- Standardized schema for permissions metadata.
+- Support for hierarchical permissions, such as folder-level ACLs.
+
+This article explains how to use the push REST API to index document-level permissions' metadata in Azure AI Search. This process prepares your index to query and enforce end-user permissions on search results.
+
+## Prerequisites
+
+- Content with ACL metadata from [Microsoft Entra ID](/entra/fundamentals/whatis) or another POSIX-style ACL system. 
+
+- Preview API version [2025-05-01-preview](/rest/api/searchservice/documents/?view=rest-searchservice-2025-05-01-preview&preserve-view=true) or a prerelease Azure SDK package providing equivalent features.
+
+- An index schema with a `permissionFilterOption` defined to hold the RBAC or ACL metadata.
+
+## Limitations
 
-### Limitations
 - An ACL field with permission filter type `userIds` or `groupIds` can hold at most 32 values.
+
 - An index can hold at most five unique values among fields of type `rbacScope` on all documents. There's no limit on the number of documents that share the same value of `rbacScope`.
-- A preexisting field can't be converted into a `permissionFilter` field type for use with built-in ACLs / RBAC metadata filtering. To enable filtering on an existing index, new fields must be created with the correct permission filter type.
-- Only one field of each `permissionFilter` type such as `groupIds`, `usersIds`, and `rbacScope`, can exist in an index.
 
-## Key features  
-- Flexible control over ingestion pipelines
-- Standardized schema for permissions metadata
-- Support for hierarchical permissions, such as folder-level ACLs, is available.
+- A preexisting field can't be converted into a `permissionFilter` field type for use with built-in ACLs or RBAC metadata filtering. To enable filtering on an existing index, new fields must be created with the correct permission filter type.
+
+- Only one field of each `permissionFilter` type such as `groupIds`, `usersIds`, and `rbacScope`, can exist in an index.
 
-## Requirements
-- ACLs and RBAC container roles are only supported in API version [2025-05-01-preview](/rest/api/searchservice/documents/?view=rest-searchservice-2025-05-01-preview&preserve-view=true) and later
-- You must create an index which has a schema with `permissionFilterOption` defined to hold the RBAC metadata and / or ACL values as desired
+## Create an index with permission filter fields
 
-## Creating an index with RBAC / ACL fields
-Indexing document ACLs and RBAC metadata with the REST API requires setting up an index schema that uses the desired field types for ACLs. See [How to Index Permission Information](tutorial-adls-gen2-indexer-acls.md) for a full walkthrough on how to set up an index with a schema that supports ACLs and RBAC metadata.
+Indexing document ACLs and RBAC metadata with the REST API requires setting up an index schema that enables permission filters and has fields with permission filter assignments.
 
-Permission filter field types can be added to an existing index. The value of `permissionFilterOption` can be set to either `enabled` or `disabled` while indexing documents. However, setting it to `disabled` turns off the permission filter functionality.
+Permission filter field types can be added to an existing index on new fields. The value of `permissionFilterOption` can be set to either `enabled` or `disabled` while indexing documents. However, setting it to `disabled` turns off the permission filter functionality.
 
 Here's a basic example schema that includes both user and group ACLs and RBAC metadata:
 
@@ -54,6 +62,7 @@ Here's a basic example schema that includes both user and group ACLs and RBAC me
 ```
 
 ## REST API indexing example
+
 Once you have an index with the desired permission filter fields, you can populate those values using the Indexing Push API as with any other document fields. Here's an example using the specified index schema.
 
 ```https
@@ -84,9 +93,11 @@ POST https://exampleservice.search.windows.net/indexes('indexdocumentsexample')/
 ```
 
 ## ACL access resolution rules
-This section explains how document access is determined for a user based on the ACL values assigned to each document. The key rule is that **a user only needs to match one ACL type to gain access to the document**. For example, if a document has fields for `userIds`, `groupIds`, and `rbacScope`, the user can access the document by matching any one of these ACL fields.
+
+This section explains how document access is determined for a user based on the ACL values assigned to each document. The key rule is that *a user only needs to match one ACL type to gain access to the document*. For example, if a document has fields for `userIds`, `groupIds`, and `rbacScope`, the user can access the document by matching any one of these ACL fields.
 
 ### Special ACL values "all" and "none"
+
 ACL fields, such as `userIds` and `groupIds`, typically contain lists of GUIDs (Globally Unique Identifiers) that identify the users and groups with access to the document. Two special string values, "all" and "none", are supported for these ACL field types. These values act as broad filters to control access at the global level as showcased in the following table. 
 
 | userIds / groupIds value | Meaning |
@@ -98,6 +109,7 @@ ACL fields, such as `userIds` and `groupIds`, typically contain lists of GUIDs (
 Because a user needs to match only one field type, the special value "all" grants public access regardless of the contents of any other ACL field, as all users are matched and granted permission. In contrast, setting `userIds` to "none" or "empty" means no users are granted access to the document _based on their user ID_. It might be possible that they're still granted access by matching their group ID or by RBAC metadata.
 
 ### Access control example
+
 This example illustrates how the document access rules are resolved based on the specific document ACL field values. For readability, this scenario uses ACL aliases such as "user1," "group1," etc., instead of GUIDs.
 
 | Document # | userIds | groupIds | RBAC Scope | Permitted users list | Note |
@@ -111,5 +123,6 @@ This example illustrates how the document access rules are resolved based on the
 | 7 | ["user1", "user2"] | [] | Empty | User1, user2, or any user with RBAC permissions to container1 | |
 
 ## Next steps
-- [How to query the index using end user ENTRA-token to enforce document-level permissions](search-query-access-control-rbac-enforcement.md)
-- [How to index ADLS Gen2 document-level permission information using indexers](tutorial-adls-gen2-indexer-acls.md)
+
+- [Query-Time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md)
+- [azure-search-python-samples/Quickstart-Document-Permissions-Push-API](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Document-Permissions-Push-API)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ACLおよびRBACのインデックス作成に関するガイドの更新"
}
```

### Explanation
このコードの変更では、Azure AI Searchにおけるアクセス制御リスト（ACL）およびロールベースのアクセス制御（RBAC）をREST APIを利用してインデックスに追加する方法についてのガイドが更新されています。主な変更点には、タイトルの簡潔化、トピックの再分類、主要な機能に関する追加情報の提供が含まれています。特に、ACLのインデックス付けに関連する新しいプラクティスや制約条件が強調されており、ACLメタデータの読み込みの流れや前提条件、制限について具体的に説明が加えられました。

また、既存のフィールドをACLまたはRBAC用のフィールドタイプに変える際の注意点が明確化されており、読み手がインデックス設定を容易に理解できるように工夫されています。最後に、具体的なインデックス作成例や、ACLやRBACのルールに基づくアクセス制御の例も追加されており、実践的な理解を深めるための情報が提供されています。

## articles/search/search-security-trimming-for-azure-search.md{#item-d8ae51}

<details>
<summary>Diff</summary>
````diff
@@ -10,12 +10,12 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 01/15/2025
+ms.date: 06/06/2025
 ---
 
 # Security filters for trimming results in Azure AI Search
 
-Azure AI Search doesn't provide native document-level permissions and can't vary search results based on user identity. As a workaround, you can create a filter that trims search results based on a string containing a group or user identity.
+For search solutions that can't use the [built-in access control list (ACL) support](search-document-level-access-overview.md)  for document-level authorization, Azure AI Search supports creating a filter that trims search results based on a string containing a group or user identity.
 
 This article describes a pattern for security filtering having the following steps:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおけるセキュリティフィルタリングの改善"
}
```

### Explanation
この変更では、Azure AI Searchにおけるセキュリティフィルタリングの概要が更新されています。主な内容は、ドキュメントレベルの権限を持たない検索ソリューションにおいて、グループまたはユーザーの識別子を含む文字列に基づいて検索結果をトリミングするフィルタの利用を強調しています。

具体的には、以前の文言から「Azure AI Searchはネイティブのドキュメントレベルの権限を提供しない」との表現が改訂され、代わりに「組み込みのアクセス制御リスト（ACL）サポートを利用できない場合」にフィルタの使用が推奨される旨が説明されています。また、更新の日付が変更され、記事に新しい日付が記載されています。このように、コンテンツが明確化され、ユーザーにとっての使い勝手が向上しています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -98,10 +98,8 @@ items:
     items:
     - name: Index encrypted blobs
       href: search-howto-index-encrypted-blobs.md
-    - name: Index permissioned ADLS Gen2 blobs
+    - name: Index permissioned ADLS Gen2 files
       href: tutorial-adls-gen2-indexer-acls.md
-    - name: Index any permission metadata
-      href: search-index-access-control-lists-and-rbac-push-api.md
   - name: Multimodal indexing tutorials
     items:
     - name: Use document extraction and multimodal embeddings
@@ -211,10 +209,6 @@ items:
       href: ./security-controls-policy.md
     - name: Security baseline
       href: /security/benchmark/azure/baselines/cognitive-search-security-baseline?toc=/azure/search/TOC.json
-    - name: Document-level security
-      href: search-document-level-access-overview.md
-    - name: Query with permission filters
-      href: search-query-access-control-rbac-enforcement.md
 - name: How-to guides
   items:
   - name: Service management
@@ -502,16 +496,26 @@ items:
         href: semantic-how-to-enable-scoring-profiles.md
   - name: Security
     items:
-    - name: Configure network access
-      href: service-configure-firewall.md
-    - name: Enable role-based access
-      href: search-security-enable-roles.md
-    - name: Assign roles (users)
-      href: search-security-rbac.md
-    - name: Assign roles (apps)
-      href: keyless-connections.md
-    - name: Authenticate with keys
-      href: search-security-api-keys.md
+    - name: Network access
+      items:
+      - name: Configure network access
+        href: service-configure-firewall.md
+      - name: Create a private endpoint
+        href: service-create-private-endpoint.md
+      - name: Troubleshoot private connections
+        href: troubleshoot-shared-private-link-resources.md
+      - name: Connect using Network Security Perimeter
+        href: search-security-network-security-perimeter.md
+    - name: Authentication and authorization
+      items:
+      - name: Enable role-based access
+        href: search-security-enable-roles.md
+      - name: Assign roles (users)
+        href: search-security-rbac.md
+      - name: Assign roles (apps)
+        href: keyless-connections.md
+      - name: Authenticate with keys
+        href: search-security-api-keys.md
     - name: Outbound connections
       items:
       - name: Configure a managed identity
@@ -530,32 +534,32 @@ items:
           href: search-howto-managed-identities-azure-functions.md
       - name: Connect through a firewall
         href: search-indexer-howto-access-ip-restricted.md
-      - name: Connect using Network Security Perimeter
-        href: search-security-network-security-perimeter.md
       - name: Connect as a trusted service
         href: search-indexer-howto-access-trusted-service-exception.md
       - name: Connect through a shared private link
         href: search-indexer-howto-access-private.md
       - name: Connect to a SQL managed instance private endpoint
         href: search-indexer-how-to-access-private-sql.md
-    - name: Document-level permissions
+    - name: Document-level access
       items:
-      - name: Security filters
+      - name: Document-level security overview
+        href: search-document-level-access-overview.md
+      - name: Use security filters
         href: search-security-trimming-for-azure-search.md
-      - name: ADLS Gen2 permission filters
-        href: search-indexer-access-control-lists-and-role-based-access.md
-    - name: Advanced options
-      items:
-      - name: Create a private endpoint
-        href: service-create-private-endpoint.md
-      - name: Troubleshoot private connections
-        href: troubleshoot-shared-private-link-resources.md
-      - name: Data encryption
+      - name: Use ACLs
         items:
-        - name: Customer-managed keys
-          href: search-security-manage-encryption-keys.md
-        - name: Find encrypted objects
-          href: search-security-get-encryption-keys.md
+        - name: Push document-level permissions to an index
+          href: search-index-access-control-lists-and-rbac-push-api.md
+        - name: Pull ADLS Gen2 permissions into an index
+          href: search-indexer-access-control-lists-and-role-based-access.md
+        - name: Query with permission filters
+          href: search-query-access-control-rbac-enforcement.md
+    - name: Data encryption
+      items:
+      - name: Customer-managed keys
+        href: search-security-manage-encryption-keys.md
+      - name: Find encrypted objects
+        href: search-security-get-encryption-keys.md
   - name: Development
     items:
     - name: API versions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Searchの目次の更新"
}
```

### Explanation
この変更では、Azure Searchに関する目次（TOC）ファイルが更新され、いくつかのリンクやセクションが整理されました。具体的には、ADLS Gen2に関連するファイルの名称が「Index permissioned ADLS Gen2 blobs」から「Index permissioned ADLS Gen2 files」に変更され、より明確な表現になっています。また、ドキュメントレベルのセキュリティに関するセクションが再構成され、トピックがより整理されて表示されるようになりました。

新たに「Network access」および「Authentication and authorization」といったカテゴリが追加され、各セクション内に関連するサブトピックが体系的に配置されています。これにより、ユーザーが必要な情報を迅速に見つけやすくなることを目的としています。また、リンク先のURLもいくつか変更されており、最新のガイドラインやリソースに対応しています。この更新は、ドキュメント全体の可読性を向上させ、情報へのアクセスを容易にするための重要なステップとなっています。


