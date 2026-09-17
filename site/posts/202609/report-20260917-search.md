---
date: '2026-09-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:db0f4dc...MicrosoftDocs:cf104d1
summary: |-
  Azure AI Searchのドキュメントに対する最新の更新内容について、以下のように要約します。

  新機能として、Azure AI Searchの制限と割当の情報が最新化され、ユーザーにとっての理解がしやすくなりました。破壊的変更は特にないものの、表現や情報の更新が、ユーザーの計画に影響を及ぼす可能性があります。また、高需要地域でのデプロイメント計画に関する情報も見直され、よりわかりやすくなりました。これにより、ユーザーはAzure AI Searchのリソースを効果的に利用し、計画やリソース配分において安心感をもってサービスを使用できるようになります。全体として、これらの更新はユーザーに戦略的価値を提供し、利用の透明性と効率性を向上させるものです。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:db0f4dc...MicrosoftDocs:cf104d1){target="_blank"}

# ハイライト

## 新機能
- Azure AI Searchの制限と割当の最新情報が提供されること。

## 破壊的変更
- 破壊的な変更は特にありませんが、表現や情報の更新がユーザーの計画に影響を及ぼすかもしれません。

## その他の更新
- 高需要地域でのAzure AI Searchデプロイメントの計画方法について、情報が更新されわかりやすくなりました。

# 洞察

Azure AI Searchのドキュメントに関する最新の更新は、主に二つのセクションで実施されました。これらの変更は、ユーザーにより正確かつ最新の情報を提供し、特にAzure AI Searchのリソースを効果的に利用するためのサポートを強化することを目的としています。

最初の変更は「検索制限と割当」についてです。このセクションでは、日付の更新や記述の明確化が行われました。特に、検索サービスの制限や割当情報が具体的に記載され、それによりユーザーはAzure AI Searchを利用する際の最新の制約を理解しやすくなります。また、テーブル内の情報も更新され、注釈が付加されることで、利用可能なリソースについての情報透明性が向上しています。ユーザーにとってはこれが非常に有益であり、計画やリソースの配分において安心してサービスを利用できます。

次に、「地域の容量制限」に関する記事の更新です。この記事は「高需要地域」に焦点を当てた内容に変わり、タイトルや説明が再構築されました。新しい文面では、高需要地域でのデプロイメント戦略が具体的に解説され、地域の利用制限がある場合の対策として、代替的な地域へのデプロイメントやオフピーク時間への再試行が明確に記されています。この修正により、事業が迅速に拡大する際や、地域のリソースが不足する状況に直面したときの対応策を事前に理解できるようになっており、リソースプランニングの柔軟性が増します。

全体として、これらの改訂は、Azure AI Searchを利用する企業や開発者にとって、戦略的な価値を提供するものであり、サービスの利用における透明性と効率性を高める重要な更新といえるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索サービスの制限と割当の更新 | modified | 13 | 11 | 24 | 
| [search-region-capacity.md](#item-4a3fe4) | minor update | 高需要地域でのAzure AI Searchデプロイメントの計画 | modified | 8 | 8 | 16 | 


# Modified Contents
## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: mattwojo
 ms.author: mattwoj
 ms.service: azure-ai-search
 ms.topic: limits-and-quotas
-ms.date: 09/04/2026
+ms.date: 09/16/2026
 ms.update-cycle: 180-days
 ai-usage: ai-assisted
 ms.custom:
@@ -38,7 +38,7 @@ If a create, scale, or upgrade operation is still running, wait for the provisio
 | Failure | Likely cause | First action |
 | --- | --- | --- |
 | Service creation blocked in a subscription and region | Subscription quota | In the **Quotas** service, check the limit for your tier and region, then [request more services](search-create-service-portal.md#add-more-services-to-your-subscription). |
-| Create, scale, or upgrade fails even though quota is available | Regional capacity constraint | Check the footnotes in [region support](search-region-support.md) for constrained tiers, then [choose another region](search-region-capacity.md#capacity-constraint-options). |
+| Create, scale, or upgrade fails even though quota is available | Consider alternative regions and off-peak deployment | Check the footnotes in [region support](search-region-support.md) for high-demand tiers, then [consider an alternative](search-region-capacity.md#consider-alternative-regions-and-off-peak-deployment). |
 | Replica, partition, tier, or object request rejected | Service or index limit | Compare your configuration and object counts with [service limits](#service-limits) and [index limits](#index-limits). |
 | The search service returns throttling responses under load | Throttling | Reduce the request rate or add search units. See [Throttling limits](#throttling-limits). |
 | Indexing fails near a storage or vector limit | Storage or vector quota | Compare `storageSize` with [partition storage](#partition-storage-gb) for disk and `vectorIndexSize` with [vector index size limits](#vector-index-size-limits) for memory. |
@@ -112,27 +112,29 @@ This table shows the progression of storage quota increases in GB over time. Sta
 
 ## Index limits
 
-| Resource | Free | Basic <sup>1</sup> | S1 | S2 | S3 | S3 HD | L1 | L2 | Serverless Developer |
+| Resource | Free | Basic | S1 | S2 | S3 | S3 HD | L1 | L2 | Serverless Developer |
 |----------|------|--------------------|----|----|----|--------|----|----|------------|
-| Maximum indexes | 3 | 5 or 15 | 50 | 200 | 200 | 1000 per partition or 3000 per service | 10 | 10 | 30 |
-| Maximum simple fields per index <sup>2</sup> | 1000 | 100 | 1000 | 1000 | 1000 | 1000 | 1000 | 1000 | 1000 |
+| Maximum indexes | 3 | 5 or 15 <sup>1</sup> | 50 | 200 | 200 | 1000 per partition or 3000 per service | 10 | 10 | 30 |
+| Maximum simple fields per index <sup>2</sup> | 1000 | 100 or 1000 <sup>3</sup> | 1000 | 1000 | 1000 | 1000 | 1000 | 1000 | 1000 |
 | Maximum dimensions per vector field | 4096 | 4096 | 4096 | 4096 | 4096 | 4096 | 4096 | 4096 | 4096 |
 | Maximum complex collections per index | 40 | 40 | 40 | 40 | 40 | 40 | 40 | 40 | 40 |
-| Maximum elements across all complex collections per document <sup>3</sup> | 3000 | 3000 | 3000 | 3000 | 3000 | 3000 | 3000 | 3000 | 3000 |
+| Maximum elements across all complex collections per document <sup>4</sup> | 3000 | 3000 | 3000 | 3000 | 3000 | 3000 | 3000 | 3000 | 3000 |
 | Maximum depth of complex fields | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
 | Maximum suggesters per index | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
 | Maximum scoring profiles per index | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
 | Maximum semantic configurations per index | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
 | Maximum functions per profile | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
-| Maximum index size <sup>4</sup> | N/A | N/A | N/A | 1.88 TB | 2.34 TB | 100 GB | N/A | N/A | 1 GB |
+| Maximum index size <sup>5</sup> | N/A | N/A | N/A | 1.88 TB | 2.34 TB | 100 GB | N/A | N/A | 1 GB |
 
-<sup>1</sup> Basic services created before December 2017 have lower limits (5 instead of 15) on indexes. Basic tier is the only tier with a lower limit of 100 fields per index.
+<sup>1</sup> Basic services created before December 2017 have lower limits (5 instead of 15) on indexes.
+
+<sup>2</sup> The upper limit on fields includes both first-level fields and nested subfields in a complex collection. For example, if an index contains 15 fields and has two complex collections with five subfields each, the field count of your index is 25. Indexes with a very large fields collection can be slow, especially on older Basic services. [Limit fields and attributes](search-what-is-an-index.md#physical-structure-and-size) to just those you need, and run indexing and query tests to ensure performance is acceptable.
 
-<sup>2</sup> The upper limit on fields includes both first-level fields and nested subfields in a complex collection. For example, if an index contains 15 fields and has two complex collections with five subfields each, the field count of your index is 25. Indexes with a very large fields collection can be slow. [Limit fields and attributes](search-what-is-an-index.md#physical-structure-and-size) to just those you need, and run indexing and query test to ensure performance is acceptable.
+<sup>3</sup> Basic services created before April 3, 2024 support a maximum of 100 fields per index. Newer Basic services support 1,000 fields per index.
 
-<sup>3</sup> An upper limit exists for elements because having a large number of them significantly increases the storage required for your index. An element of a complex collection is defined as a member of that collection. For example, assume a [Hotel document with a Rooms complex collection](search-howto-complex-data-types.md#complex-collection-limits). Each room in the Rooms collection is considered an element. During indexing, the indexing engine can safely process a maximum of 3,000 elements across the document as a whole. [This limit](search-api-migration.md#upgrade-to-2019-05-06) was introduced in `api-version=2019-05-06` and applies to complex collections only, and not to string collections or to complex fields.
+<sup>4</sup> An upper limit exists for elements because having a large number of them significantly increases the storage required for your index. An element of a complex collection is defined as a member of that collection. For example, assume a [Hotel document with a Rooms complex collection](search-howto-complex-data-types.md#complex-collection-limits). Each room in the Rooms collection is considered an element. During indexing, the indexing engine can safely process a maximum of 3,000 elements across the document as a whole. [This limit](search-api-migration.md#upgrade-to-2019-05-06) was introduced in `api-version=2019-05-06` and applies to complex collections only, and not to string collections or to complex fields.
 
-<sup>4</sup> For most tiers, the maximum index size is the total available storage on your search service. For S2, S3, and S3 HD services with multiple partitions, and therefore more storage, the maximum size of a single index is provided in the table. Applies to search services created after April 3, 2024. Indexes for services set up with the Serverless model (Preview) have a set maximum size provided in the table.
+<sup>5</sup> For most tiers, the maximum index size is the total available storage on your search service. For S2, S3, and S3 HD services with multiple partitions, and therefore more storage, the maximum size of a single index is provided in the table. Applies to search services created after April 3, 2024. Indexes for services set up with the Serverless model (Preview) have a set maximum size provided in the table.
 
 You might find some variation in maximum limits if your service happens to be provisioned on a more powerful cluster. The limits here represent the common denominator. Indexes built to the above specifications are portable across equivalent service tiers in any region.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスの制限と割当の更新"
}
```

### Explanation
この修正は、Azure AI Searchサービスのドキュメントにおける検索制限と割当についての情報を更新したものです。変更内容には、日付の更新、テーブルの内容の明確化、条件の見直しが含まれています。具体的には、既存の説明を改善するために、特定のフレーズや表現を修正し、より適切な情報を提供しています。また、テーブル内の項目に対して新たな注釈が追加され、情報の透明性向上が図られています。この修正により、ユーザーは現行の制限や使用可能なリソースに関する最新の情報を得ることができるようになります。

## articles/search/search-region-capacity.md{#item-4a3fe4}

<details>
<summary>Diff</summary>
````diff
@@ -1,24 +1,24 @@
 ---
-title: How to handle regional capacity constraints in Azure AI Search
-description: Learn how to handle a regional capacity constraint that effects your Azure AI Search service.
+title: How to plan Azure AI Search deployments in high-demand regions
+description: Learn how to handle high demanded regions that effects your Azure AI Search service.
 author: mattwojo
 ms.author: mattwoj
 ms.reviewer: angiesi
-ms.date: 07/21/2026
+ms.date: 09/08/2026
 ms.service: azure-ai-search
 ms.topic: concept-article
 ai-usage: ai-assisted
 ---
 
-# How to handle regional capacity constraints in Azure AI Search
+# How to manage Azure AI Search deployments in high-demand regions
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-This article helps you decide what to do when your preferred Azure AI Search region is unavailable due to capacity constraints. It also provides evaluation criteria for selecting an alternative region.
+This article helps you decide what to do when your preferred Azure AI Search region is unavailable due to high demand. It also provides evaluation criteria for selecting an alternative region.
 
-## Capacity constraint options
+## Consider alternative regions and off-peak deployment
 
-When a preferred Azure region is unavailable due to capacity constraints, you have two options:
+When a preferred Azure region is unavailable due to high demand, you have two options:
 
 - Deploy to an alternative region. 
 - Retry deployment during off-peak hours.
@@ -27,7 +27,7 @@ When a preferred Azure region is unavailable due to capacity constraints, you ha
 Azure AI Search is available across many Azure regions with consistent APIs, SDKs, SLAs, and compliance certifications. For most workloads, the operational difference between regions within the same geography is negligible. See the following section, *Criteria for selecting an alternative region*, for a full evaluation framework.
 
 **Retrying the service during off-peak hours is also a viable consideration.**
-Capacity constraints are sometimes temporary. Retrying deployment during low-traffic periods, such as nights or weekends in UTC, might succeed when peak-hour attempts fail. This option isn't guaranteed and isn't a substitute for evaluating an alternative region. If retries don't succeed within a reasonable window, proceed with an alternative region.
+High demand is sometimes temporary. Retrying deployment during low-traffic periods, such as nights or weekends in UTC, might succeed when peak-hour attempts fail. This option isn't guaranteed and isn't a substitute for evaluating an alternative region. If retries don't succeed within a reasonable window, proceed with an alternative region.
 
 Retry during off-peak hours when:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "高需要地域でのAzure AI Searchデプロイメントの計画"
}
```

### Explanation
この修正は、Azure AI Searchに関するドキュメントの一部を更新し、高需要地域でのデプロイメントに関する計画の方法を説明しています。記事のタイトルと説明が変更され、従来の「地域の容量制約」に関する表現から「高需要地域」に焦点を当てる内容にシフトしています。また、地域が利用できない場合のアプローチに関する文言も調整されており、代替地域へのデプロイメントやオフピーク時間での再試行の選択肢について明確に示されています。この変更により、読者は高需要の状況における戦略を理解しやすくなり、適切な判断を行うための情報が提供されます。


