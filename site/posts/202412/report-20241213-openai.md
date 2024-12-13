---
date: '2024-12-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a7b86da...MicrosoftDocs:3d9c9bc
summary: 今回のコード変更では、Azure OpenAIサービスに関するドキュメントが更新され、特にリアルタイムAPIに関連する新機能が追加されました。また、既存の文書の明確化と情報の整理が行われています。新機能には、GPT-4oリアルタイムAPIに関する新しいドキュメントの追加や、プレビュー機能のインクルードファイル、リアルタイムAPIリファレンスの追加が含まれます。破壊的変更はないものの、文書の整理や用語の統一が重要な点です。これらの更新は、ユーザーエクスペリエンスの向上を目的としており、特にAzure
  Governmentやファインチューニング情報、モデル退職のスケジュール、新地域の追加、リアルタイムAPIのリソース提供において詳細が改善されています。全体として、ユーザーのナビゲーションや理解を助ける内容となっています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a7b86da...MicrosoftDocs:3d9c9bc){target="_blank"}

# ハイライト

今回のコード変更には、Azure OpenAIサービスにおける数々のドキュメント更新が含まれています。特に注目すべき点は、リアルタイムAPIに関する新機能と、既存の文書の明確化や情報の追加です。

## 新機能
- GPT-4oリアルタイムAPIに関連する新規ドキュメントの追加。
- プレビュー機能に関するインクルードファイルの追加。
- リアルタイムAPIリファレンスの追加。

## 破壊的変更
今回の変更に破壊的な変更は含まれていませんが、一部ドキュメントの削除および情報の整理は注目に値します。

## その他の更新
- 各種ドキュメントでの内容の明確化および用語の統一。
- ファインチューニングやモデル退職に関する情報の更新。
- 地域可用性の追加と関連情報の編集。

# インサイト

このドキュメントの更新は、Azure OpenAIサービスのユーザーエクスペリエンスを改善し、より正確かつ分かりやすい情報提供を目指すものです。以下に各種変更の詳細とその背景を説明します。

## Azure Governmentのドキュメント更新

Azure Governmentに関する文書は、ユーザーがサービスを簡単に利用できるよう、タイトルの形式や情報の整理が行われました。これにはモデルクォータ制限の明確化やデプロイメントモデルの可用性に関する可読性の向上が含まれています。

## ファインチューニングに関する考慮事項の更新

ファインチューニングに関する文書では、読者が準備状況を理解しやすくするため、記述の一貫性と明瞭性が向上されました。データセットの整形についての記述がより具体的になり、ユーザーが自身のプロジェクトに対する自信を持ちやすくなっています。

## モデルの退職情報の更新

`text-embedding-ada-002`モデルの退職スケジュールが延長されました。この更新により、利用者はモデル使用の計画を立てやすくなり、サービスの長期運用における信頼性も向上します。

## プロビジョニングされたスループットに関する情報の更新

ユーザーがスループットの管理をより理解しやすくするため、ドキュメントではPTUに関する詳細やエラーハンドリングの説明が修正されています。これにより、サービスの効率的な利用が促進されます。

## 評価機能の地域対応情報の更新

「East US2」という新しい地域が追加され、Azure OpenAIサービスの地理的拡張が確認できました。これにより、より多くのユーザーがサービスを利用できるようになります。

## リアルタイムAPI関連の情報追加

GPT-4oリアルタイムAPIに関する新しいドキュメントは、開発者が音声アシスタントやリアルタイム翻訳など多様なユースケースでこのAPIを利用するためのリソースとして提供されます。WebSocketベースの非同期通信機能を強調し、開発者が高度に応答性の高いアプリケーションを構築する支援を行います。

## プレビュー機能のインクルード

プレビュー機能のインクルードファイルにより、開発者は今後の公開機能への期待とリスクを適切に理解し、実運用での使用を控えることが推奨されます。これにより、ユーザーは未成熟な技術の育成過程を追うことができます。

## 目次の更新

目次に新機能や地域更新の項目が追加され、ユーザーのナビゲーション体験が向上しました。全体を通じて、これらの更新はAzure OpenAIサービスのドキュメントの機能性と情報提供を高め、開発者にとってより便利で理解しやすい内容となっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-government.md](#item-a47549) | minor update | Azure Government Documentationの更新 | modified | 9 | 6 | 15 | 
| [fine-tuning-considerations.md](#item-71d8ac) | minor update | ファインチューニングに関する考慮事項の更新 | modified | 6 | 6 | 12 | 
| [model-retirements.md](#item-03fc2e) | minor update | モデルの退任に関する情報の更新 | modified | 8 | 4 | 12 | 
| [provisioned-throughput.md](#item-022e0c) | minor update | プロビジョニングされたスループットに関する情報の更新 | modified | 24 | 24 | 48 | 
| [evaluations.md](#item-dfaa1c) | minor update | 評価機能の地域対応情報に関する更新 | modified | 1 | 0 | 1 | 
| [fine-tuning.md](#item-5c0e85) | minor update | ファインチューニングに関する注意事項の削除 | modified | 0 | 3 | 3 | 
| [realtime-audio.md](#item-482ba3) | new feature | Azure OpenAIサービスのためのGPT-4oリアルタイムAPIに関する新規ドキュメント | added | 165 | 0 | 165 | 
| [fine-tuning-unified.md](#item-718336) | minor update | ファインチューニング体験の説明の更新 | modified | 6 | 1 | 7 | 
| [preview-feature.md](#item-564a89) | new feature | プレビュー機能に関するインクルードファイルの追加 | added | 10 | 0 | 10 | 
| [realtime-audio-quickstart.md](#item-727df8) | minor update | リアルタイムオーディオAPIに関する記事の修正 | modified | 5 | 2 | 7 | 
| [realtime-audio-reference.md](#item-276d51) | new feature | リアルタイムAPIリファレンスの追加 | added | 1487 | 0 | 1487 | 
| [toc.yml](#item-c945af) | minor update | 目次にリアルタイムAPI関連の項目を追加 | modified | 4 | 0 | 4 | 


# Modified Contents
## articles/ai-services/openai/azure-government.md{#item-a47549}

<details>
<summary>Diff</summary>
````diff
@@ -21,20 +21,23 @@ Learn more about the different capabilities of each model in [Azure OpenAI Servi
 
 The following sections show model availability by region and deployment type.
 
-### Standard deployment model availability
+<br>
+
+## Standard deployment model availability
 |   **Region**  | **gpt-4o**, **2024-05-13** | **gpt-4o-mini**, **2024-07-18** | **gpt-4**, **1106-Preview** | **gpt-35-turbo**, **0125** | **gpt-35-turbo**, **1106** | **text-embedding-3-large**, **1** | **text-embedding-ada-002**, **2** |
 |:--------------|:--------------------------:|:-------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:---------------------------------:|:---------------------------------:|
 | usgovarizona  | ✅ | ✅ | ✅ | ✅ | -  | ✅ | ✅ |
 | usgovvirginia | ✅ | -  | ✅ | ✅ | ✅ |  - | ✅ |
- 
-#### Standard quota limits in tokens per minute (TPM): 
+
+To request quota increases for these models, submit a request at [https://aka.ms/AOAIGovQuota](https://aka.ms/AOAIGovQuota). Please note the following maximum quota limits that will be granted via that form:
+
 | **gpt-4o** | **gpt-4o-mini** | **gpt-4** | **gpt-35-turbo** | **text-embedding-3-large** | **text-embedding-ada-002**|
 |:----------:|:---------------:|:---------:|:----------------:|:--------------------------:|:-------------------------:|
-|    300k    |      600k       |    200k   |      500k        |            700k            |           600k            |
+|    300k    |      600k       |    200k   |      500k        |            700k            |           700k            |
 
-To request quota increases up to these maximum values, submit a request at [https://aka.ms/AOAIGovQuota](https://aka.ms/AOAIGovQuota).
+<br>
 
-### Provisioned deployment model availability
+## Provisioned deployment model availability
 |   **Region**  | **gpt-4o**, **2024-05-13** | **gpt-4o-mini**, **2024-07-18** | **gpt-4**, **1106-Preview** | **gpt-35-turbo**, **0125** | **gpt-35-turbo**, **1106** |
 |:--------------|:--------------------------:|:-------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|
 | usgovarizona  | ✅ | - | - | ✅ | - |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Government Documentationの更新"
}
```

### Explanation
この変更は、Azure Governmentに関する文書の一部を更新するもので、主にヘッダーとテーブルの構成に関連しています。具体的には、標準的なデプロイメントモデルの可用性とプロビジョンドデプロイメントモデルの可用性のセクションでのタイトルの形式が変更されました。また、モデルの最大クォータ制限に関する情報が整理され、リクエストのためのリンクが明示的に記載されています。

主な変更点には、セクションタイトルの形式を変更し、Markdownの可読性を向上させるためにテーブルの一部を再配置しました。また、特定のモデルに関するクォータ制限に対する改訂が盛り込まれ、新しい情報が追加されました。全体として、この更新は情報をより明確にし、ユーザーが理解しやすくすることを目指しています。

## articles/ai-services/openai/concepts/fine-tuning-considerations.md{#item-71d8ac}

<details>
<summary>Diff</summary>
````diff
@@ -66,9 +66,9 @@ Here’s an example: A customer wanted to use GPT-3.5-Turbo to turn natural lang
 **If you are ready for fine-tuning you:**
 
 - Have clear examples on how you have approached the challenges in alternate approaches and what’s been tested as possible resolutions to improve performance.
-- You've identified shortcomings using a base model, such as inconsistent performance on edge cases, inability to fit enough few shot prompts in the context window to steer the model, high latency, etc.
+- Identified shortcomings using a base model, such as inconsistent performance on edge cases, inability to fit enough few shot prompts in the context window to steer the model, high latency, etc.
 
-**Common signs you might not be ready for fine-tuning yet:**
+**Common signs you might not be ready for fine-tuning include:**
 
 - Insufficient knowledge from the model or data source.
 - Inability to find the right data to serve the model.
@@ -86,9 +86,9 @@ Another important point is even with high quality data if your data isn't in the
 
 **If you are ready for fine-tuning you:**
 
-- Have identified a dataset for fine-tuning.
-- The dataset is in the appropriate format for training.
-- Some level of curation has been employed to ensure dataset quality.
+- Identified a dataset for fine-tuning.
+- Formatted the dataset appropriately for training.
+- Curated the dataset to ensure quality.
 
 **Common signs you might not be ready for fine-tuning yet:**
 
@@ -103,4 +103,4 @@ There isn’t a single right answer to this question, but you should have clearl
 
 - Watch the [Azure AI Show episode: "To fine-tune or not to fine-tune, that is the question"](https://www.youtube.com/watch?v=0Jo-z-MFxJs)
 - Learn more about [Azure OpenAI fine-tuning](../how-to/fine-tuning.md)
-- Explore our [fine-tuning tutorial](../tutorials/fine-tune.md)
\ No newline at end of file
+- Explore our [fine-tuning tutorial](../tutorials/fine-tune.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングに関する考慮事項の更新"
}
```

### Explanation
この変更は、ファインチューニングに関する考慮事項を説明する文書の一部を改訂するもので、文章の整合性と可読性を向上させるためにいくつかの表現が修正されました。具体的には、「準備が整っている」ことや「準備が整っていない」ことを示す条件の記述が、より明確で一貫性のある形式に変更されました。

主な変更点には、「あなたがファインチューニングの準備ができている場合」と「まだ早いかもしれない一般的な兆候」の段落内での表現が簡略化され、より簡潔な言い回しに置き換えられています。また、データセットの特定や適切なフォーマットへの整形に関する記述も、同じく明確化されています。この更新により、読者はファインチューニングの準備状況をより簡単に理解できるようになります。

## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -107,10 +107,10 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-4o` | 2024-05-13 | No earlier than May 20, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on February 13, 2025. | |
 | `gpt-4o-mini` | 2024-07-18 | No earlier than July 18, 2025  | |
 | `gpt-3.5-turbo-instruct` | 0914 | No earlier than February 1, 2025 |  |
-| `text-embedding-ada-002` | 2 | No earlier than April 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
-| `text-embedding-ada-002` | 1 | No earlier than April 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
-| `text-embedding-3-small` | | No earlier than April 3, 2025 | |
-| `text-embedding-3-large` | | No earlier than April 3, 2025 | |
+| `text-embedding-ada-002` | 2 | No earlier than October 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
+| `text-embedding-ada-002` | 1 | No earlier than October 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
+| `text-embedding-3-small` | | No earlier than October 3, 2025 | |
+| `text-embedding-3-large` | | No earlier than October 3, 2025 | |
 
  **<sup>1</sup>** We will notify all customers with these preview deployments at least 30 days before the start of the upgrades. We will publish an upgrade schedule detailing the order of regions and model versions that we will follow during the upgrades, and link to that schedule from here.
 
@@ -162,6 +162,10 @@ If you're an existing customer looking for information about these models, see [
 
 ## Retirement and deprecation history
 
+## December 11, 2024
+
+Embeddings models updated to no earlier than October 3, 2025.
+
 ## December 2, 2024
 
 `gpt-3.5-turbo-instruct` updated to no earlier than February 1, 2025.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの退任に関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるモデルの退任に関する情報を更新するもので、特定のモデルの対応日や退任スケジュールについての詳細が変更されています。具体的には、`text-embedding-ada-002`とその各バージョンについての退任が延長され、以前の「2025年4月3日」から「2025年10月3日」以降に引き上げられました。

また、モデルの退任および廃止履歴のセクションに新しい日付が追加され、最新の退任予定についての情報が明確化されています。これにより、ユーザーはモデルの使用とその更新に関する最新情報にアクセスしやすくなります。この変更は、サービスの運用に影響を与える重要な情報を提供し、ユーザーへの通知計画についても言及されています。

## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -1,8 +1,8 @@
 ---
 title: Azure OpenAI Service provisioned throughput
-description: Learn about provisioned throughput and Azure OpenAI. 
+description: Learn about provisioned throughput and Azure OpenAI.
 ms.service: azure-ai-openai
-ms.topic: conceptual 
+ms.topic: conceptual
 ms.date: 08/07/2024
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -20,7 +20,7 @@ The provisioned throughput capability allows you to specify the amount of throug
 
 ## What do the provisioned deployment types provide?
 
-- **Predictable performance:** stable max latency and throughput for uniform workloads. 
+- **Predictable performance:** stable max latency and throughput for uniform workloads.
 - **Reserved processing capacity:** A deployment configures the amount of throughput. Once deployed, the throughput is available whether used or not.
 - **Cost savings:** High throughput workloads might provide cost savings vs token-based consumption.
 
@@ -40,7 +40,7 @@ An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model.
 
 
 ## How much throughput per PTU you get for each model
-The amount of throughput (tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in the minute. Generating output tokens requires more processing than input tokens and so the more output tokens generated the lower your overall TPM. The service dynamically balances the input & output costs, so users do not have to set specific input and output limits. This approach means your deployment is resilient to fluctuations in the workload shape. 
+The amount of throughput (tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in the minute. Generating output tokens requires more processing than input tokens and so the more output tokens generated the lower your overall TPM. The service dynamically balances the input & output costs, so users do not have to set specific input and output limits. This approach means your deployment is resilient to fluctuations in the workload shape.
 
 To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the `gpt-4o` and `gpt-4o-mini` models which represent the max TPM assuming all traffic is either input or output. To understand how different ratios of input and output tokens impact your Max TPM per PTU, see the [Azure OpenAI capacity calculator](https://oai.azure.com/portal/calculator). The table also shows Service Level Agreement (SLA) Latency Target Values per model.  For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
 
@@ -77,39 +77,39 @@ az cognitiveservices account deployment create \
 --model-version 0613  \
 --model-format OpenAI \
 --sku-capacity 100 \
---sku-name ProvisionedManaged 
+--sku-name ProvisionedManaged
 ```
 
 ### Quota
 
-#### Provisioned throughput units 
+#### Provisioned throughput units
 
 Provisioned throughput units (PTU) are generic units of model processing capacity that you can use to size provisioned deployments to achieve the required throughput for processing prompts and generating completions.   Provisioned throughput units are granted to a subscription as quota. Each quota is specific to a region and defines  the maximum number of PTUs that can be assigned to deployments in that subscription and region.
 
 
 #### Model independent quota
 
-Unlike the Tokens Per Minute (TPM) quota used by other Azure OpenAI offerings, PTUs are model-independent. The PTUs might be used to deploy any supported model/version in the region. 
+Unlike the Tokens Per Minute (TPM) quota used by other Azure OpenAI offerings, PTUs are model-independent. The PTUs might be used to deploy any supported model/version in the region.
 
 :::image type="content" source="../media/provisioned/model-independent-quota.png" alt-text="Diagram of model independent quota with one pool of PTUs available to multiple Azure OpenAI models." lightbox="../media/provisioned/model-independent-quota.png":::
 
 For provisioned deployments, the new quota shows up in Azure AI Foundry as a quota item named **Provisioned Managed Throughput Unit**. For global provisioned deployments, the new quota shows up in the Azure AI Foundry as a quota item named **Global Provisioned Managed Throughput Unit**.  For data zone provisioned deployments, the new quota shows up in Azure AI Foundry as a quota item named **Data Zone Provisioned Managed Throughput Unit.** In the Foundry Quota pane, expanding the quota item shows the deployments contributing to usage of each quota.
 
 :::image type="content" source="../media/provisioned/ptu-quota-page.png" alt-text="Screenshot of quota UI for Azure OpenAI provisioned." lightbox="../media/provisioned/ptu-quota-page.png":::
 
-#### Obtaining PTU Quota 
+#### Obtaining PTU Quota
 
 PTU quota is available by default in many regions. If more quota is required, customers can request quota via the Request Quota link. This link can be found to the right of the designated provisioned deployment type quota tabs in Azure AI Foundry The form allows the customer to request an increase in the specified PTU quota for a given region. The customer receives an email at the included address once the request is approved, typically within two business days. 
 
-#### Per-Model PTU Minimums 
+#### Per-Model PTU Minimums
 
-The minimum PTU deployment, increments, and processing capacity associated with each unit varies by model type & version. 
+The minimum PTU deployment, increments, and processing capacity associated with each unit varies by model type & version.
 
 ## Capacity transparency
 
-Azure OpenAI is a highly sought-after service where customer demand might exceed service GPU capacity. Microsoft strives to provide capacity for all in-demand regions and models, but selling out a region is always a possibility. This constraint can limit some customers’ ability to create a deployment of their desired model, version, or number of PTUs in a desired region - even if they have quota available in that region. Generally speaking:
+Azure OpenAI is a highly sought-after service where customer demand might exceed service GPU capacity. Microsoft strives to provide capacity for all in-demand regions and models, but selling out a region is always a possibility. This constraint can limit some customers' ability to create a deployment of their desired model, version, or number of PTUs in a desired region - even if they have quota available in that region. Generally speaking:
 
-- Quota places a limit on the maximum number of PTUs that can be deployed in a subscription and region, and does not guarantee of capacity availability. 
+- Quota places a limit on the maximum number of PTUs that can be deployed in a subscription and region, and does not guarantee of capacity availability.
 - Capacity is allocated at deployment time and is held for as long as the deployment exists.  If service capacity is not available, the deployment will fail
 - Customers use real-time information on quota/capacity availability to choose an appropriate region for their scenario with the necessary model capacity
 - Scaling down or deleting a deployment releases capacity back to the region.  There is no guarantee that the capacity will be available should the deployment be scaled up or re-created later.
@@ -132,7 +132,7 @@ If an acceptable region isn't available to support the desire model, version and
 
 ### Determining the number of PTUs needed for a workload
 
-PTUs represent an amount of model processing capacity. Similar to your computer or databases, different workloads or requests to the model will consume different amounts of underlying processing capacity. The conversion from call shape characteristics (prompt size, generation size and call rate) to PTUs is complex and nonlinear. To simplify this process, you can use the [Azure OpenAI Capacity calculator](https://oai.azure.com/portal/calculator) to size specific workload shapes. 
+PTUs represent an amount of model processing capacity. Similar to your computer or databases, different workloads or requests to the model will consume different amounts of underlying processing capacity. The conversion from call shape characteristics (prompt size, generation size and call rate) to PTUs is complex and nonlinear. To simplify this process, you can use the [Azure OpenAI Capacity calculator](https://oai.azure.com/portal/calculator) to size specific workload shapes.
 
 A few high-level considerations:
 - Generations require more capacity than prompts
@@ -152,29 +152,29 @@ The [Provisioned-Managed Utilization V2 metric](../how-to/monitoring.md#azure-op
 The 429 response isn't an error, but instead part of the design for telling users that a given deployment is fully utilized at a point in time. By providing a fast-fail response, you have control over how to handle these situations in a way that best fits your application requirements.
 
 The  `retry-after-ms` and `retry-after` headers in the response tell you the time to wait before the next call will be accepted. How you choose to handle this response depends on your application requirements. Here are some considerations:
--	You can consider redirecting the traffic to other models, deployments, or experiences. This option is the lowest-latency solution because the action can be taken as soon as you receive the 429 signal. For ideas on how to effectively implement this pattern see this [community post](https://github.com/Azure/aoai-apim).
--	If you're okay with longer per-call latencies, implement client-side retry logic. This option gives you the highest amount of throughput per PTU. The Azure OpenAI client libraries include built-in capabilities for handling retries.
+-    You can consider redirecting the traffic to other models, deployments, or experiences. This option is the lowest-latency solution because the action can be taken as soon as you receive the 429 signal. For ideas on how to effectively implement this pattern see this [community post](https://github.com/Azure/aoai-apim).
+-    If you're okay with longer per-call latencies, implement client-side retry logic. This option gives you the highest amount of throughput per PTU. The Azure OpenAI client libraries include built-in capabilities for handling retries.
 
 #### How does the service decide when to send a 429?
 
 In all provisioned deployment types, each request is evaluated individually according to its prompt size, expected generation size, and model to determine its expected utilization. This is in contrast to pay-as-you-go deployments, which have a [custom rate limiting behavior](../how-to/quota.md) based on the estimated traffic load. For pay-as-you-go deployments this can lead to HTTP 429 errors being generated prior to defined quota values being exceeded if traffic is not evenly distributed.
 
 For provisioned deployments, we use a variation of the leaky bucket algorithm to maintain utilization below 100% while allowing some burstiness in the traffic. The high-level logic is as follows:
 
-1.	Each customer has a set amount of capacity they can utilize on a deployment
+1. Each customer has a set amount of capacity they can utilize on a deployment
 1. When a request is made:
 
-   a.	When the current utilization is above 100%, the service returns a 429 code with the `retry-after-ms` header set to the time until utilization is below 100%
+    a.    When the current utilization is above 100%, the service returns a 429 code with the `retry-after-ms` header set to the time until utilization is below 100%
 
-   b.	Otherwise, the service estimates the incremental change to utilization required to serve the request by combining prompt tokens and the specified `max_tokens` in the call. For requests that include at least 1024 cached tokens, the cached tokens are subtracted from the prompt token value. A customer can receive up to a 100% discount on their prompt tokens depending on the size of their cached tokens. If the `max_tokens` parameter is not specified, the service estimates a value. This estimation can lead to lower concurrency than expected when the number of actual generated tokens is small.  For highest concurrency, ensure that the `max_tokens` value is as close as possible to the true generation size. 
-   
-3.	When a request finishes, we now know the actual compute cost for the call. To ensure an accurate accounting, we correct the utilization using the following logic:
+    b.    Otherwise, the service estimates the incremental change to utilization required to serve the request by combining prompt tokens and the specified `max_tokens` in the call. For requests that include at least 1024 cached tokens, the cached tokens are subtracted from the prompt token value. A customer can receive up to a 100% discount on their prompt tokens depending on the size of their cached tokens. If the `max_tokens` parameter is not specified, the service estimates a value. This estimation can lead to lower concurrency than expected when the number of actual generated tokens is small.  For highest concurrency, ensure that the `max_tokens` value is as close as possible to the true generation size.
 
-    a.	If the actual > estimated, then the difference is added to the deployment's utilization
+1.  When a request finishes, we now know the actual compute cost for the call. To ensure an accurate accounting, we correct the utilization using the following logic:
 
-    b.	If the actual < estimated, then the difference is subtracted. 
+    a.    If the actual > estimated, then the difference is added to the deployment's utilization.
 
-4.	The overall utilization is decremented down at a continuous rate based on the number of PTUs deployed. 
+    b.    If the actual < estimated, then the difference is subtracted.
+
+1.  The overall utilization is decremented down at a continuous rate based on the number of PTUs deployed. 
 
 > [!NOTE]
 > Calls are accepted until utilization reaches 100%. Bursts just over 100% may be permitted in short periods, but over time, your traffic is capped at 100% utilization.
@@ -196,4 +196,4 @@ The number of concurrent calls you can achieve depends on each call's shape (pro
 ## Next steps
 
 - [Learn about the onboarding steps for provisioned deployments](../how-to/provisioned-throughput-onboarding.md)
-- [Provisioned Throughput Units (PTU) getting started guide](../how-to//provisioned-get-started.md) 
+- [Provisioned Throughput Units (PTU) getting started guide](../how-to//provisioned-get-started.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされたスループットに関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「プロビジョニングされたスループット」に関する文書を更新したもので、文章の明瞭さと一貫性を向上させるためにいくつかの表現が修正されています。具体的には、文の内容が調整され、プレースホルダーや不要な改行が削除され、フォーマットが整えられました。

重要なポイントとして、スループットユニット（PTU）の説明や、モデルごとのスループットの情報がより明確に記載されるようになっています。また、エラーハンドリングに関するセクションも精緻化され、ユーザーが処理の利用状況をより適切に管理できるように情報が整理されています。これにより、文書全体の可読性が向上し、ユーザーにとって役立つ内容になっています。

## articles/ai-services/openai/how-to/evaluations.md{#item-dfaa1c}

<details>
<summary>Diff</summary>
````diff
@@ -22,6 +22,7 @@ Azure OpenAI evaluation enables developers to create evaluation runs to test aga
 
 ### Regional availability
 
+- East US2
 - North Central US
 - Sweden Central
 - Switzerland West
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価機能の地域対応情報に関する更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスの評価機能に関する文書において、新たに「East US2」という地域を追加する内容の更新です。この追加により、開発者が評価を実施できる地域が明確になり、サービスの利用可能範囲が広がったことを示しています。

具体的には、地域の可用性のセクションに「East US2」が加えられ、他の地域とともに利用可能な地域のリストが更新されています。この変更は、ユーザーが自分の地域での評価実施に関する情報を簡単に確認できるようにするためのもので、サービスの透明性や利便性を向上させる要素となっています。

## articles/ai-services/openai/how-to/fine-tuning.md{#item-5c0e85}

<details>
<summary>Diff</summary>
````diff
@@ -26,9 +26,6 @@ In contrast to few-shot learning, fine tuning improves the model by training on
 
 We use LoRA, or low rank approximation, to fine-tune models in a way that reduces their complexity without significantly affecting their performance. This method works by approximating the original high-rank matrix with a lower rank one, thus only fine-tuning a smaller subset of *important* parameters during the supervised training phase, making the model more manageable and efficient. For users, this makes training faster and more affordable than other techniques.
 
-> [!NOTE]
-> Azure OpenAI currently only supports text-to-text fine-tuning for all supported models including GPT-4o mini.
-
 ::: zone pivot="programming-language-studio"
 
 [!INCLUDE [Azure OpenAI Studio fine-tuning](../includes/fine-tuning-unified.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングに関する注意事項の削除"
}
```

### Explanation
この変更は、Azure OpenAIサービスのファインチューニングに関する文書から情報の一部を削除したものです。具体的には、「Azure OpenAI currently only supports text-to-text fine-tuning for all supported models including GPT-4o mini.」という注釈が削除されました。

この削除により、ファインチューニングのサポートに関する情報が明文化される一方で、文書がより簡潔になりました。この変更は、ユーザーが現在のファインチューニングの機能に関する注意事項を把握しやすくすることを目的としています。なお、他のファインチューニング方法に関する説明や、LoRA（Low-Rank Approximation）の使用法についての情報は残されており、技術的な内容は引き続き提供されています。

## articles/ai-services/openai/how-to/realtime-audio.md{#item-482ba3}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,165 @@
+---
+title: 'How to use the GPT-4o Realtime API for speech and audio with Azure OpenAI Service'
+titleSuffix: Azure OpenAI
+description: Learn how to use the GPT-4o Realtime API for speech and audio with Azure OpenAI Service.
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: how-to
+ms.date: 12/11/2024
+author: eric-urban
+ms.author: eur
+ms.custom: references_regions
+recommendations: false
+---
+
+# How to use the GPT-4o Realtime API for speech and audio (Preview)
+
+[!INCLUDE [Feature preview](../includes/preview-feature.md)]
+
+Azure OpenAI GPT-4o Realtime API for speech and audio is part of the GPT-4o model family that supports low-latency, "speech in, speech out" conversational interactions. The GPT-4o Realtime API is designed to handle real-time, low-latency conversational interactions. Realtime API is a great fit for use cases involving live interactions between a user and a model, such as customer support agents, voice assistants, and real-time translators.
+
+Most users of the Realtime API need to deliver and receive audio from an end-user in real time, including applications that use WebRTC or a telephony system. The Realtime API isn't designed to connect directly to end user devices and relies on client integrations to terminate end user audio streams. 
+
+## Supported models
+
+Currently only `gpt-4o-realtime-preview` version: `2024-10-01-preview` supports real-time audio.
+
+The `gpt-4o-realtime-preview` model is available for global deployments in [East US 2 and Sweden Central regions](../concepts/models.md#global-standard-model-availability).
+
+> [!IMPORTANT]
+> The system stores your prompts and completions as described in the "Data Use and Access for Abuse Monitoring" section of the service-specific Product Terms for Azure OpenAI Service, except that the Limited Exception does not apply. Abuse monitoring will be turned on for use of the `gpt-4o-realtime-preview` API even for customers who otherwise are approved for modified abuse monitoring.
+
+## API support
+
+Support for the Realtime API was first added in API version `2024-10-01-preview`. 
+
+> [!NOTE]
+> For more information about the API and architecture, see the [Azure OpenAI GPT-4o real-time audio repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk).
+
+## Get started
+
+Before you can use GPT-4o real-time audio, you need:
+
+- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
+- An Azure OpenAI resource created in a [supported region](#supported-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](create-resource.md).
+- You need a deployment of the `gpt-4o-realtime-preview` model in a supported region as described in the [supported models](#supported-models) section. You can deploy the model from the [Azure AI Foundry portal model catalog](../../../ai-studio/how-to/model-catalog-overview.md) or from your project in AI Foundry portal. 
+
+For steps to deploy and use the `gpt-4o-realtime-preview` model, see [the real-time audio quickstart](../realtime-audio-quickstart.md).
+
+For more information about the API and architecture, see the remaining sections in this guide.
+
+## Sample code
+
+Right now, the fastest way to get started development with the GPT-4o Realtime API is to download the sample code from the [Azure OpenAI GPT-4o real-time audio repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk).
+
+[The Azure-Samples/aisearch-openai-rag-audio repo](https://github.com/Azure-Samples/aisearch-openai-rag-audio) contains an example of how to implement RAG support in applications that use voice as their user interface, powered by the GPT-4o realtime API for audio.
+
+## Connection and authentication
+
+The Realtime API (via `/realtime`) is built on [the WebSockets API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) to facilitate fully asynchronous streaming communication between the end user and model. 
+
+> [!IMPORTANT]
+> Device details like capturing and rendering audio data are outside the scope of the Realtime API. It should be used in the context of a trusted, intermediate service that manages both connections to end users and model endpoint connections. Don't use it directly from untrusted end user devices.
+
+The Realtime API is accessed via a secure WebSocket connection to the `/realtime` endpoint of your Azure OpenAI resource.
+
+You can construct a full request URI by concatenating:
+
+- The secure WebSocket (`wss://`) protocol
+- Your Azure OpenAI resource endpoint hostname, for example, `my-aoai-resource.openai.azure.com`
+- The `openai/realtime` API path
+- An `api-version` query string parameter for a supported API version such as `2024-10-01-preview`
+- A `deployment` query string parameter with the name of your `gpt-4o-realtime-preview` model deployment
+
+The following example is a well-constructed `/realtime` request URI:
+
+```http
+wss://my-eastus2-openai-resource.openai.azure.com/openai/realtime?api-version=2024-10-01-preview&deployment=gpt-4o-realtime-preview-deployment-name
+```
+
+To authenticate:
+- **Microsoft Entra** (recommended): Use token-based authentication with the `/realtime` API for an Azure OpenAI Service resource with managed identity enabled. Apply a retrieved authentication token using a `Bearer` token with the `Authorization` header.
+- **API key**: An `api-key` can be provided in one of two ways:
+  - Using an `api-key` connection header on the prehandshake connection. This option isn't available in a browser environment.
+  - Using an `api-key` query string parameter on the request URI. Query string parameters are encrypted when using https/wss.
+
+## Realtime API architecture
+
+Once the WebSocket connection session to `/realtime` is established and authenticated, the functional interaction takes place via events for sending and receiving WebSocket messages. These events each take the form of a JSON object. Events can be sent and received in parallel and applications should generally handle them both concurrently and asynchronously.
+
+- A caller establishes a connection to `/realtime`, which starts a new `session`.
+- A `session` automatically creates a default `conversation`. Multiple concurrent conversations aren't supported.
+- The `conversation` accumulates input signals until a `response` is started, either via a direct event by the caller or automatically by voice-activity-based (VAD) turn detection.
+- Each `response` consists of one or more `items`, which can encapsulate messages, function calls, and other information.
+- Each message `item` has `content_part`, allowing multiple modalities (text and audio) to be represented across a single item.
+- The `session` manages configuration of caller input handling (for example, user audio) and common output generation handling.
+- Each caller-initiated `response.create` can override some of the output `response` behavior, if desired.
+- Server-created `item` and the `content_part` in messages can be populated asynchronously and in parallel. For example, receiving audio, text, and function information concurrently in a round robin fashion.
+
+## Session configuration and turn handling mode
+
+Often, the first event sent by the caller on a newly established `/realtime` session is a `session.update` payload. This event controls a wide set of input and output behavior, with output and response generation portions then later overridable via `response.create` properties.
+
+One of the key session-wide settings is `turn_detection`, which controls how data flow is handled between the caller and model:
+
+- `server_vad` evaluates incoming user audio (as sent via `input_audio_buffer.append`) using a voice activity detector (VAD) component and automatically use that audio to initiate response generation on applicable conversations when an end of speech is detected. Silence detection for the VAD can be configured when specifying `server_vad` detection mode.
+- `none` relies on caller-initiated `input_audio_buffer.commit` and `response.create` events to progress conversations and produce output. This setting is useful for push-to-talk applications or situations that have external audio flow control (such as caller-side VAD component). These manual signals can still be used in `server_vad` mode to supplement VAD-initiated response generation.
+
+Transcription of user input audio is opted into via the `input_audio_transcription` property. Specifying a transcription model (`whisper-1`) in this configuration enables the delivery of `conversation.item.audio_transcription.completed` events.
+
+### Session update example
+
+An example `session.update` that configures several aspects of the session, including tools, follows. All session parameters are optional; not everything needs to be configured!
+
+```json
+{
+  "type": "session.update",
+  "session": {
+    "voice": "alloy",
+    "instructions": "Call provided tools if appropriate for the user's input.",
+    "input_audio_format": "pcm16",
+    "input_audio_transcription": {
+      "model": "whisper-1"
+    },
+    "turn_detection": {
+      "threshold": 0.4,
+      "silence_duration_ms": 600,
+      "type": "server_vad"
+    },
+    "tools": [
+      {
+        "type": "function",
+        "name": "get_weather_for_location",
+        "description": "gets the weather for a location",
+        "parameters": {
+          "type": "object",
+          "properties": {
+            "location": {
+              "type": "string",
+              "description": "The city and state e.g. San Francisco, CA"
+            },
+            "unit": {
+              "type": "string",
+              "enum": [
+                "c",
+                "f"
+              ]
+            }
+          },
+          "required": [
+            "location",
+            "unit"
+          ]
+        }
+      }
+    ]
+  }
+}
+```
+
+
+## Related content
+
+* Try the [real-time audio quickstart](../realtime-audio-quickstart.md)
+* See the [Realtime API reference](../realtime-audio-reference.md)
+* Learn more about Azure OpenAI [quotas and limits](../quotas-limits.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIサービスのためのGPT-4oリアルタイムAPIに関する新規ドキュメント"
}
```

### Explanation
この変更は、Azure OpenAIサービスのための新しいドキュメント「GPT-4oリアルタイムAPIの利用方法」が追加されたことを示しています。このドキュメントは、音声およびオーディオに関連する機能を提供するGPT-4oモデルファミリーのリアルタイムAPIの使い方を詳細に説明しています。

具体的には、リアルタイムAPIがどのように低遅延の会話型インタラクションをサポートし、カスタマーサポートや音声アシスタント、リアルタイム翻訳者などのユースケースに適しているかを解説しています。また、サポートされているモデル、APIに関する情報、接続の方法、認証のメカニズム、セッション設定および転送処理の管理方法について詳しく述べています。

この新しいドキュメントは、開発者がAPIを効果的に使用し、リアルタイムのオーディオ処理を行う上での重要なリソースとなることを目的としており、特に新しいAPI機能の理解を深めるために役立つ内容が含まれています。また、サンプルコードや関連ドキュメントへのリンクも併せて提供されており、実際の実装に向けた支援が行われています。

## articles/ai-services/openai/includes/fine-tuning-unified.md{#item-718336}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,12 @@ author: mrbullwinkle
 ms.author: mbullwin
 ---
 
-There are two unique fine-tuning experiences in Azure AI Foundry portal. Both allow you to fine-tune Azure OpenAI models, but only the Hub/Project view supports fine-tuning non Azure OpenAI models. If you are only using the Azure OpenAI fine-tuning experience which is available anytime you select a resource in a region where fine-tuning is supported.
+There are two unique fine-tuning experiences in the Azure AI Foundry portal:
+
+* [Hub/Project view](https://ai.azure.com) - supports fine-tuning models from multiple providers including Azure OpenAI, Meta Llama, Microsoft Phi, etc.
+* [Azure OpenAI centric view](https://oai.azure.com) - only supports fine-tuning Azure OpenAI models, but has support for additional features like the [Weights & Biases (W&B) preview integration](../how-to/weights-and-biases-integration.md). 
+
+If you are only fine-tuning Azure OpenAI models, we recommend the Azure OpenAI centric fine-tuning experience which is available by navigating to [https://oai.azure.com](https://oai.azure.com). 
 
 # [Azure OpenAI](#tab/azure-openai)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニング体験の説明の更新"
}
```

### Explanation
この変更は、Azure AI Foundryポータルにおけるファインチューニング体験に関する説明を改善したものです。具体的には、2つの異なるファインチューニングの方法についての詳細が追加され、それぞれがどのようなモデルをサポートしているかが明確に記されています。

新たに追加された情報は以下の通りです：

- **Hub/Project view**: 複数のプロバイダー（Azure OpenAI、Meta Llama、Microsoft Phiなど）のモデルに対するファインチューニングをサポートしています。
- **Azure OpenAI centric view**: Azure OpenAIモデルのファインチューニングに特化しており、Weights & Biases（W&B）プレビュー統合などの追加機能をサポートしています。

また、Azure OpenAIモデルのみをファインチューニングする場合には、Azure OpenAI centric viewを使用することを推奨しており、そのリンクも提供されています。これにより、ユーザーはより適切なファインチューニング体験を選択するための情報が得られるようになります。

## articles/ai-services/openai/includes/preview-feature.md{#item-564a89}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,10 @@
+---
+title: include file
+description: include file
+ms.topic: include
+ms.date: 12/11/2024
+ms.custom: include
+---
+
+> [!NOTE]
+> This feature is currently in public preview. This preview is provided without a service-level agreement, and we don't recommend it for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "プレビュー機能に関するインクルードファイルの追加"
}
```

### Explanation
この変更は、「プレビュー機能」に関する新しいインクルードファイルを追加したことを示しています。このファイルには、プレビュー機能が現在公共のプレビュー段階にあり、サービスレベル契約なしで提供されること、また、プロダクションワークロードには推奨されない旨の注意が記されています。

具体的には、以下の内容が盛り込まれています：

- プレビュー機能の説明
- プレビュー機能に関する注意喚起、特定の機能がサポートされていない可能性や制約のある機能についての説明
- プレビューに関する利用規約についてのリンク情報

このファイルは、開発者がプレビュー機能を使用する際に留意すべき重要な情報を提供しており、プレビューの現状を理解し適切に利用する手助けとなることを目的としています。

## articles/ai-services/openai/realtime-audio-quickstart.md{#item-727df8}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use GPT-4o Realtime API for speech and audio with Azur
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 10/3/2024
+ms.date: 12/11/2024
 author: eric-urban
 ms.author: eur
 ms.custom: references_regions, ignite-2024
@@ -15,6 +15,8 @@ recommendations: false
 
 # GPT-4o Realtime API for speech and audio (Preview)
 
+[!INCLUDE [Feature preview](includes/preview-feature.md)]
+
 Azure OpenAI GPT-4o Realtime API for speech and audio is part of the GPT-4o model family that supports low-latency, "speech in, speech out" conversational interactions. The GPT-4o audio `realtime` API is designed to handle real-time, low-latency conversational interactions, making it a great fit for use cases involving live interactions between a user and a model, such as customer support agents, voice assistants, and real-time translators.
 
 Most users of the Realtime API need to deliver and receive audio from an end-user in real time, including applications that use WebRTC or a telephony system. The Realtime API isn't designed to connect directly to end user devices and relies on client integrations to terminate end user audio streams. 
@@ -125,5 +127,6 @@ You can run the sample code locally on your machine by following these steps. Re
 
 ## Related content
 
-* Learn more about Azure OpenAI [deployment types](./how-to/deployment-types.md)
+* Learn more about [How to use the Realtime API](./how-to/realtime-audio.md)
+* See the [Realtime API reference](./realtime-audio-reference.md)
 * Learn more about Azure OpenAI [quotas and limits](quotas-limits.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオAPIに関する記事の修正"
}
```

### Explanation
この変更は、Azure OpenAIのリアルタイムオーディオAPIに関するドキュメントを修正し、最新の情報を反映したものです。具体的には、記事の日付が更新され、いくつかの新しい情報が追加されています。

主な変更点は以下の通りです：

1. **日付の更新**: ドキュメントの日付が2024年10月3日から2024年12月11日に変更されました。

2. **プレビュー機能のインクルード**: 「[!INCLUDE [Feature preview](includes/preview-feature.md)]」が追加され、プレビュー機能に関する注意が示されています。

3. **関連コンテンツのリンク**: リアルタイムAPIについての新しいリンクが追加され、ユーザーが関連する情報を簡単に見つけられるように改善されました。
   - 新たに「リアルタイムAPIの使用方法」や「リアルタイムAPIリファレンス」へのリンクが含まれています。

これらの修正により、ユーザーはリアルタイムオーディオAPIの使用に関する最新情報を得やすくなり、特にプレビュー機能の利用に際して留意すべき事項を理解しやすくなります。

## articles/ai-services/openai/realtime-audio-reference.md{#item-276d51}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,1487 @@
+---
+title: Azure OpenAI Service Realtime API Reference
+titleSuffix: Azure OpenAI
+description: Learn how to use the Realtime API to interact with the Azure OpenAI service in real-time.
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: conceptual
+ms.date: 12/12/2024
+author: eric-urban
+ms.author: eur
+recommendations: false
+---
+
+# Realtime API (Preview) reference
+
+[!INCLUDE [Feature preview](includes/preview-feature.md)]
+
+The Realtime API is a WebSocket-based API that allows you to interact with the Azure OpenAI service in real-time. 
+
+The Realtime API (via `/realtime`) is built on [the WebSockets API](https://developer.mozilla.org/docs/Web/API/WebSockets_API) to facilitate fully asynchronous streaming communication between the end user and model. Device details like capturing and rendering audio data are outside the scope of the Realtime API. It should be used in the context of a trusted, intermediate service that manages both connections to end users and model endpoint connections. Don't use it directly from untrusted end user devices.
+
+> [!TIP]
+> To get started with the Realtime API, see the [quickstart](realtime-audio-quickstart.md) and [how-to guide](./how-to/realtime-audio.md).
+
+## Connection
+
+The Realtime API requires an existing Azure OpenAI resource endpoint in a supported region. The API is accessed via a secure WebSocket connection to the `/realtime` endpoint of your Azure OpenAI resource.
+
+You can construct a full request URI by concatenating:
+
+- The secure WebSocket (`wss://`) protocol
+- Your Azure OpenAI resource endpoint hostname, for example, `my-aoai-resource.openai.azure.com`
+- The `openai/realtime` API path
+- An `api-version` query string parameter for a supported API version such as `2024-10-01-preview`
+- A `deployment` query string parameter with the name of your `gpt-4o-realtime-preview` model deployment
+
+The following example is a well-constructed `/realtime` request URI:
+
+```http
+wss://my-eastus2-openai-resource.openai.azure.com/openai/realtime?api-version=2024-10-01-preview&deployment=gpt-4o-realtime-preview-1001
+```
+
+## Authentication
+
+To authenticate:
+- **Microsoft Entra** (recommended): Use token-based authentication with the `/realtime` API for an Azure OpenAI Service resource with managed identity enabled. Apply a retrieved authentication token using a `Bearer` token with the `Authorization` header.
+- **API key**: An `api-key` can be provided in one of two ways:
+  - Using an `api-key` connection header on the prehandshake connection. This option isn't available in a browser environment.
+  - Using an `api-key` query string parameter on the request URI. Query string parameters are encrypted when using https/wss.
+
+## Client events
+
+There are nine client events that can be sent from the client to the server:
+
+| Event | Description |
+|-------|-------------|
+| [RealtimeClientEventConversationItemCreate](#realtimeclienteventconversationitemcreate) | Send this client event when adding an item to the conversation. |
+| [RealtimeClientEventConversationItemDelete](#realtimeclienteventconversationitemdelete) | Send this client event when you want to remove any item from the conversation history. |
+| [RealtimeClientEventConversationItemTruncate](#realtimeclienteventconversationitemtruncate) | Send this client event when you want to truncate a previous assistant message's audio. |
+| [RealtimeClientEventInputAudioBufferAppend](#realtimeclienteventinputaudiobufferappend) | Send this client event to append audio bytes to the input audio buffer. |
+| [RealtimeClientEventInputAudioBufferClear](#realtimeclienteventinputaudiobufferclear) | Send this client event to clear the audio bytes in the buffer. |
+| [RealtimeClientEventInputAudioBufferCommit](#realtimeclienteventinputaudiobuffercommit) | Send this client event to commit audio bytes to a user message. |
+| [RealtimeClientEventResponseCancel](#realtimeclienteventresponsecancel) | Send this client event to cancel an in-progress response. |
+| [RealtimeClientEventResponseCreate](#realtimeclienteventresponsecreate) | Send this client event to trigger a response generation. |
+| [RealtimeClientEventSessionUpdate](#realtimeclienteventsessionupdate) | Send this client event to update the session's default configuration. |
+
+### RealtimeClientEventConversationItemCreate
+
+Add a new item to the conversation's context, including messages, function calls, and function call responses. This event can be used to populate a history of the conversation and to add new items mid-stream. Currently this event can't populate assistant audio messages.
+
+If successful, the server responds with a `conversation.item.created` event, otherwise an `error` event is sent.
+
+#### Event structure
+
+```json
+{
+  "type": "conversation.item.create",
+  "previous_item_id": "<previous_item_id>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `conversation.item.create`. | **Required**<br>Allowed values: `conversation.item.create` |
+| previous_item_id | string | The ID of the preceding item after which the new item is inserted. If not set, the new item is appended to the end of the conversation. If set, it allows an item to be inserted mid-conversation. If the ID can't be found, then an error is returned and the item isn't added. |  |
+| item | [RealtimeConversationRequestItem](#realtimeconversationrequestitem) |  | **Required** |
+
+### RealtimeClientEventConversationItemDelete
+
+Send this client event when you want to remove any item from the conversation history. The server responds with a `conversation.item.deleted` event, unless the item doesn't exist in the conversation history, in which case the server responds with an error.
+
+#### Event structure
+
+```json
+{
+  "type": "conversation.item.delete",
+  "item_id": "<item_id>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `conversation.item.delete`. | **Required**<br>Allowed values: `conversation.item.delete` |
+| item_id | string | The ID of the item to delete. | **Required** |
+
+### RealtimeClientEventConversationItemTruncate
+
+Send this client event to truncate a previous assistant message's audio. The server produces audio faster than realtime, so this event is useful when the user interrupts to truncate audio that was sent to the client but not yet played. The server's understanding of the audio with the client's playback is synchronized.
+
+Truncating audio deletes the server-side text transcript to ensure there isn't text in the context that the user doesn't know about.
+
+If successful, the server responds with a `conversation.item.truncated` event.
+
+#### Event structure
+
+```json
+{
+  "type": "conversation.item.truncate",
+  "item_id": "<item_id>",
+  "content_index": 0,
+  "audio_end_ms": 0
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `conversation.item.truncate`. | **Required**<br>Allowed values: `conversation.item.truncate` |
+| item_id | string | The ID of the assistant message item to truncate. Only assistant message items can be truncated. | **Required** |
+| content_index | integer | The index of the content part to truncate. Set this property to "0". | **Required** |
+| audio_end_ms | integer | Inclusive duration up to which audio is truncated, in milliseconds. If the audio_end_ms is greater than the actual audio duration, the server responds with an error. | **Required** |
+
+### RealtimeClientEventInputAudioBufferAppend
+
+Send this client event to append audio bytes to the input audio buffer. The audio buffer is temporary storage you can write to and later commit. In Server VAD (Voice Activity Detection) mode, the audio buffer is used to detect speech and the server decides when to commit. When Server VAD is disabled, you must commit the audio buffer manually.
+
+The client can choose how much audio to place in each event up to a maximum of 15 MiB, for example streaming smaller chunks from the client can allow the VAD to be more responsive. Unlike made other client events, the server doesn't send a confirmation response to this event.
+
+#### Event structure
+
+```json
+{
+  "type": "input_audio_buffer.append",
+  "audio": "<audio>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `input_audio_buffer.append`. | **Required**<br>Allowed values: `input_audio_buffer.append` |
+| audio | string | Base64-encoded audio bytes. This value must be in the format specified by the `input_audio_format` field in the session configuration. | **Required** |
+
+### RealtimeClientEventInputAudioBufferClear
+
+Send this client event to clear the audio bytes in the buffer. The server responds with an `input_audio_buffer.cleared` event.
+
+#### Event structure
+
+```json
+{
+  "type": "input_audio_buffer.clear"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `input_audio_buffer.clear`. | **Required**<br>Allowed values: `input_audio_buffer.clear` |
+
+### RealtimeClientEventInputAudioBufferCommit
+
+Send this client event to commit the user input audio buffer, which creates a new user message item in the conversation. This event produces an error if the input audio buffer is empty. When in server VAD mode, the client doesn't need to send this event, the server commits the audio buffer automatically.
+
+Committing the input audio buffer triggers input audio transcription (if enabled in session configuration), but it doesn't create a response from the model. The server responds with an `input_audio_buffer.committed` event.
+
+#### Event structure
+
+```json
+{
+  "type": "input_audio_buffer.commit"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `input_audio_buffer.commit`. | **Required**<br>Allowed values: `input_audio_buffer.commit` |
+
+### RealtimeClientEventResponseCancel
+
+Send this client event to cancel an in-progress response. The server responds with a `response.cancelled` event or an error if there's no response to cancel.
+
+#### Event structure
+
+```json
+{
+  "type": "response.cancel"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.cancel`. | **Required**<br>Allowed values: `response.cancel` |
+
+### RealtimeClientEventResponseCreate
+
+This event instructs the server to create a response, which means triggering model inference. When in server VAD mode, the server creates responses automatically.
+
+A response includes at least one item, and can have two, in which case the second is a function call. These items are appended to the conversation history.
+
+The server responds with a `response.created` event, events for items and content created, and finally a `response.done` event to indicate the response is complete.
+
+The `response.create` event includes inference configuration like 
+`instructions`, and `temperature`. These fields override the session's configuration for this response only.
+
+#### Event structure
+
+```json
+{
+  "type": "response.create"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.create`. | **Required**<br>Allowed values: `response.create` |
+| response | [RealtimeResponseOptions](#realtimeresponseoptions) |  | **Required** |
+
+### RealtimeClientEventSessionUpdate
+
+Send this client event to update the session's default configuration. The client can send this event at any time to update the session configuration, and any field can be updated at any time, except for voice. The server responds with a `session.updated` event that shows the full effective configuration. 
+
+Only fields that are present are updated, thus the correct way to clear a field like "instructions" is to pass an empty string.
+
+#### Event structure
+
+```json
+{
+  "type": "session.update"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `session.update`. | **Required**<br>Allowed values: `session.update` |
+| session | [RealtimeRequestSession](#realtimerequestsession) |  | **Required** |
+
+## Server events
+
+There are 28 server events that can be received from the server:
+
+| Event | Description |
+|-------|-------------|
+| [RealtimeServerEventConversationCreated](#realtimeservereventconversationcreated) | Server event when a conversation is created. Emitted right after session creation. |
+| [RealtimeServerEventConversationItemCreated](#realtimeservereventconversationitemcreated) | Server event when a conversation item is created. |
+| [RealtimeServerEventConversationItemDeleted](#realtimeservereventconversationitemdeleted) | Server event when an item in the conversation is deleted. |
+| [RealtimeServerEventConversationItemInputAudioTranscriptionCompleted](#realtimeservereventconversationiteminputaudiotranscriptioncompleted) | Server event when input audio transcription is enabled and a transcription succeeds. |
+| [RealtimeServerEventConversationItemInputAudioTranscriptionFailed](#realtimeservereventconversationiteminputaudiotranscriptionfailed) | Server event when input audio transcription is configured, and a transcription request for a user message failed. |
+| [RealtimeServerEventConversationItemTruncated](#realtimeservereventconversationitemtruncated) | Server event when the client truncates an earlier assistant audio message item. |
+| [RealtimeServerEventError](#realtimeservereventerror) | Server event when an error occurs. |
+| [RealtimeServerEventInputAudioBufferCleared](#realtimeservereventinputaudiobuffercleared) | Server event when the client clears the input audio buffer. |
+| [RealtimeServerEventInputAudioBufferCommitted](#realtimeservereventinputaudiobuffercommitted) | Server event when an input audio buffer is committed, either by the client or automatically in server VAD mode. |
+| [RealtimeServerEventInputAudioBufferSpeechStarted](#realtimeservereventinputaudiobufferspeechstarted) | Server event in server turn detection mode when speech is detected. |
+| [RealtimeServerEventInputAudioBufferSpeechStopped](#realtimeservereventinputaudiobufferspeechstopped) | Server event in server turn detection mode when speech stops. |
+| [RealtimeServerEventRateLimitsUpdated](#realtimeservereventratelimitsupdated) | Emitted after every "response.done" event to indicate the updated rate limits. |
+| [RealtimeServerEventResponseAudioDelta](#realtimeservereventresponseaudiodelta) | Server event when the model-generated audio is updated. |
+| [RealtimeServerEventResponseAudioDone](#realtimeservereventresponseaudiodone) | Server event when the model-generated audio is done. Also emitted when a response is interrupted, incomplete, or cancelled. |
+| [RealtimeServerEventResponseAudioTranscriptDelta](#realtimeservereventresponseaudiotranscriptdelta) | Server event when the model-generated transcription of audio output is updated. |
+| [RealtimeServerEventResponseAudioTranscriptDone](#realtimeservereventresponseaudiotranscriptdone) | Server event when the model-generated transcription of audio output is done streaming. Also emitted when a response is interrupted, incomplete, or cancelled. |
+| [RealtimeServerEventResponseContentPartAdded](#realtimeservereventresponsecontentpartadded) | Server event when a new content part is added to an assistant message item during response generation. |
+| [RealtimeServerEventResponseContentPartDone](#realtimeservereventresponsecontentpartdone) | Server event when a content part is done streaming in an assistant message item. Also emitted when a response is interrupted, incomplete, or cancelled. |
+| [RealtimeServerEventResponseCreated](#realtimeservereventresponsecreated) | Server event when a new Response is created. The first event of response creation, where the response is in an initial state of "in_progress". |
+| [RealtimeServerEventResponseDone](#realtimeservereventresponsedone) | Server event when a response is done streaming. Always emitted, no matter the final state. |
+| [RealtimeServerEventResponseFunctionCallArgumentsDelta](#realtimeservereventresponsefunctioncallargumentsdelta) | Server event when the model-generated function call arguments are updated. |
+| [RealtimeServerEventResponseFunctionCallArgumentsDone](#realtimeservereventresponsefunctioncallargumentsdone) | Server event when the model-generated function call arguments are done streaming. Also emitted when a response is interrupted, incomplete, or cancelled. |
+| [RealtimeServerEventResponseOutputItemAdded](#realtimeservereventresponseoutputitemadded) | Server event when a new output item is added to a response. |
+| [RealtimeServerEventResponseOutputItemDone](#realtimeservereventresponseoutputitemdone) | Server event when an output item is done streaming. Also emitted when a response is interrupted, incomplete, or cancelled. |
+| [RealtimeServerEventResponseTextDelta](#realtimeservereventresponsetextdelta) | Server event when the model-generated text is updated. |
+| [RealtimeServerEventResponseTextDone](#realtimeservereventresponsetextdone) | Server event when the model-generated text is done. Also emitted when a response is interrupted, incomplete, or cancelled. |
+| [RealtimeServerEventSessionCreated](#realtimeservereventsessioncreated) | Server event when a session is created. |
+| [RealtimeServerEventSessionUpdated](#realtimeservereventsessionupdated) | Server event when a session is updated. |
+
+### RealtimeServerEventConversationCreated
+
+Server event when a conversation is created. Emitted right after session creation.
+
+#### Event structure
+
+```json
+{
+  "type": "conversation.created",
+  "conversation": {
+    "id": "<id>",
+    "object": "<object>"
+  }
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `conversation.created`. | **Required**<br>Allowed values: `conversation.created` |
+| conversation | object | The conversation resource. | **Required**<br>See nested properties next.|
+
+#### Conversation properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| id | string | The unique ID of the conversation. |  |
+| object | string | The object type must be `realtime.conversation`. |  |
+
+### RealtimeServerEventConversationItemCreated
+
+Server event when a conversation item is created. There are several scenarios that produce this event:
+  - The server is generating a response, which if successful produces either one or two items, which is of type `message` (role `assistant`) or type `function_call`.
+  - The input audio buffer is committed, either by the client or the server (in `server_vad` mode). The server takes the content of the input audio buffer and adds it to a new user message item.
+  - The client sent a `conversation.item.create` event to add a new item to the conversation.
+
+#### Event structure
+
+```json
+{
+  "type": "conversation.item.created",
+  "previous_item_id": "<previous_item_id>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `conversation.item.created`. | **Required**<br>Allowed values: `conversation.item.created` |
+| previous_item_id | string | The ID of the preceding item in the conversation context, allows the client to understand the order of the conversation. | **Required** |
+| item | [RealtimeConversationResponseItem](#realtimeconversationresponseitem) |  | **Required** |
+
+### RealtimeServerEventConversationItemDeleted
+
+Server event when the client deleted an item in the conversation with a `conversation.item.delete` event. This event is used to synchronize the server's understanding of the conversation history with the client's view.
+
+#### Event structure
+
+```json
+{
+  "type": "conversation.item.deleted",
+  "item_id": "<item_id>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `conversation.item.deleted`. | **Required**<br>Allowed values: `conversation.item.deleted` |
+| item_id | string | The ID of the item that was deleted. | **Required** |
+
+### RealtimeServerEventConversationItemInputAudioTranscriptionCompleted
+
+This server event is the output of audio transcription for user audio written to the user audio buffer. Transcription begins when the input audio buffer is committed by the client or server (in `server_vad` mode). Transcription runs asynchronously with response creation, so this event can come before or after the response events.
+
+Realtime API models accept audio natively, and thus input transcription is a separate process run on a separate Automatic Speech Recognition (ASR) model, currently always `whisper-1`. Thus the transcript can diverge somewhat from the model's interpretation, and should be treated as a rough guide.
+
+#### Event structure
+
+```json
+{
+  "type": "conversation.item.input_audio_transcription.completed",
+  "item_id": "<item_id>",
+  "content_index": 0,
+  "transcript": "<transcript>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `conversation.item.input_audio_transcription.completed`. | **Required**<br>Allowed values: `conversation.item.input_audio_transcription.completed` |
+| item_id | string | The ID of the user message item containing the audio. | **Required** |
+| content_index | integer | The index of the content part containing the audio. | **Required** |
+| transcript | string | The transcribed text. | **Required** |
+
+### RealtimeServerEventConversationItemInputAudioTranscriptionFailed
+
+Server event when input audio transcription is configured, and a transcription request for a user message failed. These events are separate from other `error` events so that the client can identify the related item.
+
+#### Event structure
+
+```json
+{
+  "type": "conversation.item.input_audio_transcription.failed",
+  "item_id": "<item_id>",
+  "content_index": 0,
+  "error": {
+    "code": "<code>",
+    "message": "<message>",
+    "param": "<param>"
+  }
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `conversation.item.input_audio_transcription.failed`. | **Required**<br>Allowed values: `conversation.item.input_audio_transcription.failed` |
+| item_id | string | The ID of the user message item. | **Required** |
+| content_index | integer | The index of the content part containing the audio. | **Required** |
+| error | object | Details of the transcription error. | **Required**<br>See nested properties next.|
+
+#### Error properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The type of error. |  |
+| code | string | Error code, if any. |  |
+| message | string | A human-readable error message. |  |
+| param | string | Parameter related to the error, if any. |  |
+
+### RealtimeServerEventConversationItemTruncated
+
+Server event when the client truncates an earlier assistant audio message item with a `conversation.item.truncate` event. This event is used to synchronize the server's understanding of the audio with the client's playback.
+
+This action truncates the audio and removes the server-side text transcript to ensure there's no text in the context that the user doesn't know about.
+
+#### Event structure
+
+```json
+{
+  "type": "conversation.item.truncated",
+  "item_id": "<item_id>",
+  "content_index": 0,
+  "audio_end_ms": 0
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `conversation.item.truncated`. | **Required**<br>Allowed values: `conversation.item.truncated` |
+| item_id | string | The ID of the assistant message item that was truncated. | **Required** |
+| content_index | integer | The index of the content part that was truncated. | **Required** |
+| audio_end_ms | integer | The duration up to which the audio was truncated, in milliseconds. | **Required** |
+
+### RealtimeServerEventError
+
+Server event when an error occurs, which could be a client problem or a server problem. Most errors are recoverable and the session stays open. 
+
+#### Event structure
+
+```json
+{
+  "type": "error",
+  "error": {
+    "code": "<code>",
+    "message": "<message>",
+    "param": "<param>",
+    "event_id": "<event_id>"
+  }
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `error`. | **Required**<br>Allowed values: `error` |
+| error | object | Details of the error. | **Required**<br>See nested properties next.|
+
+#### Error properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The type of error (for example, "invalid_request_error", "server_error"). |  |
+| code | string | Error code, if any. |  |
+| message | string | A human-readable error message. |  |
+| param | string | Parameter related to the error, if any. |  |
+| event_id | string | The ID of the client event that caused the error, if applicable. |  |
+
+### RealtimeServerEventInputAudioBufferCleared
+
+Server event when the client clears the input audio buffer with a `input_audio_buffer.clear` event.
+
+#### Event structure
+
+```json
+{
+  "type": "input_audio_buffer.cleared"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `input_audio_buffer.cleared`. | **Required**<br>Allowed values: `input_audio_buffer.cleared` |
+
+### RealtimeServerEventInputAudioBufferCommitted
+
+Server event when an input audio buffer is committed, either by the client or automatically in server VAD mode. The `item_id` property is the ID of the user message item created. Thus a `conversation.item.created` event is also sent to the client.
+
+#### Event structure
+
+```json
+{
+  "type": "input_audio_buffer.committed",
+  "previous_item_id": "<previous_item_id>",
+  "item_id": "<item_id>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `input_audio_buffer.committed`. | **Required**<br>Allowed values: `input_audio_buffer.committed` |
+| previous_item_id | string | The ID of the preceding item after which the new item is inserted. | **Required** |
+| item_id | string | The ID of the user message item created. | **Required** |
+
+### RealtimeServerEventInputAudioBufferSpeechStarted
+
+Server event when in `server_vad` mode to indicate that speech is detected in the audio buffer. This event can happen any time audio is added to the buffer (unless speech is already detected). The client can want to use this event to interrupt audio playback or provide visual feedback to the user. 
+
+The client should expect to receive a `input_audio_buffer.speech_stopped` event when speech stops. The `item_id` property is the ID of the user message item created when speech stops and is also included in the `input_audio_buffer.speech_stopped` event (unless the client manually commits the audio buffer during VAD activation).
+
+#### Event structure
+
+```json
+{
+  "type": "input_audio_buffer.speech_started",
+  "audio_start_ms": 0,
+  "item_id": "<item_id>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `input_audio_buffer.speech_started`. | **Required**<br>Allowed values: `input_audio_buffer.speech_started` |
+| audio_start_ms | integer | Milliseconds from the start of all audio written to the buffer during the session when speech was first detected. This property corresponds to the beginning of audio sent to the model, and thus includes the `prefix_padding_ms` configured in the session. | **Required** |
+| item_id | string | The ID of the user message item created when speech stops. | **Required** | 
+
+### RealtimeServerEventInputAudioBufferSpeechStopped
+
+Server event in `server_vad` mode when the server detects the end of speech in 
+the audio buffer. The server also sends an `conversation.item.created` 
+event with the user message item created from the audio buffer.
+
+#### Event structure
+
+```json
+{
+  "type": "input_audio_buffer.speech_stopped",
+  "audio_end_ms": 0,
+  "item_id": "<item_id>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `input_audio_buffer.speech_stopped`. | **Required**<br>Allowed values: `input_audio_buffer.speech_stopped` |
+| audio_end_ms | integer | Milliseconds since the session started when speech stopped. This property corresponds to the end of audio sent to the model, and thus includes the `min_silence_duration_ms` configured in the session. | **Required** |
+| item_id | string | The ID of the user message item created. | **Required** |
+
+### RealtimeServerEventRateLimitsUpdated
+
+Server event emitted at the beginning of a response to indicate the updated rate limits. 
+
+When a response is created some tokens are "reserved" for the output tokens, the rate limits shown here reflect that reservation, which is then adjusted accordingly once the response is completed.
+
+#### Event structure
+
+```json
+{
+  "type": "rate_limits.updated"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `rate_limits.updated`. | **Required**<br>Allowed values: `rate_limits.updated` |
+| rate_limits | array | List of rate limit information. | **Required**<br>Array items: [RealtimeServerEventRateLimitsUpdatedRateLimitsItem](#realtimeservereventratelimitsupdatedratelimitsitem) |
+
+### RealtimeServerEventRateLimitsUpdatedRateLimitsItem
+
+#### Event structure
+
+```json
+{
+  "name": "<name>",
+  "limit": 0,
+  "remaining": 0
+}
+```
+
+#### Properties
+
+| Field | Type | Description | 
+|------|------|-------------| 
+| name | string | The rate limit property name that this item includes information about. | 
+| limit | integer | The maximum configured limit for this rate limit property. | 
+| remaining | integer | The remaining quota available against the configured limit for this rate limit property. | 
+| reset_seconds | number | The remaining time, in seconds, until this rate limit property is reset. | 
+
+### RealtimeServerEventResponseAudioDelta
+
+Returned when the model-generated audio is updated.
+
+#### Event structure
+
+```json
+{
+  "type": "response.audio.delta",
+  "response_id": "<response_id>",
+  "item_id": "<item_id>",
+  "output_index": 0,
+  "content_index": 0,
+  "delta": "<delta>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.audio.delta`. | **Required**<br>Allowed values: `response.audio.delta` |
+| response_id | string | The ID of the response. | **Required** |
+| item_id | string | The ID of the item. | **Required** |
+| output_index | integer | The index of the output item in the response. | **Required** |
+| content_index | integer | The index of the content part in the item's content array. | **Required** |
+| delta | string | Base64-encoded audio data delta. | **Required** |
+
+### RealtimeServerEventResponseAudioDone
+
+Server event when the model-generated audio is done. Also emitted when a response is interrupted, incomplete, or cancelled.
+
+#### Event structure
+
+```json
+{
+  "type": "response.audio.done",
+  "response_id": "<response_id>",
+  "item_id": "<item_id>",
+  "output_index": 0,
+  "content_index": 0
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.audio.done`. | **Required**<br>Allowed values: `response.audio.done` |
+| response_id | string | The ID of the response. | **Required** |
+| item_id | string | The ID of the item. | **Required** |
+| output_index | integer | The index of the output item in the response. | **Required** |
+| content_index | integer | The index of the content part in the item's content array. | **Required** |
+
+### RealtimeServerEventResponseAudioTranscriptDelta
+
+Server event when the model-generated transcription of audio output is updated.
+
+#### Event structure
+
+```json
+{
+  "type": "response.audio_transcript.delta",
+  "response_id": "<response_id>",
+  "item_id": "<item_id>",
+  "output_index": 0,
+  "content_index": 0,
+  "delta": "<delta>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.audio_transcript.delta`. | **Required**<br>Allowed values: `response.audio_transcript.delta` |
+| response_id | string | The ID of the response. | **Required** |
+| item_id | string | The ID of the item. | **Required** |
+| output_index | integer | The index of the output item in the response. | **Required** |
+| content_index | integer | The index of the content part in the item's content array. | **Required** |
+| delta | string | The transcript delta. | **Required** |
+
+### RealtimeServerEventResponseAudioTranscriptDone
+
+Server event when the model-generated transcription of audio output is done streaming. Also emitted when a response is interrupted, incomplete, or cancelled.
+
+#### Event structure
+
+```json
+{
+  "type": "response.audio_transcript.done",
+  "response_id": "<response_id>",
+  "item_id": "<item_id>",
+  "output_index": 0,
+  "content_index": 0,
+  "transcript": "<transcript>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.audio_transcript.done`. | **Required**<br>Allowed values: `response.audio_transcript.done` |
+| response_id | string | The ID of the response. | **Required** |
+| item_id | string | The ID of the item. | **Required** |
+| output_index | integer | The index of the output item in the response. | **Required** |
+| content_index | integer | The index of the content part in the item's content array. | **Required** |
+| transcript | string | The final transcript of the audio. | **Required** |
+
+### RealtimeServerEventResponseContentPartAdded
+
+Server event when a new content part is added to an assistant message item during response generation.
+
+#### Event structure
+
+```json
+{
+  "type": "response.content_part.added",
+  "response_id": "<response_id>",
+  "item_id": "<item_id>",
+  "output_index": 0,
+  "content_index": 0
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.content_part.added`. | **Required**<br>Allowed values: `response.content_part.added` |
+| response_id | string | The ID of the response. | **Required** |
+| item_id | string | The ID of the item to which the content part was added. | **Required** |
+| output_index | integer | The index of the output item in the response. | **Required** |
+| content_index | integer | The index of the content part in the item's content array. | **Required** |
+| part | [RealtimeContentPart](#realtimecontentpart) | The content part that was added. | **Required** |
+
+#### Part properties
+
+| Field | Type | Description | 
+|------|------|-------------| 
+| type | [RealtimeContentPartType](#realtimecontentparttype) |  | 
+
+### RealtimeServerEventResponseContentPartDone
+
+Server event when a content part is done streaming in an assistant message item. Also emitted when a response is interrupted, incomplete, or cancelled.
+
+#### Event structure
+
+```json
+{
+  "type": "response.content_part.done",
+  "response_id": "<response_id>",
+  "item_id": "<item_id>",
+  "output_index": 0,
+  "content_index": 0
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.content_part.done`. | **Required**<br>Allowed values: `response.content_part.done` |
+| response_id | string | The ID of the response. | **Required** |
+| item_id | string | The ID of the item. | **Required** |
+| output_index | integer | The index of the output item in the response. | **Required** |
+| content_index | integer | The index of the content part in the item's content array. | **Required** |
+| part | [RealtimeContentPart](#realtimecontentpart) | The content part that is done. | **Required** | 
+
+#### Part properties
+
+| Field | Type | Description | 
+|------|------|-------------| 
+| type | [RealtimeContentPartType](#realtimecontentparttype) |  | 
+
+### RealtimeServerEventResponseCreated
+
+Server event when a new response is created. The first event of response creation,where  the response is in an initial state of `in_progress`.
+
+#### Event structure
+
+```json
+{
+  "type": "response.created"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.created`. | **Required**<br>Allowed values: `response.created` |
+| response | [RealtimeResponse](#realtimeresponse) |  | **Required** |
+
+### RealtimeServerEventResponseDone
+
+Server event when a response is done streaming. Always emitted, no matter the final state. The response object included in the `response.done` event includes all output items in the response but omits the raw audio data.
+
+#### Event structure
+
+```json
+{
+  "type": "response.done"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.done`. | **Required**<br>Allowed values: `response.done` |
+| response | [RealtimeResponse](#realtimeresponse) |  | **Required** |
+
+### RealtimeServerEventResponseFunctionCallArgumentsDelta
+
+Server event when the model-generated function call arguments are updated.
+
+#### Event structure
+
+```json
+{
+  "type": "response.function_call_arguments.delta",
+  "response_id": "<response_id>",
+  "item_id": "<item_id>",
+  "output_index": 0,
+  "call_id": "<call_id>",
+  "delta": "<delta>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.function_call_arguments.delta`. | **Required**<br>Allowed values: `response.function_call_arguments.delta` |
+| response_id | string | The ID of the response. | **Required** |
+| item_id | string | The ID of the function call item. | **Required** |
+| output_index | integer | The index of the output item in the response. | **Required** |
+| call_id | string | The ID of the function call. | **Required** |
+| delta | string | The arguments delta as a JSON string. | **Required** |
+
+### RealtimeServerEventResponseFunctionCallArgumentsDone
+
+Server event when the model-generated function call arguments are done streaming.
+
+Also emitted when a response is interrupted, incomplete, or cancelled.
+
+#### Event structure
+
+```json
+{
+  "type": "response.function_call_arguments.done",
+  "response_id": "<response_id>",
+  "item_id": "<item_id>",
+  "output_index": 0,
+  "call_id": "<call_id>",
+  "arguments": "<arguments>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.function_call_arguments.done`. | **Required**<br>Allowed values: `response.function_call_arguments.done` |
+| response_id | string | The ID of the response. | **Required** |
+| item_id | string | The ID of the function call item. | **Required** |
+| output_index | integer | The index of the output item in the response. | **Required** |
+| call_id | string | The ID of the function call. | **Required** |
+| arguments | string | The final arguments as a JSON string. | **Required** |
+
+### RealtimeServerEventResponseOutputItemAdded
+
+Server event when a new item is created during response generation.
+
+#### Event structure
+
+```json
+{
+  "type": "response.output_item.added",
+  "response_id": "<response_id>",
+  "output_index": 0
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.output_item.added`. | **Required**<br>Allowed values: `response.output_item.added` |
+| response_id | string | The ID of the response to which the item belongs. | **Required** |
+| output_index | integer | The index of the output item in the response. | **Required** |
+| item | [RealtimeConversationResponseItem](#realtimeconversationresponseitem) |  | **Required** | 
+
+### RealtimeServerEventResponseOutputItemDone
+
+Server event when an item is done streaming. Also emitted when a response is interrupted, incomplete, or cancelled.
+
+#### Event structure
+
+```json
+{
+  "type": "response.output_item.done",
+  "response_id": "<response_id>",
+  "output_index": 0
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.output_item.done`. | **Required**<br>Allowed values: `response.output_item.done` |
+| response_id | string | The ID of the response to which the item belongs. | **Required** |
+| output_index | integer | The index of the output item in the response. | **Required** |
+| item | [RealtimeConversationResponseItem](#realtimeconversationresponseitem) |  | **Required** |
+
+### RealtimeServerEventResponseTextDelta
+
+Server event event when the text value of a "text" content part is updated.
+
+#### Event structure
+
+```json
+{
+  "type": "response.text.delta",
+  "response_id": "<response_id>",
+  "item_id": "<item_id>",
+  "output_index": 0,
+  "content_index": 0,
+  "delta": "<delta>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.text.delta`. | **Required**<br>Allowed values: `response.text.delta` |
+| response_id | string | The ID of the response. | **Required** |
+| item_id | string | The ID of the item. | **Required** |
+| output_index | integer | The index of the output item in the response. | **Required** |
+| content_index | integer | The index of the content part in the item's content array. | **Required** |
+| delta | string | The text delta. | **Required** |
+
+### RealtimeServerEventResponseTextDone
+
+Server event when the text value of a "text" content part is done streaming. Also
+emitted when a response is interrupted, incomplete, or cancelled.
+
+#### Event structure
+
+```json
+{
+  "type": "response.text.done",
+  "response_id": "<response_id>",
+  "item_id": "<item_id>",
+  "output_index": 0,
+  "content_index": 0,
+  "text": "<text>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `response.text.done`. | **Required**<br>Allowed values: `response.text.done` |
+| response_id | string | The ID of the response. | **Required** |
+| item_id | string | The ID of the item. | **Required** |
+| output_index | integer | The index of the output item in the response. | **Required** |
+| content_index | integer | The index of the content part in the item's content array. | **Required** |
+| text | string | The final text content. | **Required** |
+
+### RealtimeServerEventSessionCreated
+
+Server event when a session is created. Emitted automatically when a new 
+connection is established as the first server event. This event contains 
+the default session configuration.
+
+#### Event structure
+
+```json
+{
+  "type": "session.created"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `session.created`. | **Required**<br>Allowed values: `session.created` |
+| session | [RealtimeResponseSession](#realtimeresponsesession) |  | **Required** |
+
+### RealtimeServerEventSessionUpdated
+
+Server event when a session is updated with a `session.update` event, unless 
+there's an error.
+
+#### Event structure
+
+```json
+{
+  "type": "session.updated"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string | The event type must be `session.updated`. | **Required**<br>Allowed values: `session.updated` |
+| session | [RealtimeResponseSession](#realtimeresponsesession) |  | **Required** |
+
+## Components
+
+### RealtimeAudioFormat
+
+**Allowed Values:**
+
+* `pcm16` 
+* `g711_ulaw` 
+* `g711_alaw` 
+
+### RealtimeAudioInputTranscriptionModel
+
+**Allowed Values:**
+
+* `whisper-1` 
+
+### RealtimeAudioInputTranscriptionSettings
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| model | [RealtimeAudioInputTranscriptionModel](#realtimeaudioinputtranscriptionmodel) |  | Default: `whisper-1` |
+
+
+### RealtimeClientEvent
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | [RealtimeClientEventType](#realtimeclienteventtype) |  | **Required** |
+| event_id | string |  |  |
+
+### RealtimeClientEventType
+
+**Allowed Values:**
+
+* `session.update` 
+* `input_audio_buffer.append` 
+* `input_audio_buffer.commit` 
+* `input_audio_buffer.clear` 
+* `conversation.item.create` 
+* `conversation.item.delete` 
+* `conversation.item.truncate` 
+* `response.create` 
+* `response.cancel` 
+
+### RealtimeContentPart
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | [RealtimeContentPartType](#realtimecontentparttype) |  | **Required** |
+
+### RealtimeContentPartType
+
+**Allowed Values:**
+
+* `input_text` 
+* `input_audio` 
+* `text` 
+* `audio` 
+
+### RealtimeConversationItemBase
+
+The item to add to the conversation.
+
+### RealtimeConversationRequestItem
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | [RealtimeItemType](#realtimeitemtype) |  | **Required** |
+| id | string |  |  |
+
+### RealtimeConversationResponseItem
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| object | string |  | **Required**<br>Allowed values: `realtime.item` |
+| type | [RealtimeItemType](#realtimeitemtype) |  | **Required** |
+| id | string |  | **Required**<br>This property is nullable. |
+
+### RealtimeFunctionTool
+
+The definition of a function tool as used by the realtime endpoint.
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string |  | **Required**<br>Allowed values: `function` |
+| name | string |  | **Required** |
+| description | string |  |  |
+| parameters |  |  |  |
+
+### RealtimeItemStatus
+
+**Allowed Values:**
+
+* `in_progress` 
+* `completed` 
+* `incomplete` 
+
+### RealtimeItemType
+
+**Allowed Values:**
+
+* `message` 
+* `function_call` 
+* `function_call_output` 
+
+### RealtimeMessageRole
+
+**Allowed Values:**
+
+* `system` 
+* `user` 
+* `assistant` 
+
+### RealtimeRequestAssistantMessageItem
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| role | string |  | **Required**<br>Allowed values: `assistant` |
+| content | array |  | **Required**<br>Array items: [RealtimeRequestTextContentPart](#realtimerequesttextcontentpart) |
+
+### RealtimeRequestAudioContentPart
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string |  | **Required**<br>Allowed values: `input_audio` |
+| transcript | string |  |  |
+
+### RealtimeRequestFunctionCallItem
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string |  | **Required**<br>Allowed values: `function_call` |
+| name | string |  | **Required** |
+| call_id | string |  | **Required** |
+| arguments | string |  | **Required** |
+| status | [RealtimeItemStatus](#realtimeitemstatus) |  |  |
+
+### RealtimeRequestFunctionCallOutputItem
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string |  | **Required**<br>Allowed values: `function_call_output` |
+| call_id | string |  | **Required** |
+| output | string |  | **Required** |
+
+### RealtimeRequestMessageItem
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string |  | **Required**<br>Allowed values: `message` |
+| role | [RealtimeMessageRole](#realtimemessagerole) |  | **Required** |
+| status | [RealtimeItemStatus](#realtimeitemstatus) |  |  |
+
+### RealtimeRequestMessageReferenceItem
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string |  | **Required**<br>Allowed values: `message` |
+| id | string |  | **Required** |
+
+### RealtimeRequestSession
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| modalities | array |  |  |
+| instructions | string |  |  |
+| voice | [RealtimeVoice](#realtimevoice) |  |  |
+| input_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) |  |  |
+| output_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) |  |  |
+| input_audio_transcription | [RealtimeAudioInputTranscriptionSettings](#realtimeaudioinputtranscriptionsettings) |  | Nullable |
+| turn_detection | [RealtimeTurnDetection](#realtimeturndetection) |  | Nullable |
+| tools | array |  | Array items: [RealtimeTool](#realtimetool) |
+| tool_choice | [RealtimeToolChoice](#realtimetoolchoice) |  |  |
+| temperature | number |  |  |
+| max_response_output_tokens |  |  |  |
+
+### RealtimeRequestSystemMessageItem
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| role | string |  | **Required**<br>Allowed values: `system` |
+| content | array |  | **Required**<br>Array items: [RealtimeRequestTextContentPart](#realtimerequesttextcontentpart) |
+
+### RealtimeRequestTextContentPart
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string |  | **Required**<br>Allowed values: `input_text` |
+| text | string |  | **Required** |
+
+### RealtimeRequestUserMessageItem
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| role | string |  | **Required**<br>Allowed values: `user` |
+| content | array |  | **Required**<br>Array items can be: [RealtimeRequestTextContentPart](#realtimerequesttextcontentpart) or [RealtimeRequestAudioContentPart](#realtimerequestaudiocontentpart) |
+
+### RealtimeResponse
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| object | string |  | **Required**<br>Allowed values: `realtime.response` |
+| id | string |  | **Required** |
+| status | [RealtimeResponseStatus](#realtimeresponsestatus) |  | **Required**<br>Default: `in_progress` |
+| status_details | [RealtimeResponseStatusDetails](#realtimeresponsestatusdetails) |  | **Required**<br>This property is nullable. |
+| output | array |  | **Required**<br>Array items: [RealtimeConversationResponseItem](#realtimeconversationresponseitem) |
+| usage | object |  | **Required**<br>See nested properties next.|
+| + total_tokens | integer | A property of the `usage` object. | **Required** |
+| + input_tokens | integer | A property of the `usage` object. | **Required** |
+| + output_tokens | integer | A property of the `usage` object. | **Required** |
+| + input_token_details | object | A property of the `usage` object. | **Required**<br>See nested properties next.|
+| + cached_tokens | integer | A property of the `input_token_details` object. | **Required** |
+| + text_tokens | integer | A property of the `input_token_details` object. | **Required** |
+| + audio_tokens | integer | A property of the `input_token_details` object. | **Required** |
+| + output_token_details | object | A property of the `usage` object. | **Required**<br>See nested properties next.|
+| + text_tokens | integer | A property of the `output_token_details` object. | **Required** |
+| + audio_tokens | integer | A property of the `output_token_details` object. | **Required** |
+
+### RealtimeResponseAudioContentPart
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string |  | **Required**<br>Allowed values: `audio` |
+| transcript | string |  | **Required**<br>This property is nullable. |
+
+### RealtimeResponseBase
+
+The response resource.
+
+### RealtimeResponseFunctionCallItem
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string |  | **Required**<br>Allowed values: `function_call` |
+| name | string |  | **Required** |
+| call_id | string |  | **Required** |
+| arguments | string |  | **Required** |
+| status | [RealtimeItemStatus](#realtimeitemstatus) |  | **Required** |
+
+### RealtimeResponseFunctionCallOutputItem
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string |  | **Required**<br>Allowed values: `function_call_output` |
+| call_id | string |  | **Required** |
+| output | string |  | **Required** |
+
+### RealtimeResponseMessageItem
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string |  | **Required**<br>Allowed values: `message` |
+| role | [RealtimeMessageRole](#realtimemessagerole) |  | **Required** |
+| content | array |  | **Required**<br>Array items: [RealtimeContentPart](#realtimecontentpart) |
+| status | [RealtimeItemStatus](#realtimeitemstatus) |  | **Required** |
+
+### RealtimeResponseOptions
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| modalities | array | The modalities for the response. |  |
+| instructions | string | Instructions for the model. |  |
+| voice | [RealtimeVoice](#realtimevoice) | The voice the model uses to respond - one of `alloy`, `echo`, or `shimmer`. |  |
+| output_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) | The format of output audio. |  |
+| tools | array | Tools (functions) available to the model. | Array items: [RealtimeTool](#realtimetool) |
+| tool_choice | [RealtimeToolChoice](#realtimetoolchoice) | How the model chooses tools. |  |
+| temperature | number | Sampling temperature. |  |
+| max_output_tokens |  | Maximum number of output tokens for a single assistant response, inclusive of tool calls. Provide an integer between 1 and 4096 to limit output tokens, or "inf" for the maximum available tokens for a given model. Defaults to "inf". |  |
+
+### RealtimeResponseSession
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| object | string |  | **Required**<br>Allowed values: `realtime.session` |
+| id | string |  | **Required** |
+| model | string |  | **Required** |
+| modalities | array |  | **Required** |
+| instructions | string |  | **Required** |
+| voice | [RealtimeVoice](#realtimevoice) |  | **Required** |
+| input_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) |  | **Required** |
+| output_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) |  | **Required** |
+| input_audio_transcription | [RealtimeAudioInputTranscriptionSettings](#realtimeaudioinputtranscriptionsettings) |  | **Required**<br>This property is nullable. |
+| turn_detection | [RealtimeTurnDetection](#realtimeturndetection) |  | **Required** |
+| tools | array |  | **Required**<br>Array items: [RealtimeTool](#realtimetool) |
+| tool_choice | [RealtimeToolChoice](#realtimetoolchoice) |  | **Required** |
+| temperature | number |  | **Required** |
+| max_response_output_tokens |  |  | **Required**<br>This property is nullable. |
+
+### RealtimeResponseStatus
+
+**Allowed Values:**
+
+* `in_progress` 
+* `completed` 
+* `cancelled` 
+* `incomplete` 
+* `failed` 
+
+### RealtimeResponseStatusDetails
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | [RealtimeResponseStatus](#realtimeresponsestatus) |  | **Required** |
+
+### RealtimeResponseTextContentPart
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string |  | **Required**<br>Allowed values: `text` |
+| text | string |  | **Required** |
+
+### RealtimeServerEvent
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | [RealtimeServerEventType](#realtimeservereventtype) |  | **Required** |
+| event_id | string |  | **Required** |
+
+### RealtimeServerEventRateLimitsUpdatedRateLimitsItem
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| name | string | The rate limit property name that this item includes information about. | **Required** |
+| limit | integer | The maximum configured limit for this rate limit property. | **Required** |
+| remaining | integer | The remaining quota available against the configured limit for this rate limit property. | **Required** |
+| reset_seconds | number | The remaining time, in seconds, until this rate limit property is reset. | **Required** |
+
+### RealtimeServerEventType
+
+**Allowed Values:**
+
+* `session.created` 
+* `session.updated` 
+* `conversation.created` 
+* `conversation.item.created` 
+* `conversation.item.deleted` 
+* `conversation.item.truncated` 
+* `response.created` 
+* `response.done` 
+* `rate_limits.updated` 
+* `response.output_item.added` 
+* `response.output_item.done` 
+* `response.content_part.added` 
+* `response.content_part.done` 
+* `response.audio.delta` 
+* `response.audio.done` 
+* `response.audio_transcript.delta` 
+* `response.audio_transcript.done` 
+* `response.text.delta` 
+* `response.text.done` 
+* `response.function_call_arguments.delta` 
+* `response.function_call_arguments.done` 
+* `input_audio_buffer.speech_started` 
+* `input_audio_buffer.speech_stopped` 
+* `conversation.item.input_audio_transcription.completed` 
+* `conversation.item.input_audio_transcription.failed` 
+* `input_audio_buffer.committed` 
+* `input_audio_buffer.cleared` 
+* `error` 
+
+### RealtimeServerVadTurnDetection
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string |  | **Required**<br>Allowed values: `server_vad` |
+| threshold | number |  | Default: `0.5` |
+| prefix_padding_ms | string |  |  |
+| silence_duration_ms | string |  |  |
+
+### RealtimeSessionBase
+
+Realtime session object configuration.
+
+### RealtimeTool
+
+The base representation of a realtime tool definition.
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | [RealtimeToolType](#realtimetooltype) |  | **Required** |
+
+### RealtimeToolChoice
+
+The combined set of available representations for a realtime tool_choice parameter, encompassing both string literal options like 'auto' and structured references to defined tools.
+
+### RealtimeToolChoiceFunctionObject
+
+The representation of a realtime tool_choice selecting a named function tool.
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | string |  | **Required**<br>Allowed values: `function` |
+| function | object |  | **Required**<br>See nested properties next.|
+| + name | string | A property of the `function` object. | **Required** |
+
+### RealtimeToolChoiceLiteral
+
+The available set of mode-level, string literal tool_choice options for the realtime endpoint.
+
+**Allowed Values:**
+
+* `auto` 
+* `none` 
+* `required` 
+
+### RealtimeToolChoiceObject
+
+A base representation for a realtime tool_choice selecting a named tool.
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | [RealtimeToolType](#realtimetooltype) |  | **Required** |
+
+### RealtimeToolType
+
+The supported tool type discriminators for realtime tools.
+Currently, only 'function' tools are supported.
+
+**Allowed Values:**
+
+* `function` 
+
+### RealtimeTurnDetection
+
+| Field | Type | Description | More Info |
+|-------|------|-------------|----------------|
+| type | [RealtimeTurnDetectionType](#realtimeturndetectiontype) |  | **Required** |
+
+### RealtimeTurnDetectionType
+
+**Allowed Values:**
+
+* `server_vad` 
+
+### RealtimeVoice
+
+**Allowed Values:**
+
+* `alloy` 
+* `shimmer` 
+* `echo` 
+
+## Related content
+
+* Get started with the [Realtime API quickstart](./realtime-audio-quickstart.md).
+* Learn more about [How to use the Realtime API](./how-to/realtime-audio.md).
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "リアルタイムAPIリファレンスの追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるリアルタイムAPIについての包括的なリファレンスドキュメントが新たに追加されたことを示しています。このリファレンス文書では、WebSocketベースのAPIを用いたリアルタイムでの相互作用について詳細に説明されています。

主な内容は以下の通りです：

1. **ドキュメントの概要**: リアルタイムAPIはAzureOpenAIサービスとリアルタイムで相互作用するためのAPIであり、完全な非同期ストリーミング通信を可能にします。

2. **接続と認証**: APIへの接続方法および認証方法が記載されており、Microsoft Entraを用いたトークンベースの認証やAPIキーを使用した方法が説明されています。

3. **クライアントイベントとサーバーイベント**: APIで使用されるクライアントからサーバーへのイベント（例：会話アイテムの追加、オーディオデータのコミットなど）およびサーバーからクライアントへのレスポンスイベント（例：会話の作成、エラー通知など）のリストが提供されています。

4. **エラーハンドリング**: エラーが発生した場合のイベント構造とそれに伴う情報が提供されており、クライアントがエラーを特定しやすくしています。

5. **コンポーネントの定義**: リアルタイムAPIのリクエストやレスポンスに関連する様々なデータ構造が定義されており、開発者がAPIを使用する際の参考になります。

6. **関連コンテンツ**: リアルタイムAPIのクイックスタートや利用法に関するリンクが提供され、ユーザーが実際にAPIを使用する際の助けとなる情報が補完されています。

このリファレンスは、開発者がリアルタイムAPIを効果的に活用し、関連する機能を理解するための重要な資源となります。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -183,6 +183,8 @@ items:
         href: ./how-to/azure-developer-cli.md
       - name: Troubleshooting and best practices
         href: ./how-to/on-your-data-best-practices.md
+  - name: Use the Realtime API (preview)
+    href: ./how-to/realtime-audio.md
   - name: Migrate to OpenAI Python v1.x
     href: ./how-to/migration.md
   - name: Migrate to OpenAI JavaScript v4.x
@@ -346,6 +348,8 @@ items:
               displayName: RAG, rag
     - name: Azure OpenAI monitoring data reference
       href: monitor-openai-reference.md
+    - name: Realtime API (preview) WebSocket reference
+      href: realtime-audio-reference.md
 - name: Resources
   items: 
     - name: Support and help options
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次にリアルタイムAPI関連の項目を追加"
}
```

### Explanation
この変更では、Azure OpenAIサービスに関する目次ファイル `toc.yml` の内容が更新され、リアルタイムAPIに関連する2つの新しい項目が追加されました。

具体的な変更点は以下の通りです：

1. **リアルタイムAPIの使用**: 
   - 新しい項目「Use the Realtime API (preview)」が追加され、これに関連するハウツーガイド「./how-to/realtime-audio.md」へのリンクが設けられました。このガイドでは、リアルタイムAPIの利用方法が説明されています。

2. **WebSocketリファレンス**:
   - さらに、「Realtime API (preview) WebSocket reference」という項目が追加され、これに関連するリファレンスドキュメント「realtime-audio-reference.md」へのリンクも設けられています。このリファレンスはWebSocketに関する詳細情報を提供します。

この更新により、ユーザーはリアルタイムAPIに関する情報をより簡単にアクセスできるようになり、その使用方法やリファレンスに関する理解を深めることができます。


