---
date: '2026-02-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7633f3f...MicrosoftDocs:9509c12
summary: このコードの変更は、Azure AI の検索 API ドキュメントのリンクと内容を更新するもので、新しい API バージョンに向けたアップグレード手順や、ドキュメントの一貫性を高める修正が含まれています。これにより、開発者が最新の情報を基に
  API を利用しやすくなることを目指しています。新機能の追加はありませんが、リンクの更新により新しい API バージョンへのアクセスが容易になります。直接的な破壊的変更はなく、文書の整理と内容の改善により、読者にとっての情報の流れが向上しています。この変更は、開発者が迅速に新しいバージョンの
  API を活用できる基盤を提供します。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7633f3f...MicrosoftDocs:9509c12){target="_blank"}

# ハイライト

このコードの変更は、Azure AI の検索 API ドキュメントのマイグレーションに関連するリンクと内容を更新するものです。主に、新しい API バージョンに向けたアップグレード手順や、ドキュメントの一貫性を高めるための修正が加えられています。これにより、開発者が最新の情報を元に API の利用をより容易にできることを目指しています。

## 新機能

特に新機能の追加はないが、リンクの更新を通じて新しい API バージョンに関する情報へのアクセスが容易になります。

## 破壊的変更

現行の API への直接的な破壊的変更は示されていませんが、文書の一貫性と正確性を高めるためのリンク修正が加えられています。

## その他の更新

- Azure API のバージョンやプレビュー情報に関するリンクが最新の状態に修正されました。
- ドキュメント内容が整理され、情報の正確性と流れが改善されています。
- API に関する知識ベースを強化するための情報が追加され、特にセキュリティや新料金体系に関するセクションが改良されています。

# 洞察

この種のリンク修正とドキュメントのアップデートは、API の利用者に最新情報を提供し続けるために不可欠です。Azure のようなプラットフォームは頻繁にアップデートされるため、開発者が古い情報に惑わされないよう、常に最新の情報にアクセス可能であることが重要です。特にAPIのバージョンが上がった場合、その変更点や新機能、注意すべき点を迅速に理解することは、開発者にとって生産性を大きく左右する要因となります。

今回の変更では、リンクの修正によって、新しいバージョンやプレビュー版APIに関する適切なドキュメントが支持されており、開発者はリファレンスを正確に得ることができるようになっています。また、段落や内容の整理によってドキュメントの読みやすさが向上しており、情報の流れがスムーズです。

結論として、ドキュメントの更新は、単に情報を新しくするだけでなく、ユーザーエクスペリエンスや開発プロセスの効率化にも大いに貢献するものです。この更新により、開発者は新しいバージョンのAPIをすぐに活用できる準備が整い、プロジェクトの円滑な進行を支援するための基盤が築かれたと言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-api-migration.md](#item-07297b) | minor update | 検索 API のマイグレーションに関するドキュメントの更新 | modified | 15 | 15 | 30 | 
| [search-api-preview.md](#item-511f5d) | minor update | 検索 API プレビューセクションのリンク修正 | modified | 1 | 1 | 2 | 
| [vector-search-how-to-query.md](#item-9bb93c) | minor update | ベクター検索クエリのドキュメント修正 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-fa71b4) | minor update | Whats New ドキュメントの段落修正 | modified | 4 | 4 | 8 | 


# Modified Contents
## articles/search/search-api-migration.md{#item-07297b}

<details>
<summary>Diff</summary>
````diff
@@ -22,8 +22,8 @@ Here are the most recent versions of the REST APIs:
 
 | Targeted operations | REST API | Status |
 |---------------------|----------|--------|
-| Data plane | [`2025-09-01`](/rest/api/searchservice/search-service-api-versions#2025-09-01) | Stable |
-| Data plane | [`2025-11-01-preview`](/rest/api/searchservice/search-service-api-versions#2025-11-01-preview&preserve-view=true) | Preview |
+| Data plane | [`2025-09-01`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-09-01&preserve-view=true) | Stable |
+| Data plane | [`2025-11-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) | Preview |
 | Control plane | [`2025-05-01`](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2025-05-01&preserve-view=true) | Stable |
 | Control plane | [`2025-02-01-preview`](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true) | Preview |
 
@@ -48,7 +48,7 @@ Azure AI Search breaks backward compatibility as a last resort. Upgrade is neces
 
 ## How to upgrade
 
-1. If you're upgrading a data plane version, review the [release notes](/rest/api/searchservice/search-service-api-versions) for the new API version.
+1. If you're upgrading a data plane version, review [what's been released](whats-new.md) in the new API version.
 
 1. Update the `api-version` parameter, specified in the request header, to a newer version.
 
@@ -100,7 +100,7 @@ Upgrade guidance assumes upgrade from the most recent previous version. If your
 
 ### Upgrade to 2025-11-01-preview
 
-[`2025-11-01-preview`](/rest/api/searchservice/search-service-api-versions#2025-11-01-preview) introduces the following breaking changes to agentic retrieval as implemented in the `2025-08-01-preview`:
+[`2025-11-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) introduces the following breaking changes to agentic retrieval as implemented in the `2025-08-01-preview`:
 
 + Replaces `agents` with `knowledgebases`. Several properties related to knowledge sources moved out of the knowledge base definition and to the retrieve action.
 + Knowledge source properties are refactored, implementing a new `ingestionParameters` object for knowledge sources that generate an indexer pipeline.
@@ -111,13 +111,13 @@ For all other existing APIs, there are no behavior changes. You can swap in the
 
 ### Upgrade to 2025-09-01
 
-[`2025-09-01`](/rest/api/searchservice/search-service-api-versions#2025-09-01) is the latest stable REST API version and it adds general availability for the OneLake indexer, Document Layout skill, and other APIs.
+[`2025-09-01`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-09-01&preserve-view=true) is the latest stable REST API version and it adds general availability for the OneLake indexer, Document Layout skill, and other APIs.
 
 There are no breaking changes if you're upgrading from `2024-07-01` and not using any preview features. To use the new stable release, change the API version and test your code.
 
 ### Upgrade to 2025-08-01-preview
 
-[`2025-08-01-preview`](/rest/api/searchservice/search-service-api-versions#2025-08-01-preview) introduces the following breaking changes to knowledge agents created using `2025-05-01-preview`:
+[`2025-08-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) introduces the following breaking changes to knowledge agents created using `2025-05-01-preview`:
 
 + Replaces `targetIndexes` with `knowledgeSources`.
 + Removes `defaultMaxDocsForReranker` without replacement.
@@ -126,15 +126,15 @@ Otherwise, there are no behavior changes on existing APIs. You can swap in the n
 
 ### Upgrade to 2025-05-01-preview
 
-[`2025-05-01-preview`](/rest/api/searchservice/search-service-api-versions#2025-05-01-preview) provides new features, but there are no behavior changes on existing APIs. You can swap in the new API version and your code runs the same as before.
+[`2025-05-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) provides new features, but there are no behavior changes on existing APIs. You can swap in the new API version and your code runs the same as before.
 
 ### Upgrade to 2025-03-01-preview
 
-[`2025-03-01-preview`](/rest/api/searchservice/search-service-api-versions#2025-03-01-preview) provides new features, but there are no behavior changes on existing APIs. You can swap in the new API version and your code runs the same as before.
+[`2025-03-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-03-01-preview&preserve-view=true) provides new features, but there are no behavior changes on existing APIs. You can swap in the new API version and your code runs the same as before.
 
 ### Upgrade to 2024-11-01-preview
 
-[`2024-11-01-preview`](/rest/api/searchservice/search-service-api-versions#2024-11-01-preview) query rewrite, Document Layout skill, keyless billing for skills processing, Markdown parsing mode, and rescoring options for compressed vectors.
+[`2024-11-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-11-01-preview&preserve-view=true) query rewrite, Document Layout skill, keyless billing for skills processing, Markdown parsing mode, and rescoring options for compressed vectors.
 
 If you're upgrading from `2024-09-01-preview`, you can swap in the new API version and your code runs the same as before.
 
@@ -147,21 +147,21 @@ Backwards compatibility is preserved due to an internal API mapping, but we reco
 
 ### Upgrade to 2024-09-01-preview
 
-[`2024-09-01-preview`](/rest/api/searchservice/search-service-api-versions#2024-09-01-preview) adds Matryoshka Representation Learning (MRL) compression for text-embedding-3 models, targeted vector filtering for hybrid queries, vector subscore details for debugging, and token chunking for [Text Split skill](cognitive-search-skill-textsplit.md).
+[`2024-09-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-09-01-preview&preserve-view=true) adds Matryoshka Representation Learning (MRL) compression for text-embedding-3 models, targeted vector filtering for hybrid queries, vector subscore details for debugging, and token chunking for [Text Split skill](cognitive-search-skill-textsplit.md).
 
 If you're upgrading from `2024-05-01-preview`, you can swap in the new API version and your code runs the same as before.
 
 ### Upgrade to 2024-07-01
 
-[`2024-07-01`](/rest/api/searchservice/search-service-api-versions#2024-07-01) is a general release. The former preview features are now generally available: integrated chunking and vectorization (Text Split skill, AzureOpenAIEmbedding skill), query vectorizer based on AzureOpenAIEmbedding, vector compression (scalar quantization, binary quantization, stored property, narrow data types).
+[`2024-07-01`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-07-01&preserve-view=true) is a general release. The former preview features are now generally available: integrated chunking and vectorization (Text Split skill, AzureOpenAIEmbedding skill), query vectorizer based on AzureOpenAIEmbedding, vector compression (scalar quantization, binary quantization, stored property, narrow data types).
 
 There are no breaking changes if you upgrade from `2024-05-01-preview` to stable. To use the new stable release, change the API version and test your code.
 
 There are breaking changes if you upgrade directly from `2023-11-01`. Follow the steps outlined for each newer preview to migrate from `2023-11-01` to `2024-07-01`.
 
 ### Upgrade to 2024-05-01-preview
 
-[`2024-05-01-preview`](/rest/api/searchservice/search-service-api-versions#2024-05-01-preview) adds an indexer for Microsoft OneLake, binary vectors, and more embedding models.
+[`2024-05-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true) adds an indexer for Microsoft OneLake, binary vectors, and more embedding models.
 
 If you're upgrading from `2024-03-01-preview`, the AzureOpenAIEmbedding skill now requires a model name and dimensions property.
 
@@ -171,7 +171,7 @@ If you're upgrading from `2024-03-01-preview`, the AzureOpenAIEmbedding skill no
 
 ### Upgrade to 2024-03-01-preview
 
-[`2024-03-01-preview`](/rest/api/searchservice/search-service-api-versions#2024-03-01-preview) adds narrow data types, scalar quantization, and vector storage options.
+[`2024-03-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-03-01-preview&preserve-view=true) adds narrow data types, scalar quantization, and vector storage options.
 
 If you're upgrading from `2023-10-01-preview`, there are no breaking changes. However, there's one behavior difference: for `2023-11-01` and newer previews, the `vectorFilterMode` default changed from postfilter to prefilter for [filter expressions](vector-search-filters.md).
 
@@ -181,15 +181,15 @@ If you're upgrading from `2023-10-01-preview`, there are no breaking changes. Ho
 
 ### Upgrade to 2023-11-01
 
-[`2023-11-01`](/rest/api/searchservice/search-service-api-versions#2023-11-01) is a general release. The former preview features are now generally available: semantic ranker and vector support.
+[`2023-11-01`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2023-11-01&preserve-view=true) is a general release. The former preview features are now generally available: semantic ranker and vector support.
 
 There are no breaking changes from `2023-10-01-preview`, but there are multiple breaking changes from `2023-07-01-preview` to `2023-11-01`. For more information, see [Upgrade from 2023-07-01-preview](#upgrade-from-2023-07-01-preview).
 
 To use the new stable release, change the API version and test your code.
 
 ### Upgrade to 2023-10-01-preview
 
-[`2023-10-01-preview`](/rest/api/searchservice/search-service-api-versions#2023-10-01-preview) was the first preview version to add [built-in data chunking and vectorization during indexing](vector-search-integrated-vectorization.md) and [built-in query vectorization](vector-search-how-to-configure-vectorizer.md). It also supports vector indexing and queries from the previous version.
+[`2023-10-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2023-10-01-preview&preserve-view=true) was the first preview version to add [built-in data chunking and vectorization during indexing](vector-search-integrated-vectorization.md) and [built-in query vectorization](vector-search-how-to-configure-vectorizer.md). It also supports vector indexing and queries from the previous version.
 
 If you're upgrading from the previous version, the next section has the steps.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索 API のマイグレーションに関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、Azure AI の検索 API マイグレーションに関するドキュメント内のリンクと内容を更新したものです。変更点には、API バージョンのリンクが変更され、リリースノートや新機能に関する情報をより明確にするための修正が含まれています。また、安定版とプレビュー版のそれぞれの情報が一貫性を持つように更新され、API のアップグレード手順が改善されています。

具体的には、次のような変更が行われました：
- REST API のいくつかのリンクが変更され、より適切な情報源に向けられるようになっています。
- アップグレード手順の文言が更新され、技術者が新しい API バージョンのリリース内容をより簡単に把握できるように改善されています。
- その他、既存のAPIに対する影響を明示するための情報内容が強化されています。

全体として、この更新はドキュメントの明確さと正確性を高め、開発者が新しいAPIバージョンにスムーズに移行できるよう支援することを目的としています。

## articles/search/search-api-preview.md{#item-511f5d}

<details>
<summary>Diff</summary>
````diff
@@ -86,7 +86,7 @@ If you write code against a preview API, you should prepare to upgrade that code
 
 Preview REST APIs are accessed through the api-version parameter on the URI. Older previews are still operational but become stale over time and aren't updated with new features or bug fixes.
 
-For data plane operations on content, [**`2025-11-01-preview`**](/rest/api/searchservice/search-service-api-versions#2025-11-01-preview) is the most recent preview version. The following example shows the syntax for [Indexes GET (preview)](/rest/api/searchservice/indexes/get?view=rest-searchservice-2025-11-01-preview&preserve-view=true):
+For data plane operations on content, [**`2025-11-01-preview`**](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) is the most recent preview version. The following example shows the syntax for [Indexes GET (preview)](/rest/api/searchservice/indexes/get?view=rest-searchservice-2025-11-01-preview&preserve-view=true):
 
 ```rest
 GET {endpoint}/indexes('{indexName}')?api-version=2025-11-01-Preview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索 API プレビューセクションのリンク修正"
}
```

### Explanation
このコードの変更は、Azure の検索 API プレビューに関するドキュメント内のリンクを更新したものです。具体的には、データプレーン操作に関する最新のプレビュー API バージョンへのリンクが修正されています。

変更点は以下の通りです：
- 以前は“search-service-api-versions”を指していたリンクが、“operation-groups”を指すように変更され、API の運用に関する情報がより適切な場所に結び付けられました。
- これは、新しい API バージョン（`2025-11-01-preview`）のリファレンスがこの場所で正確に見つけられるようにするためのもので、ドキュメントの流れと一貫性が向上しています。

全体として、今回の変更は、プレビュー API についてのユーザーの理解を助け、より正確な情報提供を実現するものです。

## articles/search/vector-search-how-to-query.md{#item-9bb93c}

<details>
<summary>Diff</summary>
````diff
@@ -135,7 +135,7 @@ api-key: {{admin-api-key}}
 
 ### [**2025-11-01-preview**](#tab/query-2025-11-01-preview)
 
-[**2025-11-01-preview**](/rest/api/searchservice/search-service-api-versions#2025-11-01-preview) is the latest preview API version of [Search - POST](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&tabs=HTTP&preserve-view=true). It supports the same vector query syntax as **2025-09-01**, but it has extra parameters for hybrid search and minimum thresholds for excluding weaker results.
+[**2025-11-01-preview**](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) is the latest preview API version of [Search - POST](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&tabs=HTTP&preserve-view=true). It supports the same vector query syntax as **2025-09-01**, but it has extra parameters for hybrid search and minimum thresholds for excluding weaker results.
 
 This preview supports:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクター検索クエリのドキュメント修正"
}
```

### Explanation
このコードの変更は、Azure のベクター検索に関するクエリのドキュメント内のリンクを更新したものです。具体的には、最新のプレビュー API バージョン（`2025-11-01-preview`）へのリンクが修正されています。

変更点は以下の通りです：
- 既存のリンクが「search-service-api-versions」を指していたところを、「operation-groups」を指すように変更されました。これにより、文書がより正確な情報源に結びついています。
- 説明文もそのまま残されており、新しいプレビュー API バージョンが提供する機能についての詳細は変更されていないまま、リンクの正確性が向上しています。

全体的に、この更新は文書の一貫性を保ちながら、ユーザーに対し最新のプレビュー版の情報を確実に提供することを目的としています。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -60,7 +60,7 @@ Learn about the latest updates to Azure AI Search functionality, docs, and sampl
 | September | General availability | [Truncate dimensions](vector-search-how-to-truncate-dimensions.md). |
 | September | General availability | [Unpack `@search.score` to view subscores in hybrid search results](hybrid-search-ranking.md#unpack-a-search-score-into-subscores). | 
 | September | Portal update | The Azure portal is undergoing a three-phase rollout to [unify the two import wizards](search-import-data-portal.md). For Phase 1, the **Import and vectorize data** wizard has been renamed to **Import data (new)** and redeveloped to support keyword search, modernizing the legacy **Import data** workflow with an improved interface and user experience.<p>**Import data (new)** isn't a direct replacement for the old wizard. For example, it supports fewer skills for keyword search.<p>Both wizards are currently available, but **Import data** will be deprecated in a future phase. |
-| September | Security | [Support for Azure confidential computing](search-security-overview.md#data-in-use). Configure [confidential computing](/azure/confidential-computing/use-cases-scenarios) during service creation to process data in use on confidential VMs. This compute type isn't intended for general use, but rather for stringent regulatory, compliance, or security requirements.<p>Confidential computing adds a 10% surcharge to the base cost of billable tiers. For more information, see the [pricing page](https://azure.microsoft.com/pricing/details/search/).<p>Now generally available through the 2025-05-01 version of [Services - Create or Update (REST API)](/rest/api/searchmanagement/services/create-or-update?view=rest-searchservice-2025-05-01&preserve-view=true) and the [Azure portal](search-create-service-portal.md#choose-a-compute-type). |
+| September | Security | [Support for Azure confidential computing](search-security-overview.md#data-in-use). Configure [confidential computing](/azure/confidential-computing/use-cases-scenarios) during service creation to process data in use on confidential VMs. This compute type isn't intended for general use, but rather for stringent regulatory, compliance, or security requirements.<p>Confidential computing adds a 10% surcharge to the base cost of billable tiers. For more information, see the [pricing page](https://azure.microsoft.com/pricing/details/search/).<p>Now generally available through the 2025-05-01 version of [Services - Create or Update (REST API)](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2025-05-01&preserve-view=true) and the [Azure portal](search-create-service-portal.md#choose-a-compute-type). |
 | August | REST API | [Search Service 2025-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true). New preview REST API version providing programmatic access to the data plane operations described in this table. |
 | August | Agentic retrieval | [Knowledge agents (preview)](agentic-retrieval-how-to-create-knowledge-base.md). Architectural changes to the knowledge agent definition, which now requires one or more `knowledgeSources` instead of `targetIndexes` and deprecates `defaultMaxDocsForReranker`. New `retrievalInstructions` and `outputConfiguration` properties provide greater control over query planning and execution. For help with breaking changes, see [Migrate your agentic retrieval code](agentic-retrieval-how-to-migrate.md). |
 | August | Agentic retrieval | [Knowledge sources (preview)](agentic-knowledge-source-overview.md). New REST APIs for creating and managing knowledge sources, which represent content that knowledge agents use to ground and answer queries. In this preview, you can create knowledge sources for [search indexes](agentic-knowledge-source-how-to-search-index.md) and [Azure blobs](agentic-knowledge-source-how-to-blob.md).  |
@@ -90,9 +90,9 @@ Learn about the latest updates to Azure AI Search functionality, docs, and sampl
 | March | Pricing | [Pricing tier change (preview)](search-capacity-planning.md#change-your-pricing-tier). Change the [pricing tier](search-sku-tier.md) of your search service. This provides flexibility to scale storage, increase request throughput, and decrease latency based on your needs. Initially, this preview only supported upgrades between Basic and Standard (S1, S2, and S3) tiers, but starting in July 2025, it supports upgrades *and* downgrades between these tiers. Available in [Update Service (2025-02-01-preview)](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true#searchupdateservicewithsku) and the Azure portal. |
 | March | Queries | [Facet hierarchies, aggregations, and facet filters (preview)](search-faceted-navigation-examples.md). New facet query parameters support nested facets. For numeric facetable fields, you can sum the values of each field. You can also specify filters on a facet to add inclusion or exclusion criteria. Available in [Search Documents (2025-03-01-preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-03-01-preview&preserve-view=true) and the Azure portal.|
 | March | Vector search | [Rescore vector queries over binary quantization using full precision vectors (preview)](vector-search-how-to-quantization.md#supported-rescoring-techniques). For vector indexes that contain binary quantization, you can rescore query results using a full precision vector query. The query engine uses the dot product of the binary embeddings and the vector query for rescoring, which improves the quality of search results.  Set `enableRescoring` and `discardOriginals` to use this feature, and call the latest preview API version on the request.|
-| March | Queries | [Semantic ranker prerelease models (preview)](semantic-how-to-configure.md#opt-in-for-prerelease-semantic-ranking-models). Opt in to use prerelease semantic ranker models if one happens to be available in your region. Available in [Create or Update Index (2025-03-01-preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview#semanticconfiguration&preserve-view=true).|
-| March | REST API | [Search Service REST 2025-03-01-preview](/rest/api/searchservice/search-service-api-versions?view=rest-searchservice-2025-03-01-preview&preserve-view=true). Preview release of REST APIs for data plane operations. Adds support for multi-vector embeddings, hierarchical facets, facet aggregation, and facet filters. |
-| March | REST API | [Search Management 2025-02-01-preview](/rest/api/searchmanagement/management-api-versions?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true). Preview release of REST APIs for control plane operations. Adds support for in-place upgrade to higher capacity partitions, in-place upgrade to higher tiers, and Azure Confidential Compute. |
+| March | Queries | [Semantic ranker prerelease models (preview)](semantic-how-to-configure.md#opt-in-for-prerelease-semantic-ranking-models). Opt in to use prerelease semantic ranker models if one happens to be available in your region. Available in [Create or Update Index (2025-03-01-preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true#semanticconfiguration).|
+| March | REST API | [Search Service REST 2025-03-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-03-01-preview&preserve-view=true). Preview release of REST APIs for data plane operations. Adds support for multi-vector embeddings, hierarchical facets, facet aggregation, and facet filters. |
+| March | REST API | [Search Management 2025-02-01-preview](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true). Preview release of REST APIs for control plane operations. Adds support for in-place upgrade to higher capacity partitions, in-place upgrade to higher tiers, and Azure Confidential Compute. |
 | April | Demo | [RAG Time Journey](https://github.com/microsoft/rag-time). Code and video demonstrations of Retrieval Augmented Generation (RAG) workflows that use Azure AI Search. Segments include fundamentals, patterns and use-cases, [vector indexing at scale](https://github.com/microsoft/rag-time/tree/main/Journey%203%20-%20Optimize%20your%20Vector%20Index%20for%20Scale), and [agentic search](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/bonus-rag-time-journey-agentic-rag/4404652) where you use an agent to evaluate a result and generate a better answer. |
 | February | Security | [Customer-managed keys support for Managed HSM](search-security-manage-encryption-keys.md). Use either Azure Key Vault or Azure Key Vault Managed HSM (Hardware Security Module) to store customer-managed keys for extra encryption of sensitive content. |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whats New ドキュメントの段落修正"
}
```

### Explanation
このコードの変更は、「Whats New」ドキュメントの内容の一部を修正したものです。具体的には、いくつかの機能や更新情報の説明をより正確にするために、リンクやテキストの表現が見直されています。

変更点は以下の通りです：
- Azure の新しいプレビュー API バージョンとして、特定のリンクが更新されており、これにより正しい情報へのアクセスが可能となっています。
- 特定のセクションが再編成され、文の流れと一貫性が向上しました。たとえば、セキュリティ関連の機能情報が整理され、新しい料金体系やバージョンの情報が追加されています。
- 変更された内容は、最新の機能やプレビューに関する詳細情報を提供し、ユーザーが Azure AI Search の機能の進化をより理解できるように配慮されています。

この更新は、ドキュメントを通じて最新の情報を提供し、ユーザー体験を向上させることを目的としています。


