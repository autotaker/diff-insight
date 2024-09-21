---
date: '2024-09-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e496207...MicrosoftDocs:655e817
summary: |-
  # 概要

  今回のコード変更では、主にAzure AI Search関連のドキュメントファイルが更新されました。特に地域選択に関するガイダンスやサポート地域、SKUティアに関する情報が追加され、メタデータの更新も行われました。重大な機能の変更はありませんが、一部のファイルに重要な注意点が含まれています。全体として、ユーザーがサービスをより効率的に利用できるよう情報が明確化され、ドキュメンテーションの精度向上が図られています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e496207...MicrosoftDocs:655e817){target="_blank"}

# Highlights
今回のコード変更では、主にドキュメントファイルの更新が行われています。具体的には画像ファイルのメタデータや、Azure AI Search関連ドキュメントの内容更新が中心です。以下に新機能、重大な変更、その他の更新についてまとめます。

## New features
- 地域選択に関する詳細情報追加 (`search-create-service-portal.md`)
- サポート地域とその機能の可用性に関する情報追加 (`search-region-support.md`)
- SKUティアと地域制限に関する説明の明確化 (`search-sku-tier.md`)

## Breaking changes
特に重大な機能の変更や削除はありませんが、以下のファイルには注意が必要です。
- `search-create-service-portal.md`: 地域選択に関する注意点の更新
- `search-region-support.md`: 特定の地域のサービス利用不可に関する情報

## Other updates
- 画像ファイル（`deployment-details.png`、`resource-group-deployments.png`）のメタデータ更新
- ベクトルインデックスサイズに関する情報の日付更新 (`vector-search-index-size.md`)
- 検索サービスの制限とクォータに関する内容の更新 (`search-limits-quotas-capacity.md`)

# Insights
今回のコード更新では、Azure AI Searchドキュメントにおける最新情報の反映と、情報の明確化が主な目的と考えられます。特に以下の点に注目すると、その背景と意図について理解が深まるでしょう。

### 画像ファイルのメタデータ更新
`deployment-details.png` と `resource-group-deployments.png` のメタデータが更新されましたが、ファイルの実際の内容は変更されていません。この更新は、バージョン管理やファイルの整合性を保つためのものであり、ドキュメント管理の一環と考えられます。

### 地域選択に関する情報更新 (`search-create-service-portal.md`)
この更新は、Azure AI Searchサービスの利用可能地域が高需要により制限される場合があるという点に対する注意喚起を強化するためのものです。地域選択に関するガイダンスが明確化され、ユーザーがサービス利用プランを立てる際に役立つ内容が追加されました。

### ベクトル検索インデックスサイズに関する情報更新
`search-limits-quotas-capacity.md` 及び `vector-search-index-size.md` では、ベクトルインデックスサイズに関する詳細が整理・明確化されています。これにより、ユーザーはより正確な情報に基づいてリソースのプランニングを行いやすくなります。特にパーティションサイズが制限に与える影響についての情報が強調されており、重要な注意事項が明示されています。

### サポート地域とSKUティアに関する情報更新
`search-region-support.md` と `search-sku-tier.md` では、Azure AI Searchのサポート地域やSKUティアについての情報がアップデートされています。特定の地域でサービスが利用できない理由や、古いインフラストラクチャの制限に関する説明が明確化されています。これにより、ユーザーは自分のニーズに適した地域やティアを選びやすくなります。

まとめると、今回の変更はドキュメンテーションの精度向上と、ユーザーがAzure AI Searchサービスを最大限に活用するための情報提供を目的としています。今後もこのようなアップデートが続くことで、ユーザーの利便性と満足度がさらに向上することが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [deployment-details.png](#item-e7b137) | minor update | 画像ファイルのメタデータの更新 | modified | 0 | 0 | 0 | 
| [resource-group-deployments.png](#item-9fde8e) | minor update | 画像ファイルのメタデータの更新 | modified | 0 | 0 | 0 | 
| [search-create-service-portal.md](#item-f90159) | minor update | サービスポータルにおける地域選択に関する更新 | modified | 5 | 5 | 10 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索サービスの制限とクォータに関する内容の更新 | modified | 8 | 32 | 40 | 
| [search-region-support.md](#item-25b0f1) | minor update | Azure AI Searchのサポート地域に関する内容の更新 | modified | 30 | 40 | 70 | 
| [search-sku-tier.md](#item-7686b8) | minor update | Azure AI SearchのSKUティアに関する内容の更新 | modified | 5 | 3 | 8 | 
| [vector-search-index-size.md](#item-bb2846) | minor update | ベクトル検索インデックスサイズに関する日付の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/media/vector-search-index-size/deployment-details.png{#item-e7b137}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルのメタデータの更新"
}
```

### Explanation
このコードの変更は、指定された画像ファイル（`deployment-details.png`）のメタデータに関するものであり、ファイルの内容自体には変更はありません。具体的には、ファイルに対しての追加や削除はなく、変更点もないため、ファイルのバージョンやメタ情報に関連するマイナーな更新が行われたと考えられます。これは、ビジュアルリソースに関するドキュメントや情報の整理に役立つための操作と理解できます。詳細は、変更されたファイルの [こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/655e817c107d34c5d8a21c38e9ee16f71f3547de/articles%2Fsearch%2Fmedia%2Fvector-search-index-size%2Fdeployment-details.png) から確認できます。

## articles/search/media/vector-search-index-size/resource-group-deployments.png{#item-9fde8e}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルのメタデータの更新"
}
```

### Explanation
このコードの変更は、指定された画像ファイル（`resource-group-deployments.png`）のメタデータが更新されたことを示しています。ファイルを構成するコンテンツ自体には追加や削除、変更はなく、具体的な内容が変わったわけではありません。このため、これはファイルのバージョン管理やドキュメントの整合性を促進するためのマイナーな更新と見なされます。詳しい内容は、変更されたファイルの [こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/655e817c107d34c5d8a21c38e9ee16f71f3547de/articles%2Fsearch%2Fmedia%2Fvector-search-index-size%2Fresource-group-deployments.png) から確認できます。

## articles/search/search-create-service-portal.md{#item-f90159}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - references_regions
   - build-2024
 ms.topic: conceptual
-ms.date: 08/22/2024
+ms.date: 09/19/2024
 ---
 
 # Create an Azure AI Search service in the portal
@@ -87,25 +87,25 @@ Service name requirements:
 ## Choose a region
 
 > [!IMPORTANT]
-> Due to high demand, Azure AI Search is currently unavailable for new instances in West Europe. If you don't immediately need semantic ranker or skillsets, choose Sweden Central because it has the most data center capacity. Otherwise, North Europe is another option. Currently, there are also capacity constraints for Basic and Standard (S1) tiers within a given region.
+> Due to high demand, Azure AI Search is currently unavailable for new instances in some regions. 
 
 If you use multiple Azure services, putting all of them in the same region minimizes or voids bandwidth charges. There are no charges for data egress among same-region services.
 
 Generally, choose a region near you, unless the following considerations apply:
 
-+ Your nearest region is capacity constrained. West Europe is at capacity and unavailable for new instances. Other regions are [at capacity for specific tiers](search-sku-tier.md#region-availability-by-tier). One advantage to using the Azure portal for resource setup is that it provides only those regions and tiers that are available. You can't select regions or tiers that are unavailable.
++ Your nearest region is capacity constrained. For example, West Europe is at capacity and unavailable for new instances. Other regions are [at capacity for specific tiers](search-sku-tier.md#region-availability-by-tier). One advantage to using the Azure portal for resource setup is that it provides only those regions and tiers that are available.
 
 + You want to use integrated data chunking and vectorization or built-in skills for AI enrichment. Azure OpenAI and Azure AI services multiservice accounts must be in the same region as Azure AI Search for integration purposes. [Choose a region](search-region-support.md) that provides all necessary resources.
 
 + You want to use Azure Storage for indexer-based indexing or you need to store application data that isn't in an index. Debug session state, enrichment caches, and knowledge stores are Azure AI Search features that have a dependency on Azure Storage. The region you choose for Azure Storage has implications for network security. Specifically, if you're setting up a firewall, you should place the resources in separate regions. For more information, see [Outbound connections from Azure AI Search to Azure Storage](search-indexer-securing-resources.md).
 
 Here's a checklist for choosing a region:
 
-1. Is Azure AI Search available in a nearby region? Check the [supported regions list](search-region-support.md). Capacity-constrained regions are indicated in the footnotes.
+1. Is Azure AI Search available in a nearby region? Check the [supported regions list](search-region-support.md).
 
 1. Do you know which tier you want to use? Tiers are covered in the next step. Check [region availability by tier](search-sku-tier.md#region-availability-by-tier) to determine if you can create a search service at the desired tier in your region of choice.
 
-1. Do you need [AI enrichment](cognitive-search-concept-intro.md) or [integrated data chunking and vectorization](vector-search-integrated-vectorization.md)? Verify that Azure OpenAI and Azure AI services are [offered in the same region](search-region-support.md) as Azure AI Search. 
+1. Do you need [AI enrichment](cognitive-search-concept-intro.md) or [integrated data chunking and vectorization](vector-search-integrated-vectorization.md)? Verify that Azure OpenAI and Azure AI multiservice are [offered in the same region](search-region-support.md) as Azure AI Search. 
 
    Be aware that Azure AI Vision multimodal embeddings API, used for [integrated image vectorization](search-get-started-portal-image-search.md), must be accessed through an Azure AI multiservice account, but is available in a [smaller subset of regions](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービスポータルにおける地域選択に関する更新"
}
```

### Explanation
このコードの変更は、`search-create-service-portal.md`ファイルにおける内容の更新を反映しています。具体的には、Azure AI Searchサービスに関する地域選択の注意点が修正されており、主に高需要に起因するサービスの利用可能地域に関する説明が更新されています。変更点は、古い情報の更新、新しい情報の追加、または不明確な表現の明確化を含みます。例えば、特定の地域（例えば西ヨーロッパ）での新規インスタンスの利用不可に関する記述が既存の内容からより一般的な表現へと変更されています。また、Azure Storageとの統合の必要性や、地域選択によるネットワークセキュリティへの影響についての明確なガイダンスも追加されました。これにより、ユーザーが適切な地域を選択するための助けとなる内容が提供されています。詳細は、変更されたファイルの [こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/655e817c107d34c5d8a21c38e9ee16f71f3547de/articles%2Fsearch%2Fsearch-create-service-portal.md) から確認できます。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: conceptual
-ms.date: 09/04/2024
+ms.date: 09/19/2024
 ms.custom:
   - references_regions
   - build-2024
@@ -80,53 +80,29 @@ When estimating document size, remember to consider only those fields that add v
 
 When you index documents with vector fields, Azure AI Search constructs internal vector indexes using the algorithm parameters you provide. The size of these vector indexes is restricted by the memory reserved for vector search for your service's tier (or `SKU`).
 
-The service enforces a vector index size quota **for every partition** in your search service. Each extra partition increases the available vector index size quota. This quota is a hard limit to ensure your service remains healthy, which means that further indexing attempts once the limit is exceeded results in failure. You can resume indexing once you free up available quota by either deleting some vector documents or by scaling up in partitions.
-
-Vector limits vary by service creation date and tier.
-
-+ To check the age of your search service or learn more about vector indexes, see [Vector index size and staying under limits](vector-search-index-size.md).
-
-+ To view the vector quota in effect for your search service, use [GET Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics), or check the **Properties** and **Usage** tabs for your search service in the Azure portal.
-
-#### Vector quota per partition (GB)
+Vector limits vary by [service creation date](vector-search-index-size.md#how-to-check-service-creation-date) and [tier](search-sku-tier.md). For guidance on managing and maximizing vector storage, see [Vector index size and staying under limits](vector-search-index-size.md).
 
 This table shows the progression of vector quota increases in GB over time. The quota is per partition, so if you scale a new Standard (S1) service to 6 partitions, total vector quota is 35 multiplied by 6.
 
 | Service creation date |Basic | S1| S2 | S3/HD | L1 | L2 |
 |-----------------------|------|---|----|----|----|----|
 |**Before July 1, 2023** <sup>1</sup> | 0.5 | 1 | 6 | 12 | 12 | 36 |
 | **July 1, 2023 through April 3, 2024** <sup>2</sup>| 1  | 3 | 12 | 36 | 12 | 36 |
-|**April 3, 2024 through May 17, 2024** <sup>3</sup> | 5  | 35 | 100 | 200 | 12 | 36 |
-|**After May 17, 2024** <sup>4</sup> | 5  | 35 | 150 | 300 | 150 | 300 |
+|**April 3, 2024 through May 17, 2024** <sup>3</sup> | **5**  | **35** | **150** | **300** | 12 | 36 |
+|**After May 17, 2024** <sup>4</sup> | 5  | 35 | 150 | 300 | **150** | **300** |
 
 <sup>1</sup> Initial vector limits during early preview.
 
 <sup>2</sup> Vector limits during the later preview period. Three regions didn't have the higher limits: Germany West Central, West India, Qatar Central.
 
-<sup>3</sup> Higher vector quota based on the larger partitions for supported tiers and regions.
+<sup>3</sup> Higher vector quota based on the larger partitions for supported tiers and regions. 
 
 <sup>4</sup> Higher vector quota for more tiers and regions based on partition size updates.
 
-#### Partition limits (GB)
-
-This table repeats [partition storage limits](#service-limits) for context. The table shows the progression of storage quota increases in GB over time. Vector quota is per partition, so the more significant increases in vector quota that occurred starting in April 2024 correspond to the increases in per-partition storage occuring at the same time. 
-
-Higher capacity partitions were brought online starting in April 2024.
-
-| Service creation date |Basic | S1| S2 | S3/HD | L1 | L2 |
-|-----------------------|------|---|----|----|----|----|
-|**Before July 1, 2023** <sup>1</sup> | 2  | 25 | 100 | 200 | 1,024 | 2,048 |
-|**July 1, 2023 through April 3, 2024** <sup>2</sup>| 2  | 25 | 100 | 200 | 1,024 | 2,048 |
-|**April 3, 2024 through May 17, 2024** <sup>3</sup> | 15  | 160 | 512 | 1,024 | 1,024 | 2,048 |
-|**After May 17, 2024** <sup>4</sup> | 15  | 160 | 512 | 1,024 | 2,048 | 4,096 |
-
-<sup>1</sup> Partition sizes during early preview.
-
-<sup>2</sup> No change during the later preview period.
-
-<sup>3</sup> Higher capacity storage for Basic, S1, S2, S3 in these regions. **Americas**: Brazil South​, Canada Central​, Canada East​​, East US​, East US 2, ​Central US​, North Central US​, South Central US​, West US​, West US 2​, West US 3​, West Central US. **Europe**: France Central​. Italy North​​, North Europe​​, Norway East, Poland Central​​, Switzerland North​, Sweden Central​, UK South​, UK West​. **Middle East**:  UAE North. **Africa**: South Africa North. **Asia Pacific**: Australia East​, Australia Southeast​​, Central India, Jio India West​, East Asia, Southeast Asia​, Japan East, Japan West​, Korea Central, Korea South​.
+The service enforces a vector index size quota **for every partition** in your search service. Each extra partition increases the available vector index size quota. This quota is a hard limit to ensure your service remains healthy, which means that further indexing attempts once the limit is exceeded results in failure. You can resume indexing once you free up available quota by either deleting some vector documents or by scaling up in partitions.
 
-<sup>4</sup> Higher capacity storage for more tiers and more regions. **Europe**: Germany North​, Germany West Central, Switzerland West​. **Azure Government**: Texas, Arizona, Virginia. **Africa**: South Africa North​. **Asia Pacific**: China North 3, China East 3.
+> [!IMPORTANT]
+> Higher vector limits are tied to larger partition sizes. Regions that run on older infrastructure are subject to the July-April limits. Review the [regions list](search-region-support.md) for status on partition storage limits.
 
 ## Indexer limits
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスの制限とクォータに関する内容の更新"
}
```

### Explanation
このコードの変更は、`search-limits-quotas-capacity.md`ファイルにおける情報の更新を反映しています。主な変更点は、Azure AI Searchサービスのベクトルインデックスのサイズ制限に関する詳細の整理と明確化です。古い情報が削除され、新しいルールやガイドラインが追加されることで、特定の地域やサービスのティアに基づくベクトルの制限についてより正確な理解が得られるようになっています。

さらに、ベクトルインデックスのサイズ制限に関しての重要な注意事項が強調されており、パーティションのサイズがどのようにベクトル制限に影響を与えるかについても更新されています。また、古い情報の整理に伴って不要な項目が削除され、コンテンツがより一貫性を持ってきれいに整理されている点も確認できます。この変更により、ユーザーが適切なリソースプランニングや容量管理を行うための支援が強化されています。詳細は、変更されたファイルの [こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/655e817c107d34c5d8a21c38e9ee16f71f3547de/articles%2Fsearch%2Fsearch-limits-quotas-capacity.md) から確認できます。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Feature availability across clouds regions
+title: Supported regions
 titleSuffix: Azure AI Search
 description: Shows supported regions and feature availability across regions for Azure AI Search.
 
@@ -9,13 +9,13 @@ ms.author: heidist
 ms.service: cognitive-search
 ms.topic: conceptual
 ms.custom: references_regions
-ms.date: 09/03/2024
+ms.date: 09/19/2024
 
 ---
 
-# Azure AI Search feature availability across cloud regions
+# Azure AI Search regions list
 
-This article identifies the cloud regions in which Azure AI Search is available. It also lists which premium features are available in each region.
+This article identifies the cloud regions in which Azure AI Search is available. It also lists which premium features are available in each region. 
 
 ## Features subject to regional availability
 
@@ -57,24 +57,26 @@ You can create an Azure AI Search resource in any of the following Azure public
 | Canada East​​ ​ |  | ✅ | |
 | East US​ | ✅ | ✅ | ✅ |
 | East US 2 ​ | ✅ | ✅ | ✅ |
-| ​Central US​ <sup>1</sup>​ | ✅ | ✅ | ✅ |
+| ​Central US​​ <sup>1</sup> | ✅ | ✅ | ✅ |
 | North Central US​ ​ | ✅ | ✅ | |
-| South Central US​ <sup>1</sup>​ | ✅ | ✅ | ✅ |
+| South Central US​ <sup>2</sup>​ | ✅ | ✅ | ✅ |
 | West US​ ​ | ✅ | ✅ | |
-| West US 2​ <sup>1</sup>​ | ✅ | ✅ | ✅ |
-| West US 3​ <sup>1</sup>​ | ✅ | ✅ |✅ |
+| West US 2​ ​ | ✅ | ✅ | ✅ |
+| West US 3​ <sup>2</sup>​ | ✅ | ✅ |✅ |
 | West Central US​ ​ | ✅ | ✅ | |
 
-<sup>1</sup> Currently, this region is at capacity for Basic and Standard (S1) tiers. Choose a higher tier or a different region.
+<sup>1</sup> This region has capacity, but some tiers are [not available](search-sku-tier.md#region-availability-by-tier). 
+
+<sup>2</sup> Currently, this region is at full capacity and not accepting new search services. 
 
 ### Europe
 
 | Region | AI integration | Semantic ranking | Availability zones |
 |--|--|--|--|
-| North Europe​​ <sup>1</sup>| ✅ | ✅ | ✅ |
-| West Europe​​ <sup>2</sup>| ✅ | ✅ | ✅ |
+| North Europe​​ | ✅ | ✅ | ✅ |
+| West Europe​​ <sup>1, 2</sup>| ✅ | ✅ | ✅ |
 | France Central​​ | ✅ | ✅ | ✅ |
-| Germany West Central​ ​| ✅ |  | ✅ |
+| Germany West Central​ <sup>2</sup> ​| ✅ |  | ✅ |
 | Italy North​​ |  |  | ✅ |
 | Norway East​​ | ✅ |  | ✅ |
 | Poland Central​​ |  |  |  |
@@ -85,9 +87,9 @@ You can create an Azure AI Search resource in any of the following Azure public
 | UK South​ | ✅ | ✅ | ✅ |
 | UK West​ ​|  | ✅ | |
 
-<sup>1</sup> Currently, this region is at capacity for Basic and Standard (S1) tiers. Choose a higher tier or a different region.
+<sup>1</sup> Currently, this region is at full capacity and not accepting new search services.
 
-<sup>2</sup> West Europe is at capacity for all tiers and isn't accepting any new search services. Additionally, the clusters used to run Azure AI Search don't have the [higher capacity partitions](search-limits-quotas-capacity.md#service-limits) that were brought online in April 2024. This means that search services deployed in this region have lower storage and computing capability.
+<sup>2</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
 
 ### Middle East
 
@@ -97,15 +99,17 @@ You can create an Azure AI Search resource in any of the following Azure public
 | Qatar Central​ <sup>1, 2</sup> |  |  | ✅ |
 | UAE North​​ | ✅ |  | ✅ |
 
-<sup>1</sup> Currently, this region is at capacity for Basic and Standard (S1) tiers. Choose a higher tier or a different region.
+<sup>1</sup> Currently, this region is at full capacity and not accepting new search services.
 
-<sup>2</sup> These regions run on older infrastructure that has lower capacity per partition at every tier. Choose a different region if you want [higher capacity](search-limits-quotas-capacity.md#service-limits).
+<sup>2</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
 
 ### Africa
 
 | Region | AI integration | Semantic ranking | Availability zones |
 |--|--|--|--|
-| South Africa North​ | ✅ |  | ✅ |
+| South Africa North​ <sup>1</sup> | ✅ |  | ✅ |
+
+<sup>1</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
 
 ### Asia Pacific
 
@@ -123,51 +127,37 @@ You can create an Azure AI Search resource in any of the following Azure public
 | Korea Central | ✅ | ✅ | ✅ |
 | Korea South​ ​ |  | ✅ |  |
 
-<sup>1</sup> Currently, this region is at capacity for Basic and Standard (S1) tiers. Choose a higher tier or a different region.
+<sup>1</sup> This region has capacity, but some tiers are [not available](search-sku-tier.md#region-availability-by-tier). 
 
-<sup>2</sup> These regions run on older infrastructure that has lower capacity per partition at every tier. Choose a different region if you want [higher capacity](search-limits-quotas-capacity.md#service-limits).
+<sup>2</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
 
 ## Azure Government regions
 
-All of these regions support [higher capacity tiers](search-limits-quotas-capacity.md#service-limits). 
-
-None of these regions support Azure [role-based access for data plane operations](search-security-rbac.md). You must use key-based authentication for indexing and query workloads.
-
 | Region | AI integration | Semantic ranking | Availability zones |
 |--|--|--|--|
 | Arizona | ✅ | ✅  | |
 | Texas |  |  |  |
-| Virginia | ✅ | ✅  | ✅ |
+| Virginia <sup>1</sup> | ✅ | ✅  | ✅ |
 
-## Azure operated by 21Vianet
+<sup>1</sup> Currently, this region is at full capacity and not accepting new search services.
 
-You can install Azure AI Search in any of the following regions. If you need semantic ranking or AI enrichment, choose a region that provides the feature.
+## Azure operated by 21Vianet
 
 | Region | AI integration | Semantic ranking | Availability zones |
 |--|--|--|--|
-| China East <sup>1</sup> |  |  |  |
+| China East |  |  |  |
 | China East 2 <sup>1</sup> | ✅  | | |
 | China East 3 |  |  |  |
-| China North <sup>1</sup> |  |  | |
+| China North |  |  | |
 | China North 2 <sup>1</sup> |  |  | |
 | China North 3 | | ✅ | ✅ |
 
-<sup>1</sup> These regions run on older infrastructure that has lower capacity per partition at every tier. Choose a different region if you want [higher capacity](search-limits-quotas-capacity.md#service-limits).
-
-<!-- ## Early Update Access Program (EUAP)
-
-These regions
-
-| Region | AI enrichment | Semantic ranking | Availability zones |
-|--|--|--|--|
-| Central US EUAP​ <sup>1</sup> | | ✅ | |
-| East US 2 EUAP ​ | | ✅ | |
-
-<sup>1</sup> This region runs on older infrastructure that has lower capacity per partition at every tier. You can't create a search service with [higher capacity](search-limits-quotas-capacity.md#service-limits) in this region. -->
+<sup>1</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
 
 ## See also
 
 - [Azure AI Studio region availability](/azure/ai-studio/reference/region-support)
 - [Azure OpenAI model region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)
+- [Azure AI Vision region list](/azure/ai-services/computer-vision/overview-image-analysis#region-availability)
 - [Availability zone region availability](/azure/reliability/availability-zones-service-support#azure-regions-with-availability-zone-support)
 - [Azure product by region page](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=search)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのサポート地域に関する内容の更新"
}
```

### Explanation
この変更は、`search-region-support.md`ファイルにおいて、Azure AI Searchのサポート地域とその機能の可用性に関する情報を見直したものです。主な変更点は、地域名の表記を整理し、各地域での機能の可用性についての注記を更新した点にあります。

具体的には、特定の地域がフルキャパシティに達しているため新しい検索サービスを受け付けていないことや、古いインフラストラクチャが原因で各タイルのストレージ制限が低いことに関する情報が明確にされています。また、追加された新しい情報には、特定のタイルが利用できないかどうかの詳細が含まれており、ユーザーにとっての選択肢をよりクリアに示しています。

これにより、ユーザーは自分のニーズに合った地域を選択しやすくなり、Azure AI Searchの導入と運用において非常に有用な情報が提供されています。詳しい情報は、変更されたファイルの [こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/655e817c107d34c5d8a21c38e9ee16f71f3547de/articles%2Fsearch%2Fsearch-region-support.md) から確認できます。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: conceptual
-ms.date: 08/22/2024
+ms.date: 09/19/2024
 
 ---
 
@@ -53,7 +53,9 @@ You can find out more about the various tiers on the [pricing page](https://azur
 
 ## Region availability by tier
 
-Currently, several regions are at capacity for Basic and Standard (S1) tiers and can't be used for new search services. If you use the Azure portal to create a search service, the portal excludes any region-tier combinations that aren't available.
+The supported [regions list](search-region-support.md) provides the locations where Azure AI Search is offered.
+
+Currently, several regions are at capacity for specific tiers and can't be used for new search services. If you use the Azure portal to create a search service, the portal excludes any region-tier combinations that aren't available.
 
 | Region | Disabled tier (SKU) due to over-capacity |
 |--------|------------------------------------------|
@@ -93,7 +95,7 @@ Tiers determine the  maximum storage of the service itself, plus the maximum num
 Tier pricing includes details about per-partition storage that ranges from 15 GB for Basic, up to 2 TB for Storage Optimized (L2) tiers. Other hardware characteristics, such as speed of operations, latency, and transfer rates, aren't published, but tiers that are designed for specific solution architectures are built on hardware that has the features to support those scenarios. For more information about partitions, see [Estimate and manage capacity](search-capacity-planning.md) and [Reliability in Azure AI Search](search-reliability.md).
 
 > [!NOTE]
-> Higher capacity partitions became available in selected regions starting in April 2024. A second wave of higher capacity partitions released in May 2024. If you're using an older search service, consider creating a new search service to benefit from more capacity at the same billing rate. For more information, see [Service limits](search-limits-quotas-capacity.md#service-limits)
+> Higher capacity partitions became available in selected regions starting in April 2024. A second wave of higher capacity partitions released in May 2024. If you're using an older search service, consider creating a new search service to benefit from more capacity at the same billing rate. For more information, see [Service limits](search-limits-quotas-capacity.md#service-limits). To check the age of your search service, see [How to check service creation date](vector-search-index-size.md#how-to-check-service-creation-date).
 
 ## Billing rates
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI SearchのSKUティアに関する内容の更新"
}
```

### Explanation
この変更は、`search-sku-tier.md`ファイル内のAzure AI SearchのSKUティアに関する情報の更新を反映しています。主な更新点として、日付の変更に加え、利用可能な地域とそれに関連する制限についての説明が明確化されています。

具体的には、特定のティアが利用できない地域に関する情報が整理され、より詳細な地域リストが参照できるようになっています。また、既存の検索サービスの古いインフラストラクチャに対して新しい検索サービスの作成を推奨する文が追加され、より多くの容量を同じ料金で利用できる可能性が強調されています。

これにより、ユーザーは自分の要求に合ったティアを選択しやすくなり、検索サービスの計画や運用において有用な情報が提供されるようになっています。詳しい情報は、変更されたファイルの [こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/655e817c107d34c5d8a21c38e9ee16f71f3547de/articles%2Fsearch%2Fsearch-sku-tier.md) から確認できます。

## articles/search/vector-search-index-size.md{#item-bb2846}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: cognitive-search
 ms.custom:
   - build-2024
 ms.topic: conceptual
-ms.date: 08/05/2024
+ms.date: 09/19/2024
 ---
 
 # Vector index size and staying under limits
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索インデックスサイズに関する日付の更新"
}
```

### Explanation
この変更は、`vector-search-index-size.md`ファイルにおいて、ベクトル検索インデックスのサイズに関連する情報の更新を行ったものです。主な変更点は、最終更新日が2024年8月5日から2024年9月19日に変更されたことです。

この更新により、ユーザーは最新の情報に基づいてコンテンツを参照できるようになります。適切な情報を保持することは、Azure AI Searchの運用や計画を行う際に重要です。詳しい情報は、変更されたファイルの [こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/655e817c107d34c5d8a21c38e9ee16f71f3547de/articles%2Fsearch%2Fvector-search-index-size.md) から確認できます。


