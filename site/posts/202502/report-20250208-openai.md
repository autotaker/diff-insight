---
date: '2025-02-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:22af4d0...MicrosoftDocs:4912a73
summary: このドキュメントの変更は、Azure OpenAIサービスに関する複数のドキュメントの軽微な更新です。主な内容は、音声生成および推論モデルに関連する情報の更新、地域情報の拡充、クォータ制限の調整です。これにより、ドキュメントはより正確で使いやすくなります。新機能として地域の利用可能性情報が追加され、Azure
  OpenAIリソースの地域要件が柔軟化しました。また、特定のセクションが削除され、ドキュメントの公開日が更新されています。これらの変更により、ユーザーは最新の情報を得やすくなり、モデルの選択が効果的になります。全体的に、ユーザーエクスペリエンスが向上し、サービス活用の効果が期待されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:22af4d0...MicrosoftDocs:4912a73){target="_blank"}

# Highlights
このドキュメントの変更は、主にAzure OpenAIサービスに関する複数のドキュメントの軽微な更新を目的としています。変更の内容は、各種音声生成および推論モデルに関連する情報の更新や、ユーザーが利用可能な地域情報の拡充、およびクォータ制限の調整などです。新しい情報の追加と日付更新を含み、全体としてドキュメントはより正確で使いやすくなるように改善されています。

## New features
- 各モデルにおける地域の利用可能性情報が追加。
- Azure OpenAIリソースの地域要件が柔軟になり選択肢が拡大。

## Breaking changes
- 特定のセクションの削除（例：「最大応答」セクション）。

## Other updates
- ドキュメントの公開日が更新され、最新情報が反映。
- モデルのクォータ制限が明確化および拡大。

# Insights
この更新は利用者にとって主に以下の点で利益があります。まず、ドキュメントの日付の更新により、その情報が最新のものであることを確認できるようになり、信頼性が向上します。次に、モデルに関する地域情報やクォータ制限の調整は、ユーザーが自身のニーズに合ったモデルをより効果的に選択し利用するための指針を提供します。

例えば、`gpt-4o`モデルのクォータ制限の変更により、これまで以上に大量のトークンを使用することが可能になり、より多くのデータ処理を行えます。このことは、企業や研究者がAzure OpenAIの機能を十分に引き出し、最適化された運用を実現するために大いに役立つでしょう。

一方で、特定の情報セクションの削除や表現の簡素化により、ドキュメントがよりコンパクトになり、読者の混乱を減らす効果があります。これにより、ユーザーは自分にとって必要な情報だけを簡単に見つけやすくなっています。

地域情報の更新は、Azure OpenAIの可用性を向上させるため、様々な地理的条件下での利用を考慮に入れるためのものであり、グローバルな展開を目指す企業にとっては非常に重要な要素です。

このようなアップデートにより、Azure OpenAIサービスにおけるユーザーエクスペリエンスはより良いものとなり、利用者がこれまで以上に効果的にサービスを活用できることが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [audio-completions-quickstart.md](#item-be5860) | minor update | 音声生成クイックスタートの更新 | modified | 3 | 3 | 6 | 
| [models.md](#item-db2c37) | minor update | モデルに関するドキュメントの更新 | modified | 13 | 2 | 15 | 
| [use-your-data.md](#item-455d6e) | minor update | データ利用に関するドキュメントの修正 | modified | 0 | 5 | 5 | 
| [batch.md](#item-a131d5) | minor update | バッチ処理に関するドキュメントの更新 | modified | 4 | 1 | 5 | 
| [reasoning.md](#item-a54b2f) | minor update | 推論モデルに関する情報の追加 | modified | 16 | 1 | 17 | 
| [audio-completions-intro.md](#item-7391cb) | minor update | 音声生成モデルに関する地域情報の更新 | modified | 1 | 1 | 2 | 
| [audio-completions-javascript.md](#item-b1be01) | minor update | Azure OpenAIリソースの地域要件の更新 | modified | 1 | 1 | 2 | 
| [audio-completions-python.md](#item-a88047) | minor update | Azure OpenAIリソースの地域要件の更新 | modified | 1 | 1 | 2 | 
| [audio-completions-rest.md](#item-0ec305) | minor update | Azure OpenAIリソースの地域要件の更新 | modified | 1 | 1 | 2 | 
| [audio-completions-typescript.md](#item-94bc1f) | minor update | Azure OpenAIリソースの地域要件の更新 | modified | 1 | 1 | 2 | 
| [global-batch.md](#item-929e6a) | minor update | モデルマトリックスの更新 | modified | 24 | 24 | 48 | 
| [provisioned-global.md](#item-340884) | minor update | モデルマトリックスの地域情報の修正 | modified | 0 | 1 | 1 | 
| [provisioned-models.md](#item-8ee639) | minor update | プロビジョニングされたモデルの情報更新 | modified | 2 | 1 | 3 | 
| [realtime-javascript.md](#item-3c125e) | minor update | Azure OpenAIリソースの地域情報の更新 | modified | 1 | 1 | 2 | 
| [realtime-python.md](#item-1291c0) | minor update | Azure OpenAIリソースの地域情報の更新 | modified | 1 | 1 | 2 | 
| [realtime-typescript.md](#item-eacc9c) | minor update | Azure OpenAIリソースの地域情報の更新 | modified | 1 | 1 | 2 | 
| [quotas-limits.md](#item-06c6f9) | minor update | gpt-4oモデルのクォータ制限の更新 | modified | 4 | 4 | 8 | 
| [realtime-audio-quickstart.md](#item-727df8) | minor update | リアルタイムオーディオAPIに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [realtime-audio-reference.md](#item-276d51) | minor update | リアルタイムAPIリファレンスの更新 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-53303b) | minor update | 新機能の追加とモデル情報の更新 | modified | 3 | 5 | 8 | 


# Modified Contents
## articles/ai-services/openai/audio-completions-quickstart.md{#item-be5860}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Walkthrough on how to get started with audio generation using Azure
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 1/21/2025
+ms.date: 2/6/2025
 author: eric-urban
 ms.author: eur
 ms.custom: references_regions
@@ -55,5 +55,5 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 
 ## Related content
 
-* Learn more about Azure OpenAI [deployment types](./how-to/deployment-types.md)
-* Learn more about Azure OpenAI [quotas and limits](quotas-limits.md)
+* Learn more about Azure OpenAI [deployment types](./how-to/deployment-types.md).
+* Learn more about Azure OpenAI [quotas and limits](quotas-limits.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "音声生成クイックスタートの更新"
}
```

### Explanation
このコードの変更は、音声生成に関するクイックスタートガイドのドキュメントに対するマイナーアップデートです。具体的には、公開日の更新が行われ、2025年1月21日から2025年2月6日へと変更されました。また、関連コンテンツのセクションにおいて、リンクの終了にピリオドが追加されました。この変更は、ドキュメントの正確性を向上させ、より良い文書を提供することを目的としています。全体として、内容に重要な影響は与えませんが、より整った形式を意識しています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 01/30/2025
+ms.date: 2/7/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -64,7 +64,7 @@ The GPT 4o audio models are part of the GPT-4o model family and support either l
 - GPT-4o real-time audio is designed to handle real-time, low-latency conversational interactions, making it a great fit for support agents, assistants, translators, and other use cases that need highly responsive back-and-forth with a user. For more information on how to use GPT-4o real-time audio, see the [GPT-4o real-time audio quickstart](../realtime-audio-quickstart.md) and [how to use GPT-4o audio](../how-to/realtime-audio.md).
 - GPT-4o audio completion is designed to generate audio from audio or text prompts, making it a great fit for generating audio books, audio content, and other use cases that require audio generation. The GPT-4o audio completions model introduces the audio modality into the existing `/chat/completions` API. For more information on how to use GPT-4o audio completions, see the [audio generation quickstart](../audio-completions-quickstart.md).
 
-GPT-4o audio is available in the East US 2 (`eastus2`) and Sweden Central (`swedencentral`) regions. To use GPT-4o real-time audio, you need [an Azure OpenAI resource](../how-to/create-resource.md) in one of the supported regions.
+To use GPT-4o audio, you need [an Azure OpenAI resource](../how-to/create-resource.md) in one of the [supported regions](#global-standard-model-availability).
 
 When your resource is created, you can [deploy](../how-to/create-resource.md#deploy-a-model) the GPT-4o audio model. 
 
@@ -78,6 +78,17 @@ Details about maximum request tokens and training data are available in the foll
 |`gpt-4o-realtime-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for real-time audio processing. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
 |`gpt-4o-realtime-preview` (2024-10-01) <br> **GPT-4o audio** | **Audio model** for real-time audio processing. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
 
+### Region availability
+
+| Model | Region |
+|---|---|
+|`gpt-4o-mini-audio-preview` | East US2 (Global Standard) |
+|`gpt-4o-mini-realtime-preview` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
+|`gpt-4o-audio-preview` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
+|`gpt-4o-realtime-preview` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
+
+To compare the availability of GPT-4o audio models across all regions, see the [models table](#global-standard-model-availability).
+
 ## GPT-4o and GPT-4 Turbo
 
 GPT-4o integrates text and images in a single model, enabling it to handle multiple data types simultaneously. This multimodal approach enhances accuracy and responsiveness in human-computer interactions. GPT-4o matches GPT-4 Turbo in English text and coding tasks while offering superior performance in non-English languages and vision tasks, setting new benchmarks for AI capabilities.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルに関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスのモデルに関するドキュメントのマイナーアップデートです。主な更新点は、公開日が2025年1月30日から2025年2月7日に変更されたことです。また、GPT-4oモデルの利用に関する情報が明確化され、特定のリソースや地域のサポート情報が強調されています。新しく「地域の利用可能性」というセクションが追加され、各モデルがサポートされる地域の一覧が提供されています。これにより、ユーザーはGPT-4oオーディオモデルの利用に関する情報をより簡単に理解できるようになります。この更新は、情報の整理と文書の正確性を向上させることを目的としています。

## articles/ai-services/openai/concepts/use-your-data.md{#item-455d6e}

<details>
<summary>Diff</summary>
````diff
@@ -515,11 +515,6 @@ There are many tricks in prompt engineering that you can try to improve the outp
 > The system message is only guidance. The model might not adhere to every instruction specified because it has been primed with certain behaviors such as objectivity, and avoiding controversial statements. Unexpected behavior might occur if the system message contradicts with these behaviors. 
 
 
-
-### Maximum response 
-
-Set a limit on the number of tokens per model response. The upper limit for Azure OpenAI On Your Data is 1500. This is equivalent to setting the `max_tokens` parameter in the API. 
-
 ### Limit responses to your data 
 
 This option encourages the model to respond using your data only, and is selected by default. If you unselect this option, the model might more readily apply its internal knowledge to respond. Determine the correct selection based on your use case and scenario. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ利用に関するドキュメントの修正"
}
```

### Explanation
このコードの変更は、Azure OpenAIでのデータ利用に関するドキュメントのマイナーアップデートです。具体的には、「最大応答」というセクションが削除されました。このセクションでは、モデルの応答に制限を設定する方法およびその上限値（1500トークン）に関する情報が提供されていましたが、情報が不要と判断されたか、他の部分との重複があると考えられます。その結果、ドキュメントはより簡潔になり、モデルのデータ利用に関する重要なオプションに焦点を当てています（デフォルトで選択されたデータのみを応じさせるオプション）。この変更は、ユーザーにとっての理解を促進し、より明確なガイダンスを提供することを目的としています。

## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -46,6 +46,8 @@ Key use cases include:
 
 [!INCLUDE [Global batch](../includes/model-matrix/global-batch.md)]
 
+Registration is required for access to `o3-mini`. For more information see, our [reasoning models guide](./reasoning.md).
+
 # [Data Zone Batch](#tab/datazone-batch)
 
 ### Data zone batch model availability
@@ -58,6 +60,7 @@ The following models support global batch:
 
 | Model | Version | Input format |
 |---|---|---|
+| `o3-mini` | 2025-01-31 | text |
 |`gpt-4o` | 2024-08-06 |text + image |
 |`gpt-4o-mini`| 2024-07-18 | text + image |
 |`gpt-4o` | 2024-05-13 |text + image |
@@ -74,7 +77,7 @@ Refer to the [models page](../concepts/models.md) for the most up-to-date inform
 |   | API Version   |
 |---|---|
 |**Latest GA API release:**| `2024-10-21`|
-|**Latest Preview API release:**| `2024-10-01-preview`|
+|**Latest Preview API release:**| `2025-01-01-preview`|
 
 Support first added in: `2024-07-01-preview`
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理に関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのバッチ処理に関するドキュメントのマイナーアップデートです。主な追加情報として、`o3-mini` モデルへのアクセスに必要な登録についての注意が追加され、詳細は「推論モデルガイド」へのリンクが提供されています。また、サポートされるモデル一覧に `o3-mini` が新たに追加され、バージョンとして「2025-01-31」が示されています。さらに、最新のプレビューAPIリリースの日付が「2024-10-01-preview」から「2025-01-01-preview」に更新されました。これらの変更は、ユーザーが最新の情報を把握しやすくするために行われており、全体的な文書の明確さと正確性を高めています。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's advanced o3-mini, o1, & o1-mini rea
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 01/30/2025
+ms.date: 02/06/2025
 author: mrbullwinkle    
 ms.author: mbullwin
 ---
@@ -55,8 +55,11 @@ Request access: [limited access model application](https://aka.ms/OAI/o1access)
 | Streaming | ✅ | - | - | - |
 
 <sup>*</sup> Reasoning models will only work with the `max_completion_tokens` parameter. <br><br>
+
 <sup>**</sup>The latest o<sup>&#42;</sup> series model support system messages to make migration easier. When you use a system message with `o3-mini` and `o1` it will be treated as a developer message. You should not use both a developer message and a system message in the same API request.
 
+
+
 ### Not Supported
 
 The following are currently unsupported with reasoning models:
@@ -312,3 +315,15 @@ print(response.model_dump_json(indent=2))
 
 ---
 
+## Markdown output
+
+By default the `o3-mini` and `o1` models will not attempt to produce output that includes markdown formatting. A common use case where this behavior is undesirable is when you want the model to output code contained within a markdown code block. When the model generates output without markdown formatting you lose features like syntax highlighting, and copyable code blocks in interactive playground experiences. To override this new default behavior and encourage markdown inclusion in model responses, add the string `Formatting re-enabled` to the beginning of your developer message.
+
+Adding `Formatting re-enabled` to the beginning of your developer message does not guarantee that the model will include markdown formatting in its response, it only increases the likelihood. We have found from internal testing that `Formatting re-enabled` is less effective by itself with the `o1` model than with `o3-mini`.
+
+To improve the performance of `Formatting re-enabled` you can further augment the beginning of the developer message which will often result in the desired output. Rather than just adding `Formatting re-enabled` to the beginning of your developer message, you can experiment with adding a more descriptive initial instruction like one of the examples below:
+
+- `Formatting re-enabled - please enclose code blocks with appropriate markdown tags.`
+- `Formatting re-enabled - code output should be wrapped in markdown.`
+
+Depending on your expected output you may need to customize your initial developer message further to target your specific use case.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "推論モデルに関する情報の追加"
}
```

### Explanation
このコードの変更は、Azure OpenAIの推論モデルに関するドキュメントへのマイナーアップデートです。主な変更点は、新しい情報の追加と日付の更新です。具体的には、`o3-mini` と `o1` モデルでのシステムメッセージのサポートに関する注意が追加され、これらのモデルでのシステムメッセージは開発者メッセージとして扱われる旨が明記されています。また、推論モデルの出力にMarkdown形式を含めるための具体的な指示が提供され、ユーザーが開発者メッセージの冒頭に「Formatting re-enabled」という文字列を追加することで、Markdownの出力を促進できることが説明されています。この変更は、ユーザーがモデルを使用する際の期待される出力を向上させるための具体的な指針を与えることを目的としています。全体的に、ドキュメントはユーザーに利便性や柔軟性を提供する方向に進化しています。

## articles/ai-services/openai/includes/audio-completions-intro.md{#item-7391cb}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ By using audio generation capabilities, you can achieve more dynamic and interac
 
 Currently only `gpt-4o-audio-preview` and `gpt-4o-mini-audio-preview` version: `2024-12-17` supports audio generation.
 
-The `gpt-4o-audio-preview` and and `gpt-4o-mini-audio-preview` models are available for global deployments in [East US 2 and Sweden Central regions](../concepts/models.md#global-standard-model-availability).
+For more information about region availability, see the [models and versions documentation](../concepts/models.md#global-standard-model-availability).
 
 Currently the following voices are supported for audio out: Alloy, Echo, and Shimmer.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "音声生成モデルに関する地域情報の更新"
}
```

### Explanation
このコードの変更は、音声生成機能に関するドキュメントのマイナーアップデートです。具体的には、`gpt-4o-audio-preview` と `gpt-4o-mini-audio-preview` モデルの地域展開に関する情報が更新されました。従来の表現では、モデルが「East US 2」と「Sweden Central」地域で利用可能であると記載されていましたが、新しい表現では「地域の可用性に関する詳細については、モデルとバージョンのドキュメントを参照してください」となっており、より包括的で参照しやすい内容に改善されています。この変更により、ユーザーは利用可能な地域についての情報を容易に見つけることができるようになり、情報の透明性が向上します。全体として、この更新はユーザーにとっての利便性を増すことを目的としています。

## articles/ai-services/openai/includes/audio-completions-javascript.md{#item-b1be01}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.date: 1/21/2025
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
 - <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
-- An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- An Azure OpenAI resource created in one of the supported regions. For more information about region availability, see the [models and versions documentation](../concepts/models.md#global-standard-model-availability).
 - Then, you need to deploy a `gpt-4o-mini-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
 
 ## Microsoft Entra ID prerequisites
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIリソースの地域要件の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIの音声生成に関するJavaScriptのドキュメントのマイナーアップデートです。主な変更点は、Azure OpenAIリソースの作成に関する地域の要件が更新されたことです。以前は、リソースが「East US 2」または「Sweden Central」地域で作成される必要があると明記されていましたが、新しい表現では「サポートされている地域のいずれかで作成されたAzure OpenAIリソースが必要」となっており、地域の選択肢が拡大されたことを示しています。また、地域の可用性に関しては、よく参照されるドキュメントへのリンクも更新されています。この変更により、ユーザーはより多くの選択肢の中からリソースを作成できるようになり、利用しやすさが向上しています。全体として、この更新は明確さと情報の柔軟性を強化することを目的としています。

## articles/ai-services/openai/includes/audio-completions-python.md{#item-a88047}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ Use this guide to get started generating audio with the Azure OpenAI SDK for Pyt
 
 - An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
 - <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>. We recommend using Python 3.10 or later, but having at least Python 3.8 is required. If you don't have a suitable version of Python installed, you can follow the instructions in the [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter) for the easiest way of installing Python on your operating system.
-- An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- An Azure OpenAI resource created in one of the supported regions. For more information about region availability, see the [models and versions documentation](../concepts/models.md#global-standard-model-availability).
 - Then, you need to deploy a `gpt-4o-mini-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 ## Microsoft Entra ID prerequisites
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIリソースの地域要件の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIの音声生成に関するPythonのドキュメントのマイナーアップデートです。具体的には、Azure OpenAIリソースの作成に関連する地域要件が更新されました。以前は、リソースを「East US 2」または「Sweden Central」地域で作成する必要があると明示されていましたが、新しい文言では「サポートされている地域のいずれかで作成されたAzure OpenAIリソースが必要」となり、ユーザーに選べる地域が増えています。これに伴い、地域の可用性についての詳細は、別のドキュメントへのリンクを通じて参照できるようになっています。この変更は、ユーザーの利便性を向上させ、より柔軟なリソースの作成を可能にすることを目的としています。全体として、これにより情報の明確さとアクセスのしやすさが向上します。

## articles/ai-services/openai/includes/audio-completions-rest.md{#item-0ec305}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.date: 1/21/2025
 
 - An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
 - <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>. We recommend using Python 3.10 or later, but having at least Python 3.8 is required. If you don't have a suitable version of Python installed, you can follow the instructions in the [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter) for the easiest way of installing Python on your operating system.
-- An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- An Azure OpenAI resource created in one of the supported regions. For more information about region availability, see the [models and versions documentation](../concepts/models.md#global-standard-model-availability).
 - Then, you need to deploy a `gpt-4o-mini-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 ## Microsoft Entra ID prerequisites
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIリソースの地域要件の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIに関するREST APIのドキュメントでのマイナーアップデートです。主な変更点は、Azure OpenAIリソースの作成に関連する地域要件が更新されたことです。以前の記述ではリソースが「East US 2」または「Sweden Central」地域で作成される必要があると明記されていましたが、新しい説明では「サポートされている地域のいずれかで作成されたAzure OpenAIリソースが必要」となっています。この変更により、サポートされる地域が広がったことが示されており、利用者はより多くの選択肢からリソースを作成できるようになります。また、地域の可用性に関する詳細は、他のドキュメントへのリンクを通じて確認できるようになっています。このように、情報の透明性とユーザーの利便性を向上させることを目的とした更新です。

## articles/ai-services/openai/includes/audio-completions-typescript.md{#item-94bc1f}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.date: 1/21/2025
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
 - <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
 - [TypeScript](https://www.typescriptlang.org/download/) installed globally.
-- An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- An Azure OpenAI resource created in one of the supported regions. For more information about region availability, see the [models and versions documentation](../concepts/models.md#global-standard-model-availability).
 - Then, you need to deploy a `gpt-4o-mini-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
 
 ## Microsoft Entra ID prerequisites
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIリソースの地域要件の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIの音声生成に関するTypeScriptのドキュメントに対するマイナーアップデートです。変更内容は、Azure OpenAIリソースの作成に関する地域要件が更新されたことです。具体的には、以前はリソースが「East US 2」または「Sweden Central」地域で作成される必要があると記載されていましたが、更新後は「サポートされている地域のいずれかで作成されたAzure OpenAIリソースが必要」となり、利用可能な地域に関する柔軟性が増しています。また、地域の可用性についての詳細な情報は、他のドキュメントへのリンクを通じて確認できるようになっています。この変更は、ユーザーに対してより多くの選択肢を提供し、サービスの利用を促進することを目的としています。全体として、情報の明確さを高め、ユーザーの利便性を向上させるための更新です。

## articles/ai-services/openai/includes/model-matrix/global-batch.md{#item-929e6a}

<details>
<summary>Diff</summary>
````diff
@@ -6,30 +6,30 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 01/15/2025
+ms.date: 02/07/2025
 ---
 
 
-| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
-|:-------------------|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
-| australiaeast      | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| brazilsouth        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| canadaeast         | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| eastus             | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| eastus2            | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| francecentral      | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| germanywestcentral | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| japaneast          | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| koreacentral       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| northcentralus     | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| norwayeast         | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| polandcentral      | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southafricanorth   | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southcentralus     | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southindia         | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| swedencentral      | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| switzerlandnorth   | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| uksouth            | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westeurope         | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westus             | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westus3            | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| **Region**     | **o3-mini**, **2025-01-31**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
+|:-------------------|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
+| australiaeast      | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| brazilsouth        | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| canadaeast         | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| eastus             | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| eastus2            | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| francecentral      | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| germanywestcentral | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| japaneast          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| koreacentral       | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| northcentralus     | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| norwayeast         | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| polandcentral      | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southafricanorth   | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southcentralus     | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southindia         | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| swedencentral      | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| switzerlandnorth   | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| uksouth            | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westeurope         | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westus             | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westus3            | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルマトリックスの更新"
}
```

### Explanation
このコードの変更は、モデルマトリックスに関するドキュメントの更新です。主な変更点は、スプレッドシートのセクションが刷新され、変化した情報を反映した新しいデータが追加されています。具体的には、いくつかのモデルについての地域別の可用性が新たな形式で示されるようになりました。

新しいバージョンでは、モデル「o3-mini」が追加され、さらに以前のモデルやバージョンとともに、それぞれの地域でのサポート状況が整理されています。特に、地域が「-」で示されるモデルは、該当地域で未対応のことを示し、他のいくつかのモデルに関しては、対応状況が「✅」で示されており、明確に可用性が確認できるようになっています。

この更新により、利用者がAzure OpenAIサービスを使用する際の地域ごとのモデルの対応状況を一目で把握できるようになり、情報の透明性が向上しました。全体として、ユーザーにとってより使いやすい情報を提供するためのマイナーな変更です。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,6 @@ ms.date: 02/06/2025
 | southcentralus     | ✅                       | ✅                       | ✅                       | ✅                            |
 | southeastasia      | ✅                       | ✅                       | ✅                       | ✅                            |
 | southindia         | ✅                       | ✅                       | ✅                       | ✅                            |
-| spaincentral       | ✅                       | ✅                       | ✅                       | ✅                            |
 | swedencentral      | ✅                       | ✅                       | ✅                       | ✅                            |
 | switzerlandnorth   | ✅                       | ✅                       | ✅                       | ✅                            |
 | switzerlandwest    | ✅                       | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルマトリックスの地域情報の修正"
}
```

### Explanation
このコードの変更は、モデルマトリックスに関するドキュメントのマイナーな更新です。この更新では、「spaincentral」という地域に関する行が削除されました。これにより、スプレッドシートからはその地域でのモデルの可用性情報が除外されたことになります。

変更内容は、地域情報の可用性を最新の状態に保つためのものであり、正確な情報を提供することを目的としています。この修正は、ユーザーがAzure OpenAIサービスを利用する際の地域ごとのモデルの対応状況を正しく理解できるようにするための重要な更新です。全体として、より信頼性の高い情報を提供するための軽微な変更です。

## articles/ai-services/openai/includes/model-matrix/provisioned-models.md{#item-8ee639}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,8 @@ ms.date: 10/24/2024
 | norwayeast         | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                           | ✅                    | -                      | -                      |
 | polandcentral      | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | southafricanorth   | ✅                       | -                      | -                           | ✅                | ✅                        | -                       | ✅                            | ✅                    | ✅                       | -                      |
-| southcentralus     | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| southcentralus     | ✅                       | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| southeastasia      | -                      | ✅                       | ✅                            | -               | -                       | -                       | -                           | -                   | -                      | -                      |
 | southindia         | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | ✅                       |
 | swedencentral      | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | switzerlandnorth   | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされたモデルの情報更新"
}
```

### Explanation
このコードの変更は、プロビジョニングされたモデルに関するドキュメントのマイナーな更新です。この更新では、スプレッドシートにおけるモデルの可用性に関する情報が更新され、具体的には以下の変更が行われました。

まず、「southcentralus」地域のモデルに新しい情報が追加され、対応状況が「✅」から「-」に変更されることで、いくつかのモデルがその地域での利用可能性を示しています。加えて、新たに「southeastasia」地域に関する情報が追加され、こちらではいくつかのモデルに「✅」マークが付けられることによって、今後の利用可能性が保証されています。

この更新により、ユーザーはAzure OpenAIサービスにおける各地域のモデルの利用状況をより正確に把握できるようになります。更新された情報は、利用者が適切にサービスを選択できるようにするためのものです。この変更は、全体的に見て情報をより明確にし、信頼性を高めるための軽微な修正です。

## articles/ai-services/openai/includes/realtime-javascript.md{#item-3c125e}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.date: 1/21/2025
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
 - <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
-- An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- An Azure OpenAI resource created in one of the supported regions. For more information about region availability, see the [models and versions documentation](../concepts/models.md#global-standard-model-availability).
 - Then, you need to deploy a `gpt-4o-mini-realtime-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
 
 ### Microsoft Entra ID prerequisites
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIリソースの地域情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIリソースに関するドキュメントの軽微な更新です。この更新では、リソースの地域に関する説明が修正されました。

具体的には、以前は「East US 2またはSweden Central地域で作成されたAzure OpenAIリソース」という文言が削除され、代わりに「サポートされている地域のいずれかで作成されたAzure OpenAIリソース」と記載されるようになりました。これにより、ユーザーに対して利用可能な地域の選択肢が広がり、特定の地域に制約されないことが強調されました。

さらに、地域の可用性についての情報を得るためのリンクも更新され、より具体的に「[models and versions documentation]」へのリンクが示されるようになりました。これによって、ユーザーはさらに詳細な情報を簡単に探しやすくなり、正確なリソースの設定が可能となります。

この変更は、ユーザーがAzure OpenAIサービス利用時に必要な情報を正しく理解し、柔軟にリソースを利用できるようにするための重要なアップデートです。全体としては、ドキュメントの信頼性と明瞭性を向上させるためのマイナーな修正です。

## articles/ai-services/openai/includes/realtime-python.md{#item-1291c0}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.date: 1/21/2025
 
 - An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
 - <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>. We recommend using Python 3.10 or later, but having at least Python 3.8 is required. If you don't have a suitable version of Python installed, you can follow the instructions in the [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter) for the easiest way of installing Python on your operating system.
-- An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- An Azure OpenAI resource created in one of the supported regions. For more information about region availability, see the [models and versions documentation](../concepts/models.md#global-standard-model-availability).
 - Then, you need to deploy a `gpt-4o-mini-realtime-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 ## Microsoft Entra ID prerequisites
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIリソースの地域情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIリソースに関連するドキュメントの軽微な更新です。主な変更点は、Azure OpenAIリソースに関する地域の説明が更新されたことです。

元の記述では「East US 2またはSweden Central地域で作成されたAzure OpenAIリソース」と明記されていましたが、これが「サポートされている地域のいずれかで作成されたAzure OpenAIリソース」と表現されるようになりました。これにより、特定の地域に制限されることなく、ユーザーがリソースを作成できることが明確にされています。

地域の可用性に関するリンクも修正され、「モデルおよびバージョンのドキュメント」へのリンクが提供され、情報の探しやすさが向上しています。これによって、ユーザーはリソースの設定をより正確に行うための情報を迅速に取得できるようになります。

全体として、この変更はユーザーに対する情報提供の質を向上させ、Azure OpenAIサービスの利用における柔軟性を高めるものであり、ドキュメントの信頼性を向上させるためのマイナーな修正と言えます。

## articles/ai-services/openai/includes/realtime-typescript.md{#item-eacc9c}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.date: 1/21/2025
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
 - <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
 - [TypeScript](https://www.typescriptlang.org/download/) installed globally.
-- An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- An Azure OpenAI resource created in one of the supported regions. For more information about region availability, see the [models and versions documentation](../concepts/models.md#global-standard-model-availability).
 - Then, you need to deploy a `gpt-4o-mini-realtime-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
 
 ### Microsoft Entra ID prerequisites
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIリソースの地域情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIリソースに関するドキュメントの軽微な更新を示しています。主な内容は、Azure OpenAIリソースが作成される地域に関する文章が修正された点です。

以前は「East US 2またはSweden Central地域で作成されたAzure OpenAIリソース」と記載されていましたが、変更後は「サポートされている地域のいずれかで作成されたAzure OpenAIリソース」と表現されるようになりました。この修正により、特定の地域に限定されることなく、ユーザーが任意のサポート地域でリソースを作成できることが明確になりました。

地域の可用性に関する情報へのリンクも更新され、「モデルおよびバージョンのドキュメント」への参照が追加され、利用可能な地域に関する詳細情報をユーザーが簡単に取得できるようになっています。これによって、ユーザーは自身のニーズに応じたリソースの選択をよりスムーズに行えるようになります。

この変更は、Azure OpenAIサービスを利用する際の情報の正確性と透明性を向上させるためのものであり、全体としてはマイナーな修正と位置付けられます。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -142,10 +142,10 @@ The rate limits for each `gpt-4o` audio model deployment are 100K TPM and 1K RPM
 
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
 |---|---|:---:|:---:|
-|`gpt-4o-audio-preview` | Default | 100 K | 1 K |
-|`gpt-4o-realtime-preview` | Default | 100 K | 1 K |
-|`gpt-4o-mini-audio-preview` | Default | 100 K | 1 K |
-|`gpt-4o-mini-realtime-preview` | Default | 100 K | 1 K |
+|`gpt-4o-audio-preview` | Default | 450 K | 1 K |
+|`gpt-4o-realtime-preview` | Default | 800 K | 1 K |
+|`gpt-4o-mini-audio-preview` | Default | 2 M | 1 K |
+|`gpt-4o-mini-realtime-preview` | Default | 800 K | 1 K |
 
 M = million | K = thousand
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "gpt-4oモデルのクォータ制限の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスにおけるgpt-4oモデルのクォータ制限に関する情報の軽微な更新を示しています。具体的には、各モデルのトークンやリクエストの制限が変更されました。

変更前は、全てのgpt-4oモデル（`gpt-4o-audio-preview`、`gpt-4o-realtime-preview`、`gpt-4o-mini-audio-preview`、および`gpt-4o-mini-realtime-preview`）のクォータ制限が100Kトークン（TPM）で統一されていましたが、変更後はそれぞれのモデルに対するクォータが異なる数値に更新されています。具体的には、以下のようになります：

- `gpt-4o-audio-preview`: 450K TPM
- `gpt-4o-realtime-preview`: 800K TPM
- `gpt-4o-mini-audio-preview`: 2M TPM
- `gpt-4o-mini-realtime-preview`: 800K TPM

この変更により、各モデルが利用することのできるトークンの上限が明確になり、ユーザーはそれぞれのモデルの性能や利用制限について理解を深めることができるようになりました。また、制限が増加したことで、ユーザーの利用可能なリソースが充実し、より柔軟な運用が可能となります。

全体として、これらの変更はユーザーに対して重要な情報であり、gpt-4oモデルの利用に関連する計画や調整を行う上で有益な内容となっています。

## articles/ai-services/openai/realtime-audio-quickstart.md{#item-727df8}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use GPT-4o Realtime API for speech and audio with Azur
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 1/21/2025
+ms.date: 2/7/2025
 author: eric-urban
 ms.author: eur
 ms.custom: references_regions, ignite-2024
@@ -23,7 +23,7 @@ Most users of the Realtime API need to deliver and receive audio from an end-use
 
 ## Supported models
 
-The GPT 4o real-time models are available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability).
+The GPT 4o real-time models are available for global deployments.
 - `gpt-4o-realtime-preview` (version `2024-12-17`)
 - `gpt-4o-mini-realtime-preview` (version `2024-12-17`)
 - `gpt-4o-realtime-preview` (version `2024-10-01`)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオAPIに関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのリアルタイムオーディオAPIに関するドキュメントの軽微な更新を示しています。具体的には、主に日付やサポートするモデルの地域に関する情報が修正されました。

1. **日付の更新**: ドキュメントの最終更新日が「2025年1月21日」から「2025年2月7日」に変更され、最新の情報が反映されています。

2. **サポートモデルの地域情報の変更**: もともと「East US 2およびSweden Central地域でのグローバル展開が可能」との記載がありましたが、更新後は「グローバル展開が可能」と簡潔に表現され、特定の地域が言及されなくなりました。この変更により、ユーザーは任意の地域での利用が可能であることが強調され、柔軟性が向上しています。

この更新により、リアルタイムAPIを使用するユーザーは、利用可能な情報を基にサービスをより効果的に活用できるようになります。また、最新の情報を提供することで、ドキュメントの有用性と信頼性が向上しています。全体として、これらの変更は明確さと利便性を持つものであり、ユーザーの体験を向上させることを目的としています。

## articles/ai-services/openai/realtime-audio-reference.md{#item-276d51}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use the Realtime API to interact with the Azure OpenAI
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 12/20/2024
+ms.date: 2/7/2024
 author: eric-urban
 ms.author: eur
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムAPIリファレンスの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのリアルタイムAPIに関するリファレンス文書の軽微な更新を示しています。主に、文書の日付に関する情報が修正されました。

具体的には、最終更新日が「2024年12月20日」から「2024年2月7日」に変更されています。この更新により、ユーザーは最新の情報を入手することができ、リアルタイムAPIの利用に関する知識を最新の状態に保つことができます。

日付の更新は、ドキュメントが正確で信頼性の高い情報を提供するために重要であり、ユーザーが依存するリソースとしての価値を保つためにも必須の対応です。このような小規模な変更でも、ドキュメント全体の有用性を向上させ、利用者の体験をより良いものにすることに寄与します。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: whats-new
-ms.date: 1/30/2025
+ms.date: 2/6/2025
 recommendations: false
 ---
 
@@ -23,13 +23,11 @@ This article provides a summary of the latest releases and major documentation u
 
 ### gpt-4o mini audio released
 
-The `gpt-4o-audio-preview` (2024-12-17) model is the latest audio completions model. Use the `gpt-4o-audio-preview` model for audio generation. For more information, see the [audio generation quickstart](./audio-completions-quickstart.md).
+The `gpt-4o-mini-audio-preview` (2024-12-17) model is the latest audio completions model. For more information, see the [audio generation quickstart](./audio-completions-quickstart.md).
 
 The `gpt-4o-mini-realtime-preview` (2024-12-17) model is the latest real-time audio model. The real-time models use the same underlying GPT-4o audio model as the completions API, but is optimized for low-latency, real-time audio interactions. For more information, see the [real-time audio quickstart](./realtime-audio-quickstart.md).
 
-### GPT-4o audio completions
-
-The `gpt-4o-audio-preview` model is now available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability). Use the `gpt-4o-audio-preview` model for audio generation.
+For more information about available models, see the [models and versions documentation](./concepts/models.md#gpt-4o-audio).
 
 ## January 2025
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能の追加とモデル情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIに関する「What's New」文書の軽微な更新を示しています。具体的には、日付の更新とモデルに関連する情報の修正が行われています。

1. **日付の更新**: 文書の最終更新日が「2025年1月30日」から「2025年2月6日」に変更され、最新の情報が反映されています。

2. **モデル情報の修正**:
   - **モデル名の変更**: `gpt-4o-audio-preview`が`gpt-4o-mini-audio-preview`に変更され、現在の最新音声補完モデルとして言及されています。これに伴い、モデルの使用方法に関する記述がすっきりと整理されています。
   - **情報の簡素化**: 音声生成に関する段落が削除され、代わりに「利用可能なモデル」についての情報が提供されています。これにより、ユーザーは様々なモデルの詳細を簡単に参照できるようになっています。

この更新により、Azure OpenAIの最新情報がより明確かつアクセスしやすくなり、ユーザーは必要な情報を素早く探し出すことができるようになっています。全体として、この変更はドキュメントの利便性を向上させることを目的としています。


