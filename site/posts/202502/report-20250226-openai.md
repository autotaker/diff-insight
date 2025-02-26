---
date: '2025-02-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:50dc684...MicrosoftDocs:bc33227
summary: この変更は、Azure OpenAIサービスに関する様々な文書の更新を行い、新機能として「ストアドコンプリート機能」が追加されました。これにより、コンテンツの保存や再利用が容易になり、AIアプリケーションの構築がサポートされます。また、環境変数のデフォルト値設定、モデルの退役日情報の変更、セキュリティ関連リンクの追加が行われ、ドキュメント内で多くの改善がなされています。破壊的な変更はないものの、一部変数名の変更があり、コードの互換性に影響する可能性があります。この一連の更新は、開発者の利便性とセキュリティ向上を目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:50dc684...MicrosoftDocs:bc33227){target="_blank"}

<format>
# ハイライト
この変更は、Azure OpenAIサービスに関連する複数の文書にわたる様々な更新を行っています。特に、新機能として「ストアドコンプリート機能」が追加され、他にも環境変数のデフォルト値設定、モデルの退役日情報の変更、セキュリティ関連リンクの追加などが行われています。また、新しいAPIサポートやサンプルコードの改善といった内容改善が多数含まれています。

## 新機能
- ストアドコンプリート機能に関する詳細とAPIが追加。
- JavaScriptおよびTypeScriptの環境設定が統一。

## 破壊的な変更
特に破壊的な変更はないが、デプロイIDの名称変更などの一部の変数名の変更が行われ、コードの互換性に影響を及ぼす可能性がある。

## その他の更新
- 多くのドキュメントで環境変数やエラーメッセージの改善が行われている。
- 各言語のガイドやサンプルコードの整形、更新が行われた。

# インサイト
この一連の更新は、主に開発者の利便性とセキュリティの向上を目的として行われています。まず、ストアドコンプリート機能の追加は、ユーザーがより効果的にAzure OpenAIのサービスを利用できるよう設計されています。この新機能により、コンテンツの保存や再利用が容易になり、より高度なAIアプリケーションの構築をサポートしています。

また、環境変数のデフォルト値の設定やセキュリティ情報へのアクセスが容易になったことで、ユーザーは設定を行う際の手間を軽減することが可能です。例えば、デプロイIDの名称変更は、開発中のコードにおける一貫性を確保し、将来的な誤解を避けるためのものです。

レビューと修正は、ガイドラインそのものの可読性や使い勝手の向上を目指しており、特に新しい開発者がプロジェクトに参入した際の障壁を低くするよう心がけられています。多くのドキュメントで改訂が行われ、新しく導入されたリンクや改善されたエラーメッセージがその一例です。

さらに、モデルの退役日や使用可能地域の見直しなど、ドキュメントの内容が最新の情報を反映しており、ユーザーがAzure OpenAIサービスを活用するための最適化が図られています。これにより、ユーザーは継続的に最新のサービスを享受し、効率的なAI開発が行える環境が整っています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [content-filter.md](#item-dfc7e7) | minor update | 環境変数のデフォルト値の更新 | modified | 2 | 2 | 4 | 
| [model-retirements.md](#item-03fc2e) | minor update | モデル退役の情報更新 | modified | 11 | 7 | 18 | 
| [create-resource.md](#item-c1c8a3) | minor update | Azure OpenAI セキュリティに関するリンクの追加 | modified | 1 | 0 | 1 | 
| [fine-tuning-functions.md](#item-8a03a5) | minor update | ファインチューニングの情報更新とツール呼び出しへの移行 | modified | 103 | 8 | 111 | 
| [role-based-access-control.md](#item-4b9817) | minor update | Azure OpenAI セキュリティに関するリンクの追加 | modified | 1 | 0 | 1 | 
| [stored-completions.md](#item-ccc7e6) | new feature | ストアドコンプリート機能の詳細とAPIの追加 | modified | 670 | 5 | 675 | 
| [assistants-javascript.md](#item-ad3627) | minor update | JavaScript用アシスタントのガイドの改善 | modified | 12 | 21 | 33 | 
| [assistants-typescript.md](#item-3195a9) | minor update | TypeScript用アシスタントのガイドの改善 | modified | 11 | 16 | 27 | 
| [audio-completions-javascript.md](#item-b1be01) | minor update | JavaScript用音声完了ガイドの改善 | modified | 12 | 19 | 31 | 
| [audio-completions-python.md](#item-a88047) | minor update | Python用音声完了ガイドの手順修正 | modified | 1 | 1 | 2 | 
| [audio-completions-rest.md](#item-0ec305) | minor update | REST API用音声完了ガイドの手順修正 | modified | 1 | 1 | 2 | 
| [audio-completions-typescript.md](#item-94bc1f) | minor update | TypeScript用音声完了ガイドの環境変数修正 | modified | 12 | 12 | 24 | 
| [chatgpt-javascript.md](#item-cbf09f) | minor update | JavaScript用ChatGPTガイドの手順更新 | modified | 120 | 103 | 223 | 
| [chatgpt-typescript.md](#item-6d2f1f) | minor update | TypeScript用ChatGPTガイドの手順強化 | modified | 210 | 160 | 370 | 
| [dall-e-dotnet.md](#item-755f0a) | minor update | DALL·E .NETガイドのSAS URLへの更新 | modified | 1 | 1 | 2 | 
| [dall-e-go.md](#item-132707) | minor update | DALL·E GoガイドのSAS URLへの更新 | modified | 1 | 1 | 2 | 
| [dall-e-java.md](#item-373f89) | minor update | DALL·E JavaガイドのSAS URLへの更新 | modified | 1 | 1 | 2 | 
| [dall-e-javascript.md](#item-6cffcf) | minor update | DALL·E JavaScriptガイドのSAS URLへの更新と構成の簡素化 | modified | 149 | 136 | 285 | 
| [dall-e-typescript.md](#item-57b205) | minor update | DALL·E TypeScriptガイドのSAS URLへの更新と構成手順の合理化 | modified | 180 | 126 | 306 | 
| [fine-tuning-studio.md](#item-439f1e) | minor update | クイックレスポンスチャットボットの例の追加 | modified | 10 | 3 | 13 | 
| [gpt-v-javascript.md](#item-a128c9) | minor update | JavaScriptアプリケーションの設定と実行手順の更新 | modified | 49 | 44 | 93 | 
| [gpt-v-typescript.md](#item-03ec34) | minor update | TypeScriptアプリケーションの設定手順の拡充 | modified | 89 | 49 | 138 | 
| [javascript.md](#item-f4828f) | minor update | JavaScript環境変数の設定方法の改善 | modified | 7 | 7 | 14 | 
| [datazone-standard.md](#item-188333) | minor update | モデルの地域対応状況の更新 | modified | 7 | 7 | 14 | 
| [provisioned-models.md](#item-8ee639) | minor update | 提供されたモデルの地域対応状況の更新 | modified | 27 | 27 | 54 | 
| [realtime-javascript.md](#item-3c125e) | minor update | JavaScriptファイル名と環境変数の整備 | modified | 10 | 18 | 28 | 
| [realtime-python.md](#item-1291c0) | minor update | Pythonスクリプト環境変数の改善 | modified | 3 | 3 | 6 | 
| [realtime-typescript.md](#item-eacc9c) | minor update | TypeScriptファイル名と環境変数の整備 | modified | 10 | 10 | 20 | 
| [resource-authentication.md](#item-59aece) | minor update | APIバージョン管理に関する説明の強化 | modified | 1 | 1 | 2 | 
| [text-to-speech-dotnet.md](#item-fea66a) | minor update | レビュアー情報の更新 | modified | 1 | 1 | 2 | 
| [text-to-speech-javascript.md](#item-e9b653) | minor update | JavaScriptにおけるテキスト読み上げの手順を更新 | modified | 46 | 36 | 82 | 
| [text-to-speech-rest.md](#item-d067a1) | minor update | レビュアー情報の更新 | modified | 1 | 1 | 2 | 
| [text-to-speech-typescript.md](#item-1335d5) | minor update | TypeScriptでのテキスト読み上げ手順の更新 | modified | 88 | 40 | 128 | 
| [typescript.md](#item-ee5b93) | minor update | 環境変数の使用による設定の改善 | modified | 7 | 7 | 14 | 
| [use-your-data-common-variables.md](#item-c35afc) | minor update | デプロイIDの名称修正 | modified | 2 | 2 | 4 | 
| [use-your-data-dotnet.md](#item-b811b8) | minor update | デプロイIDの名称修正 | modified | 1 | 1 | 2 | 
| [use-your-data-go.md](#item-484724) | minor update | デプロイIDの名称修正 | modified | 1 | 1 | 2 | 
| [use-your-data-javascript.md](#item-786699) | minor update | JavaScriptサンプルの更新 | modified | 45 | 37 | 82 | 
| [use-your-data-python.md](#item-3dc5e2) | minor update | デプロイメントIDの名称修正 | modified | 3 | 3 | 6 | 
| [use-your-data-rest.md](#item-d1e071) | minor update | デプロイメントIDの名称修正 | modified | 1 | 1 | 2 | 
| [use-your-data-typescript.md](#item-ec0b7e) | minor update | TypeScriptでのアプリケーションセットアップ手順の改善 | modified | 83 | 40 | 123 | 
| [whisper-javascript.md](#item-3ee990) | minor update | Whisper APIのJavaScriptサンプルコードの改善 | modified | 45 | 35 | 80 | 
| [whisper-powershell.md](#item-7db269) | minor update | Whisper PowerShell ドキュメントのレビュアー情報の更新 | modified | 1 | 1 | 2 | 
| [whisper-rest.md](#item-639ccb) | minor update | Whisper REST APIドキュメントのレビュアー情報の更新 | modified | 1 | 1 | 2 | 
| [whisper-typescript.md](#item-eafedb) | minor update | Whisper TypeScript ドキュメントの内容更新と構成の変更 | modified | 87 | 36 | 123 | 
| [text-to-speech-quickstart.md](#item-c344ad) | minor update | Text-to-Speech クイックスタートドキュメントのレビュアー情報の更新 | modified | 1 | 1 | 2 | 
| [whisper-quickstart.md](#item-4cae3d) | minor update | Whisper クイックスタートドキュメントのレビュアー情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/content-filter.md{#item-dfc7e7}

<details>
<summary>Diff</summary>
````diff
@@ -620,8 +620,8 @@ import * as dotenv from "dotenv";
 dotenv.config();
 
 // You will need to set these environment variables or edit the following values
-const endpoint = process.env["ENDPOINT"] || "<endpoint>";
-const azureApiKey = process.env["AZURE_API_KEY"] || "<api key>";
+const endpoint = process.env["ENDPOINT"] || "Your endpoint";
+const azureApiKey = process.env["AZURE_API_KEY"] || "Your API key";
 
 const messages = [
   { role: "system", content: "You are a helpful assistant. You will talk like a pirate." },
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "環境変数のデフォルト値の更新"
}
```

### Explanation
この修正では、`content-filter.md`ファイル内の環境変数に関するデフォルト値が変更されました。具体的には、`ENDPOINT`と`AZURE_API_KEY`のデフォルト値がそれぞれ`"<endpoint>"`および`"<api key>"`から`"Your endpoint"`および`"Your API key"`に変更されました。この変更により、ユーザーは環境変数の利用方法をより明確に理解でき、設定を行う際の手間が軽減されることが目的です。修正の行数は合計で4行であり、追加と削除がそれぞれ2行ずつ発生しています。

## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 02/20/2025
+ms.date: 02/25/2025
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -93,18 +93,16 @@ These models are currently available for use in Azure OpenAI Service.
 
 | Model | Version | Retirement date | Suggested replacements |
 | ---- | ---- | ---- | --- |
-| `dall-e-3` | 3 | No earlier than April 30, 2025 | |
-| `gpt-35-turbo` | 0301 | February 13, 2025<br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 21, 2025.   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
-| `gpt-35-turbo` | 0613 | February 13, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 21, 2025.  | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
+| `dall-e-3` | 3 | No earlier than June 30, 2025 | |
 | `gpt-35-turbo-16k`| 0613 | April, 30, 2025 | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
 | `gpt-35-turbo` | 1106 | No earlier than May 31, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 21, 2025. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
 | `gpt-35-turbo` | 0125 | No earlier than May 31, 2025 | `gpt-4o-mini` |
 | `gpt-4`<br>`gpt-4-32k` | 0314 | June 6, 2025 | `gpt-4o` |
 | `gpt-4`<br>`gpt-4-32k` | 0613 | June 6, 2025 | `gpt-4o` |
 | `gpt-4` | turbo-2024-04-09 | No earlier than June 6, 2025 | `gpt-4o`|
-| `gpt-4` | 1106-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than February 10, 2025 **<sup>1</sup>** <br>Retirement date: February 28, 2025  | `gpt-4o`|
-| `gpt-4` | 0125-preview |To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than February 10, 2025 **<sup>1</sup>** <br>Retirement date: February 28, 2025  | `gpt-4o` |
-| `gpt-4` | vision-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than February 10, 2025  **<sup>1</sup>** <br>Retirement date: February 28, 2025 | `gpt-4o`|
+| `gpt-4` | 1106-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than February 10, 2025 **<sup>1</sup>** <br>Retirement date: April 02, 2025  | `gpt-4o`|
+| `gpt-4` | 0125-preview |To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than February 10, 2025 **<sup>1</sup>** <br>Retirement date: April 02, 2025  | `gpt-4o` |
+| `gpt-4` | vision-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than February 10, 2025  **<sup>1</sup>** <br>Retirement date: April 02, 2025 | `gpt-4o`|
 | `gpt-4o` | 2024-05-13 | No earlier than May 20, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on February 13, 2025. | |
 | `gpt-4o` | 2024-08-06 | No earlier than August 6, 2025  | |
 | `gpt-4o` | 2024-11-20 | No earlier than November 20, 2025  | |
@@ -138,6 +136,8 @@ If you're an existing customer looking for information about these models, see [
 
 | Model | Deprecation date | Retirement date | Suggested replacement |
 | --------- | --------------------- | ------------------- | -------------------- |
+| `gpt-35-turbo` - 0301 | | February 13, 2025   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
+| `gpt-35-turbo` - 0613 | | February 13, 2025 | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
 | babbage-002 | | January 27, 2025 |  |
 | davinci-002 | | January 27, 2025 | |
 | dall-e-2|  | January 27, 2025 | dalle-3 |
@@ -171,6 +171,10 @@ If you're an existing customer looking for information about these models, see [
 
 ## Retirement and deprecation history
 
+## February 25, 2025
+
+-  `dalle-3` updated to no earlier than June 30, 2025.
+
 ## February 20, 2025
 
 - `o1-preview` updated to no earlier than April 2, 2025.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル退役の情報更新"
}
```

### Explanation
この修正は、`model-retirements.md`ファイル内のAzure OpenAIのモデルに関する退役および廃止日を更新しました。主な変更点は、`dall-e-3`の退役日が2025年4月30日から2025年6月30日に変更されたことです。さらに、GPTモデルに関する情報や、いくつかのモデルの退役日および推奨代替モデルに関する詳細が追加されました。

具体的には、以下の情報が追加および修正されました：
- `gpt-35-turbo`のモデルについて、退役日や推奨代替モデルが明示されました。
- 新たに退役と廃止の履歴が更新され、2025年2月25日に`dall-e-3`の情報が修正されたことが記載されました。

この変更により、ユーザーはモデルの退役に関する最新情報を得やすくなります。変更の合計行数は18行であり、11行の追加と7行の削除が含まれています。

## articles/ai-services/openai/how-to/create-resource.md{#item-c1c8a3}

<details>
<summary>Diff</summary>
````diff
@@ -46,6 +46,7 @@ In this article, you review examples for creating and deploying resources in the
 
 ## Next steps
 
+- [Get started with the Azure OpenAI security building block](/azure/developer/ai/get-started-securing-your-ai-app?tabs=github-codespaces&pivots=python)
 - Make API calls and generate text with [Azure OpenAI Service quickstarts](../quickstart.md).
 - Learn more about the [Azure OpenAI Service models](../concepts/models.md).
 - For information on pricing visit the [Azure OpenAI pricing page](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI セキュリティに関するリンクの追加"
}
```

### Explanation
この修正では、`create-resource.md`ファイルに新しいリンクが追加されました。具体的には、記事の「次のステップ」セクションに「Azure OpenAIセキュリティビルディングブロックを始める」というタイトルのリンクが挿入されました。このリンクは、ユーザーがAzure OpenAIに関するセキュリティ情報を得るための出発点を提供することを目的としています。

この更新により、ユーザーはリソースの作成や展開に関する情報に加えて、安全なAIアプリケーションの構築に必要な情報を簡単に見つけることができるようになります。変更の行数は1行で、追加のみが行われています。

## articles/ai-services/openai/how-to/fine-tuning-functions.md{#item-8a03a5}

<details>
<summary>Diff</summary>
````diff
@@ -1,24 +1,118 @@
 ---
 title: Fine-tuning function calls with Azure OpenAI Service
-description: Learn how to improve function calling performance with Azure OpenAI fine-tuning
+description: Learn how to improve tool calling performance with Azure OpenAI fine-tuning
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 09/05/2024
+ms.date: 02/20/2025
 author: mrbullwinkle
 ms.author: mbullwin
 ---
 
 
-# Fine-tuning and function calling
+# Fine-tuning and tool calling
 
-Models that use the chat completions API support [function calling](../how-to/function-calling.md). Unfortunately, functions defined in your chat completion calls don't always perform as expected. Fine-tuning your model with function calling examples can improve model output by enabling you to:
+Models that use the chat completions API support [tool calling](../how-to/function-calling.md). Unfortunately, functions defined in your chat completion calls don't always perform as expected. Fine-tuning your model with tool calling examples can improve model output by enabling you to:
 
 * Get similarly formatted responses even when the full function definition isn't present. (Allowing you to potentially save money on prompt tokens.)
 * Get more accurate and consistent outputs.
 
-## Constructing a training file
+> [!NOTE]
+> `function_call` and `functions` have been deprecated in favor of `tools`. 
+> It is recommended to use the `tools` parameter instead.
+
+
+## Tool calling (recommended)
+### Constructing a training file
+
+When constructing a training file of tool calling examples, you would take a function definition like this:
+
+```json
+{
+    "messages": [
+        { "role": "user", "content": "What is the weather in San Francisco?" },
+        {
+            "role": "assistant",
+            "tool_calls": [
+                {
+                    "id": "call_id",
+                    "type": "function",
+                    "function": {
+                        "name": "get_current_weather",
+                        "arguments": "{\"location\": \"San Francisco, USA\", \"format\": \"celsius\"}"
+                    }
+                }
+            ]
+        }
+    ],
+    "tools": [
+        {
+            "type": "function",
+            "function": {
+                "name": "get_current_weather",
+                "description": "Get the current weather",
+                "parameters": {
+                    "type": "object",
+                    "properties": {
+                        "location": {
+                            "type": "string",
+                            "description": "The city and country, eg. San Francisco, USA"
+                        },
+                        "format": { "type": "string", "enum": ["celsius", "fahrenheit"] }
+                    },
+                    "required": ["location", "format"]
+                }
+            }
+        }
+    ]
+}
+```
+
+And express the information as a single line within your `.jsonl` training file as below:
+
+```jsonl
+{"messages":[{"role":"user","content":"What is the weather in San Francisco?"},{"role":"assistant","tool_calls":[{"id":"call_id","type":"function","function":{"name":"get_current_weather","arguments":"{\"location\": \"San Francisco, USA\", \"format\": \"celsius\"}"}}]}],"tools":[{"type":"function","function":{"name":"get_current_weather","description":"Get the current weather","parameters":{"type":"object","properties":{"location":{"type":"string","description":"The city and country, eg. San Francisco, USA"},"format":{"type":"string","enum":["celsius","fahrenheit"]}},"required":["location","format"]}}}]}
+```
+
+As with all fine-tuning training your example file requires at least 10 examples.
+
+### Optimize for cost
+
+OpenAI recommends that if you're trying to optimize to use fewer prompt tokens post fine-tuning your model on the full function definitions you can experiment with:
+
+* Omit function and parameter descriptions: remove the description field from function and parameters.
+* Omit parameters: remove the entire properties field from the parameters object.
+* Omit function entirely: remove the entire function object from the functions array.
+
+### Optimize for quality
+
+Alternatively, if you're trying to improve the quality of the tool calling output, it's recommended that the function definitions present in the fine-tuning training dataset and subsequent chat completion calls remain identical.
+
+### Customize model responses to function outputs
+
+Fine-tuning based on tool calling examples can also be used to improve the model's response to function outputs. To accomplish this, you include examples consisting of function response messages and assistant response messages where the function response is interpreted and put into context by the assistant.
+
+```json
+{
+    "messages": [
+        {"role": "user", "content": "What is the weather in San Francisco?"},
+        {"role": "assistant", "tool_calls": [{"id": "call_id", "type": "function", "function": {"name": "get_current_weather", "arguments": "{\"location\": \"San Francisco, USA\", \"format\": \"celsius\"}"}}]}
+        {"role": "tool", "tool_call_id": "call_id", "content": "21.0"},
+        {"role": "assistant", "content": "It is 21 degrees celsius in San Francisco, CA"}
+    ],
+    "tools": [] // same as before
+}
+```
+
+As with the example before, this example is artificially expanded for readability. The actual entry in the `.jsonl` training file would be a single line:
+
+```jsonl
+{"messages":[{"role":"user","content":"What is the weather in San Francisco?"},{"role":"assistant","tool_calls":[{"id":"call_id","type":"function","function":{"name":"get_current_weather","arguments":"{\"location\": \"San Francisco, USA\", \"format\": \"celsius\"}"}}]},{"role":"tool","tool_call_id":"call_id","content":"21.0"},{"role":"assistant","content":"It is 21 degrees celsius in San Francisco, CA"}],"tools":[]}
+```
+
+## Function calling
+### Constructing a training file
 
 When constructing a training file of function calling examples, you would take a function definition like this:
 
@@ -51,19 +145,19 @@ And express the information as a single line within your `.jsonl` training file
 
 As with all fine-tuning training your example file requires at least 10 examples.
 
-## Optimize for cost
+### Optimize for cost
 
 OpenAI recommends that if you're trying to optimize to use fewer prompt tokens post fine-tuning your model on the full function definitions you can experiment with:
 
 * Omit function and parameter descriptions: remove the description field from function and parameters.
 * Omit parameters: remove the entire properties field from the parameters object.
 * Omit function entirely: remove the entire function object from the functions array.
 
-## Optimize for quality
+### Optimize for quality
 
 Alternatively, if you're trying to improve the quality of the function calling output, it's recommended that the function definitions present in the fine-tuning training dataset and subsequent chat completion calls remain identical.
 
-## Customize model responses to function outputs
+### Customize model responses to function outputs
 
 Fine-tuning based on function calling examples can also be used to improve the model's response to function outputs. To accomplish this, you include examples consisting of function response messages and assistant response messages where the function response is interpreted and put into context by the assistant.
 
@@ -85,6 +179,7 @@ As with the example before, this example is artificially expanded for readabilit
 {"messages": [{"role": "user", "content": "What is the weather in San Francisco?"}, {"role": "assistant", "function_call": {"name": "get_current_weather", "arguments": "{\"location\": \"San Francisco, USA\", \"format\": \"celcius\"}"}}, {"role": "function", "name": "get_current_weather", "content": "21.0"}, {"role": "assistant", "content": "It is 21 degrees celsius in San Francisco, CA"}], "functions": []}
 ```
 
+
 ## Next steps
 
 * [Function calling fine-tuning scenarios](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/fine-tuning-with-function-calling-on-azure-openai-service/ba-p/4065968).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングの情報更新とツール呼び出しへの移行"
}
```

### Explanation
この修正では、`fine-tuning-functions.md`ファイルが大幅に更新され、特に「ファインチューニング」に関する情報が「ツール呼び出し」という用語に変更されました。この変更は、Azure OpenAIサービスの機能をより明確に反映させるために行われました。

主な変更内容は以下の通りです：

1. **タイトルと説明の変更**: 記事のタイトルと説明が「ファインチューニング関数呼び出し」から「ファインチューニングツール呼び出し」に更新されました。また、推奨される構成に関する具体的な情報や、ツール呼び出しのサポートも強調されています。

2. **トレーニングファイルの構成**: ツール呼び出しの事例を構築する手法が詳細に説明され、新たなサンプルコードが追加されました。これにより、ユーザーはファインチューニングに必要なツール呼び出しの構造をより理解しやすくなります。

3. **最適化の勧告**: コストの削減と品質の向上に関する推奨事項が、それぞれのセクションとして整理されました。

4. **次のステップ**: 追加情報として、「ファインチューニングの機能呼び出しシナリオ」のリンクも挿入されています。

全体で103行が追加され、8行が削除され、内容が大幅に強化されました。この改善により、ユーザーはツール呼び出しを通じてモデルをより効果的にファインチューニングする方法を学ぶことができます。

## articles/ai-services/openai/how-to/role-based-access-control.md{#item-4b9817}

<details>
<summary>Diff</summary>
````diff
@@ -208,5 +208,6 @@ Possible reasons why the user may **not** have permissions:
 
 ## Next steps
 
+- [Get started with the Azure OpenAI security building block](/azure/developer/ai/get-started-securing-your-ai-app?tabs=github-codespaces&pivots=python)
 - Learn more about [Azure-role based access control (Azure RBAC)](/azure/role-based-access-control/).
 - Also check out[assign Azure roles using the Azure portal](/azure/role-based-access-control/role-assignments-portal).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI セキュリティに関するリンクの追加"
}
```

### Explanation
この修正では、`role-based-access-control.md`ファイルに新たにセキュリティ関連のリンクが追加されました。具体的には、「次のステップ」セクションに「Azure OpenAIセキュリティビルディングブロックを始める」というリンクが挿入されました。このリンクは、Azure OpenAIのセキュリティに関する情報を提供し、ユーザーが安全にAIアプリケーションを構築する際の出発点となることを目的としています。

これにより、ユーザーは役割ベースのアクセス制御に関する情報に加えて、Azure OpenAIのセキュリティに特化したリソースを簡単に見つけることができるようになります。変更は1行の追加のみで、他に削除はありません。最大限に活用できる情報の提供がなされたことが強調されています。

## articles/ai-services/openai/how-to/stored-completions.md{#item-ccc7e6}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
 ms.custom: references_regions
-ms.date: 02/24/2025
+ms.date: 02/25/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -20,7 +20,7 @@ Stored completions allow you to capture the conversation history from chat compl
 
 ### API support
 
-Support first added in `2024-10-01-preview`
+Support first added in `2024-10-01-preview`, use `2025-02-01-preview` or later for access to the latest features.
 
 ### Deployment type
 
@@ -38,7 +38,6 @@ Currently only `Standard` model deployments support stored completions.
 
 To enable stored completions for your Azure OpenAI deployment set the `store` parameter to `True`. Use the `metadata` parameter to enrich your stored completion dataset with additional information.
 
-
 # [Python (Microsoft Entra ID)](#tab/python-secure)
 
 ```python
@@ -53,7 +52,7 @@ token_provider = get_bearer_token_provider(
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   azure_ad_token_provider=token_provider,
-  api_version="2024-10-01-preview"
+  api_version="2025-02-01-preview"
 )
 
 completion = client.chat.completions.create(
@@ -85,7 +84,7 @@ from openai import AzureOpenAI
     
 client = AzureOpenAI(
     api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-    api_version="2024-10-01-preview",
+    api_version="2025-02-01-preview",
     azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
     )
 
@@ -105,6 +104,149 @@ ompletion = client.chat.completions.create(
 
 print(completion.choices[0].message)
 ```
+
+# [REST API](#tab/rest-api)
+
+### Microsoft Entra ID
+
+```bash
+curl $AZURE_OPENAI_ENDPOINT/openai/deployments/gpt-4o/chat/completions?api-version=2025-02-01-preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+  -d '{
+    "model": "gpt-4o",
+    "store": True,
+    "messages": [
+      {
+        "role": "system",
+        "content": "You are a helpful assistant."
+      },
+      {
+        "role": "user",
+        "content": "Hello!"
+      }
+    ]
+  }'
+```
+
+### API Key
+
+```bash
+curl $AZURE_OPENAI_ENDPOINT/openai/deployments/gpt-4o/chat/completions?api-version=2025-02-01-preview \
+  -H "Content-Type: application/json" \
+  -H "api-key: $AZURE_OPENAI_API_KEY" \
+  -d '{
+    "model": "gpt-4o",
+    "store": True,
+    "messages": [
+      {
+        "role": "system",
+        "content": "You are a helpful assistant."
+      },
+      {
+        "role": "user",
+        "content": "Hello!"
+      }
+    ]
+  }'
+```
+
+# [Output](#tab/output)
+
+```json
+{
+  "id": "chatcmpl-B4eQ716S5wGUyFpGgX2MXnJEC5AW5",
+  "choices": [
+    {
+      "finish_reason": "stop",
+      "index": 0,
+      "logprobs": null,
+      "message": {
+        "content": "Ensemble methods enhance machine learning performance by combining multiple models to create a more robust and accurate predictor. The key techniques include:\n\n1. **Bagging (Bootstrap Aggregating)**: Involves training multiple models on random subsets of the data to reduce variance and overfitting. A popular method within bagging is Random Forests, which build numerous decision trees using random subsets of features and data samples.\n\n2. **Boosting**: Focuses on sequentially training models, where each new model attempts to correct the errors made by previous ones. Gradient Boosting is a common boosting technique that builds trees sequentially, concentrating on the mistakes of earlier trees to improve accuracy.\n\n3. **Stacking**: Uses a meta-model to combine predictions from various base models, leveraging their strengths to enhance overall predictions.\n\nThese ensemble methods generally outperform individual models because they effectively handle overfitting, reduce variance, and capture diverse aspects of the data. In practical applications, they are valued for their ability to improve model accuracy and stability.",
+        "refusal": null,
+        "role": "assistant",
+        "audio": null,
+        "function_call": null,
+        "tool_calls": null
+      },
+      "content_filter_results": {
+        "hate": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "protected_material_code": {
+          "filtered": false,
+          "detected": false
+        },
+        "protected_material_text": {
+          "filtered": false,
+          "detected": false
+        },
+        "self_harm": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "sexual": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "violence": {
+          "filtered": false,
+          "severity": "safe"
+        }
+      }
+    }
+  ],
+  "created": 1740448387,
+  "model": "gpt-4o-2024-08-06",
+  "object": "chat.completion",
+  "service_tier": null,
+  "system_fingerprint": "fp_b705f0c291",
+  "usage": {
+    "completion_tokens": 205,
+    "prompt_tokens": 157,
+    "total_tokens": 362,
+    "completion_tokens_details": {
+      "accepted_prediction_tokens": 0,
+      "audio_tokens": 0,
+      "reasoning_tokens": 0,
+      "rejected_prediction_tokens": 0
+    },
+    "prompt_tokens_details": {
+      "audio_tokens": 0,
+      "cached_tokens": 0
+    }
+  },
+  "prompt_filter_results": [
+    {
+      "prompt_index": 0,
+      "content_filter_results": {
+        "hate": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "jailbreak": {
+          "filtered": false,
+          "detected": false
+        },
+        "self_harm": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "sexual": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "violence": {
+          "filtered": false,
+          "severity": "safe"
+        }
+      }
+    }
+  ]
+}
+```
+
 ---
 
 Once stored completions are enabled for an Azure OpenAI deployment, they'll begin to show up in the [Azure AI Foundry portal](https://oai.azure.com) in the **Stored Completions** pane.
@@ -161,6 +303,529 @@ Stored completions can be used as a dataset for running evaluations.
 
 To learn more about evaluation see, [getting started with evaluations](./evaluations.md)
 
+## Stored completions API
+
+To access the stored completions API commands you may need to upgrade your version of the OpenAI library.
+
+```cmd
+pip install --upgrade openai
+```
+
+### List stored completions
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
+
+Additional parameters:
+
+* `metadata`: Filter by the key/value pair in the stored completions
+* `after`: Identifier for the last stored completion message from the previous pagination request.
+* `limit`: Number of stored completions messages to retrieve.
+* `order`: Order of the results by index (ascending or descending).
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
+  azure_endpoint = "https://YOUR-RESOURCE-NAME.openai.azure.com", 
+  azure_ad_token_provider=token_provider,
+  api_version="2025-02-01-preview"
+)
+
+response = client.chat.completions.list()
+
+print(response.model_dump_json(indent=2))
+```
+
+# [Python (API Key)](#tab/python-key)
+
+```python
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+  azure_endpoint = "https://YOUR-RESOURCE-NAME.openai.azure.com", 
+  api_key=os.getenv("AZURE_OPENAI_API_KEY"), 
+  api_version="2025-02-01-preview"
+)
+
+response = client.chat.completions.list()
+
+print(response.model_dump_json(indent=2))
+```
+
+# [REST API](#tab/rest-api)
+
+### Microsoft Entra ID
+
+```bash
+curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/chat/completions?api-version=2025-02-01-preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+```
+
+### API Key
+
+```bash
+curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/chat/completions?api-version=2025-02-01-preview \
+  -H "Content-Type: application/json" \
+  -H "api-key: $AZURE_OPENAI_API_KEY" \
+```
+
+# [Output](#tab/output)
+
+```json
+{
+  "data": [
+    {
+      "id": "chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u",
+      "choices": [
+        {
+          "finish_reason": null,
+          "index": 0,
+          "logprobs": null,
+          "message": {
+            "content": "Ensemble methods enhance machine learning performance by combining multiple models to create a more robust and accurate predictor. The key techniques include:\n\n1. **Bagging (Bootstrap Aggregating):** This involves training models on random subsets of the data to reduce variance and prevent overfitting. Random Forests, a popular bagging method, build multiple decision trees using random feature subsets, leading to robust predictions.\n\n2. **Boosting:** This sequential approach trains models to correct the errors of their predecessors, thereby focusing on difficult-to-predict data points. Gradient Boosting is a common implementation that sequentially builds decision trees, each improving upon the prediction errors of the previous ones.\n\n3. **Stacking:** This technique uses a meta-model to combine the predictions of multiple base models, leveraging their diverse strengths to enhance overall prediction accuracy.\n\nThe practical implications of ensemble methods include achieving superior model performance compared to single models by capturing various data patterns and reducing overfitting and variance. These methods are widely used in applications where high accuracy and model reliability are critical.",
+            "refusal": null,
+            "role": "assistant",
+            "audio": null,
+            "function_call": null,
+            "tool_calls": null
+          }
+        }
+      ],
+      "created": 1740447656,
+      "model": "gpt-4o-2024-08-06",
+      "object": null,
+      "service_tier": null,
+      "system_fingerprint": "fp_b705f0c291",
+      "usage": {
+        "completion_tokens": 208,
+        "prompt_tokens": 157,
+        "total_tokens": 365,
+        "completion_tokens_details": null,
+        "prompt_tokens_details": null
+      },
+      "request_id": "0000aaaa-11bb-cccc-dd22-eeeeee333333",
+      "seed": -430976584126747957,
+      "top_p": 1,
+      "temperature": 1,
+      "presence_penalty": 0,
+      "frequency_penalty": 0,
+      "metadata": {
+        "user": "admin",
+        "category": "docs-test"
+      }
+    }
+  ],
+  "has_more": false,
+  "object": "list",
+  "total": 1,
+  "first_id": "chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u",
+  "last_id": "chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u"
+}
+```
+
+---
+
+### Get stored completion
+
+Get stored completion by ID.
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
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
+  azure_endpoint = "https://YOUR-RESOURCE-NAME.openai.azure.com/", 
+  azure_ad_token_provider=token_provider,
+  api_version="2025-02-01-preview"
+)
+
+response = client.chat.completions.retrieve("chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u")
+
+print(response.model_dump_json(indent=2))
+```
+
+# [Python (API Key)](#tab/python-key)
+
+```python
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+  azure_endpoint = "https://YOUR-RESOURCE-NAME.openai.azure.com", 
+  api_key=os.getenv("AZURE_OPENAI_API_KEY"), 
+  api_version="2025-02-01-preview"
+)
+
+response = client.chat.completions.retrieve("chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u")
+
+print(response.model_dump_json(indent=2))
+```
+
+# [REST API](#tab/rest-api)
+
+### Microsoft Entra ID
+
+```bash
+curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/chat/completions/chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u?api-version=2025-02-01-preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+```
+
+### API Key
+
+```bash
+curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/chat/completions/chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u?api-version=2025-02-01-preview \
+  -H "Content-Type: application/json" \
+  -H "api-key: $AZURE_OPENAI_API_KEY" \
+```
+
+# [Output](#tab/output)
+
+```json
+{
+  "id": "chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u",
+  "choices": [
+    {
+      "finish_reason": null,
+      "index": 0,
+      "logprobs": null,
+      "message": {
+        "content": "Ensemble methods enhance machine learning performance by combining multiple models to create a more robust and accurate predictor. The key techniques include:\n\n1. **Bagging (Bootstrap Aggregating):** This involves training models on random subsets of the data to reduce variance and prevent overfitting. Random Forests, a popular bagging method, build multiple decision trees using random feature subsets, leading to robust predictions.\n\n2. **Boosting:** This sequential approach trains models to correct the errors of their predecessors, thereby focusing on difficult-to-predict data points. Gradient Boosting is a common implementation that sequentially builds decision trees, each improving upon the prediction errors of the previous ones.\n\n3. **Stacking:** This technique uses a meta-model to combine the predictions of multiple base models, leveraging their diverse strengths to enhance overall prediction accuracy.\n\nThe practical implications of ensemble methods include achieving superior model performance compared to single models by capturing various data patterns and reducing overfitting and variance. These methods are widely used in applications where high accuracy and model reliability are critical.",
+        "refusal": null,
+        "role": "assistant",
+        "audio": null,
+        "function_call": null,
+        "tool_calls": null
+      }
+    }
+  ],
+  "created": 1740447656,
+  "model": "gpt-4o-2024-08-06",
+  "object": "chat.completion",
+  "service_tier": null,
+  "system_fingerprint": "fp_b705f0c291",
+  "usage": {
+    "completion_tokens": 208,
+    "prompt_tokens": 157,
+    "total_tokens": 365,
+    "completion_tokens_details": null,
+    "prompt_tokens_details": null
+  },
+  "request_id": "0000aaaa-11bb-cccc-dd22-eeeeee333333",
+  "seed": -430976584126747957,
+  "top_p": 1,
+  "temperature": 1,
+  "presence_penalty": 0,
+  "frequency_penalty": 0,
+  "metadata": {
+    "user": "admin",
+    "category": "docs-test"
+  }
+}
+```
+
+---
+
+### Get stored chat completion messages
+
+Additional parameters:
+
+* `after`: Identifier for the last stored completion message from the previous pagination request.
+* `limit`: Number of stored completions messages to retrieve.
+* `order`: Order of the results by index (ascending or descending).
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
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
+  azure_endpoint = "https://YOUR-RESOURCE-NAME.openai.azure.com/", 
+  azure_ad_token_provider=token_provider,
+  api_version="2025-02-01-preview"
+)
+
+response = client.chat.completions.messages.list("chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u", limit=2)
+
+print(response.model_dump_json(indent=2))
+```
+
+# [Python (API Key)](#tab/python-key)
+
+```python
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+  azure_endpoint = "https://YOUR-RESOURCE-NAME.openai.azure.com", 
+  api_key=os.getenv("AZURE_OPENAI_API_KEY"), 
+  api_version="2025-02-01-preview"
+)
+
+response = client.chat.completions.messages.list("chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u", limit=2)
+
+print(response.model_dump_json(indent=2))
+```
+
+# [REST API](#tab/rest-api)
+
+### Microsoft Entra ID
+
+```bash
+curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/chat/completions/chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u/messages?api-version=2025-02-01-preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+```
+
+### API Key
+
+```bash
+curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/chat/completions/chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u/messages?api-version=2025-02-01-preview \
+  -H "Content-Type: application/json" \
+  -H "api-key: $AZURE_OPENAI_API_KEY" \
+```
+
+# [Output](#tab/output)
+
+```json
+{
+  "data": [
+    {
+      "content": "Provide a clear and concise summary of the technical content, highlighting key concepts and their relationships. Focus on the main ideas and practical implications.",
+      "refusal": null,
+      "role": "system",
+      "audio": null,
+      "function_call": null,
+      "tool_calls": null,
+      "id": "chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u-0"
+    },
+    {
+      "content": "Ensemble methods combine multiple machine learning models to create a more robust and accurate predictor. Common techniques include bagging (training models on random subsets of data), boosting (sequentially training models to correct previous errors), and stacking (using a meta-model to combine base model predictions). Random Forests, a popular bagging method, create multiple decision trees using random feature subsets. Gradient Boosting builds trees sequentially, with each tree focusing on correcting the errors of previous trees. These methods often achieve better performance than single models by reducing overfitting and variance while capturing different aspects of the data.",
+      "refusal": null,
+      "role": "user",
+      "audio": null,
+      "function_call": null,
+      "tool_calls": null,
+      "id": "chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u-1"
+    }
+  ],
+  "has_more": false,
+  "object": "list",
+  "total": 2,
+  "first_id": "chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u-0",
+  "last_id": "chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u-1"
+}
+```
+
+---
+
+### Update stored chat completion
+
+Add metadata key:value pairs to an existing stored completion.
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
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
+  azure_endpoint = "https://YOUR-RESOURCE-NAME.openai.azure.com/", 
+  azure_ad_token_provider=token_provider,
+  api_version="2025-02-01-preview"
+)
+
+response = client.chat.completions.update(
+    "chatcmpl-C2dE3fH4iJ5kL6mN7oP8qR9sT0uV1w",
+    metadata={"fizz": "buzz"}
+)
+
+print(response.model_dump_json(indent=2))
+```
+
+# [Python (API Key)](#tab/python-key)
+
+```python
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+  azure_endpoint = "https://YOUR-RESOURCE-NAME.openai.azure.com", 
+  api_key=os.getenv("AZURE_OPENAI_API_KEY"), 
+  api_version="2025-02-01-preview"
+)
+
+response = client.chat.completions.update(
+    "chatcmpl-C2dE3fH4iJ5kL6mN7oP8qR9sT0uV1w",
+    metadata={"fizz": "buzz"}
+)
+
+print(response.model_dump_json(indent=2))
+```
+
+# [REST API](#tab/rest-api)
+
+### Microsoft Entra ID
+
+```bash
+curl -X https://YOUR-RESOURCE-NAME.openai.azure.com/openai/chat/completions/chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u?api-version=2025-02-01-preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN"
+  -d '{
+    "metadata": {
+      "fizz": "buzz"
+    }
+  }' 
+```
+
+### API Key
+
+```bash
+curl -X https://YOUR-RESOURCE-NAME.openai.azure.com/openai/chat/completions/chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u?api-version=2025-02-01-preview \
+  -H "Content-Type: application/json" \
+  -H "api-key: $AZURE_OPENAI_API_KEY" 
+  -d '{
+    "metadata": {
+      "fizz": "buzz"
+    }
+  }'
+```
+
+# [Output](#tab/output)
+
+```json
+  "id": "chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u",
+  "choices": [
+    {
+      "finish_reason": null,
+      "index": 0,
+      "logprobs": null,
+      "message": {
+        "content": "Ensemble methods enhance machine learning performance by combining multiple models to create a more robust and accurate predictor. The key techniques include:\n\n1. **Bagging (Bootstrap Aggregating):** This involves training models on random subsets of the data to reduce variance and prevent overfitting. Random Forests, a popular bagging method, build multiple decision trees using random feature subsets, leading to robust predictions.\n\n2. **Boosting:** This sequential approach trains models to correct the errors of their predecessors, thereby focusing on difficult-to-predict data points. Gradient Boosting is a common implementation that sequentially builds decision trees, each improving upon the prediction errors of the previous ones.\n\n3. **Stacking:** This technique uses a meta-model to combine the predictions of multiple base models, leveraging their diverse strengths to enhance overall prediction accuracy.\n\nThe practical implications of ensemble methods include achieving superior model performance compared to single models by capturing various data patterns and reducing overfitting and variance. These methods are widely used in applications where high accuracy and model reliability are critical.",
+        "refusal": null,
+        "role": "assistant",
+        "audio": null,
+        "function_call": null,
+        "tool_calls": null
+      }
+    }
+  ],
+  "created": 1740447656,
+  "model": "gpt-4o-2024-08-06",
+  "object": "chat.completion",
+  "service_tier": null,
+  "system_fingerprint": "fp_b705f0c291",
+  "usage": {
+    "completion_tokens": 208,
+    "prompt_tokens": 157,
+    "total_tokens": 365,
+    "completion_tokens_details": null,
+    "prompt_tokens_details": null
+  },
+  "request_id": "0000aaaa-11bb-cccc-dd22-eeeeee333333",
+  "seed": -430976584126747957,
+  "top_p": 1,
+  "temperature": 1,
+  "presence_penalty": 0,
+  "frequency_penalty": 0,
+  "metadata": {
+    "user": "admin",
+    "category": "docs-test"
+    "fizz": "buzz"
+  }
+}
+```
+
+---
+
+### Delete stored chat completion
+
+Delete stored completion by completion ID.
+
+### Microsoft Entra ID
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
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
+  azure_endpoint = "https://YOUR-RESOURCE-NAME.openai.azure.com/", 
+  azure_ad_token_provider=token_provider,
+  api_version="2025-02-01-preview"
+)
+
+response = client.chat.completions.delete("chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u")
+
+print(response.model_dump_json(indent=2))
+
+```
+
+# [Python (API Key)](#tab/python-key)
+
+```python
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+  azure_endpoint = "https://YOUR-RESOURCE-NAME.openai.azure.com", 
+  api_key=os.getenv("AZURE_OPENAI_API_KEY"), 
+  api_version="2025-02-01-preview"
+)
+
+response = client.chat.completions.delete("chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u")
+
+print(response.model_dump_json(indent=2))
+```
+
+# [REST API](#tab/rest-api)
+
+```bash
+curl -X DELETE -D - https://YOUR-RESOURCE-NAME.openai.azure.com/openai/chat/completions/chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u?api-version=2025-02-01-preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN"
+```
+
+### API Key
+
+```bash
+curl -X DELETE -D - https://YOUR-RESOURCE-NAME.openai.azure.com/openai/chat/completions/chatcmpl-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u?api-version=2025-02-01-preview \
+  -H "Content-Type: application/json" \
+  -H "api-key: $AZURE_OPENAI_API_KEY" 
+```
+
+# [Output](#tab/output)
+
+```json
+"id"• "chatcmp1-A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u", 
+"deleted": true, 
+"object": "chat. completion. deleted" 
+```
+
+---
+
 ## Troubleshooting
 
 ### Do I need special permissions to use stored completions?
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ストアドコンプリート機能の詳細とAPIの追加"
}
```

### Explanation
この修正では、`stored-completions.md`ファイルが大幅に更新され、ストアドコンプリート機能に関する詳細が追加されました。具体的には、670行の情報が新たに追加され、ストアドコンプリートを使用するためのAPIコマンドや実装例が含まれています。

主な変更内容は以下の通りです：

1. **APIサポートの更新**: 新しいAPIバージョンである`2025-02-01-preview`を使って、最新の機能へのアクセスが提供されることが明記されています。

2. **ストアドコンプリートAPIの詳細**: ストアドコンプリートデータを取得するための新しいAPIコマンドが追加され、PythonコードとREST APIの例が豊富に提供されています。これによって、ユーザーは自分のアプリケーションでストアドコンプリートを容易に利用できるようになります。

3. **メタデータの追加**: ストアドコンプリートにメタデータを追加する方法や、保存されたコンプリートを取得するための様々なパラメータが紹介されています。

4. **トラブルシューティングのセクション**: ストアドコンプリート機能を使用するために特別な権限が必要かどうかについての情報も追加されています。

これらの変更によって、ユーザーはストアドコンプリートの機能をより効果的に活用できるようになり、関連APIの使用方法を明確に理解することができます。全体的に、ストアドコンプリート機能の説明が充実し、実装への道筋が譲歩されています。

## articles/ai-services/openai/includes/assistants-javascript.md{#item-ad3627}

<details>
<summary>Diff</summary>
````diff
@@ -33,24 +33,17 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create a new folder `assistants-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
     ```shell
-    mkdir assistants-quickstart && code assistants-quickstart
+    mkdir assistants-quickstart && cd assistants-quickstart
     ```
     
 
 1. Create the `package.json` with the following command:
 
     ```shell
     npm init -y
-    ```
-
-1. Update the `package.json` to ECMAScript with the following command: 
-
-    ```shell
-    npm pkg set type=module
-    ```
-    
+    ```   
 
-1. Install the OpenAI Assistants client library for JavaScript with:
+1. Install the OpenAI client library for JavaScript with:
 
     ```console
     npm install openai
@@ -100,14 +93,14 @@ An individual assistant can access up to 128 tools including `code interpreter`,
     } = require("@azure/identity");
     
     // Get environment variables
-    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT;
-    const azureOpenAIDeployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME;
-    const azureOpenAIVersion = process.env.OPENAI_API_VERSION;
+    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const azureOpenAIDeployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "Your deployment name";
+    const azureOpenAIVersion = process.env.OPENAI_API_VERSION || "A supported API version";
     
     // Check env variables
     if (!azureOpenAIEndpoint || !azureOpenAIDeployment || !azureOpenAIVersion) {
       throw new Error(
-        "Please ensure to set AZURE_OPENAI_DEPLOYMENT_NAME and AZURE_OPENAI_ENDPOINT in your environment variables."
+        "You need to set the endpoint, deployment name, and API version."
       );
     }
     
@@ -193,8 +186,6 @@ An individual assistant can access up to 128 tools including `code interpreter`,
     node index.js
     ```
 
-
-
 #### [API key](#tab/api-key)
 
 1. Create the `index.js` file with the following code:
@@ -203,15 +194,15 @@ An individual assistant can access up to 128 tools including `code interpreter`,
     const { AzureOpenAI } = require("openai");
     
     // Get environment variables
-    const azureOpenAIKey = process.env.AZURE_OPENAI_KEY;
-    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT;
-    const azureOpenAIDeployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME;
-    const azureOpenAIVersion = process.env.OPENAI_API_VERSION;
+    const azureOpenAIKey = process.env.AZURE_OPENAI_KEY || "Your API key";
+    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const azureOpenAIDeployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "Your deployment name";
+    const azureOpenAIVersion = process.env.OPENAI_API_VERSION || "A supported API version";
     
     // Check env variables
     if (!azureOpenAIKey || !azureOpenAIEndpoint || !azureOpenAIDeployment || !azureOpenAIVersion) {
       throw new Error(
-        "Please set AZURE_OPENAI_KEY and AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_DEPLOYMENT_NAME in your environment variables."
+        "You need to set the endpoint, deployment name, and API version."
       );
     }
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript用アシスタントのガイドの改善"
}
```

### Explanation
この修正では、`assistants-javascript.md`ファイルが更新され、JavaScriptにおけるアシスタントの利用に関するガイドラインが改善されました。以下は主な変更点です：

1. **環境変数のデフォルト値設定**: 以前は必要な環境変数を設定するための説明が明確でなかったが、現在ではすべての環境変数に対してデフォルト値が指定されています。これにより、APIのエンドポイント、デプロイメント名、およびAPIバージョンの設定がよりユーザーフレンドリーになります。

2. **テキストの簡潔化**: 一部の手順が簡潔になり、必要なコマンドの記述が明確化されました。例えば、`package.json`の初期化およびOpenAIクライアントライブラリのインストールの手順が簡素化されています。

3. **エラーメッセージの改善**: 環境変数が設定されていない場合のエラーメッセージが更新され、何が必要なのかをよりわかりやすく示すようになりました。

4. **コードの整形**: 不要な空行が削除され、全体的にスッキリとした印象に改善されています。

この修正によって、ユーザーはJavaScript用アシスタントを利用する際の手順をより簡単に理解しやすくなり、環境の設定も容易になります。全体として、ドキュメントの可読性と使用体験が向上しました。

## articles/ai-services/openai/includes/assistants-typescript.md{#item-3195a9}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create a new folder `assistants-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
     ```shell
-    mkdir assistants-quickstart && code assistants-quickstart
+    mkdir assistants-quickstart && cd assistants-quickstart
     ```
     
 
@@ -51,7 +51,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     ```
     
 
-1. Install the OpenAI Assistants client library for JavaScript with:
+1. Install the OpenAI client library for JavaScript with:
 
     ```console
     npm install openai
@@ -110,15 +110,15 @@ An individual assistant can access up to 128 tools including `code interpreter`,
     } from "@azure/identity";
     
     // Get environment variables
-    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT as string;
+    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint" as string;
     const azureOpenAIDeployment = process.env
-      .AZURE_OPENAI_DEPLOYMENT_NAME as string;
-    const openAIVersion = process.env.OPENAI_API_VERSION as string;
+      .AZURE_OPENAI_DEPLOYMENT_NAME  || "Your deployment name" as string;
+    const openAIVersion = process.env.OPENAI_API_VERSION || "A supported API version" as string;
     
     // Check env variables
     if (!azureOpenAIEndpoint || !azureOpenAIDeployment || !openAIVersion) {
       throw new Error(
-        "Please ensure to set AZURE_OPENAI_DEPLOYMENT_NAME and AZURE_OPENAI_ENDPOINT in your environment variables."
+        "You need to set the endpoint, deployment name, and API version."
       );
     }
     
@@ -186,8 +186,6 @@ An individual assistant can access up to 128 tools including `code interpreter`,
       }
     }
     ```
-    
-
 
 1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
 
@@ -222,8 +220,6 @@ An individual assistant can access up to 128 tools including `code interpreter`,
     node index.js
     ```
 
-
-
 #### [API key](#tab/typescript-key)
 
 1. Create the `index.ts` file with the following code:
@@ -240,16 +236,16 @@ An individual assistant can access up to 128 tools including `code interpreter`,
     import { Thread } from "openai/resources/beta/threads/threads";
     
     // Get environment variables
-    const azureOpenAIKey = process.env.AZURE_OPENAI_KEY as string;
-    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT as string;
+    const azureOpenAIKey = process.env.AZURE_OPENAI_KEY || "Your API key" as string;
+    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint" as string;
     const azureOpenAIDeployment = process.env
-      .AZURE_OPENAI_DEPLOYMENT_NAME as string;
-    const openAIVersion = process.env.OPENAI_API_VERSION as string;
+      .AZURE_OPENAI_DEPLOYMENT_NAME || "Your deployment name" as string;
+    const openAIVersion = process.env.OPENAI_API_VERSION || "A supported API version" as string;
     
     // Check env variables
     if (!azureOpenAIKey || !azureOpenAIEndpoint || !azureOpenAIDeployment || !openAIVersion) {
       throw new Error(
-        "Please set AZURE_OPENAI_KEY and AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_DEPLOYMENT_NAME in your environment variables."
+        "You need to set the endpoint, deployment name, and API version."
       );
     }
     
@@ -314,7 +310,6 @@ An individual assistant can access up to 128 tools including `code interpreter`,
       }
     }
     ```
-    
 
 1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScript用アシスタントのガイドの改善"
}
```

### Explanation
この修正では、`assistants-typescript.md`ファイルが更新され、TypeScript用アシスタントの利用に関するガイドラインが改善されました。具体的には以下のような変更が行われています：

1. **環境変数のデフォルト値設定**: JavaScriptのバージョンに引き続き、TypeScript版でも各環境変数にデフォルト値が追加されました。これにより、APIエンドポイント、デプロイメント名、およびAPIバージョンが未設定の場合でも、ユーザーは何を入力すべきか明確に示されます。

2. **テキストの簡素化**: 一部のインストラクションが簡潔になり、手順がより直感的に理解できるよう改善されています。例えば、OpenAIクライアントライブラリのインストール手順や環境変数の設定に関する説明がすっきりしました。

3. **エラーメッセージの改善**: 環境変数の未設定時に表示されるエラーメッセージが更新され、必要な情報が明確にされました。

4. **不要な空行の削除**: ドキュメント内の不要な空行が削除され、全体的に整った印象を与えるようになっています。

これらの変更により、TypeScriptを用いるユーザーはアシスタントを活用する際の手順をより理解しやすくなり、迅速に設定を行えるようになっています。全体として、ドキュメントの可読性が向上し、利用者の体験が改善されました。

## articles/ai-services/openai/includes/audio-completions-javascript.md{#item-b1be01}

<details>
<summary>Diff</summary>
````diff
@@ -29,7 +29,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create a new folder `audio-completions-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
     ```shell
-    mkdir audio-completions-quickstart && code audio-completions-quickstart
+    mkdir audio-completions-quickstart && cd audio-completions-quickstart
     ```
     
 1. Create the `package.json` with the following command:
@@ -38,13 +38,6 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     npm init -y
     ```
 
-1. Update the `package.json` to ECMAScript with the following command: 
-
-    ```shell
-    npm pkg set type=module
-    ```
-    
-
 1. Install the OpenAI client library for JavaScript with:
 
     ```console
@@ -83,9 +76,9 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     const azureADTokenProvider = getBearerTokenProvider(credential, scope);
     
     // Set environment variables or edit the corresponding values here.
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
-    const apiVersion = "2025-01-01-preview"; 
-    const deployment = "gpt-4o-mini-audio-preview"; 
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
+    const deployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini-audio-preview"; 
+    const apiVersion = process.env.OPENAI_API_VERSION || "2025-01-01-preview"; 
     
     const client = new AzureOpenAI({ 
         endpoint, 
@@ -150,8 +143,8 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     const { writeFileSync } = require("node:fs");
     
     // Set environment variables or edit the corresponding values here.
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "AZURE_OPENAI_API_KEY";
     const apiVersion = "2025-01-01-preview"; 
     const deployment = "gpt-4o-mini-audio-preview"; 
     
@@ -229,7 +222,7 @@ The script generates an audio file named _dog.wav_ in the same directory as the
     const azureADTokenProvider = getBearerTokenProvider(credential, scope);
     
     // Set environment variables or edit the corresponding values here.
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
     const apiVersion = "2025-01-01-preview"; 
     const deployment = "gpt-4o-mini-audio-preview"; 
     
@@ -312,8 +305,8 @@ The script generates an audio file named _dog.wav_ in the same directory as the
     const { writeFileSync } = require("node:fs");
     
     // Set environment variables or edit the corresponding values here.
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "AZURE_OPENAI_API_KEY";
     const apiVersion = "2025-01-01-preview"; 
     const deployment = "gpt-4o-mini-audio-preview"; 
     
@@ -404,7 +397,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
     const azureADTokenProvider = getBearerTokenProvider(credential, scope);
     
     // Set environment variables or edit the corresponding values here.
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
     const apiVersion = "2025-01-01-preview"; 
     const deployment = "gpt-4o-mini-audio-preview"; 
     
@@ -508,8 +501,8 @@ The script generates a transcript of the summary of the spoken audio input. It a
     const fs = require('fs').promises;
     
     // Set environment variables or edit the corresponding values here.
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "AZURE_OPENAI_API_KEY";
     const apiVersion = "2025-01-01-preview"; 
     const deployment = "gpt-4o-mini-audio-preview"; 
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript用音声完了ガイドの改善"
}
```

### Explanation
この修正では、`audio-completions-javascript.md`ファイルが更新され、JavaScriptにおける音声完了に関するガイドラインが改善されました。主な変更点は以下の通りです：

1. **ディレクトリの移動コマンドの改善**: アプリケーションを作成する手順において、`mkdir`コマンドの後にフォルダに移動するための`cd`コマンドが正しく追加されました。これにより、ユーザーは新しいフォルダにアクセスしやすくなります。

2. **環境変数のデフォルト値設定**: 各環境変数のデフォルト値が設定されていることを明確にし、新しい書き方が導入されました。これにより、ユーザーは環境変数が設定されていない場合でも、どの値が未設定であるかを理解しやすくなります。

3. **エラーメッセージの改善**: 環境変数が設定されていない際のエラーメッセージが改善され、何が必要なのかを具体的に示すようになりました。

4. **コードの整形**: 読みやすさ向上のため、環境変数の取得方法について、より一貫性のあるスタイルが適用されました。

これらの変更により、ユーザーはJavaScriptを利用した音声完了機能に関するガイドをより簡単に理解し、実装できるようになります。全体として、ドキュメントの可読性と使用体験が向上しました。

## articles/ai-services/openai/includes/audio-completions-python.md{#item-a88047}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create a new folder `audio-completions-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
     ```shell
-    mkdir audio-completions-quickstart && code audio-completions-quickstart
+    mkdir audio-completions-quickstart && cd audio-completions-quickstart
     ```
     
 1. Create a virtual environment. If you already have Python 3.10 or higher installed, you can create a virtual environment using the following commands:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python用音声完了ガイドの手順修正"
}
```

### Explanation
この修正では、`audio-completions-python.md`ファイルが更新され、Pythonにおける音声完了のためのガイドラインに対するわずかな変更が行われました。主な変更点は以下の通りです：

1. **ディレクトリの移動コマンドの修正**: アプリケーションを作成する手順で、フォルダを作成した後に移動するための`cd`コマンドが正しく追加されました。この修正により、ユーザーは新しく作成したフォルダに移動する手順が明確になり、使いやすくなっています。

このように、修正は非常に単純ですが、重要な手順の正確性を保つことで、ユーザーの体験を向上させています。全体的に、ドキュメントの指示がより明確で分かりやすくなりました。

## articles/ai-services/openai/includes/audio-completions-rest.md{#item-0ec305}

<details>
<summary>Diff</summary>
````diff
@@ -29,7 +29,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create a new folder `audio-completions-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
     ```shell
-    mkdir audio-completions-quickstart && code audio-completions-quickstart
+    mkdir audio-completions-quickstart && cd audio-completions-quickstart
     ```
     
 1. Create a virtual environment. If you already have Python 3.10 or higher installed, you can create a virtual environment using the following commands:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST API用音声完了ガイドの手順修正"
}
```

### Explanation
この修正では、`audio-completions-rest.md`ファイルが更新され、REST APIにおける音声完了のためのガイドラインに関する手順が改善されました。主な変更点は以下の通りです：

1. **ディレクトリの移動コマンドの修正**: 手順の中で、フォルダを作成後、そのフォルダに移動するために`cd`コマンドが追加されました。これにより、ユーザーは新しいフォルダに正しく移動できるようになり、手順がより明確になりました。

この改善により、ユーザーは作業をスムーズに進められ、実装手順がより理解しやすくなっています。全体として、ドキュメントの可読性と使用性が向上しました。

## articles/ai-services/openai/includes/audio-completions-typescript.md{#item-94bc1f}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create a new folder `audio-completions-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
     ```shell
-    mkdir audio-completions-quickstart && code audio-completions-quickstart
+    mkdir audio-completions-quickstart && cd audio-completions-quickstart
     ```
     
 
@@ -82,9 +82,9 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
       } from "@azure/identity";
     
     // Set environment variables or edit the corresponding values here.
-    const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
-    const apiVersion: string = "2025-01-01-preview"; 
-    const deployment: string = "gpt-4o-mini-audio-preview"; 
+    const endpoint: string = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
+    const deployment: string = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini-audio-preview"; 
+    const apiVersion: string = process.env.OPENAI_API_VERSION || "2025-01-01-preview"; 
     
     // Keyless authentication 
     const getClient = (): AzureOpenAI => {
@@ -180,8 +180,8 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     import { AzureOpenAI } from "openai/index.mjs";
     
     // Set environment variables or edit the corresponding values here.
-    const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
-    const apiKey: string = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
+    const endpoint: string = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
+    const apiKey: string = process.env.AZURE_OPENAI_API_KEY || "AZURE_OPENAI_API_KEY";
     const apiVersion: string = "2025-01-01-preview"; 
     const deployment: string = "gpt-4o-mini-audio-preview"; 
     
@@ -280,7 +280,7 @@ The script generates an audio file named _dog.wav_ in the same directory as the
       } from "@azure/identity";
     
     // Set environment variables or edit the corresponding values here.
-    const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const endpoint: string = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
     const apiVersion: string = "2025-01-01-preview"; 
     const deployment: string = "gpt-4o-mini-audio-preview"; 
     
@@ -391,8 +391,8 @@ The script generates an audio file named _dog.wav_ in the same directory as the
     import { promises as fs } from 'fs';
     
     // Set environment variables or edit the corresponding values here.
-    const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
-    const apiKey: string = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
+    const endpoint: string = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
+    const apiKey: string = process.env.AZURE_OPENAI_API_KEY || "AZURE_OPENAI_API_KEY";
     const apiVersion: string = "2025-01-01-preview"; 
     const deployment: string = "gpt-4o-mini-audio-preview"; 
     
@@ -503,7 +503,7 @@ The script generates a transcript of the summary of the spoken audio input. It a
       } from "@azure/identity";
     
     // Set environment variables or edit the corresponding values here.
-    const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT";
+    const endpoint: string = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
     const apiVersion: string = "2025-01-01-preview"; 
     const deployment: string = "gpt-4o-mini-audio-preview"; 
     
@@ -635,8 +635,8 @@ The script generates a transcript of the summary of the spoken audio input. It a
     import { ChatCompletionMessageParam } from "openai/resources/index.mjs";
     
     // Set environment variables or edit the corresponding values here.
-    const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "AZURE_OPENAI_ENDPOINT" as string;
-    const apiKey: string = process.env["AZURE_OPENAI_API_KEY"] || "AZURE_OPENAI_API_KEY";
+    const endpoint: string = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT" as string;
+    const apiKey: string = process.env.AZURE_OPENAI_API_KEY || "AZURE_OPENAI_API_KEY";
     const apiVersion: string = "2025-01-01-preview"; 
     const deployment: string = "gpt-4o-mini-audio-preview"; 
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScript用音声完了ガイドの環境変数修正"
}
```

### Explanation
この修正では、`audio-completions-typescript.md`ファイルが更新され、TypeScriptにおける音声完了のガイドラインに関するコードの説明が修正されました。主な変更点は以下の通りです：

1. **環境変数の記述方法の統一**: 環境変数を取得するための記述が、`process.env[...]` 形式から `process.env.` 形式に変更され、より一貫性が持たせられています。この修正により、コードが明瞭になり、初心者でも理解しやすくなっています。

2. **設定変数の柔軟性の向上**: `deployment` と `apiVersion` の環境変数も、デフォルト値から環境変数に切り替えられており、実行環境に応じた設定が容易になりました。

このように、修正は主にコードの可読性と環境変数の扱いに関するもので、ユーザーが必要な設定を自然に適用できるように改善されています。全体として、ドキュメントの品質と使い勝手が向上しました。

## articles/ai-services/openai/includes/chatgpt-javascript.md{#item-cbf09f}

<details>
<summary>Diff</summary>
````diff
@@ -29,127 +29,144 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 - Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
 - Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-## Retrieve resource information
+## Set up
+ 
+1. Create a new folder `chat-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-[!INCLUDE [resource authentication](resource-authentication.md)]
+    ```shell
+    mkdir chat-quickstart && cd chat-quickstart
+    ```
 
-> [!CAUTION]
-> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+1. Create the `package.json` with the following command:
 
+    ```shell
+    npm init -y
+    ```   
 
-## Create a Node application
+1. Install the OpenAI client library for JavaScript with:
 
-In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. 
+    ```console
+    npm install openai
+    ```
 
-## Install the client library
+1. For the **recommended** passwordless authentication:
 
-Install the required packages for JavaScript with npm from within the context of your new directory:
+    ```console
+    npm install @azure/identity
+    ```
 
-```console
-npm install openai @azure/identity
-```
-
-Your app's _package.json_ file is updated with the dependencies.
+## Retrieve resource information
 
-## Create a sample application
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
-Open a command prompt where you want the new project, and create a new file named ChatCompletion.js. Copy the following code into the ChatCompletion.js file.
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
+## Create a sample application
 
 ## [Microsoft Entra ID](#tab/keyless)
 
-```javascript
-const { AzureOpenAI } = require("openai");
-const { 
-  DefaultAzureCredential, 
-  getBearerTokenProvider 
-} = require("@azure/identity");
-
-// You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-const apiVersion = "2024-05-01-preview";
-const deployment = "gpt-4o"; //This must match your deployment name.
-
-
-// keyless authentication    
-const credential = new DefaultAzureCredential();
-const scope = "https://cognitiveservices.azure.com/.default";
-const azureADTokenProvider = getBearerTokenProvider(credential, scope);
-
-async function main() {
-
-  const client = new AzureOpenAI({ endpoint, apiKey, azureADTokenProvider, deployment });
-  const result = await client.chat.completions.create({
-    messages: [
-    { role: "system", content: "You are a helpful assistant." },
-    { role: "user", content: "Does Azure OpenAI support customer managed keys?" },
-    { role: "assistant", content: "Yes, customer managed keys are supported by Azure OpenAI?" },
-    { role: "user", content: "Do other Azure AI services support this too?" },
-    ],
-    model: "",
-  });
-
-  for (const choice of result.choices) {
-    console.log(choice.message);
-  }
-}
-
-main().catch((err) => {
-  console.error("The sample encountered an error:", err);
-});
-
-module.exports = { main };
-```
-
-Run the script with the following command:
-
-```cmd
-node.exe ChatCompletion.js
-```
+1. Create the `index.js` file with the following code:
+    
+    ```javascript
+    const { AzureOpenAI } = require("openai");
+    const { 
+      DefaultAzureCredential, 
+      getBearerTokenProvider 
+    } = require("@azure/identity");
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-05-01-preview";
+    const deployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o"; //This must match your deployment name.
+    
+    // keyless authentication    
+    const credential = new DefaultAzureCredential();
+    const scope = "https://cognitiveservices.azure.com/.default";
+    const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+    
+    async function main() {
+    
+      const client = new AzureOpenAI({ endpoint, apiKey, azureADTokenProvider, deployment });
+      const result = await client.chat.completions.create({
+        messages: [
+        { role: "system", content: "You are a helpful assistant." },
+        { role: "user", content: "Does Azure OpenAI support customer managed keys?" },
+        { role: "assistant", content: "Yes, customer managed keys are supported by Azure OpenAI?" },
+        { role: "user", content: "Do other Azure AI services support this too?" },
+        ],
+        model: "",
+      });
+    
+      for (const choice of result.choices) {
+        console.log(choice.message);
+      }
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
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
+    node index.js
+    ```
 
 
 ## [API key](#tab/api-key)
 
-```javascript
-const { AzureOpenAI } = require("openai");
-
-// You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
-const apiVersion = "2024-05-01-preview";
-const deployment = "gpt-4o"; //This must match your deployment name.
-
-async function main() {
-
-  const client = new AzureOpenAI({ endpoint, apiKey, apiVersion, deployment });
-  const result = await client.chat.completions.create({
-    messages: [
-    { role: "system", content: "You are a helpful assistant." },
-    { role: "user", content: "Does Azure OpenAI support customer managed keys?" },
-    { role: "assistant", content: "Yes, customer managed keys are supported by Azure OpenAI?" },
-    { role: "user", content: "Do other Azure AI services support this too?" },
-    ],
-    model: "",
-  });
-
-  for (const choice of result.choices) {
-    console.log(choice.message);
-  }
-}
-
-main().catch((err) => {
-  console.error("The sample encountered an error:", err);
-});
-
-module.exports = { main };
-```
-
-Run the script with the following command:
-
-```cmd
-node.exe ChatCompletion.js
-```
-
+1. Create the `index.js` file with the following code:
+    
+    ```javascript
+    const { AzureOpenAI } = require("openai");
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-05-01-preview";
+    const deployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o"; //This must match your deployment name.
+    
+    async function main() {
+    
+      const client = new AzureOpenAI({ endpoint, apiKey, apiVersion, deployment });
+      const result = await client.chat.completions.create({
+        messages: [
+        { role: "system", content: "You are a helpful assistant." },
+        { role: "user", content: "Does Azure OpenAI support customer managed keys?" },
+        { role: "assistant", content: "Yes, customer managed keys are supported by Azure OpenAI?" },
+        { role: "user", content: "Do other Azure AI services support this too?" },
+        ],
+        model: "",
+      });
+    
+      for (const choice of result.choices) {
+        console.log(choice.message);
+      }
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
+    
+    module.exports = { main };
+    ```
+    
+1. Run the JavaScript file.
+
+    ```shell
+    node index.js
+    ```
+    
 ---
 
 ## Output
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript用ChatGPTガイドの手順更新"
}
```

### Explanation
この修正では、`chatgpt-javascript.md`ファイルが更新され、JavaScriptにおけるChatGPTの利用方法に関する手順が改善されました。主な変更点は以下の通りです：

1. **手順の整理と明確化**: 新しい手順が追加され、アプリケーションのセットアッププロセスがより整理されました。具体的には、プロジェクトフォルダの作成、パッケージの初期化、必要なライブラリのインストール手順などが明確に示されています。

2. **新しいファイルの作成**: `index.js`ファイルの作成が明示的に含まれ、その中に必要なコードサンプルが含まれています。これにより、ユーザーが一貫した流れで作業を進めることができるようになります。

3. **環境変数の使用法の改良**: 環境変数の取得方法が一貫性を持たせられ、ユーザーが必要な設定を直感的に行えるようになっています。

4. **注記の強調**: 推奨されるキーなし認証を使用するための注意事項が、目立つように強調されており、より安全な実装を促す内容となっています。

全体として、修正はチュートリアルの使い勝手を向上させ、ユーザーがより簡単にChatGPTを使い始められるように配慮されています。これにより、初心者でも手順が分かりやすくなり、学習を進めやすくなっています。

## articles/ai-services/openai/includes/chatgpt-typescript.md{#item-6d2f1f}

<details>
<summary>Diff</summary>
````diff
@@ -30,183 +30,233 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 - Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
 - Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-## Retrieve resource information
-
-[!INCLUDE [resource authentication](resource-authentication.md)]
-
-> [!CAUTION]
-> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+## Set up
 
-## Create a Node application
+1. Create a new folder `chat-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. 
+    ```shell
+    mkdir chat-quickstart && cd chat-quickstart
+    ```
+    
+1. Create the `package.json` with the following command:
 
-## Install the client library
+    ```shell
+    npm init -y
+    ```
 
-Install the required packages for JavaScript with npm from within the context of your new directory:
+1. Update the `package.json` to ECMAScript with the following command: 
 
-```console
-npm install openai @azure/identity
-```
+    ```shell
+    npm pkg set type=module
+    ```
+    
 
-Your app's _package.json_ file is updated with the dependencies.
+1. Install the OpenAI client library for JavaScript with:
 
+    ```console
+    npm install openai
+    ```
 
-## Create a sample application
+1. For the **recommended** passwordless authentication:
 
-Open a command prompt where you want the new project, and create a new file named ChatCompletion.ts. Copy the following code into the ChatCompletion.ts file.
-
-## [Microsoft Entra ID](#tab/typescript-keyless)
+    ```console
+    npm install @azure/identity
+    ```
 
-```typescript
-import { AzureOpenAI } from "openai";
-import { 
-  DefaultAzureCredential, 
-  getBearerTokenProvider 
-} from "@azure/identity";
-import type {
-  ChatCompletion,
-  ChatCompletionCreateParamsNonStreaming,
-} from "openai/resources/index";
-
-// You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-
-// Required Azure OpenAI deployment name and API version
-const apiVersion = "2024-08-01-preview";
-const deploymentName = "gpt-4o-mini"; //This must match your deployment name.
-
-// keyless authentication    
-const credential = new DefaultAzureCredential();
-const scope = "https://cognitiveservices.azure.com/.default";
-const azureADTokenProvider = getBearerTokenProvider(credential, scope);
-
-function getClient(): AzureOpenAI {
-  return new AzureOpenAI({
-    endpoint,
-    azureADTokenProvider,
-    apiVersion,
-    deployment: deploymentName,
-  });
-}
-
-function createMessages(): ChatCompletionCreateParamsNonStreaming {
-  return {
-    messages: [
-      { role: "system", content: "You are a helpful assistant." },
-      {
-        role: "user",
-        content: "Does Azure OpenAI support customer managed keys?",
-      },
-      {
-        role: "assistant",
-        content: "Yes, customer managed keys are supported by Azure OpenAI?",
-      },
-      { role: "user", content: "Do other Azure AI services support this too?" },
-    ],
-    model: "",
-  };
-}
-async function printChoices(completion: ChatCompletion): Promise<void> {
-  for (const choice of completion.choices) {
-    console.log(choice.message);
-  }
-}
-export async function main() {
-  const client = getClient();
-  const messages = createMessages();
-  const result = await client.chat.completions.create(messages);
-  await printChoices(result);
-}
-
-main().catch((err) => {
-  console.error("The sample encountered an error:", err);
-});
-```
+## Retrieve resource information
 
-Build the script with the following command:
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
-```cmd
-tsc
-```
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
-Run the script with the following command:
+## Create a sample application
 
-```cmd
-node.exe ChatCompletion.js
-```
+## [Microsoft Entra ID](#tab/typescript-keyless)
+   
+1. Create the `index.ts` file with the following code:
+ 
+    ```typescript
+    import { AzureOpenAI } from "openai";
+    import { 
+      DefaultAzureCredential, 
+      getBearerTokenProvider 
+    } from "@azure/identity";
+    import type {
+      ChatCompletion,
+      ChatCompletionCreateParamsNonStreaming,
+    } from "openai/resources/index";
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    
+    // Required Azure OpenAI deployment name and API version
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-08-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini"; //This must match your deployment name.
+    
+    // keyless authentication    
+    const credential = new DefaultAzureCredential();
+    const scope = "https://cognitiveservices.azure.com/.default";
+    const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        azureADTokenProvider,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    
+    function createMessages(): ChatCompletionCreateParamsNonStreaming {
+      return {
+        messages: [
+          { role: "system", content: "You are a helpful assistant." },
+          {
+            role: "user",
+            content: "Does Azure OpenAI support customer managed keys?",
+          },
+          {
+            role: "assistant",
+            content: "Yes, customer managed keys are supported by Azure OpenAI?",
+          },
+          { role: "user", content: "Do other Azure AI services support this too?" },
+        ],
+        model: "",
+      };
+    }
+    async function printChoices(completion: ChatCompletion): Promise<void> {
+      for (const choice of completion.choices) {
+        console.log(choice.message);
+      }
+    }
+    export async function main() {
+      const client = getClient();
+      const messages = createMessages();
+      const result = await client.chat.completions.create(messages);
+      await printChoices(result);
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
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
+    node index.js
+    ```
 
 ## [API Key](#tab/typescript-key)
 
-```typescript
-import { AzureOpenAI } from "openai";
-import type {
-  ChatCompletion,
-  ChatCompletionCreateParamsNonStreaming,
-} from "openai/resources/index";
-
-// You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
-
-// Required Azure OpenAI deployment name and API version
-const apiVersion = "2024-08-01-preview";
-const deploymentName = "gpt-4o-mini"; //This must match your deployment name.
-
-function getClient(): AzureOpenAI {
-  return new AzureOpenAI({
-    endpoint,
-    apiKey,
-    apiVersion,
-    deployment: deploymentName,
-  });
-}
-
-function createMessages(): ChatCompletionCreateParamsNonStreaming {
-  return {
-    messages: [
-      { role: "system", content: "You are a helpful assistant." },
-      {
-        role: "user",
-        content: "Does Azure OpenAI support customer managed keys?",
-      },
-      {
-        role: "assistant",
-        content: "Yes, customer managed keys are supported by Azure OpenAI?",
-      },
-      { role: "user", content: "Do other Azure AI services support this too?" },
-    ],
-    model: "",
-  };
-}
-async function printChoices(completion: ChatCompletion): Promise<void> {
-  for (const choice of completion.choices) {
-    console.log(choice.message);
-  }
-}
-export async function main() {
-  const client = getClient();
-  const messages = createMessages();
-  const result = await client.chat.completions.create(messages);
-  await printChoices(result);
-}
-
-main().catch((err) => {
-  console.error("The sample encountered an error:", err);
-});
-```
-
-Build the script with the following command:
-
-```cmd
-tsc
-```
-
-Run the script with the following command:
-
-```cmd
-node.exe ChatCompletion.js
-```
+1. Create the `index.ts` file with the following code:
+    
+    ```typescript
+    import { AzureOpenAI } from "openai";
+    import type {
+      ChatCompletion,
+      ChatCompletionCreateParamsNonStreaming,
+    } from "openai/resources/index";
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
+    
+    // Required Azure OpenAI deployment name and API version
+    const apiVersion = process.env.OPENAI_API_KEY || "2024-08-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini"; //This must match your deployment name.
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    
+    function createMessages(): ChatCompletionCreateParamsNonStreaming {
+      return {
+        messages: [
+          { role: "system", content: "You are a helpful assistant." },
+          {
+            role: "user",
+            content: "Does Azure OpenAI support customer managed keys?",
+          },
+          {
+            role: "assistant",
+            content: "Yes, customer managed keys are supported by Azure OpenAI?",
+          },
+          { role: "user", content: "Do other Azure AI services support this too?" },
+        ],
+        model: "",
+      };
+    }
+    async function printChoices(completion: ChatCompletion): Promise<void> {
+      for (const choice of completion.choices) {
+        console.log(choice.message);
+      }
+    }
+    export async function main() {
+      const client = getClient();
+      const messages = createMessages();
+      const result = await client.chat.completions.create(messages);
+      await printChoices(result);
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
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
+    node index.js
+    ```
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScript用ChatGPTガイドの手順強化"
}
```

### Explanation
この修正では、`chatgpt-typescript.md`ファイルが更新され、TypeScriptでのChatGPTの設定および使用に関する手順が強化されました。主な変更点は以下の通りです：

1. **手順の再構成**: 新しいセクションとして「セットアップ」が追加され、アプリケーションを構築するための手順がより明確に示されています。具体的には、プロジェクトフォルダの作成、`package.json`の初期化、必要なライブラリのインストール手順が一連の流れとして整理されています。

2. **ECMAScriptのサポート**: `package.json`がECMAScriptモジュールを用いるように更新される手順が追加されています。これにより、最新のJavaScript機能が活用できるようになります。

3. **新しいコードサンプル**: 具体的な実装例が`index.ts`ファイルとして明示的に提供され、ユーザーが簡単に実装を理解できるようになっています。これにより、サンプルコードをそのまま利用することができます。

4. **TypeScriptの設定ファイル**: `tsconfig.json`の作成手順が含まれ、TypeScriptのコンパイル設定が示されています。これにより、開発者はTypeScriptをより効果的に使用できるようになります。

5. **注意事項の強調**: キーレス認証を使用する際の注意事項が強調され、エラーを避けるための重要な情報が提供されています。

全体として、この修正はドキュメントのユーザビリティを向上させ、TypeScriptを使用する開発者がよりスムーズにChatGPTを利用できるように配慮されています。これにより、初心者から上級者まで、適切な手順に従って効率的に学習・実装できる環境が整っています。

## articles/ai-services/openai/includes/dall-e-dotnet.md{#item-755f0a}

<details>
<summary>Diff</summary>
````diff
@@ -104,7 +104,7 @@ dotnet run
 The URL of the generated image is printed to the console.
 
 ```console
-https://dalleproduse.blob.core.windows.net/private/images/b7ac5e55-f1f8-497a-8d0e-8f51446bf538/generated_00.png?se=2024-07-12T13%3A47%3A56Z&sig=Zri37iYVTVtc52qzTFBOqPgSHvXwEhcO86Smv2ojB%2FE%3D&ske=2024-07-17T12%3A15%3A44Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2024-07-10T12%3A15%3A44Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02
+<SAS URL>
 ```
 
 > [!NOTE]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL·E .NETガイドのSAS URLへの更新"
}
```

### Explanation
この修正では、`dall-e-dotnet.md`ファイルの内容が更新され、DALL·Eを使用した.NETアプリケーションに関する情報が改訂されました。具体的な変更点は以下の通りです：

1. **画像URLの表記変更**: 以前は特定の画像のURLが直接表示されていましたが、こちらが「<SAS URL>」というプレースホルダーに置き換えられました。これにより、ユーザーが自身の環境で生成された画像のURLを適切に設定できるように意図されています。

2. **明確さの向上**: プレースホルダーへの変更により、ユーザーに対してURLの設定方法や必要性をより明確に示すことができるようになりました。これにより、ユーザーは誤って固定されたURLを使用することなく、自分のキーや設定を使って生成した画像へのアクセスが可能になります。

全体的に、この更新は情報の柔軟性を高め、ユーザーがDALL·Eを使用する際に自分自身の環境に応じたリンクを利用できるように改善されています。これにより、より正確で安全な実装が促進されることが期待されます。

## articles/ai-services/openai/includes/dall-e-go.md{#item-132707}

<details>
<summary>Diff</summary>
````diff
@@ -121,7 +121,7 @@ The URL of the generated image is printed to the console.
 
 ```console
 Image generated, HEAD request on URL returned 200
-Image URL: https://dalleproduse.blob.core.windows.net/private/images/d7b28a5c-ca32-4792-8c2a-6a5d8d8e5e45/generated_00.png?se=2023-08-29T17%3A05%3A37Z&sig=loqntaPypYVr9VTT5vpbsjsCz31g1GsdoQi0smbGkks%3D&ske=2023-09-02T18%3A53%3A23Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2023-08-26T18%3A53%3A23Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02
+Image URL: <SAS URL>
 ```
 > [!NOTE]
 > The image generation APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it won't return a generated image. For more information, see the [content filter](../concepts/content-filter.md) article.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL·E GoガイドのSAS URLへの更新"
}
```

### Explanation
この修正では、`dall-e-go.md`ファイルの該当部分が更新され、DALL·Eを使用したGoアプリケーションに関する情報が改訂されました。主な変更点は以下の通りです：

1. **画像URLの表記変更**: 以前は具体的な画像のURLが記載されていた部分が「<SAS URL>」というプレースホルダーに置き換えられました。これにより、ユーザーが自身の環境設定に応じて適切な遵守リンクを提供できるようになりました。

2. **柔軟性の向上**: プレースホルダーへの変更により、ユーザーは自分のSAS（Shared Access Signature）URLを適宜設定して使用できるため、特定のURLに依存しなくなります。この変更は、情報のカスタマイズ性を高め、ユーザーがより簡単に画像を生成・利用できるようにすることを目的としています。

さらに、利用者が生成した画像のURLを扱う際の誤解を避けるため、ドキュメントの明確さが向上しています。全体として、この更新はDALL·Eを使用する開発者がより効率的に実装できるようにサポートしており、使いやすさが向上しています。

## articles/ai-services/openai/includes/dall-e-java.md{#item-373f89}

<details>
<summary>Diff</summary>
````diff
@@ -163,7 +163,7 @@ dependencies {
 The URL of the generated image is printed to the console.
 
 ```console
-Image location URL that provides temporary access to download the generated image is https://dalleproduse.blob.core.windows.net/private/images/d2ea917f-8802-4ad6-8ef6-3fb7a15c8482/generated_00.png?se=2023-08-25T23%3A11%3A28Z&sig=%2BKa5Mkb9U88DfvxoBpyAjamYRzwb7aVCEucM6XJC3wQ%3D&ske=2023-08-31T15%3A27%3A47Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2023-08-24T15%3A27%3A47Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02.
+Image location URL that provides temporary access to download the generated image is <SAS URL>.
 Completed getImages.
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL·E JavaガイドのSAS URLへの更新"
}
```

### Explanation
この修正では、`dall-e-java.md`ファイルが更新され、DALL·Eを使用したJavaアプリケーションに関する情報が改訂されました。具体的な変更点は以下の通りです：

1. **画像アクセスURLの表記変更**: 以前は具体的な画像のURLが記載されていましたが、それが「<SAS URL>」というプレースホルダーに置き換えられました。この変更により、ユーザーが自身の環境設定に基づいて画像のダウンロード用URLを柔軟に設定できるようになります。

2. **ユーザビリティの向上**: プレースホルダーに変換することによって、ユーザーは固定されたURLに依存せず、必要なSAS URLを提供して画像にアクセスすることができます。これにより、特定の個別のURLに縛られることなく、より多様な使用が可能となります。

このように、更新はドキュメントの使い勝手を向上させ、DALL·Eを利用する開発者がより快適に実装を行えるような配慮がなされています。全体として、DALL·Eを活用するための情報がさらに明確で実用的になったと考えられます。

## articles/ai-services/openai/includes/dall-e-javascript.md{#item-6cffcf}

<details>
<summary>Diff</summary>
````diff
@@ -28,154 +28,167 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 - Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
 - Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-## Retrieve resource information
-
-[!INCLUDE [resource authentication](resource-authentication.md)]
-
-> [!CAUTION]
-> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+## Set up
+ 
+1. Create a new folder `image-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-## Create a Node application
+    ```shell
+    mkdir image-quickstart && cd image-quickstart
+    ```
 
-In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+1. Create the `package.json` with the following command:
 
-```console
-npm init
-```
+    ```shell
+    npm init -y
+    ```   
 
-## Install the client library
+1. Install the OpenAI client library for JavaScript with:
 
-Install the client libraries with:
+    ```console
+    npm install openai
+    ```
 
-```console
-npm install openai @azure/identity
-```
+1. For the **recommended** passwordless authentication:
 
-Your app's _package.json_ file will be updated with the dependencies.
+    ```console
+    npm install @azure/identity
+    ```
 
-## Generate images with DALL-E
+## Retrieve resource information
 
-Create a new file named _ImageGeneration.js_ and open it in your preferred code editor. Copy the following code into the _ImageGeneration.js_ file:
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
+## Generate images with DALL-E
 
 #### [Microsoft Entra ID](#tab/keyless)
 
-```javascript
-const { AzureOpenAI } = require("openai");
-const { 
-    DefaultAzureCredential, 
-    getBearerTokenProvider 
-} = require("@azure/identity");
-
-// You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
-
-// Required Azure OpenAI deployment name and API version
-const apiVersion = "2024-07-01";
-const deploymentName = "dall-e-3";
-
-// The prompt to generate images from
-const prompt = "a monkey eating a banana";
-const numberOfImagesToGenerate = 1;
-
-// keyless authentication    
-const credential = new DefaultAzureCredential();
-const scope = "https://cognitiveservices.azure.com/.default";
-const azureADTokenProvider = getBearerTokenProvider(credential, scope);
-
-function getClient(): AzureOpenAI {
-  return new AzureOpenAI({
-    endpoint,
-    azureADTokenProvider,
-    apiVersion,
-    deployment: deploymentName,
-  });
-}
-async function main() {
-  console.log("== Image Generation ==");
-
-  const client = getClient();
-
-  const results = await client.images.generate({
-    prompt,
-    size: "1024x1024",
-    n: numberOfImagesToGenerate,
-    model: "",
-    style: "vivid", // or "natural"
-  });
-
-  for (const image of results.data) {
-    console.log(`Image generation result URL: ${image.url}`);
-  }
-}
-
-main().catch((err) => {
-  console.error("The sample encountered an error:", err);
-});
-```
-
-Run the script with the following command:
-
-```console
-node ImageGeneration.js
-```
-
-
-
-#### [API key](#tab/api-key)
-
-```javascript
-const { AzureOpenAI } = require("openai");
-
-// You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
-const apiKey = process.env["AZURE_OPENAI_API_KEY"];
-
-// Required Azure OpenAI deployment name and API version
-const apiVersion = "2024-07-01";
-const deploymentName = "dall-e-3";
-
-// The prompt to generate images from
-const prompt = "a monkey eating a banana";
-const numberOfImagesToGenerate = 1;
-
-function getClient() {
-  return new AzureOpenAI({
-    endpoint,
-    apiKey,
-    apiVersion,
-    deployment: deploymentName,
-  });
-}
-async function main() {
-  console.log("== Image Generation ==");
-
-  const client = getClient();
-
-  const results = await client.images.generate({
-    prompt,
-    size: "1024x1024",
-    n: numberOfImagesToGenerate,
-    model: "",
-    style: "vivid", // or "natural"
-  });
-
-  for (const image of results.data) {
-    console.log(`Image generation result URL: ${image.url}`);
-  }
-}
-
-main().catch((err) => {
-  console.error("The sample encountered an error:", err);
-});
-```
-
-Run the script with the following command:
-
-```console
-node ImageGeneration.js
-```
+1. Create the `index.js` file with the following code:
+
+    ```javascript
+    const { AzureOpenAI } = require("openai");
+    const { 
+        DefaultAzureCredential, 
+        getBearerTokenProvider 
+    } = require("@azure/identity");
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    
+    // Required Azure OpenAI deployment name and API version
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-07-01";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "dall-e-3";
+    
+    // The prompt to generate images from
+    const prompt = "a monkey eating a banana";
+    const numberOfImagesToGenerate = 1;
+    
+    // keyless authentication    
+    const credential = new DefaultAzureCredential();
+    const scope = "https://cognitiveservices.azure.com/.default";
+    const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        azureADTokenProvider,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    async function main() {
+      console.log("== Image Generation ==");
+    
+      const client = getClient();
+    
+      const results = await client.images.generate({
+        prompt,
+        size: "1024x1024",
+        n: numberOfImagesToGenerate,
+        model: "",
+        style: "vivid", // or "natural"
+      });
+    
+      for (const image of results.data) {
+        console.log(`Image generation result URL: ${image.url}`);
+      }
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
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
+    node index.js
+    ```
+
+
+## [API key](#tab/api-key)
+
+1. Create the `index.js` file with the following code:
+    
+    ```javascript
+    const { AzureOpenAI } = require("openai");
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
+    
+    // Required Azure OpenAI deployment name and API version
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-07-01";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "dall-e-3";
+    
+    // The prompt to generate images from
+    const prompt = "a monkey eating a banana";
+    const numberOfImagesToGenerate = 1;
+    
+    function getClient() {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    async function main() {
+      console.log("== Image Generation ==");
+    
+      const client = getClient();
+    
+      const results = await client.images.generate({
+        prompt,
+        size: "1024x1024",
+        n: numberOfImagesToGenerate,
+        model: "",
+        style: "vivid", // or "natural"
+      });
+    
+      for (const image of results.data) {
+        console.log(`Image generation result URL: ${image.url}`);
+      }
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
+    ```
+    
+1. Run the JavaScript file.
+
+    ```shell
+    node index.js
+    ```
 
 ---
 
@@ -185,8 +198,8 @@ The URL of the generated image is printed to the console.
 
 ```console
 == Batch Image Generation ==
-Image generation result URL: https://dalleproduse.blob.core.windows.net/private/images/5e7536a9-a0b5-4260-8769-2d54106f2913/generated_00.png?se=2023-08-29T19%3A12%3A57Z&sig=655GkWajOZ9ALjFykZF%2FBMZRPQALRhf4UPDImWCQoGI%3D&ske=2023-09-02T18%3A53%3A23Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2023-08-26T18%3A53%3A23Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02
-Image generation result URL: https://dalleproduse.blob.core.windows.net/private/images/5e7536a9-a0b5-4260-8769-2d54106f2913/generated_01.png?se=2023-08-29T19%3A12%3A57Z&sig=B24ymPLSZ3HfG23uojOD9VlRFGxjvgcNmvFo4yPUbEc%3D&ske=2023-09-02T18%3A53%3A23Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2023-08-26T18%3A53%3A23Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02
+Image generation result URL: <SAS URL>
+Image generation result URL: <SAS URL>
 ```
 
 > [!NOTE]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL·E JavaScriptガイドのSAS URLへの更新と構成の簡素化"
}
```

### Explanation
この修正では、`dall-e-javascript.md`ファイルが大幅に改訂され、DALL·Eを使用したJavaScriptアプリケーションの導入を簡素化しました。主な変更点は以下の通りです：

1. **構成手順の更新**: 読者がアプリケーションのセットアップを迅速に行えるよう、新しいフォルダの作成や`package.json`ファイルの生成方法を具体的に示した手順が追加されました。また、パスワードレス認証を推奨するための環境変数の使用が強調されました。

2. **画像アクセスURLのプレースホルダー化**: 画像生成結果のURLが実際のURLから「<SAS URL>」というプレースホルダーに変更されました。この変更により、ユーザーが自身の環境に合わせた適切なSAS（Shared Access Signature）URLを利用できるようになり、ドキュメントの柔軟性が向上しました。

3. **サンプルコードの改訂**: サンプルコードが新しい構成に合わせて更新され、より分かりやすくなりました。また、依存ライブラリのインストール手順も明確になり、開発者が必要なツールを簡単に導入できるようになっています。

全体として、この更新はDALL·Eを用いたJavaScriptアプリケーションの導入をよりシンプルで効果的にし、ユーザーがより容易に画像生成を行えるように改善されています。

## articles/ai-services/openai/includes/dall-e-typescript.md{#item-57b205}

<details>
<summary>Diff</summary>
````diff
@@ -29,157 +29,211 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 - Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
 - Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-## Retrieve resource information
+## Set up
 
-[!INCLUDE [resource authentication](resource-authentication.md)]
+1. Create a new folder `image-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-> [!CAUTION]
-> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+    ```shell
+    mkdir image-quickstart && cd image-quickstart
+    ```
+    
+1. Create the `package.json` with the following command:
 
-## Create a Node application
+    ```shell
+    npm init -y
+    ```
 
-In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+1. Update the `package.json` to ECMAScript with the following command: 
 
-```console
-npm init
-```
+    ```shell
+    npm pkg set type=module
+    ```
+    
+
+1. Install the OpenAI client library for JavaScript with:
 
-## Install the client library
+    ```console
+    npm install openai
+    ```
 
-Install the client libraries with:
+1. For the **recommended** passwordless authentication:
 
-```console
-npm install openai @azure/identity
-```
+    ```console
+    npm install @azure/identity
+    ```
 
-Your app's _package.json_ file will be updated with the dependencies.
+## Retrieve resource information
 
-## Generate images with DALL-E
+[!INCLUDE [resource authentication](resource-authentication.md)]
+
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
-Create a new file named _ImageGeneration.ts_ and open it in your preferred code editor. Copy the following code into the _ImageGeneration.ts_ file:
+## Generate images with DALL-E
 
 #### [Microsoft Entra ID](#tab/typescript-keyless)
 
-```typescript
-import { AzureOpenAI } from "openai";
-import { 
-    DefaultAzureCredential, 
-    getBearerTokenProvider 
-} from "@azure/identity";
-
-// You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
-
-// Required Azure OpenAI deployment name and API version
-const apiVersion = "2024-07-01";
-const deploymentName = "dall-e-3";
-
-// keyless authentication    
-const credential = new DefaultAzureCredential();
-const scope = "https://cognitiveservices.azure.com/.default";
-const azureADTokenProvider = getBearerTokenProvider(credential, scope);
-
-function getClient(): AzureOpenAI {
-  return new AzureOpenAI({
-    endpoint,
-    azureADTokenProvider,
-    apiVersion,
-    deployment: deploymentName,
-  });
-}
-async function main() {
-  console.log("== Image Generation ==");
-
-  const client = getClient();
-
-  const results = await client.images.generate({
-    prompt,
-    size: "1024x1024",
-    n: numberOfImagesToGenerate,
-    model: "",
-    style: "vivid", // or "natural"
-  });
-
-  for (const image of results.data) {
-    console.log(`Image generation result URL: ${image.url}`);
-  }
-}
-
-main().catch((err) => {
-  console.error("The sample encountered an error:", err);
-});
-```
+1. Create the `index.ts` file with the following code:
+
+    ```typescript
+    import { AzureOpenAI } from "openai";
+    import { 
+        DefaultAzureCredential, 
+        getBearerTokenProvider 
+    } from "@azure/identity";
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    
+    // Required Azure OpenAI deployment name and API version
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-07-01";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "dall-e-3";
+    
+    // keyless authentication    
+    const credential = new DefaultAzureCredential();
+    const scope = "https://cognitiveservices.azure.com/.default";
+    const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        azureADTokenProvider,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    async function main() {
+      console.log("== Image Generation ==");
+    
+      const client = getClient();
+    
+      const results = await client.images.generate({
+        prompt,
+        size: "1024x1024",
+        n: numberOfImagesToGenerate,
+        model: "",
+        style: "vivid", // or "natural"
+      });
+    
+      for (const image of results.data) {
+        console.log(`Image generation result URL: ${image.url}`);
+      }
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
+    ```
 
-1. Build the application with the following command:
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
 
-    ```console
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
     tsc
     ```
+    
+1. Sign in to Azure with the following command:
 
-1. Run the application with the following command:
+    ```shell
+    az login
+    ```
 
-    ```console
-    node ImageGeneration.js
+1. Run the code with the following command:
+
+    ```shell
+    node index.js
     ```
 
-#### [API key](#tab/typescript-key)
-
-```typescript
-import { AzureOpenAI } from "openai";
-
-// You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
-const apiKey = process.env["AZURE_OPENAI_API_KEY"];
-
-// Required Azure OpenAI deployment name and API version
-const apiVersion = "2024-07-01";
-const deploymentName = "dall-e-3";
-
-// The prompt to generate images from
-const prompt = "a monkey eating a banana";
-const numberOfImagesToGenerate = 1;
-
-function getClient(): AzureOpenAI {
-  return new AzureOpenAI({
-    endpoint,
-    apiKey,
-    apiVersion,
-    deployment: deploymentName,
-  });
-}
-async function main() {
-  console.log("== Image Generation ==");
-
-  const client = getClient();
-
-  const results = await client.images.generate({
-    prompt,
-    size: "1024x1024",
-    n: numberOfImagesToGenerate,
-    model: "",
-    style: "vivid", // or "natural"
-  });
-
-  for (const image of results.data) {
-    console.log(`Image generation result URL: ${image.url}`);
-  }
-}
-
-main().catch((err) => {
-  console.error("The sample encountered an error:", err);
-});
-```
+## [API key](#tab/typescript-key)
+
+1. Create the `index.ts` file with the following code:
+
+    ```typescript
+    import { AzureOpenAI } from "openai";
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
+    
+    // Required Azure OpenAI deployment name and API version
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-07-01";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "dall-e-3";
+    
+    // The prompt to generate images from
+    const prompt = "a monkey eating a banana";
+    const numberOfImagesToGenerate = 1;
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    async function main() {
+      console.log("== Image Generation ==");
+    
+      const client = getClient();
+    
+      const results = await client.images.generate({
+        prompt,
+        size: "1024x1024",
+        n: numberOfImagesToGenerate,
+        model: "",
+        style: "vivid", // or "natural"
+      });
+    
+      for (const image of results.data) {
+        console.log(`Image generation result URL: ${image.url}`);
+      }
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
+    ```
 
-1. Build the application with the following command:
 
-    ```console
-    tsc
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
     ```
 
-1. Run the application with the following command:
+1. Transpile from TypeScript to JavaScript.
 
-    ```console
-    node ImageGeneration.js
+    ```shell
+    tsc
+    ```
+    
+1. Run the code with the following command:
+
+    ```shell
+    node index.js
     ```
 
 ---
@@ -190,8 +244,8 @@ The URL of the generated image is printed to the console.
 
 ```console
 == Batch Image Generation ==
-Image generation result URL: https://dalleproduse.blob.core.windows.net/private/images/5e7536a9-a0b5-4260-8769-2d54106f2913/generated_00.png?se=2023-08-29T19%3A12%3A57Z&sig=655GkWajOZ9ALjFykZF%2FBMZRPQALRhf4UPDImWCQoGI%3D&ske=2023-09-02T18%3A53%3A23Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2023-08-26T18%3A53%3A23Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02
-Image generation result URL: https://dalleproduse.blob.core.windows.net/private/images/5e7536a9-a0b5-4260-8769-2d54106f2913/generated_01.png?se=2023-08-29T19%3A12%3A57Z&sig=B24ymPLSZ3HfG23uojOD9VlRFGxjvgcNmvFo4yPUbEc%3D&ske=2023-09-02T18%3A53%3A23Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2023-08-26T18%3A53%3A23Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02
+Image generation result URL: <SAS URL>
+Image generation result URL: <SAS URL>
 ```
 
 > [!NOTE]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL·E TypeScriptガイドのSAS URLへの更新と構成手順の合理化"
}
```

### Explanation
この修正では、`dall-e-typescript.md`ファイルが大幅に更新され、DALL·Eを使用したTypeScriptアプリケーションの導入手順が改善されました。主要な変更点は以下の通りです：

1. **セットアップ手順の明確化**: ユーザーがアプリケーションを迅速にセットアップできるよう、新しいフォルダの作成や`package.json`ファイルの追加、ECMAScriptへの更新手順が具体的に示されました。これにより、初めてのユーザーでも容易に環境構築が行えるようになっています。

2. **画像生成URLのプレースホルダー化**: 実際の画像生成結果が記載されていたURLが「<SAS URL>」というプレースホルダーに変更されました。この変更により、ユーザーは自身の環境に応じたSAS（Shared Access Signature）URLを使用でき、特定のURLに依存せずに柔軟に対応できます。

3. **サンプルコードの改良**: サンプルコードが更新され、TypeScriptの標準に基づく適切な構成が反映されています。これにより、ユーザーはより洗練されたコードを元に開発を進めることができ、また環境変数の利用も強調されています。

4. **TypeScript設定ファイルの導入**: `tsconfig.json`ファイルが新たに追加され、TypeScriptのトランスパイルに必要な設定が具体的に示されています。これにより、ユーザーはコンパイルオプションを簡単に設定できます。

全体として、この更新はDALL·Eを使用するTypeScriptアプリケーションの導入をシンプルかつ効果的にし、開発者が画像生成を行う際の障壁を下げることを目指しています。

## articles/ai-services/openai/includes/fine-tuning-studio.md{#item-439f1e}

<details>
<summary>Diff</summary>
````diff
@@ -64,9 +64,16 @@ If you would like a step-by-step walk-through of fine-tuning a `gpt-4o-mini` (20
 ### Example file format
 
 ```json
-{"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
-{"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
-{"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
+{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "Who discovered Antarctica?"}, {"role": "assistant", "content": "Some chaps named Fabian Gottlieb von Bellingshausen and Mikhail Lazarev, as if they don't teach that in every school!"}]}
+{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What is the biggest ocean?"}, {"role": "assistant", "content": "The Pacific Ocean. It's not like it's a small pond or anything."}]}
+{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What is the largest planet?"}, {"role": "assistant", "content": "It's called Jupiter, you might have heard of it...or not."}]}
+{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "Who painted the Mona Lisa?"}, {"role": "assistant", "content": "Oh, some obscure artist named Leonardo da Vinci. Not that he is famous or anything."}]}
+{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What's the boiling point of water?"}, {"role": "assistant", "content": "Exciting fact of the day: it's 100 degrees Celsius. Life-changing, isn't it?"}]}
+{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "Who wrote 'The Odyssey'?"}, {"role": "assistant", "content": "Oh, just some poet named Homer. Nothing special, really."}]}
+{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What is the largest mammal?"}, {"role": "assistant", "content": "Blue Whale. Quite a big fish isn't it? Oh wait, it's not a fish!"}]}
+{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What's the highest mountain peak?"}, {"role": "assistant", "content": "Everest. Brace yourself, it's not a walk in the park."}]}
+{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "Who invented the telephone?"}, {"role": "assistant", "content": "A guy named Alexander Graham Bell. Bet you didn't guess that one!"}]}
+{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What is the distance from Earth to the Sun?"}, {"role": "assistant", "content": "About 93 million miles. Just a quick drive, really."}]}
 ```
 
 ### Multi-turn chat file format Azure OpenAI 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックレスポンスチャットボットの例の追加"
}
```

### Explanation
この変更では、`fine-tuning-studio.md`のドキュメントに新しいサンプルが追加され、特に「Clippy」というキャラクターを用いた皮肉を交えた会話の例が含まれています。主な変更点は以下の通りです：

1. **新しい例の追加**: 以前のサンプルがXbox関連のサポートエージェントの会話に重点を置いていたのに対し、更新されたサンプルでは「Clippy」が皮肉を交えた受け答えをするチャットボットとして描かれています。これにより、ドキュメントはより多様なユースケースに対応できるようになりました。

2. **JSONフォーマットの拡張**: 新しい会話例には、さまざまな質問とそれに対する皮肉的な回答が含まれています。具体的には、ユーザーが尋ねる一般的な知識に基づいた質問に対して、Clippyが素早く、かつユーモアを交えて答える形式となっています。

3. **サンプルの多様性**: 過去のサポートエージェントの視点から、汎用的な知識を持つキャラクターへの移行により、ドキュメントがより幅広い対象にアピールできるようになりました。これにより、新たなユーザー層の興味を引くことが期待されます。

この更新は、ユーザーに対してより魅力的でエンターテインメント的な要素を提供し、実際の応答性や対応範囲を広げることを目的としています。

## articles/ai-services/openai/includes/gpt-v-javascript.md{#item-a128c9}

<details>
<summary>Diff</summary>
````diff
@@ -32,39 +32,50 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 - Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
 - Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-## Retrieve resource information
+## Set up
+ 
+1. Create a new folder `vision-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-[!INCLUDE [resource authentication](resource-authentication.md)]
+    ```shell
+    mkdir vision-quickstart && cd vision-quickstart
+    ```
+    
 
-> [!CAUTION]
-> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+1. Create the `package.json` with the following command:
 
-## Create a Node application
+    ```shell
+    npm init -y
+    ```   
 
-In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+1. Install the OpenAI client library for JavaScript with:
 
-```console
-npm init
-```
+    ```console
+    npm install openai
+    ```
 
-## Install the client library
+1. For the **recommended** passwordless authentication:
 
-Install the client libraries with:
+    ```console
+    npm install @azure/identity
+    ```
 
-```console
-npm install openai @azure/identity
-```
+## Retrieve resource information
+
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
-Your app's _package.json_ file will be updated with the dependencies.
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Create a new JavaScript application for image prompts
 
-Select an image from the [azure-samples/cognitive-services-sample-data-files](https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images) and set the URL for an image in the environment variables.
+Select an image from the [azure-samples/cognitive-services-sample-data-files](https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images). Use the image URL in the code below or set the `IMAGE_URL` environment variable to the image URL.
 
+> [!TIP]
+> You can also use a base 64 encoded image data instead of a URL. For more information, see the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-a-local-image).
 
 ## [Microsoft Entra ID](#tab/keyless)
 
-1. Replace the contents of _quickstart.js_ with the following code. 
+1. Create the `index.js` file with the following code:
     
     ```javascript
     const AzureOpenAI = require('openai').AzureOpenAI;
@@ -74,12 +85,12 @@ Select an image from the [azure-samples/cognitive-services-sample-data-files](ht
     } = require('@azure/identity');
 
     // You will need to set these environment variables or edit the following values
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-    const imageUrl = process.env["IMAGE_URL"] || "<image url>";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const imageUrl = process.env.IMAGE_URL || "<image url>";
     
     // Required Azure OpenAI deployment name and API version
-    const apiVersion = "2024-07-01-preview";
-    const deploymentName = "gpt-4-with-turbo";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-07-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4-with-turbo";
     
     // keyless authentication    
     const credential = new DefaultAzureCredential();
@@ -137,34 +148,34 @@ Select an image from the [azure-samples/cognitive-services-sample-data-files](ht
     });
     ```
 
-1. Make the following changes:
-    1. Enter the name of your GPT-4 Turbo with Vision deployment in the appropriate field.
-    1. Change the value of the `"url"` field to the URL of your image.
-        > [!TIP]
-        > You can also use a base 64 encoded image data instead of a URL. For more information, see the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-a-local-image).
-1. Run the application with the following command:
+1. Sign in to Azure with the following command:
 
-    ```console
-    node quickstart.js
+    ```shell
+    az login
     ```
 
+1. Run the JavaScript file.
+
+    ```shell
+    node index.js
+    ```
 
 
 ## [API key](#tab/api-key)
 
-1. Replace the contents of _quickstart.js_ with the following code. 
+1. Create the `index.js` file with the following code: 
     
     ```javascript
     const { AzureOpenAI } = require("openai");
     
     // You will need to set these environment variables or edit the following values
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
-    const imageUrl = process.env["IMAGE_URL"] || "<image url>";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
+    const imageUrl = process.env.IMAGE_URL || "<image url>";
     
     // Required Azure OpenAI deployment name and API version
-    const apiVersion = "2024-07-01-preview";
-    const deploymentName = "gpt-4-with-turbo";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-07-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4-with-turbo";
     
     function getClient() {
       return new AzureOpenAI({
@@ -217,17 +228,11 @@ Select an image from the [azure-samples/cognitive-services-sample-data-files](ht
     });
     ```
 
-1. Make the following changes:
-    1. Enter the name of your GPT-4 Turbo with Vision deployment in the appropriate field.
-    1. Change the value of the `"url"` field to the URL of your image.
-        > [!TIP]
-        > You can also use a base 64 encoded image data instead of a URL. For more information, see the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-a-local-image).
-1. Run the application with the following command:
+1. Run the JavaScript file.
 
-    ```console
-    node quickstart.js
+    ```shell
+    node index.js
     ```
-[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptアプリケーションの設定と実行手順の更新"
}
```

### Explanation
この変更では、`gpt-v-javascript.md`ファイルが更新され、JavaScriptを使用したOpenAIのGPTモデルとの統合に関する手順が改善されました。主要な変更点は以下の通りです：

1. **セットアップ手順の明確化**: 新しいフォルダを作成し、Visual Studio Codeを開く手順が詳細に記載されており、開発環境のセットアップが容易になっています。具体的には、`vision-quickstart`フォルダの作成とそこに必要なファイルを配置する方法が明示されています。

2. **環境変数の使用推奨**: 各種設定において環境変数を使用することが強調されています。例えば、エンドポイントやAPIキー、イメージURLを環境変数から取得する方法が示され、コーディング時の柔軟性が向上しています。

3. **エラーハンドリングと実行コマンドの変更**: アプリケーションの実行手順が整理され、Azureにサインインするためのコマンド`az login`と、JavaScriptファイルを実行するコマンド`node index.js`が明示されています。これにより、ユーザーは正確な手順に従ってスムーズにアプリを実行できるようになります。

4. **Tipsの追加**: Base64エンコードされた画像データの使用に関するヒントが追加され、ユーザーは選択肢を持ったまま取り組むことができます。これにより、より多様な利用シナリオに対応可能となっています。

この更新は、OpenAIのAPIを使用したJavaScriptアプリケーションの構築における手順を整理し、ユーザーがより効率的に開発を進められるよう配慮されています。

## articles/ai-services/openai/includes/gpt-v-typescript.md{#item-03ec34}

<details>
<summary>Diff</summary>
````diff
@@ -33,39 +33,57 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 - Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
 - Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-## Retrieve resource information
+## Set up
 
-[!INCLUDE [resource authentication](resource-authentication.md)]
+1. Create a new folder `vision-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-> [!CAUTION]
-> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+    ```shell
+    mkdir vision-quickstart && cd vision-quickstart
+    ```
+    
 
-## Create a Node application
+1. Create the `package.json` with the following command:
 
-In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+    ```shell
+    npm init -y
+    ```
 
-```console
-npm init
-```
+1. Update the `package.json` to ECMAScript with the following command: 
 
-## Install the client library
+    ```shell
+    npm pkg set type=module
+    ```
+    
 
-Install the client libraries with:
+1. Install the OpenAI client library for JavaScript with:
 
-```console
-npm install openai @azure/identity
-```
+    ```console
+    npm install openai
+    ```
 
-Your app's _package.json_ file will be updated with the dependencies.
+1. For the **recommended** passwordless authentication:
+
+    ```console
+    npm install @azure/identity
+    ```
+
+## Retrieve resource information
+
+[!INCLUDE [resource authentication](resource-authentication.md)]
+
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Create a new JavaScript application for image prompts
 
-Select an image from the [azure-samples/cognitive-services-sample-data-files](https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images) and set the URL for an image in the environment variables.
+Select an image from the [azure-samples/cognitive-services-sample-data-files](https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images). Use the image URL in the code below or set the `IMAGE_URL` environment variable to the image URL.
 
+> [!TIP]
+> You can also use a base 64 encoded image data instead of a URL. For more information, see the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-a-local-image).
 
 ## [Microsoft Entra ID](#tab/typescript-keyless)
 
-1. Create a _quickstart.ts_ and paste in the following code. 
+1. Create the `index.ts` file with the following code:
     
     ```typescript
     import { AzureOpenAI } from "openai";
@@ -79,12 +97,12 @@ Select an image from the [azure-samples/cognitive-services-sample-data-files](ht
     } from "openai/resources/index";
     
     // You will need to set these environment variables or edit the following values
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
     const imageUrl = process.env["IMAGE_URL"] || "<image url>";
     
     // Required Azure OpenAI deployment name and API version
-    const apiVersion = "2024-07-01-preview";
-    const deploymentName = "gpt-4-with-turbo";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-07-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4-with-turbo";
     
     // keyless authentication    
     const credential = new DefaultAzureCredential();
@@ -141,29 +159,43 @@ Select an image from the [azure-samples/cognitive-services-sample-data-files](ht
       console.error("Error occurred:", err);
     });
     ```
-1. Make the following changes:
-    1. Enter the name of your GPT-4 Turbo with Vision deployment in the appropriate field.
-    1. Change the value of the `"url"` field to the URL of your image.
-        > [!TIP]
-        > You can also use a base 64 encoded image data instead of a URL. For more information, see the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-a-local-image).
 
-1. Build the application with the following command:
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
 
-    ```console
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
     tsc
     ```
+    
+1. Sign in to Azure with the following command:
 
-1. Run the application with the following command:
-
-    ```console
-    node quickstart.js
+    ```shell
+    az login
     ```
 
+1. Run the code with the following command:
 
+    ```shell
+    node index.js
+    ```
 
 ## [API key](#tab/typescript-key)
 
-1. Create a _quickstart.ts_ and paste in the following code. 
+1. Create the `index.ts` file with the following code:
     
     ```typescript
     import { AzureOpenAI } from "openai";
@@ -173,13 +205,13 @@ Select an image from the [azure-samples/cognitive-services-sample-data-files](ht
     } from "openai/resources/index";
     
     // You will need to set these environment variables or edit the following values
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
     const imageUrl = process.env["IMAGE_URL"] || "<image url>";
     
     // Required Azure OpenAI deployment name and API version
-    const apiVersion = "2024-07-01-preview";
-    const deploymentName = "gpt-4-with-turbo";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-07-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4-with-turbo";
     
     function getClient(): AzureOpenAI {
       return new AzureOpenAI({
@@ -231,25 +263,33 @@ Select an image from the [azure-samples/cognitive-services-sample-data-files](ht
       console.error("Error occurred:", err);
     });
     ```
-1. Make the following changes:
-    1. Enter the name of your GPT-4 Turbo with Vision deployment in the appropriate field.
-    1. Change the value of the `"url"` field to the URL of your image.
-        > [!TIP]
-        > You can also use a base 64 encoded image data instead of a URL. For more information, see the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-a-local-image).
-
-1. Build the application with the following command:
 
-    ```console
-    tsc
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
     ```
 
-1. Run the application with the following command:
+1. Transpile from TypeScript to JavaScript.
 
-    ```console
-    node quickstart.js
+    ```shell
+    tsc
     ```
+    
+1. Run the code with the following command:
 
-[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+    ```shell
+    node index.js
+    ```
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptアプリケーションの設定手順の拡充"
}
```

### Explanation
今回の変更では、`gpt-v-typescript.md`ファイルが更新され、TypeScriptを使用したOpenAIのGPTモデルとの統合に関する手順が整理され、細分化されています。主な変更内容は次の通りです：

1. **セットアップ手順の明確化**: 新しいフォルダ（`vision-quickstart`）の作成、Visual Studio Codeの起動、`package.json`の生成手順が追加され、ユーザーが環境を設定しやすくなっています。

2. **ECMAScriptの対応**: `package.json`にECMAScriptモジュールを設定するためのコマンド（`npm pkg set type=module`）が明示され、TypeScriptでのモジュール使用が容易になっています。

3. **クライアントライブラリのインストール方法の変更**: OpenAIのクライアントライブラリのインストール手順が更新され、Azureのアイデンティティライブラリをインストールする手順が追加されました。これにより、パスワードレス認証が可能になっています。

4. **構成ファイルの追加**: TypeScriptをコンパイルするための`tsconfig.json`ファイルの作成方法が追加され、型安全性を向上させるオプションが設定されています。

5. **アプリケーションの実行手順の明確化**: Azureへのサインイン手順とアプリケーションの実行コマンドがそれぞれ明文化されており、ユーザーが手順に従いやすくなっています。

6. **TIPやCAUTIONの追加**: 画像データのベース64エンコーディングに関するTIPおよびSDKを使用する際のCAUTIONが追加され、ユーザーに対する注意喚起が強化されています。

この更新によって、TypeScriptを使用する開発者がOpenAIのAPIをより効果的に利用できるように手順が整理され、環境の設定からアプリケーションの実行までのフローが改善されています。

## articles/ai-services/openai/includes/javascript.md{#item-f4828f}

<details>
<summary>Diff</summary>
````diff
@@ -59,9 +59,9 @@ const {
 } = require("@azure/identity");
 
 // You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-const apiVersion = "2024-04-01-preview";
-const deployment = "gpt-35-turbo-instruct"; //The deployment name for your completions API model. The instruct model is the only new model that supports the legacy API.
+const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+const apiVersion = process.env.OPENAI_API_VERSION || "2024-04-01-preview";
+const deployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-35-turbo-instruct"; //The deployment name for your completions API model. The instruct model is the only new model that supports the legacy API.
 
 // keyless authentication    
 const credential = new DefaultAzureCredential();
@@ -102,10 +102,10 @@ node.exe Completion.js
 const { AzureOpenAI } = require("openai");
 
 // You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
-const apiVersion = "2024-04-01-preview";
-const deployment = "gpt-35-turbo-instruct"; //The deployment name for your completions API model. The instruct model is the only new model that supports the legacy API.
+const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
+const apiVersion = process.env.OPENAI_API_VERSION || "2024-04-01-preview";
+const deployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-35-turbo-instruct"; //The deployment name for your completions API model. The instruct model is the only new model that supports the legacy API.
 
 const prompt = ["When was Microsoft founded?"];
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript環境変数の設定方法の改善"
}
```

### Explanation
この変更では、`javascript.md`ファイルが更新され、JavaScriptにおけるOpenAI APIの利用に関する環境変数の設定方法が改善されました。具体的な変更点は以下の通りです：

1. **環境変数の取り扱いの統一**: 環境変数から取得する値が改良され、コードの可読性が向上しました。特に、以前はハードコーディングされていたエンドポイント、APIバージョン、およびデプロイメント名が環境変数から取得されるようになりました。これにより、セキュアかつ柔軟に構成変更が行えるようになります。

    - 例: 
      - `const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";`
      - `const apiVersion = process.env.OPENAI_API_VERSION || "2024-04-01-preview";`
      - `const deployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-35-turbo-instruct";`

2. **一貫したエラーハンドリング**: 各環境変数が取得できない場合のデフォルト値が明示的に指定されることで、エラーの発生を未然に防ぐ設計がなされています。

この改良は、OpenAIのAPIを使用するJavaScriptの開発者にとって、環境設定の柔軟性とコードのメンテナンス性を向上させるものです。

## articles/ai-services/openai/includes/model-matrix/datazone-standard.md{#item-188333}

<details>
<summary>Diff</summary>
````diff
@@ -6,20 +6,20 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 02/19/2025
+ms.date: 02/25/2025
 ---
 
 | **Region**     | **o3-mini**, **2025-01-31**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
 |:-------------------|:---------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
 | eastus             | ✅                        | ✅                       | ✅                       | ✅                            |
 | eastus2            | ✅                        | ✅                       | ✅                       | ✅                            |
-| francecentral      | -                       | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | -                       | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                        | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                        | ✅                       | ✅                       | ✅                            |
 | northcentralus     | ✅                        | ✅                       | ✅                       | ✅                            |
-| polandcentral      | -                       | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                        | ✅                       | ✅                       | ✅                            |
 | southcentralus     | ✅                        | ✅                       | ✅                       | ✅                            |
-| spaincentral       | -                       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | -                       | ✅                       | ✅                       | ✅                            |
-| westeurope         | -                       | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                        | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                        | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                        | ✅                       | ✅                       | ✅                            |
 | westus             | ✅                        | ✅                       | ✅                       | ✅                            |
 | westus3            | ✅                        | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの地域対応状況の更新"
}
```

### Explanation
この変更では、`datazone-standard.md`ファイルが更新され、OpenAIモデルの地域対応状況に関する情報が改訂されました。具体的な変更内容は以下の通りです：

1. **対応地域の更新**: フランス中央、ドイツ西部、ポーランド中央、スペイン中央、スウェーデン中央、西ヨーロッパの各地域の対応状況が更新され、全てのモデル（o3-mini、gpt-4o、gpt-4o-mini）がこれらの地域で利用可能であることが示されています。

   - 例えば、以下のように各地域の対応が"✅"で示されています：
     - フランス中央: ✅
     - ドイツ西部: ✅
     - ポーランド中央: ✅
     - スペイン中央: ✅
     - スウェーデン中央: ✅
     - 西ヨーロッパ: ✅

2. **日付の更新**: ドキュメントの日付が更新され、提供される情報が最新であることを示しています。具体的には、日付が「2025年02月19日」から「2025年02月25日」に変更されています。

このアップデートにより、ユーザーは最新の地域支持状況を把握しやすくなり、適切な地域選択に基づいたモデルの利用が可能になります。

## articles/ai-services/openai/includes/model-matrix/provisioned-models.md{#item-8ee639}

<details>
<summary>Diff</summary>
````diff
@@ -6,32 +6,32 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 10/24/2024
+ms.date: 02/25/2024
 ---
 
-| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
-|:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|
-| australiaeast      | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| brazilsouth        | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | -                      |
-| canadacentral      | ✅                       | -                      | -                           | ✅                | -                       | -                       | -                           | ✅                    | -                      | ✅                       |
-| canadaeast         | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      |
-| eastus             | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| eastus2            | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| francecentral      | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | -                      | ✅                       |
-| germanywestcentral | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | -                      |
-| japaneast          | ✅                       | ✅                       | ✅                            | -               | ✅                        | ✅                        | ✅                            | -                   | -                      | ✅                       |
-| koreacentral       | ✅                       | ✅                       | ✅                            | ✅                | -                       | -                       | ✅                            | ✅                    | ✅                       | -                      |
-| northcentralus     | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| norwayeast         | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                           | ✅                    | -                      | -                      |
-| polandcentral      | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| southafricanorth   | ✅                       | -                      | -                           | ✅                | ✅                        | -                       | ✅                            | ✅                    | ✅                       | -                      |
-| southcentralus     | ✅                       | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| southeastasia      | -                      | ✅                       | ✅                            | -               | -                       | -                       | -                           | -                   | -                      | -                      |
-| southindia         | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | ✅                       |
-| swedencentral      | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| switzerlandnorth   | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| switzerlandwest    | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
-| uaenorth           | ✅                       | ✅                       | -                           | -               | ✅                        | -                       | -                           | -                   | ✅                       | ✅                       |
-| uksouth            | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| westus             | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| westus3            | ✅                       | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
+|:-------------------|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|
+| australiaeast      | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| brazilsouth        | ✅                       | -                      | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | -                      |
+| canadacentral      | ✅                       | -                      | -                      | -                           | ✅                | -                       | -                       | -                           | ✅                    | -                      | ✅                       |
+| canadaeast         | ✅                       | ✅                       | -                       | ✅                            | ✅                | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      |
+| eastus             | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| eastus2            | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| francecentral      | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | -                      | ✅                       |
+| germanywestcentral | ✅                       | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | -                      |
+| japaneast          | ✅                       | ✅                       | -                      | ✅                            | -               | ✅                        | ✅                        | ✅                            | -                   | -                      | ✅                       |
+| koreacentral       | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | -                       | ✅                            | ✅                    | ✅                       | -                      |
+| northcentralus     | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| norwayeast         | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                           | ✅                    | -                      | -                      |
+| polandcentral      | ✅                       | -                      | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| southafricanorth   | ✅                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                            | ✅                    | ✅                       | -                      |
+| southcentralus     | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| southeastasia      | -                      | ✅                       | -                      | ✅                            | -               | -                       | -                       | -                           | -                   | -                      | -                      |
+| southindia         | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | ✅                       |
+| swedencentral      | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| switzerlandnorth   | ✅                       | ✅                       | -                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| switzerlandwest    | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
+| uaenorth           | ✅                       | ✅                       | ✅                       | -                           | -               | ✅                        | -                       | -                           | -                   | ✅                       | ✅                       |
+| uksouth            | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| westus             | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| westus3            | ✅                       | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "提供されたモデルの地域対応状況の更新"
}
```

### Explanation
この変更では、`provisioned-models.md`ファイルが更新され、OpenAIの提供されるモデルの地域対応状況が見直され、情報が更新されました。具体的な変更内容は以下の通りです：

1. **地域対応状況の新たな整理**: モデルのバージョンについて、各地域の対応状況が変更され、新しいモデルバージョン（例：`gpt-4o`, `gpt-4o-mini`, `gpt-4`など）に対して地域の対応が明確に示されています。新たに追加されたモデルのバージョンも含まれており、各地域での利用可能性が更新されています。

   - 例えば、対応する地域でのモデルの利用可能性の表示が次のような形で改訂されています：
     - `gpt-4o`, **2024-11-20**: 各地域の対応状況に対するチェックマークの見直し。
     - 特定の地域での対応状況が"✅"または"-"で明示。

2. **日付の変更**: ドキュメントの日付が「2024年10月24日」から「2024年02月25日に」変更され、モデルの情報が最新であることを示しています。

この更新により、ユーザーはより正確で最新の地域ごとのモデルの対応状況を把握しやすくなり、プラットフォームにおける利用選択が容易になります。

## articles/ai-services/openai/includes/realtime-javascript.md{#item-3c125e}

<details>
<summary>Diff</summary>
````diff
@@ -29,7 +29,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create a new folder `realtime-audio-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
     ```shell
-    mkdir realtime-audio-quickstart && code realtime-audio-quickstart
+    mkdir realtime-audio-quickstart && cd realtime-audio-quickstart
     ```
     
 1. Create the `package.json` with the following command:
@@ -38,13 +38,6 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     npm init -y
     ```
 
-1. Update the `package.json` to ECMAScript with the following command: 
-
-    ```shell
-    npm pkg set type=module
-    ```
-    
-
 1. Install the real-time audio client library for JavaScript with:
 
     ```console
@@ -68,7 +61,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 #### [Microsoft Entra ID](#tab/keyless)
 
-1. Create the `text-in-audio-out.js` file with the following code:
+1. Create the `index.js` file with the following code:
 
     ```javascript 
     import { DefaultAzureCredential } from "@azure/identity";
@@ -77,8 +70,8 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     dotenv.config();
     async function text_in_audio_out() {
         // Set environment variables or edit the corresponding values here.
-        const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "yourEndpoint";
-        const deployment = "gpt-4o-mini-realtime-preview";
+        const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "YourEndpoint";
+        const deployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini-realtime-preview";
         if (!endpoint || !deployment) {
             throw new Error("You didn't set the environment variables.");
         }
@@ -131,13 +124,12 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Run the JavaScript file.
 
     ```shell
-    node text-in-audio-out.js
+    node index.js
     ```
 
-
 #### [API key](#tab/api-key)
 
-1. Create the `text-in-audio-out.js` file with the following code:
+1. Create the `index.js` file with the following code:
 
     ```javascript 
     import { AzureKeyCredential } from "@azure/core-auth";
@@ -146,9 +138,9 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     dotenv.config();
     async function text_in_audio_out() {
         // Set environment variables or edit the corresponding values here.
-        const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "yourKey";
-        const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "yourEndpoint";
-        const deployment = "gpt-4o-mini-realtime-preview";
+        const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
+        const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+        const deployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini-realtime-preview";
         if (!endpoint || !deployment) {
             throw new Error("You didn't set the environment variables.");
         }
@@ -195,7 +187,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Run the JavaScript file.
 
     ```shell
-    node text-in-audio-out.js
+    node index.js
     ```
 
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptファイル名と環境変数の整備"
}
```

### Explanation
この変更では、`realtime-javascript.md`ファイルが改訂され、JavaScriptのサンプルコードにおけるファイル名や環境変数の取り扱いについての説明が更新されました。主な変更内容は以下の通りです：

1. **ファイル名の一貫性の更新**: サンプルコードのファイル名が`text-in-audio-out.js`から`index.js`に変更され、これに伴い、文中でもこの変更が反映されています。すべての手順が新しいファイル名を指すように更新されました。

2. **環境変数の明確化**: 環境変数へのアクセスの方法が改良され、`process.env`を使用する形に統一されました。例えば、`AZURE_OPENAI_ENDPOINT`と`AZURE_OPENAI_DEPLOYMENT_NAME`が環境変数として明示され、デフォルト値も改善されました（例：`YourEndpoint`、`Your API key`）。

3. **手順の簡素化**: 更新された手順により、ユーザーはPython環境の設定や実行がよりスムーズに行えるようになります。また、手順内のコマンドが新しいファイル名に対応するように統一されています。

これにより、ユーザーはスクリプトの実行や環境設定をより簡単に行うことができ、エラーの発生を防ぐことが期待されます。

## articles/ai-services/openai/includes/realtime-python.md{#item-1291c0}

<details>
<summary>Diff</summary>
````diff
@@ -29,7 +29,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create a new folder `realtime-audio-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
     ```shell
-    mkdir realtime-audio-quickstart && code realtime-audio-quickstart
+    mkdir realtime-audio-quickstart && cd realtime-audio-quickstart
     ```
     
 1. Create a virtual environment. If you already have Python 3.10 or higher installed, you can create a virtual environment using the following commands:
@@ -95,8 +95,8 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     )
     
     # Set environment variables or edit the corresponding values here.
-    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
-    deployment = "gpt-4o-mini-realtime-preview"
+    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"] or "https://<your-resource-name>.openai.azure.com/"
+    deployment = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] or "gpt-4o-mini-realtime-preview"
     
     async def text_in_audio_out():
         async with RTLowLevelClient(
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonスクリプト環境変数の改善"
}
```

### Explanation
この変更では、`realtime-python.md`ファイルの内容が更新され、Pythonでのリアルタイムオーディオ処理に必要な環境変数の取り扱いが改良されました。主な変更点は次のとおりです：

1. **フォルダ作成コマンドの修正**: 新しいフォルダ`realtime-audio-quickstart`を作成する手順が修正され、コマンドが`cd realtime-audio-quickstart`に変更されました。これにより、ディレクトリに移動する手順が明確に示され、ユーザーが次のステップに進みやすくなっています。

2. **環境変数のデフォルト値の追加**: 環境変数`AZURE_OPENAI_ENDPOINT`と`AZURE_OPENAI_DEPLOYMENT_NAME`の取得方法が改善されました。これにより、もし環境変数が未設定の場合には、デフォルト値が提供されるようになりました。具体的には、`AZURE_OPENAI_ENDPOINT`のデフォルト値としてリソース名に基づくURLが設定され、ユーザーにとっての利便性が向上しています。

この更新により、ユーザーは設定に不備がある場合でも、スクリプトが正しく機能するための明確なガイダンスを受けられるようになり、エラーメッセージを軽減し、スクリプトの実行がスムーズになります。

## articles/ai-services/openai/includes/realtime-typescript.md{#item-eacc9c}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create a new folder `realtime-audio-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
     ```shell
-    mkdir realtime-audio-quickstart && code realtime-audio-quickstart
+    mkdir realtime-audio-quickstart && cd realtime-audio-quickstart
     ```
     
 
@@ -69,7 +69,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 #### [Microsoft Entra ID](#tab/keyless)
 
-1. Create the `text-in-audio-out.ts` file with the following code:
+1. Create the `index.ts` file with the following code:
 
     ```typescript
     import { DefaultAzureCredential } from "@azure/identity";
@@ -79,8 +79,8 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     
     async function text_in_audio_out() {
         // Set environment variables or edit the corresponding values here.
-        const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "yourEndpoint";
-        const deployment = "gpt-4o-mini-realtime-preview";
+        const endpoint: string = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+        const deployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini-realtime-preview";
         if (!endpoint || !deployment) {
             throw new Error("You didn't set the environment variables.");
         }
@@ -159,12 +159,12 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Run the code with the following command:
 
     ```shell
-    node text-in-audio-out.js
+    node index.js
     ```
 
 #### [API key](#tab/api-key)
 
-1. Create the `text-in-audio-out.ts` file with the following code:
+1. Create the `index.ts` file with the following code:
 
     ```typescript
     import { AzureKeyCredential } from "@azure/core-auth";
@@ -174,9 +174,9 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     
     async function text_in_audio_out() {
         // Set environment variables or edit the corresponding values here.
-        const apiKey: string = process.env["AZURE_OPENAI_API_KEY"] || "yourKey";
-        const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "yourEndpoint";
-        const deployment = "gpt-4o-mini-realtime-preview";
+        const apiKey: string = process.env.AZURE_OPENAI_API_KEY || "Your API key";
+        const endpoint: string = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+        const deployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini-realtime-preview";
         if (!endpoint || !deployment) {
             throw new Error("You didn't set the environment variables.");
         }
@@ -249,7 +249,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Run the code with the following command:
 
     ```shell
-    node text-in-audio-out.js
+    node index.js
     ```
 
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptファイル名と環境変数の整備"
}
```

### Explanation
この変更により、`realtime-typescript.md`ファイルが更新され、TypeScriptを用いたリアルタイムオーディオ処理に関するサンプルコードが改訂されました。主な修正点は次のとおりです：

1. **ファイル名の統一**: サンプルコード内のファイル名が`text-in-audio-out.ts`から`index.ts`に変更され、すべての手順が新しいファイル名を指し示すように調整されました。これによって、ユーザーがこのファイルを参照しやすくなっています。

2. **環境変数の設定方法の改善**: 環境変数にアクセスする際の記述が改善され、デフォルト値が明示的に設定されるようになりました。具体的には、環境変数`AZURE_OPENAI_ENDPOINT`と`AZURE_OPENAI_DEPLOYMENT_NAME`について、それぞれデフォルト値が適用されるようになりました。これにより、ユーザーは環境変数が未設定の場合でも有用な回避策を得ることが可能です。

3. **手順の明確化**: コード実行の手順においても、実行するスクリプト名が`text-in-audio-out.js`から`index.js`に変更され、手順が一貫性を持つようになりました。

このような変更により、ユーザーはスクリプトをより直感的に理解し、実行できるようになり、設定ミスやエラーメッセージの発生率を減少させることが期待されています。

## articles/ai-services/openai/includes/resource-authentication.md{#item-59aece}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ You need to retrieve the following information to authenticate your application
 |--------------------------|-------------|
 | `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. |
 | `AZURE_OPENAI_DEPLOYMENT_NAME` | This value will correspond to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Model Deployments** in the Azure portal.|
-| `OPENAI_API_VERSION`|Learn more about [API Versions](/azure/ai-services/openai/api-version-deprecation).|
+| `OPENAI_API_VERSION`|Learn more about [API Versions](/azure/ai-services/openai/api-version-deprecation).<br/><br/>You can change the version in code or use an environment variable.|
 
 Learn more about [keyless authentication](/azure/ai-services/authentication) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョン管理に関する説明の強化"
}
```

### Explanation
この変更では、`resource-authentication.md`ファイルの内容が更新され、OpenAI APIのバージョン管理に関する情報が強化されました。具体的には以下の点が重要です：

1. **APIバージョンの変更方法の明示**: `OPENAI_API_VERSION`に関する説明が修正され、ユーザーがコード内でバージョンを変更する方法や、環境変数を使用することができる旨が明確に示されています。これにより、ユーザーはAPIバージョンの設定に関して柔軟性を持って対応できるようになります。

2. **内容の説明の追加**: 改訂された行では、APIバージョンの管理に関する詳細が追記され、ユーザーがどのようにバージョンを変更できるかを理解しやすくするための具体的な指針が提供されています。

これにより、OpenAI APIを使用するユーザーは、バージョン管理についての理解が深まり、必要に応じて設定を調整しやすくなることが期待されます。

## articles/ai-services/openai/includes/text-to-speech-dotnet.md{#item-fea66a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.date: 09/23/2024
-ms.reviewer: v-baolianzou
+ms.reviewer: eur
 ms.author: alexwolf
 author: alexwolfmsft
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レビュアー情報の更新"
}
```

### Explanation
この変更では、`text-to-speech-dotnet.md`ファイルのメタデータが更新され、主にレビュアーに関する情報が修正されました。具体的には以下の点が挙げられます：

1. **レビュアーの変更**: 以前は`v-baolianzou`というレビュアーが指定されていましたが、これが`eur`に変更されました。この変更により、コンテンツのレビュープロセスが現在の体制に沿ったものになっています。

2. **メタデータへの影響**: この記事の更新は、小規模ではありますが、適切なレビュアーによる確認を促進し、結果的に文書の品質を向上させるための一環として重要です。

このように、レビュアー情報の更新は、文章の正確性や信頼性を維持するために重要な要素です。文書管理のプロセスが適切に行われることによって、ユーザーに対してより良い情報提供が行われることが期待されます。

## articles/ai-services/openai/includes/text-to-speech-javascript.md{#item-e9b653}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.date: 09/12/2024
-ms.reviewer: v-baolianzou
+ms.reviewer: eur
 ms.author: eur
 author: eric-urban
 recommendations: false
@@ -25,38 +25,44 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 - Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
 - Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-## Retrieve resource information
+## Set up
+ 
+1. Create a new folder `synthesis-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-[!INCLUDE [resource authentication](resource-authentication.md)]
+    ```shell
+    mkdir synthesis-quickstart && cd synthesis-quickstart
+    ```
+    
+1. Create the `package.json` with the following command:
 
-> [!CAUTION]
-> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+    ```shell
+    npm init -y
+    ```   
 
-## Create a Node application
+1. Install the OpenAI client library for JavaScript with:
 
-In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+    ```console
+    npm install openai
+    ```
 
-```console
-npm init
-```
+1. For the **recommended** passwordless authentication:
 
-## Install the client library
+    ```console
+    npm install @azure/identity
+    ```
 
-Install the client libraries with:
+## Retrieve resource information
 
-```console
-npm install openai @azure/identity
-```
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
-Your app's _package.json_ file will be updated with the dependencies.
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Create a speech file
 
-    
-
 #### [Microsoft Entra ID](#tab/keyless)
 
-1. Create a new file named _Text-to-speech.js_ and open it in your preferred code editor. Copy the following code into the _Text-to-speech.js_ file:
+1. Create the `index.js` file with the following code:
 
     ```javascript
     const { writeFile } = require("fs/promises");
@@ -65,12 +71,12 @@ Your app's _package.json_ file will be updated with the dependencies.
     require("openai/shims/node");
     
     // You will need to set these environment variables or edit the following values
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
     const speechFilePath = "<path to save the speech file>";
     
     // Required Azure OpenAI deployment name and API version
-    const deploymentName = "tts";
-    const apiVersion = "2024-08-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "tts";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-08-01-preview";
     
     // keyless authentication    
     const credential = new DefaultAzureCredential();
@@ -115,29 +121,35 @@ Your app's _package.json_ file will be updated with the dependencies.
     
     ```
 
-1. Run the script with the following command:
+1. Sign in to Azure with the following command:
 
-    ```console
-    node Text-to-speech.js
+    ```shell
+    az login
     ```
 
-#### [API key](#tab/api-key)
+1. Run the JavaScript file.
 
-1. Create a new file named _Text-to-speech.js_ and open it in your preferred code editor. Copy the following code into the _Text-to-speech.js_ file:
+    ```shell
+    node index.js
+    ```
+
+## [API key](#tab/api-key)
+
+1. Create the `index.js` file with the following code: 
 
     ```javascript
     const { writeFile } = require("fs/promises");
     const { AzureOpenAI } = require("openai");
     require("openai/shims/node");
     
     // You will need to set these environment variables or edit the following values
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
     const speechFilePath = "<path to save the speech file>";
     
     // Required Azure OpenAI deployment name and API version
-    const deploymentName = "tts";
-    const apiVersion = "2024-08-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "tts";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-08-01-preview";
     
     function getClient() {
       return new AzureOpenAI({
@@ -176,13 +188,11 @@ Your app's _package.json_ file will be updated with the dependencies.
     });
     
     ```
-[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
-1. Run the script with the following command:
+1. Run the JavaScript file.
 
-    ```console
-    node Text-to-speech.js
+    ```shell
+    node index.js
     ```
     
-
 ---
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptにおけるテキスト読み上げの手順を更新"
}
```

### Explanation
この変更では、`text-to-speech-javascript.md`ファイルの内容が大幅に改訂され、JavaScriptでのテキスト読み上げの手順がよりわかりやすく、実用的に更新されました。具体的な変更点は以下の通りです：

1. **レビュアーおよび著者情報の更新**: ファイルのメタデータが更新され、レビュアーが`v-baolianzou`から`eur`に変更され、著者も`eric-urban`から`eur`に変更されました。これにより、文書管理に一貫性と明確性が生まれます。

2. **手順の再構成**: 構成が整理され、手順が明確に示されるようになりました。新しく`Set up`というセクションが導入され、アプリケーションのセットアップ手順がより分かりやすくなっています。

3. **具体的なコマンドの追加**: 各手順に必要なコマンドが追加され、ユーザーがコピー＆ペーストで使用できる形式で提供されています。これにはディレクトリ作成、`package.json`の作成、OpenAIクライアントライブラリのインストールなどが含まれます。

4. **警告の強調**: 推奨されるパスワードレス認証を使用するための注意点が強調され、`AZURE_OPENAI_API_KEY`環境変数を設定しないよう注意喚起されています。

5. **ファイル名の変更**: 新しいファイル名`index.js`が登場し、ユーザーが作成するスクリプトの名前が統一されました。

これらの変更により、ユーザーはJavaScriptによるテキスト読み上げの手順がより分かりやすく、実行可能な形で提供されるようになり、プログラムの構築が容易になることが期待されます。

## articles/ai-services/openai/includes/text-to-speech-rest.md{#item-d067a1}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.date: 2/1/2024
-ms.reviewer: v-baolianzou
+ms.reviewer: eur
 ms.author: eur
 author: eric-urban
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レビュアー情報の更新"
}
```

### Explanation
この変更は、`text-to-speech-rest.md`ファイルのメタデータに関するもので、主にレビュアーの情報が更新されました。以下の点が変更されています：

1. **レビュアーの変更**: 以前はレビュアーとして`v-baolianzou`が指定されていましたが、これが`eur`に変更されました。この更新により、文書のレビュー体制が現在の人員に合わせて整えられています。

2. **著者情報の統一**: 著者情報も`eric-urban`から`eur`に変更され、文書の管理が一貫した形に整えられました。

このように、レビュアーおよび著者情報の整備は、文書の信頼性や正確性を保つために重要なステップであり、今後の更新や管理がスムーズに行われることを目指しています。変更は小規模ですが、大きな影響を与える可能性があります。

## articles/ai-services/openai/includes/text-to-speech-typescript.md{#item-1335d5}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.date: 09/12/2024
-ms.reviewer: v-baolianzou
+ms.reviewer: eur
 ms.author: eur
 author: eric-urban
 recommendations: false
@@ -26,38 +26,52 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 - Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
 - Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-## Retrieve resource information
+## Set up
 
-[!INCLUDE [resource authentication](resource-authentication.md)]
+1. Create a new folder `assistants-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-> [!CAUTION]
-> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+    ```shell
+    mkdir assistants-quickstart && cd assistants-quickstart
+    ```
+    
+
+1. Create the `package.json` with the following command:
 
-## Create a Node application
+    ```shell
+    npm init -y
+    ```
 
-In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+1. Update the `package.json` to ECMAScript with the following command: 
 
-```console
-npm init
-```
+    ```shell
+    npm pkg set type=module
+    ```
+    
 
-## Install the client library
+1. Install the OpenAI client library for JavaScript with:
 
-Install the client libraries with:
+    ```console
+    npm install openai
+    ```
 
-```console
-npm install openai @azure/identity
-```
+1. For the **recommended** passwordless authentication:
 
-Your app's _package.json_ file will be updated with the dependencies.
+    ```console
+    npm install @azure/identity
+    ```
 
-## Create a speech file
+## Retrieve resource information
 
-    
+[!INCLUDE [resource authentication](resource-authentication.md)]
+
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+
+## Create a speech file
 
 #### [Microsoft Entra ID](#tab/typescript-keyless)
 
-1. Create a new file named _Text-to-speech.ts_ and open it in your preferred code editor. Copy the following code into the _Text-to-speech.ts_ file:
+1. Create the `index.ts` file with the following code:
 
     ```typescript
     import { writeFile } from "fs/promises";
@@ -67,12 +81,12 @@ Your app's _package.json_ file will be updated with the dependencies.
     import "openai/shims/node";
     
     // You will need to set these environment variables or edit the following values
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
     const speechFilePath = "<path to save the speech file>";
     
     // Required Azure OpenAI deployment name and API version
-    const deploymentName = "tts";
-    const apiVersion = "2024-08-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "tts";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-08-01-preview";
 
     // keyless authentication    
     const credential = new DefaultAzureCredential();
@@ -119,22 +133,42 @@ Your app's _package.json_ file will be updated with the dependencies.
     
    The import of `"openai/shims/node"` is necessary when running the code in a Node.js environment. It ensures that the output type of the `client.audio.speech.create` method is correctly set to `NodeJS.ReadableStream`.
 
-1. Build the application with the following command:
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
 
-    ```console
+    ```shell
     tsc
     ```
+    
+1. Sign in to Azure with the following command:
 
-1. Run the application with the following command:
-
-    ```console
-    node Text-to-speech.js
+    ```shell
+    az login
     ```
 
+1. Run the code with the following command:
+
+    ```shell
+    node index.js
+    ```
 
 #### [API key](#tab/typescript-key)
 
-1. Create a new file named _Text-to-speech.ts_ and open it in your preferred code editor. Copy the following code into the _Text-to-speech.ts_ file:
+1. Create the `index.ts` file with the following code:
 
     ```typescript
     import { writeFile } from "fs/promises";
@@ -143,14 +177,14 @@ Your app's _package.json_ file will be updated with the dependencies.
     import "openai/shims/node";
     
     // You will need to set these environment variables or edit the following values
-    const endpoint = "<endpoint>";
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+    const endpoint = "Your endpoint";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
     const speechFilePath =
       process.env["SPEECH_FILE_PATH"] || "<path to save the speech file>";
     
     // Required Azure OpenAI deployment name and API version
-    const deploymentName = "tts";
-    const apiVersion = "2024-08-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "tts";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-08-01-preview";
     
     function getClient(): AzureOpenAI {
       return new AzureOpenAI({
@@ -192,17 +226,31 @@ Your app's _package.json_ file will be updated with the dependencies.
     
    The import of `"openai/shims/node"` is necessary when running the code in a Node.js environment. It ensures that the output type of the `client.audio.speech.create` method is correctly set to `NodeJS.ReadableStream`.
 
-1. Build the application with the following command:
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
 
-    ```console
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
     tsc
     ```
+    
+1. Run the code with the following command:
 
-1. Run the application with the following command:
-
-    ```console
-    node Text-to-speech.js
+    ```shell
+    node index.js
     ```
 
-[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 ---
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptでのテキスト読み上げ手順の更新"
}
```

### Explanation
この変更は、`text-to-speech-typescript.md`ファイルに対する修正で、TypeScriptを使用したテキスト読み上げの手順が拡充され、より具体的かつ使いやすくなりました。以下のポイントが特徴的です：

1. **レビュアー情報の更新**: 以前のレビュアーであった`v-baolianzou`が`eur`に変更され、文書のメタデータが整理されました。

2. **新セクションの追加**: `Set up`という新しいセクションが導入され、アプリケーションのセットアップ手順が段階的に詳しく説明されています。これは初心者にとっても理解しやすくなっています。

3. **具体的なコマンドの提供**: ユーザーが必要なコマンドを実行できるよう、ディレクトリの作成、`package.json`の初期化、モジュールタイプの設定などが追加されました。また、OpenAIクライアントライブラリのインストール手順が明示されています。

4. **TypeScriptにおける設定の明確化**: TypeScript用の`tsconfig.json`ファイルを作成する手順が追加され、コンパイラオプションの設定内容が具体的に示されています。これにより、環境設定が円滑に行えるようになります。

5. **コマンドの整理と統一**: ファイル名が`Text-to-speech.ts`から`index.ts`に変更され、またコマンドが整理され、実行時の流れが一貫して示されています。

6. **環境変数の使用についての注意点**: 推奨されるパスワードレス認証を使用する際の環境変数に関する注意喚起が強調され、使用者に対する明確なガイダンスが提供されています。

これらの更新により、TypeScriptを使用したテキスト読み上げの実装がより簡単になり、開発者が自分のアプリケーションにAI機能を統合する際の利便性が向上しています。

## articles/ai-services/openai/includes/typescript.md{#item-ee5b93}

<details>
<summary>Diff</summary>
````diff
@@ -60,11 +60,11 @@ import { AzureOpenAI } from "openai";
 import { type Completion } from "openai/resources/index";
 
 // You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
 
 // Required Azure OpenAI deployment name and API version
-const apiVersion = "2024-08-01-preview";
-const deploymentName = "gpt-35-turbo-instruct";
+const apiVersion = process.env.OPENAI_API_VERSION || "2024-08-01-preview";
+const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-35-turbo-instruct";
 
 // keyless authentication    
 const credential = new DefaultAzureCredential();
@@ -131,12 +131,12 @@ import { AzureOpenAI } from "openai";
 import { type Completion } from "openai/resources/index";
 
 // You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
 
 // Required Azure OpenAI deployment name and API version
-const apiVersion = "2024-08-01-preview";
-const deploymentName = "gpt-35-turbo-instruct";
+const apiVersion = process.env.OPENAI_API_VERSION || "2024-08-01-preview";
+const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-35-turbo-instruct";
 
 // Chat prompt and max tokens
 const prompt = ["When was Microsoft founded?"];
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "環境変数の使用による設定の改善"
}
```

### Explanation
この変更は、`typescript.md`ファイルにおけるコードの改善で、環境変数を使用することにより、設定方法をより柔軟かつ安全にしています。具体的な変更点は以下の通りです：

1. **エンドポイントの設定の見直し**: `AZURE_OPENAI_ENDPOINT`環境変数を用いてエンドポイントを設定する方法が更新され、デフォルト値として`"Your endpoint"`が指定されるようになりました。これにより、開発者は環境変数を簡単に設定できるようになっています。

2. **APIバージョンおよびデプロイ名の環境変数使用**: `apiVersion`と`deploymentName`も同様に環境変数を使って設定できるようになり、実行環境に応じた柔軟な対応が可能になりました。デフォルトでは、APIバージョンが`"2024-08-01-preview"`、デプロイ名が`"gpt-35-turbo-instruct"`とされています。

3. **キー管理の明確化**: 必要に応じて`AZURE_OPENAI_API_KEY`環境変数が使用される設定となっており、セキュリティを考慮した設計になっています。デフォルトでは`"Your API key"`が指定されています。

この変更によって、開発サイクルにおける環境設定が簡易化され、運用環境に応じた適切な設定が容易に行えるようになりました。また、環境変数を使用することにより、コードの可搬性とセキュリティが向上しています。

## articles/ai-services/openai/includes/use-your-data-common-variables.md{#item-c35afc}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ You need to retrieve the following information to authenticate your application
 |Variable name | Value |
 |--------------------------|-------------|
 | `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your Azure OpenAI resource from the Azure portal. An example endpoint is: `https://my-resoruce.openai.azure.com`.|
-| `AZURE_OPENAI_DEPLOYMENT_ID` | This value corresponds to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Deployments** in the Azure portal.|
+| `AZURE_OPENAI_DEPLOYMENT_NAME` | This value corresponds to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Deployments** in the Azure portal.|
 | `AZURE_AI_SEARCH_ENDPOINT` | This value can be found in the **Overview** section when examining your Azure AI Search resource from the Azure portal. |
 | `AZURE_AI_SEARCH_INDEX` | This value corresponds to the name of the index you created to store your data. You can find it in the **Overview** section when examining your Azure AI Search resource from the Azure portal. |
 
@@ -27,7 +27,7 @@ Learn more about [keyless authentication](/azure/ai-services/authentication) and
 |--------------------------|-------------|
 | `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your Azure OpenAI resource from the Azure portal. An example endpoint is: `https://my-resoruce.openai.azure.com`.|
 | `AZURE_OPENAI_API_KEY` | This value can be found in **Resource management** > **Keys & Endpoint** section when examining your Azure OpenAI resource from the Azure portal. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption. |
-| `AZURE_OPENAI_DEPLOYMENT_ID` | This value corresponds to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Deployments** in the Azure portal.|
+| `AZURE_OPENAI_DEPLOYMENT_NAME` | This value corresponds to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Deployments** in the Azure portal.|
 | `AZURE_AI_SEARCH_ENDPOINT` | This value can be found in the **Overview** section when examining your Azure AI Search resource from the Azure portal. |
 | `AZURE_AI_SEARCH_API_KEY` | This value can be found in the **Settings** > **Keys** section when examining your Azure AI Search resource from the Azure portal. You can use either the primary admin key or secondary admin key. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption. |
 | `AZURE_AI_SEARCH_INDEX` | This value corresponds to the name of the index you created to store your data. You can find it in the **Overview** section when examining your Azure AI Search resource from the Azure portal. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイIDの名称修正"
}
```

### Explanation
この変更は、`use-your-data-common-variables.md`ファイルに対する修正で、Azure OpenAIリソースに関連する変数名の更新が含まれています。主なポイントは以下の通りです：

1. **変数名の変更**: `AZURE_OPENAI_DEPLOYMENT_ID`という変数名が`AZURE_OPENAI_DEPLOYMENT_NAME`に変更されました。この変更は、リソースに関する説明の整合性を向上させ、開発者が理解しやすくなっています。

2. **変更箇所の反映**: 変更は、学習リソースの文脈において、デプロイメントを識別する際の変数名が一貫したものとなるよう、全体で統一されています。これにより、ユーザーに対する指示や説明が正確になります。

3. **他の変数の整合性**: その他の変数や関連情報（エンドポイント、APIキー、インデックス名など）については、変更なくそのまま維持されていますが、説明文との整合性が保たれています。

この更新により、Azureのドキュメントがより一貫性を持ち、利用者にとって分かりやすいものに改善されています。また、正しい変数名を使用することで、開発者がリソースを管理する際の可能性のある誤解を減少させることにも寄与しています。

## articles/ai-services/openai/includes/use-your-data-dotnet.md{#item-b811b8}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ using static System.Environment;
 
 string azureOpenAIEndpoint = GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
 string azureOpenAIKey = GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
-string deploymentName = GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT_ID");
+string deploymentName = GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT_NAME");
 string searchEndpoint = GetEnvironmentVariable("AZURE_AI_SEARCH_ENDPOINT");
 string searchKey = GetEnvironmentVariable("AZURE_AI_SEARCH_API_KEY");
 string searchIndex = GetEnvironmentVariable("AZURE_AI_SEARCH_INDEX");
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイIDの名称修正"
}
```

### Explanation
この変更は、`use-your-data-dotnet.md`ファイルに対する修正で、Azure OpenAIリソースに関連する変数名の更新が含まれています。主な内容は以下の通りです：

1. **変数名の変更**: `AZURE_OPENAI_DEPLOYMENT_ID`という変数が`AZURE_OPENAI_DEPLOYMENT_NAME`に変更されました。この修正により、コード内の変数名がより正確になり、開発者にとっての理解が向上します。

2. **一致性の向上**: 変数名を変更することにより、ドキュメント全体での用語の一貫性が保たれ、リソース管理がスムーズになります。その結果、ユーザーがリソースを設定する際の混乱を避けることができるようになります。

この更新は、ドキュメントの品質を向上させ、開発者が正しい変数名を使用してAzureのリソースにアクセスする手助けとなります。変更は機能に直接影響を与えるものではありませんが、正当な命名によってドキュメントの整合性と可読性を向上させる重要な改善です。

## articles/ai-services/openai/includes/use-your-data-go.md{#item-484724}

<details>
<summary>Diff</summary>
````diff
@@ -39,7 +39,7 @@ ms.date: 01/17/2025
    
    func main() {
    	azureOpenAIKey := os.Getenv("AZURE_OPENAI_API_KEY")
-   	modelDeploymentID := os.Getenv("AZURE_OPENAI_DEPLOYMENT_ID")
+   	modelDeploymentID := os.Getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    
    	// Ex: "https://<your-azure-openai-host>.openai.azure.com"
    	azureOpenAIEndpoint := os.Getenv("AZURE_OPENAI_ENDPOINT")
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイIDの名称修正"
}
```

### Explanation
この変更は、`use-your-data-go.md`ファイルに対する修正で、Azure OpenAIリソースに関連する変数名の更新が行われています。具体的には以下の点が修正されています：

1. **変数名の変更**: `AZURE_OPENAI_DEPLOYMENT_ID`という環境変数名が`AZURE_OPENAI_DEPLOYMENT_NAME`に変更されました。この修正により、コード内で使用されている変数名がより適切で、一貫性が持たせられています。

2. **コードの整合性**: この変更によって、他のドキュメントや例と合わせた表現になり、開発者にとって理解しやすくなります。正しい変数名を使用することで、ユーザーがAzureリソースにアクセスする際の混乱を減らすことが期待されます。

この更新は機能の追加や大きな変更とは言えませんが、ドキュメントの整合性と可読性を向上させ、ユーザーが正しい情報を取得できるようにするための重要な改善です。

## articles/ai-services/openai/includes/use-your-data-javascript.md{#item-786699}

<details>
<summary>Diff</summary>
````diff
@@ -10,48 +10,55 @@ ms.date: 01/10/2025
 
 [!INCLUDE [Set up required variables](./use-your-data-common-variables.md)]
 
+## Set up
+ 
+1. Create a new folder `use-data-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-## Initialize a Node.js application
-
-In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+    ```shell
+    mkdir use-data-quickstart && cd use-data-quickstart
+    ```
+    
+1. Create the `package.json` with the following command:
 
-```console
-npm init
-```
+    ```shell
+    npm init -y
+    ```   
 
-## Install the client library
+1. Install the OpenAI client library for JavaScript with:
 
-Install the Azure OpenAI client and Azure Identity libraries for JavaScript with npm:
+    ```console
+    npm install openai
+    ```
 
-```console
-npm install openai @azure/identity
-```
+1. For the **recommended** passwordless authentication:
 
-Your app's _package.json_ file will be updated with the dependencies.
+    ```console
+    npm install @azure/identity
+    ```
 
 ## Add the JavaScript code
 
 #### [Microsoft Entra ID](#tab/keyless)
 
-1. Open a command prompt where you want the new project, and create a new file named `ChatWithOwnData.js`. Copy the following code into the `ChatWithOwnData.js` file.
+1. Create the `index.js` file with the following code: 
     
     ```javascript
     const { DefaultAzureCredential, getBearerTokenProvider } = require("@azure/identity");
     const { AzureOpenAI } = require("openai");
     
     // Set the Azure and AI Search values from environment variables
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
-    const searchEndpoint = process.env["AZURE_AI_SEARCH_ENDPOINT"];
-    const searchIndex = process.env["AZURE_AI_SEARCH_INDEX"];
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const searchEndpoint = process.enV.AZURE_AI_SEARCH_ENDPOINT || "Your search endpoint";
+    const searchIndex = process.env.AZURE_AI_SEARCH_INDEX || "Your search index";
 
     // keyless authentication    
     const credential = new DefaultAzureCredential();
     const scope = "https://cognitiveservices.azure.com/.default";
     const azureADTokenProvider = getBearerTokenProvider(credential, scope);
 
     // Required Azure OpenAI deployment name and API version
-    const deploymentName = "gpt-4";
-    const apiVersion = "2024-10-21";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-10-21";
     
     function getClient() {
       return new AzureOpenAI({
@@ -116,30 +123,35 @@ Your app's _package.json_ file will be updated with the dependencies.
     });
     ```
 
-1. Run the application with the following command:
+1. Sign in to Azure with the following command:
 
-    ```console
-    node ChatWithOwnData.js
+    ```shell
+    az login
     ```
 
+1. Run the JavaScript file.
+
+    ```shell
+    node index.js
+    ```
 
-#### [API key](#tab/api-key)
+## [API key](#tab/api-key)
 
-1. Open a command prompt where you want the new project, and create a new file named `ChatWithOwnData.js`. Copy the following code into the `ChatWithOwnData.js` file.
+1. Create the `index.js` file with the following code: 
     
     ```javascript
     const { AzureOpenAI } = require("openai");
     
     // Set the Azure and AI Search values from environment variables
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"];
-    const searchEndpoint = process.env["AZURE_AI_SEARCH_ENDPOINT"];
-    const searchKey = process.env["AZURE_AI_SEARCH_API_KEY"];
-    const searchIndex = process.env["AZURE_AI_SEARCH_INDEX"];
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
+    const searchEndpoint = process.env.AZURE_AI_SEARCH_ENDPOINT || "Your search endpoint";
+    const searchKey = process.env.AZURE_AI_SEARCH_API_KEY || "Your search key";
+    const searchIndex = process.env.AZURE_AI_SEARCH_INDEX || "Your search index";
     
     // Required Azure OpenAI deployment name and API version
-    const deploymentName = "gpt-4";
-    const apiVersion = "2024-10-21";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-10-21";
     
     function getClient() {
       return new AzureOpenAI({
@@ -204,19 +216,15 @@ Your app's _package.json_ file will be updated with the dependencies.
     });
     ```
 
-1. Run the application with the following command:
+1. Run the JavaScript file.
 
-    ```console
-    node ChatWithOwnData.js
+    ```shell
+    node index.js
     ```
 
 ---
 
 
-> [!IMPORTANT]
-> For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see the Azure AI services [security](../../security-features.md) article.
-
-
 ## Output
 
 ```output
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptサンプルの更新"
}
```

### Explanation
この変更は、`use-your-data-javascript.md`ファイルに対する修正で、主にJavaScriptを使用してAzure OpenAIを設定する手順が更新されています。具体的には以下の点が修正されています：

1. **設計の改善**: 新しいフォルダを作成する手順やアプリケーションをVisual Studio Codeで開く手順が追加され、初期設定が明確になりました。

2. **コマンドの簡略化**: `npm init`コマンドを`npm init -y`に変更し、デフォルト設定でpackage.jsonを作成するようにしました。また、OpenAIのクライアントライブラリをインストールする手順が明確になり、ユーザーへの実行方法が整理されました。

3. **環境変数の使用**: APIエンドポイントやキーを取得する際に、環境変数からの取得に加え、デフォルト値を設定する方法が示されるようになりました。この変更により、必須情報が欠けている場合でも、プログラムが正常に動作するようになります。

4. **ファイル名の統一**: `ChatWithOwnData.js`から`index.js`にファイル名が変更され、コードの実行手順が更新されたことで、開発者が使用する際の一貫性が保たれています。

この更新は、ドキュメントの可読性を向上させ、初心者でも手順を追いやすくするための重要な改善であり、Azure OpenAIの利用を促進しています。

## articles/ai-services/openai/includes/use-your-data-python.md{#item-3dc5e2}

<details>
<summary>Diff</summary>
````diff
@@ -54,7 +54,7 @@ dotenv.load_dotenv()
 
 endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
 api_key = os.environ.get("AZURE_OPENAI_API_KEY")
-deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT_ID")
+deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")
 
 client = openai.AzureOpenAI(
     azure_endpoint=endpoint,
@@ -132,12 +132,12 @@ print(f"{completion.choices[0].message.role}: {completion.choices[0].message.con
 
        openai.requestssession = session
 
-   aoai_deployment_id = os.environ.get("AZURE_OPENAI_DEPLOYMENT_ID")
+   aoai_deployment_id = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")
    setup_byod(aoai_deployment_id)
 
    completion = openai.ChatCompletion.create(
        messages=[{"role": "user", "content": "What are my available health plans?"}],
-       deployment_id=os.environ.get("AZURE_OPENAI_DEPLOYMENT_ID"),
+       deployment_id=os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME"),
        dataSources=[  # camelCase is intentional, as this is the format the API expects
            {
                "type": "AzureCognitiveSearch",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントIDの名称修正"
}
```

### Explanation
この変更は、`use-your-data-python.md`ファイルに対する修正で、Azure OpenAIに関連する変数名が更新されています。具体的には以下の点が修正されています：

1. **変数名の変更**: 元の環境変数名`AZURE_OPENAI_DEPLOYMENT_ID`が`AZURE_OPENAI_DEPLOYMENT_NAME`に変更されました。この変更により、コード内での変数名がより直感的かつ一貫性のあるものとなり、開発者が理解しやすくなっています。

2. **コードの整合性**: これらの修正により、他の部分との整合性が取れ、同じドキュメント内で複数の言語での使用が統一されます。特に、ユーザーが異なるプログラミング言語で同様の概念を理解するのに役立ちます。

3. **引数の統一**: `AzureOpenAI`クライアントや、チャット補完の呼び出しにおいて、デプロイメント名の指定も同様に変更されています。このことは、エンドユーザーにとってより理解しやすく、間違いを避ける助けになります。

この更新は、機能の大きな変更や新機能の追加ではないものの、コードの可読性を高め、開発者が正しい情報を参照しやすくするために重要な改善です。

## articles/ai-services/openai/includes/use-your-data-rest.md{#item-d1e071}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ To trigger a response from the model, you should end with a user message indicat
 > There are several parameters you can use to change the model's response, such as `temperature` or `top_p`. See the [reference documentation](../reference.md#completions-extensions) for more information.
 
 ```bash
-curl -i -X POST $AZURE_OPENAI_ENDPOINT/openai/deployments/$AZURE_OPENAI_DEPLOYMENT_ID/chat/completions?api-version=2024-10-21 \
+curl -i -X POST $AZURE_OPENAI_ENDPOINT/openai/deployments/$AZURE_OPENAI_DEPLOYMENT_NAME/chat/completions?api-version=2024-10-21 \
 -H "Content-Type: application/json" \
 -H "api-key: $AZURE_OPENAI_API_KEY" \
 -d \
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントIDの名称修正"
}
```

### Explanation
この変更は、`use-your-data-rest.md`ファイルに対する修正で、Azure OpenAIのREST APIを呼び出す際のデプロイメントIDに関する記述が更新されています。具体的には以下の点が修正されています：

1. **変数名の変更**: `$AZURE_OPENAI_DEPLOYMENT_ID`が`$AZURE_OPENAI_DEPLOYMENT_NAME`に変更されました。この更新により、API呼び出しの文脈で使用される環境変数がより直感的で一貫性のあるものとなり、開発者にとって理解しやすくなっています。

2. **全体の整合性の向上**: この変更により、他のドキュメントやプログラミング言語での表記と整合性が保たれ、ユーザーが異なる環境や言語を扱う際に混乱を避けることができるようになります。

この更新は、コーディングの正確性や可読性を向上させるための重要な修正であり、エンドユーザーが正しい変数名を使用することでAPIの利用を円滑にします。

## articles/ai-services/openai/includes/use-your-data-typescript.md{#item-ec0b7e}

<details>
<summary>Diff</summary>
````diff
@@ -10,52 +10,62 @@ ms.date: 10/22/2024
 
 [!INCLUDE [Set up required variables](./use-your-data-common-variables.md)]
 
+## Set up
 
-## Initialize a Node.js application
+1. Create a new folder `use-data-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
-
-```console
-npm init
-```
+    ```shell
+    mkdir use-data-quickstart && cd use-data-quickstart
+    ```
+    
+1. Create the `package.json` with the following command:
 
-## Install the client library
+    ```shell
+    npm init -y
+    ```
 
-Install the Azure OpenAI client and Azure Identity libraries for JavaScript with npm:
+1. Update the `package.json` to ECMAScript with the following command: 
 
-```console
-npm install openai @azure/identity @azure/openai 
-```
+    ```shell
+    npm pkg set type=module
+    ```
+    
+1. Install the OpenAI client library for JavaScript with:
 
-The `@azure/openai/types` dependency is included to extend the Azure OpenAI model for the `data_sources` property. This import is only necessary for TypeScript.
+    ```console
+    npm install openai
+    ```
 
+1. For the **recommended** passwordless authentication:
 
-Your app's _package.json_ file will be updated with the dependencies.
+    ```console
+    npm install @azure/identity
+    ```
 
 ## Add the TypeScript code
 
 #### [Microsoft Entra ID](#tab/typescript-keyless)
 
-1. Open a command prompt where you want the new project, and create a new file named `ChatWithOwnData.ts`. Copy the following code into the `ChatWithOwnData.ts` file.
+1. Create the `index.ts` file with the following code:
     
     ```typescript
     import { AzureOpenAI } from "openai";
     import { DefaultAzureCredential, getBearerTokenProvider } from "@azure/identity";
     import "@azure/openai/types";
     
     // Set the Azure and AI Search values from environment variables
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
-    const searchEndpoint = process.env["AZURE_AI_SEARCH_ENDPOINT"];
-    const searchIndex = process.env["AZURE_AI_SEARCH_INDEX"];
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const searchEndpoint = process.env.AZURE_AI_SEARCH_ENDPOINT || "Your search endpoint";
+    const searchIndex = process.env.AZURE_AI_SEARCH_INDEX || "Your search index";
     
     // keyless authentication    
     const credential = new DefaultAzureCredential();
     const scope = "https://cognitiveservices.azure.com/.default";
     const azureADTokenProvider = getBearerTokenProvider(credential, scope);
 
     // Required Azure OpenAI deployment name and API version
-    const deploymentName = "gpt-4";
-    const apiVersion = "2024-07-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-07-01-preview";
     
     function getClient(): AzureOpenAI {
       return new AzureOpenAI({
@@ -120,37 +130,57 @@ Your app's _package.json_ file will be updated with the dependencies.
     });
     ```
 
-1. Build the application with the following command:
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
 
-    ```console
+    ```shell
     tsc
     ```
+    
+1. Sign in to Azure with the following command:
 
-1. Run the application with the following command:
-
-    ```console
-    node ChatWithOwnData.js
+    ```shell
+    az login
     ```
 
+1. Run the code with the following command:
+
+    ```shell
+    node index.js
+    ```
 
 #### [API key](#tab/typescript-key)
 
-1. Open a command prompt where you want the new project, and create a new file named `ChatWithOwnData.ts`. Copy the following code into the `ChatWithOwnData.ts` file.
+1. Create the `index.ts` file with the following code:
     
     ```typescript
     import { AzureOpenAI } from "openai";
     import "@azure/openai/types";
     
     // Set the Azure and AI Search values from environment variables
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"];
-    const searchEndpoint = process.env["AZURE_AI_SEARCH_ENDPOINT"];
-    const searchKey = process.env["AZURE_AI_SEARCH_API_KEY"];
-    const searchIndex = process.env["AZURE_AI_SEARCH_INDEX"];
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
+    const searchEndpoint = process.env.AZURE_AI_SEARCH_ENDPOINT || "Your search endpoint";
+    const searchKey = process.env.AZURE_AI_SEARCH_API_KEY || "Your search key";
+    const searchIndex = process.env.AZURE_AI_SEARCH_INDEX || "Your search index";
     
     // Required Azure OpenAI deployment name and API version
-    const deploymentName = "gpt-4";
-    const apiVersion = "2024-07-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-07-01-preview";
     
     function getClient(): AzureOpenAI {
       return new AzureOpenAI({
@@ -215,19 +245,33 @@ Your app's _package.json_ file will be updated with the dependencies.
     });
     ```
 
-1. Build the application with the following command:
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
 
-    ```console
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
     tsc
     ```
 
-1. Run the application with the following command:
+1. Run the code with the following command:
 
-    ```console
-    node ChatWithOwnData.js
+    ```shell
+    node index.js
     ```
 
-
 ---
 
 
@@ -240,6 +284,5 @@ Your app's _package.json_ file will be updated with the dependencies.
 ```output
 Message: What are my available health plans?
 The available health plans in the Contoso Electronics plan and benefit packages are the Northwind Health Plus and Northwind Standard plans.
-
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptでのアプリケーションセットアップ手順の改善"
}
```

### Explanation
この変更は、`use-your-data-typescript.md`ファイルに対する修正で、TypeScriptを使用したAzure OpenAIアプリケーションのセットアップ手順が強化されています。具体的には以下の点が改善されています：

1. **手順の詳細化**: アプリケーションのフォルダ作成や初期設定、必要なパッケージのインストール手順が詳細に示され、初心者にも分かりやすい形に改善されています。具体的には、コマンドが分割され、各段階での説明が追加されました。

2. **設定ファイルの追加**: TypeScript コードをトランスパイルするための`tsconfig.json`ファイルを作成する手順が追加され、これにより、ECMAScriptモジュール対応の構成が明示的に示されました。

3. **環境変数の取り扱い**: 環境変数の設定に関する行が改善され、デフォルト値も明示されるようになりました。これにより、必要な変数が設定されていない場合でも、コードの動作に影響を与えにくくなっています。

この更新により、TypeScriptを使用した開発者にとって、Azure OpenAIサービスの利用がより直感的でスムーズに行えるようになっています。全体的なドキュメントの整合性と使いやすさが向上し、ユーザーや開発者の経験が向上することを目指しています。

## articles/ai-services/openai/includes/whisper-javascript.md{#item-3ee990}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.date: 10/22/2024
-ms.reviewer: v-baolianzou
+ms.reviewer: eur
 ms.author: eur
 author: eric-urban
 ---
@@ -24,37 +24,44 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 - Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
 - Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-## Retrieve resource information
+## Set up
+ 
+1. Create a new folder `synthesis-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-[!INCLUDE [resource authentication](resource-authentication.md)]
+    ```shell
+    mkdir synthesis-quickstart && cd synthesis-quickstart
+    ```
+    
+1. Create the `package.json` with the following command:
 
-> [!CAUTION]
-> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+    ```shell
+    npm init -y
+    ```   
 
-## Create a Node application
+1. Install the OpenAI client library for JavaScript with:
 
-In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+    ```console
+    npm install openai
+    ```
 
-```console
-npm init
-```
+1. For the **recommended** passwordless authentication:
 
-## Install the client library
+    ```console
+    npm install @azure/identity
+    ```
 
-Install the client libraries with:
+## Retrieve resource information
 
-```console
-npm install openai @azure/identity
-```
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
----
-Your app's _package.json_ file will be updated with the dependencies.
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Create a sample application
 
 #### [Microsoft Entra ID](#tab/keyless)
 
-1. Create a new file named _Whisper.js_ and open it in your preferred code editor. Copy the following code into the _Whisper.js_ file:
+1. Create the `index.js` file with the following code: 
 
     ```javascript
     const { createReadStream } = require("fs");
@@ -63,11 +70,11 @@ Your app's _package.json_ file will be updated with the dependencies.
     
     // You will need to set these environment variables or edit the following values
     const audioFilePath = "<audio file path>";
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
     
     // Required Azure OpenAI deployment name and API version
-    const apiVersion = "2024-08-01-preview";
-    const deploymentName = "whisper";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-08-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "whisper";
     
     // keyless authentication    
     const credential = new DefaultAzureCredential();
@@ -100,26 +107,30 @@ Your app's _package.json_ file will be updated with the dependencies.
     });
     ```
 
-1. Run the script with the following command:
+1. Sign in to Azure with the following command:
 
-    ```console
-    node Whisper.js
+    ```shell
+    az login
     ```
 
+1. Run the JavaScript file.
 
+    ```shell
+    node index.js
+    ```
 
-#### [API key](#tab/typescript-key)
+## [API key](#tab/api-key)
 
-1. Create a new file named _Whisper.js_ and open it in your preferred code editor. Copy the following code into the _Whisper.js_ file:
+1. Create the `index.js` file with the following code: 
     
     ```javascript
     import { createReadStream } from "fs";
     import { AzureOpenAI } from "openai";
     
     // You will need to set these environment variables or edit the following values
     const audioFilePath = "<audio file path>";
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
     
     // Required Azure OpenAI deployment name and API version
     const apiVersion = "2024-08-01-preview";
@@ -151,23 +162,22 @@ Your app's _package.json_ file will be updated with the dependencies.
     });
     ```
 
-1. Build the application with the following command:
+1. Sign in to Azure with the following command:
 
-    ```console
-    tsc
+    ```shell
+    az login
     ```
 
-1. Run the application with the following command:
+1. Run the JavaScript file.
 
-    ```console
-    node Whisper.js
+    ```shell
+    node index.js
     ```
 
 ---
 
 You can get sample audio files, such as *wikipediaOcelot.wav*, from the [Azure AI Speech SDK repository at GitHub](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/sampledata/audiofiles).
 
-[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 ## Output
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisper APIのJavaScriptサンプルコードの改善"
}
```

### Explanation
この変更は、`whisper-javascript.md`ファイルに対する修正で、Whisper APIを利用するJavaScriptアプリケーションの構成手順やサンプルコードが改善されています。具体的な変更点は以下のとおりです：

1. **手順の整理と強化**: アプリケーションのセットアップ手順がより明確に順序立てられ、各ステップの説明が追加されました。特に、フォルダの作成や依存関係のインストールがより具体的に記載されています。

2. **ファイル名の統一**: 新たに作成するファイルの名前が`Whisper.js`から`index.js`に統一され、コード例もそれに合わせて修正されています。この変更により、コードの一貫性が保たれています。

3. **環境変数の取り扱い**: 環境変数の設定方法が明示化されており、デフォルト値を設定することで、コード実行時のエラーを回避できるようになっています。また、APIのバージョンとデプロイメント名も環境変数から取得できるように更新されています。

4. **認証手順の更新**: Microsoft Entra IDを使用したキーなし認証に関する情報が整理され、注意事項が強調されるようになりました。また、Azureにサインインする手順も追加されており、ユーザーがスムーズにアプリケーションを実行できるようになっています。

この改定により、Whisper APIに基づいたJavaScriptアプリケーションの開発がより効果的に行えるようになり、ユーザーにとって使いやすさと明確さが向上しています。

## articles/ai-services/openai/includes/whisper-powershell.md{#item-7db269}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.date: 2/1/2024
-ms.reviewer: v-baolianzou
+ms.reviewer: eur
 ms.author: eur
 author: eric-urban
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisper PowerShell ドキュメントのレビュアー情報の更新"
}
```

### Explanation
この変更は、`whisper-powershell.md`ファイルに対して行われたもので、主にレビュアー情報の更新が含まれています。具体的には、レビュアーの名前が`v-baolianzou`から`eur`に変更されており、これにより文書の責任者やレビュー担当者が明確になります。この修正は、文書管理や更新プロセスの透明性を高めるための重要なステップです。全体としては、情報の更新に関する軽微な変更と位置付けられます。

## articles/ai-services/openai/includes/whisper-rest.md{#item-639ccb}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.date: 2/1/2024
-ms.reviewer: v-baolianzou
+ms.reviewer: eur
 ms.author: eur
 author: eric-urban
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisper REST APIドキュメントのレビュアー情報の更新"
}
```

### Explanation
この変更は、`whisper-rest.md`ファイルに対するもので、レビュアー情報が更新されています。具体的には、元々のレビュアーである`v-baolianzou`から新しいレビュアーである`eur`に変更されています。この変更は、文書の質を保証するためのレビュープロセスを明確にし、関連する責任者を最新の情報に合わせる重要なステップです。全体として、これは文書の更新に伴う軽微な修正として位置付けられます。

## articles/ai-services/openai/includes/whisper-typescript.md{#item-eafedb}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.date: 10/22/2024
-ms.reviewer: v-baolianzou
+ms.reviewer: eur
 ms.author: eur
 author: eric-urban
 ---
@@ -24,37 +24,51 @@ author: eric-urban
 For the recommended keyless authentication with Microsoft Entra ID, you need to:
 - Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
 - Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
+## Set up
 
-## Retrieve resource information
+1. Create a new folder `whisper-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-[!INCLUDE [resource authentication](resource-authentication.md)]
+    ```shell
+    mkdir whisper-quickstart && cd whisper-quickstart
+    ```
+    
+1. Create the `package.json` with the following command:
 
-> [!CAUTION]
-> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+    ```shell
+    npm init -y
+    ```
 
-## Create a Node application
+1. Update the `package.json` to ECMAScript with the following command: 
 
-In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+    ```shell
+    npm pkg set type=module
+    ```
+    
 
-```console
-npm init
-```
+1. Install the OpenAI client library for JavaScript with:
 
-## Install the client library
+    ```console
+    npm install openai
+    ```
 
-Install the client libraries with:
+1. For the **recommended** passwordless authentication:
 
-```console
-npm install openai @azure/identity
-```
+    ```console
+    npm install @azure/identity
+    ```
 
-Your app's _package.json_ file will be updated with the dependencies.
+## Retrieve resource information
+
+[!INCLUDE [resource authentication](resource-authentication.md)]
+
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Create a sample application
 
 #### [Microsoft Entra ID](#tab/typescript-keyless)
 
-1. Create a new file named _Whisper.ts_ and open it in your preferred code editor. Copy the following code into the _Whisper.ts_ file:
+1. Create the `index.ts` file with the following code:
     
     ```typescript
     import { createReadStream } from "fs";
@@ -63,11 +77,11 @@ Your app's _package.json_ file will be updated with the dependencies.
 
     // You will need to set these environment variables or edit the following values
     const audioFilePath = "<audio file path>";
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
     
     // Required Azure OpenAI deployment name and API version
-    const apiVersion = "2024-08-01-preview";
-    const deploymentName = "whisper";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-08-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "whisper";
 
     // keyless authentication    
     const credential = new DefaultAzureCredential();
@@ -100,34 +114,56 @@ Your app's _package.json_ file will be updated with the dependencies.
     });
     ```
 
-1. Build the application with the following command:
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
 
-    ```console
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
     tsc
     ```
+    
+1. Sign in to Azure with the following command:
 
-1. Run the application with the following command:
+    ```shell
+    az login
+    ```
 
-    ```console
-    node Whisper.js
+1. Run the code with the following command:
+
+    ```shell
+    node index.js
     ```
 
+
 #### [API key](#tab/typescript-key)
 
-1. Create a new file named _Whisper.ts_ and open it in your preferred code editor. Copy the following code into the _Whisper.ts_ file:
+1. Create the `index.ts` file with the following code:
     
     ```typescript
     import { createReadStream } from "fs";
     import { AzureOpenAI } from "openai";
     
     // You will need to set these environment variables or edit the following values
     const audioFilePath = "<audio file path>";
-    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+    const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
+    const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
     
     // Required Azure OpenAI deployment name and API version
-    const apiVersion = "2024-08-01-preview";
-    const deploymentName = "whisper";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2024-08-01-preview";
+    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "whisper";
     
     function getClient(): AzureOpenAI {
       return new AzureOpenAI({
@@ -155,16 +191,31 @@ Your app's _package.json_ file will be updated with the dependencies.
     });
     ```
 
-1. Build the application with the following command:
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
 
-    ```console
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
     tsc
     ```
+    
+1. Run the code with the following command:
 
-1. Run the application with the following command:
-
-    ```console
-    node Whisper.js
+    ```shell
+    node index.js
     ```
 
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisper TypeScript ドキュメントの内容更新と構成の変更"
}
```

### Explanation
この変更は、`whisper-typescript.md`ファイルに対して行われた大規模な更新であり、追加されたコンテンツが87行、削除されたコンテンツが36行、合計で123行の変更が含まれています。主な更新内容は、TypeScriptでのアプリケーションのセットアップ手順の明確化です。

具体的には、以下の変更が行われました：
1. レビュアーの情報が`v-baolianzou`から`eur`に更新されました。
2. 新しいセクションが追加され、アプリケーションのセットアップに関する具体的なコマンドや手順が詳述されています。特に、フォルダーの作成や`package.json`の設定方法、TypeScriptコードのコンパイル命令などが明記されました。
3. 追加されたコードブロックには、コマンドの実行例や環境変数の設定が含まれており、ユーザーが実際に手を動かして作業できるようになっています。
4. より良い可読性と整理のために、セクションが再構成され、新たに`tsconfig.json`の作成手順が含まれています。

この更新は、文書が最新の開発環境に合わせて適切に維持され、よりユーザーフレンドリーになるように設計されています。

## articles/ai-services/openai/text-to-speech-quickstart.md{#item-c344ad}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: quickstart
 ms.date: 9/12/2024
-ms.reviewer: v-baolianzou
+ms.reviewer: eur
 ms.author: eur
 author: eric-urban
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Text-to-Speech クイックスタートドキュメントのレビュアー情報の更新"
}
```

### Explanation
この変更は、`text-to-speech-quickstart.md`ファイルに対するもので、レビュアーの情報が更新されています。具体的には、レビュアーが`v-baolianzou`から新しいレビュアーである`eur`に変更されました。この変更は、ドキュメントの責任者を最新の状態に保つためのものであり、文書の質を高めることを目的としています。この更新は軽微なものですが、レビュープロセスの重要性を反映しており、最新のレビュー担当者が文書の内容を確認し、改善の機会を提供することが期待されます。

## articles/ai-services/openai/whisper-quickstart.md{#item-4cae3d}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-openai
 ms.custom: devx-track-python
 ms.topic: quickstart
 ms.date: 8/09/2024
-ms.reviewer: v-baolianzou
+ms.reviewer: eur
 ms.author: eur
 author: eric-urban
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisper クイックスタートドキュメントのレビュアー情報の更新"
}
```

### Explanation
この変更は、`whisper-quickstart.md`ファイルに対するもので、レビュアーの情報が更新されています。具体的には、レビュアーが`v-baolianzou`から新しいレビュアーである`eur`に変更されました。この更新は、ドキュメントの最新のレビューチームのメンバーを反映するためのものであり、文書の品質改善に寄与することが期待されています。レビュアーの変更は、文書の内容が信頼性のあるものであることを保証し、関連する情報が正確であることを確認する上でも重要です。変更は軽微ですが、文書の更新におけるレビュープロセスの重要性を示しています。


