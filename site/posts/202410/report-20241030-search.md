---
date: '2024-10-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d84fb33...MicrosoftDocs:a68723c
summary: このコード変更では、Azure AI Searchに関するドキュメントの複数のセクションの情報が更新され、トレーニングリソースや信頼性、同義語の使用、セマンティックランカーの管理が強化されました。具体的には、新しい学習パスとトレーニングモジュールが追加され、同義語マップの作成手順も充実。信頼性向上のためのガイドラインやセマンティックランカーの手順が改訂され、正確さを高めるために見出しが変更されました。この更新は、ユーザー体験の向上や検索精度の向上につながる重要な要素を多く含んでいます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d84fb33...MicrosoftDocs:a68723c){target="_blank"}

# ハイライト
このコード変更は、Azure AI Searchに関するドキュメントの複数のセクションにおいて、トレーニングリソースや信頼性、同義語の使用、セマンティックランカーの管理に関する情報の更新を行っています。また、ドキュメントの見出しも一部変更され、正確さを高めています。

## 新機能
- 新しい学習パスとトレーニングモジュールがAzure AI Searchのトレーニングリソースに追加されました。
- 同義語マップの作成手順や特典の詳細が充実されました。

## 破壊的変更
- 特に無し。

## その他の更新
- 信頼性向上のためのガイドラインが増補されました。
- セマンティックランカーの有効化と無効化の手順がより分かりやすく改訂されました。
- トピック名の変更と、ドキュメント更新による最新の日付への更新。

# 洞察
Azure AI Searchドキュメントのこの更新は、ユーザー体験を向上させるための重要な要素を多く含んでいます。特に、トレーニングリソースの拡充は、Azure AI Searchに関心を持つ開発者やエンジニアにとって貴重なリソースの提供として期待されます。学習パスや新しいモジュールの導入によって、ユーザーは段階的にスキルを習得することができ、実践的な知識を深める手助けとなります。

信頼性に関するセクションの更新は、Azure AI Searchのサービス利用における安心感を高めるものであり、サービスの可用性とデータの保護に関する戦略が明確に示されています。これに関連して、災害復旧の戦略や複数リージョンへのサービス展開についても詳細が補完され、ユーザーがこれらのポイントを理解しやすいよう工夫されています。

同義語機能についての更新は、検索の精度と利便性の向上に寄与します。この機能を活用することにより、検索結果の質を高め、ユーザー満足度を向上させることが可能です。特に、同義語マップの作成や扱いに関する具体的な情報が追加された点は、多くの利用者が直面するクエリの問題を解決する助けとなります。

さらに、セマンティックランカーの設定管理が明文化され、実際の活用にあたってのハードルが低減されています。これにより、ユーザーは自身のニーズに合わせて検索精度をコントロールすることができます。

全体として、この小規模な更新は細やかな改善を通じてAzure AI Searchの使用をより直感的で効果的なものにしており、ユーザーの技術的な成功に寄与する多岐にわたるサポートを提供しています。これらのドキュメントを頻繁に更新することで、常に最新の技術動向に基づいた知識提供が可能となっている点も重要です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [resource-training.md](#item-07788d) | minor update | 検索リソーストレーニングに関する更新 | modified | 30 | 7 | 37 | 
| [search-reliability.md](#item-3e9b1a) | minor update | Azure AI Searchの信頼性に関する文書更新 | modified | 22 | 23 | 45 | 
| [search-synonyms.md](#item-2d5d63) | minor update | 検索クエリ拡張のための同義語の追加 | modified | 23 | 21 | 44 | 
| [semantic-how-to-enable-disable.md](#item-71ac1e) | minor update | セマンティックランカーの有効化と無効化に関する手順の更新 | modified | 14 | 13 | 27 | 
| [toc.yml](#item-c4768f) | minor update | トピック名の変更: 可用性と復旧から信頼性と復旧へ | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/resource-training.md{#item-07788d}

<details>
<summary>Diff</summary>
````diff
@@ -7,20 +7,43 @@ manager: nitinme
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 05/22/2024
+ms.date: 10/28/2024
 ---
 
 # Training - Azure AI Search
 
 Training modules deliver an end-to-end experience that helps you build skills and develop insights while working through a progression of exercises. Visit the following links to begin learning with prepared lessons from Microsoft and other training providers.
 
-+ [Fundamentals of Knowledge Mining and Azure AI Search](/training/modules/intro-to-azure-search/)
+## Learning paths
+
+Learning paths are a collection of training modules that are organized around specific roles (like developer) or technologies (like Azure AI Search). Azure AI Search is covered in two learning paths.
+
++ [Microsoft Azure AI Fundamentals: Document Intelligence and Knowledge Mining](/training/paths/document-intelligence-knowledge-mining/) includes two modules: [Fundamentals of Azure AI Search and knowledge mining](/training/modules/intro-to-azure-search/) and [Fundamentals of Azure AI Document Intelligence](/training/modules/analyze-receipts-form-recognizer/). Choose this learning path to broaden your understanding of when to use each technology.
+
++ [Implement knowledge mining with Azure AI Search](/training/paths/implement-knowledge-mining-azure-cognitive-search/) includes eight modules that teach important skills. Choose this learning path to gain expertise in Azure AI Search.
+
+## Modules
+
+| Module | Learning path |
+|--------|---------------|
+[Fundamentals of Knowledge Mining and Azure AI Search](/training/modules/intro-to-azure-search/) | [Microsoft Azure AI Fundamentals:](/training/paths/document-intelligence-knowledge-mining/) |
+| [Create an Azure AI Search solution](/training/modules/create-azure-cognitive-search-solution/) | [Implement knowledge mining](/training/paths/implement-knowledge-mining-azure-cognitive-search/) |
+| [Create a custom skill for Azure AI Search](/training/modules/create-azure-ai-custom-skill/) | [Implement knowledge mining](/training/paths/implement-knowledge-mining-azure-cognitive-search/) |
+| [Build an Azure Machine Learning custom skill for Azure AI Search](/training/modules/build-azure-machine-learn-custom-skill-for-azure-cognitive-search/) | |
+| [Enrich your data with Azure AI Language](/training/modules/enrich-search-index-using-language-studio/) | |
+| [Create a knowledge store with Azure AI Search](/training/modules/create-knowledge-store-azure-cognitive-search/) | [Implement knowledge mining](/training/paths/implement-knowledge-mining-azure-cognitive-search/) |
+| [Implement advanced search features in Azure AI Search](/training/modules/implement-advanced-search-features-azure-cognitive-search/)| [Implement knowledge mining](/training/paths/implement-knowledge-mining-azure-cognitive-search/) |
+| [Search data outside the Azure platform in Azure AI Search using Azure Data Factory](/training/modules/search-data-outside-azure-platform-cognitive-search/) | [Implement knowledge mining](/training/paths/implement-knowledge-mining-azure-cognitive-search/) |
+| [Perform vector search and retrieval in Azure AI Search](/training/modules/improve-search-results-vector-search/) | [Implement knowledge mining](/training/paths/implement-knowledge-mining-azure-cognitive-search/) |
+| [Perform search reranking with semantic ranking in Azure AI Search](/training/modules/use-semantic-search/) | [Implement knowledge mining](/training/paths/implement-knowledge-mining-azure-cognitive-search/) |
+| [Maintain an Azure AI Search solution](/training/modules/maintain-azure-cognitive-search-solution/) | [Implement knowledge mining](/training/paths/implement-knowledge-mining-azure-cognitive-search/) |
+
+## RAG-centric modules
+
 + [Build a RAG-based copilot solution with your own data using Azure AI Studio](/training/modules/build-copilot-ai-studio/)
-+ [Create a custom skill for Azure AI Search](/training/modules/create-enrichment-pipeline-azure-cognitive-search/)
 + [Implement Retrieval Augmented Generation (RAG) with Azure OpenAI Service](/training/modules/use-own-data-azure-openai/)
-+ [Implement knowledge mining with Azure AI Search (Microsoft)](/training/paths/implement-knowledge-mining-azure-cognitive-search/)
-+ [Implement advanced search features in Azure AI Search](/training/modules/implement-advanced-search-features-azure-cognitive-search/)
-+ [Perform vector search and retrieval in Azure AI Search](/training/modules/improve-search-results-vector-search/)
-+ [Perform search re-ranking with semantic ranking in Azure AI Search](/training/modules/use-semantic-search/)
+
+## Pluralsight training
+
 + [Add search to apps (Pluralsight)](https://www.pluralsight.com/courses/azure-adding-search-abilities-apps)
 + [Developer course (Pluralsight)](https://www.pluralsight.com/courses/microsoft-azure-textual-content-search-enabling) 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索リソーストレーニングに関する更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchに関するトレーニングリソースを含むドキュメントの更新を示しています。具体的には、文書のいくつかのセクションが追加され、新しい学習パスやモジュールが紹介されています。更新内容には、学習パスについての異なる側面や、特定の技術を対象としたトレーニングモジュールの詳細が含まれており、これによりユーザーはAzure AI Searchをより深く理解し、スキルを向上させることができるようになります。また、文書の日付が2024年5月22日から2024年10月28日へ変更されており、資料の最新性が保持されています。新しく追加された内容には、各モジュールや関連するトレーニングパスの詳細情報が含まれています。

## articles/search/search-reliability.md{#item-3e9b1a}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,12 @@
 ---
 title: Reliability in Azure AI Search
 titleSuffix: Azure AI Search
-description: Find out about reliability in Azure AI Search.
+description: Learn how to improve the reliability and availability of Azure AI Search services.
 author: mattgotteiner
 ms.author: magottei
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 09/04/2024
+ms.date: 10/29/2024
 ms.custom:
   - subject-reliability
   - references_regions
@@ -21,7 +21,7 @@ Across Azure, [reliability](/azure/reliability/overview) means resiliency and av
 
 + Deploy multiple search services across different geographic regions. All search workloads are fully contained within a single service that runs in a single geographic region, but in a multi-service scenario, you have options for synchronizing content so that it's the same across all services. You can also set up a load balancing solution to redistribute requests or fail over if there's a service outage.
 
-For business continuity and recovery from disasters at a regional level, plan on a cross-regional topology, consisting of multiple search services having identical configuration and content. Your custom script or code provides the "fail over" mechanism to an alternate search service if one suddenly becomes unavailable.
+For business continuity and recovery from disasters at a regional level, plan on a cross-regional topology, consisting of multiple search services having identical configuration and content. Your custom script or code provides the *fail over* mechanism to an alternate search service if one suddenly becomes unavailable.
 
 <a name="scale-for-availability"></a>
 
@@ -31,27 +31,27 @@ In Azure AI Search, replicas are copies of your index. A search service is commi
 
 For each individual search service, Microsoft guarantees at least 99.9% availability for configurations that meet these criteria:
 
-+ Two replicas for high availability of read-only workloads (queries)
++ Two replicas for high availability of *read-only* workloads (queries)
 
-+ Three or more replicas for high availability of read-write workloads (queries and indexing) 
++ Three or more replicas for high availability of *read-write* workloads (queries and indexing) 
 
 The system has internal mechanisms for monitoring replica health and partition integrity. If you provision a specific combination of replicas and partitions, the system ensures that level of capacity for your service.
 
-No SLA is provided for the Free tier. For more information, see [SLA for Azure AI Search](https://azure.microsoft.com/support/legal/sla/search/v1_0/).
+No Service Level Agreement (SLA) is provided for the *Free* tier. For more information, see the [SLA for Azure AI Search](https://azure.microsoft.com/support/legal/sla/search/v1_0/).
 
 <a name="availability-zones"></a>
 
 ## Availability zone support
 
-[Availability zones](/azure/availability-zones/az-overview) are an Azure platform capability that divides a region's data centers into distinct physical location groups to provide high-availability, within the same region. In Azure AI Search, individual replicas are the units for zone assignment. A search service runs within one region; its replicas run in different physical data centers (or zones) within that region.
+[Availability zones](/azure/availability-zones/az-overview) are an Azure platform capability that divides a region's data centers into distinct physical location groups to provide high availability, within the same region. In Azure AI Search, individual replicas are the units for zone assignment. A search service runs within one region; its replicas run in different physical data centers (or zones) within that region.
 
 Availability zones are used when you add two or more replicas to your search service. Each replica is placed in a different availability zone within the region. If you have more replicas than available zones in the search service region, the replicas are distributed across zones as evenly as possible. There's no specific action on your part, except to [create a search service](search-create-service-portal.md) in a region that provides availability zones, and then to configure the service to [use multiple replicas](search-capacity-planning.md#adjust-capacity).
 
 ### Prerequisites
 
-+ Service tier must be Standard or higher.
-+ Service region must be in a region that has available zones (listed in the following section).
-+ Configuration must include multiple replicas: two for read-only query workloads, three for read-write workloads that include indexing.
++ Service tier must be *Standard* or higher
++ Service region must be in a region that has available zones (listed in the following section)
++ Configuration must include multiple replicas: two for read-only query workloads, three for read-write workloads that include indexing
 
 ### Supported regions
 
@@ -61,7 +61,7 @@ Support for availability zones depends on infrastructure and storage. Currently,
 
 Otherwise, availability zones for Azure AI Search are supported in the following regions:
 
-| Region | Roll out |
+| Region | Roll out date |
 |--------|-----------|
 | Australia East | January 30, 2021 or later |
 | Brazil South |  May 2, 2021 or later |
@@ -94,13 +94,13 @@ Otherwise, availability zones for Azure AI Search are supported in the following
 | West US 3 | June 02, 2021 or later |
 
 > [!NOTE]
-> Availability zones don't change the terms of the [Azure AI Search Service Level Agreement](https://azure.microsoft.com/support/legal/sla/search/v1_0/). You still need three or more replicas for query high availability.
+> Availability zones don't change the terms of the [SLA](https://azure.microsoft.com/support/legal/sla/search/v1_0/). You still need three or more replicas for query high availability.
 
 ## Multiple services in separate geographic regions
 
 Service redundancy is necessary if your operational requirements include:
 
-+ [Business continuity and disaster recovery (BCDR) requirements](/azure/availability-zones/cross-region-replication-azure) (Azure AI Search doesn't provide instant failover if there's an outage).
++ [Business continuity and disaster recovery (BCDR) requirements](/azure/reliability/disaster-recovery-overview). Azure AI Search doesn't provide instant failover if there's an outage.
 
 + Fast performance for a globally distributed application. If query and indexing requests come from all over the world, users who are closest to the host data center experience faster performance. Creating more services in regions with close proximity to these users can equalize performance for all users.
 
@@ -110,7 +110,7 @@ Azure AI Search doesn't provide an automated method of replicating search indexe
 
 The goal of a geo-distributed set of search services is to have two or more indexes available in two or more regions, where a user is routed to the Azure AI Search service that provides the lowest latency:
 
-   ![Cross-tab of services by region][1]
+   ![Diagram showing cross-tab view of services by region.][1]
 
 You can implement this architecture by creating multiple services and designing a strategy for data synchronization. Optionally, you can include a resource like Azure Traffic Manager for routing requests. 
 
@@ -134,7 +134,7 @@ If you're already using indexer on one service, you can configure a second index
 
 Here's a high-level visual of what that architecture would look like.
 
-![Single data source with distributed indexer and service combinations][2]
+![Diagram showing a single data source with distributed indexer and service combinations.][2]
 
 #### Option 2: Use REST APIs for pushing content updates on multiple services
 
@@ -164,39 +164,38 @@ Azure Traffic Manager is primarily used for routing network traffic across diffe
 
 Traffic Manager doesn't provide an endpoint for a direct connection to Azure AI Search, which means you can't put a search service directly behind Traffic Manager. Instead, the assumption is that requests flow to Traffic Manager, then to a search-enabled web client, and finally to a search service on the backend. The client and service are located in the same region. If one search service goes down, the search client starts failing, and Traffic Manager redirects to the remaining client.
 
-![Search apps connecting through Azure Traffic Manager][4]
+![Diagram of search apps connecting through Azure Traffic Manager.][4]
 
-## About data residency in a multi-region deployment
+## Data residency in a multi-region deployment
 
 When you deploy multiple search services in various geographic regions, your content is stored in the region you chose for each search service.
 
-Azure AI Search won't store data outside of your specified region without your authorization. Authorization is implicit when you use features that write to an Azure Storage resource: [enrichment cache](cognitive-search-incremental-indexing-conceptual.md), [debug session](cognitive-search-debug-session.md), [knowledge store](knowledge-store-concept-intro.md). In all cases, the storage account is one that you provide, in the region of your choice. 
+Azure AI Search doesn't store data outside of your specified region without your authorization. Authorization is implicit when you use features that write to an Azure Storage resource: [enrichment cache](cognitive-search-incremental-indexing-conceptual.md), [debug session](cognitive-search-debug-session.md), [knowledge store](knowledge-store-concept-intro.md). In all cases, the storage account is one that you provide, in the region of your choice. 
 
 > [!NOTE]
 > If both the storage account and the search service are in the same region, network traffic between search and storage uses a private IP address and occurs over the Microsoft backbone network. Because private IP addresses are used, you can't configure IP firewalls or a private endpoint for network security. Instead, use the [trusted service exception](search-indexer-howto-access-trusted-service-exception.md) as an alternative when both services are in the same region. 
 
 ## About service outages and catastrophic events
 
-As stated in the [Service Level Agreement (SLA)](https://azure.microsoft.com/support/legal/sla/search/v1_0/), Microsoft guarantees a high level of availability for index query requests when an Azure AI Search service instance is configured with two or more replicas, and index update requests when an Azure AI Search service instance is configured with three or more replicas. However, there's no built-in mechanism for disaster recovery. If continuous service is required in the event of a catastrophic failure outside of Microsoft’s control, we recommend provisioning a second service in a different region and implementing a geo-replication strategy to ensure indexes are fully redundant across all services.
+As stated in the [SLA](https://azure.microsoft.com/support/legal/sla/search/v1_0/), Microsoft guarantees a high level of availability for index query requests when an Azure AI Search service instance is configured with two or more replicas, and index update requests when an Azure AI Search service instance is configured with three or more replicas. However, there's no built-in mechanism for disaster recovery. If continuous service is required in the event of a catastrophic failure outside of Microsoft’s control, we recommend provisioning a second service in a different region and implementing a geo-replication strategy to ensure indexes are fully redundant across all services.
 
 Customers who use [indexers](search-indexer-overview.md) to populate and refresh indexes can handle disaster recovery through geo-specific indexers that retrieve data from the same data source. Two services in different regions, each running an indexer, could index the same data source to achieve geo-redundancy. If you're indexing from data sources that are also geo-redundant, remember that Azure AI Search indexers can only perform incremental indexing (merging updates from new, modified, or deleted documents) from primary replicas. In a failover event, be sure to redirect the indexer to the new primary replica. 
 
-If you don't use indexers, you would use your application code to push objects and data to different search services in parallel. For more information, see [Keep data synchronized across multiple services](#data-sync).
+If you don't use indexers, you would use your application code to push objects and data to different search services in parallel. For more information, see [Synchronize data across multiple services](#data-sync).
 
 ## Back up and restore alternatives
 
 A business continuity strategy for the data layer usually includes a restore-from-backup step. Because Azure AI Search isn't a primary data storage solution, Microsoft doesn't provide a formal mechanism for self-service backup and restore. However, you can use the **index-backup-restore** sample code in this [Azure AI Search .NET sample repo](https://github.com/Azure-Samples/azure-search-dotnet-utilities) to back up your index definition and snapshot to a series of JSON files, and then use these files to restore the index, if needed. This tool can also move indexes between service tiers.
 
 Otherwise, your application code used for creating and populating an index is the de facto restore option if you delete an index by mistake. To rebuild an index, you would delete it (assuming it exists), recreate the index in the service, and reload by retrieving data from your primary data store.
 
-## Next steps
+## Related content
 
-+ Review [Service limits](search-limits-quotas-capacity.md) to learn more about the pricing tiers and services limits for each one.
++ Review [Service limits](search-limits-quotas-capacity.md) to learn more about the pricing tiers and service limits.
 + Review [Plan for capacity](search-capacity-planning.md) to learn more about partition and replica combinations.
 + Review [Case Study: Use Cognitive Search to Support Complex AI Scenarios](https://techcommunity.microsoft.com/t5/azure-ai/case-study-effectively-using-cognitive-search-to-support-complex/ba-p/2804078) for more configuration guidance.
 
 <!--Image references-->
 [1]: ./media/search-reliability/geo-redundancy.png
 [2]: ./media/search-reliability/scale-indexers.png
-[3]: ./media/search-reliability/geo-search-traffic-mgr.png
 [4]: ./media/search-reliability/azure-function-search-traffic-mgr.png
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchの信頼性に関する文書更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchの信頼性に関するドキュメントの改訂を示しています。主な更新ポイントには、文書の説明が改善され、Azure AI Searchサービスの信頼性と可用性を向上させる方法についての指針が追加されています。また、データの保存に関するガイダンスや災害復旧の戦略に関する情報も強調されています。

具体的には、可用性を確保するためのレプリカの数や地理的なリージョンにおける複数サービスの配置の重要性が記載されています。さらに、一部のテキストが明確化され、重要なポイントを強調するために書式が変更されました。また、文書の日付も更新され、最新の情報が反映されています。全体として、この変更はAzure AI Searchを利用する顧客にとっての信頼性と可用性を向上させるための重要な情報を提供します。

## articles/search/search-synonyms.md{#item-2d5d63}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Synonyms for query expansion
+title: Add synonyms to expand queries for equivalent terms
 titleSuffix: Azure AI Search
 description: Create a synonym map to expand the scope of a search query over an Azure AI Search index. The query can search on equivalent terms provided in the synonym map, even if the query doesn't explicitly include the term.
 
@@ -10,12 +10,12 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 07/22/2024
+ms.date: 10/28/2024
 ---
 
-# Synonyms in Azure AI Search
+# Add synonyms in Azure AI Search
 
-On a search service, a synonym map associates equivalent terms, expanding the scope of a query without the user having to actually provide the term. For example, assuming "dog", "canine", and "puppy" are mapped synonyms, a query on "canine" matches on a document containing "dog". You might create multiple synonym maps for different languages, such as English and French versions, or lexicons if your content includes technical jargon, slang, or obscure terminology. 
+On a search service, a synonym map associates equivalent terms, expanding the scope of a query without the user having to actually provide the term. For example, assuming *dog*, *canine*, and *puppy* are mapped synonyms, a query on *canine* matches on a document containing *dog*. You might create multiple synonym maps for different languages, such as English and French versions, or lexicons if your content includes technical jargon, slang, or obscure terminology. 
 
 Some key points about synonym maps:
 
@@ -27,7 +27,7 @@ Some key points about synonym maps:
 
 ## Create a synonym map
 
-A synonym map consists of name, format, and rules that function as synonym map entries. The only format that is supported is `solr`, and the `solr` format determines rule construction.
+A synonym map consists of name, format, and rules that function as synonym map entries. The only format that's supported is `solr`, and the `solr` format determines rule construction.
 
 To create a synonym map, do so programmatically. The portal doesn't support synonym map definitions.
 
@@ -48,7 +48,7 @@ POST /synonymmaps?api-version=2024-07-01
 
 ### [.NET](#tab/dotnet)
 
-Use the [SynonymMap class (.NET)](/dotnet/api/azure.search.documents.indexes.models.synonymmap) and [Create a synonym map(Azure SDK sample)](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample02_Service.md#create-a-synonym-map) to create the map.
+Use the [SynonymMap class (.NET)](/dotnet/api/azure.search.documents.indexes.models.synonymmap) and [Create a synonym map (Azure SDK sample)](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample02_Service.md#create-a-synonym-map) to create the map.
 
 ### [Python](#tab/python)
 
@@ -66,21 +66,21 @@ Use the [SynonymMap interface (JavaScript)](/javascript/api/@azure/search-docume
 
 ### Define rules
 
-Mapping rules adhere to the open-source synonym filter specification of Apache Solr, described in this document: [SynonymFilter](https://cwiki.apache.org/confluence/display/solr/Filter+Descriptions#FilterDescriptions-SynonymFilter). The `solr` format supports two kinds of rules:
+Mapping rules adhere to the open-source synonym filter specification of Apache Solr, described in this document: [SynonymGraphFilter](https://cwiki.apache.org/confluence/display/solr/Filter+Descriptions#FilterDescriptions-SynonymGraphFilter). The `solr` format supports two kinds of rules:
 
 - equivalency (where terms are equal substitutes in the query)
 
 - explicit mappings (where terms are mapped to one explicit term)
 
-Each rule is delimited by the new line character (`\n`). You can define up to 5,000 rules per synonym map in a free service and 20,000 rules per map in other tiers. Each rule can have up to 20 expansions (or items in a rule). For more information, see [Synonym limits](search-limits-quotas-capacity.md#synonym-limits).
+Each rule is delimited by the new line character (`\n`). You can define up to 5,000 rules per synonym map in a free service and 20,000 rules per map in other tiers. Each rule can have up to 20 expansions, or items in a rule. For more information, see [Synonym limits](search-limits-quotas-capacity.md#synonym-limits).
 
 Query parsers automatically lower-case any upper or mixed case terms. To preserve special characters in the string, such as a comma or dash, add the appropriate escape characters when creating the synonym map.
 
 ### Equivalency rules
 
-Rules for equivalent terms are comma-delimited within the same rule. In the first example, a query on `USA` expands to `USA` OR `"United States"` OR `"United States of America"`. Notice that if you want to match on a phrase, the query itself must be a quote-enclosed phrase query.
+Rules for equivalent terms are comma-delimited within the same rule. In the first example, a query on *USA* expands to *USA* OR *"United States"* OR *"United States of America."* Notice that if you want to match on a phrase, the query itself must be a quote-enclosed phrase query.
 
-In the equivalence case, a query for `dog` expands the query to also include `puppy` and `canine`.
+In the equivalence case, a query for *dog* expands the query to also include *puppy* and *canine*.
 
 ```json
 {
@@ -96,7 +96,7 @@ In the equivalence case, a query for `dog` expands the query to also include `pu
 
 Rules for an explicit mapping are denoted by an arrow `=>`. When specified, a term sequence of a search query that matches the left-hand side of `=>` is replaced with the alternatives on the right-hand side at query time.
 
-In the explicit case, a query for `Washington`, `Wash.` or `WA` is rewritten as `WA`, and the query engine only looks for matches on the term `WA`. Explicit mapping only applies in the direction specified, and doesn't rewrite the query `WA` to `Washington` in this case.
+In the explicit case, a query for *Washington*, *Wash.* or *WA* is rewritten as *WA*, and the query engine only looks for matches on the term *WA*. Explicit mapping only applies in the direction specified, and doesn't rewrite the query *WA* to *Washington* in this case.
 
 ```json
 {
@@ -109,7 +109,7 @@ In the explicit case, a query for `Washington`, `Wash.` or `WA` is rewritten as
 
 ### Escaping special characters
 
-Synonyms are analyzed during query processing just like any other query term, which means that rules for reserved and special characters apply to the terms in your synonym map. The list of characters that requires escaping varies between the simple syntax and full syntax:
+Synonyms are analyzed during query processing just like any other query term, which means that rules for reserved and special characters apply to the terms in your synonym map. The list of characters that require escaping varies between the simple syntax and full syntax:
 
 - [simple syntax](query-simple-syntax.md)  `+ | " ( ) ' \`
 - [full syntax](query-lucene-syntax.md) `+ - & | ! ( ) { } [ ] ^ " ~ * ? : \ /`
@@ -136,7 +136,7 @@ Since the backslash is itself a special character in other languages like JSON a
 
 ## Manage synonym maps
 
-You can update a synonym map without disrupting query and indexing workloads. However, once you add a synonym map to a field, if you then delete a synonym map, any query that includes the fields in question fail with a 404 error.
+You can update a synonym map without disrupting query and indexing workloads. However, once you add a synonym map to a field, if you then delete a synonym map, any query that includes the fields in question fails with a 404 error.
 
 Creating, updating, and deleting a synonym map is always a whole-document operation. You can't update or delete parts of the synonym map incrementally. Updating even a single rule requires a reload.
 
@@ -184,10 +184,10 @@ POST /indexes?api-version=2024-07-01
 
 Use the [**SearchIndexClient**](/dotnet/api/azure.search.documents.indexes.searchindexclient) to update an index. Provide the whole index definition and include the new parameters for synonym map assignments.
 
-In this example, the "country" field has a synonymMapName property.
+In this example, the `country` field has a `synonymMapName` property.
 
 ```csharp
-// Update anindex
+// Update an index
 string indexName = "hotels";
 SearchIndex index = new SearchIndex(indexName)
 {
@@ -214,7 +214,7 @@ SearchIndex index = new SearchIndex(indexName)
 await indexClient.CreateIndexAsync(index);
 ```
 
-For more examples, see[azure-search-dotnet-samples/quickstart/v11/](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/v11).
+For more examples, see the [quickstart/v11 on GitHub](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/v11).
 
 ### [**Other SDKs**](#tab/other-sdks-assign)
 
@@ -223,7 +223,7 @@ You can use any supported SDK to update a search index. All of them provide a **
 | Azure SDK | Client | Examples |
 |-----------|--------|----------|
 | Java | [SearchIndexClient](/java/api/com.azure.search.documents.indexes.searchindexclient) | [CreateIndexExample.java](https://github.com/Azure/azure-sdk-for-java/blob/azure-search-documents_11.1.3/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateIndexExample.java) |
-| JavaScript | [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient) | [Indexes](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) |
+| JavaScript | [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient) | [JavaScript sample](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) |
 | Python | [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient) | [sample_index_crud_operations.py](https://github.com/Azure/azure-sdk-for-python/blob/7cd31ac01fed9c790cec71de438af9c45cb45821/sdk/search/azure-search-documents/samples/sample_index_crud_operations.py) |
 
 ---
@@ -238,17 +238,19 @@ Synonyms are a query expansion technique that supplements the contents of an ind
 
 For synonym-enabled fields, synonyms are subject to the same text analysis as the associated field. For example, if a field is analyzed using the standard Lucene analyzer, synonym terms are also subject to the standard Lucene analyzer at query time. If you want to preserve punctuation, such as periods or dashes, in the synonym term, apply a content-preserving analyzer on the field.
 
-Internally, the synonyms feature rewrites the original query with synonyms with the OR operator. For this reason, hit highlighting and scoring profiles treat the original term and synonyms as equivalent.
+Internally, the synonyms feature rewrites the original query with synonyms by using the OR operator. For this reason, hit highlighting and scoring profiles treat the original term and synonyms as equivalent.
 
 Synonyms apply to free-form text queries only and aren't supported for filters, facets, autocomplete, or suggestions. Autocomplete and suggestions are based only on the original term; synonym matches don't appear in the response.
 
+If you have an existing index in a development (nonproduction) environment, experiment with a small dictionary to see how the addition of synonyms changes the search experience, including impact on scoring profiles, hit highlighting, and suggestions.
+
+### Wildcard searches
+
 Synonym expansions don't apply to wildcard search terms; prefix, fuzzy, and regex terms aren't expanded.
 
 If you need to do a single query that applies synonym expansion and wildcard, regex, or fuzzy searches, you can combine the queries using the OR syntax. For example, to combine synonyms with wildcards for simple query syntax, the term would be `<query> | <query>*`.
 
-If you have an existing index in a development (nonproduction) environment, experiment with a small dictionary to see how the addition of synonyms changes the search experience, including impact on scoring profiles, hit highlighting, and suggestions.
-
-## Next steps
+## Next step
 
 > [!div class="nextstepaction"]
 > [Create a synonym map (REST API)](/rest/api/searchservice/synonym-maps/create)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索クエリ拡張のための同義語の追加"
}
```

### Explanation
このコードの変更は、Azure AI Searchにおける同義語の使用に関するドキュメントの更新を示しています。主な変更点として、文書のタイトルが「同義語によるクエリの拡張」から「同義語を追加してクエリを拡張する」に変更され、内容はより具体的に同義語マップの作成とその効果について説明しています。また、いくつかの文章が見やすくするために書式が調整されています。

更新内容には、同義語マップの作成手順、ルールの定義、特別な文字のエスケープ方法に関する詳細な情報が含まれています。また、クエリの処理時に同義語がどのように扱われるかについても説明が加えられています。さらに、同義語を使用する際の制約や、ワイルドカード検索との組み合わせについての情報も提供されており、ユーザーがより効果的に同義語機能を利用できるようになっています。全体的に、この変更はユーザーにとって検索体験を向上させるための重要な情報を提供します。

## articles/search/semantic-how-to-enable-disable.md{#item-71ac1e}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Enable or disable semantic ranker
 titleSuffix: Azure AI Search
-description: Steps for turning semantic ranker on or off in Azure AI Search.
+description: Learn how to turn semantic ranker on or off in Azure AI Search, and how to prevent others from enabling it.
 
 manager: nitinme
 author: HeidiSteen
@@ -10,16 +10,16 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 09/24/2024
+ms.date: 10/28/2024
 ---
 
 # Enable or disable semantic ranker
 
-Semantic ranker is a premium feature billed by usage. By default, semantic ranker is turned off on a new search service, but it can be enabled by anyone with **Contributor** permissions. If you don't want anyone enabling it inadvertently, you can [disable it using the REST API](#disable-semantic-ranker-using-the-rest-api).
+Semantic ranker is a premium feature billed by usage. By default, semantic ranker is turned off when you create a new search service, but anyone with *Contributor* permissions can enable it. If you don't want anyone enabling it inadvertently, you can [disable it using the REST API](#disable-semantic-ranker-using-the-rest-api).
 
 ## Check availability
 
-Check the [regions list](search-region-support.md) to see if your region is listed.
+To check if semantic ranker is available in your region, see the [Azure AI Search regions list](search-region-support.md).
 
 ## Enable semantic ranker
 
@@ -29,7 +29,7 @@ Follow these steps to enable [semantic ranker](semantic-search-overview.md) at t
 
 1. Open the [Azure portal](https://portal.azure.com).
 
-1. Navigate to your search service. On the **Overview** page, make sure the service is a billable tier, Basic or higher.
+1. Navigate to your search service. On the **Overview** page, make sure the pricing tier is set to **Basic** or higher.
 
 1. On the left-navigation pane, select **Settings** > **Semantic ranker**.
 
@@ -43,14 +43,14 @@ The free plan is capped at 1,000 queries per month. After the first 1,000 querie
 
 To enable semantic ranker using the REST API, you can use the [Create or Update Service API](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2023-11-01&tabs=HTTP#searchsemanticsearch&preserve-view=true).
 
-Management REST API calls are authenticated through Microsoft Entra ID. See [Manage your Azure AI Search service with REST APIs](search-manage-rest.md) for instructions on how to authenticate.
+Management REST API calls are authenticated through Microsoft Entra ID. For instructions on how to authenticate, see [Manage your Azure AI Search service with REST APIs](search-manage-rest.md).
 
 * Management REST API version 2023-11-01 provides the configuration property.
 
-* Owner or Contributor permissions are required to enable or disable features. 
+* *Owner* or *Contributor* permissions are required to enable or disable features. 
 
 > [!NOTE]
-> Create or Update supports two HTTP methods: PUT and PATCH. Both PUT and PATCH can be used to update existing services, but only PUT can be used to create a new service. If PUT is used to update an existing service, it replaces all properties in the service with their defaults if they are not specified in the request. When PATCH is used to update an existing service, it only replaces properties that are specified in the request. When using PUT to update an existing service, it's possible to accidentally introduce an unexpected scaling or configuration change. When enabling semantic ranking on an existing service, it's recommended to use PATCH instead of PUT.
+> Create or Update supports two HTTP methods: *PUT* and *PATCH*. Both PUT and PATCH can be used to update existing services, but only PUT can be used to create a new service. If PUT is used to update an existing service, it replaces all properties in the service with their defaults if they aren't specified in the request. When PATCH is used to update an existing service, it only replaces properties that are specified in the request. When using PUT to update an existing service, it's possible to accidentally introduce an unexpected scaling or configuration change. When enabling semantic ranking on an existing service, it's recommended to use PATCH instead of PUT.
 
 ```http
 PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2023-11-01
@@ -65,9 +65,9 @@ PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegrou
 
 ## Disable semantic ranker using the REST API
 
-To reverse feature enablement, or for full protection against accidental usage and charges, you can disable semantic ranker using the [Create or Update Service API](/rest/api/searchmanagement/services/create-or-update#searchsemanticsearch) on your search service. After the feature is disabled, any requests that include the semantic query type will be rejected.
+To turn off feature enablement, or for full protection against accidental usage and charges, you can disable semantic ranker by using the [Create or Update Service API](/rest/api/searchmanagement/services/create-or-update#searchsemanticsearch) on your search service. After the feature is disabled, any requests that include the semantic query type are rejected.
 
-Management REST API calls are authenticated through Microsoft Entra ID. See [Manage your Azure AI Search service with REST APIs](search-manage-rest.md) for instructions on how to authenticate.
+Management REST API calls are authenticated through Microsoft Entra ID. For instructions on how to authenticate, see [Manage your Azure AI Search service with REST APIs](search-manage-rest.md).
 
 ```http
 PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2023-11-01
@@ -78,8 +78,9 @@ PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegrou
     }
 ```
 
-To re-enable semantic ranker, rerun the previous request, setting "semanticSearch" to either "free" (default) or "standard".
+To re-enable semantic ranker, run the previous request again and set `semanticSearch` to either **Free** (default) or **Standard**.
 
-## Next steps
+## Next step
 
-[Configure semantic ranker](semantic-how-to-configure.md) so that you can test out semantic ranking on your content.
+> [!div class="nextstepaction"]
+> [Configure semantic ranker](semantic-how-to-configure.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーの有効化と無効化に関する手順の更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchにおけるセマンティックランカーの有効化および無効化に関するドキュメントの改訂を示しています。主な内容には、セマンティックランカーの機能が新しい検索サービスを作成する際にデフォルトで無効化されていると同時に、許可されたユーザーによって容易に有効化できることが強調されています。また、誤って有効化されないようにするための手順も紹介されています。

具体的には、サービスが利用可能なリージョンの確認方法、セマンティックランカーの有効化手順、およびREST APIを通じた無効化方法に関する記述が更新されています。さらに、REST APIの認証方法に関する情報も整理され、利用可能なHTTPメソッド（PUTおよびPATCH）の使用に関する注意点が強調されています。全体として、この変更はユーザーがAzure AI Searchのセマンティックランカー機能をより効果的に管理できるようにするための重要な情報を提供します。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -199,7 +199,7 @@ items:
       href: search-capacity-planning.md
     - name: Plan and manage costs
       href: search-sku-manage-costs.md
-    - name: Availability and recovery
+    - name: Reliability and recovery
       href: search-reliability.md
     - name: Availability migration guidance
       href: /azure/reliability/migrate-search-service
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピック名の変更: 可用性と復旧から信頼性と復旧へ"
}
```

### Explanation
このコードの変更は、Azure AI Searchに関するトピックの見出しを更新しています。具体的には、「可用性と復旧」という項目名が「信頼性と復旧」に変更されました。この変更は、ドキュメントの内容をより正確に反映させることを目的としており、信頼性に関連する情報が強調されています。全体として、この小さな更新は、ユーザーが関連情報を見つけやすくするための改善として機能します。


