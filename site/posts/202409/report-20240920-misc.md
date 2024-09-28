---
date: '2024-09-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e496207...MicrosoftDocs:daa818e
summary: この差分では、新しい機能の追加とドキュメントの微修正が行われました。特に、Azure AIスタジオとLlamaIndexを利用したアプリケーション開発に関する新しい文書が追加され、全体のドキュメント構造がより整理され、使いやすくなりました。新しい機能には、LlamaIndexとAzure
  AIスタジオに関する文書、およびサーバーレスエンドポイントのURLキーに関する画像が含まれています。破壊的変更はなく、その他の更新としては、Azure AI SDKにLlamaIndexを追加し、モデルカタログのテキストの微修正やAPIリクエストのパラメータ追加が行われました。全体的に、開発者がAzure
  AIスタジオをより活用しやすくなる内容です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e496207...MicrosoftDocs:daa818e){target="_blank"}

# ハイライト
この差分の全体的なハイライトは、新しい機能の追加と既存ドキュメントの微修正です。特に、Azure AIスタジオとLlamaIndexを使用したアプリケーション開発に関する新しいドキュメントが追加され、全体のドキュメント構造がより整理され、使いやすくなった点が注目されます。

## 新機能
- LlamaIndexとAzure AIスタジオを使ったアプリケーション開発に関する新しい文書の追加
- サーバーレスエンドポイントのURLキーに関する新しい画像の追加

## 破壊的変更
- なし

## その他の更新
- Azure AI SDKの概要にLlamaIndexを追加
- モデルカタログの概要におけるテキストの微修正
- チャット補完リクエストと埋め込みリクエストにモデル名のパラメータを追加
- AI Studioの案内目次の更新

# インサイト
今回の差分により、Azure AIスタジオのドキュメントが大幅に改善され、特にLlamaIndexを利用したアプリケーション開発が容易になりました。以下は差分の詳細とその背景についての技術的な見解です。

## LlamaIndexとAzure AIスタジオを使ったアプリケーション開発
新しい文書が追加されることにより、Azure AIスタジオを利用する開発者はLlamaIndexを活用した高度な知能アプリケーションを迅速に構築できるようになりました。この文書は、前提条件から具体的なコードサンプルまでを網羅しており、特に以下の点が強調されています：

- **前提条件**: Azureのサブスクリプションやモデルのデプロイ、Python環境設定、LlamaIndexのインストール
- **API利用方法**: モデル推論APIおよびプロバイダー特有のAPI
- **具体的なコードサンプル**: 環境変数の設定からクライアント作成、推論パラメーターの設定方法

これにより、開発者は理論から実践まで一貫して進めることができ、Azure AIスタジオを使った開発のハードルが大きく下がります。

## Azure AI SDKの概要にLlamaIndexを追加
この更新により、LlamaIndexがAzure AIスタジオ内で提供される生成AIアプリケーションの一つとして位置づけられ、より多様な選択肢が開発者に提供されます。これにより、開発者は自分のニーズに最も適したフレームワークを選択しやすくなります。

## モデルカタログの概要におけるテキストの微修正
用語の一貫性や説明の明確さが向上することで、読者はモデルのデプロイメントオプションについてより正確な理解を得ることができます。また、「managed compute」や「public network access flag」といった用語の変更により、技術文書としての信頼性が向上しています。

## サーバーレスエンドポイントURLキーの画像追加
新しい画像の追加は、視覚的な情報提示による理解促進を目的としています。特に、設定や管理が複雑になる可能性のあるサーバーレスエンドポイントにおいて、具体的なビジュアルガイドは非常に有用です。これにより、ユーザーはよりスムーズに設定を行うことができます。

## チャット補完リクエストと埋め込みリクエストにモデル名のパラメータを追加
APIリクエストにおける「model」パラメータの追加は、ユーザーが異なるモデルを指定してより柔軟にリクエストを行えるようにするための重要な変更です。特定のモデルを指定できることで、APIの利用シーンが広がり、開発者にとっても便利です。

## AI Studioの案内目次の更新
目次（toc.yml）の更新によって、ドキュメント全体の構造が整理され、必要な

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [llama-index.md](#item-613372) | new feature | LlamaIndexとAzure AIスタジオを使ったアプリケーション開発 | added | 202 | 0 | 202 | 
| [sdk-overview.md](#item-d3ab19) | minor update | Azure AI SDKの概要にLlamaIndexを追加 | modified | 4 | 1 | 5 | 
| [model-catalog-overview.md](#item-278001) | minor update | モデルカタログの概要におけるテキストの微修正 | modified | 11 | 11 | 22 | 
| [serverless-endpoint-url-keys.png](#item-015560) | new feature | サーバーレスエンドポイントURLキーの画像を追加 | added | 0 | 0 | 0 | 
| [reference-model-inference-chat-completions.md](#item-e09823) | minor update | チャット補完リクエストにモデル名のパラメータを追加 | modified | 1 | 0 | 1 | 
| [reference-model-inference-embeddings.md](#item-5e9064) | minor update | 埋め込みリクエストにモデル名のパラメータを追加 | modified | 1 | 0 | 1 | 
| [toc.yml](#item-2745cd) | minor update | AI Studioの案内目次の更新 | modified | 46 | 44 | 90 | 


# Modified Contents
## articles/ai-studio/how-to/develop/llama-index.md{#item-613372}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,202 @@
+---
+title: Develop application with LlamaIndex and Azure AI studio
+titleSuffix: Azure AI Studio
+description: This article explains how to use LlamaIndex with models deployed in Azure AI studio to build advance intelligent applications.
+manager: nitinme
+ms.service: azure-ai-studio
+ms.topic: how-to
+ms.date: 9/14/2024
+ms.reviewer: fasantia
+ms.author: eur
+author: eric-urban
+---
+
+# Develop applications with LlamaIndex and Azure AI studio
+
+In this article, you learn how to use [LlamaIndex](https://github.com/run-llama/llama_index) with models deployed from the Azure AI model catalog deployed to Azure AI studio.
+
+Models deployed to Azure AI studio can be used with LlamaIndex in two ways:
+
+- **Using the Azure AI model inference API:** All models deployed to Azure AI studio support the [Azure AI model inference API](../../reference/reference-model-inference-api.md), which offers a common set of functionalities that can be used for most of the models in the catalog. The benefit of this API is that, since it's the same for all the models, changing from one to another is as simple as changing the model deployment being use. No further changes are required in the code. When working with LlamaIndex, install the extensions `llama-index-llms-azure-inference` and `llama-index-embeddings-azure-inference`.
+
+- **Using the model's provider specific API:** Some models, like OpenAI, Cohere, or Mistral, offer their own set of APIs and extensions for LlamaIndex. Those extensions may include specific functionalities that the model support and hence are suitable if you want to exploit them. When working with `llama-index`, install the extension specific for the model you want to use, like `llama-index-llms-openai` or `llama-index-llms-cohere`.
+
+In this example, we are working with the **Azure AI model inference API**.
+
+## Prerequisites
+
+To run this tutorial, you need:
+
+1. An [Azure subscription](https://azure.microsoft.com).
+2. An Azure AI hub resource as explained at [How to create and manage an Azure AI Studio hub](../create-azure-ai-resource.md).
+3. A model supporting the [Azure AI model inference API](https://aka.ms/azureai/modelinference) deployed. In this example, we use a `Mistral-Large` deployment, but use any model of your preference. For using embeddings capabilities in LlamaIndex, you need an embedding model like `cohere-embed-v3-multilingual`. 
+
+    * You can follow the instructions at [Deploy models as serverless APIs](../deploy-models-serverless.md).
+
+4. Python 3.8 or later installed, including pip.
+5. LlamaIndex installed. You can do it with:
+
+    ```bash
+    pip install llama-index
+    ```
+
+6. In this example, we are working with the Azure AI model inference API, hence we install the following packages:
+
+    ```bash
+    pip install -U llama-index-llms-azure-inference
+    pip install -U llama-index-embeddings-azure-inference
+    ``` 
+
+## Configure the environment
+
+To use LLMs deployed in Azure AI studio, you need the endpoint and credentials to connect to it. The parameter `model_name` is not required for endpoints serving a single model, like Managed Online Endpoints. Follow these steps to get the information you need from the model you want to use:
+
+1. Go to the [Azure AI studio](https://ai.azure.com/).
+2. Go to deployments and select the model you deployed as indicated in the prerequisites.
+3. Copy the endpoint URL and the key.
+
+    :::image type="content" source="../../media/how-to/inference/serverless-endpoint-url-keys.png" alt-text="Screenshot of the option to copy endpoint URI and keys from an endpoint." lightbox="../../media/how-to/inference/serverless-endpoint-url-keys.png":::
+    
+    > [!TIP]
+    > If your model was deployed with Microsoft Entra ID support, you don't need a key.
+
+In this scenario, we placed both the endpoint URL and key in the following environment variables:
+
+```bash
+export AZURE_INFERENCE_ENDPOINT="<your-model-endpoint-goes-here>"
+export AZURE_INFERENCE_CREDENTIAL="<your-key-goes-here>"
+```
+
+Once configured, create a client to connect to the endpoint:
+
+```python
+import os
+from llama_index.llms.azure_inference import AzureAICompletionsModel
+
+llm = AzureAICompletionsModel(
+    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
+)
+```
+
+Alternatively, if your endpoint support Microsoft Entra ID, you can use the following code to create the client:
+
+```python
+from azure.identity import DefaultAzureCredential
+
+llm = AzureAICompletionsModel(
+    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    credential=DefaultAzureCredential(),
+)
+```
+
+> [!NOTE]
+> > Note: When using Microsoft Entra ID, make sure that the endpoint was deployed with that authentication method and that you have the required permissions to invoke it.
+
+If you are planning to use asynchronous calling, it's a best practice to use the asynchronous version for the credentials:
+
+```python
+from azure.identity.aio import (
+    DefaultAzureCredential as DefaultAzureCredentialAsync,
+)
+
+llm = AzureAICompletionsModel(
+    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    credential=DefaultAzureCredentialAsync(),
+)
+```
+
+### Inference parameters
+
+You can configure how inference in performed for all the operations that are using this client by setting extra parameters. This helps avoid indicating them on each call you make to the model.
+
+```python
+llm = AzureAICompletionsModel(
+    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
+    temperature=0.0,
+    model_kwargs={"top_p": 1.0},
+)
+```
+
+Parameters not supported in the Azure AI model inference API ([reference](../../reference/reference-model-inference-chat-completions.md)) but available in the underlying model, you can use the `model_extras` argument. In the following example, the parameter `safe_prompt`, only available for Mistral models, is being passed.
+
+```python
+llm = AzureAICompletionsModel(
+    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
+    temperature=0.0,
+    model_kwargs={"model_extras": {"safe_prompt": True}},
+)
+```
+
+## Use LLMs models
+
+Use the `chat` endpoint for chat instruction models. The `complete` method is still available for model of type `chat-completions`. On those cases, your input text is converted to a message with `role="user"`.
+
+```python
+from llama_index.core.llms import ChatMessage
+
+messages = [
+    ChatMessage(
+        role="system", content="You are a pirate with colorful personality."
+    ),
+    ChatMessage(role="user", content="Hello"),
+]
+
+response = llm.chat(messages)
+print(response)
+```
+
+You can stream the outputs also:
+
+```python
+response = llm.stream_chat(messages)
+for r in response:
+    print(r.delta, end="")
+```
+
+## Use embeddings models
+
+In the same way you create an LLM client, you can connect to an embedding model. In the following example, we are setting again the environment variable to now point to an embeddings model:
+
+```bash
+export AZURE_INFERENCE_ENDPOINT="<your-model-endpoint-goes-here>"
+export AZURE_INFERENCE_CREDENTIAL="<your-key-goes-here>"
+```
+
+Then create the client:
+
+```python
+from llama_index.embeddings.azure_inference import AzureAIEmbeddingsModel
+
+embed_model = AzureAIEmbeddingsModel(
+    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    credential=os.environ['AZURE_INFERENCE_CREDENTIAL'],
+)
+```
+
+## Configure the models used by your code
+
+You can use the LLM or embeddings model client individually in the code you develop with LlamaIndex or you can configure the entire session using the `Settings` options. Configuring the session has the advantage of all your code using the same models for all the operations.
+
+```python
+from llama_index.core import Settings
+
+Settings.llm = llm
+Settings.embed_model = embed_model
+```
+
+However, there are scenarios where you want to use a general model for most of the operations but a specific one for a given task. On those cases, it's useful to set the LLM or embedding model you are using for each LlamaIndex construct. In the following example, we set a specific model:
+
+```python
+from llama_index.core.evaluation import RelevancyEvaluator
+
+relevancy_evaluator = RelevancyEvaluator(llm=llm)
+```
+
+In general, you use a combination of both strategies.
+
+## Related content
+
+* [How to get started with Azure AI SDKs](sdk-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "LlamaIndexとAzure AIスタジオを使ったアプリケーション開発"
}
```

### Explanation
この修正では、Azure AIスタジオとLlamaIndexを使用してアプリケーションを開発する方法を説明する新しい文書が追加されました。この文書では、Azure AIスタジオにデプロイされたモデルを利用して、知能アプリケーションを構築するための手順が詳述されています。

文書は、LlamaIndexを使用するための前提条件として、Azureのサブスクリプション、モデルのデプロイ、Python環境設定、LlamaIndexのインストールなどを挙げています。また、モデル推論APIを使用する方法と、モデルのプロバイダー特有のAPIを使用する方法も説明しています。

さらに、環境変数を設定する手順、クライアントを作成するためのPythonコード、推論パラメーターの設定方法など、具体的なコードサンプルも提供されています。この新しい追加により、Azure AIスタジオを利用した開発者は、LlamaIndexと連携して効率的にアプリケーションを構築できるようになります。

## articles/ai-studio/how-to/develop/sdk-overview.md{#item-d3ab19}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: eric-urban
 
 # Overview of the Azure AI SDKs
 
-Microsoft offers a variety of packages that you can use for building generative AI applications in the cloud. In most applications, you need to use a combination of packages to manage and use various Azure services that provide AI functionality. We also offer integrations with open-source libraries like LangChain and mlflow for use with Azure. In this article we'll give an overview of the main services and SDKs you can use with Azure AI Studio.
+Microsoft offers a variety of packages that you can use for building generative AI applications in the cloud. In most applications, you need to use a combination of packages to manage and use various Azure services that provide AI functionality. We also offer integrations with open-source libraries like LangChain and MLflow for use with Azure. In this article we'll give an overview of the main services and SDKs you can use with Azure AI Studio.
 
 For building generative AI applications, we recommend using the following services and SDKs:
  * [Azure Machine Learning](/azure/machine-learning/overview-what-is-azure-machine-learning) for the hub and project infrastructure used in AI Studio to organize your work into projects, manage project artifacts (data, evaluation runs, traces), fine-tune & deploy models, and connect to external services and resources.
@@ -54,6 +54,9 @@ Azure AI services
 Prompt flow
  * [Prompt flow SDK](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html)
 
+Agentic frameworks:
+* [LlamaIndex](llama-index.md)
+
 ## Related content
 
 - [Get started building a chat app using the prompt flow SDK](../../quickstarts/get-started-code.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI SDKの概要にLlamaIndexを追加"
}
```

### Explanation
この修正では、Azure AI SDKの概要にLlamaIndexを追加し、更新を行いました。具体的には、エージェント系のフレームワークとしてLlamaIndexが紹介され、Azure AIスタジオでの生成AIアプリケーションの構築に役立つサービスとSDKのリストに加えられました。

文書の内容は、Azureで生成AIアプリケーションを構築するためのパッケージやサービスの概要を提供しており、その中でLlamaIndexの重要性が強調されています。これにより、開発者はより多様な選択肢を持つことになり、Azure AIスタジオでのアプリケーション開発がよりスムーズになることが期待されます。

全体としては、Azure AI SDKの概要がわかりやすく、関連する重要な情報が収集されていることが進化した点となります。

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
    "modification_title": "モデルカタログの概要におけるテキストの微修正"
}
```

### Explanation
この修正では、モデルカタログの概要に関する文書が微修正されました。具体的には、「Managed compute」と「Serverless API」に関する部分の文言がより明確に整理され、表現の一貫性が向上しました。

主な変更点は、次の通りです：
- 「Managed compute」と「Serverless API」の説明において、「managed online endpoints」が「managed compute」へと適切に変更され、用語の一貫性が取られました。
- ネットワーク隔離における説明でも、用語が整理され、より明確な表現になりました。特に、「PNAフラグ」に関する説明が「public network access flag」に置き換えられ、認識が容易になっています。

これにより、読者はAzure AIスタジオにおけるモデルのDeploymentオプションと機能を理解するのが容易となり、正確な情報を得ることができます。この更新は、全体として文書の質の向上に寄与しています。

## articles/ai-studio/media/how-to/inference/serverless-endpoint-url-keys.png{#item-015560}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "サーバーレスエンドポイントURLキーの画像を追加"
}
```

### Explanation
この修正では、サーバーレスエンドポイントに関連する新しい画像が文書に追加されました。この画像は「serverless-endpoint-url-keys.png」として名付けられており、サーバーレスエンドポイントのURLキーに関する情報を視覚的に示すためのものです。

画像を追加することで、ユーザーはサーバーレスエンドポイントの設定や管理方法をより理解しやすくなることが期待されます。ビジュアルコンテンツが文書に加わることで、テキストだけでは伝わりにくい情報が明確にされ、読者の理解を深める役割を果たします。このような追加は、ユーザー体験を向上させる重要なステップと言えます。

## articles/ai-studio/reference/reference-model-inference-chat-completions.md{#item-e09823}

<details>
<summary>Diff</summary>
````diff
@@ -42,6 +42,7 @@ POST /chat/completions?api-version=2024-04-01-preview
 
 | Name | Required | Type | Description |
 | --- | --- | --- | --- |
+| model |      | string | The model name. This parameter is ignored if the endpoint serves only one model. |
 | messages | True | [ChatCompletionRequestMessage](#chatcompletionrequestmessage) | A list of messages comprising the conversation so far. Returns a 422 error if at least some of the messages can't be understood by the model. |
 | frequency\_penalty |     | number | Helps prevent word repetitions by reducing the chance of a word being selected if it has already been used. The higher the frequency penalty, the less likely the model is to repeat the same words in its output. Return a 422 error if value or parameter is not supported by model. |
 | max\_tokens |     | integer | The maximum number of tokens that can be generated in the chat completion.<br><br>The total length of input tokens and generated tokens is limited by the model's context length. Passing null causes the model to use its max context length. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャット補完リクエストにモデル名のパラメータを追加"
}
```

### Explanation
この修正では、チャット補完に関するリファレンス文書において、新しいパラメータ「model」が追加されました。この変更により、APIリクエストの形式が更新され、モデル名が指定できるようになりました。

具体的には、以下の情報が新たに追加されました：
- **model**: このパラメータはストリング型で、モデル名を指定する役割を果たします。特に、エンドポイントが単一のモデルだけを提供する場合、このパラメータは無視されることが明記されています。

この変更は、ユーザーが異なるモデルを使用する際に、より柔軟性を持ってAPIを利用できるようにするためのものです。また、文書にこの情報を加えることで、利用者に対してリクエスト形式の理解を深め、正確なAPI使用を促進します。

## articles/ai-studio/reference/reference-model-inference-embeddings.md{#item-5e9064}

<details>
<summary>Diff</summary>
````diff
@@ -42,6 +42,7 @@ POST /embeddings?api-version=2024-04-01-preview
 
 | Name            | Required | Type                                                | Description                                                                                                                                                             |
 | --------------- | -------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| model |      | string | The model name. This parameter is ignored if the endpoint serves only one model. |
 | input           | True     | string[]                                            | Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays.           |
 | dimensions      |          | integer                                             | The number of dimensions the resulting output embeddings should have. Returns a 422 error if the model doesn't support the value or parameter.                          |
 | encoding_format |          | [EmbeddingEncodingFormat](#embeddingencodingformat) | The format to return the embeddings in. Either base64, float, int8, uint8, binary, or ubinary. Returns a 422 error if the model doesn't support the value or parameter. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "埋め込みリクエストにモデル名のパラメータを追加"
}
```

### Explanation
この修正では、埋め込みに関するリファレンス文書に新たなパラメータ「model」が追加されました。この変更により、埋め込みAPIリクエストを行う際に、使用するモデル名を指定できるようになりました。

具体的には、以下の情報が新たに記載されています：
- **model**: このパラメータはストリング型で、モデル名を指定するためのものです。エンドポイントが単一のモデルのみを提供する場合は、このパラメータは無視されることが明記されています。

この追加により、ユーザーは異なるモデルを使って埋め込みリクエストをより柔軟に行えるようになります。また、埋め込みの作成に関する文書を通じて、モデルの選択が明確になり、APIの使用が向上します。このような更新は、開発者やユーザーにとって利便性を高める重要な変更です。

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
@@ -218,6 +252,8 @@ items:
         href: how-to/develop/vscode.md
       - name: Start with an AI template
         href: how-to/develop/ai-template-get-started.md
+      - name: Develop with LlamaIndex and Azure AI studio
+        href: how-to/develop/llama-index.md
       - name: Trace your application with prompt flow
         href: how-to/develop/trace-local-sdk.md
         displayName: code,sdk
@@ -261,40 +297,6 @@ items:
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
    "modification_title": "AI Studioの案内目次の更新"
}
```

### Explanation
この修正では、AI Studioに関連する案内目次（toc.yml）が更新されました。主に、新しい項目の追加や既存項目の名称変更が行われており、全体の構成も整理されています。

具体的な変更点は以下の通りです：
- **項目名の変更**: 例えば、「AI Studio or AML: Which should I choose?」が「AI Studio versus AML studio」に変更されました。
- **新規項目の追加**: 「Connect to services and resources」という新しいセクションが追加され、その中に複数の関連サブトピックが設けられました。これには、接続の概要や接続の作成手順などが含まれています。
- **削除された項目**: 一部のセクションが再構成され、重複する内容が削除されました。これにより、情報が整理され、利用者が必要な情報にスムーズにアクセスできるようになっています。
- **AIサービスに関する詳細の追加**: Azure OpenAIやAIコンテンツの安全性、音声認識など、具体的なサービスに関する新しい項目が追加され、より詳細な情報が提供されています。

これにより、AI Studioのドキュメントがより包括的に、かつ最新の情報を反映する形に更新され、利用者がサービスをより理解しやすくなることを目的としています。


