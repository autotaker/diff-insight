---
date: '2025-01-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:36d0ff5...MicrosoftDocs:f3626a8
summary: この文書の変更は、Azure OpenAIサービスに関するさまざまな文書のマイナーアップデートに焦点を当てています。具体的には、モデルのリタイア情報の更新、新しいデータゾーンバッチモデルの追加、バッチデプロイおよびグローバルバッチモデルの可用性情報の改善が含まれます。また、一部の更新では地域ごとのモデルの可用性についての詳細が提供され、新しいモデルバージョンの追加や視覚的要素の最新化も行われました。これらの変更により、ユーザーは利用可能なリソースをより効果的に把握できるようになり、Azure
  OpenAIの利用が直感的かつ効率的になります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:36d0ff5...MicrosoftDocs:f3626a8){target="_blank"}

# ハイライト

この文書の変更は、Azure OpenAI サービスに関するさまざまな文書のマイナーアップデートを中心にしています。具体的に、モデルのリタイア情報の更新、新しいデータゾーンバッチモデルの追加、バッチデプロイおよびグローバルバッチモデルの可用性情報の改善などがあります。また、一部の更新では、地域ごとのモデルの可用性についての詳細が提供され、新しいモデルバージョンの追加、テーブルや画像など視覚的な要素の最新化が行われました。

## 新機能

- グローバルバッチモデルに関する新しい文書の追加。
- データゾーンバッチモデルの詳細追加。

## 破壊的変更

特に記載なし。

## 他の更新

- リタイアメント情報やモデルの可用性に関する日付と情報の更新。
- バッチデプロイメントやデプロイメントタイプでのセクションタイトル変更や内容整理。
- グローバルバッチモデルの可用性やプロビジョニングされたモデル情報の整理と改善。
- 画像ファイル`deploy-models-new.png`の更新。

# 洞察

Azure OpenAIにおけるこの一連のマイナーアップデートは、サービスの提供する情報の正確性と最新性を保つために重要です。それぞれの文書において、特定地域でのモデルの可用性情報が更新されているため、ユーザーは利用可能なリソースをより効果的に把握することが可能になります。これは、企業や開発者が地域別に最適なモデルを選択し、エクスペリエンスを向上させる助けになります。

新しいデータゾーンバッチモデルやグローバルバッチモデルの情報追加では、Azureがデータ処理の地域性やセキュリティ考慮を強化していることがうかがえます。データゾーン批処理は、特定の地域におけるデプロイメントの柔軟性を提供し、プライバシーとデータの居住性を確保するための手段を示しています。また、新しい文書の追加は、ユーザーがサービスの変化や拡張についてタイムリーにフォローできるよう設計されています。

これらの変更により、Azure OpenAIの利用はより直感的かつ効率的になり、ユーザーエクスペリエンスの向上と、企業の運用効率を高めるための基盤が強化されていると考えられます。特に今後の動的なデータニーズに対応するために、柔軟かつグローバルなアクセスモデルがますます重要となるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルの更新日付と情報の追加 | modified | 2 | 1 | 3 | 
| [models.md](#item-db2c37) | minor update | データゾーンバッチモデルに関する情報の追加 | modified | 7 | 1 | 8 | 
| [batch.md](#item-a131d5) | minor update | バッチデプロイメントに関する情報の更新と拡張 | modified | 17 | 8 | 25 | 
| [deployment-types.md](#item-210814) | minor update | デプロイメントタイプに関する情報の整理と更新 | modified | 7 | 15 | 22 | 
| [global-batch-limits.md](#item-73207b) | minor update | バッチ制限とクォータに関する情報の更新 | modified | 13 | 4 | 17 | 
| [datazone-provisioned-managed.md](#item-ae7f5b) | minor update | データゾーンプロビジョニング済みモデルの地域可用性の更新 | modified | 5 | 1 | 6 | 
| [global-batch-datazone.md](#item-94a58c) | new feature | グローバルバッチモデルの可用性に関する新しい文書の追加 | added | 18 | 0 | 18 | 
| [global-batch.md](#item-929e6a) | minor update | グローバルバッチモデルの可用性の更新 | modified | 24 | 24 | 48 | 
| [provisioned-global.md](#item-340884) | minor update | プロビジョニングされたグローバルモデル可用性の更新 | modified | 28 | 27 | 55 | 
| [provisioned-models.md](#item-8ee639) | minor update | プロビジョニングモデルの可用性の更新 | modified | 3 | 3 | 6 | 
| [deploy-models-new.png](#item-eb7e89) | minor update | デプロイメントタイプ画像の更新 | modified | 0 | 0 | 0 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 01/09/2025
+ms.date: 01/15/2025
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -101,6 +101,7 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-35-turbo` | 0125 | No earlier than May 31, 2025 | `gpt-4o-mini` |
 | `gpt-4`<br>`gpt-4-32k` | 0314 | June 6, 2025 | `gpt-4o` |
 | `gpt-4`<br>`gpt-4-32k` | 0613 | June 6, 2025 | `gpt-4o` |
+| `gpt-4` | turbo-2024-04-09 | No earlier than April 9, 2025 | `gpt-4o`|
 | `gpt-4` | 1106-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025 **<sup>1</sup>** | `gpt-4o`|
 | `gpt-4` | 0125-preview |To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025 **<sup>1</sup>**  | `gpt-4o` |
 | `gpt-4` | vision-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025  **<sup>1</sup>** | `gpt-4o`|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの更新日付と情報の追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスにおけるモデルのリタイアメントに関する文書の小規模な更新です。具体的には、ドキュメントの一部である日付情報の更新と、新しいモデルに関する情報の追加が行われました。`ms.date`フィールドが2025年1月9日から2025年1月15日に変更され、さらに新しいモデル`gpt-4`の情報が表に追加されました。これにより、利用可能なモデルの詳細が最新のデータに基づいて更新され、ユーザーが最新の情報を得られるようになっています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -231,6 +231,12 @@ All deployments can perform the exact same inference operations, however the bil
 
 [!INCLUDE [Global data zone provisioned managed](../includes/model-matrix/datazone-provisioned-managed.md)]
 
+# [Data Zone Batch](#tab/datazone-batch)
+
+### Data zone batch model availability
+
+[!INCLUDE [Data zone batch](../includes/model-matrix/global-batch-datazone.md)]
+
 # [Standard](#tab/standard)
 
 ### Standard deployment model availability
@@ -264,7 +270,7 @@ This table doesn't include fine-tuning regional availability information.  Consu
 
 #### Select customer access
 
-In addition to the regions above which are available to all Azure OpenAI customers, some select pre-existing customers have been granted access to versions of GPT-4 in additional regions:
+In addition to the regions above which are available to all Azure OpenAI customers, some select preexisting customers have been granted access to versions of GPT-4 in additional regions:
 
 | Model | Region |  
 |---|:---|  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データゾーンバッチモデルに関する情報の追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関する文書における小規模な更新です。主な内容は、「データゾーンバッチモデル」の可用性に関する情報が追加されたことです。この部分では、データゾーンバッチに関連するモデルの詳細を記載したセクションが新たに導入され、ユーザーがそれらのモデルの使用可能性について知識を得られるようになっています。また、文中の表現に若干の修正が行われ、一部の顧客に特定のGPT-4バージョンへのアクセスが付与されたことについての説明が改善されました。この更新により、文書は最新の情報を反映し、理解しやすさが向上しています。

## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -6,14 +6,14 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: references_regions
 ms.topic: how-to
-ms.date: 10/18/2024
+ms.date: 01/14/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
 zone_pivot_groups: openai-fine-tuning-batch
 ---
 
-# Getting started with Azure OpenAI global batch deployments
+# Getting started with Azure OpenAI batch deployments
 
 The Azure OpenAI Batch API is designed to handle large-scale and high-volume processing tasks efficiently. Process asynchronous groups of requests with separate quota, with 24-hour target turnaround, at [50% less cost than global standard](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). With batch processing, rather than send one request at a time you send a large number of requests in a single file. Global batch requests have a separate enqueued token quota avoiding any disruption of your online workloads.  
 
@@ -38,14 +38,22 @@ Key use cases include:
 >
 > Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).  
 
-## Global batch support
+## Batch support
 
-### Region and model support
+# [Global Batch](#tab/global-batch)
 
-Global batch is currently supported in the following regions:
+### Global batch model availability
 
 [!INCLUDE [Global batch](../includes/model-matrix/global-batch.md)]
 
+# [Data Zone Batch](#tab/datazone-batch)
+
+### Data zone batch model availability
+
+[!INCLUDE [Data zone batch](../includes/model-matrix/global-batch-datazone.md)]
+
+---
+
 The following models support global batch:
 
 | Model | Version | Input format |
@@ -80,9 +88,10 @@ The following aren't currently supported:
 > [!NOTE]
 > Structured outputs is now supported with Global Batch.
 
-### Global batch deployment
+### Batch deployment
 
-In the Azure AI Foundry portal the deployment type will appear as `Global-Batch`.
+> [!NOTE]
+> In the Azure AI Foundry portal the batch deployment types will appear as `Global-Batch` and `Data Zone Batch`. To learn more about Azure OpenAI deployment types, see our [deployment types guide](../how-to/deployment-types.md).
 
 :::image type="content" source="../media/how-to/global-batch/global-batch.png" alt-text="Screenshot that shows the model deployment dialog in Azure AI Foundry portal with Global-Batch deployment type highlighted." lightbox="../media/how-to/global-batch/global-batch.png":::
 
@@ -154,7 +163,7 @@ Yes. Similar to other deployment types, you can create content filters and assoc
 
 ### Can I request additional quota?
 
-Yes, from the quota page in the Azure AI Foundry portal. Default quota allocation can be found in the [quota and limits article](../quotas-limits.md#global-batch-quota).
+Yes, from the quota page in the Azure AI Foundry portal. Default quota allocation can be found in the [quota and limits article](../quotas-limits.md#batch-quota).
 
 ### What happens if the API doesn't complete my request within the 24 hour time frame?
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチデプロイメントに関する情報の更新と拡張"
}
```

### Explanation
この変更は、Azure OpenAIのバッチデプロイメントに関する文書の小規模な更新です。主な改訂には、文書タイトルの変更、日付の更新、及びバッチ処理機能に関連する具体的な情報が含まれています。新たに「データゾーンバッチ」と呼ばれるバッチモデルの可用性が追加され、ユーザーが利用できるモデルに関する情報が明確になりました。

また、「グローバルバッチ」のセクションが改名され、情報が整理されたことで、データの処理や居住に関する情報も一貫して提供されています。さらに、Azure AI Foundryポータルでのデプロイメントタイプに関する具体的な手順や情報が強化され、ユーザーにとっての利便性が向上しています。この改善により、バッチ処理の全体像が明確になり、関連する情報が一元化されることで、読者の理解を深める手助けとなります。

## articles/ai-services/openai/how-to/deployment-types.md{#item-210814}

<details>
<summary>Diff</summary>
````diff
@@ -33,21 +33,6 @@ Data zone deployments leverage Azure's global infrastructure to dynamically rout
 If the Azure OpenAI resource used in your Data Zone deployment is located in the United States, the data will be processed within the United States. If the Azure OpenAI resource used in your Data Zone deployment is located in a European Union Member Nation, the data will be processed within the European Union Member Nation geographies. For all Azure OpenAI service deployment types, any data stored at rest will continue to remain in the geography of the Azure OpenAI resource. Azure data processing and compliance commitments remain applicable.
 
 For any [deployment type](/azure/ai-services/openai/how-to/deployment-types) labeled 'Global,' prompts and responses may be processed in any geography where the relevant Azure OpenAI model is deployed (learn more about [region availability of models](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For any deployment type labeled as 'DataZone,' prompts and responses may be processed in any geography within the specified data zone, as defined by Microsoft. If you create a DataZone deployment in an Azure OpenAI resource located in the United States, prompts and responses may be processed anywhere within the United States. If you create a DataZone deployment in an Azure OpenAI resource located in a European Union Member Nation, prompts and responses may be processed in that or any other European Union Member Nation. For both Global and DataZone deployment types, any data stored at rest, such as uploaded data, is stored in the customer-designated geography. Only the location of processing is affected when a customer uses a Global deployment type or DataZone deployment type in Azure OpenAI Service; Azure data processing and compliance commitments remain applicable.
-## Deployment types
-
-Azure OpenAI offers three types of deployments. These provide a varied level of capabilities that provide trade-offs on: throughput, SLAs, and price. Below is a summary of the options followed by a deeper description of each.
-
-| **Offering** | **Global-Batch** | **Global-Standard**|  **Global-Provisioned**  | **Standard** | **Provisioned**  |
-|---|:---|:---| -------- |:---|:---|
-| **Best suited for**      | Offline scoring <br><br> Workloads that are not latency sensitive and can be completed in hours.<br><br>|Recommended starting place for customers. <br><br>Global-Standard will have the higher default quota and larger number of models available than Standard. |Real-time scoring for large consistent volume. Includes the highest commitments and limits.                                                                                             | For customers with data residency requirements. Optimized for low to medium volume. |Real-time scoring for large consistent volume. Includes the highest commitments and limits.                                                                                          For use cases with data residency requirements|
-| **How it works**         | Offline processing via files |Traffic may be routed anywhere in the world |Traffic may be routed anywhere in the world| | |
-| **Getting started**      | [Global-Batch](./batch.md) | [Model deployment](./create-resource.md) |[Provisioned onboarding](/azure/ai-services/openai/how-to/provisioned-throughput-onboarding)| [Model deployment](./create-resource.md) | [Provisioned onboarding](./provisioned-throughput-onboarding.md) |
-| **Cost**                 | [Least expensive option](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> 50% less cost compared to Global Standard prices. Access to all new models with larger quota allocations.  | [Global deployment pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) |May experience cost savings for consistent usage|  [Regional pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) |May experience cost savings for consistent usage |
-| **What you get**         |[Significant discount compared to Global Standard](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) | Easy access to all new models with the highest default pay-per-call limits.<br><br> Customers with high volume usage may see higher latency variability |Access to high & predictable throughput across Azure global infrastructure. Determine throughput per PTU using the provided [capacity calculator](/azure/ai-services/openai/how-to/provisioned-throughput-onboarding). |  [SLA on availability](https://azure.microsoft.com/support/legal/sla/). Optimized for low to medium volume workloads with high burstiness. <br><br>Customers with high consistent volume may experience greater latency variability. | Regional access with very high & predictable throughput. Determine throughput per PTU using the provided [capacity calculator](./provisioned-throughput-onboarding.md) |
-| **What you don’t get**   |❌Real-time call performance <br><br>❌Data processing guarantee<br> <br> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/)  |❌Data processing guarantee<br> <br> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) |❌Pay-per-call flexibility <br> <br>❌Data processing guarantee<br> <br> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/)| ❌High volume w/consistent low latency | ❌Pay-per-call flexibility |
-| **Per-call Latency**     | Not Applicable (file based async process) | Optimized for real-time calling & low to medium volume usage. Customers with high volume usage may see higher latency variability. Threshold set per model |Optimized for real-time calling & high-volume usage. | Optimized for real-time calling & low to medium volume usage. Customers with high volume usage may see higher latency variability. Threshold set per model |Optimized for real-time calling & high-volume usage.|
-| **Sku Name in code**     |  `GlobalBatch` |   `GlobalStandard`               |`GlobalProvisionedManaged`| `Standard`   |      `ProvisionedManaged`       |
-| **Billing model**        |  Pay-per-token |Pay-per-token |Hourly billing with optional purchase of monthly or yearly reservations| Pay-per-token |Hourly billing with optional purchase of monthly or yearly reservations|
 
 ## Global standard
 
@@ -103,6 +88,13 @@ Customers with high consistent volume may experience greater latency variability
 
 Data zone provisioned deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft specified data zone with the best availability for each request. Data zone provisioned deployments provide reserved model processing capacity for high and predictable throughput using Azure infrastructure within the Microsoft specified data zone.  
 
+## Data zone batch
+
+> [!IMPORTANT]
+> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location within the Microsoft specified data zone. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
+
+Data zone batch deployments provide all the same functionality as [global batch deployments](./batch.md) while allowing you to leverage Azure global infrastructure to dynamically route traffic to only data centers within the Microsoft defined data zone with the best availability for each request. 
+
 ## Standard
 
 Standard deployments provide a pay-per-call billing model on the chosen model. Provides the fastest way to get started as you only pay for what you consume. Models available in each region as well as throughput may be limited.  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントタイプに関する情報の整理と更新"
}
```

### Explanation
この変更は、Azure OpenAIにおけるデプロイメントタイプに関する文書の小規模な更新です。主な変更点として、「デプロイメントタイプ」のセクションが整理され、特に「データゾーンバッチ」に関する情報が新たに追加されました。この新しいデプロイメントタイプは、グローバルバッチデプロイメントと同等の機能を提供すると同時に、Microsoftが定めるデータゾーン内でのトラフィックの動的ルーティングを可能にします。

また、元々あったデプロイメントタイプのテーブルの内容が簡略化され、全体の説明がよりわかりやすくなるよう調整されています。データ処理の居住性に関する注意点も強調され、ユーザーに対して、データの保存と処理の場所についての重要な情報が提供されています。この更新によって、利用者は異なるデプロイメントタイプの機能や利点をより明確に理解できるようになります。

## articles/ai-services/openai/includes/global-batch-limits.md{#item-73207b}

<details>
<summary>Diff</summary>
````diff
@@ -5,21 +5,23 @@ description: Azure OpenAI model global batch limits
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 10/14/2024
+ms.date: 01/14/2025
 ---
 
-## Global batch limits
+## Batch limits
 
 | Limit Name | Limit Value |
 |--|--|
 | Max files per resource | 500 |
 | Max input file size | 200 MB |
 | Max requests per file | 100,000 |
 
-## Global batch quota
+## Batch quota
 
 The table shows the batch quota limit. Quota values for global batch are represented in terms of enqueued tokens. When you submit a file for batch processing the number of tokens present in the file are counted. Until the batch job reaches a terminal state, those tokens will count against your  total enqueued token limit.
 
+### Global batch
+
 |Model|Enterprise agreement|Default| Monthly credit card based subscriptions | MSDN subscriptions | Azure for Students, Free Trials |
 |---|---|---|---|---|---|
 | `gpt-4o` | 5 B | 200 M | 50 M | 90 K | N/A|
@@ -28,4 +30,11 @@ The table shows the batch quota limit. Quota values for global batch are represe
 | `gpt-4` | 150 M | 30 M | 5 M | 100 K | N/A |
 | `gpt-35-turbo` | 10 B | 1 B | 100 M | 2 M | 50 K |
 
-B = billion | M = million | K = thousand
\ No newline at end of file
+B = billion | M = million | K = thousand
+
+### Data zone batch
+
+|Model|Enterprise agreement|Default| Monthly credit card based subscriptions | MSDN subscriptions | Azure for Students, Free Trials |
+|---|---|---|---|---|---|
+| `gpt-4o` | 500 M | 30 M | 30 M | 90 K | N/A|
+| `gpt-4o-mini` | 1.5 B | 100 M | 50 M | 90 K | N/A |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ制限とクォータに関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIのグローバルバッチ制限に関する文書の小規模な更新です。主な改訂点として、日付の更新、セクションタイトルの変更、およびバッチ制限とクォータに関する情報が追加されました。

特に、バッチ制限のテーブルが「グローバルバッチ」から「バッチ」に変更され、より包括的な表現となりました。また、新しいバッチクォータに関するセクションが追加され、データゾーンバッチの限界に関する詳細も含まれています。これにより、ユーザーは異なるモデルに対するバッチ処理の制限やクォータに関する重要な情報をより理解しやすくなりました。

これらの改善により、利用者はAzure OpenAIのバッチ機能を利用する際の制限や費用に関する情報を明確に把握できるようになります。全体として、この更新は文書の構造と可読性を向上させ、利用者にとっての利便性を高めています。

## articles/ai-services/openai/includes/model-matrix/datazone-provisioned-managed.md{#item-ae7f5b}

<details>
<summary>Diff</summary>
````diff
@@ -5,16 +5,20 @@ description: Regional availability for data zone provisioned managed models
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 12/05/2024
+ms.date: 01/15/2025
 ---
 
 | **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
 |:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|
+| eastus             | ✅                       | ✅                       | ✅                            |
 | eastus2            | ✅                       | ✅                       | ✅                            |
 | francecentral      | ✅                       | ✅                       | ✅                            |
 | germanywestcentral | ✅                       | ✅                       | ✅                            |
 | northcentralus     | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                       | ✅                       | ✅                            |
 | southcentralus     | ✅                       | ✅                       | ✅                            |
 | spaincentral       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                       | ✅                       | ✅                            |
 | westeurope         | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                       | ✅                       | ✅                            |
 | westus3            | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データゾーンプロビジョニング済みモデルの地域可用性の更新"
}
```

### Explanation
この変更は、Azure OpenAIのデータゾーンプロビジョニング済みモデルの地域可用性に関する文書の小規模な更新です。具体的には、日付の更新、いくつかの地域に対する可用性チェックマークの追加、及びモデル名の改訂が行われました。

更新された内容には、新たに「ポーランド中央」と「スウェーデン中央」と「西アメリカ」の地域が追加され、これらの地域における各モデルの可用性が確認されました。これにより、ユーザーは特定の地域におけるモデルの利用可能性についてより詳細な情報を得ることができ、実際の利用状況に基づいた意思決定を行いやすくなります。

全体として、この修正は文書の最新情報を提供し、利用者にとっての利便性を向上させています。

## articles/ai-services/openai/includes/model-matrix/global-batch-datazone.md{#item-94a58c}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,18 @@
+---
+title: Global Batch model availability
+titleSuffix: Azure OpenAI Service
+description: Regional availability for Global Batch models
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.custom: references_regions
+ms.date: 01/14/2025
+---
+
+
+| **Region**         |  **gpt-4o**, **2024-08-06**| **gpt-4o-mini**, **2024-07-18**  |
+|:-------------------|:--------------------------:|:--------------------------:|
+| eastus             | ✅                       | ✅                          |  
+| germanywestcentral | ✅                       | ✅                          |
+| swedencentral      | ✅                       | ✅                          |  
+| westus             | ✅                       | ✅                          |  
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "グローバルバッチモデルの可用性に関する新しい文書の追加"
}
```

### Explanation
この変更は、Azure OpenAIにおけるグローバルバッチモデルの地域可用性に関する新しい文書の追加を示しています。新たに作成されたこの文書は、特定の地域での利用可能なモデルの情報を提供しています。

具体的には、文書には各地域のモデルに対する可用性がテーブル形式で示されています。テーブルには、モデル名（gpt-4oおよびgpt-4o-mini）と、対応する地域（eastus、germanywestcentral、swedencentral、westus）においてそれぞれのモデルが利用可能であることがチェックマークで示されています。これにより、ユーザーはどの地域でどのモデルが利用できるかを一目で把握でき、サービスの選択に役立てることができます。

全体的に、この新しい文書の追加は、利用者にとって非常に有益な情報を提供し、Azure OpenAIサービスの活用を促進する目的があります。

## articles/ai-services/openai/includes/model-matrix/global-batch.md{#item-929e6a}

<details>
<summary>Diff</summary>
````diff
@@ -5,30 +5,30 @@ description: Regional availability for Global Batch models
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 11/07/2024
+ms.date: 01/15/2025
 ---
 
 
-| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
-|:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
-| australiaeast      | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| brazilsouth        | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| canadaeast         | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| eastus             | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| eastus2            | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| francecentral      | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| germanywestcentral | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| japaneast          | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| koreacentral       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| northcentralus     | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| norwayeast         | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| polandcentral      | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southafricanorth   | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southcentralus     | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southindia         | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| swedencentral      | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| switzerlandnorth   | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| uksouth            | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westeurope         | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westus             | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westus3            | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
\ No newline at end of file
+| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
+|:-------------------|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
+| australiaeast      | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| brazilsouth        | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| canadaeast         | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| eastus             | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| eastus2            | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| francecentral      | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| germanywestcentral | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| japaneast          | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| koreacentral       | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| northcentralus     | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| norwayeast         | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| polandcentral      | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southafricanorth   | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southcentralus     | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southindia         | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| swedencentral      | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| switzerlandnorth   | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| uksouth            | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westeurope         | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westus             | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westus3            | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルバッチモデルの可用性の更新"
}
```

### Explanation
この変更は、Azure OpenAIのグローバルバッチモデルに関する文書の更新を示します。主な変更点として、モデルの可用性に関するテーブルが更新され、いくつかのモデルの情報が追加または修正されました。

具体的には、テーブルには各地域に対する複数のモデル（gpt-4o、gpt-4o-mini、gpt-4、gpt-35-turboなど）の可用性が示されています。新しい日付が適用され、一部のモデルに関する利用可能性が更新されたことにより、ユーザーはより正確で最新な情報を得ることができます。特に、新たに「gpt-4o）の2024年11月20日のバージョンが追加され、他のいくつかのモデルは特定の地域での可用性が削除されました。

この更新は、ユーザーが地域ごとのモデル利用可能性についての最新情報にアクセスし、それに基づいてサービスを選択する際に非常に役立ちます。全体えお通して、この修正は文書の情報の正確性を向上させ、ユーザー体験を改善することを目的としています。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -6,32 +6,33 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 10/25/2024
+ms.date: 01/15/2025
 ---
 
-| **Region**     | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:--------------------------:|:-------------------------------:|
-| australiaeast      | ✅                       | ✅                            |
-| brazilsouth        | ✅                       | ✅                            |
-| canadacentral      | ✅                       | ✅                            |
-| canadaeast         | ✅                       | ✅                            |
-| eastus             | ✅                       | ✅                            |
-| eastus2            | ✅                       | ✅                            |
-| francecentral      | ✅                       | ✅                            |
-| germanywestcentral | ✅                       | ✅                            |
-| japaneast          | ✅                       | ✅                            |
-| koreacentral       | ✅                       | ✅                            |
-| northcentralus     | ✅                       | ✅                            |
-| norwayeast         | ✅                       | ✅                            |
-| polandcentral      | ✅                       | ✅                            |
-| southafricanorth   | ✅                       | ✅                            |
-| southcentralus     | ✅                       | ✅                            |
-| southindia         | ✅                       | ✅                            |
-| swedencentral      | ✅                       | ✅                            |
-| switzerlandnorth   | ✅                       | ✅                            |
-| switzerlandwest    | ✅                       | ✅                            |
-| uaenorth           | ✅                       | ✅                            |
-| uksouth            | ✅                       | ✅                            |
-| westeurope         | ✅                       | ✅                            |
-| westus             | ✅                       | ✅                            |
-| westus3            | ✅                       | ✅                            |
\ No newline at end of file
+| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|
+| australiaeast      | -                      | ✅                       | ✅                            |
+| brazilsouth        | -                      | ✅                       | ✅                            |
+| canadacentral      | -                      | ✅                       | ✅                            |
+| canadaeast         | -                      | ✅                       | ✅                            |
+| eastus             | ✅                       | ✅                       | ✅                            |
+| eastus2            | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | -                      | ✅                       | ✅                            |
+| japaneast          | -                      | ✅                       | ✅                            |
+| koreacentral       | -                      | ✅                       | ✅                            |
+| northcentralus     | -                      | ✅                       | ✅                            |
+| norwayeast         | -                      | ✅                       | ✅                            |
+| polandcentral      | -                      | ✅                       | ✅                            |
+| southafricanorth   | -                      | ✅                       | ✅                            |
+| southcentralus     | ✅                       | ✅                       | ✅                            |
+| southindia         | -                      | ✅                       | ✅                            |
+| spaincentral       | -                      | ✅                       | ✅                            |
+| swedencentral      | ✅                       | ✅                       | ✅                            |
+| switzerlandnorth   | -                      | ✅                       | ✅                            |
+| switzerlandwest    | -                      | ✅                       | ✅                            |
+| uaenorth           | ✅                       | ✅                       | ✅                            |
+| uksouth            | -                      | ✅                       | ✅                            |
+| westeurope         | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされたグローバルモデル可用性の更新"
}
```

### Explanation
この変更は、Azure OpenAIのプロビジョニングされたグローバルモデルに関する文書の更新を示しています。主な更新内容としては、モデルの可用性を示すテーブルが変更され、いくつかのモデルに関する情報が追加または修正されている点です。

具体的には、テーブル内のモデル情報が包括的に更新され、各地域（例えば、オーストラリア東部、ブラジル南部、カナダ中部など）に対する利用可能なモデルの状況が見直されています。この新しいテーブルでは、特定のモデル（gpt-4o、gpt-4o-miniなど）の提供日や可用性が異なることが明記されています。特に、一部の地域において新しいモデルの提供状況が「-」で示されており、特定のモデルはその地域で利用できないことを意味します。

この修正により、ユーザーは最新のモデル可用性情報にアクセスでき、情報に基づいてサービスを選択する際により良い判断ができるようになります。全体として、この更新は文書の有用性と正確性を向上させ、Azure OpenAIサービスの利用を促進することを目指しています。

## articles/ai-services/openai/includes/model-matrix/provisioned-models.md{#item-8ee639}

<details>
<summary>Diff</summary>
````diff
@@ -14,23 +14,23 @@ ms.date: 10/24/2024
 | australiaeast      | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | brazilsouth        | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | -                      |
 | canadacentral      | ✅                       | -                      | -                           | ✅                | -                       | -                       | -                           | ✅                    | -                      | ✅                       |
-| canadaeast         | ✅                       | -                      | ✅                            | ✅                | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      |
+| canadaeast         | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      |
 | eastus             | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | eastus2            | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | francecentral      | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | -                      | ✅                       |
 | germanywestcentral | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | -                      |
 | japaneast          | ✅                       | ✅                       | ✅                            | -               | ✅                        | ✅                        | ✅                            | -                   | -                      | ✅                       |
 | koreacentral       | ✅                       | ✅                       | ✅                            | ✅                | -                       | -                       | ✅                            | ✅                    | ✅                       | -                      |
 | northcentralus     | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| norwayeast         | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                           | ✅                    | -                      | -                      |
+| norwayeast         | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                           | ✅                    | -                      | -                      |
 | polandcentral      | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | southafricanorth   | ✅                       | -                      | -                           | ✅                | ✅                        | -                       | ✅                            | ✅                    | ✅                       | -                      |
 | southcentralus     | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | southindia         | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | ✅                       |
 | swedencentral      | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | switzerlandnorth   | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | switzerlandwest    | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
-| uaenorth           | ✅                       | -                      | -                           | -               | ✅                        | -                       | -                           | -                   | ✅                       | ✅                       |
+| uaenorth           | ✅                       | ✅                       | -                           | -               | ✅                        | -                       | -                           | -                   | ✅                       | ✅                       |
 | uksouth            | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | westus             | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | westus3            | ✅                       | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングモデルの可用性の更新"
}
```

### Explanation
この変更は、Azure OpenAIにおけるプロビジョニングモデルの可用性に関する文書が更新されたことを示します。主な内容として、可用性を示すテーブルの一部が修正され、いくつかのモデルに関する情報が追加または変更されています。

具体的には、テーブルの各地域のモデル対応状況が見直され、特にカナダ東部とノルウェー東部におけるモデルの利用状況が改善されました。これにより、一部の地域で新たに利用可能なモデルが追加され、他のモデルの対応状況が明確化されています。また、いくつかのモデルの提供日も更新され、最新の情報が反映されています。

この修正により、ユーザーは特定の地域におけるモデルの最新の可用性情報にアクセスでき、より正確にサービスの選択を行うことができるようになります。全体的に見て、この更新は文書の正確性を向上させ、Azure OpenAIサービスの利用をよりスムーズにすることを目的としています。

## articles/ai-services/openai/media/deployment-types/deploy-models-new.png{#item-eb7e89}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントタイプ画像の更新"
}
```

### Explanation
この変更は、Azure OpenAIにおけるデプロイモデルの種類を示す画像ファイルの更新を示しています。具体的には、`deploy-models-new.png`というファイルが修正されましたが、追加や削除は行われていないため、実際の内容の変更はなかったと考えられます。

この変更は、視覚的な要素を最新の状態に維持するためのものであり、コンテンツの他の部分と整合性を持たせることを目的としています。画像の更新は、ユーザーが今後の文書やガイドラインにアクセスしたときに、より明確で関連性のある情報が提供されることを意図しています。

全体として、この更新は文書の視覚的な魅力を向上させ、読者にとっての理解を助けることを狙っています。


