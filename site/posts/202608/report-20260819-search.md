---
date: '2026-08-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a8ff591...MicrosoftDocs:8250a49
summary: このドキュメントの更新において、Azure AI Searchのインデクサに関連する実行時間、クォータ、制限に関する重要な情報が変更されました。特に、インデクサの実行時間制限が2時間、累積実行時間のデイリークォータが24時間に設定され、複数インデクサの同時運用時にクォータ管理が求められます。また、サーバーレスや高密度インデクサにおける運用のベストプラクティスも更新され、APIレスポンスの情報も強化されています。これにより、ユーザーはインデクサのパフォーマンスをより効果的に制御し、効率的な検索サービスの運営が可能になります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a8ff591...MicrosoftDocs:8250a49){target="_blank"}

<format>
# ハイライト
このドキュメントの更新では、Azure AI Searchにおけるインデクサの実行時間、クォータ、制限に関する情報が変更されたことに焦点を当てています。特に重要なのは、インデクサの実行時間制限が2時間で、累積実行時間のデイリークォータが24時間に変更されたことです。これにより、複数のインデクサが同時に実行されるときにクォータをより効果的に管理する必要があります。また、S3 HDやサーバーレス環境における新しいベストプラクティスとAPIレスポンスに関する情報も更新されています。

## 新機能
- サーバーレスおよび高密度インデクサの実行時間クォータが、24時間に拡張。
- Azure AI Searchの最新機能におけるランタイム追跡情報が強化され、サーバーレス環境にも対応。

## 破壊的変更
- 各インデクサ実行時間が2時間に限定され、サービス全体で24時間の累積クォータを使用すること。

## その他の更新
- 特定のワークロードに基づく推奨されるドキュメント数が示され、キャパシティ計画における考慮点として説明されています。
- インデクサの効率を高めるためのベストプラクティスが追加されました。

# インサイト
Azure AI Searchのインデクサに関するドキュメントの最新更新は、ユーザーがインデクサのパフォーマンスをより正確に制御し、最適化するための情報を提供することに重点を置いています。具体的には、実行時間のクォータや制限に関する明確なガイドラインや、パフォーマンスを向上させるためのベストプラクティスが含まれており、ユーザーはこれを活用することで効率的な検索サービス管理を行うことが可能です。

サーバーレス環境での実行時間制限の明確化と、累積クォータの共有に関する情報は、リソースの効率的な利用を促進し、サービスの持続可能性を向上させます。また、APIレスポンスに関する情報の詳細化は、運用上の透明性を高め、トラブルシューティングやリソースプランニングでの即時対応を支援します。

これらの更新により、Azure AI Searchのユーザーは、より現実的なキャパシティ計画を立て、管理リソースの最適化が可能となり、ビジネスニーズにあった検索機能をより確実に提供できるようになります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-howto-run-reset-indexers.md](#item-fb10c8) | minor update | インデクサの実行時間クォータに関する情報の更新 | modified | 10 | 8 | 18 | 
| [search-indexer-high-density-serverless-overview.md](#item-2bc606) | minor update | サーバーレスおよび高密度インデクサに関する概要の更新 | modified | 32 | 7 | 39 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | インデクサの制限とクォータに関する情報の更新 | modified | 7 | 4 | 11 | 
| [whats-new.md](#item-fa71b4) | minor update | Azure AI Searchの新機能に関する情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-howto-run-reset-indexers.md{#item-fb10c8}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Run or Reset Indexers
 description: Run indexers in full, or reset an indexer, skills, or individual documents to refresh all or part of a search index or knowledge store.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/07/2026
+ms.date: 08/17/2026
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
@@ -334,25 +334,27 @@ To check the reset status and see which document keys are queued for processing,
 
 1. After the indexer reprocesses the documents, run Get Indexer Status again. The indexer returns to the **`indexingAllDocs`** mode and processes any new or updated documents on the next run.
 
-## Check indexer runtime quota for S3 HD search services
+## Check indexer runtime quota for S3 HD and Serverless search services
 
-Applies to search services at the Standard 3 High Density (S3 HD) pricing tier.
+This section applies to Standard 3 High Density (S3 HD) and Serverless search services. For aggregate quota behavior and planning guidance, see [Indexer execution on Serverless and S3 HD](search-indexer-high-density-serverless-overview.md).
 
-To help you monitor indexer running times relative to the 24-hour window, [Get Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics#servicestatistics?view=rest-searchservice-2026-05-01-preview&preserve-view=true) and [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&preserve-view=true) now return more information in the response.
+Each indexer run has a two-hour maximum. Separately, all indexers share 24 hours of cumulative runtime per service in each 24-hour UTC window.
+
+To help you monitor indexer running times relative to the 24-hour window, [Get Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics?view=rest-searchservice-2026-05-01-preview&preserve-view=true#servicestatistics) and [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&preserve-view=true) now return more information in the response.
 
 ### Track cumulative runtime quota
 
-Track a search service's cumulative indexer runtime usage and determine how much runtime quota is left within the current 24-hour window period.
+Track a search service's cumulative indexer runtime usage and determine how much runtime quota is left within the current 24-hour window.
 
-Send a GET request to the search service resource provider. For help with setting up a REST client and getting an access token, see [Connect to a search service](/azure/search/search-get-started-rbac?pivots=rest).
+Send a GET request to the search service endpoint. For help with setting up a REST client and getting an access token, see [Connect to a search service](/azure/search/search-get-started-rbac?pivots=rest).
 
 ```http
 GET {{search-endpoint}}/servicestats?api-version=2026-05-01-preview 
   Content-Type: application/json
   Authorization: Bearer {{accessToken}}
 ```
 
-Responses include `indexersRuntime` properties, showing start and end times, seconds used, seconds remaining, and cumulative runtime within the last 24 hours.
+Responses include `indexersRuntime` properties that show the window start and end times, cumulative seconds used by all indexers, and seconds remaining for the service.
 
 ### Track indexer runtime quota
 
@@ -364,7 +366,7 @@ GET {{search-endpoint}}/indexers/hotels-sample-indexer/search.status?api-version
   Authorization: Bearer {{accessToken}}
 ```
 
-Responses include a `runtime` properties, showing start and end times, seconds used, and seconds remaining.
+Responses include `runtime` properties that show the window start and end times, seconds used by the indexer, and seconds remaining for all indexers in the service.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサの実行時間クォータに関する情報の更新"
}
```

### Explanation
この変更では、Azure AI Searchに関するドキュメントが更新されました。具体的には、インデクサの実行状況やクォータに関する新しい情報が追加されています。ドキュメントの最終更新日が2026年7月7日から2026年8月17日に変更され、S3 HDおよびサーバーレス検索サービスに関する説明が強化されました。特に、インデクサの実行時間に関する制限が明確にされ、各インデクサ実行の最大時間が二時間であることや、サービス全体での24時間の累積実行時間の制限が説明されています。

また、インデクサの実行時間に関する統計情報を取得するためのAPIエンドポイントも変更されており、レスポンスには開始・終了時間、使用された秒数および残りの時間に関する詳細情報が含まれることが明記されています。これにより、ユーザーはインデクサの利用状況をより効果的に監視することができるようになります。

## articles/search/search-indexer-high-density-serverless-overview.md{#item-2bc606}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how Azure AI Search runs indexers, applies daily runtime quot
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 08/08/2026
+ms.date: 08/17/2026
 ai-usage: ai-assisted
 ms.custom: doc-kit-assisted
 ---
@@ -49,12 +49,14 @@ Indexer execution is governed by a daily runtime quota that resets at 00:00 UTC.
 + **Service level:** It applies to the search service as a whole.
 + **Cumulative:** Runtime from every indexer in the service counts toward the same budget. The quota isn't applied per indexer.
 
+All running indexers accrue time against one shared service budget. The service doesn't reserve runtime for individual indexers or automatically divide the quota equally among them. For example, the cumulative durations of 12 indexers that each run for two hours can consume all 24 aggregate runtime hours, whether the runs overlap or occur at different times.
+
 The following table lists the daily quota by SKU and the minimum API version that supports it:
 
 | SKU | Daily quota per 24-hour UTC window | Minimum API version |
 |-----|------------------------------------|---------------------|
-| S3 HD | 6 hours | `2025-11-01-preview` |
-| Serverless | 6 hours | `2026-05-01-preview` |
+| S3 HD | 24 hours | `2025-11-01-preview` |
+| Serverless | 24 hours | `2026-05-01-preview` |
 
 When the daily quota is exhausted:
 
@@ -72,6 +74,10 @@ To recover from quota exhaustion and reduce the likelihood of hitting it again:
 
 + Put indexers on [staggered schedules](search-howto-schedule-indexers.md) so that work spreads across the 24-hour window instead of running concurrently.
 
++ You can't pause or stop active runs. Use [Get Indexer Status](/rest/api/searchservice/indexers/get-status) to monitor them, and see [Run or reset indexers](search-howto-run-reset-indexers.md#indexer-execution) for runtime control behavior.
+
++ If runtime remains but indexer runs fail, see [Troubleshoot indexer issues](search-indexer-troubleshooting.md).
+
 + Reduce skillset cost. Skills that call external services, such as the [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md), [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md), and [Azure Content Understanding skill](cognitive-search-skill-content-understanding.md), consume runtime quickly. Lower the number of skills, batch documents, or [configure an enrichment cache](enrichment-cache-how-to-configure.md) to reuse prior results instead of reprocessing.
 
 + Monitor `remainingSeconds` proactively at both the service and indexer level so that you can throttle workloads before they fail.
@@ -88,12 +94,12 @@ Use [Get Service Statistics](/rest/api/searchservice/get-service-statistics/get-
 GET {endpoint}/servicestats?api-version=2026-05-01-preview
 ```
 
-The response includes an `indexersRuntime` section. The following JSON shows a service whose six-hour daily quota hasn't been used:
+The response includes an `indexersRuntime` section. The following JSON shows a service whose 24-hour daily quota isn't used:
 
 ```json
 "indexersRuntime": {
     "usedSeconds": 0,
-    "remainingSeconds": 21600,
+    "remainingSeconds": 86400,
     "beginningTime": "2026-05-16T00:00:00.000Z",
     "endingTime": "2026-05-17T00:00:00.000Z"
 }
@@ -113,12 +119,12 @@ Use [Get Indexer Status](/rest/api/searchservice/indexers/get-status) (REST API)
 GET {endpoint}/indexers('{indexerName}')/search.status?api-version=2026-05-01-preview
 ```
 
-The response includes a `runtime` section. The following JSON shows an indexer on a service whose six-hour daily quota hasn't been used:
+The response includes a `runtime` section. The following JSON shows an indexer on a service whose 24-hour daily quota isn't used:
 
 ```json
 "runtime": {
     "usedSeconds": 0,
-    "remainingSeconds": 21600,
+    "remainingSeconds": 86400,
     "beginningTime": "2026-05-16T00:00:00.000Z",
     "endingTime": "2026-05-17T00:00:00.000Z"
 }
@@ -144,6 +150,25 @@ During the preview, S3 HD indexer support is designed for workloads with no skil
 
 + Expect limited parallelism during the preview. Use scheduled, staggered runs for large indexer fleets so that work spreads across the 24-hour window rather than competing for the same budget.
 
+#### Illustrative split-and-embed workload
+
+In one controlled S3 HD test, a Split skill and one Azure OpenAI Embedding skill generated chunks and embeddings. The workload produced approximately 2.5 chunks per source document, and approximately 22,000 source documents were observed in this test during one 24-hour S3 HD test window.
+
+The following values are rounded, illustrative fair-share arithmetic based on the aggregate observation. They aren't measured per-indexer results.
+
+| Indexer count | Illustrative source documents per indexer per day |
+|---------------|---------------------------------------------------|
+| 100 | About 200 |
+| 500 | About 40 |
+| 1,000 | About 20 |
+
+The service doesn't reserve capacity or guarantee equal distribution, execution order, or throughput for these indexer counts.
+
+> [!NOTE]
+> This result was observed in one controlled test. It isn't a performance target, service guarantee, capacity commitment, sizing formula, or substitute for testing your workload.
+
+Throughput can vary materially with document complexity and profile, chunking, the number and type of skills and vector outputs, model latency, capacity, and quota, source and target performance, concurrency, scheduling order, throttling, region, failures and retries, document cracking or optical character recognition (OCR), and uneven tenant volumes. Test with representative production inputs before you plan capacity.
+
 ### Serverless
 
 During the preview, Serverless indexers are designed to simplify ingestion for retrieval-augmented generation (RAG) and knowledge base scenarios:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスおよび高密度インデクサに関する概要の更新"
}
```

### Explanation
この変更では、Azure AI Searchにおける高密度およびサーバーレスインデクサの概要に関するドキュメントが更新されました。主な変更点として、インデクサの実行時間に関するデイリーのクォータが6時間から24時間に引き上げられ、すべてのインデクサが共有のサービス予算に対して時間を蓄積することが強調されています。そのため、複数のインデクサが同時に実行されると、すべてのインデクサの運用時間が累積され、1日の合計クォータを使い尽くしてしまう可能性があります。

ドキュメントには、インデクサがクォータの消費を抑えるためのベストプラクティスや、効率的なスケジュール設定に関するアドバイスも追加されています。また、APIレスポンスに関する詳細が改訂され、使用済みの秒数や残りの秒数に関する新しい情報が盛り込まれています。

さらに、特定のワークロードの例として、S3 HD環境での定量テスト結果が提示され、異なるインデクサ数に基づく推奨されるドキュメント数が示されています。このテスト結果は、実際のパフォーマンス目標やサービス保証とは異なるものであり、容量計画のためには実際の使用状況を考慮することが重要です。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: mattwojo
 ms.author: mattwoj
 ms.service: azure-ai-search
 ms.topic: limits-and-quotas
-ms.date: 08/08/2026
+ms.date: 08/17/2026
 ms.update-cycle: 180-days
 ai-usage: ai-assisted
 ms.custom:
@@ -216,7 +216,7 @@ This quota is a hard limit to ensure your service remains healthy. Further index
 Maximum running times exist to provide balance and stability to the service as a whole, but larger data sets might need more indexing time than the maximum allows. If an indexing job can't complete within the maximum time allowed, try running it on a schedule. The scheduler keeps track of indexing status. If a scheduled indexing job is interrupted for any reason, the indexer can pick up where it last left off at the next scheduled run.
 
 > [!NOTE]
-> In the Serverless pricing model, indexer behavior differs from Dedicated services. Capacity isn't defined by replicas or partitions. Instead, per-service object limits, per-index storage caps, and service-level throttling govern indexing limits. As a result, some limits, such as maximum execution time, aren't fixed values.
+> In the Serverless pricing model, indexer behavior differs from Dedicated services. Capacity isn't defined by replicas or partitions. Instead, per-service object limits, per-index storage caps, and service-level throttling govern indexing limits. The maximum running time per Serverless Developer indexer run is two hours.
 
 ### Indexer object and throughput limits
 
@@ -227,18 +227,21 @@ Maximum running times exist to provide balance and stability to the service as a
 | Maximum skillsets <sup>4</sup> | 3 | 5 or 15 | 50 | 200 | 200 | N/A | 10 | 10 | 30 |
 | Maximum indexing load per invocation | 10,000 docs | Limited only by max docs | Limited only by max docs | Limited only by max docs | Limited only by max docs | N/A | No limit | No limit | Limited only by max docs |
 | Minimum schedule | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min |
-| Maximum running time <sup>5</sup> | 1-3 or 3-10 min | 2 or 24 hours | 2 or 24 hours | 2 or 24 hours | 2 or 24 hours | N/A | 2 or 24 hours | 2 or 24 hours | 2 hours |
+| Maximum running time per indexer run <sup>5</sup> | 1-3 or 3-10 min | 2 or 24 hours | 2 or 24 hours | 2 or 24 hours | 2 or 24 hours | 2 hours | 2 or 24 hours | 2 or 24 hours | 2 hours |
+| Cumulative indexer runtime per service <sup>6</sup> | N/A | N/A | N/A | N/A | N/A | 24 hours | N/A | N/A | 24 hours |
 
 <sup>1</sup> Free services have indexer maximum execution time of 3 minutes for blob sources and 1 minute for all other data sources. Indexer invocation is once every 180 seconds. For AI indexing that calls Foundry Tools, free services are limited to 20 free transactions per indexer per day, where a transaction is defined as a document that successfully passes through the enrichment pipeline. (Tip: You can reset an indexer to reset its count.)
 
 <sup>2</sup> Basic services created before December 2017 have lower limits (5 instead of 15) on indexers, data sources, and skillsets.
 
-<sup>3</sup> S3 HD indexer support is in preview, requires the `2025-11-01-preview` REST API version or later, and is governed by a service-level daily quota of six hours of cumulative indexer runtime shared across all indexers. S3 HD indexers run only in the [multitenant execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment) and don't support [shared private link resources](search-indexer-howto-access-private.md). During the preview, S3 HD indexer support is best suited for small workloads (approximately 1 GB index size) with no or minimal skillsets. For more information, see [Indexer execution on Serverless and S3 HD](search-indexer-high-density-serverless-overview.md).
+<sup>3</sup> S3 HD indexer support is in preview and requires the `2025-11-01-preview` REST API version or later. S3 HD indexers run only in the [multitenant execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment) and don't support [shared private link resources](search-indexer-howto-access-private.md). During the preview, S3 HD indexer support is best suited for small workloads (approximately 1 GB index size) with no or minimal skillsets. For aggregate behavior, monitoring, and planning guidance, see [Indexer execution on Serverless and S3 HD](search-indexer-high-density-serverless-overview.md).
 
 <sup>4</sup> Maximum of 30 skills per skillset.
 
 <sup>5</sup> Regarding the 2 or 24 hour maximum duration for indexers: a 2-hour maximum is the most common and it's what you should plan for. It refers to indexers that run in the [public environment](search-howto-run-reset-indexers.md#indexer-execution-environment), which offloads computationally intensive processing and leaves more resources for queries. The 24-hour limit applies if you configure the indexer to run in a private environment using only the infrastructure that's allocated to your search service. Some older indexers are incapable of running in the public environment, and those indexers always have a 24-hour processing range. If you have unscheduled indexers that run continuously for 24 hours, you can assume those indexers couldn't be migrated to the newer infrastructure. As a general rule, for indexing jobs that can't finish within two hours, put the indexer on a [5-minute schedule](search-howto-schedule-indexers.md) so that the indexer can quickly pick up where it left off. On the Free tier, the 3-10 minute maximum running time is for indexers with skillsets.
 
+<sup>6</sup> On S3 HD and Serverless services, all indexers share 24 hours of cumulative runtime per service in each 24-hour UTC window. For quota behavior, monitoring, and planning guidance, see [Indexer execution on Serverless and S3 HD](search-indexer-high-density-serverless-overview.md).
+
 ### Source-file limits for blob-like indexers
 
 File processing happens in stages, and each stage has its own limits:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサの制限とクォータに関する情報の更新"
}
```

### Explanation
この変更では、Azure AI Searchのインデクサに関する制限やクォータに関するドキュメントを更新しました。主な変更点として、サーバーレスの価格モデルにおけるインデクサの最大実行時間が明確にされ、各サーバーレスインデクサの実行が2時間に制限されることが記載されています。これにより、インデクサの動作が専用サービスとは異なることが強調されています。

また、S3 HDインデクサのサポートがプレビューであり、従来の運用と比較して新しい制御を可能にすることが述べられています。累積実行時間に関する情報も更新され、サーバーレスおよびS3 HDインデクサが24時間の累積クォータを共有することが強調されています。

さらに、インデクサの設定に関するベストプラクティスや、パフォーマンスの向上のためにインデクサを5分ごとにスケジュールすることを推奨する内容が追加され、ユーザーがインデクサの効率を高めるための手助けとなる情報が提供されています。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -128,7 +128,7 @@ Learn about the latest updates to Azure AI Search functionality, documentation,
 | August | Agentic retrieval | [Answer synthesis (preview)](agentic-retrieval-how-to-answer-synthesis.md). New `answerSynthesis` modality for knowledge agents. When specified, an LLM generates a natural-language answer as an embedded step in the retrieval pipeline. This differs from the default `extractiveData` modality, which returns raw search results for downstream processing. |
 | August | Agentic retrieval | "Fast path" for knowledge agents (preview). (Removed in the 2025-11-01-preview. This documentation no longer exists). The `attemptFastPath` boolean in knowledge agents enabled a shorter processing time if queries are concise and the initial response is sufficiently relevant. Replacement feature is the minimal retrieval reasoning effort. |
 | August | Agentic retrieval | [Retrieval instructions (preview)](agentic-retrieval-how-to-create-knowledge-base.md). New `retrievalInstructions` property for knowledge agents guides query planning in an agentic retrieval workflow. For example, you can specify criteria for including or excluding specific knowledge sources.  |
-| August | Indexers | [Improved indexer runtime tracking information (preview)](search-howto-run-reset-indexers.md#check-indexer-runtime-quota-for-s3-hd-search-services). Applies to Standard 3 High Density (S3 HD) services only. [Get Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics?view=rest-searchservice-2025-08-01-preview&preserve-view=true) response now provides cumulative indexer processing information for the entire service. [Get Status - Indexers](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-08-01-preview&preserve-view=true) provides the same information, but for a specific indexer. |
+| August | Indexers | [Improved indexer runtime tracking information (preview)](search-howto-run-reset-indexers.md#check-indexer-runtime-quota-for-s3-hd-and-serverless-search-services). Applies to Standard 3 High Density (S3 HD) services only. [Get Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics?view=rest-searchservice-2025-08-01-preview&preserve-view=true) response now provides cumulative indexer processing information for the entire service. [Get Status - Indexers](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-08-01-preview&preserve-view=true) provides the same information, but for a specific indexer. |
 | August | Vector search | [Strict postfiltering for vector queries (preview)](vector-search-filters.md). New `strictPostFilter` mode for the `vectorFilterMode` parameter. When specified, filters are applied after the global top-`k` vector results are identified, ensuring that returned documents are a subset of the unfiltered results. |
 | August | Vector search | [Increased maximum dimensions for vector fields](search-limits-quotas-capacity.md#index-limits).  The maximum dimensions per vector field are now `4096`. This update applies to all stable and preview REST API versions that support vectors and doesn't introduce breaking changes. |
 | July | REST API | [Search Management 2025-05-01](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2025-05-01&preserve-view=true). Stable release of the REST APIs for the control plane operations described in this table. For migration guidance, see [Upgrade to the latest REST API in Azure AI Search](search-api-migration.md). |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchの新機能に関する情報の更新"
}
```

### Explanation
この変更では、Azure AI Searchに関する最新の機能と更新情報のドキュメントが改訂されました。具体的には、インデクサのランタイム追跡情報が強化され、従来の「S3 HDサービス専用」に加えて「サーバーレスサービス」も対象となることが明記されています。

これにより、ユーザーは全体的なサービスに対する累積インデクサ処理情報を取得することができ、特定のインデクサに対する詳細な情報も得られるようになります。この更新は、サービスのパフォーマンスをより効果的にモニタリングし、管理できるようにするためのものです。

その他にも、エージェントによる情報取得機能の新しいプロパティや、ベクトル検索におけるフィルタリング機能に関する情報も更新されています。これらの変更は、関連する機能をより利用しやすくすることを目的としています。


