---
date: '2026-04-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2646972...MicrosoftDocs:cca71eb
summary: このコード差分には、いくつかの小規模な更新と新機能が含まれています。特に、新しい記事「Azure AI Searchの地域キャパシティ制約に関する情報」が追加され、文書の日付と地域情報が更新され、プライベートリンク接続に関する詳細情報も提供されています。全体として、これらの変更はAzure
  AI Searchの利用体験を向上させ、ユーザーが直面するかもしれない地域のキャパシティ制約に対する対策を支援することを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2646972...MicrosoftDocs:cca71eb){target="_blank"}

<format>
# Highlights
このコード差分にはいくつかの小規模な更新と新機能が含まれています。特に、日付の更新、地域情報の修正、プライベートリンク接続に関する情報の追加、Azure AI Searchの地域キャパシティ制約に関する新しい記事の追加が行われました。

## New features
- 新しい記事「Azure AI Searchの地域キャパシティ制約に関する情報」の追加。

## Breaking changes
- なし

## Other updates
- 文書の日付と地域情報の更新。
- プライベートリンク接続に関する詳細な情報の追加。
- SharePointインデクサーの再同期に関する説明の明確化。
- TOCファイルに新しい項目の追加。

# Insights
このコード差分は、主にAzure AI Searchに関連したドキュメントのメンテナンスと改善を目的としています。特に新しい記事の追加によって、Azure AI Searchの地域キャパシティ制約への対応方法が詳しく説明されており、サービスを最大限に活用するための手引きとなっています。この記事は、地域がキャパシティ制約を受けた場合の潜在的な解決策を詳述しており、ユーザーがスムーズにサービスを移行したり調整するための手助けとなるでしょう。

全体として、これらの変更はユーザーがAzure AI Searchを利用する際の体験を向上させ、より包括的なサポート情報を提供することを目的としています。地域のキャパシティ制約は頻繁に起こりうる問題であり、これに適切に対処するための情報提供は重要です。この新しいリソースにより、ユーザーは問題発生時に迅速かつ効果的に対策を講じることが可能となります。また、TOCの更新によりこれらの情報へのアクセスが容易になったことで、ユーザーの利便性も向上しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-document-intelligence-layout.md](#item-62c06f) | minor update | 文書の更新日付と地域情報の修正 | modified | 2 | 2 | 4 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | プライベートリンク接続に関する情報の更新 | modified | 7 | 4 | 11 | 
| [search-indexer-sharepoint-access-control-lists.md](#item-532a24) | minor update | SharePoint インデクサーに関する更新 | modified | 2 | 2 | 4 | 
| [search-region-capacity.md](#item-4a3fe4) | new feature | Azure AI Searchの地域キャパシティ制約に関する記事の追加 | added | 123 | 0 | 123 | 
| [toc.yml](#item-c4768f) | minor update | TOCに地域キャパシティ制約に関する項目の追加 | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/search/cognitive-search-skill-document-intelligence-layout.md{#item-62c06f}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: reference
-ms.date: 01/16/2026
+ms.date: 04/22/2026
 ms.update-cycle: 365-days
 ---
 
@@ -38,7 +38,7 @@ Supported regions vary by modality and how the skill connects to the Azure Docum
 
 | Approach | Requirement |
 |----------|-------------|
-| [**Import data** wizard](search-import-data-portal.md) | Create an Azure AI Search service and [Azure AI multi-service account](https://portal.azure.com/#create/Microsoft.CognitiveServicesAllInOne) in one of the following regions: East US, West Europe, or North Central US. | 
+| [**Import data** wizard](search-import-data-portal.md) | Create an Azure AI Search service and [Azure AI multi-service account](https://portal.azure.com/#create/Microsoft.CognitiveServicesAllInOne) in one of the following regions: East US, West Europe 2, or North Central US. | 
 | Programmatic, using a [Microsoft Foundry resource key](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) for billing | Create an Azure AI Search service and Microsoft Foundry resource in the same region. The region must support both [Azure AI Search and Azure Document Intelligence](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table). |
 | Programmatic, using [Microsoft Entra ID authentication (preview)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) for billing | No same-region requirement. Create an Azure AI Search service and Microsoft Foundry resource in any region where [each service is available](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table). |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書の更新日付と地域情報の修正"
}
```

### Explanation
この変更は、`cognitive-search-skill-document-intelligence-layout.md` ファイルにおける2つの主な更新を含んでいます。まず、文書の日付が2026年01月16日から2026年04月22日に変更されました。次に、対応する地域の情報が更新され、"West Europe" が "West Europe 2" に修正されました。この更新により、ユーザーは最新のドキュメント情報を参照できるようになり、Azure AI Searchサービスを設定する際の地域選択の正確性が向上します。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Configure indexer connections to access content from other Azure re
 ms.reviewer: mcarter
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 04/10/2026
+ms.date: 04/22/2026
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
@@ -59,7 +59,8 @@ You can create a shared private link for the following resources.
 | Microsoft.Sql/managedInstances (preview) <sup>5</sup>| `managedInstance` |
 | Microsoft.CognitiveServices/accounts <sup>6</sup> <sup>7</sup>| `openai_account` |
 | Microsoft.CognitiveServices/accounts <sup>8</sup> | `cognitiveservices_account` |
-| Microsoft.Fabric/privateLinkServicesForFabric <sup>9</sup> | `workspace` |
+| Microsoft.CognitiveServices/accounts <sup>9</sup> | `foundry_account` |
+| Microsoft.Fabric/privateLinkServicesForFabric <sup>10</sup> | `workspace` |
 
 <sup>1</sup> If Azure Storage and Azure AI Search are in the same region, the connection to storage is made over the Microsoft backbone network, which means a shared private link is redundant for this configuration. However, if you already set up a private endpoint for Azure Storage, you should also set up a shared private link or the connection is refused on the storage side. Also, if you're using multiple storage formats for various scenarios in search, make sure to create a separate shared private link for each subresource.
 
@@ -75,9 +76,11 @@ You can create a shared private link for the following resources.
 
 <sup>7</sup> Shared private link for Azure OpenAI is only supported in public cloud and [Microsoft Azure Government](https://azure.microsoft.com/explore/global-infrastructure/government/). Other cloud offerings don't have support for shared private links for `openai_account` Group ID.
 
-<sup>8</sup> Shared private links are supported for connections to Foundry resources. For AI enrichment, Azure AI Search connects to a Foundry resource for [billing purposes](cognitive-search-attach-cognitive-services.md). These connections can be private through a shared private link, which is only supported when configuring [a managed identity (keyless configuration)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) in the skillset definition.
+<sup>8</sup> Shared private links are supported for connections to Foundry resources. For [Foundry resource skills](cognitive-search-predefined-skills.md#foundry-resource) used in [AI enrichment](cognitive-search-concept-intro.md), Azure AI Search connects to a Foundry resource for [billing purposes](cognitive-search-attach-cognitive-services.md). These connections can be private through a shared private link, which is only supported when configuring [a managed identity (keyless configuration)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) in the skillset definition. 
 
-<sup>9</sup> Shared private link is supported for connections to OneLake workspace. To create a `privateLinkServicesForFabric` resource specific to a workspace, [register](/azure/azure-resource-manager/management/resource-providers-and-types#register-resource-provider) `Microsoft.Fabric` namespace to your subscription and refer to step 2 as documented in [Create the private link service in Azure](/fabric/security/security-workspace-level-private-links-set-up#step-2-create-the-private-link-service-in-azure). Note that when using a shared private link, the OneLake data source configuration must be defined with a specific connection string as outlined in the [OneLake indexer documentation](search-how-to-index-onelake-files.md#define-the-data-source).
+<sup>9</sup> Shared private links are supported for connections to Foundry resources. For Azure-hosted model skills such as [GenAI prompt skill](cognitive-search-skill-genai-prompt.md), [Azure OpenAI embedding skill](cognitive-search-skill-azure-openai-embedding.md), or [Content Understanding skill](cognitive-search-skill-content-understanding.md), Azure AI Search connects to a Foundry resource to execute the underlying processing. 
+
+<sup>10</sup> Shared private link is supported for connections to OneLake workspace. To create a `privateLinkServicesForFabric` resource specific to a workspace, [register](/azure/azure-resource-manager/management/resource-providers-and-types#register-resource-provider) `Microsoft.Fabric` namespace to your subscription and refer to step 2 as documented in [Create the private link service in Azure](/fabric/security/security-workspace-level-private-links-set-up#step-2-create-the-private-link-service-in-azure). Note that when using a shared private link, the OneLake data source configuration must be defined with a specific connection string as outlined in the [OneLake indexer documentation](search-how-to-index-onelake-files.md#define-the-data-source).
 
 ## 1 - Create a shared private link
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートリンク接続に関する情報の更新"
}
```

### Explanation
この変更は、`search-indexer-howto-access-private.md` ファイルにおいて、いくつかの重要な情報が更新されます。まず、文書の日付が2026年04月10日から2026年04月22日に変更されました。加えて、プライベートリンクに関連するリソース情報が修正され、特定のサービスの名称や使用法が正確に反映されました。たとえば、"Microsoft.CognitiveServices/accounts" のエントリーが "foundry_account" として変更され、新たに "workspace" に関する情報が追加されました。また、Foundryリソースとの接続やAIエンリッチメントに関する説明もより明確にされており、ユーザーがプライベートリンク設定を正しく理解し、利用できるように改善されています。

## articles/search/search-indexer-sharepoint-access-control-lists.md{#item-532a24}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how to configure Azure AI Search indexers for ingesting Acces
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 04/26/2026
+ms.date: 04/23/2026
 ---
 
 # Use a SharePoint indexer to ingest permission metadata and filter search results based on user access rights
@@ -192,7 +192,7 @@ POST https://{service}.search.windows.net/indexers/{indexer}/resetdocs?api-versi
 
 ### Resync ACLs across the full data source
 
-You can [resync the full data set ACL content](/rest/api/searchservice/indexers/resync?view=rest-searchservice-2025-11-01-preview&preserve-view=true) after initial ingestion.
+You can [resync the full data set ACL content](/rest/api/searchservice/indexers/resync?view=rest-searchservice-2025-11-01-preview&preserve-view=true) after initial ingestion. To fully succeed, this operation requires an [indexer run](search-howto-run-reset-indexers.md) after completion. 
 
 ```
 POST https://{service}.search.windows.net/indexers/{indexer}/resync?api-version=2025-11-01-preview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint インデクサーに関する更新"
}
```

### Explanation
この変更は、`search-indexer-sharepoint-access-control-lists.md` ファイルに対して行われ、主に文書の日付の更新と、ACLコンテンツの再同期に関する説明の明確化が含まれています。文書の日付は2026年04月26日から2026年04月23日に修正されました。また、ACLコンテンツの再同期操作に関して、完全に成功させるためには「インデクサーの実行」が必要であることが明記されました。この修正により、ユーザーは再同期操作を行う際の要件を理解しやすくなり、正しい手順を踏んで作業を進めることができます。

## articles/search/search-region-capacity.md{#item-4a3fe4}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,123 @@
+---
+title: How to handle regional capacity constraints in Azure AI Search
+description: Learn how to handle a regional capacity constraint that effects your Azure AI Search service.
+author: mattwojo
+ms.author: mattwoj
+ms.reviewer: angiesi
+ms.date: 04/22/2026
+ms.service: azure-ai-search
+ms.topic: concept-article
+---
+
+# How to handle regional capacity constraints in Azure AI Search
+
+This article helps you decide what to do when your preferred Azure AI Search region is unavailable due to capacity constraints. It also provides evaluation criteria for selecting an alternative region.
+
+## Capacity constraint options
+
+When a preferred Azure region is unavailable due to capacity constraints, you have two options:
+
+- Deploy to an alternative region. 
+- Retry deployment during off-peak hours.
+
+**Deploy to an alternative region.** (Recommended path)
+Azure AI Search is available across many Azure regions with consistent APIs, SDKs, SLAs, and compliance certifications. For most workloads, the operational difference between regions within the same geography is negligible. See the following section, *Criteria for selecting an alternative region*, for a full evaluation framework.
+
+**Retrying the service during off-peak hours is also a viable consideration.**
+Capacity constraints are sometimes temporary. Retrying deployment during low-traffic periods, such as nights or weekends in UTC, might succeed when peak-hour attempts fail. This option isn't guaranteed and isn't a substitute for evaluating an alternative region. If retries don't succeed within a reasonable window, proceed with an alternative region.
+
+Retry during off-peak hours when:
+
+- The deployment timeline allows for a delay of several days.
+- The constraint is likely the result of a temporary regional surge.
+- You prefer no architectural changes at this time.
+
+## Criteria for selecting an alternative region
+
+Evaluate the following criteria before selecting an alternative region:
+
+- Network latency
+- Compliance
+- Availability Zones
+- Feature and model availability
+- Data residency and sovereignty
+- Pricing
+
+### Network latency
+
+If existing services, such as applications or databases, remain in a different region than the new Azure AI Search deployment, each API call between them incurs cross-region round-trip time (RTT). For US-to-US regional pairs, this time is typically 26–50ms. For most search workloads, latency under 50ms RTT isn't perceptible to end users.
+Co-locating the application and the search service in the same region eliminates cross-region RTT entirely.
+For current region-to-region latency measurements, see [Azure network round-trip latency statistics](/azure/networking/azure-network-latency).
+
+### Compliance
+
+Azure compliance certifications - including FedRAMP High, HIPAA, CJIS, DoD IL2, IRS 1075, PCI DSS, and StateRAMP - are applied at the geography level, not the individual region level. All commercial Azure regions within the same geography carry an identical compliance posture.
+
+For more information, see:
+
+- [Azure compliance documentation](/azure/compliance)
+- [Azure regions list](/azure/reliability/regions-list)
+
+### Availability Zones
+
+Availability Zones (AZ) are physically separate datacenters within an Azure region. When a search service has two or more replicas in an AZ-supported region, Azure automatically distributes them across zones at no extra cost and with no configuration required.
+
+AZ support is relevant when the workload requires a 99.99% query SLA or operates in a regulated industry with documented high-availability requirements. For dev/test environments or workloads protected by a multiregion disaster recovery strategy, AZ support is generally not a blocking requirement.
+
+For the current list of regions that support Availability Zones for Azure AI Search, see [Azure regions with Availability Zones](/azure/reliability/availability-zones-region-support).
+
+## Feature and model availability
+
+Not all Azure AI Search features and AI models are available in every region. Before selecting an alternative region, verify availability for the specific capabilities your workload depends on, including any Azure OpenAI or Azure AI Foundry models used in retrieval-augmented generation (RAG), semantic ranking, or AI enrichment pipelines.
+
+When selecting an alternative region for Azure AI Search, verify model availability in the same region. Co-locating Azure AI Search with Azure OpenAI or Azure AI Foundry in the same region eliminates cross-service latency and simplifies compliance and data residency requirements.
+
+For more information, see:
+
+- [Azure AI Search regional availability](/azure/search/search-region-support)
+- [Azure OpenAI Service models by region](/azure/ai-services/openai/concepts/models)
+- [Azure AI Foundry regional availability](/azure/foundry/reference/region-support)
+- [Azure OpenAI quotas and limits](/azure/foundry/openai/quotas-limits)
+
+### Data residency and sovereignty
+
+Azure replicates data for resiliency within the same geography. For all commercial Azure regions within the United States geography, data at rest stays within the United States. This replication satisfies data residency requirements common in federal, state, and regulated industry workloads.
+
+For more information, see:
+
+- [Data, privacy, and built-in protections in Azure AI Search](/azure/search/search-security-overview)
+- [Azure data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/)
+
+### Pricing
+
+Azure AI Search service pricing is uniform across all regions within the same geography. Selecting an alternative region within the same geography doesn't change the service tier pricing.
+
+For current pricing, see [Azure AI Search pricing](https://azure.microsoft.com/pricing/details/search/).
+
+## Move or restore an Azure AI Search service
+
+You can back up and restore indexes, skillsets, indexers, and synonym maps to any region by using official scripts and tooling. This process enables both migration to an alternative region and a return to the original region when capacity becomes available.
+
+For more information, see:
+
+- [Move your Azure AI Search service to another region](/azure/search/search-howto-move-across-regions)
+- [Code sample demonstrating how to copy an index from one Azure AI Search service to another](/samples/azure-samples/azure-search-dotnet-utilities/azure-search-backup-restore-index/)
+
+## Related content
+
+- [Azure AI Search regional availability](/azure/search/search-region-support)
+- [Azure AI Search pricing](https://azure.microsoft.com/pricing/details/search/)
+- [Azure network round-trip latency statistics](/azure/networking/azure-network-latency)
+- [Azure regions list](/azure/reliability/regions-list)
+- [Azure compliance documentation](/azure/compliance/)
+- [Azure OpenAI Service models by region](/azure/ai-services/openai/concepts/models)
+- [Azure AI Foundry regional availability](/azure/foundry/reference/region-support)
+- [Move your Azure AI Search service to another region](/azure/search/search-howto-move-across-regions)
+- [Azure regions with Availability Zones](/azure/reliability/availability-zones-region-support)
+- [Data, privacy, and built-in protections in Azure AI Search](/azure/search/search-security-overview)
+
+
+
+
+
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Searchの地域キャパシティ制約に関する記事の追加"
}
```

### Explanation
この変更は、`search-region-capacity.md` という新しいファイルの追加を示しています。このファイルは、Azure AI Searchサービスの地域キャパシティ制約を扱う方法に関する情報を提供します。具体的には、利用可能な地域が容量制約により使用できない場合の選択肢として、代替地域へのデプロイやオフピーク時間帯での再試行について説明しています。

記事では、代替地域を選定する際の評価基準として、ネットワークの遅延、コンプライアンス、可用性ゾーン、機能およびモデルの可用性、データの居住地と主権、価格設定などが詳述されています。さらに、Azure AI Searchサービスを他の地域に移動または復元する方法についても解説されており、バックアップやスキルセット、インデクサーのデータを活用する方法が示されています。

この新たに追加されたコンテンツは、Azure AI Searchを利用するユーザーにとって、地域制約が発生した際に取るべき具体的な行動を理解するのに役立つ重要なリソースです。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -79,6 +79,8 @@ items:
       href: search-capacity-planning.md
     - name: Plan and manage costs
       href: search-sku-manage-costs.md
+    - name: Handling regional capacity constraints 
+      href: search-region-capacity.md
   - name: Reliability and tenancy
     items:
     - name: Reliability
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCに地域キャパシティ制約に関する項目の追加"
}
```

### Explanation
この変更は、`toc.yml` ファイルの更新を示しており、Azure AI Searchに関連する目次に「地域キャパシティ制約の扱い」という新しい項目が追加されました。具体的には、`search-region-capacity.md` というファイルへのリンクを持つ項目が追加されており、これによりユーザーは地域キャパシティの制約に関しての重要な情報やガイドラインに直接アクセスできるようになります。

この変更は、Azure AI Searchサービスを利用するユーザーが地域キャパシティの問題に対処するためのリソースを見つけやすくするためのものであり、ドキュメント全体の整合性と利便性を高めることに寄与しています。


