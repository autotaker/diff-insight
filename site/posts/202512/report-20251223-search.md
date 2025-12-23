---
date: '2025-12-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:84e593e...MicrosoftDocs:ccb0359
summary: ハイライトとして、エージェントリトリーバルに関するMicrosoftDocsのクイックスタートガイドが更新され、特にJavaScriptおよびTypeScript向けに大規模な改訂がなされました。新しいサンプルコードや具体的な手順が追加され、情報の明確性や一貫性が向上しています。これにより、ユーザーは最新のベストプラクティスに基づいてエージェントリトリーバル機能をより効率的に活用できるようになります。他の言語に関するガイドも微調整が施され、読みやすさが改善されています。全体的に、ユーザーのプロジェクト実行の障壁が軽減され、Azure
  AIを活用した高度なソリューション構築が支援されることが期待されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:84e593e...MicrosoftDocs:ccb0359){target="_blank"}

# ハイライト

エージェントリトリーバルに関するMicrosoftDocsの各種クイックスタートガイドが更新されました。一部では大規模な改訂が行われており、新しいサンプルコードや具体的な手順が追加されています。特に、JavaScriptおよびTypeScript向けのガイドでは重大な変更が施されています。

## 新機能
- なし

## 互換性に影響を与える変更
- JavaScript用エージェントリトリーバルクイックスタートでの大規模な修正
- TypeScript用エージェントリトリーバルクイックスタートでの大規模な改訂

## その他の更新
- 各言語別のクイックスタートガイドの微調整および表現の一貫性を向上
- 日付や用語、見出しの一貫性を修正
- 情報の明確性を高めるためのテキストの修正

# インサイト

今回の変更は、MicrosoftDocsにおけるエージェントリトリーバルのクイックスタート記事が、利用者向けにより明確で一貫した情報を提供することを目的としています。特に、JavaScriptおよびTypeScriptの記事に関しては大幅な再設計が行われ、古い情報を削除し、最新の実装方法が提示されています。これにより、ユーザーは最新のベストプラクティスに基づいて効率的にエージェントリトリーバル機能を活用できるようになります。

他のクイックスタートガイド（C#, Java, Python, REST, セットアップ）については、細かい微調整が主であり、特に用語や表現の統一に重点が置かれています。これにより、ドキュメントの読みやすさが向上し、技術的な利用者以外の方にも理解しやすいガイドラインとなることが期待されます。

また、記事の更新に伴い日付や関連リソースへのリンク、役割ベースのアクセス設定手順なども改善されており、全体としてユーザーのプロジェクト実行における障壁が軽減されることが見込まれます。こうした修正は、ドキュメントを通じた学習や実装をよりスムーズにし、最終的にはAzure AIを活用した高度なソリューションの構築をサポートするものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | エージェントリトリーバルパイプラインの作成方法 | modified | 416 | 142 | 558 | 
| [agentic-retrieval-csharp.md](#item-f93ed3) | minor update | C#用エージェントリトリーバルクイックスタート | modified | 4 | 4 | 8 | 
| [agentic-retrieval-java.md](#item-4e2c55) | minor update | Java用エージェントリトリーバルクイックスタート | modified | 2 | 2 | 4 | 
| [agentic-retrieval-javascript.md](#item-715283) | breaking change | JavaScript用エージェントリトリーバルクイックスタート | modified | 684 | 819 | 1503 | 
| [agentic-retrieval-python.md](#item-efee6a) | minor update | Python用エージェントリトリーバルクイックスタート | modified | 3 | 3 | 6 | 
| [agentic-retrieval-rest.md](#item-3df373) | minor update | REST用エージェントリトリーバルクイックスタート | modified | 2 | 2 | 4 | 
| [agentic-retrieval-setup.md](#item-e5e297) | minor update | エージェントリトリーバルセットアップのクイックスタート | modified | 11 | 11 | 22 | 
| [agentic-retrieval-typescript.md](#item-e6370b) | breaking change | エージェントリトリーバル TypeScript クイックスタート | modified | 676 | 961 | 1637 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to design and build a custom agentic retrieval solution w
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 12/17/2025
+ms.date: 12/22/2025
 ms.service: azure-ai-search
 ms.topic: tutorial
 ms.custom:
@@ -16,153 +16,321 @@ ms.custom:
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-In this tutorial, you learn how to build a solution that integrates Azure AI Search and Foundry Agent Service for intelligent knowledge retrieval.
+Learn how to create an intelligent, MCP-enabled solution that integrates Azure AI Search with Foundry Agent Service for [agentic retrieval](agentic-retrieval-overview.md). You can use this architecture for conversational applications that require complex reasoning over large knowledge domains, such as customer support or technical troubleshooting.
 
-This solution uses Model Context Protocol (MCP) to establish a standardized connection between your agentic retrieval pipeline in Azure AI Search, which consists of a *knowledge base* that references a *knowledge source*, and your agent in Foundry Agent Service. You can use this architecture for conversational applications that require complex reasoning over large knowledge domains, such as customer support or technical troubleshooting.
+In this tutorial, you:
 
-The following diagram shows the high-level architecture of this agentic retrieval solution:
+> [!div class="checklist"]
+>
+> + Configure role-based access for Azure AI Search and Microsoft Foundry
+> + Create a search index, knowledge source, and knowledge base in Azure AI Search
+> + Create a project connection for MCP communication between Azure AI Search and Microsoft Foundry
+> + Create an agent in Microsoft Foundry that uses the MCP tool for retrieval
+> + Test the solution by chatting with the agent
+> + Review tips for optimizing the solution
 
 :::image type="content" source="media/agentic-retrieval/end-to-end-pipeline.svg" alt-text="Diagram of Azure AI Search integration with Foundry Agent Service via MCP." lightbox="media/agentic-retrieval/end-to-end-pipeline.svg" :::
 
 > [!TIP]
-> + Want to get started right away? See the [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) source code.
-> + Want a simpler introduction to agentic retrieval? See [Quickstart: Use agentic retrieval](search-get-started-agentic-retrieval.md).
+> Want to get started right away? Clone the [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) Python notebook on GitHub. The notebook contains the code from this tutorial in a ready-to-run format.
 
 ## Prerequisites
 
 + An Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md).
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
-+ A [supported LLM](agentic-retrieval-how-to-create-knowledge-base.md#supported-models) deployed to your project. We recommend a minimum token capacity of 100,000. You can find the LLM's capacity and rate limit in the Foundry portal. If you want [vectorization at query time](vector-search-integrated-vectorization.md#using-integrated-vectorization-in-queries), you should also deploy a text embedding model.
++ A text embedding model deployed to your project for [query-time vectorization](vector-search-integrated-vectorization.md#using-integrated-vectorization-in-queries). This solution uses `text-embedding-3-large`.
 
-+ [Authentication and permissions](#authentication-and-permissions) on your search service and project.
++ An LLM deployed to your project for the agent. This solution uses `gpt-4.1-mini`.
 
-+ Preview package versions. For a complete list of versions used in this solution, see the [`requirements.txt`](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/agentic-retrieval-pipeline-example/requirements.txt) file.
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-### Authentication and permissions
++ [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter package](https://pypi.org/project/jupyter/).
 
-Before you begin, make sure you have permissions to access content and operations. We recommend Microsoft Entra ID authentication and role-based access for authorization. You must be an **Owner** or **User Access Administrator** to assign roles. If roles aren't feasible, you can use [key-based authentication](search-security-api-keys.md) instead.
+## Understand the solution
 
-To configure access for this solution, you must set permissions in both Azure AI Search and Microsoft Foundry. Select both of the following tabs for service-specific guidance.
+This solution combines Azure AI Search and Microsoft Foundry to create an end-to-end retrieval pipeline:
 
-### [**Azure AI Search**](#tab/search-perms)
++ **Azure AI Search** hosts your knowledge base, which handles query planning, query execution, and result synthesis. You create a search index to store content, a knowledge source that references the index, and a knowledge base that performs hybrid retrieval from the knowledge source.
 
-1. [Enable role-based access](search-security-enable-roles.md).
-1. [Configure a managed identity](search-how-to-managed-identities.md).
-1. [Assign roles](search-security-rbac.md):
++ **Microsoft Foundry** hosts your Azure OpenAI model deployments, project connection, and agent. You create a project connection that points to the MCP endpoint of your knowledge base, and then you create an agent that uses the MCP tool to access the knowledge base.
 
-   + You must have the **Search Service Contributor**, **Search Index Data Contributor**, and **Search Index Data Reader** roles to create, load, and retrieve on Azure AI Search.
+A user initiates query processing by interacting with a client app, such as a chatbot, that calls the agent. The agent uses the MCP tool to orchestrate requests to the knowledge base and synthesize responses. When the chatbot calls the agent, the MCP tool calls the knowledge base in Azure AI Search and sends the response to the agent and chatbot.
 
-   + For integrated operations, ensure that all clients using the retrieval pipeline have the **Search Index Data Reader** role for sending retrieval requests.
+## Configure access
 
-### [**Microsoft Foundry**](#tab/foundry-perms)
+Before you begin, make sure you have permissions to access content and operations. We recommend Microsoft Entra ID for authentication and role-based access for authorization. You must be an **Owner** or **User Access Administrator** to assign roles. If roles aren't feasible, use [key-based authentication](search-security-api-keys.md) instead.
 
-+ On the resource, you must have the **Azure AI User** role to access model deployments and create agents. This assignment is conferred automatically for **Owners** when you create the resource. Other users need a specific role assignment. For more information, see [Role-based access control in Foundry portal](/azure/ai-foundry/concepts/rbac-azure-ai-foundry).
+To configure access for this solution:
 
-+ On the resource, you must have the **Azure AI Project Manager** role to create a project connection for MCP authentication and either **Azure AI User** or **Azure AI Project Manager** to use the MCP tool in agents.
+1. Sign in to the [Azure portal](https://portal.azure.com).
 
-+ For integrated operations, ensure your [search service identity](search-how-to-managed-identities.md) has the **Cognitive Services User** role on the resource.
+1. [Enable a system-assigned managed identity](search-how-to-managed-identities.md#create-a-system-managed-identity) for both your search service and your project. You can do so on the **Identity** page of each resource.
 
----
+1. On your search service, [enable role-based access](search-security-enable-roles.md) and [assign the following roles](search-security-rbac.md).
 
-## Understand the solution
+    | Role | Assignee | Purpose |
+    |------|----------|---------|
+    | Search Service Contributor | Your user account | Create objects |
+    | Search Index Data Contributor | Your user account | Load data |
+    | Search Index Data Reader | Your user account and project managed identity | Read indexed content |
 
-This section pairs each component of the solution with its corresponding development tasks. For deeper guidance, see the linked how-to articles.
+1. On your project's parent resource, assign the following roles.
 
-### [Azure AI Search](#tab/search-development)
+    | Role | Assignee | Purpose |
+    |------|----------|---------|
+    | Azure AI User | Your user account | Access model deployments and create agents |
+    | Azure AI Project Manager | Your user account | Create project connection and use MCP tool in agents |
+    | Cognitive Services User | Search service managed identity | Access knowledge base |
 
-Azure AI Search hosts your indexed content and the agentic retrieval pipeline. Development tasks include:
+## Set up your environment
 
-+ Create a [knowledge source](agentic-knowledge-source-overview.md). Agentic retrieval supports multiple types of knowledge sources, but this solution creates a [search index knowledge source](agentic-knowledge-source-how-to-search-index.md).
+1. Create a folder named `tutorial-agentic-retrieval` on your local system.
 
-+ [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) that maps to your LLM deployment and uses the extractive data output mode. We recommend this output mode for interaction with Foundry Agent Service because it provides the agent with verbatim, unprocessed content for grounding and reasoning.
+1. Open the folder in Visual Studio Code.
 
-### [Microsoft Foundry](#tab/foundry-development)
+1. Select **View > Command Palette**, and then select **Python: Create Environment**. Follow the prompts to create a virtual environment.
 
-Microsoft Foundry hosts your Azure OpenAI model deployments, project connection, and agent. Development tasks include:
+1. Select **Terminal > New Terminal**.
 
-+ Create a project connection that points to the MCP endpoint of your knowledge base.
+1. Install the required packages.
 
-+ Create an agent that uses the MCP tool.
+   ```console
+   pip install azure-ai-projects==2.0.0b1 azure-mgmt-cognitiveservices azure-identity ipykernel dotenv azure-search-documents==11.7.0b2 requests openai
+   ```
 
-+ Use the MCP tool to coordinate calls from the agent to the knowledge base.
+1. Create a file named `.env` in the `tutorial-agentic-retrieval` folder.
 
----
+1. Add the following variables to the `.env` file, replacing the placeholder values with your own.
+
+   ```
+   AZURE_SEARCH_ENDPOINT = https://{your-service-name}.search.windows.net
+   PROJECT_ENDPOINT = https://{your-resource-name}.services.ai.azure.com/api/projects/{your-project-name}
+   PROJECT_RESOURCE_ID = /subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.CognitiveServices/accounts/{account-name}/projects/{project-name}
+   AZURE_OPENAI_ENDPOINT = https://{your-resource-name}.openai.azure.com
+   AZURE_OPENAI_EMBEDDING_DEPLOYMENT = text-embedding-3-large
+   AGENT_MODEL = gpt-4.1-mini
+   ```
+
+   You can find the endpoints and resource ID in the Azure portal:
+
+   + `AZURE_SEARCH_ENDPOINT` is on the **Overview** page of your search service.
+
+   + `PROJECT_ENDPOINT` is on the **Endpoints** page of your project.
+
+   + `PROJECT_RESOURCE_ID` is on the **Properties** page of your project.
+
+   + `AZURE_OPENAI_ENDPOINT` is on the **Endpoints** page of your project's parent resource.
 
-A user initiates query processing by interacting with a client app, such as a chatbot, that calls the agent. The agent uses the MCP tool to orchestrate requests to the knowledge base and synthesize responses. When the chatbot calls the agent, the MCP tool calls the knowledge base in Azure AI Search and sends it back to the agent and chatbot.
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Microsoft Foundry project.
+
+    ```azurecli
+    az login
+    ```
+
+1. Create a file named `tutorial.ipynb` in the `tutorial-agentic-retrieval` folder. You add code cells to this file in the next section.
 
 ## Build the solution
 
-Follow these steps to create an end-to-end agentic retrieval solution.
+In this section, you create the components of the agentic retrieval solution. Add each code snippet to a separate code cell in the `tutorial.ipynb` notebook and run the cells sequentially.
 
-### Get endpoints
+Steps in this section include:
 
-For this solution, you need the following endpoints:
+1. [Load connections](#load-connections)
+1. [Create a search index](#create-a-search-index)
+1. [Upload documents to the index](#upload-documents-to-the-index)
+1. [Create a knowledge source](#create-a-knowledge-source)
+1. [Create a knowledge base](#create-a-knowledge-base)
+1. [Set up a project client](#set-up-a-project-client)
+1. [Create a project connection](#create-a-project-connection)
+1. [Create an agent with the MCP tool](#create-an-agent-with-the-mcp-tool)
+1. [Chat with the agent](#chat-with-the-agent)
+1. [Clean up resources](#clean-up-resources)
 
-#### [Azure AI Search](#tab/search-setup)
+### Load connections
 
-+ The endpoint for your search service, which you can find on the **Overview** page in the Azure portal. It should look like this: `https://{your-service-name}.search.windows.net/`
+The following code loads the environment variables from your `.env` file and establishes connections to Azure AI Search and Microsoft Foundry.
 
-#### [Microsoft Foundry](#tab/foundry-setup)
+```python
+import os
 
-+ The Azure OpenAI endpoint of your project's parent resource, which you can find on the **Endpoints** page in the Azure portal. It should look like this: `https://{your-resource-name}.openai.azure.com/`
+from azure.identity import DefaultAzureCredential
+from azure.mgmt.core.tools import parse_resource_id
+from dotenv import load_dotenv
 
-+ The endpoint for your project, which you can find on the **Endpoints** page in the Azure portal. It should look like this: `https://{your-resource-name}.services.ai.azure.com/api/projects/{your-project-name}`
+load_dotenv(override=True) # Take environment variables from .env
 
-+ The resource ID of your project, which you can find on the **Properties** page in the Azure portal. It should look like this: `/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.CognitiveServices/accounts/{account-name}/projects/{project-name}`
+project_endpoint = os.environ["PROJECT_ENDPOINT"]
+project_resource_id = os.environ["PROJECT_RESOURCE_ID"]
+project_connection_name = os.getenv("PROJECT_CONNECTION_NAME", "earthknowledgeconnection")
+agent_model = os.getenv("AGENT_MODEL", "gpt-4.1-mini")
+agent_name = os.getenv("AGENT_NAME", "earth-knowledge-agent")
+endpoint = os.environ["AZURE_SEARCH_ENDPOINT"]
+credential = DefaultAzureCredential()
+knowledge_source_name = os.getenv("AZURE_SEARCH_KNOWLEDGE_SOURCE_NAME", "earth-knowledge-source")
+index_name = os.getenv("AZURE_SEARCH_INDEX", "earth-at-night")
+azure_openai_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
+azure_openai_embedding_deployment = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-large")
+azure_openai_embedding_model = os.getenv("AZURE_OPENAI_EMBEDDING_MODEL", "text-embedding-3-large")
+base_name = os.getenv("AZURE_SEARCH_AGENT_NAME", "earth-knowledge-base")
+
+# Parse the resource ID to extract subscription and other components
+parsed_resource_id = parse_resource_id(project_resource_id)
+subscription_id = parsed_resource_id['subscription']
+resource_group = parsed_resource_id['resource_group']
+account_name = parsed_resource_id['name']
+project_name = parsed_resource_id['child_name_1']
+```
 
----
+### Create a search index
 
-### Create agentic retrieval objects
+In Azure AI Search, an index is a structured collection of data. The following code creates an index to store searchable content for your knowledge base.
 
-This section omits code snippets for creating the knowledge source and knowledge base in Azure AI Search, skipping ahead to the Foundry Agent Service integration. For more information about the omitted steps, see the [Understand the solution](#understand-the-solution) section.
+The index schema contains fields for document identification and page content, embeddings, and numbers. The schema also includes configurations for semantic ranking and vector search, which uses your `text-embedding-3-large` deployment to vectorize text and match documents based on semantic similarity.
 
-### Create a project connection
+For more information about this step, see [Create an index for agentic retrieval in Azure AI Search](agentic-retrieval-how-to-create-index.md).
+
+```python
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import (
+    AzureOpenAIVectorizer, AzureOpenAIVectorizerParameters,
+    HnswAlgorithmConfiguration, SearchField, SearchIndex,
+    SemanticConfiguration, SemanticField, SemanticPrioritizedFields,
+    SemanticSearch, VectorSearch, VectorSearchProfile
+)
+
+index = SearchIndex(
+    name=index_name,
+    fields=[
+        SearchField(name="id", type="Edm.String", key=True, filterable=True, sortable=True, facetable=True),
+        SearchField(name="page_chunk", type="Edm.String", filterable=False, sortable=False, facetable=False),
+        SearchField(name="page_embedding_text_3_large", type="Collection(Edm.Single)", stored=False, vector_search_dimensions=3072, vector_search_profile_name="hnsw_text_3_large"),
+        SearchField(name="page_number", type="Edm.Int32", filterable=True, sortable=True, facetable=True)
+    ],
+    vector_search=VectorSearch(
+        profiles=[VectorSearchProfile(name="hnsw_text_3_large", algorithm_configuration_name="alg", vectorizer_name="azure_openai_text_3_large")],
+        algorithms=[HnswAlgorithmConfiguration(name="alg")],
+        vectorizers=[
+            AzureOpenAIVectorizer(
+                vectorizer_name="azure_openai_text_3_large",
+                parameters=AzureOpenAIVectorizerParameters(
+                    resource_url=azure_openai_endpoint,
+                    deployment_name=azure_openai_embedding_deployment,
+                    model_name=azure_openai_embedding_model
+                )
+            )
+        ]
+    ),
+    semantic_search=SemanticSearch(
+        default_configuration_name="semantic_config",
+        configurations=[
+            SemanticConfiguration(
+                name="semantic_config",
+                prioritized_fields=SemanticPrioritizedFields(
+                    content_fields=[
+                        SemanticField(field_name="page_chunk")
+                    ]
+                )
+            )
+        ]
+    )
+)
+
+index_client = SearchIndexClient(endpoint=endpoint, credential=credential)
+index_client.create_or_update_index(index)
+print(f"Index '{index_name}' created or updated successfully")
+```
+
+### Upload documents to the index
+
+Currently, the index is empty. The following code populates the index with JSON documents from [NASA's Earth at Night e-book](https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json). As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
 
-Before you can use the MCP tool in an agent, you must create a project connection in Foundry that points to the `mcp_endpoint` of your knowledge base. This endpoint allows the agent to access your knowledge base.
+For more information about this step, see [Pushing data to an index](search-what-is-data-import.md#pushing-data-to-an-index).
 
 ```python
 import requests
-from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+from azure.search.documents import SearchIndexingBufferedSender
 
-# Provide connection details
-credential = DefaultAzureCredential()
-project_resource_id = "{project_resource_id}" # e.g. /subscriptions/{subscription}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{account_name}/projects/{project_name}
-project_connection_name = "{project_connection_name}"
-mcp_endpoint = "{search_service_endpoint}/knowledgebases/{knowledge_base_name}/mcp?api-version=2025-11-01-preview" # This endpoint enables the MCP connection between the agent and knowledge base
+url = "https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json"
+documents = requests.get(url).json()
 
-# Get bearer token for authentication
-bearer_token_provider = get_bearer_token_provider(credential, "https://management.azure.com/.default")
-headers = {
-  "Authorization": f"Bearer {bearer_token_provider()}",
-}
+with SearchIndexingBufferedSender(endpoint=endpoint, index_name=index_name, credential=credential) as client:
+    client.upload_documents(documents=documents)
 
-# Create project connection
-response = requests.put(
-  f"https://management.azure.com{project_resource_id}/connections/{project_connection_name}?api-version=2025-10-01-preview",
-  headers = headers,
-  json = {
-    "name": "project_connection_name",
-    "type": "Microsoft.MachineLearningServices/workspaces/connections",
-    "properties": {
-      "authType": "ProjectManagedIdentity",
-      "category": "RemoteTool",
-      "target": mcp_endpoint,
-      "isSharedToAll": True,
-      "audience": "https://search.azure.com/",
-      "metadata": { "ApiType": "Azure" }
-    }
-  }
+print(f"Documents uploaded to index '{index_name}'")
+```
+
+### Create a knowledge source
+
+A knowledge source is a reusable reference to source data. The following code creates a knowledge source that targets the index you previously created.
+
+`source_data_fields` specifies which index fields are included in citation references. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+
+For more information about this step, see [Create a search index knowledge source](agentic-knowledge-source-how-to-search-index.md).
+
+```python
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import (
+    SearchIndexFieldReference, SearchIndexKnowledgeSource,
+    SearchIndexKnowledgeSourceParameters
 )
 
-response.raise_for_status()
-print(f"Connection '{project_connection_name}' created or updated successfully.")
+ks = SearchIndexKnowledgeSource(
+    name=knowledge_source_name,
+    description="Knowledge source for Earth at night data",
+    search_index_parameters=SearchIndexKnowledgeSourceParameters(
+        search_index_name=index_name,
+        source_data_fields=[SearchIndexFieldReference(name="id"), SearchIndexFieldReference(name="page_number")]
+    ),
+)
+
+index_client = SearchIndexClient(endpoint=endpoint, credential=credential)
+index_client.create_or_update_knowledge_source(knowledge_source=ks)
+print(f"Knowledge source '{knowledge_source_name}' created or updated successfully.")
 ```
 
-### Set up an AI project client
+### Create a knowledge base
+
+The following code creates a knowledge base that orchestrates agentic retrieval from your knowledge source. The code also stores the MCP endpoint of the knowledge base, which your agent will use to access the knowledge base.
+
+For integration with Foundry Agent Service, the knowledge base is configured with the following parameters:
+
++ `output_mode` is set to extractive data, which provides the agent with verbatim, unprocessed content for grounding and reasoning. The alternative mode, answer synthesis, returns pregenerated answers that limit the agent's ability to reason over source content.
+
++ `retrieval_reasoning_effort` is set to minimal effort, which bypasses LLM-based query planning to reduce costs and latency. For other reasoning efforts, the knowledge base uses an LLM to reformulate user queries before retrieval.
 
-Use [AIProjectClient](/python/api/azure-ai-projects/azure.ai.projects.aiprojectclient?view=azure-python-preview&preserve-view=true) to create a client connection to your Foundry project.
+For more information about this step, see [Create a knowledge base in Azure AI Search](agentic-retrieval-how-to-create-knowledge-base.md).
+
+```python
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import (
+    KnowledgeBase, KnowledgeRetrievalMinimalReasoningEffort,
+    KnowledgeRetrievalOutputMode, KnowledgeSourceReference
+)
+
+knowledge_base = KnowledgeBase(
+    name=base_name,
+    knowledge_sources=[
+        KnowledgeSourceReference(
+            name=knowledge_source_name
+        )
+    ],
+    output_mode=KnowledgeRetrievalOutputMode.EXTRACTIVE_DATA,
+    retrieval_reasoning_effort=KnowledgeRetrievalMinimalReasoningEffort()
+)
+
+
+index_client = SearchIndexClient(endpoint=endpoint, credential=credential)
+index_client.create_or_update_knowledge_base(knowledge_base=knowledge_base)
+print(f"Knowledge base '{base_name}' created or updated successfully")
+
+mcp_endpoint = f"{endpoint}/knowledgebases/{base_name}/mcp?api-version=2025-11-01-Preview"
+```
+
+### Set up a project client
+
+Use [AIProjectClient](/python/api/azure-ai-projects/azure.ai.projects.aiprojectclient?view=azure-python-preview&preserve-view=true) to create a client connection to your Microsoft Foundry project. Your project might not contain any agents yet, but if you've already completed this tutorial, the agent is listed here.
 
 ```python
 from azure.ai.projects import AIProjectClient
@@ -172,135 +340,201 @@ project_client = AIProjectClient(endpoint=project_endpoint, credential=credentia
 list(project_client.agents.list())
 ```
 
-### Create an agent that uses the MCP tool
+### Create a project connection
+
+The following code creates a project connection in Microsoft Foundry that points to the MCP endpoint of your knowledge base. This connection uses your project managed identity to authenticate to Azure AI Search.
+
+```python
+import requests
+from azure.identity import get_bearer_token_provider
+
+bearer_token_provider = get_bearer_token_provider(credential, "https://management.azure.com/.default")
+headers = {
+    "Authorization": f"Bearer {bearer_token_provider()}",
+}
+
+response = requests.put(
+    f"https://management.azure.com{project_resource_id}/connections/{project_connection_name}?api-version=2025-10-01-preview",
+    headers=headers,
+    json={
+        "name": project_connection_name,
+        "type": "Microsoft.MachineLearningServices/workspaces/connections",
+        "properties": {
+            "authType": "ProjectManagedIdentity",
+            "category": "RemoteTool",
+            "target": mcp_endpoint,
+            "isSharedToAll": True,
+            "audience": "https://search.azure.com/",
+            "metadata": { "ApiType": "Azure" }
+        }
+    }
+)
+
+response.raise_for_status()
+print(f"Connection '{project_connection_name}' created or updated successfully.")
+```
+
+### Create an agent with the MCP tool
 
-The next step is to create an agent configured with the MCP tool. When the agent receives a user query, it can call your knowledge base through the MCP tool to retrieve relevant content for response grounding.
+The following code creates an agent configured with the MCP tool. When the agent receives a user query, it can call your knowledge base through the MCP tool to retrieve relevant content for response grounding.
 
-The agent definition includes instructions that specify its behavior and the project connection you previously created. For more information, see [Quickstart: Create a new agent](/azure/ai-foundry/agents/quickstart).
+The agent definition includes instructions that specify its behavior and the project connection you previously created. Based on our experiments, these instructions are effective in maximizing the accuracy of knowledge base invocations and ensuring proper citation formatting.
+
+For more information about this step, see [Quickstart: Create a new agent](/azure/ai-foundry/agents/quickstart).
 
 ```python
 from azure.ai.projects.models import PromptAgentDefinition, MCPTool
 
-# Define agent instructions
 instructions = """
-A Q&A agent that can answer questions based on the attached knowledge base.
-Always provide references to the ID of the data source used to answer the question.
-If you don't have the answer, respond with "I don't know".
+You are a helpful assistant that must use the knowledge base to answer all the questions from the user. You must never answer from your own knowledge under any circumstances.
+Every answer must always provide annotations for using the MCP knowledge base tool and render them as: `【message_idx:search_idx†source_name】`
+If you cannot find the answer in the provided knowledge base you must respond with "I don't know".
 """
 
-# Create MCP tool with knowledge base connection
 mcp_kb_tool = MCPTool(
-    server_label = "knowledge-base",
-    server_url = mcp_endpoint,
-    require_approval = "never",
-    allowed_tools = ["knowledge_base_retrieve"],
-    project_connection_id = project_connection_name
+    server_label="knowledge-base",
+    server_url=mcp_endpoint,
+    require_approval="never",
+    allowed_tools=["knowledge_base_retrieve"],
+    project_connection_id=project_connection_name
 )
 
-# Create agent with MCP tool
 agent = project_client.agents.create_version(
-    agent_name = agent_name,
-    definition = PromptAgentDefinition(
-        model = agent_model,
-        instructions = instructions,
-        tools = [mcp_kb_tool]
+    agent_name=agent_name,
+    definition=PromptAgentDefinition(
+        model=agent_model,
+        instructions=instructions,
+        tools=[mcp_kb_tool]
     )
 )
 
-print(f"Agent '{agent_name}' created or updated successfully.")
+print(f"AI agent '{agent_name}' created or updated successfully")
 ```
 
-### Connect to a remote SharePoint knowledge source
+#### Connect to a remote SharePoint knowledge source
 
-Optionally, if your knowledge base includes a [remote SharePoint knowledge source](agentic-knowledge-source-how-to-sharepoint-remote.md), you must also include the `x-ms-query-source-authorization` header in the MCP tool connection.
+Optionally, if you create a [remote SharePoint knowledge source](agentic-knowledge-source-how-to-sharepoint-remote.md), you must also include the `x-ms-query-source-authorization` header in the MCP tool connection.
 
 ```python
+from azure.search.documents.indexes.models import RemoteSharePointKnowledgeSource, KnowledgeSourceReference
+from azure.search.documents.indexes import SearchIndexClient
 from azure.identity import get_bearer_token_provider
 
-# Create MCP tool with SharePoint authorization header
+remote_sp_ks = RemoteSharePointKnowledgeSource(
+    name="remote-sharepoint",
+    description="SharePoint knowledge source"
+)
+
+index_client = SearchIndexClient(endpoint=endpoint, credential=credential)
+index_client.create_or_update_knowledge_source(knowledge_source=remote_sp_ks)
+print(f"Knowledge source '{remote_sp_ks.name}' created or updated successfully.")
+
+knowledge_base.knowledge_sources = [
+    KnowledgeSourceReference(name=remote_sp_ks.name), KnowledgeSourceReference(name=knowledge_source_name)
+]
+
+index_client.create_or_update_knowledge_base(knowledge_base=knowledge_base)
+print(f"Knowledge base '{base_name}' updated with new knowledge source successfully")
+
 mcp_kb_tool = MCPTool(
-    server_label = "knowledge-base",
-    server_url = mcp_endpoint,
-    require_approval = "never",
-    allowed_tools = ["knowledge_base_retrieve"],
-    project_connection_id = project_connection_name,
-    headers = {
+    server_label="knowledge-base",
+    server_url=mcp_endpoint,
+    require_approval="never",
+    allowed_tools=["knowledge_base_retrieve"],
+    project_connection_id=project_connection_name,
+    headers={
         "x-ms-query-source-authorization": get_bearer_token_provider(credential, "https://search.azure.com/.default")()
     }
 )
+
+agent = project_client.agents.create_version(
+    agent_name=agent_name,
+    definition=PromptAgentDefinition(
+        model=agent_model,
+        instructions=instructions,
+        tools=[mcp_kb_tool]
+    )
+)
+
+print(f"AI agent '{agent_name}' created or updated successfully")
 ```
 
 ### Chat with the agent
 
-Your client app uses the Conversations and [Responses](/azure/ai-foundry/openai/how-to/responses) APIs from Azure OpenAI to send user input to the agent. The client creates a conversation and passes each user message to the agent through the Responses API, resembling a typical chat experience.
+Your client app uses the Conversations and [Responses](/azure/ai-foundry/openai/how-to/responses) APIs from Azure OpenAI to interact with the agent.
 
-The agent manages the conversation, determines when to call your knowledge base through the MCP tool, and returns a natural-language response (with references to the retrieved content) to the client app.
+The following code creates a conversation and passes user messages to the agent, resembling a typical chat experience. The agent determines when to call your knowledge base through the MCP tool and returns a natural-language answer with references. Setting `tool_choice="required"` ensures the agent always uses the knowledge base tool when processing queries.
 
 ```python
 # Get the OpenAI client for responses and conversations
 openai_client = project_client.get_openai_client()
 
-# Create conversation
 conversation = openai_client.conversations.create()
 
-# Send request to trigger the MCP tool
+# Send initial request that will trigger the MCP tool
 response = openai_client.responses.create(
-    conversation = conversation.id,
-    input = """
+    conversation=conversation.id,
+    tool_choice="required",
+    input="""
         Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown?
         Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?
     """,
-    extra_body = {"agent": {"name": agent.name, "type": "agent_reference"}},
+    extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
 )
 
 print(f"Response: {response.output_text}")
 ```
 
-## Improve data quality
+The response should be similar to the following:
 
-By default, search results from your knowledge base are consolidated into a large unified string that can be passed to the agent for grounding. Azure AI Search provides the following indexing and relevance-tuning features to help you generate high-quality results. You can implement these features in the search index, and the improvements in search relevance are evident in the quality of retrieval responses.
+```
+Response: Here are evidence-based explanations to your questions:
 
-+ [Scoring profiles](index-add-scoring-profiles.md) provide built-in boosting criteria. Your index must specify a default scoring profile, which is used by the retrieval engine when queries include fields associated with that profile.
+---
 
-+ [Semantic configuration](semantic-how-to-configure.md) is required, but you determine which fields are prioritized and used for ranking.
+**1. Why do suburban belts display larger December brightening than urban cores, even though absolute light levels are higher downtown?**
 
-+ For plain-text content, you can use [analyzers](index-add-custom-analyzers.md) to control tokenization during indexing.
+- Suburban belts show a *larger percentage increase* in night brightness during December compared to urban cores, largely because suburban residential areas feature more single-family homes and larger yards, which are typically decorated with holiday lights. These areas start from a lower baseline (less bright overall at night compared to dense urban centers), so the relative change (brightening) is much more noticeable.
 
-+ For [multimodal or image content](multimodal-search-overview.md), you can use image verbalization for LLM-generated descriptions of your images or classic OCR and image analysis via skillsets during indexing.
+- In contrast, the downtown core is already very bright at night due to dense commercial lighting and streetlights. While it also sees a December increase (often 20–30% brighter), the *absolute* change is less striking because it begins at a much higher base of illumination.
 
-## Control the number of subqueries
+- This pattern is observed across U.S. cities, with the phenomenon driven by widespread cultural practices and the suburban landscape’s suitability for holiday lighting displays. The effect is visible in satellite data and was quantified at 20–50% brighter in December, especially in suburbs and city outskirts.
 
-The LLM that powers your knowledge base determines the number of subqueries based on the following factors:
+---
 
-+ User query
-+ Chat history
-+ Semantic ranker input constraints
+**2. Why is the Phoenix nighttime street grid so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?**
 
-As the developer, you can control the number of subqueries by [setting the retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). The reasoning effort determines the level of LLM processing for query planning, ranging from minimal (no LLM processing) to medium (deeper search and follow-up iterations).
+- Phoenix’s sharply visible nighttime street grid from space is a result of its urban layout: the city (like many western U.S. cities) was developed using a regular grid system, with extensive and uniform street lighting and strong urban sprawl. The grid pattern, and the dense network of intersecting surface streets, is brightly illuminated, particularly at intersections, commercial areas, and major thoroughfares.
 
-## Control the context sent to the agent
+- The interstate highways between midwestern cities, though significant in length and crucial to national infrastructure, traverse sparsely populated rural areas. These stretches typically have very little artificial lighting (due to low traffic volumes at night and cost considerations), making them much less visible in nighttime satellite imagery. Only nodes (cities and towns) along the route show as bright "pearls" in the darkness, while the "strings" (highways) connecting them remain faint or invisible.
 
-The Responses API controls what is sent to the agent and knowledge base. To optimize performance and relevance, adjust your agent instructions to summarize or filter the chat history before sending it to the MCP tool.
+- In summary:
+  - Urban areas like Phoenix stand out with strong, connected patterns of light due to dense development and extensive lighting.
+  - Rural interstates are sparsely lit, and only their endpoints—cities and large towns—generate notable light visible from space.
 
-## Control costs and limit operations
+---
 
-For insights into the query plan, look at output tokens in the [activity array](agentic-retrieval-how-to-retrieve.md#review-the-activity-array) of knowledge base responses.
+**References**:
+- [Holiday Lights increase most dramatically in suburbs, not downtowns: earth_at_night_508_page_176_verbalized, page 160](4:5)
+- [Lighting paths and urban grids are visible from space, while rural highways remain dim: earth_at_night_508_page_124_verbalized, page 108](4:3)
+- [Phoenix’s grid and surrounding urban structure: earth_at_night_508_page_104_verbalized, page 88](4:1)
+```
 
-## Improve performance
+### Inspect the response
 
-To optimize performance and reduce latency, consider the following strategies:
+The underlying response from the agent contains metadata about the queries sent to the knowledge base and the citations found. You can inspect this metadata to understand how the agent processed the user input.
 
-+ Summarize message threads.
+```python
+response.to_dict()
+```
 
-+ Use `gpt-4.1-mini` or a smaller model that performs faster.
+### Clean up resources
 
-+ Set `maxOutputSize` on the [retrieve action](agentic-retrieval-how-to-retrieve.md) to govern the size of the response or `maxRuntimeInSeconds` for time-bound processing.
+When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
 
-## Clean up resources
+In the Azure portal, you can manage your Azure AI Search and Microsoft Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
 
-When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-You can also delete individual objects:
+You can also run the following code to delete individual objects:
 
 ```python
 # Delete the agent
@@ -320,6 +554,46 @@ index_client.delete_index(index)
 print(f"Index '{index_name}' deleted successfully")
 ```
 
+## Improve data quality
+
+By default, search results from knowledge bases are consolidated into a large, unified string that can be passed to agents for grounding. Azure AI Search provides the following indexing and relevance-tuning features to help you generate high-quality results. You can implement these features in the search index, and the improvements in search relevance are evident in the quality of retrieval responses.
+
++ [Scoring profiles](index-add-scoring-profiles.md) provide built-in boosting criteria. Your index must specify a default scoring profile, which is used by the retrieval engine when queries include fields associated with that profile.
+
++ [Semantic configuration](semantic-how-to-configure.md) is required, but you determine which fields are prioritized and used for ranking.
+
++ For plain-text content, you can use [analyzers](index-add-custom-analyzers.md) to control tokenization during indexing.
+
++ For [multimodal or image content](multimodal-search-overview.md), you can use image verbalization for LLM-generated descriptions of your images or classic OCR and image analysis via skillsets during indexing.
+
+## Control the number of subqueries
+
+You can control the number of subqueries by [setting the retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md) on the knowledge base. The reasoning effort determines the level of LLM processing for query planning, ranging from minimal (no LLM processing) to medium (deeper search and follow-up iterations).
+
+For non-minimal reasoning efforts, the LLM determines the number of subqueries based on the following factors:
+
++ User query
++ Chat history
++ Semantic ranker input constraints
+
+## Control the context sent to the agent
+
+The Responses API controls what is sent to the agent and knowledge base. To optimize performance and relevance, adjust the agent instructions to summarize or filter the chat history before sending it to the MCP tool.
+
+## Control costs and limit operations
+
+For insights into the query plan, look at output tokens in the [activity array](agentic-retrieval-how-to-retrieve.md#review-the-activity-array) of knowledge base responses.
+
+## Improve performance
+
+To optimize performance and reduce latency, consider the following strategies:
+
++ Summarize message threads.
+
++ Use `gpt-4.1-mini` or a smaller model that performs faster.
+
++ Set `maxOutputSize` on the [retrieve action](agentic-retrieval-how-to-retrieve.md) to govern the size of the response or `maxRuntimeInSeconds` for time-bound processing.
+
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルパイプラインの作成方法"
}
```

### Explanation
このコードの変更は、MicrosoftDocsの「エージェントリトリーバルパイプラインの作成方法」記事の文書を更新しています。主な変更点には、日付の更新やチュートリアルの説明の強化が含まれています。新しい内容では、Azure AI SearchとFoundry Agent Serviceを統合したインテリジェントなMCP対応ソリューションの作成方法が詳述されており、ユーザーが複雑な推論を伴う会話型アプリケーションを構築するためのステップが強調されています。

また、tutorialセクションには手順がリスト化され、読者が非技術的な内容から具体的な実装手順まで理解しやすくしています。更新された内容は、エージェントの構成、役割ベースのアクセスの設定、知識ベースやエージェントの作成方法を網羅しており、全体として読者に向けた理解を一層深める内容となっています。これにより、ユーザーはソリューションの設定と展開において具体的で実用的な情報を得ることができるようになりました。

## articles/search/includes/quickstarts/agentic-retrieval-csharp.md{#item-f93ed3}

<details>
<summary>Diff</summary>
````diff
@@ -46,7 +46,7 @@ To set up the console application for this quickstart:
     dotnet new console
     ```
 
-1. Install the [Azure AI Search client library](/dotnet/api/overview/azure/search.documents-readme) for .NET.
+1. Install the [Azure AI Search client library for .NET](/dotnet/api/overview/azure/search.documents-readme).
 
     ```console
     dotnet add package Azure.Search.Documents --version 11.8.0-beta.1
@@ -64,7 +64,7 @@ To set up the console application for this quickstart:
     dotnet add package Azure.Identity
     ```
 
-1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Foundry project.
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Microsoft Foundry project.
 
     ```console
     az login
@@ -682,7 +682,7 @@ Console.WriteLine($"Documents uploaded to index '{indexName}' successfully.");
 
 A knowledge source is a reusable reference to source data. The following code defines a knowledge source named `earth-knowledge-source` that targets the `earth-at-night` index.
 
-`SourceDataFields` specifies which index fields are accessible for retrieval and citations. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+`SourceDataFields` specifies which index fields are included in citation references. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
 
 ```csharp
 // Create a knowledge source
@@ -897,7 +897,7 @@ foreach (var reference in retrievalResult.Value.References)
 
 When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
 
-In the Azure portal, you can manage your Azure AI Search and Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
+In the Azure portal, you can manage your Azure AI Search and Microsoft Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
 
 Otherwise, the following code from `Program.cs` deleted the objects you created in this quickstart.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#用エージェントリトリーバルクイックスタート"
}
```

### Explanation
このコードの変更は、MicrosoftDocsの「C#用エージェントリトリーバルクイックスタート」記事に対して行われたものであり、主に内容を明確にするための微調整が施されています。具体的には、テキストの表現を改善し、文中での用語やフレーズがより一貫性を持つように修正されました。

例えば、「Azure AI Search client library for .NET」と表記が改められ、Microsoft Foundryプロジェクトに言及する際には、「Microsoft Foundry project」と言及が追加されています。また、知識ソースの説明部分では、引用参照に関してより具体的な表現が用いられるようになりました。

これらの修正はユーザーにとっての理解度を向上させ、よりクリアな情報提供を可能にするためのものであり、全体としては機能的には影響が少ない微調整と位置付けられます。これにより、読者はよりスムーズに記事を理解しやすくなっています。

## articles/search/includes/quickstarts/agentic-retrieval-java.md{#item-4e2c55}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 + An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md).
 
-+ A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects). You get a Foundry resource (that you need for model deployments) when you create a Foundry project.
++ A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
 + The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
@@ -805,7 +805,7 @@ The sample in this quickstart works with the Java Runtime. Install a Java Develo
 
 ### Output
 
-The output of the application should look similar to the following:
+The output of the application should be similar to the following:
 
 ```
 Starting Azure AI Search agentic retrieval quickstart...
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java用エージェントリトリーバルクイックスタート"
}
```

### Explanation
このコードの変更は、MicrosoftDocsの「Java用エージェントリトリーバルクイックスタート」記事に対するもので、内容の明確性を向上させるための微調整が行われています。具体的には、いくつかの文の表現が修正され、より一貫した内容が提供されています。

例えば、Microsoft Foundryプロジェクトに関しての説明が、「Microsoft Foundry projectとresource」と具体的な情報が追加され、プロジェクト作成時に必要なリソースについて補足が行われています。また、アプリケーションの出力に関する説明も微妙に修正され、「出力の結果は以下のようになります」といった表現に改善されています。

これらの変更により、ドキュメントの情報はより明確で一貫したものとなり、ユーザーが手順を追いやすく、理解しやすい内容となっています。全体として、情報の精度向上と読みやすさの向上が目的とされた変更です。

## articles/search/includes/quickstarts/agentic-retrieval-javascript.md{#item-715283}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "JavaScript用エージェントリトリーバルクイックスタート"
}
```

### Explanation
このコードの変更は、MicrosoftDocsの「JavaScript用エージェントリトリーバルクイックスタート」記事に対する大規模な修正を示しています。具体的には、684行の追加と819行の削除が行われ、結果として1503行の変更が記録されています。このような大規模な変更は、既存の内容が大幅に見直され、改訂されたことを示唆しています。

主な変更点には、より詳細な説明の追加、新しいサンプルコードの提供、手順の改善などが含まれます。これにより、ユーザーがエージェントリトリーバル機能をJavaScriptで実装する際に必要な情報が提供され、全体的により包括的で理解しやすい内容へと進化しています。

この変更は、内容の根本的な再設計を伴うものであり、従来の内容に依存していたユーザーには破壊的な変更を引き起こす可能性があります。このため、変更後のドキュメントの内容への移行には慎重な検討が必要です。全体として、ユーザー体験の向上を目指した大幅な改善が施されています。

## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 + The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-+ [Visual Studio Code](https://code.visualstudio.com/download) with the latest version of [Python](https://www.python.org/downloads/).
++ [Visual Studio Code](https://code.visualstudio.com/download) and the latest version of [Python](https://www.python.org/downloads/).
 
 [!INCLUDE [Setup](./agentic-retrieval-setup.md)]
 
@@ -639,7 +639,7 @@ print(f"Documents uploaded to index '{index_name}' successfully.")
 
 A knowledge source is a reusable reference to source data. The following code defines a knowledge source named `earth-knowledge-source` that targets the `earth-at-night` index.
 
-`source_data_fields` specifies which index fields are accessible for retrieval and citations. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+`source_data_fields` specifies which index fields are included in citation references. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
 
 ```python
 # Create a knowledge source
@@ -877,7 +877,7 @@ print("references_content:\n", references_content)
 
 When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
 
-In the [Azure portal](https://portal.azure.com/), you can manage your Azure AI Search and Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
+In the [Azure portal](https://portal.azure.com/), you can manage your Azure AI Search and Microsoft Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
 
 Otherwise, the following code from `agentic-retrieval.py` deleted the objects you created in this quickstart.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python用エージェントリトリーバルクイックスタート"
}
```

### Explanation
このコードの変更は、MicrosoftDocsの「Python用エージェントリトリーバルクイックスタート」記事に対する微調整を示しています。具体的には、3行の追加と3行の削除が行われ、全体で6行の変更が記録されています。この更新は、情報の明確性と一貫性を向上させることを目的としています。

主な変更点としては、Azure CLIを用いた認証方法や「Visual Studio Code」と「Python」の関係についての文言が修正されました。特に、Pythonの最新バージョンに関する記述が一貫して、より簡潔に表現されています。また、引用のためにどのインデックスフィールドが使用されるかについての説明も更新されました。

これにより、ユーザーがこのクイックスタートを利用する際の理解が深まり、手順がよりスムーズになっています。全体として、この更新は文書の明確さを向上させ、ユーザーが必要な情報を容易に見つけられるようにするためのものであり、ユーザー体験を改善するための小さな一歩として位置付けられます。

## articles/search/includes/quickstarts/agentic-retrieval-rest.md{#item-3df373}

<details>
<summary>Diff</summary>
````diff
@@ -506,7 +506,7 @@ Authorization: Bearer {{token}}
 
 A knowledge source is a reusable reference to source data. The following code uses [Knowledge Sources - Create (REST API)](/rest/api/searchservice/knowledge-sources/create?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to define a knowledge source named `earth-knowledge-source` that targets the `earth-at-night` index.
 
-`sourceDataFields` specifies which index fields are accessible for retrieval and citations. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+`sourceDataFields` specifies which index fields are included in citation references. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
 
 ```HTTP
 ### Create a knowledge source
@@ -618,7 +618,7 @@ The output should contain the following components:
 
 When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
 
-In the [Azure portal](https://portal.azure.com/), you can manage your Azure AI Search and Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
+In the [Azure portal](https://portal.azure.com/), you can manage your Azure AI Search and Microsoft Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
 
 Otherwise, the following requests from `agentic-retrieval.rest` deleted the objects you created in this quickstart.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST用エージェントリトリーバルクイックスタート"
}
```

### Explanation
このコードの変更は、MicrosoftDocsの「REST用エージェントリトリーバルクイックスタート」記事に対する軽微な修正を示しています。具体的には、2行の追加と2行の削除が行われ、合計で4行の変更が記録されています。この調整は、文書内の表現の一貫性を向上させることを目的としています。

主な変更点としては、`sourceDataFields`に関する説明文における用語の修正が挙げられます。「取得可能なインデックスフィールド」という表現から「引用参照に含まれるインデックスフィールド」という表現に変更されており、より明確な理解を促進しています。また、Azureポータルでのリソース管理に関する記述も、Microsoft Foundryに言及するように更新されています。

これにより、ユーザーがドキュメントを読んだ際の理解が深まり、特にREST APIの使用方法に関する指示がより明確に示されるようになっています。全体として、この変更は文の明確さを高め、ユーザーが必要な情報をより簡単に見つけられるようにするためのものです。

## articles/search/includes/quickstarts/agentic-retrieval-setup.md{#item-e5e297}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 10/16/2025
+ms.date: 12/22/2025
 ---
 
 ## Configure access
@@ -13,7 +13,7 @@ Before you begin, make sure you have permissions to access content and operation
 
 To configure access for this quickstart, select both of the following tabs.
 
-### [Azure AI Search](#tab/search-perms)
+### [Azure AI Search](#tab/search)
 
 Azure AI Search provides the agentic retrieval pipeline. Configure access for yourself and your search service to read and write data, interact with Foundry, and run the pipeline.
 
@@ -31,11 +31,11 @@ On your Azure AI Search service:
 
     + **Search Index Data Reader**
 
-### [Microsoft Foundry](#tab/foundry-perms)
+### [Microsoft Foundry](#tab/foundry)
 
-Foundry provides the Azure OpenAI models used for embeddings, query planning, and answer generation. Grant your search service permission to use these models.
+Microsoft Foundry provides the Azure OpenAI models used for embeddings, query planning, and answer generation. Grant your search service permission to use these models.
 
-On your Foundry resource:
+On your Microsoft Foundry resource:
 
 + Assign **Cognitive Services User** to the managed identity of your search service.
 
@@ -51,21 +51,21 @@ On your Foundry resource:
 
 ## Get endpoints
 
-Each Azure AI Search service and Foundry resource has an *endpoint*, which is a unique URL that identifies and provides network access to the resource. In a later section, you specify these endpoints to connect to your resources programmatically.
+Each Azure AI Search service and Microsoft Foundry resource has an *endpoint*, which is a unique URL that identifies and provides network access to the resource. In a later section, you specify these endpoints to connect to your resources programmatically.
 
 To get the endpoints for this quickstart, select both of the following tabs.
 
-### [Azure AI Search](#tab/search-endpoint)
+### [Azure AI Search](#tab/search)
 
 1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
 
 1. From the left pane, select **Overview**.
 
 1. Make a note of the endpoint, which should look like `https://my-service.search.windows.net`.
 
-### [Microsoft Foundry](#tab/foundry-endpoint)
+### [Microsoft Foundry](#tab/foundry)
 
-1. Sign in to the [Azure portal](https://portal.azure.com/) and select your Foundry resource.
+1. Sign in to the [Azure portal](https://portal.azure.com/) and select your Microsoft Foundry resource.
 
 1. From the left pane, select **Resource Management** > **Keys and Endpoint**.
 
@@ -77,10 +77,10 @@ To get the endpoints for this quickstart, select both of the following tabs.
 
 ## Deploy models
 
-To use agentic retrieval, you must deploy two Azure OpenAI models to your Foundry project:
+For this quickstart, you must deploy two Azure OpenAI models to your Microsoft Foundry project:
 
 + An embedding model for text-to-vector conversion. This quickstart uses `text-embedding-3-large`, but you can use any `text-embedding` model.
 
 + An LLM for query planning and answer generation. This quickstart uses `gpt-5-mini`, but you can use any [supported LLM for agentic retrieval](../../agentic-retrieval-how-to-create-knowledge-base.md#supported-models).
 
-For deployment instructions, see [Deploy Azure OpenAI models with Foundry](/azure/ai-foundry/how-to/deploy-models-openai).
+For deployment instructions, see [Deploy Azure OpenAI models with Microsoft Foundry](/azure/ai-foundry/how-to/deploy-models-openai).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルセットアップのクイックスタート"
}
```

### Explanation
このコードの変更は、MicrosoftDocsの「エージェントリトリーバルセットアップのクイックスタート」記事に対する更新を示しています。具体的には、11行の追加と11行の削除が行われ、合計で22行の変更が記録されています。これらの変更は、文書の正確性、一貫性および明確さを向上させることを目的としています。

変更点の主な内容には、次のようなものがあります：
- ドキュメントの日付が「10/16/2025」から「12/22/2025」に更新されました。
- Azure AI SearchおよびMicrosoft Foundryに関するタブの見出しが一貫性を持たせるために修正され、「アクセス権」や「エンドポイント」の見出しが明確に表示されています。
- Microsoft Foundryに関する表現が一貫して更新され、「Microsoft Foundryリソース」などの用語が採用されています。
- Azure OpenAIモデルをMicrosoft Foundryプロジェクトにデプロイする際の説明文も明確化されました。

これらの更新により、ユーザーは手続きの理解が容易になり、必要な情報にアクセスしやすくなります。全体として、この変更はドキュメントの明確さを向上させ、ユーザーのエクスペリエンスを改善することを目的としています。

## articles/search/includes/quickstarts/agentic-retrieval-typescript.md{#item-e6370b}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エージェントリトリーバル TypeScript クイックスタート"
}
```

### Explanation
このコードの変更は、MicrosoftDocsの「エージェントリトリーバル TypeScript クイックスタート」記事に対する大幅な改訂を示しています。具体的には、676行の追加と961行の削除が行われ、合計で1637行の変更が記録されています。この改訂は、ドキュメントの構造、内容、および全体的な目的において大きな影響を与える可能性があるため、重要な変更とみなされます。

主な変更点としては、次のような内容が含まれます：
- 内容の大規模な再構成が行われ、TypeScriptにおけるエージェントリトリーバルの実装方法や関連するAPIの使用法が更新されています。
- 新しいサンプルコードや実装方法が追加され、最新のベストプラクティスに従った形で具体的な手順が示されています。
- 古い情報や使用されていないコードが削除され、ドキュメントがよりクリーンで理解しやすいものになっています。

この大幅な変更は、読者が最新の情報をもとに正確な実装ができるようにするためのものであり、整合性と信頼性を高めることを目的としています。全般的に、この更新により、ユーザーはTypeScriptを使用したエージェントリトリーバルのプロセスを理解しやすくなり、実装しやすくなります。


