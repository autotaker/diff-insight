---
date: '2024-11-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c2df9dc...MicrosoftDocs:6c09135
summary: |-
  この報告では、Azure OpenAIサービスに関するドキュメントの重要な更新について説明しています。主な内容としては、`provisioned-throughput.md`および`overview.md`の情報がより具体的かつ実用的に改訂され、ユーザーがサービスを利用する上での理解を深めるのに役立つようにしています。特に、`provisioned-throughput.md`の更新により、トークン生成の性能やSLAの遅延基準が明確化され、ユーザーの期待をサポートしています。

  一方、`gpt-4-turbo.md`には、GPT-4 Turboのビジョン機能の退役に関する警告が追加され、ユーザーが将来的に機能が利用できなくなる可能性についての予測と準備を促しています。これにより、技術的なビジョン機能に依存するアプリケーションの開発者にとって重要な情報となります。

  さらに、`overview.md`の改訂では、特に新規ユーザーに対してAzure OpenAIサービスの利用開始手順が詳しく説明され、責任あるAIの重要性も強調されています。これらの変更は、全体としてAzure OpenAIサービスの使いやすさを向上させ、ユーザーが最新の情報をもとにサービスを効果的に利用できるようにすることを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c2df9dc...MicrosoftDocs:6c09135){target="_blank"}

# ハイライト

- **新機能**: `provisioned-throughput.md` および `overview.md` の情報を更新して、ユーザーがAzure OpenAIサービスの使用に関してより具体的かつ実用的な情報を得られるようにしました。
- **重大な変更**: `gpt-4-turbo.md` にGPT-4 Turboのビジョン機能の退役についての警告を追加し、ユーザーが将来のモデルアップグレードによる潜在的な影響を予測し準備できるようにしました。

## 新機能
- `provisioned-throughput.md` では、`gpt-4o` や `gpt-4o-mini` モデルのトークン生成に関する情報を明確化し、SLAの遅延目標値を追加。
- `overview.md` にAzure OpenAIサービスの開始方法と、責任あるAIに関する情報を強調するセクションが追加されました。

## 重大な変更
- `gpt-4-turbo.md` で、GPT-4 Turboのビジョン機能の退役に関する警告を追加。具体的には、OCR、オブジェクトのグラウンディング、ビデオプロンプトのビジョン強化機能が退役することを明記。

## その他の更新
- 値段: 更新情報の具体的な内容と行数の増減に関する情報が追加されました。

# インサイト

このコード変更は、Azure OpenAIサービスの様々なドキュメントを細かく更新することで、ユーザーに現状のサービス内容をより正確に伝えようとしています。特に、`provisioned-throughput.md`の更新は、サービス利用者がトークン生成の性能やSLAの遅延基準を理解し、期待されるパフォーマンスの評価に役立ちます。

一方で、`gpt-4-turbo.md`の更新は、非常に重要なもので、ユーザーが現在使用している機能が将来的に利用不可となる可能性を早めに通知し、計画的な移行の準備を促しています。このような退役に関する警告は、技術的なビジョン機能に依存しているアプリケーションの開発者にとって、将来のアップグレード計画において重要な情報となります。

また、`overview.md`の更新では、特に新規ユーザー向けにAzure OpenAIサービスの利用開始手順が詳述され、コンプライアンスおよび責任あるAIの重要性を強調しています。これはAI技術の倫理的な利用促進に寄与し、企業が安心してサービスを導入できるように意図されています。

全体として、これらの変更は、Azure OpenAIサービスの使い勝手を向上させ、ユーザーが最新の情報を基にサービスを最大限に活用できるようにするためのものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [provisioned-throughput.md](#item-022e0c) | minor update | プルーフ・オブ・スループットに関する情報の更新 | modified | 4 | 3 | 7 | 
| [gpt-4-turbo.md](#item-e233e0) | breaking change | GPT-4 Turboのビジョン機能の退役に関する警告 | modified | 3 | 0 | 3 | 
| [overview.md](#item-97d507) | minor update | Azure OpenAIサービスの概要の更新 | modified | 20 | 7 | 27 | 


# Modified Contents
## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -41,13 +41,14 @@ An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model.
 ## How much throughput per PTU you get for each model
 The amount of throughput (tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in the minute. Generating output tokens requires more processing than input tokens and so the more output tokens generated the lower your overall TPM. The service dynamically balances the input & output costs, so users do not have to set specific input and output limits. This approach means your deployment is resilient to fluctuations in the workload shape. 
 
-To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the `gpt-4o` and `gpt-4o-mini` models
+To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the `gpt-4o` and `gpt-4o-mini` models. The table also shows Service Level Agreement (SLA) Latency Target Values per model.  For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page].(https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
 
-|     | **gpt-4o**, **2024-05-13**   & **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | 
+|     | **gpt-4o**, **2024-05-13**   & **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
 | --- | --- | --- |
 | Deployable Increments | 50 | 25|
 | Input TPM per PTU | 2,500 | 37,000  |
-| Output TPM per PTU | 833  | 12,333 |
+| Output TPM per PTU| 833|12,333|
+| Latency Target Value |25 Tokens Per Second* |33 Tokens Per Second*|
 
 For a full list see the [AOAI Studio calculator](https://oai.azure.com/portal/calculator).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プルーフ・オブ・スループットに関する情報の更新"
}
```

### Explanation
このコードの変更は、「provisioned-throughput.md」ファイルの内容を更新しています。主な変更点は、`gpt-4o`および`gpt-4o-mini`モデルのトークン生成についての情報をより明確にしたことです。また、サービスレベルアグリーメント（SLA）の遅延目標値に関する情報も追加されました。この更新により、ユーザーがモデルのパフォーマンスや期待される遅延について理解しやすくなり、Azure OpenAIサービスの使用時に役立つ情報が提供されています。変更は合計で7行で、4行が追加され、3行が削除されています。

## articles/ai-services/openai/includes/gpt-4-turbo.md{#item-e233e0}

<details>
<summary>Diff</summary>
````diff
@@ -27,6 +27,9 @@ This is the replacement for the following preview models:
 
 - Azure AI specific Vision enhancements integration with GPT-4 Turbo with Vision isn't supported for `gpt-4` **Version:** `turbo-2024-04-09`. This includes Optical Character Recognition (OCR), object grounding, video prompts, and improved handling of your data with images.
 
+> [!IMPORTANT]
+> Vision enhancements preview features including Optical Character Recognition (OCR), object grounding, video prompts will be retired and no longer available once `gpt-4` Version: `vision-preview` is upgraded to `turbo-2024-04-09`. If you are currently relying on any of these preview features, this automatic model upgrade will be a breaking change.
+
 ### GPT-4 Turbo provisioned managed availability
 
 - `gpt-4` **Version:** `turbo-2024-04-09` is available for both standard and provisioned deployments. Currently the provisioned version of this model **doesn't support image/vision inference requests**. Provisioned deployments of this model only accept text input. Standard model deployments accept both text and image/vision inference requests.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "GPT-4 Turboのビジョン機能の退役に関する警告"
}
```

### Explanation
このコードの変更は、「gpt-4-turbo.md」ファイルにおいて、GPT-4 Turboのビジョン機能に関する重要な情報と警告を追加しています。変更された内容では、Optical Character Recognition (OCR)、オブジェクトのグラウンディング、ビデオプロンプトなどのビジョン強化のプレビュー機能が、`gpt-4`のバージョンが`turbo-2024-04-09`にアップグレードされると、退役し利用できなくなることが明記されています。この警告は、これらの機能に依存しているユーザーにとって重要であり、自動モデルアップグレードが壊滅的な変更を引き起こす可能性があることを示しています。変更は全体で3行で、追加のみが行われています。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -27,15 +27,28 @@ Azure OpenAI Service provides REST API access to OpenAI's powerful language mode
 | Managed Identity| Yes, via Microsoft Entra ID | 
 | UI experience | [Azure portal](https://portal.azure.com) for account & resource management, <br> [Azure AI Studio](https://ai.azure.com) for model exploration and fine-tuning |
 | Model regional availability | [Model availability](./concepts/models.md) |
-| Content filtering | Prompts and completions are evaluated against our content policy with automated systems. High severity content will be filtered. |
+| Content filtering | Prompts and completions are evaluated against our content policy with automated systems. High severity content is filtered. |
 
 ## Responsible AI
 
 At Microsoft, we're committed to the advancement of AI driven by principles that put people first. Generative models such as the ones available in Azure OpenAI have significant potential benefits, but without careful design and thoughtful mitigations, such models have the potential to generate incorrect or even harmful content. Microsoft has made significant investments to help guard against abuse and unintended harm, which includes incorporating Microsoft’s <a href="https://www.microsoft.com/ai/responsible-ai?activetab=pivot1:primaryr6" target="_blank">principles for responsible AI use</a>, adopting a [Code of Conduct](/legal/cognitive-services/openai/code-of-conduct?context=/azure/ai-services/openai/context/context) for use of the service, building [content filters](/azure/ai-services/content-safety/overview) to support customers, and providing responsible AI [information and guidance](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=image) that customers should consider when using Azure OpenAI.
 
-## How do I get access to Azure OpenAI?
+## Get started with Azure OpenAI Service
 
-A Limited Access registration form is not required to access most Azure OpenAI models. Learn more on the [Azure OpenAI Limited Access page](/legal/cognitive-services/openai/limited-access?context=/azure/ai-services/openai/context/context).
+To get started with Azure OpenAI Service, you need to create an Azure OpenAI Service resource in your Azure subscription. 
+
+Start with the [Create and deploy an Azure OpenAI Service resource](./how-to/create-resource.md) guide.
+1. You can create a resource via Azure portal, Azure CLI, or Azure PowerShell. 
+1. When you have an Azure OpenAI Service resource, you can deploy a model such as GPT-4o.
+1. When you have a deployed model, you can:
+
+    - Try out the Azure AI Studio playgrounds to explore the capabilities of the models. 
+    - You can also just start making API calls to the service using the REST API or SDKs.
+    
+    For example, you can try [real-time audio](./realtime-audio-quickstart.md) and [assistants](./assistants-quickstart.md) in the playgrounds or via code.
+
+> [!NOTE]
+> A Limited Access registration form is required to access some Azure OpenAI Service models or features. Learn more on the [Azure OpenAI Limited Access page](/legal/cognitive-services/openai/limited-access?context=/azure/ai-services/openai/context/context).
 
 ## Comparing Azure OpenAI and OpenAI
 
@@ -47,7 +60,7 @@ With Azure OpenAI, customers get the security capabilities of Microsoft Azure wh
 
 ### Prompts & completions
 
-The completions endpoint is the core component of the API service. This API provides access to the model's text-in, text-out interface. Users simply need to provide an input  **prompt** containing the English text command, and the model will generate a text **completion**.
+The completions endpoint is the core component of the API service. This API provides access to the model's text-in, text-out interface. Users simply need to provide an input  **prompt** containing the English text command, and the model generates a text **completion**.
 
 Here's an example of a simple prompt and completion:
 
@@ -70,7 +83,7 @@ Here's an example of a simple prompt and completion:
 
 Azure OpenAI processes text by breaking it down into tokens. Tokens can be words or just chunks of characters. For example, the word “hamburger” gets broken up into the tokens “ham”, “bur” and “ger”, while a short and common word like “pear” is a single token. Many tokens start with a whitespace, for example “ hello” and “ bye”.
 
-The total number of tokens processed in a given request depends on the length of your input, output and request parameters. The quantity of tokens being processed will also affect your response latency and throughput for the models.
+The total number of tokens processed in a given request depends on the length of your input, output, and request parameters. The quantity of tokens being processed will also affect your response latency and throughput for the models.
  
 #### Image tokens
 
@@ -106,9 +119,9 @@ Once you create an Azure OpenAI Resource, you must deploy a model before you can
 
 ### Prompt engineering
 
-The GPT-3, GPT-3.5 and GPT-4 models from OpenAI are prompt-based. With prompt-based models, the user interacts with the model by entering a text prompt, to which the model responds with a text completion. This completion is the model’s continuation of the input text.
+The GPT-3, GPT-3.5, and GPT-4 models from OpenAI are prompt-based. With prompt-based models, the user interacts with the model by entering a text prompt, to which the model responds with a text completion. This completion is the model’s continuation of the input text.
 
-While these models are extremely powerful, their behavior is also very sensitive to the prompt. This makes [prompt engineering](./concepts/prompt-engineering.md) an important skill to develop.
+While these models are powerful, their behavior is also sensitive to the prompt. This makes [prompt engineering](./concepts/prompt-engineering.md) an important skill to develop.
 
 Prompt construction can be difficult. In practice, the prompt acts to configure the model weights to complete the desired task, but it's more of an art than a science, often requiring experience and intuition to craft a successful prompt.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスの概要の更新"
}
```

### Explanation
このコードの変更は、「overview.md」ファイルにおけるAzure OpenAIサービスに関する情報の更新を含んでいます。主な変更点としては、Azure OpenAIサービスの開始方法に関するセクションが追加され、ユーザーがサービスリソースを作成する手順が明確に示されています。また、各種機能やモデルの利用方法、特にコンプライアンスや責任あるAIに関する情報が強調されています。内容の整理や表現の改善が行われ、ユーザーがAzure OpenAIサービスを理解しやすくするための情報が充実しています。全体で27行の変更があり、20行が追加され、7行が削除されています。


