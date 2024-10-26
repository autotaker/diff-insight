---
date: '2024-10-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:edd8070...MicrosoftDocs:0bc728f
summary: この差分では、Azure OpenAIサービスに関連するモデルの文書が大幅に更新され、特に新しいスタンダードオーディオモデル、スタンダードチャット完了モデル、スタンダード完了モデル、スタンダード画像生成モデルに関する情報が追加されました。また、特定の既存モデルの非推奨日と退役日が更新され、誤字修正により文書の正確性と可読性が向上しました。これにより、ユーザーはモデルの選択や実装に関する重要な情報を簡単に得ることができ、Azure
  OpenAIをより効果的に活用できるようになります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:edd8070...MicrosoftDocs:0bc728f){target="_blank"}

<format>
# Highlights
この差分では、Azure OpenAIサービスに関連するモデルの非推奨および可用性に関する文書の更新、モデルとデプロイメントタイプの詳細、ならびにスタンダードオーディオモデル、チャット完了モデル、完了モデル、画像生成モデルの新しい文書追加などが含まれています。また、いくつかの細かな誤字修正が行われ、文書の正確性と可読性が向上しました。

## New features
- スタンダードオーディオモデル、スタンダードチャット完了モデル、スタンダード完了モデル、スタンダード画像生成モデルに関する新しい文書が追加されました。

## Breaking changes
- 特定の既存モデルの非推奨日と退役日が更新され、利用者はこれに応じてプランを更新する必要があります。

## Other updates
- 既存文書の誤字修正。
- 各種モデルの地域可用性テーブルの更新。
- Azure OpenAIモデルの非推奨日や退役日の調整。

# Insights
この差分では、Azure OpenAIの各種モデルに関する文書が大幅に更新され、特に利用可能な地域ごとのモデルの可用性情報が細かく整理されています。ユーザーはこれにより、特定のビジネスニーズや技術要件に合ったモデルを効果的に選択するための指針を得ることができます。

新しく追加された文書は、特に地域ごとの可用性に焦点を当てており、ユーザーがモデルの選択や実装を迅速かつ正確に行えるよう支援します。加えて、誤字の修正は文書全体の読みやすさを改善し、情報に基づく意思決定を支える重要な役割を果たしています。

Azure OpenAIサービスを使用するにあたり、これらの変更によってユーザーは最新のモデル機能や制限、そしてその利用可能性に関する詳細な情報に簡単にアクセスすることが可能となり、効率的かつ効果的にサービスを活用できるようになります。このような情報整理と新機能の追加は、Azure OpenAIが提供する幅広いAIサービスを最大限に活用する上で非常に価値があります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | Azure OpenAIモデルの非推奨および退役に関する更新 | modified | 7 | 2 | 9 | 
| [models.md](#item-db2c37) | minor update | Azure OpenAIモデルの詳細とデプロイメントタイプの更新 | modified | 77 | 49 | 126 | 
| [provisioned-throughput.md](#item-022e0c) | minor update | Provisioned Throughputに関する誤字修正 | modified | 2 | 2 | 4 | 
| [global-batch.md](#item-929e6a) | minor update | Global Batchモデルの地域可用性テーブルの更新 | modified | 6 | 6 | 12 | 
| [provisioned-global.md](#item-340884) | minor update | Provisioned Globalモデルの地域可用性テーブルの日付更新 | modified | 2 | 2 | 4 | 
| [provisioned-models.md](#item-8ee639) | minor update | Provisioned Modelsテーブルの地域可用性の更新 | modified | 25 | 25 | 50 | 
| [standard-audio.md](#item-1d8db7) | new feature | スタンダードオーディオモデルの可用性に関する新しい文書 | added | 20 | 0 | 20 | 
| [standard-chat-completions.md](#item-aae3f1) | new feature | スタンダードチャット完了モデルの可用性に関する新しい文書 | added | 29 | 0 | 29 | 
| [standard-completions.md](#item-a9c095) | new feature | スタンダード完了モデルの可用性に関する新しい文書 | added | 16 | 0 | 16 | 
| [standard-embeddings.md](#item-656427) | minor update | スタンダード埋め込みモデルの地域可用性に関する文書の更新 | modified | 14 | 14 | 28 | 
| [standard-global.md](#item-17a84b) | minor update | グローバルスタンダードモデルの地域可用性に関する文書の更新 | modified | 25 | 25 | 50 | 
| [standard-image-generation.md](#item-dd78ea) | new feature | スタンダード画像生成モデルの地域可用性に関する新しい文書の追加 | added | 16 | 0 | 16 | 
| [standard-models.md](#item-af04c4) | minor update | スタンダードモデルに関する資料の更新 | modified | 21 | 22 | 43 | 
| [whats-new.md](#item-53303b) | minor update | Whats NewにおけるGPT-4モデルの利用可能地域情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 10/02/2024
+ms.date: 10/25/2024
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -91,6 +91,8 @@ These models are currently available for use in Azure OpenAI Service.
 
 | Model | Version | Retirement date | Suggested replacements |
 | ---- | ---- | ---- | --- |
+| `babbage-002` | 1 | Deprecation Date: November 15, 2024 <br>Retirement Date: January 27, 2025 | |
+| `davinci-002` | 1 | Deprecation Date: November 15, 2024 <br>Retirement Date: January 27, 2025 | |
 | `dall-e-2`| 2 | January 27, 2025 | `dalle-3` |
 | `dall-e-3` | 3 | No earlier than April 30, 2025 | |
 | `gpt-35-turbo` | 0301 | January 27, 2025<br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024.   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
@@ -158,9 +160,12 @@ If you're an existing customer looking for information about these models, see [
 | code-search-babbage-code-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
 | code-search-babbage-text-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
 
-
 ## Retirement and deprecation history
 
+## October 25, 2024
+
+* `babbage-002` & `davinci-002` deprecation date: November 15, 2024  and retirement date: January 27, 2025.
+
 ## September 12, 2024
 
 * `gpt-35-turbo` (0301), (0613), (1106) and `gpt-35-turbo-16k` (0613) auto-update to default upgrade date updated to November 13, 2024.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIモデルの非推奨および退役に関する更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIに関する文書の更新を反映しています。具体的には、モデルの非推奨および退役に関する日付が修正され、新たに`babbage-002`および`davinci-002`モデルの非推奨日と退役日が追加されました。旧日付を新しい日付（2024年10月2日から2024年10月25日へ）に変更し、モデルの退役に関する情報を最新化することによって、利用者に正確で最新の情報を提供することを目的としています。また、モデルの非推奨日や退役日が表形式で整理され、わかりやすさも向上しています。この更新により、Azure OpenAIサービスを利用している顧客が必要な情報を容易に見つけられるようになっています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 10/09/2024
+ms.date: 10/25/2024
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -357,16 +357,40 @@ You can also use the OpenAI text to speech voices via Azure AI Speech. To learn
 
 ## Model summary table and region availability
 
-> [!NOTE]
-> This article primarily covers model/region availability that applies to all Azure OpenAI customers with deployment types of **Standard**. Some select customers have access to model/region combinations that are not listed in the unified table below. For more information on Provisioned deployments, see our [Provisioned guidance](./provisioned-throughput.md).
+### Models by deployment type
+
+Azure OpenAI provides customers with choices on the hosting structure that fits their business and usage patterns. The service offers two main types of deployment: 
+
+- **Standard** is offered with a global deployment option, routing traffic globally to provide higher throughput.
+- **Provisioned** is also offered with a global deployment option, allowing customers to purchase and deploy provisioned throughput units across Azure global infrastructure.
+
+All deployments can perform the exact same inference operations, however the billing, scale, and performance are substantially different. To learn more about Azure OpenAI deployment types see our [deployment types guide](../how-to/deployment-types.md).
+
+# [Global Standard](#tab/global-standard)
+
+### Global standard model availability
+
+[!INCLUDE [Standard Global](../includes/model-matrix/standard-global.md)]
+
+# [Global Provisioned Managed](#tab/global-ptum)
+
+### Global provisioned managed model availability
+
+[!INCLUDE [Provisioned Managed Global](../includes/model-matrix/provisioned-global.md)]
+
+# [Global Batch](#tab/global-batch)
+
+### Global batch model availability
+
+[!INCLUDE [Global batch](../includes/model-matrix/global-batch.md)]
+
+# [Standard](#tab/standard)
 
 ### Standard deployment model availability
 
 [!INCLUDE [Standard Models](../includes/model-matrix/standard-models.md)]
 
-This table doesn't include fine-tuning regional availability information.  Consult the [fine-tuning section](#fine-tuning-models) for this information.
-
-For information on default quota, refer to the [quota and limits article](../quotas-limits.md).
+# [Provisioned Managed](#tab/provisioned)
 
 ### Provisioned deployment model availability
 
@@ -377,24 +401,20 @@ For information on default quota, refer to the [quota and limits article](../quo
 
 For more information on Provisioned deployments, see our [Provisioned guidance](./provisioned-throughput.md).
 
-### Global standard model availability
+---
 
-[!INCLUDE [Standard Global](../includes/model-matrix/standard-global.md)]
+This table doesn't include fine-tuning regional availability information.  Consult the [fine-tuning section](#fine-tuning-models) for this information.
 
-### Global provisioned managed model availability
+### Standard models by endpoint
 
-[!INCLUDE [Provisioned Managed Global](../includes/model-matrix/provisioned-global.md)]
+# [Chat Completions](#tab/standard-chat-completions)
 
-### Global batch model availability
+### Chat completions
 
-[!INCLUDE [Global batch](../includes/model-matrix/global-batch.md)]
+[!INCLUDE [Chat Completions](../includes/model-matrix/standard-chat-completions.md)]
 
 ### GPT-4 and GPT-4 Turbo model availability
 
-#### Public cloud regions
-
-[!INCLUDE [GPT-4](../includes/model-matrix/standard-gpt-4.md)]
-
 #### Select customer access
 
 In addition to the regions above which are available to all Azure OpenAI customers, some select pre-existing customers have been granted access to versions of GPT-4 in additional regions:
@@ -406,23 +426,14 @@ In addition to the regions above which are available to all Azure OpenAI custome
 
 ### GPT-3.5 models
 
-> [!IMPORTANT]
-> The NEW `gpt-35-turbo (0125)`  model has various improvements, including higher accuracy at responding in requested formats and a fix for a bug which caused a text encoding issue for non-English language function calls.
-
-GPT-3.5 Turbo is used with the Chat Completion API. GPT-3.5 Turbo version 0301 can also be used with the Completions API, though this is not recommended.  GPT-3.5 Turbo versions 0613 and 1106 only support the Chat Completions API.
-
-GPT-3.5 Turbo version 0301 is the first version of the model released.  Version 0613 is the second version of the model and adds function calling support.
-
 See [model versions](../concepts/model-versions.md) to learn about how Azure OpenAI Service handles model version upgrades, and [working with models](../how-to/working-with-models.md) to learn how to view and configure the model version settings of your GPT-3.5 Turbo deployments.
 
-### GPT-3.5-Turbo model availability
-
-#### Public cloud regions
-
-[!INCLUDE [GPT-35-Turbo](../includes/model-matrix/standard-gpt-35-turbo.md)]
+# [Embeddings](#tab/standard-embeddings)
 
 ### Embeddings models
 
+[!INCLUDE [Embeddings](../includes/model-matrix/standard-embeddings.md)]
+
 These models can only be used with Embedding API requests.
 
 > [!NOTE]
@@ -438,21 +449,51 @@ These models can only be used with Embedding API requests.
 > [!NOTE]
 > When sending an array of inputs for embedding, the max number of input items in the array per call to the embedding endpoint is 2048.
 
-#### Public cloud regions
+# [Image Generation](#tab/standard-image-generations)
 
-[!INCLUDE [Embeddings](../includes/model-matrix/standard-embeddings.md)]
+### Image generation models
+
+[!INCLUDE [Image Generation](../includes/model-matrix/standard-image-generation.md)]
 
 ### DALL-E models
 
-|  Model ID  | Feature Availability | Max Request (characters) |
-|  --- |  --- | :---: |
-| dalle2 (preview) | East US | 1,000 |
-| dall-e-3 | East US, Australia East, Sweden Central | 4,000 |
+|  Model ID  | Max Request (characters) |
+|  --- | :---: |
+| dalle2 (preview)  | 1,000 |
+| dall-e-3  | 4,000 |
+
+# [Audio](#tab/standard-audio)
+
+### Audio models
+
+[!INCLUDE [Audio](../includes/model-matrix/standard-audio.md)]
+
+### Whisper models
 
-### Fine-tuning models
+|  Model ID  | Max Request (audio file size) |
+|  --- | :---: |
+| `whisper` | 25 MB |
+
+### Text to speech models (Preview)
+
+|  Model ID  | Description |
+|  --- | :--- |
+| `tts` | The latest Azure OpenAI text to speech model, optimized for speed. |
+| `tts-hd` | The latest Azure OpenAI text to speech model, optimized for quality.|
+ |
+
+# [Completions (Legacy)](#tab/standard-completions)
+
+### Completions models
 
 `babbage-002` and `davinci-002` are not trained to follow instructions. Querying these base models should only be done as a point of reference to a fine-tuned version to evaluate the progress of your training.
 
+[!INCLUDE [Completions](../includes/model-matrix/standard-completions.md)]
+
+---
+
+## Fine-tuning models
+
 `gpt-35-turbo` - fine-tuning of this model is limited to a subset of regions, and is not available in every region the base model is available.  
 
 |  Model ID  | Fine-Tuning Regions | Max Request (tokens) | Training Data (up to) |
@@ -468,20 +509,7 @@ These models can only be used with Embedding API requests.
 
 **<sup>1</sup>** GPT-4 is currently in public preview.
 
-### Whisper models
-
-|  Model ID  | Model Availability | Max Request (audio file size) |
-|  --- |  --- | :---: |
-| `whisper` | East US 2 <br> North Central US <br> Norway East <br> South India <br> Sweden Central <br> West Europe | 25 MB |
-
-### Text to speech models (Preview)
-
-|  Model ID  | Model Availability |
-|  --- |  --- | :---: |
-| `tts-1` | North Central US <br> Sweden Central |
-| `tts-1-hd` | North Central US <br> Sweden Central |
-
-### Assistants (Preview)
+## Assistants (Preview)
 
 For Assistants you need a combination of a supported model, and a supported region. Certain tools and capabilities require the latest models. The following models are available in the Assistants API, SDK, Azure AI Studio and Azure OpenAI Studio. The following table is for pay-as-you-go. For information on Provisioned Throughput Unit (PTU) availability, see [provisioned throughput](./provisioned-throughput.md). The listed models and regions can be used with both Assistants v1 and v2. You can use [global standard models](#global-standard-model-availability) if they are supported in the regions listed below. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIモデルの詳細とデプロイメントタイプの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIに関するモデルとデプロイメントタイプに関する情報を更新したものです。具体的には、文書内にモデルのデプロイメントタイプ（StandardおよびProvisioned）に基づく情報が明記され、各デプロイメントタイプの機能と特徴が詳細に説明されています。これにより、ユーザーが自分のビジネスニーズに合ったホスティング構造を選択しやすくなります。また、モデルの利用可能性に関するテーブルが改善され、さまざまなモデルの可用性が整理された形で示されています。

さらに、従来のテーブルから細かい調整が行われ、新しいモデルや機能の情報が追加されており、特に音声モデルや画像生成モデルなど、各種機能の利用方法に関する情報が積極的に提供されています。この変更は、利用者がAzure OpenAIサービスを最大限に活用できるように、新たな情報を反映することを目的としています。

## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ To help with simplifying the sizing effort, the following table outlines the TPM
 | Input TPM per PTU | 2,500 | 37,000  |
 | Output TPM per PTU | 833  | 12,333 |
 
-\** For a full list see the [AOAI Studio calcualator](https://oai.azure.com/portal/calculator)
+For a full list see the [AOAI Studio calculator](https://oai.azure.com/portal/calculator).
 
 
 ## Key concepts
@@ -114,7 +114,7 @@ In Azure OpenAI Studio, the deployment experience identifies when a region lacks
 
 Details on the new deployment experience can be found in the Azure OpenAI [Provisioned get started guide](../how-to/provisioned-get-started.md).
 
-The new [model capacities API](/rest/api/aiservices/accountmanagement/model-capacities/list?view=rest-aiservices-accountmanagement-2024-04-01-preview&tabs=HTTP&preserve-view=true) can  be used to programmatically identify the maximum sized deployment of a specified model.  The API consideres both the your quota and service capacity in the region.
+The new [model capacities API](/rest/api/aiservices/accountmanagement/model-capacities/list?view=rest-aiservices-accountmanagement-2024-04-01-preview&tabs=HTTP&preserve-view=true) can  be used to programmatically identify the maximum sized deployment of a specified model.  The API considers both your quota and service capacity in the region.
 
 If an acceptable region isn't available to support the desire model, version and/or PTUs, customers can also try the following steps:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Provisioned Throughputに関する誤字修正"
}
```

### Explanation
このコードの変更では、Azure OpenAIの「Provisioned Throughput」文書において、いくつかの誤字修正が行われました。具体的には、計算機に関する文言が修正され、誤って「calcualator」と記載されていた部分が「calculator」に修正されています。また、文章中の「consideres」という単語が「considers」に修正され、文の流れをスムーズにするための改善が加えられています。

これらの修正により、文書の正確性と読みやすさが向上し、利用者にとってより分かりやすい情報提供が実現されています。全体として、変更は軽微ですが、専門的な文書においては重要な修正となります。

## articles/ai-services/openai/includes/model-matrix/global-batch.md{#item-929e6a}

<details>
<summary>Diff</summary>
````diff
@@ -5,11 +5,11 @@ description: Regional availability for Global Batch models
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 10/03/2024
+ms.date: 10/24/2024
 ---
 
-| **Region**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
-|:-----------------|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
-| eastus           | ✅                | ✅                            | ✅                       | ✅                       | ✅                            | ✅                       | ✅                       | ✅                       |
-| swedencentral    | ✅                | ✅                            | ✅                       | ✅                       | ✅                            | ✅                       | ✅                       | ✅                       |
-| westus           | ✅                | ✅                            | ✅                       | ✅                       | ✅                            | ✅                       | ✅                       | ✅                       |
\ No newline at end of file
+| **Region**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
+|:-----------------|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
+| eastus           | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| swedencentral    | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westus           | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Global Batchモデルの地域可用性テーブルの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIにおける「Global Batchモデル」の地域可用性に関するテーブルを更新したものです。具体的には、モデルのバージョンや地域に関連する情報が整理され、列の順序が変更されました。これにより、どのモデルがどの地域で利用可能かが一目で分かるように改善されています。

主な変更点としては、モデルの順序の変更と、最新のリリース日付を含むモデルの情報が反映されています。これにより、利用者は地域における特定のモデルの可用性を簡単に確認でき、迅速な意思決定が可能となります。このテーブルは、Azure OpenAIのサービスを利用する上で重要なリソースとなっており、情報の提供がより明確且つ正確になったことが確認できます。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 10/03/2024
+ms.date: 10/25/2024
 ---
 
 | **Region**     | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
@@ -34,4 +34,4 @@ ms.date: 10/03/2024
 | uksouth            | ✅                       | ✅                            |
 | westeurope         | ✅                       | ✅                            |
 | westus             | ✅                       | ✅                            |
-| westus3            | ✅                       | ✅                            |
+| westus3            | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Provisioned Globalモデルの地域可用性テーブルの日付更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIの「Provisioned Globalモデル」に関する地域可用性テーブルの日付情報を更新したものです。具体的には、`ms.date`の値が「2024年10月3日」から「2024年10月25日」に変更されています。この変更により、文書が最新の情報を反映するようになっています。

また、テーブルの内容に変更はありませんが、`westus3`地域に関する情報が改めて整理されています。このような更新は、利用者に対して正確で最新のリソースを提供するために重要です。文書は引き続き、特定の地域でのモデルの可用性を明示しており、ユーザーが必要な情報を容易に得られるように保たれています。

## articles/ai-services/openai/includes/model-matrix/provisioned-models.md{#item-8ee639}

<details>
<summary>Diff</summary>
````diff
@@ -6,30 +6,30 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 10/03/2024
+ms.date: 10/24/2024
 ---
 
-| **Region**     | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
-|:-------------------|:-------------------:|:---------------------------:|:---------------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|
-| australiaeast      | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | ✅                       | ✅                       |
-| brazilsouth        | ✅                | ✅                        | ✅                        | -                           | ✅                       | -                      | ✅                            | ✅                    | ✅                       | -                      |
-| canadacentral      | ✅                | -                       | -                       | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       |
-| canadaeast         | ✅                | ✅                        | -                       | ✅                            | ✅                       | -                      | ✅                            | -                   | ✅                       | -                      |
-| eastus             | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | ✅                       | ✅                       |
-| eastus2            | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | ✅                       | ✅                       |
-| francecentral      | ✅                | ✅                        | ✅                        | -                           | ✅                       | -                      | ✅                            | ✅                    | -                      | ✅                       |
-| germanywestcentral | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | -                      | -                           | ✅                    | ✅                       | -                      |
-| japaneast          | -               | ✅                        | ✅                        | ✅                            | ✅                       | -                      | ✅                            | -                   | -                      | ✅                       |
-| koreacentral       | ✅                | -                       | -                       | ✅                            | ✅                       | -                      | ✅                            | ✅                    | ✅                       | -                      |
-| northcentralus     | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | ✅                       | ✅                       |
-| norwayeast         | ✅                | -                       | ✅                        | -                           | -                      | -                      | ✅                            | ✅                    | -                      | -                      |
-| polandcentral      | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | -                      | -                           | ✅                    | ✅                       | ✅                       |
-| southafricanorth   | ✅                | ✅                        | -                       | ✅                            | ✅                       | -                      | -                           | ✅                    | ✅                       | -                      |
-| southcentralus     | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | -                      | -                           | ✅                    | ✅                       | ✅                       |
-| southindia         | ✅                | ✅                        | ✅                        | -                           | ✅                       | -                      | ✅                            | ✅                    | ✅                       | ✅                       |
-| swedencentral      | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | ✅                       | ✅                       |
-| switzerlandnorth   | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | -                      | ✅                            | ✅                    | ✅                       | ✅                       |
-| switzerlandwest    | -               | -                       | -                       | -                           | -                      | -                      | -                           | -                   | -                      | ✅                       |
-| uksouth            | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | -                      | -                           | ✅                    | ✅                       | ✅                       |
-| westus             | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | ✅                       | ✅                       |
-| westus3            | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | ✅                       | -                           | ✅                    | ✅                       | ✅                       |
\ No newline at end of file
+| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
+|:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|
+| australiaeast      | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| brazilsouth        | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | -                      |
+| canadacentral      | -                      | -                      | -                           | ✅                | -                       | -                       | -                           | ✅                    | -                      | ✅                       |
+| canadaeast         | ✅                       | -                      | ✅                            | ✅                | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      |
+| eastus             | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| eastus2            | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| francecentral      | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | -                      | ✅                       |
+| germanywestcentral | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | -                      |
+| japaneast          | ✅                       | -                      | ✅                            | -               | ✅                        | ✅                        | ✅                            | -                   | -                      | ✅                       |
+| koreacentral       | ✅                       | -                      | ✅                            | ✅                | -                       | -                       | ✅                            | ✅                    | ✅                       | -                      |
+| northcentralus     | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| norwayeast         | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                           | ✅                    | -                      | -                      |
+| polandcentral      | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| southafricanorth   | ✅                       | -                      | -                           | ✅                | ✅                        | -                       | ✅                            | ✅                    | ✅                       | -                      |
+| southcentralus     | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| southindia         | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | ✅                       |
+| swedencentral      | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| switzerlandnorth   | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| switzerlandwest    | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
+| uksouth            | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| westus             | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| westus3            | ✅                       | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Provisioned Modelsテーブルの地域可用性の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIにおける「Provisioned Models」に関する地域可用性テーブルの更新です。主に、`ms.date`の更新やモデルの可用性に関する情報が整理されています。具体的には、日付が「2024年10月3日」から「2024年10月24日」に変更されました。

テーブル自体は、各モデルがどの地域で利用可能かを示しており、列の整理が行われています。ここでは、`gpt-4o`、`gpt-4`、および`gpt-35-turbo`モデルの地域毎の可用性が明示され、それぞれの地域における対応状況が整理されています。特に、一部のモデルが新たに追加される地域や既存の地域での可用性の変化が反映されています。

この修正により、ユーザーは最新の情報に基づいてモデルの選択を行うことができ、全体的なユーザー体験が向上します。新しい情報は、利用者にとって重要な意思決定の基盤となるため、このような更新は非常に重要です。

## articles/ai-services/openai/includes/model-matrix/standard-audio.md{#item-1d8db7}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,20 @@
+---
+title: Standard audio model availability
+titleSuffix: Azure OpenAI Service
+description: Standard audio model availability
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.custom: references_regions
+ms.date: 10/25/2024
+---
+
+| **Region**   | **tts**, **001**   | **tts-hd**, **001**   | **whisper**, **001**   |
+|:-----------------|:----------------:|:-------------------:|:--------------------:|
+| eastus2          | -            | -               | ✅                 |
+| northcentralus   | ✅             | ✅                | ✅                 |
+| norwayeast       | -            | -               | ✅                 |
+| southindia       | -            | -               | ✅                 |
+| swedencentral    | ✅             | ✅                | ✅                 |
+| switzerlandnorth | -            | -               | ✅                 |
+| westeurope       | -            | -               | ✅                 |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "スタンダードオーディオモデルの可用性に関する新しい文書"
}
```

### Explanation
このコードの変更は、新たに「スタンダードオーディオモデルの可用性」と題された文書が追加されたことを示しています。文書には、Azure OpenAI Serviceの各地域における標準オーディオモデル（テキスト・トゥ・スピーチ、Whisperなど）の可用性が示されています。

新しく追加されたテーブルには、複数の地域における各モデルの対応状況が示されており、具体的には以下のモデルが含まれています：
- Text to Speech (tts)
- Text to Speech HD (tts-hd)
- Whisper

例えば、`northcentralus`地域では、すべてのモデルが利用可能である一方、`eastus2`や`norwayeast`地域などでは、Whisperモデルのみが利用可能であることが示されています。これにより、ユーザーは特定の地域における各モデルの可用性を簡単に把握できるようになり、適切な選択を行う際の助けとなります。この変更は、ユーザーにとって重要な新機能であり、情報を明確に整理することで、サービスの効果的な利用を促進します。

## articles/ai-services/openai/includes/model-matrix/standard-chat-completions.md{#item-aae3f1}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,29 @@
+---
+title: Standard chat completions model availability
+titleSuffix: Azure OpenAI Service
+description: Standard chat completions model availability
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.custom: references_regions
+ms.date: 10/25/2024
+---
+
+| **Region**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **vision-preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **0301**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   | **gpt-35-turbo-16k**, **0613**   |
+|:-----------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-----------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:------------------------------:|
+| australiaeast    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           |
+| canadaeast       | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           |
+| eastus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           |
+| eastus2          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           |
+| francecentral    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | ✅                       | ✅                       | ✅                       | -                      | ✅                           |
+| japaneast        | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | ✅                          | -                           | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           |
+| northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           |
+| norwayeast       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          |
+| southcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | -                      | -                      | ✅                       | -                          |
+| southindia       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | ✅                       | -                      | -                          |
+| swedencentral    | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           |
+| switzerlandnorth | -                          | -                       | -                      | -                      | -                           | ✅                | -                       | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | -                      | -                      | ✅                           |
+| uksouth          | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | ✅                        | -                         | -                           | -                   | ✅                       | ✅                       | ✅                       | ✅                       | ✅                           |
+| westeurope       | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          |
+| westus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | ✅                          | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          |
+| westus3          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "スタンダードチャット完了モデルの可用性に関する新しい文書"
}
```

### Explanation
このコードの変更は、新たに「スタンダードチャット完了モデルの可用性」に関する文書が追加されたことを示しています。この文書では、Azure OpenAI Serviceにおけるスタンダードチャット完了モデルの地域ごとの可用性が詳細に記載されています。

新たに追加されたテーブルには、複数のチャット完了モデル（o1-preview、gpt-4o、gpt-35-turboなど）の対応地域が一覧化されており、各地域におけるモデルの可用性がマークされています。例えば、`northcentralus`地域では、複数のモデルが利用可能である一方、`norwayeast`地域では、特定のモデルの可用性が確認できないという情報が示されています。

この変更により、ユーザーは特定の地域でどのモデルが利用できるのかを一目で把握でき、適切な選択を行う際の手助けとなります。また、チャットアプリケーションやAIサービスを開発する際に、利用可能なリソースを明確に理解するために重要な情報を提供しています。このような新しい文書は、利用者にとって有益であり、サービスの円滑な利用を促進する役割を果たします。

## articles/ai-services/openai/includes/model-matrix/standard-completions.md{#item-a9c095}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,16 @@
+---
+title: Standard completions model availability
+titleSuffix: Azure OpenAI Service
+description: Standard completions model availability
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.custom: references_regions
+ms.date: 10/25/2024
+---
+
+| **Region**   | **gpt-35-turbo-instruct**, **0914**   | **babbage-002**, **1**   | **davinci-002**, **1**   |
+|:-----------------|:-----------------------------------:|:----------------------:|:----------------------:|
+| eastus           | ✅                                | -                  | -                  |
+| northcentralus   | -                               | ✅                   | ✅                   |
+| swedencentral    | ✅                                | ✅                   | ✅                   |
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "スタンダード完了モデルの可用性に関する新しい文書"
}
```

### Explanation
このコードの変更は、新たに「スタンダード完了モデルの可用性」に関する文書が追加されたことを示しています。この文書では、Azure OpenAI Serviceのスタンダード完了モデルが、地域ごとにどのように利用可能かが記載されています。

新たに追加されたテーブルには、`gpt-35-turbo-instruct`、`babbage-002`、`davinci-002`といったモデルの各地域における可用性が示されています。例えば、`eastus`地域では`gpt-35-turbo-instruct`が利用可能である一方、`northcentralus`地域では`babbage-002`と`davinci-002`が利用可能であることが明確に示されています。

この変更により、ユーザーは特定のモデルがどの地域で利用できるかを簡単に把握でき、AIベースのアプリケーションを開発・展開する際の参考情報として活用することができます。新しい文書は、モデルの地域別の可用性を提供することで、ユーザーが最適な選択を行うためのサポートを行い、Azureのサービス利用をよりスムーズにします。

## articles/ai-services/openai/includes/model-matrix/standard-embeddings.md{#item-656427}

<details>
<summary>Diff</summary>
````diff
@@ -5,26 +5,26 @@ description: embedding model regional availability
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 03/13/2024
+ms.date: 03/25/2024
 ---
 
-| **Region**   | **text-embedding-ada-002**, **1**   | **text-embedding-ada-002**, **2**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   |
+| **Region**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **1**   | **text-embedding-ada-002**, **2**   |
 |:-----------------|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|
-| australiaeast    | -                             | ✅                              | -                             | -                             |
-| brazilsouth      | -                             | ✅                              | -                             | -                             |
-| canadaeast       | -                             | ✅                              | ✅                              | ✅                              |
+| australiaeast    | -                             | -                             | -                             | ✅                              |
+| brazilsouth      | -                             | -                             | -                             | ✅                              |
+| canadaeast       | ✅                              | ✅                              | -                             | ✅                              |
 | eastus           | ✅                              | ✅                              | ✅                              | ✅                              |
-| eastus2          | -                             | ✅                              | ✅                              | ✅                              |
+| eastus2          | ✅                              | ✅                              | -                             | ✅                              |
 | francecentral    | -                             | ✅                              | -                             | ✅                              |
-| japaneast        | -                             | ✅                              | -                             | ✅                              |
-| northcentralus   | -                             | ✅                              | -                             | -                             |
+| japaneast        | ✅                              | ✅                              | -                             | ✅                              |
+| northcentralus   | -                             | -                             | -                             | ✅                              |
 | norwayeast       | -                             | ✅                              | -                             | ✅                              |
-| southafricanorth | -                             | ✅                              | -                             | -                             |
-| southcentralus   | ✅                              | ✅                              | -                             | -                             |
+| southafricanorth | -                             | -                             | -                             | ✅                              |
+| southcentralus   | -                             | -                             | ✅                              | ✅                              |
 | southindia       | -                             | ✅                              | -                             | ✅                              |
 | swedencentral    | -                             | ✅                              | -                             | ✅                              |
-| switzerlandnorth | -                             | ✅                              | -                             | -                             |
+| switzerlandnorth | -                             | -                             | -                             | ✅                              |
 | uksouth          | -                             | ✅                              | -                             | ✅                              |
-| westeurope       | -                             | ✅                              | -                             | -                             |
-| westus           | -                             | ✅                              | -                             | -                             |
-| westus3          | -                             | ✅                              | -                             | ✅                              |
+| westeurope       | -                             | -                             | -                             | ✅                              |
+| westus           | -                             | -                             | -                             | ✅                              |
+| westus3          | -                             | ✅                              | -                             | ✅                              |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スタンダード埋め込みモデルの地域可用性に関する文書の更新"
}
```

### Explanation
このコードの変更は、スタンダード埋め込みモデルに関する文書が修正され、地域ごとのモデルの可用性に関する情報が更新されたことを示しています。具体的には、文書の説明やモデルの配置が整理されています。

主な変更点には、最初の列のモデルの順序が変更され、新しい日時が設定されていることが含まれています。また、地域ごとの埋め込みモデルの可用性に関して、いくつかのモデルが新たに追加、または移動されています。たとえば、`canadaeast`地域では`text-embedding-ada-002`と`text-embedding-3-large`が利用可能として更新されており、`australiaeast`地域や`brazilsouth`地域の記載も変更されています。

これにより、利用者は最新のモデル可用性情報を反映した文書にアクセスでき、特定の地域における埋め込みモデルの利用可能性を迅速に理解できるようになります。この更新は、Azure OpenAI Serviceを利用する際に重要なリソースを提供し、ユーザーの意思決定をサポートします。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -5,30 +5,30 @@ description: Regional availability for Global Standard models.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 10/03/2024
+ms.date: 10/25/2024
 ---
 
-| **Region**     | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-10-01**   |
-|:-------------------|:------------------------------:|:---------------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|
-| australiaeast      | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| brazilsouth        | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| canadaeast         | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| eastus             | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
-| eastus2            | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                                        |
-| francecentral      | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| germanywestcentral | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| japaneast          | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| koreacentral       | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| northcentralus     | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
-| norwayeast         | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| polandcentral      | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| southafricanorth   | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| southcentralus     | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
-| southindia         | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| spaincentral       | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| swedencentral      | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                                        |
-| switzerlandnorth   | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| uksouth            | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| westeurope         | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| westus             | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
-| westus3            | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
+| **Region**     | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-10-01**   | **gpt-4**, **turbo-2024-04-09**   |
+|:-------------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:-------------------------------:|
+| australiaeast      | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| brazilsouth        | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| canadaeast         | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| eastus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
+| eastus2            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                            |
+| francecentral      | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| germanywestcentral | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| japaneast          | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| koreacentral       | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| northcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
+| norwayeast         | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| polandcentral      | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| southafricanorth   | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| southcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
+| southindia         | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| spaincentral       | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
+| swedencentral      | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                            |
+| switzerlandnorth   | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| uksouth            | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| westeurope         | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| westus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
+| westus3            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルスタンダードモデルの地域可用性に関する文書の更新"
}
```

### Explanation
このコードの変更は、グローバルスタンダードモデルに関する文書が修正され、地域ごとのモデルの可用性情報が最新化されたことを示しています。具体的には、モデルの配列が変更され、日付が更新されています。

主な変更点として、`gpt-4o`、`gpt-4o-mini`、`gpt-4o-realtime-preview`のモデルがテーブル内での順序が変更され、地域ごとの可用性が新たに整理されています。以前のバージョンでは`gpt-4`が最後に記載されていましたが、更新後の文書では他のモデルよりも後ろに移動しました。

これにより、利用者は最新の地域ごとのモデル可用性に関する情報を一目で確認でき、特定の地域でどのモデルが利用可能かを素早く把握できるようになります。また、ユーザーが選択する際の参考にしやすく、Azure OpenAI Serviceの利用価値を高めることでしょう。この更新は、ユーザーが必要な情報に迅速にアクセスできるようにし、サービス利用の効率を向上させるものとなります。

## articles/ai-services/openai/includes/model-matrix/standard-image-generation.md{#item-dd78ea}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,16 @@
+---
+title: Standard image model availability
+titleSuffix: Azure OpenAI Service
+description: Standard image model availability
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.custom: references_regions
+ms.date: 10/25/2024
+---
+
+| **Region**   | **dall-e-2**, **2.0**   | **dall-e-3**, **3.0**   |
+|:-----------------|:---------------------:|:---------------------:|
+| australiaeast    | -                 | ✅                  |
+| eastus           | ✅                  | ✅                  |
+| swedencentral    | -                 | ✅                  |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "スタンダード画像生成モデルの地域可用性に関する新しい文書の追加"
}
```

### Explanation
このコードの変更は、スタンダード画像生成モデルに関する新しい文書が追加されたことを示しています。この文書では、`dall-e-2`および`dall-e-3`モデルの地域ごとの可用性について記載されています。

追加された内容には、文書のメタデータとしてタイトル、説明、管理者、サービスの情報、日付が含まれており、文書がどのように構成されているかを示しています。さらに、具体的な地域における各モデルの利用可能性が表形式で示されており、各地域に対する情報は以下の通りです:

- `australiaeast`地域では`dall-e-2`は未対応であるのに対し、`dall-e-3`は対応しています。
- `eastus`地域では両方のモデルが対応しており、利用可能です。
- `swedencentral`地域では`dall-e-2`は未対応ですが、`dall-e-3`は対応しています。

この文書の追加により、Azure OpenAI Serviceにおけるスタンダード画像生成モデルの地域ごとの利用可能性に関する情報が提供され、ユーザーが必要とする情報にアクセスしやすくなります。これにより、モデルの選択やサービスの利用において、ユーザーはより明確な判断を下せるようになるでしょう。

## articles/ai-services/openai/includes/model-matrix/standard-models.md{#item-af04c4}

<details>
<summary>Diff</summary>
````diff
@@ -5,27 +5,26 @@ description: Quota and limits for Azure OpenAI by region.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 10/04/2024
+ms.date: 10/25/2024
 ---
 
-| **Region**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **vision-preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **0301**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   | **gpt-35-turbo-16k**, **0613**   | **gpt-35-turbo-instruct**, **0914**   | **text-embedding-ada-002**, **1**   | **text-embedding-ada-002**, **2**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **dall-e-2**, **2.0**   | **dall-e-3**, **3.0**   | **babbage-002**, **1**   | **davinci-002**, **1**   | **tts**, **001**   | **tts-hd**, **001**   | **whisper**, **001**   |
-|:-----------------|:------------------------------:|:---------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-----------------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:------------------------------:|:-----------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------:|:---------------------:|:----------------------:|:----------------------:|:----------------:|:-------------------:|:--------------------:|
-| australiaeast    | -                          | -                       | ✅                | ✅                        | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | ✅                  | -                  | -                  | -            | -               | -                |
-| brazilsouth      | -                          | -                       | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
-| canadaeast       | -                          | -                       | ✅                | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| eastus           | ✅                           | ✅                        | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | ✅                  | -                  | -                  | -            | -               | -                |
-| eastus2          | ✅                           | ✅                        | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| francecentral    | -                          | -                       | ✅                | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | ✅                    | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| japaneast        | -                          | -                       | -               | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | -                   | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| northcentralus   | ✅                           | ✅                        | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
-| norwayeast       | -                          | -                       | -               | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| southafricanorth | -                          | -                       | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
-| southcentralus   | ✅                           | ✅                        | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | ✅                       | -                      | -                      | ✅                       | -                          | -                               | ✅                              | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
-| southindia       | -                          | -                       | -               | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | ✅                       | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| swedencentral    | ✅                           | ✅                        | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           | ✅                                | -                             | ✅                              | -                             | ✅                              | -                 | ✅                  | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
-| switzerlandnorth | -                          | -                       | ✅                | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| uksouth          | -                          | -                       | -               | ✅                        | ✅                        | -                         | -                           | -                      | -                      | -                           | -                   | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| westeurope       | -                          | -                       | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| westus           | ✅                           | ✅                        | -               | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
-| westus3          | ✅                           | ✅                        | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-
+| **Region**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **vision-preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **0301**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   | **gpt-35-turbo-16k**, **0613**   | **gpt-35-turbo-instruct**, **0914**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **1**   | **text-embedding-ada-002**, **2**   | **dall-e-2**, **2.0**   | **dall-e-3**, **3.0**   | **babbage-002**, **1**   | **davinci-002**, **1**   | **tts**, **001**   | **tts-hd**, **001**   | **whisper**, **001**   |
+|:-----------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-----------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:------------------------------:|:-----------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------:|:---------------------:|:----------------------:|:----------------------:|:----------------:|:-------------------:|:--------------------:|
+| australiaeast    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | -                             | -                             | ✅                              | -                 | ✅                  | -                  | -                  | -            | -               | -                |
+| brazilsouth      | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| canadaeast       | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| eastus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | ✅                  | -                  | -                  | -            | -               | -                |
+| eastus2          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| francecentral    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| japaneast        | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | ✅                          | -                           | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
+| norwayeast       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| southafricanorth | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| southcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | -                      | -                      | ✅                       | -                          | -                               | -                             | -                             | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| southindia       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | ✅                       | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| swedencentral    | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           | ✅                                | -                             | ✅                              | -                             | ✅                              | -                 | ✅                  | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
+| switzerlandnorth | -                          | -                       | -                      | -                      | -                           | ✅                | -                       | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| uksouth          | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | ✅                        | -                         | -                           | -                   | ✅                       | ✅                       | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| westeurope       | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| westus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | ✅                          | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| westus3          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スタンダードモデルに関する資料の更新"
}
```

### Explanation
このコードの変更は、スタンダードモデルに関する文書が修正されたことを示しています。主な内容としては、地域ごとのモデルの可用性情報が更新され、日付も新しいものに変更されています。

具体的な変更内容には、以下の点が含まれています：

- 文書の日付が2024年10月25日に更新されました。
- 表形式で示されたモデルの可用性データにおいて、一部のモデル名が移動しました。
- 新しいモデルの追加や既存モデルの削除に伴い、表の行と列の順序が変更されています。

例えば、`gpt-4o`、`gpt-4o-mini`、`gpt-4-32k`などのモデルの位置が変更され、特定の地域におけるその可用性がより明確に示されるようになっています。また、モデルの可用性において、特定の地域での対応状況も見やすくなっており、ユーザーはどのモデルがどの地域で利用可能かを簡単に把握できるようになっています。

この更新により、Azure OpenAI Serviceにおけるスタンダードモデルの利用に関する理解が深まり、利用者が必要な情報に素早くアクセスできるようになることを目的としています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -405,7 +405,7 @@ Fine-tuning now supports [multi-turn chat training examples](./how-to/fine-tunin
 
 ### GPT-4 (0125) is available for Azure OpenAI On Your Data
 
-You can now use the GPT-4 (0125) model in [available regions](./concepts/models.md#public-cloud-regions) with Azure OpenAI On Your Data.
+You can now use the GPT-4 (0125) model in [available regions](./concepts/models.md#chat-completions-1) with Azure OpenAI On Your Data.
 
 ## March 2024
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whats NewにおけるGPT-4モデルの利用可能地域情報の更新"
}
```

### Explanation
このコードの変更は、「Whats New」文書内のGPT-4 (0125)モデルに関する情報が修正されたことを示しています。変更内容は非常に小規模で、追加された文と削除された文の変更が反映されています。

具体的には、GPT-4 (0125)モデルを使用できる地域に関するリンクが更新されており、以前のリンクから新しいリンクへの変更が行われています。以前は「available regions」として示されていたリンクは、今後は「chat-completions-1」として参照されるようになります。

この修正により、利用者が特定のモデルに関する最新情報にアクセスしやすくなり、より正確な情報源に導かれることが期待されています。このような改善は、ユーザーがAzure OpenAIの各モデルについての利用可能性を把握する上での利便性を向上させます。


