---
date: '2026-04-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a39b296...MicrosoftDocs:a69d470
summary: このドキュメントの更新では、Azure AI 検索に関するガイドが最新情報に基づき修正され、新機能の追加や情報の精度向上が行われました。新しいREST
  APIのプレビューや顧客管理鍵の強化が含まれ、セキュリティ管理が容易になりました。APIバージョンの更新に伴う注意点も示されており、ドキュメント日付の更新や「What's
  New」セクションへのリンク整理も行われています。これらの変更により、開発者にとっての利便性と安全性が向上し、Azure AI 検索の信頼性が強化されました。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a39b296...MicrosoftDocs:a69d470){target="_blank"}

<format>
# Highlights
このドキュメントの更新では、Azure AI 検索に関する多くのガイドが最新の情報に基づいて修正されました。いくつかのセクションでは、新機能の追加や既存情報の精度向上が図られています。また、日付の更新が各ドキュメントで行われ、新しいAPIバージョンやセキュリティ機能の管理についての推奨が提示されています。

## New features
- Azure AI 検索における新しいプレビューのREST APIが追加されました。
- 顧客管理鍵（CMK）に関する細部が強化され、利用者はセキュリティ設定を直感的に管理できるようになりました。

## Breaking changes
特に破壊的な変更はありませんが、APIバージョンの更新により、古いバージョンのAPIを使用するプロジェクトには注意が必要です。

## Other updates
- ドキュメントの日付が最新のものに更新されました。
- 「What's New」セクションへのリンクが一貫して編集され、開発者は容易に最新の情報にアクセスできるようになっています。

# Insights
これらのドキュメントの更新は、特にAzure AI 検索を使用する開発者にとって重要なものであると言えます。Azure AI 検索は、複雑なデータに対して効率的に検索を行う重要なコンポーネントであり、最新のプレビューAPIや新しい機能によってその能力が強化されます。新機能として追加された「serviceLevelEncryptionKey」や「knowledgeRetrieval」プロパティにより、ユーザーは検索システムの構築においてさらなるセキュリティと効率化を達成できます。

また、顧客管理鍵（CMK）の設定方法が詳しく説明され、デフォルトのセキュリティ設定が新しいデータオブジェクトに適用されるようになったことは、セキュリティを重要視するビジネスにとって大きな利点です。これにより、Azure AI 検索の利用はよりセキュアで使いやすくなるため、ユーザーは運用上の心配を減らし、主要なビジネス機能の改善に集中できます。

全体として、今回の更新により、動作の信頼性が向上し、最新技術を活用した効率的な検索環境が提供され、開発者をサポートするためのドキュメントの精度が向上しています。これにより、企業はデータのセキュリティと管理性を強化しながら、新機能によって競争力を高めることが可能です。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-migrate.md](#item-9653ea) | minor update | 移行手順の更新: Azure AI 検索の新機能について | modified | 2 | 2 | 4 | 
| [search-api-migration.md](#item-07297b) | minor update | Azure AI 検索 API 移行手順の更新 | modified | 3 | 3 | 6 | 
| [search-api-preview.md](#item-511f5d) | minor update | Azure AI 検索 API プレビュー機能の更新 | modified | 28 | 27 | 55 | 
| [search-indexer-how-to-access-private-sql.md](#item-1bd4cc) | minor update | プライベート SQL アクセスのためのインデクサー設定に関する更新 | modified | 4 | 4 | 8 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | プライベートリソースへのインデクサー接続に関する更新 | modified | 2 | 2 | 4 | 
| [search-security-manage-encryption-keys.md](#item-db3487) | minor update | Azure AI Search における顧客管理キーの設定に関する更新 | modified | 155 | 46 | 201 | 
| [whats-new.md](#item-fa71b4) | minor update | Azure AI Search の最新情報更新 | modified | 4 | 1 | 5 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-migrate.md{#item-9653ea}

<details>
<summary>Diff</summary>
````diff
@@ -12,10 +12,10 @@ ms.date: 03/25/2026
 
 If you wrote [agentic retrieval](agentic-retrieval-overview.md) code using an early preview REST API, this article explains when and how to migrate to a newer version. It also describes breaking and nonbreaking changes for all REST API versions that support agentic retrieval.
 
-Migration instructions are intended to help you run an existing solution on a newer API version. The instructions in this article help you address breaking changes at the API level so that your app runs as before. For help with adding new functionality, start with [What's new](whats-new.md).
+Migration instructions are intended to help you run an existing solution on a newer API version. The instructions in this article help you address breaking changes at the API level so that your app runs as before. For help with adding new functionality, start with [What's new in Azure AI Search](whats-new.md).
 
 > [!TIP]
-> Using Azure SDKs instead of REST? Read this article to learn about breaking changes, and then install a newer preview package to begin your updates. Before you start, check the SDK change logs to confirm API updates: [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md), [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md), [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
+> Using Azure SDKs instead of REST? Read this article to learn about breaking changes, and then install a newer preview package to begin your updates. Before you start, check the SDK changelogs to confirm API updates: [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md), [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md), [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
 
 ## When to migrate
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "移行手順の更新: Azure AI 検索の新機能について"
}
```

### Explanation
この変更は、ドキュメント「agentic-retrieval-how-to-migrate.md」において、移行手順に関する情報を最新の状況に合わせて更新するものです。具体的には、APIの新しいバージョンを使用する際の移行に関する説明が加わり、特に「What's new」セクションへのリンクが「What's new in Azure AI Search」に変更されています。また、SDKの変更ログの参照が一貫した表現に修正されています。これにより、開発者はAPIの最新バージョンへの移行をより容易に理解できるようになります。

## articles/search/search-api-migration.md{#item-07297b}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: upgrade-and-migration-article
-ms.date: 12/17/2025
+ms.date: 03/30/2026
 ---
 
 # Upgrade to the latest REST API in Azure AI Search
@@ -22,9 +22,9 @@ Here are the most recent versions of the REST APIs:
 | Data plane | [`2025-09-01`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-09-01&preserve-view=true) | Stable |
 | Data plane | [`2025-11-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) | Preview |
 | Control plane | [`2025-05-01`](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2025-05-01&preserve-view=true) | Stable |
-| Control plane | [`2025-02-01-preview`](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true) | Preview |
+| Control plane | [`2026-03-01-preview`](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true) | Preview |
 
-Upgrade instructions focus on code changes that get you through breaking changes from previous versions so that existing code runs the same as before, but on the newer API version. Once your code is in working order, you can decide whether to adopt newer features. To learn more about new features, see [What's New](whats-new.md).
+Upgrade instructions focus on code changes that get you through breaking changes from previous versions so that existing code runs the same as before, but on the newer API version. Once your code is in working order, you can decide whether to adopt newer features. To learn more about new features, see [What's new in Azure AI Search](whats-new.md).
 
 We recommend upgrading API versions in succession, working through each version until you get to the newest one.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI 検索 API 移行手順の更新"
}
```

### Explanation
この変更は、「search-api-migration.md」ドキュメントに対して行われたもので、移行手順およびAPIバージョンの情報を更新するものです。主な修正点として、文書の日付が2025年12月17日から2026年3月30日に変更され、最新のREST API情報が反映されています。特に、コントロールプレーンAPIのプレビュー版が「2025-02-01-preview」から「2026-03-01-preview」に更新されました。また、「What's New」セクションへのリンクも、「What's new in Azure AI Search」に変更されています。これにより、開発者は新しいAPIバージョンへの移行手順をより正確に理解することができ、最新機能に関する情報を得る一助となります。

## articles/search/search-api-preview.md{#item-511f5d}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: concept-article
-ms.date: 12/17/2025
+ms.date: 03/30/2026
 ---
 
 # Preview features in Azure AI Search
@@ -15,21 +15,21 @@ This article identifies all data plane and control plane features in public prev
 
 Preview API versions are cumulative and roll up to the next preview. We recommend always using the latest preview APIs for full access to all preview features.
 
-Preview features are removed from this list if they're retired or transition to general availability. For announcements regarding general availability and retirement, see [Service Updates](https://azure.microsoft.com/updates/?product=search) or [What's New](whats-new.md).
+Preview features are removed from this list if they're retired or transition to general availability. For announcements regarding general availability and retirement, see [What's new in Azure AI Search](whats-new.md).
 
 ## Data plane preview features
 
 | Feature | Description | Availability |
 |--|--|--|
-| [**Agentic retrieval**](agentic-retrieval-overview.md) | Create a conversational search experience powered by large language models (LLMs). Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries simultaneously, reranks the results for relevance, and either extracts grounding data or synthesizes answers into natural language.<p>The pipeline involves one or more [knowledge sources](agentic-knowledge-source-overview.md#supported-knowledge-sources) within a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), whose [response payload](agentic-retrieval-how-to-retrieve.md) provides full transparency into the query plan and reference data.<p>To get started, see [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md) (programmatic) or [Quickstart: Agentic retrieval in the Azure portal](get-started-portal-agentic-retrieval.md). | [Knowledge Sources (preview)](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true), [Knowledge bases (preview)](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true), [Knowledge Retrieval (preview)](/rest/api/searchservice/knowledge-retrieval?view=rest-searchservice-2025-11-01-preview&preserve-view=true), and the Azure portal |
+| [**Agentic retrieval**](agentic-retrieval-overview.md) | Create a conversational search experience powered by large language models (LLMs). Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries simultaneously, reranks the results for relevance, and either extracts grounding data or synthesizes answers into natural language.<p>The pipeline involves one or more [knowledge sources](agentic-knowledge-source-overview.md#supported-knowledge-sources) within a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), whose [response payload](agentic-retrieval-how-to-retrieve.md) provides full transparency into the query plan and reference data.<p>To get started, see [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md) (programmatic) or [Quickstart: Agentic retrieval in the Azure portal](get-started-portal-agentic-retrieval.md). | [Knowledge Sources (preview)](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true), [Knowledge bases (preview)](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true), [Knowledge Retrieval (preview)](/rest/api/searchservice/knowledge-retrieval?view=rest-searchservice-2025-11-01-preview&preserve-view=true), and the Azure portal. |
 | [**Purview index configuration**](search-indexer-sensitivity-labels.md) | Apply Microsoft Purview classifications and sensitivity labels to indexed content based on source metadata for enhanced data governance. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 | [**Scoring function aggregation**](index-add-scoring-profiles.md#example-function-aggregation) | Combine and aggregate multiple scoring functions, enabling more sophisticated relevance customization and weighted signal combination. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 | [**Facet aggregations**](search-faceted-navigation-examples.md#facet-aggregation-example) | Use sum, count, minimum, maximum, and other aggregate functions to provide enhanced analytics in faceted search experiences. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 | [**Improved indexer runtime tracking information**](search-howto-run-reset-indexers.md) | Cumulative indexer processing information for the search service and for specific indexers. | [Get Service Statistics (preview)](/rest/api/searchservice/get-service-statistics/get-service-statistics?view=rest-searchservice-2025-11-01-preview&preserve-view=true) and [Get Status - Indexers (preview)](/rest/api/searchservice/get-service-statistics/get-service-statistics?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 | [**Strict postfiltering for vector queries**](vector-search-filters.md) | Adds the `strictPostFilter` mode to the `vectorFilterMode` parameter. When specified, filters are applied after the global top-`k` vector results are identified, ensuring that returned documents are a subset of the unfiltered results. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 | [**Multivector support**](vector-search-multi-vector-fields.md) | Index multiple child vectors within a single document field. You can now use vector types in nested fields of complex collections, effectively allowing multiple vectors to be associated with a single document.| [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 | [**Document-level access control**](search-document-level-access-overview.md) | Flow document-level permissions from blobs in Azure Data Lake Storage (ADLS) Gen2 to searchable documents in an index. Queries can now filter results based on user identity for selected data sources. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-| [**GenAI Prompt skill**](cognitive-search-skill-genai-prompt.md) | Skill that connects to a large language model (LLM) for information using a prompt you provide. With this skill, you can populate a searchable field using content from an LLM. A primary use case for this skill is *image verbalization*, using an LLM to describe images and send the description to a searchable field in your index. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+| [**GenAI Prompt skill**](cognitive-search-skill-genai-prompt.md) | Skill that connects to an LLM for information using a prompt you provide. With this skill, you can populate a searchable field using content from an LLM. A primary use case for this skill is *image verbalization*, using an LLM to describe images and send the description to a searchable field in your index. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 | [**flightingOptIn parameter in a semantic configuration**](semantic-how-to-configure.md#opt-in-for-prerelease-semantic-ranking-models) | Opt in to use prerelease semantic ranking models if one is available in a search service region. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true) |
 | [**Facet hierarchies, aggregations, and facet filters**](search-faceted-navigation-examples.md) | New facet query parameters support nested facets. For numeric facetable fields, you can sum the values of each field. You can also specify filters on a facet to add inclusion or exclusion criteria. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-03-01-preview&preserve-view=true) |
 | [**Query rewrite in the semantic reranker**](semantic-how-to-query-rewrite.md) | Set options on a semantic query to rewrite the query input into a revised or expanded query that generates more relevant results from the L2 ranker. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&preserve-view=true)|
@@ -42,29 +42,31 @@ Preview features are removed from this list if they're retired or transition to
 | [**Incremental enrichment cache**](enrichment-cache-how-to-configure.md) | Adds caching to an enrichment pipeline, allowing you to reuse existing output if a targeted modification, such as an update to a skillset or another object, doesn't change the content. Caching applies only to enriched documents produced by a skillset.| [Create or Update Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 |  [**Azure Files indexer**](search-file-storage-integration.md) | Data source for indexer-based indexing from [Azure Files](https://azure.microsoft.com/services/storage/files/). | [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 | [**SharePoint indexer**](search-how-to-index-sharepoint-online.md) | Data source for indexer-based indexing of SharePoint content. | [Sign up](https://aka.ms/azure-cognitive-search/indexer-preview) to enable the feature. [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) or the Azure portal. |
-|  [**MySQL indexer**](search-how-to-index-mysql.md) | Data source for indexer-based indexing of Azure MySQL data sources.| [Sign up](https://aka.ms/azure-cognitive-search/indexer-preview) to enable the feature. [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true), [.NET SDK 11.2.1](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourcetype.mysql), and Azure portal |
+|  [**MySQL indexer**](search-how-to-index-mysql.md) | Data source for indexer-based indexing of Azure MySQL data sources.| [Sign up](https://aka.ms/azure-cognitive-search/indexer-preview) to enable the feature. [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true), [.NET SDK 11.2.1](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourcetype.mysql), and Azure portal. |
 | [**Azure Cosmos DB for MongoDB indexer**](search-how-to-index-cosmosdb-sql.md) | Data source for indexer-based indexing through the MongoDB APIs in Azure Cosmos DB. | [Sign up](https://aka.ms/azure-cognitive-search/indexer-preview) to enable the feature. [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) or the Azure portal. |
 | [**Azure Cosmos DB for Apache Gremlin indexer**](search-how-to-index-cosmosdb-sql.md) | Data source for indexer-based indexing through the Apache Gremlin APIs in Azure Cosmos DB. | [Sign up](https://aka.ms/azure-cognitive-search/indexer-preview) to enable the feature. [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true). |
 | [**Native blob soft delete**](search-how-to-index-azure-blob-changed-deleted.md) | Applies to the Azure Blob Storage indexer. Recognizes blobs that are in a soft-deleted state, and removes the corresponding search document during indexing. | [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true). |
-| [**Reset Documents**](search-howto-run-reset-indexers.md) | Reprocesses individually selected search documents in indexer workloads. | [Reset Documents (preview)](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2025-11-01-preview&preserve-view=true). |
-| [**speller**](speller-how-to-add.md) | Optional spelling correction on query term inputs for simple, full, and semantic queries. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&preserve-view=true). |
+| [**Reset Documents**](search-howto-run-reset-indexers.md) | Reprocesses individually selected search documents in indexer workloads. | [Reset Documents (preview)](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+| [**speller**](speller-how-to-add.md) | Optional spelling correction on query term inputs for simple, full, and semantic queries. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 | [**featuresMode parameter**](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&preserve-view=true) | BM25 relevance score expansion to include details: per field similarity score, per field term frequency, and per field number of unique tokens matched. You can consume these data points in [custom scoring solutions](https://github.com/Azure-Samples/search-ranking-tutorial). | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&preserve-view=true)|
 | [**vectorQueries.threshold parameter**](vector-search-how-to-query.md#vector-weighting) | Exclude low-scoring search result based on a minimum score. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 | [**hybridSearch.maxTextRecallSize and countAndFacetMode parameters**](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) | Adjust the inputs to a hybrid query by controlling the amount BM25-ranked results that flow to the hybrid ranking model. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 | [**moreLikeThis**](search-more-like-this.md) | Finds documents that are relevant to a specific document. This feature has been in earlier previews. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 
 ## Control plane preview features
 
-Currently, there are no control plane features in preview.
+| Feature | Description | Availability |
+|--|--|--|
+| [**Service-level CMK**](search-security-manage-encryption-keys.md#enable-service-level-cmk-on-new-objects-by-default-preview) | Enables a customer-managed key (CMK) on all newly created objects by default. Service-level CMK ensures all sensitive data in your search service is protected by a key you control, without having to specify key information each time an object is created. | [Services - Create or Update (preview)](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true) |
 
 ## Preview features in Azure SDKs
 
-Preview features in Azure SDKs are available through preview packages. To determine which preview features are available in a specific package version, see the SDK's change log:
+Preview features in Azure SDKs are available through preview packages. To determine which preview features are available in a specific package version, see the SDK's changelog:
 
-+ [Change log for Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md)
-+ [Change log for Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md)
-+ [Change log for Azure SDK for JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md)
-+ [Change log for Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
++ [Changelog for Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md)
++ [Changelog for Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md)
++ [Changelog for Azure SDK for JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md)
++ [Changelog for Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md)
 
 ## Using preview features
 
@@ -80,18 +82,18 @@ If you write code against a preview API, you should prepare to upgrade that code
 
 ## How to call a preview REST API
 
-Preview REST APIs are accessed through the api-version parameter on the URI. Older previews are still operational but become stale over time and aren't updated with new features or bug fixes.
+Preview REST APIs are accessed through the `api-version` parameter on the URI. Although older previews are still operational, they become stale over time and aren't updated with new features or bug fixes.
 
-For data plane operations on content, [**`2025-11-01-preview`**](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) is the most recent preview version. The following example shows the syntax for [Indexes GET (preview)](/rest/api/searchservice/indexes/get?view=rest-searchservice-2025-11-01-preview&preserve-view=true):
+For data plane operations on content, [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) is the most recent preview version. The following example shows how to call [Indexes - Get](/rest/api/searchservice/indexes/get?view=rest-searchservice-2025-11-01-preview&preserve-view=true) (REST API) for this preview version.
 
-```rest
-GET {endpoint}/indexes('{indexName}')?api-version=2025-11-01-Preview
+```http
+GET {endpoint}/indexes('{indexName}')?api-version=2025-11-01-preview
 ```
 
-For management operations on the search service, [**`2025-05-01-preview`**](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2025-05-01-preview&preserve-view=true) is the most recent preview version. The following example shows the syntax for Update Service 2025-05-01-preview version.
+For management operations on the search service, [2026-03-01-preview](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true) is the most recent preview version. The following example shows how to call [Services - Update](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true) (REST API) for this preview version.
 
-```rest
-PATCH https://management.azure.com/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Search/searchServices/mysearchservice?api-version=2025-05-01-preview
+```http
+PATCH https://management.azure.com/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Search/searchServices/mysearchservice?api-version=2026-03-01-preview
 
 {
   "tags": {
@@ -104,11 +106,10 @@ PATCH https://management.azure.com/subscriptions/subid/resourceGroups/rg1/provid
 }
 ```
 
-## See also
+## Related content
 
-+ [Quickstart: Full-text search using REST APIs](search-get-started-text.md)
-+ [Search REST API overview](/rest/api/searchservice/)
-+ [Search REST API versions](/rest/api/searchservice/search-service-api-versions)
-+ [Manage using the REST APIs](search-manage-rest.md)
-+ [Management REST API overview](/rest/api/searchmanagement/)
-+ [Management REST API versions](/rest/api/searchmanagement/management-api-versions)
++ [Search Service REST API overview](/rest/api/searchservice/)
++ [Search Service REST API versions](/rest/api/searchservice/search-service-api-versions)
++ [Search Management REST API overview](/rest/api/searchmanagement/)
++ [Search Management REST API versions](/rest/api/searchmanagement/management-api-versions)
++ [Manage your Azure AI Search service using REST APIs](search-manage-rest.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI 検索 API プレビュー機能の更新"
}
```

### Explanation
この変更は、「search-api-preview.md」ドキュメントに対するもので、Azure AI 検索におけるプレビュー機能に関する情報が更新されました。主な修正内容には、文書の日付が2025年12月17日から2026年3月30日に変更されたこと、最新のプレビューAPIの情報が追加されたことがあります。特に、コントロールプレーンのプレビュー機能が新たに追加され、カスタマー管理キー（CMK）の機能が明示されました。

また、いくつかのリンクが「What's New in Azure AI Search」に変更され、利用者が新機能についての情報をより容易に得られるようになっています。全体として、この変更は開発者が最新の機能やAPI情報を把握しやすくすることを目的としており、特にプレビュー機能に関連する項目が豊富に取り上げられています。

## articles/search/search-indexer-how-to-access-private-sql.md{#item-1bd4cc}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Configure an indexer connection to access content in an Azure SQL M
 ms.reviewer: magottei
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 01/23/2026
+ms.date: 03/17/2026
 ms.update-cycle: 365-days
 ms.custom: sfi-ropc-nochange
 ---
@@ -83,10 +83,10 @@ For more information about connection properties, see [Create an Azure SQL Manag
 
 1. Call the `az rest` command to use the [Management REST API](/rest/api/searchmanagement) of Azure AI Search. 
 
-   Because shared private link support for SQL managed instances is still in preview, you need a preview version of the management REST API. Use `2021-04-01-preview` or a later preview API version for this step. We recommend using the latest preview API version.
+   Shared private link support for SQL managed instances is in preview, so you must use a preview version of the Management REST API. We recommend the latest preview API version.
 
    ```azurecli
-   az rest --method put --uri https://management.azure.com/subscriptions/{{search-service-subscription-ID}}/resourceGroups/{{search service-resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}/sharedPrivateLinkResources/{{shared-private-link-name}}?api-version=2025-05-01-preview --body @create-pe.json
+   az rest --method put --uri https://management.azure.com/subscriptions/{{search-service-subscription-ID}}/resourceGroups/{{search service-resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}/sharedPrivateLinkResources/{{shared-private-link-name}}?api-version=2026-03-01-preview --body @create-pe.json
    ```
 
    Provide the subscription ID, resource group name, and service name of your Azure AI Search resource.
@@ -186,7 +186,7 @@ An easy choice is [running an indexer](search-howto-run-reset-indexers.md) in Az
 
 Here are some reminders for testing:
 
-+ If you use a REST client, use the [Management REST API](/rest/api/searchmanagement/) and the [2021-04-01-Preview API version](/rest/api/searchmanagement/management-api-versions) to create the shared private link. Use the [Search REST API](/rest/api/searchservice/) and a [stable API version](/rest/api/searchservice/search-service-api-versions) to create and invoke indexers and data sources.
++ If you use a REST client, use the [Management REST API](/rest/api/searchmanagement/) and the [latest preview API version](/rest/api/searchmanagement/management-api-versions) to create the shared private link. Use the [Search REST API](/rest/api/searchservice/) and a [stable API version](/rest/api/searchservice/search-service-api-versions) to create and invoke indexers and data sources.
 
 + You can use the **Import data** wizard to create an indexer, data source, and index. However, the generated indexer won't have the correct execution environment setting.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベート SQL アクセスのためのインデクサー設定に関する更新"
}
```

### Explanation
この変更は、「search-indexer-how-to-access-private-sql.md」ドキュメントに対するもので、Azure SQL マネージドインスタンスにアクセスするためのインデクサー接続設定に関する情報が更新されました。具体的には、文書の日付が2026年1月23日から2026年3月17日に変更され、プレビューAPIバージョンに関する文言が明確化されています。

変更内容の一部として、SQL マネージドインスタンスの共有プライベートリンクサポートについての説明が強化され、どのプレビューAPIバージョンを使用すべきかが推奨されています。また、インデクサーやデータソースを作成する際の具体的なAPIバージョンについても、最新のプレビューAPIバージョンを使用するように推奨されています。このようにして、開発者が最新かつ適切なAPIを使用することが容易になり、ドキュメント全体の精度が向上しています。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Configure indexer connections to access content from other Azure re
 ms.reviewer: mcarter
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 01/23/2026
+ms.date: 03/17/2026
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
@@ -419,7 +419,7 @@ While both scenarios have a dependency on Azure Private Link, they're independen
 
 When evaluating shared private links for your scenario, remember these constraints:
 
-+ Several of the resource types used in a shared private link are in preview. If you're connecting to a preview resource (Azure Database for MySQL or Azure SQL Managed Instance), use a preview version of the Management REST API to create the shared private link. We recommend the [latest preview API](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true).
++ Several of the resource types used in a shared private link are in preview. If you're connecting to a preview resource (Azure Database for MySQL or Azure SQL Managed Instance), use a preview version of the Management REST API to create the shared private link. We recommend the [latest preview API version](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true).
 
 + Indexer execution must use the [private execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment) that's specific to your search service. Private endpoint connections aren't supported from the multitenant content processing environment. The configuration setting for this requirement is covered in this article.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートリソースへのインデクサー接続に関する更新"
}
```

### Explanation
この変更は、「search-indexer-howto-access-private.md」ドキュメントに対して行われたもので、Azureのプライベートリソースにアクセスするためのインデクサー接続に関する情報が更新されました。主な変更点は、文書の日付が2026年1月23日から2026年3月17日に変更されたことと、プレビューAPIに関する推奨が最新のものに更新されたことです。

具体的には、共有プライベートリンクの利用に際して、新たに接続するリソースがプレビューである場合に使用すべきManagement REST APIのバージョンについての記述が更新され、最新のプレビューAPIバージョンを推奨する形になっています。また、インデクサーの実行環境についても言及があり、プライベートエンドポイント接続がマルチテナントのコンテンツ処理環境からはサポートされない旨が説明されています。これにより、ユーザーはより正確な情報を基に設定を行うことができるようになっています。

## articles/search/search-security-manage-encryption-keys.md{#item-db3487}

<details>
<summary>Diff</summary>
````diff
@@ -1,46 +1,72 @@
 ---
-title: Encrypt Data Using Customer-Managed Keys
+title: Configure Customer-Managed Keys for Azure AI Search
 description: Supplement server-side encryption in Azure AI Search using customer managed keys (CMK) or bring your own keys (BYOK) that you create and manage in Azure Key Vault.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 09/18/2025
+ms.date: 04/07/2026
 ms.update-cycle: 365-days
 ms.custom:
   - references_regions
   - ignite-2023
   - sfi-image-nochange
 ---
 
-# Configure customer-managed keys for data encryption in Azure AI Search
+# Configure customer-managed keys for Azure AI Search encrypted data
 
-Azure AI Search automatically encrypts data at rest with [Microsoft-managed keys](/azure/security/fundamentals/encryption-atrest#azure-encryption-at-rest-components). If you need another layer of encryption or the ability to revoke keys and shut down access to content, you can use keys that you create and manage in Azure Key Vault. This article explains how to set up customer-managed key (CMK) encryption.
+Enabling customer‑managed keys (CMK) adds additional security on top of the default encryption at rest when using [Microsoft-managed keys](/azure/security/fundamentals/encryption-atrest#azure-encryption-at-rest-components). When you enable CMK, you control the encryption keys used to protect your data, including the ability to:
 
-You can store keys using either:
+- Rotate keys on a customer‑defined schedule
+- Disable or revoke keys to block access to encrypted content *(cached keys may persist for up to 60 minutes)*
+- Audit key usage through Azure Key Vault logging
+
+You can create, store, and manage keys by using either:
 
 + Azure Key Vault
 
-+ Azure Key Vault Managed HSM (Hardware Security Module). An Azure Key Vault Managed HSM is an FIPS 140-2 Level 3 validated HSM. HSM support is new in Azure AI Search. To migrate from Azure Key Vault to HSM, [rotate your keys](#rotate-or-update-encryption-keys) and choose Managed HSM for storage.
++ Azure Key Vault Managed HSM (Hardware Security Module). An Azure Key Vault Managed HSM is an FIPS 140-2 Level 3 validated HSM. To migrate from Azure Key Vault to HSM, [rotate your keys](#rotate-or-update-encryption-keys) and choose Managed HSM for storage.
 
-> [!IMPORTANT]
-> + CMK provides encryption for data at rest. If you need to protect data in use, consider using [confidential computing](search-security-best-practices.md#optional-enable-confidential-computing).
->
-> + CMK encryption is irreversible. You can rotate keys and change CMK configuration, but index encryption lasts for the lifetime of the index. Post-CMK encryption, an index is only accessible if the search service has access to the key. If you revoke access to the key by deleting or changing role assignment, the index is unusable and the service can't be scaled until the index is deleted or access to the key is restored. If you delete or rotate keys, the most recent key is cached for up to 60 minutes.
+This article explains how to configure CMK for additional protection of your encrypted data in Azure AI Search.
 
-## CMK encrypted objects
+> [!IMPORTANT]
+> + Adding a customer-managed key (CMK) applies to encryption for data at rest. If you need to protect data in use, consider using [confidential computing](search-security-best-practices.md#optional-enable-confidential-computing).
 
-CMK encryption applies to individual objects when they're created. This means you can't encrypt objects that already exist. CMK encryption occurs each time an object is saved to disk, for both data at rest (long-term storage) or temporary cached data (short-term storage). With CMK, the disk never sees unencrypted data.
+## Configure CMK on Azure AI Search objects
 
-Objects that can be encrypted include indexes, synonym lists, indexers, data sources, and skillsets. Encryption is computationally expensive to decrypt so only sensitive content is encrypted.
+Objects with encrypted data that can be configured with a customer-managed key (CMK) include indexes, synonym lists, indexers, data sources, vectorizers, and skillsets. Encryption is computationally expensive to decrypt so only sensitive content is encrypted.
 
-Encryption is performed over the following content:
+Encryption is performed over:
 
 + All content within indexes and synonym lists.
 
 + Sensitive content in indexers, data sources, skillsets, and vectorizers. Sensitive content refers to connection strings, descriptions, identities, keys, and user inputs. For example, skillsets have Foundry Tools keys, and some skills accept user inputs, such as custom entities. In both cases, keys and user inputs are encrypted. Any references to external resources (such as Azure data sources or Azure OpenAI models) are also encrypted.
 
-If you require CMK across your search service, [set an enforcement policy](#set-up-a-policy-to-enforce-cmk-compliance).
+Adding a customer-managed key to an object must happen when the object is newly created. It is important to keep in mind:
+
+- You cannot retroactively add CMK to an existing object. If you want to add a customer-managed key to an existing object, you must delete and recreate that object with encryption enabled.
+
+- Once CMK is configured, encryption happens every time the service writes data, including both data at rest (long-term storage) or temporary cached data (short-term storage). For objects like data sources, indexers, and skillsets, the object definition is encrypted. For indexes, the indexed documents themselves (not just the index schema) are encrypted.
+
+- Although you can't add encryption to an existing object, once an object is configured for encryption, you can change all parts of its encryption definition, including switching to a different key vault or HMS storage as long as the resource is in the same tenant.
+
+- Encryption with a CMK is irreversible. You can rotate keys and change CMK configuration, but index encryption lasts for the lifetime of the index. After encryption with CMK, an index is only accessible if the search service has access to the key. If you revoke access to the key by deleting or changing role assignment, the index is unusable and the service can't be scaled until the index is deleted or access to the key is restored. If you delete or rotate keys, the most recent key is cached for up to 60 minutes.
+
+- If you require CMK across your search service, [set an enforcement policy](#set-up-a-policy-to-enforce-cmk-compliance).
 
-Although you can't add encryption to an existing object, once an object is configured for encryption, you can change all parts of its encryption definition, including switching to a different key vault or HMS storage as long as the resource is in the same tenant.
+- CMK enforcement by using Azure Policy and service-level CMK configuration (which is still in preview) are independent settings. You can use either or both, depending on your needs. Service-level CMK configuration applies a default key to new objects, while Azure Policy enforcement ensures that all objects comply with your encryption requirements. If you enable a CMK enforcement policy without a service‑level key, all CMK‑enabled objects must specify their own encryption key at creation time. Object creation requests that omit CMK configuration fail.
+
+## Enable service-level CMK on new objects by default (preview)
+
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+Beginning in the 2026-03-01-preview release, you have the ability to configure a customer-managed key at the **service-level** on the Azure AI Search service itself. This feature makes it possible to configure the key once at the service level and have it apply to all newly created objects by default. This ensures all sensitive data in your search service is protected by a key you control, without having to specify key information each time an object is created.
+
+Enabling CMK at the service level means:
+
+- All **new** objects created on your Azure AI Search service automatically use the service‑level customer‑managed key by default, so you no longer need to explicitly specify encryption key details each time you create an object.
+
+- This feature is optional, and you can continue to configure CMK on a per‑object basis. You can also override the service‑level key for individual objects and rotate the service‑level key independently, allowing you to use different keys for different objects as needed.
+
+You can also rotate this default key by specifying a new key, specific to the object that you are creating. The object-level key that you specify will override the default service-level key for that object.
 
 ## Prerequisites
 
@@ -92,7 +118,7 @@ To generate or import a key, use the [Azure CLI](/azure/key-vault/managed-hsm/ke
 
 Create a security principal that your search service uses to access to the encryption key. You can use a managed identity and role assignment, or you can register an application and have the search service provide the application ID on requests.
 
-We recommend using a managed identity and roles. You can use either a system-managed identity or user-managed identity. A managed identity enables your search service to authenticate through Microsoft Entra ID, without storing credentials (ApplicationID or ApplicationSecret) in code. The lifecycle of this type of managed identity is tied to the lifecycle of your search service, which can only have one system assigned managed identity. For more information about how managed identities work, see [What are managed identities for Azure resources](/azure/active-directory/managed-identities-azure-resources/overview).
+Use a managed identity and roles. You can use either a system-managed identity or user-managed identity. A managed identity enables your search service to authenticate through Microsoft Entra ID, without storing credentials (ApplicationID or ApplicationSecret) in code. The lifecycle of this type of managed identity is tied to the lifecycle of your search service, which can only have one system assigned managed identity. For more information about how managed identities work, see [What are managed identities for Azure resources](/azure/active-directory/managed-identities-azure-resources/overview).
 
 ### [**System-managed identity**](#tab/managed-id-sys)
 
@@ -112,17 +138,17 @@ Follow these instructions if you can't use role assignments for search service a
 
 1. On the left, under **Manage**, select **App registrations**, and then select **New registration**.
 
-1. Give the registration a name, perhaps a name that is similar to the search application name. Select **Register**.
+1. Enter a name for the registration, such as a name that's similar to the search application name. Select **Register**.
 
-1. Once the app registration is created, copy the Application ID. You need to provide this string to your application. 
+1. After the app registration is created, copy the Application ID. Provide this string to your application. 
 
    If you're stepping through the [DotNetHowToEncryptionUsingCMK](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToEncryptionUsingCMK), paste this value into the **appsettings.json** file.
 
    :::image type="content" source="media/search-manage-encryption-keys/cmk-application-id.png" alt-text="Application ID in the Essentials section":::
 
 1. Next, select **Certificates & secrets**.
 
-1. Select **New client secret**. Give the secret a display name and select **Add**.
+1. Select **New client secret**. Enter a display name for the secret and select **Add**.
 
 1. Copy the application secret. If you're stepping through the sample, paste this value into the **appsettings.json** file.
 
@@ -151,19 +177,25 @@ Role-based access control is recommended over the Access Policy permission model
 
 Wait a few minutes for the role assignment to become operational.
 
-## Step 4: Encrypt content
+## Step 4: Add encryption key information to Azure AI Search objects
+
+When you create an encrypted object, enter the key vault URI, key name, and key version. If you're using a Microsoft Entra ID application for authentication, also enter the application ID and secret.
 
-Encryption occurs when you create or update an object. You can use the Azure portal for select objects. For all objects, use the [Search Service REST APIs](/rest/api/searchservice/) or an Azure SDK.
+You can configure new search objects with a customer-managed key at the **service level** or at the **object level**. When you configure CMK at the service level, you apply the same key by default to all newly created objects in the service, unless you specify a different object-level key to override the service-level default.
+
+Specify the customer-managed key in the object definition when you create an encrypted object. This object can be an index, indexer, data source, skillset, vectorizer, or synonym map.
+
+To configure CMK on an object, use the Azure portal, [Search Service REST APIs](/rest/api/searchservice/), or an Azure SDK.
 
 ### [**Azure portal**](#tab/portal)
 
-When you create a new object in the Azure portal, you can specify a predefined customer-managed key in a key vault. The Azure portal lets you enable CMK encryption for:
+When you create a new object in the Azure portal, you can specify a predefined customer-managed key in a key vault. The Azure portal lets you enable encryption with a CMK for:
 
 + Indexes
 + Data sources
 + Indexers
 
-Requirements for using the Azure portal are that the key vault and key must exist, and you completed the previous steps for authorized access to the key.
+To use the Azure portal, the key vault and key must exist, and you must complete the previous steps for authorized access to the key.
 
 In the Azure portal, skillsets are defined in JSON view. Use the JSON shown in the REST API examples to provide a customer-managed key on a skillset.
 
@@ -247,9 +279,11 @@ After you create the encrypted object on the search service, you can use it as y
 
 None of these key vault details are considered secret and could be easily retrieved by browsing to the relevant Azure Key Vault page in Azure portal.
 
-### [**Python**](#tab/python)
+### [**Azure SDKs**](#tab/sdks)
 
-This example shows the Python representation of an `encryptionKey` in an object definition. The same definition applies to indexes, data sources, skillets, indexers, and synonym maps. To try this example on your search service and key vault, download the notebook from [azure-search-python-samples](https://github.com/Azure-Samples/azure-search-python-samples).
+Configuration of CMK on search objects is supported in Azure SDK packages, including [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net), [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java), [Azure SDK for JavaScript](https://github.com/Azure/azure-sdk-for-js), and [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python).
+
+The following example demonstrates the **Python** representation of an `encryptionKey` in an object definition. The same definition applies to indexes, data sources, skillets, indexers, and synonym maps. To try this example on your search service and key vault, download the notebook from [azure-search-python-samples](https://github.com/Azure-Samples/azure-search-python-samples).
 
 1. Install some packages.
 
@@ -385,6 +419,89 @@ This example shows the Python representation of an `encryptionKey` in an object
 > [!Important]
 > Encrypted content in Azure AI Search is configured to use a specific key with a specific *version*. If you change the key or version, the object must be updated to use it **before** you delete the previous one. Failing to do so renders the object unusable. You won't be able to decrypt the content if the key is lost.
 
+### Configure CMK at the service-level (preview)
+
+To enable service-level CMK configuration, we recommend that you use the [Search Management REST API](/rest/api/searchmanagement) or an Azure SDK package that has been updated to support Search Management REST API version 2026-03-01-preview or later. This feature is not yet supported in the Azure portal. *Enabling CMK at the service level does not add encryption to existing objects, but it applies the same key by default to all newly-created objects in the service, unless you specify a different object-level key to override the service-level default.*
+
+### [**Azure portal**](#tab/portal)
+
+Currently, the Azure portal doesn't support service-level encryption. Use the REST API directly.
+
+### [**REST APIs**](#tab/rest)
+
+To configure encryption with a CMK at the service level on your search service, use [Services - Create Or Update](/rest/api/searchmanagement/services/create-or-update) with `PATCH` to update an existing search service or `PUT` to create a new one. The API version must be 2026-03-01-preview or later to support service-level configuration. 
+
+In this example, be sure to replace `{{subscription-id}}`, `{{resource-group}}`, `{{search-service}}`, and `{{token}}` with your subscription ID, resource group name, search service name, and access token, respectively. The key definition uses the same schema as object-level CMK, and all three identity options are supported (system-assigned managed identity, user-assigned managed identity, or registered application).
+
+```http
+PATCH https://management.azure.com/subscriptions/{{subscription-id}}/resourceGroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service}}?api-version=2026-03-01-preview
+Authorization: Bearer {{token}}
+Content-Type: application/json
+```
+
+See the following examples for how to insert the encryptionKey construct at the service level for different identity types.
+
+Example using system-assigned managed identity:
+
+```json
+{
+  "encryptionWithCmk": {
+    "serviceLevelEncryptionKey": {
+      "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
+      "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
+      "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>"
+    }
+  }
+}
+```
+
+Example using user-managed identity:
+
+```json
+{
+  "encryptionWithCmk": {
+    "serviceLevelEncryptionKey": {
+      "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
+      "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
+      "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
+      "identity": {
+        "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
+        "userAssignedIdentity": "/subscriptions/<your-subscription-ID>/resourceGroups/<your-resource-group-name>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<your-managed-identity-name>"
+      }
+    }
+  }
+}
+```
+
+Example using application ID:
+
+```json
+{
+  "encryptionWithCmk": {
+    "serviceLevelEncryptionKey": {
+          "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
+          "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
+          "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
+          "accessCredentials": {
+                  "applicationId": "<YOUR-APPLICATION-ID>",
+                  "applicationSecret": "<YOUR-APPLICATION-SECRET>"
+      }       
+    }
+  }
+}
+```
+
+### [**Azure SDKs**](#tab/sdks)
+
+Configuration of service-level CMK is supported in Azure SDK packages that target Search Management REST API version 2026-03-01-preview or later. To confirm support, check the changelog for your package:
+
+- .NET: [Azure.ResourceManager.Search changelog](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.ResourceManager.Search/CHANGELOG.md)
+- Java: [azure-resourcemanager-search changelog](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-resourcemanager-search/CHANGELOG.md)
+- JavaScript: [@azure/arm-search changelog](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/arm-search/CHANGELOG.md)
+- Python: [azure-mgmt-search changelog](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-mgmt-search/CHANGELOG.md)
+
+---
+
 ## Step 5: Test encryption
 
 To verify encryption is working, revoke the encryption key, query the index (it should be unusable), and then reinstate the encryption key.
@@ -411,7 +528,7 @@ Use the Azure portal for this task. Make sure you have a role assignment that gr
 
 Azure policies help to enforce organizational standards and to assess compliance at-scale. Azure AI Search has two optional built-in policies related to CMK. These policies apply to new and existing search services.
 
-| Effect | Effect if enabled|
+| Effect | Description |
 |--------|------------------|
 | [**AuditIfNotExists**](/azure/governance/policy/concepts/effect-audit-if-not-exists) | Checks for policy compliance: do objects have a customer-managed key defined, and is the content encrypted. This effect applies to existing services with content. It's evaluated each time an object is created or updated, or [per the evaluation schedule](/azure/governance/policy/overview#understand-evaluation-outcomes). [Learn more...](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F356da939-f20a-4bb9-86f8-5db445b0e354) |
 | [**Deny**](/azure/governance/policy/concepts/effect-deny) | Checks for policy enforcement: does the search service have [SearchEncryptionWithCmk](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2025-05-01&tabs=HTTP&preserve-view=true#searchencryptionwithcmk) set to `Enabled`. This effect applies to new services only, which must be created with encryption enabled. Existing services remain operational but you can't update them unless you patch the service. None of the tools used for provisioning services expose this property, so be aware that setting the policy limits you to [programmatic set up](#enable-cmk-policy-enforcement).|
@@ -428,19 +545,19 @@ Azure policies help to enforce organizational standards and to assess compliance
 
    :::image type="content" source="media/search-security-manage-encryption-keys/assign-policy.png" alt-text="Screenshot of assigning built-in CMK policy." border="true":::
 
-1. Set [policy scope](/azure/governance/policy/concepts/scope) by selecting the subscription and resource group. Exclude any search services for which the policy shouldn't apply.
+1. Set the [policy scope](/azure/governance/policy/concepts/scope) by selecting the subscription and resource group. Exclude any search services for which the policy shouldn't apply.
 
-1. Accept or modify the defaults. Select **Review +create**, followed by **Create**.
+1. Accept or modify the default values. Select **Review + create**, and then select **Create**.
 
 ### Enable CMK policy enforcement
 
-A policy that's assigned to a resource group in your subscription is effective immediately. Audit policies flag non-compliant resources, but Deny policies prevent the creation and update of non-compliant search services. This section explains how to create a compliant search service or update a service to make it compliant. To bring objects into compliance, start at [step one](#step-1-create-an-encryption-key) of this article.
+When you assign a policy to a resource group in your subscription, it takes effect immediately. Audit policies flag non-compliant resources, but Deny policies prevent the creation and update of non-compliant search services. This section explains how to create a compliant search service or update a service to make it compliant. To bring objects into compliance, start at [step one](#step-1-create-an-encryption-key) of this article.
 
 #### Create a compliant search service
 
 For new search services, create them with [SearchEncryptionWithCmk](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2025-05-01&tabs=HTTP&preserve-view=true#searchencryptionwithcmk) set to `Enabled`.
 
-Neither the Azure portal nor the command line tools (the Azure CLI and Azure PowerShell) provide this property natively, but you can use [Management REST API](/rest/api/searchmanagement/services/create-or-update) to provision a search service with a CMK policy definition.
+Neither the Azure portal nor the command-line tools (the Azure CLI and Azure PowerShell) provide this property natively, but you can use [Management REST API](/rest/api/searchmanagement/services/create-or-update) to provision a search service with a CMK policy definition.
 
 ### [**Management REST API**](#tab/mgmt-rest-create)
 
@@ -469,16 +586,6 @@ PUT https://management.azure.com/subscriptions/{{subscriptionId}}/resourceGroups
       }
     }
 ```
-<!-- 
-### [**Azure CLI**](#tab/azure-cli-create)
-
-These instructions assume you have a Deny policy defined for the resource group into which you're deploying a new search service.
-
-Run the following [`az resource`](/cli/azure/resource) command to create a new search service with CMK enforcement enabled. Substitute valid values for the name of the new search service and name of the existing resource group. The command includes eastus for a region so that you can see how regions are specified (lower case, no spaces).
-
-```azurecli
-az resource create --name SEARCH-SERVICE-PLACEHOLDER --location eastus --resource-group RESOURCE-GROUP-PLACEHOLDER --resource-type searchServices --namespace Microsoft.Search --set properties.encryptionWithCmk.enforcement=Enabled
-``` -->
 
 ---
 
@@ -526,11 +633,13 @@ The response should include the following statement:
 
 Use the following instructions to rotate keys or to migrate from Azure Key Vault to the Hardware Security Model (HSM). 
 
-For key rotation, we recommend using the [autorotation capabilities of Azure Key Vault](/azure/key-vault/keys/how-to-configure-key-rotation). If you use autorotation, omit the key version in object definitions. The latest key is used, rather than a specific version.
+For key rotation, use the [autorotation capabilities of Azure Key Vault](/azure/key-vault/keys/how-to-configure-key-rotation). If you use autorotation, omit the key version in object definitions. The latest key is used, rather than a specific version.
+
+When you change a key or its version, update any object that uses the key to use the new values **before** you delete the old values. Otherwise, the object becomes unusable because it can't be decrypted.
 
-When you change a key or its version, any object that uses the key must first be updated to use the new values **before** you delete the old values. Otherwise, the object becomes unusable because it can't be decrypted. 
+If you configured CMK at the service level, rotating the service-level key applies to newly created objects going forward. Objects that already inherited the previous service-level key automatically pick up the new key, so you don't need to update them. However, if you had any objects that were configured with an object-level key that you also want to rotate, then you need to update those objects to use the new key.
 
-Recall that keys are cached for 60 minutes. Remember this when testing and rotating keys.
+Keys are cached for 60 minutes. Remember this when testing and rotating keys.
 
 1. [Determine the key used by an index or synonym map](search-security-get-encryption-keys.md).
 
@@ -550,15 +659,15 @@ For performance reasons, the search service caches the key for up to several hou
 
 + Use the same [Azure tenant](/entra/fundamentals/create-new-tenant) so that you can retrieve your managed key through role assignments and by connecting through a system or user-managed identity. For more information about creating a tenant, see [Set up a new tenant](/azure/active-directory/develop/quickstart-create-new-tenant).
 
-+ [Enable purge protection](/azure/key-vault/general/soft-delete-overview#purge-protection) and [soft-delete](/azure/key-vault/general/soft-delete-overview) on a key vault. Due to the nature of encryption with customer-managed keys, no one can retrieve your data if your Azure Key Vault key is deleted. To prevent data loss caused by accidental Key Vault key deletions, soft-delete and purge protection must be enabled on the key vault. Soft-delete is enabled by default, so you'll only encounter issues if you purposely disable it. Purge protection isn't enabled by default, but it's required for CMK encryption in Azure AI Search.
++ [Enable purge protection](/azure/key-vault/general/soft-delete-overview#purge-protection) and [soft-delete](/azure/key-vault/general/soft-delete-overview) on a key vault. Due to the nature of encryption with customer-managed keys, no one can retrieve your data if your Azure Key Vault key is deleted. To prevent data loss caused by accidental Key Vault key deletions, soft-delete and purge protection must be enabled on the key vault. Soft-delete is enabled by default, so you'll only encounter issues if you purposely disable it. Purge protection isn't enabled by default, but it's required for encryption with a CMK in Azure AI Search.
 
 + [Enable logging](/azure/key-vault/general/logging) on the key vault so that you can monitor key usage.
 
 + [Enable autorotation of keys](/azure/key-vault/keys/how-to-configure-key-rotation) or follow strict procedures during routine rotation of key vault keys and application secrets and registration. Always update all [encrypted content](search-security-get-encryption-keys.md) to use new secrets and keys before deleting the old ones. If you miss this step, your content can't be decrypted.
 
 ## Work with encrypted content
 
-With CMK encryption, you might notice latency for both indexing and queries due to the extra encrypt/decrypt work. Azure AI Search doesn't log encryption activity, but you can monitor key access through key vault logging.
+Using CMK, you might notice latency for both indexing and queries due to the extra encrypt/decrypt work. Azure AI Search doesn't log encryption activity, but you can monitor key access through key vault logging.
 
 We recommend that you [enable logging](/azure/key-vault/general/logging) as part of key vault configuration.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search における顧客管理キーの設定に関する更新"
}
```

### Explanation
この変更は、「search-security-manage-encryption-keys.md」ドキュメントに対して行われたもので、Azure AI Searchにおける顧客管理キー（CMK）の設定に関する内容が更新されました。主な変更点は、文書の日付が2025年9月18日から2026年4月7日に変更されたこと、タイトルが「Encrypt Data Using Customer-Managed Keys」から「Configure Customer-Managed Keys for Azure AI Search」に変更されたことです。

内容的には、CMKの追加が、Microsoft管理の鍵による既存の暗号化の上にさらなるセキュリティを提供するという点が強調されています。CMKの管理や使用に関する詳細が追加され、顧客が暗号化キーのローテーションや使用状況の監査を行う方法が詳しく説明されています。また、サービスレベルでのCMKの設定やその適用方法も新たに取り入れられ、デフォルトの鍵を使用する新しいオブジェクトの管理が容易になっています。

この改訂により、顧客はAzure AI Searchを使用する際の暗号化設定の正確性と効率性を高めながら、より強固なセキュリティを確保するための情報を得ることができます。さらに、特定のAPIやAzure SDKを利用して、CMKの管理ができる方法が紹介されています。これにより、ユーザーは複雑な設定を行う際にも、より便利に機能を活用できるようになっています。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: What's New
 description: Stay up to date with the latest Azure AI Search features, updates, and announcements. Discover new capabilities for search, vector, and AI-powered retrieval.
-ms.date: 03/13/2026
+ms.date: 03/30/2026
 ms.service: azure-ai-search
 ms.topic: overview
 ms.custom:
@@ -21,6 +21,9 @@ Learn about the latest updates to Azure AI Search functionality, docs, and sampl
 
 | Item | Description |
 |--|--|
+| [Search Management 2026-03-01-preview](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true) | New preview REST API version providing programmatic access to the control plane operations described in this table. |
+| [Service-level CMK](search-security-manage-encryption-keys.md#enable-service-level-cmk-on-new-objects-by-default-preview) (preview) | For security-conscious customers who want more control over how their data is protected, the new `serviceLevelEncryptionKey` property in the `encryptionWithCmk` configuration helps you enable a customer-managed key (CMK) on all newly created objects by default. It ensures all sensitive data in your search service is protected by a key you control, without having to specify key information each time an object is created. You can later rotate from the default key to one specifically for the object. Note that encryption is set at creation time and can't be added to existing objects. |
+| [`knowledgeRetrieval` property](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true) (preview) | Search Management 2026-03-01-preview adds a `knowledgeRetrieval` property to the search service definition. This property doesn't affect any data plane versions, including Search Service 2025-11-01-preview. Ignore for now. |
 | [**Import data** wizard unification](search-import-data-portal.md) | The **Import data** and **Import data (new)** wizards have been unified into a single **Import data** wizard that supports keyword search, RAG, and multimodal RAG. |
 
 ## February 2026
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search の最新情報更新"
}
```

### Explanation
この変更は、「whats-new.md」ドキュメントに対するもので、Azure AI Searchの最新機能、アップデート、アナウンスメントに関する情報が更新されました。主な変更点は、ドキュメントの日付が2026年3月13日から2026年3月30日に変更されたことと、新たな機能に関するいくつかの項目が追加されたことです。

新たに追加された内容には、「Search Management 2026-03-01-preview」という新しいプレビューのREST APIバージョンや、セキュリティを重視する顧客向けの「serviceLevelEncryptionKey」プロパティに関する情報が含まれています。このプロパティにより、すべての新しいオブジェクトに対してデフォルトで顧客管理鍵（CMK）を有効にすることができるようになります。また、その他の機能として、「knowledgeRetrieval」プロパティの追加に関する情報も含まれており、これは検索サービスの定義に影響を与えないことが説明されています。

この更新により、ユーザーはAzure AI Searchにおける最新の開発状況を把握し、新機能の利用方法についての情報を得ることができます。また、これによってより良い検索システムの構築が可能となり、セキュリティやデータ管理の向上が期待されます。


