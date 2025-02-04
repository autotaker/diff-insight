---
date: '2025-02-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:83a6833...MicrosoftDocs:89e0bdf
summary: 以下のコード変更は、主にマイナーアップデートであり、機能の追加やドキュメントの明確化、フィードバックプロセスの改善を目的としています。新機能として、「次のステップ」セクションに各種プログラミング言語のドキュメントリンクが追加されました。特に破壊的変更はありませんが、リソースとフィードバックの名称更新が行われました。その他の更新には、コードインタプリタのドキュメント修正、フィードバックボタンの名称変更、reasoning.mdのタイトル修正、地域ごとのモデル情報の更新が含まれます。このドキュメント更新は、ユーザーエクスペリエンスの向上と正確な情報提供を狙ったもので、特にリソースの把握やフィードバックプロセスの明確化、地域特化アプリケーションの構築に役立つ内容となっています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:83a6833...MicrosoftDocs:89e0bdf){target="_blank"}

# ハイライト
以下のコード変更は、主にマイナーアップデートであり、機能の追加やドキュメントの明確化、フィードバックプロセスの改善を目的としています。

## 新機能
- 「次のステップ」セクションに、.NET、Java、JavaScript、Pythonの各ドキュメントに対し、「独自データサンプルを使用したチャット開始」のリンクが追加されました。

## 破壊的変更
- 特に破壊的変更は見当たりませんが、リソースとフィードバックの名称更新がありました。

## その他の更新
- コードインタプリタに関するドキュメントの日付修正と新しいフィールド「tool_resources」の追加。
- コンテンツフィルタに関するフィードバックボタンの名称を「Send Feedback」から「Filters Feedback」に変更。
- reasonig.mdのタイトルを具体的なモデル名を含むものに修正。
- モデルマトリクス（standard-global.md）の地域ごとのモデル情報の更新。

# インサイト
今回のドキュメント更新は、ユーザーエクスペリエンスの向上と正確な情報提供を目的にしています。

まず、コードインタプリタに関するドキュメント内の「tool_resources」という新しいフィールドの追加は、ユーザーが使用可能なリソースをより簡単に把握できるようにするためのものです。これにより、コードインタプリタの効果的な利用が実現できます。また、フィードバックボタンの名称変更は、ユーザーが送信するフィードバックの内容をより明確化することが狙いで、フィルタリングプロセスの精度を高めています。

さらに、reasoning.mdの修正により、ユーザーは利用可能なモデルの選択が容易になり、Azure OpenAIのさまざまな機能を的確に活用する手助けとなります。加えて、新たに追加されたリンク群は、開発者が独自データを用いてアプリケーションを迅速に試すことを促進し、開発フローの効率化に寄与します。

最後に、モデルマトリクスにおける情報は、地域ごとのモデルサポート状況を示すことで、開発者が地域特化アプリケーションを構築する際の意思決定を支援します。これらの更新は全体として、ドキュメントの有用性と正確性を向上させ、ユーザーにとっての利便性を確保するものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [code-interpreter.md](#item-95efbd) | minor update | コードインタプリタの更新と日付の修正 | modified | 7 | 2 | 9 | 
| [content-filters.md](#item-6f0627) | minor update | フィードバックボタンの名称変更 | modified | 1 | 1 | 2 | 
| [reasoning.md](#item-a54b2f) | minor update | タイトルの修正とモデルの明確化 | modified | 1 | 1 | 2 | 
| [chatgpt-dotnet.md](#item-2563fb) | minor update | 次のステップに新しいリンクを追加 | modified | 1 | 0 | 1 | 
| [chatgpt-java.md](#item-06c77f) | minor update | 次のステップに新しいリンクを追加 | modified | 1 | 0 | 1 | 
| [chatgpt-javascript.md](#item-cbf09f) | minor update | 次のステップに新しいリンクを追加 | modified | 1 | 0 | 1 | 
| [chatgpt-python.md](#item-f1dade) | minor update | 次のステップに新しいリンクを追加 | modified | 1 | 0 | 1 | 
| [standard-global.md](#item-17a84b) | minor update | モデルマトリクスの更新 | modified | 26 | 25 | 51 | 


# Modified Contents
## articles/ai-services/openai/how-to/code-interpreter.md{#item-95efbd}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 01/28/2025
+ms.date: 02/03/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -104,7 +104,12 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/assistants?api-version=2
     "tools": [
       { "type": "code_interpreter" }
     ],
-    "model": "gpt-4-1106-preview"
+    "model": "gpt-4-1106-preview",
+    "tool_resources": {
+      "code_interpreter": {
+        "file_ids": ["assistant-123abc456"]
+      }
+    }
   }'
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コードインタプリタの更新と日付の修正"
}
```

### Explanation
この変更は、コードインタプリタに関するドキュメントの更新を含んでいます。具体的には、最初の部分で日付が「2025年1月28日」から「2025年2月3日」に修正されました。さらに、APIリクエストのサンプルコードに新しいフィールド「tool_resources」が追加され、その中に「code_interpreter」オブジェクトが含まれるようになりました。このオブジェクトには、関連付けられたファイルのID「assistant-123abc456」が設定されています。これにより、ユーザーはコードインタプリタの使用に必要なリソースを明確に理解できるようになります。この変更は、仕様の明確化を目的としたマイナーアップデートです。

## articles/ai-services/openai/how-to/content-filters.md{#item-6f0627}

<details>
<summary>Diff</summary>
````diff
@@ -51,7 +51,7 @@ You can configure the following filter categories in addition to the default har
 
 ## Report content filtering feedback
 
-If you are encountering a content filtering issue, select the **Send Feedback** button at the top of the playground. This is enabled in the **Images, Chat, and Completions** playground.  
+If you are encountering a content filtering issue, select the **Filters Feedback** button at the top of the playground. This is enabled in the **Images, Chat, and Completions** playground once you submit a prompt. 
 
 When the dialog appears, select the appropriate content filtering issue. Include as much detail as possible relating to your content filtering issue, such as the specific prompt and content filtering error you encountered. Do not include any private or sensitive information. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フィードバックボタンの名称変更"
}
```

### Explanation
この変更は、コンテンツフィルタに関するドキュメントの内容を微調整するもので、特にフィードバックボタンの名称が変更されました。具体的には、「**Send Feedback**」ボタンが「**Filters Feedback**」ボタンに改名され、その説明も若干変更されています。新しい説明では、ユーザーがプロンプトを送信した後にこのボタンが有効になることを明示しています。また、コンテンツフィルタリングに関するフィードバックを送信する際の詳細についても、変更後の文言ではより明確に指示されています。この修正は、ユーザーの理解を深め、操作の正確性を向上させることを目的としたマイナーアップデートです。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Azure OpenAI o1 series reasoning models
+title: Azure OpenAI reasoning models - o3-mini, o1, o1-mini
 titleSuffix: Azure OpenAI
 description: Learn how to use Azure OpenAI's advanced o3-mini, o1, & o1-mini reasoning models 
 manager: nitinme
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "タイトルの修正とモデルの明確化"
}
```

### Explanation
この変更は、「reasoning.md」ドキュメントのタイトルに関する修正を行ったものです。元のタイトル「Azure OpenAI o1 series reasoning models」から、より具体的な「Azure OpenAI reasoning models - o3-mini, o1, o1-mini」というタイトルに変更されました。この変更により、ユーザーは関連するモデルが明確に示され、どのモデルが利用できるかを一目で理解しやすくなっています。この修正は、文書の内容をより効果的に伝えることを目的としたマイナーアップデートです。

## articles/ai-services/openai/includes/chatgpt-dotnet.md{#item-2563fb}

<details>
<summary>Diff</summary>
````diff
@@ -125,4 +125,5 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 
 ## Next steps
 
+* [Get started with the chat using your own data sample for .NET](/dotnet/ai/get-started-app-chat-template?toc=/azure/ai-services/openai/toc.json&bc=/azure/ai-services/openai/breadcrumb/toc.json&tabs=github-codespaces)
 * For more examples, check out the [Azure OpenAI Samples GitHub repository](https://github.com/Azure-Samples/openai)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "次のステップに新しいリンクを追加"
}
```

### Explanation
この変更は、「chatgpt-dotnet.md」ドキュメントの「次のステップ」セクションに新しいリンクを追加したものです。具体的には、「.NET用の独自データサンプルを使用してチャットを開始する」ためのリンクが新たに挿入されました。このリンクは、ユーザーが提供されているリソースを使って、より具体的な実装を試す手助けをすることを目的としています。この修正は、ドキュメントの有用性を高めるためのマイナーアップデートです。

## articles/ai-services/openai/includes/chatgpt-java.md{#item-06c77f}

<details>
<summary>Diff</summary>
````diff
@@ -180,4 +180,5 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 
 ## Next steps
 
+* [Get started with the chat using your own data sample for Java](/azure/developer/java/ai/get-started-app-chat-template?toc=/azure/ai-services/openai/toc.json&bc=/azure/ai-services/openai/breadcrumb/toc.json&tabs=github-codespaces)
 * For more examples, check out the [Azure OpenAI Samples GitHub repository](https://github.com/Azure-Samples/openai)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "次のステップに新しいリンクを追加"
}
```

### Explanation
この変更は、「chatgpt-java.md」ドキュメントの「次のステップ」セクションに新しいリンクを追加したものです。具体的には、「Java用の独自データサンプルを使用してチャットを開始する」ためのリンクが新たに挿入されました。このリンクは、Javaを使用するユーザーが具体的なサンプルを活用して、より簡単にアプリケーションを開発できるようにすることを目的としています。この修正は、ドキュメントの情報量を増やし、ユーザーの利便性を向上させるためのマイナーアップデートです。

## articles/ai-services/openai/includes/chatgpt-javascript.md{#item-cbf09f}

<details>
<summary>Diff</summary>
````diff
@@ -178,4 +178,5 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 ## Next steps
 
 * [Azure OpenAI Overview](../overview.md)
+* [Get started with the chat using your own data sample for JavaScript](/azure/developer/javascript/ai/get-started-app-chat-template?toc=/azure/ai-services/openai/toc.json&bc=/azure/ai-services/openai/breadcrumb/toc.json&tabs=github-codespaces)
 * For more examples, check out the [Azure OpenAI Samples GitHub repository](https://github.com/Azure-Samples/openai)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "次のステップに新しいリンクを追加"
}
```

### Explanation
この変更は、「chatgpt-javascript.md」ドキュメントの「次のステップ」セクションに新しいリンクを追加したものです。具体的には、「JavaScript用の独自データサンプルを使用してチャットを開始する」ためのリンクが新たに挿入されました。このリンクは、JavaScriptを用いたアプリケーションの開発者が、提供されるリソースを基に実装を進めるための手助けを目的としています。この修正は、ユーザーにとっての情報の充実を図るマイナーアップデートです。

## articles/ai-services/openai/includes/chatgpt-python.md{#item-f1dade}

<details>
<summary>Diff</summary>
````diff
@@ -162,4 +162,5 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 ## Next steps
 
 * Learn more about how to work with GPT-35-Turbo and the GPT-4 models with [our how-to guide](../how-to/chatgpt.md).
+* [Get started with the chat using your own data sample for Python](/azure/developer/python/get-started-app-chat-template?toc=/azure/ai-services/openai/toc.json&bc=/azure/ai-services/openai/breadcrumb/toc.json&tabs=github-codespaces)
 * For more examples, check out the [Azure OpenAI Samples GitHub repository](https://github.com/Azure-Samples/openai)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "次のステップに新しいリンクを追加"
}
```

### Explanation
この変更は、「chatgpt-python.md」ドキュメントの「次のステップ」セクションに新たにリンクを追加したものです。具体的には、「Python用の独自データサンプルを使用してチャットを開始する」ためのリンクが挿入されました。このリンクは、Pythonを使用する開発者が、実際のサンプルを基にしてアプリケーションを構築しやすくすることを目的としています。この修正はユーザーの利便性を向上させるためのマイナーアップデートであり、資料の情報量の増加にも寄与しています。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -9,28 +9,29 @@ ms.custom: references_regions
 ms.date: 01/23/2025
 ---
 
-| **Region**     | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-10-01**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4o-audio-preview**, **2024-12-17**   |
-|:-------------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:-------------------------------------------:|:-------------------------------:|:----------------------------------------:|
-| australiaeast      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| brazilsouth        | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| canadaeast         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| eastus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| eastus2            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                            | ✅                                     |
-| francecentral      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| germanywestcentral | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| japaneast          | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| koreacentral       | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| northcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| norwayeast         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| polandcentral      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| southafricanorth   | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| southcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| southindia         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| spaincentral       | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| swedencentral      | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                            | ✅                                     |
-| switzerlandnorth   | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| uaenorth           | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| uksouth            | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| westeurope         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| westus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            | -                                    |
-| westus3            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            | -                                    |
\ No newline at end of file
+| **Region**     | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-10-01**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4o-audio-preview**, **2024-12-17**   | **gpt-4**, **turbo-2024-04-09**   |
+|:-------------------|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:-------------------------------------------:|:----------------------------------------:|:-------------------------------:|
+| australiaeast      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| brazilsouth        | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| canadaeast         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| eastus             | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| eastus2            | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                                     | ✅                            |
+| francecentral      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| germanywestcentral | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| japaneast          | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| koreacentral       | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| northcentralus     | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| norwayeast         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| polandcentral      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| southafricanorth   | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| southcentralus     | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| southindia         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| spaincentral       | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| swedencentral      | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                                     | ✅                            |
+| switzerlandnorth   | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| uaenorth           | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| uksouth            | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| westeurope         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| westus             | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+| westus3            | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | ✅                            |
+
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルマトリクスの更新"
}
```

### Explanation
この変更は、「standard-global.md」ドキュメント内のモデルマトリクスセクションにおける更新です。具体的には、地域に関連するモデル情報が新しいバージョンで更新され、さらなる詳細が追加されました。特に、利用可能なモデルの新しいリリース日やバージョンが更新され、地域ごとのサポート状況が明示されています。これにより、開発者やユーザーが各モデルの利用可能性についての最新情報を把握しやすくなり、特定の地域での実装を計画する際に役立つ情報が提供されています。この変更はマイナーアップデートに該当し、ドキュメントの正確性と関連性を向上させています。


