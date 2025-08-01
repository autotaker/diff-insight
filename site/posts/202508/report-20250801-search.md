---
date: '2025-08-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:18e731f...MicrosoftDocs:543d2d6
summary: この更新は、複数のドキュメントに対するマイナーな修正を行い、最新情報を反映させ、ユーザーの理解と体験を向上させることを目的としています。新機能として、一部のドキュメントに新しいセクションや説明が追加され、特にロールと権限についての説明が明確化されました。過去の変更による互換性の問題はなく、具体的な情報の向上や用語の一貫性をもたらす修正も行われています。これにより、Azureサービス利用時の設定や操作が強調され、ユーザーはより適切な判断を下すことができるようになりました。全体として、ドキュメントの可読性が向上し、より効果的なシステムの活用が可能となります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:18e731f...MicrosoftDocs:543d2d6){target="_blank"}

<format>
# Highlights
この更新は、複数のドキュメントに対するマイナーな修正を行い、最新情報を反映させ、ユーザーの理解と体験を向上させることに焦点を当てています。

## New features
- 一部のドキュメント内に新たなセクションや説明を追加し、内容を充実化。
- ユーザーが操作を円滑に行うための役割と権限に関する説明を明確化。

## Breaking changes
- 特に大きな変更はなく、互換性を損なうような更新は見られません。

## Other updates
- 日付やコンテナ名、レスポンスデータなどの具体性を向上。
- 一貫性を持たせるため、文言や用語の細かな修正。

# Insights
この更新では、特にAzureサービスを利用する際の設定や操作方法が強調されています。変更はユーザーの実用性と理解を深めることを狙ったものです。

たとえば、検索ポータルや対応地域における具体的な機能情報が提供され、利用者はより適切な判断を下せるようになっています。また、ロールや権限の明確化により、利用者は必要な権限についての誤解が減少し、効率的にアクセス設定を行えます。APIのレスポンス例の追加は、実装面での理解を助け、期待される出力形式があらかじめ分かることでトラブルシューティングも容易になるでしょう。

さらに技術的な詳細の微調整により、ドキュメント全体の可読性が向上し、應用ソフトウェアのスムーズな展開を可能にしています。従来の説明から一歩進んだこれらの改善により、ユーザーはシステムをより効果的に活用できるようになります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-create-service-portal.md](#item-f90159) | minor update | 検索サービスポータルの更新日付と地域の説明の修正 | modified | 2 | 2 | 4 | 
| [search-region-support.md](#item-25b0f1) | minor update | 地域サポートドキュメントの更新日付と説明の修正 | modified | 3 | 2 | 5 | 
| [tutorial-document-extraction-image-verbalization.md](#item-398a90) | minor update | ドキュメント抽出と画像の言語化チュートリアルの更新 | modified | 17 | 16 | 33 | 
| [tutorial-document-extraction-multimodal-embeddings.md](#item-a3db59) | minor update | マルチモーダル埋め込みドキュメント抽出チュートリアルの更新 | modified | 38 | 38 | 76 | 
| [tutorial-document-layout-image-verbalization.md](#item-f5de57) | minor update | ドキュメントレイアウトと画像の言語化チュートリアルの更新 | modified | 54 | 15 | 69 | 
| [tutorial-document-layout-multimodal-embeddings.md](#item-f67371) | minor update | マルチモーダル埋め込みドキュメントレイアウトチュートリアルの更新 | modified | 57 | 17 | 74 | 


# Modified Contents
## articles/search/search-create-service-portal.md{#item-f90159}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: how-to
-ms.date: 06/11/2025
+ms.date: 07/31/2025
 ms.custom:
   - references_regions
   - build-2024
@@ -104,7 +104,7 @@ If you use multiple Azure services, putting all of them in the same region minim
 
 In most cases, choose a region near you, unless any of the following apply:
 
-+ Your nearest region is [at capacity](search-sku-tier.md#region-availability-by-tier). The Azure portal has the advantage of hiding unavailable regions and tiers during resource setup.
++ Your nearest region is [at capacity](search-region-support.md), which is indicated by the footnotes of each table. The Azure portal has the advantage of hiding unavailable regions and tiers during resource setup.
 
 + You want to use integrated data chunking and vectorization or built-in skills for AI enrichment. Integrated operations have region requirements.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスポータルの更新日付と地域の説明の修正"
}
```

### Explanation
この変更は、`search-create-service-portal.md` ドキュメントに対するマイナーな更新を示しています。具体的には、ドキュメント内の2つのエントリが修正されました。

1. ドキュメントの日付が「06/11/2025」から「07/31/2025」に変更され、更新された内容が正確であることが反映されています。
2. 地域に関する説明文が少し改良され、ユーザーが「あなたの最寄りの地域が[容量に達している](search-region-support.md)」というフレーズで理解しやすくなりました。新しいリンクは、地域のサポート情報を提供するページを指し示しています。

これらの変更により、ドキュメントは最新の情報を保ち、利用者にとっての有用性が向上しています。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Shows supported regions and feature availability across regions for
 author: haileytap
 ms.author: haileytapia
 manager: nitinme
-ms.date: 06/12/2025
+ms.date: 07/31/2025
 ms.service: azure-ai-search
 ms.update-cycle: 90-days
 ms.topic: conceptual
@@ -55,7 +55,8 @@ You can create an Azure AI Search service in any of the following Azure public r
 | West US 3​ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | West Central US​ ​ | ✅ |  | ✅ | ✅ |  |
 
-<sup>1</sup> This region has capacity constraints in all tiers.
+<sup>1</sup> This region has capacity constraints on all tiers.
+
 ### Europe
 
 | Region | AI enrichment | Availability zones | Agentic retrieval | Semantic ranker | Query rewrite |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域サポートドキュメントの更新日付と説明の修正"
}
```

### Explanation
この変更は、`search-region-support.md` ドキュメントに対するマイナーな更新を示しています。主な修正点は以下の通りです。

1. 文書の日付が「06/12/2025」から「07/31/2025」に変更され、より正確な情報を反映させています。
2. 地域に関する注意事項の表記がわずかに調整され、「この地域はすべてのティアにおいて容量制限があります。」という文が「この地域はすべてのティアにおいて容量制限があります。」に変更されています。これにより言葉の明確さが改善されました。
3. 新たに「ヨーロッパ」セクションが追加され、そこには関連する地域と機能の情報が提供されています。

これらの変更により、ドキュメントが最新の状態に保たれ、利用者にとっての理解が向上しています。

## articles/search/tutorial-document-extraction-image-verbalization.md{#item-398a90}

<details>
<summary>Diff</summary>
````diff
@@ -63,7 +63,7 @@ The following instructions apply to Azure Storage which provides the sample data
 
 1. [Create role assignments and specify a managed identity in a connection string](search-howto-managed-identities-storage.md):
 
-   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer and **Storage Blob Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
+   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer. Assign **Storage Blob Data Contributor** and **Storage Table Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
 
    1. For connections made using a system-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
 
@@ -105,11 +105,11 @@ For more information, see [Role-based access control for Azure OpenAI in Azure A
 
 For this tutorial, your local REST client connection to Azure AI Search requires an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Connect to a search service](search-get-started-rbac.md).
 
-For other authenticated connections, the search service uses the role assignments you previously defined.
+For authenticated connections that occur during indexer and skillset processing, the search service uses the role assignments you previously defined.
 
 1. Start Visual Studio Code and create a new file.
 
-1. Provide values for variables used in the request.
+1. Provide values for variables used in the request. For `@storageConnection`, make sure your connection string doesn't have a trailing semicolon or quotation marks. For `@imageProjectionContainer`, provide a container name that's unique in blob storage. Azure AI Search creates this container for you during skills processing.
 
    ```http
    @searchUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
@@ -119,7 +119,7 @@ For other authenticated connections, the search service uses the role assignment
    @openAIKey = PUT-YOUR-OPENAI-KEY-HERE
    @chatCompletionResourceUri = PUT-YOUR-CHAT-COMPLETION-URI-HERE
    @chatCompletionKey = PUT-YOUR-CHAT-COMPLETION-KEY-HERE
-   @imageProjectionContainer=PUT-YOUR-IMAGE-PROJECTION-CONTAINER-HERE (Azure AI Search creates this container for you during skills processing)
+   @imageProjectionContainer=sustainable-ai-pdf-images
    ```
 
 1. Save the file using a `.rest` or `.http` file extension. For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
@@ -147,11 +147,11 @@ POST {{searchUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
     "description": null,
     "type": "azureblob",
     "subtype": null,
-    "credentials": {
-      "connectionString":  "{{storageConnection}}"
+    "credentials":{
+      "connectionString":"{{storageConnection}}"
     },
     "container": {
-      "name": "doc-extraction-image-verbalization-container",
+      "name": "sustainable-ai-pdf",
       "query": null
     },
     "dataChangeDetectionPolicy": null,
@@ -167,7 +167,7 @@ Send the request. The response should look like:
 HTTP/1.1 201 Created
 Transfer-Encoding: chunked
 Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
-Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-image-verbalization-ds')?api-version=2025-05-01-preview -Preview
+Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-05-01-preview -Preview
 Server: Microsoft-IIS/10.0
 Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
 Preference-Applied: odata.include-annotations="*"
@@ -178,16 +178,16 @@ Date: Sat, 26 Apr 2025 21:25:24 GMT
 Connection: close
 
 {
-  "name": "doc-extraction-image-verbalization-ds",
-  "description": "A test datasource",
+  "name": "doc-extraction-multimodal-embedding-ds",
+  "description": null,
   "type": "azureblob",
   "subtype": null,
   "indexerPermissionOptions": [],
   "credentials": {
     "connectionString": null
   },
   "container": {
-    "name": "doc-extraction-multimodality-container",
+    "name": "sustainable-ai-pdf",
     "query": null
   },
   "dataChangeDetectionPolicy": null,
@@ -293,7 +293,7 @@ POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
             {
                 "name": "hnsw",
                 "algorithm": "defaulthnsw",
-                "vectorizer": "{{vectorizer}}"
+                "vectorizer": "demo-vectorizer"
             }
         ],
         "algorithms": [
@@ -309,7 +309,7 @@ POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
         ],
         "vectorizers": [
             {
-              "name": "{{vectorizer}}",
+              "name": "demo-vectorizer",
               "kind": "azureOpenAI",    
               "azureOpenAIParameters": {
                 "resourceUri": "{{openAIResourceUri}}",
@@ -497,7 +497,7 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
     {
       "@odata.type": "#Microsoft.Skills.Util.ShaperSkill",
       "name": "shaper-skill",
-      "description": "Shaper skill to reshape the data to fit the index schema"
+      "description": "Shaper skill to reshape the data to fit the index schema",
       "context": "/document/normalized_images/*",
       "inputs": [
         {
@@ -536,7 +536,7 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
    "indexProjections": {
       "selectors": [
         {
-          "targetIndexName": "{{index}}",
+          "targetIndexName": "doc-extraction-image-verbalization-index",
           "parentKeyFieldName": "text_document_id",
           "sourceContext": "/document/pages/*",
           "mappings": [    
@@ -555,7 +555,7 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
           ]
         },        
         {
-          "targetIndexName": "{{index}}",
+          "targetIndexName": "doc-extraction-image-verbalization-index",
           "parentKeyFieldName": "image_document_id",
           "sourceContext": "/document/normalized_images/*",
           "mappings": [    
@@ -588,6 +588,7 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
   },  
   "knowledgeStore": {
     "storageConnectionString": "{{storageConnection}}",
+    "identity": null,
     "projections": [
       {
         "files": [
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメント抽出と画像の言語化チュートリアルの更新"
}
```

### Explanation
この変更は、`tutorial-document-extraction-image-verbalization.md` ドキュメントに対するマイナーな更新を反映しています。主な修正内容は以下の通りです。

1. **ロールの割り当て説明**: 「Storage Blob Data Contributor」が追加され、ユーザーがナレッジストアの作成とロードができるようになったことが明確化されました。これにより、必要な権限の理解が改善されました。
   
2. **コンテナ名の明確化**: `@imageProjectionContainer` の値がより具体的な名称「sustainable-ai-pdf-images」に置き換えられ、依存関係が明示されています。

3. **API呼び出しのリスポンス変更**: APIレスポンス内のデータソース名が「doc-extraction-image-verbalization-ds」から「doc-extraction-multimodal-embedding-ds」に変更されており、内容がより具体化されました。

4. **インデックスの名前変更**: インデックス名が具体的な名前「doc-extraction-image-verbalization-index」に置き換えられ、ユーザーに対してより一貫性のある指示を提供しています。

5. **技術的詳細の細かな修正**: 一部のコード行で空白や形式に関する調整が行われ、全体として読みやすさと正確性を向上させています。

これらの変更により、チュートリアルは最新の情報を反映し、ユーザーがアプリケーションでの操作を円滑に行えるようサポートしています。

## articles/search/tutorial-document-extraction-multimodal-embeddings.md{#item-a3db59}

<details>
<summary>Diff</summary>
````diff
@@ -39,15 +39,15 @@ This tutorial demonstrates a lower-cost approach for indexing multimodal content
 
 + [Azure AI services multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills). This account provides access to the Azure AI Vision multimodal embedding model used in this tutorial. You must use an Azure AI multi-service account for skillset access to this resource.
 
-+ [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity for connections to Azure Storage and Azure AI Vision. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier. The search service must also be in the same region as your multi-service account.
++ [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity for connections to Azure Storage and Azure AI Vision. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier. 
 
 + [Azure Storage](/azure/storage/common/storage-account-create), used for storing sample data and for creating a [knowledge store](knowledge-store-concept-intro.md).
 
 + [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
 ## Limitations
 
-+ The [Azure AI Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) also has limited regional availability. For an updated list of regions that provide multimodal embeddings, see the [Azure AI Vision documentation](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
++ The [Azure AI Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) has limited regional availability. When you install the multi-service account, choose a region that provides multimodal embeddings. For an updated list of regions that provide multimodal embeddings, see the [Azure AI Vision documentation](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
 
 ## Prepare data
 
@@ -61,7 +61,7 @@ The following instructions apply to Azure Storage which provides the sample data
 
 1. [Create role assignments and specify a managed identity in a connection string](search-howto-managed-identities-storage.md):
 
-   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer and **Storage Blob Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
+   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer. Assign **Storage Blob Data Contributor** and **Storage Table Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
 
    1. For connections made using a system-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
 
@@ -101,20 +101,19 @@ This tutorial assumes you have an existing Azure AI multiservice account through
 
 For this tutorial, your local REST client connection to Azure AI Search requires an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Connect to a search service](search-get-started-rbac.md).
 
-For other authenticated connections, the search service uses the role assignments you previously defined.
+For authenticated connections that occur during indexer and skillset processing, the search service uses the role assignments you previously defined.
 
 1. Start Visual Studio Code and create a new file.
 
-1. Provide values for variables used in the request.
+1. Provide values for variables used in the request. For `@storageConnection`, make sure your connection string doesn't have a trailing semicolon or quotation marks. For `@imageProjectionContainer`, provide a container name that's unique in blob storage. Azure AI Search creates this container for you during skills processing.
 
    ```http
-   @searchUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
-   @searchsearchApiKey = PUT-YOUR-ADMIN-API-KEY-HERE
-   @storageConnection = PUT-YOUR-STORAGE-CONNECTION-STRING-HERE
-   @cognitiveServicesUrl = PUT-YOUR-COGNITIVE-SERVICES-URL-HERE
-   @cognitiveServicesKey= PUT-YOUR-COGNITIVE-SERVICES-URL-KEY-HERE
-   @modelVersion = PUT-YOUR-VECTORIZE-MODEL-VERSION-HERE
-   @imageProjectionContainer=PUT-YOUR-IMAGE-PROJECTION-CONTAINER-HERE (Azure AI Search creates this container for you during skills processing)
+    @searchUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
+    @searchApiKey = PUT-YOUR-ADMIN-API-KEY-HERE
+    @storageConnection = PUT-YOUR-STORAGE-CONNECTION-STRING-HERE
+    @cognitiveServicesUrl = PUT-YOUR-AZURE-AI-MULTI-SERVICE-ENDPOINT-HERE
+    @modelVersion = 2023-04-15
+    @imageProjectionContainer=sustainable-ai-pdf-images
    ```
 
 1. Save the file using a `.rest` or `.http` file extension. For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
@@ -132,28 +131,27 @@ To get the Azure AI Search endpoint and API key:
 [Create Data Source (REST)](/rest/api/searchservice/data-sources/create) creates a data source connection that specifies what data to index.
 
 ```http
-### Create a data source
 POST {{searchUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
-  {
-    "name": "doc-extraction-multimodal-embedding-ds",
-    "description": null,
-    "type": "azureblob",
-    "subtype": null,
-    "credentials": {
-      "connectionString":  "{{storageConnection}}"
-    },
-    "container": {
-      "name": "doc-extraction-multimodality-container",
-      "query": null
-    },
-    "dataChangeDetectionPolicy": null,
-    "dataDeletionDetectionPolicy": null,
-    "encryptionKey": null,
-    "identity": null
-  }
+{
+   "name":"doc-extraction-multimodal-embedding-ds",
+   "description":null,
+   "type":"azureblob",
+   "subtype":null,
+   "credentials":{
+      "connectionString":"{{storageConnection}}"
+   },
+   "container":{
+      "name":"sustainable-ai-pdf",
+      "query":null
+   },
+   "dataChangeDetectionPolicy":null,
+   "dataDeletionDetectionPolicy":null,
+   "encryptionKey":null,
+   "identity":null
+}
 ```
 
 Send the request. The response should look like:
@@ -174,15 +172,15 @@ Connection: close
 
 {
   "name": "doc-extraction-multimodal-embedding-ds",
-  "description": "A test datasource",
+  "description": null,
   "type": "azureblob",
   "subtype": null,
   "indexerPermissionOptions": [],
   "credentials": {
     "connectionString": null
   },
   "container": {
-    "name": "doc-extraction-multimodality-container",
+    "name": "sustainable-ai-pdf",
     "query": null
   },
   "dataChangeDetectionPolicy": null,
@@ -288,7 +286,7 @@ POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
             {
                 "name": "hnsw",
                 "algorithm": "defaulthnsw",
-                "vectorizer": "{{vectorizer}}"
+                "vectorizer": "demo-vectorizer"
             }
         ],
         "algorithms": [
@@ -304,11 +302,11 @@ POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
         ],
         "vectorizers": [
             {
-                "name": "{{ vectorizer }}",
+                "name": "demo-vectorizer",
                 "kind": "aiServicesVision",
                 "aiServicesVisionParameters": {
                     "resourceUri": "{{cognitiveServicesUrl}}",
-                    "searchApiKey": "{{cognitiveServicesKey}}",
+                    "authIdentity": null,
                     "modelVersion": "{{modelVersion}}"
                 }
             }
@@ -451,7 +449,7 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
     {
       "@odata.type": "#Microsoft.Skills.Util.ShaperSkill",
       "name": "shaper-skill",
-      "description": "Shaper skill to reshape the data to fit the index schema"
+      "description": "Shaper skill to reshape the data to fit the index schema",
       "context": "/document/normalized_images/*",
       "inputs": [
         {
@@ -493,9 +491,9 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
     }  
   ],
   "cognitiveServices": {
-    "@odata.type": "#Microsoft.Azure.Search.AIServicesByKey",
+    "@odata.type": "#Microsoft.Azure.Search.AIServicesByIdentity",
     "subdomainUrl": "{{cognitiveServicesUrl}}",
-    "key": "{{cognitiveServicesKey}}"
+    "identity": null
   },
   "indexProjections": {
       "selectors": [
@@ -548,6 +546,7 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
   },
   "knowledgeStore": {
     "storageConnectionString": "{{storageConnection}}",
+    "identity": null,
     "projections": [
       {
         "files": [
@@ -583,6 +582,7 @@ POST {{searchUrl}}/indexers?api-version=2025-05-01-preview   HTTP/1.1
   api-key: {{searchApiKey}}
 
 {
+  "name": "doc-extraction-multimodal-embedding-indexer",
   "dataSourceName": "doc-extraction-multimodal-embedding-ds",
   "targetIndexName": "doc-extraction-multimodal-embedding-index",
   "skillsetName": "doc-extraction-multimodal-embedding-skillset",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダル埋め込みドキュメント抽出チュートリアルの更新"
}
```

### Explanation
この変更は、`tutorial-document-extraction-multimodal-embeddings.md` ドキュメントのマイナーな更新を示しています。主な修正内容は以下の通りです。

1. **リソース要件の明確化**: Azure AIサービスのマルチサービスアカウントの説明が追加され、これがチュートリアルで使用するために必要であることが強調されています。

2. **ロールと権限の説明**: Azure Storageへの接続に必要な役割が明確に記載され、データの抽出に必要な権限が「Storage Blob Data Contributor」と「Storage Table Data Contributor」に分けて説明されています。

3. **API呼び出しの更新**: 許可や認証が関わる処理における役割の使用についての説明が詳細化され、ユーザーの理解が向上しました。

4. **サンプルデータの配置**: 新たに「sustainable-ai-pdf」コンテナ名が指定され、ユーザーが一貫して同じデータストレージ名を使用することを促しています。

5. **インデックスとスキルセットの情報更新**: 一部の設定やパラメータ名が具体的に記述され、より明確な情報が提供されています。例えば、インデックス名が「doc-extraction-multimodal-embedding-indexer」に設定されています。

6. **技術的な詳細の改善**: 各種APIリクエストやレスポンスの一部が整形され、よりわかりやすい内容になっています。

これらの変更により、チュートリアルは最新の情報を基にしており、ユーザーがマルチモーダル埋め込みの設定をしやすくなることを目的としています。

## articles/search/tutorial-document-layout-image-verbalization.md{#item-f5de57}

<details>
<summary>Diff</summary>
````diff
@@ -64,7 +64,7 @@ The following instructions apply to Azure Storage which provides the sample data
 
 1. [Create role assignments and specify a managed identity in a connection string](search-howto-managed-identities-storage.md):
 
-   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer and **Storage Blob Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
+   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer. Assign **Storage Blob Data Contributor** and **Storage Table Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
 
    1. For connections made using a system-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
 
@@ -122,11 +122,12 @@ For more information, see [Role-based access control for Azure OpenAI in Azure A
 
 For this tutorial, your local REST client connection to Azure AI Search requires an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Connect to a search service](search-get-started-rbac.md).
 
-For other authenticated connections, the search service uses the role assignments you previously defined.
+For authenticated connections that occur during indexer and skillset processing, the search service uses the role assignments you previously defined.
 
 1. Start Visual Studio Code and create a new file.
 
-1. Provide values for variables used in the request.
+1. Provide values for variables used in the request. For `@storageConnection`, make sure your connection string doesn't have a trailing semicolon or quotation marks. For `@imageProjectionContainer`, provide a container name that's unique in blob storage. Azure AI Search creates this container for you during skills processing.
+
    ```http
    @searchUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
    @searchApiKey = PUT-YOUR-ADMIN-API-KEY-HERE
@@ -135,7 +136,7 @@ For other authenticated connections, the search service uses the role assignment
    @openAIKey = PUT-YOUR-OPENAI-KEY-HERE
    @chatCompletionResourceUri = PUT-YOUR-CHAT-COMPLETION-URI-HERE
    @chatCompletionKey = PUT-YOUR-CHAT-COMPLETION-KEY-HERE
-   @imageProjectionContainer=PUT-YOUR-IMAGE-PROJECTION-CONTAINER-HERE (Azure AI Search creates this container for you during skills processing)
+   @imageProjectionContainer=sustainable-ai-pdf-images
    ```
 
 1. Save the file using a `.rest` or `.http` file extension. For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
@@ -163,11 +164,11 @@ POST {{searchUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
     "description": "A data source to store multi-modality documents",
     "type": "azureblob",
     "subtype": null,
-    "credentials": {
-      "connectionString":  "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;"
+    "credentials":{
+      "connectionString":"{{storageConnection}}"
     },
     "container": {
-      "name": "doc-intelligence-multimodality-container",
+      "name": "sustainable-ai-pdf",
       "query": null
     },
     "dataChangeDetectionPolicy": null,
@@ -178,6 +179,42 @@ POST {{searchUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
 
 ```
 
+Send the request. The response should look like:
+
+```json
+HTTP/1.1 201 Created
+Transfer-Encoding: chunked
+Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
+Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-05-01-preview -Preview
+Server: Microsoft-IIS/10.0
+Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
+Preference-Applied: odata.include-annotations="*"
+OData-Version: 4.0
+request-id: 4eb8bcc3-27b5-44af-834e-295ed078e8ed
+elapsed-time: 346
+Date: Sat, 26 Apr 2025 21:25:24 GMT
+Connection: close
+
+{
+  "name": "doc-extraction-multimodal-embedding-ds",
+  "description": null,
+  "type": "azureblob",
+  "subtype": null,
+  "indexerPermissionOptions": [],
+  "credentials": {
+    "connectionString": null
+  },
+  "container": {
+    "name": "sustainable-ai-pdf",
+    "query": null
+  },
+  "dataChangeDetectionPolicy": null,
+  "dataDeletionDetectionPolicy": null,
+  "encryptionKey": null,
+  "identity": null
+}
+```
+
 ## Create an index
 
 [Create Index (REST)](/rest/api/searchservice/indexes/create) creates a search index on your search service. An index specifies all the parameters and their attributes.
@@ -274,7 +311,7 @@ POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
             {
                 "name": "hnsw",
                 "algorithm": "defaulthnsw",
-                "vectorizer": "{{vectorizer}}"
+                "vectorizer": "demo-vectorizer"
             }
         ],
         "algorithms": [
@@ -290,12 +327,12 @@ POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
         ],
         "vectorizers": [
             {
-              "name": "{{vectorizer}}",
+              "name": "demo-vectorizer",
               "kind": "azureOpenAI",    
               "azureOpenAIParameters": {
                 "resourceUri": "{{openAIResourceUri}}",
                 "deploymentId": "text-embedding-3-large",
-                "searchApiKey": "{{openAIKey}}",
+                "apiKey": "{{openAIKey}}",
                 "modelName": "text-embedding-3-large"
               }
             }
@@ -344,6 +381,7 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
   api-key: {{searchApiKey}}
 
 {
+  "name": "doc-intelligence-image-verbalization-skillset",
   "description": "A sample skillset for multi-modality using image verbalization",
   "skills": [
     {
@@ -395,15 +433,15 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
     ],
     "resourceUri": "{{openAIResourceUri}}",
     "deploymentId": "text-embedding-3-large",
-    "searchApiKey": "",
+    "apiKey": "{{openAIKey}}",
     "dimensions": 3072,
     "modelName": "text-embedding-3-large"
     },
     {
     "@odata.type": "#Microsoft.Skills.Custom.ChatCompletionSkill",
     "uri": "{{chatCompletionResourceUri}}",
     "timeout": "PT1M",
-    "searchApiKey": "",
+    "apiKey": "{{chatCompletionKey}}",
     "name": "genAI-prompt-skill",
     "description": "GenAI Prompt skill for image verbalization",
     "context": "/document/normalized_images/*",
@@ -448,7 +486,7 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
     ],
     "resourceUri": "{{openAIResourceUri}}",
     "deploymentId": "text-embedding-3-large",
-    "searchApiKey": "",
+    "apiKey": "{{openAIKey}}",
     "dimensions": 3072,
     "modelName": "text-embedding-3-large"
     },
@@ -479,7 +517,7 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
    "indexProjections": {
       "selectors": [
         {
-          "targetIndexName": "{{index}}",
+          "targetIndexName": "doc-intelligence-image-verbalization-index",
           "parentKeyFieldName": "text_document_id",
           "sourceContext": "/document/text_sections/*",
           "mappings": [    
@@ -502,7 +540,7 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
           ]
         },        
         {
-          "targetIndexName": "{{index}}",
+          "targetIndexName": "doc-intelligence-image-verbalization-index",
           "parentKeyFieldName": "image_document_id",
           "sourceContext": "/document/normalized_images/*",
           "mappings": [    
@@ -535,6 +573,7 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
   },  
   "knowledgeStore": {
     "storageConnectionString": "{{storageConnection}}",
+    "identity": null,
     "projections": [
       {
         "files": [
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントレイアウトと画像の言語化チュートリアルの更新"
}
```

### Explanation
この変更は、`tutorial-document-layout-image-verbalization.md` ドキュメントに対するマイナーな更新を示しています。主な修正内容は以下の通りです。

1. **ロールと権限の更新**: ストレージの役割の説明がより明確にされ、「Storage Blob Data Contributor」と「Storage Table Data Contributor」が具体的に指定されました。これにより、ユーザーはどの権限が必要かを理解しやすくなっています。

2. **接続設定の明確化**: `@imageProjectionContainer` の名前が「sustainable-ai-pdf-images」に変更され、ユーザーが一貫してこのコンテナ名を使用することが求められるようになっています。

3. **APIリクエストの改善**: データソースやインデックス作成に関するリクエストで、より効果的なリクエスト形式が提供され、ユーザーは具体的な構文を参考にしやすくなりました。また、レスポンス例も追加され、期待される結果がより具体的に示されています。

4. **インデックス名の明確化**: インデックス名が「doc-intelligence-image-verbalization-index」に明示的に設定され、ユーザーに対して一貫した情報が提供されています。

5. **技術的な変更の微調整**: APIパラメータ名が整理され、特にAPIキーの指定方法が改善されています。ユーザーが必要な資格情報を正確に設定できるように配慮されています。

これらの変更は、チュートリアルが最新の情報を反映し、ユーザーが技術を効果的に利用できるようにサポートすることを目的としています。全体として、コミュニケーションが強化され、ユーザーエクスペリエンスが向上しています。

## articles/search/tutorial-document-layout-multimodal-embeddings.md{#item-f67371}

<details>
<summary>Diff</summary>
````diff
@@ -34,15 +34,15 @@ In this tutorial, you use:
 
 + [Azure AI services multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills). This account provides access to both the Azure AI Vision multimodal embedding model and the Document Intelligence Layout model used by the skills in this tutorial. You must use an Azure AI multi-service account for skillset access to these resources. 
 
-+ [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier. It must also be in the same region as your multi-service account.
++ [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier.
 
 + [Azure Storage](/azure/storage/common/storage-account-create), used for storing sample data and for creating a [knowledge store](knowledge-store-concept-intro.md).
 
 + [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
 ## Limitations
 
-+ The [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) has limited regional availability. For a list of supported regions, see [Document Layout skill> Supported regions](cognitive-search-skill-document-intelligence-layout.md#supported-regions).
++ The [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) has limited regional availability. When you install the multi-service account, choose a region that provides multimodal embeddings. For a list of supported regions, see [Document Layout skill> Supported regions](cognitive-search-skill-document-intelligence-layout.md#supported-regions).
 
 + The [Azure AI Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) also has limited regional availability. For an updated list of regions that provide multimodal embeddings, see the [Azure AI Vision documentation](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
 
@@ -58,7 +58,7 @@ The following instructions apply to Azure Storage which provides the sample data
 
 1. [Create role assignments and specify a managed identity in a connection string](search-howto-managed-identities-storage.md):
 
-   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer and **Storage Blob Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
+   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer. Assign **Storage Blob Data Contributor** and **Storage Table Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
 
    1. For connections made using a system-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
 
@@ -100,20 +100,19 @@ The same role assignment is also used for accessing the Document Intelligence La
 
 For this tutorial, your local REST client connection to Azure AI Search requires an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Connect to a search service](search-get-started-rbac.md).
 
-For other authenticated connections, the search service uses the role assignments you previously defined.
+For authenticated connections that occur during indexer and skillset processing, the search service uses the role assignments you previously defined.
 
 1. Start Visual Studio Code and create a new file.
 
-1. Provide values for variables used in the request.
+1. Provide values for variables used in the request. For `@storageConnection`, make sure your connection string doesn't have a trailing semicolon or quotation marks. For `@imageProjectionContainer`, provide a container name that's unique in blob storage. Azure AI Search creates this container for you during skills processing.
 
    ```http
    @searchUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
    @searchApiKey = PUT-YOUR-ADMIN-API-KEY-HERE
    @storageConnection = PUT-YOUR-STORAGE-CONNECTION-STRING-HERE
-   @cognitiveServicesUrl = PUT-YOUR-COGNITIVE-SERVICES-URL-HERE
-   @cognitiveServicesKey= PUT-YOUR-COGNITIVE-SERVICES-API-KEY-HERE
-   @modelVersion = PUT-YOUR-VECTORIZE-MODEL-VERSION-HERE
-   @imageProjectionContainer=PUT-YOUR-IMAGE-PROJECTION-CONTAINER-HERE (Azure AI Search creates this container for you during skills processing)
+   @cognitiveServicesUrl = PUT-YOUR-AZURE-AI-MULTI-SERVICE-ENDPOINT-HERE
+   @modelVersion = 2023-04-15
+   @imageProjectionContainer=sustainable-ai-pdf-images
    ```
 
 1. Save the file using a `.rest` or `.http` file extension. For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
@@ -141,19 +140,54 @@ POST {{searchUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
     "description": "A data source to store multimodal documents",
     "type": "azureblob",
     "subtype": null,
-    "credentials": {
-      "connectionString":  "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;"
+    "credentials":{
+      "connectionString":"{{storageConnection}}"
     },
     "container": {
-      "name": "doc-intelligence-multimodality-container",
+      "name": "sustainable-ai-pdf",
       "query": null
     },
     "dataChangeDetectionPolicy": null,
     "dataDeletionDetectionPolicy": null,
     "encryptionKey": null,
     "identity": null
   }
+```
+
+Send the request. The response should look like:
+
+```json
+HTTP/1.1 201 Created
+Transfer-Encoding: chunked
+Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
+Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-05-01-preview -Preview
+Server: Microsoft-IIS/10.0
+Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
+Preference-Applied: odata.include-annotations="*"
+OData-Version: 4.0
+request-id: 4eb8bcc3-27b5-44af-834e-295ed078e8ed
+elapsed-time: 346
+Date: Sat, 26 Apr 2025 21:25:24 GMT
+Connection: close
 
+{
+  "name": "doc-extraction-multimodal-embedding-ds",
+  "description": null,
+  "type": "azureblob",
+  "subtype": null,
+  "indexerPermissionOptions": [],
+  "credentials": {
+    "connectionString": null
+  },
+  "container": {
+    "name": "sustainable-ai-pdf",
+    "query": null
+  },
+  "dataChangeDetectionPolicy": null,
+  "dataDeletionDetectionPolicy": null,
+  "encryptionKey": null,
+  "identity": null
+}
 ```
 
 ## Create an index
@@ -252,7 +286,7 @@ POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
             {
                 "name": "hnsw",
                 "algorithm": "defaulthnsw",
-                "vectorizer": "{{vectorizer}}"
+                "vectorizer": "demo-vectorizer"
             }
         ],
         "algorithms": [
@@ -268,11 +302,11 @@ POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
         ],
         "vectorizers": [
             {
-                "name": "{{ vectorizer }}",
+                "name": "demo-vectorizer",
                 "kind": "aiServicesVision",
                 "aiServicesVisionParameters": {
                     "resourceUri": "{{cognitiveServicesUrl}}",
-                    "searchApiKey": "{{cognitiveServicesKey}}",
+                    "authIdentity": null,
                     "modelVersion": "{{modelVersion}}"
                 }
             }
@@ -416,7 +450,7 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
    "indexProjections": {
       "selectors": [
         {
-          "targetIndexName": "{{index}}",
+          "targetIndexName": "doc-intelligence-multimodal-embedding-index",
           "parentKeyFieldName": "text_document_id",
           "sourceContext": "/document/text_sections/*",
           "mappings": [    
@@ -465,9 +499,15 @@ POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
       "parameters": {
         "projectionMode": "skipIndexingParentDocuments"
       }
-  },  
+  },
+  "cognitiveServices": {
+    "@odata.type": "#Microsoft.Azure.Search.AIServicesByIdentity",
+    "subdomainUrl": "{{cognitiveServicesUrl}}",
+    "identity": null
+  },
   "knowledgeStore": {
     "storageConnectionString": "",
+    "identity": null,
     "projections": [
       {
         "files": [
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダル埋め込みドキュメントレイアウトチュートリアルの更新"
}
```

### Explanation
この変更は、`tutorial-document-layout-multimodal-embeddings.md` ドキュメントに対するマイナーな更新を示しています。主な修正内容は以下の通りです。

1. **新規リソースの追加**: Azure AIサービスのマルチサービスアカウントの使用を強調し、具体的にどのリソースにアクセスできるか（マルチモーダル埋め込みモデルとドキュメントインテリジェンスレイアウトモデル）を明記しました。

2. **接続要件の変更**: `@imageProjectionContainer` の名前が「sustainable-ai-pdf-images」に設定され、ユーザーに一貫したコンテナ名を提供するようになっています。また、接続設定に関する説明が微調整されています。

3. **役割の説明の明確化**: ストレージに関する役割割り当ての詳細が改善され、各ロールの具体的な役割が示されています。特に「Storage Blob Data Contributor」と「Storage Table Data Contributor」が明記され、ユーザーにとって理解しやすくなっています。

4. **APIリクエストの改善**: データソース作成やインデックス作成のためのリクエストにおいて、レスポンス例が追加され、期待される出力が具体的に示されています。また、インデックスの名前が「doc-intelligence-multimodal-embedding-index」に変更され、より明確な情報が提供されています。

5. **技術的な詳細の整備**: 一部のAPIパラメータと構造が整理され、特にAIサービスの接続情報に関する記述が更新されています。これは、ユーザーが必要な設定を行いやすくすることを目的としています。

全体として、これらの変更により、チュートリアルは最新の情報を反映し、ユーザーがマルチモーダル埋め込みを効果的に活用できるようにサポートしています。


