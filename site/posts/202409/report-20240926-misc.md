---
date: '2024-09-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:beebdfc...MicrosoftDocs:5e7dab7
summary: |-
  この報告書は、Azure AI Studioに関するドキュメントの更新を含んでいます。主な内容は、プライベートリンクの設定、Meta Llamaモデルの展開、およびシミュレーターインタラクションデータに関するもので、新しいMeta Llamaモデルの追加や情報の詳細化が行われています。

  破壊的な変更は特にありませんが、インポートパスが修正されるなど、コードの整合性向上に寄与する更新が含まれています。また、プライベートリンクの設定に関する制限が削除され、ユーザーがより正確で一貫した情報を得られるようになっています。

  Meta Llamaモデルの展開に関しては、モデル名の変更や新しいモデルの紹介が行われ、開発者が最新の情報に基づいてモデルをデプロイできる環境が整えられています。さらに、シミュレーターのインポートパスの修正により、エラーが減少し、作業効率が向上することが期待されます。

  これらの変更は、Azure AI Studioのユーザーにとって、使いやすさと情報の正確性を高める重要な更新となっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:beebdfc...MicrosoftDocs:5e7dab7){target="_blank"}

# ハイライト
このコードの差分は、Azure AI Studioに関するドキュメントの更新を含んでいます。それぞれ「プライベートリンクの設定」、「Meta Llamaモデルの展開」、「シミュレーターインタラクションデータ」に関するもので、以下のようにまとめられます。

## 新機能
- 新しいMeta Llamaモデルの追加とそれに関する情報の詳細化。

## 破壊的変更
- 特に目立った破壊的変更はありませんが、インポートパスの修正などが行われています。

## その他の更新
- プライベートリンクの設定に関する制限の削除。
- モジュールのインポートパスの修正により、コードの整合性が向上。

# インサイト
これらの変更は、Azure AI Studioのユーザーにとって、使いやすさと情報の正確性を高めるための重要な更新です。また、特に新しいMeta Llamaモデルの追加やその詳細なデプロイ手順が含まれているため、ユーザーにとって価値の高い情報が提供されています。

## プライベートリンクの設定に関する制限の更新
今回の変更で「Azure AI Studioプレイグラウンドでの「データを追加する」機能は、プライベートストレージアカウントをサポートしていません。」という制限の記述が削除されました。これはおそらく、現在ではプライベートストレージアカウントのサポートが実現され、この記述がもはや必要ないためと推測されます。これにより、ユーザーはより一貫した情報を得ることができます。

## Meta Llamaモデルの展開に関する更新
Meta Llamaモデルに関するドキュメントの更新は、その名称変更とモデル範囲の拡大を明確にしています。これにより、特定のチャットモデルに限らず、テキストや画像の推論モデルも含まれることが強調されました。最新モデルであるLlama 3.2やLlama 3.1の紹介も含まれており、それぞれの具体的なデプロイ手順が追加されています。これにより、開発者は最新の技術と情報をもとにより高度なモデル展開が可能になります。

## シミュレーターインタラクションデータに関するインポートの修正
こちらの変更では、モジュールのインポートパスが修正され、`azure.ai.evaluation.synthetic`から`azure.ai.evaluation.simulator`へと変更されました。この修正は、クラスのインポート処理における正確性とコードの整合性を向上させます。これにより、開発者はエラーを減らし、より効率的に作業を進めることができます。また、この修正が文書内の複数の箇所で適用されているため、全体としてのコード品質が向上しています。

これらの変更は総じて、Azure AI Studio内でのユーザー体験を向上させるためのものであり、最新情報とツールの提供を目指しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [configure-private-link.md](#item-bbf93d) | minor update | プライベートリンクの設定に関する制限の更新 | modified | 0 | 1 | 1 | 
| [deploy-models-llama.md](#item-6274a7) | minor update | Meta Llamaモデルの展開に関するドキュメントの更新 | modified | 48 | 36 | 84 | 
| [simulator-interaction-data.md](#item-c753d1) | minor update | シミュレーターインタラクションデータに関するインポートの修正 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/ai-studio/how-to/configure-private-link.md{#item-bbf93d}

<details>
<summary>Diff</summary>
````diff
@@ -279,7 +279,6 @@ To check AI-PROJECT-GUID, go to the Azure portal, select your project, settings,
 
 ## Limitations
 
-* The "Add your data" feature in the Azure AI Studio playground doesn't support private storage account.
 * You might encounter problems trying to access the private endpoint for your hub if you're using Mozilla Firefox. This problem might be related to DNS over HTTPS in Mozilla Firefox. We recommend using Microsoft Edge or Google Chrome.
 
 ## Next steps
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートリンクの設定に関する制限の更新"
}
```

### Explanation
この変更は、Azure AI Studioに関するドキュメントの「プライベートリンクの設定」において、制限事項のセクションから一つの項目が削除されるというマイナーな更新です。具体的には、「Azure AI Studioプレイグラウンドでの「データを追加する」機能は、プライベートストレージアカウントをサポートしていません。」という行が削除されました。この修正は、ユーザーがプライベートリンクとその制限について正確な情報を得られるようにするためのものです。その他の制限事項に関しては、特に変更されていません。

## articles/ai-studio/how-to/deploy-models-llama.md{#item-6274a7}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: How to use Meta Llama chat models with Azure AI Studio
+title: How to use the Meta Llama family of models with Azure AI Studio
 titleSuffix: Azure AI Studio
-description: Learn how to use Meta Llama chat models with Azure AI Studio.
+description: Learn how to use the Meta Llama family of models with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
@@ -14,24 +14,36 @@ ms.custom: references_regions, generated
 zone_pivot_groups: azure-ai-model-catalog-samples-chat
 ---
 
-# How to use Meta Llama chat models
+# How to use the Meta Llama family of models
 
 [!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
 
-In this article, you learn about Meta Llama chat models and how to use them.
-Meta Llama 2 and 3 models and tools are a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. The model family also includes fine-tuned versions optimized for dialogue use cases with reinforcement learning from human feedback (RLHF).
-
+In this article, you learn about the Meta Llama family of models and how to use them. Meta Llama models and tools are a collection of pretrained and fine-tuned generative AI text and image reasoning models - ranging in scale from SLMs (1B, 3B Base and Instruct models) for on-device and edge inferencing - to mid-size LLMs (7B, 8B and 70B Base and Instruct models) and high performant models like Meta Llama 3.1 405B Instruct for synthetic data generation and distillation use cases.
 
+> [!TIP]
+> See our announcements of Meta's Llama 3.2 family models available now on Azure AI Model Catalog through [Meta's blog](https://aka.ms/llama-3.2-meta-announcement) and [Microsoft Tech Community Blog](https://aka.ms/llama-3.2-microsoft-announcement).
 
 ::: zone pivot="programming-language-python"
 
-## Meta Llama chat models
+## Meta Llama family of models
 
-The Meta Llama chat models include the following models:
+The Meta Llama family of models include the following models:
 
-# [Meta Llama-3.1](#tab/meta-llama-3-1)
+# [Llama-3.2](#tab/python-llama-3-2)
 
-The Meta Llama 3.1 collection of multilingual large language models (LLMs) is a collection of pretrained and instruction tuned generative models in 8B, 70B and 405B sizes (text in/text out). The Llama 3.1 instruction tuned text only models (8B, 70B, 405B) are optimized for multilingual dialogue use cases and outperform many of the available open-source and closed chat models on common industry benchmarks.
+The Llama 3.2 collection of SLMs and image reasoning models are now available. Coming soon, Llama 3.2 11B Vision Instruct and Llama 3.2 90B Vision Instruct will be available as a serverless API endpoint via Models-as-a-Service. Starting today, the following models will be available for deployment via managed compute:
+* Llama 3.2 1B
+* Llama 3.2 3B
+* Llama 3.2 1B Instruct
+* Llama 3.2 3B Instruct
+* Llama Guard 3 1B
+* Llama Guard 11B Vision
+* Llama 3.2 11B Vision Instruct
+* Llama 3.2 90B Vision Instruct are available for managed compute deployment.
+
+# [Meta Llama-3.1](#tab/python-meta-llama-3-1)
+
+The Meta Llama 3.1 collection of multilingual large language models (LLMs) is a collection of pretrained and instruction tuned generative models in 8B, 70B and 405B sizes (text in/text out). The Llama 3.1 instruction tuned text only models (8B, 70B, 405B) are optimized for multilingual dialogue use cases and outperform many of the available open-source and closed models on common industry benchmarks.
 
 
 The following models are available:
@@ -41,9 +53,9 @@ The following models are available:
 * [Meta-Llama-3.1-8B-Instruct](https://ai.azure.com/explore/models/Meta-Llama-3.1-8B-Instruct/version/1/registry/azureml-meta)
 
 
-# [Meta Llama-3](#tab/meta-llama-3)
+# [Meta Llama-3](#tab/python-meta-llama-3)
 
-Meta developed and released the Meta Llama 3 family of large language models (LLMs), a collection of pretrained and instruction tuned generative text models in 8B, 70B, and 405B sizes. The Llama 3 instruction tuned models are optimized for dialogue use cases and outperform many of the available open-source chat models on common industry benchmarks. Further, in developing these models, we took great care to optimize helpfulness and safety.
+Meta developed and released the Meta Llama 3 family of large language models (LLMs), a collection of pretrained and instruction tuned generative text models in 8B, and 70B sizes. The Llama 3 instruction tuned models are optimized for dialogue use cases and outperform many of the available open-source models on common industry benchmarks. Further, in developing these models, we took great care to optimize helpfulness and safety.
 
 
 The following models are available:
@@ -52,7 +64,7 @@ The following models are available:
 * [Meta-Llama-3-8B-Instruct](https://ai.azure.com/explore/models/Meta-Llama-3-8B-Instruct/version/6/registry/azureml-meta)
 
 
-# [Meta Llama-2](#tab/meta-llama-2)
+# [Meta Llama-2](#tab/python-meta-llama-2)
 
 Meta has developed and publicly released the Llama 2 family of large language models (LLMs), a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. Our fine-tuned LLMs, called Llama-2-Chat, are optimized for dialogue use cases. Llama-2-Chat models outperform open-source chat models on most benchmarks we tested, and in our human evaluations for helpfulness and safety, are on par with some popular closed-source models like ChatGPT and PaLM. We provide a detailed description of our approach to fine-tuning and safety improvements of Llama-2-Chat in order to enable the community to build on our work and contribute to the responsible development of LLMs.
 
@@ -68,13 +80,13 @@ The following models are available:
 
 ## Prerequisites
 
-To use Meta Llama chat models with Azure AI Studio, you need the following prerequisites:
+To use Meta Llama models with Azure AI Studio, you need the following prerequisites:
 
 ### A model deployment
 
 **Deployment to serverless APIs**
 
-Meta Llama chat models can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+Meta Llama models can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
 
 Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Studio, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
 
@@ -83,7 +95,7 @@ Deployment to a serverless API endpoint doesn't require quota from your subscrip
 
 **Deployment to a self-hosted managed compute**
 
-Meta Llama chat models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
+Meta Llama models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
 
 For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
 
@@ -111,7 +123,7 @@ Read more about the [Azure AI inference package and reference](https://aka.ms/az
 In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
 
 > [!TIP]
-> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Studio with the same code and structure, including Meta Llama chat models.
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Studio with the same code and structure, including Meta Llama Instruct models - text-only or image reasoning models.
 
 ### Create a client to consume the model
 
@@ -296,7 +308,7 @@ response = client.complete(
 )
 ```
 
-The following extra parameters can be passed to Meta Llama chat models:
+The following extra parameters can be passed to Meta Llama models:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
@@ -350,9 +362,9 @@ except HttpResponseError as ex:
 
 ::: zone pivot="programming-language-javascript"
 
-## Meta Llama chat models
+## Meta Llama models
 
-The Meta Llama chat models include the following models:
+The Meta Llama models include the following models:
 
 # [Meta Llama-3.1](#tab/meta-llama-3-1)
 
@@ -393,13 +405,13 @@ The following models are available:
 
 ## Prerequisites
 
-To use Meta Llama chat models with Azure AI Studio, you need the following prerequisites:
+To use Meta Llama models with Azure AI Studio, you need the following prerequisites:
 
 ### A model deployment
 
 **Deployment to serverless APIs**
 
-Meta Llama chat models can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+Meta Llama models can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
 
 Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Studio, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
 
@@ -408,7 +420,7 @@ Deployment to a serverless API endpoint doesn't require quota from your subscrip
 
 **Deployment to a self-hosted managed compute**
 
-Meta Llama chat models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
+Meta Llama models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
 
 For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
 
@@ -434,7 +446,7 @@ npm install @azure-rest/ai-inference
 In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
 
 > [!TIP]
-> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Studio with the same code and structure, including Meta Llama chat models.
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Studio with the same code and structure, including Meta Llama models.
 
 ### Create a client to consume the model
 
@@ -638,7 +650,7 @@ var response = await client.path("/chat/completions").post({
 });
 ```
 
-The following extra parameters can be passed to Meta Llama chat models:
+The following extra parameters can be passed to Meta Llama models:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
@@ -698,13 +710,13 @@ catch (error) {
 
 ::: zone pivot="programming-language-csharp"
 
-## Meta Llama chat models
+## Meta Llama models
 
-The Meta Llama chat models include the following models:
+The Meta Llama models include the following models:
 
 # [Meta Llama-3.1](#tab/meta-llama-3-1)
 
-The Meta Llama 3.1 collection of multilingual large language models (LLMs) is a collection of pretrained and instruction tuned generative models in 8B, 70B and 405B sizes (text in/text out). The Llama 3.1 instruction tuned text only models (8B, 70B, 405B) are optimized for multilingual dialogue use cases and outperform many of the available open-source and closed chat models on common industry benchmarks.
+The Meta Llama 3.1 collection of multilingual large language models (LLMs) is a collection of pretrained and instruction tuned generative models in 8B, 70B and 405B sizes (text in/text out). The Llama 3.1 instruction tuned text only models (8B, 70B, 405B) are optimized for multilingual dialogue use cases and outperform many of the available open-source and closed models on common industry benchmarks.
 
 
 The following models are available:
@@ -716,7 +728,7 @@ The following models are available:
 
 # [Meta Llama-3](#tab/meta-llama-3)
 
-Meta developed and released the Meta Llama 3 family of large language models (LLMs), a collection of pretrained and instruction tuned generative text models in 8B, 70B, and 405B sizes. The Llama 3 instruction tuned models are optimized for dialogue use cases and outperform many of the available open-source chat models on common industry benchmarks. Further, in developing these models, we took great care to optimize helpfulness and safety.
+Meta developed and released the Meta Llama 3 family of large language models (LLMs), a collection of pretrained and instruction tuned generative text models in 8B, 70B, and 405B sizes. The Llama 3 instruction tuned models are optimized for dialogue use cases and outperform many of the available open-source models on common industry benchmarks. Further, in developing these models, we took great care to optimize helpfulness and safety.
 
 
 The following models are available:
@@ -741,13 +753,13 @@ The following models are available:
 
 ## Prerequisites
 
-To use Meta Llama chat models with Azure AI Studio, you need the following prerequisites:
+To use Meta Llama models with Azure AI Studio, you need the following prerequisites:
 
 ### A model deployment
 
 **Deployment to serverless APIs**
 
-Meta Llama chat models can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+Meta Llama models can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
 
 Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Studio, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
 
@@ -756,7 +768,7 @@ Deployment to a serverless API endpoint doesn't require quota from your subscrip
 
 **Deployment to a self-hosted managed compute**
 
-Meta Llama chat models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
+Meta Llama models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
 
 For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
 
@@ -998,7 +1010,7 @@ response = client.Complete(requestOptions, extraParams: ExtraParameters.PassThro
 Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
-The following extra parameters can be passed to Meta Llama chat models:
+The following extra parameters can be passed to Meta Llama models:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
@@ -1101,7 +1113,7 @@ The following models are available:
 
 ## Prerequisites
 
-To use Meta Llama chat models with Azure AI Studio, you need the following prerequisites:
+To use Meta Llama models with Azure AI Studio, you need the following prerequisites:
 
 ### A model deployment
 
@@ -1116,7 +1128,7 @@ Deployment to a serverless API endpoint doesn't require quota from your subscrip
 
 **Deployment to a self-hosted managed compute**
 
-Meta Llama chat models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
+Meta Llama models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
 
 For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
 
@@ -1476,4 +1488,4 @@ It is a good practice to start with a low number of instances and scale up as ne
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Meta Llamaモデルの展開に関するドキュメントの更新"
}
```

### Explanation
この変更は、「Meta Llamaモデルの展開」に関するドキュメントにおける重要な更新を含んでいます。主な改訂点は、タイトルや説明文をより包括的な表現に変更した点であり、"Meta Llama chat models"から"Meta Llama family of models"に名称が変更されました。この修正により、AIモデルの範囲がチャットモデルに限定されず、テキストや画像の推論モデルを含むことが明示されています。また、追加のモデルやバージョンの情報が記述され、デプロイメントに関する手順が更新されました。具体的には、Llama 3.2やLlama 3.1などの新しいモデルが紹介され、それぞれのデプロイ方法に関する情報も強化されています。全体として、ユーザーがAzure AI Studio内でMeta Llamaモデルをより効果的に活用できるよう、より詳細で明確な内容に刷新されています。

## articles/ai-studio/how-to/develop/simulator-interaction-data.md{#item-c753d1}

<details>
<summary>Diff</summary>
````diff
@@ -42,7 +42,7 @@ Azure AI Evaluation SDK's `Simulator` provides an end-to-end synthetic data gene
 By automating the creation of synthetic data, the `Simulator` class helps streamline the development and testing processes, ensuring your applications are robust and reliable.
 
 ```python
-from azure.ai.evaluation.synthetic import Simulator
+from azure.ai.evaluation.simulator import Simulator
 ```
 
 ### Generate text or index-based synthetic data as input
@@ -215,7 +215,7 @@ print(json.dumps(outputs, indent=2))
 Augment and accelerate your red-teaming operation by using Azure AI Studio safety evaluations to generate an adversarial dataset against your application. We provide adversarial scenarios along with configured access to a service-side Azure OpenAI GPT-4 model with safety behaviors turned off to enable the adversarial simulation.
 
 ```python
-from azure.ai.evaluation.synthetic import AdversarialSimulator
+from azure.ai.evaluation.simulator import AdversarialSimulator
 ```
 
 The adversarial simulator works by setting up a service-hosted GPT large language model to simulate an adversarial user and interact with your application. An AI Studio project is required to run the adversarial simulator:
@@ -272,7 +272,7 @@ async def callback(
 ## Run an adversarial simulation
 
 ```python
-from azure.ai.evaluation.synthetic import AdversarialScenario
+from azure.ai.evaluation.simulator import AdversarialScenario
 
 scenario = AdversarialScenario.ADVERSARIAL_QA
 adversarial_simulator = AdversarialSimulator(azure_ai_project=azure_ai_project)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "シミュレーターインタラクションデータに関するインポートの修正"
}
```

### Explanation
この変更は、「シミュレーターインタラクションデータ」に関する文書内でのモジュールのインポートパスの修正を含んでいます。具体的には、`azure.ai.evaluation.synthetic`から`azure.ai.evaluation.simulator`へのインポートパスの変更が行われています。これにより、`Simulator`や`AdversarialSimulator`などのクラスが正しいモジュールからインポートできるようになり、コードの整合性が保たれます。この変更は文書内の複数の箇所に適用されており、また、全体としてコードの質を向上させ、開発者がより効率的に作業できるように配慮されています。


