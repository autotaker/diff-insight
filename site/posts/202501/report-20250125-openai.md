---
date: '2025-01-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fee2fd2...MicrosoftDocs:c67b444
summary: このドキュメントは、Azure OpenAIサービスに関する更新内容をまとめたものです。新たにSKU名が追加され、モデル対応地域の情報が更新されましたが、特に破壊的な変更はありません。文書の更新により、最新の情報が反映され、ユーザーが明確な情報をもとにデプロイメントオプションを選択できるようになっています。この更新は、サービスの透明性を高め、ユーザーエクスペリエンスの向上に寄与しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fee2fd2...MicrosoftDocs:c67b444){target="_blank"}

# Highlights

## New features
- 明示的に SKU 名（`GlobalStandard`、`GlobalProvisionedManaged`、`GlobalBatch`、`DataZoneStandard`、`DataZoneProvisionedManaged`、`DataZoneBatch`、`Standard`、`ProvisionedManaged`）が追加されました。
- モデルマトリックスに新たなモデルの SKU 情報が加えられ、モデル対応地域の情報が更新されました。

## Breaking changes
- 特に破壊的変更はありませんが、ドキュメントの情報更新により、より正確な情報に基づいた選択が必要です。

## Other updates
- ドキュメントの日付更新により、最新の情報が反映されています。

# Insights

このドキュメントの更新は、Azure OpenAI サービスのデプロイメントオプションとモデルマトリックスに関する情報をより詳細に、そして最新のものにするためのものです。企業や開発者が特定のニーズに応じた最適なデプロイメント選択を行うために、SKU 名の明示と特徴の詳細が追加されました。これにより、異なるデプロイメントタイプの利点と運用方式がより効果的に伝わり、選択の精度が向上します。

さらに、モデルマトリックスの更新により、利用可能なモデルの地域情報が最新の状態に保たれています。このような更新は、グローバルなサービス展開を考慮し、ユーザーが地理的条件を踏まえた利用計画を立てやすくするための重要な変更です。これにより、ユーザーは提供される全モデルの可用性を把握し、最適な技術的ソリューションを導入することができます。

全体として、このアップデートは Azure OpenAI サービスの透明性を高め、ユーザーエクスペリエンスの向上に寄与するものです。詳細な情報提供により、ユーザーがより多角的にサービスを理解し、合理的な判断を下せるよう支援することを目的としています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [deployment-types.md](#item-210814) | minor update | デプロイメントタイプに関する情報の更新 | modified | 18 | 1 | 19 | 
| [standard-global.md](#item-17a84b) | minor update | モデルマトリックスの更新 | modified | 26 | 26 | 52 | 


# Modified Contents
## articles/ai-services/openai/how-to/deployment-types.md{#item-210814}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: mrbullwinkle
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 07/11/2024
+ms.date: 01/24/2025
 ms.author: mbullwin
 ---
 
@@ -39,6 +39,8 @@ For any [deployment type](/azure/ai-services/openai/how-to/deployment-types) lab
 > [!IMPORTANT]
 > Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
 
+**SKU name in code:** `GlobalStandard`
+
 Global deployments are available in the same Azure OpenAI resources as non-global deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center with best availability for each request.  Global standard provides the highest default quota and eliminates the need to load balance across multiple resources.  
 
 Customers with high consistent volume may experience greater latency variability. The threshold is set per model. See the [quotas page to learn more](./quota.md).  For applications that require the lower latency variance at large workload usage, we recommend purchasing provisioned throughput.
@@ -48,6 +50,8 @@ Customers with high consistent volume may experience greater latency variability
 > [!IMPORTANT]
 > Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
 
+**SKU name in code:** `GlobalProvisionedManaged`
+
 Global deployments are available in the same Azure OpenAI resources as non-global deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center with best availability for each request. Global provisioned deployments provide reserved model processing capacity for high and predictable throughput using Azure global infrastructure.  
 
 ## Global batch
@@ -57,6 +61,8 @@ Global deployments are available in the same Azure OpenAI resources as non-globa
 
 [Global batch](./batch.md) is designed to handle large-scale and high-volume processing tasks efficiently. Process asynchronous groups of requests with separate quota, with 24-hour target turnaround, at [50% less cost than global standard](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). With batch processing, rather than send one request at a time you send a large number of requests in a single file. Global batch requests have a separate enqueued token quota avoiding any disruption of your online workloads.  
 
+**SKU name in code:** `GlobalBatch`
+
 Key use cases include:
 
 * **Large-Scale Data Processing:** Quickly analyze extensive datasets in parallel.
@@ -74,9 +80,12 @@ Key use cases include:
 * **Marketing and Personalization:** Generate personalized content and recommendations at scale.
 
 ## Data zone standard
+
 > [!IMPORTANT]
 > Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location within the Microsoft specified data zone. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
 
+**SKU name in code:** `DataZoneStandard`
+
 Data zone standard deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. Data zone standard provides higher default quotas than our Azure geography-based deployment types. 
 
 Customers with high consistent volume may experience greater latency variability. The threshold is set per model. See the [Quotas and limits](/azure/ai-services/openai/quotas-limits#usage-tiers) page to learn more. For workloads that require low latency variance at large volume, we recommend leveraging the provisioned deployment offerings. 
@@ -86,23 +95,31 @@ Customers with high consistent volume may experience greater latency variability
 > [!IMPORTANT]
 > Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location within the Microsoft specified data zone.[Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
 
+**SKU name in code:** `DataZoneProvisionedManaged`
+
 Data zone provisioned deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft specified data zone with the best availability for each request. Data zone provisioned deployments provide reserved model processing capacity for high and predictable throughput using Azure infrastructure within the Microsoft specified data zone.  
 
 ## Data zone batch
 
 > [!IMPORTANT]
 > Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location within the Microsoft specified data zone. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
+ 
+**SKU name in code:** `DataZoneBatch`
 
 Data zone batch deployments provide all the same functionality as [global batch deployments](./batch.md) while allowing you to leverage Azure global infrastructure to dynamically route traffic to only data centers within the Microsoft defined data zone with the best availability for each request. 
 
 ## Standard
 
+**SKU name in code:** `Standard`
+
 Standard deployments provide a pay-per-call billing model on the chosen model. Provides the fastest way to get started as you only pay for what you consume. Models available in each region as well as throughput may be limited.  
 
 Standard deployments are optimized for low to medium volume workloads with high burstiness. Customers with high consistent volume may experience greater latency variability.
 
 ## Provisioned
 
+**SKU name in code:** `ProvisionedManaged`
+
 Provisioned deployments allow you to specify the amount of throughput you require in a deployment. The service then allocates the necessary model processing capacity and ensures it's ready for you. Throughput is defined in terms of provisioned throughput units (PTU) which is a normalized way of representing the throughput for your deployment. Each model-version pair requires different amounts of PTU to deploy and provide different amounts of throughput per PTU. Learn more from our [Provisioned throughput concepts article](../concepts/provisioned-throughput.md).
 
 ### How to disable access to global deployments in your subscription
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントタイプに関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAI のデプロイメントタイプに関するドキュメントの更新を反映しています。具体的には、いくつかの SKU 名をコード内で明示的に記載し、その特徴を詳述しています。新たに追加された情報には、`GlobalStandard`、`GlobalProvisionedManaged`、`GlobalBatch`、`DataZoneStandard`、`DataZoneProvisionedManaged`、`DataZoneBatch`、`Standard`、および `ProvisionedManaged` の各 SKU 名が含まれ、それぞれがどのように機能し、どのような利点があるのかが説明されています。

これにより、ユーザーは各デプロイメントオプションについての理解を深め、特定のニーズに最適な選択をするための情報を得ることができます。また、日付の更新も行われ、最新の情報を反映したドキュメントとなっています。このような修正により、Azure OpenAI サービスにおけるデプロイメントの選択肢がより明確になり、利用者にとって有益なリソースとなることでしょう。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -6,31 +6,31 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 10/25/2024
+ms.date: 01/23/2025
 ---
 
-| **Region**     | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-10-01**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4**, **turbo-2024-04-09**   |
-|:-------------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:-------------------------------------------:|:-------------------------------:|
-| australiaeast      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| brazilsouth        | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| canadaeast         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| eastus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            |
-| eastus2            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                            |
-| francecentral      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| germanywestcentral | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| japaneast          | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| koreacentral       | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| northcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            |
-| norwayeast         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| polandcentral      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| southafricanorth   | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| southcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            |
-| southindia         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| spaincentral       | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| swedencentral      | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                            |
-| switzerlandnorth   | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| uaenorth           | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| uksouth            | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| westeurope         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
-| westus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            |
-| westus3            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            |
+| **Region**     | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-10-01**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4o-audio-preview**, **2024-12-17**   |
+|:-------------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:-------------------------------------------:|:-------------------------------:|:----------------------------------------:|
+| australiaeast      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| brazilsouth        | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| canadaeast         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| eastus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| eastus2            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                            | ✅                                     |
+| francecentral      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| germanywestcentral | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| japaneast          | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| koreacentral       | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| northcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| norwayeast         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| polandcentral      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| southafricanorth   | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| southcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| southindia         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| spaincentral       | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| swedencentral      | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                            | ✅                                     |
+| switzerlandnorth   | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| uaenorth           | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| uksouth            | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| westeurope         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| westus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            | -                                    |
+| westus3            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            | -                                    |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルマトリックスの更新"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関連する「標準グローバル」モデルマトリックスドキュメントの内容を更新したものです。主な変更点は、使用される日付やモデルのカテゴリ、及び新たに追加されたモデルのSKUに関する情報です。また、全体的な構造は維持されながら、各モデルの対応地域リストを更新して、特定のモデルがサポートする地域をより明確に示しています。

特に、各地域におけるモデルの可用性を示す表に新しい情報が追加され、既存のデータが更新されています。この改訂により、ユーザーはどの地域でどのモデルが利用可能かを明確に理解することができ、利用の計画を立てやすくなります。この種の更新は、サービスの透明性を向上させ、ユーザーが最適な技術的選択を行うための重要な情報源となります。


