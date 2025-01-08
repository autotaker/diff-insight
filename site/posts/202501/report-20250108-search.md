---
date: '2025-01-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7840f69...MicrosoftDocs:058aad5
summary: 今回の変更は、主にドキュメントの更新を目的としたもので、新しい情報の追加や既存情報の修正が行われました。特に、ベクトル検索のクイックスタートが初心者に優しい内容になり、認証方法にMicrosoft
  Entraトークンが追加されたことが注目です。セマンティック検索に関するバグ修正や、役割名称の変更も行われ、情報の最新化が進められました。全体として、ユーザーがAzure
  AI関連のサービスを理解しやすくするための大幅な情報更新が実施され、実運用における効率性が向上しました。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7840f69...MicrosoftDocs:058aad5){target="_blank"}

# ハイライト

今回の変更は、主にドキュメントの更新を目的としたものであり、新たな情報の追加や既存情報の修正が含まれています。特に、日付の更新、セマンティック検索のバグ修正、ユーザーロールや認証方法の改善が注目されます。

## 新機能
- ベクトル検索クイックスタートでは、サンプルデータでの使用方法を詳細に説明することで、初心者ユーザーにも理解しやすい内容に。
- ベクトル検索での新しい認証手法として、APIキーに加えて、安全性の高いMicrosoft Entraトークンを推奨。
- クォータとキャパシティに関して、Azureポータルでのリソース確認方法が明示され、より利用者フレンドリーに。

## 破壊的変更
- なし

## その他の更新
- 日付の最新化を通じて、ドキュメントの情報を最新に更新。
- 「Cognitive Services OpenAI User」役割の名称が廃止され、「Cognitive Services User」に変更。
- セマンティック検索の設定から冗長な行を削除し、コードの明確さを向上。

# 洞察

この一連の変更は、Azure AI関連の検索サービスのクイックスタートや関連ドキュメントをユーザーがより理解しやすくするための、大規模な情報更新と整理の一環と考えられます。これにより、従来の設定や使用方法が直感的でシンプルになり、新しいユーザーにもAzure AIサービスの導入や活用が進めやすくなったことが期待できます。

特に注目すべきは、ベクトル検索の改訂です。単なる情報の追加ではなく、新しい技術やベストプラクティスを取り入れることで、ユーザーが最新の検索技術を活用し、より効率的にデータを取得できるように配慮されています。また、Microsoft Entraトークンによるキー不要の接続方法の採用は、セキュリティと利便性の両立を推し進め、ユーザー体験を向上させる重要な変更です。

さらに、クォータやキャパシティの管理について、利用者が直感的にリソースの状態を確認し、効率的に管理できる仕組みを提供することで、実運用におけるパフォーマンスの最適化にも寄与しています。これらの変更は、Azure AIプラットフォームを活用した業務効率化を考慮したユーザー視点での改善として評価できるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [java.md](#item-bd5406) | minor update | Javaクイックスタートの更新日付修正 | modified | 1 | 1 | 2 | 
| [python-semantic.md](#item-4cc2ee) | bug fix | Pythonセマンティック検索の設定修正 | modified | 0 | 1 | 1 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | Cognitive Servicesのユーザーロールの名称変更 | modified | 3 | 3 | 6 | 
| [search-get-started-text.md](#item-935941) | minor update | クイックスタートの更新と日付変更 | modified | 3 | 1 | 4 | 
| [search-get-started-vector.md](#item-4984d9) | minor update | ベクトル検索クイックスタートの改訂 | modified | 684 | 432 | 1116 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | クォータとキャパシティに関する情報の更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/includes/quickstarts/java.md{#item-bd5406}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: include
-ms.date: 11/01/2024
+ms.date: 01/07/2025
 ---
 
 Build a Java console application using the [Azure.Search.Documents](/java/api/overview/azure/search) library to create, load, and query a search index. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaクイックスタートの更新日付修正"
}
```

### Explanation
この変更は、`articles/search/includes/quickstarts/java.md`ファイルにおける日付の更新に関するものです。具体的には、`ms.date`の値が`11/01/2024`から`01/07/2025`に変更されました。この変更は、Javaのクイックスタートガイドのコンテンツにおいて、最新の情報を反映させるための小規模な更新を示しています。総体的には、1行の追加と1行の削除が行われており、内容に影響を与える重要な変更はありませんが、日付の更新は知識の最新化に寄与します。

## articles/search/includes/quickstarts/python-semantic.md{#item-4cc2ee}

<details>
<summary>Diff</summary>
````diff
@@ -106,7 +106,6 @@ semantic_config = SemanticConfiguration(
 # Create the semantic settings with the configuration
 semantic_search = SemanticSearch(configurations=[semantic_config])
 
-semantic_settings = SemanticSearch(configurations=[semantic_config])
 scoring_profiles = []
 suggester = [{'name': 'sg', 'source_fields': ['Tags', 'Address/City', 'Address/Country']}]
 
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "Pythonセマンティック検索の設定修正"
}
```

### Explanation
この変更は、`articles/search/includes/quickstarts/python-semantic.md`ファイルにおけるPythonのセマンティック検索設定に関するものです。具体的には、セマンティック検索の設定である`semantic_settings`の行が削除され、`semantic_search`の初期化のみが残りました。これにより、冗長な設定が排除され、コードの明確さが向上しました。この変更は、正しい動作を確保するためのバグ修正としての重要性を持っています。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -193,12 +193,12 @@ The wizard supports Azure AI Vision image retrieval through multimodal embedding
 
 1. Make sure your Azure AI Search service is in the same region.
 
-1. After the service is deployed, go to the resource and select **Access control** to assign the **Cognitive Services OpenAI User** role to your search service's managed identity. Optionally, you can use key-based authentication for the connection.
+1. After the service is deployed, go to the resource and select **Access control** to assign the **Cognitive Services User** role to your search service's managed identity. Optionally, you can use key-based authentication for the connection.
 
 After you finish these steps, you should be able to select the Azure AI Vision vectorizer in the **Import and vectorize data** wizard.
 
 > [!NOTE]
-> If you can't select an Azure AI Vision vectorizer, make sure you have an Azure AI Vision resource in a supported region. Also make sure that your search service's managed identity has **Cognitive Services OpenAI User** permissions.
+> If you can't select an Azure AI Vision vectorizer, make sure you have an Azure AI Vision resource in a supported region. Also make sure that your search service's managed identity has **Cognitive Services User** permissions.
 
 ### [Azure AI Foundry model catalog](#tab/model-catalog)
 
@@ -331,7 +331,7 @@ Chunking is built in and nonconfigurable. The effective settings are:
 
 1. Specify whether you want your search service to authenticate using an API key or managed identity.
 
-   + The identity should have a **Cognitive Services OpenAI User** role on the Azure AI multi-services account.
+   + The identity should have a **Cognitive Services User** role on the Azure AI multi-services account.
 
 1. Select the checkbox that acknowledges the billing effects of using these resources.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cognitive Servicesのユーザーロールの名称変更"
}
```

### Explanation
この変更は、`articles/search/search-get-started-portal-import-vectors.md`ファイルにおけるAzure AI Vision画像検索に関連するセクションの内容を更新するものです。具体的には、Azure AI Searchサービスの管理アイデンティティに割り当てるべき役割が「Cognitive Services OpenAI User」から「Cognitive Services User」に変更されました。この変更は、正しい役割の指定を反映するもので、手順の正確性を向上させるための小規模な更新です。全体的には、テキストの修正が加わったことで、利用者が適切に役割を割り当てられるようになります。

## articles/search/search-get-started-text.md{#item-935941}

<details>
<summary>Diff</summary>
````diff
@@ -14,13 +14,15 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: quickstart
-ms.date: 11/01/2024
+ms.date: 01/07/2025
 ---
 
 # Quickstart: Full text search using the Azure SDKs
 
 Learn how to use the *Azure.Search.Documents* client library in an Azure SDK to create, load, and query a search index using sample data for [full text search](search-lucene-query-architecture.md). Full text search uses Apache Lucene for indexing and queries, and a BM25 ranking algorithm for scoring results.
 
+This quickstart creates and queries a small hotels-quickstart index containing data about 4 hotels.
+
 This quickstart has steps for the following SDKs:
 
 + [Azure SDK for .NET](?tabs=dotnet#create-load-and-query-an-index)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートの更新と日付変更"
}
```

### Explanation
この変更は、`articles/search/search-get-started-text.md`ファイルに対するもので、Azure SDKを利用したフルテキスト検索に関するクイックスタートの内容を更新しています。主な変更点は、クイックスタートに関する説明の一部が追加され、ホテルに関するデータを含む小規模なインデックス（hotels-quickstart）を作成しクエリを実行することが明示されました。また、文書の日付が「2024年11月01日」から「2025年01月07日」に変更されています。これにより、ユーザーが新しい情報に基づいて最新の手順を利用できるようになります。全体として、クイックスタートの内容が明確になり、ユーザーエクスペリエンスの向上が図られています。

## articles/search/search-get-started-vector.md{#item-4984d9}

<details>
<summary>Diff</summary>
````diff
@@ -26,25 +26,37 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 
 - [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
-- [Azure AI Search](search-what-is-azure-search.md), in any region and on any tier. You can use the Free tier for this quickstart, but Basic or higher is recommended for larger data files. [Create](search-create-service-portal.md) or [find an existing Azure AI Search resource](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) under your current subscription.
+- [Azure AI Search](search-what-is-azure-search.md), in any region and on any tier. [Create](search-create-service-portal.md) or [find an existing Azure AI Search resource](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch) under your current subscription.
+    - You can use the *Free* tier for most of this quickstart, but *Basic* or higher is recommended for larger data files. 
+    - To run the query example that invokes [semantic reranking](semantic-search-overview.md), your search service must be the *Basic* tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
-  Most existing services support vector search. For a small subset of services created prior to January 2019, an index that contains vector fields fails on creation. In this situation, a new service must be created.
 
-- Optionally, to run the query example that invokes [semantic reranking](semantic-search-overview.md), your search service must be the Basic tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
+## Retrieve resource information
 
-## Download files
+Requests to the search endpoint must be authenticated and authorized. You can use API keys or roles for this task. We recommend [using a keyless connection via Microsoft Entra ID](search-get-started-rbac.md).
 
-[Download a REST sample](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) from GitHub to send the requests in this quickstart. For more information, see [Downloading files from GitHub](https://docs.github.com/get-started/start-your-journey/downloading-files-from-github).
+Select the tab that corresponds to your preferred authentication method. Use the same method for all requests in this quickstart.
 
-You can also start a new file on your local system and create requests manually by using the instructions in this article.
+#### [Microsoft Entra ID](#tab/keyless)
 
-## Get a search endpoint and an API key
+1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch).
 
-You can find the search service endpoint and API keys in the Azure portal. You're pasting these values into a `.rest` or `.http` file in the next step.
+1. On the **Overview** home page, find the URL. An example endpoint might look like `https://mydemo.search.windows.net`. 
+
+   :::image type="content" source="media/search-get-started-rest/get-endpoint.png" lightbox="media/search-get-started-rest/get-endpoint.png" alt-text="Screenshot of the URL property on the overview page.":::
+
+1. Follow the steps in the [keyless quickstart](./search-get-started-rbac.md) to get your Microsoft Entra token. 
+
+    You get the token when you run the `az account get-access-token` command in step 3 of the previous quickstart.
+    
+    ```bash
+    az account get-access-token --scope https://search.azure.com/.default --query accessToken --output tsv
+    ```
 
-Requests to the search endpoint must be authenticated and authorized. You can use API keys or roles for this task. Keys are easier to start with, but roles are more secure. Although we use API keys for this quickstart, we recommend [switching to a keyless connection](search-get-started-rbac.md).
+#### [API key](#tab/api-key)
 
-1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
+
+1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch).
 
 1. On the **Overview** home page, find the URL. An example endpoint might look like `https://mydemo.search.windows.net`. 
 
@@ -54,31 +66,55 @@ Requests to the search endpoint must be authenticated and authorized. You can us
 
    :::image type="content" source="media/search-get-started-rest/get-api-key.png" lightbox="media/search-get-started-rest/get-api-key.png" alt-text="Screenshot that shows the API keys in the Azure portal.":::
 
-## Create a vector index
+---
+
+## Create or download the code file
 
-[Create Index (REST)](/rest/api/searchservice/indexes/create) creates a vector index and sets up the physical data structures on your search service.
+You use one `.rest` or `.http` file to run all the requests in this quickstart. You can download the REST file that contains the code for this quickstart, or you can create a new file in Visual Studio Code and copy the code into it.
 
-The index schema is organized around hotel content. Sample data consists of vector and nonvector names and descriptions of seven fictitious hotels. This schema includes configurations for vector indexing and queries, and for semantic ranking.
+1. In Visual Studio Code, create a new file with a `.rest` or `.http` file extension. For example, `az-search-vector-quickstart.rest`. Copy and paste the raw contents of the [Azure-Samples/azure-search-rest-samples/blob/main/Quickstart-vectors/az-search-vector-quickstart.rest](https://raw.githubusercontent.com/Azure-Samples/azure-search-rest-samples/refs/heads/main/Quickstart-vectors/az-search-vector-quickstart.rest) file into this new file. 
 
-1. Create a new text file in Visual Studio Code.
+1. At the top of the file, replace the placeholder value for `@baseUrl` with your search service URL. See the [Retrieve resource information](#retrieve-resource-information) section for instructions on how to find your search service URL.
 
-1. At the top of the file, add variables for the values you collected earlier.
 
    ```http
    @baseUrl = PUT-YOUR-SEARCH-SERVICE-URL-HERE
-   @apiKey = PUT-YOUR-ADMIN-KEY-HERE
    ```
 
-1. Save the file with a `.rest` or `.http` file extension.
+1. At the top of the file, replace the placeholder value for authentication. See the [Retrieve resource information](#retrieve-resource-information) section for instructions on how to get your Microsoft Entra token or API key.
 
-1. Paste in the following example to create the `hotels-vector-quickstart` index on your search service.
+    For the **recommended** keyless authentication via Microsoft Entra ID, you need to replace `@apiKey` with the `@token` variable.
+
+   ```http
+   @token = PUT-YOUR-MICROSOFT-ENTRA-TOKEN-HERE
+   ```
+
+    If you prefer to use an API key, replace `@apiKey` with the key you copied from the Azure portal.
 
     ```http
-    ### Create a new index
-    POST {{baseUrl}}/indexes?api-version=2023-11-01  HTTP/1.1
-        Content-Type: application/json
-        api-key: {{apiKey}}
+    @apiKey = PUT-YOUR-ADMIN-KEY-HERE
+    ```
+
+1. For the **recommended** keyless authentication via Microsoft Entra ID, you need to replace `api-key: {{apiKey}}` with `Authorization: Bearer {{token}}` in the request headers. Replace all instances of `api-key: {{apiKey}}` that you find in the file.
+
+
+## Create a vector index
+
+You use the [Create Index](/rest/api/searchservice/indexes/create) REST API to create a vector index and set up the physical data structures on your search service.
+
+The index schema in this example is organized around hotel content. Sample data consists of vector and nonvector names and descriptions of fictitious hotels. This schema includes configurations for vector indexing and queries, and for semantic ranking.
+
+1. In Visual Studio Code, open the `az-search-vector-quickstart.rest` file you [created earlier](#create-or-download-the-code-file).
+
+1. Find the `### Create a new index` code block in the file. This block contains the request to create the `hotels-vector-quickstart` index on your search service. 
     
+
+    ```http
+    ### Create a new index
+    POST  {{baseUrl}}/indexes?api-version=2023-11-01  HTTP/1.1
+    Content-Type: application/json
+    Authorization: Bearer {{token}}
+
     {
         "name": "hotels-vector-quickstart",
         "fields": [
@@ -125,6 +161,24 @@ The index schema is organized around hotel content. Sample data consists of vect
                 "retrievable": true,
                 "dimensions": 1536,
                 "vectorSearchProfile": "my-vector-profile"
+            },
+                    {
+                "name": "Description_fr", 
+                "type": "Edm.String",
+                "searchable": true, 
+                "filterable": false, 
+                "retrievable": true, 
+                "sortable": false, 
+                "facetable": false,
+                "analyzer": "en.microsoft"
+            },
+            {
+                "name": "Description_frvector",
+                "type": "Collection(Edm.Single)",
+                "searchable": true,
+                "retrievable": true,
+                "dimensions": 1536,
+                "vectorSearchProfile": "my-vector-profile"
             },
             {
                 "name": "Category", 
@@ -143,18 +197,57 @@ The index schema is organized around hotel content. Sample data consists of vect
                 "retrievable": true,
                 "sortable": false,
                 "facetable": true
+            },
+                    {
+                "name": "ParkingIncluded",
+                "type": "Edm.Boolean",
+                "searchable": false,
+                "filterable": true,
+                "retrievable": true,
+                "sortable": true,
+                "facetable": true
+            },
+            {
+                "name": "LastRenovationDate",
+                "type": "Edm.DateTimeOffset",
+                "searchable": false,
+                "filterable": true,
+                "retrievable": true,
+                "sortable": true,
+                "facetable": true
+            },
+            {
+                "name": "Rating",
+                "type": "Edm.Double",
+                "searchable": false,
+                "filterable": true,
+                "retrievable": true,
+                "sortable": true,
+                "facetable": true
             },
             {
                 "name": "Address", 
                 "type": "Edm.ComplexType",
                 "fields": [
+                    {
+                        "name": "StreetAddress", "type": "Edm.String",
+                        "searchable": true, "filterable": false, "retrievable": true, "sortable": false, "facetable": false
+                    },
                     {
                         "name": "City", "type": "Edm.String",
                         "searchable": true, "filterable": true, "retrievable": true, "sortable": true, "facetable": true
                     },
                     {
                         "name": "StateProvince", "type": "Edm.String",
                         "searchable": true, "filterable": true, "retrievable": true, "sortable": true, "facetable": true
+                    },
+                    {
+                        "name": "PostalCode", "type": "Edm.String",
+                        "searchable": true, "filterable": true, "retrievable": true, "sortable": true, "facetable": true
+                    },
+                    {
+                        "name": "Country", "type": "Edm.String",
+                        "searchable": true, "filterable": true, "retrievable": true, "sortable": true, "facetable": true
                     }
                 ]
             },
@@ -180,6 +273,23 @@ The index schema is organized around hotel content. Sample data consists of vect
                         "efSearch": 500,
                         "metric": "cosine"
                     }
+                },
+                {
+                    "name": "my-hnsw-vector-config-2",
+                    "kind": "hnsw",
+                    "hnswParameters": 
+                    {
+                        "m": 4,
+                        "metric": "euclidean"
+                    }
+                },
+                {
+                    "name": "my-eknn-vector-config",
+                    "kind": "exhaustiveKnn",
+                    "exhaustiveKnnParameters": 
+                    {
+                        "metric": "cosine"
+                    }
                 }
             ],
             "profiles": [      
@@ -201,7 +311,7 @@ The index schema is organized around hotel content. Sample data consists of vect
                             { "fieldName": "Description" }
                         ],
                         "prioritizedKeywordsFields": [
-                            { "fieldName": "Tags" }
+                            { "fieldName": "Category" }
                         ]
                     }
                 }
@@ -210,164 +320,272 @@ The index schema is organized around hotel content. Sample data consists of vect
     }
     ```
 
-1. Save the file again, and then select **Send request**. You should have an `HTTP/1.1 201 Created` response. The response body should include the JSON representation of the index schema.
-
-    Key takeaways about this REST API:
-
-    - The `fields` collection includes a required key field and text and vector fields (such as `Description` and `DescriptionVector`) for text and vector search. Colocating vector and nonvector fields in the same index enables hybrid queries. For instance, you can combine filters, text search with semantic ranking, and vectors into a single query operation.
-
-    - Vector fields must be `type: Collection(Edm.Single)` with `dimensions` and `vectorSearchProfile` properties.
-
-    - The `vectorSearch` section is an array of approximate nearest neighbor algorithm configurations and profiles. Supported algorithms include hierarchical navigable small world and exhaustive k-nearest neighbor. For more information, see [Relevance scoring in vector search](vector-search-ranking.md).
-
-    - [Optional]: The `semantic` configuration enables reranking of search results. You can rerank results in queries of type `semantic` for string fields that are specified in the configuration. To learn more, see [Semantic ranking overview](semantic-search-overview.md).
-
-## Upload documents
-
-Creating and loading the index are separate steps. In Azure AI Search, the index contains all searchable data and queries run on the search service. For REST calls, the data is provided as JSON documents. Use [Documents- Index REST API](/rest/api/searchservice/documents/) for this task.
-
-The URI is extended to include the `docs` collection and the `index` operation.
-
-> [!IMPORTANT]
-> The following example isn't runnable code. For readability, we excluded vector values because each one contains 1,536 embeddings, which is too long for this article. If you want to try this step, copy runnable code from the [sample on GitHub](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors).
-
-1. Paste in a valid request that uploads documents, similar to the example below.
-
-1. Save the file, and then select **Send request**. You should have an `HTTP/1.1 201 Created` response. The response body should include the JSON representation of the search documents.
+1. Select **Send request**. You should have an `HTTP/1.1 201 Created` response. 
 
-```http
-### Upload documents
-POST {{baseUrl}}/indexes/hotels-quickstart-vectors/docs/index?api-version=2023-11-01  HTTP/1.1
-Content-Type: application/json
-api-key: {{apiKey}}
+The response body should include the JSON representation of the index schema.
 
+```json
 {
-    "value": [
+    "@odata.context": "https://my-demo-search.search.windows.net/$metadata#indexes/$entity",
+    "@odata.etag": "\"0x8DD2E70E6C36D8E\"",
+    "name": "hotels-vector-quickstart",
+    "defaultScoringProfile": null,
+    "fields": [
+    {
+        "name": "HotelId",
+        "type": "Edm.String",
+        "searchable": false,
+        "filterable": true,
+        "retrievable": true,
+        "sortable": false,
+        "facetable": false,
+        "key": true,
+        "indexAnalyzer": null,
+        "searchAnalyzer": null,
+        "analyzer": null,
+        "dimensions": null,
+        "vectorSearchProfile": null,
+        "synonymMaps": []
+    },
+    [MORE FIELD DEFINITIONS OMITTED FOR BREVITY]
+    ],
+    "scoringProfiles": [],
+    "corsOptions": null,
+    "suggesters": [],
+    "analyzers": [],
+    "tokenizers": [],
+    "tokenFilters": [],
+    "charFilters": [],
+    "encryptionKey": null,
+    "similarity": {
+    "@odata.type": "#Microsoft.Azure.Search.BM25Similarity",
+    "k1": null,
+    "b": null
+    },
+    "vectorSearch": {
+    "algorithms": [
         {
-            "@search.action": "mergeOrUpload",
-            "HotelId": "1",
-            "HotelName": "Stay-Kay City Hotel",
-            "HotelNameVector": [VECTOR ARRAY OMITTED],
-            "Description": 
-                "The hotel is ideally located on the main commercial artery of the city 
-                in the heart of New York.",
-            "DescriptionVector": [VECTOR ARRAY OMITTED],
-            "Category": "Boutique",
-            "Tags": [
-                "pool",
-                "air conditioning",
-                "concierge"
-            ],
+        "name": "my-hnsw-vector-config-1",
+        "kind": "hnsw",
+        "hnswParameters": {
+            "metric": "cosine",
+            "m": 4,
+            "efConstruction": 400,
+            "efSearch": 500
+        },
+        "exhaustiveKnnParameters": null
         },
         {
-            "@search.action": "mergeOrUpload",
-            "HotelId": "2",
-            "HotelName": "Old Century Hotel",
-            "HotelNameVector": [VECTOR ARRAY OMITTED],
-            "Description": 
-                "The hotel is situated in a  nineteenth century plaza, which has been 
-                expanded and renovated to the highest architectural standards to create a modern, 
-                functional and first-class hotel in which art and unique historical elements 
-                coexist with the most modern comforts.",
-            "DescriptionVector": [VECTOR ARRAY OMITTED],
-            "Category": "Boutique",
-            "Tags": [
-                "pool",
-                "air conditioning",
-                "free wifi",
-                "concierge"
-            ]
+        "name": "my-hnsw-vector-config-2",
+        "kind": "hnsw",
+        "hnswParameters": {
+            "metric": "euclidean",
+            "m": 4,
+            "efConstruction": 400,
+            "efSearch": 500
+        },
+        "exhaustiveKnnParameters": null
         },
         {
-            "@search.action": "mergeOrUpload",
-            "HotelId": "3",
-            "HotelName": "Gastronomic Landscape Hotel",
-            "HotelNameVector": [VECTOR ARRAY OMITTED],
-            "Description": 
-                "The Hotel stands out for its gastronomic excellence under the management of 
-                William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
-            "DescriptionVector": [VECTOR ARRAY OMITTED],
-            "Category": "Resort and Spa",
-            "Tags": [
-                "air conditioning",
-                "bar",
-                "continental breakfast"
-            ]
+        "name": "my-eknn-vector-config",
+        "kind": "exhaustiveKnn",
+        "hnswParameters": null,
+        "exhaustiveKnnParameters": {
+            "metric": "cosine"
         }
+        }
+    ],
+    "profiles": [
         {
-            "@search.action": "mergeOrUpload",
-            "HotelId": "4",
-            "HotelName": "Sublime Palace Hotel",
-            "HotelNameVector": [VECTOR ARRAY OMITTED],
-            "Description": 
-                "Sublime Palace Hotel is located in the heart of the historic center of 
-                Sublime in an extremely vibrant and lively area within short walking distance to 
-                the sites and landmarks of the city and is surrounded by the extraordinary beauty 
-                of churches, buildings, shops and monuments. 
-                Sublime Palace is part of a lovingly restored 1800 palace.",
-            "DescriptionVector": [VECTOR ARRAY OMITTED],
-            "Category": "Boutique",
-            "Tags": [
-                "concierge",
-                "view",
-                "24-hour front desk service"
-            ]
-        },
-        {
-            "@search.action": "mergeOrUpload",
-            "HotelId": "13",
-            "HotelName": "Luxury Lion Resort",
-            "HotelNameVector": [VECTOR ARRAY OMITTED],
-            "Description": 
-                "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury 
-                accommodations. Moments from the stadium, we feature the best in comfort",
-            "DescriptionVector": [VECTOR ARRAY OMITTED],
-            "Category": "Resort and Spa",
-            "Tags": [
-                "view",
-                "free wifi",
-                "pool"
-            ]
-        },
+        "name": "my-vector-profile",
+        "algorithm": "my-hnsw-vector-config-1"
+        }
+    ]
+    },
+    "semantic": {
+    "defaultConfiguration": null,
+    "configurations": [
         {
-            "@search.action": "mergeOrUpload",
-            "HotelId": "48",
-            "HotelName": "Nordick's Valley Motel",
-            "HotelNameVector": [VECTOR ARRAY OMITTED],
-            "Description": 
-                "Only 90 miles (about 2 hours) from the nation's capital and nearby 
-                most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring 
-                the caverns?  It's all nearby and we have specially priced packages to help make 
-                our B&B your home base for fun while visiting the valley.",
-            "DescriptionVector": [VECTOR ARRAY OMITTED],
-            "Category": "Boutique",
-            "Tags": [
-                "continental breakfast",
-                "air conditioning",
-                "free wifi"
+        "name": "my-semantic-config",
+        "prioritizedFields": {
+            "titleField": {
+            "fieldName": "HotelName"
+            },
+            "prioritizedContentFields": [
+            {
+                "fieldName": "Description"
+            }
             ],
-        },
-        {
-            "@search.action": "mergeOrUpload",
-            "HotelId": "49",
-            "HotelName": "Swirling Currents Hotel",
-            "HotelNameVector": [VECTOR ARRAY OMITTED],
-            "Description": 
-                "Spacious rooms, glamorous suites and residences, rooftop pool, walking 
-                access to shopping, dining, entertainment and the city center.",
-            "DescriptionVector": [VECTOR ARRAY OMITTED],
-            "Category": "Luxury",
-            "Tags": [
-                "air conditioning",
-                "laundry service",
-                "24-hour front desk service"
+            "prioritizedKeywordsFields": [
+            {
+                "fieldName": "Category"
+            }
             ]
         }
+        }
     ]
+    }
 }
 ```
 
-Key takeaways about this REST API:
+Key takeaways about the [Create Index](/rest/api/searchservice/indexes/create) REST API:
+
+- The `fields` collection includes a required key field and text and vector fields (such as `Description` and `DescriptionVector`) for text and vector search. Colocating vector and nonvector fields in the same index enables hybrid queries. For instance, you can combine filters, text search with semantic ranking, and vectors into a single query operation.
+
+- Vector fields must be `type: Collection(Edm.Single)` with `dimensions` and `vectorSearchProfile` properties.
+
+- The `vectorSearch` section is an array of approximate nearest neighbor algorithm configurations and profiles. Supported algorithms include hierarchical navigable small world and exhaustive k-nearest neighbor. For more information, see [Relevance scoring in vector search](vector-search-ranking.md).
+
+- The (optional) `semantic` configuration enables reranking of search results. You can rerank results in queries of type `semantic` for string fields that are specified in the configuration. To learn more, see [Semantic ranking overview](semantic-search-overview.md).
+
+## Upload documents
+
+Creating and loading the index are separate steps. You created the index schema [in the previous step](#create-a-vector-index). Now you need to load documents into the index.
+ 
+In Azure AI Search, the index contains all searchable data and queries run on the search service. For REST calls, the data is provided as JSON documents. Use [Documents- Index REST API](/rest/api/searchservice/documents/) for this task. The URI is extended to include the `docs` collection and the `index` operation.
+
+1. In Visual Studio Code, open the `az-search-vector-quickstart.rest` file you [created earlier](#create-or-download-the-code-file).
+
+1. Find the `### Upload documents` code block in the file. This block contains the request to upload documents to the `hotels-vector-quickstart` index on your search service.
+
+    ```http
+    ### Upload documents
+    POST {{baseUrl}}/indexes/hotels-quickstart-vectors/docs/index?api-version=2023-11-01  HTTP/1.1
+    Content-Type: application/json
+    Authorization: Bearer {{token}}
+    
+    {
+        "value": [
+            {
+                "@search.action": "mergeOrUpload",
+                "HotelId": "1",
+                "HotelName": "Stay-Kay City Hotel",
+                "HotelNameVector": [VECTOR ARRAY OMITTED],
+                "Description": 
+                    "The hotel is ideally located on the main commercial artery of the city 
+                    in the heart of New York.",
+                "DescriptionVector": [VECTOR ARRAY OMITTED],
+                "Category": "Boutique",
+                "Tags": [
+                    "pool",
+                    "air conditioning",
+                    "concierge"
+                ],
+            },
+            {
+                "@search.action": "mergeOrUpload",
+                "HotelId": "2",
+                "HotelName": "Old Century Hotel",
+                "HotelNameVector": [VECTOR ARRAY OMITTED],
+                "Description": 
+                    "The hotel is situated in a  nineteenth century plaza, which has been 
+                    expanded and renovated to the highest architectural standards to create a modern, 
+                    functional and first-class hotel in which art and unique historical elements 
+                    coexist with the most modern comforts.",
+                "DescriptionVector": [VECTOR ARRAY OMITTED],
+                "Category": "Boutique",
+                "Tags": [
+                    "pool",
+                    "air conditioning",
+                    "free wifi",
+                    "concierge"
+                ]
+            },
+            {
+                "@search.action": "mergeOrUpload",
+                "HotelId": "3",
+                "HotelName": "Gastronomic Landscape Hotel",
+                "HotelNameVector": [VECTOR ARRAY OMITTED],
+                "Description": 
+                    "The Hotel stands out for its gastronomic excellence under the management of 
+                    William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
+                "DescriptionVector": [VECTOR ARRAY OMITTED],
+                "Category": "Resort and Spa",
+                "Tags": [
+                    "air conditioning",
+                    "bar",
+                    "continental breakfast"
+                ]
+            }
+            {
+                "@search.action": "mergeOrUpload",
+                "HotelId": "4",
+                "HotelName": "Sublime Palace Hotel",
+                "HotelNameVector": [VECTOR ARRAY OMITTED],
+                "Description": 
+                    "Sublime Palace Hotel is located in the heart of the historic center of 
+                    Sublime in an extremely vibrant and lively area within short walking distance to 
+                    the sites and landmarks of the city and is surrounded by the extraordinary beauty 
+                    of churches, buildings, shops and monuments. 
+                    Sublime Palace is part of a lovingly restored 1800 palace.",
+                "DescriptionVector": [VECTOR ARRAY OMITTED],
+                "Category": "Boutique",
+                "Tags": [
+                    "concierge",
+                    "view",
+                    "24-hour front desk service"
+                ]
+            },
+            {
+                "@search.action": "mergeOrUpload",
+                "HotelId": "13",
+                "HotelName": "Luxury Lion Resort",
+                "HotelNameVector": [VECTOR ARRAY OMITTED],
+                "Description": 
+                    "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury 
+                    accommodations. Moments from the stadium, we feature the best in comfort",
+                "DescriptionVector": [VECTOR ARRAY OMITTED],
+                "Category": "Resort and Spa",
+                "Tags": [
+                    "view",
+                    "free wifi",
+                    "pool"
+                ]
+            },
+            {
+                "@search.action": "mergeOrUpload",
+                "HotelId": "48",
+                "HotelName": "Nordick's Valley Motel",
+                "HotelNameVector": [VECTOR ARRAY OMITTED],
+                "Description": 
+                    "Only 90 miles (about 2 hours) from the nation's capital and nearby 
+                    most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring 
+                    the caverns?  It's all nearby and we have specially priced packages to help make 
+                    our B&B your home base for fun while visiting the valley.",
+                "DescriptionVector": [VECTOR ARRAY OMITTED],
+                "Category": "Boutique",
+                "Tags": [
+                    "continental breakfast",
+                    "air conditioning",
+                    "free wifi"
+                ],
+            },
+            {
+                "@search.action": "mergeOrUpload",
+                "HotelId": "49",
+                "HotelName": "Swirling Currents Hotel",
+                "HotelNameVector": [VECTOR ARRAY OMITTED],
+                "Description": 
+                    "Spacious rooms, glamorous suites and residences, rooftop pool, walking 
+                    access to shopping, dining, entertainment and the city center.",
+                "DescriptionVector": [VECTOR ARRAY OMITTED],
+                "Category": "Luxury",
+                "Tags": [
+                    "air conditioning",
+                    "laundry service",
+                    "24-hour front desk service"
+                ]
+            }
+        ]
+    }
+    ```
+
+    > [!IMPORTANT]
+    > The code in this example isn't runable. Several characters or lines are removed for brevity. Use the code in your `az-search-vector-quickstart.rest` file to run the request.
+
+1. Select **Send request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search documents.
+
+Key takeaways about the [Documents - Index REST API](/rest/api/searchservice/documents/) request:
 
 - Documents in the payload consist of fields defined in the index schema.
 
@@ -377,32 +595,32 @@ Key takeaways about this REST API:
 
 Now that documents are loaded, you can issue vector queries against them by using [Documents - Search Post (REST)](/rest/api/searchservice/documents/search-post).
 
-There are several queries to demonstrate various patterns:
+In the next sections, we run queries against the `hotels-vector-quickstart` index. The queries include:
 
 - [Single vector search](#single-vector-search)
 - [Single vector search with filter](#single-vector-search-with-filter)
 - [Hybrid search](#hybrid-search)
 - [Semantic hybrid search with filter](#semantic-hybrid-search-with-a-filter)
 
-The vector queries in this section are based on two strings:
+The example vector queries are based on two strings:
 
 - **Search string**: `historic hotel walk to restaurants and shopping`
 - **Vector query string** (vectorized into a mathematical representation): `classic lodging near running trails, eateries, retail`
 
 The vector query string is semantically similar to the search string, but it includes terms that don't exist in the search index. If you do a keyword search for `classic lodging near running trails, eateries, retail`, results are zero. We use this example to show how you can get relevant results even if there are no matching terms.
 
-> [!IMPORTANT]
-> The following examples aren't runnable code. For readability, we excluded vector values because each array contains 1,536 embeddings, which is too long for this article. If you want to try these queries, copy runnable code from the [sample on GitHub](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors).
-
 ### Single vector search
 
-1. Paste in a POST request to query the search index. Save the file. Then select **Send request**. The URI is extended to include the `/docs/search` operator.
+1. In Visual Studio Code, open the `az-search-vector-quickstart.rest` file you [created earlier](#create-or-download-the-code-file).
+
+1. Find the `### Run a single vector query` code block in the file. This block contains the request to query the search index.
+
 
     ```http
-    ### Run a query
+    ### Run a single vector query
     POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2023-11-01  HTTP/1.1
         Content-Type: application/json
-        api-key: {{apiKey}}
+        Authorization: Bearer {{token}}
         
         {
             "count": true,
@@ -421,67 +639,89 @@ The vector query string is semantically similar to the search string, but it inc
         }
     ```
 
-   This vector query is shortened for brevity. The `vectorQueries.vector` contains the vectorized text of the query input, `fields` determines which vector fields are searched, and `k` specifies the number of nearest neighbors to return.
+    This vector query is shortened for brevity. The `vectorQueries.vector` contains the vectorized text of the query input, `fields` determines which vector fields are searched, and `k` specifies the number of nearest neighbors to return.
+
+    The vector query string is `classic lodging near running trails, eateries, retail`, which is vectorized into 1,536 embeddings for this query.
+
+    > [!IMPORTANT]
+    > The code in this example isn't runable. Several characters or lines are removed for brevity. Use the code in your `az-search-vector-quickstart.rest` file to run the request.
 
-   The vector query string is `classic lodging near running trails, eateries, retail`, which is vectorized into 1,536 embeddings for this query.
+1. Select **Send request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
 
-1. Review the response. The response for the vector equivalent of `classic lodging near running trails, eateries, retail` includes seven results. Each result provides a search score and the fields listed in `select`. In a similarity search, the response always includes `k` results ordered by the value similarity score.
+The response for the vector equivalent of `classic lodging near running trails, eateries, retail` includes seven results. Each result provides a search score and the fields listed in `select`. In a similarity search, the response always includes `k` results ordered by the value similarity score.
 
-    ```json
+```json
+{
+  "@odata.context": "https://my-demo-search.search.windows.net/indexes('hotels-vector-quickstart')/$metadata#docs(*)",
+  "@odata.count": 7,
+  "value": [
     {
-        "@odata.context": "https://my-demo-search.search.windows.net/indexes('hotels-vector-quickstart')/$metadata#docs(*)",
-        "@odata.count": 7,
-        "value": [
-            {
-                "@search.score": 0.857736,
-                "HotelName": "Nordick's Valley Motel",
-                "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley."
-            },
-            {
-                "@search.score": 0.8399129,
-                "HotelName": "Swirling Currents Hotel",
-                "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center."
-            },
-            {
-                "@search.score": 0.8383954,
-                "HotelName": "Luxury Lion Resort",
-                "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort"
-            },
-            {
-                "@search.score": 0.8254346,
-                "HotelName": "Sublime Palace Hotel",
-                "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace."
-            },
-            {
-                "@search.score": 0.82380056,
-                "HotelName": "Stay-Kay City Hotel",
-                "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York."
-            },
-            {
-                "@search.score": 0.81514084,
-                "HotelName": "Old Century Hotel",
-                "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts."
-            },
-            {
-                "@search.score": 0.8133763,
-                "HotelName": "Gastronomic Landscape Hotel",
-                "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services."
-            }
-        ]
+      "@search.score": 0.85773647,
+      "HotelId": "48",
+      "HotelName": "Nordick's Motel",
+      "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
+      "Category": "Boutique"
+    },
+    {
+      "@search.score": 0.8399132,
+      "HotelId": "49",
+      "HotelName": "Old Carrabelle Hotel",
+      "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center.",
+      "Category": "Luxury"
+    },
+    {
+      "@search.score": 0.83839583,
+      "HotelId": "13",
+      "HotelName": "Historic Lion Resort",
+      "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort",
+      "Category": "Resort and Spa"
+    },
+    {
+      "@search.score": 0.82543474,
+      "HotelId": "4",
+      "HotelName": "Sublime Cliff Hotel",
+      "Description": "Sublime Cliff Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 1800 palace.",
+      "Category": "Boutique"
+    },
+    {
+      "@search.score": 0.82380104,
+      "HotelId": "1",
+      "HotelName": "Secret Point Hotel",
+      "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York.",
+      "Category": "Boutique"
+    },
+    {
+      "@search.score": 0.8151413,
+      "HotelId": "2",
+      "HotelName": "Twin Dome Hotel",
+      "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
+      "Category": "Boutique"
+    },
+    {
+      "@search.score": 0.8133767,
+      "HotelId": "3",
+      "HotelName": "Triple Landscape Hotel",
+      "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel\u2019s restaurant services.",
+      "Category": "Resort and Spa"
     }
-    ```
+  ]
+}
+```
 
 ### Single vector search with filter
 
 You can add filters, but the filters are applied to the nonvector content in your index. In this example, the filter applies to the `Tags` field to filter out any hotels that don't provide free Wi-Fi.
 
-1. Paste in a POST request to query the search index.
+1. In Visual Studio Code, open the `az-search-vector-quickstart.rest` file you [created earlier](#create-or-download-the-code-file).
+
+1. Find the `### Run a vector query with a filter` code block in the file. This block contains the request to query the search index.
+
 
     ```http
     ### Run a vector query with a filter
     POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2023-11-01  HTTP/1.1
         Content-Type: application/json
-        api-key: {{apiKey}}
+        Authorization: Bearer {{token}}
     
         {
             "count": true,
@@ -500,46 +740,58 @@ You can add filters, but the filters are applied to the nonvector content in you
     }
     ``` 
 
-1. Review the response. The query is the same as the previous example, but it includes a post-processing exclusion filter and returns only the three hotels that have free Wi-Fi.
+    > [!IMPORTANT]
+    > The code in this example isn't runable. Several characters or lines are removed for brevity. Use the code in your `az-search-vector-quickstart.rest` file to run the request.
+
+1. Select **Send request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
+
+The query was the same as the previous [single vector search example](#single-vector-search), but it includes a post-processing exclusion filter and returns only the three hotels that have free Wi-Fi.
 
-    ```json
+```json
+{
+  "@odata.context": "https://my-demo-search.search.windows.net/indexes('hotels-vector-quickstart')/$metadata#docs(*)",
+  "@odata.count": 3,
+  "value": [
     {
-    
-        "@odata.count": 3,
-        "value": [
-            {
-                "@search.score": 0.857736,
-                "HotelName": "Nordick's Valley Motel",
-                "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
-                "Tags": [
-                    "continental breakfast",
-                    "air conditioning",
-                    "free wifi"
-                ]
-            },
-            {
-                "@search.score": 0.8383954,
-                "HotelName": "Luxury Lion Resort",
-                "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort",
-                "Tags": [
-                    "view",
-                    "free wifi",
-                    "pool"
-                ]
-            },
-            {
-                "@search.score": 0.81514084,
-                "HotelName": "Old Century Hotel",
-                "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
-                "Tags": [
-                    "pool",
-                    "free wifi",
-                    "concierge"
-                ]
-            }
-        ]
+      "@search.score": 0.85773647,
+      "HotelId": "48",
+      "HotelName": "Nordick's Motel",
+      "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
+      "Category": "Boutique",
+      "Tags": [
+        "continental breakfast",
+        "air conditioning",
+        "free wifi"
+      ]
+    },
+    {
+      "@search.score": 0.83839583,
+      "HotelId": "13",
+      "HotelName": "Historic Lion Resort",
+      "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort",
+      "Category": "Resort and Spa",
+      "Tags": [
+        "view",
+        "free wifi",
+        "pool"
+      ]
+    },
+    {
+      "@search.score": 0.8151413,
+      "HotelId": "2",
+      "HotelName": "Twin Dome Hotel",
+      "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
+      "Category": "Boutique",
+      "Tags": [
+        "pool",
+        "free wifi",
+        "air conditioning",
+        "concierge"
+      ]
     }
-    ```
+  ]
+}
+```
 
 ### Hybrid search
 
@@ -548,13 +800,16 @@ Hybrid search consists of keyword queries and vector queries in a single search
 - **Search string**: `historic hotel walk to restaurants and shopping`
 - **Vector query string** (vectorized into a mathematical representation): `classic lodging near running trails, eateries, retail`
 
-1. Paste in a POST request to query the search index. Then select **Send request**.
+1. In Visual Studio Code, open the `az-search-vector-quickstart.rest` file you [created earlier](#create-or-download-the-code-file).
+
+1. Find the `### Run a hybrid query` code block in the file. This block contains the request to query the search index.
+
 
     ```http
     ### Run a hybrid query
     POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2023-11-01  HTTP/1.1
         Content-Type: application/json
-        api-key: {{apiKey}}
+        Authorization: Bearer {{token}}
         
     {
         "count": true,
@@ -573,135 +828,142 @@ Hybrid search consists of keyword queries and vector queries in a single search
     }
     ```
 
-   Because this is a hybrid query, results are [ranked by Reciprocal Rank Fusion (RRF)](hybrid-search-ranking.md). RRF evaluates search scores of multiple search results, takes the inverse, and then merges and sorts the combined results. The `top` number of results are returned.
+    > [!IMPORTANT]
+    > The code in this example isn't runable. Several characters or lines are removed for brevity. Use the code in your `az-search-vector-quickstart.rest` file to run the request.
 
-1. Review the response.
+1. Select **Send request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
+   
+Because this is a hybrid query, results are [ranked by Reciprocal Rank Fusion (RRF)](hybrid-search-ranking.md). RRF evaluates search scores of multiple search results, takes the inverse, and then merges and sorts the combined results. The `top` number of results are returned.
 
-    ```json
-    {
-        "@odata.count": 7,
-        "value": [
-            {
-                "@search.score": 0.03279569745063782,
-                "HotelName": "Luxury Lion Resort",
-                "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort"
-            },
-            {
-                "@search.score": 0.03226646035909653,
-                "HotelName": "Sublime Palace Hotel",
-                "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace."
-            },
-            {
-                "@search.score": 0.03226646035909653,
-                "HotelName": "Swirling Currents Hotel",
-                "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center."
-            },
-            {
-                "@search.score": 0.03205128386616707,
-                "HotelName": "Nordick's Valley Motel",
-                "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley."
-            },
-            {
-                "@search.score": 0.03128054738044739,
-                "HotelName": "Gastronomic Landscape Hotel",
-                "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services."
-            },
-            {
-                "@search.score": 0.03100961446762085,
-                "HotelName": "Old Century Hotel",
-                "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts."
-            },
-            {
-                "@search.score": 0.03077651560306549,
-                "HotelName": "Stay-Kay City Hotel",
-                "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York."
-            }
-        ]
-    }
-    ```
+Review the response:
 
-     Because RRF merges results, it helps to review the inputs. The following results are from only the full-text query. The top two results are Sublime Palace Hotel and History Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
+```json
+{
+    "@odata.count": 7,
+    "value": [
+        {
+            "@search.score": 0.03279569745063782,
+            "HotelName": "Luxury Lion Resort",
+            "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort"
+        },
+        {
+            "@search.score": 0.03226646035909653,
+            "HotelName": "Sublime Palace Hotel",
+            "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace."
+        },
+        {
+            "@search.score": 0.03226646035909653,
+            "HotelName": "Swirling Currents Hotel",
+            "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center."
+        },
+        {
+            "@search.score": 0.03205128386616707,
+            "HotelName": "Nordick's Valley Motel",
+            "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley."
+        },
+        {
+            "@search.score": 0.03128054738044739,
+            "HotelName": "Gastronomic Landscape Hotel",
+            "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services."
+        },
+        {
+            "@search.score": 0.03100961446762085,
+            "HotelName": "Old Century Hotel",
+            "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts."
+        },
+        {
+            "@search.score": 0.03077651560306549,
+            "HotelName": "Stay-Kay City Hotel",
+            "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York."
+        }
+    ]
+}
+```
 
-    ```json
-            {
-                "@search.score": 2.2626662,
-                "HotelName": "Sublime Palace Hotel",
-                "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace."
-            },
-            {
-                "@search.score": 0.86421645,
-                "HotelName": "Luxury Lion Resort",
-                "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort"
-                },
-    ```
+Because RRF merges results, it helps to review the inputs. The following results are from only the full-text query. The top two results are Sublime Palace Hotel and History Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
 
-    In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to fourth position. Historic Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
+```json
+{
+    "@search.score": 2.2626662,
+    "HotelName": "Sublime Palace Hotel",
+    "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace."
+},
+{
+    "@search.score": 0.86421645,
+    "HotelName": "Luxury Lion Resort",
+    "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort"
+},
+```
 
-    ```json
-        "value": [
-            {
-                "@search.score": 0.857736,
-                "HotelId": "48",
-                "HotelName": "Nordick's Valley Motel",
-                "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
-                "Category": "Boutique"
-            },
-            {
-                "@search.score": 0.8399129,
-                "HotelId": "49",
-                "HotelName": "Swirling Currents Hotel",
-                "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center.",
-                "Category": "Luxury"
-            },
-            {
-                "@search.score": 0.8383954,
-                "HotelId": "13",
-                "HotelName": "Luxury Lion Resort",
-                "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort",
-                "Category": "Resort and Spa"
-            },
-            {
-                "@search.score": 0.8254346,
-                "HotelId": "4",
-                "HotelName": "Sublime Palace Hotel",
-                "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.",
-                "Category": "Boutique"
-            },
-            {
-                "@search.score": 0.82380056,
-                "HotelId": "1",
-                "HotelName": "Stay-Kay City Hotel",
-                "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York.",
-                "Category": "Boutique"
-            },
-            {
-                "@search.score": 0.81514084,
-                "HotelId": "2",
-                "HotelName": "Old Century Hotel",
-                "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
-                "Category": "Boutique"
-            },
-            {
-                "@search.score": 0.8133763,
-                "HotelId": "3",
-                "HotelName": "Gastronomic Landscape Hotel",
-                "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
-                "Category": "Resort and Spa"
-            }
-        ]
-    ```
+In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to fourth position. Historic Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
+
+```json
+"value": [
+    {
+        "@search.score": 0.857736,
+        "HotelId": "48",
+        "HotelName": "Nordick's Valley Motel",
+        "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
+        "Category": "Boutique"
+    },
+    {
+        "@search.score": 0.8399129,
+        "HotelId": "49",
+        "HotelName": "Swirling Currents Hotel",
+        "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center.",
+        "Category": "Luxury"
+    },
+    {
+        "@search.score": 0.8383954,
+        "HotelId": "13",
+        "HotelName": "Luxury Lion Resort",
+        "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort",
+        "Category": "Resort and Spa"
+    },
+    {
+        "@search.score": 0.8254346,
+        "HotelId": "4",
+        "HotelName": "Sublime Palace Hotel",
+        "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.",
+        "Category": "Boutique"
+    },
+    {
+        "@search.score": 0.82380056,
+        "HotelId": "1",
+        "HotelName": "Stay-Kay City Hotel",
+        "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York.",
+        "Category": "Boutique"
+    },
+    {
+        "@search.score": 0.81514084,
+        "HotelId": "2",
+        "HotelName": "Old Century Hotel",
+        "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
+        "Category": "Boutique"
+    },
+    {
+        "@search.score": 0.8133763,
+        "HotelId": "3",
+        "HotelName": "Gastronomic Landscape Hotel",
+        "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
+        "Category": "Resort and Spa"
+    }
+]
+```
 
 ### Semantic hybrid search with a filter
 
 Here's the last query in the collection. This hybrid query with semantic ranking is filtered to show only the hotels within a 500-kilometer radius of Washington D.C. You can set `vectorFilterMode` to null, which is equivalent to the default (`preFilter` for newer indexes and `postFilter` for older ones).
 
-1. Paste in a POST request to query the search index. Then select **Send request**.
+1. In Visual Studio Code, open the `az-search-vector-quickstart.rest` file you [created earlier](#create-or-download-the-code-file).
+
+1. Find the `### Run a hybrid query with semantic reranking` code block in the file. This block contains the request to query the search index.
 
     ```http
-    ### Run a hybrid query
+    ### Run a hybrid query with semantic reranking
     POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2023-11-01  HTTP/1.1
         Content-Type: application/json
-        api-key: {{apiKey}}
+        Authorization: Bearer {{token}}
 
     {
         "count": true,
@@ -727,88 +989,78 @@ Here's the last query in the collection. This hybrid query with semantic ranking
     }
     ```
 
-1. Review the response. The response is three hotels, which are filtered by location and faceted by `StateProvince` and semantically reranked to promote results that are closest to the search string query (`historic hotel walk to restaurants and shopping`).
+    > [!IMPORTANT]
+    > The code in this example isn't runable. Several characters or lines are removed for brevity. Use the code in your `az-search-vector-quickstart.rest` file to run the request.
+
+1. Select **Send request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
+
+Review the response. The response is three hotels, which are filtered by location and faceted by `StateProvince` and semantically reranked to promote results that are closest to the search string query (`historic hotel walk to restaurants and shopping`).
 
-    The Swirling Currents Hotel now moves into the top spot. Without semantic ranking, Nordick's Valley Motel is number one. With semantic ranking, the machine comprehension models recognize that `historic` applies to "hotel, within walking distance to dining (restaurants) and shopping."
+The Swirling Currents Hotel now moves into the top spot. Without semantic ranking, Nordick's Valley Motel is number one. With semantic ranking, the machine comprehension models recognize that `historic` applies to "hotel, within walking distance to dining (restaurants) and shopping."
 
-    ```json
+```json
+{
+  "@odata.context": "https://my-demo-search.search.windows.net/indexes('hotels-vector-quickstart')/$metadata#docs(*)",
+  "@odata.count": 2,
+  "@search.facets": {
+    "Address/StateProvince": [
+      {
+        "count": 1,
+        "value": "VA"
+      }
+    ]
+  },
+  "@search.answers": [],
+  "value": [
     {
-        "@odata.count": 3,
-        "@search.facets": {
-            "Address/StateProvince": [
-                {
-                    "count": 1,
-                    "value": "NY"
-                },
-                {
-                    "count": 1,
-                    "value": "VA"
-                }
-            ]
-        },
-        "@search.answers": [],
-        "value": [
-            {
-                "@search.score": 0.03306011110544205,
-                "@search.rerankerScore": 2.5094974040985107,
-                "HotelId": "49",
-                "HotelName": "Swirling Currents Hotel",
-                "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center.",
-                "Category": "Luxury",
-                "Address": {
-                    "City": "Arlington",
-                    "StateProvince": "VA"
-                }
-            },
-            {
-                "@search.score": 0.03306011110544205,
-                "@search.rerankerScore": 2.0370211601257324,
-                "HotelId": "48",
-                "HotelName": "Nordick's Valley Motel",
-                "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
-                "Category": "Boutique",
-                "Address": {
-                    "City": "Washington D.C.",
-                    "StateProvince": null
-                }
-            },
-            {
-                "@search.score": 0.032258063554763794,
-                "@search.rerankerScore": 1.6706111431121826,
-                "HotelId": "1",
-                "HotelName": "Stay-Kay City Hotel",
-                "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York.",
-                "Category": "Boutique",
-                "Address": {
-                    "City": "New York",
-                    "StateProvince": "NY"
-                }
-            }
-        ]
+      "@search.score": 0.03306011110544205,
+      "@search.rerankerScore": 2.8773112297058105,
+      "HotelId": "49",
+      "HotelName": "Old Carrabelle Hotel",
+      "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center.",
+      "Category": "Luxury",
+      "Address": {
+        "City": "Arlington",
+        "StateProvince": "VA"
+      }
+    },
+    {
+      "@search.score": 0.03306011110544205,
+      "@search.rerankerScore": 2.1703834533691406,
+      "HotelId": "48",
+      "HotelName": "Nordick's Motel",
+      "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
+      "Category": "Boutique",
+      "Address": {
+        "City": "Washington D.C.",
+        "StateProvince": null
+      }
     }
-    ```
+  ]
+}
+```
 
-    Key takeaways about this REST API:
+Key takeaways about [Documents - Search Post](/rest/api/searchservice/documents/search-post) REST API:
 
-    - Vector search is specified through the `vectors.value` property. Keyword search is specified through the `search` property.
+- Vector search is specified through the `vectors.value` property. Keyword search is specified through the `search` property.
 
-    - In a hybrid search, you can integrate vector search with full-text search over keywords. Filters, spell check, and semantic ranking apply to textual content only, and not vectors. In this final query, there's no semantic `answer` because the system didn't produce one that was sufficiently strong.
+- In a hybrid search, you can integrate vector search with full-text search over keywords. Filters, spell check, and semantic ranking apply to textual content only, and not vectors. In this final query, there's no semantic `answer` because the system didn't produce one that was sufficiently strong.
 
-    - Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
+- Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
 
 ## Clean up
 
 When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
 
 You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
 
-You can also try this `DELETE` command:
+If you want to keep the search service, but delete the index and documents, you can use the `DELETE` command in the REST client. This command (at the end of your `az-search-vector-quickstart.rest` file) deletes the `hotels-vector-quickstart` index:
 
 ```http
 ### Delete an index
 DELETE  {{baseUrl}}/indexes/hotels-vector-quickstart?api-version=2023-11-01 HTTP/1.1
     Content-Type: application/json
-    api-key: {{apiKey}}
+    Authorization: Bearer {{token}}
 ```
 
 ## Next steps
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索クイックスタートの改訂"
}
```

### Explanation
この変更は、`articles/search/search-get-started-vector.md`ファイルに対する大幅な更新であり、Azure AI Searchのベクトル検索に関するクイックスタートガイドを改訂しています。主な変更点は以下の通りです。

1. **内容の追加と修正**: クイックスタートセクションに、サンプルデータベースに基づく小規模なインデックスの作成とクエリに関する詳細を追加しました。特に、ベクトル化検索の使用方法や必要な設定に関する明確な指示が含まれています。

2. **認証方法の選択肢**: APIキーに加えて、Microsoft Entraトークンを使用したキーなしの接続方法が推奨されています。これにより、セキュリティが向上し、ユーザーに柔軟な選択肢を提供します。

3. **新しいインデックス作成手順**: インデックススキーマの詳細に注目し、具体的なフィールドや構成内容が記述され、どのようにベクトルインデックスを作成するかが説明されています。また、インデックスへのドキュメントのアップロード方法も新たに整理されています。

4. **検索クエリの実行方法**: ユーザーが実行する各種検索クエリ（ベクトル検索、ハイブリッド検索など）の処理手順と、その結果を解釈する方法が詳細に説明されています。

これにより、ユーザーはベクトル検索の実装に関してより高い理解を得られるようになっており、実際のデータを使って操作を試すための具体的な手順が示されています。全体として、ドキュメントは最新の情報とベストプラクティスに基づいて大幅に改善されています。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 12/09/2024
+ms.date: 01/07/2025
 ms.custom:
   - references_regions
   - build-2024
@@ -69,7 +69,7 @@ Maximum number of documents per index are:
 + 288 billion on L1
 + 576 billion on L2
 
-Each instance of a complex collection counts as a separate document in terms of these limits.
+You can check the number of documents in the Azure portal and through REST calls that include `search=*` and `count=true`.
 
 Maximum size of each document is approximately 16 megabytes. Document size is actually a limit on the size of the indexing API request payload, which is 16 megabytes. That payload can be a single document, or a batch of documents. For a batch with a single document, the maximum document size is 16 MB of JSON. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータとキャパシティに関する情報の更新"
}
```

### Explanation
この変更は、`articles/search/search-limits-quotas-capacity.md`ファイルに対するもので、Azure AI Searchのクォータおよびキャパシティに関する情報を更新しています。変更の主な内容は以下の通りです。

1. **更新日付の変更**: 文書の日付が「2024年12月09日」から「2025年01月07日」に更新され、最新の情報として扱われています。

2. **新しい情報の追加**: ドキュメントには、新たに「Azureポータルでのドキュメント数確認方法」についての情報が追加されました。REST呼び出しに`search=*`と`count=true`を含めることで、ドキュメントの総数をチェックできることが明記されています。

3. **文言の修正**: 「複雑なコレクションの各インスタンスがこれらの制限における別のドキュメントとしてカウントされる」という記述が削除され、代わりにドキュメント数の確認方法が強調されています。

この変更により、ユーザーはAzure AI Searchのクォータとキャパシティに関する最新の情報をより明確に把握できるようになっています。これにより、システムの使用に関する理解が深まり、適切なリソース管理が促進されることが期待されています。


