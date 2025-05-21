---
date: '2025-05-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9b2c87c...MicrosoftDocs:f021165
summary: このコード変更では、Azure OpenAI関連の文書に新機能が追加され、いくつかの重要なドキュメントが大規模に削除されました。特に、プログラミング言語に関するアシスタントのクイックスタートガイドやドキュメントが削除されたため、ユーザーにとって貴重な情報が失われました。ただし、エージェントサービスに関する新しい情報が追加され、情報の再構築と整理が進められています。この変更により、ユーザーや開発者に与える影響が懸念されており、今後の情報提供方法に注目が集まっています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9b2c87c...MicrosoftDocs:f021165){target="_blank"}

<format>
# ハイライト
このコード変更では、Azure OpenAI関連の文書に関し、いくつかの新機能の追加と大規模なドキュメント削除が行われました。特に、様々なプログラミング言語を使用したアシスタントのクイックスタートガイドが削除され、ユーザーに提供できる情報が失われています。

## 新機能
- エージェントサービスに関する新しい情報の追加

## 破壊的変更
- Azure OpenAIアシスタントのクイックスタートガイドの削除
- 様々なプログラミング言語（C#、JavaScript、Python、TypeScript、REST API）に関するアシスタントの使い方ドキュメントの削除
- 助手スタジオに関するドキュメントの削除

## その他の更新
- 各種文書の日付の更新と情報整理
- スピルオーバー管理やデプロイメントに関する情報の軽微な修正

# インサイト
今回の変更の背後には、Azure OpenAIサービスが提供する情報の再構築、整理、及び最新化を目的にした戦略的意図が伺えます。特に、大規模なドキュメント削除が目立ちますが、これにはユーザーへの新しい情報提供方法や、より効果的な情報伝達手段の導入を模索している兆候と考えられます。

エージェントサービスに関する新しい情報の追加は、特定のAzureサービスを強調する方向性を示しており、また、破壊的変更として挙げられているクイックスタートガイドの削除は、情報が過時的だったり、新たな提供方法に移行するための準備段階にある可能性があります。

削除されたドキュメントには開発者向けに重要な情報が多く含まれていたため、これまで依存していたユーザーや開発者にとっては利用への影響が懸念されます。今後、新しい情報がどのような形で提供され、どういったサポートがなされるのかに注目が集まります。それまでの間、開発者は代替のリソースを探すか、直接Azureの公式サポートに依存する必要があります。

迅速な対応が求められる中で、Azureプラットフォームがどのようにユーザー体験を変化・向上させていくのかが、今後の技術者コミュニティの焦点ポイントとなるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [assistants-quickstart.md](#item-eaf614) | minor update | Azure OpenAIアシスタントのクイックスタートガイドの削除 | removed | 0 | 55 | 55 | 
| [assistants.md](#item-eab970) | minor update | Azure OpenAIアシスタントAPIの概念に関する拡張 | modified | 20 | 4 | 24 | 
| [models.md](#item-db2c37) | minor update | Azure OpenAIモデルに関する情報の更新 | modified | 0 | 13 | 13 | 
| [assistant-functions.md](#item-a47205) | minor update | Azure OpenAIアシスタントの関数呼び出しに関する情報の更新 | modified | 3 | 1 | 4 | 
| [assistants-logic-apps.md](#item-57ae37) | minor update | Azure OpenAIアシスタントによるAzure Logic Appsの使用に関する情報の更新 | modified | 3 | 1 | 4 | 
| [azure-developer-cli.md](#item-3d4cfb) | minor update | Azure Developer CLIを使用したリソースデプロイに関する情報の更新 | modified | 2 | 2 | 4 | 
| [code-interpreter.md](#item-95efbd) | minor update | Azure OpenAIアシスタントのコードインタープリターに関する情報の更新 | modified | 3 | 1 | 4 | 
| [deployment-types.md](#item-210814) | minor update | デプロイメントタイプに関する注意事項の追加 | modified | 3 | 0 | 3 | 
| [file-search.md](#item-f9d6d7) | minor update | ファイル検索ツールに関する情報の更新 | modified | 3 | 1 | 4 | 
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | Provisioned Throughputに関する情報の更新 | modified | 1 | 5 | 6 | 
| [spillover-traffic-management.md](#item-3c21ff) | minor update | スピルオーバー交通管理に関する情報の更新 | modified | 3 | 3 | 6 | 
| [use-web-app.md](#item-802413) | minor update | Webアプリの使用に関する情報の更新 | modified | 1 | 1 | 2 | 
| [agent-service.md](#item-186020) | new feature | エージェントサービスに関する新しい情報の追加 | added | 12 | 0 | 12 | 
| [assistants-ai-studio.md](#item-1632e2) | breaking change | エージェントスタジオに関するドキュメントの削除 | removed | 0 | 134 | 134 | 
| [assistants-csharp.md](#item-cc4697) | breaking change | C#によるアシスタントの使い方に関するドキュメントの削除 | removed | 0 | 269 | 269 | 
| [assistants-javascript.md](#item-ad3627) | breaking change | JavaScriptによるアシスタントの使い方に関するドキュメントの削除 | removed | 0 | 313 | 313 | 
| [assistants-python.md](#item-82d745) | breaking change | Pythonによるアシスタントの使い方に関するドキュメントの削除 | removed | 0 | 263 | 263 | 
| [assistants-rest.md](#item-261c46) | breaking change | REST APIを使用したAIアシスタントの構築に関するドキュメントの削除 | removed | 0 | 146 | 146 | 
| [assistants-typescript.md](#item-3195a9) | breaking change | TypeScriptを用いたAzure OpenAIのアシスタント作成に関するドキュメントの削除 | removed | 0 | 373 | 373 | 
| [toc.yml](#item-c945af) | minor update | TOCからのアシスタント(プレビュー)の削除 | modified | 0 | 2 | 2 | 


# Modified Contents
## articles/ai-services/openai/assistants-quickstart.md{#item-eaf614}

<details>
<summary>Diff</summary>
````diff
@@ -1,55 +0,0 @@
----
-title: Quickstart - Getting started with Azure OpenAI Assistants (Preview)
-titleSuffix: Azure OpenAI
-description: Walkthrough on how to get started with Azure OpenAI assistants with new features like code interpreter and retrieval.
-manager: nitinme
-ms.service: azure-ai-openai
-ms.custom: devx-track-python, devx-track-dotnet, devx-track-extended-java, devx-track-js
-ms.topic: quickstart
-author: aahill
-ms.author: aahi
-ms.date: 3/10/2025
-zone_pivot_groups: openai-quickstart-assistants
-recommendations: false
----
-
-
-# Quickstart: Get started using Azure OpenAI Assistants (Preview)
-
-Azure OpenAI Assistants (Preview) allows you to create AI assistants tailored to your needs through custom instructions and augmented by advanced tools like code interpreter, file search, and custom functions.
-
-::: zone pivot="ai-foundry-portal"
-
-[!INCLUDE [Azure AI Foundry portal](includes/assistants-ai-studio.md)]
-
-::: zone-end
-
-::: zone pivot="programming-language-python"
-
-[!INCLUDE [Python SDK quickstart](includes/assistants-python.md)]
-
-::: zone-end
-
-::: zone pivot="programming-language-csharp"
-
-[!INCLUDE [C# quickstart](includes/assistants-csharp.md)]
-
-::: zone-end
-
-::: zone pivot="programming-language-javascript"
-
-[!INCLUDE [JavaScript quickstart](includes/assistants-javascript.md)]
-
-::: zone-end
-
-::: zone pivot="programming-language-typescript"
-
-[!INCLUDE [TypeScript quickstart](includes/assistants-typescript.md)]
-
-::: zone-end
-
-::: zone pivot="rest-api"
-
-[!INCLUDE [REST API quickstart](includes/assistants-rest.md)]
-
-::: zone-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIアシスタントのクイックスタートガイドの削除"
}
```

### Explanation
この変更は、Azure OpenAIアシスタントに関するクイックスタートガイドがファイルから完全に削除されたことを示しています。この変更により、関連する記事の内容が55行削除され、メンテナンスや情報の更新を目的とした軽微な更新と考えられます。このガイドは、Azure OpenAIアシスタントの使用方法やカスタム指示の設定方法に関する情報を提供していました。削除された内容には、各プログラミング言語（Python、C#、JavaScript、TypeScript、およびREST API）のクイックスタートリンクや、Azure AI Foundryポータルに関する情報が含まれていました。この更新は、ユーザーが最新の情報へアクセスできるように情報を整理するためのものと推測されます。

## articles/ai-services/openai/concepts/assistants.md{#item-eab970}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Azure OpenAI in Azure AI Foundry Models Assistants API concepts
 titleSuffix: Azure OpenAI
 description: Learn about the concepts behind the Azure OpenAI Assistants API.
 ms.topic: conceptual
-ms.date: 02/04/2025
+ms.date: 05/20/2025
 ms.service: azure-ai-openai
 manager: nitinme
 author: aahill
@@ -13,19 +13,21 @@ recommendations: false
 
 # Azure OpenAI Assistants API (Preview)
 
+[!INCLUDE [agent-service](../includes/agent-service.md)]
+
 Assistants, a feature of Azure OpenAI in Azure AI Foundry Models, is available in public preview starting in the `2024-02-15-preview` API version. Assistants API makes it easier for developers to create applications with sophisticated copilot-like experiences that can sift through data, suggest solutions, and automate tasks.
 
 * Assistants can call Azure OpenAI’s [models](../concepts/models.md) with specific instructions to tune their personality and capabilities.
 * Assistants can access **multiple tools in parallel**. These can be both Azure OpenAI-hosted tools like [code interpreter](../how-to/code-interpreter.md) and [file search](../how-to/file-search.md), or tools you build, host, and access through [function calling](../how-to/function-calling.md).
-* Assistants can access **persistent Threads**. Threads simplify AI application development by storing message history and truncating it when the conversation gets too long for the model's context length. You create a Thread once, and simply append Messages to it as your users reply.
+* Assistants can access **persistent Threads**. Threads simplify AI application development by storing message history and truncating it when the conversation gets too long for the model's context length. You create a Thread once, and append Messages to it as your users reply.
 * Assistants can access files in several formats. Either as part of their creation or as part of Threads between Assistants and users. When using tools, Assistants can also create files (such as images or spreadsheets) and cite files they reference in the Messages they create.
 
 ## Overview
 
 Previously, building custom AI assistants needed heavy lifting even for experienced developers. While the chat completions API is lightweight and powerful, it's inherently stateless, which means that developers had to manage conversation state and chat threads, tool integrations, retrieval documents and indexes, and execute code manually.
 
 The Assistants API, as the stateful evolution of the chat completion API, provides a solution for these challenges.
-Assistants API supports persistent automatically managed threads. This means that as a developer you no longer need to develop conversation state management systems and work around a model’s context window constraints. The Assistants API will automatically handle the optimizations to keep the thread below the max context window of your chosen model. Once you create a Thread, you can simply append new messages to it as users respond. Assistants can also access multiple tools in parallel, if needed. These tools include:
+Assistants API supports persistent automatically managed threads. This means that as a developer you no longer need to develop conversation state management systems and work around a model’s context window constraints. The Assistants API will automatically handle the optimizations to keep the thread below the max context window of your chosen model. Once you create a Thread, you can append new messages to it as users respond. Assistants can also access multiple tools in parallel, if needed. These tools include:
 
 - [Code Interpreter](../how-to/code-interpreter.md)
 - [Function calling](../how-to/assistant-functions.md)
@@ -38,12 +40,26 @@ Assistants API is built on the same capabilities that power OpenAI’s GPT produ
 > [!IMPORTANT]
 > Retrieving untrusted data using Function calling, Code Interpreter or File Search with file input, and Assistant Threads functionalities could compromise the security of your Assistant, or the application that uses the Assistant. Learn about mitigation approaches [here](https://aka.ms/oai/assistant-rai).
 
+### Using assistants
+
+For information on using assistants, see the following reference documentation. 
+* [C#](/dotnet/api/overview/azure/ai.openai.assistants-readme?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext)
+* [Java](/java/api/overview/azure/ai-openai-assistants-readme?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext)
+* [JavaScript](../how-to/migration-javascript.md?tabs=javascript-new#assistants)
+* [Python](https://platform.openai.com/docs/api-reference/assistants)
+* [REST API](../reference-preview.md#list---assistants)
+
 ## Available models
 
-To see a list of Azure OpenAI models that you can use with assitants, see the [Models](./models.md#assistants-preview) article.
+To see a list of Azure OpenAI models that you can use with assistants, see the [Models](./models.md#assistants-preview) article.
 
 ## Assistants playground
 
+Before using assistants, you need:
+
+- A [compatible model](../concepts/models.md#assistants-preview) deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
+- An [Azure AI project](../../../ai-foundry/how-to/create-projects.md) in Azure AI Foundry portal.
+
 We provide a walkthrough of the Assistants playground in our [quickstart guide](../assistants-quickstart.md). This provides a no-code environment to test out the capabilities of assistants.
 
 ## Assistants components
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIアシスタントAPIの概念に関する拡張"
}
```

### Explanation
この変更は、Azure OpenAIアシスタントAPIに関する概念を説明する文書の修正を示しています。ファイルに20行が追加され、4行が削除され、合計で24行の変更が行われました。主な変更点には、日付の更新や新しい情報の追加が含まれています。

具体的には、アシスタントAPIの機能強化についての詳細が追加され、開発者が自分のアプリケーションに洗練されたコパイロットのような体験を提供できることが強調されています。また、アシスタントが複数のツールに同時にアクセスし、会話のスレッドを管理できる機能に関する説明が明確化されました。

さらに、アシスタントの使用方法に関する参照用ドキュメントへのリンクも追加され、C#、Java、JavaScript、Pythonの各言語用のリソースが提供されています。最終的に、アシスタントを使用するための前提条件が明記され、ユーザーが実装において考慮すべき点が整理されています。この更新は、ユーザーにとって有益な情報を提供し、アシスタントAPIの利用を促進することを目的としています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -160,8 +160,6 @@ When your resource is created, you can [deploy](../how-to/create-resource.md#dep
 
 GPT-4 Turbo is a large multimodal model (accepting text or image inputs and generating text) that can solve difficult problems with greater accuracy than any of OpenAI's previous models. Like GPT-3.5 Turbo, and older GPT-4 models GPT-4 Turbo is optimized for chat and works well for traditional completions tasks.
 
-[!INCLUDE [GPT-4 Turbo](../includes/gpt-4-turbo.md)]
-
 ## GPT-4
 
 GPT-4 is the predecessor to GPT-4 Turbo. Both the GPT-4 and GPT-4 Turbo models have a base model name of `gpt-4`. You can distinguish between the GPT-4 and Turbo models by examining the model version.
@@ -185,9 +183,6 @@ See [model versions](../concepts/model-versions.md) to learn about how Azure Ope
 |`gpt-4o-mini` (2024-07-18) <br> **GPT-4o mini** | **Latest small GA model** <br> - Fast, inexpensive, capable model ideal for replacing GPT-3.5 Turbo series models. <br> - Text, image processing <br>- JSON Mode <br> - parallel function calling | Input: 128,000 <br> Output: 16,384  | Oct 2023 |
 |`gpt-4o` (2024-05-13) <br> **GPT-4o (Omni)** | Text, image processing <br> - JSON Mode <br> - parallel function calling <br> - Enhanced accuracy and responsiveness <br> - Parity with English text and coding tasks compared to GPT-4 Turbo with Vision <br> - Superior performance in non-English languages and in vision tasks |Input: 128,000  <br> Output: 4,096| Oct 2023 |
 | `gpt-4` (turbo-2024-04-09) <br>**GPT-4 Turbo with Vision** | **New GA model** <br> - Replacement for all previous GPT-4 preview models (`vision-preview`, `1106-Preview`, `0125-Preview`). <br> - [**Feature availability**](#gpt-4o-and-gpt-4-turbo) is currently different depending on method of input, and deployment type. | Input: 128,000  <br> Output: 4,096  | Dec 2023 |
-| `gpt-4` (0125-Preview)*<br>**GPT-4 Turbo Preview** | **Preview Model** <br> -Replaces 1106-Preview <br>- Better code generation performance <br> - Reduces cases where the model doesn't complete a task <br> - JSON Mode <br> - parallel function calling <br> - reproducible output (preview) | Input: 128,000  <br> Output: 4,096           | Dec 2023         |
-| `gpt-4` (vision-preview)<br>**GPT-4 Turbo with Vision Preview**  | **Preview model** <br> - Accepts text and image input. <br> - Supports enhancements <br> - JSON Mode <br> - parallel function calling <br> - reproducible output (preview) | Input: 128,000  <br> Output: 4,096              | Apr 2023       |
-| `gpt-4` (1106-Preview)<br>**GPT-4 Turbo Preview** | **Preview Model** <br> - JSON Mode <br> - parallel function calling <br> - reproducible output (preview) | Input: 128,000  <br> Output: 4,096 | Apr 2023         |
 | `gpt-4-32k` (0613) | **Older GA model** <br> - Basic function calling with tools  | 32,768               | Sep 2021         |
 | `gpt-4` (0613)     | **Older GA model** <br> - Basic function calling with tools | 8,192                | Sep 2021         |
 | `gpt-4-32k`(0314)  | **Older GA model** <br> - [Retirement information](./model-retirements.md#current-models) | 32,768               | Sep 2021         |
@@ -196,11 +191,6 @@ See [model versions](../concepts/model-versions.md) to learn about how Azure Ope
 > [!CAUTION]
 > We don't recommend using preview models in production. We will upgrade all deployments of preview models to either future preview versions or to the latest stable GA version. Models that are designated preview don't follow the standard Azure OpenAI model lifecycle.
 
-- GPT-4 version 0125-preview is an updated version of the GPT-4 Turbo preview previously released as version 1106-preview.  
-- GPT-4 version 0125-preview completes tasks such as code generation more completely compared to gpt-4-1106-preview. Because of this, depending on the task, customers may find that GPT-4-0125-preview generates more output compared to the gpt-4-1106-preview.  We recommend customers compare the outputs of the new model.  GPT-4-0125-preview also addresses bugs in gpt-4-1106-preview with UTF-8 handling for non-English languages. 
-- GPT-4 version `turbo-2024-04-09` is the latest GA release and replaces `0125-Preview`, `1106-preview`, and `vision-preview`.
-
-
 ## GPT-3.5
 
 GPT-3.5 models can understand and generate natural language or code. The most capable and cost effective model in the GPT-3.5 family is GPT-3.5 Turbo, which has been optimized for chat and works well for traditional completions tasks as well. GPT-3.5 Turbo is available for use with the Chat Completions API. GPT-3.5 Turbo Instruct has similar capabilities to `text-davinci-003` using the Completions API instead of the Chat Completions API.  We recommend using GPT-3.5 Turbo and GPT-3.5 Turbo Instruct over [legacy GPT-3.5 and GPT-3 models](./legacy-models.md).
@@ -211,9 +201,6 @@ GPT-3.5 models can understand and generate natural language or code. The most ca
 | `gpt-35-turbo` (0125) **NEW** | **Latest GA Model** <br> - JSON Mode <br> - parallel function calling <br> - reproducible output (preview) <br> - Higher accuracy at responding in requested formats. <br> - Fix for a bug which caused a text encoding issue for non-English language function calls.  | Input: 16,385<br> Output: 4,096  | Sep 2021 |
 | `gpt-35-turbo` (1106) | **Older GA Model** <br> - JSON Mode <br> - parallel function calling <br> - reproducible output (preview) | Input: 16,385<br> Output: 4,096 |  Sep 2021|
 | `gpt-35-turbo-instruct` (0914) | **Completions endpoint only** <br> - Replacement for [legacy completions models](./legacy-models.md) | 4,097 |Sep 2021 |
-| `gpt-35-turbo-16k` (0613) | **Older GA Model** <br> - Basic function calling with tools | 16,384 | Sep 2021 |
-| `gpt-35-turbo` (0613) | **Older GA Model** <br> - Basic function calling with tools   | 4,096 | Sep 2021 |
-| `gpt-35-turbo`**<sup>1</sup>** (0301) |  **Older GA Model**  <br> - [Retirement information](./model-retirements.md#current-models) | 4,096 | Sep 2021 |
 
 To learn more about how to interact with GPT-3.5 Turbo and the Chat Completions API check out our [in-depth how-to](../how-to/chatgpt.md).
 
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
この変更は、Azure OpenAIのモデルに関する文書が更新されたことを示しており、合計で13行が削除されました。主な変更内容は、GPT-4およびGPT-3.5に関する情報の整理と明確化です。

具体的には、GPT-4 Turboとその前のモデルに関する断片的な情報と比較が行われ、いくつかのプレビュー版モデルの説明が削除されました。削除された部分には、モデルのバージョンや性能についての具体的な説明が含まれており、これによって情報が簡潔になったと考えられます。

また、GPT-3.5モデルについても同様に、旧バージョンの情報が整理され、最新の情報が強調される形で文書が改善されています。全体として、この更新は文書の可読性や情報の正確性を向上させ、ユーザーにとっての理解を助ける目的を持っていると言えます。

## articles/ai-services/openai/how-to/assistant-functions.md{#item-a47205}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 03/31/2025
+ms.date: 05/20/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -15,6 +15,8 @@ recommendations: false
 
 # Azure OpenAI Assistants function calling
 
+[!INCLUDE [agent-service](../includes/agent-service.md)]
+
 The Assistants API supports function calling, which allows you to describe the structure of functions to an Assistant and then return the functions that need to be called along with their arguments.
 
 ## Function calling support
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIアシスタントの関数呼び出しに関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIアシスタントの関数呼び出しに関する文書の更新を示しており、合計で4行の変更が行われました。具体的には、3行が追加され、1行が削除されています。

主な変更点は、文書の日付が「2025年3月31日」から「2025年5月20日」に更新されたことです。また、新しく追加された行には、アシスタントが利用するエージェントサービスに関するインクルード文が加わり、関数呼び出しの機能をより明確に説明する要素が強化されています。

これにより、開発者はアシスタントAPIを使って機能を呼び出す際の構造をよりよく理解できるようになり、関数の引数と呼び出しに関する情報も提供されています。この更新は、ユーザーの理解を助け、より効果的な利用を促進することを目的としています。

## articles/ai-services/openai/how-to/assistants-logic-apps.md{#item-57ae37}

<details>
<summary>Diff</summary>
````diff
@@ -6,14 +6,16 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 04/29/2025
+ms.date: 05/20/2025
 author: aahill
 ms.author: aahi
 recommendations: false
 ---
 
 # Call Azure Logic apps as functions using Azure OpenAI Assistants 
 
+[!INCLUDE [agent-service](../includes/agent-service.md)]
+
 [Azure Logic Apps](https://azure.microsoft.com/products/logic-apps) is an integration platform in Azure that allows you to build applications and automation workflows with low code tools enabling developer productivity and faster time to market. By using the visual designer and selecting from hundreds of prebuilt connectors, you can quickly build a workflow that integrates and manages your apps, data, services, and systems.
 
 Azure Logic Apps is fully managed by Microsoft Azure, which frees you from worrying about hosting, scaling, managing, monitoring, and maintaining solutions built with these services. When you use these capabilities to create [serverless](/azure/logic-apps/logic-apps-overview) apps and solutions, you can just focus on the business logic and functionality. These services automatically scale to meet your needs, make automation workflows faster, and help you build robust cloud apps using little to no code.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIアシスタントによるAzure Logic Appsの使用に関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIアシスタントを使用してAzure Logic Appsを関数として呼び出す方法に関する文書の更新を示しており、合計で4行の変更が行われました。具体的には、3行が追加され、1行が削除されています。

主要な変更点は、文書の日付が「2025年4月29日」から「2025年5月20日」に更新されたことです。また、新たに加えられた行には、アシスタントが利用するエージェントサービスに関するインクルード文が追加されており、これにより文書の内容が一層充実しています。

さらに、Azure Logic Appsの説明が詳細に記述され、ローカルツールによるアプリケーションの構築や自動化ワークフローの迅速な開発が強調されています。これにより、開発者は低コードでの開発が可能なポイントや、Microsoft Azureが提供するマネージドサービスの利点を理解しやすくなります。この更新は、ユーザーにとってより明確で有用な情報を提供することを目的としています。

## articles/ai-services/openai/how-to/azure-developer-cli.md{#item-3d4cfb}

<details>
<summary>Diff</summary>
````diff
@@ -7,13 +7,13 @@ ms.service: azure-ai-openai
 ms.topic: quickstart
 author: aahill
 ms.author: aahi
-ms.date: 02/25/2025
+ms.date: 05/20/2025
 recommendations: false
 ---
 
 # Use the Azure Developer CLI to deploy resources for Azure OpenAI On Your Data 
 
-Use this article to learn how to automate resource deployment for Azure OpenAI in Azure AI Foundry Models On Your Data. The Azure Developer CLI (`azd`) is an open-source command-line tool that streamlines provisioning and deploying resources to Azure by using a template system. The template contains infrastructure files to provision the necessary Azure OpenAI resources and configurations. The source code for the template can be found on [GitHub](https://github.com/Azure-Samples/openai-chat-your-own-data/tree/main).
+Use this article to learn how to automate resource deployment for Azure OpenAI On Your Data. The Azure Developer CLI (`azd`) is an open-source command-line tool that streamlines provisioning and deploying resources to Azure by using a template system. The template contains infrastructure files to provision the necessary Azure OpenAI resources and configurations. The source code for the template can be found on [GitHub](https://github.com/Azure-Samples/openai-chat-your-own-data/tree/main).
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Developer CLIを使用したリソースデプロイに関する情報の更新"
}
```

### Explanation
この変更は、Azure Developer CLIを使用してAzure OpenAIのためのリソースをデプロイする方法に関する文書の更新を示しており、合計で4行の変更が行われました。具体的には、2行が追加され、2行が削除されています。

主な変更の一つは、文書の日付が「2025年2月25日」から「2025年5月20日」に更新されたことです。この更新により、情報が最新のものとなることが意図されています。

また、記事の内容については、実際には文言の変更はなく、全体として文書が一層整然とした印象を持つようになっています。Azure Developer CLI (`azd`)が、Azureへのリソースのプロビジョニングやデプロイを効率化するためのオープンソースのコマンドラインツールであることが強調されています。この変更は、開発者がリソースを簡単かつ迅速にデプロイできる方法を強化することを目的としています。

## articles/ai-services/openai/how-to/code-interpreter.md{#item-95efbd}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 02/03/2025
+ms.date: 05/20/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -15,6 +15,8 @@ recommendations: false
 
 # Azure OpenAI Assistants Code Interpreter (Preview)
 
+[!INCLUDE [agent-service](../includes/agent-service.md)]
+
 Code Interpreter allows the Assistants API to write and run Python code in a sandboxed execution environment. With Code Interpreter enabled, your Assistant can run code iteratively to solve more challenging code, math, and data analysis problems. When your Assistant writes code that fails to run, it can iterate on this code by modifying and running different code until the code execution succeeds.
 
 > [!IMPORTANT]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIアシスタントのコードインタープリターに関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIアシスタント用のコードインタープリターに関する文書の更新を示しており、合計で4行の変更が行われました。具体的には、3行が追加され、1行が削除されています。

変更の一つは、文書の日付が「2025年2月3日」から「2025年5月20日」に更新されたことです。これにより、文書が最新情報を反映するようになっています。

新たに加えられた行には、アシスタントが利用するエージェントサービスを示すインクルード文が含まれています。この追加により、ユーザーが関連情報を容易に参照できるように配慮されています。

また、コードインタープリターの機能についての説明が明確化されており、アシスタントAPIがPythonコードを書いてサンドボックス環境内で実行できることが強調されています。この機能により、アシスタントはより複雑なコードの問題や数学、データ分析の問題を解決するために、反復的にコードを修正して実行することができるようになります。これらの変更は、ユーザーにとってよりわかりやすく、有用な情報を提供することを目指しています。

## articles/ai-services/openai/how-to/deployment-types.md{#item-210814}

<details>
<summary>Diff</summary>
````diff
@@ -34,6 +34,9 @@ If the Azure OpenAI resource used in your Data Zone deployment is located in the
 
 For any [deployment type](/azure/ai-services/openai/how-to/deployment-types) labeled 'Global,' prompts and responses may be processed in any geography where the relevant Azure OpenAI model is deployed (learn more about [region availability of models](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For any deployment type labeled as 'DataZone,' prompts and responses may be processed in any geography within the specified data zone, as defined by Microsoft. If you create a DataZone deployment in an Azure OpenAI resource located in the United States, prompts and responses may be processed anywhere within the United States. If you create a DataZone deployment in an Azure OpenAI resource located in a European Union Member Nation, prompts and responses may be processed in that or any other European Union Member Nation. For both Global and DataZone deployment types, any data stored at rest, such as uploaded data, is stored in the customer-designated geography. Only the location of processing is affected when a customer uses a Global deployment type or DataZone deployment type in Azure OpenAI in Azure AI Foundry Models; Azure data processing and compliance commitments remain applicable.
 
+> [!NOTE]
+> With Global standard and Data zone standard deployment types if the primary region experiences an interruption in service all traffic that is initially routed to this region will be impacted. To learn more, consult the [business continuity and disaster recovery guide](../how-to/business-continuity-disaster-recovery.md).
+
 ## Global standard
 
 > [!IMPORTANT]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントタイプに関する注意事項の追加"
}
```

### Explanation
この変更は、Azure OpenAIのデプロイメントタイプに関する文書の更新を示しており、合計で3行の変更が加えられました。具体的には、3行が新たに追加されました。

追加された内容には、グローバル標準およびデータゾーン標準デプロイメントタイプに関する重要な注意事項が含まれています。この注意事項では、主な地域でサービスが中断された場合、その地域に最初にルーティングされていたすべてのトラフィックが影響を受ける可能性があることが説明されています。さらに、ビジネス継続性と災害復旧についてのガイドを参照するように促されています。

この変更は、ユーザーがデプロイメントの選択に関連するリスクを理解し、適切な情報を得るための助けとなることを目的としています。また、デプロイメント環境でのデータ処理およびコンプライアンスへの影響を考慮するための重要なポイントが強調されています。全体として、文書の透明性と信頼性を向上させる役割を果たしています。

## articles/ai-services/openai/how-to/file-search.md{#item-f9d6d7}

<details>
<summary>Diff</summary>
````diff
@@ -6,14 +6,16 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 03/31/2025
+ms.date: 05/20/2025
 author: aahill
 ms.author: aahi
 recommendations: false
 ---
 
 # Azure OpenAI Assistants file search tool (Preview)
 
+[!INCLUDE [agent-service](../includes/agent-service.md)]
+
 File Search augments the Assistant with knowledge from outside its model, such as proprietary product information or documents provided by your users. OpenAI automatically parses and chunks your documents, creates and stores the embeddings, and use both vector and keyword search to retrieve relevant content to answer user queries.
 
 > [!IMPORTANT]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイル検索ツールに関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIアシスタントのファイル検索ツールに関する文書の更新を示しており、合計で4行の変更が行われました。具体的には、3行が追加され、1行が削除されています。

変更の一つとして、文書の日付が「2025年3月31日」から「2025年5月20日」に更新されており、これにより最新の情報が反映されています。

新たに加えられた行には、アシスタントが利用するエージェントサービスを示すインクルード文が含まれています。また、ファイル検索ツールの機能についての説明が強化されており、オープンAIが内部モデル以外の知識を用いてユーザーの質問に回答する様子が詳述されています。このツールは、ユーザーから提供された文書や独自の製品情報を解析し、ベクトル検索とキーワード検索を活用して関連するコンテンツを取得することができると述べられています。

これらの変更は、ユーザーに対してファイル検索ツールの利便性と機能をより明確に伝えることを目指しており、文書全体の透明性を高めています。

## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title:  Understanding costs associated with provisioned throughput units (PTU)
 description: Learn about provisioned throughput costs and billing in Azure OpenAI. 
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 03/31/2025
+ms.date: 05/20/2025
 manager: nitinme
 author: aahill 
 ms.author: aahi 
@@ -47,10 +47,6 @@ Quota for provisioned deployments shows up in Azure AI Foundry as the following
 
 :::image type="content" source="../media/provisioned/ptu-quota-page.png" alt-text="Screenshot of quota UI for Azure OpenAI provisioned." lightbox="../media/provisioned/ptu-quota-page.png":::
 
-
-> [!NOTE]
-> Global provisioned and data zone provisioned deployments are only supported for gpt-4o and gpt-4o-mini models at this time. For more information on model availability, review the [models documentation](../concepts/models.md).
-
 ## Hourly usage
 
 Provisioned, Data Zone Provisioned, and Global Provisioned deployments are charged an hourly rate ($/PTU/hr) on the number of PTUs that have been deployed.  For example, a 300 PTU deployment will be charged the hourly rate times 300.  All Azure OpenAI pricing is available in the Azure Pricing Calculator. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Provisioned Throughputに関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIにおける「Provisioned Throughput（プロビジョニングスループット）」に関する文書の更新を示しており、合計で6行が変更されました。具体的には、1行が追加され、5行が削除されています。

日付が「2025年3月31日」から「2025年5月20日」へと更新されたことにより、情報の最新性が確保されています。

削除された部分には、グローバルプロビジョンドおよびデータゾーンプロビジョンドデプロイメントが、現時点でgpt-4oおよびgpt-4o-miniモデルのみをサポートしているという重要な注意書きが含まれていました。これにより、特定のモデルに関する制限やサポート状況についての情報が消失しました。

追加された内容は特に明示されていないため、更新の焦点は主に日付の変更と、以前の制限事項の削除にあります。結果として、この変更がユーザーにどのような影響を及ぼすのかは明確ではないものの、文書の一貫性や正確性を保つための努力として評価されます。

## articles/ai-services/openai/how-to/spillover-traffic-management.md{#item-3c21ff}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: aahill # GitHub alias
 ms.author: aahi
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 03/05/2025
+ms.date: 05/20/2025
 ---
 
 # Manage traffic with spillover for provisioned deployments (Preview)
@@ -18,15 +18,15 @@ Spillover manages traffic fluctuations on provisioned deployments by routing ove
 
 - The provisioned and standard deployments must be in the same Azure OpenAI resource to be eligible for spillover.
 
-- The data processing level of your standard deployment must match your provisioned deployment (e.g. global provisioned deployment must be used with a global standard spillover deployment).
+- The data processing level of your standard deployment must match your provisioned deployment (for example, a global provisioned deployment must be used with a global standard spillover deployment).
 
 ## When to enable spillover on provisioned deployments
 To maximize the utilization of your provisioned deployment, it is recommended to enable spillover for all global and data zone provisioned deployments. With spillover, bursts or fluctuations in traffic can be automatically managed by the service. This capability reduces the risk of experiencing disruptions when a provisioned deployment is fully utilized. Alternatively, spillover is configurable per-request to provide flexibility across different scenarios and workloads.  
 
 ## When does spillover come into effect?
 When spillover is enabled for a deployment or configured for a given inference request, spillover is initiated when a non-200 response code is received for a given inference request. When a request results in a non-200 response code, the Azure OpenAI automatically sends the request from your provisioned deployment to your standard deployment to be processed. Even if a subset of requests is routed to the standard deployment, the service prioritizes sending requests to the provisioned deployment before sending any overage requests to the standard deployment.
 
-## How does spillover impact cost?
+## How does spillover affect cost?
 Since spillover uses a combination of provisioned and standard deployments to manage traffic fluctuations, billing for spillover involves two components:
 
 - For any requests processed by your provisioned deployment, only the hourly provisioned deployment cost applies. No additional costs are incurred for these requests.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スピルオーバー交通管理に関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIの「スピルオーバー交通管理」に関する文書の更新を示しています。合計で6行が変更され、3行が追加され、同じく3行が削除されました。

主な変更点の一つは、文書の日付が「2025年3月5日」から「2025年5月20日」に変更されたことです。これにより、最新の情報が反映されています。

また、文章の中での表現も若干修正されています。例えば、スピルオーバーの条件に関する説明がより明確にされ、「例えば」との語が加えられています。さらに、コストに関するセクションのタイトルが「スピルオーバーがコストに与える影響？」に変更されており、表現がより自然になっています。

これらの修正により、ユーザーがスピルオーバー機能の条件やコストに関する情報をよりわかりやすく理解できるように工夫されています。また、全体を通して文書の一貫性や明瞭性が向上しています。

## articles/ai-services/openai/how-to/use-web-app.md{#item-802413}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-openai
 ms.topic: how-to
 author: aahill
 ms.author: aahi
-ms.date: 02/19/2025
+ms.date: 05/20/2025
 recommendations: false
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Webアプリの使用に関する情報の更新"
}
```

### Explanation
この変更は、「Webアプリの使用」に関するAzure OpenAIの文書が更新されたことを示しています。合計で2行が変更され、1行が追加され、1行が削除されています。

主な変更点は文書の日付が「2025年2月19日」から「2025年5月20日」へと更新されたことです。この更新により、情報が最新のものとなっています。

他の内容については特に詳しい変更が見られないため、今回の更新の主な目的は文書の新しさを保つことにあると言えます。ユーザーは、これによって最新の情報にアクセスできる利点があります。全体として、この更新は文書の整合性と正確性を向上させるためのものです。

## articles/ai-services/openai/includes/agent-service.md{#item-186020}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,12 @@
+---
+manager: nitinme
+ms.service: azure-ai-services
+ms.custom:
+ms.topic: include
+ms.date: 05/20/2025
+ms.author: aahi
+author: aahill
+---
+
+> [!NOTE]
+> The [Azure AI Foundry Agent Service](../../agents/overview.md) is now Generally Available, which provides more tools and better enterprise features. We recommend using the new service for the latest feature updates and improvements.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "エージェントサービスに関する新しい情報の追加"
}
```

### Explanation
この変更は、「エージェントサービス」に関する新しい情報が文書に追加されたことを示しています。新たに追加された内容は合計12行で、既存のコンテンツは削除されていません。

追加された部分には、エージェントサービスに関するメタデータ（著者、サービス、トピック、日付など）が含まれています。また、エージェントサービスが「一般提供」になったことを通知する注記も追加されており、これにより最新の機能や改善を利用するために新しいサービスを使用することが推奨されています。

この新しい情報は、Azure AI Foundryエージェントサービスに関する最新の機能や利用方法をユーザーに提供することが目的です。全体として、エージェントサービスに対する認識を高め、利用促進を図る内容となっています。

## articles/ai-services/openai/includes/assistants-ai-studio.md{#item-1632e2}

<details>
<summary>Diff</summary>
````diff
@@ -1,134 +0,0 @@
----
-title: Quickstart - getting started with Azure OpenAI assistants (preview) in Azure AI Foundry portal
-titleSuffix: Azure OpenAI
-description: Walkthrough on how to get started with Azure OpenAI assistants with new features like code interpreter in Azure AI Foundry portal.
-manager: nitinme
-ms.service: azure-ai-foundry
-ms.custom:
-  - build-2024
-  - ignite-2024
-ms.topic: include
-ms.date: 02/10/2025
-author: aahill
-ms.author: aahi
----
-
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
-
-## Prerequisites
-
-- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
-- A GTP-4 model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
-- An [Azure AI project](../../../ai-foundry/how-to/create-projects.md) in Azure AI Foundry portal.
-
-## Go to the Azure AI Foundry portal
-
-[Azure AI Foundry](https://ai.azure.com) lets you use Assistants v2 which provides several upgrades such as the [file search](../how-to/file-search.md) tool which is faster and supports more files.
-
-1. Sign in to [Azure AI Foundry](https://ai.azure.com).
-1. If your screen doesn't look like the following screenshot, select **Azure AI Foundry** in the top left of the screen.
-1. Select **Let's go** in the Azure OpenAI in Azure AI Foundry Models card. 
-
-    :::image type="content" source="../media/assistants/foundry-openai-selectior.png" alt-text="A screenshot of the main page of the Azure AI Foundry." lightbox="../media/assistants/foundry-openai-selectior.png":::
-    
-1. In the navigation menu on the left, select **Assistants**, located under **playgrounds**.
-
-    :::image type="content" source="../media/quickstarts/assistants-ai-studio-playground.png" alt-text="Screenshot of the Assistant configuration screen without all the values filled in." lightbox="../media/quickstarts/assistants-ai-studio-playground.png":::
-
-    The Assistants playground allows you to explore, prototype, and test AI Assistants without needing to run any code. From this page, you can quickly iterate and experiment with new ideas.
-    
-    The playground provides several options to configure your Assistant. In the following steps, you will use the **setup** pane to create a new AI assistant.
-    
-    | **Name** | **Description** |
-    |:---|:---|
-    | **Assistant name** | Your deployment name that is associated with a specific model. |
-    | **Instructions** | Instructions are similar to system messages this is where you give the model guidance about how it should behave and any context it should reference when generating a response. You can describe the assistant's personality, tell it what it should and shouldn't answer, and tell it how to format responses. You can also provide examples of the steps it should take when answering responses. |
-    | **Deployment** | This is where you set which model deployment to use with your assistant. |
-    | **Functions**| Create custom function definitions for the models to formulate API calls and structure data outputs based on your specifications. Not used in this quickstart. |
-    | **Code interpreter** | Code interpreter provides access to a sandboxed Python environment that can be used to allow the model to test and execute code. |
-    | **Files** | You can upload up to 10,000 files, with a max file size of 512 MB to use with tools. Not used in this quickstart. |
-    
-## Create your first Assistant
-
-1. Select your deployment from the **Deployments** dropdown.
-1. From the Assistant setup drop-down, select **New assistant**.
-1. Give your Assistant a name.
-1. Enter the following instructions "You are an AI assistant that can write code to help answer math questions"
-1. Select a model deployment. We recommend testing with one of the latest gpt-4 models.
-1. Select the toggle enabling code interpreter.
-1. Select Save.
-
-    :::image type="content" source="../media/quickstarts/assistant-configuration.png" alt-text="Screenshot of the assistant with configuration details entered." lightbox="../media/quickstarts/assistant-configuration.png":::
-
-7. Enter a question for the assistant to answer: "I need to solve the equation `3x + 11 = 14`. Can you help me?"
-8. Select the **Add and run button** :::image type="icon" source="../media/quickstarts/run.png":::
-
-    ```output
-    The solution to the equation (3x + 11 = 14) is (x = 1).
-    ```
-
-    While we can see that answer is correct, to confirm that the model used code interpreter to get to this answer, and that the code it wrote is valid rather than just repeating an answer from the model's training data we'll ask another question.
-
-9. Enter the follow-up question: "Show me the code you ran to get this solution."
-
-    ```output
-   Sure. The code is very straightforward
-    ```
-
-    ```python
-    # calculation
-    x = (14 - 11) / 3
-    x
-
-    ```
-
-    ```output
-    First, we subtract 11 from 14, then divide the result by 3. This gives us the value of x which is 1.0.
-    ````
-
-    :::image type="content" source="../media/quickstarts/assistant-ai-studio-session.png" alt-text="Screenshot of conversation session in the Assistant playground." lightbox="../media/quickstarts/assistant-ai-studio-session.png":::
-
-You could also consult the logs in the right-hand panel to confirm that code interpreter was used and to validate the code that was run to generate the response. It is important to remember that while code interpreter gives the model the capability to respond to more complex math questions by converting the questions into code and running in a sandboxed Python environment, you still need to validate the response to confirm that the model correctly translated your question into a valid representation in code.
-
-## Key concepts
-
-While using the Assistants playground, keep the following concepts in mind. 
-
-### Tools
-
-An individual assistant can access up to 128 tools, including `code interpreter`, as well as any custom tools you create via [functions](../how-to/assistant-functions.md).
-
-### Chat session
-
-Chat session also known as a *thread* within the Assistant's API is where the conversation between the user and assistant occurs. Unlike traditional chat completion calls there is no limit to the number of messages in a thread. The assistant will automatically compress requests to fit the input token limit of the model.
-
-This also means that you are not controlling how many tokens are passed to the model during each turn of the conversation. Managing tokens is abstracted away and handled entirely by the Assistants API.
-
-Select the **Clear chat** button to delete the current conversation history.
-
-Underneath the text input box there are two buttons:
-
-- Add a message without run.
-- Add and run.
-
-### Logs
-
-Logs provide a detailed snapshot of the assistant's API activity.
-
-### Show panels
-
-By default there are three panels: assistant setup, chat session, and Logs. **Show panels** allows you to add, remove, and rearrange the panels. If you ever close a panel and need to get it back, use **Show panels** to restore the lost panel.
-
-## Clean up resources
-
-If you want to clean up and remove an Azure OpenAI resource, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
-
-- [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
-- [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
-
-Alternatively you can delete the [assistant](../assistants-reference.md#delete-assistant), or [thread](../assistants-reference-threads.md#delete-thread) via the [Assistant's API](../assistants-reference.md).
-
-## See also
-
-* Learn more about how to use Assistants with our [How-to guide on Assistants](../how-to/assistant.md).
-* [Azure OpenAI Assistants API samples](https://github.com/Azure-Samples/azureai-samples/tree/main/scenarios/Assistants)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エージェントスタジオに関するドキュメントの削除"
}
```

### Explanation
この変更は、「Assistants AI Studio」に関するドキュメントが完全に削除されたことを示しています。削除されたコンテンツは合計で134行あり、内容にはAzure OpenAIアシスタントの使用を開始するための手順や必要な情報、注意事項、キーポイント、クリーンアップ手順などが含まれていました。

これにより、Azure AI Foundryポータル内でのアシスタントの使用方法やモデルのデプロイに関するガイドラインが利用できなくなり、関連する情報を探しているユーザーにとっては重要な情報源が失われることになります。

このドキュメントが削除された背景には、内容の更新や再編成がある可能性があります。しかし、この変更は既存のユーザーにとって混乱を招く可能性が高く、アシスタント機能を利用する上でのアクセス可能なガイドが減少するため、注意が必要です。今後、関連する新しい情報を提供するためには別のドキュメントが追加されることが期待されます。

## articles/ai-services/openai/includes/assistants-csharp.md{#item-cc4697}

<details>
<summary>Diff</summary>
````diff
@@ -1,269 +0,0 @@
----
-title: 'Quickstart: Use the OpenAI Service via the .NET SDK'
-titleSuffix: Azure OpenAI in Azure AI Foundry Models
-description: Walkthrough on how to get started with Azure OpenAI and make your first completions call with the .NET SDK. 
-manager: masoucou
-author: aapowell
-ms.author: aapowell
-ms.service: azure-ai-openai
-ms.topic: include
-ms.date: 3/11/2025
----
-
-[Reference documentation](/dotnet/api/overview/azure/ai.openai.assistants-readme?context=/azure/ai-services/openai/context/context) |  [Source code](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/openai/Azure.AI.OpenAI/src) | [Package (NuGet)](https://www.nuget.org/packages/Azure.AI.OpenAI/)
-
-## Prerequisites
-
-- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
-- The [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0)
-- An Azure OpenAI resource with a [compatible model in a supported region](../concepts/models.md#assistants-preview).
-- We recommend reviewing the [Responsible AI transparency note](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=text) and other [Responsible AI resources](/legal/cognitive-services/openai/overview?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext) to familiarize yourself with the capabilities and limitations of the Azure OpenAI in Azure AI Foundry Models.
-- An Azure OpenAI resource with the `gpt-4o` model deployed was used testing this example.
-
-### Microsoft Entra ID prerequisites
-
-For the recommended keyless authentication with Microsoft Entra ID, you need to:
-- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
-- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
-
-## Set up
-
-1. Create a new folder `assistants-quickstart` and go to the quickstart folder with the following command:
-
-    ```shell
-    mkdir assistants-quickstart && cd assistants-quickstart
-    ```
-
-1. Create a new console application with the following command:
-
-    ```shell
-    dotnet new console
-    ```
-
-3. Install the [OpenAI .NET client library](https://www.nuget.org/packages/Azure.AI.OpenAI/) with the [dotnet add package](/dotnet/core/tools/dotnet-add-package) command:
-
-    ```console
-    dotnet add package Azure.AI.OpenAI --prerelease
-    ```
-
-1. For the **recommended** keyless authentication with Microsoft Entra ID, install the [Azure.Identity](https://www.nuget.org/packages/Azure.Identity) package with:
-
-    ```console
-    dotnet add package Azure.Identity
-    ```
-
-1. For the **recommended** keyless authentication with Microsoft Entra ID, sign in to Azure with the following command:
-
-    ```console
-    az login
-    ```
-
-## Retrieve resource information
-
-[!INCLUDE [resource authentication](resource-authentication.md)]
-
-## Run the quickstart
-
-The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with an `AzureKeyCredential` object. 
-
-#### [Microsoft Entra ID](#tab/keyless)
-
-```csharp
-AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new DefaultAzureCredential()); 
-```
-
-#### [API key](#tab/api-key)
-
-```csharp
-AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new AzureKeyCredential(key));
-```
----
-
-To run the quickstart, follow these steps:
-
-1. Replace the contents of `Program.cs` with the following code and update the placeholder values with your own.
-    
-    ```csharp
-    using Azure;
-    using Azure.AI.OpenAI;
-    using Azure.Identity;
-    using OpenAI.Assistants;
-    using OpenAI.Files;
-    using System.ClientModel;
-    
-    // Assistants is a beta API and subject to change
-    // Acknowledge its experimental status by suppressing the matching warning.
-    #pragma warning disable OPENAI001
-    
-    string deploymentName = "gpt-4o";
-    
-    string endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT") ?? "https://<your-resource-name>.openai.azure.com/";
-    string key = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY") ?? "<your-key>";
-    
-    // Use the recommended keyless credential instead of the AzureKeyCredential credential.
-    AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new DefaultAzureCredential()); 
-    //AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new AzureKeyCredential(key));
-    
-    OpenAIFileClient fileClient = openAIClient.GetOpenAIFileClient();
-    AssistantClient assistantClient = openAIClient.GetAssistantClient();
-    
-    // First, let's contrive a document we'll use retrieval with and upload it.
-    using Stream document = BinaryData.FromString("""
-        {
-            "description": "This document contains the sale history data for Contoso products.",
-            "sales": [
-                {
-                    "month": "January",
-                    "by_product": {
-                        "113043": 15,
-                        "113045": 12,
-                        "113049": 2
-                    }
-                },
-                {
-                    "month": "February",
-                    "by_product": {
-                        "113045": 22
-                    }
-                },
-                {
-                    "month": "March",
-                    "by_product": {
-                        "113045": 16,
-                        "113055": 5
-                    }
-                }
-            ]
-        }
-        """).ToStream();
-    
-    OpenAI.Files.OpenAIFile salesFile = await fileClient.UploadFileAsync(
-        document,
-        "monthly_sales.json",
-        FileUploadPurpose.Assistants);
-    
-    // Now, we'll create a client intended to help with that data
-    OpenAI.Assistants.AssistantCreationOptions assistantOptions = new()
-    {
-        Name = "Example: Contoso sales RAG",
-        Instructions =
-            "You are an assistant that looks up sales data and helps visualize the information based"
-            + " on user queries. When asked to generate a graph, chart, or other visualization, use"
-            + " the code interpreter tool to do so.",
-        Tools =
-                {
-                    new FileSearchToolDefinition(),
-                    new OpenAI.Assistants.CodeInterpreterToolDefinition(),
-                },
-        ToolResources = new()
-        {
-            FileSearch = new()
-            {
-                NewVectorStores =
-                    {
-                        new VectorStoreCreationHelper([salesFile.Id]),
-                    }
-            }
-        },
-    };
-    
-    Assistant assistant = await assistantClient.CreateAssistantAsync(deploymentName, assistantOptions);
-    
-    // Create and run a thread with a user query about the data already associated with the assistant
-    ThreadCreationOptions threadOptions = new()
-    {
-        InitialMessages = { "How well did product 113045 sell in February? Graph its trend over time." }
-    };
-    
-    var initialMessage = new OpenAI.Assistants.ThreadInitializationMessage(OpenAI.Assistants.MessageRole.User, ["hi"]);
-    
-    ThreadRun threadRun = await assistantClient.CreateThreadAndRunAsync(assistant.Id, threadOptions);
-    
-    // Check back to see when the run is done
-    do
-    {
-        Thread.Sleep(TimeSpan.FromSeconds(1));
-        threadRun = assistantClient.GetRun(threadRun.ThreadId, threadRun.Id);
-    } while (!threadRun.Status.IsTerminal);
-    
-    // Finally, we'll print out the full history for the thread that includes the augmented generation
-    AsyncCollectionResult<OpenAI.Assistants.ThreadMessage> messages
-        = assistantClient.GetMessagesAsync(
-            threadRun.ThreadId,
-            new MessageCollectionOptions() { Order = MessageCollectionOrder.Ascending });
-    
-    await foreach (OpenAI.Assistants.ThreadMessage message in messages)
-    {
-        Console.Write($"[{message.Role.ToString().ToUpper()}]: ");
-        foreach (OpenAI.Assistants.MessageContent contentItem in message.Content)
-        {
-            if (!string.IsNullOrEmpty(contentItem.Text))
-            {
-                Console.WriteLine($"{contentItem.Text}");
-    
-                if (contentItem.TextAnnotations.Count > 0)
-                {
-                    Console.WriteLine();
-                }
-    
-                // Include annotations, if any.
-                foreach (TextAnnotation annotation in contentItem.TextAnnotations)
-                {
-                    if (!string.IsNullOrEmpty(annotation.InputFileId))
-                    {
-                        Console.WriteLine($"* File citation, file ID: {annotation.InputFileId}");
-                    }
-                    if (!string.IsNullOrEmpty(annotation.OutputFileId))
-                    {
-                        Console.WriteLine($"* File output, new file ID: {annotation.OutputFileId}");
-                    }
-                }
-            }
-            if (!string.IsNullOrEmpty(contentItem.ImageFileId))
-            {
-                OpenAI.Files.OpenAIFile imageFile = await fileClient.GetFileAsync(contentItem.ImageFileId);
-                BinaryData imageBytes = await fileClient.DownloadFileAsync(contentItem.ImageFileId);
-                using FileStream stream = File.OpenWrite($"{imageFile.Filename}.png");
-                imageBytes.ToStream().CopyTo(stream);
-    
-                Console.WriteLine($"<image: {imageFile.Filename}.png>");
-            }
-        }
-        Console.WriteLine();
-    }
-    ```
-
-1. Run the application with the following command:
-
-    ```shell
-    dotnet run
-    ```
-
-## Output
-
-The console output should resemble the following:
-
-```text
-[USER]: How well did product 113045 sell in February? Graph its trend over time.
-
-[ASSISTANT]: Product 113045 sold 22 units in February. Let's visualize its sales trend over the given months (January through March).
-
-I'll create a graph to depict this trend.
-
-[ASSISTANT]: <image: 553380b7-fdb6-49cf-9df6-e8e6700d69f4.png>
-The graph above visualizes the sales trend for product 113045 from January to March. As seen, the sales peaked in February with 22 units sold, and fluctuated over the period from January (12 units) to March (16 units).
-
-If you need further analysis or more details, feel free to ask!
-```
-
-## Clean up resources
-
-If you want to clean up and remove an Azure OpenAI resource, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
-
-- [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
-- [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
-
-## See also
-
-* Learn more about how to use Assistants with our [How-to guide on Assistants](../how-to/assistant.md).
-* [Azure OpenAI Assistants API samples](https://github.com/Azure-Samples/azureai-samples/tree/main/scenarios/Assistants)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "C#によるアシスタントの使い方に関するドキュメントの削除"
}
```

### Explanation
この変更は、C#を使用してAzure OpenAIサービスにアクセスするためのクイックスタートガイドが完全に削除されたことを示しています。削除されたコンテンツは269行で、これによりユーザーは.NET SDKを通じてOpenAIサービスを利用するための手順や必要な情報を失うことになります。

削除されたドキュメントには、前提条件としてAzureサブスクリプションや.NET SDKのインストール方法、Microsoft Entra IDを利用したキーレス認証に関する情報が含まれていました。また、サンプルコードや実行方法が詳細に記載されており、ユーザーが直ちにOpenAIサービスを使い始めるための具体的な手順を提供していました。

このような重要なリソースの削除は、Azure OpenAIサービスを利用したい開発者やデベロッパーにとって大きな影響を与える可能性があり、利用者が前もって準備するための情報が不足することになります。今後、これに代わる新しいドキュメントや更新が期待されますが、現時点では既存のドキュメントにアクセスできなくなったことは、利用者にとっての大きな課題となるでしょう。

## articles/ai-services/openai/includes/assistants-javascript.md{#item-ad3627}

<details>
<summary>Diff</summary>
````diff
@@ -1,313 +0,0 @@
----
-title: 'Quickstart: Use the Azure OpenAI in Azure AI Foundry Models via the JavaScript SDK'
-titleSuffix: Azure OpenAI
-description: Walkthrough on how to get started with Azure OpenAI and make your first completions call with the JavaScript SDK. 
-manager: nitinme
-author: aahill
-ms.author: aahi
-ms.service: azure-ai-openai
-ms.topic: include
-ms.date: 10/28/2024
-ms.custom: passwordless-ts, devex-track-js
----
-
-<a href="/javascript/api/@azure/openai-assistants" target="_blank">Reference documentation</a> | <a href="https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai" target="_blank">Library source code</a> | <a href="https://www.npmjs.com/package/@azure/openai-assistants" target="_blank">Package (npm)</a> |
-
-## Prerequisites
-
-- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
-- <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
-- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI. 
-- An Azure OpenAI resource with a [compatible model in a supported region](../concepts/models.md#assistants-preview).
-- We recommend reviewing the [Responsible AI transparency note](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=text) and other [Responsible AI resources](/legal/cognitive-services/openai/overview?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext) to familiarize yourself with the capabilities and limitations of the Azure OpenAI in Azure AI Foundry Models.
-- An Azure OpenAI resource with the `gpt-4 (1106-preview)` model deployed was used testing this example. 
-
-### Microsoft Entra ID prerequisites
-
-For the recommended keyless authentication with Microsoft Entra ID, you need to:
-- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
-- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
-
-## Set up
- 
-1. Create a new folder `assistants-quickstart` and go to the quickstart folder with the following command:
-
-    ```shell
-    mkdir assistants-quickstart && cd assistants-quickstart
-    ```
-    
-
-1. Create the `package.json` with the following command:
-
-    ```shell
-    npm init -y
-    ```   
-
-1. Install the OpenAI client library for JavaScript with:
-
-    ```console
-    npm install openai
-    ```
-
-1. For the **recommended** passwordless authentication:
-
-    ```console
-    npm install @azure/identity
-    ```
-
-
-## Retrieve resource information
-
-[!INCLUDE [resource authentication](resource-authentication.md)]
-
-> [!CAUTION]
-> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
-
-
-## Create an assistant
-
-In our code we're going to specify the following values:
-
-| **Name** | **Description** |
-|:---|:---|
-| **Assistant name** | Your deployment name that is associated with a specific model. |
-| **Instructions** | Instructions are similar to system messages this is where you give the model guidance about how it should behave and any context it should reference when generating a response. You can describe the assistant's personality, tell it what it should and shouldn't answer, and tell it how to format responses. You can also provide examples of the steps it should take when answering responses. |
-| **Model** | This is the deployment name. |
-| **Code interpreter** | Code interpreter provides access to a sandboxed Python environment that can be used to allow the model to test and execute code. |
-
-### Tools
-
-An individual assistant can access up to 128 tools including `code interpreter`, and any custom tools you create via [functions](../how-to/assistant-functions.md).
-    
-## Create a new JavaScript application
-
-#### [Microsoft Entra ID](#tab/keyless)
-
-1. Create the `index.js` file with the following code:
-
-    ```javascript
-    const { AzureOpenAI } = require("openai");
-    const {
-      DefaultAzureCredential,
-      getBearerTokenProvider,
-    } = require("@azure/identity");
-    
-    // Get environment variables
-    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
-    const azureOpenAIDeployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "Your deployment name";
-    const azureOpenAIVersion = process.env.OPENAI_API_VERSION || "A supported API version";
-    
-    // Check env variables
-    if (!azureOpenAIEndpoint || !azureOpenAIDeployment || !azureOpenAIVersion) {
-      throw new Error(
-        "You need to set the endpoint, deployment name, and API version."
-      );
-    }
-    
-    // Get Azure SDK client
-    const getClient = () => {
-      const credential = new DefaultAzureCredential();
-      const scope = "https://cognitiveservices.azure.com/.default";
-      const azureADTokenProvider = getBearerTokenProvider(credential, scope);
-
-      const assistantsClient = new AzureOpenAI({
-        endpoint: azureOpenAIEndpoint,
-        apiVersion: azureOpenAIVersion,
-        azureADTokenProvider,
-      });
-      return assistantsClient;
-    };
-    
-    const assistantsClient = getClient();
-    
-    const options = {
-      model: azureOpenAIDeployment, // Deployment name seen in Azure AI Foundry portal
-      name: "Math Tutor",
-      instructions:
-        "You are a personal math tutor. Write and run JavaScript code to answer math questions.",
-      tools: [{ type: "code_interpreter" }],
-    };
-    const role = "user";
-    const message = "I need to solve the equation `3x + 11 = 14`. Can you help me?";
-    
-    // Create an assistant
-    const assistantResponse = await assistantsClient.beta.assistants.create(
-      options
-    );
-    console.log(`Assistant created: ${JSON.stringify(assistantResponse)}`);
-    
-    // Create a thread
-    const assistantThread = await assistantsClient.beta.threads.create({});
-    console.log(`Thread created: ${JSON.stringify(assistantThread)}`);
-    
-    // Add a user question to the thread
-    const threadResponse = await assistantsClient.beta.threads.messages.create(
-      assistantThread.id,
-      {
-        role,
-        content: message,
-      }
-    );
-    console.log(`Message created:  ${JSON.stringify(threadResponse)}`);
-    
-    // Run the thread and poll it until it is in a terminal state
-    const runResponse = await assistantsClient.beta.threads.runs.createAndPoll(
-      assistantThread.id,
-      {
-        assistant_id: assistantResponse.id,
-      },
-      { pollIntervalMs: 500 }
-    );
-    console.log(`Run created:  ${JSON.stringify(runResponse)}`);
-    
-    // Get the messages
-    const runMessages = await assistantsClient.beta.threads.messages.list(
-      assistantThread.id
-    );
-    for await (const runMessageDatum of runMessages) {
-      for (const item of runMessageDatum.content) {
-        // types are: "image_file" or "text"
-        if (item.type === "text") {
-          console.log(`Message content: ${JSON.stringify(item.text?.value)}`);
-        }
-      }
-    }
-    ```
-
-1. Sign in to Azure with the following command:
-
-    ```shell
-    az login
-    ```
-
-1. Run the JavaScript file.
-
-    ```shell
-    node index.js
-    ```
-
-#### [API key](#tab/api-key)
-
-1. Create the `index.js` file with the following code:
-
-    ```javascript
-    const { AzureOpenAI } = require("openai");
-    
-    // Get environment variables
-    const azureOpenAIKey = process.env.AZURE_OPENAI_KEY || "Your API key";
-    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
-    const azureOpenAIDeployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "Your deployment name";
-    const azureOpenAIVersion = process.env.OPENAI_API_VERSION || "A supported API version";
-    
-    // Check env variables
-    if (!azureOpenAIKey || !azureOpenAIEndpoint || !azureOpenAIDeployment || !azureOpenAIVersion) {
-      throw new Error(
-        "You need to set the endpoint, deployment name, and API version."
-      );
-    }
-    
-    // Get Azure SDK client
-    const getClient = () => {
-      const assistantsClient = new AzureOpenAI({
-        endpoint: azureOpenAIEndpoint,
-        apiVersion: azureOpenAIVersion,
-        apiKey: azureOpenAIKey,
-      });
-      return assistantsClient;
-    };
-    
-    const assistantsClient = getClient();
-    
-    const options = {
-      model: azureOpenAIDeployment, // Deployment name seen in Azure AI Foundry portal
-      name: "Math Tutor",
-      instructions:
-        "You are a personal math tutor. Write and run JavaScript code to answer math questions.",
-      tools: [{ type: "code_interpreter" }],
-    };
-    const role = "user";
-    const message = "I need to solve the equation `3x + 11 = 14`. Can you help me?";
-    
-    // Create an assistant
-    const assistantResponse = await assistantsClient.beta.assistants.create(
-      options
-    );
-    console.log(`Assistant created: ${JSON.stringify(assistantResponse)}`);
-    
-    // Create a thread
-    const assistantThread = await assistantsClient.beta.threads.create({});
-    console.log(`Thread created: ${JSON.stringify(assistantThread)}`);
-    
-    // Add a user question to the thread
-    const threadResponse = await assistantsClient.beta.threads.messages.create(
-      assistantThread.id,
-      {
-        role,
-        content: message,
-      }
-    );
-    console.log(`Message created:  ${JSON.stringify(threadResponse)}`);
-    
-    // Run the thread and poll it until it is in a terminal state
-    const runResponse = await assistantsClient.beta.threads.runs.createAndPoll(
-      assistantThread.id,
-      {
-        assistant_id: assistantResponse.id,
-      },
-      { pollIntervalMs: 500 }
-    );
-    console.log(`Run created:  ${JSON.stringify(runResponse)}`);
-    
-    // Get the messages
-    const runMessages = await assistantsClient.beta.threads.messages.list(
-      assistantThread.id
-    );
-    for await (const runMessageDatum of runMessages) {
-      for (const item of runMessageDatum.content) {
-        // types are: "image_file" or "text"
-        if (item.type === "text") {
-          console.log(`Message content: ${JSON.stringify(item.text?.value)}`);
-        }
-      }
-    }
-    ```
-
-1. Run the JavaScript file.
-
-    ```shell
-    node index.js
-    ```
-
----
-
-## Output
-
-```console
-Assistant created: {"id":"asst_zXaZ5usTjdD0JGcNViJM2M6N","createdAt":"2024-04-08T19:26:38.000Z","name":"Math Tutor","description":null,"model":"daisy","instructions":"You are a personal math tutor. Write and run JavaScript code to answer math questions.","tools":[{"type":"code_interpreter"}],"fileIds":[],"metadata":{}}
-Thread created: {"id":"thread_KJuyrB7hynun4rvxWdfKLIqy","createdAt":"2024-04-08T19:26:38.000Z","metadata":{}}
-Message created:  {"id":"msg_o0VkXnQj3juOXXRCnlZ686ff","createdAt":"2024-04-08T19:26:38.000Z","threadId":"thread_KJuyrB7hynun4rvxWdfKLIqy","role":"user","content":[{"type":"text","text":{"value":"I need to solve the equation `3x + 11 = 14`. Can you help me?","annotations":[]},"imageFile":{}}],"assistantId":null,"runId":null,"fileIds":[],"metadata":{}}
-Created run
-Run created:  {"id":"run_P8CvlouB8V9ZWxYiiVdL0FND","object":"thread.run","status":"queued","model":"daisy","instructions":"You are a personal math tutor. Write and run JavaScript code to answer math questions.","tools":[{"type":"code_interpreter"}],"metadata":{},"usage":null,"assistantId":"asst_zXaZ5usTjdD0JGcNViJM2M6N","threadId":"thread_KJuyrB7hynun4rvxWdfKLIqy","fileIds":[],"createdAt":"2024-04-08T19:26:39.000Z","expiresAt":"2024-04-08T19:36:39.000Z","startedAt":null,"completedAt":null,"cancelledAt":null,"failedAt":null}
-Message content: "The solution to the equation \\(3x + 11 = 14\\) is \\(x = 1\\)."
-Message content: "Yes, of course! To solve the equation \\( 3x + 11 = 14 \\), we can follow these steps:\n\n1. Subtract 11 from both sides of the equation to isolate the term with x.\n2. Then, divide by 3 to find the value of x.\n\nLet me calculate that for you."
-Message content: "I need to solve the equation `3x + 11 = 14`. Can you help me?"
-```
-
-It's important to remember that while the code interpreter gives the model the capability to respond to more complex queries by converting the questions into code and running that code iteratively in JavaScript until it reaches a solution, you still need to validate the response to confirm that the model correctly translated your question into a valid representation in code.
-
-## Clean up resources
-
-If you want to clean up and remove an Azure OpenAI resource, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
-
-- [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
-- [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
-
-## Sample code
-
-* [Quickstart sample code](https://github.com/Azure-Samples/azure-typescript-e2e-apps/tree/main/quickstarts/azure-openai-assistants)
-
-## See also
-
-* Learn more about how to use Assistants with our [How-to guide on Assistants](../how-to/assistant.md).
-* [Azure OpenAI Assistants API samples](https://github.com/Azure-Samples/azureai-samples/tree/main/scenarios/Assistants)
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "JavaScriptによるアシスタントの使い方に関するドキュメントの削除"
}
```

### Explanation
この変更は、Azure OpenAIサービスをJavaScript SDKを使用して利用するためのクイックスタートガイドが完全に削除されたことを示しています。削除されたコンテンツは313行あり、これによりユーザーはJavaScriptでOpenAIサービスにアクセスする際の手順や必要な情報を失うことになります。

削除されたドキュメントには、AzureサブスクリプションやNode.jsのインストール、Azure CLIを使用したパスワードレス認証に関する手順が含まれていました。また、サンプルコードが提供されており、具体的な実装方法やアシスタントの作成、スレッドの実行方法が詳細に説明されていました。

このような重要なリソースの削除は、JavaScriptを使用している開発者やデベロッパーにとって大きな影響を及ぼす可能性があります。特に、初心者にとっては適切な導入ガイドを失うことは、学習の妨げとなり得ます。今後、新しい文書が提供されることが期待されますが、現時点ではこの重要な情報源が利用できなくなったことで、ユーザーにとっての課題が増えることになります。

## articles/ai-services/openai/includes/assistants-python.md{#item-82d745}

<details>
<summary>Diff</summary>
````diff
@@ -1,263 +0,0 @@
----
-title: 'Quickstart: Use the OpenAI Service via the Python SDK'
-titleSuffix: Azure OpenAI in Azure AI Foundry Models
-description: Walkthrough on how to get started with Azure OpenAI and make your first Assistants call with the Python SDK. 
-manager: nitinme
-author: aahill
-ms.author: aahi
-ms.service: azure-ai-openai
-ms.topic: include
-ms.date: 05/22/2024
----
-
-[Reference documentation](https://platform.openai.com/docs/api-reference/assistants/createAssistant) | <a href="https://github.com/openai/openai-python" target="_blank">Library source code</a> | <a href="https://pypi.org/project/openai/" target="_blank">Package (PyPi)</a> |
-
-## Prerequisites
-
-- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
-- <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>
-- The following Python libraries: os, openai (Version 1.x is required)
-- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI. 
-- An Azure OpenAI resource with a [compatible model in a supported region](../concepts/models.md#assistants-preview).
-- We recommend reviewing the [Responsible AI transparency note](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=text) and other [Responsible AI resources](/legal/cognitive-services/openai/overview?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext) to familiarize yourself with the capabilities and limitations of the Azure OpenAI in Azure AI Foundry Models.
-- An Azure OpenAI resource with the `gpt-4 (1106-preview)` model deployed was used testing this example.
-
-## Passwordless authentication is recommended
-
-For passwordless authentication, you need to:
-
-1. Use the [azure-identity](https://pypi.org/project/azure-identity/) package.
-2. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal under **Access control (IAM)** > **Add role assignment**.
-3. Sign in with the Azure CLI such as `az login`.
-
-## Set up
-
-1. Install the OpenAI Python client library with:
-
-```console
-pip install openai
-```
-
-2. For the **recommended** passwordless authentication:
-
-```console
-pip install azure-identity
-```
-
-> [!NOTE]
-> This library is maintained by OpenAI. Refer to the [release history](https://github.com/openai/openai-python/releases) to track the latest updates to the library.
-
-## Retrieve key and endpoint
-
-To successfully make a call against the Azure OpenAI service, you'll need the following:
-
-|Variable name | Value |
-|--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. You can also find the endpoint via the **Deployments** page in Azure AI Foundry portal. An example endpoint is: `https://docs-test-001.openai.azure.com/`.|
-| `API-KEY` | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
-| `DEPLOYMENT-NAME` | This value will correspond to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Model Deployments** in the Azure portal or via the **Deployments** page in Azure AI Foundry portal.|
-
-Go to your resource in the Azure portal. The **Keys and Endpoint** can be found in the **Resource Management** section. Copy your endpoint and access key as you'll need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
-
-:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview blade for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location circled in red." lightbox="../media/quickstarts/endpoint.png":::
-
-[!INCLUDE [environment-variables](environment-variables.md)]
-
-## Create an assistant
-
-In our code we are going to specify the following values:
-
-| **Name** | **Description** |
-|:---|:---|
-| **Assistant name** | Your deployment name that is associated with a specific model. |
-| **Instructions** | Instructions are similar to system messages this is where you give the model guidance about how it should behave and any context it should reference when generating a response. You can describe the assistant's personality, tell it what it should and shouldn't answer, and tell it how to format responses. You can also provide examples of the steps it should take when answering responses. |
-| **Model** | This is where you set which model deployment name to use with your assistant. The retrieval tool requires `gpt-35-turbo (1106)` or `gpt-4 (1106-preview)` model. **Set this value to your deployment name, not the model name unless it is the same.** |
-| **Code interpreter** | Code interpreter provides access to a sandboxed Python environment that can be used to allow the model to test and execute code. |
-
-### Tools
-
-An individual assistant can access up to 128 tools including `code interpreter`, as well as any custom tools you create via [functions](../how-to/assistant-functions.md).
-
-### Create the Python app
-
-Sign in to Azure with `az login` then create and run an assistant with the following **recommended** passwordless Python example:
-
-```python
-import os
-from azure.identity import DefaultAzureCredential, get_bearer_token_provider
-from openai import AzureOpenAI
-
-token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")
-
-client = AzureOpenAI(
-    azure_ad_token_provider=token_provider,
-    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
-    api_version="2024-05-01-preview",
-)
-
-# Create an assistant
-assistant = client.beta.assistants.create(
-    name="Math Assist",
-    instructions="You are an AI assistant that can write code to help answer math questions.",
-    tools=[{"type": "code_interpreter"}],
-    model="gpt-4-1106-preview" # You must replace this value with the deployment name for your model.
-)
-
-# Create a thread
-thread = client.beta.threads.create()
-
-# Add a user question to the thread
-message = client.beta.threads.messages.create(
-    thread_id=thread.id,
-    role="user",
-    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
-)
-
-# Run the thread and poll for the result
-run = client.beta.threads.runs.create_and_poll(
-    thread_id=thread.id,
-    assistant_id=assistant.id,
-    instructions="Please address the user as Jane Doe. The user has a premium account.",
-)
-
-print("Run completed with status: " + run.status)
-
-if run.status == "completed":
-    messages = client.beta.threads.messages.list(thread_id=thread.id)
-    print(messages.to_json(indent=2))
-```
-
-To use the service API key for authentication, you can create and run an assistant with the following Python example:
-
-```python
-import os
-from openai import AzureOpenAI
-
-client = AzureOpenAI(
-    api_key=os.environ["AZURE_OPENAI_API_KEY"],
-    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
-    api_version="2024-05-01-preview",
-)
-
-# Create an assistant
-assistant = client.beta.assistants.create(
-    name="Math Assist",
-    instructions="You are an AI assistant that can write code to help answer math questions.",
-    tools=[{"type": "code_interpreter"}],
-    model="gpt-4-1106-preview" # You must replace this value with the deployment name for your model.
-)
-
-# Create a thread
-thread = client.beta.threads.create()
-
-# Add a user question to the thread
-message = client.beta.threads.messages.create(
-    thread_id=thread.id,
-    role="user",
-    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
-)
-
-# Run the thread and poll for the result
-run = client.beta.threads.runs.create_and_poll(
-    thread_id=thread.id,
-    assistant_id=assistant.id,
-    instructions="Please address the user as Jane Doe. The user has a premium account.",
-)
-
-print("Run completed with status: " + run.status)
-
-if run.status == "completed":
-    messages = client.beta.threads.messages.list(thread_id=thread.id)
-    print(messages.to_json(indent=2))
-```
-
-## Output
-
-Run completed with status: completed
-
-```json
-{
-  "data": [
-    {
-      "id": "msg_4SuWxTubHsHpt5IlBTO5Hyw9",
-      "assistant_id": "asst_cYqL1RuwLyFV3HU1gkaE2k0K",
-      "attachments": [],
-      "content": [
-        {
-          "text": {
-            "annotations": [],
-            "value": "The solution to the equation \\(3x + 11 = 14\\) is \\(x = 1\\)."
-          },
-          "type": "text"
-        }
-      ],
-      "created_at": 1716397091,
-      "metadata": {},
-      "object": "thread.message",
-      "role": "assistant",
-      "run_id": "run_hFgBPbUtO8ZNTnNPC8PgpH1S",
-      "thread_id": "thread_isb7spwRycI5ueT9E7357aOm"
-    },
-    {
-      "id": "msg_Z32w2E7kY5wEWhZqQWxIbIUB",
-      "assistant_id": null,
-      "attachments": [],
-      "content": [
-        {
-          "text": {
-            "annotations": [],
-            "value": "I need to solve the equation `3x + 11 = 14`. Can you help me?"
-          },
-          "type": "text"
-        }
-      ],
-      "created_at": 1716397025,
-      "metadata": {},
-      "object": "thread.message",
-      "role": "user",
-      "run_id": null,
-      "thread_id": "thread_isb7spwRycI5ueT9E7357aOm"
-    }
-  ],
-  "object": "list",
-  "first_id": "msg_4SuWxTubHsHpt5IlBTO5Hyw9",
-  "last_id": "msg_Z32w2E7kY5wEWhZqQWxIbIUB",
-  "has_more": false
-}
-```
-
-## Understanding your results
-
-In this example we create an assistant with code interpreter enabled. When we ask the assistant a math question it translates the question into python code and executes the code in sandboxed environment in order to determine the answer to the question. The code the model creates and tests to arrive at an answer is:
-
-```python
-from sympy import symbols, Eq, solve  
-  
-# Define the variable  
-x = symbols('x')  
-  
-# Define the equation  
-equation = Eq(3*x + 11, 14)  
-  
-# Solve the equation  
-solution = solve(equation, x)  
-solution  
-```
-
-It is important to remember that while code interpreter gives the model the capability to respond to more complex queries by converting the questions into code and running that code iteratively in the Python sandbox until it reaches a solution, you still need to validate the response to confirm that the model correctly translated your question into a valid representation in code.
-
-<!--We walk through the process of creating assistants with code in much more depth in our [Azure OpenAI Assistants how-to guide](../how-to/assistant.md).-->
-
-## Clean up resources
-
-If you want to clean up and remove an Azure OpenAI resource, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
-
-- [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
-- [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
-
-## See also
-
-* Learn more about how to use Assistants with our [How-to guide on Assistants](../how-to/assistant.md).
-* [Azure OpenAI Assistants API samples](https://github.com/Azure-Samples/azureai-samples/tree/main/scenarios/Assistants)
-
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Pythonによるアシスタントの使い方に関するドキュメントの削除"
}
```

### Explanation
この変更は、Azure OpenAIサービスをPython SDKを使用して利用するためのクイックスタートガイドが完全に削除されたことを示しています。削除されたコンテンツは263行で、これによりユーザーはPythonでOpenAIサービスにアクセスする際の手順や必要な情報を失います。

削除されたドキュメントには、AzureサブスクリプションやPythonの環境設定に関する手順、パスワードレス認証の設定方法が含まれていました。また、サンプルコードが具体的に提供されており、アシスタントの作成やスレッドの実行方法、エラーハンドリングの指針が詳細に説明されていました。

このような重要なリソースの削除は、Pythonを使用した開発者やデベロッパーにとって大きな影響を与える可能性があります。特に、初心者にとっては適切な導入ガイドを失うことは、学習の妨げとなります。また、ユーザーが実際のアプリケーションを構築する際に必要な情報が不足するため、開発プロセスにおける障壁が高まることが懸念されます。今後、新しい文書が提供されることが期待されますが、現時点ではこの重要な情報源が利用できなくなったことは、ユーザーにとっての大きな課題となるでしょう。

## articles/ai-services/openai/includes/assistants-rest.md{#item-261c46}

<details>
<summary>Diff</summary>
````diff
@@ -1,146 +0,0 @@
----
-title: 'Quickstart: Use the OpenAI Service to make your AI Assistant with the REST API'
-titleSuffix: Azure OpenAI in Azure AI Foundry Models
-description: Walkthrough on how to get started with Azure OpenAI AI Assistants API with the REST API. 
-manager: nitinme
-author: aahill
-ms.author: aahi
-ms.service: azure-ai-openai
-ms.topic: include
-ms.date: 05/20/2024
----
-
-## Prerequisites
-
-- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
-- <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>
-- An Azure OpenAI resource with a [compatible model in a supported region](../concepts/models.md#assistants-preview).
-- We recommend reviewing the [Responsible AI transparency note](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=text) and other [Responsible AI resources](/legal/cognitive-services/openai/overview?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext) to familiarize yourself with the capabilities and limitations of the Azure OpenAI in Azure AI Foundry Models.
-- An Azure OpenAI resource with the `gpt-4 (1106-preview)` model deployed was used testing this example.
-
-
-## Set up
-
-### Retrieve key and endpoint
-
-To successfully make a call against Azure OpenAI, you'll need the following:
-
-|Variable name | Value |
-|--------------------------|-------------|
-| `ENDPOINT`               | The service endpoint can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the endpoint via the **Deployments** page in Azure AI Foundry portal. An example endpoint is: `https://docs-test-001.openai.azure.com/`.|
-| `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
-| `DEPLOYMENT-NAME` | This value will correspond to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Deployments** in the Azure portal or via the **Deployments** page in Azure AI Foundry portal.|
-
-Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you'll need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
-
-:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview blade for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location circled in red." lightbox="../media/quickstarts/endpoint.png":::
-
-[!INCLUDE [environment-variables](environment-variables.md)]
-
-## REST API
-
-### Create an assistant
-
-> [!NOTE]
-> With Azure OpenAI the `model` parameter requires model deployment name. If your model deployment name is different than the underlying model name then you would adjust your code to ` "model": "{your-custom-model-deployment-name}"`.
-
-```console
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/assistants?api-version=2024-05-01-preview \
-  -H "api-key: $AZURE_OPENAI_API_KEY" \
-  -H "Content-Type: application/json" \
-  -d '{
-    "instructions": "You are an AI assistant that can write code to help answer math questions.",
-    "name": "Math Assist",
-    "tools": [{"type": "code_interpreter"}],
-    "model": "gpt-4-1106-preview"
-  }'
-```
-
-### Tools
-
-An individual assistant can access up to 128 tools including `code interpreter`, as well as any custom tools you create via [functions](../how-to/assistant-functions.md).
-
-
-### Create a thread
-
-```console
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/threads \
-  -H "Content-Type: application/json" \
-  -H "api-key: $AZURE_OPENAI_API_KEY" \
-  -d ''
-
-```
-
-### Add a user question to the thread
-
-```console
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/threads/thread_abc123/messages \
-  -H "Content-Type: application/json" \
-  -H "api-key: $AZURE_OPENAI_API_KEY" \
-  -d '{
-      "role": "user",
-      "content": "I need to solve the equation `3x + 11 = 14`. Can you help me?"
-    }'
-```
-
-### Run the thread
-
-```console
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/threads/thread_abc123/runs \
-  -H "api-key: $AZURE_OPENAI_API_KEY" \
-  -H "Content-Type: application/json" \
-  -d '{
-    "assistant_id": "asst_abc123",
-  }'
-```
-
-### Retrieve the status of the run
-
-```console
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/threads/thread_abc123/runs/run_abc123 \
-  -H "api-key: $AZURE_OPENAI_API_KEY" \
-```
-
-### Assistant response
-
-```
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/threads/thread_abc123/messages \
-  -H "Content-Type: application/json" \
-  -H "api-key: $AZURE_OPENAI_API_KEY" \
-```
-
-
-## Understanding your results
-
-In this example we create an assistant with code interpreter enabled. When we ask the assistant a math question it translates the question into python code and executes the code in sandboxed environment in order to determine the answer to the question. The code the model creates and tests to arrive at an answer is:
-
-```python
-    from sympy import symbols, Eq, solve  
-      
-    # Define the variable  
-    x = symbols('x')  
-      
-    # Define the equation  
-    equation = Eq(3*x + 11, 14)  
-      
-    # Solve the equation  
-    solution = solve(equation, x)  
-    solution  
-```
-
-It is important to remember that while code interpreter gives the model the capability to respond to more complex queries by converting the questions into code and running that code iteratively in the Python sandbox until it reaches a solution, you still need to validate the response to confirm that the model correctly translated your question into a valid representation in code.
-
-<!-- We walk through the process of creating assistants with code in much more depth in our [Azure OpenAI Assistants how-to guide](../how-to/assistant.md). -->
-
-## Clean up resources
-
-If you want to clean up and remove an Azure OpenAI resource, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
-
-- [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
-- [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
-
-## See also
-
-* Learn more about how to use Assistants with our [How-to guide on Assistants](../how-to/assistant.md).
-* [Azure OpenAI Assistants API samples](https://github.com/Azure-Samples/azureai-samples/tree/main/scenarios/Assistants)
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "REST APIを使用したAIアシスタントの構築に関するドキュメントの削除"
}
```

### Explanation
この変更は、Azure OpenAIサービスを利用してREST APIによりAIアシスタントを構築するためのクイックスタートガイドが完全に削除されたことを示しています。この変更により、146行のコードや説明が削除されており、ユーザーはアシスタントを作成するための手順を失いました。

削除されたドキュメントには、Azureサブスクリプションの作成方法や、必要なAPIエンドポイントおよびAPIキーの取得方法、アシスタントを作成するための具体的なcurlコマンドの例が含まれていました。また、アシスタントの使用方法やスレッドの作成、メッセージの送信、実行結果の取得に関する手順が詳細に記述されていました。

このようなリソースの削除は、REST APIを使用して開発を行うデベロッパーにとって大きな影響を及ぼす可能性があります。特に、APIを通じてアシスタント機能を利用しようとしているユーザーや新規の開発者にとって、必要な情報が失われることは大きな障壁となるでしょう。今後、新しいガイドが提供されることが期待されますが、現時点での情報源の欠如はユーザーにとっての厳しい課題となります。

## articles/ai-services/openai/includes/assistants-typescript.md{#item-3195a9}

<details>
<summary>Diff</summary>
````diff
@@ -1,373 +0,0 @@
----
-title: 'Quickstart: Use the Azure OpenAI in Azure AI Foundry Models via the JavaScript SDK'
-titleSuffix: Azure OpenAI
-description: Walkthrough on how to get started with Azure OpenAI and make your first completions call with the JavaScript SDK. 
-manager: nitinme
-author: aahill
-ms.author: aahi
-ms.service: azure-ai-openai
-ms.topic: include
-ms.date: 10/09/2024
-ms.custom: passwordless-js, devex-track-typescript
----
-
-<a href="/javascript/api/@azure/openai-assistants" target="_blank">Reference documentation</a> | <a href="https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai" target="_blank">Library source code</a> | <a href="https://www.npmjs.com/package/@azure/openai-assistants" target="_blank">Package (npm)</a> |
-
-## Prerequisites
-
-- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
-- <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
-- [TypeScript](https://www.typescriptlang.org/download/) installed globally
-- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI. 
-- An Azure OpenAI resource with a [compatible model in a supported region](../concepts/models.md#assistants-preview).
-- We recommend reviewing the [Responsible AI transparency note](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=text) and other [Responsible AI resources](/legal/cognitive-services/openai/overview?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext) to familiarize yourself with the capabilities and limitations of the Azure OpenAI in Azure AI Foundry Models.
-- An Azure OpenAI resource with the `gpt-4 (1106-preview)` model deployed was used testing this example. 
-
-### Microsoft Entra ID prerequisites
-
-For the recommended keyless authentication with Microsoft Entra ID, you need to:
-- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
-- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
-
-## Set up
-
-1. Create a new folder `assistants-quickstart` and go to the quickstart folder with the following command:
-
-    ```shell
-    mkdir assistants-quickstart && cd assistants-quickstart
-    ```
-    
-
-1. Create the `package.json` with the following command:
-
-    ```shell
-    npm init -y
-    ```
-
-1. Update the `package.json` to ECMAScript with the following command: 
-
-    ```shell
-    npm pkg set type=module
-    ```
-    
-
-1. Install the OpenAI client library for JavaScript with:
-
-    ```console
-    npm install openai
-    ```
-
-1. For the **recommended** passwordless authentication:
-
-    ```console
-    npm install @azure/identity
-    ```
-
-## Retrieve resource information
-
-[!INCLUDE [resource authentication](resource-authentication.md)]
-
-> [!CAUTION]
-> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
-
-## Create an assistant
-
-In our code we're going to specify the following values:
-
-| **Name** | **Description** |
-|:---|:---|
-| **Assistant name** | Your deployment name that is associated with a specific model. |
-| **Instructions** | Instructions are similar to system messages this is where you give the model guidance about how it should behave and any context it should reference when generating a response. You can describe the assistant's personality, tell it what it should and shouldn't answer, and tell it how to format responses. You can also provide examples of the steps it should take when answering responses. |
-| **Model** | This is the deployment name. |
-| **Code interpreter** | Code interpreter provides access to a sandboxed Python environment that can be used to allow the model to test and execute code. |
-
-### Tools
-
-An individual assistant can access up to 128 tools including `code interpreter`, and any custom tools you create via [functions](../how-to/assistant-functions.md).
-
-    
-## Create a new TypeScript application
-
-#### [Microsoft Entra ID](#tab/typescript-keyless)
-
-1. Create the `index.ts` file with the following code:
-
-    ```typescript
-    import { AzureOpenAI } from "openai";
-    import {
-      Assistant,
-      AssistantCreateParams,
-      AssistantTool,
-    } from "openai/resources/beta/assistants";
-    import { Message, MessagesPage } from "openai/resources/beta/threads/messages";
-    import { Run } from "openai/resources/beta/threads/runs/runs";
-    import { Thread } from "openai/resources/beta/threads/threads";
-    
-    // Add `Cognitive Services User` to identity for Azure OpenAI resource
-    import {
-      DefaultAzureCredential,
-      getBearerTokenProvider,
-    } from "@azure/identity";
-    
-    // Get environment variables
-    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint" as string;
-    const azureOpenAIDeployment = process.env
-      .AZURE_OPENAI_DEPLOYMENT_NAME  || "Your deployment name" as string;
-    const openAIVersion = process.env.OPENAI_API_VERSION || "A supported API version" as string;
-    
-    // Check env variables
-    if (!azureOpenAIEndpoint || !azureOpenAIDeployment || !openAIVersion) {
-      throw new Error(
-        "You need to set the endpoint, deployment name, and API version."
-      );
-    }
-    
-    // Get Azure SDK client
-    const getClient = (): AzureOpenAI => {
-      const credential = new DefaultAzureCredential();
-      const scope = "https://cognitiveservices.azure.com/.default";
-      const azureADTokenProvider = getBearerTokenProvider(credential, scope);
-      const assistantsClient = new AzureOpenAI({
-        endpoint: azureOpenAIEndpoint,
-        apiVersion: openAIVersion,
-        azureADTokenProvider,
-      });
-      return assistantsClient;
-    };
-    
-    const assistantsClient = getClient();
-    
-    const options: AssistantCreateParams = {
-      model: azureOpenAIDeployment, // Deployment name seen in Azure AI Foundry portal
-      name: "Math Tutor",
-      instructions:
-        "You are a personal math tutor. Write and run JavaScript code to answer math questions.",
-      tools: [{ type: "code_interpreter" } as AssistantTool],
-    };
-    const role = "user";
-    const message = "I need to solve the equation `3x + 11 = 14`. Can you help me?";
-    
-    // Create an assistant
-    const assistantResponse: Assistant =
-      await assistantsClient.beta.assistants.create(options);
-    console.log(`Assistant created: ${JSON.stringify(assistantResponse)}`);
-    
-    // Create a thread
-    const assistantThread: Thread = await assistantsClient.beta.threads.create({});
-    console.log(`Thread created: ${JSON.stringify(assistantThread)}`);
-    
-    // Add a user question to the thread
-    const threadResponse: Message =
-      await assistantsClient.beta.threads.messages.create(assistantThread.id, {
-        role,
-        content: message,
-      });
-    console.log(`Message created:  ${JSON.stringify(threadResponse)}`);
-    
-    // Run the thread and poll it until it is in a terminal state
-    const runResponse: Run = await assistantsClient.beta.threads.runs.createAndPoll(
-      assistantThread.id,
-      {
-        assistant_id: assistantResponse.id,
-      },
-      { pollIntervalMs: 500 }
-    );
-    console.log(`Run created:  ${JSON.stringify(runResponse)}`);
-    
-    // Get the messages
-    const runMessages: MessagesPage =
-      await assistantsClient.beta.threads.messages.list(assistantThread.id);
-    for await (const runMessageDatum of runMessages) {
-      for (const item of runMessageDatum.content) {
-        // types are: "image_file" or "text"
-        if (item.type === "text") {
-          console.log(`Message content: ${JSON.stringify(item.text?.value)}`);
-        }
-      }
-    }
-    ```
-
-1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
-
-    ```json
-    {
-        "compilerOptions": {
-          "module": "NodeNext",
-          "target": "ES2022", // Supports top-level await
-          "moduleResolution": "NodeNext",
-          "skipLibCheck": true, // Avoid type errors from node_modules
-          "strict": true // Enable strict type-checking options
-        },
-        "include": ["*.ts"]
-    }
-    ```
-
-1. Transpile from TypeScript to JavaScript.
-
-    ```shell
-    tsc
-    ```
-    
-1. Sign in to Azure with the following command:
-
-    ```shell
-    az login
-    ```
-
-1. Run the code with the following command:
-
-    ```shell
-    node index.js
-    ```
-
-#### [API key](#tab/typescript-key)
-
-1. Create the `index.ts` file with the following code:
-
-    ```typescript
-    import { AzureOpenAI } from "openai";
-    import {
-      Assistant,
-      AssistantCreateParams,
-      AssistantTool,
-    } from "openai/resources/beta/assistants";
-    import { Message, MessagesPage } from "openai/resources/beta/threads/messages";
-    import { Run } from "openai/resources/beta/threads/runs/runs";
-    import { Thread } from "openai/resources/beta/threads/threads";
-    
-    // Get environment variables
-    const azureOpenAIKey = process.env.AZURE_OPENAI_KEY || "Your API key" as string;
-    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint" as string;
-    const azureOpenAIDeployment = process.env
-      .AZURE_OPENAI_DEPLOYMENT_NAME || "Your deployment name" as string;
-    const openAIVersion = process.env.OPENAI_API_VERSION || "A supported API version" as string;
-    
-    // Check env variables
-    if (!azureOpenAIKey || !azureOpenAIEndpoint || !azureOpenAIDeployment || !openAIVersion) {
-      throw new Error(
-        "You need to set the endpoint, deployment name, and API version."
-      );
-    }
-    
-    // Get Azure SDK client
-    const getClient = (): AzureOpenAI => {
-      const assistantsClient = new AzureOpenAI({
-        endpoint: azureOpenAIEndpoint,
-        apiVersion: openAIVersion,
-        apiKey: azureOpenAIKey,
-      });
-      return assistantsClient;
-    };
-    
-    const assistantsClient = getClient();
-    
-    const options: AssistantCreateParams = {
-      model: azureOpenAIDeployment, // Deployment name seen in Azure AI Foundry portal
-      name: "Math Tutor",
-      instructions:
-        "You are a personal math tutor. Write and run JavaScript code to answer math questions.",
-      tools: [{ type: "code_interpreter" } as AssistantTool],
-    };
-    const role = "user";
-    const message = "I need to solve the equation `3x + 11 = 14`. Can you help me?";
-    
-    // Create an assistant
-    const assistantResponse: Assistant =
-      await assistantsClient.beta.assistants.create(options);
-    console.log(`Assistant created: ${JSON.stringify(assistantResponse)}`);
-    
-    // Create a thread
-    const assistantThread: Thread = await assistantsClient.beta.threads.create({});
-    console.log(`Thread created: ${JSON.stringify(assistantThread)}`);
-    
-    // Add a user question to the thread
-    const threadResponse: Message =
-      await assistantsClient.beta.threads.messages.create(assistantThread.id, {
-        role,
-        content: message,
-      });
-    console.log(`Message created:  ${JSON.stringify(threadResponse)}`);
-    
-    // Run the thread and poll it until it is in a terminal state
-    const runResponse: Run = await assistantsClient.beta.threads.runs.createAndPoll(
-      assistantThread.id,
-      {
-        assistant_id: assistantResponse.id,
-      },
-      { pollIntervalMs: 500 }
-    );
-    console.log(`Run created:  ${JSON.stringify(runResponse)}`);
-    
-    // Get the messages
-    const runMessages: MessagesPage =
-      await assistantsClient.beta.threads.messages.list(assistantThread.id);
-    for await (const runMessageDatum of runMessages) {
-      for (const item of runMessageDatum.content) {
-        // types are: "image_file" or "text"
-        if (item.type === "text") {
-          console.log(`Message content: ${JSON.stringify(item.text?.value)}`);
-        }
-      }
-    }
-    ```
-
-1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
-
-    ```json
-    {
-        "compilerOptions": {
-          "module": "NodeNext",
-          "target": "ES2022", // Supports top-level await
-          "moduleResolution": "NodeNext",
-          "skipLibCheck": true, // Avoid type errors from node_modules
-          "strict": true // Enable strict type-checking options
-        },
-        "include": ["*.ts"]
-    }
-    ```
-
-1. Transpile from TypeScript to JavaScript.
-
-    ```shell
-    tsc
-    ```
-
-1. Run the code with the following command:
-
-    ```shell
-    node index.js
-    ```
-
----
-
-## Output
-
-```console
-Assistant created: {"id":"asst_zXaZ5usTjdD0JGcNViJM2M6N","createdAt":"2024-04-08T19:26:38.000Z","name":"Math Tutor","description":null,"model":"daisy","instructions":"You are a personal math tutor. Write and run JavaScript code to answer math questions.","tools":[{"type":"code_interpreter"}],"fileIds":[],"metadata":{}}
-Thread created: {"id":"thread_KJuyrB7hynun4rvxWdfKLIqy","createdAt":"2024-04-08T19:26:38.000Z","metadata":{}}
-Message created:  {"id":"msg_o0VkXnQj3juOXXRCnlZ686ff","createdAt":"2024-04-08T19:26:38.000Z","threadId":"thread_KJuyrB7hynun4rvxWdfKLIqy","role":"user","content":[{"type":"text","text":{"value":"I need to solve the equation `3x + 11 = 14`. Can you help me?","annotations":[]},"imageFile":{}}],"assistantId":null,"runId":null,"fileIds":[],"metadata":{}}
-Created run
-Run created:  {"id":"run_P8CvlouB8V9ZWxYiiVdL0FND","object":"thread.run","status":"queued","model":"daisy","instructions":"You are a personal math tutor. Write and run JavaScript code to answer math questions.","tools":[{"type":"code_interpreter"}],"metadata":{},"usage":null,"assistantId":"asst_zXaZ5usTjdD0JGcNViJM2M6N","threadId":"thread_KJuyrB7hynun4rvxWdfKLIqy","fileIds":[],"createdAt":"2024-04-08T19:26:39.000Z","expiresAt":"2024-04-08T19:36:39.000Z","startedAt":null,"completedAt":null,"cancelledAt":null,"failedAt":null}
-Message content: "The solution to the equation \\(3x + 11 = 14\\) is \\(x = 1\\)."
-Message content: "Yes, of course! To solve the equation \\( 3x + 11 = 14 \\), we can follow these steps:\n\n1. Subtract 11 from both sides of the equation to isolate the term with x.\n2. Then, divide by 3 to find the value of x.\n\nLet me calculate that for you."
-Message content: "I need to solve the equation `3x + 11 = 14`. Can you help me?"
-```
-
-It's important to remember that while the code interpreter gives the model the capability to respond to more complex queries by converting the questions into code and running that code iteratively in JavaScript until it reaches a solution, you still need to validate the response to confirm that the model correctly translated your question into a valid representation in code.
-
-## Clean up resources
-
-If you want to clean up and remove an Azure OpenAI resource, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
-
-- [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
-- [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
-
-## Sample code
-
-* [Quickstart sample code](https://github.com/Azure-Samples/azure-typescript-e2e-apps/tree/main/quickstarts/azure-openai-assistants)
-
-## See also
-
-* Learn more about how to use Assistants with our [How-to guide on Assistants](../how-to/assistant.md).
-* [Azure OpenAI Assistants API samples](https://github.com/Azure-Samples/azureai-samples/tree/main/scenarios/Assistants)
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "TypeScriptを用いたAzure OpenAIのアシスタント作成に関するドキュメントの削除"
}
```

### Explanation
この変更は、Azure OpenAIをTypeScriptを使用してアシスタントを作成するためのクイックスタートガイドが完全に削除されたことを示しています。削除された内容は373行で、これにより開発者はJavaScript SDKを用いたアシスタントの作成手順を失います。

削除されたドキュメントには、Azureサブスクリプションの作成方法や、Node.jsのインストールに関する情報、必要な設定や構成手順が記載されていました。具体的には、アシスタントの作成、質問の送信、スレッドのランニングといった実用的なコード例が含まれており、これらは開発者がAzureでAIアシスタントを活用する際に必要不可欠な情報です。

このようなリソースの削除は、TypeScriptやJavaScriptに精通した開発者にとって大きな影響を及ぼす可能性があります。特に新規ユーザーや開発者にとっては、手順や具体例が不足するため、アシスタントの導入や実装において高い障壁が生じるでしょう。今後、同様の情報が新たに提供されることが期待されますが、現時点ではこの重要なリソースの欠如は大きな課題となっています。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -27,8 +27,6 @@ items:
       href: azure-government.md
 - name: Quickstarts
   items:
-    - name: Assistants (preview)
-      href: assistants-quickstart.md
     - name: Audio generation
       href: audio-completions-quickstart.md
     - name: Chat
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCからのアシスタント(プレビュー)の削除"
}
```

### Explanation
この変更は、Azure OpenAIに関する目次ファイル（`toc.yml`）の修正を示しています。この修正では、"Quickstarts"セクションから「アシスタント（プレビュー）」に関する項目が削除されました。これにより、ユーザーはこのセクションでアシスタントに関するクイックスタートガイドへのリンクをもはや参照することができなくなります。

変更内容は2行で、削除された部分は具体的に「アシスタント（プレビュー）」という名称の項目でした。この改訂によって、目次は他のクイックスタートガイドセクションと整合性が取れたものの、アシスタントのプレビューに関する情報は失われたため、ユーザーが関連情報にアクセスする際の利便性が低下します。

この変更は、目次を最新の状態に保つためのものであり、アシスタント機能の現在の状況や提供されるリソースに合わせた形での更新と考えられます。しかし、ユーザーにとっては新たな情報源を探す手間がかかる可能性があります。


