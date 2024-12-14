---
date: '2024-12-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3d9c9bc...MicrosoftDocs:d4c5788
summary: 今回の更新では、AI Studio文書でLlama、Mistral、Phiモデルに関する情報が改訂され、ユーザーに最新のモデル情報が提供されるようになりました。また、サンプルデータパスやスクリプトの更新により、チュートリアルの実行がスムーズになりました。新たにPhi-4ファミリーのチャットモデルに関するガイドが追加され、Phi-4モデルがリファレンスAPIに組み込まれました。LlamaやMistralファミリーに関する情報が更新され、モデルの可用性がより確認しやすくなっています。全体として、正確な情報とユーザビリティ向上を目指した重要なアップデートが実施されました。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3d9c9bc...MicrosoftDocs:d4c5788){target="_blank"}

# ハイライト
今回の更新では、AI Studio文書においてLlama、Mistral、Phiモデルに関する情報の改訂および追加が行われ、ユーザーに最新のモデル情報が提供されるようになりました。また、サンプルデータパスやスクリプトの更新により、チュートリアルのスムーズな実行が可能になりました。

## 新機能
- Phi-4ファミリーのチャットモデルに関する新しいガイドが追加
- Phi-4モデルがリファレンスAPIに追加

## 重大な変更
特に重大な変更はありませんでしたが、LlamaやMistralファミリーの情報に一部変更が加わり、ユーザーが最新のモデルバージョンや可用性を確認しやすくなりました。

## その他の更新
- Llama 3.3モデルに関する情報更新
- Mistralモデルの情報更新および新しい属性情報の追加
- 所定のチュートリアル文書におけるサンプルデータのパスやスクリプトの更新

# 洞察
今回のアップデートでは、AIモデルの最新情報をユーザーに提供するための一連の調整が行われています。Llamaモデル情報の更新によって、新たにLlama 3.3シリーズが導入され、これは性能や機能面で向上を期待できるでしょう。また、Mistral Largeモデルについては、複数の変種の詳細情報が加えられ、より精密なモデル選定が可能となっています。

さらに、Phi-4ファミリーのチャットモデルに関するドキュメントの新規追加は、完全な新機能の提供を示しており、Azure AI Foundryでの実装例やAPIアクセス方法まで詳細に紹介されています。これにより、ユーザーは最新の技術を試すハードルが下がり、開発プロセスの効率化を図れるでしょう。

また、様々なチュートリアルにおいてサンプルデータとスクリプトのパスが更新されており、最新の開発環境に対応したコンテンツが提供されています。この更新により、ユーザーは直感的にステップを追うことができ、チュートリアルがより理解しやすくなっています。全体として、情報の正確性とユーザービリティの向上を目的とした、小規模ながらも重要なアップデートが行われています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [deploy-models-llama.md](#item-6274a7) | minor update | Llama 3.3モデルに関する情報の更新 | modified | 6 | 1 | 7 | 
| [deploy-models-mistral.md](#item-487a41) | minor update | Mistralモデルの情報更新と追加 | modified | 38 | 14 | 52 | 
| [deploy-models-phi-4.md](#item-c40212) | new feature | Phi-4ファミリーのチャットモデルに関する新しいガイド | added | 1141 | 0 | 1141 | 
| [model-catalog-overview.md](#item-278001) | minor update | Llamaファミリーのモデルバージョンの更新 | modified | 1 | 1 | 2 | 
| [region-availability-maas.md](#item-35d79c) | minor update | Mistralファミリーのモデル情報の更新 | modified | 2 | 2 | 4 | 
| [reference-model-inference-api.md](#item-9fe240) | minor update | Phi-4モデルの追加とAPIリファレンスリンクの修正 | modified | 4 | 4 | 8 | 
| [toc.yml](#item-2745cd) | minor update | Phiファミリーのモデル名の変更とPhi-4モデルの追加 | modified | 4 | 2 | 6 | 
| [copilot-sdk-build-rag.md](#item-b77dba) | minor update | サンプルデータのパス変更とスクリプトの修正 | modified | 16 | 15 | 31 | 
| [copilot-sdk-create-resources.md](#item-552960) | minor update | リソース作成チュートリアルのファイルパス更新 | modified | 2 | 2 | 4 | 
| [copilot-sdk-evaluate.md](#item-bb5754) | minor update | 評価チュートリアルのファイルパス更新 | modified | 4 | 4 | 8 | 


# Modified Contents
## articles/ai-studio/how-to/deploy-models-llama.md{#item-6274a7}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 
 In this article, you learn about the Meta Llama family of models and how to use them. Meta Llama models and tools are a collection of pretrained and fine-tuned generative AI text and image reasoning models - ranging in scale from SLMs (1B, 3B Base and Instruct models) for on-device and edge inferencing - to mid-size LLMs (7B, 8B and 70B Base and Instruct models) and high performant models like Meta Llama 3.1 405B Instruct for synthetic data generation and distillation use cases.
 
-See our announcements of Meta's Llama 3.2 family models available now on Azure AI Model Catalog through [Meta's blog](https://aka.ms/llama-3.2-meta-announcement) and [Microsoft Tech Community Blog](https://aka.ms/llama-3.2-microsoft-announcement).
+See our announcements of Meta's Llama 3.3 family models available now on Azure AI Model Catalog through [Microsoft Tech Community Blog](https://aka.ms/Metallama70blaunchblog).
 
 [!INCLUDE [models-preview](../includes/models-preview.md)]
 
@@ -30,6 +30,11 @@ See our announcements of Meta's Llama 3.2 family models available now on Azure A
 
 The Meta Llama family of models include the following models:
 
+# [Llama-3.3](#tab/python-llama-3-3)
+
+* Llama-3.3-70B-Instruct
+
+
 # [Llama-3.2](#tab/python-llama-3-2)
 
 The Llama 3.2 collection of SLMs and image reasoning models are now available. Coming soon, Llama 3.2 11B Vision Instruct and Llama 3.2 90B Vision Instruct will be available as a serverless API endpoint via Models-as-a-Service. Starting today, the following models will be available for deployment via managed compute:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Llama 3.3モデルに関する情報の更新"
}
```

### Explanation
この修正は、AI Studioの「Llamaモデルのデプロイ方法」に関する文書で、Llama 3.2モデルの情報をLlama 3.3モデルに更新しています。具体的には、Llama 3.3ファミリーモデルに関するリンクと説明が追加され、旧情報が削除されました。また、文中に新たにLlama-3.3-70B-Instructモデルが追加されています。この更新により、ユーザーは最新のモデル情報にアクセスできるようになり、Azure AI Model Catalogでの利用が促進されます。全体として、記事の情報が更新され、エンドユーザーに対してより関連性の高いコンテンツが提供されることになりました。

## articles/ai-studio/how-to/deploy-models-mistral.md{#item-487a41}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Mistral premium chat models with Azure AI Foundry.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 10/23/2024
+ms.date: 11/20/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -31,27 +31,33 @@ The Mistral premium chat models include the following models:
 
 # [Mistral Large](#tab/mistral-large)
 
-Mistral Large is Mistral AI's most advanced Large Language Model (LLM). It can be used on any language-based task, thanks to its state-of-the-art reasoning and knowledge capabilities.
+Mistral Large models are Mistral AI's most advanced Large Language Models (LLM). They can be used on any language-based task, thanks to their state-of-the-art reasoning, knowledge, and coding capabilities. Several Mistral Large model variants are available, and their attributes are as follows.
 
-Additionally, Mistral Large is:
+Attributes of **Mistral Large (2402)**, also abbreviated as Mistral Large, include:
 
 * **Specialized in RAG**. Crucial information isn't lost in the middle of long context windows (up to 32-K tokens).
 * **Strong in coding**. Code generation, review, and comments. Supports all mainstream coding languages.
 * **Multi-lingual by design**. Best-in-class performance in French, German, Spanish, Italian, and English. Dozens of other languages are supported.
 * **Responsible AI compliant**. Efficient guardrails baked in the model and extra safety layer with the safe_mode option.
 
-And attributes of Mistral Large (2407) include:
+Attributes of **Mistral Large (2407)** include:
 
 * **Multi-lingual by design**. Supports dozens of languages, including English, French, German, Spanish, and Italian.
 * **Proficient in coding**. Trained on more than 80 coding languages, including Python, Java, C, C++, JavaScript, and Bash. Also trained on more specific languages such as Swift and Fortran.
 * **Agent-centric**. Possesses agentic capabilities with native function calling and JSON outputting.
 * **Advanced in reasoning**. Demonstrates state-of-the-art mathematical and reasoning capabilities.
 
+Attributes of **Mistral Large (2411)** include the same as Mistral Large (2407) with the following additional attributes:
+* System prompts are injected before each conversation.
+* Better performance on long content.
+* Improved function calling capabilities.
+
 
 The following models are available:
 
 * [Mistral-Large](https://aka.ms/azureai/landing/Mistral-Large)
 * [Mistral-Large-2407](https://aka.ms/azureai/landing/Mistral-Large-2407)
+* [Mistral-Large-2411](https://aka.ms/aistudio/landing/Mistral-Large-2411)
 
 
 # [Mistral Small](#tab/mistral-small)
@@ -515,27 +521,33 @@ The Mistral premium chat models include the following models:
 
 # [Mistral Large](#tab/mistral-large)
 
-Mistral Large is Mistral AI's most advanced Large Language Model (LLM). It can be used on any language-based task, thanks to its state-of-the-art reasoning and knowledge capabilities.
+Mistral Large models are Mistral AI's most advanced Large Language Models (LLM). They can be used on any language-based task, thanks to their state-of-the-art reasoning, knowledge, and coding capabilities. Several Mistral Large model variants are available, and their attributes are as follows.
 
-Additionally, Mistral Large is:
+Attributes of **Mistral Large (2402)**, also abbreviated as Mistral Large, include:
 
 * **Specialized in RAG**. Crucial information isn't lost in the middle of long context windows (up to 32-K tokens).
 * **Strong in coding**. Code generation, review, and comments. Supports all mainstream coding languages.
 * **Multi-lingual by design**. Best-in-class performance in French, German, Spanish, Italian, and English. Dozens of other languages are supported.
 * **Responsible AI compliant**. Efficient guardrails baked in the model and extra safety layer with the safe_mode option.
 
-And attributes of Mistral Large (2407) include:
+Attributes of **Mistral Large (2407)** include:
 
 * **Multi-lingual by design**. Supports dozens of languages, including English, French, German, Spanish, and Italian.
 * **Proficient in coding**. Trained on more than 80 coding languages, including Python, Java, C, C++, JavaScript, and Bash. Also trained on more specific languages such as Swift and Fortran.
 * **Agent-centric**. Possesses agentic capabilities with native function calling and JSON outputting.
 * **Advanced in reasoning**. Demonstrates state-of-the-art mathematical and reasoning capabilities.
 
+Attributes of **Mistral Large (2411)** include the same as Mistral Large (2407) with the following additional attributes:
+* System prompts are injected before each conversation.
+* Better performance on long content.
+* Improved function calling capabilities.
+
 
 The following models are available:
 
 * [Mistral-Large](https://aka.ms/azureai/landing/Mistral-Large)
 * [Mistral-Large-2407](https://aka.ms/azureai/landing/Mistral-Large-2407)
+* [Mistral-Large-2411](https://aka.ms/aistudio/landing/Mistral-Large-2411)
 
 
 # [Mistral Small](#tab/mistral-small)
@@ -1018,27 +1030,33 @@ The Mistral premium chat models include the following models:
 
 # [Mistral Large](#tab/mistral-large)
 
-Mistral Large is Mistral AI's most advanced Large Language Model (LLM). It can be used on any language-based task, thanks to its state-of-the-art reasoning and knowledge capabilities.
+Mistral Large models are Mistral AI's most advanced Large Language Models (LLM). They can be used on any language-based task, thanks to their state-of-the-art reasoning, knowledge, and coding capabilities. Several Mistral Large model variants are available, and their attributes are as follows.
 
-Additionally, Mistral Large is:
+Attributes of **Mistral Large (2402)**, also abbreviated as Mistral Large, include:
 
 * **Specialized in RAG**. Crucial information isn't lost in the middle of long context windows (up to 32-K tokens).
 * **Strong in coding**. Code generation, review, and comments. Supports all mainstream coding languages.
 * **Multi-lingual by design**. Best-in-class performance in French, German, Spanish, Italian, and English. Dozens of other languages are supported.
 * **Responsible AI compliant**. Efficient guardrails baked in the model and extra safety layer with the safe_mode option.
 
-And attributes of Mistral Large (2407) include:
+Attributes of **Mistral Large (2407)** include:
 
 * **Multi-lingual by design**. Supports dozens of languages, including English, French, German, Spanish, and Italian.
 * **Proficient in coding**. Trained on more than 80 coding languages, including Python, Java, C, C++, JavaScript, and Bash. Also trained on more specific languages such as Swift and Fortran.
 * **Agent-centric**. Possesses agentic capabilities with native function calling and JSON outputting.
 * **Advanced in reasoning**. Demonstrates state-of-the-art mathematical and reasoning capabilities.
 
+Attributes of **Mistral Large (2411)** include the same as Mistral Large (2407) with the following additional attributes:
+* System prompts are injected before each conversation.
+* Better performance on long content.
+* Improved function calling capabilities.
+
 
 The following models are available:
 
 * [Mistral-Large](https://aka.ms/azureai/landing/Mistral-Large)
 * [Mistral-Large-2407](https://aka.ms/azureai/landing/Mistral-Large-2407)
+* [Mistral-Large-2411](https://aka.ms/aistudio/landing/Mistral-Large-2411)
 
 
 # [Mistral Small](#tab/mistral-small)
@@ -1543,27 +1561,33 @@ The Mistral premium chat models include the following models:
 
 # [Mistral Large](#tab/mistral-large)
 
-Mistral Large is Mistral AI's most advanced Large Language Model (LLM). It can be used on any language-based task, thanks to its state-of-the-art reasoning and knowledge capabilities.
+Mistral Large models are Mistral AI's most advanced Large Language Models (LLM). They can be used on any language-based task, thanks to their state-of-the-art reasoning, knowledge, and coding capabilities. Several Mistral Large model variants are available, and their attributes are as follows.
 
-Additionally, Mistral Large is:
+Attributes of **Mistral Large (2402)**, also abbreviated as Mistral Large, include:
 
 * **Specialized in RAG**. Crucial information isn't lost in the middle of long context windows (up to 32-K tokens).
 * **Strong in coding**. Code generation, review, and comments. Supports all mainstream coding languages.
 * **Multi-lingual by design**. Best-in-class performance in French, German, Spanish, Italian, and English. Dozens of other languages are supported.
 * **Responsible AI compliant**. Efficient guardrails baked in the model and extra safety layer with the safe_mode option.
 
-And attributes of Mistral Large (2407) include:
+Attributes of **Mistral Large (2407)** include:
 
 * **Multi-lingual by design**. Supports dozens of languages, including English, French, German, Spanish, and Italian.
 * **Proficient in coding**. Trained on more than 80 coding languages, including Python, Java, C, C++, JavaScript, and Bash. Also trained on more specific languages such as Swift and Fortran.
 * **Agent-centric**. Possesses agentic capabilities with native function calling and JSON outputting.
 * **Advanced in reasoning**. Demonstrates state-of-the-art mathematical and reasoning capabilities.
 
+Attributes of **Mistral Large (2411)** include the same as Mistral Large (2407) with the following additional attributes:
+* System prompts are injected before each conversation.
+* Better performance on long content.
+* Improved function calling capabilities.
+
 
 The following models are available:
 
 * [Mistral-Large](https://aka.ms/azureai/landing/Mistral-Large)
 * [Mistral-Large-2407](https://aka.ms/azureai/landing/Mistral-Large-2407)
+* [Mistral-Large-2411](https://aka.ms/aistudio/landing/Mistral-Large-2411)
 
 
 # [Mistral Small](#tab/mistral-small)
@@ -2147,7 +2171,7 @@ View the response from the model:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralモデルの情報更新と追加"
}
```

### Explanation
この修正は、Mistralプレミアムチャットモデルに関する文書を更新し、新たな情報を追加しています。主な変更点として、Mistral Largeモデルの説明が強化され、モデルの属性が詳細に記述されています。具体的には、Mistral Largeが複数の変種（2402、2407、2411）を持つことや、それぞれの特徴（コーディング能力、マルチリンガル対応、エージェント機能、優れた推論能力など）が明確になりました。また、Mistral Large (2411)には新たにシステムプロンプトや長文処理能力に関する追加属性が含まれました。さらに、ドキュメントの日付も更新され、継続的な情報の正確性が保証されています。全体として、ユーザーは新しいモデルに関するより充実した情報を得ることができ、AIモデルに関する理解が深まることが期待されます。

## articles/ai-studio/how-to/deploy-models-phi-4.md{#item-c40212}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,1141 @@
+---
+title: How to use Phi-4 family chat models with Azure AI Foundry
+titleSuffix: Azure AI Foundry
+description: Learn how to use Phi-4 family chat models with Azure AI Foundry.
+ms.service: azure-ai-studio
+manager: scottpolly
+ms.topic: how-to
+ms.date: 12/12/2024
+ms.reviewer: fasantia
+reviewer: santiagxf
+ms.author: mopeakande
+author: msakande
+ms.custom: references_regions, generated
+zone_pivot_groups: azure-ai-model-catalog-samples-chat
+---
+
+# How to use Phi-4 family chat models
+
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
+
+In this article, you learn about Phi-4 family chat models and how to use them.
+The Phi-4 family of small language models (SLMs) is a collection of instruction-tuned generative text models.
+
+
+
+::: zone pivot="programming-language-python"
+
+## Phi-4 family chat models
+
+Phi-4 is a state-of-the-art open model built upon a blend of synthetic datasets, data from filtered public domain websites, and acquired academic books and Q&A datasets. The goal of this approach was to ensure that small capable models were trained with data focused on high quality and advanced reasoning.
+
+Phi-4 underwent a rigorous enhancement and alignment process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures.
+
+The Phi-4 models come in the following variants with a 16K tokens length.
+
+
+You can learn more about the models in their respective model card:
+
+* [Phi-4](https://aka.ms/azureai/landing/Phi-4)
+
+
+## Prerequisites
+
+To use Phi-4 family chat models with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to a self-hosted managed compute**
+
+Phi-4 family chat models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
+
+For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
+
+> [!div class="nextstepaction"]
+> [Deploy the model to managed compute](../concepts/deployments-overview.md)
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
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry with the same code and structure, including Phi-4 family chat models.
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
+When you deploy the model to a self-hosted online endpoint with **Microsoft Entra ID** support, you can use the following code snippet to create a client.
+
+
+```python
+import os
+from azure.ai.inference import ChatCompletionsClient
+from azure.identity import DefaultAzureCredential
+
+client = ChatCompletionsClient(
+    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    credential=DefaultAzureCredential(),
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
+Model name: Phi-4
+Model type: chat-completions
+Model provider name: Microsoft
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
+Model: Phi-4
+Usage: 
+  Prompt tokens: 19
+  Total tokens: 91
+  Completion tokens: 72
+```
+
+Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
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
+    import time
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
+#### Explore more parameters supported by the inference client
+
+Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
+
+```python
+from azure.ai.inference.models import ChatCompletionsResponseFormatText
+
+response = client.complete(
+    messages=[
+        SystemMessage(content="You are a helpful assistant."),
+        UserMessage(content="How many languages are in the world?"),
+    ],
+    presence_penalty=0.1,
+    frequency_penalty=0.8,
+    max_tokens=2048,
+    stop=["<|endoftext|>"],
+    temperature=0,
+    top_p=1,
+    response_format={ "type": ChatCompletionsResponseFormatText() },
+)
+```
+
+> [!WARNING]
+> Phi-4 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+
+If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
+
+### Pass extra parameters to the model
+
+The Azure AI Model Inference API allows you to pass extra parameters to the model. The following code example shows how to pass the extra parameter `logprobs` to the model. 
+
+Before you pass extra parameters to the Azure AI model inference API, make sure your model supports those extra parameters. When the request is made to the underlying model, the header `extra-parameters` is passed to the model with the value `pass-through`. This value tells the endpoint to pass the extra parameters to the model. Use of extra parameters with the model doesn't guarantee that the model can actually handle them. Read the model's documentation to understand which extra parameters are supported.
+
+
+```python
+response = client.complete(
+    messages=[
+        SystemMessage(content="You are a helpful assistant."),
+        UserMessage(content="How many languages are in the world?"),
+    ],
+    model_extras={
+        "logprobs": True
+    }
+)
+```
+
+The following extra parameters can be passed to Phi-4 family chat models:
+
+| Name           | Description           | Type            |
+| -------------- | --------------------- | --------------- |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
+| `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
+| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+
+
+::: zone-end
+
+
+::: zone pivot="programming-language-javascript"
+
+## Phi-4 family chat models
+
+Phi-4 is a state-of-the-art open model built upon a blend of synthetic datasets, data from filtered public domain websites, and acquired academic books and Q&A datasets. The goal of this approach was to ensure that small capable models were trained with data focused on high quality and advanced reasoning.
+
+Phi-4 underwent a rigorous enhancement and alignment process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures.
+
+The Phi-4 models come in the following variants with a 16K tokens length.
+
+
+You can learn more about the models in their respective model card:
+
+* [Phi-4](https://aka.ms/azureai/landing/Phi-4)
+
+
+## Prerequisites
+
+To use Phi-4 family chat models with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to a self-hosted managed compute**
+
+Phi-4 family chat models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
+
+For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
+
+> [!div class="nextstepaction"]
+> [Deploy the model to managed compute](../concepts/deployments-overview.md)
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
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry with the same code and structure, including Phi-4 family chat models.
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
+When you deploy the model to a self-hosted online endpoint with **Microsoft Entra ID** support, you can use the following code snippet to create a client.
+
+
+```javascript
+import ModelClient from "@azure-rest/ai-inference";
+import { isUnexpected } from "@azure-rest/ai-inference";
+import { DefaultAzureCredential }  from "@azure/identity";
+
+const client = new ModelClient(
+    process.env.AZURE_INFERENCE_ENDPOINT, 
+    new DefaultAzureCredential()
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
+Model name: Phi-4
+Model type: chat-completions
+Model provider name: Microsoft
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
+Model: Phi-4
+Usage: 
+  Prompt tokens: 19
+  Total tokens: 91
+  Completion tokens: 72
+```
+
+Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
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
+#### Explore more parameters supported by the inference client
+
+Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
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
+        presence_penalty: "0.1",
+        frequency_penalty: "0.8",
+        max_tokens: 2048,
+        stop: ["<|endoftext|>"],
+        temperature: 0,
+        top_p: 1,
+        response_format: { type: "text" },
+    }
+});
+```
+
+> [!WARNING]
+> Phi-4 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+
+If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
+
+### Pass extra parameters to the model
+
+The Azure AI Model Inference API allows you to pass extra parameters to the model. The following code example shows how to pass the extra parameter `logprobs` to the model. 
+
+Before you pass extra parameters to the Azure AI model inference API, make sure your model supports those extra parameters. When the request is made to the underlying model, the header `extra-parameters` is passed to the model with the value `pass-through`. This value tells the endpoint to pass the extra parameters to the model. Use of extra parameters with the model doesn't guarantee that the model can actually handle them. Read the model's documentation to understand which extra parameters are supported.
+
+
+```javascript
+var messages = [
+    { role: "system", content: "You are a helpful assistant" },
+    { role: "user", content: "How many languages are in the world?" },
+];
+
+var response = await client.path("/chat/completions").post({
+    headers: {
+        "extra-params": "pass-through"
+    },
+    body: {
+        messages: messages,
+        logprobs: true
+    }
+});
+```
+
+The following extra parameters can be passed to Phi-4 family chat models:
+
+| Name           | Description           | Type            |
+| -------------- | --------------------- | --------------- |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
+| `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
+| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+
+
+::: zone-end
+
+
+::: zone pivot="programming-language-csharp"
+
+## Phi-4 family chat models
+
+Phi-4 is a state-of-the-art open model built upon a blend of synthetic datasets, data from filtered public domain websites, and acquired academic books and Q&A datasets. The goal of this approach was to ensure that small capable models were trained with data focused on high quality and advanced reasoning.
+
+Phi-4 underwent a rigorous enhancement and alignment process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures.
+
+The Phi-4 models come in the following variants with a 16K tokens length.
+
+
+You can learn more about the models in their respective model card:
+
+* [Phi-4](https://aka.ms/azureai/landing/Phi-4)
+
+
+## Prerequisites
+
+To use Phi-4 family chat models with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to a self-hosted managed compute**
+
+Phi-4 family chat models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
+
+For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
+
+> [!div class="nextstepaction"]
+> [Deploy the model to managed compute](../concepts/deployments-overview.md)
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
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry with the same code and structure, including Phi-4 family chat models.
+
+### Create a client to consume the model
+
+First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
+
+
+```csharp
+ChatCompletionsClient client = new ChatCompletionsClient(
+    new Uri(Environment.GetEnvironmentVariable("AZURE_INFERENCE_ENDPOINT")),
+    new AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_INFERENCE_CREDENTIAL"))
+);
+```
+
+When you deploy the model to a self-hosted online endpoint with **Microsoft Entra ID** support, you can use the following code snippet to create a client.
+
+
+```csharp
+client = new ChatCompletionsClient(
+    new Uri(Environment.GetEnvironmentVariable("AZURE_INFERENCE_ENDPOINT")),
+    new DefaultAzureCredential(includeInteractiveCredentials: true)
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
+Model name: Phi-4
+Model type: chat-completions
+Model provider name: Microsoft
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
+Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
+Console.WriteLine($"Model: {response.Value.Model}");
+Console.WriteLine("Usage:");
+Console.WriteLine($"\tPrompt tokens: {response.Value.Usage.PromptTokens}");
+Console.WriteLine($"\tTotal tokens: {response.Value.Usage.TotalTokens}");
+Console.WriteLine($"\tCompletion tokens: {response.Value.Usage.CompletionTokens}");
+```
+
+```console
+Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
+Model: Phi-4
+Usage: 
+  Prompt tokens: 19
+  Total tokens: 91
+  Completion tokens: 72
+```
+
+Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
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
+#### Explore more parameters supported by the inference client
+
+Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
+
+```csharp
+requestOptions = new ChatCompletionsOptions()
+{
+    Messages = {
+        new ChatRequestSystemMessage("You are a helpful assistant."),
+        new ChatRequestUserMessage("How many languages are in the world?")
+    },
+    PresencePenalty = 0.1f,
+    FrequencyPenalty = 0.8f,
+    MaxTokens = 2048,
+    StopSequences = { "<|endoftext|>" },
+    Temperature = 0,
+    NucleusSamplingFactor = 1,
+    ResponseFormat = new ChatCompletionsResponseFormatText()
+};
+
+response = client.Complete(requestOptions);
+Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
+```
+
+> [!WARNING]
+> Phi-4 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+
+If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
+
+### Pass extra parameters to the model
+
+The Azure AI Model Inference API allows you to pass extra parameters to the model. The following code example shows how to pass the extra parameter `logprobs` to the model. 
+
+Before you pass extra parameters to the Azure AI model inference API, make sure your model supports those extra parameters. When the request is made to the underlying model, the header `extra-parameters` is passed to the model with the value `pass-through`. This value tells the endpoint to pass the extra parameters to the model. Use of extra parameters with the model doesn't guarantee that the model can actually handle them. Read the model's documentation to understand which extra parameters are supported.
+
+
+```csharp
+requestOptions = new ChatCompletionsOptions()
+{
+    Messages = {
+        new ChatRequestSystemMessage("You are a helpful assistant."),
+        new ChatRequestUserMessage("How many languages are in the world?")
+    },
+    AdditionalProperties = { { "logprobs", BinaryData.FromString("true") } },
+};
+
+response = client.Complete(requestOptions, extraParams: ExtraParameters.PassThrough);
+Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
+```
+
+The following extra parameters can be passed to Phi-4 family chat models:
+
+| Name           | Description           | Type            |
+| -------------- | --------------------- | --------------- |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
+| `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
+| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+
+
+::: zone-end
+
+
+::: zone pivot="programming-language-rest"
+
+## Phi-4 family chat models
+
+Phi-4 is a state-of-the-art open model built upon a blend of synthetic datasets, data from filtered public domain websites, and acquired academic books and Q&A datasets. The goal of this approach was to ensure that small capable models were trained with data focused on high quality and advanced reasoning.
+
+Phi-4 underwent a rigorous enhancement and alignment process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures.
+
+The Phi-4 models come in the following variants with a 16K tokens length.
+
+
+You can learn more about the models in their respective model card:
+
+* [Phi-4](https://aka.ms/azureai/landing/Phi-4)
+
+
+## Prerequisites
+
+To use Phi-4 family chat models with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to a self-hosted managed compute**
+
+Phi-4 family chat models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
+
+For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
+
+> [!div class="nextstepaction"]
+> [Deploy the model to managed compute](../concepts/deployments-overview.md)
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
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry with the same code and structure, including Phi-4 family chat models.
+
+### Create a client to consume the model
+
+First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
+
+When you deploy the model to a self-hosted online endpoint with **Microsoft Entra ID** support, you can use the following code snippet to create a client.
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
+    "model_name": "Phi-4",
+    "model_type": "chat-completions",
+    "model_provider_name": "Microsoft"
+}
+```
+
+### Create a chat completion request
+
+The following example shows how you can create a basic chat completions request to the model.
+
+```json
+{
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
+    "model": "Phi-4",
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
+#### Stream content
+
+By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
+
+You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
+
+
+```json
+{
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
+    "model": "Phi-4",
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
+    "model": "Phi-4",
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
+#### Explore more parameters supported by the inference client
+
+Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
+
+```json
+{
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
+    "presence_penalty": 0.1,
+    "frequency_penalty": 0.8,
+    "max_tokens": 2048,
+    "stop": ["<|endoftext|>"],
+    "temperature" :0,
+    "top_p": 1,
+    "response_format": { "type": "text" }
+}
+```
+
+
+```json
+{
+    "id": "0a1234b5de6789f01gh2i345j6789klm",
+    "object": "chat.completion",
+    "created": 1718726686,
+    "model": "Phi-4",
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
+> [!WARNING]
+> Phi-4 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+
+If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
+
+### Pass extra parameters to the model
+
+The Azure AI Model Inference API allows you to pass extra parameters to the model. The following code example shows how to pass the extra parameter `logprobs` to the model. 
+
+Before you pass extra parameters to the Azure AI model inference API, make sure your model supports those extra parameters. When the request is made to the underlying model, the header `extra-parameters` is passed to the model with the value `pass-through`. This value tells the endpoint to pass the extra parameters to the model. Use of extra parameters with the model doesn't guarantee that the model can actually handle them. Read the model's documentation to understand which extra parameters are supported.
+
+```http
+POST /chat/completions HTTP/1.1
+Host: <ENDPOINT_URI>
+Authorization: Bearer <TOKEN>
+Content-Type: application/json
+extra-parameters: pass-through
+```
+
+
+```json
+{
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
+    "logprobs": true
+}
+```
+
+The following extra parameters can be passed to Phi-4 family chat models:
+
+| Name           | Description           | Type            |
+| -------------- | --------------------- | --------------- |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
+| `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
+| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+
+
+::: zone-end
+
+## More inference examples
+
+For more examples of how to use Phi-4 family models, see the following examples and tutorials:
+
+| Description                               | Language          | Sample                                                          |
+|-------------------------------------------|-------------------|-----------------------------------------------------------------|
+| CURL request                              | Bash              | [Link](https://aka.ms/phi-3/webrequests-sample)         |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
+| Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
+| Python web requests                       | Python            | [Link](https://aka.ms/phi-3/webrequests-sample)         |
+| OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/phi-3/openaisdk)                  |
+| LangChain                                 | Python            | [Link](https://aka.ms/phi-3/langchain-sample)           |
+| LiteLLM                                   | Python            | [Link](https://aka.ms/phi-3/litellm-sample)             | 
+
+
+## Cost and quota considerations for Phi-4 family models deployed to managed compute
+
+Phi-4 family models deployed to managed compute are billed based on core hours of the associated compute instance. The cost of the compute instance is determined by the size of the instance, the number of instances running, and the run duration.
+
+It is a good practice to start with a low number of instances and scale up as needed. You can monitor the cost of the compute instance in the Azure portal.
+
+## Related content
+
+
+* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Deploy models as serverless APIs](deploy-models-serverless.md)
+* [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
+* [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Phi-4ファミリーのチャットモデルに関する新しいガイド"
}
```

### Explanation
この修正は、AI Studioにおいて「Phi-4ファミリーのチャットモデル」に関する新しい文書を追加しています。この文書では、Phi-4ファミリー小型言語モデル（SLM）を使用する方法が詳細に説明されています。Phi-4モデルは、優れた推論能力を持つ状態最先端のオープンモデルで、合成データセットやフィルタリングされた公共ドメインのウェブサイト、学術書籍から得られたデータを組み合わせて構築されています。

文書には、Phi-4ファミリーモデルをAzure AI Foundryで展開するための前提条件や手順、実装例、APIを通じてのモデルへのアクセス方法が含まれています。また、Python、JavaScript、C#、REST APIに関連するクライアントライブラリの使用方法が具体的なコード例とともに示されています。加えて、Phi-4モデルの展開に関するコストやクォータの考慮事項も記載されており、情報に基づいた導入を行うための参考になる内容となっています。

この新しい文書の追加によって、ユーザーはPhi-4ファミリーモデルの利用方法を理解しやすくなり、Azure AI Foundryでの展開が容易になることが期待されます。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -77,7 +77,7 @@ The following list contains Serverless API models. For Azure OpenAI models, see
 
 Model | Managed compute | Serverless API (pay-per-token)
 --|--|--
-Llama family models | Llama-3.2-3B-Instruct<BR>  Llama-3.2-1B-Instruct<BR>  Llama-3.2-1B<BR>  Llama-3.2-90B-Vision-Instruct<BR>  Llama-3.2-11B-Vision-Instruct<BR>  Llama-3.1-8B-Instruct<BR>  Llama-3.1-8B<BR>  Llama-3.1-70B-Instruct<BR>  Llama-3.1-70B<BR>  Llama-3-8B-Instruct<BR>  Llama-3-70B<BR>  Llama-3-8B<BR>  Llama-Guard-3-1B<BR>  Llama-Guard-3-8B<BR>  Llama-Guard-3-11B-Vision<BR>  Llama-2-7b<BR>  Llama-2-70b<BR>  Llama-2-7b-chat<BR>  Llama-2-13b-chat<BR>  CodeLlama-7b-hf<BR>  CodeLlama-7b-Instruct-hf<BR>  CodeLlama-34b-hf<BR>  CodeLlama-34b-Python-hf<BR>  CodeLlama-34b-Instruct-hf<BR>  CodeLlama-13b-Instruct-hf<BR>  CodeLlama-13b-Python-hf<BR>  Prompt-Guard-86M<BR>  CodeLlama-70b-hf<BR> | Llama-3.2-90B-Vision-Instruct<br>  Llama-3.2-11B-Vision-Instruct<br>  Llama-3.1-8B-Instruct<br>  Llama-3.1-70B-Instruct<br>  Llama-3.1-405B-Instruct<br>  Llama-3-8B-Instruct<br>  Llama-3-70B-Instruct<br>  Llama-2-7b<br>  Llama-2-7b-chat<br>  Llama-2-70b<br>  Llama-2-70b-chat<br>  Llama-2-13b<br>  Llama-2-13b-chat<br>
+Llama family models | Llama-3.3-70B-Instruct<BR> Llama-3.2-3B-Instruct<BR>  Llama-3.2-1B-Instruct<BR>  Llama-3.2-1B<BR>  Llama-3.2-90B-Vision-Instruct<BR>  Llama-3.2-11B-Vision-Instruct<BR>  Llama-3.1-8B-Instruct<BR>  Llama-3.1-8B<BR>  Llama-3.1-70B-Instruct<BR>  Llama-3.1-70B<BR>  Llama-3-8B-Instruct<BR>  Llama-3-70B<BR>  Llama-3-8B<BR>  Llama-Guard-3-1B<BR>  Llama-Guard-3-8B<BR>  Llama-Guard-3-11B-Vision<BR>  Llama-2-7b<BR>  Llama-2-70b<BR>  Llama-2-7b-chat<BR>  Llama-2-13b-chat<BR>  CodeLlama-7b-hf<BR>  CodeLlama-7b-Instruct-hf<BR>  CodeLlama-34b-hf<BR>  CodeLlama-34b-Python-hf<BR>  CodeLlama-34b-Instruct-hf<BR>  CodeLlama-13b-Instruct-hf<BR>  CodeLlama-13b-Python-hf<BR>  Prompt-Guard-86M<BR>  CodeLlama-70b-hf<BR> | Llama-3.3-70B-Instruct<BR> Llama-3.2-90B-Vision-Instruct<br>  Llama-3.2-11B-Vision-Instruct<br>  Llama-3.1-8B-Instruct<br>  Llama-3.1-70B-Instruct<br>  Llama-3.1-405B-Instruct<br>  Llama-3-8B-Instruct<br>  Llama-3-70B-Instruct<br>  Llama-2-7b<br>  Llama-2-7b-chat<br>  Llama-2-70b<br>  Llama-2-70b-chat<br>  Llama-2-13b<br>  Llama-2-13b-chat<br>
 Mistral family models | mistralai-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x22B-Instruct-v0-1 <br> mistral-community-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x7B-v01 <br> mistralai-Mistral-7B-Instruct-v0-2 <br> mistralai-Mistral-7B-v01 <br> mistralai-Mixtral-8x7B-Instruct-v01 <br> mistralai-Mistral-7B-Instruct-v01 | Mistral-large (2402) <br> Mistral-large (2407) <br> Mistral-small <br> Ministral-3B <br> Mistral-NeMo
 Cohere family models | Not available | Cohere-command-r-plus-08-2024 <br> Cohere-command-r-08-2024 <br> Cohere-command-r-plus <br> Cohere-command-r <br> Cohere-embed-v3-english <br> Cohere-embed-v3-multilingual <br> Cohere-rerank-v3-english <br> Cohere-rerank-v3-multilingual
 JAIS | Not available | jais-30b-chat
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Llamaファミリーのモデルバージョンの更新"
}
```

### Explanation
この修正は、「モデルカタログ概要」文書においてLlamaファミリーのモデルに関する情報を更新しました。変更された内容には、Llamaファミリーの新しいモデルバージョン「Llama-3.3-70B-Instruct」が追加され、従来の「Llama-3.2」シリーズのモデルが変更されています。この更新により、利用可能なLlamaファミリーのモデルリストが最新の情報を反映し、ユーザーにとって選択肢が増えることになります。また、他のモデルファミリー（Mistral、Cohere、JAIS）についての情報は変更されていません。これにより、ユーザーは最新のモデルにアクセスするための正確な情報を得ることができるようになります。

## articles/ai-studio/includes/region-availability-maas.md{#item-35d79c}

<details>
<summary>Diff</summary>
````diff
@@ -60,8 +60,8 @@ Phi-3-Medium-4K-Instruct  <br>  Phi-3-Medium-128K-Instruct  | Not applicable | E
 Mistral Nemo     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong <br> Israel     | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
 Ministral-3B     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)   <br> Brazil <br> Hong Kong <br> Israel      | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           |  Not available       |
 Mistral Small     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)   <br> Brazil <br> Hong Kong <br> Israel      | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           |  Not available       |
-Mistral Large (2402)     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong <br> Israel    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
-Mistral-Large (2407)     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)   <br> Brazil <br> Hong Kong <br> Israel   | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
+Mistral Large <br>  Mistral-Large (2407) <br> Mistral-Large (2411)    | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong <br> Israel    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
+
 
 
 ### Nixtla models
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralファミリーのモデル情報の更新"
}
```

### Explanation
この修正は、「地域の可用性」に関する文書でMistralファミリーのモデルに関する情報を更新しました。変更点として、「Mistral Large (2402)」と「Mistral-Large (2407)」の二つのモデルを統合し、新しい形式で「Mistral Large」「Mistral-Large (2407)」「Mistral-Large (2411)」という名前のリストにまとめています。

この統合により、Mistralファミリーのモデルの可用性が一つの行に凝縮され、より整理された形で表示されるようになります。この更新は文書の一貫性を高め、ユーザーがモデルを見つけやすくするためのもので、地域における可用性についても情報は変更されていません。全体として、文書の可読性と使いやすさが向上します。

## articles/ai-studio/reference/reference-model-inference-api.md{#item-9fe240}

<details>
<summary>Diff</summary>
````diff
@@ -55,8 +55,8 @@ Models deployed to [managed inference](../concepts/deployments-overview.md):
 
 > [!div class="checklist"]
 > * [Meta Llama 3 instruct](../how-to/deploy-models-llama.md) family of models
-> * [Phi-3](../how-to/deploy-models-phi-3.md) family of models
-> * [Mistral](../how-to/deploy-models-mistral-open.md) and [Mixtral](../how-to/deploy-models-mistral-open.md?tabs=mistral-8x7B-instruct) family of models.
+> * [Phi-3](../how-to/deploy-models-phi-3.md), and [Phi-4](../how-to/deploy-models-phi-4.md) family of models
+> * [Mistral](../how-to/deploy-models-mistral-open.md) and [Mixtral](../how-to/deploy-models-mistral-open.md?tabs=mistral-8x7B-instruct) family of models
 
 The API is compatible with Azure OpenAI model deployments.
 
@@ -152,7 +152,7 @@ const client = new ModelClient(
 );
 ```
 
-Explore our [samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples) and read the [API reference documentation](https://aka.ms/AAp1kxa) to get yourself started.
+Explore our [samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples) and read the [API reference documentation](/javascript/api/@azure-rest/ai-inference) to get yourself started.
 
 # [C#](#tab/csharp)
 
@@ -602,7 +602,7 @@ Explore our [samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sd
 
 The client library `@azure-rest/ai-inference` does inference, including chat completions, for AI models deployed by Azure AI Foundry and Azure Machine Learning studio. It supports Serverless API endpoints and Managed Compute endpoints (formerly known as Managed Online Endpoints).
 
-Explore our [samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples) and read the [API reference documentation](https://aka.ms/AAp1kxa) to get yourself started.
+Explore our [samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples) and read the [API reference documentation](/javascript/api/@azure-rest/ai-inference) to get yourself started.
 
 # [C#](#tab/csharp)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-4モデルの追加とAPIリファレンスリンクの修正"
}
```

### Explanation
この修正は、「モデル推論API」に関する文書において、モデルのリストとAPIリファレンスのリンクを更新しました。具体的には、Phi-3モデルファミリーに加えてPhi-4モデルファミリーを追加し、モデルの一覧が最新の内容を反映するようにしました。また、APIリファレンスドキュメントへのリンクが変更され、より正確な参照先が提供されるようになりました。

修正された内容は、ユーザーが利用可能なモデルとそのドキュメントに関する情報の明確化を目的としており、新しいモデルがリストに追加されたことで、利用者が最新の情報に基づいたモデルを容易に発見できるようになっています。この変更により、利用者はより豊富な選択肢を持ち、正確なリファレンスにアクセスできるようになります。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -125,14 +125,16 @@ items:
           href: how-to/healthcare-ai/deploy-cxrreportgen.md
         - name: MedImageParse - prompted segmentation model
           href: how-to/healthcare-ai/deploy-medimageparse.md
-    - name: Phi-3 family models
+    - name: Microsoft Phi family models
       items:
-        - name: Phi-3 family chat models
+        - name: Phi-3 chat models
           href: how-to/deploy-models-phi-3.md
         - name: Phi-3 chat model with vision
           href: how-to/deploy-models-phi-3-vision.md
         - name: Phi-3.5 chat model with vision
           href: how-to/deploy-models-phi-3-5-vision.md
+        - name: Phi-4 chat models
+          href: how-to/deploy-models-phi-4.md
         - name: Fine-tune Phi-3 chat models
           href: how-to/fine-tune-phi-3.md
     - name: Cohere models
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phiファミリーのモデル名の変更とPhi-4モデルの追加"
}
```

### Explanation
この修正は、「Table of Contents (TOC)」ファイルにおいて、Microsoft Phiファミリーのモデル名を変更し、新しいPhi-4モデルを追加しました。具体的には、「Phi-3ファミリー」という名称が「Microsoft Phiファミリー」に変更され、その下に「Phi-3チャットモデル」というサブカテゴリが設けられました。この変更により、モデルのクラスターがより明確になり、ユーザーにとっての可読性が向上します。

さらに、Phi-4チャットモデルが追加され、これに関連するドキュメントへのリンクも提供されました。これにより、ユーザーは新しいモデルにアクセスする際に必要な情報を簡単に見つけやすくなります。この変更は、ドキュメントの構造を整理し、最新のモデル情報を反映させることを目的としています。全体として、ユーザーフレンドリーな更新と言えるでしょう。

## articles/ai-studio/tutorials/copilot-sdk-build-rag.md{#item-b77dba}

<details>
<summary>Diff</summary>
````diff
@@ -42,7 +42,7 @@ If you already have a search index with data, you can skip to [Get product docum
 
 Create an **assets** directory and add this example data to a **products.csv** file:
 
-:::code language="csv" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/assets/products.csv":::
+:::code language="csv" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/assets/products.csv":::
 
 ## Create a search index
 
@@ -52,19 +52,19 @@ The search index is used to store vectorized data from the embeddings model. The
 1. Copy and paste the following code into your **create_search_index.py** file.
 1. Add the code to import the required libraries, create a project client, and configure some settings: 
 
-    :::code language="python" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/create_search_index.py" id="imports_and_config":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/create_search_index.py" id="imports_and_config":::
 
 1. Now add the function to define a search index:
 
-    :::code language="python" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/create_search_index.py" id="create_search_index":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/create_search_index.py" id="create_search_index":::
 
 1. Create the function to add a csv file to the index:
 
-    :::code language="python" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/create_search_index.py" id="add_csv_to_index":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/create_search_index.py" id="add_csv_to_index":::
 
 1. Finally, run the functions to build the index and register it to the cloud project:
 
-    :::code language="python" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/create_search_index.py" id="test_create_index":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/create_search_index.py" id="test_create_index":::
 
 1. From your console, log in to your Azure account and follow instructions for authenticating your account:
 
@@ -95,23 +95,23 @@ When the chat gets a request, it searches through your data to find relevant inf
 
 1. Start with code to import the required libraries, create a project client, and configure settings: 
 
-    :::code language="python" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/get_product_documents.py" id="imports_and_config":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/get_product_documents.py" id="imports_and_config":::
 
 1. Add the function to get product documents:
 
-    :::code language="python" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/get_product_documents.py" id="get_product_documents":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/get_product_documents.py" id="get_product_documents":::
 
 1. Finally, add code to test the function when you run the script directly:
 
-    :::code language="python" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/get_product_documents.py" id="test_get_documents":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/get_product_documents.py" id="test_get_documents":::
 
 ### Create prompt template for intent mapping
 
 The **get_product_documents.py** script uses a prompt template to convert the conversation to a search query. The template instructs how to extract the user's intent from the conversation.  
 
 Before you run the script, create the prompt template. Add the file **intent_mapping.prompty** to your **assets** folder:
 
-:::code language="prompty" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/assets/intent_mapping.prompty":::
+:::code language="prompty" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/assets/intent_mapping.prompty":::
 
 ### Test the product document retrieval script
 
@@ -130,23 +130,23 @@ Next you create custom code to add retrieval augmented generation (RAG) capabili
 1. In your main folder, create a new file called **chat_with_products.py**. This script retrieves product documents and generates a response to a user's question.
 1. Add the code to import the required libraries, create a project client, and configure settings: 
 
-    :::code language="python" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/chat_with_products.py" id="imports_and_config":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/chat_with_products.py" id="imports_and_config":::
 
 1. Create the chat function that uses the RAG capabilities:
 
-    :::code language="python" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/chat_with_products.py" id="chat_function":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/chat_with_products.py" id="chat_function":::
 
 1. Finally, add the code to run the chat function:
     
-    :::code language="python" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/chat_with_products.py" id="test_function":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/chat_with_products.py" id="test_function":::
 
 ### Create a grounded chat prompt template
 
 The **chat_with_products.py** script calls a prompt template to generate a response to the user's question. The template instructs how to generate a response based on the user's question and the retrieved documents.  Create this template now.
 
 In your **assets** folder, add the file **grounded_chat.prompty**:
 
-:::code language="prompty" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/assets/grounded_chat.prompty":::
+:::code language="prompty" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/assets/grounded_chat.prompty":::
 
 ### Run the chat script with RAG capabilities
 
@@ -156,7 +156,7 @@ Now that you have both the script and the template, run the script to test your
 python chat_with_products.py --query "I need a new tent for 4 people, what would you recommend?"
 ```
 
-To enable logging of telemetry to your project:
+<!-- To enable logging of telemetry to your project:
 
 1. Install `azure-monitor-opentelemetry`:
 
@@ -167,8 +167,9 @@ To enable logging of telemetry to your project:
 1. Add the `--enable-telemetry` flag when you use the `chat_with_products.py` script:
 
    ```bash
-   python chat_with_products.py --query "I need a new tent for 4 people, what would you recommend?" --enable-telemetry
+   python chat_with_products.py --query "I need a new tent for 4 people, what would you recommend?" --enable-telemetry 
    ```
+-->
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サンプルデータのパス変更とスクリプトの修正"
}
```

### Explanation
この修正は、「Copilot SDKを使用してRAGを構築する」チュートリアルの文書において、サンプルデータへのパスを変更し、いくつかのスクリプトの参照を最新のディレクトリ構造に合わせて修正しました。具体的には、指定されたサンプルデータファイルやスクリプトファイルのパスが、以前の「azureai-samples-nov2024」から「azureai-samples-main」に更新されました。この変更は、ユーザーが最新のサンプルコードを正確に参照できるようにするためのものです。

また、修正に伴い、いくつかのコードブロックが更新され、全体としてドキュメントの整合性と可読性が向上しています。これにより、ユーザーは実際のデータやスクリプトを使用して、RAG機能を効果的に構築するための手順をより簡単に理解し、実行できるようになります。全体を通じて、より良いユーザーエクスペリエンスを提供することを目的としたマイナーな更新です。

## articles/ai-studio/tutorials/copilot-sdk-create-resources.md{#item-552960}

<details>
<summary>Diff</summary>
````diff
@@ -127,7 +127,7 @@ Install `azure-ai-projects`(preview) and `azure-ai-inference` (preview), along w
 
 1. First, create a file named **requirements.txt** in your project folder. Add the following packages to the file:
 
-    :::code language="txt" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/requirements.txt":::
+    :::code language="txt" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/requirements.txt":::
 
 1. Install the required packages:
 
@@ -139,7 +139,7 @@ Install `azure-ai-projects`(preview) and `azure-ai-inference` (preview), along w
 
 Create a folder for your work. Create a file called **config.py** in this folder. This helper script is used in the next two parts of the tutorial series. Add the following code:
 
-:::code language="python" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/config.py":::
+:::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/config.py":::
 
 
 ## Configure environment variables
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソース作成チュートリアルのファイルパス更新"
}
```

### Explanation
この修正は、「Copilot SDKでリソースを作成する」チュートリアルの文書において、サンプルファイルのパスを最新のディレクトリ構造に合わせて更新しました。具体的には、「requirements.txt」ファイルと「config.py」スクリプトへのパスが、以前の「azureai-samples-nov2024」から「azureai-samples-main」に変更されています。

この変更により、ユーザーは最新のサンプルコードと設定ファイルに簡単にアクセスできるようになり、チュートリアルの手順を正確に実行できるようになります。全体として、修正はマイナーですが、ドキュメントの正確性を向上させ、ユーザーが手順をよりスムーズに理解できるようにすることを目的としています。

## articles/ai-studio/tutorials/copilot-sdk-evaluate.md{#item-bb5754}

<details>
<summary>Diff</summary>
````diff
@@ -46,7 +46,7 @@ Use the following evaluation dataset, which contains example questions and expec
 1. Create a file called **chat_eval_data.jsonl** in your **assets** folder.
 1. Paste this dataset into the file:
 
-    :::code language="jsonl" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/assets/chat_eval_data.jsonl":::
+    :::code language="jsonl" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/assets/chat_eval_data.jsonl":::
 
 ## Evaluate with Azure AI evaluators
 
@@ -65,15 +65,15 @@ The script also logs the evaluation results to the cloud project so that you can
 1. Create a file called **evaluate.py** in your main folder.
 1. Add the following code to import the required libraries, create a project client, and configure some settings: 
 
-    :::code language="python" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/evaluate.py" id="imports_and_config":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/evaluate.py" id="imports_and_config":::
 
 1. Add code to create a wrapper function that implements the evaluation interface for query and response evaluation:
 
-    :::code language="python" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/evaluate.py" id="evaluate_wrapper":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/evaluate.py" id="evaluate_wrapper":::
 
 1. Finally, add code to run the evaluation, view the results locally, and gives you a link to the evaluation results in AI Foundry portal:
  
-    :::code language="python" source="~/azureai-samples-nov2024/scenarios/rag/custom-rag-app/evaluate.py" id="run_evaluation":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/evaluate.py" id="run_evaluation":::
 
 ### Configure the evaluation model
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価チュートリアルのファイルパス更新"
}
```

### Explanation
この修正は、「Copilot SDKを使用して評価を行う」チュートリアルの文書において、サンプルファイルのパスを最新のディレクトリ構造に合わせて更新しました。具体的には、「chat_eval_data.jsonl」データセットおよび「evaluate.py」スクリプトへのパスが、以前の「azureai-samples-nov2024」から「azureai-samples-main」に変更されています。

この変更により、ユーザーは最新のサンプルデータとスクリプトに簡単にアクセスできるようになり、評価手順を正確に実行できるようになります。また、手順に関連するコードブロックも同時に更新されることで、ドキュメント全体の整合性が保たれ、より良いユーザーエクスペリエンスが提供されます。全体として、この修正は、ユーザーがチュートリアルをより簡単に理解し、利用できるようにするためのマイナーな更新です。


