---
date: '2025-01-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f3626a8...MicrosoftDocs:0fcd6d7
summary: 今回のドキュメント更新では、Azure OpenAIサービスに関する複数のドキュメントがマイナーアップデートされ、新しい「gpt-4o-realtime-preview」モデルが追加されました。このモデルはリアルタイムアプリケーションにフォーカスしており、音声処理に活用されます。文書の表現が整理され、モデルやデプロイ手順が明確化され、リージョンやプロビジョニングスループットに関する情報も簡潔化されました。特に、ドキュメントの更新に合わせて使用計画の見直しが推奨されています。全体として、ユーザーが最新機能をより活用できるよう、有益な情報が提供されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f3626a8...MicrosoftDocs:0fcd6d7){target="_blank"}

# ハイライト
今回のドキュメント更新では、Azure OpenAIサービスに関する複数のドキュメントがマイナーアップデートされ、新しいモデルの導入やモデル、リージョン、プロビジョニングスループット、制限、クイックスタートガイドの改善が含まれています。特に「gpt-4o-realtime-preview」モデルに関する情報が重点的に取り上げられています。

## 新機能
- 「gpt-4o-realtime-preview」モデルが新たに追加され、その利用可能性が具体的に明記されました。
- 品質向上のため、ドキュメントの表現が整理され、モデルの名称やデプロイ手順が明瞭化されました。

## 破壊的変更
- 明示的な破壊的変更はありませんが、ユーザーはドキュメントの更新に伴い、最新の情報に基づいてモデルの使用やデプロイ計画を見直す必要があります。

## その他の更新
- 新しいリージョンでのモデルサポートやプロビジョニングスループットの説明が簡潔化され、理解しやすくなりました。
- リアルタイムオーディオ機能における許可されたツールリストが拡張されました。

# インサイト
Azure OpenAIサービスのドキュメント更新は、主に新しいモデル「gpt-4o-realtime-preview」に焦点を当てています。このモデルは、音声処理などリアルタイムアプリケーションに活用されるもので、特に最新の2024年12月17日版が推奨されています。この新バージョンは、より効率的なリアルタイムオーディオインタラクションを可能とし、使用される地域も明確にされています（「East US 2」および「Sweden Central」）。

また、プロンプトキャッシュやプロビジョニングスループットに関する情報が更新され、ユーザーがモデルやスループットの管理をより効果的に行えるようになっています。具体的には、入力トークンと出力トークンの比率、ターゲットレイテンシー、サービスレベル契約についての情報がクリアになりました。これにより、ユーザーはより適切なスループットプランニングが可能です。

さらに、リアルタイムオーディオ機能では、許可されたツールに多様性が加わりました。「ash」「ballad」「coral」などの新しいツールが追加され、開発者はこれらを利用してオーディオ機能を拡充できます。

全体として、今回の更新は、ユーザーがAzure OpenAIの最新機能を活用しやすくするとともに、モデル選定や利用計画の際に有益な指針を提供するものです。特に、地域やバージョンに基づくモデルの可用性と、リアルタイムアプリケーションでの効率的なデプロイが強調されています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルのリタイアメントに関する最新情報の追加 | modified | 1 | 0 | 1 | 
| [models.md](#item-db2c37) | minor update | GPT-4oリアルタイムオーディオモデルに関する情報の更新 | modified | 5 | 4 | 9 | 
| [provisioned-throughput.md](#item-022e0c) | minor update | プロビジョニングスループットに関する情報の更新 | modified | 40 | 23 | 63 | 
| [prompt-caching.md](#item-1631df) | minor update | プロンプトキャッシュのサポートモデルに関する情報の更新 | modified | 8 | 7 | 15 | 
| [realtime-audio.md](#item-482ba3) | minor update | リアルタイムオーディオのサポートモデルの情報更新 | modified | 4 | 12 | 16 | 
| [global-batch-datazone.md](#item-94a58c) | minor update | 新しいリージョンがgpt-4oおよびgpt-4o-miniのサポートに追加 | modified | 10 | 6 | 16 | 
| [global-batch.md](#item-929e6a) | minor update | モデルのサポート情報が拡充 | modified | 14 | 14 | 28 | 
| [realtime-deploy-model.md](#item-21f911) | minor update | デプロイモデルのバージョン更新 | modified | 1 | 1 | 2 | 
| [quotas-limits.md](#item-06c6f9) | minor update | gpt-4oオーディオの制限に関する情報追加 | modified | 8 | 1 | 9 | 
| [realtime-audio-quickstart.md](#item-727df8) | minor update | リアルタイムオーディオモデルの情報更新 | modified | 4 | 5 | 9 | 
| [realtime-audio-reference.md](#item-276d51) | minor update | リアルタイムオーディオツールの許可された値の追加 | modified | 8 | 2 | 10 | 
| [whats-new.md](#item-53303b) | minor update | Azure OpenAIサービスの最新情報の更新 | modified | 15 | 3 | 18 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -107,6 +107,7 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-4` | vision-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025  **<sup>1</sup>** | `gpt-4o`|
 | `gpt-4o` | 2024-05-13 | No earlier than May 20, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on February 13, 2025. | |
 | `gpt-4o-mini` | 2024-07-18 | No earlier than July 18, 2025  | |
+| `gpt-4o-realtime-preview` | 2024-10-01 | No earlier than September 30, 2025  | `gpt-4o-realtime-preview` (version 2024-12-17) |
 | `gpt-3.5-turbo-instruct` | 0914 | No earlier than April 1, 2025 |  |
 | `o1` | 2024-12-17 | No earlier than December 17, 2025 | |
 | `text-embedding-ada-002` | 2 | No earlier than October 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのリタイアメントに関する最新情報の追加"
}
```

### Explanation
このコードの差分では、Azure OpenAIサービスにおける利用可能なモデルのリストに新しいエントリとして「`gpt-4o-realtime-preview`」モデルが追加されました。この変更により、`gpt-4o-realtime-preview`モデルは2024年10月1日に利用可能となり、2025年9月30日以降に使用可能となる旨が明記されています。このような情報更新は、ユーザーがモデルの利用可能性と将来の予定を理解するのに役立ちます。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -58,17 +58,18 @@ To learn more about the advanced `o1` series models see, [getting started with o
 
 ## GPT-4o-Realtime-Preview
 
-The `gpt-4o-realtime-preview` model is part of the GPT-4o model family and supports low-latency, "speech in, speech out" conversational interactions. GPT-4o audio is designed to handle real-time, low-latency conversational interactions, making it a great fit for support agents, assistants, translators, and other use cases that need highly responsive back-and-forth with a user.
+The GPT 4o audio models are part of the GPT-4o model family and support low-latency, "speech in, speech out" conversational interactions. GPT-4o audio is designed to handle real-time, low-latency conversational interactions, making it a great fit for support agents, assistants, translators, and other use cases that need highly responsive back-and-forth with a user.
 
 GPT-4o audio is available in the East US 2 (`eastus2`) and Sweden Central (`swedencentral`) regions. To use GPT-4o audio, you need to [create](../how-to/create-resource.md) or use an existing resource in one of the supported regions.
 
-When your resource is created, you can [deploy](../how-to/create-resource.md#deploy-a-model) the GPT-4o audio model. If you are performing a programmatic deployment, the **model** name is `gpt-4o-realtime-preview`. For more information on how to use GPT-4o audio, see the [GPT-4o audio documentation](../realtime-audio-quickstart.md).
+When your resource is created, you can [deploy](../how-to/create-resource.md#deploy-a-model) the GPT-4o audio model. For more information on how to use GPT-4o audio, see the [GPT-4o audio quickstart](../realtime-audio-quickstart.md) and [how to use GPT-4o audio](../how-to/realtime-audio.md).
 
 Details about maximum request tokens and training data are available in the following table.
 
 |  Model ID  | Description | Max Request (tokens) | Training Data (up to)  |
-|  --- |  :--- |:--- |:---: |
-|`gpt-4o-realtime-preview` (2024-10-01-preview) <br> **GPT-4o audio** | **Audio model** for real-time audio processing |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
+|---|---|---|---|
+|`gpt-4o-realtime-preview` (2024-10-01) <br> **GPT-4o audio** | **Audio model** for real-time audio processing |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
+|`gpt-4o-realtime-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for real-time audio processing |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
 
 ## GPT-4o and GPT-4 Turbo
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4oリアルタイムオーディオモデルに関する情報の更新"
}
```

### Explanation
このコードの差分では、GPT-4oモデルファミリーに関する情報が更新され、特に「`gpt-4o-realtime-preview`」オーディオモデルに関する説明が明確化されました。具体的には、モデル名称の表記が統一され、より具体的な情報が提供されるように改善されています。また、モデルに関するリソースの展開手順が簡略化され、関連するリンクも追加されました。これにより、ユーザーはGPT-4oオーディオモデルの使用に関する理解を深めやすくなっています。さらに、モデルのバージョンについての情報も更新され、同モデルのリリース日が明記されています。

## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -30,35 +30,34 @@ An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model.
 
 | Topic | Provisioned|
 |---|---|
-| What is it? | Provides guaranteed throughput at smaller increments than the existing provisioned offer. Deployments have a consistent max latency for a given model-version. |
+| What is it? |Provides guaranteed throughput at smaller increments than the existing provisioned offer. Deployments have a consistent max latency for a given model-version. |
 | Who is it for? | Customers who want guaranteed throughput with minimal latency variance. |
 | Quota |Provisioned Managed Throughput Unit, Global Provisioned Managed Throughput Unit, or Data Zone Provisioned Managed Throughput Unit assigned per region. Quota can be used across any available Azure OpenAI model.|
 | Latency | Max latency constrained from the model. Overall latency is a factor of call shape.  |
 | Utilization | Provisioned-managed Utilization V2 measure provided in Azure Monitor. |
-| Estimating size | Provided calculator in Azure AI Foundry & benchmarking script. |
+|Estimating size |Provided sizing calculator in Azure AI Foundry.|
 |Prompt caching | For supported models, we discount up to 100% of cached input tokens. |
 
 
 ## How much throughput per PTU you get for each model
-The amount of throughput (tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in the minute. Generating output tokens requires more processing than input tokens and so the more output tokens generated the lower your overall TPM. The service dynamically balances the input & output costs, so users do not have to set specific input and output limits. This approach means your deployment is resilient to fluctuations in the workload shape.
+The amount of throughput (tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in the minute. Generating output tokens requires more processing than input tokens. For the models specified in the table below, 1 output token counts as 3 input tokens towards your TPM per PTU limit. The service dynamically balances the input & output costs, so users do not have to set specific input and output limits. This approach means your deployment is resilient to fluctuations in the workload shape.
 
-To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the `gpt-4o` and `gpt-4o-mini` models which represent the max TPM assuming all traffic is either input or output. To understand how different ratios of input and output tokens impact your Max TPM per PTU, see the [Azure OpenAI capacity calculator](https://oai.azure.com/portal/calculator). The table also shows Service Level Agreement (SLA) Latency Target Values per model.  For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
+To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the specified models. To understand the impact of output tokens on the TPM per PTU limit, use the 3 input token to 1 output token ratio. For a detailed understanding of how different ratios of input and output tokens impact the throughput your workload needs, see the [Azure OpenAI capacity calculator](https://oai.azure.com/portal/calculator). The table also shows Service Level Agreement (SLA) Latency Target Values per model.  For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
 
-|Topic| **gpt-4o**, **2024-05-13**   & **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
+|Topic| **gpt-4o**   | **gpt-4o-mini**   |
 | --- | --- | --- |
 |Global & data zone provisioned minimum deployment|15|15|
 |Global & data zone provisioned scale increment|5|5|
 |Regional provisioned minimum deployment | 50 | 25|
 |Regional provisioned scale increment|50|25|
-|Max Input TPM per PTU | 2,500 | 37,000  |
-|Max Output TPM per PTU| 833|12,333|
+|Input TPM per PTU | 2,500 | 37,000  |
 |Latency Target Value |25 Tokens Per Second|33 Tokens Per Second|
 
 For a full list see the [Azure OpenAI Service in Azure AI Foundry portal calculator](https://oai.azure.com/portal/calculator).
 
 
 > [!NOTE]
-> Global provisioned deployments are only supported for gpt-4o, 2024-08-06 and gpt-4o-mini, 2024-07-18 models at this time. Data zone provisioned deployments are only supported for gpt-4o, 2024-08-06, gpt-4o, 2024-05-13, and gpt-4o-mini, 2024-07-18 models at this time. For more information on model availability, review the [models documentation](./models.md).
+> Global provisioned and data zone provisioned deployments are only supported for gpt-4o and gpt-4o-mini models at this time. For more information on model availability, review the [models documentation](./models.md).
 
 ## Key concepts
 
@@ -73,11 +72,11 @@ az cognitiveservices account deployment create \
 --name <myResourceName> \
 --resource-group  <myResourceGroupName> \
 --deployment-name MyDeployment \
---model-name gpt-4 \
---model-version 0613  \
+--model-name gpt-4o \
+--model-version 2024-08-06  \
 --model-format OpenAI \
---sku-capacity 100 \
---sku-name ProvisionedManaged
+--sku-capacity 15 \
+--sku-name GlobalProvisionedManaged
 ```
 
 ### Quota
@@ -132,7 +131,7 @@ If an acceptable region isn't available to support the desire model, version and
 
 ### Determining the number of PTUs needed for a workload
 
-PTUs represent an amount of model processing capacity. Similar to your computer or databases, different workloads or requests to the model will consume different amounts of underlying processing capacity. The conversion from call shape characteristics (prompt size, generation size and call rate) to PTUs is complex and nonlinear. To simplify this process, you can use the [Azure OpenAI Capacity calculator](https://oai.azure.com/portal/calculator) to size specific workload shapes.
+PTUs represent an amount of model processing capacity. Similar to your computer or databases, different workloads or requests to the model will consume different amounts of underlying processing capacity. The conversion from throughput needs to PTUs can be approximated using historical token usage data or call shape estimations (input tokens, output tokens, and requests per minute) as outlined in our [performance and latency](../how-to/latency.md) documentation. To simplify this process, you can use the [Azure OpenAI Capacity calculator](https://oai.azure.com/portal/calculator) to size specific workload shapes.
 
 A few high-level considerations:
 - Generations require more capacity than prompts
@@ -165,16 +164,16 @@ For provisioned deployments, we use a variation of the leaky bucket algorithm to
 1. When a request is made:
 
     a.    When the current utilization is above 100%, the service returns a 429 code with the `retry-after-ms` header set to the time until utilization is below 100%
+   
+    b.    Otherwise, the service estimates the incremental change to utilization required to serve the request by combining the prompt tokens, less any cacehd tokens, and the specified `max_tokens` in the call. A customer can receive up to a 100% discount on their prompt tokens depending on the size of their cached tokens. If the `max_tokens` parameter is not specified, the service estimates a value. This estimation can lead to lower concurrency than expected when the number of actual generated tokens is small.  For highest concurrency, ensure that the `max_tokens` value is as close as possible to the true generation size.
+   
+1. When a request finishes, we now know the actual compute cost for the call. To ensure an accurate accounting, we correct the utilization using the following logic:
 
-    b.    Otherwise, the service estimates the incremental change to utilization required to serve the request by combining prompt tokens and the specified `max_tokens` in the call. For requests that include at least 1024 cached tokens, the cached tokens are subtracted from the prompt token value. A customer can receive up to a 100% discount on their prompt tokens depending on the size of their cached tokens. If the `max_tokens` parameter is not specified, the service estimates a value. This estimation can lead to lower concurrency than expected when the number of actual generated tokens is small.  For highest concurrency, ensure that the `max_tokens` value is as close as possible to the true generation size.
-
-1.  When a request finishes, we now know the actual compute cost for the call. To ensure an accurate accounting, we correct the utilization using the following logic:
-
-    a.    If the actual > estimated, then the difference is added to the deployment's utilization.
-
-    b.    If the actual < estimated, then the difference is subtracted.
-
-1.  The overall utilization is decremented down at a continuous rate based on the number of PTUs deployed. 
+   a.    If the actual > estimated, then the difference is added to the deployment's utilization.
+   
+   b.    If the actual < estimated, then the difference is subtracted.
+   
+1. The overall utilization is decremented down at a continuous rate based on the number of PTUs deployed. 
 
 > [!NOTE]
 > Calls are accepted until utilization reaches 100%. Bursts just over 100% may be permitted in short periods, but over time, your traffic is capped at 100% utilization.
@@ -184,12 +183,30 @@ For provisioned deployments, we use a variation of the leaky bucket algorithm to
 
 #### How many concurrent calls can I have on my deployment?
 
-The number of concurrent calls you can achieve depends on each call's shape (prompt size, max_token parameter, etc.). The service continues to accept calls until the utilization reach 100%. To determine the approximate number of concurrent calls, you can model out the maximum requests per minute for a particular call shape in the [capacity calculator](https://oai.azure.com/portal/calculator). If the system generates less than the number of samplings tokens like max_token, it will accept more requests.
+The number of concurrent calls you can achieve depends on each call's shape (prompt size, `max_tokens` parameter, etc.). The service continues to accept calls until the utilization reaches 100%. To determine the approximate number of concurrent calls, you can model out the maximum requests per minute for a particular call shape in the [capacity calculator](https://oai.azure.com/portal/calculator). If the system generates less than the number of output tokens set for the `max_tokens` parameter, then the provisioned deployment will accept more requests.
 
 ## What models and regions are available for provisioned throughput?
 
+# [Global Provisioned Managed](#tab/global-ptum)
+
+### Global provisioned managed model availability
+
+[!INCLUDE [Provisioned Managed Global](../includes/model-matrix/provisioned-global.md)]
+
+# [Data Zone Provisioned Managed](#tab/datazone-provisioned-managed)
+
+### Data zone provisioned managed model availability
+
+[!INCLUDE [Global data zone provisioned managed](../includes/model-matrix/datazone-provisioned-managed.md)]
+
+# [Provisioned Managed](#tab/provisioned)
+
+### Provisioned deployment model availability
+
 [!INCLUDE [Provisioned](../includes/model-matrix/provisioned-models.md)]
 
+---
+
 > [!NOTE]
 > The provisioned version of `gpt-4` **Version:** `turbo-2024-04-09` is currently limited to text only.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングスループットに関する情報の更新"
}
```

### Explanation
このコードの差分では、Azure OpenAIサービスにおけるプロビジョニングスループットに関するドキュメントが更新されました。新たに40行が追加され、23行が削除されることにより、情報が整理され、明確性が向上しています。主な変更点としては、情報の表現方法が簡素化され、特定のモデルとそのスループットに関する具体的な数値が提供されています。加えて、入力トークンと出力トークンの比率についての説明がより明確になり、ユーザーはモデルの利用に関する詳細な知識を持つことができるようになっています。ターゲットレイテンシーやサービスレベル契約についても追記され、利用者がプロビジョニングスループットを正確に計画できるような情報が提供されています。これにより、ユーザーは処理能力や使用モデルの選定において、より適切な選択ができるようになります。

## articles/ai-services/openai/how-to/prompt-caching.md{#item-1631df}

<details>
<summary>Diff</summary>
````diff
@@ -28,6 +28,7 @@ Currently only the following models support prompt caching with Azure OpenAI:
 - `gpt-4o-2024-11-20`
 - `gpt-4o-2024-08-06`
 - `gpt-4o-mini-2024-07-18`
+- `gpt-4o-realtime-preview` (version 2024-12-17)`
 
 > [!NOTE]
 > Prompt caching is now also available as part of model fine-tuning for `gpt-4o` and `gpt-4o-mini`. Refer to the fine-tuning section of the [pricing page](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) for details.
@@ -76,14 +77,14 @@ A single character difference in the first 1,024 tokens will result in a cache m
 
 The o1-series models are text only and don't support system messages, images, tool use/function calling, or structured outputs. This limits the efficacy of prompt caching for these models to the user/assistant portions of the messages array which are less likely to have an identical 1024 token prefix.
 
-For `gpt-4o` and `gpt-4o-mini` models, prompt caching is supported for:  
+Prompt caching is supported for:
 
-| **Caching Supported** | **Description** |
-|--------|--------|
-|**Messages** | The complete messages array: system, user, and assistant content |
-|**Images** | Images included in user messages, both as links or as base64-encoded data. The detail parameter must be set the same across requests.
-|**Tool use**| Both the messages array and tool definitions |
-|**Structured outputs** | Structured output schema is appended as a prefix to the system message|
+|**Caching supported**|**Description**|**Supported models**|
+|--------|--------|--------|
+| **Messages** | The complete messages array: system, user, and assistant content | `gpt-4o`<br/>`gpt-4o-mini`<br/>`gpt-4o-realtime-preview` (version 2024-12-17) |
+| **Images** | Images included in user messages, both as links or as base64-encoded data. The detail parameter must be set the same across requests. | `gpt-4o`<br/>`gpt-4o-mini` |
+| **Tool use** | Both the messages array and tool definitions. | `gpt-4o`<br/>`gpt-4o-mini`<br/>`gpt-4o-realtime-preview` (version 2024-12-17) |
+| **Structured outputs** | Structured output schema is appended as a prefix to the system message. | `gpt-4o`<br/>`gpt-4o-mini` |
 
 To improve the likelihood of cache hits occurring, you should structure your requests such that repetitive content occurs at the beginning of the messages array.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトキャッシュのサポートモデルに関する情報の更新"
}
```

### Explanation
このコードの差分では、Azure OpenAIにおけるプロンプトキャッシュに関する情報が更新されました。新たにいくつかのモデルがプロンプトキャッシュのサポート対象として追加され、特に「`gpt-4o-realtime-preview`（バージョン2024-12-17）」が加わりました。これにより、ユーザーは新たにこのモデルもプロンプトキャッシュの機能を利用できるようになります。

また、プロンプトキャッシュの詳細についても整理され、各モデルでサポートされる機能がわかりやすく示されています。特に、キャッシュがサポートされるメッセージや画像、ツールの使用、構造化出力についての情報が明確に記載されています。この改訂により、ユーザーは利用可能なモデルとそれぞれのキャッシュ機能について一層理解を深めやすくなっています。

## articles/ai-services/openai/how-to/realtime-audio.md{#item-482ba3}

<details>
<summary>Diff</summary>
````diff
@@ -22,19 +22,11 @@ Most users of the Realtime API need to deliver and receive audio from an end-use
 
 ## Supported models
 
-Currently only `gpt-4o-realtime-preview` version: `2024-10-01-preview` supports real-time audio.
+The GPT 4o realtime models are available for global deployments in [East US 2 and Sweden Central regions](../concepts/models.md#global-standard-model-availability).
+- `gpt-4o-realtime-preview` (2024-12-17)
+- `gpt-4o-realtime-preview` (2024-10-01)
 
-The `gpt-4o-realtime-preview` model is available for global deployments in [East US 2 and Sweden Central regions](../concepts/models.md#global-standard-model-availability).
-
-> [!IMPORTANT]
-> The system stores your prompts and completions as described in the "Data Use and Access for Abuse Monitoring" section of the service-specific Product Terms for Azure OpenAI Service, except that the Limited Exception does not apply. Abuse monitoring will be turned on for use of the `gpt-4o-realtime-preview` API even for customers who otherwise are approved for modified abuse monitoring.
-
-## API support
-
-Support for the Realtime API was first added in API version `2024-10-01-preview`. 
-
-> [!NOTE]
-> For more information about the API and architecture, see the [Azure OpenAI GPT-4o real-time audio repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk).
+See the [models and versions documentation](../concepts/models.md#gpt-4o-realtime-preview) for more information.
 
 ## Get started
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオのサポートモデルの情報更新"
}
```

### Explanation
このコードの差分では、Azure OpenAIにおけるリアルタイムオーディオのサポートモデルに関する情報が更新されました。主な変更点として、リアルタイムオーディオ機能が利用可能なモデルが明確に示され、特に「`gpt-4o-realtime-preview`」の二つのバージョン（2024-12-17および2024-10-01）が追加されました。これにより、ユーザーはサポートされている特定のモデルを容易に理解できるようになっています。

さらに、モデルの展開地域に関する情報も整理され、「East US 2」と「Sweden Central」のグローバルデプロイメントがサポートされていることが強調されています。また、APIのバージョンに関する説明が簡潔に改訂され、リアルタイムAPIの利用開始に関する情報提供が改善されています。

これらの変更により、ユーザーはリアルタイムオーディオを利用する際のモデルとバージョンに関する情報をより明確に把握できるようになっています。

## articles/ai-services/openai/includes/model-matrix/global-batch-datazone.md{#item-94a58c}

<details>
<summary>Diff</summary>
````diff
@@ -10,9 +10,13 @@ ms.date: 01/14/2025
 ---
 
 
-| **Region**         |  **gpt-4o**, **2024-08-06**| **gpt-4o-mini**, **2024-07-18**  |
-|:-------------------|:--------------------------:|:--------------------------:|
-| eastus             | ✅                       | ✅                          |  
-| germanywestcentral | ✅                       | ✅                          |
-| swedencentral      | ✅                       | ✅                          |  
-| westus             | ✅                       | ✅                          |  
+| **Region**     | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:--------------------------:|:-------------------------------:|
+| eastus             | ✅                       | ✅                            |
+| eastus2            | ✅                       | ✅                            |
+| germanywestcentral | ✅                       | ✅                            |
+| southcentralus     | ✅                       | ✅                            |
+| swedencentral      | ✅                       | ✅                            |
+| westeurope         | ✅                       | ✅                            |
+| westus             | ✅                       | ✅                            |
+| westus3            | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいリージョンがgpt-4oおよびgpt-4o-miniのサポートに追加"
}
```

### Explanation
このコードの差分では、Azure OpenAIのモデルマトリックスにおいて、新しいリージョンが「gpt-4o」と「gpt-4o-mini」のサポート対象として追加されました。具体的には、「eastus2」、「southcentralus」、「westeurope」、および「westus3」といった地域が新たにテーブルに追加されており、それぞれのモデルがこれらのリージョンで利用可能であることが示されています。

また、表の構成が整理され、視覚的に情報がわかりやすくなっています。この変更により、ユーザーは利用可能なリージョンを容易に把握できるようになり、特定のモデルをどの地域で使用できるかについての理解が深まります。

## articles/ai-services/openai/includes/model-matrix/global-batch.md{#item-929e6a}

<details>
<summary>Diff</summary>
````diff
@@ -11,24 +11,24 @@ ms.date: 01/15/2025
 
 | **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
 |:-------------------|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
-| australiaeast      | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| brazilsouth        | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| canadaeast         | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| australiaeast      | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| brazilsouth        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| canadaeast         | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | eastus             | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | eastus2            | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | francecentral      | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| germanywestcentral | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| japaneast          | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| koreacentral       | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| northcentralus     | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| norwayeast         | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| polandcentral      | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southafricanorth   | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| germanywestcentral | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| japaneast          | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| koreacentral       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| northcentralus     | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| norwayeast         | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| polandcentral      | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southafricanorth   | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | southcentralus     | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southindia         | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southindia         | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | swedencentral      | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| switzerlandnorth   | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| uksouth            | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| switzerlandnorth   | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| uksouth            | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | westeurope         | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | westus             | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westus3            | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westus3            | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのサポート情報が拡充"
}
```

### Explanation
このコードの差分では、Azure OpenAIのモデルマトリックスにおけるサポート情報が拡充されました。具体的には、各モデルが利用可能なリージョンに関して、いくつかの変更が行われています。新たに、さまざまな地域で「gpt-4o」と「gpt-4o-mini」を含むモデルのサポート状況が追加されました。

主な変更点は、従来は「-」で示されていたモデルサポートが、全ての該当リージョンにおいて「✅」に更新され、利用可能性が確認されました。例えば、「australiaeast」、「brazilsouth」、「canadaeast」などの地域において、全てのバージョンのモデルが利用可能になっています。

この更新により、ユーザーはより多くの地域で対応しているモデルを利用できることを理解しやすくなり、特に選ばれた地域でのモデルの利用可能性が向上しています。全体として、ドキュメントが整理され、ユーザーへの情報提供が改善されています。

## articles/ai-services/openai/includes/realtime-deploy-model.md{#item-21f911}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ To deploy the `gpt-4o-realtime-preview` model in the Azure AI Foundry portal:
 1. Select the **Real-time audio** playground from under **Playgrounds** in the left pane.
 1. Select **Create new deployment** to open the deployment window. 
 1. Search for and select the `gpt-4o-realtime-preview` model and then select **Confirm**.
-1. In the deployment wizard, make sure to select the `2024-10-01` model version.
+1. In the deployment wizard, select the `2024-12-17` model version.
 1. Follow the wizard to finish deploying the model.
 
 Now that you have a deployment of the `gpt-4o-realtime-preview` model, you can interact with it in real time in the Azure AI Foundry portal **Real-time audio** playground or Realtime API.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイモデルのバージョン更新"
}
```

### Explanation
このコードの差分では、Azure AI Foundryにおける「gpt-4o-realtime-preview」モデルのデプロイ手順の一部が更新されました。具体的には、デプロイウィザードで選択するモデルのバージョンが「2024-10-01」から「2024-12-17」に変更されました。

この更新は、最新のモデルバージョンを使用することを促進し、ユーザーが新機能や改善点を活用できるようにする目的があります。手順自体はほぼ同じですが、バージョン番号の変更により、ユーザーが正しいバージョンを選択できることが重要です。この修正により、リアルタイムオーディオプレイグラウンドやリアルタイムAPIでの相互作用が向上することが期待されます。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -51,7 +51,6 @@ The following sections provide you with a quick guide to the default quotas and
 | GPT-4o max images per request (# of images in the messages array/conversation history) | 50 |
 | GPT-4 `vision-preview` & GPT-4 `turbo-2024-04-09` default max tokens | 16 <br><br> Increase the `max_tokens` parameter value to avoid truncated responses. GPT-4o max tokens defaults to 4096. |
 | Max number of custom headers in API requests<sup>1</sup> | 10 |
-| Max number requests per minute<br/><br/>Current rate limits for real time audio (`gpt-4o-realtime-preview`) are defined as the number of new websocket connections per minute. For example, 100 requests per minute (RPM) means 100 new connections per minute. | 100 new connections per minute |
 
 <sup>1</sup> Our current APIs allow up to 10 custom headers, which are passed through the pipeline, and returned. Some customers now exceed this header count resulting in HTTP 431 errors. There's no solution for this error, other than to reduce header volume. **In future API versions we will no longer pass through custom headers**. We recommend customers not depend on custom headers in future system architectures.
 
@@ -132,6 +131,14 @@ M = million | K = thousand
 
 M = million | K = thousand
 
+## gpt-4o audio
+
+| Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
+|---|---|:---:|:---:|
+|`gpt-4o-realtime-preview` | Default | 100 K | 1 K |
+
+M = million | K = thousand
+
 #### Usage tiers
 
 Global standard deployments use Azure's global infrastructure, dynamically routing customer traffic to the data center with best availability for the customer’s inference requests. Similarly, Data zone standard deployments allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. This enables more consistent latency for customers with low to medium levels of traffic. Customers with high sustained levels of usage might see greater variability in response latency.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "gpt-4oオーディオの制限に関する情報追加"
}
```

### Explanation
このコードの差分では、OpenAIの「クォータと制限」に関するドキュメントが更新され、新たに「gpt-4o」モデルに関連するオーディオの制限についての情報が追加されました。具体的には、「gpt-4o-realtime-preview」モデルに対する制限がテーブル形式で示され、分かりやすくなっています。

新たに追加されたテーブルでは、モデルのティア、トークンごとの制限（TPM）、およびリクエスト数（RPM）が明確に記載されています。例えば、「gpt-4o-realtime-preview」モデルは、デフォルトで100Kトークン/分の制限と1Kリクエスト/分の制限があります。

また、既存の内容の一部が削除されたことで、ドキュメントがよりシンプルかつ明瞭になっています。これにより、ユーザーはリアルタイムオーディオ処理における制限をより簡単に理解できるようになり、システムのパフォーマンスを効果的に管理できることが期待されます。この更新は、特に開発者にとって重要な情報となるでしょう。

## articles/ai-services/openai/realtime-audio-quickstart.md{#item-727df8}

<details>
<summary>Diff</summary>
````diff
@@ -23,12 +23,11 @@ Most users of the Realtime API need to deliver and receive audio from an end-use
 
 ## Supported models
 
-Currently only `gpt-4o-realtime-preview` version: `2024-10-01-preview` supports real-time audio.
+The GPT 4o realtime models are available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability).
+- `gpt-4o-realtime-preview` (2024-12-17)
+- `gpt-4o-realtime-preview` (2024-10-01)
 
-The `gpt-4o-realtime-preview` model is available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability).
-
-> [!IMPORTANT]
-> The system stores your prompts and completions as described in the "Data Use and Access for Abuse Monitoring" section of the service-specific Product Terms for Azure OpenAI Service, except that the Limited Exception does not apply. Abuse monitoring will be turned on for use of the `gpt-4o-realtime-preview` API even for customers who otherwise are approved for modified abuse monitoring.
+See the [models and versions documentation](./concepts/models.md#gpt-4o-realtime-preview) for more information.
 
 ## API support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオモデルの情報更新"
}
```

### Explanation
このコードの差分では、リアルタイムオーディオAPIに関するクイックスタートガイドが更新され、サポートされているモデルに関する情報が追加されました。具体的には、既存の内容が整理され、現在利用可能な「gpt-4o-realtime-preview」モデルのバージョンが明確に示されています。

新しい情報では、現在サポートされているモデルとして、2024年12月17日版と2024年10月1日版の「gpt-4o-realtime-preview」がリストされています。また、これらのモデルがどの地域で利用可能か（「East US 2」と「Sweden Central」）についても記載があり、ユーザーが利用可能なリソースをより理解しやすくなっています。

さらに、重要な注意事項に関する情報が簡素化され、プロンプトや完了内容のデータ使用に関するセクションが参照されるようになりました。この変更により、ユーザーはモデルの使用に際して必要な情報を迅速に見つけることができるようになり、全体的なユーザー体験が向上することが期待されます。

## articles/ai-services/openai/realtime-audio-reference.md{#item-276d51}

<details>
<summary>Diff</summary>
````diff
@@ -1508,8 +1508,14 @@ Currently, only 'function' tools are supported.
 **Allowed Values:**
 
 * `alloy` 
-* `shimmer` 
-* `echo` 
+* `ash`
+* `ballad`
+* `coral`
+* `echo`
+* `sage`
+* `shimmer`
+* `verse`
+ 
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオツールの許可された値の追加"
}
```

### Explanation
このコードの差分では、リアルタイムオーディオリファレンス文書が更新され、サポートされる「機能」ツールに関するリストが拡張されました。具体的には、以前は「shimmer」しかリストされていなかった許可された値に対して、新たに「ash」「ballad」「coral」「echo」「sage」「shimmer」「verse」が追加されました。

この変更により、ユーザーはリアルタイムオーディオ機能で使用できるツールの選択肢をより広範に理解できるようになります。特に、これらのツールはオーディオ処理や生成に関連するものであり、開発者やエンジニアが自分のプロジェクトに最適なツールを選択するのに役立つ情報となるでしょう。この更新は、ユーザーの利便性を向上させ、より多様なオーディオ処理のニーズに対応できるように設計されています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -11,14 +11,26 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: whats-new
-ms.date: 11/18/2024
+ms.date: 1/15/2025
 recommendations: false
 ---
 
 # What's new in Azure OpenAI Service
 
 This article provides a summary of the latest releases and major documentation updates for Azure OpenAI.
 
+## January 2025
+
+### GPT-4o Realtime API 2024-12-17
+
+The `gpt-4o-realtime-preview` model version 2024-12-17 is available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability). Use the `gpt-4o-realtime-preview` version 2024-12-17 model instead of the `gpt-4o-realtime-preview` version 2024-10-01-preview model for real-time audio interactions.
+
+- Added support for [prompt caching](./how-to/prompt-caching.md) with the `gpt-4o-realtime-preview` model.
+- Added support for new voices. The `gpt-4o-realtime-preview` models now support the following voices: "alloy", "ash", "ballad", "coral", "echo", "sage", "shimmer", "verse".
+- Rate limits are no longer based on connections per minute. Rate limiting is now based on RPM (requests per minute) and TPM (tokens per minute) for the `gpt-4o-realtime-preview` model. The rate limits for the `gpt-4o-realtime-preview` model are 100K TPM and 1K RPM.
+
+For more information, see the [GPT-4o real-time audio quickstart](realtime-audio-quickstart.md) and the [how-to guide](./how-to/realtime-audio.md).
+
 ## December 2024
 
 ### o1 reasoning model released for limited access
@@ -77,7 +89,7 @@ For fine-tuning model region availability, see the [models page](./concepts/mode
 
 We are introducing new forms of abuse monitoring that leverage LLMs to improve efficiency of detection of potentially abusive use of the Azure OpenAI service and to enable abuse monitoring without the need for human review of prompts and completions. Learn more, see [Abuse monitoring](/azure/ai-services/openai/concepts/abuse-monitoring).
 
-Prompts and completions that are flagged through content classification and/or identified to be part of a potentially abusive pattern of use are subjected to an additional review process to help confirm the system’s analysis and inform actioning decisions. Our abuse monitoring systems have been expanded to enable review by LLM by default and by humans when necessary and appropriate. 
+Prompts and completions that are flagged through content classification and/or identified to be part of a potentially abusive pattern of use are subjected to an additional review process to help confirm the system's analysis and inform actioning decisions. Our abuse monitoring systems have been expanded to enable review by LLM by default and by humans when necessary and appropriate. 
 
 ## October 2024
 
@@ -135,7 +147,7 @@ Azure OpenAI GPT-4o audio is part of the GPT-4o model family that supports low-l
 
 The `gpt-4o-realtime-preview` model is available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability).
 
-For more information, see the [GPT-4o real-time audio documentation](realtime-audio-quickstart.md).
+For more information, see the [GPT-4o real-time audio quickstart](realtime-audio-quickstart.md).
 
 ### Global batch support updates
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスの最新情報の更新"
}
```

### Explanation
このコードの差分では、Azure OpenAIサービスに関する最新情報の文書が更新され、2025年1月の新機能や変更点が追加されました。主な変更内容は以下の通りです。

- **日付の更新**: マニュアルの最終更新日が2024年11月18日から2025年1月15日に変更されました。
- **GPT-4oリアルタイムAPIの新バージョン**: 「gpt-4o-realtime-preview」モデルの2024年12月17日版がグローバルに展開可能であることが記されています。この新バージョンは、リアルタイムオーディオインタラクション用に推奨されています。
- **新機能の追加**: プロンプトキャッシングのサポートや新しい音声のサポートが加わりました。特に、新しい音声として「alloy」「ash」「ballad」「coral」「echo」「sage」「shimmer」「verse」がリストされています。
- **レート制限の見直し**: リアルタイムモデルにおけるレート制限が、接続数からRPM（リクエスト毎分）およびTPM（トークン毎分）に変更され、具体的な制限値も示されています。

これらの更新により、ユーザーは新しい機能やモデルの使用に関する最新情報を手に入れることができ、効率的かつ効果的にAzure OpenAIサービスを利用できるようになります。さらに、関連するクイックスタートやハウツーガイドへのリンクも提供され、より詳細な情報に迅速にアクセス可能となっています。


