---
date: '2025-06-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ca0291a...MicrosoftDocs:178e7a4
summary: このコード変更では、Azure AI Searchにおけるナレッジエージェントとエージェント型情報取得に関連するドキュメントが更新され、新機能や破壊的変更が追加されました。主な新機能には、ナレッジエージェントのモデルに関する更新、取得パイプラインの詳細説明及び新しいAPI要件の具体例が含まれます。破壊的変更には、チャット完了モデルへの表現変更やリクエスト内の`role`変更が挙げられます。これらの変更を通じて、ユーザーエクスペリエンスが向上し、エージェント型情報取得の機能と使いやすさが強化されました。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ca0291a...MicrosoftDocs:178e7a4){target="_blank"}

<format>
# ハイライト
このコード変更では、Azure AI Searchにおけるナレッジエージェントとエージェント型情報取得に関連するドキュメントが更新されました。特に、新しい機能や破壊的変更を含み、ユーザーエクスペリエンスの向上を目指しています。

## 新機能
- ナレッジエージェントの機能や使用するモデルに関する更新。
- 取得パイプラインの詳細説明と関連リソースのリンク追加。
- 新しいAPI要件の詳細追加と具体的操作例の提供。

## 破壊的変更
- チャット完了モデルへの言及の変更。
- リクエストおよびレスポンス内の`role`の変更（「system」から「assistant」へ）。
- 取得リクエストに関する指示がオーバーライド可能に。

## その他の更新
- エージェント型情報取得に関する関連コンテンツの追加。
- 文書日付の更新（最終更新日: 2025年5月30日）。

# インサイト
Azure AI Searchのエージェント型情報取得機能の更新には、ユーザビリティの改善と機能の拡張が含まれています。これらの変更は、特にエージェントがどのように情報を扱うかについて、より明確な記述と制御を提供します。

まず、ナレッジエージェントに使用されるモデルに関する表現が更新され、従来の「会話型言語モデル」から「チャット完了モデル」に変更されました。これにより、エージェントの情報取得パイプラインの理解が深まり、ユーザーが適切なモデルを選択する際の指針として役立ちます。

また、関連するリソースへのリンクが新たに追加され、ユーザーはエージェント型情報取得に関する実用的な知識をより容易に深めることが可能となっています。このようなリソースの追加は、エコシステム全体としての情報へのアクセス性を改善し、ユーザーの理解を助ける重要な要素となっています。

さらに、特筆すべきはAPIを通じたリクエストおよびレスポンスの形式変更です。特に、`role`の変更は、システム内の役割を明確に分けるための措置であり、開発者が異なるシナリオでエージェントを効果的に活用するのを助けることになります。

これらの更新を通じて、Azure AI Searchはより強力で使いやすいプラットフォームへの進化を遂げており、開発者およびエンドユーザー双方にとっての有用性を高めることに寄与しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-agentic-retrieval-how-to-create.md](#item-310fbe) | minor update | Azure AI Searchにおけるナレッジエージェントの更新 | modified | 37 | 22 | 59 | 
| [search-agentic-retrieval-how-to-index.md](#item-a078ea) | minor update | Azure AI Searchのエージェント型情報取得に関する関連コンテンツの追加 | modified | 2 | 0 | 2 | 
| [search-agentic-retrieval-how-to-pipeline.md](#item-1ad1c3) | minor update | Azure AI Searchのエージェント型情報取得パイプラインに関する関連リソースの追加 | modified | 2 | 0 | 2 | 
| [search-agentic-retrieval-how-to-retrieve.md](#item-5f7fc0) | breaking change | Azure AI Searchにおけるエージェント型情報取得の変更と強化 | modified | 76 | 57 | 133 | 


# Modified Contents
## articles/search/search-agentic-retrieval-how-to-create.md{#item-310fbe}

<details>
<summary>Diff</summary>
````diff
@@ -8,32 +8,38 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/05/2025
+ms.date: 05/30/2025
 ---
 
 # Create a knowledge agent in Azure AI Search
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-In Azure AI Search, a *knowledge agent* is a top-level resource representing a connection to a conversational language model for use in agentic retrieval workloads. It specifies a model that provides reasoning capabilities, and it identifies the search index used at query time.
+In Azure AI Search, a *knowledge agent* is a top-level resource representing a connection to a chat completion model for use in agentic retrieval workloads. A knowledge agent is used by the [retrieve method](search-agentic-retrieval-how-to-retrieve.md) in an LLM-powered information retrieval pipeline.
+
+A knowledge agent specifies:
+
++ A model that provides reasoning capabilities
++ A target search index used at query time
++ Parameters on the index for setting default behaviors and response shaping
 
 After you can create a knowledge agent, you can update its properties at any time. If the knowledge agent is in use, updates take effect on the next job.
 
 ## Prerequisites
 
 + Familiarity with [agentic retrieval concepts and use cases](search-agentic-retrieval-concept.md).
 
-+ A conversational language model on Azure OpenAI, either gpt-4o or gpt-4o-mini.
++ A [supported chat completion model](#supported-models) on Azure OpenAI.
 
-+ Azure AI Search, in any [region that provides semantic ranker](search-region-support.md), on basic tier and above. Your search service must have a [managed identity](search-howto-managed-identities-data-sources.md) for role-based access to a chat model.
++ Azure AI Search, in any [region that provides semantic ranker](search-region-support.md), on the basic pricing tier or higher. Your search service must have a [managed identity](search-howto-managed-identities-data-sources.md) for role-based access to the model.
 
-+ Permission requirements on Azure AI Search. An **Owner/Contributor** or **Search Service Contributor** can create and manage a knowledge agent. **Search Index Data Contributor** uploads and indexes document. **Search Index Data Reader** runs queries. Instructions are provided in this article.
++ Permissions on Azure AI Search. **Search Service Contributor** can create and manage a knowledge agent. **Search Index Data Reader** can run queries. Instructions are provided in this article.
 
-+ A search index containing plain text or vectors. The index must [meet requirements for agentic retrieval](search-agentic-retrieval-how-to-index.md), including a [semantic configuration](semantic-how-to-configure.md) with the `defaultConfiguration` specified.
++ A search index containing plain text or vectors. The index must [meet the requirements for agentic retrieval](search-agentic-retrieval-how-to-index.md), including a [semantic configuration](semantic-how-to-configure.md) with the `defaultConfiguration` specified.
 
-+ API requirements. To create or use a knowledge agent, use 2025-05-01-preview data plane REST API or a prerelease package of an Azure SDK that provides knowledge agent APIs.
++ API requirements. To create or use a knowledge agent, use [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API. Or, use a prerelease package of an Azure SDK that provides knowledge agent APIs: [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1170-beta3-2025-03-25), [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
 
-To follow the steps in this guide, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending REST API calls to Azure AI Search. There's no portal support at this time.
+To follow the steps in this guide, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending preview REST API calls to Azure AI Search. There's no portal support at this time.
 
 ## Deploy a model for agentic retrieval
 
@@ -43,7 +49,9 @@ Make sure you have a supported model that Azure AI Search can access. The follow
 
 1. Deploy a supported model using [these instructions](/azure/ai-foundry/how-to/deploy-models-openai).
 
-1. Verify the search service managed identity has **Cognitive Services User** permissions on the Azure OpenAI resource. If you're testing locally, you also need **Cognitive Services User** permissions.
+1. Verify the search service managed identity has **Cognitive Services User** permissions on the Azure OpenAI resource. 
+
+   If you're testing locally, you also need **Cognitive Services User** permissions.
 
 ### Supported models
 
@@ -97,34 +105,37 @@ You can use API keys if you don't have permission to create role assignments.
 
    # List Indexes
    GET https://{{search-url}}/indexes?api-version=2025-05-01-preview
-   api-key: {{search-api-key}}
+      Content-Type: application/json
+      @api-key: {{search-api-ke}}
    ```
 
 ## Check for existing knowledge agents
 
-The following request lists knowledge agents by name. Within the knowledge agents collection, all knowledge agents must be uniquely named. It's helpful for knowing about existing knowledge agents for reuse or  naming purposes.
+The following request lists knowledge agents by name on your search service. Within the knowledge agents collection, all knowledge agents are uniquely named. It's helpful for knowing about existing knowledge agents for reuse or naming purposes.
 
 <!-- ### [**REST APIs**](#tab/rest-get) -->
 
 ```http
 # List knowledge agents
 GET https://{{search-url}}/agents?api-version=2025-05-01-preview
-api-key: {{search-api-key}}
+   Content-Type: application/json
+   Authorization: Bearer {{accessToken}}
 ```
 
-You can also return a single agent by name.
+You can also return a single agent by name to review its JSON definition.
 
 ```http
 # Get knowledge agent
 GET https://{{search-url}}/agents/{{agent-name}}?api-version=2025-05-01-preview
-api-key: {{search-api-key}}
+   Content-Type: application/json
+   Authorization: Bearer {{accessToken}}
 ```
 
 <!-- --- -->
 
 ## Create a knowledge agent
 
-A knowledge agent represents a connection to a model that you've deployed. Parameters on the model establish the connection.
+A knowledge agent represents a connection between a model that you've deployed in Azure OpenAI and a target index on Azure AI Search. Parameters on the model establish the connection. Parameters on the index establish defaults that inform query execution and the response.
 
 <!-- ### [**REST APIs**](#tab/rest-create) -->
 
@@ -136,12 +147,12 @@ To create an agent, use the 2025-05-01-preview data plane REST API or an Azure S
 @agent-name=<YOUR AGENT NAME>
 @index-name=<YOUR INDEX NAME>
 @model-provider-url=<YOUR AZURE OPENAI RESOURCE URI>
-@model-api-key=<YOUR AZURE OPENAI API KEY>
+@accessToken = <a long GUID>
 
 # Create knowledge agent
 PUT https://{{search-url}}/agents/{{agent-name}}?api-version=2025-05-01-preview
-api-key: {{search-api-key}}
-Content-Type: application/json
+   Content-Type: application/json
+   Authorization: Bearer {{accessToken}}
 
 {
     "name" : "{{agent-name}}",
@@ -174,7 +185,7 @@ Content-Type: application/json
 
 **Key points**:
 
-+ `name` must be unique within the knowledge agents collection it must adhere to [naming rules](/rest/api/searchservice/naming-rules) for objects on Azure AI Search.
++ `name` must be unique within the knowledge agents collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects on Azure AI Search.
 
 + `targetIndexes` is required for knowledge agent creation. It lists the search indexes that can use the knowledge agent. Currently in this preview release, the `targetIndexes` array can contain only one index. *It must have a default semantic configuration* (`defaultConfiguration`). For more information, see [Design an index for agentic retrieval](search-agentic-retrieval-how-to-index.md).
 
@@ -213,8 +224,8 @@ Replace "What are my vision benefits?" with a query string that's valid for your
 ```http
 # Send Grounding Request
 POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-05-01-preview
-api-key: {{search-api-key}}
-Content-Type: application/json
+   Content-Type: application/json
+   Authorization: Bearer {{accessToken}}
 
 {
     "messages" : [
@@ -247,14 +258,18 @@ For more information about the **retrieve** API and the shape of the response, s
 
 ## Delete an agent
 
+If you no longer need the agent, or if you need to rebuild it on the search service, use this request to delete the current object.
+
 ```http
 # Delete Agent
 DELETE https://{{search-url}}/agents/{{agent-name}}?api-version=2025-05-01-preview
-api-key: {{search-api-key}}
+   Authorization: Bearer {{accessToken}}
 ```
 
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
 
++ [Agentic RAG: build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
+
 + [Azure OpenAI Demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおけるナレッジエージェントの更新"
}
```

### Explanation
この変更は、Azure AI Searchに関連するナレッジエージェントに関するドキュメントの更新です。主な内容は、ナレッジエージェントの機能や使用するモデルに関する記述を明確にすることにあります。

具体的には、次の点が修正されました：
- 「会話型言語モデル」から「チャット完了モデル」へのモデルの表現が変更され、エージェントによる情報取得パイプラインにおける役割が明示されています。
- ナレッジエージェントが指定する要素（推論能力を提供するモデル、クエリ時に使用される検索インデックス、デフォルトの動作設定を条件付けるパラメータ）について説明が追加されています。
- 必要な権限や前提条件に関するセクションが更新され、権限の詳細についても簡潔に整理されていることが確認できます。
- API要求の形式の変更により、Bearerトークンを用いた認証方法が強調されています。

これにより、ユーザーはナレッジエージェントの作成と管理に関する最新の情報を得ることができ、Azure OpenAIや関連サービスとの接続方法についても理解を深めることができます。また、文書内での情報の一貫性が向上されています。

## articles/search/search-agentic-retrieval-how-to-index.md{#item-a078ea}

<details>
<summary>Diff</summary>
````diff
@@ -323,4 +323,6 @@ Synonym maps are defined as a top-level resource on a search index and assigned
 
 + [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
 
++ [Agentic RAG: build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
+
 + [Azure OpenAI Demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのエージェント型情報取得に関する関連コンテンツの追加"
}
```

### Explanation
この変更は、Azure AI Searchにおけるエージェント型情報取得に関するインデックス作成に関するドキュメントの更新です。具体的には、次の通りです。

- 文書の末尾に、Azure AI Searchにおけるエージェント型情報取得に関連するリソースのリンクが追加されました。
- 新たに追加されたリンクには、エージェント型情報取得の概念を詳しく説明したページおよび、Azure AI Searchを利用した推論型情報取得エンジンの構築に関するYouTube動画が含まれています。

この更新により、ユーザーはエージェント型情報取得に関するさらに詳しいリソースへのアクセスが可能となり、実用的な知識を深めるためのサポートが強化されます。

## articles/search/search-agentic-retrieval-how-to-pipeline.md{#item-1ad1c3}

<details>
<summary>Diff</summary>
````diff
@@ -263,4 +263,6 @@ Look at output tokens in the [activity array](search-agentic-retrieval-how-to-re
 
 + [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
 
++ [Agentic RAG: build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
+
 + [Azure OpenAI Demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのエージェント型情報取得パイプラインに関する関連リソースの追加"
}
```

### Explanation
この変更は、Azure AI Searchにおけるエージェント型情報取得パイプラインに関するドキュメントの更新です。具体的には、以下の点が修正されました。

- 文書の後半に、関連するリソースへのリンクが新たに追加されました。
- 新しく追加されたリンクには、エージェント型情報取得に関する概念を詳しく解説したページと、Azure AI Searchを用いた推論型情報取得エンジンの構築に関するYouTube動画が含まれています。

この更新により、読者はエージェント型情報取得に関連する多様なリソースにアクセスしやすくなり、実装や理解を深める助けとなる情報を得ることができます。これにより、Azure AI Searchの利用における理解が一層深まります。

## articles/search/search-agentic-retrieval-how-to-retrieve.md{#item-5f7fc0}

<details>
<summary>Diff</summary>
````diff
@@ -8,68 +8,79 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/05/2025
+ms.date: 05/30/2025
 ---
 
 # Retrieve data using a knowledge agent in Azure AI Search
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-In Azure AI Search, *agentic retrieval* is a new parallel query architecture that uses a conversational large language model (LLM) for query planning, generating subqueries that broaden the scope of what's searchable and relevant.
+In Azure AI Search, *agentic retrieval* is a new parallel query architecture that uses a chat completion model for query planning. It generates subqueries that broaden the scope of what's searchable and relevant.
 
-This article explains how to use the [**retrieve** method](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-05-01-preview&preserve-view=true) that invokes a knowledge agent and parallel query processing. This article also explains the three components of the retrieval response: 
+This article explains how to use the [**retrieve method**](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-05-01-preview&preserve-view=true) that invokes a knowledge agent and parallel query processing. This article also explains the three components of the retrieval response: 
 
 + *extracted response for the LLM*
 + *referenced results*
 + *query activity*
 
+The retrieve request can include instructions for query processing that override the defaults set on the knowledge agent.
+
 > [!NOTE]
-> Currently, there's no model-generated "answer" in the response. Instead, the response provides grounding data that you can use to generate an answer from an LLM. For an end-to-end example, see [Build an agent-to-agent retrieval solution ](search-agentic-retrieval-how-to-pipeline.md) or [Azure OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo).
+> There's no model-generated "answer" in the response. Instead, the response passes content to an LLM that grounds its answer based on the content. For an end-to-end example that includes this step, see [Build an agent-to-agent retrieval solution ](search-agentic-retrieval-how-to-pipeline.md) or [Azure OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo).
 
 ## Prerequisites
 
-+ A [knowledge agent definition](search-agentic-retrieval-how-to-create.md) that represents a conversational language model.
++ A [knowledge agent](search-agentic-retrieval-how-to-create.md) that represents the chat completion model and a valid target index.
+
++ Azure AI Search, in any [region that provides semantic ranker](search-region-support.md), on basic tier and higher. Your search service must have a [managed identity](search-howto-managed-identities-data-sources.md) for role-based access to a chat completion model.
 
-+ Azure AI Search, in any [region that provides semantic ranker](search-region-support.md), on basic tier and above. Your search service must have a [managed identity](search-howto-managed-identities-data-sources.md) for role-based access to a chat model.
++ Permissions on Azure AI Search. **Search Index Data Reader** can run queries on Azure AI Search, but the search service managed identity must have **Cognitive Services User** permissions on the Azure OpenAI resource. For more information about local testing and obtaining access tokens, see [Quickstart: Connect without keys](search-get-started-rbac.md).
 
-+ API requirements. Use 2025-05-01-preview data plane REST API or a prerelease package of an Azure SDK that provides knowledge agent APIs.
++ API requirements. To create or use a knowledge agent, use [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API. Or, use a prerelease package of an Azure SDK that provides knowledge agent APIs: [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1170-beta3-2025-03-25), [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
 
 To follow the steps in this guide, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending REST API calls to Azure AI Search. There's no portal support at this time.
 
 ## Call the retrieve action
 
 Call the **retrieve** action on the knowledge agent object to invoke retrieval and return a response. Use the [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API or an Azure SDK prerelease package that provides equivalent functionality for this task.
 
+All `searchable` fields in the search index are in-scope for query execution. If the index includes vector fields, your index should have a valid vectorizer definition so that it can vectorize the query inputs. Otherwise, vector fields are ignored. The implied query type is `semantic`, and there's no search mode or selection of search fields.
+
 The input for the retrieval route is chat conversation history in natural language, where the `messages` array contains the conversation.
 
 ```http
+@search-url=<YOUR SEARCH SERVICE URL>
+@accessToken=<YOUR PERSONAL ID>
+
 # Send Grounding Request
 POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-05-01-preview
-api-key: {{search-api-key}}
-Content-Type: application/json
+    Content-Type: application/json
+    Authorization: Bearer {{accessToken}}
 
 {
     "messages" : [
             {
-                "role" : "system",
+                "role" : "assistant",
                 "content" : [
-                  { "type" : "text", "text" : "You are a helpful assistant for Contoso Human Resources. You have access to a search index containing guidelines about health care coverage for Washington state. If you can't find the answer in the search, say you don't know." }
+                  { "type" : "text", "text" : "You can answer questions about the Earth at night.
+                    Sources have a JSON format with a ref_id that must be cited in the answer.
+                    If you do not have the answer, respond with "I don't know"." }
                 ]
             },
             {
                 "role" : "user",
                 "content" : [
-                  { "type" : "text", "text" : "What are my vision benefits?" }
+                  { "type" : "text", "text" : "Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?" }
                 ]
             }
         ],
     "targetIndexParams" :  [
         { 
             "indexName" : "{{index-name}}",
-            "filterAddOn" : "State eq 'WA'",
+            "filterAddOn" : "page_number eq 105'",
             "IncludeReferenceSourceData": true, 
-            "rerankerThreshold " : 2.5,
-            "maxDocsForReranker": 250
+            "rerankerThreshold" : 2.5,
+            "maxDocsForReranker": 50
         } 
     ]
 }
@@ -79,21 +90,23 @@ Content-Type: application/json
 
 + `messages` articulates the messages sent to the model. The message format is similar to Azure OpenAI APIs.
 
-  + `role` defines where the message came from, for example either `system` or `user`. The model you use determines which roles are valid.
+  + `role` defines where the message came from, for example either `assistant` or `user`. The model you use determines which roles are valid.
 
   + `content` is the message sent to the LLM. It must be text in this preview.
 
 + `targetIndexParams` provide instructions on the retrieval. Currently in this preview, you can only target a single index. 
 
   + `filterAddOn` lets you set an [OData filter expression](search-filters.md) for keyword or hybrid search.
 
-  + `IncludeReferenceSourceData` is initially set in the knowledge agent definition. You can override that setting in the retrieve action to return grounding data in the [references section](#review-the-references-array) of the response.
+  + `IncludeReferenceSourceData` tells the retrieval engine to return the source content in the response. This value is initially set in the knowledge agent definition. You can override that setting in the retrieve action to return original source content in the [references section](#review-the-references-array) of the response.
 
   + `rerankerThreshold` and `maxDocsForReranker` are also initially set in the knowledge agent definition as defaults. You can override them in the retrieve action to configure [semantic reranker](semantic-how-to-configure.md), setting minimum thresholds and the maximum number of inputs sent to the reranker.
 
     `rerankerThreshold` is the minimum semantic reranker score that's acceptable for inclusion in a response. [Reranker scores](semantic-search-overview.md#how-ranking-is-scored) range from 1 to 4. Plan on revising this value based on testing and what works for your content.
 
-    `maxDocsForReranker` dictates the maximum number of documents to consider for the final response string. Semantic reranker accepts 50 documents. If the maximum is 200, four more subqueries are added to the query plan to ensure all 200 documents are semantically ranked. for semantic ranking. If the number isn't evenly divisible by 50, the query plan rounds up to nearest whole number.
+    `maxDocsForReranker` dictates the maximum number of documents to consider for the final response string. Semantic reranker accepts 50 documents. If the maximum is 200, four more subqueries are added to the query plan to ensure all 200 documents are semantically ranked. for semantic ranking. If the number isn't evenly divisible by 50, the query plan rounds up to nearest whole number. 
+
+    The `content` portion of the response consists of the 200 chunks or less, excluding any results that fail to meet the minimum threshold of a 2.5 reranker score.
 
 ## Review the extracted response
 
@@ -104,22 +117,25 @@ The body of the response is also structured in the chat message style format. Cu
 ```http
 "response": [
     {
-        "role": "system",
+        "role": "assistant",
         "content": [
             {
                 "type": "text",
-                "text": "[{\"ref_id\":0,\"title\":\"Vision benefits\",\"terms\":\"exams, frames, contacts\",\"content\":\"<content chunk>\"}]"
+                "text": "[{\"ref_id\":0,\"title\":\"Urban Structure\",\"terms\":\"Location of Phoenix, Grid of City Blocks, Phoenix Metropolitan Area at Night\",\"content\":\"<content chunk redacted>\"}]"
             }
         ]
     }
 ]
 ```
 
-`content` is a JSON array. It's a single string composed of the most relevant documents (or chunks) found in the search index, given the query and chat history inputs. This array is your grounding data that a conversational language model uses to formulate a response to the user's question.
+**Key points**:
 
-The `maxOutputSize` property on the knowledge agent determines the length of the string. We recommend 5,000 tokens.
++ `content` is a JSON array. It's a single string composed of the most relevant documents (or chunks) found in the search index, given the query and chat history inputs. This array is your grounding data that a conversational language model uses to formulate a response to the user's question.
 
-Fields in the content `text` response string include the ref_id and semantic configuration fields: `title`, `terms`, `terms`.
++ text is the only valid value for type, and the text consists of the reference ID of the chunk (used for citation purposes), and any fields specified in the semantic configuration of the target index. In this example, you should assume the semantic configuration in the target index has a "title" field, a "terms" field, and a "content" filed. 
+
+> [!NOTE]
+> The `maxOutputSize` property on the [knowledge agent](search-agentic-retrieval-how-to-create.md) determines the length of the string. We recommend 5,000 tokens.
 
 ## Review the activity array
 
@@ -137,36 +153,53 @@ Output includes:
 Here's an example of an activity array.
 
 ```json
-  "activity": [
+"activity": [
     {
       "type": "ModelQueryPlanning",
       "id": 0,
-      "inputTokens": 1308,
-      "outputTokens": 141
+      "inputTokens": 1261,
+      "outputTokens": 270
     },
     {
       "type": "AzureSearchQuery",
       "id": 1,
-      "targetIndex": "myindex",
+      "targetIndex": "earth_at_night",
       "query": {
-        "search": "hello world programming",
+        "search": "suburban belts December brightening urban cores comparison",
         "filter": null
       },
-      "queryTime": "2025-04-25T16:40:08.811Z",
-      "count": 2,
-      "elapsedMs": 867
+      "queryTime": "2025-05-30T21:23:25.944Z",
+      "count": 0,
+      "elapsedMs": 600
     },
     {
       "type": "AzureSearchQuery",
       "id": 2,
-      "targetIndex": "myindex",
+      "targetIndex": "earth_at_night",
       "query": {
-        "search": "hello world meaning",
+        "search": "Phoenix nighttime street grid visibility from space",
         "filter": null
       },
-      "queryTime": "2025-04-25T16:40:08.955Z",
+      "queryTime": "2025-05-30T21:23:26.128Z",
       "count": 2,
-      "elapsedMs": 136
+      "elapsedMs": 161
+    },
+    {
+      "type": "AzureSearchQuery",
+      "id": 3,
+      "targetIndex": "earth_at_night",
+      "query": {
+        "search": "interstate visibility from space midwestern cities",
+        "filter": null
+      },
+      "queryTime": "2025-05-30T21:23:26.277Z",
+      "count": 0,
+      "elapsedMs": 147
+    },
+    {
+      "type": "AzureSearchSemanticRanker",
+      "id": 4,
+      "inputTokens": 2622
     }
   ],
 ```
@@ -175,6 +208,8 @@ Here's an example of an activity array.
 
 The `references` array is a direct reference from the underlying grounding data and includes the `sourceData` used to generate the response. It consists of every single document that was found and semantically ranked by the search engine. Fields in the `sourceData` include an `id` and semantic fields: `title`, `terms`, `content`.
 
+The `id` is a reference ID for an item within a specific response. It's not the document key in the search index. It's used for providing citations.
+
 The purpose of this array is to provide a chat message style structure for easy integration. For example, if you want to serialize the results into a different structure or you require some programmatic manipulation of the data before you returned it to the user.
 
 You can also get the structured data from the source data object in the references array to manipulate it however you see fit.
@@ -187,39 +222,23 @@ Here's an example of the references array.
       "type": "AzureSearchDoc",
       "id": "0",
       "activitySource": 2,
-      "docKey": "2",
-      "sourceData": {
-        "id": "2",
-        "parent": {
-          "title": null,
-          "content": "good by cruel world"
-        }
-      }
+      "docKey": "earth_at_night_508_page_104_verbalized",
+      "sourceData": null
     },
     {
       "type": "AzureSearchDoc",
       "id": "1",
       "activitySource": 2,
-      "docKey": "4",
-      "sourceData": {
-        "id": "4",
-        "parent": {
-          "title": "zzzzzzz",
-          "content": "zzzzzzz"
-        }
-      }
+      "docKey": "earth_at_night_508_page_105_verbalized",
+      "sourceData": null
     }
   ]
 ```
 
-<!-- Create H2s for the main patterns. -->
-<!-- This section is in progress. It needs a code sample for the simple case showing how to pipeline ground data to chat completions and responses -->
-## Use data for grounding
-
-The `includeReferenceSourceData` parameter tells the search engine to provide grounding data to the knowledge agent.
-
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
 
++ [Agentic RAG: build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
+
 + [Azure OpenAI Demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azure AI Searchにおけるエージェント型情報取得の変更と強化"
}
```

### Explanation
この変更は、Azure AI Searchにおけるエージェント型情報取得に関するドキュメントの大幅な更新を示しています。具体的には、多くの新しい情報が追加され、既存の情報が改訂されています。

- **文書日付の更新**: 最終更新日が2025年5月30日に変更されました。
- **エージェント型情報取得の説明**: エージェント型情報取得の説明が改良され、会話型の大規模言語モデル（LLM）からチャット完了モデルに言及が変更されました。
- **新しいコンポーネントの追加**: 取得レスポンスの構成要素として「抽出されたレスポンス」、「参照結果」、および「クエリアクティビティ」が追加され、より詳細な情報が提供されています。
- **クエリ処理の指示の追加**: 取得リクエストにおいて、知識エージェントで設定されたデフォルトをオーバーライドできるクエリ処理の指示が含まれるようになりました。
- **API要件の更新**: 使用するAPIやAzure SDKに関する要件が明確化され、詳細が追加されています。具体的な操作例が示され、使い方がより分かりやすくなっています。
- **メッセージ形式の変更**: リクエストおよびレスポンス内の`role`が「system」から「assistant」に変更され、より明確な役割分担がされました。
- **アクティビティ配列の構造更新**: アクティビティ配列の情報が更新され、各クエリの具体的な詳細が反映されています。

この更新により、Azure AI Searchにおけるエージェント型情報取得がさらに強化され、ユーザーに提供される情報が豊富になりました。これにより、開発者とユーザーは新しい機能を利用しやすくなり、より良い体験を得ることができるでしょう。


