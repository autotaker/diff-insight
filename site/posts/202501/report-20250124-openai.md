---
date: '2025-01-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:985f323...MicrosoftDocs:fee2fd2
summary: このコードの変更では、Azure OpenAIサービスに新しい音声生成機能に関する詳細なドキュメントが追加され、リソース認証関連のリンク修正や日付更新などが行われました。特に、`gpt-4o-audio-preview`モデルのデプロイや使用法に関するクイックスタートガイドやステップバイステップのガイドラインが新たに提供され、音声生成をサポートするためのリソースが充実しています。また、大きな破壊的変更はなく、リンクの修正や情報の最新化が行われています。新しいドキュメントの導入により、開発者が音声を用いたAIアプリケーションをより簡単に設計できるようになり、ユーザー体験が向上します。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:985f323...MicrosoftDocs:fee2fd2){target="_blank"}

<format>
# Highlights
このコードの変更では、Azure OpenAIサービスに関連する新しい音声生成機能に関する詳細なドキュメントが追加され、リソース認証関連のリンク修正や日付更新などの軽微な修正が行われています。特に`gpt-4o-audio-preview`モデルのデプロイ方法や使用法を詳細に説明する複数の新機能が追加され、音声生成の利用をサポートするためのリソースが充実しています。

## New features
1. 音声生成のクイックスタートガイドを含むドキュメントが新たに追加されました。
2. `gpt-4o-audio-preview`モデルのデプロイと利用に関するステップバイステップのガイドラインが提供されています。
3. JavaScript、Python、TypeScript、およびREST APIによる音声完了機能の実装方法が説明される新しいドキュメントが追加されています。
4. AIモデルの展開や使用手順に関連するクイックスタートおよび関連資料が追加されています。

## Breaking changes
特に大きな破壊的変更は含まれていません。

## Other updates
1. 多くのドキュメントで、リソース認証に関するリンクが「resource-auth.md」から「resource-authentication.md」に変更されました。
2. 各種ファイルの日付が最新の日付に更新されました。
3. 各モデルの説明や可能性について詳細が更新されています。

# Insights
Azure OpenAIの音声生成機能に関する新しいドキュメントの追加は、開発者が音声を用いたAIアプリケーションをより容易に設計するための重要なステップです。`gpt-4o-audio-preview`モデルは、音声生成を含む完全なAIサービスを構成するための中心的な役割を担います。この新機能の導入により、Azure AI Foundryプラットフォームを通じて、リアルタイムの音声インタラクションをサポートするためのリソースも強化されています。

背景には、音声がエンドユーザーのインタラクション方法に革命をもたらすという期待があり、今回の更新はその実現を加速するものです。また、ドキュメントの更新・リンク修正は、情報の正確性を高め、ユーザーが必要なリソースに迅速かつ簡単にアクセスできるようにするためのものです。これにより、Azure OpenAIサービスを利用する上でのユーザー体験が大幅に向上し、開発者への支援を強化します。

このように、音声生成機能と関連する新ドキュメントの導入は、AI技術の応用領域を広げ、さまざまな業界での利用拡大に寄与するものと考えられます。加えて、ドキュメントの整合性・可読性を向上させるための微細な修正は、サービスの利用を一層向上させる基盤となります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [audio-completions-quickstart.md](#item-be5860) | new feature | 音声生成のクイックスタートガイドの追加 | added | 59 | 0 | 59 | 
| [models.md](#item-db2c37) | minor update | モデル関連情報の更新 | modified | 14 | 16 | 30 | 
| [gpt-with-vision.md](#item-4d8502) | minor update | GPT-4 Turboモデルに関する情報の修正 | modified | 6 | 7 | 13 | 
| [realtime-audio.md](#item-482ba3) | minor update | リアルタイムオーディオに関する情報の更新 | modified | 5 | 5 | 10 | 
| [reasoning.md](#item-a54b2f) | minor update | o1シリーズモデルの利用可能性に関する情報の修正 | modified | 9 | 8 | 17 | 
| [assistants-javascript.md](#item-ad3627) | minor update | リソース認証に関するリンクの修正 | modified | 1 | 1 | 2 | 
| [assistants-typescript.md](#item-3195a9) | minor update | リソース認証に関するリンクの修正 | modified | 1 | 1 | 2 | 
| [audio-completions-ai-foundry.md](#item-748538) | new feature | 音声生成のためのモデル展開に関する新しいドキュメントの追加 | added | 30 | 0 | 30 | 
| [audio-completions-deploy-model.md](#item-c5a63e) | new feature | gpt-4o-audio-previewモデルのデプロイ方法に関する新しいドキュメントの追加 | added | 18 | 0 | 18 | 
| [audio-completions-intro.md](#item-7391cb) | new feature | gpt-4o-audio-previewモデルの音声機能に関する新しい導入ドキュメントの追加 | added | 39 | 0 | 39 | 
| [audio-completions-javascript.md](#item-b1be01) | new feature | JavaScript用音声完了機能に関する新しいドキュメントの追加 | added | 605 | 0 | 605 | 
| [audio-completions-python.md](#item-a88047) | new feature | Python用音声完了機能に関する新しいドキュメントの追加 | added | 502 | 0 | 502 | 
| [audio-completions-rest.md](#item-0ec305) | new feature | REST APIによる音声完了機能に関する新しいドキュメントの追加 | added | 539 | 0 | 539 | 
| [audio-completions-typescript.md](#item-94bc1f) | new feature | TypeScriptによる音声完了機能に関する新しいドキュメントの追加 | added | 753 | 0 | 753 | 
| [chatgpt-javascript.md](#item-cbf09f) | minor update | ChatGPT用JavaScriptドキュメントの修正 | modified | 3 | 3 | 6 | 
| [chatgpt-typescript.md](#item-6d2f1f) | minor update | ChatGPT用TypeScriptドキュメントの修正 | modified | 1 | 1 | 2 | 
| [dall-e-javascript.md](#item-6cffcf) | minor update | DALL-E用JavaScriptドキュメントの修正 | modified | 3 | 3 | 6 | 
| [dall-e-typescript.md](#item-57b205) | minor update | DALL-E用TypeScriptドキュメントの修正 | modified | 1 | 1 | 2 | 
| [gpt-v-javascript.md](#item-a128c9) | minor update | GPT-V用JavaScriptドキュメントの修正 | modified | 3 | 3 | 6 | 
| [gpt-v-typescript.md](#item-03ec34) | minor update | GPT-V用TypeScriptドキュメントの修正 | modified | 1 | 1 | 2 | 
| [javascript.md](#item-f4828f) | minor update | JavaScriptドキュメントの修正 | modified | 3 | 3 | 6 | 
| [dotnet.md](#item-46e881) | minor update | .NET用Azure OpenAIクライアントライブラリの文書修正 | modified | 5 | 5 | 10 | 
| [realtime-deploy-model.md](#item-21f911) | minor update | リアルタイムモデルデプロイメント手順の更新 | modified | 4 | 4 | 8 | 
| [realtime-javascript.md](#item-3c125e) | minor update | JavaScript用リアルタイムガイドの文書修正 | modified | 2 | 2 | 4 | 
| [realtime-portal.md](#item-1b81a2) | minor update | リアルタイムポータルガイドの日付更新 | modified | 1 | 1 | 2 | 
| [realtime-python.md](#item-1291c0) | minor update | リアルタイムPythonガイドの日付更新とリンク修正 | modified | 2 | 2 | 4 | 
| [realtime-typescript.md](#item-eacc9c) | minor update | リアルタイムTypeScriptガイドの日付更新とリンク修正 | modified | 2 | 2 | 4 | 
| [resource-authentication.md](#item-59aece) | minor update | リソース認証ドキュメントの名称変更 | renamed | 0 | 0 | 0 | 
| [text-to-speech-javascript.md](#item-e9b653) | minor update | テキスト読み上げJavaScriptガイドのリンク修正 | modified | 3 | 3 | 6 | 
| [text-to-speech-typescript.md](#item-1335d5) | minor update | テキスト読み上げTypeScriptガイドのリンク修正 | modified | 1 | 1 | 2 | 
| [typescript.md](#item-ee5b93) | minor update | TypeScriptガイドのリンク修正 | modified | 1 | 1 | 2 | 
| [use-your-data-javascript.md](#item-786699) | minor update | JavaScriptガイドのタブリンク修正 | modified | 2 | 2 | 4 | 
| [whisper-javascript.md](#item-3ee990) | minor update | Whisper JavaScriptガイドのリンク修正 | modified | 2 | 2 | 4 | 
| [whisper-typescript.md](#item-eafedb) | minor update | Whisper TypeScriptガイドのリンク修正 | modified | 1 | 1 | 2 | 
| [audio-completions-chat-playground.png](#item-d78bda) | new feature | 音声完了チャットプレイグラウンドの画像追加 | added | 0 | 0 | 0 | 
| [overview.md](#item-97d507) | minor update | OpenAIオーバービュードキュメントの日付とモデル情報の修正 | modified | 2 | 2 | 4 | 
| [quotas-limits.md](#item-06c6f9) | minor update | 音声ファイルのメッセージサイズ制限の追加 | modified | 1 | 0 | 1 | 
| [realtime-audio-quickstart.md](#item-727df8) | minor update | リアルタイムオーディオクイックスタートの更新 | modified | 2 | 2 | 4 | 
| [toc.yml](#item-c945af) | minor update | 音声生成に関するセクションの追加 | modified | 2 | 0 | 2 | 
| [whats-new.md](#item-53303b) | minor update | Azure OpenAIサービスの新機能に関する更新 | modified | 13 | 4 | 17 | 


# Modified Contents
## articles/ai-services/openai/audio-completions-quickstart.md{#item-be5860}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,59 @@
+---
+title: Quickstart - Getting started with Azure OpenAI audio generation
+titleSuffix: Azure OpenAI
+description: Walkthrough on how to get started with audio generation using Azure OpenAI.
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: how-to
+ms.date: 1/21/2025
+author: eric-urban
+ms.author: eur
+ms.custom: references_regions
+zone_pivot_groups: audio-completions-quickstart
+recommendations: false
+---
+
+# Quickstart: Get started using Azure OpenAI audio generation
+
+::: zone pivot="ai-foundry-portal"
+
+[!INCLUDE [AI Foundry](includes/audio-completions-ai-foundry.md)]
+
+::: zone-end
+
+::: zone pivot="programming-language-javascript"
+
+[!INCLUDE [JavaScript quickstart](includes/audio-completions-javascript.md)]
+
+::: zone-end
+
+::: zone pivot="programming-language-python"
+
+[!INCLUDE [Python SDK quickstart](includes/audio-completions-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest-api"
+
+[!INCLUDE [REST API quickstart](includes/audio-completions-rest.md)]
+
+::: zone-end
+
+::: zone pivot="programming-language-typescript"
+
+[!INCLUDE [TypeScript quickstart](includes/audio-completions-typescript.md)]
+
+::: zone-end
+
+
+## Clean-up resources
+
+If you want to clean up and remove an Azure OpenAI resource, you can delete the resource. Before deleting the resource, you must first delete any deployed models.
+
+- [Azure portal](../multi-service-resource.md?pivots=azportal#clean-up-resources)
+- [Azure CLI](../multi-service-resource.md?pivots=azcli#clean-up-resources)
+
+## Related content
+
+* Learn more about Azure OpenAI [deployment types](./how-to/deployment-types.md)
+* Learn more about Azure OpenAI [quotas and limits](quotas-limits.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "音声生成のクイックスタートガイドの追加"
}
```

### Explanation
この変更は、Azure OpenAI音声生成のクイックスタートガイドを新たに追加するもので、主に59行の新しいコンテンツが含まれています。このガイドでは、音声生成を開始するための手順を詳細に解説しており、AI Foundryポータル、各種プログラミング言語（JavaScript、Python、TypeScript）及びREST APIに関連するクイックスタートが盛り込まれています。また、Azure OpenAIリソースのクリーンアップ手順や関連コンテンツへのリンクも提供されており、ユーザーが必要な情報に迅速にアクセスできるようになっています。このドキュメントは、開発者がAzure OpenAIを利用して音声生成機能を実装する際の便利なリソースとなります。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -18,17 +18,17 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 
 | Models | Description |
 |--|--|
-| [o1 & o1-mini](#o1-and-o1-mini-models-limited-access) | Limited access models, specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability.  |
+| [o1 & o1-mini](#o1-and-o1-mini-models) |[Reasoning models](../how-to/reasoning.md) with advanced problem-solving and increased focus and capability.  |
 | [GPT-4o & GPT-4o mini & GPT-4 Turbo](#gpt-4o-and-gpt-4-turbo) | The latest most capable Azure OpenAI models with multimodal versions, which can accept both text and images as input. |
-| [GPT-4o-Realtime-Preview](#gpt-4o-realtime-preview) | A GPT-4o model that supports low-latency, "speech in, speech out" conversational interactions. |
+| [GPT-4o audio](#gpt-4o-audio) | GPT-4o audio models that support either low-latency, "speech in, speech out" conversational interactions or audio generation. |
 | [GPT-4](#gpt-4) | A set of models that improve on GPT-3.5 and can understand and generate natural language and code. |
 | [GPT-3.5](#gpt-35) | A set of models that improve on GPT-3 and can understand and generate natural language and code. |
 | [Embeddings](#embeddings-models) | A set of models that can convert text into numerical vector form to facilitate text similarity. |
 | [DALL-E](#dall-e-models) | A series of models that can generate original images from natural language. |
 | [Whisper](#whisper-models) | A series of models in preview that can transcribe and translate speech to text. |
 | [Text to speech](#text-to-speech-models-preview) (Preview) | A series of models in preview that can synthesize text to speech. |
 
-## o1 and o1-mini models limited access
+## o1 and o1-mini models
 
 The Azure OpenAI `o1` and `o1-mini` models are specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
 
@@ -40,7 +40,7 @@ The Azure OpenAI `o1` and `o1-mini` models are specifically designed to tackle r
 
 ### Availability
 
-The `o1` and `o1-mini` models are now available for API access and model deployment. **Registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who previously applied and received access to `o1-preview`, don't need to reapply as they are automatically on the wait-list for the latest model.
+The `o1` and `o1-mini` models are now available for API access and model deployment. **For access to `o1` registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who previously applied and received access to `o1-preview`, don't need to reapply as they are automatically on the wait-list for the latest model.
 
 Request access: [limited access model application](https://aka.ms/OAI/o1access)
 
@@ -56,20 +56,23 @@ To learn more about the advanced `o1` series models see, [getting started with o
 | `o1-preview` | See the [models table](#global-standard-model-availability). |
 | `o1-mini` | See the [models table](#global-provisioned-managed-model-availability). |
 
-## GPT-4o-Realtime-Preview
+## GPT-4o audio
 
-The GPT 4o audio models are part of the GPT-4o model family and support low-latency, "speech in, speech out" conversational interactions. GPT-4o audio is designed to handle real-time, low-latency conversational interactions, making it a great fit for support agents, assistants, translators, and other use cases that need highly responsive back-and-forth with a user.
+The GPT 4o audio models are part of the GPT-4o model family and support either low-latency, "speech in, speech out" conversational interactions or audio generation. 
+- GPT-4o real-time audio is designed to handle real-time, low-latency conversational interactions, making it a great fit for support agents, assistants, translators, and other use cases that need highly responsive back-and-forth with a user. For more information on how to use GPT-4o real-time audio, see the [GPT-4o real-time audio quickstart](../realtime-audio-quickstart.md) and [how to use GPT-4o audio](../how-to/realtime-audio.md).
+- GPT-4o audio completion is designed to generate audio from audio or text prompts, making it a great fit for generating audio books, audio content, and other use cases that require audio generation. The GPT-4o audio completions model introduces the audio modality into the existing `/chat/completions` API. For more information on how to use GPT-4o audio completions, see the [audio generation quickstart](../audio-completions-quickstart.md).
 
-GPT-4o audio is available in the East US 2 (`eastus2`) and Sweden Central (`swedencentral`) regions. To use GPT-4o audio, you need to [create](../how-to/create-resource.md) or use an existing resource in one of the supported regions.
+GPT-4o audio is available in the East US 2 (`eastus2`) and Sweden Central (`swedencentral`) regions. To use GPT-4o real-time audio, you need [an Azure OpenAI resource](../how-to/create-resource.md) in one of the supported regions.
 
-When your resource is created, you can [deploy](../how-to/create-resource.md#deploy-a-model) the GPT-4o audio model. For more information on how to use GPT-4o audio, see the [GPT-4o audio quickstart](../realtime-audio-quickstart.md) and [how to use GPT-4o audio](../how-to/realtime-audio.md).
+When your resource is created, you can [deploy](../how-to/create-resource.md#deploy-a-model) the GPT-4o audio model. 
 
 Details about maximum request tokens and training data are available in the following table.
 
 |  Model ID  | Description | Max Request (tokens) | Training Data (up to)  |
 |---|---|---|---|
-|`gpt-4o-realtime-preview` (2024-10-01) <br> **GPT-4o audio** | **Audio model** for real-time audio processing |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
-|`gpt-4o-realtime-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for real-time audio processing |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
+|`gpt-4o-audio-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for audio and text generation. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
+|`gpt-4o-realtime-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for real-time audio processing. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
+|`gpt-4o-realtime-preview` (2024-10-01) <br> **GPT-4o audio** | **Audio model** for real-time audio processing. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
 
 ## GPT-4o and GPT-4 Turbo
 
@@ -126,7 +129,7 @@ See [model versions](../concepts/model-versions.md) to learn about how Azure Ope
 | `gpt-4` (0314) | **Older GA model** <br> - [Retirement information](./model-retirements.md#current-models)  | 8,192 | Sep 2021         |
 
 > [!CAUTION]
-> We don't recommend using preview models in production. We will upgrade all deployments of preview models to either future preview versions or to the latest stable GA version. Models designated preview do not follow the standard Azure OpenAI model lifecycle.
+> We don't recommend using preview models in production. We will upgrade all deployments of preview models to either future preview versions or to the latest stable GA version. Models that are designated preview don't follow the standard Azure OpenAI model lifecycle.
 
 - GPT-4 version 0125-preview is an updated version of the GPT-4 Turbo preview previously released as version 1106-preview.  
 - GPT-4 version 0125-preview completes tasks such as code generation more completely compared to gpt-4-1106-preview. Because of this, depending on the task, customers may find that GPT-4-0125-preview generates more output compared to the gpt-4-1106-preview.  We recommend customers compare the outputs of the new model.  GPT-4-0125-preview also addresses bugs in gpt-4-1106-preview with UTF-8 handling for non-English languages. 
@@ -358,19 +361,14 @@ For Assistants you need a combination of a supported model, and a supported regi
 | **Region**   |  **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**    | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**  | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   | **gpt-35-turbo-16k**, **0613**   |
 |:-----------------|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:------------------------------:|
 | australiaeast    | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                           | ✅                    | ✅                       | ✅                       | ✅                       | ✅                           |
-| canadaeast       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                           | ✅                    | ✅                       | ✅                       | ✅                       | ✅                           |
 | eastus           | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        |  ✅                            | -                   | ✅                       | -                      | ✅                       | ✅                           |
 | eastus2          | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      | ✅                       | ✅                           |
 | francecentral    | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                           | ✅                    | ✅                       | ✅                       | -                      | ✅                           |
 | japaneast        | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | ✅                       | -                      | ✅                       | ✅                           |
-| northcentralus   | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | ✅                            | -                   | ✅                       | -                      | ✅                       | ✅                           |
 | norwayeast       | -                      | -                      | -                           | -               | ✅                        | -                       |  -                           | -                   | -                      | -                      | -                      | -                          |
-| southcentralus   | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                       | ✅                            | -                   | -                      | -                      | ✅                       | -                          |
 | southindia       | -                      | -                      | -                           | -               | ✅                        | -                       | -                           | -                   | -                      | ✅                       | ✅                       | -                          |
 | swedencentral    | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                            | ✅                    | ✅                       | ✅                       | -                      | ✅                           |
-| switzerlandnorth | -                      | -                      | -                           | ✅                | -                       | -                       |  -                           | ✅                    | ✅                       | -                      | ✅                       | ✅                           |
 | uksouth          | -                      | -                      | -                           | -               | ✅                        | ✅                        | -                           | -                   | ✅                       | ✅                       | ✅                       | ✅                           |
-| westeurope       | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | -                      | -                      | -                      | -                          |
 | westus           | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       |✅                            | -                   | -                      | ✅                       | ✅                       | -                          |
 | westus3          | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | ✅                            | -                   | -                      | -                      | ✅                       | -                          |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル関連情報の更新"
}
```

### Explanation
この変更では、Azure OpenAIのモデルに関する情報が更新され、主に14行の新しいコンテンツが追加され、16行の旧コンテンツが削除されています。具体的には、o1およびo1-miniモデルに関する説明が改訂され、特にその機能に関する詳細が追加されました。また、GPT-4oモデル関連のセクションも修正され、モデルの機能や用途が明確になりました。GPT-4oモデルが「低遅延の音声入出力」会話をサポートするだけでなく、音声生成機能も持つことが強調されており、これにより開発者がモデルを利用する際の理解が深まります。これらの更新は、ドキュメントの信頼性を向上させ、ユーザーがモデルを適切に理解し活用するための助けとなります。

## articles/ai-services/openai/how-to/gpt-with-vision.md{#item-4d8502}

<details>
<summary>Diff</summary>
````diff
@@ -13,17 +13,13 @@ manager: nitinme
 # Use vision-enabled chat models
 
 
-Vision-enabled chat models are large multimodal models (LMM) developed by OpenAI that can analyze images and provide textual responses to questions about them. They incorporate both natural language processing and visual understanding. The current vision-enabled models are GPT-4 Turbo with Vision, GPT-4o, and GPT-4o-mini.
+Vision-enabled chat models are large multimodal models (LMM) developed by OpenAI that can analyze images and provide textual responses to questions about them. They incorporate both natural language processing and visual understanding. The current vision-enabled models are [o1](./reasoning.md), GPT-4o, and GPT-4o-mini, GPT-4 Turbo with Vision.
 
 The vision-enabled models answer general questions about what's present in the images you upload.
 
 > [!TIP]
 > To use vision-enabled models, you call the Chat Completion API on a supported model that you have deployed. If you're not familiar with the Chat Completion API, see the [Vision-enabled chat how-to guide](/azure/ai-services/openai/how-to/chatgpt?tabs=python&pivots=programming-language-chat-completions).
 
-## GPT-4 Turbo model upgrade
-
-[!INCLUDE [GPT-4 Turbo](../includes/gpt-4-turbo.md)]
-
 ## Call the Chat Completion APIs
 
 The following command shows the most basic way to use the GPT-4 Turbo with Vision model with code. If this is your first time using these models programmatically, we recommend starting with our [GPT-4 Turbo with Vision quickstart](../gpt-v-quickstart.md). 
@@ -39,8 +35,6 @@ Send a POST request to `https://{RESOURCE_NAME}.openai.azure.com/openai/deployme
 - `Content-Type`: application/json 
 - `api-key`: {API_KEY} 
 
-
-
 **Body**: 
 The following is a sample request body. The format is the same as the chat completions API for GPT-4, except that the message content can be an array containing text and images (either a valid HTTP or HTTPS URL to an image, or a base-64-encoded image). 
 
@@ -368,6 +362,11 @@ Every response includes a `"finish_reason"` field. It has the following possible
     ```
 -->
 
+## GPT-4 Turbo model upgrade
+
+[!INCLUDE [GPT-4 Turbo](../includes/gpt-4-turbo.md)]
+
+
 ## Next steps
 
 * [Learn more about Azure OpenAI](../overview.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turboモデルに関する情報の修正"
}
```

### Explanation
この変更では、Azure OpenAIの「視覚機能を持つチャットモデル」に関する情報が更新されており、主に6行の新しいコンテンツが追加され、7行の旧コンテンツが削除されています。具体的には、視覚機能を持つチャットモデルの定義が明確化され、現在利用可能なモデルのリストにo1モデルが追加されました。また、GPT-4 Turboモデルの情報は再配置され、情報が明確に整理されています。この更新により、ユーザーは視覚機能を持つモデルの使用方法や適用可能なモデルについてより良く理解できるようになります。これらの変更は、ドキュメントの信頼性を高め、ユーザーが必要な情報に迅速にアクセスできるようにすることを目的としています。

## articles/ai-services/openai/how-to/realtime-audio.md{#item-482ba3}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ The GPT 4o real-time models are available for global deployments in [East US 2 a
 - `gpt-4o-realtime-preview` (2024-12-17)
 - `gpt-4o-realtime-preview` (2024-10-01)
 
-See the [models and versions documentation](../concepts/models.md#gpt-4o-realtime-preview) for more information.
+See the [models and versions documentation](../concepts/models.md#gpt-4o-audio) for more information.
 
 ## Get started
 
@@ -248,7 +248,7 @@ In this case, the server evaluates user audio from the client (as sent via [`inp
 - The server commits the input audio buffer by sending the [`input_audio_buffer.committed`](../realtime-audio-reference.md#realtimeservereventinputaudiobuffercommitted) event.
 - The server sends the [`conversation.item.created`](../realtime-audio-reference.md#realtimeservereventconversationitemcreated) event with the user message item created from the audio buffer.
 
-:::image type="content" source="../media/how-to/real-time/input-audio-buffer-server-vad.png" alt-text="Diagram of the Realtime API input audio sequence with server decision mode." lightbox="../media/how-to/real-time/input-audio-buffer-server-vad.png":::
+:::image type="content" source="../media/how-to/real-time/input-audio-buffer-server-vad.png" alt-text="Diagram of the real time API input audio sequence with server decision mode." lightbox="../media/how-to/real-time/input-audio-buffer-server-vad.png":::
 
 
 <!-- 
@@ -300,7 +300,7 @@ Optionally, the client can truncate or delete items in the conversation:
 - The client deletes an item in the conversation with a [`conversation.item.delete`](../realtime-audio-reference.md#realtimeclienteventconversationitemdelete) event.
 - The server [`conversation.item.deleted`](../realtime-audio-reference.md#realtimeservereventconversationitemdeleted) event is returned to sync the client and server state.
 
-:::image type="content" source="../media/how-to/real-time/conversation-item-sequence.png" alt-text="Diagram of the Realtime API conversation item sequence." lightbox="../media/how-to/real-time/conversation-item-sequence.png":::
+:::image type="content" source="../media/how-to/real-time/conversation-item-sequence.png" alt-text="Diagram of the real-time API conversation item sequence." lightbox="../media/how-to/real-time/conversation-item-sequence.png":::
 
 <!-- 
 sequenceDiagram
@@ -324,11 +324,11 @@ To get a response from the model:
 - The client sends a [`response.create`](../realtime-audio-reference.md#realtimeclienteventresponsecreate) event. The server responds with a [`response.created`](../realtime-audio-reference.md#realtimeservereventresponsecreated) event. The response can contain one or more items, each of which can contain one or more content parts.
 - Or, when using server-side voice activity detection (VAD), the server automatically generates a response when it detects the end of speech in the input audio buffer. The server sends a [`response.created`](../realtime-audio-reference.md#realtimeservereventresponsecreated) event with the generated response.
 
-### Response interuption
+### Response interruption
 
 The client [`response.cancel`](../realtime-audio-reference.md#realtimeclienteventresponsecancel) event is used to cancel an in-progress response. 
 
-A user might want to interrupt the assistant's response or ask the assistant to stop talking. The server produces audio faster than realtime. The client can send a [`conversation.item.truncate`](../realtime-audio-reference.md#realtimeclienteventconversationitemtruncate) event to truncate the audio before it's played. 
+A user might want to interrupt the assistant's response or ask the assistant to stop talking. The server produces audio faster than real-time. The client can send a [`conversation.item.truncate`](../realtime-audio-reference.md#realtimeclienteventconversationitemtruncate) event to truncate the audio before it's played. 
 - The server's understanding of the audio with the client's playback is synchronized. 
 - Truncating audio deletes the server-side text transcript to ensure there isn't text in the context that the user doesn't know about.
 - The server responds with a [`conversation.item.truncated`](../realtime-audio-reference.md#realtimeservereventconversationitemtruncated) event.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオに関する情報の更新"
}
```

### Explanation
この変更では、Azure OpenAIのリアルタイムオーディオに関するセクションが修正され、全体で5行の新しいコンテンツが追加され、5行の旧コンテンツが削除されました。主な変更点として、GPT-4oリアルタイムモデルのドキュメントへのリンクが更新され、具体的なモデルについての情報が明確化されました。また、リアルタイムAPIに関連する画像のキャプションが改善され、読みやすさが向上しています。さらに、「レスポンスの中断」というセクションの見出しが文法的に修正され、ユーザーがアシスタントのレスポンスを中断したり、停止を要求する際の手順が明確に説明されています。この更新により、ユーザーはリアルタイムオーディオの利用に関する理解が深まるでしょう。全体として、情報の一貫性と明瞭さが向上し、ドキュメントの全体的な品質が改善されています。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -24,19 +24,19 @@ Azure OpenAI `o1` and `o1-mini` models are designed to tackle reasoning and prob
 
 ## Availability
 
-The **o1 series** models are now available for API access and model deployment. **Registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who previously applied and received access to `o1-preview`, don't need to reapply as they are automatically on the wait-list for the latest model.
+The **o1 series** models are now available for API access and model deployment. **For access to o1, and o1-preview registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who previously applied and received access to `o1-preview`, don't need to reapply as they are automatically on the wait-list for the latest model.
 
 Request access: [limited access model application](https://aka.ms/OAI/o1access)
 
 Once access has been granted, you'll need to create a deployment for each model. If you have an existing `o1-preview` deployment, in-place upgrade is currently not supported, you'll need to create a new deployment.
 
 ### Region availability
 
-| Model | Region |
-|---|---|
-|`o1` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
-| `o1-preview` | See [models page](../concepts/models.md#global-standard-model-availability). |
-| `o1-mini` | See [models page](../concepts/models.md#global-standard-model-availability). |
+| Model | Region | Limited access |
+|---|---|---|
+|`o1` | East US2 (Global Standard) <br> Sweden Central (Global Standard) | [Limited access model application](https://aka.ms/OAI/o1access) |
+| `o1-preview` | See [models page](../concepts/models.md#global-standard-model-availability). | [Limited access model application](https://aka.ms/OAI/o1access) |
+| `o1-mini` | See [models page](../concepts/models.md#global-standard-model-availability). | No access request needed |
 
 ## API & feature support
 
@@ -45,11 +45,12 @@ Once access has been granted, you'll need to create a deployment for each model.
 | **API Version**       | `2024-12-01-preview` | `2024-09-01-preview`  <br> `2024-10-01-preview` <br> `2024-12-01-preview`    | `2024-09-01-preview`  <br> `2024-10-01-preview` <br> `2024-12-01-preview`    |
 | **[Developer Messages](#developer-messages)** | ✅ | - | - |
 | **[Structured Outputs](./structured-outputs.md)** | ✅ | - | - |
-| **[Context Window](../concepts/models.md#o1-and-o1-mini-models-limited-access)** | Input: 200,000 <br> Output: 100,000 | Input: 128,000  <br> Output: 32,768 | Input: 128,000  <br> Output: 65,536 |
+| **[Context Window](../concepts/models.md#o1-and-o1-mini-models)** | Input: 200,000 <br> Output: 100,000 | Input: 128,000  <br> Output: 32,768 | Input: 128,000  <br> Output: 65,536 |
 | **[Reasoning effort](#reasoning-effort)** | ✅ | - | - |
-| System Messages | - | - | - |
+| **[Vision Support](./gpt-with-vision.md)** |✅ | - | - |
 | Functions/Tools | ✅  | -  |  - |
 | `max_completion_tokens` |✅ |✅ |✅ |
+| System Messages | - | - | - |
 
 **o1 series** models will only work with the `max_completion_tokens` parameter.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "o1シリーズモデルの利用可能性に関する情報の修正"
}
```

### Explanation
この変更はAzure OpenAIの「推論」についてのドキュメントを更新しており、主に9行の新しいテキストが追加され、8行が削除されました。具体的には、o1シリーズモデルのアクセス条件が明確化され、o1およびo1-previewに対する登録が必要であることが強調されました。さらに、モデルの地域別の利用可能性についても更新され、各モデルのアクセス情報が表に整理され、見やすさが向上しています。

表には、o1モデルとo1-previewモデルについてのアクセス申請リンクが追加され、利用者が必要な情報に迅速にアクセスできるよう配慮されています。また、他のAPIや機能のサポートに関する情報も一貫して整理され、特にコンテキストウィンドウや推論努力に関連する情報が最新の状態に更新されています。全体として、この変更により、ユーザーがo1シリーズモデルの競技性や利用方法についてより深く理解できるようになっています。

## articles/ai-services/openai/includes/assistants-javascript.md{#item-ad3627}

<details>
<summary>Diff</summary>
````diff
@@ -65,7 +65,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソース認証に関するリンクの修正"
}
```

### Explanation
この変更は、Azure OpenAIのJavaScript向けアシスタントに関連するドキュメントの更新です。具体的には、リソース認証に関するインクルードリンクが修正され、旧リンクから新しいリンクへの変更が行われました。具体的には、「resource-auth.md」から「resource-authentication.md」へと変更され、リソース認証に関する情報の正確性が向上しています。

この小規模な更新は、ドキュメント内での関連情報へのアクセスを容易にし、ユーザーが最新の情報を得られるよう支援しています。また、環境変数に関する注意喚起が引き続き記載されており、キーなし認証の使用時における重要な注意点が強調されています。このように、全体的な文書の整合性と信頼性が向上することにつながります。

## articles/ai-services/openai/includes/assistants-typescript.md{#item-3195a9}

<details>
<summary>Diff</summary>
````diff
@@ -65,7 +65,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソース認証に関するリンクの修正"
}
```

### Explanation
この変更は、Azure OpenAIのTypeScript向けアシスタントに関連するドキュメントを更新したもので、リソース認証に関するインクルードリンクが修正されています。具体的には、「resource-auth.md」から「resource-authentication.md」への変更が行われています。このリンク修正により、ユーザーはリソース認証に関する最新の情報に確実にアクセスできるようになっています。

また、ドキュメント内には、SDKを使用した推奨されるキーなし認証に際し、`AZURE_OPENAI_API_KEY`環境変数が設定されていないことを確認するための注意喚起が引き続き掲載されています。これにより、利用者が正しい設定で機能を使用できるよう配慮されており、全体的な文書の精度と有用性が向上しています。

## articles/ai-services/openai/includes/audio-completions-ai-foundry.md{#item-748538}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,30 @@
+---
+manager: nitinme
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 1/7/2025
+---
+
+[!INCLUDE [Audio completions introduction](audio-completions-intro.md)]
+
+## Deploy a model for audio generation
+
+[!INCLUDE [Deploy model](audio-completions-deploy-model.md)]
+
+## Use GPT-4o audio generation
+
+To chat with your deployed `gpt-4o-audio-preview` model in the **Chat** playground of [Azure AI Foundry portal](https://ai.azure.com), follow these steps:
+
+1. Go to the [Azure OpenAI Service page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource and the deployed `gpt-4o-audio-preview` model.
+1. Select the **Chat** playground from under **Resource playground** in the left pane.
+1. Select your deployed `gpt-4o-audio-preview` model from the **Deployment** dropdown. 
+1. Start chatting with the model and listen to the audio responses.
+
+    :::image type="content" source="../media/quickstarts/audio-completions-chat-playground.png" alt-text="Screenshot of the Chat playground page." lightbox="../media/quickstarts/audio-completions-chat-playground.png":::
+
+    You can:
+    - Record audio prompts.
+    - Attach audio files to the chat.
+    - Enter text prompts.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "音声生成のためのモデル展開に関する新しいドキュメントの追加"
}
```

### Explanation
この変更は、Azure OpenAIの音声完了機能に関する新しいドキュメントを追加したもので、具体的には「audio-completions-ai-foundry.md」というファイルが新たに作成されています。このファイルには、音声生成のためにデプロイされたモデルを使用する方法が詳細に記載されています。

新しいコンテンツには、音声生成の基本概念を紹介するためのセクションや、Azure AI Foundryポータル内の「Chat」プレイグラウンドで`gpt-4o-audio-preview`モデルと対話する手順が含まれています。ユーザーは、Azure OpenAIサービスページにアクセスし、リソースプレイグラウンドから自分のモデルを選択することで、音声返答を得ることができます。また、音声プロンプトを録音したり、音声ファイルをチャットに添付したり、テキストプロンプトを入力したりする機能も説明されています。

これにより、ユーザーは新しい音声生成機能をより効果的に利用できるようになり、Azure AI Foundryが提供する音声アプリケーションの可能性が広がります。

## articles/ai-services/openai/includes/audio-completions-deploy-model.md{#item-c5a63e}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,18 @@
+---
+manager: nitinme
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 1/21/2025
+---
+
+To deploy the `gpt-4o-audio-preview` model in the Azure AI Foundry portal:
+1. Go to the [Azure OpenAI Service page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource and the deployed `gpt-4o-audio-preview` model.
+1. Select the **Chat** playground from under **Playgrounds** in the left pane.
+1. Select **+ Create new deployment** > **From base models** to open the deployment window. 
+1. Search for and select the `gpt-4o-audio-preview` model and then select **Deploy to selected resource**.
+1. In the deployment wizard, select the `2024-12-17` model version.
+1. Follow the wizard to finish deploying the model.
+
+Now that you have a deployment of the `gpt-4o-audio-preview` model, you can interact with it in the Azure AI Foundry portal **Chat** playground or chat completions API.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "gpt-4o-audio-previewモデルのデプロイ方法に関する新しいドキュメントの追加"
}
```

### Explanation
この変更は、Azure OpenAIの音声完了機能に関連する新しいドキュメント「audio-completions-deploy-model.md」を追加したもので、特に`gpt-4o-audio-preview`モデルをAzure AI Foundryポータルでデプロイする手順が詳述されています。

このドキュメントには、モデルのデプロイに関する重要なステップがリスト形式で示されており、ユーザーはAzure OpenAI Serviceページにアクセスし、Chatプレイグラウンドから新しいデプロイメントを作成する方法を学ぶことができます。具体的には、`gpt-4o-audio-preview`モデルを見つけて選択し、モデルのバージョンを指定しながらデプロイメントウィザードを進める手順が説明されています。

これにより、ユーザーは新しい音声モデルを簡単にデプロイし、Azure AI Foundryポータル内のChatプレイグラウンドやチャット完了APIを介してインタラクションを行えるようになり、音声アプリケーションの活用が大幅に向上します。

## articles/ai-services/openai/includes/audio-completions-intro.md{#item-7391cb}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,39 @@
+---
+manager: nitinme
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 1/21/2025
+---
+
+The `gpt-4o-audio-preview` model introduces the audio modality into the existing `/chat/completions` API. The audio model expands the potential for AI applications in text and voice-based interactions and audio analysis. Modalities supported in `gpt-4o-audio-preview` model include:  text, audio, and text + audio.
+
+Here's a table of the supported modalities with example use cases:
+
+| Modality input | Modality output | Example use case |
+| --- | --- | --- |
+| Text | Text + audio | Text to speech, audio book generation |
+| Audio | Text + audio | Audio transcription, audio book generation |
+| Audio | Text | Audio transcription |
+| Text + audio | Text + audio | Audio book generation |
+| Text + audio | Text | Audio transcription |
+
+By using audio generation capabilities, you can achieve more dynamic and interactive AI applications. Models that support audio inputs and outputs allow you to generate spoken audio responses to prompts and use audio inputs to prompt the model. 
+
+## Supported models
+
+Currently only `gpt-4o-audio-preview` version: `2024-12-17` supports audio generation.
+
+The `gpt-4o-audio-preview` model is available for global deployments in [East US 2 and Sweden Central regions](../concepts/models.md#global-standard-model-availability).
+
+Currently the following voices are supported for audio out: Alloy, Echo, and Shimmer.
+
+The maximum audio file size is 20 MB.
+
+> [!NOTE]
+> The [Realtime API](../realtime-audio-quickstart.md) uses the same underlying GPT-4o audio model as the completions API, but is optimized for low-latency, real-time audio interactions.
+
+## API support
+
+Support for audio completions was first added in API version `2025-01-01-preview`. 
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "gpt-4o-audio-previewモデルの音声機能に関する新しい導入ドキュメントの追加"
}
```

### Explanation
この変更は、`gpt-4o-audio-preview`モデルが音声モダリティを既存の`/chat/completions` APIに導入することを説明する新しいドキュメント「audio-completions-intro.md」を追加したものです。このドキュメントには、音声モデルがテキストおよび音声ベースのインタラクションや音声分析におけるAIアプリケーションの可能性を拡大する方法が詳述されています。

新しいコンテンツでは、サポートされているモダリティやそれぞれの使用例を表形式で紹介しており、テキストや音声を入力として受け取り、テキストや音声を出力する具体例が挙げられています。また、音声生成機能を利用することによって、よりダイナミックでインタラクティブなAIアプリケーションを実現可能であることが強調されています。

さらに、音声生成をサポートするモデルの情報として、現在唯一のサポート対象である`gpt-4o-audio-preview`モデルが利用できる地域、サポートされている音声、最大音声ファイルサイズの制限も記載されています。リアルタイム音声インタラクション向けのAPIについても言及されており、同じ音声モデルを基にしたリアルタイムAPIの存在が説明されています。

音声完了のAPIサポートは2025年1月1日のプレビュー版から開始されており、このドキュメントは新しい音声機能の利用方法を学ぶための重要なリソースとなります。

## articles/ai-services/openai/includes/audio-completions-javascript.md{#item-b1be01}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,605 @@
+---
+manager: nitinme
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 1/21/2025
+---
+
+[Reference documentation](https://platform.openai.com/docs/api-reference/chat) | [Library source code](https://github.com/openai/openai-node?azure-portal=true) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
+
+[!INCLUDE [Audio completions introduction](audio-completions-intro.md)]
+
+## Prerequisites
+
+- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
+- <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
+- An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- Then, you need to deploy a `gpt-4o-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
+
+## Microsoft Entra ID prerequisites
+
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
+
+## Set up
+
+1. Create a new folder `audio-completions-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
+
+    ```shell
+    mkdir audio-completions-quickstart && code audio-completions-quickstart
+    ```
+    
+1. Create the `package.json` with the following command:
+
+    ```shell
+    npm init -y
+    ```
+
+1. Update the `package.json` to ECMAScript with the following command: 
+
+    ```shell
+    npm pkg set type=module
+    ```
+    
+
+1. Install the OpenAI client library for JavaScript with:
+
+    ```console
+    npm install openai
+    ```
+
+1. For the **recommended** keyless authentication with Microsoft Entra ID, install the `@azure/identity` package with:
+
+    ```console
+    npm install @azure/identity
+    ```
+
+
+## Retrieve resource information
+
+[!INCLUDE [resource authentication](resource-authentication.md)]
+
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+
+## Generate audio from text input
+
+#### [Microsoft Entra ID](#tab/keyless)
+
+1. Create the `to-audio.js` file with the following code:
+
+    ```javascript
+    require("dotenv").config();
+    const { AzureOpenAI } = require("openai");
+    const { DefaultAzureCredential, getBearerTokenProvider } = require("@azure/identity");
+    const { writeFileSync } = require("node:fs");
+    
+    // Keyless authentication    
+    const credential = new DefaultAzureCredential();
+    const scope = "https://cognitiveservices.azure.com/.default";
+    const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+    
+    // Set environment variables or edit the corresponding values here.
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const apiVersion = "2025-01-01-preview"; 
+    const deployment = "gpt-4o-audio-preview"; 
+    
+    const client = new AzureOpenAI({ 
+        endpoint, 
+        azureADTokenProvider, 
+        apiVersion, 
+        deployment 
+    }); 
+    
+    async function main() {
+    
+        // Make the audio chat completions request
+        const response = await client.chat.completions.create({ 
+            model: "gpt-4o-audio-preview", 
+            modalities: ["text", "audio"], 
+            audio: { voice: "alloy", format: "wav" }, 
+            messages: [ 
+            { 
+                role: "user", 
+                content: "Is a golden retriever a good family dog?" 
+            } 
+            ] 
+        }); 
+      
+    // Inspect returned data 
+    console.log(response.choices[0]); 
+    
+    // Write the output audio data to a file
+    writeFileSync( 
+        "dog.wav", 
+        Buffer.from(response.choices[0].message.audio.data, 'base64'), 
+        { encoding: "utf-8" } 
+    ); 
+    }
+    
+    main().catch((err) => {
+      console.error("Error occurred:", err);
+    });
+    
+    module.exports = { main };
+    ```
+
+1. Sign in to Azure with the following command:
+
+    ```shell
+    az login
+    ```
+
+1. Run the JavaScript file.
+
+    ```shell
+    node to-audio.js
+    ```
+
+
+#### [API key](#tab/api-key)
+
+1. Create the `to-audio.js` file with the following code:
+
+    ```javascript
+    require("dotenv").config();
+    const { AzureOpenAI } = require("openai");
+    const { writeFileSync } = require("node:fs");
+    
+    // Set environment variables or edit the corresponding values here.
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
+    const apiVersion = "2025-01-01-preview"; 
+    const deployment = "gpt-4o-audio-preview"; 
+    
+    const client = new AzureOpenAI({ 
+        endpoint, 
+        apiKey, 
+        apiVersion, 
+        deployment 
+    });  
+    
+    async function main() {
+    
+        // Make the audio chat completions request
+        const response = await client.chat.completions.create({ 
+            model: "gpt-4o-audio-preview", 
+            modalities: ["text", "audio"], 
+            audio: { voice: "alloy", format: "wav" }, 
+            messages: [ 
+            { 
+                role: "user", 
+                content: "Is a golden retriever a good family dog?" 
+            } 
+            ] 
+        }); 
+      
+    // Inspect returned data 
+    console.log(response.choices[0]); 
+    
+    // Write the output audio data to a file
+    writeFileSync( 
+        "dog.wav", 
+        Buffer.from(response.choices[0].message.audio.data, 'base64'), 
+        { encoding: "utf-8" } 
+    ); 
+    }
+    
+    main().catch((err) => {
+      console.error("Error occurred:", err);
+    });
+    
+    module.exports = { main };
+    ```
+
+1. Run the JavaScript file.
+
+    ```shell
+    node to-audio.js
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+### Output for audio generation from text input
+
+The script generates an audio file named _dog.wav_ in the same directory as the script. The audio file contains the spoken response to the prompt, "Is a golden retriever a good family dog?"
+
+
+## Generate audio and text from audio input
+
+#### [Microsoft Entra ID](#tab/keyless)
+
+1. Create the `from-audio.js` file with the following code:
+
+    ```javascript
+    require("dotenv").config();
+    const { AzureOpenAI } = require("openai");
+    const { DefaultAzureCredential, getBearerTokenProvider } = require("@azure/identity");
+    const fs = require('fs').promises;
+    const { writeFileSync } = require("node:fs");
+    
+    // Keyless authentication    
+    const credential = new DefaultAzureCredential();
+    const scope = "https://cognitiveservices.azure.com/.default";
+    const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+    
+    // Set environment variables or edit the corresponding values here.
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const apiVersion = "2025-01-01-preview"; 
+    const deployment = "gpt-4o-audio-preview"; 
+    
+    const client = new AzureOpenAI({ 
+        endpoint, 
+        azureADTokenProvider, 
+        apiVersion, 
+        deployment 
+    });    
+    
+    async function main() {
+        
+        // Buffer the audio for input to the chat completion
+        const wavBuffer = await fs.readFile("dog.wav"); 
+        const base64str = Buffer.from(wavBuffer).toString("base64"); 
+        
+        // Make the audio chat completions request
+        const response = await client.chat.completions.create({
+            model: "gpt-4o-audio-preview",
+            modalities: ["text", "audio"],
+            audio: { voice: "alloy", format: "wav" }, 
+            messages: [
+                {
+                    role: "user",
+                    content: [
+                        { 
+                            type: "text", 
+                            text: "Describe in detail the spoken audio input." 
+                        },
+                        { 
+                            type: "input_audio", 
+                            input_audio: { 
+                                data: base64str, 
+                                format: "wav" 
+                            } 
+                        }
+                    ]
+                }
+            ]
+        });
+        
+        console.log(response.choices[0]); 
+      
+        // Write the output audio data to a file
+        writeFileSync( 
+            "analysis.wav", 
+            Buffer.from(response.choices[0].message.audio.data, 'base64'), 
+            { encoding: "utf-8" } 
+        ); 
+    }
+    
+    main().catch((err) => {
+        console.error("Error occurred:", err);
+    });
+    
+    module.exports = { main };
+    ```
+
+1. Sign in to Azure with the following command:
+
+    ```shell
+    az login
+    ```
+
+1. Run the JavaScript file.
+
+    ```shell
+    node from-audio.js
+    ```
+
+
+#### [API key](#tab/api-key)
+
+1. Create the `from-audio.js` file with the following code:
+
+    ```javascript 
+    require("dotenv").config();
+    const { AzureOpenAI } = require("openai");
+    const fs = require('fs').promises;
+    const { writeFileSync } = require("node:fs");
+    
+    // Set environment variables or edit the corresponding values here.
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
+    const apiVersion = "2025-01-01-preview"; 
+    const deployment = "gpt-4o-audio-preview"; 
+    
+    const client = new AzureOpenAI({ 
+        endpoint, 
+        apiKey, 
+        apiVersion, 
+        deployment 
+    });  
+    
+    async function main() {
+        
+        // Buffer the audio for input to the chat completion
+        const wavBuffer = await fs.readFile("dog.wav"); 
+        const base64str = Buffer.from(wavBuffer).toString("base64"); 
+        
+        // Make the audio chat completions request
+        const response = await client.chat.completions.create({
+            model: "gpt-4o-audio-preview",
+            modalities: ["text", "audio"],
+            audio: { voice: "alloy", format: "wav" }, 
+            messages: [
+                {
+                    role: "user",
+                    content: [
+                        { 
+                            type: "text", 
+                            text: "Describe in detail the spoken audio input." 
+                        },
+                        { 
+                            type: "input_audio", 
+                            input_audio: { 
+                                data: base64str, 
+                                format: "wav" 
+                            } 
+                        }
+                    ]
+                }
+            ]
+        });
+        
+        console.log(response.choices[0]); 
+      
+        // Write the output audio data to a file
+        writeFileSync( 
+            "analysis.wav", 
+            Buffer.from(response.choices[0].message.audio.data, 'base64'), 
+            { encoding: "utf-8" } 
+        ); 
+    }
+    
+    main().catch((err) => {
+        console.error("Error occurred:", err);
+    });
+    
+    module.exports = { main };
+    ```
+
+1. Run the JavaScript file.
+
+    ```shell
+    node from-audio.js
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+### Output for audio and text generation from audio input
+
+The script generates a transcript of the summary of the spoken audio input. It also generates an audio file named _analysis.wav_ in the same directory as the script. The audio file contains the spoken response to the prompt.
+
+## Generate audio and use multi-turn chat completions
+
+#### [Microsoft Entra ID](#tab/keyless)
+
+1. Create the `multi-turn.js` file with the following code:
+
+    ```javascript 
+    require("dotenv").config();
+    const { AzureOpenAI } = require("openai");
+    const { DefaultAzureCredential, getBearerTokenProvider } = require("@azure/identity");
+    const fs = require('fs').promises;
+    
+    // Keyless authentication    
+    const credential = new DefaultAzureCredential();
+    const scope = "https://cognitiveservices.azure.com/.default";
+    const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+    
+    // Set environment variables or edit the corresponding values here.
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const apiVersion = "2025-01-01-preview"; 
+    const deployment = "gpt-4o-audio-preview"; 
+    
+    const client = new AzureOpenAI({ 
+        endpoint, 
+        azureADTokenProvider, 
+        apiVersion, 
+        deployment 
+    }); 
+    
+    async function main() {
+        
+        // Buffer the audio for input to the chat completion
+        const wavBuffer = await fs.readFile("dog.wav"); 
+        const base64str = Buffer.from(wavBuffer).toString("base64"); 
+        
+        // Initialize messages with the first turn's user input 
+        const messages = [
+            {
+                role: "user",
+                content: [
+                    { 
+                        type: "text", 
+                        text: "Describe in detail the spoken audio input." 
+                    },
+                    { 
+                        type: "input_audio", 
+                        input_audio: { 
+                            data: base64str, 
+                            format: "wav" 
+                        } 
+                    }
+                ]
+            }
+        ];
+        
+        // Get the first turn's response 
+    
+        const response = await client.chat.completions.create({ 
+            model: "gpt-4o-audio-preview",
+            modalities: ["text", "audio"], 
+            audio: { voice: "alloy", format: "wav" }, 
+            messages: messages
+        }); 
+        
+        console.log(response.choices[0]); 
+        
+        // Add a history message referencing the previous turn's audio by ID 
+        messages.push({ 
+            role: "assistant", 
+            audio: { id: response.choices[0].message.audio.id }
+        });
+    
+        // Add a new user message for the second turn
+        messages.push({ 
+            role: "user", 
+            content: [ 
+                { 
+                    type: "text", 
+                    text: "Very concisely summarize the favorability." 
+                } 
+            ] 
+        }); 
+    
+        // Send the follow-up request with the accumulated messages
+        const followResponse = await client.chat.completions.create({ 
+            model: "gpt-4o-audio-preview",
+            messages: messages
+        });
+    
+        console.log(followResponse.choices[0].message.content); 
+    }
+    
+    main().catch((err) => {
+        console.error("Error occurred:", err);
+    });
+    
+    module.exports = { main };
+    ```
+
+1. Sign in to Azure with the following command:
+
+    ```shell
+    az login
+    ```
+
+1. Run the JavaScript file.
+
+    ```shell
+    node multi-turn.js
+    ```
+
+
+#### [API key](#tab/api-key)
+
+1. Create the `multi-turn.js` file with the following code:
+
+    ```javascript 
+    require("dotenv").config();
+    const { AzureOpenAI } = require("openai");
+    const fs = require('fs').promises;
+    
+    // Set environment variables or edit the corresponding values here.
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
+    const apiVersion = "2025-01-01-preview"; 
+    const deployment = "gpt-4o-audio-preview"; 
+    
+    const client = new AzureOpenAI({ 
+        endpoint, 
+        apiKey, 
+        apiVersion, 
+        deployment 
+    });  
+    
+    async function main() {
+        
+        // Buffer the audio for input to the chat completion
+        const wavBuffer = await fs.readFile("dog.wav"); 
+        const base64str = Buffer.from(wavBuffer).toString("base64"); 
+        
+        // Initialize messages with the first turn's user input 
+        const messages = [
+            {
+                role: "user",
+                content: [
+                    { 
+                        type: "text", 
+                        text: "Describe in detail the spoken audio input." 
+                    },
+                    { 
+                        type: "input_audio", 
+                        input_audio: { 
+                            data: base64str, 
+                            format: "wav" 
+                        } 
+                    }
+                ]
+            }
+        ];
+        
+        // Get the first turn's response 
+    
+        const response = await client.chat.completions.create({ 
+            model: "gpt-4o-audio-preview",
+            modalities: ["text", "audio"], 
+            audio: { voice: "alloy", format: "wav" }, 
+            messages: messages
+        }); 
+        
+        console.log(response.choices[0]); 
+        
+        // Add a history message referencing the previous turn's audio by ID 
+        messages.push({ 
+            role: "assistant", 
+            audio: { id: response.choices[0].message.audio.id }
+        });
+    
+        // Add a new user message for the second turn
+        messages.push({ 
+            role: "user", 
+            content: [ 
+                { 
+                    type: "text", 
+                    text: "Very concisely summarize the favorability." 
+                } 
+            ] 
+        }); 
+    
+        // Send the follow-up request with the accumulated messages
+        const followResponse = await client.chat.completions.create({ 
+            model: "gpt-4o-audio-preview",
+            messages: messages
+        });
+    
+        console.log(followResponse.choices[0].message.content); 
+    }
+    
+    main().catch((err) => {
+        console.error("Error occurred:", err);
+    });
+    
+    module.exports = { main };
+    ```
+
+1. Run the JavaScript file.
+
+    ```shell
+    node multi-turn.js
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+### Output for multi-turn chat completions
+
+The script generates a transcript of the summary of the spoken audio input. Then, it makes a multi-turn chat completion to briefly summarize the spoken audio input. 
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "JavaScript用音声完了機能に関する新しいドキュメントの追加"
}
```

### Explanation
この変更は、`gpt-4o-audio-preview`モデルを使用して音声完了を実現するためのJavaScriptに関する新しいドキュメント「audio-completions-javascript.md」を追加したものです。このドキュメントでは、音声とテキストの相互作用が可能なAIアプリケーションを構築するための手順が詳述されています。

ドキュメントには、まずAzureのサブスクリプション、Node.jsの環境、および`gpt-4o-audio-preview`モデルを展開するためのAzure OpenAIリソースの設定が必要であることが説明されています。また、Microsoft Entra IDを使用したキーのない認証に関する前提条件も記載されています。

続いて、音声入力をテキストとして、またはその逆に変換するための具体的な手順が示されています。全体を通してコードスニペットが豊富に含まれており、ユーザーは具体的にどのように設定を行い、どのようにスクリプトを実行するかを学ぶことができます。スクリプトの実行により、音声ファイルから音声出力を生成したり、音声を認識してその内容を要約することが可能です。

最後に、マルチターンチャット機能を利用する方法も説明されており、ユーザーは更にインタラクティブな体験を構築できます。これにより、音声に基づいたAIアプリケーションの実装が簡易化されるとともに、開発者の幅広いニーズに応える情報が提供されることになります。

## articles/ai-services/openai/includes/audio-completions-python.md{#item-a88047}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,502 @@
+---
+manager: nitinme
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 1/21/2025
+---
+
+[Library source code](https://github.com/openai/openai-python/tree/main/src/openai) | [Package](https://github.com/openai/openai-python) | [Samples](https://github.com/openai/openai-python/tree/main/examples)
+
+[!INCLUDE [Audio completions introduction](audio-completions-intro.md)]
+
+Use this guide to get started generating audio with the Azure OpenAI SDK for Python.
+
+## Prerequisites
+
+- An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
+- <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>. We recommend using Python 3.10 or later, but having at least Python 3.8 is required. If you don't have a suitable version of Python installed, you can follow the instructions in the [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter) for the easiest way of installing Python on your operating system.
+- An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- Then, you need to deploy a `gpt-4o-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+
+## Microsoft Entra ID prerequisites
+
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
+
+## Set up
+
+1. Create a new folder `audio-completions-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
+
+    ```shell
+    mkdir audio-completions-quickstart && code audio-completions-quickstart
+    ```
+    
+1. Create a virtual environment. If you already have Python 3.10 or higher installed, you can create a virtual environment using the following commands:
+    
+    # [Windows](#tab/windows)
+    
+    ```bash
+    py -3 -m venv .venv
+    .venv\scripts\activate
+    ```
+    
+    # [Linux](#tab/linux)
+    
+    ```bash
+    python3 -m venv .venv
+    source .venv/bin/activate
+    ```
+    
+    # [macOS](#tab/macos)
+    
+    ```bash
+    python3 -m venv .venv
+    source .venv/bin/activate
+    ```
+    
+    ---
+    
+    Activating the Python environment means that when you run ```python``` or ```pip``` from the command line, you then use the Python interpreter contained in the ```.venv``` folder of your application. You can use the ```deactivate``` command to exit the python virtual environment, and can later reactivate it when needed.
+
+    > [!TIP]
+    > We recommend that you create and activate a new Python environment to use to install the packages you need for this tutorial. Don't install packages into your global python installation. You should always use a virtual or conda environment when installing python packages, otherwise you can break your global installation of Python.
+
+1. Install the OpenAI client library for Python with:
+
+    ```console
+    pip install openai
+    ```
+
+1. For the **recommended** keyless authentication with Microsoft Entra ID, install the `azure-identity` package with:
+
+    ```console
+    pip install azure-identity
+    ```
+
+## Retrieve resource information
+
+[!INCLUDE [resource authentication](resource-authentication.md)]
+
+## Generate audio from text input
+
+## [Microsoft Entra ID](#tab/keyless)
+
+1. Create the `to-audio.py` file with the following code:
+
+    ```python
+    import requests
+    import base64 
+    import os 
+    from openai import AzureOpenAI
+    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+    
+    token_provider=get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")
+    
+    # Set environment variables or edit the corresponding values here.
+    endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
+    
+    # Keyless authentication
+    client=AzureOpenAI(
+        azure_ad_token_provider=token_provider,
+        azure_endpoint=endpoint,
+        api_version="2025-01-01-preview"
+    )
+    
+    # Make the audio chat completions request
+    completion=client.chat.completions.create(
+        model="gpt-4o-audio-preview",
+        modalities=["text", "audio"],
+        audio={"voice": "alloy", "format": "wav"},
+        messages=[
+            {
+                "role": "user",
+                "content": "Is a golden retriever a good family dog?"
+            }
+        ]
+    )
+    
+    print(completion.choices[0])
+    
+    # Write the output audio data to a file
+    wav_bytes=base64.b64decode(completion.choices[0].message.audio.data)
+    with open("dog.wav", "wb") as f:
+        f.write(wav_bytes)
+    ```
+
+1. Run the Python file.
+
+    ```shell
+    python to-audio.py
+    ```
+
+## [API key](#tab/api-key)
+
+1. Create the `to-audio.py` file with the following code:
+
+    ```python
+    import base64 
+    import os 
+    from openai import AzureOpenAI 
+    
+    # Set environment variables or edit the corresponding values here.
+    endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
+    api_key = os.environ['AZURE_OPENAI_API_KEY']
+    
+    client = AzureOpenAI(
+        api_version="2025-01-01-preview",  
+        api_key=api_key,
+        azure_endpoint=endpoint
+    )
+    
+    # Make the audio chat completions request
+    completion = client.chat.completions.create(
+        model="gpt-4o-audio-preview",
+        modalities=["text", "audio"],
+        audio={"voice": "alloy", "format": "wav"},
+        messages=[
+            {
+                "role": "user",
+                "content": "Is a golden retriever a good family dog?"
+            }
+        ]
+    )
+    
+    print(completion.choices[0])
+    
+    # Write the output audio data to a file
+    wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
+    with open("dog.wav", "wb") as f:
+        f.write(wav_bytes)
+    ```
+
+1. Run the Python file.
+
+    ```shell
+    python to-audio.py
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+### Output for audio generation from text input
+
+The script generates an audio file named _dog.wav_ in the same directory as the script. The audio file contains the spoken response to the prompt, "Is a golden retriever a good family dog?"
+
+## Generate audio and text from audio input
+
+## [Microsoft Entra ID](#tab/keyless)
+
+1. Create the `from-audio.py` file with the following code:
+
+    ```python
+    import base64
+    import os
+    from openai import AzureOpenAI
+    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+    
+    token_provider=get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")
+    
+    # Set environment variables or edit the corresponding values here.
+    endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
+    
+    # Keyless authentication
+    client=AzureOpenAI(
+        azure_ad_token_provider=token_provider,
+        azure_endpoint=endpoint
+        api_version="2025-01-01-preview"
+    )
+    
+    # Read and encode audio file  
+    with open('dog.wav', 'rb') as wav_reader: 
+        encoded_string = base64.b64encode(wav_reader.read()).decode('utf-8') 
+     
+    # Make the audio chat completions request
+    completion = client.chat.completions.create( 
+        model="gpt-4o-audio-preview", 
+        modalities=["text", "audio"], 
+        audio={"voice": "alloy", "format": "wav"}, 
+        messages=[ 
+            { 
+                "role": "user", 
+                "content": [ 
+                    {  
+                        "type": "text", 
+                        "text": "Describe in detail the spoken audio input." 
+                    }, 
+                    { 
+                        "type": "input_audio", 
+                        "input_audio": { 
+                            "data": encoded_string, 
+                            "format": "wav" 
+                        } 
+                    } 
+                ] 
+            }, 
+        ] 
+    ) 
+    
+    print(completion.choices[0].message.audio.transcript)
+    
+    # Write the output audio data to a file
+    wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
+    with open("analysis.wav", "wb") as f:
+        f.write(wav_bytes)
+    ```
+
+1. Run the Python file.
+
+    ```shell
+    python from-audio.py
+    ```
+
+## [API key](#tab/api-key)
+
+1. Create the `from-audio.py` file with the following code:
+
+    ```python
+    import base64
+    import os
+    from openai import AzureOpenAI
+    
+    # Set environment variables or edit the corresponding values here.
+    endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
+    api_key = os.environ['AZURE_OPENAI_API_KEY']
+    
+    client = AzureOpenAI(
+        api_version="2025-01-01-preview",  
+        api_key=api_key, 
+        azure_endpoint=endpoint
+    )
+    
+    # Read and encode audio file  
+    with open('dog.wav', 'rb') as wav_reader: 
+        encoded_string = base64.b64encode(wav_reader.read()).decode('utf-8') 
+     
+    # Make the audio chat completions request
+    completion = client.chat.completions.create( 
+        model="gpt-4o-audio-preview", 
+        modalities=["text", "audio"], 
+        audio={"voice": "alloy", "format": "wav"}, 
+        messages=[ 
+            { 
+                "role": "user", 
+                "content": [ 
+                    {  
+                        "type": "text", 
+                        "text": "Describe in detail the spoken audio input." 
+                    }, 
+                    { 
+                        "type": "input_audio", 
+                        "input_audio": { 
+                            "data": encoded_string, 
+                            "format": "wav" 
+                        } 
+                    } 
+                ] 
+            }, 
+        ] 
+    ) 
+    
+    print(completion.choices[0].message.audio.transcript)
+    
+    # Write the output audio data to a file
+    wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
+    with open("analysis.wav", "wb") as f:
+        f.write(wav_bytes)
+    ```
+
+1. Run the Python file.
+
+    ```shell
+    python from-audio.py
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+### Output for audio and text generation from audio input
+
+The script generates a transcript of the summary of the spoken audio input. It also generates an audio file named _analysis.wav_ in the same directory as the script. The audio file contains the spoken response to the prompt.
+
+
+## Generate audio and use multi-turn chat completions
+
+## [Microsoft Entra ID](#tab/keyless)
+
+1. Create the `multi-turn.py` file with the following code:
+
+    ```python
+    import base64 
+    import os 
+    from openai import AzureOpenAI 
+    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+    
+    token_provider=get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")
+    
+    # Set environment variables or edit the corresponding values here.
+    endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
+    
+    # Keyless authentication
+    client=AzureOpenAI(
+        azure_ad_token_provider=token_provider,
+        azure_endpoint=endpoint,
+        api_version="2025-01-01-preview"
+    )
+    
+    # Read and encode audio file  
+    with open('dog.wav', 'rb') as wav_reader: 
+        encoded_string = base64.b64encode(wav_reader.read()).decode('utf-8') 
+    
+    # Initialize messages with the first turn's user input 
+    messages = [
+        { 
+            "role": "user", 
+            "content": [ 
+                { "type": "text", "text": "Describe in detail the spoken audio input." }, 
+                { "type": "input_audio", 
+                    "input_audio": { 
+                        "data": encoded_string, 
+                        "format": "wav" 
+                    } 
+                } 
+            ] 
+        }] 
+    
+    # Get the first turn's response
+    
+    completion = client.chat.completions.create( 
+        model="gpt-4o-audio-preview", 
+        modalities=["text", "audio"], 
+        audio={"voice": "alloy", "format": "wav"}, 
+        messages=messages
+    ) 
+    
+    print("Get the first turn's response:")
+    print(completion.choices[0].message.audio.transcript) 
+    
+    print("Add a history message referencing the first turn's audio by ID:")
+    print(completion.choices[0].message.audio.id)
+    
+    # Add a history message referencing the first turn's audio by ID 
+    messages.append({ 
+        "role": "assistant", 
+        "audio": { "id": completion.choices[0].message.audio.id } 
+    }) 
+    
+    # Add the next turn's user message 
+    messages.append({ 
+        "role": "user", 
+        "content": "Very briefly, summarize the favorability." 
+    }) 
+    
+    # Send the follow-up request with the accumulated messages
+    completion = client.chat.completions.create( 
+        model="gpt-4o-audio-preview", 
+        messages=messages
+    ) 
+    
+    print("Very briefly, summarize the favorability.")
+    print(completion.choices[0].message.content)
+    ```
+
+1. Run the Python file.
+
+    ```shell
+    python multi-turn.py
+    ```
+
+## [API key](#tab/api-key)
+
+1. Create the `multi-turn.py` file with the following code:
+
+    ```python
+    import base64 
+    import os 
+    from openai import AzureOpenAI 
+    
+    # Set environment variables or edit the corresponding values here.
+    endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
+    api_key = os.environ['AZURE_OPENAI_API_KEY']
+    
+    client = AzureOpenAI(
+        api_version="2025-01-01-preview",  
+        api_key=api_key, 
+        azure_endpoint=endpoint
+    )
+    
+    # Read and encode audio file  
+    with open('dog.wav', 'rb') as wav_reader: 
+        encoded_string = base64.b64encode(wav_reader.read()).decode('utf-8') 
+    
+    # Initialize messages with the first turn's user input 
+    messages = [
+        { 
+            "role": "user", 
+            "content": [ 
+                { "type": "text", "text": "Describe in detail the spoken audio input." }, 
+                { "type": "input_audio", 
+                    "input_audio": { 
+                        "data": encoded_string, 
+                        "format": "wav" 
+                    } 
+                } 
+            ] 
+        }] 
+    
+    # Get the first turn's response 
+    
+    completion = client.chat.completions.create( 
+        model="gpt-4o-audio-preview", 
+        modalities=["text", "audio"], 
+        audio={"voice": "alloy", "format": "wav"}, 
+        messages=messages
+    ) 
+    
+    print("Get the first turn's response:")
+    print(completion.choices[0].message.audio.transcript) 
+    
+    print("Add a history message referencing the first turn's audio by ID:")
+    print(completion.choices[0].message.audio.id)
+    
+    # Add a history message referencing the first turn's audio by ID 
+    messages.append({ 
+        "role": "assistant", 
+        "audio": { "id": completion.choices[0].message.audio.id } 
+    }) 
+    
+    # Add the next turn's user message 
+    messages.append({ 
+        "role": "user", 
+        "content": "Very briefly, summarize the favorability." 
+    }) 
+    
+    # Send the follow-up request with the accumulated messages 
+    completion = client.chat.completions.create( 
+        model="gpt-4o-audio-preview", 
+        messages=messages
+    ) 
+    
+    print("Very briefly, summarize the favorability.")
+    print(completion.choices[0].message.content)
+    ```
+
+1. Run the Python file.
+
+    ```shell
+    python multi-turn.py
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+### Output for multi-turn chat completions
+
+The script generates a transcript of the summary of the spoken audio input. Then, it makes a multi-turn chat completion to briefly summarize the spoken audio input. 
+
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Python用音声完了機能に関する新しいドキュメントの追加"
}
```

### Explanation
この変更は、Azure OpenAI SDK for Pythonを使用して音声を生成するためのガイド「audio-completions-python.md」を新たに追加したものです。このドキュメントでは、音声生成を実現するために必要な設定や手順が詳細に説明されています。

まず、Azureのサブスクリプション、Python 3.8以上の環境、Azure OpenAIリソースの展開を準備することが求められています。Microsoft Entra IDを用いた推奨のキーなし認証のための前提条件も詳しく記載されています。次に、Python環境を設定し、必要なパッケージをインストールする手順が示されています。

音声生成のためのスクリプト例が提供されており、ユーザーはテキスト入力を音声に変換する方法や、音声入力からテキストを生成する方法を学ぶことができます。具体的なコード例が含まれ、ユーザーが環境変数を設定し、ファイルを実行することで得られる出力についても説明されています。特に、生成された音声ファイルの取得や、その音声に関連付けられたメッセージの管理方法など、具体的な実装手順が示されています。

また、マルチターンチャット機能の使用方法も説明されており、ユーザーは音声対話をよりインタラクティブに行うことができるようになります。これにより、魅力的な音声アプリケーションをPythonで簡単に構築できる手助けとなる情報が提供されます。

## articles/ai-services/openai/includes/audio-completions-rest.md{#item-0ec305}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,539 @@
+---
+manager: nitinme
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 1/21/2025
+---
+
+[REST API Spec](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference/stable/2024-11-01/inference.json?azure-portal=true) |
+
+[!INCLUDE [Audio completions introduction](audio-completions-intro.md)]
+
+## Prerequisites
+
+- An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
+- <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>. We recommend using Python 3.10 or later, but having at least Python 3.8 is required. If you don't have a suitable version of Python installed, you can follow the instructions in the [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter) for the easiest way of installing Python on your operating system.
+- An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- Then, you need to deploy a `gpt-4o-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+
+## Microsoft Entra ID prerequisites
+
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
+
+## Set up
+
+1. Create a new folder `audio-completions-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
+
+    ```shell
+    mkdir audio-completions-quickstart && code audio-completions-quickstart
+    ```
+    
+1. Create a virtual environment. If you already have Python 3.10 or higher installed, you can create a virtual environment using the following commands:
+    
+    # [Windows](#tab/windows)
+    
+    ```bash
+    py -3 -m venv .venv
+    .venv\scripts\activate
+    ```
+    
+    # [Linux](#tab/linux)
+    
+    ```bash
+    python3 -m venv .venv
+    source .venv/bin/activate
+    ```
+    
+    # [macOS](#tab/macos)
+    
+    ```bash
+    python3 -m venv .venv
+    source .venv/bin/activate
+    ```
+    
+    ---
+    
+    Activating the Python environment means that when you run ```python``` or ```pip``` from the command line, you then use the Python interpreter contained in the ```.venv``` folder of your application. You can use the ```deactivate``` command to exit the python virtual environment, and can later reactivate it when needed.
+
+    > [!TIP]
+    > We recommend that you create and activate a new Python environment to use to install the packages you need for this tutorial. Don't install packages into your global python installation. You should always use a virtual or conda environment when installing python packages, otherwise you can break your global installation of Python.
+
+1. Install the OpenAI client library for Python with:
+
+    ```console
+    pip install openai
+    ```
+
+1. For the **recommended** keyless authentication with Microsoft Entra ID, install the `azure-identity` package with:
+
+    ```console
+    pip install azure-identity
+    ```
+
+
+## Retrieve resource information
+
+[!INCLUDE [resource authentication](resource-authentication.md)]
+
+
+## Generate audio from text input
+
+## [Microsoft Entra ID](#tab/keyless)
+
+1. Create the `to-audio.py` file with the following code:
+
+    ```python
+    import requests
+    import base64 
+    import os 
+    from openai import AzureOpenAI
+    from azure.identity import DefaultAzureCredential
+    
+    # Set environment variables or edit the corresponding values here.
+    endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
+    
+    # Keyless authentication
+    credential = DefaultAzureCredential()
+    token = credential.get_token("https://cognitiveservices.azure.com/.default")
+    
+    api_version = '2025-01-01-preview'
+    url = f"{endpoint}/openai/deployments/gpt-4o-audio-preview/chat/completions?api-version={api_version}"
+    headers= { "Authorization": f"Bearer {token.token}", "Content-Type": "application/json" }
+    body = {
+      "modalities": ["audio", "text"],
+      "model": "gpt-4o-audio-preview",
+      "audio": {
+          "format": "wav",
+          "voice": "alloy"
+      },
+      "messages": [
+        {
+          "role": "user",
+          "content": [
+            {
+              "type": "text",
+              "text": "Is a golden retriever a good family dog?"
+            }
+          ]
+        }
+      ]
+    }
+    
+    # Make the audio chat completions request
+    completion = requests.post(url, headers=headers, json=body)
+    audio_data = completion.json()['choices'][0]['message']['audio']['data']
+    
+    # Write the output audio data to a file
+    wav_bytes = base64.b64decode(audio_data)
+    with open("dog.wav", "wb") as f: 
+      f.write(wav_bytes) 
+    ```
+
+1. Run the Python file.
+
+    ```shell
+    python to-audio.py
+    ```
+
+## [API key](#tab/api-key)
+
+1. Create the `to-audio.py` file with the following code:
+
+    ```python
+    import requests
+    import base64 
+    import os 
+    from openai import AzureOpenAI 
+    
+    # Set environment variables or edit the corresponding values here.
+    endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
+    api_key = os.environ['AZURE_OPENAI_API_KEY']
+    
+    api_version = '2025-01-01-preview'
+    url = f"{endpoint}/openai/deployments/gpt-4o-audio-preview/chat/completions?api-version={api_version}"
+    headers= { "api-key": api_key, "Content-Type": "application/json" }
+    body = {
+      "modalities": ["audio", "text"],
+      "model": "gpt-4o-audio-preview",
+      "audio": {
+          "format": "wav",
+          "voice": "alloy"
+      },
+      "messages": [
+        {
+          "role": "user",
+          "content": [
+            {
+              "type": "text",
+              "text": "Is a golden retriever a good family dog?"
+            }
+          ]
+        }
+      ]
+    }
+    
+    # Make the audio chat completions request
+    completion = requests.post(url, headers=headers, json=body)
+    audio_data = completion.json()['choices'][0]['message']['audio']['data']
+    
+    # Write the output audio data to a file 
+    wav_bytes = base64.b64decode(audio_data)
+    with open("dog.wav", "wb") as f: 
+      f.write(wav_bytes) 
+    ```
+
+1. Run the Python file.
+
+    ```shell
+    python to-audio.py
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+### Output for audio generation from text input
+
+The script generates an audio file named _dog.wav_ in the same directory as the script. The audio file contains the spoken response to the prompt, "Is a golden retriever a good family dog?"
+
+## Generate audio and text from audio input
+
+## [Microsoft Entra ID](#tab/keyless)
+
+1. Create the `from-audio.py` file with the following code:
+
+    ```python
+    import requests
+    import base64
+    import os
+    from azure.identity import DefaultAzureCredential
+    
+    # Set environment variables or edit the corresponding values here.
+    endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
+    
+    # Keyless authentication
+    credential = DefaultAzureCredential()
+    token = credential.get_token("https://cognitiveservices.azure.com/.default")
+    
+    # Read and encode audio file  
+    with open('dog.wav', 'rb') as wav_reader: 
+      encoded_string = base64.b64encode(wav_reader.read()).decode('utf-8') 
+    
+    api_version = '2025-01-01-preview'
+    url = f"{endpoint}/openai/deployments/gpt-4o-audio-preview/chat/completions?api-version={api_version}"
+    headers= { "Authorization": f"Bearer {token.token}", "Content-Type": "application/json" }
+    body = {
+      "modalities": ["audio", "text"],
+      "model": "gpt-4o-audio-preview",
+      "audio": {
+          "format": "wav",
+          "voice": "alloy"
+      },
+      "messages": [
+        { 
+            "role": "user", 
+            "content": [ 
+                {  
+                    "type": "text", 
+                    "text": "Describe in detail the spoken audio input." 
+                }, 
+                { 
+                    "type": "input_audio", 
+                    "input_audio": { 
+                        "data": encoded_string, 
+                        "format": "wav" 
+                    } 
+                } 
+            ] 
+        }, 
+      ]
+    }
+    
+    completion = requests.post(url, headers=headers, json=body)
+    
+    print(completion.json()['choices'][0]['message']['audio']['transcript'])
+    
+    # Write the output audio data to a file
+    audio_data = completion.json()['choices'][0]['message']['audio']['data'] 
+    wav_bytes = base64.b64decode(audio_data)
+    with open("analysis.wav", "wb") as f: 
+      f.write(wav_bytes) 
+    ```
+
+1. Run the Python file.
+
+    ```shell
+    python from-audio.py
+    ```
+
+## [API key](#tab/api-key)
+
+1. Create the `from-audio.py` file with the following code:
+
+    ```python
+    import requests
+    import base64
+    import os
+    
+    # Set environment variables or edit the corresponding values here.
+    endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
+    api_key = os.environ['AZURE_OPENAI_API_KEY']
+    
+    # Read and encode audio file  
+    with open('dog.wav', 'rb') as wav_reader: 
+      encoded_string = base64.b64encode(wav_reader.read()).decode('utf-8') 
+    
+    api_version = '2025-01-01-preview'
+    url = f"{endpoint}/openai/deployments/gpt-4o-audio-preview/chat/completions?api-version={api_version}"
+    headers= { "api-key": api_key, "Content-Type": "application/json" }
+    body = {
+      "modalities": ["audio", "text"],
+      "model": "gpt-4o-audio-preview",
+      "audio": {
+          "format": "wav",
+          "voice": "alloy"
+      },
+      "messages": [
+        { 
+            "role": "user", 
+            "content": [ 
+                {  
+                    "type": "text", 
+                    "text": "Describe in detail the spoken audio input." 
+                }, 
+                { 
+                    "type": "input_audio", 
+                    "input_audio": { 
+                        "data": encoded_string, 
+                        "format": "wav" 
+                    } 
+                } 
+            ] 
+        }, 
+      ]
+    }
+    
+    completion = requests.post(url, headers=headers, json=body)
+    
+    print(completion.json()['choices'][0]['message']['audio']['transcript'])
+    
+    # Write the output audio data to a file
+    audio_data = completion.json()['choices'][0]['message']['audio']['data'] 
+    wav_bytes = base64.b64decode(audio_data)
+    with open("analysis.wav", "wb") as f: 
+      f.write(wav_bytes) 
+    ```
+
+1. Run the Python file.
+
+    ```shell
+    python from-audio.py
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+### Output for audio and text generation from audio input
+
+The script generates a transcript of the summary of the spoken audio input. It also generates an audio file named _analysis.wav_ in the same directory as the script. The audio file contains the spoken response to the prompt.
+
+
+## Generate audio and use multi-turn chat completions
+
+## [Microsoft Entra ID](#tab/keyless)
+
+1. Create the `multi-turn.py` file with the following code:
+
+    ```python
+    import requests
+    import base64 
+    import os 
+    from openai import AzureOpenAI 
+    from azure.identity import DefaultAzureCredential
+    
+    # Set environment variables or edit the corresponding values here.
+    endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
+    
+    # Keyless authentication
+    credential = DefaultAzureCredential()
+    token = credential.get_token("https://cognitiveservices.azure.com/.default")
+    
+    api_version = '2025-01-01-preview'
+    url = f"{endpoint}/openai/deployments/gpt-4o-audio-preview/chat/completions?api-version={api_version}"
+    headers= { "Authorization": f"Bearer {token.token}", "Content-Type": "application/json" }
+    
+    # Read and encode audio file  
+    with open('dog.wav', 'rb') as wav_reader: 
+      encoded_string = base64.b64encode(wav_reader.read()).decode('utf-8') 
+    
+    # Initialize messages with the first turn's user input 
+    messages = [
+        { 
+            "role": "user", 
+            "content": [ 
+                {  
+                    "type": "text", 
+                    "text": "Describe in detail the spoken audio input." 
+                }, 
+                { 
+                    "type": "input_audio", 
+                    "input_audio": { 
+                        "data": encoded_string, 
+                        "format": "wav" 
+                    } 
+                } 
+            ] 
+        }] 
+    
+    body = {
+      "modalities": ["audio", "text"],
+      "model": "gpt-4o-audio-preview",
+      "audio": {
+          "format": "wav",
+          "voice": "alloy"
+      },
+      "messages": messages
+    }
+    
+    # Get the first turn's response, including generated audio 
+    completion = requests.post(url, headers=headers, json=body)
+    
+    print("Get the first turn's response:")
+    print(completion.json()['choices'][0]['message']['audio']['transcript']) 
+    
+    print("Add a history message referencing the first turn's audio by ID:")
+    print(completion.json()['choices'][0]['message']['audio']['id'])
+    
+    # Add a history message referencing the first turn's audio by ID 
+    messages.append({ 
+        "role": "assistant", 
+        "audio": { "id": completion.json()['choices'][0]['message']['audio']['id'] } 
+    }) 
+    
+    # Add the next turn's user message 
+    messages.append({ 
+        "role": "user", 
+        "content": "Very briefly, summarize the favorability." 
+    }) 
+    
+    body = {
+      "model": "gpt-4o-audio-preview",
+      "messages": messages
+    }
+    
+    # Send the follow-up request with the accumulated messages
+    completion = requests.post(url, headers=headers, json=body) 
+    
+    print("Very briefly, summarize the favorability.")
+    print(completion.json()['choices'][0]['message']['content'])
+    ```
+
+1. Run the Python file.
+
+    ```shell
+    python multi-turn.py
+    ```
+
+## [API key](#tab/api-key)
+
+1. Create the `multi-turn.py` file with the following code:
+
+    ```python
+    import requests
+    import base64 
+    import os 
+    from openai import AzureOpenAI 
+    
+    # Set environment variables or edit the corresponding values here.
+    endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
+    api_key = os.environ['AZURE_OPENAI_API_KEY']
+    
+    api_version = '2025-01-01-preview'
+    url = f"{endpoint}/openai/deployments/gpt-4o-audio-preview/chat/completions?api-version={api_version}"
+    headers= { "api-key": api_key, "Content-Type": "application/json" }
+    
+    # Read and encode audio file  
+    with open('dog.wav', 'rb') as wav_reader: 
+      encoded_string = base64.b64encode(wav_reader.read()).decode('utf-8') 
+    
+    # Initialize messages with the first turn's user input 
+    messages = [
+        { 
+            "role": "user", 
+            "content": [ 
+                {  
+                    "type": "text", 
+                    "text": "Describe in detail the spoken audio input." 
+                }, 
+                { 
+                    "type": "input_audio", 
+                    "input_audio": { 
+                        "data": encoded_string, 
+                        "format": "wav" 
+                    } 
+                } 
+            ] 
+        }] 
+    
+    body = {
+      "modalities": ["audio", "text"],
+      "model": "gpt-4o-audio-preview",
+      "audio": {
+          "format": "wav",
+          "voice": "alloy"
+      },
+      "messages": messages
+    }
+    
+    
+    # Get the first turn's response, including generated audio 
+    completion = requests.post(url, headers=headers, json=body)
+    
+    print("Get the first turn's response:")
+    print(completion.json()['choices'][0]['message']['audio']['transcript']) 
+    
+    print("Add a history message referencing the first turn's audio by ID:")
+    print(completion.json()['choices'][0]['message']['audio']['id'])
+    
+    # Add a history message referencing the first turn's audio by ID 
+    messages.append({ 
+        "role": "assistant", 
+        "audio": { "id": completion.json()['choices'][0]['message']['audio']['id'] } 
+    }) 
+    
+    # Add the next turn's user message 
+    messages.append({ 
+        "role": "user", 
+        "content": "Very briefly, summarize the favorability." 
+    }) 
+    
+    body = {
+      "model": "gpt-4o-audio-preview",
+      "messages": messages
+    }
+    
+    # Send the follow-up request with the accumulated messages
+    completion = requests.post(url, headers=headers, json=body) 
+    
+    print("Very briefly, summarize the favorability.")
+    print(completion.json()['choices'][0]['message']['content'])
+    ```
+
+1. Run the Python file.
+
+    ```shell
+    python multi-turn.py
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+### Output for multi-turn chat completions
+
+The script generates a transcript of the summary of the spoken audio input. Then, it makes a multi-turn chat completion to briefly summarize the spoken audio input. 
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "REST APIによる音声完了機能に関する新しいドキュメントの追加"
}
```

### Explanation
この変更は、Azure OpenAIのREST APIを使用して音声を生成するための新しいドキュメント「audio-completions-rest.md」を追加したものです。このドキュメントでは、音声生成のために必要な設定や手順を説明しています。

最初に、AzureサブスクリプションやPythonのインストール、Azure OpenAIリソースの展開が必要であることが強調されています。Microsoft Entra IDを使用したキーなし認証に関する前提条件も説明されており、Azure CLIのインストールと「Cognitive Services User」ロールの割り当てが必要です。

文書には、音声を生成するためのPythonのサンプルコードがいくつか含まれています。コードは、REST APIエンドポイントにリクエストを送信し、音声データを取得してファイルに保存する方法を示しています。ユーザーは、音声データを基にしたチャットの応答を生成したり、音声ファイルを使用してさらなる処理を行うことができます。

また、音声入力からテキストを生成する手順も示されています。多段階のチャット機能を利用する方法に関しても詳しく説明がされており、ユーザーはより高度な対話型の体験を実現できます。全体を通じて、豊富なサンプルコードと手稿が提供されており、開発者が音声完了機能を簡単に実装できるようになっています。

## articles/ai-services/openai/includes/audio-completions-typescript.md{#item-94bc1f}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,753 @@
+---
+manager: nitinme
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 1/21/2025
+---
+
+[Reference documentation](https://platform.openai.com/docs/api-reference/chat) | [Library source code](https://github.com/openai/openai-node?azure-portal=true) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
+
+[!INCLUDE [Audio completions introduction](audio-completions-intro.md)]
+
+## Prerequisites
+
+- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
+- <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
+- [TypeScript](https://www.typescriptlang.org/download/) installed globally.
+- An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- Then, you need to deploy a `gpt-4o-audio-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
+
+## Microsoft Entra ID prerequisites
+
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
+
+## Set up
+
+1. Create a new folder `audio-completions-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
+
+    ```shell
+    mkdir audio-completions-quickstart && code audio-completions-quickstart
+    ```
+    
+
+1. Create the `package.json` with the following command:
+
+    ```shell
+    npm init -y
+    ```
+
+1. Update the `package.json` to ECMAScript with the following command: 
+
+    ```shell
+    npm pkg set type=module
+    ```
+    
+
+1. Install the OpenAI client library for JavaScript with:
+
+    ```console
+    npm install openai
+    ```
+
+1. For the **recommended** keyless authentication with Microsoft Entra ID, install the `@azure/identity` package with:
+
+    ```console
+    npm install @azure/identity
+    ```
+
+
+## Retrieve resource information
+
+[!INCLUDE [resource authentication](resource-authentication.md)]
+
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+    
+## Generate audio from text input
+
+#### [Microsoft Entra ID](#tab/typescript-keyless)
+
+1. Create the `to-audio.ts` file with the following code:
+
+    ```typescript
+    import { writeFileSync } from "node:fs";
+    import { AzureOpenAI } from "openai/index.mjs";
+    import {
+        DefaultAzureCredential,
+        getBearerTokenProvider,
+      } from "@azure/identity";
+    
+    // Set environment variables or edit the corresponding values here.
+    const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const apiVersion: string = "2025-01-01-preview"; 
+    const deployment: string = "gpt-4o-audio-preview"; 
+    
+    // Keyless authentication 
+    const getClient = (): AzureOpenAI => {
+        const credential = new DefaultAzureCredential();
+        const scope = "https://cognitiveservices.azure.com/.default";
+        const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+        const client = new AzureOpenAI({
+          endpoint: endpoint,
+          apiVersion: apiVersion,
+          azureADTokenProvider,
+        });
+        return client;
+    };
+      
+    const client = getClient();
+    
+    async function main(): Promise<void> {
+    
+        // Make the audio chat completions request
+        const response = await client.chat.completions.create({ 
+            model: "gpt-4o-audio-preview", 
+            modalities: ["text", "audio"], 
+            audio: { voice: "alloy", format: "wav" }, 
+            messages: [ 
+            { 
+                role: "user", 
+                content: "Is a golden retriever a good family dog?" 
+            } 
+            ] 
+        }); 
+      
+      // Inspect returned data 
+      console.log(response.choices[0]); 
+      
+      // Write the output audio data to a file
+      if (response.choices[0].message.audio) {
+        writeFileSync( 
+          "dog.wav", 
+          Buffer.from(response.choices[0].message.audio.data, 'base64'), 
+          { encoding: "utf-8" } 
+        ); 
+      } else {
+        console.error("Audio data is null or undefined.");
+      }
+    }
+    
+    main().catch((err: Error) => {
+      console.error("Error occurred:", err);
+    });
+    
+    export { main };
+    ```
+
+1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
+
+    ```json
+    {
+        "compilerOptions": {
+          "module": "NodeNext",
+          "target": "ES2022", // Supports top-level await
+          "moduleResolution": "NodeNext",
+          "skipLibCheck": true, // Avoid type errors from node_modules
+          "strict": true // Enable strict type-checking options
+        },
+        "include": ["*.ts"]
+    }
+    ```
+
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
+    tsc
+    ```
+    
+1. Sign in to Azure with the following command:
+
+    ```shell
+    az login
+    ```
+
+1. Run the code with the following command:
+
+    ```shell
+    node to-audio.js
+    ```
+
+#### [API key](#tab/typescript-key)
+
+1. Create the `to-audio.ts` file with the following code:
+
+    ```typescript
+    import { writeFileSync } from "node:fs";
+    import { AzureOpenAI } from "openai/index.mjs";
+    
+    // Set environment variables or edit the corresponding values here.
+    const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const apiKey: string = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
+    const apiVersion: string = "2025-01-01-preview"; 
+    const deployment: string = "gpt-4o-audio-preview"; 
+    
+    const client = new AzureOpenAI({ 
+      endpoint, 
+      apiKey, 
+      apiVersion, 
+      deployment 
+    });  
+    
+    async function main(): Promise<void> {
+    
+        // Make the audio chat completions request
+        const response = await client.chat.completions.create({ 
+            model: "gpt-4o-audio-preview", 
+            modalities: ["text", "audio"], 
+            audio: { voice: "alloy", format: "wav" }, 
+            messages: [ 
+            { 
+                role: "user", 
+                content: "Is a golden retriever a good family dog?" 
+            } 
+            ] 
+        }); 
+      
+      // Inspect returned data 
+      console.log(response.choices[0]); 
+      
+      // Write the output audio data to a file
+      if (response.choices[0].message.audio) {
+        writeFileSync( 
+          "dog.wav", 
+          Buffer.from(response.choices[0].message.audio.data, 'base64'), 
+          { encoding: "utf-8" } 
+        ); 
+      } else {
+        console.error("Audio data is null or undefined.");
+      }
+    }
+    
+    main().catch((err: Error) => {
+      console.error("Error occurred:", err);
+    });
+    
+    export { main };
+    ```
+
+1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
+
+    ```json
+    {
+        "compilerOptions": {
+          "module": "NodeNext",
+          "target": "ES2022", // Supports top-level await
+          "moduleResolution": "NodeNext",
+          "skipLibCheck": true, // Avoid type errors from node_modules
+          "strict": true // Enable strict type-checking options
+        },
+        "include": ["*.ts"]
+    }
+    ```
+
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
+    tsc
+    ```
+
+1. Run the code with the following command:
+
+    ```shell
+    node to-audio.js
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+### Output for audio generation from text input
+
+The script generates an audio file named _dog.wav_ in the same directory as the script. The audio file contains the spoken response to the prompt, "Is a golden retriever a good family dog?"
+
+## Generate audio and text from audio input
+
+#### [Microsoft Entra ID](#tab/typescript-keyless)
+
+1. Create the `from-audio.ts` file with the following code:
+
+    ```typescript
+    import { AzureOpenAI } from "openai";
+    import { writeFileSync } from "node:fs";
+    import { promises as fs } from 'fs';
+    import {
+        DefaultAzureCredential,
+        getBearerTokenProvider,
+      } from "@azure/identity";
+    
+    // Set environment variables or edit the corresponding values here.
+    const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const apiVersion: string = "2025-01-01-preview"; 
+    const deployment: string = "gpt-4o-audio-preview"; 
+    
+    // Keyless authentication 
+    const getClient = (): AzureOpenAI => {
+        const credential = new DefaultAzureCredential();
+        const scope = "https://cognitiveservices.azure.com/.default";
+        const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+        const client = new AzureOpenAI({
+          endpoint: endpoint,
+          apiVersion: apiVersion,
+          azureADTokenProvider,
+        });
+        return client;
+    };
+      
+    const client = getClient();
+    
+    async function main(): Promise<void> {
+    
+        // Buffer the audio for input to the chat completion
+        const wavBuffer = await fs.readFile("dog.wav"); 
+        const base64str = Buffer.from(wavBuffer).toString("base64"); 
+        
+        // Make the audio chat completions request
+        const response = await client.chat.completions.create({ 
+          model: "gpt-4o-audio-preview",
+          modalities: ["text", "audio"], 
+          audio: { voice: "alloy", format: "wav" },
+          messages: [ 
+            { 
+              role: "user", 
+              content: [ 
+                { 
+                  type: "text", 
+                  text: "Describe in detail the spoken audio input." 
+                }, 
+                { 
+                  type: "input_audio", 
+                  input_audio: { 
+                    data: base64str, 
+                    format: "wav" 
+                  } 
+                } 
+              ] 
+            } 
+          ] 
+        }); 
+        
+        console.log(response.choices[0]); 
+     
+        // Write the output audio data to a file
+        if (response.choices[0].message.audio) {
+            writeFileSync("analysis.wav", Buffer.from(response.choices[0].message.audio.data, 'base64'), { encoding: "utf-8" });
+        }
+        else {
+            console.error("Audio data is null or undefined.");
+      }
+    }
+    
+    main().catch((err: Error) => {
+      console.error("Error occurred:", err);
+    });
+    
+    export { main };
+    ```
+
+1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
+
+    ```json
+    {
+        "compilerOptions": {
+          "module": "NodeNext",
+          "target": "ES2022", // Supports top-level await
+          "moduleResolution": "NodeNext",
+          "skipLibCheck": true, // Avoid type errors from node_modules
+          "strict": true // Enable strict type-checking options
+        },
+        "include": ["*.ts"]
+    }
+    ```
+
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
+    tsc
+    ```
+    
+1. Sign in to Azure with the following command:
+
+    ```shell
+    az login
+    ```
+
+1. Run the code with the following command:
+
+    ```shell
+    node from-audio.js
+    ```
+
+#### [API key](#tab/typescript-key)
+
+1. Create the `from-audio.ts` file with the following code:
+
+    ```typescript
+    import { AzureOpenAI } from "openai";
+    import { writeFileSync } from "node:fs";
+    import { promises as fs } from 'fs';
+    
+    // Set environment variables or edit the corresponding values here.
+    const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const apiKey: string = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
+    const apiVersion: string = "2025-01-01-preview"; 
+    const deployment: string = "gpt-4o-audio-preview"; 
+    
+    const client = new AzureOpenAI({ 
+      endpoint, 
+      apiKey, 
+      apiVersion, 
+      deployment 
+    });  
+    
+    async function main(): Promise<void> {
+    
+      // Buffer the audio for input to the chat completion
+      const wavBuffer = await fs.readFile("dog.wav"); 
+      const base64str = Buffer.from(wavBuffer).toString("base64"); 
+      
+      // Make the audio chat completions request
+      const response = await client.chat.completions.create({ 
+        model: "gpt-4o-audio-preview",
+        modalities: ["text", "audio"], 
+        audio: { voice: "alloy", format: "wav" },
+        messages: [ 
+          { 
+            role: "user", 
+            content: [ 
+              { 
+                type: "text", 
+                text: "Describe in detail the spoken audio input." 
+              }, 
+              { 
+                type: "input_audio", 
+                input_audio: { 
+                  data: base64str, 
+                  format: "wav" 
+                } 
+              } 
+            ] 
+          } 
+        ] 
+      }); 
+      
+      console.log(response.choices[0]); 
+    
+      // Write the output audio data to a file
+      if (response.choices[0].message.audio) {
+          writeFileSync("analysis.wav", Buffer.from(response.choices[0].message.audio.data, 'base64'), { encoding: "utf-8" });
+      }
+      else {
+          console.error("Audio data is null or undefined.");
+    }
+    }
+    
+    main().catch((err: Error) => {
+    console.error("Error occurred:", err);
+    });
+    
+    export { main };
+    ```
+
+1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
+
+    ```json
+    {
+        "compilerOptions": {
+          "module": "NodeNext",
+          "target": "ES2022", // Supports top-level await
+          "moduleResolution": "NodeNext",
+          "skipLibCheck": true, // Avoid type errors from node_modules
+          "strict": true // Enable strict type-checking options
+        },
+        "include": ["*.ts"]
+    }
+    ```
+
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
+    tsc
+    ```
+
+1. Run the code with the following command:
+
+    ```shell
+    node from-audio.js
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+### Output for audio and text generation from audio input
+
+The script generates a transcript of the summary of the spoken audio input. It also generates an audio file named _analysis.wav_ in the same directory as the script. The audio file contains the spoken response to the prompt.
+
+## Generate audio and use multi-turn chat completions
+
+#### [Microsoft Entra ID](#tab/typescript-keyless)
+
+1. Create the `multi-turn.ts` file with the following code:
+
+    ```typescript
+    import { AzureOpenAI } from "openai/index.mjs";
+    import { promises as fs } from 'fs';
+    import { ChatCompletionMessageParam } from "openai/resources/index.mjs";
+    import {
+        DefaultAzureCredential,
+        getBearerTokenProvider,
+      } from "@azure/identity";
+    
+    // Set environment variables or edit the corresponding values here.
+    const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const apiVersion: string = "2025-01-01-preview"; 
+    const deployment: string = "gpt-4o-audio-preview"; 
+    
+    // Keyless authentication 
+    const getClient = (): AzureOpenAI => {
+        const credential = new DefaultAzureCredential();
+        const scope = "https://cognitiveservices.azure.com/.default";
+        const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+        const client = new AzureOpenAI({
+          endpoint: endpoint,
+          apiVersion: apiVersion,
+          azureADTokenProvider,
+        });
+        return client;
+    };
+      
+    const client = getClient(); 
+    
+    async function main(): Promise<void> {
+    
+        // Buffer the audio for input to the chat completion
+        const wavBuffer = await fs.readFile("dog.wav"); 
+        const base64str = Buffer.from(wavBuffer).toString("base64"); 
+      
+        // Initialize messages with the first turn's user input 
+        const messages: ChatCompletionMessageParam[] = [
+          {
+            role: "user",
+            content: [
+              { 
+                type: "text", 
+                text: "Describe in detail the spoken audio input." 
+              },
+              { 
+                type: "input_audio", 
+                input_audio: { 
+                  data: base64str, 
+                  format: "wav" 
+                } 
+              }
+            ]
+          }
+        ];
+        
+        // Get the first turn's response 
+    
+        const response = await client.chat.completions.create({ 
+            model: "gpt-4o-audio-preview",
+            modalities: ["text", "audio"], 
+            audio: { voice: "alloy", format: "wav" }, 
+            messages: messages
+        }); 
+        
+        console.log(response.choices[0]); 
+        
+        // Add a history message referencing the previous turn's audio by ID 
+        messages.push({ 
+            role: "assistant", 
+            audio: response.choices[0].message.audio ? { id: response.choices[0].message.audio.id } : undefined
+        });
+    
+        // Add a new user message for the second turn
+        messages.push({ 
+            role: "user", 
+            content: [ 
+                { 
+                  type: "text", 
+                  text: "Very concisely summarize the favorability." 
+                } 
+            ] 
+        }); 
+    
+        // Send the follow-up request with the accumulated messages
+        const followResponse = await client.chat.completions.create({ 
+            model: "gpt-4o-audio-preview",
+            messages: messages
+        });
+    
+        console.log(followResponse.choices[0].message.content); 
+    }
+    
+    main().catch((err: Error) => {
+      console.error("Error occurred:", err);
+    });
+    
+    export { main };
+    ```
+
+1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
+
+    ```json
+    {
+        "compilerOptions": {
+          "module": "NodeNext",
+          "target": "ES2022", // Supports top-level await
+          "moduleResolution": "NodeNext",
+          "skipLibCheck": true, // Avoid type errors from node_modules
+          "strict": true // Enable strict type-checking options
+        },
+        "include": ["*.ts"]
+    }
+    ```
+
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
+    tsc
+    ```
+    
+1. Sign in to Azure with the following command:
+
+    ```shell
+    az login
+    ```
+
+1. Run the code with the following command:
+
+    ```shell
+    node multi-turn.js
+    ```
+
+#### [API key](#tab/typescript-key)
+
+1. Create the `multi-turn.ts` file with the following code:
+
+    ```typescript
+    import { AzureOpenAI } from "openai/index.mjs";
+    import { promises as fs } from 'fs';
+    import { ChatCompletionMessageParam } from "openai/resources/index.mjs";
+    
+    // Set environment variables or edit the corresponding values here.
+    const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT" as string;
+    const apiKey: string = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
+    const apiVersion: string = "2025-01-01-preview"; 
+    const deployment: string = "gpt-4o-audio-preview"; 
+    
+    const client = new AzureOpenAI({ 
+      endpoint, 
+      apiKey, 
+      apiVersion, 
+      deployment 
+    });  
+    
+    async function main(): Promise<void> {
+    
+        // Buffer the audio for input to the chat completion
+        const wavBuffer = await fs.readFile("dog.wav"); 
+        const base64str = Buffer.from(wavBuffer).toString("base64"); 
+    
+        // Initialize messages with the first turn's user input 
+        const messages: ChatCompletionMessageParam[] = [
+          {
+            role: "user",
+            content: [
+              { 
+                type: "text", 
+                text: "Describe in detail the spoken audio input." 
+              },
+              { 
+                type: "input_audio", 
+                input_audio: { 
+                  data: base64str, 
+                  format: "wav" 
+                } 
+              }
+            ]
+          }
+        ];
+        
+        // Get the first turn's response 
+        
+        const response = await client.chat.completions.create({ 
+          model: "gpt-4o-audio-preview",
+          modalities: ["text", "audio"], 
+          audio: { voice: "alloy", format: "wav" }, 
+          messages: messages
+        }); 
+        
+        console.log(response.choices[0]); 
+        
+        // Add a history message referencing the previous turn's audio by ID 
+        messages.push({ 
+            role: "assistant", 
+            audio: response.choices[0].message.audio ? { id: response.choices[0].message.audio.id } : undefined
+        });
+    
+        // Add a new user message for the second turn
+        messages.push({ 
+            role: "user", 
+            content: [ 
+                { 
+                  type: "text", 
+                  text: "Very concisely summarize the favorability." 
+                } 
+            ] 
+        }); 
+    
+        // Send the follow-up request with the accumulated messages
+        const followResponse = await client.chat.completions.create({ 
+            model: "gpt-4o-audio-preview",
+            messages: messages
+        });
+    
+        console.log(followResponse.choices[0].message.content); 
+    }
+    
+    main().catch((err: Error) => {
+      console.error("Error occurred:", err);
+    });
+    
+    export { main };
+    ```
+
+1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
+
+    ```json
+    {
+        "compilerOptions": {
+          "module": "NodeNext",
+          "target": "ES2022", // Supports top-level await
+          "moduleResolution": "NodeNext",
+          "skipLibCheck": true, // Avoid type errors from node_modules
+          "strict": true // Enable strict type-checking options
+        },
+        "include": ["*.ts"]
+    }
+    ```
+
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
+    tsc
+    ```
+
+1. Run the code with the following command:
+
+    ```shell
+    node multi-turn.js
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+### Output for multi-turn chat completions
+
+The script generates a transcript of the summary of the spoken audio input. Then, it makes a multi-turn chat completion to briefly summarize the spoken audio input. 
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "TypeScriptによる音声完了機能に関する新しいドキュメントの追加"
}
```

### Explanation
この変更は、Azure OpenAIの音声完了機能をTypeScriptで利用するための新しいドキュメント「audio-completions-typescript.md」を追加した内容です。このドキュメントでは、音声生成における手順や必要な準備について詳しく説明しています。

最初に、AzureサブスクリプションやNode.jsのインストール、TypeScriptのグローバルインストールなど、システムの前提条件が明確に示されています。また、Microsoft Entra IDを使用したキーなし認証の設定についても説明しており、Azure CLIのインストールと適切なロールの割り当てが必要です。

ドキュメントには、音声を生成するためのTypeScriptコードが含まれており、具体的には、ユーザーからのテキスト入力を基に音声データを生成し、ファイルに保存する手順が示されています。また、生成された音声入力を解析して、さらなるテキスト出力を得るためのマルチターン対話の実装方法も取り上げています。

各コードブロックには、環境設定やエラーハンドリングの方法も含まれ、ユーザーが自身の環境で簡単に音声処理アプリケーションを構築できるように設計されています。この新しいドキュメントは、TypeScriptを使用した音声アプリケーション開発において非常に役立つリソースとなります。

## articles/ai-services/openai/includes/chatgpt-javascript.md{#item-cbf09f}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
@@ -56,7 +56,7 @@ Your app's _package.json_ file is updated with the dependencies.
 Open a command prompt where you want the new project, and create a new file named ChatCompletion.js. Copy the following code into the ChatCompletion.js file.
 
 
-## [Microsoft Entra ID](#tab/javascript-keyless)
+## [Microsoft Entra ID](#tab/keyless)
 
 ```javascript
 const { AzureOpenAI } = require("openai");
@@ -108,7 +108,7 @@ node.exe ChatCompletion.js
 ```
 
 
-## [API key](#tab/javascript-key)
+## [API key](#tab/api-key)
 
 ```javascript
 const { AzureOpenAI } = require("openai");
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ChatGPT用JavaScriptドキュメントの修正"
}
```

### Explanation
この変更は、ChatGPTのJavaScriptに関するドキュメント「chatgpt-javascript.md」の内容を修正したものです。主な変更点は、リソース認証に関するリンクの更新と、セクションタイトルの一部における用語の統一です。

具体的には、Microsoft Entra IDに関連するセクションの見出しが修正され、より一貫性のあるリンクが設定されました。また、APIキーのセクションの見出しも更新され、リンクの名前が適切に見直されています。これにより、読者が必要な情報をより簡単に見つけられるようになり、全体的なドキュメントの整合性が向上しました。

これらの変更は主に文書の可読性や整合性に寄与するものであり、機能的な変更は伴っていませんが、ユーザーの体験をより良くするための重要な更新です。

## articles/ai-services/openai/includes/chatgpt-typescript.md{#item-6d2f1f}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ChatGPT用TypeScriptドキュメントの修正"
}
```

### Explanation
この変更は、ChatGPTのTypeScriptに関するドキュメント「chatgpt-typescript.md」に対する軽微な修正です。具体的には、リソース認証に関するリンクが変更されました。

変更内容としては、元々のリンク「resource-auth.md」が「resource-authentication.md」に修正されています。これにより、読者は正しいリソース認証情報にアクセスできるようになります。この修正はドキュメントの整合性を高め、ユーザーが必要な情報をより容易に見つけられるようにするための重要な改善です。

全体として、この変更はドキュメントの可読性や信頼性を向上させるためのものですが、機能そのものには影響を与えません。

## articles/ai-services/openai/includes/dall-e-javascript.md{#item-6cffcf}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
@@ -59,7 +59,7 @@ Create a new file named _ImageGeneration.js_ and open it in your preferred code
 
 
 
-#### [Microsoft Entra ID](#tab/javascript-keyless)
+#### [Microsoft Entra ID](#tab/keyless)
 
 ```javascript
 const { AzureOpenAI } = require("openai");
@@ -123,7 +123,7 @@ node ImageGeneration.js
 
 
 
-#### [API key](#tab/javascript-key)
+#### [API key](#tab/api-key)
 
 ```javascript
 const { AzureOpenAI } = require("openai");
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL-E用JavaScriptドキュメントの修正"
}
```

### Explanation
この変更は、DALL-Eに関連するJavaScriptのドキュメント「dall-e-javascript.md」の更新です。変更内容には、リソース認証に関するリンクの修正とセクションタイトルの一部の見直しが含まれています。

具体的には、リソース認証のセクションで、元々のリンク「resource-auth.md」が「resource-authentication.md」に修正されました。これは、文書内の情報へのアクセスを容易にし、リンクの整合性を向上させるためのものです。

さらに、Microsoft Entra IDとAPIキーに関する見出しもそれぞれ「javascript-keyless」から「keyless」、および「javascript-key」から「api-key」に変更され、これにより直感的で標準的な用語が使用されるようになりました。これらの修正により、ユーザーは必要な情報をより簡単に見つけられるようになり、全体的なドキュメントの整合性が向上します。

全体として、この変更はドキュメントの明確さと可読性の向上を目的としていますが、機能には影響を与えていません。

## articles/ai-services/openai/includes/dall-e-typescript.md{#item-57b205}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL-E用TypeScriptドキュメントの修正"
}
```

### Explanation
この変更は、DALL-Eに関連するTypeScriptのドキュメント「dall-e-typescript.md」に対する軽微な修正です。主な変更点は、リソース認証に関するリンクの更新にあります。

具体的には、以前は「resource-auth.md」というリンクが使用されていましたが、これが「resource-authentication.md」に置き換えられています。この修正により、リソース認証に関する情報へのリンクが正確かつ最新のものとなり、ユーザーが必要な情報を容易に入手できるようになります。

この修正は、ドキュメントの正確性と整合性を向上させることを目的としていますが、機能面には影響を与えません。全体的に、この変更はドキュメントの可読性を高め、ユーザー体験を改善するためのものであると言えます。

## articles/ai-services/openai/includes/gpt-v-javascript.md{#item-a128c9}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
@@ -62,7 +62,7 @@ Your app's _package.json_ file will be updated with the dependencies.
 Select an image from the [azure-samples/cognitive-services-sample-data-files](https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images) and set the URL for an image in the environment variables.
 
 
-## [Microsoft Entra ID](#tab/javascript-keyless)
+## [Microsoft Entra ID](#tab/keyless)
 
 1. Replace the contents of _quickstart.js_ with the following code. 
     
@@ -150,7 +150,7 @@ Select an image from the [azure-samples/cognitive-services-sample-data-files](ht
 
 
 
-## [API key](#tab/javascript-key)
+## [API key](#tab/api-key)
 
 1. Replace the contents of _quickstart.js_ with the following code. 
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-V用JavaScriptドキュメントの修正"
}
```

### Explanation
この変更は、GPT-Vに関連するJavaScriptのドキュメント「gpt-v-javascript.md」の軽微な修正です。主な変更点は、リソース認証に関するリンクの修正とセクションタイトルの見直しにあります。

具体的には、リソース認証を参照するリンクが「resource-auth.md」から「resource-authentication.md」へと変更され、情報の正確さが向上しています。また、Microsoft Entra IDおよびAPIキーに関するセクションの見出しでも、元々の「javascript-keyless」と「javascript-key」がそれぞれ「keyless」と「api-key」に修正されました。これにより、セクションタイトルがより直感的で意味のあるものとなり、ユーザーが必要な情報をより理解しやすくなります。

全体として、この変更はドキュメントの正確性、整合性、および可読性を向上させるものであり、ユーザー体験の向上に寄与しますが、機能に対する影響はありません。

## articles/ai-services/openai/includes/gpt-v-typescript.md{#item-03ec34}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-V用TypeScriptドキュメントの修正"
}
```

### Explanation
この変更は、GPT-Vに関連するTypeScriptのドキュメント「gpt-v-typescript.md」に対する軽微な修正です。主な変更点は、リソース認証に関するリンクの名称変更です。

具体的には、以前のリンク「resource-auth.md」が「resource-authentication.md」に更新されました。この修正により、文書内での情報への参照がより正確になり、ユーザーは必要なリソース認証に関する情報を容易に見つけることができるようになります。

この変更は、ドキュメントの整合性と正確性を向上させることを目的としており、機能的な影響はありませんが、より良いユーザー体験を提供することに寄与します。

## articles/ai-services/openai/includes/javascript.md{#item-f4828f}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ ms.date: 10/22/2024
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
@@ -49,7 +49,7 @@ Your app's _package.json_ file is updated with the dependencies.
 Open a command prompt where you created the new project, and create a new file named Completion.js. Copy the following code into the Completion.js file.
 
 
-## [Microsoft Entra ID](#tab/javascript-keyless)
+## [Microsoft Entra ID](#tab/keyless)
 
 ```javascript
 const { AzureOpenAI } = require("openai");
@@ -96,7 +96,7 @@ node.exe Completion.js
 ```
 
 
-## [API key](#tab/javascript-key)
+## [API key](#tab/api-key)
 
 ```javascript
 const { AzureOpenAI } = require("openai");
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptドキュメントの修正"
}
```

### Explanation
この変更は、JavaScriptに関するドキュメント「javascript.md」に対して行われた軽微な修正です。主な変更点は、リソース認証に関連するリンクの名称修正と、いくつかのセクションタイトルの変更にあります。

具体的には、リソース認証のリンクが「resource-auth.md」から「resource-authentication.md」に変更され、より明確で正確な情報への指針が提供されます。また、「Microsoft Entra ID」に関するセクションのタイトルが「javascript-keyless」から「keyless」に変更され、「API key」に関するセクションも「javascript-key」から「api-key」に修正されました。これにより、ユーザーは各セクションの内容をより容易に理解できるようになります。

この変更は、ドキュメント内の情報の整合性と可読性を向上させるものであり、ユーザー体験の向上に寄与しますが、機能に対しては影響を与えません。

## articles/ai-services/openai/includes/language-overview/dotnet.md{#item-46e881}

<details>
<summary>Diff</summary>
````diff
@@ -9,22 +9,22 @@ ms.date: 11/18/2024
 ---
 
 
-The Azure OpenAI client library for .NET is a companion to the [official OpenAI client library for .NET](https://github.com/openai/openai-dotnet). The Azure OpenAI library configures a client for use with Azure OpenAI and provides additional strongly typed extension support for request and response models specific to Azure OpenAI scenarios.
+The Azure OpenAI client library for .NET is a companion to the [official OpenAI client library for .NET](https://github.com/openai/openai-dotnet). The Azure OpenAI library configures a client for use with Azure OpenAI and provides extra strongly typed extension support for request and response models specific to Azure OpenAI scenarios.
 
 ### Stable release: 
 
 [Source code](https://github.com/Azure/azure-sdk-for-net/blob/Azure.AI.OpenAI_2.0.0/sdk/openai/Azure.AI.OpenAI/src) | [Package (NuGet)](https://www.nuget.org/packages/Azure.AI.OpenAI) | [Package reference documentation](/dotnet/api/overview/azure/ai.openai-readme?view=azure-dotnet&preserve-view=true) [API reference documentation](../../reference.md) |  [Samples](https://github.com/Azure/azure-sdk-for-net/blob/Azure.AI.OpenAI_2.0.0/sdk/openai/Azure.AI.OpenAI/tests/Samples)
  
 ### Preview release: 
 
-The preview release will have access to the latest features.
+The preview release has access to the latest features.
 
 [Source code](https://github.com/Azure/azure-sdk-for-net/tree/Azure.AI.OpenAI_2.1.0-beta.2/sdk/openai/Azure.AI.OpenAI/src) | [Package (NuGet)](https://www.nuget.org/packages/Azure.AI.OpenAI/2.1.0-beta.2) | [API reference documentation](../../reference.md) | [Package reference documentation](/dotnet/api/overview/azure/ai.openai-readme?view=azure-dotnet-preview&preserve-view=true)   [Samples](https://github.com/Azure/azure-sdk-for-net/tree/Azure.AI.OpenAI_2.1.0-beta.2/sdk/openai/Azure.AI.OpenAI/tests/Samples)
 
 
 ## Azure OpenAI API version support
 
-Unlike the Azure OpenAI client libraries for Python and JavaScript, the Azure OpenAI .NET package is limited to targeting a specific subset of the Azure OpenAI API versions. Generally each Azure OpenAI .NET package will unlock access to newer Azure OpenAI API release features. Having access to the latest API versions impacts feature availability.
+Unlike the Azure OpenAI client libraries for Python and JavaScript, the Azure OpenAI .NET package is limited to targeting a specific subset of the Azure OpenAI API versions. Generally each Azure OpenAI .NET package unlocks access to newer Azure OpenAI API release features. Having access to the latest API versions impacts feature availability.
 
 Version selection is controlled by the [`AzureOpenAIClientOptions.ServiceVersion`](/dotnet/api/azure.ai.openai.azureopenaiclientoptions.serviceversion?view=azure-dotnet&preserve-view=true) enum.
 
@@ -260,7 +260,7 @@ bytes.ToStream().CopyTo(stream);
 
 ```
 
-- [C# DALL-E quickstart guide](/azure/ai-services/openai/dall-e-quickstart?tabs=dalle3%2Ccommand-line%2Cjavascript-keyless%2Ctypescript-keyless&pivots=programming-language-csharp)
+- [C# DALL-E quickstart guide](/azure/ai-services/openai/dall-e-quickstart?tabs=dalle3%2Ccommand-line%2Ckeyless%2Ctypescript-keyless&pivots=programming-language-csharp)
 
 
 ## Completions (legacy)
@@ -286,7 +286,7 @@ Not supported with the Azure OpenAI .NET packages.
 
 ### Retries
 
-The client classes will automatically retry the following errors up to three additional times using exponential backoff:
+The client classes will automatically retry the following errors up to three more times using exponential backoff:
 
 - 408 Request Timeout
 - 429 Too Many Requests
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": ".NET用Azure OpenAIクライアントライブラリの文書修正"
}
```

### Explanation
この変更は、Azure OpenAIクライアントライブラリに関するドキュメント「dotnet.md」に対する軽微な修正です。主な修正点は、文の表現の改善やリンクの更新です。

具体的には、以下の変更が行われました：
- 「extra strongly typed extension support」への表現の修正や、「will have access」から「has access」への文の更新が行われ、文章がより明潔で現在形に統一されています。
- PythonおよびJavaScript用のAzure OpenAIクライアントライブラリとの相違点についての説明においても、文の自然さを優先した修正がなされています。
- DALL-Eに関するクイックスタートガイドへのリンクも、クエリパラメータの一部が変更されました。

これらの修正により、情報の正確性と可読性が向上し、ユーザーがライブラリの使い方や特性に関してより明確に理解できるようになります。全体として、この変更はユーザー体験を向上させるものですが、機能自体には影響を与えません。

## articles/ai-services/openai/includes/realtime-deploy-model.md{#item-21f911}

<details>
<summary>Diff</summary>
````diff
@@ -4,14 +4,14 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 12/26/2024
+ms.date: 1/21/2025
 ---
 
 To deploy the `gpt-4o-realtime-preview` model in the Azure AI Foundry portal:
-1. Go to the [Azure AI Foundry portal](https://ai.azure.com) and make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource (with or without model deployments.)
+1. Go to the [Azure OpenAI Service page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource (with or without model deployments.)
 1. Select the **Real-time audio** playground from under **Playgrounds** in the left pane.
-1. Select **Create new deployment** to open the deployment window. 
-1. Search for and select the `gpt-4o-realtime-preview` model and then select **Confirm**.
+1. Select **+ Create new deployment** > **From base models** to open the deployment window. 
+1. Search for and select the `gpt-4o-realtime-preview` model and then select **Deploy to selected resource**.
 1. In the deployment wizard, select the `2024-12-17` model version.
 1. Follow the wizard to finish deploying the model.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムモデルデプロイメント手順の更新"
}
```

### Explanation
この変更は、Azure AI Foundryポータルにおける`gpt-4o-realtime-preview`モデルのデプロイメント手順を説明する文書「realtime-deploy-model.md」に対する軽微な修正です。主な変更は、手順の明確化と日付の更新です。

具体的な変更点は以下の通りです：
- 文書の日付が「12/26/2024」から「1/21/2025」へ変更され、更新されたことを反映しています。
- Azure AI Foundryポータルへのアクセス手順が「Azure AI Foundry portal」から「Azure OpenAI Service page」に修正され、より具体的なページが示されています。
- 「Create new deployment」の手順が「+ Create new deployment > From base models」という形に変更され、インターフェースの操作をより明確に説明する内容に改善されています。また、「Confirm」から「Deploy to selected resource」へ変更され、ユーザーがどのボタンを押すべきかを具体的に示しています。

これらの修正により、手順の正確性と可読性が向上し、ユーザーがスムーズにモデルをデプロイできるようにサポートします。全体として、これらの変更はユーザー体験を向上させるもので、機能自体には影響を与えません。

## articles/ai-services/openai/includes/realtime-javascript.md{#item-3c125e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 12/26/2024
+ms.date: 1/21/2025
 ---
 
 ## Prerequisites
@@ -59,7 +59,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript用リアルタイムガイドの文書修正"
}
```

### Explanation
この変更は、JavaScript用のリアルタイム機能に関する文書「realtime-javascript.md」に対する軽微な修正です。主な変更は、日付の更新と文書内のリンクの修正です。

具体的な変更点は以下の通りです：
- 文書の日付が「12/26/2024」から「1/21/2025」に更新され、最新の情報を反映しています。
- リソース情報を取得するセクションにおけるリンクが「resource-auth.md」から「resource-authentication.md」へ修正されました。これはリンク先が正確になっていると考えられるため、ユーザーが正しい情報にアクセスできるようになります。

これらの修正により、ドキュメントの正確性と一貫性が向上しています。全体として、これらの変更はユーザー体験を改善するものであり、機能や手順そのものには影響を与えません。

## articles/ai-services/openai/includes/realtime-portal.md{#item-1b81a2}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 12/26/2024
+ms.date: 1/21/2025
 ---
 
 ## Deploy a model for real-time audio
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムポータルガイドの日付更新"
}
```

### Explanation
この変更は、リアルタイムポータルに関する文書「realtime-portal.md」に対する軽微な修正を示しています。修正点は主に日付の更新です。

具体的には、以下の変更が行われました：
- 文書の日付が「12/26/2024」から「1/21/2025」へと更新され、最新の情報が反映されています。

この更新は文書の正確性を保つため重要であり、ユーザーに最新のドキュメントを提供することに寄与します。全体として、この変更は内容の機能や手順に影響を与えず、ユーザーが信頼できる最新の情報を得られるようにするためのものです。

## articles/ai-services/openai/includes/realtime-python.md{#item-1291c0}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 12/26/2024
+ms.date: 1/21/2025
 ---
 
 ## Prerequisites
@@ -76,7 +76,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 ## Text in audio out
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムPythonガイドの日付更新とリンク修正"
}
```

### Explanation
この変更は、リアルタイムPythonに関する文書「realtime-python.md」に対する軽微な修正を示しています。これらの変更は、主に日付の更新とリンクの修正に関連しています。

具体的な変更点は以下の通りです：
- 文書の日付が「12/26/2024」から「1/21/2025」に更新され、最新の情報を反映しています。
- リソース情報を取得するセクションにおいて、リンクが「resource-auth.md」から「resource-authentication.md」へ修正されました。これにより、ユーザーが正確で最新の情報にアクセスできるようになります。

これらの変更によって、ドキュメントの正確性が向上し、ユーザー体験が改善されます。全体として、これらの修正は機能や手順そのものには影響を与えない軽微なものであり、情報の信頼性を高めることを目的としています。

## articles/ai-services/openai/includes/realtime-typescript.md{#item-eacc9c}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 12/26/2024
+ms.date: 1/21/2025
 ---
 
 ## Prerequisites
@@ -60,7 +60,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムTypeScriptガイドの日付更新とリンク修正"
}
```

### Explanation
この変更は、リアルタイムTypeScriptに関する文書「realtime-typescript.md」に対する軽微な修正を示しています。この修正では、主に日付の更新とリンクの修正が行われています。

具体的な変更点は以下の通りです：
- 文書の日付が「12/26/2024」から「1/21/2025」に更新されており、最新の情報が反映されています。
- リソース情報を取得するセクションにおいて、リンクが「resource-auth.md」から「resource-authentication.md」に修正されました。これにより、正確で信頼性のある情報へのアクセスが向上します。

これらの変更は、文書の内容の正確性を確保し、ユーザーが必要な情報に迅速にアクセスできるようにすることを目的としています。全体として、機能や手順には影響を与えず、ユーザー体験の向上に寄与しています。

## articles/ai-services/openai/includes/resource-authentication.md{#item-59aece}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソース認証ドキュメントの名称変更"
}
```

### Explanation
この変更は、「resource-auth.md」というファイルが「resource-authentication.md」に改名されたことを示しています。ファイルの内容自体には変更がなく、追加や削除も行われていません。

この名称変更は、ファイルの目的をより明確にすることを意図していると考えられます。「resource-authentication」という名前は、リソースの認証に関する内容であることをより的確に示しており、ユーザーが関連情報を見つけやすくなります。

この種の軽微な更新は、ドキュメント全体の整合性と可読性を改善し、ユーザー体験の向上に寄与します。

## articles/ai-services/openai/includes/text-to-speech-javascript.md{#item-e9b653}

<details>
<summary>Diff</summary>
````diff
@@ -27,7 +27,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
@@ -54,7 +54,7 @@ Your app's _package.json_ file will be updated with the dependencies.
 
     
 
-#### [Microsoft Entra ID](#tab/javascript-keyless)
+#### [Microsoft Entra ID](#tab/keyless)
 
 1. Create a new file named _Text-to-speech.js_ and open it in your preferred code editor. Copy the following code into the _Text-to-speech.js_ file:
 
@@ -121,7 +121,7 @@ Your app's _package.json_ file will be updated with the dependencies.
     node Text-to-speech.js
     ```
 
-#### [API key](#tab/javascript-key)
+#### [API key](#tab/api-key)
 
 1. Create a new file named _Text-to-speech.js_ and open it in your preferred code editor. Copy the following code into the _Text-to-speech.js_ file:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト読み上げJavaScriptガイドのリンク修正"
}
```

### Explanation
この変更は、「text-to-speech-javascript.md」ファイル内のリンクや見出しの名称修正を目的とした軽微な更新を示しています。具体的には、いくつかのリンクや見出しの表記が改善され、内容がより明確になっています。

主な変更点は以下の通りです：
1. リソース認証に関するセクションで、リンクが「resource-auth.md」から「resource-authentication.md」に修正されました。この変更により、ユーザーは正確な情報を見つけやすくなります。
2. 見出し「Microsoft Entra ID」および「API key」のリンク部分が、それぞれ「#tab/javascript-keyless」と「#tab/javascript-key」から「#tab/keyless」と「#tab/api-key」に変更されました。これにより、リンク先がより直感的で、分かりやすくなりました。

これらの修正は、ドキュメントの整合性を高め、読者が必要な情報を迅速に見つけられるようにすることで、全体的なユーザー体験を向上させることを目指しています。

## articles/ai-services/openai/includes/text-to-speech-typescript.md{#item-1335d5}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト読み上げTypeScriptガイドのリンク修正"
}
```

### Explanation
この変更は、「text-to-speech-typescript.md」ファイル内のリンクの修正を示す軽微なアップデートです。具体的には、リソース認証に関するリンクが変更されました。

変更内容は以下の通りです：
- リンクが「resource-auth.md」から「resource-authentication.md」に修正されました。この修正により、ユーザーがリソース認証の正確かつ関連性のある情報を見つけやすくなります。

この修正は、ドキュメントの整合性を高め、ユーザーが必要な情報により迅速にアクセスできるようにすることを目的としています。改善されたリンクによって、全体的なユーザー体験が向上すると期待されます。

## articles/ai-services/openai/includes/typescript.md{#item-ee5b93}

<details>
<summary>Diff</summary>
````diff
@@ -27,7 +27,7 @@ ms.date: 10/22/2024
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptガイドのリンク修正"
}
```

### Explanation
この変更は、「typescript.md」ファイル内のリソース認証に関するリンクの修正を含む軽微な更新です。具体的には、以下の変更が行われました。

- リンクが「resource-auth.md」から「resource-authentication.md」に変更されました。この修正により、ユーザーはリソース認証に関するより正確で関連性のある情報にアクセスできるようになります。

このような修正は、ドキュメントの品質と整合性を向上させ、読者が必要な情報を迅速に見つけられるようにすることを目的としています。全体として、ユーザー体験の向上が期待されます。

## articles/ai-services/openai/includes/use-your-data-javascript.md{#item-786699}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ Your app's _package.json_ file will be updated with the dependencies.
 
 ## Add the JavaScript code
 
-#### [Microsoft Entra ID](#tab/javascript-keyless)
+#### [Microsoft Entra ID](#tab/keyless)
 
 1. Open a command prompt where you want the new project, and create a new file named `ChatWithOwnData.js`. Copy the following code into the `ChatWithOwnData.js` file.
     
@@ -123,7 +123,7 @@ Your app's _package.json_ file will be updated with the dependencies.
     ```
 
 
-#### [API key](#tab/javascript-key)
+#### [API key](#tab/api-key)
 
 1. Open a command prompt where you want the new project, and create a new file named `ChatWithOwnData.js`. Copy the following code into the `ChatWithOwnData.js` file.
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptガイドのタブリンク修正"
}
```

### Explanation
この変更は、「use-your-data-javascript.md」ファイル内の見出しに関連するタブのリンクを更新する軽微な変更です。具体的には、以下の修正が行われました。

- 「Microsoft Entra ID」に関するタブのリンクが「javascript-keyless」から「keyless」に変更されました。
- 「API key」に関するタブのリンクも「javascript-key」から「api-key」に修正されました。

これらの変更により、ユーザーがより適切にそれぞれのタブへアクセスできるようにし、ドキュメントの整合性と可読性を向上させることを目的としています。全体として、ユーザー体験の向上が期待されます。

## articles/ai-services/openai/includes/whisper-javascript.md{#item-3ee990}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
@@ -52,7 +52,7 @@ Your app's _package.json_ file will be updated with the dependencies.
 
 ## Create a sample application
 
-#### [Microsoft Entra ID](#tab/javascript-keyless)
+#### [Microsoft Entra ID](#tab/keyless)
 
 1. Create a new file named _Whisper.js_ and open it in your preferred code editor. Copy the following code into the _Whisper.js_ file:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisper JavaScriptガイドのリンク修正"
}
```

### Explanation
この変更は、「whisper-javascript.md」ファイル内のリソース認証に関するリンクの修正を含む軽微な更新です。具体的には、以下の変更が行われました。

- リソース認証に関連するインクルードが「resource-auth.md」から「resource-authentication.md」に変更されました。この修正により、正確なリソース認証に関する情報が提供されるようになります。
  
- 「Microsoft Entra ID」に関するタブの見出しも、「javascript-keyless」から「keyless」に修正されました。このリンクの更新は、ユーザーが正しいセクションにアクセスしやすくするためのものです。

これらの変更は、ドキュメントの整合性とユーザビリティを向上させ、より効果的な情報提供を目指しています。全体として、高品質な情報の提供が期待されます。

## articles/ai-services/openai/includes/whisper-typescript.md{#item-eafedb}

<details>
<summary>Diff</summary>
````diff
@@ -27,7 +27,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-[!INCLUDE [resource authentication](resource-auth.md)]
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisper TypeScriptガイドのリンク修正"
}
```

### Explanation
この変更は、「whisper-typescript.md」ファイル内のリソース認証に関するリンクを修正する軽微な更新です。具体的には、以下の修正が加えられました。

- リソース認証に関するインクルードが「resource-auth.md」から「resource-authentication.md」に変更されました。この変更により、リソース認証に関する正確な情報が提供されるようになります。

この更新は、文書の内容の正確性と信頼性を向上させることを目的としており、ユーザーにとってより理解しやすい情報を提供しています。全体として、ユーザーエクスペリエンスの向上が期待されます。

## articles/ai-services/openai/media/quickstarts/audio-completions-chat-playground.png{#item-d78bda}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "音声完了チャットプレイグラウンドの画像追加"
}
```

### Explanation
この変更は、「audio-completions-chat-playground.png」という新しい画像ファイルの追加を示しています。この画像は、AIサービスのOpenAIに関連するクイックスタートガイドの一部であり、ユーザーが音声完了機能の使用方法を視覚的に理解できるサポートを提供する目的で作成されています。

画像の追加により、ドキュメントの内容がより豊かになり、ユーザーが設定や動作をより容易に把握できるようになります。この視覚コンテンツは、特に視覚的な学習スタイルを持つユーザーにとって有益です。全体として、この変更はユーザーエクスペリエンスの向上に寄与するものです。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: mrbullwinkle
 ms.author: mbullwin
 ms.service: azure-ai-openai
 ms.topic: overview
-ms.date: 12/15/2024
+ms.date: 01/23/2025
 ms.custom: build-2023, build-2023-dataai
 recommendations: false
 ---
@@ -20,7 +20,7 @@ Azure OpenAI Service provides REST API access to OpenAI's powerful language mode
 
 | Feature | Azure OpenAI |
 | --- | --- |
-| Models available | [**o1** & **o1-mini**](./how-to/reasoning.md) - (Limited Access - [Request Access](https://aka.ms/OAI/o1access))<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
+| Models available | [**o1**](./how-to/reasoning.md) - (Limited Access - [Request Access](https://aka.ms/OAI/o1access))<br>[**o1-mini**](./how-to/reasoning.md)<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
 | Fine-tuning | `GPT-4o-mini` (preview) <br> `GPT-4` (preview) <br>`GPT-3.5-Turbo` (0613) <br> `babbage-002` <br> `davinci-002`.|
 | Price | [Available here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> For details on vision-enabled chat models, see the [special pricing information](../openai/concepts/gpt-with-vision.md#special-pricing-information).|
 | Virtual network support & private link support | Yes.  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OpenAIオーバービュードキュメントの日付とモデル情報の修正"
}
```

### Explanation
この変更は、「overview.md」ファイルに対する軽微な更新を示しています。具体的には、以下の内容が修正されました。

1. 文書の日付が「2024年12月15日」から「2025年1月23日」に更新されました。これにより、ドキュメントの適用性と最新性が確保されます。
  
2. モデル情報の形式が改善されました。具体的には、リスト形式でのモデル名表示が行われ、各モデルへのリンクが明確に区切られました。これにより、ユーザーが情報をより簡単に理解し、ナビゲートできるようになります。

全体として、これらの修正は、ドキュメントの可読性を向上させ、最新情報を提供することで、ユーザーエクスペリエンスの向上に寄与しています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -52,6 +52,7 @@ The following sections provide you with a quick guide to the default quotas and
 | GPT-4 `vision-preview` & GPT-4 `turbo-2024-04-09` default max tokens | 16 <br><br> Increase the `max_tokens` parameter value to avoid truncated responses. GPT-4o max tokens defaults to 4096. |
 | Max number of custom headers in API requests<sup>1</sup> | 10 |
 | Message character limit | 1048576 |
+| Message size for audio files | 20 MB |
 
 <sup>1</sup> Our current APIs allow up to 10 custom headers, which are passed through the pipeline, and returned. Some customers now exceed this header count resulting in HTTP 431 errors. There's no solution for this error, other than to reduce header volume. **In future API versions we will no longer pass through custom headers**. We recommend customers not depend on custom headers in future system architectures.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "音声ファイルのメッセージサイズ制限の追加"
}
```

### Explanation
この変更は、「quotas-limits.md」ファイルに対する軽微な更新を示しています。具体的には、音声ファイルのメッセージサイズに関する新しい情報が追加されました。

追加された内容は、「音声ファイルのメッセージサイズ」は「20 MB」であるという情報です。これにより、ユーザーは音声ファイルを扱う際の制限を理解しやすくなります。音声データをAPIに送信する際、どのサイズまでが受け入れられるのかが明確になり、エラーを避けることができるでしょう。

全体として、この更新は、ユーザーが音声ファイルを扱うための要件を理解する手助けになり、API使用時のトラブルシューティングにも役立ちます。

## articles/ai-services/openai/realtime-audio-quickstart.md{#item-727df8}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use GPT-4o Realtime API for speech and audio with Azur
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 12/26/2024
+ms.date: 1/21/2025
 author: eric-urban
 ms.author: eur
 ms.custom: references_regions, ignite-2024
@@ -27,7 +27,7 @@ The GPT 4o realtime models are available for global deployments in [East US 2 an
 - `gpt-4o-realtime-preview` (2024-12-17)
 - `gpt-4o-realtime-preview` (2024-10-01)
 
-See the [models and versions documentation](./concepts/models.md#gpt-4o-realtime-preview) for more information.
+See the [models and versions documentation](./concepts/models.md#gpt-4o-audio) for more information.
 
 ## API support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオクイックスタートの更新"
}
```

### Explanation
この変更は、「realtime-audio-quickstart.md」ファイルに対する軽微な更新を示しています。具体的には、以下の2点が修正されています。

1. ドキュメントの日付が「2024年12月26日」から「2025年1月21日」に更新されました。この変更は、ドキュメントが最新の状態であることを示し、ユーザーに最新情報を提供します。

2. モデルに関するリンクが修正され、「gpt-4o-realtime-preview」から「gpt-4o-audio」に変更されました。これにより、ユーザーが最新の音声モデルに関する情報をより正確に参照できるようになります。

これらの更新は、ドキュメントの信頼性を高め、ユーザーが必要とする情報へ迅速にアクセスできるようにするための重要なステップです。全体として、これにより、リアルタイムオーディオ機能の利用に関する指針がより明確になります。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -29,6 +29,8 @@ items:
   items:
     - name: Assistants (preview)
       href: assistants-quickstart.md
+    - name: Audio generation
+      href: audio-completions-quickstart.md
     - name: Chat
       href: chatgpt-quickstart.md  
       displayName: ChatGPT, chatgpt
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "音声生成に関するセクションの追加"
}
```

### Explanation
この変更は、「toc.yml」ファイルに対する軽微な更新を示しています。具体的には、目次項目に新しいセクションが追加されました。

新しく追加された項目は「音声生成」で、関連するドキュメントへのリンクとして「audio-completions-quickstart.md」が指定されています。この更新により、ユーザーは音声生成に関する情報に簡単にアクセスできるようになります。

これにより、ドキュメントのナビゲーションが改善され、特に音声生成機能に関連するクイックスタートガイドが目次に明示されることで、ユーザーが必要な情報をより迅速に見つけやすくなります。全体として、この変更はユーザーエクスペリエンスの向上に寄与します。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -11,16 +11,25 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: whats-new
-ms.date: 1/17/2025
+ms.date: 1/21/2025
 recommendations: false
 ---
 
 # What's new in Azure OpenAI Service
 
-This article provides a summary of the latest releases and major documentation updates for Azure OpenAI.
+This article provides a summary of the latest releases and major documentation updates for Azure OpenAI Service.
 
 ## January 2025
 
+### GPT-4o audio completions
+
+The `gpt-4o-audio-preview` model is now available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability). Use the `gpt-4o-audio-preview` model for audio generation.
+
+The `gpt-4o-audio-preview` model introduces the audio modality into the existing `/chat/completions` API. The audio model expands the potential for AI applications in text and voice-based interactions and audio analysis. Modalities supported in `gpt-4o-audio-preview` model include:  text, audio, and text + audio. For more information, see the [audio generation quickstart](./audio-completions-quickstart.md).
+
+> [!NOTE]
+> The [Realtime API](./realtime-audio-quickstart.md) uses the same underlying GPT-4o audio model as the completions API, but is optimized for low-latency, real-time audio interactions.
+
 ### GPT-4o Realtime API 2024-12-17
 
 The `gpt-4o-realtime-preview` model version 2024-12-17 is available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability). Use the `gpt-4o-realtime-preview` version 2024-12-17 model instead of the `gpt-4o-realtime-preview` version 2024-10-01-preview model for real-time audio interactions.
@@ -794,9 +803,9 @@ If you're currently using the `2023-03-15-preview` API, we recommend migrating t
 
 - **GPT-4 series models are now available in preview on Azure OpenAI**. To request access, existing Azure OpenAI customers can [apply by filling out this form](https://aka.ms/oai/get-gpt4). These models are currently available in the East US and South Central US regions.
 
-- **New Chat Completion API for GPT-35-Turbo and GPT-4 models released in preview on 3/21**. To learn more checkout the [updated quickstarts](./quickstart.md) and [how-to article](./how-to/chatgpt.md).
+- **New Chat Completion API for GPT-35-Turbo and GPT-4 models released in preview on 3/21**. To learn more, check out the [updated quickstarts](./quickstart.md) and [how-to article](./how-to/chatgpt.md).
 
-- **GPT-35-Turbo preview**. To learn more checkout the [how-to article](./how-to/chatgpt.md).
+- **GPT-35-Turbo preview**. To learn more, check out the [how-to article](./how-to/chatgpt.md).
 
 - Increased training limits for fine-tuning: The max training job size (tokens in training file) x (# of epochs) is 2 Billion tokens for all models. We have also increased the max training job from 120 to 720 hours. 
 - Adding additional use cases to your existing access.  Previously, the process for adding new use cases required customers to reapply to the service. Now, we're releasing a new process that allows you to quickly add new use cases to your use of the service. This process follows the established Limited Access process within Azure AI services. [Existing customers can attest to any and all new use cases here](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUM003VEJPRjRSOTZBRVZBV1E5N1lWMk1XUyQlQCN0PWcu). Please note that this is required anytime you would like to use the service for a new use case you didn't originally apply for.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスの新機能に関する更新"
}
```

### Explanation
この変更は、「whats-new.md」ファイルの軽微な更新を示しており、Azure OpenAIサービスの最新のリリースと主な文書更新についての情報が追加されています。

具体的には、以下の主要なポイントがあります：

1. **日付の更新**: 文書の日付が「2025年1月17日」から「2025年1月21日」に更新されました。これにより、文書が最新のものであることが確認できます。

2. **新機能の追加**: 「GPT-4o audio completions」という新しいモデルが紹介され、音声生成に使用できる「gpt-4o-audio-preview」モデルが追加されました。このモデルは、テキストや音声ベースのインタラクションにおけるAIアプリケーションの可能性を広げています。また、関連するクイックスタートガイドへのリンクも提供されています。

3. **認識マークの追加**: Realtime APIが同じGPT-4o音声モデルを使用しているが、リアルタイムの音声インタラクションに最適化されていることが注記として追加されました。

4. **内容全般の改善**: いくつかの表現が明確にされ、文書全体の読みやすさが向上しています。

この更新は、Azure OpenAIサービスのユーザーにとって重要な情報を提供し、最新の機能や利用可能なリソースを明確に示すものであり、特に音声生成に関心のあるユーザーにとって有益です。


