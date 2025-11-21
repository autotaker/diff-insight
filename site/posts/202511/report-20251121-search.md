---
date: '2025-11-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:05b2bb7...MicrosoftDocs:ff7d49c
summary: このドキュメントは、Azure AI Searchおよび関連サービスに関する情報を最新のものとして整備するために行われたコードの更新をまとめています。主な変更点には、日付やAPIバージョンの更新、新しい情報の追加、文言の明確化、手順の再編成が含まれます。特に、セマンティックランカーにおけるクイックスタートガイドやFAQの更新、複数データソースを使用したチュートリアルの整理が実施され、ユーザーが手順を明確に理解できるようになっています。また、MCPを用いたAzure
  AI検索とFoundryエージェントサービスの統合方法に関する説明が強化され、全体としての情報の正確性と可読性が向上しています。この一連の更新により、ユーザー体験が向上し、技術文書の一貫性も強化されました。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:05b2bb7...MicrosoftDocs:ff7d49c){target="_blank"}

<format>
# Highlights
このドキュメントの複数の記事にわたるコードの更新は、Azure AI Searchおよび関連サービスに関する新しい情報と明確化を提供し、全体としての整合性と実用性を高めます。主な変更は、日付やAPIバージョンの更新、新しい情報の追加、文言の明確化、および手順の再編成です。

## New features
- セマンティックランカーにおけるクイックスタートガイドやFAQの更新を通じてユーザーが必要な手順を明確に理解できるようになりました。
- 複数データソースを使用するチュートリアルの内容が整理され、具体的な例や説明が追加されました。

## Breaking changes
特記すべき重大な変更はありません。

## Other updates
- MCPを利用したAzure AI検索とFoundryエージェントサービスの統合方法に関する細かい説明を増強。
- 日付が最新状態に更新され、APIバージョンや地域サポートに関する情報が明示化されました。
- 一部のセクション名やタイトルの変更で、一貫性や明確性が向上されています。

# Insights
この一連の更新は、Azureサービスに関する情報の正確性と可読性を高めることを目的としています。特に、エージェントリトリーバルやセマンティックランカーなど、特定の機能やサービスに関連したガイドが微細な変更を受けることで、ユーザーがそれらの機能を迅速かつ確実に導入するためのサポートを強化しています。

各ガイドが最新の情報を反映するとともに、それぞれのプログラミング言語や使用ケースに応じて細かくカスタマイズされた情報を提供することで、開発者がAzureの機能を最大限に活用できる手引きとしての役割を強化しています。また、技術ドキュメントとしての一貫性が向上したことで、異なるドキュメント間の内容比較や手順の確認がより容易になりました。サービスの枠組みや高度な設定を理解するにあたり、このような変更は非常に重要であり、ユーザーフレンドリーな体験を提供します。

さらに、Azure AI SearchのFAQや限界、クオータに関するドキュメントの更新は、利用者がシステムの利用制約や可能性を正しく理解する助けとなり、計画的なサービス使用を支えるものです。この情報の更新により、技術文書がユーザー体験を豊かにし、効率的な問題解決を可能にします。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | エージェントリトリーバルパイプラインの作成方法に関するドキュメントの更新 | modified | 92 | 104 | 196 | 
| [cognitive-search-skill-document-intelligence-layout.md](#item-62c06f) | minor update | ドキュメントインテリジェンスレイアウトスキルに関する記事の更新 | modified | 5 | 3 | 8 | 
| [agentic-retrieval-csharp.md](#item-f93ed3) | minor update | エージェントリトリーバルに関するクイックスタートガイドの更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-java.md](#item-4e2c55) | minor update | エージェントリトリーバルに関するクイックスタートガイドの更新（Java版） | modified | 1 | 1 | 2 | 
| [agentic-retrieval-javascript.md](#item-715283) | minor update | エージェントリトリーバルに関するクイックスタートガイドの更新（JavaScript版） | modified | 1 | 1 | 2 | 
| [agentic-retrieval-python.md](#item-efee6a) | minor update | エージェントリトリーバルに関するクイックスタートガイドの更新（Python版） | modified | 1 | 1 | 2 | 
| [agentic-retrieval-rest.md](#item-3df373) | minor update | エージェントリトリーバルに関するクイックスタートガイドの更新（REST版） | modified | 1 | 1 | 2 | 
| [agentic-retrieval-typescript.md](#item-e6370b) | minor update | エージェントリトリーバルに関するクイックスタートガイドの更新（TypeScript版） | modified | 1 | 1 | 2 | 
| [full-text-csharp.md](#item-2e943a) | minor update | フルテキスト検索に関するクイックスタートガイドの更新（C#版） | modified | 4 | 4 | 8 | 
| [full-text-java.md](#item-d659f9) | minor update | フルテキスト検索に関するクイックスタートガイドの更新（Java版） | modified | 3 | 3 | 6 | 
| [full-text-javascript.md](#item-568e3a) | minor update | フルテキスト検索に関するクイックスタートガイドの更新（JavaScript版） | modified | 3 | 3 | 6 | 
| [full-text-python.md](#item-9bba1c) | minor update | フルテキスト検索に関するクイックスタートガイドの更新（Python版） | modified | 4 | 4 | 8 | 
| [full-text-typescript.md](#item-6630e8) | minor update | フルテキスト検索に関するクイックスタートガイドの更新（TypeScript版） | modified | 3 | 3 | 6 | 
| [search-get-started-rag-rest.md](#item-aa7f2b) | minor update | REST APIクイックスタートガイドの更新 | modified | 2 | 2 | 4 | 
| [search-get-started-rbac-python.md](#item-de7760) | minor update | PythonによるRBACを使用したAzure AI Searchのクイックスタートガイドの更新 | modified | 7 | 7 | 14 | 
| [search-get-started-rbac-rest.md](#item-fd8ef4) | minor update | RBACを使用したAzure AI SearchへのREST接続に関するクイックスタートガイドの更新 | modified | 15 | 13 | 28 | 
| [search-get-started-vector-dotnet.md](#item-8f2f1b) | minor update | .NETアプリを使用したベクトル操作に関するクイックスタートガイドの更新 | modified | 2 | 4 | 6 | 
| [search-get-started-vector-java.md](#item-a3db97) | minor update | Javaを使用したベクトル操作に関するクイックスタートガイドの更新 | modified | 1 | 3 | 4 | 
| [search-get-started-vector-javascript.md](#item-d0387c) | minor update | JavaScriptを使用したベクトル操作に関するクイックスタートガイドの更新 | modified | 1 | 3 | 4 | 
| [search-get-started-vector-python.md](#item-53085f) | minor update | Pythonを使用したベクトル操作に関するクイックスタートガイドの更新 | modified | 2 | 4 | 6 | 
| [search-get-started-vector-rest.md](#item-c7d261) | minor update | REST APIを使用したベクトル操作に関するクイックスタートガイドの更新 | modified | 11 | 15 | 26 | 
| [search-get-started-vector-typescript.md](#item-9b3bc8) | minor update | TypeScriptを使用したベクトル操作に関するクイックスタートガイドの更新 | modified | 1 | 3 | 4 | 
| [semantic-ranker-csharp.md](#item-09fa32) | minor update | C#によるセマンティックランカーのクイックスタートガイドの更新 | modified | 2 | 2 | 4 | 
| [semantic-ranker-intro.md](#item-538e0f) | minor update | セマンティックランカーの紹介ガイドの更新 | modified | 31 | 30 | 61 | 
| [semantic-ranker-java.md](#item-93a05a) | minor update | Javaによるセマンティックランカーのクイックスタートガイドの更新 | modified | 3 | 3 | 6 | 
| [semantic-ranker-javascript.md](#item-2e091c) | minor update | JavaScriptによるセマンティックランカーのクイックスタートガイドの更新 | modified | 7 | 9 | 16 | 
| [semantic-ranker-python.md](#item-a6dcfa) | minor update | Pythonによるセマンティックランカーのクイックスタートガイドの更新 | modified | 5 | 5 | 10 | 
| [semantic-ranker-rest.md](#item-d74861) | minor update | REST APIによるセマンティックランカーのクイックスタートガイドの更新 | modified | 6 | 6 | 12 | 
| [semantic-ranker-typescript.md](#item-6d5573) | minor update | TypeScriptによるセマンティックランカーのクイックスタートガイドの更新 | modified | 9 | 12 | 21 | 
| [search-faq-frequently-asked-questions.yml](#item-eab2ba) | minor update | Azure AI Search FAQの更新 | modified | 30 | 36 | 66 | 
| [search-get-started-rbac.md](#item-9d96c1) | minor update | RBACのクイックスタートガイドの日付更新 | modified | 1 | 1 | 2 | 
| [search-get-started-semantic.md](#item-2b3902) | minor update | セマンティック検索のクイックスタートガイドの日付更新 | modified | 1 | 1 | 2 | 
| [search-get-started-text.md](#item-935941) | minor update | 全文検索のクイックスタートガイドの日付更新 | modified | 1 | 1 | 2 | 
| [search-get-started-vector.md](#item-4984d9) | minor update | ベクトル検索のクイックスタートガイドの日付更新 | modified | 1 | 1 | 2 | 
| [search-indexer-sensitivity-labels.md](#item-2a7bfc) | minor update | センシティビティラベルに関するドキュメントの更新 | modified | 10 | 2 | 12 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | Azure AI Searchのサービス限界およびクオータに関するドキュメントの更新 | modified | 18 | 18 | 36 | 
| [semantic-how-to-enable-scoring-profiles.md](#item-e8d524) | minor update | スコアリングプロファイルを有効にするための前提条件の修正 | modified | 1 | 1 | 2 | 
| [semantic-how-to-query-request.md](#item-85530d) | minor update | クエリリクエストの前提条件の修正 | modified | 1 | 1 | 2 | 
| [semantic-how-to-query-rewrite.md](#item-3e168f) | minor update | クエリリライトの前提条件の修正 | modified | 1 | 1 | 2 | 
| [tutorial-multiple-data-sources.md](#item-71558f) | minor update | 複数データソースに関するチュートリアルの更新 | modified | 70 | 57 | 127 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to design and build a custom agentic retrieval solution w
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 11/07/2025
+ms.date: 11/19/2025
 ms.service: azure-ai-search
 ms.topic: tutorial
 ms.custom:
@@ -18,40 +18,36 @@ ms.custom:
 
 In this tutorial, you learn how to build a solution that integrates Azure AI Search and Foundry Agent Service for intelligent knowledge retrieval.
 
-This solution uses the Model Context Protocol (MCP) to establish a standardized connection between your agentic retrieval pipeline in Azure AI Search, which consists of a *knowledge base* that references a *knowledge source*, and your agent in Foundry Agent Service.
+This solution uses Model Context Protocol (MCP) to establish a standardized connection between your agentic retrieval pipeline in Azure AI Search, which consists of a *knowledge base* that references a *knowledge source*, and your agent in Foundry Agent Service. You can use this architecture for conversational applications that require complex reasoning over large knowledge domains, such as customer support or technical troubleshooting.
 
 The following diagram shows the high-level architecture of this agentic retrieval solution:
 
 :::image type="content" source="media/agentic-retrieval/end-to-end-pipeline.svg" alt-text="Diagram of Azure AI Search integration with Foundry Agent Service via MCP." lightbox="media/agentic-retrieval/end-to-end-pipeline.svg" :::
 
 > [!TIP]
-> + To run the code for this tutorial, download the [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) Python sample on GitHub.
+> + Want to get started right away? See the [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) source code.
 > + Want a simpler introduction to agentic retrieval? See [Quickstart: Use agentic retrieval](search-get-started-agentic-retrieval.md).
 
 ## Prerequisites
 
-+ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md).
-
-+ A search index that satisfies the [criteria for agentic retrieval](agentic-retrieval-how-to-create-index.md).
++ An Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md).
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
-+ An Azure OpenAI resource with a [supported LLM](agentic-retrieval-how-to-create-knowledge-base.md#supported-models) deployment. We recommend a minimum token capacity of 100,000. You can find the LLM's capacity and rate limit in the Foundry portal. If you want [vectorization at query time](vector-search-integrated-vectorization.md#using-integrated-vectorization-in-queries), you should also deploy a text embedding model.
++ A [supported LLM](agentic-retrieval-how-to-create-knowledge-base.md#supported-models) deployed to your project. We recommend a minimum token capacity of 100,000. You can find the LLM's capacity and rate limit in the Foundry portal. If you want [vectorization at query time](vector-search-integrated-vectorization.md#using-integrated-vectorization-in-queries), you should also deploy a text embedding model.
 
-+ [Authorization and permissions](#configure-access) to access each resource.
++ [Authentication and permissions](#authentication-and-permissions) on your search service and project.
 
-+ Package versions that provide preview functionality. For the complete list of versions used in this solution, see the [`requirements.txt`](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/agentic-retrieval-pipeline-example/requirements.txt) file.
++ Preview package versions. For a complete list of versions used in this solution, see the [`requirements.txt`](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/agentic-retrieval-pipeline-example/requirements.txt) file.
 
-### Configure access
+### Authentication and permissions
 
 Before you begin, make sure you have permissions to access content and operations. We recommend Microsoft Entra ID authentication and role-based access for authorization. You must be an **Owner** or **User Access Administrator** to assign roles. If roles aren't feasible, you can use [key-based authentication](search-security-api-keys.md) instead.
 
-Configure access to each resource identified in this section.
+To configure access for this solution, select both of the following tabs.
 
 ### [**Azure AI Search**](#tab/search-perms)
 
-Azure AI Search provides the agentic retrieval pipeline. Configure access for yourself, your app, and your search service for downstream access to models.
-
 1. [Enable role-based access](search-security-enable-roles.md).
 1. [Configure a managed identity](search-how-to-managed-identities.md).
 1. [Assign roles](search-security-rbac.md):
@@ -60,124 +56,108 @@ Azure AI Search provides the agentic retrieval pipeline. Configure access for yo
 
    + For integrated operations, ensure that all clients using the retrieval pipeline have the **Search Index Data Reader** role for sending retrieval requests.
 
-### [**Azure OpenAI**](#tab/openai-perms)
-
-Azure OpenAI hosts the models used by the agentic retrieval pipeline. Configure access for yourself and the search service.
-
-+ You must have the **Cognitive Services User** role to access the LLM and embedding model (if using).
-
-+ For integrated operations, ensure your [search service identity](search-how-to-managed-identities.md) has the **Cognitive Services User** role for model access.
-
 ### [**Microsoft Foundry**](#tab/foundry-perms)
 
-Foundry hosts the agent and MCP tool. Permissions are needed to create and use these resources. For more information, see [Role-based access control in Foundry portal](/azure/ai-foundry/concepts/rbac-azure-ai-foundry).
-
-+ You must be an **Owner** of your Azure subscription to create the project and resource.
-
-+ On the resource, you must have the **Azure AI User** role to access model deployments and create agents. This assignment is conferred automatically for **Owners** when you create the resource. Other users need a specific role assignment.
++ On the resource, you must have the **Azure AI User** role to access model deployments and create agents. This assignment is conferred automatically for **Owners** when you create the resource. Other users need a specific role assignment. For more information, see [Role-based access control in Foundry portal](/azure/ai-foundry/concepts/rbac-azure-ai-foundry).
 
 + On the resource, you must have the **Azure AI Project Manager** role to create a project connection for MCP authentication and either **Azure AI User** or **Azure AI Project Manager** to use the MCP tool in agents.
 
 + For integrated operations, ensure your [search service identity](search-how-to-managed-identities.md) has the **Cognitive Services User** role on the resource.
 
 ---
 
-## Components of the solution
-
-This solution consists of the following integrated components:
-
-+ External data from anywhere, but we recommend [data sources used for integrated indexing](search-data-sources-gallery.md).
-
-+ Azure AI Search hosts your indexed content and provides the agentic retrieval engine (knowledge base that references a knowledge source).
-
-+ Azure OpenAI hosts an LLM used by the knowledge base and any embedding models used by vectorizers in the search index.
-
-+ Foundry hosts the agent configured with the MCP tool, as well as the project connection that stores the MCP endpoint and API credentials for agent-to-knowledge-base communication.
+## Understand the solution
 
-A user initiates query processing by interacting with a client app, such as a chatbot, that calls an agent. The agent uses the MCP tool to orchestrate requests to the knowledge base and synthesize responses. When the chatbot calls the agent, the MCP tool calls the knowledge base in Azure AI Search and sends it back to the agent and chatbot.
-
-## Development tasks
-
-Development tasks for this solution include:
+This section pairs each component of the solution with its corresponding development tasks. For deeper guidance, see the linked how-to articles.
 
 ### [Azure AI Search](#tab/search-development)
 
+Azure AI Search hosts your indexed content and the agentic retrieval pipeline. Development tasks include:
+
 + Create a [knowledge source](agentic-knowledge-source-overview.md). Agentic retrieval supports multiple types of knowledge sources, but this solution creates a [search index knowledge source](agentic-knowledge-source-how-to-search-index.md).
 
-+ [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) that maps to your LLM deployment and uses the extractive data output mode. We recommend this output mode for interaction with Foundry Agent Service because it provides the agent with verbatim, unprocessed content for grounding and reasoning. The agent is responsible for synthesizing answers and performing other tasks with this verbatim content.
++ [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) that maps to your LLM deployment and uses the extractive data output mode. We recommend this output mode for interaction with Foundry Agent Service because it provides the agent with verbatim, unprocessed content for grounding and reasoning.
 
-+ [Call the retrieve action](agentic-retrieval-how-to-retrieve.md) on the knowledge base to process a query, conversation, and override parameters.
+### [Microsoft Foundry](#tab/foundry-development)
 
-+ Parse the response for the parts you want to include in your chat application. For many scenarios, the [content portion](agentic-retrieval-how-to-retrieve.md#review-the-extracted-response) of the response is sufficient.
+Microsoft Foundry hosts your Azure OpenAI model deployments, project connection, and agent. Development tasks include:
 
-### [Microsoft Foundry](#tab/foundry-development)
++ Create a project connection that points to the MCP endpoint of your knowledge base.
 
-+ Create a project connection and an agent that uses the MCP tool.
++ Create an agent that uses the MCP tool.
 
 + Use the MCP tool to coordinate calls from the agent to the knowledge base.
 
 ---
 
-## Set up your environment
+A user initiates query processing by interacting with a client app, such as a chatbot, that calls the agent. The agent uses the MCP tool to orchestrate requests to the knowledge base and synthesize responses. When the chatbot calls the agent, the MCP tool calls the knowledge base in Azure AI Search and sends it back to the agent and chatbot.
 
-This solution combines an agentic retrieval engine built in Azure AI Search with a custom agent built in Foundry. An agent simplifies development by tracking conversation history and managing the orchestration of tool calls.
+## Build the solution
 
-For this solution, you need the following information from each resource:
+Follow these steps to create an end-to-end agentic retrieval solution.
 
-### [Azure AI Search](#tab/search-setup)
+### Get endpoints
 
-+ The endpoint for your search service, which you can find on the **Overview** page in the Azure portal. It should look like this: `https://{your-service-name}.search.windows.net/`
+For this solution, you need the following endpoints:
 
-+ An API key for your search service, which you can find on the **Keys and Endpoint** page in the Azure portal. This key is used for MCP authentication between your knowledge base and the agent in Foundry.
+#### [Azure AI Search](#tab/search-setup)
 
-### [Azure OpenAI](#tab/aoai-setup)
++ The endpoint for your search service, which you can find on the **Overview** page in the Azure portal. It should look like this: `https://{your-service-name}.search.windows.net/`
 
-+ The endpoint for your Azure OpenAI resource, which you can find on the **Keys and Endpoint** page in the Azure portal. It should look like this: `https://{your-resource-name}.openai.azure.com/`
+#### [Microsoft Foundry](#tab/foundry-setup)
 
-### [Microsoft Foundry](#tab/foundry-setup)
++ The Azure OpenAI endpoint of your project's parent resource, which you can find on the **Endpoints** page in the Azure portal. It should look like this: `https://{your-resource-name}.openai.azure.com/`
 
 + The endpoint for your project, which you can find on the **Endpoints** page in the Azure portal. It should look like this: `https://{your-resource-name}.services.ai.azure.com/api/projects/{your-project-name}`
 
 + The resource ID of your project, which you can find on the **Properties** page in the Azure portal. It should look like this: `/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.CognitiveServices/accounts/{account-name}/projects/{project-name}`
 
 ---
 
+### Create agentic retrieval objects
+
+This section omits code snippets for creating the knowledge source and knowledge base in Azure AI Search, skipping ahead to the Foundry Agent Service integration. For more information about the omitted steps, see the [Understand the solution](#understand-the-solution) section.
+
 ### Create a project connection
 
 Before you can use the MCP tool in an agent, you must create a project connection in Foundry that points to the `mcp_endpoint` of your knowledge base. This endpoint allows the agent to access your knowledge base.
 
 ```python
-from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient
-from azure.mgmt.cognitiveservices.models import ConnectionPropertiesV2BasicResource, CustomKeysConnectionProperties, CustomKeys
+import requests
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
 
+# Provide connection details
+credential = DefaultAzureCredential()
 project_resource_id = "{project_resource_id}" # e.g. /subscriptions/{subscription}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{account_name}/projects/{project_name}
-parsed = parse_resource_id(project_resource_id)
-subscription_id = parsed['subscription']
-resource_group = parsed['resource_group']
-account_name = parsed['name']
-project_name = parsed['child_name_1']
-mcp_endpoint = f"{search_service_endpoint}/knowledgebases/{knowledge_base_name}/mcp?api-version=2025-11-01-preview"
-
-mgmt_client = CognitiveServicesManagementClient(credential, subscription_id)
-resource = mgmt_client.project_connections.create(
-    resource_group_name=resource_group,
-    account_name=account_name,
-    project_name=project_name,
-    connection_name=project_connection_name,
-    connection=ConnectionPropertiesV2BasicResource(
-        properties=CustomKeysConnectionProperties(
-            category="RemoteTool",
-            target=mcp_endpoint,
-            is_shared_to_all=True,
-            metadata={ "ApiType": "Azure" },
-            credentials=CustomKeys(
-                keys={ "api-key": search_api_key }
-            )
-        )
-    )
+project_connection_name = "{project_connection_name}"
+mcp_endpoint = "{search_service_endpoint}/knowledgebases/{knowledge_base_name}/mcp?api-version=2025-11-01-preview" # This endpoint enables the MCP connection between the agent and knowledge base
+
+# Get bearer token for authentication
+bearer_token_provider = get_bearer_token_provider(credential, "https://management.azure.com/.default")
+headers = {
+  "Authorization": f"Bearer {bearer_token_provider()}",
+}
+
+# Create project connection
+response = requests.put(
+  f"https://management.azure.com{project_resource_id}/connections/{project_connection_name}?api-version=2025-10-01-preview",
+  headers = headers,
+  json = {
+    "name": "project_connection_name",
+    "type": "Microsoft.MachineLearningServices/workspaces/connections",
+    "properties": {
+      "authType": "ProjectManagedIdentity",
+      "category": "RemoteTool",
+      "target": mcp_endpoint,
+      "isSharedToAll": True,
+      "audience": "https://search.azure.com/",
+      "metadata": { "ApiType": "Azure" }
+    }
+  }
 )
 
-print(f"Connection '{resource.name}' created or updated successfully.")
+response.raise_for_status()
+print(f"Connection '{project_connection_name}' created or updated successfully.")
 ```
 
 ### Set up an AI project client
@@ -201,31 +181,36 @@ The agent definition includes instructions that specify its behavior and the pro
 ```python
 from azure.ai.projects.models import PromptAgentDefinition, MCPTool
 
+# Define agent instructions
 instructions = """
-A Q&A agent that can answer questions about the Earth at night.
+A Q&A agent that can answer questions based on the attached knowledge base.
 Always provide references to the ID of the data source used to answer the question.
-If you do not have the answer, respond with "I don't know".
+If you don't have the answer, respond with "I don't know".
 """
+
+# Create MCP tool with knowledge base connection
 mcp_kb_tool = MCPTool(
-    server_label="knowledge-base",
-    server_url=mcp_endpoint,
-    require_approval="never",
-    allowed_tools=["knowledge_base_retrieve"],
-    project_connection_id=project_connection_name
+    server_label = "knowledge-base",
+    server_url = mcp_endpoint,
+    require_approval = "never",
+    allowed_tools = ["knowledge_base_retrieve"],
+    project_connection_id = project_connection_name
 )
+
+# Create agent with MCP tool
 agent = project_client.agents.create_version(
-    agent_name=agent_name,
-    definition=PromptAgentDefinition(
-        model=agent_model,
-        instructions=instructions,
-        tools=[mcp_kb_tool]
+    agent_name = agent_name,
+    definition = PromptAgentDefinition(
+        model = agent_model,
+        instructions = instructions,
+        tools = [mcp_kb_tool]
     )
 )
 
-print(f"AI agent '{agent_name}' created or updated successfully")
+print(f"Agent '{agent_name}' created or updated successfully.")
 ```
 
-## Chat with the agent
+### Chat with the agent
 
 Your client app uses the Conversations and [Responses](/azure/ai-foundry/openai/how-to/responses) APIs from Azure OpenAI to send user input to the agent. The client creates a conversation and passes each user message to the agent through the Responses API, resembling a typical chat experience.
 
@@ -235,24 +220,25 @@ The agent manages the conversation, determines when to call your knowledge base
 # Get the OpenAI client for responses and conversations
 openai_client = project_client.get_openai_client()
 
+# Create conversation
 conversation = openai_client.conversations.create()
 
-# Send initial request that will trigger the MCP tool
+# Send request to trigger the MCP tool
 response = openai_client.responses.create(
-    conversation=conversation.id,
-    input="""
+    conversation = conversation.id,
+    input = """
         Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown?
         Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?
     """,
-    extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
+    extra_body = {"agent": {"name": agent.name, "type": "agent_reference"}},
 )
 
 print(f"Response: {response.output_text}")
 ```
 
 ## Improve data quality
 
-By default, search results from your knowledge base are consolidated into a large unified string that you can pass to the agent for grounding. Azure AI Search provides the following indexing and relevance-tuning features to help you generate high-quality results. You can implement these features in the search index, and the improvements in search relevance are evident in the quality of the response returned during retrieval.
+By default, search results from your knowledge base are consolidated into a large unified string that can be passed to the agent for grounding. Azure AI Search provides the following indexing and relevance-tuning features to help you generate high-quality results. You can implement these features in the search index, and the improvements in search relevance are evident in the quality of retrieval responses.
 
 + [Scoring profiles](index-add-scoring-profiles.md) provide built-in boosting criteria. Your index must specify a default scoring profile, which is used by the retrieval engine when queries include fields associated with that profile.
 
@@ -280,7 +266,9 @@ The Responses API controls what is sent to the agent and knowledge base. To opti
 
 For insights into the query plan, look at output tokens in the [activity array](agentic-retrieval-how-to-retrieve.md#review-the-activity-array) of knowledge base responses.
 
-## Tips for improving performance
+## Improve performance
+
+To optimize performance and reduce latency, consider the following strategies:
 
 + Summarize message threads.
 
@@ -290,7 +278,7 @@ For insights into the query plan, look at output tokens in the [activity array](
 
 ## Clean up resources
 
-When you're working in your own subscription, at the end of a project, it's a good idea to remove the resources that you no longer need. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
+When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
 
 You can also delete individual objects:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルパイプラインの作成方法に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI 検索および Foundry エージェントサービスに関するチュートリアルのドキュメントを更新したものです。主な変更点は、日付の修正、新しい情報の追加、文言の明確化、セクションの再構成です。具体的には、手順、要件、およびアクセス設定についての説明が改善されており、最新の Azure サービスとの整合性を持たせています。また、エージェントリトリーバルソリューションの各コンポーネントにおける開発タスクが明確に整理され、ユーザーが理解しやすくなっています。

特に、MCP（モデルコンテキストプロトコル）を通じた Azure AI 検索と Foundry エージェントサービスの統合に関する詳細が追加され、開発者が迅速に始められるようにサンプルコードのセクションが設けられています。この修正により、ユーザーはエージェントリトリーバル機能の実装に関して、より実用的な手引きを得ることができます。

## articles/search/cognitive-search-skill-document-intelligence-layout.md{#item-62c06f}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: reference
-ms.date: 10/21/2025
+ms.date: 11/19/2025
 ms.update-cycle: 365-days
 ---
 
@@ -40,16 +40,18 @@ This skill has the following limitations:
 
 ## Supported regions
 
-The Document Layout skill calls the [Azure Document Intelligence 2024-11-30 API](/rest/api/aiservices/operation-groups).
+The Document Layout skill calls the [Azure Document Intelligence 2024-11-30 API version V4.0](/rest/api/aiservices/operation-groups).
 
-Supported regions vary by modality and how the skill connects to the Azure Document Intelligence layout model.
+Supported regions vary by modality and how the skill connects to the Azure Document Intelligence layout model. 
 
 | Approach | Requirement |
 |----------|-------------|
 | [**Import data (new)** wizard](search-import-data-portal.md) | Create a Foundry resource in one of these regions to get the portal experience: **East US**, **West Europe**, **North Central US**. | 
 | Programmatic, using [Microsoft Entra ID authentication (preview)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) for billing |  Create Azure AI Search in one of the regions where the service is supported, according to [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table). <br>Create the Foundry resource in any region listed in the [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table) table.|
 | Programmatic, using a [Foundry resource key](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) for billing | Create your Azure AI Search service and Foundry resource in the same region. This means that the region chosen must have support for both [Azure AI Search and Azure Document Intelligence services](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table). |
 
+The implemented version of Document Layout model doesn't have support for [21Vianet](/azure/china/overview-operations) regions at this time.
+
 ## Supported file formats
 
 This skill recognizes the following file formats.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスレイアウトスキルに関する記事の更新"
}
```

### Explanation
この修正では、Azure Cognitive Searchの「ドキュメントインテリジェンスレイアウトスキル」に関連する文書が更新され、いくつかの重要な情報が追加されています。主な変更点は、日付の更新とAPIバージョンの明示化、ならびにドキュメントレイアウトモデルのサポートについての明確な説明が含まれています。

具体的には、API呼び出しに関する記述が「バージョンV4.0」を含むようになり、サポートされる地域については、特定のリソース要件が追加されています。また、21Vianet地域でのモデルの非対応についても明記され、これによってユーザーは利用可能なリソースや地域に関する理解を得やすくなっています。全体的に、ドキュメントの可読性と正確性が向上しています。

## articles/search/includes/quickstarts/agentic-retrieval-csharp.md{#item-f93ed3}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](../../search-create-service-portal.md), in any [region that provides agentic retrieval](../../search-region-support.md).
++ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md).
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azureのエージェントリトリーバルに関するC#クイックスタートガイドのドキュメントを更新したもので、主に手順と要件に関する情報が一部修正されています。具体的には、Azure AI Searchサービスの説明がわずかに修正され、文の構造が整理されています。

変更点では、Azure AI Searchサービスに関連する情報と、エージェントリトリーバルを提供する地域に関するリンクが一貫した形式で明記されました。また、Azureアカウントの作成を推奨する文が追加され、ユーザーがすぐに利用可能なリソースを持っていることを確認できるようになっています。この更新により、ドキュメントの読みやすさと明確さが向上し、ユーザーが必要な設定を把握しやすくなっています。

## articles/search/includes/quickstarts/agentic-retrieval-java.md{#item-4e2c55}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](../../search-create-service-portal.md), in any [region that provides agentic retrieval](../../search-region-support.md).
++ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md).
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects). You get a Foundry resource (that you need for model deployments) when you create a Foundry project.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するクイックスタートガイドの更新（Java版）"
}
```

### Explanation
この変更は、Azureのエージェントリトリーバルに関するJavaクイックスタートガイドのドキュメントを更新したもので、主に手順と要件に関する記述が調整されています。具体的には、Azure AI Searchサービスの説明が若干修正され、より明確な文脈が提供されています。

修正では、Azureアカウントの作成を促す文が追加され、ユーザーがリソースを簡単に取得できるようになっています。また、Azure AI Searchサービスについての情報はリンクを通じて整然と表示され、エージェントリトリーバルを提供する地域に関するヒントが強化されました。さらに、Microsoft Foundryプロジェクトやそのリソースに関する説明も更新され、ユーザーがモデルデプロイメントに必要な情報を簡単に把握できるようになっています。このアップデートにより、ドキュメントの品質と実用性が向上しています。

## articles/search/includes/quickstarts/agentic-retrieval-javascript.md{#item-715283}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](../../search-create-service-portal.md), in any [region that provides agentic retrieval](../../search-region-support.md).
++ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md).
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects). You get a Foundry resource (that you need for model deployments) when you create a Foundry project.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するクイックスタートガイドの更新（JavaScript版）"
}
```

### Explanation
この変更は、Azureのエージェントリトリーバルに関するJavaScriptのクイックスタートガイドを更新したもので、手順や要件についての記述が微調整されています。具体的には、Azure AI Searchサービスに関する情報が改良され、より明確な表現が使用されています。

変更の内容には、Azureアカウントを作成することを促す新たな文が追加され、ユーザーがリソースを簡単に入手できるよう工夫されています。また、Azure AI Searchサービスに関連する情報が整理され、エージェントリトリーバルを利用できる地域についての記載が明確になっています。さらに、Microsoft Foundryプロジェクトや、そのリソースについての情報も更新され、モデルデプロイメントに必要なリソースが自動的に提供されることが説明されています。このアップデートにより、ユーザーが必要な情報をより容易に理解できるようになり、ドキュメントの実用性が向上しています。

## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](../../search-create-service-portal.md), in any [region that provides agentic retrieval](../../search-region-support.md).
++ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md).
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するクイックスタートガイドの更新（Python版）"
}
```

### Explanation
この変更は、Azureのエージェントリトリーバルに関するPythonのクイックスタートガイドを更新したもので、ドキュメント内の手順と要件に順応性を持たせるための微調整が行われています。具体的には、新たにAzureアカウントの作成を促す文が追加され、ユーザーが必要なリソースを取得しやすくなっています。

また、Azure AI Searchサービスに関する記述が整えられ、エージェントリトリーバルをサポートしている地域についての情報が明確に示されています。さらに、Microsoft Foundryプロジェクトに関する詳細も更新され、プロジェクト作成時にリソースが自動的に作成されることに関する説明が強化されました。これにより、ユーザーは必要な情報を理解しやすく、プロジェクトの開始がスムーズになります。このアップデートは、ドキュメントの利便性と実用性を向上させるための重要な修正です。

## articles/search/includes/quickstarts/agentic-retrieval-rest.md{#item-3df373}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](../../search-create-service-portal.md), in any [region that provides agentic retrieval](../../search-region-support.md).
++ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md).
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するクイックスタートガイドの更新（REST版）"
}
```

### Explanation
この変更は、Azureのエージェントリトリーバルに関するRESTのクイックスタートガイドを更新したもので、手順や要件についての記述が微調整されています。具体的には、Azureアカウントを作成するための案内が追加され、ユーザーが必要なリソースを簡単に入手できるようになっています。

さらに、Azure AI Searchサービスに関する情報も整理され、エージェントリトリーバルを利用できる地域についての記載が明確になっています。また、Microsoft Foundryプロジェクトに関連する情報が更新され、プロジェクト作成時に自動的にリソースが作成される旨が説明されています。このアップデートにより、ユーザーが必要な情報をよりスムーズに理解できるようになり、ドキュメントの実用性が向上しています。全体的に、変更はドキュメントの明確さを改善する方向に寄与しています。

## articles/search/includes/quickstarts/agentic-retrieval-typescript.md{#item-e6370b}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](../../search-create-service-portal.md), in any [region that provides agentic retrieval](../../search-region-support.md).
++ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md).
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects). You get a Foundry resource (that you need for model deployments) when you create a Foundry project.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するクイックスタートガイドの更新（TypeScript版）"
}
```

### Explanation
この変更は、Azureのエージェントリトリーバルに関するTypeScriptのクイックスタートガイドにおける微調整を反映したものです。具体的には、Azureアカウントの作成手続きに関する案内が追加されており、ユーザーが無料でアカウントを取得できることが明記されています。

また、Azure AI Searchサービスに関する記述が整理され、エージェントリトリーバルをサポートしている地域に関する説明が明確化されています。さらに、Microsoft Foundryプロジェクトについても情報が更新され、プロジェクト作成時に必要なFoundryリソースが自動的に取得できることが強調されています。このアップデートにより、ユーザーは手順や要件をより理解しやすくなり、ドキュメントの実用性が向上しています。全体として、変更は情報の明確性と容易な理解を促進する内容となっています。

## articles/search/includes/quickstarts/full-text-csharp.md{#item-2e943a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 06/23/2025
+ms.date: 11/20/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
@@ -26,7 +26,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you must:
 
 - Assign the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
 
-## Retrieve resource information
+## Get service information
 
 [!INCLUDE [resource authentication](../resource-authentication.md)]
 
@@ -66,7 +66,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you must:
 
 In the prior [set up](#set-up) section, you created a new console application and installed the Azure AI Search client library. 
 
-In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [explaining the code](#explaining-the-code) section.
+In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [Explaining the code](#explaining-the-code) section.
 
 The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
 
@@ -606,7 +606,7 @@ In *Program.cs*, you created two clients:
 - [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient) creates the index.
 - [SearchClient](/dotnet/api/azure.search.documents.searchclient) loads and queries an existing index. 
 
-Both clients need the search service endpoint and credentials described previously in the [resource information](#retrieve-resource-information) section.
+Both clients need the search service endpoint and credentials described previously in the [Get service information](#get-service-information) section.
 
 The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フルテキスト検索に関するクイックスタートガイドの更新（C#版）"
}
```

### Explanation
この変更は、Azureのフルテキスト検索に関するC#のクイックスタートガイドを更新したもので、いくつかの文言が修正されています。具体的には、日付が更新され、リソース情報に関するセクション名が「Retrieve resource information」から「Get service information」に変更されました。この変更は、セクション名の一貫性と明確性を高めることを目的としています。

また、コードの説明セクションにおいても、見出しの表記が「explaining the code」から「Explaining the code」に修正されており、これによりタイトルのフォーマットが統一されています。その他、既存の文の改良が行われたことによって、読者が手順や情報をより容易に理解できるようになっています。このような細部の変更は、ドキュメント全体の品質向上に寄与するものです。全体として、修正は内容の明瞭さと一貫性を改善しています。

## articles/search/includes/quickstarts/full-text-java.md{#item-d659f9}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 06/23/2025
+ms.date: 11/20/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
@@ -26,7 +26,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you must:
 
 - Assign the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
 
-## Retrieve resource information
+## Get service information
 
 [!INCLUDE [resource authentication](../resource-authentication.md)]
 
@@ -98,7 +98,7 @@ The sample in this quickstart works with the Java Runtime. Install a Java Develo
 
 In the prior [set up](#set-up) section, you installed the Azure AI Search client library and other dependencies. 
 
-In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [explaining the code](#explaining-the-code) section.
+In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [Explaining the code](#explaining-the-code) section.
 
 The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フルテキスト検索に関するクイックスタートガイドの更新（Java版）"
}
```

### Explanation
この変更は、Azureのフルテキスト検索に関するJavaのクイックスタートガイドにおける微調整を反映したものです。主な改訂点として、日付が更新され、リソース情報に関するセクション名が「Retrieve resource information」から「Get service information」に変更されました。この変更は、情報をより理解しやすくすることを目的としています。

さらに、コードを説明するセクションの見出しが「explaining the code」から「Explaining the code」に変更され、大文字表記が適用されています。また、内容の他の部分でもわずかな文言の修正が行われ、使用する言語の一貫性が向上しています。これにより、読者は手順をよりスムーズに追いやすくなり、全体の理解率が向上することが期待されます。修正全体は、ドキュメントの明瞭さと整合性を強化しています。

## articles/search/includes/quickstarts/full-text-javascript.md{#item-568e3a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 06/23/2025
+ms.date: 11/20/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
@@ -26,7 +26,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you must:
 
 - Assign the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
 
-## Retrieve resource information
+## Get service information
 
 [!INCLUDE [resource authentication](../resource-authentication.md)]
 
@@ -62,7 +62,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you must:
 
 In the prior [set up](#set-up) section, you installed the Azure AI Search client library and other dependencies. 
 
-In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [explaining the code](#explaining-the-code) section.
+In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [Explaining the code](#explaining-the-code) section.
 
 The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フルテキスト検索に関するクイックスタートガイドの更新（JavaScript版）"
}
```

### Explanation
この変更は、Azureのフルテキスト検索に関するJavaScriptのクイックスタートガイドを更新したもので、いくつかの小さな修正が行われています。主な更新としては、日付が「06/23/2025」から「11/20/2025」に変更されており、最新の情報を反映しています。

また、リソース情報に関するセクション名が「Retrieve resource information」から「Get service information」に変更され、より直感的で理解しやすい表現に改善されています。さらに、コード説明セクションの見出しも「explaining the code」から「Explaining the code」に修正され、大文字の始まりを示すことで、一貫性を持たせています。このような細部の変更は、文書の質を高め、読者が情報をより効率的に利用できるようにすることを目的としています。全体として、更新はドキュメントの明瞭さと整合性を向上させるための努力を反映したものです。

## articles/search/includes/quickstarts/full-text-python.md{#item-9bba1c}

<details>
<summary>Diff</summary>
````diff
@@ -4,13 +4,13 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 06/23/2025
+ms.date: 11/20/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
 
 > [!TIP]
-> You can download and run a [finished notebook](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart).
+> You can download the [source code](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart)  to start with a finished project or follow these steps to create your own.
 
 ## Prerequisites
 
@@ -28,7 +28,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you must:
 
 - Assign the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
 
-## Retrieve resource information
+## Get service information
 
 [!INCLUDE [resource authentication](../resource-authentication.md)]
 
@@ -85,7 +85,7 @@ You run the sample code in a Jupyter notebook. So, you need to set up your envir
 
 ## Create, load, and query a search index
 
-In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [explaining the code](#explaining-the-code) section.
+In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [Explaining the code](#explaining-the-code) section.
 
 1. Make sure the notebook is open in the `.venv` kernel as described in the previous section.
 1. Run the first code cell to install the required packages, including [azure-search-documents](/python/api/azure-search-documents). 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フルテキスト検索に関するクイックスタートガイドの更新（Python版）"
}
```

### Explanation
この変更は、Azureのフルテキスト検索に関するPythonのクイックスタートガイドの微調整を反映しています。主な修正内容は、日付が「06/23/2025」から「11/20/2025」に変更され、最新のリリース情報を反映しています。

さらに、読者に提供される情報に関して、ダウンロード可能なノートブックの説明が「You can download and run a [finished notebook]」から「You can download the [source code] to start with a finished project or follow these steps to create your own.」に変更され、より具体的かつ明確な指示が提供されています。

リソース情報に関するセクション名も「Retrieve resource information」から「Get service information」に変更され、直感的な表現になっています。また、コードを説明するセクションの見出しが「explaining the code」から「Explaining the code」に変わり、大文字表記が適用されています。これらの変更は、読者が情報をより理解しやすくするためのものであり、文書の一貫性と明瞭性を向上させることを目的としています。全体として、更新は重要な情報を強調し、より質の高いリソースを提供しています。

## articles/search/includes/quickstarts/full-text-typescript.md{#item-6630e8}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 06/13/2025
+ms.date: 11/20/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
@@ -25,7 +25,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you must:
 
 - Assign the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
 
-## Retrieve resource information
+## Get service information
 
 [!INCLUDE [resource authentication](../resource-authentication.md)]
 
@@ -66,7 +66,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you must:
 
 In the prior [set up](#set-up) section, you installed the Azure AI Search client library and other dependencies. 
 
-In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [explaining the code](#explaining-the-code) section.
+In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [Explaining the code](#explaining-the-code) section.
 
 The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フルテキスト検索に関するクイックスタートガイドの更新（TypeScript版）"
}
```

### Explanation
この変更は、Azureのフルテキスト検索に関するTypeScriptのクイックスタートガイドに対する微細な更新を示しています。主な修正として、日付が「06/13/2025」から「11/20/2025」に変更され、最新の情報を反映しています。

また、リソース情報に関するセクション名が「Retrieve resource information」から「Get service information」に変更されており、より明確で直感的な表現に改善されています。さらに、コードを説明するセクションの見出しも「explaining the code」から「Explaining the code」に変更され、大文字が用いられることで一貫性が保たれています。

これらの変更は、読者が必要な情報をより簡単に見つけ、理解しやすくすることを目的としています。全体として、この更新は文書の整合性と明瞭さを向上させ、より品質の高いリソースを提供しようとする努力を反映しています。

## articles/search/includes/quickstarts/search-get-started-rag-rest.md{#item-aa7f2b}

<details>
<summary>Diff</summary>
````diff
@@ -89,7 +89,7 @@ In this quickstart, you use a REST client and the [Azure AI Search REST APIs](/r
 We recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for this quickstart.
 
 > [!TIP]
-> You can [download the source code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-rag) to start with a finished project or follow these steps to create your own. 
+> You can download the [source code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-rag) to start with a finished project or follow these steps to create your own. 
 
 1. Start Visual Studio Code and open the [quickstart-rag.rest](https://github.com/Azure-Samples/azure-search-rest-samples/blob/main/Quickstart-RAG/rag.rest) file or create a new file.
 
@@ -108,7 +108,7 @@ We recommend [Visual Studio Code](https://code.visualstudio.com/download) with a
     Authorization: Bearer {{personalAccessToken}}
    ```
 
-1. Select **Sent request**.
+1. Select **Send Request**.
 
    :::image type="content" source="../../media/search-get-started-semantic/visual-studio-code-send-request.png" alt-text="Screenshot of the REST client send request link.":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azure AI SearchのREST APIを使用するクイックスタートガイドの微調整を示しています。主な修正点は、ユーザーに対してより明確な指示を提供するための用語の修正です。

具体的には、「Sent request」というフレーズが「Send Request」に変更されており、これにより操作がより直感的に理解できるようになっています。また、ソースコードのダウンロードに関する記述は元の内容から変更がありませんが、レイアウトや一貫性の向上を目的として微調整が行われた可能性があります。

全体として、これらの変更は、読者がガイドを使用する際の体験を向上させ、より明確で使いやすいリソースを提供することを目的としています。

## articles/search/includes/quickstarts/search-get-started-rbac-python.md{#item-de7760}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 07/09/2025
+ms.date: 11/20/2025
 ---
 
 In this quickstart, you use role-based access control (RBAC) and Microsoft Entra ID to establish a keyless connection to your Azure AI Search service. You then use Python in Visual Studio Code to interact with your service.
@@ -33,13 +33,13 @@ To sign in:
 
 1. On your local system, open a command-line tool.
 
-1. Check for the active tenant and subscription in your local environment.
+1. Check the active subscription and tenant in your local environment.
 
    ```azurecli
    az account show
    ```
 
-1. If the active subscription and tenant aren't valid for your search service, change the variables. You can check for the subscription ID on the search service overview page in the Azure portal. You can check for the tenant ID by clicking through to the subscription. In the Azure portal, the tenant ID is referred to as the **Parent management group**. Make a note of the values that are valid for your search service and run the following commands to update your local environment.
+1. If the active subscription and tenant aren't valid for your search service, run the following commands to update their values. You can find the subscription ID on the search service **Overview** page in the Azure portal. To find the tenant ID, select the name of your subscription on the **Overview** page, and then locate the **Parent management group** value.
 
    ```azurecli
     az account set --subscription <your-subscription-id>
@@ -71,17 +71,17 @@ To connect using Python:
    ```python
    from azure.identity import DefaultAzureCredential
    from azure.search.documents.indexes import SearchIndexClient
-    
+   
    service_endpoint = "PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE"
    credential = DefaultAzureCredential()
-   client = SearchIndexClient(endpoint=service_endpoint, credential=credential)
+   client = SearchIndexClient(endpoint = service_endpoint, credential = credential)
     
    # List existing indexes
    indexes = client.list_indexes()
     
    for index in indexes:
       index_dict = index.as_dict()
-      print(json.dumps(index_dict, indent=2))
+      print(json.dumps(index_dict, indent = 2))
    ```
 
 1. Set `service_endpoint` to the value you obtained in [Get service information](#get-service-information).
@@ -94,7 +94,7 @@ To connect using Python:
 
 If you encounter a 401 error, follow these troubleshooting steps:
 
-+ Revisit [Configure role-based access](#configure-role-based-access). Your search service must have **Role-based access control** or **Both** enabled. Policies at the subscription or resource group level might also override your role assignments.
++ Revisit [Configure role-based access](#configure-role-based-access). Your search service must have **Role-based access control** or **Both** enabled. Policies at the subscription or resource group level might override your role assignments.
 
 + Revisit [Sign in to Azure](#sign-in-to-azure). You must sign in to the subscription that contains your search service.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PythonによるRBACを使用したAzure AI Searchのクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Pythonを使用してAzure AI Searchサービスに役立つRBAC（Role-Based Access Control）を設定するためのクイックスタートガイドの更新を示しています。主な修正点は、文中の用語や説明のクリアさを向上させるための微調整です。

具体的には、日付が「07/09/2025」から「11/20/2025」に変更され、ドキュメントが最新の情報を反映するようになっています。また、「Check for the active tenant and subscription」という表現が「Check the active subscription and tenant」に修正され、さらなる明確さが加わっています。

さらに、コードブロック内でのスペースの配置が統一され、視認性が向上しています。例えば、`endpoint=credential`の前後にスペースが挿入されることで一貫性が保たれています。最後に、「Revisit [Sign in to Azure]」に新しい文が追加され、検索サービスにサインインする必要性が強調されています。

これらの変更は、エンドユーザーが手順を理解しやすくし、スムーズにAzure AI Searchを利用できるように設計されています。全体として、文書の明瞭さと使いやすさが向上し、クイックスタートの効果が増しています。

## articles/search/includes/quickstarts/search-get-started-rbac-rest.md{#item-fd8ef4}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 08/13/2025
+ms.date: 11/20/2025
 ---
 
 In this quickstart, you use role-based access control (RBAC) and Microsoft Entra ID to establish a keyless connection to your Azure AI Search service. You then use REST in Visual Studio Code to interact with your service.
@@ -29,13 +29,17 @@ Keyless connections provide enhanced security through granular permissions and i
 
 Before you connect to your Azure AI Search service, use the Azure CLI to sign in to the subscription that contains your service.
 
-1. Check for the active tenant and subscription in your local environment.
+To sign in:
+
+1. On your local system, open a command-line tool.
+
+1. Check the active subscription and tenant in your local environment.
 
    ```azurecli
    az account show
    ```
 
-1. If the active subscription and tenant aren't valid for your search service, change the variables. You can check for the subscription ID on the search service overview page in the Azure portal. You can check for the tenant ID by clicking through to the subscription. In the Azure portal, the tenant ID is referred to as the **Parent management group**. Make a note of the values that are valid for your search service and run the following commands to update your local environment.
+1. If the active subscription and tenant aren't valid for your search service, run the following commands to update their values. You can find the subscription ID on the search service **Overview** page in the Azure portal. To find the tenant ID, select the name of your subscription on the **Overview** page, and then locate the **Parent management group** value.
 
    ```azurecli
     az account set --subscription <your-subscription-id>
@@ -49,15 +53,13 @@ REST API calls require the inclusion of a Microsoft Entra ID token. You use this
 
 To get your token:
 
-1. On your local system, open a command-line tool.
-
-1. Generate an access token.
+1. Using the same command-line tool, generate an access token.
 
    ```azurecli
    az account get-access-token --scope https://search.azure.com/.default --query accessToken --output tsv
    ```
 
-1. Copy the token output.
+1. Make a note of the token output.
 
 ## Connect to Azure AI Search
 
@@ -72,7 +74,7 @@ To connect using REST:
 
 1. Create a `.rest` or `.http` file.
 
-1. Paste the following placeholders and request into the file.
+1. Paste the following variables and request into the file.
 
    ```http
    @baseUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
@@ -84,9 +86,9 @@ To connect using REST:
       Authorization: Bearer {{token}}
    ```
 
-1. Replace `@baseUrl` with the value you obtained in [Get service information](#get-service-information).
+1. Set `@baseUrl` to the value you obtained in [Get service information](#get-service-information).
 
-1. Replace `@token` with the value you obtained in [Get token](#get-token).
+1. Set `@token` to the value you obtained in [Get token](#get-token).
 
 1. Under `### List existing indexes`, select **Send Request**.
 
@@ -96,12 +98,12 @@ To connect using REST:
 
 If you encounter a 401 error, follow these troubleshooting steps:
 
-+ Revisit [Configure role-based access](#configure-role-based-access). Your search service must have **Role-based access control** or **Both** enabled. Policies at the subscription or resource group level might also override your role assignments.
++ Revisit [Configure role-based access](#configure-role-based-access). Your search service must have **Role-based access control** or **Both** enabled. Policies at the subscription or resource group level might override your role assignments.
 
-+ Revisit [Get token](#get-token). You must sign in to the subscription that contains your search service.
++ Revisit [Sign in to Azure](#sign-in-to-azure). You must sign in to the subscription that contains your search service.
 
 + Make sure your endpoint and token variables don't have surrounding quotes or extra spaces.
 
 + Make sure your token doesn't have the `@` symbol in the request header. For example, if the variable is `@token`, the reference in the request should be `{{token}}`.
 
-+ If all else fails, restart your device to remove cached tokens and then repeat the steps in this quickstart, starting with [Get token](#get-token).
++ If all else fails, restart your device to remove cached tokens and then repeat the steps in this quickstart, starting with [Sign in to Azure](#sign-in-to-azure).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACを使用したAzure AI SearchへのREST接続に関するクイックスタートガイドの更新"
}
```

### Explanation
このコード変更は、Azure AI Searchサービスに対するRBAC（Role-Based Access Control）を利用したREST接続のためのクイックスタートガイドに関する更新を示しています。主に手順の明確化と内容の整理が行われています。

変更点では、ドキュメントの日付が「08/13/2025」から「11/20/2025」に更新され、より正確な情報が反映されています。また、サインイン手順の項目が整理され、最初に「To sign in:」という見出しが追加され、手順が段階的に提示されるようになっています。これにより、ユーザーは各ステップを視覚的に追いやすくなっています。

具体的には、コマンドラインツールの使用に関する説明が統一され、「generate an access token」から「Using the same command-line tool, generate an access token」という形に変更され、流れがスムーズになっています。さらに、変数に関する表現も「Paste the following placeholders and request into the file」から「Paste the following variables and request into the file」に変更され、より正確な表現に修正されています。

トラブルシューティングセクションでは、サインイン関連の指示がより明確になり、「Revisit [Sign in to Azure]」としてサインインの重要性が強調されています。加えて、EndpointやTokenの設定に対する具体的な注意点も追加されており、ユーザーがエラーを避けやすくなっています。

全体として、この更新はユーザーがAzure AI Searchサービスにアクセスする際の体験を向上させることを目的としており、手順の明確さを向上させています。

## articles/search/includes/quickstarts/search-get-started-vector-dotnet.md{#item-8f2f1b}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: rotabor
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 06/19/2025
+ms.date: 11/20/2025
 ---
 
 In this quickstart, you work with a .NET app to create, populate, and query vectors. The code examples perform these operations by using the [Azure AI Search client library](/dotnet/api/overview/azure/search). The library provides an abstraction over the REST API for access to index operations such as data ingestion, search operations, and index management operations.
@@ -26,9 +26,7 @@ In Azure AI Search, a [vector store](../../vector-store.md) has an index schema
 
 - [Git](https://git-scm.com/downloads) to clone the sample repo.
 
----
-
-## Retrieve resource information
+## Get service information
 
 Requests to the search endpoint must be authenticated and authorized. While it's possible to use API keys or roles for this task, we recommend [using a keyless connection via Microsoft Entra ID](../../search-get-started-rbac.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": ".NETアプリを使用したベクトル操作に関するクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchを使用してベクトルを操作するための.NETアプリのクイックスタートガイドの更新を示しています。主な変更内容は、日付の更新とセクションタイトルの変更です。

まず、ドキュメントの日付が「06/19/2025」から「11/20/2025」に変更され、最新の情報が反映されています。次に、セクションタイトルが「Retrieve resource information」から「Get service information」に変更されています。この変更により、ユーザーがこのセクションで何を学ぶのかが明確になり、情報が整理されています。

また、要点としては、Azure AI Searchのエンドポイントへのリクエストが認証および承認される必要があり、APIキーやロールを使用する方法もありますが、Microsoft Entra IDを介したキーレス接続の使用が推奨されています。これにより、セキュリティと使いやすさが向上します。

全体として、この更新はユーザーがAzure AI Searchを利用する際の理解を深め、操作手順をクリアにすることを目指しています。

## articles/search/includes/quickstarts/search-get-started-vector-java.md{#item-a3db97}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ ms.author: karler
 ms.service: azure-ai-search
 ms.custom: devx-track-java
 ms.topic: include
-ms.date: 09/08/2025
+ms.date: 11/20/2025
 ai-usage: ai-assisted
 ---
 
@@ -28,8 +28,6 @@ In Azure AI Search, a [vector store](../../vector-store.md) has an index schema
 
 - [Maven](https://maven.apache.org/download.cgi).
 
----
-
 ## Get service endpoints
 
 In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints so that you can provide them as variables in your code.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaを使用したベクトル操作に関するクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchを使ってベクトルを操作するためのJavaアプリのクイックスタートガイドに関する更新です。変更内容は主に日付の更新といくつかの文言の修正です。

具体的には、ドキュメントの日付が「09/08/2025」から「11/20/2025」に変更され、最新のリリース日が反映されています。この変更により、ユーザーは最新の情報を得ることができます。

さらに、「Get service endpoints」というセクションが強調され、ユーザーがAzure OpenAIおよびAzure AI Searchに対するAPI呼び出しを設定するためのサービスエンドポイントの取得方法について説明しています。この部分は、ユーザーがコード内で使用する変数としてサービスエンドポイントを提供する準備をするための重要なステップです。

全体として、この更新はJavaを使用したAzure AI Searchの体験を改善し、ユーザーがよりスムーズにベクトル操作を行えるようにすることを目的としています。

## articles/search/includes/quickstarts/search-get-started-vector-javascript.md{#item-d0387c}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: diberry
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 06/30/2025
+ms.date: 11/20/2025
 ---
 
 In this quickstart, you use JavaScript to create, load, and query vectors. The code examples perform these operations by using the [Azure AI Search client library](/javascript/api/overview/azure/search-documents-readme). The library provides an abstraction over the REST API for access to index operations such as data ingestion, search operations, and index management operations.
@@ -27,8 +27,6 @@ In Azure AI Search, a [vector store](../../vector-store.md) has an index schema
 
 - [Node.JS with LTS](https://nodejs.org/en/download/).
 
----
-
 ## Get service endpoints
 
 In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints so that you can provide them as variables in your code.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptを使用したベクトル操作に関するクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchを利用してベクトルを操作するためのJavaScriptアプリのクイックスタートガイドに関する更新を示しています。主な変更点は、日付の更新と一部の文言の修正です。

具体的には、文書の日付が「06/30/2025」から「11/20/2025」へと変更され、最新のリリース日が反映されています。この更新により、必ず最新の情報がユーザーに提供されます。

また、「Get service endpoints」というセクションが記載されており、このセクションではAzure OpenAIおよびAzure AI Searchに対するAPI呼び出しの設定方法が説明されています。この手順により、ユーザーはコード内で利用するサービスエンドポイントを変数として取得できるようになります。

全体として、この更新はJavaScriptを利用したAzure AI Searchの体験を向上させ、ユーザーがベクトル操作をより効率的に行えるようにすることを目的としています。

## articles/search/includes/quickstarts/search-get-started-vector-python.md{#item-53085f}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: rotabor
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 06/19/2025
+ms.date: 11/20/2025
 ---
 
 In this quickstart, you use a Jupyter notebook to create, load, and query vectors. The code examples perform these operations by using the [Azure AI Search client library](/python/api/overview/azure/search-documents-readme). The library provides an abstraction over the REST API for access to index operations such as data ingestion, search operations, and index management operations.
@@ -26,9 +26,7 @@ In Azure AI Search, a [vector store](../../vector-store.md) has an index schema
 
 - [Git](https://git-scm.com/downloads) to clone the repo containing the Jupyter notebook and other related files.
 
----
-
-## Retrieve resource information
+## Get service information
 
 Requests to the search endpoint must be authenticated and authorized. While it's possible to use API keys or roles for this task, we recommend [using a keyless connection via Microsoft Entra ID](../../search-get-started-rbac.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonを使用したベクトル操作に関するクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchを使用してベクトルを操作するPythonアプリのクイックスタートガイドに関する更新を示しています。主な変更は日付の更新とセクションタイトルの変更、ならびにいくつかの文言の修正です。

具体的には、文書の日付が「06/19/2025」から「11/20/2025」に変更され、最新のリリース日が反映されています。この更新により、ユーザーは最新の情報に基づいて操作を進めることができます。

さらに、「Retrieve resource information」というセクションのタイトルが「Get service information」に変更され、このセクションでは検索エンドポイントへのリクエストが認証され、権限を持っている必要があることが強調されています。また、APIキーやロールを使う方法も述べられている一方で、Microsoft Entra IDを介したキーなし接続を推奨しています。

これらの変更により、Pythonを使用したAzure AI Searchに関するクイックスタートガイドは、ユーザーがベクトル操作をより効率的かつ安全に行うための最新で明確な情報を提供することを目的としています。

## articles/search/includes/quickstarts/search-get-started-vector-rest.md{#item-c7d261}

<details>
<summary>Diff</summary>
````diff
@@ -4,10 +4,9 @@ author: haileytapia
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 06/19/2025
+ms.date: 11/20/2025
 ---
 
-
 In this quickstart, you use the [Azure AI Search REST APIs](/rest/api/searchservice) to create, load, and query vectors.
 
 In Azure AI Search, a [vector store](../../vector-store.md) has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. The [Create Index](/rest/api/searchservice/indexes/create-or-update) REST API creates the vector store.
@@ -25,10 +24,7 @@ In Azure AI Search, a [vector store](../../vector-store.md) has an index schema
 
 - [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
----
-
-
-## Retrieve resource information
+## Get service information
 
 Requests to the search endpoint must be authenticated and authorized. You can use API keys or roles for this task. We recommend [using a keyless connection via Microsoft Entra ID](../../search-get-started-rbac.md).
 
@@ -38,7 +34,7 @@ Select the tab that corresponds to your preferred authentication method. Use the
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch).
 
-1. On the **Overview** home page, find the URL. An example endpoint might look like `https://mydemo.search.windows.net`. 
+1. On the **Overview** home page, find the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
 
    :::image type="content" source="../../media/search-get-started-rest/get-endpoint.png" lightbox="../../media/search-get-started-rest/get-endpoint.png" alt-text="Screenshot of the URL property on the overview page.":::
 
@@ -71,14 +67,14 @@ You use one `.rest` or `.http` file to run all the requests in this quickstart.
 
 1. In Visual Studio Code, create a new file with a `.rest` or `.http` file extension. For example, `az-search-vector-quickstart.rest`. Copy and paste the raw contents of the [Azure-Samples/azure-search-rest-samples/blob/main/Quickstart-vectors/az-search-vector-quickstart.rest](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) file into this new file. 
 
-1. At the top of the file, replace the placeholder value for `@baseUrl` with your search service URL. See the [Retrieve resource information](#retrieve-resource-information) section for instructions on how to find your search service URL.
+1. At the top of the file, replace the placeholder value for `@baseUrl` with your search service URL. See the [Get service information](#get-service-information) section for instructions on how to find your search service URL.
 
 
    ```http
    @baseUrl = PUT-YOUR-SEARCH-SERVICE-URL-HERE
    ```
 
-1. At the top of the file, replace the placeholder value for authentication. See the [Retrieve resource information](#retrieve-resource-information) section for instructions on how to get your Microsoft Entra token or API key.
+1. At the top of the file, replace the placeholder value for authentication. See the [Get service information](#get-service-information) section for instructions on how to get your Microsoft Entra token or API key.
 
     For the **recommended** keyless authentication via Microsoft Entra ID, you need to replace `@apiKey` with the `@token` variable.
 
@@ -283,7 +279,7 @@ The index schema in this example is organized around hotel content. Sample data
     }
     ```
 
-1. Select **Send request**. You should have an `HTTP/1.1 201 Created` response. 
+1. Select **Send Request**. You should have an `HTTP/1.1 201 Created` response. 
 
     The response body should include the JSON representation of the index schema.
     
@@ -641,7 +637,7 @@ In Azure AI Search, the index contains all searchable data and queries run on th
     }
     ```
 
-1. Select **Send request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search documents.
+1. Select **Send Request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search documents.
 
 Key takeaways about the [Documents - Index REST API](/rest/api/searchservice/documents/) request:
 
@@ -702,7 +698,7 @@ The vector query string is semantically similar to the search string, but it inc
 
     + `k` specifies the number of matches to return in the response. A `count` parameter specifies the number of matches found in the index. Including count is a best practice for queries, but it's less useful for similarity search where the algorithm can find some degree of similarity in almost any document. 
 
-1. Select **Send request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
+1. Select **Send Request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
 
     The response for the vector equivalent of `quintessential lodging near running trails, eateries, retail` includes k-5 results although the search engine found 7 matches. The top results are considered the most semantically similar to the query. Each result provides a search score and the fields listed in `select`. In a similarity search, the response always includes `k` results ordered by the value similarity score.
     
@@ -805,7 +801,7 @@ You can add filters, but the filters are applied to the nonvector content in you
     }
     ```
 
-1. Select **Send request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
+1. Select **Send Request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
 
     The query was the same as the previous [single vector search example](#single-vector-search), but it includes a post-processing exclusion filter and returns only the two hotels that have free Wi-Fi.
     
@@ -938,7 +934,7 @@ Hybrid search consists of keyword queries and vector queries in a single search
     }
     ```
 
-1. Select **Send request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
+1. Select **Send Request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
 
 Because this is a hybrid query, results are [ranked by Reciprocal Rank Fusion (RRF)](../../hybrid-search-ranking.md#scores-in-a-hybrid-search-results). Notice that `@search.score` values have a different basis and are uniformly smaller values. RRF evaluates search scores of multiple search results, takes the inverse, and then merges and sorts the combined results. The `top` number of results are returned.
 
@@ -1056,7 +1052,7 @@ Here's the last query in the collection. This hybrid query adds L2 semantic rank
     }
     ```
 
-1. Select **Send request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
+1. Select **Send Request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
 
 Review the response, consisting of a semantic reranking of the RRF-ranked results of the hybrid query. Semantic ranking works off of text inputs. In a text or hybrid query, this input is the text portion of the query (*historic hotel walk to restaurants and shopping*). To use semantic ranking on a pure vector query, such as the first example, or to explicitly control the text used for semantic ranking, [provide a semanticQuery string](../../semantic-how-to-query-request.md#set-up-the-query).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIを使用したベクトル操作に関するクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azure AI SearchのREST APIを使用してベクトルを操作するためのクイックスタートガイドに対する更新を示しています。主な変更点は、日付の更新、セクションタイトルの変更、及び文言の修正です。

具体的には、「06/19/2025」から「11/20/2025」への日付更新が行われ、最新のリリース日が反映されています。また、「Retrieve resource information」というセクションのタイトルが「Get service information」に変更され、内容が最新の手法に合わせて調整されています。

この更新には、サービスエンドポイントへのリクエストが認証される必要があることが強調されており、APIキーや役割を使用する方法が記載されていますが、Microsoft Entra IDを使用したキーなし接続が推奨されています。

さらに、いくつかの指示文やセクションタイトルが変更されており、特に「Send request」という表現が「Send Request」に統一されるなど、内容の一貫性が保たれています。

全体的に、この更新はユーザーがAzure AI SearchのREST APIを使用してベクトル操作をより効果的に行えるよう、最新の情報と明確な手順を提供することを目的としています。

## articles/search/includes/quickstarts/search-get-started-vector-typescript.md{#item-9b3bc8}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: diberry
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 06/30/2025
+ms.date: 11/20/2025
 ---
 
 In this quickstart, you use TypeScript to create, load, and query vectors. The code examples perform these operations by using the [Azure AI Search client library](/javascript/api/overview/azure/search-documents-readme). The library provides an abstraction over the REST API for access to index operations such as data ingestion, search operations, and index management operations.
@@ -32,8 +32,6 @@ In Azure AI Search, a [vector store](../../vector-store.md) has an index schema
    npm install -g typescript
    ```
 
----
-
 ## Get service endpoints
 
 In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints so that you can provide them as variables in your code.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptを使用したベクトル操作に関するクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchを使用してTypeScriptでベクトルを操作するクイックスタートガイドに対する軽微な更新を示しています。主な変更点は日付の更新と、不要な文の削除です。

具体的には、ドキュメントの日付が「06/30/2025」から「11/20/2025」に変更され、最新のリリース日が反映されています。この改善により、ユーザーは最新の情報に基づいて学習を進めることができます。

また、「Get service endpoints」というセクションについては、タイトルと内容が短縮され、不要な説明が削除されています。これにより、ガイドがより簡潔に、必要な情報に焦点を当てる形になっています。

全体として、この更新は、ユーザーがTypeScriptを使用してAzure AI Searchでのベクトル操作をスムーズに行うための最新の情報を提供することを目的としています。

## articles/search/includes/quickstarts/semantic-ranker-csharp.md{#item-09fa32}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: include
-ms.date: 07/03/2025
+ms.date: 11/20/2025
 ---
 
 [!INCLUDE [Semantic ranker introduction](semantic-ranker-intro.md)]
@@ -17,7 +17,7 @@ In this quickstart, you use an IDE and the [**Azure.Search.Documents**](/dotnet/
 We recommend [Visual Studio](https://visualstudio.microsoft.com/vs/community/) for this quickstart.
 
 > [!TIP]
-> You can [download the source code](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-semantic-search) to start with a finished project or follow these steps to create your own. 
+> You can download the [source code](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-semantic-search) to start with a finished project or follow these steps to create your own.
 
 ### Install libraries
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#によるセマンティックランカーのクイックスタートガイドの更新"
}
```

### Explanation
この変更は、C#を使用したセマンティックランカーに関するクイックスタートガイドにおける軽微な修正を示しています。主に、日付の更新とテキストのわずかな調整が行われています。

具体的には、ドキュメントの日付が「07/03/2025」から「11/20/2025」に変更され、最新の情報が反映されています。これにより、ユーザーは最新のリリース情報に基づいて手順を実行できるようになります。

また、注釈の部分で、「You can [download the source code]」という文が、リンクのフォーマットが若干変更されており、より明確に記載されています。これにより、ユーザーがソースコードをダウンロードする手順がわかりやすくなっています。

全体的に、この更新は、C#を使用したAzure AI Searchのセマンティックランカーの利用方法をより効果的に伝えることを目的としています。

## articles/search/includes/quickstarts/semantic-ranker-intro.md{#item-538e0f}

<details>
<summary>Diff</summary>
````diff
@@ -4,72 +4,74 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 06/27/2025
+ms.date: 11/20/2025
 ---
 
-In this quickstart, you learn how to add semantic ranking to an existing index. You can use the hotels-sample-index or one of your own.
+In this quickstart, you learn how to use [semantic ranking](../../semantic-search-overview.md) by adding a semantic configuration to a search index and adding semantic parameters to a query. You can use the hotels-sample-index or one of your own.
 
-In Azure AI Search, [semantic ranking](../../semantic-search-overview.md) is query-side functionality that uses machine reading comprehension from Microsoft to rescore search results, promoting the most semantically relevant matches to the top of the list. Depending on the content and the query, semantic ranking can [significantly improve search relevance](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-outperforming-vector-search-with-hybrid/ba-p/3929167) with minimal developer effort. 
+In Azure AI Search, semantic ranking is query-side functionality that uses machine reading comprehension from Microsoft to rescore search results, promoting the most semantically relevant matches to the top of the list. Depending on the content and the query, semantic ranking can [significantly improve search relevance](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-outperforming-vector-search-with-hybrid/ba-p/3929167) with minimal developer effort.
 
 You can add a semantic configuration to an existing index with no rebuild requirement. Semantic ranking is most effective on text that's informational or descriptive.
 
-In this quickstart, you learn how to:
-
-> [!div class="checklist"]
-> + Add a semantic configuration to a search index
-> + Add semantic parameters to a query
-
 ## Prerequisites
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](../../search-create-service-portal.md), at Basic tier or higher, with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
++ An [Azure AI Search service](../../search-create-service-portal.md) with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
 
-+ A [new or existing index](../../search-how-to-create-search-index.md) with descriptive or verbose text fields, attributed as retrievable in your index. This quickstart assumes the [hotels-sample-index](../../search-get-started-portal.md).
++ A [new or existing index](../../search-how-to-create-search-index.md) with descriptive or verbose text fields that are attributed as retrievable. This quickstart assumes the [hotels-sample-index](../../search-get-started-portal.md).
 
 ## Configure access
 
-You can connect to your Azure AI Search service [using API keys](../../search-security-api-keys.md) or Microsoft Entra ID with role assignments. Keys are easier to start with, but roles are more secure.
+You can connect to your Azure AI Search service using API keys or Microsoft Entra ID with role assignments. Keys are easier to start with, but roles are more secure. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
 
 To configure role-based access:
 
 1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
 
 1. From the left pane, select **Settings** > **Keys**.
 
-1. Under **API Access control**, select **Both**.
-
-   This option enables both key-based and keyless authentication. After you assign roles, you can return to this step and select **Role-based access control**.
+1. Under **API Access control**, select **Role-based access control** or **Both** if you need time to transition clients to role-based access.
 
 1. From the left pane, select **Access control (IAM)**.
 
 1. Select **Add** > **Add role assignment**.
 
-1. Assign these roles to your user account:
-
-   + **Search Service Contributor**
-
-   + **Search Index Data Contributor**
-
-For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
+1. Assign the **Search Service Contributor** and **Search Index Data Contributor** roles to your user account.
 
 ## Start with an index
 
-This quickstart assumes an existing index, modified to include a semantic configuration. We recommend the [hotels-sample-index](../../search-get-started-portal.md) that you can create in minutes using an Azure portal wizard.
+This quickstart assumes an existing index and modifies it to include a semantic configuration. We recommend the [hotels-sample-index](../../search-get-started-portal.md) that you can create in minutes using an Azure portal wizard.
+
+To start with an existing index:
 
 1. Sign in to the [Azure portal](https://portal.azure.com/) and find your search service.
 
-1. Under **Search management** > **Indexes**, open the hotels-sample-index. Make sure the index doesn't have a semantic configuration.
+1. Under **Search management** > **Indexes**, select the hotels-sample-index.
+
+1. Select **Semantic configurations** to ensure the index doesn't have a semantic configuration.
 
    :::image type="content" source="../../media/search-get-started-semantic/no-semantic-configuration.png" alt-text="Screenshot of an empty semantic configuration page in the Azure portal.":::
 
-1. To verify the index is operational, run a query. In **Search explorer**, enter this search string *"walking distance to live music"* so that you can view the response *before* semantic ranking is applied. 
+1. Select **Search explorer**, and then select the **JSON view**.
+
+1. Paste the following JSON into the query editor.
+
+    ```json
+    {
+      "search": "walking distance to live music",
+      "select": "HotelId, HotelName, Description",
+      "count": true
+    }
+    ```
 
    :::image type="content" source="../../media/search-get-started-semantic/search-explorer-simple-query.png" alt-text="Screenshot of a query in Search Explorer in the portal.":::
 
-   Your response should be similar to the following example, as scored by the default BM25 L1 ranker for full text search. For readability, the example selects just the "HotelName" "HotelId", and "Description" fields.
+1. Select **Search** to run the query.
+
+   This query is a keyword search. The response should be similar to the following example, as scored by the default BM25 L1 ranker for full-text search.
 
-   This query is a keyword search. The results contain verbatim matches on the query terms (walking, distance, live, music) or on a linguistic variant (walk, living).
+   For readability, the example only selects the `HotelId`, `HotelName`, and `Description` fields. The results contain verbatim matches on the query terms (`walking`, `distance`, `live`, `music`) or linguistic variants (`walk`, `living`).
 
     ```json
     "@odata.count": 13,
@@ -155,8 +157,7 @@ This quickstart assumes an existing index, modified to include a semantic config
     ]
    ```
 
-Later, you can try this query again after semantic ranking is configured to see how the response changes.
+This query shows how the response looks *before* semantic ranking is applied. Later, you can run the same query after semantic ranking is configured to see how the response changes.
 
 > [!TIP]
-> You can add a semantic configuration in the Azure portal. However, if you want to learn how to add a semantic configuration programmatically, continue with the instructions in this quickstart.
->
+> You can add a semantic configuration in the Azure portal. However, if you want to learn how to add a semantic configuration programmatically, continue with this quickstart.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーの紹介ガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchのセマンティックランカーに関する紹介ガイドにおける軽微な修正を示しています。具体的な内容としては、日付の更新といくつかの文言の改善が行われています。

まず、ドキュメントの日付が「06/27/2025」から「11/20/2025」に変更され、最新の情報が反映されています。これにより、ユーザーはもっとも新しい情報に基づいて学習を進めることができます。

さらに、セマンティックランキングの導入部分が拡充され、どのように検索インデックスにセマンティック設定を追加し、クエリにセマンティックパラメータを加えるかについての説明が明確化されています。また、関連情報へのリンクも保持されており、ユーザーの理解を助ける内容となっています。

加えて、一部の手順が再編成され、より一貫性のある流れで記述されるように改善されています。この結果、ユーザーはガイドを通してセマンティックランキングの導入が容易になり、実際の操作の意図を理解しやすくなっています。

全体として、この更新は、ユーザーがAzureの機能を効果的に活用できるように、セマンティックランカーの利用に関する明確で実用的な情報を提供することを目的としています。

## articles/search/includes/quickstarts/semantic-ranker-java.md{#item-93a05a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ ms.author: karler
 ms.service: azure-ai-search
 ms.custom: devx-track-java
 ms.topic: include
-ms.date: 08/22/2025
+ms.date: 11/20/2025
 ai-usage: ai-assisted
 ---
 
@@ -32,7 +32,7 @@ The quickstart assumes the following is available on your computer:
 
    :::code language="xml" source="~/azure-search-java-samples/semantic-ranking-quickstart/pom.xml" :::
 
-1. Compile the project to resolve the dependencies:
+1. Compile the project to resolve the dependencies.
 
     ```bash
     mvn compile
@@ -71,7 +71,7 @@ In this section, you get settings for the existing `hotels-sample-index` index o
 
    :::code language="java" source="~/azure-search-java-samples/semantic-ranking-quickstart/src/main/java/com/azure/search/quickstart/GetIndexSettings.java" :::
 
-1. Compile and run the code:
+1. Compile and run the code.
 
     ```bash
     mvn compile exec:java -Dexec.mainClass="com.azure.search.quickstart.GetIndexSettings"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaによるセマンティックランカーのクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Javaを使用したセマンティックランカーに関するクイックスタートガイドに対する軽微な修正を示しています。主な内容としては、日付の更新と手順の文言の整形があります。

具体的には、ドキュメントの日付が「08/22/2025」から「11/20/2025」に変更され、最新の情報を反映する形になっています。これにより、利用者は新しい日付に基づいてコンテンツを確認できます。

また、一部の手順で文末に句点（。）が追加され、文がより明確で一貫したものになっています。特に「Compile the project to resolve the dependencies.」および「Compile and run the code.」の文が修正され、読みやすさとプロフェッショナルな印象が向上しています。

全体として、この更新は、セマンティックランカーの利用方法に関する情報を最新の状態に保ち、ユーザーに対してより明確で使いやすい手順を提供することを目的としています。

## articles/search/includes/quickstarts/semantic-ranker-javascript.md{#item-2e091c}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: include
-ms.date: 07/09/2025
+ms.date: 11/20/2025
 ---
 
 [!INCLUDE [Semantic ranker introduction](semantic-ranker-intro.md)]
@@ -19,7 +19,7 @@ The quickstart assumes the following is available on your computer:
 - [Node.js](https://nodejs.org/) (LTS) for running the sample.
 
 > [!TIP]
-> You can [download the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-js) to start with a finished project or follow these steps to create your own. 
+> You can download the [source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-js) to start with a finished project or follow these steps to create your own.
 
 ### Set up local development environment
 
@@ -37,7 +37,7 @@ The quickstart assumes the following is available on your computer:
    npm pkg set type=module
    ```
 
-1. Install packages, including [azure-search-documents](/javascript/api/%40azure/search-documents). 
+1. Install packages, including [azure-search-documents](/javascript/api/%40azure/search-documents).
 
     ```bash
    npm install @azure/identity @azure/search-documents dotenv
@@ -51,14 +51,12 @@ The quickstart assumes the following is available on your computer:
     SEMANTIC_CONFIGURATION_NAME=semantic-config
     ```
 
-
 1. Create a `src` directory in your project directory.
 
    ```bash
    mkdir src
    ```
 
-
 ### Sign in to Azure
 
 If you signed in to the [Azure portal](https://portal.azure.com), you're signed into Azure. If you aren't sure, use the Azure CLI or Azure PowerShell to log in: `az login` or `az connect`. If you have multiple tenants and subscriptions, see [Quickstart: Connect without keys](../../search-get-started-rbac.md) for help on how to connect.
@@ -119,7 +117,7 @@ In this section, you get settings for the existing `hotels-sample-index` index o
     }
     ```
 
-1. Run the code: 
+1. Run the code.
 
     ```bash
     node -r dotenv/config src/getIndexSettings.js
@@ -198,7 +196,7 @@ In this section, you get settings for the existing `hotels-sample-index` index o
         console.error("Error updating semantic configuration:", error);
     }
     ```
-    
+
 1. Run the code.
 
     ```bash
@@ -258,7 +256,7 @@ Once the `hotels-sample-index` index has a semantic configuration, you can run q
 
 Optionally, you can add captions to extract portions of the text and apply hit highlighting to the important terms and phrases. This query adds captions.
 
-1. Create a file in `./src` called `semanticQueryReturnCaptions.js` and copy in the following code to add captions to the query. 
+1. Create a file in `./src` called `semanticQueryReturnCaptions.js` and copy in the following code to add captions to the query.
 
     ```javascript
     import { SearchClient } from "@azure/search-documents";
@@ -420,7 +418,7 @@ To produce a semantic answer, the question and answer must be closely aligned, a
 1. Output should look similar to the following example, where the best answer to question is pulled from one of the results.
 
     Recall that answers are *verbatim content* pulled from your index and might be missing phrases that a user would expect to see. To get *composed answers* as generated by a chat completion model, considering using a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
-    
+
     ```console
     Semantic answer result #1:
     Semantic Answer: Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptによるセマンティックランカーのクイックスタートガイドの更新"
}
```

### Explanation
この変更は、JavaScriptを使用したセマンティックランカーに関するクイックスタートガイドの軽微な修正を示しています。主なポイントは、日付の更新、文言の調整、およびいくつかの手順の明確化です。

まず、ドキュメントの日付が「07/09/2025」から「11/20/2025」に変更されており、最新の状態が反映されています。これにより、ユーザーは新鮮な情報にアクセスできるようになりました。

文言の点では、いくつかの手順の説明の末尾に句点（。）が追加されました。具体的には、「Install packages, including [azure-search-documents](/javascript/api/%40azure/search-documents).」や「Run the code.」など、手順がより明瞭に示されています。

また、不要な空行が削除され、内容が整理されて読みやすくなっています。特に、手順の流れをスムーズにするための細かな改善が見受けられます。

全体として、この更新はセマンティックランカーの実装に際してのユーザー体験を向上させることを目的としており、特に手順の明確さを強化することに注力しています。

## articles/search/includes/quickstarts/semantic-ranker-python.md{#item-a6dcfa}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: include
-ms.date: 07/03/2025
+ms.date: 11/20/2025
 ---
 
 [!INCLUDE [Semantic ranker introduction](semantic-ranker-intro.md)]
@@ -17,7 +17,7 @@ In this quickstart, use a Jupyter notebook and the [**azure-search-documents**](
 We recommend [Visual Studio Code](https://code.visualstudio.com/download) with Python 3.10 or later and the [Python extension](https://code.visualstudio.com/docs/languages/python) for this quickstart.
 
 > [!TIP]
-> You can [download a finished notebook](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) to start with a finished project or follow these steps to create your own. 
+> You can [download a finished notebook](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) to start with a finished project or follow these steps to create your own.
 
 We recommend a virtual environment for this quickstart:
 
@@ -37,7 +37,7 @@ It can take a minute to set up. If you run into problems, see [Python environmen
 
 ### Install packages and set environment variables
 
-1. Install packages, including [azure-search-documents](/python/api/azure-search-documents). 
+1. Install packages, including [azure-search-documents](/python/api/azure-search-documents).
 
     ```python
    ! pip install -r requirements.txt --quiet
@@ -183,7 +183,7 @@ In this section, you update a search index to include a semantic configuration.
     except Exception as ex:
         print(f"❌ Error adding semantic configuration: {ex}")
     ```
-    
+
 1. Run the code.
 
 1. Output is the semantic configuration you just added.
@@ -298,7 +298,7 @@ To produce a semantic answer, the question and answer must be closely aligned, a
 1. Output should look similar to the following example, where the best answer to question is pulled from one of the results.
 
     Recall that answers are *verbatim content* pulled from your index and might be missing phrases that a user would expect to see. To get *composed answers* as generated by a chat completion model, considering using a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
-    
+
     ```bash
     Semantic Answer: Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
     Semantic Answer Score: 0.9829999804496765
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonによるセマンティックランカーのクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Pythonを使用したセマンティックランカーに関するクイックスタートガイドの軽微な修正を示しています。主なポイントとしては、日付の更新、文言の調整、および手順の明確化があります。

まず、ドキュメントの日付が「07/03/2025」から「11/20/2025」に変更され、新しい情報が反映されています。これにより、ユーザーは最新のコンテンツを参照できるようになります。

また、一部の手順において、文の末尾に句点（。）が追加され、構成が整えられています。具体的には「Install packages, including [azure-search-documents](/python/api/azure-search-documents).」や「Run the code.」の部分が修正され、文章がより明確になっています。

不要な空行が削除され、内容が整理されているため、手順がスムーズに読み進められるようになっています。これにより、ユーザーがクイックスタートをより簡単に理解し、実行できるようになります。

全体として、この更新はセマンティックランカーの利用におけるユーザー体験を向上させることを目的としており、特に手順の明確さや整理され方に焦点を当てています。

## articles/search/includes/quickstarts/semantic-ranker-rest.md{#item-d74861}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: heidisteen
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 08/27/2025
+ms.date: 11/20/2025
 ---
 
 [!INCLUDE [Semantic ranker introduction](semantic-ranker-intro.md)]
@@ -16,7 +16,7 @@ In this quickstart, you use a REST client and the [Azure AI Search REST APIs](/r
 We recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for this quickstart.
 
 > [!TIP]
-> You can [download the source code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-semantic-search) to start with a finished project or follow these steps to create your own. 
+> You can download the [source code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-semantic-search) to start with a finished project or follow these steps to create your own.
 
 1. Start Visual Studio Code and open the [semantic-search-index-update.rest](https://github.com/Azure-Samples/azure-search-rest-samples/blob/main/Quickstart-semantic-search/semantic-search-index-update.rest) file or create a new file.
 
@@ -34,7 +34,7 @@ We recommend [Visual Studio Code](https://code.visualstudio.com/download) with a
     Authorization: Bearer {{personalAccessToken}}
    ```
 
-1. Select **Sent request**.
+1. Select **Send Request**.
 
    :::image type="content" source="../../media/search-get-started-semantic/visual-studio-code-send-request.png" alt-text="Screenshot of the REST client send request link.":::
 
@@ -135,9 +135,9 @@ To update an index using the REST API, you must provide the entire schema, plus
     }
     ```
 
-1. Select **Sent request**.
+1. Select **Send Request**.
 
-1. Output for this POST request is an HTTP 200 Success status message.
+1. Output for this POST request is an `HTTP 200 Success` status message.
 
 ## Run semantic queries
 
@@ -302,7 +302,7 @@ To produce a semantic answer, the question and answer must be closely aligned, a
 
    Recall that answers are *verbatim content* pulled from your index and might be missing phrases that a user would expect to see. To get *composed answers* as generated by a chat completion model, considering using a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
 
-   In this example, the answer is considered as a strong fit for the question. 
+   In this example, the answer is considered as a strong fit for the question.
 
     ```json
     {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIによるセマンティックランカーのクイックスタートガイドの更新"
}
```

### Explanation
この変更は、REST APIを利用したセマンティックランカーに関するクイックスタートガイドの軽微な修正を示しています。主要な修正点には、日付の更新、文言の整形、手順の明確化が含まれています。

まず、ドキュメントの日付が「08/27/2025」から「11/20/2025」に変更されています。これにより、最新の情報が反映され、ユーザーはより新しいコンテンツにアクセスできます。

文言に関しては、「Sent request」という表記が「Send Request」に修正されています。この変更により、ボタンやオプションに関する説明がより正確になりました。

手順に関しては、手順の最後に句点（。）が追加され、より整然とした印象を与えています。さらに、手順の構成において不要な空行が削除され、全体的に読みやすさが向上しています。

全体として、この更新はREST APIを使用したセマンティックランカーの実装にとって、ユーザーが手順をより明確に理解できるようにすることを目的としています。このような変更は、ドキュメントの整合性を高め、利用者の体験を向上させることに寄与しています。

## articles/search/includes/quickstarts/semantic-ranker-typescript.md{#item-6d5573}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: include
-ms.date: 07/09/2025
+ms.date: 11/20/2025
 ---
 
 [!INCLUDE [Semantic ranker introduction](semantic-ranker-intro.md)]
@@ -20,7 +20,7 @@ The quickstart assumes the following is available on your computer:
 - [TypeScript](https://www.typescriptlang.org/) for writing the sample code.
 
 > [!TIP]
-> You can [download the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-js) to start with a finished project or follow these steps to create your own. 
+> You can download the [source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-js) to start with a finished project or follow these steps to create your own.
 
 ### Set up local development environment
 
@@ -38,13 +38,13 @@ The quickstart assumes the following is available on your computer:
    npm pkg set type=module
    ```
 
-1. Install development packages, including [azure-search-documents](/javascript/api/%40azure/search-documents). 
+1. Install development packages, including [azure-search-documents](/javascript/api/%40azure/search-documents).
 
     ```bash
    npm install @azure/identity @azure/search-documents dotenv
     ```
 
-1. Install development dependency packages. 
+1. Install development dependency packages.
 
     ```bash
    npm install dotenv @types/node --save-dev
@@ -82,7 +82,7 @@ The quickstart assumes the following is available on your computer:
     }
    ```
 
-1. Update `package.json` to include a script for building TypeScript files. Add the following line to the `scripts` section:
+1. Update `package.json` to include a script for building TypeScript files. Add the following line to the `scripts` section.
 
    ```json
    "build": "tsc"
@@ -102,7 +102,6 @@ The quickstart assumes the following is available on your computer:
    mkdir src
    ```
 
-
 ### Sign in to Azure
 
 If you signed in to the [Azure portal](https://portal.azure.com), you're signed into Azure. If you aren't sure, use the Azure CLI or Azure PowerShell to log in: `az login` or `az connect`. If you have multiple tenants and subscriptions, see [Quickstart: Connect without keys](../../search-get-started-rbac.md) for help on how to connect.
@@ -146,13 +145,12 @@ export interface HotelDocument {
 }
 ```
 
-
 ## Get the index schema
 
 In this section, you get settings for the existing `hotels-sample-index` index on your search service.
 
 1. Create a file in `./src` called `getIndexSettings.ts` and copy in the following code.
-    
+
     ```typescript
     import {
         SearchIndexClient
@@ -186,8 +184,7 @@ In this section, you get settings for the existing `hotels-sample-index` index o
     }
     ```
 
-
-1. Run the code: 
+1. Run the code.
 
     ```bash
     npm run build && node -r dotenv/config dist/getIndexSettings.js
@@ -269,7 +266,7 @@ In this section, you get settings for the existing `hotels-sample-index` index o
         console.error("Error updating semantic configuration:", error);
     }
     ```
-    
+
 1. Run the code.
 
     ```bash
@@ -494,7 +491,7 @@ To produce a semantic answer, the question and answer must be closely aligned, a
 1. Output should look similar to the following example, where the best answer to question is pulled from one of the results.
 
     Recall that answers are *verbatim content* pulled from your index and might be missing phrases that a user would expect to see. To get *composed answers* as generated by a chat completion model, considering using a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
-    
+
     ```console
     Semantic answer result #1:
     Semantic Answer: Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptによるセマンティックランカーのクイックスタートガイドの更新"
}
```

### Explanation
この変更は、TypeScriptを使用したセマンティックランカーに関するクイックスタートガイドの軽微な修正を示しています。主な修正点には、日付の更新、文言の統一、手順の整備が含まれています。

まず、ドキュメントの日付が「07/09/2025」から「11/20/2025」に変更され、最新の情報が反映されています。この更新により、ユーザーはより新しいコンテンツを参照できるようになります。

文言に関しては、「Sent request」という表現が「Send Request」に統一され、一貫性が高まっています。また、手順の最後に句点（。）が追加され、文が整えられています。これにより、読み手に対する明確さが増しています。

さらに、一部の不要な空行が削除されており、全体としての構成が整理されていることが見て取れます。具体的な手順においては、「Run the code:」が「Run the code.」に変更され、簡潔さが強調されています。

全体として、この更新はTypeScriptを利用したセマンティックランカーのクイックスタートガイドをより分かりやすく、整理されたものにすることを目的としています。これにより、ユーザーは手順をより簡単に理解し、実行できるようになります。

## articles/search/search-faq-frequently-asked-questions.yml{#item-eab2ba}

<details>
<summary>Diff</summary>
````diff
@@ -2,14 +2,13 @@
 metadata:
   title: Azure AI Search FAQ
   titleSuffix: Azure AI Search
-  description: Get answers to common questions about Microsoft Azure AI Search service, a cloud hosted search service on Microsoft Azure.
-  
+  description: Get answers to common questions about Azure AI Search, a cloud-hosted search service on Microsoft Azure.
   manager: nitinme
   author: haileytap
   ms.author: haileytapia
   ms.service: azure-ai-search
   ms.topic: faq
-  ms.date: 08/01/2025
+  ms.date: 11/20/2025
 title: Azure AI Search Frequently Asked Questions
 summary:  Find answers to commonly asked questions about Azure AI Search.
 
@@ -19,17 +18,17 @@ sections:
       - question: |
           What is Azure AI Search?
         answer: | 
-          Azure AI Search provides a dedicated search engine and persistent storage of your searchable content for full text and vector search scenarios. It also includes optional, integrated AI to extract more text and structure from raw content, and to chunk and vectorize content for vector search.
+          Azure AI Search provides a dedicated search engine and persistent storage of your searchable content for agentic, full-text, and vector search scenarios. It also includes optional integrated AI to extract text and structure from raw content and to chunk and vectorize content for vector search.
 
       - question: |
           How do I work with Azure AI Search?
         answer: | 
           The primary workflow is create, load, and query an index. Although you can use the Azure portal for most tasks, Azure AI Search is intended to be used programmatically, handling requests from client code. Programmatic support is provided through REST APIs and client libraries in .NET, Python, Java, and JavaScript SDKs for Azure.
 
       - question: |
-          Are "Azure Search" and "Azure Cognitive Search" and "Azure AI Search" the same product?
+          Are "Azure Search," "Azure Cognitive Search," and "Azure AI Search" the same product?
         answer: |
-          Azure Search was renamed to Azure Cognitive Search in October 2019 to reflect the expanded (yet optional) use of cognitive skills and AI processing in service operations. Azure Cognitive Search was renamed to Azure AI Search in October 2023 to align with Foundry Tools. 
+          Yes. They're all the same product, with rebranding occurring in October 2019 and again in October 2023. You might occasionally see evidence of the former names at the programmatic level.
 
       - question: |
           What languages are supported?
@@ -41,19 +40,12 @@ sections:
       - question: |
           How do I integrate search into my solution?
         answer: |
-          Client code should call the Azure SDK client libraries or REST APIs to connect to a search index, formulate queries, and handle responses. You can also write code that builds and refreshes an index, or runs indexers programmatically or by script.
-
-      - question: |
-          Is there functional parity across the various APIs?
-        answer: |
-          Not always. The REST API is always the first to implement new features in preview API versions. The client libraries in Azure SDKs will pick up new features over time, but are released on their own schedule.
-
-          Although the REST APIs are first out with newest features, the Azure SDKs provide more coding support, and are recommended over REST unless a required feature is unavailable.
+          Client code should call the Azure SDK client libraries or REST APIs to connect to a search index, formulate queries, and handle responses. You can also write code that builds and refreshes an index, or that runs indexers programmatically or via script.
 
       - question: |
           Can I pause the service and stop billing?
         answer: |
-          You can't pause a search service. In Azure AI Search, computing resources are allocated when the service is created. It's not possible to release and reclaim those resources on-demand.
+          You can't pause a search service. In Azure AI Search, computing resources are allocated when the service is created. It's not possible to release and reclaim those resources on demand.
 
       - question: |
           Can I upgrade or downgrade the service?
@@ -89,14 +81,14 @@ sections:
       - question: |
           Can I move, backup, and restore indexes?
         answer: |
-          There's no native support for porting indexes. Search indexes are considered downstream data structures, accepting content from other data sources that collect operational data. As such, there's no built-in support for backing up and restoring indexes because the expectation is that you would rebuild an index from source data if you deleted it, or wanted to move it.
+          There's no native support for porting indexes. Search indexes are considered downstream data structures, accepting content from other data sources that collect operational data. Therefore, there's no built-in support for backing up and restoring indexes. The expectation is that you would rebuild an index from source data if it was deleted or needed to be moved.
           
-          However, if you want to move an index between search services, you can try the **index-backup-restore** sample code in this [Azure AI Search .NET sample repo](https://github.com/Azure-Samples/azure-search-dotnet-utilities). There's also a [Python version of backup and restore](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/index-backup-restore/azure-search-backup-and-restore.ipynb).
+          However, if you want to move an index between search services, you can try the backup and restore code sample for [.NET](https://github.com/Azure-Samples/azure-search-dotnet-utilities/tree/main/index-backup-restore) or [Python](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/index-backup-restore/azure-search-backup-and-restore.ipynb).
                    
       - question: |
-          Can I restore my index or service once it's deleted?
+          Can I restore my index or service after it's deleted?
         answer: |
-          No, if you delete an Azure AI Search index or service, it can't be recovered. When you delete a search service, all indexes in the service are deleted permanently.   
+          No. If you delete an Azure AI Search index or service, it can't be recovered. When you delete a search service, all indexes in the service are permanently deleted.   
                     
       - question: |
           Can I index from SQL Database replicas?
@@ -108,12 +100,14 @@ sections:
       - question: |
           What is vector search?
         answer: |
-          Vector search is a technique that finds the most similar documents by comparing their vector representations. Since the goal of a vector representation is to capture the essential characteristics of an item in a numerical format, vector queries can identify similar content even if there are no explicit matches based on keywords or tags. When a user performs a search, the query is summarized into a vector representation and the vector search engine identifies the most similar documents. To improve efficiency on large databases, vector search often provides the approximate nearest neighbors for a query vector. See [Vector search overview](vector-search-overview.md) for the specifics of Azure AI Search's vector offering.
+          Vector search is a technique that finds the most similar documents by comparing their vector representations. Because the goal of a vector representation is to capture the essential characteristics of an item in a numerical format, vector queries can identify similar content, even if there are no explicit matches based on keywords or tags.
+          
+          When a user performs a search, the query is summarized into a vector representation, and the vector search engine identifies the most similar documents. To improve efficiency on large databases, vector search often provides the Approximate Nearest Neighbors (ANN) for a query vector. For more information, see [Vector search in Azure AI Search](vector-search-overview.md).
 
       - question: |
           Does Azure AI Search support vector search?
         answer: |
-          Azure AI Search supports vector indexing and retrieval. It can chunk and vectorize query strings and content if you use [integrated vectorization](vector-search-integrated-vectorization.md) and take a dependency on indexers and skillsets. 
+          Azure AI Search supports vector indexing and retrieval. It can chunk and vectorize query strings and content if you use [integrated vectorization](vector-search-integrated-vectorization.md), which takes a dependency on indexers and skillsets.
 
       - question: |
           How does vector search work in Azure AI Search?
@@ -152,11 +146,11 @@ sections:
       - question: |
           How do I enable vector search on a search index?
         answer: |
-          To enable vector search in an index, you should:
+          To enable vector search in an index:
 
           * Add one or more vector fields to a field collection.
           
-          * Add a "vectorSearch" section to the index schema specifying the configuration used by vector search fields, including the parameters of the Approximate Nearest Neighbor algorithm used, like HNSW.
+          * Add a "vectorSearch" section to the index schema specifying the configuration used by vector search fields, including the parameters of the ANN algorithm used, like HNSW.
           
           * Use the latest stable version, [**2025-09-01**](/rest/api/searchservice), or an Azure SDK to create or update the index, load documents, and issue queries. For more information, see [Create a vector index](vector-search-how-to-create-index.md).
 
@@ -170,24 +164,24 @@ sections:
       - question: |
           Why are there zero matches on terms I know to be valid?
         answer: |
-          The most common case isn't knowing that each query type supports different search behaviors and levels of linguistic analyses. Full text search, which is the predominant workload, includes a language analysis phase that breaks down terms to root forms. This aspect of query parsing casts a broader net over possible matches, because the tokenized term matches a greater number of variants.
+          The most common case isn't knowing that each query type supports different search behaviors and levels of linguistic analyses. Full-text search, which is the predominant workload, includes a language analysis phase that breaks down terms to root forms. This aspect of query parsing casts a broader net over possible matches, because the tokenized term matches a greater number of variants.
           
-          Wildcard, fuzzy and regex queries, however, aren't analyzed like regular term or phrase queries and can lead to poor recall if the query doesn't match the analyzed form of the word in the search index. For more information on query parsing and analysis, see [query architecture](./search-lucene-query-architecture.md).
+          However, wildcard, fuzzy, and regex queries aren't analyzed like regular term or phrase queries and can lead to poor recall if the query doesn't match the analyzed form of the word in the search index. For more information about query parsing and analysis, see [Full-text search in Azure AI Search](./search-lucene-query-architecture.md).
           
       - question: |
           Why are my wildcard searches slow?
         answer: |
-          Most wildcard search queries, like prefix, fuzzy and regex, are rewritten internally with matching terms in the search index. This extra processing adds to latency. Further, broad search queries, like `a*` for example, are likely to be rewritten with many terms, which can be slow. For performant wildcard searches, consider defining a [custom analyzer](/rest/api/searchservice/custom-analyzers-in-azure-search).
+          Most wildcard search queries, like prefix, fuzzy, and regex, are rewritten internally with matching terms in the search index. This extra processing adds to latency. Additionally, broad search queries like `a*` are likely to be rewritten with many terms, which can be slow. For performant wildcard searches, consider defining a [custom analyzer](/rest/api/searchservice/custom-analyzers-in-azure-search).
 
       - question: |
           Can I search across multiple indexes?
         answer: |
-          No, a query is always scoped to a single index.
+          No. A query is always scoped to a single index.
            
       - question: |
           Why is the search score a constant 1.0 for every match?
         answer: |
-          Search scores are generated for full text search queries, based on the [statistical properties of matching terms](search-lucene-query-architecture.md#stage-4-scoring), and ordered high to low in the result set. Query types that aren't full text search (wildcard, prefix, regex) aren't ranked by a relevance score. This behavior is by design. A constant score allow matches found through query expansion to be included in the results, without affecting the ranking.
+          Search scores are generated for full-text search queries based on the [statistical properties of matching terms](search-lucene-query-architecture.md#stage-4-scoring) and are ordered from high to low in the result set. Query types that aren't full-text search (wildcard, prefix, regex) aren't ranked by a relevance score. A constant score allows matches found through query expansion to be included in the results without affecting the ranking.
           
           For example, suppose an input of "tour*" in a wildcard search produces matches on "tours", "tourettes", and "tourmaline". Given the nature of these results, there's no way to reasonably infer which terms are more valuable than others. For this reason, term frequencies are ignored when scoring results in queries of types wildcard, prefix, and regex. Search results based on a partial input are given a constant score to avoid bias towards potentially unexpected matches.
 
@@ -196,34 +190,34 @@ sections:
       - question: |
           Where does Azure AI Search store customer data?
         answer: |
-          It stores your data in the [geography (Geo)](https://azure.microsoft.com/explore/global-infrastructure/geographies/#geographies) where your service is deployed. Microsoft might replicate your data within the same geo for high availability and durability. For more information, see [data residency in Azure](https://azure.microsoft.com/explore/global-infrastructure/data-residency/#overview).
+          It stores your data in the [geography (Geo)](https://azure.microsoft.com/explore/global-infrastructure/geographies/#geographies) where your service is deployed. Microsoft might replicate your data within the same geo for high availability and durability. For more information, see [Data residency in Azure](https://azure.microsoft.com/explore/global-infrastructure/data-residency/#overview).
 
       - question: |
           Does Azure AI Search send customer data to other services for processing?
         answer: |
-          Yes, skills and vectorizers make [outbound calls from Azure AI Search](search-security-overview.md) to other Azure resources or external models that you specify for embedding or chat. Calls to those APIs typically contain raw content to be processed or queries that are vectorized by an embedding model. For Azure-to-Azure connections, the service sends requests over the internal network. If you add a custom skill or vectorizer, the indexer sends content to the URI provided in the custom skill over the public network unless you configure a [shared private link](search-indexer-howto-access-private.md).
+          Yes. Skills and vectorizers make [outbound calls from Azure AI Search](search-security-overview.md) to other Azure resources or external models that you specify for embedding or chat. Calls to those APIs typically contain raw content to be processed or queries that are vectorized by an embedding model. For Azure-to-Azure connections, the service sends requests over the internal network. If you add a custom skill or vectorizer, the indexer sends content to the URI provided in the custom skill over the public network unless you configure a [shared private link](search-indexer-howto-access-private.md).
 
       - question: |
           Does Azure AI Search process customer data in other regions?
         answer: |
-          Processing (vectorization or applied AI transformations) is performed in the Geo that hosts the Foundry Tools used by skills, or the Azure apps or functions hosting custom skills, or the Azure OpenAI or Microsoft Foundry region that hosts your deployed models. These resources are specified by you, so you can choose whether to deploy them in the same Geo as your search service or not.
+          Processing (vectorization or applied AI transformations) is performed in the Geo that hosts the Foundry Tools subservice used by skills, the Azure apps or functions hosting custom skills, or the Azure OpenAI or Microsoft Foundry region that hosts your deployed models. These resources are specified by you, so you can choose whether to deploy them in the same Geo as your search service or not.
           
           If you send data to external (non-Azure) models or services, the processing location is determined by the external service. 
 
       - question: |
           Can I control access to search results based on user identity?
         answer: |
-          You can if you implement a solution that associates documents with a user identity. Typically, users who are authorized to run your application are also authorized to see all search results. Azure AI Search doesn't have built-in support for row-level or document-level permissions, but you can implement [security filters](./search-security-trimming-for-azure-search.md) as a workaround. For steps and script, see [Get started with the Python enterprise chat sample using RAG](/azure/developer/python/get-started-app-chat-template).
+          You can if you implement a solution that associates documents with a user identity. Typically, users who are authorized to run your application are also authorized to see all search results. Azure AI Search doesn't have built-in support for row-level or document-level permissions, but you can implement [security filters](./search-security-trimming-for-azure-search.md) as a workaround. For steps and script, see [Get started: Chat using your own data (Python sample)](/azure/developer/python/get-started-app-chat-template).
 
       - question: |
           Can I control access to operations based on user identity?
         answer: |
-          Yes, you can use [role-based authorization](search-security-rbac.md) for data plane operations over content.
+          Yes. You can use [role-based authorization](search-security-rbac.md) for data plane operations over content.
 
       - question: |
-          Can I use the Azure portal to view and manage search content if the search service is behind an IP firewall or a private endpoint?
+          Can I use the Azure portal to view and manage search content if my search service is behind an IP firewall or private endpoint?
         answer: |
-          You can use the Azure portal on a network-protected search service if you create a network exception that allows client and portal access. For more information, see [connect through an IP firewall](./service-configure-firewall.md#allow-access-from-your-client-and-portal-ip) or [connect through a private endpoint](./service-create-private-endpoint.md#portal-access-private-search-service).
+          You can use the Azure portal on a network-protected search service if you create a network exception that allows client and portal access. For more information, see [Connect through an IP firewall](./service-configure-firewall.md#allow-access-from-your-client-and-portal-ip) or [Connect through a private endpoint](./service-create-private-endpoint.md#portal-access-private-search-service).
 
 additionalContent: |
 
@@ -232,5 +226,5 @@ additionalContent: |
   If your question isn't answered here, you can refer to the following sources for more questions and answers.
   
      [Stack Overflow: Azure AI Search](https://stackoverflow.com/questions/tagged/azure-search)   
-     [How full text search works in Azure AI Search](search-lucene-query-architecture.md)  
+     [How full-text search works in Azure AI Search](search-lucene-query-architecture.md)  
      [What is Azure AI Search?](search-what-is-azure-search.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search FAQの更新"
}
```

### Explanation
この変更は、Azure AI Searchに関するFAQ（よくある質問）のYAMLファイルに対する軽微な修正を示しています。主なポイントとしては、文言の修正、一部の内容の追加、日付の更新が含まれています。

まず、ドキュメントの日付が「08/01/2025」から「11/20/2025」に変更され、最新の情報が反映されています。これにより、ユーザーは情報が新しいものであることを確認できます。

文言の修正としては、特にブランド名に関する部分が改善され、以前の名称と現在の名称の関連性がより明確になっています。例如、「Azure Search」と「Azure AI Search」などを明示的に区別し、同じ製品であることが強調されています。また、文章全体でスタイルの統一が図られており、読みやすさが向上しています。

さらに、一部の質問と回答において、文の構成が整理され、重要な情報が強調されるようになっています。たとえば、特定の機能や実装に関する手順がより具体的に説明され、ユーザーが実際の操作を理解しやすくなっています。また、セキュリティ関連の質問についても、具体的な情報が追加されており、利用者が必要な知識を得やすくなっています。

全体として、この更新はAzure AI SearchのFAQをより分かりやすく、実用的なものにすることを目的とし、ユーザーの質問に対する回答の質を向上させています。このような軽微な更新によって、ドキュメントの全体的な信頼性と有用性が高まります。

## articles/search/search-get-started-rbac.md{#item-9d96c1}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 07/08/2025
+ms.date: 11/20/2025
 zone_pivot_groups: search-get-started-rbac
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACのクイックスタートガイドの日付更新"
}
```

### Explanation
この変更は、RBAC（ロールベースのアクセス制御）に関するクイックスタートガイドのYAMLファイルに対する軽微な修正を示しています。主な内容は、ドキュメントの日付の更新です。

具体的には、日付が「07/08/2025」から「11/20/2025」に変更されています。この日付の更新により、ユーザーは最新の情報を確認できるようになります。ドキュメントの日付は、コンテンツがどれほど最新であるかを示す重要な指標となるため、特に技術的な内容においては更新が反映されることが求められます。

その他の変更点はなく、全体的には文書の信頼性を高めるためのシンプルな改訂となっています。このような更新は、技術文書を常に最新の状態に保つために重要です。

## articles/search/search-get-started-semantic.md{#item-2b3902}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: quickstart
-ms.date: 07/09/2025
+ms.date: 11/20/2025
 zone_pivot_groups: search-get-started-semantic
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティック検索のクイックスタートガイドの日付更新"
}
```

### Explanation
この変更は、セマンティック検索に関するクイックスタートガイドのYAMLファイルに対する軽微な修正を示しています。主な変更点は、ドキュメントの日付の更新です。

具体的には、日付が「07/09/2025」から「11/20/2025」に変更されており、これによりユーザーは最新の情報を得ることができます。文書の日付は、技術的な内容や手順の最新性を確認する際に重要な指標です。

その他の変更はなく、この更新は文書全体の信頼性を高め、利用者にとっての有用性を向上させる役割を果たしています。このような軽微な更新も、ドキュメントを一貫して最新の状態に保つためには欠かせません。

## articles/search/search-get-started-text.md{#item-935941}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.custom:
   - ignite-2023
 ms.topic: quickstart
 zone_pivot_groups: search-quickstart-full-text
-ms.date: 06/25/2025
+ms.date: 11/20/2025
 ---
 
 # Quickstart: Full-text search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "全文検索のクイックスタートガイドの日付更新"
}
```

### Explanation
この変更は、全文検索に関するクイックスタートガイドのYAMLファイルに対する軽微な修正を示しています。主に、ドキュメントの日付が更新されました。

具体的には、日付が「06/25/2025」から「11/20/2025」に変更されており、これによりユーザーが最新の情報を取得できるようになります。文書の日付は、その内容の信頼性を示すための重要な要素です。

その他の部分には変更はなく、全体的には文書の整合性と信頼性を高めるためのシンプルな改訂となっています。このような軽微な更新が反映されることにより、技術文書が常に進化し続けることが求められています。

## articles/search/search-get-started-vector.md{#item-4984d9}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: quickstart
-ms.date: 06/19/2025
+ms.date: 11/20/2025
 zone_pivot_groups: search-get-started-vector-search
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のクイックスタートガイドの日付更新"
}
```

### Explanation
この変更は、ベクトル検索に関するクイックスタートガイドのYAMLファイルに対する軽微な修正を示しています。主な変更点は、ドキュメントの日付の更新です。

具体的には、日付が「06/19/2025」から「11/20/2025」に変更されており、これによって利用者は最新の情報を得ることが可能になります。文書の日付は、内容の正確性や関連性を判断するための重要な要素です。

この修正の他には変更点がなく、文書の整合性を保ちつつ情報を更新するためのシンプルなものであり、技術文書としての信頼性を高める役割を果たしています。こうした軽微な更新も、ユーザーが常に最新の情報にアクセスできるようにするために重要です。

## articles/search/search-indexer-sensitivity-labels.md{#item-2a7bfc}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn how to configure Azure AI Search indexers to ingest Microsoft Purview sensitivity labels from supported data sources for document-level security enforcement.  
 ms.service: azure-ai-search  
 ms.topic: how-to  
-ms.date: 11/14/2025  
+ms.date: 11/19/2025  
 author: gmndrg  
 ms.author: gimondra  
 ---
@@ -53,12 +53,20 @@ These updates are detected if they occurred since the last indexer run.
 
 ## Limitations
 
-+ There's a known issue with document deletion and sensitivity labels. When sensitivity labels are enabled for an index, the indexer fails to enumerate the index’s documents. As a result, soft delete operations don't run because the indexer can't list the documents that need to be removed. This applies to indexers that support soft delete, including Azure Blob, Azure Tables, OneLake, indexed SharePoint, MySQL, and Cosmos DB.
++ There's a known issue with document deletion and sensitivity labels. When sensitivity labels are enabled for an index, the indexer fails to enumerate the index’s documents. As a result, soft delete operations don't run because the indexer can't list the documents that need to be removed. This applies to indexers that support soft delete, including Azure Blob, ADLS Gen2, OneLake, SharePoint.
 + Initial release supports REST API version 2025-11-01-preview and associated beta SDK only. There's no portal experience for configuration or management.  
 + This feature isn't supported when used simultaneously with [ACL-based security filters](search-query-access-control-rbac-enforcement.md) (currently also in preview). Test each feature independently until Microsoft announces official coexistence support.
 + [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) and [Suggest](/rest/api/searchservice/documents/suggest-post) APIs are disabled for Purview-enabled indexes, as they can't yet enforce label-based access control.  
 + Guest accounts and cross-tenant queries aren't supported.
 + In the initial release, sensitivity label-enabled indexes don't support unlabeled documents and don't return them in query results. This capability will be documented when available.
++ The following indexer features don't support documents with sensitivity labels. If you use any of these features in a skillset or indexer, they don't process those documents.
+
+    - Custom Web API skill
+    - GenAI Prompt skill
+    - Knowledge store
+    - Indexer enrichment cache
+    - Debug sessions
+
 
 The following steps must be followed in order to configure sensitivity label synchronization in Azure AI Search.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "センシティビティラベルに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchのインデクサーでのセンシティビティラベルに関するドキュメントに対する修正を示しています。主に、日付の更新と特定の制限事項の追加が行われています。

具体的には、以下の点が変更されました：
1. ドキュメントの日付が「11/14/2025」から「11/19/2025」に更新され、最新の情報が反映されています。
2. センシティビティラベルを使用したドキュメント削除に関する既知の問題の説明が修正され、対応するストレージオプションとして「ADLS Gen2」や「SharePoint」が追加されています。
3. 新しい機能に関して、REST APIバージョンやインデクサーの制限など、細かい情報がいくつか追加されました。この変更により、センシティビティラベルに関連するさまざまなインデクサー機能が文書化され、ユーザーに対する理解が深まるようになっています。

全体として、この更新はドキュメントの正確性と有用性を高め、ユーザーがAzure AI Searchのセンシティビティラベル機能をより良く理解できるようにすることを目的としています。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 11/06/2025
+ms.date: 11/20/2025
 ms.update-cycle: 180-days
 ms.custom:
   - references_regions
@@ -17,13 +17,13 @@ ms.custom:
 
 # Service limits in Azure AI Search
 
-Maximum limits on storage, workloads, and quantities of indexes and other objects depend on whether you [create Azure AI Search](search-create-service-portal.md) at **Free**, **Basic**, **Standard**, or **Storage Optimized** pricing tiers.
+Maximum limits on storage, workloads, and quantities of indexes and other objects depend on the [pricing tier](search-sku-tier.md) of your Azure AI Search service:
 
 + **Free** is a multitenant shared service that comes with your Azure subscription.
 
 + **Basic** provides dedicated computing resources for production workloads at a smaller scale.
 
-+ **Standard** runs on dedicated machines with more storage and processing capacity at every level. Standard comes in four levels: S1, S2, S3, and S3 HD. S3 High Density (S3 HD) is engineered for [multi-tenancy](search-modeling-multitenant-saas-applications.md) and large quantities of small indexes (3,000 indexes per service). S3 HD doesn't provide the [indexer feature](search-indexer-overview.md) and data ingestion must use APIs that push data from source to index.
++ **Standard** runs on dedicated machines with more storage and processing capacity at every level. Standard comes in four levels: S1, S2, S3, and S3 HD. S3 High Density (S3 HD) is engineered for [multi-tenancy](search-modeling-multitenant-saas-applications.md) and large quantities of small indexes (3,000 indexes per service). S3 HD doesn't support [indexers](search-indexer-overview.md), so data ingestion must use APIs that push data from the source to the index.
 
 + **Storage Optimized** runs on dedicated machines with more total storage, storage bandwidth, and memory than **Standard**. This tier targets large, slow-changing indexes. Storage Optimized comes in two levels: L1 and L2.
 
@@ -55,7 +55,7 @@ Maximum limits on storage, workloads, and quantities of indexes and other object
 
 <sup>2</sup> The upper limit on fields includes both first-level fields and nested subfields in a complex collection. For example, if an index contains 15 fields and has two complex collections with five subfields each, the field count of your index is 25. Indexes with a very large fields collection can be slow. [Limit fields and attributes](search-what-is-an-index.md#physical-structure-and-size) to just those you need, and run indexing and query test to ensure performance is acceptable.
 
-<sup>3</sup> An upper limit exists for elements because having a large number of them significantly increases the storage required for your index. An element of a complex collection is defined as a member of that collection. For example, assume a [Hotel document with a Rooms complex collection](search-howto-complex-data-types.md#complex-collection-limits), each room in the Rooms collection is considered an element. During indexing, the indexing engine can safely process a maximum of 3,000 elements across the document as a whole. [This limit](search-api-migration.md#upgrade-to-2019-05-06) was introduced in `api-version=2019-05-06` and applies to complex collections only, and not to string collections or to complex fields.
+<sup>3</sup> An upper limit exists for elements because having a large number of them significantly increases the storage required for your index. An element of a complex collection is defined as a member of that collection. For example, assume a [Hotel document with a Rooms complex collection](search-howto-complex-data-types.md#complex-collection-limits). Each room in the Rooms collection is considered an element. During indexing, the indexing engine can safely process a maximum of 3,000 elements across the document as a whole. [This limit](search-api-migration.md#upgrade-to-2019-05-06) was introduced in `api-version=2019-05-06` and applies to complex collections only, and not to string collections or to complex fields.
 
 <sup>4</sup> For most tiers, the maximum index size is the total available storage on your search service. For S2, S3, and S3 HD services with multiple partitions, and therefore more storage, the maximum size of a single index is provided in the table. Applies to search services created after April 3, 2024.
 
@@ -70,11 +70,11 @@ Maximum number of documents per index are:
 + 288 billion on L1
 + 576 billion on L2
 
-Maximum size of each document is approximately 16 megabytes. Document size is actually a limit on the size of the indexing API request payload, which is 16 megabytes. That payload can be a single document, or a batch of documents. For a batch with a single document, the maximum document size is 16 MB of JSON. 
+Maximum size of each document is approximately 16 megabytes. Document size is actually a limit on the size of the indexing API request payload, which is 16 megabytes. That payload can be a single document, or a batch of documents. For a batch with a single document, the maximum document size is 16 MB of JSON.
 
 Document size applies to *push mode* indexing that uploads documents to a search service. If you're using an indexer for *pull mode* indexing, your source files can be any file size, subject to [indexer limits](#indexer-limits). For the blob indexer, file size limits are larger for higher tiers. For example, the S1 limit is 128 megabytes, S2 limit is 256 megabytes, and so forth.
 
-When estimating document size, remember to index only those fields that add value to your search scenarios, and exclude any source fields that have no purpose in the queries you intend to run.
+When you estimate document size, remember to index only the fields that add value to your search scenarios. Exclude source fields that have no purpose in the queries you intend to run.
 
 ## Vector index size limits
 
@@ -127,22 +127,22 @@ Maximum running times exist to provide balance and stability to the service as a
 | Minimum schedule | 5 minutes |5 minutes |5 minutes |5 minutes |5 minutes |5 minutes |5 minutes | 5 minutes |
 | Maximum running time <sup>5</sup>| 1-3 or 3-10 minutes |2 or 24 hours |2 or 24 hours |2 or 24 hours |2 or 24 hours |N/A  |2 or 24 hours |2 or 24 hours |
 | Blob indexer: maximum blob size, MB |16 |16 |128 |256 |256 |N/A  |256 |256 |
-| Blob indexer: maximum characters of content extracted from a blob <sup>6</sup> |32,000 |64,000 |4&nbsp;million |8&nbsp;million |16&nbsp;million |N/A |4&nbsp;million |4&nbsp;million |
+| Blob indexer: maximum characters of content extracted from a blob <sup>6</sup> |256,000 |512,000 |4&nbsp;million |8&nbsp;million |16&nbsp;million |N/A |4&nbsp;million |4&nbsp;million |
 
-<sup>1</sup> Free services have indexer maximum execution time of 3 minutes for blob sources and 1 minute for all other data sources. Indexer invocation is once every 180 seconds. For AI indexing that calls into Foundry Tools, free services are limited to 20 free transactions per indexer per day, where a transaction is defined as a document that successfully passes through the enrichment pipeline (tip: you can reset an indexer to reset its count).
+<sup>1</sup> Free services have indexer maximum execution time of 3 minutes for blob sources and 1 minute for all other data sources. Indexer invocation is once every 180 seconds. For AI indexing that calls Foundry Tools, free services are limited to 20 free transactions per indexer per day, where a transaction is defined as a document that successfully passes through the enrichment pipeline. (Tip: You can reset an indexer to reset its count.)
 
 <sup>2</sup> Basic services created before December 2017 have lower limits (5 instead of 15) on indexers, data sources, and skillsets.
 
 <sup>3</sup> S3 HD services don't include indexer support.
 
 <sup>4</sup> Maximum of 30 skills per skillset.
 
-<sup>5</sup> Regarding the 2 or 24 hour maximum duration for indexers: a 2-hour maximum is the most common and it's what you should plan for. It refers to indexers that run in the [public environment](search-howto-run-reset-indexers.md#indexer-execution-environment), used to offload computationally intensive processing and leave more resources for queries. The 24-hour limit applies if you configure the indexer to run in a private environment using only the infrastructure that's allocated to your search service. Note that some older indexers are incapable of running in the public environment, and those indexers always have a 24-hour processing range. If you have unscheduled indexers that run continuously for 24 hours, you can assume those indexers couldn't be migrated to the newer infrastructure. As a general rule, for indexing jobs that can't finish within two hours, put the indexer on a [5 minute schedule](search-howto-schedule-indexers.md) so that the indexer can quickly pick up where it left off. On the Free tier, the 3-10 minute maximum running time is for indexers with skillsets.
+<sup>5</sup> Regarding the 2 or 24 hour maximum duration for indexers: a 2-hour maximum is the most common and it's what you should plan for. It refers to indexers that run in the [public environment](search-howto-run-reset-indexers.md#indexer-execution-environment), which offloads computationally intensive processing and leaves more resources for queries. The 24-hour limit applies if you configure the indexer to run in a private environment using only the infrastructure that's allocated to your search service. Some older indexers are incapable of running in the public environment, and those indexers always have a 24-hour processing range. If you have unscheduled indexers that run continuously for 24 hours, you can assume those indexers couldn't be migrated to the newer infrastructure. As a general rule, for indexing jobs that can't finish within two hours, put the indexer on a [5-minute schedule](search-howto-schedule-indexers.md) so that the indexer can quickly pick up where it left off. On the Free tier, the 3-10 minute maximum running time is for indexers with skillsets.
 
 <sup>6</sup> The maximum number of characters is based on Unicode code units, specifically UTF-16.
 
 > [!NOTE]
-> As stated in the [Index limits](#index-limits), indexers will also enforce the upper limit of 3000 elements across all complex collections per document starting with the latest GA API version that supports complex types (`2019-05-06`) onwards. This means that if you've created your indexer with a prior API version, you will not be subject to this limit. To preserve maximum compatibility, an indexer that was created with a prior API version and then updated with an API version `2019-05-06` or later, will still be **excluded** from the limits. Customers should be aware of the adverse impact of having very large complex collections (as stated previously) and we highly recommend creating any new indexers with the latest GA API version.
+> As stated in [Index limits](#index-limits), indexers also enforce the upper limit of 3,000 elements across all complex collections per document starting with the latest GA API version that supports complex types (`2019-05-06`) onwards. This means that if you created your indexer with a prior API version, you won't be subject to this limit. To preserve maximum compatibility, an indexer that was created with a prior API version and then updated with an API version `2019-05-06` or later, will still be **excluded** from the limits. Customers should be aware of the adverse impact of having very large complex collections (as stated previously) and we highly recommend creating any new indexers with the latest GA API version.
 
 ## Shared private link resource limits
 
@@ -156,7 +156,7 @@ Indexers can access other Azure resources [over private endpoints](search-indexe
 | Maximum private endpoints | N/A | 10 or 30 | 100 | 400 | 400 | N/A | 20 | 20 |
 | Maximum distinct resource types <sup>3</sup> | N/A | 4 | 7 | 15 | 15 | N/A | 4 | 4 |
 
-<sup>1</sup> AI enrichment and image analysis are computationally intensive and consume disproportionate amounts of available processing power. For this reason, private connections are disabled on lower tiers to ensure the performance and stability of the search service itself. On Basic services, private connections to a Microsoft Foundry resource are unsupported to preserve service stability. For the S1 tier, make sure the service was created with [higher limits](search-limits-quotas-capacity.md#partition-storage-gb) after April 3, 2024. Indexers with more than 2 Azure OpenAI Embedding or Azure Vision multimodal embeddings skills will be restricted from running in private environment, and private connections will not be available.
+<sup>1</sup> AI enrichment and image analysis are computationally intensive and consume disproportionate amounts of available processing power. For this reason, private connections are disabled on lower tiers to ensure the performance and stability of the search service itself. On Basic services, private connections to a Microsoft Foundry resource are unsupported to preserve service stability. For the S1 tier, make sure the service was created with [higher limits](search-limits-quotas-capacity.md#partition-storage-gb) after April 3, 2024. Indexers with more than 2 Azure OpenAI Embedding or Azure Vision multimodal embeddings skills are restricted from running in private environment, and private connections aren't available.
 
 <sup>2</sup> Private connections to an embedding model are supported on Basic and S1 high-capacity search services created after April 3, 2024, with the [higher limits](search-limits-quotas-capacity.md#partition-storage-gb) for storage and computational processing.
 
@@ -166,7 +166,7 @@ Indexers can access other Azure resources [over private endpoints](search-indexe
 
 Maximum number of synonym maps varies by tier. Each rule can have up to 20 expansions, where an expansion is an equivalent term. For example, given "cat", association with "kitty", "feline", and "felis" (the genus for cats) would count as 3 expansions.
 
-| Resource | Free | Basic | S1 | S2 | S3 | S3HD |L1 | L2 |
+| Resource | Free | Basic | S1 | S2 | S3 | S3 HD |L1 | L2 |
 |----------|------|-------|----|----|----|-------|----|----|
 | Maximum synonym maps |3 |3|5 |10 |20 |20 | 10 | 10 |
 | Maximum number of rules per map |5000 |20000|20000 |20000 |20000 |20000 | 20000 | 20000  |
@@ -175,7 +175,7 @@ Maximum number of synonym maps varies by tier. Each rule can have up to 20 expan
 
 Maximum number of [index aliases](search-how-to-alias.md) varies by tier and [service creation date](search-how-to-upgrade.md#check-your-service-creation-or-upgrade-date). On all tiers, if the service was created after October 2022, the maximum number of aliases is double the maximum number of indexes allowed. If the service was created before October 2022, the limit is the number of indexes allowed.
 
-| Service creation date | Free | Basic | S1 | S2 | S3 | S3HD |L1 | L2 |
+| Service creation date | Free | Basic | S1 | S2 | S3 | S3 HD |L1 | L2 |
 |----------|------|-------|----|----|----|-------|----|----|
 | Before October 2022 | 3 | 5 or 15 <sup>1</sup> | 50 | 200 | 200 | 1000 per partition or 3000 per service | 10 | 10 |
 | After October 2022 | 6 | 30 | 100 | 400 | 400 | 2000 per partition or 6000 per service | 20 | 20 |
@@ -186,7 +186,7 @@ Maximum number of [index aliases](search-how-to-alias.md) varies by tier and [se
 
 Each [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) contains [knowledge sources](agentic-knowledge-source-overview.md), which are data source connections, and configurations that agents consume for [agentic retrieval](agentic-retrieval-overview.md). The following limits apply to knowledge sources and knowledge bases per service tier.
 
-| Resource | Free | Basic <sup>1</sup> | S1 | S2 | S3 | S3HD | L1 | L2 |
+| Resource | Free | Basic <sup>1</sup> | S1 | S2 | S3 | S3 HD | L1 | L2 |
 |--|--|--|--|--|--|--|--|--|
 | Maximum knowledge sources | 3 | 5 or 15 | 50 | 200 | 200 | 0 | 10 | 10 |
 | Maximum knowledge bases | 3 | 5 or 15 | 50 | 200 | 200 | 0 | 10 | 10 |
@@ -195,7 +195,7 @@ Each [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) contain
 
 ## Data limits (AI enrichment)
 
-An [AI enrichment pipeline](cognitive-search-concept-intro.md) that makes calls to an Azure Language in Foundry Tools for [entity recognition](cognitive-search-skill-entity-recognition-v3.md), [entity linking](cognitive-search-skill-entity-linking-v3.md), [key phrase extraction](cognitive-search-skill-keyphrases.md), [sentiment analysis](cognitive-search-skill-sentiment-v3.md), [language detection](cognitive-search-skill-language-detection.md), and [personal-information detection](cognitive-search-skill-pii-detection.md) is subject to data limits. The maximum size of a record should be 50,000 characters as measured by [`String.Length`](/dotnet/api/system.string.length). If you need to break up your data before sending it to the sentiment analyzer, use the [Text Split skill](cognitive-search-skill-textsplit.md).
+Data limits apply to an [AI enrichment pipeline](cognitive-search-concept-intro.md) that makes calls to Azure Language in Foundry Tools for [entity recognition](cognitive-search-skill-entity-recognition-v3.md), [entity linking](cognitive-search-skill-entity-linking-v3.md), [key phrase extraction](cognitive-search-skill-keyphrases.md), [sentiment analysis](cognitive-search-skill-sentiment-v3.md), [language detection](cognitive-search-skill-language-detection.md), and [personal-information detection](cognitive-search-skill-pii-detection.md). The maximum size of a record should be 50,000 characters as measured by [`String.Length`](/dotnet/api/system.string.length). If you need to break up your data before sending it to the sentiment analyzer, use the [Text Split skill](cognitive-search-skill-textsplit.md).
 
 ## Throttling limits
 
@@ -226,10 +226,10 @@ Total semantic ranker queries per second varies based on the following factors:
 
 The following table describes the semantic ranker throttling limits by tier, subject to available capacity in the region. You can contact Microsoft support to request a limit increase.
 
-| Resource | Basic | S1 | S2 | S3 | S3HD | L1 | L2 |
+| Resource | Basic | S1 | S2 | S3 | S3 HD | L1 | L2 |
 |----------|-------|----|----|----|-------|----|----|
-| Maximum Concurrent Requests (per Search Unit) | 2 | 3 | 4 | 4 | 4 | 4 | 4 |
-| Maximum Request Queue Size (per Search Unit) | 4 | 6 | 8 | 8 | 8 | 8 | 8 |
+| Maximum concurrent requests (per search unit) | 2 | 3 | 4 | 4 | 4 | 4 | 4 |
+| Maximum request queue size (per search unit) | 4 | 6 | 8 | 8 | 8 | 8 | 8 |
 
 ## API request limits
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのサービス限界およびクオータに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchのサービス限界およびクオータに関するドキュメントの内容を更新したものです。主に以下の点が変更されています：

1. **日付の更新**：ドキュメントの日付が「11/06/2025」から「11/20/2025」に変更されています。
   
2. **文中の表現修正**：料金プランの説明が明確になり、たとえば「Free」「Basic」「Standard」「Storage Optimized」の各プランの特徴が具体的に強調されています。

3. **部分的情報の整合性**：特定の制限事項の説明が精緻化され、関連の情報が整理されています。例えば、S3 HDプランのインデクサー機能の不支持に関する情報が修正され、より正確な表現が適用されています。

4. **段落の整形・統一**：文中の構成要素が整理され、一貫性が持たされ、読みやすくなっています。特に索引制限、データ制限、スロット制限に関連する情報が整理され、明確なガイドラインが提供されています。

これらの更新を通じて、ユーザーはAzure AI Searchの制限やクオータに関する情報をより理解しやすくなります。また、このドキュメントは、サービスの利用を計画する際に非常に重要なリソースとなります。

## articles/search/semantic-how-to-enable-scoring-profiles.md{#item-e8d524}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ To ensure the scoring profile provides the determining score, the semantic ranke
 
 ## Prerequisites
 
-- [Azure AI Search](search-create-service-portal.md), in any [region that provides semantic ranking](search-region-support.md), with [semantic ranker enabled](semantic-how-to-enable-disable.md).
+- [Azure AI Search](search-create-service-portal.md) in any [region that provides semantic ranking](search-region-support.md), with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
 - A search index with a semantic configuration that specifies `"rankingOrder": "boostedRerankerScore"` and a scoring profile that specifies [functions](index-add-scoring-profiles.md#use-functions).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリングプロファイルを有効にするための前提条件の修正"
}
```

### Explanation
この変更は、Azure AI Searchのスコアリングプロファイルを有効にするための前提条件に対する文の修正を示しています。具体的には、以下の内容が変更されました：

1. **文の構成の修正**：元の文では「- [Azure AI Search]...」の前に不要な「-」があり、この点が削除されて文が整形されました。修正後は、表現が一貫性を持つようになり、可読性が向上しています。

2. **構造の明確化**：情報が簡潔にまとめられ、前提条件がより明確に記載されています。これにより、ユーザーは必要な条件を迅速に把握でき、手続きが容易になります。

この修正は主に文章の表現を整えるものであり、ユーザーに対する情報の伝達がより正確かつわかりやすくなることを目的としています。

## articles/search/semantic-how-to-query-request.md{#item-85530d}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ This article explains how to invoke the semantic ranker on queries. It assumes y
 
 ## Prerequisites
 
-+ [Azure AI Search](search-create-service-portal.md), in any [region that provides semantic ranking](search-region-support.md), with [semantic ranker enabled](semantic-how-to-enable-disable.md).
++ [Azure AI Search](search-create-service-portal.md) in any [region that provides semantic ranking](search-region-support.md), with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
 + An existing search index with a [semantic configuration](semantic-how-to-configure.md) and rich text content.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリリクエストの前提条件の修正"
}
```

### Explanation
この変更は、「クエリリクエストにおけるセマンティックランカーの呼び出し方法」に関する記事の前提条件の文を修正したものです。具体的な変更点は以下の通りです：

1. **文の構成の改善**：元々の文では、Azure AI Searchの参照前に不要な「+」が付加されていましたが、それが削除されました。修正後の文は、構文として整頓され、読みやすくなっています。

2. **情報の整合性**：前提条件に関する情報が整理された結果、ユーザーが必要な条件を理解しやすくなりました。また、セマンティックな構成とリッチテキストコンテンツを持つ既存の検索インデックスも新たに条件として追加されています。

この修正は、読者が必須の前提条件を素早く把握できるようにし、Azure AI Searchの効果的な使用を促進することを目的としています。

## articles/search/semantic-how-to-query-rewrite.md{#item-3e168f}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ Query rewriting is an optional feature. Without query rewriting, the search serv
 
 ## Prerequisites
 
-- [Azure AI Search](search-create-service-portal.md), in any [region that provides query rewrite](search-region-support.md), with [semantic ranker enabled](semantic-how-to-enable-disable.md).
+- [Azure AI Search](search-create-service-portal.md) in any [region that provides query rewrite](search-region-support.md), with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
 - An existing search index with a [semantic configuration](semantic-how-to-configure.md) and rich text content. The examples in this guide use the [hotels-sample-index](search-get-started-portal.md) sample data to demonstrate query rewriting. You can use your own data and index to test query rewriting.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリリライトの前提条件の修正"
}
```

### Explanation
この変更は、「クエリリライトに関する記事」の前提条件に対する文の修正を反映しています。主な変更点は以下の通りです：

1. **文の構造の修正**：元の文には、Azure AI Searchの参照前に不要な「-」記号が存在しましたが、それが削除されました。この修正により、文の構成が改善され、読みやすさが向上しています。

2. **情報の明瞭化**：修正後の文では、前提条件に関する情報がより明確になり、Azure AI Searchの活用方法がわかりやすくなりました。また、引き続きリッチテキストコンテンツとセマンティックな設定を持つ既存の検索インデックスが必要であることが強調されています。

これにより、ユーザーはクエリリライト機能の利用に際して必要な条件を迅速かつ容易に理解できるようになります。

## articles/search/tutorial-multiple-data-sources.md{#item-71558f}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: tutorial
-ms.date: 03/28/2025
+ms.date: 11/20/2025
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
@@ -25,15 +25,15 @@ This C# tutorial uses the [Azure.Search.Documents](/dotnet/api/overview/azure/se
 In this tutorial, you:
 
 > [!div class="checklist"]
-> * Upload sample data and create data sources
+> * Upload sample data to data sources
 > * Identify the document key
 > * Define and create the index
 > * Index hotel data from Azure Cosmos DB
-> * Merge hotel room data from Blob storage
+> * Merge hotel room data from Blob Storage
 
 ## Overview
 
-This tutorial uses [Azure.Search.Documents](/dotnet/api/overview/azure/search) to create and run multiple indexers. In this tutorial, you set up two Azure data sources so that you can configure an indexer that pulls from both to populate a single search index. The two data sets must have a value in common to support the merge. In this sample, that field is an ID. As long as there's a field in common to support the mapping, an indexer can merge data from disparate resources: structured data from Azure SQL, unstructured data from Blob storage, or any combination of [supported data sources](search-indexer-overview.md#supported-data-sources) on Azure.
+This tutorial uses [Azure.Search.Documents](/dotnet/api/overview/azure/search) to create and run multiple indexers. You upload sample data to two Azure data sources and configure an indexer that pulls from both sources to populate a single search index. The two data sets must have a value in common to support the merge. In this tutorial, that field is an ID. As long as there's a field in common to support the mapping, an indexer can merge data from disparate resources: structured data from Azure SQL, unstructured data from Blob Storage, or any combination of [supported data sources](search-indexer-overview.md#supported-data-sources) on Azure.
 
 A finished version of the code in this tutorial can be found in the following project:
 
@@ -43,15 +43,14 @@ A finished version of the code in this tutorial can be found in the following pr
 
 * An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 * An [Azure Cosmos DB for NoSQL account](/azure/cosmos-db/create-cosmosdb-resources-portal).
-* An [Azure storage account](/azure/storage/common/storage-account-create).
+* An [Azure Storage account](/azure/storage/common/storage-account-create).
 * An [Azure AI Search service](search-create-service-portal.md).
-* The [Azure AI Search (version 11.x) NuGet package](https://www.nuget.org/packages/Azure.Search.Documents/).
 * [Visual Studio](https://visualstudio.microsoft.com/).
 
 > [!NOTE]
-> You can use a free search service for this tutorial. The free tier limits you to three indexes, three indexers, and three data sources. This tutorial creates one of each. Before starting, make sure you have room on your service to accept the new resources.
+> You can use a free search service for this tutorial. The free tier limits you to three indexes, three indexers, and three data sources. This tutorial creates one of each. Before you start, make sure you have room on your service to accept the new resources.
 
-## Create services
+## Prepare services
 
 This tutorial uses Azure AI Search for indexing and queries, Azure Cosmos DB for the first data set, and Azure Blob Storage for the second data set.
 
@@ -61,71 +60,87 @@ This sample uses two small sets of data describing seven fictional hotels. One s
 
 ### Start with Azure Cosmos DB
 
-1. Sign in to the [Azure portal](https://portal.azure.com), and then go to the **Overview** page of your Azure Cosmos DB account.
+1. Sign in to the [Azure portal](https://portal.azure.com) and select your Azure Cosmos DB account.
 
-1. Select **Data Explorer**, and then select **New Database**.
+1. From the left pane, select **Data Explorer**.
+
+1. Select **New Container** > **New Database**.
 
    :::image type="content" source="media/tutorial-multiple-data-sources/cosmos-newdb.png" alt-text="Create a new database" border="true":::
 
-1. Enter the name **hotel-rooms-db**. Accept the default values for the remaining settings.
+1. Enter **hotel-rooms-db** for the name. Accept the default values for the remaining settings.
 
    :::image type="content" source="media/tutorial-multiple-data-sources/cosmos-dbname.png" alt-text="Configure database" border="true":::
 
-1. Create a new container. Use the existing database you previously created. Enter **hotels** for the container name and use **/HotelId** for the Partition key.
+1. Create a container that targets the database you previously created. Enter **hotels** for the container name and **/HotelId** for the partition key.
 
    :::image type="content" source="media/tutorial-multiple-data-sources/cosmos-add-container.png" alt-text="Add container" border="true":::
 
-1. Select **Items** under **hotels**, and then select **Upload Item** on the command bar. Navigate to and select the file **cosmosdb/HotelsDataSubset_CosmosDb.json** in the project folder.
+1. Select **hotels** > **Items**, and then select **Upload Item** on the command bar.
+
+1. Upload the JSON file from the `cosmosdb` folder in [multiple-data-sources/v11](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources/v11).
 
    :::image type="content" source="media/tutorial-multiple-data-sources/cosmos-upload.png" alt-text="Upload to Azure Cosmos DB collection" border="true":::
 
-1. Use the Refresh button to refresh your view of the items in the hotels collection. You should see seven new database documents listed.
+1. Use the refresh button to refresh your view of the items in the hotels collection. You should see seven new database documents listed.
 
-1. Copy a connection string from the **Keys** page into Notepad. You need this value for **appsettings.json** in a later step. If you didn't use the suggested database name "hotel-rooms-db", copy the database name as well.
+1. From the left pane, select **Settings** > **Keys**.
+
+1. Make a note of a connection string. You need this value for **appsettings.json** in a later step. If you didn't use the suggested **hotel-rooms-db** database name, copy the database name as well.
 
 ### Azure Blob Storage
 
-1. Sign in to the [Azure portal](https://portal.azure.com), go to your Azure storage account, select **Blobs**, and then select **+ Container**.
+1. Sign in to the [Azure portal](https://portal.azure.com) and select your Azure Storage account.
+
+1. From the left pane, select **Data storage** > **Containers**.
 
-1. [Create a blob container](/azure/storage/blobs/storage-quickstart-blobs-portal) named **hotel-rooms** to store the sample hotel room JSON files. You can set the Public Access Level to any of its valid values.
+1. [Create a blob container](/azure/storage/blobs/storage-quickstart-blobs-portal) named **hotel-rooms** to store the sample hotel room JSON files. You can set the access level to any valid value.
 
    :::image type="content" source="media/tutorial-multiple-data-sources/blob-add-container.png" alt-text="Create a blob container" border="true":::
 
-1. After the container is created, open it and select **Upload** on the command bar. Navigate to the folder containing the sample files. Select all of them, and then select **Upload**.
+1. Open the container, and then select **Upload** on the command bar.
+
+1. Upload the seven JSON files from the `blob` folder in [multiple-data-sources/v11](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources/v11).
 
    :::image type="content" source="media/tutorial-multiple-data-sources/blob-upload.png" alt-text="Upload files" border="false":::
 
-1. Copy the storage account name and a connection string from the **Access Keys** page into Notepad. You need both values for **appsettings.json** in a later step.
+1. From the left pane, select **Security + networking** > **Access keys**.
+
+1. Make a note of the account name and a connection string. You need both values for **appsettings.json** in a later step.
 
 ### Azure AI Search
 
 The third component is Azure AI Search, which you can [create in the Azure portal](search-create-service-portal.md) or [find an existing search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your Azure resources.
 
 ### Copy an admin key and URL for Azure AI Search
 
-To authenticate to your search service, you need the service URL and an access key.
+To authenticate to your search service, you need the service URL and an access key. Having a valid key establishes trust on a per-request basis between the application sending the request and the service handling it.
+
+1. Sign in to the [Azure portal](https://portal.azure.com) and select your search service.
 
-1. Sign in to the [Azure portal](https://portal.azure.com).
+1. From the left pane, select **Overview**.
 
-1. On the **Overview** page of your search service, get the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
+1. Make a note of the URL, which should look like `https://my-service.search.windows.net`.
 
-1. On **Settings** > **Keys**, get an admin key for full rights on the service. There are two interchangeable admin keys, provided for business continuity in case you need to roll one over. You can use either the primary or secondary key on requests for adding, modifying, and deleting objects.
+1. From the left pane, select **Settings** > **Keys**.
 
-Having a valid key establishes trust, on a per-request basis, between the application sending the request and the service handling it.
+1. Make a note of an admin key for full rights on the service. There are two interchangeable admin keys, provided for business continuity in case you need to roll one over. You can use either the primary or secondary key on requests for adding, modifying, and deleting objects.
 
 ## Set up your environment
 
-1. Open Visual Studio.
+1. Open the `AzureSearchMultipleDataSources.sln` file from [multiple-data-sources/v11](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources/v11) in Visual Studio.
 
-1. In the **Tools** menu, select **NuGet Package Manager**, and then select **Manage NuGet Packages for Solution...**.
+1. In Solution Explorer, right-click the project and select **Manage NuGet Packages for Solution...**.
 
-1. On the **Browse** tab, find and install **Azure.Search.Documents** (version 11.0 or later).
+1. On the **Browse** tab, find and install the following packages:
 
-1. Find and install the **Microsoft.Extensions.Configuration** and **Microsoft.Extensions.Configuration.Json** NuGet packages.
+    + **Azure.Search.Documents** (version 11.0 or later)
 
-1. Open the solution file **/v11/AzureSearchMultipleDataSources.sln**.
+    + **Microsoft.Extensions.Configuration**
 
-1. In Solution Explorer, edit the **appsettings.json** file to add connection information.  
+    + **Microsoft.Extensions.Configuration.Json**
+
+1. In Solution Explorer, edit the `appsettings.json` file with the connection information you collected in the previous steps.
 
     ```json
     {
@@ -138,10 +153,6 @@ Having a valid key establishes trust, on a per-request basis, between the applic
     }
     ```
 
-The first two entries are the URL and admin keys of a search service. Use the full endpoint. For example: `https://mydemo.search.windows.net`.
-
-The next entries specify account names and connection string information for the Azure Blob Storage and Azure Cosmos DB data sources.
-
 ## Map key fields
 
 Merging content requires that both data streams are targeting the same documents in the search index.
@@ -150,29 +161,29 @@ In Azure AI Search, the key field uniquely identifies each document. Every searc
 
 When indexing data from multiple data sources, make sure each incoming row or document contains a common document key. This allows you to merge data from two physically distinct source documents into a new search document in the combined index.
 
-It often requires some up-front planning to identify a meaningful document key for your index and to make sure it exists in both data sources. In this demo, the `HotelId` key for each hotel in Azure Cosmos DB is also present in the rooms JSON blobs in Blob storage.
+It often requires some up-front planning to identify a meaningful document key for your index and to make sure it exists in both data sources. In this demo, the `HotelId` key for each hotel in Azure Cosmos DB is also present in the rooms JSON blobs in Blob Storage.
 
-Azure AI Search indexers can use field mappings to rename and even reformat data fields during the indexing process, so that source data can be directed to the correct index field. For example, in Azure Cosmos DB, the hotel identifier is called **`HotelId`**, but in the JSON blob files for the hotel rooms, the hotel identifier is  named **`Id`**. The program handles this discrepancy by mapping the **`Id`** field from the blobs to the **`HotelId`** key field in the indexer.
+Azure AI Search indexers can use field mappings to rename and even reformat data fields during the indexing process, so that source data can be directed to the correct index field. For example, in Azure Cosmos DB, the hotel identifier is called `HotelId`, but in the JSON blob files for the hotel rooms, the hotel identifier is  named `Id`. The program handles this discrepancy by mapping the `Id` field from the blobs to the `HotelId` key field in the indexer.
 
 > [!NOTE]
 > In most cases, autogenerated document keys, such as those created by default by some indexers, don't make good document keys for combined indexes. In general, use a meaningful, unique key value that already exists in your data sources or can be easily added.
 
 ## Explore the code
 
-When the data and configuration settings are in place, the sample program in **/v11/AzureSearchMultipleDataSources.sln** should be ready to build and run.
+When the data and configuration settings are in place, the sample program in `AzureSearchMultipleDataSources.sln` should be ready to build and run.
 
 This simple C#/.NET console app performs the following tasks:
 
 * Creates a new index based on the data structure of the C# Hotel class, which also references the Address and Room classes.
 * Creates a new data source and an indexer that maps Azure Cosmos DB data to index fields. These are both objects in Azure AI Search.
 * Runs the indexer to load hotel data from Azure Cosmos DB.
 * Creates a second data source and an indexer that maps JSON blob data to index fields.
-* Runs the second indexer to load hotel room data from Blob storage.
+* Runs the second indexer to load hotel room data from Blob Storage.
 
- Before running the program, take a minute to study the code and the index and indexer definitions for this sample. The relevant code is in two files:
+Before you run the program, take a minute to study the code, index definition, and indexer definition. The relevant code is in two files:
 
-* **Hotel.cs** contains the schema that defines the index.
-* **Program.cs** contains functions that create the Azure AI Search index, data sources, and indexers, and load the combined results into the index.
+* `Hotel.cs` contains the schema that defines the index.
+* `Program.cs` contains functions that create the Azure AI Search index, data sources, and indexers, and load the combined results into the index.
 
 ### Create an index
 
@@ -182,7 +193,7 @@ The data model is defined by the Hotel class, which also contains references to
 
 The program deletes any existing index of the same name before creating the new one, in case you want to run this example more than once.
 
-The following snippets from the **Hotel.cs** file show single fields, followed by a reference to another data model class, Room[], which in turn is defined in **Room.cs** file (not shown).
+The following snippets from the `Hotel.cs` file show single fields, followed by a reference to another data model class, Room[], which in turn is defined in `Room.cs` file (not shown).
 
 ```csharp
 . . .
@@ -196,7 +207,7 @@ public Room[] Rooms { get; set; }
 . . .
 ```
 
-In the **Program.cs** file, a [SearchIndex](/dotnet/api/azure.search.documents.indexes.models.searchindex) is defined with a name and a field collection generated by the `FieldBuilder.Build` method, and then created as follows:
+In the `Program.cs` file, a [SearchIndex](/dotnet/api/azure.search.documents.indexes.models.searchindex) is defined with a name and a field collection generated by the `FieldBuilder.Build` method, and then created as follows:
 
 ```csharp
 private static async Task CreateIndexAsync(string indexName, SearchIndexClient indexClient)
@@ -237,7 +248,7 @@ private static async Task CreateAndRunCosmosDbIndexerAsync(string indexName, Sea
     await indexerClient.CreateOrUpdateDataSourceConnectionAsync(cosmosDbDataSource);
 ```
 
-After the data source is created, the program sets up an Azure Cosmos DB indexer named **hotel-rooms-cosmos-indexer**.
+After the data source is created, the program sets up an Azure Cosmos DB indexer named `hotel-rooms-cosmos-indexer`.
 
 The program updates any existing indexers with the same name, overwriting the existing indexer with the content of the previous code. It also includes reset and run actions, in case you want to run this example more than once.
 
@@ -283,11 +294,11 @@ catch (RequestFailedException ex) when (ex.Status == 429)
 
 This example includes a simple try-catch block to report any errors that might occur during execution.
 
-After the Azure Cosmos DB indexer runs, the search index contains a full set of sample hotel documents. However, the rooms field for each hotel is an empty array, since the Azure Cosmos DB data source omits room details. Next, the program pulls from Blob storage to load and merge the room data.
+After the Azure Cosmos DB indexer runs, the search index contains a full set of sample hotel documents. However, the rooms field for each hotel is an empty array, since the Azure Cosmos DB data source omits room details. Next, the program pulls from Blob Storage to load and merge the room data.
 
-### Create Blob storage data source and indexer
+### Create Blob Storage data source and indexer
 
-To get the room details, the program first sets up a Blob storage data source to reference a set of individual JSON blob files.
+To get the room details, the program first sets up a Blob Storage data source to reference a set of individual JSON blob files.
 
 ```csharp
 private static async Task CreateAndRunBlobIndexerAsync(string indexName, SearchIndexerClient indexerClient)
@@ -303,11 +314,11 @@ private static async Task CreateAndRunBlobIndexerAsync(string indexName, SearchI
     await indexerClient.CreateOrUpdateDataSourceConnectionAsync(blobDataSource);
 ```
 
-After the data source is created, the program sets up a blob indexer named **hotel-rooms-blob-indexer**, as shown below.
+After the data source is created, the program sets up a blob indexer named `hotel-rooms-blob-indexer`, as shown below.
 
 The JSON blobs contain a key field named **`Id`** instead of **`HotelId`**. The code uses the `FieldMapping` class to tell the indexer to direct the **`Id`** field value to the **`HotelId`** document key in the index.
 
-Blob storage indexers can use [IndexingParameters](/dotnet/api/azure.search.documents.indexes.models.indexingparameters) to specify a parsing mode. You should set different parsing modes depending on whether blobs represent a single document or multiple documents within the same blob. In this example, each blob represents a single JSON document, so the code uses the `json` parsing mode. For more information about indexer parsing parameters for JSON blobs, see [Index JSON blobs](search-how-to-index-azure-blob-json.md).
+Blob Storage indexers can use [IndexingParameters](/dotnet/api/azure.search.documents.indexes.models.indexingparameters) to specify a parsing mode. You should set different parsing modes depending on whether blobs represent a single document or multiple documents within the same blob. In this example, each blob represents a single JSON document, so the code uses the `json` parsing mode. For more information about indexer parsing parameters for JSON blobs, see [Index JSON blobs](search-how-to-index-azure-blob-json.md).
 
 This example defines a schedule for the indexer, so that it runs once per day. You can remove the schedule property from this call if you don't want the indexer to automatically run again in the future.
 
@@ -351,25 +362,27 @@ catch (CloudException e) when (e.Response.StatusCode == (HttpStatusCode)429)
 Because the index is already populated with hotel data from the Azure Cosmos DB database, the blob indexer updates the existing documents in the index and adds the room details.
 
 > [!NOTE]
-> If you have the same non-key fields in both of your data sources, and the data in those fields doesn't match, the index contains the values from whichever indexer ran most recently. In our example, both data sources contain a **HotelName** field. If for some reason the data in this field is different, for documents with the same key value, the **HotelName** data from the most recently indexed data source is the value stored in the index.
+> If you have the same non-key fields in both of your data sources, and the data in those fields doesn't match, the index contains the values from whichever indexer ran most recently. In our example, both data sources contain a `HotelName` field. If for some reason the data in this field is different, for documents with the same key value, the `HotelName` data from the most recently indexed data source is the value stored in the index.
 
 ## Search
 
-After running the program, you can explore the populated search index using the [**Search explorer**](search-explorer.md) in the Azure portal.
+After you run the program, you can explore the populated search index using [**Search explorer**](search-explorer.md) in the Azure portal.
 
-In the portal, go to the **Overview** page of your search service, and then find the **hotel-rooms-sample** index in the **Indexes** list.
+1. Sign in to the [Azure portal](https://portal.azure.com) and select your search service.
 
-  :::image type="content" source="media/tutorial-multiple-data-sources/index-list.png" alt-text="List of Azure AI Search indexes" border="false":::
+1. From the left pane, select **Search management** > **Indexes**.
 
-Select the **hotel-rooms-sample** index to see a Search explorer interface for the index. Enter a query for a term like "Luxury". You should see at least one document in the results, and this document should show a list of room objects in its rooms array.
+1. Select **hotel-rooms-sample** from the list of indexes.
+
+1. On the **Search explorer** tab, enter a query for a term like `Luxury`.
+
+   You should see at least one document in the results. This document should contain a list of room objects in its `Rooms` array.
 
 ## Reset and rerun
 
 In the early experimental stages of development, the most practical approach for design iteration is to delete the objects from Azure AI Search and allow your code to rebuild them. Resource names are unique. Deleting an object lets you recreate it using the same name.
 
-The sample code checks for existing objects and deletes or updates them so that you can rerun the program.
-
-You can also use the Azure portal to delete indexes, indexers, and data sources.
+The sample code checks for existing objects and deletes or updates them so that you can rerun the program. You can also use the Azure portal to delete indexes, indexers, and data sources.
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "複数データソースに関するチュートリアルの更新"
}
```

### Explanation
この変更は、「複数データソースを使用したチュートリアル」に関連するドキュメントの内容を更新し、全体の流れや表現を改善しました。主な変更点は以下の通りです：

1. **日付の更新**：ドキュメントの日付が2025年3月28日から2025年11月20日に変更され、内容の新しさと関連性が保持されています。

2. **内容の明確化**：手順に関する記述がより明確にされ、特に「データソースへのサンプルデータのアップロード」や「Blobストレージ」などのセクションにおいて、表現が改善されました。例えば、「Blob storage」が「Blob Storage」に修正されています。

3. **手順の整理**：手順がより論理的な順序で提示され、必要なアクションが一貫して記載されています。「Azureポータルへのサインイン」、「データベースの作成」といった具体的なアクションが弁別しやすくなっています。

4. **例と説明の追加**：プログラムの動作やデータソース間のマッピングに関する詳細が追加され、より分かりやすく、実用的なコードサンプルが提供されています。

この更新は、読者がAzureの複数のデータソースを活用したインデキシングのプロセスを理解しやすくするために、明確さと実用性を向上させることを目的としています。


