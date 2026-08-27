---
date: '2026-08-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:eaaa74d...MicrosoftDocs:d002f33
summary: この更新では、Azure AI Searchに関する文書が調整され、サポートされているリージョンと新機能のサポート状況が追加されました。特に、機密コンピューティングとサーバーレス料金モデルに関連する情報が整理され、具体的なリージョンごとの利用可能性が明示されています。また、文書の日付フィールドが更新され、機能サポートのテーブルもよりユーザーフレンドリーに改善されています。この改訂は、特に国際的な顧客やサービス提供者にとって、機能の利用可能性を確認しやすくすることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:eaaa74d...MicrosoftDocs:d002f33){target="_blank"}

# ハイライト
この更新では、Azure AI Searchにおけるサポートされるリージョンに関する文書が調整され、新しい機能のサポート状況が追加されました。また、特定の機能がどのリージョンで使用可能かを明確化しています。機密コンピューティングやサーバーレス料金モデルに特化した更新が行われました。

## 新機能
- 各リージョンにおける「機密コンピューティング」のサポート状況が明記されました。
- 「サーバーレス料金モデル」に関する情報が整理され、より読みやすい形式で追加されました。

## 既存機能に対する破壊的変更
この更新により、既存の機能が破壊されたという情報はありません。

## その他の更新
- 文書の日付フィールドが2026年7月13日から2026年8月24日に更新されました。
- リージョンごとの機能サポートのテーブルが整形され、ユーザーフレンドリーになっています。

# 洞察
今回の更新は、Azure AI Searchのリージョンサポートに関する文書を、ユーザーがアクセスしやすくすることを目的としています。特に、機能の利用可能性をリージョン別に確認できるようになったことは、国際的な顧客やサービス提供者にとって非常に有益です。

「機密コンピューティング」は、データプライバシーおよびセキュリティにおいて重要な役割を果たしており、多くのリージョンでのサポート状況が明示されたことで、ユーザーは安心してこれらの機能を利用する計画を立てられます。また、「サーバーレス料金モデル」の情報が更新されたことにより、柔軟な価格設定を重視する企業にとって、コスト管理がより容易になります。

これらの文書更新は、Azure AI Searchの国際展開を模索する企業にとって、どの市場でどの機能を提供するかとういう戦略を立案する手助けとなります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-region-support.md](#item-25b0f1) | minor update | サポートされるリージョンに関する更新 | modified | 47 | 45 | 92 | 


# Modified Contents
## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Supported Regions
 description: Learn about the regions that offer Azure AI Search and the features available in each region.
 author: mattwojo
 ms.author: mattwoj
-ms.date: 07/13/2026
+ms.date: 08/24/2026
 ms.service: azure-ai-search
 ms.topic: concept-article
 ai-usage: ai-assisted
@@ -29,10 +29,10 @@ When you create an Azure AI Search service, your region selection might depend o
 | [AI enrichment](cognitive-search-concept-intro.md) | Refers to [built-in skills](cognitive-search-predefined-skills.md) that make internal calls to Foundry Tools for enrichment and transformation during indexing. Integration requires that Azure AI Search coexists with a [Microsoft Foundry resource](/azure/ai-services/multi-service-resource) in the same physical region. You can bypass region requirements by using [identity-based connections](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection).  For the purposes of region availability in this article, AI enrichment refers only to built-in AI skills that use an [Azure AI Search-managed / Foundry-attached resource for billing](cognitive-search-predefined-skills.md#foundry-resource). It doesn't include [custom skills](cognitive-search-predefined-skills.md#custom-skills), or [customer-hosted AI workloads](cognitive-search-predefined-skills.md#azure-hosted-model-or-resource). | Regional support is noted in this article. |
 | [Availability zones](/azure/reliability/reliability-ai-search#availability-zone-support) | Divides a region's data centers into distinct physical location groups, providing high availability within the same geo. | Regional support is noted in this article. |
 | [Agentic retrieval](agentic-retrieval-overview.md) | Uses the agentic retrieval engine designed for conversational search. | Regional support is noted in this article. |
-| [Confidential computing](search-security-best-practices.md#optional-enable-confidential-computing) | Deploys your search service on confidential VMs to process data in a hardware-based trusted execution environment.<p>Confidential computing disables or restricts certain features, including agentic retrieval, semantic ranker, query rewrite, and skillset execution. | Regional support is noted in this article. |
+| [Confidential computing](search-security-best-practices.md#optional-enable-confidential-computing) | Deploys your search service on confidential VMs to process data in a hardware-based trusted execution environment.<p>Confidential computing disables or restricts certain features, including agentic retrieval, semantic ranker, query rewrite, and skillset execution. | Available in Australia East, Brazil South, Canada Central, East US 2, Italy North, Korea Central, Norway East, South Africa North, Spain Central, Switzerland North, UAE North, UK South, and West Europe. |
 | [Semantic ranker](semantic-search-overview.md) | Takes a dependency on Microsoft-hosted models in specific regions. | Regional support is noted in this article. |
 | [Query rewrite](semantic-how-to-query-rewrite.md) | Takes a dependency on Microsoft-hosted models in specific regions. | Regional support is noted in this article. |
-| [Serverless pricing model](serverless-cost-optimization.md) | Enables pay-per-request billing for search workloads. | Preview in Australia East, Central India, Central US, Japan East, North Central US, Sweden Central, Switzerland North, UK South, West Central US, West US, and West US 2. |
+| [Serverless pricing model (preview)](serverless-cost-optimization.md) | Enables pay-per-request billing for search workloads. | Regional support is noted in this article. |
 | [Extra capacity](search-limits-quotas-capacity.md#service-limits) | Higher-capacity partitions became available in select regions starting in April 2024, with a second wave following in May 2024. Currently, there are just a few regions that *don't* offer higher-capacity partitions.<p>If you have an older search service in a supported region, check if you can [upgrade your service](search-how-to-upgrade.md). Otherwise, create a new search service to benefit from more capacity at the same billing rate. | Regional support is noted in the footnotes of this article. |
 | Capacity constraints | In some regions, insufficient capacity prevents you from creating search services on certain tiers. The Azure portal automatically hides regions and tiers that aren't available for new deployments. | Regional support is noted in the footnotes of this article. |
 | [Azure Vision in Foundry Tools 4.0 multimodal APIs](search-get-started-portal-image-search.md) | Refers to the Azure Vision multimodal embeddings skill and vectorizer that call the multimodal embedding API. | Check the [Azure Vision region list](/azure/ai-services/computer-vision/overview-image-analysis#region-availability) first, and then verify Azure AI Search is available in the same region.|
@@ -43,105 +43,107 @@ You can create an Azure AI Search service in any of the following Azure public r
 
 ### Americas
 
-| Region | AI enrichment | Availability zones | Agentic retrieval | Confidential computing | Semantic ranker | Query rewrite |
-|--|--|--|--|--|--|--|
-| Brazil South​​ <sup>1</sup> ​| ✅ |  | ✅ | ✅ | ✅ | ✅ |
-| Canada Central​​ <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| Canada East​​ ​<sup>1</sup> |  |  | ✅ |  | ✅ |  |
-| ​Central US​​ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| Region | AI enrichment | Agentic retrieval | Semantic ranker | Serverless | Availability zones | Query rewrite |
+| --- | --- | --- | --- | --- | --- | --- |
+| Brazil South​​ <sup>1</sup> ​| ✅ | ✅ | ✅ |  |  | ✅ |
+| Canada Central​​ <sup>1</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| Canada East​​ ​<sup>1</sup> |  | ✅ | ✅ |  |  |  |
+| ​Central US​​ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | East US​ <sup>1, 2</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
-| East US 2 <sup>1, 2</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| Mexico Central |  | ✅ |  |  |  |  |
-| North Central US​ <sup>1</sup> ​| ✅ |  | ✅ |  | ✅ | ✅ |
+| East US 2 <sup>1, 2</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| Mexico Central |  |  |  |  | ✅ |  |
+| North Central US​ <sup>1</sup> ​| ✅ | ✅ | ✅ | ✅ |  | ✅ |
 | South Central US​ <sup>1 </sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
-| West US​​ <sup>1, 2</sup> | ✅ |  | ✅ |  | ✅ | ✅ |
-| West US 2​ <sup>2,3</sup> ​| ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| West US​​ <sup>1, 2</sup> | ✅ | ✅ | ✅ | ✅ |  | ✅ |
+| West US 2​ <sup>2,3</sup> ​| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | West US 3​ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
-| West Central US​ ​<sup>1</sup>| ✅ |  | ✅ |  | ✅ |  |
+| West Central US​ ​<sup>1</sup>| ✅ | ✅ | ✅ | ✅ |  |  |
 
 <sup>1</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
 
-<sup>2</sup> This region is experiencing capacity constraints that prevent the creation of new search services and scaling operations. Please choose a different region.
+<sup>2</sup> This region is in high demand, which prevents the creation of new search services. Please choose a different region.
 
 <sup>3</sup> This region doesn't have indexer support for [Microsoft Purview sensitivity labels](search-indexer-sensitivity-labels.md).
 
 ### Europe
 
-| Region | AI enrichment | Availability zones | Agentic retrieval | Confidential computing | Semantic ranker | Query rewrite |
+| Region | AI enrichment | Agentic retrieval | Semantic ranker | Serverless | Availability zones | Query rewrite |
 |--|--|--|--|--|--|--|
 | France Central​​ <sup>1</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
-| Germany West Central​ <sup>1</sup> ​| ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| Germany West Central​ <sup>1,2</sup> ​| ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | Italy North​​ |  | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Norway East​​ | ✅ | ✅ |  | ✅ |  |  |
 | North Europe​ <sup>2</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
-| Poland Central​​ <sup>1</sup> |  |  | ✅ |  | ✅ | ✅ |
-| Spain Central <sup>3</sup> |  | ✅ |  | ✅ | ✅ | ✅ |
-| Sweden Central​​ <sup>1</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| Poland Central​​ <sup>1</sup> |  | ✅ | ✅ |  |  | ✅ |
+| Spain Central <sup>3</sup> |  |  | ✅ |  | ✅ | ✅ |
+| Sweden Central​​ <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Switzerland North​ <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Switzerland West​ | ✅ | ✅ | ✅ |  | ✅ |  |
 | UK South​ <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| UK West​ ​|  |  | ✅ |  | ✅ |  |
-| West Europe​​ <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
+| UK West​ ​|  | ✅ | ✅ |  |  |  |
+| West Europe​​ <sup>1</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 
 <sup>1</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
 
-<sup>2</sup> This region is experiencing capacity constraints that prevent the creation of new search services. Please choose a different region.
+<sup>2</sup> This region is in high demand, which prevents the creation of new search services. Please choose a different region.
 
 <sup>3</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
 
 ### Middle East
 
-| Region | AI enrichment | Availability zones | Agentic retrieval | Confidential computing | Semantic ranker | Query rewrite |
+| Region | AI enrichment | Agentic retrieval | Semantic ranker | Serverless | Availability zones | Query rewrite |
 |--|--|--|--|--|--|--|
-| Israel Central​ <sup>1</sup> |  | ✅ |  |  |  |  |
+| Israel Central​ <sup>1</sup> |  |  |  |  | ✅ |  |
 | Qatar Central​ <sup>1</sup> |  | ✅ | ✅ |  | ✅ | ✅ |
-| UAE North​​ <sup>2</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
+| UAE North​​ <sup>2, 3</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 
 <sup>1</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
 
-<sup>2</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
+<sup>2</sup> This region is in high demand, which prevents the creation of new search services. Please choose a different region.
+
+<sup>3</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
 
 ### Africa
 
-| Region | AI enrichment | Availability zones | Agentic retrieval | Confidential computing | Semantic ranker | Query rewrite |
+| Region | AI enrichment | Agentic retrieval | Semantic ranker | Serverless | Availability zones | Query rewrite |
 |--|--|--|--|--|--|--|
-| South Africa North​ <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
+| South Africa North​ <sup>1</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 
 <sup>1</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
 
 ### Asia Pacific
 
-| Region | AI enrichment | Availability zones | Agentic retrieval | Confidential computing | Semantic ranker | Query rewrite |
+| Region | AI enrichment | Agentic retrieval | Semantic ranker | Serverless | Availability zones | Query rewrite |
 |--|--|--|--|--|--|--|
 | Australia East​ <sup>1</sup> ​| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| Australia Southeast​​​ |  |  | ✅ |  | ✅ |  |
-| Central India | ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| Australia Southeast​​​ |  | ✅ | ✅ |  |  |  |
+| Central India | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | East Asia​ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
-| Indonesia Central |  | ✅ |  |  |  |  |
-| Jio India West​​ | ✅ |  | ✅ |  | ✅ | ✅ |
+| Indonesia Central |  |  |  |  | ✅ |  |
+| Jio India West​​ | ✅ | ✅ | ✅ |  |  | ✅ |
 | Jio India Central​​ |  |  |  |  |  |  |
-| Japan East <sup>1</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
-| Japan West​ | ✅ |  | ✅ |  | ✅ | ✅ |
-| Korea Central <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| Korea South​​ |  |  | ✅ |  | ✅ |  |
-| Malaysia West |  | ✅ |  |  |  |  |
-| New Zealand North |  | ✅ |  |  |  |  |
-| South India |  | ✅ |  |  |  |  |
+| Japan East <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
+| Japan West​ | ✅ | ✅ | ✅ |  |  | ✅ |
+| Korea Central <sup>1</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| Korea South​​ |  | ✅ | ✅ |  |  |  |
+| Malaysia West |  |  |  |  | ✅ |  |
+| New Zealand North |  |  |  |  | ✅ |  |
+| South India |  |  |  |  | ✅ |  |
 | Southeast Asia​​ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 
 <sup>1</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
 
 ## Azure Government regions
 
-| Region | AI enrichment | Availability zones | Agentic retrieval | Confidential computing | Semantic ranker | Query rewrite |
+| Region | AI enrichment | Agentic retrieval | Semantic ranker | Serverless | Availability zones | Query rewrite |
 |--|--|--|--|--|--|--|
-| Arizona | ✅ |  | ✅ |  | ✅ | ✅ |
+| Arizona | ✅ | ✅ | ✅ |  |  | ✅ |
 | Texas |  |  |  |  |  |  |
 | Virginia | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 
 ## Azure operated by 21Vianet
 
-| Region | AI enrichment <sup>1</sup> | Availability zones | Agentic retrieval | Confidential computing | Semantic ranker | Query rewrite |
+| Region | AI enrichment <sup>1</sup> | Agentic retrieval | Semantic ranker | Serverless | Availability zones | Query rewrite |
 |--|--|--|--|--|--|--|
 | China East |  |  |  |  |  |  |
 | China East 2 <sup>2</sup> | ✅ |  |  |  |  |  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サポートされるリージョンに関する更新"
}
```

### Explanation
この変更では、Azure AI Searchに関連するサポートされるリージョンに関する文書が更新されました。主な変更点には、各リージョンの新しい機能のサポート状況の追加、日付の更新、およびテーブル形式の整形が含まれています。この差分では、特に「機密コンピューティング」や「サーバーレス料金モデル」についての情報が具体的に各リージョンに追加され、どのリージョンが特定の機能をサポートしているかが明確に示されています。

具体的には、以下の点が更新されました：
- `ms.date`フィールドが2026年7月13日から2026年8月24日に変更されました。
- 機密コンピューティングの使用可能性が多くのリージョンにわたって具体的に記載されています。
- サーバーレス料金モデル、エージェントリトリーバル、およびセマンティックランカーに関する情報が整理され、新しい形式でまとめられています。

これにより、ユーザーは各リージョンにおける機能の利用可能性をより簡単に確認できるようになっています。


