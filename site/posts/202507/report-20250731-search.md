---
date: '2025-07-31'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c2bb090...MicrosoftDocs:18e731f
summary: このドキュメント更新では、Azure OpenAIに関する情報が強化され、ユーザーの利便性向上を目指しています。新しいエンドポイントや非互換リソースに関する詳細が追加され、特にマルチモーダル埋め込みのチュートリアルが更新されました。これにより、テキストや画像を活用した検索システムの設計・実装が実践的に行えるようになっています。また、前提条件や設定手順が整理されて、ユーザーが利用しやすい形になっています。全体として、Azureのサービス活用をサポートする内容となっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c2bb090...MicrosoftDocs:18e731f){target="_blank"}

<format>
# Highlights
このドキュメント更新では、Azure OpenAIの埋め込みやベクトライザーに関連する情報が強化されており、ユーザーがよりスムーズに利用できるようエンドポイント設定や非互換リソースに関する詳細が提供されています。また、マルチモーダル埋め込みや画像の言語化に関するチュートリアルが更新され、実践的な手順が強調されました。

## New features
- Azure AI Foundryによって自動的に生成される新しいエンドポイントに関する情報追加
- マルチモーダルインデクシングの具体的なプロセスについての詳細が強化
- 文書構造に基づく画像の言語化やインデクシング方法の明確化

## Breaking changes
- Azure OpenAIリソースに対して非互換な部分の明記
- 既存エンドポイントからの変更に伴う新しいエンドポイント使用指示

## Other updates
- チュートリアルにおける画像データとテキストデータの処理手法の詳細化
- 前提条件や設定手順に関する情報を整理し、実行が容易な形に

# Insights
このコード差分がもたらす最も重要な点は、Azure OpenAIとその関連サービスの設定をより具体的かつ明確にすることで、ユーザーにとっての利便性を向上させることです。具体的に、新たなエンドポイントに関する情報を提供することで、ユーザーが新しい技術を適用する際の障壁を減らしています。この変更により、Azure AI Foundryで作成されたリソースの互換性が明確化され、サービス利用を円滑に進められるようになっています。

さらに、マルチモーダル埋め込みのチュートリアルが更新されたことで、テキストおよび画像の両方を活用した検索システムの設計と実装がより実践的に行えるようになりました。特に、データを効率的に取り扱い、検索可能な方法に統合する手順が詳細に示されていることは、ユーザーの実装の際の理解を助ける役割を果たします。

画像ファイル自体の更新は見た目の改善に留まるものの、視覚的に内容を強化し、技術的な概念を直感的に理解できるようになります。

全体として、これらの文書更新は、Azureのマルチサービスを効果的に活用するサポートを強化することを目的としており、エンドユーザーにとっての技術採用と適応をサポートするものとなっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-azure-openai-embedding.md](#item-3eca57) | minor update | Azure OpenAI 埋め込みスキルに関する文書の更新 | modified | 4 | 4 | 8 | 
| [scoring-over-ranked-results.png](#item-bee24f) | minor update | スコアリング順位結果の画像更新 | modified | 0 | 0 | 0 | 
| [tutorial-document-extraction-image-verbalization.md](#item-398a90) | minor update | 画像の言語化を使用した文書抽出チュートリアルの更新 | modified | 83 | 65 | 148 | 
| [tutorial-document-extraction-multimodal-embeddings.md](#item-a3db59) | minor update | マルチモーダル埋め込みを使用した文書抽出チュートリアルの更新 | modified | 81 | 63 | 144 | 
| [tutorial-document-layout-image-verbalization.md](#item-f5de57) | minor update | 構造化文書レイアウトから画像を言語化するチュートリアルの更新 | modified | 96 | 60 | 156 | 
| [tutorial-document-layout-multimodal-embeddings.md](#item-f67371) | minor update | 構造化文書レイアウトからマルチモーダル埋め込み生成に関するチュートリアルの更新 | modified | 74 | 56 | 130 | 
| [vector-search-vectorizer-azure-open-ai.md](#item-e75cee) | minor update | Azure OpenAI ベクトライザーに関するドキュメントの更新 | modified | 3 | 2 | 5 | 


# Modified Contents
## articles/search/cognitive-search-skill-azure-openai-embedding.md{#item-3eca57}

<details>
<summary>Diff</summary>
````diff
@@ -2,14 +2,14 @@
 title: Azure OpenAI Embedding skill
 titleSuffix: Azure AI Search
 description: Connects to a deployed model on your Azure OpenAI resource.
-author: dharun1995
-ms.author: dhanasekars
+author: gmndrg
+ms.author: gimondra
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: reference
-ms.date: 05/08/2025
+ms.date: 07/29/2025
 ---
 
 #	Azure OpenAI Embedding skill
@@ -20,7 +20,7 @@ The **Azure OpenAI Embedding** skill connects to a deployed embedding model on y
 
 Your Azure OpenAI in Azure AI Foundry Models resource must have an associated [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains). If the service was created through the Azure portal, this subdomain is automatically generated as part of your service setup. Ensure that your service includes a custom subdomain before using it with the Azure AI Search integration.
 
-Azure OpenAI resources (with access to embedding models) that were created in Azure AI Foundry portal aren't supported. Only the Azure OpenAI resources created in the Azure portal are compatible with the **Azure OpenAI Embedding** skill integration.
+If you create an AI Service using Azure AI Foundry, it will automatically generate an endpoint with the domain cognitiveservices.azure.com. When you deploy an Azure OpenAI embedding model in this service, you can change the endpoint to use openai.azure.com domain instead, when using it in this skill. For example, change your endpoint from `https://<yourendpoint>.cognitiveservices.azure.com` to `https://<yourendpoint>.openai.azure.com`. Use this updated endpoint as the value for the `resourceUri` property for this skill. 
 
 The [Import and vectorize data wizard](search-get-started-portal-import-vectors.md) in the Azure portal uses the **Azure OpenAI Embedding** skill to vectorize content. You can run the wizard and review the generated skillset to see how the wizard builds the skill for embedding models.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI 埋め込みスキルに関する文書の更新"
}
```

### Explanation
この変更は、"Azure OpenAI 埋め込みスキル"に関する文書の更新を含んでいます。具体的には、著者情報や日付の修正、さらに非互換性に関する説明の刷新が含まれています。以前は、Azure AI Foundryポータルで作成されたリソースがサポートされていないとされていましたが、最新の修正で新しいエンドポイントについての情報が追加され、ユーザーがサービスをよりスムーズに利用できるようになりました。 

このドキュメントでは、Azure AI Foundryを使用してAIサービスを作成した場合に自動的に生成されるエンドポイントと、それを使用して埋め込みモデルをデプロイする際の手順が明確化されています。エンドポイントの変更に伴う`resourceUri`プロパティの設定方法も具体的に示され、より良いユーザー体験を提供しています。

## articles/search/media/scoring-profiles/scoring-over-ranked-results.png{#item-bee24f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリング順位結果の画像更新"
}
```

### Explanation
この変更は、"スコアリングプロファイル"に関連する画像ファイルの更新を示しています。具体的には、`scoring-over-ranked-results.png`というファイルが改訂されたものの、追加や削除は行われていないため、内容的には実質的な変更は見られません。このような更新は、画像の品質改善や、ドキュメントのコンテキストに合わせた微調整など、視覚的な要素を強化する目的で行われることがあります。

画像の更新は、閲覧者にとってより明確で直感的な理解を提供する可能性があり、特に技術文書においては重要な役割を果たすことがあります。リンク先で直接新しい画像を見ることができるため、ユーザーは最新のビジュアルコンテンツを確認することができます。

## articles/search/tutorial-document-extraction-image-verbalization.md{#item-398a90}

<details>
<summary>Diff</summary>
````diff
@@ -10,119 +10,137 @@ ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.custom:
 ms.topic: tutorial
-ms.date: 05/29/2025
+ms.date: 07/30/2025
 
 ---
 
 # Tutorial: Verbalize images using generative AI
 
-Azure AI Search can extract and index both text and images from PDF documents stored in Azure Blob Storage. This tutorial shows you how to build a multimodal indexing pipeline that includes steps for describing visual content in natural language and using the generated descriptions in your searchable index.
+Azure AI Search can extract and index both text and images from PDF documents stored in Azure Blob Storage. This tutorial shows you how to build a multimodal indexing pipeline that *chunks data  using the built-in Text Split skill* and uses *image verbalization* to describe images. Cropped images are stored in a knowledge store, and visual content is described in natural language and ingested alongside text in a searchable index.
 
-From the source document, each image is passed to the [GenAI Prompt skill (preview)](cognitive-search-skill-genai-prompt.md) that calls a chat completion model to generate a concise textual description. These descriptions, along with the original document text, are then embedded into vector representations using Azure OpenAI’s text-embedding-3-large model. The result is a single index containing semantically searchable content from both modalities: text and verbalized images.
+To get image verbalizations, each extracted image is passed to the [GenAI Prompt skill (preview)](cognitive-search-skill-genai-prompt.md) that calls a chat completion model to generate a concise textual description. These descriptions, along with the original document text, are then embedded into vector representations using Azure OpenAI’s text-embedding-3-large model. The result is a single index containing searchable content from both modalities: text and verbalized images.
 
 In this tutorial, you use:
 
 + A 36-page PDF document that combines rich visual content, such as charts, infographics, and scanned pages, with traditional text.
 
 + An indexer and skillset to create an indexing pipeline that includes AI enrichment through skills.
 
-+ The [Document Extraction skill](cognitive-search-skill-document-extraction.md) for extracting normalized images and text.
++ The [Document Extraction skill](cognitive-search-skill-document-extraction.md) for extracting normalized images and text. The [Text Split skill](cognitive-search-skill-textsplit.md) chunks the data.
 
 + The [GenAI Prompt skill (preview)](cognitive-search-skill-genai-prompt.md) that calls a chat completion model to create descriptions of visual content.
 
-+ A search index configured to store text and image verbalizations.
++ A search index configured to store text and image verbalizations. Some content is vectorized for vector-based similarity search.
 
 This tutorial demonstrates a lower-cost approach for indexing multimodal content using the Document Extraction skill and image captioning. It enables extraction and search over both text and images from documents in Azure Blob Storage. However, it doesn't include locational metadata for text, such as page numbers or bounding regions. For a more comprehensive solution that includes structured text layout and spatial metadata, see [Tutorial: Verbalize images from a structured document layout](tutorial-document-layout-image-verbalization.md).
 
 > [!NOTE]
-> Setting `imageAction` to `generateNormalizedImages` results in image extraction, which is an extra charge. For more information, see [Azure AI Search pricing](https://azure.microsoft.com/pricing/details/search/) for image extraction.
+> Image extraction by the Document Extraction skill isn't free. Setting `imageAction` to `generateNormalizedImages` in the skillset triggers image extraction, which is an extra charge. For billing information, see [Azure AI Search pricing](https://azure.microsoft.com/pricing/details/search/).
 
 ## Prerequisites
 
-+ [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier. It must also be in the same region as your multi-service account.
++ [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier.
 
 + [Azure Storage](/azure/storage/common/storage-account-create), used for storing sample data and for creating a [knowledge store](knowledge-store-concept-intro.md).
 
-+ A chat completion model hosted in Azure AI Foundry or another source. The model is used to verbalize image content. You provide the URI to the hosted model in the GenAI Prompt skill definition.
++ [Azure OpenAI](/azure/ai-foundry/openai/how-to/create-resource) with a deployment of
 
-+ A text embedding model deployed in Azure AI Foundry. The model is used to vectorize text content pull from source documents and the image descriptions generated by the chat completion model. For integrated vectorization, the embedding model must be located in Azure AI Foundry, and it must be either text-embedding-ada-002, text-embedding-3-large, or text-embedding-3-small. If you want to use an external embedding model, use a custom skill instead of the Azure OpenAI embedding skill.
+  + A chat completion model hosted in Azure AI Foundry or another source. The model is used to verbalize image content. You provide the URI to the hosted model in the GenAI Prompt skill definition. You can use [any chat completion model](cognitive-search-skill-genai-prompt.md#supported-models).
+
+  + A text embedding model deployed in Azure AI Foundry. The model is used to vectorize text content pull from source documents and the image descriptions generated by the chat completion model. For integrated vectorization, the embedding model must be located in Azure AI Foundry, and it must be either text-embedding-ada-002, text-embedding-3-large, or text-embedding-3-small. If you want to use an external embedding model, use a custom skill instead of the Azure OpenAI embedding skill.
 
 + [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
 ## Prepare data
 
-Download the following sample PDF:
-
-+ [sustainable-ai-pdf](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Accelerating-Sustainability-with-AI-2025.pdf)
+The following instructions apply to Azure Storage which provides the sample data and also hosts the knowledge store. A search service identity needs read access to Azure Storage to retrieve the sample data, and it needs write access to create the knowledge store. The search service creates the container for cropped images during skillset processing, using the name you provide in an environment variable.
 
-### Upload sample data to Azure Storage
+1. Download the following sample PDF: [sustainable-ai-pdf](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Accelerating-Sustainability-with-AI-2025.pdf)
 
-1. In Azure Storage, create a new container named **doc-extraction-image-verbalization-container**.
+1. In Azure Storage, create a new container named **sustainable-ai-pdf**.
 
 1. [Upload the sample data file](/azure/storage/blobs/storage-quickstart-blobs-portal).
 
-1. [Create a **Storage Blob Data Reader** role assignment and specify a managed identity in a connection string](search-howto-managed-identities-storage.md)
+1. [Create role assignments and specify a managed identity in a connection string](search-howto-managed-identities-storage.md):
 
-1. For connections made using a system-assigned managed identity. Provide a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
+   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer and **Storage Blob Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
 
-    ```json
-    "credentials" : { 
-        "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
-    }
-    ```
+   1. For connections made using a system-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
 
-1. For connections made using a user-assigned managed identity. Provide a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. Provide an identity using the syntax shown in the following example. Set userAssignedIdentity to the user-assigned managed identity The connection string is similar to the following example:
+        ```json
+        "credentials" : { 
+            "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
+        }
+        ```
 
-    ```json
-    "credentials" : { 
-        "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
-    },
-    "identity" : { 
-        "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
-        "userAssignedIdentity" : "/subscriptions/00000000-0000-0000-0000-00000000/resourcegroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MY-DEMO-USER-MANAGED-IDENTITY" 
-    }
-    ```
+   1. For connections made using a user-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. Provide an identity using the syntax shown in the following example. Set userAssignedIdentity to the user-assigned managed identity The connection string is similar to the following example:
 
-### Copy a search service URL and API key
+      ```json
+      "credentials" : { 
+          "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
+      },
+      "identity" : { 
+          "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
+          "userAssignedIdentity" : "/subscriptions/00000000-0000-0000-0000-00000000/resourcegroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MY-DEMO-USER-MANAGED-IDENTITY" 
+      }
+      ```
 
-For this tutorial, connections to Azure AI Search require an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Managed identities](search-howto-managed-identities-data-sources.md).
+## Prepare models
 
-1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the search service **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
+This tutorial assumes you have an existing Azure OpenAI resource through which the skills call the text embedding model and chat completion models. The search service connects to the models during skillset processing and during query execution using its managed identity. This section gives you guidance and links for assigning roles for authorized access.
 
-1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
+1. Sign in to the Azure portal (not the Foundry portal) and find the Azure OpenAI resource.
 
-   :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
+1. Select **Access control (IAM)**.
+
+1. Select **Add** and then **Add role assignment**.
+
+1. Search for **Cognitive Services OpenAI User** and then select it.
+
+1. Choose **Managed identity** and then assign your [search service managed identity](search-howto-managed-identities-data-sources.md).
+
+For more information, see [Role-based access control for Azure OpenAI in Azure AI Foundry Models](/azure/ai-foundry/openai/how-to/role-based-access-control).
 
 ## Set up your REST file
 
+For this tutorial, your local REST client connection to Azure AI Search requires an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Connect to a search service](search-get-started-rbac.md).
+
+For other authenticated connections, the search service uses the role assignments you previously defined.
+
 1. Start Visual Studio Code and create a new file.
 
 1. Provide values for variables used in the request.
 
    ```http
-   @baseUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
-   @apiKey = PUT-YOUR-ADMIN-API-KEY-HERE
+   @searchUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
+   @searchApiKey = PUT-YOUR-ADMIN-API-KEY-HERE
    @storageConnection = PUT-YOUR-STORAGE-CONNECTION-STRING-HERE
    @openAIResourceUri = PUT-YOUR-OPENAI-URI-HERE
    @openAIKey = PUT-YOUR-OPENAI-KEY-HERE
    @chatCompletionResourceUri = PUT-YOUR-CHAT-COMPLETION-URI-HERE
    @chatCompletionKey = PUT-YOUR-CHAT-COMPLETION-KEY-HERE
-   @imageProjectionContainer=PUT-YOUR-IMAGE-PROJECTION-CONTAINER-HERE
+   @imageProjectionContainer=PUT-YOUR-IMAGE-PROJECTION-CONTAINER-HERE (Azure AI Search creates this container for you during skills processing)
    ```
 
-1. Save the file using a `.rest` or `.http` file extension.
+1. Save the file using a `.rest` or `.http` file extension. For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
+
+To get the Azure AI Search endpoint and API key:
 
-For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
+1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the search service **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
+
+1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
+
+   :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
 
 ## Create a data source
 
 [Create Data Source (REST)](/rest/api/searchservice/data-sources/create) creates a data source connection that specifies what data to index.
 
 ```http
 ### Create a data source
-POST {{baseUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
   {
     "name": "doc-extraction-image-verbalization-ds",
@@ -187,9 +205,9 @@ For nested JSON, the index fields must be identical to the source fields. Curren
 
 ```http
 ### Create an index
-POST {{baseUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
 {
     "name": "doc-extraction-image-verbalization-index",
@@ -296,7 +314,7 @@ POST {{baseUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
               "azureOpenAIParameters": {
                 "resourceUri": "{{openAIResourceUri}}",
                 "deploymentId": "text-embedding-3-large",
-                "apiKey": "{{openAIKey}}",
+                "searchApiKey": "{{openAIKey}}",
                 "modelName": "text-embedding-3-large"
               }
             }
@@ -339,9 +357,9 @@ The skillset also performs actions specific to images. It uses the GenAI Prompt
 
 ```http
 ### Create a skillset
-POST {{baseUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
 {
   "name": "doc-extraction-image-verbalization-skillset",
@@ -419,7 +437,7 @@ POST {{baseUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
     ],
     "resourceUri": "{{openAIResourceUri}}",
     "deploymentId": "text-embedding-3-large",
-    "apiKey": "{{openAIKey}}",
+    "searchApiKey": "{{openAIKey}}",
     "dimensions": 3072,
     "modelName": "text-embedding-3-large"
     },
@@ -429,7 +447,7 @@ POST {{baseUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
     "description": "GenAI Prompt skill for image verbalization",
     "uri": "{{chatCompletionResourceUri}}",
     "timeout": "PT1M",
-    "apiKey": "{{chatCompletionKey}}",
+    "searchApiKey": "{{chatCompletionKey}}",
     "context": "/document/normalized_images/*",
     "inputs": [
         {
@@ -472,7 +490,7 @@ POST {{baseUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
     ],
     "resourceUri": "{{openAIResourceUri}}",
     "deploymentId": "text-embedding-3-large",
-    "apiKey": "{{openAIKey}}",
+    "searchApiKey": "{{openAIKey}}",
     "dimensions": 3072,
     "modelName": "text-embedding-3-large"
     },
@@ -606,9 +624,9 @@ Key points:
 
 ```http
 ### Create and run an indexer
-POST {{baseUrl}}/indexers?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
 {
   "dataSourceName": "doc-extraction-image-verbalization-ds",
@@ -638,9 +656,9 @@ You can start searching as soon as the first document is loaded.
 
 ```http
 ### Query the index
-POST {{baseUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
   
   {
     "search": "*",
@@ -689,9 +707,9 @@ Here are some examples of other queries:
 
 ```http
 ### Query for only images
-POST {{baseUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
   
   {
     "search": "*",
@@ -702,9 +720,9 @@ POST {{baseUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?ap
 
 ```http
 ### Query for text or images with content related to energy, returning the id, parent document, and text (extracted text for text chunks and verbalized image text for images), and the content path where the image is saved in the knowledge store (only populated for images)
-POST {{baseUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
   
   {
     "search": "energy",
@@ -719,20 +737,20 @@ Indexers can be reset to clear the high-water mark, which allows a full rerun. T
 
 ```http
 ### Reset the indexer
-POST {{baseUrl}}/indexers/doc-extraction-image-verbalization-indexer/reset?api-version=2025-05-01-preview   HTTP/1.1
-  api-key: {{apiKey}}
+POST {{searchUrl}}/indexers/doc-extraction-image-verbalization-indexer/reset?api-version=2025-05-01-preview   HTTP/1.1
+  api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Run the indexer
-POST {{baseUrl}}/indexers/doc-extraction-image-verbalization-indexer/run?api-version=2025-05-01-preview   HTTP/1.1
-  api-key: {{apiKey}}
+POST {{searchUrl}}/indexers/doc-extraction-image-verbalization-indexer/run?api-version=2025-05-01-preview   HTTP/1.1
+  api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Check indexer status 
-GET {{baseUrl}}/indexers/doc-extraction-image-verbalization-indexer/status?api-version=2025-05-01-preview   HTTP/1.1
-  api-key: {{apiKey}}
+GET {{searchUrl}}/indexers/doc-extraction-image-verbalization-indexer/status?api-version=2025-05-01-preview   HTTP/1.1
+  api-key: {{searchApiKey}}
 ```
 
 ## Clean up resources
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像の言語化を使用した文書抽出チュートリアルの更新"
}
```

### Explanation
この変更は、"文書抽出：画像の言語化"に関するチュートリアル文書の大幅な更新を含んでいます。主に、画像の言語化技術の詳細が強調され、データの処理方法について具体的な手法が追加されました。新しい内容では、データをチャンクする手法や、視覚コンテンツを自然言語で説明することに焦点を当てています。

具体的には、元の文書から抽出された各画像は、生成されたテキスト説明を用いてインデックスに統合され、テキストと画像の両方のコンテンツが検索可能になることが説明されています。また、必要な前提条件や手順の一部も改訂され、ユーザーにとっての利便性が向上しています。特に、Azure AI Searchの設定や実行における接続手順が明確化されており、チュートリアル全体が一層実践的なものとなっています。この更新は、ユーザーがより効果的にマルチモーダルインデクシングパイプラインを構築できるよう手助けすることを目的としています。

## articles/search/tutorial-document-extraction-multimodal-embeddings.md{#item-a3db59}

<details>
<summary>Diff</summary>
````diff
@@ -10,114 +10,132 @@ ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.custom:
 ms.topic: tutorial
-ms.date: 06/11/2025
+ms.date: 07/30/2025
 
 ---
-<!-- # Tutorial: Index mixed content using multimodal embeddings and the Document Extraction skill -->
+
 # Tutorial: Vectorize images and text
 
-Azure AI Search can extract and index both text and images from PDF documents stored in Azure Blob Storage. This tutorial shows you how to build a multimodal indexing pipeline by embedding both text and images into a unified semantic search index.
+Azure AI Search can extract and index both text and images from PDF documents stored in Azure Blob Storage. This tutorial shows you how to build a multimodal indexing pipeline in Azure AI Search that *chunks data using the built-in Text Split skill* and *uses multimodal embeddings* to vectorize text and images from the same document. Cropped images are stored in a knowledge store, and both text and visual content are vectorized and ingested in a searchable index.
 
 In this tutorial, you use:
 
 + A 36-page PDF document that combines rich visual content, such as charts, infographics, and scanned pages, with traditional text.
 
 + An indexer and skillset to create an indexing pipeline that includes AI enrichment through skills.
 
-+ The [Document Extraction skill](cognitive-search-skill-document-extraction.md) for extracting normalized images and text.
++ The [Document Extraction skill](cognitive-search-skill-document-extraction.md) for extracting normalized images and text. The [Text Split skill](cognitive-search-skill-textsplit.md) chunks the data.
 
 + The [Azure AI Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) to vectorize text and images.
 
-+ A search index configured to store text and image embeddings and support for vector-based similarity search.
++ A search index configured to store extracted text and image content. Some content is vectorized for vector-based similarity search.
 
-This tutorial demonstrates a lower-cost approach for indexing multimodal content using the Document Extraction skill and image captioning. It enables extraction and search over both text and images from documents in Azure Blob Storage. However, it doesn't include locational metadata for text, such as page numbers or bounding regions. For a more comprehensive solution that includes structured text layout and spatial metadata, see [Tutorial: Verbalize images from a structured document layout](tutorial-document-layout-image-verbalization.md).
+This tutorial demonstrates a lower-cost approach for indexing multimodal content using the Document Extraction skill. It enables extraction and search over both text and images from documents pulled from Azure Blob Storage. However, it doesn't include locational metadata for text, such as page numbers or bounding regions. For a more comprehensive solution that includes structured text layout and spatial metadata, see [Tutorial: Vectorize from a structured document layout](tutorial-document-layout-multimodal-embeddings.md).
 
 > [!NOTE]
-> Setting `imageAction` to `generateNormalizedImages` results in image extraction, which is an extra charge. For more information, see [Azure AI Search pricing](https://azure.microsoft.com/pricing/details/search/) for image extraction.
+> Image extraction by the Document Extraction skill isn't free. Setting `imageAction` to `generateNormalizedImages` in the skillset triggers image extraction, which is an extra charge. For billing information, see [Azure AI Search pricing](https://azure.microsoft.com/pricing/details/search/).
 
 ## Prerequisites
 
-+ [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier. It must also be in the same region as your multi-service account.
++ [Azure AI services multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills). This account provides access to the Azure AI Vision multimodal embedding model used in this tutorial. You must use an Azure AI multi-service account for skillset access to this resource.
 
-+ [Azure Storage](/azure/storage/common/storage-account-create), used for storing sample data and for creating a [knowledge store](knowledge-store-concept-intro.md).
++ [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity for connections to Azure Storage and Azure AI Vision. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier. The search service must also be in the same region as your multi-service account.
 
-+ An [Azure AI services multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills) that provides Azure AI Vision for multimodal embeddings. You must use an Azure AI multi-service account for this task. For an updated list of regions that provide multimodal embeddings, see the [Azure AI Vision documentation](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
++ [Azure Storage](/azure/storage/common/storage-account-create), used for storing sample data and for creating a [knowledge store](knowledge-store-concept-intro.md).
 
 + [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
-## Prepare data
+## Limitations
 
-Download the following sample PDF:
++ The [Azure AI Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) also has limited regional availability. For an updated list of regions that provide multimodal embeddings, see the [Azure AI Vision documentation](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
 
-+ [sustainable-ai-pdf](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Accelerating-Sustainability-with-AI-2025.pdf)
+## Prepare data
+
+The following instructions apply to Azure Storage which provides the sample data and also hosts the knowledge store. A search service identity needs read access to Azure Storage to retrieve the sample data, and it needs write access to create the knowledge store. The search service creates the container for cropped images during skillset processing, using the name you provide in an environment variable.
 
-### Upload sample data to Azure Storage
+1. Download the following sample PDF: [sustainable-ai-pdf](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Accelerating-Sustainability-with-AI-2025.pdf)
 
-1. In Azure Storage, create a new container named **doc-extraction-multimodality-container**.
+1. In Azure Storage, create a new container named **sustainable-ai-pdf**.
 
 1. [Upload the sample data file](/azure/storage/blobs/storage-quickstart-blobs-portal).
 
-1. [Create a **Storage Blob Data Reader** role assignment and specify a managed identity in a connection string](search-howto-managed-identities-storage.md)
+1. [Create role assignments and specify a managed identity in a connection string](search-howto-managed-identities-storage.md):
 
-1. For connections made using a system-assigned managed identity. Provide a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
+   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer and **Storage Blob Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
 
-    ```json
-    "credentials" : { 
-        "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
-    }
-    ```
+   1. For connections made using a system-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
 
-1. For connections made using a user-assigned managed identity. Provide a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. Provide an identity using the syntax shown in the following example. Set userAssignedIdentity to the user-assigned managed identity The connection string is similar to the following example:
+        ```json
+        "credentials" : { 
+            "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
+        }
+        ```
 
-    ```json
-    "credentials" : { 
-        "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
-    },
-    "identity" : { 
-        "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
-        "userAssignedIdentity" : "/subscriptions/00000000-0000-0000-0000-00000000/resourcegroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MY-DEMO-USER-MANAGED-IDENTITY" 
-    }
-    ```
+   1. For connections made using a user-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. Provide an identity using the syntax shown in the following example. Set userAssignedIdentity to the user-assigned managed identity The connection string is similar to the following example:
 
-### Copy a search service URL and API key
+      ```json
+      "credentials" : { 
+          "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
+      },
+      "identity" : { 
+          "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
+          "userAssignedIdentity" : "/subscriptions/00000000-0000-0000-0000-00000000/resourcegroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MY-DEMO-USER-MANAGED-IDENTITY" 
+      }
+      ```
 
-For this tutorial, connections to Azure AI Search require an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Managed identities](search-howto-managed-identities-data-sources.md).
+## Prepare models
 
-1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the search service **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
+This tutorial assumes you have an existing Azure AI multiservice account through which the skill calls the Azure AI Vision multimodal 4.0 embedding model. The search service connects to the model during skillset processing using its managed identity. This section gives you guidance and links for assigning roles for authorized access.
 
-1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
+1. Sign in to the Azure portal (not the Foundry portal) and find the Azure AI multiservice account. Make sure it's in a region that provides the [multimodal 4.0 API](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
 
-   :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
+1. Select **Access control (IAM)**.
+
+1. Select **Add** and then **Add role assignment**.
+
+1. Search for **Cognitive Services User** and then select it.
+
+1. Choose **Managed identity** and then assign your [search service managed identity](search-howto-managed-identities-data-sources.md).
 
 ## Set up your REST file
 
+For this tutorial, your local REST client connection to Azure AI Search requires an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Connect to a search service](search-get-started-rbac.md).
+
+For other authenticated connections, the search service uses the role assignments you previously defined.
+
 1. Start Visual Studio Code and create a new file.
 
 1. Provide values for variables used in the request.
 
    ```http
-   @baseUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
-   @apiKey = PUT-YOUR-ADMIN-API-KEY-HERE
+   @searchUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
+   @searchsearchApiKey = PUT-YOUR-ADMIN-API-KEY-HERE
    @storageConnection = PUT-YOUR-STORAGE-CONNECTION-STRING-HERE
    @cognitiveServicesUrl = PUT-YOUR-COGNITIVE-SERVICES-URL-HERE
    @cognitiveServicesKey= PUT-YOUR-COGNITIVE-SERVICES-URL-KEY-HERE
    @modelVersion = PUT-YOUR-VECTORIZE-MODEL-VERSION-HERE
-   @imageProjectionContainer=PUT-YOUR-IMAGE-PROJECTION-CONTAINER-HERE
+   @imageProjectionContainer=PUT-YOUR-IMAGE-PROJECTION-CONTAINER-HERE (Azure AI Search creates this container for you during skills processing)
    ```
 
-1. Save the file using a `.rest` or `.http` file extension.
+1. Save the file using a `.rest` or `.http` file extension. For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
 
-For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
+To get the Azure AI Search endpoint and API key:
+
+1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the search service **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
+
+1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
+
+   :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
 
 ## Create a data source
 
 [Create Data Source (REST)](/rest/api/searchservice/data-sources/create) creates a data source connection that specifies what data to index.
 
 ```http
 ### Create a data source
-POST {{baseUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
   {
     "name": "doc-extraction-multimodal-embedding-ds",
@@ -182,9 +200,9 @@ For nested JSON, the index fields must be identical to the source fields. Curren
 
 ```http
 ### Create an index
-POST {{baseUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
 {
     "name": "doc-extraction-multimodal-embedding-index",
@@ -290,7 +308,7 @@ POST {{baseUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
                 "kind": "aiServicesVision",
                 "aiServicesVisionParameters": {
                     "resourceUri": "{{cognitiveServicesUrl}}",
-                    "apiKey": "{{cognitiveServicesKey}}",
+                    "searchApiKey": "{{cognitiveServicesKey}}",
                     "modelVersion": "{{modelVersion}}"
                 }
             }
@@ -331,9 +349,9 @@ Key points:
 
 ```http
 ### Create a skillset
-POST {{baseUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
 {
   "name": "doc-extraction-multimodal-embedding-skillset",
@@ -560,9 +578,9 @@ Key points:
 
 ```http
 ### Create and run an indexer
-POST {{baseUrl}}/indexers?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
 {
   "dataSourceName": "doc-extraction-multimodal-embedding-ds",
@@ -592,9 +610,9 @@ You can start searching as soon as the first document is loaded.
 
 ```http
 ### Query the index
-POST {{baseUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
   
   {
     "search": "*",
@@ -640,9 +658,9 @@ For filters, you can also use Logical operators (and, or, not) and comparison op
 
 ```http
 ### Query for only images
-POST {{baseUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
   
   {
     "search": "*",
@@ -653,9 +671,9 @@ POST {{baseUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?a
 
 ```http
 ### Query for text or images with content related to energy, returning the id, parent document, and text (only populated for text chunks), and the content path where the image is saved in the knowledge store (only populated for images)
-POST {{baseUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
   
 
   {
@@ -671,20 +689,20 @@ Indexers can be reset to clear the high-water mark, which allows a full rerun. T
 
 ```http
 ### Reset the indexer
-POST {{baseUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/reset?api-version=2025-05-01-preview   HTTP/1.1
-  api-key: {{apiKey}}
+POST {{searchUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/reset?api-version=2025-05-01-preview   HTTP/1.1
+  api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Run the indexer
-POST {{baseUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/run?api-version=2025-05-01-preview   HTTP/1.1
-  api-key: {{apiKey}}
+POST {{searchUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/run?api-version=2025-05-01-preview   HTTP/1.1
+  api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Check indexer status 
-GET {{baseUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/status?api-version=2025-05-01-preview   HTTP/1.1
-  api-key: {{apiKey}}
+GET {{searchUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/status?api-version=2025-05-01-preview   HTTP/1.1
+  api-key: {{searchApiKey}}
 ```
 
 ## Clean up resources
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダル埋め込みを使用した文書抽出チュートリアルの更新"
}
```

### Explanation
この変更は、"マルチモーダル埋め込みを使用した文書抽出"に関するチュートリアル文書の更新を示しています。主な改善点は、データをテキストと画像の両方からベクトル化する方法に関する詳細強化であり、特にAzure AI Search内でのデータのチャンク処理と、マルチモーダル埋め込みを利用して同じ文書からの情報を統合するプロセスが強調されています。

新しく追加された内容では、チュートリアルが提供する機能や手順に関する情報がより明確になり、特定のスキルセットやインデックスの設定、Azure AI Visionの活用が含まれています。また、チュートリアルが必要とする前提条件が適切に整理され、これによりユーザーにとっての実行が容易になっています。

さらに、画像埋め込みやテキスト埋め込みに関する新しい注意事項も追加されており、コストに関連する情報が強調されています。これにより、ユーザーがリソースを効率的に利用できるようにするための指針が提供されています。この更新は、マルチモーダルコンテンツのインデクシングと検索をより効率的かつ効果的に行うための内容を提供することを目的としています。

## articles/search/tutorial-document-layout-image-verbalization.md{#item-f5de57}

<details>
<summary>Diff</summary>
````diff
@@ -10,15 +10,15 @@ ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.custom:
 ms.topic: tutorial
-ms.date: 05/29/2025
+ms.date: 07/30/2025
 
 ---
 
 # Tutorial: Verbalize images from a structured document layout
 
-In this Azure AI Search tutorial, learn how to build a multimodal indexing pipeline that chunks data based on document structure and uses image verbalization to describe images. Cropped images are stored in a knowledge store, and visual content is described in natural language and ingested alongside text in a searchable index.
+Azure AI Search can extract and index both text and images from PDF documents stored in Azure Blob Storage. This tutorial shows you how to build a multimodal indexing pipeline that *chunks data based on document structure* and uses *image verbalization* to describe images. Cropped images are stored in a knowledge store, and visual content is described in natural language and ingested alongside text in a searchable index. Chunking is based on the Azure AI Document Intelligence Layout model that recognizes document structure.
 
-From the source document, each image is passed to the [GenAI Prompt skill (preview)](cognitive-search-skill-genai-prompt.md) to generate a concise textual description. These descriptions, along with the original document text, are then embedded into vector representations using Azure OpenAI’s text-embedding-3-large model. The result is a single index containing semantically searchable content from both modalities: text and verbalized images.
+To get image verbalizations, each extracted image is passed to the [GenAI Prompt skill (preview)](cognitive-search-skill-genai-prompt.md) that calls a chat completion model to generate a concise textual description. These descriptions, along with the original document text, are then embedded into vector representations using Azure OpenAI’s text-embedding-3-large model. The result is a single index containing searchable content from both modalities: text and verbalized images.
 
 In this tutorial, you use:
 
@@ -34,93 +34,129 @@ In this tutorial, you use:
 
 ## Prerequisites
 
-+ [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier. It must also be in the same region as your multi-service account.
++ [Azure AI services multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills). This account provides access to the Document Intelligence Layout model used in this tutorial. You must use an Azure AI multi-service account for skillset access to this resource.
+
++ [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier.
 
 + [Azure Storage](/azure/storage/common/storage-account-create), used for storing sample data and for creating a [knowledge store](knowledge-store-concept-intro.md).
 
-+ A chat completion model hosted in Azure AI Foundry or another source. The model is used to verbalize image content. You provide the URI to the hosted model in the GenAI Prompt skill definition.
++ [Azure OpenAI](/azure/ai-foundry/openai/how-to/create-resource) with a deployment of
+
+  + A chat completion model hosted in Azure AI Foundry or another source. The model is used to verbalize image content. You provide the URI to the hosted model in the GenAI Prompt skill definition. You can use [any chat completion model](cognitive-search-skill-genai-prompt.md#supported-models).
 
-+ A text embedding model deployed in Azure AI Foundry. The model is used to vectorize text content pull from source documents and the image descriptions generated by the chat completion model. For integrated vectorization, the embedding model must be located in Azure AI Foundry, and it must be either text-embedding-ada-002, text-embedding-3-large, or text-embedding-3-small. If you want to use an external embedding model, use a custom skill instead of the Azure OpenAI embedding skill.
+  + A text embedding model deployed in Azure AI Foundry. The model is used to vectorize text content pull from source documents and the image descriptions generated by the chat completion model. For integrated vectorization, the embedding model must be located in Azure AI Foundry, and it must be either text-embedding-ada-002, text-embedding-3-large, or text-embedding-3-small. If you want to use an external embedding model, use a custom skill instead of the Azure OpenAI embedding skill.
 
 + [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
 ## Limitations
 
-The [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) has limited regional availability, is bound to Azure AI services, and requires a [billable resource](cognitive-search-attach-cognitive-services.md) for transactions that exceed 20 documents per indexer per day. For a lower-cost solution to indexing multimodal content, see [Tutorial: Verbalize images using generative AI](tutorial-document-extraction-image-verbalization.md).
++ The [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) has limited regional availability. For a list of supported regions, see [Document Layout skill> Supported regions](cognitive-search-skill-document-intelligence-layout.md#supported-regions).
 
 ## Prepare data
 
-Download the following sample PDF:
-
-+ [sustainable-ai-pdf](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Accelerating-Sustainability-with-AI-2025.pdf)
+The following instructions apply to Azure Storage which provides the sample data and also hosts the knowledge store. A search service identity needs read access to Azure Storage to retrieve the sample data, and it needs write access to create the knowledge store. The search service creates the container for cropped images during skillset processing, using the name you provide in an environment variable.
 
-### Upload sample data to Azure Storage
+1. Download the following sample PDF: [sustainable-ai-pdf](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Accelerating-Sustainability-with-AI-2025.pdf)
 
-1. In Azure Storage, create a new container named **doc-intelligence-multimodality-container**.
+1. In Azure Storage, create a new container named **sustainable-ai-pdf**.
 
 1. [Upload the sample data file](/azure/storage/blobs/storage-quickstart-blobs-portal).
 
-1. [Create a **Storage Blob Data Reader** role assignment and specify a managed identity in a connection string](search-howto-managed-identities-storage.md)
+1. [Create role assignments and specify a managed identity in a connection string](search-howto-managed-identities-storage.md):
 
-   1. For connections made using a system-assigned managed identity. Provide a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
+   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer and **Storage Blob Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
+
+   1. For connections made using a system-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
 
         ```json
         "credentials" : { 
             "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
         }
         ```
-   1. For connections made using a user-assigned managed identity. Provide a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. Provide an identity using the syntax shown in the following example. Set userAssignedIdentity to the user-assigned managed identity The connection string is similar to the following example:
-    
-        ```json
-        "credentials" : { 
-            "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
-        },
-        "identity" : { 
-            "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
-            "userAssignedIdentity" : "/subscriptions/00000000-0000-0000-0000-00000000/resourcegroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MY-DEMO-USER-MANAGED-IDENTITY" 
-        }
-        ```
 
-### Copy a search service URL and API key
+   1. For connections made using a user-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. Provide an identity using the syntax shown in the following example. Set userAssignedIdentity to the user-assigned managed identity The connection string is similar to the following example:
 
-For this tutorial, connections to Azure AI Search require an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Managed identities](search-howto-managed-identities-data-sources.md).
+      ```json
+      "credentials" : { 
+          "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
+      },
+      "identity" : { 
+          "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
+          "userAssignedIdentity" : "/subscriptions/00000000-0000-0000-0000-00000000/resourcegroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MY-DEMO-USER-MANAGED-IDENTITY" 
+      }
+      ```
 
-1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the search service **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
+## Prepare models
 
-1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
+This tutorial assumes you have an existing Azure OpenAI resource through which the skills a chat completion model for GenAI Prompt and also a text embedding model for vectorization. The search service connects to the models during skillset processing and during query execution using its managed identity. This section gives you guidance and links for assigning roles for authorized access.
 
-   :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
+You also need a role assignment for accessing the Document Intelligence Layout model via an Azure AI multi-service account.
+
+### Assign roles in Azure AI multi-service
+
+1. Sign in to the Azure portal (not the Foundry portal) and find the Azure AI multi=service account. Make sure it's in a region that provides the [Document Intelligence Layout model](cognitive-search-skill-document-intelligence-layout.md#supported-regions).
+
+1. Select **Access control (IAM)**.
+
+1. Select **Add** and then **Add role assignment**.
+
+1. Search for **Cognitive Services User** and then select it.
+
+1. Choose **Managed identity** and then assign your [search service managed identity](search-howto-managed-identities-data-sources.md).
+
+### Assign roles in Azure OpenAI
+
+1. Sign in to the Azure portal (not the Foundry portal) and find the Azure OpenAI resource.
+
+1. Select **Access control (IAM)**.
+
+1. Select **Add** and then **Add role assignment**.
+
+1. Search for **Cognitive Services OpenAI User** and then select it.
+
+1. Choose **Managed identity** and then assign your [search service managed identity](search-howto-managed-identities-data-sources.md).
+
+For more information, see [Role-based access control for Azure OpenAI in Azure AI Foundry Models](/azure/ai-foundry/openai/how-to/role-based-access-control).
 
 ## Set up your REST file
 
+For this tutorial, your local REST client connection to Azure AI Search requires an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Connect to a search service](search-get-started-rbac.md).
+
+For other authenticated connections, the search service uses the role assignments you previously defined.
+
 1. Start Visual Studio Code and create a new file.
 
 1. Provide values for variables used in the request.
-
    ```http
-   @baseUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
-   @apiKey = PUT-YOUR-ADMIN-API-KEY-HERE
+   @searchUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
+   @searchApiKey = PUT-YOUR-ADMIN-API-KEY-HERE
    @storageConnection = PUT-YOUR-STORAGE-CONNECTION-STRING-HERE
    @openAIResourceUri = PUT-YOUR-OPENAI-URI-HERE
    @openAIKey = PUT-YOUR-OPENAI-KEY-HERE
    @chatCompletionResourceUri = PUT-YOUR-CHAT-COMPLETION-URI-HERE
    @chatCompletionKey = PUT-YOUR-CHAT-COMPLETION-KEY-HERE
-   @imageProjectionContainer=PUT-YOUR-IMAGE-PROJECTION-CONTAINER-HERE
+   @imageProjectionContainer=PUT-YOUR-IMAGE-PROJECTION-CONTAINER-HERE (Azure AI Search creates this container for you during skills processing)
    ```
 
-1. Save the file using a `.rest` or `.http` file extension.
+1. Save the file using a `.rest` or `.http` file extension. For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
 
-For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
+To get the Azure AI Search endpoint and API key:
+
+1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the search service **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
+
+1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
+
+   :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
 
 ## Create a data source
 
 [Create Data Source (REST)](/rest/api/searchservice/data-sources/create) creates a data source connection that specifies what data to index.
 
 ```http
 ### Create a data source using system-assigned managed identities
-POST {{baseUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
   {
     "name": "doc-intelligence-image-verbalization-ds",
@@ -150,9 +186,9 @@ For nested JSON, the index fields must be identical to the source fields. Curren
 
 ```http
 ### Create an index
-POST {{baseUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
 {
     "name": "doc-intelligence-image-verbalization-index",
@@ -259,7 +295,7 @@ POST {{baseUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
               "azureOpenAIParameters": {
                 "resourceUri": "{{openAIResourceUri}}",
                 "deploymentId": "text-embedding-3-large",
-                "apiKey": "{{openAIKey}}",
+                "searchApiKey": "{{openAIKey}}",
                 "modelName": "text-embedding-3-large"
               }
             }
@@ -303,9 +339,9 @@ The skillset also performs actions specific to images. It uses the GenAI Prompt
 
 ```http
 ### Create a skillset
-POST {{baseUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
 {
   "description": "A sample skillset for multi-modality using image verbalization",
@@ -359,15 +395,15 @@ POST {{baseUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
     ],
     "resourceUri": "{{openAIResourceUri}}",
     "deploymentId": "text-embedding-3-large",
-    "apiKey": "",
+    "searchApiKey": "",
     "dimensions": 3072,
     "modelName": "text-embedding-3-large"
     },
     {
     "@odata.type": "#Microsoft.Skills.Custom.ChatCompletionSkill",
     "uri": "{{chatCompletionResourceUri}}",
     "timeout": "PT1M",
-    "apiKey": "",
+    "searchApiKey": "",
     "name": "genAI-prompt-skill",
     "description": "GenAI Prompt skill for image verbalization",
     "context": "/document/normalized_images/*",
@@ -412,7 +448,7 @@ POST {{baseUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
     ],
     "resourceUri": "{{openAIResourceUri}}",
     "deploymentId": "text-embedding-3-large",
-    "apiKey": "",
+    "searchApiKey": "",
     "dimensions": 3072,
     "modelName": "text-embedding-3-large"
     },
@@ -536,9 +572,9 @@ Key points:
 
 ```http
 ### Create and run an indexer
-POST {{baseUrl}}/indexers?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
 {
   "dataSourceName": "doc-intelligence-image-verbalization-ds",
@@ -568,9 +604,9 @@ You can start searching as soon as the first document is loaded.
 
 ```http
 ### Query the index
-POST {{baseUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
   
   {
     "search": "*",
@@ -602,9 +638,9 @@ For filters, you can also use Logical operators (and, or, not) and comparison op
 
 ```http
 ### Query for only images
-POST {{baseUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
   
   {
     "search": "*",
@@ -615,9 +651,9 @@ POST {{baseUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?
 
 ```http
 ### Query for text or images with content related to energy, returning the id, parent document, and text (only populated for text chunks), and the content path where the image is saved in the knowledge store (only populated for images)
-POST {{baseUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
   
   {
     "search": "energy",
@@ -632,20 +668,20 @@ Indexers can be reset to clear execution history, which allows a full rerun. The
 
 ```http
 ### Reset the indexer
-POST {{baseUrl}}/indexers/doc-intelligence-image-verbalization-indexer/reset?api-version=2025-05-01-preview   HTTP/1.1
-  api-key: {{apiKey}}
+POST {{searchUrl}}/indexers/doc-intelligence-image-verbalization-indexer/reset?api-version=2025-05-01-preview   HTTP/1.1
+  api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Run the indexer
-POST {{baseUrl}}/indexers/doc-intelligence-image-verbalization-indexer/run?api-version=2025-05-01-preview   HTTP/1.1
-  api-key: {{apiKey}}
+POST {{searchUrl}}/indexers/doc-intelligence-image-verbalization-indexer/run?api-version=2025-05-01-preview   HTTP/1.1
+  api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Check indexer status 
-GET {{baseUrl}}/indexers/doc-intelligence-image-verbalization-indexer/status?api-version=2025-05-01-preview   HTTP/1.1
-  api-key: {{apiKey}}
+GET {{searchUrl}}/indexers/doc-intelligence-image-verbalization-indexer/status?api-version=2025-05-01-preview   HTTP/1.1
+  api-key: {{searchApiKey}}
 ```
 
 ## Clean up resources
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "構造化文書レイアウトから画像を言語化するチュートリアルの更新"
}
```

### Explanation
この変更は、「構造化文書レイアウトから画像を言語化する」ためのチュートリアル文書の更新を含んでいます。主な改善点は、文書の構造に基づいてデータをチャンク化する方法と、画像を言語化するプロセスを強調する内容の追加です。このチュートリアルでは、PDF文書からテキストと画像を抽出し、自然言語での説明を付けてインデクシングする方法が詳述されています。

特に、Azure AI Document Intelligence Layoutモデルを使用して文書構造を認識し、それに基づいてデータをチャンク化するプロセスが明確になっています。また、前提条件に関する情報が整理されており、Azure AIサービスのマルチサービスアカウントの使用が必須であることが示されています。

さらに、Azure OpenAIリソースとの連携についても詳しく説明されており、ユーザーが必要な役割を適切に割り当てる手順が追加されています。この更新は、文書レイアウトに基づくより効果的な画像の言語化と検索機能をサポートすることを目的としています。全体として、チュートリアルはより実践的で包括的な内容となり、ユーザーにとっての利便性が向上しています。

## articles/search/tutorial-document-layout-multimodal-embeddings.md{#item-f67371}

<details>
<summary>Diff</summary>
````diff
@@ -10,14 +10,13 @@ ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.custom:
 ms.topic: tutorial
-ms.date: 06/11/2025
+ms.date: 07/30/2025
 
 ---
 
 # Tutorial: Vectorize from a structured document layout
 
-<!-- Multimodal plays an essential role in generative AI apps and the user experience as it enables the extraction of information not only from text but also from complex images embedded within documents.  -->
-In this Azure AI Search tutorial, learn how to build a multimodal indexing pipeline that chunks data based on document structure, and uses a multimodal embedding model to vectorize text and images in a searchable index.
+Azure AI Search can extract and index both text and images from PDF documents stored in Azure Blob Storage. This tutorial shows you how to build a multimodal indexing pipeline that *chunks data based on document structure* and *uses multimodal embeddings* to vectorize text and images from the same document. Cropped images are stored in a knowledge store, and both text and visual content are vectorized and ingested in a searchable index. Chunking is based on the Azure AI Document Intelligence Layout model that recognizes document structure.
 
 In this tutorial, you use:
 
@@ -29,94 +28,113 @@ In this tutorial, you use:
 
 + The [Azure AI Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) to vectorize text and images.
 
-+ A search index configured to store extracted text and image verbalizations. Some content is vectorized for vector-based similarity search.
++ A search index configured to store extracted text and image content. Some content is vectorized for vector-based similarity search.
 
 ## Prerequisites
 
++ [Azure AI services multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills). This account provides access to both the Azure AI Vision multimodal embedding model and the Document Intelligence Layout model used by the skills in this tutorial. You must use an Azure AI multi-service account for skillset access to these resources. 
+
 + [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier. It must also be in the same region as your multi-service account.
 
 + [Azure Storage](/azure/storage/common/storage-account-create), used for storing sample data and for creating a [knowledge store](knowledge-store-concept-intro.md).
 
-+ An [Azure AI services multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills) that provides Azure AI Vision for multimodal embeddings. You must use an Azure AI multi-service account for this task. For an updated list of regions that provide multimodal embeddings, see the [Azure AI Vision documentation](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
-
 + [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
 ## Limitations
 
-The [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) has limited regional availability, is bound to Azure AI services, and requires a [billable resource](cognitive-search-attach-cognitive-services.md) for transactions that exceed 20 documents per indexer per day. For a lower-cost solution to indexing multimodal content, see [Tutorial: Verbalize images using generative AI](tutorial-document-extraction-image-verbalization.md).
++ The [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) has limited regional availability. For a list of supported regions, see [Document Layout skill> Supported regions](cognitive-search-skill-document-intelligence-layout.md#supported-regions).
 
-## Prepare data 
++ The [Azure AI Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) also has limited regional availability. For an updated list of regions that provide multimodal embeddings, see the [Azure AI Vision documentation](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
 
-Download the following sample PDF:
+## Prepare data
 
-+ [sustainable-ai-pdf](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Accelerating-Sustainability-with-AI-2025.pdf)
+The following instructions apply to Azure Storage which provides the sample data and also hosts the knowledge store. A search service identity needs read access to Azure Storage to retrieve the sample data, and it needs write access to create the knowledge store. The search service creates the container for cropped images during skillset processing, using the name you provide in an environment variable.
 
-### Upload sample data to Azure Storage
+1. Download the following sample PDF: [sustainable-ai-pdf](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Accelerating-Sustainability-with-AI-2025.pdf)
 
-1. In Azure Storage, create a new container named **doc-intelligence-multimodality-container**.
+1. In Azure Storage, create a new container named **sustainable-ai-pdf**.
 
 1. [Upload the sample data file](/azure/storage/blobs/storage-quickstart-blobs-portal).
 
-1. [Create a **Storage Blob Data Reader** role assignment and specify a managed identity in a connection string](search-howto-managed-identities-storage.md)
+1. [Create role assignments and specify a managed identity in a connection string](search-howto-managed-identities-storage.md):
 
-   1. For connections made using a system-assigned managed identity, provide a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
+   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer and **Storage Blob Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
+
+   1. For connections made using a system-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
 
         ```json
         "credentials" : { 
             "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
         }
         ```
-   1. For connections made using a user-assigned managed identity. Provide a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. Provide an identity using the syntax shown in the following example. Set userAssignedIdentity to the user-assigned managed identity The connection string is similar to the following example:
 
-        ```json
-        "credentials" : { 
-            "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
-        },
-        "identity" : { 
-            "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
-            "userAssignedIdentity" : "/subscriptions/00000000-0000-0000-0000-00000000/resourcegroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MY-DEMO-USER-MANAGED-IDENTITY" 
-        }
-    ```
+   1. For connections made using a user-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. Provide an identity using the syntax shown in the following example. Set userAssignedIdentity to the user-assigned managed identity The connection string is similar to the following example:
 
-### Copy a search service URL and API key
+      ```json
+      "credentials" : { 
+          "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
+      },
+      "identity" : { 
+          "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
+          "userAssignedIdentity" : "/subscriptions/00000000-0000-0000-0000-00000000/resourcegroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MY-DEMO-USER-MANAGED-IDENTITY" 
+      }
+      ```
 
-For this tutorial, connections to Azure AI Search require an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Managed identities](search-howto-managed-identities-data-sources.md).
+## Prepare models
 
-1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the search service **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
+This tutorial assumes you have an existing Azure AI multiservice account through which the skill calls the Azure AI Vision multimodal 4.0 embedding model. The search service connects to the model during skillset processing using its managed identity. This section gives you guidance and links for assigning roles for authorized access.
 
-1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
+The same role assignment is also used for accessing the Document Intelligence Layout model via an Azure AI multi-service account.
 
-   :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
+1. Sign in to the Azure portal (not the Foundry portal) and find the Azure AI multiservice account. Make sure it's in a region that provides the [multimodal 4.0 API](/azure/ai-services/computer-vision/overview-image-analysis#region-availability) and the [Document Intelligence Layout model](cognitive-search-skill-document-intelligence-layout.md#supported-regions).
+
+1. Select **Access control (IAM)**.
+
+1. Select **Add** and then **Add role assignment**.
+
+1. Search for **Cognitive Services User** and then select it.
+
+1. Choose **Managed identity** and then assign your [search service managed identity](search-howto-managed-identities-data-sources.md).
 
 ## Set up your REST file
 
+For this tutorial, your local REST client connection to Azure AI Search requires an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Connect to a search service](search-get-started-rbac.md).
+
+For other authenticated connections, the search service uses the role assignments you previously defined.
+
 1. Start Visual Studio Code and create a new file.
 
 1. Provide values for variables used in the request.
 
    ```http
-   @baseUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
-   @apiKey = PUT-YOUR-ADMIN-API-KEY-HERE
+   @searchUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
+   @searchApiKey = PUT-YOUR-ADMIN-API-KEY-HERE
    @storageConnection = PUT-YOUR-STORAGE-CONNECTION-STRING-HERE
    @cognitiveServicesUrl = PUT-YOUR-COGNITIVE-SERVICES-URL-HERE
-   @cognitiveServicesKey= PUT-YOUR-COGNITIVE-SERVICES-URL-KEY-HERE
+   @cognitiveServicesKey= PUT-YOUR-COGNITIVE-SERVICES-API-KEY-HERE
    @modelVersion = PUT-YOUR-VECTORIZE-MODEL-VERSION-HERE
-   @imageProjectionContainer=PUT-YOUR-IMAGE-PROJECTION-CONTAINER-HERE
+   @imageProjectionContainer=PUT-YOUR-IMAGE-PROJECTION-CONTAINER-HERE (Azure AI Search creates this container for you during skills processing)
    ```
 
-1. Save the file using a `.rest` or `.http` file extension.
+1. Save the file using a `.rest` or `.http` file extension. For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
 
-For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
+To get the Azure AI Search endpoint and API key:
+
+1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the search service **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
+
+1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
+
+   :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
 
 ## Create a data source
 
 [Create Data Source (REST)](/rest/api/searchservice/data-sources/create) creates a data source connection that specifies what data to index.
 
 ```http
 ### Create a data source using system-assigned managed identities
-POST {{baseUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
   {
     "name": "doc-intelligence-multimodal-embedding-ds",
@@ -146,9 +164,9 @@ For nested JSON, the index fields must be identical to the source fields. Curren
 
 ```http
 ### Create an index
-POST {{baseUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
 {
     "name": "doc-intelligence-multimodal-embedding-index",
@@ -254,7 +272,7 @@ POST {{baseUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
                 "kind": "aiServicesVision",
                 "aiServicesVisionParameters": {
                     "resourceUri": "{{cognitiveServicesUrl}}",
-                    "apiKey": "{{cognitiveServicesKey}}",
+                    "searchApiKey": "{{cognitiveServicesKey}}",
                     "modelVersion": "{{modelVersion}}"
                 }
             }
@@ -295,9 +313,9 @@ Key points:
 
 ```http
 ### Create a skillset
-POST {{baseUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
 {
   "name": "doc-intelligence-multimodal-embedding-skillset",
@@ -480,9 +498,9 @@ Key points:
 
 ```http
 ### Create and run an indexer
-POST {{baseUrl}}/indexers?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
 
 {
   "dataSourceName": "doc-intelligence-multimodal-embedding-ds",
@@ -512,9 +530,9 @@ You can start searching as soon as the first document is loaded.
 
 ```http
 ### Query the index
-POST {{baseUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
   
   {
     "search": "*",
@@ -546,9 +564,9 @@ For filters, you can also use Logical operators (and, or, not) and comparison op
 
 ```http
 ### Query for only images
-POST {{baseUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
   
   {
     "search": "*",
@@ -559,9 +577,9 @@ POST {{baseUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search
 
 ```http
 ### Query for text or images with content related to energy, returning the id, parent document, and text (only populated for text chunks), and the content path where the image is saved in the knowledge store (only populated for images)
-POST {{baseUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
   Content-Type: application/json
-  api-key: {{apiKey}}
+  api-key: {{searchApiKey}}
   
   {
     "search": "energy",
@@ -576,20 +594,20 @@ Indexers can be reset to clear execution history, which allows a full rerun. The
 
 ```http
 ### Reset the indexer
-POST {{baseUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/reset?api-version=2025-05-01-preview   HTTP/1.1
-  api-key: {{apiKey}}
+POST {{searchUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/reset?api-version=2025-05-01-preview   HTTP/1.1
+  api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Run the indexer
-POST {{baseUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/run?api-version=2025-05-01-preview   HTTP/1.1
-  api-key: {{apiKey}}
+POST {{searchUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/run?api-version=2025-05-01-preview   HTTP/1.1
+  api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Check indexer status 
-GET {{baseUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/status?api-version=2025-05-01-preview   HTTP/1.1
-  api-key: {{apiKey}}
+GET {{searchUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/status?api-version=2025-05-01-preview   HTTP/1.1
+  api-key: {{searchApiKey}}
 ```
 
 ## Clean up resources
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "構造化文書レイアウトからマルチモーダル埋め込み生成に関するチュートリアルの更新"
}
```

### Explanation
この変更は、「構造化文書レイアウトからマルチモーダル埋め込みを生成する」ためのチュートリアル文書の更新を示しています。主な改善点は、PDF文書からテキストと画像を抽出し、それをインデクシングするためのマルチモーダルインデクシングパイプラインを構築する方法が強調されています。このチュートリアルでは、Azure AI Document Intelligence Layoutモデルを利用して文書構造を認識し、データを効果的にチャンク化するプロセスが詳細に説明されています。

また、Azure AI Visionのマルチモーダル埋め込みスキルを活用してテキストと画像をベクトル化し、検索可能なインデックスに格納する方法が示されています。これにより、ユーザーは同じ文書からの異なる形式の情報を統合的に検索できるようになります。

さらに、前提条件の項目が整理され、Azure AIマルチサービスアカウントに関する情報や、Azure Storageを利用する手順が明確になっています。リソースの役割を適切に設定するための手順も追加されており、ユーザーにとって操作が容易になっています。全体として、この更新はドキュメント管理と情報検索における利便性を向上させることを目的としています。

## articles/search/vector-search-vectorizer-azure-open-ai.md{#item-e75cee}

<details>
<summary>Diff</summary>
````diff
@@ -4,12 +4,11 @@ titleSuffix: Azure AI Search
 description: Connects to a deployed model on your Azure OpenAI resource at query time.
 author: HeidiSteen
 ms.author: heidist
-ms.reviewer: chalton
 ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: reference
-ms.date: 10/16/2024
+ms.date: 07/29/2025
 ---
 
 # Azure OpenAI vectorizer
@@ -29,6 +28,8 @@ Vectorizers are used at query time, but specified in index definitions, and refe
 
 Your Azure OpenAI in Azure AI Foundry Models must have an associated [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains). If the service was created through the Azure portal, this subdomain is automatically generated as part of your service setup. Ensure that your service includes a custom subdomain before using it with the Azure AI Search integration.
 
+If you create an AI Service using Azure AI Foundry, it will automatically generate an endpoint with the domain cognitiveservices.azure.com. When you deploy an Azure OpenAI embedding model in this service, you can change the endpoint to use openai.azure.com domain instead, when using it in this skill. For example, change your endpoint from `https://<yourendpoint>.cognitiveservices.azure.com` to `https://<yourendpoint>.openai.azure.com`. Use this updated endpoint as the value for the `resourceUri` property for this skill. 
+
 Azure OpenAI resources (with access to embedding models) that were created in Azure AI Foundry portal aren't supported. Only the Azure OpenAI resources created in the Azure portal are compatible with the **Azure OpenAI Embedding** skill integration. 
 
 ## Vectorizer parameters
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI ベクトライザーに関するドキュメントの更新"
}
```

### Explanation
この変更は、「Azure OpenAI ベクトライザー」に関するドキュメントの更新を含んでいます。主な修正点は、日付の更新と、Azure AI Foundryを使用してAIサービスを作成する際の新しいエンドポイントについての説明が追加されたことです。

具体的には、AIサービスをAzure AI Foundryで作成すると、自動的に`cognitiveservices.azure.com`というドメインでエンドポイントが生成され、Azure OpenAI埋め込みモデルをこのサービスにデプロイした際には、エンドポイントを`openai.azure.com`に変更できることが明記されています。これにより、ユーザーはスキルで使用する際に新しいエンドポイントを`resourceUri`プロパティの値として設定することができます。

加えて、Azure AI Foundryポータルで作成されたAzure OpenAIリソースには、埋め込みモデルへのアクセスが提供されないことも明確に記されています。これにより、ユーザーはどのリソースがAzure OpenAI Embeddingスキル統合と互換性があるかを理解できるようになります。全体的に、これらのアップデートは、Azure AI Searchとの統合をよりスムーズにすることを目的としています。


