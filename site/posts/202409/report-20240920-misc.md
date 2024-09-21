---
date: '2024-09-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e496207...MicrosoftDocs:655e817
summary: |-
  ## 概要
  今回のコード変更では、文書の内容がより理解しやすく、利用しやすくなるようにマイナーなアップデートが行われました。主な新機能としては、`model-catalog-overview.md`の表現の一貫性の強化や、`toc.yml`の目次の再構成を含みます。また、重要な変更点には用語の統一があり、他にもAPIやネットワーク設定の強化や新しいセクションの追加が行われました。全体として、Azure AI Studioのユーザー体験が向上しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e496207...MicrosoftDocs:655e817){target="_blank"}

# ハイライト
今回のコード変更において、主な新機能および重要な変更点をまとめます。

## 新機能
1. `model-catalog-overview.md`の内容が更新され、表現の一貫性が強化されました。
2. `toc.yml`の目次が再構成され、新しいセクションや項目が追加されました。

## 重要な変更点
1. `managed online endpoints`の表記が`managed compute`に変更されました。

## その他の更新
1. APIやネットワーク設定に関するセクションが強化されました。
2. 新たに「Connect to external resources」セクションが追加されました。

# インサイト
このコードの変更は、文書の内容をより理解しやすく、利用しやすくするためのマイナーアップデートです。具体的な変更点に注目しながら、その背景と意図を以下に詳述します。

## 文書の統一と専門用語の修正
今回の`model-catalog-overview.md`の更新では、特に以下の変更が目立ちます。

1. **表現の一貫性**:
    - 以前の文書では「managed online endpoints」という用語が用いられていましたが、これが「managed compute」に統一されました。この変更は、用語の一貫性を図るためです。同じコンセプトや機能について異なる用語が使われると、読者が混乱する可能性が高まります。したがって、特定の概念に対して一つの用語を統一して使うことは、理解しやすさを向上させるために重要です。

2. **APIやネットワーク設定セクションの強化**:
    - 文書の具体的な指示が強化され、読者にとってわかりやすい内容になりました。特に、Azureでのモデルのデプロイメントに関する詳細な指示が追加されており、ユーザーが具体的な手順を踏む際の道しるべとなっています。

## 目次の組織化と新規追加
`toc.yml`の更新では、目次の構造が見直され、新たなセクションが追加されました。特に注目すべき点を以下に示します。

1. **項目の明確化**:
    - 「AI Studio or AML: Which should I choose?」が「AI Studio versus AML studio」に変更されました。この表現変更により、ユーザーは異なるスタジオの比較がより簡単に行えます。文書タイトルは、その内容が一目でわかるようにすることが重要です。

2. **新セクションの追加**:
    - 「Connect to external resources」という新しいセクションが追加され、複数のサブ項目が新設されました。このセクションは、サービスやリソースとの接続方法に関する情報を提供します。これにより、ユーザーは必要な情報に迅速にアクセスでき、サービスの利用が容易になります。

今回の変更は、一貫性とユーザビリティを向上させるためのものであり、結果としてAzure AI Studioのユーザー体験が大幅に改善されています。最新の情報と整理された目次により、Azure AI Studioを最大限に活用するための資料がさらに充実しました。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-catalog-overview.md](#item-278001) | minor update | モデルカタログの概要の文書修正 | modified | 11 | 11 | 22 | 
| [toc.yml](#item-2745cd) | minor update | AIスタジオの目次更新 | modified | 44 | 44 | 88 | 


# Modified Contents
## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -57,10 +57,10 @@ The deployment options and features available for each model vary, as described
 
 Features | Managed compute | Serverless API (pay-as-you-go)
 --|--|--
-Deployment experience and billing | Model weights are deployed to dedicated virtual machines with managed online endpoints. A managed online endpoint, which can have one or more deployments, makes available a REST API for inference. You're billed for the virtual machine core hours that the deployments use. | Access to models is through a deployment that provisions an API to access the model. The API provides access to the model that Microsoft hosts and manages, for inference. You're billed for inputs and outputs to the APIs, typically in tokens. Pricing information is provided before you deploy.
+Deployment experience and billing | Model weights are deployed to dedicated virtual machines with managed compute. A managed compute, which can have one or more deployments, makes available a REST API for inference. You're billed for the virtual machine core hours that the deployments use. | Access to models is through a deployment that provisions an API to access the model. The API provides access to the model that Microsoft hosts and manages, for inference. You're billed for inputs and outputs to the APIs, typically in tokens. Pricing information is provided before you deploy.
 API authentication | Keys and Microsoft Entra authentication. | Keys only.  
 Content safety | Use Azure AI Content Safety service APIs. | Azure AI Content Safety filters are available integrated with inference APIs. Azure AI Content Safety filters are billed separately.
-Network isolation | [Configure managed networks for Azure AI Studio hubs](configure-managed-network.md).  | Endpoints follow your hub's public network access (PNA) flag setting. For more information, see the [Network isolation for models deployed via Serverless APIs](#network-isolation-for-models-deployed-via-serverless-apis) section later in this article.
+Network isolation | [Configure managed networks for Azure AI Studio hubs](configure-managed-network.md).  | Managed compute follow your hub's public network access (PNA) flag setting. For more information, see the [Network isolation for models deployed via Serverless APIs](#network-isolation-for-models-deployed-via-serverless-apis) section later in this article.
 
 Model | Managed compute | Serverless API (pay-as-you-go)
 --|--|--
@@ -74,7 +74,7 @@ Other models | Available | Not available
 
 <!-- docutune:enable -->
 
-:::image type="content" source="../media/explore/platform-service-cycle.png" alt-text="Diagram that shows models as a service and the service cycle of real-time endpoints." lightbox="../media/explore/platform-service-cycle.png":::
+:::image type="content" source="../media/explore/platform-service-cycle.png" alt-text="Diagram that shows models as a service and the service cycle of managed computes." lightbox="../media/explore/platform-service-cycle.png":::
 
 ## Managed compute
 
@@ -94,7 +94,7 @@ The registries build on top of a highly scalable and enterprise-ready infrastruc
 
 ### Deployment of models for inference with managed compute
 
-Models available for deployment to managed compute can be deployed to Azure Machine Learning online endpoints for real-time inference. Deploying to managed compute requires you to have a virtual machine quota in your Azure subscription for the specific products that you need to optimally run the model. Some models allow you to deploy to a [temporarily shared quota for model testing](deploy-models-open.md).
+Models available for deployment to managed compute can be deployed to Azure Machine Learning managed compute for real-time inference. Deploying to managed compute requires you to have a virtual machine quota in your Azure subscription for the specific products that you need to optimally run the model. Some models allow you to deploy to a [temporarily shared quota for model testing](deploy-models-open.md).
 
 Learn more about deploying models:
 
@@ -151,25 +151,25 @@ Pay-as-you-go billing is available only to users whose Azure subscription belong
 
 ### Network isolation for models deployed via serverless APIs
 
-Endpoints for models deployed as serverless APIs follow the PNA flag setting of the AI Studio hub that has the project in which the deployment exists. To help secure your MaaS endpoint, disable the PNA flag on your AI Studio hub. You can help secure inbound communication from a client to your endpoint by using a private endpoint for the hub.
+Managed computes for models deployed as serverless APIs follow the public network access flag setting of the AI Studio hub that has the project in which the deployment exists. To help secure your managed compute, disable the public network access flag on your AI Studio hub. You can help secure inbound communication from a client to your managed compute by using a private endpoint for the hub.
 
-To set the PNA flag for the AI Studio hub:
+To set the public network access flag for the AI Studio hub:
 
 * Go to the [Azure portal](https://ms.portal.azure.com/).
 * Search for the resource group to which the hub belongs, and select your AI Studio hub from the resources listed for this resource group.
 * On the hub overview page, on the left pane, go to **Settings** > **Networking**.
-* On the **Public access** tab, you can configure settings for the PNA flag.
+* On the **Public access** tab, you can configure settings for the public network access flag.
 * Save your changes. Your changes might take up to five minutes to propagate.
 
 #### Limitations
 
-* If you have an AI Studio hub with a private endpoint created before July 11, 2024, new MaaS endpoints added to projects in this hub won't follow the networking configuration of the hub. Instead, you need to create a new private endpoint for the hub and create new serverless API deployments in the project so that the new deployments can follow the hub's networking configuration.
+* If you have an AI Studio hub with a managed compute created before July 11, 2024, managed computes added to projects in this hub won't follow the networking configuration of the hub. Instead, you need to create a new managed compute for the hub and create new serverless API deployments in the project so that the new deployments can follow the hub's networking configuration.
 
-* If you have an AI Studio hub with MaaS deployments created before July 11, 2024, and you enable a private endpoint on this hub, the existing MaaS deployments won't follow the hub's networking configuration. For serverless API deployments in the hub to follow the hub's networking configuration, you need to create the deployments again.
+* If you have an AI Studio hub with MaaS deployments created before July 11, 2024, and you enable a managed compute on this hub, the existing MaaS deployments won't follow the hub's networking configuration. For serverless API deployments in the hub to follow the hub's networking configuration, you need to create the deployments again.
 
-* Currently, [Azure OpenAI On Your Data](/azure/ai-services/openai/concepts/use-your-data) support isn't available for MaaS deployments in private hubs, because private hubs have the PNA flag disabled.
+* Currently, [Azure OpenAI On Your Data](/azure/ai-services/openai/concepts/use-your-data) support isn't available for MaaS deployments in private hubs, because private hubs have the public network access flag disabled.
 
-* Any network configuration change (for example, enabling or disabling the PNA flag) might take up to five minutes to propagate.
+* Any network configuration change (for example, enabling or disabling the public network access flag) might take up to five minutes to propagate.
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルカタログの概要の文書修正"
}
```

### Explanation
この変更は、"model-catalog-overview.md"の文書に対するマイナーな更新を示しています。主に、表現の統一と専門用語の修正が行われました。具体的には、"managed online endpoints"の表記が"managed compute"に変更され、記述内容もそれに合わせて調整されています。さらに、APIやネットワークの設定に関するセクションが強化され、より明確な指示と情報が提供されています。この更新によって、読み手がAzureでのモデルのデプロイメントオプションをより理解しやすくなることを目指しています。全体として、文書の一貫性と正確性が高まり、ユーザーに対する利便性が向上しました。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ items:
     href: what-is-ai-studio.md
   - name: Azure AI Studio architecture
     href: concepts/architecture.md
-  - name: "AI Studio or AML: Which should I choose?"
+  - name: AI Studio versus AML studio
     href: /ai/ai-studio-experiences-overview?context=/azure/ai-studio/context/context
   - name: Region support
     href: reference/region-support.md
@@ -65,16 +65,50 @@ items:
     - name: Create a project
       href: how-to/create-projects.md
     - name: Create and manage compute
-      href: how-to/create-manage-compute.md
-    - name: Connect to external resources
+    href: how-to/create-manage-compute.md
+  - name: Connect to services and resources
+    items:
+    - name: Connections overview
+      href: concepts/connections.md
+    - name: Create a connection
+      href: how-to/connections-add.md
+    - name: Create a connection using the Azure Machine Learning SDK
+      href: how-to/develop/connections-add-sdk.md
+      displayName: code
+    - name: Azure AI services connections
       items:
-      - name: Connections overview
-        href: concepts/connections.md
-      - name: Create a connection
-        href: how-to/connections-add.md
-      - name: Create a connection using the Azure Machine Learning SDK
-        href: how-to/develop/connections-add-sdk.md
-        displayName: code
+      - name: What are AI services?
+        href: ../ai-services/what-are-ai-services.md?context=/azure/ai-studio/context/context
+        displayName: cognitive
+      - name: Get started with AI services in AI Studio
+        href: ai-services/get-started.md
+      - name: Connect AI services in AI Studio
+        href: ai-services/connect-ai-services.md
+      - name: Azure OpenAI
+        items:
+        - name: Get started with Assistants and code interpreter in the playground
+          href: ../ai-services/openai/assistants-quickstart.md?context=/azure/ai-studio/context/context
+        - name: Analyze images and video with GPT-4 for Vision in the playground
+          href: quickstarts/multimodal-vision.md
+        - name: Use your image data with Azure OpenAI
+          href: how-to/data-image-add.md
+          displayName: vision, gpt, turbo
+      - name: Azure AI Content Safety
+        items:
+        - name: Content filtering
+          href: concepts/content-filtering.md
+        - name: Prevent input attacks with Prompt Shields
+          href: how-to/prompt-shields.md
+        - name: Detect groundedness in chat responses
+          href: how-to/groundedness.md
+      - name: Speech
+        items:
+        - name: Real-time speech to text
+          href: ../ai-services/speech-service/get-started-speech-to-text.md?context=/azure/ai-studio/context/context
+        - name: Pronunciation assessment
+          href: ../ai-services/speech-service/pronunciation-assessment-tool.md?context=/azure/ai-studio/context/context
+        - name: Hear and speak with chat in the playground
+          href: quickstarts/hear-speak-playground.md
   - name: Select and deploy AI models
     items:
     - name: Model catalog
@@ -261,40 +295,6 @@ items:
       href: how-to/monitor-quality-safety.md
     - name: Troubleshoot deployments and monitoring
       href: how-to/troubleshoot-deploy-and-monitor.md
-  - name: Get started with Azure AI services
-    items:
-    - name: What are AI services?
-      href: ../ai-services/what-are-ai-services.md?context=/azure/ai-studio/context/context
-      displayName: cognitive
-    - name: Get started with AI services in AI Studio
-      href: ai-services/get-started.md
-    - name: Connect AI services in AI Studio
-      href: ai-services/connect-ai-services.md
-    - name: Azure OpenAI
-      items:
-      - name: Get started with Assistants and code interpreter in the playground
-        href: ../ai-services/openai/assistants-quickstart.md?context=/azure/ai-studio/context/context
-      - name: Analyze images and video with GPT-4 for Vision in the playground
-        href: quickstarts/multimodal-vision.md
-      - name: Use your image data with Azure OpenAI
-        href: how-to/data-image-add.md
-        displayName: vision, gpt, turbo
-    - name: Azure AI Content Safety
-      items:
-      - name: Content filtering
-        href: concepts/content-filtering.md
-      - name: Prevent input attacks with Prompt Shields
-        href: how-to/prompt-shields.md
-      - name: Detect groundedness in chat responses
-        href: how-to/groundedness.md
-    - name: Speech
-      items:
-      - name: Real-time speech to text
-        href: ../ai-services/speech-service/get-started-speech-to-text.md?context=/azure/ai-studio/context/context
-      - name: Pronunciation assessment
-        href: ../ai-services/speech-service/pronunciation-assessment-tool.md?context=/azure/ai-studio/context/context
-      - name: Hear and speak with chat in the playground
-        href: quickstarts/hear-speak-playground.md
   - name: Costs and quotas
     items:
     - name: Plan and manage costs
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIスタジオの目次更新"
}
```

### Explanation
この変更は、"toc.yml"ファイルの内容を修正したもので、目次の項目がいくつか再構成され、新しい項目が追加されました。特に、「AI Studio or AML: Which should I choose?」の項目が「AI Studio versus AML studio」という形に変更され、より明確な表現になっています。

また、"Connect to external resources"のセクションが新たに追加され、その中に複数のサブ項目が新設されました。この更新により、サービスやリソースとの接続に関する情報がより分かり易くなり、具体的な手順や関連情報へのリンクが明確に示されています。全体として、目次の組織が改善され、ユーザーが必要な情報に迅速にアクセスできるようになっています。これにより、Azure AI Studioの利用者に対するナビゲーションの利便性が向上しました。


