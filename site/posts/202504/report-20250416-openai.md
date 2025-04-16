---
date: '2025-04-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1f18936...MicrosoftDocs:81ad672
summary: 今回の変更は、複数のドキュメントファイルに対する軽微な更新から新機能の追加に至るまで広範囲にわたります。特に、音声モデルの統合および名称の変更が行われており、ユーザーの利便性を向上させることを目的としています。重要な改訂点として、音声モデル「Whisper」の名称変更や新たに「gpt-4.1」「gpt-4o」が追加されたことが挙げられます。これにより、Azure
  OpenAIの音声機能やモデル選択肢が一層明確になり、ユーザーの理解が深まることが期待されます。全体的に、この更新はAzure OpenAIのサービスの利用価値を高め、ユーザー体験を向上させる重要なステップとなります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1f18936...MicrosoftDocs:81ad672){target="_blank"}

<format>
# Highlights
今回の変更は、多数のドキュメントファイルにおける軽微な更新から新機能の追加まで、幅広い範囲にわたっています。特に、音声モデルの統合や、名前変更が多く実施されており、ユーザーの利便性と理解を高めることを目的としている。この中で注意すべき点は、音声モデル「Whisper」の名称変更と最新モデル「gpt-4.1」「gpt-4o」の追加です。

## New features
- `articles/ai-services/openai/concepts/audio.md`: Azure OpenAIの音声機能に関する新規記事が追加されました。
- `articles/ai-services/openai/includes/language-overview/dotnet.md`: .NET用ライブラリに推論モデルの例が組み込まれました。

## Breaking changes
- `articles/ai-services/openai/concepts/models.md`: 音声モデルの構成変更がなされ、旧来の用語が統合されました。

## Other updates
- 「Whisper」が「Speech to text」に名称変更され、用語の一貫性が向上。
- 新モデルの追加に伴うクォータおよび制限の更新。
- ドキュメントの内部リンクや日付の更新による精度の向上。
- いくつかの環境変数名やコードサンプルの修正により、ユーザビリティを改善。

# Insights
今回のドキュメント更新は、主にAzure OpenAIサービスの音声機能に焦点を当て、特に音声認識や合成機能の最新情報を提供することを目的としています。これにより、従来の「Whisper」モデルなどの曖昧な表現から、より具体的な「Speech to text」などに変更されました。こうした改名や統合により、以前から続いていた語と機能の混乱を解消する狙いがあることが伺えます。

さらに、新モデル「gpt-4.1」の登場により、より高度な言語処理が可能となり、ユーザーはこれまで以上に細分化されたモデル選択肢を活用できるようになります。特に音声からテキスト、テキストから音声へといった変換機能は、現在のコンテンツ生成やリアルタイム処理において非常に重要です。

また、ドキュメントの項目やリンクの見直しも進められており、ユーザーは関連情報に簡単にアクセス可能になるとともに、APIの利用方法に一貫性が増しています。このような細部の更新は、開発者体験の向上に直接影響をもたらし、Azure OpenAIサービスの利用を今後さらに促進させることでしょう。

全体として、今回の更新は、Azure OpenAIが提供するモデルやAPIの利用価値をより一層高めるための重要なステップであり、ユーザーにとっての利便性や理解の向上を目指していることが明白です。この変化を契機に、より多くのシナリオで音声機能が利用されることが期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [api-version-deprecation.md](#item-1cad50) | minor update | APIバージョン非推奨に関する更新 | modified | 1 | 1 | 2 | 
| [audio.md](#item-624e70) | new feature | Azure OpenAIサービスの音声機能に関する新規記事 | added | 43 | 0 | 43 | 
| [content-filter.md](#item-dfc7e7) | minor update | コンテンツフィルタリングに関する情報の更新 | modified | 1 | 1 | 2 | 
| [model-retirements.md](#item-03fc2e) | minor update | モデルのリタイア情報の更新と日付の修正 | modified | 9 | 2 | 11 | 
| [models.md](#item-db2c37) | breaking change | モデルの構成と情報の大幅な更新 | modified | 52 | 58 | 110 | 
| [embeddings.md](#item-e38d07) | minor update | クライアント名の変更 | modified | 1 | 1 | 2 | 
| [function-calling.md](#item-32f8e0) | minor update | 日付とモデルの追加情報の更新 | modified | 3 | 1 | 4 | 
| [on-your-data-configuration.md](#item-4875d3) | minor update | 日付の更新と不要な情報の削除 | modified | 2 | 6 | 8 | 
| [predicted-outputs.md](#item-212eb9) | minor update | 日付の更新と新モデルの追加 | modified | 2 | 1 | 3 | 
| [prompt-caching.md](#item-1631df) | minor update | 日付の更新と新モデルの追加 | modified | 3 | 1 | 4 | 
| [realtime-audio.md](#item-482ba3) | minor update | リンクの更新とトランスクリプションモデル情報の強化 | modified | 2 | 2 | 4 | 
| [reasoning.md](#item-a54b2f) | minor update | C#のサンプルコードの追加と推論努力レベルの指定 | modified | 70 | 3 | 73 | 
| [responses.md](#item-b9757d) | minor update | モデルサポートの更新と新モデルの追加 | modified | 3 | 1 | 4 | 
| [structured-outputs.md](#item-cc2557) | minor update | 日付の更新と新モデルの追加 | modified | 3 | 1 | 4 | 
| [use-web-app.md](#item-802413) | minor update | リンクの修正 | modified | 2 | 2 | 4 | 
| [api-surface.md](#item-a25fa2) | minor update | データプレーン推論APIの説明修正 | modified | 1 | 1 | 2 | 
| [latest-inference.md](#item-b30a63) | minor update | モデルに関する説明修正とプレビューラベル追加 | modified | 3 | 3 | 6 | 
| [content-filter-configurability.md](#item-11f064) | minor update | Whisperモデルを除外するための説明修正 | modified | 1 | 1 | 2 | 
| [dotnet.md](#item-46e881) | new feature | .NET用Azure OpenAIライブラリに推論モデルの例を追加 | modified | 36 | 1 | 37 | 
| [go.md](#item-a289f2) | bug fix | 環境変数名の修正 | modified | 3 | 3 | 6 | 
| [standard-audio.md](#item-1d8db7) | minor update | 音声モデルマトリックスに新しいモデルを追加 | modified | 11 | 11 | 22 | 
| [standard-global.md](#item-17a84b) | minor update | モデルマトリックスの更新と新モデルの追加 | modified | 27 | 27 | 54 | 
| [text-to-speech-dotnet.md](#item-fea66a) | minor update | テキストから音声へのモデル要件の更新 | modified | 1 | 1 | 2 | 
| [whisper-dotnet.md](#item-562a58) | minor update | スピーチからテキストへのモデル要件の更新 | modified | 1 | 1 | 2 | 
| [whisper-javascript.md](#item-3ee990) | minor update | スピーチからテキストへのモデル要件の更新 | modified | 1 | 1 | 2 | 
| [whisper-powershell.md](#item-7db269) | minor update | スピーチからテキストへのモデル要件の更新 | modified | 1 | 2 | 3 | 
| [whisper-python.md](#item-e61179) | minor update | スピーチからテキストへのモデル要件の更新 | modified | 1 | 1 | 2 | 
| [whisper-rest.md](#item-639ccb) | minor update | スピーチからテキストへのモデル要件の更新 | modified | 1 | 1 | 2 | 
| [whisper-typescript.md](#item-eafedb) | minor update | スピーチからテキストへのモデル要件の更新 | modified | 1 | 1 | 2 | 
| [index.yml](#item-0adb87) | minor update | Whisperの名称変更 | modified | 1 | 1 | 2 | 
| [overview.md](#item-97d507) | minor update | モデル名と機能に関する説明の更新 | modified | 5 | 7 | 12 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータおよび制限の更新 | modified | 6 | 4 | 10 | 
| [realtime-audio-quickstart.md](#item-727df8) | minor update | モデル情報へのリンクの更新 | modified | 1 | 1 | 2 | 
| [realtime-audio-reference.md](#item-276d51) | minor update | リアルタイムオーディオ参照の情報更新 | modified | 4 | 2 | 6 | 
| [supported-languages.md](#item-12c019) | minor update | サポートされている言語のドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [text-to-speech-quickstart.md](#item-c344ad) | minor update | 音声合成におけるドキュメントリンクの更新 | modified | 2 | 2 | 4 | 
| [toc.yml](#item-c945af) | minor update | 目次の更新と新しいセクションの追加 | modified | 3 | 1 | 4 | 
| [whats-new.md](#item-53303b) | minor update | 新機能の追加とモデル情報の更新 | modified | 12 | 2 | 14 | 
| [whisper-quickstart.md](#item-4cae3d) | minor update | Whisperクイックスタートの情報更新 | modified | 3 | 0 | 3 | 


# Modified Contents
## articles/ai-services/openai/api-version-deprecation.md{#item-1cad50}

<details>
<summary>Diff</summary>
````diff
@@ -40,7 +40,7 @@ This version contains support for the latest Azure OpenAI features including:
 - [Text to speech](./text-to-speech-quickstart.md). [**Added in 2024-02-15-preview**]
 - [DALL-E 3](./dall-e-quickstart.md). [**Added in 2023-12-01-preview**]
 - [Fine-tuning](./how-to/fine-tuning.md). [**Added in 2023-10-01-preview**]
-- [Whisper](./whisper-quickstart.md). [**Added in 2023-09-01-preview**]
+- [Speech to text](./whisper-quickstart.md). [**Added in 2023-09-01-preview**]
 - [Function calling](./how-to/function-calling.md)  [**Added in 2023-07-01-preview**]
 - [Retrieval augmented generation with your data feature](./use-your-data-quickstart.md).  [**Added in 2023-06-01-preview**]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョン非推奨に関する更新"
}
```

### Explanation
この変更は、「api-version-deprecation.md」ファイルにおける軽微な更新を表しています。具体的には、存在する機能のリストの一部が更新され、「Whisper」から「Speech to text」に名称が変更されました。この変更は、新しいオーディオ機能を反映しており、それ以外の情報は維持されています。該当する機能がどのプリビューで追加されたかの情報も残っており、ユーザーは最新の情報にアクセスできます。この変更によって、APIの機能に関する正確性が向上します。

## articles/ai-services/openai/concepts/audio.md{#item-624e70}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,43 @@
+---
+title: Azure OpenAI Service audio
+titleSuffix: Azure OpenAI
+description: Learn about the audio capabilities of Azure OpenAI Service.
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-openai
+ms.topic: conceptual 
+ms.date: 4/15/2025
+ms.custom: template-concept
+manager: nitinme
+---
+
+# Audio capabilities in Azure OpenAI Service
+
+> [!IMPORTANT]
+> The content filtering system isn't applied to prompts and completions processed by the audio models such as Whisper in Azure OpenAI Service. 
+
+Audio models in Azure OpenAI are available via the `realtime`, `completions`, and `audio` APIs. The audio models are designed to handle a variety of tasks, including speech recognition, translation, and text to speech.
+
+For information about the available audio models per region in Azure OpenAI Service, see the [audio models](models.md?tabs=standard-audio#standard-models-by-endpoint), [standard models by endpoint](models.md?tabs=standard-audio#standard-models-by-endpoint), and [global standard model availability](models.md?tabs=standard-audio#global-standard-model-availability) documentation.
+
+### GPT-4o audio Realtime API
+
+GPT-4o real-time audio is designed to handle real-time, low-latency conversational interactions, making it a great fit for support agents, assistants, translators, and other use cases that need highly responsive back-and-forth with a user. For more information on how to use GPT-4o real-time audio, see the [GPT-4o real-time audio quickstart](../realtime-audio-quickstart.md) and [how to use GPT-4o audio](../how-to/realtime-audio.md).
+
+## GPT-4o audio completions
+
+GPT-4o audio completion is designed to generate audio from audio or text prompts, making it a great fit for generating audio books, audio content, and other use cases that require audio generation. The GPT-4o audio completions model introduces the audio modality into the existing `/chat/completions` API. For more information on how to use GPT-4o audio completions, see the [audio generation quickstart](../audio-completions-quickstart.md).
+
+## Audio API
+
+The audio models via the `/audio` API can be used for speech to text, translation, and text to speech. To get started with the audio API, see the [Whisper quickstart](../whisper-quickstart.md) for speech to text.
+
+> [!NOTE]
+> To help you decide whether to use Azure AI Speech or Azure OpenAI Service, see the [Azure AI Speech batch transcription](../../speech-service/batch-transcription-create.md), [What is the Whisper model?](../../speech-service/whisper-overview.md), and [OpenAI text to speech voices](../../speech-service/openai-voices.md#openai-text-to-speech-voices-via-azure-openai-service-or-via-azure-ai-speech) guides.
+
+## Related content
+
+- [Audio models](models.md#audio-models)
+- [Whisper quickstart](../whisper-quickstart.md)
+- [Audio generation quickstart](../audio-completions-quickstart.md)
+- [GPT-4o real-time audio quickstart](../realtime-audio-quickstart.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIサービスの音声機能に関する新規記事"
}
```

### Explanation
この変更は、「audio.md」という新しいファイルの追加を示しています。このファイルでは、Azure OpenAIサービスにおける音声機能について詳細に説明されており、音声認識、翻訳、テキスト音声変換など、さまざまなタスクを処理する音声モデルが紹介されています。重要な点として、音声モデルで処理されたプロンプトおよび完了に対してはコンテンツフィルタリングシステムが適用されないことが強調されています。

記事は、リアルタイム音声API、音声完了モデル、Audio APIなど、各音声機能の詳細を提供しています。また、Azure OpenAIサービスにおける音声モデルの利用に関するクイックスタートガイドや関連ドキュメントへのリンクも含まれており、ユーザーが必要な情報に簡単にアクセスできるようになっています。この新しい情報は、音声を用いたインタラクションやコンテンツ生成に関心のあるユーザーにとって、大変有用です。

## articles/ai-services/openai/concepts/content-filter.md{#item-dfc7e7}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ manager: nitinme
 # Content filtering
 
 > [!IMPORTANT]
-> The content filtering system isn't applied to prompts and completions processed by the Whisper model in Azure OpenAI Service. Learn more about the [Whisper model in Azure OpenAI](models.md#whisper).
+> The content filtering system isn't applied to prompts and completions processed by the audio models such as Whisper in Azure OpenAI Service. Learn more about the [Audio models in Azure OpenAI](models.md?tabs=standard-audio#standard-models-by-endpoint).
 
 Azure OpenAI Service includes a content filtering system that works alongside core models, including DALL-E image generation models. This system works by running both the prompt and completion through an ensemble of classification models designed to detect and prevent the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions. Variations in API configurations and application design might affect completions and thus filtering behavior.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングに関する情報の更新"
}
```

### Explanation
この変更は、「content-filter.md」ファイルの小規模な修正を示しています。具体的には、音声モデルに関する説明において、「Whisperモデル」という具体的な名称から「音声モデル」の一般的な表現に変更されました。この更新により、Azure OpenAIサービス内の音声モデル全般に対してコンテンツフィルタリングシステムが適用されないことがより明確に示されています。

変更後のテキストは、音声モデルの一部としてWhisperが言及されていますが、全体的に音声モデルの枠組みを指し、利用者にとって関連情報へのリンクが改めて提供されています。この更新は、コンテンツフィルタリングの適用範囲をより正確に説明することで、ユーザーに重要な注意事項を伝えることを目的としています。

## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 03/26/2025
+ms.date: 04/14/2025
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -103,6 +103,8 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-4` | 1106-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025 **<sup>1</sup>** <br>Retirement date: May 1, 2025  | `gpt-4o`|
 | `gpt-4` | 0125-preview |To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025 **<sup>1</sup>** <br>Retirement date: May 1, 2025  | `gpt-4o` |
 | `gpt-4` | vision-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025  **<sup>1</sup>** <br>Retirement date: May 1, 2025 | `gpt-4o`|
+| `gpt-4.5-preview` | 2025-02-27 | No earlier than July 02, 2025 | `gpt-4.1` |
+| `gpt-4.1` | 2025-04-14 | No earlier than April 11, 2026 | |
 | `gpt-4o` | 2024-05-13 | No earlier than June 30, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on March 17, 2025. | |
 | `gpt-4o` | 2024-08-06 | No earlier than August 6, 2025  | |
 | `gpt-4o` | 2024-11-20 | No earlier than November 20, 2025  | |
@@ -111,6 +113,7 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-3.5-turbo-instruct` | 0914 | No earlier than May 31, 2025 |  |
 | `o1-preview` | 2024-09-12 | No earlier than April 2, 2025 | `o1` |
 | `o1` | 2024-12-17 | No earlier than December 17, 2025 | |
+| `o3-mini` | 2025-01-31 | No earlier than February 1, 2026 | |
 | `text-embedding-ada-002` | 2 | No earlier than October 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
 | `text-embedding-ada-002` | 1 | No earlier than October 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
 | `text-embedding-3-small` | | No earlier than January 25, 2026 | |
@@ -131,7 +134,7 @@ These models are currently available for use in Azure OpenAI Service.
 | Model | Current default version | New default version | Default upgrade date |
 |---|---|---|---|
 | `gpt-35-turbo` | 0301 | 0125 | Deployments of versions `0301`, `0613`, and `1106` set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 21, 2025.|
-|  `gpt-4o` | 2024-05-13 | 2024-08-06 | Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on March 26, 2025. |
+|  `gpt-4o` | 2024-08-06 | - | - |
 
 ## Deprecated models
 
@@ -176,6 +179,10 @@ If you're an existing customer looking for information about these models, see [
 
 ## Retirement and deprecation history
 
+## April 15, 2025
+
+To track further updates to this article refer to the [Git History](https://github.com/MicrosoftDocs/azure-ai-docs/commits/main/articles/ai-services/openai/concepts/model-retirements.md)
+
 ## March 18, 2025
 
 GPT-4 preview models retirement date updated to date: May 1, 2025.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのリタイア情報の更新と日付の修正"
}
```

### Explanation
この変更は、「model-retirements.md」ファイルの内容を更新し、いくつかのモデルリタイアに関する情報を修正しました。主な変更点は、モデルのリタイア日やアップグレードに関する新しい情報の追加です。特に、`gpt-4`モデルや新しい`gpt-4.5-preview`および`gpt-4.1`モデルのリタイアスケジュールが明確に追加されました。

さらに、ドキュメントの日付が更新され、情報のタイムスタンプが変更されました。新たに「リタイアと廃止の履歴」というセクションが追加されたことで、過去の変更履歴を容易に追跡できるようになっています。これにより、ユーザーは使用しているモデルの将来のアップグレードやリタイアに関する最新情報を把握しやすくなります。全体として、この更新はユーザビリティの向上を目的としており、利用者にとってより有益な情報を提供しています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 04/14/2025
+ms.date: 04/15/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -23,13 +23,11 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 | [GPT-4.5 Preview](#gpt-45-preview) |The latest GPT model that excels at diverse text and image tasks.  |
 | [o-series models](#o-series-models) |[Reasoning models](../how-to/reasoning.md) with advanced problem-solving and increased focus and capability.  |
 | [GPT-4o & GPT-4o mini & GPT-4 Turbo](#gpt-4o-and-gpt-4-turbo) | The latest most capable Azure OpenAI models with multimodal versions, which can accept both text and images as input. |
-| [GPT-4o audio](#gpt-4o-audio) | GPT-4o audio models that support either low-latency, "speech in, speech out" conversational interactions or audio generation. |
 | [GPT-4](#gpt-4) | A set of models that improve on GPT-3.5 and can understand and generate natural language and code. |
 | [GPT-3.5](#gpt-35) | A set of models that improve on GPT-3 and can understand and generate natural language and code. |
 | [Embeddings](#embeddings-models) | A set of models that can convert text into numerical vector form to facilitate text similarity. |
 | [DALL-E](#dall-e-models) | A series of models that can generate original images from natural language. |
-| [Whisper](#whisper-models) | A series of models in preview that can transcribe and translate speech to text. |
-| [Text to speech](#text-to-speech-models-preview) (Preview) | A series of models in preview that can synthesize text to speech. |
+| [Audio](#audio-models) | A series of models for speech to text, translation, and text to speech. GPT-4o audio models support either low-latency, "speech in, speech out" conversational interactions or audio generation. |
 
 ## GPT 4.1 series
 
@@ -38,12 +36,17 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 | Model | Region |
 |---|---|
 | `gpt-4.1` (2025-04-14) | East US2 (Global Standard), Sweden Central (Global Standard) |
+| `gpt-4.1-nano` (2025-04-14) | East US2 (Global Standard), Sweden Central (Global Standard)|
+| `gpt-4.1-mini` (2025-04-14) | East US2 (Global Standard), Sweden Central (Global Standard)|
 
 ### Capabilities
 
 |  Model ID  | Description | Context Window | Max Output Tokens | Training Data (up to)  |
 |  --- |  :--- |:--- |:---|:---: |
 | `gpt-4.1` (2025-04-14) <br> <br> **Latest model from Azure OpenAI**  | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | 1,047,576 | 32,768 | May 31, 2024 |
+| `gpt-4.1-nano` (2025-04-14) <br><br> **Fastest 4.1 model** | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | 1,047,576  | 32,768 | May 31, 2024 |
+| `gpt-4.1-mini` (2025-04-14) | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | 1,047,576  | 32,768 | May 31, 2024 |
+
 
 ## computer-use-preview
 
@@ -114,40 +117,6 @@ To learn more about the advanced `o-series` models see, [getting started with re
 | `o1-preview` | See the [models table](#model-summary-table-and-region-availability). This model is only available for customers who were granted access as part of the original limited access |
 | `o1-mini` | See the [models table](#model-summary-table-and-region-availability). |
 
-## GPT-4o audio
-
-The GPT 4o audio models are part of the GPT-4o model family and support either low-latency, "speech in, speech out" conversational interactions or audio generation. 
-- GPT-4o real-time audio is designed to handle real-time, low-latency conversational interactions, making it a great fit for support agents, assistants, translators, and other use cases that need highly responsive back-and-forth with a user. For more information on how to use GPT-4o real-time audio, see the [GPT-4o real-time audio quickstart](../realtime-audio-quickstart.md) and [how to use GPT-4o audio](../how-to/realtime-audio.md).
-- GPT-4o audio completion is designed to generate audio from audio or text prompts, making it a great fit for generating audio books, audio content, and other use cases that require audio generation. The GPT-4o audio completions model introduces the audio modality into the existing `/chat/completions` API. For more information on how to use GPT-4o audio completions, see the [audio generation quickstart](../audio-completions-quickstart.md).
-
-> [!CAUTION]
-> We don't recommend using preview models in production. We will upgrade all deployments of preview models to either future preview versions or to the latest stable GA version. Models that are designated preview don't follow the standard Azure OpenAI model lifecycle.
-
-To use GPT-4o audio, you need [an Azure OpenAI resource](../how-to/create-resource.md) in one of the [supported regions](#global-standard-model-availability).
-
-When your resource is created, you can [deploy](../how-to/create-resource.md#deploy-a-model) the GPT-4o audio model. 
-
-Details about maximum request tokens and training data are available in the following table.
-
-|  Model ID  | Description | Max Request (tokens) | Training Data (up to)  |
-|---|---|---|---|
-|`gpt-4o-mini-audio-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for audio and text generation. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
-|`gpt-4o-mini-realtime-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for real-time audio processing. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
-|`gpt-4o-audio-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for audio and text generation. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
-|`gpt-4o-realtime-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for real-time audio processing. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
-|`gpt-4o-realtime-preview` (2024-10-01) <br> **GPT-4o audio** | **Audio model** for real-time audio processing. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
-
-### Region availability
-
-| Model | Region |
-|---|---|
-|`gpt-4o-mini-audio-preview` | East US2 (Global Standard) |
-|`gpt-4o-mini-realtime-preview` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
-|`gpt-4o-audio-preview` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
-|`gpt-4o-realtime-preview` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
-
-To compare the availability of GPT-4o audio models across all regions, see the [models table](#global-standard-model-availability).
-
 ## GPT-4o and GPT-4 Turbo
 
 GPT-4o integrates text and images in a single model, enabling it to handle multiple data types simultaneously. This multimodal approach enhances accuracy and responsiveness in human-computer interactions. GPT-4o matches GPT-4 Turbo in English text and coding tasks while offering superior performance in non-English languages and vision tasks, setting new benchmarks for AI capabilities.
@@ -251,17 +220,56 @@ OpenAI's MTEB benchmark testing found that even when the third generation model'
 
 The DALL-E models generate images from text prompts that the user provides. DALL-E 3 is generally available for use with the REST APIs. DALL-E 2 and DALL-E 3 with client SDKs are in preview.
 
-## Whisper
+## Audio models
+
+Audio models in Azure OpenAI are available via the `realtime`, `completions`, and `audio` APIs.
+
+### GPT-4o audio models
+
+The GPT 4o audio models are part of the GPT-4o model family and support either low-latency, "speech in, speech out" conversational interactions or audio generation. 
+
+> [!CAUTION]
+> We don't recommend using preview models in production. We will upgrade all deployments of preview models to either future preview versions or to the latest stable GA version. Models that are designated preview don't follow the standard Azure OpenAI model lifecycle.
 
-The Whisper models can be used for speech to text.
+Details about maximum request tokens and training data are available in the following table.
+
+|  Model ID  | Description | Max Request (tokens) | Training Data (up to)  |
+|---|---|---|---|
+|`gpt-4o-mini-audio-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for audio and text generation. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
+|`gpt-4o-mini-realtime-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for real-time audio processing. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
+|`gpt-4o-audio-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for audio and text generation. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
+|`gpt-4o-realtime-preview` (2024-12-17) <br> **GPT-4o audio** | **Audio model** for real-time audio processing. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
+|`gpt-4o-realtime-preview` (2024-10-01) <br> **GPT-4o audio** | **Audio model** for real-time audio processing. |Input: 128,000  <br> Output: 4,096 | Oct 2023 |
+
+To compare the availability of GPT-4o audio models across all regions, see the [models table](#global-standard-model-availability).
 
-You can also use the Whisper model via Azure AI Speech [batch transcription](../../speech-service/batch-transcription-create.md) API. Check out [What is the Whisper model?](../../speech-service/whisper-overview.md) to learn more about when to use Azure AI Speech vs. Azure OpenAI Service.
+### Audio API
 
-## Text to speech (Preview)
+The audio models via the `/audio` API can be used for speech to text, translation, and text to speech. 
 
-The OpenAI text to speech models, currently in preview, can be used to synthesize text to speech.
+#### Speech to text models
 
-You can also use the OpenAI text to speech voices via Azure AI Speech. To learn more, see [OpenAI text to speech voices via Azure OpenAI Service or via Azure AI Speech](../../speech-service/openai-voices.md#openai-text-to-speech-voices-via-azure-openai-service-or-via-azure-ai-speech) guide. 
+|  Model ID  | Description | Max Request (audio file size) |
+| ----- | ----- | ----- |
+| `whisper` | General-purpose speech recognition model. | 25 MB |
+| `gpt-4o-transcribe` | Speech to text powered by GPT-4o. | 25 MB|
+| `gpt-4o-mini-transcribe` | Speech to text powered by GPT-4o mini. | 25 MB|
+
+#### Speech translation models
+
+|  Model ID  | Description | Max Request (audio file size) |
+| ----- | ----- | ----- |
+| `whisper` | General-purpose speech recognition model. | 25 MB |
+
+#### Text to speech models (Preview)
+
+|  Model ID  | Description |
+|  --- | :--- |
+| `tts` | Text to speech optimized for speed. |
+| `tts-hd` | Text to speech optimized for quality.|
+| `gpt-4o-mini-tts` | Text to speech model powered by GPT-4o mini.<br/><br/>You can guide the voice to speak in a style or tone. |
+
+For more information see [Audio models region availability](?tabs=standard-audio#standard-models-by-endpoint) in this article.
 
 ## Model summary table and region availability
 
@@ -414,20 +422,6 @@ These models can only be used with Embedding API requests.
 
 [!INCLUDE [Audio](../includes/model-matrix/standard-audio.md)]
 
-### Whisper models
-
-|  Model ID  | Max Request (audio file size) |
-|  --- | :---: |
-| `whisper` | 25 MB |
-
-### Text to speech models (Preview)
-
-|  Model ID  | Description |
-|  --- | :--- |
-| `tts` | The latest Azure OpenAI text to speech model, optimized for speed. |
-| `tts-hd` | The latest Azure OpenAI text to speech model, optimized for quality.|
- |
-
 # [Completions (Legacy)](#tab/standard-completions)
 
 ### Completions models
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルの構成と情報の大幅な更新"
}
```

### Explanation
この変更は、「models.md」ファイルの構成と内容に大規模な修正を加えたもので、特に音声モデルに関するセクションが見直されています。主な更新点は次の通りです：

1. **音声モデルの統合**: 音声モデルに関する情報が集約され、旧来の「Whisper」や「Text to speech」モデルから「Audio」セクションに統合されました。これにより、音声認識や生成に関する機能が一つのセクションで包括的に説明されています。

2. **新しいモデルの追加**: `gpt-4.1-nano`や`gpt-4.1-mini`などの新しいモデルが追加され、それぞれの能力や利用可能な地域についての情報が整理されています。これにより、利用者は利用するモデルの選択肢とその詳細をより明確に理解できるようになりました。

3. **アップデートされた日付**: ドキュメントの日付が更新され、最新の情報が反映されています。

4. **モデル機能の詳細化**: 各モデルの機能や特性が詳細に説明されており、例として、`gpt-4o`モデルのマルチモーダル機能や、音声モデルの低遅延な会話処理能力が強調されています。

全体として、これらの変更は従来の情報を整理し、新しい機能やモデルについて詳細な情報を提供することで、ユーザーの利便性を向上させることを目的としています。利用者は、Azure OpenAIサービスでのモデル利用に関する最新情報をより効率的に得られるようになっています。

## articles/ai-services/openai/how-to/embeddings.md{#item-e38d07}

<details>
<summary>Diff</summary>
````diff
@@ -57,7 +57,7 @@ string oaiKey = "YOUR_API_KEY";
 
 AzureKeyCredential credentials = new (oaiKey);
 
-OpenAIClient openAIClient = new (oaiEndpoint, credentials);
+AzureOpenAIClient openAIClient = new (oaiEndpoint, credentials);
 
 EmbeddingsOptions embeddingOptions = new()
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クライアント名の変更"
}
```

### Explanation
この変更は、「embeddings.md」ファイルのコードサンプル内で使用されているクライアント名を変更したものです。具体的には、`OpenAIClient`から`AzureOpenAIClient`に変更されました。この修正により、Azureに特化したクライアント名が明示的に示され、利用者はAzure OpenAIサービスに接続するために適切なクライアントクラスを使用することができます。

この変更は、ユーザがAPIキーを使用して接続する際に、正しいクライアントのインスタンスを作成することを容易にするためのもので、APIの利用方法に一貫性を持たせることを目的としています。その結果、ユーザビリティが向上し、新しい利用者にもわかりやすいドキュメントになります。

## articles/ai-services/openai/how-to/function-calling.md{#item-32f8e0}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: mbullwin #delegenz
 ms.service: azure-ai-openai
 ms.custom: devx-track-python
 ms.topic: how-to
-ms.date: 02/28/2025
+ms.date: 04/14/2025
 manager: nitinme
 ---
 
@@ -40,6 +40,8 @@ At a high level you can break down working with functions into three steps:
 * `gpt-4o` (`2024-11-20`)
 * `gpt-4o-mini` (`2024-07-18`)
 * `gpt-4.5-preview` (`2025-02-27`)
+* `gpt-4.1` (`2025-14-2025`)
+* `gpt-4.1-nano` (`2025-14-2025`)
 
 Support for parallel function was first added in API version [`2023-12-01-preview`](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2023-12-01-preview/inference.json)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付とモデルの追加情報の更新"
}
```

### Explanation
この変更は、「function-calling.md」ファイルにおける日付の更新と新しいモデルに関する情報の追加を含んでいます。

1. **日付の更新**: ドキュメントの日付が`02/28/2025`から`04/14/2025`に変更され、情報の最新性が反映されました。

2. **新しいモデルの情報追加**: 新たに`gpt-4.1`および`gpt-4.1-nano`がリストに追加され、それぞれのモデルが`2025-04-14`に登場することが示されています。この追加は新モデルの存在を示し、ユーザーが新機能を利用できることを期待させるものです。

これらの変更は、ドキュメントの最新情報を提供し、利用者が新しいモデルや機能を簡単に認識できるようにすることを目的としています。全体として、これによりユーザーの理解が深まり、より適切な利用が可能になるでしょう。

## articles/ai-services/openai/how-to/on-your-data-configuration.md{#item-4875d3}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-openai
 ms.topic: how-to
 author: aahill
 ms.author: aahi
-ms.date: 03/31/2025
+ms.date: 04/15/2025
 recommendations: false
 ---
 
@@ -64,10 +64,6 @@ Azure OpenAI On Your Data lets you restrict the documents that can be used in re
 
 Once the Azure AI Search index is connected, your responses in the studio have document access based on the Microsoft Entra permissions of the logged in user.
 
-**Web app**
-
-If you are using a published [web app](./use-web-app.md), you need to redeploy it to upgrade to the latest version. The latest version of the web app includes the ability to retrieve the groups of the logged in user's Microsoft Entra account, cache it, and include the group IDs in each API request.
-
 **API**
 
 When using the API, pass the `filter` parameter in each API request. For example:
@@ -98,7 +94,7 @@ For more information about AI services security, see [Authenticate requests to A
 }
 ```
 * `my_group_ids` is the field name that you selected for **Permitted groups** during [fields mapping](../concepts/use-your-data.md#index-field-mapping).
-* `group_id1, group_id2` are groups attributed to the logged in user. The client application can retrieve and cache users' groups.
+* `group_id1, group_id2` are groups attributed to the logged in user. The client application can retrieve and cache users' groups using the [Microsoft Graph API](/graph/api/user-list-transitivememberof).
 
 
 ## Resource configuration
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新と不要な情報の削除"
}
```

### Explanation
この変更は、「on-your-data-configuration.md」ファイルにおいて、更新された日付と情報の整理を行ったものです。

1. **日付の更新**: ドキュメントの日付が`03/31/2025`から`04/15/2025`に変更され、情報の最新性を確保しています。

2. **不要な情報の削除**: Webアプリに関する説明の一部が削除されました。具体的には、Webアプリの再デプロイについての情報が削除され、これによりドキュメントがよりコンパクトで読みやすくなりました。この変更は、ユーザーが不必要な情報に惑わされず、必要な情報に集中しやすくすることを目的としています。

3. **API関連の詳細の追加**: APIを使用する際の指示が更新され、ユーザーがMicrosoft Graph APIを使用してグループ情報を取得およびキャッシュできることが明記されています。これにより、API利用時の手順が明確になり、実装の際の助けになります。

これらの変更は、ドキュメントの精度を向上させ、読者が必要な情報をより簡単に得られるようにするためのものです。全体として、読者の使いやすさが改善されています。

## articles/ai-services/openai/how-to/predicted-outputs.md{#item-212eb9}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 01/29/2025
+ms.date: 04/14/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -21,6 +21,7 @@ Predicted outputs can improve model response latency for chat completions calls
 - `gpt-4o-mini` version: `2024-07-18`
 - `gpt-4o` version: `2024-08-06`
 - `gpt-4o` version: `2024-11-20`
+- `gpt-4.1` version: `2025-04-14`
 
 ## API support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新と新モデルの追加"
}
```

### Explanation
この変更は、「predicted-outputs.md」ファイルに対するもので、主に日付の更新と新しいモデル情報の追加が含まれています。

1. **日付の更新**: ドキュメントの日付が`01/29/2025`から`04/14/2025`に変更され、内容が新しくなったことが示されています。

2. **新モデルの追加**: 新たに`gpt-4.1`モデルがリストに追加され、そのバージョンが`2025-04-14`であることが明示されています。これにより、ユーザーは最新のモデルに関する情報を得ることができ、選択肢を増やすことができます。

この変更は、ユーザーが利用可能な最新の情報を提供し、モデルの選択肢を広げることを目的としています。全体として、ドキュメントの最新性と有用性が向上しています。

## articles/ai-services/openai/how-to/prompt-caching.md{#item-1631df}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 03/20/2025
+ms.date: 04/14/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -31,6 +31,8 @@ Currently only the following models support prompt caching with Azure OpenAI:
 - `gpt-4o-mini-2024-07-18`
 - `gpt-4o-realtime-preview` (version 2024-12-17)
 - `gpt-4o-mini-realtime-preview` (version 2024-12-17)
+- `gpt-4.1-2025-04-14`
+- `gpt-4.1-nano-2025-04-14`
 
 > [!NOTE]
 > Prompt caching is now also available as part of model fine-tuning for `gpt-4o` and `gpt-4o-mini`. Refer to the fine-tuning section of the [pricing page](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) for details.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新と新モデルの追加"
}
```

### Explanation
この変更は、「prompt-caching.md」ファイルにおける日付の更新と新しいモデルの情報追加に関するものです。

1. **日付の更新**: ドキュメントの日付が`03/20/2025`から`04/14/2025`に変更され、内容の新しさを反映しています。

2. **新モデルの追加**: 新たに`gpt-4.1-2025-04-14`および`gpt-4.1-nano-2025-04-14`モデルがリストに追加され、これによりユーザーが利用可能なプロンプトキャッシングに対応したモデルの選択肢が増えています。

3. **プロンプトキャッシングについての注意事項**: プロンプトキャッシングが`gpt-4o`および`gpt-4o-mini`のモデル微調整の一部として利用可能になったことが明記されており、ユーザーが関連情報を確認できるよう、価格ページへのリンクも提供されています。

これらの変更は、ユーザーが最新のモデルと機能を理解し、利用するのに役立つように設計されています。全体として、ドキュメントの情報が充実し、最新性が保たれています。

## articles/ai-services/openai/how-to/realtime-audio.md{#item-482ba3}

<details>
<summary>Diff</summary>
````diff
@@ -27,7 +27,7 @@ The GPT 4o real-time models are available for global deployments in [East US 2 a
 - `gpt-4o-realtime-preview` (2024-12-17)
 - `gpt-4o-realtime-preview` (2024-10-01)
 
-See the [models and versions documentation](../concepts/models.md#gpt-4o-audio) for more information.
+See the [models and versions documentation](../concepts/models.md#audio-models) for more information.
 
 ## Get started
 
@@ -116,7 +116,7 @@ Events can be sent and received in parallel and applications should generally ha
 Often, the first event sent by the caller on a newly established `/realtime` session is a [`session.update`](../realtime-audio-reference.md#realtimeclienteventsessionupdate) payload. This event controls a wide set of input and output behavior, with output and response generation properties then later overridable using the [`response.create`](../realtime-audio-reference.md#realtimeclienteventresponsecreate) event.
 
 The [`session.update`](../realtime-audio-reference.md#realtimeclienteventsessionupdate) event can be used to configure the following aspects of the session:
-- Transcription of user input audio is opted into via the session's `input_audio_transcription` property. Specifying a transcription model (`whisper-1`) in this configuration enables the delivery of [`conversation.item.audio_transcription.completed`](../realtime-audio-reference.md#realtimeservereventconversationiteminputaudiotranscriptioncompleted) events.
+- Transcription of user input audio is opted into via the session's `input_audio_transcription` property. Specifying a transcription model (such as `whisper-1`) in this configuration enables the delivery of [`conversation.item.audio_transcription.completed`](../realtime-audio-reference.md#realtimeservereventconversationiteminputaudiotranscriptioncompleted) events.
 - Turn handling is controlled by the `turn_detection` property. This property's type can be set to `none` or `server_vad` as described in the [voice activity detection (VAD) and the audio buffer](#voice-activity-detection-vad-and-the-audio-buffer) section.
 - Tools can be configured to enable the server to call out to external services or functions to enrich the conversation. Tools are defined as part of the `tools` property in the session configuration.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの更新とトランスクリプションモデル情報の強化"
}
```

### Explanation
この変更は、「realtime-audio.md」ファイルにおけるリンクの修正とトランスクリプションモデルに関する説明の強化に関するものです。

1. **リンクの更新**: モデルおよびバージョンに関する文書へのリンクが`../concepts/models.md#gpt-4o-audio`から`../concepts/models.md#audio-models`に変更され、より適切なセクションに誘導する形になっています。この変更により、ユーザーは関連情報をより簡単に探し出すことができるようになります。

2. **トランスクリプションモデル情報の強化**: トランスクリプションに関する説明が、「whisper-1」という特定のモデルを指定することで、音声トランスクリプションの完了イベントを受け取ることができるという情報が追加されました。この構成により、ユーザーが実際にどのモデルを使用するか選択する際の指針がより明確になっています。

これらの変更は、ユーザーがリアルタイムオーディオ機能を理解し、効果的に活用するための情報を提供することを目的としています。全体として、ドキュメントの利便性と明確性が向上しています。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -131,9 +131,41 @@ response = client.chat.completions.create(
 print(response.model_dump_json(indent=2))
 ```
 
+# [C#](#tab/csharp)
+
+```c#
+using Azure.AI.OpenAI;
+using Azure.AI.OpenAI.Chat;
+using Azure.Identity;
+using OpenAI.Chat;
+
+AzureOpenAIClient openAIClient = new(
+    new Uri("https://YOUR-RESOURCE-NAME.openai.azure.com/"),
+    new DefaultAzureCredential());
+ChatClient chatClient = openAIClient.GetChatClient("o3-mini"); //model deployment name
+
+ChatCompletionOptions options = new ChatCompletionOptions
+{
+    MaxOutputTokenCount = 100000
+};
+
+#pragma warning disable AOAI001 //currently required to use MaxOutputTokenCount
+
+options.SetNewMaxCompletionTokensPropertyEnabled(true);
+
+ChatCompletion completion = chatClient.CompleteChat(
+    [
+
+        new UserChatMessage("Testing 1,2,3")
+    ],
+    options); // Pass the options to the CompleteChat method
+
+Console.WriteLine($"{completion.Role}: {completion.Content[0].Text}");
+```
+
 ---
 
-**Output:**
+**Python Output:**
 
 ```json
 {
@@ -270,7 +302,8 @@ response = client.chat.completions.create(
         {"role": "developer","content": "You are a helpful assistant."}, # optional equivalent to a system message for reasoning models 
         {"role": "user", "content": "What steps should I think about when writing my first Python API?"},
     ],
-    max_completion_tokens = 5000
+    max_completion_tokens = 5000,
+    reasoning_effort = "medium" # low, medium, or high
 
 )
 
@@ -301,12 +334,46 @@ response = client.chat.completions.create(
         {"role": "developer","content": "You are a helpful assistant."}, # optional equivalent to a system message for reasoning models 
         {"role": "user", "content": "What steps should I think about when writing my first Python API?"},
     ],
-    max_completion_tokens = 5000
+    max_completion_tokens = 5000,
+    reasoning_effort = "medium" # low, medium, or high
 )
 
 print(response.model_dump_json(indent=2))
 ```
 
+# [C#](#tab/csharp)
+
+```csharp
+using Azure.AI.OpenAI;
+using Azure.AI.OpenAI.Chat;
+using Azure.Identity;
+using OpenAI.Chat;
+
+AzureOpenAIClient openAIClient = new(
+    new Uri("https://YOUR-RESOURCE-NAME.openai.azure.com/"),
+    new DefaultAzureCredential());
+ChatClient chatClient = openAIClient.GetChatClient("o3-mini"); //model deployment name
+
+ChatCompletionOptions options = new ChatCompletionOptions
+{
+    ReasoningEffortLevel = ChatReasoningEffortLevel.Low,
+    MaxOutputTokenCount = 100000
+};
+
+#pragma warning disable AOAI001 //currently required to use MaxOutputTokenCount
+
+options.SetNewMaxCompletionTokensPropertyEnabled(true);
+
+ChatCompletion completion = chatClient.CompleteChat(
+    [
+        new DeveloperChatMessage("You are a helpful assistant."),
+        new UserChatMessage("Testing 1,2,3")
+    ],
+    options); // Pass the options to the CompleteChat method
+
+Console.WriteLine($"{completion.Role}: {completion.Content[0].Text}");
+```
+
 ---
 
 ## Markdown output
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#のサンプルコードの追加と推論努力レベルの指定"
}
```

### Explanation
この変更は、「reasoning.md」ファイルにおいて、新たにC#のサンプルコードを追加し、推論の努力レベルを指定するオプションを加えたことに関するものです。

1. **C#サンプルコードの追加**: C#におけるAzure OpenAIを利用したチャット機能の具体例が新たに追加されました。このコードスニペットでは、Azure OpenAIクライアントの作成、チャットクライアントの取得、チャット完成オプションの設定が示されています。また、ユーザーがメッセージを入力し、その結果を出力する方法も示されています。

2. **推論努力レベルの指定**: PythonコードおよびC#コードの両方において、推論の努力レベルを設定する`reasoning_effort`のパラメータが導入されました。このパラメータにより、利用者は「low」「medium」「high」のいずれかの値を指定でき、より詳細で柔軟な応答を得るための選択肢が提供されます。

3. **複数の言語での一貫性**: PythonとC#でのサンプルコードが追加され、ユーザーは自分のニーズに応じてどちらの言語でも利用できる形となっています。これにより、ドキュメントの利便性が向上し、さまざまな開発者が利用しやすくなっています。

全体として、この変更はユーザーにとっての情報の明確性と有用性を高め、実際のコード例を通じて理解を深める手助けをすることを目的としています。

## articles/ai-services/openai/how-to/responses.md{#item-b9757d}

<details>
<summary>Diff</summary>
````diff
@@ -41,8 +41,10 @@ The responses API is currently available in the following regions:
 ### Model support
 
 - `gpt-4o` (Versions: `2024-11-20`, `2024-08-06`, `2024-05-13`)
-- `gpt-4o-mini` (Versions: `2024-07-18`)
+- `gpt-4o-mini` (Version: `2024-07-18`)
 - `computer-use-preview`
+- `gpt-4.1` (Version: `2025-04-14`)
+- `gpt-4.1-nano` (Version: `2025-04-14`)
 
 Not every model is available in the regions supported by the responses API. Check the [models page](../concepts/models.md) for model region availability.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルサポートの更新と新モデルの追加"
}
```

### Explanation
この変更は、「responses.md」ファイルにおけるモデルサポートの情報を更新し、新たなモデルを追加したことに関するものです。

1. **モデルサポートの表現の変更**: `gpt-4o-mini`のバージョン表記が単数形の「Versions:」から「Version:」に変更され、より正確な情報が提供されています。

2. **新モデルの追加**: 新たに`gpt-4.1`および`gpt-4.1-nano`という2つのモデルが追加されました。これらはどちらも `2025-04-14` がバージョンとして指定されています。

3. **情報の明確化**: モデルが全ての地域で利用可能ではない場合があることを明記しており、ユーザーがモデルの地域的な可用性を確認できるリンクを提供しています。これにより、ユーザーは自分の使用している地域で利用可能なモデルを正確に把握する手助けとなります。

全体として、この変更はユーザーが利用可能なモデルの最新情報を把握しやすくすることを目的としており、より明確で正確な情報提供を実現しています。

## articles/ai-services/openai/how-to/structured-outputs.md{#item-cc2557}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 02/28/2025
+ms.date: 04/14/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -31,6 +31,8 @@ Structured outputs make a model follow a [JSON Schema](https://json-schema.org/o
 - `gpt-4o-mini` version: `2024-07-18`
 - `gpt-4o` version: `2024-08-06`
 - `gpt-4o` version: `2024-11-20`
+- `gpt-4.1` version `2025-04-14`
+- `gpt-4.1-nano` version (`2025-14-2025`)
 
 ## API support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新と新モデルの追加"
}
```

### Explanation
この変更は、「structured-outputs.md」ファイルにおいて、文書の日付を更新し、新たにモデルを追加したことに関するものです。

1. **日付の更新**: ドキュメントの日付が「02/28/2025」から「04/14/2025」に更新されました。これにより、最新の情報が反映されるようになっています。

2. **新モデルの追加**: 新たに`gpt-4.1`と`gpt-4.1-nano`モデルが追加され、両モデルのバージョンがそれぞれ「2025-04-14」とされています。これにより、ユーザーは新しいモデルの存在とそのバージョンを確認できるようになっています。

3. **モデルに関する情報の拡充**: これにより、利用可能なモデルに関する情報が充実し、ユーザーは最新の進展に基づいて選択肢を更新できます。

全体として、この変更は文書の正確性と最新性を保つためのものであり、ユーザーが利用可能なモデルについて正確な情報を得る手助けをしています。

## articles/ai-services/openai/how-to/use-web-app.md{#item-802413}

<details>
<summary>Diff</summary>
````diff
@@ -290,11 +290,11 @@ The JSON to paste in the Advanced edit JSON editor is:
 
 ## Connecting to Prompt Flow as a data source
 
-[Prompt flows](/azure/ai-foundry/how-to/flow-develop) allow you to define highly customizable RAG and processing logic on a user's queries. 
+[Prompt flows](../../../ai-foundry/how-to/flow-develop.md) allow you to define highly customizable RAG and processing logic on a user's queries.
 
 ### Creating and deploying your prompt flow in Azure AI Foundry portal
 
-Follow [this tutorial](/azure/ai-foundry/tutorials/deploy-copilot-ai-studio) to create, test, and deploy an inferencing endpoint for your prompt flow in [Azure AI Foundry portal](https://ai.azure.com/).
+Follow [this tutorial](../../../ai-foundry/how-to/flow-deploy.md) to create, test, and deploy an inferencing endpoint for your prompt flow in [Azure AI Foundry portal](https://ai.azure.com/).
 
 ### Enable underlying citations from your prompt flow
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの修正"
}
```

### Explanation
この変更は、「use-web-app.md」ファイルにおいて、内部リンクの修正を行ったことに関するものです。

1. **リンクの修正**: テキスト内のいくつかのリンクパスが修正されました。具体的には、`/azure/ai-foundry/how-to/flow-develop` から `../../../ai-foundry/how-to/flow-develop.md` に、また `/azure/ai-foundry/tutorials/deploy-copilot-ai-studio` から `../../../ai-foundry/how-to/flow-deploy.md` に変更されています。これにより、リンクがより正確に関連するページを指すようになっています。

2. **内部参照の明確化**: 修正されたリンクは、ユーザーが特定のチュートリアルやガイドラインにアクセスしやすくするためのものです。この変更により、ユーザーは必要な情報に迅速にたどり着けるようになります。

全体として、この変更は文書のナビゲーションを改善し、ユーザーが関連情報を容易に見つけられるようにするためのものです。

## articles/ai-services/openai/includes/api-surface.md{#item-a25fa2}

<details>
<summary>Diff</summary>
````diff
@@ -23,7 +23,7 @@ Each API surface/specification encapsulates a different set of Azure OpenAI capa
 |:---|:----|:----|:----|:---|
 | **Control plane** | [`2024-06-01-preview`](/rest/api/aiservices/accountmanagement/operation-groups?view=rest-aiservices-accountmanagement-2024-06-01-preview&preserve-view=true) | [`2024-10-01`](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices) | Azure OpenAI shares a common control plane with all other Azure AI Services. The control plane API is used for things like [creating Azure OpenAI resources](/rest/api/aiservices/accountmanagement/accounts/create?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), [model deployment](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), and other higher level resource management tasks. The control plane also governs what is possible to do with capabilities like Azure Resource Manager, Bicep, Terraform, and Azure CLI.|
 | **Data plane - authoring** | `2025-03-01-preview` | `2024-10-21` | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
-| **Data plane - inference** | [`2025-03-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-10-21`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, speech/whisper, on your data, Dall-e, assistants, etc. |
+| **Data plane - inference** | [`2025-03-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-10-21`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, audio, on your data, Dall-e, assistants, etc. |
 
 ## Authentication
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データプレーン推論APIの説明修正"
}
```

### Explanation
この変更は、「api-surface.md」ファイルにおいて、データプレーンの推論APIに関する説明を修正したことに関するものです。

1. **説明の修正**: データプレーン推論APIの説明が更新されました。具体的には、「speech/whisper」が「audio」に変更されたことで、音声関連機能の説明がより包括的になっています。この変更は、ユーザーが利用可能な機能を正確に理解できるようにするためのものです。

2. **一貫性の向上**: 用語を「audio」に統一することで、APIが提供する機能をより正確に表現しています。これにより、文書全体の一貫性が強化され、ユーザーにとっての理解が促進されます。

全体として、この変更はデータプレーン推論APIの記述をより正確にし、ユーザーが各機能の内容を容易に把握できるようにするために行われました。

## articles/ai-services/openai/includes/api-versions/latest-inference.md{#item-b30a63}

<details>
<summary>Diff</summary>
````diff
@@ -645,7 +645,7 @@ Transcribes audio into the input language.
 | Name | In | Required | Type | Description |
 |------|------|----------|------|-----------|
 | endpoint | path | Yes | string<br>url | Supported Azure OpenAI endpoints (protocol and hostname, for example: `https://aoairesource.openai.azure.com`. Replace "aoairesource" with your Azure OpenAI resource name). https://{your-resource-name}.openai.azure.com |
-| deployment-id | path | Yes | string | Deployment ID of the whisper model. |
+| deployment-id | path | Yes | string | Deployment ID of the speech to text model.<br/><br/>For information about supported models, see [/azure/ai-services/openai/concepts/models#audio-models]. |
 | api-version | query | Yes | string | API version |
 
 ### Request Header
@@ -731,7 +731,7 @@ Transcribes and translates input audio into English text.
 | Name | In | Required | Type | Description |
 |------|------|----------|------|-----------|
 | endpoint | path | Yes | string<br>url | Supported Azure OpenAI endpoints (protocol and hostname, for example: `https://aoairesource.openai.azure.com`. Replace "aoairesource" with your Azure OpenAI resource name). https://{your-resource-name}.openai.azure.com |
-| deployment-id | path | Yes | string | Deployment ID of the whisper model which was deployed. |
+| deployment-id | path | Yes | string | Deployment ID of the whisper model which was deployed.<br/><br/>For information about supported models, see [/azure/ai-services/openai/concepts/models#audio-models]. |
 | api-version | query | Yes | string | API version |
 
 ### Request Header
@@ -2318,6 +2318,6 @@ Completions extensions aren't part of the latest GA version of the Azure OpenAI
 
 The Chat message object isn't part of the latest GA version of the Azure OpenAI data plane inference spec.
 
-### Text to speech
+### Text to speech (Preview)
 
 Is not currently part of the latest Azure OpenAI GA version of the Azure OpenAI data plane inference spec. Refer to the latest [preview](../../reference-preview.md) version for this capability.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルに関する説明修正とプレビューラベル追加"
}
```

### Explanation
この変更は、「latest-inference.md」ファイルにおけるモデル関連の説明の更新と、テキスト読み上げセクションにプレビューラベルを追加したことに関するものです。

1. **モデル説明の修正**: `deployment-id` の説明が更新され、「whisper model」を「speech to text model」に変更されました。これにより、音声認識モデルに対応することが明確になり、関連する情報へのリンクも追加されました。この修正は、ユーザーが利用可能なモデルの範囲を理解しやすくします。

2. **プレビューラベルの追加**: 「Text to speech」のセクションに「(Preview)」というラベルが追加されました。これにより、この機能が現在の一般提供（GA）版には含まれていないことが強調され、ユーザーに対して最新のプレビュー版の情報への参照が促されています。

3. **一貫性の向上**: 全体の文書内での用語と説明が一貫性を持つように見直されており、ユーザーはAPIの使用方法をより明確に理解できます。この変更は、ドキュメントの正確性と可用性を向上させるための重要なステップです。

全体として、この変更はAPIの説明を明確化し、ユーザーがモデルと機能についてより理解しやすくすることを目的としています。

## articles/ai-services/openai/includes/content-filter-configurability.md{#item-11f064}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ recommendations: false
 
 
 
-Azure OpenAI Service includes default safety settings applied to all models, excluding Azure OpenAI Whisper. These configurations provide you with a responsible experience by default, including content filtering models, blocklists, prompt transformation, [content credentials](../concepts/content-credentials.md), and others. [Read more about it here](/azure/ai-services/openai/concepts/default-safety-policies). 
+Azure OpenAI Service includes default safety settings applied to all models, excluding audio API models such as Whisper. These configurations provide you with a responsible experience by default, including content filtering models, blocklists, prompt transformation, [content credentials](../concepts/content-credentials.md), and others. [Read more about it here](/azure/ai-services/openai/concepts/default-safety-policies). 
 
 All customers can also configure content filters and create custom safety policies that are tailored to their use case requirements. The configurability feature allows customers to adjust the settings, separately for prompts and completions, to filter content for each content category at different severity levels as described in the table below. Content detected at the 'safe' severity level is labeled in annotations but is not subject to filtering and isn't configurable.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisperモデルを除外するための説明修正"
}
```

### Explanation
この変更は、「content-filter-configurability.md」ファイルにおいて、Azure OpenAIサービスのデフォルト安全設定に関する説明を修正したことに関するものです。

1. **モデルの定義の明確化**: 説明内で「Azure OpenAI Whisper」との表現が「audio API models such as Whisper」に変更されました。これにより、Whisperが音声APIモデルの一部であることが明確になり、他の音声APIモデルも含まれることが示されています。

2. **安全設定の透明性**: デフォルトの安全設定が適用されるモデルの範囲を明確にすることで、ユーザーはどのモデルがこの設定の対象となるのかを理解しやすくなります。この変更は、ユーザーが安全性やフィルタリング対策についての理解を深めるのに役立ちます。

3. **一貫性の向上**: APIやモデル名についてより適切な表現を用いることで、文書全体の一貫性が向上しています。これによって、ユーザーは安全設定についてより正確に理解できるようになります。

全体として、この変更はAzure OpenAIサービスのデフォルト安全設定に関する理解を深めることを目的とし、ユーザーにとっての情報提供の質を向上させるものです。

## articles/ai-services/openai/includes/language-overview/dotnet.md{#item-46e881}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,7 @@ The Azure OpenAI client library for .NET is a companion to the [official OpenAI
 
 The preview release has access to the latest features.
 
-[Source code](https://github.com/Azure/azure-sdk-for-net/tree/Azure.AI.OpenAI_2.1.0-beta.2/sdk/openai/Azure.AI.OpenAI/src) | [Package (NuGet)](https://www.nuget.org/packages/Azure.AI.OpenAI/2.1.0-beta.2) | [API reference documentation](../../reference.md) | [Package reference documentation](/dotnet/api/overview/azure/ai.openai-readme?view=azure-dotnet-preview&preserve-view=true)   [Samples](https://github.com/Azure/azure-sdk-for-net/tree/Azure.AI.OpenAI_2.1.0-beta.2/sdk/openai/Azure.AI.OpenAI/tests/Samples)
+[Source code](https://github.com/Azure/azure-sdk-for-net/tree/Azure.AI.OpenAI_2.1.0-beta.2/sdk/openai/Azure.AI.OpenAI/src) | [Package (NuGet)](https://www.nuget.org/packages/Azure.AI.OpenAI/2.2.0-beta.4) | [API reference documentation](../../reference.md) | [Package reference documentation](/dotnet/api/overview/azure/ai.openai-readme?view=azure-dotnet-preview&preserve-view=true)   [Samples](https://github.com/Azure/azure-sdk-for-net/tree/Azure.AI.OpenAI_2.2.0-beta.4/sdk/openai/Azure.AI.OpenAI/tests/Samples)
 
 
 ## Azure OpenAI API version support
@@ -266,6 +266,41 @@ bytes.ToStream().CopyTo(stream);
 
 - [C# DALL-E quickstart guide](/azure/ai-services/openai/dall-e-quickstart?tabs=dalle3%2Ccommand-line%2Ckeyless%2Ctypescript-keyless&pivots=programming-language-csharp)
 
+## Reasoning models
+
+```csharp
+using Azure.AI.OpenAI;
+using Azure.AI.OpenAI.Chat;
+using Azure.Identity;
+using OpenAI.Chat;
+
+
+AzureOpenAIClient openAIClient = new(
+    new Uri("https://YOUR-RESOURCE-NAME.openai.azure.com/"),
+    new DefaultAzureCredential());
+ChatClient chatClient = openAIClient.GetChatClient("o3-mini");
+
+// Create ChatCompletionOptions and set the reasoning effort level
+ChatCompletionOptions options = new ChatCompletionOptions
+{
+    ReasoningEffortLevel = ChatReasoningEffortLevel.Low,
+    MaxOutputTokenCount = 100000
+};
+
+#pragma warning disable AOAI001 //currently required to use MaxOutputTokenCount
+
+options.SetNewMaxCompletionTokensPropertyEnabled(true);
+
+ChatCompletion completion = chatClient.CompleteChat(
+    [
+
+        new UserChatMessage("Testing 1,2,3")
+    ],
+    options); // Pass the options to the CompleteChat method
+
+Console.WriteLine($"{completion.Role}: {completion.Content[0].Text}");
+```
+
 
 ## Completions (legacy)
 
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": ".NET用Azure OpenAIライブラリに推論モデルの例を追加"
}
```

### Explanation
この変更は、「dotnet.md」ファイルにおいて、Azure OpenAIライブラリに推論モデルに関する新しい例を追加したことに関するものです。

1. **新しいライブラリバージョンの参照**: NuGetパッケージのバージョンが「2.1.0-beta.2」から「2.2.0-beta.4」に更新され、最新の機能にアクセスできることが強調されています。この変更によって、ユーザーは常に最新のライブラリを使用していることを確認できます。

2. **推論モデルのコード例の追加**: 新たに「Reasoning models」というセクションが導入され、Azure OpenAIクライアントを使用して推論モデル「o3-mini」を操作するための具体的なC#のコード例が追加されています。このコードは、推論の努力レベルを設定し、チャットメッセージの作成方法を示しています。

   - **コード構成**: 使用されるライブラリのインポート、クライアントの初期化、オプションの設定、そしてチャットの完了取得までの流れが具体的に提示されています。これにより、開発者は如何にして推論機能を利用できるかを容易に理解できるようになります。

3. **フィードバックと警告の抑制**: コード内には警告を抑制するための指示が含まれており、ユーザーが設定を変更する際の問題を事前に回避できるようになっています。

全体として、この変更はAzure OpenAIライブラリの機能を拡充し、ユーザーに対して推論モデルにアクセスするための具体的な手段を提供することを目的としています。この新しいセクションは、プログラミング言語C#を使用する開発者にとって非常に有益です。

## articles/ai-services/openai/includes/language-overview/go.md{#item-a289f2}

<details>
<summary>Diff</summary>
````diff
@@ -190,12 +190,12 @@ import (
 )
 
 func main() {
-	azureOpenAIKey := os.Getenv("AOAI_WHISPER_API_KEY")
+	azureOpenAIKey := os.Getenv("AOAI_AUDIO_API_KEY")
 
 	// Ex: "https://<your-azure-openai-host>.openai.azure.com"
-	azureOpenAIEndpoint := os.Getenv("AOAI_WHISPER_ENDPOINT")
+	azureOpenAIEndpoint := os.Getenv("AOAI_AUDIO_ENDPOINT")
 
-	modelDeploymentID := os.Getenv("AOAI_WHISPER_MODEL")
+	modelDeploymentID := os.Getenv("AOAI_AUDIO_MODEL")
 
 	if azureOpenAIKey == "" || azureOpenAIEndpoint == "" || modelDeploymentID == "" {
 		fmt.Fprintf(os.Stderr, "Skipping example, environment variables missing\n")
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "環境変数名の修正"
}
```

### Explanation
この変更は、「go.md」ファイルにおいて、Azure OpenAIの環境変数名を正しいものに修正したことに関するものです。

1. **環境変数の更新**: 
   - 「AOAI_WHISPER_API_KEY」、「AOAI_WHISPER_ENDPOINT」、および「AOAI_WHISPER_MODEL」という環境変数名が、音声APIに関連する正しい環境変数名である「AOAI_AUDIO_API_KEY」、「AOAI_AUDIO_ENDPOINT」、「AOAI_AUDIO_MODEL」に置き換えられました。この変更により、利用者が正しい環境変数を使用してAzure OpenAIサービスにアクセスできるようになります。

2. **コードの一貫性**: 環境変数名の修正は、ドキュメントの使い勝手を向上させ、ユーザーが正しい設定を迅速に行えるようにします。これにより、開発者は実際のAPIキーやエンドポイントが何であるかを混乱することなく理解できるようになります。

3. **エラーハンドリングの改善**: 環境変数が空の場合に出力されるエラーメッセージはそのままであり、ユーザーが必要な設定を行っていない場合に明確なフィードバックが提供されます。

全体として、この修正は、Azure OpenAIの音声APIを利用する際の環境設定を正確にし、開発者がスムーズにアプリケーションを構築できるようにするためのものであり、バグ修正として位置付けられています。

## articles/ai-services/openai/includes/model-matrix/standard-audio.md{#item-1d8db7}

<details>
<summary>Diff</summary>
````diff
@@ -6,16 +6,16 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 10/25/2024
+ms.date: 4/15/2025
 ---
 
-| **Region**   | **tts**, **001**   | **tts-hd**, **001**   | **whisper**, **001**   |
-|:-----------------|:----------------:|:-------------------:|:--------------------:|
-| eastus2          | -            | -               | ✅                 |
-| northcentralus   | ✅             | ✅                | ✅                 |
-| norwayeast       | -            | -               | ✅                 |
-| southindia       | -            | -               | ✅                 |
-| swedencentral    | ✅             | ✅                | ✅                 |
-| switzerlandnorth | -            | -               | ✅                 |
-| uaenorth         | -            | -               | ✅                 |
-| westeurope       | -            | -               | ✅                 |
+| **Region**   | **tts**, **001**   | **tts-hd**, **001**   | **whisper**, **001**  |  **gpt-4o-mini-tts**, **001** | **gpt-4o-transcribe**, **001**   | **gpt-4o-mini-transcribe**, **001**   |
+|:-----------------|:----------------:|:-------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|
+| eastus2          | - | - | ✅ | - | ✅ | ✅ |
+| northcentralus   | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
+| norwayeast       | - | - | ✅ | - | ✅ | ✅ |
+| southindia       | - | - | ✅ | - | ✅ | ✅ |
+| swedencentral    | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
+| switzerlandnorth | - | - | ✅ | - | ✅ | ✅ |
+| uaenorth         | - | - | ✅ | - | ✅ | ✅ |
+| westeurope       | - | - | ✅ | - | ✅ | ✅ |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "音声モデルマトリックスに新しいモデルを追加"
}
```

### Explanation
この変更は、「standard-audio.md」ファイルにおいて、音声モデルに関する地域別サポートのテーブルに新しいモデルを追加したことに関連しています。

1. **日付の更新**: 最初に、更新日が「2024年10月25日」から「2025年4月15日」に変更され、情報の鮮度が保たれるようにされています。

2. **モデル情報の拡充**: テーブルの構造が変更され、新たに「gpt-4o-mini-tts」、「gpt-4o-transcribe」、および「gpt-4o-mini-transcribe」という新しいモデルが追加されました。これにより、ユーザーはこれらの新しいモデルがどの地域で利用可能かを確認できるようになります。

3. **地域別サポートの明示化**: 新しいモデルの導入に伴って、各地域におけるサポート状況が明示的に示されています。例えば、「eastus2」や「northcentralus」などの特定の地域において、新しいモデルが利用可能であることがテーブル内で示されています。

この変更により、開発者やユーザーは、利用可能な音声モデルの選択肢が増えたことを認識し、より多くの地域でこれらの機能を利用できることを理解することができます。全体として、音声サービスの利用可能性を向上させるための重要な情報が提供されています。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -6,32 +6,32 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 04/04/2025
+ms.date: 04/14/2025
 ---
 
-| **Region**     | **gpt-4.5-preview**, **2025-02-27**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4o-audio-preview**, **2024-12-17**   | **gpt-4o-mini-realtime-preview**, **2024-12-17**   | **gpt-4o-mini-audio-preview**, **2024-12-17**   | **gpt-4**, **turbo-2024-04-09**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **2**   |
-|:-------------------|:-----------------------------------:|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:----------------------------------------:|:------------------------------------------------:|:---------------------------------------------:|:-------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|
-| australiaeast      | -                               | ✅                        | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| brazilsouth        | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| canadaeast         | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| eastus             | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | ✅                                          | ✅                            | ✅                              | ✅                              | ✅                              |
-| eastus2            | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | ✅                                          | ✅                            | ✅                              | ✅                              | ✅                              |
-| francecentral      | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| germanywestcentral | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| italynorth         | -                               | ✅                        | ✅                   | -                          | -                       | -                      | -                      | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | -                           | ✅                              | ✅                              | ✅                              |
-| japaneast          | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| koreacentral       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| northcentralus     | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| norwayeast         | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| polandcentral      | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| southafricanorth   | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| southcentralus     | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| southindia         | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| spaincentral       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| swedencentral      | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| switzerlandnorth   | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| uaenorth           | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| uksouth            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| westeurope         | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| westus             | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| westus3            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| **Region**     | **gpt-4.1**, **2025-04-14**   | **gpt-4.5-preview**, **2025-02-27**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4o-audio-preview**, **2024-12-17**   | **gpt-4o-mini-realtime-preview**, **2024-12-17**   | **gpt-4o-mini-audio-preview**, **2024-12-17**   | **gpt-4**, **turbo-2024-04-09**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **2**   |
+|:-------------------|:---------------------------:|:-----------------------------------:|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:----------------------------------------:|:------------------------------------------------:|:---------------------------------------------:|:-------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|
+| australiaeast      | -                       | -                               | ✅                        | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
+| brazilsouth        | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| canadaeast         | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
+| eastus             | -                       | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | ✅                                          | ✅                            | ✅                              | ✅                              | ✅                              |
+| eastus2            | ✅                        | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | ✅                                          | ✅                            | ✅                              | ✅                              | ✅                              |
+| francecentral      | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
+| germanywestcentral | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
+| italynorth         | -                       | -                               | ✅                        | ✅                   | -                          | -                       | -                      | -                      | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | -                           | ✅                              | ✅                              | ✅                              |
+| japaneast          | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| koreacentral       | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| northcentralus     | -                       | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| norwayeast         | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| polandcentral      | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| southafricanorth   | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| southcentralus     | -                       | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
+| southindia         | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| spaincentral       | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
+| swedencentral      | ✅                        | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
+| switzerlandnorth   | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
+| uaenorth           | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| uksouth            | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
+| westeurope         | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
+| westus             | -                       | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| westus3            | -                       | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルマトリックスの更新と新モデルの追加"
}
```

### Explanation
この変更は、「standard-global.md」ファイルにおいて、モデルマトリックスの内容を更新し、新しいモデルを追加したことに関連しています。

1. **日付の更新**: 更新日が「2025年4月4日」から「2025年4月14日」に変更され、最新の情報が反映されるようになっています。

2. **新しいモデルの追加**: テーブルに「gpt-4.1」という新しいモデルが追加されました。これにより、ユーザーは新しいモデルがどの地域で利用可能かを確認できるようになり、利用の幅が広がります。

3. **地域別サポートの詳細化**: 各地域において新しいモデルや他のモデルがどのようにサポートされているかを詳しく示しています。例えば、多くの地域で新しい「gpt-4.1」モデルが利用可能であることが確認でき、既存のモデルに比べてまた一歩進んだ選択肢が提供されることになります。

4. **テーブルの整備**: テーブルの整形が行われており、視認性が向上しています。各モデルのリリース日や地域別のサポート状況が一目で理解できるようになっています。

この変更は、Azure OpenAIサービスの利用者にとって重要な情報の更新を含んでおり、特に新モデルのリリースは開発やサービスの拡充に直結するため、非常に有益です。また、ドキュメントの整備により、情報の伝わりやすさも向上しています。

## articles/ai-services/openai/includes/text-to-speech-dotnet.md{#item-fea66a}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ recommendations: false
 ## Prerequisites
 
 - An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
-- An Azure OpenAI resource with a Whisper model deployed in a [supported region](../concepts/models.md#whisper-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure OpenAI resource with a text to speech model (such as `tts`) deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 - [The .NET 8.0 SDK](https://dotnet.microsoft.com/en-us/download)
 
 ### Microsoft Entra ID prerequisites
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキストから音声へのモデル要件の更新"
}
```

### Explanation
この変更は、「text-to-speech-dotnet.md」ファイルにおいて、必要な条件の記述を更新したことに関連しています。

1. **モデルの変更**: 以前は「Whisperモデル」が必要とされていましたが、新しい変更では「テキストから音声へのモデル（例えば`tts`）」が必要とされるように記述が変更されています。これにより、ユーザーにより明確な選択肢が提供され、テキストから音声への機能の利用が促進されます。

2. **地域の参照**: モデルの展開が「サポートされている地域」であることは変わっていませんが、具体的なモデルの指定によって、ユーザーが正しいリソースを選択する助けとなります。新しいリンク先により、ユーザーは音声モデルの対応状況をより正確に確認できるようになります。

3. **文書の整合性**: この変更は全体として、ドキュメントの整合性と明確さを向上させる役割を果たしています。ユーザーが使用するモデルやリソースを理解しやすくするために、情報が正確に更新されています。

この変更は、テキストから音声へのサービスを利用する開発者やユーザーにとって非常に重要であり、実際の利用状況に即した最新の情報を反映しています。

## articles/ai-services/openai/includes/whisper-dotnet.md{#item-562a58}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.date: 3/11/2025
 ## Prerequisites
 
 - An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
-- An Azure OpenAI resource with a Whisper model deployed in a [supported region](../concepts/models.md#whisper-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 - [The .NET 8.0 SDK](https://dotnet.microsoft.com/en-us/download)
 
 ### Microsoft Entra ID prerequisites
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スピーチからテキストへのモデル要件の更新"
}
```

### Explanation
この変更は、「whisper-dotnet.md」ファイルにおいて、必要な条件の記述を更新したことに関連しています。

1. **モデルの変更**: 以前は「Whisperモデル」が必要とされていましたが、記述が「スピーチからテキストへのモデル」に変更されました。これにより、具体的な利用シーンに基づいて情報が明確化され、ユーザーにとって分かりやすくなっています。

2. **地域の参照変更**: 「サポートされている地域」での展開に関する要件は変わりませんが、新しい文言により、スピーチからテキストへのモデルの適合性について、ユーザーは正しいリソースを選択しやすくなっています。

3. **文書の整合性と明確性の向上**: 変更によって、記事が一貫性を持ち、正しい情報を反映することが強化されています。利用者は、文書を通じてより具体的な取り扱いが分かりやすくなり、特定のモデルを利用する際の要件が明確になります。

この変更は、Azure OpenAIサービスを利用してスピーチをテキストに変換する機能に関心のある開発者やユーザーにとって、重要な情報の正確性を提供するものであり、利用体験の向上に寄与しています。

## articles/ai-services/openai/includes/whisper-javascript.md{#item-3ee990}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: eric-urban
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
-- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 ### Microsoft Entra ID prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スピーチからテキストへのモデル要件の更新"
}
```

### Explanation
この変更は、「whisper-javascript.md」ファイル内で、必要な条件に関する記述が更新されたことを示しています。

1. **モデルの変更**: 以前の記述では、「サポートされている地域に作成されたAzure OpenAIリソース」としてWhisperモデルが使われていましたが、新しい変更では「スピーチからテキストへのモデル」と具体的に記載されるようになりました。これにより、ユーザーは特定のモデルの選択肢をより明確に理解できます。

2. **地域の参照**: 「サポートされている地域」でのモデル展開要件は保持されていますが、モデルの種類が明確に指定されたことで、より適切なリソース選択が可能になります。

3. **文書の整合性と明確性**: 変更によって、文書の情報が一貫性を持ち、技術的な詳細が適切に反映されています。これにより、ユーザーはAzure OpenAIサービスを利用する際に、必要なリソースや条件をより簡単に理解することができます。

この変更は、開発者がJavaScriptを使用してスピーチをテキストに変換する際に必要な要件を明確に示しており、利用者にとっての利便性を向上させる重要な情報となります。

## articles/ai-services/openai/includes/whisper-powershell.md{#item-7db269}

<details>
<summary>Diff</summary>
````diff
@@ -14,8 +14,7 @@ author: eric-urban
 
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - <a href="https://aka.ms/installpowershell" target="_blank">You can use either the latest version, PowerShell 7, or Windows PowerShell 5.1.</a>
-- An Azure OpenAI Service resource with a model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
-- An Azure OpenAI Service resource with either the `gpt-35-turbo` or the `gpt-4` models deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
+- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 ## Set up
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スピーチからテキストへのモデル要件の更新"
}
```

### Explanation
この変更は、「whisper-powershell.md」ファイルにおいて、必要な条件に関する記述が更新されたことを示しています。

1. **モデルの変更**: 以前は「Azure OpenAI Serviceリソースにデプロイされたモデル」や「`gpt-35-turbo`または`gpt-4`モデル」が必要とされていましたが、変更後は「スピーチからテキストへのモデル」がデプロイされることが求められるようになりました。これにより、ユーザーは具体的な利用シーンに合わせたモデルを理解しやすくなっています。

2. **不要な記述の削除**: 以前の文書からは複数のモデルに関する記述が削除され、一貫性のある情報提供が強化されています。これにより、文書が簡潔になり、ユーザーが必要な条件を理解しやすくなります。

3. **文書の明確化**: 新しい条件によって、文書全体の整合性が改善され、ユーザーがどのようにAzure OpenAIサービスを利用可能であるかの具体的な指針が提供されています。

この変更は、PowerShellを使用してスピーチをテキストに変換する機能に関心があるユーザーにとって、より明確かつ正確な情報を提供するものであり、利用体験向上に寄与します。

## articles/ai-services/openai/includes/whisper-python.md{#item-e61179}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.date: 3/19/2024
 ## Prerequisites
 
 - An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
-- An Azure OpenAI resource with a Whisper model deployed in a [supported region](../concepts/models.md#whisper-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 - [Python 3.8 or later](https://www.python.org)
 - The following Python library: os
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スピーチからテキストへのモデル要件の更新"
}
```

### Explanation
この変更は、「whisper-python.md」ファイル内で、必要な条件に関する記述が更新されたことを示しています。

1. **モデルの変更**: 以前は「Whisperモデル」が必要とされていましたが、現在は「スピーチからテキストモデル」が必要と明記されています。これにより、ユーザーは適切なモデルをより理解しやすくなります。

2. **文書の明確化**: スピーチからテキストへのモデルに関する記載は、リソースの配置場所についての情報も引き続き提示されており、利用者にとっての利便性が向上しています。「サポートされている地域」でのモデルデプロイに関する記述が保持され、どの地域で利用可能かを明確にしています。

3. **整合性の強化**: 新しい条件によって、文書が一貫性を持ち、Azure OpenAIサービスを利用する際の具体的な要件が明瞭になっています。これにより、開発者がPython環境での実装に向けて必要な情報を容易に取得できるようになります。

この変更は、Pythonを使用してスピーチをテキストに変換する機能を利用する際に、ユーザーが必要とする要件を明確に示しており、全体的な利用体験の向上に寄与します。

## articles/ai-services/openai/includes/whisper-rest.md{#item-639ccb}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ author: eric-urban
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
 
-- An Azure OpenAI resource deployed in a [supported region and with a supported model](../concepts/use-your-data.md#regional-availability-and-model-support).
+- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 - Be sure that you are assigned at least the [Cognitive Services Contributor](../how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スピーチからテキストへのモデル要件の更新"
}
```

### Explanation
この変更は、「whisper-rest.md」ファイルにおいて、Azure OpenAIリソースに関する条件が更新されたことを示しています。

1. **モデルの変更**: 以前の記載では「サポートされている地域かつサポートされているモデルがデプロイされたAzure OpenAIリソース」が必要とされていましたが、変更後は「スピーチからテキストモデルがデプロイされたAzure OpenAIリソース」が求められるようになりました。この明確化により、ユーザーは具体的にどのモデルを利用すべきかを理解しやすくなります。

2. **文書の明確化**: 新しい条件では、モデルがスピーチからテキストに特化していることが強調され、関連するリソースのリンクも提供されています。この情報により、ユーザーはモデルのデプロイと利用に関する詳細を簡単に参照できるようになります。

3. **整合性の向上**: この変更は、他のドキュメントとの一貫性を持たせるために重要であり、Azure OpenAIに関連する要件がより明確に整理されています。これにより、開発者が必要なリソースを確保する際の混乱を避ける手助けになります。

この変更は、REST APIを介してスピーチをテキストに変換する機能の利用を考えているユーザーに対して、必要な要件を明白にしており、全体的なユーザー体験の向上に寄与します。

## articles/ai-services/openai/includes/whisper-typescript.md{#item-eafedb}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ author: eric-urban
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
 - [TypeScript](https://www.typescriptlang.org/download/)
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
-- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 ### Microsoft Entra ID prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スピーチからテキストへのモデル要件の更新"
}
```

### Explanation
この変更は、「whisper-typescript.md」ファイル内でAzure OpenAIリソースに関する要件が更新されたことを示しています。

1. **モデル要件の明確化**: 以前は「サポートされている地域で作成されたAzure OpenAIリソース」が必要とされていましたが、現在は「スピーチからテキストモデルがデプロイされたAzure OpenAIリソース」が求められるようになりました。この変更により、ユーザーはどの特定のモデルが必要であるかをより明確に理解できます。

2. **参照リンクの更新**: 新しいモデルの要件を反映させるために、関連するリソースやドキュメントへのリンクも提供されています。これにより、ユーザーは必要な手続きを迅速に確認し、適切な設定を行うことが容易になります。

3. **一貫性の保持**: 他のドキュメントと同様に、Azure OpenAIに関連する情報が整合性を持たせて更新されているため、全体的なユーザー体験を向上させています。この整合性により、開発者は必要なリソースを効率的に準備することができます。

この変更は、TypeScript環境でスピーチからテキストに変換する機能の実装を目指しているユーザーに対して、必須のリソースを明示的に示すものであり、開発の簡略化に寄与します。

## articles/ai-services/openai/index.yml{#item-0adb87}

<details>
<summary>Diff</summary>
````diff
@@ -46,7 +46,7 @@ landingContent:
              url: dall-e-quickstart.md
            - text: Use your data (preview)
              url: use-your-data-quickstart.md
-           - text: Whisper
+           - text: Speech to text with Whisper
              url: whisper-quickstart.md
            - text: Text to speech (preview)
              url: text-to-speech-quickstart.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisperの名称変更"
}
```

### Explanation
この変更は、「index.yml」ファイル内でWhisperのセクション名が更新されたことを示しています。

1. **名称の明確化**: 以前は「Whisper」という名称が使用されていましたが、変更後は「Speech to text with Whisper」となりました。この変更により、ユーザーはWhisperがスピーチからテキストへの変換に特化した機能であることをより明確に理解できるようになります。

2. **ユーザーの理解促進**: この明確な表現は、初めてこのドキュメントに触れるユーザーにとって役立ちます。特に、AIサービスの機能に関心があるユーザーが、それぞれの機能の用途を素早く把握する助けになります。

3. **一貫性のある情報提供**: この変更は、関連する他のドキュメントやリソースと整合性を持たせることにも寄与しています。これにより、Azure OpenAIに関する情報がより統一的になり、ユーザーは必要な情報を探しやすくなります。

この変更は、ユーザーに対してWhisperの用途を明示し、全体的なユーザー体験の向上に貢献しています。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -7,20 +7,20 @@ author: mrbullwinkle
 ms.author: mbullwin
 ms.service: azure-ai-openai
 ms.topic: overview
-ms.date: 03/25/2025
+ms.date: 04/14/2025
 ms.custom: build-2023, build-2023-dataai
 recommendations: false
 ---
 
 # What is Azure OpenAI Service?
 
-Azure OpenAI Service provides REST API access to OpenAI's powerful language models including o3-mini, o1, o1-mini, GPT-4o, GPT-4o mini, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, image understanding, semantic search, and natural language to code translation. Users can access the service through REST APIs, [Python/C#/JS/Java/Go SDKs](/azure/ai-services/openai/supported-languages).
+Azure OpenAI Service provides REST API access to OpenAI's powerful language models including gpt-4.1, o3-mini, o1, o1-mini, GPT-4o, GPT-4o mini, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, image understanding, semantic search, and natural language to code translation. Users can access the service through REST APIs, [Python/C#/JS/Java/Go SDKs](/azure/ai-services/openai/supported-languages).
 
 ### Features overview
 
 | Feature | Azure OpenAI |
 | --- | --- |
-| Models available | [**computer-use-preview**](./concepts/models.md#computer-use-preview)<br>[**o3-mini & o1**](./how-to/reasoning.md) <br>[**o1-mini**](./how-to/reasoning.md)<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
+| Models available | [gpt-4.1](./concepts/models.md#gpt-41-series) <br> [**computer-use-preview**](./concepts/models.md#computer-use-preview)<br>[**o3-mini & o1**](./how-to/reasoning.md) <br>[**o1-mini**](./how-to/reasoning.md)<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
 | Fine-tuning | `GPT-4o-mini` (preview) <br> `GPT-4` (preview) <br>`GPT-3.5-Turbo` (0613).|
 | Price | [Available here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> For details on vision-enabled chat models, see the [special pricing information](../openai/concepts/gpt-with-vision.md#special-pricing-information).|
 | Virtual network support & private link support | Yes.  |
@@ -52,7 +52,7 @@ Start with the [Create and deploy an Azure OpenAI Service resource](./how-to/cre
 
 ## Comparing Azure OpenAI and OpenAI
 
-Azure OpenAI Service gives customers advanced language AI with OpenAI GPT-4, GPT-3, Codex, DALL-E, Whisper, and text to speech models with the security and enterprise promise of Azure. Azure OpenAI co-develops the APIs with OpenAI, ensuring compatibility and a smooth transition from one to the other.
+Azure OpenAI Service gives customers advanced language AI with OpenAI GPT-4, GPT-3, Codex, DALL-E, speech to text, and text to speech models with the security and enterprise promise of Azure. Azure OpenAI co-develops the APIs with OpenAI, ensuring compatibility and a smooth transition from one to the other.
 
 With Azure OpenAI, customers get the security capabilities of Microsoft Azure while running the same models as OpenAI. Azure OpenAI offers private networking, regional availability, and responsible AI content filtering.  
 
@@ -131,9 +131,7 @@ The service provides users access to several different models. Each model provid
 
 The DALL-E models (some in preview; see [models](./concepts/models.md#dall-e)) generate images from text prompts that the user provides.
 
-The Whisper models can be used to transcribe and translate speech to text.
-
-The text to speech models, currently in preview, can be used to synthesize text to speech.
+The audio API models can be used to transcribe and translate speech to text. The text to speech models, currently in preview, can be used to synthesize text to speech.
 
 Learn more about each model on our [models concept page](./concepts/models.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル名と機能に関する説明の更新"
}
```

### Explanation
この変更は、「overview.md」ファイルの内容がいくつかの点で更新されたことを示しています。

1. **モデル名の更新**: OpenAIの言語モデルのリストにおいて、「gpt-4.1」が新たに追加され、従来の「Whisper」の部分が「スピーチからテキスト」に変更されました。この変更により、最新のモデルのバージョンが反映されているとともに、その機能がより明確になり、ユーザーが利用可能なモデルを把握しやすくなっています。

2. **機能説明の改善**: 特に「Whisper」モデルに関する説明が「音声APIモデル」という一般的な用語に変更され、その機能が「スピーチからテキストを転写および翻訳する」ことに集中しています。この更新により、ユーザーは新しいモデルの特長をより簡潔に把握できるようになります。

3. **他の情報の整理**: 他のセクションでも情報が整理され、全体的な記述が一貫性を持つように更新されています。これにより、Azure OpenAIサービスの機能や特長が明確に伝わるようになっています。

4. **日付の更新**: ドキュメントの日付も「2025年3月25日」から「2025年4月14日」に更新され、新しい情報やモデルの追加に伴う変更が反映されていることを表しています。

これらの変更は、ドキュメントの正確性を向上させ、ユーザーが必要とする情報に迅速にアクセスできるようにするためのものです。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ The following sections provide you with a quick guide to the default quotas and
 | Azure OpenAI resources per region per Azure subscription | 30 |
 | Default DALL-E 2 quota limits | 2 concurrent requests |
 | Default DALL-E 3 quota limits| 2 capacity units (6 requests per minute)|
-| Default Whisper quota limits | 3 requests per minute |
+| Default speech to text audio API quota limits | 3 requests per minute |
 | Maximum prompt tokens per request | Varies per model. For more information, see [Azure OpenAI Service models](./concepts/models.md)|
 | Max Standard deployments per resource | 32 |
 | Max fine-tuned model deployments | 5 |
@@ -66,6 +66,8 @@ The following sections provide you with a quick guide to the default quotas and
 |---|---|:---:|:---:|
 | `gpt-4.1` (2025-04-14) | Enterprise Tier | 5 M | 5 K |
 | `gpt-4.1` (2025-04-14) | Default | 1 M | 1 K |
+| `gpt-4.1-nano` (2025-04-14) | Enterprise Tier | 5 M | 5 K |
+| `gpt-4.1-nano` (2025-04-14) | Default | 1 M | 1 K |
 
 
 ## computer-use-preview global standard
@@ -208,9 +210,9 @@ If your Azure subscription is linked to certain [offer types](https://azure.micr
 |Tier| Quota Limit in tokens per minute (TPM) |
 |---|:---|
 |`Azure for Students` | 1 K (all models) <br>Exception o-series & GPT-4.1 & GPT 4.5 Preview: 0|
-| `MSDN` | GPT-4o-mini: 200 K <br> GPT 3.5 Turbo Series: 200 K <br> GPT-4 series: 50 K <br>computer-use-preview: 8 K <br> gpt-4o-realtime-preview: 1 K <br> o-series: 0 <br> GPT 4.5 Preview: 0 <br> GPT-4.1: 0  |
-|`Pay-as-you-go` | GPT-4o-mini: 200 K <br> GPT 3.5 Turbo Series: 200 K <br> GPT-4 series: 50 K <br>computer-use-preview: 30 K <br> o-series: 0 <br> GPT 4.5 Preview: 0  <br> GPT-4.1: 0  |
-| `Azure_MS-AZR-0111P`  <br> `Azure_MS-AZR-0035P` <br> `Azure_MS-AZR-0025P` <br> `Azure_MS-AZR-0052P` <br>| GPT-4o-mini: 200 K <br> GPT 3.5 Turbo Series: 200 K <br> GPT-4 series: 50 K   |
+| `MSDN` | GPT-4o-mini: 200 K <br> GPT 3.5 Turbo Series: 200 K <br> GPT-4 series: 50 K <br>computer-use-preview: 8 K <br> gpt-4o-realtime-preview: 1 K <br> o-series: 0 <br> GPT 4.5 Preview: 0 <br> GPT-4.1: 50 K <br> GPT-4.1-nano: 200 K  |
+|`Pay-as-you-go` | GPT-4o-mini: 200 K <br> GPT 3.5 Turbo Series: 200 K <br> GPT-4 series: 50 K <br>computer-use-preview: 30 K <br> o-series: 0 <br> GPT 4.5 Preview: 0  <br> GPT-4.1: 50 K <br> GPT-4.1-nano: 200 K  |
+| `Azure_MS-AZR-0111P`  <br> `Azure_MS-AZR-0035P` <br> `Azure_MS-AZR-0025P` <br> `Azure_MS-AZR-0052P` <br>| GPT-4o-mini: 200 K <br> GPT 3.5 Turbo Series: 200 K <br> GPT-4 series: 50 K |
 | `CSP Integration Sandbox` <sup>*</sup> | All models: 0 |
 | `Lightweight trial`<br>`Free Trials`<br>`Azure Pass`  | All models: 0 |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータおよび制限の更新"
}
```

### Explanation
この変更は、「quotas-limits.md」ファイルの内容が一部更新されたことを示しています。この更新は、Azure OpenAIサービスにおけるさまざまなリソースの制限やクォータに関する情報を最新のものにすることを目的としています。

1. **クォータの名称変更**: 具体的には、「Default Whisper quota limits」が「Default speech to text audio API quota limits」に変更され、機能がより具体的に示されています。この変更により、ユーザーは音声からテキストへの変換機能に関する制限を理解しやすくなります。

2. **新しいモデルの追加**: 新たに「gpt-4.1-nano」というモデルが追加されており、Enterprise TierおよびDefaultのクォータが設定されています。これにより、利用可能なモデルの種類が増え、ユーザーはニーズに応じた選択肢を持つことができます。

3. **クォータ数値の見直し**: クォータの数値もいくつか更新されており、特定のモデルに対するリクエストの上限が見直されています。これにより、ユーザーがモデルの使用においてどのような制限があるのか、より正確な情報を得られるようになります。

4. **価格プランにおける調整**: 特にMSDNやPay-as-you-goプランのクォータに関する情報が更新され、これらのプランにおける制限が明確に示されています。この情報の更新は、ユーザーが自身のプランに基づいて利用できるリソースを正確に把握するために重要です。

以上の変更は、Azure OpenAIサービスの利用者にとって、最新のクォータや制限についての情報を提供し、サービスをより有効に活用できるようにすることを目的としています。

## articles/ai-services/openai/realtime-audio-quickstart.md{#item-727df8}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ The GPT 4o real-time models are available for global deployments.
 - `gpt-4o-mini-realtime-preview` (version `2024-12-17`)
 - `gpt-4o-realtime-preview` (version `2024-10-01`)
 
-See the [models and versions documentation](./concepts/models.md#gpt-4o-audio) for more information.
+See the [models and versions documentation](./concepts/models.md#audio-models) for more information.
 
 ## API support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル情報へのリンクの更新"
}
```

### Explanation
この変更は、「realtime-audio-quickstart.md」ファイルにおける情報のリンク先が更新されたことを示しています。

1. **ドキュメント内のリンク変更**: 元のリンク「./concepts/models.md#gpt-4o-audio」が新しいリンク「./concepts/models.md#audio-models」に変更されています。この変更は、より一般的な「オーディオモデル」に関連する情報を参照するためのものであり、リンク先の内容が最新の情報を反映することを目的としています。

2. **モデルバージョンに関する文脈の維持**: ナビゲーションを改良することにより、読者が必要とする情報をより容易に見つけられるようになっており、特に「GPT 4o」リアルタイムモデルの使用に関心があるユーザーにとって役立つ更新です。この文脈において、モデルやバージョンに関する詳細情報に簡単にアクセスできるようになります。

この変更は、ユーザーがリアルタイムオーディオモデルの詳細情報を迅速に取得できるようにするために重要です。

## articles/ai-services/openai/realtime-audio-reference.md{#item-276d51}

<details>
<summary>Diff</summary>
````diff
@@ -390,7 +390,7 @@ The server `conversation.item.input_audio_transcription.completed` event is the
 
 Transcription begins when the input audio buffer is committed by the client or server (in `server_vad` mode). Transcription runs asynchronously with response creation, so this event can come before or after the response events.
 
-Realtime API models accept audio natively, and thus input transcription is a separate process run on a separate speech recognition model, currently always `whisper-1`. Thus the transcript can diverge somewhat from the model's interpretation, and should be treated as a rough guide.
+Realtime API models accept audio natively, and thus input transcription is a separate process run on a separate speech recognition model such as `whisper-1`. Thus the transcript can diverge somewhat from the model's interpretation, and should be treated as a rough guide.
 
 #### Event structure
 
@@ -1067,12 +1067,14 @@ The server `session.updated` event is returned when a session is updated by the
 **Allowed Values:**
 
 * `whisper-1` 
+* `gpt-4o-transcribe`
+* `gpt-4o-mini-transcribe`
 
 ### RealtimeAudioInputTranscriptionSettings
 
 | Field | Type | Description | 
 |-------|------|-------------|
-| model | [RealtimeAudioInputTranscriptionModel](#realtimeaudioinputtranscriptionmodel) | The default `whisper-1` model is currently the only model supported for audio input transcription. | 
+| model | [RealtimeAudioInputTranscriptionModel](#realtimeaudioinputtranscriptionmodel) | The `whisper-1` model is currently the default model supported for audio input transcription. | 
 
 
 ### RealtimeClientEvent
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオ参照の情報更新"
}
```

### Explanation
この変更は、「realtime-audio-reference.md」ファイル内の情報が更新されたことを示しています。主なポイントは次の通りです。

1. **トランスクリプションモデルの明確化**: 「whisper-1」モデルについての記述が、「現在常に 'whisper-1'」という表現から「'whisper-1' のような別の音声認識モデルを使用する」という表現に置き換えられました。この変更により、今後のモデル追加に対する柔軟性が示されています。

2. **新しいトランスクリプションモデルの追加**: 使用可能なモデルに「gpt-4o-transcribe」と「gpt-4o-mini-transcribe」が新たに追加されました。これにより、ユーザーは複数の選択肢からモデルを選択できるようになり、特に異なるニーズに合わせたトランスクリプションが可能になります。

3. **デフォルトモデルの説明の調整**: 「RealtimeAudioInputTranscriptionSettings」のセクションにおいて、音声入力トランスクリプションに対応しているデフォルトモデルとして「whisper-1」が現在も推奨されることを明示しています。この更新は、ユーザーがモデルの選択肢を理解しやすくすることに寄与しています。

この変更は、リアルタイムオーディオAPIの使用において、トランスクリプションモデルに関する最新の情報を提供し、ユーザーが適切なモデルを選択する手助けをすることを目的としています。

## articles/ai-services/openai/supported-languages.md{#item-12c019}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom:
 ms.topic: conceptual
-ms.date: 03/27/2025
+ms.date: 04/14/2025
 ms.author: mbullwin
 zone_pivot_groups: openai-supported-languages
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サポートされている言語のドキュメントの日付更新"
}
```

### Explanation
この変更は、「supported-languages.md」ファイル内の日付が更新されたことを示しています。

1. **日付の更新**: 元の「ms.date: 03/27/2025」が新しい日付「ms.date: 04/14/2025」に変更されました。この変更は、ドキュメントの内容が最新の情報を反映していることを示すものであり、ユーザーが最新のサポート状況を正確に把握できるようにするためのものです。

このような日付の更新は、文書管理における透明性を高め、ユーザーにとって重要な情報の正確性を確保します。

## articles/ai-services/openai/text-to-speech-quickstart.md{#item-c344ad}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ zone_pivot_groups: programming-languages-rest-js-cs
 
 In this quickstart, you use the Azure OpenAI Service for text to speech with OpenAI voices.  
 
-The available voices are: `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer`. For more information, see [Azure OpenAI Service reference documentation for text to speech](./reference.md#text-to-speech).
+The available voices are: `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer`. For more information, see [Azure OpenAI Service reference documentation for text to speech](./reference.md#text-to-speech-preview).
 
 ::: zone pivot="rest-api"
 
@@ -52,5 +52,5 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 
 ## Next steps
 
-* Learn more about how to work with text to speech with Azure OpenAI Service in the [Azure OpenAI Service reference documentation](./reference.md#text-to-speech).
+* Learn more about how to work with text to speech with Azure OpenAI Service in the [Azure OpenAI Service reference documentation](./reference.md#text-to-speech-preview).
 * For more examples, check out the [Azure OpenAI Samples GitHub repository](https://github.com/Azure-Samples/openai)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "音声合成におけるドキュメントリンクの更新"
}
```

### Explanation
この変更は、「text-to-speech-quickstart.md」ファイル内のリンク情報が更新されたことを示しています。

1. **リンクの調整**: 音声合成で利用可能な音声の情報や、「Azure OpenAI Service reference documentation」でのテキスト音声変換に関するリンクが「text-to-speech」から「text-to-speech-preview」に変更されました。この更新により、ドキュメントが最新の情報を反映し、プレビュー版に特化した情報へアクセスできることが示しています。

2. **ドキュメントの精度向上**: リンク先が正確であることで、ユーザーは最新の機能や情報にアクセスしやすくなります。また、プレビュー版に関する具体的な情報提供は、試行中の機能について理解を深める助けになります。

この変更は、ユーザーに対してより良い体験を提供し、正しいリソースへのアクセスを促す意図があります。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -42,7 +42,7 @@ items:
       href: use-your-data-quickstart.md
     - name: Realtime API for speech and audio (preview)
       href: realtime-audio-quickstart.md
-    - name: Whisper model
+    - name: Speech to text with Whisper
       href: whisper-quickstart.md
     - name: Text to speech (preview)
       href: text-to-speech-quickstart.md
@@ -54,6 +54,8 @@ items:
       href: ./concepts/assistants.md
     - name: Abuse monitoring
       href: ./concepts/abuse-monitoring.md
+    - name: Audio
+      href: ./concepts/audio.md
     - name: Content filtering
       href: ./concepts/content-filter.md
     - name: Default safety policies
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新と新しいセクションの追加"
}
```

### Explanation
この変更は、「toc.yml」ファイルにおける目次の内容が更新されたことを示しています。

1. **項目名の変更**: 「Whisper model」という項目が「Speech to text with Whisper」に変更され、より具体的な説明が提供されています。これにより、ユーザーはこの機能が何であるかをより明確に理解できるようになります。

2. **新しい項目の追加**: 新たに「Audio」という項目が目次に追加され、関連するリソースへのリンクが提供されています。この追加により、ユーザーが音声に関するコンテンツを探しやすくなります。

3. **既存項目の保持**: 他の項目はそのままとなっており、目次の整合性が保たれています。このような更新は、ユーザーが必要な情報に迅速にアクセスできるようにするために重要です。

これらの変更は、ドキュメントのナビゲーションを向上させ、ユーザーエクスペリエンスを改善することを目的としています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -23,7 +23,17 @@ This article provides a summary of the latest releases and major documentation u
 
 ### GPT-4.1 released
 
-The latest model from Azure OpenAI with a 1 million token context limit. For more information, see the [models page](./concepts/models.md#gpt-41-series).
+GPT 4.1 and GPT 4.1-nano are now available. These are the latest models from Azure OpenAI. GPT 4.1 has a 1 million token context limit. For more information, see the [models page](./concepts/models.md#gpt-41-series).
+
+### gpt-4o audio models released
+
+New audio models powered by GPT-4o are now available.  
+
+- The `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` speech to text models are released. Use these models via the `/audio` and `/realtime` APIs.  
+
+- The `gpt-4o-mini-tts` text to speech model is released. Use the `gpt-4o-mini-tts` model for text to speech generation via the `/audio` API.
+
+For more information about available models, see the [models and versions documentation](./concepts/models.md#audio-models).
 
 ## March 2025
 
@@ -73,7 +83,7 @@ The `gpt-4o-mini-audio-preview` (2024-12-17) model is the latest audio completio
 
 The `gpt-4o-mini-realtime-preview` (2024-12-17) model is the latest real-time audio model. The real-time models use the same underlying GPT-4o audio model as the completions API, but is optimized for low-latency, real-time audio interactions. For more information, see the [real-time audio quickstart](./realtime-audio-quickstart.md).
 
-For more information about available models, see the [models and versions documentation](./concepts/models.md#gpt-4o-audio).
+For more information about available models, see the [models and versions documentation](./concepts/models.md#audio-models).
 
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
この変更は、「whats-new.md」ファイルにおける新機能およびモデル情報が更新されたことを示しています。

1. **新モデルのリリース情報**: GPT-4.1およびその派生モデルであるGPT-4.1-nanoがリリースされたことが記載されています。これにより、ユーザーは最新のモデルの利用状況を把握しやすくなっています。

2. **音声モデルの追加**: 新たに「gpt-4o」音声モデルに関する情報が追加され、具体的には`gpt-4o-transcribe`および`gpt-4o-mini-transcribe`のスピーチ-to-テキストモデル、さらに`gpt-4o-mini-tts`のテキスト-to-スピーチモデルがリリースされたことが紹介されています。これにより、ユーザーは新しい音声機能を活用する方法を理解できます。

3. **情報リンクの更新**: モデル情報の文献へのリンクも更新され、音声モデルに関連する最新の情報にアクセスできるようになっています。

これらの追加と更新により、ユーザーは新たな機能や利用可能なモデルについての理解を深め、より効果的にAzure OpenAIサービスを活用できるようになります。

## articles/ai-services/openai/whisper-quickstart.md{#item-4cae3d}

<details>
<summary>Diff</summary>
````diff
@@ -18,6 +18,9 @@ zone_pivot_groups: programming-languages-rest-ps-py-js-cs
 
 This quickstart explains how to use the [Azure OpenAI Whisper model](../speech-service/whisper-overview.md) for speech to text conversion. The Whisper model can transcribe human speech in numerous languages, and it can also translate other languages into English.
 
+> [!NOTE]
+> For information about other audio models that you can use with Azure OpenAI, see [Audio models](./concepts/models.md?tabs=standard-audio#standard-models-by-endpoint).
+
 The file size limit for the Whisper model is 25 MB. If you need to transcribe a file larger than 25 MB, you can use the Azure AI Speech [batch transcription](../speech-service/batch-transcription-create.md#use-a-whisper-model) API.
 
 ::: zone pivot="rest-api"
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
この変更は、「whisper-quickstart.md」ファイルにおいて、Whisperモデルに関する情報が更新されたことを示しています。

1. **追加ノートの挿入**: 新たに注釈が追加され、Azure OpenAIで使用できるその他の音声モデルについての情報が提供されています。ユーザーは「Audio models」というリンクを通じて、さまざまな音声モデルの詳細を簡単に見つけることができます。

2. **Whisperモデルの説明**: このクイックスタートは、Whisperモデルを使用した音声からテキストへの変換方法を説明しており、Whisperモデルが人間の音声を多くの言語で音声認識し、他の言語を英語に翻訳することができることが再確認されています。

3. **ファイルサイズ制限の再確認**: Whisperモデルのファイルサイズ制限が25 MBであることが再確認され、25 MBを超えるファイルを処理するためのバッチトランスクリプションAPIの使用についても言及されています。

これらの更新は、ユーザーがWhisperモデルを効果的に使用するために必要な情報を提供し、音声処理機能の理解を深めることを目的としています。


