---
date: '2025-06-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:45b2d74...MicrosoftDocs:c6cc5fa
summary: この更新では、Azure OpenAI関連のドキュメントがAzure AI Foundryに基づいて更新され、日付やリンクが改訂されました。また、新しい画像が追加され、一部の画像が更新されています。用語の修正も行われ、ドキュメントの一貫性が保たれています。特にビジュアル的な資料の追加により、ユーザーがデプロイやクォータに関する概念を理解しやすくなっています。全体として、一貫性と明確さが強化され、ユーザーの体験が向上することが期待されます。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:45b2d74...MicrosoftDocs:c6cc5fa){target="_blank"}

<format>
# Highlights
この更新では、Azure OpenAIの関連ドキュメントがAzure AI Foundryに基づくものに逐次更新され、各種ドキュメントの日付とリンクが改訂されています。また、新しい画像が追加され、一部画像の更新が行われています。新たな概念や用語の修正がいくつか含まれています。

## New features
- `deepseek-deployment.png` および `fungible-quota.png` といった視覚的な資料の追加により、ユーザーがデプロイやクォータに関する概念を理解しやすくなっています。

## Breaking changes
- 破壊的な変更は特にありませんが、用語の置き換えやリンクの更新により一貫性が保持されています。

## Other updates
- 多くのドキュメントで日付が更新され、情報の最新性が確保されています。
- 各ドキュメント内でAzure OpenAIからAzure AI Foundryへの名称とリンク更新が行われています。
- 既存の画像の多くが刷新され、視覚的な情報伝達が強化されています。

# Insights
今回の更新では、Azure AI Foundryへの移行を意識した大規模なドキュメント整備が中心となっています。特に最新の技術やサービス名への適応が意識され、ユーザーが新しいプラットフォームやデプロイメントタイプをより正確に理解し、利用できるようになっています。日付の更新やリンクの修正は、利用者が常に最新の情報にアクセスできるように整備されています。

新たに追加された画像ファイルによって、複雑な概念を視覚的にサポートする取り組みがなされています。これにより、技術的な情報が視覚的に確認できるため、理解しやすくなっています。

全体を通して、ドキュメントの一貫性と明確さが改訂の主眼となっており、特にビジュアルの強化が顕著です。この結果、ユーザーの体験とAIサービスの利用理解が大幅に向上すると期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [gov-provisioned.md](#item-753c19) | minor update | 日付とリンクの更新: 政府が提供する Azure OpenAI の概念 | modified | 2 | 2 | 4 | 
| [provisioned-migration.md](#item-68e143) | minor update | 日付とリンクの更新: プロビジョニング移行ガイド | modified | 4 | 4 | 8 | 
| [provisioned-throughput.md](#item-022e0c) | minor update | プロビジョニングスループットガイドの更新 | modified | 100 | 37 | 137 | 
| [deployment-types.md](#item-210814) | minor update | デプロイメントタイプガイドの更新 | modified | 24 | 22 | 46 | 
| [fine-tuning-deploy.md](#item-286d57) | minor update | ファインチューニングデプロイガイドの用語変更 | modified | 4 | 4 | 8 | 
| [provisioned-get-started.md](#item-c8df1c) | minor update | プロビジョニングデプロイメントのガイドライン更新 | modified | 54 | 30 | 84 | 
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | プロビジョンドスループットのオンボーディングガイドを更新 | modified | 36 | 36 | 72 | 
| [provisioned-global.md](#item-340884) | minor update | グローバルプロビジョンドモデルの可用性を更新 | modified | 29 | 31 | 60 | 
| [available-quota.png](#item-439bf9) | minor update | 利用可能なクォータ画像を更新 | modified | 0 | 0 | 0 | 
| [deepseek-deployment.png](#item-20d652) | new feature | DeepSeekデプロイメント画像の追加 | added | 0 | 0 | 0 | 
| [deployment-screen.png](#item-5bc2ef) | minor update | デプロイメントスクリーン画像の更新 | modified | 0 | 0 | 0 | 
| [fungible-quota.png](#item-2f93fd) | new feature | ファンジブルクォータ画像の追加 | added | 0 | 0 | 0 | 
| [model-independent-quota.png](#item-29a034) | minor update | モデル非依存クォータ画像の更新 | modified | 0 | 0 | 0 | 
| [ptu-quota-page.png](#item-aedb7d) | minor update | PTUクォータページ画像の更新 | modified | 0 | 0 | 0 | 
| [toc.yml](#item-c945af) | minor update | PTUの用語修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/gov-provisioned.md{#item-753c19}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: challenp
 ms.service: azure-ai-openai
 ms.topic: how-to
 ms.custom: references_regions, azuregovernment
-ms.date: 5/1/2025
+ms.date: 05/30/2025
 recommendations: false
 ---
 
@@ -84,7 +84,7 @@ In addition to the updates for the hourly payment model, new [Azure Reservations
 
 #### Supported models on commitment payment model:
 
-Only the following list of Azure OpenAI models are supported in Commitments. For onboarding any other models that aren't in the list below, or any newer models on provisioned throughput offering, refer to the [Azure OpenAI provisioned onboarding guide](../how-to/provisioned-throughput-onboarding.md) and [Azure Reservations for Azure OpenAI provisioned deployments](../how-to/provisioned-throughput-onboarding.md#azure-reservations-for-azure-openai-provisioned-deployments)
+Only the following list of Azure OpenAI models are supported in Commitments. For onboarding any other models that aren't in the list below, or any newer models on provisioned throughput offering, refer to the [Azure OpenAI provisioned onboarding guide](../how-to/provisioned-throughput-onboarding.md) and [Azure Reservations for Azure OpenAI provisioned deployments](../how-to/provisioned-throughput-onboarding.md#azure-reservations-for-azure-ai-foundry-provisioned-throughput)
     
 |Supported models on Commitment plan |Versions|
 |-|-|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付とリンクの更新: 政府が提供する Azure OpenAI の概念"
}
```

### Explanation
このコードの変更では、`gov-provisioned.md` ファイルに関して、日付の変更とリンクの更新が行われました。具体的には、`ms.date` フィールドの値が「5/1/2025」から「05/30/2025」に更新されました。また、Azure OpenAI モデルのサポートに関する記述も修正され、リンクの一部が「…#azure-reservations-for-azure-ai-foundry-provisioned-throughput」に変更されています。この更新は、文書の正確性を向上させるためのものであり、特定の日付と関連するリソースへのアクセス向上を目的としています。

## articles/ai-services/openai/concepts/provisioned-migration.md{#item-68e143}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-openai
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 03/26/2025
+ms.date: 05/30/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -44,7 +44,7 @@ This article is intended for existing users of the provisioned throughput offeri
 | Default provisioned-managed quota in many regions | Get started quickly in new regions without having to first request quota. |
 | Flexible choice of payment model for existing provisioned customers | Customers with commitments can stay on the commitment model until the end of life of the currently supported models, and can choose to migrate existing commitments to hourly/reservations via managed process. We recommend migrating to hourly/ reservations to take advantage of term discounts and to work with the latest models. |
 | Supports latest model generations | The latest models are available only on hourly/ reservations in provisioned offering. |
-| Differentiated pricing | Greater flexibility and control of pricing and performance. In December 2024, we introduced  differentiated hourly pricing across [global provisioned](../how-to/deployment-types.md#global-provisioned), [data zone provisioned](../how-to/deployment-types.md#data-zone-provisioned), and [provisioned](../how-to/deployment-types.md#provisioned) deployment types with the option to purchase [Azure Reservations](#new-azure-reservations-for-global-and-data-zone-provisioned-deployments) to support additional discounts. For more information on the hourly price for each provisioned deployment type, see the [Pricing details](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) page. |
+| Differentiated pricing | Greater flexibility and control of pricing and performance. In December 2024, we introduced  differentiated hourly pricing across [global provisioned](../how-to/deployment-types.md#global-provisioned), [data zone provisioned](../how-to/deployment-types.md#data-zone-provisioned), and [regional provisioned](../how-to/deployment-types.md#regional-provisioned) deployment types with the option to purchase [Azure Reservations](#new-azure-reservations-for-global-and-data-zone-provisioned-deployments) to support additional discounts. For more information on the hourly price for each provisioned deployment type, see the [Pricing details](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) page. |
 
 ## Usability improvement details
 
@@ -81,7 +81,7 @@ We also recommend that customers using commitments now create their deployments
 See the following links for more information. The guidance for reservations and commitments is the same:
 
 * [Capacity Transparency](#self-service-migration)
-* [Sizing reservations](../how-to/provisioned-throughput-onboarding.md#important-sizing-azure-openai-provisioned-reservations)
+* [Sizing reservations](../how-to/provisioned-throughput-onboarding.md#important-sizing-azure-ai-foundry-provisioned-throughput-reservation)
 
 ## New hourly reservation payment model
 
@@ -112,7 +112,7 @@ In addition to the updates for the hourly payment model, in December 2024 new [A
 - Commitments can't be canceled or altered during their term, except to add new PTUs.
 
 #### Supported models on commitment payment model:
-  Only the following list of Azure OpenAI models are supported in Commitments. For onboarding any other models that aren't in the list below, or any newer models on provisioned throughput offering,  refer to the [Azure OpenAI provisioned onboarding guide](../how-to/provisioned-throughput-onboarding.md) and [Azure Reservations for Azure OpenAI provisioned deployments](../how-to/provisioned-throughput-onboarding.md#azure-reservations-for-azure-openai-provisioned-deployments)
+  Only the following list of Azure OpenAI models are supported in Commitments. For onboarding any other models that aren't in the list below, or any newer models on provisioned throughput offering,  refer to the [Azure OpenAI provisioned onboarding guide](../how-to/provisioned-throughput-onboarding.md) and [Azure Reservations for Azure OpenAI provisioned deployments](../how-to/provisioned-throughput-onboarding.md#azure-reservations-for-azure-ai-foundry-provisioned-throughput)
     
 |Supported models on Commitment plan |Versions|
 |-|-|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付とリンクの更新: プロビジョニング移行ガイド"
}
```

### Explanation
この変更では、`provisioned-migration.md` ファイルにおいて、主に2つの修正が行われました。一つ目は、`ms.date` フィールドの更新です。以前は「03/26/2025」となっていましたが、「05/30/2025」に変更されました。二つ目は、いくつかのリンクの修正です。特に、Azure OpenAI 提供に関連する情報のリンクが更新され、一部の文言が新しいモデルに合わせて調整されました。このような修正は、資料の正確性と最新の情報を提供するためのものであり、ユーザーがよりスムーズに必要な情報にアクセスできるようにすることを目的としています。

## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -1,51 +1,81 @@
 ---
-title: Azure OpenAI in Azure AI Foundry Models provisioned throughput
-description: Learn about provisioned throughput and Azure OpenAI.
+title: Provisioned throughput for Azure AI Foundry Models
+description: Learn about provisioned throughput and Azure AI Foundry.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 04/30/2025
+ms.date: 06/03/2025
 manager: nitinme
 author: aahill #ChrisHMSFT
 ms.author: aahi #chrhoder
+ms.reviewer: shiyingfu
+reviewer: swingfu
 recommendations: false
 ---
 
 # What is provisioned throughput?
 
 > [!NOTE]
-> If you're looking for what's recently changed with the provisioned throughput offering, see the [update article](./provisioned-migration.md) for more information.
+> For more information on recent changes to the provisioned throughput offering, see the [update article](./provisioned-migration.md) for more information.
 
-The provisioned throughput offering is a model deployment type that allows you to specify the amount of throughput you require in a model deployment. Azure OpenAI then allocates the necessary model processing capacity and ensures it's ready for you. Provisioned throughput provides:
+The Azure AI Foundry provisioned throughput offering is a model deployment type that allows you to specify the amount of throughput you require in a model deployment. Azure AI Foundry then allocates the necessary model processing capacity and ensures it's ready for you. You can use the provisioned throughput you requested across a diverse portfolio of [models that are sold directly by Azure](../../../ai-foundry/concepts/foundry-models-overview.md#models-sold-directly-by-azure). These models include Azure OpenAI models and newly introduced flagship model families like Azure DeepSeek, Azure Grok, Azure Llama, and more within Azure AI Foundry Models.
 
-- **Predictable performance:** stable max latency and throughput for uniform workloads.
+Provisioned throughput provides:
+
+- **A boarder model choice** on the latest flagship models
+- **Flexibility** to switch models and deployments with given provisioned throughput quota
+- **Significant discounts** and the ability to boost your reservation utilization with a more flexible reservation choice
+- **Predictable performance**, by providing stable max latency and throughput for uniform workloads.
 - **Allocated processing capacity:** A deployment configures the amount of throughput. Once deployed, the throughput is available whether used or not.
 - **Cost savings:** High throughput workloads might provide cost savings vs token-based consumption.
 
 > [!TIP]
-> * You can take advantage of additional cost savings when you buy [Microsoft Azure OpenAI in Azure AI Foundry Models reservations](/azure/cost-management-billing/reservations/azure-openai#buy-a-microsoft-azure-openai-service-reservation).
-> * Provisioned throughput is available as the following deployment types: [global provisioned](../how-to/deployment-types.md#global-provisioned), [data zone provisioned](../how-to/deployment-types.md#data-zone-provisioned) and [standard provisioned](../how-to/deployment-types.md#provisioned).
+> * You can take advantage of more cost savings when you buy [Microsoft Azure AI Foundry Provisioned Throughput reservations](/azure/cost-management-billing/reservations/azure-openai#buy-a-microsoft-azure-openai-service-reservation).
+> * Provisioned throughput is available as the following deployment types: [global provisioned](../how-to/deployment-types.md#global-provisioned), [data zone provisioned](../how-to/deployment-types.md#data-zone-provisioned) and [regional provisioned](../how-to/deployment-types.md#regional-provisioned).
+
 
 <!--
 Throughput is defined in terms of provisioned throughput units (PTU) which is a normalized way of representing the throughput for your deployment. Each model-version pair requires different amounts of PTU to deploy, and provides different amounts of throughput per PTU. 
 
 An Azure OpenAI deployment is a unit of management for a specific OpenAI Model. A deployment provides customer access to a model for inference and using features, such as [content moderation](content-filter.md). 
 -->
 
+
 ## When to use provisioned throughput
 
-You should consider switching from standard deployments to provisioned managed deployments when you have well-defined, predictable throughput and latency requirements. Typically, this occurs when the application is ready for production or has already been deployed in production and there's an understanding of the expected traffic. This allows users to accurately forecast the required capacity and avoid unexpected billing. Provisioned managed deployments are also useful for applications that have real-time/latency sensitive requirements.
+You should consider switching from standard deployments to provisioned throughput deployments when you have well-defined, predictable throughput and latency requirements. Typically, this occurs when the application is ready for production or is already deployed in production and there's an understanding of the expected traffic. This allows users to accurately forecast the required capacity and avoid unexpected billing. Provisioned Throughput deployments are also useful for applications that have real-time/latency sensitive requirements.
 
 ## Key concepts
+The sections that follow describe key concepts that you should be aware of when using the provisioned throughput offering.
 
 ### Provisioned Throughput Units (PTU)
 
-Provisioned throughput units (PTUs) are generic units of model processing capacity that you can use to size provisioned deployments to achieve the required throughput for processing prompts and generating completions. Provisioned throughput units are granted to a subscription as quota, and used to define costs. Each quota is specific to a region and defines the maximum number of PTUs that can be assigned to deployments in that subscription and region. For information about the costs associated with the provision managed offering and PTUs, see [Understanding costs associated with PTU](../how-to/provisioned-throughput-onboarding.md).
+Provisioned throughput units (PTU) are generic units of model processing capacity that you can use to size provisioned deployments to achieve the required throughput for processing prompts and generating completions. Provisioned throughput units are granted to a subscription as quota, and used to define costs. Each quota is specific to a region and defines the maximum number of PTU that can be assigned to deployments in that subscription and region.
+
+#### Cost management under shared PTU reservation
+
+You can use the PTU capability to seamlessly manage costs for Foundry Models under a shared PTU reservation. However, the required PTU units for deployment and throughput performance are dynamically tailored to the chosen models. To learn more about PTU costs and model latency points, see [Understanding costs associated with PTU](../how-to/provisioned-throughput-onboarding.md).
+
+Existing PTU reservations are automatically upgraded to empower customers with enhanced efficiency and cost savings as they deploy Foundry Models. For example, suppose you have an existing PTU reservation with 500 PTU purchased. You use 300 units for Azure OpenAI models, and you choose to also use PTU to deploy Azure DeepSeek, Azure Llama, or other models with PTU capability on Foundry Models.
+
+- If you use the remaining 200 PTU for DeepSeek-R1, the 200 PTU share the reservation discount automatically, and your total usage for the reservation is 500 PTU. 
+
+- If you use 300 PTU for DeepSeek-R1, then 200 PTU share the reservation discount automatically while 100 PTU exceed the reservation and are charged with DeepSeek-R1's hourly rate.  
+
+To learn about saving costs with PTU reservations, see [Save costs with Microsoft Azure AI Foundry Provisioned Throughput Reservations](/azure/cost-management-billing/reservations/azure-openai).
 
 ### Deployment types
 
-When creating a provisioned deployment in Azure AI Foundry, the deployment type on the Create Deployment dialog can be set to the Global Provisioned-Managed, DataZone Provisioned-Managed, or regional Provisioned-Managed deployment type depending on the data processing needs for the given workload.
+When you're creating a provisioned deployment in Azure AI Foundry, the deployment type on the "Create Deployment" dialog can be set to the Global Provisioned Throughput, Data Zone Provisioned Throughput, or Regional Provisioned Throughput deployment type depending on the data processing needs for the given workload.
 
-When creating a provisioned deployment in Azure OpenAI via CLI or API, the `sku-name` can be set to `GlobalProvisionedManaged`, `DataZoneProvisionedManaged`, or `ProvisionedManaged` depending on the data processing need for the given workload. To adapt the Azure CLI example command below to a different deployment type, simply update the `sku-name` parameter to match the deployment type you wish to deploy.
+When you're creating a provisioned deployment in Azure AI Foundry via CLI or API, the `sku-name` can be set to `GlobalProvisionedManaged`, `DataZoneProvisionedManaged`, or `ProvisionedManaged` depending on the data processing need for the given workload.
+
+| **Deployment Type** | **sku-name in CLI** |
+|----------|----------|
+| Global Provisioned Throughput | GlobalProvisionedManaged    |
+| Data Zone Provisioned Throughput | DataZoneProvisionedManaged    |
+| Regional Provisioned Throughput | ProvisionedManaged    |
+
+To adapt the following Azure CLI example command to a different deployment type, update the `sku-name` parameter to match the deployment type you wish to deploy. 
 
 ```azurecli
 az cognitiveservices account deployment create \
@@ -61,26 +91,26 @@ az cognitiveservices account deployment create \
 
 ### Capacity transparency
 
-Azure OpenAI is a highly sought-after service where customer demand might exceed service GPU capacity. Microsoft strives to provide capacity for all in-demand regions and models, but selling out a region is always a possibility. This constraint can limit some customers' ability to create a deployment of their desired model, version, or number of PTUs in a desired region - even if they have quota available in that region. Generally speaking:
+The models sold directly by Azure are highly sought-after services where customer demand might exceed service GPU capacity. Microsoft strives to provide capacity for all in-demand regions and models, but selling out a region is always a possibility. This constraint can limit some customers' ability to create a deployment of their desired model, version, or number of PTU in a desired region - even if they have quota available in that region. Generally speaking:
 
-- Quota places a limit on the maximum number of PTUs that can be deployed in a subscription and region, and does not guarantee of capacity availability.
-- Capacity is allocated at deployment time and is held for as long as the deployment exists.  If service capacity is not available, the deployment will fail
-- Customers use real-time information on quota/capacity availability to choose an appropriate region for their scenario with the necessary model capacity
-- Scaling down or deleting a deployment releases capacity back to the region.  There is no guarantee that the capacity will be available should the deployment be scaled up or re-created later.
+- Quota places a limit on the maximum number of PTU that can be deployed in a subscription and region, and doesn't guarantee capacity availability.
+- Capacity is allocated at deployment time and is held for as long as the deployment exists. If service capacity isn't available, the deployment fails.
+- Customers use real-time information on quota/capacity availability to choose an appropriate region for their scenario with the necessary model capacity.
+- Scaling down or deleting a deployment releases capacity back to the region. There's no guarantee that the capacity will be available should the deployment be scaled up or re-created later.
 
 #### Regional capacity guidance
 
 To find the capacity needed for their deployments, use the capacity API or the Azure AI Foundry deployment experience to provide real-time information on capacity availability.
 
-In Azure AI Foundry, the deployment experience identifies when a region lacks the capacity needed to deploy the model. This looks at the desired model, version and number of PTUs. If capacity is unavailable, the experience directs users to a select an alternative region.
+In Azure AI Foundry, the deployment experience identifies when a region lacks the capacity needed to deploy the model. This looks at the desired model, version, and number of PTU. If capacity is unavailable, the experience directs users to select an alternative region.
 
-Details on the deployment experience can be found in the Azure OpenAI [Provisioned get started guide](../how-to/provisioned-get-started.md).
+Details on the deployment experience can be found in the Azure AI Foundry [Provisioned get started guide](../how-to/provisioned-get-started.md).
 
 The [model capacities API](/rest/api/aiservices/accountmanagement/model-capacities/list?view=rest-aiservices-accountmanagement-2024-04-01-preview&tabs=HTTP&preserve-view=true) can be used to programmatically identify the maximum sized deployment of a specified model.  The API considers both your quota and service capacity in the region.
 
-If an acceptable region isn't available to support the desire model, version and/or PTUs, customers can also try the following steps:
+If an acceptable region isn't available to support the desired model, version, and/or PTU, customers can also try the following steps:
 
-- Attempt the deployment with a smaller number of PTUs.
+- Attempt the deployment with a smaller number of PTU.
 - Attempt the deployment at a different time. Capacity availability changes dynamically based on customer demand and more capacity might become available later.
 - Ensure that quota is available in all acceptable regions. The [model capacities API](/rest/api/aiservices/accountmanagement/model-capacities/list?view=rest-aiservices-accountmanagement-2024-04-01-preview&tabs=HTTP&preserve-view=true) and Azure AI Foundry experience consider quota availability in returning alternative regions for creating a deployment.
 
@@ -92,18 +122,18 @@ The [Provisioned-Managed Utilization V2 metric](../how-to/monitoring.md#azure-op
 
 Provisioned deployments provide you with an allocated amount of model processing capacity to run a given model.
 
-In all provisioned deployment types, when capacity is exceeded, the API will return a 429 HTTP Status Error. This fast response enables the user to make decisions on how to manage their traffic. Users can redirect requests to a separate deployment, to a standard deployment instance, or use a retry strategy to manage a given request. The service continues to return the 429 HTTP status code until the utilization drops below 100%.
+In all provisioned deployment types, when capacity is exceeded, the API returns a 429 HTTP Status Error. The fast response enables the user to make decisions on how to manage their traffic. Users can redirect requests to a separate deployment, to a standard deployment instance, or use a retry strategy to manage a given request. The service continues to return the 429 HTTP status code until the utilization drops below 100%.
 
 #### What should  I do when I receive a 429 response?
-The 429 response isn't an error, but instead part of the design for telling users that a given deployment is fully utilized at a point in time. By providing a fast-fail response, you have control over how to handle these situations in a way that best fits your application requirements.
+The 429 response isn't an error, but instead, it's part of the design for telling users that a given deployment is fully utilized at a point in time. By providing a fast-fail response, you have control over how to handle these situations in a way that best fits your application requirements.
 
 The  `retry-after-ms` and `retry-after` headers in the response tell you the time to wait before the next call will be accepted. How you choose to handle this response depends on your application requirements. Here are some considerations:
 -    You can consider redirecting the traffic to other models, deployments, or experiences. This option is the lowest-latency solution because the action can be taken as soon as you receive the 429 signal. For ideas on how to effectively implement this pattern see this [community post](https://github.com/Azure/aoai-apim).
--    If you're okay with longer per-call latencies, implement client-side retry logic. This option gives you the highest amount of throughput per PTU. The Azure OpenAI client libraries include built-in capabilities for handling retries.
+-    If you're okay with longer per-call latencies, implement client-side retry logic. This option gives you the highest amount of throughput per PTU. The Azure AI Foundry client libraries include built-in capabilities for handling retries.
 
 #### How does the service decide when to send a 429?
 
-In all provisioned deployment types, each request is evaluated individually according to its prompt size, expected generation size, and model to determine its expected utilization. This is in contrast to standard deployments, which have a [custom rate limiting behavior](../how-to/quota.md) based on the estimated traffic load. For standard deployments this can lead to HTTP 429 errors being generated prior to defined quota values being exceeded if traffic is not evenly distributed.
+In all provisioned deployment types, each request is evaluated individually according to its prompt size, expected generation size, and model, to determine its expected utilization. This behavior is in contrast to standard deployments, which have a [custom rate limiting behavior](../how-to/quota.md) based on the estimated traffic load. For standard deployments, this custom rate limiting behavior can lead to HTTP 429 errors being generated before defined quota values are exceeded if traffic isn't evenly distributed.
 
 For provisioned deployments, we use a variation of the leaky bucket algorithm to maintain utilization below 100% while allowing some burstiness in the traffic. The high-level logic is as follows:
 
@@ -112,18 +142,18 @@ For provisioned deployments, we use a variation of the leaky bucket algorithm to
 
     a.    When the current utilization is above 100%, the service returns a 429 code with the `retry-after-ms` header set to the time until utilization is below 100%
    
-    b.    Otherwise, the service estimates the incremental change to utilization required to serve the request by combining the prompt tokens, less any cached tokens, and the specified `max_tokens` in the call. A customer can receive up to a 100% discount on their prompt tokens depending on the size of their cached tokens. If the `max_tokens` parameter is not specified, the service estimates a value. This estimation can lead to lower concurrency than expected when the number of actual generated tokens is small. For highest concurrency, ensure that the `max_tokens` value is as close as possible to the true generation size.
+    b.    Otherwise, the service estimates the incremental change to utilization required to serve the request by combining the prompt tokens, less any cached tokens, and the specified `max_tokens` in the call. A customer can receive up to a 100% discount on their prompt tokens depending on the size of their cached tokens. If the `max_tokens` parameter isn't specified, the service estimates a value. This estimation can lead to lower concurrency than expected when the number of actual generated tokens is small. For highest concurrency, ensure that the `max_tokens` value is as close as possible to the true generation size.
    
 1. When a request finishes, we now know the actual compute cost for the call. To ensure an accurate accounting, we correct the utilization using the following logic:
 
    a.    If the actual > estimated, then the difference is added to the deployment's utilization.
    
    b.    If the actual < estimated, then the difference is subtracted.
    
-1. The overall utilization is decremented down at a continuous rate based on the number of PTUs deployed. 
+1. The overall utilization is decremented at a continuous rate based on the number of PTU deployed. 
 
 > [!NOTE]
-> Calls are accepted until utilization reaches 100%. Bursts just over 100% may be permitted in short periods, but over time, your traffic is capped at 100% utilization.
+> Calls are accepted until utilization reaches 100%. Bursts just over 100% might be permitted in short periods, but over time, your traffic is capped at 100% utilization.
 
 
 :::image type="content" source="../media/provisioned/utilization.jpg" alt-text="Diagram showing how subsequent calls are added to the utilization." lightbox="../media/provisioned/utilization.jpg":::
@@ -132,23 +162,56 @@ For provisioned deployments, we use a variation of the leaky bucket algorithm to
 
 The number of concurrent calls you can achieve depends on each call's shape (prompt size, `max_tokens` parameter, etc.). The service continues to accept calls until the utilization reaches 100%. To determine the approximate number of concurrent calls, you can model out the maximum requests per minute for a particular call shape in the [capacity calculator](https://ai.azure.com/resource/calculator). If the system generates less than the number of output tokens set for the `max_tokens` parameter, then the provisioned deployment will accept more requests.
 
-## What models and regions are available for provisioned throughput?
 
-# [Global Provisioned Managed](#tab/global-ptum)
+## Provisioned throughput capability for Models Sold Directly by Azure  
+
+This section lists Foundry Models that support the provisioned throughput capability. You can use your PTU quota and PTU reservation across the models shown in the table. 
+
+The following points are some important takeaways from the table:
+
+- The model version isn't included in this table. Check the version supported for each model when you choose the deployment option in the Azure AI Foundry portal. 
+
+- Regional provisioned throughput deployment option varies by region.  
+
+- New models sold directly by Azure are onboarded with Global provisioned throughput deployment option first. The Data zone provisioned option comes later.  
+
+- PTU are managed regionally and by offer type. PTU quota and any reservations must be in the region and shape (Global, Data zone, Regional) you wish to use. 
+
+- Spillover is an optional capability that manages traffic fluctuations on provisioned deployments. For more information on spillover, see [Manage traffic with spillover for provisioned deployments (Preview)](../how-to/spillover-traffic-management.md).
+
+| Model Family       | Model name       | Global provisioned | Data zone provisioned | Regional provisioned | Spillover feature |
+|--------------------|------------------|--------------------|-----------------------|----------------------|-------------------|
+| **Azure OpenAI**   | Gpt4.1           | ✅                 | ✅                     | ✅                   | ✅                 |
+|                    | Gpt 4.1 mini     | ✅                 | ✅                     | ✅                   | ✅                 |
+|                    | Gpt 4.1 nano     | ✅                 | ✅                     | ✅                   | ✅                 |
+|                    | Gpt 4o           | ✅                 | ✅                     | ✅                   | ✅                 |
+|                    | Gpt 4o mini      | ✅                 | ✅                     | ✅                   | ✅                 |
+|                    | Gpt 3.5 Turbo    | ✅                 | ✅                     | ✅                   | ✅                 |
+|                    | o1               | ✅                 | ✅                     | ✅                   | ✅                 |
+|                    | O3 mini          | ✅                 | ✅                     | ✅                   | ✅                 |
+|                    | O4 mini          | ✅                 | ✅                     | ✅                   | ✅                 |
+| **Azure DeepSeek** | DeepSeek-R1      | ✅                 |                       |                      |                   |
+|                    | DeepSeek-V3-0324 | ✅                 |                       |                      |                   |
+
+
+
+### Region availability for provisioned throughput capability
+
+# [Global Provisioned Throughput](#tab/global-ptum)
 
-### Global provisioned managed model availability
+#### Global provisioned Throughput model availability
 
 [!INCLUDE [Provisioned Managed Global](../includes/model-matrix/provisioned-global.md)]
 
-# [Data Zone Provisioned Managed](#tab/datazone-provisioned-managed)
+# [Data Zone Provisioned Throughput](#tab/datazone-provisioned-managed)
 
-### Data zone provisioned managed model availability
+#### Data Zone provisioned Throughput model availability
 
 [!INCLUDE [Global data zone provisioned managed](../includes/model-matrix/datazone-provisioned-managed.md)]
 
-# [Provisioned Managed](#tab/provisioned)
+# [Regional Provisioned Throughput](#tab/provisioned)
 
-### Provisioned deployment model availability
+#### Regional Provisioned Throughput deployment model availability
 
 [!INCLUDE [Provisioned](../includes/model-matrix/provisioned-models.md)]
 
@@ -157,7 +220,7 @@ The number of concurrent calls you can achieve depends on each call's shape (pro
 > [!NOTE]
 > The provisioned version of `gpt-4` **Version:** `turbo-2024-04-09` is currently limited to text only.
 
-## Next steps
+## Related content
 
 - [Learn about the onboarding steps for provisioned deployments](../how-to/provisioned-throughput-onboarding.md)
-- [Provisioned Throughput Units (PTU) getting started guide](../how-to//provisioned-get-started.md)
+- [Provisioned Throughput Units (PTU) getting started guide](../how-to//provisioned-get-started.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングスループットガイドの更新"
}
```

### Explanation
この変更では、`provisioned-throughput.md` ファイルに大規模な改訂が行われ、内容が更新されました。主な変更点には、文書のタイトルと説明が変更され、新しい日付「06/03/2025」が設定されました。また、Azure AI Foundry モデルに関する情報が追加され、プロビジョニングスループットの機能が強化されました。

具体的には、プロビジョニングスループットの利点が明確に設計され、導入された新しいモデルに関する詳細が提供されています。さらに、プロビジョニングスループットユニット（PTU）の概念に関する情報が強化され、コスト管理の仕組みや、異なるデプロイメントタイプに関するガイドラインが明確化されました。これらの変更は、ユーザーがより良い理解を持って Azure AI Foundry の機能を利用できるようにすることを目的としています。

## articles/ai-services/openai/how-to/deployment-types.md{#item-210814}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
-title: Understanding Azure OpenAI in Azure AI Foundry Models deployment types
-description: Learn how to use Azure OpenAI deployment types | Global-Standard | Standard | Provisioned.
+title: Understanding Azure AI Foundry Models deployment types
+description: Learn how to use Azure AI Foundry deployment types | Global-Standard | Standard | Provisioned.
 author: mrbullwinkle
 ms.author: mbullwin
 manager: nitinme
@@ -11,9 +11,11 @@ ms.custom:
   - build-2025
 ---
 
-# Azure OpenAI deployment types
+# Deployment types for Azure AI Foundry Models
 
-Azure OpenAI provides customers with choices on the hosting structure that fits their business and usage patterns. The service offers two main types of deployments: **standard** and **provisioned**. For a given deployment type, customers can align their workloads with their data processing requirements by choosing an Azure geography (`Standard` or `Provisioned-Managed`), Microsoft specified data zone (`DataZone-Standard` or `DataZone Provisioned-Managed`), or Global (`Global-Standard` or `Global Provisioned-Managed`) processing options.
+Azure AI Foundry Models makes models available using the model deployment concept in Azure AI Foundry Services (formerly known Azure AI Services). Model deployments are also Azure resources and, when created, they give access to a given model under certain configurations. Such configuration includes the infrastructure require to process the requests. 
+
+Azure AI Foundry Models provides customers with choices on the hosting structure that fits their business and usage patterns. Those options are translated to different deployments types (or SKUs) that are available at model deployment time in the Azure AI Foundry resource. The service offers two main types of deployments are: **standard** and **provisioned**. For a given deployment type, customers can align their workloads with their data processing requirements by choosing an Azure geography (`Standard` or `Provisioned-Managed`), Microsoft specified data zone (`DataZone-Standard` or `DataZone Provisioned-Managed`), or Global (`Global-Standard` or `Global Provisioned-Managed`) processing options. 
 
 For fine-tuned models, an additional `Developer` deployment type provides a cost-efficient means of custom model evaluation, but without data residency.
 
@@ -22,47 +24,47 @@ All deployments can perform the exact same inference operations, however the bil
 - **Data processing location**  
 - **Call volume**
 
-## Azure OpenAI Deployment Data Processing Locations
+## Azure AI Foundry Deployment Data Processing Locations
 
 For standard deployments, there are three deployment type options to choose from - global, data zone, and Azure geography. For provisioned deployments, there are two deployment type options to choose from - global and Azure geography. Global standard is the recommended starting point. 
 
 Global deployments leverage Azure's global infrastructure to dynamically route customer traffic to the data center with the best availability for the customer’s inference requests. This means you will get the highest initial throughput limits and best model availability with Global while still providing our uptime SLA and low latency. For high volume workloads above the specified usage tiers on standard and global standard, you may experience increased latency variation. For customers that require the lower latency variance at large workload usage, we recommend leveraging our provisioned deployment types.
 
 Our global deployments will be the first location for all new models and features. Depending on call volume, customers with large volume and low latency variance requirements should consider our provisioned deployment types.
 
-Data zone deployments leverage Azure's global infrastructure to dynamically route customer traffic to the data center with the best availability for the customer's inference requests within the data zone defined by Microsoft. Positioned between our Azure geography and Global deployment offerings, data zone deployments provide elevated quota limits while keeping data processing within the Microsoft specified data zone. Data stored at rest will continue to remain in the geography of the Azure OpenAI resource (e.g., for an Azure OpenAI resource created in the Sweden Central Azure region, the Azure geography is Sweden).
+Data zone deployments leverage Azure's global infrastructure to dynamically route customer traffic to the data center with the best availability for the customer's inference requests within the data zone defined by Microsoft. Positioned between our Azure geography and Global deployment offerings, data zone deployments provide elevated quota limits while keeping data processing within the Microsoft specified data zone. Data stored at rest will continue to remain in the geography of the Azure AI Foundry resource (e.g., for an AI Foundry resource created in the Sweden Central Azure region, the Azure geography is Sweden).
 
-If the Azure OpenAI resource used in your Data Zone deployment is located in the United States, the data will be processed within the United States. If the Azure OpenAI resource used in your Data Zone deployment is located in a European Union Member Nation, the data will be processed within the European Union Member Nation geographies. For all Azure OpenAI deployment types, any data stored at rest will continue to remain in the geography of the Azure OpenAI resource. Azure data processing and compliance commitments remain applicable.
+If the Azure AI Foundry resource used in your Data Zone deployment is located in the United States, the data will be processed within the United States. If the Azure AI Foundry resource used in your Data Zone deployment is located in a European Union Member Nation, the data will be processed within the European Union Member Nation geographies. For all Azure AI Foundry deployment types, any data stored at rest will continue to remain in the geography of the Azure AI Foundry resource. Azure data processing and compliance commitments remain applicable.
 
-For any [deployment type](/azure/ai-services/openai/how-to/deployment-types) labeled 'Global,' prompts and responses may be processed in any geography where the relevant Azure OpenAI model is deployed (learn more about [region availability of models](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For any deployment type labeled as 'DataZone,' prompts and responses may be processed in any geography within the specified data zone, as defined by Microsoft. If you create a DataZone deployment in an Azure OpenAI resource located in the United States, prompts and responses may be processed anywhere within the United States. If you create a DataZone deployment in an Azure OpenAI resource located in a European Union Member Nation, prompts and responses may be processed in that or any other European Union Member Nation. For both Global and DataZone deployment types, any data stored at rest, such as uploaded data, is stored in the customer-designated geography. Only the location of processing is affected when a customer uses a Global deployment type or DataZone deployment type in Azure OpenAI in Azure AI Foundry Models; Azure data processing and compliance commitments remain applicable.
+For any [deployment type](/azure/ai-services/openai/how-to/deployment-types) labeled 'Global,' prompts and responses may be processed in any geography where the relevant Azure AI Foundry model is deployed (learn more about [region availability of models](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For any deployment type labeled as 'DataZone,' prompts and responses may be processed in any geography within the specified data zone, as defined by Microsoft. If you create a DataZone deployment in an Azure AI Foundry resource located in the United States, prompts and responses may be processed anywhere within the United States. If you create a DataZone deployment in an Azure AI Foundry resource located in a European Union Member Nation, prompts and responses may be processed in that or any other European Union Member Nation. For both Global and DataZone deployment types, any data stored at rest, such as uploaded data, is stored in the customer-designated geography. Only the location of processing is affected when a customer uses a Global deployment type or DataZone deployment type in Azure AI Foundry resource; Azure data processing and compliance commitments remain applicable.
 
 > [!NOTE]
 > With Global standard and Data zone standard deployment types if the primary region experiences an interruption in service all traffic that is initially routed to this region will be impacted. To learn more, consult the [business continuity and disaster recovery guide](../how-to/business-continuity-disaster-recovery.md).
 
 ## Global standard
 
 > [!IMPORTANT]
-> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
+> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure AI Foundry location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
 
 **SKU name in code:** `GlobalStandard`
 
-Global deployments are available in the same Azure OpenAI resources as non-global deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center with best availability for each request.  Global standard provides the highest default quota and eliminates the need to load balance across multiple resources.  
+Global deployments are available in the same Azure AI Foundry resources as non-global deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center with best availability for each request.  Global standard provides the highest default quota and eliminates the need to load balance across multiple resources.  
 
 Customers with high consistent volume may experience greater latency variability. The threshold is set per model. See the [quotas page to learn more](./quota.md).  For applications that require the lower latency variance at large workload usage, we recommend purchasing provisioned throughput.
 
 ## Global provisioned
 
 > [!IMPORTANT]
-> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
+> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure AI Foundry location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
 
 **SKU name in code:** `GlobalProvisionedManaged`
 
-Global deployments are available in the same Azure OpenAI resources as non-global deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center with best availability for each request. Global provisioned deployments provide reserved model processing capacity for high and predictable throughput using Azure global infrastructure.  
+Global deployments are available in the same Azure AI Foundry resources as non-global deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center with best availability for each request. Global provisioned deployments provide reserved model processing capacity for high and predictable throughput using Azure global infrastructure.  
 
 ## Global batch
 
 > [!IMPORTANT]
-> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
+> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure AI Foundry location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
 
 [Global batch](./batch.md) is designed to handle large-scale and high-volume processing tasks efficiently. Process asynchronous groups of requests with separate quota, with 24-hour target turnaround, at [50% less cost than global standard](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). With batch processing, rather than send one request at a time you send a large number of requests in a single file. Global batch requests have a separate enqueued token quota avoiding any disruption of your online workloads.  
 
@@ -87,27 +89,27 @@ Key use cases include:
 ## Data zone standard
 
 > [!IMPORTANT]
-> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location within the Microsoft specified data zone. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
+> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure AI Foundry location within the Microsoft specified data zone. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
 
 **SKU name in code:** `DataZoneStandard`
 
-Data zone standard deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. Data zone standard provides higher default quotas than our Azure geography-based deployment types. 
+Data zone standard deployments are available in the same Azure AI Foundry resource as all other Azure AI Foundry deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. Data zone standard provides higher default quotas than our Azure geography-based deployment types. 
 
 Customers with high consistent volume may experience greater latency variability. The threshold is set per model. See the [Quotas and limits](/azure/ai-services/openai/quotas-limits#usage-tiers) page to learn more. For workloads that require low latency variance at large volume, we recommend leveraging the provisioned deployment offerings. 
 
 ## Data zone provisioned
 
 > [!IMPORTANT]
-> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location within the Microsoft specified data zone.[Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
+> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure AI Foundry location within the Microsoft specified data zone.[Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
 
 **SKU name in code:** `DataZoneProvisionedManaged`
 
-Data zone provisioned deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft specified data zone with the best availability for each request. Data zone provisioned deployments provide reserved model processing capacity for high and predictable throughput using Azure infrastructure within the Microsoft specified data zone.  
+Data zone provisioned deployments are available in the same Azure AI Foundry resource as all other Azure AI Foundry deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft specified data zone with the best availability for each request. Data zone provisioned deployments provide reserved model processing capacity for high and predictable throughput using Azure infrastructure within the Microsoft specified data zone.  
 
 ## Data zone batch
 
 > [!IMPORTANT]
-> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location within the Microsoft specified data zone. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
+> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure AI Foundry location within the Microsoft specified data zone. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
  
 **SKU name in code:** `DataZoneBatch`
 
@@ -121,17 +123,17 @@ Standard deployments provide a pay-per-call billing model on the chosen model. P
 
 Standard deployments are optimized for low to medium volume workloads with high burstiness. Customers with high consistent volume may experience greater latency variability.
 
-## Provisioned
+## Regional Provisioned
 
 **SKU name in code:** `ProvisionedManaged`
 
-Provisioned deployments allow you to specify the amount of throughput you require in a deployment. The service then allocates the necessary model processing capacity and ensures it's ready for you. Throughput is defined in terms of provisioned throughput units (PTU) which is a normalized way of representing the throughput for your deployment. Each model-version pair requires different amounts of PTU to deploy and provide different amounts of throughput per PTU. Learn more from our [Provisioned throughput concepts article](../concepts/provisioned-throughput.md).
+Regional Provisioned deployments allow you to specify the amount of throughput you require in a deployment. The service then allocates the necessary model processing capacity and ensures it's ready for you. Throughput is defined in terms of provisioned throughput units (PTU) which is a normalized way of representing the throughput for your deployment. Each model-version pair requires different amounts of PTU to deploy and provide different amounts of throughput per PTU. Learn more from our [Provisioned throughput concepts article](../concepts/provisioned-throughput.md).
 
 ### How to disable access to global deployments in your subscription
 
 Azure Policy helps to enforce organizational standards and to assess compliance at-scale. Through its compliance dashboard, it provides an aggregated view to evaluate the overall state of the environment, with the ability to drill down to the per-resource, per-policy granularity. It also helps to bring your resources to compliance through bulk remediation for existing resources and automatic remediation for new resources. [Learn more about Azure Policy and specific built-in controls for AI services](/azure/ai-services/security-controls-policy).
 
-You can use the following policy to disable access to any Azure OpenAI deployment type. To disable access to a specific deployment type, replace `GlobalStandard` with the sku name for the deployment type that you would like to disable access to. 
+You can use the following policy to disable access to any Azure AI Foundry deployment type. To disable access to a specific deployment type, replace `GlobalStandard` with the sku name for the deployment type that you would like to disable access to. 
 
 ```json
 {
@@ -156,7 +158,7 @@ You can use the following policy to disable access to any Azure OpenAI deploymen
 ## Developer (for fine-tuned models)
 
 > [!IMPORTANT]
-> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
+> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure AI Foundry location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
 
 **SKU name in code:** `Developer`
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントタイプガイドの更新"
}
```

### Explanation
この変更では、`deployment-types.md` ファイルに対して内容のクリアな更新が行われました。主に、タイトルと説明が誇張され、Azure OpenAIからAzure AI Foundry Modelsへの名称変更が反映されました。また、ドキュメント全体が適切な用語に修正され、それに伴い表現もより明確になっています。

具体的には、デプロイメントの種類についての詳細な説明が強化され、顧客が自分のビジネスニーズや使用パターンに最適なホスティング構造を選択できるようにする情報が改善されました。さらに、地域別やデータゾーン別のデータ処理ロケーションに関する情報が最新の状態に更新され、処理データの所在地について明確なコミットメントが行われています。

最終的に、これらの変更は、ユーザーがAzure AI Foundryのサービスとデプロイメントタイプをより理解しやすくすることを目的としています。

## articles/ai-services/openai/how-to/fine-tuning-deploy.md{#item-286d57}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: build-2023, build-2023-dataai, devx-track-python, references_regions
 ms.topic: how-to
-ms.date: 03/31/2025
+ms.date: 05/30/2025
 author: mrbullwinkle
 ms.author: mbullwin
 ---
@@ -17,7 +17,7 @@ Once your model is fine-tuned, you can deploy the model and can use it in your o
 
 When you deploy the model, you make the model available for inferencing, and that incurs an hourly hosting charge. Fine-tuned models, however, can be stored in Azure AI Foundry at no cost until you're ready to use them.
 
-Azure OpenAI provides choices of deployment types for fine-tuned models on the hosting structure that fits different business and usage patterns: **Standard**, **Global Standard** (preview) and **Provisioned Managed** (preview). Learn more about [deployment types for fine-tuned models](#deployment-types) and the [concepts of all deployment types](./deployment-types.md).
+Azure OpenAI provides choices of deployment types for fine-tuned models on the hosting structure that fits different business and usage patterns: **Standard**, **Global Standard** (preview) and **Provisioned Throughput** (preview). Learn more about [deployment types for fine-tuned models](#deployment-types) and the [concepts of all deployment types](./deployment-types.md).
 
 ## Deploy your fine-tuned model
 
@@ -380,14 +380,14 @@ Azure OpenAI fine-tuning supports the following deployment types.
 
 :::image type="content" source="../media/fine-tuning/global-standard.png" alt-text="Screenshot of the global standard deployment user experience with a fine-tuned model." lightbox="../media/fine-tuning/global-standard.png":::
 
-### Provisioned Managed
+### Provisioned Throughput
 
 | Models | Region |
 |--|--|
 |GPT-4o-finetune|North Central US, Sweden Central|
 |GPT-4o-mini-finetune|North Central US, Sweden Central|
 
-[Provisioned managed](./deployment-types.md#provisioned) fine-tuned deployments offer [predictable performance](../concepts/provisioned-throughput.md) for latency-sensitive agents and applications. They use the same regional provisioned throughput (PTU) capacity as base models, so if you already have regional PTU quota you can deploy your fine-tuned model in support regions.
+[Provisioned throughput](./deployment-types.md#regional-provisioned) fine-tuned deployments offer [predictable performance](../concepts/provisioned-throughput.md) for latency-sensitive agents and applications. They use the same regional provisioned throughput (PTU) capacity as base models, so if you already have regional PTU quota you can deploy your fine-tuned model in support regions.
 
 ## Clean up your deployment
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングデプロイガイドの用語変更"
}
```

### Explanation
この変更では、`fine-tuning-deploy.md` ファイルにおいて、いくつかの用語の置換と日付の更新が行われました。特に、ファインチューニングされたモデルのデプロイメントタイプに関する表現が改善され、"Provisioned Managed" が "Provisioned Throughput" に変更されました。これにより、利用者がデプロイメントの種類をより明確に理解できる内容になっています。

また、ドキュメントの日付も「03/31/2025」から「05/30/2025」に更新され、最新の情報を反映した形となっています。これらの変更は、ファインチューニングデプロイに関する内容をよりクリアで一貫したものにし、ユーザーが使用する際の利便性を向上させることを目的としています。

## articles/ai-services/openai/how-to/provisioned-get-started.md{#item-c8df1c}

<details>
<summary>Diff</summary>
````diff
@@ -14,9 +14,9 @@ recommendations: false
 
 # Get started using provisioned deployments on the Azure OpenAI in Azure AI Foundry Models
 
-The following guide walks you through key steps in creating a provisioned deployment with your Azure OpenAI resource. For more details on the concepts discussed here, see:
-* [Azure OpenAI Provisioned Onboarding Guide](./provisioned-throughput-onboarding.md)
-* [Azure OpenAI Provisioned Concepts](../concepts/provisioned-throughput.md) 
+The following guide walks you through key steps in creating a provisioned deployment with your Azure AI Foundry resource. For more details on the concepts discussed here, see:
+* [Azure AI Foundry Provisioned Throughput Onboarding Guide](./provisioned-throughput-onboarding.md)
+* [Azure AI Foundry Provisioned Throughput Concepts](../concepts/provisioned-throughput.md) 
 
 ## Prerequisites
 
@@ -32,48 +32,60 @@ Creating a new deployment requires available (unused) quota to cover the desired
 * Total PTU Quota = 500 PTUs 
 * Deployments: 
     * 100 PTUs: GPT-4o, 2024-05-13 
-    * 100 PTUs: GPT-4, 0613 
+    * 100 PTUs: DeepSeek-R1, 1
 
 Then 200 PTUs of quota are considered used, and there are 300 PTUs available for use to create new deployments. 
 
-A default amount of global, data zone, and regional provisioned quota is assigned to eligible subscriptions in several regions. You can view the quota available to you in a region by visiting the Quotas pane in [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and selecting the desired subscription and region. For example, the screenshot below shows a quota limit of 500 PTUs in West US for the selected subscription. Note that you might see lower values of available default quotas. 
+A default amount of global, data zone, and regional provisioned quota is assigned to eligible subscriptions in several regions. You can view the quota available to you in a region by visiting the Quotas pane in [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and selecting the desired subscription and region. For example, the screenshot below shows a quota limit of 300 Global Provisioned Throughput PTUs in West US for the selected subscription. The total usage of this Global PTUs is 50, then you will have 250 PTU units available to deploy Global Provisioned Throughput deployment type.
 
 :::image type="content" source="../media/provisioned/available-quota.png" alt-text="A screenshot of the available quota in Azure AI Foundry portal." lightbox="../media/provisioned/available-quota.png":::
 
-Additional quota can be requested by clicking the Request Quota link to the right of the “Usage/Limit” column.  (This is off-screen in the screenshot above). 
+Additional quota can be requested by clicking the "Request Quota" Button.
 
-## Create an Azure OpenAI resource 
+## Create an Azure AI Foundry resource 
 
-Provisioned deployments are created via Azure OpenAI resource objects within Azure. You must have an Azure OpenAI resource in each region where you intend to create a deployment. Use the Azure portal to [create a resource](./create-resource.md) in a region with available quota, if required.  
+Provisioned deployments are created via Azure AI Foundry resource objects within Azure. You must have an Azure AI Foundry resource in each region where you intend to create a deployment. Use the Azure portal to [create a resource](./create-resource.md) in a region with available quota, if required.  
 
 > [!NOTE]
-> Azure OpenAI resources can support multiple types of Azure OpenAI deployments at the same time.  It is not necessary to dedicate new resources for your provisioned deployments. 
+> Azure AI Foundry resources can support multiple types of Azure AI Foundry deployments at the same time.  It is not necessary to dedicate new resources for your provisioned deployments. 
+
+## Discover models with provisioned deployment option
+
+Once you have verified your quota, you can create a deployment. Navigate to Azure AI Foundry model catalog to discover the models with provisioned deployment options. 
+
+1. Sign into the [Azure AI Foundry portal](https://ai.azure.com/). 
+2. Choose the subscription that was enabled for provisioned deployments & select the desired resource in a region where you have the quota. 
+3. You can select models by filtering **Direct from Microsoft** in the model collections filter. Those are models held and served by Azure directly and support provisioned throughput deployment option. 
+4. Select the model that you want to deploy and check the model details in the model card. 
+
 
 ## Create your provisioned deployment - capacity is available
 
-Once you have verified your quota, you can create a deployment. To create a provisioned deployment, you can follow these steps; the choices described reflect the entries shown in the screenshot. 
+To create a provisioned deployment, you can follow these steps; the choices described reflect the entries shown in the screenshot.
 
 :::image type="content" source="../media/provisioned/deployment-screen.png" alt-text="Screenshot of the Azure AI Foundry portal deployment page for a provisioned deployment." lightbox="../media/provisioned/deployment-screen.png":::
 
 
 
-1. Sign into the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs).
-1. Choose the subscription that was enabled for provisioned deployments & select the desired resource in a region where you have the quota.
-1. Under **Management** in the left-nav select **Deployments**.
-1. Select Create new deployment and configure the following fields. Expand the **advanced options** drop-down menu.
-1. Fill out the values in each field. Here's an example:
+1. Click **Use this model** and configure the following fields. 
+
+2. Select "Global Provisioned Throughput"," Data Zone Provisioned Throughput" or" Regional Provisioned Throughput" as you required in the Deployment type drop-down for your provisioned deployment. 
+
+3. Expand the **advanced options** drop-down menu. 
+
+4. Fill out the values in each field. Here's an example: 
 
-| Field | Description |	Example |
+| Field | Description |    Example |
 |--|--|--|
-| Select a model|	Choose the specific model you wish to deploy.	| GPT-4 |
-| Model version |	Choose the version of the model to deploy.	 | 0613 |
-| Deployment Name	 | The deployment name is used in your code to call the model by using the client libraries and the REST APIs.	| gpt-4|
-| Content filter	| Specify the filtering policy to apply to the deployment. Learn more on our [Content Filtering](../concepts/content-filter.md) how-to. | 	Default |
-| Deployment Type	|This impacts the throughput and performance. Choose Global Provisioned-Managed, DataZone Provisioned-Managed or Provisioned-Managed from the deployment dialog dropdown for your deployment 	| Provisioned-Managed |
-| Provisioned Throughput Units |	Choose the amount of throughput you wish to include in the deployment. |	100 |
+| Select a model|    Choose the specific model you wish to deploy.    | GPT-4 |
+| Model version |    Choose the version of the model to deploy.     | 0613 |
+| Deployment Name     | The deployment name is used in your code to call the model by using the client libraries and the REST APIs.    | gpt-4|
+| Content filter    | Specify the filtering policy to apply to the deployment. Learn more on our [Content Filtering](../concepts/content-filter.md) how-to. |     Default |
+| Deployment Type    |This impacts the throughput and performance. Choose Global Provisioned Throughput, Data Zone Provisioned Throughput or Regional Provisioned Throughput from the deployment dialog dropdown for your deployment     | Global Provisioned Throughput |
+| Provisioned Throughput Units |    Choose the amount of throughput you wish to include in the deployment. |    100 |
 
 > [!NOTE]
-> The deployment dialog contains a reminder that you can purchase an Azure Reservation for Azure OpenAI Provisioned to obtain a significant discount for a term commitment. 
+> The deployment dialog contains a reminder that you can purchase an Azure Reservation for Azure AI Foundry Provisioned Throughput to obtain a significant discount for a term commitment. 
 
 Once you have entered the deployment settings, click **Confirm Pricing** to continue.  A pricing confirmation dialog will appear that will display the list price for the deployment, if you choose to pay for it on an hourly basis, with no Azure Reservation to provide a term discount.
 
@@ -113,20 +125,32 @@ In this event, the wizard in [Azure AI Foundry portal](https://ai.azure.com/?cid
 Things to notice: 
 
 * A message displays showing you many PTUs you have in available quota, and how many can currently be deployed at this time. 
-* If you select a number of PTUs greater than service capacity, a message will appear that provides options for you to obtain more capacity, and a button to allow you to select an alternate region. Clicking the "See other regions" button will display a dialog that shows a list of Azure OpenAI resources where you can create a deployment, along with the maximum sized deployment that can be created based on available quota and service capacity in each region. 
+* If you select a number of PTUs greater than service capacity, a message will appear that provides options for you to obtain more capacity, and a button to allow you to select an alternate region. Clicking the "See other regions" button will display a dialog that shows a list of Azure AI Foundry resources where you can create a deployment, along with the maximum sized deployment that can be created based on available quota and service capacity in each region. 
 
 :::image type="content" source="../media/provisioned/choose-different-resource.png" alt-text="Screenshot of the Azure AI Foundry portal deployment page for choosing a different resource and region." lightbox="../media/provisioned/choose-different-resource.png":::
 
 Selecting a resource and clicking **Switch resource** will cause the deployment dialog to redisplay using the selected resource. You can then proceed to create your deployment in the new region. 
 
+## Create a new deployment or exchange models with your quota
+
+If you still have quota available under the subscription and region, you can create new provisioned deployments for other models that direct host and sold from Microsoft. 
+
+The steps are the same as the above example. When you create a new deployment, you will see the total available quota you can use in the deployment widget. In the screenshot below, the available quota is 250 units. 
+
+:::image type="content" source="../media/provisioned/deepseek-deployment.png" alt-text="Screenshot of the fungible PTU to deploy flagship models." lightbox="../media/provisioned/deepseek-deployment.png":::
+
+After you deployed the new model, you can check the quota usage in [AI Foundry portal](https://ai.azure.com/managementCenter/quota?wsid=/subscriptions/6a6fff00-4464-4eab-a6b1-0b533c7202e0/resourceGroups/rg-fokikioluai/providers/Microsoft.CognitiveServices/accounts/ai-fokikioluai889906014325&tid=72f988bf-86f1-41af-91ab-2d7cd011db47#aoaiProvisionedManaged). You can manage your quota by either requesting new quota or deleting existing deployments to free up PTU quotas for new provisioned deployments. 
+
+:::image type="content" source="../media/provisioned/fungible-quota.png" alt-text="Screenshot of the fungible PTU quota in quota page." lightbox="../media/provisioned/fungible-quota.png":::
+
 ## Optionally purchase a reservation 
 
 Following the creation of your deployment, you might want to purchase a term discount via an Azure Reservation.  An Azure Reservation can provide a substantial discount on the hourly rate for users intending to use the deployment beyond a few days.   
 
 For more information on the purchase model and reservations, see:
-* [Save costs with Microsoft Azure OpenAI provisioned reservations](/azure/cost-management-billing/reservations/azure-openai).
-* [Azure OpenAI provisioned onboarding guide](./provisioned-throughput-onboarding.md) 
-* [Guide for Azure OpenAI provisioned reservations](../concepts/provisioned-throughput.md) 
+* [Save costs with Microsoft Azure AI Foundry provisioned throughput reservations](/azure/cost-management-billing/reservations/azure-openai).
+* [Azure AI Foundry provisioned throughput onboarding guide](./provisioned-throughput-onboarding.md) 
+* [Guide for Azure AI Foundry provisioned throughput reservations](../concepts/provisioned-throughput.md) 
 
 > [!IMPORTANT]
 > Capacity availability for model deployments is dynamic and changes frequently across regions and models. To prevent you from purchasing a reservation for more PTUs than you can use, create deployments first, and then purchase the Azure Reservation to cover the PTUs you have deployed. This best practice will ensure that you can take full advantage of the reservation discount and prevent you from purchasing a term commitment that you cannot use.
@@ -181,12 +205,12 @@ For more information about monitoring your deployments, see the [Monitoring Azur
 
 
 ## Handling high utilization
-Provisioned deployments provide you with an allocated amount of compute capacity to run a given model. The ‘Provisioned-Managed Utilization V2’ metric in Azure Monitor measures the utilization of the deployment in one-minute increments. Provisioned-Managed deployments are also optimized so that calls accepted are processed with a consistent per-call max latency. When the workload exceeds its allocated capacity, the service returns a 429 HTTP status code until the utilization drops down below 100%. The time before retrying is provided in the `retry-after` and `retry-after-ms` response headers that provide the time in seconds and milliseconds respectively. This approach maintains the per-call latency targets while giving the developer control over how to handle high-load situations – for example retry or divert to another experience/endpoint. 
+Provisioned deployments provide you with an allocated amount of compute capacity to run a given model. The 'Provisioned-Managed Utilization V2' metric in Azure Monitor measures the utilization of the deployment in one-minute increments. Provisioned-Managed deployments are also optimized so that calls accepted are processed with a consistent per-call max latency. When the workload exceeds its allocated capacity, the service returns a 429 HTTP status code until the utilization drops down below 100%. The time before retrying is provided in the `retry-after` and `retry-after-ms` response headers that provide the time in seconds and milliseconds respectively. This approach maintains the per-call latency targets while giving the developer control over how to handle high-load situations – for example retry or divert to another experience/endpoint. 
 
 ### What should  I do when I receive a 429 response?
 A 429 response indicates that the allocated PTUs are fully consumed at the time of the call. The response includes the `retry-after-ms` and `retry-after` headers that tell you the time to wait before the next call will be accepted. How you choose to handle a 429 response depends on your application requirements. Here are some considerations:
--	If you are okay with longer per-call latencies, implement client-side retry logic to wait the `retry-after-ms` time and retry. This approach lets you maximize the throughput on the deployment. Microsoft-supplied client SDKs already handle it with reasonable defaults. You might still need further tuning based on your use-cases.
--	Consider redirecting the traffic to other models, deployments, or experiences. This approach is the lowest-latency solution because this action can be taken as soon as you receive the 429 signal.
+-    If you are okay with longer per-call latencies, implement client-side retry logic to wait the `retry-after-ms` time and retry. This approach lets you maximize the throughput on the deployment. Microsoft-supplied client SDKs already handle it with reasonable defaults. You might still need further tuning based on your use-cases.
+-    Consider redirecting the traffic to other models, deployments, or experiences. This approach is the lowest-latency solution because this action can be taken as soon as you receive the 429 signal.
 The 429 signal isn't an unexpected error response when pushing to high utilization but instead part of the design for managing queuing and high load for provisioned deployments. 
 
 ### Modifying retry logic within the client libraries
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングデプロイメントのガイドライン更新"
}
```

### Explanation
この変更では、`provisioned-get-started.md` ファイルに対していくつかの重要な修正が行われました。主な変更点は、Azure OpenAIリソースをAzure AI Foundryリソースに置き換えたことです。この修正により、利用者は「プロビジョニングされたデプロイメント」を使用する際に、正確なリソースに基づいた手順を把握しやすくなります。

さらに、関連するリンクやリソースの名称も改善され、より一貫性のある表現になっています。また、グローバル、データゾーン、地域のプロビジョニングクォータについての具体的な数値が更新され、利用者が利用可能なクォータをより正確に把握できるようになっています。

新たに追加されたセクションもあり、モデルをプロビジョニングデプロイとして発見する方法、デプロイメントの作成手順、モデルの交換に関する手順が詳しく説明されています。これらの更新は、利用者がプロビジョンドデプロイメントをより効果的に利用できるようにするためのものです。

## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
 title:  Understanding costs associated with provisioned throughput units (PTU)
-description: Learn about provisioned throughput costs and billing in Azure OpenAI. 
+description: Learn about provisioned throughput costs and billing in Azure AI Foundry. 
 ms.service: azure-ai-openai
 ms.topic: conceptual 
 ms.date: 05/28/2025
@@ -23,49 +23,49 @@ Provisioned throughput units (PTUs) are generic units of model processing capaci
 
 ## Understanding provisioned throughput billing
 
-Azure OpenAI [Provisioned](../how-to/deployment-types.md#provisioned), [Data Zone Provisioned](../how-to/deployment-types.md#data-zone-provisioned) (also known as regional), and [Global Provisioned](../how-to/deployment-types.md#global-provisioned) are purchased on-demand at an hourly basis based on the number of deployed PTUs, with substantial term discount available via the purchase of [Azure Reservations](#azure-reservations-for-azure-openai-provisioned-deployments).  
+Azure AI Foundry [Regional Provisioned Throughput](../how-to/deployment-types.md#regional-provisioned), [Data Zone Provisioned Throughput](../how-to/deployment-types.md#data-zone-provisioned), and [Global Provisioned Throughput](../how-to/deployment-types.md#global-provisioned) are purchased on-demand at an hourly basis based on the number of deployed PTUs, with substantial term discount available via the purchase of [Azure Reservations](#azure-reservations-for-azure-ai-foundry-provisioned-throughput).  
 
-The hourly model is useful for short-term deployment needs, such as validating new models or acquiring capacity for a hackathon.  However, the discounts provided by the Azure Reservation for Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned are considerable and most customers with consistent long-term usage will find a reserved model to be a better value proposition. 
+The hourly model is useful for short-term deployment needs, such as validating new models or acquiring capacity for a hackathon.  However, the discounts provided by the Azure Reservation for Azure AI Foundry Regional Provisioned, Data Zone Provisioned, and Global Provisioned are considerable and most customers with consistent long-term usage will find a reserved model to be a better value proposition. 
 
 > [!NOTE]
-> Azure OpenAI Provisioned customers onboarded prior to the August self-service update use a purchase model called the Commitment model. These customers can continue to use this older purchase model alongside the Hourly/reservation purchase model. The Commitment model is not available for new customers or [certain new models](../concepts/provisioned-migration.md#supported-models-on-commitment-payment-model) introduced after August 2024. For details on the Commitment purchase model and options for coexistence and migration, see the [Azure OpenAI Provisioned August Update](../concepts/provisioned-migration.md).
+> Azure AI Foundry Provisioned customers onboarded prior to the August self-service update use a purchase model called the Commitment model. These customers can continue to use this older purchase model alongside the Hourly/reservation purchase model. The Commitment model is not available for new customers or [certain new models](../concepts/provisioned-migration.md#supported-models-on-commitment-payment-model) introduced after August 2024. For details on the Commitment purchase model and options for coexistence and migration, see the [Azure AI Foundry Provisioned August Update](../concepts/provisioned-migration.md).
 
 
 ## Model independent quota
 
-Unlike the Tokens Per Minute (TPM) quota used by other Azure OpenAI offerings, PTUs are model-independent. The PTUs might be used to deploy any supported model/version in the region.
+Unlike the Tokens Per Minute (TPM) quota used by other Azure AI Foundry offerings, PTUs are model-independent. The PTUs might be used to deploy any supported models hosted and sold directly by Microsoft in the region.
 
 :::image type="content" source="../media/provisioned/model-independent-quota.png" alt-text="Diagram of model independent quota with one pool of PTUs available to multiple Azure OpenAI models." lightbox="../media/provisioned/model-independent-quota.png":::
 
-Quota for provisioned deployments shows up in Azure AI Foundry as the following deployment types: [global provisioned](../how-to/deployment-types.md#global-provisioned), [data zone provisioned](../how-to/deployment-types.md#data-zone-provisioned) and [standard provisioned](../how-to/deployment-types.md#provisioned).
+Quota for provisioned deployments shows up in Azure AI Foundry as the following deployment types: [global provisioned](../how-to/deployment-types.md#global-provisioned), [data zone provisioned](../how-to/deployment-types.md#data-zone-provisioned) and [regional provisioned](../how-to/deployment-types.md#regional-provisioned).
 
 |deployment type  |Quota name  |
 |---------|---------|
-|[provisioned](../how-to/deployment-types.md#provisioned)     |  Provisioned Managed Throughput Unit       |
-|[global provisioned](../how-to/deployment-types.md#global-provisioned)     | Global Provisioned Managed Throughput Unit        |
-|[data zone provisioned](../how-to/deployment-types.md#data-zone-provisioned)    | Data Zone Provisioned Managed Throughput Unit        |
+|[Regional Provisioned](../how-to/deployment-types.md#regional-provisioned)     |  Regional Provisioned Throughput Unit       |
+|[Global Provisioned](../how-to/deployment-types.md#global-provisioned)     | Global Provisioned Throughput Unit        |
+|[Data zone Provisioned](../how-to/deployment-types.md#data-zone-provisioned)    | Data Zone Provisioned Throughput Unit        |
 
-:::image type="content" source="../media/provisioned/ptu-quota-page.png" alt-text="Screenshot of quota UI for Azure OpenAI provisioned." lightbox="../media/provisioned/ptu-quota-page.png":::
+:::image type="content" source="../media/provisioned/ptu-quota-page.png" alt-text="Screenshot of quota UI for Azure AI Foundry provisioned." lightbox="../media/provisioned/ptu-quota-page.png":::
 
 ## Hourly usage
 
-Provisioned, Data Zone Provisioned, and Global Provisioned deployments are charged an hourly rate ($/PTU/hr) on the number of PTUs that have been deployed.  For example, a 300 PTU deployment will be charged the hourly rate times 300.  All Azure OpenAI pricing is available in the Azure Pricing Calculator. 
+Regional Provisioned, Data Zone Provisioned, and Global Provisioned deployments are charged an hourly rate ($/PTU/hr) on the number of PTUs that have been deployed.  For example, a 300 PTU deployment will be charged the hourly rate times 300.  All Azure AI Foundry model pricing is available in the Azure Pricing Calculator. 
 
 If a deployment exists for a partial hour, it will receive a prorated charge based on the number of minutes it was deployed during the hour.  For example, a deployment that exists for 15 minutes during an hour will receive 1/4th the hourly charge.  
 
 If the deployment size is changed, the costs of the deployment will adjust to match the new number of PTUs.  
 
 :::image type="content" source="../media/provisioned/hourly-billing.png" alt-text="A diagram showing hourly billing." lightbox="../media/provisioned/hourly-billing.png":::
 
-Paying for provisioned, data zoned provisioned, and global provisioned deployments on an hourly basis is ideal for short-term deployment scenarios.  For example: Quality and performance benchmarking of new models, or temporarily increasing PTU capacity to cover an event such as a hackathon.  
+Paying for regional provisioned, data zone provisioned, and global provisioned deployments on an hourly basis is ideal for short-term deployment scenarios.  For example: Quality and performance benchmarking of new models, or temporarily increasing PTU capacity to cover an event such as a hackathon.  
 
-Customers that require long-term usage of provisioned, data zoned provisioned, and global provisioned deployments, however, might pay significantly less per month by purchasing a term discount via [Azure Reservations](#azure-reservations-for-azure-openai-provisioned-deployments) as discussed later in the article. 
+Customers that require long-term usage of regional provisioned, data zone provisioned, and global provisioned deployments, however, might pay significantly less per month by purchasing a term discount via [Azure Reservations](#azure-reservations-for-azure-ai-foundry-provisioned-throughput) as discussed later in the article. 
 
 > [!IMPORTANT]
 > It's not recommended to scale production deployments according to incoming traffic and pay for them purely on an hourly basis. There are two reasons for this:
-> * The cost savings achieved by purchasing Azure Reservations for Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned are significant, and it will be less expensive in many cases to maintain a deployment sized for full production volume paid for via a reservation than it would be to scale the deployment with incoming traffic.
+> * The cost savings achieved by purchasing Azure Reservations for Azure AI Foundry Provisioned Throughput, Data Zone Provisioned, and Global Provisioned are significant, and it will be less expensive in many cases to maintain a deployment sized for full production volume paid for via a reservation than it would be to scale the deployment with incoming traffic.
 > * Having unused provisioned quota (PTUs) doesn't guarantee that capacity will be available to support an increase in the size of the deployment when required. Quota limits the maximum number of PTUs that can be deployed, but it isn't a capacity guarantee. Provisioned capacity for each region and model dynamically changes throughout the day and might not be available when required. As a result, it's recommended to maintain a permanent deployment to cover your traffic needs (paid for via a reservation).
-> Charges for deployments on a deleted resource will continue until the resource is purged. To prevent this, delete a resource’s deployment before deleting the resource. For more information, see [Recover or purge deleted Azure OpenAI resources](../../recover-purge-resources.md). 
+> Charges for deployments on a deleted resource will continue until the resource is purged. To prevent this, delete a resource's deployment before deleting the resource. For more information, see [Recover or purge deleted Azure OpenAI resources](../../recover-purge-resources.md). 
 
 ## How much throughput per PTU you get for each model
 
@@ -75,33 +75,33 @@ Customers that require long-term usage of provisioned, data zoned provisioned, a
 
 The amount of throughput (measured in tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in a given minute. Generating output tokens requires more processing than input tokens.  Starting with GPT 4.1 models and later, the system matches the global standard price ratio between input and output tokens. Cached tokens are deducted 100% from the utilization.
 
-For example, for `gpt-4.1:2025-04-14`, 1 output token counts as 4 input tokens towards your utilization limit which matches the [pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). Older models use a different ratio and for a deeper understanding on how different ratios of input and output tokens impact the throughput your workload needs, see the [Azure OpenAI capacity calculator](https://ai.azure.com/resource/calculator).
+For example, for `gpt-4.1:2025-04-14`, 1 output token counts as 4 input tokens towards your utilization limit which matches the [pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). Older models use a different ratio and for a deeper understanding on how different ratios of input and output tokens impact the throughput your workload needs, see the [Azure AI Foundry PTU quota calculator](https://ai.azure.com/resource/calculator).
 
-|Topic| **o4-mini** | **gpt-4.1** | **gpt-4.1-mini** | **gpt-4.1-nano** | **o3** | **o3-mini** | **o1** | **gpt-4o** | **gpt-4o-mini** |
-| --- |  --- | --- |  --- |  --- | --- | --- | --- | --- | --- |
-|Global & data zone provisioned minimum deployment| 15 | 15|15| 15 | 15 |15|15|15|15|
-|Global & data zone provisioned scale increment| 5 | 5|5| 5 | 5 |5|5|5|5|
-|Regional provisioned minimum deployment|25| 50|25| 25 |50 | 25|25|50|25|
-|Regional provisioned scale increment|25| 50|25| 25 | 50 | 25|50|50|25|
-|Input TPM per PTU|5,400 | 3,000|14,900| 59,400 | 600 | 2,500|230|2,500|37,000|
-|Latency Target Value| 66 Tokens Per Second | 40 Tokens Per Second|50 Tokens Per Second| 60 Tokens Per Second | 40 Tokens Per Second | 66 Tokens Per Second |25 Tokens Per Second|25 Tokens Per Second|33 Tokens Per Second|
+|Topic| **o4-mini** | **gpt-4.1** | **gpt-4.1-mini** | **gpt-4.1-nano** | **o3** | **o3-mini** | **o1** | **gpt-4o** | **gpt-4o-mini** |  **DeepSeek-R1** | **DeepSeek-V3-0324** | **MAI-DS-R1** |
+| --- |  --- | --- |  --- |  --- | --- | --- | --- | --- | --- | --- | --- | --- |
+|Global & data zone provisioned minimum deployment| 15 | 15|15| 15 | 15 |15|15|15|15| 100|100|100|
+|Global & data zone provisioned scale increment| 5 | 5|5| 5 | 5 |5|5|5|5|  100|100|100|
+|Regional provisioned minimum deployment|25| 50|25| 25 |50 | 25|25|50|25| NA|NA|NA|
+|Regional provisioned scale increment|25| 50|25| 25 | 50 | 25|50|50|25|NA|NA|NA|
+|Input TPM per PTU|5,400 | 3,000|14,900| 59,400 | 600 | 2,500|230|2,500|37,000|4,000|4,000|4,000|
+|Latency Target Value| 66 Tokens Per Second | 40 Tokens Per Second|50 Tokens Per Second| 60 Tokens Per Second | 40 Tokens Per Second | 66 Tokens Per Second |25 Tokens Per Second|25 Tokens Per Second|33 Tokens Per Second|50 Tokens Per Second|50 Tokens Per Second|50 Tokens Per Second|
 
 
-For a full list, see the [Azure OpenAI in Azure AI Foundry Models in Azure AI Foundry portal calculator](https://ai.azure.com/resource/calculator).
+For a full list, see the [Azure AI Foundry calculator](https://ai.azure.com/resource/calculator).
 
 ## Determining the number of PTUs needed for a workload
 
 Determining the right amount of provisioned throughput, or PTUs, you require for your workload is an essential step to optimizing performance and cost. 
 
-PTUs represent an amount of model processing capacity. Similar to your computer or databases, different workloads or requests to the model will consume different amounts of underlying processing capacity. The conversion from throughput needs to PTUs can be approximated using historical token usage data or call shape estimations (input tokens, output tokens, and requests per minute) as outlined in our [performance and latency](../how-to/latency.md) documentation. To simplify this process, you can use the [Azure OpenAI Capacity calculator](https://ai.azure.com/resource/calculator) to size specific workload shapes.
+PTUs represent an amount of model processing capacity. Similar to your computer or databases, different workloads or requests to the model will consume different amounts of underlying processing capacity. The conversion from throughput needs to PTUs can be approximated using historical token usage data or call shape estimations (input tokens, output tokens, and requests per minute) as outlined in our [performance and latency](../how-to/latency.md) documentation. To simplify this process, you can use the [Azure AI Foundry PTU quota calculator](https://ai.azure.com/resource/calculator) to size specific workload shapes.
 
 A few high-level considerations:
 - Generations require more capacity than prompts
 - For GPT-4o and later models, the TPM per PTU is set for input and output tokens separately. For older models, larger calls are progressively more expensive to compute. For example, 100 calls of with a 1000 token prompt size requires less capacity than one call with 100,000 tokens in the prompt. This tiering means that the distribution of these call shapes is important in overall throughput. Traffic patterns with a wide distribution that includes some large calls might experience lower throughput per PTU than a narrower distribution with the same average prompt & completion token sizes.
 
 ### Obtaining PTU quota
 
-PTU quota is available by default in many regions. If more quota is required, customers can request quota via the Request Quota link. This link can be found to the right of the designated provisioned deployment type quota tabs in Azure AI Foundry The form allows the customer to request an increase in the specified PTU quota for a given region. The customer receives an email at the included address once the request is approved, typically within two business days. 
+Customers need to request quota via the [Request Quota Link](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR4xPXO648sJKt4GoXAed-0pUMFE1Rk9CU084RjA0TUlVSUlMWEQzVkJDNCQlQCN0PWcu). If more quotas are required, you also need to request quota via this link. This link can be found in the quota hub in management center of Azure AI Foundry. The form allows the customer to request an increase in the specified PTU quota for a given region. The customer receives an email at the included address once the request is approved, typically within two business days. 
 
 ### Per-Model PTU minimums
 
@@ -115,17 +115,17 @@ To use the capacity planner, go to the Azure AI Foundry Portal and select the **
 
 :::image type="content" source="../media/provisioned/deploy-model-button.png" alt-text="A screenshot of the model deployment screen." lightbox="../media/provisioned/deploy-model-button.png":::
 
-Choose a model, and click **Confirm**. Select a provision-managed deployment type. After filling out the input and output TPM data in the built-in capacity calculator, select the **Calculate** button to view your PTU allocation recommendation. 
+Choose a model, and click **Confirm**. Select a provision throughput deployment type. After filling out the input and output TPM data in the built-in capacity calculator, select the **Calculate** button to view your PTU allocation recommendation. 
 
 :::image type="content" source="../media/provisioned/deployment-ptu-capacity-calculator.png" alt-text="A screenshot of deployment workflow PTU capacity calculator." lightbox="../media/provisioned/deployment-ptu-capacity-calculator.png":::
 
-To estimate provisioned capacity using request level data, open the capacity planner in the [Azure AI Foundry](https://ai.azure.com/?cid=learnDocs). The capacity calculator is under **Shared resources** > **Model Quota** > **Azure OpenAI Provisioned**.
+To estimate provisioned capacity using request level data, open the capacity planner in the [Azure AI Foundry](https://ai.azure.com?cid=learnDocs). The capacity calculator is under **Management Center** > **Quota** > **Provisioned Throughput**.
 
-The **Provisioned** option and the capacity planner are only available in certain regions within the Quota pane, if you don't see this option setting the quota region to *Sweden Central* will make this option available. Enter the following parameters based on your workload.
+The **Provisioned Throughput** option and the calculator are only available in certain regions within the Quota pane, if you don't see this option setting the quota region to *Sweden Central* will make this option available. Enter the following parameters based on your workload.
 
 | Input | Description |
 |---|---|
-|Model | OpenAI model you plan to use. For example: GPT-4 |
+|Model | model you plan to use. For example: GPT-4 |
 | Version | Version of the model you plan to use, for example 0614 |
 | Peak calls per min | The number of calls per minute that are expected to be sent to the model |
 | Tokens in prompt call | The number of tokens in the prompt for each call to the model. Calls with larger prompts utilize more of the PTU deployment. Currently this calculator assumes a single prompt value so for workloads with wide variance. We recommend benchmarking your deployment on your traffic to determine the most accurate estimate of PTU needed for your deployment. |
@@ -140,9 +140,9 @@ The values in the output column are the estimated value of PTU units required fo
 > [!NOTE]
 > The capacity calculators provide an estimate based on simple input criteria. The most accurate way to determine your capacity is to benchmark a deployment with a representational workload for your use case.
 
-## Azure Reservations for Azure OpenAI provisioned deployments
+## Azure Reservations for Azure AI Foundry Provisioned Throughput
 
-Discounts on top of the hourly usage price can be obtained by purchasing an Azure Reservation for Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned. An Azure Reservation is a term-discounting mechanism shared by many Azure products. For example, Compute and Cosmos DB. For Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned, the reservation provides a discount in exchange for committing to payment for fixed number of PTUs for a one-month or one-year period.  
+Discounts on top of the hourly usage price can be obtained by purchasing an Azure Reservation for Azure AI Foundry Regional Provisioned, Data Zone Provisioned, and Global Provisioned. An Azure Reservation is a term-discounting mechanism shared by many Azure products. For example, Compute and Cosmos DB. For Azure AI Foundry Regional Provisioned, Data Zone Provisioned, and Global Provisioned, the reservation provides a discount in exchange for committing to payment for fixed number of PTUs for a one-month or one-year period.  
 
 * Azure Reservations are purchased via the Azure portal, not the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) Link to Azure reservation portal.
 
@@ -167,9 +167,9 @@ Discounts on top of the hourly usage price can be obtained by purchasing an Azur
 > [!IMPORTANT] 
 > * Capacity availability for model deployments is dynamic and changes frequently across regions and models. To prevent you from purchasing a reservation for more PTUs than you can use, create deployments first, and then purchase the Azure Reservation to cover the PTUs you have deployed. This best practice will ensure that you can take full advantage of the reservation discount and prevent you from purchasing a term commitment that you cannot use. 
 >
-> * The Azure role and tenant policy requirements to purchase a reservation are different than those required to create a deployment or Azure OpenAI resource. Verify authorization to purchase reservations in advance of needing to do so. See Azure OpenAI [Provisioned reservation documentation](https://aka.ms/oai/docs/ptum-reservations) for more details.
+> * The Azure role and tenant policy requirements to purchase a reservation are different than those required to create a deployment or Azure AI Foundry resource. Verify authorization to purchase reservations in advance of needing to do so. See [Azure AI Foundry Provisioned Throughput Reservation](https://aka.ms/oai/docs/ptum-reservations) for more details.
 
-## Important: sizing Azure OpenAI provisioned reservations
+## Important: sizing Azure AI Foundry Provisioned Throughput Reservation
 
 The PTU amounts in reservation purchases are independent of PTUs allocated in quota or used in deployments. It's possible to purchase a reservation for more PTUs than you have in quota, or can deploy for the desired region, model, or version. Credits for over-purchasing a reservation are limited, and customers must take steps to ensure they maintain their reservation sizes in line with their deployed PTUs. 
  
@@ -180,7 +180,7 @@ Reservations for Global, Data Zone, and Regional deployments aren't interchangea
 
 To assist customers with purchasing the correct reservation amounts. The total number of PTUs in a subscription and region that can be covered by a reservation are listed on the Quotas page of Azure AI Foundry. See the message "PTUs Available for reservation." 
 
-:::image type="content" source="../media/provisioned/available-quota.png" alt-text="A screenshot showing available PTU quota." lightbox="../media/provisioned/available-quota.png":::
+:::image type="content" source="../media/provisioned/ptu-quota-page.png" alt-text="A screenshot showing available PTU quota." lightbox="../media/provisioned/available-quota.png":::
 
 Managing Azure Reservations 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョンドスループットのオンボーディングガイドを更新"
}
```

### Explanation
この変更では、`provisioned-throughput-onboarding.md` ファイルにおいて、いくつかの重要な修正が行われました。主な変更点は、Azure OpenAIという表現がAzure AI Foundryに置き換えられたことです。これにより、最新のプラットフォームを反映した明確なガイドラインが提供されています。

ドキュメント内のさまざまなセクションで、プロビジョンドスループットに関連する料金や課金に関する情報が更新されています。たとえば、各プロビジョニングタイプの説明や、Azure Reservationsに関する情報がより具体的かつ統一感のある内容に改善されています。

また、利用者が必要なPTU数を決定するための手順や、キャパシティプランナーの使用に関する情報も強化され、利用者が自分の必要に応じたリソースの計画をしやすいように配慮されています。これらの変更は、プロビジョンドスループットの利活用を促進し、全体的な利用体験を向上させることを目的としています。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -1,40 +1,38 @@
 ---
 title: Global Provisioned model availability
-titleSuffix: Azure OpenAI in Azure AI Foundry Models
-description: Global PTU-managed model availability by region.
+description: Global PTU model availability by region for Foundry models.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
 ms.date: 05/05/2025
 ---
 
-
-| **Region**     | **o3**, **2025-04-16**   | **o4-mini**, **2025-04-16**   | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-nano**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:----------------------:|:---------------------------:|:---------------------------:|:--------------------------------:|:--------------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
-| australiaeast      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| brazilsouth        | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| canadaeast         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus             | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus2            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| francecentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| italynorth         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| japaneast          | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| koreacentral       | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| northcentralus     | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| norwayeast         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| polandcentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southafricanorth   | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southcentralus     | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southeastasia      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southindia         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| spaincentral       | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandnorth   | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandwest    | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| uaenorth           | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| uksouth            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westeurope         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus             | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| **Region**         | **o3**<br>2025-04-16 | **o4-mini**<br>2025-04-16 | **gpt-4.1**<br>2025-04-14 | **gpt-4.1-nano**<br>2025-04-14 | **gpt-4.1-mini**<br>2025-04-14 | **o3-mini**<br>2025-01-31 | **o1**<br>2024-12-17 | **gpt-4o**<br>2024-05-13 | **gpt-4o**<br>2024-08-06 | **gpt-4o**<br>2024-11-20 | **gpt-4o-mini**<br>2024-07-18 | **DeepSeek-R1** | **DeepSeek-V3-0324** |
+|:-------------------|:-------------------:|:------------------------:|:------------------------:|:-----------------------------:|:-----------------------------:|:------------------------:|:-------------------:|:------------------------:|:------------------------:|:------------------------:|:----------------------------:|:--------------:|:---------------------:|
+| australiaeast      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| brazilsouth        | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| canadaeast         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| eastus             | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| eastus2            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| francecentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| germanywestcentral | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| italynorth         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| japaneast          | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| koreacentral       | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| northcentralus     | ✅                   | ✅                        | ✅                        | -                              | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| norwayeast         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| polandcentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| southafricanorth   | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| southcentralus     | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| southeastasia      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| southindia         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| spaincentral       | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| swedencentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| switzerlandnorth   | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| switzerlandwest    | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| uaenorth           | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| uksouth            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| westeurope         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| westus             | ✅                   | ✅                        | ✅                        | -                              | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
+| westus3            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルプロビジョンドモデルの可用性を更新"
}
```

### Explanation
この変更では、`provisioned-global.md` ファイルの内容が更新され、グローバルプロビジョンドモデルの可用性に関する情報が調整されました。具体的には、Azure OpenAIの情報がAzure AI Foundryに統合され、このプラットフォームにおけるモデルの可用性が明確に示されています。

テーブルのヘッダーには各モデルのバージョンと日付が追加され、各地域におけるモデルの利用可能状況が一目で分かりやすくなりました。具体的には、モデル名が段落の中でより視覚的に区分され、利用可能なかどうかが確認しやすくなっています。

さらに、この更新により不要な情報が削除され、内容が精整されているため、より具体的で関連性の高い情報が集中した構成となっています。これにより、利用者は自分のニーズに適したモデルを見つけやすくなります。全体として、文書の明確さと使いやすさが向上しています。

## articles/ai-services/openai/media/provisioned/available-quota.png{#item-439bf9}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "利用可能なクォータ画像を更新"
}
```

### Explanation
この変更は、`available-quota.png` ファイルに対する修正を示しています。具体的には、画像に関して追加や削除は行われていませんが、ファイル自体が何らかの形で更新されたことを反映しています。

画像は、プロビジョンドスループットに関するクォータの可用性を示すために使用されており、ユーザーが現在のリソース使用状況を把握するのに役立ちます。この更新により、関連するドキュメントで使用されるビジュアル情報が最新化され、ユーザーに対する情報提供の質が向上することが期待されます。

この変更は、全体的には変更内容が目に見えないものであるため、実際には視覚的な情報が改良され、ユーザーがより良い理解を得られるよう配慮されています。

## articles/ai-services/openai/media/provisioned/deepseek-deployment.png{#item-20d652}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "DeepSeekデプロイメント画像の追加"
}
```

### Explanation
この変更では、`deepseek-deployment.png` という新しい画像ファイルが追加されました。この画像は、DeepSeekのデプロイメントに関連する情報を視覚的に示すために使用される予定です。

新たに追加された画像は、ユーザーがDeepSeekのデプロイメントプロセスやその関連情報を理解するのに役立つツールとして機能します。この視覚資料によって、ドキュメントや記事全体の内容がより理解しやすくなり、利用者に対する説明が強化されます。

画像の追加は、特に技術的なコンセプトやプロセスを視覚的に示すことにより、文章だけでは伝わりにくい情報を補完するための重要なステップです。この変更により、ユーザーはDeepSeekに関連する情報をより効果的に吸収できると考えられます。

## articles/ai-services/openai/media/provisioned/deployment-screen.png{#item-5bc2ef}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントスクリーン画像の更新"
}
```

### Explanation
この変更は、`deployment-screen.png` という画像ファイルが更新されたことを示しています。具体的な追加や削除はありませんが、既存の画像が何らかの理由で改訂されたことを反映しています。

このデプロイメントスクリーン画像は、AIサービスのデプロイメントプロセスに関連する内容を示すために使用され、ユーザーがシステムの設定や作業の進行状況を視覚的に把握できるようにします。画像の更新により、情報の正確性や関連性が保たれ、ドキュメント全体の品質向上に寄与することが期待されます。

更新された画像は、ユーザーにとってより明確で、理解しやすい情報を提供するものであり、技術的な文脈での認識を助ける重要な役割を果たします。この変更は、ユーザーがより良い体験を得られるよう、視覚資料を最新の内容に保つための重要な一歩です。

## articles/ai-services/openai/media/provisioned/fungible-quota.png{#item-2f93fd}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファンジブルクォータ画像の追加"
}
```

### Explanation
この変更では、`fungible-quota.png` という新たな画像ファイルが追加されました。この画像は、ファンジブルクォータに関連する情報を視覚的に提供するために使用されることを目的としています。

ファンジブルクォータは、AIサービスの使用やリソースの管理において重要な概念です。この画像の追加により、ユーザーはファンジブルクォータの設定や管理方法をより直感的に理解できるようになります。

視覚的な資料は、複雑な概念を説明する際に特に有効であり、文章だけでは伝えきれない情報を補完する役割を果たします。この新しい画像が導入されたことで、ユーザーはAIサービスに関するディスカッションや理解を深めるためのより効果的なリソースを得ることができます。

## articles/ai-services/openai/media/provisioned/model-independent-quota.png{#item-29a034}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル非依存クォータ画像の更新"
}
```

### Explanation
この変更は、`model-independent-quota.png` という画像ファイルが更新されたことを示しています。具体的には、追加や削除はないものの、既存の画像が何らかの形で改訂されたことを反映しています。

モデル非依存クォータは、AIサービスを利用する際に異なるモデルに関連するリソースの割り当てを管理するための重要な要素です。この画像の更新により、ユーザーに対して最新の情報が提供され、視覚的な説明がより正確で、関連性のあるものとなることが期待されます。

更新された画像は、ユーザーがモデル非依存クォータの概念を理解するためのサポートを提供し、全体のドキュメントの品質を向上させる役割を果たします。この更新は、情報伝達の明確さを向上させるための重要な改訂であり、ユーザーがAIサービスの使用においてより良い理解を得られるように支援します。

## articles/ai-services/openai/media/provisioned/ptu-quota-page.png{#item-aedb7d}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PTUクォータページ画像の更新"
}
```

### Explanation
この変更は、`ptu-quota-page.png` という画像ファイルが更新されたことを示しています。具体的には、画像に対する追加や削除は行われていませんが、既存の画像が何らかの理由で修正されたことが反映されています。

PTUクォータは、AIサービスにおけるリソース管理の重要な部分であり、この画像はその概念を視覚的に表現する役割を果たしています。更新された画像により、ユーザーはPTUクォータの管理手法や関連情報をより適切に理解できるようになります。

このようなマイナーな更新は、情報の正確性や視覚的な魅力を保つために重要であり、ユーザーが必要なリソースを効果的に利用できるよう支援します。また、更新により、全体のドキュメントの品質が向上し、ユーザーに提供される情報がよりタイムリーで関連性のあるものであることを確保します。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -283,7 +283,7 @@ items:
         href: ./how-to/monitor-openai.md
       - name: Provisioned throughput units (PTU)
         items:
-        - name: What is the Provisioned Managed offering (PTU)?
+        - name: What is the Provisioned Throughput offering (PTU)?
           href: ./concepts/provisioned-throughput.md
           displayName: PTU, provisioned, provisioned throughput units
         - name: Understanding and calculating PTU costs 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PTUの用語修正"
}
```

### Explanation
この変更は、`toc.yml` ファイルの内容がわずかに更新されたことを示しています。具体的には、"Provisioned Managed offering (PTU)" から "Provisioned Throughput offering (PTU)" への用語の修正が行われています。この変更によって、PTUに関連するリソースの名称がより正確かつ明確になります。

この用語の更新は、ユーザーが提供される情報の理解を助け、混乱を避けるために重要です。また、ドキュメント全体の整合性を確保し、ユーザーが正確な情報を基にした決定を行えるようにするための重要な要素でもあります。

このようなマイナーな更新は、テクニカルライティングやドキュメンテーションの品質を維持するために欠かせないものであり、ユーザーに対する信頼性を高める役割を果たします。これにより、効果的な情報提供が可能となり、ユーザーの体験向上にも寄与します。


