---
date: '2025-10-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c359015...MicrosoftDocs:2b0d8aa
summary: このコード差分は、Azure AI Searchドキュメントの多方面での改善を反映しており、特にRBACを用いたサインイン手順やエージェント的検索のガイドラインが強調されています。新機能として、ナレッジエージェントの作成についての詳細なガイドと新しいコード例が追加され、ユーザーの理解が向上しています。また、RBACに関するガイドも直感的に理解しやすく改善され、最新の技術ステータスが反映されています。全体として、これらの変更はAzure
  AI Searchの利用をより直感的かつ効率的にし、開発者が高度なシステム構築を行いやすくなることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c359015...MicrosoftDocs:2b0d8aa){target="_blank"}

# ハイライト

このコード差分は、Azure AI Searchドキュメントを複数の側面で改善し、特にRole-Based Access Control（RBAC）を使用したサインイン手順やエージェント的検索のためのガイドラインに重点が置かれています。いくつかの重要な新機能と文書のアップデートが含まれており、ユーザーの理解と操作性が向上するよう設計されています。

## 新機能
- Azure AI Searchのナレッジエージェントの作成に関する詳細なガイドが追加され、PythonとREST APIを使用した新しいコード例が提供されています。
- 知識ソースがエージェント的検索にどのように役立つかを示す内容がより具体的になり、特に「retrievalInstructions」の使用法が詳述されています。

## ブレイクイングチェンジ
- 特に大きな破壊的変更は見受けられませんが、表現の変更や計画指示の更新により、既存のシステムの微細な設定が必要な場合があります。

## その他のアップデート
- RBACを使用したPythonおよびREST APIガイドがより直感的に理解できるよう、Azureへのサインイン手順とユーザーの環境チェックが改善されました。
- ドキュメントの日付更新と用語の明確化が行われ、最新の技術ステータスに反映されています。

# 分析

このドキュメント変更は、Azure AI Searchを利用する開発者の体験を向上させるために行われた一連の修正と改善を示しています。

まず、RBACを使用したサインイン手順の改善は、ユーザーがシステムにアクセスする際の困難を軽減します。環境の誤設定を事前に防ぐことで、作業効率を高めることができるでしょう。特に、`az account show`コマンドの使用により、自分のサブスクリプションとテナント状況を簡単に確認できる点は評価できます。

次に、ナレッジエージェント作成の新しいガイドラインは、Azure AI Searchの高度な機能であるエージェント的検索を利用する上で、不可欠なリソースを提供しています。これにより、開発者はより複雑なクエリや検索フローを構築しやすくなっています。また、特にAPIキーやロールの割り当てといった認証方法の明確化はセキュリティとアクセス管理の改善に繋がります。

最後に、知識ソースの概要と操作手順の改善は、取り扱うデータの多様性に応じた柔軟なクエリの設計を可能にし、ユーザーが情報を迅速かつ的確に取得できるようになることを意図しています。特に、ベクトルフィールドの活用に関する詳細な説明は、検索結果の精度向上に寄与する重要な要素と言えます。

これらの変更を通じて、Azure AI Searchの活用がより直感的かつ効率的になると考えられます。ユーザーは最新の機能に迅速にアクセスできるようになり、開発者はこれを基にしたより高度なシステムを構築できるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-get-started-rbac-python.md](#item-de7760) | minor update | クイックスタートのRBAC Pythonガイドの更新 | modified | 10 | 2 | 12 | 
| [search-get-started-rbac-rest.md](#item-fd8ef4) | minor update | RBAC RESTガイドにおけるAzureサインイン手順の更新 | modified | 12 | 8 | 20 | 
| [search-agentic-retrieval-how-to-create.md](#item-310fbe) | new feature | エージェント的検索を用いたナレッジエージェントの作成方法の拡充 | modified | 202 | 45 | 247 | 
| [search-agentic-retrieval-how-to-index.md](#item-a078ea) | minor update | エージェント的検索用インデックス設計ガイドの更新 | modified | 8 | 17 | 25 | 
| [search-agentic-retrieval-how-to-retrieve.md](#item-5f7fc0) | minor update | 回答のフォーマットに関する文字列の修正 | modified | 1 | 1 | 2 | 
| [search-knowledge-source-overview.md](#item-1969d3) | minor update | 知識ソースの概要と操作手順の更新 | modified | 22 | 10 | 32 | 


# Modified Contents
## articles/search/includes/quickstarts/search-get-started-rbac-python.md{#item-de7760}

<details>
<summary>Diff</summary>
````diff
@@ -33,10 +33,18 @@ To sign in:
 
 1. On your local system, open a command-line tool.
 
-1. Sign in to Azure. If you have multiple subscriptions, select the one whose ID you obtained in [Get service information](#get-service-information).
+1. Check for the active tenant and subscription in your local environment.
 
    ```azurecli
-   az login
+   az account show
+   ```
+
+1. If the active subscription and tenant aren't valid for your search service, change the variables. You can check for the subscription ID on the search service overview page in the Azure portal. You can check for the tenant ID by clicking through to the subscription. In the Azure portal, the tenant ID is referred to as the **Parent management group**. Make a note of the values that are valid for your search service and run the following commands to update your local environment.
+
+   ```azurecli
+    az account set --subscription <your-subscription-id>
+
+    az login --tenant <your-tenant-id>
    ```
 
 ## Connect to Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートのRBAC Pythonガイドの更新"
}
```

### Explanation
この変更では、RBAC（Role-Based Access Control）を使用してAzureにサインインする手順を更新しています。具体的には、古い手順に代わって、現行のテナントとサブスクリプションの確認を優先し、適切な情報に基づいて環境を更新するための新しいステップが導入されました。変更内容には、以下のような新たな指示が含まれています:

1. Azureへのログインの代わりに、アカウント情報を表示するためのコマンド`az account show`を使用することが提案されています。
2. ユーザーが有効なサブスクリプションとテナントを確認して、必要があれば環境を更新する手順が明確に記載されています。この更新により、ユーザーは自身の環境を正確に設定できるようになり、初期設定の手間を減らすことができます。

これによって、ドキュメントがより使いやすく、ユーザーがAzure AI Searchに接続する際のフローが改善されました。

## articles/search/includes/quickstarts/search-get-started-rbac-rest.md{#item-fd8ef4}

<details>
<summary>Diff</summary>
````diff
@@ -25,35 +25,39 @@ Keyless connections provide enhanced security through granular permissions and i
 
 [!INCLUDE [Setup](./search-get-started-rbac-setup.md)]
 
-## Get token
-
-Before you connect to your Azure AI Search service, use the Azure CLI to sign in to the subscription that contains your service and generate a Microsoft Entra ID token. You use this token to authenticate requests in the next section.
-
-To get your token:
+## Sign in to Azure
 
-1. On your local system, open a command-line tool.
+Before you connect to your Azure AI Search service, use the Azure CLI to sign in to the subscription that contains your service.
 
 1. Check for the active tenant and subscription in your local environment.
 
    ```azurecli
    az account show
    ```
 
-1. If the active subscription and tenant aren't valid for your search service, change the variables. You can check for the subscription ID on the search service overview page in the Azure portal. You can check for the tenant ID by clicking through to the subscription. Make a note of the values that are valid for your search service and run the following commands to update your local environment.
+1. If the active subscription and tenant aren't valid for your search service, change the variables. You can check for the subscription ID on the search service overview page in the Azure portal. You can check for the tenant ID by clicking through to the subscription. In the Azure portal, the tenant ID is referred to as the **Parent management group**. Make a note of the values that are valid for your search service and run the following commands to update your local environment.
 
    ```azurecli
     az account set --subscription <your-subscription-id>
 
     az login --tenant <your-tenant-id>
    ```
 
+## Get token
+
+REST API calls require the inclusion of a Microsoft Entra ID token. You use this token to authenticate requests in the next section.
+
+To get your token:
+
+1. On your local system, open a command-line tool.
+
 1. Generate an access token.
 
    ```azurecli
    az account get-access-token --scope https://search.azure.com/.default --query accessToken --output tsv
    ```
 
-1. Make a note of the token output.
+1. Copy the token output.
 
 ## Connect to Azure AI Search
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBAC RESTガイドにおけるAzureサインイン手順の更新"
}
```

### Explanation
この変更は、Azure AI Searchサービスに接続する際の手順を改善するために、RBAC（Role-Based Access Control）を使用したREST APIガイドを更新したものです。主な変更点は以下の通りです：

1. **サインイン手順の整理**: 最初のステップとして「Azureにサインイン」という見出しが追加され、サインイン手順が明確に整理されました。これにより、ユーザーは自分の環境に利用可能なテナントとサブスクリプションを確認し、適切にログインする方法を簡単に理解できるようになりました。

2. **トークン取得手順の追加**: REST APIの呼び出しに必須なMicrosoft Entra IDトークンを取得する手順が明確に示されました。これにより、ユーザーはトークンを生成し、その値をコピーすることで次のリクエストに使用できるようになります。

3. **コマンドの具体化**: コマンドの説明も明確化され、ユーザーは必要な環境設定をより簡潔に行うことができます。特に、サブスクリプションとテナントの確認や、トークンの取得に関する具体的なコマンドが示されています。

この変更により、ドキュメント全体がより使いやすく、ユーザーがAzure AI Searchに接続するプロセスが一層スムーズに進むようになっています。

## articles/search/search-agentic-retrieval-how-to-create.md{#item-310fbe}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/29/2025
+ms.date: 09/30/2025
 ---
 
 # Create a knowledge agent in Azure AI Search
@@ -31,17 +31,17 @@ After you create a knowledge agent, you can update its properties at any time. I
 
 + Familiarity with [agentic retrieval concepts and use cases](search-agentic-retrieval-concept.md).
 
-+ A [supported chat completion model](#supported-models) on Azure OpenAI.
-
 + Azure AI Search, in any [region that provides semantic ranker](search-region-support.md), on the basic pricing tier or higher. Your search service must have a [managed identity](search-how-to-managed-identities.md) for role-based access to the model.
 
-+ Permissions on Azure AI Search. **Search Service Contributor** can create and manage a knowledge agent. **Search Index Data Reader** can run queries. Instructions are provided in this article. [Quickstart: Connect to a search service](/azure/search/search-get-started-rbac?pivots=rest) explains how to configure roles and get a personal access token for REST calls.
++ A [supported chat completion model](#supported-models) on Azure OpenAI.
 
-+ A [knowledge source](search-knowledge-source-overview.md) that identifies searchable content used by the agent. It can be either a [search index knowledge source](search-knowledge-source-how-to-index.md) or a [blob knowledge source](search-knowledge-source-how-to-blob.md)
++ Permission requirements. **Search Service Contributor** can create and manage a knowledge agent. **Search Index Data Reader** can run queries. Instructions are provided in this article. [Quickstart: Connect to a search service](/azure/search/search-get-started-rbac?pivots=rest) explains how to configure roles and get a personal access token for REST calls.
+
++ Content requirements. A [knowledge source](search-knowledge-source-overview.md) that identifies searchable content used by the agent. It can be either a [search index knowledge source](search-knowledge-source-how-to-index.md) or a [blob knowledge source](search-knowledge-source-how-to-blob.md)
 
 + API requirements. To create or use a knowledge agent, use the [2025-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) data plane REST API. Or, use a preview package of an Azure SDK that provides knowledge agent APIs: [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1170-beta3-2025-03-25), [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md). **There's no Azure portal support knowledge agents at this time**.
 
-To follow the steps in this guide, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending preview REST API calls to Azure AI Search. T
+To follow the steps in this guide, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending preview REST API calls to Azure AI Search or the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter package](https://pypi.org/project/jupyter/).
 
 ## Deploy a model for agentic retrieval
 
@@ -72,7 +72,7 @@ Use Azure OpenAI or an equivalent open source model:
 
 Azure AI Search needs access to the chat completion model. You can use key-based or role-based authentication (recommended).
 
-### Use role-based authentication
+### [**Use roles**](#tab/rbac)
 
 If you're using role-based authentication, on your Azure OpenAI resource, assign the **Cognitive Services User** role to a search service managed identity.
 
@@ -96,7 +96,7 @@ In Azure, you must have **Owner** or **User Access Administrator** permissions o
 > [!IMPORTANT]
 > If you use role-based authentication, be sure to remove all references to the API key in your requests. In a request that specifies both approaches, the API key is used instead of roles.
 
-### Use key-based authentication
+### [**Use keys**](#tab/keys)
 
 You can use API keys if you don't have permission to create role assignments.
 
@@ -114,10 +114,94 @@ You can use API keys if you don't have permission to create role assignments.
       @api-key: {{search-api-key}}
    ```
 
+---
+
 ## Check for existing knowledge agents
 
 The following request lists knowledge agents by name. Within the knowledge agents collection, all knowledge agents must be uniquely named. It's helpful to know about existing knowledge agents for reuse or for naming new agents.
 
+### [**Python**](#tab/python-get-agents)
+
+```python
+# List existing knowledge agents on the search service
+from azure.search.documents.indexes import SearchIndexClient
+
+index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
+
+try:
+    agents = {agent.name: agent for agent in index_client.list_agents(api_version=search_api_version)}
+    print(f"\nKnowledge agents on search service '{search_endpoint}':")
+    
+    if agents:
+        print(f"Found {len(agents)} knowledge agent(s):")
+        for i, (name, agent) in enumerate(sorted(agents.items()), 1):
+            print(f"{i}. Name: {name}")
+            if agent.knowledge_sources:
+                ks_names = [ks.name for ks in agent.knowledge_sources]
+                print(f"   Knowledge Sources: {', '.join(ks_names)}")
+            print()
+    else:
+        print("No knowledge agents found.")
+        
+except Exception as e:
+    print(f"Error listing knowledge agents: {str(e)}")
+```
+
+You can also return a single agent by name to review its JSON definition.
+
+```python
+# Get knowledge agent definition for earth-knowledge-agent-2
+from azure.search.documents.indexes import SearchIndexClient
+import json
+
+index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
+
+try:
+    agent_name = "earth-knowledge-agent-2"
+    agent = index_client.get_agent(agent_name, api_version=search_api_version)
+    
+    print(f"Knowledge agent '{agent_name}':")
+    print(f"Name: {agent.name}")
+    
+    if agent.description:
+        print(f"Description: {agent.description}")
+    
+    if agent.models:
+        print(f"\nModels ({len(agent.models)}):")
+        for i, model in enumerate(agent.models, 1):
+            print(f"  {i}. {type(model).__name__}")
+            if hasattr(model, 'azure_open_ai_parameters'):
+                params = model.azure_open_ai_parameters
+                print(f"     Resource: {params.resource_url}")
+                print(f"     Deployment: {params.deployment_name}")
+                print(f"     Model: {params.model_name}")
+    
+    if agent.knowledge_sources:
+        print(f"\nKnowledge Sources ({len(agent.knowledge_sources)}):")
+        for i, ks in enumerate(agent.knowledge_sources, 1):
+            print(f"  {i}. {ks.name} (threshold: {ks.reranker_threshold})")
+    
+    if agent.output_configuration:
+        config = agent.output_configuration
+        print(f"\nOutput: {config.modality} (activity: {config.include_activity})")
+    
+    # Full JSON definition
+    print(f"\nJSON definition:")
+    print(json.dumps(agent.as_dict(), indent=2))
+    
+except Exception as e:
+    print(f"Error: {str(e)}")
+    
+    # Show available agents
+    try:
+        agents = {agent.name: agent for agent in index_client.list_agents(api_version=search_api_version)}
+        print(f"\nAvailable agents: {list(agents.keys())}")
+    except Exception:
+        print("Could not list available agents.")
+```
+
+### [**REST**](#tab/rest-get-agents)
+
 ```http
 # List knowledge agents
 GET {{search-url}}/agents?api-version=2025-08-01-preview
@@ -134,6 +218,8 @@ GET {{search-url}}/agents/{{agent-name}}?api-version=2025-08-01-preview
    Authorization: Bearer {{accessToken}}
 ```
 
+---
+
 ## Create a knowledge agent
 
 A knowledge agent drives the agentic retrieval pipeline. In application code, it's called by other agents or chat bots. 
@@ -142,6 +228,44 @@ Its composition consists of connections between *knowledge sources* (searchable
 
 To create an agent, use the 2025-08-01-preview data plane REST API or an Azure SDK preview package that provides equivalent functionality.
 
+Recall that you must have an existing [knowledge source](search-knowledge-source-overview.md) to give to the agent.
+
+### [**Python**](#tab/python-create-agent)
+
+```python
+from azure.search.documents.indexes.models import KnowledgeAgent, KnowledgeAgentAzureOpenAIModel, KnowledgeSourceReference, AzureOpenAIVectorizerParameters, KnowledgeAgentOutputConfiguration, KnowledgeAgentOutputConfigurationModality
+from azure.search.documents.indexes import SearchIndexClient
+
+aoai_params = AzureOpenAIVectorizerParameters(
+    resource_url=aoai_endpoint,
+    deployment_name=aoai_gpt_deployment,
+    model_name=aoai_gpt_model,
+)
+
+output_cfg = KnowledgeAgentOutputConfiguration(
+    modality=KnowledgeAgentOutputConfigurationModality.ANSWER_SYNTHESIS,
+    include_activity=True,
+)
+
+agent = KnowledgeAgent(
+    name=knowledge_agent_name,
+    models=[KnowledgeAgentAzureOpenAIModel(azure_open_ai_parameters=aoai_params)],
+    knowledge_sources=[
+        KnowledgeSourceReference(
+            name=knowledge_source_name,
+            reranker_threshold=2.5,
+        )
+    ],
+    output_configuration=output_cfg,
+)
+
+index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
+index_client.create_or_update_agent(agent, api_version=search_api_version)
+print(f"Knowledge agent '{knowledge_agent_name}' created or updated successfully.")
+```
+
+### [**REST**](#tab/rest-create-agent)
+
 ```http
 @search-url=<YOUR SEARCH SERVICE URL>
 @agent-name=<YOUR AGENT NAME>
@@ -242,14 +366,68 @@ PUT {{search-url}}/agents/{{agent-name}}?api-version=2025-08-01-preview
 
 + `encryptionKey` is optional. Include an encryption key definition if you're supplementing with [customer-managed keys](search-security-manage-encryption-keys.md).
 
-<!-- --- -->
+---
 
 ## Query the knowledge agent
 
-Call the **retrieve** action on the knowledge agent object to confirm the model connection and return a response. Use the [2025-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) data plane REST API or an Azure SDK preview package that provides equivalent functionality for this task.
+Call the **retrieve** action on the knowledge agent object to confirm the model connection and return a response. Use the [2025-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) data plane REST API or an Azure SDK preview package that provides equivalent functionality for this task. For more information about the **retrieve** API and the shape of the response, see [Retrieve data using a knowledge agent in Azure AI Search](search-agentic-retrieval-how-to-retrieve.md).
 
 Replace "where does the ocean look green?" with a query string that's valid for your search index.
 
+### [**Python**](#tab/python-query-agent)
+
+Start with instructions.
+
+```python
+instructions = """
+A Q&A agent that can answer questions about the Earth at night.
+If you don't have the answer, respond with "I don't know".
+"""
+
+messages = [
+    {
+        "role": "system",
+        "content": instructions
+    }
+]
+```
+
+Then send the query.
+
+```python
+from azure.search.documents.agent import KnowledgeAgentRetrievalClient
+from azure.search.documents.agent.models import KnowledgeAgentRetrievalRequest, KnowledgeAgentMessage, KnowledgeAgentMessageTextContent, SearchIndexKnowledgeSourceParams
+
+agent_client = KnowledgeAgentRetrievalClient(endpoint=search_endpoint, agent_name=knowledge_agent_name, credential=credential)
+query_1 = """
+    where does the ocean look green??
+    """
+
+messages.append({
+    "role": "user",
+    "content": query_1
+})
+
+req = KnowledgeAgentRetrievalRequest(
+    messages=[
+        KnowledgeAgentMessage(
+            role=m["role"],
+            content=[KnowledgeAgentMessageTextContent(text=m["content"])]
+        ) for m in messages if m["role"] != "system"
+    ],
+    knowledge_source_params=[
+        SearchIndexKnowledgeSourceParams(
+            knowledge_source_name=knowledge_source_name,
+        )
+    ]
+)
+
+result = agent_client.retrieve(retrieval_request=req, api_version=search_api_version)
+print(f"Retrieved content from '{knowledge_source_name}' successfully.")
+```
+
+### [**REST**](#tab/rest-query-agent)
+
 ```http
 # Send grounding request
 POST {{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-08-01-preview
@@ -301,55 +479,34 @@ The response to the previous query might look like this:
         }
       ]
     }
-  ],
+  ]
 ```
 
+---
 
-<!-- ```http
-# Send grounding request
-POST {{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-08-01-preview
-   Content-Type: application/json
-   Authorization: Bearer {{accessToken}}
+## Delete an agent
 
-{
-    "messages" : [
-            {
-                "role" : "assistant",
-                "content" : [
-                  { "type" : "text", "text" : "You are a helpful assistant for Contoso Human Resources. You have access to a search index containing guidelines about health care coverage for Washington state. If you can't find the answer in the search, say you don't know." }
-                ]
-            },
-            {
-                "role" : "user",
-                "content" : [
-                  { "type" : "text", "text" : "What are my vision benefits?" }
-                ]
-            }
-        ],
-    "targetIndexParams" :  [
-        { 
-            "indexName" : "{{index-name}}",
-            "filterAddOn" : "State eq 'WA'",
-            "IncludeReferenceSourceData": true,
-            "rerankerThreshold" : 2.5
-            "maxDocsForReranker": 250
-        } 
-    ]
-}
-``` -->
+If you no longer need the agent, or if you need to rebuild it on the search service, use this request to delete the current object.
 
-For more information about the **retrieve** API and the shape of the response, see [Retrieve data using a knowledge agent in Azure AI Search](search-agentic-retrieval-how-to-retrieve.md).
+### [**Python**](#tab/python-delete-agent)
 
-## Delete an agent
+```python
+from azure.search.documents.indexes import SearchIndexClient
 
-If you no longer need the agent, or if you need to rebuild it on the search service, use this request to delete the current object.
+index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
+index_client.delete_agent(knowledge_agent_name)
+print(f"Knowledge agent '{knowledge_agent_name}' deleted successfully.")
+```
 
+### [**REST**](#tab/rest-delete-agent)
 ```http
 # Delete agent
 DELETE {{search-url}}/agents/{{agent-name}}?api-version=2025-08-01-preview
    Authorization: Bearer {{accessToken}}
 ```
 
+---
+
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "エージェント的検索を用いたナレッジエージェントの作成方法の拡充"
}
```

### Explanation
この変更は、Azure AI Searchのナレッジエージェントを作成するための手順を大幅に拡充し、新しい機能を追加した内容です。主な更新点は以下の通りです：

1. **新しいセクションの追加**: 知識エージェントを作成するための詳細な手順が追加され、PythonおよびREST APIを使用した具体的なコード例が提供されています。これにより、開発者はエージェントの作成と管理を容易に行えるようになります。

2. **認証方法の明確化**: Azure OpenAIリソースへのロールベースの認証やキーによる認証の使用が説明され、エージェントの作成に必要な具体的な権限が明示されました。これにはAPIキーや役割の割り当てに関する情報も含まれています。

3. **エラー処理と例外の処理**: ユーザーが知識エージェントのリストや詳細を取得する際のエラー処理の方法も含まれ、実装の信頼性を向上させています。

4. **全体的な構造の見直し**: コンテンツの構造が整理され、必要な手順や要件が明確に提示されているため、使用者が情報を迅速に把握できるようになっています。また、エージェントの削除方法や関連コンテンツへのリンクも新たに追加されています。

これにより、ユーザーはAzure AI Searchを用いたエージェントの作成や管理に関する知識を深め、より効果的に利用できるようになります。

## articles/search/search-agentic-retrieval-how-to-index.md{#item-a078ea}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/29/2025
+ms.date: 10/01/2025
 ---
 
 # Design an index for agentic retrieval in Azure AI Search
@@ -16,13 +16,13 @@ ms.date: 08/29/2025
 
 In Azure AI Search, *agentic retrieval* is a new parallel query architecture that uses a chat completion model for query planning, generating subqueries that broaden the scope of what's searchable and relevant.
 
-Subqueries are created internally. Certain aspects of the subqueries are determined by your search index. This article explains which index elements have an effect on agentic retrieval. None of the required elements are new or specific to agentic retrieval, which means you can use an existing index if it meets the criteria identified in this article, even if it was created using earlier API versions.
+Subqueries are created internally. Certain aspects of the subqueries are determined by your search index. This article explains which index elements have an effect on the query logic. None of the required elements are new or specific to agentic retrieval, which means you can use an existing index if it meets the criteria identified in this article, even if it was created using earlier API versions.
 
-A search index that's used in agentic retrieval is specified as *knowledge source* and is either:
+A search index that's used in agentic retrieval is specified as *knowledge source* on a *knowledge agent*, and is either:
 
 + An existing indexing containing searchable content. This index is made available to agentic retrieval through a [search index knowledge source](search-knowledge-source-how-to-index.md) definition.
 
-+ A generated index created from a generated blob indexer pipeline. This index is generated and populated using information from a [blob knowledge source](search-knowledge-source-how-to-blob.md). It's based on a template that meets all of the criteria for knowledge agents and agentic retrieval. 
++ A generated index created from a blob indexer pipeline. This index is generated and populated using information from a [blob knowledge source](search-knowledge-source-how-to-blob.md). It's based on a template that meets all of the criteria for knowledge agents and agentic retrieval. 
 
 ## Criteria for agentic retrieval
 
@@ -64,7 +64,7 @@ Here's an example index that works for agentic retrieval. It meets the criteria
       "synonymMaps": []
     },
     {
-      "name": "page_chunk_text_3_large", "type": "Collection(Edm.Single)",
+      "name": "page_chunk_vector_text_3_large", "type": "Collection(Edm.Single)",
       "searchable": true, "retrievable": false, "filterable": false, "sortable": false, "facetable": false,
       "dimensions": 3072,
       "vectorSearchProfile": "hnsw_text_3_large",
@@ -91,9 +91,7 @@ Here's an example index that works for agentic retrieval. It meets the criteria
   "tokenizers": [],
   "tokenFilters": [],
   "charFilters": [],
-  "similarity": {
-    "@odata.type": "#Microsoft.Azure.Search.BM25Similarity"
-  },
+  "similarity": {},
   "semantic": {
     "defaultConfiguration": "semantic_config",
     "configurations": [
@@ -152,21 +150,14 @@ Here's an example index that works for agentic retrieval. It meets the criteria
 
 In agentic retrieval, a large language model (LLM) is used twice. First, it's used to create a query plan. After the query plan is executed and search results are generated, those results are passed to the LLM again, this time as grounding data that's used to formulate an answer. 
 
-LLMs consume and emit tokenized strings of human readable plain text content. For this reason, you must have `searchable` fields that provide plain text strings, and are `retrievable` in the response. Vector fields and vector search are also important because they add similarity search to information retrieval. Vectors enhance and improve the quality of search, but aren't otherwise strictly required. Azure AI Search has built-in capabilities that [simplify and automate vectorization](vector-search-overview.md).
+LLMs consume and emit tokenized strings of human readable plain text content. For this reason, you must have `searchable` fields that provide plain text strings, and are `retrievable` in the response. Vector fields and vector search are also important because they add similarity search to information retrieval. Vectors enhance and improve the quality of search that produces grounding data, but aren't otherwise strictly required. Azure AI Search has built-in capabilities that [simplify and automate vectorization](vector-search-overview.md).
 
 The previous example index includes a vector field that's used at query time. You don't need the vector in results because it isn't human or LLM readable, but notice that its `searchable` for vector search. Since you don't need vectors in the response, both `retrievable` and `stored` are false. 
 
-The vectorizer defined in the vector search configuration is critical. It determines whether your vector field is used during query execution. The vectorizer encodes subqueries into vectors at query time for similarity search over the vectors. The vectorizer must be the same embedding model used to create the vectors in the index.
+The vectorizer defined in the vector search configuration is critical. It determines whether your vector field is used during query execution. The vectorizer encodes string subqueries into vectors at query time for similarity search over the vectors. The vectorizer must be the same embedding model used to create the vectors in the index.
 
 All `searchable` fields are included in query execution. There's no support for a `select` statement that explicitly states which fields to query.
 
-<!-- 
-> [!div class="checklist"]
-> + A fields collection with `searchable` text and vetor fields, and `retrievable` text fields
-> + Vector fields that are queried are fields having a vectorizer
-> + Fields selected in the response string are semantic fields (title, terms, content)
-> + Fields in reference source data are all `retrievable` fields, assuming reference source data is true -->
-
 ## Add a description
 
 An index `description` field is a user-defined string that you can use to provide guidance to LLMs and Model Context Protocol (MCP) servers when deciding to use a specific index for a query. This human-readable text is invaluable when a system must access several indexes and make a decision based on the description. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント的検索用インデックス設計ガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるエージェント的検索のためのインデックス設計に関する文書を更新するもので、いくつかの重要な修正が含まれています。

1. **用語の明確化**: "knowledge agent" に関連するインデックスが具体的に「knowledge source」として記述され、より明確な表現が使用されました。これにより、読者はエージェント的検索におけるインデックスの役割を理解しやすくなります。

2. **技術的な表現の修正**: 文章の一部が変更され、エージェント的検索のクエリロジックに関連するインデックス要素がより具体的に説明されています。これにより、開発者がどのインデックス要素がどのように影響するのかを把握しやすくなっています。

3. **コード例の更新**: インデックスの例におけるフィールド名の修正などが行われ、最新の設定に合わせて内容が更新されました。この変更により、具体的な実装に役立つ情報が提供されています。

4. **ベクトルフィールドの使用に関する説明の強化**: ベクトルフィールドとその検索能力に関するセクションが強化され、特にクエリ実行時のベクトルの利用方法が詳述されています。これによって、読者はベクトルを用いた情報検索の重要性とその実装方法を理解しやすくなります。

全体として、このドキュメントの更新は、Azure AI Searchを利用したエージェント的検索の理解を深め、実装における指針を提供することを目的としています。

## articles/search/search-agentic-retrieval-how-to-retrieve.md{#item-5f7fc0}

<details>
<summary>Diff</summary>
````diff
@@ -69,7 +69,7 @@ POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-08-0
                 "content" : [
                   { "type" : "text", "text" : "You can answer questions about the Earth at night.
                     Sources have a JSON format with a ref_id that must be cited in the answer.
-                    If you do not have the answer, respond with 'I don't know'." }
+                    If you do not have the answer, respond with 'I do not know'." }
                 ]
             },
             {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "回答のフォーマットに関する文字列の修正"
}
```

### Explanation
この変更は、Azure AI Searchのエージェント的検索に関する文書の一部を微調整するもので、回答フォーマットに関する表現を修正しています。具体的には、プログラムからの応答として指示されているフレーズが変更されました：

- 「If you do not have the answer, respond with 'I don't know'.」から「If you do not have the answer, respond with 'I do not know'.」に修正されました。この変更により、より正式な表現が使用され、応答の整合性を保つことが意図されています。

全体として、この変更は文書の明瞭性とプロフェッショナル性を向上させるためのものであり、ユーザーがエージェントからの応答形式を理解しやすくすることを目的としています。

## articles/search/search-knowledge-source-overview.md{#item-1969d3}

<details>
<summary>Diff</summary>
````diff
@@ -7,22 +7,24 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/29/2025
+ms.date: 10/01/2025
 ---
 
 # Create a knowledge source
 
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
 A knowledge source wraps a search index with extra properties for agentic retrieval. It's a required definition in a knowledge agent. We provide guidance on how to create specific knowledge sources, but generally, you can:
 
 + Create multiple knowledge sources as top-level resources on your search service.
 
-+ Reference one or more knowledge sources in a knowledge agent. In an agentic retrieval pipeline, it's possible to query against multiple knowledge sources in single request. Subqueries are generated for each knowledge sources. Top results are returned in the retrieval response.
++ Reference one or more knowledge sources in a knowledge agent. In an agentic retrieval pipeline, it's possible to query against multiple knowledge sources in single request. Subqueries are generated for each knowledge source. Top results are returned in the retrieval response.
 
-Make sure you have at least one knowledge source before creating a knowledge agent. The full specification of a knowledge agent is in the [REST API reference](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true). 
+Make sure you have at least one knowledge source before creating a knowledge agent. The full specification of a knowledge source and a knowledge agent is in the [REST API reference](/rest/api/searchservice). 
 
 ## Key points about a knowledge source
 
-+ Creation path: first create knowledge source, then create knowledge agents. Deletion path: update or delete knowledge agents, delete knowledge sources last.
++ Creation path: first create a knowledge source, then create a knowledge agent. Deletion path: update or delete knowledge agents, delete knowledge sources last.
 
 + A knowledge source, its index, and the knowledge agent must all exist on the same search service.
 
@@ -53,15 +55,15 @@ When you have multiple knowledge sources, set the following properties to bias q
 + Setting `alwaysQuerySource` forces query planning to always include the knowledge source.
 + Setting `retrievalInstructions` provides guidance that includes or excludes a knowledge source. 
 
-Retrieval instructions are sent as a prompt to the large language model (LLM) used for query planning. This prompt is helpful when you have multiple knowledge sources and want to provide guidance on when to use each one. For example, if you have separate indexes for product information, job postings, and technical support, the retrieval instructions might say "use the jobs index only if the question is about a job application."
+Retrieval instructions are sent as a user-defined prompt to the large language model (LLM) used for query planning. This prompt is helpful when you have multiple knowledge sources and want to provide guidance on when to use each one. For example, if you have separate indexes for product information, job postings, and technical support, the retrieval instructions might say "use the jobs index only if the question is about a job application."
 
 The `alwaysQuerySource` property overrides `retrievalInstructions`. You should set `alwaysQuerySource` to false when providing retrieval instructions.
 
 ### Attempt fast path processing
 
 Fast path is opportunistic query processing that approaches the millisecond query performance of regular search. If you enable it, the search engine attempts fast path under the following conditions:
 
-+ `attemptFastPath` is set to true in `knowledgeSourceReferences`.
++ `attemptFastPath` is set to true in `outputConfiguration`.
 
 + The query input is a single message that's fewer than 512 characters.
 
@@ -75,13 +77,23 @@ Under fast path, `retrievalInstructions` are ignored. In general, `alwaysQuerySo
 
 To achieve the fastest possible response times, follow these best practices:
 
-+ Set `modality` to `answerSynthesis` to get a response framed as an LLM-formulated answer. It takes a few extra seconds, but it improves the quality of the response and saves time overall if the answer is usable without further LLM processing.
+1. In the knowledge agent:
+
+   + Set `outputConfiguration.attemptFastPath` to true.
+
+   + Set `outputConfiguration.modality` to `answerSynthesis` to get a response framed as an LLM-formulated answer. It takes a few extra seconds, but it improves the quality of the response and saves time overall if the answer is usable without further LLM processing.
+
+   + Retain `outputConfiguration.includeActivity` set to true (default setting) for insights about query execution and elapsed time.
+
+   + Retain `knowledgeSource.includeReferences` set to true (default setting) for details about each individually scored result.
+
+   + Set `knowledgeSources.alwaysQuerySource` to true.
 
-+ Retain `includeActivity` set to true (default setting) for insights about query execution and elapsed time.
+   + Set `knowledgeSources.retrievalInstructions` to false.
 
-+ Retain `includeReferences` set to true (default setting) for details about each individually scored result.
+   + Set `knowledgeSources.includeReferenceSourceData` to false if you don't need the verbatim content from the index. Omitting this information simplifies the response and makes it more readable.
 
-+ Set `includeReferenceSourceData` to false if you don't need the verbatim content from the index. Omitting this information simplifies the response and makes it more readable.
+1. In the [retrieve action](search-agentic-retrieval-how-to-retrieve.md), provide a single message query that's fewer than 512 characters.
 
 ## Delete a knowledge source
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ソースの概要と操作手順の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける知識ソースの概要に関する文書を更新し、複数の重要な点を追加・修正しています。

1. **日付の更新**: ドキュメントの日付が「2025年8月29日」から「2025年10月1日」に更新され、最新の状態が反映されています。

2. **知識ソースの説明の強化**: 知識ソースがエージェント的検索のために検索インデックスをラップし、追加プロパティを持つことが強調されています。また、知識エージェント内での知識ソースの参照方法が明確に示され、同時に複数の知識ソースに対するクエリが可能であることが説明されています。

3. **クエリ計画に関する指示**: 「retrievalInstructions」についての説明が強化され、特定の条件下での使用方法が詳述されました。

4. **高速処理の実装手順**: 高速パス処理に関する条件が明記され、実装に役立つ新しい手順が追加されました。これにより、ユーザーがクエリのパフォーマンスを向上させるための具体的な設定方法を理解しやすくなっています。

5. **小さな表現の修正**: 一部の文中での表現が修正され、言語がより明確で一貫性のあるものに変更されています。

全体として、この更新は、知識ソースの理解を深め、実装手順をより具体的かつ実用的にすることを目的としています。これにより、ユーザーはAzure AI Searchにおける知識ソースの利用をより効果的に行えるようになります。


