---
date: '2025-01-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9cc44af...MicrosoftDocs:2067774
summary: このコード差分は、Azure AI Searchに関するドキュメントの最新情報を反映するためのマイナーアップデートです。具体的には、複数の記事の日付を2025年1月27日に更新し、地域サポートやRBACに関する詳細な情報が追加されました。特に破壊的な変更はなく、これらの更新はドキュメントの正確性と有効性を保つことを目的としています。最終的に、ユーザーが正確かつ詳細な情報を容易に取得できるようにし、Azure
  AI Searchサービスの利便性を向上させることに寄与しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9cc44af...MicrosoftDocs:2067774){target="_blank"}

# ハイライト

このコード差分では、Azure AI Searchに関する複数の記事での日付を更新することにより、文書の最新情報を反映するマイナーアップデートが行われています。さらに、特定の記事では、内容に関する更新も行われています。

## 新機能

- 特定の文書での詳細な情報更新（地域サポート、RBACに関する情報）

## 破壊的変更

- 特に破壊的な変更は報告されていません。

## その他の更新

- 複数の記事の日付を2025年1月27日に更新。
- 機能可用性に関するより詳細な情報の追加。

# インサイト

これらの更新は、Azure AI Searchサービスに関連するドキュメントの正確性と有効性を保つためのものです。以下では、各変更の詳細とその意図について掘り下げます。

まず、日付の更新について。これは、文書が最新の情報を反映していることを示すためのものであり、ドキュメントが継続的にメンテナンスされていることを示唆します。日付だけの更新ではありますが、文書が最新であることを確認するための重要な要素です。

次に、メジャーな内容更新が行われた2つの記事についてですが、一つは地域サポートに関するもので、提供される機能の説明がより明確になり、地域別に利用可能な機能が一目で分かるような表形式が導入されました。これにより、ユーザーは地域による機能の差異を確認しやすくなり、より適切な判断が可能になります。

もう一つはRBACに関するもので、役割とその権限についての説明が改善されました。役割がどのようにデータプレーンおよびコントロールプレーンの操作に関連付けられているのかが明示され、特定の操作についての詳細が見やすい表形式で提供されるようになりました。この更新は、ユーザーが適切なアクセス権を設定しやすくし、アプリケーションのセキュリティ運用をよりスムーズに進める助けとなります。

最終的に、これらの更新は、ドキュメントの利用者が正確かつ詳細な情報を容易に取得できるようにすることを目的としており、Azure AI Searchサービスの利便性と信頼性を向上させることに寄与しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [monitor-azure-cognitive-search-data-reference.md](#item-561425) | minor update | Azure AI Searchのデータ参照に関する日付更新 | modified | 1 | 1 | 2 | 
| [monitor-azure-cognitive-search.md](#item-5be826) | minor update | Azure AI Searchの監視に関する日付更新 | modified | 1 | 1 | 2 | 
| [search-monitor-queries.md](#item-279569) | minor update | Azure AI Searchのクエリモニタリングに関する日付更新 | modified | 1 | 1 | 2 | 
| [search-region-support.md](#item-25b0f1) | minor update | Azure AI Searchの地域サポートに関する内容更新 | modified | 12 | 10 | 22 | 
| [search-security-rbac.md](#item-a5d129) | minor update | Azure AI SearchのRBACに関する内容更新 | modified | 7 | 5 | 12 | 


# Modified Contents
## articles/search/monitor-azure-cognitive-search-data-reference.md{#item-561425}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Monitoring data reference for Azure AI Search
 description: This article contains important reference material you need when you monitor Azure AI Search.
-ms.date: 02/15/2024
+ms.date: 01/27/2025
 ms.custom: horz-monitor
 ms.topic: reference
 author: HeidiSteen
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのデータ参照に関する日付更新"
}
```

### Explanation
この変更は、Azure AI Searchに関するデータ参照記事のメタデータの日付を更新するものです。具体的には、元の日付が「2024年2月15日」から「2025年1月27日」に変更されました。この小規模な更新は、文書の情報が最新であることを反映しています。その他のメタデータは変更されておらず、著者やトピックに関する情報はそのまま維持されています。このアップデートは、ユーザーに対してより正確なタイムスタンプを提供し、リソースを定期的に見直す重要性を示しています。

## articles/search/monitor-azure-cognitive-search.md{#item-5be826}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Monitor Azure AI Search
 description: Start here to learn how to monitor Azure AI Search.
-ms.date: 02/15/2024
+ms.date: 01/27/2025
 ms.custom: horz-monitor
 ms.topic: conceptual
 author: HeidiSteen
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchの監視に関する日付更新"
}
```

### Explanation
この変更は、「Azure AI Searchの監視」に関する記事のメタデータの日付を更新したものです。具体的には、元の日付が「2024年2月15日」から「2025年1月27日」に変更されました。この更新は文書の最新情報を反映させるためのもので、ユーザーが正確な情報を得られるようにしています。その他のメタ情報は変わらず、著者やトピックの情報もそのまま保持されています。このような小さな更新は、ドキュメントの維持管理において重要です。

## articles/search/search-monitor-queries.md{#item-279569}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 02/21/2024
+ms.date: 01/27/2025
 ---
 
 # Monitor query requests in Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのクエリモニタリングに関する日付更新"
}
```

### Explanation
この変更は、「Azure AI Searchのクエリモニタリング」に関する記事のメタデータの日付を更新したものです。具体的には、元の日付が「2024年2月21日」から「2025年1月27日」に変更されました。この更新は、文書の最新情報を反映させることを目的としており、ユーザーが信頼できる情報を得るために重要です。その他のメタ情報、特にサービスに関する情報やトピックについては変更されていないため、コンテンツの一貫性は保たれています。このような小さな更新は、文書の有効期限を維持するために必要です。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
 ms.custom: references_regions
-ms.date: 11/19/2024
+ms.date: 01/27/2025
 
 ---
 
@@ -19,15 +19,17 @@ This article identifies the cloud regions in which Azure AI Search is available.
 
 ## Features subject to regional availability
 
-| Feature | Availability |
-|---------|--------------|
-| [Extra capacity](search-limits-quotas-capacity.md#service-limits) | Higher capacity partitions became available in selected regions starting in April 2024 with a second wave following in May 2024. If you're using an older search service, create a new search service to benefit from more capacity at the same billing rate. To check existing capacity, [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) and select the **Properties** tab in the middle of the Overview page. To check search service age, follow [these instructions](vector-search-index-size.md#how-to-check-service-creation-date).  Currently, there are just a few regions that *don't* offer higher capacity partitions. Regional support for extra capacity is noted in the footnotes of this article.|
-| [Availability zones](search-reliability.md#availability-zone-support) | Divides a region's data centers into distinct physical location groups, providing high-availability within the same geo. Regional support is noted in this article. |
-| [AI service integration](cognitive-search-concept-intro.md) | Refers to skills that make internal calls to Azure AI for enrichment and transformation during indexing. Integration requires that Azure AI Search coexists with an [Azure AI multi-service account](/azure/ai-services/multi-service-resource) in the same physical region. Regional support is noted in this article. |
-| [Azure OpenAI integration](vector-search-integrated-vectorization.md)  | Refers to skills and vectorizers that make internal calls to deployed embedding and chat models on Azure OpenAI. Check [Azure OpenAI model region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability) for the most current list of regions for each embedding and chat model. Specific Azure OpenAI models are in fewer regions, so be sure to check for joint regional availability before installing.|
-| [Azure AI Foundry integration](vector-search-integrated-vectorization-ai-studio.md) | Refers to skills and vectorizers that make internal calls to the models hosted in the model catalog. Check [Azure AI Foundry region availability](/azure/ai-studio/reference/region-support) for the most current list of regions. |
-| [Azure AI Vision 4.0 multimodal APIs for image vectorization](search-get-started-portal-image-search.md) | Refers to skills and vectorizers that call the multimodal embedding API. Check the [Azure AI Vision region list](/azure/ai-services/computer-vision/overview-image-analysis#region-availability) for joint regional availability. |
-| [Semantic ranker](semantic-search-overview.md) | Takes a dependency on Microsoft-hosted models in specific regions. Regional support is noted in this article. |
+Some features take a dependency on other Azure services or infrastructure that are subject to regional availability. If you need a specific feature, make sure it's available in the desired region.
+
+| Feature | Description | Availability |
+|---------|-------------|--------------|
+| [Extra capacity](search-limits-quotas-capacity.md#service-limits) | Higher capacity partitions became available in selected regions starting in April 2024 with a second wave following in May 2024. Currently, there are just a few regions that *don't* offer higher capacity partitions. If you're using an older search service, create a new search service to benefit from more capacity at the same billing rate. |  Regional support for extra capacity is noted in the footnotes of this article. <p>Check [service age](vector-search-index-size.md#how-to-check-service-creation-date) to see if your search service was created after high capacity partitions became available. <p>To check the capacity of an existing service, [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) and select the **Properties** tab in the middle of the Overview page.|
+| [Availability zones](search-reliability.md#availability-zone-support) | Divides a region's data centers into distinct physical location groups, providing high-availability within the same geo. | Regional support is noted in this article. |
+| [Semantic ranker](semantic-search-overview.md) | Takes a dependency on Microsoft-hosted models in specific regions. | Regional support is noted in this article. |
+| [AI service integration](cognitive-search-concept-intro.md) | Refers to [built-in skills](cognitive-search-predefined-skills.md) that make internal calls to Azure AI for enrichment and transformation during indexing. Integration requires that Azure AI Search coexists with an [Azure AI multi-service account](/azure/ai-services/multi-service-resource) in the same physical region. You can bypass region requirements if you use [identity-based connections](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection), currently in public review. | Regional support is noted in this article. |
+| [Azure OpenAI integration](vector-search-integrated-vectorization.md)  | Refers to the AzureOpenAIEmbedding skill and vectorizer that make internal calls to deployed embedding models on Azure OpenAI. | Check [Azure OpenAI model region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability) for the most current list of regions for each embedding and chat model. Specific Azure OpenAI models are in fewer regions, so check for model availability first, and then verify Azure AI Search is available in the same region.|
+| [Azure AI Foundry integration](vector-search-integrated-vectorization-ai-studio.md) | Refers to skills and vectorizers that make internal calls to the models hosted in the model catalog. | Check [Azure AI Foundry region availability](/azure/ai-studio/reference/region-support) for the most current list of regions. |
+| [Azure AI Vision 4.0 multimodal APIs](search-get-started-portal-image-search.md) | Refers to the Azure AI Vision multimodal embeddings skill and vectorizer that call the multimodal embedding API. | Check the [Azure AI Vision region list](/azure/ai-services/computer-vision/overview-image-analysis#region-availability) first, and then verify Azure AI Search is available in the same region.|
 
 ## Azure Public regions
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchの地域サポートに関する内容更新"
}
```

### Explanation
この変更は、「Azure AI Searchの地域サポート」に関する記事の内容を更新したもので、特に機能の可用性についての情報が見直されました。具体的には、記事に記載されている日付が「2024年11月19日」から「2025年1月27日」に変更されました。内容的には、地域によって提供される機能の説明が誇張され、特定の機能が他のAzureサービスやインフラに依存していることが明記されています。

更新後の表形式では、機能名、説明、可用性が詳細に記載され、利用者が各機能の地域サポートを一目で確認できるようになっています。これにより、ユーザーは自分が必要とする機能が希望する地域に存在するかどうかを簡単に判断できるようになり、情報の透明性が向上しています。この更新は、情報が正確で最新であることを示し、利用者にとって有益です。

## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 10/30/2024
+ms.date: 01/27/2025
 ms.custom: subject-rbac-steps, devx-track-azurepowershell
 ---
 
@@ -59,6 +59,8 @@ The following steps work for all role assignments.
 
 ## Built-in roles used in search
 
+Roles are a collection of permissions on specific operations affecting either data plane or control plane layers.
+
 *Data plane* refers to operations against the search service endpoint, such as indexing or queries, or any other operation specified in the [Search Service REST APIs](/rest/api/searchservice/) or equivalent Azure SDK client libraries. 
 
 *Control plane* refers to Azure resource management, such as creating or configuring a search service.
@@ -67,7 +69,7 @@ The following roles are built in. If these roles are insufficient, [create a cus
 
 | Role | Plane | Description  |
 | ---- | ------|--------------------- |
-| [Owner](/azure/role-based-access-control/built-in-roles#owner) | Control & Data | Full access to the control plane of the search resource, including the ability to assign Azure roles. Only the Owner role can enable or disable authentication options or manage roles for other users. Subscription administrators are members by default. </br></br>On the data plane, this role has the same access as the Search Service Contributor role. It includes access to all data plane actions except the ability to query or index documents.|
+| [Owner](/azure/role-based-access-control/built-in-roles#owner) | Control & Data | Full access to the control plane of the search resource, including the ability to assign Azure roles. Only the Owner role can enable or disable authentication options or manage roles for other users. Subscription administrators are members by default. </br></br>On the data plane, this role has the same access as the Search Service Contributor role. It includes access to all data plane actions except the ability to query documents.|
 | [Contributor](/azure/role-based-access-control/built-in-roles#contributor) | Control & Data |  Same level of control plane access as Owner, minus the ability to assign roles or change authentication options. </br></br>On the data plane, this role has the same access as the Search Service Contributor role. It includes access to all data plane actions except the ability to query or index documents.|
 | [Reader](/azure/role-based-access-control/built-in-roles#reader) | Control & Data | Read access across the entire service, including search metrics, content metrics (storage consumed, number of objects), and the object definitions of data plane resources (indexes, indexers, and so on). However, it can't read API keys or read content within indexes. |
 | [Search Service Contributor](/azure/role-based-access-control/built-in-roles#search-service-contributor) | Control & Data | Read-write access to object definitions (indexes, aliases, synonym maps, indexers, data sources, and skillsets). This role is for developers who create objects, and for administrators who manage a search service and its objects, but without access to index content. Use this role to create, delete, and list indexes, get index definitions, get service information (statistics and quotas), test analyzers, create and manage synonym maps, indexers, data sources, and skillsets. See [`Microsoft.Search/searchServices/*`](/azure/role-based-access-control/resource-provider-operations#microsoftsearch) for the permissions list. |
@@ -88,7 +90,7 @@ Combine these roles to get sufficient permissions for your use case.
 |List all objects on the resource |❌|❌|✅|✅|✅|
 |Access quotas and service statistics |❌|❌|✅|✅|❌|
 |Read/query an index |✅|✅|❌|❌|❌|
-|Upload data for indexing |❌|✅|❌|❌|❌|
+|Upload data for indexing |❌|✅|❌|✅|❌|
 |Create or edit indexes/aliases |❌|❌|✅|✅|❌|
 |Create, edit and run indexers/data sources/skillsets |❌|❌|✅|✅|❌|
 |Create or edit synonym maps |❌|❌|✅|✅|❌|
@@ -103,7 +105,7 @@ Combine these roles to get sufficient permissions for your use case.
 
 Owners and Contributors grant the same permissions, except that only Owners can assign roles.
 
-Owners and Contributors can create, read, update, and delete objects in the Azure portal *if API keys are enabled*. the Azure portal uses keys on internal calls to data plane APIs. In you subsequently configure Azure AI Search to use "roles only", then Owner and Contributor won't be able to manage objects in the Azure portal using just those role assignments. The solution is to assign more roles, such as Search Index Data Reader, Search Index Data Contributor, and Search Service Contributor.
+<!-- Owners and Contributors can create, read, update, and delete objects in the Azure portal *if API keys are enabled*. the Azure portal uses keys on internal calls to data plane APIs. In you subsequently configure Azure AI Search to use "roles only", then Owner and Contributor won't be able to manage objects in the Azure portal using just those role assignments. The solution is to assign more roles, such as Search Index Data Reader, Search Index Data Contributor, and Search Service Contributor. -->
 
 ## Assign roles
 
@@ -175,7 +177,7 @@ Role assignments are global across the search service. To [scope permissions to
 
 | Task | Role | ID|
 | --- | --- | --- |
-| CRUD operations | [`Search Service Contributor`](/azure/role-based-access-control/built-in-roles#search-service-contributor)|7ca78c08-252a-4471-8644-bb5ff32d4ba0|
+| Create or manage objects| [`Search Service Contributor`](/azure/role-based-access-control/built-in-roles#search-service-contributor)|7ca78c08-252a-4471-8644-bb5ff32d4ba0|
 | Load documents, run indexing jobs | [`Search Index Data Contributor`](/azure/role-based-access-control/built-in-roles#search-index-data-contributor)|8ebe5a00-799e-43f5-93ac-243d3dce84a7|
 | Query an index | [`Search Index Data Reader`](/azure/role-based-access-control/built-in-roles#search-index-data-reader)|1407120a-92aa-4202-b7e9-c0e197c71c8f|
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI SearchのRBACに関する内容更新"
}
```

### Explanation
この変更は、「Azure AI SearchのRBAC（Role-Based Access Control）」に関する記事の内容を更新するもので、主に役割やその説明が改善されました。具体的には、日付が「2024年10月30日」から「2025年1月27日」に更新されたほか、特定の機能の可用性についての説明が追加されました。

更新後の内容では、役割がデータプレーンとコントロールプレーンの特定の操作に対する権限を集約したものであることが明示され、新しい表組みによって役割ごとの詳細な説明が強調されています。また、検索サービスの操作に関する役割の記載が明確になり、ユーザーが自分のニーズに応じた役割を容易に理解できるようになっています。

最後に、APIキーの有効化によるAzureポータルでのオブジェクトの管理に関する注記が非表示にされており、情報が整理されてより明確になったことで、ユーザー体験が向上しています。全体として、この更新は利用者にとっての有用性を高めることを目的としています。


