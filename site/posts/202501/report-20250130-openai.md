---
date: '2025-01-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b5fac8b...MicrosoftDocs:62147e0
summary: このコード差分には、Azure AI FoundryおよびOpenAIサービスに関する重要な更新が含まれています。特に、コンテンツフィルターのデフォルト設定が「オフ」から「オン」に変更され、新たに「予測出力」機能に関するドキュメントが追加されました。また、APIやモデルのリリース日および地域情報の更新も行われています。これらの変更は、セキュリティと応答速度を向上させることを目的としており、ユーザーにより良い体験を提供します。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b5fac8b...MicrosoftDocs:62147e0){target="_blank"}

# ハイライト
このコード差分には、Azure AI FoundryおよびOpenAIサービスに関するドキュメントの主要な更新が含まれています。注目すべき点は、コンテンツフィルターのデフォルト設定の変更、新たに追加された「予測出力」機能のドキュメント、およびいくつかのAPIやモデルに関する日付および地域情報の更新です。

## 新機能
- Azure OpenAIサービスに「予測出力」機能のドキュメントが追加され、テキストのレスポンスレイテンシを改善する方法が説明されています。

## ブレイキングチェンジ
特にブレイキングチェンジは報告されていませんが、コンテンツフィルターのデフォルト設定の変更は、ユーザー設定を変更せずに影響を与える可能性があるため、注意が必要です。

## その他の更新
- コンテンツフィルターのデフォルトが「オフ」から「オン」に変更。
- 新しいAPIおよびモデルのリリース日と対応地域に関する更新。
- Azure OpenAIの最新のAPIバージョンとドキュメントの日付更新。
- 目次に「Predicted outputs」に関する項目が追加。

# 洞察
このコード差分は、Azure AIとOpenAIサービスの機能とドキュメントを最新情報に保つための重要な更新を含んでいます。まず、コンテンツフィルターのデフォルト設定が「オン」に変わったことで、セキュリティと使用の自動保護レベルが向上しています。特に、Jailbreakリスク検出機能は多くのユーザーにとって安心感を提供する改良といえるでしょう。

新たに追加された「予測出力」機能は、モデルの応答速度を重要視するアプリケーションでのパフォーマンス改善を目指しています。この機能は、リアルタイムまたは即応性が求められるシナリオでのレスポンス向上に寄与し、開発者に新たなツールとガイドラインを提供します。

APIやモデルのリリース日更新は、開発者が最新の仕様と機能をもとにシステムを設計・構築するために必須の情報であり、これにより一貫したユーザーエクスペリエンスとシステムの安定性が確保されます。また、目次の更新は、必要な情報の迅速なアクセスを可能にし、ユーザーエクスペリエンス全体を向上させる小さなが重要な改善です。

このように、各変更はそれぞれ独立していますが、全体としてAzure AIとOpenAIサービスの利用者により良い価値を提供し、サービスの信頼性と効率性を強化するものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [content-filters.md](#item-6f0627) | minor update | コンテンツフィルターの設定変更 | modified | 1 | 1 | 2 | 
| [predicted-outputs.md](#item-212eb9) | new feature | Azure OpenAIサービスの予測出力の使い方 | added | 418 | 0 | 418 | 
| [api-surface.md](#item-a25fa2) | minor update | APIリリース日の更新 | modified | 3 | 3 | 6 | 
| [latest-inference-preview.md](#item-24bf0f) | minor update | 最新の推論プレビュードキュメントの更新 | modified | 263 | 125 | 388 | 
| [provisioned-global.md](#item-340884) | minor update | 最新のgpt-4oリリースの地域情報更新 | modified | 28 | 27 | 55 | 
| [reference-preview.md](#item-e197a2) | minor update | Azure OpenAI REST APIのプレビュー日付更新 | modified | 2 | 2 | 4 | 
| [reference.md](#item-7b1183) | minor update | Azure OpenAI REST APIのドキュメント日付更新 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c945af) | minor update | 目次の更新: 予測出力に関する項目追加 | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/ai-services/openai/how-to/content-filters.md{#item-6f0627}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ The content filtering system integrated into Azure AI Foundry runs alongside the
 
 The default content filtering configuration is set to filter at the medium severity threshold for all four content harms categories for both prompts and completions. That means that content that is detected at severity level medium or high is filtered, while content detected at severity level low or safe is not filtered by the content filters. Learn more about content categories, severity levels, and the behavior of the content filtering system [here](../concepts/content-filter.md). 
 
-Jailbreak risk detection and protected text and code models are optional and off by default. For jailbreak and protected material text and code models, the configurability feature allows all customers to turn the models on and off. The models are by default off and can be turned on per your scenario. Some models are required to be on for certain scenarios to retain coverage under the [Customer Copyright Commitment](/legal/cognitive-services/openai/customer-copyright-commitment?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext).
+Jailbreak risk detection and protected text and code models are optional and on by default. For jailbreak and protected material text and code models, the configurability feature allows all customers to turn the models on and off. The models are by default on and can be turned off per your scenario. Some models are required to be on for certain scenarios to retain coverage under the [Customer Copyright Commitment](/legal/cognitive-services/openai/customer-copyright-commitment?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext).
 
 > [!NOTE]
 > All customers have the ability to modify the content filters and configure the severity thresholds (low, medium, high). Approval is required for turning the content filters partially or fully off. Managed customers only may apply for full content filtering control via this form: [Azure OpenAI Limited Access Review: Modified Content Filters](https://ncv.microsoft.com/uEfCgnITdR). At this time, it is not possible to become a managed customer.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルターの設定変更"
}
```

### Explanation
この変更は、Azure AI Foundryのコンテンツフィルタリングシステムに関するドキュメント内のテキストの一部を更新しています。具体的には、「Jailbreakリスク検出と保護されたテキストおよびコードモデル」がデフォルトで「オフ」であるという記述が、「オン」に変更されています。つまり、これらのモデルはデフォルトで有効になっており、ユーザーはシナリオに応じてモデルをオフにすることができるということです。この修正は、コンテンツフィルターの使いやすさや設定を改善することを目的としています。

## articles/ai-services/openai/how-to/predicted-outputs.md{#item-212eb9}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,418 @@
+---
+title: 'How to use predicted outputs with Azure OpenAI Service'
+titleSuffix: Azure OpenAI
+description: Learn how to improve your model response latency with predicted outputs
+services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: how-to
+ms.date: 01/29/2025
+author: mrbullwinkle
+ms.author: mbullwin
+recommendations: false
+---
+
+# Predicted outputs (preview)
+
+Predicted outputs can improve model response latency for chat completions calls where minimal changes are needed to a larger body of text. If you're asking the model to provide a response where a large portion of the expected response is already known, predicted outputs can significantly reduce the latency of this request. This capability is particularly well-suited for coding scenarios, including autocomplete, error detection, and real-time editing, where speed and responsiveness are critical for developers and end-users. Rather than have the model regenerate all the text from scratch, you can indicate to the model that most of the response is already known by passing the known text to the `prediction` parameter.
+
+## Model support
+
+- `gpt-4o-mini` version: `2024-07-18`
+- `gpt-4o` version: `2024-05-13`
+- `gpt-4o` version: `2024-08-06`
+- `gpt-4o` version: `2024-11-20`
+
+## API support
+
+- `2025-01-01-preview`
+
+## Unsupported features
+
+Predicted outputs is currently text-only. These features can't be used in conjunction with the `prediction` parameter and predicted outputs.
+
+- Tools/Function calling
+- audio models/inputs and outputs
+- `n` values higher than `1`
+- `logprobs`
+- `presence_penalty` values greater than `0`
+- `frequency_penalty` values greater than `0`
+- `max_completion_tokens`
+
+> [!NOTE]
+> The predicted outputs feature is currently unavailable for models in the South East Asia region.
+
+## Getting started
+
+To demonstrate the basics of predicted outputs, we'll start by asking a model to refactor the code from the common programming `FizzBuzz` problem to replace the instance of `FizzBuzz` with `MSFTBuzz`. We'll pass our example code to the model in two places. First as part of a user message in the `messages` array/list, and a second time as part of the content of the new `prediction` parameter.
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
+
+You might need to upgrade your OpenAI client library to access the `prediction` parameter.
+
+```cmd
+pip install openai --upgrade
+```
+
+```python
+import os
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+client = AzureOpenAI(
+  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+  azure_ad_token_provider=token_provider,
+  api_version="2025-01-01-preview"
+)
+
+code = """
+for number in range(1, 101):
+    if number % 3 == 0 and number % 5 == 0:
+        print("FizzBuzz")
+    elif number % 3 == 0:
+        print("Fizz")
+    elif number % 5 == 0:
+        print("Buzz")
+    else:
+        print(number)
+"""
+
+instructions = """
+Replace string `FizzBuzz` with `MSFTBuzz`. Respond only 
+with code, and with no markdown formatting.
+"""
+
+
+completion = client.chat.completions.create(
+    model="gpt-4o-mini", # replace with your unique model deployment name
+    messages=[
+        {
+            "role": "user",
+            "content": instructions
+        },
+        {
+            "role": "user",
+            "content": code
+        }
+    ],
+    prediction={
+        "type": "content",
+        "content": code
+    }
+)
+
+print(completion.model_dump_json(indent=2))
+```
+
+# [Python (key-based auth)](#tab/python)
+
+You might need to upgrade your OpenAI client library to access the `prediction` parameter.
+
+```cmd
+pip install openai --upgrade
+```
+
+```python
+import os
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
+  api_version="2025-01-01-preview"
+)
+
+code = """
+for number in range(1, 101):
+    if number % 3 == 0 and number % 5 == 0:
+        print("FizzBuzz")
+    elif number % 3 == 0:
+        print("Fizz")
+    elif number % 5 == 0:
+        print("Buzz")
+    else:
+        print(number)
+"""
+
+instructions = """
+Replace string `FizzBuzz` with `MSFTBuzz`. Respond only 
+with code, and with no markdown formatting.
+"""
+
+
+completion = client.chat.completions.create(
+    model="gpt-4o-mini", # replace with your unique model deployment name
+    messages=[
+        {
+            "role": "user",
+            "content": instructions
+        },
+        {
+            "role": "user",
+            "content": code
+        }
+    ],
+    prediction={
+        "type": "content",
+        "content": code
+    }
+)
+
+print(completion.model_dump_json(indent=2))
+```
+
+---
+
+### Output
+
+```json
+{
+  "id": "chatcmpl-AskZk3P5QGmefqobDw4Ougo6jLxSP",
+  "choices": [
+    {
+      "finish_reason": "stop",
+      "index": 0,
+      "logprobs": null,
+      "message": {
+        "content": "for number in range(1, 101):\n    if number % 3 == 0 and number % 5 == 0:\n        print(\"MSFTBuzz\")\n    elif number % 3 == 0:\n        print(\"Fizz\")\n    elif number % 5 == 0:\n        print(\"Buzz\")\n    else:\n        print(number)",
+        "refusal": null,
+        "role": "assistant",
+        "audio": null,
+        "function_call": null,
+        "tool_calls": null
+      },
+      "content_filter_results": {
+        "hate": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "protected_material_code": {
+          "filtered": false,
+          "detected": false
+        },
+        "protected_material_text": {
+          "filtered": false,
+          "detected": false
+        },
+        "self_harm": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "sexual": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "violence": {
+          "filtered": false,
+          "severity": "safe"
+        }
+      }
+    }
+  ],
+  "created": 1737612112,
+  "model": "gpt-4o-mini-2024-07-18",
+  "object": "chat.completion",
+  "service_tier": null,
+  "system_fingerprint": "fp_5154047bf2",
+  "usage": {
+    "completion_tokens": 77,
+    "prompt_tokens": 124,
+    "total_tokens": 201,
+    "completion_tokens_details": {
+      "accepted_prediction_tokens": 6,
+      "audio_tokens": 0,
+      "reasoning_tokens": 0,
+      "rejected_prediction_tokens": 4
+    },
+    "prompt_tokens_details": {
+      "audio_tokens": 0,
+      "cached_tokens": 0
+    }
+  },
+  "prompt_filter_results": [
+    {
+      "prompt_index": 0,
+      "content_filter_results": {
+        "hate": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "jailbreak": {
+          "filtered": false,
+          "detected": false
+        },
+        "self_harm": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "sexual": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "violence": {
+          "filtered": false,
+          "severity": "safe"
+        }
+      }
+    }
+  ]
+}
+```
+
+Notice in the output the new response parameters for `accepted_prediction_tokens` and `rejected_prediction_tokens`:
+
+```json
+  "usage": {
+    "completion_tokens": 77,
+    "prompt_tokens": 124,
+    "total_tokens": 201,
+    "completion_tokens_details": {
+      "accepted_prediction_tokens": 6,
+      "audio_tokens": 0,
+      "reasoning_tokens": 0,
+      "rejected_prediction_tokens": 4
+    }
+```
+
+The `accepted_prediction_tokens` help reduce model response latency, but any `rejected_prediction_tokens` have the same cost implication as additional output tokens generated by the model. For this reason, while predicted outputs can improve model response times, it can result in greater costs. You'll need to evaluate and balance the increased model performance against the potential increases in cost.
+
+It's also important to understand, that using predictive outputs doesn't guarantee a reduction in latency. A large request with a greater percentage of rejected prediction tokens than accepted prediction tokens could result in an increase in model response latency, rather than a decrease.  
+
+> [!NOTE]
+> Unlike [prompt caching](./prompt-caching.md) which only works when a set minimum number of initial tokens at the beginning of a request are identical, predicted outputs isn't constrained by token location. Even if your response text contains new output that will be returned prior to the predicted output, `accepted_prediction_tokens` can still occur.
+
+## Streaming
+
+Predicted outputs performance boost is often most obvious if you're returning your responses with streaming enabled.
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
+
+You might need to upgrade your OpenAI client library to access the `prediction` parameter.
+
+```cmd
+pip install openai --upgrade
+```
+
+```python
+import os
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+client = AzureOpenAI(
+  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+  azure_ad_token_provider=token_provider,
+  api_version="2025-01-01-preview"
+)
+
+code = """
+for number in range(1, 101):
+    if number % 3 == 0 and number % 5 == 0:
+        print("FizzBuzz")
+    elif number % 3 == 0:
+        print("Fizz")
+    elif number % 5 == 0:
+        print("Buzz")
+    else:
+        print(number)
+"""
+
+instructions = """
+Replace string `FizzBuzz` with `MSFTBuzz`. Respond only 
+with code, and with no markdown formatting.
+"""
+
+
+completion = client.chat.completions.create(
+    model="gpt-4o-mini", # replace with your unique model deployment name
+    messages=[
+        {
+            "role": "user",
+            "content": instructions
+        },
+        {
+            "role": "user",
+            "content": code
+        }
+    ],
+    prediction={
+        "type": "content",
+        "content": code
+    },
+    stream=True
+)
+
+for chunk in completion:
+    if chunk.choices and chunk.choices[0].delta.content is not None:
+        print(chunk.choices[0].delta.content, end='',)
+
+```
+
+# [Python (key-based auth)](#tab/python)
+
+You might need to upgrade your OpenAI client library to access the `prediction` parameter.
+
+```cmd
+pip install openai --upgrade
+```
+
+```python
+import os
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
+  api_version="2025-01-01-preview"
+)
+
+code = """
+for number in range(1, 101):
+    if number % 3 == 0 and number % 5 == 0:
+        print("FizzBuzz")
+    elif number % 3 == 0:
+        print("Fizz")
+    elif number % 5 == 0:
+        print("Buzz")
+    else:
+        print(number)
+"""
+
+instructions = """
+Replace string `FizzBuzz` with `MSFTBuzz`. Respond only 
+with code, and with no markdown formatting.
+"""
+
+
+completion = client.chat.completions.create(
+    model="gpt-4o-mini", # replace with your unique model deployment name
+    messages=[
+        {
+            "role": "user",
+            "content": instructions
+        },
+        {
+            "role": "user",
+            "content": code
+        }
+    ],
+    prediction={
+        "type": "content",
+        "content": code
+    },
+    stream=True
+)
+
+for chunk in completion:
+    if chunk.choices and chunk.choices[0].delta.content is not None:
+        print(chunk.choices[0].delta.content, end='',)
+```
+
+---
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIサービスの予測出力の使い方"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおける「予測出力」機能に関する新たなドキュメントを追加したものです。このドキュメントでは、モデルのレスポンスレイテンシを改善する方法について説明しています。予測出力機能は、特に一部の知られたテキストに対して迅速な応答が要求されるシナリオに役立ちます。この機能を使用することで、開発者や最終ユーザーにとって重要な速度と応答性を高めることができます。

ドキュメントには、モデルのサポート、APIサポート、サポートされていない機能、および、プログラミングの具体例が含まれており、コードスニペットを用いてどのように予測出力を実装するかを示しています。また、利用者が予測出力機能を活用する上での留意点や、コスト面での考慮事項も詳述されています。これにより、開発者はこの新機能を簡単に理解し、利用できるようになります。

## articles/ai-services/openai/includes/api-surface.md{#item-a25fa2}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Information on the division of control plane and data plane API sur
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 01/08/2024
+ms.date: 01/29/2025
 ---
 
 
@@ -22,8 +22,8 @@ Each API surface/specification encapsulates a different set of Azure OpenAI capa
 | API | Latest preview release | Latest GA release | Specifications | Description |
 |:---|:----|:----|:----|:---|
 | **Control plane** | [`2024-06-01-preview`](/rest/api/aiservices/accountmanagement/operation-groups?view=rest-aiservices-accountmanagement-2024-06-01-preview&preserve-view=true) | [`2024-10-01`](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices) | Azure OpenAI shares a common control plane with all other Azure AI Services. The control plane API is used for things like [creating Azure OpenAI resources](/rest/api/aiservices/accountmanagement/accounts/create?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), [model deployment](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), and other higher level resource management tasks. The control plane also governs what is possible to do with capabilities like Azure Resource Manager, Bicep, Terraform, and Azure CLI.|
-| **Data plane - authoring** | `2024-10-01-preview` | `2024-10-21` | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
-| **Data plane - inference** | [`2024-12-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-10-21`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, speech/whisper, on your data, Dall-e, assistants, etc. |
+| **Data plane - authoring** | `2025-01-01-preview` | `2024-10-21` | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
+| **Data plane - inference** | [`2025-01-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-10-21`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, speech/whisper, on your data, Dall-e, assistants, etc. |
 
 ## Authentication
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリリース日の更新"
}
```

### Explanation
この変更は、Azure OpenAI APIの仕様に関するドキュメントで、いくつかのAPIリリース日の更新を含んでいます。具体的には、「データプレーン - 作成」および「データプレーン - 推論」セクションの最新プレビューリリース日がそれぞれ「2025-01-01」に設定され、さらに、各種APIに関する説明が明確化されています。これにより、利用者は最新のAPIリリース情報を正確に把握できるようになります。この修正は、APIの方針や仕様に関する理解を助け、開発者が適切に更新された情報を参照できることを目指しています。

## articles/ai-services/openai/includes/api-versions/latest-inference-preview.md{#item-24bf0f}

<details>
<summary>Diff</summary>
````diff
@@ -5,13 +5,13 @@ description: Latest preview data plane inference documentation generated from Op
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 01/08/2024
+ms.date: 01/29/2025
 ---
 
 ## Completions - Create
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/completions?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/completions?api-version=2025-01-01-preview
 ```
 
 Creates a completion for the provided prompt, parameters and chosen model.
@@ -41,18 +41,36 @@ Creates a completion for the provided prompt, parameters and chosen model.
 | echo | boolean | Echo back the prompt in addition to the completion<br> | No | False |
 | frequency_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.<br> | No | 0 |
 | logit_bias | object | Modify the likelihood of specified tokens appearing in the completion.<br><br>Accepts a JSON object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.<br><br>As an example, you can pass `{"50256": -100}` to prevent the <&#124;endoftext&#124;> token from being generated.<br> | No | None |
-| logprobs | integer | Include the log probabilities on the `logprobs` most likely output tokens, as well the chosen tokens. For example, if `logprobs` is 5, the API will return a list of the five most likely tokens. The API will always return the `logprob` of the sampled token, so there may be up to `logprobs+1` elements in the response.<br><br>The maximum value for `logprobs` is 5.<br> | No | None |
-| max_tokens | integer | The maximum number of tokens that can be generated in the completion.<br><br>The token count of your prompt plus `max_tokens` can't exceed the model's context length. <br> | No | 16 |
+| logprobs | integer | Include the log probabilities on the `logprobs` most likely output tokens, as well the chosen tokens. For example, if `logprobs` is 5, the API will return a list of the 5 most likely tokens. The API will always return the `logprob` of the sampled token, so there may be up to `logprobs+1` elements in the response.<br><br>The maximum value for `logprobs` is 5.<br> | No | None |
+| max_tokens | integer | The maximum number of tokens that can be generated in the completion.<br><br>The token count of your prompt plus `max_tokens` can't exceed the model's context length.  | No | 16 |
 | n | integer | How many completions to generate for each prompt.<br><br>**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.<br> | No | 1 |
+| modalities | [ChatCompletionModalities](#chatcompletionmodalities) | Output types that you would like the model to generate for this request.<br>Most models are capable of generating text, which is the default:<br><br>`["text"]`<br><br>The `gpt-4o-audio-preview` model can also be used to generate audio. To<br>request that this model generate both text and audio responses, you can<br>use:<br><br>`["text", "audio"]`<br> | No |  |
+| prediction | [PredictionContent](#predictioncontent) | Configuration for a Predicted Output, which can greatly improve response times when large parts of the model response are known ahead of time. This is most common when you are regenerating a file with only minor changes to most of the content. | No |  |
+| audio | object | Parameters for audio output. Required when audio output is requested with<br>`modalities: ["audio"]`.  | No |  |
 | presence_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.<br> | No | 0 |
 | seed | integer | If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.<br><br>Determinism isn't guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.<br> | No |  |
 | stop | string or array | Up to four sequences where the API will stop generating further tokens. The returned text won't contain the stop sequence.<br> | No |  |
-| stream | boolean | Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. <br> | No | False |
+| stream | boolean | Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message.  | No | False |
 | suffix | string | The suffix that comes after a completion of inserted text.<br><br>This parameter is only supported for `gpt-3.5-turbo-instruct`.<br> | No | None |
 | temperature | number | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.<br><br>We generally recommend altering this or `top_p` but not both.<br> | No | 1 |
 | top_p | number | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br><br>We generally recommend altering this or `temperature` but not both.<br> | No | 1 |
 | user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse.<br> | No |  |
 
+
+### Properties for audio
+
+#### voice
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| voice | string | Specifies the voice type. Supported voices are `alloy`, `echo`, <br>`fable`, `onyx`, `nova`, and `shimmer`.<br> |  |
+
+#### format
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| format | string | Specifies the output audio format. Must be one of `wav`, `mp3`, `flac`,<br>`opus`, or `pcm16`. <br> |  |
+
 ### Responses
 
 **Status Code:** 200
@@ -79,7 +97,7 @@ Creates a completion for the provided prompt, parameters and chosen model.
 Creates a completion for the provided prompt, parameters and chosen model.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/completions?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/completions?api-version=2025-01-01-preview
 
 {
  "prompt": [
@@ -119,7 +137,7 @@ Status Code: 200
 ## Embeddings - Create
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/embeddings?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/embeddings?api-version=2025-01-01-preview
 ```
 
 Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms.
@@ -190,7 +208,7 @@ Get a vector representation of a given input that can be easily consumed by mach
 Return the embeddings for a given prompt.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/embeddings?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/embeddings?api-version=2025-01-01-preview
 
 {
  "input": [
@@ -249,8 +267,7 @@ Status Code: 200
           -0.021560553,
           0.016515596,
           -0.015572986,
-          0.0038666942,
-          -8.432463e-05
+          0.0038666942
         ]
       }
     ],
@@ -265,7 +282,7 @@ Status Code: 200
 ## Chat completions - Create
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2025-01-01-preview
 ```
 
 Creates a completion for the chat message
@@ -292,19 +309,19 @@ Creates a completion for the chat message
 |------|------|-------------|----------|---------|
 | temperature | number | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.<br><br>We generally recommend altering this or `top_p` but not both.<br> | No | 1 |
 | top_p | number | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br><br>We generally recommend altering this or `temperature` but not both.<br> | No | 1 |
-| stream | boolean | If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. <br> | No | False |
+| stream | boolean | If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message.  | No | False |
 | stop | string or array | Up to four sequences where the API will stop generating further tokens.<br> | No |  |
-| max_tokens | integer | The maximum number of tokens that can be generated in the chat completion.<br><br>The total length of input tokens and generated tokens is limited by the model's context length. <br> | No |  |
+| max_tokens | integer | The maximum number of tokens that can be generated in the chat completion.<br><br>The total length of input tokens and generated tokens is limited by the model's context length.  | No |  |
 | max_completion_tokens | integer | An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens. This is only supported in o1 series models. Will expand the support to other models in future API release. | No |  |
 | presence_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.<br> | No | 0 |
 | frequency_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.<br> | No | 0 |
 | logit_bias | object | Modify the likelihood of specified tokens appearing in the completion.<br><br>Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.<br> | No | None |
 | store | boolean | Whether or not to store the output of this chat completion request for use in our model distillation or evaluation products. | No |  |
 | metadata | object | Developer-defined tags and values used for filtering completions in the stored completions dashboard. | No |  |
 | user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse.<br> | No |  |
-| messages | array | A list of messages comprising the conversation so far. | Yes |  |
+| messages | array | A list of messages comprising the conversation so far.  | Yes |  |
 | data_sources | array |   The configuration entries for Azure OpenAI chat extensions that use them.<br>  This additional specification is only compatible with Azure OpenAI. | No |  |
-| reasoning_effort | enum | **o1 models only** <br><br> Constrains effort on reasoning for <br>reasoning models.<br><br>Currently supported values are `low`, `medium`, and `high`. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response.<br>Possible values: low, medium, high | No |  |
+| reasoning_effort | enum | **o1 models only** <br><br> Constrains effort on reasoning for reasoning models.<br><br>Currently supported values are `low`, `medium`, and `high`. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response.<br>Possible values: low, medium, high | No |  |
 | logprobs | boolean | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | No | False |
 | top_logprobs | integer | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | No |  |
 | n | integer | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs. | No | 1 |
@@ -343,7 +360,7 @@ Creates a completion for the chat message
 Creates a completion for the provided prompt, parameters and chosen model.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2025-01-01-preview
 
 {
  "messages": [
@@ -391,7 +408,7 @@ Status Code: 200
 Creates a completion based on Azure Search data and system-assigned managed identity.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2025-01-01-preview
 
 {
  "messages": [
@@ -459,7 +476,7 @@ Status Code: 200
 Creates a completion based on Azure Search image vector data.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2025-01-01-preview
 
 {
  "messages": [
@@ -522,7 +539,7 @@ Status Code: 200
 Creates a completion based on Azure Search vector data, previous assistant message and user-assigned managed identity.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2025-01-01-preview
 
 {
  "messages": [
@@ -623,7 +640,7 @@ Status Code: 200
 Creates a completion for the provided Azure Cosmos DB.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2025-01-01-preview
 
 {
  "messages": [
@@ -705,7 +722,7 @@ Status Code: 200
 Creates a completion for the provided Mongo DB.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2025-01-01-preview
 
 {
  "messages": [
@@ -790,7 +807,7 @@ Status Code: 200
 Creates a completion for the provided Elasticsearch.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2025-01-01-preview
 
 {
  "messages": [
@@ -860,7 +877,7 @@ Status Code: 200
 Creates a completion for the provided Pinecone resource.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2025-01-01-preview
 
 {
  "messages": [
@@ -940,7 +957,7 @@ Status Code: 200
 ## Transcriptions - Create
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/audio/transcriptions?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/audio/transcriptions?api-version=2025-01-01-preview
 ```
 
 Transcribes audio into the input language.
@@ -990,7 +1007,7 @@ Transcribes audio into the input language.
 Gets transcribed text and associated metadata from provided spoken audio data.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/audio/transcriptions?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/audio/transcriptions?api-version=2025-01-01-preview
 
 ```
 
@@ -1009,7 +1026,7 @@ Status Code: 200
 Gets transcribed text and associated metadata from provided spoken audio data.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/audio/transcriptions?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/audio/transcriptions?api-version=2025-01-01-preview
 
 "---multipart-boundary\nContent-Disposition: form-data; name=\"file\"; filename=\"file.wav\"\nContent-Type: application/octet-stream\n\nRIFF..audio.data.omitted\n---multipart-boundary--"
 
@@ -1027,7 +1044,7 @@ Status Code: 200
 ## Translations - Create
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/audio/translations?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/audio/translations?api-version=2025-01-01-preview
 ```
 
 Transcribes and translates input audio into English text.
@@ -1075,7 +1092,7 @@ Transcribes and translates input audio into English text.
 Gets English language transcribed text and associated metadata from provided spoken audio data.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/audio/translations?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/audio/translations?api-version=2025-01-01-preview
 
 "---multipart-boundary\nContent-Disposition: form-data; name=\"file\"; filename=\"file.wav\"\nContent-Type: application/octet-stream\n\nRIFF..audio.data.omitted\n---multipart-boundary--"
 
@@ -1096,7 +1113,7 @@ Status Code: 200
 Gets English language transcribed text and associated metadata from provided spoken audio data.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/audio/translations?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/audio/translations?api-version=2025-01-01-preview
 
 "---multipart-boundary\nContent-Disposition: form-data; name=\"file\"; filename=\"file.wav\"\nContent-Type: application/octet-stream\n\nRIFF..audio.data.omitted\n---multipart-boundary--"
 
@@ -1114,7 +1131,7 @@ Status Code: 200
 ## Speech - Create
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/audio/speech?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/audio/speech?api-version=2025-01-01-preview
 ```
 
 Generates audio from the input text.
@@ -1161,7 +1178,7 @@ Generates audio from the input text.
 Synthesizes audio from the provided text.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/audio/speech?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/audio/speech?api-version=2025-01-01-preview
 
 {
  "input": "Hi! What are you going to make?",
@@ -1182,7 +1199,7 @@ Status Code: 200
 ## Image generations - Create
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/images/generations?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/images/generations?api-version=2025-01-01-preview
 ```
 
 Generates a batch of images from a text caption on a given DALLE model deployment
@@ -1240,7 +1257,7 @@ Generates a batch of images from a text caption on a given DALLE model deploymen
 Creates images given a prompt.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/images/generations?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/images/generations?api-version=2025-01-01-preview
 
 {
  "prompt": "In the style of WordArt, Microsoft Clippy wearing a cowboy hat.",
@@ -1314,7 +1331,7 @@ Status Code: 200
 ## List - Assistants
 
 ```HTTP
-GET https://{endpoint}/openai/assistants?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/assistants?api-version=2025-01-01-preview
 ```
 
 Returns a list of assistants.
@@ -1353,7 +1370,7 @@ Returns a list of assistants.
 Returns a list of assistants.
 
 ```HTTP
-GET https://{endpoint}/openai/assistants?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/assistants?api-version=2025-01-01-preview
 
 ```
 
@@ -1424,7 +1441,7 @@ Status Code: 200
 ## Create - Assistant
 
 ```HTTP
-POST https://{endpoint}/openai/assistants?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/assistants?api-version=2025-01-01-preview
 ```
 
 Create an assistant with a model and instructions.
@@ -1492,7 +1509,7 @@ Create an assistant with a model and instructions.
 Create an assistant with a model and instructions.
 
 ```HTTP
-POST https://{endpoint}/openai/assistants?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/assistants?api-version=2025-01-01-preview
 
 {
  "name": "Math Tutor",
@@ -1535,7 +1552,7 @@ Status Code: 200
 ## Get - Assistant
 
 ```HTTP
-GET https://{endpoint}/openai/assistants/{assistant_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/assistants/{assistant_id}?api-version=2025-01-01-preview
 ```
 
 Retrieves an assistant.
@@ -1571,7 +1588,7 @@ Retrieves an assistant.
 Retrieves an assistant.
 
 ```HTTP
-GET https://{endpoint}/openai/assistants/{assistant_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/assistants/{assistant_id}?api-version=2025-01-01-preview
 
 ```
 
@@ -1603,7 +1620,7 @@ Status Code: 200
 ## Modify - Assistant
 
 ```HTTP
-POST https://{endpoint}/openai/assistants/{assistant_id}?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/assistants/{assistant_id}?api-version=2025-01-01-preview
 ```
 
 Modifies an assistant.
@@ -1671,7 +1688,7 @@ Modifies an assistant.
 Modifies an assistant.
 
 ```HTTP
-POST https://{endpoint}/openai/assistants/{assistant_id}?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/assistants/{assistant_id}?api-version=2025-01-01-preview
 
 {
  "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies. Always response with info from either of the files.",
@@ -1718,7 +1735,7 @@ Status Code: 200
 ## Delete - Assistant
 
 ```HTTP
-DELETE https://{endpoint}/openai/assistants/{assistant_id}?api-version=2024-12-01-preview
+DELETE https://{endpoint}/openai/assistants/{assistant_id}?api-version=2025-01-01-preview
 ```
 
 Delete an assistant.
@@ -1754,7 +1771,7 @@ Delete an assistant.
 Deletes an assistant.
 
 ```HTTP
-DELETE https://{endpoint}/openai/assistants/{assistant_id}?api-version=2024-12-01-preview
+DELETE https://{endpoint}/openai/assistants/{assistant_id}?api-version=2025-01-01-preview
 
 ```
 
@@ -1773,7 +1790,7 @@ Status Code: 200
 ## Create - Thread
 
 ```HTTP
-POST https://{endpoint}/openai/threads?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads?api-version=2025-01-01-preview
 ```
 
 Create a thread.
@@ -1834,7 +1851,7 @@ Create a thread.
 Creates a thread.
 
 ```HTTP
-POST https://{endpoint}/openai/threads?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads?api-version=2025-01-01-preview
 
 ```
 
@@ -1854,7 +1871,7 @@ Status Code: 200
 ## Get - Thread
 
 ```HTTP
-GET https://{endpoint}/openai/threads/{thread_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/threads/{thread_id}?api-version=2025-01-01-preview
 ```
 
 Retrieves a thread.
@@ -1890,7 +1907,7 @@ Retrieves a thread.
 Retrieves a thread.
 
 ```HTTP
-GET https://{endpoint}/openai/threads/{thread_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/threads/{thread_id}?api-version=2025-01-01-preview
 
 ```
 
@@ -1915,7 +1932,7 @@ Status Code: 200
 ## Modify - Thread
 
 ```HTTP
-POST https://{endpoint}/openai/threads/{thread_id}?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/{thread_id}?api-version=2025-01-01-preview
 ```
 
 Modifies a thread.
@@ -1975,7 +1992,7 @@ Modifies a thread.
 Modifies a thread.
 
 ```HTTP
-POST https://{endpoint}/openai/threads/{thread_id}?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/{thread_id}?api-version=2025-01-01-preview
 
 {
  "metadata": {
@@ -2006,7 +2023,7 @@ Status Code: 200
 ## Delete - Thread
 
 ```HTTP
-DELETE https://{endpoint}/openai/threads/{thread_id}?api-version=2024-12-01-preview
+DELETE https://{endpoint}/openai/threads/{thread_id}?api-version=2025-01-01-preview
 ```
 
 Delete a thread.
@@ -2042,7 +2059,7 @@ Delete a thread.
 Deletes a thread.
 
 ```HTTP
-DELETE https://{endpoint}/openai/threads/{thread_id}?api-version=2024-12-01-preview
+DELETE https://{endpoint}/openai/threads/{thread_id}?api-version=2025-01-01-preview
 
 ```
 
@@ -2061,7 +2078,7 @@ Status Code: 200
 ## List - Messages
 
 ```HTTP
-GET https://{endpoint}/openai/threads/{thread_id}/messages?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/threads/{thread_id}/messages?api-version=2025-01-01-preview
 ```
 
 Returns a list of messages for a given thread.
@@ -2102,7 +2119,7 @@ Returns a list of messages for a given thread.
 List Messages
 
 ```HTTP
-GET https://{endpoint}/openai/threads/{thread_id}/messages?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/threads/{thread_id}/messages?api-version=2025-01-01-preview
 
 ```
 
@@ -2164,7 +2181,7 @@ Status Code: 200
 ## Create - Message
 
 ```HTTP
-POST https://{endpoint}/openai/threads/{thread_id}/messages?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/{thread_id}/messages?api-version=2025-01-01-preview
 ```
 
 Create a message.
@@ -2211,7 +2228,7 @@ Create a message.
 Create a message.
 
 ```HTTP
-POST https://{endpoint}/openai/threads/{thread_id}/messages?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/{thread_id}/messages?api-version=2025-01-01-preview
 
 {
  "role": "user",
@@ -2250,7 +2267,7 @@ Status Code: 200
 ## Get - Message
 
 ```HTTP
-GET https://{endpoint}/openai/threads/{thread_id}/messages/{message_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/threads/{thread_id}/messages/{message_id}?api-version=2025-01-01-preview
 ```
 
 Retrieve a message.
@@ -2287,7 +2304,7 @@ Retrieve a message.
 Retrieve a message.
 
 ```HTTP
-GET https://{endpoint}/openai/threads/{thread_id}/messages/{message_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/threads/{thread_id}/messages/{message_id}?api-version=2025-01-01-preview
 
 ```
 
@@ -2321,7 +2338,7 @@ Status Code: 200
 ## Modify - Message
 
 ```HTTP
-POST https://{endpoint}/openai/threads/{thread_id}/messages/{message_id}?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/{thread_id}/messages/{message_id}?api-version=2025-01-01-preview
 ```
 
 Modifies a message.
@@ -2366,7 +2383,7 @@ Modifies a message.
 Modify a message.
 
 ```HTTP
-POST https://{endpoint}/openai/threads/{thread_id}/messages/{message_id}?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/{thread_id}/messages/{message_id}?api-version=2025-01-01-preview
 
 {
  "metadata": {
@@ -2410,7 +2427,7 @@ Status Code: 200
 ## Create - Thread And Run
 
 ```HTTP
-POST https://{endpoint}/openai/threads/runs?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/runs?api-version=2025-01-01-preview
 ```
 
 Create a thread and run it in one request.
@@ -2436,7 +2453,7 @@ Create a thread and run it in one request.
 |------|------|-------------|----------|---------|
 | assistant_id | string | The ID of the assistant to use to execute this run. | Yes |  |
 | thread | [createThreadRequest](#createthreadrequest) |  | No |  |
-| model | string | The ID of the Model to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used. | No |  |
+| model | string | The ID of the model to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used. | No |  |
 | instructions | string | Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis. | No |  |
 | tools | array | Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis. | No |  |
 | tool_resources | object | A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.<br> | No |  |
@@ -2484,7 +2501,7 @@ Create a thread and run it in one request.
 Create a thread and run it in one request.
 
 ```HTTP
-POST https://{endpoint}/openai/threads/runs?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/runs?api-version=2025-01-01-preview
 
 {
  "assistant_id": "asst_abc123",
@@ -2542,7 +2559,7 @@ Status Code: 200
 ## List - Runs
 
 ```HTTP
-GET https://{endpoint}/openai/threads/{thread_id}/runs?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/threads/{thread_id}/runs?api-version=2025-01-01-preview
 ```
 
 Returns a list of runs belonging to a thread.
@@ -2582,7 +2599,7 @@ Returns a list of runs belonging to a thread.
 Returns a list of runs belonging to a thread.
 
 ```HTTP
-GET https://{endpoint}/openai/threads/{thread_id}/runs?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/threads/{thread_id}/runs?api-version=2025-01-01-preview
 
 ```
 
@@ -2696,7 +2713,7 @@ Status Code: 200
 ## Create - Run
 
 ```HTTP
-POST https://{endpoint}/openai/threads/{thread_id}/runs?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/{thread_id}/runs?api-version=2025-01-01-preview
 ```
 
 Create a run.
@@ -2756,7 +2773,7 @@ Create a run.
 Create a run.
 
 ```HTTP
-POST https://{endpoint}/openai/threads/{thread_id}/runs?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/{thread_id}/runs?api-version=2025-01-01-preview
 
 {
  "assistant_id": "asst_abc123"
@@ -2808,7 +2825,7 @@ Status Code: 200
 ## Get - Run
 
 ```HTTP
-GET https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}?api-version=2025-01-01-preview
 ```
 
 Retrieves a run.
@@ -2845,7 +2862,7 @@ Retrieves a run.
 Gets a run.
 
 ```HTTP
-GET https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}?api-version=2025-01-01-preview
 
 ```
 
@@ -2878,7 +2895,7 @@ Status Code: 200
 ## Modify - Run
 
 ```HTTP
-POST https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}?api-version=2025-01-01-preview
 ```
 
 Modifies a run.
@@ -2923,7 +2940,7 @@ Modifies a run.
 Modifies a run.
 
 ```HTTP
-POST https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}?api-version=2025-01-01-preview
 
 {
  "metadata": {
@@ -2991,7 +3008,7 @@ Status Code: 200
 ## Submit - Tool Outputs To Run
 
 ```HTTP
-POST https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/submit_tool_outputs?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/submit_tool_outputs?api-version=2025-01-01-preview
 ```
 
 When a run has the `status: "requires_action"` and `required_action.type` is `submit_tool_outputs`, this endpoint can be used to submit the outputs from the tool calls once they're all completed. All outputs must be submitted in a single request.
@@ -3039,7 +3056,7 @@ When a run has the `status: "requires_action"` and `required_action.type` is `su
 
 
 ```HTTP
-POST https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/submit_tool_outputs?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/submit_tool_outputs?api-version=2025-01-01-preview
 
 {
  "tool_outputs": [
@@ -3118,7 +3135,7 @@ Status Code: 200
 ## Cancel - Run
 
 ```HTTP
-POST https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/cancel?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/cancel?api-version=2025-01-01-preview
 ```
 
 Cancels a run that is `in_progress`.
@@ -3156,7 +3173,7 @@ Cancels a run that is `in_progress`.
 
 
 ```HTTP
-POST https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/cancel?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/cancel?api-version=2025-01-01-preview
 
 ```
 
@@ -3203,7 +3220,7 @@ Status Code: 200
 ## List - Run Steps
 
 ```HTTP
-GET https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/steps?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/steps?api-version=2025-01-01-preview
 ```
 
 Returns a list of run steps belonging to a run.
@@ -3245,7 +3262,7 @@ Returns a list of run steps belonging to a run.
 Returns a list of run steps belonging to a run.
 
 ```HTTP
-GET https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/steps?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/steps?api-version=2025-01-01-preview
 
 ```
 
@@ -3293,7 +3310,7 @@ Status Code: 200
 ## Get - Run Step
 
 ```HTTP
-GET https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/steps/{step_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/steps/{step_id}?api-version=2025-01-01-preview
 ```
 
 Retrieves a run step.
@@ -3333,7 +3350,7 @@ Retrieves a run step.
 Retrieves a run step.
 
 ```HTTP
-GET https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/steps/{step_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/threads/{thread_id}/runs/{run_id}/steps/{step_id}?api-version=2025-01-01-preview
 
 ```
 
@@ -3373,7 +3390,7 @@ Status Code: 200
 ## List - Vector Stores
 
 ```HTTP
-GET https://{endpoint}/openai/vector_stores?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/vector_stores?api-version=2025-01-01-preview
 ```
 
 Returns a list of vector stores.
@@ -3412,7 +3429,7 @@ Returns a list of vector stores.
 Returns a list of vector stores.
 
 ```HTTP
-GET https://{endpoint}/openai/vector_stores?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/vector_stores?api-version=2025-01-01-preview
 
 ```
 
@@ -3462,7 +3479,7 @@ Status Code: 200
 ## Create - Vector Store
 
 ```HTTP
-POST https://{endpoint}/openai/vector_stores?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/vector_stores?api-version=2025-01-01-preview
 ```
 
 Create a vector store.
@@ -3509,7 +3526,7 @@ Create a vector store.
 Creates a vector store.
 
 ```HTTP
-POST https://{endpoint}/openai/vector_stores?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/vector_stores?api-version=2025-01-01-preview
 
 ```
 
@@ -3537,7 +3554,7 @@ Status Code: 200
 ## Get - Vector Store
 
 ```HTTP
-GET https://{endpoint}/openai/vector_stores/{vector_store_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/vector_stores/{vector_store_id}?api-version=2025-01-01-preview
 ```
 
 Retrieves a vector store.
@@ -3573,7 +3590,7 @@ Retrieves a vector store.
 Retrieves a vector store.
 
 ```HTTP
-GET https://{endpoint}/openai/vector_stores/{vector_store_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/vector_stores/{vector_store_id}?api-version=2025-01-01-preview
 
 ```
 
@@ -3592,7 +3609,7 @@ Status Code: 200
 ## Modify - Vector Store
 
 ```HTTP
-POST https://{endpoint}/openai/vector_stores/{vector_store_id}?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/vector_stores/{vector_store_id}?api-version=2025-01-01-preview
 ```
 
 Modifies a vector store.
@@ -3638,7 +3655,7 @@ Modifies a vector store.
 Modifies a vector store.
 
 ```HTTP
-POST https://{endpoint}/openai/vector_stores/{vector_store_id}?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/vector_stores/{vector_store_id}?api-version=2025-01-01-preview
 
 {
  "name": "Support FAQ"
@@ -3670,7 +3687,7 @@ Status Code: 200
 ## Delete - Vector Store
 
 ```HTTP
-DELETE https://{endpoint}/openai/vector_stores/{vector_store_id}?api-version=2024-12-01-preview
+DELETE https://{endpoint}/openai/vector_stores/{vector_store_id}?api-version=2025-01-01-preview
 ```
 
 Delete a vector store.
@@ -3706,7 +3723,7 @@ Delete a vector store.
 Deletes a vector store.
 
 ```HTTP
-DELETE https://{endpoint}/openai/vector_stores/{vector_store_id}?api-version=2024-12-01-preview
+DELETE https://{endpoint}/openai/vector_stores/{vector_store_id}?api-version=2025-01-01-preview
 
 ```
 
@@ -3725,7 +3742,7 @@ Status Code: 200
 ## List - Vector Store Files
 
 ```HTTP
-GET https://{endpoint}/openai/vector_stores/{vector_store_id}/files?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/vector_stores/{vector_store_id}/files?api-version=2025-01-01-preview
 ```
 
 Returns a list of vector store files.
@@ -3766,7 +3783,7 @@ Returns a list of vector store files.
 Returns a list of vector store files.
 
 ```HTTP
-GET https://{endpoint}/openai/vector_stores/{vector_store_id}/files?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/vector_stores/{vector_store_id}/files?api-version=2025-01-01-preview
 
 ```
 
@@ -3800,7 +3817,7 @@ Status Code: 200
 ## Create - Vector Store File
 
 ```HTTP
-POST https://{endpoint}/openai/vector_stores/{vector_store_id}/files?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/vector_stores/{vector_store_id}/files?api-version=2025-01-01-preview
 ```
 
 Create a vector store file by attaching a File to a vector store.
@@ -3845,7 +3862,7 @@ Create a vector store file by attaching a File to a vector store.
 Create a vector store file by attaching a File to a vector store.
 
 ```HTTP
-POST https://{endpoint}/openai/vector_stores/{vector_store_id}/files?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/vector_stores/{vector_store_id}/files?api-version=2025-01-01-preview
 
 {
  "file_id": "file-abc123"
@@ -3872,7 +3889,7 @@ Status Code: 200
 ## Get - Vector Store File
 
 ```HTTP
-GET https://{endpoint}/openai/vector_stores/{vector_store_id}/files/{file_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/vector_stores/{vector_store_id}/files/{file_id}?api-version=2025-01-01-preview
 ```
 
 Retrieves a vector store file.
@@ -3909,7 +3926,7 @@ Retrieves a vector store file.
 Retrieves a vector store file.
 
 ```HTTP
-GET https://{endpoint}/openai/vector_stores/{vector_store_id}/files/{file_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/vector_stores/{vector_store_id}/files/{file_id}?api-version=2025-01-01-preview
 
 ```
 
@@ -3931,7 +3948,7 @@ Status Code: 200
 ## Delete - Vector Store File
 
 ```HTTP
-DELETE https://{endpoint}/openai/vector_stores/{vector_store_id}/files/{file_id}?api-version=2024-12-01-preview
+DELETE https://{endpoint}/openai/vector_stores/{vector_store_id}/files/{file_id}?api-version=2025-01-01-preview
 ```
 
 Delete a vector store file. This will remove the file from the vector store but the file itself won't be deleted. To delete the file, use the delete file endpoint.
@@ -3968,7 +3985,7 @@ Delete a vector store file. This will remove the file from the vector store but
 Delete a vector store file. This will remove the file from the vector store but the file itself won't be deleted. To delete the file, use the delete file endpoint.
 
 ```HTTP
-DELETE https://{endpoint}/openai/vector_stores/{vector_store_id}/files/{file_id}?api-version=2024-12-01-preview
+DELETE https://{endpoint}/openai/vector_stores/{vector_store_id}/files/{file_id}?api-version=2025-01-01-preview
 
 ```
 
@@ -3987,7 +4004,7 @@ Status Code: 200
 ## Create - Vector Store File Batch
 
 ```HTTP
-POST https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches?api-version=2025-01-01-preview
 ```
 
 Create a vector store file batch.
@@ -4032,7 +4049,7 @@ Create a vector store file batch.
 Create a vector store file batch.
 
 ```HTTP
-POST https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches?api-version=2025-01-01-preview
 
 {
  "file_ids": [
@@ -4065,7 +4082,7 @@ Status Code: 200
 ## Get - Vector Store File Batch
 
 ```HTTP
-GET https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches/{batch_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches/{batch_id}?api-version=2025-01-01-preview
 ```
 
 Retrieves a vector store file batch.
@@ -4102,7 +4119,7 @@ Retrieves a vector store file batch.
 Retrieves a vector store file batch.
 
 ```HTTP
-GET https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches/{batch_id}?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches/{batch_id}?api-version=2025-01-01-preview
 
 ```
 
@@ -4130,7 +4147,7 @@ Status Code: 200
 ## Cancel - Vector Store File Batch
 
 ```HTTP
-POST https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel?api-version=2025-01-01-preview
 ```
 
 Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.
@@ -4167,7 +4184,7 @@ Cancel a vector store file batch. This attempts to cancel the processing of file
 Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.
 
 ```HTTP
-POST https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel?api-version=2024-12-01-preview
+POST https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel?api-version=2025-01-01-preview
 
 ```
 
@@ -4195,7 +4212,7 @@ Status Code: 200
 ## List - Vector Store File Batch Files
 
 ```HTTP
-GET https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches/{batch_id}/files?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches/{batch_id}/files?api-version=2025-01-01-preview
 ```
 
 Returns a list of vector store files in a batch.
@@ -4237,7 +4254,7 @@ Returns a list of vector store files in a batch.
 Returns a list of vector store files.
 
 ```HTTP
-GET https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches/{batch_id}/files?api-version=2024-12-01-preview
+GET https://{endpoint}/openai/vector_stores/{vector_store_id}/file_batches/{batch_id}/files?api-version=2025-01-01-preview
 
 ```
 
@@ -4576,20 +4593,38 @@ Information about the content filtering category (hate, sexual, violence, self_h
 | best_of | integer | Generates `best_of` completions server-side and returns the "best" (the one with the highest log probability per token). Results can't be streamed.<br><br>When used with `n`, `best_of` controls the number of candidate completions and `n` specifies how many to return â€“ `best_of` must be greater than `n`.<br><br>**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.<br> | No | 1 |
 | echo | boolean | Echo back the prompt in addition to the completion<br> | No | False |
 | frequency_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.<br> | No | 0 |
-| logit_bias | object | Modify the likelihood of specified tokens appearing in the completion.<br><br>Accepts a JSON object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100.  Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.<br><br>As an example, you can pass `{"50256": -100}` to prevent the <&#124;endoftext&#124;> token from being generated.<br> | No | None |
-| logprobs | integer | Include the log probabilities on the `logprobs` most likely output tokens, as well the chosen tokens. For example, if `logprobs` is 5, the API will return a list of the five most likely tokens. The API will always return the `logprob` of the sampled token, so there may be up to `logprobs+1` elements in the response.<br><br>The maximum value for `logprobs` is 5.<br> | No | None |
-| max_tokens | integer | The maximum number of tokens that can be generated in the completion.<br><br>The token count of your prompt plus `max_tokens` can't exceed the model's context length. <br> | No | 16 |
+| logit_bias | object | Modify the likelihood of specified tokens appearing in the completion.<br><br>Accepts a JSON object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.<br><br>As an example, you can pass `{"50256": -100}` to prevent the <&#124;endoftext&#124;> token from being generated.<br> | No | None |
+| logprobs | integer | Include the log probabilities on the `logprobs` most likely output tokens, as well the chosen tokens. For example, if `logprobs` is 5, the API will return a list of the 5 most likely tokens. The API will always return the `logprob` of the sampled token, so there may be up to `logprobs+1` elements in the response.<br><br>The maximum value for `logprobs` is 5.<br> | No | None |
+| max_tokens | integer | The maximum number of tokens that can be generated in the completion.<br><br>The token count of your prompt plus `max_tokens` can't exceed the model's context length.  | No | 16 |
 | n | integer | How many completions to generate for each prompt.<br><br>**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.<br> | No | 1 |
+| modalities | [ChatCompletionModalities](#chatcompletionmodalities) | Output types that you would like the model to generate for this request.<br>Most models are capable of generating text, which is the default:<br><br>`["text"]`<br><br>The `gpt-4o-audio-preview` model can also be used to generate audio. To<br>request that this model generate both text and audio responses, you can<br>use:<br><br>`["text", "audio"]`<br> | No |  |
+| prediction | [PredictionContent](#predictioncontent) | Configuration for a Predicted Output, which can greatly improve response times when large parts of the model response are known ahead of time. This is most common when you are regenerating a file with only minor changes to most of the content. | No |  |
+| audio | object | Parameters for audio output. Required when audio output is requested with<br>`modalities: ["audio"]`.  | No |  |
 | presence_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.<br> | No | 0 |
 | seed | integer | If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.<br><br>Determinism isn't guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.<br> | No |  |
 | stop | string or array | Up to four sequences where the API will stop generating further tokens. The returned text won't contain the stop sequence.<br> | No |  |
-| stream | boolean | Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. <br> | No | False |
+| stream | boolean | Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message.  | No | False |
 | suffix | string | The suffix that comes after a completion of inserted text.<br><br>This parameter is only supported for `gpt-3.5-turbo-instruct`.<br> | No | None |
 | temperature | number | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.<br><br>We generally recommend altering this or `top_p` but not both.<br> | No | 1 |
 | top_p | number | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br><br>We generally recommend altering this or `temperature` but not both.<br> | No | 1 |
 | user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse.<br> | No |  |
 
 
+### Properties for audio
+
+#### voice
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| voice | string | Specifies the voice type. Supported voices are `alloy`, `echo`, <br>`fable`, `onyx`, `nova`, and `shimmer`.<br> |  |
+
+#### format
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| format | string | Specifies the output audio format. Must be one of `wav`, `mp3`, `flac`,<br>`opus`, or `pcm16`. <br> |  |
+
+
 ### createCompletionResponse
 
 Represents a completion response from the API. Note: both the streamed and non-streamed response objects share the same shape (unlike the chat endpoint).
@@ -4615,17 +4650,17 @@ Represents a completion response from the API. Note: both the streamed and non-s
 |------|------|-------------|----------|---------|
 | temperature | number | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.<br><br>We generally recommend altering this or `top_p` but not both.<br> | No | 1 |
 | top_p | number | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br><br>We generally recommend altering this or `temperature` but not both.<br> | No | 1 |
-| stream | boolean | If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. <br> | No | False |
+| stream | boolean | If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message.  | No | False |
 | stop | string or array | Up to four sequences where the API will stop generating further tokens.<br> | No |  |
-| max_tokens | integer | The maximum number of tokens that can be generated in the chat completion.<br><br>The total length of input tokens and generated tokens is limited by the model's context length. <br> | No |  |
+| max_tokens | integer | The maximum number of tokens that can be generated in the chat completion.<br><br>The total length of input tokens and generated tokens is limited by the model's context length.  | No |  |
 | max_completion_tokens | integer | An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens. This is only supported in o1 series models. Will expand the support to other models in future API release. | No |  |
 | presence_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.<br> | No | 0 |
 | frequency_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.<br> | No | 0 |
 | logit_bias | object | Modify the likelihood of specified tokens appearing in the completion.<br><br>Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.<br> | No | None |
 | store | boolean | Whether or not to store the output of this chat completion request for use in our model distillation or evaluation products. | No |  |
 | metadata | object | Developer-defined tags and values used for filtering completions in the stored completions dashboard. | No |  |
 | user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse.<br> | No |  |
-| messages | array | A list of messages comprising the conversation so far. | Yes |  |
+| messages | array | A list of messages comprising the conversation so far.  | Yes |  |
 | data_sources | array |   The configuration entries for Azure OpenAI chat extensions that use them.<br>  This additional specification is only compatible with Azure OpenAI. | No |  |
 | reasoning_effort | enum | **o1 models only** <br><br> Constrains effort on reasoning for <br>reasoning models.<br><br>Currently supported values are `low`, `medium`, and `high`. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response.<br>Possible values: low, medium, high | No |  |
 | logprobs | boolean | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | No | False |
@@ -4662,7 +4697,7 @@ User security context contains several parameters that describe the AI applicati
 |------|------|-------------|----------|---------|
 | description | string | A description of what the function does, used by the model to choose when and how to call the function. | No |  |
 | name | string | The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. | Yes |  |
-| parameters | [FunctionParameters](#functionparameters) | The parameters the functions accepts, described as a JSON Schema object. See the guide](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. <br><br>Omitting `parameters` defines a function with an empty parameter list. | No |  |
+| parameters | [FunctionParameters](#functionparameters) | The parameters the functions accepts, described as a JSON Schema object. [See the guide](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. <br><br>Omitting `parameters` defines a function with an empty parameter list. | No |  |
 
 
 ### chatCompletionFunctionCallOption
@@ -4743,7 +4778,7 @@ With o1 models and newer, `developer` messages replace the previous `system` mes
 
 | Name | Type | Description | Default |
 |------|------|-------------|--------|
-| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model doesn't always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. |  |
+| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. |  |
 
 #### name
 
@@ -4819,6 +4854,30 @@ This component can be one of the following:
 | text | string | The text content. | Yes |  |
 
 
+### chatCompletionRequestMessageContentPartAudio
+
+
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| type | enum | The type of the content part. Always `input_audio`.<br>Possible values: input_audio | Yes |  |
+| input_audio | object |  | Yes |  |
+
+
+### Properties for input_audio
+
+#### data
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| data | string | Base64 encoded audio data. |  |
+
+#### format
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| format | string | The format of the encoded audio data. Currently supports "wav" and "mp3".<br> |  |
+
+
 ### chatCompletionRequestMessageContentPartImage
 
 
@@ -4981,7 +5040,7 @@ MongoDB vCore.
 |------|------|-------------|----------|---------|
 | authentication | [onYourDataConnectionStringAuthenticationOptions](#onyourdataconnectionstringauthenticationoptions) | The authentication options for Azure OpenAI On Your Data when using a connection string. | Yes |  |
 | top_n_documents | integer | The configured top number of documents to feature for the configured query. | No |  |
-| max_search_queries | integer | The max number of rewritten queries that should be sent to search provider for one user message. If not specified, the system will decide the number of queries to send. | No |  |
+| max_search_queries | integer | The max number of rewritten queries should be send to search provider for one user message. If not specified, the system will decide the number of queries to send. | No |  |
 | allow_partial_result | boolean | If specified as true, the system will allow partial search results to be used and the request fails if all the queries fail. If not specified, or specified as false, the request will fail if any search query fails. | No | False |
 | in_scope | boolean | Whether queries should be restricted to use of indexed data. | No |  |
 | strictness | integer | The configured strictness of the search relevance filtering. The higher of strictness, the higher of the precision but lower recall of the answer. | No |  |
@@ -5464,7 +5523,7 @@ The filtering reason of the retrieved document.
 
 | Name | Type | Description | Default |
 |------|------|-------------|--------|
-| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model doesn't always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. |  |
+| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. |  |
 
 
 ### toolCallType
@@ -5556,7 +5615,7 @@ A chat completion delta generated by streamed model responses.
 
 | Name | Type | Description | Default |
 |------|------|-------------|--------|
-| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model doesn't always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. |  |
+| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. |  |
 
 #### name
 
@@ -5589,7 +5648,7 @@ A chat completion delta generated by streamed model responses.
 
 | Name | Type | Description | Default |
 |------|------|-------------|--------|
-| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model doesn't always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. |  |
+| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. |  |
 
 
 ### chatCompletionStreamOptions
@@ -5635,9 +5694,37 @@ A chat completion message generated by the model.
 | content | string | The contents of the message. | Yes |  |
 | tool_calls | array | The tool calls generated by the model, such as function calls. | No |  |
 | function_call | [chatCompletionFunctionCall](#chatcompletionfunctioncall) | Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model. | No |  |
+| audio | object | If the audio output modality is requested, this object contains data<br>about the audio response from the model.  | No |  |
 | context | [azureChatExtensionsMessageContext](#azurechatextensionsmessagecontext) |   A representation of the additional context information available when Azure OpenAI chat extensions are involved<br>  in the generation of a corresponding chat completions response. This context information is only populated when<br>  using an Azure OpenAI request configured to use a matching extension. | No |  |
 
 
+### Properties for audio
+
+#### id
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| id | string | Unique identifier for this audio response. |  |
+
+#### expires_at
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| expires_at | integer | The Unix timestamp (in seconds) for when this audio response will<br>no longer be accessible on the server for use in multi-turn<br>conversations.<br> |  |
+
+#### data
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| data | string | Base64 encoded audio bytes generated by the model, in the format<br>specified in the request.<br> |  |
+
+#### transcript
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| transcript | string | Transcript of the audio generated by the model. |  |
+
+
 ### chatCompletionResponseMessageRole
 
 The role of the author of the response message.
@@ -5686,21 +5773,48 @@ Whether to enable parallel function calling during tool use.
 No properties defined for this component.
 
 
+### PredictionContent
+
+Static predicted output content, such as the content of a text file that is being regenerated.
+
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| type | enum | The type of the predicted content you want to provide. This type is currently always `content`.<br>Possible values: content | Yes |  |
+| content | string or array | The content that should be matched when generating a model response. If generated tokens would match this content, the entire model response can be returned much more quickly. | Yes |  |
+
+
 ### chatCompletionMessageToolCalls
 
 The tool calls generated by the model, such as function calls.
 
 No properties defined for this component.
 
 
+### ChatCompletionModalities
+
+Output types that you would like the model to generate for this request.
+Most models are capable of generating text, which is the default:
+
+`["text"]`
+
+The `gpt-4o-audio-preview` model can also be used to generate audio. To
+request that this model generate both text and audio responses, you can
+use:
+
+`["text", "audio"]`
+
+
+No properties defined for this component.
+
+
 ### chatCompletionFunctionCall
 
 Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
 | name | string | The name of the function to call. | Yes |  |
-| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model doesn't always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. | Yes |  |
+| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. | Yes |  |
 
 
 ### completionUsage
@@ -5718,6 +5832,12 @@ Usage statistics for the completion request.
 
 ### Properties for prompt_tokens_details
 
+#### audio_tokens
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| audio_tokens | integer | Audio input tokens present in the prompt. |  |
+
 #### cached_tokens
 
 | Name | Type | Description | Default |
@@ -5727,12 +5847,30 @@ Usage statistics for the completion request.
 
 ### Properties for completion_tokens_details
 
+#### accepted_prediction_tokens
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| accepted_prediction_tokens | integer | When using Predicted Outputs, the number of tokens in the prediction that appeared in the completion. |  |
+
+#### audio_tokens
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| audio_tokens | integer | Audio input tokens generated by the model. |  |
+
 #### reasoning_tokens
 
 | Name | Type | Description | Default |
 |------|------|-------------|--------|
 | reasoning_tokens | integer | Tokens generated by the model for reasoning. |  |
 
+#### rejected_prediction_tokens
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| rejected_prediction_tokens | integer | When using Predicted Outputs, the number of tokens in the prediction that did not appear in the completion. However, like reasoning tokens, these tokens are still counted in the total  completion tokens for purposes of billing, output, and context window limits. |  |
+
 
 ### chatCompletionTool
 
@@ -5746,7 +5884,7 @@ Usage statistics for the completion request.
 
 ### FunctionParameters
 
-The parameters the functions accepts, described as a JSON Schema object. See the guide](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. 
+The parameters the functions accepts, described as a JSON Schema object. [See the guide](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. 
 
 Omitting `parameters` defines a function with an empty parameter list.
 
@@ -5761,7 +5899,7 @@ No properties defined for this component.
 |------|------|-------------|----------|---------|
 | description | string | A description of what the function does, used by the model to choose when and how to call the function. | No |  |
 | name | string | The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. | Yes |  |
-| parameters | [FunctionParameters](#functionparameters) | The parameters the functions accepts, described as a JSON Schema object. See the guide](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. <br><br>Omitting `parameters` defines a function with an empty parameter list. | No |  |
+| parameters | [FunctionParameters](#functionparameters) | The parameters the functions accepts, described as a JSON Schema object. [See the guide](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. <br><br>Omitting `parameters` defines a function with an empty parameter list. | No |  |
 | strict | boolean | Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. | No | False |
 
 
@@ -6170,7 +6308,7 @@ Represents an `assistant` that can call the model and use tools.
 
 | Name | Type | Description | Default |
 |------|------|-------------|--------|
-| file_ids | array | A list of file IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.<br> | [] |
+| file_ids | array | A list of file IDs made available to the `code_interpreter`` tool. There can be a maximum of 20 files associated with the tool.<br> | [] |
 
 #### file_search
 
@@ -6375,7 +6513,7 @@ Represents an `assistant` that can call the model and use tools.
 
 | Name | Type | Description | Default |
 |------|------|-------------|--------|
-| parameters | [chatCompletionFunctionParameters](#chatcompletionfunctionparameters) | The parameters the functions accepts, described as a JSON Schema object. See the [guide/](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. |  |
+| parameters | [chatCompletionFunctionParameters](#chatcompletionfunctionparameters) | The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. |  |
 
 
 
@@ -6640,7 +6778,7 @@ Tool call objects
 |------|------|-------------|----------|---------|
 | assistant_id | string | The ID of the assistant to use to execute this run. | Yes |  |
 | thread | [createThreadRequest](#createthreadrequest) |  | No |  |
-| model | string | The ID of the Model to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used. | No |  |
+| model | string | The ID of the model to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used. | No |  |
 | instructions | string | Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis. | No |  |
 | tools | array | Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis. | No |  |
 | tool_resources | object | A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.<br> | No |  |
@@ -7209,7 +7347,7 @@ Represents a step in execution of a run.
 | created_at | integer | The Unix timestamp (in seconds) for when the run step was created. | Yes |  |
 | assistant_id | string | The ID of the assistant associated with the run step. | Yes |  |
 | thread_id | string | The ID of the thread that was run. | Yes |  |
-| run_id | string | The ID of the run) that this run step is a part of. | Yes |  |
+| run_id | string | The ID of the run that this run step is a part of. | Yes |  |
 | type | string | The type of run step, which can be either `message_creation` or `tool_calls`. | Yes |  |
 | status | string | The status of the run, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`. | Yes |  |
 | step_details | [runStepDetailsMessageCreationObject](#runstepdetailsmessagecreationobject) or [runStepDetailsToolCallsObject](#runstepdetailstoolcallsobject) | The details of the run step. | Yes |  |
@@ -7647,7 +7785,7 @@ A result instance of the file search.
 
 | Name | Type | Description | Default |
 |------|------|-------------|--------|
-| output | string | The output of the function. This will be `null` if the outputs have not been submitted yet. |  |
+| output | string | The output of the function. This will be `null` if the outputs have not been [submitted](/docs/api-reference/runs/submitToolOutputs) yet. |  |
 
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新の推論プレビュードキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAIの最新の推論プレビューに関するドキュメントを更新したものです。変更の主なポイントは、APIのバージョンが「2024-12-01プレビュー」から「2025-01-01プレビュー」に更新されたことです。また、新しいAPIバージョンに対応するために、複数のエンドポイントについての説明が追加され、一部のパラメーターも変更されています。

さらに、音声出力や予測出力に関連する新しいプロパティが導入され、それにより開発者がモデルの応答時間を改善するために活用できる情報が強化されています。この修正により、開発者は最新の機能や仕様に基づいた実装を行う際に必要なガイダンスを受け取ることができ、Azure OpenAIサービスの利用がよりスムーズに行えるようになります。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -9,30 +9,31 @@ ms.custom: references_regions
 ms.date: 01/15/2025
 ---
 
-| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|
-| australiaeast      | ✅                       | ✅                       | ✅                            |
-| brazilsouth        | ✅                       | ✅                       | ✅                            |
-| canadacentral      | ✅                       | ✅                       | ✅                            |
-| canadaeast         | ✅                       | ✅                       | ✅                            |
-| eastus             | ✅                       | ✅                       | ✅                            |
-| eastus2            | ✅                       | ✅                       | ✅                            |
-| francecentral      | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | ✅                       | ✅                       | ✅                            |
-| japaneast          | ✅                       | ✅                       | ✅                            |
-| koreacentral       | ✅                       | ✅                       | ✅                            |
-| northcentralus     | ✅                       | ✅                       | ✅                            |
-| norwayeast         | ✅                       | ✅                       | ✅                            |
-| polandcentral      | ✅                       | ✅                       | ✅                            |
-| southafricanorth   | ✅                       | ✅                       | ✅                            |
-| southcentralus     | ✅                       | ✅                       | ✅                            |
-| southindia         | ✅                       | ✅                       | ✅                            |
-| spaincentral       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | ✅                       | ✅                       | ✅                            |
-| switzerlandnorth   | ✅                       | ✅                       | ✅                            |
-| switzerlandwest    | ✅                       | ✅                       | ✅                            |
-| uaenorth           | ✅                       | ✅                       | ✅                            |
-| uksouth            | ✅                       | ✅                       | ✅                            |
-| westeurope         | ✅                       | ✅                       | ✅                            |
-| westus             | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
+| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
+| australiaeast      | ✅                       | ✅                       | -                      | ✅                            |
+| brazilsouth        | ✅                       | ✅                       | -                      | ✅                            |
+| canadacentral      | ✅                       | ✅                       | -                      | ✅                            |
+| canadaeast         | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus             | ✅                       | ✅                       | -                      | ✅                            |
+| eastus2            | ✅                       | ✅                       | -                      | ✅                            |
+| francecentral      | ✅                       | ✅                       | -                      | ✅                            |
+| germanywestcentral | ✅                       | ✅                       | -                      | ✅                            |
+| japaneast          | ✅                       | ✅                       | -                      | ✅                            |
+| koreacentral       | ✅                       | ✅                       | -                      | ✅                            |
+| northcentralus     | ✅                       | ✅                       | -                      | ✅                            |
+| norwayeast         | ✅                       | ✅                       | -                      | ✅                            |
+| polandcentral      | ✅                       | ✅                       | -                      | ✅                            |
+| southafricanorth   | ✅                       | ✅                       | -                      | ✅                            |
+| southcentralus     | ✅                       | ✅                       | -                      | ✅                            |
+| southeastasia      | ✅                       | ✅                       | -                      | ✅                            |
+| southindia         | ✅                       | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                       | ✅                       | -                      | ✅                            |
+| swedencentral      | ✅                       | ✅                       | -                      | ✅                            |
+| switzerlandnorth   | ✅                       | ✅                       | -                      | ✅                            |
+| switzerlandwest    | ✅                       | ✅                       | -                      | ✅                            |
+| uaenorth           | ✅                       | ✅                       | -                      | ✅                            |
+| uksouth            | ✅                       | ✅                       | -                      | ✅                            |
+| westeurope         | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                       | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新のgpt-4oリリースの地域情報更新"
}
```

### Explanation
この変更は、Azure OpenAIモデルの提供地域に関するドキュメントの最新化を反映しています。具体的には、表において新たに「gpt-4o」モデルの2024年11月20日のリリース日が追加され、各地域における利用可能な状態が示されています。

従来の情報と比較して、特定の地域（たとえば、australiaeast、brazilsouthなど）において、gpt-4oの新しいリリースが提供されないことを示すために「-」マークが導入されました。また、gpt-4o-miniモデルは変わらず利用可能であることが確認されています。このような更新は、開発者やユーザーが最新のモデルリリースに基づいた地域の可用性を迅速に理解できるようにするために重要です。

## articles/ai-services/openai/reference-preview.md{#item-e197a2}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's latest preview REST API. In this ar
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 10/16/2024
+ms.date: 01/29/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -20,7 +20,7 @@ This article provides details on the inference REST API endpoints for Azure Open
 
 ## Data plane inference
 
-The rest of the article covers the latest preview release of the Azure OpenAI data plane inference specification, `2024-10-01-preview`. This article includes documentation for the latest preview capabilities like assistants, threads, and vector stores.
+The rest of the article covers the latest preview release of the Azure OpenAI data plane inference specification, `2025-01-01-preview`. This article includes documentation for the latest preview capabilities like assistants, threads, and vector stores.
 
 If you're looking for documentation on the latest GA API release, refer to the [latest GA data plane inference API](./reference.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI REST APIのプレビュー日付更新"
}
```

### Explanation
この変更は、Azure OpenAIの最新のプレビューREST APIに関するドキュメントの更新です。具体的には、文書内の「ms.date」フィールドが2024年10月16日から2025年1月29日に更新されています。これは、記事の情報が現行のリリースに適合していることを示すための変更です。

さらに、データプレーン推論仕様の最新プレビューリリースのバージョンが、2024年10月1日から2025年1月1日プレビューに変更されました。これにより、読者は最新の機能、アシスタント、スレッド、ベクトルストアに関する情報を正確に入手できるようになります。このような更新は、開発者やユーザーが最新のAPIの状態を把握しやすくするために重要です。

## articles/ai-services/openai/reference.md{#item-7b1183}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's REST API. In this article, you lear
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 11/01/2024
+ms.date: 01/29/2025
 author: mrbullwinkle 
 ms.author: mbullwin
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI REST APIのドキュメント日付更新"
}
```

### Explanation
この変更は、Azure OpenAI REST APIに関するドキュメントの更新を示しています。具体的には、文書内の「ms.date」フィールドが2024年11月1日から2025年1月29日に変更されました。この日付の更新は、ドキュメントが最新の情報を反映していることを示し、ユーザーに対して正確なリファレンスを提供することを目的としています。

この修正は、開発者やユーザーがAPIの最新版に基づいて重要な情報を得やすくするために重要で、ドキュメントの信頼性と正確性を保つための一般的なメンテナンス作業です。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -136,6 +136,8 @@ items:
       href: ./how-to/completions.md
     - name: JSON mode
       href: ./how-to/json-mode.md
+    - name: Predicted outputs
+      href: ./how-to/predicted-outputs.md
     - name: Prompt caching
       href: ./how-to/prompt-caching.md
     - name: Reproducible output
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新: 予測出力に関する項目追加"
}
```

### Explanation
この変更は、Azure OpenAIに関するドキュメントの目次（toc.yml）における更新を示しています。具体的には、目次に「Predicted outputs」という新しい項目が追加され、そのリンクが「./how-to/predicted-outputs.md」に設定されました。

この更新により、ユーザーは予測出力に関する情報にアクセスしやすくなり、関連するドキュメントを見つけるためのナビゲーションが改善されます。このような小さな更新は、ユーザーエクスペリエンスを向上させるために重要です。


