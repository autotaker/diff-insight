---
date: '2025-04-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:57b3ac1...MicrosoftDocs:869fffd
summary: 今回の変更は、Azure OpenAIサービスにおける複数のドキュメントの更新を行い、新しい画像生成モデルである`GPT-image-1`についての情報を追加し、記述を見直すものです。主な新機能としては、`GPT-image-1`モデルのリリース、関連するAPIエンドポイントやパラメータの詳細、画像生成機能の説明の大幅な更新が含まれます。特に大きな破壊的変更はありませんが、一部文書でモデル名や用語の統一が行われているため、旧ドキュメントとの一貫性に注意が必要です。全体として、この変更はユーザーに正確で最新の情報を提供し、混乱を避けるための工夫が施されています。今後もOpenAIが迅速な情報提供を続けることが期待されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:57b3ac1...MicrosoftDocs:869fffd){target="_blank"}

<format>
# Highlights
このコードの変更は、Azure OpenAIサービスにおける複数のドキュメントを更新し、特に画像生成モデルに関する記述を見直し、新しい情報を追加するものです。主な新機能として、新しい`GPT-image-1`モデルのリリースが挙げられます。これに伴い、多くのドキュメントで用語の変更や情報の明確化が行われています。

## New features
- 新しい`GPT-image-1`モデルの公開。
- `GPT-image-1`に関連したAPIエンドポイントやパラメータの詳細が追加。
- 画像生成機能の説明の大幅な更新。

## Breaking changes
特にありませんが、一部の文書でモデル名の変更や用語の統一が行われているため、旧ドキュメントとの一貫性が失われる可能性があります。

## Other updates
- 複数のドキュメントにおいて、用語の統一とコンテンツの明確化が行われました。
- FAQやコンテンツフィルタ、プロンプト変換に関する情報が最新化。
- モデルの廃止日や安全ポリシーが更新。
- REST API、Python、JavaScript、PowerShellなど異なるプログラミング言語に対応したドキュメントでの調整。

# Insights
今回の変更は、Azure OpenAIサービスのドキュメントの質を向上させ、利用者に正確で最新の情報を提供することを目的としています。特に、`GPT-image-1`という新しい画像生成モデルの導入が中心となり、ユーザーが最先端のAIモデルを適切に活用できるようにサポートしています。

「DALL-E」から「GPT-image-1」への移行は、単なる名前の変更ではなく、精度と機能性の向上を意図したものであり、画像生成の領域でのOpenAIの技術力向上を示しています。このモデルは、テキストプロンプトからの画像生成に新しい領域を切り拓く一方、他の非画像生成モデルへの適用も見据えています。

また、ドキュメント全般にわたって用語の統一が行われており、これはユーザーが異なるドキュメントセクション間で混乱しないようにするための工夫です。特に、APIリクエストにおける正確なパラメータやエンドポイント情報を提供することで、不具合のない、スムーズな開発体験が得られるように設計されています。

クオータや制限に関する最新情報も、リソース管理やサービス利用計画において実用的なものであり、企業ユーザーには特に重要な情報といえるでしょう。今後もOpenAIがこのような更新を続け、技術革新に対応した迅速な情報提供を行うことが期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [content-credentials.md](#item-a23b50) | minor update | コンテンツクレデンシャルに関する新情報の更新 | modified | 8 | 8 | 16 | 
| [content-filter.md](#item-dfc7e7) | minor update | コンテンツフィルタリングシステムに関する記述の修正 | modified | 1 | 1 | 2 | 
| [default-safety-policies.md](#item-39b6a0) | minor update | 画像生成モデルに関する安全ポリシーの明確化 | modified | 1 | 1 | 2 | 
| [model-retirements.md](#item-03fc2e) | minor update | モデルの廃止日と引き継ぎ予定の更新 | modified | 8 | 8 | 16 | 
| [models.md](#item-db2c37) | minor update | 画像生成モデルに関する用語の更新 | modified | 21 | 5 | 26 | 
| [prompt-transformation.md](#item-21e047) | minor update | プロンプト変換に関する情報の更新 | modified | 5 | 5 | 10 | 
| [faq.yml](#item-6deb71) | minor update | Azure OpenAIサービスに関するFAQの情報更新 | modified | 1 | 1 | 2 | 
| [content-filters.md](#item-6f0627) | minor update | コンテンツフィルタに関する説明の更新 | modified | 1 | 1 | 2 | 
| [dall-e.md](#item-ac9616) | new feature | 画像生成モデルに関する内容の大幅更新 | modified | 197 | 23 | 220 | 
| [evaluations.md](#item-dfaa1c) | minor update | ROUGEメトリクスの説明の改善 | modified | 8 | 6 | 14 | 
| [reasoning.md](#item-a54b2f) | minor update | モデル機能に関する詳細情報の明確化 | modified | 9 | 7 | 16 | 
| [responses.md](#item-b9757d) | minor update | 新しいモデルの追加情報の更新 | modified | 1 | 0 | 1 | 
| [latest-inference-preview.md](#item-24bf0f) | new feature | GPT-image-1モデルの新機能とAPIエンドポイントの更新 | modified | 150 | 9 | 159 | 
| [dall-e-dotnet.md](#item-755f0a) | minor update | 用語の統一と更新 | modified | 2 | 2 | 4 | 
| [dall-e-go.md](#item-132707) | minor update | 用語の統一と更新 | modified | 2 | 2 | 4 | 
| [dall-e-java.md](#item-373f89) | minor update | 用語の統一と更新 | modified | 2 | 2 | 4 | 
| [dall-e-javascript.md](#item-6cffcf) | minor update | 用語の統一と更新 | modified | 2 | 2 | 4 | 
| [dall-e-powershell.md](#item-97878b) | minor update | 用語の統一と更新 | modified | 2 | 2 | 4 | 
| [dall-e-python.md](#item-c91824) | minor update | 用語の統一と説明の更新 | modified | 2 | 2 | 4 | 
| [dall-e-rest.md](#item-4bac64) | minor update | 用語の統一と情報の明確化 | modified | 2 | 2 | 4 | 
| [dall-e-studio.md](#item-439729) | minor update | 用語の統一と情報の明確化 | modified | 2 | 2 | 4 | 
| [dall-e-typescript.md](#item-57b205) | minor update | 用語の統一と情報の明確化 | modified | 2 | 2 | 4 | 
| [dotnet.md](#item-46e881) | minor update | ガイドタイトルの修正 | modified | 1 | 1 | 2 | 
| [global-batch.md](#item-929e6a) | minor update | モデルマトリックスの地域データの修正 | modified | 0 | 2 | 2 | 
| [structured-outputs-python.md](#item-2734f0) | minor update | Pythonモジュールのインポート追加 | modified | 2 | 0 | 2 | 
| [index.yml](#item-0adb87) | minor update | モデル名の修正とリンクテキストの変更 | modified | 3 | 3 | 6 | 
| [overview.md](#item-97d507) | minor update | モデル名と説明の修正 | modified | 2 | 2 | 4 | 
| [quotas-limits.md](#item-06c6f9) | minor update | GPT-image-1のクオータ制限の追加 | modified | 2 | 1 | 3 | 
| [toc.yml](#item-c945af) | minor update | DALL-Eの名称をImage Generationに変更 | modified | 2 | 2 | 4 | 
| [whats-new.md](#item-53303b) | new feature | GPT-image-1モデルのリリース情報追加 | modified | 11 | 0 | 11 | 


# Modified Contents
## articles/ai-services/openai/concepts/content-credentials.md{#item-a23b50}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: PatrickFarley
 ms.author: pafarley
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 02/20/2025
+ms.date: 04/23/2025
 manager: nitinme
 ---
 
@@ -16,14 +16,14 @@ With the improved quality of content from generative AI models, there is an incr
 
 ## What are Content Credentials? 
 
-Content Credentials in the Azure OpenAI Service provide customers with information about the origin of an image generated by the DALL-E series models. This information is represented by a manifest attached to the image. The manifest is cryptographically signed by a certificate that traces back to Azure OpenAI Service.
+Content Credentials in the Azure OpenAI Service provide customers with information about the origin of an image generated by the image generation models. This information is represented by a manifest attached to the image. The manifest is cryptographically signed by a certificate that traces back to Azure OpenAI Service.
 
 The manifest contains several key pieces of information: 
 
 | Field name | Field content |
 | ---| ---|
-| `"description"` | This field has a value of `"AI Generated Image"` for all DALL-E model generated images, attesting to the AI-generated nature of the image. |
-| `"softwareAgent"` | This field has a value of `"Azure OpenAI DALL-E"` for all images generated by DALL-E series models in Azure OpenAI Service. |
+| `"description"` | This field has a value of `"AI Generated Image"` for all generated images, attesting to the AI-generated nature of the image. |
+| `"softwareAgent"` | This field has a value of `"Azure OpenAI DALL-E"` or `"Azure OpenAI ImageGen"` for all images generated by DALL-E series models or GPT-image-1 models in Azure OpenAI Service. |
 |`"when"` |The timestamp of when the Content Credentials were created. | 
 
 
@@ -32,12 +32,12 @@ Content Credentials in the Azure OpenAI Service can help people understand when
 ## How do I use Content Credentials in my solution today?
 
 Customers may use Content Credentials by:
-- Ensuring that their AI generated images contain Content Credentials
-    No additional set-up is necessary. Content Credentials are automatically applied to all generated images from DALL·E in the Azure OpenAI Service. 
+- Ensuring that their AI-generated images contain Content Credentials
+    No additional set-up is necessary. Content Credentials are automatically applied to all generated images from DALL·E and GPT-image-1 in the Azure OpenAI Service. 
 - Verifying that an image has Content Credentials
-    There are two recommended ways today to check the credential of an image generated by Azure OpenAI DALL-E models:
+    There are two recommended ways today to check the credential of an image generated by Azure OpenAI models:
 
-    - **Content Credentials Verify webpage (contentcredentials.org/verify)**: This is a tool that allows users to inspect the Content Credentials of a piece of content. If an image was generated by DALL-E in Azure OpenAI, the tool will display that its Content Credentials were issued by Microsoft Corporation alongside the date and time of issuance.
+    - **Content Credentials Verify webpage (contentcredentials.org/verify)**: This is a tool that allows users to inspect the Content Credentials of a piece of content. If an image was generated by an Azure OpenAI image generation model, the tool will display that its Content Credentials were issued by Microsoft Corporation alongside the date and time of issuance.
        :::image type="content" source="../media/encryption/credential-check.png" alt-text="Screenshot of the content credential verification website.":::
     
        This page shows that an image generated by Azure OpenAI DALL-E has Content Credentials issued by Microsoft.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツクレデンシャルに関する新情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるコンテンツクレデンシャルに関するドキュメントのいくつかの情報を最新にすることを目的としています。具体的には、DALL-Eモデルから生成された画像に関連する説明やフィールド情報の更新が含まれています。修正された内容は以下の通りです。

1. 日付が新たに「2025年4月23日」に変更されました。
2. コンテンツクレデンシャルの説明が、DALL-Eモデルに限定されず、さまざまな画像生成モデルに適用されることを反映するように更新されました。
3. 使用者が自分の解決策でコンテンツクレデンシャルを利用するための手順の拡張が行われています。具体的には、利用可能な画像生成モデルの範囲が広がり、DALL-EモデルおよびGPT-image-1モデルから生成された画像が含まれています。

この修正により、ユーザーは新しい情報をもとにAzure OpenAIサービスを利用する上での理解が深まることが期待されます。

## articles/ai-services/openai/concepts/content-filter.md{#item-dfc7e7}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ manager: nitinme
 > [!IMPORTANT]
 > The content filtering system isn't applied to prompts and completions processed by the audio models such as Whisper in Azure OpenAI Service. Learn more about the [Audio models in Azure OpenAI](models.md?tabs=standard-audio#standard-deployment-regional-models-by-endpoint).
 
-Azure OpenAI Service includes a content filtering system that works alongside core models, including DALL-E image generation models. This system works by running both the prompt and completion through an ensemble of classification models designed to detect and prevent the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions. Variations in API configurations and application design might affect completions and thus filtering behavior.
+Azure OpenAI Service includes a content filtering system that works alongside core models, including image generation models. This system works by running both the prompt and completion through an ensemble of classification models designed to detect and prevent the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions. Variations in API configurations and application design might affect completions and thus filtering behavior.
 
 The text content filtering models for the hate, sexual, violence, and self-harm categories have been specifically trained and tested on the following languages: English, German, Japanese, Spanish, French, Italian, Portuguese, and Chinese. However, the service can work in many other languages, but the quality might vary. In all cases, you should do your own testing to ensure that it works for your application.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングシステムに関する記述の修正"
}
```

### Explanation
この変更は、Azure OpenAIサービスのコンテンツフィルタリングシステムに関する説明を少し更新したものです。主な更新内容は次のとおりです。

1. **モデルの言及の修正**: DALL-E画像生成モデルを具体的に言及する文から、単に「画像生成モデル」として簡略化されました。これにより、DALL-Eだけでなく、他の生成モデルに対しても適用可能であることが反映されています。

2. **重要な注意事項の強調**: 音声モデル（例えばWhisper）によって処理されたプロンプトや結果には、コンテンツフィルタリングシステムが適用されないという重要な情報が強調されています。

この変更により、ユーザーはコンテンツフィルタリングシステムの機能をより正確に理解し、他の画像生成モデルとの関係性についても明確になることが期待されます。

## articles/ai-services/openai/concepts/default-safety-policies.md{#item-39b6a0}

<details>
<summary>Diff</summary>
````diff
@@ -65,4 +65,4 @@ Text models in the Azure OpenAI Service can take in and generate both text and c
 | Profanity                                         | Prompts                | N/A                 |
 
 
-In addition to the above safety configurations, Azure OpenAI DALL-E also comes with [prompt transformation](./prompt-transformation.md) by default. This transformation occurs on all prompts to enhance the safety of your original prompt, specifically in the risk categories of diversity, deceptive generation of political candidates, depictions of public figures, protected material, and others. 
\ No newline at end of file
+In addition to the above safety configurations, the latest image generation models also come with [prompt transformation](./prompt-transformation.md) by default. This transformation occurs on all prompts to enhance the safety of your original prompt, specifically in the risk categories of diversity, deceptive generation of political candidates, depictions of public figures, protected material, and others. 
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像生成モデルに関する安全ポリシーの明確化"
}
```

### Explanation
この変更は、Azure OpenAIサービスのデフォルトの安全ポリシーに関する文書の一部を更新したものです。具体的には、DALL-Eに関連する記述が最新の画像生成モデルの記述に変更されています。これにより、DALL-Eだけでなく、その他の最新の画像生成モデルにも適用されることを明確にしています。

主な更新ポイントは以下の通りです：

1. **モデルの範囲の拡大**: 「Azure OpenAI DALL-E」という特定のモデルから「最新の画像生成モデル」というより広範な表現に変更されました。これにより、新しい画像生成モデルが同様の安全性を提供することを示しています。

2. **安全性の強化に関する説明の維持**: プロンプト変換が引き続き全てのプロンプトに適用されることが強調されており、リスクカテゴリに対する安全性の強化が目的である点はそのまま維持されています。

この修正により、ユーザーはAzure OpenAIの最新の画像生成モデルが持つ安全機能についてより正確な理解が得られることが期待されます。

## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 04/17/2025
+ms.date: 04/23/2025
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -95,25 +95,24 @@ These models are currently available for use in Azure OpenAI Service.
 | ---- | ---- | ---- | --- |
 | `dall-e-3` | 3 | No earlier than June 30, 2025 | |
 | `gpt-35-turbo-16k`| 0613 | April, 30, 2025 | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
-| `gpt-35-turbo` | 1106 | No earlier than May 31, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 21, 2025. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
-| `gpt-35-turbo` | 0125 | No earlier than May 31, 2025 | `gpt-4o-mini` |
+| `gpt-35-turbo` | 1106 | July 16, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 21, 2025. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
+| `gpt-35-turbo` | 0125 | July 16, 2025 | `gpt-4o-mini` |
 | `gpt-4`<br>`gpt-4-32k` | 0314 | June 6, 2025 | `gpt-4o` |
 | `gpt-4`<br>`gpt-4-32k` | 0613 | June 6, 2025 | `gpt-4o` |
 | `gpt-4` | turbo-2024-04-09 | No earlier than June 6, 2025 | `gpt-4o`|
 | `gpt-4` | 1106-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025 **<sup>1</sup>** <br>Retirement date: May 1, 2025  | `gpt-4o`|
 | `gpt-4` | 0125-preview |To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025 **<sup>1</sup>** <br>Retirement date: May 1, 2025  | `gpt-4o` |
-| `gpt-4` | vision-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025  **<sup>1</sup>** <br>Retirement date: May 1, 2025 | `gpt-4o`|
+| `gpt-4` | vision-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025  **<sup>1</sup>** <br>Retirement date: May 15, 2025 | `gpt-4o`|
 | `gpt-4.5-preview` | 2025-02-27 | July 14, 2025 | `gpt-4.1` |
 | `gpt-4.1` | 2025-04-14 | No earlier than April 11, 2026 | |
 | `gpt-4.1-mini` | 2025-04-14 | No earlier than April 11, 2026 |
 | `gpt-4.1-nano` | 2025-04-14 | No earlier than April 11, 2026 |
 | `gpt-4o` | 2024-05-13 | No earlier than June 30, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on March 17, 2025. | |
 | `gpt-4o` | 2024-08-06 | No earlier than August 6, 2025  | |
-| `gpt-4o` | 2024-11-20 | No earlier than November 20, 2025  | |
-| `gpt-4o-mini` | 2024-07-18 | No earlier than July 18, 2025  | |
-| `gpt-4o-realtime-preview` | 2024-10-01 | **Deprecated:** February 25, 2025<br>**Retirement:** No earlier than March 26, 2025 | `gpt-4o-realtime-preview` (version 2024-12-17) or `gpt-4o-mini-realtime-preview` (version 2024-12-17) |
+| `gpt-4o` | 2024-11-20 | January 30, 2026  | |
+| `gpt-4o-mini` | 2024-07-18 | August 16, 2025  | |
 | `gpt-3.5-turbo-instruct` | 0914 | No earlier than May 31, 2025 |  |
-| `o1-preview` | 2024-09-12 | No earlier than April 2, 2025 | `o1` |
+| `o1-preview` | 2024-09-12 | May 29, 2025 | `o1` |
 | `o1` | 2024-12-17 | No earlier than December 17, 2025 | |
 | `o4-mini` | 2025-04-16 | No earlier than April 11, 2026 | |
 | `o3` | 2025-04-16 | No earlier than April 11, 2026 | |
@@ -149,6 +148,7 @@ If you're an existing customer looking for information about these models, see [
 
 | Model | Deprecation date | Retirement date | Suggested replacement |
 | --------- | --------------------- | ------------------- | -------------------- |
+| `gpt-4o-realtime-preview` - 2024-10-01 | February 25, 2025 | March 26, 2025 | `gpt-4o-realtime-preview` (version 2024-12-17) or `gpt-4o-mini-realtime-preview` (version 2024-12-17) |
 | `gpt-35-turbo` - 0301 | | February 13, 2025   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
 | `gpt-35-turbo` - 0613 | | February 13, 2025 | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
 | babbage-002 | | January 27, 2025 |  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの廃止日と引き継ぎ予定の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるモデルの廃止日や新しいモデルへの引き継ぎに関する情報を更新したものです。主な変更点は以下の通りです：

1. **日付の更新**: 更新された日付により、モデルの廃止予定日やアップグレード日が新しいタイムラインに調整されています。具体的には、`gpt-35-turbo`や`gpt-4`などのモデルの廃止日が変更され、最新の情報が反映されています。

2. **構造の整理**: モデルごとの詳細情報が整理され、各モデルの廃止日や引き継ぎが明確に記載されています。また、一部のモデルについては、今後の自動アップデートに関する情報も強調されています。

3. **新モデルの追加**: 新たに`gpt-4o`や`gpt-4o-mini`などのモデルが追加され、これらのモデルの廃止日や引き継ぎに関する情報も追記されています。これにより、ユーザーは新旧モデルの関係を理解しやすくなっています。

この変更により、Azure OpenAIサービスのユーザーは、モデルの運用に関する最新の情報を把握できるようになり、適切な計画や準備を行う助けとなることが期待されます。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 04/16/2025
+ms.date: 04/23/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -26,7 +26,7 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 | [GPT-4](#gpt-4) | A set of models that improve on GPT-3.5 and can understand and generate natural language and code. |
 | [GPT-3.5](#gpt-35) | A set of models that improve on GPT-3 and can understand and generate natural language and code. |
 | [Embeddings](#embeddings-models) | A set of models that can convert text into numerical vector form to facilitate text similarity. |
-| [DALL-E](#dall-e-models) | A series of models that can generate original images from natural language. |
+| [Image generation](#image-generation-models) | A series of models that can generate original images from natural language. |
 | [Audio](#audio-models) | A series of models for speech to text, translation, and text to speech. GPT-4o audio models support either low-latency, "speech in, speech out" conversational interactions or audio generation. |
 
 ## GPT 4.1 series
@@ -220,9 +220,24 @@ The third generation embeddings models support reducing the size of the embeddin
 
 OpenAI's MTEB benchmark testing found that even when the third generation model's dimensions are reduced to less than `text-embeddings-ada-002` 1,536 dimensions performance remains slightly better.
 
-## DALL-E
+## Image generation models
 
-The DALL-E models generate images from text prompts that the user provides. DALL-E 3 is generally available for use with the REST APIs. DALL-E 2 and DALL-E 3 with client SDKs are in preview.
+The image generation models generate images from text prompts that the user provides. GPT-image-1 is in limited access public preview. DALL-E 3 is generally available for use with the REST APIs. DALL-E 2 and DALL-E 3 with client SDKs are in preview.
+
+### Availability
+
+**For access to `gpt-image-1` registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who have access to other limited access models will still need to request access for this model.
+
+Request access: [`computer-use-preview` limited access model application](https://aka.ms/oai/gptimage1access)
+
+Once access has been granted, you will need to create a deployment for the model.
+
+### Region availability
+
+| Model | Region |
+|---|---|
+|`dall-e-3` | East US<br>Australia East<br>Sweden Central|
+|`gpt-image-1` | West US 2 (Global Standard) <br> UAE North (Global Standard) |
 
 ## Audio models
 
@@ -414,10 +429,11 @@ These models can only be used with Embedding API requests.
 
 [!INCLUDE [Image Generation](../includes/model-matrix/standard-image-generation.md)]
 
-### DALL-E models
+### Image generation models
 
 |  Model ID  | Max Request (characters) |
 |  --- | :---: |
+| gpt-image-1 | 4,000 |
 | dall-e-3  | 4,000 |
 
 # [Audio](#tab/standard-audio)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像生成モデルに関する用語の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスのモデルに関する文書の一部を更新したものです。主な変更点は以下の通りです：

1. **セクションタイトルの変更**: 「DALL-E」という名称が「画像生成モデル」に変更され、DALL-Eに関連する情報がこれに基づいて記述されています。これにより、文書はより包括的な内容に整理されました。

2. **モデルの詳細の追加**: 新しいGPT画像モデルである`gpt-image-1`についての情報が追加されました。このモデルのアクセス方法、利用可能な地域、以及びリクエスト方法が詳述されています。

3. **モデルの可用性の明確化**: 特定のモデルがどの地域で利用可能かを示す表が追加され、ユーザーはどの地域で特定の画像生成モデルを利用できるかを参照できるようになりました。

4. **コア情報の更新**: その他のモデルについても必要な情報が更新され、APIや利用方法に関する整合性が向上しています。

この変更によって、Azure OpenAIサービスのユーザーは、画像生成モデルに関する最新の情報を得ることができ、モデルの利用についての理解が深まることが期待されます。

## articles/ai-services/openai/concepts/prompt-transformation.md{#item-21e047}

<details>
<summary>Diff</summary>
````diff
@@ -12,12 +12,12 @@ manager: nitinme
 
 # What is prompt transformation?
 
-Prompt transformation is a process included in DALL-E 3 image generation that applies a safety and quality system message to your original prompt. It uses a large language model (LLM) call to add the message before sending your prompt to the model for image generation. This system message enriches your original prompt with the goal of generating more diverse and higher-quality images while maintaining intent. 
+Prompt transformation is a process included in the DALL-E 3 and GPT-image-1 (preview) models that applies a safety and quality system message to your original prompt. It uses a large language model (LLM) call to add the message before sending your prompt to the model for image generation. This system message enriches your original prompt with the goal of generating more diverse and higher-quality images while maintaining intent. 
 
 After prompt transformation is applied to the original prompt, content filtering is applied as a secondary step before image generation; for more information, see [Content filtering](./content-filter.md).
 
 > [!TIP]
-> Learn more about image generation prompting in OpenAI's [DALL·E documentation](https://platform.openai.com/docs/guides/images/language-specific-tips).
+> Learn more about image generation prompting in OpenAI's [Image generation documentation](https://platform.openai.com/docs/guides/images/language-specific-tips).
 
 ## Prompt transformation example
 
@@ -30,11 +30,11 @@ After prompt transformation is applied to the original prompt, content filtering
 
 Prompt transformation is essential for responsible and high-quality generations. Not only does prompt transformation improve the safety of your generated image, but it also enriches your prompt in a more descriptive manner, leading to higher quality and descriptive imagery.
 
-Default prompt transformation in Azure OpenAI DALL-E 3 contains safety enhancements that steer the model away from generating images of Copyright Studio characters and artwork, public figures, and other harmful content such as sexual, hate and unfairness, violence, and self-harm content.
+Default prompt transformation contains safety enhancements that steer the model away from generating images of Copyright Studio characters and artwork, public figures, and other harmful content such as sexual, hate and unfairness, violence, and self-harm content.
 
 ## How do I use prompt transformation?
 
-Prompt transformation is applied by default to all Azure OpenAI DALL-E 3 requests. No extra setup is required to benefit from prompt transformation enhancements.
+Prompt transformation is applied by default to all Azure OpenAI DALL-E 3 and GPT-image-1 requests. No extra setup is required to benefit from prompt transformation enhancements.
 
 Like image generation, prompt transformation is non-deterministic due to the nature of large language models. A single original prompt may lead to many image variants.
 
@@ -69,4 +69,4 @@ Output Content:
 ## Next step
 
 > [!div class="nextstepaction"]
-> [DALL-E quickstart](/azure/ai-services/openai/dall-e-quickstart)
+> [Image generation quickstart](/azure/ai-services/openai/dall-e-quickstart)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプト変換に関する情報の更新"
}
```

### Explanation
この変更は、「プロンプト変換」に関する文書を更新し、Azure OpenAIサービスにおける画像生成のプロセスを明確にすることを目的としています。主な変更点は以下になります：

1. **モデルの拡張**: プロンプト変換の説明において、画像生成に使用されるモデルがDALL-E 3から`GPT-image-1（プレビュー）`に拡張されました。これにより、両方のモデルがプロンプト変換の恩恵を受けることが強調されています。

2. **リンクの更新**: DALL-Eに関するドキュメントへのリンクが、新しい「画像生成に関するドキュメント」に更新され、より適切なリソースへの誘導となっています。

3. **安全性情報の明確化**: プロンプト変換のデフォルト設定について具体的なモデル名が削除され、一般的な安全性の向上について言及されています。これにより、実装の柔軟性が高まり、複数のモデルに対して同様の安全基準が適用されることが示されています。

4. **手順の簡潔化**: Azure OpenAI DALL-E 3とGPT-image-1のリクエストにプロンプト変換がデフォルトで適用されることが明記され、ユーザーが特別な設定を必要としないことが強調されています。

この更新により、プロンプト変換の機能や利点がより広く理解されやすくなり、ユーザーはAzure OpenAIサービスを利用する上でのしっかりとしたガイダンスを得られることが期待されます。

## articles/ai-services/openai/faq.yml{#item-6deb71}

<details>
<summary>Diff</summary>
````diff
@@ -41,7 +41,7 @@ sections:
       - question: |
           How do the capabilities of Azure OpenAI compare to OpenAI?
         answer: | 
-          Azure OpenAI Service gives customers advanced language AI with OpenAI GPT-3, Codex, and DALL-E models with the security and enterprise promise of Azure. Azure OpenAI codevelops the APIs with OpenAI, ensuring compatibility and a smooth transition from one to the other.
+          Azure OpenAI Service gives customers advanced language AI with the latest OpenAI models with the security and enterprise promise of Azure. Azure OpenAI codevelops the APIs with OpenAI, ensuring compatibility and a smooth transition from one to the other.
           
           With Azure OpenAI, customers get the security capabilities of Microsoft Azure while running the same models as OpenAI. 
       - question: |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスに関するFAQの情報更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関するFAQの内容を更新したものです。主な変更点は以下の通りです：

1. **最新のモデルへの言及の更新**: FAQの中で「OpenAI GPT-3、Codex、DALL-Eモデル」と具体的に名前を挙げていた部分が、「最新のOpenAIモデル」に変更されています。この変更により、記載内容がより包括的かつ最新の状態を反映していることが強調され、特定のモデルに依存しない説明になっています。

2. **全体的な明瞭さの向上**: モデルの名称を一般化することで、今後リリースされる新しいモデルにも言及することが可能になり、ユーザーが常に最新の情報を求める際のアクセスが容易になります。

この更新によって、Azure OpenAIサービスの便利さや安全性をアピールしながら、ユーザーが持つ質問に対してより正確で包括的な回答が提供されるようになっています。

## articles/ai-services/openai/how-to/content-filters.md{#item-6f0627}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.custom: FY25Q1-Linter
 
 # How to configure content filters
 
-The content filtering system integrated into Azure AI Foundry runs alongside the core models, including DALL-E image generation models. It uses an ensemble of multi-class classification models to detect four categories of harmful content (violence, hate, sexual, and self-harm) at four severity levels respectively (safe, low, medium, and high), and optional binary classifiers for detecting jailbreak risk, existing text, and code in public repositories. 
+The content filtering system integrated into Azure AI Foundry runs alongside the core models, including image generation models. It uses an ensemble of multi-class classification models to detect four categories of harmful content (violence, hate, sexual, and self-harm) at four severity levels respectively (safe, low, medium, and high), and optional binary classifiers for detecting jailbreak risk, existing text, and code in public repositories. 
 
 The default content filtering configuration is set to filter at the medium severity threshold for all four content harms categories for both prompts and completions. That means that content that is detected at severity level medium or high is filtered, while content detected at severity level low or safe is not filtered by the content filters. Learn more about content categories, severity levels, and the behavior of the content filtering system [here](../concepts/content-filter.md). 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタに関する説明の更新"
}
```

### Explanation
この変更は、Azure AI Foundryに統合されたコンテンツフィルタリングシステムの説明部分を更新したものです。主な変更点は以下の通りです：

1. **モデルの説明の一般化**: コンテンツフィルタリングシステムの説明から「DALL-E画像生成モデル」という特定の名前が削除され、「画像生成モデル」というより一般的な表現に変更されました。この修正により、他の画像生成モデルも含めた広範なアプローチを反映しています。

2. **システムの役割の明確化**: コンテンツフィルタリングの機能が引き続き強調されている一方で、具体的なモデル名を外すことで、Azure AI Foundryのシステムがより柔軟かつ適用範囲広く機能することを示しています。

この更新により、ユーザーはAzure AI Foundryのコンテンツフィルタリングシステムの動作をより広範に理解できるようになり、特定のモデルに固定されることなく、その機能を利用できることが期待されます。

## articles/ai-services/openai/how-to/dall-e.md{#item-ac9616}

<details>
<summary>Diff</summary>
````diff
@@ -1,43 +1,84 @@
 ---
-title: How to use DALL-E models 
+title: How to use image generation models 
 titleSuffix: Azure OpenAI Service
-description: Learn how to generate images with the DALL-E models, and learn about the configuration options that are available.
+description: Learn how to generate and edit images with image models, and learn about the configuration options that are available.
 author: PatrickFarley
 ms.author: pafarley 
 ms.service: azure-ai-openai
 ms.custom: 
 ms.topic: how-to
-ms.date: 02/20/2025
+ms.date: 04/23/2025
 manager: nitinme
 keywords: 
 zone_pivot_groups: 
 # Customer intent: as an engineer or hobbyist, I want to know how to use DALL-E image generation models to their full capability.
 ---
 
-# How to use the DALL-E models
+# How to use Azure OpenAI image generation models
 
-OpenAI's DALL-E models generate images based on user-provided text prompts. This guide demonstrates how to use the DALL-E models and configure their options through REST API calls.
+OpenAI's image generation models render images based on user-provided text prompts and optionally provided images. This guide demonstrates how to use the image generation models and configure their options through REST API calls.
 
 
 ## Prerequisites
 
 - An Azure subscription. You can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?icid=ai-services).
 - An Azure OpenAI resource created in a supported region. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
-- - Deploy a *dall-e-3* model with your Azure OpenAI resource.
+- Deploy a `dall-e-3` or `gpt-image-1` model with your Azure OpenAI resource. For more information on deployments, see [Create a resource and deploy a model with Azure OpenAI](/azure/ai-services/openai/how-to/create-resource).
+    - GPT-image-1 is the newer model and features a number of improvements over DALL-E 3. It's available in limited access: apply for access with [this form](https://aka.ms/oai/gptimage1access).
 
-## Call the Image Generation APIs
+## Call the Image Generation API
 
-The following command shows the most basic way to use DALL-E with code. If this is your first time using these models programmatically, we recommend starting with the [DALL-E quickstart](/azure/ai-services/openai/dall-e-quickstart).
+The following command shows the most basic way to use an image model with code. If this is your first time using these models programmatically, we recommend starting with the [quickstart](/azure/ai-services/openai/dall-e-quickstart).
 
+
+#### [GPT-image-1](#tab/gpt-image-1)
 Send a POST request to:
 
 ```
 https://<your_resource_name>.openai.azure.com/openai/deployments/<your_deployment_name>/images/generations?api-version=<api_version>
 ```
 
-**Replace the following placeholders**:
+
+**URL**:
+
+Replace the following values:
 - `<your_resource_name>` is the name of your Azure OpenAI resource.
-- `<your_deployment_name>` is the name of your DALL-E 3 model deployment.
+- `<your_deployment_name>` is the name of your DALL-E 3 or GPT-image-1 model deployment.
+- `<api_version>` is the version of the API you want to use. For example, `2025-04-01-preview`.
+
+**Required headers**:
+- `Content-Type`: `application/json`
+- `api-key`: `<your_API_key>`
+
+**Body**:
+
+The following is a sample request body. You specify a number of options, defined in later sections.
+
+```json
+{
+    "prompt": "A multi-colored umbrella on the beach, disposable camera",
+    "model": "gpt-image-1",
+    "size": "1024x1024", 
+    "n": 1,
+    "quality": "high"
+}
+```
+
+
+
+#### [DALL-E 3](#tab/dalle-3)
+
+Send a POST request to:
+
+```
+https://<your_resource_name>.openai.azure.com/openai/deployments/<your_deployment_name>/images/generations?api-version=<api_version>
+```
+
+**URL**:
+
+Replace the following values:
+- `<your_resource_name>` is the name of your Azure OpenAI resource.
+- `<your_deployment_name>` is the name of your DALL-E 3 or GPT-image-1 model deployment.
 - `<api_version>` is the version of the API you want to use. For example, `2024-02-01`.
 
 **Required headers**:
@@ -58,9 +99,11 @@ The following is a sample request body. You specify a number of options, defined
 }
 ```
 
-## Output
+---
+
+### Output
 
-The output from a successful image generation API call looks like the following example. The `url` field contains a URL where you can download the generated image. The URL stays active for 24 hours.
+The response from a successful image generation API call looks like the following example. The `url` field contains a URL where you can download the generated image. The URL stays active for 24 hours.
 
 ```json
 { 
@@ -104,51 +147,182 @@ It's also possible that the generated image itself is filtered. In this case, th
 }
 ```
 
-## Write image prompts
+### Write text-to-image prompts
 
-Your image prompts should describe the content you want to see in the image, and the visual style of image.
+Your prompts should describe the content you want to see in the image, and the visual style of image.
 
-When writing prompts, consider that the image generation APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it doesn't generate an image. For more information, see [Content filtering](../concepts/content-filter.md).
+When you write prompts, consider that the Image APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it doesn't generate an image. For more information, see [Content filtering](../concepts/content-filter.md).
 
 > [!TIP]
 > For a thorough look at how you can tweak your text prompts to generate different kinds of images, see the [Image prompt engineering guide](/azure/ai-services/openai/concepts/gpt-4-v-prompt-engineering).
 
 
-## Specify API options
+### Specify API options
+
+The following API body parameters are available for image generation models.
+
+
+#### [GPT-image-1](#tab/gpt-image-1)
+
+
+#### Size
+
+Specify the size of the generated images. Must be one of `1024x1024`, `1024x1536`, or `1536x1024` for GPT-image-1 models. Square images are faster to generate.
+
+
+#### Quality
+
+There are three options for image quality: `low`, `medium`, and `high`.Lower quality images can be generated faster.
+
+The default value is `high`.
 
-The following API body parameters are available for DALL-E image generation.
+#### Number
 
-### Size
+You can generate between one and 10 images in a single API call. The default value is `1`.
+
+#### Response format
+
+The format in which the generated images are returned. Must be either `url` (a URL pointing to the image) or `b64_json` (the base 64-byte code in JSON format). The default is `url`.
+
+#### User ID
+
+Use the *user* parameter to specify a unique identifier for the user making the request. This is useful for tracking and monitoring usage patterns. The value can be any string, such as a user ID or email address.
+
+#### Output format
+
+Use the *output_format* parameter to specify the format of the generated image. Supported formats are `PNG` and `JPEG`. The default is `PNG`.
+
+> [!NOTE]
+> WEBP images are not supported in the Azure OpenAI Service.
+
+#### Compression
+
+Use the *output_compression* parameter to specify the compression level for the generated image. Input an integer between `0` and `100`, where `0` is no compression and `100` is maximum compression. The default is `100`.
+
+
+#### [DALL-E 3](#tab/dalle-3)
+
+<!--
+| Parameter Name   | Description       | Values         |
+|------------------|-------------|--------------------------|
+| Size             | Specifies the size of generated images. Square images generate faster.    | `1024x1024` (default), `1792x1024`, `1024x1792`           |
+| Style            | DALL-E 3 offers two style options. The natural style is more similar to the default style of older models, while the vivid style generates more hyper-real and cinematic images. </br></br>The natural style is useful in cases where DALL-E 3 over-exaggerates or confuses a subject that's meant to be more simple, subdued, or realistic.     | `natural`, `vivid` (default)           |
+| Quality          | Controls image quality. `hd` has finer details and better consistency; `standard` is faster.    | `hd`, `standard` (default) |
+| Number (`n`)     | Must be set to 1 for DALL-E 3. To get multiple images, make parallel requests.        | `1`              |
+| Response format  | Format for the returned images. Default is `url`.   | `url`, `b64_json`|
+-->
+
+#### Size
 
 Specify the size of the generated images. Must be one of `1024x1024`, `1792x1024`, or `1024x1792` for DALL-E 3 models. Square images are faster to generate.
 
-### Style
+#### Style
 
 DALL-E 3 offers two style options: `natural` and `vivid`. The natural style is more similar to the default style of older models, while the vivid style generates more hyper-real and cinematic images.
 
 The natural style is useful in cases where DALL-E 3 over-exaggerates or confuses a subject that's meant to be more simple, subdued, or realistic.
 
 The default value is `vivid`.
 
-### Quality
+#### Quality
 
 There are two options for image quality: `hd` and `standard`. The hd option creates images with finer details and greater consistency across the image. Standard images can be generated faster.
 
 The default value is `standard`.
 
-### Number
+#### Number
 
 With DALL-E 3, you can't generate more than one image in a single API call: the `n` parameter must be set to *1*. If you need to generate multiple images at once, make parallel requests.
 
-### Response format
+#### Response format
 
 The format in which the generated images are returned. Must be one of `url` (a URL pointing to the image) or `b64_json` (the base 64-byte code in JSON format). The default is `url`.
 
+---
+
+## Call the Image Edit API
+
+The Image Edit API allows you to modify existing images based on text prompts you provide. The API call is similar to the image generation API call, but you also need to provide an image URL or base 64-encoded image data.
+
+
+
+#### [GPT-image-1](#tab/gpt-image-1)
+
+Send a POST request to:
+
+```
+https://<your_resource_name>.openai.azure.com/openai/deployments/<your_deployment_name>/images/edits?api-version=<api_version>
+```
+
+
+**URL**:
+
+Replace the following values:
+- `<your_resource_name>` is the name of your Azure OpenAI resource.
+- `<your_deployment_name>` is the name of your DALL-E 3 or GPT-image-1 model deployment.
+- `<api_version>` is the version of the API you want to use. For example, `2025-04-01-preview`.
+
+**Required headers**:
+- `Content-Type`: `application/json`
+- `api-key`: `<your_API_key>`
+
+**Body**:
+
+The following is a sample request body. You specify a number of options, defined in later sections.
+
+```json
+{
+    "image": "<base64_encoded_image>",
+    "prompt": "Add a beach ball in the center.",
+    "model": "gpt-image-1",
+    "size": "1024x1024", 
+    "n": 1,
+    "quality": "high"
+}
+```
+
+### Output
+
+The response from a successful image editing API call looks like the following example. The `url` field contains a URL where you can download the generated image. The URL stays active for 24 hours.
+
+```json
+{ 
+    "created": 1698116662, 
+    "data": [ 
+        { 
+            "url": "<URL_to_generated_image>",
+            "revised_prompt": "<prompt_that_was_used>" 
+        }
+    ]
+} 
+```
+
+### Specify API options
+
+The following API body parameters are available for image editing models, in addition to the ones available for image generation models.
+
+### Image
+
+The *image* value indicates the image file you want to edit. It can be either a URL string to an image file, or base 64-encoded image data.
+
+
+#### Mask
+
+The *mask* parameter is the same type as the main *image* input parameter. It defines the area of the image that you want the model to change, using fully transparent pixels (alpha of zero) in those areas. The mask can be a URL or base 64-encoded image data. It must be a PNG file and have the same dimensions as the image.
+
+
+#### [DALL-E 3](#tab/dalle-3)
+
+DALL-E models don't support the Image Edit API.
+
+---
+
 ## Related content
 
 * [What is Azure OpenAI Service?](../overview.md)
 * [Quickstart: Generate images with Azure OpenAI Service](../dall-e-quickstart.md)
-* [Image generation API reference](/azure/ai-services/openai/reference#image-generation)
+* [Image API reference](/azure/ai-services/openai/reference#image-generation)
+* [Image API (preview) reference](/azure/ai-services/openai/reference-preview)
 
 
 <!-- OAI HT guide https://platform.openai.com/docs/guides/images/usage
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "画像生成モデルに関する内容の大幅更新"
}
```

### Explanation
この変更は、Azure OpenAIにおける画像生成モデルに関するガイドの内容を大幅に更新したものです。主な変更点は以下の通りです：

1. **タイトルと説明の更新**: タイトルが「DALL-Eモデルの使用方法」から「Azure OpenAI画像生成モデルの使用方法」に変更され、説明文も画像生成と編集に関するより包括的なものへと更新されました。これにより、新しいモデル群に対する情報も含まれるようになりました。

2. **新しいモデルの追加**: DALL-E 3モデルだけでなく、GPT-image-1モデルが追加され、その特徴と利用方法が説明されています。この新しいモデルは、DALL-E 3に比べて改善点が多く、限定アクセスが必要であることも明記されています。

3. **APIの使い方の具体化**: 画像生成APIの呼び出し方法が具体的に示され、リクエストのサンプルや必須のヘッダー情報が詳しく説明されています。特に、APIを使った画像生成や編集に関するセクションが充実しています。

4. **オプションの参照の拡充**: APIの仕様に関して、サイズ、質、レスポンス形式、圧縮レベルなど、多くの新たなパラメータや情報が追加され、ユーザーがより詳細にAPIを利用しやすくなりました。

5. **編集APIの追加**: 新たに「画像編集API」が導入され、既存の画像を基にした編集方法が明確に示されています。このセクションでは、編集に必要な要素やリクエストボディの例も紹介されています。

このような改訂により、ユーザーはAzure OpenAIの画像生成機能をより深く理解し、活用するための具体的な手引きを得られるようになっています。

## articles/ai-services/openai/how-to/evaluations.md{#item-dfaa1c}

<details>
<summary>Diff</summary>
````diff
@@ -305,12 +305,14 @@ BLEU (BiLingual Evaluation Understudy) score is commonly used in natural languag
 
 ROUGE (Recall-Oriented Understudy for Gisting Evaluation) is a set of metrics used to evaluate automatic summarization and machine translation. It measures the overlap between generated text and reference summaries. ROUGE focuses on recall-oriented measures to assess how well the generated text covers the reference text.
 The ROUGE score provides various metrics, including:
-•	ROUGE-1: Overlap of unigrams (single words) between generated and reference text.
-•	ROUGE-2: Overlap of bigrams (two consecutive words) between generated and reference text.
-•	ROUGE-3: Overlap of trigrams (three consecutive words) between generated and reference text.
-•	ROUGE-4: Overlap of four-grams (four consecutive words) between generated and reference text.
-•	ROUGE-5: Overlap of five-grams (five consecutive words) between generated and reference text.
-•	ROUGE-L: Overlap of L-grams (L consecutive words) between generated and reference text.
+
+- ROUGE-1: Overlap of unigrams (single words) between generated and reference text.
+- ROUGE-2: Overlap of bigrams (two consecutive words) between generated and reference text.
+- ROUGE-3: Overlap of trigrams (three consecutive words) between generated and reference text.
+- ROUGE-4: Overlap of four-grams (four consecutive words) between generated and reference text.
+- ROUGE-5: Overlap of five-grams (five consecutive words) between generated and reference text.
+- ROUGE-L: Overlap of L-grams (L consecutive words) between generated and reference text.
+
 Text summarization and document comparison are among optimal use cases for ROUGE, particularly in scenarios where text coherence and relevance are critical.
 
 Cosine similarity measures how closely two text embeddings—such as model outputs and reference texts—align in meaning, helping assess the semantic similarity between them. Same as other model-based evaluators, you need to provide a model deployment using for evaluation. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ROUGEメトリクスの説明の改善"
}
```

### Explanation
この変更は、自然言語処理におけるROUGEメトリクスに関する説明を改善したものです。主な変更点は以下の通りです：

1. **フォーマットの調整**: ROUGEメトリクスの各項目について記述されているリストが、箇条書き形式に改められました。これにより、閲覧者が情報をより視覚的に把握しやすくなります。

2. **メトリクスの明確化**: ROUGE-1からROUGE-Lまでの各スコアについて、元のテキストと生成されたテキストの間のオーバーラップを詳しく説明しています。この変更は、メトリクスの目的や使用方法を理解するために役立つものです。

3. **使用例の追加**: ROUGEメトリクスの最適な利用ケースとして、テキスト要約や文書比較が示され、テキストの一貫性や関連性が重要なシナリオにおける有用性が強調されています。

これらの変更により、ROUGEメトリクスの効果的な使用の理解が進み、自然言語生成や評価におけるその重要性が明確になっています。全体的に、説明がより分かりやすくなり、ユーザーがこの評価指標をどのように活用するかを把握しやすくなりました。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -49,16 +49,18 @@ Azure OpenAI `o-series` models are designed to tackle reasoning and problem-solv
 | Responses API | ✅ | ✅  | - | - | - | - |
 | Functions/Tools | ✅ | ✅ | ✅  | ✅  |  - | - |
 | Parallel Tool Calls | - | - | -  | -  |  - | - |
-| `max_completion_tokens`<sup>*</sup> | ✅ | ✅ |✅ |✅ |✅ | ✅ |
-| System Messages<sup>**</sup> | ✅ | ✅ | ✅ | ✅ | - | - |
-| [Reasoning summary](#reasoning-summary) <sup>***</sup> | ✅ | ✅ | -  | -  |  - | - |
-| Streaming | ✅ | ✅ | ✅ | - | - | - |
+| `max_completion_tokens` <sup>1</sup> | ✅ | ✅ |✅ |✅ |✅ | ✅ |
+| System Messages <sup>2</sup> | ✅ | ✅ | ✅ | ✅ | - | - |
+| [Reasoning summary](#reasoning-summary) <sup>3</sup> | ✅ | ✅ | -  | -  |  - | - |
+| Streaming <sup>4</sup>  | ✅ | ✅| ✅ | - | - | - |
 
-<sup>*</sup> Reasoning models will only work with the `max_completion_tokens` parameter. <br><br>
+<sup>1</sup> Reasoning models will only work with the `max_completion_tokens` parameter. <br><br>
 
-<sup>**</sup>The latest o<sup>&#42;</sup> series model support system messages to make migration easier. When you use a system message with `o4-mini`, `o3`, `o3-mini`, and `o1` it will be treated as a developer message. You should not use both a developer message and a system message in the same API request.
+<sup>2</sup> The latest o<sup>&#42;</sup> series model support system messages to make migration easier. When you use a system message with `o4-mini`, `o3`, `o3-mini`, and `o1` it will be treated as a developer message. You should not use both a developer message and a system message in the same API request.
 
-<sup>***</sup> Access to the chain-of-thought reasoning summary is limited access only for `o4-mini`. 
+<sup>3</sup> Access to the chain-of-thought reasoning summary is limited access only for `o4-mini`.
+
+<sup>4</sup> Streaming for `o3` is currently only supported for Enterprise subscriptions.
 
 ### Not Supported
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル機能に関する詳細情報の明確化"
}
```

### Explanation
この変更では、Azure OpenAIの`o-series`モデルに関する機能の説明が更新され、いくつかの重要な点が明確化されました。主な変更点は以下の通りです：

1. **脚注の番号付けの変更**: 各機能に関連する脚注が番号で識別されるように変更され、より視認性が高くなりました。これにより、ユーザーは特定の機能に関連する説明を簡単に参照できるようになりました。

2. **ストリーミング機能の追記**: ストリーミング機能に関する情報が追加され、特に`o3`モデルに関しては、現時点でEnterpriseサブスクリプションのみがサポートされていることが明示されました。これは利用者にとって重要な情報です。

3. **詳細な説明の追加**: `max_completion_tokens`およびシステムメッセージに関する説明が改善され、モデルがこれらのパラメータとどのように連携するかが明確になりました。特にシステムメッセージと開発者メッセージの併用に関する注意事項が強調されています。

これらの更新により、ユーザーは`o-series`モデルの使用に関連する機能をより理解しやすくなるとともに、特定の制限や注意点を考慮に入れた上で適切に利用できるようになります。全体として、文書の可読性と理解のしやすさが向上しています。

## articles/ai-services/openai/how-to/responses.md{#item-b9757d}

<details>
<summary>Diff</summary>
````diff
@@ -46,6 +46,7 @@ The responses API is currently available in the following regions:
 - `gpt-4.1` (Version: `2025-04-14`)
 - `gpt-4.1-nano` (Version: `2025-04-14`)
 - `gpt-4.1-mini` (Version: `2025-04-14`)
+- `gpt-image-1` (Version: `2025-04-15`)
 - `o3` (Version: `2025-04-16`)
 - `o4-mini` (Version: `2025-04-16`)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいモデルの追加情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIのレスポンスAPIに関する文書の一部を更新し、新しいモデルの情報を反映させるものです。具体的には、次の点が変更されました：

1. **新しいモデルの追加**: `gpt-image-1`という新しいモデルが、対応するバージョン情報とともにリストに追加されました。このモデルはバージョン`2025-04-15`として記載されています。

2. **情報の更新**: これにより、ユーザーは利用可能なAPIモデルの最新情報を得ることができ、異なるモデルのバージョンや地域に関する理解が深まります。

この更新は、レスポンスAPIを利用する開発者やエンジニアにとって重要であり、特に新しいモデルを活用したいユーザーにとって、必要な情報が提供されることで利便性が向上します。全体的に、ドキュメントが最新の状況を反映するようになり、ユーザーに有益な情報を提供しています。

## articles/ai-services/openai/includes/api-versions/latest-inference-preview.md{#item-24bf0f}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Latest preview data plane inference documentation generated from Op
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 03/24/2025
+ms.date: 04/23/2025
 ---
 
 ## Completions - Create
@@ -1192,7 +1192,7 @@ Status Code: 200
 POST https://{endpoint}/openai/deployments/{deployment-id}/images/generations?api-version=2025-03-01-preview
 ```
 
-Generates a batch of images from a text caption on a given DALLE model deployment
+Generates a batch of images from a text caption on a given DALL-E or GPT-image-1 model deployment
 
 ### URI Parameters
 
@@ -1219,11 +1219,13 @@ Generates a batch of images from a text caption on a given DALLE model deploymen
 |------|------|-------------|----------|---------|
 | n | integer | The number of images to generate. | No | 1 |
 | prompt | string | A text description of the desired image(s). The maximum length is 4000 characters. | Yes |  |
-| quality | [imageQuality](#imagequality) | The quality of the image that will be generated. | No | standard |
+| quality | [imageQuality](#imagequality) | The quality of the image that will be generated. | No | standard (for DALL-E)</br>high (for GPT-image-1) |
 | response_format | [imagesResponseFormat](#imagesresponseformat) | The format in which the generated images are returned. | No | url |
 | size | [imageSize](#imagesize) | The size of the generated images. | No | 1024x1024 |
 | style | [imageStyle](#imagestyle) | The style of the generated images. | No | vivid |
 | user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse. | No |  |
+| output_format | string | The format in which the generated images are returned. GPT-image-1 models only. | No | PNG |
+| output_compression | integer | The compression level (on a scale of 0-100) of the generated images. GPT-image-1 | No | 0 |
 
 ### Responses
 
@@ -1243,14 +1245,12 @@ Generates a batch of images from a text caption on a given DALLE model deploymen
 |:---|:---|:---|
 |application/json | [dalleErrorResponse](#dalleerrorresponse) | |
 
-### Examples
-
 ### Example
 
 Creates images given a prompt.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/images/generations?api-version=2025-03-01-preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/images/generations?api-version=2025-04-01-preview
 
 {
  "prompt": "In the style of WordArt, Microsoft Clippy wearing a cowboy hat.",
@@ -1264,6 +1264,9 @@ POST https://{endpoint}/openai/deployments/{deployment-id}/images/generations?ap
 **Responses**:
 Status Code: 200
 
+> [!NOTE]
+> The GPT-image-1 model doesn't return content filtering annotations.
+
 ```json
 {
   "body": {
@@ -1322,6 +1325,112 @@ Status Code: 200
 }
 ```
 
+
+## Image generations - Edit
+
+```HTTP
+POST https://{endpoint}/openai/deployments/{deployment-id}/images/edits?api-version=2025-04-01-preview
+```
+
+Generates an image based on an input image and text prompt instructions. Requires a GPT-image-1 model deployment
+
+### URI Parameters
+
+| Name | In | Required | Type | Description |
+|------|------|----------|------|-----------|
+| endpoint | path | Yes | string<br>url | Supported Azure OpenAI endpoints (protocol and hostname, for example: `https://aoairesource.openai.azure.com`. Replace "aoairesource" with your Azure OpenAI resource name). https://{your-resource-name}.openai.azure.com |
+| deployment-id | path | Yes | string |  |
+| api-version | query | Yes | string |  |
+
+### Request Header
+
+**Use either token based authentication or API key. Authenticating with token based authentication is recommended and more secure.**
+
+| Name | Required | Type | Description |
+| --- | --- | --- | --- |
+| Authorization | True | string | **Example:** `Authorization: Bearer {Azure_OpenAI_Auth_Token}`<br><br>**To generate an auth token using Azure CLI: `az account get-access-token --resource https://cognitiveservices.azure.com`**<br><br>Type: oauth2<br>Authorization Url: `https://login.microsoftonline.com/common/oauth2/v2.0/authorize`<br>scope: `https://cognitiveservices.azure.com/.default`|
+| api-key | True | string | Provide Azure OpenAI API key here |
+
+### Request Body
+
+**Content-Type**: application/json
+
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| image | file | The input image to edit. Must be a valid image URL or base64-encoded image. tbd | Yes |  |
+| n | integer | The number of images to generate. | No | 1 |
+| prompt | string | A text description of how the input image should be edited. The maximum length is 4000 characters. | Yes |  |
+| mask | file | A mask image to define the area of the input image that the model should edit, using fully transparent pixels (alpha of zero) in those areas. Must be a valid image URL or base64-encoded image. | No |  |
+| quality | string | The quality of the image that will be generated. Values are 'low', 'medium', 'high' | No | high |
+| response_format | [imagesResponseFormat](#imagesresponseformat) | The format in which the generated images are returned. | No | url |
+| size | [imageSize](#imagesize) | The size of the generated images. | No | 1024x1024 |
+| style | [imageStyle](#imagestyle) | The style of the generated images. | No | vivid |
+| user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse. | No |  |
+| output_format | [imageOutputFormat](#imageoutputformat) | The format in which the generated images are returned. | No | PNG |
+| output_compression | integer | The compression level (on a scale of 0-100) of the generated images. GPT-image-1 | No | 0 |
+
+
+### Responses
+
+**Status Code:** 200
+
+**Description**: Ok 
+
+|**Content-Type**|**Type**|**Description**|
+|:---|:---|:---|
+|application/json | [generateImagesResponse](#generateimagesresponse) | |
+
+**Status Code:** default
+
+**Description**: An error occurred. 
+
+|**Content-Type**|**Type**|**Description**|
+|:---|:---|:---|
+|application/json | [dalleErrorResponse](#dalleerrorresponse) | |
+
+### Example
+
+Creates images given an input image and text instructions.
+
+```HTTP
+POST https://{endpoint}/openai/deployments/{deployment-id}/images/edits?api-version=2025-04-01-preview
+
+{
+  "image": "<base64_encoded_image>",
+  "prompt": "Add a beach ball in the center.",
+  "model": "gpt-image-1",
+  "size": "1024x1024", 
+  "n": 1,
+  "quality": "high"
+}
+
+```
+
+**Responses**:
+Status Code: 200
+
+> [!NOTE]
+> The GPT-image-1 model doesn't return content filtering annotations.
+
+```json
+{
+  "body": {
+    "created": 1698342300,
+    "data": [
+      {
+        "b64_json": "<base64_encoded_image>",
+        "revised_prompt": "A vivid, natural representation of Microsoft Clippy wearing a cowboy hat.",
+      }],
+    "usage": 
+      {
+        "input_tokens": 557,
+        "output_tokens": 1000,
+      }
+    
+  }
+}
+```
+
 ## List - Assistants
 
 ```HTTP
@@ -6012,6 +6121,17 @@ Speech request.
 | speed | number | The speed of the synthesized audio. Select a value from `0.25` to `4.0`. `1.0` is the default. | No | 1.0 |
 | voice | enum | The voice to use for speech synthesis.<br>Possible values: `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer` | Yes |  |
 
+### imageOutputFormat
+
+The requested output format for the generated image.
+
+| Property | Value |
+|----------|-------|
+| **Description** | The requested output format for the generated image. |
+| **Type** | string |
+| **Default** | PNG |
+| **Values** | `PNG`<br>`JPEG` |
+
 ### imageQuality
 
 The quality of the image that will be generated.
@@ -6020,8 +6140,8 @@ The quality of the image that will be generated.
 |----------|-------|
 | **Description** | The quality of the image that will be generated. |
 | **Type** | string |
-| **Default** | standard |
-| **Values** | `standard`<br>`hd` |
+| **Default** | standard (for DALL-E)<br>high (for GPT-image-1) |
+| **Values** | `standard`, `hd` (for DALL-E)<br>`low`, `medium`, `high` (for GPT-image-1) |
 
 ### imagesResponseFormat
 
@@ -6062,11 +6182,32 @@ The style of the generated images.
 |------|------|-------------|----------|---------|
 | n | integer | The number of images to generate. | No | 1 |
 | prompt | string | A text description of the desired image(s). The maximum length is 4000 characters. | Yes |  |
-| quality | [imageQuality](#imagequality) | The quality of the image that will be generated. | No | standard |
+| quality | [imageQuality](#imagequality) | The quality of the image that will be generated. | No | standard (for DALL-E)</br>high (for GPT-image-1) |
 | response_format | [imagesResponseFormat](#imagesresponseformat) | The format in which the generated images are returned. | No | url |
 | size | [imageSize](#imagesize) | The size of the generated images. | No | 1024x1024 |
 | style | [imageStyle](#imagestyle) | The style of the generated images. | No | vivid |
 | user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse. | No |  |
+| output_format | string | The format in which the generated images are returned. GPT-image-1 models only. | No | PNG |
+| output_compression | integer | The compression level (on a scale of 0-100) of the generated images. GPT-image-1 | No | 0 |
+
+### imageEditsRequest
+
+
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| image | file | The input image to edit. Must be a valid image URL or base64-encoded image. tbd | Yes |  |
+| n | integer | The number of images to generate. | No | 1 |
+| prompt | string | A text description of how the input image should be edited. The maximum length is 4000 characters. | Yes |  |
+| mask | file | A mask image to define the area of the input image that the model should edit, using fully transparent pixels (alpha of zero) in those areas. Must be a valid image URL or base64-encoded image. | No |  |
+| quality | string | The quality of the image that will be generated. Values are 'low', 'medium', 'high' | No | high |
+| response_format | [imagesResponseFormat](#imagesresponseformat) | The format in which the generated images are returned. | No | url |
+| size | [imageSize](#imagesize) | The size of the generated images. | No | 1024x1024 |
+| style | [imageStyle](#imagestyle) | The style of the generated images. | No | vivid |
+| user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse. | No |  |
+| output_format | [imageOutputFormat](#imageoutputformat) | The format in which the generated images are returned. | No | PNG |
+| output_compression | integer | The compression level (on a scale of 0-100) of the generated images. GPT-image-1 | No | 0 |
+
+
 
 ### generateImagesResponse
 
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "GPT-image-1モデルの新機能とAPIエンドポイントの更新"
}
```

### Explanation
この変更は、Azure OpenAIのインファレンスプレビューに関する文書を大幅に更新し、新しい機能やAPIエンドポイントに関する詳細を追加したものです。主な変更点は以下の通りです：

1. **新しいモデルの追加**: `GPT-image-1`モデルが登場し、これに関連する新しいエンドポイントやパラメータが文書に追加されました。このモデルは、テキストのプロンプトに基づいた画像生成を提供します。

2. **エンドポイントの更新**: 画像生成のためのAPIエンドポイントが更新され、バージョン`2025-04-01-preview`が使用されています。これにより、最新の機能を利用するための正確なリクエストURLが提供されています。

3. **新しいリクエストパラメータの導入**: `output_format`や`output_compression`など、新しいURIパラメータが追加され、特にGPT-image-1モデルに特有の設定が可能になっています。また、`DALL-E`モデルと`GPT-image-1`モデルの品質設定も明確にされました。

4. **画像編集機能の紹介**: 新たに、入力画像を基にした画像生成や編集機能が追加され、ユーザーが具体的な指示に基づいて画像を編集できるようになりました。これにより、ユーザーのニーズに合わせた柔軟な画像生成が可能になります。

これらの更新により、ユーザーは新たに利用可能となった機能をフル活用することができ、特に画像生成に関心のある利用者にとっての利便性が大幅に向上します。全体的にこの修正は、ユーザーに最新の情報と機能を提供する重要な更新といえます。

## articles/ai-services/openai/includes/dall-e-dotnet.md{#item-755f0a}

<details>
<summary>Diff</summary>
````diff
@@ -125,7 +125,7 @@ The URL of the generated image is printed to the console.
 ```
 
 > [!NOTE]
-> The image generation APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it won't return a generated image. For more information, see the [content filter](../concepts/content-filter.md) article.
+> The Image APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it won't return a generated image. For more information, see the [content filter](../concepts/content-filter.md) article.
 
 ## Clean up resources
 
@@ -136,5 +136,5 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 
 ## Next steps
 
-* Explore the image generation APIs in more depth with the [DALL-E how-to guide](../how-to/dall-e.md).
+* Explore the Image APIs in more depth with the [Image API how-to guide](../how-to/dall-e.md).
 * For more examples check out the [Azure OpenAI Samples GitHub repository](https://github.com/Azure/openai-samples).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の統一と更新"
}
```

### Explanation
この変更は、DALL-E に関連するドキュメントの文言を一部見直し、用語の統一を図ったものです。主な更新点は以下のとおりです：

1. **用語の変更**: 「画像生成API」を「Image APIs」と翻訳し、全体的に英語の用語を一貫して使用するようにしています。これにより、読者が英語の用語と日本語の説明を混同しないよう配慮されています。

2. **注意書きの修正**: コンテンツモデレーションフィルターに関する説明を簡略化し、情報の明確さを向上させるための編集が行われました。具体的には、ユーザーのプロンプトが有害な内容と認識された場合に生成された画像が返されないことについて、注意喚起がよりスムーズに表現されています。

3. **次のステップの更新**: 次のステップに関連するリンクの表現も更新され、より広範な「Image APIs」に関連する情報を提供する方向に修正されています。これにより、読者がDALL-Eだけでなく、他の画像APIにも興味を持つことが期待されます。

これらの更新は、情報の一貫性と明瞭さを向上させ、読者がより良い体験ができるようにすることを目的としています。全体として、文書の品質が向上したことを示す重要な改善です。

## articles/ai-services/openai/includes/dall-e-go.md{#item-132707}

<details>
<summary>Diff</summary>
````diff
@@ -248,7 +248,7 @@ Image generated, HEAD request on URL returned 200
 Image URL: <SAS URL>
 ```
 > [!NOTE]
-> The image generation APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it won't return a generated image. For more information, see the [content filter](../concepts/content-filter.md) article.
+> The Image APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it won't return a generated image. For more information, see the [content filter](../concepts/content-filter.md) article.
 
 ## Clean up resources
 
@@ -259,5 +259,5 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 
 ## Next steps
 
-* Explore the image generation APIs in more depth with the [DALL-E how-to guide](../how-to/dall-e.md).
+* Explore the Image APIs in more depth with the [Image API how-to guide](../how-to/dall-e.md).
 * For more examples check out the [Azure OpenAI Samples GitHub repository](https://github.com/Azure/openai-samples).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の統一と更新"
}
```

### Explanation
この変更は、DALL-Eに関連するドキュメントにおいて、用語の一貫性を高めるために行われた修正です。具体的な変更内容は以下の通りです：

1. **用語の統一**: 「画像生成API」という表現が「Image APIs」に統一され、英語が統一的に使用されるようになっています。これにより、ドキュメント全体の一貫性が保たれ、読者が誤解しにくくされています。

2. **コンテンツモデレーションフィルターについての注意書きの修正**: コンテンツモデレーションフィルターに関する記述が若干変更され、より明瞭に説明されるようになりました。具体的には、ユーザーのプロンプトが有害な内容と認識された場合には生成された画像が返されないことが強調されています。

3. **次のステップの文言修正**: 次のステップセクションにおいて、リンクの表現が更新され、DALL-Eに特化した表現ではなく「Image APIs」というより広範な表現が使われています。これにより、より多くのAPIに関心を持つよう誘導されています。

これらの変更は、読者にとって文書がより明確で使いやすくなるよう努めたものであり、全体的な品質向上を示しています。

## articles/ai-services/openai/includes/dall-e-java.md{#item-373f89}

<details>
<summary>Diff</summary>
````diff
@@ -263,7 +263,7 @@ Completed getImages.
 ```
 
 > [!NOTE]
-> The image generation APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it won't return a generated image. For more information, see the [content filter](../concepts/content-filter.md) article.
+> The Image APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it won't return a generated image. For more information, see the [content filter](../concepts/content-filter.md) article.
 
 
 ## Clean up resources
@@ -275,5 +275,5 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 
 ## Next steps
 
-* Explore the image generation APIs in more depth with the [DALL-E how-to guide](../how-to/dall-e.md).
+* Explore the Image APIs in more depth with the [Image API how-to guide](../how-to/dall-e.md).
 * For more examples, check out the [Azure OpenAI Samples GitHub repository](https://github.com/Azure-Samples/openai)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の統一と更新"
}
```

### Explanation
この変更は、DALL-Eに関するJava用のドキュメントにおいて、用語を統一し、情報を明確にするために行われました。具体的な変更内容は以下の通りです：

1. **用語の変更**: 「画像生成API」という表現が「Image APIs」に統一されました。これにより、ドキュメント内での用語の整合性が保たれ、読者が理解しやすくなっています。

2. **コンテンツモデレーションフィルターに関する注意書きの修正**: 注意書きの内容が修正され、フィルターが有害なコンテンツとして認識した場合には生成された画像が返されないことが明確に示されています。これにより、ユーザーがこの機能の挙動をより理解しやすくなります。

3. **次のステップの文言修正**: 次のステップセクションにおいて、DALL-Eに関する文言も「Image APIs」に変更されています。これにより、読者はDALL-E以外の画像APIにも関心を持つよう促されています。

このような修正は、ドキュメントの情報の明瞭性と一貫性を向上させることを目的としており、読者にとっての利便性を高める結果となっています。全体的に、重要な改善を示す変更です。

## articles/ai-services/openai/includes/dall-e-javascript.md{#item-6cffcf}

<details>
<summary>Diff</summary>
````diff
@@ -202,7 +202,7 @@ Image generation result URL: <SAS URL>
 ```
 
 > [!NOTE]
-> The image generation APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it won't return a generated image. For more information, see the [content filter](../concepts/content-filter.md) article.
+> The Image APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it won't return a generated image. For more information, see the [content filter](../concepts/content-filter.md) article.
 
 ## Clean up resources
 
@@ -213,5 +213,5 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 
 ## Next steps
 
-* Explore the image generation APIs in more depth with the [DALL-E how-to guide](../how-to/dall-e.md).
+* Explore the Image APIs in more depth with the [Image API how-to guide](../how-to/dall-e.md).
 * For more examples check out the [Azure OpenAI Samples GitHub repository](https://github.com/Azure/openai-samples).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の統一と更新"
}
```

### Explanation
この変更は、DALL-Eに関するJavaScript用のドキュメントにおいて、用語の統一と内容の明確化を目的とした修正です。具体的な変更点は以下の通りです：

1. **用語の統一**: 「画像生成API」という表現が「Image APIs」に変更され、用語が統一されました。この変更により、ドキュメント全体が一貫性を持ち、読者が内容を理解しやすくなっています。

2. **コンテンツモデレーションフィルターの説明の修正**: 注意書きの内容が若干変更され、フィルターが有害な内容と判断した場合には生成された画像が返されないことが強調されています。このことは、ユーザーがフィルターの動作をより明確に理解できるようにするためのものです。

3. **次のステップの文言更新**: 次のステップセクションにおいて、「DALL-Eハウツーガイド」という表現が「Image APIハウツーガイド」に改められ、より広範囲な対象を示しています。これにより、ユーザーがDALL-E以外の画像APIにも興味を持つよう促されています。

これらの修正は、情報の明確性を向上させ、ドキュメント全体の品質を高めるための重要な変更となっています。読者にとってより使いやすい内容にするための取り組みが反映されています。

## articles/ai-services/openai/includes/dall-e-powershell.md{#item-97878b}

<details>
<summary>Diff</summary>
````diff
@@ -106,7 +106,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 PowerShell requests the image from Azure OpenAI and stores the output image in the _generated_image.png_ file in your specified directory. For convenience, the full path for the file is returned at the end of the script.
 
-The image generation APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it doesn't generate an image. For more information, see [Content filtering](../concepts/content-filter.md).
+The Image APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it doesn't generate an image. For more information, see [Content filtering](../concepts/content-filter.md).
 
 ## Clean up resources
 
@@ -117,5 +117,5 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 
 ## Next steps
 
-* Explore the image generation APIs in more depth with the [DALL-E how-to guide](../how-to/dall-e.md).
+* Explore the Image APIs in more depth with the [Image API how-to guide](../how-to/dall-e.md).
 - Try examples in the [Azure OpenAI Samples GitHub repository](https://github.com/Azure/openai-samples).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の統一と更新"
}
```

### Explanation
このコードの変更は、DALL-Eに関するPowerShell用のドキュメントにおける用語の統一及び内容の明確化を目的としたものです。主な変更点は以下の通りです：

1. **用語の変更**: 「画像生成API」という表現が「Image APIs」に統一され、用語が一貫して使用されるようになりました。これにより、読者はドキュメント全体を通じて同じ用語を使用することで混乱を避けることができます。

2. **コンテンツモデレーションフィルターの説明の修正**: フィルターに関する説明が更新され、フィルターが有害なコンテンツとして認識した場合には画像が生成されないことが明確にされています。これにより、ユーザーはフィルターの動作をより理解しやすくなります。

3. **次のステップの文言修正**: 次のステップセクション内の言葉が「DALL-Eハウツーガイド」から「Image APIハウツーガイド」に変更され、より重要な情報と幅広い関連性を示すようになっています。これにより、読者がDALL-E以外の画像APIにも関心を持つきっかけを提供しています。

これらの変更は、ドキュメント全体の品質を向上させ、読者に対して情報の明確性と一貫性を提供するための重要な取り組みです。

## articles/ai-services/openai/includes/dall-e-python.md{#item-c91824}

<details>
<summary>Diff</summary>
````diff
@@ -120,7 +120,7 @@ Wait a few moments to get the response.
 
 Azure OpenAI stores the output image in the _generated_image.png_ file in your specified directory. The script also displays the image in your default image viewer.
 
-The image generation APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it doesn't generate an image. For more information, see [Content filtering](../concepts/content-filter.md).
+The Image APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it doesn't generate an image. For more information, see [Content filtering](../concepts/content-filter.md).
 
 ## Clean up resources
 
@@ -131,6 +131,6 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 
 ## Next steps
 
-* Explore the image generation APIs in more depth with the [DALL-E how-to guide](../how-to/dall-e.md).
+* Explore the Image APIs in more depth with the [Image API how-to guide](../how-to/dall-e.md).
 * Try examples in the [Azure OpenAI Samples GitHub repository](https://github.com/Azure/openai-samples).
 * See the [API reference](../reference.md#image-generation)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の統一と説明の更新"
}
```

### Explanation
この変更は、DALL-Eに関するPython用のドキュメントにおける用語の統一および情報の明確化を目指したものです。変更点は次のようになります：

1. **用語の統一**: 「画像生成API」という表現が「Image APIs」に改められ、用語が統一されました。この改訂により、ドキュメント内の一貫性が向上し、利用者にとって理解しやすい内容となっています。

2. **コンテンツモデレーションフィルターの説明の更新**: フィルターに関する文言が若干変更され、フィルターが有害なコンテンツとして認識した際に画像を生成しない旨が記載されています。この明確化によって、ユーザーはフィルターの動作についてより理解しやすくなります。

3. **次のステップの文言修正**: 次のステップセクションでは、ガイドのタイトルが「DALL-Eハウツーガイド」から「Image APIハウツーガイド」へ変更され、単一のAPIからより広範な対象へと視野が広がりました。これにより、読者がDALL-E以外の画像APIの利用にもつなげられるようになっています。

これらの変更は、情報の一貫性を持たせ、読者の理解を促進するために行われたもので、全体的なドキュメントの質を向上させることに寄与しています。

## articles/ai-services/openai/includes/dall-e-rest.md{#item-4bac64}

<details>
<summary>Diff</summary>
````diff
@@ -99,7 +99,7 @@ The output from a successful image generation API call looks like the following
 } 
 ```
 
-The image generation APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it doesn't generate an image. For more information, see [Content filtering](../concepts/content-filter.md). For examples of error responses, see the [DALL-E how-to guide](../how-to/dall-e.md).
+The Image APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it doesn't generate an image. For more information, see [Content filtering](../concepts/content-filter.md). For examples of error responses, see the [DALL-E how-to guide](../how-to/dall-e.md).
 
 The system returns an operation status of `Failed` and the `error.code` value in the message is set to `contentFilter`. Here's an example:
 
@@ -137,6 +137,6 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 
 ## Next steps
 
-* Explore the image generation APIs in more depth with the [DALL-E how-to guide](../how-to/dall-e.md).
+* Explore the Image APIs in more depth with the [Image API how-to guide](../how-to/dall-e.md).
 * Try examples in the [Azure OpenAI Samples GitHub repository](https://github.com/Azure/openai-samples).
 * See the [API reference](../reference.md#image-generation)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の統一と情報の明確化"
}
```

### Explanation
この変更は、DALL-Eに関するREST API用のドキュメントにおける用語の統一と内容の明確化を図るものです。変更点の概要は以下の通りです：

1. **用語の統一**: 「画像生成API」という表現が「Image APIs」に統一され、用語の整合性が強化されました。これにより、ドキュメント全体での表現が一貫しており、読者にとって理解が容易になります。

2. **コンテンツモデレーションフィルターの説明の更新**: フィルターに関する文言が若干改善され、フィルターが有害なコンテンツを認識した場合に画像を生成しないことが明示されています。これにより、読者がフィルターの機能をより正確に理解できるようになります。

3. **次のステップの文言修正**: 次のステップセクションにおいて、ガイドのタイトルが「DALL-Eハウツーガイド」から「Image APIハウツーガイド」に変更され、読者がDALL-E以外の画像APIにも関心を持つよう促されています。

これらの変更は、文書の品質向上と情報の一貫性を目的としており、ドキュメントを利用する読者にとっての使いやすさを向上させる効果があります。

## articles/ai-services/openai/includes/dall-e-studio.md{#item-439729}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ On the model's page, select **Open in playground**.
 Start exploring Azure OpenAI capabilities with a no-code approach through the **Images playground**. Enter your image prompt into the text box and select **Generate**. When the AI-generated image is ready, it appears on the page.
 
 > [!NOTE]
-> The image generation APIs come with a content moderation filter. If Azure OpenAI recognizes your prompt as harmful content, it doesn't return a generated image. For more information, see [Content filtering](../concepts/content-filter.md).
+> The Image APIs come with a content moderation filter. If Azure OpenAI recognizes your prompt as harmful content, it doesn't return a generated image. For more information, see [Content filtering](../concepts/content-filter.md).
 
 In the **Images playground**, you can also view Python and cURL code samples, which are prefilled according to your settings. Select **View code** near the top of the page. You can use this code to write an application that completes the same task.
 
@@ -44,6 +44,6 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 
 ## Next steps
 
-* Explore the image generation APIs in more depth with the [DALL-E how-to guide](../how-to/dall-e.md).
+* Explore the Image APIs in more depth with the [Image API how-to guide](../how-to/dall-e.md).
 * Try examples in the [Azure OpenAI Samples GitHub repository](https://github.com/Azure/openai-samples).
 * See the [API reference](../reference.md#image-generation)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の統一と情報の明確化"
}
```

### Explanation
この変更は、DALL-E Studioに関するドキュメントの一部で、用語の統一と情報の明確化を目的としています。以下は変更の要点です：

1. **用語の統一**: 「画像生成API」という表現が「Image APIs」に変更され、用語の一貫性が強化されました。この変更により、参照する文書内での用語が統一され、読者の理解が促進されます。

2. **コンテンツモデレーションフィルターの説明の改善**: フィルターに関する文が改訂され、Azure OpenAIが有害なコンテンツと認識した場合に画像が生成されないことが明確に示されています。この情報の明確化により、ユーザーがフィルターの機能を理解しやすくなります。

3. **次のステップの文言修正**: 次のステップセクションにおいて、ガイドのタイトルが「DALL-Eハウツーガイド」から「Image APIハウツーガイド」に変更され、読者がDALL-E以外の画像APIについても興味を持つように促しています。

これらの変更は、ドキュメントのクオリティを向上させ、利用者にとっての使いやすさを増すことを目指しています。

## articles/ai-services/openai/includes/dall-e-typescript.md{#item-57b205}

<details>
<summary>Diff</summary>
````diff
@@ -248,7 +248,7 @@ Image generation result URL: <SAS URL>
 ```
 
 > [!NOTE]
-> The image generation APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it won't return a generated image. For more information, see the [content filter](../concepts/content-filter.md) article.
+> The Image APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it won't return a generated image. For more information, see the [content filter](../concepts/content-filter.md) article.
 
 ## Clean up resources
 
@@ -259,5 +259,5 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 
 ## Next steps
 
-* Explore the image generation APIs in more depth with the [DALL-E how-to guide](../how-to/dall-e.md).
+* Explore the Image APIs in more depth with the [Image API how-to guide](../how-to/dall-e.md).
 * For more examples check out the [Azure OpenAI Samples GitHub repository](https://github.com/Azure/openai-samples).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の統一と情報の明確化"
}
```

### Explanation
この変更は、DALL-Eに関するTypeScriptのドキュメントにおける用語の統一と内容の明確化を目的としています。以下は変更の要点です：

1. **用語の統一**: 「画像生成API」という表現が「Image APIs」に統一され、文書内での表現が一貫性を持つようになりました。この変更により、読者は異なるセクションで同じ用語を認識しやすくなります。

2. **コンテンツモデレーションフィルターの説明の改善**: フィルターに関する文が見直され、サービスが有害なコンテンツと認識した場合に画像が生成されないことが明確に示されています。この情報の明確化によって、ユーザーはフィルターの機能についてより良い理解を得ることができます。

3. **次のステップの文言修正**: 次のステップセクションにおいて、ガイドのタイトルが「DALL-Eハウツーガイド」から「Image APIハウツーガイド」に変更され、これにより読者がDALL-E以外の画像APIに興味を持つ動機付けが行われています。

これらの変更は、ドキュメントの品質向上と読者の理解を深めることを目指しています。

## articles/ai-services/openai/includes/language-overview/dotnet.md{#item-46e881}

<details>
<summary>Diff</summary>
````diff
@@ -264,7 +264,7 @@ bytes.ToStream().CopyTo(stream);
 
 ```
 
-- [C# DALL-E quickstart guide](/azure/ai-services/openai/dall-e-quickstart?tabs=dalle3%2Ccommand-line%2Ckeyless%2Ctypescript-keyless&pivots=programming-language-csharp)
+- [C# Image generation quickstart guide](/azure/ai-services/openai/dall-e-quickstart?tabs=dalle3%2Ccommand-line%2Ckeyless%2Ctypescript-keyless&pivots=programming-language-csharp)
 
 ## Reasoning models
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ガイドタイトルの修正"
}
```

### Explanation
この変更は、.NETに関するドキュメントの一部で、ガイドのタイトル修正を行っています。具体的には、以下の変更が行われました：

1. **ガイドタイトルの変更**: 「C# DALL-Eクイックスタートガイド」という表現が「C#画像生成クイックスタートガイド」に変更されました。この変更により、コンテンツがより具体的で明確になり、読者にとって理解しやすくなります。

この修正は、ドキュメントがより正確で統一的な表現を持つことを目的としており、読者が必要な情報をより迅速に見つけられるように助けています。

## articles/ai-services/openai/includes/model-matrix/global-batch.md{#item-929e6a}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,6 @@ ms.date: 04/21/2025
 | eastus2            | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
 | francecentral      | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
 | germanywestcentral | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| italynorth         | ✅                        | -                      | -                      | -                      | -                           | -               | -                           | -                      | -                      | -                      |
 | japaneast          | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
 | koreacentral       | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | northcentralus     | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
@@ -31,7 +30,6 @@ ms.date: 04/21/2025
 | spaincentral       | ✅                        | -                      | -                      | -                      | -                           | -               | -                           | -                      | -                      | -                      |
 | swedencentral      | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
 | switzerlandnorth   | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
-| uaenorth           | ✅                        | -                      | -                      | -                      | -                           | -               | -                           | -                      | -                      | -                      |
 | uksouth            | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
 | westeurope         | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | westus             | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルマトリックスの地域データの修正"
}
```

### Explanation
この変更は、グローバルバッチに関するモデルマトリックスのドキュメントで、特定の地域に関するデータを修正するために行われました。具体的な変更内容は以下の通りです：

1. **地域データの削除**: 「italynorth」および「uaenorth」という地域に関する行が削除されました。これにより、これらの地域のモデルサポート情報が無効または利用できないことを反映しています。

2. **データの整合性向上**: 不要な地域データを削除することで、表はより正確で信頼できる情報を提供することができ、読者が現在利用可能なサービスの理解を助けることになります。

この変更は、使用されていないまたは利用できない地域情報を排除することで、ドキュメントの品質と正確さを向上させることを目指しています。

## articles/ai-services/openai/includes/structured-outputs-python.md{#item-2734f0}

<details>
<summary>Diff</summary>
````diff
@@ -20,6 +20,7 @@ pip install openai pydantic --upgrade
 If you are new to using Microsoft Entra ID for authentication see [How to configure Azure OpenAI Service with Microsoft Entra ID authentication](../how-to/managed-identity.md).
 
 ```python
+import os
 from pydantic import BaseModel
 from openai import AzureOpenAI
 from azure.identity import DefaultAzureCredential, get_bearer_token_provider
@@ -105,6 +106,7 @@ pip install openai pydantic --upgrade
 ```
 
 ```python
+import os
 from pydantic import BaseModel
 from openai import AzureOpenAI
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonモジュールのインポート追加"
}
```

### Explanation
この変更は、Python用の構造化出力に関するドキュメントでの軽微な更新を示しています。具体的には、以下の2つの行に新しく`import os`というインポート宣言が追加されました：

1. **osモジュールのインポート**: Pythonの`os`モジュールをインポートすることで、OSに関連する機能を利用可能にします。これにより、ファイルパス操作や環境変数の取得など、OS固有の操作に簡単にアクセスできるようになります。

この修正は、コードサンプルがより高機能で柔軟に動作することを目的としており、エンドユーザーが必要な機能を容易に使用できるように支援します。

## articles/ai-services/openai/index.yml{#item-0adb87}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,11 @@
 ### YamlMime:Landing
 
 title: Azure OpenAI Service documentation # < 60 chars
-summary: Azure OpenAI Service provides access to OpenAI's models including o-series, GPT-4o, GPT-4o mini, GPT-4, GPT-4 Turbo with Vision, GPT-3.5-Turbo, DALLE-3 and Embeddings model series with the security and enterprise capabilities of Azure. 
+summary: Azure OpenAI Service provides access to OpenAI's models including o-series, GPT-4o, GPT-4o mini, GPT-4, GPT-4 Turbo with Vision, GPT-3.5-Turbo, GPT-image-1 and Embeddings model series with the security and enterprise capabilities of Azure. 
   
 metadata:
   title: Azure OpenAI Service documentation - Quickstarts, Tutorials, API Reference - Azure AI services | Microsoft Docs
-  description: Learn how to use Azure OpenAI's powerful models including o-series, GPT-4o, GPT-4o mini, GPT-4, GPT-4 Turbo with Vision, GPT-3.5-Turbo, DALL-E 3 and Embeddings model series
+  description: Learn how to use Azure OpenAI's powerful models including o-series, GPT-4o, GPT-4o mini, GPT-4, GPT-4 Turbo with Vision, GPT-3.5-Turbo, GPT-image-1, and Embeddings model series
   ms.service: azure-ai-openai
   ms.custom:
   ms.topic: landing-page
@@ -42,7 +42,7 @@ landingContent:
              url: chatgpt-quickstart.md
            - text: Vision-enabled models
              url: gpt-v-quickstart.md  
-           - text: DALL-E
+           - text: Image generation
              url: dall-e-quickstart.md
            - text: Use your data (preview)
              url: use-your-data-quickstart.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル名の修正とリンクテキストの変更"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関するYAMLファイルの軽微な更新を示しています。具体的な内容は次の通りです：

1. **要約の修正**: `summary`フィールド内のモデル名が更新されました。「DALLE-3」という名称が「GPT-image-1」に変更され、最新のモデル情報を反映しています。この修正により、ユーザーが利用可能な最新のモデルに対する正確な情報を得ることができます。

2. **説明文の更新**: `description`フィールドも更新され、同様にモデル名が「DALL-E 3」から「GPT-image-1」に変更されています。これにより、文中の表記に一貫性が持たせられます。

3. **リンクテキストの変更**: リンク先のテキストが「DALL-E」から「Image generation」に変更され、より明確にその内容が伝わるようになっています。

この変更は、ユーザーに対して提供される情報の正確性と明瞭さを向上させ、Azure OpenAIサービスに関連するドキュメントの質を高めることを目的としています。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -52,7 +52,7 @@ Start with the [Create and deploy an Azure OpenAI Service resource](./how-to/cre
 
 ## Comparing Azure OpenAI and OpenAI
 
-Azure OpenAI Service gives customers advanced language AI with OpenAI GPT-4, GPT-3, Codex, DALL-E, speech to text, and text to speech models with the security and enterprise promise of Azure. Azure OpenAI co-develops the APIs with OpenAI, ensuring compatibility and a smooth transition from one to the other.
+Azure OpenAI Service gives customers advanced language AI with OpenAI GPT-4, GPT-3, Codex, GPT-image-1 (preview), DALL-E, speech to text, and text to speech models with the security and enterprise promise of Azure. Azure OpenAI co-develops the APIs with OpenAI, ensuring compatibility and a smooth transition from one to the other.
 
 With Azure OpenAI, customers get the security capabilities of Microsoft Azure while running the same models as OpenAI. Azure OpenAI offers private networking, regional availability, and responsible AI content filtering.  
 
@@ -129,7 +129,7 @@ Prompt construction can be difficult. In practice, the prompt acts to configure
 
 The service provides users access to several different models. Each model provides a different capability and price point.
 
-The DALL-E models (some in preview; see [models](./concepts/models.md#dall-e)) generate images from text prompts that the user provides.
+The image generation models (some in preview; see [models](./concepts/models.md#image-generation-models)) generate and edit images from text prompts that the user provides.
 
 The audio API models can be used to transcribe and translate speech to text. The text to speech models, currently in preview, can be used to synthesize text to speech.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル名と説明の修正"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関する概要ドキュメントの軽微な更新を示しています。主な内容は以下の通りです：

1. **モデル名の更新**: 概要のセクションでは、`DALL-E`というモデル名が`GPT-image-1 (preview)`に変更されています。これにより、最新のモデル情報が正確に伝えられるようになります。

2. **説明文の改善**: コピー内にあった`DALL-E`モデルに関する記述が、`image generation models`という表現に変更されています。さらに、これに関連する説明文も更新され、ユーザーが提供するテキストプロンプトから生成・編集される画像に関してより正確に記述されています。

この修正は、Azure OpenAIサービスの提供情報を最新のものに保ち、ユーザーが利用可能な機能を正確に理解できるようにサポートすることを目的としています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 4/14/2025
+ms.date: 04/23/2025
 ms.author: mbullwin
 ---
 
@@ -26,6 +26,7 @@ The following sections provide you with a quick guide to the default quotas and
 | Azure OpenAI resources per region per Azure subscription | 30 |
 | Default DALL-E 2 quota limits | 2 concurrent requests |
 | Default DALL-E 3 quota limits| 2 capacity units (6 requests per minute)|
+| Default GPT-image-1 quota limits | 2 capacity units (6 requests per minute) |
 | Default speech to text audio API quota limits | 3 requests per minute |
 | Maximum prompt tokens per request | Varies per model. For more information, see [Azure OpenAI Service models](./concepts/models.md)|
 | Max Standard deployments per resource | 32 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-image-1のクオータ制限の追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスのクオータと制限に関するドキュメントの軽微な更新を示しています。主な変更点は以下の通りです：

1. **日付の更新**: `ms.date`フィールドの日付が`4/14/2025`から`04/23/2025`に更新され、最新の情報に合わせられています。

2. **GPT-image-1のクオータ追加**: 新しいモデルである`GPT-image-1`のデフォルトのクオータ制限が文書に追加されました。具体的には、`GPT-image-1`モデルについて「2 capacity units (6 requests per minute)」という制限が明記され、他のモデルと同様に、利用可能なリソースを明確にしています。

この修正により、ユーザーはAzure OpenAIサービスにおける最新のクオータと制限を把握できるようになり、サービスを利用する際の計画を立てやすくなります。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -36,7 +36,7 @@ items:
       displayName: ChatGPT, chatgpt
     - name: Vision-enabled chats
       href: gpt-v-quickstart.md
-    - name: DALL-E
+    - name: Image generation
       href: dall-e-quickstart.md
     - name: Use your data
       href: use-your-data-quickstart.md
@@ -128,7 +128,7 @@ items:
       displayName: cua, computer using model
     - name: Vision-enabled chats
       href: ./how-to/gpt-with-vision.md
-    - name: DALL-E
+    - name: Image generation
       href: ./how-to/dall-e.md
     - name: Function calling
       href: ./how-to/function-calling.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL-Eの名称をImage Generationに変更"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連する目次（toc.yml）ファイルの軽微な更新を表しています。主な変更点は以下の通りです：

1. **DALL-Eの名称変更**: 目次の中で`DALL-E`の項目が`Image generation`に変更されました。この変更は、DALL-Eに関連するコンテンツのタイトルをより広範な「画像生成」とすることで、ユーザーがサービスの範囲をより良く理解できるように意図されています。

2. **パスの保持**: 変わらず、各項目のリンク（href）は元のまま維持されています。これは、ユーザーが変更された名称の背後にある実際のコンテンツへのアクセスを容易にするためです。

この変更により、目次が最新の用語に適応し、より明確で包括的なものになることが目的となっています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -21,6 +21,17 @@ This article provides a summary of the latest releases and major documentation u
 
 ## April 2025
 
+### GPT-image-1 released (preview, limited access)
+
+GPT-image-1 (2025-04-15) is the latest image generation model from Azure OpenAI. It features major improvements over DALL-E, including:
+- Better at responding to precise instructions.
+- Reliably renders text.
+- Accepts images as input, which enables the new capabilities of image editing and inpainting.
+
+Request access: [Limited access model application](https://aka.ms/oai/gptimage1access)
+
+Follow the [image generation how-to guide](/en-us/azure/ai-services/openai/how-to/dall-e) to get started with the new model.
+
 ### o4-mini and o3 models released
 
 `o4-mini` and `o3` models are now available. These are the latest reasoning models from Azure OpenAI offering significantly enhanced reasoning, quality, and performance. For more information, see the [getting started with reasoning models page](./how-to/reasoning.md).
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "GPT-image-1モデルのリリース情報追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「新着情報」セクションに関する重要な更新を示しています。具体的には、以下の内容が追加されました：

1. **新モデルGPT-image-1のリリース**: 新たに「GPT-image-1」という画像生成モデルがプレビュー版として発表され、その日付は2025年4月15日です。このモデルはDALL-Eに対して以下のような重要な改善点を持っています：
   - 精確な指示に対する応答能力の向上。
   - テキストの信頼性のあるレンダリング。
   - 画像を入力として受け入れる機能により、画像編集やインペインティングの新しい能力を実現。

2. **アクセス申し込みのリンク**: モデルの利用を希望するユーザー向けに、制限付きアクセスモデルの申し込みリンクが提供されています。

3. **新モデルのガイドへのリンク**: ユーザーが新しいモデルに関するスタートガイドを参照できるように、画像生成関連のハウツーガイドへのリンクが追加されています。

この修正により、ユーザーは新しい画像生成モデルの特性や利用方法を容易に理解し、興味を持って試すことができるでしょう。


