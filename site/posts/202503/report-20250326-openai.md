---
date: '2025-03-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7af2ef0...MicrosoftDocs:e737b2f
summary: このコードの変更は、Azure OpenAIサービスのドキュメントに対するマイナーアップデートおよび新機能の追加を含む大規模な修正を行ったものです。新たに「Responses
  API」や「computer-use-preview」モデルに関する情報が追加され、既存のドキュメントは最新仕様に対応しています。Responses APIはチャット完了やアシスタントAPIを統合した新しいステートフルAPIで、computer-use-previewモデルのサポートも追加されました。破壊的な変更はなく、利用者はシステムを更新しない限り新機能にアクセスできない可能性があります。その他、リリース情報やアップグレードに関する日付の更新、情報アクセスの利便性向上が図られています。全体として、これらの変更は互換性や利便性を強化し、開発者に新しいインタラクションの方法を提供するものです。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7af2ef0...MicrosoftDocs:e737b2f){target="_blank"}

<format>
# ハイライト
このコードの変更は、Azure OpenAIサービスのドキュメント全体を対象としたマイナーアップデートおよび新機能の追加を含む、大規模な修正を行ったものです。新たに「Responses API」や「computer-use-preview」モデルに関する情報が追加されました。また、既存のドキュメントについても最新仕様への対応が行われています。

## 新機能
- **Responses API** という新しいステートフルAPIが追加されました。これは、チャット完了やアシスタントAPIの機能を統合したもので、新しい「computer-use-preview」モデルを含む、より高度なインタラクションが可能になりました。
- **computer-use-previewモデル**のサポートが追加され、これによりアプリケーションとインタラクションが可能になります。登録が必要である旨も明記されています。

## 破壊的変更
特に破壊的な変更は見られませんが、モデルやAPIバージョン対応に関する情報が最新化されたため、利用者がシステムを更新しない限り、いくつかの新機能にアクセスできない可能性があります。

## その他の更新
- 本文の日付やリリース情報の更新。
- モデルの退役およびアップグレードに関する日付の変更。
- プロンプトキャッシング、クォータと制限の情報が更新され、新モデルが追加。
- OpenAIサービスの目次が整理され、アクセス可能な情報の利便性が向上。

# インサイト
Azure OpenAIサービス向けのドキュメントで行われた変更点は、今後の利用における互換性や利便性を強化する内容が多く含まれています。特に、Responses APIとcomputer-use-previewモデルの追加は注目に値します。これらの新機能はエージェントがアプリケーションに直接インタラクションする方法を提供し、新たな開発やルーチンの自動化に活用できる可能性があります。

開発者にとっては、これまでのAIモデルの枠を越えてより多様な機能を迅速に試すことができるため、新機能の試験的な適用や差別化に有効です。また、地域的な可用性の指定やメタデータの正確な更新により、グローバルでの展開計画が立てやすくなりました。

さらに、ドキュメント更新により、用語の整理、そして情報へのアクセス向上を挙るための整理整頓が施されており、開発や運用においてドキュメントを参照しやすくなっています。これらの調整は、Azure OpenAIプラットフォームをより使いやすくするための一環と言えるでしょう。今後、これらの改善がサービス全体にどのような影響を与えるか見守る必要がありますが、現時点では利用者としては期待と注目に値する内容です。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [api-version-deprecation.md](#item-1cad50) | minor update | APIバージョンの更新に関するドキュメントの修正 | modified | 9 | 3 | 12 | 
| [model-retirements.md](#item-03fc2e) | minor update | モデルの退役に関する情報の更新 | modified | 4 | 4 | 8 | 
| [models.md](#item-db2c37) | minor update | モデル情報の追加と更新 | modified | 30 | 1 | 31 | 
| [computer-use.md](#item-6fbca8) | new feature | コンピュータ使用に関する新しいガイドの追加 | added | 366 | 0 | 366 | 
| [prompt-caching.md](#item-1631df) | minor update | プロンプトキャッシングに関する情報の更新 | modified | 8 | 7 | 15 | 
| [responses.md](#item-b9757d) | new feature | Azure OpenAIのレスポンスAPIに関する新しいドキュメントの追加 | added | 1477 | 0 | 1477 | 
| [api-surface.md](#item-a25fa2) | minor update | データプレーンAPIの著作および推論のバージョン更新 | modified | 2 | 2 | 4 | 
| [latest-inference-preview.md](#item-24bf0f) | minor update | 最新の推論プレビューAPIに関するドキュメントの更新 | modified | 2944 | 2351 | 5295 | 
| [standard-global.md](#item-17a84b) | minor update | 標準グローバルモデルマトリックスの更新 | modified | 21 | 21 | 42 | 
| [overview.md](#item-97d507) | minor update | OpenAI サービスの概要ドキュメントの更新 | modified | 2 | 2 | 4 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータと制限に関するドキュメントの更新 | modified | 13 | 7 | 20 | 
| [reference-preview.md](#item-e197a2) | minor update | Azure OpenAI の参照プレビュードキュメントの更新 | modified | 2 | 2 | 4 | 
| [toc.yml](#item-c945af) | minor update | OpenAI サービスの目次ファイルの更新 | modified | 6 | 1 | 7 | 
| [whats-new.md](#item-53303b) | new feature | Azure OpenAIの新機能に関する更新 | modified | 10 | 0 | 10 | 


# Modified Contents
## articles/ai-services/openai/api-version-deprecation.md{#item-1cad50}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 02/28/2025
+ms.date: 03/25/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -24,11 +24,12 @@ This article is to help you understand the support lifecycle for the Azure OpenA
 
 Azure OpenAI API latest release:
 
-- Inference: [2025-02-01-preview](reference-preview.md)
-- Authoring: [2025-02-01-preview](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/2025-02-01-preview/azureopenai.json)
+- Inference: [2025-03-01-preview](reference-preview.md)
+- Authoring: [2025-03-01-preview](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/)
 
 This version contains support for the latest Azure OpenAI features including:
 
+- [Responses API & support for `computer-use-preview` model](./how-to/responses.md) [**Added in 2025-03-01-preview**]
 - [Stored Completions (distillation) API](./how-to/stored-completions.md#stored-completions-api) [**Added in 2025-02-01-preview**]
 - [Predicted Outputs](./how-to/predicted-outputs.md) [**Added in 2025-01-01-preview**]
 - [Reasoning models](./how-to/reasoning.md) [**Added in 2024-12-01-preview**]
@@ -43,6 +44,11 @@ This version contains support for the latest Azure OpenAI features including:
 - [Function calling](./how-to/function-calling.md)  [**Added in 2023-07-01-preview**]
 - [Retrieval augmented generation with your data feature](./use-your-data-quickstart.md).  [**Added in 2023-06-01-preview**]
 
+## Changes between 2025-03-01-preview and 2025-02-01-preview
+
+- [Responses API](./how-to/responses.md)
+- [Computer use](./how-to/computer-use.md)
+
 ## Changes between 2025-02-01-preview and 2025-01-01-preview
 
 - [Stored completions (distillation)](./how-to/stored-completions.md#stored-completions-api) API support.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新に関するドキュメントの修正"
}
```

### Explanation
このコードの変更は、Azure OpenAI APIのバージョンに関するドキュメントを更新するもので、主に日付やリリース情報の変更が含まれています。この修正では、リリース日が2025年2月1日から2025年3月1日に変更され、関連する情報が更新されています。また、"Responses API"と"computer-use"モデルに関する新しいセクションが追加され、2025年3月1日プレビューにおける変更点も記載されています。これにより、最新の機能やAPIのサポート内容が文書に反映され、利用者に対してより正確な情報が提供されるようになっています。

## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 03/11/2025
+ms.date: 03/24/2025
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -100,9 +100,9 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-4`<br>`gpt-4-32k` | 0314 | June 6, 2025 | `gpt-4o` |
 | `gpt-4`<br>`gpt-4-32k` | 0613 | June 6, 2025 | `gpt-4o` |
 | `gpt-4` | turbo-2024-04-09 | No earlier than June 6, 2025 | `gpt-4o`|
-| `gpt-4` | 1106-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than March 10, 2025 **<sup>1</sup>** <br>Retirement date: May 1, 2025  | `gpt-4o`|
-| `gpt-4` | 0125-preview |To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than March 10, 2025 **<sup>1</sup>** <br>Retirement date: May 1, 2025  | `gpt-4o` |
-| `gpt-4` | vision-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than March 10, 2025  **<sup>1</sup>** <br>Retirement date: May 1, 2025 | `gpt-4o`|
+| `gpt-4` | 1106-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025 **<sup>1</sup>** <br>Retirement date: May 1, 2025  | `gpt-4o`|
+| `gpt-4` | 0125-preview |To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025 **<sup>1</sup>** <br>Retirement date: May 1, 2025  | `gpt-4o` |
+| `gpt-4` | vision-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025  **<sup>1</sup>** <br>Retirement date: May 1, 2025 | `gpt-4o`|
 | `gpt-4o` | 2024-05-13 | No earlier than June 30, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on March 17, 2025. | |
 | `gpt-4o` | 2024-08-06 | No earlier than August 6, 2025  | |
 | `gpt-4o` | 2024-11-20 | No earlier than November 20, 2025  | |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの退役に関する情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIにおけるモデルの退役に関するドキュメントを更新するものであり、主に日付やリリース情報が変更されています。特に、モデルのアップグレードが開始される日付が2025年3月10日から2025年4月17日に変更され、関連する情報が更新されました。この修正により、ユーザーは新しいモデルバージョンのスケジュールを確認できるようになり、モデルの利用について最新の情報を得ることができます。また、文書全体にわたって小規模な修正が行われており、全体の整合性が保たれています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 2/27/2025
+ms.date: 03/25/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -18,6 +18,7 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 
 | Models | Description |
 |--|--|
+| [computer-use-preview](#computer-use-preview) | An experimental model trained for use with the Responses API computer use tool. |
 | [GPT-4.5 Preview](#gpt-45-preview) |The latest GPT model that excels at diverse text and image tasks.  |
 | [o-series models](#o-series-models) |[Reasoning models](../how-to/reasoning.md) with advanced problem-solving and increased focus and capability.  |
 | [GPT-4o & GPT-4o mini & GPT-4 Turbo](#gpt-4o-and-gpt-4-turbo) | The latest most capable Azure OpenAI models with multimodal versions, which can accept both text and images as input. |
@@ -29,6 +30,34 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 | [Whisper](#whisper-models) | A series of models in preview that can transcribe and translate speech to text. |
 | [Text to speech](#text-to-speech-models-preview) (Preview) | A series of models in preview that can synthesize text to speech. |
 
+## computer-use-preview
+
+An experimental model trained for use with the [Responses API](../how-to/responses.md) computer use tool. It can be used in conjunction with 3rd-party libraries to allow the model to control mouse & keyboard input while getting context from screenshots of the current environment.
+
+> [!CAUTION]
+> We don't recommend using preview models in production. We will upgrade all deployments of preview models to either future preview versions or to the latest stable GA version. Models that are designated preview don't follow the standard Azure OpenAI model lifecycle.
+
+### Availability
+
+**For access to `computer-use-preview` registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who have access to other limited access models will still need to request access for this model.
+
+Request access: [`computer-use-preview` limited access model application](https://aka.ms/oai/cuaaccess)
+
+Once access has been granted, you will need to create a deployment for the model.
+
+### Region Availability
+
+| Model | Region |
+|---|---|
+| `computer-use-preview` | East US 2 (Global Standard) <br> South India (Global Standard) <br> Sweden Central (Global Standard) |
+
+### Capabilities
+
+|  Model ID  | Description | Context Window | Max Output Tokens | Training Data (up to)  |
+|  --- |  :--- |:--- |:---|:---: |
+| `computer-use-preview` (2025-03-11)  | Specialized model for use with the [Responses API](../how-to/responses.md) computer use tool <br> <br>-Tools <br>-Streaming<br>-Text(input/output)<br>- Image(input)   | 8,192 | 1,024 | Oct 2023 |
+
+
 ## GPT-4.5 Preview
 
 ### Availability
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル情報の追加と更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIに関するモデルの情報を更新し、新しいモデルに関する詳細を追加するもので、特に「computer-use-preview」という実験的なモデルが追加されました。このモデルは、Responses APIと連携して、マウスやキーボードの入力を制御しながら、現在の環境のスクリーンショットから文脈を取得する機能を持っています。また、このモデルを利用するための登録手続きや地域の可用性、モデルの能力といった情報も明確に記載されています。

さらに、メタデータの更新として、文書の日付が2025年2月27日から2025年3月25日に変更され、他のモデルに関する説明も強化されています。これにより、利用者は新しいモデルの特性や利用方法について、より包括的な情報を得ることができます。変更された内容は、モデルの採用を検討しているユーザーにとって重要なインサイトを提供します。

## articles/ai-services/openai/how-to/computer-use.md{#item-6fbca8}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,366 @@
+---
+title: 'Computer Use (preview) in Azure OpenAI'
+titleSuffix: Azure OpenAI
+description: Learn about Computer Use in Azure OpenAI which allows AI to interact with computer applications.
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: how-to
+ms.date: 03/25/2025
+author: aahill
+ms.author: aahi
+---
+
+# Computer Use (preview) in Azure OpenAI
+
+Use this article to learn how to work with Computer Use in Azure OpenAI. Computer Use is a specialized AI tool that uses a specialized model that can perform tasks by interacting with computer systems and applications through their UIs. With Computer Use, you can create an agent that can handle complex tasks and make decisions by interpreting visual elements and taking action based on on-screen content. 
+
+Computer Use provides:
+
+* **Autonomous navigation**: For example, opens applications, clicks buttons, fills out forms, and navigates multi-page workflows.
+* **Dynamic adaptation**: Interprets UI changes and adjusts actions accordingly.
+* **Cross-application task execution**: Operates across web-based and desktop applications.
+* **Natural language interface**: Users can describe a task in plain language, and the Computer Use model determines the correct UI interactions to execute.   
+
+## Request access
+
+For access to the `computer-use-preview` model, registration is required and access will be granted based on Microsoft's eligibility criteria. Customers who have access to other limited access models will still need to request access for this model.
+
+Request access: [computer-use-preview limited access model application](https://aka.ms/oai/cuaaccess)
+
+Once access has been granted, you will need to create a deployment for the model.
+
+## Regional support
+
+Computer Use is available in the following regions:
+* `eastus2`
+* `swedencentral`
+* `southindia`
+
+## Sending an API call to the Computer Use model using the responses API
+
+The Computer Use tool is accessed through the [responses API](./responses.md). The tool operates in a continuous loop that sends actions such as typing text or performing a click. Your code executes these actions on a computer, and sends screenshots of the outcome to the model. 
+
+In this way, your code simulates the actions of a human using a computer interface, while the model uses the screenshots to understand the state of the environment and suggest next actions.
+
+The following examples show a basic API call. 
+
+> [!NOTE]
+> You need an Azure OpenAI resource with a `computer-use-preview` model deployment in a [supported region](#regional-support).
+
+## [Python](#tab/python)
+
+To send requests, you will need to install the following Python packages.
+
+```console
+pip install openai
+pip install azure-identity
+```
+
+```python
+import os
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+from openai import AzureOpenAI
+
+#from openai import OpenAI
+token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")
+
+client = AzureOpenAI(
+    azure_ad_token_provider=token_provider,
+    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
+    api_version="2025-03-01-preview"
+)
+
+response = client.responses.create(
+    model="computer-use-preview", # set this to your model deployment name
+    tools=[{
+        "type": "computer_use_preview",
+        "display_width": 1024,
+        "display_height": 768,
+        "environment": "browser" # other possible values: "mac", "windows", "ubuntu"
+    }],
+    input=[
+        {
+            "role": "user",
+            "content": "Check the latest AI news on bing.com."
+        }
+    ],
+    truncation="auto"
+)
+
+print(response.output)
+```
+
+### Output
+
+```console
+[
+    ResponseComputerToolCall(
+        id='cu_67d841873c1081908bfc88b90a8555e0', 
+        action=ActionScreenshot(type='screenshot'), 
+        call_id='call_wwEnfFDqQr1Z4Edk62Fyo7Nh', 
+        pending_safety_checks=[], 
+        status='completed', 
+        type='computer_call'
+    )
+]
+```
+
+## [REST API](#tab/rest-api)
+
+```bash
+curl ${MY_ENDPOINT}/openai/responses?api-version=2025-03-01-preview \ 
+  -H "Content-Type: application/json" \ 
+  -H "api-key: $MY_API_KEY" \ 
+  -d '{ 
+    "model": "computer-use-preview", 
+    "input": [ 
+      { 
+        "type": "message", 
+        "role": "user", 
+        "content": "Check the latest AI news on bing.com." 
+      }
+    ],
+    "tools": [{
+        "type": "computer_use_preview",
+        "display_width": 1024,
+        "display_height": 768,
+        "environment": "browser" 
+    }],
+    "truncation":"auto"
+  }' 
+```
+
+### Output
+
+```json
+{
+  "id": "resp_xxxxxxxxxxxxxxxxxxxxxxxx",
+  "object": "response",
+  "created_at": 1742227653,
+  "status": "completed",
+  "error": null,
+  "incomplete_details": null,
+  "instructions": null,
+  "max_output_tokens": null,
+  "model": "computer-use-preview",
+  "output": [
+    {
+      "type": "computer_call",
+      "id": "cu_xxxxxxxxxxxxxxxxxxxxxxxxxx",
+      "call_id": "call_xxxxxxxxxxxxxxxxxxxxxxx",
+      "action": {
+        "type": "screenshot"
+      },
+      "pending_safety_checks": [],
+      "status": "completed"
+    }
+  ],
+  "parallel_tool_calls": true,
+  "previous_response_id": null,
+  "reasoning": {
+    "effort": "medium",
+    "generate_summary": null
+  },
+  "store": true,
+  "temperature": 1.0,
+  "text": {
+    "format": {
+      "type": "text"
+    }
+  },
+  "tools": [
+    {
+      "type": "computer_use_preview",
+      "display_height": 768,
+      "display_width": 1024,
+      "environment": "browser"
+    }
+  ],
+  "top_p": 1.0,
+  "truncation": "auto",
+  "usage": {
+    "input_tokens": 519,
+    "input_tokens_details": {
+      "cached_tokens": 0
+    },
+    "output_tokens": 7,
+    "output_tokens_details": {
+      "reasoning_tokens": 0
+    },
+    "total_tokens": 526
+  },
+  "user": null,
+  "metadata": {}
+}
+```
+
+---
+
+Once the initial API request is sent, you perform a loop where the specified action is performed in your application code, sending a screenshot with each turn so the model can evaluate the updated state of the environment.
+
+## [Python](#tab/python)
+
+```python
+
+## response.output is the previous response from the model
+computer_calls = [item for item in response.output if item.type == "computer_call"]
+if not computer_calls:
+    print("No computer call found. Output from model:")
+    for item in response.output:
+        print(item)
+
+computer_call = computer_calls[0]
+last_call_id = computer_call.call_id
+action = computer_call.action
+
+# Your application would now perform the action suggested by the model
+# And create a screenshot of the updated state of the environment before sending another response
+
+response_2 = client.responses.create(
+    model="computer-use-preview",
+    previous_response_id=response.id,
+    tools=[{
+        "type": "computer-preview",
+        "display_width": 1024,
+        "display_height": 768
+        "environment": "browser" # other possible values: "mac", "windows", "ubuntu"
+    }],
+    input=[
+        {
+            "call_id": last_call_id,
+            "type": "computer_call_output",
+            "output": {
+                "type": "input_image",
+                # Image should be in base64
+                "image_url": f"data:image/png;base64,{<base64_string>}"
+            }
+        }
+    ],
+    truncation="auto"
+)
+```
+
+
+## [REST API](#tab/rest-api)
+
+```bash
+curl ${MY_ENDPOINT}/openai/responses?api-version=2025-03-01-preview \ 
+  -H "Content-Type: application/json" \ 
+  -H "api-key: $MY_API_KEY" \ 
+  -d '{ 
+    "model": "computer-use-preview", 
+    "input": [ 
+      "tools": [{
+        "type": "computer-preview",
+        "display_width": 1024,
+        "display_height": 768,
+        "environment": "browser" # other possible values: "mac", "windows", "ubuntu"
+      }], 
+        {
+        "call_id": last_call_id,
+        "type": "computer_call_output",
+        "output": {
+            "type": "input_image",
+            "image_url": "<base64_string>"
+        }
+      }
+    ],
+    "truncation":"auto"
+  }' 
+```
+
+---
+## Understanding the Computer Use integration
+
+When working with the Computer Use tool, you typically would perform the following to integrate it into your application.
+
+1. Send a request to the model that includes a call to the computer use tool, and the display size and environment. You can also include a screenshot of the initial state of the environment in the first API request. 
+1. Receive a response from the model. If the response has `action` items, those items contain suggested actions to make progress toward the specified goal. For example an action might be `screenshot` so the model can assess the current state with an updated screenshot, or `click` with X/Y coordinates indicating where the mouse should be moved.
+1. Execute the action using your application code on your computer or browser environment.
+1. After executing the action, capture the updated state of the environment as a screenshot.
+1. Send a new request with the updated state as a `computer_call_output`, and repeat this loop until the model stops requesting actions or you decide to stop. 
+
+## Handling conversation history
+
+You can use the `previous_response_id` parameter to link the current request to the previous response. Using this parameter is recommended if you don't want to manage the conversation history.
+
+If you don't use this parameter, you should make sure to include all the items returned in the response output of the previous request in your inputs array. This includes reasoning items if present.
+
+## Safety checks
+
+The API has safety checks to help protect against prompt injection and model mistakes. These checks include:
+
+* **Malicious instruction detection**: The system evaluates the screenshot image and checks if it contains adversarial content that might change the model's behavior.
+* **Irrelevant domain detection**: The system evaluates the `current_url` (if provided) and checks if the current domain is considered relevant given the conversation history.
+* **Sensitive domain detection**: The system checks the `current_url` (if provided) and raises a warning when it detects the user is on a sensitive domain.
+
+If one or more of the above checks is triggered, a safety check is raised when the model returns the next `computer_call`, with the `pending_safety_checks` parameter.
+
+```json
+"output": [
+    {
+        "type": "reasoning",
+        "id": "rs_67cb...",
+        "summary": [
+            {
+                "type": "summary_text",
+                "text": "Exploring 'File' menu option."
+            }
+        ]
+    },
+    {
+        "type": "computer_call",
+        "id": "cu_67cb...",
+        "call_id": "call_nEJ...",
+        "action": {
+            "type": "click",
+            "button": "left",
+            "x": 135,
+            "y": 193
+        },
+        "pending_safety_checks": [
+            {
+                "id": "cu_sc_67cb...",
+                "code": "malicious_instructions",
+                "message": "We've detected instructions that may cause your application to perform malicious or unauthorized actions. Please acknowledge this warning if you'd like to proceed."
+            }
+        ],
+        "status": "completed"
+    }
+]
+```
+
+You need to pass the safety checks back as `acknowledged_safety_checks` in the next request in order to proceed. 
+
+```json
+"input":[
+        {
+            "type": "computer_call_output",
+            "call_id": "<call_id>",
+            "acknowledged_safety_checks": [
+                {
+                    "id": "<safety_check_id>",
+                    "code": "malicious_instructions",
+                    "message": "We've detected instructions that may cause your application to perform malicious or unauthorized actions. Please acknowledge this warning if you'd like to proceed."
+                }
+            ],
+            "output": {
+                "type": "computer_screenshot",
+                "image_url": "<image_url>"
+            }
+        }
+    ],
+```
+
+### Safety check handling
+
+In all cases where `pending_safety_checks` are returned, actions should be handed over to the end user to confirm proper model behavior and accuracy.
+
+* `malicious_instructions` and `irrelevant_domain`: end users should review model actions and confirm that the model is behaving as intended.
+* `sensitive_domain`: ensure an end user is actively monitoring the model actions on these sites. Exact implementation of this "watch mode" can vary by application, but a potential example could be collecting user impression data on the site to make sure there is active end user engagement with the application.
+
+## See also
+
+* [Responses API](./responses.md)
+    * [Computer Use with playwright](./responses.md#computer-use)
+* [Computer Use Assistant sample on Github](https://github.com/Azure-Samples/computer-use-model)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "コンピュータ使用に関する新しいガイドの追加"
}
```

### Explanation
この変更は、Azure OpenAIにおける「コンピュータ使用」という新機能に関する完全なガイド文書を追加したものです。このガイドでは、AIがコンピュータのアプリケーションと対話することを可能にする専用モデルの使用方法について説明されています。具体的には、ユーザーインターフェースを通じてタスクを実行するエージェントを作成する方法、そしてそれに伴う様々な機能が紹介されています。 

主な機能としては、アプリケーションの自動ナビゲーション、動的適応、複数アプリケーション間でのタスクの実行、自然言語インターフェースを利用した指示の実行が含まれます。ユーザーは、特定のモデル「computer-use-preview」にアクセスするための登録方法や、それを使用するためのAPIへの呼び出し方法、PythonやREST APIを用いたサンプルコードも提供されています。 

文書の中には、API呼び出しの流れや安全性チェックについての情報、ならびにユーザーが自身のアプリケーションにこの機能を統合する方法も詳述されており、非常に包括的な内容となっています。この新しいドキュメントは、開発者が新機能を効果的に利用し、操作するための貴重なリソースとなります。

## articles/ai-services/openai/how-to/prompt-caching.md{#item-1631df}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 12/15/2024
+ms.date: 03/20/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -22,6 +22,7 @@ Caches are typically cleared within 5-10 minutes of inactivity and are always re
 
 Currently only the following models support prompt caching with Azure OpenAI:
 
+- `o3-mini-2025-01-31`
 - `o1-2024-12-17`
 - `o1-preview-2024-09-12`
 - `o1-mini-2024-09-12`
@@ -36,7 +37,7 @@ Currently only the following models support prompt caching with Azure OpenAI:
 
 ## API support
 
-Official support for prompt caching was first added in API version `2024-10-01-preview`. At this time, only the o1 model family supports the `cached_tokens` API response parameter.
+Official support for prompt caching was first added in API version `2024-10-01-preview`. At this time, only the o-series model family supports the `cached_tokens` API response parameter.
 
 ## Getting started
 
@@ -50,7 +51,7 @@ When a match is found between the token computations in a prompt and the current
 ```json
 {
   "created": 1729227448,
-  "model": "o1-preview-2024-09-12",
+  "model": "o1-2024-12-17",
   "object": "chat.completion",
   "service_tier": null,
   "system_fingerprint": "fp_50cdd5dc04",
@@ -82,13 +83,13 @@ Prompt caching is supported for:
 
 |**Caching supported**|**Description**|**Supported models**|
 |--------|--------|--------|
-| **Messages** | The complete messages array: system, developer, user, and assistant content | `gpt-4o`<br/>`gpt-4o-mini`<br/>`gpt-4o-realtime-preview` (version 2024-12-17)<br/>`gpt-4o-mini-realtime-preview` (version 2024-12-17)<br> `o1` (version 2024-12-17) |
+| **Messages** | The complete messages array: system, developer, user, and assistant content | `gpt-4o`<br/>`gpt-4o-mini`<br/>`gpt-4o-realtime-preview` (version 2024-12-17)<br/>`gpt-4o-mini-realtime-preview` (version 2024-12-17)<br> `o1` (version 2024-12-17) <br> `o3-mini` (version 2025-01-31) |
 | **Images** | Images included in user messages, both as links or as base64-encoded data. The detail parameter must be set the same across requests. | `gpt-4o`<br/>`gpt-4o-mini` <br> `o1` (version 2024-12-17)  |
-| **Tool use** | Both the messages array and tool definitions. | `gpt-4o`<br/>`gpt-4o-mini`<br/>`gpt-4o-realtime-preview` (version 2024-12-17)<br/>`gpt-4o-mini-realtime-preview` (version 2024-12-17)<br> `o1` (version 2024-12-17) |
-| **Structured outputs** | Structured output schema is appended as a prefix to the system message. | `gpt-4o`<br/>`gpt-4o-mini` <br> `o1` (version 2024-12-17) |
+| **Tool use** | Both the messages array and tool definitions. | `gpt-4o`<br/>`gpt-4o-mini`<br/>`gpt-4o-realtime-preview` (version 2024-12-17)<br/>`gpt-4o-mini-realtime-preview` (version 2024-12-17)<br> `o1` (version 2024-12-17) <br> `o3-mini` (version 2025-01-31) |
+| **Structured outputs** | Structured output schema is appended as a prefix to the system message. | `gpt-4o`<br/>`gpt-4o-mini` <br> `o1` (version 2024-12-17) <br> `o3-mini` (version 2025-01-31) |
 
 To improve the likelihood of cache hits occurring, you should structure your requests such that repetitive content occurs at the beginning of the messages array.
 
 ## Can I disable prompt caching?
 
-Prompt caching is enabled by default for all supported models. There is no opt-out support for prompt caching. 
+Prompt caching is enabled by default for all supported models. There is no opt-out support for prompt caching.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトキャッシングに関する情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのプロンプトキャッシングに関するドキュメントを更新した内容です。主な修正点には、以下の項目が含まれています。

1. 文書の日付が2024年12月15日から2025年3月20日に更新されました。
2. 新たに「o3-mini-2025-01-31」モデルがプロンプトキャッシングをサポートするモデルリストに追加されました。
3. API応答パラメータの説明が調整され、現在は「o-series」モデルファミリーが「cached_tokens」API応答パラメータをサポートすることが明記されています。
4. プロンプトキャッシングがサポートされるメッセージの説明が更新され、特定のモデルがリストに追加されました。

全体として、この更新はプロンプトキャッシング機能がどのモデルでサポートされるのか、またその利用方法のおさらいを提供し、潜在的なユーザーにとっての利便性を向上させる内容となっています。この情報は、開発者がプロンプトキャッシング機能を効果的に活用できるようにサポートしています。

## articles/ai-services/openai/how-to/responses.md{#item-b9757d}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,1477 @@
+---
+title: Azure OpenAI Responses API
+titleSuffix: Azure OpenAI
+description: Learn how to use Azure OpenAI's new stateful Responses API.
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 03/21/2025
+author: mrbullwinkle    
+ms.author: mbullwin
+ms.custom: references_regions
+---
+
+# Azure OpenAI Responses API (Preview)
+
+The Responses API is a new stateful API from Azure OpenAI. It brings together the best capabilities from the chat completions and assistants API in one unified experience. The Responses API also adds support for the new `computer-use-preview` model which powers the [Computer use](../how-to/computer-use.md) capability.
+
+## Responses API
+
+### API support
+
+`2025-03-01-preview` or later
+
+### Region Availability
+
+The responses API is currently available in the following regions:
+
+- australiaeast
+- eastus
+- eastus2
+- francecentral
+- japaneast
+- norwayeast
+- southindia
+- swedencentral
+- uaenorth
+- uksouth
+- westus
+- westus3
+
+### Model support
+
+- `gpt-4o`
+- `gpt-4o-mini`
+- `computer-use-preview`
+
+> [!NOTE]
+> The responses API does not currently support:
+> - Structured outputs
+> - tool_choice
+> - image_url pointing to an internet address  
+>
+> There is also a known issue with vision performance when using the Responses API, particularly with OCR tasks. Once this issue is fixed and support is added, this article will be updated.
+
+### Reference documentation
+
+- [Responses API reference documentation](/azure/ai-services/openai/reference-preview?#responses-api---create)
+
+## Getting started with the responses API
+
+To access the responses API commands, you need to upgrade your version of the OpenAI library.
+
+```cmd
+pip install --upgrade openai
+```
+
+## Generate a text response
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
+
+```python
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
+  api_version="2025-03-01-preview"
+)
+
+response = client.responses.create(
+    model="gpt-4o", # replace with your model deployment name 
+    input="This is a test."
+    #truncation="auto" required when using computer-use-preview model.
+
+)
+```
+
+# [Python (API Key)](#tab/python-key)
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+
+```python
+import os
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
+    api_version="2025-03-01-preview",
+    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
+    )
+
+response = client.responses.create(
+    model="gpt-4o", # replace with your model deployment name 
+    input="This is a test."
+    #truncation="auto" required when using computer-use-preview model.
+
+)
+```
+
+# [REST API](#tab/rest-api)
+
+### Microsoft Entra ID
+
+```bash
+curl -X POST "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/responses?api-version=2025-03-01-preview" \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+  -d '{
+     "model": "gpt-4o",
+     "input": "This is a test"
+    }'
+```
+
+### API Key
+
+```bash
+curl -X POST https://YOUR-RESOURCE-NAME.openai.azure.com/openai/responses?api-version=2025-03-01-preview \
+  -H "Content-Type: application/json" \
+  -H "api-key: $AZURE_OPENAI_API_KEY" \
+  -d '{
+     "model": "gpt-4o",
+     "input": "This is a test"
+    }'
+```
+
+# [Output](#tab/output)
+
+**Output:**
+
+```json
+{
+  "id": "resp_67cb32528d6881909eb2859a55e18a85",
+  "created_at": 1741369938.0,
+  "error": null,
+  "incomplete_details": null,
+  "instructions": null,
+  "metadata": {},
+  "model": "gpt-4o-2024-08-06",
+  "object": "response",
+  "output": [
+    {
+      "id": "msg_67cb3252cfac8190865744873aada798",
+      "content": [
+        {
+          "annotations": [],
+          "text": "Great! How can I help you today?",
+          "type": "output_text"
+        }
+      ],
+      "role": "assistant",
+      "status": null,
+      "type": "message"
+    }
+  ],
+  "output_text": "Great! How can I help you today?",
+  "parallel_tool_calls": null,
+  "temperature": 1.0,
+  "tool_choice": null,
+  "tools": [],
+  "top_p": 1.0,
+  "max_output_tokens": null,
+  "previous_response_id": null,
+  "reasoning": null,
+  "status": "completed",
+  "text": null,
+  "truncation": null,
+  "usage": {
+    "input_tokens": 20,
+    "output_tokens": 11,
+    "output_tokens_details": {
+      "reasoning_tokens": 0
+    },
+    "total_tokens": 31
+  },
+  "user": null,
+  "reasoning_effort": null
+}
+```
+
+---
+
+## Retrieve a response
+
+To retrieve a response from a previous call to the responses API.
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
+
+```python
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
+  api_version="2025-03-01-preview"
+)
+
+response = client.responses.retrieve("resp_67cb61fa3a448190bcf2c42d96f0d1a8")
+
+print(response.model_dump_json(indent=2))
+```
+
+# [Python (API Key)](#tab/python-key)
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+
+```python
+import os
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
+    api_version="2025-03-01-preview",
+    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
+    )
+
+response = client.responses.retrieve("resp_67cb61fa3a448190bcf2c42d96f0d1a8")
+```
+
+# [REST API](#tab/rest-api)
+
+### Microsoft Entra ID
+
+```bash
+curl -X GET "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/{response_id}?api-version=2025-03-01-preview" \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" 
+```
+
+### API Key
+
+```bash
+curl -X GET https://YOUR-RESOURCE-NAME.openai.azure.com/openai/responses/{response_id}?api-version=2025-03-01-preview \
+  -H "Content-Type: application/json" \
+  -H "api-key: $AZURE_OPENAI_API_KEY" 
+```
+
+# [Output](#tab/output)
+
+```json
+{
+  "id": "resp_67cb61fa3a448190bcf2c42d96f0d1a8",
+  "created_at": 1741382138.0,
+  "error": null,
+  "incomplete_details": null,
+  "instructions": null,
+  "metadata": {},
+  "model": "gpt-4o-2024-08-06",
+  "object": "response",
+  "output": [
+    {
+      "id": "msg_67cb61fa95588190baf22ffbdbbaaa9d",
+      "content": [
+        {
+          "annotations": [],
+          "text": "Hello! How can I assist you today?",
+          "type": "output_text"
+        }
+      ],
+      "role": "assistant",
+      "status": null,
+      "type": "message"
+    }
+  ],
+  "parallel_tool_calls": null,
+  "temperature": 1.0,
+  "tool_choice": null,
+  "tools": [],
+  "top_p": 1.0,
+  "max_output_tokens": null,
+  "previous_response_id": null,
+  "reasoning": null,
+  "status": "completed",
+  "text": null,
+  "truncation": null,
+  "usage": {
+    "input_tokens": 20,
+    "output_tokens": 11,
+    "output_tokens_details": {
+      "reasoning_tokens": 0
+    },
+    "total_tokens": 31
+  },
+  "user": null,
+  "reasoning_effort": null
+}
+```
+
+---
+
+## Delete response
+
+By default response data is retained for 30 days. To delete a response, you can use `response.delete"("{response_id})`
+
+```python
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
+  api_version="2025-03-01-preview"
+)
+
+response = client.responses.delete("resp_67cb61fa3a448190bcf2c42d96f0d1a8")
+
+print(response)
+```
+
+## Chaining responses together
+
+You can chain responses together by passing the `response.id` from the previous response to the `previous_response_id` parameter.
+
+```python
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
+  api_version="2025-03-01-preview"
+)
+
+response = client.responses.create(
+    model="gpt-4o",  # replace with your model deployment name
+    input="Define and explain the concept of catastrophic forgetting?"
+)
+
+second_response = client.responses.create(
+    model="gpt-4o",  # replace with your model deployment name
+    previous_response_id=response.id,
+    input=[{"role": "user", "content": "Explain this at a level that could be understood by a college freshman"}]
+)
+print(second_response.model_dump_json(indent=2)) 
+```
+
+Note from the output that even though we never shared the first input question with the `second_response` API call, by passing the `previous_response_id` the model has full context of previous question and response to answer the new question.
+
+**Output:**
+
+```json
+{
+  "id": "resp_67cbc9705fc08190bbe455c5ba3d6daf",
+  "created_at": 1741408624.0,
+  "error": null,
+  "incomplete_details": null,
+  "instructions": null,
+  "metadata": {},
+  "model": "gpt-4o-2024-08-06",
+  "object": "response",
+  "output": [
+    {
+      "id": "msg_67cbc970fd0881908353a4298996b3f6",
+      "content": [
+        {
+          "annotations": [],
+          "text": "Sure! Imagine you are studying for exams in different subjects like math, history, and biology. You spend a lot of time studying math first and get really good at it. But then, you switch to studying history. If you spend all your time and focus on history, you might forget some of the math concepts you learned earlier because your brain fills up with all the new history facts. \n\nIn the world of artificial intelligence (AI) and machine learning, a similar thing can happen with computers. We use special programs called neural networks to help computers learn things, sort of like how our brain works. But when a neural network learns a new task, it can forget what it learned before. This is what we call \"catastrophic forgetting.\"\n\nSo, if a neural network learned how to recognize cats in pictures, and then you teach it how to recognize dogs, it might get really good at recognizing dogs but suddenly become worse at recognizing cats. This happens because the process of learning new information can overwrite or mess with the old information in its \"memory.\"\n\nScientists and engineers are working on ways to help computers remember everything they learn, even as they keep learning new things, just like students have to remember math, history, and biology all at the same time for their exams. They use different techniques to make sure the neural network doesn’t forget the important stuff it learned before, even when it gets new information.",
+          "type": "output_text"
+        }
+      ],
+      "role": "assistant",
+      "status": null,
+      "type": "message"
+    }
+  ],
+  "parallel_tool_calls": null,
+  "temperature": 1.0,
+  "tool_choice": null,
+  "tools": [],
+  "top_p": 1.0,
+  "max_output_tokens": null,
+  "previous_response_id": "resp_67cbc96babbc8190b0f69aedc655f173",
+  "reasoning": null,
+  "status": "completed",
+  "text": null,
+  "truncation": null,
+  "usage": {
+    "input_tokens": 405,
+    "output_tokens": 285,
+    "output_tokens_details": {
+      "reasoning_tokens": 0
+    },
+    "total_tokens": 690
+  },
+  "user": null,
+  "reasoning_effort": null
+}
+```
+
+### Chaining responses manually
+
+Alternatively you can manually chain responses together using the method below:
+
+```python
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
+  api_version="2025-03-01-preview"
+)
+
+
+inputs = [{"type": "message", "role": "user", "content": "Define and explain the concept of catastrophic forgetting?"}] 
+  
+response = client.responses.create(  
+    model="gpt-4o",  # replace with your model deployment name  
+    input="inputs"  
+)  
+  
+inputs += response.output
+
+inputs.append({"role": "user", "type": "message", "content": "Explain this at a level that could be understood by a college freshman"}) 
+               
+
+second_response = client.responses.create(  
+    model="gpt-4o",  
+    previous_response_id=response.id,  
+    input=inputs
+)  
+      
+print(second_response.model_dump_json(indent=2))  
+```
+
+## Function calling
+
+The responses API supports function calling.
+
+```python
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
+  api_version="2025-03-01-preview"
+)
+
+response = client.responses.create(  
+    model="gpt-4o",  # replace with your model deployment name  
+    tools=[  
+        {  
+            "type": "function",  
+            "name": "get_weather",  
+            "description": "Get the weather for a location",  
+            "parameters": {  
+                "type": "object",  
+                "properties": {  
+                    "location": {"type": "string"},  
+                },  
+                "required": ["location"],  
+            },  
+        }  
+    ],  
+    input=[{"role": "user", "content": "What's the weather in San Francisco?"}],  
+)  
+
+print(response.model_dump_json(indent=2))  
+  
+# To provide output to tools, add a response for each tool call to an array passed  
+# to the next response as `input`  
+input = []  
+for output in response.output:  
+    if output.type == "function_call":  
+        match output.name:  
+            case "get_weather":  
+                input.append(  
+                    {  
+                        "type": "function_call_output",  
+                        "call_id": output.id,  
+                        "output": '{"temperature": "70 degrees"}',  
+                    }  
+                )  
+            case _:  
+                raise ValueError(f"Unknown function call: {output.name}")  
+  
+second_response = client.responses.create(  
+    model="gpt-4o",  
+    previous_response_id=response.id,  
+    input=input  
+)  
+
+print(second_response.model_dump_json(indent=2)) 
+
+```
+
+## List input items
+
+```python
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
+  api_version="2025-03-01-preview"
+)
+
+response = client.responses.input_items.list("resp_67d856fcfba0819081fd3cffee2aa1c0")
+
+print(response.model_dump_json(indent=2))
+```
+
+**Output:**
+
+```json
+{
+  "data": [
+    {
+      "id": "msg_67d856fcfc1c8190ad3102fc01994c5f",
+      "content": [
+        {
+          "text": "This is a test.",
+          "type": "input_text"
+        }
+      ],
+      "role": "user",
+      "status": "completed",
+      "type": "message"
+    }
+  ],
+  "has_more": false,
+  "object": "list",
+  "first_id": "msg_67d856fcfc1c8190ad3102fc01994c5f",
+  "last_id": "msg_67d856fcfc1c8190ad3102fc01994c5f"
+}
+```
+
+## Image input
+
+### Image url
+
+```python
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
+  api_version="2025-03-01-preview"
+)
+
+response = client.responses.create(
+    model="gpt-4o",
+    input=[
+        {
+            "role": "user",
+            "content": [
+                { "type": "input_text", "text": "what is in this image?" },
+                {
+                    "type": "input_image",
+                    "image_url": "<image_URL>"
+                }
+            ]
+        }
+    ]
+)
+
+print(response)
+
+```
+
+### Base64 encoded image
+
+```python
+import base64
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
+  api_version="2025-03-01-preview"
+)
+
+def encode_image(image_path):
+    with open(image_path, "rb") as image_file:
+        return base64.b64encode(image_file.read()).decode("utf-8")
+
+# Path to your image
+image_path = "path_to_your_image.jpg"
+
+# Getting the Base64 string
+base64_image = encode_image(image_path)
+
+response = client.responses.create(
+    model="gpt-4o",
+    input=[
+        {
+            "role": "user",
+            "content": [
+                { "type": "input_text", "text": "what is in this image?" },
+                {
+                    "type": "input_image",
+                    "image_url": f"data:image/jpeg;base64,{base64_image}"
+                }
+            ]
+        }
+    ]
+)
+
+print(response)
+```
+
+## Computer use
+
+In this section, we provide a simple example script that integrates Azure OpenAI's `computer-use-preview` model with [Playwright](https://playwright.dev/) to automate basic browser interactions. Combining the model with [Playwright](https://playwright.dev/) allows the model to see the browser screen, make decisions, and perform actions like clicking, typing, and navigating websites. You should exercise caution when running this example code. This code is designed to be run locally but should only be executed in a test environment. Use a human to confirm decisions and don't give the model access to sensitive data.
+
+First you'll need to install the Python library for [Playwright](https://playwright.dev/).
+
+```cmd
+pip install playwright
+```
+
+Once the package is installed, you'll also need to run
+
+```cmd
+playwright install
+```
+
+### Imports and configuration
+
+First, we import the necessary libraries and define our configuration parameters. Since we're using `asyncio` we'll be executing this code outside of Jupyter notebooks. We'll walk through the code first in chunks and then demonstrate how to use it.
+
+```python
+import os
+import asyncio
+import base64
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+from playwright.async_api import async_playwright, TimeoutError
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+
+# Configuration
+
+AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
+MODEL = "computer-use-preview" # Set to model deployment name
+DISPLAY_WIDTH = 1024
+DISPLAY_HEIGHT = 768
+API_VERSION = "2025-03-01-preview" #Use this API version or later
+ITERATIONS = 5 # Max number of iterations before returning control to human supervisor
+```
+
+### Key mapping for browser interaction
+
+Next, we set up mappings for special keys that the model might need to pass to Playwright. Ultimately the model is never performing actions itself, it passes representations of commands and you have to provide the final integration layer that can take those commands and execute them in your chosen environment.
+
+This isn't an exhaustive list of possible key mappings. You can expand this list as needed. This dictionary is specific to integrating the model with Playwright. If you were integrating the model with an alternate library to provide API access to your operating systems keyboard/mouse you would need to provide a mapping specific to that library.
+
+```python
+# Key mapping for special keys in Playwright
+KEY_MAPPING = {
+    "/": "Slash", "\\": "Backslash", "alt": "Alt", "arrowdown": "ArrowDown",
+    "arrowleft": "ArrowLeft", "arrowright": "ArrowRight", "arrowup": "ArrowUp",
+    "backspace": "Backspace", "ctrl": "Control", "delete": "Delete", 
+    "enter": "Enter", "esc": "Escape", "shift": "Shift", "space": " ",
+    "tab": "Tab", "win": "Meta", "cmd": "Meta", "super": "Meta", "option": "Alt"
+}
+```
+
+This dictionary translates user-friendly key names to the format expected by Playwright's keyboard API.
+
+### Coordinate validation function
+
+To make sure that any mouse actions that are passed from the model stay within the browser window boundaries we'll add the following utility function:
+
+```python
+def validate_coordinates(x, y):
+    """Ensure coordinates are within display bounds."""
+    return max(0, min(x, DISPLAY_WIDTH)), max(0, min(y, DISPLAY_HEIGHT))
+```
+
+This simple utility attempts to prevent out-of-bounds errors by clamping coordinates to the window dimensions.
+
+### Action handling
+
+The core of our browser automation is the action handler that processes various types of user interactions and convert them into actions within the browser.
+
+```python
+async def handle_action(page, action):
+    """Handle different action types from the model."""
+    action_type = action.type
+    
+    if action_type == "drag":
+        print("Drag action is not supported in this implementation. Skipping.")
+        return
+        
+    elif action_type == "click":
+        button = getattr(action, "button", "left")
+        # Validate coordinates
+        x, y = validate_coordinates(action.x, action.y)
+        
+        print(f"\tAction: click at ({x}, {y}) with button '{button}'")
+        
+        if button == "back":
+            await page.go_back()
+        elif button == "forward":
+            await page.go_forward()
+        elif button == "wheel":
+            await page.mouse.wheel(x, y)
+        else:
+            button_type = {"left": "left", "right": "right", "middle": "middle"}.get(button, "left")
+            await page.mouse.click(x, y, button=button_type)
+            try:
+                await page.wait_for_load_state("domcontentloaded", timeout=3000)
+            except TimeoutError:
+                pass
+        
+    elif action_type == "double_click":
+        # Validate coordinates
+        x, y = validate_coordinates(action.x, action.y)
+        
+        print(f"\tAction: double click at ({x}, {y})")
+        await page.mouse.dblclick(x, y)
+        
+    elif action_type == "scroll":
+        scroll_x = getattr(action, "scroll_x", 0)
+        scroll_y = getattr(action, "scroll_y", 0)
+        # Validate coordinates
+        x, y = validate_coordinates(action.x, action.y)
+        
+        print(f"\tAction: scroll at ({x}, {y}) with offsets ({scroll_x}, {scroll_y})")
+        await page.mouse.move(x, y)
+        await page.evaluate(f"window.scrollBy({{left: {scroll_x}, top: {scroll_y}, behavior: 'smooth'}});")
+        
+    elif action_type == "keypress":
+        keys = getattr(action, "keys", [])
+        print(f"\tAction: keypress {keys}")
+        mapped_keys = [KEY_MAPPING.get(key.lower(), key) for key in keys]
+        
+        if len(mapped_keys) > 1:
+            # For key combinations (like Ctrl+C)
+            for key in mapped_keys:
+                await page.keyboard.down(key)
+            await asyncio.sleep(0.1)
+            for key in reversed(mapped_keys):
+                await page.keyboard.up(key)
+        else:
+            for key in mapped_keys:
+                await page.keyboard.press(key)
+                
+    elif action_type == "type":
+        text = getattr(action, "text", "")
+        print(f"\tAction: type text: {text}")
+        await page.keyboard.type(text, delay=20)
+        
+    elif action_type == "wait":
+        ms = getattr(action, "ms", 1000)
+        print(f"\tAction: wait {ms}ms")
+        await asyncio.sleep(ms / 1000)
+        
+    elif action_type == "screenshot":
+        print("\tAction: screenshot")
+        
+    else:
+        print(f"\tUnrecognized action: {action_type}")
+```
+
+This function attempts to handle various types of actions such as:
+
+- Clicking and dragging the mouse.
+- Clicking (left, right, middle buttons).
+- Double-clicking.
+- Scrolling.
+- Key presses (including combinations).
+- Typing text.
+
+### Screenshot capture
+
+In order for the model to be able to see what it's interacting with the model needs a way to capture screenshots. For this code we're using Playwright to capture the screenshots and we're limiting the view to just the content in the browser window. The screenshot won't include the url bar or other aspects of the browser GUI. If you need the model to see outside the main browser window you could augment the model by creating your own screenshot function.
+
+```python
+async def take_screenshot(page):
+    """Take a screenshot and return base64 encoding with caching for failures."""
+    global last_successful_screenshot
+    
+    try:
+        screenshot_bytes = await page.screenshot(full_page=False)
+        last_successful_screenshot = base64.b64encode(screenshot_bytes).decode("utf-8")
+        return last_successful_screenshot
+    except Exception as e:
+        print(f"Screenshot failed: {e}")
+        print(f"Using cached screenshot from previous successful capture")
+        if last_successful_screenshot:
+            return last_successful_screenshot
+```
+
+This function captures the current browser state as an image and returns it as a base64-encoded string, ready to be sent to the model. We'll constantly do this in a loop after each step allowing the model to see if the command it tried to execute was successful or not, which then allows it to adjust based on the contents of the screenshot.
+
+### Model response processing
+
+This function processes the model's responses and executes the requested actions:
+
+```python
+async def process_model_response(client, response, page, max_iterations=ITERATIONS):
+    """Process the model's response and execute actions."""
+    for iteration in range(max_iterations):
+        if not hasattr(response, 'output') or not response.output:
+            print("No output from model.")
+            break
+        
+        # Safely access response id
+        response_id = getattr(response, 'id', 'unknown')
+        print(f"\nIteration {iteration + 1} - Response ID: {response_id}\n")
+        
+        # Print text responses and reasoning
+        for item in response.output:
+            # Handle text output
+            if hasattr(item, 'type') and item.type == "text":
+                print(f"\nModel message: {item.text}\n")
+                
+            # Handle reasoning output
+            if hasattr(item, 'type') and item.type == "reasoning":
+                # Extract meaningful content from the reasoning
+                meaningful_content = []
+                
+                if hasattr(item, 'summary') and item.summary:
+                    for summary in item.summary:
+                        # Handle different potential formats of summary content
+                        if isinstance(summary, str) and summary.strip():
+                            meaningful_content.append(summary)
+                        elif hasattr(summary, 'text') and summary.text.strip():
+                            meaningful_content.append(summary.text)
+                
+                # Only print reasoning section if there's actual content
+                if meaningful_content:
+                    print("=== Model Reasoning ===")
+                    for idx, content in enumerate(meaningful_content, 1):
+                        print(f"{content}")
+                    print("=====================\n")
+        
+        # Extract computer calls
+        computer_calls = [item for item in response.output 
+                         if hasattr(item, 'type') and item.type == "computer_call"]
+        
+        if not computer_calls:
+            print("No computer call found in response. Reverting control to human operator")
+            break
+        
+        computer_call = computer_calls[0]
+        if not hasattr(computer_call, 'call_id') or not hasattr(computer_call, 'action'):
+            print("Computer call is missing required attributes.")
+            break
+        
+        call_id = computer_call.call_id
+        action = computer_call.action
+        
+        # Handle safety checks
+        acknowledged_checks = []
+        if hasattr(computer_call, 'pending_safety_checks') and computer_call.pending_safety_checks:
+            pending_checks = computer_call.pending_safety_checks
+            print("\nSafety checks required:")
+            for check in pending_checks:
+                print(f"- {check.code}: {check.message}")
+            
+            if input("\nDo you want to proceed? (y/n): ").lower() != 'y':
+                print("Operation cancelled by user.")
+                break
+            
+            acknowledged_checks = pending_checks
+        
+        # Execute the action
+        try:
+           await page.bring_to_front()
+           await handle_action(page, action)
+           
+           # Check if a new page was created after the action
+           if action.type in ["click"]:
+               await asyncio.sleep(1.5)
+               # Get all pages in the context
+               all_pages = page.context.pages
+               # If we have multiple pages, check if there's a newer one
+               if len(all_pages) > 1:
+                   newest_page = all_pages[-1]  # Last page is usually the newest
+                   if newest_page != page and newest_page.url not in ["about:blank", ""]:
+                       print(f"\tSwitching to new tab: {newest_page.url}")
+                       page = newest_page  # Update our page reference
+           elif action.type != "wait":
+               await asyncio.sleep(0.5)
+               
+        except Exception as e:
+           print(f"Error handling action {action.type}: {e}")
+           import traceback
+           traceback.print_exc()    
+
+        # Take a screenshot after the action
+        screenshot_base64 = await take_screenshot(page)
+
+        print("\tNew screenshot taken")
+        
+        # Prepare input for the next request
+        input_content = [{
+            "type": "computer_call_output",
+            "call_id": call_id,
+            "output": {
+                "type": "input_image",
+                "image_url": f"data:image/png;base64,{screenshot_base64}"
+            }
+        }]
+        
+        # Add acknowledged safety checks if any
+        if acknowledged_checks:
+            acknowledged_checks_dicts = []
+            for check in acknowledged_checks:
+                acknowledged_checks_dicts.append({
+                    "id": check.id,
+                    "code": check.code,
+                    "message": check.message
+                })
+            input_content[0]["acknowledged_safety_checks"] = acknowledged_checks_dicts
+        
+        # Add current URL for context
+        try:
+            current_url = page.url
+            if current_url and current_url != "about:blank":
+                input_content[0]["current_url"] = current_url
+                print(f"\tCurrent URL: {current_url}")
+        except Exception as e:
+            print(f"Error getting URL: {e}")
+        
+        # Send the screenshot back for the next step
+        try:
+            response = client.responses.create(
+                model=MODEL,
+                previous_response_id=response_id,
+                tools=[{
+                    "type": "computer_use_preview",
+                    "display_width": DISPLAY_WIDTH,
+                    "display_height": DISPLAY_HEIGHT,
+                    "environment": "browser"
+                }],
+                input=input_content,
+                truncation="auto"
+            )
+
+            print("\tModel processing screenshot")
+        except Exception as e:
+            print(f"Error in API call: {e}")
+            import traceback
+            traceback.print_exc()
+            break
+    
+    if iteration >= max_iterations - 1:
+        print("Reached maximum number of iterations. Stopping.")
+```
+
+In this section we have added code that:
+
+- Extracts and displays text and reasoning from the model.
+- Processes computer action calls.
+- Handles potential safety checks requiring user confirmation.
+- Executes the requested action.
+- Captures a new screenshot.
+- Sends the updated state back to the model.
+- Repeats this process for multiple iterations.
+
+### Main function
+
+The main function coordinates the entire process:
+
+```python
+    # Initialize OpenAI client
+    client = AzureOpenAI(
+        azure_endpoint=AZURE_ENDPOINT,
+        azure_ad_token_provider=token_provider,
+        api_version=API_VERSION
+    )
+    
+    # Initialize Playwright
+    async with async_playwright() as playwright:
+        browser = await playwright.chromium.launch(
+            headless=False,
+            args=[f"--window-size={DISPLAY_WIDTH},{DISPLAY_HEIGHT}", "--disable-extensions"]
+        )
+        
+        context = await browser.new_context(
+            viewport={"width": DISPLAY_WIDTH, "height": DISPLAY_HEIGHT},
+            accept_downloads=True
+        )
+        
+        page = await context.new_page()
+        
+        # Navigate to starting page
+        await page.goto("https://www.bing.com", wait_until="domcontentloaded")
+        print("Browser initialized to Bing.com")
+        
+        # Main interaction loop
+        try:
+            while True:
+                print("\n" + "="*50)
+                user_input = input("Enter a task to perform (or 'exit' to quit): ")
+                
+                if user_input.lower() in ('exit', 'quit'):
+                    break
+                
+                if not user_input.strip():
+                    continue
+                
+                # Take initial screenshot
+                screenshot_base64 = await take_screenshot(page)
+                print("\nTake initial screenshot")
+                
+                # Initial request to the model
+                response = client.responses.create(
+                    model=MODEL,
+                    tools=[{
+                        "type": "computer_use_preview",
+                        "display_width": DISPLAY_WIDTH,
+                        "display_height": DISPLAY_HEIGHT,
+                        "environment": "browser"
+                    }],
+                    instructions = "You are an AI agent with the ability to control a browser. You can control the keyboard and mouse. You take a screenshot after each action to check if your action was successful. Once you have completed the requested task you should stop running and pass back control to your human operator.",
+                    input=[{
+                        "role": "user",
+                        "content": [{
+                            "type": "input_text",
+                            "text": user_input
+                        }, {
+                            "type": "input_image",
+                            "image_url": f"data:image/png;base64,{screenshot_base64}"
+                        }]
+                    }],
+                    reasoning={"generate_summary": "concise"},
+                    truncation="auto"
+                )
+                print("\nSending model initial screenshot and instructions")
+
+                # Process model actions
+                await process_model_response(client, response, page)
+                
+        except Exception as e:
+            print(f"An error occurred: {e}")
+            import traceback
+            traceback.print_exc()
+        
+        finally:
+            # Close browser
+            await context.close()
+            await browser.close()
+            print("Browser closed.")
+
+if __name__ == "__main__":
+    asyncio.run(main())
+```
+
+The main function:
+
+- Initializes the AzureOpenAI client.
+- Sets up the Playwright browser.
+- Starts at Bing.com.
+- Enters a loop to accept user tasks.
+- Captures the initial state.
+- Sends the task and screenshot to the model.
+- Processes the model's response.
+- Repeats until the user exits.
+- Ensures the browser is properly closed.
+
+### Complete script
+
+> [!CAUTION]
+> This code is experimental and for demonstration purposes only. It's only intended to illustrate the basic flow of the responses API and the `computer-use-preview` model. While you can execute this code on your local computer, we strongly recommend running this code on a low privilege virtual machine with no access to sensitive data. This code is for basic testing purposes only. 
+
+```python
+import os
+import asyncio
+import base64
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+from playwright.async_api import async_playwright, TimeoutError
+
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+# Configuration
+
+AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
+MODEL = "computer-use-preview"
+DISPLAY_WIDTH = 1024
+DISPLAY_HEIGHT = 768
+API_VERSION = "2025-03-01-preview"
+ITERATIONS = 5 # Max number of iterations before forcing the model to return control to the human supervisor
+
+# Key mapping for special keys in Playwright
+KEY_MAPPING = {
+    "/": "Slash", "\\": "Backslash", "alt": "Alt", "arrowdown": "ArrowDown",
+    "arrowleft": "ArrowLeft", "arrowright": "ArrowRight", "arrowup": "ArrowUp",
+    "backspace": "Backspace", "ctrl": "Control", "delete": "Delete", 
+    "enter": "Enter", "esc": "Escape", "shift": "Shift", "space": " ",
+    "tab": "Tab", "win": "Meta", "cmd": "Meta", "super": "Meta", "option": "Alt"
+}
+
+def validate_coordinates(x, y):
+    """Ensure coordinates are within display bounds."""
+    return max(0, min(x, DISPLAY_WIDTH)), max(0, min(y, DISPLAY_HEIGHT))
+
+async def handle_action(page, action):
+    """Handle different action types from the model."""
+    action_type = action.type
+    
+    if action_type == "drag":
+        print("Drag action is not supported in this implementation. Skipping.")
+        return
+        
+    elif action_type == "click":
+        button = getattr(action, "button", "left")
+        # Validate coordinates
+        x, y = validate_coordinates(action.x, action.y)
+        
+        print(f"\tAction: click at ({x}, {y}) with button '{button}'")
+        
+        if button == "back":
+            await page.go_back()
+        elif button == "forward":
+            await page.go_forward()
+        elif button == "wheel":
+            await page.mouse.wheel(x, y)
+        else:
+            button_type = {"left": "left", "right": "right", "middle": "middle"}.get(button, "left")
+            await page.mouse.click(x, y, button=button_type)
+            try:
+                await page.wait_for_load_state("domcontentloaded", timeout=3000)
+            except TimeoutError:
+                pass
+        
+    elif action_type == "double_click":
+        # Validate coordinates
+        x, y = validate_coordinates(action.x, action.y)
+        
+        print(f"\tAction: double click at ({x}, {y})")
+        await page.mouse.dblclick(x, y)
+        
+    elif action_type == "scroll":
+        scroll_x = getattr(action, "scroll_x", 0)
+        scroll_y = getattr(action, "scroll_y", 0)
+        # Validate coordinates
+        x, y = validate_coordinates(action.x, action.y)
+        
+        print(f"\tAction: scroll at ({x}, {y}) with offsets ({scroll_x}, {scroll_y})")
+        await page.mouse.move(x, y)
+        await page.evaluate(f"window.scrollBy({{left: {scroll_x}, top: {scroll_y}, behavior: 'smooth'}});")
+        
+    elif action_type == "keypress":
+        keys = getattr(action, "keys", [])
+        print(f"\tAction: keypress {keys}")
+        mapped_keys = [KEY_MAPPING.get(key.lower(), key) for key in keys]
+        
+        if len(mapped_keys) > 1:
+            # For key combinations (like Ctrl+C)
+            for key in mapped_keys:
+                await page.keyboard.down(key)
+            await asyncio.sleep(0.1)
+            for key in reversed(mapped_keys):
+                await page.keyboard.up(key)
+        else:
+            for key in mapped_keys:
+                await page.keyboard.press(key)
+                
+    elif action_type == "type":
+        text = getattr(action, "text", "")
+        print(f"\tAction: type text: {text}")
+        await page.keyboard.type(text, delay=20)
+        
+    elif action_type == "wait":
+        ms = getattr(action, "ms", 1000)
+        print(f"\tAction: wait {ms}ms")
+        await asyncio.sleep(ms / 1000)
+        
+    elif action_type == "screenshot":
+        print("\tAction: screenshot")
+        
+    else:
+        print(f"\tUnrecognized action: {action_type}")
+
+async def take_screenshot(page):
+    """Take a screenshot and return base64 encoding with caching for failures."""
+    global last_successful_screenshot
+    
+    try:
+        screenshot_bytes = await page.screenshot(full_page=False)
+        last_successful_screenshot = base64.b64encode(screenshot_bytes).decode("utf-8")
+        return last_successful_screenshot
+    except Exception as e:
+        print(f"Screenshot failed: {e}")
+        print(f"Using cached screenshot from previous successful capture")
+        if last_successful_screenshot:
+            return last_successful_screenshot
+
+
+async def process_model_response(client, response, page, max_iterations=ITERATIONS):
+    """Process the model's response and execute actions."""
+    for iteration in range(max_iterations):
+        if not hasattr(response, 'output') or not response.output:
+            print("No output from model.")
+            break
+        
+        # Safely access response id
+        response_id = getattr(response, 'id', 'unknown')
+        print(f"\nIteration {iteration + 1} - Response ID: {response_id}\n")
+        
+        # Print text responses and reasoning
+        for item in response.output:
+            # Handle text output
+            if hasattr(item, 'type') and item.type == "text":
+                print(f"\nModel message: {item.text}\n")
+                
+            # Handle reasoning output
+            if hasattr(item, 'type') and item.type == "reasoning":
+                # Extract meaningful content from the reasoning
+                meaningful_content = []
+                
+                if hasattr(item, 'summary') and item.summary:
+                    for summary in item.summary:
+                        # Handle different potential formats of summary content
+                        if isinstance(summary, str) and summary.strip():
+                            meaningful_content.append(summary)
+                        elif hasattr(summary, 'text') and summary.text.strip():
+                            meaningful_content.append(summary.text)
+                
+                # Only print reasoning section if there's actual content
+                if meaningful_content:
+                    print("=== Model Reasoning ===")
+                    for idx, content in enumerate(meaningful_content, 1):
+                        print(f"{content}")
+                    print("=====================\n")
+        
+        # Extract computer calls
+        computer_calls = [item for item in response.output 
+                         if hasattr(item, 'type') and item.type == "computer_call"]
+        
+        if not computer_calls:
+            print("No computer call found in response. Reverting control to human supervisor")
+            break
+        
+        computer_call = computer_calls[0]
+        if not hasattr(computer_call, 'call_id') or not hasattr(computer_call, 'action'):
+            print("Computer call is missing required attributes.")
+            break
+        
+        call_id = computer_call.call_id
+        action = computer_call.action
+        
+        # Handle safety checks
+        acknowledged_checks = []
+        if hasattr(computer_call, 'pending_safety_checks') and computer_call.pending_safety_checks:
+            pending_checks = computer_call.pending_safety_checks
+            print("\nSafety checks required:")
+            for check in pending_checks:
+                print(f"- {check.code}: {check.message}")
+            
+            if input("\nDo you want to proceed? (y/n): ").lower() != 'y':
+                print("Operation cancelled by user.")
+                break
+            
+            acknowledged_checks = pending_checks
+        
+        # Execute the action
+        try:
+           await page.bring_to_front()
+           await handle_action(page, action)
+           
+           # Check if a new page was created after the action
+           if action.type in ["click"]:
+               await asyncio.sleep(1.5)
+               # Get all pages in the context
+               all_pages = page.context.pages
+               # If we have multiple pages, check if there's a newer one
+               if len(all_pages) > 1:
+                   newest_page = all_pages[-1]  # Last page is usually the newest
+                   if newest_page != page and newest_page.url not in ["about:blank", ""]:
+                       print(f"\tSwitching to new tab: {newest_page.url}")
+                       page = newest_page  # Update our page reference
+           elif action.type != "wait":
+               await asyncio.sleep(0.5)
+               
+        except Exception as e:
+           print(f"Error handling action {action.type}: {e}")
+           import traceback
+           traceback.print_exc()    
+
+        # Take a screenshot after the action
+        screenshot_base64 = await take_screenshot(page)
+
+        print("\tNew screenshot taken")
+        
+        # Prepare input for the next request
+        input_content = [{
+            "type": "computer_call_output",
+            "call_id": call_id,
+            "output": {
+                "type": "input_image",
+                "image_url": f"data:image/png;base64,{screenshot_base64}"
+            }
+        }]
+        
+        # Add acknowledged safety checks if any
+        if acknowledged_checks:
+            acknowledged_checks_dicts = []
+            for check in acknowledged_checks:
+                acknowledged_checks_dicts.append({
+                    "id": check.id,
+                    "code": check.code,
+                    "message": check.message
+                })
+            input_content[0]["acknowledged_safety_checks"] = acknowledged_checks_dicts
+        
+        # Add current URL for context
+        try:
+            current_url = page.url
+            if current_url and current_url != "about:blank":
+                input_content[0]["current_url"] = current_url
+                print(f"\tCurrent URL: {current_url}")
+        except Exception as e:
+            print(f"Error getting URL: {e}")
+        
+        # Send the screenshot back for the next step
+        try:
+            response = client.responses.create(
+                model=MODEL,
+                previous_response_id=response_id,
+                tools=[{
+                    "type": "computer_use_preview",
+                    "display_width": DISPLAY_WIDTH,
+                    "display_height": DISPLAY_HEIGHT,
+                    "environment": "browser"
+                }],
+                input=input_content,
+                truncation="auto"
+            )
+
+            print("\tModel processing screenshot")
+        except Exception as e:
+            print(f"Error in API call: {e}")
+            import traceback
+            traceback.print_exc()
+            break
+    
+    if iteration >= max_iterations - 1:
+        print("Reached maximum number of iterations. Stopping.")
+        
+async def main():    
+    # Initialize OpenAI client
+    client = AzureOpenAI(
+        azure_endpoint=AZURE_ENDPOINT,
+        azure_ad_token_provider=token_provider,
+        api_version=API_VERSION
+    )
+    
+    # Initialize Playwright
+    async with async_playwright() as playwright:
+        browser = await playwright.chromium.launch(
+            headless=False,
+            args=[f"--window-size={DISPLAY_WIDTH},{DISPLAY_HEIGHT}", "--disable-extensions"]
+        )
+        
+        context = await browser.new_context(
+            viewport={"width": DISPLAY_WIDTH, "height": DISPLAY_HEIGHT},
+            accept_downloads=True
+        )
+        
+        page = await context.new_page()
+        
+        # Navigate to starting page
+        await page.goto("https://www.bing.com", wait_until="domcontentloaded")
+        print("Browser initialized to Bing.com")
+        
+        # Main interaction loop
+        try:
+            while True:
+                print("\n" + "="*50)
+                user_input = input("Enter a task to perform (or 'exit' to quit): ")
+                
+                if user_input.lower() in ('exit', 'quit'):
+                    break
+                
+                if not user_input.strip():
+                    continue
+                
+                # Take initial screenshot
+                screenshot_base64 = await take_screenshot(page)
+                print("\nTake initial screenshot")
+                
+                # Initial request to the model
+                response = client.responses.create(
+                    model=MODEL,
+                    tools=[{
+                        "type": "computer_use_preview",
+                        "display_width": DISPLAY_WIDTH,
+                        "display_height": DISPLAY_HEIGHT,
+                        "environment": "browser"
+                    }],
+                    instructions = "You are an AI agent with the ability to control a browser. You can control the keyboard and mouse. You take a screenshot after each action to check if your action was successful. Once you have completed the requested task you should stop running and pass back control to your human supervisor.",
+                    input=[{
+                        "role": "user",
+                        "content": [{
+                            "type": "input_text",
+                            "text": user_input
+                        }, {
+                            "type": "input_image",
+                            "image_url": f"data:image/png;base64,{screenshot_base64}"
+                        }]
+                    }],
+                    reasoning={"generate_summary": "concise"},
+                    truncation="auto"
+                )
+                print("\nSending model initial screenshot and instructions")
+
+                # Process model actions
+                await process_model_response(client, response, page)
+                
+        except Exception as e:
+            print(f"An error occurred: {e}")
+            import traceback
+            traceback.print_exc()
+        
+        finally:
+            # Close browser
+            await context.close()
+            await browser.close()
+            print("Browser closed.")
+
+if __name__ == "__main__":
+    asyncio.run(main())
+```
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIのレスポンスAPIに関する新しいドキュメントの追加"
}
```

### Explanation
この変更は、Azure OpenAIの新しい「レスポンスAPI」に関する包括的なドキュメントを追加したものです。このAPIは、チャット完了およびアシスタントAPIの機能を統合したもので、ユーザーは新しい「computer-use-preview」モデルを使用して、より複雑なインタラクションを実現できます。

新たに追加されたページでは、以下の内容が詳細されています。

- **APIの概要とサポートバージョン**: `2025-03-01-preview`以降に対応していることや、プロンプトキャッシング機能を持つモデルについて紹介されています。
- **利用可能地域**: オーストラリア東部、米国東部、スウェーデン中央などの地域でAPIが利用可能であることが記されています。
- **モデルのサポート**: `gpt-4o`や`gpt-4o-mini`、`computer-use-preview`といったモデルがサポートされていること。
- **使用方法**: PythonとAPIキーを使用した具体的なコード例が添えられており、テキストレスポンスやレスポンスの取得、削除に関する詳細な説明が行われています。
- **計算および画像の入力処理例**: Playwrightを使用して、コンピュータの操作を行うための自動化スクリプトの例が提供されており、ユーザーはこのAPIを使ってブラウザ上での対話的な操作を行うことができます。

このドキュメントは、開発者がAzureの新しいレスポンスAPIを活用し、自身のアプリケーションに組み込むための強力な道筋を示すものとなります。

## articles/ai-services/openai/includes/api-surface.md{#item-a25fa2}

<details>
<summary>Diff</summary>
````diff
@@ -22,8 +22,8 @@ Each API surface/specification encapsulates a different set of Azure OpenAI capa
 | API | Latest preview release | Latest GA release | Specifications | Description |
 |:---|:----|:----|:----|:---|
 | **Control plane** | [`2024-06-01-preview`](/rest/api/aiservices/accountmanagement/operation-groups?view=rest-aiservices-accountmanagement-2024-06-01-preview&preserve-view=true) | [`2024-10-01`](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices) | Azure OpenAI shares a common control plane with all other Azure AI Services. The control plane API is used for things like [creating Azure OpenAI resources](/rest/api/aiservices/accountmanagement/accounts/create?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), [model deployment](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), and other higher level resource management tasks. The control plane also governs what is possible to do with capabilities like Azure Resource Manager, Bicep, Terraform, and Azure CLI.|
-| **Data plane - authoring** | `2025-02-01-preview` | `2024-10-21` | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
-| **Data plane - inference** | [`2025-02-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-10-21`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, speech/whisper, on your data, Dall-e, assistants, etc. |
+| **Data plane - authoring** | `2025-03-01-preview` | `2024-10-21` | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
+| **Data plane - inference** | [`2025-03-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-10-21`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, speech/whisper, on your data, Dall-e, assistants, etc. |
 
 ## Authentication
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データプレーンAPIの著作および推論のバージョン更新"
}
```

### Explanation
この変更は、Azure OpenAIのAPIサーフェスに関するドキュメントの一部を更新しています。具体的には、データプレーンAPIに関する著作および推論のバージョン情報が更新されました。以下の点が主な内容です。

1. **データプレーン - 著作**: APIのプレビュー版が `2025-02-01-preview` から `2025-03-01-preview` に変更され、最新GAリリースは `2024-10-21` のままとされています。
2. **データプレーン - 推論**: プレビュー版として `2025-02-01-preview` の行が `2025-03-01-preview` に更新され、最新GAリリースは `2024-10-21` のまま維持されています。

これにより、開発者はデータプレーンAPIの異なる機能バージョンを把握しやすくなり、APIの使用時に最新の情報に基づいて開発を行うことができるようになります。APIの各セクションは、Azure OpenAIサービスのリソースや機能と一貫して動作することを目指しています。ユーザーは、最新のAPI仕様にアクセスし、適切に利用できるようになることを期待できます。

## articles/ai-services/openai/includes/api-versions/latest-inference-preview.md{#item-24bf0f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新の推論プレビューAPIに関するドキュメントの更新"
}
```

### Explanation
この変更は、最新の推論プレビューAPIに関するドキュメントにおける大幅な更新を示しています。具体的には、以下のポイントが含まれています。

1. **ドキュメントの追加および削除**: 2944行の新しい内容が追加された一方で、2351行の古い内容が削除されており、合計5295行の変更が行われました。これは、ドキュメントが大きく改訂されたことを示しています。

2. **情報の充実**: 新しい内容には、最新のAPIの機能、使用方法、要求仕様など、詳細な情報が含まれている可能性があります。これにより、開発者は最新の推論プレビューAPIを効率的に活用できるようになります。

3. **仕様の最新化**: この更新により、開発者は、新機能や改善された処理能力に基づいてアプリケーションを調整し、最適な結果を得ることができるようになります。

このように、推論APIに関するドキュメントの内容が大幅に更新されることで、Azure OpenAIを利用するユーザーにとって、より明確で役立つリソースが提供されることになります。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -11,26 +11,26 @@ ms.date: 03/13/2025
 
 | **Region**     | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4o-audio-preview**, **2024-12-17**   | **gpt-4o-mini-realtime-preview**, **2024-12-17**   | **gpt-4o-mini-audio-preview**, **2024-12-17**   | **gpt-4**, **turbo-2024-04-09**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **2**   |
 |:-------------------|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:----------------------------------------:|:------------------------------------------------:|:---------------------------------------------:|:-------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|
-| australiaeast      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| brazilsouth        | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| canadaeast         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
+| australiaeast      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| brazilsouth        | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| canadaeast         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
 | eastus             | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                          | ✅                            | ✅                              | ✅                              | ✅                              |
-| eastus2            | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | ✅                                          | ✅                            | -                             | ✅                              | -                             |
-| francecentral      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| germanywestcentral | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| japaneast          | -                       | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| koreacentral       | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| northcentralus     | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| norwayeast         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| polandcentral      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| southafricanorth   | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
+| eastus2            | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | ✅                                          | ✅                            | ✅                              | ✅                              | -                             |
+| francecentral      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| germanywestcentral | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| japaneast          | -                       | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| koreacentral       | -                       | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| northcentralus     | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| norwayeast         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| polandcentral      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| southafricanorth   | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
 | southcentralus     | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| southindia         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| spaincentral       | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| swedencentral      | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | -                                         | ✅                            | -                             | ✅                              | -                             |
-| switzerlandnorth   | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| uaenorth           | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| uksouth            | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| westeurope         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| westus             | -                       | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
-| westus3            | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | -                             | ✅                              | -                             |
+| southindia         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| spaincentral       | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| swedencentral      | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| switzerlandnorth   | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| uaenorth           | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| uksouth            | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| westeurope         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| westus             | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| westus3            | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準グローバルモデルマトリックスの更新"
}
```

### Explanation
この変更は、標準グローバルモデルマトリックスに関するドキュメントを更新したもので、以下の点が主な内容です。

1. **行数の変更**: 21行の新しい内容が追加され、同じく21行の古い内容が削除され、合計42行の変更が行われました。これにより、ドキュメントの内容が最新の情報に基づくようになっています。

2. **機能の追加と更新**: 各地域でのモデルの利用可能性やバージョン情報の変更が含まれており、特定のモデルの最新リリース日やステータスが明確に示されています。これにより、開発者はどの地域でどのモデルが利用可能かを把握しやすくなります。

3. **新しいモデルの追加**: 更新された情報には、新たに登場したモデルの情報や、既存モデルの新しいバージョンが反映されている可能性があります。これにより、ユーザーが最新の技術を活用できるようになります。

この更新により、Azure OpenAIを利用する開発者は、利用可能なモデルの最新情報を把握し、それに基づいた開発や実装を行うことが容易になります。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: mrbullwinkle
 ms.author: mbullwin
 ms.service: azure-ai-openai
 ms.topic: overview
-ms.date: 01/30/2025
+ms.date: 03/25/2025
 ms.custom: build-2023, build-2023-dataai
 recommendations: false
 ---
@@ -20,7 +20,7 @@ Azure OpenAI Service provides REST API access to OpenAI's powerful language mode
 
 | Feature | Azure OpenAI |
 | --- | --- |
-| Models available | [**o3-mini & o1**](./how-to/reasoning.md) <br>[**o1-mini**](./how-to/reasoning.md)<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
+| Models available | [**computer-use-preview**](./concepts/models.md#computer-use-preview)<br>[**o3-mini & o1**](./how-to/reasoning.md) <br>[**o1-mini**](./how-to/reasoning.md)<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
 | Fine-tuning | `GPT-4o-mini` (preview) <br> `GPT-4` (preview) <br>`GPT-3.5-Turbo` (0613).|
 | Price | [Available here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> For details on vision-enabled chat models, see the [special pricing information](../openai/concepts/gpt-with-vision.md#special-pricing-information).|
 | Virtual network support & private link support | Yes.  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OpenAI サービスの概要ドキュメントの更新"
}
```

### Explanation
この変更は、OpenAIサービスの概要に関するドキュメントに対する小さな更新を示しています。以下のポイントが要約されています。

1. **日付の更新**: 更新されたドキュメントの日付が「2025年1月30日」から「2025年3月25日」へと変更されており、これはドキュメント内容が最近の情報に基づいていくつかの点で進化したことを示しています。

2. **モデルの情報の追加**: 利用可能なモデルのリストに「computer-use-preview」が追加されました。この新しいモデルは、ユーザーに対して追加的な機能や用途を提供することを示唆しています。

3. **情報の整理**: モデルの説明が変更され、利用可能なモデルの各種名が明確に区分けされ、リンク先も整理されたことから、利用者が必要な情報を見つけやすくなっています。

これらの変更により、Azure OpenAIサービスを利用する開発者やユーザーは、最新のモデル情報およびサービス内容をより効果的に把握し、活用できるようになります。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -57,11 +57,16 @@ The following sections provide you with a quick guide to the default quotas and
 
 ## Regional quota limits
 
-[!INCLUDE [Quota](./includes/model-matrix/quota.md)]
-
 [!INCLUDE [Quota](./includes/global-batch-limits.md)]
 
-### GPT-4.5 Preview global standard
+## computer-use-preview global standard
+
+| Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
+|---|---|:---:|:---:|
+| `computer-use-preview`| Enterprise Tier | 30 M | 300 K |
+| `computer-use-preview`| Default         | 450 K | 4.5 K |
+
+## GPT-4.5 Preview global standard
 
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
 |---|---|:---:|:---:|
@@ -93,13 +98,14 @@ The following sections provide you with a quick guide to the default quotas and
 | `o1` & `o1-preview` | Default | 3 M | 500 |
 | `o1-mini`| Default | 5 M | 500 |
 
-### `o3-mini` data zone standard
+### `o-series` data zone standard
 
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
 |---|---|:---:|:---:|
 | `o3-mini` | Enterprise agreement | 20 M | 2 K  |
 | `o3-mini` | Default | 2 M | 200 |
-
+| `o1` | Enterprise agreement | 6 M | 1 K |
+| `o1` | Default | 600 K | 100 |
 
 ### o1-preview & o1-mini standard
 
@@ -194,8 +200,8 @@ If your Azure subscription is linked to certain [offer types](https://azure.micr
 |Tier| Quota Limit in tokens per minute (TPM) |
 |---|:---|
 |Azure for Students, Free Trials | 1 K (all models) <br>Exception o-series & GPT 4.5 Preview: 0|
-| MSDN & Cloud Solution Provider (CSP) subscriptions | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br> gpt-4o-realtime-preview: 1 K <br> o-series: 0 <br> GPT 4.5 Preview: 0  |
-| Monthly credit card based subscriptions <sup>1</sup> | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br> o-series: 0 <br> GPT 4.5 Preview: 0   |
+| MSDN & Cloud Solution Provider (CSP) subscriptions | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br>computer-use-preview: 30 K <br> gpt-4o-realtime-preview: 1 K <br> o-series: 0 <br> GPT 4.5 Preview: 0  |
+| Monthly credit card based subscriptions <sup>1</sup> | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br>computer-use-preview: 30 K <br> o-series: 0 <br> GPT 4.5 Preview: 0   |
 
 <sup>1</sup> This currently applies to [offer type 0003P](https://azure.microsoft.com/support/legal/offer-details/)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータと制限に関するドキュメントの更新"
}
```

### Explanation
この変更は、OpenAIサービスのクォータと制限に関するドキュメントを更新したもので、以下の主な点が含まれています。

1. **新しいモデルの追加**: 「computer-use-preview」という新しいモデルが追加され、そのクォータ制限が記載されました。具体的には、エンタープライズティアでの30Mトークン/分およびデフォルトでの450Kトークン/分という制限が設定されています。この情報は、開発者に対して新しいサービス利用の可能性を示しています。

2. **既存モデルに関する情報更新**: GPT-4.5プレビューの情報がそれに続いて更新され、最新のクォータ制限が示されています。また、o3-miniモデルのデータゾーン標準が「oシリーズ」に改称され、そのクォータ設定が明確になりました。

3. **クォータ制限の見直し**: 他のサブスクリプションオプションに対するクォータ制限も見直され、特にMSDNおよびCloud Solution Provider (CSP) サブスクリプションに関する更新が行われています。「computer-use-preview」モデルが新たに30Kトークン/分の利用制限が加わりました。

これらの変更により、ユーザーは新しいモデルのクォータと制限についての詳細を把握し、計画的な利用を行うことができるようになります。また、更新された情報は、Azure OpenAIサービスの利用に対する理解を深めるのに役立ちます。

## articles/ai-services/openai/reference-preview.md{#item-e197a2}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's latest preview REST API. In this ar
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 01/29/2025
+ms.date: 03/25/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -20,7 +20,7 @@ This article provides details on the inference REST API endpoints for Azure Open
 
 ## Data plane inference
 
-The rest of the article covers the latest preview release of the Azure OpenAI data plane inference specification, `2025-02-01-preview`. This article includes documentation for the latest preview capabilities like assistants, threads, and vector stores.
+The rest of the article covers the latest preview release of the Azure OpenAI data plane inference specification, `2025-03-01-preview`. This article includes documentation for the latest preview capabilities like assistants, threads, and vector stores.
 
 If you're looking for documentation on the latest GA API release, refer to the [latest GA data plane inference API](./reference.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI の参照プレビュードキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAIの参照プレビュードキュメントに対する小さな更新を示しています。以下の重要な点が反映されています。

1. **日付の更新**: ドキュメントの日付が「2025年1月29日」から「2025年3月25日」へと変更され、これは最新の情報に基づく更新を示しています。

2. **プレビュースペックのバージョン変更**: データプレーン推論仕様の最新プレビューリリースが「2025年2月1日プレビューバージョン」から「2025年3月1日プレビューバージョン」に更新されました。この変更は、新機能や改善点が含まれていることを示唆しています。

3. **情報の明確化**: ドキュメントの内容は、アシスタントやスレッド、ベクターストアなどの最新のプレビュ機能についての情報を提供しており、ユーザーが新機能を理解しやすくなっています。

これらの更新により、開発者やユーザーは最新のAPI情報を把握し、Azure OpenAIサービスの新機能を効果的に利用できるようになります。また、更新されたリリース情報は、サービスの使用を計画する上で役立つでしょう。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -112,13 +112,18 @@ items:
         href: ./how-to/file-search.md
   - name: Batch
     href: ./how-to/batch.md
-  - name: Completions & chat completions
+  - name: Responses & chat completions
     items:
+    - name: Responses API
+      href: ./how-to/responses.md
     - name: Reasoning models
       href: ./how-to/reasoning.md
     - name: GPT-35-Turbo & GPT-4 
       href: ./how-to/chatgpt.md
       displayName: ChatGPT, chatgpt
+    - name: Computer Use
+      href: ./how-to/computer-use.md
+      displayName: cua, computer using model
     - name: Vision-enabled chats
       href: ./how-to/gpt-with-vision.md
     - name: DALL-E
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OpenAI サービスの目次ファイルの更新"
}
```

### Explanation
この変更は、OpenAIサービスの目次（toc.yml）ファイルに対する小さな更新を示しています。主なポイントは以下の通りです。

1. **項目名の変更**: 「Completions & chat completions」という項目名が「Responses & chat completions」に変更されました。この変更は、APIの機能をより正確に反映するためのものです。

2. **新しいセクションの追加**: 
   - 「Responses API」が新たに追加され、そのリンク（./how-to/responses.md）が提供されています。これにより、ユーザーは応答APIに関する情報に簡単にアクセスできるようになります。
   - 「Computer Use」という新しいセクションが追加され、関連するリンク（./how-to/computer-use.md）も設定されています。これにより、コンピュータ利用モデルにアクセスするための情報が明確に示されます。

3. **その他の項目の整理**: 「Reasoning models」や「Vision-enabled chats」などの他の項目はそのまま保持されており、これらのセクションもユーザーが必要な情報を見つけるための手助けとなります。

これらの変更は、ドキュメントの整理を進め、ユーザーがOpenAIサービスに関連する情報をより利用しやすくすることを目的としています。また、新しいAPIや機能へのアクセスを明示化することで、開発者にとっての利便性を向上させています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -21,6 +21,16 @@ This article provides a summary of the latest releases and major documentation u
 
 ## March 2025
 
+### Responses API & computer-use-preview model
+
+The [Responses API](./how-to/responses.md) is a new stateful API from Azure OpenAI. It brings together the best capabilities from the chat completions and assistants API in one unified experience. The Responses API also adds support for the new `computer-use-preview` model which powers the [Computer use](./how-to/computer-use.md) capability.
+
+**For access to `computer-use-preview` registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who have access to other limited access models will still need to request access for this model.
+
+Request access: [`computer-use-preview` limited access model application](https://aka.ms/oai/cuaaccess)
+
+For more information on model capabilities, and region availability see the [models documentation](./concepts/models.md#computer-use-preview).
+
 ### Provisioned spillover (preview)
 
 Spillover manages traffic fluctuations on provisioned deployments by routing overages to a designated standard deployment. To learn more about how to maximize utilization for your provisioned deployments with spillover, see [Manage traffic with spillover for provisioned deployments (preview)](./how-to/spillover-traffic-management.md).
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIの新機能に関する更新"
}
```

### Explanation
この変更は、Azure OpenAIの「What's New」ドキュメントに対する新機能の追加を示しています。主なポイントは以下の通りです。

1. **新しいAPIの紹介**: 
   - **Responses API**が新たに追加されました。このAPIはAzure OpenAIからの新しいステートフルAPIであり、チャット完了およびアシスタントAPIの優れた機能を統合した体験を提供します。これにより、ユーザーは一貫した操作性を享受できるようになります。

2. **新モデルのサポート**: 
   - **computer-use-previewモデル**がResponses APIに追加され、このモデルは「コンピュータ利用」（Computer use）機能をサポートします。これにより、ユーザーは新しい機能やモデルにアクセスできるようになります。

3. **アクセスポリシーの明示**: 
   - `computer-use-preview`モデルへのアクセスには登録が必要であり、Microsoftの適格基準に基づいてアクセスが承認されることが強調されています。既存の制限付きモデルにアクセスを持つ顧客も、このモデルのアクセスのためには別途リクエストが必要です。

4. **アクセスリクエストのリンク**: 
   - ユーザーは`computer-use-preview`モデルのアクセスをリクエストするためのリンク（[`computer-use-preview` limited access model application](https://aka.ms/oai/cuaaccess)）が提供されています。

5. **モデルの能力と地域利用可能性に関する情報**: 
   - モデルの能力や地域の利用可能性についての詳細は、モデルのドキュメンテーション（[models documentation](./concepts/models.md#computer-use-preview)）で確認できる旨が記載されています。

これらの更新により、ユーザーは新しいAPIとモデルについての重要な情報を把握でき、Azure OpenAIサービスの新機能を効果的に活用できるようになります。また、利用にあたっての条件や手続きも明確に示されています。


