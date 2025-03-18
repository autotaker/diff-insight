---
date: '2025-03-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6e505af...MicrosoftDocs:b32e527
summary: |-
  Azure OpenAIサービスに関連するドキュメントの重要な更新が行われました。主にファインチューニングモデルやプロビジョニングに関する情報が中心となっています。新たに商業モデルや自己サービスのクォータリクエスト機能が導入され、Azure予約を活用した割引オプションも追加されました。一方で、プロビジョニングされた予約に関するドキュメントが削除され、ユーザーは新しいデプロイメントタイプの情報を他の資源から収集する必要があります。

  さらに、ファインチューニングモデル名の変更や監視ダッシュボードの説明が明確化され、目次が整理されることで情報へのアクセスが向上しました。これらの変更は、Azure OpenAIサービスの利用をより効率的で便利にし、ユーザー体験の向上を図ることを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6e505af...MicrosoftDocs:b32e527){target="_blank"}

<format>
# Highlights
この差分全体を通じて、Azure OpenAIサービス関連のドキュメントで複数の更新が行われており、主にファインチューニングモデルやプロビジョニング関連の情報に焦点が当てられています。特に、モデル名の修正やドキュメントの構成の整理と明確化が見られます。

## New features
- 新しい商業モデルと自己サービスのクォータリクエスト機能が導入されました。
- Azure予約を使用した割引オプションが追加され、グローバルプロビジョニングに関する情報が拡充されました。

## Breaking changes
- Azure OpenAIサービスのプロビジョニングされた予約に関するドキュメントが削除されたことにより、ユーザーは新しいデプロイメントタイプの情報を他のリソースから得る必要があります。

## Other updates
- ファインチューニングされたモデル名の変更。
- 監視ダッシュボードの説明が更新され、アクセス方法がより明確になりました。
- 目次でのプロビジョニングスループットユニットに関する整理が行われました。

# Insights
このドキュメントの更新は、Azure OpenAIサービスを利用するユーザーにとって非常に重要な修正と情報の追加を提供しています。プロビジョニング関連の大幅な変更は、より柔軟で効率的なリソース管理を可能にし、ユーザー体験を向上させることを目的としています。特に、新しい商業モデルや割引オプションの提供により、顧客はコスト削減の可能性を享受することができるようになります。

また、ファインチューニングモデルに関する一連の更新は、最新のモデルと技術を利用した高いパフォーマンスのAIモデルの利用を促進します。モデル名の修正により、ドキュメントと実際の操作との一貫性が保たれ、ユーザーはよりシームレスに最新の技術環境を構築できるようになります。

加えて、目次の再構築によって、必要な情報へのアクセスが容易となり、また監視に関するセクションの明確化は、運用の効率化に寄与します。これらの変更は、全体としてAzure OpenAIサービスの利用がより親しみやすく、導入しやすいものとなることを狙っています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [provisioned-migration.md](#item-68e143) | minor update | プロビジョニングされた移行の更新 | modified | 47 | 9 | 56 | 
| [provisioned-reservation-update.md](#item-53236b) | breaking change | プロビジョニングされた予約更新の削除 | removed | 0 | 71 | 71 | 
| [fine-tuning-deploy.md](#item-286d57) | minor update | ファインチューニングデプロイメントのモデル名の更新 | modified | 4 | 4 | 8 | 
| [monitor-openai.md](#item-fcba4d) | minor update | Azure OpenAIリソースの監視ダッシュボードの説明の更新 | modified | 6 | 1 | 7 | 
| [fine-tune-models.md](#item-2aadea) | bug fix | ファインチューニングモデルに関する情報の更新 | modified | 0 | 4 | 4 | 
| [fine-tuning-openai-in-ai-studio.md](#item-723c8d) | minor update | ファインチューニングのモデル情報の更新 | modified | 2 | 6 | 8 | 
| [fine-tuning-python.md](#item-976f58) | minor update | Python SDKにおけるファインチューニングモデルの更新 | modified | 8 | 12 | 20 | 
| [fine-tuning-rest.md](#item-9add3e) | minor update | REST APIによるファインチューニングに関する更新 | modified | 6 | 10 | 16 | 
| [fine-tuning-studio.md](#item-439f1e) | minor update | ファインチューニングスタジオのドキュメント更新 | modified | 2 | 6 | 8 | 
| [toc.yml](#item-c945af) | minor update | 目次の更新: プロビジョニングスループットユニットに関する整理 | modified | 12 | 12 | 24 | 


# Modified Contents
## articles/ai-services/openai/concepts/provisioned-migration.md{#item-68e143}

<details>
<summary>Diff</summary>
````diff
@@ -23,7 +23,7 @@ This article is intended for existing users of the provisioned throughput offeri
 
 
 > [!IMPORTANT]
-> The changes in this article don't apply to the older *"Provisioned Classic (PTU-C)"* offering. They only affect the Provisioned (also known as the Provisioned Managed) offering.
+> The changes in this article describe changes made to provisioned managed offering in August and December 2024. These changes don't apply to the older *"Provisioned Classic (PTU-C)"* offering. They only affect the Provisioned (also known as the Provisioned Managed) offering.
 
 ### Usability improvements
 
@@ -33,6 +33,7 @@ This article is intended for existing users of the provisioned throughput offeri
 |Self-service quota requests | Request quota increases without engaging the sales team – many can be autoapproved. |
 |Default provisioned-managed quota in many regions | Get started quickly without having to first request quota. |
 |Transparent information on real-time capacity availability + New deployment flow | Reduced negotiation around availability accelerates time-to-market. |
+| Data zone provisioned deployments | Allows you to leverage Azure's global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. For more information, see the [deployment types](../how-to/deployment-types.md#data-zone-provisioned) article. |
 
 ### New hourly/reservation commercial model
 
@@ -41,8 +42,9 @@ This article is intended for existing users of the provisioned throughput offeri
 |Non-binding, Hourly option | Hourly payment option without any binding enables short-term deployment scenarios. Ideal for testing new models and assessing benefits of Provisioned Throughput. |
 |Term discounts via Azure Reservations | Azure reservations provide substantial discounts over the hourly rate for one month and one year terms, and provide flexible scopes that minimize administration and associated with today’s resource-bound commitments.|
 | Default provisioned-managed quota in many regions | Get started quickly in new regions without having to first request quota. |
-| Flexible choice of payment model for existing provisioned customers | Customers with commitments can stay on the commitment model till the end of life of the currently supported models, and can choose to migrate existing commitments to hourly/reservations via managed process. We recommend migrating to hourly/ reservations to take advantage of term discounts and to work with the latest models. |
+| Flexible choice of payment model for existing provisioned customers | Customers with commitments can stay on the commitment model until the end of life of the currently supported models, and can choose to migrate existing commitments to hourly/reservations via managed process. We recommend migrating to hourly/ reservations to take advantage of term discounts and to work with the latest models. |
 | Supports latest model generations | The latest models are available only on hourly/ reservations in provisioned offering. |
+| Differentiated pricing | Greater flexibility and control of pricing and performance. In December 2024, we introduced  differentiated hourly pricing across [global provisioned](../how-to/deployment-types.md#global-provisioned), [data zone provisioned](../how-to/deployment-types.md#data-zone-provisioned), and [provisioned](../how-to/deployment-types.md#provisioned) deployment types with the option to purchase [Azure Reservations](#new-azure-reservations-for-global-and-data-zone-provisioned-deployments) to support additional discounts. For more information on the hourly price for each provisioned deployment type, see the [Pricing details](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) page. |
 
 ## Usability improvement details
 
@@ -86,7 +88,20 @@ See the following links for more information. The guidance for reservations and
 > [!NOTE]
 > The following description of payment models doesn't apply to the older "Provisioned Classic (PTU-C)" offering. They only affect the Provisioned (also known as Provisioned Managed) offering. Provisioned Classic continues to be governed by the unchanged monthly commitment payment model.
 
-Microsoft has introduced a new "Hourly/reservation" payment model for provisioned deployments. This is in addition to the current **Commitment** payment model, which will continue to be supported until end of life of the currently supported limited model list. Refer to the [supported models on **Commitment payment model**](./provisioned-migration.md#supported-models-on-commitment-payment-model) for the list of supported models on Commitment payment model.
+Microsoft has introduced a new "Hourly/reservation" payment model for provisioned deployments. This is in addition to the current **Commitment** payment model, which will continue to be supported until end of life of the currently supported limited model list. Refer to the [supported models on **Commitment payment model**](./provisioned-migration.md#supported-models-on-commitment-payment-model) for the list of supported models on Commitment payment model. You also have the option to purchase Azure Reservations to support additional discounts.
+
+### New Azure Reservations for global and data zone provisioned deployments
+
+In addition to the updates for the hourly payment model, in December 2024 new [Azure Reservations](https://aka.ms/oai/docs/ptum-reservations) were introduced specifically for global and data zone provisioned deployment types. With these new Azure Reservations, every provisioned deployment type will have a separate Azure Reservation that can be purchased to support additional discounts. The mapping between each provisioned deployment type and the associated Azure Reservation are as follows:
+
+| Provisioned deployment type | Sku name in code  | Azure Reservation product name |
+|---|---|---|
+| Global provisioned | `GlobalProvisionedManaged`  | Provisioned Managed Global  |
+| Data zone provisioned | `DataZoneProvisionedManaged`  | Provisioned Managed Data Zone  |
+| Provisioned | `ProvisionedManaged`  | Provisioned Managed Regional |
+
+> [!IMPORTANT]
+> Azure Reservations for Azure OpenAI provisioned offers are not interchangeable across deployment types. The Azure Reservation purchased must match the provisioned deployment type. If the Azure Reservation purchased does not match the provisioned deployment type, the provisioned deployment will default to the hourly payment model until a matching Azure Reservation product is purchased. For more information, see the [Azure Reservations for Azure OpenAI Service provisioned guidance](https://aka.ms/oai/docs/ptum-reservations).
 
 ### Commitment payment model
 
@@ -172,7 +187,7 @@ Customers using Azure OpenAI Provisioned offer prior to August 2024 can use eith
 
 **Resource has an active Commitment** 
 
-* The commitment discounts all deployments on the resource up to the number of PTUs on the commitment. Any excess PTUs is billed hourly unless the excess PTUs aren't in the scope of an active reservation. If the excess PTUs exist in the scope of an active reservation, will be discounted as a group up to the number of PTUs on the reservation and any excess spill still leftover will be billed hourly. 
+* The commitment discounts all deployments on the resource up to the number of PTUs on the commitment. Any excess PTUs is billed hourly unless the excess PTUs aren't in the scope of an active reservation. If the excess PTUs exist in the scope of an active reservation, will be discounted as a group, up to the number of PTUs on the reservation and any excess spill still leftover will be billed hourly. 
 
 **Resource does not have an active commitment** 
 
@@ -244,6 +259,29 @@ Customers must reach out to their account teams to schedule a managed migration.
 - All commitments in a subscription/region must be migrated at the same time.
 - Needing to coordinate a time for migration with the Microsoft team.
 
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
+- Once your new deployment has succeeded, you can resume inference traffic on the new global or data zone deployment.
+
+## How do I migrate my existing Azure Reservation to the new Azure Reservation products?
+Azure Reservations for Azure OpenAI Service provisioned offers are specific to the provisioned deployment type. If the Azure Reservation purchased does not match the provisioned deployment type, the deployment will default to the hourly payment model. If you choose to migrate to global or data zone provisioned deployments, you might need to purchase a new Azure Reservation for these deployments to support additional discounts. For more information on how to purchase a new Azure Reservation or make changes to an existing Azure Reservation, see the [Azure Reservations for Azure OpenAI Service Provisioned guidance](https://aka.ms/aoai/reservation-transition).
+
 ## Managing Provisioned Throughput Commitments
 
 Provisioned throughput commitments are created and managed by selecting **Management center** in the [Azure AI Foundry portal](https://ai.azure.com/)'s navigation menu > **Quota** > **Manage Commitments**. 
@@ -315,20 +353,20 @@ Commitment renewal settings can be changed at any time before the expiration dat
 
 ## Monitor commitments and prevent unexpected billings
 
-The manage commitments pane provides a subscription wide overview of all resources with commitments and PTU usage within a given Azure Subscription. Of particular importance are:
+The **Manage Commitments** section provides a subscription wide overview of all resources with commitments and PTU usage within a given Azure Subscription. Of particular importance are:
 
 - **PTUs Committed, Deployed and Usage** – These figures provide the sizes of your commitments, and how much is in use by deployments. Maximize your investment by using all of your committed PTUs.
 - **Expiration policy and date** - The expiration date and policy tell you when a commitment will expire and what will happen when it does. A commitment set to autorenew will generate a billing event on the renewal date. For commitments that are expiring, be sure you delete deployments from these resources prior to the expiration date to prevent hourly overage billingThe current renewal settings for a commitment. 
 - **Notifications** - Alerts regarding important conditions like unused commitments, and configurations that might result in billing overages. Billing overages can be caused by situations such as when a commitment has expired and deployments are still present, but have shifted to hourly billing.
 
 > [!IMPORTANT]
-> If you set a commitment to *auto-renew* the renewal date will be the same date next month. If the date doesn't exist then the renewal date will be end of month.
+> If you set a commitment to *auto-renew* the renewal date will be the same date next month. If the date doesn't exist, then the renewal date will be end of month.
 > Examples -  
-> *Scenario 1:* If you purchase a commitment on February 21st, and set the commitment on *auto-renew*, the next renewal date for the commitment will be March 21st.
+> *Scenario 1:* If you purchase a commitment on February 21, and set the commitment on *auto-renew*, the next renewal date for the commitment will be March 21.
 >
-> *Scenario 2:* If you purchase the commitment on May 31st, and set the commitment on *auto-renew*, the next renewal date for the commitment will be 30th June (end of month) as there's no 31st in the month of June.
+> *Scenario 2:* If you purchase the commitment on May 31, and set the commitment on *auto-renew*, the next renewal date for the commitment will be June 30 (end of month) as there's no 31st in the month of June.
 >
-> *Scenario 3:* If you purchase the commitment on January 31st, and set the commitment on *auto-renew*, the next renewal date for the commitment will be February 28th (end of month) as there's no 31st or 30th or 29th (in non-leap years) and the renewal date would be February 29th (in a leap-year) in the month of February. 
+> *Scenario 3:* If you purchase the commitment on January 31, and set the commitment on *auto-renew*, the next renewal date for the commitment will be February 28 (end of month) as there's no 31st or 30th or 29th (in non-leap years) and the renewal date would be February 29 (in a leap-year) in the month of February. 
 
 ## Common Commitment Management Scenarios
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされた移行の更新"
}
```

### Explanation
このコード差分は、AzureのOpenAIサービスの「プロビジョニングされた移行」に関するドキュメントに対する修正を示しています。主な変更点として、2024年8月および12月に実施されたプロビジョニングされた管理オファリングの変更点を明確にし、従来の「プロビジョニングクラシック（PTU-C）」オファリングには影響しないことを強調しています。また、文書が新しい時間単位または予約制の商業モデルを導入していることも明らかにしています。

改善点には、自己サービスのクォータリクエスト機能や、デフォルトのプロビジョニング管理クォータ、リアルタイムでのキャパシティの透明性向上、新しい展開フローなどが含まれています。これらは顧客が迅速に始めたり、新しいモデルのテストを行ったりするのに役立ちます。

さらに、グローバルプロビジョニングおよびデータゾーンプロビジョニングのための新しいAzure予約が導入され、顧客が追加の割引を受けるための選択肢が広がったことも記載されています。移行手続きについての詳細な手順も追加されており、ゼロダウンタイムでの移行方法及びダウンタイムを伴う移行方法の紹介が進められています。

このように、これらの変更はユーザーの利便性を高め、より柔軟な料金モデルを提供するために行われています。

## articles/ai-services/openai/concepts/provisioned-reservation-update.md{#item-53236b}

<details>
<summary>Diff</summary>
````diff
@@ -1,71 +0,0 @@
----
-title: 'Azure OpenAI Provisioned December 2024 Update'
-titleSuffix: Azure OpenAI
-description: Learn about new Provisioned skus and commercial changes for Provisioned offers
-manager: chrhoder
-ms.service: azure-ai-openai
-ms.custom:
-ms.topic: how-to
-ms.date: 11/25/2024
-author: sydneemayers
-ms.author: sydneemayers
-recommendations: false
----
-# Azure OpenAI provisioned December 2024 update 
-
-In early December, 2024, Microsoft launched several changes to the provisioned offering. These changes include:
-- A new deployment type, **data zone provisioned**.
-- Updated hourly pricing for global and data zone provisioned deployment types
-- New Azure Reservations for global and data zone provisioned deployment types
-
-This article is intended for existing users of the provisioned throughput offering. New customers should refer to the [Azure OpenAI provisioned onboarding guide](../how-to/provisioned-throughput-onboarding.md).
-
-## What's changing?
-
-The changes below apply to the global provisioned, data zone provisioned, and provisioned deployment types.
-
-> [!IMPORTANT]
-> The changes in this article do not apply to the older *"Provisioned Classic (PTU-C)"* offering. They only affect the Provisioned (also known as the Provisioned Managed) offering.
-
-### Data zone provisioned
-Data zone provisioned deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. Data zone provisioned deployments provide reserved model processing capacity for high and predictable throughput using Azure global infrastructure within the Microsoft defined data zone. Data zone deployments are supported for gpt-4o and gpt-4o-mini model families. 
-
-For more information, see the [deployment types guide](https://aka.ms/aoai/docs/deployment-types).
-
-### New hourly pricing for global and data zone provisioned deployments
-In August 2024, Microsoft announced that Provisioned deployments would move to a new [hourly payment model](./provisioned-migration.md) with the option to purchase Azure Reservations to support additional discounts. In December's provisioned update, we will be introducing differentiated hourly pricing across global provisioned, data zone provisioned, and provisioned deployment types. For more information on the hourly price for each provisioned deployment type, see the [Pricing details page](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). 
-
-### New Azure Reservations for global and data zone provisioned deployments
-In addition to the updates for the hourly payment model, new Azure Reservations will be introduced specifically for global and data zone provisioned deployment types. With these new Azure Reservations, every provisioned deployment type will have a separate Azure Reservation that can be purchased to support additional discounts. The mapping between each provisioned deployment type and the associated Azure Reservation are as follows:
-
-| Provisioned deployment type | Sku name in code  | Azure Reservation product name |
-|---|---|---|
-| Global provisioned | `GlobalProvisionedManaged`  | Provisioned Managed Global  |
-| Data zone provisioned | `DataZoneProvisionedManaged`  | Provisioned Managed Data Zone  |
-| Provisioned | `ProvisionedManaged`  | Provisioned Managed Regional |
-
-> [!IMPORTANT]
-> Azure Reservations for Azure OpenAI provisioned offers are not interchangeable across deployment types. The Azure Reservation purchased must match the provisioned deployment type. If the Azure Reservation purchased does not match the provisioned deployment type, the provisioned deployment will default to the hourly payment model until a matching Azure Reservation product is purchased. For more information, see the [Azure Reservations for Azure OpenAI Service provisioned guidance](https://aka.ms/oai/docs/ptum-reservations).
-
-## Migrating existing deployments to global or data zone provisioned
-Existing customers of provisioned deployments can choose to migrate to global or data zone provisioned deployments to benefit from the lower deployment minimums, granular scale increments, or differentiated pricing available for these deployment types. To learn more about how global and data zone provisioned deployments handle data processing across Azure geographies, see the Azure OpenAI deployment [data processing documentation](https://aka.ms/aoai/docs/data-processing-locations).
-
-Two approaches are available for customers to migrate from provisioned deployments to global or data zone provisioned deployments. 
-
-### Zero downtime migration 
-The zero downtime migration approach allows customers to migrate their existing provisioned deployments to global or data zone provisioned deployments without interrupting the existing inference traffic on their deployment. This migration approach minimizes workload interruptions, but does require a customer to have multiple coexisting deployments while shifting traffic over. The process to migrate a provisioned deployment using the zero downtime migration approach is as follows:
-- Create a new deployment using the global or data zone provisioned deployment types in the target Azure OpenAI resource.
-- Transition traffic from the existing regional provisioned deployment type to the newly created global or data zone provisioned deployment until all traffic is offloaded from the existing regional provisioned deployment.
-- Once traffic is migrated over to the new deployment, validate that there are no inference requests being processed on the previous provisioned deployment by ensuring the Azure OpenAI Requests metric does not show any API calls made within 5-10 minutes of the inference traffic being migrated over to the new deployment. For more information on this metric, [see the Monitor Azure OpenAI documentation](https://aka.ms/aoai/docs/monitor-azure-openai).
-- Once you confirm that no inference calls have been made, delete the regional provisioned deployment.
-
-### Migration with downtime 
-The migration with downtime approach involves migrating existing provisioned deployments to global or data zone provisioned deployments while stopping any existing inference traffic on the original provisioned deployment. This migration approach does not require coexistence of multiple deployments to support but does require workload interruption to complete. The process to migrate a provisioned deployment using the migration with downtime approach is as follows:
-- Validate that there are no inference requests being processed on the previous provisioned deployment by ensuring the Azure OpenAI Requests metric does not show any API calls made within the last 5-10 minutes. For more information on this metric, [see the Monitor Azure OpenAI documentation](https://aka.ms/aoai/docs/monitor-azure-openai).
-- Once you confirm that no inference calls have been made, delete the regional provisioned deployment.
-- Create a new deployment using the global or data zone deployment types in the target Azure OpenAI resource.
-- Once your new deployment has succeeded, you may resume inference traffic on the new global or data zone deployment.
-
-## How do I migrate my existing Azure Reservation to the new Azure Reservation products?
-Azure Reservations for Azure OpenAI Service provisioned offers are specific to the provisioned deployment type. If the Azure Reservation purchased does not match the provisioned deployment type, the deployment will default to the hourly payment model. If you choose to migrate to global or data zone provisioned deployments, you might need to purchase a new Azure Reservation for these deployments to support additional discounts. For more information on how to purchase a new Azure Reservation or make changes to an existing Azure Reservation, see the [Azure Reservations for Azure OpenAI Service Provisioned guidance](https://aka.ms/aoai/reservation-transition).
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロビジョニングされた予約更新の削除"
}
```

### Explanation
このコード差分は、Azure OpenAIサービスにおける「プロビジョニングされた予約更新」に関連するドキュメントが削除されたことを示しています。削除された内容には、2024年12月に実施されたプロビジョニングの変更に関する重要な情報が含まれていました。具体的には、新しいデプロイメントタイプ「データゾーンプロビジョニング」や、グローバルおよびデータゾーンプロビジョニングのための更新された時間料金モデル、新しいAzure予約の導入についての情報が提供されていました。

この文書は、従来の「プロビジョニングクラシック（PTU-C）」オファリングには影響しないことを明記し、既存の顧客が新しいデプロイメントタイプへの移行を行う際の手順についても詳しく解説されていました。ゼロダウンタイムでの移行やダウンタイムを伴う移行の方法、また既存のAzure予約の移行方法についても触れられていました。

この削除は、関連情報の統廃合やドキュメントの整理を意図している可能性がありますが、特にユーザーが重要な移行手順や新しいモデルに関する情報を見つけることが困難になる可能性があるため、注意が必要です。

## articles/ai-services/openai/how-to/fine-tuning-deploy.md{#item-286d57}

<details>
<summary>Diff</summary>
````diff
@@ -56,7 +56,7 @@ deploy_data = {
     "properties": {
         "model": {
             "format": "OpenAI",
-            "name": <"fine_tuned_model">, #retrieve this value from the previous call, it will look like gpt-35-turbo-0613.ft-b044a9d3cf9c4228b5d393567f693b83
+            "name": <"fine_tuned_model">, #retrieve this value from the previous call, it will look like gpt-35-turbo-0125.ft-b044a9d3cf9c4228b5d393567f693b83
             "version": "1"
         }
     }
@@ -82,7 +82,7 @@ print(r.json())
 | resource_group | The resource group name for your Azure OpenAI resource. |
 | resource_name | The Azure OpenAI resource name. |
 | model_deployment_name | The custom name for your new fine-tuned model deployment. This is the name that will be referenced in your code when making chat completion calls. |
-| fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It will look like `gpt-35-turbo-0613.ft-b044a9d3cf9c4228b5d393567f693b83`. You will need to add that value to the deploy_data json. Alternatively you can also deploy a checkpoint, by passing the checkpoint ID which will appear in the format `ftchkpt-e559c011ecc04fc68eaa339d8227d02d` |
+| fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It will look like `gpt-35-turbo-0125.ft-b044a9d3cf9c4228b5d393567f693b83`. You will need to add that value to the deploy_data json. Alternatively you can also deploy a checkpoint, by passing the checkpoint ID which will appear in the format `ftchkpt-e559c011ecc04fc68eaa339d8227d02d` |
 
 ### Cross region deployment
 
@@ -122,7 +122,7 @@ deploy_data = {
     "properties": {
         "model": {
             "format": "OpenAI",
-            "name": <"FINE_TUNED_MODEL_NAME">, # This value will look like gpt-35-turbo-0613.ft-0ab3f80e4f2242929258fff45b56a9ce 
+            "name": <"FINE_TUNED_MODEL_NAME">, # This value will look like gpt-35-turbo-0125.ft-0ab3f80e4f2242929258fff45b56a9ce 
             "version": "1",
             "source": source
         }
@@ -220,7 +220,7 @@ curl -X POST "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resource
 | resource_group | The resource group name for your Azure OpenAI resource. |
 | resource_name | The Azure OpenAI resource name. |
 | model_deployment_name | The custom name for your new fine-tuned model deployment. This is the name that will be referenced in your code when making chat completion calls. |
-| fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It will look like `gpt-35-turbo-0613.ft-b044a9d3cf9c4228b5d393567f693b83`. You'll need to add that value to the deploy_data json. Alternatively you can also deploy a checkpoint, by passing the checkpoint ID which will appear in the format `ftchkpt-e559c011ecc04fc68eaa339d8227d02d` |
+| fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It will look like `gpt-35-turbo-0125.ft-b044a9d3cf9c4228b5d393567f693b83`. You'll need to add that value to the deploy_data json. Alternatively you can also deploy a checkpoint, by passing the checkpoint ID which will appear in the format `ftchkpt-e559c011ecc04fc68eaa339d8227d02d` |
 
 
 ### Cross region deployment
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングデプロイメントのモデル名の更新"
}
```

### Explanation
このコード差分は、Azure OpenAIサービスのファインチューニングデプロイメントに関連するドキュメントに対する変更を示しています。主な変更点として、ファインチューニングされたモデルの名前に関する具体的な例が更新されました。

具体的には、モデル名の例として提供される文字列が `gpt-35-turbo-0613.ft-*` から `gpt-35-turbo-0125.ft-*` に変更されています。この変更は、ユーザーがファインチューニングジョブの結果から正しいモデル名を取得する際に、新しい情報を反映するために重要です。これにより、ユーザーは最新のモデル名を使用してデプロイメントを正確に行うことができるようになります。

加えて、他の部分でも同様のモデル名の更新が行われており、ファインチューニングプロセスにおける一貫性と明確さが保たれています。この変更は主に、現在のファインチューニングされたモデルに基づくデプロイメント手順の理解を助け、混乱を防ぐことを目的としています。

## articles/ai-services/openai/how-to/monitor-openai.md{#item-fcba4d}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,12 @@ ms.service: azure-ai-openai
 
 ## Dashboards
 
-Azure OpenAI provides out-of-box dashboards for each of your Azure OpenAI resources. To access the monitoring dashboards sign-in to [https://portal.azure.com](https://portal.azure.com) and select the overview pane for one of your Azure OpenAI resources.
+Azure OpenAI provides out-of-box dashboards for each of your Azure OpenAI resources. There are two key dashboards to monitor your resource: 
+
+- The metrics dashboard in the AI Foundry Azure OpenAI resource view 
+- The dashboard in the overview pane within the Azure portal 
+
+To access the monitoring dashboards, sign in to the [Azure portal](https://portal.azure.com) and then select the overview pane for one of your Azure OpenAI resources. To see the AI Foundry metrics dashboard from the Azure portal, select the overview pane and **Go to Azure AI Foundry portal**. Under tools, select the metrics dashboard.   
 
 :::image type="content" source="../media/monitoring/dashboard.png" alt-text="Screenshot that shows out-of-box dashboards for an Azure OpenAI resource in the Azure portal." lightbox="../media/monitoring/dashboard.png" border="false":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIリソースの監視ダッシュボードの説明の更新"
}
```

### Explanation
このコード差分は、Azure OpenAIリソースの監視ダッシュボードに関するドキュメントの内容を更新したものです。変更点としては、リソースを監視するためのダッシュボードに関する情報が具体化され、2つの主要なダッシュボードが明示的に挙げられました。

新たに追加された内容では、Azure OpenAIリソースを監視するためのダッシュボードとして、「AI Foundryのメトリクスダッシュボード」と「Azureポータル内の概要ペイン」が明記されています。これにより、ユーザーはどのダッシュボードでどの情報を確認できるかをより簡単に理解できるようになります。

また、監視ダッシュボードにアクセスするための手順も再確認されており、Azureポータルにサインインし、特定のリソースの概要ペインを選択することで、ダッシュボードへアクセスする方法が詳述されています。この変更は、ユーザーが簡単に監視体験を向上させるための手助けをすることを目的としており、利用しやすさを向上させています。

## articles/ai-services/openai/includes/fine-tune-models.md{#item-2aadea}

<details>
<summary>Diff</summary>
````diff
@@ -17,11 +17,7 @@ manager: nitinme
 
 |  Model ID  | Fine-tuning regions | Max request (tokens) | Training Data (up to) |
 |  --- | --- | :---: | :---: |
-| `gpt-35-turbo` (0613) | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | 4,096 | Sep 2021 |
 | `gpt-35-turbo` (1106) | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | Input: 16,385<br> Output: 4,096 |  Sep 2021|
 | `gpt-35-turbo` (0125)  | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | 16,385 | Sep 2021 |
-| `gpt-4` (0613) <sup>**1**</sup> | North Central US <br> Sweden Central | 8192 | Sep 2021 |
 | `gpt-4o-mini` (2024-07-18) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 64,536 | Oct 2023 |
 | `gpt-4o` (2024-08-06) | East US2 <br> North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 64,536 | Oct 2023 | 
-
-**<sup>1</sup>** GPT-4 is currently in public preview.
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "ファインチューニングモデルに関する情報の更新"
}
```

### Explanation
このコード差分は、ファインチューニングモデルに関連する情報が記載されたドキュメントの更新です。具体的には、以前のモデルIDに関連する行が削除され、その内容が改訂されています。

削除された情報には、`gpt-4` モデルに関する注釈が含まれており、特に「GPT-4は現在パブリックプレビュー中である」という記述が行間から取り除かれました。この変更により、最新の状況により正確に合致した情報提供を行うことを目的としています。

また、テーブルには異なるファインチューニングモデルのID、リージョン、最大リクエストトークン数、トレーニングデータの日付が保持されていますが、関連情報の簡素化と更新によって、ドキュメントの整合性と明確性が向上しています。この修正により、利用者は混乱することなく、ファインチューニングモデルに関する最新の内容を容易に把握できるようになります。

## articles/ai-services/openai/includes/fine-tuning-openai-in-ai-studio.md{#item-723c8d}

<details>
<summary>Diff</summary>
````diff
@@ -28,15 +28,11 @@ ms.custom: include, build-2024
 
 The following models support fine-tuning:
 
-- `gpt-35-turbo` (0613)
 - `gpt-35-turbo` (1106)
 - `gpt-35-turbo` (0125)
-- `gpt-4` (0613)**<sup>*</sup>**
 - `gpt-4o` (2024-08-06)
 - `gpt-4o-mini` (2024-07-18)
 
-**<sup>*</sup>** Fine-tuning for this model is currently in public preview.
-
 Or you can fine tune a previously fine-tuned model, formatted as base-model.ft-{jobid}.
 
 Consult the [models page](../concepts/models.md#fine-tuning-models) to check which regions currently support fine-tuning.
@@ -62,7 +58,7 @@ Take a moment to review the fine-tuning workflow for using Azure AI Foundry:
 
 Your training data and validation data sets consist of input and output examples for how you would like the model to perform.
 
-The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document. For `gpt-35-turbo-0613` the fine-tuning dataset must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
+The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document and must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
 
 It's generally recommended to use the instructions and prompts that you found worked best in every training example. This will help you get the best results, especially if you have fewer than a hundred examples.
 
@@ -117,7 +113,7 @@ To fine-tune an Azure OpenAI model in an existing Azure AI Foundry project, foll
 
 1. Select a base model to fine-tune. Your choice influences both the performance and the cost of your model. In this example, we are choosing the `gpt-35-turbo` model. Then select **Confirm**.
 
-1. For `gpt-35-turbo` we have different versions available for fine-tuning, so please choose which version you'd like to fine-tune. We will choose (0301). 
+1. For `gpt-35-turbo` we have different versions available for fine-tuning, so please choose which version you'd like to fine-tune. We will choose (0125). 
 
 1. We also recommend including the `suffix` parameter to make it easier to distinguish between different iterations of your fine-tuned model. `suffix` takes a string, and is set to identify the fine-tuned model. With the OpenAI Python API a string of up to 18 characters is supported that will be added to your fine-tuned model name.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングのモデル情報の更新"
}
```

### Explanation
このコード差分は、Azure AI StudioでのOpenAIモデルのファインチューニングに関するドキュメントの一部を更新したものです。変更内容には、サポートされているファインチューニングモデルのリストの一部が削除され、新しい情報が追加されています。

具体的には、`gpt-35-turbo`のいくつかのバージョンが削除され、特に`gpt-4`の関連情報も取り除かれました。しかし、最新の`gpt-4o-mini`や`gpt-4o`の情報が保持されています。また、元のファインチューニングの表記に関する説明がわかりやすくなり、ファインチューニング用のデータのフォーマットに関する条件が強調されています。

特に、トレーニングデータと検証データがどのように構成されるべきかに関する説明が簡潔にまとめられました。また、ファインチューニングの際に選択できる`gpt-35-turbo`のバージョンについても02のバージョンから`0125`に変更されています。これにより、ユーザーがファインチューニングに関する最新情報を得やすくなり、ドキュメント全体の明確さと有用性が向上しています。

## articles/ai-services/openai/includes/fine-tuning-python.md{#item-976f58}

<details>
<summary>Diff</summary>
````diff
@@ -26,15 +26,11 @@ ms.author: mbullwin
 
 The following models support fine-tuning:
 
-- `gpt-35-turbo` (0613)
 - `gpt-35-turbo` (1106)
 - `gpt-35-turbo` (0125)
-- `gpt-4` (0613)**<sup>*</sup>**
 - `gpt-4o` (2024-08-06)
 - `gpt-4o-mini` (2024-07-18)
 
-**<sup>*</sup>** Fine-tuning for this model is currently in public preview.
-
 Or you can fine tune a previously fine-tuned model, formatted as `base-model.ft-{jobid}`.
 
 
@@ -57,9 +53,9 @@ Take a moment to review the fine-tuning workflow for using the Python SDK with A
 
 Your training data and validation data sets consist of input and output examples for how you would like the model to perform.
 
-The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document. For `gpt-35-turbo-0613` the fine-tuning dataset must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
+The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document and must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
 
-If you would like a step-by-step walk-through of fine-tuning a `gpt-35-turbo-0613` please refer to the [Azure OpenAI fine-tuning tutorial](../tutorials/fine-tune.md)
+If you would like a step-by-step walk-through of fine-tuning a `gpt-4o-mini-2024-07-18` please refer to the [Azure OpenAI fine-tuning tutorial](../tutorials/fine-tune.md)
 
 ### Example file format
 
@@ -196,7 +192,7 @@ In this example we are also passing the seed parameter. The seed controls the re
 response = client.fine_tuning.jobs.create(
     training_file=training_file_id,
     validation_file=validation_file_id,
-    model="gpt-35-turbo-0613", # Enter base model name. Note that in Azure OpenAI the model name contains dashes and cannot contain dot/period characters. 
+    model="gpt-35-turbo-0125", # Enter base model name. Note that in Azure OpenAI the model name contains dashes and cannot contain dot/period characters. 
     seed = 105  # seed parameter controls reproducibility of the fine-tuning job. If no seed is specified one will be generated automatically.
 )
 
@@ -235,7 +231,7 @@ client = AzureOpenAI(
 
 client.fine_tuning.jobs.create(
   training_file="file-abc123", 
-  model="gpt-35-turbo-0613", # Enter base model name. Note that in Azure OpenAI the model name contains dashes and cannot contain dot/period characters. 
+  model="gpt-35-turbo-0125", # Enter base model name. Note that in Azure OpenAI the model name contains dashes and cannot contain dot/period characters. 
   hyperparameters={
     "n_epochs":2
   }
@@ -327,7 +323,7 @@ Unlike the previous SDK commands, deployment must be done using the control plan
 | resource_group | The resource group name for your Azure OpenAI resource. |
 | resource_name | The Azure OpenAI resource name. |
 | model_deployment_name | The custom name for your new fine-tuned model deployment. This is the name that will be referenced in your code when making chat completion calls. |
-| fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It will look like `gpt-35-turbo-0613.ft-b044a9d3cf9c4228b5d393567f693b83`. You will need to add that value to the deploy_data json. Alternatively you can also deploy a checkpoint, by passing the checkpoint ID which will appear in the format `ftchkpt-e559c011ecc04fc68eaa339d8227d02d` |
+| fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It will look like `gpt-35-turbo-0125.ft-b044a9d3cf9c4228b5d393567f693b83`. You will need to add that value to the deploy_data json. Alternatively you can also deploy a checkpoint, by passing the checkpoint ID which will appear in the format `ftchkpt-e559c011ecc04fc68eaa339d8227d02d` |
 
 ```python
 import json
@@ -348,7 +344,7 @@ deploy_data = {
     "properties": {
         "model": {
             "format": "OpenAI",
-            "name": <"fine_tuned_model">, #retrieve this value from the previous call, it will look like gpt-35-turbo-0613.ft-b044a9d3cf9c4228b5d393567f693b83
+            "name": <"fine_tuned_model">, #retrieve this value from the previous call, it will look like gpt-35-turbo-0125.ft-b044a9d3cf9c4228b5d393567f693b83
             "version": "1"
         }
     }
@@ -374,7 +370,7 @@ Learn more about cross region deployment and use the deployed model [here](../ho
 
 Once you have created a fine-tuned model you might want to continue to refine the model over time through further fine-tuning. Continuous fine-tuning is the iterative process of selecting an already fine-tuned model as a base model and fine-tuning it further on new sets of training examples.
 
-To perform fine-tuning on a model that you have previously fine-tuned you would use the same process as described in [create a customized model](#create-a-customized-model) but instead of specifying the name of a generic base model you would specify your already fine-tuned model's ID. The fine-tuned model ID looks like `gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7`
+To perform fine-tuning on a model that you have previously fine-tuned you would use the same process as described in [create a customized model](#create-a-customized-model) but instead of specifying the name of a generic base model you would specify your already fine-tuned model's ID. The fine-tuned model ID looks like `gpt-35-turbo-0125.ft-5fd1918ee65d4cd38a5dcf6835066ed7`
 
 ```python
 from openai import AzureOpenAI
@@ -388,7 +384,7 @@ client = AzureOpenAI(
 response = client.fine_tuning.jobs.create(
     training_file=training_file_id,
     validation_file=validation_file_id,
-    model="gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7" # Enter base model name. Note that in Azure OpenAI the model name contains dashes and cannot contain dot/period characters. 
+    model="gpt-35-turbo-0125.ft-5fd1918ee65d4cd38a5dcf6835066ed7" # Enter base model name. Note that in Azure OpenAI the model name contains dashes and cannot contain dot/period characters. 
 )
 
 job_id = response.id
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python SDKにおけるファインチューニングモデルの更新"
}
```

### Explanation
このコード差分は、Python SDKを使用してのファインチューニングに関するドキュメントの更新を示しています。主に、ファインチューニングをサポートするモデル情報の変更と、具体的なモデル名の置き換えが行われています。

変更点としては、ファインチューニングに使用するモデルのリストからいくつかの古いモデルが削除されており、特に`gpt-35-turbo-0613`が`gpt-35-turbo-0125`へと変更されています。これにより、最新のモデルに基づくファインチューニングの手法がより正確にユーザーに提示されるようになっています。

また、トレーニングデータや検証データに関する要件も強調されています。JSON Lines形式でのデータ構成が引き続き求められ、特に会話形式が必要であることが指摘されています。さらに、ファインチューニングチュートリアルへの参照も最新のモデルに合わせて更新されました。

この修正により、ユーザーは新しいモデルを使用したファインチューニングプロセスに関する最新情報を得ることができ、SDKを用いたファインチューニングの実行が円滑になります。全体として、文書の明確性と正確性が向上し、利用者にとっての有用性が増しています。

## articles/ai-services/openai/includes/fine-tuning-rest.md{#item-9add3e}

<details>
<summary>Diff</summary>
````diff
@@ -25,15 +25,11 @@ ms.author: mbullwin
 
 The following models support fine-tuning:
 
-- `gpt-35-turbo` (0613)
 - `gpt-35-turbo` (1106)
 - `gpt-35-turbo` (0125)
-- `gpt-4` (0613)**<sup>*</sup>**
 - `gpt-4o` (2024-08-06)
 - `gpt-4o-mini` (2024-07-18)
 
-**<sup>*</sup>** Fine-tuning for this model is currently in public preview.
-
 Or you can fine tune a previously fine-tuned model, formatted as base-model.ft-{jobid}.
 
 Consult the [models page](../concepts/models.md#fine-tuning-models) to check which regions currently support fine-tuning.
@@ -57,9 +53,9 @@ Take a moment to review the fine-tuning workflow for using the REST APIS and Pyt
 
 Your training data and validation data sets consist of input and output examples for how you would like the model to perform.
 
-The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document. For `gpt-35-turbo-0613` and other related models, the fine-tuning dataset must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
+The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document and must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
 
-If you would like a step-by-step walk-through of fine-tuning a `gpt-35-turbo-0613` please refer to the [Azure OpenAI fine-tuning tutorial.](../tutorials/fine-tune.md)
+If you would like a step-by-step walk-through of fine-tuning a `gpt-4o-mini-2024-07-18` please refer to the [Azure OpenAI fine-tuning tutorial.](../tutorials/fine-tune.md)
 
 ### Example file format
 
@@ -141,7 +137,7 @@ curl -X POST $AZURE_OPENAI_ENDPOINT/openai/fine_tuning/jobs?api-version=2024-10-
   -H "Content-Type: application/json" \
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -d '{
-    "model": "gpt-35-turbo-0613", 
+    "model": "gpt-35-turbo-0125", 
     "training_file": "<TRAINING_FILE_ID>", 
     "validation_file": "<VALIDATION_FILE_ID>",
     "seed": 105
@@ -237,7 +233,7 @@ The following example shows how to use the REST API to create a model deployment
 | resource_group | The resource group name for your Azure OpenAI resource. |
 | resource_name | The Azure OpenAI resource name. |
 | model_deployment_name | The custom name for your new fine-tuned model deployment. This is the name that will be referenced in your code when making chat completion calls. |
-| fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It will look like `gpt-35-turbo-0613.ft-b044a9d3cf9c4228b5d393567f693b83`. You'll need to add that value to the deploy_data json. Alternatively you can also deploy a checkpoint, by passing the checkpoint ID which will appear in the format `ftchkpt-e559c011ecc04fc68eaa339d8227d02d` |
+| fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It will look like `gpt-35-turbo-0125.ft-b044a9d3cf9c4228b5d393567f693b83`. You'll need to add that value to the deploy_data json. Alternatively you can also deploy a checkpoint, by passing the checkpoint ID which will appear in the format `ftchkpt-e559c011ecc04fc68eaa339d8227d02d` |
 
 ```bash
 curl -X POST "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-21" \
@@ -262,14 +258,14 @@ Learn more about cross region deployment and use the deployed model [here](../ho
 
 Once you have created a fine-tuned model, you might want to continue to refine the model over time through further fine-tuning. Continuous fine-tuning is the iterative process of selecting an already fine-tuned model as a base model and fine-tuning it further on new sets of training examples.
 
-To perform fine-tuning on a model that you have previously fine-tuned, you would use the same process as described in [create a customized model](#create-a-customized-model) but instead of specifying the name of a generic base model you would specify your already fine-tuned model's ID. The fine-tuned model ID looks like `gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7`
+To perform fine-tuning on a model that you have previously fine-tuned, you would use the same process as described in [create a customized model](#create-a-customized-model) but instead of specifying the name of a generic base model you would specify your already fine-tuned model's ID. The fine-tuned model ID looks like `gpt-35-turbo-0125.ft-5fd1918ee65d4cd38a5dcf6835066ed7`
 
 ```bash
 curl -X POST $AZURE_OPENAI_ENDPOINT/openai/fine_tuning/jobs?api-version=2023-12-01-preview \
   -H "Content-Type: application/json" \
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -d '{
-    "model": "gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7", 
+    "model": "gpt-35-turbo-0125.ft-5fd1918ee65d4cd38a5dcf6835066ed7", 
     "training_file": "<TRAINING_FILE_ID>", 
     "validation_file": "<VALIDATION_FILE_ID>",
     "suffix": "<additional text used to help identify fine-tuned models>"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIによるファインチューニングに関する更新"
}
```

### Explanation
このコード差分は、REST APIを使用したファインチューニングのドキュメントを更新した内容です。主な変更点は、サポート対象のモデル情報の改訂と、具体的なファインチューニング用のモデル名の更新です。

具体的には、使用されているモデル名が`gpt-35-turbo-0613`から`gpt-35-turbo-0125`に変更され、これに伴い関連する部分も適時修正されています。ファインチューニングに必要なトレーニングデータや検証データのフォーマットについての説明も明確化され、JSON Lines（JSONL）形式での要件が強調されています。

さらに、ファインチューニングの手順に関する指示も更新されています。例えば、最新のモデルである`gpt-4o-mini-2024-07-18`に基づく具体例が示され、ユーザーが新しいモデルでのファインチューニングを行いやすくなっています。

全体として、この変更はREST APIを使用してファインチューニングを行う際のユーザー体験を向上させ、最新の情報を反映させたものとなっています。

## articles/ai-services/openai/includes/fine-tuning-studio.md{#item-439f1e}

<details>
<summary>Diff</summary>
````diff
@@ -23,15 +23,11 @@ ms.author: mbullwin
 
 The following models support fine-tuning:
 
-- `gpt-35-turbo` (0613)
 - `gpt-35-turbo` (1106)
 - `gpt-35-turbo` (0125)
-- `gpt-4` (0613)**<sup>*</sup>**
 - `gpt-4o` (2024-08-06)
 - `gpt-4o-mini` (2024-07-18)
 
-**<sup>*</sup>** Fine-tuning for this model is currently in public preview.
-
 Or you can fine tune a previously fine-tuned model, formatted as base-model.ft-{jobid}.
 
 
@@ -57,7 +53,7 @@ Take a moment to review the fine-tuning workflow for using Azure AI Foundry port
 
 Your training data and validation data sets consist of input and output examples for how you would like the model to perform.
 
-The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document. For `gpt-35-turbo` (all versions), `gpt-4`, `gpt-4o`, and `gpt-4o-mini`, the fine-tuning dataset must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
+The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document and must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
 
 It's generally recommended to use the instructions and prompts that you found worked best in every training example. This will help you get the best results, especially if you have fewer than a hundred examples.
 
@@ -235,7 +231,7 @@ After your fine-tuned model deploys, you can use it like any other deployed mode
 
 Once you have created a fine-tuned model you may wish to continue to refine the model over time through further fine-tuning. Continuous fine-tuning is the iterative process of selecting an already fine-tuned model as a base model and fine-tuning it further on new sets of training examples.
 
-To perform fine-tuning on a model that you have previously fine-tuned you would use the same process as described in [create a customized model](#use-the-create-custom-model-wizard) but instead of specifying the name of a generic base model you would specify your already fine-tuned model. A custom fine-tuned model would look like `gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7`
+To perform fine-tuning on a model that you have previously fine-tuned you would use the same process as described in [create a customized model](#use-the-create-custom-model-wizard) but instead of specifying the name of a generic base model you would specify your already fine-tuned model. A custom fine-tuned model would look like `gpt-35-turbo-0125.ft-5fd1918ee65d4cd38a5dcf6835066ed7`
 
 :::image type="content" source="../media/fine-tuning/studio-continuous.png" alt-text="Screenshot of the Create a custom model UI with a fine-tuned model highlighted." lightbox="../media/fine-tuning/studio-continuous.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングスタジオのドキュメント更新"
}
```

### Explanation
このコード差分は、ファインチューニングスタジオに関するドキュメントの更新を示しています。主な変更点は、サポートされているモデル名の修正と、ファインチューニングデータのフォーマット要件の明確化です。

具体的には、文中でのモデルのリストから古いモデル名の`gpt-35-turbo-0613`が`gpt-35-turbo-0125`に変更され、最新モデルの利用を促進しています。また、トレーニングおよび検証データのフォーマットに関する記述も改善され、JSON Lines（JSONL）形式での必要性が強調されました。これにより、ユーザーが適切なデータ形式を使用してファインチューニングを行う際の理解が深まります。

加えて、ファインチューニングのプロセスに関する指示も更新されており、カスタムファインチューニングモデルの仕様が具体的に示されています。この更新を通じて、ユーザーはより効果的に最新のモデルでの操作を行えるようになります。

全体として、ドキュメントの品質と正確性が向上し、ファインチューニングスタジオの利用者にとってより有用な情報が提供されることを目的としています。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -88,13 +88,6 @@ items:
         href: ./concepts/safety-system-message-templates.md
     - name: Model versions
       href: ./concepts/model-versions.md
-    - name: Provisioned throughput units (PTU)
-      href: ./concepts/provisioned-throughput.md
-      displayName: PTU, provisioned, provisioned throughput units
-    - name: Azure OpenAI PTU update
-      href: ./concepts/provisioned-migration.md
-    - name: Azure OpenAI PTU reservation update
-      href: ./concepts/provisioned-reservation-update.md
     - name: Legacy models
       href: ./concepts/legacy-models.md
 - name: How-to 
@@ -242,11 +235,18 @@ items:
       - name: Onboarding to Provisioned Throughput Units (PTU)
         href: ./how-to/provisioned-throughput-onboarding.md
         displayName: PTU, provisioned, provisioned throughput units
-      - name: Get started with Provisioned Deployments
-        href: ./how-to/provisioned-get-started.md
-        displayName: PTU, provisioned, provisioned throughput units
-      - name: Provisioned spillover
-        href: ./how-to/spillover-traffic-management.md
+      - name: Provisioned throughput units (PTU)
+        items:
+        - name: What is the Provisioned Managed offering (PTU)?
+          href: ./concepts/provisioned-throughput.md
+          displayName: PTU, provisioned, provisioned throughput units
+        - name: Get started with Provisioned Deployments
+          href: ./how-to/provisioned-get-started.md
+          displayName: PTU, provisioned, provisioned throughput units
+        - name: Provisioned spillover
+          href: ./how-to/spillover-traffic-management.md
+        - name: Azure OpenAI PTU updates
+          href: ./concepts/provisioned-migration.md
       - name: Plan and manage costs
         href: ./how-to/manage-costs.md
       - name: Performance & latency
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新: プロビジョニングスループットユニットに関する整理"
}
```

### Explanation
このコード差分は、目次（toc.yml）の内容を更新したもので、特にプロビジョニングスループットユニット（PTU）に関する項目を整理しています。変更の主要なポイントは、PTUに関連する情報が一つのまとまりとしてまとめられ、明確に階層化されたことです。

具体的には、プロビジョニングスループットユニットに関する項目が新たに追加され、以下のような具体的な項目が含まれています： 

- 「What is the Provisioned Managed offering (PTU)?」
- 「Get started with Provisioned Deployments」
- 「Provisioned spillover」
- 「Azure OpenAI PTU updates」

これにより、ユーザーがPTUに関する情報をより容易にナビゲートできるようになっています。また、一部の古い項目（例えば、直接的なリンクの形式で表示されていた個別のPTUのリンク）が削除され、コンテンツの整理が図られました。

全体として、この変更はドキュメントの構造をより論理的にし、視覚的に分かりやすくすることで、ユーザーが必要な情報にアクセスしやすくなることを目的としています。


