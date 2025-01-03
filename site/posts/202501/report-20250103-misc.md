---
date: '2025-01-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:14202e8...MicrosoftDocs:2f26af9
summary: この報告書では、「AIテンプレートの開始方法」というドキュメントが最新の情報に基づいて更新され、内容と日付が修正されたことが述べられています。また、「Copilot
  SDK」の評価に関するチュートリアルのタイトルも変更されました。新機能として、Azure AIサービスを統合する方法についての詳細が追加され、特に破壊的な変更はありません。日付は2024年から2025年に更新され、チュートリアルタイトルの変更により内容がより具体的になりました。これにより、ユーザーは正確な情報にアクセスしやすくなり、AIスタジオでの開発作業が効率化されます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:14202e8...MicrosoftDocs:2f26af9){target="_blank"}

<format>
# Highlights
「AIテンプレートの開始方法」のドキュメントが最新の情報を反映するために更新され、日付と内容の一部が修正されました。また、「Copilot SDK」の評価に関するチュートリアルのタイトルも修正されています。

## New features
- 「AIテンプレートの開始方法」ドキュメントで、Azure AIサービスを統合する方法に関する詳細が追加。

## Breaking changes
- 破壊的な変更は特にありません。

## Other updates
- 日付の更新（2024年から2025年へ）。
- チュートリアルタイトルの修正で、内容がより具体的に。

# Insights
今回の更新は、主に二つのドキュメントのマイナー修正を伴っています。まず「AIテンプレートの開始方法」では、AIスタジオでのテンプレート情報を最新にするための日付の変更と、テンプレートの使用を容易にするための手順改善が行われています。具体的な変更としては、Azure AIの基本的なプロンプトベースの統合方法を詳細に説明し、重要な設定を強調しました。これにより、ユーザーがアプリケーション開発の際に時間を節約し、スムーズに作業を進められるようにしています。

「Copilot SDK」の評価チュートリアルのタイトル変更については、文書の焦点を「評価」に絞ることで、チュートリアルの内容がより明確にユーザーに伝わることを目指しています。この変更により、ユーザーがドキュメントを利用して何を学ぶべきかを把握しやすくなり、学習体験の向上につながります。

全体として、これらの更新は、ユーザーがより簡単に正確な情報にアクセスでき、AIスタジオを活用した開発作業を効率化するためのものです。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [ai-template-get-started.md](#item-d71b59) | minor update | AIテンプレートの開始方法の更新 | modified | 5 | 2 | 7 | 
| [copilot-sdk-evaluate.md](#item-bb5754) | minor update | チャットアプリの評価に関するタイトルの修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-studio/how-to/develop/ai-template-get-started.md{#item-d71b59}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-studio
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 01/02/2025
 ms.reviewer: dantaylo
 ms.author: sgilley
 author: sdgilley
@@ -30,13 +30,16 @@ Start with our sample applications! Choose the right template for your needs, th
 
 | Template      | App host | Tech stack | Description |
 | ----------- | ----------| ----------- | ------------|
-| [Azure AI Basic Template with Python](https://github.com/azure-samples/azureai-basic-python) | [Azure AI Foundry online endpoints](/azure/machine-learning/concept-endpoints-online) | [Azure Managed Identity](/entra/identity/managed-identities-azure-resources/overview), [Azure OpenAI Service](../../../ai-services/openai/overview.md), Bicep | The app serves as a straightforward example of integrating Azure AI Services within a basic prompt-based application. This template walks you through building a simple chat app that utilizes models and prompts. It also covers setting up the necessary infrastructure for the app, including creating an Azure AI Foundry Hub, configuring projects, and provisioning essential resources such as Azure AI Service, Azure Container Apps, Cognitive Search, and more. <br>You can build, deploy, and test it with a single command.  |
+| [Azure AI Basic Template with Python](https://github.com/azure-samples/azureai-basic-python) | [Azure AI Foundry online endpoints](/azure/machine-learning/concept-endpoints-online) | [Azure Managed Identity](/entra/identity/managed-identities-azure-resources/overview), [Azure OpenAI Service](../../../ai-services/openai/overview.md), Bicep | The app serves as a straightforward example of integrating Azure AI Services within a basic prompt-based application. This template walks you through building a simple chat app that utilizes models and prompts. The template also covers setting up the necessary infrastructure for the app, including creating an Azure AI Foundry Hub, configuring projects, and provisioning essential resources such as Azure AI Service, Azure Container Apps, Cognitive Search, and more. <br>You can build, deploy, and test it with a single command.  |
 | [Contoso Chat Retail copilot with Azure AI Foundry](https://github.com/Azure-Samples/contoso-chat) | [Azure Container Apps](/azure/container-apps/overview) | [Azure Cosmos DB](/azure/cosmos-db/index-overview), [Azure Managed Identity](/entra/identity/managed-identities-azure-resources/overview), [Azure OpenAI Service](../../../ai-services/openai/overview.md), [Azure AI Search](/azure/search/search-what-is-azure-search), Bicep  | A retailer conversation agent that can answer questions grounded in your product catalog and customer order history. This template uses a retrieval augmented generation architecture with cutting-edge models for chat completion, chat evaluation, and embeddings. Build, evaluate, and deploy, an end-to-end solution with a single command. | 
 | [Process Automation: speech to text and summarization with Azure AI Foundry](https://github.com/Azure-Samples/summarization-openai-python-prompflow) | [Azure AI Foundry online endpoints](/azure/machine-learning/concept-endpoints-online) | [Azure Managed Identity](/entra/identity/managed-identities-azure-resources/overview), [Azure OpenAI Service](../../../ai-services/openai/overview.md), [Azure AI speech to text service](../../../ai-services/speech-service/index-speech-to-text.yml), Bicep  | An app for workers to report issues via text or speech, translating audio to text, summarizing it, and specify the relevant department. | 
 | [Multi-Modal Creative Writing copilot with Dalle](https://github.com/Azure-Samples/agent-openai-python-prompty) | [Azure AI Foundry online endpoints](/azure/machine-learning/concept-endpoints-online) | [Azure AI Search](/azure/search/search-what-is-azure-search), [Azure OpenAI Service](../../../ai-services/openai/overview.md), Bicep | demonstrates how to create and work with AI agents. The app takes a topic and instruction input and then calls a research agent, writer agent, and editor agent. |  
 | [Assistant API Analytics Copilot with Python and Azure AI Foundry](https://github.com/Azure-Samples/assistant-data-openai-python-promptflow) | [Azure AI Foundry online endpoints](/azure/machine-learning/concept-endpoints-online) |  [Azure Managed Identity](/entra/identity/managed-identities-azure-resources/overview), [Azure AI Search](/azure/search/search-what-is-azure-search), [Azure OpenAI Service](../../../ai-services/openai/overview.md), Bicep| A data analytics chatbot based on the Assistants API. The chatbot can answer questions in natural language, and interpret them as queries on an example sales dataset. |
+<!-- remove for now
 | Function Calling with Prompty, LangChain, and Pinecone | [Azure AI Foundry online endpoints](/azure/machine-learning/concept-endpoints-online) | [Azure Managed Identity](/entra/identity/managed-identities-azure-resources/overview), [Azure OpenAI Service](../../../ai-services/openai/overview.md), [LangChain](https://python.langchain.com/v0.1/docs/get_started/introduction), [Pinecone](https://www.pinecone.io/), Bicep  | Utilize the new Prompty tool, LangChain, and Pinecone to build a large language model (LLM) search agent. This agent with Retrieval-Augmented Generation (RAG) technology is capable of answering user questions based on the provided data by integrating real-time information retrieval with generative responses. | 
 | Function Calling with Prompty, LangChain, and Elastic Search | [Azure AI Foundry online endpoints](/azure/machine-learning/concept-endpoints-online) | [Azure Managed Identity](/entra/identity/managed-identities-azure-resources/overview), [Azure OpenAI Service](../../../ai-services/openai/overview.md), [Elastic Search](https://www.elastic.co/elasticsearch), [LangChain](https://python.langchain.com/v0.1/docs/get_started/introduction) , Bicep  | Utilize the new Prompty tool, LangChain, and Elasticsearch to build a large language model (LLM) search agent. This agent with Retrieval-Augmented Generation (RAG) technology is capable of answering user questions based on the provided data by integrating real-time information retrieval with generative responses |
+-->
+
 
 ### [C#](#tab/csharp)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIテンプレートの開始方法の更新"
}
```

### Explanation
この変更は、AIスタジオ向けの「AIテンプレートの開始方法」を説明するドキュメントのマイナーアップデートを反映しています。具体的には、ドキュメント内の日付が「2024年5月21日」から「2025年1月2日」に変更されています。この変更を通じて、提供されるテンプレートに関連する情報が最新のリファレンスを反映していることが求められます。

さらに、既存のテンプレートの説明がわずかに修正され、テキストの一部が有益な情報を強調するために改良されました。具体的には、アプリがAzure AIサービスを基本的なプロンプトベースのアプリケーションに統合する方法に関する詳細が追加され、重要なリソースやインフラの設定を行う手順がより明確になっています。この修正は、ユーザーがテンプレートを利用しやすくするためのものであり、アプリの構築、デプロイ、およびテストを一つのコマンドで実行できるという利点も強調されています。

## articles/ai-studio/tutorials/copilot-sdk-evaluate.md{#item-bb5754}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: "Part 3: Evaluate and deploy chat app with the Azure AI SDK"
+title: "Part 3: Evaluate a chat app with the Azure AI SDK"
 titleSuffix: Azure AI Foundry
 description: Evaluate and deploy a custom chat app with the prompt flow SDK. This tutorial is part 3 of a 3-part tutorial series.
 manager: scottpolly
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットアプリの評価に関するタイトルの修正"
}
```

### Explanation
この変更は、「AIスタジオ」における「Copilot SDK」の評価に関するチュートリアルドキュメントのタイトルを修正するためのマイナーアップデートです。具体的には、タイトルが「Part 3: Evaluate and deploy chat app with the Azure AI SDK」から「Part 3: Evaluate a chat app with the Azure AI SDK」に変更されました。

この変更により、「チャットアプリの評価とデプロイ」という内容から、「チャットアプリの評価」に焦点を絞った表現に更新されています。この修正は、ドキュメントの内容をより正確に反映するものであり、ユーザーがチュートリアルの目的を理解しやすくすることを目的としています。全体として、この修正は文書の明確さを向上させるためのものであり、ユーザーエクスペリエンスに寄与します。


