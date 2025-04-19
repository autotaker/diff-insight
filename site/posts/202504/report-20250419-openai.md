---
date: '2025-04-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d942a6a...MicrosoftDocs:57a614f
summary: この記事では、Azure OpenAIサービスに関する技術文書の更新内容をまとめています。主な変更点として、新たに追加された推論サマリー機能により、モデルの思考過程をより深く理解できるようになったことが挙げられます。また、モデルの説明が明確化され、顧客管理キーに関する情報が更新され、レスポンスAPIには新しいモデルとストリーミング機能が追加されました。全体として、これらの変更はユーザー体験を向上させ、より信頼性のある結果を得る手助けとなります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d942a6a...MicrosoftDocs:57a614f){target="_blank"}

# ハイライト

この記事では、Azure OpenAIサービスに関連する複数の技術文書に対する更新内容をご紹介します。このドキュメントの変更では、モデルの説明の改善、新しい機能の追加、および既存機能の詳細な情報の提供が行われています。

## 新機能
- 推論サマリー機能が追加されました。この新機能で、`o3`および`o4-mini`モデルによる思考過程のサマリーを受け取ることができ、より深い理解が可能となります。

## 破壊的変更
- 破壊的な変更は特に報告されていません。

## その他の更新
- Azure OpenAIのモデル説明が整理され、明確化されました。
- 「データの静止時の暗号化」に関連する情報が最新化され、特に顧客管理キー（CMK）に関する注記が追加されました。
- 「レスポンスAPI」に新しいモデルのサポートとストリーミング機能のセクションが追加されました。

# インサイト

Azure OpenAIの各技術文書に対する最近の更新は、ユーザー体験と理解を向上させることを目的としています。特に、新機能である推論サマリーの追加は、モデルの思考過程を可視化する重要な役割を果たします。これにより、モデルの出力をより深く理解し、より信頼性のある結果を得ることが可能になります。選択可能なサマリーパラメーターも、ユーザーのニーズに応じたカスタマイズをサポートしています。

さらに、顧客管理キーに関する注記の更新は、サービスの制限を明確にすることでユーザーの混乱を避けるとともに、セキュリティに対する理解を深めます。

新しいモデルとストリーミング機能を組み込んだレスポンスAPIの更新も、リアルタイムでのデータ取得を可能にすることで、インタラクティブな体験を提供し、開発者の利便性を向上させます。

これらの変更によってドキュメントはより洗練され、分かりやすくなり、Azure OpenAIの利用者が提供されるテクノロジーを最大限に活用できる手助けとなります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | モデルの説明を更新しました | modified | 2 | 2 | 4 | 
| [encrypt-data-at-rest.md](#item-765ec8) | minor update | 情報を更新し、注記を追加しました | modified | 4 | 1 | 5 | 
| [reasoning.md](#item-a54b2f) | new feature | 推論サマリー機能を追加しました | modified | 139 | 8 | 147 | 
| [responses.md](#item-b9757d) | minor update | 新しいモデルとストリーミング機能を追加 | modified | 35 | 0 | 35 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -99,8 +99,8 @@ The Azure OpenAI o<sup>&#42;</sup> series models are specifically designed to ta
 
 |  Model ID  | Description | Max Request (tokens) | Training Data (up to)  |
 |  --- |  :--- |:--- |:---: |
-| `o4-mini` (2025-04-16) | - **NEW** reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br><br> - Chat Completions API <br> - [Responses API](../how-to/responses.md) (**Feature coming soon!**)  <br>- Structured outputs<br> - Text, image processing <br> - Functions/Tools/Parallel tool calling <br> [Full summary of capabilities](../how-to/reasoning.md) | Input: 200,000 <br> Output: 100,000 | May 31, 2024 |   
-| `o3` (2025-04-16) | - **NEW** reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br>  <br> - Chat Completions API <br> - [Responses API](../how-to/responses.md) (**Feature coming soon!**) <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools/Parallel tool calling <br> [Full summary of capabilities](../how-to/reasoning.md) | Input: 200,000 <br> Output: 100,000 | May 31, 2024 |    
+| `o4-mini` (2025-04-16) | - **NEW** reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br><br> - Chat Completions API <br> - [Responses API](../how-to/responses.md) <br>- Structured outputs<br> - Text, image processing <br> - Functions/Tools/Parallel tool calling <br> [Full summary of capabilities](../how-to/reasoning.md) | Input: 200,000 <br> Output: 100,000 | May 31, 2024 |   
+| `o3` (2025-04-16) | - **NEW** reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br>  <br> - Chat Completions API <br> - [Responses API](../how-to/responses.md) <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools/Parallel tool calling <br> [Full summary of capabilities](../how-to/reasoning.md) | Input: 200,000 <br> Output: 100,000 | May 31, 2024 |    
 | `o3-mini` (2025-01-31) | - [Enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text-only processing <br> - Functions/Tools | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
 | `o1` (2024-12-17) | - [Enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
 |`o1-preview` (2024-09-12) | Older preview version | Input: 128,000  <br> Output: 32,768 | Oct 2023 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの説明を更新しました"
}
```

### Explanation
この変更は、Azure OpenAIのモデルに関する文書の一部を更新したものです。具体的には、モデルの説明の書式が一部修正され、情報が整理されました。`o4-mini`と`o3`モデルに関する記述が、特定の機能についてより明確に伝わるように調整されています。また、いくつかの要素が削除され、その代わりにより簡潔で理解しやすい形式で情報が提示されるようになっています。この変更により、利用者はモデルの特徴や機能をより理解しやすくなります。

## articles/ai-services/openai/encrypt-data-at-rest.md{#item-765ec8}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: mrbullwinkle
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 03/27/2025
+ms.date: 04/17/2025
 ms.author: mbullwin
 ---
 
@@ -39,6 +39,9 @@ Only RSA and RSA-HSM keys of size 2048 are supported with Azure AI services encr
 
 ### Enable your Azure OpenAI resource's managed identity
 
+> [!NOTE]
+> Azure OpenAI only supports customer-managed keys (CMK) with system-assigned managed identities. User-assigned managed identities are not supported with Azure OpenAI and customer-managed keys (CMK).
+
 1. Go to your Azure AI services resource.
 1. On the left, under **Resource Management**, select **Identity**.
 1. Switch the system-assigned managed identity status to **On**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "情報を更新し、注記を追加しました"
}
```

### Explanation
この変更は、Azure OpenAIの「データの静止時の暗号化」に関する文書の更新を示しています。主な変更点は、文書の日付が2025年3月27日から2025年4月17日に更新されたことです。また、顧客が管理するキー（CMK）についての新しい注記が追加されました。この注記では、Azure OpenAIがサポートする顧客管理のキーに関して、システム割り当てのマネージドIDのみがサポートされ、ユーザー割り当てのマネージドIDはサポートされていないことが明記されています。このようにして、利用者はサービスの制限をより理解しやすくなり、誤解を避けることができます。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's advanced o3-mini, o1, & o1-mini rea
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 04/16/2025
+ms.date: 04/18/2025
 author: mrbullwinkle    
 ms.author: mbullwin
 ---
@@ -39,19 +39,19 @@ Azure OpenAI `o-series` models are designed to tackle reasoning and problem-solv
 
 | **Feature**     | **o4-mini**, **2025-04-16**  | **o3**, **2025-04-16** | **o3-mini**, **2025-01-31**  |**o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   |
 |:-------------------|:--------------------------:|:-----:|:-------:|:--------------------------:|:-------------------------------:|:---:|
-| **API Version**    | `2025-03-01-preview`   | `2025-03-01-preview`   | `2024-12-01-preview` or later <br> `2025-03-01-preview` (Recommended)   | `2024-12-01-preview` or later <br> `2025-03-01-preview` (Recommended) | `2024-09-01-preview` or later <br> `2025-03-01-preview` (Recommended)    | `2024-09-01-preview` or later <br> `2025-03-01-preview` (Recommended)    |
+| **API Version**    | `2025-04-01-preview`   | `2025-04-01-preview`   | `2024-12-01-preview` or later <br> `2025-03-01-preview` (Recommended)   | `2024-12-01-preview` or later <br> `2025-03-01-preview` (Recommended) | `2024-09-01-preview` or later <br> `2025-03-01-preview` (Recommended)    | `2024-09-01-preview` or later <br> `2025-03-01-preview` (Recommended)    |
 | **[Developer Messages](#developer-messages)** | ✅ | ✅ | ✅ | ✅ | - | - |
 | **[Structured Outputs](./structured-outputs.md)** | ✅ | ✅ | ✅ | ✅ | - | - |
 | **[Context Window](../concepts/models.md#o-series-models)** | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 128,000  <br> Output: 32,768 | Input: 128,000  <br> Output: 65,536 |
 | **[Reasoning effort](#reasoning-effort)** | ✅| ✅ |✅ | ✅ | - | - |
 | **[Vision Support](./gpt-with-vision.md)** | ✅ | ✅ | - | ✅ | - | - |
 | Chat Completions API | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| Responses API | ✅ (**Feature coming soon!**) | ✅ (**Feature coming soon!**) | - | - | - | - |
+| Responses API | ✅ | ✅  | - | - | - | - |
 | Functions/Tools | ✅ | ✅ | ✅  | ✅  |  - | - |
 | Parallel Tool Calls | ✅ | ✅ | -  | -  |  - | - |
 | `max_completion_tokens`<sup>*</sup> | ✅ | ✅ |✅ |✅ |✅ | ✅ |
 | System Messages<sup>**</sup> | ✅ | ✅ | ✅ | ✅ | - | - |
-| Reasoning summary <sup>***</sup> | ✅ (**Feature coming soon!**) | ✅ (**Feature coming soon!**) | -  | -  |  - | - |
+| [Reasoning summary](#reasoning-summary) <sup>***</sup> | ✅ | ✅ | -  | -  |  - | - |
 | Streaming | ✅ | ✅ | ✅ | - | - | - |
 
 <sup>*</sup> Reasoning models will only work with the `max_completion_tokens` parameter. <br><br>
@@ -91,7 +91,7 @@ token_provider = get_bearer_token_provider(
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   azure_ad_token_provider=token_provider,
-  api_version="2024-12-01-preview"
+  api_version="2025-03-01-preview"
 )
 
 response = client.chat.completions.create(
@@ -121,7 +121,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-12-01-preview"
+  api_version="2025-03-01-preview"
 )
 
 response = client.chat.completions.create(
@@ -298,7 +298,7 @@ token_provider = get_bearer_token_provider(
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   azure_ad_token_provider=token_provider,
-  api_version="2024-12-01-preview"
+  api_version="2025-03-01-preview"
 )
 
 response = client.chat.completions.create(
@@ -330,7 +330,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-12-01-preview"
+  api_version="2025-03-01-preview"
 )
 
 response = client.chat.completions.create(
@@ -381,6 +381,137 @@ Console.WriteLine($"{completion.Role}: {completion.Content[0].Text}");
 
 ---
 
+## Reasoning summary
+
+When using the latest `o3` and `o4-mini` models with the [Responses API](./responses.md) you can use the reasoning summary parameter to receive summaries of the model's chain of thought reasoning. This parameter can be set to `auto`, `concise`, or `detailed`. Access to this feature requires you to [Request Access](https://aka.ms/oai/o3access).
+
+> [!NOTE]
+> Even when enabled, reasoning summaries are not generated for every step/request. This is expected behavior.
+
+# [Python](#tab/py)
+
+You'll need to upgrade your OpenAI client library for access to the latest parameters.
+
+```cmd
+pip install openai --upgrade
+```
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
+  api_version="2025-04-01-preview" # You must use this version or greater to access reasoning summary
+)
+
+response = client.responses.create(
+    input="Tell me about the curious case of neural text degeneration",
+    model="o4-mini", # replace with model deployment name
+    reasoning={
+        "effort": "medium",
+        "summary": "detailed" # auto, concise, or detailed (currently only supported with o4-mini and o3)
+    }
+)
+
+print(response.model_dump_json(indent=2))
+```
+
+# [REST](#tab/REST)
+
+```bash
+curl -X POST "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/responses?api-version=2025-04-01-preview" \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+ -d '{
+     "model": "o4-mini",
+     "input": "Tell me about the curious case of neural text degeneration",
+     "reasoning": {"summary": "detailed"}
+    }'
+```
+
+---
+
+```output
+{
+  "id": "resp_68007e26b2cc8190b83361014f3a78c50ae9b88522c3ad24",
+  "created_at": 1744862758.0,
+  "error": null,
+  "incomplete_details": null,
+  "instructions": null,
+  "metadata": {},
+  "model": "o4-mini",
+  "object": "response",
+  "output": [
+    {
+      "id": "rs_68007e2773bc8190b5b8089949bfe13a0ae9b88522c3ad24",
+      "summary": [
+        {
+          "text": "**Summarizing neural text degeneration**\n\nThe user's asking about \"The Curious Case of Neural Text Degeneration,\" a paper by Ari Holtzman et al. from 2020. It explains how certain decoding strategies produce repetitive and dull text. In contrast, methods like nucleus sampling yield more coherent and diverse outputs. The authors introduce metrics like surprisal and distinct-n for evaluation and suggest that maximum likelihood decoding often favors generic continuations, leading to loops and repetitive patterns in longer texts. They promote sampling from truncated distributions for improved text quality.",
+          "type": "summary_text"
+        },
+        {
+          "text": "**Explaining nucleus sampling**\n\nThe authors propose nucleus sampling, which captures a specified mass of the predictive distribution, improving metrics such as coherence and diversity. They identify a \"sudden drop\" phenomenon in token probabilities, where a few tokens dominate, leading to a long tail. By truncating this at a cumulative probability threshold, they aim to enhance text quality compared to top-k sampling. Their evaluations include human assessments, showing better results in terms of BLEU scores and distinct-n measures. Overall, they highlight how decoding strategies influence quality and recommend adaptive techniques for improved outcomes.",
+          "type": "summary_text"
+        }
+      ],
+      "type": "reasoning",
+      "status": null
+    },
+    {
+      "id": "msg_68007e35c44881908cb4651b8e9972300ae9b88522c3ad24",
+      "content": [
+        {
+          "annotations": [],
+          "text": "Researchers first became aware that neural language models, when used to generate long stretches of text with standard “maximum‐likelihood” decoding (greedy search, beam search, etc.), often produce bland, repetitive or looping output. The 2020 paper “The Curious Case of Neural Text Degeneration” (Holtzman et al.) analyzes this failure mode and proposes a simple fix—nucleus (top‑p) sampling—that dramatically improves output quality.\n\n1. The Problem: Degeneration  \n   • With greedy or beam search, models tend to pick very high‑probability tokens over and over, leading to loops (“the the the…”) or generic, dull continuations.  \n   • Even sampling with a fixed top‑k (e.g. always sample from the 40 most likely tokens) can be suboptimal: if the model’s probability mass is skewed, k may be too small (overly repetitive) or too large (introducing incoherence).\n\n2. Why It Happens: Distributional Peakedness  \n   • At each time step the model’s predicted next‐token distribution often has one or two very high‑probability tokens, then a long tail of low‑probability tokens.  \n   • Maximum‐likelihood decoding zeroes in on the peak, collapsing diversity.  \n   • Uniform sampling over a large k allows low‑probability “wild” tokens, harming coherence.\n\n3. The Fix: Nucleus (Top‑p) Sampling  \n   • Rather than fixing k, dynamically truncate the distribution to the smallest set of tokens whose cumulative probability ≥ p (e.g. p=0.9).  \n   • Then renormalize and sample from that “nucleus.”  \n   • This keeps only the “plausible” mass and discards the improbable tail, adapting to each context.\n\n4. Empirical Findings  \n   • Automatic metrics (distinct‑n, repetition rates) and human evaluations show nucleus sampling yields more diverse, coherent, on‑topic text than greedy/beam or fixed top‑k.  \n   • It also outperforms simple temperature scaling (raising logits to 1/T) because it adapts to changes in the distribution’s shape.\n\n5. Takeaways for Practitioners  \n   • Don’t default to beam search for open-ended generation—its high likelihood doesn’t mean high quality.  \n   • Use nucleus sampling (p between 0.8 and 0.95) for a balance of diversity and coherence.  \n   • Monitor repetition and distinct‑n scores if you need automatic sanity checks.\n\nIn short, “neural text degeneration” is the tendency of likelihood‐maximizing decoders to produce dull or looping text. By recognizing that the shape of the model’s probability distribution varies wildly from step to step, nucleus sampling provides an elegant, adaptive way to maintain both coherence and diversity in generated text.",
+          "type": "output_text"
+        }
+      ],
+      "role": "assistant",
+      "status": "completed",
+      "type": "message"
+    }
+  ],
+  "parallel_tool_calls": true,
+  "temperature": 1.0,
+  "tool_choice": "auto",
+  "tools": [],
+  "top_p": 1.0,
+  "max_output_tokens": null,
+  "previous_response_id": null,
+  "reasoning": {
+    "effort": "medium",
+    "generate_summary": null,
+    "summary": "detailed"
+  },
+  "status": "completed",
+  "text": {
+    "format": {
+      "type": "text"
+    }
+  },
+  "truncation": "disabled",
+  "usage": {
+    "input_tokens": 16,
+    "output_tokens": 974,
+    "output_tokens_details": {
+      "reasoning_tokens": 384
+    },
+    "total_tokens": 990,
+    "input_tokens_details": {
+      "cached_tokens": 0
+    }
+  },
+  "user": null,
+  "store": true
+}
+```
+
 ## Markdown output
 
 By default the `o3-mini` and `o1` models will not attempt to produce output that includes markdown formatting. A common use case where this behavior is undesirable is when you want the model to output code contained within a markdown code block. When the model generates output without markdown formatting you lose features like syntax highlighting, and copyable code blocks in interactive playground experiences. To override this new default behavior and encourage markdown inclusion in model responses, add the string `Formatting re-enabled` to the beginning of your developer message.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "推論サマリー機能を追加しました"
}
```

### Explanation
この変更は、Azure OpenAIの「推論」に関する文書を大幅に更新したもので、特に新しい機能として「推論サマリー」が追加されました。文書の日付が2025年4月16日から2025年4月18日に変更され、新機能に関する詳細な説明が含まれています。この推論サマリー機能により、最新の`o3`および`o4-mini`モデルを使用する際に、モデルの思考過程をまとめたサマリーを受け取ることができるようになります。具体的には、サマリーのパラメーターには「auto」、「concise」、「detailed」を選ぶことができ、この機能を利用するには事前にアクセスリクエストが必要です。

また、ドキュメントには新しいAPIバージョン及びコマンド、サンプルコードが追加され、推論サマリーの利用方法が具体的に示されています。これにより、開発者はより効果的にモデルの機能を活用し、各モデルのパラメータを適切に設定して利用する方法を学ぶことができるようになっています。全体として、この変更はユーザーに新しい情報を提供し、Azure OpenAIの利用体験を豊かにするものとなっています。

## articles/ai-services/openai/how-to/responses.md{#item-b9757d}

<details>
<summary>Diff</summary>
````diff
@@ -46,6 +46,8 @@ The responses API is currently available in the following regions:
 - `gpt-4.1` (Version: `2025-04-14`)
 - `gpt-4.1-nano` (Version: `2025-04-14`)
 - `gpt-4.1-mini` (Version: `2025-04-14`)
+- `o3` (Version: `2025-04-16`)
+- `o4-mini` (Version: `2025-04-16`)
 
 Not every model is available in the regions supported by the responses API. Check the [models page](../concepts/models.md) for model region availability.
 
@@ -460,6 +462,35 @@ second_response = client.responses.create(
 print(second_response.model_dump_json(indent=2))  
 ```
 
+## Streaming
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
+  azure_ad_token_provider = token_provider,
+  api_version = "2025-04-01-preview" 
+)
+
+response = client.responses.create(
+    input = "This is a test",
+    model = "o4-mini", # replace with model deployment name
+    stream = True
+)
+
+for event in response:
+    if event.type == 'response.output_text.delta':
+        print(event.delta, end='')
+
+```
+
+
 ## Function calling
 
 The responses API supports function calling.
@@ -658,6 +689,10 @@ response = client.responses.create(
 print(response)
 ```
 
+## Reasoning models
+
+For examples of how to use reasoning models with the responses API see the [reasoning models guide](./reasoning.md#reasoning-summary).
+
 ## Computer use
 
 In this section, we provide a simple example script that integrates Azure OpenAI's `computer-use-preview` model with [Playwright](https://playwright.dev/) to automate basic browser interactions. Combining the model with [Playwright](https://playwright.dev/) allows the model to see the browser screen, make decisions, and perform actions like clicking, typing, and navigating websites. You should exercise caution when running this example code. This code is designed to be run locally but should only be executed in a test environment. Use a human to confirm decisions and don't give the model access to sensitive data.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいモデルとストリーミング機能を追加"
}
```

### Explanation
この変更は、Azure OpenAIの「レスポンスAPI」に関する文書の更新を示しています。主な追加内容は、新しいモデル`o3`および`o4-mini`がレスポンスAPIで利用可能であることを示す情報が追加されたことです。また、ストリーミング機能に関する新しいセクションが追加され、Pythonでの使用例が提供されています。この機能により、ユーザーはリアルタイムでレスポンスを受け取ることができ、よりインタラクティブな体験を提供することが可能になります。

さらに、推論モデルをレスポンスAPIで使用するためのガイドへのリンクも追加されており、ユーザーは利用方法を簡単に参照できるようになっています。この変更により、文書はより包括的になり、ユーザーにとっての便利さが向上しました。全体として、機能拡張が提供されることによって、開発者はAzure OpenAIの活用方法をさらに広げることができるようになっています。


