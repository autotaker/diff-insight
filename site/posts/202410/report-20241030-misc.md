---
date: '2024-10-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d84fb33...MicrosoftDocs:a68723c
summary: このコード差分は、ドキュメントインテリジェンスやAIスタジオに関連する目次の改善、新しいリダイレクト設定の追加、説明文の明確化、モデル展開手順の整理、リンクの修正などの更新を含んでいます。特に、AIサービスに関する「始めに」記事と共有インクルードファイルの削除が目立つ破壊的変更として挙げられます。新しいセクションが追加され、ユーザーが情報にアクセスしやすくなる一方、一部の情報が失われる可能性もあります。全体として、これらの変更はユーザビリティの向上を目指したものと考えられます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d84fb33...MicrosoftDocs:a68723c){target="_blank"}

<format>
# Highlights
このコード差分には、ドキュメントインテリジェンスやAIスタジオに関連する目次の改善、新しいリダイレクト設定の追加、説明文の明確化、モデル展開手順の整理、リンクの修正といった更新が含まれています。特に、AIサービスに関する「始めに」記事と共有インクルードファイルの削除が目立つ破壊的変更として挙げられます。

## New features
- AIスタジオの目次に「Azure OpenAIとAIサービス」や「ハブとプロジェクトの作成」といった新しいセクションが追加。

## Breaking changes
- AIサービスに関する「始めに」記事の完全削除。
- 共有インクルードファイルの削除により、関連情報が失われる恐れ。

## Other updates
- ドキュメントインテリジェンス関連の目次に新しい項目が追加。
- AIスタジオにリダイレクト設定が追加され、ユーザーが簡単に情報にアクセスできるように。
- 説明文やリンクの修正により情報の明確性とアクセスが向上。
- 医療AIモデルの展開手順の改善と整理。

# Insights
この変更は、AzureのAIサービスとAIスタジオを中心としたドキュメント更新を目的にしています。主にユーザーが必要な情報にアクセスしやすくすることを念頭に置いています。例えば、新しい項目の追加やリダイレクト設定は、情報の取得をスムーズにするための措置であり、ユーザーがドキュメントを効率よく利用できるように考慮されています。

一方で、AIサービスに関する基本的な記事の削除や共有インクルードファイルが削除されており、これまで提供されていた情報が一部失われる可能性があります。これに関しては、関連する新しい文書やセクションの追加が行われなければ、ユーザーが正しい情報を確実に受け取るためのサポートが不足するかもしれません。そのため、さらに詳細なドキュメントの補完や新しいコンテンツの配信が必要になるでしょう。

実際の使用において、これらの変更がどのように影響するかは、特にスタジオを利用する際のユーザビリティの向上につながることが期待されます。情報の精査やテストを通じて継続的な改善が求められる場面もあるでしょう。全体として、目次の更新などは情報の一貫性と統一されたユーザー体験を提供する基盤になると考えられます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [toc.yml](#item-81aa7b) | minor update | ドキュメントインテリジェンスのリソース作成に関する項目の追加と修正 | modified | 5 | 5 | 10 | 
| [.openpublishing.redirection.ai-studio.json](#item-c75c21) | minor update | AIスタジオに関するリダイレクト設定の追加 | modified | 5 | 0 | 5 | 
| [connect-ai-services.md](#item-3f7954) | minor update | AIサービスの紹介文の修正 | modified | 1 | 1 | 2 | 
| [get-started.md](#item-8378f4) | breaking change | AIサービスに関する「始めに」記事の削除 | removed | 0 | 47 | 47 | 
| [access-on-premises-resources.md](#item-8e3926) | minor update | リソースアクセスガイドの文言修正 | modified | 2 | 2 | 4 | 
| [concept-data-privacy.md](#item-af88ce) | minor update | データプライバシーに関する記事の更新 | modified | 4 | 1 | 5 | 
| [trace-local-sdk.md](#item-f7dfb5) | minor update | Trace Local SDKの記事の著者情報修正 | modified | 2 | 2 | 4 | 
| [deploy-cxrreportgen.md](#item-377d15) | minor update | CXRReportGenモデルの展開手順の改善 | modified | 5 | 6 | 11 | 
| [deploy-medimageinsight.md](#item-e9ab9e) | minor update | MedImageInsightモデルの展開手順の改善 | modified | 4 | 5 | 9 | 
| [deploy-medimageparse.md](#item-611e84) | minor update | MedImageParseモデルの展開手順の改善 | modified | 5 | 6 | 11 | 
| [healthcare-ai-models.md](#item-12fcfc) | minor update | Azure AIモデルカタログのリンク修正 | modified | 1 | 3 | 4 | 
| [shared-ai-studio-and-azure-ml-articles.md](#item-c1f692) | breaking change | 共有インクルードファイルの削除 | removed | 0 | 13 | 13 | 
| [toc.yml](#item-2745cd) | minor update | 目次の更新と整理 | modified | 67 | 63 | 130 | 


# Modified Contents
## articles/ai-services/document-intelligence/toc.yml{#item-81aa7b}

<details>
<summary>Diff</summary>
````diff
@@ -9,6 +9,9 @@ items:
     href: overview.md
   - name: Which model should I choose?
     href: concept/choose-model-feature.md
+  - name: Create a Document Intelligence resource
+    displayName: endpoint, key, portal
+    href:  how-to-guides/create-document-intelligence-resource.md  
   - name: Document Intelligence Studio
     displayName: get started
     href: studio-overview.md
@@ -138,9 +141,9 @@ items:
   - name: Custom model lifecycle
     displayName: custom, train, modelId, model ID, expiration, train, build
     href: train/custom-lifecycle.md
-- name: Features
+- name: Add-on features
   items:
-  - name: Add-on capabilities
+  - name: Enhanced capabilities
     displayName: extract, formula, font, styles, fontStyle, ocr.highResolution, ocr.formula, high resolution, background color, inline, display
     href: concept-add-on-capabilities.md
   - name: Query field extraction
@@ -176,9 +179,6 @@ items:
   - name: Use Document Intelligence models
     displayName: documentAnalysisClient, document analysis client, polygon, boundingPolygon, begin_analyze_document,ormRecognizerClient, Document Intelligence client, boundingBox, box, begin_recognize, v2.1
     href: how-to-guides/use-sdk-rest-api.md
-  - name: Create a Document Intelligence resource
-    displayName: endpoint, key, portal
-    href:  how-to-guides/create-document-intelligence-resource.md
   - name: 🆕 Build and train a custom generative model
     displayName: ai studio, neural, template, custom
     href: how-to-guides/build-train-custom-generative-model.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのリソース作成に関する項目の追加と修正"
}
```

### Explanation
この修正は、ドキュメントインテリジェンスに関するトピックの目次ファイル（toc.yml）の小規模な更新です。特に、以下の変更が行われました：

1. **新しい項目の追加**: "Create a Document Intelligence resource"という新しい項目が、目次に追加されました。これにより、このリソースの作成に関するガイドへのリンクが提供され、ユーザーがより簡単にアクセスできるようになっています。

2. **項目名の変更**: "Features"というセクション名が"Add-on features"に更新され、特定の機能に対する理解を深めるための名称変更が行われました。

3. **特定の機能の名称変更**: "Add-on capabilities"は"Enhanced capabilities"に変更され、これにより提供される機能のより良い説明が図られています。

このように、トピックの目次において、ユーザーが必要とする情報により迅速にアクセスできるような小さな改善が行われました。

## articles/ai-studio/.openpublishing.redirection.ai-studio.json{#item-c75c21}

<details>
<summary>Diff</summary>
````diff
@@ -134,6 +134,11 @@
             "source_path_from_root": "/articles/ai-studio/how-to/evaluate-flow-results.md",
             "redirect_url": "/azure/ai-studio/how-to/evaluate-results",
             "redirect_document_id": true
+        },
+        {
+            "source_path_from_root": "/articles/ai-studio/ai-services/get-started.md",
+            "redirect_url": "/azure/ai-studio/ai-services/connect-ai-services",
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
    "modification_title": "AIスタジオに関するリダイレクト設定の追加"
}
```

### Explanation
この修正は、AIスタジオに関連するリダイレクト設定を含むJSONファイル（.openpublishing.redirection.ai-studio.json）の小規模な更新を示しています。具体的には、以下の変更が行われました：

1. **新しいリダイレクトエントリの追加**: 新たに、"get-started.md"から"/azure/ai-studio/ai-services/connect-ai-services"へのリダイレクトが追加されました。このリダイレクトは、ユーザーがAIサービスの接続に関する資料にアクセスするのを容易にします。

2. **リダイレクト設定の詳細**: 新しいエントリは、元のパスとリダイレクト先の両方を含む詳細な設定が提供されており、リダイレクト時に文書IDは不要とされています。

この変更により、利用者がAIスタジオに関連する情報をより簡単に見つけられるようになり、利便性が向上しています。

## articles/ai-studio/ai-services/connect-ai-services.md{#item-3f7954}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: eric-urban
 
 # Connect AI services to your hub in Azure AI Studio
 
-You can try out AI services for free in Azure AI Studio as described in the [getting started with AI services](get-started.md) article. This article describes how to use AI services connections to do more via Azure AI Studio, SDKs, and APIs. 
+You can try out AI services for free in Azure AI Studio via model catalog cards and playground experiences. This article describes how to use AI services connections to do more via Azure AI Studio, SDKs, and APIs. 
 
 After you create a hub with AI services, you can use the AI services connection via the AI Studio UI, APIs, and SDKs. For example, you can try out AI services via **Home** > **AI Services** in the AI Studio UI as shown here.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIサービスの紹介文の修正"
}
```

### Explanation
この修正は、AIスタジオにおけるAIサービスの接続に関する記事（connect-ai-services.md）の内容の小規模な更新を示しています。具体的には、以下の変更が行われました：

1. **説明文の修正**: 記事中の文が変更され、AIサービスを試す方法として「モデルカタログカードとプレイグラウンド体験」を通じて無料で利用できることが強調されています。以前の文言は「getting started with AI services」へのリンクを参照していましたが、更新後は直接的な体験方法に焦点を当てています。

2. **情報の明確化**: これは利用者に対して、より具体的な体験を提供するための更新であり、AIサービスを試す際の具体的なアプローチが強調されています。

この変更により、読者がAIサービスの利用に関する理解を深めやすくなっており、利便性が向上しています。

## articles/ai-studio/ai-services/get-started.md{#item-8378f4}

<details>
<summary>Diff</summary>
````diff
@@ -1,47 +0,0 @@
----
-title: Get started with AI services in Azure AI Studio
-titleSuffix: Azure AI Studio
-description: This article describes how to get started with AI services in Azure AI Studio.
-manager: scottpolly
-ms.service: azure-ai-studio
-ms.custom:
-  - build-2024
-ms.topic: how-to
-ms.date: 5/21/2024
-ms.reviewer: eur
-ms.author: eur
-author: eric-urban
----
-
-# Get started with AI services in Azure AI Studio
-
-This article describes how to get started with AI services in [Azure AI Studio](https://ai.azure.com). You can connect to AI services in Azure AI Studio to use AI capabilities such as Azure OpenAI, Speech, Language, Translator, Vision, Document Intelligence, and Content Safety.
-
-Go to the **Home** page and then select **AI Services** from the left pane to explore these services.
-
-:::image type="content" source="../media/ai-services/ai-services-home.png" alt-text="Screenshot of the AI Services page in Azure AI Studio." lightbox="../media/ai-services/ai-services-home.png":::
-
-## Azure AI services in Azure AI Studio
-
-Azure AI services in Azure AI Studio provide a wide range of AI capabilities to help you build intelligent applications. You can use these services to perform a variety of tasks, such as natural language processing, computer vision, speech recognition, and translation.
-
-Azure AI Studio supports the following AI services:
-
-| Service | Description |
-| --- | --- |
-| ![Azure OpenAI Service icon](~/reusable-content/ce-skilling/azure/media/ai-services/azure-openai.svg) [Azure OpenAI](../../ai-services/openai/index.yml) | Perform a wide variety of natural language tasks.<br/><br/>You can connect to Azure OpenAI in several ways in Azure AI Studio. You can use Azure OpenAI in the [assistants playground](../quickstarts/assistants.md) to create and test your own AI assistant. You can also use Azure OpenAI when you [get started building a chat app using the prompt flow SDK](../quickstarts/get-started-code.md).  |
-| ![Content Safety icon](~/reusable-content/ce-skilling/azure/media/ai-services/content-safety.svg) [Content Safety](../../ai-services/content-safety/index.yml) | An AI service that detects unwanted contents.<br/><br/>Go to **Home** > **AI Services** > **Content Safety**. |
-| ![Document Intelligence icon](~/reusable-content/ce-skilling/azure/media/ai-services/document-intelligence.svg) [Document Intelligence](../../ai-services/document-intelligence/index.yml) | Turn documents into intelligent data-driven solutions.<br/><br/>Go to **Home** > **AI Services** > **Vision + Document**. |
-| ![Face icon](~/reusable-content/ce-skilling/azure/media/ai-services/face.svg) [Face](../../ai-services/computer-vision/overview-identity.md) | Detect and identify people and emotions in images.<br/><br/>Go to **Home** > **AI Services** > **Vision + Document**. |
-| ![Language icon](~/reusable-content/ce-skilling/azure/media/ai-services/language.svg) [Language](../../ai-services/language-service/index.yml) | Build apps with industry-leading natural language understanding capabilities.<br/><br/>Go to **Home** > **AI Services** > **Language + Translator**. |
-| ![Speech icon](~/reusable-content/ce-skilling/azure/media/ai-services/speech.svg) [Speech](../../ai-services/speech-service/index.yml) | Give your apps the ability to hear, understand, and even talk to your customers with features like speech to text and text to speech.<br/><br/>Go to **Home** > **AI Services** > **Speech**.<br/><br/>You can also try speech to text and text to speech capabilities in the Azure AI Studio playground. For more information, see [Real-time speech to text](../../ai-services/speech-service/get-started-speech-to-text.md?context=/azure/ai-studio/context/context), and [Pronunciation assessment](../../ai-services/speech-service/pronunciation-assessment-tool.md?context=/azure/ai-studio/context/context). |
-| ![Translator icon](~/reusable-content/ce-skilling/azure/media/ai-services/translator.svg) [Translator](../../ai-services/translator/index.yml) | Use AI-powered translation technology to translate more than 100 in-use, at-risk, and endangered languages and dialects.<br/><br/>Go to **Home** > **AI Services** > **Language + Translator**. |
-| ![Vision icon](~/reusable-content/ce-skilling/azure/media/ai-services/vision.svg) [Vision](../../ai-services/computer-vision/index.yml) | Analyze content in images and videos.<br/><br/>Go to **Home** > **AI Services** > **Vision + Document**. |
-
-For information about more AI services, see the [Azure AI services documentation](../../ai-services/index.yml).
-
-## Related content
-
-- [What are Azure AI services?](../../ai-services/what-are-ai-services.md?context=/azure/ai-studio/context/context)
-- [Azure AI Studio hubs](../concepts/ai-resources.md)
-- [Connections in Azure AI Studio](../concepts/connections.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "AIサービスに関する「始めに」記事の削除"
}
```

### Explanation
この変更は、AIスタジオにおけるAIサービスの「始めに」記事（get-started.md）の削除を示しています。この修正によって、本文全体が削除され、47行の内容が取り消されました。

1. **記事全体の削除**: このリダイレクトは、AIサービスに関する基本的な情報、接続方法、利用可能なサービスのリストなどを含む包括的な説明が削除されたことを意味します。この情報は、Azure AI スタジオでのサービス利用を始めるための重要な参照ポイントでした。

2. **影響**: 記事が削除されたことにより、ユーザーはAIサービスについての基本的なガイダンスを失うことになります。この削除は、関連情報が他の場所に移動したか、あるいは更新される予定である可能性があります。

この変更は、AIスタジオの利用者にとって重要な情報源が取り除かれるため、注意が必要です。今後の構成や情報の提供方法についてのさらなる調整が期待されます。

## articles/ai-studio/how-to/access-on-premises-resources.md{#item-8e3926}

<details>
<summary>Diff</summary>
````diff
@@ -83,7 +83,7 @@ Follow the [Quickstart: Direct web traffic using the portal](/azure/application-
     > - If you are using HTTPS listener with certificate uploaded, make sure the FQDN alias matches with the certificate's CN (Common Name) or SAN (Subject Alternative Name) otherwise HTTPS call will fail with SNI (Server Name Indication).
     > - The provided FQDNs must have at least three labels in the name to properly create the private DNS zone of thee private endpoint for Application Gateway.
     > - The FQDNs field is editable after the private endpoint creation through SDK or CLI. The field is not editable in the Azure portal.
-    > - Dyname sub-resource naming is not supported for the private Frontend IP configuration. The Frontend IP name must be `appGwPrivateFrontendIpIPv4`.
+    > - Dynamic sub-resource naming is not supported for the private Frontend IP configuration. The Frontend IP name must be `appGwPrivateFrontendIpIPv4`.
 
 ### Configure using Python SDK and Azure CLI
 
@@ -109,4 +109,4 @@ For errors related to the Application Gateway connection to your backend resourc
 
 ## Related content
 
-- [Managed virtual network isolation](configure-managed-network.md)
\ No newline at end of file
+- [Managed virtual network isolation](configure-managed-network.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースアクセスガイドの文言修正"
}
```

### Explanation
この変更は、オンプレミスリソースへのアクセスに関する記事（access-on-premises-resources.md）の内容に対する小規模な更新を示しています。具体的には、以下の変更が行われました：

1. **文言の修正**: "Dyname"（誤字）という用語が"Dynamic"に修正されました。これにより、プライベートフロントエンドIP設定に関する明確な説明が提供されるようになりました。これは、用語の正確さを確保するための重要なアップデートです。

2. **関連コンテンツのフォーマット**: 記事の末尾にある関連コンテンツのリストにおいて、改行が追加され、整形式が改善されています。これにより、読みやすさが向上し、関連情報へのアクセスが容易になっています。

総じて、この更新は記事の内容を明確にし、ユーザーが情報をより正確に理解できるように配慮されています。

## articles/ai-studio/how-to/concept-data-privacy.md{#item-af88ce}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: scottpolly
 ms.service: azure-ai-studio
 ms.custom: references_regions, build-2024
 ms.topic: conceptual
-ms.date: 5/21/2024
+ms.date: 10/29/2024
 ms.reviewer: shubhirajMsft
 ms.author: scottpolly
 author: s-polly
@@ -16,6 +16,9 @@ author: s-polly
 
 This article describes how the data that you provide is processed, used, and stored when you deploy models from the model catalog. Also see the [Microsoft Products and Services Data Protection Addendum](https://aka.ms/DPA), which governs data processing by Azure services.
 
+> [!IMPORTANT]
+> For information about responsible AI in Azure OpenAI and AI services, see [Responsible use of AI](../../ai-services/responsible-use-of-ai-overview.md?context=/azure/ai-studio/context/context).
+
 ## What data is processed for models deployed in Azure AI Studio?
 
 When you deploy models in Azure AI Studio, the following types of data are processed to provide the service:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データプライバシーに関する記事の更新"
}
```

### Explanation
この変更は、データプライバシーに関する記事（concept-data-privacy.md）に対して行われた小規模な更新を示しています。具体的な変更点は以下の通りです：

1. **日付の更新**: 記事の最終更新日が「2024年5月21日」から「2024年10月29日」に変更されました。これは、情報が最新であることを反映するための重要な修正です。

2. **新しい重要情報の追加**: 記事内に、「Azure OpenAIおよびAIサービスにおける責任あるAIに関する情報」として、新しい注意事項が追加されました。この部分には、責任あるAIの利用に関する参照リンクも含まれており、利用者が倫理的にAIを使用するためのガイダンスを提供しています。

3. **内容の強化**: 上記の変更により、データプライバシーの観点から、より包括的な情報が提供されるようになりました。この更新は、ユーザーがデータ処理の方法や責任あるAIの使用に関する重要な情報を簡単に見つけられるようにすることを目的としています。

これらの改善により、読者はデータプライバシーに関する理解を深めることができ、Azure AIスタジオの利用においてより良い判断を下すことができるようになります。

## articles/ai-studio/how-to/develop/trace-local-sdk.md{#item-f7dfb5}

<details>
<summary>Diff</summary>
````diff
@@ -9,8 +9,8 @@ ms.custom:
 ms.topic: how-to
 ms.date: 5/21/2024
 ms.reviewer: chenlujiao
-ms.author: sgilley
-author: sdgilley
+ms.author: lagayhar  
+author: lgayhardt
 ---
 
 # How to trace your application with prompt flow SDK | Azure AI Studio
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Trace Local SDKの記事の著者情報修正"
}
```

### Explanation
この変更は、Trace Local SDKに関する記事（trace-local-sdk.md）の著者情報に関する小規模な更新です。具体的な変更点は以下の通りです：

1. **著者情報の更新**: 記事の著者が「sgilley」から「lagayhar」に変更され、名前が「sdgilley」から「lgayhardt」に更新されました。これにより、記事の情報が最新のものとなり、正確なクレジットが反映されるようになります。

2. **日付やメタデータの保持**: 文章の他の部分、特に記事の最終更新日やトピックの指定には変更はありません。この記事は、引き続きユーザーが役立つ情報にアクセスできるように管理されています。

この微調整により、著者の正確性が確保され、読者がその情報を提供した人物に対して正しい認識を持つことができるようになります。この更新は、コンテンツの透明性を高め、信頼性を向上させます。

## articles/ai-studio/how-to/healthcare-ai/deploy-cxrreportgen.md{#item-377d15}

<details>
<summary>Diff</summary>
````diff
@@ -37,20 +37,19 @@ The CXRReportGen model combines a radiology-specific image encoder with a large
 
 ## Prerequisites
 
-[!INCLUDE [shared-ai-studio-and-azure-ml-articles](../../includes/shared-ai-studio-and-azure-ml-articles.md)]
-
-To use CXRReportGen model with Azure AI Studio or Azure Machine Learning studio, you need the following prerequisites:
+To use the CXRReportGen model, you need the following prerequisites:
 
 ### A model deployment
 
 **Deployment to a self-hosted managed compute**
 
-CXRReportGen model can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served. You can deploy the model through the model catalog UI or programmatically.
+CXRReportGen model can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served. You can deploy the model through the catalog UI (in [AI Studio](https://aka.ms/healthcaremodelstudio) or [Azure Machine Learning studio](https://ml.azure.com/model/catalog)) or deploy programmatically.
 
 To __deploy the model through the UI__:
 
-1. Go to the [model card in the catalog](https://aka.ms/cxrreportgenmodelcard). 
-1. On the model's overview page, select __Deploy__. 
+1. Go to the catalog.
+1. Search for _CxrReportGen_ and select the model card.
+1. On the model's overview page, select __Deploy__.
 1. If given the option to choose between serverless API deployment and deployment using a managed compute, select **Managed Compute**.
 1. Fill out the details in the deployment window.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "CXRReportGenモデルの展開手順の改善"
}
```

### Explanation
この変更は、CXRReportGenモデルに関する記事（deploy-cxrreportgen.md）の展開手順において行われた小規模な修正を示しています。具体的な変更点は以下の通りです：

1. **不要な文の削除**: 「Azure AI StudioまたはAzure Machine Learning StudioでCXRReportGenモデルを使用するには、以下の前提条件が必要です」という文から不要な部分が削除され、説明がより簡潔になりました。

2. **手順の明確化**: モデルをUIを通じて展開する手順が明確に整理されており、「モデルカードをカタログ内で探して選択する」というステップが追加されました。これにより、ユーザーが要求される操作をより簡単に理解できるようになります。

3. **リンクの強調**: CXRReportGenモデルがAI StudioやAzure Machine Learning StudioのカタログUIを通じて展開可能であることが明確に記載され、関連リンク（AI StudioやAzure Machine Learning Studioへのリンク）が強調されています。これにより、読者は関連情報にすぐにアクセスできるようになります。

これらの変更により、ユーザーがCXRReportGenモデルを展開する際の手順がより分かりやすくなり、実行しやすくなっています。このアップデートは、読者が記事を通じて求める情報に迅速にアクセスできることを目的としています。

## articles/ai-studio/how-to/healthcare-ai/deploy-medimageinsight.md{#item-e9ab9e}

<details>
<summary>Diff</summary>
````diff
@@ -35,19 +35,18 @@ An embedding model is capable of serving as the basis of many different solution
 
 ## Prerequisites
 
-[!INCLUDE [shared-ai-studio-and-azure-ml-articles](../../includes/shared-ai-studio-and-azure-ml-articles.md)]
-
-To use MedImageInsight models with Azure AI Studio or Azure Machine Learning studio, you need the following prerequisites:
+To use the MedImageInsight model, you need the following prerequisites:
 
 ### A model deployment
 
 **Deployment to a self-hosted managed compute**
 
-MedImageInsight model can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served. You can deploy the model through the model catalog UI or programmatically.
+MedImageInsight model can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served. You can deploy the model through the catalog UI (in [AI Studio](https://aka.ms/healthcaremodelstudio) or [Azure Machine Learning studio](https://ml.azure.com/model/catalog)) or deploy programmatically.
 
 To __deploy the model through the UI__:
 
-1. Go to the [model card in the catalog](https://aka.ms/mi2modelcard). 
+1. Go to the catalog.
+1. Search for _MedImageInsight_ and select the model card.
 1. On the model's overview page, select __Deploy__. 
 1. If given the option to choose between serverless API deployment and deployment using a managed compute, select **Managed Compute**.
 1. Fill out the details in the deployment window.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MedImageInsightモデルの展開手順の改善"
}
```

### Explanation
この変更は、MedImageInsightモデルに関する記事（deploy-medimageinsight.md）の展開手順に関する小規模な修正を示しています。具体的な変更点は以下の通りです：

1. **不要な文の削除**: 文章から「Azure AI StudioまたはAzure Machine Learning StudioでMedImageInsightモデルを使用するには、以下の前提条件が必要です」という文が削除され、必要な情報がより簡潔に整理されました。

2. **手順の明確化**: モデルをUIを通じて展開する手順がより明確になり、ユーザーが「MedImageInsight」をカタログで検索してモデルカードを選択するという新しいステップが追加されています。これにより、より明瞭な指示が提供されています。

3. **リンクの強調**: MedImageInsightモデルの展開に関する情報がAI StudioやAzure Machine Learning Studioへの関連リンクと共に明示されています。これにより、読者が関連情報に迅速にアクセス可能になります。

これらの変更により、ユーザーがMedImageInsightモデルを展開する際の手順が簡略化され、実行しやすくなっています。このアップデートは、読者が必要な情報を素早く見つけ出せるようにすることを目的としています。

## articles/ai-studio/how-to/healthcare-ai/deploy-medimageparse.md{#item-611e84}

<details>
<summary>Diff</summary>
````diff
@@ -38,20 +38,19 @@ Remarkably, the segmentation masks and textual descriptions were achieved by usi
 
 ## Prerequisites
 
-[!INCLUDE [shared-ai-studio-and-azure-ml-articles](../../includes/shared-ai-studio-and-azure-ml-articles.md)]
-
-To use MedImageParse model with Azure AI Studio or Azure Machine Learning studio, you need the following prerequisites:
+To use the MedImageParse model, you need the following prerequisites:
 
 ### A model deployment
 
 **Deployment to a self-hosted managed compute**
 
-MedImageParse model can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served. You can deploy the model through the model catalog UI or programmatically. 
+MedImageParse model can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served. You can deploy the model through the catalog UI (in [AI Studio](https://aka.ms/healthcaremodelstudio) or [Azure Machine Learning studio](https://ml.azure.com/model/catalog)) or deploy programmatically.
 
 To __deploy the model through the UI__:
 
-1. Go to the [model card in the catalog](https://aka.ms/medimageparsemodelcard). 
-1. On the model's overview page, select __Deploy__. 
+1. Go to the catalog.
+1. Search for _MedImageParse_ and select the model card.
+1. On the model's overview page, select __Deploy__.
 1. If given the option to choose between serverless API deployment and deployment using a managed compute, select **Managed Compute**.
 1. Fill out the details in the deployment window.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MedImageParseモデルの展開手順の改善"
}
```

### Explanation
この変更は、MedImageParseモデルに関する記事（deploy-medimageparse.md）の展開手順に関する小規模な修正を示しています。具体的な変更点は以下の通りです：

1. **不要な文の削除**: 「Azure AI StudioまたはAzure Machine Learning StudioでMedImageParseモデルを使用するには、以下の前提条件が必要です」という文が削除され、情報がより簡潔になりました。

2. **手順の明確化**: モデルをUIを通じて展開する手順が改善されており、ユーザーが「MedImageParse」をカタログで検索してモデルカードを選択するという新しいステップが追加されました。これにより、手順がより明確になり、実行が容易になります。

3. **リンクの強調**: MedImageParseモデルの展開方法に関する情報が、AI StudioやAzure Machine Learning Studioへの関連リンクと共に明示されており、読者が関連情報に迅速にアクセスできるようになっています。

これらの変更により、ユーザーがMedImageParseモデルを展開する際の手順が簡単になり、必要な情報を迅速に得られることを目的としています。このアップデートは、読者がよりスムーズに作業を行えるようにするためのものです。

## articles/ai-studio/how-to/healthcare-ai/healthcare-ai-models.md{#item-12fcfc}

<details>
<summary>Diff</summary>
````diff
@@ -26,9 +26,7 @@ The healthcare industry is undergoing a revolutionary transformation driven by t
 
 :::image type="content" source="../../media/how-to/healthcare-ai/connect-modalities.gif" alt-text="Models that reason about various modalities come together to support discover, development and delivery of healthcare":::
 
-The [Azure AI model catalog](../model-catalog-overview.md) provides healthcare foundation models that facilitate AI-powered analysis of various medical data types and expand well beyond medical text comprehension into the multimodal reasoning about medical data. These AI models can integrate and analyze data from diverse sources that come in various modalities, such as medical imaging, genomics, clinical records, and other structured and unstructured data sources. The models also span several healthcare fields like dermatology, ophthalmology, radiology, and pathology. 
-
-[!INCLUDE [shared-ai-studio-and-azure-ml-articles](../../includes/shared-ai-studio-and-azure-ml-articles.md)]
+The Azure AI model catalog available in [AI Studio](../model-catalog-overview.md) and [Azure Machine Learning studio](../../../machine-learning/concept-model-catalog.md) provides healthcare foundation models that facilitate AI-powered analysis of various medical data types and expand well beyond medical text comprehension into the multimodal reasoning about medical data. These AI models can integrate and analyze data from diverse sources that come in various modalities, such as medical imaging, genomics, clinical records, and other structured and unstructured data sources. The models also span several healthcare fields like dermatology, ophthalmology, radiology, and pathology. 
 
 ## Microsoft first-party models
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AIモデルカタログのリンク修正"
}
```

### Explanation
この変更は、医療AIモデルに関する記事（healthcare-ai-models.md）内の情報を少し改善するもので、主にリンクの修正が行われています。具体的な変更点は以下の通りです：

1. **リンクの修正**: 「Azure AIモデルカタログ」の説明が修正され、AI StudioとAzure Machine Learning Studioに関連する新たなリンクが挿入されています。これにより、読者が必要なリソースに簡単にアクセスできるようになっています。

2. **不要なインクルードの削除**: 共通のインクルード文（[!INCLUDE [shared-ai-studio-and-azure-ml-articles]）が削除され、文章が簡潔になりました。

3. **文章の簡素化**: 修正されたリンクと情報によって、医療データの分析に関するAIモデルの説明がより明確かつ一貫性を持ったものになっています。

これにより、読者はAzure AIモデルカタログにより効果的にアクセスし、医療データに対するAIの利用方法についての理解を深めることができるようになります。このアップデートは、情報の関連性や可読性を向上させることを目的としています。

## articles/ai-studio/includes/shared-ai-studio-and-azure-ml-articles.md{#item-c1f692}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +0,0 @@
----
-title: include file
-description: include file
-author: msakande
-ms.author: mopeakande
-ms.service: azure-ai-studio
-ms.topic: include
-ms.date: 10/21/2024
-ms.custom: include file
----
-
-> [!NOTE]
-> This article applies to both [Azure AI Studio](https://ai.azure.com/) and [Azure Machine Learning studio](https://ml.azure.com/). To learn more about the differences between these two products and which one to use, see [AI Studio or Azure Machine Learning: Which experience should I choose?](/ai/ai-studio-experiences-overview).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "共有インクルードファイルの削除"
}
```

### Explanation
この変更は、共有インクルードファイル（shared-ai-studio-and-azure-ml-articles.md）が完全に削除されたことを示しています。このインクルードファイルは、Azure AI StudioとAzure Machine Learning Studioに関連する情報や注記を含んでいました。具体的な変更点は以下の通りです：

1. **ファイルの削除**: 全ての内容が削除され、ファイル自体が存在しなくなりました。これにより、このインクルード文書を参照している他のドキュメントは影響を受ける可能性があります。

2. **情報の喪失**: 削除された内容には、2つの製品（Azure AI StudioとAzure Machine Learning Studio）間の違いや使用方法に関する重要な情報が含まれていました。この情報が失われることで、読者が正しい選択をする際の手助けが減少する可能性があります。

この変更は破壊的であり、他の文書に依存している場合、メンテナンスや更新が必要になるでしょう。また、Azure AI StudioとAzure Machine Learning Studioのユーザーにとって重要な情報を即時に得る手段が失われることになります。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ items:
     href: faq.yml
   - name: What is Azure OpenAI?
     href: ../ai-services/openai/overview.md?context=/azure/ai-studio/context/context
-  - name: "AI Studio or Azure Machine Learning studio: Which should I choose?"
+  - name: Which studio should I choose?
     href: /ai/ai-studio-experiences-overview?context=/azure/ai-studio/context/context
 - name: Quickstarts
   items:
@@ -47,70 +47,42 @@ items:
 - name: How-to
   expanded: true
   items:
-  - name: Create hubs and projects
+  - name: Azure OpenAI and AI services
     items:
-    - name: Hubs and projects overview
-      href: concepts/ai-resources.md
-    - name: Create your first hub
-      href: how-to/create-azure-ai-resource.md
-    - name: Create a hub using the Azure Machine Learning SDK and CLI
-      href: how-to/develop/create-hub-project-sdk.md
-    - name: Create a hub with custom security
+    - name: What is Azure OpenAI?
+      href: ../ai-services/openai/overview.md?context=/azure/ai-studio/context/context
+      displayName: cognitive
+    - name: What are AI services?
+      href: ../ai-services/what-are-ai-services.md?context=/azure/ai-studio/context/context
+    - name: Azure OpenAI
       items:
-      - name: Create a hub in the Azure portal
-        href: how-to/create-secure-ai-hub.md
-      - name: Create a hub from template
-        href: how-to/create-azure-ai-hub-template.md
-        displayName: code
-      - name: Create a hub using Terraform
-        href: how-to/create-hub-terraform.md
-    - name: Create a project
-      href: how-to/create-projects.md
-    - name: Create and manage compute
-      href: how-to/create-manage-compute.md
-  - name: Connect to services and resources
-    items:
-    - name: Connections overview
-      href: concepts/connections.md
-    - name: Create a connection
-      href: how-to/connections-add.md
-    - name: Create a connection using the Azure Machine Learning SDK
-      href: how-to/develop/connections-add-sdk.md
-      displayName: code
-    - name: Azure AI services connections
+      - name: Deploy Azure OpenAI models
+        href: how-to/deploy-models-openai.md
+      - name: Fine-tune Azure OpenAI models
+        href: ../ai-services/openai/how-to/fine-tuning.md?context=/azure/ai-studio/context/context
+      - name: Get started with Assistants and code interpreter in the playground
+        href: ../ai-services/openai/assistants-quickstart.md?context=/azure/ai-studio/context/context
+      - name: Analyze images and video with GPT-4 for Vision in the playground
+        href: quickstarts/multimodal-vision.md
+      - name: Use your image data with Azure OpenAI
+        href: how-to/data-image-add.md
+        displayName: vision, gpt, turbo
+    - name: Azure AI Content Safety
       items:
-      - name: What are AI services?
-        href: ../ai-services/what-are-ai-services.md?context=/azure/ai-studio/context/context
-        displayName: cognitive
-      - name: Get started with AI services in AI Studio
-        href: ai-services/get-started.md
-      - name: Connect AI services in AI Studio
-        href: ai-services/connect-ai-services.md
-      - name: Azure OpenAI
-        items:
-        - name: Get started with Assistants and code interpreter in the playground
-          href: ../ai-services/openai/assistants-quickstart.md?context=/azure/ai-studio/context/context
-        - name: Analyze images and video with GPT-4 for Vision in the playground
-          href: quickstarts/multimodal-vision.md
-        - name: Use your image data with Azure OpenAI
-          href: how-to/data-image-add.md
-          displayName: vision, gpt, turbo
-      - name: Azure AI Content Safety
-        items:
-        - name: Content filtering
-          href: concepts/content-filtering.md
-        - name: Prevent input attacks with Prompt Shields
-          href: how-to/prompt-shields.md
-        - name: Detect groundedness in chat responses
-          href: how-to/groundedness.md
-      - name: Speech
-        items:
-        - name: Real-time speech to text
-          href: ../ai-services/speech-service/get-started-speech-to-text.md?context=/azure/ai-studio/context/context
-        - name: Pronunciation assessment
-          href: ../ai-services/speech-service/pronunciation-assessment-tool.md?context=/azure/ai-studio/context/context
-        - name: Hear and speak with chat in the playground
-          href: quickstarts/hear-speak-playground.md
+      - name: Content filtering
+        href: concepts/content-filtering.md
+      - name: Prevent input attacks with Prompt Shields
+        href: how-to/prompt-shields.md
+      - name: Detect groundedness in chat responses
+        href: how-to/groundedness.md
+    - name: Speech
+      items:
+      - name: Real-time speech to text
+        href: ../ai-services/speech-service/get-started-speech-to-text.md?context=/azure/ai-studio/context/context
+      - name: Pronunciation assessment
+        href: ../ai-services/speech-service/pronunciation-assessment-tool.md?context=/azure/ai-studio/context/context
+      - name: Hear and speak with chat in the playground
+        href: quickstarts/hear-speak-playground.md
   - name: Explore and select AI models
     items:
     - name: Model catalog
@@ -125,7 +97,7 @@ items:
       href: concepts/concept-model-distillation.md
     - name: Azure OpenAI models
       items:
-      - name: Azure OpenAI models
+      - name: Deploy Azure OpenAI models
         href: how-to/deploy-models-openai.md
       - name: Fine-tune Azure OpenAI models
         href: ../ai-services/openai/how-to/fine-tuning.md?context=/azure/ai-studio/context/context
@@ -212,6 +184,38 @@ items:
       - name: Managed compute
         href: how-to/deploy-models-managed.md
         displayName: endpoint, online, SDK, CLI
+  - name: Create hubs and projects
+    items:
+    - name: Hubs and projects overview
+      href: concepts/ai-resources.md
+    - name: Create your first hub
+      href: how-to/create-azure-ai-resource.md
+    - name: Create a hub using the Azure Machine Learning SDK and CLI
+      href: how-to/develop/create-hub-project-sdk.md
+    - name: Create a hub with custom security
+      items:
+      - name: Create a hub in the Azure portal
+        href: how-to/create-secure-ai-hub.md
+      - name: Create a hub from template
+        href: how-to/create-azure-ai-hub-template.md
+        displayName: code
+      - name: Create a hub using Terraform
+        href: how-to/create-hub-terraform.md
+    - name: Create a project
+      href: how-to/create-projects.md
+    - name: Create and manage compute
+      href: how-to/create-manage-compute.md
+  - name: Connect to services and resources
+    items:
+    - name: Connections overview
+      href: concepts/connections.md
+    - name: Create a connection
+      href: how-to/connections-add.md
+    - name: Create a connection using the Azure Machine Learning SDK
+      href: how-to/develop/connections-add-sdk.md
+    - name: Connect AI services in AI Studio
+      href: ai-services/connect-ai-services.md
+      displayName: code
   - name: Data for your generative AI app
     items:
     - name: Overview of retrieval augmented generation (RAG)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新と整理"
}
```

### Explanation
この変更は、AI Studioの目次ファイル（toc.yml）の大幅な更新と整理を示しています。主な変更点は以下の通りです：

1. **項目名の変更**: 一部の項目名がより明確にするために簡略化または再命名されています。たとえば、「AI StudioまたはAzure Machine Learning studio: どちらを選ぶべきか？」が「どのスタジオを選ぶべきか？」に変更されました。

2. **新しいセクションの追加**: 新しい項目として「Azure OpenAIとAIサービス」や「ハブとプロジェクトの作成」などが追加され、AIサービスに関する情報が強化されています。

3. **無駄な項目の削除**: 一部の古い項目が削除され、新しい情報や手順が追加されています。これにより目次がより整理された形になり、必要な情報へのアクセスが容易になっています。

4. **リンクの修正と更新**: 各項目に関連するリンクが更新され、新しい情報が反映されるようになっています。特に、Azure OpenAIに関連するチュートリアルが強調され、最新の機能や手順に基づいています。

このアップデートは、読者がAI Studioおよび関連するAIサービスに関する情報をよりスムーズに見つけられるよう設計されています。全体として、目次はより使いやすく、一貫性のある情報提供を目指した内容になりました。


