---
date: '2025-01-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6c9883f...MicrosoftDocs:1227d31
summary: このコードの差分は、Azure Cognitive SearchおよびAIサービス関連のドキュメントに対する小規模なアップデートです。主な変更点としては、ドキュメントの日付の更新、新情報の追加、既存情報の説明の改善があります。特に、ベクトルフィールドの次元指定やAzure
  AIサービスの設定手順の説明が強化され、ユーザーに対してより最新で明確な情報が提供されています。また、サブドメインの一意性に関する詳細が追加され、チュートリアルには具体的な手順が増補されています。破壊的な変更は確認されていませんが、いくつかのAPI使用法やスキーマについて詳細が追加され、既存の設定に影響を及ぼす可能性があります。最終更新日が統一され、用語の微調整によりユーザーエクスペリエンスも向上しています。この更新は、AzureのAI機能を使ったプロジェクトに従事するエンジニアにとって有益な情報を提供し、実装の手間を軽減する助けとなるでしょう。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6c9883f...MicrosoftDocs:1227d31){target="_blank"}

# ハイライト

このコードの差分は、複数のAzure Cognitive SearchおよびAIサービス関連のドキュメントに対する小規模なアップデートを伴います。主な変更点には、ドキュメントの日付の更新、新しい情報の追加、既存情報の説明の改善があります。特に、ベクトルフィールドの次元指定やAzure AIサービスの設定手順に関する記述が強化され、ユーザーに最新かつ明確な情報が提供されるようになっています。

## 新機能

- サブドメインの一意性に関する詳細が、Azure AIサービスの統合にあたって追加されました。
- チュートリアルには、具体的な手順や設定方法が追加されており、ユーザーの理解を助ける内容が増補されています。

## 破壊的変更

- 特に破壊的な変更は確認されていませんが、いくつかのAPI使用方法やスキーマについて詳細が追加・修正されており、これらが既存の設定に影響を及ぼす可能性があります。

## その他の更新

- 多くのドキュメントで最終更新日が2025年1月9日に統一され、最新の状態が維持されています。
- 用語の微調整により、ユーザーエクスペリエンスが向上しています。

# 洞察

この更新は、Azure Cognitive SearchおよびAIサービスの使用とそのドキュメントの一貫性および最新性を確保するためのものであることが明白です。特に、Azure AIサービスとCognitive Searchの統合を検討しているユーザーにとっては、有用な情報が新たに追加され、また次元の設定やサブドメインの一意性に関する既存の情報がクリアになっています。

実務上、この情報は、AzureのAI機能を使ったプロジェクトに携わるエンジニアにとって有益です。特に、ベクトルフィールドの設定や埋め込みモデルの次元数の一致など、技術的な細部が明確にされており、設計フェーズからデプロイメントにかけての一連のプロセスがより円滑になります。加えて、具体的な実装手順が強化されたことで、導入時のトラブルシューティングや初期設定の手間が軽減されるでしょう。

この更新はまた、Azureプラットフォームを活用したプロジェクトにおける技術的なガイダンスを提供し、今後のAzureサービスとの連携を見据えたインフラストラクチャの構築において非常に有用であるといえます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | 日付の更新とAzure AIサービスのサブドメインに関する情報追加 | modified | 3 | 1 | 4 | 
| [cognitive-search-skill-azure-openai-embedding.md](#item-3eca57) | minor update | 日付の更新と次元設定の説明の改善 | modified | 2 | 2 | 4 | 
| [search-get-started-rag.md](#item-05ff0e) | minor update | クイックスタートガイドの更新と詳細情報の追加 | modified | 71 | 24 | 95 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | ドキュメントのサイズに関する情報の修正 | modified | 0 | 2 | 2 | 
| [tutorial-rag-build-solution-index-schema.md](#item-9a17ca) | minor update | 索引スキーマの説明を強化 | modified | 2 | 0 | 2 | 
| [tutorial-rag-build-solution-pipeline.md](#item-25ce01) | minor update | チュートリアルの日付と内容の微調整 | modified | 2 | 2 | 4 | 
| [tutorial-rag-build-solution-query.md](#item-93965f) | minor update | クエリチュートリアルの構成の修正 | modified | 2 | 8 | 10 | 
| [vector-search-how-to-create-index.md](#item-97c769) | minor update | ベクトルインデックス作成チュートリアルの更新 | modified | 2 | 2 | 4 | 
| [vector-search-vectorizer-ai-services-vision.md](#item-942a3e) | minor update | Azure AI Visionベクトライザのドキュメント修正 | modified | 1 | 1 | 2 | 
| [vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md](#item-ebe7a3) | minor update | Azure AI Foundryモデルカタログのベクトライザのドキュメント修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 01/09/2025
 ---
 
 # Attach an Azure AI multi-service resource to a skillset in Azure AI Search
@@ -57,6 +57,8 @@ Using the Azure portal or newer preview REST APIs and beta SDK packages, you can
 
 As with keys, the details you provide about the Azure AI Services resource are used for billing, not connections.  All API requests made by Azure AI Search to Azure AI services for built-in skills processing continue to be internal and managed by Microsoft.
 
+The subdomain URL must include a unique name (for example, `https://hereismyuniquename.cognitiveservices.azure.com`). If the service was created through the Azure portal, a unique subdomain is automatically generated as part of your service setup. Ensure that your service includes a unique subdomain before using it with the Azure AI Search integration.
+
 ### Example: system-assigned managed identity
 
 Identity is set to null.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新とAzure AIサービスのサブドメインに関する情報追加"
}
```

### Explanation
この変更では、`cognitive-search-attach-cognitive-services.md`ファイルに対して2つの主要な修正が行われました。まず、ドキュメントの日付が2024年11月19日から2025年1月9日に更新されました。次に、Azure AIサービスの統合に関する新しい情報が追加され、具体的には、サブドメインURLが一意である必要があることが記載されました。この情報は、Azureポータルでリソースを作成する際に自動的に生成されることを確認するために重要です。これにより、利用者がAzure AI Search統合を利用する際の実装に関する理解が深まります。

## articles/search/cognitive-search-skill-azure-openai-embedding.md{#item-3eca57}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: reference
-ms.date: 10/16/2024
+ms.date: 01/09/2025
 ---
 
 #	Azure OpenAI Embedding skill
@@ -46,7 +46,7 @@ Parameters are case-sensitive.
 | `deploymentId`   | The name of the deployed Azure OpenAI embedding model. The model should be an embedding model, such as text-embedding-ada-002. See the [List of Azure OpenAI models](/azure/ai-services/openai/concepts/models) for supported models.|
 | `authIdentity`   | A user-managed identity used by the search service for connecting to Azure OpenAI. You can use either a [system or user managed identity](search-howto-managed-identities-data-sources.md). To use a system manged identity, leave `apiKey` and `authIdentity` blank. The system-managed identity is used automatically. A managed identity must have [Cognitive Services OpenAI User](/azure/ai-services/openai/how-to/role-based-access-control#azure-openai-roles) permissions to send text to Azure OpenAI. |
 | `modelName` | This property is required if your skillset is created using the 2024-05-01-preview or 2024-07-01 REST API. Set this property to the deployment name of an Azure OpenAI embedding model deployed on the provider specified through `resourceUri` and identified through `deploymentId`. Currently, the supported values are `text-embedding-ada-002`, `text-embedding-3-large`, and `text-embedding-3-small`.  |
-| `dimensions` | (Optional, introduced in the 2024-05-01-preview REST API). The dimensions of embeddings that you would like to generate if the model supports reducing the embedding dimensions. Supported ranges are listed below. Defaults to the maximum dimensions for each model if not specified. For skillsets created using the 2023-10-01-preview, dimensions are fixed at 1536. |
+| `dimensions` | Optional, starting in the 2024-05-01-preview REST API, the dimensions of embeddings that you would like to generate, assuming the model supports a range of dimensions. Supported ranges are listed below, and currently only apply to the text-embedding-3 model series. The default is the maximum dimensions for each model. For skillsets created using earlier RESt API versions dating back to the 2023-10-01-preview, dimensions are fixed at 1536. When setting the dimensions property on a skill, make sure to set the `dimensions` property on the [vector field definition](vector-search-how-to-create-index.md#add-a-vector-field-to-the-fields-collection) to the same value. |
 
 ## Supported dimensions by `modelName`
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新と次元設定の説明の改善"
}
```

### Explanation
この変更では、`cognitive-search-skill-azure-openai-embedding.md`ファイルに対して2つの重要な修正が行われました。まず、ドキュメントの日付が2024年10月16日から2025年1月9日に更新されました。次に、`dimensions`プロパティに関する説明が改善され、特に新しいAPIバージョンでの使用方法が明確になりました。前の説明から、次元設定がオプションであること、また特定のモデルシリーズにのみ適用されることが強調されています。また、次元プロパティがスキルと同様に、ベクトルフィールド定義で一致させる必要があることも明記されています。これにより、開発者がAzure OpenAI埋め込みスキルをより正確に設定できるようになります。

## articles/search/search-get-started-rag.md{#item-05ff0e}

<details>
<summary>Diff</summary>
````diff
@@ -8,22 +8,34 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: quickstart
-ms.date: 10/14/2024
+ms.date: 01/09/2025
 ---
 
 # Quickstart: Generative search (RAG) with grounding data from Azure AI Search
 
-This quickstart shows you how to send basic and complex queries to a Large Language Model (LLM) for a conversational search experience over your indexed content on Azure AI Search. You use the Azure portal to set up the resources, and then run Python code to call the APIs. 
+This quickstart shows you how to send queries to a chat completion model for a conversational search experience over your indexed content on Azure AI Search. You use the Azure portal to set up the resources, and then run Python code to call the APIs. 
 
 ## Prerequisites
 
-- An Azure subscription. [Create one for free](https://azure.microsoft.com/free/).
+- [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and the [Jupyter package](https://pypi.org/project/jupyter/). For more information, see [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python).
 
-- [Azure AI Search](search-create-service-portal.md), Basic tier or higher so that you can [enable semantic ranker](semantic-how-to-enable-disable.md). Region must be the same one used for Azure OpenAI.
+- An Azure subscription with permissions to assign roles. [Create one for free](https://azure.microsoft.com/free/).
 
-- [Azure OpenAI](https://aka.ms/oai/access) resource with a deployment of `gpt-4o`, `gpt-4o-mini`, or equivalent LLM, in the same region as Azure AI Search.
+- [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource)
 
-- [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and the [Jupyter package](https://pypi.org/project/jupyter/). For more information, see [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python).
+  - [Choose a region](/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#global-standard-model-availability) that supports the chat completion model you want to use (gpt-4o, gpt-4o-mini, or equivalent model). 
+  - [Deploy the chat completion model](/azure/ai-studio/how-to/deploy-models-openai) in Azure AI Foundry or [use another approach](/azure/ai-services/openai/how-to/working-with-models).
+
+- [Azure AI Search](search-create-service-portal.md)
+
+  - Same region as Azure OpenAI.
+  - Basic tier or higher is recommended.
+  - [Enable semantic ranking](semantic-how-to-enable-disable.md).
+  - [Enable role-based access control (see below)](#configure-access).
+
+To meet the same-region requirement, start by reviewing the [regions for the chat model](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability) you want to use. Once you identify a region, confirm that Azure AI Search is available in the [same region](search-region-support.md#azure-public-regions).
+
+Make sure you know the name of the deployed model, and have the endpoints for both Azure resources at hand. You'll provide this information in the steps that follow.
 
 ## Download file
 
@@ -37,20 +49,12 @@ Requests to the search endpoint must be authenticated and authorized. You can us
 
 You're setting up two clients, so you need permissions on both resources.
 
-Azure AI Search is receiving the query request from your local system. Assign yourself the **Search Index Data Reader** role assignment for that task. If you're also creating and loading the hotel sample index, add **Search Service Contributor** and **Search Index Data Contributor** roles as well.
+Azure AI Search is receiving the query request from your local system. Assign yourself the **Search Index Data Reader** role assignment if the hotels sample index already exists. If it doesn't exist, assign yourself **Search Service Contributor** and **Search Index Data Contributor** roles so that you can create and query the index.
 
-Azure OpenAI is receiving the (query) "Can you recommend a few hotels" from your local system, plus its receiving the search results (source) from the search service. Assign yourself and the search service the **Cognitive Services OpenAI User** role.
+Azure OpenAI is receiving the query and the search results from your local system. Assign yourself the **Cognitive Services OpenAI User** role on Azure OpenAI.
 
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
-1. Configure Azure AI Search to use a system-assigned managed identity so that you can you give it role assignments:
-
-    1. In the Azure portal, [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
- 
-    1. On the left menu, select **Settings** > **Identity**.
-
-    1. On the System assigned tab, set status to **On**.
-
 1. Configure Azure AI Search for role-based access:
 
     1. In the Azure portal, find your Azure AI Search service.
@@ -61,20 +65,20 @@ Azure OpenAI is receiving the (query) "Can you recommend a few hotels" from your
 
     1. On the left menu, select **Access control (IAM)**.
 
-    1. On Azure AI Search, make sure you have permissions to create, load, and query a search index:
+    1. On Azure AI Search, select these roles to create, load, and query a search index, and then assign them to your Microsoft Entra ID user identity:
 
        - **Search Index Data Contributor**
        - **Search Service Contributor**
 
-    1. On Azure OpenAI, select **Access control (IAM)** to assign yourself and the search service identity permissions on Azure OpenAI. The code for this quickstart runs locally. Requests to Azure OpenAI originate from your system. Also, search results from the search engine are passed to Azure OpenAI. For these reasons, both you and the search service need permissions on Azure OpenAI.
+    1. On Azure OpenAI, select **Access control (IAM)** to assign this role to yourself on Azure OpenAI:
 
        - **Cognitive Services OpenAI User**
 
 It can take several minutes for permissions to take effect.
 
 ## Create an index
 
-We recommend the hotels-sample-index, which can be created in minutes and runs on any search service tier. This index is created using built-in sample data.
+A search index provides grounding data for the chat model. We recommend the hotels-sample-index, which can be created in minutes and runs on any search service tier. This index is created using built-in sample data.
 
 1. In the Azure portal, [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
 
@@ -90,7 +94,17 @@ We recommend the hotels-sample-index, which can be created in minutes and runs o
 
 1. Select **Edit JSON**. 
 
-1. Search for "semantic" to find the section in the index for a semantic configuration. Replace the empty `"semantic": {}` line with the following semantic configuration. This example specifies a `"defaultConfiguration"`, which is important to the running of this quickstart.
+1. Scroll to the end of the index, where you can find placeholders for constructs that can be added to an index.
+
+   ```json
+   "analyzers": [],
+   "tokenizers": [],
+   "tokenFilters": [],
+   "charFilters": [],
+   "normalizers": [],
+   ```
+
+1. On a new line after "normalizers", paste in the following semantic configuration. This example specifies a `"defaultConfiguration"`, which is important to the running of this quickstart.
 
     ```json
     "semantic":{
@@ -201,6 +215,34 @@ In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Sea
 
 1. On the **Overview** home page, select the link to view the endpoints. Copy the URL. An example endpoint might look like `https://example.openai.azure.com/`.
 
+## Create a virtual environment
+
+In this step, switch back to your local system and Visual Studio Code. We recommend that you create a virtual environment so that you can install the dependencies in isolation.
+
+1. In Visual Studio Code, open the folder containing Quickstart-RAG.ipynb.
+
+1. Press Ctrl-shift-P to open the command palette, search for "Python: Create Environment", and then select `Venv` to create a virtual environment in the current workspace.
+
+1. Select Quickstart-RAG\requirements.txt for the dependencies.
+
+It takes several minutes to create the environment. When the environment is ready, continue to the next step.
+
+## Sign in to Azure
+
+You're using Microsoft Entra ID and role assignments for the connection. Make sure you're logged in to the same tenant and subscription as Azure AI Search and Azure OpenAI. You can use the Azure CLI on the command line to show current properties, change properties, and to sign in. For more information, see [Connect without keys](search-get-started-rbac.md). 
+
+Run each of the following commands in sequence.
+
+```azure-cli
+az account show
+
+az account set --subscription <PUT YOUR SUBSCRIPTION ID HERE>
+
+az login --tenant <PUT YOUR TENANT ID HERE>
+```
+
+You should now be logged in to Azure from your local device.
+
 ## Set up the query and chat thread
 
 This section uses Visual Studio Code and Python to call the chat completion APIs on Azure OpenAI.
@@ -261,18 +303,20 @@ This section uses Visual Studio Code and Python to call the chat completion APIs
     Sources:\n{sources}
     """
     
-    # Query is the question being asked. It's sent to the search engine and the LLM.
+    # Query is the question being asked. It's sent to the search engine and the chat model
     query="Can you recommend a few hotels with complimentary breakfast?"
     
-    # Set up the search results and the chat thread.
-    # Retrieve the selected fields from the search index related to the question.
+    # Search results are created by the search client
+    # Search results are composed of the top 5 results and the fields selected from the search index
+    # Search results include the top 5 matches to your query
     search_results = search_client.search(
         search_text=query,
         top=5,
         select="Description,HotelName,Tags"
     )
     sources_formatted = "\n".join([f'{document["HotelName"]}:{document["Description"]}:{document["Tags"]}' for document in search_results])
     
+    # Send the search results and the query to the LLM to generate a response based on the prompt.
     response = openai_client.chat.completions.create(
         messages=[
             {
@@ -283,6 +327,7 @@ This section uses Visual Studio Code and Python to call the chat completion APIs
         model=AZURE_DEPLOYMENT_MODEL
     )
     
+    # Here is the response from the chat model.
     print(response.choices[0].message.content)
     ```
 
@@ -311,6 +356,8 @@ This section uses Visual Studio Code and Python to call the chat completion APIs
 
     If you get an **Authorization failed** error message, wait a few minutes and try again. It can take several minutes for role assignments to become operational.
 
+    If you get a **Resource not found** error message, check the resource URIs and make sure the API version on the chat model is valid.
+
     Otherwise, to experiment further, change the query and rerun the last step to better understand how the model works with the grounding data.
 
     You can also modify the prompt to change the tone or structure of the output.
@@ -321,7 +368,7 @@ This section uses Visual Studio Code and Python to call the chat completion APIs
 
 Azure AI Search supports [complex types](search-howto-complex-data-types.md) for nested JSON structures. In the hotels-sample-index, `Address` is an example of a complex type, consisting of `Address.StreetAddress`, `Address.City`, `Address.StateProvince`, `Address.PostalCode`, and `Address.Country`. The index also has complex collection of `Rooms` for each hotel.
 
-If your index has complex types, your query can provide those fields if you first convert the search results output to JSON, and then pass the JSON to the LLM. The following example adds complex types to the request. The formatting instructions include a JSON specification.
+If your index has complex types, your query can provide those fields if you first convert the search results output to JSON, and then pass the JSON to the chat model. The following example adds complex types to the request. The formatting instructions include a JSON specification.
 
 ```python
 import json
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートガイドの更新と詳細情報の追加"
}
```

### Explanation
この変更では、`search-get-started-rag.md`ファイルにおいて、クイックスタートガイドの内容が大幅に更新されました。主要な修正点は、ドキュメントの日付が2024年10月14日から2025年1月9日に変更されたこと、そしてAzure AI SearchとAzure OpenAIサービスの設定手順に関する詳細が追加されたことです。

具体的には、クイックスタートの説明が、従来の「大規模言語モデル（LLM）」から「チャット完了モデル」へと変更され、視覚的なツールやモデルのデプロイに関する具体的な手順が強調されました。また、Visual Studio Code内での仮想環境の作成やAzureへのサインイン手順も新たに追加され、利便性が高まりました。

さらに、ユーザーが適切な役割を割り当てられるようにするための詳細情報や、クエリとチャットスレッドの設定方法が改善されています。これにより、よりスムーズにAzure AI SearchとAzure OpenAIを統合した検索体験を構築できるようになります。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -69,8 +69,6 @@ Maximum number of documents per index are:
 + 288 billion on L1
 + 576 billion on L2
 
-You can check the number of documents in the Azure portal and through REST calls that include `search=*` and `count=true`.
-
 Maximum size of each document is approximately 16 megabytes. Document size is actually a limit on the size of the indexing API request payload, which is 16 megabytes. That payload can be a single document, or a batch of documents. For a batch with a single document, the maximum document size is 16 MB of JSON. 
 
 Document size applies to *push mode* indexing that uploads documents to a search service. If you're using an indexer for *pull mode* indexing, your source files can be any file size, subject to [indexer limits](#indexer-limits). For the blob indexer, file size limits are larger for higher tiers. For example, the S1 limit is 128 megabytes, S2 limit is 256 megabytes, and so forth.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントのサイズに関する情報の修正"
}
```

### Explanation
この変更では、`search-limits-quotas-capacity.md`ファイルにおいて、いくつかの小さな修正が行われました。具体的には、最大ドキュメント数に関する説明が変更され、新しい情報が追加されました。2つの行が削除され、Azureポータルでのドキュメント数の確認方法についての言及がなくなりました。

また、ドキュメントの最大サイズに関する情報が明確に強調され、インデックス APIリクエストのペイロードサイズとして最大16メガバイトが参照されています。これは、単一のドキュメントまたはドキュメントのバッチとして送信される場合に適用されます。インデックスのプッシュモードでのインデキシングについての情報も確認でき、プルモードでのインデキシング方法に関する注意事項が記載されています。これにより、ドキュメントサイズの制限に関する理解が深まります。

## articles/search/tutorial-rag-build-solution-index-schema.md{#item-9a17ca}

<details>
<summary>Diff</summary>
````diff
@@ -106,6 +106,8 @@ A minimal index for LLM is designed to store chunks of content. It typically inc
 
    Like the basic schema, it's organized around chunks. The `chunk_id` uniquely identifies each chunk. The `text_vector` field is an embedding of the chunk. The nonvector `chunk` field is a readable string. The `title` maps to a unique metadata storage path for the blobs. The `parent_id` is the only parent-level field, and it's a base64-encoded version of the parent file URI. 
 
+   In integrated vectorization workloads like the one used in this tutorial series, the `dimensions` property on your vector fields should be identical to the number of `dimensions` generated by the embedding skill used to vectorize your data. In this series, we use the Azure OpenAI embedding skill, which calls the text-embedding-3-large model on Azure OpenAI. The skill is specified in the next tutorial. We set dimensions to 1024 in both the vector field and in the skill definition.
+
    The schema also includes a `locations` field for storing generated content that's created by the [indexing pipeline](tutorial-rag-build-solution-pipeline.md).
 
    ```python
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "索引スキーマの説明を強化"
}
```

### Explanation
この変更では、`tutorial-rag-build-solution-index-schema.md`ファイルにおいて、最小限のインデックススキーマに関する説明が追加されました。特に、LLM（Large Language Model）用に設計されたインデックスが、データをベクトル化する際の`dimensions`プロパティについて詳しく説明しています。

新しく追加された情報によれば、統合ベクトル化ワークロードでは、ベクトルフィールドの`dimensions`プロパティは、データをベクトル化するために使用される埋め込みスキルによって生成される`dimensions`の数と一致しなければならないとされています。このチュートリアルシリーズでは、Azure OpenAIの埋め込みスキルが使用され、`text-embedding-3-large`モデルが呼び出されます。また、両方のベクトルフィールドおよびスキル定義において、次元は1024に設定されている旨の説明も含まれています。

さらに、スキーマには`locations`フィールドが追加されており、これはインデクシングパイプラインによって生成されたコンテンツを格納するためのものであることが説明されています。この改訂により、インデックススキーマの理解が深まり、ユーザーがインデクシングパイプラインでのデータの処理についてより良く理解できるようになります。

## articles/search/tutorial-rag-build-solution-pipeline.md{#item-25ce01}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: tutorial
-ms.date: 11/19/2024
+ms.date: 01/09/2025
 ---
 
 # Tutorial: Build an indexing pipeline for RAG on Azure AI Search
@@ -51,7 +51,7 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 
 Open or create a Jupyter notebook (`.ipynb`) in Visual Studio Code to contain the scripts that comprise the pipeline. Initial steps install packages and collect variables for the connections. After you complete the setup steps, you're ready to begin with the components of the indexing pipeline. 
 
-Let's start with the index schema from the [previous tutorial](tutorial-rag-build-solution-index-schema.md). It's organized around vectorized and nonvectorized chunks. It includes a `locations` field that stores AI-generated content created by the skillset.  
+Let's start with the index schema from the [previous tutorial](tutorial-rag-build-solution-index-schema.md). It's organized around vectorized and nonvectorized chunks. It includes a `locations` field that stores AI-generated content created by the skillset.
 
 ```python
 from azure.identity import DefaultAzureCredential
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルの日付と内容の微調整"
}
```

### Explanation
この変更では、`tutorial-rag-build-solution-pipeline.md`ファイルにおいて、いくつかの小さな修正が行われました。主に、ドキュメントの最終更新日が変更されており、2024年11月19日から2025年1月9日に更新されています。これにより、ユーザーに最新の情報を提供しています。

また、パイプラインの構築に関する説明の一部がわずかに変更されており、インデックススキーマに関する内容が明確にされています。特に、インデックススキーマがベクトル化されたチャンクと非ベクトル化されたチャンクを基にして整理されていることや、`locations`フィールドがスキルセットによって作成されたAI生成コンテンツを格納することが強調されています。

このように、特に日付の更新と文章の表現の微調整により、チュートリアルの正確性と読みやすさが向上しています。ユーザーは、インデクシングパイプラインの理解を深めることができるでしょう。

## articles/search/tutorial-rag-build-solution-query.md{#item-93965f}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: tutorial
-ms.date: 10/04/2024
+ms.date: 01/09/2025
 ---
 
 # Tutorial: Search your data using a chat model (RAG in Azure AI Search)
@@ -167,16 +167,10 @@ search_results = search_client.search(
     vector_queries= [vector_query],
     filter="search.ismatch('ice*', 'locations', 'full', 'any')",
     select=["title", "chunk", "locations"],
-    top=5,
+    top=5
 )
 
 sources_formatted = "=================\n".join([f'TITLE: {document["title"]}, CONTENT: {document["chunk"]}, LOCATIONS: {document["locations"]}' for document in search_results])
-
-search_results = search_client.search(
-    search_text=query,
-    top=10,
-    filter="search.ismatch('ice*', 'locations', 'full', 'any')",
-    select="title, chunk, locations"
 ```
 
 Results from the filtered query should now look similar to the following response. Notice the emphasis on ice cover.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリチュートリアルの構成の修正"
}
```

### Explanation
この変更では、`tutorial-rag-build-solution-query.md`ファイルにおいて、主に構成の調整と日付の更新が行われました。具体的には、ドキュメントの最終更新日が2024年10月4日から2025年1月9日に変更されています。これにより、最新の情報が提供されています。

コードの部分では、特に検索クエリの記述に関連する部分に変更が加えられています。一部のコード行が削除され、他のコード行がわずかに修正されました。具体的には、複数の検索クエリの呼び出しが整理されており、`top`パラメータの設定が明示的に示されています。これによって、検索結果の取得方法が簡潔になり、ユーザーがコードを理解しやすくなるとともに、クエリのパフォーマンスが向上する可能性があります。

全体として、この修正により、チュートリアルの内容がより明確になり、ユーザーがAzure AI Searchを活用する際の使いやすさが向上しています。

## articles/search/vector-search-how-to-create-index.md{#item-97c769}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 08/05/2024
+ms.date: 01/09/2025
 ---
 
 # Create a vector index
@@ -281,7 +281,7 @@ Vector fields are characterized by [their data type](/rest/api/searchservice/sup
 1. Define a vector field with the following attributes. You can store one generated embedding per field. For each vector field:
 
    + `type` must be a [vector data types](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields). `Collection(Edm.Single)` is the most common for embedding models.
-   + `dimensions` is the number of dimensions generated by the embedding model. For text-embedding-ada-002, it's 1536.
+   + `dimensions` is the number of dimensions generated by the embedding model. For text-embedding-ada-002, it's fixed at 1536. For the text-embedding-3 model series, there's a range of values. If you're using integrated vectorization and an embedding skill to generate vectors, make sure this property is set to the [same dimensions value](cognitive-search-skill-azure-openai-embedding.md#supported-dimensions-by-modelname) used by the embedding skill.
    + `vectorSearchProfile` is the name of a profile defined elsewhere in the index.
    + `searchable` must be true.
    + `retrievable` can be true or false. True returns the raw vectors (1536 of them) as plain text and consumes storage space. Set to true if you're passing a vector result to a downstream app.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルインデックス作成チュートリアルの更新"
}
```

### Explanation
この変更では、`vector-search-how-to-create-index.md`ファイルに対して微調整が行われました。主な修正点として、ドキュメントの最終更新日が2024年8月5日から2025年1月9日に変更されています。この日付の更新により、読者に最新の情報が提供されるようになっています。

また、ベクトルフィールドに関する説明にも修正が加えられています。具体的には、`dimensions`属性についての記述が強化され、text-embedding-ada-002モデルの次元数が1536で固定されていることが明確に記載されました。さらに、text-embedding-3モデルシリーズにおける次元の範囲についても触れられ、統合ベクトル化と埋め込みスキルを使用する際には、この属性が使用する埋め込みスキルによって設定された次元値と一致する必要があることが述べられています。

このような修正により、ユーザーがAzure AI Searchのベクトルインデックス作成をより理解しやすくなり、正確な情報に基づいた作業が可能となります。全体として、チュートリアルの内容がクリアになり、実践的なガイダンスが強化されています。

## articles/search/vector-search-vectorizer-ai-services-vision.md{#item-942a3e}

<details>
<summary>Diff</summary>
````diff
@@ -38,7 +38,7 @@ The Azure AI Vision vectorizer supports `text`, `imageUrl`, and `imageBinary` ve
 
 ## Expected field dimensions
 
-A field configured with the Azure AI Vision vectorizer should have a dimensions value of 1024.
+A vector field configured with the Azure AI Vision vectorizer should have a dimensions value of 1024.
 
 ## Sample definition
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Visionベクトライザのドキュメント修正"
}
```

### Explanation
この変更では、`vector-search-vectorizer-ai-services-vision.md`ファイルにおいて、一部の表現が修正されました。具体的には、「Azure AI Visionベクトライザで構成されたフィールドは1024の次元値を持つ必要があります」という文が、「Azure AI Visionベクトライザで構成されたベクトルフィールドは1024の次元値を持つ必要があります」という文に変更されました。

この修正により、用語が明確になり、「フィールド」を「ベクトルフィールド」として具体的に表現することで、ユーザーに対してより正確な情報を提供しています。結果として、Azure AI Visionベクトライザの使用方法に関する理解が深まり、読者にとっての情報の明確さが向上しています。全体として、この微調整はユーザー体験を改善するための小さなが重要な更新です。

## articles/search/vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md{#item-ebe7a3}

<details>
<summary>Diff</summary>
````diff
@@ -58,7 +58,7 @@ Which vector query types are supported by the Azure AI Foundry model catalog vec
 
 ## Expected field dimensions
 
-The expected field dimensions for a field configured with an Azure AI Foundry model catalog vectorizer depend on the `modelName` that is configured.
+The expected field dimensions for a vector field configured with an Azure AI Foundry model catalog vectorizer depend on the `modelName` that is configured.
 
 | `modelName` | Expected dimensions |
 |--------------------|-------------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryモデルカタログのベクトライザのドキュメント修正"
}
```

### Explanation
この変更では、`vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md`ファイルの一部表現が修正されました。具体的には、「Azure AI Foundryモデルカタログベクトライザで構成されたフィールドの期待される次元値は、構成された`modelName`に依存する」という文が、「Azure AI Foundryモデルカタログベクトライザで構成されたベクトルフィールドの期待される次元値は、構成された`modelName`に依存する」に変更されました。

この変更により、「フィールド」という用語が「ベクトルフィールド」に具体的に置き換えられ、より明確で一貫した表現が提供されています。これにより、Azure AI Foundryモデルカタログの使用方法に関して読者が理解しやすくなり、情報の精度が向上しています。全体として、この微細なアップデートは、ユーザーエクスペリエンスに貢献する重要な修正です。


