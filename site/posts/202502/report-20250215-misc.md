---
date: '2025-02-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f2b9798...MicrosoftDocs:b07793e
summary: この修正では、Azureドキュメントに関するさまざまな変更が行われました。特に注目すべきは、AIサービス関連の新しいドキュメントの追加と、いくつかの文書の翻訳やリンクの整備です。また、マルチモーダルビジョンのクイックスタートガイドが完全に削除されたことも重要な変更点です。これにより、AIサービスがよりユーザーに優しく、直感的になることを目指しています。全体として、AzureはAIサービスの提供を進化させ、ユーザーエクスペリエンスを向上させるための努力を続けています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f2b9798...MicrosoftDocs:b07793e){target="_blank"}

# ハイライト

このdiffでは、Azureドキュメントに関する画像やドキュメントの小規模な修正から、新しい機能に至るまで、様々な変更が行われました。特に注目すべきは、AIサービス関連の新しいドキュメントの追加と、いくつかの文書の翻訳やリンクの整備です。また、重要な変更点として、マルチモーダルビジョンのクイックスタートガイドが完全に削除されています。

## 新しい機能
- AIサービスに関する新しいドキュメント「what-are-ai-services.md」の追加。Azureが提供するAIサービスの概要や利用方法について説明されています。

## 破壊的変更
- マルチモーダルビジョンに関するクイックスタートガイドが削除され、当該機能や情報が別途提供されている可能性があります。

## その他の更新
- `overview-custom.jpg`の画像修正。（実質的な変更はない）
- リダイレクション設定ファイルに15行の追加。
- ドキュメントやリンクテキストの文言修正が数件。
- AIスタジオの目次ファイルの大幅な更新と再構成。

# 洞察

このdiffから得られる最も重要な洞察は、AzureのAI関連ドキュメントがよりユーザーに優しく、直感的になるように整備されていることです。特に、AIサービスに関する新たなドキュメントの追加は、AIソリューションを構築したいユーザーにとって非常に有用なリソースであり、サービスの理解を助けるものです。また、目次の大幅な更新や文言の修正は、ユーザーが必要な情報に迅速にアクセスできるよう、ナビゲーションを容易にすることを目的としています。

一方で、マルチモーダルビジョンのクイックスタートガイドが削除されたことは、何らかの方針変更や提供方法の見直しを示唆しています。これに関しては、別の場所で情報が得られるよう手配される可能性があり、注意深く状況を確認する必要があります。

これらの変更は、AzureがAIサービスの提供を進化させ、ユーザーエクスペリエンスを向上させるための継続的な努力の一環と言えます。特にドキュメントの質を向上させ、整合性を高めることに注力しており、ユーザーがより効果的にAzureのAIサービスを活用できるようにサポートしています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [overview-custom.jpg](#item-a164e7) | minor update | 画像ファイルの修正 | modified | 0 | 0 | 0 | 
| [.openpublishing.redirection.ai-studio.json](#item-c75c21) | minor update | リダイレクション設定の追加 | modified | 15 | 0 | 15 | 
| [connect-azure-openai.md](#item-46b8a6) | minor update | ドキュメント内の文言修正 | modified | 1 | 1 | 2 | 
| [ai-resources.md](#item-14adb9) | minor update | リンクテキストの修正 | modified | 1 | 1 | 2 | 
| [what-are-ai-services.md](#item-addaca) | new feature | AIサービスに関する新しいドキュメントの追加 | added | 36 | 0 | 36 | 
| [index.yml](#item-68b5b4) | minor update | AIスタジオのインデックスファイルの更新 | modified | 23 | 30 | 53 | 
| [multimodal-vision.md](#item-740e84) | breaking change | マルチモーダルビジョンに関するクイックスタートガイドの削除 | removed | 0 | 167 | 167 | 
| [toc.yml](#item-2745cd) | minor update | Azure AI Studio の目次ファイルの更新 | modified | 322 | 220 | 542 | 


# Modified Contents
## articles/ai-services/document-intelligence/media/overview-custom.jpg{#item-a164e7}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの修正"
}
```

### Explanation
この修正は、`overview-custom.jpg`という画像ファイルに関するもので、ファイルの中身や変更はないものの、ファイルが修正されたことを示しています。追加、削除、または変更は行われていないため、これはマイナーアップデートと見なされます。ファイルのURLは以下の通りです：[GitHub上の画像ファイル](https://github.com/MicrosoftDocs/azure-ai-docs/blob/b07793e742363ee5bdb8f64774c24fc8a5555086/articles%2Fai-services%2Fdocument-intelligence%2Fmedia%2Foverview-custom.jpg)。この変更は、ドキュメントの整合性や表示に寄与する可能性があります。

## articles/ai-studio/.openpublishing.redirection.ai-studio.json{#item-c75c21}

<details>
<summary>Diff</summary>
````diff
@@ -245,6 +245,11 @@
               "redirect_url": "/azure/ai-studio/quickstarts/multimodal-vision",
               "redirect_document_id": false
           },
+          {
+            "source_path_from_root": "/articles/ai-studio/quickstarts/multimodal-vision.md",
+            "redirect_url": "/azure/ai-services/openai/gpt-v-quickstart",
+            "redirect_document_id": false
+          },
           {
             "source_path_from_root": "/articles/ai-studio/reference/reference-model-inference-api.md",
             "redirect_url": "/azure/ai-foundry/model-inference/reference/reference-model-inference-api",
@@ -269,6 +274,16 @@
             "source_path_from_root": "/articles/ai-studio/reference/reference-model-inference-images-embeddings.md",
             "redirect_url": "/azure/ai-foundry/model-inference/reference/reference-model-inference-images-embeddings",
             "redirect_document_id": false
+          },
+          {
+            "source_path_from_root": "/articles/ai-studio/concepts/about-capabilities.md",
+            "redirect_url": "/azure/ai-studio/concepts/what-are-ai-services",
+            "redirect_document_id": false
+          },
+          {
+            "source_path_from_root": "/articles/ai-studio/concepts/related-content.md",
+            "redirect_url": "/azure/ai-studio/concepts/what-are-ai-services",
+            "redirect_document_id": false
           }
     ]
 }
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リダイレクション設定の追加"
}
```

### Explanation
今回の修正では、`articles/ai-studio/.openpublishing.redirection.ai-studio.json`ファイルに、15行の追加が行われましたが、削除はありません。具体的には、AIスタジオに関連するリダイレクションルールが複数追加されています。新しいリダイレクション設定により、特定の文書から別のページへシームレスに移動できるようになります。これにより、ユーザーが必要な情報に容易にアクセスできるよう配慮されています。変更後のファイルは以下のリンクから確認できます：[GitHub上のリダイレクション設定ファイル](https://github.com/MicrosoftDocs/azure-ai-docs/blob/b07793e742363ee5bdb8f64774c24fc8a5555086/articles%2Fai-studio%2F.openpublishing.redirection.ai-studio.json)。

## articles/ai-studio/ai-services/how-to/connect-azure-openai.md{#item-46b8a6}

<details>
<summary>Diff</summary>
````diff
@@ -100,7 +100,7 @@ Here are a few guides to help you get started with Azure OpenAI Service playgrou
 - [Quickstart: Use the chat playground](../../quickstarts/get-started-playground.md)
 - [Quickstart: Get started using Azure OpenAI Assistants](../../../ai-services/openai/assistants-quickstart.md?context=/azure/ai-studio/context/context)
 - [Quickstart: Use GPT-4o in the real-time audio playground](../../../ai-services/openai/realtime-audio-quickstart.md?context=/azure/ai-studio/context/context)
-- [Quickstart: Analyze images and video with GPT-4 for Vision in the playground](../../quickstarts/multimodal-vision.md)
+- [Quickstart: Analyze images and video in the chat playground](../../quickstarts/multimodal-vision.md)
 
 Each playground has different model requirements and capabilities. The supported regions vary depending on the model. For more information about model availability per region, see the [Azure OpenAI Service models documentation](../../../ai-services/openai/concepts/models.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメント内の文言修正"
}
```

### Explanation
この修正は、`articles/ai-studio/ai-services/how-to/connect-azure-openai.md`というドキュメントに対するもので、1行の追加と1行の削除が行われました。具体的には、Azure OpenAI Serviceのプレイグラウンドに関するガイドのリスト内の文言が変更されました。元の文は「GPT-4 for Vision in the playground」となっていましたが、新しい文では「チャットプレイグラウンドで画像と動画を分析する」という形に改訂されています。この変更は、利用者がより明確な情報を得られるようにするためのものであり、文書の可読性向上に寄与しています。変更されたファイルは以下のリンクから確認できます：[GitHub上のドキュメント](https://github.com/MicrosoftDocs/azure-ai-docs/blob/b07793e742363ee5bdb8f64774c24fc8a5555086/articles%2Fai-studio%2Fai-services%2Fhow-to%2Fconnect-azure-openai.md)。

## articles/ai-studio/concepts/ai-resources.md{#item-14adb9}

<details>
<summary>Diff</summary>
````diff
@@ -128,6 +128,6 @@ In the Azure portal, you can find resources that correspond to your project in A
 
 ## Next steps
 
-- [Quickstart: Analyze images and video with GPT-4 for Vision in the playground](../quickstarts/multimodal-vision.md)
+- [Quickstart: Analyze images and video in the chat playground](../quickstarts/multimodal-vision.md)
 - [Learn more about Azure AI Foundry](../what-is-ai-studio.md)
 - [Learn more about projects](../how-to/create-projects.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクテキストの修正"
}
```

### Explanation
この修正は、`articles/ai-studio/concepts/ai-resources.md`ファイルにおいて行われ、1行の追加と1行の削除がありました。具体的には、Azureポータルでのリソースの対応に関するセクションの「次のステップ」において、Quickstartリンクの文言が変更されています。元のリンクテキストは「GPT-4 for Vision in the playground」であったのに対し、新たに「チャットプレイグラウンドで画像と動画を分析する」という文言に変更されました。この更新は、利用者がリンク先の内容をより正確に理解できるようにすることを目的としています。また、変更されたファイルは以下のリンクから確認できます：[GitHub上のドキュメント](https://github.com/MicrosoftDocs/azure-ai-docs/blob/b07793e742363ee5bdb8f64774c24fc8a5555086/articles%2Fai-studio%2Fconcepts%2Fai-resources.md)。

## articles/ai-studio/concepts/what-are-ai-services.md{#item-addaca}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,36 @@
+---
+title: What are AI services?
+description: Learn about the various Azure AI services and their capabilities that you can use in Azure AI Foundry.
+author: sdgilley
+ms.author: sgilley
+ms.service: azure-ai-studio
+ms.topic: concept-article  
+ms.date: 1/30/2025
+
+#CustomerIntent: I want to understand what AI services are and how they can help me build AI solutions.
+---
+
+# What are AI services?
+
+[Azure AI Foundry](../what-is-ai-studio.md) is a comprehensive platform for AI development that provides a wide range of tools and services to help you build AI solutions. You can explore the [model catalog](../how-to/model-catalog-overview.md) to find the right model for your use case. 
+
+[Azure AI services](../../ai-services/what-are-ai-services.md) are a collection of task and general purpose models in Azure AI Foundry. These services are designed to help you build AI solutions quickly and easily, without needing to build and train your own models from scratch. In some cases, you can customize these models to better fit your specific needs. 
+
+> [!TIP]
+> While some articles from each service are available in the [Azure AI Foundry documentation](../ai-services/how-to/connect-ai-services.md), explore each service in more depth in their individual service documentation.
+
+| Service | Description |
+| --- | --- |
+| ![Azure OpenAI Service icon](~/reusable-content/ce-skilling/azure/media/ai-services/azure-openai.svg) [Azure OpenAI](../../ai-services/openai/index.yml) | Perform a wide variety of natural language tasks. |
+| ![Content Safety icon](~/reusable-content/ce-skilling/azure/media/ai-services/content-safety.svg) [Content Safety](../../ai-services/content-safety/index.yml) | An AI service that detects unwanted contents. |
+| ![Content Understanding icon](~/reusable-content/ce-skilling/azure/media/ai-services/content-understanding.svg) [Content Understanding](../../ai-services/content-understanding/index.yml) | Analyze various media content—such as audio, video, text, and images— and transform it into structured, organized, and searchable data for your applications. |
+| ![Document Intelligence icon](~/reusable-content/ce-skilling/azure/media/ai-services/document-intelligence.svg) [Document Intelligence](../../ai-services/document-intelligence/index.yml) | Turn documents into intelligent data-driven solutions. |
+| ![Language icon](~/reusable-content/ce-skilling/azure/media/ai-services/language.svg) [Language](../../ai-services/language-service/index.yml) | Build apps with industry-leading natural language understanding capabilities. |
+| ![Speech icon](~/reusable-content/ce-skilling/azure/media/ai-services/speech.svg) [Speech](../../ai-services/speech-service/index.yml) | Speech to text, text to speech, translation, and speaker recognition. |
+| ![Translator icon](~/reusable-content/ce-skilling/azure/media/ai-services/translator.svg) [Translator](../../ai-services/translator/index.yml) | Use AI-powered translation technology to translate more than 100 in-use, at-risk, and endangered languages and dialects. |
+| ![Vision icon](~/reusable-content/ce-skilling/azure/media/ai-services/vision.svg) [Vision](../../ai-services/computer-vision/index.yml) | Analyze content in images and videos. | 
+
+## Related content
+
+- [Use Azure OpenAI Service in Azure AI Foundry portal](../ai-services/how-to/connect-azure-openai.md)
+- [Use Azure AI services in Azure AI Foundry portal](../ai-services/how-to/connect-ai-services.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "AIサービスに関する新しいドキュメントの追加"
}
```

### Explanation
この変更は、`articles/ai-studio/concepts/what-are-ai-services.md`という新しいファイルが追加されたことを示しています。このドキュメントは、Azure AI Foundry内で利用できるさまざまなAIサービスおよびその機能についての情報を提供しています。具体的には、AIサービスの概念を理解し、AIソリューションを迅速に構築するためのツールとサービスがどのように役立つかを説明しています。

新たに追加された内容には、Azure OpenAI、コンテンツ安全性、コンテンツ理解、ドキュメントインテリジェンス、言語処理、音声、翻訳、コンピュータビジョンなど、複数のAIサービスの説明が含まれています。さらに、利用者が各サービスの詳細なドキュメントを探索できるよう、関連するリンクも含まれています。

この文書の目的は、ユーザーがAIサービスを理解し、それを利用してAIソリューションを構築する手助けをすることです。変更されたファイルは以下のリンクから確認できます：[GitHub上のドキュメント](https://github.com/MicrosoftDocs/azure-ai-docs/blob/b07793e742363ee5bdb8f64774c24fc8a5555086/articles%2Fai-studio%2Fconcepts%2Fwhat-are-ai-services.md)。

## articles/ai-studio/index.yml{#item-68b5b4}

<details>
<summary>Diff</summary>
````diff
@@ -11,6 +11,7 @@ metadata:
     - copilot-learning-hub
     - ignite-2024
   ms.topic: landing-page
+  manager: scottpolly
   ms.reviewer: sgilley
   ms.author: sgilley
   author: sdgilley
@@ -29,42 +30,38 @@ landingContent:
             url: what-is-ai-studio.md
           - text: Azure OpenAI Service in Azure AI Foundry
             url: azure-openai-in-ai-studio.md
-          - text: Select and deploy models from the catalog
-            url: how-to/model-catalog.md
           - text: Retrieval Augmented Generation (RAG)
             url: concepts/retrieval-augmented-generation.md
           - text: Evaluation and monitoring metrics for generative AI
             url: concepts/evaluation-metrics-built-in.md
-      - linkListType: how-to-guide
-        links:
-          - text: Create a project in Azure AI Foundry portal
-            url: how-to/create-projects.md
-          - text: Get started with prompt flow
-            url: how-to/flow-develop.md
-          - text: Connect to AI services
-            url: ai-services/how-to/connect-ai-services.md
+          - text: Model deployment options
+            url: concepts/deployments-overview.md
+
   # Card
-  - title: 10-minute quickstarts
-    linkLists:
+  - title: Get started
+    linkLists:   
       - linkListType: quickstart
         links:
+          - text: Build a chap app in the playground
+            url: quickstarts/get-started-playground.md
           - text: Build a chat app using the Azure AI SDK
             url: quickstarts/get-started-code.md
-          - text: Use Azure OpenAI Assistants in the playground
-            url: ../ai-services/openai/assistants-quickstart.md?context=/azure/ai-studio/context/context
-          - text: Get started using GPT-4 Turbo with Vision
-            url: quickstarts/multimodal-vision.md
-      - linkListType: tutorial
-        links:
-          - text: Deploy an enterprise chat web app
-            url: tutorials/deploy-chat-web-app.md
 
+      - linkListType: how-to-guide
+        links:
+          - text: Select and deploy models from the catalog
+            url: how-to/model-catalog.md
+          - text: Compare benchmarks across models and datasets
+            url: how-to/benchmark-model-in-catalog.md
+          - text: What is Azure AI Agent service?
+            url: ../ai-services/agents/overview.md?context=/azure/ai-studio/context/context
+      
   # Card
-  - title: Develop apps
+  - title: Azure AI Foundry SDK
     linkLists:
       - linkListType: how-to-guide
         links:
-          - text: Get started with the Azure AI SDKs
+          - text: Get started with the Azure AI Foundry SDKs
             url: how-to/develop/sdk-overview.md
           - text: Work with Azure AI Foundry projects in VS Code
             url: how-to/develop/vscode.md
@@ -73,13 +70,9 @@ landingContent:
         links:
           - text: Build a custom chat app with the Azure AI SDK
             url: tutorials/copilot-sdk-create-resources.md
-
-      - linkListType: concept
-        links:
-          - text: Connections for flows and indexing
-            url: concepts/connections.md
-          - text: Deploy models, flows, and web apps
-            url: concepts/deployments-overview.md
+          - text: Deploy an enterprise chat web app
+            url: tutorials/deploy-chat-web-app.md
+            
       - linkListType: reference
         links:
           - text: Azure AI Foundry SDK
@@ -101,4 +94,4 @@ landingContent:
           - text: Azure Machine Learning
             url: /azure/machine-learning/
           - text: Semantic Kernel
-            url: /semantic-kernel/
+            url: /semantic-kernel/
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIスタジオのインデックスファイルの更新"
}
```

### Explanation
この変更は、`articles/ai-studio/index.yml`ファイルの更新を示しており、23行が追加され、30行が削除されています。主な目的は、Azure AI Foundryに関する情報を構造化し、ユーザーがリソースやガイドにアクセスしやすくすることです。

変更内容の要点は以下の通りです：
- メタデータに「manager: scottpolly」が追加され、コンテンツの管理者が明示されました。
- 一部のリンクが更新され、新しいリファレンスやチュートリアルが追加されています。特に、モデルのデプロイ方法やベンチマークの比較に関する情報が強化されました。
- リンクリストのセクションが整理され、関連するガイドやチュートリアルリンクが見やすく配置されています。
- ドキュメントのタイトルが「Develop apps」から「Azure AI Foundry SDK」に変更され、より具体的な内容になっています。

これにより、ユーザーはAzure AIスタジオの機能に関する情報をより迅速かつ効率的に見つけることができるようになります。変更されたファイルは以下のリンクから確認できます：[GitHub上のドキュメント](https://github.com/MicrosoftDocs/azure-ai-docs/blob/b07793e742363ee5bdb8f64774c24fc8a5555086/articles%2Fai-studio%2Findex.yml)。

## articles/ai-studio/quickstarts/multimodal-vision.md{#item-740e84}

<details>
<summary>Diff</summary>
````diff
@@ -1,167 +0,0 @@
----
-title: Get started vision-enabled chats in Azure AI Foundry portal
-titleSuffix: Azure AI Foundry
-description: Get started using vision-enabled chats in Azure AI Foundry portal.
-manager: nitinme
-ms.service: azure-ai-foundry
-ms.custom:
-  - build-2024
-ms.topic: quickstart
-ms.date: 01/10/2025
-ms.reviewer: eur
-ms.author: pafarley
-author: PatrickFarley
----
-
-# Quickstart: Get started using vision-enabled chats in Azure AI Foundry portal
-
-[!INCLUDE [feature-preview](../includes/feature-preview.md)]
-
-Use this article to get started using [Azure AI Foundry](https://ai.azure.com) to deploy and test a chat completion model with image understanding. 
-
-<!--
-GPT-4 Turbo with Vision and [Azure AI Vision](../../ai-services/computer-vision/overview.md) offer advanced functionality including:
-
-- Optical Character Recognition (OCR): Extracts text from images and combines it with the user's prompt and image to expand the context. 
-- Object grounding: Complements the GPT-4 Turbo with Vision text response with object grounding and outlines salient objects in the input images.
-- Video prompts: GPT-4 Turbo with Vision can answer questions by retrieving the video frames most relevant to the user's prompt.
--->
-
-Extra usage fees might apply when using chat completion models with vision functionality.
-
-## Prerequisites
-
-- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
-- Once you have your Azure subscription, <a href="/azure/ai-services/openai/how-to/create-resource?pivots=web-portal"  title="Create an Azure OpenAI resource."  target="_blank">create an Azure OpenAI resource </a>.
-- An [Azure AI Foundry hub](../how-to/create-azure-ai-resource.md) with your Azure OpenAI resource added as a connection. 
-
-## Prepare your media
-
-You need an image to complete this quickstart. You can use this sample image or any other image you have available.
-
-:::image type="content" source="../media/quickstarts/multimodal-vision/car-accident.png" alt-text="Photo of a car accident that can be used to complete the quickstart." lightbox="../media/quickstarts/multimodal-vision/car-accident.png":::
-
-## Deploy a vision-enabled chat model
-
-1. Sign in to [Azure AI Foundry](https://ai.azure.com) and select the hub you'd like to work in.
-1. On the left nav menu, select **Models + endpoints** and select **+ Deploy model**.
-1. On the model selection page, select a vision-enabled model like GPT-4o. In the window that appears, select a name and deployment type. Make sure your Azure OpenAI resource is connected.
-1. Select **Deploy**.
-1. Next, select your new model and select **Open in playground**. In the chat playground, the deployment you created should be selected in the **Deployment** dropdown.
-    
-<!-- # [Image prompts](#tab/image-chat) -->
-
-## Image prompts
-
-In this chat session, you instruct the assistant to aid you in understanding images that you input.
-
-1. In the context text box on the **Setup** panel, provide this prompt to guide the assistant: `"You're an AI assistant that helps people find information."` Or, you can tailor the prompt to your image or scenario.
-1. Select **Apply changes** to save your changes. 
-1. In the chat session pane, select the attachment button and then **Upload image**. Choose your image.
-1. Add the following prompt in the chat field: `"Describe this image"`, and then select the send icon to submit it.
-1. The send icon is replaced by a stop button. If you select it, the assistant stops processing your request. For this quickstart, let the assistant finish its reply.
-1. The assistant replies with a description of the image.
-    <!--:::image type="content" source="../media/quickstarts/multimodal-vision/chat-car-accident-reply-license.png" alt-text="Screenshot of the chat playground with the assistant's reply for basic image analysis." lightbox="../media/quickstarts/multimodal-vision/chat-car-accident-reply-license.png":::-->
-1. Ask a follow-up question related to the analysis of your image. You could enter, `"What should I highlight about this image to my insurance company?"`.
-1. You should receive a relevant response similar to what's shown here:
-    ```
-    When reporting the incident to your insurance company, you should highlight the following key points from the image:  
-       
-    1. **Location of Damage**: Clearly state that the front end of the car, particularly the driver's side, is damaged. Mention the crumpled hood, broken front bumper, and the damaged left headlight.  
-       
-    2. **Point of Impact**: Indicate that the car has collided with a guardrail, which may suggest that no other vehicles were involved in the accident.  
-       
-    3. **Condition of the Car**: Note that the damage seems to be concentrated on the front end, and there is no visible damage to the windshield or rear of the car from this perspective.  
-       
-    4. **License Plate Visibility**: Mention that the license plate is intact and can be used for identification purposes.  
-       
-    5. **Environment**: Report that the accident occurred near a roadside with a guardrail, possibly in a rural or semi-rural area, which might help in establishing the accident location and context.  
-       
-    6. **Other Observations**: If there were any other circumstances or details not visible in the image that may have contributed to the accident, such as weather conditions, road conditions, or any other relevant information, be sure to include those as well.  
-       
-    Remember to be factual and descriptive, avoiding speculation about the cause of the accident, as the insurance company will conduct its own investigation.
-    ```
-<!--
-# [Image prompt enhancements](#tab/enhanced-image-chat)
-
-In this chat session, you instruct the assistant to aid in understanding images that you input. Try out the capabilities of the augmented vision model.  
-
-1. In the **Enhancements** pane on the left side of the chat window, turn on the option for **Vision**. In the window that appears, select your Azure Computer Vision resource.
-1. In the **System message** text box on the **System message** tab, provide this prompt to guide the assistant: `"You're an AI assistant that helps people find information."` You can tailor the prompt to your image or scenario. Select **Apply changes** to save your changes. 
-1. In the chat session pane, select the attachment button and then **Upload image**. Choose your image.
-1. Add the following question in the chat field: `"Describe this image"`, and then select the right arrow icon to send.
-1. The right arrow icon is replaced by a Stop button. If you select it, the assistant stops processing your request. For this quickstart, let the assistant finish its reply.
-1. The assistant replies with a description of the image. It uses the Azure AI Vision service to extract more detail from the image you uploaded.
-
-1. Ask a follow-up question related to the analysis of your image. Enter, `"What should I highlight about this image to my insurance company?" `and then select the right arrow icon to send.
-1. You should receive a relevant response similar to what's shown here:
-    ```
-    When reporting the incident to your insurance company, you should highlight the following key points from the image:  
-       
-    1. **Location of Damage**: Clearly state that the front end of the car, particularly the driver's side, is damaged. Mention the crumpled hood, broken front bumper, and the damaged left headlight.  
-       
-    2. **Point of Impact**: Indicate that the car has collided with a guardrail, which may suggest that no other vehicles were involved in the accident.  
-       
-    3. **Condition of the Car**: Note that the damage seems to be concentrated on the front end, and there is no visible damage to the windshield or rear of the car from this perspective.  
-       
-    4. **License Plate Visibility**: Mention that the license plate is intact and can be used for identification purposes.  
-       
-    5. **Environment**: Report that the accident occurred near a roadside with a guardrail, possibly in a rural or semi-rural area, which might help in establishing the accident location and context.  
-       
-    6. **Other Observations**: If there were any other circumstances or details not visible in the image that may have contributed to the accident, such as weather conditions, road conditions, or any other relevant information, be sure to include those as well.  
-       
-    Remember to be factual and descriptive, avoiding speculation about the cause of the accident, as the insurance company will conduct its own investigation.
-    ```
-
-# [Video prompt enhancements](#tab/video-chat)
-
-In this chat session, you are instructing the assistant to aid in understanding videos that you input. The assistant extracts several frames from the video and uses them to answer your questions.
-
-1. In the **Enhancements** pane on the left side of the chat window, turn on the option for **Vision**. In the window that appears, select your Azure Computer Vision resource.
-1. In the **System message** text box on the **System message** tab, provide this prompt to guide the assistant: `"You're an AI assistant that helps people find information."` You can tailor the prompt to your image or scenario.
-1. Select **Apply changes** to save your changes. 
-1. In the chat session pane, select the attachment button and then **Upload video**. Choose your video.
-1. Enter a text prompt like, `"Provide details about this video"`, and then select the right arrow icon to send.
-1. The right arrow icon is replaced by a Stop button. If you select it, the assistant stops processing your request. For this quickstart, let the assistant finish its reply.
-1. The assistant should reply with a description of the video.
-1. Feel free to ask any follow-up questions related to the analysis of your video.
-
-
-## Limitations
-
-Below are the known limitations of the video prompt enhancements.
-
-- **Low resolution:** The frames are analyzed using GPT-4 Turbo with Vision's "low resolution" setting, which may affect the accuracy of small object and text recognition in the video.
-- **Video file limits:** Both MP4 and MOV file types are supported. In the Azure AI Foundry portal Playground, videos must be less than 3 minutes long. When you use the API there is no such limitation.
-- **Prompt limits:** Video prompts only contain one video and no images. In Playground, you can clear the session to try with another video or images.
-- **Limited frame selection:** Currently the system selects 20 frames from the entire video, which might not capture all critical moments or details. Frame selection can either be evenly spread through the video or focused by a specific Video Retrieval query, depending on the prompt.
-- **Language support:** Currently, the system primarily supports English for grounding with transcripts. Transcripts don't provide accurate information on lyrics from songs.
-
----
--->
-
-
-## View and export code
-
-At any point in the chat session, you can enable the **Show raw JSON** switch at the top of the chat window to see the conversation formatted as JSON. Heres' what it looks like at the beginning of the quickstart chat session:
-
-```json
-[
-	{
-		"role": "system",
-		"content": [
-			"You are an AI assistant that helps people find information."
-		]
-	},
-]
-```
-
-## Clean up resources
-
-To avoid incurring unnecessary Azure costs, you should delete the resources you created in this quickstart if they're no longer needed. To manage resources, you can use the [Azure portal](https://portal.azure.com?azure-portal=true).
-
-## Next steps
-
-- [Create a project](../how-to/create-projects.md)
-- Learn more about [Azure AI Vision](../../ai-services/computer-vision/overview.md).
-- Learn more about [Azure OpenAI models](../../ai-services/openai/concepts/models.md).
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "マルチモーダルビジョンに関するクイックスタートガイドの削除"
}
```

### Explanation
この変更は、`articles/ai-studio/quickstarts/multimodal-vision.md`というファイルが完全に削除されたことを示しています。削除されたファイルには、Azure AI Foundryポータルで視覚機能を利用したチャットモデルをデプロイおよびテストするための手順が詳細に記されていました。

具体的には、このドキュメントでは、以下の内容が含まれていました：
- Azure AI Foundryを使用して、画像理解機能を持つチャットモデルをデプロイするための具体的な手順。
- 必要な前提条件（Azureサブスクリプション、Azure OpenAIリソースなど）。
- 実際の操作手順や画像を使ったデモ、ビデオプロンプトに関する情報。
- 使用に関する料金や制限事項、リソースのクリーンアップの仕方の説明。

このファイルの削除は、マルチモーダルビジョン機能の利用方法や関連するリソースが別の場所に移動されたか、またはもはや利用できないことを示唆しています。現在、ユーザーはこの情報を他のリソースを通じて確認する必要があります。この変更に関する詳細は、以下のリンクで確認できます：[GitHub上のドキュメント](https://github.com/MicrosoftDocs/azure-ai-docs/blob/f2b97989f8f69b4bd21461059c352cbe95859c00/articles%2Fai-studio%2Fquickstarts%2Fmultimodal-vision.md)。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -1,51 +1,36 @@
 items:
 - name: Azure AI Foundry documentation
   href: index.yml
-- name: Overview
+- name: What is Azure AI Foundry?
+  href: what-is-ai-studio.md
+- name: Get started
   expanded: true
   items:
-  - name: What is Azure AI Foundry?
-    href: what-is-ai-studio.md
-  - name: Azure AI Foundry architecture
-    href: concepts/architecture.md
-  - name: Azure OpenAI in Azure AI Foundry
-    href: azure-openai-in-ai-studio.md
-  - name: Management center
-    href: concepts/management-center.md
-  - name: Azure AI Foundry SDK
-    href: how-to/develop/sdk-overview.md
-    displayName: code, sdk
-  - name: Region support
-    href: reference/region-support.md
-  - name: Azure AI FAQ
-    href: faq.yml
-  - name: Which studio should I choose?
-    href: /ai/ai-studio-experiences-overview?context=/azure/ai-studio/context/context
-- name: Quickstarts
-  items:
-  - name: Use the chat playground
-    href: quickstarts/get-started-playground.md
-  - name: Build a chat app using the Azure AI SDK
-    href: quickstarts/get-started-code.md
-    displayName: code
-  - name: Get started using Azure OpenAI Assistants
-    href: ../ai-services/openai/assistants-quickstart.md?context=/azure/ai-studio/context/context
-- name: Tutorials
-  items:
-  - name: Deploy an enterprise chat web app
-    href: tutorials/deploy-chat-web-app.md
-  - name: Build a custom chat app with the Azure AI Foundry SDK
+  - name: Quickstarts
     items:
-      - name: "Part 1: Set up project and install SDK"
-        href: tutorials/copilot-sdk-create-resources.md
-      - name: "Part 2: Build with data retrieval"
-        href: tutorials/copilot-sdk-build-rag.md
-        displayName: code,sdk
-      - name: "Part 3: Evaluate the chat app"
-        href: tutorials/copilot-sdk-evaluate.md
-        displayName: code,sdk
-- name: How-to
-  expanded: true
+    - name: Use the chat playground
+      href: quickstarts/get-started-playground.md
+    - name: Build app in Python with Azure AI Foundry SDK
+      href: quickstarts/get-started-code.md
+    - name: Get started with Azure AI Foundry SDK
+      href: how-to/develop/sdk-overview.md
+  - name: Tutorials
+    items:
+    - name: Build a custom chat app with Azure AI Foundry SDK
+      items:
+        - name: "Part 1: Set up project and install SDK"
+          href: tutorials/copilot-sdk-create-resources.md
+        - name: "Part 2: Build with data retrieval"
+          href: tutorials/copilot-sdk-build-rag.md
+          displayName: code,sdk
+        - name: "Part 3: Evaluate the chat app"
+          href: tutorials/copilot-sdk-evaluate.md
+          displayName: code,sdk
+    - name: Deploy an enterprise chat web app
+      href: tutorials/deploy-chat-web-app.md
+    - name: Build a RAG solution using Azure AI Search
+      href: /azure/search/tutorial-rag-build-solution?context=/azure/ai-studio/context/context
+- name: Explore AI model capabilities
   items:
   - name: Azure OpenAI and AI services
     items:
@@ -107,34 +92,6 @@ items:
     - name: Distillation
       href: concepts/concept-model-distillation.md
     - name: Azure OpenAI models
-      items:
-      - name: Deploy Azure OpenAI models
-        href: how-to/deploy-models-openai.md
-      - name: Fine-tune Azure OpenAI models
-        href: ../ai-services/openai/how-to/fine-tuning.md?context=/azure/ai-studio/context/context
-    - name: Healthcare AI models
-      items:
-        - name: Foundational AI models for healthcare
-          href: how-to/healthcare-ai/healthcare-ai-models.md
-        - name: MedImageInsight - embedding model
-          href: how-to/healthcare-ai/deploy-medimageinsight.md
-        - name: CXRReportGen - text generation model
-          href: how-to/healthcare-ai/deploy-cxrreportgen.md
-        - name: MedImageParse - prompted segmentation model
-          href: how-to/healthcare-ai/deploy-medimageparse.md
-    - name: Microsoft Phi family models
-      items:
-        - name: Phi-3 chat models
-          href: how-to/deploy-models-phi-3.md
-        - name: Phi-3 chat model with vision
-          href: how-to/deploy-models-phi-3-vision.md
-        - name: Phi-3.5 chat model with vision
-          href: how-to/deploy-models-phi-3-5-vision.md
-        - name: Phi-4 chat models
-          href: how-to/deploy-models-phi-4.md
-        - name: Fine-tune Phi-3 chat models
-          href: how-to/fine-tune-phi-3.md
-    - name: Cohere models
       items:
       - name: Cohere Command models
         href: how-to/deploy-models-cohere-command.md
@@ -144,55 +101,119 @@ items:
         href: how-to/deploy-models-cohere-rerank.md
     - name: DeepSeek-R1 reasoning models
       href: how-to/deploy-models-deepseek.md
+    - name: Gretel Navigator model
+      href: how-to/deploy-models-gretel-navigator.md
+    - name: Healthcare AI models
+      items:
+      - name: Foundational AI models for healthcare
+        href: how-to/healthcare-ai/healthcare-ai-models.md
+      - name: MedImageInsight - embedding model
+        href: how-to/healthcare-ai/deploy-medimageinsight.md
+      - name: CXRReportGen - text generation model
+        href: how-to/healthcare-ai/deploy-cxrreportgen.md
+      - name: MedImageParse - prompted segmentation model
+        href: how-to/healthcare-ai/deploy-medimageparse.md
+    - name: JAIS model
+      href: how-to/deploy-models-jais.md
     - name: Meta Llama models
       items:
       - name: Meta Llama family models
         href: how-to/deploy-models-llama.md
       - name: Fine-tune Meta Llama family models
         href: how-to/fine-tune-model-llama.md
+    - name: Microsoft Phi family models
+      items:
+      - name: Phi-3 chat models
+        href: how-to/deploy-models-phi-3.md
+      - name: Phi-3 chat model with vision
+        href: how-to/deploy-models-phi-3-vision.md
+      - name: Phi-3.5 chat model with vision
+        href: how-to/deploy-models-phi-3-5-vision.md
+      - name: Phi-4 chat models
+        href: how-to/deploy-models-phi-4.md
+      - name: Fine-tune Phi-3 chat models
+        href: how-to/fine-tune-phi-3.md
     - name: Mistral family models
       items:
-        - name: Mistral premium models
-          href: how-to/deploy-models-mistral.md
-        - name: Codestral model
-          href: how-to/deploy-models-mistral-codestral.md
-        - name: Mistral Nemo model
-          href: how-to/deploy-models-mistral-nemo.md
-        - name: Mistral-7B and Mixtral models
-          href: how-to/deploy-models-mistral-open.md
+      - name: Mistral premium models
+        href: how-to/deploy-models-mistral.md
+      - name: Codestral model
+        href: how-to/deploy-models-mistral-codestral.md
+      - name: Mistral Nemo model
+        href: how-to/deploy-models-mistral-nemo.md
+      - name: Mistral-7B and Mixtral models
+        href: how-to/deploy-models-mistral-open.md
       displayName: maas
-    - name: Gretel Navigator model
-      href: how-to/deploy-models-gretel-navigator.md
-    - name: JAIS model
-      href: how-to/deploy-models-jais.md
-    - name: AI21 Jamba models
-      href: how-to/deploy-models-jamba.md
+    - name: NTTDATA tsuzumi model
+      items:
+        - name: NTTDATA tsuzumi model
+          href: how-to/deploy-models-tsuzumi.md
+        - name: Fine-tune tsuzumi model
+          href: how-to/fine-tune-models-tsuzumi.md
     - name: TimeGEN-1 model
       href: how-to/deploy-models-timegen-1.md
-    - name: NTTDATA tsuzumi model
-      href: how-to/deploy-models-tsuzumi.md
-    - name: Fine-tune tsuzumi model
-      href: how-to/fine-tune-models-tsuzumi.md
-  - name: Deploy AI models
+  - name: Azure OpenAI and AI services
     items:
-      - name: Deployments overview
-        href: concepts/deployments-overview.md
-        displayName: endpoint
-      - name: Azure AI model inference
-        items:
-        - name: What is the Azure AI model inference service?
-          href: ../ai-foundry/model-inference/overview.md?context=/azure/ai-studio/context/context
-        - name: Upgrade from GitHub Models
-          href: ../ai-foundry/model-inference/how-to/quickstart-github-models.md?context=/azure/ai-studio/context/context
-        - name: Add and configure models
-          href: ../ai-foundry/model-inference/how-to/create-model-deployments.md?context=/azure/ai-studio/context/context
+    - name: Use Azure OpenAI Service in Azure AI Foundry portal
+      href: ai-services/how-to/connect-azure-openai.md
+    - name: Use Azure AI services in Azure AI Foundry portal
+      href: ai-services/how-to/connect-ai-services.md
+      displayName: cognitive,task
+    - name: What are Azure AI services?
+      href: concepts/what-are-ai-services.md
+    - name: Azure OpenAI
+      items:
+      - name: Deploy Azure OpenAI models
+        items: 
+        - name: Azure OpenAI in Azure AI Foundry
+          href: azure-openai-in-ai-studio.md
+        - name: Model region availability
+          href:  ../ai-services/openai/concepts/models.md?context=/azure/ai-studio/context/context
+          displayName: OpenAI, gpt-4o, gpt-4o-mini, whisper
         - name: Deployment types
-          href: ../ai-foundry/model-inference/concepts/deployment-types.md?context=/azure/ai-studio/context/context
-        - name: Use the inference endpoint
-          href: ../ai-foundry/model-inference/concepts/endpoints.md?context=/azure/ai-studio/context/context
-        - name: Quotas and limits
-          href: ../ai-foundry/model-inference/quotas-limits.md?context=/azure/ai-studio/context/context
-      - name: Serverless API
+          href: ../ai-services/openai/how-to/deployment-types.md?context=/azure/ai-studio/context/context
+          displayName: provisioned, global standard, datazone, data zone, global data zone, batch, globalbatch
+        - name: Model deployment
+          href: how-to/deploy-models-openai.md
+      - name: Generate text
+        items:
+        - name: Batch
+          href: ../ai-services/openai/how-to/batch.md?context=/azure/ai-studio/context/context
+          displayName: OpenAI, global batch, globalbatch, chat, chat completions
+        - name: Reasoning models
+          href: ../ai-services/openai/how-to/reasoning.md?context=/azure/ai-studio/context/context
+          displayName: OpenAI, o1, o1-mini, o3-mini, reasoning effort
+        - name: Function calling
+          href: ../ai-services/openai/how-to/function-calling.md?context=/azure/ai-studio/context/context
+          displayName: OpenAI 
+        - name: Predicted outputs
+          href: ../ai-services/openai/how-to/predicted-outputs.md?context=/azure/ai-studio/context/context 
+        - name: Prompt caching
+          href: ../ai-services/openai/how-to/prompt-caching.md?context=/azure/ai-studio/context/context 
+        - name: Structured outputs
+          href: ../ai-services/openai/how-to/structured-outputs.md?context=/azure/ai-studio/context/context 
+        - name: Use vision-enabled chat
+          href:  ../ai-services/openai/gpt-v-quickstart.md?context=/azure/ai-studio/context/context
+      - name: Generate images
+        href: ../ai-services/openai/dall-e-quickstart.md?context=/azure/ai-studio/context/context
+        displayName: OpenAI, DALLE, dall-e, DALL-E
+      - name: Audio
+        items:
+          - name: Use GPT-4o in the real-time audio playground
+            href: ../ai-services/openai/realtime-audio-quickstart.md?context=/azure/ai-studio/context/context
+            displayName: OpenAI, realtime, real-time
+          - name: Audio generation
+            href: ../ai-services/openai/audio-completions-quickstart.md?context=/azure/ai-studio/context/context 
+      - name: Distillation (stored completions)
+        href: ../ai-services/openai/how-to/stored-completions.md?context=/azure/ai-studio/context/context
+        displayName: OpenAI, Azure OpenAI, stored completions, model distillation
+      - name: Embeddings
+        href: ../ai-services/openai/tutorials/embeddings.md?context=/azure/ai-studio/context/context
+        displayName: text-embedding-ada-002, text-embedding-3-large, text-embedding-3-small
+      - name: Evaluation
+        href: ../ai-services/openai/how-to/evaluations.md?context=/azure/ai-studio/context/context
+        displayName: OpenAI
+      - name: Fine-tuning
         items:
         - name: Deploy models as serverless API
           href: how-to/deploy-models-serverless.md
@@ -219,103 +240,116 @@ items:
       href: how-to/develop/create-hub-project-sdk.md
     - name: Create a hub with custom security
       items:
-      - name: Create a hub in the Azure portal
-        href: how-to/create-secure-ai-hub.md
-      - name: Create a hub from template
-        href: how-to/create-azure-ai-hub-template.md
-        displayName: code
-      - name: Create a hub using Terraform
-        href: how-to/create-hub-terraform.md
-
-    - name: Create and manage compute
-      href: how-to/create-manage-compute.md
-  - name: Connections
+      - name: Azure Image Analysis
+        items:
+        - name: What is Image Analysis?
+          href: /azure/ai-services/computer-vision/overview-image-analysis?context=/azure/ai-studio/context/context
+        - name: Quickstart
+          href: /azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library-40?context=/azure/ai-studio/context/context
+        - name: Optical Character Recognition concepts
+          href: /azure/ai-services/computer-vision/concept-ocr?context=/azure/ai-studio/context/context
+        - name: Image captioning concepts
+          href: /azure/ai-services/computer-vision/concept-describe-images-40?context=/azure/ai-studio/context/context
+      - name: Azure AI Face
+        items:
+        - name: What is Azure AI Face service?
+          href: /azure/ai-services/computer-vision/overview-identity?context=/azure/ai-studio/context/context
+        - name: Quickstart 
+          href: /azure/ai-services/computer-vision/quickstarts-sdk/identity-client-library?context=/azure/ai-studio/context/context
+        - name: Face detection concepts
+          href: /azure/ai-services/computer-vision/concept-face-detection?context=/azure/ai-studio/context/context
+        - name: Face recognition concepts
+          href: /azure/ai-services/computer-vision/concept-face-recognition?context=/azure/ai-studio/context/context
+        - name: Liveness detection tutorial
+          href: /azure/ai-services/computer-vision/tutorials/liveness?context=/azure/ai-studio/context/context
+- name: Solutions
+  items:
+  - name: Agents
     items:
-    - name: Connections overview
-      href: concepts/connections.md
-    - name: Create a connection
-      href: how-to/connections-add.md
-    - name: Create a connection using the Azure Machine Learning SDK
-      href: how-to/develop/connections-add-sdk.md
-      displayName: code
-  - name: Data for your generative AI app
+    - name: What is Azure AI Agent Service
+      href: ../ai-services/agents/overview.md?context=/azure/ai-studio/context/context
+    - name: "Quickstart: Create a new agent"
+      href: ../ai-services/agents/quickstart.md?context=/azure/ai-studio/context/context
+  - name: Azure AI Search for RAG
     items:
-    - name: Overview of retrieval augmented generation (RAG)
+    - name: Retrieval Augmented Generation (RAG) overview
       href: concepts/retrieval-augmented-generation.md
-      displayName: RAG
-    - name: Add data to your project
-      href: how-to/data-add.md
-      displayName: index
-    - name: Build and consume vector indexes
+    - name: Use Azure AI Search
+      href: /azure/search/search-what-is-azure-search?context=/azure/ai-studio/context/context
+    - name: Build and consume vector indexes (Portal)
       href: how-to/index-add.md
-    - name: Build and consume indexes using code
+    - name: Build and consume vector indexes (Code)
       href: how-to/develop/index-build-consume-sdk.md
+    - name: Build a RAG solution using Azure AI Search
+      href: /azure/search/tutorial-rag-build-solution?context=/azure/ai-studio/context/context
+  - name: Develop with code
+    items:
+    - name: Work with projects in VS Code
+      href: how-to/develop/vscode.md
+    - name: Start with an AI template
+      href: how-to/develop/ai-template-get-started.md
+    - name: Develop with LangChain
+      href: how-to/develop/langchain.md
+    - name: Develop with LlamaIndex
+      href: how-to/develop/llama-index.md
+      displayName: code,sdk
+    - name: Develop with Semantic Kernel
+      href: how-to/develop/semantic-kernel.md
+  - name: Model inference
+    items:
+    - name: What is Azure AI model inference?
+      href: ../ai-foundry/model-inference/overview.md?context=/azure/ai-studio/context/context
+    - name: Upgrade from GitHub Models
+      href: ../ai-foundry/model-inference/how-to/quickstart-github-models.md?context=/azure/ai-studio/context/context
+    - name: Add and configure models
+      href: ../ai-foundry/model-inference/how-to/create-model-deployments.md?context=/azure/ai-studio/context/context
+    - name: Use the inference endpoint
+      href: ../ai-foundry/model-inference/concepts/endpoints.md?context=/azure/ai-studio/context/context
+  - name: Deployments
+    items:
+    - name: Deploying models in Azure AI Foundry
+      href: concepts/deployments-overview.md
+    - name: Deploy models as serverless API
+      href: how-to/deploy-models-serverless.md
+    - name: Deploy models via managed compute
+      href: how-to/deploy-models-managed.md
+    - name: Consume serverless API models from a different project or hub
+      href: how-to/deploy-models-serverless-connect.md
+      displayName: maas, paygo, models-as-a-service
+    - name: Model and region availability for Serverless API deployments
+      href: how-to/deploy-models-serverless-availability.md
+    - name: Quotas and limits
+      href: ai-services/concepts/quotas-limits.md
+    - name: Troubleshoot deployments and monitoring
+      href: how-to/troubleshoot-deploy-and-monitor.md
+- name: Optimizations
+  items:
+  - name: Prompt engineering
+    items:
+    - name: Prompt engineering techniques
+      href: ../ai-services/openai/concepts/prompt-engineering.md?context=/azure/ai-studio/context/context
+    - name: Image prompt engineering
+      href: ../ai-services/openai/concepts/gpt-4-v-prompt-engineering.md?context=/azure/ai-studio/context/context
     - name: Synthetic Data Generation
       href: concepts/concept-synthetic-data.md
-      displayName: code,sdk
-  - name: Develop generative AI apps
+  - name: Fine-tuning
     items:
-    - name: Develop in Azure AI Foundry portal
-      items:
-      - name: Build apps with prompt flow
-        items:
-        - name: Prompt flow overview
-          href: how-to/prompt-flow.md
-        - name: Develop flows
-          items:
-          - name: Create and manage compute session
-            href: how-to/create-manage-compute-session.md
-          - name: Create a flow
-            href: how-to/flow-develop.md
-          - name: Tune prompts using variants
-            href: how-to/flow-tune-prompts-using-variants.md
-          - name: Process images in a flow
-            href: how-to/flow-process-image.md
-          - name: Use prompt flow tools
-            items:
-            - name: Prompt flow tools overview
-              href: how-to/prompt-flow-tools/prompt-flow-tools-overview.md
-            - name: LLM tool
-              href: how-to/prompt-flow-tools/llm-tool.md
-            - name: Prompt tool
-              href: how-to/prompt-flow-tools/prompt-tool.md
-            - name: Python tool
-              href: how-to/prompt-flow-tools/python-tool.md
-            - name: Azure OpenAI GPT-4 Turbo with Vision tool
-              href: how-to/prompt-flow-tools/azure-open-ai-gpt-4v-tool.md
-            - name: Index Lookup tool
-              href: how-to/prompt-flow-tools/index-lookup-tool.md
-            - name: Rerank tool
-              href: how-to/prompt-flow-tools/rerank-tool.md
-            - name: Content Safety tool
-              href: how-to/prompt-flow-tools/content-safety-tool.md
-            - name: Embedding tool
-              href: how-to/prompt-flow-tools/embedding-tool.md
-            - name: Serp API tool
-              href: how-to/prompt-flow-tools/serp-api-tool.md
-        - name: Troubleshoot prompt flow
-          href: how-to/prompt-flow-troubleshoot.md
-    - name: Develop with code
-      items:
-      - name: Work with projects in VS Code
-        href: how-to/develop/vscode.md
-      - name: Start with an AI template
-        href: how-to/develop/ai-template-get-started.md
-      - name: Develop with LangChain
-        href: how-to/develop/langchain.md
-      - name: Develop with LlamaIndex
-        href: how-to/develop/llama-index.md
-        displayName: code,sdk
-      - name: Develop with Semantic Kernel 
-        href: how-to/develop/semantic-kernel.md
-    - name: Trace generative AI apps
-      items:
-       - name: Tracing overview
-         href: concepts/trace.md 
-       - name: Trace your application with Azure AI Inference SDK
-         href: how-to/develop/trace-local-sdk.md
-       - name: Visualize your traces
-         href: how-to/develop/visualize-traces.md
+    - name: Fine-tuning in Azure AI Foundry
+      href: concepts/fine-tuning-overview.md
+    - name: Fine-tune with a managed compute
+      href: how-to/fine-tune-managed-compute.md
+    - name: Fine-tune Azure OpenAI models
+      href: ../ai-services/openai/how-to/fine-tuning.md?context=/azure/ai-studio/context/context
+    - name: Distillation
+      href: concepts/concept-model-distillation.md
+  - name: Tracing
+    items:
+    - name: Tracing in Azure AI Foundry
+      href: concepts/trace.md
+    - name: Trace your application with Azure AI Inference SDK
+      href: how-to/develop/trace-local-sdk.md
+    - name: Visualize your traces
+      href: how-to/develop/visualize-traces.md
   - name: Evaluate generative AI apps
     items:
     - name: Evaluations concepts
@@ -344,24 +378,96 @@ items:
           href: how-to/flow-bulk-test-evaluation.md
         - name: Develop an evaluation flow in Prompt flow
           href: how-to/flow-develop-evaluation.md
-    - name: A/B experimentation 
+    - name: A/B experimentation
       href: concepts/a-b-experimentation.md
-  - name: Deploy and monitor generative AI apps
+  - name: Build apps with prompt flow
+    items:
+    - name: Prompt flow overview
+      href: how-to/prompt-flow.md
+    - name: Develop flows
+      items:
+      - name: Create and manage compute session
+        href: how-to/create-manage-compute-session.md
+      - name: Create a flow
+        href: how-to/flow-develop.md
+      - name: Tune prompts using variants
+        href: how-to/flow-tune-prompts-using-variants.md
+      - name: Process images in a flow
+        href: how-to/flow-process-image.md
+      - name: Use prompt flow tools
+        items:
+        - name: Prompt flow tools overview
+          href: how-to/prompt-flow-tools/prompt-flow-tools-overview.md
+        - name: LLM tool
+          href: how-to/prompt-flow-tools/llm-tool.md
+        - name: Prompt tool
+          href: how-to/prompt-flow-tools/prompt-tool.md
+        - name: Python tool
+          href: how-to/prompt-flow-tools/python-tool.md
+        - name: Azure OpenAI GPT-4 Turbo with Vision tool
+          href: how-to/prompt-flow-tools/azure-open-ai-gpt-4v-tool.md
+        - name: Index Lookup tool
+          href: how-to/prompt-flow-tools/index-lookup-tool.md
+        - name: Rerank tool
+          href: how-to/prompt-flow-tools/rerank-tool.md
+        - name: Content Safety tool
+          href: how-to/prompt-flow-tools/content-safety-tool.md
+        - name: Embedding tool
+          href: how-to/prompt-flow-tools/embedding-tool.md
+        - name: Serp API tool
+          href: how-to/prompt-flow-tools/serp-api-tool.md
+    - name: Deploy and monitor generative AI apps
+      items:
+      - name: Continuously monitor your applications
+        href: how-to/monitor-applications.md
+      - name: Deploy and monitor flows
+        items:
+        - name: Deploy a flow for real-time inference
+          href: how-to/flow-deploy.md
+          displayName: endpoint
+        - name: Enable tracing and collect feedback for a flow deployment
+          href: how-to/develop/trace-production-sdk.md
+          displayName: code
+        - name: Monitor prompt flow deployments
+          href: how-to/monitor-quality-safety.md
+        - name: Troubleshoot prompt flow
+          href: how-to/prompt-flow-troubleshoot.md
+- name: Management center
+  items:
+  - name: Management center overview
+    href: concepts/management-center.md
+  - name: Manage projects and hubs
     items:
-    - name: Continuously monitor your applications
-      href: how-to/monitor-applications.md
-    - name: Deploy and monitor flows
+    - name: Create a project
+      href: how-to/create-projects.md
+    - name: Hubs and projects overview
+      href: concepts/ai-resources.md
+    - name: Create your first hub
+      href: how-to/create-azure-ai-resource.md
+    - name: Create a hub using the Azure Machine Learning SDK and CLI
+      href: how-to/develop/create-hub-project-sdk.md
+    - name: Create a hub with custom security
       items:
-      - name: Deploy a flow for real-time inference
-        href: how-to/flow-deploy.md
-        displayName: endpoint
-      - name: Enable tracing and collect feedback for a flow deployment
-        href: how-to/develop/trace-production-sdk.md
+      - name: Create a hub in the Azure portal
+        href: how-to/create-secure-ai-hub.md
+      - name: Create a hub from template
+        href: how-to/create-azure-ai-hub-template.md
         displayName: code
-      - name: Monitor prompt flow deployments
-        href: how-to/monitor-quality-safety.md
-      - name: Troubleshoot deployments and monitoring
-        href: how-to/troubleshoot-deploy-and-monitor.md
+      - name: Create a hub using Terraform
+        href: how-to/create-hub-terraform.md
+  - name: Create and manage compute
+    href: how-to/create-manage-compute.md
+  - name: Connections
+    items:
+    - name: Connections overview
+      href: concepts/connections.md
+    - name: Create a connection
+      href: how-to/connections-add.md
+    - name: Create a connection using the Azure Machine Learning SDK
+      href: how-to/develop/connections-add-sdk.md
+      displayName: code
+  - name: Add and manage data in Azure AI Foundry
+    href: how-to/data-add.md
   - name: Costs and quotas
     items:
     - name: Plan and manage costs
@@ -416,7 +522,7 @@ items:
   items:
   - name: Responsible AI overview
     href: responsible-use-of-ai-overview.md
-  - name: What is Azure AI Content Safety?
+  - name: Azure AI Content Safety in AI Foundry portal overview
     href: ai-services/content-safety-overview.md
   - name: Content safety for models deployed with serverless APIs
     href: concepts/model-catalog-content-safety.md
@@ -448,15 +554,19 @@ items:
   - name: Azure AI services REST APIs
     displayName: swagger http
     href: ../ai-services/reference/rest-api-resources.md?context=/azure/ai-studio/context/context
-  - name: Prompt flow Python SDK
-    href: https://microsoft.github.io/promptflow/reference/index.html#
   - name: Azure AI Model Inference API
     href: ../ai-foundry/model-inference/reference/reference-model-inference-api.md
   - name: Azure Policy built-ins
     displayName: samples, policies, definitions
     href: ../ai-services/policy-reference.md?context=/azure/ai-studio/context/context
+  - name: Region support
+    href: reference/region-support.md
 - name: Resources
   items:
+  - name: Azure AI FAQ
+    href: faq.yml
+  - name: Azure AI Foundry architecture
+    href: concepts/architecture.md
   - name: Support & help options
     href: ../ai-services/cognitive-services-support-options.md?context=/azure/ai-studio/context/context
   - name: Use Azure AI Foundry with a screen reader
@@ -473,11 +583,3 @@ items:
     href: https://azure.microsoft.com/support/legal/sla/cognitive-services/v1_1/
   - name: Azure Government
     href: /azure/azure-government/compare-azure-government-global-azure
-  - name: Videos
-    href: https://azure.microsoft.com/resources/videos/index/?services=cognitive-services
-  - name: Azure Blog
-    href: https://azure.microsoft.com/blog/
-  - name: Artificial Intelligence and Machine Learning Blog
-    href: https://techcommunity.microsoft.com/t5/artificial-intelligence-and/ct-p/AI
-  - name: LLMOps with Prompt Flow
-    href: https://github.com/microsoft/llmops-promptflow-template
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studio の目次ファイルの更新"
}
```

### Explanation
この変更は、`articles/ai-studio/toc.yml`ファイルの更新を示しており、322行が追加され、220行が削除されています。この変更により、Azure AI Studioに関連する情報の整理が行われ、目次がより一貫性のある構造になりました。

主なポイントは以下の通りです：
- 目次の項目が再構成されており、新しいタイトルやリンクが追加されています。例えば、「Overview」という項目が「What is Azure AI Foundry?」に変更され、関連するドキュメントへのリンクが設定されています。
- 「Quickstarts」「Tutorials」「How-to」といったセクションが再編成され、ナビゲーションが改善されています。これにより、ユーザーが必要な情報に迅速にアクセスできるようになっています。
- 新たに「Explore AI model capabilities」という項目が追加され、Azure OpenAIやAIサービスに関する資料が含まれるようになっています。
- いくつかのリンクが更新され、古いリンクや内容が削除されていますが、新しい情報で補完されています。

この変更により、Azure AI Studioに関する情報がより明確で整理され、ユーザーにとって使いやすくなっています。変更されたファイルの詳細は、以下のリンクで確認できます：[GitHub上のドキュメント](https://github.com/MicrosoftDocs/azure-ai-docs/blob/b07793e742363ee5bdb8f64774c24fc8a5555086/articles%2Fai-studio%2Ftoc.yml)。


