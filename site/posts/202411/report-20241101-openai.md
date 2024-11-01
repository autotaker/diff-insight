---
date: '2024-11-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b16ebe2...MicrosoftDocs:7c64df0
summary: この更新では、文書内に複数の重要な変更が加えられました。新しいファインチューニングモデルに関するガイダンスや、Azure OpenAIにおけるデプロイメントタイプが導入され、情報が強化されています。既存の文書も更新され、特にgpt-4oモデルに関する制限情報も最新化されています。構成改善により情報の可読性が向上し、ユーザーが最新の機能を効果的に活用できるようになっています。この結果、ユーザーは自身のビジネスニーズに合わせた適切なソリューションを選択しやすくなり、意思決定も迅速かつ正確に行えることが期待されます。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b16ebe2...MicrosoftDocs:7c64df0){target="_blank"}

# Highlights
文書内での更新が複数行われました。特に、新しいファインチューニングモデルのガイダンスが追加されたほか、既存の情報がユーザーの理解を助ける形で強化されています。さらに、Azure OpenAIのデプロイメントタイプやデータゾーンスタンダードに関する新機能が取り入れられています。

## New features
- 新しいファイル「fine-tune-models.md」が追加され、ファインチューニングモデルに関するガイダンスが提供されました。
- Azure OpenAIにおける「データゾーンスタンダードデプロイメントタイプ」が新たに導入され、「whats-new.md」に関連情報が記載されました。

## Breaking changes
特に大きな破壊的変更はありませんが、構成の改善により一部の既存セクションが整理されました。

## Other updates
- 「models.md」や「deployment-types.md」など既存の文書を更新し、情報の明確化と追加が行われました。
- 「quotas-limits.md」でgpt-4oモデルに関する制限情報が最新化されました。

# Insights
最近の更新では、Azure OpenAIの利用シーンに合わせた柔軟なデプロイメントオプションの提供が強化されており、特にデータゾーンスタンダードデプロイメントの紹介が注目されます。このデプロイメントタイプは、異なる地域のデータゾーンに対応し、トラフィックのルーティングを最適化することで、利用者により高いパフォーマンスと対応力を提供します。加えて、特定のAIモデルに対する制限やクォータに関する情報が追加され、ユーザーがリソースの管理を効率的に行えるようにサポートされています。

ファインチューニングモデルの新しいガイダンスが追加されたことで、ユーザーは初期設定やトレーニングに関する具体的な助けを得られるようになります。特に、地域ごとの利用制限に関する詳細は、国際的な規制やデータプライバシーに敏感なユーザーにとって重要な情報となるでしょう。また、ドキュメントの構成や順序の見直しは、情報の可読性と一貫性を高めることに寄与しており、既存のユーザーの利用体験を向上させます。

この更新により、ユーザーはAzure OpenAIの最新機能を効果的に活用し、自分のビジネス要件に適したソリューションを選択する際に必要な情報を容易に取得できるようになります。デプロイメントタイプやリソースの選択基準が明確になることで、ユーザーの意思決定がより迅速かつ精度の高いものになると期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | モデルの可用性に関する更新 | modified | 8 | 14 | 22 | 
| [deployment-types.md](#item-210814) | minor update | Azure OpenAIのデプロイメントタイプに関する更新 | modified | 31 | 17 | 48 | 
| [fine-tune-models.md](#item-2aadea) | new feature | ファインチューニングモデルガイダンスの追加 | added | 29 | 0 | 29 | 
| [fine-tuning-openai-in-ai-studio.md](#item-723c8d) | minor update | AI StudioにおけるOpenAIのファインチューニングガイドの更新 | modified | 3 | 1 | 4 | 
| [quotas-limits.md](#item-06c6f9) | minor update | gpt-4oモデルの制限とクォータの更新 | modified | 15 | 3 | 18 | 
| [whats-new.md](#item-53303b) | new feature | 新しいデータゾーンスタンダードデプロイメントタイプの追加 | modified | 5 | 0 | 5 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -405,6 +405,13 @@ For more information on Provisioned deployments, see our [Provisioned guidance](
 
 This table doesn't include fine-tuning regional availability information.  Consult the [fine-tuning section](#fine-tuning-models) for this information.
 
+### Data zone standard model availability
+
+|Model|United States Data zone regions|European Union Data zone regions|
+|---|---|---|
+| `gpt-4o` (2024-08-06, 2024-05-13)| East US 2 <br> West US 3 <br> | Spain Central <br> West Europe|
+| `gpt-4o-mini` (2024-07-18) | East US 2 <br> West US 3 <br> | Spain Central <br> West Europe|
+
 ### Standard models by endpoint
 
 # [Chat Completions](#tab/standard-chat-completions)
@@ -494,20 +501,7 @@ These models can only be used with Embedding API requests.
 
 ## Fine-tuning models
 
-`gpt-35-turbo` - fine-tuning of this model is limited to a subset of regions, and is not available in every region the base model is available.  
-
-|  Model ID  | Fine-Tuning Regions | Max Request (tokens) | Training Data (up to) |
-|  --- | --- | :---: | :---: |
-| `babbage-002` | North Central US <br> Sweden Central  <br> Switzerland West | 16,384 | Sep 2021 |
-| `davinci-002` | North Central US <br> Sweden Central  <br> Switzerland West | 16,384 | Sep 2021 |
-| `gpt-35-turbo` (0613) | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | 4,096 | Sep 2021 |
-| `gpt-35-turbo` (1106) | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | Input: 16,385<br> Output: 4,096 |  Sep 2021|
-| `gpt-35-turbo` (0125)  | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | 16,385 | Sep 2021 |
-| `gpt-4` (0613) <sup>**1**</sup> | North Central US <br> Sweden Central | 8192 | Sep 2021 |
-| `gpt-4o-mini` <sup>**1**</sup> (2024-07-18) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 64,536 | Oct 2023 |
-| `gpt-4o` <sup>**1**</sup> (2024-08-06) | East US2 <br> North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 64,536 | Oct 2023 | 
-
-**<sup>1</sup>** GPT-4 is currently in public preview.
+[!INCLUDE [Fine-tune models](../includes/fine-tune-models.md)]
 
 ## Assistants (Preview)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの可用性に関する更新"
}
```

### Explanation
このコードの変更は、AIサービスに関連する文書「models.md」に minor update を加えたものです。新しいセクション「データゾーン標準モデルの可用性」が追加され、特定のモデルがアメリカとヨーロッパのデータゾーン地域でどのように利用可能かが示されています。また、既存の「ファインチューニングモデル」に関する情報が一部削除され、代わりに関連するリンクを追加することで情報の構成が改善されています。全体で、8行が追加され、14行が削除されており、モディフィケーションの合計行数は22行です。これにより、必要な情報がより明確に提示されるようになっています。

## articles/ai-services/openai/how-to/deployment-types.md{#item-210814}

<details>
<summary>Diff</summary>
````diff
@@ -13,18 +13,24 @@ ms.author: mbullwin
 
 # Azure OpenAI deployment types
 
-Azure OpenAI provides customers with choices on the hosting structure that fits their business and usage patterns. The service offers two main types of deployment: **standard** and **provisioned**. Standard is offered with a global deployment option, routing traffic globally to provide higher throughput. Provisioned is also offered with a global deployment option, allowing customers to purchase and deploy provisioned throughput units across Azure global infrastructure. All deployments can perform the exact same inference operations, however the billing, scale and performance are substantially different. As part of your solution design, you will need to make two key decisions:
+Azure OpenAI provides customers with choices on the hosting structure that fits their business and usage patterns. The service offers two main types of deployments: **standard** and **provisioned**. For a given deployment type, customers can align their workloads with their data processing requirements by choosing an Azure geography (`Standard` or `Provisioned`), Microsoft specified data zone (`DataZone-Standard`), or Global (`Global-Standard` or `Global Provisioned-Managed`) processing options.
 
-- **Data processing needs**: global vs. regional resources  
-- **Call volume**: standard vs. provisioned
+All deployments can perform the exact same inference operations, however the billing, scale, and performance are substantially different. As part of your solution design, you will need to make two key decisions:
 
-## Global versus regional deployment types
+- **Data processing location**  
+- **Call volume**
 
-For standard and provisioned deployments, you have an option of two types of configurations within your resource – **global** or **regional**. Global standard is the recommended starting point. 
+## Azure OpenAI Deployment Data Processing Locations
 
-Global deployments leverage Azure's global infrastructure, dynamically route customer traffic to the data center with best availability for the customer’s inference requests. This means you will get the highest initial throughput limits and best model availability with Global while still providing our uptime SLA and low latency. For high volume workloads above the specified usage tiers on standard and global standard, you may experience increased latency variation. For customers that require the lower latency variance at large workload usage, we recommend purchasing provisioned throughput.
+For standard deployments, there are three deployment type options to choose from - global, data zone, and Azure geography. For provisioned deployments, there are two deployment type options to choose from - global and Azure geography. Global standard is the recommended starting point. 
 
-Our global deployments will be the first location for all new models and features. Customers with very large throughput requirements should consider our provisioned deployment offering.
+Global deployments leverage Azure's global infrastructure to dynamically route customer traffic to the data center with the best availability for the customer’s inference requests. This means you will get the highest initial throughput limits and best model availability with Global while still providing our uptime SLA and low latency. For high volume workloads above the specified usage tiers on standard and global standard, you may experience increased latency variation. For customers that require the lower latency variance at large workload usage, we recommend leveraging our provisioned deployment types.
+
+Our global deployments will be the first location for all new models and features. Depending on call volume, customers with large volume and low latency variance requirements should consider our provisioned deployment types.
+
+Data zone deployments leverage Azure's global infrastructure to dynamically route customer traffic to the data center with the best availability for the customer's inference requests within the data zone defined by Microsoft. Positioned between our Azure geography and Global deployment offerings, data zone deployments provide elevated quota limits while keeping data processing within the Microsoft specified data zone. Data stored at rest will continue to remain in the geography of the Azure OpenAI resource (e.g., for an Azure OpenAI resource created in the Sweden Central Azure region, the Azure geography is Sweden).
+
+If the Azure OpenAI resource used in your Data Zone deployment is located in the United States, the data will be processed within the United States. If the Azure OpenAI resource used in your Data Zone deployment is located in a European Union Member Nation, the data will be processed within the European Union Member Nation geographies. For all Azure OpenAI service deployment types, any data stored at rest will continue to remain in the geography of the Azure OpenAI resource. Azure data processing and compliance commitments remain applicable.
 
 ## Deployment types
 
@@ -42,16 +48,6 @@ Azure OpenAI offers three types of deployments. These provide a varied level of
 | **Sku Name in code**     |  `GlobalBatch` |   `GlobalStandard`               |`GlobalProvisionedManaged`| `Standard`   |      `ProvisionedManaged`       |
 | **Billing model**        |  Pay-per-token |Pay-per-token |Hourly billing with optional purchase of monthly or yearly reservations| Pay-per-token |Hourly billing with optional purchase of monthly or yearly reservations|
 
-## Provisioned
-
-Provisioned deployments allow you to specify the amount of throughput you require in a deployment. The service then allocates the necessary model processing capacity and ensures it's ready for you. Throughput is defined in terms of provisioned throughput units (PTU) which is a normalized way of representing the throughput for your deployment. Each model-version pair requires different amounts of PTU to deploy and provide different amounts of throughput per PTU. Learn more from our [Provisioned throughput concepts article](../concepts/provisioned-throughput.md).
-
-## Standard
-
-Standard deployments provide a pay-per-call billing model on the chosen model. Provides the fastest way to get started as you only pay for what you consume. Models available in each region as well as throughput may be limited.  
-
-Standard deployments are optimized for low to medium volume workloads with high burstiness. Customers with high consistent volume may experience greater latency variability.
-
 ## Global standard
 
 > [!IMPORTANT]
@@ -91,6 +87,24 @@ Key use cases include:
 
 * **Marketing and Personalization:** Generate personalized content and recommendations at scale.
 
+## Data zone standard
+> [!IMPORTANT]
+> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location within the Microsoft specified data zone. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
+
+Data zone standard deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. Data zone standard provides higher default quotas than our Azure geography-based deployment types. 
+
+Customers with high consistent volume may experience greater latency variability. The threshold is set per model. See the [Quotas and limits](/azure/ai-services/openai/quotas-limits#usage-tiers) page to learn more. For workloads that require low latency variance at large volume, we recommend leveraging the provisioned deployment offerings. 
+
+## Standard
+
+Standard deployments provide a pay-per-call billing model on the chosen model. Provides the fastest way to get started as you only pay for what you consume. Models available in each region as well as throughput may be limited.  
+
+Standard deployments are optimized for low to medium volume workloads with high burstiness. Customers with high consistent volume may experience greater latency variability.
+
+## Provisioned
+
+Provisioned deployments allow you to specify the amount of throughput you require in a deployment. The service then allocates the necessary model processing capacity and ensures it's ready for you. Throughput is defined in terms of provisioned throughput units (PTU) which is a normalized way of representing the throughput for your deployment. Each model-version pair requires different amounts of PTU to deploy and provide different amounts of throughput per PTU. Learn more from our [Provisioned throughput concepts article](../concepts/provisioned-throughput.md).
+
 ### How to disable access to global deployments in your subscription
 
 Azure Policy helps to enforce organizational standards and to assess compliance at-scale. Through its compliance dashboard, it provides an aggregated view to evaluate the overall state of the environment, with the ability to drill down to the per-resource, per-policy granularity. It also helps to bring your resources to compliance through bulk remediation for existing resources and automatic remediation for new resources. [Learn more about Azure Policy and specific built-in controls for AI services](/azure/ai-services/security-controls-policy).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIのデプロイメントタイプに関する更新"
}
```

### Explanation
この変更は、「deployment-types.md」ファイルの内容を更新したもので、Azure OpenAIのデプロイメントタイプに関する情報が強化されています。追加された内容には、データ処理の選択肢として「データゾーン」や「グローバル」デプロイメントなどの詳細が含まれており、それぞれのデプロイメントタイプの特性や選択基準について明確に説明されています。また、プロビジョニングデプロイメントの導入に伴うデータ処理のロケーションとその要件も詳述されています。全体で31行が追加され、17行が削除され、モディフィケーションの合計行数は48行です。この変更により、ユーザーが自分のビジネスニーズに最適なデプロイメントタイプを選択する際の理解が深まることを目的としています。

## articles/ai-services/openai/includes/fine-tune-models.md{#item-2aadea}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,29 @@
+---
+title: Fine-tuning model guidance
+titleSuffix: Azure OpenAI
+description: Describes the models that support fine-tuning and the regions where fine-tuning is available.
+author: mrbullwinkle 
+ms.author: mbullwin 
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 10/31/2024
+manager: nitinme
+---
+
+> [!NOTE]
+> `gpt-35-turbo` - Fine-tuning of this model is limited to a subset of regions, and isn't available in every region the base model is available. 
+>
+> The supported regions for fine-tuning might vary if you use Azure OpenAI models in an AI Studio project versus outside a project.
+
+|  Model ID  | Fine-tuning regions | Max request (tokens) | Training Data (up to) |
+|  --- | --- | :---: | :---: |
+| `babbage-002` | North Central US <br> Sweden Central  <br> Switzerland West | 16,384 | Sep 2021 |
+| `davinci-002` | North Central US <br> Sweden Central  <br> Switzerland West | 16,384 | Sep 2021 |
+| `gpt-35-turbo` (0613) | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | 4,096 | Sep 2021 |
+| `gpt-35-turbo` (1106) | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | Input: 16,385<br> Output: 4,096 |  Sep 2021|
+| `gpt-35-turbo` (0125)  | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | 16,385 | Sep 2021 |
+| `gpt-4` (0613) <sup>**1**</sup> | North Central US <br> Sweden Central | 8192 | Sep 2021 |
+| `gpt-4o-mini` <sup>**1**</sup> (2024-07-18) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 64,536 | Oct 2023 |
+| `gpt-4o` <sup>**1**</sup> (2024-08-06) | East US2 <br> North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 64,536 | Oct 2023 | 
+
+**<sup>1</sup>** GPT-4 is currently in public preview.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファインチューニングモデルガイダンスの追加"
}
```

### Explanation
この変更は、新しいファイル「fine-tune-models.md」を追加したもので、ファインチューニングに関するモデルのガイダンスを提供しています。このドキュメントでは、ファインチューニングが可能なモデルと、それぞれのモデルが利用できる地域について詳しく説明しています。また、モデルごとの最大リクエストトークン数やトレーニングデータの上限も表形式で整理されています。内容には、特に`gpt-35-turbo`モデルのファインチューニングが限られた地域でのみ可能であることや、AI Studioプロジェクト内外でのサポート地域の違いに関する注意書きも含まれています。全体として29行が追加され、この情報はファインチューニングの利用を希望するユーザーにとって重要なリファレンスとなるでしょう。

## articles/ai-services/openai/includes/fine-tuning-openai-in-ai-studio.md{#item-723c8d}

<details>
<summary>Diff</summary>
````diff
@@ -19,6 +19,8 @@ ms.custom: include, build-2024
 - An [Azure AI hub resource](../../../ai-studio/how-to/create-azure-ai-resource.md).
 - An [Azure AI project](../../../ai-studio/how-to/create-projects.md) in Azure AI Studio.
 - An [Azure OpenAI connection](/azure/ai-studio/how-to/connections-add?tabs=azure-openai#connection-details) to a resource in a [region where fine-tuning is supported](/azure/ai-services/openai/concepts/models#fine-tuning-models).
+    > [!NOTE]
+    > The supported regions might vary if you use Azure OpenAI models in an AI Studio project versus outside a project.
 - Fine-tuning access requires **Cognitive Services OpenAI Contributor** role on the Azure OpenAI resource.
 - If you don't already have access to view quota and deploy models in Azure AI Studio you need [more permissions](../how-to/role-based-access-control.md).
 
@@ -92,7 +94,7 @@ In addition to the JSONL format, training and validation data files must be enco
 
 ### Create your training and validation datasets
 
-The more training examples you have, the better. Fine tuning jobs will not proceed without at least 10 training examples, but such a small number are not enough to noticeably influence model responses. It is best practice to provide hundreds, if not thousands, of training examples to be successful.
+The more training examples you have, the better. Fine tuning jobs will not proceed without at least 10 training examples, but such a small number is not enough to noticeably influence model responses. It is best practice to provide hundreds, if not thousands, of training examples to be successful.
 
 In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively impact performance. If you train the model on a large amount of internal data, without first pruning the dataset for only the highest quality examples you could end up with a model that performs much worse than expected.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI StudioにおけるOpenAIのファインチューニングガイドの更新"
}
```

### Explanation
この変更は、「fine-tuning-openai-in-ai-studio.md」ファイルの内容を更新したもので、OpenAIのファインチューニングに関するAI Studio内での利用に関する情報が強化されています。具体的には、ファインチューニングのサポート地域に関する注意事項が追加され、AI Studioプロジェクト内外での地域サポートの違いについての情報が明記されました。また、ファインチューニングに必要なトレーニング例の数に関する説明も微調整されています。全体で3行が追加され、1行が削除され、内容が明確にされることで、ユーザーがファインチューニングを実施する際の理解が向上することを目指しています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -108,6 +108,18 @@ The following sections provide you with a quick guide to the default quotas and
 
 M = million | K = thousand
 
+### gpt-4o data zone standard
+
+| Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
+|---|---|:---:|:---:|
+|`gpt-4o`|Enterprise agreement | 10 M | 60 K |
+|`gpt-4o-mini` | Enterprise agreement | 20 M | 120 K |
+|`gpt-4o` |Default | 300 K | 1.8 K |
+|`gpt-4o-mini` | Default | 1 M | 6 K  |
+
+M = million | K = thousand
+
+
 ### gpt-4o standard
 
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
@@ -121,14 +133,14 @@ M = million | K = thousand
 
 #### Usage tiers
 
-Global Standard deployments use Azure's global infrastructure, dynamically routing customer traffic to the data center with best availability for the customer’s inference requests. This enables more consistent latency for customers with low to medium levels of traffic. Customers with high sustained levels of usage might see more variability in response latency.
+Global standard deployments use Azure's global infrastructure, dynamically routing customer traffic to the data center with best availability for the customer’s inference requests. Similarly, Data zone standard deployments allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. This enables more consistent latency for customers with low to medium levels of traffic. Customers with high sustained levels of usage might see more variability in response latency.
 
 The Usage Limit determines the level of usage above which customers might see larger variability in response latency. A customer’s usage is defined per model and is the total tokens consumed across all deployments in all subscriptions in all regions for a given tenant.
 
 > [!NOTE]
-> Usage tiers only apply to standard and global standard deployment types. Usage tiers do not apply to global batch and provisioned throughput deployments.
+> Usage tiers only apply to standard, data zone standard, and global standard deployment types. Usage tiers do not apply to global batch and provisioned throughput deployments.
 
-#### GPT-4o global standard & standard
+#### GPT-4o global standard, data zone standard, & standard
 
 |Model| Usage Tiers per month |
 |----|----|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "gpt-4oモデルの制限とクォータの更新"
}
```

### Explanation
この変更は、「quotas-limits.md」ファイルの更新であり、特にgpt-4oモデルに関するデータゾーンスタンダードの制限とクォータ情報が追加されました。具体的には、gpt-4oおよびgpt-4o-miniモデルに関するトークン制限やリクエスト数の情報が新たに含まれています。また、データゾーンスタンダードの利用についての説明が追加され、グローバル標準デプロイメントとの違いが明確にされています。さらに、使用限度に関する注意書きが更新され、適用対象が標準およびデータゾーンスタンダード、グローバルスタンダードに拡張されています。全体で15行が追加され、3行が削除されており、gpt-4oモデルの利用に関する最新の情報をユーザーに提供しています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -20,6 +20,11 @@ This article provides a summary of the latest releases and major documentation u
 
 ## October 2024
 
+### NEW data zone standard deployment type
+Data zone standard deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. Data zone standard provides higher default quotas than our Azure geography-based deployment types.  Data zone standard deployments are supported on `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13, and `gpt-4o-mini-2024-07-18` models.
+
+For more information, see the [deployment types guide](https://aka.ms/aoai/docs/deployment-types).
+
 ### Global Batch GA
 
 Azure OpenAI global batch is now generally available.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しいデータゾーンスタンダードデプロイメントタイプの追加"
}
```

### Explanation
この変更は、「whats-new.md」ファイルの更新で、Azure OpenAIに新たに追加された「データゾーンスタンダードデプロイメントタイプ」についての情報が盛り込まれています。この新しいデプロイメントタイプは、Microsoftが定義したデータゾーン内のデータセンターに動的にトラフィックをルーティングし、より高いクォータを提供することができる特徴を持っています。また、データゾーンスタンダードデプロイメントは特定のgpt-4oモデルに対応していることも言及されています。さらに、詳細情報へのリンクも追加されており、ユーザーがさらに学びやすくなっています。全体で5行が追加され、文書が最新のリリース情報を反映する形で更新されています。


