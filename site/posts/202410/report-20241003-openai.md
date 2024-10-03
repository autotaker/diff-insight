---
date: '2024-10-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b0599a2...MicrosoftDocs:94dabc3
summary: このドキュメント更新では、Azure OpenAIに関連する文書が改訂され、新機能の追加と情報の改善が行われました。主な内容としては、新しいモデル「o1-preview」と「o1-mini」に関する詳細情報や、DALL-Eモデルの引退に関する情報、GPT-4oリアルタイムAPIの利用手順が含まれています。また、バッチ処理の仕様や規制関連の更新、目次の整理、Whisperモデルの情報削除も行われました。新モデルの追加により、ユーザーの選択肢が広がり、APIパラメータの変更も行われているため、ユーザーはより詳細な設定が可能になっています。全体として、Azure
  OpenAIサービスの利用範囲が拡大し、最新の情報を確保する重要性が強調されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b0599a2...MicrosoftDocs:94dabc3){target="_blank"}

# ハイライト

このドキュメント更新には、複数のAzure OpenAI関連の文書が新機能の追加と情報の改善を含んでいます。特に、新しいモデルやAPIの利用に関する詳細な情報が追加され、ユーザーの理解を助けることが目的です。
- 新モデル「o1-preview」と「o1-mini」の詳細な情報
- DALL-Eモデルの引退に関する日付と推奨される代替品
- GPT-4oリアルタイムAPIとその利用手順
- バッチ処理の仕様更新
- 規制に関連する更新
- 目次（TOC）の整理
- Whisperモデルの情報削除

## 新機能
- 新たに、モデル「o1-preview」と「o1-mini」がAzure OpenAIモデルのリストに追加されました。これにより、ユーザーは幅広いモデルの選択肢を得ることができます。
- GPT-4oのリアルタイムAPIに新しい使用手順が追加され、音声入力と出力のアプリケーションを構築するためのヒントとなります。
- API利用におけるパラメータの更新が行われました。`max_tokens`が非推奨となり、新しい`max_completion_tokens`パラメータが導入されています。
- 新モデルを使用する際のレート制限が詳細に説明されています。特にエンタープライズおよびデフォルトティアでの利用に関してです。

## 破壊的変更
- Whisperモデルの限定アクセスに関する情報削除が行われました。この変更により、モデルの現在の状態についての情報が不足している可能性があります。
- 目次において、一部項目が削除され、ユーザーが情報にアクセスしにくくなる可能性があります。

## その他アップデート
- Azure OpenAIサービスにおけるREST APIアクセスおよびフィーチャーセクションの更新
- コンテンツフィルタリング関連の文書において、フィルタ設定に関する情報の更新
- モデルの引退とその代替品について詳細に述べられた情報
- さまざまな文書において、表の形式や内容が整理・更新されています。

# インサイト

これらの変更はAzure OpenAIサービスの最新アップデートを反映するためのものです。特に、新しいモデル「o1-preview」と「o1-mini」の追加により、このサービスが提供する機能の幅が広がりました。これらのモデルは特定の推論タスクに特化しており、それらを効果的に利用するための情報を整然と提供しています。また、APIパラメータの変更は、より細かい設定や制限をユーザーが管理できるようにするために行われています。このような細かな設定をサポートすることは、将来のスケーラビリティとユーザー適応力の向上に寄与するでしょう。

目次の整理は、情報へのアクセスをスムーズにするための取り組みです。削除された情報もありますが、これは予告なく情報にアクセスできなくなるリスクを伴うため、利用者に最新の情報を提供し続けるためのアップデートが重要です。特に、Whisperモデルに関する利用条件の情報が削除されたことに注意が必要です。現場でこれを利用するユーザーは、最新のドキュメントを参照し、モデルやサービスの利用に何らかの新しい制限や更新がないかを確認することが推奨されます。

全体として、このドキュメント更新はAzure OpenAIサービスの利用範囲を拡大し、利用者がより豊富な選択肢を持つことを促進します。それにより、技術的な進展や改善がある一方で、利用者が正確で最新の情報を得る手段の確保がより重要になることが窺えます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [content-filter.md](#item-dfc7e7) | minor update | コンテンツフィルタリングに関するドキュメントの更新 | modified | 1 | 3 | 4 | 
| [model-retirements.md](#item-03fc2e) | minor update | モデルの廃止と引退に関する情報の更新 | modified | 4 | 1 | 5 | 
| [models.md](#item-db2c37) | minor update | Azure OpenAIモデルに関する情報の更新 | modified | 20 | 8 | 28 | 
| [audio-real-time.md](#item-bd52a6) | minor update | GPT-4oリアルタイムAPIに関する情報の更新 | modified | 24 | 15 | 39 | 
| [batch.md](#item-a131d5) | minor update | バッチ処理に関する情報の更新 | modified | 11 | 9 | 20 | 
| [content-filter-configurability.md](#item-11f064) | minor update | コンテンツフィルタの設定可能性に関する情報の更新 | modified | 5 | 2 | 7 | 
| [overview.md](#item-97d507) | minor update | Azure OpenAIサービスに関する情報の更新 | modified | 3 | 3 | 6 | 
| [quotas-limits.md](#item-06c6f9) | minor update | o1-previewおよびo1-miniモデルのレート制限の追加 | modified | 20 | 0 | 20 | 
| [toc.yml](#item-c945af) | minor update | 目次の更新 - リアルタイムAPIに関する項目の変更 | modified | 2 | 2 | 4 | 
| [whats-new.md](#item-53303b) | minor update | 新機能およびAPI更新の追加 | modified | 44 | 22 | 66 | 
| [whisper-quickstart.md](#item-4cae3d) | minor update | Whisperクイックスタートの情報更新 | modified | 0 | 3 | 3 | 


# Modified Contents
## articles/ai-services/openai/concepts/content-filter.md{#item-dfc7e7}

<details>
<summary>Diff</summary>
````diff
@@ -83,8 +83,6 @@ Detecting indirect attacks requires using document delimiters when constructing
 
 [!INCLUDE [content-filter-configurability](../includes/content-filter-configurability.md)]
 
-
-
 ## Scenario details
 
 When the content filtering system detects harmful content, you receive either an error on the API call if the prompt was deemed inappropriate, or the `finish_reason` on the response will be `content_filter` to signify that some of the completion was filtered. When building your application or system, you'll want to account for these scenarios where the content returned by the Completions API is filtered, which might result in content that is incomplete. How you act on this information will be application specific. The behavior can be summarized in the following points:
@@ -1012,4 +1010,4 @@ As part of your application design, consider the following best practices to del
 - Apply for modified content filters via [this form](https://ncv.microsoft.com/uEfCgnITdR).
 - Azure OpenAI content filtering is powered by [Azure AI Content Safety](https://azure.microsoft.com/products/cognitive-services/ai-content-safety).
 - Learn more about understanding and mitigating risks associated with your application: [Overview of Responsible AI practices for Azure OpenAI models](/legal/cognitive-services/openai/overview?context=/azure/ai-services/openai/context/context).
-- Learn more about how data is processed in connection with content filtering and abuse monitoring: [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy?context=/azure/ai-services/openai/context/context#preventing-abuse-and-harmful-content-generation).
+- Learn more about how data is processed in connection with content filtering and abuse monitoring: [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy?context=/azure/ai-services/openai/context/context#preventing-abuse-and-harmful-content-generation).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングに関するドキュメントの更新"
}
```

### Explanation
このコードの変更では、`content-filter.md`ファイルに対する小規模な更新が行われました。具体的には、いくつかの行が削除され、1行が追加されました。削除された内容には、コンテンツフィルタリングのシナリオに関する詳細が含まれており、現在の情報に合わせて内容が整理されています。新しい情報は、適切なリンクを通じてユーザーに追加のリソースを提供することで、コンテンツフィルタリングシステムの利用についての理解を深めようとしています。この変更は、ユーザーがAzure OpenAIのコンテンツフィルタリングの使用において重要な知識を得られるようにすることを意図しています。

## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 09/26/2024
+ms.date: 10/02/2024
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -91,6 +91,8 @@ These models are currently available for use in Azure OpenAI Service.
 
 | Model | Version | Retirement date | Suggested replacements |
 | ---- | ---- | ---- | --- |
+| `dall-e-2`| 2 | January 27, 2025 | `dalle-3` |
+| `dall-e-3` | 3 | No earlier than April 30, 2025 | |
 | `gpt-35-turbo` | 0301 | January 27, 2025<br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024.   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
 | `gpt-35-turbo`<br>`gpt-35-turbo-16k` | 0613 | January 27, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024.  | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
 | `gpt-35-turbo` | 1106 | No earlier than January 27, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
@@ -100,6 +102,7 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-4` | 1106-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025 **<sup>1</sup>** | `gpt-4o`|
 | `gpt-4` | 0125-preview |To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025 **<sup>1</sup>**  | `gpt-4o` |
 | `gpt-4` | vision-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025  **<sup>1</sup>** | `gpt-4o`|
+| `gpt-4o` | 2024-05-13 | No earlier than March 20, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on December 5, 2024. | |
 | `gpt-3.5-turbo-instruct` | 0914 | No earlier than Sep 14, 2025 |  |
 | `text-embedding-ada-002` | 2 | No earlier than April 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
 | `text-embedding-ada-002` | 1 | No earlier than April 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの廃止と引退に関する情報の更新"
}
```

### Explanation
この変更では、`model-retirements.md`ファイルに関するいくつかの重要な更新が実施されました。新しいモデル、`dall-e-2`および`dall-e-3`のリタイアメント日および推奨される代替品に関する情報が追加されました。具体的には、`dall-e-2`は2025年1月27日にリタイアし、`dall-e-3`は2025年4月30日以降に使用可能になることが示されています。また、一部のモデルのリタイアメント日が更新され、該当するリンクが含まれており、自動アップデート機能に関する具体的な情報も提供されています。このドキュメントの改訂は、ユーザーに対して最新のモデルの利用状況と今後の変更についての明確なガイダンスを提供することを目的としています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 09/30/2024
+ms.date: 10/01/2024
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -18,6 +18,7 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 
 | Models | Description |
 |--|--|
+| [o1-preview and o1-mini](#o1-preview-and-o1-mini-models-limited-access) | Limited access models, specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability.  |
 | [GPT-4o & GPT-4o mini & GPT-4 Turbo](#gpt-4o-and-gpt-4-turbo) | The latest most capable Azure OpenAI models with multimodal versions, which can accept both text and images as input. |
 | [GPT-4o audio](#gpt-4o-audio) | A GPT-4o model that supports low-latency, "speech in, speech out" conversational interactions. |
 | [GPT-4](#gpt-4) | A set of models that improve on GPT-3.5 and can understand and generate natural language and code. |
@@ -31,18 +32,28 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 
 The Azure OpenAI `o1-preview` and `o1-mini` models are specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
 
-### Availability
+|  Model ID  | Description | Max Request (tokens) | Training Data (up to)  |
+|  --- |  :--- |:--- |:---: |
+|`o1-preview` (2024-09-12) | The most capable model in the o1 series, offering enhanced reasoning abilities.| Input: 128,000  <br> Output: 32,768 | Oct 2023 |
+| `o1-mini` (2024-09-12) | A faster and more cost-efficient option in the o1 series, ideal for coding tasks requiring speed and lower resource consumption.| Input: 128,000  <br> Output: 65,536 | Oct 2023 |
 
-The `o1-preview` and `o1-mini` models are available in the East US2 region for limited access through the [AI Studio](https://ai.azure.com) early access playground. Data processing for the `o1` models may occur in a different region than where they are available for use.
+### Availability
 
-To try the `o1-preview` and `o1-mini` models in the early access playground, **registration is required, and access will be granted based on Microsoft’s eligibility criteria**.
+The `o1-preview` and `o1-mini` models are now available for API access and model deployment. **Registration is required, and access will be granted based on Microsoft's eligibility criteria**.
 
 Request access: [limited access model application](https://aka.ms/oai/modelaccess)
 
-Once access has been granted, you will need to:
+Once access has been granted, you will need to create a deployment for each model.
+
+### API support
+
+Support for the **o1 series** models was added in API version `2024-09-01-preview`.
+
+The `max_tokens` parameter has been deprecated and replaced with the new `max_completion_tokens` parameter. **o1 series** models will only work with the `max_completions_tokens` parameter. 
+
+### Region availability
 
-1. Navigate to https://ai.azure.com/resources and select a resource in the `eastus2` region. If you do not have an Azure OpenAI resource in this region you will need to [create one](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI).  
-2. Once the `eastus2` Azure OpenAI resource is selected, in the upper left-hand panel under **Playgrounds** select **Early access playground (preview)**.
+Available for standard and global standard deployment in East US2 and Sweden Central for approved customers.
 
 ## GPT-4o audio
 
@@ -289,6 +300,7 @@ The following models support global batch:
 
 | Model | Version | Input format |
 |---|---|---|
+|`gpt-4o` | 2024-08-06 |text + image |
 |`gpt-4o-mini`| 2024-07-18 | text + image |
 |`gpt-4o` | 2024-05-13 |text + image |
 |`gpt-4` | turbo-2024-04-09 | text |
@@ -421,4 +433,4 @@ For the latest information on model retirements, refer to the [model retirement
 - [Model retirement and deprecation](./model-retirements.md)
 - [Learn more about working with Azure OpenAI models](../how-to/working-with-models.md)
 - [Learn more about Azure OpenAI](../overview.md)
-- [Learn more about fine-tuning Azure OpenAI models](../how-to/fine-tuning.md)
+- [Learn more about fine-tuning Azure OpenAI models](../how-to/fine-tuning.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIモデルに関する情報の更新"
}
```

### Explanation
この変更では、`models.md`ファイルにおけるAzure OpenAIモデルに関する情報が大幅に更新されました。主な改訂内容には、新しいモデル`o1-preview`および`o1-mini`に関する詳細が追加され、これらのモデルが推論および問題解決タスクに特化していることが強調されています。また、各モデルの利用可能性、最大リクエストトークン数、トレーニングデータの更新が新しいテーブル形式で整理されました。

さらに、`o1-preview`と`o1-mini`モデルがAPIアクセスおよびモデルデプロイメントに対応することが明記され、アクセスには登録が必要である旨が強調されています。APIサポートに関する情報も追加されており、`max_tokens`パラメータが廃止され、新しい`max_completion_tokens`パラメータが導入されたことが説明されています。このドキュメントの改訂は、ユーザーがAzure OpenAIの最新の利用可能なモデルとその特性に対して理解を深めるための重要なリソースを提供することを目的としています。

## articles/ai-services/openai/how-to/audio-real-time.md{#item-bd52a6}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: 'How to use GPT-4o real-time audio with Azure OpenAI Service'
+title: 'How to use GPT-4o Realtime API for speech and audio with Azure OpenAI Service'
 titleSuffix: Azure OpenAI
-description: Learn how to use GPT-4o real-time audio with Azure OpenAI Service.
+description: Learn how to use GPT-4o Realtime API for speech and audio with Azure OpenAI Service.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
@@ -12,11 +12,11 @@ ms.custom: references_regions
 recommendations: false
 ---
 
-# GPT-4o real-time audio
+# GPT-4o Realtime API for speech and audio (Preview)
 
-Azure OpenAI GPT-4o audio is part of the GPT-4o model family that supports low-latency, "speech in, speech out" conversational interactions. The GPT-4o audio `realtime` API is designed to handle real-time, low-latency conversational interactions, making it a great fit for use cases involving live interactions between a user and a model, such as customer support agents, voice assistants, and real-time translators.
+Azure OpenAI GPT-4o Realtime API for speech and audio is part of the GPT-4o model family that supports low-latency, "speech in, speech out" conversational interactions. The GPT-4o audio `realtime` API is designed to handle real-time, low-latency conversational interactions, making it a great fit for use cases involving live interactions between a user and a model, such as customer support agents, voice assistants, and real-time translators.
 
-Most users of this API need to deliver and receive audio from an end-user in real time, including applications that use WebRTC or a telephony system. The real-time API isn't designed to connect directly to end user devices and relies on client integrations to terminate end user audio streams. 
+Most users of the Realtime API need to deliver and receive audio from an end-user in real time, including applications that use WebRTC or a telephony system. The Realtime API isn't designed to connect directly to end user devices and relies on client integrations to terminate end user audio streams. 
 
 ## Supported models
 
@@ -29,7 +29,7 @@ The `gpt-4o-realtime-preview` model is available for global deployments in [East
 
 ## API support
 
-Support for real-time audio was first added in API version `2024-10-01-preview`. 
+Support for the Realtime API was first added in API version `2024-10-01-preview`. 
 
 > [!NOTE]
 > For more information about the API and architecture, see the [Azure OpenAI GPT-4o real-time audio repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk).
@@ -43,7 +43,7 @@ Support for real-time audio was first added in API version `2024-10-01-preview`.
 
 Before you can use GPT-4o real-time audio, you need a deployment of the `gpt-4o-realtime-preview` model in a supported region as described in the [supported models](#supported-models) section.
 
-You can deploy the model from the Azure OpenAI model catalog or from your project in AI Studio. Follow these steps to deploy a `gpt-4o-realtime-preview` model from the [AI Studio model catalog](../../../ai-studio/how-to/model-catalog-overview.md):
+You can deploy the model from the [Azure AI Studio model catalog](../../../ai-studio/how-to/model-catalog-overview.md) or from your project in AI Studio. Follow these steps to deploy a `gpt-4o-realtime-preview` model from the model catalog:
 
 1. Sign in to [AI Studio](https://ai.azure.com) and go to the **Home** page.
 1. Select **Model catalog** from the left sidebar.
@@ -54,17 +54,20 @@ You can deploy the model from the Azure OpenAI model catalog or from your projec
 1. Modify other default settings depending on your requirements.
 1. Select **Deploy**. You land on the deployment details page. 
 
-Now that you have a deployment of the `gpt-4o-realtime-preview` model, you can use the playground to interact with the model in real time. Select **Early access playground** from the list of playgrounds in the left pane.
+Now that you have a deployment of the `gpt-4o-realtime-preview` model, you can use the Realtime API to interact with it in real time.
 
-## Use the GPT-4o real-time audio API
+## Use the GPT-4o Realtime API
 
 > [!TIP]
 > A playground for GPT-4o real-time audio is coming soon to [Azure AI Studio](https://ai.azure.com). You can already use the API directly in your application.
 
-Right now, the fastest way to get started with GPT-4o real-time audio is to download the sample code from the [Azure OpenAI GPT-4o real-time audio repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk).
+Right now, the fastest way to get started with the GPT-4o Realtime API is to download the sample code from the [Azure OpenAI GPT-4o real-time audio repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk).
+
+The JavaScript web sample demonstrates how to use the GPT-4o Realtime API to interact with the model in real time. The sample code includes a simple web interface that captures audio from the user's microphone and sends it to the model for processing. The model responds with text and audio, which the sample code renders in the web interface.
+
+You can run the sample code locally on your machine by following these steps. Refer to the [repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk) for the most up-to-date instructions.
+1. If you don't have Node.js installed, download and install the [LTS version of Node.js](https://nodejs.org/).
 
-The JavaScript web sample demonstrates how to use the GPT-4o real-time audio API to interact with the model in real time. The sample code includes a simple web interface that captures audio from the user's microphone and sends it to the model for processing. The model responds with text and audio, which the sample code renders in the web interface.
- 
 1. Clone the repository to your local machine:
     
     ```bash
@@ -74,12 +77,18 @@ The JavaScript web sample demonstrates how to use the GPT-4o real-time audio API
 1. Go to the `javascript/samples/web` folder in your preferred code editor.
 
     ```bash
-    cd .\javascript\samples\web\
+    cd ./javascript/samples
     ```
 
-1. If you don't have Node.js installed, download and install the [LTS version of Node.js](https://nodejs.org/).
+1. Run `download-pkg.ps1` or `download-pkg.sh` to download the required packages. 
+
+1. Go to the `web` folder from the `./javascript/samples` folder.
+
+    ```bash
+    cd ./web
+    ```
 
-1. Run `npm install` to download a few dependency packages. For more information, see the `package.json` file in the same `web` folder.
+1. Run `npm install` to install package dependencies.
 
 1. Run `npm run dev` to start the web server, navigating any firewall permissions prompts as needed.
 1. Go to any of the provided URIs from the console output (such as `http://localhost:5173/`) in a browser.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4oリアルタイムAPIに関する情報の更新"
}
```

### Explanation
この変更では、`audio-real-time.md`ファイルにおけるGPT-4oリアルタイムAPIに関する情報が更新されました。主な改訂ポイントとして、タイトルと説明が変更され、APIの機能が明確に強調されています。また、リアルタイムAPIの概要が特定のユースケースに特化して再構成されています。

新たに、リアルタイムAPIの使用法を示す手順が整理され、モデルのデプロイ方法やサンプルコードの取得方法についての詳細が追加されました。具体的には、サンプルコードがローカルでの実行方法が説明され、Node.jsのインストール方法や依存関係の設定方法が詳述されています。この改訂は、ユーザーがGPT-4oリアルタイムAPIを活用して、音声入力と音声出力を行うアプリケーションを構築する際の理解を向上させるために策定されています。

## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: 
 ms.topic: how-to
-ms.date: 09/04/2024
+ms.date: 10/02/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -50,15 +50,17 @@ Global batch is currently supported in the following regions:
 
 The following models support global batch:
 
-| Model | Version | Supported |
+| Model | Version | Input format |
 |---|---|---|
-|`gpt-4o` | 2024-05-13 |Yes (text + vision) |
-|`gpt-4o-mini` | 2024-07-18  | Yes (text + vision) |
-|`gpt-4` | turbo-2024-04-09 | Yes (text only) |
-|`gpt-4` | 0613 | Yes |
-| `gpt-35-turbo` | 0125 | Yes |
-| `gpt-35-turbo` | 1106 | Yes |
-| `gpt-35-turbo` | 0613 | Yes |
+|`gpt-4o` | 2024-08-06 |text + image |
+|`gpt-4o-mini`| 2024-07-18 | text + image |
+|`gpt-4o` | 2024-05-13 |text + image |
+|`gpt-4` | turbo-2024-04-09 | text |
+|`gpt-4` | 0613 | text |
+| `gpt-35-turbo` | 0125 | text |
+| `gpt-35-turbo` | 1106 | text |
+| `gpt-35-turbo` | 0613 | text |
+
 
 
 Refer to the [models page](../concepts/models.md) for the most up-to-date information on regions/models where global batch is currently supported.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理に関する情報の更新"
}
```

### Explanation
この変更では、`batch.md`ファイルにおけるバッチ処理に関する内容が更新されました。主な変更点として、バージョン情報やサポートされる入力フォーマットに関する表の形式が改善され、各モデルの対応する入力形式（テキストや画像）についての明示が追加されました。

具体的には、`gpt-4o`および`gpt-4o-mini`モデルが新しいバージョンで更新され、これらのモデルがテキストと画像の両方を支持することが記載されています。また、ドキュメントの日付も更新されており、最新の情報が反映されています。この改訂は、ユーザーがグローバルバッチサポートを利用する際に、どのモデルがどの入力フォーマットをサポートしているかを把握しやすくすることを目的としています。

## articles/ai-services/openai/includes/content-filter-configurability.md{#item-11f064}

<details>
<summary>Diff</summary>
````diff
@@ -24,16 +24,19 @@ All customers can also configure content filters and create custom safety polici
 | No filters | If approved<sup>1</sup>| If approved<sup>1</sup>| No content is filtered regardless of severity level detected. Requires approval<sup>1</sup>.|
 |Annotate only | If approved<sup>1</sup>| If approved<sup>1</sup>| Disables the filter functionality, so content will not be blocked, but annotations are returned via API response. Requires approval<sup>1</sup>.|
 
-<sup>1</sup> For Azure OpenAI models, only customers who have been approved for modified content filtering have full content filtering control and can turn off content filters. Apply for modified content filters via this form: [Azure OpenAI Limited Access Review: Modified Content Filters](https://ncv.microsoft.com/uEfCgnITdR) For Azure Government customers, apply for modified content filters via this form: [Azure Government - Request Modified Content Filtering for Azure OpenAI Service](https://aka.ms/AOAIGovModifyContentFilter).
+<sup>1</sup> For Azure OpenAI models, only customers who have been approved for modified content filtering have full content filtering control and can turn off content filters. Apply for modified content filters via this form: [Azure OpenAI Limited Access Review: Modified Content Filters](https://ncv.microsoft.com/uEfCgnITdR). For Azure Government customers, apply for modified content filters via this form: [Azure Government - Request Modified Content Filtering for Azure OpenAI Service](https://aka.ms/AOAIGovModifyContentFilter).
 
 Configurable content filters for inputs (prompts) and outputs (completions) are available for the following Azure OpenAI models:
-
 * GPT model series
 * GPT-4 Turbo Vision GA<sup>*</sup> (`turbo-2024-04-09`)
 * GPT-4o
 * GPT-4o mini
 * DALL-E 2 and 3
 
+Configurable content filters are not available for 
+- o1-preview
+- o1-mini 
+
 <sup>*</sup>Only available for GPT-4 Turbo Vision GA, does not apply to GPT-4 Turbo Vision preview 
 
 Content filtering configurations are created within a Resource in Azure AI Studio, and can be associated with Deployments. [Learn more about configurability here](../how-to/content-filters.md).  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタの設定可能性に関する情報の更新"
}
```

### Explanation
この変更では、`content-filter-configurability.md`ファイルにおけるコンテンツフィルタの設定可能性に関する情報が更新されました。主な変更点は、特定のフィルタ設定に関する説明の明確化と、フィルタが適用されるモデルのリストに関する情報が追加されたことです。

具体的には、コンテンツフィルタの選択肢に関する詳細が更新され、Azure OpenAIモデルにおける承認条件と、カスタマイズされたコンテンツフィルタを利用するための申請方法が再確認されました。また、設定可能なコンテンツフィルタをサポートするモデルのリストに、`o1-preview`および`o1-mini`モデルが設定可能でないことが追加されました。この改訂は、ユーザーが利用可能なフィルタ設定についての理解を深め、適切なモデルを選択するための助けとなることを目的としています。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -14,13 +14,13 @@ recommendations: false
 
 # What is Azure OpenAI Service?
 
-Azure OpenAI Service provides REST API access to OpenAI's powerful language models including GPT-4o, GPT-4o mini, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, image understanding, semantic search, and natural language to code translation. Users can access the service through REST APIs, Python SDK, or our web-based interface in the Azure OpenAI Studio.
+Azure OpenAI Service provides REST API access to OpenAI's powerful language models including o1-preview, o1-mini, GPT-4o, GPT-4o mini, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, image understanding, semantic search, and natural language to code translation. Users can access the service through REST APIs, Python SDK, or our web-based interface in the Azure OpenAI Studio.
 
 ### Features overview
 
 | Feature | Azure OpenAI |
 | --- | --- |
-| Models available | **GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
+| Models available | **o1-preview** & **o1-mini** - (Limited Access - [Request Access](https://aka.ms/oai/modelaccess))<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
 | Fine-tuning | `GPT-4o-mini` (preview) <br> `GPT-4` (preview) <br>`GPT-3.5-Turbo` (0613) <br> `babbage-002` <br> `davinci-002`.|
 | Price | [Available here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> For details on GPT-4 Turbo with Vision, see the [special pricing information](../openai/concepts/gpt-with-vision.md#special-pricing-information).|
 | Virtual network support & private link support | Yes, unless using [Azure OpenAI on your data](./concepts/use-your-data.md).  |
@@ -125,4 +125,4 @@ Learn more about each model on our [models concept page](./concepts/models.md).
 
 ## Next steps
 
-Learn more about the [underlying models that power Azure OpenAI](./concepts/models.md).
+Learn more about the [underlying models that power Azure OpenAI](./concepts/models.md).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスに関する情報の更新"
}
```

### Explanation
この変更では、`overview.md`ファイルにおけるAzure OpenAIサービスに関する情報が更新されました。主な変更点は、利用可能なモデルのリストに`o1-preview`と`o1-mini`が追加されたことです。これにより、ユーザーが利用できるモデルの選択肢が広がりました。

具体的には、Azure OpenAIサービスが提供するREST APIアクセスに関する記述が更新され、新たに対象となるモデルが指定されています。また、フィーチャーの概要セクションでも、`o1-preview`および`o1-mini`が「限定アクセス」として明記され、アクセスリクエストのリンクも追加されています。この改訂は、Azure OpenAIサービスを利用するユーザーが最新のモデル情報を基にサービスを選択しやすくすることを目的としています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -60,6 +60,26 @@ The following sections provide you with a quick guide to the default quotas and
 
 [!INCLUDE [Quota](./includes/global-batch-limits.md)]
 
+## o1-preview & o1-mini rate limits
+
+### o1-preview & o1-mini global standard
+
+| Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
+|---|---|:---:|:---:|
+| `o1-preview` | Enterprise agreement | 15 M | 2.5 K |
+| `o1-mini`| Enterprise agreement | 50 M | 5 K |
+| `o1-preview` | Default | 1.5 M | 250 |
+| `o1-mini`| Default | 1 M | 100 |
+
+### o1-preview & o1-mini standard
+
+| Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
+|---|---|:---:|:---:|
+| `o1-preview` | Enterprise agreement | 600 K | 100 |
+| `o1-mini`| Enterprise agreement |  1 M | 100 |
+| `o1-preview` | Default | 300 K | 50 |
+| `o1-mini`| Default | 500 K | 50 |
+
 ## gpt-4o & GPT-4 Turbo rate limits
 
 `gpt-4o` and `gpt-4o-mini`, and `gpt-4` (`turbo-2024-04-09`) have rate limit tiers with higher limits for certain customer types.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "o1-previewおよびo1-miniモデルのレート制限の追加"
}
```

### Explanation
この変更では、`quotas-limits.md`ファイルにおいて、`o1-preview`および`o1-mini`モデルに関するレート制限の情報が追加されました。具体的には、これらのモデルが異なるティアにおけるトークンあたりの制限とリクエストの制限が詳述されています。

新たに追加されたセクションでは、エンタープライズ契約とデフォルトティアのそれぞれについて、各モデルの分単位でのトークン制限（TPM）とリクエスト数が表形式で示されています。この情報は、ユーザーが`o1-preview`および`o1-mini`モデルを利用する際のパフォーマンス予測と計画に役立つものであり、リソースの管理において重要なデータを提供しています。これにより、ユーザーは各モデルの利用可能性と制限を理解し、適切に使い分けることが可能となることを目指しています。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -111,8 +111,6 @@ items:
           href: ./how-to/assistants-logic-apps.md
       - name: File search
         href: ./how-to/file-search.md
-  - name: Audio in real time
-    href: ./how-to/audio-real-time.md
   - name: Batch
     href: ./how-to/batch.md
   - name: Completions & chat completions
@@ -164,6 +162,8 @@ items:
       - name: Function calling
         href: ./how-to/fine-tuning-functions.md
         displayName: fine-tuning, finetuning
+  - name: Realtime API for speech and audio (Preview)
+    href: ./how-to/audio-real-time.md
   - name: Use your data
     items:
       - name: Text data
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新 - リアルタイムAPIに関する項目の変更"
}
```

### Explanation
この変更では、`toc.yml`ファイルにおいて、目次の項目が更新されました。具体的には、リアルタイム音声およびオーディオに関する項目が削除され、代わりに「Realtime API for speech and audio (Preview)」という新しい項目が追加されています。

元々の「Audio in real time」という項目が削除された後、関連するリアルタイムAPIの情報が新たに組み込まれる形となっています。この変更により、ユーザーは最新の情報や機能にアクセスしやすくなり、特にプレビュー版のリアルタイムAPIに関心がある場合に重要な情報が目次から容易に見つけられるようになります。この更新は、ドキュメントの navigational structureを改善し、利用者が必要な情報を迅速に取得できることを目指しています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: whats-new
-ms.date: 9/19/2024
+ms.date: 10/01/2024
 recommendations: false
 ---
 
@@ -20,14 +20,36 @@ This article provides a summary of the latest releases and major documentation u
 
 ## October 2024
 
-### New GPT-4o real-time audio public preview
+### o1-preview and o1-mini models limited access
+
+The `o1-preview` and `o1-mini` models are now available for API access and model deployment. **Registration is required, and access will be granted based on Microsoft's eligibility criteria**.
+
+Request access: [limited access model application](https://aka.ms/oai/modelaccess)
+
+Customers who were already approved and have access to the model through the early access playground don't need to apply again, you'll automatically be granted API access. Once access has been granted, you'll need to create a deployment for each model.
+
+**API support:**
+
+Support for the **o1 series** models was added in API version `2024-09-01-preview`.
+
+The `max_tokens` parameter has been deprecated and replaced with the new `max_completion_tokens` parameter. **o1 series** models will only work with the `max_completions_tokens` parameter.
+
+**Region availability**:
+
+Models are available for standard and global standard deployment in East US2 and Sweden Central for approved customers.
+
+### New GPT-4o Realtime API for speech and audio public preview
 
 Azure OpenAI GPT-4o audio is part of the GPT-4o model family that supports low-latency, "speech in, speech out" conversational interactions. The GPT-4o audio `realtime` API is designed to handle real-time, low-latency conversational interactions, making it a great fit for use cases involving live interactions between a user and a model, such as customer support agents, voice assistants, and real-time translators.
 
 The `gpt-4o-realtime-preview` model is available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability).
 
 For more information, see the [GPT-4o real-time audio documentation](./how-to/audio-real-time.md).
 
+### Global batch support updates
+
+Global batch now supports GPT-4o (2024-08-06). See the [global batch getting started guide](./how-to/batch.md) for more information.
+
 ## September 2024
 
 ### Azure OpenAI Studio UX updates
@@ -36,7 +58,7 @@ On September 19, when you access the [Azure OpenAI Studio](https://oai.azure.com
 
 
 ### GPT-4o 2024-08-06 provisioned deployments
-GPT-4o 2024-08-06 is now available for provisioned deployments in East US, East US 2, North Central US, and Sweden Central. It is also available for global provisioned deployments.
+GPT-4o 2024-08-06 is now available for provisioned deployments in East US, East US 2, North Central US, and Sweden Central. It's also available for global provisioned deployments.
 
 For the latest information on model availability, see the [models page](/azure/ai-services/openai/concepts/models#provisioned-deployment-model-availability).
 
@@ -47,7 +69,7 @@ For more information, see the [deployment types guide](https://aka.ms/aoai/docs/
 
 ### NEW o1-preview and o1-mini models available for limited access
 
-The Azure OpenAI `o1-preview` and `o1-mini` models are specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
+The Azure OpenAI `o1-preview` and `o1-mini` models are designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
 
 ### Key capabilities of the o1 series
 
@@ -67,23 +89,23 @@ Request access: [limited access model application](https://aka.ms/oai/modelacces
 
 ### Limitations
 
-The `o1` series models are currently in preview and do not include some features available in other models, such as image understanding and structured outputs which are available in the latest GPT-4o model. For many tasks, the generally available GPT-4o models may still be more suitable.
+The `o1` series models are currently in preview and don't include some features available in other models, such as image understanding and structured outputs which are available in the latest GPT-4o model. For many tasks, the generally available GPT-4o models might still be more suitable.
 
 ### Safety
 
 OpenAI has incorporated additional safety measures into the `o1` models, including new techniques to help the models refuse unsafe requests. These advancements make the `o1` series some of the most robust models available.
 
 ### Availability
 
-The `o1-preview` and `o1-mini` are available in the East US2 region for limited access through the [AI Studio](https://ai.azure.com) early access playground. Data processing for the `o1` models may occur in a different region than where they are available for use.
+The `o1-preview` and `o1-mini` are available in the East US2 region for limited access through the [AI Studio](https://ai.azure.com) early access playground. Data processing for the `o1` models might occur in a different region than where they are available for use.
 
 To try the `o1-preview` and `o1-mini` models in the early access playground **registration is required, and access will be granted based on Microsoft’s eligibility criteria.**
 
 Request access: [limited access model application](https://aka.ms/oai/modelaccess)
 
 Once access has been granted, you will need to:
 
-1. Navigate to https://ai.azure.com/resources and select a resource in the `eastus2` region. If you do not have an Azure OpenAI resource in this region you will need to [create one](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI).  
+1. Navigate to https://ai.azure.com/resources and select a resource in the `eastus2` region. If you don't have an Azure OpenAI resource in this region you'll need to [create one](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI).  
 2. Once the `eastus2` Azure OpenAI resource is selected, in the upper left-hand panel under **Playgrounds** select **Early access playground (preview)**.
  
 ## August 2024
@@ -133,10 +155,10 @@ On August 6, 2024, OpenAI [announced](https://openai.com/index/introducing-struc
 
 Azure customers can test out GPT-4o `2024-08-06` today in the new AI Studio early access playground (preview).
 
-Unlike the previous early access playground, the AI Studio early access playground (preview) does not require you to have a resource in a specific region.
+Unlike the previous early access playground, the AI Studio early access playground (preview) doesn't require you to have a resource in a specific region.
 
 > [!NOTE]
-> Prompts and completions made through the early access playground (preview) may be processed in any Azure OpenAI region, and are currently subject to a 10 request per minute per Azure subscription limit. This limit may change in the future.
+> Prompts and completions made through the early access playground (preview) might be processed in any Azure OpenAI region, and are currently subject to a 10 request per minute per Azure subscription limit. This limit might change in the future.
 >
 > Azure OpenAI Service abuse monitoring is enabled for all early access playground users even if approved for modification; default content filters are enabled and cannot be modified.
 
@@ -265,7 +287,7 @@ Threads and Files in Assistants now supports CMK in the following region:
 ### GPT-4o provisioned deployments
 
 `gpt-4o` Version: `2024-05-13` is available for both standard and provisioned deployments. Provisioned and standard model deployments accept both text and image/vision inference requests.
-For information on model regional availability consult the model matrix for [provisioned deployments](./concepts/models.md#provisioned-deployment-model-availability).
+For information on model regional availability, consult the model matrix for [provisioned deployments](./concepts/models.md#provisioned-deployment-model-availability).
 
 ### Assistants v2 (preview)
 
@@ -302,7 +324,7 @@ For information on model regional availability, see the [models page](./concepts
 
 ### Global standard deployment type (preview)
 
-Global deployments are available in the same Azure OpenAI resources as non-global offers but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center with best availability for each request. Global standard will provide the highest default quota for new models and eliminates the need to load balance across multiple resources.
+Global deployments are available in the same Azure OpenAI resources as non-global offers but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center with best availability for each request. Global standard provides the highest default quota for new models and eliminates the need to load balance across multiple resources.
 
 For more information, see the [deployment types guide](https://aka.ms/aoai/docs/deployment-types).
 
@@ -321,7 +343,7 @@ Running filters asynchronously for improved latency in streaming scenarios is no
 
 ### Prompt Shields
 
-Prompt Shields protect applications powered by Azure OpenAI models from two types of attacks: direct (jailbreak) and indirect attacks. Indirect Attacks (also known as Indirect Prompt Attacks or Cross-Domain Prompt Injection Attacks) are a type of attack on systems powered by Generative AI models that may occur when an application processes information that wasn’t directly authored by either the developer of the application or the user. [Content filtering](/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cpython-new#prompt-shields)
+Prompt Shields protect applications powered by Azure OpenAI models from two types of attacks: direct (jailbreak) and indirect attacks. Indirect Attacks (also known as Indirect Prompt Attacks or Cross-Domain Prompt Injection Attacks) are a type of attack on systems powered by Generative AI models that might occur when an application processes information that wasn’t directly authored by either the developer of the application or the user. [Content filtering](/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cpython-new#prompt-shields)
 
 ### 2024-05-01-preview API release
 
@@ -376,9 +398,9 @@ Azure OpenAI Studio now provides a Risks & Safety dashboard for each of your dep
 
 ### 2024-02-01 general availability (GA) API released
 
-This is the latest GA API release and is the replacement for the previous `2023-05-15` GA release. This release adds support for the latest Azure OpenAI GA features like Whisper, DALLE-3, fine-tuning, on your data, etc.
+This is the latest GA API release and is the replacement for the previous `2023-05-15` GA release. This release adds support for the latest Azure OpenAI GA features like Whisper, DALLE-3, fine-tuning, on your data, and more.
 
-Features that are still in preview such as Assistants, text to speech (TTS), certain on your data datasources, still require a preview API version. For more information check out our [API version lifecycle guide](./api-version-deprecation.md).
+Features that are in preview such as Assistants, text to speech (TTS), and some of the "on your data" datasources, require a preview API version. For more information, check out our [API version lifecycle guide](./api-version-deprecation.md).
 
 ### Whisper general availability (GA)
 
@@ -405,9 +427,9 @@ We have added a page to track [model deprecations and retirements](./concepts/mo
 `2024-03-01-preview` has all the same functionality as `2024-02-15-preview` and adds two new parameters for embeddings:
 
 - `encoding_format` allows you to specify the format to generate embeddings in `float`, or `base64`. The default is `float`.
-- `dimensions` allows you set the number of output embeddings. This parameter is only supported with the new third generation embeddings models: `text-embedding-3-large`, `text-embedding-3-small`. Typically larger embeddings are more expensive from a compute, memory, and storage perspective. Being able to adjust the number of dimensions allows more control over overall cost and performance. The `dimensions` parameter is not supported in all versions of the OpenAI 1.x Python library, to take advantage of this parameter  we recommend upgrading to the latest version: `pip install openai --upgrade`.
+- `dimensions` allows you set the number of output embeddings. This parameter is only supported with the new third generation embeddings models: `text-embedding-3-large`, `text-embedding-3-small`. Typically larger embeddings are more expensive from a compute, memory, and storage perspective. Being able to adjust the number of dimensions allows more control over overall cost and performance. The `dimensions` parameter isn't supported in all versions of the OpenAI 1.x Python library, to take advantage of this parameter  we recommend upgrading to the latest version: `pip install openai --upgrade`.
 
-If you are currently using a preview API version to take advantage of the latest features, we recommend consulting the [API version lifecycle](./api-version-deprecation.md) article to track how long your current API version will be supported.
+If you're currently using a preview API version to take advantage of the latest features, we recommend consulting the [API version lifecycle](./api-version-deprecation.md) article to track how long your current API version will be supported.
 
 ### Update to GPT-4-1106-Preview upgrade plans
 
@@ -434,7 +456,7 @@ For information on model regional availability and upgrades refer to the [models
 
 ### GPT-3.5 Turbo quota consolidation
 
-To simplify migration between different versions of the GPT-3.5-Turbo models (including 16k), we will be consolidating all GPT-3.5-Turbo quota into a single quota value.
+To simplify migration between different versions of the GPT-3.5-Turbo models (including 16k), we'll be consolidating all GPT-3.5-Turbo quota into a single quota value.
 
 - Any customers who have increased quota approved will have combined total quota that reflects the previous increases.
 
@@ -502,13 +524,13 @@ GPT-4 Turbo with Vision on Azure OpenAI service is now in public preview. GPT-4
 
 ### New data source support in Azure OpenAI On Your Data
 
-- You can now use [Azure Cosmos DB for MongoDB vCore](./concepts/use-your-data.md#supported-data-sources) as well as URLs/web addresses as data sources to ingest your data and chat with a supported Azure OpenAI model.
+- You can now use [Azure Cosmos DB for MongoDB vCore](./concepts/use-your-data.md#supported-data-sources) and URLs/web addresses as data sources to ingest your data and chat with a supported Azure OpenAI model.
 
 ### GPT-4 Turbo Preview & GPT-3.5-Turbo-1106 released
 
 Both models are the latest release from OpenAI with improved instruction following, [JSON mode](./how-to/json-mode.md), [reproducible output](./how-to/reproducible-output.md), and parallel function calling.
 
-- **GPT-4 Turbo Preview** has a max context window of 128,000 tokens and can generate 4,096 output tokens. It has the latest training data with knowledge up to April 2023. This model is in preview and is not recommended for production use. All deployments of this preview model will be automatically updated in place once the stable release becomes available.
+- **GPT-4 Turbo Preview** has a max context window of 128,000 tokens and can generate 4,096 output tokens. It has the latest training data with knowledge up to April 2023. This model is in preview and isn't recommended for production use. All deployments of this preview model will be automatically updated in place once the stable release becomes available.
 
 - **GPT-3.5-Turbo-1106** has a max context window of 16,385 tokens and can generate 4,096 output tokens.
 
@@ -649,7 +671,7 @@ Azure OpenAI Service now supports speech to text APIs powered by OpenAI's Whispe
   - GPT-35-Turbo models.
   - GPT-4 model series. 
   
-If you are currently using the `2023-03-15-preview` API, we recommend migrating to the GA `2023-05-15` API. If you are currently using API version `2022-12-01` this API remains GA, but does not include the latest Chat Completion capabilities.
+If you're currently using the `2023-03-15-preview` API, we recommend migrating to the GA `2023-05-15` API. If you're currently using API version `2022-12-01` this API remains GA, but doesn't include the latest Chat Completion capabilities.
 
 > [!IMPORTANT]
 > Using the current versions of the GPT-35-Turbo models with the completion endpoint remains in preview.
@@ -674,7 +696,7 @@ If you are currently using the `2023-03-15-preview` API, we recommend migrating
 - **GPT-35-Turbo preview**. To learn more checkout the [how-to article](./how-to/chatgpt.md).
 
 - Increased training limits for fine-tuning: The max training job size (tokens in training file) x (# of epochs) is 2 Billion tokens for all models. We have also increased the max training job from 120 to 720 hours. 
-- Adding additional use cases to your existing access.  Previously, the process for adding new use cases required customers to reapply to the service. Now, we're releasing a new process that allows you to quickly add new use cases to your use of the service. This process follows the established Limited Access process within Azure AI services. [Existing customers can attest to any and all new use cases here](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUM003VEJPRjRSOTZBRVZBV1E5N1lWMk1XUyQlQCN0PWcu). Please note that this is required anytime you would like to use the service for a new use case you did not originally apply for.
+- Adding additional use cases to your existing access.  Previously, the process for adding new use cases required customers to reapply to the service. Now, we're releasing a new process that allows you to quickly add new use cases to your use of the service. This process follows the established Limited Access process within Azure AI services. [Existing customers can attest to any and all new use cases here](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUM003VEJPRjRSOTZBRVZBV1E5N1lWMk1XUyQlQCN0PWcu). Please note that this is required anytime you would like to use the service for a new use case you didn't originally apply for.
 
 ## February 2023
 
@@ -774,4 +796,4 @@ New training course:
 
 ## Next steps
 
-Learn more about the [underlying models that power Azure OpenAI](./concepts/models.md).
+Learn more about the [underlying models that power Azure OpenAI](./concepts/models.md).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能およびAPI更新の追加"
}
```

### Explanation
この変更では、`whats-new.md`ファイルにおいて、Azure OpenAIの最新リリースや重要なドキュメント更新の要約が更新されました。特に、`o1-preview`および`o1-mini`モデルに関する新しい情報が追加されました。

新しいセクションでは、これらのモデルへのアクセスが制限されていること、申請が必要であること、既に早期アクセスを取得している顧客は再申請が不要であることなどが詳述されています。また、APIサポートの変更として、`max_tokens`パラメータが非推奨となり、`max_completion_tokens`パラメータに置き換えられたことが記載されています。さらに、地域ごとのモデルの可用性も明記されており、特定の地域でのデプロイに関する情報も含まれています。

加えて、GPT-4oのリアルタイムAPI、グローバルバッチのサポートアップデート、Azure OpenAI StudioのUX更新なども含まれており、ユーザーはこれらの新しい機能を理解し、活用するための最新情報を得ることができます。このアップデートは、ユーザーにとって重要なリソースであり、製品の利用促進に寄与することを目的としています。

## articles/ai-services/openai/whisper-quickstart.md{#item-4cae3d}

<details>
<summary>Diff</summary>
````diff
@@ -20,9 +20,6 @@ This quickstart explains how to use the [Azure OpenAI Whisper model](../speech-s
 
 The file size limit for the Whisper model is 25 MB. If you need to transcribe a file larger than 25 MB, you can use the Azure AI Speech [batch transcription](../speech-service/batch-transcription-create.md#use-a-whisper-model) API.
 
-> [!NOTE]
-> The OpenAI Whisper model is currently in Limited Access Public Preview.
-
 ::: zone pivot="rest-api"
 
 [!INCLUDE [REST API quickstart](includes/whisper-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisperクイックスタートの情報更新"
}
```

### Explanation
この変更では、`whisper-quickstart.md`ファイルが更新され、いくつかの項目が削除されました。具体的には、Whisperモデルの使用に関する注意書きが削除されました。

具体的には、Whisperモデルが「現在限定アクセスのパブリックプレビュー中である」というメッセージが削除されました。これにより、ユーザーに対する最新の状況やアクセス条件に関する情報が曖昧になり、利用者がWhisperモデルの状態について理解する一助となる情報が欠如しています。

この変更は、ドキュメントのクリーンアップを意図したものであると考えられますが、重要な使用条件に関する情報が不足している可能性があるため、ユーザーへのインパクトが懸念される部分もあります。


