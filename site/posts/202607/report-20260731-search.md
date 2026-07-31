---
date: '2026-07-31'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:205a580...MicrosoftDocs:c0c7917
summary: この差分では、主に以下の変更が行われました。クイックスタートガイドのリンクやコード記述が改善され、一貫性と明瞭性が向上しました。また、Azure
  AI SearchのAPIバージョンに関する文書が最新情報に更新され、マイグレーションの推奨が明確化されました。そして、RBACに関するセキュリティガイドが大幅に改訂され、手順の明確化と情報の整合性が向上しました。新たに具体的な操作手順やカスタムロール作成の例が追加されていますが、RBACに関する主要な改訂が既存のプロセスに影響を及ぼす可能性があるため、注意が必要です。全体として、これらの変更は利用者のドキュメンテーション体験を向上させることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:205a580...MicrosoftDocs:c0c7917){target="_blank"}

# Highlights
この差分では、以下の主要な変更が含まれています：

- クイックスタートガイドにおけるリンクやコード記述の修正により、一貫性と明瞭性が向上。
- Azure AI SearchのAPIバージョンに関する文書で、最新情報へのアップデートとマイグレーションの推奨をより明確化。
- RBACに関するセキュリティガイドの大幅改訂により、手順の明確化と情報の整合性向上が図られた。

## New features
- RBACにおける具体的な操作手順の追加。
- カスタムロール作成例の追加。

## Breaking changes
- RBACに関する主要な改訂は、既存のプロセスに影響を及ぼす可能性があるため、注意が必要。

## Other updates
- クイックスタートガイドのリンクとコード記述の改善。
- APIバージョンに関する情報の最新化。

# Insights
今回の修正は、利用者のドキュメンテーション体験を向上させるための全般的な強化を目的としています。特に、RBACのセキュリティガイドにおいて大幅な改訂が行われており、Azure AI Searchのロール管理がより明確かつアクセス可能になっています。

RBACドキュメントの大改訂は、Azureポータルなど各クライアントツールでのロール操作を詳細に説明するにとどまらず、カスタムロールの作成方法も具体的に示しています。これにより、技術者が実際の環境に適用しやすくなり、組織のセキュリティ・ポリシーを効果的に反映させることが可能です。

また、APIバージョン関連ドキュメントでは、非推奨バージョンの扱いとマイグレーションの推奨が強調され、最新の技術スタックの採用が促進されています。これにより、旧環境から新しいバージョンへのスムーズな移行が支援され、最新の機能を活用できるようになります。

クイックスタートガイドの細部における改訂は、一貫した経験の提供と、ユーザーが求める情報に迅速にアクセスできるようにするためのもので、特に初心者や新しい開発者にとっての学習のハードルを下げる効果があります。

全体として、この差分は、Azure AI Searchのセキュリティや検索機能をより一層理解し実装するための貴重なリソースとなるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-java.md](#item-4e2c55) | minor update | クイックスタートガイドの一部修正 | modified | 1 | 1 | 2 | 
| [full-text-java.md](#item-d659f9) | minor update | フルテキスト検索に関するクイックスタートガイドの修正 | modified | 4 | 4 | 8 | 
| [search-api-versions.md](#item-69ca3e) | minor update | APIバージョンに関する文書の更新 | modified | 20 | 23 | 43 | 
| [search-security-rbac.md](#item-a5d129) | breaking change | RBACに関するセキュリティガイドの大幅改訂 | modified | 495 | 149 | 644 | 


# Modified Contents
## articles/search/includes/quickstarts/agentic-retrieval-java.md{#item-4e2c55}

<details>
<summary>Diff</summary>
````diff
@@ -323,7 +323,7 @@ searchClient.uploadDocuments(documents);
 ```
 
 
-**Reference:** [SearchClient](/java/api/com.azure.search.documents.searchclient), [SearchDocument](/java/api/com.azure.search.documents.searchdocument)
+**Reference:** [SearchClient](/java/api/com.azure.search.documents.searchclient), SearchDocument
 
 ### Create a knowledge source
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートガイドの一部修正"
}
```

### Explanation
この変更は、`agentic-retrieval-java.md`ファイルの中で、参照リンクに関するテキストを微調整したものです。具体的には、"SearchDocument"の前にあったリンク形式が削除され、そのままの形で表記されています。これにより、文書内の参照がより一貫性を持ち、明確になりました。変更は1行追加され、1行削除されており、全体の構成が整えられています。この修正により、ユーザーが情報を確認しやすくなっています。

## articles/search/includes/quickstarts/full-text-java.md{#item-d659f9}

<details>
<summary>Diff</summary>
````diff
@@ -162,7 +162,7 @@ This example uses synchronous methods of the [SearchIndexClient](/java/api/com.a
 
 You create two helper classes, `Hotel.java` and `Address.java`, to define the structure of a hotel document and its address. The `Hotel` class includes fields for a hotel ID, name, description, category, tags, parking, renovation date, rating, and address. The `Address` class includes fields for street address, city, state/province, postal code, and country/region.
 
-In the azure-search-documents client library, you can use [SearchableField](/java/api/com.azure.search.documents.indexes.searchablefield) and [SimpleField](/java/api/com.azure.search.documents.indexes.simplefield) to streamline field definitions. Both are annotations that you can apply to fields or methods to generate a [SearchField](/java/api/com.azure.search.documents.indexes.models.searchfield):
+In the azure-search-documents client library, you can use `SearchableField` and `SimpleField` to streamline field definitions. Both are annotations that you can apply to fields or methods to generate a [SearchField](/java/api/com.azure.search.documents.indexes.models.searchfield):
 
 + `SimpleField` can be any data type, is always nonsearchable (ignored for full-text search queries), and is retrievable (not hidden). Other attributes are off by default, but can be enabled. You might use a `SimpleField` for document IDs or fields used only in filters, facets, or scoring profiles. If so, apply any attributes that are necessary for the scenario, such as `isKey = true` for a document ID.
 + `SearchableField` must be a string, and is always searchable and retrievable. Other attributes are off by default, but can be enabled. Because this field type is searchable, it supports synonyms and the full complement of analyzer properties.
@@ -186,7 +186,7 @@ Azure AI Search searches over content stored in the service. In this step, you l
 
 In Azure AI Search, search documents are data structures that are both inputs to indexing and outputs from queries. As obtained from an external data source, document inputs might be rows in a database, blobs in Azure Blob Storage, or JSON documents on disk. In this example, you take a shortcut and embed JSON documents for four hotels directly.
 
-When uploading documents, you must use an [IndexDocumentsBatch](/java/api/com.azure.search.documents.indexes.models.indexdocumentsbatch) object. An `IndexDocumentsBatch` object contains a collection of [IndexActions](/java/api/com.azure.search.documents.models.indexaction), each of which contains a document and a property telling Azure AI Search what action to perform ([upload, merge, delete, and mergeOrUpload](/azure/search/search-what-is-data-import#indexing-actions)).
+When uploading documents, you must use an `IndexDocumentsBatch` object. An `IndexDocumentsBatch` object contains a collection of [IndexActions](/java/api/com.azure.search.documents.models.indexaction), each of which contains a document and a property that tells Azure AI Search what action to perform ([upload, merge, delete, and mergeOrUpload](/azure/search/search-what-is-data-import#indexing-actions)).
 
 In `App.java`, you create an array of documents and index actions, and then pass the array to `IndexDocumentsBatch`. The following documents conform to the hotels-quickstart index, as defined by the hotel class.
 
@@ -230,7 +230,7 @@ private static void uploadDocuments(SearchClient searchClient)
 }
 ```
 
-The `uploadDocuments` method creates an [IndexDocumentsBatch](/java/api/com.azure.search.documents.indexes.models.indexdocumentsbatch) and calls [indexDocuments](/java/api/com.azure.search.documents.searchclient) on a [SearchClient](/java/api/com.azure.search.documents.searchclient) to upload the documents. This quickstart creates `SearchClient` independently using [SearchClientBuilder](/java/api/com.azure.search.documents.searchclientbuilder), which requires configuring the endpoint and credentials separately.
+The `uploadDocuments` method creates an `IndexDocumentsBatch` and calls [indexDocuments](/java/api/com.azure.search.documents.searchclient) on a [SearchClient](/java/api/com.azure.search.documents.searchclient) to upload the documents. This quickstart creates `SearchClient` independently by using [SearchClientBuilder](/java/api/com.azure.search.documents.searchclientbuilder), which requires configuring the endpoint and credentials separately.
 
 ```java
 uploadDocuments(searchClient);
@@ -258,7 +258,7 @@ You can get query results as soon as the first document is indexed, but actual t
 
 This section adds two pieces of functionality: query logic and results. For queries, use the [search](/java/api/com.azure.search.documents.searchclient) method. This method takes search text (the query string) and other [options](/java/api/com.azure.search.documents.models.searchoptions).
 
-The [SearchPagedIterable](/java/api/com.azure.search.documents.util.searchpagediterable) class represents the results.
+The `SearchPagedIterable` class represents the results.
 
 In `App.java`, the `WriteDocuments` method prints search results to the console.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フルテキスト検索に関するクイックスタートガイドの修正"
}
```

### Explanation
この変更は、`full-text-java.md`ファイルにおけるフルテキスト検索のクイックスタートガイドを微調整するもので、いくつかの文において、コードの表示方法や説明を改善しました。具体的には、クラス名やメソッド名の前後でのバッククォートの使用を追加し、コードとしての視認性を向上させています。また、コメントや説明文の明確さを増すために一部の文が修正されています。この修正により、ユーザーがフルテキスト検索を利用する際に、より明確で理解しやすい情報を得ることができるようになりました。全体的に、4行の追加と削除が行われ、合計8カ所の変更が加えられています。

## articles/search/search-api-versions.md{#item-69ca3e}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
 title: API Versions
-description: Version policy for Azure AI Search REST APIs and the client library in the .NET SDK.
+description: Version policy for Azure AI Search REST APIs and the Azure SDK client libraries.
 ms.service: azure-ai-search
 ms.custom:
   - devx-track-dotnet
@@ -9,7 +9,8 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: concept-article
-ms.date: 03/25/2026
+ms.date: 07/28/2026
+ai-usage: ai-assisted
 ---
 
 # API versions in Azure AI Search
@@ -18,30 +19,28 @@ ms.date: 03/25/2026
 
 Azure AI Search rolls out feature updates regularly. Sometimes, but not always, these updates require a new version of the API to preserve backward compatibility. Publishing a new version allows you to control when and how you integrate search service updates in your code.
 
-As a rule, the REST APIs and libraries are versioned only when necessary, since it can involve some effort to upgrade your code to use a new API version. A new version is needed only if some aspect of the API has changed in a way that breaks backward compatibility. Such changes can happen because of fixes to existing features, or because of new features that change existing API surface area.
+As a rule, the REST APIs and Azure SDK client libraries are versioned only when necessary, since it can involve some effort to upgrade your code to use a new API version. A new version is needed only if some aspect of the API has changed in a way that breaks backward compatibility. Such changes can happen because of fixes to existing features, or because of new features that change existing API surface area.
 
 For more information about the deprecation path, see the [Azure SDK lifecycle and support policy](https://azure.github.io/azure-sdk/policies_support.html).
 
 ## Deprecated versions
 
-**2023-07-01-preview** was deprecated on April 8, 2024 and is no longer supported as of July 8, 2024.
-
-This was the first REST API that offered vector search support. Newer API versions have a different vector configuration. You should [migrate to a newer version](search-api-migration.md) as soon as possible.
+**2023-07-01-preview** was deprecated on April 8, 2024 and is no longer supported as of July 8, 2024. This version was the first REST API that offered vector search support. Newer API versions have a different vector configuration. [Migrate to a newer API version](search-api-migration.md) or to a newer SDK version as soon as possible.
 
 <a name="unsupported-versions"></a>
 
 ## Discontinued versions
 
-Some API versions are discontinued and are no longer documented or supported:
+As of October 15, 2020, the following API versions are discontinued and no longer documented or supported:
 
 + **2015-02-28**
 + **2015-02-28-Preview**
 + **2014-07-31-Preview**
 + **2014-10-20-Preview**
 
-All SDKs are based on REST API versions. If a REST version is discontinued, SDK packages based on that version are also discontinued. All Azure AI Search .NET SDKs older than [**3.0.0-rc**](https://www.nuget.org/packages/Microsoft.Azure.Search/3.0.0-rc) are now obsolete.
+All SDKs are based on REST API versions. If a REST API version is discontinued, the SDK packages based on it are also discontinued. All Azure AI Search .NET SDKs older than [**3.0.0-rc**](https://www.nuget.org/packages/Microsoft.Azure.Search/3.0.0-rc) are now obsolete.
 
-Support for the above-listed versions ended on October 15, 2020. If you have code that uses a discontinued version, you can [migrate existing code](search-api-migration.md) to a newer [REST API version](/rest/api/searchservice/) or to a newer Azure SDK.
+If you have code that uses a discontinued version, [migrate to a newer API version](search-api-migration.md) or to a newer SDK version.
 
 ## REST APIs
 
@@ -52,33 +51,31 @@ Support for the above-listed versions ended on October 15, 2020. If you have cod
 
 ## Azure SDK for .NET
 
-The following table provides links to more recent SDK versions.
-
-| SDK version | Status | Change log | Description |
+| SDK version | Status | Changelog | Description |
 |-------------|--------|------------ |-----------------|
-| [Azure.Search.Documents 11](/dotnet/api/overview/azure/search.documents-readme) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | APIs for data plane operations on a service, such as read-write operations on content and objects. |
-| [Azure.ResourceManager.Search](https://www.nuget.org/packages/Microsoft.Azure.Management.Search/4.0.0) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.ResourceManager.Search/CHANGELOG.md) | APIs for control plane operations on the search service. |
+| [Azure.Search.Documents 12](/dotnet/api/overview/azure/search.documents-readme) | Active | [Changelog](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | APIs for data plane operations on a service, such as read-write operations on content and objects. |
+| [Azure.ResourceManager.Search](https://www.nuget.org/packages/Microsoft.Azure.Management.Search/4.0.0) | Active | [Changelog](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.ResourceManager.Search/CHANGELOG.md) | APIs for control plane operations on the search service. |
 
 ## Azure SDK for Java
 
-| SDK version | Status | Change log | Description |
+| SDK version | Status | Changelog | Description |
 |-------------|--------|------------|-----------------|
-| [azure-search-documents 11](/java/api/overview/azure/search-documents-readme) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) Use the `azure-search-documents` client library for data plane operations. |
-| [azure-resourcemanager-search 2](/java/api/overview/azure/resourcemanager-search-readme) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-resourcemanager-search/CHANGELOG.md) | Use the `azure-resourcemanager-search` client library for control plane operations. |
+| [azure-search-documents 12](/java/api/overview/azure/search-documents-readme) | Active | [Changelog](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | Use the `azure-search-documents` client library for data plane operations. |
+| [azure-resourcemanager-search 2](/java/api/overview/azure/resourcemanager-search-readme) | Active | [Changelog](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-resourcemanager-search/CHANGELOG.md) | Use the `azure-resourcemanager-search` client library for control plane operations. |
 
 ## Azure SDK for JavaScript
 
-| SDK version | Status | Change log | Description |
+| SDK version | Status | Changelog | Description |
 |-------------|--------|------------|------------------|
-| [@azure/search-documents 12](/javascript/api/overview/azure/search-documents-readme) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | Use the `@azure/search-documents` client library for data plane operations. |
-| [@azure/arm-search 4](/javascript/api/overview/azure/arm-search-readme) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/arm-search/CHANGELOG.md) | Use the `@azure/arm-search` package for control plane operations. |
+| [@azure/search-documents 13](/javascript/api/overview/azure/search-documents-readme) | Active | [Changelog](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | Use the `@azure/search-documents` client library for data plane operations. |
+| [@azure/arm-search 4](/javascript/api/overview/azure/arm-search-readme) | Active | [Changelog](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/arm-search/CHANGELOG.md) | Use the `@azure/arm-search` package for control plane operations. |
 
 ## Azure SDK for Python
 
-| SDK version | Status | Change log | Description |
+| SDK version | Status | Changelog | Description |
 |-------------|--------|------------|------------------|
-| [azure-search-documents 11](/python/api/overview/azure/search-documents-readme) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | Use the `azure-search-documents` client library for data plane operations. |
-| [azure-mgmt-search 9](https://pypi.org/project/azure-mgmt-search/) | Active | [Change Log](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-mgmt-search/CHANGELOG.md) | Use the `azure-mgmt-search` client library for control plane operations. |
+| [azure-search-documents 12](/python/api/overview/azure/search-documents-readme) | Active | [Changelog](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | Use the `azure-search-documents` client library for data plane operations. |
+| [azure-mgmt-search 9](https://pypi.org/project/azure-mgmt-search/) | Active | [Changelog](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-mgmt-search/CHANGELOG.md) | Use the `azure-mgmt-search` client library for control plane operations. |
 
 ## All Azure SDKs
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンに関する文書の更新"
}
```

### Explanation
この変更は、`search-api-versions.md`ファイルにおけるAzure AI SearchのAPIバージョンに関する説明を見直し、いくつかの文言を更新したものです。具体的には、Azure SDKクライアントライブラリに関する説明を明確にし、日付要素を最新のものに更新しました。また、Deprecated（非推奨）およびDiscontinued（廃止）バージョンに関する情報が整理され、ユーザーに対するマイグレーションの推奨が強調されています。さらに、SDKのバージョンに関する表においても、バージョン番号を最新のものに更新し、"Changelog"の表記を統一しました。変更総数は43カ所で、20行が追加され、23行が削除されています。この改訂によって、利用者が関連情報をより容易に理解できるようになっています。

## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Connect Using Azure Roles
 description: Learn how to assign Azure roles in Azure AI Search to manage permissions for service administration, development, and query access with Microsoft Entra ID.
-ms.date: 04/06/2026
+ms.date: 07/24/2026
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: how-to
@@ -19,7 +19,7 @@ ai-usage: ai-assisted
 
 Azure AI Search supports [role-based access control](/azure/role-based-access-control/role-assignments-steps) through Microsoft Entra ID. Role-based access is optional but recommended. The alternative is [key-based authentication](search-security-api-keys.md), which is the default.
 
-If you assign multiple roles to a security principal, permissions are combined. Role assignments apply across all tools and client libraries. You can assign roles using any [supported approach](/azure/role-based-access-control/role-assignments-steps#step-5-assign-role).
+If you assign multiple roles to a security principal, permissions are combined. Role assignments apply across all tools and client libraries.
 
 This article explains how to assign built-in roles for service administration, development, and read-only query and retrieval access. It also provides steps for creating custom roles and testing role assignments.
 
@@ -37,6 +37,14 @@ This article explains how to assign built-in roles for service administration, d
   + Role Based Access Control Administrator
   + A custom role with [Microsoft.Authorization/roleAssignments/write](/azure/templates/microsoft.authorization/roleassignments) permissions
 
++ Review the role assignment instructions for your preferred client:
+   + [Assign Azure roles using the Azure portal](/azure/role-based-access-control/role-assignments-portal)
+   + [Assign Azure roles using Azure CLI](/azure/role-based-access-control/role-assignments-cli)
+   + [Assign Azure roles using Azure PowerShell](/azure/role-based-access-control/role-assignments-powershell)
+   + [Assign Azure roles using the REST API](/azure/role-based-access-control/role-assignments-rest)
+
++ Identify the assignee value required by your preferred client. Depending on the client and assignee type, this value might be a user principal name, group object ID, service principal name, service principal application ID, or Microsoft Entra object ID.
+
 ## Built-in roles
 
 Roles are a collection of permissions that affect the control plane or data plane:
@@ -105,7 +113,7 @@ The following roles let you create, configure, and manage a search service. Thes
 | [Contributor](#role-descriptions) | b24988ac-6180-42a0-ab88-20f7382dd24c |
 | [Reader](#role-descriptions) | acdd72a7-3385-48ef-bd42-f606fba81ae7 |
 
-#### [**Azure portal**](#tab/roles-portal-admin)
+#### [Portal](#tab/portal)
 
 1. Go to your search service in the [Azure portal](https://portal.azure.com).
 
@@ -121,19 +129,75 @@ The following roles let you create, configure, and manage a search service. Thes
 
 1. On the **Review + assign** tab, select **Review + assign** to assign the role.
 
-#### [**PowerShell**](#tab/roles-powershell-admin)
+#### [CLI](#tab/cli)
+
+1. Sign in to your Azure subscription.
+
+   ```azurecli
+   az login
+   ```
+
+1. Create a role assignment scoped to the search service. Provide the assignee and scope.
+
+   ```azurecli
+   az role assignment create \
+       --assignee <assignee> \
+       --role "Reader" \
+       --scope "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>"
+   ```
+
+   **Reference:** [az role assignment create](/cli/azure/role/assignment#az-role-assignment-create)
+
+#### [PowerShell](#tab/powershell)
+
+1. Import the required module and connect to your Azure account.
+
+   ```powershell
+   Import-Module Az.Resources
+   Connect-AzAccount
+   ```
+
+1. Create a role assignment scoped to the search service. This example uses a user sign-in name.
+
+   ```powershell
+   New-AzRoleAssignment -SignInName <email> `
+       -RoleDefinitionName "Reader" `
+       -Scope  "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>"
+   ```
+
+   **Reference:** [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment)
+
+#### [REST](#tab/rest)
+
+1. Open a command shell and sign in to your Azure subscription.
+
+   ```azurecli
+   az login
+   ```
+
+1. Get an access token for Azure Resource Manager.
+
+   ```azurecli
+   az account get-access-token --scope https://management.azure.com/.default --query accessToken --output tsv
+   ```
 
-When you [assign roles using PowerShell](/azure/role-based-access-control/role-assignments-powershell), call `New-AzRoleAssignment`, providing the Azure user or group name and the scope of the assignment.
+1. Send a PUT request to create a role assignment scoped to the search service. Set `principalType` to `User`, `Group`, or `ServicePrincipal` to match the assignee.
 
-This example creates a role assignment scoped to a search service:
+   ```http
+   PUT https://management.azure.com/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/providers/Microsoft.Authorization/roleAssignments/<role-assignment-guid>?api-version=2022-04-01 HTTP/1.1
+   Authorization: Bearer <access-token>
+   Content-Type: application/json
 
-```powershell
-New-AzRoleAssignment -SignInName <email> `
-    -RoleDefinitionName "Reader" `
-    -Scope  "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>"
-```
+   {
+       "properties": {
+           "roleDefinitionId": "/subscriptions/<subscription>/providers/Microsoft.Authorization/roleDefinitions/acdd72a7-3385-48ef-bd42-f606fba81ae7",
+           "principalId": "<principal-object-id>",
+           "principalType": "<principal-type>"
+       }
+   }
+   ```
 
-**Reference:** [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment)
+   **Reference:** [Role Assignments - Create](/rest/api/authorization/role-assignments/create)
 
 ---
 
@@ -147,7 +211,7 @@ The following roles let you create search objects, load documents, query indexes
 | [Search Index Data Contributor](#role-descriptions) | 8ebe5a00-799e-43f5-93ac-243d3dce84a7 |
 | [Search Index Data Reader](#role-descriptions) | 1407120a-92aa-4202-b7e9-c0e197c71c8f |
 
-#### [**Azure portal**](#tab/roles-portal)
+#### [Portal](#tab/portal)
 
 1. Go to your search service in the [Azure portal](https://portal.azure.com).
 
@@ -165,27 +229,114 @@ The following roles let you create search objects, load documents, query indexes
 
 1. Repeat these steps to assign **Search Index Data Contributor** and **Search Index Data Reader**.
 
-#### [**PowerShell**](#tab/roles-powershell)
+#### [CLI](#tab/cli)
 
-When you [assign roles using PowerShell](/azure/role-based-access-control/role-assignments-powershell), call `New-AzRoleAssignment`, providing the Azure user or group name and the scope of the assignment.
+1. Sign in to your Azure subscription.
 
-This example creates a role assignment scoped to a search service:
+   ```azurecli
+   az login
+   ```
 
-```powershell
-New-AzRoleAssignment -SignInName <email> `
-    -RoleDefinitionName "Search Index Data Contributor" `
-    -Scope  "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>"
-```
+1. Create a role assignment scoped to the search service. Provide the assignee and scope.
 
-This example creates a role assignment scoped to a specific index:
+   ```azurecli
+   az role assignment create \
+       --assignee <assignee> \
+       --role "Search Index Data Contributor" \
+       --scope "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>"
+   ```
+
+   **Reference:** [az role assignment create](/cli/azure/role/assignment#az-role-assignment-create)
+
+1. (Optional) Create a role assignment scoped to an index. Provide the assignee and scope.
+
+   ```azurecli
+   az role assignment create \
+       --assignee <assignee> \
+       --role "Search Index Data Contributor" \
+       --scope "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/indexes/<index-name>"
+   ```
+
+   **Reference:** [az role assignment create](/cli/azure/role/assignment#az-role-assignment-create)
 
-```powershell
-New-AzRoleAssignment -SignInName <email> `
-    -RoleDefinitionName "Search Index Data Contributor" `
-    -Scope  "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/indexes/<index-name>"
-```
+#### [PowerShell](#tab/powershell)
 
-**Reference:** [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment)
+1. Import the required module and connect to your Azure account.
+
+   ```powershell
+   Import-Module Az.Resources
+   Connect-AzAccount
+   ```
+
+1. Create a role assignment scoped to the search service. This example uses a user sign-in name.
+
+   ```powershell
+   New-AzRoleAssignment -SignInName <email> `
+       -RoleDefinitionName "Search Index Data Contributor" `
+       -Scope  "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>"
+   ```
+
+   **Reference:** [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment)
+
+1. (Optional) Create a role assignment scoped to an index. This example uses a user sign-in name.
+
+   ```powershell
+   New-AzRoleAssignment -SignInName <email> `
+       -RoleDefinitionName "Search Index Data Contributor" `
+       -Scope  "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/indexes/<index-name>"
+   ```
+
+   **Reference:** [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment)
+
+#### [REST](#tab/rest)
+
+1. Open a command shell and sign in to your Azure subscription.
+
+   ```azurecli
+   az login
+   ```
+
+1. Get an access token for Azure Resource Manager.
+
+   ```azurecli
+   az account get-access-token --scope https://management.azure.com/.default --query accessToken --output tsv
+   ```
+
+1. Send a PUT request to create a role assignment scoped to the search service. Set `principalType` to `User`, `Group`, or `ServicePrincipal` to match the assignee.
+
+   ```http
+   PUT https://management.azure.com/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/providers/Microsoft.Authorization/roleAssignments/<role-assignment-guid>?api-version=2022-04-01 HTTP/1.1
+   Authorization: Bearer <access-token>
+   Content-Type: application/json
+
+   {
+       "properties": {
+           "roleDefinitionId": "/subscriptions/<subscription>/providers/Microsoft.Authorization/roleDefinitions/8ebe5a00-799e-43f5-93ac-243d3dce84a7",
+           "principalId": "<principal-object-id>",
+           "principalType": "<principal-type>"
+       }
+   }
+   ```
+
+   **Reference:** [Role Assignments - Create](/rest/api/authorization/role-assignments/create)
+
+1. (Optional) Send a PUT request to create a role assignment scoped to an index.
+
+   ```http
+   PUT https://management.azure.com/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/indexes/<index-name>/providers/Microsoft.Authorization/roleAssignments/<role-assignment-guid>?api-version=2022-04-01 HTTP/1.1
+   Authorization: Bearer <access-token>
+   Content-Type: application/json
+
+   {
+       "properties": {
+           "roleDefinitionId": "/subscriptions/<subscription>/providers/Microsoft.Authorization/roleDefinitions/8ebe5a00-799e-43f5-93ac-243d3dce84a7",
+           "principalId": "<principal-object-id>",
+           "principalType": "<principal-type>"
+       }
+   }
+   ```
+
+   **Reference:** [Role Assignments - Create](/rest/api/authorization/role-assignments/create)
 
 ---
 
@@ -197,7 +348,7 @@ Use the following role for apps and processes that only need read access to inde
 | -- | -- |
 | [Search Index Data Reader](#role-descriptions) | 1407120a-92aa-4202-b7e9-c0e197c71c8f |
 
-#### [**Azure portal**](#tab/roles-portal-query)
+#### [Portal](#tab/portal)
 
 1. Go to your search service in the [Azure portal](https://portal.azure.com).
 
@@ -213,43 +364,114 @@ Use the following role for apps and processes that only need read access to inde
 
 1. On the **Review + assign** tab, select **Review + assign** to assign the role.
 
-#### [**PowerShell**](#tab/roles-powershell-query)
+#### [CLI](#tab/cli)
+
+1. Sign in to your Azure subscription.
+
+   ```azurecli
+   az login
+   ```
+
+1. Create a role assignment scoped to the search service. Provide the assignee and scope.
 
-When you [assign roles using PowerShell](/azure/role-based-access-control/role-assignments-powershell), call `New-AzRoleAssignment`, providing the Azure user or group name and the scope of the assignment.
+   ```azurecli
+   az role assignment create \
+       --assignee <assignee> \
+       --role "Search Index Data Reader" \
+       --scope "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>"
+   ```
 
-1. Get your subscription ID, search service resource group, and search service name.
+   **Reference:** [az role assignment create](/cli/azure/role/assignment#az-role-assignment-create)
 
-1. Get the object identifier of your Azure service, such as Azure OpenAI.
+1. (Optional) Create a role assignment scoped to an index. Provide the assignee and scope.
 
-   ```azurepowershell
-    Get-AzADServicePrincipal -SearchString <your-azure-openai-resource-name>
+   ```azurecli
+   az role assignment create \
+       --assignee <assignee> \
+       --role "Search Index Data Reader" \
+       --scope "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/indexes/<index-name>"
    ```
 
-   The output includes an `Id` property containing the object ID you need for the role assignment.
+   **Reference:** [az role assignment create](/cli/azure/role/assignment#az-role-assignment-create)
+
+#### [PowerShell](#tab/powershell)
 
-1. Get the role definition and review the permissions to make sure this is the role you want.
+1. Import the required module and connect to your Azure account.
 
-   ```azurepowershell
-   Get-AzRoleDefinition -Name "Search Index Data Reader"
+   ```powershell
+   Import-Module Az.Resources
+   Connect-AzAccount
    ```
 
-1. Create the role assignment, substituting valid values for the placeholders.
+1. Create a role assignment scoped to the search service. This example uses a user sign-in name.
 
-   ```azurepowershell
-   New-AzRoleAssignment -ObjectId <your-azure-openai-object-id> -RoleDefinitionName "Search Index Data Reader" -Scope /subscriptions/<your-subscription-id>/resourcegroups/<your-resource-group>/providers/Microsoft.Search/searchServices/<your-search-service-name>
+   ```powershell
+   New-AzRoleAssignment -SignInName <email> `
+       -RoleDefinitionName "Search Index Data Reader" `
+       -Scope  "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>"
    ```
 
-   A successful assignment returns the role assignment details including `RoleAssignmentId`.
+   **Reference:** [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment)
 
-1. Here's an example of a role assignment scoped to a specific index:
+1. (Optional) Create a role assignment scoped to an index. This example uses a user sign-in name.
 
-    ```powershell
-    New-AzRoleAssignment -ObjectId <your-azure-openai-object-id> `
-        -RoleDefinitionName "Search Index Data Reader" `
-        -Scope /subscriptions/<your-subscription-id>/resourcegroups/<your-resource-group>/providers/Microsoft.Search/searchServices/<your-search-service-name>/indexes/<your-index-name>
-    ```
+   ```powershell
+   New-AzRoleAssignment -SignInName <email> `
+       -RoleDefinitionName "Search Index Data Reader" `
+       -Scope  "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/indexes/<index-name>"
+   ```
+
+   **Reference:** [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment)
+
+#### [REST](#tab/rest)
+
+1. Open a command shell and sign in to your Azure subscription.
+
+   ```azurecli
+   az login
+   ```
+
+1. Get an access token for Azure Resource Manager.
+
+   ```azurecli
+   az account get-access-token --scope https://management.azure.com/.default --query accessToken --output tsv
+   ```
+
+1. Send a PUT request to create a role assignment scoped to the search service. Set `principalType` to `User`, `Group`, or `ServicePrincipal` to match the assignee.
+
+   ```http
+   PUT https://management.azure.com/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/providers/Microsoft.Authorization/roleAssignments/<role-assignment-guid>?api-version=2022-04-01 HTTP/1.1
+   Authorization: Bearer <access-token>
+   Content-Type: application/json
+
+   {
+       "properties": {
+           "roleDefinitionId": "/subscriptions/<subscription>/providers/Microsoft.Authorization/roleDefinitions/1407120a-92aa-4202-b7e9-c0e197c71c8f",
+           "principalId": "<principal-object-id>",
+           "principalType": "<principal-type>"
+       }
+   }
+   ```
+
+   **Reference:** [Role Assignments - Create](/rest/api/authorization/role-assignments/create)
+
+1. (Optional) Send a PUT request to create a role assignment scoped to an index.
+
+   ```http
+   PUT https://management.azure.com/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/indexes/<index-name>/providers/Microsoft.Authorization/roleAssignments/<role-assignment-guid>?api-version=2022-04-01 HTTP/1.1
+   Authorization: Bearer <access-token>
+   Content-Type: application/json
+
+   {
+       "properties": {
+           "roleDefinitionId": "/subscriptions/<subscription>/providers/Microsoft.Authorization/roleDefinitions/1407120a-92aa-4202-b7e9-c0e197c71c8f",
+           "principalId": "<principal-object-id>",
+           "principalType": "<principal-type>"
+       }
+   }
+   ```
 
-    **Reference:** [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment)
+   **Reference:** [Role Assignments - Create](/rest/api/authorization/role-assignments/create)
 
 ---
 
@@ -259,7 +481,7 @@ Use a client to test role assignments. Remember that roles are cumulative. You c
 
 Before you proceed, [configure your application for keyless connections](search-security-rbac-client-code.md) and have role assignments in place.
 
-### [**Azure portal**](#tab/test-portal)
+### [Portal](#tab/test-portal)
 
 1. Go to your search service in the [Azure portal](https://portal.azure.com).
 
@@ -271,7 +493,7 @@ Before you proceed, [configure your application for keyless connections](search-
 
    + Search Index Data Readers can query indexes. To verify permissions, use [Search explorer](search-explorer.md). You should be able to send queries and view results, but you shouldn't be able to view index definitions or create indexes.
 
-### [**REST API**](#tab/test-rest)
+### [REST](#tab/test-rest)
 
 This approach assumes Visual Studio Code with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
@@ -281,12 +503,6 @@ This approach assumes Visual Studio Code with the [REST Client extension](https:
    az login
    ```
 
-1. Get your tenant ID and subscription ID. Use the ID as a variable in a future step. 
-
-   ```azurecli
-   az account show
-   ```
-
 1. Get an access token for the Azure AI Search data plane.
 
    ```azurecli
@@ -305,28 +521,28 @@ This approach assumes Visual Studio Code with the [REST Client extension](https:
 
    ```http
    POST https://{{baseUrl}}/indexes/{{index-name}}/docs/search?api-version=2026-04-01 HTTP/1.1
-     Content-type: application/json
-     Authorization: Bearer {{token}}
-
-       {
-            "queryType": "simple",
-            "search": "motel",
-            "filter": "",
-            "select": "HotelName,Description,Category,Tags",
-            "count": true
-        }
+   Content-type: application/json
+   Authorization: Bearer {{token}}
+
+   {
+       "queryType": "simple",
+       "search": "motel",
+       "filter": "",
+       "select": "HotelName,Description,Category,Tags",
+       "count": true
+   }
    ```
 
    **Reference:** [Search Documents](/rest/api/searchservice/documents/search-post)
 
    A successful query returns search results with matching documents. If the index is empty or has no matches, `value` contains an empty array.
 
-    > [!TIP]
-    > For more information on how to acquire a token for a specific environment, see [Manage an Azure AI Search service with REST APIs](search-manage-rest.md) and [Microsoft identity platform authentication libraries](/azure/active-directory/develop/reference-v2-libraries).
-    
-### [**.NET**](#tab/test-csharp)
+   > [!TIP]
+   > For more information on how to acquire a token for a specific environment, see [Manage an Azure AI Search service with REST APIs](search-manage-rest.md) and [Microsoft identity platform authentication libraries](/azure/active-directory/develop/reference-v2-libraries).
 
-1. Install the required packages:
+### [.NET](#tab/test-csharp)
+
+1. Install the required packages.
 
    ```dotnetcli
    dotnet add package Azure.Search.Documents
@@ -335,7 +551,7 @@ This approach assumes Visual Studio Code with the [REST Client extension](https:
 
 1. Use [Azure.Identity for .NET](/dotnet/api/overview/azure/identity-readme) for token authentication. Microsoft recommends [`DefaultAzureCredential()`](/dotnet/api/azure.identity.defaultazurecredential) for most scenarios.
 
-1. Here's an example of a client connection using `DefaultAzureCredential()`:
+1. Here's an example of a client connection using `DefaultAzureCredential()`.
 
     ```csharp
     // Create a SearchIndexClient to send create/delete index commands
@@ -349,14 +565,14 @@ This approach assumes Visual Studio Code with the [REST Client extension](https:
 
     **Reference:** [SearchClient](/dotnet/api/azure.search.documents.searchclient), [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient), [DefaultAzureCredential](/dotnet/api/azure.identity.defaultazurecredential)
 
-1. Here's another example of using [client secret credential](/dotnet/api/azure.core.tokencredential):
+1. Here's another example of using [client secret credential](/dotnet/api/azure.core.tokencredential).
 
     ```csharp
     var tokenCredential =  new ClientSecretCredential(aadTenantId, aadClientId, aadSecret);
     SearchClient srchclient = new SearchClient(serviceEndpoint, indexName, tokenCredential);
     ```
 
-1. Here's an example of running a query:
+1. Here's an example of running a query.
 
     ```csharp
     SearchResults<SearchDocument> response = srchclient.Search<SearchDocument>("motel");
@@ -368,9 +584,9 @@ This approach assumes Visual Studio Code with the [REST Client extension](https:
 
     A successful query returns search results. If no documents match, the results collection is empty.
 
-### [**Python**](#tab/test-python)
+### [Python](#tab/test-python)
 
-1. Install the required packages:
+1. Install the required packages.
 
    ```bash
    pip install azure-search-documents azure-identity
@@ -380,7 +596,7 @@ This approach assumes Visual Studio Code with the [REST Client extension](https:
 
 1. Use [DefaultAzureCredential](/python/api/overview/azure/identity-readme?view=azure-python#authenticate-with-defaultazurecredential&preserve-view=true) if the Python client is an application that executes server-side. Enable [interactive authentication](/python/api/overview/azure/identity-readme?view=azure-python#enable-interactive-authentication-with-defaultazurecredential&preserve-view=true) if the app runs in a browser.
 
-1. Here's an example:
+1. Here's an example.
 
     ```python
     from azure.search.documents import SearchClient
@@ -394,9 +610,9 @@ This approach assumes Visual Studio Code with the [REST Client extension](https:
 
     **Reference:** [SearchClient](/python/api/azure-search-documents/azure.search.documents.searchclient), [DefaultAzureCredential](/python/api/azure-identity/azure.identity.defaultazurecredential)
 
-### [**JavaScript**](#tab/test-javascript)
+### [JavaScript](#tab/test-javascript)
 
-1. Install the required packages:
+1. Install the required packages.
 
    ```bash
    npm install @azure/search-documents @azure/identity
@@ -408,9 +624,9 @@ This approach assumes Visual Studio Code with the [REST Client extension](https:
 
     **Reference:** [SearchClient](/javascript/api/@azure/search-documents/searchclient), [DefaultAzureCredential](/javascript/api/@azure/identity/defaultazurecredential)
 
-### [**Java**](#tab/test-java)
+### [Java](#tab/test-java)
 
-1. Add the required dependencies to your `pom.xml`:
+1. Add the required dependencies to your `pom.xml`.
 
    ```xml
    <dependency>
@@ -437,28 +653,82 @@ This approach assumes Visual Studio Code with the [REST Client extension](https:
 
 In some scenarios, you might want to limit an application's access to a single resource, such as an index.
 
-The Azure portal doesn't currently support role assignments at this level of granularity, but you can assign roles using [PowerShell](/azure/role-based-access-control/role-assignments-powershell) or the [Azure CLI](/azure/role-based-access-control/role-assignments-cli).
+### [Portal](#tab/portal)
+
+Currently, the Azure portal doesn't support role assignments at the index level. Use the Azure CLI, PowerShell, or the REST API to assign roles scoped to a single index.
 
-In PowerShell, use `New-AzRoleAssignment`, providing the Azure user or group name and the scope of the assignment.
+### [CLI](#tab/cli)
 
-1. Load the `Azure` and `AzureAD` modules and connect to your Azure account:
+1. Sign in to your Azure subscription.
+
+   ```azurecli
+   az login
+   ```
+
+1. Create a role assignment scoped to a single index. Provide the assignee and index-level scope.
+
+   ```azurecli
+   az role assignment create \
+       --assignee <assignee> \
+       --role "Search Index Data Contributor" \
+       --scope "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/indexes/<index-name>"
+   ```
+
+   **Reference:** [az role assignment create](/cli/azure/role/assignment#az-role-assignment-create)
+
+### [PowerShell](#tab/powershell)
+
+1. Import the required module and connect to your Azure account.
 
    ```powershell
-   Import-Module -Name Az
-   Import-Module -Name AzureAD
+   Import-Module Az.Resources
    Connect-AzAccount
    ```
 
-1. Add a role assignment scoped to an individual index:
+1. Create a role assignment scoped to a single index. This example uses a user sign-in name.
 
    ```powershell
-   New-AzRoleAssignment -ObjectId <objectId> `
+   New-AzRoleAssignment -SignInName <email> `
        -RoleDefinitionName "Search Index Data Contributor" `
        -Scope  "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/indexes/<index-name>"
    ```
 
    **Reference:** [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment)
 
+### [REST](#tab/rest)
+
+1. Open a command shell and sign in to your Azure subscription.
+
+   ```azurecli
+   az login
+   ```
+
+1. Get an access token for Azure Resource Manager.
+
+   ```azurecli
+   az account get-access-token --scope https://management.azure.com/.default --query accessToken --output tsv
+   ```
+
+1. Send a PUT request to create a role assignment scoped to a single index. Set `principalType` to `User`, `Group`, or `ServicePrincipal` to match the assignee.
+
+   ```http
+   PUT https://management.azure.com/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/indexes/<index-name>/providers/Microsoft.Authorization/roleAssignments/<role-assignment-guid>?api-version=2022-04-01 HTTP/1.1
+   Authorization: Bearer <access-token>
+   Content-Type: application/json
+
+   {
+       "properties": {
+           "roleDefinitionId": "/subscriptions/<subscription>/providers/Microsoft.Authorization/roleDefinitions/8ebe5a00-799e-43f5-93ac-243d3dce84a7",
+           "principalId": "<principal-object-id>",
+           "principalType": "<principal-type>"
+       }
+   }
+   ```
+
+   **Reference:** [Role Assignments - Create](/rest/api/authorization/role-assignments/create)
+
+---
+
 ### Per-index scope and indexer operations
 
 Per-index role assignments apply to direct API operations only, such as queries or document uploads from users or applications. Indexers aren't restricted by per-index permissions because they operate with service-level credentials.
@@ -477,7 +747,7 @@ If built-in roles don't provide the right combination of permissions, you can cr
 
 The following examples clone **Search Index Data Reader** and then add the ability to list indexes by name. Normally, listing the indexes on a search service is considered an administrative right.
 
-### [**Azure portal**](#tab/custom-role-portal)
+### [Portal](#tab/portal)
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and navigate to your search service.
 
@@ -502,90 +772,166 @@ The following examples clone **Search Index Data Reader** and then add the abili
 
    ```json
    {
-    "properties": {
-        "roleName": "search index data explorer",
-        "description": "",
-        "assignableScopes": [
-            "/subscriptions/0000000000000000000000000000000/resourceGroups/free-search-svc/providers/Microsoft.Search/searchServices/demo-search-svc"
-        ],
-        "permissions": [
-            {
-                "actions": [
-                    "Microsoft.Search/operations/read",
-                    "Microsoft.Search/searchServices/indexes/read"
-                ],
-                "notActions": [],
-                "dataActions": [
-                    "Microsoft.Search/searchServices/indexes/documents/read"
-                ],
-                "notDataActions": []
-            }
-        ]
-      }
-    }
-    ```
+       "properties": {
+           "roleName": "Search Index Data Explorer",
+           "description": "List all indexes on the service and query them.",
+           "assignableScopes": [
+               "/subscriptions/<subscription>/resourceGroups/<resource-group>"
+           ],
+           "permissions": [
+               {
+                   "actions": [
+                       "Microsoft.Search/operations/read",
+                       "Microsoft.Search/searchServices/indexes/read"
+                   ],
+                   "notActions": [],
+                   "dataActions": [
+                       "Microsoft.Search/searchServices/indexes/documents/read"
+                   ],
+                   "notDataActions": []
+               }
+           ]
+       }
+   }
+   ```
 
 1. Select **Add** to close the pane.
 
 1. Select **Review + create** to create the role.
 
    You can now assign users and groups to the role. For more information about these steps, see [Create or update Azure custom roles using the Azure portal](/azure/role-based-access-control/custom-roles-portal).
 
-### [**Azure PowerShell**](#tab/custom-role-ps)
+### [CLI](#tab/cli)
 
-The PowerShell example shows the JSON syntax for creating a custom role that's a clone of **Search Index Data Reader**, but with the ability to list all indexes by name.
+The Azure CLI example shows the JSON syntax for creating a custom role that's a clone of **Search Index Data Reader**, but with the ability to list all indexes by name. For step-by-step instructions on custom role creation, see [Create or update Azure custom roles using Azure CLI](/azure/role-based-access-control/custom-roles-cli).
 
 1. Review the [list of atomic permissions](/azure/role-based-access-control/resource-provider-operations#microsoftsearch) to determine which ones you need. For this example, you need the following permissions:
 
-   ```json
-   "Microsoft.Search/operations/read",
-   "Microsoft.Search/searchServices/read",
-   "Microsoft.Search/searchServices/indexes/read"
-   ```
+    ```text
+    "Microsoft.Search/operations/read",
+    "Microsoft.Search/searchServices/indexes/read",
+    "Microsoft.Search/searchServices/indexes/documents/read"
+    ```
 
-1. Set up a PowerShell session to create the custom role. For detailed instructions, see [Azure PowerShell](/azure/role-based-access-control/custom-roles-powershell).
+1. Save the following role definition to a JSON file named `search-index-data-explorer.json`. For `Id`, provide a new GUID that you generate.
 
-1. Provide the role definition as a JSON document. The following example shows the syntax for creating a custom role with PowerShell.
+    ```json
+    {
+        "Name": "Search Index Data Explorer",
+        "Id": "<role-definition-guid>",
+        "IsCustom": true,
+        "Description": "List all indexes on the service and query them.",
+        "Actions": [
+            "Microsoft.Search/operations/read",
+            "Microsoft.Search/searchServices/indexes/read"
+        ],
+        "NotActions": [],
+        "DataActions": [
+            "Microsoft.Search/searchServices/indexes/documents/read"
+        ],
+        "NotDataActions": [],
+        "AssignableScopes": [
+            "/subscriptions/<subscription>/resourceGroups/<resource-group>"
+        ]
+    }
+    ```
+
+1. Create the custom role by passing the JSON file to `az role definition create`.
+
+    ```azurecli
+    az role definition create --role-definition @search-index-data-explorer.json
+    ```
+
+    **Reference:** [az role definition create](/cli/azure/role/definition#az-role-definition-create)
+
+### [PowerShell](#tab/powershell)
+
+The PowerShell example shows the JSON syntax for creating a custom role that's a clone of **Search Index Data Reader**, but with the ability to list all indexes by name. For step-by-step instructions on custom role creation, see [Create or update Azure custom roles using Azure PowerShell](/azure/role-based-access-control/custom-roles-powershell).
+
+1. Review the [list of atomic permissions](/azure/role-based-access-control/resource-provider-operations#microsoftsearch) to determine which ones you need. For this example, you need the following permissions:
+
+    ```text
+    "Microsoft.Search/operations/read",
+    "Microsoft.Search/searchServices/indexes/read",
+    "Microsoft.Search/searchServices/indexes/documents/read"
+    ```
+
+1. Save the following role definition to a JSON file named `search-index-data-explorer.json`. For `Id`, provide a new GUID that you generate.
 
     ```json
     {
-      "Name": "Search Index Data Explorer",
-      "Id": "88888888-8888-8888-8888-888888888888",
-      "IsCustom": true,
-      "Description": "List all indexes on the service and query them.",
-      "Actions": [
-          "Microsoft.Search/operations/read",
-          "Microsoft.Search/searchServices/read"
-      ],
-      "NotActions": [],
-      "DataActions": [
-          "Microsoft.Search/searchServices/indexes/read"
-      ],
-      "NotDataActions": [],
-      "AssignableScopes": [
-        "/subscriptions/{subscriptionId1}"
-      ]
+        "Name": "Search Index Data Explorer",
+        "Id": "<role-definition-guid>",
+        "IsCustom": true,
+        "Description": "List all indexes on the service and query them.",
+        "Actions": [
+            "Microsoft.Search/operations/read",
+            "Microsoft.Search/searchServices/indexes/read"
+        ],
+        "NotActions": [],
+        "DataActions": [
+            "Microsoft.Search/searchServices/indexes/documents/read"
+        ],
+        "NotDataActions": [],
+        "AssignableScopes": [
+            "/subscriptions/<subscription>/resourceGroups/<resource-group>"
+        ]
     }
     ```
 
-    > [!NOTE]
-    > If you assign the scope at the index level, use the data action `"Microsoft.Search/searchServices/indexes/documents/read"`.
+1. Create the custom role by passing the JSON file to `New-AzRoleDefinition`.
 
-### [**REST API**](#tab/custom-role-rest)
+    ```powershell
+    New-AzRoleDefinition -InputFile "search-index-data-explorer.json"
+    ```
 
-1. Review the [list of atomic permissions](/azure/role-based-access-control/resource-provider-operations#microsoftsearch) to determine which ones you need.
+    **Reference:** [New-AzRoleDefinition](/powershell/module/az.resources/new-azroledefinition)
 
-1. See [Create or update Azure custom roles using the REST API](/azure/role-based-access-control/custom-roles-rest) for steps.
+### [REST](#tab/rest)
 
-1. Copy or create a role, or use JSON to specify the custom role (see the PowerShell tab for JSON syntax).
+The REST API example shows the JSON syntax for creating a custom role that's a clone of **Search Index Data Reader**, but with the ability to list all indexes by name. For step-by-step instructions on custom role creation, see [Create or update Azure custom roles using the REST API](/azure/role-based-access-control/custom-roles-rest).
 
-### [**Azure CLI**](#tab/custom-role-cli)
+1. Review the [list of atomic permissions](/azure/role-based-access-control/resource-provider-operations#microsoftsearch) to determine which ones you need. For this example, you need the following permissions:
 
-1. Review the [list of atomic permissions](/azure/role-based-access-control/resource-provider-operations#microsoftsearch) to determine which ones you need.
+    ```text
+    "Microsoft.Search/operations/read",
+    "Microsoft.Search/searchServices/indexes/read",
+    "Microsoft.Search/searchServices/indexes/documents/read"
+    ```
 
-1. See [Create or update Azure custom roles using Azure CLI](/azure/role-based-access-control/custom-roles-cli) for steps.
+1. Create the custom role by sending the following request to the role definition endpoint.
+
+    ```http
+    PUT https://management.azure.com/subscriptions/<subscription>/providers/Microsoft.Authorization/roleDefinitions/<role-definition-guid>?api-version=2022-04-01 HTTP/1.1
+    Authorization: Bearer <access-token>
+    Content-Type: application/json
+
+    {
+        "properties": {
+            "roleName": "Search Index Data Explorer",
+            "description": "List all indexes on the service and query them.",
+            "type": "CustomRole",
+            "permissions": [
+                {
+                    "actions": [
+                        "Microsoft.Search/operations/read",
+                        "Microsoft.Search/searchServices/indexes/read"
+                    ],
+                    "notActions": [],
+                    "dataActions": [
+                        "Microsoft.Search/searchServices/indexes/documents/read"
+                    ],
+                    "notDataActions": []
+                }
+            ],
+            "assignableScopes": [
+                "/subscriptions/<subscription>/resourceGroups/<resource-group>"
+            ]
+        }
+    }
+    ```
 
-1. See the PowerShell tab for JSON syntax.
+    **Reference:** [Role Definitions - Create Or Update](/rest/api/authorization/role-definitions/create-or-update)
 
 ---
 
@@ -603,7 +949,7 @@ To create a Conditional Access policy for Azure AI Search:
 
 1. Under **Cloud apps or actions**, add **Azure AI Search** as a cloud app, depending on how you want to set up your policy.
 
-1. Update the remaining parameters of your policy. For example, specify which users and groups to which the policy applies. 
+1. Update the remaining parameters of your policy. For example, specify which users and groups the policy applies to. 
 
 1. Save the policy.
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "RBACに関するセキュリティガイドの大幅改訂"
}
```

### Explanation
この変更は、`search-security-rbac.md`ファイルに対する大幅な改訂を反映しています。主な改訂内容は、Azure AI Searchでのロールベースのアクセス制御（RBAC）に関する情報の整理と更新です。495行の追加と149行の削除を含む内容により、全体で644か所の変更が行われました。

改訂により、Azureの各クライアントツール（Azureポータル、Azure CLI、Azure PowerShell、REST API）におけるロールの割り当て操作が明確化され、具体的な手順やコード例が詳述されています。これにより、ユーザーはテクニカルな手法を用いてよりスムーズにロールを適切に割り当てることができるようになります。また、カスタムロールの作成に関する情報も強化され、JSONの例示が追加されることで、ユーザーが何をどのように設定するかを理解しやすくしています。

このような大規模な変更によって、RBACに関するドキュメントの整合性や可用性が大幅に向上し、利用者はより一層簡潔で正確な情報を得ることができるようになっています。


