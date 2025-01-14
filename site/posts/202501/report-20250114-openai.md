---
date: '2025-01-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:70337bc...MicrosoftDocs:de17d62
summary: このコード差分では、「Azure OpenAI Studio」から「Azure AI Foundry」への名称変更が行われています。新しい名称がドキュメント内に反映され、正確な情報を提供することを目的としています。機能的な変更はなく、ドキュメントの正確性を向上させるためのマイナーアップデートです。主な変更点は、名称の変更とそれに伴う関連ドキュメントの更新です。この更新により、ユーザーは新しい名称を使用してサービスにアクセスできるようになります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:70337bc...MicrosoftDocs:de17d62){target="_blank"}

# ハイライト
このコード差分では、「Azure OpenAI Studio」から「Azure AI Foundry」への名称変更が行われています。新しい名称がドキュメント内のタイトルや説明に反映され、ユーザーに正確な情報を伝えることが目的です。機能的な変更はなく、ドキュメントの正確性向上を目的とするマイナーアップデートです。

## 新しい機能
- なし

## 重大な変更
- なし

## その他の更新
- 「Azure OpenAI Studio」の名称を「Azure AI Foundry」に変更
- 関連するドキュメントの更新：説明や例を新しい名称に基づいて修正

# 洞察
このコード差分は、Azureプラットフォーム内のサービス名称が改定されたことを反映しています。「Azure OpenAI Studio」という以前の名称が「Azure AI Foundry」に変更され、それに伴ってドキュメントが更新されています。これにより、ユーザーは新しいサービス名称を使用し、サービス機能や利用方法について混乱なくアクセスできるようになります。

名称変更は通常、ブランドイメージの統一や新しいサービス展開に伴うものであり、今回のケースでもその可能性があります。ドキュメントの更新は、ユーザーが新しい名称を理解し正確な情報をもとにサービスを利用できるようにするために重要なステップです。このような名称変更に伴うドキュメントの更新は、ユーザーエクスペリエンスを向上させ、混乱を防ぐための必要不可欠なプロセスとなっています。文書だけでなく、UIや別のシステムでも同様の更新が行われている可能性があるため、ユーザーは変更を総合的に理解することが推奨されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [chatgpt-studio.md](#item-ab43f3) | minor update | Azure OpenAI StudioからAzure AI Foundryへの名称変更 | modified | 6 | 8 | 14 | 
| [studio.md](#item-eeeaff) | minor update | Azure OpenAI StudioからAzure AI Foundryへの名称変更 | modified | 8 | 12 | 20 | 


# Modified Contents
## articles/ai-services/openai/includes/chatgpt-studio.md{#item-ab43f3}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: 'Quickstart: Use GPT-4o and GPT-4o mini via the Azure OpenAI Studio'
+title: 'Quickstart: Use GPT-4o and GPT-4o mini via Azure AI Foundry'
 titleSuffix: Azure OpenAI Service
-description: Walkthrough on how to get started with Azure OpenAI and make your first completions call with Azure OpenAI Studio. 
+description: Walkthrough on how to get started with Azure OpenAI and make your first completions call with Azure AI Foundry. 
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
@@ -14,17 +14,15 @@ ms.date: 09/19/2024
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
 - An Azure OpenAI Service resource with either `gpt-4o` or the `gpt-4o-mini` models deployed. We recommend using standard or global standard model [deployment types](../how-to/deployment-types.md) for initial exploration. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 
-## Go to Azure OpenAI Studio
+## Go to Azure AI Foundry
 
-Navigate to Azure OpenAI Studio at [https://oai.azure.com/](https://oai.azure.com/) and sign-in with credentials that have access to your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
+Navigate to [Azure AI Foundry](https://oai.azure.com/) and sign-in with credentials that have access to your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
 
-From the Azure OpenAI Studio landing page, select **Chat playground**.
-
-:::image type="content" source="../media/quickstarts/chatgpt-playground-new.png" alt-text="Screenshot of the Azure OpenAI Studio landing page with Chat playground highlighted." lightbox="../media/quickstarts/chatgpt-playground-new.png":::
+From Azure AI Foundry, select **Chat playground**.
 
 ## Playground
 
-Start exploring Azure OpenAI Service capabilities with a no-code approach through the Azure OpenAI Studio Chat playground. From this page, you can quickly iterate and experiment with the capabilities.
+Start exploring Azure OpenAI Service capabilities with a no-code approach through the Azure AI Foundry Chat playground. From this page, you can quickly iterate and experiment with the capabilities.
 
 :::image type="content" source="../media/quickstarts/chatgpt-playground-load-new.png" alt-text="Screenshot of the Chat playground page." lightbox="../media/quickstarts/chatgpt-playground-load-new.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI StudioからAzure AI Foundryへの名称変更"
}
```

### Explanation
このコードの変更は、Azure OpenAI Studioに関するドキュメントの一部であり、タイトルや説明などの用語が「Azure OpenAI Studio」から「Azure AI Foundry」に更新されています。具体的には、ファイル内のテキストが6行追加され、8行削除されています。この変更は、ユーザーに新しい名称での利用方法を適切に伝えることを目的としています。例えば、サインイン手順の指示やリソースへのアクセスに関する記述が修正されています。この修正は機能的な変更ではなく、文書の正確性を高めるためのマイナーな更新です。

## articles/ai-services/openai/includes/studio.md{#item-eeeaff}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: 'Quickstart: Use Azure OpenAI Service via the Azure OpenAI Studio'
+title: 'Quickstart: Use Azure OpenAI Service via Azure AI Foundry'
 titleSuffix: Azure OpenAI
-description: Walkthrough on how to get started with Azure OpenAI and make your first completions call with Azure OpenAI Studio. 
+description: Walkthrough on how to get started with Azure OpenAI and make your first completions call with Azure AI Foundry. 
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
@@ -13,19 +13,15 @@ ms.date: 09/19/2023
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
 - An Azure OpenAI resource with a model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 
-## Go to the Azure OpenAI Studio
+## Go to the Azure AI Foundry
 
-Navigate to Azure OpenAI Studio at <a href="https://oai.azure.com/" target="_blank">https://oai.azure.com/</a> and sign-in with credentials that have access to your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
-
-From the Azure OpenAI Studio landing page navigate further to explore examples for prompt completion, manage your deployments and models, and find learning resources such as documentation and community forums. 
-
-:::image type="content" source="../media/quickstarts/studio-start-new.png" alt-text="Screenshot of the Azure OpenAI Studio landing page." lightbox="../media/quickstarts/studio-start-new.png":::
+Navigate to <a href="https://oai.azure.com/" target="_blank">Azure AI Foundry</a> and sign-in with credentials that have access to your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
 
 ## Playground
 
-Start exploring Azure OpenAI capabilities with a no-code approach through the GPT-3 Playground. It's simply a text box where you can submit a prompt to generate a completion. From this page, you can quickly iterate and experiment with the capabilities. 
+Start exploring Azure OpenAI capabilities with a no-code approach through the completions playground. It's simply a text box where you can submit a prompt to generate a completion. From this page, you can quickly iterate and experiment with the capabilities. 
 
-:::image type="content" source="../media/quickstarts/playground-load-new.png" alt-text="Screenshot of the playground page of the Azure OpenAI Studio with sections highlighted." lightbox="../media/quickstarts/playground-load-new.png":::
+:::image type="content" source="../media/quickstarts/playground-load-new.png" alt-text="Screenshot of the playground page of AI Foundry playground with sections highlighted." lightbox="../media/quickstarts/playground-load-new.png":::
 
 You can select a deployment and choose from a few pre-loaded examples to get started. If your resource doesn't have a deployment, select **Create a deployment** and follow the instructions provided by the wizard. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 
@@ -43,13 +39,13 @@ In the Completions playground you can also view Python and curl code samples pre
 
 To use the Azure OpenAI for text summarization in the Completions playground, follow these steps:
 
-1. Sign in to [Azure OpenAI Studio](https://oai.azure.com).
+1. Sign in to [Azure AI Foundry](https://oai.azure.com).
 1. Select the subscription and OpenAI resource to work with. 
 1. Select **Completions playground** on the landing page.
 1. Select your deployment from the **Deployments** dropdown. If your resource doesn't have a deployment, select **Create a deployment** and then revisit this step.
 1. Enter a prompt for the model.
 
-    :::image type="content" source="../media/quickstarts/summarize-text-new.png" alt-text="Screenshot of the playground page of the Azure OpenAI Studio with a text summarization example." lightbox="../media/quickstarts/summarize-text-new.png":::
+    :::image type="content" source="../media/quickstarts/summarize-text-new.png" alt-text="Screenshot of the playground page of Azure AI Foundry with a text summarization example." lightbox="../media/quickstarts/summarize-text-new.png":::
 
 1. Select `Generate`. Azure OpenAI will attempt to capture the context of text and rephrase it succinctly. You should get a result that resembles the following text:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI StudioからAzure AI Foundryへの名称変更"
}
```

### Explanation
このコードの変更は、Azure OpenAI Studioに関連するドキュメントのアップデートであり、タイトルや説明における「Azure OpenAI Studio」の表記が「Azure AI Foundry」に変更されています。具体的には、8行が追加され、12行が削除されており、全体で20行が修正されています。この変更は、ユーザーが新しい名称を理解し、正しいリソースへアクセスできるようにするためのものです。具体的には、サインインの指示や、さまざまな機能を探索する方法に関する説明が修正されており、実際の操作手順も更新されています。これにより、ユーザーは新しいサイト名のもとでの操作を円滑に行えるようになります。この修正は、機能的な変更を伴わない、文書の精度を向上させるためのマイナーな更新です。


