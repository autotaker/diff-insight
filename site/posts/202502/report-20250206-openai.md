---
date: '2025-02-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d46a0e8...MicrosoftDocs:ea9b000
summary: このドキュメントの変更点は、Azure OpenAIサービスにおける音声モデルの更新と新しいモデルの追加に焦点を当てています。具体的には、`gpt-4o-mini-audio-preview`および`gpt-4o-mini-realtime-preview`という新しい音声モデルが導入され、関連文書が更新されました。さらに、新しいデプロイ手順やプロンプトキャッシング、サポートモデルのリストが明確化されました。特に大きな非互換変更はありませんが、以前のモデル名が新しい名前に変更されている点に注意が必要です。これらの変更は、音声生成やリアルタイム音声処理の機能を強化し、開発者にはより便利な選択肢を提供しています。また、詳細な実装ガイダンスが含まれており、ユーザーが直感的に新機能を利用できるようになっています。全体として、これらの更新はAzure
  OpenAIの機能性を拡大し、より良いユーザー体験を提供するための重要なステップです。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d46a0e8...MicrosoftDocs:ea9b000){target="_blank"}

# Highlights
このドキュメントの差分は、Azure OpenAIサービスにおけるモデル情報の更新と新しい音声モデルの追加を中心にしています。具体的には、新しい音声モデル`gpt-4o-mini-audio-preview`とリアルタイムモデル`gpt-4o-mini-realtime-preview`が導入され、これに関連する文書が全面的に更新されました。新しいデプロイ手順やプロンプトキャッシング、サポートモデルのリストなどが明確化されています。

## New features
- 新しい音声モデル`gpt-4o-mini-audio-preview`と`gpt-4o-audio-preview`の追加。
- リアルタイムオーディオモデル`gpt-4o-mini-realtime-preview`の導入。
- 各モデルの仕様やデプロイ手順に関する詳細情報の追加。

## Breaking changes
特に大きな非互換変更は示されていませんが、以前のモデル名が新しいモデル名に変更されている点に注意が必要です。

## Other updates
- モデルのレート制限に関する情報更新。
- REST APIおよびSDKにおける音声モデルの使用方法に関するガイダンスを更新。

# Insights
この一連の変更は、Azure OpenAIサービスのモデル群に新たに音声入力やリアルタイム音声処理の機能を強化する新モデルを導入するもので、ユーザーの利便性と選択肢の拡充を図っています。新モデルの追加により、音声生成やリアルタイムオーディオ処理が可能となったことで、音声インタラクションを活用するアプリケーション開発がより容易になります。

ドキュメントの更新は非常に包括的であり、新モデルの導入にあたって考えられる全てのケースに対応しています。これには、デプロイ手順のチューニングや、モデルのバージョン管理と使用方法に関する技術的な詳細が含まれています。これにより、ユーザーは適切なモデルを選択し、予測可能な形で新機能を実装することができます。

また、開発者向けの詳細なコードスニペットや設定項目の更新が含まれており、JavaScript、Python、TypeScriptなど様々なプログラミング言語での実装ガイダンスが提供されています。これにより、ユーザーの技術的な理解度に関係なく、直観的かつ効率的に音声モデル機能をテストおよび展開することが可能となります。

全体として、これらの更新はAzure OpenAIの機能性を拡大し、ユーザーにより良い体験を提供するための重要な一歩と言えます。ユーザーは新たに追加された音声モジュールを活用することで、AI導入によるビジネス価値をさらに高めることができるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルリタイアメントに関する情報の更新 | modified | 1 | 1 | 2 | 
| [models.md](#item-db2c37) | minor update | 新しい音声モデル情報の追加 | modified | 2 | 0 | 2 | 
| [create-resource.md](#item-c1c8a3) | minor update | Azureへのデプロイボタンの追加 | modified | 2 | 0 | 2 | 
| [prompt-caching.md](#item-1631df) | minor update | 音声モデルのキャッシングサポートの更新 | modified | 4 | 3 | 7 | 
| [realtime-audio.md](#item-482ba3) | minor update | 新しいリアルタイムオーディオモデルの追加 | modified | 9 | 8 | 17 | 
| [structured-outputs.md](#item-cc2557) | minor update | 構造化出力のサポートモデルの更新 | modified | 1 | 1 | 2 | 
| [audio-completions-ai-foundry.md](#item-748538) | minor update | モデル名の更新 | modified | 3 | 3 | 6 | 
| [audio-completions-deploy-model.md](#item-c5a63e) | minor update | オーディオモデルのデプロイ手順の更新 | modified | 4 | 4 | 8 | 
| [audio-completions-intro.md](#item-7391cb) | minor update | オーディオモデルの導入とサポートの更新 | modified | 3 | 3 | 6 | 
| [audio-completions-javascript.md](#item-b1be01) | minor update | JavaScriptでのオーディオモデルの使用に関する更新 | modified | 15 | 15 | 30 | 
| [audio-completions-python.md](#item-a88047) | minor update | Pythonでのオーディオモデルの使用に関する更新 | modified | 9 | 9 | 18 | 
| [audio-completions-rest.md](#item-0ec305) | minor update | REST APIにおけるオーディオモデルの使用に関する更新 | modified | 15 | 15 | 30 | 
| [audio-completions-typescript.md](#item-94bc1f) | minor update | TypeScriptでのオーディオモデルの使用に関する更新 | modified | 15 | 15 | 30 | 
| [realtime-deploy-model.md](#item-21f911) | minor update | リアルタイムデプロイモデルに関するドキュメントの更新 | modified | 3 | 3 | 6 | 
| [realtime-javascript.md](#item-3c125e) | minor update | JavaScriptでのリアルタイムモデルに関するドキュメントの更新 | modified | 4 | 4 | 8 | 
| [realtime-portal.md](#item-1b81a2) | minor update | リアルタイムポータルでのモデル名の更新 | modified | 3 | 3 | 6 | 
| [realtime-python.md](#item-1291c0) | minor update | Pythonでのリアルタイムモデルに関するドキュメントの更新 | modified | 3 | 3 | 6 | 
| [realtime-typescript.md](#item-eacc9c) | minor update | TypeScriptでのリアルタイムモデルに関するドキュメントの更新 | modified | 3 | 3 | 6 | 
| [quotas-limits.md](#item-06c6f9) | minor update | gpt-4oモデルのレート制限に関する文書の更新 | modified | 4 | 1 | 5 | 
| [realtime-audio-quickstart.md](#item-727df8) | minor update | リアルタイムオーディオクイックスタートガイドの更新 | modified | 5 | 7 | 12 | 
| [realtime-audio-reference.md](#item-276d51) | minor update | リアルタイムオーディオリファレンスの文書更新 | modified | 5 | 5 | 10 | 
| [whats-new.md](#item-53303b) | new feature | 新機能の追加: GPT-4o音声モデルのリリース | modified | 12 | 0 | 12 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -109,7 +109,7 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-4` | vision-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025  **<sup>1</sup>** | `gpt-4o`|
 | `gpt-4o` | 2024-05-13 | No earlier than May 20, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on February 13, 2025. | |
 | `gpt-4o-mini` | 2024-07-18 | No earlier than July 18, 2025  | |
-| `gpt-4o-realtime-preview` | 2024-10-01 | No earlier than September 30, 2025  | `gpt-4o-realtime-preview` (version 2024-12-17) |
+| `gpt-4o-realtime-preview` | 2024-10-01 | No earlier than September 30, 2025  | `gpt-4o-realtime-preview` (version 2024-12-17) or `gpt-4o-mini-realtime-preview` (version 2024-12-17) |
 | `gpt-3.5-turbo-instruct` | 0914 | No earlier than April 1, 2025 |  |
 | `o1` | 2024-12-17 | No earlier than December 17, 2025 | |
 | `text-embedding-ada-002` | 2 | No earlier than October 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルリタイアメントに関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおける現在利用可能なモデルのリストに関する文書の更新を含んでいます。特に、「gpt-4o-realtime-preview」モデルに関連する行が改訂され、新しい情報として「gpt-4o-mini-realtime-preview」バージョンが追加されました。これにより、モデルのアップグレードの選択肢が広がり、ユーザーは最新の利用可能なバージョンについての情報を受け取ることができます。変更は、モデルのリタイアに向けたスケジュールとその影響を伝えるものです。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -72,6 +72,8 @@ Details about maximum request tokens and training data are available in the foll
 
 |  Model ID  | Description | Max Request (tokens) | Training Data (up to)  |
 |---|---|---|---|
+|`gpt-4o-mini-audio-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for audio and text generation. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
+|`gpt-4o-mini-realtime-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for real-time audio processing. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
 |`gpt-4o-audio-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for audio and text generation. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
 |`gpt-4o-realtime-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for real-time audio processing. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
 |`gpt-4o-realtime-preview` (2024-10-01) <br> **GPT-4o audio** | **Audio model** for real-time audio processing. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しい音声モデル情報の追加"
}
```

### Explanation
この変更では、Azure OpenAIサービスにおけるモデルに関する文書に新しい音声モデルの情報が追加されました。具体的には、`gpt-4o-mini-audio-preview`および`gpt-4o-mini-realtime-preview`の2つのモデルが新たにリストに加えられています。これらのモデルは、音声とテキストの生成、ならびにリアルタイム音声処理を目的としており、それぞれの入力トークン数や出力トークン数、トレーニングデータの情報も提供されています。この更新により、ユーザーは新しい音声モデルの詳細な仕様を理解しやすくなります。

## articles/ai-services/openai/how-to/create-resource.md{#item-c1c8a3}

<details>
<summary>Diff</summary>
````diff
@@ -16,6 +16,8 @@ recommendations: false
 
 # Create and deploy an Azure OpenAI Service resource
 
+[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://go.microsoft.com/fwlink/?linkid=2303211)
+
 This article describes how to get started with Azure OpenAI Service and provides step-by-step instructions to create a resource and deploy a model. You can create resources in Azure in several different ways:
 
 - The [Azure portal](https://portal.azure.com/?microsoft_azure_marketplace_ItemHideKey=microsoft_openai_tip#create/Microsoft.CognitiveServicesOpenAI)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureへのデプロイボタンの追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスのリソースを作成する方法に関する文書に、Azureへのデプロイボタンを追加したものです。このボタンは、ユーザーが簡単にリソースをデプロイできるように設計されています。文書の内容は、Azure OpenAIサービスを利用開始するための手順を示しており、リソース作成やモデルのデプロイに関する具体的な手順が含まれています。この更新により、ユーザーはよりスムーズにリソース作成のプロセスを行えるようになります。

## articles/ai-services/openai/how-to/prompt-caching.md{#item-1631df}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,8 @@ Currently only the following models support prompt caching with Azure OpenAI:
 - `gpt-4o-2024-11-20`
 - `gpt-4o-2024-08-06`
 - `gpt-4o-mini-2024-07-18`
-- `gpt-4o-realtime-preview` (version 2024-12-17)`
+- `gpt-4o-realtime-preview` (version 2024-12-17)
+- `gpt-4o-mini-realtime-preview` (version 2024-12-17)
 
 > [!NOTE]
 > Prompt caching is now also available as part of model fine-tuning for `gpt-4o` and `gpt-4o-mini`. Refer to the fine-tuning section of the [pricing page](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) for details.
@@ -81,9 +82,9 @@ Prompt caching is supported for:
 
 |**Caching supported**|**Description**|**Supported models**|
 |--------|--------|--------|
-| **Messages** | The complete messages array: system, developer, user, and assistant content | `gpt-4o`<br/>`gpt-4o-mini`<br/>`gpt-4o-realtime-preview` (version 2024-12-17) <br> `o1` (version 2024-12-17) |
+| **Messages** | The complete messages array: system, developer, user, and assistant content | `gpt-4o`<br/>`gpt-4o-mini`<br/>`gpt-4o-realtime-preview` (version 2024-12-17)<br/>`gpt-4o-mini-realtime-preview` (version 2024-12-17)<br> `o1` (version 2024-12-17) |
 | **Images** | Images included in user messages, both as links or as base64-encoded data. The detail parameter must be set the same across requests. | `gpt-4o`<br/>`gpt-4o-mini` <br> `o1` (version 2024-12-17)  |
-| **Tool use** | Both the messages array and tool definitions. | `gpt-4o`<br/>`gpt-4o-mini`<br/>`gpt-4o-realtime-preview` (version 2024-12-17) <br> `o1` (version 2024-12-17) |
+| **Tool use** | Both the messages array and tool definitions. | `gpt-4o`<br/>`gpt-4o-mini`<br/>`gpt-4o-realtime-preview` (version 2024-12-17)<br/>`gpt-4o-mini-realtime-preview` (version 2024-12-17)<br> `o1` (version 2024-12-17) |
 | **Structured outputs** | Structured output schema is appended as a prefix to the system message. | `gpt-4o`<br/>`gpt-4o-mini` <br> `o1` (version 2024-12-17) |
 
 To improve the likelihood of cache hits occurring, you should structure your requests such that repetitive content occurs at the beginning of the messages array.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "音声モデルのキャッシングサポートの更新"
}
```

### Explanation
この変更では、Azure OpenAIサービスにおけるプロンプトキャッシングに関する文書が更新され、プロンプトキャッシングをサポートするモデルのリストに、新しい音声モデル`gpt-4o-mini-realtime-preview`が追加されました。具体的には、キャッシングがサポートされるモデルのセクションが修正され、モデルのバージョン情報も整理されています。また、プロンプトキャッシングが`gpt-4o`および`gpt-4o-mini`のモデルファインチューニングの一環として利用可能であることが強調されています。この更新により、ユーザーは最新のモデル情報を確認し、キャッシング機能を効果的に活用することができるようになります。

## articles/ai-services/openai/how-to/realtime-audio.md{#item-482ba3}

<details>
<summary>Diff</summary>
````diff
@@ -23,6 +23,7 @@ Most users of the Realtime API need to deliver and receive audio from an end-use
 ## Supported models
 
 The GPT 4o real-time models are available for global deployments in [East US 2 and Sweden Central regions](../concepts/models.md#global-standard-model-availability).
+- `gpt-4o-mini-realtime-preview` (2024-12-17)
 - `gpt-4o-realtime-preview` (2024-12-17)
 - `gpt-4o-realtime-preview` (2024-10-01)
 
@@ -34,10 +35,10 @@ Before you can use GPT-4o real-time audio, you need:
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
 - An Azure OpenAI resource created in a [supported region](#supported-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](create-resource.md).
-- You need a deployment of the `gpt-4o-realtime-preview` model in a supported region as described in the [supported models](#supported-models) section. You can deploy the model from the [Azure AI Foundry portal model catalog](../../../ai-studio/how-to/model-catalog-overview.md) or from your project in Azure AI Foundry portal. 
+- You need a deployment of the `gpt-4o-realtime-preview` or `gpt-4o-mini-realtime-preview` model in a supported region as described in the [supported models](#supported-models) section. You can deploy the model from the [Azure AI Foundry portal model catalog](../../../ai-studio/how-to/model-catalog-overview.md) or from your project in Azure AI Foundry portal. 
 
 Here are some of the ways you can get started with the GPT-4o Realtime API for speech and audio:
-- For steps to deploy and use the `gpt-4o-realtime-preview` model, see [the real-time audio quickstart](../realtime-audio-quickstart.md).
+- For steps to deploy and use the `gpt-4o-realtime-preview` or `gpt-4o-mini-realtime-preview` model, see [the real-time audio quickstart](../realtime-audio-quickstart.md).
 - Download the sample code from the [Azure OpenAI GPT-4o real-time audio repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk).
 - [The Azure-Samples/aisearch-openai-rag-audio repo](https://github.com/Azure-Samples/aisearch-openai-rag-audio) contains an example of how to implement RAG support in applications that use voice as their user interface, powered by the GPT-4o realtime API for audio.
 
@@ -52,16 +53,16 @@ The Realtime API is accessed via a secure WebSocket connection to the `/realtime
 
 You can construct a full request URI by concatenating:
 
-- The secure WebSocket (`wss://`) protocol
+- The secure WebSocket (`wss://`) protocol.
 - Your Azure OpenAI resource endpoint hostname, for example, `my-aoai-resource.openai.azure.com`
-- The `openai/realtime` API path
-- An `api-version` query string parameter for a supported API version such as `2024-10-01-preview`
-- A `deployment` query string parameter with the name of your `gpt-4o-realtime-preview` model deployment
+- The `openai/realtime` API path.
+- An `api-version` query string parameter for a supported API version such as `2024-12-17`
+- A `deployment` query string parameter with the name of your `gpt-4o-realtime-preview` or `gpt-4o-mini-realtime-preview` model deployment.
 
 The following example is a well-constructed `/realtime` request URI:
 
 ```http
-wss://my-eastus2-openai-resource.openai.azure.com/openai/realtime?api-version=2024-10-01-preview&deployment=gpt-4o-realtime-preview-deployment-name
+wss://my-eastus2-openai-resource.openai.azure.com/openai/realtime?api-version=2024-12-17&deployment=gpt-4o-mini-realtime-preview-deployment-name
 ```
 
 To authenticate:
@@ -346,7 +347,7 @@ When you connect to the `/realtime` endpoint, the server responds with a [`sessi
   "session": {
     "id": "REDACTED",
     "object": "realtime.session",
-    "model": "gpt-4o-realtime-preview-2024-10-01",
+    "model": "gpt-4o-mini-realtime-preview-2024-12-17",
     "expires_at": 1734626723,
     "modalities": [
       "audio",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいリアルタイムオーディオモデルの追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスのリアルタイムオーディオに関する文書に新たに`gpt-4o-mini-realtime-preview`モデルを追加するもので、これにより利用可能なモデルの選択肢が広がります。具体的には、リアルタイムAPIを使用する際のサポートモデルのセクションが更新され、新しいモデルに関する情報が明記されています。また、リソースをデプロイする際に必要な条件の説明も調整され、`gpt-4o-realtime-preview`および新たに追加された`gpt-4o-mini-realtime-preview`両方のモデルを使用することができると記載されています。これにより、ユーザーは2つのモデルのどちらかを選択してリアルタイムオーディオ機能を利用できるようになります。さらに、URIの構築の部分でも新しいモデルに合わせたバージョン情報の更新が行われています。

## articles/ai-services/openai/how-to/structured-outputs.md{#item-cc2557}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ Structured outputs make a model follow a [JSON Schema](https://json-schema.org/o
 > Currently structured outputs are not supported with:
 > - [Bring your own data](../concepts/use-your-data.md) scenarios.
 > - [Assistants](../how-to/assistant.md) or [Azure AI Agents Service](../../agents/overview.md).
-> - `gpt-4o-audio-preview` version: `2024-12-17`.
+> - `gpt-4o-audio-preview` and `gpt-4o-mini-audio-preview` version: `2024-12-17`.
 
 ## Supported models
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "構造化出力のサポートモデルの更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおける構造化出力に関する文書の更新であり、サポートされていないモデルのリストに新たに`gpt-4o-mini-audio-preview`モデルが追加されました。具体的には、現在構造化出力がサポートされていないモデルの項目が修正され、`gpt-4o-audio-preview`のみから、`gpt-4o-mini-audio-preview`も含まれるように更新されています。この更新は、ユーザーに対してどのモデルが構造化出力の機能を利用できるかを明確にし、使用できないモデルに関する情報を正確に提供することを目的としています。

## articles/ai-services/openai/includes/audio-completions-ai-foundry.md{#item-748538}

<details>
<summary>Diff</summary>
````diff
@@ -15,11 +15,11 @@ ms.date: 1/7/2025
 
 ## Use GPT-4o audio generation
 
-To chat with your deployed `gpt-4o-audio-preview` model in the **Chat** playground of [Azure AI Foundry portal](https://ai.azure.com), follow these steps:
+To chat with your deployed `gpt-4o-mini-audio-preview` model in the **Chat** playground of [Azure AI Foundry portal](https://ai.azure.com), follow these steps:
 
-1. Go to the [Azure OpenAI Service page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource and the deployed `gpt-4o-audio-preview` model.
+1. Go to the [Azure OpenAI Service page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource and the deployed `gpt-4o-mini-audio-preview` model.
 1. Select the **Chat** playground from under **Resource playground** in the left pane.
-1. Select your deployed `gpt-4o-audio-preview` model from the **Deployment** dropdown. 
+1. Select your deployed `gpt-4o-mini-audio-preview` model from the **Deployment** dropdown. 
 1. Start chatting with the model and listen to the audio responses.
 
     :::image type="content" source="../media/quickstarts/audio-completions-chat-playground.png" alt-text="Screenshot of the Chat playground page." lightbox="../media/quickstarts/audio-completions-chat-playground.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル名の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるオーディオ生成に関する文書の一部で、`gpt-4o-audio-preview`モデルの記述を`gpt-4o-mini-audio-preview`モデルに更新する内容です。手順の各ステップで参照されるモデル名が変更されており、ユーザーがAzure AI Foundryポータル内での操作を行う際に、最新のモデルを正確に使用できるようにしています。この更新により、ユーザーは新たにデプロイされた`gpt-4o-mini-audio-preview`モデルを適切に選択し、チャット機能を利用できるようになります。

## articles/ai-services/openai/includes/audio-completions-deploy-model.md{#item-c5a63e}

<details>
<summary>Diff</summary>
````diff
@@ -7,12 +7,12 @@ ms.topic: include
 ms.date: 1/21/2025
 ---
 
-To deploy the `gpt-4o-audio-preview` model in the Azure AI Foundry portal:
-1. Go to the [Azure OpenAI Service page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource and the deployed `gpt-4o-audio-preview` model.
+To deploy the `gpt-4o-mini-audio-preview` model in the Azure AI Foundry portal:
+1. Go to the [Azure OpenAI Service page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource and the deployed `gpt-4o-mini-audio-preview` model.
 1. Select the **Chat** playground from under **Playgrounds** in the left pane.
 1. Select **+ Create new deployment** > **From base models** to open the deployment window. 
-1. Search for and select the `gpt-4o-audio-preview` model and then select **Deploy to selected resource**.
+1. Search for and select the `gpt-4o-mini-audio-preview` model and then select **Deploy to selected resource**.
 1. In the deployment wizard, select the `2024-12-17` model version.
 1. Follow the wizard to finish deploying the model.
 
-Now that you have a deployment of the `gpt-4o-audio-preview` model, you can interact with it in the Azure AI Foundry portal **Chat** playground or chat completions API.
+Now that you have a deployment of the `gpt-4o-mini-audio-preview` model, you can interact with it in the Azure AI Foundry portal **Chat** playground or chat completions API.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オーディオモデルのデプロイ手順の更新"
}
```

### Explanation
この変更は、Azure AI Foundryポータルにおけるオーディオモデルのデプロイ手順に関する文書の更新で、`gpt-4o-audio-preview`モデルが`gpt-4o-mini-audio-preview`モデルに変更されています。具体的には、デプロイ手順の各ステップで参照されるモデル名が更新されており、ユーザーが最新の`gpt-4o-mini-audio-preview`モデルを正しくデプロイできるようにしています。また、手順が明確にされ、ユーザーが正しい操作を行うためのガイドラインが提供されています。この更新により、ユーザーは所定のモデルを効率的にデプロイし、使用を開始できることになります。

## articles/ai-services/openai/includes/audio-completions-intro.md{#item-7391cb}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.topic: include
 ms.date: 1/21/2025
 ---
 
-The `gpt-4o-audio-preview` model introduces the audio modality into the existing `/chat/completions` API. The audio model expands the potential for AI applications in text and voice-based interactions and audio analysis. Modalities supported in `gpt-4o-audio-preview` model include:  text, audio, and text + audio.
+The `gpt-4o-audio-preview` and `gpt-4o-mini-audio-preview` models introduce the audio modality into the existing `/chat/completions` API. The audio model expands the potential for AI applications in text and voice-based interactions and audio analysis. Modalities supported in `gpt-4o-audio-preview` and `gpt-4o-mini-audio-preview` models include:  text, audio, and text + audio.
 
 Here's a table of the supported modalities with example use cases:
 
@@ -23,9 +23,9 @@ By using audio generation capabilities, you can achieve more dynamic and interac
 
 ## Supported models
 
-Currently only `gpt-4o-audio-preview` version: `2024-12-17` supports audio generation.
+Currently only `gpt-4o-audio-preview` and `gpt-4o-mini-audio-preview` version: `2024-12-17` supports audio generation.
 
-The `gpt-4o-audio-preview` model is available for global deployments in [East US 2 and Sweden Central regions](../concepts/models.md#global-standard-model-availability).
+The `gpt-4o-audio-preview` and and `gpt-4o-mini-audio-preview` models are available for global deployments in [East US 2 and Sweden Central regions](../concepts/models.md#global-standard-model-availability).
 
 Currently the following voices are supported for audio out: Alloy, Echo, and Shimmer.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オーディオモデルの導入とサポートの更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるオーディオモデルの紹介文書の更新で、`gpt-4o-audio-preview`モデルに加えて、`gpt-4o-mini-audio-preview`モデルが新たに言及されています。具体的には、これらのモデルが`/chat/completions` APIに音声モダリティを取り入れ、テキストと音声の対話や音声分析におけるAIアプリケーションの可能性を拡大することを示しています。また、サポートされているモデルのリストも更新され、両方のモデルが音声生成をサポートしていることが明確にされています。この変更により、ユーザーは新しいモデルの機能を理解し、どのモデルを使用すべきかを判断する際のガイダンスを得ることができます。

## articles/ai-services/openai/includes/audio-completions-javascript.md{#item-b1be01}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.date: 1/21/2025
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
 - <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
 - An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
-- Then, you need to deploy a `gpt-4o-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
+- Then, you need to deploy a `gpt-4o-mini-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
 
 ## Microsoft Entra ID prerequisites
 
@@ -85,7 +85,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     // Set environment variables or edit the corresponding values here.
     const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
     const apiVersion = "2025-01-01-preview"; 
-    const deployment = "gpt-4o-audio-preview"; 
+    const deployment = "gpt-4o-mini-audio-preview"; 
     
     const client = new AzureOpenAI({ 
         endpoint, 
@@ -98,7 +98,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     
         // Make the audio chat completions request
         const response = await client.chat.completions.create({ 
-            model: "gpt-4o-audio-preview", 
+            model: "gpt-4o-mini-audio-preview", 
             modalities: ["text", "audio"], 
             audio: { voice: "alloy", format: "wav" }, 
             messages: [ 
@@ -153,7 +153,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
     const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
     const apiVersion = "2025-01-01-preview"; 
-    const deployment = "gpt-4o-audio-preview"; 
+    const deployment = "gpt-4o-mini-audio-preview"; 
     
     const client = new AzureOpenAI({ 
         endpoint, 
@@ -166,7 +166,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     
         // Make the audio chat completions request
         const response = await client.chat.completions.create({ 
-            model: "gpt-4o-audio-preview", 
+            model: "gpt-4o-mini-audio-preview", 
             modalities: ["text", "audio"], 
             audio: { voice: "alloy", format: "wav" }, 
             messages: [ 
@@ -231,7 +231,7 @@ The script generates an audio file named _dog.wav_ in the same directory as the
     // Set environment variables or edit the corresponding values here.
     const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
     const apiVersion = "2025-01-01-preview"; 
-    const deployment = "gpt-4o-audio-preview"; 
+    const deployment = "gpt-4o-mini-audio-preview"; 
     
     const client = new AzureOpenAI({ 
         endpoint, 
@@ -248,7 +248,7 @@ The script generates an audio file named _dog.wav_ in the same directory as the
         
         // Make the audio chat completions request
         const response = await client.chat.completions.create({
-            model: "gpt-4o-audio-preview",
+            model: "gpt-4o-mini-audio-preview",
             modalities: ["text", "audio"],
             audio: { voice: "alloy", format: "wav" }, 
             messages: [
@@ -315,7 +315,7 @@ The script generates an audio file named _dog.wav_ in the same directory as the
     const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
     const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
     const apiVersion = "2025-01-01-preview"; 
-    const deployment = "gpt-4o-audio-preview"; 
+    const deployment = "gpt-4o-mini-audio-preview"; 
     
     const client = new AzureOpenAI({ 
         endpoint, 
@@ -332,7 +332,7 @@ The script generates an audio file named _dog.wav_ in the same directory as the
         
         // Make the audio chat completions request
         const response = await client.chat.completions.create({
-            model: "gpt-4o-audio-preview",
+            model: "gpt-4o-mini-audio-preview",
             modalities: ["text", "audio"],
             audio: { voice: "alloy", format: "wav" }, 
             messages: [
@@ -406,7 +406,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     // Set environment variables or edit the corresponding values here.
     const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
     const apiVersion = "2025-01-01-preview"; 
-    const deployment = "gpt-4o-audio-preview"; 
+    const deployment = "gpt-4o-mini-audio-preview"; 
     
     const client = new AzureOpenAI({ 
         endpoint, 
@@ -444,7 +444,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
         // Get the first turn's response 
     
         const response = await client.chat.completions.create({ 
-            model: "gpt-4o-audio-preview",
+            model: "gpt-4o-mini-audio-preview",
             modalities: ["text", "audio"], 
             audio: { voice: "alloy", format: "wav" }, 
             messages: messages
@@ -471,7 +471,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     
         // Send the follow-up request with the accumulated messages
         const followResponse = await client.chat.completions.create({ 
-            model: "gpt-4o-audio-preview",
+            model: "gpt-4o-mini-audio-preview",
             messages: messages
         });
     
@@ -511,7 +511,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
     const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
     const apiVersion = "2025-01-01-preview"; 
-    const deployment = "gpt-4o-audio-preview"; 
+    const deployment = "gpt-4o-mini-audio-preview"; 
     
     const client = new AzureOpenAI({ 
         endpoint, 
@@ -549,7 +549,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
         // Get the first turn's response 
     
         const response = await client.chat.completions.create({ 
-            model: "gpt-4o-audio-preview",
+            model: "gpt-4o-mini-audio-preview",
             modalities: ["text", "audio"], 
             audio: { voice: "alloy", format: "wav" }, 
             messages: messages
@@ -576,7 +576,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     
         // Send the follow-up request with the accumulated messages
         const followResponse = await client.chat.completions.create({ 
-            model: "gpt-4o-audio-preview",
+            model: "gpt-4o-mini-audio-preview",
             messages: messages
         });
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptでのオーディオモデルの使用に関する更新"
}
```

### Explanation
この変更は、JavaScriptにおけるAzure OpenAIサービスのオーディオモデルに関する文書の更新です。特に、デプロイするオーディオモデルが`gpt-4o-audio-preview`から`gpt-4o-mini-audio-preview`に変更されており、関連するすべてのコードスニペットでのモデル名が更新されています。これにより、開発者は最新のモデルを正しく使用できるようになります。また、ドキュメント内の条件や手順が一貫して変更されているため、ユーザーがアプリケーションにおいて音声機能を利用する際に、最新の情報を基にした実装が可能になります。この更新は、特に音声生成や対話システムを構築する開発者にとって重要です。

## articles/ai-services/openai/includes/audio-completions-python.md{#item-a88047}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ Use this guide to get started generating audio with the Azure OpenAI SDK for Pyt
 - An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
 - <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>. We recommend using Python 3.10 or later, but having at least Python 3.8 is required. If you don't have a suitable version of Python installed, you can follow the instructions in the [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter) for the easiest way of installing Python on your operating system.
 - An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
-- Then, you need to deploy a `gpt-4o-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- Then, you need to deploy a `gpt-4o-mini-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 ## Microsoft Entra ID prerequisites
 
@@ -107,7 +107,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     
     # Make the audio chat completions request
     completion=client.chat.completions.create(
-        model="gpt-4o-audio-preview",
+        model="gpt-4o-mini-audio-preview",
         modalities=["text", "audio"],
         audio={"voice": "alloy", "format": "wav"},
         messages=[
@@ -153,7 +153,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     
     # Make the audio chat completions request
     completion = client.chat.completions.create(
-        model="gpt-4o-audio-preview",
+        model="gpt-4o-mini-audio-preview",
         modalities=["text", "audio"],
         audio={"voice": "alloy", "format": "wav"},
         messages=[
@@ -216,7 +216,7 @@ The script generates an audio file named _dog.wav_ in the same directory as the
      
     # Make the audio chat completions request
     completion = client.chat.completions.create( 
-        model="gpt-4o-audio-preview", 
+        model="gpt-4o-mini-audio-preview", 
         modalities=["text", "audio"], 
         audio={"voice": "alloy", "format": "wav"}, 
         messages=[ 
@@ -278,7 +278,7 @@ The script generates an audio file named _dog.wav_ in the same directory as the
      
     # Make the audio chat completions request
     completion = client.chat.completions.create( 
-        model="gpt-4o-audio-preview", 
+        model="gpt-4o-mini-audio-preview", 
         modalities=["text", "audio"], 
         audio={"voice": "alloy", "format": "wav"}, 
         messages=[ 
@@ -370,7 +370,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     # Get the first turn's response
     
     completion = client.chat.completions.create( 
-        model="gpt-4o-audio-preview", 
+        model="gpt-4o-mini-audio-preview", 
         modalities=["text", "audio"], 
         audio={"voice": "alloy", "format": "wav"}, 
         messages=messages
@@ -396,7 +396,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     
     # Send the follow-up request with the accumulated messages
     completion = client.chat.completions.create( 
-        model="gpt-4o-audio-preview", 
+        model="gpt-4o-mini-audio-preview", 
         messages=messages
     ) 
     
@@ -451,7 +451,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     # Get the first turn's response 
     
     completion = client.chat.completions.create( 
-        model="gpt-4o-audio-preview", 
+        model="gpt-4o-mini-audio-preview", 
         modalities=["text", "audio"], 
         audio={"voice": "alloy", "format": "wav"}, 
         messages=messages
@@ -477,7 +477,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     
     # Send the follow-up request with the accumulated messages 
     completion = client.chat.completions.create( 
-        model="gpt-4o-audio-preview", 
+        model="gpt-4o-mini-audio-preview", 
         messages=messages
     ) 
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonでのオーディオモデルの使用に関する更新"
}
```

### Explanation
この変更は、Python向けAzure OpenAI SDKにおけるオーディオモデルに関する文書を更新したものです。主な変更点として、ユーザーがデプロイするモデルが`gpt-4o-audio-preview`から`gpt-4o-mini-audio-preview`に変更されたことが挙げられます。この改訂に伴い、文中のすべての関連箇所でモデル名が更新され、ユーザーは新しいモデルを使用することが明示されています。また、音声生成や音声チャットのリクエストを行う際のコードスニペットも更新されており、最新の情報に基づいて正確な実装ができるようになっています。これにより、開発者はAzure OpenAIの音声機能を効果的に活用できるようになります。

## articles/ai-services/openai/includes/audio-completions-rest.md{#item-0ec305}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.date: 1/21/2025
 - An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
 - <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>. We recommend using Python 3.10 or later, but having at least Python 3.8 is required. If you don't have a suitable version of Python installed, you can follow the instructions in the [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter) for the easiest way of installing Python on your operating system.
 - An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
-- Then, you need to deploy a `gpt-4o-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- Then, you need to deploy a `gpt-4o-mini-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 ## Microsoft Entra ID prerequisites
 
@@ -101,11 +101,11 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     token = credential.get_token("https://cognitiveservices.azure.com/.default")
     
     api_version = '2025-01-01-preview'
-    url = f"{endpoint}/openai/deployments/gpt-4o-audio-preview/chat/completions?api-version={api_version}"
+    url = f"{endpoint}/openai/deployments/gpt-4o-mini-audio-preview/chat/completions?api-version={api_version}"
     headers= { "Authorization": f"Bearer {token.token}", "Content-Type": "application/json" }
     body = {
       "modalities": ["audio", "text"],
-      "model": "gpt-4o-audio-preview",
+      "model": "gpt-4o-mini-audio-preview",
       "audio": {
           "format": "wav",
           "voice": "alloy"
@@ -154,11 +154,11 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     api_key = os.environ['AZURE_OPENAI_API_KEY']
     
     api_version = '2025-01-01-preview'
-    url = f"{endpoint}/openai/deployments/gpt-4o-audio-preview/chat/completions?api-version={api_version}"
+    url = f"{endpoint}/openai/deployments/gpt-4o-mini-audio-preview/chat/completions?api-version={api_version}"
     headers= { "api-key": api_key, "Content-Type": "application/json" }
     body = {
       "modalities": ["audio", "text"],
-      "model": "gpt-4o-audio-preview",
+      "model": "gpt-4o-mini-audio-preview",
       "audio": {
           "format": "wav",
           "voice": "alloy"
@@ -224,11 +224,11 @@ The script generates an audio file named _dog.wav_ in the same directory as the
       encoded_string = base64.b64encode(wav_reader.read()).decode('utf-8') 
     
     api_version = '2025-01-01-preview'
-    url = f"{endpoint}/openai/deployments/gpt-4o-audio-preview/chat/completions?api-version={api_version}"
+    url = f"{endpoint}/openai/deployments/gpt-4o-mini-audio-preview/chat/completions?api-version={api_version}"
     headers= { "Authorization": f"Bearer {token.token}", "Content-Type": "application/json" }
     body = {
       "modalities": ["audio", "text"],
-      "model": "gpt-4o-audio-preview",
+      "model": "gpt-4o-mini-audio-preview",
       "audio": {
           "format": "wav",
           "voice": "alloy"
@@ -288,11 +288,11 @@ The script generates an audio file named _dog.wav_ in the same directory as the
       encoded_string = base64.b64encode(wav_reader.read()).decode('utf-8') 
     
     api_version = '2025-01-01-preview'
-    url = f"{endpoint}/openai/deployments/gpt-4o-audio-preview/chat/completions?api-version={api_version}"
+    url = f"{endpoint}/openai/deployments/gpt-4o-mini-audio-preview/chat/completions?api-version={api_version}"
     headers= { "api-key": api_key, "Content-Type": "application/json" }
     body = {
       "modalities": ["audio", "text"],
-      "model": "gpt-4o-audio-preview",
+      "model": "gpt-4o-mini-audio-preview",
       "audio": {
           "format": "wav",
           "voice": "alloy"
@@ -364,7 +364,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     token = credential.get_token("https://cognitiveservices.azure.com/.default")
     
     api_version = '2025-01-01-preview'
-    url = f"{endpoint}/openai/deployments/gpt-4o-audio-preview/chat/completions?api-version={api_version}"
+    url = f"{endpoint}/openai/deployments/gpt-4o-mini-audio-preview/chat/completions?api-version={api_version}"
     headers= { "Authorization": f"Bearer {token.token}", "Content-Type": "application/json" }
     
     # Read and encode audio file  
@@ -392,7 +392,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     
     body = {
       "modalities": ["audio", "text"],
-      "model": "gpt-4o-audio-preview",
+      "model": "gpt-4o-mini-audio-preview",
       "audio": {
           "format": "wav",
           "voice": "alloy"
@@ -422,7 +422,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     }) 
     
     body = {
-      "model": "gpt-4o-audio-preview",
+      "model": "gpt-4o-mini-audio-preview",
       "messages": messages
     }
     
@@ -454,7 +454,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     api_key = os.environ['AZURE_OPENAI_API_KEY']
     
     api_version = '2025-01-01-preview'
-    url = f"{endpoint}/openai/deployments/gpt-4o-audio-preview/chat/completions?api-version={api_version}"
+    url = f"{endpoint}/openai/deployments/gpt-4o-mini-audio-preview/chat/completions?api-version={api_version}"
     headers= { "api-key": api_key, "Content-Type": "application/json" }
     
     # Read and encode audio file  
@@ -482,7 +482,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     
     body = {
       "modalities": ["audio", "text"],
-      "model": "gpt-4o-audio-preview",
+      "model": "gpt-4o-mini-audio-preview",
       "audio": {
           "format": "wav",
           "voice": "alloy"
@@ -513,7 +513,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     }) 
     
     body = {
-      "model": "gpt-4o-audio-preview",
+      "model": "gpt-4o-mini-audio-preview",
       "messages": messages
     }
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIにおけるオーディオモデルの使用に関する更新"
}
```

### Explanation
この変更は、Azure OpenAIのREST APIに関する文書の更新であり、使用するオーディオモデルが`gpt-4o-audio-preview`から`gpt-4o-mini-audio-preview`に変更されました。更新された内容には、モデル名が新しいものに置き換えられたことが含まれ、ユーザーはこの新しいモデルを使用して音声チャットのリクエストを行うことが明示されています。この変更が適用されたことにより、APIのエンドポイントのURLやリクエストボディ内でも、すべての関連箇所でモデル名が一貫して更新されています。この改訂により、開発者は最新の情報を基にして正確なリクエストを行うことができ、音声生成の機能をより効果的に活用できるようになります。

## articles/ai-services/openai/includes/audio-completions-typescript.md{#item-94bc1f}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ ms.date: 1/21/2025
 - <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
 - [TypeScript](https://www.typescriptlang.org/download/) installed globally.
 - An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
-- Then, you need to deploy a `gpt-4o-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
+- Then, you need to deploy a `gpt-4o-mini-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
 
 ## Microsoft Entra ID prerequisites
 
@@ -84,7 +84,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     // Set environment variables or edit the corresponding values here.
     const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
     const apiVersion: string = "2025-01-01-preview"; 
-    const deployment: string = "gpt-4o-audio-preview"; 
+    const deployment: string = "gpt-4o-mini-audio-preview"; 
     
     // Keyless authentication 
     const getClient = (): AzureOpenAI => {
@@ -105,7 +105,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     
         // Make the audio chat completions request
         const response = await client.chat.completions.create({ 
-            model: "gpt-4o-audio-preview", 
+            model: "gpt-4o-mini-audio-preview", 
             modalities: ["text", "audio"], 
             audio: { voice: "alloy", format: "wav" }, 
             messages: [ 
@@ -183,7 +183,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
     const apiKey: string = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
     const apiVersion: string = "2025-01-01-preview"; 
-    const deployment: string = "gpt-4o-audio-preview"; 
+    const deployment: string = "gpt-4o-mini-audio-preview"; 
     
     const client = new AzureOpenAI({ 
       endpoint, 
@@ -196,7 +196,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     
         // Make the audio chat completions request
         const response = await client.chat.completions.create({ 
-            model: "gpt-4o-audio-preview", 
+            model: "gpt-4o-mini-audio-preview", 
             modalities: ["text", "audio"], 
             audio: { voice: "alloy", format: "wav" }, 
             messages: [ 
@@ -282,7 +282,7 @@ The script generates an audio file named _dog.wav_ in the same directory as the
     // Set environment variables or edit the corresponding values here.
     const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
     const apiVersion: string = "2025-01-01-preview"; 
-    const deployment: string = "gpt-4o-audio-preview"; 
+    const deployment: string = "gpt-4o-mini-audio-preview"; 
     
     // Keyless authentication 
     const getClient = (): AzureOpenAI => {
@@ -307,7 +307,7 @@ The script generates an audio file named _dog.wav_ in the same directory as the
         
         // Make the audio chat completions request
         const response = await client.chat.completions.create({ 
-          model: "gpt-4o-audio-preview",
+          model: "gpt-4o-mini-audio-preview",
           modalities: ["text", "audio"], 
           audio: { voice: "alloy", format: "wav" },
           messages: [ 
@@ -394,7 +394,7 @@ The script generates an audio file named _dog.wav_ in the same directory as the
     const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
     const apiKey: string = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
     const apiVersion: string = "2025-01-01-preview"; 
-    const deployment: string = "gpt-4o-audio-preview"; 
+    const deployment: string = "gpt-4o-mini-audio-preview"; 
     
     const client = new AzureOpenAI({ 
       endpoint, 
@@ -411,7 +411,7 @@ The script generates an audio file named _dog.wav_ in the same directory as the
       
       // Make the audio chat completions request
       const response = await client.chat.completions.create({ 
-        model: "gpt-4o-audio-preview",
+        model: "gpt-4o-mini-audio-preview",
         modalities: ["text", "audio"], 
         audio: { voice: "alloy", format: "wav" },
         messages: [ 
@@ -505,7 +505,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     // Set environment variables or edit the corresponding values here.
     const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
     const apiVersion: string = "2025-01-01-preview"; 
-    const deployment: string = "gpt-4o-audio-preview"; 
+    const deployment: string = "gpt-4o-mini-audio-preview"; 
     
     // Keyless authentication 
     const getClient = (): AzureOpenAI => {
@@ -551,7 +551,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
         // Get the first turn's response 
     
         const response = await client.chat.completions.create({ 
-            model: "gpt-4o-audio-preview",
+            model: "gpt-4o-mini-audio-preview",
             modalities: ["text", "audio"], 
             audio: { voice: "alloy", format: "wav" }, 
             messages: messages
@@ -578,7 +578,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     
         // Send the follow-up request with the accumulated messages
         const followResponse = await client.chat.completions.create({ 
-            model: "gpt-4o-audio-preview",
+            model: "gpt-4o-mini-audio-preview",
             messages: messages
         });
     
@@ -638,7 +638,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT" as string;
     const apiKey: string = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
     const apiVersion: string = "2025-01-01-preview"; 
-    const deployment: string = "gpt-4o-audio-preview"; 
+    const deployment: string = "gpt-4o-mini-audio-preview"; 
     
     const client = new AzureOpenAI({ 
       endpoint, 
@@ -676,7 +676,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
         // Get the first turn's response 
         
         const response = await client.chat.completions.create({ 
-          model: "gpt-4o-audio-preview",
+          model: "gpt-4o-mini-audio-preview",
           modalities: ["text", "audio"], 
           audio: { voice: "alloy", format: "wav" }, 
           messages: messages
@@ -703,7 +703,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     
         // Send the follow-up request with the accumulated messages
         const followResponse = await client.chat.completions.create({ 
-            model: "gpt-4o-audio-preview",
+            model: "gpt-4o-mini-audio-preview",
             messages: messages
         });
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptでのオーディオモデルの使用に関する更新"
}
```

### Explanation
この変更は、TypeScriptでのAzure OpenAIのオーディオモデルに関する文書を更新したもので、主にモデル名が`gpt-4o-audio-preview`から`gpt-4o-mini-audio-preview`に変更されました。この変更により、ユーザーは新しいモデルを使用して音声チャットのリクエストを行うことができます。具体的には、コード内のさまざまな箇所で、モデル名やAPIエンドポイントの設定が一貫して更新されています。これにより、開発者は最新の情報を基に音声生成機能を利用でき、正確なリクエストが可能となるため、技術文書の整合性と信頼性が向上しています。

## articles/ai-services/openai/includes/realtime-deploy-model.md{#item-21f911}

<details>
<summary>Diff</summary>
````diff
@@ -7,12 +7,12 @@ ms.topic: include
 ms.date: 1/21/2025
 ---
 
-To deploy the `gpt-4o-realtime-preview` model in the Azure AI Foundry portal:
+To deploy the `gpt-4o-mini-realtime-preview` model in the Azure AI Foundry portal:
 1. Go to the [Azure OpenAI Service page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource (with or without model deployments.)
 1. Select the **Real-time audio** playground from under **Playgrounds** in the left pane.
 1. Select **+ Create new deployment** > **From base models** to open the deployment window. 
-1. Search for and select the `gpt-4o-realtime-preview` model and then select **Deploy to selected resource**.
+1. Search for and select the `gpt-4o-mini-realtime-preview` model and then select **Deploy to selected resource**.
 1. In the deployment wizard, select the `2024-12-17` model version.
 1. Follow the wizard to finish deploying the model.
 
-Now that you have a deployment of the `gpt-4o-realtime-preview` model, you can interact with it in real time in the Azure AI Foundry portal **Real-time audio** playground or Realtime API.
+Now that you have a deployment of the `gpt-4o-mini-realtime-preview` model, you can interact with it in real time in the Azure AI Foundry portal **Real-time audio** playground or Realtime API.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムデプロイモデルに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Foundryポータルにおけるモデルのデプロイメントに関する文書を更新したもので、使用するモデルが`gpt-4o-realtime-preview`から`gpt-4o-mini-realtime-preview`に変更されました。具体的には、デプロイ手順の中でモデル名が新しいものに置き換えられ、ユーザーはこの新しいモデルを使ってリソースにデプロイする手順を実行することが明示されています。更新された文書によって、ユーザーは最新のモデルを使用してリアルタイムで音声処理を行うことができ、正確な手順が提供されることで、デプロイメントの成功率が向上します。全体として、この変更はユーザーの体験を向上させ、正確で効果的なデプロイメントを支援するものです。

## articles/ai-services/openai/includes/realtime-javascript.md{#item-3c125e}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.date: 1/21/2025
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
 - <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
 - An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
-- Then, you need to deploy a `gpt-4o-realtime-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
+- Then, you need to deploy a `gpt-4o-mini-realtime-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
 
 ### Microsoft Entra ID prerequisites
 
@@ -78,7 +78,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     async function text_in_audio_out() {
         // Set environment variables or edit the corresponding values here.
         const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "yourEndpoint";
-        const deployment = "gpt-4o-realtime-preview";
+        const deployment = "gpt-4o-mini-realtime-preview";
         if (!endpoint || !deployment) {
             throw new Error("You didn't set the environment variables.");
         }
@@ -148,7 +148,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
         // Set environment variables or edit the corresponding values here.
         const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "yourKey";
         const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "yourEndpoint";
-        const deployment = "gpt-4o-realtime-preview";
+        const deployment = "gpt-4o-mini-realtime-preview";
         if (!endpoint || !deployment) {
             throw new Error("You didn't set the environment variables.");
         }
@@ -261,7 +261,7 @@ You can run the sample code locally on your machine by following these steps. Re
 1. Enter the following information in the web interface:
     - **Endpoint**: The resource endpoint of an Azure OpenAI resource. You don't need to append the `/realtime` path. An example structure might be `https://my-azure-openai-resource-from-portal.openai.azure.com`.
     - **API Key**: A corresponding API key for the Azure OpenAI resource.
-    - **Deployment**: The name of the `gpt-4o-realtime-preview` model that [you deployed in the previous section](#deploy-a-model-for-real-time-audio).
+    - **Deployment**: The name of the `gpt-4o-mini-realtime-preview` model that [you deployed in the previous section](#deploy-a-model-for-real-time-audio).
     - **System Message**: Optionally, you can provide a system message such as "You always talk like a friendly pirate."
     - **Temperature**: Optionally, you can provide a custom temperature.
     - **Voice**: Optionally, you can select a voice.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptでのリアルタイムモデルに関するドキュメントの更新"
}
```

### Explanation
この変更は、JavaScriptにおけるAzure OpenAIのリアルタイムモデルに関する文書を更新したもので、主にデプロイするモデルが`gpt-4o-realtime-preview`から`gpt-4o-mini-realtime-preview`に変更されました。この変更により、ユーザーは新しいモデルを利用してリアルタイムで音声リクエストを行うことが可能になります。また、環境変数設定や実行時のインターフェースでのモデル名も適切に変更されています。これにより、最新の情報に基づいた正確な使い方が提供され、開発者が新モデルを使用する際の混乱を避けることができるようになりました。全体として、この更新はユーザー体験の向上と技術文書の整合性を確保するための重要な改善です。

## articles/ai-services/openai/includes/realtime-portal.md{#item-1b81a2}

<details>
<summary>Diff</summary>
````diff
@@ -13,11 +13,11 @@ ms.date: 1/21/2025
 
 ## Use the GPT-4o real-time audio
 
-To chat with your deployed `gpt-4o-realtime-preview` model in the [Azure AI Foundry](https://ai.azure.com) **Real-time audio** playground, follow these steps:
+To chat with your deployed `gpt-4o-mini-realtime-preview` model in the [Azure AI Foundry](https://ai.azure.com) **Real-time audio** playground, follow these steps:
 
-1. Go to the [Azure OpenAI Service page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource and the deployed `gpt-4o-realtime-preview` model.
+1. Go to the [Azure OpenAI Service page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource and the deployed `gpt-4o-mini-realtime-preview` model.
 1. Select the **Real-time audio** playground from under **Playgrounds** in the left pane.
-1. Select your deployed `gpt-4o-realtime-preview` model from the **Deployment** dropdown. 
+1. Select your deployed `gpt-4o-mini-realtime-preview` model from the **Deployment** dropdown. 
 1. Select **Enable microphone** to allow the browser to access your microphone. If you already granted permission, you can skip this step.
 
     :::image type="content" source="../media/how-to/real-time/real-time-playground.png" alt-text="Screenshot of the real-time audio playground with the deployed model selected." lightbox="../media/how-to/real-time/real-time-playground.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムポータルでのモデル名の更新"
}
```

### Explanation
この変更は、Azure AI Foundryポータルにおけるリアルタイム音声チャットの手順を更新したものです。具体的には、使用するモデルが`gpt-4o-realtime-preview`から`gpt-4o-mini-realtime-preview`に変更されました。この更新に伴い、手順内の各ステップで新しいモデル名が反映され、ユーザーが正しいモデルを選択してチャットを行うためのガイダンスが明確に示されています。全体として、この修正により、ユーザーは最新のモデルを用いてAzure AI Foundryのリアルタイム音声遊び場でスムーズにやり取りを行うことができるようになります。これは、情報を最新の状態に保つことによるユーザー体験の向上を目的としています。

## articles/ai-services/openai/includes/realtime-python.md{#item-1291c0}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.date: 1/21/2025
 - An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
 - <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>. We recommend using Python 3.10 or later, but having at least Python 3.8 is required. If you don't have a suitable version of Python installed, you can follow the instructions in the [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter) for the easiest way of installing Python on your operating system.
 - An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
-- Then, you need to deploy a `gpt-4o-realtime-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- Then, you need to deploy a `gpt-4o-mini-realtime-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 ## Microsoft Entra ID prerequisites
 
@@ -96,7 +96,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     
     # Set environment variables or edit the corresponding values here.
     endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
-    deployment = "gpt-4o-realtime-preview"
+    deployment = "gpt-4o-mini-realtime-preview"
     
     async def text_in_audio_out():
         async with RTLowLevelClient(
@@ -158,7 +158,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     # Set environment variables or edit the corresponding values here.
     api_key = os.environ["AZURE_OPENAI_API_KEY"]    
     endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
-    deployment = "gpt-4o-realtime-preview"
+    deployment = "gpt-4o-mini-realtime-preview"
     
     async def text_in_audio_out():
         async with RTLowLevelClient(
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonでのリアルタイムモデルに関するドキュメントの更新"
}
```

### Explanation
この変更は、PythonにおけるAzure OpenAIのリアルタイムモデルに関する文書を更新したものです。主な変更点は、デプロイするモデルが`gpt-4o-realtime-preview`から`gpt-4o-mini-realtime-preview`に変更されたことです。この修正により、設定方法や使用手順が新しいモデルに合わせて更新されており、ユーザーは最新の情報に基づいてシステムを構築できるようになります。具体的には、環境変数設定やサンプルコード内でのモデル名が適正化されているため、開発者が正しいモデルを使えるようサポートしています。これにより、ユーザー体験が向上し、技術的な整合性が保たれます。

## articles/ai-services/openai/includes/realtime-typescript.md{#item-eacc9c}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ ms.date: 1/21/2025
 - <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
 - [TypeScript](https://www.typescriptlang.org/download/) installed globally.
 - An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
-- Then, you need to deploy a `gpt-4o-realtime-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
+- Then, you need to deploy a `gpt-4o-mini-realtime-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
 
 ### Microsoft Entra ID prerequisites
 
@@ -80,7 +80,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     async function text_in_audio_out() {
         // Set environment variables or edit the corresponding values here.
         const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "yourEndpoint";
-        const deployment = "gpt-4o-realtime-preview";
+        const deployment = "gpt-4o-mini-realtime-preview";
         if (!endpoint || !deployment) {
             throw new Error("You didn't set the environment variables.");
         }
@@ -176,7 +176,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
         // Set environment variables or edit the corresponding values here.
         const apiKey: string = process.env["AZURE_OPENAI_API_KEY"] || "yourKey";
         const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "yourEndpoint";
-        const deployment = "gpt-4o-realtime-preview";
+        const deployment = "gpt-4o-mini-realtime-preview";
         if (!endpoint || !deployment) {
             throw new Error("You didn't set the environment variables.");
         }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptでのリアルタイムモデルに関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、TypeScriptを使用したAzure OpenAIのリアルタイムモデルに関する文書の更新を示しています。主な修正点として、デプロイするモデル名が`gpt-4o-realtime-preview`から`gpt-4o-mini-realtime-preview`に変更されました。この変更により、ユーザーは正しいモデルを使った実装方法についての情報が提供され、最新のリソースに基づいて開発を進めることができるようになります。文書内では、環境変数の設定やサンプルコードにおいて新しいモデル名が適用されており、これにより開発者は正確な設定を行うことができ、エラーを回避する手助けとなります。全体として、この更新はドキュメントの整合性を高め、ユーザー体験を改善することを目的としています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -138,11 +138,14 @@ M = million | K = thousand
 
 ## gpt-4o audio
 
-The rate limits for each `gpt-4o-realtime-preview` model deployment are 100K TPM and 1K RPM. During the preview, Azure AI Foundry portal and APIs might inaccurately show different rate limits. Even if you try to set a different rate limit, the actual rate limit will be 100K TPM and 1K RPM.
+The rate limits for each `gpt-4o` audio model deployment are 100K TPM and 1K RPM. During the preview, Azure AI Foundry portal and APIs might inaccurately show different rate limits. Even if you try to set a different rate limit, the actual rate limit will be 100K TPM and 1K RPM.
 
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
 |---|---|:---:|:---:|
+|`gpt-4o-audio-preview` | Default | 100 K | 1 K |
 |`gpt-4o-realtime-preview` | Default | 100 K | 1 K |
+|`gpt-4o-mini-audio-preview` | Default | 100 K | 1 K |
+|`gpt-4o-mini-realtime-preview` | Default | 100 K | 1 K |
 
 M = million | K = thousand
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "gpt-4oモデルのレート制限に関する文書の更新"
}
```

### Explanation
この変更は、Azure OpenAIの`gpt-4o`モデルに関連するレート制限に関する文書の更新です。具体的には、モデルの名称に関する情報が追加され、`gpt-4o-realtime-preview`の記述が`gpt-4o`の音声モデル全体に関連付けられています。また、新しいモデルとして`gpt-4o-audio-preview`と`gpt-4o-mini-audio-preview`がリストに追加され、それぞれの標準のトークン毎分（TPM）およびリクエスト毎分（RPM）の制限が明示されています。この更新により、ユーザーは使用可能なモデルとその制限についてより明確な情報を得られるようになり、設計や実装時の参考になります。全体として、これによりドキュメントの正確性が向上し、ユーザー体験が改善されることが期待されます。

## articles/ai-services/openai/realtime-audio-quickstart.md{#item-727df8}

<details>
<summary>Diff</summary>
````diff
@@ -23,18 +23,16 @@ Most users of the Realtime API need to deliver and receive audio from an end-use
 
 ## Supported models
 
-The GPT 4o realtime models are available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability).
-- `gpt-4o-realtime-preview` (2024-12-17)
-- `gpt-4o-realtime-preview` (2024-10-01)
+The GPT 4o real-time models are available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability).
+- `gpt-4o-realtime-preview` (version `2024-12-17`)
+- `gpt-4o-mini-realtime-preview` (version `2024-12-17`)
+- `gpt-4o-realtime-preview` (version `2024-10-01`)
 
 See the [models and versions documentation](./concepts/models.md#gpt-4o-audio) for more information.
 
 ## API support
 
-Support for the Realtime API was first added in API version `2024-10-01-preview`. 
-
-> [!NOTE]
-> For more information about the API and architecture, see the [Azure OpenAI GPT-4o real-time audio repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk).
+Support for the Realtime API was first added in API version `2024-10-01-preview`. Use the latest `2024-12-17` model version. 
 
 ::: zone pivot="ai-foundry-portal"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azure OpenAIのリアルタイムオーディオのクイックスタートガイドに関する文書の更新を反映しています。主に、サポートされるモデルのリストが更新され、新たに`gpt-4o-mini-realtime-preview`モデルが追加されました。また、各モデルのバージョン番号が明示され、どのモデルが利用可能であるかがより明確になります。具体的には、`gpt-4o-realtime-preview`モデルとそのリリースバージョンが記載され、最新のモデルバージョンを使用することが強調されています。また、APIのサポートに関しても、最新のモデルバージョンの使用を促す文言が追加されており、ユーザーへの指針がより分かりやすくなっています。このような変更により、ユーザーは最新の情報をもとに実装を行うことができ、導入の際の混乱を避けることができます。

## articles/ai-services/openai/realtime-audio-reference.md{#item-276d51}

<details>
<summary>Diff</summary>
````diff
@@ -28,16 +28,16 @@ The Realtime API requires an existing Azure OpenAI resource endpoint in a suppor
 
 You can construct a full request URI by concatenating:
 
-- The secure WebSocket (`wss://`) protocol
+- The secure WebSocket (`wss://`) protocol.
 - Your Azure OpenAI resource endpoint hostname, for example, `my-aoai-resource.openai.azure.com`
-- The `openai/realtime` API path
-- An `api-version` query string parameter for a supported API version such as `2024-10-01-preview`
-- A `deployment` query string parameter with the name of your `gpt-4o-realtime-preview` model deployment
+- The `openai/realtime` API path.
+- An `api-version` query string parameter for a supported API version such as `2024-12-17`
+- A `deployment` query string parameter with the name of your `gpt-4o-realtime-preview` or `gpt-4o-mini-realtime-preview` model deployment.
 
 The following example is a well-constructed `/realtime` request URI:
 
 ```http
-wss://my-eastus2-openai-resource.openai.azure.com/openai/realtime?api-version=2024-10-01-preview&deployment=gpt-4o-realtime-preview-1001
+wss://my-eastus2-openai-resource.openai.azure.com/openai/realtime?api-version=2024-12-17&deployment=gpt-4o-realtime-preview
 ```
 
 ## Authentication
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオリファレンスの文書更新"
}
```

### Explanation
この変更は、Azure OpenAIのリアルタイムオーディオリファレンスに関する文書の更新を示しています。主な修正点は、WebSocketリクエストURIの構造に関する情報の明確化です。具体的には、リクエストURIの各構成要素の説明が改善され、最後にピリオド（.）を追加することで文書の読みやすさが向上しています。

加えて、APIバージョンが`2024-10-01-preview`から`2024-12-17`に更新され、新たに`gpt-4o-mini-realtime-preview`モデルのデプロイメントもサポートされることが記載されています。これにより、ユーザーは最新のAPIバージョンを基にリクエストURIを構築できるようになり、使用可能なモデルの選択肢が増えることで、利便性が向上します。全体的に、この変更は技術文書の正確性を高め、ユーザーに対してより明確なガイダンスを提供することを目的としています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -19,6 +19,18 @@ recommendations: false
 
 This article provides a summary of the latest releases and major documentation updates for Azure OpenAI Service.
 
+## February 2025
+
+### gpt-4o mini audio released
+
+The `gpt-4o-audio-preview` (2024-12-17) model is the latest audio completions model. Use the `gpt-4o-audio-preview` model for audio generation. For more information, see the [audio generation quickstart](./audio-completions-quickstart.md).
+
+The `gpt-4o-mini-realtime-preview` (2024-12-17) model is the latest real-time audio model. The real-time models use the same underlying GPT-4o audio model as the completions API, but is optimized for low-latency, real-time audio interactions. For more information, see the [real-time audio quickstart](./realtime-audio-quickstart.md).
+
+### GPT-4o audio completions
+
+The `gpt-4o-audio-preview` model is now available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability). Use the `gpt-4o-audio-preview` model for audio generation.
+
 ## January 2025
 
 ### o3-mini released
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新機能の追加: GPT-4o音声モデルのリリース"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関する「新着情報」文書に新たな内容を追加したものです。具体的には、2025年2月のリリース情報が追加され、`gpt-4o-mini-audio`および`gpt-4o-audio-preview`モデルに関する詳細が記載されています。

新しい音声生成モデル`gpt-4o-audio-preview`は、2024年12月17日にリリースされ、音声生成に最適化されています。さらに、リアルタイムオーディオモデルである`gpt-4o-mini-realtime-preview`も同日にリリースされ、このモデルは低遅延のリアルタイムオーディオインタラクションに対応しています。

この変更により、ユーザーは新しく導入された音声関連の機能やモデルについての情報を得られ、具体的な利用方法として関連するクイックスタートガイドへのリンクも提供されています。全体として、この文書の更新は、Azure OpenAIサービスにおける最新の機能とその利用可能性を示し、より良いユーザーエクスペリエンスを提供することを目的としています。


