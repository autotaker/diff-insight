---
date: '2026-08-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6ebd472...MicrosoftDocs:90a93ce
summary: この差分では、ユーザー体験の向上を目指してリダイレクションURLの更新と新たな追加が行われ、Azure検索の新機能やコスト効率に関する情報が加えられました。また、プレビューフィーチャー関連の文書が整理され、REST
  APIバージョンへの参照が更新されることで情報へのアクセス性が向上しています。全体として、ユーザーエクスペリエンスの向上と情報整合性の維持を目的とした内容となっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6ebd472...MicrosoftDocs:90a93ce){target="_blank"}

<format>
# ハイライト
この差分では、リダイレクションURLの更新と新規追加を通じたユーザー体験の改善、Azure検索の新しい機能やコスト効率に関連する情報の追加、プレビューフィーチャーに関する文書や参照の整理が行われました。また、REST APIバージョンへの参照の更新による情報のアクセス性向上が図られています。

## 新機能
- `articles/search/cognitive-search-skill-content-understanding.md` の変更で、コスト効率とAIベースの説明生成に関する情報が追加。
  
## 破壊的変更
- `articles/search/search-api-preview.md` が削除され、関連情報が提供されなくなる。
- `articles/search/search-features-list.md`、`articles/search/toc.yml`でプレビューフィーチャーリストの参照が削除。

## その他の更新
- リダイレクションURLの更新
- テキストの簡潔化とトピックタイプ変更
- 最新のプレビューREST APIバージョンへのリンクの改善

# 洞察
この差分では、Azureの検索サービスに関連した文書全般にわたって、いくつかの小規模な改善や削除が行われています。特に注目すべき点として、古い情報が整理され、新しいリダイレクション設定によって用途に即したアクセスが容易になることが挙げられます。例えば、`articles/search/.openpublishing.redirection.search.json`ファイルでは古いAPIドキュメントから新しいコンテンツへのスムーズな移行が可能になるよう調整されています。

さらに、`articles/search/cognitive-search-skill-content-understanding.md`の変更では、Content Understandingスキルの低コスト性が強調され、ユーザーが最適な選択を行いやすくなるよう情報が充実されています。このような追加情報は、使用コストを考慮するユーザーにとって非常に有益です。

一方で、Ajax Searchのプレビューフィーチャーの詳細が`articles/search/search-api-preview.md`から削除されたり、関連リンクが整理されたことは、情報が一時的にアクセスしづらくなるという側面があるものの、極力最新の情報を提供することで全体の精度を高めようという意図が見受けられます。

REST APIの最新版へのリンクなど、関連情報へのアクセスをより迅速かつ直感的に行えるようにするための改良も随所に施されています。これにより、ユーザーが最新かつ正確な情報を得られる環境が整えられています。

全体として、変更はユーザーエクスペリエンスの向上と情報の整合性を保つことを目的としており、Azureの技術文書が進化し続けていることを示しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [.openpublishing.redirection.search.json](#item-8b66f9) | minor update | リダイレクションURLの更新と新しいエントリの追加 | modified | 9 | 4 | 13 | 
| [cognitive-search-skill-content-understanding.md](#item-c7787e) | minor update | コスト効率とAIベースの説明生成に関する情報の追加 | modified | 2 | 0 | 2 | 
| [search-api-preview.md](#item-511f5d) | breaking change | 検索APIプレビューフィーチャーリストの削除 | removed | 0 | 120 | 120 | 
| [search-features-list.md](#item-d34448) | minor update | プレビューフィーチャーリストの参照を削除 | modified | 0 | 3 | 3 | 
| [search-how-to-index-cosmosdb-gremlin.md](#item-e5e93d) | minor update | プレビューREST APIバージョンへの参照を改善 | modified | 1 | 1 | 2 | 
| [search-how-to-index-cosmosdb-mongodb.md](#item-b5aa9f) | minor update | プレビューREST APIバージョンへの参照を改善 | modified | 1 | 1 | 2 | 
| [search-how-to-index-sharepoint-online.md](#item-8c099c) | minor update | プレビューREST APIバージョンへの参照を改善 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c4768f) | minor update | プレビュー機能の項目を削除 | modified | 0 | 2 | 2 | 
| [whats-new.md](#item-fa71b4) | minor update | トピックタイプの変更とテキストの簡潔化 | modified | 2 | 5 | 7 | 


# Modified Contents
## articles/search/.openpublishing.redirection.search.json{#item-8b66f9}

<details>
<summary>Diff</summary>
````diff
@@ -295,20 +295,25 @@
             "redirect_url": "/azure/search/policy-reference",
             "redirect_document_id": false
         },
+        {
+            "source_path_from_root": "/articles/search/search-api-preview.md",
+            "redirect_url": "/azure/search/whats-new",
+            "redirect_document_id": true
+        },
         {
             "source_path_from_root": "/articles/search/search-api-2015-02-28-preview.md",
-            "redirect_url": "/azure/search/search-api-preview",
+            "redirect_url": "/azure/search/whats-new",
             "redirect_document_id": false
         },
         {
             "source_path_from_root": "/articles/search/search-api-2016-09-01-preview.md",
-            "redirect_url": "/azure/search/search-api-preview",
+            "redirect_url": "/azure/search/whats-new",
             "redirect_document_id": false
         },
         {
             "source_path_from_root": "/articles/search/search-api-2017-11-11-preview.md",
-            "redirect_url": "/azure/search/search-api-preview",
-            "redirect_document_id": true
+            "redirect_url": "/azure/search/whats-new",
+            "redirect_document_id": false
         },
         {
             "source_path_from_root": "/articles/search/search-autosuggest-example.md",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リダイレクションURLの更新と新しいエントリの追加"
}
```

### Explanation
この変更は、`articles/search/.openpublishing.redirection.search.json`ファイルのリダイレクション設定に関するもので、新しいリダイレクションURLを追加し、いくつかの既存のリダイレクションURLを更新しています。具体的には、`/articles/search/search-api-preview.md`から`/azure/search/whats-new`への新しいリダイレクションエントリが追加され、この内容に伴い他のいくつかのリダイレクションURLも同様に変更されています。これにより、古いAPIドキュメントから新しいコンテンツへのアクセスが容易になり、ユーザーに最新情報を提供することができます。全体として、9行が追加され4行が削除され、合計で13行の変更が行われました。

## articles/search/cognitive-search-skill-content-understanding.md{#item-c7787e}

<details>
<summary>Diff</summary>
````diff
@@ -40,6 +40,8 @@ You can use the Azure Content Understanding skill for both content extraction an
 
 + The Azure Content Understanding skill is more cost effective than the Document Layout skill because the Content Understanding API is less expensive.
 
++ Azure Content Understanding can generate AI-based descriptions for images, charts, diagrams, and embedded figures. Embedded figure descriptions are incorporated directly into markdown content generated for retrieval. These descriptions are searchable and can improve RAG grounding and multimodal retrieval quality. 
+
 The Azure Content Understanding skill is generally available in the [`2026-04-01` REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true). Starting with the [`2026-05-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true), the skill optionally generates AI-based descriptions for document-embedded images, charts, and diagrams. To enable descriptions, you must deploy an Azure OpenAI chat completion model in the Foundry resource attached to the skillset. This API version also adds *semantic* chunking, a layout-aware option that respects paragraph boundaries and measures chunk length in tokens. Both capabilities require opt-in. When the new parameters are omitted, the skill behaves the same as in the stable `2026-04-01` API version.
 
 ## Limitations
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コスト効率とAIベースの説明生成に関する情報の追加"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-content-understanding.md`ファイルの内容に関するもので、AzureのContent Understandingスキルに関して新たな情報が追加されています。具体的には、Content Understandingスキルのコスト効率についての記述が加わり、Document Layoutスキルよりも低コストであることが強調されています。また、AIを基にした画像、チャート、図、埋め込まれた図の説明を生成する機能について詳しく説明が行われています。これらの説明はマークダウン形式で生成されたコンテンツに直接組み込まれ、検索可能であるため、検索基盤とマルチモーダル検索の品質を向上させることができます。この変更により、合計2行が追加され、全体の内容がより充実しました。

## articles/search/search-api-preview.md{#item-511f5d}

<details>
<summary>Diff</summary>
````diff
@@ -1,120 +0,0 @@
----
-title: Preview Feature List
-description: Preview features are released so that customers can provide feedback on their design and utility. This article is a comprehensive list of all features currently in preview.
-ms.service: azure-ai-search
-ms.custom:
-  - build-2024
-  - ignite-2024
-ms.topic: concept-article
-ms.date: 06/02/2026
-ai-usage: ai-assisted
----
-
-# Preview features in Azure AI Search
-
-[!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
-
-This article identifies all data plane and control plane features in preview. This list is helpful for checking feature status. It also explains how to call a preview REST API.
-
-Preview API versions are cumulative and roll up to the next preview. We recommend always using the latest preview APIs for full access to all preview features.
-
-Preview features are removed from this list if they're retired or transition to general availability. For announcements regarding retirement and general availability, see [What's new in Azure AI Search](whats-new.md).
-
-## Data plane preview features
-
-| Feature | Description | Availability |
-|--|--|--|
-| [**Agentic retrieval**](agentic-retrieval-overview.md) | [Knowledge bases](agentic-retrieval-how-to-create-knowledge-base.md) and select [knowledge sources](agentic-knowledge-source-overview.md) are generally available. However, certain agentic retrieval capabilities remain in preview, including [document-level permissions](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time-preview), [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md), configurable [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md), and multi-turn conversational messages in the [retrieve request](agentic-retrieval-how-to-retrieve.md). | [Knowledge Bases (preview)](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2026-05-01-preview&preserve-view=true), [Knowledge Sources (preview)](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-05-01-preview&preserve-view=true), [Knowledge Retrieval (preview)](/rest/api/searchservice/knowledge-retrieval?view=rest-searchservice-2026-05-01-preview&preserve-view=true), and the Azure portal. |
-| [**APIM support for Azure OpenAI skills and vectorizers**](cognitive-search-skill-azure-openai-embedding.md) | The Azure OpenAI Embedding skill, GenAI Prompt skill, and Azure OpenAI vectorizer accept `azure-api.net` endpoints for Azure API Management. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**List API paging**](search-how-to-page-list-results.md) | List operations support cursor-based paging via `$top`, `$skip`, and a continuation token. | [Indexes - List (preview)](/rest/api/searchservice/indexes/list?view=rest-searchservice-2026-05-01-preview&preserve-view=true), [Indexers - List (preview)](/rest/api/searchservice/indexers/list?view=rest-searchservice-2026-05-01-preview&preserve-view=true), [Knowledge Bases - List (preview)](/rest/api/searchservice/knowledge-bases/list?view=rest-searchservice-2026-05-01-preview&preserve-view=true), and [Knowledge Sources - List (preview)](/rest/api/searchservice/knowledge-sources/list?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**Content Understanding skill (semantic chunking, image descriptions, and knowledge store projection)**](cognitive-search-skill-content-understanding.md) | Adds semantic chunking for better retrieval segmentation, AI-generated image descriptions for visual content, and knowledge store image projection to the generally available Content Understanding skill. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**Microsoft Purview index configuration**](search-indexer-sensitivity-labels.md) | Apply Microsoft Purview classifications and sensitivity labels to indexed content based on source metadata for enhanced data governance. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**Scoring function aggregation**](index-add-scoring-profiles.md#example-function-aggregation) | Combine and aggregate multiple scoring functions, enabling more sophisticated relevance customization and weighted signal combination. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**Facet aggregations**](search-faceted-navigation-examples.md#facet-aggregation-example) | Use sum, count, minimum, maximum, and other aggregate functions to provide enhanced analytics in faceted search experiences. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**Improved indexer runtime tracking information**](search-howto-run-reset-indexers.md) | Cumulative indexer processing information for the search service and for specific indexers. | [Get Service Statistics (preview)](/rest/api/searchservice/get-service-statistics/get-service-statistics?view=rest-searchservice-2026-05-01-preview&preserve-view=true) and [Get Status - Indexers (preview)](/rest/api/searchservice/get-service-statistics/get-service-statistics?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**Strict postfiltering for vector queries**](vector-search-filters.md) | Adds the `strictPostFilter` mode to the `vectorFilterMode` parameter. When specified, filters are applied after the global top-`k` vector results are identified, ensuring that returned documents are a subset of the unfiltered results. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**Multivector support**](vector-search-multi-vector-fields.md) | Index multiple child vectors within a single document field. Use vector types in nested fields of complex collections to associate multiple vectors with a single document.| [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**Document-level access control**](search-document-level-access-overview.md) | Flow document-level permissions from blobs in Azure Data Lake Storage (ADLS) Gen2 to searchable documents in an index. Queries filter results based on user identity for selected data sources. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**flightingOptIn parameter in a semantic configuration**](semantic-how-to-configure.md#opt-in-for-prerelease-semantic-ranking-models) | Opt in to use prerelease semantic ranking models if one is available in a search service region. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true) |
-| [**Facet hierarchies, aggregations, and facet filters**](search-faceted-navigation-examples.md) | New facet query parameters support nested facets. For numeric facetable fields, you can sum the values of each field. You can also specify filters on a facet to add inclusion or exclusion criteria. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-03-01-preview&preserve-view=true) |
-| [**Query rewrite in the semantic reranker**](semantic-how-to-query-rewrite.md) | Set options on a semantic query to rewrite the query input into a revised or expanded query that generates more relevant results from the L2 ranker. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true)|
-| [**Target filters in a hybrid search to just the vector queries**](hybrid-search-how-to-query.md#example-hybrid-search-with-filters-targeting-vector-subqueries-preview) | A filter on a hybrid query involves all subqueries on the request, regardless of type. You can override the global filter to scope the filter to a specific subquery. A new `filterOverride` parameter provides the behaviors. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**Text Split skill (token chunking)**](cognitive-search-skill-textsplit.md) | This skill has new parameters that improve data chunking for embedding models. A new `unit` parameter lets you specify token chunking. Chunk by token length, setting the length to a value that makes sense for your embedding model. You can also specify the tokenizer and any tokens that shouldn't be split during data chunking. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**Azure Vision multimodal embedding skill**](cognitive-search-skill-vision-vectorize.md) | Skill that calls the Azure Vision multimodal API to generate embeddings for text or images during indexing. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**Azure Machine Learning (AML) skill**](cognitive-search-aml-skill.md) | AML skill integrates an inferencing endpoint from Azure Machine Learning. In previous preview APIs, it supports connections to deployed custom models in an AML workspace. Starting in the 2026-05-01-preview, you can use this skill in workflows that connect to embedding models in the Microsoft Foundry model catalog. It's also available in the Azure portal, in skillset design, assuming Azure AI Search and Azure Machine Learning services are deployed in the same subscription. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**Incremental enrichment cache**](enrichment-cache-how-to-configure.md) | Adds caching to an enrichment pipeline, allowing you to reuse existing output if a targeted modification, such as an update to a skillset or another object, doesn't change the content. Caching applies only to enriched documents produced by a skillset.| [Create or Update Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**Azure Files indexer**](search-file-storage-integration.md) | Data source for indexer-based indexing from [Azure Files](https://azure.microsoft.com/services/storage/files/). | [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**SharePoint indexer**](search-how-to-index-sharepoint-online.md) | Data source for indexer-based indexing of SharePoint content. | [Sign up](https://aka.ms/azure-cognitive-search/indexer-preview) to enable the feature. [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) and the Azure portal. |
-| [**MySQL indexer**](search-how-to-index-mysql.md) | Data source for indexer-based indexing of Azure MySQL data sources.| [Sign up](https://aka.ms/azure-cognitive-search/indexer-preview) to enable the feature. [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) and the Azure portal. |
-| [**Azure Cosmos DB for MongoDB indexer**](search-how-to-index-cosmosdb-sql.md) | Data source for indexer-based indexing through the MongoDB APIs in Azure Cosmos DB. | [Sign up](https://aka.ms/azure-cognitive-search/indexer-preview) to enable the feature. [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) and the Azure portal. |
-| [**Azure Cosmos DB for Apache Gremlin indexer**](search-how-to-index-cosmosdb-sql.md) | Data source for indexer-based indexing through the Apache Gremlin APIs in Azure Cosmos DB. | [Sign up](https://aka.ms/azure-cognitive-search/indexer-preview) to enable the feature. [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true). |
-| [**Native blob soft delete**](search-how-to-index-azure-blob-changed-deleted.md) | Applies to the Azure Blob Storage indexer. Recognizes blobs that are in a soft-deleted state, and removes the corresponding search document during indexing. | [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**Reset Documents**](search-howto-run-reset-indexers.md) | Reprocesses individually selected search documents in indexer workloads. | [Reset Documents (preview)](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**speller**](speller-how-to-add.md) | Optional spelling correction on query term inputs for simple, full, and semantic queries. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**featuresMode parameter**](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) | BM25 relevance score expansion to include details: per field similarity score, per field term frequency, and per field number of unique tokens matched. You can consume these data points in [custom scoring solutions](https://github.com/Azure-Samples/search-ranking-tutorial). | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true)|
-| [**vectorQueries.threshold parameter**](vector-search-how-to-query.md#vector-weighting) | Exclude low-scoring search result based on a minimum score. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**hybridSearch.maxTextRecallSize and countAndFacetMode parameters**](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) | Adjust the inputs to a hybrid query by controlling the amount BM25-ranked results that flow to the hybrid ranking model. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-| [**moreLikeThis**](search-more-like-this.md) | Finds documents that are relevant to a specific document. This feature has been in earlier previews. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-
-## Control plane preview features
-
-| Feature | Description | Availability |
-|--|--|--|
-| [**Serverless pricing model**](search-sku-tier.md) | Consumption-based pricing model where you only pay for the compute and indexed storage that you use. Compute scales to zero when idle, and there's no minimum capacity charge. | [Services - Create or Update (preview)](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true) |
-| [**Service-level CMK**](search-security-manage-encryption-keys.md#enable-service-level-cmk-on-new-objects-by-default-preview) | Enables a customer-managed key (CMK) on all newly created objects by default. Service-level CMK ensures all sensitive data in your search service is protected by a key you control, without having to specify key information each time an object is created. | [Services - Create or Update (preview)](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true) |
-| [**Network security perimeter and shared private link for Microsoft Foundry**](search-security-network-security-perimeter.md) | Network security perimeter and shared private link support for outbound connections from Azure AI Search to Microsoft Foundry resources, enabling secure private connectivity for skills, vectorizers, and knowledge bases. | [Shared Private Link Resources (preview)](/rest/api/searchmanagement/shared-private-link-resources?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true) |
-
-## Preview features in Azure SDKs
-
-Preview features in Azure SDKs are available through preview packages. To determine which preview features are available in a specific package version, see the SDK's changelog:
-
-+ [Changelog for Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md)
-+ [Changelog for Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md)
-+ [Changelog for Azure SDK for JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md)
-+ [Changelog for Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md)
-
-## Using preview features
-
-You can access experimental features through preview REST API versions or preview SDK packages. Some features might also be available in the Azure portal. For more information about availability, see [Data plane preview features](#data-plane-preview-features) and [Control plane preview features](#control-plane-preview-features).
-
-The following statements apply to preview features:
-
-+ Preview features are available under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/), without a service level agreement.
-+ Preview features might undergo breaking changes if a redesign is required. 
-+ Sometimes preview features don't make it into a GA release.
-
-If you write code against a preview API, you should prepare to upgrade that code to newer API versions when they roll out. We maintain an [Upgrade REST APIs](search-api-migration.md) document to make that step easier.
-
-## How to call a preview REST API
-
-Preview REST APIs are accessed through the `api-version` parameter on the URI. Although older previews are still operational, they become stale over time and aren't updated with new features or bug fixes.
-
-For data plane operations on content, [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) is the most recent preview version. The following example shows how to call [Indexes - Get](/rest/api/searchservice/indexes/get?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (REST API) for this preview version.
-
-```http
-GET {endpoint}/indexes('{indexName}')?api-version=2026-05-01-preview
-```
-
-For management operations on the search service, [2026-03-01-preview](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true) is the most recent preview version. The following example shows how to call [Services - Update](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true) (REST API) for this preview version.
-
-```http
-PATCH https://management.azure.com/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Search/searchServices/mysearchservice?api-version=2026-03-01-preview
-
-{
-  "tags": {
-    "app-name": "My e-commerce app",
-    "new-tag": "Adding a new tag"
-  },
-  "properties": {
-    "replicaCount": 2
-  }
-}
-```
-
-## Related content
-
-+ [Search Service REST API overview](/rest/api/searchservice/)
-+ [Search Service REST API versions](/rest/api/searchservice/search-service-api-versions)
-+ [Search Management REST API overview](/rest/api/searchmanagement/)
-+ [Search Management REST API versions](/rest/api/searchmanagement/management-api-versions)
-+ [Manage your Azure AI Search service using REST APIs](search-manage-rest.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "検索APIプレビューフィーチャーリストの削除"
}
```

### Explanation
この変更は、`articles/search/search-api-preview.md`ファイルの削除に関するものであり、合計120行が削除されました。このファイルはAzure AI Searchのプレビューフィーチャーに関するリストを提供しており、プレビュー機能のステータスや利用方法を説明していました。今回の変更により、これらの情報が削除され、ユーザーはもはやこの文書を参照することができなくなります。この変更は、検索APIのプレビュー機能に関する情報が新しい形で提供される可能性を示唆しており、古い情報が削除されたことで新しいリリースや更新に適切に対応する必要性を強調しています。

## articles/search/search-features-list.md{#item-d34448}

<details>
<summary>Diff</summary>
````diff
@@ -17,9 +17,6 @@ Azure AI Search provides information retrieval and uses optional AI integration
 
 The following table summarizes features by category. There's feature parity in all Azure public, private, and sovereign clouds, but some features aren't supported in [specific regions](search-region-support.md) or [specific tiers](search-sku-tier.md#feature-availability-by-tier).
 
-> [!NOTE]
-> Looking for preview features? See the [preview features list](search-api-preview.md).
-
 ## Agentic retrieval
 
 | Category&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Features |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビューフィーチャーリストの参照を削除"
}
```

### Explanation
この変更は、`articles/search/search-features-list.md`ファイルにおける内容の修正であり、合計3行が削除されました。具体的には、Azure AI Searchの機能に関する要約テーブルの前に記載されていた「プレビューフィーチャーを探していますか？ プレビュー機能リストを参照してください。」という注記が削除されました。この変更により、プレビュー機能のリストへの参照がなくなり、ユーザーは直接プレビューフィーチャーに関する情報を他の場所で探さなければならなくなりました。この修正は、ドキュメントの簡潔さを向上させる一方で、プレビュー機能に関連する情報へのアクセスが少し不便になる可能性があります。

## articles/search/search-how-to-index-cosmosdb-gremlin.md{#item-e5e93d}

<details>
<summary>Diff</summary>
````diff
@@ -47,7 +47,7 @@ Because terminology can be confusing, it's worth noting that [Azure Cosmos DB in
 
 The data source definition specifies the data to index, credentials, and policies for identifying changes in the data. A data source is defined as an independent resource so that it can be used by multiple indexers.
 
-For this call, specify a [preview REST API version](search-api-preview.md) to create a data source that connects via an Azure Cosmos DB for Apache Gremlin. You can use 2021-04-01-preview or later. We recommend the latest preview API.
+For this call, specify a preview REST API version to create a data source that connects via Azure Cosmos DB for Apache Gremlin. You can use `2021-04-01-preview` or later. We recommend the [latest preview REST API](/rest/api/searchservice/search-service-api-versions#preview-versions).
 
 1. [Create or update a data source](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) to set its definition: 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビューREST APIバージョンへの参照を改善"
}
```

### Explanation
この変更は、`articles/search/search-how-to-index-cosmosdb-gremlin.md`ファイルの修正に関連しており、1行の追加と1行の削除が行われました。具体的には、Azure Cosmos DB for Apache Gremlinへの接続に関するデータソース作成時に指定するプレビューレストAPIバージョンの説明が更新されました。以前は「プレビューREST APIバージョンを指定」という表現でしたが、変更後は「最新のプレビューREST API」として具体的なリンクが追加されました。この修正により、ユーザーは最新のプレビューREST APIを簡単に参照できるようになり、情報のアクセス性が向上しました。

## articles/search/search-how-to-index-cosmosdb-mongodb.md{#item-b5aa9f}

<details>
<summary>Diff</summary>
````diff
@@ -59,7 +59,7 @@ As an alternative to this connector, if your scenario has any of those requireme
 
 The data source definition specifies the data to index, credentials, and policies for identifying changes in the data. A data source is defined as an independent resource so that it can be used by multiple indexers.
 
-For this call, specify a [preview REST API version](search-api-preview.md). You can use 2020-06-30-preview or later to create a data source that connects via the MongoDB API. We recommend the latest preview REST API.
+For this call, specify a preview REST API version to create a data source that connects via the MongoDB API. You can use `2020-06-30-preview` or later. We recommend the [latest preview REST API](/rest/api/searchservice/search-service-api-versions#preview-versions).
 
 1. [Create or update a data source](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) to set its definition: 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビューREST APIバージョンへの参照を改善"
}
```

### Explanation
この変更は、`articles/search/search-how-to-index-cosmosdb-mongodb.md`ファイルにおける修正であり、1行が追加され、1行が削除されました。特に、MongoDB APIを通じて接続するデータソースを作成する際に指定するプレビューレストAPIバージョンの説明が更新されました。具体的には、「最新のプレビューREST API」へのリンクが追加され、ユーザーは簡単に最新の情報を参照できるようになりました。この修正により、プレビューREST APIバージョンの情報が一層わかりやすくなり、ユーザーの利便性が向上しました。

## articles/search/search-how-to-index-sharepoint-online.md{#item-8c099c}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ When setting up permissions, consider the following information:
 >
 > Before you proceed, review the [known limitations](#limitations-and-considerations).
 >
-> [Fill out this form](https://aka.ms/azure-cognitive-search/indexer-preview) to register for the preview. All requests are approved automatically. After you fill out the form, use a [preview REST API](search-api-preview.md) to index your content. 
+> [Fill out this form](https://aka.ms/azure-cognitive-search/indexer-preview) to register for the preview. All requests are approved automatically. After you fill out the form, use a [preview REST API](/rest/api/searchservice/search-service-api-versions#preview-versions) to index your content. 
 
 > [!IMPORTANT]
 > These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビューREST APIバージョンへの参照を改善"
}
```

### Explanation
この修正は、`articles/search/search-how-to-index-sharepoint-online.md`ファイルに関するもので、1行の追加と1行の削除が行われました。具体的には、SharePoint Onlineのコンテンツをインデックスする際に使用するプレビューレストAPIのバージョンへのリンクが更新されました。以前は「search-api-preview.md」という相対リンクが使用されていましたが、変更後は「/rest/api/searchservice/search-service-api-versions#preview-versions」というリンクが追加され、ユーザーが最新のプレビューREST APIを簡単に確認できるようになっています。この変更により、情報の正確性と利用しやすさが向上しました。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -625,8 +625,6 @@ items:
   items:
   - name: API versions
     href: search-api-versions.md
-  - name: Preview features
-    href: search-api-preview.md
   - name: Develop in .NET
     href: search-how-to-dotnet-sdk.md
   - name: Handle concurrent updates
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビュー機能の項目を削除"
}
```

### Explanation
この変更は、`articles/search/toc.yml`ファイルに関連しており、2つの行が削除されました。具体的には、目次（TOC）から「Preview features」という項目が削除され、その関連リンクも一緒に削除されました。この修正は、プレビュー機能に関する情報を整理し、目次をより簡潔にすることを目的としています。この変更により、ユーザーが必要な情報にアクセスしやすくなることが期待されます。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: What's New
 description: Stay up to date with the latest Azure AI Search features, updates, and announcements. Discover new capabilities for search, vector, and AI-powered retrieval.
 ms.date: 08/05/2026
 ms.service: azure-ai-search
-ms.topic: overview
+ms.topic: whats-new
 ms.custom:
   - references_regions
   - ignite-2024
@@ -15,10 +15,7 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-Learn about the latest updates to Azure AI Search functionality, docs, and samples.
-
-> [!NOTE]
-> Preview features are announced here, but we also maintain a [preview features list](search-api-preview.md) so you can find them in one place.
+Learn about the latest updates to Azure AI Search functionality, documentation, and samples.
 
 ## June 2026
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピックタイプの変更とテキストの簡潔化"
}
```

### Explanation
この変更は、`articles/search/whats-new.md`ファイルに対するもので、主にテキストの簡潔化が行われました。具体的には、`ms.topic`の値が「overview」から「whats-new」に変更され、文書のトピックタイプがより特定の内容を反映するようになりました。また、Azure AI Search機能、ドキュメント、およびサンプルの最新情報を学ぶ部分で、表現が一部簡略化されました。さらに、プレビュー機能に関する注意書きが削除され、最新機能の発表に関する内容が洗練されました。この修正により、情報の明確さと一貫性が改善され、ユーザーが迅速に必要な情報にアクセスできるようになります。


