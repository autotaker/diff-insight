---
date: '2025-04-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dad2f57...MicrosoftDocs:d942a6a
summary: 今回のコード変更では、Azure OpenAIに関するドキュメントが多数更新され、オーディオコンプリーションのクイックスタートガイドにトラブルシューティングセクションが追加されました。主な変更点にはリンクの修正や文法の改善が含まれ、ユーザーが適切な情報に容易にアクセスできるように改良されています。特に、不具合や破壊的変更はなく、全体的なユーザーフレンドリーな体験の向上が図られています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dad2f57...MicrosoftDocs:d942a6a){target="_blank"}

# ハイライト

今回のコード変更では、Azure OpenAIに関する多数のドキュメント更新と修正が行われました。主要な新機能としては、オーディオコンプリーションのクイックスタートガイドにトラブルシューティングセクションが追加され、具体的な使用条件が追記されました。大部分の変更はリンクの修正や文法の改善であり、ユーザーが適切な情報にアクセスしやすくするための改良が行われています。

## 新機能
- オーディオコンプリートガイドにトラブルシューティングセクションを追加し、`gpt-4o-audio-preview`の具体的な注意点を明示。

## 破壊的変更
- 特に無し。

## その他のアップデート
- 多数の技術ドキュメントでリンクの方向を修正（例：`standard-models-by-endpoint`から`standard-deployment-regional-models-by-endpoint`へ）。
- 文法やリンクの修正で、ナビゲーションと情報アクセスの向上。
- モデルのリタイア情報や利用可能地域のテーブル更新。
- 一部のコード例においてバッチ処理のコメントの改善。

# インサイト

最近の変更を通じて、Azure OpenAIのドキュメントにおけるユーザーフレンドリーな経験の向上が強化されています。この修正は、小さな文法的エラーやリンクの不整合を解決するだけでなく、ユーザーが最新かつ地域に依存しない情報へのアクセスをスムーズに行えるようにしています。

特に注目すべき変更は、オーディオコンプリーションガイドに追加されたトラブルシューティングセクションです。これにより、ユーザーは特殊な設定条件、例えば`stream`が`true`の場合にサポートされるオーディオフォーマットについて明確な理解を持つことができ、AzureのAIサービスを最大限利用するためのガイドラインが提供されます。

リンクの修正によって、異なる地域のユーザーがそれぞれの地域で使用可能なモデルに関する明確な情報にアクセスしやすくなっています。このことは、Azureのサービス提供のグローバル展開と、その地域特有のニーズに応える柔軟性を示唆しています。

また、モデルのリタイア情報やプロンプトエンジニアリングに関する文書の改善は、開発者自身が迅速かつ効果的にサービスをアップグレードできるようにするための重要なステップです。

これら一連の改善は、エンタープライズでのAIサービスの迅速な展開と効果的な利用を支援するためのもので、ユーザーエクスペリエンスと情報の精度向上に寄与します。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [audio-completions-quickstart.md](#item-be5860) | minor update | オーディオコンプリートのクイックスタートにトラブルシューティングのセクションを追加 | modified | 5 | 1 | 6 | 
| [audio.md](#item-624e70) | minor update | オーディオモデルに関する文書リンクを更新 | modified | 1 | 1 | 2 | 
| [content-filter.md](#item-dfc7e7) | minor update | コンテンツフィルタリングの注意事項におけるリンクを更新 | modified | 1 | 1 | 2 | 
| [model-retirements.md](#item-03fc2e) | minor update | モデルのリタイア情報を更新 | modified | 11 | 6 | 17 | 
| [models.md](#item-db2c37) | minor update | モデル情報のリンクと見出しを修正 | modified | 2 | 2 | 4 | 
| [prompt-engineering.md](#item-884584) | bug fix | 文法エラーの修正 | modified | 1 | 1 | 2 | 
| [provisioned-migration.md](#item-68e143) | minor update | 文章内の誤字の修正 | modified | 1 | 1 | 2 | 
| [latest-inference-preview.md](#item-24bf0f) | minor update | ドキュメントリンクの修正 | modified | 9 | 9 | 18 | 
| [batch-python.md](#item-3121c2) | minor update | バッチ処理の設定に関するコメントの修正 | modified | 8 | 7 | 15 | 
| [batch-rest.md](#item-bcccd9) | minor update | バッチ処理の有効期限設定についての説明を修正 | modified | 2 | 2 | 4 | 
| [standard-audio.md](#item-1d8db7) | minor update | 音声モデルの対応地域テーブルの更新 | modified | 12 | 11 | 23 | 
| [standard-global.md](#item-17a84b) | minor update | グローバルモデルの対応地域テーブルを更新 | modified | 27 | 27 | 54 | 
| [text-to-speech-dotnet.md](#item-fea66a) | minor update | 記事内のリンクの修正 | modified | 1 | 1 | 2 | 
| [whisper-dotnet.md](#item-562a58) | minor update | 記事内のリンクの修正 | modified | 1 | 1 | 2 | 
| [whisper-javascript.md](#item-3ee990) | minor update | 記事内のリンクの修正 | modified | 1 | 1 | 2 | 
| [whisper-powershell.md](#item-7db269) | minor update | 記事内のリンクの修正 | modified | 1 | 1 | 2 | 
| [whisper-python.md](#item-e61179) | minor update | 記事内のリンクの修正 | modified | 1 | 1 | 2 | 
| [whisper-rest.md](#item-639ccb) | minor update | 記事内のリンクの修正 | modified | 1 | 1 | 2 | 
| [whisper-typescript.md](#item-eafedb) | minor update | 記事内のリンクの修正 | modified | 1 | 1 | 2 | 
| [whisper-quickstart.md](#item-4cae3d) | minor update | 音声モデルリンクの修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/audio-completions-quickstart.md{#item-be5860}

<details>
<summary>Diff</summary>
````diff
@@ -45,14 +45,18 @@ recommendations: false
 
 ::: zone-end
 
-
 ## Clean-up resources
 
 If you want to clean up and remove an Azure OpenAI resource, you can delete the resource. Before deleting the resource, you must first delete any deployed models.
 
 - [Azure portal](../multi-service-resource.md?pivots=azportal#clean-up-resources)
 - [Azure CLI](../multi-service-resource.md?pivots=azcli#clean-up-resources)
 
+## Troubleshooting
+
+> [!NOTE]
+> When using `gpt-4o-audio-preview` for chat completions with the audio modality and `stream` is set to true the only supported audio format is pcm16.
+
 ## Related content
 
 * Learn more about Azure OpenAI [deployment types](./how-to/deployment-types.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オーディオコンプリートのクイックスタートにトラブルシューティングのセクションを追加"
}
```

### Explanation
この変更では、オーディオコンプリートのクイックスタートガイドに「トラブルシューティング」という新しいセクションが追加されました。このセクションでは、`gpt-4o-audio-preview`を使用する際のチャットコンプリートの具体的な注意事項として、`stream`がtrueに設定された場合にサポートされるオーディオフォーマットがpcm16であることが記載されています。これにより、ユーザーは特定の条件下での使用方法に関する重要な情報を得ることができ、より効果的にAzure OpenAIサービスを利用できるようになります。また、不要なリソースをクリーンアップする方法に関する情報はそのまま残されています。変更に伴う追加行は5行、削除行は1行で、合計で6行の修正が行われています。

## articles/ai-services/openai/concepts/audio.md{#item-624e70}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ manager: nitinme
 
 Audio models in Azure OpenAI are available via the `realtime`, `completions`, and `audio` APIs. The audio models are designed to handle a variety of tasks, including speech recognition, translation, and text to speech.
 
-For information about the available audio models per region in Azure OpenAI Service, see the [audio models](models.md?tabs=standard-audio#standard-models-by-endpoint), [standard models by endpoint](models.md?tabs=standard-audio#standard-models-by-endpoint), and [global standard model availability](models.md?tabs=standard-audio#global-standard-model-availability) documentation.
+For information about the available audio models per region in Azure OpenAI Service, see the [audio models](models.md?tabs=standard-audio#standard-deployment-regional-models-by-endpoint), [standard models by endpoint](models.md?tabs=standard-audio#standard-deployment-regional-models-by-endpoint), and [global standard model availability](models.md?tabs=standard-audio#global-standard-model-availability) documentation.
 
 ### GPT-4o audio Realtime API
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オーディオモデルに関する文書リンクを更新"
}
```

### Explanation
この変更では、Azure OpenAI Serviceのオーディオモデルに関する説明文の一部が修正されました。具体的には、地域ごとの利用可能なオーディオモデルについての情報を参照するリンクが更新されています。従来のリンクから、`standard-audio#standard-models-by-endpoint`から`standard-deployment-regional-models-by-endpoint`に変更され、より明確に各地域のデプロイメントに対応したモデルへと導く情報が提供されるようになりました。この更新により、ユーザーはより適切なドキュメントにアクセスしやすくなります。行数としては、追加と削除がそれぞれ1行ずつの計2行の変更となっています。

## articles/ai-services/openai/concepts/content-filter.md{#item-dfc7e7}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ manager: nitinme
 # Content filtering
 
 > [!IMPORTANT]
-> The content filtering system isn't applied to prompts and completions processed by the audio models such as Whisper in Azure OpenAI Service. Learn more about the [Audio models in Azure OpenAI](models.md?tabs=standard-audio#standard-models-by-endpoint).
+> The content filtering system isn't applied to prompts and completions processed by the audio models such as Whisper in Azure OpenAI Service. Learn more about the [Audio models in Azure OpenAI](models.md?tabs=standard-audio#standard-deployment-regional-models-by-endpoint).
 
 Azure OpenAI Service includes a content filtering system that works alongside core models, including DALL-E image generation models. This system works by running both the prompt and completion through an ensemble of classification models designed to detect and prevent the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions. Variations in API configurations and application design might affect completions and thus filtering behavior.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングの注意事項におけるリンクを更新"
}
```

### Explanation
この変更では、Azure OpenAIサービスにおけるコンテンツフィルタリングについての注意事項が更新されました。具体的には、音声モデル（Whisperなど）によって処理されるプロンプトやコンプリーションにはコンテンツフィルタリングシステムが適用されない旨が記載されています。この注意事項の文中にあるリンクが、以前の`standard-models-by-endpoint`から`standard-deployment-regional-models-by-endpoint`に修正され、最新の情報を反映した形になっています。これにより、ユーザーは適切なドキュメントにアクセスしやすくなり、コンテンツフィルタリングの理解が進むことが期待されます。変更は、追加と削除がそれぞれ1行ずつの計2行の内容です。

## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 04/14/2025
+ms.date: 04/17/2025
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -105,6 +105,8 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-4` | vision-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025  **<sup>1</sup>** <br>Retirement date: May 1, 2025 | `gpt-4o`|
 | `gpt-4.5-preview` | 2025-02-27 | No earlier than July 02, 2025 | `gpt-4.1` |
 | `gpt-4.1` | 2025-04-14 | No earlier than April 11, 2026 | |
+| `gpt-4.1-mini` | 2025-04-14 | No earlier than April 11, 2026 |
+| `gpt-4.1-nano` | 2025-04-14 | No earlier than April 11, 2026 |
 | `gpt-4o` | 2024-05-13 | No earlier than June 30, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on March 17, 2025. | |
 | `gpt-4o` | 2024-08-06 | No earlier than August 6, 2025  | |
 | `gpt-4o` | 2024-11-20 | No earlier than November 20, 2025  | |
@@ -113,11 +115,14 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-3.5-turbo-instruct` | 0914 | No earlier than May 31, 2025 |  |
 | `o1-preview` | 2024-09-12 | No earlier than April 2, 2025 | `o1` |
 | `o1` | 2024-12-17 | No earlier than December 17, 2025 | |
+| `o4-mini` | 2025-04-16 | No earlier than April 11, 2026 | |
+| `o3` | 2025-04-16 | No earlier than April 11, 2026 | |
 | `o3-mini` | 2025-01-31 | No earlier than February 1, 2026 | |
-| `text-embedding-ada-002` | 2 | No earlier than October 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
-| `text-embedding-ada-002` | 1 | No earlier than October 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
-| `text-embedding-3-small` | | No earlier than January 25, 2026 | |
-| `text-embedding-3-large` | | No earlier than January 25, 2026 | |
+| `text-embedding-ada-002` | 2 | No earlier than April 30, 2026 | `text-embedding-3-small` or `text-embedding-3-large` |
+| `text-embedding-ada-002` | 1 | No earlier than April 30, 2026 | `text-embedding-3-small` or `text-embedding-3-large` |
+| `text-embedding-3-small` | | No earlier than April 30, 2026 | |
+| `text-embedding-3-large` | | No earlier than April 30, 2026 | |
+
 
  **<sup>1</sup>** We'll notify all customers with these preview deployments at least 30 days before the start of the upgrades. We'll publish an upgrade schedule detailing the order of regions and model versions that we'll follow during the upgrades, and link to that schedule from here.
 
@@ -181,7 +186,7 @@ If you're an existing customer looking for information about these models, see [
 
 ## April 15, 2025
 
-To track further updates to this article refer to the [Git History](https://github.com/MicrosoftDocs/azure-ai-docs/commits/main/articles/ai-services/openai/concepts/model-retirements.md)
+To track further individual updates to this article refer to the [Git History](https://github.com/MicrosoftDocs/azure-ai-docs/commits/main/articles/ai-services/openai/concepts/model-retirements.md)
 
 ## March 18, 2025
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのリタイア情報を更新"
}
```

### Explanation
この変更では、Azure OpenAIにおけるモデルのリタイアに関する情報が更新されています。主な見直しとして、モデルのリタイア日やアップグレード日が修正され、新たに`gpt-4.1-mini`と`gpt-4.1-nano`がリストに追加されています。これにより、利用可能なモデルやその将来的なリタイア日についての情報がより正確に表示されるようになりました。また、指定された日付が変更され、特に`ms.date`フィールドの日付が04/14/2025から04/17/2025に更新されました。結果的に、変更の行数は追加が11行、削除が6行、合計で17行の変更が含まれています。この更新によって、利用者は最新のモデル情報に基づいて適切な意思決定を行えるようになります。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -273,7 +273,7 @@ The audio models via the `/audio` API can be used for speech to text, translatio
 | `tts-hd` | Text to speech optimized for quality.|
 | `gpt-4o-mini-tts` | Text to speech model powered by GPT-4o mini.<br/><br/>You can guide the voice to speak in a style or tone. |
 
-For more information see [Audio models region availability](?tabs=standard-audio#standard-models-by-endpoint) in this article.
+For more information see [Audio models region availability](?tabs=standard-audio#standard-deployment-regional-models-by-endpoint) in this article.
 
 ## Model summary table and region availability
 
@@ -359,7 +359,7 @@ For more information on Provisioned deployments, see our [Provisioned guidance](
 
 This table doesn't include fine-tuning regional availability information.  Consult the [fine-tuning section](#fine-tuning-models) for this information.
 
-### Standard models by endpoint
+### Standard deployment (regional) models by endpoint
 
 # [Chat Completions](#tab/standard-chat-completions)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル情報のリンクと見出しを修正"
}
```

### Explanation
この変更では、Azure OpenAIに関するモデル情報において、いくつかの文言やリンクが修正されました。具体的には、音声モデルの地域ごとの利用可能性に関するリンクが更新され、古いリンクから新しいリンクへと変更されています。具体的には、「`standard-models-by-endpoint`」から「`standard-deployment-regional-models-by-endpoint`」に変更されました。

また、見出しとして「標準モデルのエンドポイント」が「標準展開（地域）モデルのエンドポイント」に修正され、内容がより具体的になっています。これらの変更によって、利用者が必要な情報にアクセスしやすくなり、文書の一貫性が向上しています。変更の内容は、追加が2行、削除が2行で、計4行の改訂が含まれています。

## articles/ai-services/openai/concepts/prompt-engineering.md{#item-884584}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ recommendations: false
 
 # Prompt engineering techniques
 
-GPT-3, GPT-3.5, GPT-4, and GPT-4o models from OpenAI are prompt-based. With prompt-based models, the user interacts with the model by entering a text prompt, to which the model responds with a text completion. This completion is the model’s continuation of the input text. These techniques are note recommended for o-series models.
+GPT-3, GPT-3.5, GPT-4, and GPT-4o models from OpenAI are prompt-based. With prompt-based models, the user interacts with the model by entering a text prompt, to which the model responds with a text completion. This completion is the model’s continuation of the input text. These techniques are not recommended for o-series models.
 
 While these models are extremely powerful, their behavior is also very sensitive to the prompt. This makes prompt construction an important skill to develop.
 
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "文法エラーの修正"
}
```

### Explanation
この変更では、OpenAIのPromptエンジニアリングに関する文書において、文法的なエラーが修正されました。具体的には、「note recommended for o-series models」という誤った表現が、「not recommended for o-series models」に修正され、正しい文法に改善されています。

この修正により、文書の内容が明確さを増し、ユーザーに対する正確な情報提供が行われるようになりました。変更内容は、追加が1行、削除が1行で、合計2行の変更が含まれています。このような改善は、利用者が理解しやすい文書に近づけるために重要です。

## articles/ai-services/openai/concepts/provisioned-migration.md{#item-68e143}

<details>
<summary>Diff</summary>
````diff
@@ -251,7 +251,7 @@ Customers must reach out to their account teams to schedule a managed migration.
 
 **Managed migration advantages:**
 
-- Bulk migration of all commitments in an subscription/region is beneficial for customers with many commitments.
+- Bulk migration of all commitments in a subscription/region is beneficial for customers with many commitments.
 - Seamless cost migration: No possibility of double-billing or extra hourly charges.
 
 **Managed migration disadvantages:**
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文章内の誤字の修正"
}
```

### Explanation
この変更は、OpenAIのプロビジョニング移行に関する文書内の誤字を修正するものです。具体的には、元の文「in an subscription/region」が「in a subscription/region」に修正されています。この修正により、文の文法が正しくなり、読みやすさと明確さが向上しました。

変更の内容は、追加が1行、削除が1行で、合計2行の改訂が行われています。このような小さな修正でも、文書全体の品質と理解を向上させるためには重要です。

## articles/ai-services/openai/includes/api-versions/latest-inference-preview.md{#item-24bf0f}

<details>
<summary>Diff</summary>
````diff
@@ -280,7 +280,7 @@ Creates a completion for the chat message
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
 | audio | object | Parameters for audio output. Required when audio output is requested with<br>`modalities: ["audio"]`. <br> | No |  |
-| └─ format | enum | Specifies the output audio format. Must be one of `wav`, `mp3`, `flac`,<br>`opus`, or `pcm16`. <br><br>Possible values: `wav`, `mp3`, `flac`, `opus`, `pcm16` | No |  |
+| └─ format | enum | Specifies the output audio format. Must be one of `wav`, `mp3`, `flac`,<br>`opus`, or `pcm16`. <br><br>Possible values: `wav`, `mp3`, `flac`, `opus`, `pcm16`<br> When using `gpt-4o-audio-preview` and `stream` is set to true the only supported audio format is `pcm16`. | No |  |
 | └─ voice | enum | Specifies the voice type. Supported voices are `alloy`, `echo`, <br>`fable`, `onyx`, `nova`, and `shimmer`.<br><br>Possible values: `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer` | No |  |
 | data_sources | array |   The configuration entries for Azure OpenAI chat extensions that use them.<br>  This additional specification is only compatible with Azure OpenAI. | No |  |
 | frequency_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.<br> | No | 0 |
@@ -298,7 +298,7 @@ Creates a completion for the chat message
 | prediction | [PredictionContent](#predictioncontent) | Configuration for a Predicted Output, which can greatly improve response times when large parts of the model response are known ahead of time. This is most common when you are regenerating a file with only minor changes to most of the content. | No |  |
 | presence_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.<br> | No | 0 |
 | reasoning_effort | enum | **o1 models only** <br><br> Constrains effort on reasoning for <br>reasoning models.<br><br>Currently supported values are `low`, `medium`, and `high`. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response.<br>Possible values: `low`, `medium`, `high` | No |  |
-| response_format | [ResponseFormatText](#responseformattext) or [ResponseFormatJsonObject](#responseformatjsonobject) or [ResponseFormatJsonSchema](#responseformatjsonschema) | An object specifying the format that the model must output. Compatible with [GPT-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models), [GPT-4o mini](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models), [GPT-4 Turbo](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models) and all [GPT-3.5](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-35) Turbo models newer than `gpt-3.5-turbo-1106`.<br><br>Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which guarantees the model will match your supplied JSON schema.<br><br>Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.<br><br>**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.<br> | No |  |
+| response_format | [ResponseFormatText](#responseformattext) or [ResponseFormatJsonObject](#responseformatjsonobject) or [ResponseFormatJsonSchema](#responseformatjsonschema) | An object specifying the format that the model must output. Compatible with [GPT-4o](../../../../ai-services/openai/concepts/models.md#gpt-4-and-gpt-4-turbo-models), [GPT-4o mini](../../../../ai-services/openai/concepts/models.md#gpt-4-and-gpt-4-turbo-models), [GPT-4 Turbo](../../../../ai-services/openai/concepts/models.md#gpt-4-and-gpt-4-turbo-models) and all [GPT-3.5](../../../../ai-services/openai/concepts/models.md#gpt-35) Turbo models newer than `gpt-3.5-turbo-1106`.<br><br>Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which guarantees the model will match your supplied JSON schema.<br><br>Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.<br><br>**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.<br> | No |  |
 | seed | integer | This feature is in Beta.<br>If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.<br>Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.<br> | No |  |
 | stop | string or array | Up to 4 sequences where the API will stop generating further tokens.<br> | No |  |
 | store | boolean | Whether or not to store the output of this chat completion request for use in our model distillation or evaluation products. | No |  |
@@ -4938,7 +4938,7 @@ Represents a completion response from the API. Note: both the streamed and non-s
 | prediction | [PredictionContent](#predictioncontent) | Configuration for a Predicted Output, which can greatly improve response times when large parts of the model response are known ahead of time. This is most common when you are regenerating a file with only minor changes to most of the content. | No |  |
 | presence_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.<br> | No | 0 |
 | reasoning_effort | enum | **o1 models only** <br><br> Constrains effort on reasoning for <br>reasoning models.<br><br>Currently supported values are `low`, `medium`, and `high`. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response.<br>Possible values: `low`, `medium`, `high` | No |  |
-| response_format | [ResponseFormatText](#responseformattext) or [ResponseFormatJsonObject](#responseformatjsonobject) or [ResponseFormatJsonSchema](#responseformatjsonschema) | An object specifying the format that the model must output. Compatible with [GPT-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models), [GPT-4o mini](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models), [GPT-4 Turbo](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models) and all [GPT-3.5](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-35) Turbo models newer than `gpt-3.5-turbo-1106`.<br><br>Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which guarantees the model will match your supplied JSON schema.<br><br>Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.<br><br>**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.<br> | No |  |
+| response_format | [ResponseFormatText](#responseformattext) or [ResponseFormatJsonObject](#responseformatjsonobject) or [ResponseFormatJsonSchema](#responseformatjsonschema) | An object specifying the format that the model must output. Compatible with [GPT-4o](../../../../ai-services/openai/concepts/models.md#gpt-4-and-gpt-4-turbo-models), [GPT-4o mini](../../../../ai-services/openai/concepts/models.md#gpt-4-and-gpt-4-turbo-models), [GPT-4 Turbo](../../../../ai-services/openai/concepts/models.md#gpt-4-and-gpt-4-turbo-models) and all [GPT-3.5](../../../../ai-services/openai/concepts/models.md#gpt-35) Turbo models newer than `gpt-3.5-turbo-1106`.<br><br>Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which guarantees the model will match your supplied JSON schema.<br><br>Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.<br><br>**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.<br> | No |  |
 | seed | integer | This feature is in Beta.<br>If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.<br>Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.<br> | No |  |
 | stop | string or array | Up to 4 sequences where the API will stop generating further tokens.<br> | No |  |
 | store | boolean | Whether or not to store the output of this chat completion request for use in our model distillation or evaluation products. | No |  |
@@ -4969,7 +4969,7 @@ User security context contains several parameters that describe the AI applicati
 |------|------|-------------|----------|---------|
 | description | string | A description of what the function does, used by the model to choose when and how to call the function. | No |  |
 | name | string | The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. | Yes |  |
-| parameters | [FunctionParameters](#functionparameters) | The parameters the functions accepts, described as a JSON Schema object. See the guide](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. <br><br>Omitting `parameters` defines a function with an empty parameter list. | No |  |
+| parameters | [FunctionParameters](#functionparameters) | The parameters the functions accepts, described as a JSON Schema object. See [the guide](../../../../ai-services/openai/how-to/function-calling.md) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. <br><br>Omitting `parameters` defines a function with an empty parameter list. | No |  |
 
 ### chatCompletionFunctionCallOption
 
@@ -4982,7 +4982,7 @@ Specifying a particular function via `{"name": "my_function"}` forces the model
 
 ### chatCompletionFunctionParameters
 
-The parameters the functions accepts, described as a JSON Schema object. See the [guide/](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.
+The parameters the functions accepts, described as a JSON Schema object. See the [guide](../../../../ai-services/openai/how-to/function-calling.md) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.
 
 No properties defined for this component.
 
@@ -5108,7 +5108,7 @@ This component can be one of the following:
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
 | image_url | object |  | Yes |  |
-| └─ detail | enum | Specifies the detail level of the image. Learn more in the [Vision guide](https://learn.microsoft.com/azure/ai-services/openai/how-to/gpt-with-vision?tabs=rest%2Csystem-assigned%2Cresource#detail-parameter-settings-in-image-processing-low-high-auto).<br>Possible values: `auto`, `low`, `high` | No |  |
+| └─ detail | enum | Specifies the detail level of the image. Learn more in the [Vision guide](../../../../ai-services/openai/how-to/gpt-with-vision.md?tabs=rest%2Csystem-assigned%2Cresource#detail-parameter-settings).<br>Possible values: `auto`, `low`, `high` | No |  |
 | └─ url | string | Either a URL of the image or the base64 encoded image data. | No |  |
 | type | enum | The type of the content part.<br>Possible values: `image_url` | Yes |  |
 
@@ -5866,7 +5866,7 @@ Usage statistics for the completion request.
 
 ### FunctionParameters
 
-The parameters the functions accepts, described as a JSON Schema object. See the guide](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. 
+The parameters the functions accepts, described as a JSON Schema object. See the [guide](../../../../ai-services/openai/how-to/function-calling.md) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. 
 
 Omitting `parameters` defines a function with an empty parameter list.
 
@@ -5879,7 +5879,7 @@ No properties defined for this component.
 |------|------|-------------|----------|---------|
 | description | string | A description of what the function does, used by the model to choose when and how to call the function. | No |  |
 | name | string | The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. | Yes |  |
-| parameters | [FunctionParameters](#functionparameters) | The parameters the functions accepts, described as a JSON Schema object. See the guide](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. <br><br>Omitting `parameters` defines a function with an empty parameter list. | No |  |
+| parameters | [FunctionParameters](#functionparameters) | The parameters the functions accepts, described as a JSON Schema object. See the [guide](../../../../ai-services/openai/how-to/function-calling.md) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. <br><br>Omitting `parameters` defines a function with an empty parameter list. | No |  |
 | strict | boolean | Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. | No | False |
 
 ### ResponseFormatText
@@ -6309,7 +6309,7 @@ Represents an `assistant` that can call the model and use tools.
 | function | object | The function definition. | Yes |  |
 | └─ description | string | A description of what the function does, used by the model to choose when and how to call the function. | No |  |
 | └─ name | string | The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. | No |  |
-| └─ parameters | [chatCompletionFunctionParameters](#chatcompletionfunctionparameters) | The parameters the functions accepts, described as a JSON Schema object. See the [guide/](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. | No |  |
+| └─ parameters | [chatCompletionFunctionParameters](#chatcompletionfunctionparameters) | The parameters the functions accepts, described as a JSON Schema object. See the [guide](../../../../ai-services/openai/how-to/function-calling.md) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. | No |  |
 | type | string | The type of tool being defined: `function` | Yes |  |
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントリンクの修正"
}
```

### Explanation
この変更は、OpenAIのAPIバージョンに関するドキュメント内のリンクを修正するものです。具体的には、リンクが相対パスに更新され、一貫性とナビゲーションの向上が図られています。

主な変更点は、以下のとおりです：
- 一部の項目の説明において、リンクが旧来の絶対パスから新しい相対パスに変更されています。
- 新しい相対パスにより、文書全体の可読性と整合性が向上することを目的としています。

修正は、合計で9行の追加と9行の削除があり、全体で18行の変更が行われています。このような改善は、ユーザーがドキュメントの内容をより簡単に理解し、必要な情報にアクセスできるようにするために重要です。

## articles/ai-services/openai/includes/batch/batch-python.md{#item-3121c2}

<details>
<summary>Diff</summary>
````diff
@@ -102,13 +102,13 @@ client = AzureOpenAI(
 file = client.files.create(
   file=open("test.jsonl", "rb"), 
   purpose="batch",
-  #extra_body={"expires_after":{"seconds": 1209600, "anchor": "created_at"}} # Optional you can set to a number between 1209600-2592000. This is equivalent to 14-30 days
+  extra_body={"expires_after":{"seconds": 1209600, "anchor": "created_at"}} # Optional you can set to a number between 1209600-2592000. This is equivalent to 14-30 days
 )
 
 
 print(file.model_dump_json(indent=2))
 
-#print(f"File expiration: {datetime.fromtimestamp(file.expires_at) if file.expires_at is not None else 'Not set'}")
+print(f"File expiration: {datetime.fromtimestamp(file.expires_at) if file.expires_at is not None else 'Not set'}")
 
 file_id = file.id
 ```
@@ -131,20 +131,20 @@ client = AzureOpenAI(
 file = client.files.create(
   file=open("test.jsonl", "rb"), 
   purpose="batch",
-  #extra_body={"expires_after":{"seconds": 1209600, "anchor": "created_at"}} # Optional you can set to a number between 1209600-2592000. This is equivalent to 14-30 days
+  extra_body={"expires_after":{"seconds": 1209600, "anchor": "created_at"}} # Optional you can set to a number between 1209600-2592000. This is equivalent to 14-30 days
 )
 
 
 print(file.model_dump_json(indent=2))
 
-#print(f"File expiration: {datetime.fromtimestamp(file.expires_at) if file.expires_at is not None else 'Not set'}")
+print(f"File expiration: {datetime.fromtimestamp(file.expires_at) if file.expires_at is not None else 'Not set'}")
 
 file_id = file.id
 ```
 
 ---
 
-By uncommenting and adding `extra_body={"expires_after":{"seconds": 1209600, "anchor": "created_at"}}` you're setting our upload file to expire in 14 days. There's a max limit of 500 batch files per resource when no expiration is set. By setting a value for expiration the number of batch files per resource is increased to 10,000 files per resource. This feature isn't currently available in all regions. Output when file upload expiration is set:
+By uncommenting and adding `extra_body={"expires_after":{"seconds": 1209600, "anchor": "created_at"}}` you're setting our upload file to expire in 14 days. There's a max limit of 500 batch files per resource when no expiration is set. By setting a value for expiration the number of batch files per resource is increased to 10,000 files per resource. 
 
 **Output:**
 
@@ -175,7 +175,7 @@ batch_response = client.batches.create(
     input_file_id=file_id,
     endpoint="/chat/completions",
     completion_window="24h",
-    #extra_body={"output_expires_after":{"seconds": 1209600, "anchor": "created_at"}} # Optional you can set to a number between 1209600-2592000. This is equivalent to 14-30 days
+    extra_body={"output_expires_after":{"seconds": 1209600, "anchor": "created_at"}} # Optional you can set to a number between 1209600-2592000. This is equivalent to 14-30 days
 )
 
 
@@ -186,7 +186,7 @@ print(batch_response.model_dump_json(indent=2))
 
 ```
 
-The default 500 max file limit per resource also applies to output files. Here you can uncomment this line to add  `extra_body={"output_expires_after":{"seconds": 1209600, "anchor": "created_at"}}` so that your output files expire in 14 days. By setting a value for expiration the number of batch files per resource is increased to 10,000 files per resource. This feature isn't currently available in all regions.
+The default 500 max file limit per resource also applies to output files. Here you can uncomment this line to add  `extra_body={"output_expires_after":{"seconds": 1209600, "anchor": "created_at"}}` so that your output files expire in 14 days. By setting a value for expiration the number of batch files per resource is increased to 10,000 files per resource. 
 
 > [!NOTE]
 > Currently the completion window must be set to `24h`. If you set any other value than `24h` your job will fail. Jobs taking longer than 24 hours will continue to execute until canceled.
@@ -674,6 +674,7 @@ The following regions support the new fail fast behavior:
 - northcentralus
 - polandcentral
 - swedencentral
+- switzerlandnorth
 - eastus2
 - westus
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理の設定に関するコメントの修正"
}
```

### Explanation
この変更は、Azure OpenAIのバッチ処理に関するPythonコード例を更新するもので、特にファイルの有効期限を設定する機能を強調しています。コード内のいくつかの行でコメントが修正・強調され、より明確規則的になっています。

主な変更点は以下の通りです：
- `extra_body`パラメータのコメントが修正され、有効期限の設定がデフォルト値から明確に変更されました。特に、`extra_body={"expires_after":{"seconds": 1209600, "anchor": "created_at"}}`のコメントがオプションとして有効化されています。
- ファイルの有効期限を設定することによって、バッチファイルの最大数が500から10,000に増加することが明確になっていますが、現在この機能はすべての地域で利用できるわけではないことも再確認されています。
- 全体的に、コメントがより簡潔でわかりやすく修正されています。

この変更は、バッチ処理を利用するユーザーにとって、ファイルの管理と利用に関する適切なガイドラインを提供します。追加された8行と削除された7行により、全体で15行が変更されています。

## articles/ai-services/openai/includes/batch/batch-rest.md{#item-bcccd9}

<details>
<summary>Diff</summary>
````diff
@@ -86,7 +86,7 @@ curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files?api-versio
 
 The above code assumes a particular file path for your test.jsonl file. Adjust this file path as necessary for your local system. 
 
-By adding the optional `"expires_after.seconds=1209600"` and `"expires_after.anchor=created_at"` parameters  you're setting your upload file to expire in 14 days. There's a max limit of 500 batch files per resource when no expiration is set. By setting a value for expiration the number of batch files per resource is increased to 10,000 files per resource. You can set to a number between 1209600-2592000. This is equivalent to 14-30 days. This feature isn't currently available in all regions.
+By adding the optional `"expires_after.seconds=1209600"` and `"expires_after.anchor=created_at"` parameters  you're setting your upload file to expire in 14 days. There's a max limit of 500 batch files per resource when no expiration is set. By setting a value for expiration the number of batch files per resource is increased to 10,000 files per resource. You can set to a number between 1209600-2592000. This is equivalent to 14-30 days.
 
 
 
@@ -151,7 +151,7 @@ curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-vers
   }'
 ```
 
-The default 500 max file limit per resource also applies to output files. Here you can optionally add  `"output_expires_after":{"seconds": 1209600},` and `"anchor": "created_at"` so that your output files expire in 14 days. By setting a value for expiration the number of batch files per resource is increased to 10,000 files per resource. The file expiration feature is currently not available in all regions.
+The default 500 max file limit per resource also applies to output files. Here you can optionally add  `"output_expires_after":{"seconds": 1209600},` and `"anchor": "created_at"` so that your output files expire in 14 days. By setting a value for expiration the number of batch files per resource is increased to 10,000 files per resource. 
 
 > [!NOTE]
 > Currently the completion window must be set to `24h`. If you set any other value than `24h` your job will fail. Jobs taking longer than 24 hours will continue to execute until canceled.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理の有効期限設定についての説明を修正"
}
```

### Explanation
この変更は、Azure OpenAIのバッチ処理に関するREST APIのドキュメントの一部を更新し、ファイルの有効期限設定に関する説明を明確にするものです。具体的には、ファイルの有効期限の設定方法について詳細を整理しています。

主な変更点は以下の通りです：
- 有効期限設定の説明文から、不要な文を削除し、情報を簡潔にまとめています。具体的には、「この機能はすべての地域で利用できるわけではない」という部分を削除しましたが、その内容は明確で維持されています。
- 上記の変更に伴い、テキストの整形が行われ、内容が読みやすくなっています。

この更新により、ユーザーがバッチ処理におけるファイル管理のオプションをより理解しやすくなります。合計で2行の追加と2行の削除があり、4行が変更されています。

## articles/ai-services/openai/includes/model-matrix/standard-audio.md{#item-1d8db7}

<details>
<summary>Diff</summary>
````diff
@@ -6,16 +6,17 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 4/15/2025
+ms.date: 4/17/2025
 ---
 
-| **Region**   | **tts**, **001**   | **tts-hd**, **001**   | **whisper**, **001**  |  **gpt-4o-mini-tts**, **001** | **gpt-4o-transcribe**, **001**   | **gpt-4o-mini-transcribe**, **001**   |
-|:-----------------|:----------------:|:-------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|
-| eastus2          | - | - | ✅ | - | ✅ | ✅ |
-| northcentralus   | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| norwayeast       | - | - | ✅ | - | ✅ | ✅ |
-| southindia       | - | - | ✅ | - | ✅ | ✅ |
-| swedencentral    | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| switzerlandnorth | - | - | ✅ | - | ✅ | ✅ |
-| uaenorth         | - | - | ✅ | - | ✅ | ✅ |
-| westeurope       | - | - | ✅ | - | ✅ | ✅ |
+| **Region**   | **tts**, **001**   | **tts-hd**, **001**   | **whisper**, **001**   |
+|:-----------------|:----------------:|:-------------------:|:--------------------:|
+| eastus2          | -            | -               | ✅                 |
+| northcentralus   | ✅             | ✅                | ✅                 |
+| norwayeast       | -            | -               | ✅                 |
+| southindia       | -            | -               | ✅                 |
+| swedencentral    | ✅             | ✅                | ✅                 |
+| switzerlandnorth | -            | -               | ✅                 |
+| uaenorth         | -            | -               | ✅                 |
+| westeurope       | -            | -               | ✅                 |
+| westus3          | ✅             | ✅                | -                |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "音声モデルの対応地域テーブルの更新"
}
```

### Explanation
この変更は、Azure OpenAIの音声モデルに関するドキュメントの一部を更新し、対応する地域のテーブルを改訂したものです。主に、地域ごとの利用可能な音声モデルの条件が見直されています。

主な変更点は以下の通りです：
- `ms.date`が2025年4月15日から2025年4月17日に修正され、更新日が最新に保たれています。
- テーブルのカラム数が変更され、**gpt-4o-mini-tts** および **gpt-4o-transcribe** に関する情報が削除されました。その結果、音声モデルが **tts**, **tts-hd**, **whisper** のみとなり、テーブルのシンプル化が図られています。
- 新たに **westus3** 地域が追加され、対応する音声モデルのステータスが明示されています。

この更新は、ユーザーがどの地域でどの音声モデルを使用できるかをより明確に理解できるようにするための改善です。合計で12行が追加され、11行が削除されることで、テーブルの全体的な構成が見直されています。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -6,32 +6,32 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 04/14/2025
+ms.date: 04/17/2025
 ---
 
-| **Region**     | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-nano**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **gpt-4.5-preview**, **2025-02-27**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **turbo-2024-04-09**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **2**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4o-audio-preview**, **2024-12-17**   | **gpt-4o-mini-realtime-preview**, **2024-12-17**   | **gpt-4o-mini-audio-preview**, **2024-12-17**   | **gpt-4o-transcribe**, **2025-03-20**   | **gpt-4o-mini-tts**, **2025-03-20**   | **gpt-4o-mini-transcribe**, **2025-03-20**   |
-|:-------------------|:---------------------------:|:--------------------------------:|:--------------------------------:|:-----------------------------------:|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:-------------------------------------------:|:----------------------------------------:|:------------------------------------------------:|:---------------------------------------------:|:-------------------------------------:|:-----------------------------------:|:------------------------------------------:|
-| australiaeast      | -                       | -                            | -                            | -                               | ✅                        | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| brazilsouth        | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| canadaeast         | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| eastus             | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | ✅                                          | -                                 | -                               | -                                      |
-| eastus2            | ✅                        | ✅                             | ✅                             | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | ✅                                        | ✅                                     | ✅                                             | ✅                                          | ✅                                  | ✅                                | ✅                                       |
-| francecentral      | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| germanywestcentral | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| italynorth         | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | -                      | -                      | ✅                       | ✅                            | -                           | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| japaneast          | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| koreacentral       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | -                             | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| northcentralus     | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| norwayeast         | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| polandcentral      | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| southafricanorth   | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| southcentralus     | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| southindia         | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| spaincentral       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| swedencentral      | ✅                        | ✅                             | ✅                             | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | ✅                                        | ✅                                     | ✅                                             | -                                         | -                                 | -                               | -                                      |
-| switzerlandnorth   | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| uaenorth           | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| uksouth            | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| westeurope         | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| westus             | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| westus3            | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| **Region**     | **o4-mini**, **2025-04-16**   | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-nano**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **gpt-4.5-preview**, **2025-02-27**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **turbo-2024-04-09**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **2**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4o-audio-preview**, **2024-12-17**   | **gpt-4o-mini-realtime-preview**, **2024-12-17**   | **gpt-4o-mini-audio-preview**, **2024-12-17**   | **gpt-4o-transcribe**, **2025-03-20**   | **gpt-4o-mini-tts**, **2025-03-20**   | **gpt-4o-mini-transcribe**, **2025-03-20**   |
+|:-------------------|:---------------------------:|:---------------------------:|:--------------------------------:|:--------------------------------:|:-----------------------------------:|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:-------------------------------------------:|:----------------------------------------:|:------------------------------------------------:|:---------------------------------------------:|:-------------------------------------:|:-----------------------------------:|:------------------------------------------:|
+| australiaeast      | -                       | -                       | -                            | -                            | -                               | ✅                        | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| brazilsouth        | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| canadaeast         | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| eastus             | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | ✅                                          | -                                 | -                               | -                                      |
+| eastus2            | ✅                        | ✅                        | ✅                             | ✅                             | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | ✅                                        | ✅                                     | ✅                                             | ✅                                          | ✅                                  | ✅                                | ✅                                       |
+| francecentral      | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| germanywestcentral | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| italynorth         | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | -                      | -                      | ✅                       | ✅                            | -                           | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| japaneast          | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| koreacentral       | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | -                             | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| northcentralus     | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| norwayeast         | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| polandcentral      | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| southafricanorth   | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| southcentralus     | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| southindia         | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| spaincentral       | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| swedencentral      | ✅                        | ✅                        | ✅                             | ✅                             | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | ✅                                        | ✅                                     | ✅                                             | -                                         | -                                 | -                               | -                                      |
+| switzerlandnorth   | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| uaenorth           | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| uksouth            | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| westeurope         | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| westus             | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| westus3            | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルモデルの対応地域テーブルを更新"
}
```

### Explanation
この変更は、Azure OpenAIのグローバルモデルに関するドキュメントを更新し、対応する地域名や利用可能なモデルの情報を再構成したものです。全体的に、テーブルのレイアウトが見直され、モデルのリリース日が更新されています。

主な変更点は以下の通りです：
- `ms.date`が2025年4月14日から2025年4月17日に修正され、文書の更新日が最新に保たれています。
- モデルのリストが変更され、新しいモデル「**o4-mini**」が追加されました。これにより、テーブル内のモデル情報が更新されています。
- すべての地域に関連するテーブルを見直し、対応するモデルの有無が新たに整理されています。

この更新により、ユーザーは各地域でどのモデルを利用可能かをより明確に把握できるようになり、モデルの最新情報が提供されています。合計で27行が追加され、27行が削除され、54行が変更されています。これにより、文書全体が改善され、ユーザーにとっての利便性が向上しています。

## articles/ai-services/openai/includes/text-to-speech-dotnet.md{#item-fea66a}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ recommendations: false
 ## Prerequisites
 
 - An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
-- An Azure OpenAI resource with a text to speech model (such as `tts`) deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure OpenAI resource with a text to speech model (such as `tts`) deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-deployment-regional-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 - [The .NET 8.0 SDK](https://dotnet.microsoft.com/en-us/download)
 
 ### Microsoft Entra ID prerequisites
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事内のリンクの修正"
}
```

### Explanation
この変更は、Azure OpenAIに関するドキュメントの一部を更新し、テキストから音声へ変換するモデルに関連するリンクを修正したものです。具体的には、モデルのデプロイに関する情報に関連するリンクの文言が微調整されています。

主な変更点は以下の通りです：
- テキストから音声へのモデルに関する文言の一部が変更され、リンク先のテキストが「**standard-models-by-endpoint**」から「**standard-deployment-regional-models-by-endpoint**」に修正されました。これにより、読み手がより具体的な情報を得やすくなっています。

この修正は、ユーザーの参照を向上させるためのものであり、関連情報にアクセスしやすくすることを目的としています。合計で1行が追加され、1行が削除されています。

## articles/ai-services/openai/includes/whisper-dotnet.md{#item-562a58}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.date: 3/11/2025
 ## Prerequisites
 
 - An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
-- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-deployment-regional-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 - [The .NET 8.0 SDK](https://dotnet.microsoft.com/en-us/download)
 
 ### Microsoft Entra ID prerequisites
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事内のリンクの修正"
}
```

### Explanation
この変更は、Azure OpenAIに関するドキュメントの中で、音声からテキストへのモデルに関連するリンクを更新したものです。具体的には、デプロイに関する情報を含むリンクの文言が変更されています。

主な変更点は以下の通りです：
- 音声からテキストへのモデルについての説明が、リンク先のセクションを「**standard-models-by-endpoint**」から「**standard-deployment-regional-models-by-endpoint**」に変更しました。これにより、ユーザーが関連する情報により簡単にアクセスできるようになっています。

この修正は、文書の情報をより正確にし、利用者が必要な情報を効果的に得られるようにすることを意図しています。合計で1行が追加され、1行が削除されています。

## articles/ai-services/openai/includes/whisper-javascript.md{#item-3ee990}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: eric-urban
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
-- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-deployment-regional-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 ### Microsoft Entra ID prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事内のリンクの修正"
}
```

### Explanation
この変更は、Azure OpenAIに関連するJavaScriptのドキュメントにおいて、音声からテキストへのモデルに関するリンクを修正したものです。具体的には、モデルのデプロイに関する情報が含まれる文言が更新されました。

主な変更点は以下の通りです：
- 音声からテキストへのモデルについての説明で、リンク先を「**standard-models-by-endpoint**」から「**standard-deployment-regional-models-by-endpoint**」に改訂しました。この変更により、ユーザーがより適切な情報を見つけやすくなっています。

この修正は、ドキュメントの明確性を向上させ、情報アクセスを円滑にすることを目的としています。合計で1行が追加され、1行が削除されています。

## articles/ai-services/openai/includes/whisper-powershell.md{#item-7db269}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ author: eric-urban
 
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - <a href="https://aka.ms/installpowershell" target="_blank">You can use either the latest version, PowerShell 7, or Windows PowerShell 5.1.</a>
-- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-deployment-regional-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 ## Set up
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事内のリンクの修正"
}
```

### Explanation
この変更は、Azure OpenAIに関するPowerShellのドキュメントにおいて、音声からテキストへのモデルに関連するリンクの表現を修正しました。具体的には、モデルのデプロイに関する情報が正確なリンク形式に更新されています。

主な変更点は以下の通りです：
- 音声からテキストへのモデルについての説明で、リンク先を「**standard-models-by-endpoint**」から「**standard-deployment-regional-models-by-endpoint**」に変更しました。この更新は、利用者が必要な情報へアクセスする手助けとなることを目的としています。

この修正により、ドキュメントの正確性が向上し、ユーザーにとっての情報の明瞭さが増しています。合計で1行が追加され、1行が削除されています。

## articles/ai-services/openai/includes/whisper-python.md{#item-e61179}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.date: 3/19/2024
 ## Prerequisites
 
 - An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
-- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-deployment-regional-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 - [Python 3.8 or later](https://www.python.org)
 - The following Python library: os
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事内のリンクの修正"
}
```

### Explanation
この変更は、Azure OpenAIに関するPythonのドキュメントにおいて、音声からテキストモデルに関するリンクを修正したものです。具体的には、モデルのデプロイに関する情報の表現が更新され、より明確なリンクに変更されています。

主な変更点は以下の通りです：
- 音声からテキストモデルに関する説明で、リンクが「**standard-models-by-endpoint**」から「**standard-deployment-regional-models-by-endpoint**」に変更されました。この修正により、必要な情報にアクセスしやすくなり、ユーザー体験が向上しています。

この修正は、ドキュメントの正確性を高め、読者に対してより適切な情報を提供することを目的としています。合計で1行が追加され、1行が削除されており、全体として文書の内容にわずかな改善がもたらされています。

## articles/ai-services/openai/includes/whisper-rest.md{#item-639ccb}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ author: eric-urban
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
 
-- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-deployment-regional-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 - Be sure that you are assigned at least the [Cognitive Services Contributor](../how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事内のリンクの修正"
}
```

### Explanation
この変更は、Azure OpenAIに関するREST APIに関するドキュメントにおいて、音声からテキストモデルに関連するリンクの表現を修正したものです。具体的には、モデルのデプロイ情報に関するリンクがより具体的なものに更新されています。

主な変更点は以下の通りです：
- 音声からテキストモデルに関する説明で、リンクが「**standard-models-by-endpoint**」から「**standard-deployment-regional-models-by-endpoint**」に変更されました。この更新によって、ユーザーは必要な地域モデルに関する情報へよりスムーズにアクセスできるようになっています。

この修正は、技術文書の正確性を高め、読者にとっての情報の明瞭さを向上させることを目的としています。合計で1行が追加され、1行が削除されており、文書全体の内容に小幅ながら重要な改善が施されています。

## articles/ai-services/openai/includes/whisper-typescript.md{#item-eafedb}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ author: eric-urban
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
 - [TypeScript](https://www.typescriptlang.org/download/)
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
-- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure OpenAI resource with a speech to text model deployed in a [supported region](../concepts/models.md?tabs=standard-audio#standard-deployment-regional-models-by-endpoint). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 ### Microsoft Entra ID prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事内のリンクの修正"
}
```

### Explanation
この変更は、Azure OpenAIに関連するTypeScriptのドキュメントにおいて、音声からテキストモデルに関するリンクの表現を修正したものです。特に、モデルのデプロイに係る情報がより明確なリンクに更新されています。

主な変更点は以下の通りです：
- 音声からテキストモデルについての説明で、リンクが「**standard-models-by-endpoint**」から「**standard-deployment-regional-models-by-endpoint**」に変更されました。この更新により、ユーザーは特定の地域モデルに関する情報により適切にアクセスできるように設計されています。

この修正は、技術ドキュメントの正確性を向上させ、読者に対して必要な情報をより明確に提供することを目的としています。全体として、1行が追加され、1行が削除されており、文書内容にわずかながら重要な改善が施されています。

## articles/ai-services/openai/whisper-quickstart.md{#item-4cae3d}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,7 @@ zone_pivot_groups: programming-languages-rest-ps-py-js-cs
 This quickstart explains how to use the [Azure OpenAI Whisper model](../speech-service/whisper-overview.md) for speech to text conversion. The Whisper model can transcribe human speech in numerous languages, and it can also translate other languages into English.
 
 > [!NOTE]
-> For information about other audio models that you can use with Azure OpenAI, see [Audio models](./concepts/models.md?tabs=standard-audio#standard-models-by-endpoint).
+> For information about other audio models that you can use with Azure OpenAI, see [Audio models](./concepts/models.md?tabs=standard-audio#standard-deployment-regional-models-by-endpoint).
 
 The file size limit for the Whisper model is 25 MB. If you need to transcribe a file larger than 25 MB, you can use the Azure AI Speech [batch transcription](../speech-service/batch-transcription-create.md#use-a-whisper-model) API.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "音声モデルリンクの修正"
}
```

### Explanation
この変更は、Azure OpenAI Whisperモデルに関するクイックスタートガイドのドキュメントにおいて、オーディオモデルに関するリンクの表現を修正したものです。具体的には、Azure OpenAIに関連するオーディオモデルの概要についての情報が、より明確なリンクに更新されています。

主な変更点は以下の通りです：
- オーディオモデルに関する注釈内のリンクが「**standard-models-by-endpoint**」から「**standard-deployment-regional-models-by-endpoint**」に変更されています。この修正により、ユーザーはオーディオモデルの情報を特定の地域でのデプロイメントに関するものとして、より明瞭に理解できるようになります。

この修正は、技術文書の正確性の向上と、情報へのアクセスの容易さを目的としています。1行が追加され、1行が削除されており、全体としてドキュメントに対する小幅ながら重要な改善が行われています。


