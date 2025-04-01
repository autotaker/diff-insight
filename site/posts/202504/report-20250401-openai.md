---
date: '2025-04-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7dbd6d3...MicrosoftDocs:11d129c
summary: このコードの変更は、主に日付の更新、不要なノートの削除、リンクの修正に関連しています。また、プロビジョニングされたスループットに関する情報の大規模な更新や一部ドキュメントの構造見直しも含まれています。新機能としては、モデルデプロイボタンの画像が追加され、プロビジョニングされたスループットの説明が大幅に改訂されました。破壊的変更としては、アシスタントV2に関する情報が完全に削除されました。その他、軽微な更新や目次の整理も行われました。全体として、ドキュメントの最新性とユーザー体験の向上を目指した更新です。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7dbd6d3...MicrosoftDocs:11d129c){target="_blank"}

<format>
# ハイライト
このコードの変更は主に日付の更新や不要なノートの削除、リンクの修正を中心に行われました。また、一部のドキュメントにおける構造の見直しや、プロビジョニングされたスループットに関する大規模な更新が含まれています。

## 新機能
- モデルデプロイボタンの画像が追加され、視覚的な補助として機能。
- `articles/ai-services/openai/concepts/provisioned-throughput.md` では、プロビジョニングされたスループットの説明と情報が大幅に更新されました。

## 破壊的変更
- `assistants-v2-note.md` が完全に削除され、アシスタントV2に関する情報がドキュメントから取り除かれました。

## その他の更新
- 日付やノートの更新、誤ったリンクの修正などの軽微な更新。
- TOC（目次）の整理と再編成。

# 洞察
今般の変更は、ドキュメントの最新性や精度を保つことを目的として全般的に実施されました。日付や不要なノートの削除、リンクの見直しといった細かな更新が多い中、一部ではプロビジョニングされたスループットユニットに関する重要な改訂が行われています。

特に `provisioned-throughput.md` や `provisioned-throughput-onboarding.md` においては、ユーザーが理解しやすく使いやすいよう情報構成が整理されており、プロビジョニングされたスループットの利用を最大限に生かすための指針となります。また、新たに追加された画像はユーザーガイドやチュートリアルの視覚的な理解を助け、ユーザー体験を向上させる効果を発揮します。

削除された `assistants-v2-note.md` の影響は無視できないものの、これはドキュメント全体の整理や不要な情報を排除するための一環として理解できます。残されたドキュメントが分かりやすく、明確になったことで、ユーザーは重要な情報に容易にアクセスし、必要な知識を効率よく得られるでしょう。

全体的に、この一連の更新はAzure OpenAIサービスに関する利用者体験の向上を意図しており、特にプロビジョニングされたスループットに関する情報の価値を高め、より正確で信頼性のある情報を提供するものとなっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [assistants-reference-messages.md](#item-1c8daa) | minor update | 日付の更新と参照メッセージの修正 | modified | 1 | 3 | 4 | 
| [assistants-reference-runs.md](#item-ac752c) | minor update | 日付の更新と参照メッセージの修正 | modified | 1 | 3 | 4 | 
| [assistants-reference-threads.md](#item-d19db7) | minor update | 日付の更新と参照メッセージの修正 | modified | 1 | 3 | 4 | 
| [assistants-reference.md](#item-52344f) | minor update | ヘッダーからの参照メッセージの削除 | modified | 0 | 3 | 3 | 
| [provisioned-throughput.md](#item-022e0c) | breaking change | プロビジョニングされたスループットに関する著しい改訂 | modified | 24 | 81 | 105 | 
| [assistant-functions.md](#item-a47205) | minor update | 日付の更新及び不要なノートの削除 | modified | 1 | 3 | 4 | 
| [assistant.md](#item-b12c67) | minor update | 不要なノートの削除 | modified | 0 | 2 | 2 | 
| [code-interpreter.md](#item-95efbd) | minor update | 不要なノートの削除 | modified | 0 | 2 | 2 | 
| [file-search.md](#item-f9d6d7) | minor update | 日付の更新と不要なノートの削除 | modified | 1 | 4 | 5 | 
| [fine-tuning-deploy.md](#item-286d57) | minor update | 日付の更新とリンクの修正 | modified | 3 | 3 | 6 | 
| [on-your-data-configuration.md](#item-4875d3) | minor update | 日付の更新と文章の修正 | modified | 2 | 2 | 4 | 
| [provisioned-get-started.md](#item-c8df1c) | minor update | 著者情報の更新と表現の修正 | modified | 6 | 6 | 12 | 
| [provisioned-throughput-onboarding.md](#item-3eb72b) | major update | プロビジョニングされたスループットユニットに関する追加情報 | modified | 107 | 55 | 162 | 
| [working-with-models.md](#item-7ec098) | minor update | マイグレーションに関するドキュメントリンクの修正 | modified | 2 | 2 | 4 | 
| [assistants-python.md](#item-82d745) | minor update | アシスタントのV2に関する注意事項の削除 | modified | 0 | 2 | 2 | 
| [assistants-v2-note.md](#item-64ae04) | breaking change | アシスタントV2に関するノートの削除 | removed | 0 | 13 | 13 | 
| [use-your-data-studio.md](#item-705daf) | minor update | データスタジオの最終更新日を変更 | modified | 1 | 1 | 2 | 
| [deploy-model-button.png](#item-62cd49) | new feature | モデルデプロイボタンの画像を追加 | added | 0 | 0 | 0 | 
| [deployment-ptu-capacity-calculator.png](#item-aca8ed) | minor update | デプロイメントPTUのキャパシティ計算機のファイル名を変更 | renamed | 0 | 0 | 0 | 
| [toc.yml](#item-c945af) | minor update | TOCファイルの修正 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/ai-services/openai/assistants-reference-messages.md{#item-1c8daa}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's Python & REST API messages with Ass
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: reference
-ms.date: 02/27/2025
+ms.date: 03/31/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -14,8 +14,6 @@ ms.custom: devx-track-python
 
 # Assistants API (Preview) messages reference
 
-[!INCLUDE [Assistants v2 note](includes/assistants-v2-note.md)]
-
 This article provides reference documentation for Python and REST for the new Assistants API (Preview). More in-depth step-by-step guidance is provided in the [getting started guide](./how-to/assistant.md).
 
 ## Create message
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新と参照メッセージの修正"
}
```

### Explanation
この変更は、ドキュメント内の日付を更新するための小さな修正です。具体的には、ファイル `assistants-reference-messages.md` における日付が2025年2月27日から2025年3月31日に変更されました。また、ヘッダーからは「Assistants v2ノート」のインクルードが削除されました。これにより、ドキュメントが最新の情報を反映するようになります。この変更は、内容の整合性を高め、ユーザーにとって価値のある情報を提供することを目的としています。全体として、変更は1行の追加と3行の削除が行われています。

## articles/ai-services/openai/assistants-reference-runs.md{#item-ac752c}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's Python & REST API runs with Assista
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: reference
-ms.date: 09/17/2024
+ms.date: 03/31/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -14,8 +14,6 @@ ms.custom: devx-track-python
 
 # Assistants API (Preview) runs reference
 
-[!INCLUDE [Assistants v2 note](includes/assistants-v2-note.md)]
-
 This article provides reference documentation for Python and REST for the new Assistants API (Preview). More in-depth step-by-step guidance is provided in the [getting started guide](./how-to/assistant.md).
 
 ## Create run
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新と参照メッセージの修正"
}
```

### Explanation
この変更は、ファイル `assistants-reference-runs.md` における日付を更新するための小さな修正です。具体的には、日付が2024年9月17日から2025年3月31日に変更されました。また、ヘッダーから「Assistants v2ノート」のインクルードが削除されています。この変更は、ドキュメントが最新の情報を反映し続けるため、ユーザーに対する情報の信頼性を高める目的があります。全体として、1行の追加と3行の削除が行われています。

## articles/ai-services/openai/assistants-reference-threads.md{#item-d19db7}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's Python & REST API threads with Assi
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: reference
-ms.date: 02/27/2025
+ms.date: 03/31/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -14,8 +14,6 @@ ms.custom: devx-track-python
 
 # Assistants API (Preview) threads reference
 
-[!INCLUDE [Assistants v2 note](includes/assistants-v2-note.md)]
-
 This article provides reference documentation for Python and REST for the new Assistants API (Preview). More in-depth step-by-step guidance is provided in the [getting started guide](./how-to/assistant.md).
 
 ## Create a thread
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新と参照メッセージの修正"
}
```

### Explanation
この変更は、ファイル `assistants-reference-threads.md` における日付を更新するための小さな修正です。具体的には、日付が2025年2月27日から2025年3月31日に変更されました。また、ヘッダーから「Assistants v2ノート」のインクルードが削除されています。これにより、ドキュメントが最新の情報を反映し、ユーザーに信頼性の高い情報を提供することを目的としています。全体として、1行の追加と3行の削除が行われています。

## articles/ai-services/openai/assistants-reference.md{#item-52344f}

<details>
<summary>Diff</summary>
````diff
@@ -14,9 +14,6 @@ ms.custom: devx-track-python
 
 # Assistants API (Preview) reference
 
-
-[!INCLUDE [Assistants v2 note](includes/assistants-v2-note.md)]
-
 This article provides reference documentation for Python and REST for the new Assistants API (Preview). More in-depth step-by-step guidance is provided in the [getting started guide](./how-to/assistant.md).
 
 ## Create an assistant
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ヘッダーからの参照メッセージの削除"
}
```

### Explanation
この変更は、ファイル `assistants-reference.md` において、3行が削除された内容の更新です。具体的には、ヘッダーから「Assistants v2ノート」のインクルードが削除され、関連する空行も取り除かれています。この修正により、ドキュメントがよりクリーンで明確な内容に更新され、ユーザーに提供する情報の質が向上します。全体として、追加はなく、3行の削除が行われています。

## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -3,67 +3,43 @@ title: Azure OpenAI Service provisioned throughput
 description: Learn about provisioned throughput and Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 03/26/2025
+ms.date: 03/31/2025
 manager: nitinme
-author: mrbullwinkle #ChrisHMSFT
-ms.author: mbullwin #chrhoder
+author: aahill #ChrisHMSFT
+ms.author: aahi #chrhoder
 recommendations: false
 ---
 
 # What is provisioned throughput?
 
 > [!NOTE]
-> The Azure OpenAI Provisioned offering received significant updates on August 12, 2024, including aligning the purchase model with Azure standards and moving to model-independent quota. It is highly recommended that customers onboarded before this date read the Azure [OpenAI provisioned August update](./provisioned-migration.md) to learn more about these changes.
+> If you're looking for what's recently changed with the provisioned throughput offering, see the [update article](./provisioned-migration.md) for more information.
 
-
-The provisioned throughput capability allows you to specify the amount of throughput you require in a deployment. The service then allocates the necessary model processing capacity and ensures it's ready for you. Throughput is defined in terms of provisioned throughput units (PTU) which is a normalized way of representing the throughput for your deployment. Each model-version pair requires different amounts of PTU to deploy and provide different amounts of throughput per PTU. 
-
-## What do the provisioned deployment types provide?
+The provisioned throughput offering is a model deployment type that allows you to specify the amount of throughput you require in a model deployment. The Azure OpenAI service then allocates the necessary model processing capacity and ensures it's ready for you. Provisioned throughput provides:
 
 - **Predictable performance:** stable max latency and throughput for uniform workloads.
 - **Allocated processing capacity:** A deployment configures the amount of throughput. Once deployed, the throughput is available whether used or not.
 - **Cost savings:** High throughput workloads might provide cost savings vs token-based consumption.
 
-> [!NOTE]
-> Customers can take advantage of additional cost savings on provisioned deployments when they buy [Microsoft Azure OpenAI Service reservations](/azure/cost-management-billing/reservations/azure-openai#buy-a-microsoft-azure-openai-service-reservation). 
-
-
-An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model. A deployment provides customer access to a model for inference and integrates more features like Content Moderation ([See content moderation documentation](content-filter.md)). Global provisioned deployments are available in the same Azure OpenAI resources as all other deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center with the best availability for each request. Similarly, data zone provisioned deployments are also available in the same resources as all other deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center within the Microsoft specified data zone with the best availability for each request. 
-
-## What do you get?
-
-| Topic | Provisioned|
-|---|---|
-| What is it? |Provides guaranteed throughput at smaller increments than the existing provisioned offer. Deployments have a consistent max latency for a given model-version. |
-| Who is it for? | Customers who want guaranteed throughput with minimal latency variance. |
-| Quota |Provisioned Managed Throughput Unit, Global Provisioned Managed Throughput Unit, or Data Zone Provisioned Managed Throughput Unit assigned per region. Quota can be used across any available Azure OpenAI model.|
-| Latency | Max latency constrained from the model. Overall latency is a factor of call shape.  |
-| Utilization | Provisioned-managed Utilization V2 measure provided in Azure Monitor. |
-|Estimating size |Provided sizing calculator in Azure AI Foundry.|
-|Prompt caching | For supported models, we discount up to 100% of cached input tokens. |
-
+> [!TIP]
+> * You can take advantage of additional cost savings when you buy [Microsoft Azure OpenAI Service reservations](/azure/cost-management-billing/reservations/azure-openai#buy-a-microsoft-azure-openai-service-reservation).
+> * Provisioned throughput is available as the following deployment types: [global provisioned](../how-to/deployment-types.md#global-provisioned), [data zone provisioned](../how-to/deployment-types.md#data-zone-provisioned) and [standard provisioned](../how-to/deployment-types.md#provisioned).
 
-## How much throughput per PTU you get for each model
-The amount of throughput (tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in the minute. Generating output tokens requires more processing than input tokens. For the models specified in the table below, 1 output token counts as 3 input tokens towards your TPM per PTU limit. The service dynamically balances the input & output costs, so users do not have to set specific input and output limits. This approach means your deployment is resilient to fluctuations in the workload shape.
+<!--
+Throughput is defined in terms of provisioned throughput units (PTU) which is a normalized way of representing the throughput for your deployment. Each model-version pair requires different amounts of PTU to deploy, and provides different amounts of throughput per PTU. 
 
-To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the specified models. To understand the impact of output tokens on the TPM per PTU limit, use the 3 input token to 1 output token ratio. For a detailed understanding of how different ratios of input and output tokens impact the throughput your workload needs, see the [Azure OpenAI capacity calculator](https://ai.azure.com/resource/calculator). The table also shows Service Level Agreement (SLA) Latency Target Values per model.  For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
+An Azure OpenAI deployment is a unit of management for a specific OpenAI Model. A deployment provides customer access to a model for inference and using features, such as [content moderation](content-filter.md). 
+-->
 
-|Topic| **gpt-4o**   | **gpt-4o-mini**  | **o1**|
-| --- | --- | --- | --- |
-|Global & data zone provisioned minimum deployment|15|15|15|
-|Global & data zone provisioned scale increment|5|5|5|
-|Regional provisioned minimum deployment|50|25|50|
-|Regional provisioned scale increment|50|25|50|
-|Input TPM per PTU |2,500|37,000|230|
-|Latency Target Value |25 Tokens Per Second|33 Tokens Per Second|25 Tokens Per Second|
+## When to use provisioned throughput
 
-For a full list see the [Azure OpenAI Service in Azure AI Foundry portal calculator](https://ai.azure.com/resource/calculator).
+You should consider switching from standard deployments to provisioned managed deployments when you have well-defined, predictable throughput and latency requirements. Typically, this occurs when the application is ready for production or has already been deployed in production and there's an understanding of the expected traffic. This allows users to accurately forecast the required capacity and avoid unexpected billing. Provisioned managed deployments are also useful for applications that have real-time/latency sensitive requirements.
 
+## Key concepts
 
-> [!NOTE]
-> Global provisioned and data zone provisioned deployments are only supported for gpt-4o and gpt-4o-mini models at this time. For more information on model availability, review the [models documentation](./models.md).
+### Provisioned Throughput Units (PTU)
 
-## Key concepts
+Provisioned throughput units (PTUs) are generic units of model processing capacity that you can use to size provisioned deployments to achieve the required throughput for processing prompts and generating completions. Provisioned throughput units are granted to a subscription as quota, and used to define costs. Each quota is specific to a region and defines the maximum number of PTUs that can be assigned to deployments in that subscription and region. For information about the costs associated with the provision managed offering and PTUs, see [Understanding costs associated with PTU](../how-to/provisioned-throughput-onboarding.md).
 
 ### Deployment types
 
@@ -83,32 +59,7 @@ az cognitiveservices account deployment create \
 --sku-name GlobalProvisionedManaged
 ```
 
-### Quota
-
-#### Provisioned throughput units
-
-Provisioned throughput units (PTU) are generic units of model processing capacity that you can use to size provisioned deployments to achieve the required throughput for processing prompts and generating completions.   Provisioned throughput units are granted to a subscription as quota. Each quota is specific to a region and defines  the maximum number of PTUs that can be assigned to deployments in that subscription and region.
-
-
-#### Model independent quota
-
-Unlike the Tokens Per Minute (TPM) quota used by other Azure OpenAI offerings, PTUs are model-independent. The PTUs might be used to deploy any supported model/version in the region.
-
-:::image type="content" source="../media/provisioned/model-independent-quota.png" alt-text="Diagram of model independent quota with one pool of PTUs available to multiple Azure OpenAI models." lightbox="../media/provisioned/model-independent-quota.png":::
-
-For provisioned deployments, the new quota shows up in Azure AI Foundry as a quota item named **Provisioned Managed Throughput Unit**. For global provisioned deployments, the new quota shows up in the Azure AI Foundry as a quota item named **Global Provisioned Managed Throughput Unit**.  For data zone provisioned deployments, the new quota shows up in Azure AI Foundry as a quota item named **Data Zone Provisioned Managed Throughput Unit.** In the Foundry Quota pane, expanding the quota item shows the deployments contributing to usage of each quota.
-
-:::image type="content" source="../media/provisioned/ptu-quota-page.png" alt-text="Screenshot of quota UI for Azure OpenAI provisioned." lightbox="../media/provisioned/ptu-quota-page.png":::
-
-#### Obtaining PTU Quota
-
-PTU quota is available by default in many regions. If more quota is required, customers can request quota via the Request Quota link. This link can be found to the right of the designated provisioned deployment type quota tabs in Azure AI Foundry The form allows the customer to request an increase in the specified PTU quota for a given region. The customer receives an email at the included address once the request is approved, typically within two business days. 
-
-#### Per-Model PTU Minimums
-
-The minimum PTU deployment, increments, and processing capacity associated with each unit varies by model type & version.
-
-## Capacity transparency
+### Capacity transparency
 
 Azure OpenAI is a highly sought-after service where customer demand might exceed service GPU capacity. Microsoft strives to provide capacity for all in-demand regions and models, but selling out a region is always a possibility. This constraint can limit some customers' ability to create a deployment of their desired model, version, or number of PTUs in a desired region - even if they have quota available in that region. Generally speaking:
 
@@ -121,36 +72,28 @@ Azure OpenAI is a highly sought-after service where customer demand might exceed
 
 To find the capacity needed for their deployments, use the capacity API or the Azure AI Foundry deployment experience to provide real-time information on capacity availability.
 
-In Azure AI Foundry, the deployment experience identifies when a region lacks the capacity needed to deploy the model. This looks at the desired model, version and number of PTUs. If capacity is unavailable, the experience directs  users to a select an alternative region.
+In Azure AI Foundry, the deployment experience identifies when a region lacks the capacity needed to deploy the model. This looks at the desired model, version and number of PTUs. If capacity is unavailable, the experience directs users to a select an alternative region.
 
-Details on the new deployment experience can be found in the Azure OpenAI [Provisioned get started guide](../how-to/provisioned-get-started.md).
+Details on the deployment experience can be found in the Azure OpenAI [Provisioned get started guide](../how-to/provisioned-get-started.md).
 
-The new [model capacities API](/rest/api/aiservices/accountmanagement/model-capacities/list?view=rest-aiservices-accountmanagement-2024-04-01-preview&tabs=HTTP&preserve-view=true) can  be used to programmatically identify the maximum sized deployment of a specified model.  The API considers both your quota and service capacity in the region.
+The [model capacities API](/rest/api/aiservices/accountmanagement/model-capacities/list?view=rest-aiservices-accountmanagement-2024-04-01-preview&tabs=HTTP&preserve-view=true) can be used to programmatically identify the maximum sized deployment of a specified model.  The API considers both your quota and service capacity in the region.
 
 If an acceptable region isn't available to support the desire model, version and/or PTUs, customers can also try the following steps:
 
 - Attempt the deployment with a smaller number of PTUs.
 - Attempt the deployment at a different time. Capacity availability changes dynamically based on customer demand and more capacity might become available later.
 - Ensure that quota is available in all acceptable regions. The [model capacities API](/rest/api/aiservices/accountmanagement/model-capacities/list?view=rest-aiservices-accountmanagement-2024-04-01-preview&tabs=HTTP&preserve-view=true) and Azure AI Foundry experience consider quota availability in returning alternative regions for creating a deployment.
 
-### Determining the number of PTUs needed for a workload
-
-PTUs represent an amount of model processing capacity. Similar to your computer or databases, different workloads or requests to the model will consume different amounts of underlying processing capacity. The conversion from throughput needs to PTUs can be approximated using historical token usage data or call shape estimations (input tokens, output tokens, and requests per minute) as outlined in our [performance and latency](../how-to/latency.md) documentation. To simplify this process, you can use the [Azure OpenAI Capacity calculator](https://ai.azure.com/resource/calculator) to size specific workload shapes.
+### How can I monitor capacity?
 
-A few high-level considerations:
-- Generations require more capacity than prompts
-- For GPT-4o and later models, the TPM per PTU is set for input and output tokens separately. For older models, larger calls are progressively more expensive to compute. For example, 100 calls of with a 1000 token prompt size requires less capacity than one call with 100,000 tokens in the prompt. This tiering means that the distribution of these call shapes is important in overall throughput. Traffic patterns with a wide distribution that includes some large calls might experience lower throughput per PTU than a narrower distribution with the same average prompt & completion token sizes.
+The [Provisioned-Managed Utilization V2 metric](../how-to/monitoring.md#azure-openai-metrics) in Azure Monitor measures a given deployments utilization on 1-minute increments. All provisioned deployment types are optimized to ensure that accepted calls are processed with a consistent model processing time (actual end-to-end latency is dependent on a call's characteristics).  
 
 ### How utilization performance works
 
 Provisioned deployments provide you with an allocated amount of model processing capacity to run a given model.
 
 In all provisioned deployment types, when capacity is exceeded, the API will return a 429 HTTP Status Error. This fast response enables the user to make decisions on how to manage their traffic. Users can redirect requests to a separate deployment, to a standard pay-as-you-go instance, or use a retry strategy to manage a given request. The service continues to return the 429 HTTP status code until the utilization drops below 100%.
 
-### How can I monitor capacity?
-
-The [Provisioned-Managed Utilization V2 metric](../how-to/monitoring.md#azure-openai-metrics) in Azure Monitor measures a given deployments utilization on 1-minute increments. All provisioned deployment types are optimized to ensure that accepted calls are processed with a consistent model processing time (actual end-to-end latency is dependent on a call's characteristics).  
-
 #### What should  I do when I receive a 429 response?
 The 429 response isn't an error, but instead part of the design for telling users that a given deployment is fully utilized at a point in time. By providing a fast-fail response, you have control over how to handle these situations in a way that best fits your application requirements.
 
@@ -169,7 +112,7 @@ For provisioned deployments, we use a variation of the leaky bucket algorithm to
 
     a.    When the current utilization is above 100%, the service returns a 429 code with the `retry-after-ms` header set to the time until utilization is below 100%
    
-    b.    Otherwise, the service estimates the incremental change to utilization required to serve the request by combining the prompt tokens, less any cached tokens, and the specified `max_tokens` in the call. A customer can receive up to a 100% discount on their prompt tokens depending on the size of their cached tokens. If the `max_tokens` parameter is not specified, the service estimates a value. This estimation can lead to lower concurrency than expected when the number of actual generated tokens is small.  For highest concurrency, ensure that the `max_tokens` value is as close as possible to the true generation size.
+    b.    Otherwise, the service estimates the incremental change to utilization required to serve the request by combining the prompt tokens, less any cached tokens, and the specified `max_tokens` in the call. A customer can receive up to a 100% discount on their prompt tokens depending on the size of their cached tokens. If the `max_tokens` parameter is not specified, the service estimates a value. This estimation can lead to lower concurrency than expected when the number of actual generated tokens is small. For highest concurrency, ensure that the `max_tokens` value is as close as possible to the true generation size.
    
 1. When a request finishes, we now know the actual compute cost for the call. To ensure an accurate accounting, we correct the utilization using the following logic:
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロビジョニングされたスループットに関する著しい改訂"
}
```

### Explanation
この変更は、ファイル `provisioned-throughput.md` に大規模なレビューを加えたもので、合計で24行が追加され、81行が削除されています。主な変更点は、Azure OpenAIのプロビジョニングされたスループットの説明を明確化し、更新された情報を反映することにあります。特に、コンセプトの説明が整理され、利用者がプロビジョニングされたスループットの特性や利点をより理解しやすくなっています。

更新された内容には、スループットの定義、提供される機能、推奨される利用方法、コストに関連する情報が含まれています。また、新しい日付に更新されたり、特定のノートや注意事項が追加されたりして、ユーザーに対する最新の価値提供が意図されています。

削除された内容の中には、重複する情報や具体的なテーブルがあり、新しい構成をよりシンプルかつ理解しやすくするための措置と考えられます。全体的に、この変更はユーザーがよりスムーズに情報を取得し、Azure OpenAIサービスのプロビジョニングされたスループットを利用できるようにすることを目的としています。

## articles/ai-services/openai/how-to/assistant-functions.md{#item-a47205}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 09/04/2024
+ms.date: 03/31/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -17,8 +17,6 @@ recommendations: false
 
 The Assistants API supports function calling, which allows you to describe the structure of functions to an Assistant and then return the functions that need to be called along with their arguments.
 
-[!INCLUDE [Assistants v2 note](../includes/assistants-v2-note.md)]
-
 ## Function calling support
 
 ### Supported models
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新及び不要なノートの削除"
}
```

### Explanation
この変更は、ファイル `assistant-functions.md` において、1行の追加と3行の削除が行われた内容の更新です。具体的には、ドキュメントの日付が2024年9月4日から2025年3月31日に更新され、古い情報を参照しているノート（「Assistants v2 note」）が削除されています。この更新により、ドキュメントが現在の情報を反映した内容となり、ユーザーは最新のアシスタントAPI機能やその使用方法を正確に理解できるようになります。

全体として、この変更は、記事の情報の鮮度を保つための軽微な修正であり、ユーザーの体験を向上させることを目的としています。

## articles/ai-services/openai/how-to/assistant.md{#item-b12c67}

<details>
<summary>Diff</summary>
````diff
@@ -18,8 +18,6 @@ recommendations: false
 
 Azure OpenAI Assistants (Preview) allows you to create AI assistants tailored to your needs through custom instructions and augmented by advanced tools like code interpreter, and custom functions. In this article, we provide an in-depth walkthrough of getting started with the Assistants API.
 
-[!INCLUDE [Assistants v2 note](../includes/assistants-v2-note.md)]
-
 ## Assistants support
 
 ### Region, model, and API support
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "不要なノートの削除"
}
```

### Explanation
この変更は、ファイル `assistant.md` で2行の削除が行われたもので、内容としては「Assistants v2 note」と呼ばれる不要なノートが削除されています。これにより、読者がドキュメントをよりスムーズに理解できるようになり、混乱の原因となる可能性のある情報が取り除かれました。

この更新により、Azure OpenAIアシスタントに関する説明が簡潔になり、ユーザーはアシスタントAPIの始め方に関する情報をより明瞭に把握できるようになります。全体として、この変更は文書の明確性を向上させるための軽微な修正と位置付けられます。

## articles/ai-services/openai/how-to/code-interpreter.md{#item-95efbd}

<details>
<summary>Diff</summary>
````diff
@@ -20,8 +20,6 @@ Code Interpreter allows the Assistants API to write and run Python code in a san
 > [!IMPORTANT]
 > Code Interpreter has [additional charges](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) beyond the token based fees for Azure OpenAI usage. If your Assistant calls Code Interpreter simultaneously in two different threads, two code interpreter sessions are created. Each session is active by default for one hour.
 
-[!INCLUDE [Assistants v2 note](../includes/assistants-v2-note.md)]
-
 ## Code interpreter support
 
 ### Supported models
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "不要なノートの削除"
}
```

### Explanation
この変更は、ファイル `code-interpreter.md` における2行の削除に関するものです。削除された内容は「Assistants v2 note」というノートであり、これによりドキュメントの情報がシンプルになり、ユーザーにとっての理解が容易になります。

具体的には、この更新によって、コードインタープリタの機能に関する説明がより明確になり、重要な料金情報や同時スレッドに関する注意事項が引き続き強調されています。不要な情報を取り除くことで、読者は必要な知識に集中できるようになります。この修正は、Azure OpenAIサービスに関する文書の明瞭性と読みやすさを向上させるための軽微な更新と位置付けられます。

## articles/ai-services/openai/how-to/file-search.md{#item-f9d6d7}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 01/28/2025
+ms.date: 03/31/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -19,9 +19,6 @@ File Search augments the Assistant with knowledge from outside its model, such a
 > [!IMPORTANT]
 > * File search has [additional charges](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) beyond the token based fees for Azure OpenAI usage.
 
-
-[!INCLUDE [Assistants v2 note](../includes/assistants-v2-note.md)]
-
 ## File search support
 
 ### Supported regions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新と不要なノートの削除"
}
```

### Explanation
この変更は、ファイル `file-search.md` に対する修正で、主に1つの更新と4つの削除が行われています。具体的には、`ms.date` フィールドの値が「2025年1月28日」から「2025年3月31日」に変更されており、ドキュメントの情報が最新のものに更新されています。

また、不要なノート「Assistants v2 note」が削除され、ドキュメントの内容が簡潔になっています。この修正により、ファイル検索機能に関連する重要な情報はそのままにしつつ、余分な情報を省くことで利用者が理解しやすくなるように配慮されています。

全体として、この変更は、日付の更新と文書の明瞭性を高めるための軽微な修正を反映したものです。

## articles/ai-services/openai/how-to/fine-tuning-deploy.md{#item-286d57}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: build-2023, build-2023-dataai, devx-track-python, references_regions
 ms.topic: how-to
-ms.date: 02/24/2025
+ms.date: 03/31/2025
 author: mrbullwinkle
 ms.author: mbullwin
 ---
@@ -389,7 +389,7 @@ Global Standard fine-tuned deployments currently support structured outputs only
 - `gpt-4o-mini-2024-07-18`
 - `gpt-4o-2024-08-06`
 
-[Provisioned managed](./deployment-types.md#provisioned) fine-tuned deployments offer [predictable performance](../concepts/provisioned-throughput.md#what-do-the-provisioned-deployment-types-provide) for fine-tuned deployments. As part of public preview, provisioned managed deployments may be created regionally via the data-plane [REST API](../reference.md#data-plane-inference) version `2024-10-01` or newer. See below for examples.
+[Provisioned managed](./deployment-types.md#provisioned) fine-tuned deployments offer [predictable performance](../concepts/provisioned-throughput.md) for fine-tuned deployments. As part of public preview, provisioned managed deployments may be created regionally via the data-plane [REST API](../reference.md#data-plane-inference) version `2024-10-01` or newer. See below for examples.
 
 Provisioned Managed fine-tuned deployments currently support structured outputs only on GPT-4o.
 
@@ -423,7 +423,7 @@ curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceG
 
 #### Scaling a fine-tuned model on Provisioned Managed
 
-To scale a fine-tuned provision managed deployment to increase or decrease PTU capacity, perform the same `PUT` REST API call as you did when [creating the deployment](#creating-a-provisioned-managed-deployment) and provide an updated `capacity` value for the `sku`. Keep in mind, provisioned deployments must scale in [minimum increments](../concepts/provisioned-throughput.md#how-much-throughput-per-ptu-you-get-for-each-model).
+To scale a fine-tuned provision managed deployment to increase or decrease PTU capacity, perform the same `PUT` REST API call as you did when [creating the deployment](#creating-a-provisioned-managed-deployment) and provide an updated `capacity` value for the `sku`. Keep in mind, provisioned deployments must scale in [minimum increments](../how-to/provisioned-throughput-onboarding.md#how-much-throughput-per-ptu-you-get-for-each-model).
 
 For example, to scale the model deployed in the previous section from 25 to 40 PTU, make another `PUT` call and increase the capacity:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新とリンクの修正"
}
```

### Explanation
この変更は、ファイル `fine-tuning-deploy.md` に対する修正で、主に日付の更新といくつかのリンクの修正が行われています。具体的には、`ms.date` フィールドの値が「2025年2月24日」から「2025年3月31日」に変更されています。この変更は、ドキュメントの情報を最新の状態に保つためのものです。

また、リンクが一箇所修正されており、以前は別のURLを指していた部分が、適切な情報を含む新しいリンクに置き換えられています。このリンクの更新は、ユーザーが正確な情報を取得できるようにするための修正です。

全体として、これらの変更は、ドキュメントの精度を向上させ、ユーザーにとっての可用性を高めるための軽微な更新として位置付けられます。

## articles/ai-services/openai/how-to/on-your-data-configuration.md{#item-4875d3}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-openai
 ms.topic: how-to
 author: aahill
 ms.author: aahi
-ms.date: 12/03/2024
+ms.date: 03/31/2025
 recommendations: false
 ---
 
@@ -16,7 +16,7 @@ recommendations: false
 > [!NOTE]
 > As of June 2024, the application form for the Microsoft managed private endpoint to Azure AI Search is no longer needed.
 >
-> The managed private endpoint will be deleted from the Microsoft managed virtual network at July 2025. If you have already provisioned a managed private endpoint through the application process before June 2024, enable [Azure AI Search trusted service](#enable-trusted-service-1) as early as possible to avoid service disruption. 
+> The managed private endpoint will be deleted from the Microsoft managed virtual network in July 2025. If you have already provisioned a managed private endpoint through the application process before June 2024, enable [Azure AI Search trusted service](#enable-trusted-service-1) as early as possible to avoid service disruption. 
 
 Use this article to learn how to configure networking and access when using Azure OpenAI On Your Data with Microsoft Entra ID role-based access control, virtual networks, and private endpoints.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新と文章の修正"
}
```

### Explanation
この変更は、ファイル `on-your-data-configuration.md` に対する修正で、主に日付の更新と文書内の一部表現の変更が行われています。具体的には、`ms.date` フィールドの値が「2024年12月3日」から「2025年3月31日」に変更され、文書の更新日時が最新にされています。

また、文中のヒントに関する文がわずかに修正されており、「The managed private endpoint will be deleted from the Microsoft managed virtual network at July 2025」という表現が「The managed private endpoint will be deleted from the Microsoft managed virtual network in July 2025」に変更されています。この修正により、文の流れがより自然になり、理解しやすくなっています。

全体として、これらの変更は、情報の正確性を保つための軽微な更新と、表現をより明確にするための調整として位置付けられます。

## articles/ai-services/openai/how-to/provisioned-get-started.md{#item-c8df1c}

<details>
<summary>Diff</summary>
````diff
@@ -6,13 +6,13 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: openai
 ms.topic: how-to
-author: mrbullwinkle
-ms.author: mbullwin
-ms.date: 03/26/2025
+author: aahill
+ms.author: aahi
+ms.date: 03/31/2025
 recommendations: false
 ---
 
-# Get started using Provisioned Deployments on the Azure OpenAI Service
+# Get started using provisioned deployments on the Azure OpenAI Service
 
 The following guide walks you through key steps in creating a provisioned deployment with your Azure OpenAI Service resource. For more details on the concepts discussed here, see:
 * [Azure OpenAI Provisioned Onboarding Guide](./provisioned-throughput-onboarding.md)
@@ -51,7 +51,7 @@ Provisioned deployments are created via Azure OpenAI resource objects within Azu
 
 ## Create your provisioned deployment - capacity is available
 
-once you have verified your quota, you can create a deployment. To create a provisioned deployment, you can follow these steps; the choices described reflect the entries shown in the screenshot. 
+Once you have verified your quota, you can create a deployment. To create a provisioned deployment, you can follow these steps; the choices described reflect the entries shown in the screenshot. 
 
 :::image type="content" source="../media/provisioned/deployment-screen.png" alt-text="Screenshot of the Azure AI Foundry portal deployment page for a provisioned deployment." lightbox="../media/provisioned/deployment-screen.png":::
 
@@ -80,7 +80,7 @@ Once you have entered the deployment settings, click **Confirm Pricing** to cont
 If you are unsure of the costs, cancel the deployment and proceed once you understand the payment model and underlying costs for provisioned deployment. This step may prevent unexpected, high charges on your payment invoice. Resources to educate yourself include: 
 
 * [Azure Pricing Portal](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) 
-* [Understanding the provisioned throughput purchase model](provisioned-throughput-onboarding.md#understanding-the-provisioned-throughput-purchase-model) 
+* [Understanding the provisioned throughput costs](provisioned-throughput-onboarding.md) 
 
 The image below shows the pricing confirmation you will see. The price shown is an example only. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報の更新と表現の修正"
}
```

### Explanation
この変更は、ファイル `provisioned-get-started.md` に対する修正で、著者情報の更新といくつかの表現の修正が行われています。具体的には、著者が「mrbullwinkle」から「aahill」に変更され、`ms.author` フィールドもそれに合わせて更新されました。また、日付も「2025年3月26日」から「2025年3月31日」に変更されています。

タイトル行では、「Provisioned Deployments」という用語が「provisioned deployments」に修正されています。これにより、小文字を使った統一された表現が維持されています。

その他の変更点として、いくつかの文の表現も若干修正されており、これにより文書がより明確で一貫性のあるものとなっています。特に、リンクが「Understanding the provisioned throughput purchase model」から「Understanding the provisioned throughput costs」に変更され、ユーザーがより具体的な情報にアクセスできるように配慮されています。

全体として、これらの変更は、情報の正確性や一貫性を高めるための軽微な更新として位置付けられます。

## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -1,46 +1,126 @@
 ---
-title: Azure OpenAI Service Provisioned Throughput Units (PTU) onboarding
-description: Learn about provisioned throughput units onboarding and Azure OpenAI. 
+title:  Understanding costs associated with provisioned throughput units (PTU)
+description: Learn about provisioned throughput costs and billing in Azure OpenAI. 
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 03/27/2025
+ms.date: 03/31/2025
 manager: nitinme
-author: mrbullwinkle 
-ms.author: mbullwin 
+author: aahill 
+ms.author: aahi 
 recommendations: false
 ---
 
-# Provisioned throughput units onboarding
+# Understanding costs associated with provisioned throughput units (PTU)
 
-This article walks you through the process of onboarding to [Provisioned Throughput Units (PTU)](../concepts/provisioned-throughput.md). Once you complete the initial onboarding, we recommend referring to the PTU [getting started guide](./provisioned-get-started.md).
+Use this article to learn about calculating and understanding costs associated with PTU. For an overview of the provisioned throughput offering, see [What is provisioned throughput?](../concepts/provisioned-throughput.md). When you're ready to sign up for the provisioned throughput offering, see the [getting started guide](./provisioned-get-started.md).
 
-## When to use provisioned throughput units (PTU)
+> [!NOTE]
+> In function calling and agent use cases, token usage can be variable. You should understand your expected Tokens Per Minute (TPM) usage in detail before migrating workloads to PTU.
+
+## Provisioned throughput units
 
-You should consider switching from standard deployments to provisioned deployments when you have well-defined, predictable throughput and latency requirements. Typically, this occurs when the application is ready for production or has already been deployed in production and there's an understanding of the expected traffic. This allows users to accurately forecast the required capacity and avoid unexpected billing. 
+Provisioned throughput units (PTUs) are generic units of model processing capacity that you can use to size provisioned deployments to achieve the required throughput for processing prompts and generating completions.  Provisioned throughput units are granted to a subscription as quota. Each quota is specific to a region and defines  the maximum number of PTUs that can be assigned to deployments in that subscription and region.
 
-### Typical PTU scenarios
+## Understanding provisioned throughput billing
 
-- An application that is ready for production or in production. 
-- An application that has predictable capacity/usage expectations. 
-- An application has real-time/latency sensitive requirements. 
+Azure OpenAI [Provisioned](../how-to/deployment-types.md#provisioned), [Data Zone Provisioned](../how-to/deployment-types.md#data-zone-provisioned) (also known as regional), and [Global Provisioned](../how-to/deployment-types.md#global-provisioned) are purchased on-demand at an hourly basis based on the number of deployed PTUs, with substantial term discount available via the purchase of [Azure Reservations](#azure-reservations-for-azure-openai-provisioned-deployments).  
+
+The hourly model is useful for short-term deployment needs, such as validating new models or acquiring capacity for a hackathon.  However, the discounts provided by the Azure Reservation for Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned are considerable and most customers with consistent long-term usage will find a reserved model to be a better value proposition. 
 
 > [!NOTE]
-> In function calling and agent use cases, token usage can be variable. You should understand your expected Tokens Per Minute (TPM) usage in detail prior to migrating workloads to PTU.
+> Azure OpenAI Provisioned customers onboarded prior to the August self-service update use a purchase model called the Commitment model. These customers can continue to use this older purchase model alongside the Hourly/reservation purchase model. The Commitment model is not available for new customers or [certain new models](../concepts/provisioned-migration.md#supported-models-on-commitment-payment-model) introduced after August 2024. For details on the Commitment purchase model and options for coexistence and migration, see the [Azure OpenAI Provisioned August Update](../concepts/provisioned-migration.md).
 
-## Sizing and estimation: provisioned deployments
 
-Determining the right amount of provisioned throughput, or PTUs, you require for your workload is an essential step to optimizing performance and cost. If you aren't familiar with the different approaches available to estimate system level throughput, review the system level throughput estimation recommendations in our [performance and latency documentation](./latency.md). This section describes how to use Azure OpenAI capacity calculators to estimate the number of PTUs required to support a given workload.
+## Model independent quota
 
-### Estimate provisioned throughput units and cost
+Unlike the Tokens Per Minute (TPM) quota used by other Azure OpenAI offerings, PTUs are model-independent. The PTUs might be used to deploy any supported model/version in the region.
 
-To get a quick estimate for your workload using input and output TPM, leverage the built-in capacity planner in the deployment details section of the deployment dialogue screen. The built-in capacity planner is part of the deployment workflow to help streamline the sizing and allocation of quota to a PTU deployment for a given workload. For more information on how to identify and estimate TPM data, review the recommendations in our [performance and latency documentation](./latency.md). 
+:::image type="content" source="../media/provisioned/model-independent-quota.png" alt-text="Diagram of model independent quota with one pool of PTUs available to multiple Azure OpenAI models." lightbox="../media/provisioned/model-independent-quota.png":::
+
+Quota for provisioned deployments shows up in Azure AI Foundry as the following deployment types: [global provisioned](../how-to/deployment-types.md#global-provisioned), [data zone provisioned](../how-to/deployment-types.md#data-zone-provisioned) and [standard provisioned](../how-to/deployment-types.md#provisioned).
+
+|deployment type  |Quota name  |
+|---------|---------|
+|[provisioned](../how-to/deployment-types.md#provisioned)     |  Provisioned Managed Throughput Unit       |
+|[global provisioned](../how-to/deployment-types.md#global-provisioned)     | Global Provisioned Managed Throughput Unit        |
+|[data zone provisioned](../how-to/deployment-types.md#data-zone-provisioned)    | Data Zone Provisioned Managed Throughput Unit        |
+
+:::image type="content" source="../media/provisioned/ptu-quota-page.png" alt-text="Screenshot of quota UI for Azure OpenAI provisioned." lightbox="../media/provisioned/ptu-quota-page.png":::
+
+
+> [!NOTE]
+> Global provisioned and data zone provisioned deployments are only supported for gpt-4o and gpt-4o-mini models at this time. For more information on model availability, review the [models documentation](../concepts/models.md).
+
+## Hourly usage
+
+Provisioned, Data Zone Provisioned, and Global Provisioned deployments are charged an hourly rate ($/PTU/hr) on the number of PTUs that have been deployed.  For example, a 300 PTU deployment will be charged the hourly rate times 300.  All Azure OpenAI pricing is available in the Azure Pricing Calculator. 
+
+If a deployment exists for a partial hour, it will receive a prorated charge based on the number of minutes it was deployed during the hour.  For example, a deployment that exists for 15 minutes during an hour will receive 1/4th the hourly charge.  
+
+If the deployment size is changed, the costs of the deployment will adjust to match the new number of PTUs.  
+
+:::image type="content" source="../media/provisioned/hourly-billing.png" alt-text="A diagram showing hourly billing." lightbox="../media/provisioned/hourly-billing.png":::
+
+Paying for provisioned, data zoned provisioned, and global provisioned deployments on an hourly basis is ideal for short-term deployment scenarios.  For example: Quality and performance benchmarking of new models, or temporarily increasing PTU capacity to cover an event such as a hackathon.  
+
+Customers that require long-term usage of provisioned, data zoned provisioned, and global provisioned deployments, however, might pay significantly less per month by purchasing a term discount via [Azure Reservations](#azure-reservations-for-azure-openai-provisioned-deployments) as discussed later in the article. 
+
+> [!IMPORTANT]
+> It's not recommended to scale production deployments according to incoming traffic and pay for them purely on an hourly basis. There are two reasons for this:
+> * The cost savings achieved by purchasing Azure Reservations for Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned are significant, and it will be less expensive in many cases to maintain a deployment sized for full production volume paid for via a reservation than it would be to scale the deployment with incoming traffic.
+> * Having unused provisioned quota (PTUs) doesn't guarantee that capacity will be available to support an increase in the size of the deployment when required. Quota limits the maximum number of PTUs that can be deployed, but it isn't a capacity guarantee. Provisioned capacity for each region and model dynamically changes throughout the day and might not be available when required. As a result, it's recommended to maintain a permanent deployment to cover your traffic needs (paid for via a reservation).
+> Charges for deployments on a deleted resource will continue until the resource is purged. To prevent this, delete a resource’s deployment before deleting the resource. For more information, see [Recover or purge deleted Azure AI services resources](../../recover-purge-resources.md). 
+
+## How much throughput per PTU you get for each model
+The amount of throughput (measured in tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in a given minute. 
+
+Generating output tokens requires more processing than input tokens. For the models specified in the table below, 1 output token counts as 3 input tokens towards your TPM-per-PTU limit. The service dynamically balances the input & output costs, so users do not have to set specific input and output limits. This approach means your deployment is resilient to fluctuations in the workload.
+
+To help with simplifying the sizing effort, the following table outlines the TPM-per-PTU for the specified models. To understand the impact of output tokens on the TPM-per-PTU limit, use the 3 input token to 1 output token ratio. 
+
+For a detailed understanding of how different ratios of input and output tokens impact the throughput your workload needs, see the [Azure OpenAI capacity calculator](https://ai.azure.com/resource/calculator). The table also shows Service Level Agreement (SLA) Latency Target Values per model. For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
+
+
+|Topic| **gpt-4o**   | **gpt-4o-mini**  | **o1**|
+| --- | --- | --- | --- |
+|Global & data zone provisioned minimum deployment|15|15|15|
+|Global & data zone provisioned scale increment|5|5|5|
+|Regional provisioned minimum deployment|50|25|50|
+|Regional provisioned scale increment|50|25|50|
+|Input TPM per PTU |2,500|37,000|230|
+|Latency Target Value |25 Tokens Per Second|33 Tokens Per Second|25 Tokens Per Second|
 
-After filling out the input and output TPM data in the built-in capacity calculator, select the **Calculate** button to view your PTU allocation recommendation. 
+For a full list, see the [Azure OpenAI Service in Azure AI Foundry portal calculator](https://ai.azure.com/resource/calculator).
 
-![Screenshot of deployment workflow PTU capacity calculator.](media/provisioned-throughput-onboarding/deployment-ptu-capacity-calculator.png)
+## Determining the number of PTUs needed for a workload
 
+Determining the right amount of provisioned throughput, or PTUs, you require for your workload is an essential step to optimizing performance and cost. 
 
+PTUs represent an amount of model processing capacity. Similar to your computer or databases, different workloads or requests to the model will consume different amounts of underlying processing capacity. The conversion from throughput needs to PTUs can be approximated using historical token usage data or call shape estimations (input tokens, output tokens, and requests per minute) as outlined in our [performance and latency](../how-to/latency.md) documentation. To simplify this process, you can use the [Azure OpenAI Capacity calculator](https://ai.azure.com/resource/calculator) to size specific workload shapes.
 
+A few high-level considerations:
+- Generations require more capacity than prompts
+- For GPT-4o and later models, the TPM per PTU is set for input and output tokens separately. For older models, larger calls are progressively more expensive to compute. For example, 100 calls of with a 1000 token prompt size requires less capacity than one call with 100,000 tokens in the prompt. This tiering means that the distribution of these call shapes is important in overall throughput. Traffic patterns with a wide distribution that includes some large calls might experience lower throughput per PTU than a narrower distribution with the same average prompt & completion token sizes.
+
+### Obtaining PTU quota
+
+PTU quota is available by default in many regions. If more quota is required, customers can request quota via the Request Quota link. This link can be found to the right of the designated provisioned deployment type quota tabs in Azure AI Foundry The form allows the customer to request an increase in the specified PTU quota for a given region. The customer receives an email at the included address once the request is approved, typically within two business days. 
+
+### Per-Model PTU minimums
+
+The minimum PTU deployment, increments, and processing capacity associated with each unit varies by model type & version. See the above [table](#how-much-throughput-per-ptu-you-get-for-each-model) for more information.
+
+## Estimate provisioned throughput units and cost
+
+To get a quick estimate for your workload using input and output TPM, leverage the built-in capacity planner in the deployment details section of the deployment dialogue screen. The built-in capacity planner is part of the deployment workflow to help streamline the sizing and allocation of quota to a PTU deployment for a given workload. For more information on how to identify and estimate TPM data, review the recommendations in our [performance and latency documentation](./latency.md). 
+
+To use the capacity planner, go to the Azure AI Foundry Portal and select the **Deployments** button. Then select **Deploy model**.
+
+:::image type="content" source="../media/provisioned/deploy-model-button.png" alt-text="A screenshot of the model deployment screen." lightbox="../media/provisioned/deploy-model-button.png":::
+
+Choose a model, and click **Confirm**. Select a provision-managed deployment type. After filling out the input and output TPM data in the built-in capacity calculator, select the **Calculate** button to view your PTU allocation recommendation. 
+
+:::image type="content" source="../media/provisioned/deployment-ptu-capacity-calculator.png" alt-text="A screenshot of deployment workflow PTU capacity calculator." lightbox="../media/provisioned/deployment-ptu-capacity-calculator.png":::
 
 To estimate provisioned capacity using request level data, open the capacity planner in the [Azure AI Foundry](https://ai.azure.com). The capacity calculator is under **Shared resources** > **Model Quota** > **Azure OpenAI Provisioned**.
 
@@ -63,34 +143,6 @@ The values in the output column are the estimated value of PTU units required fo
 > [!NOTE]
 > The capacity calculators provide an estimate based on simple input criteria. The most accurate way to determine your capacity is to benchmark a deployment with a representational workload for your use case.
 
-## Understanding the provisioned throughput purchase model
-
-Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned are purchased on-demand at an hourly basis based on the number of deployed PTUs, with substantial term discount available via the purchase of Azure Reservations.   
-
-The hourly model is useful for short-term deployment needs, such as validating new models or acquiring capacity for a hackathon.  However, the discounts provided by the Azure Reservation for Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned are considerable and most customers with consistent long-term usage will find a reserved model to be a better value proposition. 
-
-> [!NOTE]
-> Azure OpenAI Provisioned customers onboarded prior to the August self-service update use a purchase model called the Commitment model.  These customers can continue to use this older purchase model alongside the Hourly/reservation purchase model.  The Commitment model is not available for new customers or new models introduced after August 2024.  For details on the Commitment purchase model and options for coexistence and migration, please see the [Azure OpenAI Provisioned August Update](../concepts/provisioned-migration.md).
-## Hourly usage
-
-Provisioned, Data Zone Provisioned, and Global Provisioned deployments are charged an hourly rate ($/PTU/hr) on the number of PTUs that have been deployed.  For example, a 300 PTU deployment will be charged the hourly rate times 300.  All Azure OpenAI pricing is available in the Azure Pricing Calculator. 
-
-If a deployment exists for a partial hour, it will receive a prorated charge based on the number of minutes it was deployed during the hour.  For example, a deployment that exists for 15 minutes during an hour will receive 1/4th the hourly charge.  
-
-If the deployment size is changed, the costs of the deployment will adjust to match the new number of PTUs.   
-
-:::image type="content" source="../media/provisioned/hourly-billing.png" alt-text="A diagram showing hourly billing." lightbox="../media/provisioned/hourly-billing.png":::
-
-Paying for provisioned, data zoned provisioned, and global provisioned deployments on an hourly basis is ideal for short-term deployment scenarios.  For example: Quality and performance benchmarking of new models, or temporarily increasing PTU capacity to cover an event such as a hackathon.  
-
-Customers that require long-term usage of provisioned, data zoned provisioned, and global provisioned deployments, however, might pay significantly less per month by purchasing a term discount via Azure Reservations as discussed in the next section. 
-
-> [!NOTE]
-> It is not recommended to scale production deployments according to incoming traffic and pay for them purely on an hourly basis. There are two reasons for this:
-> * The cost savings achieved by purchasing Azure Reservations for Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned are significant, and it will be less expensive in many cases to maintain a deployment sized for full production volume paid for via a reservation than it would be to scale the deployment with incoming traffic.
-> * Having unused provisioned quota (PTUs) does not guarantee that capacity will be available to support an increase in the size of the deployment when required. Quota limits the maximum number of PTUs that can be deployed, but it is not a capacity guarantee. Provisioned capacity for each region and model dynamically changes throughout the day and might not be available when required. As a result, it is recommended to maintain a permanent deployment to cover your traffic needs (paid for via a reservation).
-> * Charges for deployments on a deleted resource will continue until the resource is purged.  To prevent this, delete a resource’s deployment before deleting the resource.  For more information, see [Recover or purge deleted Azure AI services resources](../../recover-purge-resources.md). 
-
 ## Azure Reservations for Azure OpenAI provisioned deployments
 
 Discounts on top of the hourly usage price can be obtained by purchasing an Azure Reservation for Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned. An Azure Reservation is a term-discounting mechanism shared by many Azure products. For example, Compute and Cosmos DB. For Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned, the reservation provides a discount in exchange for committing to payment for fixed number of PTUs for a one-month or one-year period.  
@@ -105,26 +157,26 @@ Discounts on top of the hourly usage price can be obtained by purchasing an Azur
 
     * All subscriptions in a billing account 
 
-* New reservations can be purchased to cover the same scope as existing reservations, to allow for discounting of new provisioned deployments.  The scope of existing reservations can also be updated at any time without penalty, for example to cover a new subscription. 
+* New reservations can be purchased to cover the same scope as existing reservations, to allow for discounting of new provisioned deployments. The scope of existing reservations can also be updated at any time without penalty, for example to cover a new subscription. 
 
 * Reservations for Global, Data Zone, and Regional deployments aren't interchangeable. You need to purchase a separate reservation for each deployment type. 
 
-* Reservations can be canceled after purchase, but credits are limited.   
+* Reservations can be canceled after purchase, but credits are limited.  
 
 * If the size of provisioned deployments within the scope of a reservation exceeds the amount of the reservation, the excess is charged at the hourly rate. For example, if deployments amounting to 250 PTUs exist within the scope of a 200 PTU reservation, 50 PTUs will be charged on an hourly basis until the deployment sizes are reduced to 200 PTUs, or a new reservation is created to cover the remaining 50. 
 
 * Reservations guarantee a discounted price for the selected term.  They don't reserve capacity on the service or guarantee that it will be available when a deployment is created. It's highly recommended that customers create deployments prior to purchasing a reservation to prevent from over-purchasing a reservation. 
 
 > [!IMPORTANT] 
-> * Capacity availability for model deployments is dynamic and changes frequently across regions and models.  To prevent you from purchasing a reservation for more PTUs than you can use, create deployments first, and then purchase the Azure Reservation to cover the PTUs you have deployed.  This best practice will ensure that you can take full advantage of the reservation discount and prevent you from purchasing a term commitment that you cannot use. 
+> * Capacity availability for model deployments is dynamic and changes frequently across regions and models. To prevent you from purchasing a reservation for more PTUs than you can use, create deployments first, and then purchase the Azure Reservation to cover the PTUs you have deployed. This best practice will ensure that you can take full advantage of the reservation discount and prevent you from purchasing a term commitment that you cannot use. 
 >
-> * The Azure role and tenant policy requirements to purchase a reservation are different than those required to create a deployment or Azure OpenAI resource.  Verify authorization to purchase reservations in advance of needing to do so. See Azure OpenAI [Provisioned reservation documentation](https://aka.ms/oai/docs/ptum-reservations) for more details.
+> * The Azure role and tenant policy requirements to purchase a reservation are different than those required to create a deployment or Azure OpenAI resource. Verify authorization to purchase reservations in advance of needing to do so. See Azure OpenAI [Provisioned reservation documentation](https://aka.ms/oai/docs/ptum-reservations) for more details.
 
 ## Important: sizing Azure OpenAI provisioned reservations
 
-The PTU amounts in reservation purchases are independent of PTUs allocated in quota or used in deployments. It's possible to purchase a reservation for more PTUs than you have in quota, or can deploy for the desired region, model, or version.   Credits for over-purchasing a reservation are limited, and customers must take steps to ensure they maintain their reservation sizes in line with their deployed PTUs.  
+The PTU amounts in reservation purchases are independent of PTUs allocated in quota or used in deployments. It's possible to purchase a reservation for more PTUs than you have in quota, or can deploy for the desired region, model, or version. Credits for over-purchasing a reservation are limited, and customers must take steps to ensure they maintain their reservation sizes in line with their deployed PTUs. 
  
-The best practice is to always purchase a reservation after deployments have been created.  This prevents purchasing a reservation and then finding out that the required capacity isn't available for the desired region or model. 
+The best practice is to always purchase a reservation after deployments have been created. This prevents purchasing a reservation and then finding out that the required capacity isn't available for the desired region or model. 
  
 
 Reservations for Global, Data Zone, and Regional deployments aren't interchangeable. You need to purchase a separate reservation for each deployment type.
@@ -135,7 +187,7 @@ To assist customers with purchasing the correct reservation amounts. The total n
 
 Managing Azure Reservations 
 
-After a reservation is created, it is a best practice monitor it to ensure it is receiving the usage you're expecting.  This can be done via the Azure Reservation Portal or Azure Monitor.  Details on these articles and others can be found here: 
+After a reservation is created, it is a best practice monitor it to ensure it is receiving the usage you're expecting. This can be done via the Azure Reservation Portal or Azure Monitor. Details on these articles and others can be found here: 
 
 * [View Azure reservation utilization](/azure/cost-management-billing/reservations/reservation-utilization) 
 * [View Azure Reservation purchase and refund transactions](/azure/cost-management-billing/reservations/view-purchase-refunds) 
````
</details>

### Summary

```json
{
    "modification_type": "major update",
    "modification_title": "プロビジョニングされたスループットユニットに関する追加情報"
}
```

### Explanation
この変更は、ファイル `provisioned-throughput-onboarding.md` に対する主要な修正で、内容が大幅に更新されています。主な目的は、プロビジョンされたスループットユニット（PTU）に関連するコストと請求についての理解を深めることです。記事のタイトルが「Azure OpenAI Service Provisioned Throughput Units (PTU) onboarding」から「Understanding costs associated with provisioned throughput units (PTU)」に変更され、コストに焦点を当てた内容へと再構成されています。

最も目立つ変更点は、新たに多数のセクションが追加されたことで、PTU の概念、請求モデル、そしてリザーブの利点について詳しく解説されています。具体的には、PTUの使用方法、請求方法、利用可能なリザーブの種類、その購入と管理についての指針が提供されています。

さらに、コスト計算に関する具体的な指示や例、さらにはプロビジョンされたスループットユニットの容量計算の手法が提供され、ユーザーが自分のニーズに基づいて最適なPTUの数を見積もる手助けが行われています。

著者情報や日付の更新もあり、最新の情報や責任者が明記されています。全体として、この記事はプロビジョンされたスループットユニットの利用を考えているユーザーに対し、より価値のある情報を提供する内容に進化しています。

## articles/ai-services/openai/how-to/working-with-models.md{#item-7ec098}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about managing model deployment life cycle, updates, & retirement.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 03/26/2025
+ms.date: 03/31/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, devx-track-azurepowershell
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -289,7 +289,7 @@ Provisioned deployments support distinct model management practices. Provisioned
 ### Prerequisites
 - Validate that the target model version or model family is supported for your existing deployment type. Migrations can only occur between provisioned deployments of the same deployment type. For more information on deployment types, review the [deployment type documentation](./deployment-types.md).
 - Validate capacity availability for your target model version or model family prior to attempting a migration. For more information on determining capacity availability, review the [capacity transparency documentation](../concepts/provisioned-throughput.md#capacity-transparency).
-- For multi-deployment migrations, validate that you have sufficient quota to support multiple deployments simultaneously. For more information on how to validate quota for each provisioned deployment type, review the [provisioned quota documentation](../concepts/provisioned-throughput.md#quota).
+- For multi-deployment migrations, validate that you have sufficient quota to support multiple deployments simultaneously. For more information on how to validate quota for each provisioned deployment type, review the [provisioned throughput cost documentation](../how-to/provisioned-throughput-onboarding.md).
 
 ### In-place migrations for provisioned deployments
 In-place migrations allow you to maintain the same provisioned deployment name and size while changing the model version or model family assigned to that deployment. With in-place migrations, Azure OpenAI Service takes care of migrating any existing traffic between model versions or model families throughout the migration over a 20-30 minute window. Throughout the migration window, your provisioned deployment will display an "updating" provisioned state. You can continue to use your provisioned deployment as you normally would. Once the in-place migration is complete, the provisioned state will be updated to "succeeded", indicating that all traffic has been migrated over to the target model version or model family. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マイグレーションに関するドキュメントリンクの修正"
}
```

### Explanation
この変更は、ファイル `working-with-models.md` に対する軽微な修正で、主にリンクの更新が行われています。日付が「2025年3月26日」から「2025年3月31日」に変更され、著者やサービスのメタデータに関する情報も少し修正されています。

具体的には、マイグレーションの段落において、マルチデプロイメントのマイグレーションに関する情報が更新され、従来の「provisioned quota documentation」リンクが「provisioned throughput cost documentation」リンクに修正されています。これにより、マイグレーションを行う際のクオータのテストに関する最新の情報にアクセスできるようになります。

この変更は、情報の正確性と利用者の利便性を向上させるための小規模な調整として位置付けられます。全体的に、ドキュメントは最新の情報が反映され、ユーザーがマイグレーションプロセスを理解しやすくなるよう配慮されています。

## articles/ai-services/openai/includes/assistants-python.md{#item-82d745}

<details>
<summary>Diff</summary>
````diff
@@ -44,8 +44,6 @@ pip install openai
 pip install azure-identity
 ```
 
-[!INCLUDE [Assistants v2 note](./assistants-v2-note.md)]
-
 > [!NOTE]
 > This library is maintained by OpenAI. Refer to the [release history](https://github.com/openai/openai-python/releases) to track the latest updates to the library.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アシスタントのV2に関する注意事項の削除"
}
```

### Explanation
この変更は、ファイル `assistants-python.md` における軽微な修正で、特定のコンテンツが削除されています。具体的には、アシスタントに関するV2の注記を含む行が削除されました。この変更により、ドキュメントはより簡潔になり、特定の情報が除外されましたが、他の重要な情報や注意事項はそのまま残されています。

具体的には、削除されたのは「[!INCLUDE [Assistants v2 note](./assistants-v2-note.md)]」という行で、これがなくなることで、アシスタントV2に関する追加情報の参照がなくなりました。それにもかかわらず、開発者が利用するべきライブラリに関するノートや、リリース履歴へのリンクは残されており、ユーザーが必要とする情報へのアクセスは保たれています。

この修正は、アシスタントに関連する情報を整理し、ドキュメントの明瞭さを向上させる意図があります。全体的には、ユーザーが必要なライブラリのインストール手順を理解しやすくするための小さな調整です。

## articles/ai-services/openai/includes/assistants-v2-note.md{#item-64ae04}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +0,0 @@
----
-manager: nitinme
-author: aahill
-ms.author: aahi
-ms.service: azure-ai-openai
-ms.topic: include
-ms.date: 04/22/2024
----
-
-> [!NOTE]
-> * [File search](../how-to/file-search.md) can ingest up to 10,000 files per assistant - 500 times more than before. It is fast, supports parallel queries through multi-threaded searches, and features enhanced reranking and query rewriting.
->     * Vector store is a new object in the API. Once a file is added to a vector store, it's automatically parsed, chunked, and embedded, made ready to be searched. Vector stores can be used across assistants and threads, simplifying file management and billing.
-> * We've added support for the `tool_choice` parameter which can be used to force the use of a specific tool (like file search, code interpreter, or a function) in a particular run.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "アシスタントV2に関するノートの削除"
}
```

### Explanation
この変更は、ファイル `assistants-v2-note.md` が完全に削除されたことを示しています。これにより、アシスタントV2に関する情報がドキュメントから消え、具体的には、以前提供されていたノートや重要な機能に関する解説が取り除かれました。

削除された内容には、ファイル検索機能の強化やそれに伴う新しいベクトルストアの導入、特定のツールを強制的に使用するための `tool_choice` パラメータが含まれていました。これらの情報は、アシスタントV2の利用者にとって価値のあるものであり、技術的な詳細や新機能の説明が欠落することになりました。

この変更は、ドキュメントの更新や再編成の一環かもしれませんが、ユーザーが重要な情報を失うリスクが伴います。従って、この削除は重大な変更と見なされる可能性があります。全体として、アシスタントに関する情報の透明性や明確さが損なわれることとなり、ユーザーの体験に影響を与えるかもしれません。

## articles/ai-services/openai/includes/use-your-data-studio.md{#item-705daf}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
 ms.topic: quickstart
 author: aahill
 ms.author: aahi
-ms.date: 02/12/2024
+ms.date: 03/31/2025
 recommendations: false
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データスタジオの最終更新日を変更"
}
```

### Explanation
この変更は、ファイル `use-your-data-studio.md` のメタデータの一部である最終更新日が変更されたことを示しています。具体的には、以前の更新日「2024年2月12日」が「2025年3月31日」に変更されました。この更新は、ドキュメントの最新性を保つために必要な調整として位置づけられます。

更新日を変更することにより、ユーザーはこのリソースがいつ作成または更新されたのかを理解しやすくなります。これにより、情報が古くなっているかどうかを判断する一助となります。全体的には、ドキュメントの信頼性や有用性を高めるための細かな調整であり、ユーザーの経験に良い影響を与えることが期待されます。

## articles/ai-services/openai/media/provisioned/deploy-model-button.png{#item-62cd49}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "モデルデプロイボタンの画像を追加"
}
```

### Explanation
この変更は、ファイル `deploy-model-button.png` が新たに追加されたことを示しています。この画像は、モデルデプロイに関連するボタンのビジュアルを提供し、ドキュメント内での視覚的補足として機能します。

画像の追加は、特にユーザーガイドやチュートリアルにおいて、視覚的なコンテキストを提供するために重要です。これにより、ユーザーはデプロイプロセスを理解しやすくなり、ボタンの位置や機能を視覚的に確認することができます。全体として、この変更はユーザー体験の向上に寄与し、より直感的なナビゲーションを可能にします。

## articles/ai-services/openai/media/provisioned/deployment-ptu-capacity-calculator.png{#item-aca8ed}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントPTUのキャパシティ計算機のファイル名を変更"
}
```

### Explanation
この変更は、画像ファイルの名前が変更されたことを示しています。具体的には、以前のファイル名 `deployment-ptu-capacity-calculator.png` が、新しいパス `articles/ai-services/openai/media/provisioned/deployment-ptu-capacity-calculator.png` に移動された結果、ファイル名の変更が行われました。

ファイル名の変更は、整理や構造的な改善の一環として実施されるものであり、特にドキュメント内やリポジトリ全体の整理を目的としています。この変更により、ユーザーは関連するコンテンツをより見つけやすくなり、資産の管理がしやすくなることが期待されます。全体として、この変更は、リソースの整合性と可用性を向上させるための小規模な調整と見なされます。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -237,14 +237,14 @@ items:
         href: ./how-to/dynamic-quota.md
       - name: Monitor Azure OpenAI
         href: ./how-to/monitor-openai.md
-      - name: Onboarding to Provisioned Throughput Units (PTU)
-        href: ./how-to/provisioned-throughput-onboarding.md
-        displayName: PTU, provisioned, provisioned throughput units
       - name: Provisioned throughput units (PTU)
         items:
         - name: What is the Provisioned Managed offering (PTU)?
           href: ./concepts/provisioned-throughput.md
           displayName: PTU, provisioned, provisioned throughput units
+        - name: Understanding and calculating PTU costs 
+          href: ./how-to/provisioned-throughput-onboarding.md
+          displayName: PTU, provisioned, provisioned throughput units
         - name: Get started with Provisioned Deployments
           href: ./how-to/provisioned-get-started.md
           displayName: PTU, provisioned, provisioned throughput units
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCファイルの修正"
}
```

### Explanation
この変更は、`toc.yml` ファイルが修正されたことを示しています。具体的には、いくつかの項目が追加または削除され、全体の構造が見直されています。変更内容には、Provisioned Throughput Units (PTU) に関する情報の整理や新たなリンクの追加が含まれています。

特に、「Onboarding to Provisioned Throughput Units (PTU)」の項目が削除され、新たに「Understanding and calculating PTU costs」という項目が追加されました。この変更は、ユーザーが関連情報にアクセスしやすくするための改善を意図しており、より効率的なナビゲーションを可能にする役割を果たします。

全体として、TOC（目次）ファイルの改善により、利用者は必要な情報に迅速にたどり着けるようになり、文書の整合性が向上します。


