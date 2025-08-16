---
date: '2025-08-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e5828c1...MicrosoftDocs:80a6ada
summary: このコード修正には、Azureの検索サービスに関連する2つのドキュメント、「検索容量計画」と「Azure AI Searchのセキュリティ概要」のマイナーなアップデートが含まれています。変更点には、日付の更新、テキストの追加や明確化、不要なコメントの削除、エラーメッセージの改善、セクションの再構成、およびコンプライアンスとガバナンスの強調があります。これにより、ユーザーが情報をより理解しやすくなることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e5828c1...MicrosoftDocs:80a6ada){target="_blank"}

# ハイライト

このコード修正には、Azure の検索サービスに関連する2つのドキュメント、「検索容量計画」と「Azure AI Searchのセキュリティ概要」に対するマイナーなアップデートが含まれています。主な変更点には、日付の更新、テキストの明確化および追加、不要なコメントの削除、エラーメッセージの改善、セクションの再構成、およびコンプライアンスとガバナンスの強調が含まれます。

## 新機能

- 「検索容量計画」では価格ティアの変更オプションに関する具体的な説明が追加され、ユーザーがより理解しやすくなっています。
- 「Azure AI Searchのセキュリティ概要」では、セクションが再構成され、ネットワークトラフィック、アクセス制御、データ保護に関する明確な説明が追加されています。

## 破壊的変更

- 特段の破壊的変更はありませんが、用語や内容の具体化により、既存の認識に影響を与える可能性があります。

## その他の更新

- ドキュメントの日付の更新。
- 不要なコメントの削除。
- エラーメッセージの文体変更での簡潔化。
- タイトル変更やトラフィックに関するセクションの追加を通じた説明の明確化と詳細化。

# インサイト

今回の変更は、Azure Search に関連するユーザードキュメントを改善し、利用者にとって情報がより正確かつわかりやすいものにすることを意図しています。「検索容量計画」では、ユーザーがサービスの使用ティアを理解し、適切に管理するための情報が強化されています。これにより、最適なサービスレベルを選択し、コスト削減や効率的な運用をサポートします。

「Azure AI Searchのセキュリティ概要」では、具体的なセキュリティドメインに分かれた構成が導入され、ユーザーはより詳細にセキュリティ対策を学べます。アウトバウンドトラフィックおよび内部トラフィックに関する新しい情報は、セキュリティ管理における透明性を高め、ユーザーのコンプライアンス遵守をサポートします。このような修正は、ユーザーがセキュリティ上のベストプラクティスを理解し、適用するための指針を提供する意義があり、クラウドサービスの信頼性と利用価値を向上させます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-capacity-planning.md](#item-0dd6c9) | minor update | 検索容量計画に関する記事の更新 | modified | 8 | 10 | 18 | 
| [search-security-overview.md](#item-6b3f1e) | minor update | Azure AI Searchのセキュリティ概要の改訂 | modified | 53 | 43 | 96 | 


# Modified Contents
## articles/search/search-capacity-planning.md{#item-0dd6c9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: conceptual
-ms.date: 08/01/2025
+ms.date: 08/15/2025
 ---
 
 # Estimate and manage capacity of a search service
@@ -109,13 +109,11 @@ To increase or decrease the capacity of your service, you have two options:
 ### Change your pricing tier
 
 > [!NOTE]
-> The Azure portal supports changes between Basic and Standard (S1, S2, and S3) tiers. Currently, you can only use the portal to switch from a lower tier to a higher tier, such as switching from Basic to S1. Your region also can't have [capacity constraints on the higher tier](search-region-support.md).
+> The Azure portal supports changes between Basic and Standard (S1, S2, and S3) tiers. You can upgrade or downgrade tiers, provided your current service configuration doesn't exceed the [limits of the target tier](search-limits-quotas-capacity.md). Your region also can't have [capacity constraints on the target tier](search-region-support.md).
 
-<!-- You can upgrade or downgrade tiers, provided your current service configuration doesn't exceed the [limits of the target tier](search-limits-quotas-capacity.md). Your region also can't have [capacity constraints on the target tier](search-region-support.md). -->
+Your [pricing tier](search-sku-tier.md) determines the maximum storage of your search service. If you need more or less capacity, you can switch to a different pricing tier that accommodates your storage needs.
 
-Your [pricing tier](search-sku-tier.md) determines the maximum storage of your search service. If you need more <!-- or less capacity --> capacity, you can switch to a different pricing tier that accommodates your storage needs.
-
-In addition to capacity, pricing tiers determine limits on indexes, indexers, and other search objects. Compare the [service limits](search-limits-quotas-capacity.md) of your current tier and your desired tier before proceeding. Generally, switching to a higher tier increases your [storage limit](search-limits-quotas-capacity.md#service-limits) and [vector limit](search-limits-quotas-capacity.md#vector-index-size-limits), increases request throughput, and decreases latency. <!-- while switching to a lower tier has the opposite effect. -->
+In addition to capacity, pricing tiers determine limits on indexes, indexers, and other search objects. Compare the [service limits](search-limits-quotas-capacity.md) of your current tier and your desired tier before you proceed. Generally, switching to a higher tier increases your [storage limit](search-limits-quotas-capacity.md#service-limits) and [vector limit](search-limits-quotas-capacity.md#vector-index-size-limits), increases request throughput, and decreases latency, while switching to a lower tier has the opposite effect.
 
 Switching to a higher pricing tier also increases the cost of running your search service. For more information, see the [pricing page](https://azure.microsoft.com/pricing/details/search/).
 
@@ -131,7 +129,7 @@ To change your pricing tier:
 
 1. On the **Select Pricing Tier** page, choose a different tier from the list.
 
-   Currently, you can upgrade <!-- switch --> between Basic, S1, S2, and S3 only. Other pricing tiers are unavailable and appear dimmed.
+   Currently, you can switch between Basic, S1, S2, and S3 only. Other pricing tiers are unavailable and appear dimmed.
 
    :::image type="content" source="media/search-capacity-planning/pricing-tier-list.png" alt-text="Screenshot of the Select Pricing Tier page and the list of available tiers in the Azure portal." border="true" lightbox="media/search-capacity-planning/pricing-tier-list.png":::
 
@@ -158,12 +156,12 @@ The above steps aren't entirely consecutive. For example, the system starts prov
 
 ## Errors during scaling
 
-The following table lists the causes and solutions for errors that can occur during scaling operations.
+The following table lists causes and solutions for errors that can occur during scaling operations.
 
 | Error message | Cause | Solution |
 |--|--|--|
-| "Service update operations aren't allowed at this time because we're processing a previous request." | Another scaling operation is already in progress. | Check the **Overview** page in the Azure portal or use the [Search Management REST API](/rest/api/searchmanagement/services/get), [Azure PowerShell](search-manage-powershell.md#get-search-service-information), or [Azure CLI](search-manage-azure-cli.md#get-search-service-information) to get the status of your search service. If the status is "Provisioning," wait until it becomes "Succeeded" or "Failed" before trying again. <sup>1, 2</sup> |
-<!-- | "Failed to scale search service *servicename*. Error: *Object* count *ActualCount* exceeds allowable limit: *MaximumCount*." | Your current service configuration exceeds the limits of the target pricing tier. | Check that your storage usage, vector usage, indexes, indexers, and other objects fit within the lower tier's [service limits](search-limits-quotas-capacity.md). For example, the Basic tier supports up to 15 indexes, so you can't switch from S1 to Basic if you have 16 or more indexes. Adjust your resources before trying again. | -->
+| "Service update operations aren't allowed at this time because we're processing a previous request." | Another scaling operation is in progress. | Check the **Overview** page in the Azure portal or use the [Search Management REST API](/rest/api/searchmanagement/services/get), [Azure PowerShell](search-manage-powershell.md#get-search-service-information), or [Azure CLI](search-manage-azure-cli.md#get-search-service-information) to get the status of your search service. If the status is "Provisioning," wait until it becomes "Succeeded" or "Failed" before you try again. <sup>1, 2</sup> |
+| "Failed to scale search service *servicename*. Error: *Object* count *ActualCount* exceeds allowable limit: *MaximumCount*." | Your current service configuration exceeds the limits of the target pricing tier. | Check that your storage usage, vector usage, indexes, indexers, and other objects fit within the lower tier's [service limits](search-limits-quotas-capacity.md). For example, the Basic tier supports up to 15 indexes, so you can't switch from S1 to Basic if you have 16 indexes. Adjust your resources before you try again. |
 
 <sup>1</sup> There's no status for backups, which are internal operations that are unlikely to disrupt a scaling exercise.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索容量計画に関する記事の更新"
}
```

### Explanation
このコードの変更は、Azure の検索サービスに関連する文書「検索容量計画」において、いくつかのテキストの修正と日付の更新が行われたことを示しています。具体的には、文書全体で8行が追加され、10行が削除され、合計で18箇所が変更されました。

主な変更点には、以下の内容が含まれます：

1. **日付の更新**: 文書の日付が「2025年8月1日」から「2025年8月15日」に変更されました。
2. **テキストの明確化**: 特に、価格ティアの変更に関する説明が具体化され、ユーザーがダウングレードするオプションについても言及されています。これにより、ユーザーはサービスの上限内でティアを変更できることが明確に示されています。
3. **不要なコメントの削除**: 一部の不要なコメントが削除されています。これにより文書がすっきりし、読みやすくなっています。
4. **エラーメッセージの改善**: スケーリング操作中のエラーの原因と解決策についての表で、表現が一部変更され、文が簡潔に修正されています。

これらの修正は、ドキュメントの正確性を向上させ、ユーザーにとっての理解を助ける内容となっています。

## articles/search/search-security-overview.md{#item-6b3f1e}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Security overview
+title: Secure your Azure AI Search deployment
 titleSuffix: Azure AI Search
 description: Learn about the security features in Azure AI Search to protect endpoints, content, and operations.
 manager: nitinme
@@ -9,21 +9,26 @@ ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
+  - horz-security
 ms.topic: conceptual
-ms.date: 08/08/2025
+ms.date: 08/15/2025
 ---
 
 # Security in Azure AI Search
 
-Azure AI Search provides comprehensive security controls across network access, authentication, authorization, and data protection to meet enterprise requirements. As a solution architect, you should understand three key security domains: **network traffic patterns** (inbound client requests, outbound service connections, and internal Microsoft-managed traffic), **access control mechanisms** (Microsoft Entra ID with role-based access control or API key authentication), and **data protection** (encryption in transit via TLS 1.2/1.3, encryption at rest with optional customer-managed keys for double encryption).
+Azure AI Search provides comprehensive security controls across network access, data access, and data protection to meet enterprise requirements. As a solution architect, you should understand three key security domains:
 
-A search service supports multiple network security topologies—from IP firewall restrictions for basic protection to private endpoints for complete network isolation. For enterprise scenarios requiring granular permissions, you can implement document-level access controls and leverage network security perimeters to create logical boundaries around your Azure PaaS resources. All security features integrate with Azure's compliance framework and support common enterprise patterns like multitenancy and cross-service authentication using managed identities.
++ **Network traffic patterns and network security** - inbound, outbound, and internal traffic
++ **Access control mechanisms** - Microsoft Entra ID with roles, or API keys
++ **Data residency and protection** - encryption in transit, and at rest with optional double encryption
+
+A search service supports multiple network security topologies—from IP firewall restrictions for basic protection to private endpoints for complete network isolation. Optionally, use a network security perimeter to create a logical boundary around your Azure PaaS resources. For enterprise scenarios requiring granular permissions, you can implement document-level access controls. All security features integrate with Azure's compliance framework and support common enterprise patterns like multitenancy and cross-service authentication using managed identities.
 
 This article details the implementation options for each security layer to help you design appropriate security architectures for development and production environments.
 
-## Data flow (network traffic patterns)
+## Network traffic patterns
 
-An Azure AI Search service is hosted on Azure and is typically accessed by client applications over public network connections. While that pattern is predominant, it's not the only traffic pattern that you need to care about. Understanding all points of entry as well as outbound traffic is necessary background for securing your development and production environments.
+An Azure AI Search service can be hosted in the Azure public cloud, an Azure private cloud, or a sovereign cloud (such as Azure Government). By default, for all cloud hosts, the search service is typically accessed by client applications over public network connections. While that pattern is predominant, it's not the only traffic pattern that you need to care about. Understanding all points of entry as well as outbound traffic is necessary background for securing your development and production environments.
 
 Azure AI Search has three basic network traffic patterns:
 
@@ -38,7 +43,7 @@ Inbound requests that target a search service endpoint include:
 + Create, read, update, or delete indexes and other objects on the search service
 + Load an index with search documents
 + Query an index
-+ Trigger indexer or skillset execution
++ Run indexer or skillset jobs
 
 The [REST APIs](/rest/api/searchservice/) describe the full range of inbound requests that are handled by a search service.
 
@@ -49,32 +54,23 @@ At a minimum, all inbound requests must be authenticated using either of these o
 
 Additionally, you can add [network security features](#service-access-and-authentication) to further restrict access to the endpoint. You can create either inbound rules in an IP firewall, or create private endpoints that fully shield your search service from the public internet. 
 
-### Internal traffic
-
-Internal requests are secured and managed by Microsoft. You can't configure or control these connections. If you're locking down network access, no action on your part is required because internal traffic isn't customer-configurable.
-
-Internal traffic consists of:
-
-+ Service-to-service calls for tasks like authentication and authorization through Microsoft Entra ID, resource logging sent to Azure Monitor, and [private endpoint connections](service-create-private-endpoint.md) that utilize Azure Private Link.
-+ Requests made to Azure AI services APIs for [built-in skills](cognitive-search-predefined-skills.md)
-+ Requests made to the various models that support [semantic ranking](semantic-search-overview.md#availability-and-pricing).
-
 ### Outbound traffic
 
-Outbound requests can be secured and managed by you. Outbound requests originate from a search service to other applications. These requests are typically made by indexers for text-based indexing, custom skills-based AI enrichment, and vectorizations at query time. Outbound requests include both read and write operations.
+Outbound requests can be secured and managed by you. Outbound requests originate from a search service to other applications. These requests are typically made by indexers for text-based and multimodal indexing, custom skills-based AI enrichment, and vectorizations at query time. Outbound requests include both read and write operations.
 
 The following list is a full enumeration of the outbound requests for which you can configure secure connections. A search service makes requests on its own behalf, and on the behalf of an indexer or custom skill.
 
 | Operation | Scenario |
 | ----------| -------- |
-| Indexers | Connect to external data sources to retrieve data. For more information, see [Indexer access to content protected by Azure network security](search-indexer-securing-resources.md). |
-| Indexers | Connect to Azure Storage to persist [knowledge stores](knowledge-store-concept-intro.md), [cached enrichments](enrichment-cache-how-to-configure.md), [debug sessions](cognitive-search-debug-session.md). |
+| Indexers | Connect to external data sources to retrieve data (read access). For more information, see [Indexer access to content protected by Azure network security](search-indexer-securing-resources.md). |
+| Indexers | Connect to Azure Storage for write operations to  [knowledge stores](knowledge-store-concept-intro.md), [cached enrichments](enrichment-cache-how-to-configure.md), [debug sessions](cognitive-search-debug-session.md). |
 | Custom skills | Connect to Azure functions, Azure web apps, or other apps running external code that's hosted off-service. The request for external processing is sent during skillset execution. |
 | Indexers and [integrated vectorization](vector-search-integrated-vectorization.md) | Connect to Azure OpenAI and a deployed embedding model, or it goes through a custom skill to connect to an embedding model that you provide. The search service sends text to embedding models for vectorization during indexing. |
 | Vectorizers | Connect to Azure OpenAI or other embedding models at query time to [convert user text strings to vectors](vector-search-how-to-configure-vectorizer.md) for vector search. |
+| Knowledge agents | Connect to chat completion models for [agentic retrieval](search-agentic-retrieval-concept.md) query planning, and also for formulating answers grounded in search results. <p>If you're implementing a [basic RAG pattern](retrieval-augmented-generation-overview.md), your query logic calls an external chat completion model for formulating an answer grounded in search results. For this pattern, the connection to the model uses the identity of your client or user. The search service identity isn't used for the connection. In contrast, if you use [knowledge agents](search-agentic-retrieval-how-to-create.md) in a RAG retrieval pattern, the outbound request is made by the search service managed identity. |
 | Search service | Connect to Azure Key Vault for [customer-managed encryption keys](search-security-manage-encryption-keys.md) used to encrypt and decrypt sensitive data. |
 
-Outbound connections can be made using a resource's full access connection string that includes a key or a database login, or [a managed identity](search-how-to-managed-identities.md) if you're using Microsoft Entra ID and role-based access.
+Outbound connections can generally be made using a resource's full access connection string that includes a key or a database login, or [a managed identity](search-how-to-managed-identities.md) if you're using Microsoft Entra ID and role-based access.
 
 To reach Azure resources behind a firewall, [create inbound rules on other Azure resources that admit search service requests](search-indexer-howto-access-ip-restricted.md). 
 
@@ -89,6 +85,16 @@ Configure same-region connections using either of the following approaches:
 + [Trusted service exception](search-indexer-howto-access-trusted-service-exception.md)
 + [Resource instance rules](/azure/storage/common/storage-network-security?tabs=azure-portal#grant-access-from-azure-resource-instances)
 
+### Internal traffic
+
+Internal requests are secured and managed by Microsoft. You can't configure or control these connections. If you're locking down network access, no action on your part is required because internal traffic isn't customer-configurable.
+
+Internal traffic consists of:
+
++ Service-to-service calls for tasks like authentication and authorization through Microsoft Entra ID, resource logging sent to Azure Monitor, and [private endpoint connections](service-create-private-endpoint.md) that utilize Azure Private Link.
++ Requests made to Azure AI services APIs for [built-in skills](cognitive-search-predefined-skills.md)
++ Requests made to the various models that support [semantic ranking](semantic-search-overview.md#availability-and-pricing).
+
 <a name="service-access-and-authentication"></a>
 
 ## Network security
@@ -113,13 +119,13 @@ The private endpoint uses an IP address from the virtual network address space f
 
 :::image type="content" source="media/search-security-overview/inbound-private-link-azure-cog-search.png" alt-text="sample architecture diagram for private endpoint access":::
 
-While this solution is the most secure, using more services is an added cost so be sure you have a clear understanding of the benefits before diving in. For more information about costs, see the [pricing page](https://azure.microsoft.com/pricing/details/private-link/). For more information about how these components work together, [watch this video](#watch-this-video). Coverage of the private endpoint option starts at 5:48 into the video. For instructions on how to set up the endpoint, see [Create a Private Endpoint for Azure AI Search](service-create-private-endpoint.md).
+While this solution is the most secure, using more services is an added cost so be sure you have a clear understanding of the benefits before diving in. For more information about costs, see the [pricing page](https://azure.microsoft.com/pricing/details/private-link/). For more information about how these components work together, [watch this video](https://learn.microsoft.com/Shows/AI-Show/Azure-Cognitive-Search-Whats-new-in-security/player]). Coverage of the private endpoint option starts at 5:48 into the video. For instructions on how to set up the endpoint, see [Create a Private Endpoint for Azure AI Search](service-create-private-endpoint.md).
 
 ### Network security perimeter
 
-A network security perimeter is a logical network boundary around your platform-as-a-service (PaaS) resources that are deployed outside of a virtual network. It establishes a perimeter for controlling public network access to resources like Azure AI Search, Azure Storage, and Azure OpenAI. Inbound client connections and service-to-service connections occur within the boundary, which simplifies and strengthens your defenses against unauthorized access.
+A network security perimeter is a logical network boundary around your platform-as-a-service (PaaS) resources that are deployed outside of a virtual network. It establishes a perimeter for controlling public network access to resources like Azure AI Search, Azure Storage, and Azure OpenAI. You can grant exceptions through explicit access rules for inbound and outbound traffic. This approach helps prevent data exfiltration while maintaining necessary connectivity for your applications.
 
-It's common in Azure AI Search solutions to use multiple Azure resources. The following resources can all be joined to an [existing network security perimeter](/azure/private-link/create-network-security-perimeter-portal):
+Inbound client connections and service-to-service connections occur within the boundary, which simplifies and strengthens your defenses against unauthorized access. It's common in Azure AI Search solutions to use multiple Azure resources. The following resources can all be joined to an [existing network security perimeter](/azure/private-link/create-network-security-perimeter-portal):
 
 + [Azure AI Search](search-security-network-security-perimeter.md)
 + [Azure OpenAI](/azure/ai-foundry/openai/how-to/network-security-perimeter)
@@ -136,26 +142,30 @@ Once a request is admitted to the search service, it must still undergo authenti
 
 + [Key-based authentication](search-security-api-keys.md) is performed on the request (not the calling app or user) through an API key, where the key is a string composed of randomly generated numbers and letters that prove the request is from a trustworthy source. Keys are required on every request. Submission of a valid key is considered proof the request originates from a trusted entity. 
 
-You can use both authentication methods, or [disable an approach](search-security-enable-roles.md) that you don't want available on your search service.
+  Reliance on API key-based authentication means that you should have a plan for regenerating the admin key at regular intervals, per Azure security best practices. There are a maximum of two admin keys per search service. For more information about securing and managing API keys, see [Create and manage api-keys](search-security-api-keys.md).
+
+Key-based authentication is the default for data plane operations (creating and using objects on the search service). You can use both authentication methods, or [disable an approach](search-security-enable-roles.md) that you don't want available on your search service.
 
 ## Authorization
 
 Azure AI Search provides authorization models for service management and content management. 
 
-### Authorize service management
+### Privileged access
 
-Resource management is authorized through [role-based access control](/azure/role-based-access-control/overview) in your Microsoft Entra tenant. 
+On a new search service, existing role assignments at the subscription level are inherited by the search service, and only Owners and User Access Administrators can grant access.
 
-In Azure AI Search, Resource Manager is used to create or delete the service, manage API keys, scale the service, and configure security. As such, Azure role assignments will determine who can perform those tasks, regardless of whether they're using the [portal](search-manage.md), [PowerShell](search-manage-powershell.md), or the [Management REST APIs](/rest/api/searchmanagement).
+Control plane operations (service or resource creation and management) tasks are exclusively authorized through [role assignments](/azure/role-based-access-control/overview), with no ability to use key-based authentication for service administration.
 
-[Three basic roles](search-security-rbac.md) (Owner, Contributor, Reader) apply to search service administration. Role assignments can be made using any supported methodology (portal, PowerShell, and so forth) and are honored service-wide.
+Control plane operations include create, configure, or delete the service, and manage security. As such, Azure role assignments will determine who can perform those tasks, regardless of whether they're using the [portal](search-manage.md), [PowerShell](search-manage-powershell.md), or the [Management REST APIs](/rest/api/searchmanagement).
+
+[Three basic roles](search-security-rbac.md#assign-roles-for-service-administration) (Owner, Contributor, Reader) apply to search service administration. 
 
 > [!NOTE]
 > Using Azure-wide mechanisms, you can lock a subscription or resource to prevent accidental or unauthorized deletion of your search service by users with admin rights. For more information, see [Lock resources to prevent unexpected deletion](/azure/azure-resource-manager/management/lock-resources).
 
 ### Authorize access to content
 
-Content management refers to the objects created and hosted on a search service.
+Data plane operations refers to the objects created and used on a search service.
 
 + For role-based authorization, [use Azure role assignments](search-security-rbac.md) to establish read-write access to operations.
 
@@ -260,36 +270,36 @@ CMK support was rolled out in two phases. If you created your search service dur
 
 Enabling CMK encryption will increase index size and degrade query performance. Based on observations to date, you can expect to see an increase of 30-60 percent in query times, although actual performance will vary depending on the index definition and types of queries. Because of the negative performance impact, we recommend that you only enable this feature on indexes that really require it. For more information, see [Configure customer-managed encryption keys in Azure AI Search](search-security-manage-encryption-keys.md).
 
-## Security administration
-
-### Manage API keys
-
-Reliance on API key-based authentication means that you should have a plan for regenerating the admin key at regular intervals, per Azure security best practices. There are a maximum of two admin keys per search service. For more information about securing and managing API keys, see [Create and manage api-keys](search-security-api-keys.md).
-
-### Activity and resource logs
+## Logging and monitoring
 
 Azure AI Search doesn't log user identities so you can't refer to logs for information about a specific user. However, the service does log create-read-update-delete operations, which you might be able to correlate with other logs to understand the agency of specific actions.
 
 Using alerts and the logging infrastructure in Azure, you can pick up on query volume spikes or other actions that deviate from expected workloads. For more information about setting up logs, see [Collect and analyze log data](monitor-azure-cognitive-search.md) and [Monitor query requests](search-monitor-queries.md).
 
-### Certifications and compliance
+## Compliance and governance
 
 Azure AI Search participates in regular audits, and has been certified against many global, regional, and industry-specific standards for both the public cloud and Azure Government. For the complete list, download the [**Microsoft Azure Compliance Offerings** whitepaper](https://azure.microsoft.com/resources/microsoft-azure-compliance-offerings/) from the official Audit reports page.
 
+We recommend that you regularly review [Azure AI Search compliance certifications and documentation](/azure/compliance/) to ensure alignment with your regulatory requirements. 
+
+### Use Azure Policy
+
 For compliance, you can use [Azure Policy](/azure/governance/policy/overview) to implement the high-security best practices of [Microsoft cloud security benchmark](/security/benchmark/azure/introduction). The Microsoft cloud security benchmark is a collection of security recommendations, codified into security controls that map to key actions you should take to mitigate threats to services and data. There are currently 12 security controls, including [Network Security](/security/benchmark/azure/mcsb-network-security), Logging and Monitoring, and [Data Protection](/security/benchmark/azure/mcsb-data-protection).
 
 Azure Policy is a capability built into Azure that helps you manage compliance for multiple standards, including those of Microsoft cloud security benchmark. For well-known benchmarks, Azure Policy provides built-in definitions that provide both criteria and an actionable response that addresses noncompliance.
 
 For Azure AI Search, there's currently one built-in definition. It's for resource logging. You can assign a policy that identifies search services that are missing resource logging, and then turn it on. For more information, see [Azure Policy Regulatory Compliance controls for Azure AI Search](security-controls-policy.md).
 
-## Watch this video
+### Use tags
 
-Watch this fast-paced video for an overview of the security architecture and each feature category.
+Apply metadata tags to categorize search services based on data sensitivity and compliance requirements. This facilitates proper governance and security controls. For more information, see [Use tags to organize your Azure resources](/azure/azure-resource-manager/management/tag-resources) and [General guidance – Organize Azure resources using tags](/azure/azure-resource-manager/management/tag-resources).
 
-> [!VIDEO https://learn.microsoft.com/Shows/AI-Show/Azure-Cognitive-Search-Whats-new-in-security/player]
-
-## See also
+## Learn more
 
 + [Azure security fundamentals](/azure/security/fundamentals/)
 + [Azure Security](https://azure.microsoft.com/overview/security)
 + [Microsoft Defender for Cloud](/azure/security-center/)
+
+We also recommend the following video. It's several years old and doesn't cover newer features, but for a curated introduction to core security, you might find it helpful.
+
+> [!VIDEO https://learn.microsoft.com/Shows/AI-Show/Azure-Cognitive-Search-Whats-new-in-security/player]
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのセキュリティ概要の改訂"
}
```

### Explanation
このコードの変更は、Azure AI Searchのセキュリティに関する文書「セキュリティ概要」において、内容の更新が行われたことを示しています。変更では、53行が追加され、43行が削除され、合計で96箇所が修正されました。

主要な変更点は次のとおりです：

1. **タイトルの変更**: 文書のタイトルが「Security overview」から「Secure your Azure AI Search deployment」に変更され、より具体的な内容を示すようになりました。
2. **日付の更新**: 文書の日付が「2025年8月8日」から「2025年8月15日」に更新されています。
3. **セクションの再構成**: セキュリティドメインがより明確に示され、テキストが3つの主要なセキュリティドメイン（ネットワークトラフィックパターン、アクセス制御メカニズム、データ保護）に分けられました。
4. **内外のトラフィックの詳細な説明**: アウトバウンドトラフィックの詳細が追加され、内外のトラフィックがどのように処理されるかについての理解が深まっています。
5. **内部トラフィックに関する新しいセクション**: Microsoftによって管理される内部トラフィックに関するセクションが追加され、ユーザーが設定できないトラフィックの特性が説明されました。
6. **コンプライアンスとガバナンスの強調**: セキュリティ管理におけるコンプライアンス規制とAzure Policyを使用した管理の重要性が強調されています。

これらの修正は、ドキュメントの正確性とユーザーがAzure AI Searchのセキュリティ機能をよりよく理解できるようにすることを目的としています。


