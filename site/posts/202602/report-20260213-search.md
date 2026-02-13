---
date: '2026-02-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e4d4d10...MicrosoftDocs:e20ff5a
summary: この文書更新では、Azure AI Searchに関連する新機能の追加と重要な修正が行われました。具体的には、Microsoft Entra IDを利用したキーなし認証の情報が新たに追加され、API仕様が改訂されたことでリトリーバルプロセスが明確化されました。また、知識ベースの要件が詳細化され、全体の整合性と可読性が向上しました。これにより、ユーザーはデータ取得の過程でのトラブルシューティングやパフォーマンス最適化が容易になるとともに、技術的な透明性が向上しました。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e4d4d10...MicrosoftDocs:e20ff5a){target="_blank"}

<format>
# ハイライト
この一連の文書更新では、新しい機能の追加およびいくつかの重要な修正が行われました。特に、知識ベースを用いたAzure AI Searchのプロセスに関し、要件の追加とドキュメンテーションが強化されました。また、API呼び出しの仕様が改訂され、関連するリンクやフォーマットが調整されています。

## 新機能
- 「agentic-retrieval-how-to-create-pipeline.md」では、Microsoft Entra IDを用いたキーなしの認証のための「Azure CLI」に関する情報が追加されました。

## 破壊的変更
- 「agentic-retrieval-how-to-retrieve.md」では、エージェントリトリーバルパイプラインにおける主要なアップデートが行われ、API仕様とリトリーバルアクションのプロセスが明確化されました。

## その他の更新
- 知識ベースの要件が詳細化され、LLMや認証に関する情報が追加されました。
- リンクやフォーマットの調整によって、ドキュメント全体の整合性と可読性が向上しました。

# 洞察
このドキュメント更新は、Azure AI Searchを利用する組織や開発者にとって特に重要です。知識ベースからデータを取得するプロセスは、検索サービスの精度と効率を大きく左右します。このため、更新された要件、特に資格情報と権限に関する新たな指針が強調されていることは、システムを遵守する上で重要です。

また、APIの仕様が具体的に明文化されたことで、リトリーバルアクションや応答構造を理解しやすくなりました。この変更は、新しいAPIへの移行のための参照や、より効率的で効果的なエージェント設計の基盤を提供します。これによりユーザーは、データ取得の際のトラブルシューティングやパフォーマンス最適化が容易になるでしょう。

さらに、ドキュメントのリンクとテキストの調整により、特に新しいユーザーに対して、必要な情報を迅速かつ正確にアクセスできるよう配慮されています。このような一連の改訂は、技術的な透明性を向上させ、長期的なメンテナンスの容易化に寄与するものです。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-answer-synthesis.md](#item-f44e99) | minor update | 知識ベースの要件を更新 | modified | 6 | 2 | 8 | 
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | Azure CLIに関する情報の追加 | modified | 3 | 3 | 6 | 
| [agentic-retrieval-how-to-retrieve.md](#item-d739cf) | breaking change | エージェントリトリーバルパイプラインの更新と明確化 | modified | 162 | 149 | 311 | 
| [agentic-retrieval-how-to-set-retrieval-reasoning-effort.md](#item-141e97) | minor update | リトリーバル推論努力の設定に関する要件の明確化 | modified | 5 | 4 | 9 | 
| [get-started-portal-agentic-retrieval.md](#item-2bf1dc) | minor update | アクティビティログの参照リンクの修正 | modified | 1 | 1 | 2 | 
| [search-region-support.md](#item-25b0f1) | minor update | Central US地域の制限に関する説明の修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-answer-synthesis.md{#item-f44e99}

<details>
<summary>Diff</summary>
````diff
@@ -30,9 +30,13 @@ You can enable answer synthesis in two ways:
 
 ## Prerequisites
 
-+ A knowledge base that uses the [2025-11-01-preview syntax](agentic-retrieval-how-to-migrate.md).
++ An Azure AI Search service with a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) that specifies an LLM.
 
-+ [Visual Studio Code](https://code.visualstudio.com/) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) or a preview Azure SDK package that provides the knowledge base REST APIs.
++ Permissions to update the knowledge base. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
+
++ For outbound calls to the LLM, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource.
+
++ The [2025-11-01-preview](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) REST API or an equivalent Azure SDK preview package: [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
 
 ## Enable answer synthesis in a knowledge base
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ベースの要件を更新"
}
```

### Explanation
この変更では、`agentic-retrieval-how-to-answer-synthesis.md`という文書の一部が更新されました。具体的には、「回答合成を有効にするための前提条件」セクションが強化され、新たに必要な要件が追加されました。

変更内容としては、まず、知識ベースを指定するための「Azure AI Searchサービス」とその「LLM」の明記が求められるようになりました。また、知識ベースの更新には、**Search Service Contributor**の役割が割り当てられたユーザーアカウントでの「キーなし認証」の設定が推奨されています。さらに、LLMへのアウトバウンドコールには、**Cognitive Services User**の権限を持つ「マネージドアイデンティティ」が必要であることが補足されています。

これに加えて、REST APIや複数のプログラミング言語（.NET、Java、JavaScript、Python）向けのAzure SDKのリンクも更新され、最新情報へのアクセスが容易になっています。これらの修正は、ドキュメントの利用者に対して、特に知識ベースの設定と管理における明確なガイダンスを提供します。

## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -46,9 +46,9 @@ In this tutorial, you:
 
 + The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-- The latest version of [Python](https://www.python.org/downloads/).
++ The latest version of [Python](https://www.python.org/downloads/).
 
-- [Visual Studio Code](https://code.visualstudio.com/download) with the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions.
++ [Visual Studio Code](https://code.visualstudio.com/download) with the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions.
 
 ## Understand the solution
 
@@ -584,7 +584,7 @@ The Responses API controls what is sent to the agent and knowledge base. To opti
 
 ## Control costs and limit operations
 
-For insights into the query plan, look at output tokens in the [activity array](agentic-retrieval-how-to-retrieve.md#review-the-activity-array) of knowledge base responses.
+For insights into the query plan, look at output tokens in the [activity array](agentic-retrieval-how-to-retrieve.md#activity-array) of knowledge base responses.
 
 ## Improve performance
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure CLIに関する情報の追加"
}
```

### Explanation
この変更は、`agentic-retrieval-how-to-create-pipeline.md`という文書に対するもので、いくつかの情報が追加されました。具体的には、「このチュートリアルでは、以下のことを行います」というリストに、Microsoft Entra IDを用いたキーなしの認証のために必要な「Azure CLI」のリンクが加わりました。

さらに、他のインストール要件に関する記述は特に変更されていませんが、全体の編集によってドキュメントの一貫性が保たれています。特に、PythonやVisual Studio Codeに関連するリンクは元のままとなっており、利用者が必要なツールを簡単に見つけることができるようになっています。

また、「コストを管理し、操作を制限する」セクション内の出力トークンに関するリンクのテキストが微調整され、より明確に指示がなされるようになりました。これにより、知識ベースレスポンスの「activity array」にアクセスする際のガイダンスが強化されています。全体として、ユーザーが作業を円滑に進められるように設計された更新です。

## articles/search/agentic-retrieval-how-to-retrieve.md{#item-d739cf}

<details>
<summary>Diff</summary>
````diff
@@ -1,62 +1,39 @@
 ---
-title: Use a knowledge base to retrieve data
+title: Use Knowledge Base to Retrieve Data
 titleSuffix: Azure AI Search
 description: Set up a retrieval route for agentic retrieval workloads in Azure AI Search.
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 01/15/2026
+ms.date: 02/12/2026
+ai-usage: ai-assisted
 ---
 
-# Retrieve data by using a knowledge base in Azure AI Search
+# Use a knowledge base to retrieve data in Azure AI Search
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-In an agentic retrieval multi-query pipeline, query execution is through the [**retrieve action**](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) on a knowledge base that invokes parallel query processing. This request structure is updated for the new 2025-11-01-preview, which introduces breaking changes from previous previews. For help with breaking changes, see [Migrate your agentic retrieval code](agentic-retrieval-how-to-migrate.md).
+In an agentic retrieval pipeline, the [retrieve action](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) invokes parallel query processing from a knowledge base. This article explains how to call the retrieve action and interpret the three-pronged response.
 
-This article explains how to set up a retrieve action. It also describes the three components of the retrieval response: 
-
-+ *extracted response for the LLM*
-+ *referenced results*
-+ *query activity*
-
-A retrieve request can include instructions for query processing that override the default instructions set on the knowledge base. A retrieve action has core parameters that are supported on any request, plus parameters that are specific to a knowledge source.
-
-You can also use optional [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md) to bring LLM answer formulation into the query pipeline, returning a concise or formatted answer to an agent or app.
+You can call the retrieve action directly using the Search Service REST APIs or an Azure SDK that provides equivalent functionality. Each knowledge base also exposes a Model Context Protocol (MCP) endpoint for consumption by MCP-compatible agents.
 
 ## Prerequisites
 
-+ A [supported knowledge source](agentic-knowledge-source-overview.md#supported-knowledge-sources) that wraps a searchable index or points to an external source for native data retrieval.
-
-+ A [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) that represents one or more knowledge sources. If you want intelligent query planning and answer formulation, include a chat completion model.
-
-+ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md).
-
-+ Permissions on Azure AI Search. Roles for retrieving content include **Search Index Data Reader** for running queries. To support an outbound call from a search service to a chat completion model, you must configure a managed identity for the search service, and it must have **Cognitive Services User** permissions on the Azure OpenAI resource. For more information about local testing and obtaining access tokens, see [Quickstart: Connect without keys](search-get-started-rbac.md).
++ An Azure AI Search service with a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
-+ API version requirements. To create or use a knowledge base, use the [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) data plane REST API. Or, use a preview package of an Azure SDK that provides knowledge base APIs: [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1170-beta3-2025-03-25), [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
++ Permissions to query the knowledge base. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Index Data Reader** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
 
-To follow the steps in this guide, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending REST API calls to Azure AI Search.
++ If the knowledge base specifies an LLM, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource.
 
-## Set up the retrieve action
++ The [2025-11-01-preview](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) REST API or an equivalent Azure SDK preview package: [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
 
-Specify a retrieve action on a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md). The knowledge base has one or more knowledge sources. Retrieval can return a synthesized answer in natural language or raw grounding chunks from the knowledge sources.
-
-+ Review your knowledge base definition to understand which knowledge sources are in scope.
-
-+ Review your knowledge sources to understand their parameters and configuration.
-
-+ Use the [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) data plane REST API or an Azure SDK preview package to call retrieve.
-
-For knowledge sources that have default retrieval instructions, you can override the defaults in the retrieve request.
-
-### Retrieval from a search index
+## Call the retrieve action
 
-For knowledge sources that target a search index, all `searchable` fields are in scope for query execution. If the index includes vector fields, your index should have a valid [vectorizer definition](vector-search-how-to-configure-vectorizer.md) so that the agentic retrieval engine can vectorize the query inputs. Otherwise, vector fields are ignored. The implied query type is `semantic`, and there's no search mode.
+You specify the retrieve action on a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md). The input is chat conversation history in natural language, where the `messages` array contains the conversation. The agentic retrieval engine supports messages only if the [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md) is low or medium.
 
-The input for the retrieval route is chat conversation history in natural language, where the `messages` array contains the conversation. The agentic retrieval engine supports messages only if the [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md) is either low or medium.
+Here's an example using [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) (REST API):
 
 ```http
 @search-url=<YOUR SEARCH SERVICE URL>
@@ -94,120 +71,69 @@ POST https://{{search-url}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-
 }
 ```
 
-### Responses
+### Request parameters
 
-Successful retrieval returns a `200 OK` status code. If the knowledge base fails to retrieve from one or more knowledge sources, a `206 Partial Content` status code returns. The response only includes results from sources that succeeded. Details about the partial response appear as [errors in the activity array](#review-the-activity-array).
-
-### Retrieve parameters
+Pass the following parameters to call the retrieve action.
 
 | Name | Description | Type | Editable | Required |
 |--|--|--|--|--|
-| `messages` | Articulates the messages sent to a chat completion model. The message format is similar to Azure OpenAI APIs. | Object | Yes | No |
-| `role` | Defines where the message came from, for example either `assistant` or `user`. The model you use determines which roles are valid. | String | Yes | No |
-| `content` | The message or prompt sent to the LLM. It must be text in this preview. | String | Yes | No |
-| [`knowledgeSourceParams`](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview#searchindexknowledgesourceparams&preserve-view=true) | Specifies parameters for each knowledge source if you want to customize the query or response at query time. | Object | Yes | No |
+| [`messages`](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true#knowledgebasemessage) | Articulates the messages sent to an LLM. The message format is similar to Azure OpenAI APIs. | Object | Yes | No |
+| `messages.role` | Defines where the message came from, such as `assistant` or `user`. The model you use determines which roles are valid. | String | Yes | No |
+| `messages.content` | The message or prompt sent to the LLM. In this preview, it must be text. | String | Yes | No |
+| [`knowledgeSourceParams`](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true#knowledgebaseretrievalrequest) | Overrides default retrieval settings per knowledge source. Useful for customizing the query or response at query time. | Object | Yes | No |
 
-## Examples
+### Retrieval from a search index
 
-Retrieve requests vary depending on the knowledge sources and whether you want to override a default configuration. Here are several examples that illustrate a range of requests.
+For knowledge sources that target a search index, all `searchable` fields are in scope for query execution. The implied query type is `semantic`, and there's no search mode.
 
-### Example: Override default reasoning effort and set request limits
+If the index includes vector fields, you need a valid [vectorizer definition](vector-search-how-to-configure-vectorizer.md) so the agentic retrieval engine can vectorize query inputs. Otherwise, vector fields are ignored.
 
-This example specifies [answer formulation](agentic-retrieval-how-to-answer-synthesis.md), so `retrievalReasoningEffort` must be "low" or "medium".
+## Call the MCP endpoint
 
-```http
-POST {{url}}/knowledgebases/kb-override/retrieve?api-version={{api-version}}
-api-key: {{key}}
-Content-Type: application/json
+[MCP](https://modelcontextprotocol.io/) is an open protocol that standardizes how AI applications connect to external data sources and tools.
 
-{
-    "messages": [
-        {
-            "role": "user",
-            "content": [
-                { "type": "text", "text": "What companies are in the financial sector?" }
-            ]
-        }
-    ],
-    "retrievalReasoningEffort": { "kind": "low" },
-    "outputMode": "answerSynthesis",
-    "maxRuntimeInSeconds": 30,
-    "maxOutputSize": 6000
-}
+In Azure AI Search, each knowledge base is a standalone MCP server that exposes the `knowledge_base_retrieve` tool. Any MCP-compatible client, including [Foundry Agent Service](/azure/ai-foundry/agents/overview), [GitHub Copilot](https://github.com/features/copilot), [Claude](https://claude.ai), and [Cursor](https://cursor.com), can invoke this tool to query the knowledge base.
+
+### MCP endpoint format
+
+Each knowledge base has an MCP endpoint at the following URL:
+
+```
+https://<your-service-name>.search.windows.net/knowledgebases/<your-knowledge-base-name>/mcp?api-version=2025-11-01-preview
 ```
 
-### Example: Set references for each knowledge source
+### Authenticate to the MCP endpoint
 
-This example uses the default reasoning effort specified in the knowledge base. The focus of this example is specification of how much information to include in the response.
+The MCP endpoint requires authentication via custom headers. You have two options:
 
-```http
-POST {{url}}/knowledgebases/kb-medium-example/retrieve?api-version={{api-version}}
-api-key: {{key}}
-Content-Type: application/json
++ Pass a query key (recommended) or an admin key in the `api-key` header. The key grants read-only access, so no role assignment is needed. For more information, see [Connect to Azure AI Search using API keys](search-security-api-keys.md).
 
-{
-    "messages": [
-        {
-            "role": "user",
-            "content": [
-                { "type": "text", "text": "What companies are in the financial sector?" }
-            ]
-        }
-    ],
-    "includeActivity": true,
-    "knowledgeSourceParams": [
-        {
-            "knowledgeSourceName": "demo-financials-ks",
-            "kind": "searchIndex",
-            "includeReferences": true,
-            "includeReferenceSourceData": true
-        },
-        {
-            "knowledgeSourceName": "demo-communicationservices-ks",
-            "kind": "searchIndex",
-            "includeReferences": false,
-            "includeReferenceSourceData": false
-        },
-        {
-            "knowledgeSourceName": "demo-healthcare=ks",
-            "kind": "searchIndex",
-            "includeReferences": true,
-            "includeReferenceSourceData": false,
-            "alwaysQuerySource": true
-        }
-    ]
-}
-```
++ (Recommended) Pass a bearer token in the `Authorization` header. The identity behind the token must have the **Search Index Data Reader** role assigned on the search service. This approach avoids storing keys in configuration files. For more information, see [Connect your app to Azure AI Search using identities](search-security-rbac-client-code.md).
 
-> [!NOTE]
-> If you're retrieving content from a OneLake or indexed SharePoint knowledge source, set `includeReferenceSourceData` to `true` to include the source document URL in the citation.
+> [!TIP]
+> Each MCP client configures custom headers differently. For example:
+>
+> + In [Foundry Agent Service](/azure/ai-foundry/agents/how-to/foundry-iq-connect), you configure authentication via a project connection and add the MCP tool to an agent. The service automatically injects the required headers on MCP requests.
+>
+> + In [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp), [Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop), and similar clients, you configure headers in the MCP server JSON, such as `mcp.json`.
 
-### Example: minimal reasoning effort
+## Review the response
 
-In this example, there's no chat completion model for intelligent query planning or answer formulation. The query string goes to the agentic retrieval engine for keyword search or hybrid search.
+Successful retrieval returns a `200 OK` status code. If the knowledge base fails to retrieve from one or more knowledge sources, a `206 Partial Content` status code returns. The response only includes results from sources that succeeded. Details about the partial response appear as errors in the activity array.
 
-```http
-POST {{url}}/knowledgebases/kb-minimal/retrieve?api-version={{api-version}}
-api-key: {{key}}
-Content-Type: application/json
+The retrieve action returns three main components:
 
-{
-    "intents": [
-        {
-            "type": "semantic",
-            "search": "what is a brokerage"
-        }
-    ]
-}
-```
++ [Extracted response](#extracted-response) or [synthesized answer](agentic-retrieval-how-to-answer-synthesis.md) (depending on output mode)
++ [Activity array](#activity-array)
++ [References array](#references-array)
 
-## Review the extracted response
+### Extracted response
 
-The *extracted response* is a single unified string that you typically pass to an LLM. The LLM consumes it as grounding data and uses it to formulate a response. Your API call to the LLM includes the unified string and instructions for the model, such as whether to use the grounding exclusively or as a supplement.
+The extracted response is a single unified string that you typically pass to an LLM. The LLM consumes it as grounding data and uses it to formulate a response. Your API call to the LLM includes the unified string and instructions for the model, such as whether to use the grounding exclusively or as a supplement.
 
-The body of the response is also structured in the chat message style format. Currently, in this preview release, the content is serialized JSON.
+The body of the response is also structured in the chat message style format. In this preview, the content is serialized JSON.
 
-```http
+```json
 "response": [
     {
         "role": "assistant",
@@ -221,40 +147,32 @@ The body of the response is also structured in the chat message style format. Cu
 ]
 ```
 
-**Key points**:
+Key points:
 
 + `content.text` is a JSON array. It's a single string composed of the most relevant documents (or chunks) found in the search index, given the query and chat history inputs. This array is your grounding data that a chat completion model uses to formulate a response to the user's question.
 
   This portion of the response consists of 200 chunks or fewer, excluding any results that fail to meet the minimum threshold of a 2.5 reranker score.
 
   The string starts with the reference ID of the chunk (used for citation purposes), and any fields specified in the semantic configuration of the target index. In this example, assume the semantic configuration in the target index has a "title" field, a "terms" field, and a "content" field.
 
-+ `content.type` has one valid value in this preview: `text`. 
++ In this preview, `content.type` has one valid value: `text`.
 
-> [!NOTE]
-> The `maxOutputSize` property on the [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) determines the length of the string.
++ The `maxOutputSize` property on the [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) determines the length of the string.
 
-## Review the activity array
+### Activity array
 
-The activity array outputs the query plan, which helps you track the operations performed when executing the request. It also provides operational transparency so you can understand the billing implications and frequency of resource invocations.
+The activity array outputs the query plan, which provides operational transparency for tracking operations, billing implications, and resource invocations. It also includes subqueries sent to the retrieval pipeline and errors for any retrieval failures, such as inaccessible knowledge sources.
 
-The output includes the following components.
+The output includes the following components:
 
 | Section | Description |
 |---------|-------------|
 | modelQueryPlanning | For knowledge bases that use an LLM for query planning, this section reports on the token counts used for input, and the token count for the subqueries. |
-| source-specific activity | For each knowledge source included in the query, report on elapsed time and which arguments were used in the query, including the semantic ranker. Knowledge source types include `searchIndex`, `azureBlob`, and other [supported knowledge sources](agentic-knowledge-source-overview.md#supported-knowledge-sources). |
-| agenticReasoningEffort | For each retrieve action, you can specify the degree of LLM support. Use minimal to bypass an LLM, low for constrained LLM processing, and medium for full LLM processing. | 
-| modelAnswerSynthesis | For knowledge bases that specify answer formulation, this section reports on the token count for formulating the answer, and the token count of the answer output. |
+| source-specific activity | For each knowledge source included in the query, this section reports on elapsed time and which arguments were used in the query, including semantic ranker. Knowledge source types include `searchIndex`, `azureBlob`, and other [supported knowledge sources](agentic-knowledge-source-overview.md#supported-knowledge-sources). |
+| agenticReasoning | This section reports on token consumption for agentic reasoning during retrieval, which depends on the specified [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). |
+| modelAnswerSynthesis | For knowledge bases that use [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md), this section reports on the token count for formulating the answer, and the token count of the answer output. |
 
-The output reports on the token consumption for agentic reasoning during retrieval at the specified [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md).
-
-The output also includes the following information:
-
-+ Subqueries sent to the retrieval pipeline.
-+ Errors for any retrieval failures, such as inaccessible knowledge sources.
-
-Here's an example of an activity array.
+Here's an example of the activity array:
 
 ```json
   "activity": [
@@ -313,18 +231,17 @@ Here's an example of an activity array.
   ]
 ```
 
+### References array
 
-## Review the references array
-
-The `references` array comes directly from the underlying grounding data. It includes the `sourceData` used to generate the response. It consists of every document that the agentic retrieval engine finds and semantically ranks. Fields in the `sourceData` include an `id` and semantic fields: `title`, `terms`, and `content`.
+The references array comes directly from the underlying grounding data. It includes the `sourceData` used to generate the response. It consists of every document that the agentic retrieval engine finds and semantically ranks. Fields in the `sourceData` include an `id` and semantic fields: `title`, `terms`, and `content`.
 
 The `id` acts as a reference ID for an item within a specific response. It's not the document key in the search index. You use it for providing citations.
 
 The purpose of this array is to provide a chat message style structure for easy integration. For example, if you want to serialize the results into a different structure or you require some programmatic manipulation of the data before you returned it to the user.
 
 You can also get the structured data from the source data object in the references array to manipulate it however you see fit.
 
-Here's an example of the references array.
+Here's an example of the references array:
 
 ```json
   "references": [
@@ -345,8 +262,104 @@ Here's an example of the references array.
   ]
 ```
 
+## Examples
+
+The following examples illustrate different ways to call the retrieve action:
+
++ [Override default reasoning effort and set request limits](#override-default-reasoning-effort-and-set-request-limits)
++ [Set references for each knowledge source](#set-references-for-each-knowledge-source)
++ [Use minimal reasoning effort](#use-minimal-reasoning-effort)
+
+### Override default reasoning effort and set request limits
+
+This example specifies [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md), so `retrievalReasoningEffort` must be "low" or "medium".
+
+```http
+POST {{url}}/knowledgebases/kb-override/retrieve?api-version={{api-version}}
+api-key: {{key}}
+Content-Type: application/json
+
+{
+    "messages": [
+        {
+            "role": "user",
+            "content": [
+                { "type": "text", "text": "What companies are in the financial sector?" }
+            ]
+        }
+    ],
+    "retrievalReasoningEffort": { "kind": "low" },
+    "outputMode": "answerSynthesis",
+    "maxRuntimeInSeconds": 30,
+    "maxOutputSize": 6000
+}
+```
+
+### Set references for each knowledge source
+
+This example uses the default reasoning effort specified in the knowledge base. The focus of this example is specification of how much information to include in the response.
+
+```http
+POST {{url}}/knowledgebases/kb-medium-example/retrieve?api-version={{api-version}}
+api-key: {{key}}
+Content-Type: application/json
+
+{
+    "messages": [
+        {
+            "role": "user",
+            "content": [
+                { "type": "text", "text": "What companies are in the financial sector?" }
+            ]
+        }
+    ],
+    "includeActivity": true,
+    "knowledgeSourceParams": [
+        {
+            "knowledgeSourceName": "demo-financials-ks",
+            "kind": "searchIndex",
+            "includeReferences": true,
+            "includeReferenceSourceData": true
+        },
+        {
+            "knowledgeSourceName": "demo-communicationservices-ks",
+            "kind": "searchIndex",
+            "includeReferences": false,
+            "includeReferenceSourceData": false
+        },
+        {
+            "knowledgeSourceName": "demo-healthcare-ks",
+            "kind": "searchIndex",
+            "includeReferences": true,
+            "includeReferenceSourceData": false,
+            "alwaysQuerySource": true
+        }
+    ]
+}
+```
+
+
 > [!NOTE]
-> If you're retrieving content from a OneLake or indexed SharePoint knowledge source, set `includeReferenceSourceData` to `true` on the retrieve request to get the source document URL in the citation.
+> For indexed OneLake or indexed SharePoint knowledge sources, set `includeReferenceSourceData` to `true` to include source document URLs in citations.
+
+### Use minimal reasoning effort
+
+In this example, there's no LLM for intelligent query planning or answer synthesis. The query string goes to the agentic retrieval engine for keyword search or hybrid search.
+
+```http
+POST {{url}}/knowledgebases/kb-minimal/retrieve?api-version={{api-version}}
+api-key: {{key}}
+Content-Type: application/json
+
+{
+    "intents": [
+        {
+            "type": "semantic",
+            "search": "what is a brokerage"
+        }
+    ]
+}
+```
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エージェントリトリーバルパイプラインの更新と明確化"
}
```

### Explanation
この変更は、`agentic-retrieval-how-to-retrieve.md`という文書に対して行われ、エージェントリトリーバルのプロセスやAPI呼び出しに関する重要なアップデートが含まれています。主な内容は、リトリーブアクションの新しい呼び出し仕様や、応答構造に関する詳細が明確化されたことです。

まず、記事のタイトルと概要が更新され、「Retrieve data by using a knowledge base in Azure AI Search」から「Use Knowledge Base to Retrieve Data in Azure AI Search」に変更され、より直感的な理解が促進されています。また、文書の日付が更新され、AIによる使用のガイドラインも追加されています。

リトリーブアクションの設定に関する説明が強化され、複数の知識ソースからのデータ要求や、それに伴うレスポンスの処理についての具体的な手順が記載されています。特に、「retrieve action」の記述が簡潔化され、リクエスト構造と応答の3つの主要なコンポーネント—抽出された応答、アクティビティ配列、参照配列—が明示されています。

これに伴い、従来の手法から移行するための情報が、特に新しいAPIの利用とその関連パラメータについて詳しく説明され、利用者が新たな要件に適応しやすいよう配慮されています。全体として、文書の可読性と操作性の向上を目指した大規模な改訂が実施されました。

## articles/search/agentic-retrieval-how-to-set-retrieval-reasoning-effort.md{#item-141e97}

<details>
<summary>Diff</summary>
````diff
@@ -27,13 +27,14 @@ Levels of reasoning effort include:
 
 ## Prerequisites
 
-+ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md).
++ An Azure AI Search service with a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
-+ Familiarity with [agentic retrieval concepts and workflow](agentic-retrieval-overview.md).
++ Permissions to update the knowledge base. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
 
-+ A knowledge base that uses the [2025-11-01-preview syntax](agentic-retrieval-how-to-migrate.md).
++ If the knowledge base specifies an LLM, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource.
+
++ The [2025-11-01-preview](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) REST API or an equivalent Azure SDK preview package: [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
 
-+ [Visual Studio Code](https://code.visualstudio.com/) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) or a preview Azure SDK package that provides the knowledge base REST APIs.
 
 ## Choose a reasoning effort
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リトリーバル推論努力の設定に関する要件の明確化"
}
```

### Explanation
この変更は、`agentic-retrieval-how-to-set-retrieval-reasoning-effort.md`という文書に対し、リトリーバル推論努力の設定に関する要件を明確化するための情報が追加されました。

具体的には、前提条件セクションが更新され、以下のポイントが強調されています：
- Azure AI Searchサービスを持っていることに加え、知識ベースが必要であることが明示されました。
- 知識ベースを更新するための適切な権限を持つ必要があることが強調され、「Search Service Contributor」ロールまたはAPIキーを用いたキーなしの認証設定が推奨されるようになりました。
- 知識ベースに LLM (大規模言語モデル) が指定されている場合、検索サービスには Microsoft Foundry リソースに対する「Cognitive Services User」権限を持つマネージドアイデンティティが必要です。
- また、利用可能なAPIバージョンに関する詳細として、2025-11-01-previewに関するREST APIや各SDKパッケージのリンクも加えられました。

これらの変更は、ユーザーが推論努力を設定するために必要な準備が整うように、より具体的で明確な指針を提供することを目的としています。全体として、文書の利用可能性と効果的な設定手順の理解を向上させるための更新です。

## articles/search/get-started-portal-agentic-retrieval.md{#item-2bf1dc}

<details>
<summary>Diff</summary>
````diff
@@ -257,7 +257,7 @@ To query the knowledge base:
     ]
     ```
 
-   The activity log offers insight into the steps taken during retrieval, including query planning and execution, semantic ranking, and answer synthesis. For more information, see [Review the activity array](agentic-retrieval-how-to-retrieve.md#review-the-activity-array).
+   The activity log offers insight into the steps taken during retrieval, including query planning and execution, semantic ranking, and answer synthesis. For more information, see [Review the activity array](agentic-retrieval-how-to-retrieve.md#activity-array).
 
 ## Review the created objects
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アクティビティログの参照リンクの修正"
}
```

### Explanation
この変更は、`get-started-portal-agentic-retrieval.md`という文書に対して行われたもので、アクティビティログに関する参照リンクが修正されています。

具体的には、アクティビティログに関連するセクションでのリンクテキストが「[Review the activity array]」から「[Review the activity array](agentic-retrieval-how-to-retrieve.md#activity-array)」に変更されました。これにより、リンクが正確にアクティビティ配列の部分にリダイレクトされるようになり、ユーザーがリトリーバルプロセスの詳細をより簡単にアクセスし理解することができるようになります。

この修正は、文書の整合性を向上させ、利用者に対して必要な情報を迅速に提供するための重要な更新です。全体として、ユーザーエクスペリエンスを向上させることを目的とした軽微な修正が行われました。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -44,7 +44,7 @@ You can create an Azure AI Search service in any of the following Azure public r
 | Brazil South​​ <sup>1</sup> ​| ✅ |  | ✅ | ✅ | ✅ | ✅ |
 | Canada Central​​ <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Canada East​​ ​<sup>1</sup> |  |  | ✅ |  | ✅ |  |
-| ​Central US​​ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| ​Central US​​ <sup> 2</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | East US​ <sup>1, 2</sup> | ✅ | ✅ | ✅ |  | ✅ |  |
 | East US 2 <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Mexico Central |  | ✅ |  |  |  |  |
@@ -57,7 +57,7 @@ You can create an Azure AI Search service in any of the following Azure public r
 
 <sup>1</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
 
-<sup>2</sup> This region is experiencing capacity constraints that prevent the creation of new search services for Basic and S1 tiers. Please choose a different region.
+<sup>2</sup> This region is experiencing capacity constraints that prevent the creation of new search services. Please choose a different region.
 
 <sup>3</sup> This region doesn't have indexer support for [Microsoft Purview sensitivity labels](search-indexer-sensitivity-labels.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Central US地域の制限に関する説明の修正"
}
```

### Explanation
この変更は、`search-region-support.md`という文書に対して行われたもので、Central US地域に関する制限についての説明が修正されています。

具体的には、以下の2つの行での表現が変更されました：
1. "Central US"の地域名の後に、脚注のフォーマットが一部整理されました。
2. この地域における新しい検索サービスの作成に関する説明が更新され、元は「BasicおよびS1ティアの新しい検索サービスの作成を妨げる容量制約がある」と記述されていた部分が、「新しい検索サービスの作成を妨げる容量制約がある」と簡素化されました。

この修正は、情報をより簡潔にし、ユーザーがregion選定に関して適切な判断を下せるよう、文書の内容を明確にすることを目的としています。全体として、この変更は将来の利用者に対する役立つ情報の提供を強化するための軽微な更新です。


