---
date: '2024-12-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:51f1731...MicrosoftDocs:fffd4c5
summary: このコード変更では、Azure AIサービスに関するドキュメントが更新され、機能が改善されました。具体的には、モデルのライフサイクルと引退に関する新しいドキュメントが追加され、ユーザーが必要な情報にアクセスしやすくなるように関連リンクが強化されました。特に破壊的な変更はなく、従来のドキュメントの照会方法がやや変更される可能性があります。全体として、これらの更新はユーザビリティの向上を目的としており、データサイエンティストにとって有用な情報を提供します。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:51f1731...MicrosoftDocs:fffd4c5){target="_blank"}

# Highlights
このコード変更では、Azure AIサービスと関連ドキュメントに一連の更新や追加が行われ、機能改善が図られています。

## New features
- Azure AIモデルカタログにおけるモデルのライフサイクルと引退に関する新しいドキュメントが追加されました。

## Breaking changes
- 特に破壊的な変更は見られませんが、リンクの追加やドキュメントの更新により、従来のドキュメント参照方法が若干変わります。

## Other updates
- AI Foundryポータルのリンクが追加され、ユーザーがアクセスしやすくなりました。
- Mistralモデルやモデルカタログのドキュメントの関連コンテンツが強化されました。
- AIスタジオのドキュメント目次が更新され、新しい項目が追加されました。

# Insights
この一連のドキュメント更新は、ユーザビリティの向上と情報の入手の迅速性を目的としています。各ドキュメントは、関連性のあるリンクを追加することで、ユーザーが必要な情報を簡単に見つけ、アクセスできるように設計されています。特に、Azure AIモデルカタログにおけるモデルのライフサイクル管理に関する新しいドキュメントは、データサイエンティストにとって非常に有用で、モデル管理の効率化に寄与します。

モデルの廃止や引退に関する具体的なガイドラインや通知方法が明確に説明されており、ユーザーがこれからのAIモデル管理戦略を適切に設計できるように支援しています。また、新しく追加された目次項目や関連コンテンツのリンクにより、ドキュメント内を効率的に移動できる利便性が向上しています。

これらの更新を通じて、Azure AIのユーザーエクスペリエンスが一層充実し、効率的な作業環境が提供されることになります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [connect-ai-services.md](#item-da4289) | minor update | AIサービス接続に関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [model-lifecycle-and-retirement.md](#item-31c9c5) | new feature | Azure AIモデルカタログにおけるモデルのライフサイクルと引退に関する新しいドキュメント | added | 75 | 0 | 75 | 
| [deploy-models-mistral.md](#item-487a41) | minor update | Mistralモデルのデプロイに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [model-catalog-overview.md](#item-278001) | minor update | モデルカタログの概要に関するドキュメントの更新 | modified | 1 | 0 | 1 | 
| [toc.yml](#item-2745cd) | minor update | AIスタジオの目次に関する更新 | modified | 4 | 0 | 4 | 


# Modified Contents
## articles/ai-studio/ai-services/how-to/connect-ai-services.md{#item-da4289}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ author: eric-urban
 
 # How to use Azure AI services in AI Foundry portal
 
-You might have existing resources for Azure AI services that you used in the old studios such as Azure OpenAI Studio or Speech Studio. You can pick up where you left off by using your existing resources in AI Foundry portal.
+You might have existing resources for Azure AI services that you used in the old studios such as Azure OpenAI Studio or Speech Studio. You can pick up where you left off by using your existing resources in the [Azure AI Foundry portal](https://ai.azure.com).
 
 This article describes how to use new or existing Azure AI services resources in an AI Foundry project.
 
@@ -33,7 +33,7 @@ Depending on the AI service and model you want to use, you can use them in AI Fo
 
 ## Bring your existing Azure AI services resources into a project
 
-Let's look at two ways to connect Azure AI services resources to a project:
+Let's look at two ways to connect Azure AI services resources to an Azure AI Foundry project:
 
 - [When you create a project](#connect-azure-ai-services-when-you-create-a-project-for-the-first-time)
 - [After you create a project](#connect-azure-ai-services-after-you-create-a-project)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIサービス接続に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AIサービスとAI Foundryポータルに関するドキュメントのテキストを更新するもので、具体的にはリンクの追加と専門用語の統一が行われました。 

特に、以前の記述では「AI Foundryポータル」としていた部分が、リンクを加えたことで「[Azure AI Foundryポータル](https://ai.azure.com)」と変更され、ユーザーが直接ポータルにアクセスできるようになりました。また、「AI Foundryプロジェクト」とすることで、プロジェクトの明確なコンテキストが提供されています。

この更新は、情報の正確性と利用者に対する便宜の向上を目的としており、全体として文書の明確さを改善しています。

## articles/ai-studio/concepts/model-lifecycle-and-retirement.md{#item-31c9c5}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,75 @@
+---
+title: Deprecation and retirement for models in Azure AI model catalog
+titleSuffix: Azure AI Foundry
+description: Learn about the lifecycle stages, deprecation, and retirement for models in the Azure AI model catalog.
+manager: scottpolly
+ms.service: azure-ai-studio
+ms.topic: concept-article
+ms.date: 11/22/2024
+ms.author: mopeakande
+author: msakande
+ms.reviewer: kritifaujdar
+reviewer: fkriti
+
+#Customer intent: As a data scientist, I want to learn about the lifecycle of models that are available in the model catalog.
+---
+
+# Model deprecation and retirement in Azure AI model catalog
+
+Models in the model catalog are continually refreshed with newer and more capable models. As part of this process, model providers might deprecate and retire their older models, and you might need to update your applications to use a newer model. This document communicates information about the model lifecycle and deprecation timelines and explains how you're informed of model lifecycle stages.
+
+> [!IMPORTANT]
+> This article describes deprecation and retirement only for models that can be deployed to __serverless APIs__, not managed compute. To learn more about the differences between deployment to serverless APIs and managed computes, see [Model catalog and collections in Azure AI Foundry portal](../how-to/model-catalog-overview.md).
+
+> [!NOTE]
+> Azure OpenAI models in the model catalog are provided through Azure OpenAI Service. For information about Azure Open AI model deprecation and retirement, see the [Azure OpenAI service product documentation](/azure/ai-services/openai/concepts/model-retirements).
+
+## Model lifecycle stages
+
+Models in the model catalog belong to one of these stages:
+
+- Preview
+- Generally available
+- Legacy
+- Deprecated
+- Retired
+
+### Preview
+
+Models labeled _Preview_ are experimental in nature. A model's weights, runtime, and API schema can change while the model is in preview. Models in preview aren't guaranteed to become generally available. Models in preview have a _Preview_ label next to their name in the model catalog.  
+
+### Generally available
+
+This stage is the default model stage. Models that don't include a lifecycle label next to their name are generally available and suitable for use in production environments. In this stage, model weights and APIs are fixed. However, model containers or runtimes with vulnerabilities might get patched, but patches won't affect model outputs.  
+ 
+### Legacy
+
+Models labeled _Legacy_ are intended for deprecation. You should plan to move to a different model, such as a new, improved model that might be available in the same model family. While a model is in the legacy stage, existing deployments of the model continue to work, and you can create new deployments of the model until the deprecation date.
+
+### Deprecated
+
+Models labeled _Deprecated_ are no longer available for new deployments. You can't create any new deployments for the model; however, existing deployments continue to work until the retirement date.
+
+### Retired
+
+Models labeled _Retired_ are no longer available for use. You can't create new deployments, and attempts to use existing deployments return `<return code>` errors.
+
+
+## Notifications
+
+- Models are labeled as _Legacy_ and remain in the legacy state for at least 30 days before being moved to the deprecated state. During this notification period, you may create new deployments as you prepare for deprecation and retirement.
+
+- Models are labeled _Deprecated_ and remain in the deprecated state for at least 90 days before being moved to the retired state. During this notification period, you can migrate any existing deployments to newer or replacement models.
+
+- Members of the _owner_, _contributor_, _reader_, monitoring contributor_, and _monitoring reader_ roles for each Azure subscription with a serverless API model deployment receive a notification when a model deprecation is announced. The notification contains the dates when the model enters legacy, deprecated, and retired states. The notification might provide information about possible replacement model options, if applicable.
+
+
+
+| Model provider | Model | Legacy date | Deprecation date | Retirement date | Suggested replacement model |
+| ---- | ---- | ---- | --- | ---- | --- |
+| Mistral AI | [Mistral-large](https://aka.ms/azureai/landing/Mistral-Large) | December 15, 2024 | January 15, 2025 | April 15, 2025 | [Mistral-large-2407](https://aka.ms/azureai/landing/Mistral-Large-2407) |
+
+## Related content
+
+- [Model catalog and collections in Azure AI Foundry portal](../how-to/model-catalog-overview.md)
+- [Data, privacy, and security for use of models through the model catalog in AI Foundry portal](../how-to/concept-data-privacy.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AIモデルカタログにおけるモデルのライフサイクルと引退に関する新しいドキュメント"
}
```

### Explanation
この更新は、Azure AIモデルカタログにおけるモデルのライフサイクルおよび引退に関する新しいドキュメントが追加されたことを示しています。このドキュメントでは、モデルの廃止や引退のプロセス、通知方法が詳細に説明されています。

具体的には、モデルの各ライフサイクルの段階（プレビュー、一般提供、レガシー、廃止、引退）が紹介され、各段階におけるモデルの使用に関するガイドラインが提供されています。また、モデルの廃止と引退に関する重要なタイムラインや、ユーザーへの通知方法、および具体的なモデルの例が含まれています。

この情報は、データサイエンティストがモデルカタログ内のモデルを利用する際のインサイトを提供するとともに、ライフサイクル管理に必要な理解を深めるためのものです。新しいドキュメントによって、ユーザーはモデルの廃止や引退に関して適切に準備を進めることができます。

## articles/ai-studio/how-to/deploy-models-mistral.md{#item-487a41}

<details>
<summary>Diff</summary>
````diff
@@ -2213,9 +2213,9 @@ For more information on how to track costs, see [Monitor costs for models offere
 
 ## Related content
 
-
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
+* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Model deprecation and retirement in Azure AI model catalog](../concepts/model-lifecycle-and-retirement.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
 * [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralモデルのデプロイに関するドキュメントの更新"
}
```

### Explanation
この変更は、Mistralモデルのデプロイに関するドキュメントの「関連コンテンツ」セクションに新しいリンクが追加されたことを示しています。具体的には、Azure AIモデルカタログにおけるモデルの廃止と引退に関するドキュメントへのリンクが追加され、利用者にとって重要な情報を提供することを目的としています。

修正内容としては、関連コンテンツリストにおいて新たに「[モデルの廃止と引退に関するドキュメント](../concepts/model-lifecycle-and-retirement.md)」が追加され、特にMistralモデルをデプロイする際のコンテキストで役立つ情報が提供されるようになりました。この更新により、ユーザーはモデルのライフサイクルに関する理解を深めつつ、より効果的にモデルを活用できるようになります。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -188,3 +188,4 @@ To set the public network access flag for the AI Foundry hub:
 ## Related content
 
 * [Explore foundation models in Azure AI Foundry portal](models-foundation-azure-ai.md)
+* [Model deprecation and retirement in Azure AI model catalog](../concepts/model-lifecycle-and-retirement.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルカタログの概要に関するドキュメントの更新"
}
```

### Explanation
この変更は、モデルカタログの概要に関するドキュメントに「関連コンテンツ」セクションが更新されたことを示しています。具体的には、モデルの廃止と引退に関するドキュメントへのリンクが追加されました。

これにより、ユーザーはモデルカタログの使用に関して、モデルの廃止や引退のプロセスについてより多くの情報を得ることができるようになります。追加されたリンクは「[モデルの廃止と引退に関するドキュメント](../concepts/model-lifecycle-and-retirement.md)」であり、これにより利用者はモデルのライフサイクルに関する重要な情報に簡単にアクセスできるようになります。この更新は、モデルを効果的に管理するための重要なリソースを提供します。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -91,6 +91,10 @@ items:
       href: how-to/model-catalog-overview.md
     - name: Data, privacy, and security for Model Catalog
       href: how-to/concept-data-privacy.md
+    - name: Model lifecycle and retirement
+      href: concepts/model-lifecycle-and-retirement.md
+    - name: Model benchmarks
+      href: how-to/model-benchmarks.md
     - name: Model benchmarking
       items:
       - name: Model benchmarks
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIスタジオの目次に関する更新"
}
```

### Explanation
この変更は、AIスタジオに関するドキュメントの目次（toc.yml）に新しい項目を追加したことを示しています。具体的には、「モデルライフサイクルと引退」および「モデルベンチマーク」という2つの新しいリンクが追加されました。

これにより、利用者はモデルのライフサイクル管理や廃止に関する重要な情報や、モデルのベンチマークに関する資料に容易にアクセスできるようになります。追加された項目は以下の通りです：

- モデルライフサイクルと引退（リンク先: concepts/model-lifecycle-and-retirement.md）
- モデルベンチマーク（リンク先: how-to/model-benchmarks.md）

この更新により、ユーザーはドキュメントの関連コンテンツをより効率的に探索できるようになり、必要な情報を迅速に見つけることができるようになります。


