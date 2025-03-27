---
date: '2025-03-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e737b2f...MicrosoftDocs:4f20510
summary: この変更は、Azure OpenAIサービス関連文書に対する一連の小幅な更新を示しています。主なポイントは、モデル廃止日の更新、新機能やデモの追加、コードとリンクの整形改善、レスポンスAPIの情報強化、画像URL処理詳細の追加、およびクォータ制限に関する注意書きの導入です。新しいプレビューGIFとデモコードのリンクが追加され、ユーザーが新機能を視覚化しやすくなりました。モデルの自動アップグレードと廃止日が延期され、システムの継続的な適用が保証されています。また、文書の改良や詳細な情報の追加により、技術的理解が深まることを目指しています。全体的に、これらの変更はユーザー体験を向上させ、利用者に質の高い情報を提供することを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e737b2f...MicrosoftDocs:4f20510){target="_blank"}

<format>
# Highlights
この変更は、Azure OpenAIサービス関連文書に対する一連の小幅な更新を示しています。注目すべきは、モデル廃止日の更新、新機能やデモの追加、コードとリンクの整形改善、レスポンスAPIの情報強化、画像URL処理詳細の追加、およびクォータ制限に関する注意書きの導入です。

## New Features
- `computer-use-preview.gif` というプレビューGIFが追加され、コンピュータ使用法の視覚的デモを提供。
- "What's New" 文書にデモGIFやデモコードへのリンクが追加され、ユーザーが新機能を視覚化しやすくする。

## Breaking Changes
- 大きな破壊的変更はありませんが、モデルの自動アップグレードと廃止日が延期され、それに伴う準備の見直しが必要です。

## Other Updates
- ドキュメントの整合性とコードの保守性を高めるための小規模な文書改善。
- レスポンスAPIと画像URLに関する詳細の追加が行われ、より深い技術的理解が可能に。

# Insights
この一連の更新は、Azure OpenAIサービスに関する文書の精度、透明性、およびユーザーの理解を強化することを目指しています。

新たなモデルの導入に対する準備期間を延長することで、ユーザーが物理的および技術的な準備を整えるための時間を確保しました。特に、モデルの廃止日に関する変更は、システムの継続的な適用を保証し、業務への影響を最小限に抑えます。

また、プレビューGIFの追加やデモコードのリンクは、ユーザーがAzure OpenAIの機能を直感的に把握し、応用するのに役立つ視覚的かつ具体的な手段を提供します。これにより、技術的な特性をより広範囲の利害関係者がアクセスしやすくなり、学習曲線を平坦化する効果があります。

クォータ制限では、注意書きが追加されることで利用者はリソース計画においてアジャイルに対応可能です。この透明性を促進するアプローチは、企業が製品利用の最適化を図る上で不可欠な要素となります。

全体として、これらの変更は利用者により高水準な情報提供を実現し、サービス利用の初期段階から成熟したフェーズに至るまでのサポートを強化します。結果として、ビジュアルデモの提供や細かな設定の追加が、ユーザー体験を改善し、適切な技術導入を助けるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルの廃止日更新 | modified | 2 | 2 | 4 | 
| [computer-use.md](#item-6fbca8) | minor update | コードの整形とリンクの更新 | modified | 2 | 2 | 4 | 
| [responses.md](#item-b9757d) | minor update | レスポンスAPIに関する情報の強化 | modified | 28 | 17 | 45 | 
| [batch-python.md](#item-3121c2) | minor update | 画像URLを用いた入力の詳細の追加 | modified | 3 | 2 | 5 | 
| [batch-rest.md](#item-bcccd9) | minor update | 画像URLを利用した入力の詳細設定の追加 | modified | 3 | 2 | 5 | 
| [batch-studio.md](#item-d4822e) | minor update | 画像URLを用いた入力の詳細パラメータの追加 | modified | 2 | 1 | 3 | 
| [computer-use-preview.gif](#item-253455) | new feature | コンピュータ使用のプレビューGIFの追加 | added | 0 | 0 | 0 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータ制限に関する注意書きの追加 | modified | 3 | 0 | 3 | 
| [whats-new.md](#item-53303b) | minor update | 新機能とデモの追加 | modified | 4 | 0 | 4 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 03/24/2025
+ms.date: 03/26/2025
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -126,7 +126,7 @@ These models are currently available for use in Azure OpenAI Service.
 | Model | Current default version | New default version | Default upgrade date |
 |---|---|---|---|
 | `gpt-35-turbo` | 0301 | 0125 | Deployments of versions `0301`, `0613`, and `1106` set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 21, 2025.|
-|  `gpt-4o` | 2024-05-13 | 2024-08-06 | Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on February 13, 2025. |
+|  `gpt-4o` | 2024-05-13 | 2024-08-06 | Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on March 26, 2025. |
 
 ## Deprecated models
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの廃止日更新"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関連する文書の更新を反映しています。具体的には、`model-retirements.md` ファイルにおけるモデルの自動アップグレードに関する日付が変更されました。

1. **日付の更新**: `gpt-4o` モデルの自動アップグレード開始日が「2024年5月13日」から「2024年08月06日」に変更され、マークされた日付が「2025年2月13日」から「2025年3月26日」に変更されました。この変更により、ユーザーは新しいモデルの導入に対する準備が適切に行えるようになります。

2. **文書の整合性**: この変更は、モデルのリタイアに関する情報を最新のものに保つため、ユーザーが正しい日程を知り、計画を立てやすくすることを意図しています。

全体として、この更新は文書の正確さと関連性を向上させるものであり、ユーザーへの情報提供を強化しています。

## articles/ai-services/openai/how-to/computer-use.md{#item-6fbca8}

<details>
<summary>Diff</summary>
````diff
@@ -222,7 +222,7 @@ response_2 = client.responses.create(
     tools=[{
         "type": "computer-preview",
         "display_width": 1024,
-        "display_height": 768
+        "display_height": 768,
         "environment": "browser" # other possible values: "mac", "windows", "ubuntu"
     }],
     input=[
@@ -363,4 +363,4 @@ In all cases where `pending_safety_checks` are returned, actions should be hande
 
 * [Responses API](./responses.md)
     * [Computer Use with playwright](./responses.md#computer-use)
-* [Computer Use Assistant sample on Github](https://github.com/Azure-Samples/computer-use-model)
\ No newline at end of file
+* [Computer Use Assistant sample on Github](https://github.com/Azure-Samples/computer-use-model)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コードの整形とリンクの更新"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関する `computer-use.md` 文書の修正を行っています。主な変更点は次のとおりです。

1. **コードの整形**: コードブロック内の JSON オブジェクトにおいて、`"display_height": 768` の行の末尾にカンマを追加しました。これにより、構文としての正確性が向上し、将来的な要素追加時にエラーを防ぐことができます。この小さな変更でも、コードの読みやすさと保守性を高める効果があります。

2. **リンクの更新**: 最後の項目において、GitHub 上の「Computer Use Assistant」サンプルへのリンクが修正されました。具体的には、リンクの末尾に改行を追加し、ファイルの整形を改善しています。これにより、文書の可読性が向上し、リンクの正確な表現にもつながります。

これらの変更は、文書の機能性や可読性を向上させることを目的としており、ユーザーにとっての情報提供を円滑にしています。

## articles/ai-services/openai/how-to/responses.md{#item-b9757d}

<details>
<summary>Diff</summary>
````diff
@@ -40,17 +40,21 @@ The responses API is currently available in the following regions:
 
 ### Model support
 
-- `gpt-4o`
-- `gpt-4o-mini`
+- `gpt-4o` (Versions: `2024-11-20`, `2024-08-06`, `2024-05-13`)
+- `gpt-4o-mini` (Versions: `2024-07-18`)
 - `computer-use-preview`
 
+Not every model is available in the regions supported by the responses API. Check the [models page](../concepts/models.md) for model region availability.
+
 > [!NOTE]
-> The responses API does not currently support:
+> Not currently supported:
 > - Structured outputs
 > - tool_choice
-> - image_url pointing to an internet address  
->
-> There is also a known issue with vision performance when using the Responses API, particularly with OCR tasks. Once this issue is fixed and support is added, this article will be updated.
+> - image_url pointing to an internet address
+> - The web search tool is also not supported, and is not part of the `2025-03-01-preview` API.  
+> 
+> There is also a known issue with vision performance when using the Responses API, particularly with OCR tasks. As a temporary workaround set image detail to `high`. This article will be updated once this issue is resolved and as any additional feature support is added.
+
 
 ### Reference documentation
 
@@ -568,6 +572,8 @@ print(response.model_dump_json(indent=2))
 
 ## Image input
 
+There is a known issue with image url based image input. Currently only base64 encoded images are supported.
+
 ### Image url
 
 ```python
@@ -654,6 +660,8 @@ print(response)
 
 In this section, we provide a simple example script that integrates Azure OpenAI's `computer-use-preview` model with [Playwright](https://playwright.dev/) to automate basic browser interactions. Combining the model with [Playwright](https://playwright.dev/) allows the model to see the browser screen, make decisions, and perform actions like clicking, typing, and navigating websites. You should exercise caution when running this example code. This code is designed to be run locally but should only be executed in a test environment. Use a human to confirm decisions and don't give the model access to sensitive data.
 
+:::image type="content" source="../media/computer-use-preview.gif" alt-text="Animated gif of computer-use-preview model integrated with playwright." lightbox="../media/computer-use-preview.gif":::
+
 First you'll need to install the Python library for [Playwright](https://playwright.dev/).
 
 ```cmd
@@ -808,18 +816,21 @@ async def handle_action(page, action):
         print(f"\tUnrecognized action: {action_type}")
 ```
 
-This function attempts to handle various types of actions such as:
+This function attempts to handle various types of actions. We need to translate between the commands that the `computer-use-preview` will generate and the Playwright library which will execute the actions. For more information refer to the reference documentation for `ComputerAction`.
 
-- Clicking and dragging the mouse.
-- Clicking (left, right, middle buttons).
-- Double-clicking.
-- Scrolling.
-- Key presses (including combinations).
-- Typing text.
+- [Click](/azure/ai-services/openai/reference-preview#click)
+- [DoubleClick](/azure/ai-services/openai/reference-preview#doubleclick)
+- [Drag](/azure/ai-services/openai/reference-preview#drag)
+- [KeyPress](/azure/ai-services/openai/reference-preview#keypress)
+- [Move](/azure/ai-services/openai/reference-preview#move)
+- [Screenshot](/azure/ai-services/openai/reference-preview#screenshot)
+- [Scroll](/azure/ai-services/openai/reference-preview#scroll)
+- [Type](/azure/ai-services/openai/reference-preview#type)
+- [Wait](/azure/ai-services/openai/reference-preview#wait)
 
 ### Screenshot capture
 
-In order for the model to be able to see what it's interacting with the model needs a way to capture screenshots. For this code we're using Playwright to capture the screenshots and we're limiting the view to just the content in the browser window. The screenshot won't include the url bar or other aspects of the browser GUI. If you need the model to see outside the main browser window you could augment the model by creating your own screenshot function.
+In order for the model to be able to see what it's interacting with the model needs a way to capture screenshots. For this code we're using Playwright to capture the screenshots and we're limiting the view to just the content in the browser window. The screenshot won't include the url bar or other aspects of the browser GUI. If you need the model to see outside the main browser window you could augment the model by creating your own screenshot function. 
 
 ```python
 async def take_screenshot(page):
@@ -837,7 +848,7 @@ async def take_screenshot(page):
             return last_successful_screenshot
 ```
 
-This function captures the current browser state as an image and returns it as a base64-encoded string, ready to be sent to the model. We'll constantly do this in a loop after each step allowing the model to see if the command it tried to execute was successful or not, which then allows it to adjust based on the contents of the screenshot.
+This function captures the current browser state as an image and returns it as a base64-encoded string, ready to be sent to the model. We'll constantly do this in a loop after each step allowing the model to see if the command it tried to execute was successful or not, which then allows it to adjust based on the contents of the screenshot. We could let the model decide if it needs to take a screenshot, but for simplicity we will force a screenshot to be taken for each iteration.
 
 ### Model response processing
 
@@ -1003,7 +1014,7 @@ In this section we have added code that:
 - Handles potential safety checks requiring user confirmation.
 - Executes the requested action.
 - Captures a new screenshot.
-- Sends the updated state back to the model.
+- Sends the updated state back to the model and defines the [`ComputerTool`](/azure/ai-services/openai/reference-preview#computertool).
 - Repeats this process for multiple iterations.
 
 ### Main function
@@ -1110,7 +1121,7 @@ The main function:
 ### Complete script
 
 > [!CAUTION]
-> This code is experimental and for demonstration purposes only. It's only intended to illustrate the basic flow of the responses API and the `computer-use-preview` model. While you can execute this code on your local computer, we strongly recommend running this code on a low privilege virtual machine with no access to sensitive data. This code is for basic testing purposes only. 
+> This code is experimental and for demonstration purposes only. It's only intended to illustrate the basic flow of the responses API and the `computer-use-preview` model. While you can execute this code on your local computer, we strongly recommend running this code on a low privilege virtual machine with no access to sensitive data. This code is for basic testing purposes only.
 
 ```python
 import os
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レスポンスAPIに関する情報の強化"
}
```

### Explanation
この変更は、Azure OpenAI サービスにおけるレスポンス API に関する文書 `responses.md` の大幅な更新を含んでいます。主な変更点は以下の通りです。

1. **モデルサポートの明確化**: `gpt-4o` および `gpt-4o-mini` のバージョン情報が追加され、どのバージョンが存在するかが明示されています。これにより、利用可能なモデルのバージョンについてユーザーが理解しやすくなります。

2. **機能制限の更新**: API が現在サポートしていない機能についての説明が更新されました。特に、`image_url` に関する制限や、 vision API の既知の問題について具体的な回避策が提示されています。これにより、ユーザーは制約を理解し、効果的に使用するための対策を講じることができます。

3. **コードのセクション追加および調整**: コードセクション内では、Playwright とインタラクションを持つモデルに関する詳細が充実しました。具体的には、アクションの処理方法についての説明にリンクが追加され、ユーザーが必要な情報に簡単にアクセスできるようになっています。また、状況に応じたスクリーンショットのキャプチャ方法についても、コード内での説明が強調されています。

4. **警告文の強化**: 実験的なコードに関する注意喚起がより具体的になり、ユーザーが安全に使用するための推奨事項が明確に示されています。

これらの変更は、ユーザーがレスポンス API をより効果的に理解し、利用できるようにすることを意図しており、全体的な情報の質を向上させています。

## articles/ai-services/openai/includes/batch/batch-python.md{#item-3121c2}

<details>
<summary>Diff</summary>
````diff
@@ -52,8 +52,9 @@ Like [fine-tuning](../../how-to/fine-tuning.md), global batch uses files in JSON
 ### Input with image url
 
 ```json
-{"custom_id": "request-1", "method": "POST", "url": "/chat/completions", "body": {"model": "REPLACE-WITH-MODEL-DEPLOYMENT-NAME", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": [{"type": "text", "text": "What’s in this image?"},{"type": "image_url","image_url": {"url": "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/ai-services/openai/media/how-to/generated-seattle.png"}}]}],"max_tokens": 1000}}
+{"custom_id": "request-1", "method": "POST", "url": "/chat/completions", "body": {"model": "REPLACE-WITH-MODEL-DEPLOYMENT-NAME", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": [{"type": "text", "text": "What’s in this image?"},{"type": "image_url","image_url": {"url": "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/ai-services/openai/media/how-to/generated-seattle.png", "detail": "high"}}]}],"max_tokens": 1000}}
 ```
+The `detail` parameter tells the model what level of detail to use when processing and understanding the image (`low`, `high`, or `auto` to let the model decide). If you skip the parameter, the model will use `auto`.
 
 # [Structured outputs](#tab/structured-outputs)
 
@@ -167,7 +168,7 @@ print(batch_response.model_dump_json(indent=2))
 ```
 
 > [!NOTE]
-> Currently the completion window must be set to 24h. If you set any other value than 24h your job will fail. Jobs taking longer than 24 hours will continue to execute until cancelled.
+> Currently the completion window must be set to 24h. If you set any other value than 24h your job will fail. Jobs taking longer than 24 hours will continue to execute until canceled.
 
 **Output:**
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像URLを用いた入力の詳細の追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関する `batch-python.md` 文書の更新であり、特に画像 URL を用いた入力処理に関する情報が強化されています。主な変更点は次の通りです。

1. **画像処理の詳細パラメータの追加**: 画像を含むリクエストボディの JSON 構造に `detail` パラメータが追加されました。このパラメータは、モデルが画像を処理および理解する際に使用する詳細度を指定するもので、`low`、`high`、または `auto`（モデルに判断を任せる）を設定できます。これにより、ユーザーは画像処理の精度をより柔軟に管理できるようになります。

2. **説明文の追加**: `detail` パラメータの目的やデフォルト値についての説明が追加され、ユーザーがこの新しい機能を理解しやすくなっています。この情報は、モデルを効果的に利用するための知識を提供します。

3. **エラーメッセージの表現修正**: 24 時間の完了ウィンドウに関する注意書きの表現が改善され、特に「canceled」と「cancelled」の表記が統一されました。これにより、文書全体の表現が一貫性を持ち、読みやすさが向上しています。

これらの更新は、画像処理に関する情報の明確化と、ユーザーがシステムを最大限に活用するためのサポートを目的としています。

## articles/ai-services/openai/includes/batch/batch-rest.md{#item-bcccd9}

<details>
<summary>Diff</summary>
````diff
@@ -41,8 +41,9 @@ Like [fine-tuning](../../how-to/fine-tuning.md), global batch uses files in JSON
 ### Input with image url
 
 ```json
-{"custom_id": "request-1", "method": "POST", "url": "/chat/completions", "body": {"model": "REPLACE-WITH-MODEL-DEPLOYMENT-NAME", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": [{"type": "text", "text": "What’s in this image?"},{"type": "image_url","image_url": {"url": "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/ai-services/openai/media/how-to/generated-seattle.png"}}]}],"max_tokens": 1000}}
+{"custom_id": "request-1", "method": "POST", "url": "/chat/completions", "body": {"model": "REPLACE-WITH-MODEL-DEPLOYMENT-NAME", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": [{"type": "text", "text": "What’s in this image?"},{"type": "image_url","image_url": {"url": "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/ai-services/openai/media/how-to/generated-seattle.png", "detail": "high"}}]}],"max_tokens": 1000}}
 ```
+The `detail` parameter tells the model what level of detail to use when processing and understanding the image (`low`, `high`, or `auto` to let the model decide). If you skip the parameter, the model will use `auto`.
 
 # [Structured outputs](#tab/structured-outputs)
 
@@ -138,7 +139,7 @@ curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-vers
 ```
 
 > [!NOTE]
-> Currently the completion window must be set to 24h. If you set any other value than 24h your job will fail. Jobs taking longer than 24 hours will continue to execute until cancelled.
+> Currently the completion window must be set to 24h. If you set any other value than 24h your job will fail. Jobs taking longer than 24 hours will continue to execute until canceled.
 
 **Output:**
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像URLを利用した入力の詳細設定の追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関する `batch-rest.md` 文書の更新であり、特に画像 URL を用いた入力処理に関する情報が強化されています。主な変更点は次の通りです。

1. **画像処理の詳細パラメータの追加**: JSON のリクエストボディに `detail` パラメータが追加されました。このパラメータは、モデルが画像を処理する際の詳細度を指定するもので、`low`、`high`、または `auto`（モデルに判断を任せる）を選ぶことができます。これにより、ユーザーは画像理解の精度を調整できる柔軟性が提供されます。

2. **説明文の追加**: `detail` パラメータの目的や、デフォルトの動作についての説明が追加され、ユーザーがこの新機能を正しく理解できるようになっています。この情報は、実装や使用時に役立つでしょう。

3. **エラーメッセージの表現の修正**: 24 時間の完了ウィンドウに関する注意書きの表現が改善され、「canceled」（キャンセル）という表記が統一されています。この修正は文書の整合性を向上させ、読み手にとって理解しやすくしています。

これらの更新は、画像処理機能の拡充と、ユーザーがサービスを効果的に利用できるようにすることを目的としています。

## articles/ai-services/openai/includes/batch/batch-studio.md{#item-d4822e}

<details>
<summary>Diff</summary>
````diff
@@ -41,8 +41,9 @@ Like [fine-tuning](../../how-to/fine-tuning.md), global batch uses files in JSON
 ### Input with image url
 
 ```json
-{"custom_id": "request-1", "method": "POST", "url": "/chat/completions", "body": {"model": "REPLACE-WITH-MODEL-DEPLOYMENT-NAME", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": [{"type": "text", "text": "What’s in this image?"},{"type": "image_url","image_url": {"url": "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/ai-services/openai/media/how-to/generated-seattle.png"}}]}],"max_tokens": 1000}}
+{"custom_id": "request-1", "method": "POST", "url": "/chat/completions", "body": {"model": "REPLACE-WITH-MODEL-DEPLOYMENT-NAME", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": [{"type": "text", "text": "What’s in this image?"},{"type": "image_url","image_url": {"url": "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/ai-services/openai/media/how-to/generated-seattle.png", "detail": "high"}}]}],"max_tokens": 1000}}
 ```
+The `detail` parameter tells the model what level of detail to use when processing and understanding the image (`low`, `high`, or `auto` to let the model decide). If you skip the parameter, the model will use `auto`.
 
 # [Structured outputs](#tab/structured-outputs)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像URLを用いた入力の詳細パラメータの追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関する `batch-studio.md` 文書の更新であり、特に画像 URL を用いた入力処理に関する情報の強化が図られています。主な変更点は次の通りです。

1. **画像処理の詳細パラメータの追加**: リクエストボディの JSON データに `detail` パラメータが追加されました。これにより、モデルが画像を処理する際に参照する詳細レベルを指定でき、選択肢として `low`、`high`、または `auto`（モデルに最適な判断を任せる）を使用できます。この機能により、ユーザーはモデルの出力の精度を柔軟に管理できるようになります。

2. **説明文の追加**: 新しく追加された `detail` パラメータに関する使用方法やデフォルトの動作についての説明が文書に追加されています。これにより、ユーザーはこの機能を適切に理解し、効果的に活用することが期待されます。

3. **文書の読みやすさ向上**: 変更により、JSON サンプルがより明確になり、関連情報が強調されることで、全体の文書の可読性が向上しています。

この更新は、ユーザーが画像に基づくリクエストを行う際の理解を深め、モデルの性能を最大限に引き出すことを目的としています。

## articles/ai-services/openai/media/computer-use-preview.gif{#item-253455}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "コンピュータ使用のプレビューGIFの追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関連する文書に新たに GIF ファイルが追加されたことを示しています。具体的には、`computer-use-preview.gif` という名前のファイルが新たにリポジトリに加えられました。この GIF は、コンピュータの使用状況を示すための視覚的な要素として機能し、ユーザーが具体的な操作や機能を理解する手助けをすることを目的としています。

この追加により、文書はより視覚的に魅力的になり、利用者にとっての情報の伝達が改善されるでしょう。GIF ファイルは、特定の機能や操作の概念を具体化し、特に視覚的な学習を好むユーザーにとって有用なリソースとなります。これにより、全体としてのユーザー体験が向上すると期待されます。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -57,6 +57,9 @@ The following sections provide you with a quick guide to the default quotas and
 
 ## Regional quota limits
 
+> [!NOTE]
+> Quota limits are subject to change. 
+
 [!INCLUDE [Quota](./includes/global-batch-limits.md)]
 
 ## computer-use-preview global standard
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータ制限に関する注意書きの追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関連する `quotas-limits.md` 文書において、クォータ制限に関する情報が更新されたことを示しています。具体的には、以下の改訂が行われました。

1. **注意書きの追加**: 新たに「Quota limits are subject to change」という注意書きが文書に追加されました。これにより、クォータ制限が変更される可能性があることが明確になり、利用者は最新の情報に留意する必要があることを理解することができます。

2. **内容の明確化**: 注意書きを加えることで、文書の内容の信頼性が向上し、ユーザーに対する透明性が強化されます。この情報は、特に利用者がクォータを計画する際に重要な要素となります。

3. **全体の整合性**: この更新により、文書全体が整合性を持ったものとなり、利用者がクォータ制限について理解しやすくなることが期待されます。

この変更は、ユーザーがクォータの管理を行う際に必要な重要な情報を提供し、今後のサービス利用における混乱を防ぐ役割を果たします。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -31,6 +31,10 @@ Request access: [`computer-use-preview` limited access model application](https:
 
 For more information on model capabilities, and region availability see the [models documentation](./concepts/models.md#computer-use-preview).
 
+:::image type="content" source="./media/computer-use-preview.gif" alt-text="Animated gif of computer-use-preview model integrated with playwright." lightbox="./media/computer-use-preview.gif":::
+
+[Playwright integration demo code](./how-to/responses.md#computer-use).
+
 ### Provisioned spillover (preview)
 
 Spillover manages traffic fluctuations on provisioned deployments by routing overages to a designated standard deployment. To learn more about how to maximize utilization for your provisioned deployments with spillover, see [Manage traffic with spillover for provisioned deployments (preview)](./how-to/spillover-traffic-management.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能とデモの追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関する「What's New」文書に新たな情報が追加されたことを示しています。具体的には、以下の内容が更新されました。

1. **デモGIFの追加**: `computer-use-preview` モデルがプレイライトと統合された様子を示すアニメーションGIFが文書に追加されました。これにより、ユーザーはこのモデルの機能を視覚的に理解しやすくなります。

2. **デモコードのリンク**: プレイライトとの統合に関するデモコードへのリンクが追加され、ユーザーが具体的な実装例を参照できるようになりました。これにより、モデルを利用した時の実際の応用方法が明確になります。

3. **新機能の説明**: プロビジョニングされたデプロイメントに対する「スピルオーバー」機能についての説明が追加されました。この機能は、トラフィックの変動を管理するために、超過分を指定された標準デプロイメントにルーティングすることを目的としています。

これらの更新は、利用者にとって新しい機能や適用方法を理解しやすくすることを応援し、Azure OpenAI サービスの活用を促進することに寄与します。特に、ビジュアルデモや具体的なコーディング例は、ユーザーが機能を迅速に理解するのに役立ちます。


