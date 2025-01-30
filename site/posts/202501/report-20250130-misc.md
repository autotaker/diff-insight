---
date: '2025-01-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b5fac8b...MicrosoftDocs:62147e0
summary: この報告書は、AI Studioに関連する文書やリンクの更新、およびモデル推論に関するリファレンスの削除について述べています。主な変更点として、新しいDeepSeek-R1推論モデルのドキュメントが追加され、リンクの相対パスが修正され、ユーザーエクスペリエンスが向上しました。しかし、モデル推論完了に関するリファレンスが削除されたことは重要な変更であり、開発者にとっての情報源が失われることにつながります。全体として、この更新はユーザーフレンドリーさを向上させ、最新情報の提供を目指しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b5fac8b...MicrosoftDocs:62147e0){target="_blank"}

<format>
# ハイライト
この差分には、主にAI Studio関連の文書やリンクの更新と、モデル推論に関するリファレンスの削除が含まれています。特に、DeepSeek-R1推論モデルの新しいドキュメント追加や、既存のリンクの相対パスの修正が行われ、ユーザーエクスペリエンスの改善が図られています。また、モデル推論完了に関するリファレンスの削除という重大な変更も見られます。

## 新機能
- DeepSeek-R1推論モデルに関する新しいドキュメントの追加。これにより、特定のディープラーニングモデルに関連する詳細な情報が利用可能になりました。

## 破壊的変更
- モデル推論完了に関する詳細なリファレンスドキュメントが削除されました。この文書の削除は、開発者にとって重要な情報源の消失を意味し、代替のドキュメントが必要です。

## その他の更新
- 複数のドキュメントについて、リンクの相対パスを修正して、正しい参照情報へアクセス可能に。
- リダイレクト設定や目次に対するマイナー更新を実施。
- 複数のドキュメントの日付を更新し、最新の情報を反映。

# 知見
この差分は、AI Studioのドキュメント全般において、リンクや情報の整合性を改善するために行われた一連の更新から成ります。特に、リンクの相対パスを更新する動きは、ユーザーが正しい情報にアクセスしやすくするための重要な修正です。また、新しいDeepSeek-R1推論モデルのドキュメント追加は、ユーザーにとって価値ある情報を提供することで、AI Foundry内のモデル使用を推奨するものです。

一方で、モデル推論完了に関するリファレンスの削除は、関連するアプリケーションを開発している技術者に少なからぬ影響を与える可能性があります。これにより、使用前にAPIの詳細を確認するための参照先が失われてしまう可能性があるため、この変更に伴う追加のサポート資料や代替手段が求められます。

全体として、この更新はAI Studioプラットフォームをよりユーザーフレンドリーにし、最新の情報を提供することを意図したものです。また、今回のような大規模レンジの文書と構成の更新を通じて、開発者に対する価値提供がさらに強化されるでしょう。</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [.openpublishing.redirection.ai-studio.json](#item-c75c21) | minor update | AI Studioのリダイレクト設定の更新 | modified | 32 | 2 | 34 | 
| [toc.yml](#item-cd87b7) | minor update | AI Studioの目次設定の更新 | modified | 4 | 1 | 5 | 
| [deploy-models-cohere-command.md](#item-3e97f4) | minor update | Cohereコマンドでのモデルデプロイに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [deploy-models-cohere-embed.md](#item-eab662) | minor update | Cohere埋め込みモデルデプロイに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [deploy-models-deepseek.md](#item-7c33de) | new feature | DeepSeek-R1推論モデルを使用する方法に関する新しいドキュメント | added | 1150 | 0 | 1150 | 
| [deploy-models-gretel-navigator.md](#item-2e9806) | minor update | Gretel Navigatorモデルデプロイに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [deploy-models-jais.md](#item-0bd11f) | minor update | JAISモデルデプロイに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [deploy-models-jamba.md](#item-eeefca) | minor update | Jambaモデルデプロイに関するドキュメントのリンク修正 | modified | 3 | 3 | 6 | 
| [deploy-models-llama.md](#item-6274a7) | minor update | Llamaモデルデプロイに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [deploy-models-mistral-codestral.md](#item-83ba03) | minor update | Mistralモデルデプロイに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [deploy-models-mistral-nemo.md](#item-e7b729) | minor update | Mistral Nemoモデルデプロイに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [deploy-models-mistral-open.md](#item-84e005) | minor update | Mistral Openモデルデプロイに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [deploy-models-mistral.md](#item-487a41) | minor update | Mistralモデルデプロイに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [deploy-models-phi-3-5-vision.md](#item-8d6d7d) | minor update | Phi 3.5ビジョンモデルデプロイに関するドキュメントのリンク更新 | modified | 1 | 1 | 2 | 
| [deploy-models-phi-3-vision.md](#item-bd5aae) | minor update | Phi 3モデルデプロイに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [deploy-models-phi-3.md](#item-47e305) | minor update | Phi 3モデルデプロイに関するドキュメントのリンク変更 | modified | 1 | 1 | 2 | 
| [deploy-models-phi-4.md](#item-c40212) | minor update | Phi 4モデルデプロイに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [deploy-models-serverless.md](#item-f8177f) | minor update | サーバーレスAPIモデルデプロイに関するドキュメントのリンク更新 | modified | 2 | 2 | 4 | 
| [deploy-models-tsuzumi.md](#item-d3fd51) | minor update | Tsuzumiモデルデプロイに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [langchain.md](#item-0d59f1) | minor update | LangChainに関するドキュメントのリンク更新 | modified | 2 | 2 | 4 | 
| [llama-index.md](#item-613372) | minor update | LlamaIndexドキュメント内のリンク修正 | modified | 2 | 2 | 4 | 
| [semantic-kernel.md](#item-565785) | minor update | Semantic Kernelドキュメント内のリンク修正 | modified | 1 | 1 | 2 | 
| [trace-local-sdk.md](#item-f7dfb5) | minor update | Trace Local SDKドキュメント内のリンク修正 | modified | 1 | 1 | 2 | 
| [azure-open-ai-gpt-4v-tool.md](#item-053d0d) | minor update | Azure Open AI GPT-4Vツールドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [content-safety-tool.md](#item-09b048) | minor update | コンテンツ安全ツールドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [embedding-tool.md](#item-81420c) | minor update | 埋め込みツールドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [index-lookup-tool.md](#item-cad66d) | minor update | インデックスルックアップツールドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [llm-tool.md](#item-6691f4) | minor update | LLMツールドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [prompt-flow-tools-overview.md](#item-fd7471) | minor update | プロンプトフローツールの概要ドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [prompt-tool.md](#item-c6a9a0) | minor update | プロンプトツールドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [python-tool.md](#item-c9200f) | minor update | Pythonツールドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [rerank-tool.md](#item-dd52bf) | minor update | リランクツールドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [azure-openai-gpt-4-vision-tool.png](#item-94def5) | minor update | GPT-4ビジョンツールの画像メタデータの更新 | modified | 0 | 0 | 0 | 
| [content-safety-tool.png](#item-c673ee) | minor update | コンテンツセーフティツールの画像メタデータの更新 | modified | 0 | 0 | 0 | 
| [prompt-tool.png](#item-245957) | minor update | プロンプトツールの画像メタデータの更新 | modified | 0 | 0 | 0 | 
| [python-tool.png](#item-14e9b3) | minor update | Pythonツールの画像メタデータの更新 | modified | 0 | 0 | 0 | 
| [reference-model-inference-completions.md](#item-bae39d) | breaking change | モデル推論完了に関するリファレンスの削除 | removed | 0 | 296 | 296 | 
| [toc.yml](#item-2745cd) | minor update | TOCファイルの更新による新しいモデルの追加とリファレンスの整理 | modified | 3 | 13 | 16 | 


# Modified Contents
## articles/ai-studio/.openpublishing.redirection.ai-studio.json{#item-c75c21}

<details>
<summary>Diff</summary>
````diff
@@ -180,6 +180,11 @@
             "redirect_url": "/azure/ai-studio/concepts/content-filtering",
             "redirect_document_id": false
         },
+        {
+            "source_path_from_root": "/articles/ai-studio/reference/reference-model-inference-completions.md",
+            "redirect_url": "/azure/ai-studio/reference/reference-model-inference-chat-completions",
+            "redirect_document_id": false
+        },
         {
             "source_path_from_root": "/articles/ai-studio/concepts/evaluation-improvement-strategies.md",
             "redirect_url": "/azure/ai-studio/concepts/evaluation-approach-gen-ai",
@@ -207,8 +212,8 @@
           },
           {
             "source_path_from_root": "/articles/ai-studio/ai-services/how-to/content-safety.md",
-            "redirect_url": "/azure/ai-foundry/model-inference/how-to/configure-content-filters",
-            "redirect_document_id": false
+            "redirect_url": "/azure/ai-services/content-safety/how-to/foundry",
+            "redirect_document_id": true
           },
           {
             "source_path_from_root": "/articles/ai-studio/ai-services/concepts/quotas-limits.md",
@@ -234,6 +239,31 @@
               "source_path_from_root": "/articles/ai-studio/how-to/data-image-add.md",
               "redirect_url": "/azure/ai-studio/quickstarts/multimodal-vision",
               "redirect_document_id": false
+          },
+          {
+            "source_path_from_root": "/articles/ai-studio/reference/reference-model-inference-api.md",
+            "redirect_url": "/azure/ai-foundry/model-inference/reference/reference-model-inference-api",
+            "redirect_document_id": false
+          },
+          {
+            "source_path_from_root": "/articles/ai-studio/reference/reference-model-inference-info.md",
+            "redirect_url": "/azure/ai-foundry/model-inference/reference/reference-model-inference-info",
+            "redirect_document_id": false
+          },
+          {
+            "source_path_from_root": "/articles/ai-studio/reference/reference-model-inference-embeddings.md",
+            "redirect_url": "/azure/ai-foundry/model-inference/reference/reference-model-inference-embeddings",
+            "redirect_document_id": false
+          },
+          {
+            "source_path_from_root": "/articles/ai-studio/reference/reference-model-inference-chat-completions.md",
+            "redirect_url": "/azure/ai-foundry/model-inference/reference/reference-model-inference-chat-completions",
+            "redirect_document_id": false
+          },
+          {
+            "source_path_from_root": "/articles/ai-studio/reference/reference-model-inference-images-embeddings.md",
+            "redirect_url": "/azure/ai-foundry/model-inference/reference/reference-model-inference-images-embeddings",
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
    "modification_title": "AI Studioのリダイレクト設定の更新"
}
```

### Explanation
このコードの変更は、AI Studioに関連するリダイレクト設定を更新するためのものです。具体的には、リダイレクトを行う新しいエントリの追加と既存エントリの修正が行われています。

変更内容としては、32行が新たに追加され、2行が削除されました。これにより、"reference-model-inference-completions" および "reference-model-inference-chat-completions" などの新しいリファレンスに対するリダイレクトURLが構成されています。また、既存のリダイレクトURLも更新されており、特定のドキュメントIDの利用可否が変更されています。

この修正により、ユーザーは新しく追加されたリダイレクトURLを介してでも、関連するAI Studioのリファレンス文書へアクセスできるようになります。全体として、AI Studioに関する情報の提供が向上しています。

## articles/ai-studio/breadcrumb/toc.yml{#item-cd87b7}

<details>
<summary>Diff</summary>
````diff
@@ -2,6 +2,9 @@
   tocHref: /azure/
   topicHref: /azure/index
   items:
-  - name: Azure AI Foundry
+  - name: AI Foundry
     tocHref: /azure/ai-studio/
     topicHref: /azure/ai-studio/index
+  - name: AI Foundry
+    tocHref: /azure/ai-services/
+    topicHref: /azure/ai-studio/index
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Studioの目次設定の更新"
}
```

### Explanation
このコードの変更は、AI Studioの目次設定を更新したものです。具体的には、目次のYAMLファイルに対して4行が追加され、1行が削除されました。これにより、AI Foundryに関する情報の表示が改善され、ユーザーがナビゲートしやすくなっています。

変更点としては、"Azure AI Foundry" の名称が "AI Foundry" に簡略化され、同じ名前の項目が新たに追加されて、AIサービスに関連する新しいリンクも設定されています。これにより、AI Studio内での関連情報へのアクセスが向上し、目次が一層整理された形となっています。

この修正は、AI Studioのユーザーエクスペリエンスを向上させるために重要な更新です。

## articles/ai-studio/how-to/deploy-models-cohere-command.md{#item-3e97f4}

<details>
<summary>Diff</summary>
````diff
@@ -2161,7 +2161,7 @@ For more information on how to track costs, see [Monitor costs for models offere
 ## Related content
 
 
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cohereコマンドでのモデルデプロイに関するドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、Cohereコマンドを使用したモデルデプロイに関するドキュメント内のリンクを更新するためのものです。具体的には、1行が追加され、1行が削除される形で変更が行われました。

変更点としては、"Azure AI Model Inference API" に関するリンクパスが修正され、相対パスが更新されています。元のリンクは相対パスが誤っていたため、正しい場所へのリンクに調整されました。この更新により、ユーザーはAzure AI Model Inference APIに関する正確な情報に簡単にアクセスできるようになります。

この修正は、関連コンテンツへのナビゲーションを改善し、ユーザー体験を向上させるために重要です。

## articles/ai-studio/how-to/deploy-models-cohere-embed.md{#item-eab662}

<details>
<summary>Diff</summary>
````diff
@@ -663,7 +663,7 @@ Quota is managed per deployment. Each deployment has a rate limit of 200,000 tok
 ## Related content
 
 
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cohere埋め込みモデルデプロイに関するドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、Cohere埋め込みモデルをデプロイするためのドキュメント内のリンクを更新するものです。具体的には、1行が追加され、1行が削除される形での修正が行われました。

主な変更点は、"Azure AI Model Inference API" へのリンクの相対パスが修正され、誤りを正すために新しいパスが設定されています。この修正により、ユーザーがAzure AI Model Inference APIに関する正確な情報へのアクセスが容易になります。

このアップデートは、関連コンテンツのナビゲーションをよりスムーズにし、ユーザー体験を向上させるために重要です。

## articles/ai-studio/how-to/deploy-models-deepseek.md{#item-7c33de}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,1150 @@
+---
+title: How to use DeepSeek-R1 reasoning model with Azure AI Foundry
+titleSuffix: Azure AI Foundry
+description: Learn how to use DeepSeek-R1 reasoning model with Azure AI Foundry.
+manager: scottpolly
+author: msakande
+reviewer: santiagxf
+ms.service: azure-ai-studio
+ms.topic: how-to
+ms.date: 01/29/2025
+ms.author: mopeakande
+ms.reviewer: fasantia
+ms.custom: references_regions, generated
+zone_pivot_groups: azure-ai-model-catalog-samples-chat
+---
+
+# How to use DeepSeek-R1 reasoning model
+
+[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+
+In this article, you learn about DeepSeek-R1 and how to use them.
+DeepSeek-R1 excels at reasoning tasks using a step-by-step training process, such as language, scientific reasoning, and coding tasks. It features 671B total parameters with 37B active parameters, and 128k context length.
+
+
+
+::: zone pivot="programming-language-python"
+
+## DeepSeek-R1
+
+DeepSeek-R1 builds on the progress of earlier reasoning-focused models that improved performance by extending Chain-of-Thought (CoT) reasoning. DeepSeek-R1 takes things further by combining reinforcement learning (RL) with fine-tuning on carefully chosen datasets. It evolved from an earlier version, DeepSeek-R1-Zero, which relied solely on RL and showed strong reasoning skills but had issues like hard-to-read outputs and language inconsistencies. To address these limitations, DeepSeek-R1 incorporates a small amount of cold-start data and follows a refined training pipeline that blends reasoning-oriented RL with supervised fine-tuning on curated datasets, resulting in a model that achieves state-of-the-art performance on reasoning benchmarks.
+
+
+You can learn more about the models in their respective model card:
+
+* [DeepSeek-R1](https://aka.ms/azureai/landing/DeepSeek-R1)
+
+
+## Prerequisites
+
+To use DeepSeek-R1 with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to serverless APIs**
+
+DeepSeek-R1 can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Studio, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
+### The inference package installed
+
+You can consume predictions from this model by using the `azure-ai-inference` package with Python. To install this package, you need the following prerequisites:
+
+* Python 3.8 or later installed, including pip.
+* The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
+* Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
+  
+Once you have these prerequisites, install the Azure AI inference package with the following command:
+
+```bash
+pip install azure-ai-inference
+```
+
+Read more about the [Azure AI inference package and reference](https://aka.ms/azsdk/azure-ai-inference/python/reference).
+
+## Work with chat completions
+
+In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
+
+> [!TIP]
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry with the same code and structure, including DeepSeek-R1.
+
+### Create a client to consume the model
+
+First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
+
+
+```python
+import os
+from azure.ai.inference import ChatCompletionsClient
+from azure.core.credentials import AzureKeyCredential
+
+client = ChatCompletionsClient(
+    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    credential=AzureKeyCredential(os.environ["AZURE_INFERENCE_CREDENTIAL"]),
+)
+```
+
+### Get the model's capabilities
+
+The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
+
+
+```python
+model_info = client.get_model_info()
+```
+
+The response is as follows:
+
+
+```python
+print("Model name:", model_info.model_name)
+print("Model type:", model_info.model_type)
+print("Model provider name:", model_info.model_provider_name)
+```
+
+```console
+Model name: DeepSeek-R1
+Model type: chat-completions
+Model provider name: DeepSeek
+```
+
+### Create a chat completion request
+
+The following example shows how you can create a basic chat completions request to the model.
+
+```python
+from azure.ai.inference.models import SystemMessage, UserMessage
+
+response = client.complete(
+    messages=[
+        SystemMessage(content="You are a helpful assistant."),
+        UserMessage(content="How many languages are in the world?"),
+    ],
+)
+```
+
+The response is as follows, where you can see the model's usage statistics:
+
+
+```python
+print("Response:", response.choices[0].message.content)
+print("Model:", response.model)
+print("Usage:")
+print("\tPrompt tokens:", response.usage.prompt_tokens)
+print("\tTotal tokens:", response.usage.total_tokens)
+print("\tCompletion tokens:", response.usage.completion_tokens)
+```
+
+```console
+Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
+Model: DeepSeek-R1
+Usage: 
+  Prompt tokens: 19
+  Total tokens: 91
+  Completion tokens: 72
+```
+
+Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
+
+#### Understanding reasoning
+
+Some reasoning models, like DeepSeek-R1, generate completions and include the reasoning behind it. The reasoning associated with the completion is included in the response's content within the tags `<think>` and `</think>`. The model may select on which scenarios to generate reasoning content. For example:
+
+
+```python
+response = client.complete(
+    messages=[
+        SystemMessage(content="You are a helpful assistant."),
+        UserMessage(content="How many languages are in the world?"),
+    ],
+)
+```
+
+You can extract the reasoning content from the response to understand the model's thought process as follows:
+
+
+```python
+import re
+
+match = re.match(r"<think>(.*?)</think>(.*)", response.choices[0].message.content, re.DOTALL)
+
+print("Response:", )
+if match:
+    print("\tThinking:", match.group(1))
+    print("\tAnswer:", match.group(2))
+else:
+    print("\tAnswer:", response.choices[0].message.content)
+print("Model:", response.model)
+print("Usage:")
+print("\tPrompt tokens:", response.usage.prompt_tokens)
+print("\tTotal tokens:", response.usage.total_tokens)
+print("\tCompletion tokens:", response.usage.completion_tokens)
+```
+
+```console
+Thinking: Okay, the user is asking how many languages exist in the world. I need to provide a clear and accurate answer. Let's start by recalling the general consensus from linguistic sources. I remember that the number often cited is around 7,000, but maybe I should check some reputable organizations.\n\nEthnologue is a well-known resource for language data, and I think they list about 7,000 languages. But wait, do they update their numbers? It might be around 7,100 or so. Also, the exact count can vary because some sources might categorize dialects differently or have more recent data. \n\nAnother thing to consider is language endangerment. Many languages are endangered, with some having only a few speakers left. Organizations like UNESCO track endangered languages, so mentioning that adds context. Also, the distribution isn't even. Some countries have hundreds of languages, like Papua New Guinea with over 800, while others have just a few. \n\nA user might also wonder why the exact number is hard to pin down. It's because the distinction between a language and a dialect can be political or cultural. For example, Mandarin and Cantonese are considered dialects of Chinese by some, but they're mutually unintelligible, so others classify them as separate languages. Also, some regions are under-researched, making it hard to document all languages. \n\nI should also touch on language families. The 7,000 languages are grouped into families like Indo-European, Sino-Tibetan, Niger-Congo, etc. Maybe mention a few of the largest families. But wait, the question is just about the count, not the families. Still, it's good to provide a bit more context. \n\nI need to make sure the information is up-to-date. Let me think – recent estimates still hover around 7,000. However, languages are dying out rapidly, so the number decreases over time. Including that note about endangerment and language extinction rates could be helpful. For instance, it's often stated that a language dies every few weeks. \n\nAnother point is sign languages. Does the count include them? Ethnologue includes some, but not all sources might. If the user is including sign languages, that adds more to the count, but I think the 7,000 figure typically refers to spoken languages. For thoroughness, maybe mention that there are also over 300 sign languages. \n\nSummarizing, the answer should state around 7,000, mention Ethnologue's figure, explain why the exact number varies, touch on endangerment, and possibly note sign languages as a separate category. Also, a brief mention of Papua New Guinea as the most linguistically diverse country. \n\nWait, let me verify Ethnologue's current number. As of their latest edition (25th, 2022), they list 7,168 living languages. But I should check if that's the case. Some sources might round to 7,000. Also, SIL International publishes Ethnologue, so citing them as reference makes sense. \n\nOther sources, like Glottolog, might have a different count because they use different criteria. Glottolog might list around 7,000 as well, but exact numbers vary. It's important to highlight that the count isn't exact because of differing definitions and ongoing research. \n\nIn conclusion, the approximate number is 7,000, with Ethnologue being a key source, considerations of endangerment, and the challenges in counting due to dialect vs. language distinctions. I should make sure the answer is clear, acknowledges the variability, and provides key points succinctly.
+
+Answer: The exact number of languages in the world is challenging to determine due to differences in definitions (e.g., distinguishing languages from dialects) and ongoing documentation efforts. However, widely cited estimates suggest there are approximately **7,000 languages** globally.
+Model: DeepSeek-R1
+Usage: 
+  Prompt tokens: 11
+  Total tokens: 897
+  Completion tokens: 886
+```
+
+#### Stream content
+
+By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
+
+You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
+
+
+```python
+result = client.complete(
+    messages=[
+        SystemMessage(content="You are a helpful assistant."),
+        UserMessage(content="How many languages are in the world?"),
+    ],
+    temperature=0,
+    top_p=1,
+    max_tokens=2048,
+    stream=True,
+)
+```
+
+To stream completions, set `stream=True` when you call the model.
+
+To visualize the output, define a helper function to print the stream.
+
+```python
+def print_stream(result):
+    """
+    Prints the chat completion with streaming.
+    """
+    for update in result:
+        if update.choices:
+            print(update.choices[0].delta.content, end="")
+```
+
+You can visualize how streaming generates content:
+
+
+```python
+print_stream(result)
+```
+
+### Apply content safety
+
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+
+The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
+
+
+```python
+from azure.ai.inference.models import AssistantMessage, UserMessage, SystemMessage
+
+try:
+    response = client.complete(
+        messages=[
+            SystemMessage(content="You are an AI assistant that helps people find information."),
+            UserMessage(content="Chopping tomatoes and cutting them into cubes or wedges are great ways to practice your knife skills."),
+        ]
+    )
+
+    print(response.choices[0].message.content)
+
+except HttpResponseError as ex:
+    if ex.status_code == 400:
+        response = ex.response.json()
+        if isinstance(response, dict) and "error" in response:
+            print(f"Your request triggered an {response['error']['code']} error:\n\t {response['error']['message']}")
+        else:
+            raise
+    raise
+```
+
+> [!TIP]
+> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+
+::: zone-end
+
+
+::: zone pivot="programming-language-javascript"
+
+## DeepSeek-R1
+
+DeepSeek-R1 builds on the progress of earlier reasoning-focused models that improved performance by extending Chain-of-Thought (CoT) reasoning. DeepSeek-R1 takes things further by combining reinforcement learning (RL) with fine-tuning on carefully chosen datasets. It evolved from an earlier version, DeepSeek-R1-Zero, which relied solely on RL and showed strong reasoning skills but had issues like hard-to-read outputs and language inconsistencies. To address these limitations, DeepSeek-R1 incorporates a small amount of cold-start data and follows a refined training pipeline that blends reasoning-oriented RL with supervised fine-tuning on curated datasets, resulting in a model that achieves state-of-the-art performance on reasoning benchmarks.
+
+
+You can learn more about the models in their respective model card:
+
+* [DeepSeek-R1](https://aka.ms/azureai/landing/DeepSeek-R1)
+
+
+## Prerequisites
+
+To use DeepSeek-R1 with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to serverless APIs**
+
+DeepSeek-R1 can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Studio, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
+### The inference package installed
+
+You can consume predictions from this model by using the `@azure-rest/ai-inference` package from `npm`. To install this package, you need the following prerequisites:
+
+* LTS versions of `Node.js` with `npm`.
+* The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
+* Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
+
+Once you have these prerequisites, install the Azure Inference library for JavaScript with the following command:
+
+```bash
+npm install @azure-rest/ai-inference
+```
+
+## Work with chat completions
+
+In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
+
+> [!TIP]
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry with the same code and structure, including DeepSeek-R1.
+
+### Create a client to consume the model
+
+First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
+
+
+```javascript
+import ModelClient from "@azure-rest/ai-inference";
+import { isUnexpected } from "@azure-rest/ai-inference";
+import { AzureKeyCredential } from "@azure/core-auth";
+
+const client = new ModelClient(
+    process.env.AZURE_INFERENCE_ENDPOINT, 
+    new AzureKeyCredential(process.env.AZURE_INFERENCE_CREDENTIAL)
+);
+```
+
+### Get the model's capabilities
+
+The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
+
+
+```javascript
+var model_info = await client.path("/info").get()
+```
+
+The response is as follows:
+
+
+```javascript
+console.log("Model name: ", model_info.body.model_name)
+console.log("Model type: ", model_info.body.model_type)
+console.log("Model provider name: ", model_info.body.model_provider_name)
+```
+
+```console
+Model name: DeepSeek-R1
+Model type: chat-completions
+Model provider name: DeepSeek
+```
+
+### Create a chat completion request
+
+The following example shows how you can create a basic chat completions request to the model.
+
+```javascript
+var messages = [
+    { role: "system", content: "You are a helpful assistant" },
+    { role: "user", content: "How many languages are in the world?" },
+];
+
+var response = await client.path("/chat/completions").post({
+    body: {
+        messages: messages,
+    }
+});
+```
+
+The response is as follows, where you can see the model's usage statistics:
+
+
+```javascript
+if (isUnexpected(response)) {
+    throw response.body.error;
+}
+
+console.log("Response: ", response.body.choices[0].message.content);
+console.log("Model: ", response.body.model);
+console.log("Usage:");
+console.log("\tPrompt tokens:", response.body.usage.prompt_tokens);
+console.log("\tTotal tokens:", response.body.usage.total_tokens);
+console.log("\tCompletion tokens:", response.body.usage.completion_tokens);
+```
+
+```console
+Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
+Model: DeepSeek-R1
+Usage: 
+  Prompt tokens: 19
+  Total tokens: 91
+  Completion tokens: 72
+```
+
+Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
+
+#### Understanding reasoning
+
+Some reasoning models, like DeepSeek-R1, generate completions and include the reasoning behind it. The reasoning associated with the completion is included in the response's content within the tags `<think>` and `</think>`. The model may select on which scenarios to generate reasoning content. For example:
+
+
+```javascript
+var messages = [
+    { role: "system", content: "You are a helpful assistant" },
+    { role: "user", content: "How many languages are in the world?" },
+];
+
+var response = await client.path("/chat/completions").post({
+    body: {
+        messages: messages,
+    }
+});
+```
+
+You can extract the reasoning content from the response to understand the model's thought process as follows:
+
+
+```javascript
+var content = response.body.choices[0].message.content
+var match = content.match(/<think>(.*?)<\/think>(.*)/s);
+
+console.log("Response:");
+if (match) {
+    console.log("\tThinking:", match[1]);
+    console.log("\Answer:", match[2]);
+}
+else {
+    console.log("Response:", content);
+}
+console.log("Model: ", response.body.model);
+console.log("Usage:");
+console.log("\tPrompt tokens:", response.body.usage.prompt_tokens);
+console.log("\tTotal tokens:", response.body.usage.total_tokens);
+console.log("\tCompletion tokens:", response.body.usage.completion_tokens);
+```
+
+```console
+Thinking: Okay, the user is asking how many languages exist in the world. I need to provide a clear and accurate answer. Let's start by recalling the general consensus from linguistic sources. I remember that the number often cited is around 7,000, but maybe I should check some reputable organizations.\n\nEthnologue is a well-known resource for language data, and I think they list about 7,000 languages. But wait, do they update their numbers? It might be around 7,100 or so. Also, the exact count can vary because some sources might categorize dialects differently or have more recent data. \n\nAnother thing to consider is language endangerment. Many languages are endangered, with some having only a few speakers left. Organizations like UNESCO track endangered languages, so mentioning that adds context. Also, the distribution isn't even. Some countries have hundreds of languages, like Papua New Guinea with over 800, while others have just a few. \n\nA user might also wonder why the exact number is hard to pin down. It's because the distinction between a language and a dialect can be political or cultural. For example, Mandarin and Cantonese are considered dialects of Chinese by some, but they're mutually unintelligible, so others classify them as separate languages. Also, some regions are under-researched, making it hard to document all languages. \n\nI should also touch on language families. The 7,000 languages are grouped into families like Indo-European, Sino-Tibetan, Niger-Congo, etc. Maybe mention a few of the largest families. But wait, the question is just about the count, not the families. Still, it's good to provide a bit more context. \n\nI need to make sure the information is up-to-date. Let me think – recent estimates still hover around 7,000. However, languages are dying out rapidly, so the number decreases over time. Including that note about endangerment and language extinction rates could be helpful. For instance, it's often stated that a language dies every few weeks. \n\nAnother point is sign languages. Does the count include them? Ethnologue includes some, but not all sources might. If the user is including sign languages, that adds more to the count, but I think the 7,000 figure typically refers to spoken languages. For thoroughness, maybe mention that there are also over 300 sign languages. \n\nSummarizing, the answer should state around 7,000, mention Ethnologue's figure, explain why the exact number varies, touch on endangerment, and possibly note sign languages as a separate category. Also, a brief mention of Papua New Guinea as the most linguistically diverse country. \n\nWait, let me verify Ethnologue's current number. As of their latest edition (25th, 2022), they list 7,168 living languages. But I should check if that's the case. Some sources might round to 7,000. Also, SIL International publishes Ethnologue, so citing them as reference makes sense. \n\nOther sources, like Glottolog, might have a different count because they use different criteria. Glottolog might list around 7,000 as well, but exact numbers vary. It's important to highlight that the count isn't exact because of differing definitions and ongoing research. \n\nIn conclusion, the approximate number is 7,000, with Ethnologue being a key source, considerations of endangerment, and the challenges in counting due to dialect vs. language distinctions. I should make sure the answer is clear, acknowledges the variability, and provides key points succinctly.
+
+Answer: The exact number of languages in the world is challenging to determine due to differences in definitions (e.g., distinguishing languages from dialects) and ongoing documentation efforts. However, widely cited estimates suggest there are approximately **7,000 languages** globally.
+Model: DeepSeek-R1
+Usage: 
+  Prompt tokens: 11
+  Total tokens: 897
+  Completion tokens: 886
+```
+
+#### Stream content
+
+By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
+
+You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
+
+
+```javascript
+var messages = [
+    { role: "system", content: "You are a helpful assistant" },
+    { role: "user", content: "How many languages are in the world?" },
+];
+
+var response = await client.path("/chat/completions").post({
+    body: {
+        messages: messages,
+    }
+}).asNodeStream();
+```
+
+To stream completions, use `.asNodeStream()` when you call the model.
+
+You can visualize how streaming generates content:
+
+
+```javascript
+var stream = response.body;
+if (!stream) {
+    stream.destroy();
+    throw new Error(`Failed to get chat completions with status: ${response.status}`);
+}
+
+if (response.status !== "200") {
+    throw new Error(`Failed to get chat completions: ${response.body.error}`);
+}
+
+var sses = createSseStream(stream);
+
+for await (const event of sses) {
+    if (event.data === "[DONE]") {
+        return;
+    }
+    for (const choice of (JSON.parse(event.data)).choices) {
+        console.log(choice.delta?.content ?? "");
+    }
+}
+```
+
+### Apply content safety
+
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+
+The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
+
+
+```javascript
+try {
+    var messages = [
+        { role: "system", content: "You are an AI assistant that helps people find information." },
+        { role: "user", content: "Chopping tomatoes and cutting them into cubes or wedges are great ways to practice your knife skills." },
+    ];
+
+    var response = await client.path("/chat/completions").post({
+        body: {
+            messages: messages,
+        }
+    });
+
+    console.log(response.body.choices[0].message.content);
+}
+catch (error) {
+    if (error.status_code == 400) {
+        var response = JSON.parse(error.response._content);
+        if (response.error) {
+            console.log(`Your request triggered an ${response.error.code} error:\n\t ${response.error.message}`);
+        }
+        else
+        {
+            throw error;
+        }
+    }
+}
+```
+
+> [!TIP]
+> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+
+::: zone-end
+
+
+::: zone pivot="programming-language-csharp"
+
+## DeepSeek-R1
+
+DeepSeek-R1 builds on the progress of earlier reasoning-focused models that improved performance by extending Chain-of-Thought (CoT) reasoning. DeepSeek-R1 takes things further by combining reinforcement learning (RL) with fine-tuning on carefully chosen datasets. It evolved from an earlier version, DeepSeek-R1-Zero, which relied solely on RL and showed strong reasoning skills but had issues like hard-to-read outputs and language inconsistencies. To address these limitations, DeepSeek-R1 incorporates a small amount of cold-start data and follows a refined training pipeline that blends reasoning-oriented RL with supervised fine-tuning on curated datasets, resulting in a model that achieves state-of-the-art performance on reasoning benchmarks.
+
+
+You can learn more about the models in their respective model card:
+
+* [DeepSeek-R1](https://aka.ms/azureai/landing/DeepSeek-R1)
+
+
+## Prerequisites
+
+To use DeepSeek-R1 with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to serverless APIs**
+
+DeepSeek-R1 can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Studio, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
+### The inference package installed
+
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
+
+* The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
+* Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
+
+Once you have these prerequisites, install the Azure AI inference library with the following command:
+
+```dotnetcli
+dotnet add package Azure.AI.Inference --prerelease
+```
+
+You can also authenticate with Microsoft Entra ID (formerly Azure Active Directory). To use credential providers provided with the Azure SDK, install the `Azure.Identity` package:
+
+```dotnetcli
+dotnet add package Azure.Identity
+```
+
+Import the following namespaces:
+
+
+```csharp
+using Azure;
+using Azure.Identity;
+using Azure.AI.Inference;
+```
+
+This example also uses the following namespaces but you may not always need them:
+
+
+```csharp
+using System.Text.Json;
+using System.Text.Json.Serialization;
+using System.Reflection;
+```
+
+## Work with chat completions
+
+In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
+
+> [!TIP]
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry with the same code and structure, including DeepSeek-R1.
+
+### Create a client to consume the model
+
+First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
+
+
+```csharp
+ChatCompletionsClient client = new ChatCompletionsClient(
+    new Uri(Environment.GetEnvironmentVariable("AZURE_INFERENCE_ENDPOINT")),
+    new AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_INFERENCE_CREDENTIAL")),
+    "DeepSeek-R1"
+);
+```
+
+### Get the model's capabilities
+
+The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
+
+
+```csharp
+Response<ModelInfo> modelInfo = client.GetModelInfo();
+```
+
+The response is as follows:
+
+
+```csharp
+Console.WriteLine($"Model name: {modelInfo.Value.ModelName}");
+Console.WriteLine($"Model type: {modelInfo.Value.ModelType}");
+Console.WriteLine($"Model provider name: {modelInfo.Value.ModelProviderName}");
+```
+
+```console
+Model name: DeepSeek-R1
+Model type: chat-completions
+Model provider name: DeepSeek
+```
+
+### Create a chat completion request
+
+The following example shows how you can create a basic chat completions request to the model.
+
+```csharp
+ChatCompletionsOptions requestOptions = new ChatCompletionsOptions()
+{
+    Messages = {
+        new ChatRequestSystemMessage("You are a helpful assistant."),
+        new ChatRequestUserMessage("How many languages are in the world?")
+    },
+};
+
+Response<ChatCompletions> response = client.Complete(requestOptions);
+```
+
+The response is as follows, where you can see the model's usage statistics:
+
+
+```csharp
+Console.WriteLine($"Response: {response.Value.Content}");
+Console.WriteLine($"Model: {response.Value.Model}");
+Console.WriteLine("Usage:");
+Console.WriteLine($"\tPrompt tokens: {response.Value.Usage.PromptTokens}");
+Console.WriteLine($"\tTotal tokens: {response.Value.Usage.TotalTokens}");
+Console.WriteLine($"\tCompletion tokens: {response.Value.Usage.CompletionTokens}");
+```
+
+```console
+Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
+Model: DeepSeek-R1
+Usage: 
+  Prompt tokens: 19
+  Total tokens: 91
+  Completion tokens: 72
+```
+
+Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
+
+#### Understanding reasoning
+
+Some reasoning models, like DeepSeek-R1, generate completions and include the reasoning behind it. The reasoning associated with the completion is included in the response's content within the tags `<think>` and `</think>`. The model may select on which scenarios to generate reasoning content. For example:
+
+
+```csharp
+ChatCompletionsOptions requestOptions = new ChatCompletionsOptions()
+{
+    Messages = {
+        new ChatRequestSystemMessage("You are a helpful assistant."),
+        new ChatRequestUserMessage("How many languages are in the world?")
+    },
+};
+
+Response<ChatCompletions> response = client.Complete(requestOptions);
+```
+
+You can extract the reasoning content from the response to understand the model's thought process as follows:
+
+
+```csharp
+Regex regex = new Regex(pattern, RegexOptions.Singleline);
+Match match = regex.Match(response.Value.Content);
+
+Console.WriteLine("Response:");
+if (match.Success)
+{
+    Console.WriteLine($"\tThinking: {match.Groups[1].Value}");
+    Console.WriteLine($"\tAnswer: {match.Groups[2].Value}");
+else
+{
+    Console.WriteLine($"Response: {response.Value.Content}");
+}
+Console.WriteLine($"Model: {response.Value.Model}");
+Console.WriteLine("Usage:");
+Console.WriteLine($"\tPrompt tokens: {response.Value.Usage.PromptTokens}");
+Console.WriteLine($"\tTotal tokens: {response.Value.Usage.TotalTokens}");
+Console.WriteLine($"\tCompletion tokens: {response.Value.Usage.CompletionTokens}");
+```
+
+```console
+Thinking: Okay, the user is asking how many languages exist in the world. I need to provide a clear and accurate answer. Let's start by recalling the general consensus from linguistic sources. I remember that the number often cited is around 7,000, but maybe I should check some reputable organizations.\n\nEthnologue is a well-known resource for language data, and I think they list about 7,000 languages. But wait, do they update their numbers? It might be around 7,100 or so. Also, the exact count can vary because some sources might categorize dialects differently or have more recent data. \n\nAnother thing to consider is language endangerment. Many languages are endangered, with some having only a few speakers left. Organizations like UNESCO track endangered languages, so mentioning that adds context. Also, the distribution isn't even. Some countries have hundreds of languages, like Papua New Guinea with over 800, while others have just a few. \n\nA user might also wonder why the exact number is hard to pin down. It's because the distinction between a language and a dialect can be political or cultural. For example, Mandarin and Cantonese are considered dialects of Chinese by some, but they're mutually unintelligible, so others classify them as separate languages. Also, some regions are under-researched, making it hard to document all languages. \n\nI should also touch on language families. The 7,000 languages are grouped into families like Indo-European, Sino-Tibetan, Niger-Congo, etc. Maybe mention a few of the largest families. But wait, the question is just about the count, not the families. Still, it's good to provide a bit more context. \n\nI need to make sure the information is up-to-date. Let me think – recent estimates still hover around 7,000. However, languages are dying out rapidly, so the number decreases over time. Including that note about endangerment and language extinction rates could be helpful. For instance, it's often stated that a language dies every few weeks. \n\nAnother point is sign languages. Does the count include them? Ethnologue includes some, but not all sources might. If the user is including sign languages, that adds more to the count, but I think the 7,000 figure typically refers to spoken languages. For thoroughness, maybe mention that there are also over 300 sign languages. \n\nSummarizing, the answer should state around 7,000, mention Ethnologue's figure, explain why the exact number varies, touch on endangerment, and possibly note sign languages as a separate category. Also, a brief mention of Papua New Guinea as the most linguistically diverse country. \n\nWait, let me verify Ethnologue's current number. As of their latest edition (25th, 2022), they list 7,168 living languages. But I should check if that's the case. Some sources might round to 7,000. Also, SIL International publishes Ethnologue, so citing them as reference makes sense. \n\nOther sources, like Glottolog, might have a different count because they use different criteria. Glottolog might list around 7,000 as well, but exact numbers vary. It's important to highlight that the count isn't exact because of differing definitions and ongoing research. \n\nIn conclusion, the approximate number is 7,000, with Ethnologue being a key source, considerations of endangerment, and the challenges in counting due to dialect vs. language distinctions. I should make sure the answer is clear, acknowledges the variability, and provides key points succinctly.
+
+Answer: The exact number of languages in the world is challenging to determine due to differences in definitions (e.g., distinguishing languages from dialects) and ongoing documentation efforts. However, widely cited estimates suggest there are approximately **7,000 languages** globally.
+Model: DeepSeek-R1
+Usage: 
+  Prompt tokens: 11
+  Total tokens: 897
+  Completion tokens: 886
+```
+
+#### Stream content
+
+By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
+
+You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
+
+
+```csharp
+static async Task StreamMessageAsync(ChatCompletionsClient client)
+{
+    ChatCompletionsOptions requestOptions = new ChatCompletionsOptions()
+    {
+        Messages = {
+            new ChatRequestSystemMessage("You are a helpful assistant."),
+            new ChatRequestUserMessage("How many languages are in the world? Write an essay about it.")
+        },
+        MaxTokens=4096
+    };
+
+    StreamingResponse<StreamingChatCompletionsUpdate> streamResponse = await client.CompleteStreamingAsync(requestOptions);
+
+    await PrintStream(streamResponse);
+}
+```
+
+To stream completions, use `CompleteStreamingAsync` method when you call the model. Notice that in this example we the call is wrapped in an asynchronous method.
+
+To visualize the output, define an asynchronous method to print the stream in the console.
+
+```csharp
+static async Task PrintStream(StreamingResponse<StreamingChatCompletionsUpdate> response)
+{
+    await foreach (StreamingChatCompletionsUpdate chatUpdate in response)
+    {
+        if (chatUpdate.Role.HasValue)
+        {
+            Console.Write($"{chatUpdate.Role.Value.ToString().ToUpperInvariant()}: ");
+        }
+        if (!string.IsNullOrEmpty(chatUpdate.ContentUpdate))
+        {
+            Console.Write(chatUpdate.ContentUpdate);
+        }
+    }
+}
+```
+
+You can visualize how streaming generates content:
+
+
+```csharp
+StreamMessageAsync(client).GetAwaiter().GetResult();
+```
+
+### Apply content safety
+
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+
+The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
+
+
+```csharp
+try
+{
+    requestOptions = new ChatCompletionsOptions()
+    {
+        Messages = {
+            new ChatRequestSystemMessage("You are an AI assistant that helps people find information."),
+            new ChatRequestUserMessage(
+                "Chopping tomatoes and cutting them into cubes or wedges are great ways to practice your knife skills."
+            ),
+        },
+    };
+
+    response = client.Complete(requestOptions);
+    Console.WriteLine(response.Value.Content);
+}
+catch (RequestFailedException ex)
+{
+    if (ex.ErrorCode == "content_filter")
+    {
+        Console.WriteLine($"Your query has trigger Azure Content Safety: {ex.Message}");
+    }
+    else
+    {
+        throw;
+    }
+}
+```
+
+> [!TIP]
+> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+
+::: zone-end
+
+
+::: zone pivot="programming-language-rest"
+
+## DeepSeek-R1
+
+DeepSeek-R1 builds on the progress of earlier reasoning-focused models that improved performance by extending Chain-of-Thought (CoT) reasoning. DeepSeek-R1 takes things further by combining reinforcement learning (RL) with fine-tuning on carefully chosen datasets. It evolved from an earlier version, DeepSeek-R1-Zero, which relied solely on RL and showed strong reasoning skills but had issues like hard-to-read outputs and language inconsistencies. To address these limitations, DeepSeek-R1 incorporates a small amount of cold-start data and follows a refined training pipeline that blends reasoning-oriented RL with supervised fine-tuning on curated datasets, resulting in a model that achieves state-of-the-art performance on reasoning benchmarks.
+
+
+You can learn more about the models in their respective model card:
+
+* [DeepSeek-R1](https://aka.ms/azureai/landing/DeepSeek-R1)
+
+
+## Prerequisites
+
+To use DeepSeek-R1 with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to serverless APIs**
+
+DeepSeek-R1 can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Studio, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
+### A REST client
+
+Models deployed with the [Azure AI model inference API](https://aka.ms/azureai/modelinference) can be consumed using any REST client. To use the REST client, you need the following prerequisites:
+
+* To construct the requests, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name`` is your unique model deployment host name and `your-azure-region`` is the Azure region where the model is deployed (for example, eastus2).
+* Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
+
+## Work with chat completions
+
+In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
+
+> [!TIP]
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry with the same code and structure, including DeepSeek-R1.
+
+### Create a client to consume the model
+
+First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
+
+### Get the model's capabilities
+
+The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
+
+```http
+GET /info HTTP/1.1
+Host: <ENDPOINT_URI>
+Authorization: Bearer <TOKEN>
+Content-Type: application/json
+```
+
+The response is as follows:
+
+
+```json
+{
+    "model_name": "DeepSeek-R1",
+    "model_type": "chat-completions",
+    "model_provider_name": "DeepSeek"
+}
+```
+
+### Create a chat completion request
+
+The following example shows how you can create a basic chat completions request to the model.
+
+```json
+{
+    "model": "DeepSeek-R1",
+    "messages": [
+        {
+            "role": "system",
+            "content": "You are a helpful assistant."
+        },
+        {
+            "role": "user",
+            "content": "How many languages are in the world?"
+        }
+    ]
+}
+```
+
+The response is as follows, where you can see the model's usage statistics:
+
+
+```json
+{
+    "id": "0a1234b5de6789f01gh2i345j6789klm",
+    "object": "chat.completion",
+    "created": 1718726686,
+    "model": "DeepSeek-R1",
+    "choices": [
+        {
+            "index": 0,
+            "message": {
+                "role": "assistant",
+                "content": "As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.",
+                "tool_calls": null
+            },
+            "finish_reason": "stop",
+            "logprobs": null
+        }
+    ],
+    "usage": {
+        "prompt_tokens": 19,
+        "total_tokens": 91,
+        "completion_tokens": 72
+    }
+}
+```
+
+Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
+
+#### Understanding reasoning
+
+Some reasoning models, like DeepSeek-R1, generate completions and include the reasoning behind it. The reasoning associated with the completion is included in the response's content within the tags `<think>` and `</think>`. The model may select on which scenarios to generate reasoning content. For example:
+
+
+```json
+{
+    "model": "DeepSeek-R1",
+    "messages": [
+        {
+            "role": "system",
+            "content": "You are a helpful assistant."
+        },
+        {
+            "role": "user",
+            "content": "How many languages are in the world?"
+        }
+    ]
+}
+```
+
+You can extract the reasoning content from the response to understand the model's thought process as follows:
+
+
+```json
+{
+    "id": "0a1234b5de6789f01gh2i345j6789klm",
+    "object": "chat.completion",
+    "created": 1718726686,
+    "model": "DeepSeek-R1",
+    "choices": [
+        {
+            "index": 0,
+            "message": {
+                "role": "assistant",
+                "content": "<think>\nOkay, the user is asking how many languages exist in the world. I need to provide a clear and accurate answer. Let's start by recalling the general consensus from linguistic sources. I remember that the number often cited is around 7,000, but maybe I should check some reputable organizations.\n\nEthnologue is a well-known resource for language data, and I think they list about 7,000 languages. But wait, do they update their numbers? It might be around 7,100 or so. Also, the exact count can vary because some sources might categorize dialects differently or have more recent data. \n\nAnother thing to consider is language endangerment. Many languages are endangered, with some having only a few speakers left. Organizations like UNESCO track endangered languages, so mentioning that adds context. Also, the distribution isn't even. Some countries have hundreds of languages, like Papua New Guinea with over 800, while others have just a few. \n\nA user might also wonder why the exact number is hard to pin down. It's because the distinction between a language and a dialect can be political or cultural. For example, Mandarin and Cantonese are considered dialects of Chinese by some, but they're mutually unintelligible, so others classify them as separate languages. Also, some regions are under-researched, making it hard to document all languages. \n\nI should also touch on language families. The 7,000 languages are grouped into families like Indo-European, Sino-Tibetan, Niger-Congo, etc. Maybe mention a few of the largest families. But wait, the question is just about the count, not the families. Still, it's good to provide a bit more context. \n\nI need to make sure the information is up-to-date. Let me think – recent estimates still hover around 7,000. However, languages are dying out rapidly, so the number decreases over time. Including that note about endangerment and language extinction rates could be helpful. For instance, it's often stated that a language dies every few weeks. \n\nAnother point is sign languages. Does the count include them? Ethnologue includes some, but not all sources might. If the user is including sign languages, that adds more to the count, but I think the 7,000 figure typically refers to spoken languages. For thoroughness, maybe mention that there are also over 300 sign languages. \n\nSummarizing, the answer should state around 7,000, mention Ethnologue's figure, explain why the exact number varies, touch on endangerment, and possibly note sign languages as a separate category. Also, a brief mention of Papua New Guinea as the most linguistically diverse country. \n\nWait, let me verify Ethnologue's current number. As of their latest edition (25th, 2022), they list 7,168 living languages. But I should check if that's the case. Some sources might round to 7,000. Also, SIL International publishes Ethnologue, so citing them as reference makes sense. \n\nOther sources, like Glottolog, might have a different count because they use different criteria. Glottolog might list around 7,000 as well, but exact numbers vary. It's important to highlight that the count isn't exact because of differing definitions and ongoing research. \n\nIn conclusion, the approximate number is 7,000, with Ethnologue being a key source, considerations of endangerment, and the challenges in counting due to dialect vs. language distinctions. I should make sure the answer is clear, acknowledges the variability, and provides key points succinctly.\n</think>\n\nThe exact number of languages in the world is challenging to determine due to differences in definitions (e.g., distinguishing languages from dialects) and ongoing documentation efforts. However, widely cited estimates suggest there are approximately **7,000 languages** globally.",
+                "tool_calls": null
+            },
+            "finish_reason": "stop"
+        }
+    ],
+    "usage": {
+        "prompt_tokens": 11,
+        "total_tokens": 897,
+        "completion_tokens": 886
+    }
+}
+```
+
+#### Stream content
+
+By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
+
+You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
+
+
+```json
+{
+    "model": "DeepSeek-R1",
+    "messages": [
+        {
+            "role": "system",
+            "content": "You are a helpful assistant."
+        },
+        {
+            "role": "user",
+            "content": "How many languages are in the world?"
+        }
+    ],
+    "stream": true,
+    "temperature": 0,
+    "top_p": 1,
+    "max_tokens": 2048
+}
+```
+
+You can visualize how streaming generates content:
+
+
+```json
+{
+    "id": "23b54589eba14564ad8a2e6978775a39",
+    "object": "chat.completion.chunk",
+    "created": 1718726371,
+    "model": "DeepSeek-R1",
+    "choices": [
+        {
+            "index": 0,
+            "delta": {
+                "role": "assistant",
+                "content": ""
+            },
+            "finish_reason": null,
+            "logprobs": null
+        }
+    ]
+}
+```
+
+The last message in the stream has `finish_reason` set, indicating the reason for the generation process to stop.
+
+
+```json
+{
+    "id": "23b54589eba14564ad8a2e6978775a39",
+    "object": "chat.completion.chunk",
+    "created": 1718726371,
+    "model": "DeepSeek-R1",
+    "choices": [
+        {
+            "index": 0,
+            "delta": {
+                "content": ""
+            },
+            "finish_reason": "stop",
+            "logprobs": null
+        }
+    ],
+    "usage": {
+        "prompt_tokens": 19,
+        "total_tokens": 91,
+        "completion_tokens": 72
+    }
+}
+```
+
+### Apply content safety
+
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+
+The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
+
+
+```json
+{
+    "model": "DeepSeek-R1",
+    "messages": [
+        {
+            "role": "system",
+            "content": "You are an AI assistant that helps people find information."
+        },
+                {
+            "role": "user",
+            "content": "Chopping tomatoes and cutting them into cubes or wedges are great ways to practice your knife skills."
+        }
+    ]
+}
+```
+
+
+```json
+{
+    "error": {
+        "message": "The response was filtered due to the prompt triggering Microsoft's content management policy. Please modify your prompt and retry.",
+        "type": null,
+        "param": "prompt",
+        "code": "content_filter",
+        "status": 400
+    }
+}
+```
+
+> [!TIP]
+> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+
+::: zone-end
+
+## More inference examples
+
+For more examples of how to use DeepSeek models, see the following examples and tutorials:
+
+| Description                               | Language          | Sample                                                          |
+|-------------------------------------------|-------------------|-----------------------------------------------------------------|
+| Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
+| Azure AI Inference package for C#         | C#                | [Link](https://aka.ms/azsdk/azure-ai-inference/csharp/samples)  |
+| Azure AI Inference package for Java       | Java              | [Link](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/ai/azure-ai-inference/src/samples)  |
+
+## Cost and quota considerations for DeepSeek models deployed as serverless API endpoints
+
+Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
+
+## Related content
+
+
+* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Deploy models as serverless APIs](deploy-models-serverless.md)
+* [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
+* [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "DeepSeek-R1推論モデルを使用する方法に関する新しいドキュメント"
}
```

### Explanation
このコードの変更は、DeepSeek-R1推論モデルをAzure AI Foundryで使用する方法に関する新しいドキュメントを追加することに関するものです。全体で1150行が追加され、深層学習モデルであるDeepSeek-R1に特化した内容を詳細に説明しています。

新しいドキュメントでは、DeepSeek-R1の特長、モデルの使用方法、デプロイの手順、適用可能なプログラム言語に関する情報が網羅的に提供されています。具体的には、次のような内容が含まれています：

- **DeepSeek-R1の概要**: モデルの設計理念や性能について説明し、Chain-of-Thought（CoT）推論を拡張した点が強調されています。
- **必要要件**: Azure AI Foundryで使用するために必要な前提条件が明示されており、サーバーレスAPIへのデプロイ方法や推論パッケージのインストール手順が含まれています。
- **チャット完了リクエストの作成**: Python、JavaScript、C#などのプログラミング言語を使用してモデルにアクセスするための具体的なコード例が示されています。
- **ストリーミングコンテンツ**: モデルのレスポンスをリアルタイムで取得するストリーミング方法についても説明がなされており、データサイズが大きい場合の処理に対しての配慮があります。
- **コンテンツ安全性**: Azure AIのコンテンツ安全性機能について、悪意のあるコンテンツを検出するための仕組みが述べられています。

この追加によって、ユーザーはDeepSeek-R1モデルを利用するための豊富な情報を得られ、実際のアプリケーション開発において役立つ具体的なガイダンスが提供されることになります。

## articles/ai-studio/how-to/deploy-models-gretel-navigator.md{#item-2e9806}

<details>
<summary>Diff</summary>
````diff
@@ -537,7 +537,7 @@ For more information on how to track costs, see [Monitor costs for models offere
 ## Related content
 
 
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Gretel Navigatorモデルデプロイに関するドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、Gretel Navigatorモデルをデプロイするためのドキュメント内にあるリンクを更新するものです。具体的には、1行が追加され、1行が削除される形での修正が行われました。

主な変更点は、「Azure AI Model Inference API」へのリンクの相対パスが修正されたことです。これにより、ユーザーがAzure AI Model Inference APIに関する正確で最新の情報にアクセスしやすくなります。

このアップデートは、ドキュメントのナビゲーションの正確性を向上させ、関連コンテンツへのアクセスを円滑にすることで、ユーザー体験を改善するために重要です。

## articles/ai-studio/how-to/deploy-models-jais.md{#item-0bd11f}

<details>
<summary>Diff</summary>
````diff
@@ -1186,7 +1186,7 @@ For more information on how to track costs, see [Monitor costs for models offere
 ## Related content
 
 
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JAISモデルデプロイに関するドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、JAISモデルをデプロイするためのドキュメント内のリンクを更新するものです。具体的には、1行が追加され、1行が削除される形での修正が行われました。

主な変更点は、「Azure AI Model Inference API」へのリンクの相対パスが変更されたことです。この修正により、ユーザーが最新の情報にアクセスできるようになり、ナビゲーションが強化されます。

この小さな更新は、文書の整合性を高め、ユーザーが関連コンテンツを円滑に探せるようにするために重要です。ユーザーの利便性を向上させるために、文書内のリンクが正確であることが求められます。

## articles/ai-studio/how-to/deploy-models-jamba.md{#item-eeefca}

<details>
<summary>Diff</summary>
````diff
@@ -136,12 +136,12 @@ For more information on using the APIs, see the [reference](#reference-for-jamba
 
 Jamba family models accept both of these APIs:
 
-- The [Azure AI Model Inference API](../reference/reference-model-inference-api.md) on the route `/chat/completions` for multi-turn chat or single-turn question-answering. This API is supported because Jamba family models are fine-tuned for chat completion.
-- [AI21's Azure Client](https://docs.ai21.com/reference/jamba-instruct-api). For more information about the REST endpoint being called, visit [AI21's REST documentation](https://docs.ai21.com/reference/jamba-instruct-api).
+- The [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md) on the route `/chat/completions` for multi-turn chat or single-turn question-answering. This API is supported because Jamba family models are fine-tuned for chat completion.
+- [AI21's Azure Client](https://docs.ai21.com/reference/jamba-15-api-ref). For more information about the REST endpoint being called, visit [AI21's REST documentation](https://docs.ai21.com/reference/jamba-15-api-ref).
 
 ### Azure AI model inference API
 
-The [Azure AI model inference API](../reference/reference-model-inference-api.md) schema can be found in the [reference for Chat Completions](../reference/reference-model-inference-chat-completions.md) article and an [OpenAPI specification can be obtained from the endpoint itself](../reference/reference-model-inference-api.md?tabs=rest#getting-started).
+The [Azure AI model inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md) schema can be found in the [reference for Chat Completions](../../ai-foundry/model-inference/reference/reference-model-inference-chat-completions.md) article and an [OpenAPI specification can be obtained from the endpoint itself](../../ai-foundry/model-inference/reference/reference-model-inference-api.md?tabs=rest#getting-started).
 
 Single-turn and multi-turn chat have the same request and response format, except that question answering (single-turn) involves only a single user message in the request, while multi-turn chat requires that you send the entire chat message history in each request. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Jambaモデルデプロイに関するドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、Jambaモデルをデプロイするためのドキュメントに関するリンクを更新するものです。具体的には、3行が追加され、3行が削除される形で6つの変更が行われました。

主な変更点は、「Azure AI Model Inference API」および「AI21のAzureクライアント」へのリンクの相対パスが修正されたことです。これにより、ユーザーが適切なリソースにアクセスしやすくなり、各APIの最新情報に簡単にアクセスできるようになっています。

特に、AI21のRESTドキュメントへのリンクが新しいURLに更新されており、APIの使用方法に関する情報がより明確になります。また、AIモデル推論APIに関するスキーマへのリンクも修正されており、関連する情報が一貫して整理されています。

このような小規模な更新は、文書の正確性を向上させ、ユーザーが必要な情報を迅速に取得できるようにするために重要です。

## articles/ai-studio/how-to/deploy-models-llama.md{#item-6274a7}

<details>
<summary>Diff</summary>
````diff
@@ -1491,7 +1491,7 @@ It is a good practice to start with a low number of instances and scale up as ne
 ## Related content
 
 
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Llamaモデルデプロイに関するドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、Llamaモデルをデプロイするためのドキュメント内にあるリンクを更新したものです。具体的には、1行が追加され、1行が削除される形での変更が行われました。

主な変更点は、「Azure AI Model Inference API」へのリンクの相対パスが修正されたことです。この修正によって、ユーザーは最新の情報にアクセスしやすくなり、分かりやすいナビゲーションが実現されています。

具体的には、リンクが「../reference/reference-model-inference-api.md」から「../../ai-foundry/model-inference/reference/reference-model-inference-api.md」へと変更されており、これにより、Azure AI Foundryの構成との整合性が向上しています。このような変更は、文書全体の正確性を向上させるとともに、ユーザーにとっての利便性を高める重要な役割を果たします。

## articles/ai-studio/how-to/deploy-models-mistral-codestral.md{#item-83ba03}

<details>
<summary>Diff</summary>
````diff
@@ -2060,7 +2060,7 @@ For more information on how to track costs, see [Monitor costs for models offere
 ## Related content
 
 
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralモデルデプロイに関するドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、Mistralモデルをデプロイするためのドキュメント内のリンクを更新したものです。具体的には、1行が追加され、1行が削除され、合計で2つの変更が行われました。

主な変更点は、「Azure AI Model Inference API」へのリンクの相対パスが修正されたことです。この修正により、ユーザーは最新かつ正確な情報にアクセスしやすくなります。具体的には、リンクが「../reference/reference-model-inference-api.md」から「../../ai-foundry/model-inference/reference/reference-model-inference-api.md」へと変更されており、Azure AI Foundryに関連する情報が整理されています。

このような小規模な更新は、ドキュメントの正確性向上と、ユーザーの利便性を高めるために重要であり、ユーザーが必要とする情報に迅速にアクセスできるようになります。

## articles/ai-studio/how-to/deploy-models-mistral-nemo.md{#item-e7b729}

<details>
<summary>Diff</summary>
````diff
@@ -2043,7 +2043,7 @@ For more information on how to track costs, see [Monitor costs for models offere
 ## Related content
 
 
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistral Nemoモデルデプロイに関するドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、Mistral Nemoモデルをデプロイするためのドキュメント内でのリンクの更新に関するものです。具体的には、1行が追加され、1行が削除され、合計で2つの変更が行われています。

主な変更点は、「Azure AI Model Inference API」へのリンクの相対パスが変更されたことです。これにより、ドキュメントが最新の情報を参照していることが保証されます。リンクは「../reference/reference-model-inference-api.md」から「../../ai-foundry/model-inference/reference/reference-model-inference-api.md」へと改訂され、Azure AI Foundryに関連する情報がより正確に提供されています。

このような更新は、ドキュメントの正確性と整合性を向上させ、ユーザーが必要とする情報へ迅速にアクセスできるようにするために重要です。これにより、ユーザーエクスペリエンスが改善されることが期待されます。

## articles/ai-studio/how-to/deploy-models-mistral-open.md{#item-84e005}

<details>
<summary>Diff</summary>
````diff
@@ -1308,7 +1308,7 @@ It's a good practice to start with a low number of instances and scale up as nee
 ## Related content
 
 
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistral Openモデルデプロイに関するドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、Mistral Openモデルをデプロイするためのドキュメント内でのリンクの更新を含んでいます。具体的には、1行が追加され、1行が削除され、合計で2つの変更が行われました。

主な変更点は、「Azure AI Model Inference API」へのリンクの相対パスが修正されたことです。このリンクは「../reference/reference-model-inference-api.md」から「../../ai-foundry/model-inference/reference/reference-model-inference-api.md」へと改訂され、より正確な情報へ導くものとなっています。これにより、ユーザーは最新の情報にアクセスしやすくなります。

このような小規模な更新は、ドキュメントの一貫性と正確性を高め、ユーザーが必要とする情報へ迅速にアクセスできるようにするために重要です。これにより、ユーザーエクスペリエンスの向上が期待されます。

## articles/ai-studio/how-to/deploy-models-mistral.md{#item-487a41}

<details>
<summary>Diff</summary>
````diff
@@ -2242,7 +2242,7 @@ For more information on how to track costs, see [Monitor costs for models offere
 ## Related content
 
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
 * [Model deprecation and retirement in Azure AI model catalog](../concepts/model-lifecycle-and-retirement.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralモデルデプロイに関するドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、Mistralモデルをデプロイするためのドキュメント内でのリンクの更新に関するものです。1行が追加され、1行が削除され、合計で2つの変更が行われました。

主要な変更点は、「Azure AI Model Inference API」へのリンクの相対パスが修正されたことです。このリンクは「../reference/reference-model-inference-api.md」から「../../ai-foundry/model-inference/reference/reference-model-inference-api.md」へと変更され、より正確な情報源にアクセスできるようになっています。この更新により、ユーザーは最新の参照資料にスムーズにアクセスできるようになります。

こうしたマイナーな更新は、ドキュメントの正確性と一貫性を確保する上で重要であり、ユーザーが必要とする情報へのアクセスを向上させることが期待されます。これにより、全体的なユーザーエクスペリエンスの向上につながるでしょう。

## articles/ai-studio/how-to/deploy-models-phi-3-5-vision.md{#item-8d6d7d}

<details>
<summary>Diff</summary>
````diff
@@ -1633,7 +1633,7 @@ It's a good practice to start with a low number of instances and scale up as nee
 ## Related content
 
 
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi 3.5ビジョンモデルデプロイに関するドキュメントのリンク更新"
}
```

### Explanation
このコードの変更は、Phi 3.5ビジョンモデルをデプロイするためのドキュメント内でのリンクの更新を含んでいます。1行が追加され、1行が削除されており、合計で2つの変更が行われました。

主な変更点は、「Azure AI Model Inference API」へのリンクの相対パスが変更されたことです。もともとのリンクは「../reference/reference-model-inference-api.md」であり、新しいリンクは「../../ai-foundry/model-inference/reference/reference-model-inference-api.md」に修正されています。この変更により、ユーザーはより正確で関連性の高い資料へ容易にアクセスできるようになります。

このようなマイナーな更新は、ドキュメントの整合性と正確性を保つために重要であり、ユーザーが必要とする情報への迅速なアクセスを促進することが期待されます。全体として、ユーザーの利便性を向上させる効果があります。

## articles/ai-studio/how-to/deploy-models-phi-3-vision.md{#item-bd5aae}

<details>
<summary>Diff</summary>
````diff
@@ -1420,7 +1420,7 @@ It's a good practice to start with a low number of instances and scale up as nee
 ## Related content
 
 
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi 3モデルデプロイに関するドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、Phi 3モデルをデプロイするためのドキュメントにおけるリンクの更新を示しています。1行の追加と1行の削除があり、合計で2つの変更が行われました。

具体的な変更内容としては、「Azure AI Model Inference API」へのリンクの相対パスが修正されました。以前のリンク「../reference/reference-model-inference-api.md」が、新しいリンク「../../ai-foundry/model-inference/reference/reference-model-inference-api.md」に変更されました。この修正により、関連する情報源へより適切にアクセスできるようになります。

このマイナーな更新は、ドキュメントの正確性と信頼性を向上させ、ユーザーが必要とする情報を容易に見つけられるようにするために重要です。全体として、ドキュメントの品質を向上させる効果が期待されます。

## articles/ai-studio/how-to/deploy-models-phi-3.md{#item-47e305}

<details>
<summary>Diff</summary>
````diff
@@ -1481,7 +1481,7 @@ You can use this [sample notebook](https://github.com/Azure/azureml-examples/blo
 ## Related content
 
 
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi 3モデルデプロイに関するドキュメントのリンク変更"
}
```

### Explanation
このコードの変更は、Phi 3モデルデプロイに関連するドキュメント内のリンクの修正を含んでいます。具体的には、1行の追加と1行の削除があり、合計で2つの変更が行われました。

変更点として、「Azure AI Model Inference API」へのリンクの相対パスが変更されています。以前のリンク「../reference/reference-model-inference-api.md」が、新しいリンク「../../ai-foundry/model-inference/reference/reference-model-inference-api.md」に更新されました。このリンクの変更により、ユーザーは関連する参照資料により正しくアクセスできるようになることが意図されています。

このようなマイナーな更新は、ドキュメントの明確性と正確性を強化し、ユーザーが必要とする情報を迅速に見つけられるようにするために重要です。全体として、ユーザーエクスペリエンスの向上が期待されます。

## articles/ai-studio/how-to/deploy-models-phi-4.md{#item-c40212}

<details>
<summary>Diff</summary>
````diff
@@ -1357,7 +1357,7 @@ It's a good practice to start with a low number of instances and scale up as nee
 ## Related content
 
 
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi 4モデルデプロイに関するドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、Phi 4モデルをデプロイするためのドキュメントにおけるリンクの更新を反映しています。具体的には、1行の追加と1行の削除があり、合計で2つの変更が行われました。

変更された内容は、「Azure AI Model Inference API」へのリンクの相対パスが変更された点です。以前のリンク「../reference/reference-model-inference-api.md」から新しいリンク「../../ai-foundry/model-inference/reference/reference-model-inference-api.md」に更新されました。この修正により、ユーザーは関連する API への正確なアクセスが可能になります。

このマイナーな更新は、ドキュメント全体の整合性と正確性を保つために重要であり、ユーザーが必要な情報を簡単に見つけられるようにすることに寄与します。結果として、より良いユーザー体験が提供されることが期待されます。

## articles/ai-studio/how-to/deploy-models-serverless.md{#item-f8177f}

<details>
<summary>Diff</summary>
````diff
@@ -553,9 +553,9 @@ In this section, you create an endpoint with the name **meta-llama3-8b-qwerty**.
 
 ## Use the serverless API endpoint
 
-Models deployed in Azure Machine Learning and Azure AI Foundry in Serverless API endpoints support the [Azure AI Model Inference API](../reference/reference-model-inference-api.md) that exposes a common set of capabilities for foundational models and that can be used by developers to consume predictions from a diverse set of models in a uniform and consistent way. 
+Models deployed in Azure Machine Learning and Azure AI Foundry in Serverless API endpoints support the [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md) that exposes a common set of capabilities for foundational models and that can be used by developers to consume predictions from a diverse set of models in a uniform and consistent way. 
 
-Read more about the [capabilities of this API](../reference/reference-model-inference-api.md#capabilities) and how [you can use it when building applications](../reference/reference-model-inference-api.md#getting-started). 
+Read more about the [capabilities of this API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md#capabilities) and how [you can use it when building applications](../../ai-foundry/model-inference/reference/reference-model-inference-api.md#getting-started). 
 
 ## Network isolation
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスAPIモデルデプロイに関するドキュメントのリンク更新"
}
```

### Explanation
このコードの変更は、サーバーレスAPIにデプロイされたモデルに関するドキュメントのリンクの更新を含んでいます。具体的には、2つの追加と2つの削除があり、合計で4つの変更が行われました。

変更されたリンク部分では、元々の「Azure AI Model Inference API」へのリンクが、相対パスが更新されることにより、「../reference/reference-model-inference-api.md」から「../../ai-foundry/model-inference/reference/reference-model-inference-api.md」に変更されています。また、APIの能力に関する情報や、アプリケーションの構築時の使用方法に関するリンクも同様に更新されています。

これによって、ユーザーはより正確に関連資料へアクセスできるようになり、APIの利用や理解がスムーズになることが期待されます。このマイナーな更新は、ドキュメントの整合性を高め、ユーザーエクスペリエンスを向上させることに貢献します。

## articles/ai-studio/how-to/deploy-models-tsuzumi.md{#item-d3fd51}

<details>
<summary>Diff</summary>
````diff
@@ -1335,7 +1335,7 @@ For more information on how to track costs, see [Monitor costs for models offere
 ## Related content
 
 
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Azure AI Model Inference API](../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Tsuzumiモデルデプロイに関するドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、Tsuzumiモデルをデプロイするためのドキュメント内のリンクの更新を示しています。具体的には、1行の追加と1行の削除があり、合計で2つの変更が行われました。

変更内容としては、「Azure AI Model Inference API」へのリンクが、新しい相対パス「../reference/reference-model-inference-api.md」から「../../ai-foundry/model-inference/reference/reference-model-inference-api.md」に修正されています。この修正により、ユーザーは最新の正確な情報にアクセスできるようになります。

このマイナーな更新は、ドキュメントの整合性を向上させ、情報の正確性を保つために重要です。結果的に、ユーザーは必要なリソースに円滑にアクセスでき、学習や開発作業がより効率的に行えることが期待されます。

## articles/ai-studio/how-to/develop/langchain.md{#item-0d59f1}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,7 @@ LangChain is a development ecosystem that makes as easy possible for developers
 
 Models deployed to Azure AI Foundry can be used with LangChain in two ways:
 
-- **Using the Azure AI model inference API:** All models deployed to Azure AI Foundry support the [Azure AI model inference API](../../reference/reference-model-inference-api.md), which offers a common set of functionalities that can be used for most of the models in the catalog. The benefit of this API is that, since it's the same for all the models, changing from one to another is as simple as changing the model deployment being use. No further changes are required in the code. When working with LangChain, install the extensions `langchain-azure-ai`.
+- **Using the Azure AI model inference API:** All models deployed to Azure AI Foundry support the [Azure AI model inference API](../../../ai-foundry/model-inference/reference/reference-model-inference-api.md), which offers a common set of functionalities that can be used for most of the models in the catalog. The benefit of this API is that, since it's the same for all the models, changing from one to another is as simple as changing the model deployment being use. No further changes are required in the code. When working with LangChain, install the extensions `langchain-azure-ai`.
 
 - **Using the model's provider specific API:** Some models, like OpenAI, Cohere, or Mistral, offer their own set of APIs and extensions for LlamaIndex. Those extensions may include specific functionalities that the model support and hence are suitable if you want to exploit them. When working with LangChain, install the extension specific for the model you want to use, like `langchain-openai` or `langchain-cohere`.
 
@@ -467,4 +467,4 @@ Learn more about [how to visualize and manage traces](visualize-traces.md).
 * [Develop applications with LlamaIndex](llama-index.md)
 * [Visualize and manage traces in Azure AI Foundry](visualize-traces.md)
 * [Use the Azure AI model inference service](../../ai-services/model-inference.md)
-* [Reference: Azure AI model inference API](../../reference/reference-model-inference-api.md)
+* [Reference: Azure AI model inference API](../../../ai-foundry/model-inference/reference/reference-model-inference-api.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "LangChainに関するドキュメントのリンク更新"
}
```

### Explanation
このコードの変更は、LangChainを使用するための開発環境に関するドキュメント内のリンクの更新を示しています。具体的には、2行の追加と2行の削除があり、合計で4つの変更が行われました。

主な変更点は、「Azure AI model inference API」へのリンクが、新しい相対パス「../../reference/reference-model-inference-api.md」から「../../../ai-foundry/model-inference/reference/reference-model-inference-api.md」に更新されたことです。このリンクの修正により、ユーザーは正しいAPIリファレンスにアクセスできるようになり、最新情報を得やすくなります。

このマイナーな更新により、ドキュメントの情報の整合性が強化され、LangChainを使用する開発者にとって有益なものとなります。正確なリンクを使用することで、ユーザーはモデルやAPIに関する情報を効果的に活用できるようになり、開発作業の効率化が期待されます。

## articles/ai-studio/how-to/develop/llama-index.md{#item-613372}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,7 @@ In this article, you learn how to use [LlamaIndex](https://github.com/run-llama/
 
 Models deployed to Azure AI Foundry can be used with LlamaIndex in two ways:
 
-- **Using the Azure AI model inference API:** All models deployed to Azure AI Foundry support the [Azure AI model inference API](../../reference/reference-model-inference-api.md), which offers a common set of functionalities that can be used for most of the models in the catalog. The benefit of this API is that, since it's the same for all the models, changing from one to another is as simple as changing the model deployment being use. No further changes are required in the code. When working with LlamaIndex, install the extensions `llama-index-llms-azure-inference` and `llama-index-embeddings-azure-inference`.
+- **Using the Azure AI model inference API:** All models deployed to Azure AI Foundry support the [Azure AI model inference API](../../../ai-foundry/model-inference/reference/reference-model-inference-api.md), which offers a common set of functionalities that can be used for most of the models in the catalog. The benefit of this API is that, since it's the same for all the models, changing from one to another is as simple as changing the model deployment being use. No further changes are required in the code. When working with LlamaIndex, install the extensions `llama-index-llms-azure-inference` and `llama-index-embeddings-azure-inference`.
 
 - **Using the model's provider specific API:** Some models, like OpenAI, Cohere, or Mistral, offer their own set of APIs and extensions for LlamaIndex. Those extensions may include specific functionalities that the model support and hence are suitable if you want to exploit them. When working with `llama-index`, install the extension specific for the model you want to use, like `llama-index-llms-openai` or `llama-index-llms-cohere`.
 
@@ -175,7 +175,7 @@ llm = AzureAICompletionsModel(
 )
 ```
 
-Parameters not supported in the Azure AI model inference API ([reference](../../reference/reference-model-inference-chat-completions.md)) but available in the underlying model, you can use the `model_extras` argument. In the following example, the parameter `safe_prompt`, only available for Mistral models, is being passed.
+Parameters not supported in the Azure AI model inference API ([reference](../../../ai-foundry/model-inference/reference/reference-model-inference-chat-completions.md)) but available in the underlying model, you can use the `model_extras` argument. In the following example, the parameter `safe_prompt`, only available for Mistral models, is being passed.
 
 ```python
 llm = AzureAICompletionsModel(
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "LlamaIndexドキュメント内のリンク修正"
}
```

### Explanation
このコードの変更は、LlamaIndexを使用するためのドキュメント内でのリンクの更新を示しています。具体的には、2行の追加と2行の削除があり、合計で4つの変更が行われました。

主な変更として、「Azure AI model inference API」へのリンクが、「../../reference/reference-model-inference-api.md」から「../../../ai-foundry/model-inference/reference/reference-model-inference-api.md」に更新されました。この修正により、ユーザーは正確なAPIリファレンスにアクセスできるようになり、最新の情報を取得しやすくなります。

また、`model_extras`引数に関する説明の部分でもリンクが修正されており、同様に正しいリファレンス情報にアクセスできるようになっています。

このマイナーな更新により、LlamaIndexを利用する開発者に対して、より正確で整合性のある情報が提供されることになります。結果として、ユーザーは必要なリソースを迅速に見つけることができ、開発作業の効率性が向上することが期待されます。

## articles/ai-studio/how-to/develop/semantic-kernel.md{#item-565785}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,7 @@ In this article, you learn how to use [Semantic Kernel](/semantic-kernel/overvie
 
 - An [Azure subscription](https://azure.microsoft.com).
 - An Azure AI project as explained at [Create a project in Azure AI Foundry portal](../create-projects.md).
-- A model supporting the [Azure AI model inference API](../../reference/reference-model-inference-api.md?tabs=python) deployed. In this example, we use a `Mistral-Large` deployment, but use any model of your preference. For using embeddings capabilities in LlamaIndex, you need an embedding model like `cohere-embed-v3-multilingual`.
+- A model supporting the [Azure AI model inference API](../../../ai-foundry/model-inference/reference/reference-model-inference-api.md?tabs=python) deployed. In this example, we use a `Mistral-Large` deployment, but use any model of your preference. For using embeddings capabilities in LlamaIndex, you need an embedding model like `cohere-embed-v3-multilingual`.
 
   - You can follow the instructions at [Deploy models as serverless APIs](../deploy-models-serverless.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Semantic Kernelドキュメント内のリンク修正"
}
```

### Explanation
このコードの変更は、Semantic Kernelに関するドキュメント内でのリンクの修正を示しています。具体的には、1行の追加と1行の削除があり、合計で2つの変更が行われました。

主な変更点は、「Azure AI model inference API」へのリンクが、新しい相対パス「../../reference/reference-model-inference-api.md?tabs=python」から「../../../ai-foundry/model-inference/reference/reference-model-inference-api.md?tabs=python」に更新されたことです。この変更により、ユーザーは正確なAPIリファレンスにアクセスしやすくなり、必要な情報を迅速に取得できるようになります。

このマイナーな更新によって、Semantic Kernelの利用者に対して、最新かつ一貫した情報を提供することが可能となります。結果として、開発者は情報を効果的に活用でき、よりスムーズにプロジェクトを進めることができるでしょう。

## articles/ai-studio/how-to/develop/trace-local-sdk.md{#item-f7dfb5}

<details>
<summary>Diff</summary>
````diff
@@ -72,7 +72,7 @@ To learn more Azure AI Inference SDK for C# and observability, see the [Tracing
 
 ---
 
-To learn more , see the [Inference SDK reference](../../reference/reference-model-inference-api.md).
+To learn more , see the [Inference SDK reference](../../../ai-foundry/model-inference/reference/reference-model-inference-api.md).
 
 ### Configuration
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Trace Local SDKドキュメント内のリンク修正"
}
```

### Explanation
このコードの変更は、Trace Local SDKに関するドキュメント内でのリンクの修正を示しています。具体的には、1行の追加と1行の削除があり、合計で2つの変更が行われました。

主な変更点は、「Inference SDK reference」へのリンクが、以前の相対パス「../../reference/reference-model-inference-api.md」から新しい相対パス「../../../ai-foundry/model-inference/reference/reference-model-inference-api.md」に更新されたことです。この修正により、ユーザーはより正確なAPIリファレンスにアクセスでき、文書の整合性が向上しています。

このマイナーな更新は、Trace Local SDKの利用者に対して、最新の情報とリソースに簡単にアクセスできるようにし、開発のスムーズさと効率性を向上させることを目的としています。

## articles/ai-studio/how-to/prompt-flow-tools/azure-open-ai-gpt-4v-tool.md{#item-053d0d}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-studio
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 01/29/2025
 ms.reviewer: keli19
 ms.author: lagayhar
 author: lgayhardt
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Open AI GPT-4Vツールドキュメントの日付更新"
}
```

### Explanation
このコードの変更は、Azure Open AI GPT-4Vツールに関するドキュメントの日付更新を示しています。具体的には、1行の追加と1行の削除があり、合計で2つの変更が行われました。

主な変更点は、ドキュメントのメタデータにある日付が「5/21/2024」から「01/29/2025」に更新されたことです。この変更は、ドキュメントの内容が将来の日付に合わせて更新されたことを反映しています。

このマイナーな更新によって、利用者は新しい情報や指針が新しい日付に基づいていることを確認でき、Azure Open AI GPT-4Vツールに関する最新のリソースと情報を活用することができるようになります。信頼性の高い情報を提供することが目的です。

## articles/ai-studio/how-to/prompt-flow-tools/content-safety-tool.md{#item-09b048}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 01/29/2025
 ms.reviewer: keli19
 ms.author: lagayhar
 author: lgayhardt
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツ安全ツールドキュメントの日付更新"
}
```

### Explanation
このコードの変更は、コンテンツ安全ツールに関するドキュメントの日付を更新する内容です。具体的には、1行の追加と1行の削除が行われ、合計で2つの変更がありました。

主な変更点は、文書のメタデータにおける日付が「5/21/2024」から「01/29/2025」に変更されたことです。この更新は、ドキュメントが将来の情報に合わせて整備されたことを示しています。

このマイナーな更新によって、利用者はコンテンツ安全ツールに関連する最新のリソースを正確な日付情報に基づいて利用できるようになります。信頼性の高いガイダンスを維持することが目的です。

## articles/ai-studio/how-to/prompt-flow-tools/embedding-tool.md{#item-81420c}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 01/29/2025
 ms.reviewer: keli19
 ms.author: lagayhar
 author: lgayhardt
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "埋め込みツールドキュメントの日付更新"
}
```

### Explanation
このコードの変更は、埋め込みツールに関するドキュメントの日付を更新するものです。具体的には、1行の追加と1行の削除を含む合計2つの変更が行われました。

主な変更点は、文書内のメタデータにおける日付が「5/21/2024」から「01/29/2025」に変更されたことです。この更新は、ドキュメントが将来の情報にアップデートされたことを反映しています。

このマイナーな更新によって、利用者は埋め込みツールに関する最新のリソースを、新しい日付に基づいて正確に利用できるようになります。これにより、文書の信頼性と適時性が向上します。

## articles/ai-studio/how-to/prompt-flow-tools/index-lookup-tool.md{#item-cad66d}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-studio
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 01/29/2025
 ms.reviewer: estraight
 ms.author: lagayhar
 author: lgayhardt
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスルックアップツールドキュメントの日付更新"
}
```

### Explanation
このコードの変更は、インデックスルックアップツールに関するドキュメントの日付を更新するものです。具体的には、1行の追加と1行の削除を含む合計2つの変更が行われました。

主な変更点は、文書のメタデータに含まれる日付が「5/21/2024」から「01/29/2025」に変更されたことです。この更新は、ドキュメントの内容が最新の情報に基づいていることを示しています。

このマイナーな更新により、利用者はインデックスルックアップツールに関連する最新の情報を正確な日付とともに利用できるようになり、文書の信頼性が向上します。

## articles/ai-studio/how-to/prompt-flow-tools/llm-tool.md{#item-6691f4}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 1/29/2025
 ms.reviewer: keli19
 ms.author: lagayhar
 author: lgayhardt
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "LLMツールドキュメントの日付更新"
}
```

### Explanation
このコードの変更は、LLMツールに関するドキュメントの日付を更新することに関するものです。具体的には、1行の追加と1行の削除を含む合計2つの変更が行われました。

主な変更点は、文書内のメタデータの日付が「5/21/2024」から「1/29/2025」に変更されたことです。この更新は、ドキュメントが最新の情報に基づいていることを反映しています。

このマイナーな更新により、LLMツールに関する情報が最新の日付に合わせてアップデートされ、利用者による信頼性の高い参照が可能になります。文書は、今後の使用に対して適時で有用なリソースとなります。

## articles/ai-studio/how-to/prompt-flow-tools/prompt-flow-tools-overview.md{#item-fd7471}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-studio
 ms.custom:
   - build-2024
 ms.topic: overview
-ms.date: 5/21/2024
+ms.date: 01/29/2025
 ms.reviewer: keli19
 ms.author: lagayhar
 author: lgayhardt
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトフローツールの概要ドキュメントの日付更新"
}
```

### Explanation
このコードの変更は、プロンプトフローツールの概要に関するドキュメントの日付を更新するものです。具体的には、1行の追加と1行の削除を含む合計2つの変更が行われました。

主な変更点は、文書内のメタデータに記載されている日付が「5/21/2024」から「01/29/2025」に変更されたことです。これにより、ドキュメントの更新日が最新の情報を反映するようになっています。

このマイナーな更新により、プロンプトフローツールに関する情報が現行の状況に即したものであることが示され、利用者がこのドキュメントを参照する際に信頼性を高める効果があります。文書は、利用者にとってより有用なリソースとなります。

## articles/ai-studio/how-to/prompt-flow-tools/prompt-tool.md{#item-c6a9a0}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 01/29/2025
 ms.reviewer: keli19
 ms.author: lagayhar
 author: lgayhardt
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトツールドキュメントの日付更新"
}
```

### Explanation
このコードの変更は、プロンプトツールに関するドキュメントの日付を更新するものです。具体的には、1行の追加と1行の削除があり、合計2つの変更が行われました。

主な変更点は、文書内のメタデータの日付が「5/21/2024」から「01/29/2025」に変更されたことです。この更新により、ドキュメントがより新しい情報を反映することになります。

このマイナーな更新は、プロンプトツールに関する情報が最新のものであることを保証し、利用者がこの文書を参考にする際に信頼性を提供します。結果として、文書は利用者にとってより役立つリソースとなるでしょう。

## articles/ai-studio/how-to/prompt-flow-tools/python-tool.md{#item-c9200f}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: scottpolly
 ms.service: azure-ai-studio
 ms.custom: ignite-2023, devx-track-python, build-2024, ignite-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 01/29/2025
 ms.reviewer: keli19
 ms.author: lagayhar
 author: lgayhardt
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonツールドキュメントの日付更新"
}
```

### Explanation
このコードの変更は、Pythonツールに関連するドキュメントの日付を更新するものです。具体的には、1行の追加と1行の削除が行われ、合計2つの変更が反映されています。

主な変更点は、文書内のメタデータの日付が「5/21/2024」から「01/29/2025」に変更されたことです。この更新により、ドキュメントが最新の情報を反映することになります。

このマイナーな更新は、Pythonツールに関する情報が現行の状況を反映していることを保証し、利用者がこの文書を参照する際に信頼性と正確性を提供します。結果として、この情報は利用者にとってより価値のあるリソースとなるでしょう。

## articles/ai-studio/how-to/prompt-flow-tools/rerank-tool.md{#item-dd52bf}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: This article introduces you to the Rerank tool for flows in Azure A
 manager: scottpolly
 ms.service: azure-ai-studio
 ms.topic: how-to
-ms.date: 08/29/2024
+ms.date: 01/29/2025
 ms.reviewer: jingyizhu
 ms.author: lagayhar
 author: lgayhardt
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リランクツールドキュメントの日付更新"
}
```

### Explanation
このコードの変更は、リランクツールに関するドキュメントの日付を更新することを目的としています。具体的には、1行の追加と1行の削除があり、合計2つの変更が反映されています。

主要な変更は、文書内のメタデータの日付が「08/29/2024」から「01/29/2025」に変更された点です。この更新により、ドキュメントはより新しい情報が反映されることになります。

このマイナーな更新は、リランクツールに関する情報が最新のものであり、利用者がこの文書を参照する際に信頼性を確保します。その結果、利用者にとってこの情報はより有用で価値のあるリソースとなるでしょう。

## articles/ai-studio/media/prompt-flow/azure-openai-gpt-4-vision-tool.png{#item-94def5}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4ビジョンツールの画像メタデータの更新"
}
```

### Explanation
このコードの変更は、GPT-4ビジョンツールに関連する画像ファイルのメタデータに適用されます。具体的には、実際の追加や削除はありませんが、ファイルに対して何らかの変更が行われています。

この変更には、ファイルそのものの内容には影響を与えないものの、該当画像が文書にとって重要な意味を持つ場合があります。文書内の画像は、視覚的に情報を提供する役割を果たしており、その品質や関連性が最新のものか確認されることは重要です。

全体として、この変更はドキュメントのトータルな品質を向上させることを目的としたものであり、ユーザーにとっての情報の価値を保持するためのものです。

## articles/ai-studio/media/prompt-flow/content-safety-tool.png{#item-c673ee}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツセーフティツールの画像メタデータの更新"
}
```

### Explanation
このコードの変更は、コンテンツセーフティツールに関連する画像ファイルに関するものです。具体的には、実際には追加や削除は行われておらず、ファイルに変更が加えられたことを示していますが、内容自体には影響を与えない状態です。

この変更は、画像ファイルのメタデータやその他の情報に関するものである可能性があります。画像は、ドキュメントの視覚的な理解を助ける重要な要素であり、特に技術文書においては、その関連性や質が重要です。

最終的には、ユーザーがコンテンツをより良く理解できるよう、ドキュメントの整合性と品質を保つための微細な調整が行われたことを意味しています。

## articles/ai-studio/media/prompt-flow/prompt-tool.png{#item-245957}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトツールの画像メタデータの更新"
}
```

### Explanation
このコードの変更は、プロンプトツールに関連する画像ファイルに対して行われています。ここでは、実際に内容の追加や削除はなく、ただファイルに対して変更が加えられたことを示しています。

具体的には、ここでの変更は画像ファイルのメタデータやその他の属性に影響を与える可能性がありますが、画像自体の内容には変化がないため、ユーザーの視覚的体験には直接的な影響はありません。このようなマイナーな更新は、ドキュメントの一貫性と品質を維持するために重要です。

全体として、この変更はドキュメントの信頼性を高めることを目的としており、ユーザーが情報を正確に理解できるようサポートするものです。

## articles/ai-studio/media/prompt-flow/python-tool.png{#item-14e9b3}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonツールの画像メタデータの更新"
}
```

### Explanation
このコードの変更は、Pythonツールに関連する画像ファイルに関するものです。現時点では、実際の画像の内容や構造についての追加や削除は行われておらず、変更はありませんが、ファイル自体に関連する設定やメタデータが変更された可能性があります。

このようなマイナーな更新は、ドキュメントの整合性を保つために重要であり、特に技術的な情報を提供する際には、正確さと明確さが求められます。ユーザーにとって、適切な視覚表現を維持することで、情報をより正確に把握する手助けとなります。

最終的に、この変更はドキュメントの品質向上を図るものであり、ユーザーが必要な情報を正しく理解できるようサポートします。

## articles/ai-studio/reference/reference-model-inference-completions.md{#item-bae39d}

<details>
<summary>Diff</summary>
````diff
@@ -1,296 +0,0 @@
----
-title: Azure AI Model Inference Completions
-titleSuffix: Azure AI Foundry
-description: Reference for Azure AI Model Inference Completions API
-manager: scottpolly
-ms.service: azure-ai-studio
-ms.topic: conceptual
-ms.date: 5/21/2024
-ms.reviewer: fasantia 
-reviewer: santiagxf
-ms.author: mopeakande
-author: msakande
-ms.custom: 
- - build-2024
----
-
-# Reference: Completions | Azure AI Foundry
-
-[!INCLUDE [feature-preview](../includes/feature-preview.md)]
-
-Creates a completion for the provided prompt and parameters.
-
-```http
-POST /completions?api-version=2024-04-01-preview
-```
-
-| Name | In  | Required | Type | Description |
-| --- | --- | --- | --- | --- |
-| api-version | query | True | string | The version of the API in the format "YYYY-MM-DD" or "YYYY-MM-DD-preview". |
-
-## Request Header
-
-
-| Name | Required | Type | Description |
-| --- | --- | --- | --- |
-| extra-parameters | | string | The behavior of the API when extra parameters are indicated in the payload. Using `pass-through` makes the API to pass the parameter to the underlying model. Use this value when you want to pass parameters that you know the underlying model can support. Using `drop` makes the API to drop any unsupported parameter. Use this value when you need to use the same payload across different models, but one of the extra parameters may make a model to error out if not supported. Using `error` makes the API to reject any extra parameter in the payload. Only parameters specified in this API can be indicated, or a 400 error is returned. |
-| azureml-model-deployment |     | string | Name of the deployment you want to route the request to. Supported for endpoints that support multiple deployments. |
-
-
-## Request Body
-
-
-| Name | Required | Type | Description |
-| --- | --- | --- | --- |
-| prompt | True |     | The prompts to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays. Note that `<\|endoftext\|>` is the document separator that the model sees during training, so if a prompt is not specified the model generates as if from the beginning of a new document. |
-| frequency\_penalty |     | number | Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. |
-| max\_tokens |     | integer | The maximum number of tokens that can be generated in the completion. The token count of your prompt plus `max_tokens` cannot exceed the model's context length. |
-| presence\_penalty |     | number | Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. |
-| seed |     | integer | If specified, the model makes a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.<br><br>Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend. |
-| stop |     |     | Sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence. |
-| stream |     | boolean | Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. |
-| temperature |     | number | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.<br><br>We generally recommend altering `temperature` or `top_p` but not both. |
-| top\_p |     | number | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br><br>We generally recommend altering `top_p` or `temperature` but not both. |
-
-## Responses
-
-
-| Name | Type | Description |
-| --- | --- | --- |
-| 200 OK | [CreateCompletionResponse](#createcompletionresponse) | OK  |
-| 401 Unauthorized         | [UnauthorizedError](#unauthorizederror)                 | Access token is missing or invalid<br><br>Headers<br><br>x-ms-error-code: string                                                                           |
-| 404 Not Found            | [NotFoundError](#notfounderror)                         | Modality not supported by the model. Check the documentation of the model to see which routes are available.<br><br>Headers<br><br>x-ms-error-code: string |
-| 422 Unprocessable Entity | [UnprocessableContentError](#unprocessablecontenterror) | The request contains unprocessable content<br><br>Headers<br><br>x-ms-error-code: string                                                                   |
-| 429 Too Many Requests    | [TooManyRequestsError](#toomanyrequestserror)           | You have hit your assigned rate limit and your request need to be paced.<br><br>Headers<br><br>x-ms-error-code: string                                     |
-| Other Status Codes       | [ContentFilterError](#contentfiltererror)               | Bad request<br><br>Headers<br><br>x-ms-error-code: string                                                                                                  |
-
-
-## Security
-
-
-### Authorization
-
-The token with the `Bearer:` prefix, e.g. `Bearer abcde12345`
-
-**Type**: apiKey  
-**In**: header  
-
-
-### AADToken
-
-Azure Active Directory OAuth2 authentication
-
-**Type**: oauth2  
-**Flow**: application  
-**Token URL**: https://login.microsoftonline.com/common/oauth2/v2.0/token  
-
-
-## Examples
-
-
-### Creates a completion for the provided prompt and parameters
-
-#### Sample Request
-
-```http
-POST /completions?api-version=2024-04-01-preview
-
-{
-  "prompt": "This is a very good text",
-  "frequency_penalty": 0,
-  "presence_penalty": 0,
-  "max_tokens": 256,
-  "seed": 42,
-  "stop": "<|endoftext|>",
-  "stream": false,
-  "temperature": 0,
-  "top_p": 1
-}
-
-```
-
-#### Sample Response
-
-Status code: 200
-
-```json
-{
-  "id": "1234567890",
-  "model": "llama2-7b",
-  "choices": [
-    {
-      "index": 0,
-      "finish_reason": "stop",
-      "text": ", indeed it is a good one."
-    }
-  ],
-  "created": 1234567890,
-  "object": "text_completion",
-  "usage": {
-    "prompt_tokens": 15,
-    "completion_tokens": 8,
-    "total_tokens": 23
-  }
-}
-```
-
-## Definitions
-
-
-| Name | Description |
-| --- | --- |
-| [Choices](#choices) | A list of chat completion choices. |
-| [CompletionFinishReason](#completionfinishreason) | The reason the model stopped generating tokens. This is `stop` if the model hit a natural stop point or a provided stop sequence, `length` if the maximum number of tokens specified in the request was reached, `content_filter` if content was omitted due to a flag from our content filters. |
-| [CompletionUsage](#completionusage) | Usage statistics for the completion request. |
-| [ContentFilterError](#contentfiltererror) | The API call fails when the prompt triggers a content filter as configured. Modify the prompt and try again. |
-| [CreateCompletionRequest](#createcompletionrequest) |     |
-| [CreateCompletionResponse](#createcompletionresponse) | Represents a completion response from the API. |
-| [Detail](#detail) |     |
-| [TextCompletionObject](#textcompletionobject) | The object type, which is always "text\_completion" |
-| [UnprocessableContentError](#unprocessablecontenterror) |     |
-
-
-### Choices
-
-A list of chat completion choices.
-
-
-| Name | Type | Description |
-| --- | --- | --- |
-| finish\_reason | [CompletionFinishReason](#completionfinishreason) | The reason the model stopped generating tokens. This is `stop` if the model hit a natural stop point or a provided stop sequence, `length` if the maximum number of tokens specified in the request was reached, `content_filter` if content was omitted due to a flag from our content filters, `tool_calls` if the model called a tool. |
-| index | integer | The index of the choice in the list of choices. |
-| text | string | The generated text. |
-
-
-### CompletionFinishReason
-
-The reason the model stopped generating tokens. This is `stop` if the model hit a natural stop point or a provided stop sequence, `length` if the maximum number of tokens specified in the request was reached, `content_filter` if content was omitted due to a flag from our content filters.
-
-
-| Name | Type | Description |
-| --- | --- | --- |
-| content\_filter | string |     |
-| length | string |     |
-| stop | string |     |
-
-### CompletionUsage
-
-Usage statistics for the completion request.
-
-
-| Name | Type | Description |
-| --- | --- | --- |
-| completion\_tokens | integer | Number of tokens in the generated completion. |
-| prompt\_tokens | integer | Number of tokens in the prompt. |
-| total\_tokens | integer | Total number of tokens used in the request (prompt + completion). |
-
-
-### ContentFilterError
-
-The API call fails when the prompt triggers a content filter as configured. Modify the prompt and try again.
-
-
-| Name | Type | Description |
-| --- | --- | --- |
-| code | string | The error code. |
-| error | string | The error description. |
-| message | string | The error message. |
-| param | string | The parameter that triggered the content filter. |
-| status | integer | The HTTP status code. |
-
-
-### CreateCompletionRequest
-
-
-| Name | Type | Default Value | Description |
-| --- | --- | --- | --- |
-| frequency\_penalty | number | 0   | Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. |
-| max\_tokens | integer | 256 | The maximum number of tokens that can be generated in the completion. The token count of your prompt plus `max_tokens` cannot exceed the model's context length. |
-| presence\_penalty | number | 0   | Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. |
-| prompt |     | `<\|endoftext\|>` | The prompts to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays. Note that `<\|endoftext\|>` is the document separator that the model sees during training, so if a prompt is not specified the model generates as if from the beginning of a new document. |
-| seed | integer |     | If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.<br><br>Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend. |
-| stop |     |     | Sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence. |
-| stream | boolean | False | Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. |
-| temperature | number | 1   | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.<br><br>We generally recommend altering this or `top_p` but not both. |
-| top\_p | number | 1   | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br><br>We generally recommend altering this or `temperature` but not both. |
-
-
-### CreateCompletionResponse
-
-Represents a completion response from the API. Note: both the streamed and nonstreamed response objects share the same shape (unlike the chat endpoint).
-
-
-| Name | Type | Description |
-| --- | --- | --- |
-| choices | [Choices](#choices)\[\] | The list of completion choices the model generated for the input prompt. |
-| created | integer | The Unix timestamp (in seconds) of when the completion was created. |
-| ID  | string | A unique identifier for the completion. |
-| model | string | The model used for completion. |
-| object | [TextCompletionObject](#textcompletionobject) | The object type, which is always "text\_completion" |
-| system\_fingerprint | string | This fingerprint represents the backend configuration that the model runs with.<br><br>Can be used with the `seed` request parameter to understand when backend changes have been made that might impact determinism. |
-| usage | [CompletionUsage](#completionusage) | Usage statistics for the completion request. |
-
-### Detail
-
-
-| Name | Type | Description |
-| --- | --- | --- |
-| loc | string\[\] | The parameter causing the issue |
-| value | string | The value passed to the parameter causing issues. |
-
-
-### TextCompletionObject
-
-The object type, which is always "text\_completion"
-
-
-| Name | Type | Description |
-| --- | --- | --- |
-| text\_completion | string |     |
-
-### ListObject
-
-The object type, which is always "list".
-
-
-| Name | Type | Description |
-| --- | --- | --- |
-| list | string |     |
-
-### NotFoundError
-
-
-| Name | Type | Description |
-| --- | --- | --- |
-| error | string | The error description. |
-| message | string | The error message. |
-| status | integer | The HTTP status code. |
-
-### TooManyRequestsError
-
-
-| Name | Type | Description |
-| --- | --- | --- |
-| error | string | The error description. |
-| message | string | The error message. |
-| status | integer | The HTTP status code. |
-
-### UnauthorizedError
-
-
-| Name | Type | Description |
-| --- | --- | --- |
-| error | string | The error description. |
-| message | string | The error message. |
-| status | integer | The HTTP status code. |
-
-### UnprocessableContentError
-
-
-| Name | Type | Description |
-| --- | --- | --- |
-| code | string | The error code. |
-| detail | [Detail](#detail) |     |
-| error | string | The error description. |
-| message | string | The error message. |
-| status | integer | The HTTP status code. |
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデル推論完了に関するリファレンスの削除"
}
```

### Explanation
このコードの変更は、モデル推論完了に関するリファレンス文書が削除されたことを示しています。このリファレンスは、Azure AI Model Inference Completions APIに関する詳細な情報を提供しており、その内容にはAPIのエンドポイント、要求ヘッダー、リクエストボディ、レスポンスの形式、エラーハンドリングの方法などが含まれていました。

削除された行数は296行であり、このドキュメントは技術的に非常に重要な役割を果たしていた可能性があります。そのため、この変更は利用者にとって重大な影響を及ぼす恐れがあります。特に、APIの使用を前提としていた開発者や技術者に対しては、情報源が失われるため、新たな参照先を見つける必要が生じます。

願わくば、この変更に際しては、代わりのドキュメントやリソースへの案内が行われることが望まれます。また、どのような事情でこのリファレンスが削除されたのか、明確に説明されることが期待されます。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -140,6 +140,8 @@ items:
         href: how-to/deploy-models-cohere-embed.md
       - name: Cohere Rerank models
         href: how-to/deploy-models-cohere-rerank.md
+    - name: DeepSeek-R1 reasoning models
+      href: how-to/deploy-models-deepseek.md
     - name: Meta Llama models
       items:
       - name: Meta Llama family models
@@ -443,19 +445,7 @@ items:
   - name: Prompt flow Python SDK
     href: https://microsoft.github.io/promptflow/reference/index.html#
   - name: Azure AI Model Inference API
-    items:
-      - name: What's the Azure AI Model Inference API?
-        href: reference/reference-model-inference-api.md
-      - name: Reference
-        items:
-        - name: Get Info
-          href: reference/reference-model-inference-info.md
-        - name: Embeddings
-          href: reference/reference-model-inference-embeddings.md
-        - name: Chat Completions
-          href: reference/reference-model-inference-chat-completions.md
-        - name: Images Embeddings
-          href: reference/reference-model-inference-images-embeddings.md
+    href: ../ai-foundry/model-inference/reference/reference-model-inference-api.md
   - name: Azure Policy built-ins
     displayName: samples, policies, definitions
     href: ../ai-services/policy-reference.md?context=/azure/ai-studio/context/context
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCファイルの更新による新しいモデルの追加とリファレンスの整理"
}
```

### Explanation
このコードの変更は、`toc.yml`ファイルに関するものであり、3つの新しい項目が追加され、13行が削除され、合計で16行の変更が行われました。具体的には、DeepSeek-R1推論モデルが追加され、関連するデプロイ手順へのリンクが更新されています。

さらに、Azure AI Model Inference APIに関連する内容が整理され、以前の細分化されたリストは削除され、新しいリンクとして1つのリファレンスに統合されました。この変更により、ユーザーは新たに追加されたモデルにアクセスしやすくなり、情報がより一層明確化されることが期待されます。

このような更新は、ドキュメント全体の整合性を向上させるものであり、ユーザーが必要な情報に迅速にアクセスできるよう配慮されています。特に、AIモデルやリファレンスの使用に関連するセクションの簡素化は、エンドユーザーに対する利便性を向上させる要因となります。


