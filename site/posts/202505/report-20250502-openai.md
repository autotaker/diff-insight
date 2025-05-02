---
date: '2025-05-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0ff32a6...MicrosoftDocs:cfed402
summary: このコード変更は、Azure OpenAIサービスに関するドキュメントの一部を更新し、特にモデルごとの最大出力トークン、プロビジョニングスループットの日付、説明、およびプロビジョニンググローバルリソースの情報を改訂することを目的としています。具体的には、GPT
  4.1モデルの詳細情報が追加され、プロビジョニングスループットに関する情報が具体化されました。致命的な変更は報告されていませんが、情報の更新に伴い、従来の理解の見直しが必要な場合があります。また、ドキュメントの更新日も最新に修正され、地域別のモデル対応状況が向上しています。これにより、利用者に対してより明確で正確な情報が提供され、効率的なリソース利用の促進に寄与します。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0ff32a6...MicrosoftDocs:cfed402){target="_blank"}

<format>
# Highlights
このコード変更は、Azure OpenAIサービスに関するドキュメントの一部を更新することを目的としています。具体的には、モデルごとの最大出力トークン、プロビジョニングスループットの日付、プロビジョニングスループットに関する説明、およびプロビジョニンググローバルリソースの情報が更新されました。

## New features
- GPT 4.1モデルの最大出力トークンの情報がより詳細に提供されました。
- プロビジョニングスループットに関するモデル情報が具体化され、特に入力と出力トークンの価格比が明確化されました。

## Breaking changes
- 特に致命的な変更は報告されていませんが、情報の更新により、従来の理解に変更が必要な場合があります。

## Other updates
- ドキュメントの更新日が最新の日付に修正され、内容が最新のものであることを保証しています。
- プロビジョニンググローバルリソースに関する地域別のモデル対応状況が改善されました。

# Insights
今回の変更は、Azure OpenAIサービスの利用者に対して、より明確で正確な情報を提供することを目的としています。特に、大規模な言語モデルであるGPT 4.1に関する詳細情報の追加は、利用者がこれらのモデルを実際のアプリケーションでどのように活用できるかについての理解を深めるのに役立ちます。

まず、`models.md`ファイルでの最大出力トークンに関する更新は、GPT 4.1の実際の利用方法に影響を与える可能性があるため、重要です。特に、プロビジョニングされたマネージドデプロイメントでの制限が記載されたことで、ユーザーは計画をより具体的に立てることが可能になります。

次に、`provisioned-throughput.md`ファイルで日付が更新されたことで、ドキュメントの新鮮さが保証され、利用者は最新情報に基づいて判断を下すことができます。

さらに、`provisioned-throughput-onboarding.md`における詳細なスループット情報の追加は、投入と出力のトークンのコスト構造を明確にし、効率的な利用を促進します。特に、出力トークンが4つの入力トークンとしてカウントされるという情報は、リソースを最適に活用したい企業にとって非常に有用です。

最後に、`provisioned-global.md`ファイルにおいて、新しいモデルの対応地域が追加され、グローバル展開を視野に入れるユーザーに役立つ最新情報が提供されています。これらすべての更新は、Azure OpenAIサービスが提供する情報の透明性と信頼性を高めることに寄与しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | OpenAIモデルの最大出力トークンの情報更新 | modified | 1 | 1 | 2 | 
| [provisioned-throughput.md](#item-022e0c) | minor update | プロビジョニングスループットに関する日付の更新 | modified | 1 | 1 | 2 | 
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | プロビジョニングスループットの説明とモデル情報の更新 | modified | 13 | 12 | 25 | 
| [provisioned-global.md](#item-340884) | minor update | プロビジョニンググローバルリソースのデータ更新 | modified | 29 | 29 | 58 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -43,7 +43,7 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 
 |  Model ID  | Description | Context Window | Max Output Tokens | Training Data (up to)  |
 |  --- |  :--- |:--- |:---|:---: |
-| `gpt-4.1` (2025-04-14)   | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | 1,047,576 | 32,768 | May 31, 2024 |
+| `gpt-4.1` (2025-04-14)   | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | - 1,047,576 <br> - 128,000 (provisioned managed deployments) | 32,768 | May 31, 2024 |
 | `gpt-4.1-nano` (2025-04-14) <br><br> **Fastest 4.1 model** | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | 1,047,576  | 32,768 | May 31, 2024 |
 | `gpt-4.1-mini` (2025-04-14) | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | 1,047,576  | 32,768 | May 31, 2024 |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OpenAIモデルの最大出力トークンの情報更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関するドキュメントの一部であり、「models.md」というファイルにおいて、特定のモデル（`gpt-4.1`）の最大出力トークンに関する情報が更新されました。具体的には、`gpt-4.1`モデルの行において、最大出力トークンの値が以下のように変更されています。

以前は「1,047,576」と記載されていた部分が、現在は「- 1,047,576 <br> - 128,000 (provisioned managed deployments)」という形になっています。これにより、モデルの能力や運用に関する重要な詳細が追加され、ユーザーが利用可能な情報がより明確になっています。この更新は、ドキュメントの正確性向上に寄与しています。

## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Azure OpenAI Service provisioned throughput
 description: Learn about provisioned throughput and Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 03/31/2025
+ms.date: 04/30/2025
 manager: nitinme
 author: aahill #ChrisHMSFT
 ms.author: aahi #chrhoder
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングスループットに関する日付の更新"
}
```

### Explanation
この変更は、「provisioned-throughput.md」というファイルに関するもので、Azure OpenAIサービスのプロビジョニングスループットに関連する情報が更新されました。具体的には、ドキュメントのメタデータに記載されている日付が変更されています。

以前の更新日（`ms.date`）は「2025年3月31日」であり、これが新しい日付「2025年4月30日」に変更されました。この修正は、コンテンツの最新性を保ち、利用者に正確な情報を提供するためのものです。日付の更新により、ユーザーはドキュメントがどの程度新しいかを把握しやすくなります。

## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -72,23 +72,24 @@ Customers that require long-term usage of provisioned, data zoned provisioned, a
 > Charges for deployments on a deleted resource will continue until the resource is purged. To prevent this, delete a resource’s deployment before deleting the resource. For more information, see [Recover or purge deleted Azure AI services resources](../../recover-purge-resources.md). 
 
 ## How much throughput per PTU you get for each model
-The amount of throughput (measured in tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in a given minute. 
 
-Generating output tokens requires more processing than input tokens. For the models specified in the table below, 1 output token counts as 3 input tokens towards your TPM-per-PTU limit. The service dynamically balances the input & output costs, so users do not have to set specific input and output limits. This approach means your deployment is resilient to fluctuations in the workload.
 
-To help with simplifying the sizing effort, the following table outlines the TPM-per-PTU for the specified models. To understand the impact of output tokens on the TPM-per-PTU limit, use the 3 input token to 1 output token ratio. 
 
-For a detailed understanding of how different ratios of input and output tokens impact the throughput your workload needs, see the [Azure OpenAI capacity calculator](https://ai.azure.com/resource/calculator). The table also shows Service Level Agreement (SLA) Latency Target Values per model. For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
 
 
-|Topic| **gpt-4o**   | **gpt-4o-mini**  | **o1**|
-| --- | --- | --- | --- |
-|Global & data zone provisioned minimum deployment|15|15|15|
-|Global & data zone provisioned scale increment|5|5|5|
-|Regional provisioned minimum deployment|50|25|50|
-|Regional provisioned scale increment|50|25|50|
-|Input TPM per PTU |2,500|37,000|230|
-|Latency Target Value |25 Tokens Per Second|33 Tokens Per Second|25 Tokens Per Second|
+The amount of throughput (measured in tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in a given minute. Generating output tokens requires more processing than input tokens.  Starting with GPT 4.1 models and later, the system matches the global standard price ratio between input and output tokens. Cached tokens are deducted 100% from the utilization.
+
+For example, for `gpt-4.1:2025-04-14`, 1 output token counts as 4 input tokens towards your utilization limit which matches the [pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). Older models use a different ratio and for a deeper understanding on how different ratios of input and output tokens impact the throughput your workload needs, see the [Azure OpenAI capacity calculator](https://ai.azure.com/resource/calculator).
+
+
+|Topic| **gpt-4o**   | **gpt-4o-mini**  | **o1**| gpt-4.1 |
+| --- | --- | --- | --- | --- |
+|Global & data zone provisioned minimum deployment|15|15|15|15 |
+|Global & data zone provisioned scale increment|5|5|5| 5 | 
+|Regional provisioned minimum deployment|50|25|50| 50 |
+|Regional provisioned scale increment|50|25|50| 50 |
+|Input TPM per PTU |2,500|37,000|230| 3000 | 
+|Latency Target Value |25 Tokens Per Second|33 Tokens Per Second|25 Tokens Per Second| 44 Tokens Per Second |
 
 For a full list, see the [Azure OpenAI Service in Azure AI Foundry portal calculator](https://ai.azure.com/resource/calculator).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングスループットの説明とモデル情報の更新"
}
```

### Explanation
この変更は、「provisioned-throughput-onboarding.md」というファイルに対して行われ、Azure OpenAIサービスにおけるプロビジョニングスループットに関連する詳細が更新されました。主な変更点として、モデルごとのスループットに関する情報が明確にされ、特にGPT 4.1モデル以降の入力トークンと出力トークンの価格比に関する新しい情報が追加されています。

具体的には、出力トークンは使用量に対して4つの入力トークンとしてカウントされることが示されており、これによりシステム利用に関する透明性が向上しています。また、テーブルにGPT 4.1モデルの情報が追加され、各モデルごとの入力TPM（トークン毎分）やレイテンシターゲットの値も掲載されました。この変更により、ユーザーは各モデルの性能とサポートされているスループットについてより良い理解を得ることができるようになります。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -6,34 +6,34 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 03/31/2025
+ms.date: 05/01/2025
 ---
 
-| **Region**     | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
-| australiaeast      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| brazilsouth        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| canadaeast         | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus2            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| francecentral      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| italynorth         | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| japaneast          | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| koreacentral       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| northcentralus     | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| norwayeast         | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| polandcentral      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southafricanorth   | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southcentralus     | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southeastasia      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southindia         | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| spaincentral       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandnorth   | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandwest    | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| uaenorth           | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| uksouth            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westeurope         | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
+| **Region**     | **gpt-4.1**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:---------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
+| australiaeast      | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| brazilsouth        | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| canadaeast         | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus             | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus2            | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| italynorth         | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| japaneast          | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| koreacentral       | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| northcentralus     | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| norwayeast         | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southafricanorth   | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southcentralus     | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southeastasia      | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southindia         | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandnorth   | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandwest    | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| uaenorth           | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| uksouth            | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus             | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus3            | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニンググローバルリソースのデータ更新"
}
```

### Explanation
この変更は、「provisioned-global.md」というファイルに適用され、Azure OpenAIモデルに関するプロビジョニングの情報が更新されました。主な変更内容は、リソース使用可能地域のモデル対応状況に関するテーブルの内容がすべて更新されたことです。

具体的には、モデル列に新たにGPT 4.1が追加され、その利用可能な地域が明示されています。新しい日付（`ms.date`）も「2025年5月1日」に更新されており、情報の正確性が強化されています。これにより、ユーザーはさまざまな地域における異なるモデルの対応状況についての最新の情報を得ることができます。この更新は、Azure OpenAIサービスを利用する際の地域ごとのモデルの可用性をユーザーに迅速かつ明確に伝えるためのものです。


