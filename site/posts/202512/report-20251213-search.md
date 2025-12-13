---
date: '2025-12-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:65c59a8...MicrosoftDocs:9593226
summary: このコード変更では、.openpublishing.redirection.search.jsonに新しいリダイレクト設定が追加され、ドキュメントの内容においてはマイナーな更新から重大な変更まで多岐にわたっています。特に、いくつかのクイックスタートガイドが削除されたことが大きな影響を与える可能性があります。新しいリダイレクト設定により、ユーザーが古いコンテンツから新コンテンツに容易にアクセスできるようになりましたが、RAGに関連するクイックスタートガイドの削除はユーザーにとって重要な情報の損失を意味します。また、文書の更新や用語の修正により、情報の整理が進められ、利用者にとってより使いやすいドキュメントが提供されています。これらはAzure
  AI Searchに関連する文書の整理と最新化を目的とした重要な変更です。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:65c59a8...MicrosoftDocs:9593226){target="_blank"}

<format>
# Highlights
このコード変更では、.openpublishing.redirection.search.jsonに新しいリダイレクト設定の追加が行われ、他のドキュメントについてはマイナーな更新から重大な変更まで多岐にわたります。特に、いくつかのクイックスタートガイドの削除は大きな影響を与える可能性があります。

## New features
- 新しいリダイレクト設定が追加され、ユーザーが古いコンテンツから新コンテンツに容易にアクセスできるようになった。

## Breaking changes
- RAGに関連する複数のクイックスタートガイド（Java, JavaScript, Python, REST, TypeScript, .NET）の削除は、ユーザーにとって重要で大きな影響を与える。

## Other updates
- ドキュメントの日付や用語の修正、APIエンドポイントの更新、カスタムアナライザーに関する修正など、複数のファイルで小規模な更新が行われた。
- TOC（目次）やサンプルコード関連の文書も更新され、より一貫した情報の整理・提供が行われている。

# Insights
今回のコード変更は、Azure AI Searchに関連するドキュメントの整理と最新化を目的に、多くの主要かつ細かな修正が行われています。特に目立つのは、複数のRAGクイックスタートガイドが削除された点です。これにより、従来のRAG手法から新しい技術や代替手法（エージェンティック・リトリーバル）への移行が焦点となっていることが示されています。

ナビゲーションの改善によりユーザーが情報をより迅速に取得できるように整理されており、古いリンクの削除や新しいリンクの追加が行われています。用語の統一や名称変更（Microsoft FoundryからAzure AI Foundry）によって、製品認識が統一化されています。

一方で、クイックスタートガイドの削除は、開発者にとって大きな情報損失を意味するため、速やかな代替リソースの提供が望まれます。これらの変更は、Azure AI Searchの文書が最新の状態に保たれ、利用者が必要な情報を効果的に活用できるようになるための重要な一環となっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [.openpublishing.redirection.search.json](#item-8b66f9) | new feature | リダイレクト設定の追加 | modified | 5 | 0 | 5 | 
| [agentic-retrieval-how-to-create-knowledge-base.md](#item-7df0e2) | minor update | 日付とインクルードファイルの変更 | modified | 2 | 2 | 4 | 
| [get-started-portal-agentic-retrieval.md](#item-2bf1dc) | minor update | 用語の修正 | modified | 2 | 2 | 4 | 
| [agentic-retrieval-how-to-create-knowledge-base-python.md](#item-4e498f) | minor update | 日付およびコードの修正 | modified | 3 | 2 | 5 | 
| [knowledge-source-status-rest.md](#item-009c0e) | minor update | REST API エンドポイントの修正 | modified | 1 | 1 | 2 | 
| [search-get-started-rag-dotnet.md](#item-c07a99) | breaking change | RAG .NET クイックスタートの削除 | removed | 0 | 362 | 362 | 
| [search-get-started-rag-java.md](#item-26c939) | breaking change | RAG Java クイックスタートの削除 | removed | 0 | 387 | 387 | 
| [search-get-started-rag-javascript.md](#item-69e5ef) | breaking change | RAG JavaScript クイックスタートの削除 | removed | 0 | 389 | 389 | 
| [search-get-started-rag-python.md](#item-3927ba) | breaking change | RAG Python クイックスタートの削除 | removed | 0 | 448 | 448 | 
| [search-get-started-rag-rest.md](#item-aa7f2b) | breaking change | RAG REST クイックスタートの削除 | removed | 0 | 266 | 266 | 
| [search-get-started-rag-typescript.md](#item-11994e) | breaking change | RAG TypeScript クイックスタートの削除 | removed | 0 | 441 | 441 | 
| [index-add-custom-analyzers.md](#item-11325e) | minor update | カスタムアナライザーのドキュメント修正 | modified | 1 | 1 | 2 | 
| [index.yml](#item-c67121) | minor update | Azure AI Search ドキュメントの修正 | modified | 63 | 39 | 102 | 
| [samples-dotnet.md](#item-12f3fa) | minor update | Azure AI Search DotNet サンプルの更新 | modified | 1 | 1 | 2 | 
| [samples-javascript.md](#item-82e67e) | minor update | Azure AI Search JavaScript サンプルの更新 | modified | 2 | 3 | 5 | 
| [samples-python.md](#item-d2bf09) | minor update | Azure AI Search Python サンプルの更新 | modified | 1 | 2 | 3 | 
| [samples-rest.md](#item-198ebc) | minor update | Azure AI Search REST サンプルの更新 | modified | 1 | 6 | 7 | 
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | Azure AI Foundry 名称の変更 | modified | 3 | 3 | 6 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | Azure AI Foundry 名称の変更 | modified | 2 | 2 | 4 | 
| [search-get-started-rag.md](#item-05ff0e) | breaking change | 従来の生成検索 (RAG) ガイドの削除 | removed | 0 | 56 | 56 | 
| [toc.yml](#item-c4768f) | minor update | TOCの内容と構造の更新 | modified | 540 | 509 | 1049 | 


# Modified Contents
## articles/search/.openpublishing.redirection.search.json{#item-8b66f9}

<details>
<summary>Diff</summary>
````diff
@@ -640,6 +640,11 @@
             "source_path_from_root": "/articles/search/tutorial-csharp-create-mvc-app.md",
             "redirect_url": "/azure/search/tutorial-csharp-overview",
             "redirect_document_id": false
+        },
+        {
+            "source_path_from_root": "/articles/search/search-get-started-rag.md",
+            "redirect_url": "https://github.com/Azure-Samples/azure-search-classic-rag/tree/main/quickstarts",
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
    "modification_type": "new feature",
    "modification_title": "リダイレクト設定の追加"
}
```

### Explanation
このコードの変更は、`.openpublishing.redirection.search.json`ファイルに新しいリダイレクト設定を追加することに関するものです。具体的には、新しいリダイレクトエントリが追加され、コンテンツが特定のパスから新しいURLへ移動するように設定されています。この変更では、リダイレクト対象として`/articles/search/search-get-started-rag.md`が指定されており、リダイレクト先のURLは`https://github.com/Azure-Samples/azure-search-classic-rag/tree/main/quickstarts`となっています。このように、新しいリダイレクトルールを追加することで、ユーザーが古いコンテンツにアクセスした際に現在のコンテンツに適切に誘導されるようになります。

## articles/search/agentic-retrieval-how-to-create-knowledge-base.md{#item-7df0e2}

<details>
<summary>Diff</summary>
````diff
@@ -6,14 +6,14 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 11/19/2025
+ms.date: 12/12/2025
 zone_pivot_groups: agentic-retrieval-pivots
 ---
 
 # Create a knowledge base in Azure AI Search
 
 ::: zone pivot="csharp"
-[!INCLUDE [C#](includes/how-tos/agentic-knowledge-source-how-to-search-index-csharp.md)]
+[!INCLUDE [C#](includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-csharp.md)]
 ::: zone-end
 
 ::: zone pivot="python"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付とインクルードファイルの変更"
}
```

### Explanation
このコードの変更は、`agentic-retrieval-how-to-create-knowledge-base.md`ファイルのいくつかのパラメータを更新することに関するものです。具体的には、ドキュメントの日付が`11/19/2025`から`12/12/2025`に変更され、リダイレクトされるC#のインクルードファイルも更新されています。新しいインクルードファイルは`agentic-retrieval-how-to-create-knowledge-base-csharp.md`であり、これにより、最新の情報を持つ内容が正しく参照されるようになります。このように、文書の正確性と関連性を保つための小規模な更新が行われました。

## articles/search/get-started-portal-agentic-retrieval.md{#item-2bf1dc}

<details>
<summary>Diff</summary>
````diff
@@ -139,7 +139,7 @@ To create the knowledge source for this quickstart:
 
 1. Select **Add vectorizer**.
 
-1. Select **Microsoft Foundry** for the kind, and then select your subscription, project, and embedding model deployment.
+1. Select **Azure AI Foundry** for the kind, and then select your subscription, project, and embedding model deployment.
 
 1. Select **System managed identity** for the authentication type.
 
@@ -166,7 +166,7 @@ To create the knowledge base for this quickstart:
 
 1. Under **Model deployment**, select **Add model deployment**.
 
-1. Select **Foundry** for the kind, and then select your subscription, project, and LLM deployment.
+1. Select **Azure AI Foundry** for the kind, and then select your subscription, project, and LLM deployment.
 
 1. Select **System assigned identity** for the authentication type.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の修正"
}
```

### Explanation
このコードの変更は、`get-started-portal-agentic-retrieval.md`ファイルにおける用語の修正に関するものです。具体的には、手順の中で「Microsoft Foundry」という用語が「Azure AI Foundry」に変更されています。この変更は、正確な製品名を使用することで、ユーザーに混乱を与えないようにするためのものです。手順においても同様に、関連する箇所で一貫性を保つために同様の修正が行われています。全体として、この変更はドキュメントの明確さと正確性を向上させるための小規模な更新です。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-python.md{#item-4e498f}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/14/2025
+ms.date: 12/12/2025
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -160,6 +160,7 @@ index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyC
 
 aoai_params = AzureOpenAIVectorizerParameters(
     resource_url = "aoai_endpoint",
+    api_key="aoai_api_key",
     deployment_name = "aoai_gpt_deployment",
     model_name = "aoai_gpt_model",
 )
@@ -209,7 +210,7 @@ Replace "Where does the ocean look green?" with a query string that's valid for
 # Send grounding request
 from azure.core.credentials import AzureKeyCredential
 from azure.search.documents.knowledgebases import KnowledgeBaseRetrievalClient
-from azure.search.documents.knowledgebases.models import KnowledgeBaseMessage, KnowledgeBaseMessageTextContent, KnowledgeBaseRetrievalRequest, RemoteSharePointKnowledgeSourceParams
+from azure.search.documents.knowledgebases.models import KnowledgeBaseMessage, KnowledgeBaseMessageTextContent, KnowledgeBaseRetrievalRequest, SearchIndexKnowledgeSourceParams
 
 kb_client = KnowledgeBaseRetrievalClient(endpoint = "search_url", knowledge_base_name = "knowledge_base_name", credential = AzureKeyCredential("api_key"))
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付およびコードの修正"
}
```

### Explanation
このコードの変更は、`agentic-retrieval-how-to-create-knowledge-base-python.md`ファイルのいくつかの要素に関するものです。最初に、文書の日付が`11/14/2025`から`12/12/2025`に変更され、最新の情報が反映されています。次に、コードセクション内で`AzureOpenAIVectorizerParameters`のパラメータに`api_key`という新しいエントリが追加され、ユーザーがAPIキーを指定できるようになりました。また、インポート文の一部が修正され、`RemoteSharePointKnowledgeSourceParams`から`SearchIndexKnowledgeSourceParams`が新たに使用されています。これにより、最新のAPIやライブラリに基づいた正確なコードが提供されており、ドキュメントの有用性が向上しています。全体として、これらの修正はマイナーな更新ですが、技術的な明確さを改善することに寄与しています。

## articles/search/includes/how-tos/knowledge-source-status-rest.md{#item-009c0e}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.topic: include
 ms.date: 11/14/2025
 ---
 
-Use [Knowledge Sources - Status (REST API)](/rest/api/searchservice/knowledge-sources/status?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to monitor ingestion progress and health, including indexer status for knowledge sources that generate an indexer pipeline and populate a search index.
+Use [Knowledge Sources - Status (REST API)](/rest/api/searchservice/knowledge-sources/get-status) to monitor ingestion progress and health, including indexer status for knowledge sources that generate an indexer pipeline and populate a search index.
 
 ```http
 ### Check knowledge source ingestion status
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST API エンドポイントの修正"
}
```

### Explanation
このコードの変更は、`knowledge-source-status-rest.md`ファイル内のREST APIエンドポイントに関するもので、特定のURLが修正されています。具体的には、旧いエンドポイントの`/status`が新しいエンドポイント`/get-status`に変更されました。この更新は、APIの最新の仕様に合わせるものであり、ユーザーが適切なエンドポイントを使用して、知識ソースの取り込みの進行状況や健康状態を監視できるようにするための重要な修正です。全体として、この変更はマイナーな更新ですが、正確な情報を提供するための重要な改善点です。

## articles/search/includes/quickstarts/search-get-started-rag-dotnet.md{#item-c07a99}

<details>
<summary>Diff</summary>
````diff
@@ -1,362 +0,0 @@
----
-manager: nitinme
-author: haileytap
-ms.author: haileytapia
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 06/05/2025
----
-## Prerequisites
-
-- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-
-- An [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource).
-  - [Choose a region](/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#global-standard-model-availability) that supports the chat completion model you want to use (gpt-4o, gpt-4o-mini, or an equivalent model).
-  - [Deploy the chat completion model](/azure/ai-foundry/how-to/deploy-models-openai) in Microsoft Foundry or [use another approach](/azure/ai-services/openai/how-to/working-with-models).
-- An [Azure AI Search resource](../../search-create-service-portal.md).
-  - We recommend using the Basic tier or higher.
-  - [Enable semantic ranking](../../semantic-how-to-enable-disable.md).
-- [Visual Studio Code](https://code.visualstudio.com/download) or [Visual Studio](https://visualstudio.com).
-- [.NET 9.0](https://dotnet.microsoft.com/download) installed.
-
-## Configure access
-
-Requests to the search endpoint must be authenticated and authorized. You can use API keys or roles for this task. Keys are easier to start with, but roles are more secure. This quickstart assumes roles.
-
-You're setting up two clients, so you need permissions on both resources.
-
-Azure AI Search is receiving the query request from your local system. Assign yourself the **Search Index Data Reader** role assignment if the hotels sample index already exists. If it doesn't exist, assign yourself **Search Service Contributor** and **Search Index Data Contributor** roles so that you can create and query the index.
-
-Azure OpenAI is receiving the query and the search results from your local system. Assign yourself the **Cognitive Services OpenAI User** role on Azure OpenAI.
-
-1. Sign in to the [Azure portal](https://portal.azure.com).
-
-1. Configure Azure AI Search for role-based access:
-
-    1. In the Azure portal, find your Azure AI Search service.
-
-    1. On the left menu, select **Settings** > **Keys**, and then select either **Role-based access control** or **Both**.
-
-1. Assign roles:
-
-    1. On the left menu, select **Access control (IAM)**.
-
-    1. On Azure AI Search, select these roles to create, load, and query a search index, and then assign them to your Microsoft Entra ID user identity:
-
-       - **Search Index Data Contributor**
-       - **Search Service Contributor**
-
-    1. On Azure OpenAI, select **Access control (IAM)** to assign this role to yourself on Azure OpenAI:
-
-       - **Cognitive Services OpenAI User**
-
-It can take several minutes for permissions to take effect.
-
-## Create an index
-
-A search index provides grounding data for the chat model. We recommend the hotels-sample-index, which you can create by running the [**Import data (new)**](../../search-import-data-portal.md) wizard and following the instructions to create the index.
-
-1. In the Azure portal, [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
-
-1. On the **Overview** home page, select [**Import data**](../../search-get-started-portal.md) to start the wizard.
-
-1. On the **Connect to your data** page, select **Samples** from the dropdown list.
-
-1. Choose the **hotels-sample**.
-
-1. Select **Next** through the remaining pages, accepting the default values.
-
-1. Once the index is created, select **Search management** > **Indexes** from the left menu to open the index.
-
-1. Select **Edit JSON**. 
-
-1. Scroll to the end of the index, where you can find placeholders for constructs that can be added to an index.
-
-   ```json
-   "analyzers": [],
-   "tokenizers": [],
-   "tokenFilters": [],
-   "charFilters": [],
-   "normalizers": [],
-   ```
-
-1. On a new line after "normalizers", paste in the following semantic configuration. This example specifies a `"defaultConfiguration"`, which is important to the running of this quickstart.
-
-    ```json
-    "semantic":{
-       "defaultConfiguration":"semantic-config",
-       "configurations":[
-          {
-             "name":"semantic-config",
-             "prioritizedFields":{
-                "titleField":{
-                   "fieldName":"HotelName"
-                },
-                "prioritizedContentFields":[
-                   {
-                      "fieldName":"Description"
-                   }
-                ],
-                "prioritizedKeywordsFields":[
-                   {
-                      "fieldName":"Category"
-                   },
-                   {
-                      "fieldName":"Tags"
-                   }
-                ]
-             }
-          }
-       ]
-    },
-    ```
-
-1. **Save** your changes.
-
-1. Run the following query in [Search Explorer](../../search-explorer.md) to test your index: `complimentary breakfast`.
-
-   Output should look similar to the following example. Results that are returned directly from the search engine consist of fields and their verbatim values, along with metadata like a search score and a semantic ranking score and caption if you use semantic ranker. We used a [select statement](../../search-query-odata-select.md) to return just the HotelName, Description, and Tags fields.
-
-   ```
-   {
-   "@odata.count": 18,
-   "@search.answers": [],
-   "value": [
-      {
-         "@search.score": 2.2896252,
-         "@search.rerankerScore": 2.506816864013672,
-         "@search.captions": [
-         {
-            "text": "Head Wind Resort. Suite. coffee in lobby\r\nfree wifi\r\nview. The best of old town hospitality combined with views of the river and cool breezes off the prairie. Our penthouse suites offer views for miles and the rooftop plaza is open to all guests from sunset to 10 p.m. Enjoy a **complimentary continental breakfast** in the lobby, and free Wi-Fi throughout the hotel..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "Head Wind Resort",
-         "Description": "The best of old town hospitality combined with views of the river and cool breezes off the prairie. Our penthouse suites offer views for miles and the rooftop plaza is open to all guests from sunset to 10 p.m. Enjoy a complimentary continental breakfast in the lobby, and free Wi-Fi throughout the hotel.",
-         "Tags": [
-         "coffee in lobby",
-         "free wifi",
-         "view"
-         ]
-      },
-      {
-         "@search.score": 2.2158256,
-         "@search.rerankerScore": 2.288334846496582,
-         "@search.captions": [
-         {
-            "text": "Swan Bird Lake Inn. Budget. continental breakfast\r\nfree wifi\r\n24-hour front desk service. We serve a continental-style breakfast each morning, featuring a variety of food and drinks. Our locally made, oh-so-soft, caramel cinnamon rolls are a favorite with our guests. Other breakfast items include coffee, orange juice, milk, cereal, instant oatmeal, bagels, and muffins..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "Swan Bird Lake Inn",
-         "Description": "We serve a continental-style breakfast each morning, featuring a variety of food and drinks. Our locally made, oh-so-soft, caramel cinnamon rolls are a favorite with our guests. Other breakfast items include coffee, orange juice, milk, cereal, instant oatmeal, bagels, and muffins.",
-         "Tags": [
-         "continental breakfast",
-         "free wifi",
-         "24-hour front desk service"
-         ]
-      },
-      {
-         "@search.score": 0.92481667,
-         "@search.rerankerScore": 2.221315860748291,
-         "@search.captions": [
-         {
-            "text": "White Mountain Lodge & Suites. Resort and Spa. continental breakfast\r\npool\r\nrestaurant. Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "White Mountain Lodge & Suites",
-         "Description": "Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings.",
-         "Tags": [
-         "continental breakfast",
-         "pool",
-         "restaurant"
-         ]
-      },
-      . . .
-   ]}
-   ```
-
-## Get service endpoints
-
-In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints so that you can provide them as variables in your code.
-
-1. Sign in to the [Azure portal](https://portal.azure.com).
-
-1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
-
-1. On the **Overview** home page, copy the URL. An example endpoint might look like `https://example.search.windows.net`. 
-
-1. [Find your Azure OpenAI service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.CognitiveServices%2Faccounts).
-
-1. On the **Overview** home page, select the link to view the endpoints. Copy the URL. An example endpoint might look like `https://example.openai.azure.com/`.
-
-## Sign in to Azure
-
-You're using Microsoft Entra ID and role assignments for the connection. Make sure you're logged in to the same tenant and subscription as Azure AI Search and Azure OpenAI. You can use the Azure CLI on the command line to show current properties, change properties, and to sign in. For more information, see [Connect without keys](../../search-get-started-rbac.md). 
-
-Run each of the following commands in sequence.
-
-```azure-cli
-az account show
-
-az account set --subscription <PUT YOUR SUBSCRIPTION ID HERE>
-
-az login --tenant <PUT YOUR TENANT ID HERE>
-```
-
-You should now be logged in to Azure from your local device.
-
-## Set up the .NET app
-
-To follow along with the steps ahead, you can either clone the completed sample app from GitHub, or create the app yourself.
-
-### Clone the sample app
-
-To access the completed sample app for this article: 
-
-1. Clone the [azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples) repo from GitHub.
-
-    ```bash
-    git clone https://github.com/Azure-Samples/azure-search-dotnet-samples
-    ```
-
-1. Navigate into the `quickstart-rag` folder.
-1. Open the `quickstart-rag` folder in Visual Studio Code or open the solution file using Visual Studio.
-
-### Create the sample app
-
-Complete the following steps to create a .NET console app to connect to an AI model.
-
-1. In an empty directory on your computer, use the `dotnet new` command to create a new console app:
-
-    ```dotnetcli
-    dotnet new console -o AISearchRag
-    ```
-
-1. Change directory into the app folder:
-
-    ```dotnetcli
-    cd AISearchRag
-    ```
-
-1. Install the required packages:
-
-    ```bash
-    dotnet add package Azure.AI.OpenAI
-    dotnet add package Azure.Identity
-    dotnet add package Azure.Search.Documents
-    ```
-
-1. Open the app in Visual Studio Code (or your editor of choice).
-
-    ```bash
-    code .
-    ```
-
-## Set up the query and chat thread
-
-The following example demonstrates how to set up a minimal RAG scenario using Azure AI Search to provide an OpenAI model with contextual resources to improve the generated responses.
-
-1. In the `minimal-query` project of the sample repo, open the `Program.cs` file to view the first example. If you created the project yourself, add the following code to connect to and query the Azure AI Search and Azure OpenAI services.
-
-    > [!NOTE]
-    > Make sure to replace the placeholders for the Azure OpenAI endpoint and model name, as well as the Azure AI Search endpoint and index name.
-    
-    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-rag/minimal-query/Program.cs" :::
-    
-    The preceding code accomplishes the following:
-    
-    - Searches an Azure Search index for hotels matching a user query about complimentary breakfast, retrieving hotel name, description, and tags.
-    - Formats the search results into a structured list to serve as contextual sources for the generative AI model.
-    - Constructs a prompt instructing the Azure OpenAI model to answer using only the provided sources.
-    - Sends the prompt to the AI model and streams the generated response.
-    - Outputs the AI’s response to the console, displaying both the role and content as it streams.
-
-1. Run the project to initiate a basic RAG scenario. The output from Azure OpenAI consists of recommendations for several hotels, such as the following example:
-    
-    ```output
-    Sure! Here are a few hotels that offer complimentary breakfast:
-    
-    - **Head Wind Resort**
-    - Complimentary continental breakfast in the lobby
-    - Free Wi-Fi throughout the hotel
-    
-    - **Double Sanctuary Resort**
-    - Continental breakfast included
-    
-    - **White Mountain Lodge & Suites**
-    - Continental breakfast available
-    
-    - **Swan Bird Lake Inn**
-    - Continental-style breakfast each morning with a variety of food and drinks 
-       such as caramel cinnamon rolls, coffee, orange juice, milk, cereal, 
-       instant oatmeal, bagels, and muffins
-    ```
-
-To experiment further, change the query and rerun the last step to better understand how the model works with the grounding data. You can also modify the prompt to change the tone or structure of the output.
-
-### Troubleshooting
-
-You might receive any of the following errors while testing:
-
-- **Forbidden**: Check Azure AI Search configuration to make sure role-based access is enabled.
-- **Authorization failed**: Wait a few minutes and try again. It can take several minutes for role assignments to become operational.
-- **Resource not found**: Check the resource URIs and make sure the API version on the chat model is valid.
-
-## Send a complex RAG query
-
-Azure AI Search supports [complex types](../../search-howto-complex-data-types.md) for nested JSON structures. In the hotels-sample-index, `Address` is an example of a complex type, consisting of `Address.StreetAddress`, `Address.City`, `Address.StateProvince`, `Address.PostalCode`, and `Address.Country`. The index also has complex collection of `Rooms` for each hotel. If your index has complex types, your query can provide those fields if you first convert the search results output to JSON, and then pass the JSON to the chat model.
-
-1. In the `complex-query` project of the sample repo, open the `Program.cs` file. If you created the project yourself, replace your code with the following:
-
-    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-rag/complex-query/Program.cs" :::
-
-2. Run the project to initiate a basic RAG scenario. The output from Azure OpenAI consists of recommendations for several hotels, such as the following example:
-
-    ```output
-    1. **Double Sanctuary Resort**
-       - **Description**: 5-star luxury hotel with the biggest rooms in the city. Recognized as the #1 hotel in the area by Traveler magazine. Features include free WiFi, flexible check-in/out, a fitness center, and in-room espresso.
-       - **Address**: 2211 Elliott Ave, Seattle, WA, 98121, USA
-       - **Tags**: view, pool, restaurant, bar, continental breakfast
-       - **Room Rate for 4 People**: 
-         - Suite, 2 Queen Beds: $254.99 per night
-    
-    2. **Starlight Suites**
-       - **Description**: Spacious all-suite hotel with complimentary airport shuttle and WiFi. Facilities include an indoor/outdoor pool, fitness center, and Florida Green certification. Complimentary coffee and HDTV are also available.
-       - **Address**: 19575 Biscayne Blvd, Aventura, FL, 33180, USA
-       - **Tags**: pool, coffee in lobby, free wifi
-       - **Room Rate for 4 People**:
-         - Suite, 2 Queen Beds (Cityside): $231.99 per night
-         - Deluxe Room, 2 Queen Beds (Waterfront View): $148.99 per night
-    
-    3. **Good Business Hotel**
-       - **Description**: Located one mile from the airport with free WiFi, an outdoor pool, and a complimentary airport shuttle. Close proximity to Lake Lanier and downtown. The business center includes printers, a copy machine, fax, and a work area.
-       - **Address**: 4400 Ashford Dunwoody Rd NE, Atlanta, GA, 30346, USA
-       - **Tags**: pool, continental breakfast, free parking
-       - **Room Rate for 4 People**:
-         - Budget Room, 2 Queen Beds (Amenities): $60.99 per night
-         - Deluxe Room, 2 Queen Beds (Amenities): $139.99 per night
-    ```
-
-## Troubleshooting
-
-If you see output messages while debugging related to `ManagedIdentityCredential` and token acquisition failures, it could be that you have multiple tenants, and your Azure sign-in is using a tenant that doesn't have your search service. To get your tenant ID, search the Azure portal for "tenant properties" or run `az login tenant list`.
-
-Once you have your tenant ID, run `az login --tenant <YOUR-TENANT-ID>` at a command prompt, and then rerun the script.
-
-You can also log errors in your code by creating an instance of `ILogger`:
-
-```csharp
-using var loggerFactory = LoggerFactory.Create(builder =>
-{
-   builder.AddConsole();
-});
-ILogger logger = loggerFactory.CreateLogger<Program>();
-```
-
-## Clean up
-
-When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "RAG .NET クイックスタートの削除"
}
```

### Explanation
このコードの変更は、`search-get-started-rag-dotnet.md`ファイルが完全に削除されたことに関するものです。この削除には、362行に及ぶ内容が含まれており、具体的には、Azure AI SearchとAzure OpenAIのリソースに関するクイックスタートガイドがなくなっています。このファイルには、Azureアカウントの作成手順、必要なリソースの設定、APIの呼び出し方、クエリの実行方法、サンプルアプリの作成手順などが詳細に記載されていました。この変更は、関連する情報の整理や更新の一環として行われた可能性がありますが、ユーザーにとっては重要なリソースの喪失となるため、影響が大きいと考えられます。新しい情報やシステムが導入される場合は、別のガイドラインを参照する必要があります。

## articles/search/includes/quickstarts/search-get-started-rag-java.md{#item-26c939}

<details>
<summary>Diff</summary>
````diff
@@ -1,387 +0,0 @@
----
-manager: nitinme
-author: KarlErickson
-ms.author: karler
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 08/08/2025
-ai-usage: ai-assisted
----
-## Prerequisites
-
-- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-
-- An [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource).
-  - [Choose a region](/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#global-standard-model-availability) that supports the chat completion model you want to use (gpt-4o, gpt-4o-mini, or an equivalent model).
-  - [Deploy the chat completion model](/azure/ai-foundry/how-to/deploy-models-openai) in Microsoft Foundry or [use another approach](/azure/ai-services/openai/how-to/working-with-models).
-- An [Azure AI Search resource](../../search-create-service-portal.md).
-  - We recommend using the Basic tier or higher.
-  - [Enable semantic ranking](../../semantic-how-to-enable-disable.md).
-- [Visual Studio Code](https://code.visualstudio.com/download).
-- [Java 21 (LTS)](/java/openjdk/install).
-- [Maven](https://maven.apache.org/download.cgi).
-
-## Configure access
-
-Requests to the search endpoint must be authenticated and authorized. You can use API keys or roles for this task. Keys are easier to start with, but roles are more secure. This quickstart assumes roles.
-
-You're setting up two clients, so you need permissions on both resources.
-
-Azure AI Search receives the query request from your local system. Assign yourself the **Search Index Data Reader** role assignment if the hotels sample index already exists. If it doesn't exist, assign yourself **Search Service Contributor** and **Search Index Data Contributor** roles so that you can create and query the index.
-
-Azure OpenAI receives the query and the search results from your local system. Assign yourself the **Cognitive Services OpenAI User** role on Azure OpenAI.
-
-1. Sign in to the [Azure portal](https://portal.azure.com).
-
-1. Configure Azure AI Search for role-based access:
-
-    1. In the Azure portal, find your Azure AI Search service.
-
-    1. On the left menu, select **Settings** > **Keys**, then select either **Role-based access control** or **Both**.
-
-1. Assign roles:
-
-    1. On the left menu, select **Access control (IAM)**.
-
-    1. On Azure AI Search, select these roles to create, load, and query a search index, then assign them to your Microsoft Entra ID user identity:
-
-       - **Search Index Data Contributor**
-       - **Search Service Contributor**
-
-    1. On Azure OpenAI, select **Access control (IAM)** to assign this role to yourself on Azure OpenAI:
-
-       - **Cognitive Services OpenAI User**
-
-It can take several minutes for permissions to take effect.
-
-## Create an index
-
-A search index provides grounding data for the chat model. We recommend the **hotels-sample-index**.
-
-1. In the Azure portal, [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
-
-1. Follow the instructions in [this quickstart](../../search-import-data-portal.md) to create the index.
-
-1. Once the index is created, select **Search management** > **Indexes** from the left menu to open the index.
-
-1. Select **Edit JSON**. 
-
-1. Scroll to the end of the index, where you find placeholders for constructs that you can add to an index.
-
-   ```json
-   "analyzers": [],
-   "tokenizers": [],
-   "tokenFilters": [],
-   "charFilters": [],
-   "normalizers": [],
-   ```
-
-1. On a new line after "normalizers", paste in the following semantic configuration. This example specifies a `"defaultConfiguration"`, which is important to the running of this quickstart.
-
-    ```json
-    "semantic":{
-       "defaultConfiguration":"semantic-config",
-       "configurations":[
-          {
-             "name":"semantic-config",
-             "prioritizedFields":{
-                "titleField":{
-                   "fieldName":"HotelName"
-                },
-                "prioritizedContentFields":[
-                   {
-                      "fieldName":"Description"
-                   }
-                ],
-                "prioritizedKeywordsFields":[
-                   {
-                      "fieldName":"Category"
-                   },
-                   {
-                      "fieldName":"Tags"
-                   }
-                ]
-             }
-          }
-       ]
-    },
-    ```
-
-1. **Save** your changes.
-
-1. Run the following query in [Search Explorer](../../search-explorer.md) to test your index: `complimentary breakfast`.
-
-   The output should look similar to the following example. Results that are returned directly from the search engine consist of fields and their verbatim values, along with metadata like a search score and a semantic ranking score and caption if you use semantic ranker. We used a [select statement](../../search-query-odata-select.md) to return just the HotelName, Description, and Tags fields.
-
-   ```
-   {
-   "@odata.count": 18,
-   "@search.answers": [],
-   "value": [
-      {
-         "@search.score": 2.2896252,
-         "@search.rerankerScore": 2.506816864013672,
-         "@search.captions": [
-         {
-            "text": "Head Wind Resort. Suite. coffee in lobby\r\nfree wifi\r\nview. The best of old town hospitality combined with views of the river and cool breezes off the prairie. Our penthouse suites offer views for miles and the rooftop plaza is open to all guests from sunset to 10 p.m. Enjoy a **complimentary continental breakfast** in the lobby, and free Wi-Fi throughout the hotel..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "Head Wind Resort",
-         "Description": "The best of old town hospitality combined with views of the river and cool breezes off the prairie. Our penthouse suites offer views for miles and the rooftop plaza is open to all guests from sunset to 10 p.m. Enjoy a complimentary continental breakfast in the lobby, and free Wi-Fi throughout the hotel.",
-         "Tags": [
-         "coffee in lobby",
-         "free wifi",
-         "view"
-         ]
-      },
-      {
-         "@search.score": 2.2158256,
-         "@search.rerankerScore": 2.288334846496582,
-         "@search.captions": [
-         {
-            "text": "Swan Bird Lake Inn. Budget. continental breakfast\r\nfree wifi\r\n24-hour front desk service. We serve a continental-style breakfast each morning, featuring a variety of food and drinks. Our locally made, oh-so-soft, caramel cinnamon rolls are a favorite with our guests. Other breakfast items include coffee, orange juice, milk, cereal, instant oatmeal, bagels, and muffins..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "Swan Bird Lake Inn",
-         "Description": "We serve a continental-style breakfast each morning, featuring a variety of food and drinks. Our locally made, oh-so-soft, caramel cinnamon rolls are a favorite with our guests. Other breakfast items include coffee, orange juice, milk, cereal, instant oatmeal, bagels, and muffins.",
-         "Tags": [
-         "continental breakfast",
-         "free wifi",
-         "24-hour front desk service"
-         ]
-      },
-      {
-         "@search.score": 0.92481667,
-         "@search.rerankerScore": 2.221315860748291,
-         "@search.captions": [
-         {
-            "text": "White Mountain Lodge & Suites. Resort and Spa. continental breakfast\r\npool\r\nrestaurant. Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "White Mountain Lodge & Suites",
-         "Description": "Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings.",
-         "Tags": [
-         "continental breakfast",
-         "pool",
-         "restaurant"
-         ]
-      },
-      . . .
-   ]}
-   ```
-
-## Get service endpoints
-
-In the following sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints so that you can provide them as variables in your code.
-
-1. Sign in to the [Azure portal](https://portal.azure.com).
-
-1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
-
-1. On the **Overview** home page, copy the URL. An example endpoint might look like `https://example.search.windows.net`. 
-
-1. [Find your Azure OpenAI service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.CognitiveServices%2Faccounts).
-
-1. On the **Overview** home page, select the link to view the endpoints. Copy the URL. An example endpoint might look like `https://example.openai.azure.com/`.
-
-## Set up environment variables for local development
-
-Define environment variables by using the following commands. Replace the placeholders with your actual values.
-
-```bash
-export AZURE_SEARCH_ENDPOINT=<YOUR AZURE AI SEARCH ENDPOINT>
-export AZURE_SEARCH_INDEX_NAME=hotels-sample-index
-export AZURE_OPENAI_ENDPOINT=<YOUR AZURE OPENAI ENDPOINT>
-export AZURE_DEPLOYMENT_MODEL=<YOUR DEPLOYMENT NAME>
-```
-
-## Sign in to Azure
-
-You're using Microsoft Entra ID and role assignments for the connection. Make sure you're signed in to the same tenant and subscription as Azure AI Search and Azure OpenAI. You can use the Azure CLI on the command line to show current properties, change properties, and to sign in. For more information, see [Connect without keys](../../search-get-started-rbac.md). 
-
-Run each of the following commands in sequence.
-
-```azure-cli
-az account show
-
-az account set --subscription <PUT YOUR SUBSCRIPTION ID HERE>
-
-az login --tenant <PUT YOUR TENANT ID HERE>
-```
-
-You're now signed in to Azure from your local device.
-
-## Set up the Java project
-
-Set up a Maven project with the required dependencies.
-
-1. Create a new directory and navigate to it:
-
-   ```bash
-   mkdir rag-quickstart && cd rag-quickstart
-   ```
-
-1. Create a Maven project structure:
-
-   ```bash
-   mkdir -p src/main/java/com/example/rag
-   ```
-
-1. Create a `pom.xml` file with the following content:
-
-   :::code language="xml" source="~/azure-search-java-samples/rag-quickstart/pom.xml" :::
-
-## Set up query and chat thread
-
-Create a query script that uses the Azure AI Search index and the chat model to generate responses based on grounding data. The following steps guide you through setting up the query script.
-
-1. Create a `Query.java` file in the `src/main/java/com/example/rag` directory with the following code:
-
-   :::code language="java" source="~/azure-search-java-samples/rag-quickstart/src/main/java/com/example/rag/Query.java" :::
-
-    The preceding code does the following steps:
-    - Loads environment variables by using `System.getenv`.
-    - Configures Azure AI Search and Azure OpenAI clients by using role-based authentication.
-    - Queries Azure AI Search for hotels with complimentary breakfast by using semantic search.
-    - Sends the search results to Azure OpenAI as context for a chat completion.
-    - Prints the model's response.
-
-1. Run the following command in a terminal to execute the query script:
-
-    ```bash
-    mvn compile exec:java -Dexec.mainClass="com.example.rag.Query"
-    ```
-
-1. View the output, which consists of recommendations for several hotels. Here's an example of what the output might look like:
-
-    ```
-    Sure! Here are a few hotels that offer complimentary breakfast:
-
-    - **Head Wind Resort**
-    - Complimentary continental breakfast in the lobby
-    - Free Wi-Fi throughout the hotel
-
-    - **Double Sanctuary Resort**
-    - Continental breakfast included
-
-    - **White Mountain Lodge & Suites**
-    - Continental breakfast available
-
-    - **Swan Bird Lake Inn**
-    - Continental-style breakfast each morning with a variety of food and drinks 
-        such as caramel cinnamon rolls, coffee, orange juice, milk, cereal, 
-        instant oatmeal, bagels, and muffins
-    ```
-
-## Troubleshooting
-
-If you get a **Forbidden** error message, check your Azure AI Search configuration to make sure you enable role-based access.
-
-If you get an **Authorization failed** error message, wait a few minutes and try again. It can take several minutes for role assignments to become operational.
-
-If you get a **Resource not found** error message, check the resource URIs and make sure the API version on the chat model is valid.
-
-Otherwise, to experiment further, change the query and rerun the last step to better understand how the model works with the grounding data.
-
-You can also modify the prompt to change the tone or structure of the output.
-
-You might also try the query without semantic ranking by removing the semantic search options in the query parameters step. Semantic ranking can noticeably improve the relevance of query results and the ability of the LLM to return useful information. Experimentation can help you decide whether it makes a difference for your content.
-
-## Send a complex RAG query
-
-Azure AI Search supports [complex types](../../search-howto-complex-data-types.md) for nested JSON structures. In the hotels-sample-index, `Address` is an example of a complex type, consisting of `Address.StreetAddress`, `Address.City`, `Address.StateProvince`, `Address.PostalCode`, and `Address.Country`. The index also has complex collection of `Rooms` for each hotel.
-
-If your index has complex types, change your prompt to include formatting instructions: 
-
-```text
-Can you recommend a few hotels that offer complimentary breakfast? 
-Tell me their description, address, tags, and the rate for one room that sleeps 4 people.
-```
-
-1. Create a new file `QueryComplex.java` in the `src/main/java/com/example/rag` directory.
-1. Copy the following code to the file:
-
-   :::code language="java" source="~/azure-search-java-samples/rag-quickstart/src/main/java/com/example/rag/QueryComplex.java" :::
-
-1. Run the following command in a terminal to execute the query script:
-
-    ```bash
-    mvn compile exec:java -Dexec.mainClass="com.example.rag.QueryComplex"
-    ```
-
-1. View the output from Azure OpenAI, and it adds content from complex types.
-
-    ```
-    Here are a few hotels that offer complimentary breakfast and have rooms that sleep 4 people:
-
-    1. **Head Wind Resort**
-       - **Description:** The best of old town hospitality combined with views of the river and 
-       cool breezes off the prairie. Enjoy a complimentary continental breakfast in the lobby, 
-       and free Wi-Fi throughout the hotel.
-       - **Address:** 7633 E 63rd Pl, Tulsa, OK 74133, USA
-       - **Tags:** Coffee in lobby, free Wi-Fi, view
-       - **Room for 4:** Suite, 2 Queen Beds (Amenities) - $254.99
-
-    2. **Double Sanctuary Resort**
-       - **Description:** 5-star Luxury Hotel - Biggest Rooms in the city. #1 Hotel in the area 
-       listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso 
-       in room. Offers continental breakfast.
-       - **Address:** 2211 Elliott Ave, Seattle, WA 98121, USA
-       - **Tags:** View, pool, restaurant, bar, continental breakfast
-       - **Room for 4:** Suite, 2 Queen Beds (Amenities) - $254.99
-
-    3. **Swan Bird Lake Inn**
-       - **Description:** Continental-style breakfast featuring a variety of food and drinks. 
-       Locally made caramel cinnamon rolls are a favorite.
-       - **Address:** 1 Memorial Dr, Cambridge, MA 02142, USA
-       - **Tags:** Continental breakfast, free Wi-Fi, 24-hour front desk service
-       - **Room for 4:** Budget Room, 2 Queen Beds (City View) - $85.99
-
-    4. **Gastronomic Landscape Hotel**
-       - **Description:** Known for its culinary excellence under the management of William Dough, 
-       offers continental breakfast.
-       - **Address:** 3393 Peachtree Rd, Atlanta, GA 30326, USA
-       - **Tags:** Restaurant, bar, continental breakfast
-       - **Room for 4:** Budget Room, 2 Queen Beds (Amenities) - $66.99
-    ...
-       - **Tags:** Pool, continental breakfast, free parking
-       - **Room for 4:** Budget Room, 2 Queen Beds (Amenities) - $60.99
-
-    Enjoy your stay! Let me know if you need any more information.
-    ```
-
-## Troubleshooting errors
-
-To debug Azure SDK errors, enable logging by adding the following dependency to your `pom.xml`:
-
-```xml
-<dependency>
-    <groupId>org.slf4j</groupId>
-    <artifactId>slf4j-simple</artifactId>
-    <version>2.0.7</version>
-</dependency>
-```
-
-Then set the following system properties when running your application:
-
-```bash
-mvn compile exec:java -Dexec.mainClass="com.example.rag.Query" \
-    -Dorg.slf4j.simpleLogger.defaultLogLevel=debug
-```
-
-This configuration enables detailed logging for the Azure SDK, which can help you identify [issues with authentication](https://github.com/Azure/azure-sdk-for-java/wiki/Azure-Identity-Troubleshooting), network connectivity, or other problems.
-
-Rerun the query script. You should now see informational statements from the SDKs in the output that provide more detail about any issues.
-
-If you see output messages related to `ManagedIdentityCredential` and token acquisition failures, it might be that you have multiple tenants, and your Azure sign-in uses a tenant that doesn't have your search service. To get your tenant ID, search the Azure portal for "tenant properties" or run `az login tenant list`.
-
-After you get your tenant ID, run `az login --tenant <YOUR-TENANT-ID>` at a command prompt, then rerun the script.
-
-## Clean up
-
-When you're working in your own subscription, it's a good idea at the end of a project to check if you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "RAG Java クイックスタートの削除"
}
```

### Explanation
このコードの変更は、`search-get-started-rag-java.md`ファイルが完全に削除されたことに関連しています。この削除には387行の内容があり、具体的には、Azure AI SearchとAzure OpenAIを使用してRAG（Retrieval-Augmented Generation）を実現するためのJava向けのクイックスタートガイドが含まれていました。クイックスタートには、前提条件の設定、役割の確認、インデックスの作成、クエリの実行、エラーハンドリング、リソースの清掃に関する詳細な手順が含まれていました。この変更は、情報の整理や更新、または新しいガイダンスへの移行の一環として行われた可能性があり、開発者にとって重要なリソースが失われるため、影響は大きいです。ユーザーは新たに用意されるかもしれない他のガイドラインや資料を参照する必要があります。

## articles/search/includes/quickstarts/search-get-started-rag-javascript.md{#item-69e5ef}

<details>
<summary>Diff</summary>
````diff
@@ -1,389 +0,0 @@
----
-manager: nitinme
-author: haileytap
-ms.author: haileytapia
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 06/05/2025
----
-## Prerequisites
-
-- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-
-- An [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource).
-  - [Choose a region](/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#global-standard-model-availability) that supports the chat completion model you want to use (gpt-4o, gpt-4o-mini, or an equivalent model).
-  - [Deploy the chat completion model](/azure/ai-foundry/how-to/deploy-models-openai) in Microsoft Foundry or [use another approach](/azure/ai-services/openai/how-to/working-with-models).
-- An [Azure AI Search resource](../../search-create-service-portal.md).
-  - We recommend using the Basic tier or higher.
-  - [Enable semantic ranking](../../semantic-how-to-enable-disable.md).
-- [Visual Studio Code](https://code.visualstudio.com/download).
-- [Node.JS with LTS](https://nodejs.org/en/download/).
-
-
-## Configure access
-
-Requests to the search endpoint must be authenticated and authorized. You can use API keys or roles for this task. Keys are easier to start with, but roles are more secure. This quickstart assumes roles.
-
-You're setting up two clients, so you need permissions on both resources.
-
-Azure AI Search is receiving the query request from your local system. Assign yourself the **Search Index Data Reader** role assignment if the hotels sample index already exists. If it doesn't exist, assign yourself **Search Service Contributor** and **Search Index Data Contributor** roles so that you can create and query the index.
-
-Azure OpenAI is receiving the query and the search results from your local system. Assign yourself the **Cognitive Services OpenAI User** role on Azure OpenAI.
-
-1. Sign in to the [Azure portal](https://portal.azure.com).
-
-1. Configure Azure AI Search for role-based access:
-
-    1. In the Azure portal, find your Azure AI Search service.
-
-    1. On the left menu, select **Settings** > **Keys**, and then select either **Role-based access control** or **Both**.
-
-1. Assign roles:
-
-    1. On the left menu, select **Access control (IAM)**.
-
-    1. On Azure AI Search, select these roles to create, load, and query a search index, and then assign them to your Microsoft Entra ID user identity:
-
-       - **Search Index Data Contributor**
-       - **Search Service Contributor**
-
-    1. On Azure OpenAI, select **Access control (IAM)** to assign this role to yourself on Azure OpenAI:
-
-       - **Cognitive Services OpenAI User**
-
-It can take several minutes for permissions to take effect.
-
-## Create an index
-
-A search index provides grounding data for the chat model. We recommend the **hotels-sample-index**.
-
-1. In the Azure portal, [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
-
-1. Follow the instructions in [this quickstart](../../search-import-data-portal.md) to create the index.
-
-1. Once the index is created, select **Search management** > **Indexes** from the left menu to open the index.
-
-1. Select **Edit JSON**. 
-
-1. Scroll to the end of the index, where you can find placeholders for constructs that can be added to an index.
-
-   ```json
-   "analyzers": [],
-   "tokenizers": [],
-   "tokenFilters": [],
-   "charFilters": [],
-   "normalizers": [],
-   ```
-
-1. On a new line after "normalizers", paste in the following semantic configuration. This example specifies a `"defaultConfiguration"`, which is important to the running of this quickstart.
-
-    ```json
-    "semantic":{
-       "defaultConfiguration":"semantic-config",
-       "configurations":[
-          {
-             "name":"semantic-config",
-             "prioritizedFields":{
-                "titleField":{
-                   "fieldName":"HotelName"
-                },
-                "prioritizedContentFields":[
-                   {
-                      "fieldName":"Description"
-                   }
-                ],
-                "prioritizedKeywordsFields":[
-                   {
-                      "fieldName":"Category"
-                   },
-                   {
-                      "fieldName":"Tags"
-                   }
-                ]
-             }
-          }
-       ]
-    },
-    ```
-
-1. **Save** your changes.
-
-1. Run the following query in [Search Explorer](../../search-explorer.md) to test your index: `complimentary breakfast`.
-
-   Output should look similar to the following example. Results that are returned directly from the search engine consist of fields and their verbatim values, along with metadata like a search score and a semantic ranking score and caption if you use semantic ranker. We used a [select statement](../../search-query-odata-select.md) to return just the HotelName, Description, and Tags fields.
-
-   ```
-   {
-   "@odata.count": 18,
-   "@search.answers": [],
-   "value": [
-      {
-         "@search.score": 2.2896252,
-         "@search.rerankerScore": 2.506816864013672,
-         "@search.captions": [
-         {
-            "text": "Head Wind Resort. Suite. coffee in lobby\r\nfree wifi\r\nview. The best of old town hospitality combined with views of the river and cool breezes off the prairie. Our penthouse suites offer views for miles and the rooftop plaza is open to all guests from sunset to 10 p.m. Enjoy a **complimentary continental breakfast** in the lobby, and free Wi-Fi throughout the hotel..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "Head Wind Resort",
-         "Description": "The best of old town hospitality combined with views of the river and cool breezes off the prairie. Our penthouse suites offer views for miles and the rooftop plaza is open to all guests from sunset to 10 p.m. Enjoy a complimentary continental breakfast in the lobby, and free Wi-Fi throughout the hotel.",
-         "Tags": [
-         "coffee in lobby",
-         "free wifi",
-         "view"
-         ]
-      },
-      {
-         "@search.score": 2.2158256,
-         "@search.rerankerScore": 2.288334846496582,
-         "@search.captions": [
-         {
-            "text": "Swan Bird Lake Inn. Budget. continental breakfast\r\nfree wifi\r\n24-hour front desk service. We serve a continental-style breakfast each morning, featuring a variety of food and drinks. Our locally made, oh-so-soft, caramel cinnamon rolls are a favorite with our guests. Other breakfast items include coffee, orange juice, milk, cereal, instant oatmeal, bagels, and muffins..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "Swan Bird Lake Inn",
-         "Description": "We serve a continental-style breakfast each morning, featuring a variety of food and drinks. Our locally made, oh-so-soft, caramel cinnamon rolls are a favorite with our guests. Other breakfast items include coffee, orange juice, milk, cereal, instant oatmeal, bagels, and muffins.",
-         "Tags": [
-         "continental breakfast",
-         "free wifi",
-         "24-hour front desk service"
-         ]
-      },
-      {
-         "@search.score": 0.92481667,
-         "@search.rerankerScore": 2.221315860748291,
-         "@search.captions": [
-         {
-            "text": "White Mountain Lodge & Suites. Resort and Spa. continental breakfast\r\npool\r\nrestaurant. Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "White Mountain Lodge & Suites",
-         "Description": "Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings.",
-         "Tags": [
-         "continental breakfast",
-         "pool",
-         "restaurant"
-         ]
-      },
-      . . .
-   ]}
-   ```
-
-## Get service endpoints
-
-In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints so that you can provide them as variables in your code.
-
-1. Sign in to the [Azure portal](https://portal.azure.com).
-
-1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
-
-1. On the **Overview** home page, copy the URL. An example endpoint might look like `https://example.search.windows.net`. 
-
-1. [Find your Azure OpenAI service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.CognitiveServices%2Faccounts).
-
-1. On the **Overview** home page, select the link to view the endpoints. Copy the URL. An example endpoint might look like `https://example.openai.azure.com/`.
-
-## Set up environment variables for local development
-
-1. Create a `.env` file.
-1. Add the following environment variables to the `.env` file, replacing the values with your own service endpoints and keys.
-
-   ```plaintext
-   AZURE_SEARCH_ENDPOINT=<YOUR AZURE AI SEARCH ENDPOINT>
-   AZURE_SEARCH_INDEX_NAME=hotels-sample-index
-
-   AZURE_OPENAI_ENDPOINT=<YOUR AZURE OPENAI ENDPOINT>
-   AZURE_OPENAI_VERSION=<YOUR AZURE OPENAI API VERSION>
-   AZURE_DEPLOYMENT_MODEL=<YOUR DEPLOYMENT NAME>
-   ```
-
-## Set up the Node.JS project
-
-Set up project with Visual Studio Code and TypeScript.
-
-1. Start Visual Studio Code in a new directory.
-
-   ```bash
-   mkdir rag-quickstart && cd rag-quickstart
-   code .
-   ```
-1. Create a new package for ESM modules in your project directory.
-
-   ```bash
-   npm init -y
-   npm pkg set type=module
-   ```
-
-   This creates a `package.json` file with default values.
-
-1. Install the following npm packages.
-
-   ```bash
-   npm install @azure/identity @azure/search-documents openai dotenv 
-   ```
-
-1. Create a `src` directory in your project directory.
-
-   ```bash
-   mkdir src
-   ```
-
-## Sign in to Azure
-
-You're using Microsoft Entra ID and role assignments for the connection. Make sure you're logged in to the same tenant and subscription as Azure AI Search and Azure OpenAI. You can use the Azure CLI on the command line to show current properties, change properties, and to sign in. For more information, see [Connect without keys](../../search-get-started-rbac.md). 
-
-Run each of the following commands in sequence.
-
-```azure-cli
-az account show
-
-az account set --subscription <PUT YOUR SUBSCRIPTION ID HERE>
-
-az login --tenant <PUT YOUR TENANT ID HERE>
-```
-
-You should now be logged in to Azure from your local device.
-
-## Set up query and chat thread
-
-Create a query script that uses the Azure AI Search index and the chat model to generate responses based on grounding data. The following steps guide you through setting up the query script.
-
-1. Create a `query.js` file in the `src` directory with the following code.
-    
-    :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-rag-js/src/query.js" :::
-
-    The preceding code does the following:
-    - Imports the necessary libraries for Azure AI Search and Azure OpenAI.
-    - Uses environment variables to configure the Azure AI Search and Azure OpenAI clients.
-    - Defines a function to get the clients for Azure AI Search and Azure OpenAI, using environment variables for configuration.
-    - Defines a function to query Azure AI Search for sources based on the user query.
-    - Defines a function to query Azure OpenAI for a response based on the user query and the sources retrieved from Azure AI Search.
-    - The `main` function orchestrates the flow by calling the search and OpenAI functions, and then prints the response.    
-     
-1. Run the following command in a terminal to execute the query script:
-
-    ```bash
-    node -r dotenv/config query.js
-    ```
-
-    The `.env` is passed into the runtime using the `-r dotenv/config`. 
-
-1. View the output, which consists of recommendations for several hotels. Here's an example of what the output might look like:
-    
-    ```
-    Sure! Here are a few hotels that offer complimentary breakfast:
-    
-    - **Head Wind Resort**
-    - Complimentary continental breakfast in the lobby
-    - Free Wi-Fi throughout the hotel
-    
-    - **Double Sanctuary Resort**
-    - Continental breakfast included
-    
-    - **White Mountain Lodge & Suites**
-    - Continental breakfast available
-    
-    - **Swan Bird Lake Inn**
-    - Continental-style breakfast each morning with a variety of food and drinks 
-        such as caramel cinnamon rolls, coffee, orange juice, milk, cereal, 
-        instant oatmeal, bagels, and muffins
-    ```
-
-## Troubleshooting
-
-If you get a **Forbidden** error message, check Azure AI Search configuration to make sure role-based access is enabled.
-
-If you get an **Authorization failed** error message, wait a few minutes and try again. It can take several minutes for role assignments to become operational.
-
-If you get a **Resource not found** error message, check the resource URIs and make sure the API version on the chat model is valid.
-
-Otherwise, to experiment further, change the query and rerun the last step to better understand how the model works with the grounding data.
-
-You can also modify the prompt to change the tone or structure of the output.
-
-You might also try the query without semantic ranking by setting `use_semantic_reranker=False` in the query parameters step. Semantic ranking can noticably improve the relevance of query results and the ability of the LLM to return useful information. Experimentation can help you decide whether it makes a difference for your content.
-
-## Send a complex RAG query
-
-Azure AI Search supports [complex types](../../search-howto-complex-data-types.md) for nested JSON structures. In the hotels-sample-index, `Address` is an example of a complex type, consisting of `Address.StreetAddress`, `Address.City`, `Address.StateProvince`, `Address.PostalCode`, and `Address.Country`. The index also has complex collection of `Rooms` for each hotel.
-
-If your index has complex types, change your prompt to include formatting instructions: 
-
-```text
-Can you recommend a few hotels that offer complimentary breakfast? 
-Tell me their description, address, tags, and the rate for one room that sleeps 4 people.
-```
-
-1. Create a new file `queryComplex.js`. 
-1. Copy the following code to the file:
-
-    :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-rag-js/src/queryComplex.js" :::
-
-
-1. Run the following command in a terminal to execute the query script:
-
-    ```bash
-    node -r dotenv/config queryComplex.js
-    ```
-
-    The `.env` is passed into the runtime using the `-r dotenv/config`. 
-
-1. View the output from Azure OpenAI, and it adds content from complex types.
-    
-    ```
-    Here are a few hotels that offer complimentary breakfast and have rooms that sleep 4 people:
-    
-    1. **Head Wind Resort**
-       - **Description:** The best of old town hospitality combined with views of the river and 
-       cool breezes off the prairie. Enjoy a complimentary continental breakfast in the lobby, 
-       and free Wi-Fi throughout the hotel.
-       - **Address:** 7633 E 63rd Pl, Tulsa, OK 74133, USA
-       - **Tags:** Coffee in lobby, free Wi-Fi, view
-       - **Room for 4:** Suite, 2 Queen Beds (Amenities) - $254.99
-    
-    2. **Double Sanctuary Resort**
-       - **Description:** 5-star Luxury Hotel - Biggest Rooms in the city. #1 Hotel in the area 
-       listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso 
-       in room. Offers continental breakfast.
-       - **Address:** 2211 Elliott Ave, Seattle, WA 98121, USA
-       - **Tags:** View, pool, restaurant, bar, continental breakfast
-       - **Room for 4:** Suite, 2 Queen Beds (Amenities) - $254.99
-    
-    3. **Swan Bird Lake Inn**
-       - **Description:** Continental-style breakfast featuring a variety of food and drinks. 
-       Locally made caramel cinnamon rolls are a favorite.
-       - **Address:** 1 Memorial Dr, Cambridge, MA 02142, USA
-       - **Tags:** Continental breakfast, free Wi-Fi, 24-hour front desk service
-       - **Room for 4:** Budget Room, 2 Queen Beds (City View) - $85.99
-    
-    4. **Gastronomic Landscape Hotel**
-       - **Description:** Known for its culinary excellence under the management of William Dough, 
-       offers continental breakfast.
-       - **Address:** 3393 Peachtree Rd, Atlanta, GA 30326, USA
-       - **Tags:** Restaurant, bar, continental breakfast
-       - **Room for 4:** Budget Room, 2 Queen Beds (Amenities) - $66.99
-    ...
-       - **Tags:** Pool, continental breakfast, free parking
-       - **Room for 4:** Budget Room, 2 Queen Beds (Amenities) - $60.99
-    
-    Enjoy your stay! Let me know if you need any more information.
-    ```
-
-## Troubleshooting errors
-
-To debug Azure SDK errors, set the environment variable `AZURE_LOG_LEVEL` to one of the following: `verbose`, `info`, `warning`, `error`. This will enable detailed logging for the Azure SDK, which can help identify [issues with authentication](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/identity/identity/TROUBLESHOOTING.md#enable-and-configure-logging), network connectivity, or other problems.
-
-Rerun the query script. You should now get informational statements from the SDKs in the output that provide more detail about any issues.
-
-If you see output messages related to ManagedIdentityCredential and token acquisition failures, it could be that you have multiple tenants, and your Azure sign-in is using a tenant that doesn't have your search service. To get your tenant ID, search the Azure portal for "tenant properties" or run `az login tenant list`.
-
-Once you have your tenant ID, run `az login --tenant <YOUR-TENANT-ID>` at a command prompt, and then rerun the script.
-
-## Clean up
-
-When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "RAG JavaScript クイックスタートの削除"
}
```

### Explanation
このコードの変更は、`search-get-started-rag-javascript.md`ファイルが完全に削除されたことに関するものです。この削除には389行の内容が含まれており、具体的には、Azure AI SearchおよびAzure OpenAIを使用したRAG（Retrieval-Augmented Generation）に関するJavaScript向けのクイックスタートガイドが含まれていました。このファイルには、前提条件、アクセスの設定、インデックスの作成、クエリの実行、エラーハンドリング、ローカル開発環境の構成など、開発者が必要とする詳細な手順が記載されていました。

この変更は、リソースの整理や更新が行われる一環として行われた可能性がありますが、ユーザーにとっては有用な情報の喪失となるため、その影響は大きいと考えられます。開発者は、今後新たに提供される可能性のあるガイドラインやドキュメントに注目する必要があります。

## articles/search/includes/quickstarts/search-get-started-rag-python.md{#item-3927ba}

<details>
<summary>Diff</summary>
````diff
@@ -1,448 +0,0 @@
----
-manager: nitinme
-author: haileytap
-ms.author: haileytapia
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 06/05/2025
----
-## Prerequisites
-
-- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-
-- An [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource).
-  - [Choose a region](/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#global-standard-model-availability) that supports the chat completion model you want to use (gpt-4o, gpt-4o-mini, or an equivalent model).
-  - [Deploy the chat completion model](/azure/ai-foundry/how-to/deploy-models-openai) in Microsoft Foundry or [use another approach](/azure/ai-services/openai/how-to/working-with-models).
-- An [Azure AI Search resource](../../search-create-service-portal.md).
-  - We recommend using the Basic tier or higher.
-  - [Enable semantic ranking](../../semantic-how-to-enable-disable.md).
-- [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and the [Jupyter package](https://pypi.org/project/jupyter/). For more information, see [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python).
-
-## Download file
-
-[Download a Jupyter notebook](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-RAG) from GitHub to send the requests in this quickstart. For more information, see [Downloading files from GitHub](https://docs.github.com/get-started/start-your-journey/downloading-files-from-github).
-
-You can also start a new file on your local system and create requests manually by using the instructions in this article.
-
-## Configure access
-
-Requests to the search endpoint must be authenticated and authorized. You can use API keys or roles for this task. Keys are easier to start with, but roles are more secure. This quickstart assumes roles.
-
-You're setting up two clients, so you need permissions on both resources.
-
-Azure AI Search is receiving the query request from your local system. Assign yourself the **Search Index Data Reader** role assignment if the hotels sample index already exists. If it doesn't exist, assign yourself **Search Service Contributor** and **Search Index Data Contributor** roles so that you can create and query the index.
-
-Azure OpenAI is receiving the query and the search results from your local system. Assign yourself the **Cognitive Services OpenAI User** role on Azure OpenAI.
-
-1. Sign in to the [Azure portal](https://portal.azure.com).
-
-1. Configure Azure AI Search for role-based access:
-
-    1. In the Azure portal, find your Azure AI Search service.
-
-    1. On the left menu, select **Settings** > **Keys**, and then select either **Role-based access control** or **Both**.
-
-1. Assign roles:
-
-    1. On the left menu, select **Access control (IAM)**.
-
-    1. On Azure AI Search, select these roles to create, load, and query a search index, and then assign them to your Microsoft Entra ID user identity:
-
-       - **Search Index Data Contributor**
-       - **Search Service Contributor**
-
-    1. On Azure OpenAI, select **Access control (IAM)** to assign this role to yourself on Azure OpenAI:
-
-       - **Cognitive Services OpenAI User**
-
-It can take several minutes for permissions to take effect.
-
-## Update the hotels-sample-index
-
-A search index provides grounding data for the chat model. We recommend the **hotels-sample-index**.
-
-1. In the Azure portal, [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
-
-1. Follow the instructions in [this quickstart](../../search-import-data-portal.md) to create the index.
-
-1. Once the index is created, select **Search management** > **Indexes** from the left menu to open the index.
-
-1. Select **Edit JSON**. 
-
-1. Scroll to the end of the index, where you can find placeholders for constructs that can be added to an index.
-
-   ```json
-   "analyzers": [],
-   "tokenizers": [],
-   "tokenFilters": [],
-   "charFilters": [],
-   "normalizers": [],
-   ```
-
-1. On a new line after "normalizers", paste in the following semantic configuration. This example specifies a `"defaultConfiguration"`, which is important to the running of this quickstart.
-
-    ```json
-    "semantic":{
-       "defaultConfiguration":"semantic-config",
-       "configurations":[
-          {
-             "name":"semantic-config",
-             "prioritizedFields":{
-                "titleField":{
-                   "fieldName":"HotelName"
-                },
-                "prioritizedContentFields":[
-                   {
-                      "fieldName":"Description"
-                   }
-                ],
-                "prioritizedKeywordsFields":[
-                   {
-                      "fieldName":"Category"
-                   },
-                   {
-                      "fieldName":"Tags"
-                   }
-                ]
-             }
-          }
-       ]
-    },
-    ```
-
-1. **Save** your changes.
-
-1. Run the following query in [Search Explorer](../../search-explorer.md) to test your index: `complimentary breakfast`.
-
-   Output should look similar to the following example. Results that are returned directly from the search engine consist of fields and their verbatim values, along with metadata like a search score and a semantic ranking score and caption if you use semantic ranker. We used a [select statement](../../search-query-odata-select.md) to return just the HotelName, Description, and Tags fields.
-
-   ```
-   {
-   "@odata.count": 18,
-   "@search.answers": [],
-   "value": [
-      {
-         "@search.score": 2.2896252,
-         "@search.rerankerScore": 2.506816864013672,
-         "@search.captions": [
-         {
-            "text": "Head Wind Resort. Suite. coffee in lobby\r\nfree wifi\r\nview. The best of old town hospitality combined with views of the river and cool breezes off the prairie. Our penthouse suites offer views for miles and the rooftop plaza is open to all guests from sunset to 10 p.m. Enjoy a **complimentary continental breakfast** in the lobby, and free Wi-Fi throughout the hotel..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "Head Wind Resort",
-         "Description": "The best of old town hospitality combined with views of the river and cool breezes off the prairie. Our penthouse suites offer views for miles and the rooftop plaza is open to all guests from sunset to 10 p.m. Enjoy a complimentary continental breakfast in the lobby, and free Wi-Fi throughout the hotel.",
-         "Tags": [
-         "coffee in lobby",
-         "free wifi",
-         "view"
-         ]
-      },
-      {
-         "@search.score": 2.2158256,
-         "@search.rerankerScore": 2.288334846496582,
-         "@search.captions": [
-         {
-            "text": "Swan Bird Lake Inn. Budget. continental breakfast\r\nfree wifi\r\n24-hour front desk service. We serve a continental-style breakfast each morning, featuring a variety of food and drinks. Our locally made, oh-so-soft, caramel cinnamon rolls are a favorite with our guests. Other breakfast items include coffee, orange juice, milk, cereal, instant oatmeal, bagels, and muffins..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "Swan Bird Lake Inn",
-         "Description": "We serve a continental-style breakfast each morning, featuring a variety of food and drinks. Our locally made, oh-so-soft, caramel cinnamon rolls are a favorite with our guests. Other breakfast items include coffee, orange juice, milk, cereal, instant oatmeal, bagels, and muffins.",
-         "Tags": [
-         "continental breakfast",
-         "free wifi",
-         "24-hour front desk service"
-         ]
-      },
-      {
-         "@search.score": 0.92481667,
-         "@search.rerankerScore": 2.221315860748291,
-         "@search.captions": [
-         {
-            "text": "White Mountain Lodge & Suites. Resort and Spa. continental breakfast\r\npool\r\nrestaurant. Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "White Mountain Lodge & Suites",
-         "Description": "Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings.",
-         "Tags": [
-         "continental breakfast",
-         "pool",
-         "restaurant"
-         ]
-      },
-      . . .
-   ]}
-   ```
-
-## Get service endpoints
-
-In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints so that you can provide them as variables in your code.
-
-1. Sign in to the [Azure portal](https://portal.azure.com).
-
-1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
-
-1. On the **Overview** home page, copy the URL. An example endpoint might look like `https://example.search.windows.net`. 
-
-1. [Find your Azure OpenAI service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.CognitiveServices%2Faccounts).
-
-1. On the **Overview** home page, select the link to view the endpoints. Copy the URL. An example endpoint might look like `https://example.openai.azure.com/`.
-
-## Create a virtual environment
-
-In this step, switch back to your local system and Visual Studio Code. We recommend that you create a virtual environment so that you can install the dependencies in isolation.
-
-1. In Visual Studio Code, open the folder containing Quickstart-RAG.ipynb.
-
-1. Press Ctrl-shift-P to open the command palette, search for "Python: Create Environment", and then select `Venv` to create a virtual environment in the current workspace.
-
-1. Select Quickstart-RAG\requirements.txt for the dependencies.
-
-It takes several minutes to create the environment. When the environment is ready, continue to the next step.
-
-## Sign in to Azure
-
-You're using Microsoft Entra ID and role assignments for the connection. Make sure you're logged in to the same tenant and subscription as Azure AI Search and Azure OpenAI. You can use the Azure CLI on the command line to show current properties, change properties, and to sign in. For more information, see [Connect without keys](../../search-get-started-rbac.md). 
-
-Run each of the following commands in sequence.
-
-```azure-cli
-az account show
-
-az account set --subscription <PUT YOUR SUBSCRIPTION ID HERE>
-
-az login --tenant <PUT YOUR TENANT ID HERE>
-```
-
-You should now be logged in to Azure from your local device.
-
-## Set up the query and chat thread
-
-This section uses Visual Studio Code and Python to call the chat completion APIs on Azure OpenAI.
-
-1. Start Visual Studio Code and [open the .ipynb file](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-RAG) or create a new Python file.
-
-1. Install the following Python packages.
-
-   ```python
-   ! pip install azure-search-documents==11.6.0b5 --quiet
-   ! pip install azure-identity==1.16.1 --quiet
-   ! pip install openai --quiet
-   ! pip install aiohttp --quiet
-   ! pip install ipykernel --quiet
-   ```
-
-1. Set the following variables, substituting placeholders with the endpoints you collected in the previous step. 
-
-   ```python
-    AZURE_SEARCH_SERVICE: str = "PUT YOUR SEARCH SERVICE ENDPOINT HERE"
-    AZURE_OPENAI_ACCOUNT: str = "PUT YOUR AZURE OPENAI ENDPOINT HERE"
-    AZURE_DEPLOYMENT_MODEL: str = "gpt-4o"
-   ```
-
-1. Set up clients, the prompt, query, and response.
-
-   For the Azure Government cloud, modify the API endpoint on the token provider to `"https://cognitiveservices.azure.us/.default"`.
-
-   ```python
-   # Set up the query for generating responses
-    from azure.identity import DefaultAzureCredential
-    from azure.identity import get_bearer_token_provider
-    from azure.search.documents import SearchClient
-    from openai import AzureOpenAI
-    
-    credential = DefaultAzureCredential()
-    token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")
-    openai_client = AzureOpenAI(
-        api_version="2024-06-01",
-        azure_endpoint=AZURE_OPENAI_ACCOUNT,
-        azure_ad_token_provider=token_provider
-    )
-    
-    search_client = SearchClient(
-        endpoint=AZURE_SEARCH_SERVICE,
-        index_name="hotels-sample-index",
-        credential=credential
-    )
-    
-    # This prompt provides instructions to the model
-    GROUNDED_PROMPT="""
-    You are a friendly assistant that recommends hotels based on activities and amenities.
-    Answer the query using only the sources provided below in a friendly and concise bulleted manner.
-    Answer ONLY with the facts listed in the list of sources below.
-    If there isn't enough information below, say you don't know.
-    Do not generate answers that don't use the sources below.
-    Query: {query}
-    Sources:\n{sources}
-    """
-    
-    # Query is the question being asked. It's sent to the search engine and the chat model
-    query="Can you recommend a few hotels with complimentary breakfast?"
-    
-    # Search results are created by the search client
-    # Search results are composed of the top 5 results and the fields selected from the search index
-    # Search results include the top 5 matches to your query
-    search_results = search_client.search(
-        search_text=query,
-        top=5,
-        select="Description,HotelName,Tags"
-    )
-    sources_formatted = "\n".join([f'{document["HotelName"]}:{document["Description"]}:{document["Tags"]}' for document in search_results])
-    
-    # Send the search results and the query to the LLM to generate a response based on the prompt.
-    response = openai_client.chat.completions.create(
-        messages=[
-            {
-                "role": "user",
-                "content": GROUNDED_PROMPT.format(query=query, sources=sources_formatted)
-            }
-        ],
-        model=AZURE_DEPLOYMENT_MODEL
-    )
-    
-    # Here is the response from the chat model.
-    print(response.choices[0].message.content)
-    ```
-
-    Output is from Azure OpenAI, and it consists of recommendations for several hotels. Here's an example of what the output might look like:
-
-    ```
-   Sure! Here are a few hotels that offer complimentary breakfast:
-   
-   - **Head Wind Resort**
-   - Complimentary continental breakfast in the lobby
-   - Free Wi-Fi throughout the hotel
-   
-   - **Double Sanctuary Resort**
-   - Continental breakfast included
-   
-   - **White Mountain Lodge & Suites**
-   - Continental breakfast available
-   
-   - **Swan Bird Lake Inn**
-   - Continental-style breakfast each morning with a variety of food and drinks 
-     such as caramel cinnamon rolls, coffee, orange juice, milk, cereal, 
-     instant oatmeal, bagels, and muffins
-    ```
-
-    If you get a **Forbidden** error message, check Azure AI Search configuration to make sure role-based access is enabled.
-
-    If you get an **Authorization failed** error message, wait a few minutes and try again. It can take several minutes for role assignments to become operational.
-
-    If you get a **Resource not found** error message, check the resource URIs and make sure the API version on the chat model is valid.
-
-    Otherwise, to experiment further, change the query and rerun the last step to better understand how the model works with the grounding data.
-
-    You can also modify the prompt to change the tone or structure of the output.
-
-    You might also try the query without semantic ranking by setting `use_semantic_reranker=False` in the query parameters step. Semantic ranking can noticably improve the relevance of query results and the ability of the LLM to return useful information. Experimentation can help you decide whether it makes a difference for your content.
-
-## Send a complex RAG query
-
-Azure AI Search supports [complex types](../../search-howto-complex-data-types.md) for nested JSON structures. In the hotels-sample-index, `Address` is an example of a complex type, consisting of `Address.StreetAddress`, `Address.City`, `Address.StateProvince`, `Address.PostalCode`, and `Address.Country`. The index also has complex collection of `Rooms` for each hotel.
-
-If your index has complex types, your query can provide those fields if you first convert the search results output to JSON, and then pass the JSON to the chat model. The following example adds complex types to the request. The formatting instructions include a JSON specification.
-
-```python
-import json
-
-# Query is the question being asked. It's sent to the search engine and the LLM.
-query="Can you recommend a few hotels that offer complimentary breakfast? 
-Tell me their description, address, tags, and the rate for one room that sleeps 4 people."
-
-# Set up the search results and the chat thread.
-# Retrieve the selected fields from the search index related to the question.
-selected_fields = ["HotelName","Description","Address","Rooms","Tags"]
-search_results = search_client.search(
-    search_text=query,
-    top=5,
-    select=selected_fields,
-    query_type="semantic"
-)
-sources_filtered = [{field: result[field] for field in selected_fields} for result in search_results]
-sources_formatted = "\n".join([json.dumps(source) for source in sources_filtered])
-
-response = openai_client.chat.completions.create(
-    messages=[
-        {
-            "role": "user",
-            "content": GROUNDED_PROMPT.format(query=query, sources=sources_formatted)
-        }
-    ],
-    model=AZURE_DEPLOYMENT_MODEL
-)
-
-print(response.choices[0].message.content)
-```
-
-Output is from Azure OpenAI, and it adds content from complex types.
-
-```
-Here are a few hotels that offer complimentary breakfast and have rooms that sleep 4 people:
-
-1. **Head Wind Resort**
-   - **Description:** The best of old town hospitality combined with views of the river and 
-   cool breezes off the prairie. Enjoy a complimentary continental breakfast in the lobby, 
-   and free Wi-Fi throughout the hotel.
-   - **Address:** 7633 E 63rd Pl, Tulsa, OK 74133, USA
-   - **Tags:** Coffee in lobby, free Wi-Fi, view
-   - **Room for 4:** Suite, 2 Queen Beds (Amenities) - $254.99
-
-2. **Double Sanctuary Resort**
-   - **Description:** 5-star Luxury Hotel - Biggest Rooms in the city. #1 Hotel in the area 
-   listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso 
-   in room. Offers continental breakfast.
-   - **Address:** 2211 Elliott Ave, Seattle, WA 98121, USA
-   - **Tags:** View, pool, restaurant, bar, continental breakfast
-   - **Room for 4:** Suite, 2 Queen Beds (Amenities) - $254.99
-
-3. **Swan Bird Lake Inn**
-   - **Description:** Continental-style breakfast featuring a variety of food and drinks. 
-   Locally made caramel cinnamon rolls are a favorite.
-   - **Address:** 1 Memorial Dr, Cambridge, MA 02142, USA
-   - **Tags:** Continental breakfast, free Wi-Fi, 24-hour front desk service
-   - **Room for 4:** Budget Room, 2 Queen Beds (City View) - $85.99
-
-4. **Gastronomic Landscape Hotel**
-   - **Description:** Known for its culinary excellence under the management of William Dough, 
-   offers continental breakfast.
-   - **Address:** 3393 Peachtree Rd, Atlanta, GA 30326, USA
-   - **Tags:** Restaurant, bar, continental breakfast
-   - **Room for 4:** Budget Room, 2 Queen Beds (Amenities) - $66.99
-...
-   - **Tags:** Pool, continental breakfast, free parking
-   - **Room for 4:** Budget Room, 2 Queen Beds (Amenities) - $60.99
-
-Enjoy your stay! Let me know if you need any more information.
-```
-
-## Troubleshooting errors
-
-To debug authentication errors, insert the following code before the step that calls the search engine and the LLM.
-
-```python
-import sys
-import logging # Set the logging level for all azure-storage-* libraries
-logger = logging.getLogger('azure.identity') 
-logger.setLevel(logging.DEBUG)
-
-handler = logging.StreamHandler(stream=sys.stdout)
-formatter = logging.Formatter('[%(levelname)s %(name)s] %(message)s')
-handler.setFormatter(formatter)
-logger.addHandler(handler)
-```
-
-Rerun the query script. You should now get INFO and DEBUG statements in the output that provide more detail about the issue.
-
-If you see output messages related to ManagedIdentityCredential and token acquisition failures, it could be that you have multiple tenants, and your Azure sign-in is using a tenant that doesn't have your search service. To get your tenant ID, search the Azure portal for "tenant properties" or run `az login tenant list`.
-
-Once you have your tenant ID, run `az login --tenant <YOUR-TENANT-ID>` at a command prompt, and then rerun the script.
-
-## Clean up
-
-When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "RAG Python クイックスタートの削除"
}
```

### Explanation
このコードの変更は、`search-get-started-rag-python.md`ファイルが完全に削除されたことに関するものです。この変更により、448行の内容が削除され、具体的にはAzure AI SearchおよびAzure OpenAIを使用したRAG（Retrieval-Augmented Generation）に関するPython向けのクイックスタートガイドが含まれていました。このファイルには、クイックスタートに必要な前提条件、APIへのアクセス設定、ホテルトラッキング用インデックスの作成、クエリの設定や実行、エラーハンドリング、ローカル開発環境の構成手順が詳細に記載されていました。

この変更は、主にリソースの更新や整理の一環として行われたと考えられますが、ユーザーにとっては有用な情報が失われることになるため、大きな影響を与える可能性があります。開発者は、今後別の文書で提供されるガイドラインや情報に注目する必要があります。

## articles/search/includes/quickstarts/search-get-started-rag-rest.md{#item-aa7f2b}

<details>
<summary>Diff</summary>
````diff
@@ -1,266 +0,0 @@
----
-manager: nitinme
-author: heidisteen
-ms.author: haileytapia
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 08/27/2025
----
-
-## Prerequisites
-
-- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-
-- An [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource).
-  - [Choose a region](/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#global-standard-model-availability) that supports the chat completion model you want to use (gpt-4o, gpt-4o-mini, or an equivalent model).
-  - [Deploy the chat completion model](/azure/ai-foundry/how-to/deploy-models-openai) in Microsoft Foundry or [use another approach](/azure/ai-services/openai/how-to/working-with-models).
-- An [Azure AI Search resource](../../search-create-service-portal.md).
-  - We recommend using the Basic tier or higher.
-  - [Enable semantic ranking](../../semantic-how-to-enable-disable.md).
-
-- A [new or existing index](../../search-how-to-create-search-index.md) with descriptive or verbose text fields, attributed as retrievable in your index. This quickstart assumes the [hotels-sample-index](../../search-get-started-portal.md).
-
-- The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
-
-- [Visual Studio Code](https://code.visualstudio.com/download) with the [REST client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) .
-
-## Download file
-
-[Download a .rest file](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-RAG) from GitHub to send the requests in this quickstart. For more information, see [Downloading files from GitHub](https://docs.github.com/get-started/start-your-journey/downloading-files-from-github).
-
-You can also start a new file on your local system and create requests manually by using the instructions in this article.
-
-## Configure access
-
-Requests to the search endpoint must be authenticated and authorized. You can use [API keys](../../search-security-api-keys.md) or roles for this task. Keys are easier to start with, but roles are more secure. This quickstart assumes roles.
-
-You're setting up two clients, so you need permissions on both resources.
-
-Azure AI Search is receiving the query request from your local system. Assign yourself the **Search Index Data Reader** role assignment if the hotels sample index already exists. If it doesn't exist, assign yourself **Search Service Contributor** and **Search Index Data Contributor** roles so that you can create and query the index.
-
-Azure OpenAI is receiving the query and the search results from your local system. Assign yourself the **Cognitive Services OpenAI User** role on Azure OpenAI.
-
-1. Sign in to the [Azure portal](https://portal.azure.com).
-
-1. Configure Azure AI Search for role-based access:
-
-    1. In the Azure portal, find your Azure AI Search service.
-
-    1. On the left menu, select **Settings** > **Keys**, and then select either **Role-based access control** or **Both**.
-
-1. Assign roles:
-
-    1. On the left menu, select **Access control (IAM)**.
-
-    1. On Azure AI Search, select these roles to create, load, and query a search index, and then assign them to your Microsoft Entra ID user identity:
-
-       - **Search Index Data Contributor**
-       - **Search Service Contributor**
-
-    1. On Azure OpenAI, select **Access control (IAM)** to assign this role to yourself on Azure OpenAI:
-
-       - **Cognitive Services OpenAI User**
-
-It can take several minutes for permissions to take effect.
-
-## Get service endpoints and tokens
-
-In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints and tokens so that you can provide them as variables in your code.
-
-1. Sign in to the [Azure portal](https://portal.azure.com).
-
-1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
-
-1. On the **Overview** home page, copy the URL. An example endpoint might look like `https://example.search.windows.net`. 
-
-1. [Find your Azure OpenAI service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.CognitiveServices%2Faccounts).
-
-1. On the **Overview** home page, select the link to view the endpoints. Copy the URL. An example endpoint might look like `https://example.openai.azure.com/`.
-
-1. Get personal access tokens from the Azure CLI on a command prompt. Here are the commands for each resource:
-
-   - `az account get-access-token --resource https://search.azure.com --query "accessToken" -o tsv`
-   - `az account get-access-token --resource https://cognitiveservices.azure.com --query "accessToken" -o tsv`
-
-## Set up the client
-
-In this quickstart, you use a REST client and the [Azure AI Search REST APIs](/rest/api/searchservice) to implement the RAG pattern.
-
-We recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for this quickstart.
-
-> [!TIP]
-> You can download the [source code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-rag) to start with a finished project or follow these steps to create your own. 
-
-1. Start Visual Studio Code and open the [quickstart-rag.rest](https://github.com/Azure-Samples/azure-search-rest-samples/blob/main/Quickstart-RAG/rag.rest) file or create a new file.
-
-1. At the top, set environment variables for your search service, authorization, and index name.
-
-   - For @searchUrl, paste in the search endpoint.
-   - For @aoaiUrl, paste in the Azure OpenAI endpoint.
-   - For @searchAccessToken, paste in the access token scoped to `https://search.azure.com`.
-   - For @aoaiAccessToken, paste in the access token scoped to `https://cognitiveservices.azure.com`.
-
-1. To test the connection, send your first request.
-
-   ```http
-   ### List existing indexes by name (verify the connection)
-    GET  {{searchUrl}}/indexes?api-version=2025-11-01-preview&$select=name  HTTP/1.1
-    Authorization: Bearer {{personalAccessToken}}
-   ```
-
-1. Select **Send Request**.
-
-   :::image type="content" source="../../media/search-get-started-semantic/visual-studio-code-send-request.png" alt-text="Screenshot of the REST client send request link.":::
-
-1. Output for this GET request should be a list of indexes. You should see the **hotels-sample-index** among them.
-
-## Set up the query and chat thread
-
-This section uses Visual Studio Code and REST to call the chat completion APIs on Azure OpenAI.
-
-1. Set up a query request on the phrase *"Can you recommend a few hotels with complimentary breakfast?"*. This query uses semantic ranking to return relevant matches, even if the verbatim text isn't an exact match. Results are held in the **searchRequest** variable for reuse on the next request.
-
-   ```http
-   # @name searchRequest
-    POST {{searchUrl}}/indexes/{{index-name}}/docs/search?api-version={{api-version}} HTTP/1.1
-    Content-Type: application/json
-    Authorization: Bearer {{searchAccessToken}}
-    
-    {
-      "search": "Can you recommend a few hotels with complimentary breakfast?",
-      "queryType": "semantic",
-      "semanticConfiguration": "semantic-config",
-      "select": "Description,HotelName,Tags",
-      "top": 5
-    }
-    
-    ### 3 - Use search results in Azure OpenAI call to a chat completion model
-    POST {{aoaiUrl}}/openai/deployments/{{aoaiGptDeployment}}/chat/completions?api-version=2024-08-01-preview HTTP/1.1
-    Content-Type: application/json
-    Authorization: Bearer {{aoaiAccessToken}}
-    
-    {
-      "messages": [
-        {
-          "role": "system", 
-          "content": "You recommend hotels based on activities and amenities. Answer the query using only the search result. Answer in a friendly and concise manner. Answer ONLY with the facts provided. If there isn't enough information below, say you don't know."
-        },
-        {
-          "role": "user",
-          "content": "Based on the hotel search results, can you recommend hotels with breakfast? Here are all the hotels I found:\n\nHotel 1: {{searchRequest.response.body.value[0].HotelName}}\nDescription: {{searchRequest.response.body.value[0].Description}}\n\nHotel 2: {{searchRequest.response.body.value[1].HotelName}}\nDescription: {{searchRequest.response.body.value[1].Description}}\n\nHotel 3: {{searchRequest.response.body.value[2].HotelName}}\nDescription: {{searchRequest.response.body.value[2].Description}}\n\nHotel 4: {{searchRequest.response.body.value[3].HotelName}}\nDescription: {{searchRequest.response.body.value[3].Description}}\n\nHotel 5: {{searchRequest.response.body.value[4].HotelName}}\nDescription: {{searchRequest.response.body.value[4].Description}}\n\nPlease recommend which hotels offer breakfast based on their descriptions."
-        }
-      ],
-      "max_tokens": 1000,
-      "temperature": 0.7
-    }`
-    ```
-
-1. **Send** the request.
-
-1. Output should look similar to the following example:
-
-   ```json
-      "value": [
-        {
-          "@search.score": 3.9269178,
-          "@search.rerankerScore": 2.380699872970581,
-          "HotelName": "Head Wind Resort",
-          "Description": "The best of old town hospitality combined with views of the river and cool breezes off the prairie. Our penthouse suites offer views for miles and the rooftop plaza is open to all guests from sunset to 10 p.m. Enjoy a complimentary continental breakfast in the lobby, and free Wi-Fi throughout the hotel.",
-          "Tags": [
-            "coffee in lobby",
-            "free wifi",
-            "view"
-          ]
-        },
-        {
-          "@search.score": 1.5450059,
-          "@search.rerankerScore": 2.1258809566497803,
-          "HotelName": "Thunderbird Motel",
-          "Description": "Book Now & Save. Clean, Comfortable rooms at the lowest price. Enjoy complimentary coffee and tea in common areas.",
-          "Tags": [
-            "coffee in lobby",
-            "free parking",
-            "free wifi"
-          ]
-        },
-        {
-          "@search.score": 2.2158256,
-          "@search.rerankerScore": 2.121671438217163,
-          "HotelName": "Swan Bird Lake Inn",
-          "Description": "We serve a continental-style breakfast each morning, featuring a variety of food and drinks. Our locally made, oh-so-soft, caramel cinnamon rolls are a favorite with our guests. Other breakfast items include coffee, orange juice, milk, cereal, instant oatmeal, bagels, and muffins.",
-          "Tags": [
-            "continental breakfast",
-            "free wifi",
-            "24-hour front desk service"
-          ]
-        },
-        {
-          "@search.score": 0.6395861,
-          "@search.rerankerScore": 2.116753339767456,
-          "HotelName": "Waterfront Scottish Inn",
-          "Description": "Newly Redesigned Rooms & airport shuttle. Minutes from the airport, enjoy lakeside amenities, a resort-style pool & stylish new guestrooms with Internet TVs.",
-          "Tags": [
-            "24-hour front desk service",
-            "continental breakfast",
-            "free wifi"
-          ]
-        },
-        {
-          "@search.score": 4.885111,
-          "@search.rerankerScore": 2.0008862018585205,
-          "HotelName": "Double Sanctuary Resort",
-          "Description": "5 star Luxury Hotel - Biggest Rooms in the city. #1 Hotel in the area listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso in room.",
-          "Tags": [
-            "view",
-            "pool",
-            "restaurant",
-            "bar",
-            "continental breakfast"
-          ]
-        }
-      ]
-    ```
-
-1. Set up a conversation turn with a chat completion model. This request includes a prompt that provides instructions for the response. The `max_tokens` value is large enough to accommodate the search results from the previous query.
-
-   ```http
-    POST {{aoaiUrl}}/openai/deployments/{{aoaiGptDeployment}}/chat/completions?api-version=2024-08-01-preview HTTP/1.1
-    Content-Type: application/json
-    Authorization: Bearer {{aoaiAccessToken}}
-    
-    {
-    "messages": [
-    {
-      "role": "system", 
-      "content": "You  are a friendly assistant that recommends hotels based on activities and amenities. Answer the query using only the search result. Answer in a friendly and concise manner. Answer ONLY with the facts provided. If there isn't enough information below, say you don't know."
-        },
-    {
-      "role": "user",
-      "content": "Based on the hotel search results, can you recommend hotels with breakfast? Here are all the hotels I found:\n\nHotel 1: {{searchRequest.response.body.value[0].HotelName}}\nDescription: {{searchRequest.response.body.value[0].Description}}\n\nHotel 2: {{searchRequest.response.body.value[1].HotelName}}\nDescription: {{searchRequest.response.body.value[1].Description}}\n\nHotel 3: {{searchRequest.response.body.value[2].HotelName}}\nDescription: {{searchRequest.response.body.value[2].Description}}\n\nHotel 4: {{searchRequest.response.body.value[3].HotelName}}\nDescription: {{searchRequest.response.body.value[3].Description}}\n\nHotel 5: {{searchRequest.response.body.value[4].HotelName}}\nDescription: {{searchRequest.response.body.value[4].Description}}\n\nPlease recommend which hotels offer breakfast based on their descriptions."
-    }
-    ],
-    "max_tokens": 1000,
-    "temperature": 0.7
-    }
-    ```
-
-1. **Send** the request.
-
-1. Output should be an HTTP 200 Success status message. Included in the output is content that answers the question:
-
-   ```json
-    "message": {
-      "annotations": [],
-      "content": "I recommend the following hotels that offer breakfast:\n\n1. **Head Wind Resort** - Offers a complimentary continental breakfast in the lobby.\n2. **Swan Bird Lake Inn** - Serves a continental-style breakfast each morning, including a variety of food and drinks. \n\nEnjoy your stay!",
-      "refusal": null,
-      "role": "assistant"
-    }
-    ```
-
-Notice that the output is missing several hotels that mention breakfast in the Tags field. The Tags field is an array, and including this field breaks the JSON structure in the results. Because there are no string conversion capabilities in the REST client, extra code for manually converting the JSON to a string is required if arrays are to be included. We omit this step for this quickstart.
-
-## Clean up
-
-When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "RAG REST クイックスタートの削除"
}
```

### Explanation
このコードの変更は、`search-get-started-rag-rest.md`ファイルが完全に削除されたことに関するものです。この変更により、266行の内容が削除され、具体的にはAzure AI SearchおよびAzure OpenAIを使用したRAG（Retrieval-Augmented Generation）に関するREST API向けのクイックスタートガイドが含まれていました。このファイルには、前提条件、APIエンドポイントやトークンの取得方法、クライアントの設定、検索リクエストの構成、結果の利用方法、エラーハンドリング、リソース管理などが詳細に記載されていました。

この変更は、ドキュメントの整理や更新の一環として行われた可能性がありますが、開発者やユーザーにとってはこれらの情報の喪失が大きな影響を及ぼす可能性があります。今後新たに提供されるドキュメントやガイドラインに注目する必要があります。

## articles/search/includes/quickstarts/search-get-started-rag-typescript.md{#item-11994e}

<details>
<summary>Diff</summary>
````diff
@@ -1,441 +0,0 @@
----
-manager: nitinme
-author: haileytap
-ms.author: haileytapia
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 06/05/2025
----
-## Prerequisites
-
-- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-
-- An [Azure AI Search service](../../search-create-service-portal.md), any tier and region.
-
-- An [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource).
-  - [Choose a region](/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#global-standard-model-availability) that supports the chat completion model you want to use (gpt-4o, gpt-4o-mini, or an equivalent model).
-  - [Deploy the chat completion model](/azure/ai-foundry/how-to/deploy-models-openai) in Microsoft Foundry or [use another approach](/azure/ai-services/openai/how-to/working-with-models).
-- An [Azure AI Search resource](../../search-create-service-portal.md).
-  - We recommend using the Basic tier or higher.
-  - [Enable semantic ranking](../../semantic-how-to-enable-disable.md).
-- [Visual Studio Code](https://code.visualstudio.com/download).
-- [Node.JS with LTS](https://nodejs.org/en/download/).
-- [TypeScript](https://www.typescriptlang.org/download). You can globally install TypeScript using npm:
-
-   ```bash
-   npm install -g typescript
-   ```
-
-
-## Configure access
-
-Requests to the search endpoint must be authenticated and authorized. You can use API keys or roles for this task. Keys are easier to start with, but roles are more secure. This quickstart assumes roles.
-
-You're setting up two clients, so you need permissions on both resources.
-
-Azure AI Search is receiving the query request from your local system. Assign yourself the **Search Index Data Reader** role assignment if the hotels sample index already exists. If it doesn't exist, assign yourself **Search Service Contributor** and **Search Index Data Contributor** roles so that you can create and query the index.
-
-Azure OpenAI is receiving the query and the search results from your local system. Assign yourself the **Cognitive Services OpenAI User** role on Azure OpenAI.
-
-1. Sign in to the [Azure portal](https://portal.azure.com).
-
-1. Configure Azure AI Search for role-based access:
-
-    1. In the Azure portal, find your Azure AI Search service.
-
-    1. On the left menu, select **Settings** > **Keys**, and then select either **Role-based access control** or **Both**.
-
-1. Assign roles:
-
-    1. On the left menu, select **Access control (IAM)**.
-
-    1. On Azure AI Search, select these roles to create, load, and query a search index, and then assign them to your Microsoft Entra ID user identity:
-
-       - **Search Index Data Contributor**
-       - **Search Service Contributor**
-
-    1. On Azure OpenAI, select **Access control (IAM)** to assign this role to yourself on Azure OpenAI:
-
-       - **Cognitive Services OpenAI User**
-
-It can take several minutes for permissions to take effect.
-
-## Create an index
-
-A search index provides grounding data for the chat model. We recommend the **hotels-sample-index**.
-
-1. In the Azure portal, [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
-
-1. Follow the instructions in [this quickstart](../../search-import-data-portal.md) to create the index.
-
-1. Once the index is created, select **Search management** > **Indexes** from the left menu to open the index.
-
-1. Select **Edit JSON**. 
-
-1. Scroll to the end of the index, where you can find placeholders for constructs that can be added to an index.
-
-   ```json
-   "analyzers": [],
-   "tokenizers": [],
-   "tokenFilters": [],
-   "charFilters": [],
-   "normalizers": [],
-   ```
-
-1. On a new line after "normalizers", paste in the following semantic configuration. This example specifies a `"defaultConfiguration"`, which is important to the running of this quickstart.
-
-    ```json
-    "semantic":{
-       "defaultConfiguration":"semantic-config",
-       "configurations":[
-          {
-             "name":"semantic-config",
-             "prioritizedFields":{
-                "titleField":{
-                   "fieldName":"HotelName"
-                },
-                "prioritizedContentFields":[
-                   {
-                      "fieldName":"Description"
-                   }
-                ],
-                "prioritizedKeywordsFields":[
-                   {
-                      "fieldName":"Category"
-                   },
-                   {
-                      "fieldName":"Tags"
-                   }
-                ]
-             }
-          }
-       ]
-    },
-    ```
-
-1. **Save** your changes.
-
-1. Run the following query in [Search Explorer](../../search-explorer.md) to test your index: `complimentary breakfast`.
-
-   Output should look similar to the following example. Results that are returned directly from the search engine consist of fields and their verbatim values, along with metadata like a search score and a semantic ranking score and caption if you use semantic ranker. We used a [select statement](../../search-query-odata-select.md) to return just the HotelName, Description, and Tags fields.
-
-   ```
-   {
-   "@odata.count": 18,
-   "@search.answers": [],
-   "value": [
-      {
-         "@search.score": 2.2896252,
-         "@search.rerankerScore": 2.506816864013672,
-         "@search.captions": [
-         {
-            "text": "Head Wind Resort. Suite. coffee in lobby\r\nfree wifi\r\nview. The best of old town hospitality combined with views of the river and cool breezes off the prairie. Our penthouse suites offer views for miles and the rooftop plaza is open to all guests from sunset to 10 p.m. Enjoy a **complimentary continental breakfast** in the lobby, and free Wi-Fi throughout the hotel..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "Head Wind Resort",
-         "Description": "The best of old town hospitality combined with views of the river and cool breezes off the prairie. Our penthouse suites offer views for miles and the rooftop plaza is open to all guests from sunset to 10 p.m. Enjoy a complimentary continental breakfast in the lobby, and free Wi-Fi throughout the hotel.",
-         "Tags": [
-         "coffee in lobby",
-         "free wifi",
-         "view"
-         ]
-      },
-      {
-         "@search.score": 2.2158256,
-         "@search.rerankerScore": 2.288334846496582,
-         "@search.captions": [
-         {
-            "text": "Swan Bird Lake Inn. Budget. continental breakfast\r\nfree wifi\r\n24-hour front desk service. We serve a continental-style breakfast each morning, featuring a variety of food and drinks. Our locally made, oh-so-soft, caramel cinnamon rolls are a favorite with our guests. Other breakfast items include coffee, orange juice, milk, cereal, instant oatmeal, bagels, and muffins..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "Swan Bird Lake Inn",
-         "Description": "We serve a continental-style breakfast each morning, featuring a variety of food and drinks. Our locally made, oh-so-soft, caramel cinnamon rolls are a favorite with our guests. Other breakfast items include coffee, orange juice, milk, cereal, instant oatmeal, bagels, and muffins.",
-         "Tags": [
-         "continental breakfast",
-         "free wifi",
-         "24-hour front desk service"
-         ]
-      },
-      {
-         "@search.score": 0.92481667,
-         "@search.rerankerScore": 2.221315860748291,
-         "@search.captions": [
-         {
-            "text": "White Mountain Lodge & Suites. Resort and Spa. continental breakfast\r\npool\r\nrestaurant. Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings..",
-            "highlights": ""
-         }
-         ],
-         "HotelName": "White Mountain Lodge & Suites",
-         "Description": "Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings.",
-         "Tags": [
-         "continental breakfast",
-         "pool",
-         "restaurant"
-         ]
-      },
-      . . .
-   ]}
-   ```
-
-## Get service endpoints
-
-In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints so that you can provide them as variables in your code.
-
-1. Sign in to the [Azure portal](https://portal.azure.com).
-
-1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
-
-1. On the **Overview** home page, copy the URL. An example endpoint might look like `https://example.search.windows.net`. 
-
-1. [Find your Azure OpenAI service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.CognitiveServices%2Faccounts).
-
-1. On the **Overview** home page, select the link to view the endpoints. Copy the URL. An example endpoint might look like `https://example.openai.azure.com/`.
-
-## Set up environment variables for local development
-
-1. Create a `.env` file.
-1. Add the following environment variables to the `.env` file, replacing the values with your own service endpoints and keys.
-
-   ```plaintext
-   AZURE_SEARCH_ENDPOINT=<YOUR AZURE AI SEARCH ENDPOINT>
-   AZURE_SEARCH_INDEX_NAME=hotels-sample-index
-
-   AZURE_OPENAI_ENDPOINT=<YOUR AZURE OPENAI ENDPOINT>
-   AZURE_OPENAI_VERSION=<YOUR AZURE OPENAI API VERSION>
-   AZURE_DEPLOYMENT_MODEL=<YOUR DEPLOYMENT NAME>
-   ```
-
-## Set up the Node.JS project
-
-Set up project with Visual Studio Code and TypeScript.
-
-1. Start Visual Studio Code in a new directory.
-
-   ```bash
-   mkdir rag-quickstart && cd rag-quickstart
-   code .
-   ```
-1. Create a new package for ESM modules in your project directory.
-
-   ```bash
-   npm init -y
-   npm pkg set type=module
-   ```
-
-   This creates a `package.json` file with default values.
-
-1. Install the following npm packages.
-
-   ```bash
-   npm install @azure/identity @azure/search-documents openai dotenv @types/node
-   ``` 
-
-1. Create a `src` directory in your project directory.
-
-   ```bash
-   mkdir src
-   ```
-
-1. Create a `tsconfig.json` file in the project directory for ESM with the following content.
-
-    ```json
-    {
-      "compilerOptions": {
-        "target": "esnext",
-        "module": "NodeNext",
-        "moduleResolution": "nodenext",
-        "rootDir": "./src",
-        "outDir": "./dist/",
-        "esModuleInterop": true,
-        "forceConsistentCasingInFileNames": true,
-        "strict": true,
-        "skipLibCheck": true,
-        "declaration": true,
-        "sourceMap": true,
-        "resolveJsonModule": true,
-        "moduleDetection": "force", // Add this for ESM
-        "allowSyntheticDefaultImports": true // Helpful for ESM interop
-      },
-      "include": [
-        "src/**/*.ts"
-      ]
-    }
-   ```
-
-## Sign in to Azure
-
-You're using Microsoft Entra ID and role assignments for the connection. Make sure you're logged in to the same tenant and subscription as Azure AI Search and Azure OpenAI. You can use the Azure CLI on the command line to show current properties, change properties, and to sign in. For more information, see [Connect without keys](../../search-get-started-rbac.md). 
-
-Run each of the following commands in sequence.
-
-```azure-cli
-az account show
-
-az account set --subscription <PUT YOUR SUBSCRIPTION ID HERE>
-
-az login --tenant <PUT YOUR TENANT ID HERE>
-```
-
-You should now be logged in to Azure from your local device.
-
-## Set up query and chat thread
-
-Create a query script that uses the Azure AI Search index and the chat model to generate responses based on grounding data. The following steps guide you through setting up the query script.
-
-
-1. Create a `query.ts` file in the `src` directory with the following code.
-
-    :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-rag-ts/src/query.ts" :::
-
-
-
-    The preceding code does the following:
-    - Imports the necessary libraries for Azure AI Search and Azure OpenAI.
-    - Uses environment variables to configure the Azure AI Search and Azure OpenAI clients.
-    - Defines a function to get the clients for Azure AI Search and Azure OpenAI, using environment variables for configuration.
-    - Defines a function to query Azure AI Search for sources based on the user query.
-    - Defines a function to query Azure OpenAI for a response based on the user query and the sources retrieved from Azure AI Search.
-    - The `main` function orchestrates the flow by calling the search and OpenAI functions, and then prints the response.    
-    
-1. Build the TypeScript code to JavaScript.
-
-   ```bash
-   tsc
-   ```
-
-   This command compiles the TypeScript code in the `src` directory and outputs the JavaScript files in the `dist` directory.
-
-1. Run the following command in a terminal to execute the query script:
-
-    ```bash
-    node -r dotenv/config dist/query.js
-    ```
-
-    The `.env` is passed into the runtime using the `-r dotenv/config`. 
-
-1. View the output consists of recommendations for several hotels. Here's an example of what the output might look like:
-
-    ```
-    Sure! Here are a few hotels that offer complimentary breakfast:
-    
-    - **Head Wind Resort**
-    - Complimentary continental breakfast in the lobby
-    - Free Wi-Fi throughout the hotel
-    
-    - **Double Sanctuary Resort**
-    - Continental breakfast included
-    
-    - **White Mountain Lodge & Suites**
-    - Continental breakfast available
-    
-    - **Swan Bird Lake Inn**
-    - Continental-style breakfast each morning with a variety of food and drinks 
-        such as caramel cinnamon rolls, coffee, orange juice, milk, cereal, 
-        instant oatmeal, bagels, and muffins
-    ```
-
-## Troubleshooting
-
-If you get a **Forbidden** error message, check Azure AI Search configuration to make sure role-based access is enabled.
-
-If you get an **Authorization failed** error message, wait a few minutes and try again. It can take several minutes for role assignments to become operational.
-
-If you get a **Resource not found** error message, check the resource URIs and make sure the API version on the chat model is valid.
-
-Otherwise, to experiment further, change the query and rerun the last step to better understand how the model works with the grounding data.
-
-You can also modify the prompt to change the tone or structure of the output.
-
-You might also try the query without semantic ranking by setting `use_semantic_reranker=False` in the query parameters step. Semantic ranking can noticably improve the relevance of query results and the ability of the LLM to return useful information. Experimentation can help you decide whether it makes a difference for your content.
-
-## Send a complex RAG query
-
-Azure AI Search supports [complex types](../../search-howto-complex-data-types.md) for nested JSON structures. In the hotels-sample-index, `Address` is an example of a complex type, consisting of `Address.StreetAddress`, `Address.City`, `Address.StateProvince`, `Address.PostalCode`, and `Address.Country`. The index also has complex collection of `Rooms` for each hotel.
-
-If your index has complex types, change your prompt to include formatting instructions: 
-
-```text
-Can you recommend a few hotels that offer complimentary breakfast? 
-Tell me their description, address, tags, and the rate for one room that sleeps 4 people.
-```
-
-1. Create a new file `queryComplex.ts` in the `src` directory.
-1. Copy the following code to the file:
-
-    :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-rag-ts/src/queryComplex.ts" :::
-
-1. Build the TypeScript code to JavaScript.
-
-   ```bash
-   tsc
-   ```
-
-   This command compiles the TypeScript code in the `src` directory and outputs the JavaScript files in the `dist` directory.
-
-1. Run the following command in a terminal to execute the query script:
-
-    ```bash
-    node -r dotenv/config dist/queryComplex.js
-    ```
-
-    The `.env` is passed into the runtime using the `-r dotenv/config`. 
-
-
-1. View the output from Azure OpenAI, and it adds content from complex types.
-
-```
-Here are a few hotels that offer complimentary breakfast and have rooms that sleep 4 people:
-
-1. **Head Wind Resort**
-   - **Description:** The best of old town hospitality combined with views of the river and 
-   cool breezes off the prairie. Enjoy a complimentary continental breakfast in the lobby, 
-   and free Wi-Fi throughout the hotel.
-   - **Address:** 7633 E 63rd Pl, Tulsa, OK 74133, USA
-   - **Tags:** Coffee in lobby, free Wi-Fi, view
-   - **Room for 4:** Suite, 2 Queen Beds (Amenities) - $254.99
-
-2. **Double Sanctuary Resort**
-   - **Description:** 5-star Luxury Hotel - Biggest Rooms in the city. #1 Hotel in the area 
-   listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso 
-   in room. Offers continental breakfast.
-   - **Address:** 2211 Elliott Ave, Seattle, WA 98121, USA
-   - **Tags:** View, pool, restaurant, bar, continental breakfast
-   - **Room for 4:** Suite, 2 Queen Beds (Amenities) - $254.99
-
-3. **Swan Bird Lake Inn**
-   - **Description:** Continental-style breakfast featuring a variety of food and drinks. 
-   Locally made caramel cinnamon rolls are a favorite.
-   - **Address:** 1 Memorial Dr, Cambridge, MA 02142, USA
-   - **Tags:** Continental breakfast, free Wi-Fi, 24-hour front desk service
-   - **Room for 4:** Budget Room, 2 Queen Beds (City View) - $85.99
-
-4. **Gastronomic Landscape Hotel**
-   - **Description:** Known for its culinary excellence under the management of William Dough, 
-   offers continental breakfast.
-   - **Address:** 3393 Peachtree Rd, Atlanta, GA 30326, USA
-   - **Tags:** Restaurant, bar, continental breakfast
-   - **Room for 4:** Budget Room, 2 Queen Beds (Amenities) - $66.99
-...
-   - **Tags:** Pool, continental breakfast, free parking
-   - **Room for 4:** Budget Room, 2 Queen Beds (Amenities) - $60.99
-
-Enjoy your stay! Let me know if you need any more information.
-```
-
-## Troubleshooting errors
-
-To debug Azure SDK errors, set the environment variable `AZURE_LOG_LEVEL` to one of the following: `verbose`, `info`, `warning`, `error`. This will enable detailed logging for the Azure SDK, which can help identify [issues with authentication](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/identity/identity/TROUBLESHOOTING.md#enable-and-configure-logging), network connectivity, or other problems.
-
-Rerun the query script. You should now get informational statements from the SDKs in the output that provide more detail about any issues.
-
-If you see output messages related to ManagedIdentityCredential and token acquisition failures, it could be that you have multiple tenants, and your Azure sign-in is using a tenant that doesn't have your search service. To get your tenant ID, search the Azure portal for "tenant properties" or run `az login tenant list`.
-
-Once you have your tenant ID, run `az login --tenant <YOUR-TENANT-ID>` at a command prompt, and then rerun the script.
-
-## Clean up
-
-When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "RAG TypeScript クイックスタートの削除"
}
```

### Explanation
このコードの変更は、`search-get-started-rag-typescript.md`ファイルが完全に削除されたことに関するものです。この変更により、441行の内容が削除され、具体的にはAzure AI SearchおよびAzure OpenAIを使用したRAG（Retrieval-Augmented Generation）に関するTypeScript向けのクイックスタートガイドが含まれていました。このファイルには、前提条件、役割に基づくアクセスの設定、インデックスの作成、環境変数の設定、Node.jsプロジェクトの設定、クエリの作成手順、エラーハンドリング、結果の検証が詳細に記載されていました。

この変更は、ドキュメントの整理や更新の一環として行われたと考えられますが、利用者にとっては有用な情報が失われることになります。今後、他の資料やガイドラインでこれらの情報が再提供されることを期待する必要があります。

## articles/search/index-add-custom-analyzers.md{#item-11325e}

<details>
<summary>Diff</summary>
````diff
@@ -297,7 +297,7 @@ In the following table, the token filters that are implemented using Apache Luce
 |[shingle](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/shingle/ShingleFilter.html)|ShingleTokenFilter|Creates combinations of tokens as a single token.<br><br> **Options**<br><br> maxShingleSize (type: int) - Defaults to 2.<br><br> minShingleSize (type: int) - Defaults to 2.<br><br> outputUnigrams (type: bool) - if true, the output stream contains the input tokens (unigrams) as well as shingles. The default is true.<br><br> outputUnigramsIfNoShingles (type: bool) - If true, override the behavior of outputUnigrams==false for those times when no shingles are available. The default is false.<br><br> tokenSeparator (type: string) - The string to use when joining adjacent tokens to form a shingle. The default is a single empty space ` `. <br><br> filterToken (type: string) - The string to insert for each position for which there's no token. The default is `_`.|  
 |[snowball](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/snowball/SnowballFilter.html)|SnowballTokenFilter|Snowball Token Filter.<br><br> **Options**<br><br> language (type: string) - Allowed values include: `armenian`, `basque`, `catalan`, `danish`, `dutch`, `english`, `finnish`, `french`, `german`, `german2`, `hungarian`, `italian`, `kp`, `lovins`, `norwegian`, `porter`, `portuguese`, `romanian`, `russian`, `spanish`, `swedish`, `turkish`|  
 |[sorani_normalization](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ckb/SoraniNormalizationFilter.html)|SoraniNormalizationTokenFilter|Normalizes the Unicode representation of `Sorani` text.<br><br> **Options**<br><br> None.|  
-|stemmer|StemmerTokenFilter|Language-specific stemming filter.<br><br> **Options**<br><br> language (type: string) - Allowed values include: <br> -   [`arabic`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ar/ArabicStemmer.html)<br>-   [`armenian`](https://snowballstem.org/algorithms/armenian/stemmer.html)<br>-   [`basque`](https://snowballstem.org/algorithms/basque/stemmer.html)<br>-   [`brazilian`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/br/BrazilianStemmer.html)<br>-   `bulgarian`<br>-   [`catalan`](https://snowballstem.org/algorithms/catalan/stemmer.html)<br>-   [`czech`](https://portal.acm.org/citation.cfm?id=1598600)<br>-   [`danish`](https://snowballstem.org/algorithms/danish/stemmer.html)<br>-   [`dutch`](https://snowballstem.org/algorithms/dutch/stemmer.html)<br>-   [`dutchKp`](https://snowballstem.org/algorithms/kraaij_pohlmann/stemmer.html)<br>-   [`english`](https://snowballstem.org/algorithms/porter/stemmer.html)<br>-   [`lightEnglish`](https://ciir.cs.umass.edu/pubfiles/ir-35.pdf)<br>-   [`minimalEnglish`](https://www.researchgate.net/publication/220433848_How_effective_is_suffixing)<br>-   [`possessiveEnglish`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/en/EnglishPossessiveFilter.html)<br>-   [`porter2`](https://snowballstem.org/algorithms/english/stemmer.html)<br>-   [`lovins`](https://snowballstem.org/algorithms/lovins/stemmer.html)<br>-   [`finnish`](https://snowballstem.org/algorithms/finnish/stemmer.html)<br>-   `lightFinnish`<br>-   [`french`](https://snowballstem.org/algorithms/french/stemmer.html)<br>-   [`lightFrench`](https://dl.acm.org/citation.cfm?id=1141523)<br>-   [`minimalFrench`](https://dl.acm.org/citation.cfm?id=318984)<br>-   `galician`<br>-   `minimalGalician`<br>-   [`german`](https://snowballstem.org/algorithms/german/stemmer.html)<br>-   [`german2`](https://snowballstem.org/algorithms/german2/stemmer.html)<br>-   [`lightGerman`](https://dl.acm.org/citation.cfm?id=1141523)<br>-   `minimalGerman`<br>-   [`greek`](https://sais.se/mthprize/2007/ntais2007.pdf)<br>-   `hindi`<br>-   [`hungarian`](https://snowballstem.org/algorithms/hungarian/stemmer.html)<br>-   [`lightHungarian`](https://dl.acm.org/citation.cfm?id=1141523&dl=ACM&coll=DL&CFID=179095584&CFTOKEN=80067181)<br>-   [`indonesian`](https://eprints.illc.uva.nl/741/2/MoL-2003-03.text.pdf)<br>-   [`irish`](https://snowballstem.org/algorithms/irish/stemmer.html)<br>-   [`italian`](https://snowballstem.org/algorithms/italian/stemmer.html)<br>-   [`lightItalian`](https://www.ercim.eu/publication/ws-proceedings/CLEF2/savoy.pdf)<br>-   [`sorani`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ckb/SoraniStemmer.html)<br>-   [`latvian`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/lv/LatvianStemmer.html)<br>-   [`norwegian`](https://snowballstem.org/algorithms/norwegian/stemmer.html)<br>-   [`lightNorwegian`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/no/NorwegianLightStemmer.html)<br>-   [`minimalNorwegian`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/no/NorwegianMinimalStemmer.html)<br>-   [`lightNynorsk`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/no/NorwegianLightStemmer.html)<br>-   [`minimalNynorsk`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/no/NorwegianMinimalStemmer.html)<br>-   [`portuguese`](https://snowballstem.org/algorithms/portuguese/stemmer.html)<br>-   [`lightPortuguese`](https://dl.acm.org/citation.cfm?id=1141523&dl=ACM&coll=DL&CFID=179095584&CFTOKEN=80067181)<br>-   [`minimalPortuguese`](https://web.archive.org/web/20230425141918/https://www.inf.ufrgs.br/~buriol/papers/Orengo_CLEF07.pdf)<br>-   [`portugueseRslp`](https://web.archive.org/web/20230422082818/https://www.inf.ufrgs.br/~viviane/rslp/index.htm)<br>-   [`romanian`](https://snowballstem.org/otherapps/romanian/)<br>-   [`russian`](https://snowballstem.org/algorithms/russian/stemmer.html)<br>-   [`lightRussian`](https://doc.rero.ch/lm.php?url=1000%2C43%2C4%2C20091209094227-CA%2FDolamic_Ljiljana_-_Indexing_and_Searching_Strategies_for_the_Russian_20091209.pdf)<br>-   [`spanish`](https://snowballstem.org/algorithms/spanish/stemmer.html)<br>-   [`lightSpanish`](https://www.ercim.eu/publication/ws-proceedings/CLEF2/savoy.pdf)<br>-   [`swedish`](https://snowballstem.org/algorithms/swedish/stemmer.html)<br>-   `lightSwedish`<br>-   [`turkish`](https://snowballstem.org/algorithms/turkish/stemmer.html)|  
+|stemmer|StemmerTokenFilter|Language-specific stemming filter.<br><br> **Options**<br><br> language (type: string) - Allowed values include: <br> -   [`arabic`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ar/ArabicStemmer.html)<br>-   [`armenian`](https://snowballstem.org/algorithms/armenian/stemmer.html)<br>-   [`basque`](https://snowballstem.org/algorithms/basque/stemmer.html)<br>-   [`brazilian`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/br/BrazilianStemmer.html)<br>-   `bulgarian`<br>-   [`catalan`](https://snowballstem.org/algorithms/catalan/stemmer.html)<br>-   [`czech`](https://portal.acm.org/citation.cfm?id=1598600)<br>-   [`danish`](https://snowballstem.org/algorithms/danish/stemmer.html)<br>-   [`dutch`](https://snowballstem.org/algorithms/dutch/stemmer.html)<br>-   [`dutchKp`](https://snowballstem.org/algorithms/kraaij_pohlmann/stemmer.html)<br>-   [`english`](https://snowballstem.org/algorithms/porter/stemmer.html)<br>-   [`lightEnglish`](https://ciir.cs.umass.edu/pubfiles/ir-35.pdf)<br>-   [`minimalEnglish`](https://www.researchgate.net/publication/220433848_How_effective_is_suffixing)<br>-   [`possessiveEnglish`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/en/EnglishPossessiveFilter.html)<br>-   [`porter2`](https://snowballstem.org/algorithms/english/stemmer.html)<br>-   [`lovins`](https://snowballstem.org/algorithms/lovins/stemmer.html)<br>-   [`finnish`](https://snowballstem.org/algorithms/finnish/stemmer.html)<br>-   `lightFinnish`<br>-   [`french`](https://snowballstem.org/algorithms/french/stemmer.html)<br>-   [`lightFrench`](https://dl.acm.org/citation.cfm?id=1141523)<br>-   [`minimalFrench`](https://dl.acm.org/citation.cfm?id=318984)<br>-   `galician`<br>-   `minimalGalician`<br>-   [`german`](https://snowballstem.org/algorithms/german/stemmer.html)<br>-   [`german2`](https://snowballstem.org/algorithms/german2/stemmer.html)<br>-   [`lightGerman`](https://dl.acm.org/citation.cfm?id=1141523)<br>-   `minimalGerman`<br>-   [`greek`](https://snowballstem.org/algorithms/greek/stemmer.html)<br>-   `hindi`<br>-   [`hungarian`](https://snowballstem.org/algorithms/hungarian/stemmer.html)<br>-   [`lightHungarian`](https://dl.acm.org/citation.cfm?id=1141523&dl=ACM&coll=DL&CFID=179095584&CFTOKEN=80067181)<br>-   [`indonesian`](https://eprints.illc.uva.nl/741/2/MoL-2003-03.text.pdf)<br>-   [`irish`](https://snowballstem.org/algorithms/irish/stemmer.html)<br>-   [`italian`](https://snowballstem.org/algorithms/italian/stemmer.html)<br>-   [`lightItalian`](https://www.ercim.eu/publication/ws-proceedings/CLEF2/savoy.pdf)<br>-   [`sorani`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ckb/SoraniStemmer.html)<br>-   [`latvian`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/lv/LatvianStemmer.html)<br>-   [`norwegian`](https://snowballstem.org/algorithms/norwegian/stemmer.html)<br>-   [`lightNorwegian`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/no/NorwegianLightStemmer.html)<br>-   [`minimalNorwegian`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/no/NorwegianMinimalStemmer.html)<br>-   [`lightNynorsk`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/no/NorwegianLightStemmer.html)<br>-   [`minimalNynorsk`](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/no/NorwegianMinimalStemmer.html)<br>-   [`portuguese`](https://snowballstem.org/algorithms/portuguese/stemmer.html)<br>-   [`lightPortuguese`](https://dl.acm.org/citation.cfm?id=1141523&dl=ACM&coll=DL&CFID=179095584&CFTOKEN=80067181)<br>-   [`minimalPortuguese`](https://web.archive.org/web/20230425141918/https://www.inf.ufrgs.br/~buriol/papers/Orengo_CLEF07.pdf)<br>-   [`portugueseRslp`](https://web.archive.org/web/20230422082818/https://www.inf.ufrgs.br/~viviane/rslp/index.htm)<br>-   [`romanian`](https://snowballstem.org/otherapps/romanian/)<br>-   [`russian`](https://snowballstem.org/algorithms/russian/stemmer.html)<br>-   [`lightRussian`](https://doc.rero.ch/lm.php?url=1000%2C43%2C4%2C20091209094227-CA%2FDolamic_Ljiljana_-_Indexing_and_Searching_Strategies_for_the_Russian_20091209.pdf)<br>-   [`spanish`](https://snowballstem.org/algorithms/spanish/stemmer.html)<br>-   [`lightSpanish`](https://www.ercim.eu/publication/ws-proceedings/CLEF2/savoy.pdf)<br>-   [`swedish`](https://snowballstem.org/algorithms/swedish/stemmer.html)<br>-   `lightSwedish`<br>-   [`turkish`](https://snowballstem.org/algorithms/turkish/stemmer.html)|  
 |[stemmer_override](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/miscellaneous/StemmerOverrideFilter.html)|StemmerOverrideTokenFilter|Any dictionary-Stemmed terms are marked as keywords, which prevents stemming down the chain. Must be placed before any stemming filters.<br><br> **Options**<br><br> rules (type: string array) - Stemming rules in the following format `word => stem` for example `ran => run`. The default is an empty list.  Required.|  
 |[stopwords](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/core/StopFilter.html)|StopwordsTokenFilter|Removes stop words from a token stream. By default, the filter uses a predefined stop word list for English.<br><br> **Options**<br><br> stopwords (type: string array) - A list of stopwords. Can't be specified if a stopwordsList is specified.<br><br> stopwordsList (type: string) - A predefined list of stopwords. Can't be specified if `stopwords` is specified. Allowed values include:`arabic`, `armenian`, `basque`, `brazilian`, `bulgarian`, `catalan`, `czech`, `danish`, `dutch`, `english`, `finnish`, `french`, `galician`, `german`, `greek`, `hindi`, `hungarian`, `indonesian`, `irish`, `italian`, `latvian`, `norwegian`, `persian`, `portuguese`, `romanian`, `russian`, `sorani`, `spanish`, `swedish`, `thai`, `turkish`, default: `english`. Can't be specified if `stopwords` is specified. <br><br> ignoreCase (type: bool) - If true, all words are lower cased first. The default is false.<br><br> removeTrailing (type: bool) - If true, ignore the last search term if it's a stop word. The default is true.
 |[synonym](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/synonym/SynonymFilter.html)|SynonymTokenFilter|Matches single or multi word synonyms in a token stream.<br><br> **Options**<br><br> synonyms (type: string array) - Required. List of synonyms in one of the following two formats:<br><br> -incredible, unbelievable, fabulous => amazing - all terms on the left side of => symbol are replaced with all terms on its right side.<br><br> -incredible, unbelievable, fabulous, amazing - A comma-separated list of equivalent words. Set the expand option to change how this list is interpreted.<br><br> ignoreCase (type: bool) - Case-folds input for matching. The default is false.<br><br> expand (type: bool) - If true, all words in the list of synonyms (if => notation isn't used) map to one another. <br>The following list: incredible, unbelievable, fabulous, amazing is equivalent to: incredible, unbelievable, fabulous, amazing => incredible, unbelievable, fabulous, amazing<br><br>- If false, the following list: incredible, unbelievable, fabulous, amazing are equivalent to: incredible, unbelievable, fabulous, amazing => incredible.|  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムアナライザーのドキュメント修正"
}
```

### Explanation
このコード変更は、`index-add-custom-analyzers.md`ファイルの内容を修正したものです。修正点は、異なる言語に対応したステミングフィルターの紹介部分において、`stemmer`（ステマー）フィルターに関連する表記を更新したことです。

具体的には、`stemmer`フィルターの説明が明確化され、支持される言語のリンクの表記が見直され、テキストの整然とした表示が改善されました。これにより、開発者がカスタムアナライザーを使用する際の正確な情報が提供され、ユーザーが対応可能な言語オプションとそれに関連するリソースをより簡単に把握できるようになっています。

この変更は、ドキュメントの信頼性を高め、より多くの言語に対応した使いやすさを向上させる一助となるでしょう。

## articles/search/index.yml{#item-c67121}

<details>
<summary>Diff</summary>
````diff
@@ -1,94 +1,118 @@
 ### YamlMime:Landing
 
 title: Azure AI Search documentation # < 60 chars
-summary: Information retrieval at scale for agentic retrieval, with vector and text content in traditional or generative search scenarios.
+summary: Learn how to use Azure AI Search for information retrieval at scale, with support for text, vector, and multimodal content in traditional and generative search scenarios.
 metadata:
   title: Azure AI Search documentation
-  description: Information retrieval at scale for agentic retrieval, with vector and text content in traditional or generative search scenarios.
+  description: Learn how to use Azure AI Search for information retrieval at scale, with support for text, vector, and multimodal content in traditional and generative search scenarios.
   author: HeidiSteen
   ms.author: heidist
-  ms.date: 09/23/2025
+  ms.date: 12/12/2025
   ms.service: azure-ai-search
   ms.topic: landing-page
   ms.custom:
     - ignite-2023
     - ignite-2024
     - build-2025
-# linkListType: architecture | concept | deploy | download | get-started | how-to-guide | learn | overview | quickstart | reference | tutorial | video | whats-new
+# linkListType: architecture | concept | deploy | download | get-started | how-to-guide | tutorial | overview | quickstart | reference | sample | tutorial | video | whats-new
 
 landingContent:
 # Cards and links should be based on top customer tasks or top subjects
 # Start card title with a verb
   # Card
-  - title: About Azure AI Search
+  - title: Get started
     linkLists:
-      - linkListType: concept
+      - linkListType: overview
         links:
-          - text: What is Azure AI Search?
+          - text: What's Azure AI Search?
             url: search-what-is-azure-search.md
-          - text: AI enrichment
-            url: cognitive-search-concept-intro.md
-          - text: Semantic ranking
-            url: semantic-search-overview.md
+          - text: Features
+            url: search-features-list.md
+          - text: FAQ
+            url: search-faq-frequently-asked-questions.yml
       - linkListType: how-to-guide
         links:
           - text: Create a search service
             url: search-create-service-portal.md
           - text: Configure a search service
             url: search-manage.md
-          - text: Create a search index
-            url: search-get-started-portal.md
-          - text: Add vectors to an index
-            url: search-get-started-vector.md
-          - text: Query a vector index
-            url: vector-search-how-to-query.md
 
   # Card
-  - title: Agentic retrieval and vectors
+  - title: Agentic retrieval (RAG)
     linkLists:
       - linkListType: concept
         links:
-          - text: Retrieval Augmented Generation (RAG)
-            url: retrieval-augmented-generation-overview.md
           - text: Agentic retrieval
-            url: agentic-retrieval-overview.md        
+            url: agentic-retrieval-overview.md
+      - linkListType: quickstart
+        links:
+          - text: Use agentic retrieval
+            url: search-get-started-agentic-retrieval.md
+      - linkListType: how-to-guide
+        links:
+          - text: Create a knowledge base
+            url: agentic-retrieval-how-to-create-knowledge-base.md
+          - text: Retrieve from a knowledge base
+            url: agentic-retrieval-how-to-retrieve.md
+
+  # Card
+  - title: Classic search
+    linkLists:
+      - linkListType: concept
+        links:
+          - text: Full-text search
+            url: search-lucene-query-architecture.md
           - text: Vector search
             url: vector-search-overview.md
+          - text: Hybrid search
+            url: hybrid-search-overview.md
           - text: Multimodal search
             url: multimodal-search-overview.md
-          - text: Built-in vectorization
-            url: vector-search-integrated-vectorization.md
-          - text: Built-in compression
-            url: vector-search-how-to-quantization.md
       - linkListType: quickstart
         links:
-          - text: 'Classic RAG'
-            url: search-get-started-agentic-retrieval.md
-          - text: 'Agentic retrieval'
-            url: search-get-started-agentic-retrieval.md
-
-
+          - text: Use full-text search
+            url: search-get-started-text.md
+          - text: Use vector search
+            url: search-get-started-vector.md
+      - linkListType: how-to-guide
+        links:
+          - text: Create a search index
+            url: search-how-to-create-search-index.md
+          - text: Create a vector index
+            url: vector-search-how-to-create-index.md
+          - text: Query a vector index
+            url: vector-search-how-to-query.md
 
   # Card
-  - title: Code
+  - title: Code samples
     linkLists:
-      - linkListType: get-started
+      - linkListType: sample
         links:
-          - text: Python samples
-            url: samples-python.md
           - text: .NET samples
             url: samples-dotnet.md
+          - text: Java samples
+            url: samples-java.md
+          - text: JavaScript samples
+            url: samples-javascript.md
+          - text: Python samples
+            url: samples-python.md
+          - text: REST samples
+            url: samples-rest.md
           - text: Vector samples
             url: https://github.com/Azure/azure-search-vector-samples
+
+  # Card
+  - title: References
+    linkLists:
       - linkListType: reference
         links:
-          - text: Azure REST API Reference
-            url: /rest/api/searchservice/
           - text: Azure SDK for .NET
             url: /dotnet/api/overview/azure/search.documents-readme
-          - text: Azure SDK for Python
-            url: /python/api/overview/azure/search-documents-readme
           - text: Azure SDK for Java
             url: /java/api/overview/azure/search-documents-readme
           - text: Azure SDK for JavaScript
             url: /javascript/api/overview/azure/search-documents-readme
+          - text: Azure SDK for Python
+            url: /python/api/overview/azure/search-documents-readme
+          - text: Azure REST API
+            url: /rest/api/searchservice/
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search ドキュメントの修正"
}
```

### Explanation
この変更は、`index.yml`ファイルの内容を修正したもので、主にAzure AI Searchに関する文書の要約、説明、コンテンツのリンクリストを更新しています。具体的には、サマリーの内容がより具体的で明確な文に改訂され、ユーザーが学べる内容が強調されました。 

変更点としては、サブタイトルやリンクリストが追加・更新され、特に「エージェントによる検索（RAG）」や「古典的な検索」といった新しいカードが追加されています。これにより、ユーザーが関連する情報や具体的なクイックスタートガイド、ハウツーガイドに簡単にアクセスできるようになりました。

また、サンプルコードに関するカードも拡充され、さまざまなプログラミング言語や技術に関連するサンプルリンクが整備されています。これにより、ドキュメント全体の使いやすさと情報の網羅性が向上し、Azure AI Searchの機能を活用するための有益なリソースとしての価値が高まっています。

## articles/search/samples-dotnet.md{#item-12f3fa}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,6 @@ Code samples from the Azure AI Search team demonstrate features and workflows. T
 |--|--|--|
 | [quickstart](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/AzureSearchQuickstart) | [Quickstart: Full-text search](search-get-started-text.md) | Create, load, and query an index using sample data. |
 | [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) | [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md) | Integrate semantic ranking with LLM-powered query planning and answer generation. |
-| [quickstart-rag](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-rag) | [Quickstart: Generative search (RAG)](search-get-started-rag.md) | Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
 | [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-search/) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Add semantic ranking to an index schema and run semantic queries. |
 | [quickstart-vector-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-vector-search) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
 | [search-website](https://github.com/Azure-Samples/azure-search-static-web-app) | [Tutorial: Add search to web apps](tutorial-csharp-overview.md) | Build an end-to-end search app that uses the push API for bulk upload and a rich client for hosting the app and handling search requests. |
@@ -75,6 +74,7 @@ The following samples are also published by the Azure AI Search team but aren't
 
 | Sample | Description |
 |--|--|
+| [azure-search-classic-rag](https://github.com/Azure-Samples/azure-search-classic-rag/tree/main/quickstarts) | Single-shot RAG using the classic search engine as grounding data from Azure AI Search, with a chat completion model from Azure OpenAI. |
 | [check-storage-usage](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/check-storage-usage/README.md) | Check search service storage on a schedule using an Azure function. |
 | [export-data](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/export-data) | Partition and export a large index using a C# console app. |
 | [index-backup-restore](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore) | Copy an index from one service to another, creating JSON files with the index schema and documents. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search DotNet サンプルの更新"
}
```

### Explanation
この変更は、`samples-dotnet.md`ファイルの修正に関するもので、Azure AI Searchの機能やワークフローを示すコードサンプルに関する情報が更新されています。具体的には、次のような点が改善されています。

1. **新しいサンプルの追加**: `azure-search-classic-rag`という新しいサンプルが追加されました。このサンプルは、クラシック検索エンジンを基盤データとして利用し、Azure OpenAIのチャット補完モデルを使用する一連の機能を示しています。

2. **サンプルのリスト更新**: 古いサンプルへのリンクが削除され、新たに洗練された情報が追加されることで、利用者が最新のリソースにアクセスしやすくなっています。特に、クイックスタートやチュートリアルのリンクが更新されており、ユーザーは新機能に基づいた具体的な使い方を見つけやすくなっています。

この変更により、Azure AI Searchの使用を推進し、開発者が関連するサンプルコードを適切に見つけやすくすることで、学習や実装をサポートすることを目的としています。

## articles/search/samples-javascript.md{#item-82e67e}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - devx-track-js
   - ignite-2023
 ms.topic: concept-article
-ms.date: 09/23/2025
+ms.date: 12/12/2025
 ---
 
 # JavaScript samples for Azure AI Search
@@ -61,15 +61,13 @@ Code samples from the Azure AI Search team demonstrate features and workflows. T
 | Sample | Article | Description |
 |--|--|--|
 | [quickstart](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) | [Quickstart: Full-text search](search-get-started-text.md) | Create, load, and query a search index using sample data. |
-| [quickstart-rag-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-rag-js) | [Quickstart: Generative search (RAG)](search-get-started-rag.md) | Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
 | [quickstart-semantic-ranking-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-js) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Add semantic ranking to an index schema and run semantic queries. |
 | [quickstart-vector-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-vector-js) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
 
 ### TypeScript samples
 
 | Sample | Article | Description |
 |--|--|--|
-| [quickstart-rag-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-rag-ts) | [Quickstart: Generative search (RAG)](search-get-started-rag.md) | Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
 | [quickstart-semantic-ranking-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-ts) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Add semantic ranking to an index schema and run semantic queries. |
 | [quickstart-vector-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-vector-ts) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
 
@@ -79,6 +77,7 @@ The following samples are also published by the Azure AI Search team but aren't
 
 | Sample | Description |
 |--|--|
+| [azure-search-classic-rag](https://github.com/Azure-Samples/azure-search-classic-rag/tree/main/quickstarts) | Single-shot RAG using the classic search engine as grounding data from Azure AI Search, with a chat completion model from Azure OpenAI. |
 | [azure-search-vector-sample.js](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript/readme.md) | JavaScript example of how to perform vector search. |
 | [azure-function-search](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/azure-function-search) | JavaScript example of an Azure function that sends queries to a search service. You can substitute this JavaScript version for the `api` code used in [Add search to web sites with .NET](tutorial-csharp-overview.md). |
 | [bulk-insert](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/bulk-insert) | JavaScript example of how to [use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search JavaScript サンプルの更新"
}
```

### Explanation
この変更は、`samples-javascript.md`ファイルの修正に関するもので、Azure AI Searchに関連するJavaScriptのコードサンプルの情報が更新されています。以下の点が主な変更点です。

1. **日付の更新**: ドキュメントの日付が`09/23/2025`から`12/12/2025`に修正され、将来的な更新スケジュールを反映しています。

2. **古いサンプルの削除**: 一部のサンプルリンクが削除され、特に`quickstart-rag-js`と`quickstart-rag-ts`がリストから外れています。この変更は、古い情報の整理や、より新しいサンプルに重点を置くためのものです。

3. **新しいサンプルの追加**: 新たに`azure-search-classic-rag`というサンプルが追加され、これはクラシック検索エンジンを基にしたRAG機能を示しています。ユーザーは、Azure OpenAIのチャット補完モデルを利用するこのサンプルを通じて、より高度な検索機能を学ぶことができます。

これらの変更により、JavaScript開発者がAzure AI Searchの機能を効果的に学び、利用できるサンプルが蓄積され、ドキュメントの整合性と価値が向上しています。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -38,7 +38,6 @@ Code samples from the Azure AI Search team demonstrate features and workflows. T
 |--|--|--|
 | [Quickstart](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart) | [Quickstart: Full-text search](search-get-started-text.md) | Create, load, and query a search index using sample data. |
 | [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval) | [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md) | Integrate semantic ranking with LLM-powered query planning and answer generation. |
-| [Quickstart-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-RAG) | [Quickstart: Generative search (RAG)](search-get-started-rag.md) | Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
 | [Quickstart-Semantic-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Add semantic ranking to an index schema and run semantic queries. |
 | [Quickstart-Vector-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Vector-Search) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
 | [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) | [Tutorial: Build an end-to-end agentic retrieval solution](agentic-retrieval-how-to-create-pipeline.md) | Unlike [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval), this sample incorporates Foundry Agent Service for request orchestration. |
@@ -67,7 +66,7 @@ The following samples are also published by the Azure AI Search team but aren't
 
 | Sample | Description |
 |--|--|
-| [Classic RAG pattern](https://github.com/Azure-Samples/azure-search-classic-rag/blob/main/README.md) | Create an indexing pipeline that uses the [classic search engine](search-what-is-azure-search.md#what-is-classic-search) to load, chunk, embed, and ingest searchable content. |
+| [azure-search-classic-rag](https://github.com/Azure-Samples/azure-search-classic-rag/tree/main/quickstarts) | Single-shot RAG using the classic search engine as grounding data from Azure AI Search, with a chat completion model from Azure OpenAI. |
 | [Quickstart-Document-Permissions-Pull-API](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Document-Permissions-Pull-API) | Using an indexer "pull API" approach, flow access control lists from a data source to search results and apply permission filters that restrict access to authorized content. |
 | [Quickstart-Document-Permissions-Push-API](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Document-Permissions-Push-API) | Using the push APIs for indexing a JSON payload, flow embedded permission metadata to indexed documents and search results that are filtered based on user access to authorized content. |
 | [azure-function-search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/azure-function-search) | Use an Azure function to send queries to a search service. You can substitute this Python version for the `api` code used in [Add search to web sites with .NET](tutorial-csharp-overview.md). |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search Python サンプルの更新"
}
```

### Explanation
この変更は、`samples-python.md`ファイルに行われた修正に関するもので、Azure AI Searchに関連するPythonのコードサンプルに関する情報が更新されています。主な変更点は以下の通りです。

1. **サンプルの情報更新**: `Classic RAG pattern`というサンプルが、`azure-search-classic-rag`という新しいリンクに置き換えられました。この新しいサンプルは、クラシック検索エンジンを基にしたRAG機能を示しており、Azure OpenAIのチャット補完モデルを利用することができます。

2. **古いサンプルの削除**: 別のRAG関連のサンプルである`Quickstart-RAG`がリストから削除されています。この変更により、より関連性の高い情報が優先され、ユーザーにとっての利便性が向上しています。

3. **新しいサンプルの追加**: `Quickstart-Document-Permissions-Pull-API`と`Quickstart-Document-Permissions-Push-API`のサンプルも引き続き含まれており、文書のアクセス制御を行うアプローチが説明されています。

これらの変更は、Azure AI SearchのPythonを利用する開発者にとって、より効率的で関連性の高いサンプルコードを提案し、学習や実装の手助けをすることを目的としています。

## articles/search/samples-rest.md{#item-198ebc}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,6 @@ Code samples from the Azure AI Search team demonstrate features and workflows. T
 |--|--|--|
 | [quickstart](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart) | [Quickstart: Full-text search](search-get-started-text.md) | Create, load, and query a search index using sample data. |
 | [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-agentic-retrieval) | [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md) | Integrate semantic ranking with LLM-powered query planning and answer generation. |
-| [quickstart-RAG](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-RAG) | [Quickstart: Classic generative search (RAG)](search-get-started-rag.md) | Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
 | [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-semantic-search) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Add semantic ranking to an index schema and run semantic queries. |
 | [quickstart-vectors](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
 | [acl](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/acl) | [Query-time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md) | Implement query-time access control using role-based access control (RBAC) and access control lists (ACLs). |
@@ -41,15 +40,11 @@ Code samples from the Azure AI Search team demonstrate features and workflows. T
 
 ## Other samples
 
-Currently, there are no other REST samples available.
-
-<!--
 The following samples are also published by the Azure AI Search team but aren't referenced in documentation. Associated README files provide usage instructions.
 
 | Sample | Description |
 |--|--|
-| | |
--->
+| [azure-search-classic-rag](https://github.com/Azure-Samples/azure-search-classic-rag/tree/main/quickstarts) | Single-shot RAG using the classic search engine as grounding data from Azure AI Search, with a chat completion model from Azure OpenAI. |
 
 > [!TIP]
 > Use the [samples browser](/samples/browse/?expanded=azure&languages=http&products=azure-cognitive-search) to search for Microsoft code samples on GitHub. You can filter your search by product, service, and language.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search REST サンプルの更新"
}
```

### Explanation
この変更は、`samples-rest.md`ファイルの修正に関するもので、Azure AI Searchに関連するREST APIのコードサンプルに関する情報が更新されています。主な変更点は以下の通りです。

1. **サンプルの削除**: `quickstart-RAG`というサンプルが削除されました。これにより、古い情報が整理され、新たな情報が優先される形となっています。

2. **新しいサンプルの追加**: 代わりに、`azure-search-classic-rag`という新しいサンプルが追加されました。このサンプルはクラシック検索エンジンを用いたRAG機能を示しており、Azure OpenAIのチャット補完モデルを利用してデータを検索することができます。

3. **内容の簡素化**: 「Currently, there are no other REST samples available.」という文が削除され、代わりに他のサンプルの情報が追加されています。このことにより、ドキュメントの情報がより充実し、ユーザーに対する有益なリソースを提供しています。

4. **使用方法の提案**: サンプルブラウザへのリンクが提示されており、ユーザーがGitHub上で利用可能なMicrosoftのコードサンプルを言語や製品でフィルタリングして検索できるようになっています。

これらの変更により、Azure AI SearchのREST APIを利用する際、ユーザーはより関連性の高いサンプルを見つけやすくなり、実装の参考にするための情報がより整備されています。

## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -273,7 +273,7 @@ To use the skills for image verbalization:
 
 1. On the **Image Verbalization** tab:
 
-   1. For the kind, select your LLM provider: **Azure OpenAI** or **Foundry Hub catalog models**.
+   1. For the kind, select your LLM provider: **Azure OpenAI** or **Azure AI Foundry**.
 
    1. Select your Azure subscription, resource, and LLM deployment.
 
@@ -285,7 +285,7 @@ To use the skills for image verbalization:
 
 1. On the **Text Vectorization** tab:
 
-   1. For the kind, select your model provider: **Azure OpenAI**, **Foundry Hub catalog models**, or **AI Vision vectorization**.
+   1. For the kind, select your model provider: **Azure OpenAI**, **Azure AI Foundry**, or **AI Vision vectorization**.
 
    1. Select your Azure subscription, resource, and embedding model deployment (if applicable).
 
@@ -309,7 +309,7 @@ To use the skills for multimodal embeddings:
 
    :::image type="content" source="media/search-get-started-portal-images/multimodal-embedding-tile.png" alt-text="Screenshot of the Multimodal Embedding tile in the wizard." border="true" lightbox="media/search-get-started-portal-images/multimodal-embedding-tile.png":::
 
-1. For the kind, select your model provider: **Foundry Hub catalog models** or **AI Vision vectorization**.
+1. For the kind, select your model provider: **Azure AI Foundry** or **AI Vision vectorization**.
 
    If Azure Vision is unavailable, make sure your search service and Foundry resource are both in a [region that supports the Azure Vision multimodal APIs](/azure/ai-services/computer-vision/how-to/image-retrieval).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundry 名称の変更"
}
```

### Explanation
この変更は、`search-get-started-portal-image-search.md`ファイルに対する修正です。主なポイントは以下の通りです。

1. **名称の統一**: 文中での「Foundry Hub catalog models」が「Azure AI Foundry」という名称に変更されました。これにより、製品名の一貫性が保たれ、ユーザーが混乱することを避けられます。

2. **変更の適用箇所**: 名前の変更は、画像の言語化、テキストのベクター化、マルチモーダル埋め込みの各セクションにおいて行われています。すべての該当箇所で「Foundry Hub catalog models」が「Azure AI Foundry」に置き換えられています。

3. **コンテキストの保持**: 変更が行われたにもかかわらず、全体の文脈は保持されており、ユーザーが手順を理解しやすいように整理されています。具体的な手順や注意事項に影響を与えず、用語がただ適切なものに置き換えられただけです。

これにより、Azure AI Foundryに関連する情報がより明確になり、ユーザーが適切なリソースを選択する際の助けとなることが期待されます。また、用語の統一により、ドキュメント全体の整合性が向上しています。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -369,7 +369,7 @@ During this step, the wizard uses your chosen [embedding model](#supported-embed
 
 ### [Microsoft Foundry](#tab/vectorize-text-catalog)
 
-1. On the **Vectorize your text** page, select **Foundry Hub catalog models** for the kind.
+1. On the **Vectorize your text** page, select **Azure AI Foundry** for the kind.
 
 1. Select your Azure subscription.
 
@@ -413,7 +413,7 @@ However, if your content includes useful images, you can apply AI in one or both
 
 1. On the **Vectorize and enrich your images** page, select the **Vectorize images** checkbox.
 
-1. For the kind, select your model provider: **Foundry Hub catalog models** or **AI Vision vectorization**.
+1. For the kind, select your model provider: **Azure AI Foundry** or **AI Vision vectorization**.
 
    If Azure Vision is unavailable, make sure your search service and Foundry resource are both in a [region that supports the Azure Vision multimodal APIs](/azure/ai-services/computer-vision/how-to/image-retrieval).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundry 名称の変更"
}
```

### Explanation
この変更は、`search-get-started-portal-import-vectors.md`ファイルの修正に関するもので、Azure AI Foundryに関連する用語の更新が行われています。主な変更点は以下の通りです。

1. **用語の変更**: 「Foundry Hub catalog models」という表現が、「Azure AI Foundry」という名称に置き換えられました。これにより、製品名の呼称が統一され、利用者にとっての理解が容易になります。

2. **変更が行われたセクション**: 修正は「テキストのベクター化」ページと「画像のベクター化と拡張」ページのそれぞれで行われており、該当する選択肢の表現が更新されています。

3. **内容の整合性**: 用語が変更されたにもかかわらず、文脈は保持されているため、読者が手順を理解しやすくなっており、変更が行われたことによって手順や注意事項に影響は与えられていません。

この変更により、Azure AI Foundry関連の情報がより明確になるとともに、ドキュメントの整合性と信頼性が高まります。ユーザーは、最新かつ正確なリソースを見つけやすくなり、作業がスムーズに進むことが期待されます。

## articles/search/search-get-started-rag.md{#item-05ff0e}

<details>
<summary>Diff</summary>
````diff
@@ -1,56 +0,0 @@
----
-title: 'Quickstart: Generative Search (RAG)'
-titleSuffix: Azure AI Search
-description: Learn how to use grounding data from Azure AI Search with a chat model on Azure OpenAI.
-author: haileytap
-ms.author: haileytapia
-ms.service: azure-ai-search
-ms.custom:
-  - ignite-2024
-ms.topic: quickstart
-ms.date: 10/15/2025
-zone_pivot_groups: programming-languages-ai-search-rag-qs
----
-
-# Quickstart: Classic generative search (RAG) using grounding data from Azure AI Search
-
-In this quickstart, you send queries to a chat completion model for a conversational search experience over your indexed content on Azure AI Search. After setting up Azure OpenAI and Azure AI Search resources in the Azure portal, you run code to call the APIs.
-
-> [!NOTE]
-> We now recommend [agentic retrieval](search-get-started-agentic-retrieval.md) for RAG workflows, but classic RAG is simpler. If it meets your application requirements, it's still a good choice.
-
-::: zone pivot="csharp"
-
-[!INCLUDE [.NET quickstart](includes/quickstarts/search-get-started-rag-dotnet.md)]
-
-::: zone-end
-
-::: zone pivot="java"
-
-[!INCLUDE [Java quickstart](includes/quickstarts/search-get-started-rag-java.md)]
-
-::: zone-end
-
-::: zone pivot="javascript"
-
-[!INCLUDE [JavaScript quickstart](includes/quickstarts/search-get-started-rag-javascript.md)]
-
-::: zone-end
-
-::: zone pivot="python"
-
-[!INCLUDE [Python quickstart](includes/quickstarts/search-get-started-rag-python.md)]
-
-::: zone-end
-
-::: zone pivot="rest"
-
-[!INCLUDE [Rest quickstart](includes/quickstarts/search-get-started-rag-rest.md)]
-
-::: zone-end
-
-::: zone pivot="typescript"
-
-[!INCLUDE [TypeScript quickstart](includes/quickstarts/search-get-started-rag-typescript.md)]
-
-::: zone-end
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "従来の生成検索 (RAG) ガイドの削除"
}
```

### Explanation
この変更は、`search-get-started-rag.md`ファイルの削除に関連しています。以下は、この削除の概要です。

1. **ファイルの削除**: 完全に56行が削除され、このファイルはもはや利用できなくなりました。削除された内容には、従来の生成検索（RAG）を使用してAzure AI Searchからデータを基にしたクイックスタートガイドが含まれていました。

2. **内容の特徴**: このクイックスタートガイドでは、Azure AI Searchにインデックスされたコンテンツを使用した会話型検索体験のために、チャット補完モデルにクエリを送信する方法が説明されていました。また、Azure OpenAIとAzure AI Searchリソースの設定方法についても触れていました。

3. **代替案の推奨**: 削除に伴い、今後は「エージェンティック・リトリーバル」（agentic retrieval）が推奨されていることが記載されており、従来のRAG手法は単純ではあるものの、必要に応じて依然として有効な選択肢であるとされています。

これにより、ユーザーは古い情報にアクセスできなくなりますが、新しい手法に移行するよう促されることになります。この変更は、Azure AI Searchの文書が最新の技術や推奨事項に基づいて更新されていることを示しています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -1,210 +1,134 @@
 items:
-- name: Azure AI Search Documentation
+- name: Azure AI Search documentation
   href: index.yml
+
 - name: Overview
   items:
-  - name: What is Azure AI Search?
+  - name: What's Azure AI Search?
     href: search-what-is-azure-search.md
-  - name: New in AI Search
+  - name: What's new
     href: whats-new.md
   - name: Features
     href: search-features-list.md
-  - name: Try AI Search for free
-    href: search-try-for-free.md
   - name: FAQ
     href: search-faq-frequently-asked-questions.yml
+  - name: Try for free
+    href: search-try-for-free.md
   expanded: true
-- name: Concepts
+
+- name: Quickstart
   items:
-  - name: Data
-    items:
-    - name: Data import strategies
-      href: search-what-is-data-import.md
-    - name: Search index
-      href: search-what-is-an-index.md
-    - name: Vector index
-      href: vector-store.md
-    - name: Knowledge store in Azure Storage
-      href: knowledge-store-concept-intro.md
-    - name: Indexers
-      href: search-indexer-overview.md
-  - name: Applied AI
-    items:
-    - name: AI enrichment during indexing
-      href: cognitive-search-concept-intro.md
-    - name: Built-in vectorization
-      href: vector-search-integrated-vectorization.md
-  - name: Retrieval
+  - name: Connect to a search service
+    href: search-get-started-rbac.md
+  - name: Classic search
     items:
-    - name: Agentic search
-      href: agentic-retrieval-overview.md
     - name: Full-text search
-      href: search-lucene-query-architecture.md
+      items:
+      - name: Portal
+        href: search-get-started-portal.md
+      - name: Programmatic
+        href: search-get-started-text.md
     - name: Vector search
-      href: vector-search-overview.md
-    - name: Hybrid search
-      href: hybrid-search-overview.md
+      items:
+      - name: Portal
+        href: search-get-started-portal-import-vectors.md
+      - name: Programmatic
+        href: search-get-started-vector.md
     - name: Multimodal search
-      href: multimodal-search-overview.md
-    - name: Retrieval Augmented Generation (RAG)
-      href: retrieval-augmented-generation-overview.md
-    - name: Other query types
-      href: search-query-overview.md
-  - name: Relevance
-    href: search-relevance-overview.md
-  - name: Reliability
-    items:
-      - name: Reliability in Azure AI Search
-        href: /azure/reliability/reliability-ai-search?toc=/azure/search/toc.json&bc=/azure/search/breadcrumb/toc.json
-      - name: Multi-region deployment
-        href: search-multi-region.md
-  - name: Security
-    href: search-security-overview.md
-- name: Quickstarts
-  items:
-  - name: Connect to a search service
-    href: search-get-started-rbac.md
-  - name: Agentic search
-    href: search-get-started-agentic-retrieval.md
-  - name: Vector search
-    href: search-get-started-vector.md
-  - name: Classic RAG
-    href: search-get-started-rag.md
-  - name: Full-text search
-    href: search-get-started-text.md
-  - name: Semantic ranking
-    href: search-get-started-semantic.md
-  - name: Chat with your data
-    href: /azure/ai-services/openai/use-your-data-quickstart?context=/azure/search/context/context
-  - name: Azure portal
+      items:
+      - name: Portal
+        href: search-get-started-portal-image-search.md
+    - name: Skillsets (AI enrichment)
+      items:
+      - name: Portal
+        href: search-get-started-skillset.md
+    - name: Semantic ranking
+      items:
+      - name: Programmatic
+        href: search-get-started-semantic.md
+  - name: Agentic retrieval (RAG)
     items:
-    - name: Create an agentic search pipeline
+    - name: Portal
       href: get-started-portal-agentic-retrieval.md
-    - name: Create an index for keyword search
-      href: search-get-started-portal.md
-    - name: Create an index for vector search
-      href: search-get-started-portal-import-vectors.md
-    - name: Create an index for multimodal search
-      href: search-get-started-portal-image-search.md
-    - name: Create a demo app
-      href: search-create-app-portal.md
-    - name: Create a skillset
-      href: search-get-started-skillset.md
-    - name: Create a knowledge store
-      href: knowledge-store-create-portal.md
-    - name: Query with Search Explorer
-      href: search-explorer.md
-  - name: Deployment
+    - name: Programmatic
+      href: search-get-started-agentic-retrieval.md
+
+- name: Setup and management
+  items:
+  - name: Create a search service
     items:
+    - name: Portal
+      href: search-create-service-portal.md
     - name: ARM template
-      displayName: Resource Manager
       href: search-get-started-arm.md
     - name: Bicep
-      displayName: ARM, Resource Manager, Template
       href: search-get-started-bicep.md
     - name: Terraform
       href: search-get-started-terraform.md
-- name: Tutorials
-  items:
-  - name: Dev tutorials
-    items:
-    - name: Add search to static web apps
-      items:
-      - name: Overview
-        href: tutorial-csharp-overview.md
-      - name: Create a search index
-        href: tutorial-csharp-create-load-index.md
-      - name: Deploy static web app
-        href: tutorial-csharp-deploy-static-web-app.md
-      - name: Explore the code
-        href: tutorial-csharp-search-query-integration.md
-  - name: Indexing tutorials
+  - name: Configure a search service
+    href: search-manage.md
+  - name: Quotas, limits, and planning
     items:
-    - name: Index any data
-      href: tutorial-optimize-indexing-push-api.md
-    - name: Index at scale (Apache Spark)
-      href: search-synapseml-cognitive-services.md
-    - name: Index Azure SQL Database
-      href: search-indexer-tutorial.md
-    - name: Index JSON in Azure blobs
-      href: search-semi-structured-data.md
-    - name: Index Markdown in Azure blobs
-      href: search-markdown-data-tutorial.md
-    - name: Index multiple Azure data sources
-      href: tutorial-multiple-data-sources.md
-    - name: Create a custom analyzer
-      href: tutorial-create-custom-analyzer.md
-  - name: Security tutorials
-    items:
-    - name: Index encrypted blobs
-      href: search-how-to-index-azure-blob-encrypted.md
-    - name: Index permissioned ADLS Gen2 files
-      href: tutorial-adls-gen2-indexer-acls.md
-  - name: Multimodal indexing tutorials
-    items:
-    - name: Vectorize images and text
-      href: tutorial-document-extraction-multimodal-embeddings.md
-    - name: Vectorize from a structured document layout
-      href: tutorial-document-layout-multimodal-embeddings.md
-    - name: Verbalize images using generative AI
-      href: tutorial-document-extraction-image-verbalization.md
-    - name: Verbalize images from a structured document layout
-      href: tutorial-document-layout-image-verbalization.md
-  - name: Agentic retrieval tutorial
-    href: agentic-retrieval-how-to-create-pipeline.md
-  - name: Skills tutorials
-    items:
-    - name: Create a skillset
-      href: tutorial-skillset.md
-    - name: Debug a skillset
-      href: cognitive-search-tutorial-debug-sessions.md
-- name: How-to guides
-  items:
-  - name: Service management
-    items:
-    - name: Create a search service
-      href: search-create-service-portal.md
-    - name: Configure a search service
-      href: search-manage.md
-    - name: Choose a region
+    - name: Supported regions
       href: search-region-support.md
-    - name: Choose a tier
+    - name: Supported tiers
       href: search-sku-tier.md
-    - name: Upgrade a service
-      href: search-how-to-upgrade.md
     - name: Service limits
       href: search-limits-quotas-capacity.md
     - name: Plan and manage capacity
       href: search-capacity-planning.md
     - name: Plan and manage costs
       href: search-sku-manage-costs.md
+  - name: Reliability and tenancy
+    items:
+    - name: Reliability
+      href: /azure/reliability/reliability-ai-search?toc=/azure/search/toc.json&bc=/azure/search/breadcrumb/toc.json
+    - name: Multi-region deployment
+      href: search-multi-region.md
     - name: Multi-tenancy
       href: search-modeling-multitenant-saas-applications.md
-    - name: Manage
+  - name: Advanced management
+    items:
+    - name: Manage a service
       items:
-      - name: Manage using PowerShell
+      - name: REST
+        href: search-manage-rest.md
+      - name: PowerShell
         href: search-manage-powershell.md
-      - name: Manage using Azure CLI
+      - name: Azure CLI
         href: search-manage-azure-cli.md
-      - name: Manage using REST
-        href: search-manage-rest.md
-      - name: Move service across regions
-        href: search-howto-move-across-regions.md
-  - name: Indexing
+    - name: Upgrade a service
+      href: search-how-to-upgrade.md
+    - name: Move a service across regions
+      href: search-howto-move-across-regions.md
+
+- name: Classic search
+  items:
+  - name: Indexes
     items:
-    - name: Create an index
+    - name: What is a search index?
+      href: search-what-is-an-index.md
+    - name: What is a vector index?
+      href: vector-store.md
+    - name: Create a search index
       href: search-how-to-create-search-index.md
-    - name: Load an index
-      href: search-how-to-load-search-index.md
-    - name: Update or rebuild an index
-      href: search-howto-reindex.md
-    - name: Manage an index
-      href: search-how-to-manage-index.md
-    - name: Alias an index
-      href: search-how-to-alias.md
-    - name: Import large data sets
-      href: search-how-to-large-index.md
-    - name: Text indexing
+    - name: Create a vector index
+      href: vector-search-how-to-create-index.md
+    - name: Load and manage
+      items:
+      - name: What is data import?
+        href: search-what-is-data-import.md
+      - name: Import data
+        href: search-how-to-load-search-index.md
+      - name: Import large data sets
+        href: search-how-to-large-index.md
+      - name: Manage an index
+        href: search-how-to-manage-index.md
+      - name: Update or rebuild an index
+        href: search-howto-reindex.md
+      - name: Alias an index
+        href: search-how-to-alias.md
+    - name: Index text
       items:
       - name: Add synonyms
         href: search-synonyms.md
@@ -224,10 +148,8 @@ items:
           href: index-add-language-analyzers.md
         - name: Add a custom analyzer
           href: index-add-custom-analyzers.md
-    - name: Vector indexing
+    - name: Index vectors
       items:
-      - name: Create a vector index
-        href: vector-search-how-to-create-index.md
       - name: Chunk documents
         href: vector-search-how-to-chunk-documents.md
       - name: Chunk and vectorize by document layout
@@ -246,33 +168,73 @@ items:
           href: vector-search-how-to-configure-compression-storage.md
         - name: Compress using binary or scalar quantization
           href: vector-search-how-to-quantization.md
-        - name: Index binary data for vector search
+        - name: Index binary data
           href: vector-search-how-to-index-binary-data.md
         - name: Assign narrow data types
           href: vector-search-how-to-assign-narrow-data-types.md
         - name: Eliminate redundant storage
           href: vector-search-how-to-storage-options.md
         - name: Truncate dimensions
           href: vector-search-how-to-truncate-dimensions.md
-  - name: Indexer and enrichment pipelines
+  - name: Indexers and workflows
     items:
     - name: Index via portal wizards
       href: search-import-data-portal.md
-    - name: Logic Apps workflows
-      items:
-      - name: Create a workflow
-        href: search-how-to-index-logic-apps.md
     - name: Indexers
       items:
-      - name: Create an indexer
-        href: search-howto-create-indexers.md
-      - name: Run or reset indexers
-        href: search-howto-run-reset-indexers.md
-      - name: Schedule an indexer
-        href: search-howto-schedule-indexers.md
-      - name: Define field mappings
-        href: search-indexer-field-mappings.md
-      - name: Indexing whole files
+      - name: What is an indexer?
+        href: search-indexer-overview.md
+      - name: Create and manage
+        items:
+        - name: Create an indexer
+          href: search-howto-create-indexers.md
+        - name: Schedule an indexer
+          href: search-howto-schedule-indexers.md
+        - name: Run or reset an indexer
+          href: search-howto-run-reset-indexers.md
+        - name: Define field mappings
+          href: search-indexer-field-mappings.md
+      - name: Index from data sources
+        items:
+        - name: Supported data sources
+          href: search-data-sources-gallery.md
+        - name: Azure Storage
+          items:
+          - name: Search over blobs
+            href: search-blob-storage-integration.md
+          - name: ADLS Gen2
+            href: search-how-to-index-azure-data-lake-storage.md
+          - name: Blobs
+            href: search-how-to-index-azure-blob-storage.md
+          - name: Files
+            href: search-file-storage-integration.md
+          - name: Tables
+            href: search-how-to-index-azure-tables.md
+          - name: Index changed and deleted content
+            href: search-how-to-index-azure-blob-changed-deleted.md
+        - name: Azure Cosmos DB
+          items:
+          - name: Azure Cosmos DB for NoSQL
+            href: search-how-to-index-cosmosdb-sql.md
+          - name: Azure Cosmos DB for MongoDB
+            href: search-how-to-index-cosmosdb-mongodb.md
+          - name: Azure Cosmos DB for Apache Gremlin
+            href: search-how-to-index-cosmosdb-gremlin.md
+        - name: Azure DB for MySQL
+          href: search-how-to-index-mysql.md
+        - name: Azure SQL
+          items:
+          - name: Azure SQL Databases
+            href: search-how-to-index-sql-database.md
+          - name: Azure SQL Managed Instances
+            href: search-how-to-index-sql-managed-instance.md
+          - name: Azure SQL Server VMs
+            href: search-how-to-index-sql-server.md
+        - name: OneLake
+          href: search-how-to-index-onelake-files.md
+        - name: SharePoint in Microsoft 365
+          href: search-how-to-index-sharepoint-online.md
+      - name: Index whole files
         items:
         - name: Content metadata properties
           href: search-blob-metadata-properties.md
@@ -286,164 +248,139 @@ items:
           href: search-how-to-index-azure-blob-json.md
         - name: Index Markdown
           href: search-how-to-index-azure-blob-markdown.md
-      - name: Troubleshooting guidance
-        href: search-indexer-troubleshooting.md
-      - name: Troubleshoot indexer errors and warnings
-        href: cognitive-search-common-errors-warnings.md
-    - name: Data sources (indexers)
-      items:
-      - name: Data sources gallery
-        href: search-data-sources-gallery.md
-      - name: Azure Storage
-        items:
-        - name: Search over blobs
-          href: search-blob-storage-integration.md
-        - name: ADLS Gen2
-          href: search-how-to-index-azure-data-lake-storage.md
-        - name: Blobs
-          href: search-how-to-index-azure-blob-storage.md
-        - name: Files
-          href: search-file-storage-integration.md
-        - name: Tables
-          href: search-how-to-index-azure-tables.md
-        - name: Index changed and deleted content
-          href: search-how-to-index-azure-blob-changed-deleted.md
-      - name: Azure Cosmos DB
+      - name: Troubleshooting
         items:
-        - name: Azure Cosmos DB for NoSQL
-          href: search-how-to-index-cosmosdb-sql.md
-        - name: Azure Cosmos DB for MongoDB
-          href: search-how-to-index-cosmosdb-mongodb.md
-        - name: Azure Cosmos DB for Apache Gremlin
-          href: search-how-to-index-cosmosdb-gremlin.md
-      - name: Azure DB for MySQL
-        href: search-how-to-index-mysql.md
-      - name: Azure SQL
+        - name: Troubleshoot an indexer
+          href: search-indexer-troubleshooting.md
+        - name: Troubleshoot errors and warnings
+          href: cognitive-search-common-errors-warnings.md
+      - name: Tutorials
         items:
-        - name: Azure SQL Databases
-          href: search-how-to-index-sql-database.md
-        - name: Azure SQL Managed Instances
-          href: search-how-to-index-sql-managed-instance.md
-        - name: Azure SQL Server VMs
-          href: search-how-to-index-sql-server.md
-      - name: OneLake
-        href: search-how-to-index-onelake-files.md
-      - name: SharePoint in Microsoft 365
-        href: search-how-to-index-sharepoint-online.md
-    - name: Skillsets (indexers)
-      items:
-      - name: What is a skillset?
-        href: cognitive-search-working-with-skillsets.md
-      - name: Create a skillset
+        - name: Index any data
+          href: tutorial-optimize-indexing-push-api.md
+        - name: Index at scale (Apache Spark)
+          href: search-synapseml-cognitive-services.md
+        - name: Index Azure SQL Database
+          href: search-indexer-tutorial.md
+        - name: Index JSON in Azure blobs
+          href: search-semi-structured-data.md
+        - name: Index Markdown in Azure blobs
+          href: search-markdown-data-tutorial.md
+        - name: Index multiple Azure data sources
+          href: tutorial-multiple-data-sources.md
+        - name: Create a custom analyzer
+          href: tutorial-create-custom-analyzer.md
+    - name: Logic Apps workflows
+      items:
+      - name: Create a workflow
+        href: search-how-to-index-logic-apps.md
+  - name: Skillsets (AI enrichment)
+    items:
+    - name: What is AI enrichment?
+      href: cognitive-search-concept-intro.md
+    - name: What is integrated vectorization?
+      href: vector-search-integrated-vectorization.md
+    - name: What is a skillset?
+      href: cognitive-search-working-with-skillsets.md
+    - name: Create and manage
+      items:
+      - name: Create a skillset (how-to guide)
         href: cognitive-search-defining-skillset.md
-      - name: Design tips
-        href: cognitive-search-concept-troubleshooting.md
+      - name: Create a skillset (tutorial)
+        href: tutorial-skillset.md
       - name: Attach a billable resource
         href: cognitive-search-attach-cognitive-services.md
+      - name: Process image files
+        href: cognitive-search-concept-image-scenarios.md
+      - name: Design tips
+        href: cognitive-search-concept-troubleshooting.md
+    - name: Define projections and mappings
+      items:
       - name: Define an index projection
         href: search-how-to-define-index-projections.md
-      - name: What is a debug session?
-        href: cognitive-search-debug-session.md
-      - name: Debug a skillset
-        href: cognitive-search-how-to-debug-skillset.md
       - name: Reference a skill output
         href: cognitive-search-concept-annotations-syntax.md
       - name: Map to index fields
         href: cognitive-search-output-field-mapping.md
-      - name: Process image files
-        href: cognitive-search-concept-image-scenarios.md
-      - name: Enrichment cache
-        items:
-        - name: Configure an enrichment cache
-          href: enrichment-cache-how-to-configure.md
-        - name: Manage an enrichment cache
-          href: enrichment-cache-how-to-manage.md
-      - name: Generative AI skills
-        items:
-        - name: Add AI-generated content (GenAI Prompt skill)
-          href: chat-completion-skill-example-usage.md
-        - name: Best practices using GenAI Prompt skill
-          href: responsible-ai-best-practices-genai-prompt-skill.md
-      - name: Custom skills
-        items:
-        - name: Add custom skills
-          href: cognitive-search-custom-skill-interface.md
-        - name: Scale out custom skills
-          href: cognitive-search-custom-skill-scale.md
-        - name: Example - Bing Entity Search
-          href: cognitive-search-create-custom-skill-example.md
-        - name: Azure AI Search Power Skills
-          href: https://github.com/Azure-Samples/azure-search-power-skills
-  - name: Retrieval
-    items:
-    - name: Agentic retrieval
+    - name: Debug sessions
+      items:
+      - name: What is a debug session?
+        href: cognitive-search-debug-session.md
+      - name: Debug a skillset (portal)
+        href: cognitive-search-how-to-debug-skillset.md
+      - name: Debug a skillset (tutorial)
+        href: cognitive-search-tutorial-debug-sessions.md
+    - name: Enrichment caches
+      items:
+      - name: Configure an enrichment cache
+        href: enrichment-cache-how-to-configure.md
+      - name: Manage an enrichment cache
+        href: enrichment-cache-how-to-manage.md
+    - name: Knowledge stores
       items:
-      - name: Create an index for agentic retrieval
-        href: agentic-retrieval-how-to-create-index.md
-      - name: Create a knowledge source
+      - name: What is a knowledge store?
+        href: knowledge-store-concept-intro.md
+      - name: Create a knowledge store (REST)
+        href: knowledge-store-create-rest.md
+      - name: Create a knowledge store (portal)
+        href: knowledge-store-create-portal.md
+      - name: Connect with Power BI
+        href: knowledge-store-connect-power-bi.md
+      - name: Projections
         items:
-        - name: What is a knowledge source?
-          href: agentic-knowledge-source-overview.md
-        - name: Azure blob
-          href: agentic-knowledge-source-how-to-blob.md
-        - name: OneLake
-          href: agentic-knowledge-source-how-to-onelake.md
-        - name: Indexed SharePoint
-          href: agentic-knowledge-source-how-to-sharepoint-indexed.md
-        - name: Remote SharePoint
-          href: agentic-knowledge-source-how-to-sharepoint-remote.md
-        - name: Search index
-          href: agentic-knowledge-source-how-to-search-index.md
-        - name: Web
-          href: agentic-knowledge-source-how-to-web.md
-        - name: Manage web access
-          href: agentic-knowledge-source-how-to-web-manage.md
-      - name: Create a knowledge base
-        href: agentic-retrieval-how-to-create-knowledge-base.md
-      - name: Enable answer synthesis
-        href: agentic-retrieval-how-to-answer-synthesis.md
-      - name: Set retrieval reasoning effort
-        href: agentic-retrieval-how-to-set-retrieval-reasoning-effort.md
-      - name: Retrieve data
-        href: agentic-retrieval-how-to-retrieve.md
-      - name: Migrate agentic retrieval code
-        href: agentic-retrieval-how-to-migrate.md
-    - name: Vector search
+        - name: What is a knowledge store projection?
+          href: knowledge-store-projection-overview.md
+        - name: Shape data for projection
+          href: knowledge-store-projection-shape.md
+        - name: Define a projection
+          href: knowledge-store-projections-examples.md
+        - name: Sample shapes and projections
+          href: knowledge-store-projection-example-long.md
+    - name: Generative AI skills
       items:
-      - name: Query vectors
-        href: vector-search-how-to-query.md
-      - name: Use multi-vector fields
-        href: vector-search-multi-vector-fields.md
-      - name: Add a vectorizer for text-to-vector queries
-        displayName: query
-        href: vector-search-how-to-configure-vectorizer.md
-      - name: Filter on vector queries
-        displayName: query
-        href: vector-search-filters.md
-    - name: Keyword search
+      - name: Add AI-generated content (GenAI Prompt skill)
+        href: chat-completion-skill-example-usage.md
+      - name: Best practices for GenAI Prompt skill
+        href: responsible-ai-best-practices-genai-prompt-skill.md
+    - name: Custom skills
+      items:
+      - name: Add a custom skill
+        href: cognitive-search-custom-skill-interface.md
+      - name: Scale out a custom skill
+        href: cognitive-search-custom-skill-scale.md
+      - name: Sample custom skill (Bing Entity Search)
+        href: cognitive-search-create-custom-skill-example.md
+      - name: Azure AI Search Power Skills
+        href: https://github.com/Azure-Samples/azure-search-power-skills
+  - name: Retrieval
+    items:
+    - name: Query with Search Explorer
+      href: search-explorer.md
+    - name: Full-text search
       items:
-      - name: Full-text query
+      - name: What is full-text search?
+        href: search-lucene-query-architecture.md
+      - name: Create a full-text query
         href: search-query-create.md
-      - name: Typeahead query
+      - name: Add autocomplete and suggestions
         href: search-add-autocomplete-suggestions.md
-      - name: Query examples (simple syntax)
-        href: search-query-simple-examples.md
       - name: Add spell check
         href: speller-how-to-add.md
+      - name: Sample queries (simple syntax)
+        href: search-query-simple-examples.md
       - name: Filters and facets
         items:
-        - name: Filters in text queries
-          displayName: query
+        - name: What is a filter?
           href: search-filters.md
-        - name: Understand collection filters
+        - name: What is a collection filter?
           href: search-query-understand-collection-filters.md
-        - name: Troubleshoot collection filters
+        - name: Troubleshoot a collection filter
           href: search-query-troubleshoot-collection-filters.md
         - name: Normalize text for filters
           href: search-normalizers.md
         - name: Add faceted navigation
           href: search-faceted-navigation.md
-        - name: Faceted navigation examples
+        - name: Sample facets
           href: search-faceted-navigation-examples.md
       - name: Search results
         items:
@@ -453,28 +390,62 @@ items:
           href: semantic-answers.md
       - name: Advanced queries
         items:
-        - name: Use full Lucene (examples)
+        - name: Sample queries (Lucene syntax)
           href: search-query-lucene-examples.md
-        - name: Partial terms and special characters
+        - name: Use partial term search
           href: search-query-partial-matching.md
-        - name: Fuzzy search
+        - name: Use fuzzy search
           href: search-query-fuzzy.md
+    - name: Vector search
+      items:
+      - name: What is vector search?
+        href: vector-search-overview.md
+      - name: Create a vector query
+        href: vector-search-how-to-query.md
+      - name: Filter a vector query
+        href: vector-search-filters.md
+      - name: Add a vectorizer
+        href: vector-search-how-to-configure-vectorizer.md
+      - name: Use a multi-vector field
+        href: vector-search-multi-vector-fields.md
     - name: Hybrid search
-      href: hybrid-search-how-to-query.md
-  - name: Ranking
+      items:
+      - name: What is hybrid search?
+        href: hybrid-search-overview.md
+      - name: Create a hybrid query
+        href: hybrid-search-how-to-query.md
+    - name: Multimodal search
+      items:
+      - name: What is multimodal search?
+        href: multimodal-search-overview.md
+      - name: Tutorials
+        items:
+        - name: Vectorize images and text
+          href: tutorial-document-extraction-multimodal-embeddings.md
+        - name: Vectorize from a structured document layout
+          href: tutorial-document-layout-multimodal-embeddings.md
+        - name: Verbalize images using generative AI
+          href: tutorial-document-extraction-image-verbalization.md
+        - name: Verbalize images from a structured document layout
+          href: tutorial-document-layout-image-verbalization.md
+    - name: Other query types
+      href: search-query-overview.md
+  - name: Relevance and ranking
     items:
+    - name: What is relevance?
+      href: search-relevance-overview.md
+    - name: What is vector ranking?
+      href: vector-search-ranking.md
+    - name: What is hybrid ranking (RRF)?
+      href: hybrid-search-ranking.md
+    - name: Add a scoring profile
+      href: index-add-scoring-profiles.md
     - name: BM25 ranking
       items:
       - name: What is BM25 ranking?
         href: index-similarity-and-scoring.md
       - name: Configure BM25 ranking
         href: index-ranking-similarity.md
-    - name: Vector ranking
-      href: vector-search-ranking.md
-    - name: Hybrid ranking (RRF)
-      href: hybrid-search-ranking.md
-    - name: Add a scoring profile
-      href: index-add-scoring-profiles.md
     - name: Semantic ranking
       items:
       - name: What is semantic ranking?
@@ -487,136 +458,193 @@ items:
         href: semantic-how-to-query-request.md
       - name: Rewrite queries with semantic ranker
         href: semantic-how-to-query-rewrite.md
-      - name: Migrate semantic ranking code
-        href: semantic-code-migration.md
       - name: Enable scoring profiles in semantic ranker
         href: semantic-how-to-enable-scoring-profiles.md
-  - name: Security
+      - name: Migrate semantic ranking code
+        href: semantic-code-migration.md
+
+- name: Agentic retrieval (RAG)
+  items:
+  - name: What is agentic retrieval?
+    href: agentic-retrieval-overview.md
+  - name: What is retrieval-augmented generation (RAG)?
+    href: retrieval-augmented-generation-overview.md
+  - name: Knowledge sources
     items:
-    - name: Network access
-      items:
-      - name: Configure network access
-        href: service-configure-firewall.md
-      - name: Create a private endpoint
-        href: service-create-private-endpoint.md
-      - name: Troubleshoot private connections
-        href: troubleshoot-shared-private-link-resources.md
-      - name: Join a network security perimeter
-        href: search-security-network-security-perimeter.md
-    - name: Authentication and authorization
-      items:
-      - name: Enable role-based access
-        href: search-security-enable-roles.md
-      - name: Assign roles (users)
-        href: search-security-rbac.md
-      - name: Assign roles (apps)
-        href: keyless-connections.md
-      - name: Authenticate with keys
-        href: search-security-api-keys.md
-    - name: Outbound connections
-      items:
-      - name: Secure access to external data
-        href: search-indexer-securing-resources.md
-      - name: Configure a managed identity
-        href: search-how-to-managed-identities.md
-      - name: Connect using a managed identity
-        items:
-        - name: Azure Storage
-          href: search-howto-managed-identities-storage.md
-        - name: Azure Cosmos DB
-          href: search-howto-managed-identities-cosmos-db.md
-        - name: SQL Database
-          href: search-howto-managed-identities-sql.md
-        - name: SQL Managed Instance
-          href: search-how-to-index-sql-managed-instance-with-managed-identity.md
-        - name: Connect to an Azure function
-          href: search-howto-managed-identities-azure-functions.md
-      - name: Connect through a firewall
-        href: search-indexer-howto-access-ip-restricted.md
-      - name: Connect as a trusted service
-        href: search-indexer-howto-access-trusted-service-exception.md
-      - name: Connect through a shared private link
-        href: search-indexer-howto-access-private.md
-      - name: Connect to a SQL managed instance private endpoint
-        href: search-indexer-how-to-access-private-sql.md
-    - name: Document-level access
-      items:
-      - name: What is document-level security?
-        href: search-document-level-access-overview.md
-      - name: Use security filters
-        href: search-security-trimming-for-azure-search.md
-      - name: Use ACLs or RBAC scopes
-        items:
-        - name: Push document-level permissions to an index
-          href: search-index-access-control-lists-and-rbac-push-api.md
-        - name: Pull ADLS Gen2 permissions into an index
-          href: search-indexer-access-control-lists-and-role-based-access.md
-        - name: Pull Blob RBAC scopes into an index
-          href: search-blob-indexer-role-based-access.md
-        - name: Pull SharePoint ACL permissions into an index
-          href: search-indexer-sharepoint-access-control-lists.md
-        - name: Query with permission filters
-          href: search-query-access-control-rbac-enforcement.md
-      - name: Preserve sensitivity labels
-        items:
-        - name: Pull Purview sensitivity labels into an index
-          href: search-indexer-sensitivity-labels.md
-        - name: Query honoring sensitivity labels
-          href: search-query-sensitivity-labels.md
-    - name: Data encryption
-      items:
-      - name: Customer-managed keys (CMK)
-        href: search-security-manage-encryption-keys.md
-      - name: Configure cross-tenant CMK
-        href: search-security-managed-encryption-cross-tenant.md
-      - name: Find encrypted objects
-        href: search-security-get-encryption-keys.md
-  - name: Development
+    - name: What is a knowledge source?
+      href: agentic-knowledge-source-overview.md
+    - name: Create an index for agentic retrieval
+      href: agentic-retrieval-how-to-create-index.md
+    - name: Create an indexed source
+      items:
+      - name: Search index
+        href: agentic-knowledge-source-how-to-search-index.md
+      - name: Azure blob
+        href: agentic-knowledge-source-how-to-blob.md
+      - name: OneLake
+        href: agentic-knowledge-source-how-to-onelake.md
+      - name: SharePoint
+        href: agentic-knowledge-source-how-to-sharepoint-indexed.md
+    - name: Create a remote source
+      items:
+      - name: SharePoint
+        href: agentic-knowledge-source-how-to-sharepoint-remote.md
+      - name: Web
+        href: agentic-knowledge-source-how-to-web.md
+      - name: Manage web access
+        href: agentic-knowledge-source-how-to-web-manage.md
+  - name: Knowledge bases and retrieval
+    items:
+    - name: Create a knowledge base
+      href: agentic-retrieval-how-to-create-knowledge-base.md
+    - name: Enable answer synthesis
+      href: agentic-retrieval-how-to-answer-synthesis.md
+    - name: Set retrieval reasoning effort
+      href: agentic-retrieval-how-to-set-retrieval-reasoning-effort.md
+    - name: Retrieve data
+      href: agentic-retrieval-how-to-retrieve.md
+    - name: Build an end-to-end retrieval solution
+      href: agentic-retrieval-how-to-create-pipeline.md
+  - name: Migrate agentic retrieval code
+    href: agentic-retrieval-how-to-migrate.md
+
+- name: Security
+  items:
+  - name: Security in Azure AI Search
+    href: search-security-overview.md
+  - name: Network access
+    items:
+    - name: Configure network access
+      href: service-configure-firewall.md
+    - name: Create a private endpoint
+      href: service-create-private-endpoint.md
+    - name: Troubleshoot a private connection
+      href: troubleshoot-shared-private-link-resources.md
+    - name: Join a network security perimeter
+      href: search-security-network-security-perimeter.md
+  - name: Authentication and authorization
+    items:
+    - name: Enable role-based access
+      href: search-security-enable-roles.md
+    - name: Assign roles (users)
+      href: search-security-rbac.md
+    - name: Assign roles (apps)
+      href: keyless-connections.md
+    - name: Authenticate with keys
+      href: search-security-api-keys.md
+  - name: Outbound connections
+    items:
+    - name: Secure access to external data
+      href: search-indexer-securing-resources.md
+    - name: Configure a managed identity
+      href: search-how-to-managed-identities.md
+    - name: Connect using a managed identity
+      items:
+      - name: Azure Storage
+        href: search-howto-managed-identities-storage.md
+      - name: Azure Cosmos DB
+        href: search-howto-managed-identities-cosmos-db.md
+      - name: SQL Database
+        href: search-howto-managed-identities-sql.md
+      - name: SQL Managed Instance
+        href: search-how-to-index-sql-managed-instance-with-managed-identity.md
+      - name: Connect to an Azure function
+        href: search-howto-managed-identities-azure-functions.md
+    - name: Connect through a firewall
+      href: search-indexer-howto-access-ip-restricted.md
+    - name: Connect through a shared private link
+      href: search-indexer-howto-access-private.md
+    - name: Connect as a trusted service
+      href: search-indexer-howto-access-trusted-service-exception.md
+    - name: Connect to a SQL managed instance private endpoint
+      href: search-indexer-how-to-access-private-sql.md
+  - name: Document-level access
+    items:
+    - name: What is document-level security?
+      href: search-document-level-access-overview.md
+    - name: Use security filters
+      href: search-security-trimming-for-azure-search.md
+    - name: ACLs or RBAC scopes
+      items:
+      - name: Push document-level permissions to an index
+        href: search-index-access-control-lists-and-rbac-push-api.md
+      - name: Pull ADLS Gen2 permissions into an index
+        href: search-indexer-access-control-lists-and-role-based-access.md
+      - name: Pull Blob RBAC scopes into an index
+        href: search-blob-indexer-role-based-access.md
+      - name: Pull SharePoint ACL permissions into an index
+        href: search-indexer-sharepoint-access-control-lists.md
+      - name: Index permissioned ADLS Gen2 files
+        href: tutorial-adls-gen2-indexer-acls.md
+      - name: Query with permission filters
+        href: search-query-access-control-rbac-enforcement.md
+    - name: Sensitivity labels
+      items:
+      - name: Pull Purview sensitivity labels into an index
+        href: search-indexer-sensitivity-labels.md
+      - name: Query honoring sensitivity labels
+        href: search-query-sensitivity-labels.md
+  - name: Data encryption
+    items:
+    - name: Configure customer-managed keys (CMK)
+      href: search-security-manage-encryption-keys.md
+    - name: Configure cross-tenant CMK
+      href: search-security-managed-encryption-cross-tenant.md
+    - name: Find encrypted objects
+      href: search-security-get-encryption-keys.md
+    - name: Index encrypted blobs
+      href: search-how-to-index-azure-blob-encrypted.md
+
+- name: Development
+  items:
+  - name: API versions
+    href: search-api-versions.md
+  - name: Preview features
+    href: search-api-preview.md
+  - name: Develop in .NET
+    href: search-how-to-dotnet-sdk.md
+  - name: Handle concurrent updates
+    href: search-howto-concurrency.md
+  - name: Migration
     items:
-    - name: API versions
-      href: search-api-versions.md
-    - name: Preview features
-      href: search-api-preview.md
     - name: Upgrade the REST API
       href: search-api-migration.md
-    - name: Upgrade .NET libraries
+    - name: Upgrade .NET client libraries
       href: search-dotnet-sdk-migration-version-11.md
-    - name: Develop in .NET
-      href: search-how-to-dotnet-sdk.md
-    - name: Manage with Azure SDKs
+    - name: Upgrade .NET management libraries
       href: search-dotnet-mgmt-sdk-migration.md
-    - name: Handle concurrent updates
-      href: search-howto-concurrency.md
-  - name: Monitoring and performance
-    items:
-    - name: Monitor
-      href: monitor-azure-cognitive-search.md
-    - name: Enable diagnostic logging
-      href: search-monitor-enable-logging.md
-    - name: Monitor queries
-      href: search-monitor-queries.md
-    - name: Monitor indexer-based indexing
-      href: search-monitor-indexers.md
-    - name: Visualize resource logs
-      href: search-monitor-logs-powerbi.md
-    - name: Performance analysis
-      href: search-performance-analysis.md
-    - name: Tips for better performance
-      href: search-performance-tips.md
-  - name: Knowledge store
+  - name: Demo apps
     items:
-    - name: What is a knowledge store projection?
-      href: knowledge-store-projection-overview.md
-    - name: Create using REST
-      href: knowledge-store-create-rest.md
-    - name: Shape data
-      href: knowledge-store-projection-shape.md
-    - name: Define projections
-      href: knowledge-store-projections-examples.md
-    - name: Projection example
-      href: knowledge-store-projection-example-long.md
-    - name: Connect with Power BI
-      href: knowledge-store-connect-power-bi.md
+    - name: Create a demo app
+      href: search-create-app-portal.md
+    - name: Add search to a static web app
+      items:
+      - name: Overview
+        href: tutorial-csharp-overview.md
+      - name: Create a search index
+        href: tutorial-csharp-create-load-index.md
+      - name: Deploy static web app
+        href: tutorial-csharp-deploy-static-web-app.md
+      - name: Explore the code
+        href: tutorial-csharp-search-query-integration.md
+
+- name: Monitoring
+  items:
+  - name: Enable diagnostic logging
+    href: search-monitor-enable-logging.md
+  - name: Monitor data
+    href: monitor-azure-cognitive-search.md
+  - name: Monitor queries
+    href: search-monitor-queries.md
+  - name: Monitor indexer-based indexing
+    href: search-monitor-indexers.md
+  - name: Visualize resource logs
+    href: search-monitor-logs-powerbi.md
+  - name: Analyze search performance
+    href: search-performance-analysis.md
+  - name: Tips for better performance
+    href: search-performance-tips.md
+
 - name: Samples
   items:
   - name: C# samples
@@ -631,19 +659,21 @@ items:
     href: samples-rest.md
   - name: Vector samples
     href: https://github.com/Azure/azure-search-vector-samples
+
 - name: Responsible AI
   items:
   - name: Transparency note
     href: ../ai-foundry/responsible-ai/search/transparency-note.md
+
 - name: References
   items:
-  - name: REST API reference
+  - name: REST API
     items:
-    - name: Search REST API
+    - name: Search Service REST API
       href: /rest/api/searchservice
-    - name: Management REST API
+    - name: Search Management REST API
       href: /rest/api/searchmanagement
-  - name: Azure SDK reference
+  - name: Azure SDK
     items:
     - name: .NET
       items:
@@ -669,23 +699,36 @@ items:
         href: /python/api/overview/azure/search-documents-readme
       - name: azure-mgmt-search
         href: /python/api/azure-mgmt-search/
-  - name: Data reference
+  - name: Resource management
+    items:
+    - name: Azure CLI
+      href: /cli/azure/search
+    - name: Azure PowerShell
+      href: /powershell/module/az.search
+    - name: Azure Resource Manager template
+      href: /azure/templates/microsoft.search/searchservices
+    - name: Azure Policy built-ins
+      displayName: samples, policies, definitions
+      href: ./policy-reference.md
+    - name: Monitoring data reference
+      href: monitor-azure-cognitive-search-data-reference.md
+  - name: Data
     items:
     - name: Data types
       href: /rest/api/searchservice/supported-data-types
     - name: Data types for indexer data sources
       href: /rest/api/searchservice/data-type-map-for-indexers-in-azure-search
-    - name: Stopwords reference
+    - name: Stopwords
       href: reference-stopwords.md
-  - name: Query reference
+  - name: Query
     items:
     - name: Simple query syntax
       href: query-simple-syntax.md
     - name: Full Lucene query syntax
       href: query-lucene-syntax.md
     - name: moreLikeThis
       href: search-more-like-this.md
-    - name: OData language reference
+    - name: OData language
       items:
       - name: Overview
         href: query-odata-filter-orderby-syntax.md
@@ -711,74 +754,54 @@ items:
         href: search-query-odata-search-score-function.md
       - name: OData Language Grammar
         href: search-query-odata-syntax-reference.md
-  - name: Resource management
-    items:
-    - name: Azure CLI
-      href: /cli/azure/search
-    - name: Azure PowerShell
-      href: /powershell/module/az.search
-    - name: Azure Resource Manager template
-      href: /azure/templates/microsoft.search/searchservices
-    - name: Azure Policy built-ins
-      displayName: samples, policies, definitions
-      href: ./policy-reference.md
-    - name: Monitoring data reference
-      href: monitor-azure-cognitive-search-data-reference.md
-  - name: Security reference
-    items:
-    - name: Security controls by Azure Policy
-      displayName: regulatory, compliance, standards, domains
-      href: ./security-controls-policy.md
-    - name: Security baseline
-      href: /security/benchmark/azure/baselines/cognitive-search-security-baseline?toc=/azure/search/TOC.json
-  - name: Skills reference
+  - name: Skills
     items:
     - name: Overview
       href: cognitive-search-predefined-skills.md
     - name: Annotation reference language
       href: cognitive-search-skill-annotation-language.md
     - name: Built-in skills
       items:
-        - name: Microsoft Foundry resource
-          items:
-          - name: Azure Vision multimodal embeddings
-            href: cognitive-search-skill-vision-vectorize.md
-          - name: Document Layout
-            href: cognitive-search-skill-document-intelligence-layout.md
-          - name: Entity Linking (v3)
-            href: cognitive-search-skill-entity-linking-v3.md
-          - name: Entity Recognition (v3)
-            href: cognitive-search-skill-entity-recognition-v3.md
-          - name: Image Analysis
-            href: cognitive-search-skill-image-analysis.md
-          - name: Key Phrase Extraction
-            href: cognitive-search-skill-keyphrases.md
-          - name: Language Detection
-            href: cognitive-search-skill-language-detection.md
-          - name: OCR
-            href: cognitive-search-skill-ocr.md
-          - name: PII Detection
-            href: cognitive-search-skill-pii-detection.md
-          - name: Sentiment (v3)
-            href: cognitive-search-skill-sentiment-v3.md
-          - name: Text Translation
-            href: cognitive-search-skill-text-translation.md
-        - name: Azure-hosted model or resource
-          items:
-          - name: Azure Content Understanding
-            href: cognitive-search-skill-content-understanding.md
-          - name: Azure OpenAI Embedding
-            href: cognitive-search-skill-azure-openai-embedding.md
-          - name: GenAI Prompt
-            href: cognitive-search-skill-genai-prompt.md
+      - name: Microsoft Foundry resource
+        items:
+        - name: Azure Vision multimodal embeddings
+          href: cognitive-search-skill-vision-vectorize.md
+        - name: Document Layout
+          href: cognitive-search-skill-document-intelligence-layout.md
+        - name: Entity Linking (v3)
+          href: cognitive-search-skill-entity-linking-v3.md
+        - name: Entity Recognition (v3)
+          href: cognitive-search-skill-entity-recognition-v3.md
+        - name: Image Analysis
+          href: cognitive-search-skill-image-analysis.md
+        - name: Key Phrase Extraction
+          href: cognitive-search-skill-keyphrases.md
+        - name: Language Detection
+          href: cognitive-search-skill-language-detection.md
+        - name: OCR
+          href: cognitive-search-skill-ocr.md
+        - name: PII Detection
+          href: cognitive-search-skill-pii-detection.md
+        - name: Sentiment (v3)
+          href: cognitive-search-skill-sentiment-v3.md
+        - name: Text Translation
+          href: cognitive-search-skill-text-translation.md
+      - name: Azure-hosted model or resource
+        items:
+        - name: Azure Content Understanding
+          href: cognitive-search-skill-content-understanding.md
+        - name: Azure OpenAI Embedding
+          href: cognitive-search-skill-azure-openai-embedding.md
+        - name: GenAI Prompt
+          href: cognitive-search-skill-genai-prompt.md
     - name: Custom skills
       items:
       - name: Azure Machine Learning (AML)
         href: cognitive-search-aml-skill.md
       - name: Custom Entity Lookup
         href: cognitive-search-skill-custom-entity-lookup.md
       - name: Custom Web API
-        href: cognitive-search-custom-skill-web-api.md 
+        href: cognitive-search-custom-skill-web-api.md
     - name: Utility skills (nonbillable)
       items:
       - name: Conditional
@@ -800,7 +823,7 @@ items:
         href: cognitive-search-skill-entity-recognition.md
       - name: Sentiment (v2)
         href: cognitive-search-skill-sentiment.md
-  - name: Vectorizers reference
+  - name: Vectorizers
     items:
     - name: Microsoft Foundry model catalog
       href: vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md
@@ -810,6 +833,14 @@ items:
       href: vector-search-vectorizer-ai-services-vision.md
     - name: Custom Web API
       href: vector-search-vectorizer-custom-web-api.md
+  - name: Security
+    items:
+    - name: Security controls by Azure Policy
+      displayName: regulatory, compliance, standards, domains
+      href: ./security-controls-policy.md
+    - name: Security baseline
+      href: /security/benchmark/azure/baselines/cognitive-search-security-baseline?toc=/azure/search/TOC.json
+
 - name: Resources
   items:
   - name: Stack Overflow
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCの内容と構造の更新"
}
```

### Explanation
この変更は、`toc.yml`ファイルに対する大幅な修正を伴っています。具体的には、540行の追加と509行の削除が行われ、合計で1049行が変更されました。以下は、変更の概要です。

1. **内容整理**: ドキュメントの目次が整理され、一部の項目が改名され、他の項目が新たに追加されました。例えば、「Azure AI Search Documentation」が「Azure AI Search documentation」と名称変更され、より一貫性のあるスタイルが採用されています。

2. **セクションの追加と再編成**: 新しいトピックが追加され、既存のトピックの下に新しい項目が配置されています。「Quickstart」や「Concepts」などのセクションが明確に整理され、多くのガイドやチュートリアルが新たにリンクされていることが特徴です。

3. **内容の明確化**: 一部の項目名が分かりやすく改訂され、特に「What's Azure AI Search?」や「What's new」といった表現が用いられることで、利用者が検索やリファレンスを行う際に理解しやすくなっています。

4. **リンクの更新**: 新しいリンクが追加され、情報をより効率的に探せるようになっています。また、古いリンクが削除されており、最新の情報に基づいた内容になっています。

この修正により、Azure AI Searchのドキュメント全体の整合性が向上し、ユーザーが必要な情報に迅速にアクセスできるように改善されています。全体として、ドキュメントの使いやすさと可読性が高まっていることが重要なポイントです。


