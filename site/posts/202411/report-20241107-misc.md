---
date: '2024-11-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6c09135...MicrosoftDocs:8be6320
summary: このコード差分では、AIテンプレートのホスティング情報が更新され、文書内のタイプミスが修正されました。具体的には、「Contoso Chat Retail
  copilot with Azure AI Studio」テンプレートのホスティングが「Azure Container Apps」に変更されました。また、タイプミス「seperate」が「separate」に修正されています。新機能の追加や互換性を壊す変更はなく、主に正確性を高めることを目的としています。これらの変更はユーザーエクスペリエンス向上につながるものです。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6c09135...MicrosoftDocs:8be6320){target="_blank"}

# ハイライト
このコード差分では、AIテンプレートのホスティング情報更新と文書のタイプミス修正という2点の小規模な更新が行われています。具体的には、「Contoso Chat Retail copilot with Azure AI Studio」テンプレートのホスティングサービスが変更されました。また、別の文書では単語のスペルミスが修正されています。

## 新機能
特に新機能の追加はありません。

## 互換性を壊す変更
互換性を壊すような重大な変更はありません。

## その他の更新
- 「Contoso Chat Retail copilot with Azure AI Studio」テンプレートのホスティングが「Azure AI Studio online endpoints」から「Azure Container Apps」に変更。
- 文書内のタイプミスの修正（「seperate」→「separate」）。

# 洞察
今回のドキュメント更新は、主にホスティングプラットフォームの最新情報を取り入れることと、文書の正確性を高めることを目的としています。

AIテンプレートのホスティング情報の変更は、テンプレートが利用するインフラストラクチャがより効率的で柔軟に動作できるようにするための対応です。「Azure Container Apps」への移行によって、ユーザーはコンテナベースのアーキテクチャの利点を活用できるようになり、デプロイメントやスケーラビリティが向上する可能性があります。

別の文書におけるタイプミスの修正は、見過ごされがちではありますが、文書の信頼性を維持するために重要です。特に専門的な資料では、誤字やスペルミスがユーザーの理解を阻害しないようにすることが求められます。

これらの変更は共に、ユーザーエクスペリエンスを向上させ、最新の技術基準に準拠するためのものです。技術ドキュメントは常に進化するものであり、継続的な改善が不可欠です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [ai-template-get-started.md](#item-d71b59) | minor update | AIテンプレートのホスティング情報の更新 | modified | 1 | 1 | 2 | 
| [create-hub.md](#item-9df177) | minor update | 文書内のタイプミスの修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-studio/how-to/develop/ai-template-get-started.md{#item-d71b59}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ Start with our sample applications! Choose the right template for your needs, th
 
 | Template      | App host | Tech stack | Description |
 | ----------- | ----------| ----------- | ------------|
-| [Contoso Chat Retail copilot with Azure AI Studio](https://github.com/Azure-Samples/contoso-chat) | [Azure AI Studio online endpoints](/azure/machine-learning/concept-endpoints-online) | [Azure Cosmos DB](/azure/cosmos-db/index-overview), [Azure Managed Identity](/entra/identity/managed-identities-azure-resources/overview), [Azure OpenAI Service](../../../ai-services/openai/overview.md), [Azure AI Search](/azure/search/search-what-is-azure-search), Bicep  | A retailer conversation agent that can answer questions grounded in your product catalog and customer order history. This template uses a retrieval augmented generation architecture with cutting-edge models for chat completion, chat evaluation, and embeddings. Build, evaluate, and deploy, an end-to-end solution with a single command. | 
+| [Contoso Chat Retail copilot with Azure AI Studio](https://github.com/Azure-Samples/contoso-chat) | [Azure Container Apps](/azure/container-apps/overview) | [Azure Cosmos DB](/azure/cosmos-db/index-overview), [Azure Managed Identity](/entra/identity/managed-identities-azure-resources/overview), [Azure OpenAI Service](../../../ai-services/openai/overview.md), [Azure AI Search](/azure/search/search-what-is-azure-search), Bicep  | A retailer conversation agent that can answer questions grounded in your product catalog and customer order history. This template uses a retrieval augmented generation architecture with cutting-edge models for chat completion, chat evaluation, and embeddings. Build, evaluate, and deploy, an end-to-end solution with a single command. | 
 | [Process Automation: speech to text and summarization with Azure AI Studio](https://github.com/Azure-Samples/summarization-openai-python-prompflow) | [Azure AI Studio online endpoints](/azure/machine-learning/concept-endpoints-online) | [Azure Managed Identity](/entra/identity/managed-identities-azure-resources/overview), [Azure OpenAI Service](../../../ai-services/openai/overview.md), [Azure AI speech to text service](../../../ai-services/speech-service/index-speech-to-text.yml), Bicep  | An app for workers to report issues via text or speech, translating audio to text, summarizing it, and specify the relevant department. | 
 | [Multi-Modal Creative Writing copilot with Dalle](https://github.com/Azure-Samples/agent-openai-python-prompty) | [Azure AI Studio online endpoints](/azure/machine-learning/concept-endpoints-online) | [Azure AI Search](/azure/search/search-what-is-azure-search), [Azure OpenAI Service](../../../ai-services/openai/overview.md), Bicep | demonstrates how to create and work with AI agents. The app takes a topic and instruction input and then calls a research agent, writer agent, and editor agent. |  
 | [Assistant API Analytics Copilot with Python and Azure AI Studio](https://github.com/Azure-Samples/assistant-data-openai-python-promptflow) | [Azure AI Studio online endpoints](/azure/machine-learning/concept-endpoints-online) |  [Azure Managed Identity](/entra/identity/managed-identities-azure-resources/overview), [Azure AI Search](/azure/search/search-what-is-azure-search), [Azure OpenAI Service](../../../ai-services/openai/overview.md), Bicep| A data analytics chatbot based on the Assistants API. The chatbot can answer questions in natural language, and interpret them as queries on an example sales dataset. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIテンプレートのホスティング情報の更新"
}
```

### Explanation
今回の変更では、AIテンプレートに関するドキュメントを更新し、特定のテンプレートのアプリホスティング情報を変更しました。具体的には、「Contoso Chat Retail copilot with Azure AI Studio」というテンプレートのホスティングが「Azure AI Studio online endpoints」から「Azure Container Apps」へと移行されました。この変更により、ユーザーは新しいホスティングサービスの利点を享受できるようになります。また、ドキュメント内で1行が追加され、1行が削除されるという形で、全体の構成がわずかに調整されました。この更新は、最新の技術スタックを反映し、ユーザーにとっての利便性を向上させるものです。

## articles/ai-studio/includes/create-hub.md{#item-9df177}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ To create a hub in [Azure AI Studio](https://ai.azure.com), follow these steps:
     :::image type="content" source="../media/how-to/hubs/hub-new-connect-services.png" alt-text="Screenshot of the dialog to connect services while creating a new hub." lightbox="../media/how-to/hubs/hub-new-connect-services.png":::
 
     > [!NOTE]
-    > If you don't see (new) before the **Resource group** and **Connect Azure AI Services** entries then an existing resource is being used. For the purposes of this tutorial, create a seperate entity via **Create new resource group** and **Create new AI Services**. This will allow you to prevent any unexpected charges by deleting the entities after the tutorial.
+    > If you don't see (new) before the **Resource group** and **Connect Azure AI Services** entries then an existing resource is being used. For the purposes of this tutorial, create a separate entity via **Create new resource group** and **Create new AI Services**. This will allow you to prevent any unexpected charges by deleting the entities after the tutorial.
 
 1. Review the information and select **Create**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書内のタイプミスの修正"
}
```

### Explanation
この変更では、ドキュメント「create-hub.md」において、文中のタイプミスを修正しました。具体的には、「separate」という単語の綴りが「seperate」と誤って記載されていた部分を訂正しました。この修正は、ユーザーに対して正確で明確な情報を提供するための重要な要素であり、文書の品質向上に寄与しています。全体として、影響は限定的ですが、正確な言葉遣いを維持することで、利用者の信頼性を確保することが目的です。


