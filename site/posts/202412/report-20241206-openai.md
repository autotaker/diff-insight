---
date: '2024-12-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:04e3114...MicrosoftDocs:d62332b
summary: このコードの差分では、Azure OpenAIに関連するドキュメントが更新され、新しい機能「データゾーンプロビジョニング」が追加されました。また、APIキー設定方法の明確化やデプロイメントオプションの追加、PTU関連トピックの整備も行われています。特記すべき破壊的変更はなく、これにより利用者は最新機能や変更点を理解しやすくなります。全体として、これらの更新はAzure
  OpenAIの利用体験を向上させ、エンタープライズレベルでの信頼性と柔軟性を強化しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:04e3114...MicrosoftDocs:d62332b){target="_blank"}

<format>
# Highlights
このコードの差分では、Azure OpenAIに関連する複数のドキュメントが更新されています。特に、新しい機能として「データゾーンプロビジョニング」の追加や、それに伴う情報の整理と修正が行われている点が目立ちます。また、APIキー設定方法の明確化、デプロイメントオプションの追記、PTU関連のトピック追加なども含まれており、利用者が最新の機能や変更点を理解しやすくなる工夫がされています。

## New features
- 「データゾーンプロビジョニング」の追加。
- プロビジョニング管理モデルに関する新規ドキュメントの追加。

## Breaking changes
- 特記すべき大きな破壊的変更は見られません。

## Other updates
- ドキュメントの日付や情報の更新。
- APIキー設定方法の修正。
- デプロイメントタイプやPTUに関するトピック、リンクの追加。

# Insights
このドキュメント更新は、Azure OpenAIを利用するユーザーに向けて、新しい機能やサービスの詳細な情報を提供することに重点を置いています。特に、「データゾーンプロビジョニング」の追加は、地域ごとに最適なデータセンターにトラフィックをルーティングする機能を提供し、可用性と効率を改善するものです。これにより、企業は特定のデータゾーンでの高い可用性を求めるニーズに応えることが可能になります。

また、APIキーの設定方法の修正は、開発者が誤解しにくくなるように配慮された変更であり、実装上のエラーを減少させる成果が期待されます。

一方で、プロビジョニングデプロイメントのガイドや、PTUクォータに関する情報が追記されたことにより、新規及び既存のユーザーが適切にリソースを利用する方法を理解しやすくなっています。各種ドキュメントの更新は、Azure OpenAIの利用を円滑に進めるための重要なサポートを提供し、利用者体験の向上につながるでしょう。

これらの更新は、Azureが提供するAIサービスの信頼性と柔軟性を強化するものであり、エンタープライズレベルでの利用にも応えられるような詳細な情報が提供されています。特に、データゾーン管理に関する新しい情報は、データ主権や法的要件に配慮する企業にとって有益な選択肢となります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | モデルに関する情報の更新と修正 | modified | 8 | 2 | 10 | 
| [provisioned-reservation-update.md](#item-53236b) | new feature | Azure OpenAIの2024年12月のプロビジョニング更新 | added | 71 | 0 | 71 | 
| [provisioned-throughput.md](#item-022e0c) | minor update | プロビジョニングスループットドキュメントの内容更新 | modified | 23 | 22 | 45 | 
| [deployment-types.md](#item-210814) | minor update | デプロイメントタイプに関するドキュメントの修正 | modified | 9 | 2 | 11 | 
| [embeddings.md](#item-e38d07) | minor update | APIキーの設定方法に関する修正 | modified | 1 | 1 | 2 | 
| [provisioned-get-started.md](#item-c8df1c) | minor update | プロビジョニングデプロイメントの開始に関するガイドの更新 | modified | 17 | 15 | 32 | 
| [datazone-provisioned-managed.md](#item-ae7f5b) | new feature | データゾーンのプロビジョニング管理モデルの可用性に関する新規ドキュメントの追加 | added | 16 | 0 | 16 | 
| [toc.yml](#item-c945af) | minor update | Azure OpenAIのPTU予約更新に関するトピックの追加 | modified | 2 | 0 | 2 | 
| [whats-new.md](#item-53303b) | minor update | 2024年12月の新しいデータゾーンプロビジョニングデプロイメントタイプの追加 | modified | 8 | 0 | 8 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 10/25/2024
+ms.date: 12/05/2024
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -388,7 +388,13 @@ All deployments can perform the exact same inference operations, however the bil
 
 ### Data zone standard model availability
 
-[!INCLUDE [Global batch](../includes/model-matrix/datazone-standard.md)]
+[!INCLUDE [Data zone standard](../includes/model-matrix/datazone-standard.md)]
+
+# [Data Zone Provisioned Managed](#tab/datazone-provisioned-managed)
+
+### Data zone provisioned managed model availability
+
+[!INCLUDE [Global data zone provisioned managed](../includes/model-matrix/datazone-provisioned-managed.md)]
 
 # [Standard](#tab/standard)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルに関する情報の更新と修正"
}
```

### Explanation
このコードの差分は、Azure OpenAIに関するドキュメントの一部を修正および更新することを目的としています。具体的には、ドキュメントの日付を2024年10月25日から2024年12月5日へと変更し、新たに「データゾーン管理モデルの可用性」に関するセクションを追加しました。また、既存のグローバルバッチのインクルードを「データゾーン標準」のインクルードに置き換えています。全体として、8の行が追加され、2の行が削除されており、情報がより最新かつ正確になるように調整されています。この更新は、Azure OpenAIの機能を利用するユーザーにとって便利な情報となるでしょう。

## articles/ai-services/openai/concepts/provisioned-reservation-update.md{#item-53236b}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,71 @@
+---
+title: 'Azure OpenAI Provisioned December 2024 Update'
+titleSuffix: Azure OpenAI
+description: Learn about new Provisioned skus and commercial changes for Provisioned offers
+manager: chrhoder
+ms.service: azure-ai-openai
+ms.custom:
+ms.topic: how-to
+ms.date: 11/25/2024
+author: sydneemayers
+ms.author: sydneemayers
+recommendations: false
+---
+# Azure OpenAI provisioned December 2024 update 
+
+In early December, 2024, Microsoft launched several changes to the provisioned offering. These changes include:
+- A new deployment type, **data zone provisioned**.
+- Updated hourly pricing for global and data zone provisioned deployment types
+- New Azure Reservations for global and data zone provisioned deployment types
+
+This article is intended for existing users of the provisioned throughput offering. New customers should refer to the [Azure OpenAI provisioned onboarding guide](../how-to/provisioned-throughput-onboarding.md).
+
+## What's changing?
+
+The changes below apply to the global provisioned, data zone provisioned, and provisioned deployment types.
+
+> [!IMPORTANT]
+> The changes in this article do not apply to the older *"Provisioned Classic (PTU-C)"* offering. They only affect the Provisioned (also known as the Provisioned Managed) offering.
+
+### Data zone provisioned
+Data zone provisioned deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. Data zone provisioned deployments provide reserved model processing capacity for high and predictable throughput using Azure global infrastructure within the Microsoft defined data zone. Data zone deployments are supported for gpt-4o and gpt-4o-mini model families. 
+
+For more information, see the [deployment types guide](https://aka.ms/aoai/docs/deployment-types).
+
+### New hourly pricing for global and data zone provisioned deployments
+In August 2024, Microsoft announced that Provisioned deployments would move to a new [hourly payment model](./provisioned-migration.md) with the option to purchase Azure Reservations to support additional discounts. In December's provisioned update, we will be introducing differentiated hourly pricing across global provisioned, data zone provisioned, and provisioned deployment types. For more information on the hourly price for each provisioned deployment type, see the [Pricing details page](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). 
+
+### New Azure Reservations for global and data zone provisioned deployments
+In addition to the updates for the hourly payment model, new Azure Reservations will be introduced specifically for global and data zone provisioned deployment types. With these new Azure Reservations, every provisioned deployment type will have a separate Azure Reservation that can be purchased to support additional discounts. The mapping between each provisioned deployment type and the associated Azure Reservation are as follows:
+
+| Provisioned deployment type | Sku name in code  | Azure Reservation product name |
+|---|---|---|
+| Global provisioned | `GlobalProvisionedManaged`  | Provisioned Managed Global  |
+| Data zone provisioned | `DataZoneProvisionedManaged`  | Provisioned Managed Data Zone  |
+| Provisioned | `ProvisionedManaged`  | Provisioned Managed Regional |
+
+> [!IMPORTANT]
+> Azure Reservations for Azure OpenAI provisioned offers are not interchangeable across deployment types. The Azure Reservation purchased must match the provisioned deployment type. If the Azure Reservation purchased does not match the provisioned deployment type, the provisioned deployment will default to the hourly payment model until a matching Azure Reservation product is purchased. For more information, see the [Azure Reservations for Azure OpenAI Service provisioned guidance](https://aka.ms/oai/docs/ptum-reservations).
+
+## Migrating existing deployments to global or data zone provisioned
+Existing customers of provisioned deployments can choose to migrate to global or data zone provisioned deployments to benefit from the lower deployment minimums, granular scale increments, or differentiated pricing available for these deployment types. To learn more about how global and data zone provisioned deployments handle data processing across Azure geographies, see the Azure OpenAI deployment [data processing documentation](https://aka.ms/aoai/docs/data-processing-locations).
+
+Two approaches are available for customers to migrate from provisioned deployments to global or data zone provisioned deployments. 
+
+### Zero downtime migration 
+The zero downtime migration approach allows customers to migrate their existing provisioned deployments to global or data zone provisioned deployments without interrupting the existing inference traffic on their deployment. This migration approach minimizes workload interruptions, but does require a customer to have multiple coexisting deployments while shifting traffic over. The process to migrate a provisioned deployment using the zero downtime migration approach is as follows:
+- Create a new deployment using the global or data zone provisioned deployment types in the target Azure OpenAI resource.
+- Transition traffic from the existing regional provisioned deployment type to the newly created global or data zone provisioned deployment until all traffic is offloaded from the existing regional provisioned deployment.
+- Once traffic is migrated over to the new deployment, validate that there are no inference requests being processed on the previous provisioned deployment by ensuring the Azure OpenAI Requests metric does not show any API calls made within 5-10 minutes of the inference traffic being migrated over to the new deployment. For more information on this metric, [see the Monitor Azure OpenAI documentation](https://aka.ms/aoai/docs/monitor-azure-openai).
+- Once you confirm that no inference calls have been made, delete the regional provisioned deployment.
+
+### Migration with downtime 
+The migration with downtime approach involves migrating existing provisioned deployments to global or data zone provisioned deployments while stopping any existing inference traffic on the original provisioned deployment. This migration approach does not require coexistence of multiple deployments to support but does require workload interruption to complete. The process to migrate a provisioned deployment using the migration with downtime approach is as follows:
+- Validate that there are no inference requests being processed on the previous provisioned deployment by ensuring the Azure OpenAI Requests metric does not show any API calls made within the last 5-10 minutes. For more information on this metric, [see the Monitor Azure OpenAI documentation](https://aka.ms/aoai/docs/monitor-azure-openai).
+- Once you confirm that no inference calls have been made, delete the regional provisioned deployment.
+- Create a new deployment using the global or data zone deployment types in the target Azure OpenAI resource.
+- Once your new deployment has succeeded, you may resume inference traffic on the new global or data zone deployment.
+
+## How do I migrate my existing Azure Reservation to the new Azure Reservation products?
+Azure Reservations for Azure OpenAI Service provisioned offers are specific to the provisioned deployment type. If the Azure Reservation purchased does not match the provisioned deployment type, the deployment will default to the hourly payment model. If you choose to migrate to global or data zone provisioned deployments, you may need to purchase a new Azure Reservation for these deployments to support additional discounts. For more information on how to purchase a new Azure Reservation or make changes to an existing Azure Reservation, see the [Azure Reservations for Azure OpenAI Service Provisioned guidance](https://aka.ms/aoai/reservation-transition).
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIの2024年12月のプロビジョニング更新"
}
```

### Explanation
このコードの差分は、新しい記事「Azure OpenAI Provisioned December 2024 Update」を追加することを目的としています。この文書では、2024年の12月に発表されるAzure OpenAIのプロビジョニングオファーの変更点について詳細に説明しています。具体的には、新しいデプロイメントタイプ「データゾーンプロビジョニング」の導入や、グローバルおよびデータゾーンプロビジョニングデプロイメントの新しい時間単価についての情報が含まれています。

また、Azure Reservationsの新しいオファーについても詳述されており、これにより提供されるプロビジョニングタイプに応じて異なるディスカウントを利用する方法が説明されています。既存の顧客が新しいデプロイメントに移行するための手段も2つのアプローチで紹介され、ゼロダウンタイムの移行やダウンタイムを伴う移行手法についても解説されています。この更新は、現在のユーザー及び新規顧客にとって、Azure OpenAIサービスの最新のオファーとその利用方法を理解する上で重要な情報源となります。

## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -14,39 +14,40 @@ recommendations: false
 
 > [!NOTE]
 > The Azure OpenAI Provisioned offering received significant updates on August 12, 2024, including aligning the purchase model with Azure standards and moving to model-independent quota. It is highly recommended that customers onboarded before this date read the Azure [OpenAI provisioned August update](./provisioned-migration.md) to learn more about these changes.
- 
+
+
 The provisioned throughput capability allows you to specify the amount of throughput you require in a deployment. The service then allocates the necessary model processing capacity and ensures it's ready for you. Throughput is defined in terms of provisioned throughput units (PTU) which is a normalized way of representing the throughput for your deployment. Each model-version pair requires different amounts of PTU to deploy and provide different amounts of throughput per PTU. 
 
-## What do the provisioned and global provisioned deployment types provide?
+## What do the provisioned deployment types provide?
 
 - **Predictable performance:** stable max latency and throughput for uniform workloads. 
 - **Reserved processing capacity:** A deployment configures the amount of throughput. Once deployed, the throughput is available whether used or not.
 - **Cost savings:** High throughput workloads might provide cost savings vs token-based consumption.
 
-An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model. A deployment provides customer access to a model for inference and integrates more features like Content Moderation ([See content moderation documentation](content-filter.md)). Global deployments are available in the same Azure OpenAI resources as non-global deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center with best availability for each request.
+An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model. A deployment provides customer access to a model for inference and integrates more features like Content Moderation ([See content moderation documentation](content-filter.md)). Global provisioned deployments are available in the same Azure OpenAI resources as all other deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center with the best availability for each request. Similarly, data zone provisioned deployments are also available in the same resources as all other deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center within the Microsoft specified data zone with the best availability for each request. 
 
 ## What do you get?
 
 | Topic | Provisioned|
 |---|---|
 | What is it? | Provides guaranteed throughput at smaller increments than the existing provisioned offer. Deployments have a consistent max latency for a given model-version. |
 | Who is it for? | Customers who want guaranteed throughput with minimal latency variance. |
-| Quota | Provisioned Managed Throughput Unit or Global Provisioned Managed Throughput Unit assigned per region. Quota can be used across any available Azure OpenAI model.|
+| Quota |Provisioned Managed Throughput Unit, Global Provisioned Managed Throughput Unit, or Data Zone Provisioned Managed Throughput Unit assigned per region. Quota can be used across any available Azure OpenAI model.|
 | Latency | Max latency constrained from the model. Overall latency is a factor of call shape.  |
 | Utilization | Provisioned-managed Utilization V2 measure provided in Azure Monitor. |
-| Estimating size | Provided calculator in the studio & benchmarking script. |
-| Prompt caching | For supported models, we discount up to 100% of cached input tokens. |
+| Estimating size | Provided calculator in Azure AI Foundry & benchmarking script. |
+|Prompt caching | For supported models, we discount up to 100% of cached input tokens. |
 
 
 ## How much throughput per PTU you get for each model
 The amount of throughput (tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in the minute. Generating output tokens requires more processing than input tokens and so the more output tokens generated the lower your overall TPM. The service dynamically balances the input & output costs, so users do not have to set specific input and output limits. This approach means your deployment is resilient to fluctuations in the workload shape. 
 
 To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the `gpt-4o` and `gpt-4o-mini` models which represent the max TPM assuming all traffic is either input or output. To understand how different ratios of input and output tokens impact your Max TPM per PTU, see the [Azure OpenAI capacity calculator](https://oai.azure.com/portal/calculator). The table also shows Service Level Agreement (SLA) Latency Target Values per model.  For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
 
-|| **gpt-4o**, **2024-05-13**   & **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
+|Topic| **gpt-4o**, **2024-05-13**   & **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
 | --- | --- | --- |
-|Global provisioned minimum deployment|15|15|
-|Global provisioned scale increment|5|5|
+|Global & data zone provisioned minimum deployment|15|15|
+|Global & data zone provisioned scale increment|5|5|
 |Regional provisioned minimum deployment | 50 | 25|
 |Regional provisioned scale increment|50|25|
 |Max Input TPM per PTU | 2,500 | 37,000  |
@@ -57,15 +58,15 @@ For a full list see the [AOAI Foundry calculator](https://oai.azure.com/portal/c
 
 
 > [!NOTE]
-> Global provisioned deployments are only supported for gpt-4o, 2024-08-06 and gpt-4o-mini, 2024-07-18 models at this time. For more information on model availability, review the [models documentation](./models.md).
+> Global provisioned deployments are only supported for gpt-4o, 2024-08-06 and gpt-4o-mini, 2024-07-18 models at this time. Data zone provisioned deployments are only supported for gpt-4o, 2024-08-06, gpt-4o, 2024-05-13, and gpt-4o-mini, 2024-07-18 models at this time. For more information on model availability, review the [models documentation](./models.md).
 
 ## Key concepts
 
 ### Deployment types
 
-When creating a provisioned deployment in Azure OpenAI Studio, the deployment type on the Create Deployment dialog is Provisioned-Managed. When creating a global provisioned managed deployment in Azure Open Studio, the deployment type on the Create Deployment dialog is Global Provisioned-Managed.
+When creating a provisioned deployment in Azure AI Foundry, the deployment type on the Create Deployment dialog can be set to the Global Provisioned-Managed, DataZone Provisioned-Managed, or regional Provisioned-Managed deployment type depending on the data processing needs for the given workload.
 
-When creating a provisioned deployment in Azure OpenAI via CLI or API, you need to set the `sku-name` to be `ProvisionedManaged`. When creating a global provisioned deployment in Azure OpenAI via CLI or API, you need to set the `sku-name` to be `GlobalProvisionedManaged`. The `sku-capacity` specifies the number of PTUs assigned to the deployment. 
+When creating a provisioned deployment in Azure OpenAI via CLI or API, the `sku-name` can be set to `GlobalProvisionedManaged`, `DataZoneProvisionedManaged`, or `ProvisionedManaged` depending on the data processing need for the given workload. To adapt the Azure CLI example command below to a different deployment type, simply update the `sku-name` parameter to match the deployment type you wish to deploy.
 
 ```azurecli
 az cognitiveservices account deployment create \
@@ -92,13 +93,13 @@ Unlike the Tokens Per Minute (TPM) quota used by other Azure OpenAI offerings, P
 
 :::image type="content" source="../media/provisioned/model-independent-quota.png" alt-text="Diagram of model independent quota with one pool of PTUs available to multiple Azure OpenAI models." lightbox="../media/provisioned/model-independent-quota.png":::
 
-For provisioned deployments, the new quota shows up in Azure OpenAI Studio as a quota item named **Provisioned Managed Throughput Unit**. For global provisioned managed deployments, the new quota shows up in the Azure OpenAI Studio as a quota item named **Global Provisioned Managed Throughput Unit**.  In the Studio Quota pane, expanding the quota item shows the deployments contributing to usage of each quota.
+For provisioned deployments, the new quota shows up in Azure AI Foundry as a quota item named **Provisioned Managed Throughput Unit**. For global provisioned deployments, the new quota shows up in the Azure AI Foundry as a quota item named **Global Provisioned Managed Throughput Unit**.  For data zone provisioned deployments, the new quota shows up in Azure AI Foundry as a quota item named **Data Zone Provisioned Managed Throughput Unit.** In the Foundry Quota pane, expanding the quota item shows the deployments contributing to usage of each quota.
 
 :::image type="content" source="../media/provisioned/ptu-quota-page.png" alt-text="Screenshot of quota UI for Azure OpenAI provisioned." lightbox="../media/provisioned/ptu-quota-page.png":::
 
 #### Obtaining PTU Quota 
 
-PTU quota is available by default in many regions. If more quota is required, customers can request quota via the Request Quota link. This link can be found to the right of the Provisioned Managed Throughput Unit or Global Provisioned Managed Throughput Unit quota tabs in the Azure OpenAI Studio. The form allows the customer to request an increase in the specified PTU quota for a given region. The customer receives an email at the included address once the request is approved, typically within two business days. 
+PTU quota is available by default in many regions. If more quota is required, customers can request quota via the Request Quota link. This link can be found to the right of the designated provisioned deployment type quota tabs in Azure AI Foundry The form allows the customer to request an increase in the specified PTU quota for a given region. The customer receives an email at the included address once the request is approved, typically within two business days. 
 
 #### Per-Model PTU Minimums 
 
@@ -115,9 +116,9 @@ Azure OpenAI is a highly sought-after service where customer demand might exceed
 
 #### Regional capacity guidance
 
-To find the capacity needed for their deployments, use the capacity  API or the Studio deployment experience to provide real-time information on capacity availability.
+To find the capacity needed for their deployments, use the capacity API or the AI Foundry deployment experience to provide real-time information on capacity availability.
 
-In Azure OpenAI Studio, the deployment experience identifies when a region lacks the capacity needed to deploy the model. This looks at the desired model, version and number of PTUs. If capacity is unavailable, the experience direct  users to a select an alternative region.
+In Azure AI Foundry, the deployment experience identifies when a region lacks the capacity needed to deploy the model. This looks at the desired model, version and number of PTUs. If capacity is unavailable, the experience directs  users to a select an alternative region.
 
 Details on the new deployment experience can be found in the Azure OpenAI [Provisioned get started guide](../how-to/provisioned-get-started.md).
 
@@ -127,7 +128,7 @@ If an acceptable region isn't available to support the desire model, version and
 
 - Attempt the deployment with a smaller number of PTUs.
 - Attempt the deployment at a different time. Capacity availability changes dynamically based on customer demand and more capacity might become available later.
-- Ensure that quota is available in all acceptable regions. The [model capacities API](/rest/api/aiservices/accountmanagement/model-capacities/list?view=rest-aiservices-accountmanagement-2024-04-01-preview&tabs=HTTP&preserve-view=true) and Studio experience consider quota availability in returning alternative regions for creating a deployment.
+- Ensure that quota is available in all acceptable regions. The [model capacities API](/rest/api/aiservices/accountmanagement/model-capacities/list?view=rest-aiservices-accountmanagement-2024-04-01-preview&tabs=HTTP&preserve-view=true) and AI Foundry experience consider quota availability in returning alternative regions for creating a deployment.
 
 ### Determining the number of PTUs needed for a workload
 
@@ -139,13 +140,13 @@ A few high-level considerations:
 
 ### How utilization performance works
 
-Provisioned and global provisioned deployments provide you with an allocated amount of model processing capacity to run a given model.
+Provisioned deployments provide you with an allocated amount of model processing capacity to run a given model.
 
-In Provisioned-Managed and Global Provisioned-Managed deployments, when capacity is exceeded, the API will return a 429 HTTP Status Error. This fast response enables the user to make decisions on how to manage their traffic. Users can redirect requests to a separate deployment, to a standard pay-as-you-go instance, or use a retry strategy to manage a given request. The service continues to return the 429 HTTP status code until the utilization drops below 100%.
+In all provisioned deployment types, when capacity is exceeded, the API will return a 429 HTTP Status Error. This fast response enables the user to make decisions on how to manage their traffic. Users can redirect requests to a separate deployment, to a standard pay-as-you-go instance, or use a retry strategy to manage a given request. The service continues to return the 429 HTTP status code until the utilization drops below 100%.
 
 ### How can I monitor capacity?
 
-The [Provisioned-Managed Utilization V2 metric](../how-to/monitoring.md#azure-openai-metrics) in Azure Monitor measures a given deployments utilization on 1-minute increments. Provisioned-Managed and Global Provisioned-Managed deployments are optimized to ensure that accepted calls are processed with a consistent model processing time (actual end-to-end latency is dependent on a call's characteristics).  
+The [Provisioned-Managed Utilization V2 metric](../how-to/monitoring.md#azure-openai-metrics) in Azure Monitor measures a given deployments utilization on 1-minute increments. All provisioned deployment types are optimized to ensure that accepted calls are processed with a consistent model processing time (actual end-to-end latency is dependent on a call's characteristics).  
 
 #### What should  I do when I receive a 429 response?
 The 429 response isn't an error, but instead part of the design for telling users that a given deployment is fully utilized at a point in time. By providing a fast-fail response, you have control over how to handle these situations in a way that best fits your application requirements.
@@ -156,9 +157,9 @@ The  `retry-after-ms` and `retry-after` headers in the response tell you the tim
 
 #### How does the service decide when to send a 429?
 
-In the Provisioned-Managed and Global Provisioned-Managed offerings, each request is evaluated individually according to its prompt size, expected generation size, and model to determine its expected utilization. This is in contrast to pay-as-you-go deployments, which have a [custom rate limiting behavior](../how-to/quota.md) based on the estimated traffic load. For pay-as-you-go deployments this can lead to HTTP 429 errors being generated prior to defined quota values being exceeded if traffic is not evenly distributed.
+In all provisioned deployment types, each request is evaluated individually according to its prompt size, expected generation size, and model to determine its expected utilization. This is in contrast to pay-as-you-go deployments, which have a [custom rate limiting behavior](../how-to/quota.md) based on the estimated traffic load. For pay-as-you-go deployments this can lead to HTTP 429 errors being generated prior to defined quota values being exceeded if traffic is not evenly distributed.
 
-For Provisioned-Managed and Global Provisioned-Managed, we use a variation of the leaky bucket algorithm to maintain utilization below 100% while allowing some burstiness in the traffic. The high-level logic is as follows:
+For provisioned deployments, we use a variation of the leaky bucket algorithm to maintain utilization below 100% while allowing some burstiness in the traffic. The high-level logic is as follows:
 
 1.	Each customer has a set amount of capacity they can utilize on a deployment
 1. When a request is made:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングスループットドキュメントの内容更新"
}
```

### Explanation
このコードの差分は、Azure OpenAIの「プロビジョニングスループット」に関するドキュメントの更新を目的としています。具体的には、文書の一部が改訂され、プロビジョニングスループットの特性や利用方法についての最新情報が加えられています。

主な変更点には、プロビジョニングデプロイメントタイプの説明が整理され、データゾーンプロビジョニングのデプロイメントについても言及されています。さらに、スループットの許可単位（PTU）の情報が、データゾーンプロビジョニングに対しても明示的に記載され、プロビジョニングデプロイメントの作成時に設定するSKU名が具体的に説明されています。

追加された内容は、モデルごとのPTUあたりのスループット量や、エラー応答がどのように処理されるか、利用状況の監視方法などに関する情報で、顧客が最新の仕様や変更に理解を深める助けとなるでしょう。この更新は、Azure OpenAIを利用しているユーザーにとって、スループットや利用状況の管理に関する重要な情報を提供します。

## articles/ai-services/openai/how-to/deployment-types.md{#item-210814}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ ms.author: mbullwin
 
 # Azure OpenAI deployment types
 
-Azure OpenAI provides customers with choices on the hosting structure that fits their business and usage patterns. The service offers two main types of deployments: **standard** and **provisioned**. For a given deployment type, customers can align their workloads with their data processing requirements by choosing an Azure geography (`Standard` or `Provisioned`), Microsoft specified data zone (`DataZone-Standard`), or Global (`Global-Standard` or `Global Provisioned-Managed`) processing options.
+Azure OpenAI provides customers with choices on the hosting structure that fits their business and usage patterns. The service offers two main types of deployments: **standard** and **provisioned**. For a given deployment type, customers can align their workloads with their data processing requirements by choosing an Azure geography (`Standard` or `Provisioned-Managed`), Microsoft specified data zone (`DataZone-Standard` or `DataZone Provisioned-Managed`), or Global (`Global-Standard` or `Global Provisioned-Managed`) processing options.
 
 All deployments can perform the exact same inference operations, however the billing, scale, and performance are substantially different. As part of your solution design, you will need to make two key decisions:
 
@@ -96,6 +96,13 @@ Data zone standard deployments are available in the same Azure OpenAI resource a
 
 Customers with high consistent volume may experience greater latency variability. The threshold is set per model. See the [Quotas and limits](/azure/ai-services/openai/quotas-limits#usage-tiers) page to learn more. For workloads that require low latency variance at large volume, we recommend leveraging the provisioned deployment offerings. 
 
+## Data zone provisioned
+
+> [!IMPORTANT]
+> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location within the Microsoft specified data zone.[Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
+
+Data zone provisioned deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft specified data zone with the best availability for each request. Data zone provisioned deployments provide reserved model processing capacity for high and predictable throughput using Azure infrastructure within the Microsoft specified data zone.  
+
 ## Standard
 
 Standard deployments provide a pay-per-call billing model on the chosen model. Provides the fastest way to get started as you only pay for what you consume. Models available in each region as well as throughput may be limited.  
@@ -110,7 +117,7 @@ Provisioned deployments allow you to specify the amount of throughput you requir
 
 Azure Policy helps to enforce organizational standards and to assess compliance at-scale. Through its compliance dashboard, it provides an aggregated view to evaluate the overall state of the environment, with the ability to drill down to the per-resource, per-policy granularity. It also helps to bring your resources to compliance through bulk remediation for existing resources and automatic remediation for new resources. [Learn more about Azure Policy and specific built-in controls for AI services](/azure/ai-services/security-controls-policy).
 
-You can use the following policy to disable access to Azure OpenAI global standard deployments. To disable access to Azure global provisioned or global batch deployments, replace `GlobalStandard` with `GlobalProvisionedManaged` or `GlobalBatch` for the intended sku name. 
+You can use the following policy to disable access to any Azure OpenAI deployment type. To disable access to a specific deployment type, replace `GlobalStandard` with the sku name for the deployment type that you would like to disable access to. 
 
 ```json
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントタイプに関するドキュメントの修正"
}
```

### Explanation
このコードの差分は、「Azure OpenAIのデプロイメントタイプ」に関するドキュメントの内容を修正することを目的としています。修正内容は主にデプロイメントオプションの表現を明確にし、新たに「データゾーンプロビジョニング」のセクションを追加しています。

具体的には、データゾーンプロビジョニングデプロイメントが、Microsoftが指定したデータゾーン内で最良の可用性を持つデータセンターへトラフィックを動的にルーティングする機能を持つことが示されています。また、データが保存される場所に関する重要な注意書きも追加されており、データの居住地に関する情報へのリンクも提供されています。

さらに、グローバル標準デプロイメントと他のデプロイメントタイプへのアクセスを制御するためのポリシーについても言及があり、特定のデプロイメントタイプが無効にできる方法が説明されています。この更新は、Azure OpenAIを利用する顧客がデプロイメントの選択肢を理解しやすくするための重要な情報を提供しています。

## articles/ai-services/openai/how-to/embeddings.md{#item-e38d07}

<details>
<summary>Diff</summary>
````diff
@@ -56,7 +56,7 @@ print(response.model_dump_json(indent=2))
 import openai
 
 openai.api_type = "azure"
-openai.api_key = YOUR_API_KEY
+openai.api_key = "YOUR_API_KEY"
 openai.api_base = "https://YOUR_RESOURCE_NAME.openai.azure.com"
 openai.api_version = "2024-06-01"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIキーの設定方法に関する修正"
}
```

### Explanation
このコードの差分は、OpenAI APIを利用する際のAPIキーの設定方法を明確にするための修正です。具体的には、APIキーのプレースホルダーが `YOUR_API_KEY` から `"YOUR_API_KEY"` に変更されました。この変更は、APIキーが文字列として扱われることを明示化しています。

この修正により、ユーザーがAzure上でOpenAIを利用する際に、APIキーの設定についての誤解を減らし、正確な構文を理解する助けとなるでしょう。全体的に、この変更はドキュメントの可読性と正確性を向上させることを目的としています。

## articles/ai-services/openai/how-to/provisioned-get-started.md{#item-c8df1c}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ The following guide walks you through key steps in creating a provisioned deploy
 
 ## Obtain/verify PTU quota availability.
 
-Provisioned throughput deployments are sized in units called Provisioned Throughput Units (PTUs). PTU quota is granted to a subscription regionally and limits the total number of PTUs that can be deployed in that region across all models and versions. 
+Provisioned throughput deployments are sized in units called Provisioned Throughput Units (PTUs). PTU quota for each provisioned deployment type is granted to a subscription regionally and limits the total number of PTUs that can be deployed in that region across all models and versions. 
 
 Creating a new deployment requires available (unused) quota to cover the desired size of the deployment. For example: If a subscription has the following in South Central US: 
 
@@ -37,28 +37,29 @@ Creating a new deployment requires available (unused) quota to cover the desired
 
 Then 200 PTUs of quota are considered used, and there are 300 PTUs available for use to create new deployments. 
 
-A default amount of provisioned and global provisioned quota is assigned to all subscriptions in several regions. You can view the quota available to you in a region by visiting the Quotas blade in Azure OpenAI Studio and selecting the desired subscription and region. For example, the screenshot below shows a quota limit of 500 PTUs in West US for the selected subscription. Note that you might see lower values of available default quotas. 
+A default amount of global, data zone, and regional provisioned quota is assigned to eligible subscriptions in several regions. You can view the quota available to you in a region by visiting the Quotas pane in Azure AI Foundry and selecting the desired subscription and region. For example, the screenshot below shows a quota limit of 500 PTUs in West US for the selected subscription. Note that you might see lower values of available default quotas. 
 
 :::image type="content" source="../media/provisioned/available-quota.png" alt-text="A screenshot of the available quota in Azure OpenAI studio." lightbox="../media/provisioned/available-quota.png":::
 
 Additional quota can be requested by clicking the Request Quota link to the right of the “Usage/Limit” column.  (This is off-screen in the screenshot above). 
 
 ## Create an Azure OpenAI resource 
 
-Provisioned and global provisioned deployments are created via Azure OpenAI resource objects within Azure. You must have an Azure OpenAI resource in each region where you intend to create a deployment. Use the Azure portal to [create a resource](./create-resource.md) in a region with available quota, if required.  
+Provisioned deployments are created via Azure OpenAI resource objects within Azure. You must have an Azure OpenAI resource in each region where you intend to create a deployment. Use the Azure portal to [create a resource](./create-resource.md) in a region with available quota, if required.  
 
 > [!NOTE]
-> Azure OpenAI resources can support multiple types of Azure OpenAI deployments at the same time.  It is not necessary to dedicate new resources for your provisioned or global provisioned deployments. 
-## Create your provisioned or global provisioned deployment - capacity is available
+> Azure OpenAI resources can support multiple types of Azure OpenAI deployments at the same time.  It is not necessary to dedicate new resources for your provisioned deployments. 
+
+## Create your provisioned deployment - capacity is available
 
 once you have verified your quota, you can create a deployment. To create a provisioned deployment, you can follow these steps; the choices described reflect the entries shown in the screenshot. 
 
 :::image type="content" source="../media/provisioned/deployment-screen.png" alt-text="Screenshot of the Azure OpenAI Studio deployment page for a provisioned deployment." lightbox="../media/provisioned/deployment-screen.png":::
 
 
 
-1.	Sign into the [Azure OpenAI Studio](https://oai.azure.com)
-1. Choose the subscription that was enabled for provisioned and global provisioned deployments & select the desired resource in a region where you have the quota.
+1.	Sign into [Azure AI Foundry](https://oai.azure.com)
+1. Choose the subscription that was enabled for provisioned deployments & select the desired resource in a region where you have the quota.
 
 3.	Under **Management** in the left-nav select **Deployments**.
 4.	Select Create new deployment and configure the following fields. Expand the **advanced options** drop-down menu.
@@ -70,7 +71,7 @@ once you have verified your quota, you can create a deployment. To create a prov
 | Model version |	Choose the version of the model to deploy.	 | 0613 |
 | Deployment Name	 | The deployment name is used in your code to call the model by using the client libraries and the REST APIs.	| gpt-4|
 | Content filter	| Specify the filtering policy to apply to the deployment. Learn more on our [Content Filtering](../concepts/content-filter.md) how-to. | 	Default |
-| Deployment Type	|This impacts the throughput and performance. Choose Provisioned-Managed or Global Provisioned-Managed for your deployment 	| Provisioned-Managed |
+| Deployment Type	|This impacts the throughput and performance. Choose Global Provisioned-Managed, DataZone Provisioned-Managed or Provisioned-Managed from the deployment dialog dropdown for your deployment 	| Provisioned-Managed |
 | Provisioned Throughput Units |	Choose the amount of throughput you wish to include in the deployment. |	100 |
 
 Important things to note: 
@@ -87,7 +88,7 @@ The image below shows the pricing confirmation you will see. The price shown is
 
 :::image type="content" source="../media/provisioned/confirm-pricing.png" alt-text="Screenshot showing the pricing confirmation screen." lightbox="../media/provisioned/confirm-pricing.png":::
 
-If you wish to create your deployment programmatically, you can do so with the following Azure CLI command. To specify the deployment type, modify the `sku-name` to `ProvisionedManaged` or `GlobalProvisionedManaged` based on the intended deployment type. Update the `sku-capacity` with the desired number of provisioned throughput units.
+If you wish to create your deployment programmatically, you can do so with the following Azure CLI command. To specify the deployment type, modify the `sku-name` to `GlobalProvisionedManaged`, `DataZoneProvisionedManaged`, or `ProvisionedManaged` based on the intended deployment type. Update the `sku-capacity` with the desired number of provisioned throughput units.
 
 ```cli
 az cognitiveservices account deployment create \
@@ -101,13 +102,13 @@ az cognitiveservices account deployment create \
 --sku-name ProvisionedManaged
 ```
 
-REST, ARM template, Bicep, and Terraform can also be used to create deployments. See the section on automating deployments in the [Managing Quota](quota.md?tabs=rest#automate-deployment) how-to guide and replace the `sku.name` with "ProvisionedManaged" or "GlobalProvisionedManaged" rather than "Standard."
+REST, ARM template, Bicep, and Terraform can also be used to create deployments. See the section on automating deployments in the [Managing Quota](quota.md?tabs=rest#automate-deployment) how-to guide and replace the `sku.name` with `GlobalProvisionedManaged`, `DataZoneProvisionedManaged`, or `ProvisionedManaged` rather than `Standard`.
 
-## Create your provisioned or global provisioned deployment – Capacity is not available
+## Create your provisioned deployment – Capacity is not available
 
 Due to the dynamic nature of capacity availability, it is possible that the region of your selected resource might not have the service capacity to create the deployment of the specified model, version, and number of PTUs. 
 
-In this event, Azure OpenAI Studio will direct you to other regions with available quota and capacity to create a deployment of the desired model. If this happens, the deployment dialog will look like this: 
+In this event, Azure AI Foundry will direct you to other regions with available quota and capacity to create a deployment of the desired model. If this happens, the deployment dialog will look like this: 
 
 :::image type="content" source="../media/provisioned/deployment-screen-2.png" alt-text="Screenshot of the Azure OpenAI Studio deployment page for a provisioned deployment with no capacity available." lightbox="../media/provisioned/deployment-screen-2.png":::
 
@@ -166,7 +167,8 @@ The inferencing code for provisioned deployments is the same a standard deployme
 
 ## Understanding expected throughput
 The amount of throughput that you can achieve on the endpoint is a factor of the number of PTUs deployed, input size, output size, and call rate. The number of concurrent calls and total tokens processed can vary based on these values. Our recommended way for determining the throughput for your deployment is as follows:
-1.	Use the Capacity calculator for a sizing estimate. You can find the capacity calculator in the Azure OpenAI Studio under the quotas page and Provisioned tab.  
+1. Use the Capacity calculator for a sizing estimate. You can find the capacity calculator in Azure AI Foundry under the quotas page and Provisioned tab.  
+
 2.	Benchmark the load using real traffic workload. For more information about benchmarking, see the [benchmarking](#run-a-benchmark) section.
 
 
@@ -183,7 +185,7 @@ For more information about monitoring your deployments, see the [Monitoring Azur
 
 
 ## Handling high utilization
-Provisioned deployments provide you with an allocated amount of compute capacity to run a given model. The ‘Provisioned-Managed Utilization’ metric in Azure Monitor measures the utilization of the deployment in one-minute increments. Provisioned-Managed deployments are also optimized so that calls accepted are processed with a consistent per-call max latency. When the workload exceeds its allocated capacity, the service returns a 429 HTTP status code until the utilization drops down below 100%. The time before retrying is provided in the `retry-after` and `retry-after-ms` response headers that provide the time in seconds and milliseconds respectively. This approach maintains the per-call latency targets while giving the developer control over how to handle high-load situations – for example retry or divert to another experience/endpoint. 
+Provisioned deployments provide you with an allocated amount of compute capacity to run a given model. The ‘Provisioned-Managed Utilization V2’ metric in Azure Monitor measures the utilization of the deployment in one-minute increments. Provisioned-Managed deployments are also optimized so that calls accepted are processed with a consistent per-call max latency. When the workload exceeds its allocated capacity, the service returns a 429 HTTP status code until the utilization drops down below 100%. The time before retrying is provided in the `retry-after` and `retry-after-ms` response headers that provide the time in seconds and milliseconds respectively. This approach maintains the per-call latency targets while giving the developer control over how to handle high-load situations – for example retry or divert to another experience/endpoint. 
 
 ### What should  I do when I receive a 429 response?
 A 429 response indicates that the allocated PTUs are fully consumed at the time of the call. The response includes the `retry-after-ms` and `retry-after` headers that tell you the time to wait before the next call will be accepted. How you choose to handle a 429 response depends on your application requirements. Here are some considerations:
@@ -242,5 +244,5 @@ We recommend the following workflow:
     * [Python reference documentation](https://github.com/openai/openai-python?tab=readme-ov-file#retries)
     * [.NET reference documentation](/dotnet/api/overview/azure/ai.openai-readme)
     * [Java reference documentation](/java/api/com.azure.ai.openai.openaiclientbuilder?view=azure-java-preview&preserve-view=true#com-azure-ai-openai-openaiclientbuilder-retryoptions(com-azure-core-http-policy-retryoptions))
-    * [JavaScript reference documentation](/javascript/api/@azure/openai/openaiclientoptions?view=azure-node-preview&preserve-view=true#@azure-openai-openaiclientoptions-retryoptions)
+    * [JavaScript reference documentation](/azure/ai-services/openai/supported-languages?tabs=dotnet-secure%2Csecure%2Cpython-secure%2Ccommand&pivots=programming-language-javascript)
     * [GO reference documentation](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/ai/azopenai#ChatCompletionsOptions)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングデプロイメントの開始に関するガイドの更新"
}
```

### Explanation
このコードの差分は、「プロビジョニングデプロイメントの開始」に関するガイドを更新したもので、内容がより明確にされ、最新の情報が反映されています。主な変更点は次の通りです。

1. **PTUクォータの説明の明確化**: プロビジョニングスループットデプロイメントにおける「プロビジョニングスループットユニット（PTU）」のクォータについて、各プロビジョニングデプロイメントタイプが地域ごとにサブスクリプションに付与されることが追加されました。

2. **クォータの参照先変更**: クォータの確認先が「Azure OpenAI Studio」から「Azure AI Foundry」に変更され、これに伴い文中の表現も更新されています。

3. **デプロイメントタイプの選択肢の追加**: プロビジョニングデプロイメントをプログラム的に作成するためのCLIコマンドにおいて、デプロイメントタイプの選択肢が「GlobalProvisionedManaged」や「DataZoneProvisionedManaged」といった新しいオプションを追加されています。

4. **ノートの内容の整理**: Azure OpenAIリソースが複数のデプロイメントタイプを同時にサポートすることが強調され、新たに「プロビジョニングデプロイメント」のセクションが明確に分けられています。

これらの変更は、ユーザーがプロビジョニングデプロイメントを設定する際の理解を深める助けとなり、実際の手順に関する情報を最新のものに保つことを目的としています。

## articles/ai-services/openai/includes/model-matrix/datazone-provisioned-managed.md{#item-ae7f5b}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,16 @@
+---
+title: Data zone provisioned managed  model availability
+titleSuffix: Azure OpenAI Service
+description: Regional availability for data zone provisioned managed models
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 12/05/2024
+---
+
+| **Region**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-----------------|:--------------------------:|:--------------------------:|:-------------------------------:|
+| eastus2          | ✅                       | ✅                       | ✅                            |
+| spaincentral     | ✅                       | ✅                       | ✅                            |
+| westeurope       | ✅                       | ✅                       | ✅                            |
+| westus3          | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "データゾーンのプロビジョニング管理モデルの可用性に関する新規ドキュメントの追加"
}
```

### Explanation
このコードの差分は、データゾーンにおけるプロビジョニング管理モデルの可用性に関する新しいドキュメントが追加されたことを示しています。具体的には、以下の内容が含まれています。

1. **ドキュメントの基本情報**: 新しいファイルには、タイトル、タイトル接尾辞、説明、サービスマネージャー、サービス名、トピックタイプ、日付などのメタデータが含まれています。これにより、ドキュメントの内容が何についてのものであるかが明確になります。

2. **モデルの可用性テーブル**: 追加された内容には、各地域における特定のモデル（gpt-4oやgpt-4o-mini）の可用性が示されたテーブルがあります。これにより、ユーザーはどの地域で特定のモデルを利用できるのかを一目で確認することができます。

3. **地域ごとの情報**: テーブルには、「eastus2」「spaincentral」「westeurope」「westus3」などの地域が列挙され、それぞれの地域においてモデルが利用可能であるかどうか（チェックマークで示されている）が示されています。

この新たに追加されたドキュメントは、ユーザーがデータゾーンの環境でのモデル可用性を簡単に把握できるようにすることを目的としており、Azure OpenAIサービスの利用を促進するための重要な情報源となります。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -91,6 +91,8 @@ items:
       displayName: PTU, provisioned, provisioned throughput units
     - name: Azure OpenAI PTU update
       href: ./concepts/provisioned-migration.md
+    - name: Azure OpenAI PTU reservation update
+      href: ./concepts/provisioned-reservation-update.md
     - name: Legacy models
       href: ./concepts/legacy-models.md
 - name: How-to 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIのPTU予約更新に関するトピックの追加"
}
```

### Explanation
このコードの差分は、Azure OpenAIに関する目次（toc.yml）ファイルに新しいトピックが追加されたことを示しています。具体的な変更点は次の通りです。

1. **新トピックの追加**: 「Azure OpenAI PTU予約更新」という新しい項目が追加されており、それに関連するドキュメントへのリンクが含まれています。このリンクは「./concepts/provisioned-reservation-update.md」であり、ユーザーがPTU予約の更新に関する情報を得られるようになっています。

2. **既存のトピックとの整理**: 新しいトピックが追加されたことで、既存のトピック「Azure OpenAI PTU update」と良い形で区分され、ユーザーはさまざまなPTU関連の情報に簡単にアクセスできるようになります。

この更新は、Azure OpenAIに関心のあるユーザーがPTUの予約に関する重要な情報を効率よく探し出す手助けをします。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -19,6 +19,14 @@ recommendations: false
 
 This article provides a summary of the latest releases and major documentation updates for Azure OpenAI.
 
+## December 2024
+
+### NEW data zone provisioned deployment type
+
+Data zone provisioned deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. Data zone provisioned deployments provide reserved model processing capacity for high and predictable throughput using Azure infrastructure within Microsoft specified data zones. Data zone provisioned deployments are supported on `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, and `gpt-4o-mini-2024-07-18` models.
+
+For more information, see the [deployment types guide](https://aka.ms/aoai/docs/deployment-types).
+
 ## November 2024
 
 ### Vision Fine-tuning GA
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "2024年12月の新しいデータゾーンプロビジョニングデプロイメントタイプの追加"
}
```

### Explanation
このコードの差分は、Azure OpenAIに関する「What's New」記事に新しい情報が追加されたことを示しています。具体的には、以下の内容が新たに含まれています。

1. **新セクションの追加**: 記事に「2024年12月」セクションが新たに追加され、データゾーンプロビジョニングデプロイメントタイプの概要が説明されています。このタイプは、Azure OpenAIリソースの中での動的なトラフィックルーティングを可能にし、最も利用可能なデータセンターにリクエストを送る仕組みを持っています。

2. **モデルのサポート情報**: データゾーンプロビジョニングデプロイメントタイプは、特定のAzure OpenAIモデル（`gpt-4o-2024-08-06`、`gpt-4o-2024-05-13`、`gpt-4o-mini-2024-07-18`）をサポートしていることが明示されています。これにより、ユーザーはどのモデルが新機能に対応しているのかを理解できます。

3. **さらなる情報へのリンク**: 記事内には「デプロイメントタイプガイド」へのリンクが追加されており、読者がさらに詳細な情報を確認できるようになっています。

この更新は、Azure OpenAIの最新の機能についてユーザーに情報を提供し、デプロイメント方法の選択肢を広げることに寄与します。


