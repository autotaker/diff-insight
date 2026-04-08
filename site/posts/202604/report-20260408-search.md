---
date: '2026-04-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2d08311...MicrosoftDocs:a39b296
summary: |-
  この差分は、Azure AI Searchに関連する複数のドキュメントの更新を示しています。主な修正内容は、ロールベースのアクセス制御（RBAC）やデータプレーン関連の情報の改善です。「search-security-rbac.md」の大幅な更新が特に重要です。

  新機能としては、新しい役割の説明と、具体的なガイダンスの追加、さらには条件付きアクセスポリシーに関する情報が追加され、セキュリティが強化されました。

  破壊的変更はありません。

  そのほかの更新としては、「search-what-is-an-index.md」や「vector-store.md」における表現やリンクの微修正が行われ、全体の情報の一貫性と明瞭さが向上しています。

  全体として、この更新により、Azure AI Searchの使用がより直感的になり、開発者が適切なセキュリティ設定を容易に行えるようになっています。また、情報アクセスが向上し、ユーザーが技術的な問題に悩まされることなく業務に集中できるサポートが強化されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2d08311...MicrosoftDocs:a39b296){target="_blank"}

<format>
# ハイライト
この差分は、Azure AI Searchに関連する複数のドキュメントでの更新を表しています。主にロールベースのアクセス制御（RBAC）やデータプレーン関連の情報を改善するための修正です。「search-security-rbac.md」の大幅な更新が最も注目されます。

## 新機能
- 新しい役割の説明と、それに関連する具体的なガイダンスの追加。
- 条件付きアクセスポリシーの冒頭情報追加によりセキュリティが強化。

## 破壊的変更
- なし。

## その他の更新
- 「search-what-is-an-index.md」「vector-store.md」などにおける表現やリンクの微修正。
- ドキュメント全体の情報一貫性と明瞭さを高めるための軽微な表現改善。

# インサイト
このコードの差分は、Azure AI Searchにおけるロールベースのアクセス制御（RBAC）機能をより直感的かつ理解しやすくしようという意図が明確に表れています。特に、「search-security-rbac.md」ドキュメントの大幅な見直しと更新は、役割の管理とアクセス制御を可能な限り詳細に説明するための重要な改善です。

ドキュメントの大幅更新において注目すべきは、ユーザーに対する具体的なガイダンスの追加です。これにより、開発者はより容易に適切な役割を選択し、それに基づいたセキュリティ設定ができるようになります。また、新しい役割や割り当て方法に関するサンプルコードの追加は、実際の実装シナリオにおいて開発者の作業を円滑に進める助けとなるでしょう。

さらに、微修正が行われたドキュメントはリンクや表現の最適化に重点が置かれ、情報のアクセス性と明確さが増しています。これにより、ユーザーは必要な情報に迅速にアクセスし、Azure AI Searchにもたらされるさまざまな機能を効果的に利用できるでしょう。

全体として、この差分により、より使いやすく、開発者の学習曲線を緩和する形で、Azure AI Searchサービスの価値が向上しています。これにより、ユーザーは技術的な問題に煩わされることなく、自分たちの業務に集中できるようになります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-manage.md](#item-4043d7) | minor update | データプレーンのロールに関する情報の更新 | modified | 1 | 1 | 2 | 
| [search-query-access-control-rbac-enforcement.md](#item-d24df7) | minor update | RBACにおける役割の修正 | modified | 1 | 1 | 2 | 
| [search-security-api-keys.md](#item-d8c908) | minor update | RBACにおける役割のリンク修正 | modified | 1 | 1 | 2 | 
| [search-security-get-encryption-keys.md](#item-7aed9d) | minor update | RBACにおける役割のリンク修正 | modified | 1 | 1 | 2 | 
| [search-security-rbac-client-code.md](#item-ae3c53) | minor update | ローカル開発における役割の説明の更新 | modified | 1 | 3 | 4 | 
| [search-security-rbac.md](#item-a5d129) | major update | RBACドキュメントの大幅更新 | modified | 171 | 232 | 403 | 
| [search-what-is-an-index.md](#item-5a3344) | minor update | インデックスエンドポイントの表記の修正 | modified | 1 | 1 | 2 | 
| [vector-store.md](#item-db9b8c) | minor update | ベクターストアのエンドポイント記述の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-manage.md{#item-4043d7}

<details>
<summary>Diff</summary>
````diff
@@ -40,7 +40,7 @@ To configure role-based access:
 
 1. [Enable roles](search-security-enable-roles.md) on your search service. We recommend using both API keys and roles.
 
-1. [Assign data plane roles](search-security-rbac.md) to replace the functionality lost when you disable API keys. An owner only needs Search Index Data Reader, but developers need [more roles](search-security-rbac.md#assign-roles).
+1. [Assign data plane roles](search-security-rbac.md) to replace the functionality lost when you disable API keys. An owner only needs Search Index Data Reader, but developers need [more roles](search-security-rbac.md#assign-built-in-roles).
 
    Role assignments can take several minutes to take effect. Until then, portal pages used for data plane operations display the following message:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データプレーンのロールに関する情報の更新"
}
```

### Explanation
このコードの差分は、ドキュメント「search-manage.md」におけるデータプレーンのロールに関連する指示の軽微な修正を示しています。具体的には、以下の変更が行われました：

- 元の表現「より多くのロール」から「組み込みのロール」に表現が変更されました。これは、開発者が必要とするロールに関する具体的な情報をより明確にするための更新です。

この修正は、役割ごとのアクセス管理に関する情報の正確性を高め、ユーザーがAPIキーを無効にした際の機能損失を考慮した適切なロールの理解を促進します。全体として、この変更はドキュメントの内容の一貫性と明確さを向上させるためのものです。

## articles/search/search-query-access-control-rbac-enforcement.md{#item-d24df7}

<details>
<summary>Diff</summary>
````diff
@@ -113,7 +113,7 @@ You can accomplish these tasks by adding a custom header, `x-ms-enable-elevated-
 
 ### Permissions for elevated-read requests
 
-You must have [Search Index Data Contributor](search-security-rbac.md#built-in-roles-used-in-search) permissions or a [custom role](search-security-rbac.md#create-a-custom-role) that includes the Elevate Read permission.
+You must have [Search Index Data Contributor](search-security-rbac.md#built-in-roles) permissions or a [custom role](search-security-rbac.md#create-a-custom-role) that includes the Elevate Read permission.
 
 Queries are a data plane operation, so the custom role can only consist of atomic data plane permissions. For a custom role, add the `Microsoft.Search/searchServices/indexes/contentSecurity/elevatedOperations/read` permission.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACにおける役割の修正"
}
```

### Explanation
このコードの差分は、ドキュメント「search-query-access-control-rbac-enforcement.md」におけるRBAC（役割に基づくアクセス制御）に関する表現の軽微な修正を示しています。具体的には、次のような変更が行われました：

- 元の文では「built-in roles used in search」というフレーズが「built-in roles」に短縮されました。これにより、特定の役割に関するリンクがより簡潔な表現になります。

この修正は、RBACに関連する役割の明確性を向上させ、ユーザーが検索サービスにおける役割の理解を深めるのをサポートします。また、エレベートリード権限を含む役割の重要性が強調されています。全体として、この変更は文書の正確性を保ちながら、情報を簡潔にするためのものです。

## articles/search/search-security-api-keys.md{#item-d8c908}

<details>
<summary>Diff</summary>
````diff
@@ -323,7 +323,7 @@ After you create new keys via portal or management layer, access is restored to
 
 ## Migrate from keys to roles
 
-If you want to transition to role-based access, it's helpful to understand how keys map to [built-in roles in Azure AI Search](search-security-rbac.md#built-in-roles-used-in-search):
+If you want to transition to role-based access, it's helpful to understand how keys map to [built-in roles in Azure AI Search](search-security-rbac.md#built-in-roles):
 
 + An admin key corresponds to the **Search Service Contributor** and **Search Index Data Contributor** roles.
 + A query key corresponds to the **Search Index Data Reader** role.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACにおける役割のリンク修正"
}
```

### Explanation
このコードの差分は、ドキュメント「search-security-api-keys.md」におけるロールベースのアクセス制御（RBAC）に関連する表現の軽微な修正を反映しています。具体的な変更内容は、次の通りです：

- 「built-in roles used in search」というフレーズが「built-in roles」に短縮され、リンク先がより一般的かつ理解しやすいものになりました。

この修正により、Azure AI Searchにおける役割のマッピングに関する情報が簡潔になり、ユーザーがロールベースのアクセスの理解を深めやすくなります。全体として、この変更は情報の明確性とアクセス性を向上させるためのものです。

## articles/search/search-security-get-encryption-keys.md{#item-7aed9d}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ The **encryptionKey** construct is the same for all encrypted objects. It's a fi
 
 ## Permissions for retrieving object definitions
 
-You must have [Search Service Contributor](search-security-rbac.md#built-in-roles-used-in-search) or equivalent permissions. To use [key-based authentication](search-security-api-keys.md) instead, provide an admin API key. Admin permissions are required on requests that return object definitions and metadata. The easiest way to get the admin API key is through the Azure portal.
+You must have [Search Service Contributor](search-security-rbac.md#built-in-roles) or equivalent permissions. To use [key-based authentication](search-security-api-keys.md) instead, provide an admin API key. Admin permissions are required on requests that return object definitions and metadata. The easiest way to get the admin API key is through the Azure portal.
 
 1. Go to your search service in the [Azure portal](https://portal.azure.com).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACにおける役割のリンク修正"
}
```

### Explanation
このコードの差分は、ドキュメント「search-security-get-encryption-keys.md」における役割に関連する表現の軽微な修正を示しています。具体的には、以下の変更が行われました：

- 「built-in roles used in search」というフレーズが「built-in roles」に修正され、リファレンスがより簡潔で明確なリンクになりました。

この変更により、Azureの検索サービスでの権限についての説明がより明確になり、ユーザーがロールベースのアクセス制御を理解しやすくなります。また、関連情報へのアクセスが改善されることで、ユーザーの体験が向上します。全体として、この修正は情報の整合性と明瞭さを高めるためのものです。

## articles/search/search-security-rbac-client-code.md{#item-ae3c53}

<details>
<summary>Diff</summary>
````diff
@@ -274,8 +274,6 @@ The default authority is Azure public cloud. Custom `audience` values for sovere
 * `https://search.azure.cn` for Azure operated by 21Vianet
 * `https://search.microsoftazure.de` for Azure Germany
 
----
-
 ## Local development
 
 Local development using roles includes these steps:
@@ -289,7 +287,7 @@ Local development using roles includes these steps:
 As a local developer, your Azure identity needs full control over data plane operations. These are the suggested roles:
 
 - Search Service Contributor, create and manage objects
-- Search Index Data Contributor, load and query an index
+- Search Index Data Contributor, load and query an index and retrieve from a knowledge base
 
 Find your personal identity with one of the following tools. Use that identity as the `<identity-id>` value.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ローカル開発における役割の説明の更新"
}
```

### Explanation
このコードの差分は、ドキュメント「search-security-rbac-client-code.md」におけるローカル開発の手順に関連する内容の更新を示しています。具体的な変更は以下の通りです：

- ローカル開発に関するセクションの前から不必要な行が削除され、内容が簡潔になりました。
- 「Search Index Data Contributor」の役割の説明が更新され、インデックスの読み込みおよびクエリに加えて「知識ベースからの取得」も含まれるように修正されました。

この更新により、ユーザーはローカル開発における必要な役割とその機能についてより正確な情報を得ることができ、役割の重要性や使用方法について理解が深まります。全体として、情報の明確化と整合性を図るためのマイナーな修正です。

## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Connect Using Azure Roles
 description: Learn how to assign Azure roles in Azure AI Search to manage permissions for service administration, development, and query access with Microsoft Entra ID.
-ms.date: 03/26/2026
+ms.date: 04/06/2026
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: how-to
@@ -15,131 +15,113 @@ ai-usage: ai-assisted
 
 # Connect to Azure AI Search using roles
 
-Azure provides global authentication and [role-based access control](/azure/role-based-access-control/role-assignments-portal) through Microsoft Entra ID for all services running on the platform. In this article, learn which roles provide access to search content and administration on Azure AI Search.
+Azure AI Search supports [role-based access control](/azure/role-based-access-control/role-assignments-steps) through Microsoft Entra ID. Role-based access is optional but recommended. The alternative is [key-based authentication](search-security-api-keys.md), which is the default.
 
-In Azure AI Search, you can assign Azure roles for:
+If you assign multiple roles to a security principal, permissions are combined. Role assignments apply across all tools and client libraries. You can assign roles using any [supported approach](/azure/role-based-access-control/role-assignments-steps#step-5-assign-role).
 
-+ [Service administration](#assign-roles-for-service-administration)
-+ [Development or write-access to a search service](#assign-roles-for-development)
-+ [Read-only access for queries](#assign-roles-for-read-only-queries)
-+ [Scoped access to a single index](#grant-access-to-a-single-index)
-
-Per-user access over search results (sometimes referred to as *row-level security* or *document-level access*) is supported through permission inheritance for Azure Data Lake Storage (ADLS) Gen2 and Azure blob indexes and through security filters for all other platforms (see [Document-level access control](search-document-level-access-overview.md)).
-
-Role assignments are cumulative and pervasive across all tools and client libraries. You can assign roles by using any of the [supported approaches](/azure/role-based-access-control/role-assignments-steps) described in Azure role-based access control documentation.
-
-Role-based access is optional, but recommended. The alternative is [key-based authentication](search-security-api-keys.md), which is the default.
-
-### Quick reference: Roles by task
+This article explains how to assign built-in roles for service administration, development, and read-only query and retrieval access. It also provides steps for creating custom roles and testing role assignments.
 
-| Task | Required role(s) |
-| ---- | ---------------- |
-| Create or manage indexes, indexers, skillsets | Search Service Contributor |
-| Load documents into an index | Search Index Data Contributor |
-| Query an index | Search Index Data Reader |
-| Full development access | Search Service Contributor + Search Index Data Contributor + Search Index Data Reader |
-| Service administration | Owner or Contributor |
+> [!TIP]
+> + Want a quick overview of the built-in roles? See [Summary of permissions](#summary-of-permissions).
+> + To control access to search results at the document level, also known as row-level security, see [Document-level access control in Azure AI Search](search-document-level-access-overview.md).
 
 ## Prerequisites
 
-+ A search service in any region, on any tier, [enabled for role-based access](search-security-enable-roles.md).
++ An Azure AI Search service (any region and any tier) with [role-based access enabled](search-security-enable-roles.md).
 
-+ Owner, User Access Administrator, Role-based Access Control Administrator, or a custom role with [Microsoft.Authorization/roleAssignments/write](/azure/templates/microsoft.authorization/roleassignments) permissions.
++ Permission to assign Azure roles. Any of the following roles work:
+  + Owner
+  + User Access Administrator
+  + Role Based Access Control Administrator
+  + A custom role with [Microsoft.Authorization/roleAssignments/write](/azure/templates/microsoft.authorization/roleassignments) permissions
 
-## Built-in roles used in search
+## Built-in roles
 
-Roles are a collection of permissions on specific operations that affect either data plane or control plane layers.
+Roles are a collection of permissions that affect the control plane or data plane:
 
-*Data plane* refers to operations against the search service endpoint, such as indexing or queries, or any other operation specified in the [Search Service REST APIs](/rest/api/searchservice/) or equivalent Azure SDK client libraries. 
++ **Control plane:** Operations for service provisioning, configuration, and administration. Control plane operations include creating or deleting search services, listing API keys, and managing network and authentication settings. Available through the [Azure Resource Manager REST APIs](/rest/api/resources/), [Search Management REST APIs](/rest/api/searchmanagement/), and equivalent Azure SDK client libraries. 
 
-*Control plane* refers to Azure resource management, such as creating or configuring a search service.
++ **Data plane:** Operations against the search service endpoint. Data plane operations fall into two categories: object management and content access. Available through the [Search Service REST APIs](/rest/api/searchservice/) and equivalent Azure SDK client libraries. 
 
-The following roles are built in. If these roles don't meet your needs, [create a custom role](#create-a-custom-role). 
+### Role descriptions
 
-| Role | Plane | Description  |
-| ---- | ------|--------------------- |
-| [Owner](/azure/role-based-access-control/built-in-roles#owner) | Control & Data | Full access to the control plane of the search resource, including the ability to assign Azure roles. Only the Owner role can enable or disable authentication options or manage roles for other users. Subscription administrators are members by default. </br></br>On the data plane, this role has the same access as the Search Service Contributor role. It includes access to all data plane actions except the ability to query documents.|
-| [Contributor](/azure/role-based-access-control/built-in-roles#contributor) | Control & Data |  Same level of control plane access as Owner, minus the ability to assign roles or change authentication options. </br></br>On the data plane, this role has the same access as the Search Service Contributor role. It includes access to all data plane actions except the ability to query or index documents.|
-| [Reader](/azure/role-based-access-control/built-in-roles#reader) | Control & Data | Read access across the entire service, including search metrics, content metrics (storage consumed, number of objects), and the object definitions of data plane resources (indexes, indexers, and so on). However, it can't read API keys or read content within indexes. |
-| [Search Service Contributor](/azure/role-based-access-control/built-in-roles#search-service-contributor) | Control & Data | Read-write access to object definitions (indexes, aliases, synonym maps, indexers, data sources, and skillsets). This role is for developers who create objects, and for administrators who manage a search service and its objects, but without access to index content. Use this role to create, delete, and list indexes, get index definitions, get service information (statistics and quotas), test analyzers, create and manage synonym maps, indexers, data sources, and skillsets. See [`Microsoft.Search/searchServices/*`](/azure/role-based-access-control/resource-provider-operations#microsoftsearch) for the permissions list. |
-| [Search Index Data Contributor](/azure/role-based-access-control/built-in-roles#search-index-data-contributor) | Data | Read-write access to content in indexes. This role is for developers or index owners who need to import, refresh, or query the documents collection of an index. This role doesn't support index creation, updates, or deletion. By default, this role applies to all indexes on a search service. See [Grant access to a single index](#grant-access-to-a-single-index) to narrow the scope.  |
-| [Search Index Data Reader](/azure/role-based-access-control/built-in-roles#search-index-data-reader) | Data |  Read-only access for querying search indexes. This role is for apps and users who run queries. This role doesn't support read access to object definitions. For example, you can't read a search index definition or get search service statistics. By default, this role is for all indexes on a search service. See [Grant access to a single index](#grant-access-to-a-single-index) to narrow the scope.  |
+The following built-in roles grant permissions to Azure AI Search. Control plane roles are always available, while data plane roles require [role-based access to be enabled](search-security-enable-roles.md) on your search service. You can combine built-in roles for broader access or [create a custom role](#create-a-custom-role) with the specific permissions you need.
 
-Combine these roles to get sufficient permissions for your use case.
+| Role | Plane | Description |
+| -- | -- | -- |
+| [Owner](/azure/role-based-access-control/built-in-roles#owner) | Control | <ul><li>Full control plane access, including the ability to assign roles and change authentication settings.</li><li>Subscription administrators have this role by default.</li><li>Can manage API keys.</li><li>Can't create search objects, load documents, query indexes, or retrieve from knowledge bases.</li></ul> |
+| [Contributor](/azure/role-based-access-control/built-in-roles#contributor) | Control | <ul><li>Same level of control plane access as Owner, minus the ability to assign roles.</li></ul> |
+| [Reader](/azure/role-based-access-control/built-in-roles#reader) | Control | <ul><li>Read-only control plane access.</li><li>Can view service metrics and object definitions.</li><li>Can't view or manage API keys, load documents, query indexes, or retrieve from knowledge bases.</li></ul> |
+| [Search Service Contributor](/azure/role-based-access-control/built-in-roles#search-service-contributor) | Control & Data | <ul><li>Full control plane access. Data plane access is limited to object management.</li><li>Can create indexes, indexers, skillsets, knowledge bases, and other search objects.</li><li>Can't load documents, query indexes, or retrieve from knowledge bases.</li><li>For the full permissions list, see [`Microsoft.Search/searchServices/*`](/azure/role-based-access-control/permissions/ai-machine-learning#microsoftsearch).</li></ul> |
+| [Search Index Data Contributor](/azure/role-based-access-control/built-in-roles#search-index-data-contributor) | Data | <ul><li>Read-write content access.</li><li>Can load documents, query indexes, and retrieve from knowledge bases.</li><li>Can't modify object definitions or retrieve admin keys.</li></ul> |
+| [Search Index Data Reader](/azure/role-based-access-control/built-in-roles#search-index-data-reader) | Data | <ul><li>Read-only content access.</li><li>Can query indexes and retrieve from knowledge bases.</li><li>Can't load documents, modify object definitions, or retrieve admin keys.</li></ul> |
 
-> [!NOTE]
-> If you disable Azure role-based access, built-in roles for the control plane (Owner, Contributor, Reader) continue to be available. Disabling role-based access removes just the data-related permissions associated with those roles. If you disable data plane roles, Search Service Contributor is equivalent to control-plane Contributor.
+> [!IMPORTANT]
+> + Owner, Contributor, and Search Service Contributor can retrieve admin keys, which provide full read-write access to the data plane. Only grant these roles to trusted users.
+> + By default, data plane roles apply to all indexes on the search service. To scope Search Index Data Contributor or Search Index Data Reader to a single index, see [Grant access to a single index](#grant-access-to-a-single-index).
 
-## Summary of permissions
+### Summary of permissions
 
-| Permissions | Search Index Data Reader | Search Index Data Contributor | Search Service Contributor | Owner/Contributor | Reader |
-|-------------|--------------------------|-------------------------------|----------------------------|-------------------|--------|
-|View the resource in Azure portal |❌|❌|✅|✅|✅|
-|View resource properties, metrics, and endpoint |❌|❌|✅|✅|✅|
-|List all objects on the resource |❌|❌|✅|✅|✅|
-|Access quotas and service statistics |❌|❌|✅|✅|❌|
-|Read and query an index |✅|✅|❌|❌|❌|
-|Upload data for indexing <sup>1</sup>|❌|✅|❌|❌|❌|
-|Elevated read regardless of permission filters <sup>2</sup>|❌|✅|❌|❌|❌|
-|Create or edit indexes and aliases |❌|❌|✅|✅|❌|
-|Create, edit, and run indexers, data sources, and skillsets |❌|❌|✅|✅|❌|
-|Create or edit synonym maps |❌|❌|✅|✅|❌|
-|Create or edit debug sessions |❌|❌|✅|✅|❌|
-|Create or manage deployments |❌|❌|✅|✅|❌|
-|Create or configure Azure AI Search resources |❌|❌|✅|✅|❌|
-|View, copy, and regenerate keys under Keys |❌|❌|✅|✅|❌|
-|View roles, policies, and definitions |❌|❌|✅|✅|❌|
-|Set authentication options |❌|❌|✅|✅|❌|
-|Configure private connections |❌|❌|✅|✅|❌|
-|Configure network security |❌|❌|✅|✅|❌|
+Use the following table to quickly find which role provides the permissions you need.
 
-<sup>1</sup> An Owner or Contributor can run the [**Import data** wizard](search-import-data-portal.md) to create and load indexes, even though they can't upload documents in other clients. Similarly, [indexers](search-indexer-overview.md) can write to any index on the search service, regardless of per-index role assignments. In both cases, the search service (not the user) performs the data plane actions using its `Microsoft.Search/searchServices/indexes/documents/*` permissions.
+| Permissions | Owner/Contributor | Reader | Search Service Contributor | Search Index Data Contributor | Search Index Data Reader |
+| -- | -- | -- | -- | -- | -- |
+| Create and configure Azure AI Search services | ✅ | ❌ | ✅ | ❌ | ❌ |
+| Access service in the Azure portal | ✅ | ✅ | ✅ | ❌ | ❌ |
+| View service properties, metrics, and endpoint | ✅ | ✅ | ✅ | ❌ | ❌ |
+| List all objects on the service | ✅ | ✅ | ✅ | ❌ | ❌ |
+| Access quotas and service statistics | ✅ | ❌ | ✅ | ❌ | ❌ |
+| View, copy, and regenerate keys | ✅ | ❌ | ✅ | ❌ | ❌ |
+| Set authentication options | ✅ | ❌ | ✅ | ❌ | ❌ |
+| View roles, policies, and definitions | ✅ | ✅ | ✅ | ❌ | ❌ |
+| Configure network security and private connections | ✅ | ❌ | ✅ | ❌ | ❌ |
+| Create, run, and manage search objects <sup>1</sup> | ❌ | ❌ | ✅ | ❌ | ❌ |
+| Upload data for indexing <sup>2</sup> | ❌ | ❌ | ❌ | ✅ | ❌ |
+| Query an index | ❌ | ❌ | ❌ | ✅ | ✅ |
+| Retrieve from a knowledge base | ❌ | ❌ | ❌ | ✅ | ✅ |
+| Bypass permission filters with [elevated read](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results) | ❌ | ❌ | ❌ | ✅ | ❌ |
 
-<sup>2</sup> Use elevated read for debugging queries that obtain results by using the identity of the called. For more information, see [Investigate incorrect query results](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results).
+<sup>1</sup> Includes indexes, indexers, data sources, skillsets, aliases, synonym maps, debug sessions, knowledge bases, and knowledge sources. Indexers also support run and reset operations.
 
-Owners and Contributors grant the same permissions, except that only Owners can assign roles.
+<sup>2</sup> An Owner or Contributor can run the [**Import data** wizard](search-import-data-portal.md) to create and load indexes, even though they can't upload documents in other clients. Similarly, indexers can write to any index on the search service, regardless of [per-index role assignments](#per-index-scope-and-indexer-operations). In both cases, the search service (not the user) performs the data plane actions using its `Microsoft.Search/searchServices/indexes/documents/*` permissions.
 
-## Assign roles
+## Assign built-in roles
 
-In this section, assign roles for:
+In this section, you assign roles for:
 
-+ Service administration
-+ Development or write access to a search service
-+ Read-only access for queries
++ [Service administration](#assign-roles-for-service-administration)
++ [Development](#assign-roles-for-development)
++ [Read-only access](#assign-roles-for-read-only-access)
 
 ### Assign roles for service administration
 
-As a service administrator, you can create and configure a search service, and perform all control plane operations described in the [Management REST API](/rest/api/searchmanagement/) or equivalent client libraries. If you're an Owner or Contributor, you can also perform most data plane [Search REST API](/rest/api/searchservice/) tasks in the Azure portal.
+The following roles let you create, configure, and manage a search service. These roles are hierarchical, so select one based on the access level you need.
 
-| Role | ID|
-| --- | --- |
-|[`Owner`](/azure/role-based-access-control/built-in-roles#owner) |8e3af657-a8ff-443c-a75c-2fe8c4bcb635|
-|[`Contributor`](/azure/role-based-access-control/built-in-roles#contributor)|b24988ac-6180-42a0-ab88-20f7382dd24c|
-|[`Reader`](/azure/role-based-access-control/built-in-roles#reader)|acdd72a7-3385-48ef-bd42-f606fba81ae7|
+| Role | ID |
+| -- | -- |
+| [Owner](#role-descriptions) | 8e3af657-a8ff-443c-a75c-2fe8c4bcb635 |
+| [Contributor](#role-descriptions) | b24988ac-6180-42a0-ab88-20f7382dd24c |
+| [Reader](#role-descriptions) | acdd72a7-3385-48ef-bd42-f606fba81ae7 |
 
 #### [**Azure portal**](#tab/roles-portal-admin)
 
 1. Go to your search service in the [Azure portal](https://portal.azure.com).
 
-1. Select **Access Control (IAM)** in the left pane.
-
-1. Select **+ Add** > **Add role assignment** to start the **Add role assignment** wizard.
+1. From the left pane, select **Access control (IAM)**.
 
-   :::image type="content" source="media/search-security-rbac/portal-access-control.png" alt-text="Screenshot of the access control page in the Azure portal.":::
+1. Select **+ Add** > **Add role assignment**.
 
-1. Select a role.
+   :::image type="content" source="media/search-security-rbac/portal-access-control.png" alt-text="Screenshot of the Access control (IAM) page for assigning service administration roles.":::
 
-   + Owner (full access to all data plane and control plane operations, except for query permissions)
-   + Contributor (same as Owner, except for permissions to assign roles)
-   + Reader (acceptable for monitoring and viewing metrics)
+1. Select a role: **Owner**, **Contributor**, or **Reader**.
 
-1. On the **Members** tab, select the Microsoft Entra user or group identity. If you're setting up permissions for another Azure service, select a system or user-managed identity.
+1. On the **Members** tab, select the Microsoft Entra user or group identity. If you're setting up permissions for another Azure service, select a system-assigned or user-assigned managed identity.
 
 1. On the **Review + assign** tab, select **Review + assign** to assign the role.
 
 #### [**PowerShell**](#tab/roles-powershell-admin)
 
-When you [use PowerShell to assign roles](/azure/role-based-access-control/role-assignments-powershell), call [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment), providing the Azure user or group name, and the scope of the assignment.
+When you [assign roles using PowerShell](/azure/role-based-access-control/role-assignments-powershell), call `New-AzRoleAssignment`, providing the Azure user or group name and the scope of the assignment.
 
 This example creates a role assignment scoped to a search service:
 
@@ -155,42 +137,35 @@ New-AzRoleAssignment -SignInName <email> `
 
 ### Assign roles for development
 
-Role assignments apply globally across the search service. To [scope permissions to a single index](#rbac-single-index), use PowerShell or the Azure CLI to create a custom role.
+The following roles let you create search objects, load documents, query indexes, and retrieve from knowledge bases. Assign all three roles to cover the full range of development tasks.
 
-| Task | Role | ID |
-| --- | --- | --- |
-| Create or manage objects | [`Search Service Contributor`](/azure/role-based-access-control/built-in-roles#search-service-contributor) | 7ca78c08-252a-4471-8644-bb5ff32d4ba0 |
-| Load documents, run indexing jobs | [`Search Index Data Contributor`](/azure/role-based-access-control/built-in-roles#search-index-data-contributor) | 8ebe5a00-799e-43f5-93ac-243d3dce84a7 |
-| Query an index | [`Search Index Data Reader`](/azure/role-based-access-control/built-in-roles#search-index-data-reader) | 1407120a-92aa-4202-b7e9-c0e197c71c8f |
-
-Another combination of roles that provides full access is Contributor or Owner, plus Search Index Data Reader.
-
-> [!IMPORTANT]
-> If you configure role-based access for a service or index and you also provide an API key on the request, the search service uses the API key to authenticate.
+| Role | ID |
+| -- | -- |
+| [Search Service Contributor](#role-descriptions) | 7ca78c08-252a-4471-8644-bb5ff32d4ba0 |
+| [Search Index Data Contributor](#role-descriptions) | 8ebe5a00-799e-43f5-93ac-243d3dce84a7 |
+| [Search Index Data Reader](#role-descriptions) | 1407120a-92aa-4202-b7e9-c0e197c71c8f |
 
 #### [**Azure portal**](#tab/roles-portal)
 
 1. Go to your search service in the [Azure portal](https://portal.azure.com).
 
-1. Select **Access Control (IAM)** in the left pane.
+1. From the left pane, select **Access control (IAM)**.
 
-1. Select **+ Add** > **Add role assignment** to start the **Add role assignment** wizard.
+1. Select **+ Add** > **Add role assignment**.
 
-   :::image type="content" source="media/search-security-rbac/portal-access-control.png" alt-text="Screenshot of the access control page in the Azure portal.":::
+   :::image type="content" source="media/search-security-rbac/portal-access-control.png" alt-text="Screenshot of the Access control (IAM) page for assigning development roles.":::
 
-1. Select a role.
+1. Select **Search Service Contributor**.
 
-   + Search Service Contributor (create, read, update, and delete operations on indexes, indexers, skillsets, and other top-level objects)
-   + Search Index Data Contributor (load documents and run indexing jobs)
-   + Search Index Data Reader (query an index)
-
-1. On the **Members** tab, select the Microsoft Entra user or group identity. If you're setting up permissions for another Azure service, select a system or user-managed identity.
+1. On the **Members** tab, select the Microsoft Entra user or group identity. If you're setting up permissions for another Azure service, select a system-assigned or user-assigned managed identity.
 
 1. On the **Review + assign** tab, select **Review + assign** to assign the role.
 
+1. Repeat these steps to assign **Search Index Data Contributor** and **Search Index Data Reader**.
+
 #### [**PowerShell**](#tab/roles-powershell)
 
-When you [use PowerShell to assign roles](/azure/role-based-access-control/role-assignments-powershell), call [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment), providing the Azure user or group name, and the scope of the assignment.
+When you [assign roles using PowerShell](/azure/role-based-access-control/role-assignments-powershell), call `New-AzRoleAssignment`, providing the Azure user or group name and the scope of the assignment.
 
 This example creates a role assignment scoped to a search service:
 
@@ -212,40 +187,33 @@ New-AzRoleAssignment -SignInName <email> `
 
 ---
 
-### Assign roles for read-only queries
+### Assign roles for read-only access
 
-Use the Search Index Data Reader role for apps and processes that only need read access to an index.
+Use the following role for apps and processes that only need read access to indexes and knowledge bases. Supported operations include [search](/rest/api/searchservice/documents/search-post), [lookup](/rest/api/searchservice/documents/get), [autocomplete](/rest/api/searchservice/documents/autocomplete-post), and [suggestions](/rest/api/searchservice/documents/suggest-post) for indexes and [retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve) for knowledge bases.
 
-| Role | ID|
-| --- | --- |
-| [`Search Index Data Reader`](/azure/role-based-access-control/built-in-roles#search-index-data-reader) [with PowerShell](search-security-rbac.md#grant-access-to-a-single-index)|1407120a-92aa-4202-b7e9-c0e197c71c8f|
-
-This role is very specific. It grants [GET or POST access](/rest/api/searchservice/documents) to the *documents collection of a search index* for search, autocomplete, and suggestions. It doesn't support GET or LIST operations on an index or other top-level objects, or GET service statistics.
-
-This section provides basic steps for setting up the role assignment and is here for completeness, but for comprehensive instructions on configuring your app for role-based access, see [Use Azure AI Search without keys](search-security-rbac-client-code.md).
-
-> [!NOTE]
-> As a developer, if you need to debug queries that are predicated on a Microsoft identity, use Search Index Data Contributor or create a custom role that gives you [elevated permissions for debug purposes](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results).
+| Role | ID |
+| -- | -- |
+| [Search Index Data Reader](#role-descriptions) | 1407120a-92aa-4202-b7e9-c0e197c71c8f |
 
 #### [**Azure portal**](#tab/roles-portal-query)
 
 1. Go to your search service in the [Azure portal](https://portal.azure.com).
 
-1. Select **Access Control (IAM)** in the left pane.
+1. From the left pane, select **Access control (IAM)**.
 
-1. Select **+ Add** > **Add role assignment** to start the **Add role assignment** wizard.
+1. Select **+ Add** > **Add role assignment**.
 
-   :::image type="content" source="media/search-security-rbac/portal-access-control.png" alt-text="Screenshot of the access control page in the Azure portal.":::
+   :::image type="content" source="media/search-security-rbac/portal-access-control.png" alt-text="Screenshot of the Access control (IAM) page for assigning read-only data access roles.":::
 
 1. Select the **Search Index Data Reader** role.
 
-1. On the **Members** tab, select the Microsoft Entra user or group identity. If you're setting up permissions for another Azure service, select a system or user-managed identity.
+1. On the **Members** tab, select the Microsoft Entra user or group identity. If you're setting up permissions for another Azure service, select a system-assigned or user-assigned managed identity.
 
 1. On the **Review + assign** tab, select **Review + assign** to assign the role.
 
 #### [**PowerShell**](#tab/roles-powershell-query)
 
-When [using PowerShell to assign roles](/azure/role-based-access-control/role-assignments-powershell), call [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment), providing the Azure user or group name, and the scope of the assignment.
+When you [assign roles using PowerShell](/azure/role-based-access-control/role-assignments-powershell), call `New-AzRoleAssignment`, providing the Azure user or group name and the scope of the assignment.
 
 1. Get your subscription ID, search service resource group, and search service name.
 
@@ -287,23 +255,23 @@ When [using PowerShell to assign roles](/azure/role-based-access-control/role-as
 
 Use a client to test role assignments. Remember that roles are cumulative. You can't delete or deny inherited roles that are scoped to the subscription or resource group level at the resource (search service) level. 
 
-[Configure your application for keyless connections](search-security-rbac-client-code.md) and have role assignments in place before testing. 
+Before you proceed, [configure your application for keyless connections](search-security-rbac-client-code.md) and have role assignments in place.
 
 ### [**Azure portal**](#tab/test-portal)
 
 1. Go to your search service in the [Azure portal](https://portal.azure.com).
 
-1. On the Overview page, select the **Indexes** tab:
+1. From the left pane, select **Search management** > **Indexes** to test index-related permissions:
 
-   + Search Service Contributors can view and create any object, but can't load documents or query an index. To verify permissions, [create a search index](search-how-to-create-search-index.md#create-an-index).
+   + Search Service Contributors can create, modify, and delete search objects but can't load documents or run queries. To verify permissions, [create a search index](search-how-to-create-search-index.md#create-an-index).
 
    + Search Index Data Contributors can load documents. There's no load documents option in the Azure portal outside of the [**Import data** wizard](search-import-data-portal.md), but you can [reset and run an indexer](search-howto-run-reset-indexers.md) to confirm document load permissions.
 
-   + Search Index Data Readers can query the index. To verify permissions, use [Search explorer](search-explorer.md). You should be able to send queries and view results, but you shouldn't be able to view the index definition or create one.
+   + Search Index Data Readers can query indexes. To verify permissions, use [Search explorer](search-explorer.md). You should be able to send queries and view results, but you shouldn't be able to view index definitions or create indexes.
 
 ### [**REST API**](#tab/test-rest)
 
-This approach assumes Visual Studio Code with a [REST client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
+This approach assumes Visual Studio Code with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
 1. Open a command shell for Azure CLI and sign in to your Azure subscription.
 
@@ -317,10 +285,10 @@ This approach assumes Visual Studio Code with a [REST client extension](https://
    az account show
    ```
 
-1. Get an access token.
+1. Get an access token for the Azure AI Search data plane.
 
    ```azurecli
-   az account get-access-token --query accessToken --output tsv
+   az account get-access-token --scope https://search.azure.com/.default --query accessToken --output tsv
    ```
 
 1. Paste these variables in a new text file in Visual Studio Code.
@@ -331,7 +299,7 @@ This approach assumes Visual Studio Code with a [REST client extension](https://
    @token = PASTE-YOUR-TOKEN-HERE
    ```
 
-1. Paste and then send a request that uses the variables you specify. For the "Search Index Data Reader" role, you can send a query. You can use any [supported API version](/rest/api/searchservice/search-service-api-versions).
+1. Send a request that uses the variables you specify. For the Search Index Data Reader role, you can send a query using any [supported API version](/rest/api/searchservice/search-service-api-versions).
 
    ```http
    POST https://{{baseUrl}}/indexes/{{index-name}}/docs/search?api-version=2025-09-01 HTTP/1.1
@@ -347,13 +315,13 @@ This approach assumes Visual Studio Code with a [REST client extension](https://
         }
    ```
 
-   A successful query returns search results with matching documents. If the index is empty or has no matches, `value` contains an empty array.
-
    **Reference:** [Search Documents](/rest/api/searchservice/documents/search-post)
 
-> [!TIP]
-> For more information on how to acquire a token for a specific environment, see [Manage a Azure AI Search service with REST APIs](search-manage-rest.md) and [Microsoft identity platform authentication libraries](/azure/active-directory/develop/reference-v2-libraries).
+   A successful query returns search results with matching documents. If the index is empty or has no matches, `value` contains an empty array.
 
+    > [!TIP]
+    > For more information on how to acquire a token for a specific environment, see [Manage an Azure AI Search service with REST APIs](search-manage-rest.md) and [Microsoft identity platform authentication libraries](/azure/active-directory/develop/reference-v2-libraries).
+    
 ### [**.NET**](#tab/test-csharp)
 
 1. Install the required packages:
@@ -434,7 +402,9 @@ This approach assumes Visual Studio Code with a [REST client extension](https://
 
 1. Use [Azure.Identity for JavaScript](/javascript/api/overview/azure/identity-readme) for token authentication.
 
-1. If you're using React, use `InteractiveBrowserCredential` for Microsoft Entra authentication to Search. See [When to use `@azure/identity`](/javascript/api/overview/azure/identity-readme?view=azure-node-latest#when-to-use&preserve-view=true) for details.
+1. If you're using React, use `InteractiveBrowserCredential` for Microsoft Entra authentication to Azure AI Search. For more information, see [When to use `@azure/identity`](/javascript/api/overview/azure/identity-readme?view=azure-node-latest#when-to-use&preserve-view=true).
+
+    **Reference:** [SearchClient](/javascript/api/@azure/search-documents/searchclient), [DefaultAzureCredential](/javascript/api/@azure/identity/defaultazurecredential)
 
 ### [**Java**](#tab/test-java)
 
@@ -444,12 +414,12 @@ This approach assumes Visual Studio Code with a [REST client extension](https://
    <dependency>
      <groupId>com.azure</groupId>
      <artifactId>azure-search-documents</artifactId>
-     <version>11.6.0</version>
+     <version>11.7.4</version>
    </dependency>
    <dependency>
      <groupId>com.azure</groupId>
      <artifactId>azure-identity</artifactId>
-     <version>1.10.0</version>
+     <version>1.15.0</version>
    </dependency>
    ```
 
@@ -459,46 +429,6 @@ This approach assumes Visual Studio Code with a [REST client extension](https://
 
 ---
 
-## Test as current user
-
-If you're already a Contributor or Owner of your search service, you can use a bearer token for your user identity to authenticate to Azure AI Search.
-
-1. Get a bearer token for the current user by using the Azure CLI:
-
-    ```azurecli
-    az account get-access-token --scope https://search.azure.com/.default
-    ```
-
-   Or use PowerShell:
-
-   ```powershell
-   Get-AzAccessToken -ResourceUrl https://search.azure.com
-   ```
-
-1. Paste these variables into a new text file in Visual Studio Code.
-
-   ```http
-   @baseUrl = PASTE-YOUR-SEARCH-SERVICE-URL-HERE
-   @index-name = PASTE-YOUR-INDEX-NAME-HERE
-   @token = PASTE-YOUR-TOKEN-HERE
-   ```
-
-1. Paste in and then send a request to confirm access. Here's one that queries the hotels-quickstart index.
-
-   ```http
-   POST https://{{baseUrl}}/indexes/{{index-name}}/docs/search?api-version=2025-09-01 HTTP/1.1
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
-   ```
-
 <a name="rbac-single-index"></a>
 
 ## Grant access to a single index
@@ -507,7 +437,7 @@ In some scenarios, you might want to limit an application's access to a single r
 
 The Azure portal doesn't currently support role assignments at this level of granularity, but you can assign roles using [PowerShell](/azure/role-based-access-control/role-assignments-powershell) or the [Azure CLI](/azure/role-based-access-control/role-assignments-cli).
 
-In PowerShell, use [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment), providing the Azure user or group name, and the scope of the assignment.
+In PowerShell, use `New-AzRoleAssignment`, providing the Azure user or group name and the scope of the assignment.
 
 1. Load the `Azure` and `AzureAD` modules and connect to your Azure account:
 
@@ -525,6 +455,8 @@ In PowerShell, use [New-AzRoleAssignment](/powershell/module/az.resources/new-az
        -Scope  "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/indexes/<index-name>"
    ```
 
+   **Reference:** [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment)
+
 ### Per-index scope and indexer operations
 
 Per-index role assignments apply to direct API operations only, such as queries or document uploads from users or applications. Indexers aren't restricted by per-index permissions because they operate with service-level credentials.
@@ -539,36 +471,30 @@ For strict data isolation between indexes, consider these approaches:
 
 ## Create a custom role
 
-If [built-in roles](#built-in-roles-used-in-search) don't provide the right combination of permissions, you can create a [custom role](/azure/role-based-access-control/custom-roles) to support the operations you require.
+If built-in roles don't provide the right combination of permissions, you can create a [custom role](/azure/role-based-access-control/custom-roles) to support the operations you require.
 
-This example clones **Search Index Data Reader** and then adds the ability to list indexes by name. Normally, listing the indexes on a search service is considered an administrative right.
+The following examples clone **Search Index Data Reader** and then add the ability to list indexes by name. Normally, listing the indexes on a search service is considered an administrative right.
 
 ### [**Azure portal**](#tab/custom-role-portal)
 
-These steps are derived from [Create or update Azure custom roles using the Azure portal](/azure/role-based-access-control/custom-roles-portal). A search service page supports cloning from an existing role.
-
-These steps create a custom role that augments search query rights to include listing indexes by name. Typically, listing indexes is considered an admin function.
-
-1. In the Azure portal, go to your search service.
-
-1. In the left-navigation pane, select **Access Control (IAM)**.
+1. Sign in to the [Azure portal](https://portal.azure.com) and navigate to your search service.
 
-1. In the action bar, select **Roles**.
+1. From the left pane, select **Access control (IAM)**.
 
-1. Right-click **Search Index Data Reader** (or another role) and select **Clone** to open the **Create a custom role** wizard.
+1. On the **Roles** tab, find **Search Index Data Reader** or another role, select the ellipsis (...), and then select **Clone**.
 
-1. On the Basics tab, provide a name for the custom role, such as "Search Index Data Explorer", and then select **Next**.
+1. On the **Basics** tab, enter a name for the custom role, such as "Search Index Data Explorer", and then select **Next**.
 
-1. On the Permissions tab, select **Add permission**.
+1. On the **Permissions** tab, select **Add permissions**.
 
-1. On the Add permissions tab, search for and then select the **Microsoft Search** tile.
+1. In the **Add permissions** pane, select the **Microsoft Search** tile.
 
-1. Set the permissions for your custom role. At the top of the page, use the default **Actions** selection:
+1. With **Actions** selected at the top, set the following permissions:
 
-   + Under Microsoft.Search/operations, select **Read : List all available operations**. 
-   + Under Microsoft.Search/searchServices/indexes, select **Read : Read Index**.
+   + Under `Microsoft.Search/operations`, select **Read : List all available operations**. 
+   + Under `Microsoft.Search/searchServices/indexes`, select **Read : Read Index**.
 
-1. On the same page, switch to **Data actions** and under Microsoft.Search/searchServices/indexes/documents, select **Read : Read Documents**.
+1. Switch to **Data Actions** at the top, and under `Microsoft.Search/searchServices/indexes/documents`, select **Read : Read Documents**.
 
    The JSON definition looks like the following example:
 
@@ -597,7 +523,11 @@ These steps create a custom role that augments search query rights to include li
     }
     ```
 
-1. Select **Review + create** to create the role. You can now assign users and groups to the role.
+1. Select **Add** to close the pane.
+
+1. Select **Review + create** to create the role.
+
+   You can now assign users and groups to the role. For more information about these steps, see [Create or update Azure custom roles using the Azure portal](/azure/role-based-access-control/custom-roles-portal).
 
 ### [**Azure PowerShell**](#tab/custom-role-ps)
 
@@ -615,29 +545,29 @@ The PowerShell example shows the JSON syntax for creating a custom role that's a
 
 1. Provide the role definition as a JSON document. The following example shows the syntax for creating a custom role with PowerShell.
 
-```json
-{
-  "Name": "Search Index Data Explorer",
-  "Id": "88888888-8888-8888-8888-888888888888",
-  "IsCustom": true,
-  "Description": "List all indexes on the service and query them.",
-  "Actions": [
-      "Microsoft.Search/operations/read",
-      "Microsoft.Search/searchServices/read"
-  ],
-  "NotActions": [],
-  "DataActions": [
-      "Microsoft.Search/searchServices/indexes/read"
-  ],
-  "NotDataActions": [],
-  "AssignableScopes": [
-    "/subscriptions/{subscriptionId1}"
-  ]
-}
-```
+    ```json
+    {
+      "Name": "Search Index Data Explorer",
+      "Id": "88888888-8888-8888-8888-888888888888",
+      "IsCustom": true,
+      "Description": "List all indexes on the service and query them.",
+      "Actions": [
+          "Microsoft.Search/operations/read",
+          "Microsoft.Search/searchServices/read"
+      ],
+      "NotActions": [],
+      "DataActions": [
+          "Microsoft.Search/searchServices/indexes/read"
+      ],
+      "NotDataActions": [],
+      "AssignableScopes": [
+        "/subscriptions/{subscriptionId1}"
+      ]
+    }
+    ```
 
-> [!NOTE]
-> If you assign the scope at the index level, use the data action `"Microsoft.Search/searchServices/indexes/documents/read"`.
+    > [!NOTE]
+    > If you assign the scope at the index level, use the data action `"Microsoft.Search/searchServices/indexes/documents/read"`.
 
 ### [**REST API**](#tab/custom-role-rest)
 
@@ -657,33 +587,42 @@ The PowerShell example shows the JSON syntax for creating a custom role that's a
 
 ---
 
-## Conditional Access
+## Create a Conditional Access policy
 
 If you need to enforce organizational policies, such as multifactor authentication, use [Microsoft Entra Conditional Access](/entra/identity/conditional-access/overview).
 
-To enable a Conditional Access policy for Azure AI Search, follow these steps:
+To create a Conditional Access policy for Azure AI Search:
 
-1. [Sign in](https://portal.azure.com) to the Azure portal.
+1. Sign in to the [Azure portal](https://portal.azure.com).
 
 1. Search for **Microsoft Entra Conditional Access**.
 
-1. Select **Policies**.
+1. On the **Overview** page, select **Create new policy**.
 
-1. Select **New policy**.
+1. Under **Cloud apps or actions**, add **Azure AI Search** as a cloud app, depending on how you want to set up your policy.
 
-1. In the **Cloud apps or actions** section of the policy, add **Azure AI Search** as a cloud app depending on how you want to set up your policy.
-
-1. Update the remaining parameters of the policy. For example, specify which users and groups this policy applies to. 
+1. Update the remaining parameters of your policy. For example, specify which users and groups to which the policy applies. 
 
 1. Save the policy.
 
 > [!IMPORTANT]
-> If your search service has a managed identity assigned to it, the specific search service shows up as a cloud app that you can include or exclude as part of the Conditional Access policy. You can't enforce Conditional Access policies on a specific search service. Instead, make sure you select the general **Azure AI Search** cloud app.
+> If your search service has a managed identity assigned to it, the specific search service appears as a cloud app. However, selecting that specific search service doesn't enforce the policy. Instead, select the general **Azure AI Search** cloud app to apply Conditional Access policies to your search service.
 
-## Troubleshooting role-based access control issues
+## Troubleshooting
 
 When you develop applications that use role-based access control for authentication, you might encounter some common problems:
 
-+ If the authorization token comes from a [managed identity](/entra/identity/managed-identities-azure-resources/overview) and you recently assigned the appropriate permissions, it [might take several hours](/entra/identity/managed-identities-azure-resources/managed-identity-best-practice-recommendations#limitation-of-using-managed-identities-for-authorization) for these permissions assignments to take effect.
++ The default configuration for a search service is [key-based authentication](search-security-api-keys.md). If you don't change this setting to **Both** or **Role-based access control**, all requests that use role-based authentication are automatically denied, regardless of the underlying permissions.
+
++ If your request includes an API key alongside role-based credentials, the service authenticates using the key. Remove the API key from your request headers to use role-based authentication.
+
++ If the authorization token comes from a [managed identity](/entra/identity/managed-identities-azure-resources/overview) and you recently assigned the appropriate permissions, it [might take several hours](/entra/identity/managed-identities-azure-resources/managed-identity-best-practice-recommendations#limitation-of-using-managed-identities-for-authorization) for the permissions assignments to take effect.
+
++ If queries with document-level permissions don't return expected results, use Search Index Data Contributor or [create a custom role](#create-a-custom-role) with [elevated permissions](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results) to investigate.
+
+## Next step
+
+This article explains how to assign roles for control and data plane operations on Azure AI Search. For comprehensive instructions on adding role-based access to your application code:
 
-+ The default configuration for a search service is [key-based authentication](search-security-api-keys.md). If you don't change the default key setting to **Both** or **Role-based access control**, then all requests by using role-based authentication are automatically denied regardless of the underlying permissions.
+> [!div class="nextstepaction"]
+> [Connect your app to Azure AI Search using identities](search-security-rbac-client-code.md)
````
</details>

### Summary

```json
{
    "modification_type": "major update",
    "modification_title": "RBACドキュメントの大幅更新"
}
```

### Explanation
このコードの差分は、ドキュメント「search-security-rbac.md」に対する大幅な更新を示しています。特に、Azure AI Searchにおけるロールベースのアクセス制御（RBAC）に関する情報が大幅に改善され、整理されています。主な変更点は以下の通りです：

- ドキュメントの構成が改善され、役割の説明や関連情報が明確に整理されました。特に、制御プレーンとデータプレーンの操作に関する記述が明確化されました。
- 新しい役割の説明や、役割の割り当て方法に関する手順が追加され、具体的なガイダンスが提供されるようになりました。
- 「Search Index Data Contributor」および「Search Index Data Reader」など、役割の機能が更新され、インデックスのクエリや読み取り操作に関連する許可が強調されています。
- サンプルコードが最新のものに更新され、Azure CLIやPowerShellを使用した役割の割り当て方法が示されています。
- 「条件付きアクセスポリシーの作成」に関する情報が追加され、Azure AI Searchのセキュリティが強化されています。

このような変更により、ユーザーはAzure AI Searchにおける役割の使用と設定についてより深く理解できるようになり、ドキュメントの全体的な情報の一貫性とアクセス容易性が向上しています。全体として、この更新はドキュメントの品質を大幅に向上させるものです。

## articles/search/search-what-is-an-index.md{#item-5a3344}

<details>
<summary>Diff</summary>
````diff
@@ -160,7 +160,7 @@ All indexing and query requests target an index. Endpoints are usually one of th
 
 | Endpoint | Connection and access control |
 |----------|-------------------------------|
-| `<your-service>.search.windows.net/indexes` | Targets the indexes collection. Used when creating, listing, or deleting an index. Admin rights are required for these operations and available through admin [API keys](search-security-api-keys.md) or a [Search Contributor role](search-security-rbac.md#built-in-roles-used-in-search). |
+| `<your-service>.search.windows.net/indexes` | Targets the indexes collection. Used when creating, listing, or deleting an index. Admin rights are required for these operations and available through admin [API keys](search-security-api-keys.md) or a [Search Contributor role](search-security-rbac.md#built-in-roles). |
 | `<your-service>.search.windows.net/indexes/<your-index>/docs` | Targets the documents collection of a single index. Used when querying an index or data refresh. For queries, read rights are sufficient and available through query API keys or a data reader role. For data refresh, admin rights are required. |
 
 #### How to connect to an index
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスエンドポイントの表記の修正"
}
```

### Explanation
このコードの差分は、ドキュメント「search-what-is-an-index.md」のインデックスエンドポイントに関する説明の微修正を示しています。具体的な変更点は以下の通りです：

- インデックスのコレクションを対象とするエンドポイントの説明で、表記が少し修正されました。具体的には、「Search Contributor role used in search」との接続がより明確にするために、「built-in-roles」へのリンクが短縮されました。
- 他の部分は変更されていませんが、このマイナーな修正により、ドキュメント内の一貫性と可読性が向上します。

更新の結果、ユーザーはインデックスに関連する操作やそのために必要な権限について、よりスムーズに理解できるようになりました。このような微調整は、ドキュメント全体の情報の整合性を保つのに役立ちます。

## articles/search/vector-store.md{#item-db9b8c}

<details>
<summary>Diff</summary>
````diff
@@ -222,7 +222,7 @@ All vector indexing and query requests target an index. Endpoints are usually on
 
 | Endpoint | Connection and access control |
 |----------|-------------------------------|
-| `<your-service>.search.windows.net/indexes` | Targets the indexes collection. Used when creating, listing, or deleting an index. Admin rights are required for these operations and available through admin [API keys](search-security-api-keys.md) or a [Search Contributor role](search-security-rbac.md#built-in-roles-used-in-search). |
+| `<your-service>.search.windows.net/indexes` | Targets the indexes collection. Used when creating, listing, or deleting an index. Admin rights are required for these operations and available through admin [API keys](search-security-api-keys.md) or a [Search Contributor role](search-security-rbac.md#built-in-roles). |
 | `<your-service>.search.windows.net/indexes/<your-index>/docs` | Targets the documents collection of a single index. Used when querying an index or data refresh. For queries, read rights are sufficient and available through query API keys or a data reader role. For data refresh, admin rights are required. |
 
 ### How to connect to Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクターストアのエンドポイント記述の修正"
}
```

### Explanation
このコードの差分は、ドキュメント「vector-store.md」のエンドポイントに関する描写の微調整を示しています。具体的な変更点は以下の通りです：

- インデックスのコレクションを対象とするエンドポイントの説明において、「Search Contributor role used in search」の表記が若干修正され、リンクが適切に整理されました。この変更により、関連情報へのアクセスがより直感的になりました。
- 変更は非常に小規模ですが、文書の整合性と明確さが向上し、ユーザーがインデックスに対する操作や必要な権限について理解しやすくなっています。

このようなマイナーな修正は、情報の正確性を保ちつつ、ユーザーにとってのドキュメントの可読性を高める効果があります。全体として、この更新は文書の品質を改善するものです。


