---
date: '2026-02-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dfa2fda...MicrosoftDocs:675261b
summary: "この差分は、AzureのLanguageサービスに関するマニュアルやクイックスタートガイドの更新を示しています。主な変更点には、新機能のプレビュー情報や手順の明確化、説明文の改訂が含まれています。特に、Foundry\
  \ Toolsとマルチターン会話理解モデルに関する新情報が追加されており、破壊的な変更はありません。 \n\nまた、リンクの更新や説明文・タイトルの微調整、表形式の情報提供が進められ、ユーザーが理解しやすくなっています。手順に関する詳細も強化され、安全面の情報も充実しています。全体として、これらの改善はAzure\
  \ Languageサービスのドキュメントのユーザビリティを向上させ、幅広いユーザーにとって使いやすくすることを目的としています。"
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dfa2fda...MicrosoftDocs:675261b){target="_blank"}

<format>
# ハイライト
この差分は、Azureの「Languageサービス」に関する複数のマニュアルおよびクイックスタートガイドの小規模な更新を示しており、新機能の導入や既存ドキュメントの改善が行われています。新機能のプレビュー情報の追加や、説明文の改訂、手順の明確化が主な変更点です。

## 新機能
特に言及されているのは 「Foundry Tools」および「マルチターン会話理解（CLU）モデル」の更新で、新たにプレビュー機能や新しいエージェントの情報が追加されました。

## 破壊的な変更
破壊的な変更は含まれていませんでした。

## その他の更新
- 各種リンクの最新化。
- 説明文やタイトルの微調整。
- ユーザーが理解しやすいように表形式の情報提供。
- クイックスタートガイドやマニュアルの手順詳細化。

# インサイト
Azure Languageサービスに関するドキュメント更新では、ユーザビリティと情報提供の正確性を高めるための一連の改善が図られています。まず、タイトルと説明文の変更が目立ちます。具体的なタイトルへの変更は、ユーザーがドキュメントの対象や内容を迅速に理解できるようにするためのものです。また、新機能やプレビュー機能に関する注釈やテーブルが追加され、各項目が持つ機能を整理することでユーザーが適切な判断をしやすくしています。

手順に関する情報も、特にAzure Developer CLIを使用したエージェントの設定手順が明確になっています。APIキー管理の重要性や接続設定に関する情報が強化され、セキュリティ面の注意喚起も充実されています。

さらに、リンクの更新によって、ユーザーは最新の情報にアクセスしやすくなり、情報の透明性が向上しています。Azure Languageサービスのプレビューエージェントに関する説明が更新されて、ユーザーが新しい機能を試せるようにサポートされています。

全体として、これらの変更は情報の整理と見やすさを向上させ、ユーザーがAzure Languageサービスを利用する際の体験を向上させることを目的としています。マニュアルや手順がより親しみやすくなり、初心者から熟練ユーザーまで幅広い層がサービスを活用しやすくなっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [foundry-tools-agents.md](#item-7b932c) | minor update | Azure Language in Foundry Toolsの更新 | modified | 95 | 65 | 160 | 
| [quickstart-multi-turn-conversations.md](#item-9a3011) | minor update | マルチターン会話理解のクイックスタート更新 | modified | 14 | 12 | 26 | 
| [azure-ai-foundry.md](#item-41c23c) | minor update | 言語検出のクイックスタート更新 | modified | 62 | 59 | 121 | 
| [quickstart.md](#item-636553) | minor update | テキストの言語検出に関するクイックスタート更新 | modified | 12 | 6 | 18 | 
| [overview.md](#item-f138b4) | minor update | Azure Languageサービスの概要更新 | modified | 3 | 3 | 6 | 
| [azure-ai-foundry.md](#item-ff89fc) | minor update | 個人を特定できる情報（PII）に関するクイックスタートの更新 | modified | 57 | 46 | 103 | 
| [quickstart.md](#item-94affd) | minor update | 個人を特定できる情報（PII）クイックスタートガイドの更新 | modified | 11 | 7 | 18 | 
| [whats-new.md](#item-69b272) | minor update | Azure Languageの新機能の更新 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/ai-services/language-service/concepts/foundry-tools-agents.md{#item-7b932c}

<details>
<summary>Diff</summary>
````diff
@@ -1,45 +1,56 @@
 ---
-title: Azure Language tools and agents
+title: Azure Language in Foundry Tools - tools and agents
 titleSuffix: Foundry Tools
-description: Learn how Azure Language integrates with Foundry Tools, including Model Context Protocol (MCP) server endpoints, intent routing agents, and exact question answering agents.
+description: Learn how Azure Language in Foundry Tools integrates with Microsoft Foundry, including Model Context Protocol (MCP) server endpoints, intent routing agents, and exact question answering agents.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: concept-article
-ms.date: 01/21/2026
+ms.date: 02/06/2026
 ms.author: lajanuar
 ms.custom: pilot-ai-workflow-jan-2026
 ai-usage: ai-assisted
 ---
 
 # Azure Language tools and agents
 
-Azure Language integrates with Foundry Tools to provide agents and endpoints for building conversational applications. These tools combine Azure Language natural language processing capabilities with Microsoft Foundry agent experiences.
+Azure Language in Foundry Tools provides agents and endpoints for building conversational applications. These tools combine Azure Language natural language processing capabilities with Microsoft Foundry agent experiences.
 
 This article introduces the Azure Language integrations that are available in Foundry Tools:
 
-- An Azure Language Model Context Protocol (MCP) server endpoint.
-- An intent routing agent that combines Conversational Language Understanding (CLU) and Custom Question Answering (CQA).
-- An exact question answering agent that uses CQA to return curated, deterministic responses.
+* An Azure Language Model Context Protocol (MCP) server endpoint.
+* An intent routing agent that combines Conversational Language Understanding (CLU) and Custom Question Answering (CQA).
+* An exact question answering agent that uses CQA to return curated, deterministic responses.
+
+> [!IMPORTANT]
+> The Azure Language tools and agents described in this article are currently in preview. See the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) for legal terms that apply.
+
+The following table summarizes each integration to help you choose the right one for your scenario:
+
+| Feature | Best for | Key technology | Setup complexity |
+|---------|----------|---------------|------------------|
+| **MCP server** | Adding Azure Language NLP capabilities to any MCP-compatible agent | Model Context Protocol | Low — configure a connection and endpoint |
+| **Intent routing agent** | Multi-intent conversations that need deterministic routing with fallback | CLU + CQA | Medium — deploy CLU and CQA projects |
+| **Exact question answering agent** | FAQ-style scenarios that require consistent, verbatim answers | CQA | Low — deploy a CQA project, no code required |
 
 ## Key concepts
 
-- **Agent**: An AI experience that can interpret user input and choose actions or tools to complete tasks.
-- **Tool**: A capability an agent can call to retrieve information or perform actions.
-- **Model Context Protocol (MCP)**: An open protocol for exposing tools and contextual data to agents and large language models.
-- **Connected resources and connections**: Configuration in Microsoft Foundry that lets an agent access external services (including credentials).
+* **Agent**: An AI experience that can interpret user input and choose actions or tools to complete tasks.
+* **Tool**: A capability an agent can call to retrieve information or perform actions.
+* **Model Context Protocol (MCP)**: An open protocol for exposing tools and contextual data to agents and large language models.
+* **Connected resources and connections**: Configuration in Microsoft Foundry that lets an agent access external services (including credentials).
 
-## Azure Language MCP server 🆕
+## Azure Language MCP server (preview)
 
-The Azure Language MCP server in the [Microsoft Foundry portal](https://ai.azure.com/) connects agents to Azure Language services through the Model Context Protocol (MCP). This integration helps you build conversational applications that can call Azure Language capabilities as tools.
+The Azure Language MCP server in the [Foundry portal](https://ai.azure.com/) connects agents to Azure Language services through the Model Context Protocol (MCP). This integration helps you build conversational applications that can call Azure Language capabilities as tools.
 
 The MCP server exposes Azure Language features through an agent-friendly endpoint that supports real-time workflows.
 
 ### Core capabilities
 
 * **Language processing**: Access to Azure Language natural language processing (NLP) capabilities, including [Named Entity Recognition](../named-entity-recognition/overview.md), [Text Analytics for health](../text-analytics-for-health/overview.md), [Conversational Language Understanding](../conversational-language-understanding/overview.md), [Custom Question Answering](../question-answering/overview.md), [Language Detection](../language-detection/overview.md), [Sentiment Analysis](../sentiment-opinion-mining/overview.md), [Summarization](../summarization/overview.md), [Key Phrase Extraction](../key-phrase-extraction/overview.md), and [PII redaction](../personally-identifiable-information/overview.md).
 
-* **Local deployment**: Azure Language also provides a local MCP server that you can host in your own environment. For setup guidance, see the Language MCP Server quickstart in the [Azure Language samples repository](https://github.com/Azure-Samples/ai-language-samples).
+* **Local deployment**: Azure Language also provides a local MCP server that you can host in your own environment. For setup guidance, see the Azure Language MCP Server quickstart in the [Azure Language samples repository](https://github.com/Azure-Samples/ai-language-samples).
 
 * **Remote MCP server endpoint**
 
@@ -51,129 +62,148 @@ The MCP server exposes Azure Language features through an agent-friendly endpoin
 
 To use the Azure Language MCP server with agents:
 
-- Create a Microsoft Foundry resource and project.
-- Make sure you have an Azure Language resource.
-- Configure a connection in your Foundry project so the agent can authenticate to the Azure Language endpoint.
+* An Azure subscription. [Create one for free](https://azure.microsoft.com/free/cognitive-services).
+* A Foundry resource and project. You need Contributor or Owner role on the resource group.
+* An Azure Language resource.
+* A configured connection in your Foundry project so the agent can authenticate to the Azure Language endpoint.
 
 For connection setup details, see [Create a connection](../../../ai-foundry/how-to/connections-add.md?view=foundry&preserve-view=true).
 
 ### Security considerations
 
 If you authenticate with API keys, treat keys as secrets:
 
-- Store keys in a secure secret store and rotate them regularly.
-- Avoid embedding keys directly in source code, scripts, or documentation.
+* Store keys in a secure secret store and rotate them regularly.
+* Avoid embedding keys directly in source code, scripts, or documentation.
 
 ### Limitations
 
-Some Microsoft Foundry configurations restrict which MCP servers you can use. For example, network-secured Foundry projects can require publicly accessible MCP servers. For details, see [Connect to Model Context Protocol servers (preview)](../../../ai-foundry/default/agents/how-to/tools/model-context-protocol.md).
+Some Foundry configurations restrict which MCP servers you can use. For example, network-secured Foundry projects can require publicly accessible MCP servers. For details, see [Connect to Model Context Protocol servers (preview)](../../../ai-foundry/default/agents/how-to/tools/model-context-protocol.md).
 
-## Azure Language intent routing agent 🆕
+## Azure Language intent routing agent (preview)
 
-The intent routing agent in the [Microsoft Foundry portal](https://ai.azure.com/) manages conversation flows by combining intent classification with answer delivery. It helps you route user questions to curated answers when possible, and fall back to other approaches when needed.
+The intent routing agent in the [Foundry portal](https://ai.azure.com/) manages conversation flows by combining intent classification with answer delivery. It helps you route user questions to curated answers when possible, and fall back to other approaches when needed.
 
 The agent, which is built on Azure Language natural language understanding capabilities, processes user input through layers. The system analyzes messages to understand intentions, then you can implement logic to route requests through appropriate channels based on confidence levels.
 
 The agent prioritizes deterministic behavior, making it suitable for enterprise applications where consistency is important.
 
 ### Prerequisites
 
-Before setting up the Intent Routing agent, ensure you have the following resources and configurations in place:
+Before you set up the intent routing agent, make sure you have the following resources and configurations in place:
+
+* **Azure subscription**: [Create one for free](https://azure.microsoft.com/free/cognitive-services). You need Contributor or Owner role on the resource group.
 
 * **Foundry resource**: You need an active Foundry resource to host your agent.
 
 * **Project resources**: Create your CLU and CQA projects using one of the following resource types:
   * Foundry resource.
   * AI hub resource.
-  * Azure Language in Foundry Tools resource.
+  * Azure Language resource.
 
 * **Project deployments**: Deploy the following required projects:
 
-  * Custom Question Answering (CQA) deployment - see [CQA Overview](../question-answering/overview.md).
-  * Conversational Language Understanding (CLU) deployment - see [CLU Overview](../conversational-language-understanding/overview.md).
+  * Custom Question Answering (CQA) deployment. See [CQA Overview](../question-answering/overview.md).
+  * Conversational Language Understanding (CLU) deployment. See [CLU Overview](../conversational-language-understanding/overview.md).
 
-* **Custom connection setup**: Configure a custom connection between your agent project and the Language resources:
-  * In your agent project management center, select **Custom keys** when you add the custom connection in **Connected resources**.
-  * Add a key-value pair with `Ocp-Apim-Subscription-Key` as the key name and your resource key as the value.
-  * For Foundry and AI hub resources, find the resource key in the resource overview page in the Microsoft Foundry portal management center.
-  * For any resource type, you can also find the key in the Azure portal.
-  * For detailed connection instructions, see [Create a connection](../../../ai-foundry/how-to/connections-add.md?view=foundry&preserve-view=true).
+* **Custom connection setup**: Configure a custom connection between your agent project and the Azure Language resources. For the full connection setup steps, see [Set up a custom connection](#set-up-a-custom-connection).
 
 ### Key capabilities
 
 * **Intent classification**: [**Conversational Language Understanding (CLU)**](../conversational-language-understanding/overview.md) analyzes user utterances to identify intents and extract entities. The system recognizes conversation patterns and understands context.
 
 * **Response delivery**: [**Custom Question Answering (CQA)**](../question-answering/overview.md) provides responses drawn from curated knowledge sources. This capability ensures users receive consistent information that aligns with organizational standards.
 
-* **Knowledge management**: Users can manage their intent definitions in CLU projects and manage pairs of question-answers in CQA projects. This capability provides oversight for the agent's knowledge base and response capabilities.
+* **Knowledge management**: You can manage your intent definitions in CLU projects and manage pairs of question-answers in CQA projects. This capability provides oversight for the agent's knowledge base and response capabilities.
 
-* **Fallback processing**: Users can easily add retrieval-augmented generation (RAG) to the agent to handle edge cases and uncommon questions by using approved knowledge sources.
+* **Fallback processing**: You can add retrieval-augmented generation (RAG) to the agent to handle edge cases and uncommon questions by using approved knowledge sources.
 
-* **Download the intent routing template code with Azure Developer CLI (`azd`)**
+### Get the template
 
-  ```bash
-        azd ai agent init -m azureml://registries/azureml-staging/agentmanifests/intent_routing_agent/versions/1
-    ```
+Download the intent routing template code with Azure Developer CLI (`azd`):
 
-## Azure Language exact question answering agent 🆕
+```bash
+azd ai agent init -m azureml://registries/azureml-staging/agentmanifests/intent_routing_agent/versions/1
+```
 
-The Exact Question Answering agent in [**Foundry**](https://ai.azure.com/) delivers responses to frequently asked business questions through a fully managed, no-code solution. This agent provides consistent answers to queries while maintaining governance and quality control.
+After the command completes, the template scaffolds a project directory with configuration files and sample code.
 
-The agent combines Azure AI Agent Service capabilities with [**Custom Question Answering**](../question-answering/overview.md) technology. This integration creates a solution with minimal setup while delivering performance and oversight.
+## Azure Language Exact Question Answering agent (preview)
+
+The **Exact Question Answering** agent in the [Foundry portal](https://ai.azure.com/) delivers responses to frequently asked business questions through a fully managed, no-code solution. This agent provides consistent answers to queries while maintaining governance and quality control.
+
+The agent combines Foundry Agent Service capabilities with [**Custom Question Answering**](../question-answering/overview.md) technology. This integration creates a solution with minimal setup while delivering performance and oversight.
 
 The agent works well for scenarios where answer accuracy is important, such as customer service, help desk operations, or compliance information delivery.
 
-In addition to creating the agent from the Exact Question Answering Agent template in Agent Catalog, users can also create the agent directly from their CQA project in the Foundry portal. More details can be found in [Create and deploy a CQA agent](../question-answering/how-to/deploy-agent.md).
+In addition to creating the agent from the exact question answering agent template in Agent Catalog, you can also create the agent directly from your CQA project in the Foundry portal. For more information, see [Create and deploy a CQA agent](../question-answering/how-to/deploy-agent.md).
 
 ### Prerequisites
 
-Before setting up the Exact Question Answering agent, ensure you have the following resources and configurations in place:
+Before you set up the exact question answering agent, make sure you have the following resources and configurations in place:
+
+* **Azure subscription**: [Create one for free](https://azure.microsoft.com/free/cognitive-services). You need Contributor or Owner role on the resource group.
 
 * **Foundry resource**: You need an active Foundry resource to host your agent.
 
 * **Project resources**: Create your CQA project using one of the following resource types:
   * Foundry resource.
   * AI hub resource.
-  * Language resource.
+  * Azure Language resource.
 
 * **Project deployment**: Deploy the following required project:
 
-  * Custom Question Answering (CQA) deployment - see [CQA Overview](../question-answering/overview.md).
+  * Custom Question Answering (CQA) deployment. See [CQA Overview](../question-answering/overview.md).
 
+* **Custom connection setup**: Configure a custom connection between your agent project and the Azure Language resources. For the full connection setup steps, see [Set up a custom connection](#set-up-a-custom-connection).
 
-* **Custom connection setup**: Configure a custom connection between your agent project and the Language resources:
-  * In your agent project management center, select **Custom keys** when you add the custom connection in **Connected resources**.
-  * Add a key-value pair with `Ocp-Apim-Subscription-Key` as the key name and your resource key as the value.
-  * For Foundry and AI hub resources, find the resource key in the resource overview page in the Microsoft Foundry portal management center.
-  * For any resource type, you can also find the key in the Azure portal.
-  * For detailed connection instructions, see [Create a connection](../../../ai-foundry/how-to/connections-add.md?view=foundry&preserve-view=true).
+### Get the template
 
-* **Download the exact question answering template code with Azure Developer CLI (`azd`)**
+Download the exact question answering template code with Azure Developer CLI (`azd`):
 
-    ```bash
-        azd ai agent init -m azureml://registries/azureml-staging/agentmanifests/exact_question_answering_agent/versions/1
-    ```
+```bash
+azd ai agent init -m azureml://registries/azureml-staging/agentmanifests/exact_question_answering_agent/versions/1
+```
+
+After the command completes, the template scaffolds a project directory with configuration files and sample code.
 
 ### Key capabilities
 
-* **Azure integration**: The agent integrates Azure AI Agent Service with [**Custom Question Answering**](../question-answering/overview.md) capabilities within Azure Language services. This integration eliminates complex configuration requirements and provides access to enterprise security and monitoring features.
+* **Agent Service integration**: The agent integrates Agent Service with [**Custom Question Answering**](../question-answering/overview.md) capabilities within Azure Language services. This integration eliminates complex configuration requirements and provides access to enterprise security and monitoring features.
 
-* **No-code deployment**: Organizations can deploy and configure the agent through Foundry's visual interface without writing custom code. This approach enables business stakeholders to participate in knowledge base creation and maintenance.
+* **No-code deployment**: Organizations can deploy and configure the agent through the Foundry visual interface without writing custom code. This approach enables business stakeholders to participate in knowledge base creation and maintenance.
 
-* **Knowledge management**: Users can manage question-answer pairs in CQA projects, providing control over the agent's knowledge base and ensuring response accuracy.
+* **Knowledge management**: You can manage question-answer pairs in CQA projects, providing control over the agent's knowledge base and ensuring response accuracy.
 
 * **Deterministic answering**: The agent returns exact verbatim responses as defined in the CQA project answers, ensuring consistent and controllable responses to questions.
 
-* **Fallback processing**: Users can easily add retrieval-augmented generation (RAG) to handle queries outside the predefined knowledge base by using approved organizational content sources.
+* **Fallback processing**: You can add retrieval-augmented generation (RAG) to handle queries outside the predefined knowledge base by using approved organizational content sources.
+
+## Set up a custom connection
+
+Both the intent routing agent and the exact question answering agent require a custom connection between your agent project and Azure Language resources. Follow these steps to configure the connection:
+
+1. In your agent project management center, select **Connected resources**.
+1. Select **Custom keys** when you add the custom connection.
+1. Add a key-value pair with `Ocp-Apim-Subscription-Key` as the key name and your resource key as the value.
+1. For Foundry and AI hub resources, find the resource key on the resource overview page in the Foundry portal management center.
+1. For any resource type, you can also find the key in the Azure portal.
+
+For detailed connection instructions, see [Create a connection](../../../ai-foundry/how-to/connections-add.md?view=foundry&preserve-view=true).
+
+To verify the connection is working, send a test message to the agent. If the agent returns a response from your CQA knowledge base, the connection is configured correctly.
 
 ## Troubleshooting
 
-- **The agent returns authentication errors**: Confirm the connection uses the `Ocp-Apim-Subscription-Key` header name and that the value matches your Azure Language resource key.
-- **The agent doesn't use CLU or CQA as expected**: Confirm your CLU and CQA projects are deployed and that the agent is connected to the correct resources.
-- **Responses are low confidence or irrelevant**: Review CLU intent training data and CQA question-answer pairs, then redeploy your projects.
+* **The agent returns authentication errors**: Confirm the connection uses the `Ocp-Apim-Subscription-Key` header name and that the value matches your Azure Language resource key.
+* **The agent doesn't use CLU or CQA as expected**: Confirm your CLU and CQA projects are deployed and that the agent is connected to the correct resources.
+* **Responses are low confidence or irrelevant**: Review CLU intent training data and CQA question-answer pairs, then redeploy your projects.
+* **The MCP server returns a 404 or connection error**: Verify the endpoint URL uses the correct Foundry resource name and API version. Confirm the Azure Language resource is in a supported region.
+* **The `azd ai agent init` command fails**: Make sure you have the latest version of the [Azure Developer CLI](/azure/developer/azure-developer-cli/install-azd) installed and that you're signed in with `azd auth login`.
 
 ## Related content
 
-- [Configure Azure resources for Foundry](configure-azure-resources.md)
-- [Connect to Model Context Protocol servers (preview)](../../../ai-foundry/default/agents/how-to/tools/model-context-protocol.md)
-- [Discover tools in the Foundry Tools (preview)](../../../ai-foundry/default/agents/concepts/tool-catalog.md)
+* [Configure Azure resources for Foundry](configure-azure-resources.md)
+* [Create and deploy a CQA agent](../question-answering/how-to/deploy-agent.md)
+* [Connect to Model Context Protocol servers (preview)](../../../ai-foundry/default/agents/how-to/tools/model-context-protocol.md)
+
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Language in Foundry Toolsの更新"
}
```

### Explanation
このコードの差分は、Azure Language in Foundry Toolsに関連するドキュメントの更新を示しています。主な変更点には、記事のタイトルや説明の修正、新機能のプレビュー情報追加、リスト形式の変更、テーブルの追加などがあります。

- **タイトルと説明の変更**: 以前のタイトル「Azure Language tools and agents」から「Azure Language in Foundry Tools - tools and agents」に変更され、より具体的な説明が追加されました。この変更により、ユーザーは文章が扱う内容を一目で理解しやすくなっています。

- **概要の改善**: 記事内の情報が整理され、新しい情報が追加されました。具体的には、Azure Languageの統合に関するセクションが強化され、それぞれの機能の詳細が簡潔に示されています。

- **注釈や注意喚起の追加**: 重要な情報を強調するために、プレビュー中の機能についての注釈が新たに加えられています。

- **機能のテーブル追加**: 各統合機能に関する要約を提供するテーブルが新設され、ユーザーが適切な選択をしやすくなっています。

- **コーディング手順の明確化**: Azure Developer CLIを使用したエージェントの依存関係のダウンロード手順も更新され、認識しやすい形式で示されています。

- **セキュリティおよび接続に関する注意点**: APIキーの取り扱いや接続の設定に関する重要な注意点が強調され、トラブルシューティングセクションも詳細に更新されました。

これらの更新は、ユーザーがAzure Language in Foundry Toolsを利用する際の理解を深め、全体的なユーザー体験を向上させることを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/quickstart-multi-turn-conversations.md{#item-9a3011}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,12 @@
 ---
 title: "Quickstart: Multi-turn conversational language understanding (CLU) models with entity slot filling"
 titleSuffix: Foundry Tools
-description: Create a multi-turn conversational language understanding (CLU) model with entity slot filling in Foundry (classic).
+description: Create a multi-turn conversational language understanding (CLU) model with entity slot filling in Microsoft Foundry (classic).
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 01/21/2026
+ms.date: 02/06/2026
 ms.author: lajanuar
 ai-usage: ai-assisted
 ms.custom: 
@@ -18,6 +18,8 @@ ms.custom:
 
 In this article, get started building a CLU model that uses entity slot filling to enable multi-turn conversations. This approach allows your model to collect information progressively across multiple conversation turns, rather than requiring users to provide all details in a single interaction to complete tasks naturally and efficiently.
 
+If you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
+
 > [!NOTE]
 > Multi-turn entity slot filling is available only in Microsoft Foundry (classic). This quickstart uses the classic portal at [https://ai.azure.com/](https://ai.azure.com/). For more information about the portals, see [What is Microsoft Foundry?](../../../../ai-foundry/what-is-foundry.md).
 
@@ -88,13 +90,13 @@ Deploy an OpenAI model to provide the foundational intelligence and advanced rea
 
 1. Select **Models + endpoints** from the **My assets** section of the navigation menu.
 
-   :::image type="content" source="../media/models-endpoints.png" alt-text="Screenshot of the deploy model button menu in Foundry.":::
+   :::image type="content" source="../media/models-endpoints.png" alt-text="Screenshot of the Models and endpoints page in Foundry.":::
 
 1. From the main window, select **+ Deploy model**.
 
 1. Select **Deploy base model** from the dropdown menu.
 
-   :::image type="content" source="../media/deploy-model-button.png" alt-text="Screenshot of the connected resources menu selection in Foundry.":::
+   :::image type="content" source="../media/deploy-model-button.png" alt-text="Screenshot of the Deploy base model dropdown menu in Foundry.":::
 
 1. In the **Select a model** window, choose a model. The **gpt-4** base model is recommended for this project.
 
@@ -146,7 +148,7 @@ In this section, you create a travel agent model and deploy it using Quick Deplo
    * **Language** - English is set as the default and should already appear in the field.
    * **Description** - Optionally provide a description or leave this field empty.
 
-1. Select **Create**. The creation operation may take a few minutes to complete.
+1. Select **Create**. The creation operation might take a few minutes to complete. After it finishes, your new CLU project appears in the **AI Service fine-tuning** list.
 
 ### Add your intents
 
@@ -271,7 +273,7 @@ Now that all entities have associations, you can proceed with Quick Deploy using
 
     :::image type="content" source="../media/multi-turn/details.png" alt-text="Screenshot of the Details response window.":::
 
-You successfully created a multi-turn CLU model with entity slot filling capabilities to collect required information across multiple dialog turns.
+You successfully created a multi-turn CLU model with entity slot filling capabilities to collect required information across multiple dialog turns. To learn more about how CLU handles entity slot filling across conversation turns, see [Multi-turn conversations](../concepts/multi-turn-conversations.md).
 
 ## Troubleshooting
 
@@ -294,6 +296,8 @@ If you created an OpenAI deployment for this quickstart, delete the deployment f
 
 For more information, see [Deploy models in Foundry](../../../../ai-foundry/how-to/deploy-models-managed.md).
 
+To delete the Foundry project:
+
 1. Go to [Microsoft Foundry (classic)](https://ai.azure.com/).
 1. Select the project you want to delete.
 1. Select **Management center**.
@@ -302,12 +306,10 @@ For more information, see [Deploy models in Foundry](../../../../ai-foundry/how-
 If you want to remove Azure resources, delete either the individual resource or the entire resource group. Deleting the resource group removes all contained resources.
 
 > [!TIP]
-> If you plan to delete an Azure AI resource that has model deployments, delete deployments first.
+> If you plan to delete a resource that has model deployments, delete the deployments first.
 
-## Next steps
+## Related content
 
-* [Learn how CLU handles entity slot filling across multi-turn conversations](../concepts/multi-turn-conversations.md)
+* [Multi-turn conversations in CLU](../concepts/multi-turn-conversations.md)
 * [Build a multi-turn model](build-multi-turn-model.md)
-* [Call the CLU API](call-api.md)
-* [How to use Foundry Tools in the Foundry portal](../../../connect-services-foundry-portal.md)
-* [Language role-based access control](../../concepts/role-based-access-control.md)
+
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチターン会話理解のクイックスタート更新"
}
```

### Explanation
このコードの差分は、マルチターン会話理解（CLU）モデルのクイックスタートガイドに関する更新を示しています。主な変更点は以下の通りです。

- **タイトルと説明の更新**: 説明文が「Microsoft Foundry (classic)」と明確に記載され、Microsoft Foundryの文脈が強調されています。また、ドキュメントの更新日も新たに設定されています。

- **重要な情報の追加**: Azureサブスクリプションを持っていないユーザー向けに、無料アカウントの作成を促すリンクが追加されました。これにより、初心者ユーザーがより容易にスタートできるよう配慮されています。

- **ナビゲーションの改善**: 画像の説明が強化され、ユーザーに対してより具体的な情報が提供されています。これにより、どのページで何を選択すればよいかが明確になります。

- **トラブルシューティングの詳細強化**: クイックスタート後のモデルデプロイについての手順がテンプレート化され、新しい情報が追加されています。また、Foundryプロジェクト削除の手順が明確に示されています。

- **セクション名の変更**: "Next steps"から"Related content"への変更が行われ、関連するコンテンツへの参照が整理されました。これにより、読者が次に進むべき内容が理解しやすくなっています。

これらの更新は、ユーザーがマルチターン会話理解モデルを効果的に利用し、適切なリソースを見つける助けとなることを目的としています。全体的に、ユーザーエクスペリエンスが向上し、情報の明確性が高まったことが評価できます。

## articles/ai-services/language-service/language-detection/includes/quickstarts/azure-ai-foundry.md{#item-41c23c}

<details>
<summary>Diff</summary>
````diff
@@ -3,13 +3,16 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 11/18/2025
+ms.date: 02/06/2026
 ms.author: lajanuar
 ai-usage: ai-assisted
 ---
 ## Prerequisites
 
-* [Create a project in Foundry in the Microsoft Foundry portal](../../../../../ai-foundry/how-to/create-projects.md)
+* **Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
+* **Requisite permissions**. Make sure the person establishing the account and project has the Azure AI Account Owner role at the subscription level assigned. Alternatively, the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, see [Role based access control (RBAC)](../../../../../ai-foundry/openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+* **Foundry resource**. Create a [Foundry resource](../../../../multi-service-resource.md) or see [Configure a Foundry resource](../../../concepts/configure-azure-resources.md). Alternatively, you can use a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
+* **A Foundry project**. For more information, see [Create a Foundry project](../../../../../ai-foundry/how-to/create-projects.md).
 
 ### [Foundry (classic)](#tab/foundry-classic)
 
@@ -19,51 +22,53 @@ ai-usage: ai-assisted
 You can use [Foundry (classic)](https://ai.azure.com/) to:
 
 > [!div class="checklist"]
-> * Create a project
-> * Deploy a model
-> * Run a chat completion
-> * Create and run an agent
-> * Upload files to your agent
+> * Detect the language of input text
+> * Review confidence scores and ISO language codes
+> * Configure country/region hints for improved accuracy
 
-## [Foundry (classic)](https://ai.azure.com/) Playground
+## Navigate to the Foundry (classic) playground
 
-Using the left side pane, select **Playgrounds**. Then select the **Try Azure Language Playground** button.
+1. In the left pane, select **Playgrounds**.
+1. Select the **Try Azure Language Playground** button.
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/foundry-playground-navigation.png" alt-text="Screenshot showing the Playgrounds navigation and the Try Azure Language Playground button in Foundry (classic)." lightbox="../../media/quickstarts/azure-ai-foundry/foundry-playground-navigation.png":::
+   :::image type="content" source="../../media/quickstarts/azure-ai-foundry/foundry-playground-navigation.png" alt-text="Screenshot showing the Playgrounds navigation and the Try Azure Language Playground button in Foundry (classic)." lightbox="../../media/quickstarts/azure-ai-foundry/foundry-playground-navigation.png":::
 
-## Use Language Detection in the Foundry Playground
+## Detect language in the Foundry playground
 
-The **Language Playground** consists of four sections:
+The **Language playground** consists of four sections:
 
-* Top banner: You can select any of the currently available Languages here.
-* Left pane: This pane contains **Configuration** options for the service, such as the API version and model version.
-* Center pane: This pane is where you enter your text for processing and review results.
-* Right pane: This pane shows **Details** about the run.
 
-Here you can select Azure Language Detection capability by choosing the top banner tile, **Detect language**.
+   | Section | Purpose |
+   | --- | --- |
+   | **Top banner** | Select the **Detect language** tile. |
+   | **Left pane** | Set **Configuration** options such as API version, model version, and country hint. |
+   | **Center pane** | Enter text for processing and review results. |
+   | **Right pane** | View **Details** for detected language and script. |
 
-## Use Detect language
+1. Select the **Detect language** tile from the top banner.
+1. Enter or paste text in the center pane.
+1. In the **Configuration** pane, set the following options:
 
-**Detect language** is designed to identify the language typed in text.
+   |Option              |Description                              |
+   |--------------------|-----------------------------------------|
+   |Select API version  | Select which version of the API to use.    |
+   |Select model version| Select which version of the model to use.|
+   |Select country hint| Select the origin country/region of the input text. |
 
-In **Configuration** there are the following options:
+1. Select the **Run** button to detect the language.
 
-|Option              |Description                              |
-|--------------------|-----------------------------------------|
-|Select API version  | Select which version of the API to use.    |
-|Select model version| Select which version of the model to use.|
-|Select country hint| Select the origin country/region of the input text. |
+After the operation completes, the **Details** section displays the following fields for the detected language and script:
 
-After your operation is completed, the **Details** section contains the following fields for the most detected language and script:
+   | Field | Description |
+   | --- | --- |
+   | ISO 639-1 Code | The ISO 639-1 two-letter code for the detected language. |
+   | Confidence Score | The model's level of certainty that the language identification is correct. |
+   | Script Name | The name of the detected script in the text. |
+   | ISO 15924 Script Code | The ISO 15924 code for the detected script (writing system). |
 
-|Field | Description|
-|---|---|
-|ISO 639-1 Code| The ISO 639-1 code for the most detected language.|
-|Confidence Score| How confident the model is in the correctness of identification of the most typed language.|
-|Script Name| The name of the most detected script in the text.|
-|ISO 15924 Script Code| The ISO 15924 script code for the most detected script.|
+  :::image type="content" source="../../media/quickstarts/azure-ai-foundry/language-detection.png" alt-text="A screenshot showing language detection results with confidence scores and ISO codes displayed in the Details pane of the Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/language-detection.png":::
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/language-detection.png" alt-text="A screenshot of an example of detect language in Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/language-detection.png":::
+Verify that the detected language matches the language of your input text. If the result shows `unknown`, provide a longer text sample or set a **Country hint** for better accuracy.
 
 ### [Foundry (new)](#tab/foundry-new)
 
@@ -73,17 +78,17 @@ After your operation is completed, the **Details** section contains the followin
 You can use [Foundry (new)](https://ai.azure.com/) to:
 
 > [!div class="checklist"]
-> * Create a project
-> * Deploy a model
-> * Create and run an agent
-> * Upload files to the agent
+> * Detect the language of input text
+> * Review confidence scores and ISO language codes
+> * Configure country/region hints for improved accuracy
 
-## Navigate to [Foundry (new)](https://ai.azure.com/)
+## Navigate to the Foundry (new) playground
 
- The project you're working on appears in the upper-left corner.  
-* You can select to create a new project from the drop-down menu:
-  * Select the provided project name or create a new project name.
-  * Finally, select **Create project**.
+The active project appears in the upper-left corner. To create a new project:
+
+1. Open the project drop-down menu.
+1. Enter a project name or select an existing one.
+1. Select **Create project**.
 
    :::image type="content" source="../../../media/new-foundry-homepage.png" alt-text="Screenshot of the Foundry (new) homepage":::
 
@@ -99,29 +104,27 @@ There are two ways to access the Language Detection interface:
    * Select the **AI services** tab.
    * Next, select  **Azure-Language-detection** to go to the playground.
 
-## Use playground: detect language in text
-
-The Foundry playground is an interactive environment where you can engage with deployed AI models.
+## Detect language in the Foundry playground
 
 The **Detect Language** feature identifies the language used in written content.
 
-1. On the **Playground tab**, you can choose a text sample from the drop-down menu, choose the paperclip icon to upload your own text, or type your text directly into the sample window.
+1. On the **Playground** tab, select a text sample from the drop-down menu, use the paperclip icon to upload your text, or enter your own text.
 
-1. Next select the **Configure** button. In the **Configure** side panel, you can select from the following options:
+1. Select the **Configure** button. In the **Configure** side panel, set the following options:
 
-   |Option|Description|
-   |---|---|
-   |**API version**| Select the API version that you prefer to use.|
-   |**Model version**| Select the model version that you prefer to use.|
-   |**Country/region hint** (optional)| You can select the origin country/region for the source text.|
+  |Option|Description|
+  |---|---|
+  |**API version**| Select the API version that you prefer to use.|
+  |**Model version**| Select the model version that you prefer to use.|
+  |**Country/region hint** (optional)| You can select the origin country/region for the source text.|
 
 After you make your selections, choose the **Detect** button. Then review the text and accompanying details written in formatted text or as a JSON response:
 
-   |Field | Description|
-   |---|---|
-   |**Confidence**| The model's level of certainty regarding whether it correctly identified a language.|
-   |**ISO 639-1 code**| A two letter code for the detected language.|
-   |**Detected script**| The name of the detected script in the text.|
-   |**Detected script code**| The ISO 15924 script code for the detected script (writing system).|
+  |Field | Description|
+  |---|---|
+  |**Confidence**| The model's level of certainty regarding whether it correctly identified a language.|
+  |**ISO 639-1 code**| A two letter code for the detected language.|
+  |**Detected script**| The name of the detected script in the text.|
+  |**Detected script code**| The ISO 15924 script code for the detected script (writing system).|
 
-You can use the **Edit** button to modify the **Configure** parameters and customize your response as needed.
\ No newline at end of file
+Verify that the detected language matches the language of your input text. You can use the **Edit** button to modify the **Configure** parameters and rerun detection as needed.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語検出のクイックスタート更新"
}
```

### Explanation
このコードの差分は、Azure AI Foundryにおける言語検出機能に関するクイックスタートガイドの更新を示しています。主な変更点は以下の通りです。

- **日付の更新**: ドキュメントの更新日が2026年2月6日に変更され、新しい情報の提供が強調されています。

- **前提条件の追加と明確化**: Azureサブスクリプションや必要な権限に関する詳細が追加され、ユーザーが要求される設定を理解しやすくなっています。具体的には、Azure AIのアカウントオーナー権限やプロジェクト作成に関する情報が盛り込まれています。

- **機能のハイライト**: Foundryのチェックリストに、言語検出機能が追加され、正確性向上のために国/地域ヒントを設定するオプションが強調されています。

- **手順の改善**: 言語検出機能の使い方のセクションが詳細に説明され、構成オプションやテキストの入力方法に関する情報が分かりやすく整理されました。

- **構成オプションのテーブル化**: 各構成オプションが表形式で提示され、どのような設定が可能かが一目でわかるようになっています。

- **結果の表示内容の充実**: 検出された言語の詳細セクションに追加情報として、ISO コードや信頼度スコア、スクリプト名に関する詳細が incorporated（組み込まれ）、理解を深める手助けとなっています。

- **操作後のフィードバック**: 検出結果が適合しているか確認するためのアドバイスが追加されており、よりユーザーフレンドリーな構成になっています。

これらの変更により、ユーザーがAzure AI Foundryの言語検出機能を利用する際の利便性が向上し、必要な操作が以前よりも簡単に行えるようになっています。全体として、明確な情報の提供と使いやすさの向上が図られています。

## articles/ai-services/language-service/language-detection/quickstart.md{#item-636553}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,12 @@
 ---
-title: "Quickstart: Use the Azure Language Detection client library"
+title: "Quickstart: Detect the language of text"
 titleSuffix: Foundry Tools
-description: Detect the language of text with Azure Language Detection using SDKs, the REST API, or the Foundry portal.
+description: Use Azure Language in Foundry Tools to detect the language of text with client libraries, the REST API, or the Microsoft Foundry portal.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 11/18/2025
+ms.date: 02/06/2026
 ms.author: lajanuar
 ms.devlang: csharp
 # ms.devlang: csharp, java, javascript, python
@@ -15,7 +15,11 @@ keywords: text mining, language detection
 zone_pivot_groups: programming-languages-text-analytics
 ai-usage: ai-assisted
 ---
-# Quickstart: Use the Azure Language Detection client library and REST API
+# Quickstart: Detect the language of text
+
+In this quickstart, you use the Azure Language in Foundry Tools language detection feature to identify the language of input text. You can get started using your preferred client library, the REST API, or the Microsoft Foundry portal.
+
+If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
 
 ::: zone pivot="programming-language-csharp"
 
@@ -60,15 +64,17 @@ ai-usage: ai-assisted
 | You get a `401` or `403` error when calling the API. | Confirm your key and endpoint are correct for the same Azure AI resource. If you recently changed role assignments, wait a few minutes and try again. |
 | You get an error about missing environment variables. | Confirm `LANGUAGE_KEY` and `LANGUAGE_ENDPOINT` are set in your environment before you run the sample. |
 | The Foundry experience doesn't match the steps. | In the Foundry portal, use the version toggle to switch between Foundry (classic) and Foundry (new), then follow the matching tab in the Foundry section. |
+| The API returns `unknown` as the detected language. | The input text might be too short or ambiguous. Provide a longer text sample or set the **Country/region hint** to improve accuracy. |
+| The API returns an `InvalidCountryHint` error. | Confirm the country hint code is a valid ISO 3166-1 alpha-2 code (for example, `US`, `FR`, `JP`). |
 
 ## Clean up resources
 
-To clean up and remove an Azure AI resource, you can delete either the individual resource or the entire resource group. If you delete the resource group, all resources contained within are also deleted.
+If you no longer need the resources you created in this quickstart, delete the individual resource or the entire resource group. Deleting the resource group also deletes all other resources associated with it.
 
 * [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
 * [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
 
-## Next steps
+## Related content
 
 * [Language detection overview](overview.md)
 * [Call the Language Detection API](how-to/call-api.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキストの言語検出に関するクイックスタート更新"
}
```

### Explanation
このコードの差分は、Azureの言語検出機能に関するクイックスタートガイドの更新を示しています。主な変更点は以下の通りです。

- **タイトルと説明の変更**: タイトルが「Azure Language Detection client libraryを使用したクイックスタート」から「テキストの言語を検出するクイックスタート」に変更され、より明確に目的が示されています。また、説明文も具体的なツールと手法を示す内容に更新されています。

- **日付の更新**: ドキュメントの更新日が2026年2月6日に変更され、最新情報が反映されています。

- **導入部の追加**: クイックスタートの導入部として、Azure Language in Foundry Toolsを使用した言語検出機能の使用方法が説明されています。これにより、初めてのユーザーでも取り掛かりやすくなっています。

- **前提条件のリンクが強調**: Azureサブスクリプションを持っていない場合には、無料アカウントの作成を促すリンクが追加され、便宜が図られています。

- **エラーハンドリング情報の追加**: APIが「unknown」と言語を返す場合の対応策や、無効な国ヒントコードに関するエラーメッセージの確認方法が追加され、ユーザーの利便性が向上しています。

- **リソースのクリーンアップ手順の明確化**: 使用済みのAzure AIリソースの削除手順が分かりやすく記載され、リソース管理が容易になっています。

- **次のステップから関連コンテンツへの変更**: 「次のステップ」というセクションが「関連コンテンツ」に変更され、情報が関連付けられ、ユーザーが次にどのリソースを探索するかいえすくなっています。

この更新により、ユーザーは言語検出機能をより簡単に理解し、効果的に利用できるようになっています。全体として、ガイドの構成と内容が改善され、学習体験が向上しています。

## articles/ai-services/language-service/overview.md{#item-f138b4}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ Azure Language provides both remote and local MCP server options:
 * **Remote server**: Available through Foundry Tool Catalog for cloud-hosted deployments.
 * **Local server**: Available for developers who prefer to host the server in their own environment.
 
-For more information, *see* [Azure Language MCP server](concepts/foundry-tools-agents.md#azure-language-mcp-server-).
+For more information, *see* [Azure Language MCP server](concepts/foundry-tools-agents.md#azure-language-mcp-server-preview).
 
 ## Available agents
 
@@ -35,13 +35,13 @@ Azure Language offers prebuilt agents that handle specific conversational AI sce
 
 The Intent Routing agent intelligently manages conversation flows by understanding user intentions and delivering accurate responses in conversational AI applications. This agent uses predictable decision-making processes combined with controlled response generation to ensure consistent, reliable interactions that organizations can trust and monitor. 
 
-For more information, *see* [Azure Language Intent Routing agent](concepts/foundry-tools-agents.md#azure-language-intent-routing-agent-).
+For more information, *see* [Azure Language Intent Routing agent](concepts/foundry-tools-agents.md#azure-language-intent-routing-agent-preview).
 
 ### Azure Language Exact Question Answering agent 🆕
 
 The Exact Question Answering agent provides reliable, word-for-word responses to your most important business questions. This agent automates frequently asked questions while maintaining human oversight and quality control to ensure accuracy and compliance.
 
-For more information, *see* [Azure Language Exact Question Answering agent](concepts/foundry-tools-agents.md#azure-language-exact-question-answering-agent-).
+For more information, *see* [Azure Language Exact Question Answering agent](concepts/foundry-tools-agents.md#azure-language-exact-question-answering-agent-preview).
 
 ## Available features
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Languageサービスの概要更新"
}
```

### Explanation
このコードの差分は、Azure Languageサービスに関する概要ドキュメントの更新を示しています。主な変更点は以下の通りです。

- **リンク先の更新**: 「Azure Language MCPサーバー」や「Azure Language Intent Routingエージェント」、「Azure Language Exact Question Answeringエージェント」に関するリンクが、より具体的な「プレビュー」バージョンのリンクに変更されました。これにより、ユーザーは最新の情報に基づいたリソースにアクセスできるようになります。

- **トピックタイトルの一貫性**: プレビュー版を強調するために、リンクの一部に「-」のような記号が取り除かれ、整然とした印象を与えるようになりました。

- **新しいエージェントの紹介**: エージェントに関する説明が一貫しており、特に「Exact Question Answering agent」では、ビジネス上の重要な質問に対する信頼性のある応答を提供する旨が説明されていますが、このセクションは変更されていません。

これらの変更により、Azure Languageサービスの内容が更新され、ユーザーにとって利用可能な最新情報が強調されています。全体として、ドキュメントの明確さと情報の関連性が向上しています。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/azure-ai-foundry.md{#item-ff89fc}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 11/18/2025
+ms.date: 02/06/2026
 ms.author: lajanuar
 ms.custom: language-service-pii
 ai-usage: ai-assisted
@@ -14,11 +14,11 @@ ai-usage: ai-assisted
 >
 > * If you already have an Azure Language in Foundry Tools or multi-service resource—whether used on its own or through Language Studio—you can continue to use those existing Language resources within the Microsoft Foundry portal. 
 > * For more information, see [Connect services in the Microsoft Foundry portal](../../../../connect-services-foundry-portal.md).
-> * We recommend that you use a Foundry resource. You can also follow these instructions with a Language resource.
+> * Consider using a Foundry resource for the best experience. You can also follow these instructions with a Language resource.
 
 * **Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 * **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, see [Role based access control (RBAC)](../../../../../ai-foundry/openai/how-to/role-based-access-control.md#cognitive-services-contributor).
-*  [Foundry resource](../../../../multi-service-resource.md). For more information, see [Configure a Foundry resource](../../../concepts/configure-azure-resources.md). Alternately, you can use a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
+* **Foundry resource**. Create a [Foundry resource](../../../../multi-service-resource.md) or see [Configure a Foundry resource](../../../concepts/configure-azure-resources.md). Alternatively, you can use a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
 * **A Foundry project**. For more information, see [Create a Foundry project](../../../../../ai-foundry/how-to/create-projects.md).
 
 
@@ -31,29 +31,31 @@ ai-usage: ai-assisted
 You can use [Foundry (classic)](https://ai.azure.com/) to:
 
 > [!div class="checklist"]
-> * Create a project
-> * Deploy a model
-> * Run a chat completion
-> * Create and run an agent
-> * Upload files to your agent
+> * Extract PII from conversations
+> * Extract PII from text
+> * Configure redaction policies
+> * Review detected entities and confidence scores
 
 
-## Navigate to the [Foundry (classic)](https://ai.azure.com/) Playground
+## Navigate to the Foundry (classic) playground
 
-Using the left side pane, select **Playgrounds**. Then select the **Try Azure Language Playground** button.
+1. In the left pane, select **Playgrounds**.
+1. Select the **Try Azure Language Playground** button.
 
 :::image type="content" source="../../media/quickstarts/azure-ai-foundry/foundry-playground-navigation.png" alt-text="Screenshot showing the Playgrounds navigation and the Try Azure Language Playground button in Foundry (classic)." lightbox="../../media/quickstarts/azure-ai-foundry/foundry-playground-navigation.png":::
 
-## Use PII in the Foundry Playground
+## Detect PII in the Foundry playground
 
 The **Language Playground** consists of four sections:
 
-* Top banner: You can select any of the currently available languages here.
-* Left pane: This pane contains **Configuration** options for the service, such as the API version and model version.
-* Center pane: This pane is where you enter text for processing and review results.
-* Right pane: This pane shows **Details** about the run.
+| Section | Purpose |
+| --- | --- |
+| **Top banner** | Select the input language and choose a PII detection capability. |
+| **Left pane** | Set **Configuration** options such as API version, model version, and redaction policy. |
+| **Center pane** | Enter text for processing and review highlighted results. |
+| **Right pane** | View **Details** for each detected entity. |
 
-Here you can select from two Personally Identifying Information (PII) detection capabilities by choosing the top banner tiles, **Extract PII from conversation** or **Extract PII from text**. Each is for a different scenario.
+Select either **Extract PII from conversation** or **Extract PII from text** from the top banner tiles. Each capability targets a different scenario.
 
 ### Extract PII from conversation
 
@@ -65,22 +67,26 @@ In **Configuration** there are the following options:
 |--------------------|-----------------------------------------|
 |Select API version  | Select which version of the API to use.    |
 |Select model version| Select which version of the model to use.|
-|Select text language| Select which language the language is input in.|
-|Select types to include| Select they types of information you want to redact.|
+|Select text language| Select the language of your input text.|
+|Select types to include| Select the types of information you want to redact.|
 |Specify redaction policy| Select the method of redaction.|
-|Specify redaction character| Select which character is used for redaction. Only available with the **CharacterMask** redaction policy.|
+|Specify redaction character| Select the character used for redaction. Only available with the **CharacterMask** redaction policy.|
+
+After the operation completes, each detected entity is highlighted in the center pane with its type label displayed beneath it.
 
-After your operation is completed, the type of entity is displayed beneath each entity in the center pane. The **Details** section contains the following fields for each entity:
+The **Details** section contains the following fields for each entity:
 
 |Field | Description                |
 |------|----------------------------|
 |Entity|The detected entity.|
 |Category| The entity type that was detected.|
-|Offset| The number of characters that the entity was detected from the beginning of the line.|
+|Offset| The number of characters from the beginning of the line to the entity.|
 |Length| The character length of the entity.|
-|Confidence| How confident the model is in the correctness of identification of entity's type.|
+|Confidence| The model's level of certainty that the entity type is correct.|
+
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/conversation-pii.png" alt-text="A screenshot showing detected PII entities highlighted in a conversation with entity details displayed in the right pane of the Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/conversation-pii.png":::
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/conversation-pii.png" alt-text="A screenshot of an example of extract PII from conversation in Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/conversation-pii.png":::
+Verify that each PII entity appears highlighted with the correct category label. If no entities appear, check that the input text contains recognizable PII patterns and that the **Types** filter includes the expected categories.
 
 ### Extract PII from text
 
@@ -92,23 +98,27 @@ In **Configuration** you can select from the following options:
 |--------------------|-----------------------------------------|
 |Select API version  | Select which version of the API to use.    |
 |Select model version| Select which version of the model to use.|
-|Select text language| Select which language the language is input in.|
+|Select text language| Select the language of your input text.|
 |Select types to include| Select the types of information you want to redact.|
 |Specify redaction policy| Select the method of redaction.|
-|Specify redaction character| Select which character is used for redaction. Only available with the **CharacterMask** redaction policy.|
+|Specify redaction character| Select the character used for redaction. Only available with the **CharacterMask** redaction policy.|
 
-After your operation is completed, the type of entity is displayed beneath each entity in the center pane. The **Details** section contains the following fields for each entity:
+After the operation completes, each detected entity is highlighted in the center pane with its type label displayed beneath it.
+
+The **Details** section contains the following fields for each entity:
 
 |Field | Description                |
 |------|----------------------------|
 |Entity|The detected entity.|
 |Category| The entity type that was detected.|
-|Offset| The number of characters that the entity was detected from the beginning of the line.|
+|Offset| The number of characters from the beginning of the line to the entity.|
 |Length| The character length of the entity.|
-|Confidence| How confident the model is in the correctness of identification of entity's type.|
-|Tags| How confident the model is in the correctness for each identified entity type.|
+|Confidence| The model's level of certainty that the entity type is correct.|
+|Tags| The model's confidence scores for each identified entity subtype.|
+
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/text-pii.png" alt-text="A screenshot showing detected PII entities highlighted in text with entity details and confidence scores displayed in the right pane of the Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/text-pii.png":::
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/text-pii.png" alt-text="A screenshot of an example of extract PII from text in Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/text-pii.png":::
+Verify that each PII entity appears highlighted with the correct category label. The **Tags** column shows subcategory confidence scores when applicable.
 
 ### [Foundry (new)](#tab/foundry-new)
 
@@ -119,18 +129,18 @@ After your operation is completed, the type of entity is displayed beneath each
 You can use [Foundry (new)](https://ai.azure.com/) to:
 
 > [!div class="checklist"]
-> * Create a project
-> * Deploy a model
-> * Create and run an agent
-> * Upload files to the agent
+> * Extract PII from text
+> * Configure redaction policies and excluded values
+> * Review detected entities and confidence scores
 
 
-## Navigate to [Foundry (new)](https://ai.azure.com/)
+## Navigate to the Foundry (new) playground
 
-* The project you're working on appears in the upper-left corner.  
-* You can select to create a new project from the drop-down menu:
-  * Select the provided project name or create a new project name.
-  * Finally, select **Create project**.
+The active project appears in the upper-left corner. To create a new project:
+
+1. Open the project drop-down menu.
+1. Enter a project name or select an existing one.
+1. Select **Create project**.
 
    :::image type="content" source="../../../media/new-foundry-homepage.png" alt-text="Screenshot of the Foundry (new) homepage":::
 
@@ -148,15 +158,13 @@ There are two ways to access the PII interface:
    * Next, select **Azure-Language-Text-PII redaction** to go to the playground.
 
 
-## Use playground: extract PII from text
-
-The Foundry playground is an interactive environment where you can engage with deployed AI models.
+## Detect PII in the Foundry playground
 
 The **extract PII from text** feature detects and masks personally identifying information within written content.
 
-1. On the **Playground** tab, select the sample tab, use the paperclip icon to upload your text, or enter your own text.
+1. On the **Playground** tab, select the sample text, use the paperclip icon to upload your text, or enter your own text.
 
-1. Next select the **Configure** button. In the **Configure** side panel, you can select from the following options:
+1. Select the **Configure** button. In the **Configure** side panel, set the following options:
 
 | Option | Description |
 |--|--|
@@ -168,7 +176,10 @@ The **extract PII from text** feature detects and masks personally identifying i
 | **Excluded values** | Select the values that you want to exclude. |
 | **Synonyms** | Select a category for your redaction type values to target related synonyms. |
 
-After you make your selections, choose the **Detect** button. Then review the text and accompanying details written in formatted text or as a JSON response:
+After you make your selections, choose the **Detect** button. Detected entities are highlighted in the text and you can review the accompanying details in formatted text or as a JSON response:
+
+> [!NOTE]
+> The Foundry (new) playground currently supports **text PII** detection. For **conversation PII**, use the **Foundry (classic)** tab.
 
 | Field | Description |
 |--|--|
@@ -177,4 +188,4 @@ After you make your selections, choose the **Detect** button. Then review the te
 | **Offset** | The number of characters that the entity was detected from the beginning of the text. |
 | **Length** | The character length of the entity. |
 
-You can use the **Edit** button to modify the **Configure** parameters and customize your response as needed.
\ No newline at end of file
+Verify that the detected entities match the PII in your input text. You can use the **Edit** button to modify the **Configure** parameters and rerun detection as needed.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人を特定できる情報（PII）に関するクイックスタートの更新"
}
```

### Explanation
このコードの差分は、Azure AI Foundryにおける個人を特定できる情報（PII）に関するクイックスタートガイドの更新を示しています。主な変更点は以下の通りです。

- **日付の更新**: ドキュメントの更新日が2026年2月6日に変更され、最新情報が反映されています。

- **推奨事項の改訂**: 「Foundryリソースを使用することを推奨します」という表現が「最高の体験を得るためにFoundryリソースの使用を検討してください」とし、より柔らかいトーンになっています。

- **手順の詳細化**: PII検出を行うための手順がより明確に記載され、一部のセクションが整理されています。特に、Playgroundのインターフェースに関する説明が詳細になり、ユーザーがどのように操作するかが具体的に示されています。

- **構成オプションの整理**: 設定オプションに関する情報が整理され、各オプションの説明が明確になりました。「言語」の選択に関する説明が改善され、理解しやすくなっています。

- **エラー検出への注意喚起**: PIIエンティティが正しくハイライトされているか確認するセクションが追加され、ユーザーが期待する結果を達成するための注意が促されています。

- **ドキュメントのレイアウト改善**: セクションタイトルが整理され、内容がより簡潔に伝わりやすくなっています。また、表形式で表示される情報が増え、視覚的に理解しやすくなっています。

これらの変更により、個人を特定できる情報に関するクイックスタートガイドが改善され、ユーザーがAzure FoundryでのPII検出機能をより効果的に活用できるようになっています。全体として、ガイドの内容がよりユーザーフレンドリーになっており、実際の利用状況に即した情報が提供されています。

## articles/ai-services/language-service/personally-identifiable-information/quickstart.md{#item-94affd}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,12 @@
 ---
 title: "Quickstart: Detect personally identifiable information (PII) in text"
 titleSuffix: Foundry Tools
-description: Detect and redact personally identifiable information (PII) in text using client libraries, the REST API, or the Microsoft Foundry portal.
+description: Use Azure Language in Foundry Tools to detect and redact personally identifiable information (PII) in text with client libraries, the REST API, or the Microsoft Foundry portal.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 01/30/2026
+ms.date: 02/06/2026
 ms.author: lajanuar
 ms.devlang: csharp
 # ms.devlang: csharp, java, javascript, python
@@ -25,8 +25,12 @@ ai-usage: ai-assisted
 # Quickstart: Detect personally identifiable information (PII)
 <!-- markdownlint-disable MD025 -->
 
+In this quickstart, you use the Azure Language in Foundry Tools PII detection feature to identify and redact personally identifiable information in text. You can get started using your preferred client library, the REST API, or the Microsoft Foundry portal.
+
+If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
+
 > [!NOTE]
-> This quickstart guides you through the process of locating personally identifiable information (PII) in documents. To detect PII in conversations, see [How to detect and redact PII in conversations](how-to/redact-conversation-pii.md). To detect PII in text, see [How to detect and redact PII in text](how-to/redact-text-pii.md).
+> This quickstart covers PII detection in documents. To detect PII in conversations, see [How to detect and redact PII in conversations](how-to/redact-conversation-pii.md). To detect PII in text, see [How to detect and redact PII in text](how-to/redact-text-pii.md).
 
 ::: zone pivot="programming-language-csharp"
 
@@ -71,19 +75,19 @@ ai-usage: ai-assisted
 | You get a `401` or `403` error when calling the API. | Confirm your key and endpoint are correct for the same Azure AI resource. If you recently changed role assignments, wait a few minutes and try again. |
 | You get an error about missing environment variables. | Confirm `LANGUAGE_KEY` and `LANGUAGE_ENDPOINT` are set in your environment before you run the sample. |
 | The Foundry experience doesn't match the steps. | In the Foundry portal, use the version toggle to switch between Foundry (classic) and Foundry (new), then follow the matching tab in the Foundry section. |
+| No entities are detected in your text. | Verify that the input text contains recognizable PII patterns (names, addresses, phone numbers). Check that the **Types** filter includes the entity categories you expect. |
+| The API returns an `InvalidLanguage` error. | Confirm the language code in the request matches one of the [supported languages](language-support.md). |
 
 ## Clean up resources
 
-To clean up and remove an Azure AI resource, you can delete either the individual resource or the entire resource group. If you delete the resource group, all resources contained within are also deleted.
+If you no longer need the resources you created in this quickstart, delete the individual resource or the entire resource group. Deleting the resource group also deletes all other resources associated with it.
 
 * [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
 * [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
 
-## Next steps
+## Related content
 
 * [PII overview](overview.md)
 * [How to detect and redact PII in text](how-to/redact-text-pii.md)
 * [How to detect and redact PII in conversations](how-to/redact-conversation-pii.md)
 * [Supported entity categories for text](concepts/entity-categories.md)
-* [Language support](language-support.md)
-* [Use containers](how-to/use-containers.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人を特定できる情報（PII）クイックスタートガイドの更新"
}
```

### Explanation
このコードの差分は、Azureの個人を特定できる情報（PII）に関するクイックスタートガイドの更新を示しています。主な変更点は以下の通りです。

- **説明文の強化**: 説明がより具体的になり、「Azure Language in Foundry Toolsを使用して...」という表現が追加され、使用するツールや方法が明確に示されています。

- **日付の更新**: 更新日が2026年2月6日に変更され、情報が最新のものとなっています。

- **クイックスタートの目的の明確化**: クイックスタートの冒頭に、特に文書内のPIIを識別し、削除するためのプロセスに関する情報が追加されました。このガイドがカバーしている内容がユーザーに明確に伝えられています。

- **ノートの内容修正**: 注意書きの文言が調整され、PIIを文書内で検出することに焦点を当てつつ、会話内での検出方法へのリンクも提供されており、対象を明確にしています。

- **エラーメッセージに関する情報追加**: 新たに「No entities are detected in your text」というエラーケースが追加され、入力テキストが認識可能なPIIパターンを含んでいるかどうかを確認するよう促しています。

- **関連コンテンツセクションの名称変更**: 「次のステップ」というセクションタイトルが「関連コンテンツ」に変更され、関連資料へのリンクが提供され、ユーザーがさらに学びを深める手助けとなるようになりました。

これらの更新により、クイックスタートガイドがより理解しやすくなり、ユーザーがAzureのPII検出機能を効果的に利用できるように工夫されています。全体として、情報の一貫性や操作の明確さが向上しています。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -42,9 +42,9 @@ Stay informed about recent releases and enhancements designed to help you get th
 
 **Azure Language integrates with Foundry Tools**. Azure Language now provides specialized tools and agents for building conversational AI applications in Foundry:
 
-* [Azure Language MCP server](concepts/foundry-tools-agents.md#azure-language-mcp-server-). Connects AI agents to Azure Language services through the Model Context Protocol.
-* [Azure Language Intent Routing agent](concepts/foundry-tools-agents.md#azure-language-intent-routing-agent-). Manages conversation flows by combining intent classification with answer delivery.
-* [Azure Language Exact Question Answering agent](concepts/foundry-tools-agents.md#azure-language-exact-question-answering-agent-). Delivers consistent responses to frequently asked business questions.
+* [Azure Language MCP server](concepts/foundry-tools-agents.md#azure-language-mcp-server-preview). Connects AI agents to Azure Language services through the Model Context Protocol.
+* [Azure Language Intent Routing agent](concepts/foundry-tools-agents.md#azure-language-intent-routing-agent-preview). Manages conversation flows by combining intent classification with answer delivery.
+* [Azure Language Exact Question Answering agent](concepts/foundry-tools-agents.md#azure-language-exact-question-answering-agent-preview). Delivers consistent responses to frequently asked business questions.
 
 **Azure Language capabilities now available in Foundry**. Several Azure Language capabilities are now available with the Foundry:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Languageの新機能の更新"
}
```

### Explanation
このコードの差分は、Azure Languageサービスの「新機能」ドキュメントの更新を示しています。主な変更点は以下の通りです。

- **リンクの更新**: Azure Languageに関連するエージェントのリンクが更新され、各エージェントの参照が「-」の部分が「-preview」に変更されています。これにより、これらのエージェントがまだプレビュー版であることが明示的に示されています。

- **新機能の説明の明確化**: 各エージェント（MCPサーバー、Intent Routingエージェント、Exact Question Answeringエージェント）の説明文は変更されていませんが、リンクの更新により、ユーザーが最新の情報にアクセスできるようになっています。

- **セクションタイトル保持**: 更新された内容は、一貫して「Azure Language integrates with Foundry Tools」というタイトルの下に記載されており、Azure LanguageがFoundryツールとどのように統合されているかが示されています。

これらの変更により、ユーザーはAzure Languageの新しい機能を探す際に、プレビュー版のエージェントへの正確なリンクを受け取ることができるようになり、情報の透明性と正確性が向上しています。全体として、ドキュメントの最新の状態が保たれ、ユーザーが新しい機能を効果的に利用できるためのサポートが強化されています。


