---
date: '2026-08-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2cb7c3b...MicrosoftDocs:8ce8c73
summary: Azure AI Searchのドキュメントが更新され、新しい認証方式や画像サービングのサポート状況の変更、内部構築方法の明確化が行われました。この変更により、ユーザーは知識ソースの管理をより安全かつ効率的に理解できるようになります。主な新機能としては、Azure
  Blob Storageに対する画像サービングの支援や、ドキュメントに埋め込まれた画像を回答合成モデルに供給する機能が追加されました。一方、Bearトークンベースの認証方式への移行が進められ、旧APIキー形式の使用は非推奨となり、特定の条件下では画像サービングがサポートされなくなります。また、構成パラメータの説明が改善され、ユーザーにとってより理解しやすい内容に更新されています。この更新は、Azure
  AI Searchのセキュリティと使いやすさを向上させ、信頼性あるサービスを提供することを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2cb7c3b...MicrosoftDocs:8ce8c73){target="_blank"}

<format>
# ハイライト
Azure AI Search のドキュメントが複数の側面で更新されました。これには、新しい認証方式の導入、画像サービングのサポート状況の変更、内部構築方法の明確化が含まれます。これにより、ユーザーはより安全で効率的に知識ソースを管理する手法を理解しやすくなります。

## 新機能
- Azure Blob Storageに対する画像サービングの支援が強調され、ユーザーは管理されたインジェストを通じた画像の抽出方法のサンプルを得られます。
- `enableImageServing`パラメータを用いることで、ドキュメントに埋め込まれた画像を回答合成モデルに供給する機能が追加されました。

## 破壊的な変更
- 複数のドキュメントに渡るBearトークンベースの認証方式への移行が行われ、旧APIキー形式での呼び出しは非推奨となります。
- `ingestionPermissionOptions`を有効化した場合、画像サービングがサポートされなくなっています。

## その他の更新
- 構成パラメータの説明が明確化され、ユーザーはAzureのコグニティブサーチやBlob Knowledge Sourceのインジェスト手順と要件をより深く理解できるようになりました。
- エラーと警告のドキュメントが修正され、ユーザーはより適切な対応法を見つけやすくなります。

# インサイト
この更新はAzure AI Searchのセキュリティと使いやすさを強化するためのものであり、特に画像サービングに関するサポートとインデクサーの使用に関するプロセスが重視されています。新たに紹介されたBearトークンを用いた認証手法によってセキュリティを強化しつつ、ユーザーと開発者が直感的に利用できるインターフェースデザインが考慮されています。また、技術的更新によって最新のAzureセキュリティポリシーと整合しており、サービスの信頼性が向上します。これらの改善によって、複雑な検索リソースの管理がより洗練され、ユーザーは様々なアクセス制御オプションを活用しながら、さらに効率的に操作できるようになります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-blob.md](#item-ac6c8a) | minor update | Blob Knowledge Sourceの作成方法の更新 | modified | 17 | 28 | 45 | 
| [agentic-knowledge-source-how-to-onelake.md](#item-ec7a80) | minor update | OneLake Knowledge Sourceの作成方法の更新 | modified | 10 | 22 | 32 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed.md](#item-fe72fc) | minor update | SharePointインデクサーの作成方法の更新 | modified | 7 | 14 | 21 | 
| [agentic-knowledge-source-overview.md](#item-dcf29a) | minor update | 知識ソースの概要の更新 | modified | 2 | 0 | 2 | 
| [agentic-retrieval-how-to-image-serving.md](#item-48db70) | minor update | 画像サービングに関するドキュメントの更新 | modified | 114 | 93 | 207 | 
| [agentic-retrieval-how-to-retrieve.md](#item-d739cf) | minor update | 取得応答における画像サービングの表現変更 | modified | 4 | 4 | 8 | 
| [cognitive-search-common-errors-warnings.md](#item-a5c854) | minor update | 一般的なエラーと警告の文書更新 | modified | 3 | 3 | 6 | 
| [cognitive-search-skill-document-extraction.md](#item-072b72) | minor update | 文書抽出スキルの構成パラメータの明確化 | modified | 10 | 10 | 20 | 
| [knowledge-source-check.md](#item-e19bd3) | minor update | 知識ソースチェックの認証方式を更新 | modified | 3 | 3 | 6 | 
| [knowledge-source-delete.md](#item-4a16f9) | minor update | 知識ソース削除手順の認証方式を更新 | modified | 7 | 7 | 14 | 
| [knowledge-source-status.md](#item-8d20e6) | minor update | 知識ソースの状態確認手順の認証方式を更新 | modified | 2 | 2 | 4 | 
| [samples-dotnet.md](#item-12f3fa) | minor update | .NET サンプルの更新と新しいサンプルの追加 | modified | 2 | 2 | 4 | 
| [samples-python.md](#item-d2bf09) | minor update | Python サンプルの更新と新しいサンプルの追加 | modified | 2 | 1 | 3 | 
| [search-document-level-access-overview.md](#item-4bb055) | minor update | ドキュメントレベルアクセス制御の選択肢に関する更新 | modified | 3 | 1 | 4 | 
| [search-how-to-multiple-indexers-one-index.md](#item-5ccefd) | minor update | ストレージアカウント権限のスコープに関する明確化 | modified | 1 | 1 | 2 | 
| [search-indexer-access-control-lists-and-role-based-access.md](#item-67b42f) | minor update | ナレッジストアに関する情報の更新 | modified | 1 | 1 | 2 | 
| [search-indexer-sensitivity-labels.md](#item-2a7bfc) | minor update | 感度ラベルおよびナレッジストアに関する明確化 | modified | 2 | 2 | 4 | 
| [search-indexer-sharepoint-access-control-lists.md](#item-532a24) | minor update | SharePointのアクセ制御リストに関する情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-blob.md{#item-ac6c8a}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Create a Blob Knowledge Source for Agentic Retrieval
 description: Learn how to create a blob knowledge source in Azure AI Search that ingests content from Azure Blob Storage or ADLS Gen2 for agentic retrieval.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/08/2026
+ms.date: 08/18/2026
 ai-usage: ai-assisted
 ms.custom: doc-kit-assisted
 zone_pivot_groups: search-csharp-python-rest
@@ -54,9 +54,11 @@ The generated indexer conforms to the *blob indexer*, whose prerequisites, suppo
 
 + A blob container with [supported content types](search-how-to-index-azure-blob-storage.md#supported-document-formats) for text content. For optional image verbalization, the supported content type depends on whether your chat completion model can analyze and describe the image file.
 
++ If `contentExtractionMode` is `standard`, use a Microsoft Foundry resource in a [region supported by Content Understanding in Foundry Tools](/azure/ai-services/content-understanding/language-region-support) and the `https://<resource-name>.services.ai.azure.com` endpoint. Deploy an embedding model, and deploy a multimodal chat model if you enable image verbalization.
+
 + Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Contributor** roles assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
 
-+ If the knowledge source specifies an Azure OpenAI model for embeddings or image verbalization, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource.
++ A [managed identity](search-how-to-managed-identities.md) for the search service with **Storage Blob Data Reader** at the source storage-account scope and **Cognitive Services User** on the Microsoft Foundry resource. If you configure an asset store in a different storage account, also assign **Storage Blob Data Contributor** at that storage-account scope. If the source and asset containers share an account, **Storage Blob Data Contributor** provides both source read access and asset-store read/write access.
 
 ::: zone pivot="csharp"
 
@@ -162,7 +164,7 @@ Run the following code to create a blob knowledge source.
 // Create a blob knowledge source
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
-using Azure.Search.Documents.Models;
+using Azure.Search.Documents.KnowledgeBases.Models;
 using Azure;
 
 var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
@@ -289,7 +291,8 @@ Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated
 # Create a blob knowledge source
 from azure.core.credentials import AzureKeyCredential
 from azure.search.documents.indexes import SearchIndexClient
-from azure.search.documents.indexes.models import AzureBlobKnowledgeSource, AzureBlobKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceAzureOpenAIVectorizer, KnowledgeSourceContentExtractionMode, KnowledgeSourceIngestionParameters
+from azure.search.documents.indexes.models import AzureBlobKnowledgeSource, AzureBlobKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceContentExtractionMode
+from azure.search.documents.knowledgebases.models import KnowledgeSourceAzureOpenAIVectorizer, KnowledgeSourceIngestionParameters
 
 index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
 
@@ -396,7 +399,7 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 ```http
 ### Create a blob knowledge source
 PUT {{search-url}}/knowledgesources/my-blob-ks?api-version=2026-05-01-preview
-api-key: {{api-key}}
+Authorization: Bearer {{token}}
 Content-Type: application/json
 
 {
@@ -405,7 +408,7 @@ Content-Type: application/json
   "description": "This knowledge source pulls from a blob storage container.",
   "encryptionKey": null,
   "azureBlobParameters": {
-    "connectionString": "<YOUR AZURE STORAGE CONNECTION STRING>",
+  "connectionString": "ResourceId=<storage-resource-id>",
     "containerName": "<YOUR BLOB CONTAINER NAME>",
     "folderPath": null,
     "isADLSGen2": false,
@@ -417,17 +420,15 @@ Content-Type: application/json
             "azureOpenAIParameters": {
                 "resourceUri": "{{aoai-endpoint}}",
                 "deploymentId": "{{aoai-gpt-deployment}}",
-                "modelName": "{{aoai-gpt-model}}",
-                "apiKey": "{{aoai-key}}"
+                "modelName": "{{aoai-gpt-model}}"
             }
         },
         "embeddingModel": {
             "kind": "azureOpenAI",
             "azureOpenAIParameters": {
                 "resourceUri": "{{aoai-endpoint}}",
                 "deploymentId": "{{aoai-embedding-deployment}}",
-                "modelName": "{{aoai-embedding-model}}",
-                "apiKey": "{{aoai-key}}"
+                "modelName": "{{aoai-embedding-model}}"
             }
         },
         "contentExtractionMode": "minimal",
@@ -445,7 +446,7 @@ Content-Type: application/json
 ```http
 ### Create a blob knowledge source
 PUT {{search-url}}/knowledgesources/my-blob-ks?api-version=2026-04-01
-api-key: {{api-key}}
+Authorization: Bearer {{token}}
 Content-Type: application/json
 
 {
@@ -454,7 +455,7 @@ Content-Type: application/json
   "description": "This knowledge source pulls from a blob storage container.",
   "encryptionKey": null,
   "azureBlobParameters": {
-    "connectionString": "<YOUR AZURE STORAGE CONNECTION STRING>",
+  "connectionString": "ResourceId=<storage-resource-id>",
     "containerName": "<YOUR BLOB CONTAINER NAME>",
     "folderPath": null,
     "isADLSGen2": false,
@@ -466,17 +467,15 @@ Content-Type: application/json
             "azureOpenAIParameters": {
                 "resourceUri": "{{aoai-endpoint}}",
                 "deploymentId": "{{aoai-gpt-deployment}}",
-                "modelName": "{{aoai-gpt-model}}",
-                "apiKey": "{{aoai-key}}"
+                "modelName": "{{aoai-gpt-model}}"
             }
         },
         "embeddingModel": {
             "kind": "azureOpenAI",
             "azureOpenAIParameters": {
                 "resourceUri": "{{aoai-endpoint}}",
                 "deploymentId": "{{aoai-embedding-deployment}}",
-                "modelName": "{{aoai-embedding-model}}",
-                "apiKey": "{{aoai-key}}"
+                "modelName": "{{aoai-embedding-model}}"
             }
         },
         "contentExtractionMode": "minimal",
@@ -509,30 +508,20 @@ If you're satisfied with the knowledge source, [add it to a knowledge base](agen
 
 ## Query a knowledge base
 
-After the knowledge base is configured, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query the knowledge source. This knowledge source supports optional configurations for document-level permissions enforcement and document-embedded image surfacing.
+After you configure the knowledge base, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query the knowledge source. Choose the configuration that matches your scenario.
 
 ### Enforce document-level permissions (preview)
 
 To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time (preview)](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time-preview).
 
 ### Surface document-embedded images (preview)
 
-To surface document-embedded images (such as diagrams or scans) in answer synthesis responses, configure `assetStore` on this knowledge source, and then enable image serving on the knowledge base. For more information, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
+To surface document-embedded images (such as diagrams or scans) in answer synthesis responses, configure `assetStore` on this knowledge source, and then enable image serving on the knowledge base. Image serving isn't supported when `ingestionPermissionOptions` is configured. For more information, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
 
 ## Delete a knowledge source
 
 [!INCLUDE [Delete a knowledge source](includes/how-tos/knowledge-source-delete.md)]
 
-## Known errors
-
-When you create this knowledge source with `contentExtractionMode` set to `standard`, you might get the following error.
-
-```json
-Failed to create custom analyzer 'azs_tmp': BadRequest - {"error":{"code":"InvalidRequest","message":"Invalid request.","innererror":{"code":"DefaultsNotSet","message":"Defaults have not yet been set. Call 'PATCH /contentunderstanding/defaults' first."}}}
-```
-
-To resolve the error, define the default values as instructed in the [Content Understanding prerequisites](/azure/ai-services/content-understanding/tutorial/create-custom-analyzer?tabs=portal%2Cdocument&pivots=programming-language-rest#prerequisites). Afterwards, you can proceed with creating the knowledge source.
-
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blob Knowledge Sourceの作成方法の更新"
}
```

### Explanation
この変更は、Azure AI SearchのBlob Knowledge Sourceに関するドキュメントの更新です。主な修正内容には、日付の更新、サポートされるコンテンツタイプの説明、システム要件に関する新しい指示、認証手順の強化、および使用されるコードスニペットの整理が含まれています。

具体的には、`ms.date`フィールドが2026年8月8日から2026年8月18日に変更され、新しいパラメーターが追加され、Azure OpenAIリソースを使用する際の必要条件が明確にされました。また、ドキュメント内のコードスニペットにおいて、インポートされるモジュールが調整され、API呼び出し方法が更新され、接続文字列がセキュリティを考慮した形で変更されています。さらに、文書に埋め込まれた画像のサポートや、ユーザーのアクセス権を管理する方法についても更新が加えられました。

このように、ドキュメントは最新の機能や使用法を反映するために改善されており、ユーザーがBlob Knowledge Sourceを効果的に作成および管理できるように配慮されています。

## articles/search/agentic-knowledge-source-how-to-onelake.md{#item-ec7a80}

<details>
<summary>Diff</summary>
````diff
@@ -51,6 +51,8 @@ The generated indexer conforms to the *OneLake indexer*, whose prerequisites, su
 
 + Completion of the [OneLake indexer data preparation](search-how-to-index-onelake-files.md#prepare-data-for-indexing).
 
++ If `contentExtractionMode` is `standard`, use a Microsoft Foundry resource in a [region supported by Content Understanding in Foundry Tools](/azure/ai-services/content-understanding/language-region-support) and the `https://<resource-name>.services.ai.azure.com` endpoint. Deploy an embedding model, and deploy a multimodal chat model if you enable image verbalization.
+
 + Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Contributor** roles assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
 
 + If the knowledge source specifies an Azure OpenAI model for embeddings or image verbalization, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource.
@@ -378,7 +380,7 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 ```http
 ### Create an indexed OneLake knowledge source
 PUT {{search-url}}/knowledgesources/my-onelake-ks?api-version=2026-05-01-preview
-api-key: {{api-key}}
+Authorization: Bearer {{token}}
 Content-Type: application/json
 
 {
@@ -397,17 +399,15 @@ Content-Type: application/json
             "azureOpenAIParameters": {
                 "resourceUri": "{{aoai-endpoint}}",
                 "deploymentId": "{{aoai-gpt-deployment}}",
-                "modelName": "{{aoai-gpt-model}}",
-                "apiKey": "{{aoai-key}}"
+                "modelName": "{{aoai-gpt-model}}"
             }
         },
         "embeddingModel": {
             "kind": "azureOpenAI",
             "azureOpenAIParameters": {
                 "resourceUri": "{{aoai-endpoint}}",
                 "deploymentId": "{{aoai-embedding-deployment}}",
-                "modelName": "{{aoai-embedding-model}}",
-                "apiKey": "{{aoai-key}}"
+                "modelName": "{{aoai-embedding-model}}"
             }
         },
         "contentExtractionMode": "minimal",
@@ -425,7 +425,7 @@ Content-Type: application/json
 ```http
 ### Create an indexed OneLake knowledge source
 PUT {{search-url}}/knowledgesources/my-onelake-ks?api-version=2026-04-01
-api-key: {{api-key}}
+Authorization: Bearer {{token}}
 Content-Type: application/json
 
 {
@@ -444,17 +444,15 @@ Content-Type: application/json
             "azureOpenAIParameters": {
                 "resourceUri": "{{aoai-endpoint}}",
                 "deploymentId": "{{aoai-gpt-deployment}}",
-                "modelName": "{{aoai-gpt-model}}",
-                "apiKey": "{{aoai-key}}"
+                "modelName": "{{aoai-gpt-model}}"
             }
         },
         "embeddingModel": {
             "kind": "azureOpenAI",
             "azureOpenAIParameters": {
                 "resourceUri": "{{aoai-endpoint}}",
                 "deploymentId": "{{aoai-embedding-deployment}}",
-                "modelName": "{{aoai-embedding-model}}",
-                "apiKey": "{{aoai-key}}"
+                "modelName": "{{aoai-embedding-model}}"
             }
         },
         "contentExtractionMode": "minimal",
@@ -489,30 +487,20 @@ For any knowledge base that specifies an indexed OneLake knowledge source, be su
 
 ## Query a knowledge base
 
-After the knowledge base is configured, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query the knowledge source. This knowledge source supports optional configurations for document-level permissions enforcement and document-embedded image surfacing.
+After you configure the knowledge base, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query the knowledge source. Choose the configuration that matches your scenario.
 
 ### Enforce document-level permissions (preview)
 
 To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time (preview)](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time-preview).
 
 ### Surface document-embedded images (preview)
 
-To surface document-embedded images (such as diagrams or scans) in answer synthesis responses, configure `assetStore` on this knowledge source, and then enable image serving on the knowledge base. For more information, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
+To surface document-embedded images (such as diagrams or scans) in answer synthesis responses, configure `assetStore` on this knowledge source, and then enable image serving on the knowledge base. Image serving isn't supported when `ingestionPermissionOptions` is configured. For more information, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
 
 ## Delete a knowledge source
 
 [!INCLUDE [Delete a knowledge source](includes/how-tos/knowledge-source-delete.md)]
 
-## Known errors
-
-When you create this knowledge source with `contentExtractionMode` set to `standard`, you might get the following error.
-
-```json
-Failed to create custom analyzer 'azs_tmp': BadRequest - {"error":{"code":"InvalidRequest","message":"Invalid request.","innererror":{"code":"DefaultsNotSet","message":"Defaults have not yet been set. Call 'PATCH /contentunderstanding/defaults' first."}}}
-```
-
-To resolve the error, define the default values as instructed in the [Content Understanding prerequisites](/azure/ai-services/content-understanding/tutorial/create-custom-analyzer?tabs=portal%2Cdocument&pivots=programming-language-rest#prerequisites). Afterwards, you can proceed with creating the knowledge source.
-
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLake Knowledge Sourceの作成方法の更新"
}
```

### Explanation
この変更は、OneLake Knowledge Sourceに関するドキュメントの更新を反映しています。具体的には、OneLakeインデクサーに関連するデータ準備の完了を強調する新しい指示が追加され、システム要件と認証手順が明確化されています。更新されたドキュメントは、Azure AI SearchにおけるOneLake Knowledge Sourceの作成や管理について最新のガイダンスを提供します。

変更では、`contentExtractionMode`が`standard`の場合にMicrosoft Foundryリソースを使用する指示が追加され、知識ソースの作成に必要な権限を設定するための手順も更新されました。また、API呼び出しの関連部分には、Bearerトークンによる認証の記述が追加され、セキュリティが強化されています。

さらに、文書内の構造や文言も調整され、関連する情報源へのリンクが提供されることにより、ユーザーにとっての利便性が向上しています。これにより、読み手はOneLake Knowledge Sourceを作成する際の新しい要件や手順を理解しやすくなっています。

## articles/search/agentic-knowledge-source-how-to-sharepoint-indexed.md{#item-fe72fc}

<details>
<summary>Diff</summary>
````diff
@@ -57,6 +57,8 @@ The generated indexer conforms to the *SharePoint in Microsoft 365 indexer*, who
 
   + [Step 3: Create a Microsoft Entra application registration](search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration) (for application permissions, you also configure a [client secret](search-how-to-index-sharepoint-online.md#using-client-secret) or [secretless authentication](search-how-to-index-sharepoint-online.md#using-secretless-authentication-to-obtain-application-tokens))
 
++ If `contentExtractionMode` is `standard`, use a Microsoft Foundry resource in a [region supported by Content Understanding in Foundry Tools](/azure/ai-services/content-understanding/language-region-support) and the `https://<resource-name>.services.ai.azure.com` endpoint. Deploy an embedding model, and deploy a multimodal chat model if you enable image verbalization.
+
 + Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Contributor** roles assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
 
 + If the knowledge source specifies an Azure OpenAI model for embeddings or image verbalization, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource.
@@ -245,7 +247,7 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 ```http
 ### Create an indexed SharePoint knowledge source
 PUT {{search-url}}/knowledgesources/my-indexed-sharepoint-ks?api-version=2026-05-01-preview
-api-key: {{api-key}}
+Authorization: Bearer {{token}}
 Content-Type: application/json
 
 {
@@ -254,7 +256,7 @@ Content-Type: application/json
     "description": "A sample indexed SharePoint knowledge source.",
     "encryptionKey": null,
     "indexedSharePointParameters": {
-        "connectionString": "{{sharepoint-connection-string}}",
+        "connectionString": "{{sharepoint-federated-connection-string}}",
         "containerName": "defaultSiteLibrary",
         "query": null,
         "ingestionParameters": {
@@ -264,8 +266,7 @@ Content-Type: application/json
                 "azureOpenAIParameters": {
                     "deploymentId": "text-embedding-3-large",
                     "modelName": "text-embedding-3-large",
-                    "resourceUri": "{{aoai-endpoint}}",
-                    "apiKey": "{{aoai-key}}"
+                    "resourceUri": "{{aoai-endpoint}}"
                 }
             },
             "chatCompletionModel": null,
@@ -298,7 +299,7 @@ For any knowledge base that specifies an indexed SharePoint knowledge source, be
 
 ## Query a knowledge base
 
-After the knowledge base is configured, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query the knowledge source. This knowledge source supports optional configurations for document-level permissions enforcement and document-embedded image surfacing.
+After you configure the knowledge base, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query the knowledge source. Choose the configuration that matches your scenario.
 
 ### Enforce document-level permissions
 
@@ -308,7 +309,7 @@ For missing, unexpected, or failed results from an indexed SharePoint permission
 
 ### Surface document-embedded images
 
-To surface document-embedded images (such as diagrams or scans) in answer synthesis responses, configure `assetStore` on this knowledge source, and then enable image serving on the knowledge base. For more information, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
+To surface document-embedded images (such as diagrams or scans) in answer synthesis responses, configure `assetStore` on this knowledge source, and then enable image serving on the knowledge base. Image serving isn't supported when `ingestionPermissionOptions` is configured. For more information, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
 
 ## Delete a knowledge source
 
@@ -318,14 +319,6 @@ To surface document-embedded images (such as diagrams or scans) in answer synthe
 
 The generated SharePoint data source and indexer use the same Microsoft Entra tenant validation and authentication behavior as directly configured SharePoint indexers. For tenant-related failures, review the [generated indexer's status and execution history](search-monitor-indexers.md), and then follow the [`Invalid AAD tenant` remediation](cognitive-search-common-errors-warnings.md#error-invalid-aad-tenant).
 
-When you create this knowledge source with `contentExtractionMode` set to `standard`, you might get the following error.
-
-```json
-Failed to create custom analyzer 'azs_tmp': BadRequest - {"error":{"code":"InvalidRequest","message":"Invalid request.","innererror":{"code":"DefaultsNotSet","message":"Defaults have not yet been set. Call 'PATCH /contentunderstanding/defaults' first."}}}
-```
-
-To resolve the error, define the default values as instructed in the [Content Understanding prerequisites](/azure/ai-services/content-understanding/tutorial/create-custom-analyzer?tabs=portal%2Cdocument&pivots=programming-language-rest#prerequisites). Afterwards, you can proceed with creating the knowledge source.
-
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointインデクサーの作成方法の更新"
}
```

### Explanation
この変更は、SharePoint Knowledge Sourceの作成に関するドキュメントの最新のアップデートを示しています。具体的には、Microsoft Entraアプリケーションの登録手順、必要な認証の設定、OneLakeインデクサーに関連する新しい指示が追加され、構成手順が明確になっています。

新たに追加された部分では、`contentExtractionMode`が`standard`である場合にMicrosoft Foundryリソースを利用するよう指示されています。また、知識ソースの作成に必要な権限設定についても強調され、API呼び出しにおいてBearerトークンによる認証が導入されました。さらに、接続文字列が「`sharepoint-connection-string`」から「`sharepoint-federated-connection-string`」に変更され、セキュリティが強化されています。

ドキュメントの他の部分でも、関連する情報源へのリンクが整備されており、文書内での手順が整理されているため、ユーザーにとっての理解が容易になっています。これにより、SharePoint Knowledge Sourceを作成する際の要件や手順が最新の情報に基づいて提供され、利便性が向上しています。

## articles/search/agentic-knowledge-source-overview.md{#item-dcf29a}

<details>
<summary>Diff</summary>
````diff
@@ -93,6 +93,8 @@ If your indexed knowledge source uses a chunked index, such as with integrated v
 
 For blob, indexed OneLake, and indexed SharePoint knowledge sources, you can configure an `assetStore` in the knowledge source's `ingestionParameters` to persist images that are embedded in your source documents. When you also enable image serving on the knowledge base, the [retrieve action](agentic-retrieval-how-to-retrieve.md) injects those images into the answer synthesis prompt so the LLM can reason over diagrams, charts, and extracted image content. For more information, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
 
+Don't configure `assetStore` and `ingestionPermissionOptions` on the same knowledge source. Image serving isn't supported when `ingestionPermissionOptions` is configured.
+
 ## Using knowledge sources
 
 After you create a knowledge source, reference it in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md). The knowledge base determines which knowledge sources to query. The following sections describe options for controlling which sources are included and how the engine selects among them.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ソースの概要の更新"
}
```

### Explanation
この変更は、知識ソースの概要に関する文書の内容を最新の状態に更新することを目的としています。具体的には、`assetStore`と`ingestionPermissionOptions`を同じ知識ソースで設定しないようにという警告が追加され、画像サービングが`ingestionPermissionOptions`が設定されている場合にはサポートされないことが明確に示されています。

これにより、ユーザーは設定時の注意点を理解しやすくなり、誤った構成による問題を避けることができます。また、新しいセクション「Using knowledge sources」も追加され、知識ソースを作成した後にそれをどのように知識ベースに参照するか、そして知識ベースがどのように知識ソースを決定するかに関する情報が提供されています。この改善により、読者は関連する手順や選択オプションをより良く把握できるようになっています。

## articles/search/agentic-retrieval-how-to-image-serving.md{#item-48db70}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Use image serving in Azure AI Search to inject document-embedded im
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/02/2026
+ms.date: 08/18/2026
 ai-usage: ai-assisted
 ---
 
@@ -43,73 +43,81 @@ This article shows you how to enable image serving on a knowledge base, override
   + [Indexed OneLake knowledge source](agentic-knowledge-source-how-to-onelake.md)
   + [Indexed SharePoint knowledge source](agentic-knowledge-source-how-to-sharepoint-indexed.md)
 
+  For blob knowledge sources that use standard extraction, complete the [blob knowledge source prerequisites](agentic-knowledge-source-how-to-blob.md#prerequisites).
+
++ The knowledge source must not configure `ingestionPermissionOptions`.
+
 + Source documents that contain extractable images, such as PNG files, JPEG files, or PDFs with embedded images.
 
-+ Permissions to update the knowledge base and the knowledge source. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ A Microsoft Foundry resource in a [region supported by Azure Content Understanding in Foundry Tools](/azure/ai-services/content-understanding/language-region-support), with Azure OpenAI embedding and multimodal chat model deployments. Use the resource endpoint in the `https://<resource-name>.services.ai.azure.com` format.
+
++ Permissions to create or update the knowledge base and managed knowledge source. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Contributor** roles assigned to the user or automation identity that performs these management operations (recommended). Alternatively, use an [API key](search-security-api-keys.md).
+
++ Permissions to call the retrieve action. Assign the **Search Index Data Reader** role to the identity that sends retrieve requests (recommended) or use an API key.
 
 + For outbound calls to the LLM during answer synthesis, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource that hosts the LLM.
 
-+ For asset store access, the search service managed identity needs **Storage Blob Data Contributor** on the storage account (or container scope) that hosts the asset store. For more information, see [Configure asset store and application access](#configure-asset-store-and-application-access).
++ For asset store access, configure the search service managed identity as described in [Configure asset store and application access](#configure-asset-store-and-application-access).
 
 + The [2026-05-01-preview](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) REST API or an equivalent Azure SDK preview package: [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md)
 
 ## Limitations and considerations
 
-+ Image serving is available only through the `retrieve` API in agentic retrieval. Classic `/docs/search` queries don't return images without a custom solution or configuration.
++ Image serving is available only through the `retrieve` API in agentic retrieval. Classic `/docs/search` queries don't supply document-embedded images to downstream answer synthesis without a custom solution or configuration.
 
 + Image serving runs only in [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md) output mode. The `extractiveData` output mode skips image serving.
 
 + Image serving applies only to file-based indexed knowledge sources that have `assetStore` configured and indexed chunks with populated `image_path` values.
 
-+ In mixed knowledge bases, only supported knowledge source kinds (blob, indexed OneLake, and indexed SharePoint) return images. Other kinds can still contribute text grounding, but they don't return images.
-
-+ If Microsoft Purview sensitivity labels are enabled on the knowledge source, image serving isn't supported because images can't be exported to the asset store.
++ In mixed knowledge bases, only supported knowledge source kinds (blob, indexed OneLake, and indexed SharePoint) supply document-embedded images to downstream answer synthesis. Other kinds can still contribute text grounding.
 
-+ The retrieve response returns image references in the asset store, not inline Base64 image bytes. Inline image bytes in the response payload aren't supported because they increase payload size and can degrade latency and overall performance.
++ Image serving isn't supported for knowledge sources that use `ingestionPermissionOptions` to ingest document-level permissions, including ACLs, RBAC scopes, or Microsoft Purview sensitivity labels. The asset store creates an underlying knowledge store, and knowledge stores don't support permission inheritance.
 
-+ Image serving doesn't bypass index-level security. To control who can see image references, use [document-level access control](search-document-level-access-overview.md) on the underlying knowledge source. Set `ingestionPermissionOptions` at ingestion time and pass the user's access token at query time. For more information, see [Enforce permissions at query time (preview)](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time-preview).
++ The retrieve response schema doesn't define fields for the individual asset-store image paths or image bytes sent to the model. The `imageServing` activity reports aggregate statistics for the images retrieved and sent to the model.
 
-+ Document-level permissions apply only to index content. They don't automatically propagate to the asset store. Any identity with read access to the asset store container can fetch images. If you need per-document authorization for image retrieval, place a service layer in front of blob access and validate caller permissions before returning the blob.
++ Access to images is controlled at the storage-account level, independently of access to indexed content. Any identity with read access to the asset storage account can fetch its images.
 
 + Don't store secrets (account keys, tokens, connection strings) in source documents because content can be returned as grounding data.
 
-+ Image serving can increase answer synthesis latency because of image download and multimodal token processing. Use the [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md) and filtered results to control overhead.
++ Image serving can increase answer synthesis latency because of image download and multimodal token processing. Run representative queries with image serving enabled and disabled and compare response latency with the reported `imageServing` activity.
+
++ Content Understanding can produce different image results for PDF and DOCX files. If consistent embedded-image extraction and verbalization are required, convert source documents to PDF or test each source format with representative content.
 
 ## How image serving works
 
 Image serving has two phases:
 
-+ **Indexing:** When you configure an asset store on a knowledge source, the search service extracts images from each source document and writes them to your Azure Blob asset store. Optionally, it also calls an LLM to generate a text description (*verbalization*) for each image and stores that description in the index next to the chunk that references the image.
++ **Indexing:** When you configure standard content extraction and an asset store on a knowledge source, the generated Content Understanding skill semantically chunks the document, preserves tables as Markdown, and uses the configured LLM to describe embedded figures. Figure descriptions become part of the enriched Markdown that the embedding skill vectorizes. The skill also extracts images to your blob asset store and adds `image_path` references to overlapping chunks.
 
     When you configure an asset store, the search service also provisions a [knowledge store](knowledge-store-concept-intro.md) alongside the knowledge source to persist the extracted image artifacts. You can inspect and manage this knowledge store like any other.
 
-+ **Retrieval:** When the retrieve action runs with image serving enabled, the search service fetches the matching images from the asset store, base64-encodes them, and includes them as multimodal content in the answer synthesis prompt. Image bytes aren't returned in the retrieve response; only references (the `image_path` field on each contributing chunk) are.
-
-<!--
-Authoring placeholder: Two-phase architecture diagram for image serving.
-
-Phase 1 (top, "Indexing"): Source document -> Skillset (image extraction + optional verbalization via LLM) -> outputs: (1) Asset store (blob container) holding extracted images, (2) Search index holding chunks with image_path and optional text descriptions.
-
-Phase 2 (bottom, "Retrieval"): Retrieve request -> Search service fetches matching chunks from index -> downloads referenced images from asset store -> base64-encodes images and sends them with text content to LLM -> Synthesized answer plus activity (imageServing block) returned to caller. Application separately reads image_path values and fetches blobs from asset store using its own identity.
--->
++ **Retrieval:** When the retrieve action runs with image serving enabled, the search service fetches the matching images from the asset store, base64-encodes them, and includes them as multimodal content in the answer synthesis prompt.
 
 ## Configure asset store and application access
 
 Image serving spans three trust boundaries. At indexing time, the search service writes image artifacts to your asset store. At query time, the search service reads from the asset store to retrieve images. Your application also reads from the asset store if it needs to render images in a UI. Configure each path to follow least-privilege access.
 
 ### Search service access to the asset store
 
-+ Use Microsoft Entra ID and a [managed identity](search-how-to-managed-identities.md) for the search service. Assign the identity the **Storage Blob Data Contributor** role on the storage account (or container scope) so the indexer can write image artifacts and the retrieve action can read them back.
++ Use Microsoft Entra ID and a [managed identity](search-how-to-managed-identities.md) for the search service. Assign the identity the **Storage Blob Data Contributor** role at the storage-account scope because the indexer writes image artifacts and the retrieve action reads them. When the source and asset containers share that account, the role also provides source-blob read access.
 
 + Don't enable anonymous public access on the asset store container.
 
 ### Application access to image references
 
-The retrieve response contains references to images (the `image_path` field on each contributing chunk), not the image bytes. To display an image in your application:
+The generated index stores `image_path` references to images in the asset store. The retrieve response schema doesn't define dedicated fields for the individual asset-store image paths or image bytes sent to the model. Optional `sourceData` is structured reference data, and `image_path` isn't required in it.
+
+To display an indexed image in your application:
+
+1. Assign your application's identity the **Storage Blob Data Reader** role at the asset storage-account scope.
+
+1. Assign your application's identity the **Search Index Data Reader** role so it can query the generated index.
+
+1. Obtain an authorized `image_path` from the generated index through an application-controlled query or service endpoint.
 
-1. Assign your application's identity the **Storage Blob Data Reader** role on the asset store container.
+1. Validate that the reference resolves to the expected storage account and asset container. Reject untrusted paths before the blob lookup.
 
-1. Read the `image_path` value from the retrieve response and fetch the blob from Azure Storage using that identity.
+1. Fetch the resulting blob name from the asset container by using your application's identity.
 
 This separation lets you control who can view source images independently of who can call the retrieve API.
 
@@ -128,54 +136,56 @@ A minimal blob knowledge source with image serving enabled looks like this:
 ```http
 PUT https://{service-name}.search.windows.net/knowledgesources/my-blob-ks?api-version=2026-05-01-preview
 Content-Type: application/json
-api-key: {admin-api-key}
+Authorization: Bearer {{token}}
 
 {
   "name": "my-blob-ks",
   "kind": "azureBlob",
   "azureBlobParameters": {
-    "connectionString": "{blob-connection-string}",
-    "containerName": "source-documents"
-  },
-  "ingestionParameters": {
-    "assetStore": {
-      "connectionString": "{blob-connection-string}",
-      "containerName": "image-assets"
-    },
-    "chatCompletionModel": {
-      "kind": "azureOpenAI",
-      "azureOpenAIParameters": {
-        "resourceUri": "https://{aoai-resource}.openai.azure.com",
-        "deploymentId": "gpt-4o",
-        "modelName": "gpt-4o"
-      }
-    },
-    "embeddingModel": {
-      "kind": "azureOpenAI",
-      "azureOpenAIParameters": {
-        "resourceUri": "https://{aoai-resource}.openai.azure.com",
-        "deploymentId": "text-embedding-3-large",
-        "modelName": "text-embedding-3-large"
+    "connectionString": "ResourceId=<storage-resource-id>",
+    "containerName": "source-documents",
+    "ingestionParameters": {
+      "assetStore": {
+        "connectionString": "ResourceId=<storage-resource-id>",
+        "containerName": "image-assets"
+      },
+      "chatCompletionModel": {
+        "kind": "azureOpenAI",
+        "azureOpenAIParameters": {
+          "resourceUri": "https://{foundry-resource}.services.ai.azure.com",
+          "deploymentId": "gpt-4o",
+          "modelName": "gpt-4o"
+        }
+      },
+      "embeddingModel": {
+        "kind": "azureOpenAI",
+        "azureOpenAIParameters": {
+          "resourceUri": "https://{foundry-resource}.services.ai.azure.com",
+          "deploymentId": "text-embedding-3-large",
+          "modelName": "text-embedding-3-large"
+        }
+      },
+      "contentExtractionMode": "standard",
+      "aiServices": {
+        "uri": "https://{foundry-resource}.services.ai.azure.com"
       }
-    },
-    "contentExtractionMode": "standard",
-    "aiServices": {
-      "uri": "https://{foundry-resource}.services.ai.azure.com"
     }
   }
 }
 ```
 
 > [!NOTE]
-> The Azure Storage account that hosts the asset store needs to remain available and accessible to the search service for the lifetime of the knowledge base. If you change network rules, rotate keys, swap identities, or move the storage account in a way that prevents the search service from reading the asset store, image serving stops returning images. The retrieve API doesn't surface this as a hard error: it reports the drop in `imagesDropped` in activity, and answer synthesis proceeds with text only. Plan and test any storage account changes carefully.
+> + Replace `<storage-resource-id>` with the resource ID of the Azure Storage account. The `ResourceId=<storage-resource-id>` connection format tells the search service to use its managed identity for both containers.
+>
+> + The Azure Storage account that hosts the asset store needs to remain available and accessible to the search service for the lifetime of the knowledge base. If you change network rules, rotate keys, swap identities, or move the storage account in a way that prevents the search service from reading the asset store, image serving can't supply those images to the model. Compare `imagesRetrieved` with `imagesSentToModel` in retrieval activity and plan and test storage account changes carefully.
 
 ### Configuration outcomes
 
 The combination of `assetStore`, `disableImageVerbalization`, and `chatCompletionModel` determines what the indexer stores and what the model sees at query time:
 
-+ **Asset store + verbalization (default):** `assetStore` set, `disableImageVerbalization` left as `false`, `chatCompletionModel` set. The indexer persists images to the asset store and stores text descriptions in the index. `verbalizationUsed` is `true` at query time.
++ **Asset store + verbalization (default):** `assetStore` set, `disableImageVerbalization` left as `false`, `chatCompletionModel` set. The indexer persists images to the asset store and stores text descriptions in the index. Retrieval activity can report `verbalizationUsed` as `true`.
 
-+ **Asset store only:** `assetStore` set, `disableImageVerbalization` set to `true`, `chatCompletionModel` not required. The indexer persists images to the asset store but doesn't generate text descriptions. `verbalizationUsed` is `false`.
++ **Asset store only:** `assetStore` set, `disableImageVerbalization` set to `true`, `chatCompletionModel` not required. The indexer persists images to the asset store but doesn't generate text descriptions. Retrieval activity can report `verbalizationUsed` as `false`.
 
 + **No asset store, model set:** `assetStore` not set, `chatCompletionModel` set. Text descriptions only, no image artifacts. Image serving doesn't apply.
 
@@ -187,7 +197,7 @@ Wait for ingestion to complete before continuing:
 
 + Check indexer status in the [Azure portal](https://portal.azure.com) or use [Get Indexer Status](/rest/api/searchservice/indexers/get-status) (REST API).
 
-+ Verify that indexed chunks have a populated `image_path` field. Empty `image_path` values usually mean the source documents don't contain extractable images, the asset store isn't configured, or the indexer hasn't finished.
++ Check whether indexed chunks have a populated `image_path` field. If `image_path` is empty, check the indexer status, the knowledge source asset-store configuration, the source document contents, and the asset container contents.
 
 + Inspect the asset store container. You should see image blobs that the indexer wrote during ingestion.
 
@@ -197,12 +207,12 @@ Set `enableImageServing` to `true` on the knowledge source reference inside the
 
 The knowledge base definition also specifies the LLM used for **answer synthesis at query time**. This setting is independent of any `chatCompletionModel` that you set on the knowledge source's `ingestionParameters`, which drives image verbalization during indexing.
 
-If your knowledge base references multiple knowledge sources, set `enableImageServing` only on supported file-based indexed kinds that have `assetStore` configured. Unsupported kinds (such as search index, remote SharePoint, or web) still contribute text grounding but don't return images.
+If your knowledge base references multiple knowledge sources, set `enableImageServing` only on supported file-based indexed kinds that have `assetStore` configured. Unsupported kinds (such as search index, remote SharePoint, or web) still contribute text grounding but don't supply document-embedded images to downstream answer synthesis.
 
 ```http
 PUT https://{service-name}.search.windows.net/knowledgebases/my-kb?api-version=2026-05-01-preview
 Content-Type: application/json
-api-key: {admin-api-key}
+Authorization: Bearer {{token}}
 
 {
   "name": "my-kb",
@@ -213,14 +223,16 @@ api-key: {admin-api-key}
     }
   ],
   "outputMode": "answerSynthesis",
-  "chatCompletionModel": {
-    "kind": "azureOpenAI",
-    "azureOpenAIParameters": {
-      "resourceUri": "https://{aoai-resource}.openai.azure.com",
-      "deploymentId": "gpt-4o",
-      "modelName": "gpt-4o"
+  "models": [
+    {
+      "kind": "azureOpenAI",
+      "azureOpenAIParameters": {
+        "resourceUri": "https://{foundry-resource}.services.ai.azure.com",
+        "deploymentId": "gpt-4o",
+        "modelName": "gpt-4o"
+      }
     }
-  }
+  ]
 }
 ```
 
@@ -235,11 +247,12 @@ Call the [retrieve action](agentic-retrieval-how-to-retrieve.md) against the kno
 ```http
 POST https://{service-name}.search.windows.net/knowledgebases/my-kb/retrieve?api-version=2026-05-01-preview
 Content-Type: application/json
-api-key: {admin-api-key}
+Authorization: Bearer {{token}}
 
 {
   "retrievalReasoningEffort": { "kind": "medium" },
   "outputMode": "answerSynthesis",
+  "includeActivity": true,
   "messages": [
     {
       "role": "user",
@@ -263,19 +276,15 @@ api-key: {admin-api-key}
 
 ### What happens at retrieval time
 
-For chunks that have an `image_path`, the search service downloads the corresponding image from the asset store, base64-encodes it, and passes it as multimodal content to the LLM that produces the synthesized answer. The base64 image bytes are used only for that model call; they aren't returned to your application. Image download failures are non-fatal: successful images are forwarded to the model, and failures are silently counted in `imagesDropped`. For the exact response shape, see the reference documentation for [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (REST API).
+For image references associated with matching content, the search service downloads the corresponding images from the asset store, base64-encodes them, and passes them as multimodal content to the downstream answer-synthesis model. Inspect aggregate image-serving statistics in `activity.imageServing`. For the exact response shape, see the reference documentation for [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (REST API).
 
 ### Verify retrieve behavior
 
-A successful retrieve response with image serving enabled has these signals:
-
-+ The `activity` array contains an `imageServing` block for each knowledge source that returned images.
-
-+ `imagesSentToModel` is greater than `0` for queries whose grounding includes image-bearing chunks.
+A retrieve response can provide these image-serving signals:
 
-+ `imagesDropped` is `0` or close to it. Persistent drops usually point to RBAC or asset store availability issues. For more information, see [Troubleshooting](#troubleshooting).
++ When `includeActivity` is `true`, the `activity` array reports `imageServing` activity for a knowledge source when the service records image-serving operations.
 
-+ The synthesized answer references content that only appears in an image, such as a diagram or a scanned form.
++ An `imagesSentToModel` value greater than `0` means the service reports that it supplied images to the downstream answer-synthesis model.
 
 ### Precedence rules
 
@@ -287,7 +296,7 @@ When both the knowledge base definition and the retrieve request specify `enable
 
 The following table summarizes the nine combinations.
 
-| Knowledge base definition (`enableImageServing`) | Retrieve request (`enableImageServing`) | Images served? |
+| Knowledge base definition (`enableImageServing`) | Retrieve request (`enableImageServing`) | Image serving enabled? |
 |---|---|---|
 | `true` | `true` | Yes |
 | `true` | `false` | No |
@@ -301,7 +310,7 @@ The following table summarizes the nine combinations.
 
 ## Inspect image serving statistics
 
-When image serving runs, the retrieve response includes an `imageServing` section for each knowledge source inside the `activity` array. Use this section to verify whether images were sent to the model and to diagnose dropped images.
+When image serving runs, the retrieve response includes an `imageServing` section for each knowledge source inside the `activity` array. Use this section to compare the images retrieved from the asset store with the images sent to the model.
 
 ```json
 "activity": [
@@ -312,21 +321,25 @@ When image serving runs, the retrieve response includes an `imageServing` sectio
       "verbalizationUsed": true,
       "imagesRetrieved": 5,
       "imagesSentToModel": 4,
-      "imagesDropped": 1
+      "totalImageSizeBytes": 248361
     }
   }
 ]
 ```
 
 The fields report:
 
-+ `verbalizationUsed`: Whether the indexing pipeline generated text descriptions for images. This value is `true` when, at indexing time, both `disableImageVerbalization` was `false` (the default) **and** `chatCompletionModel` was set on the knowledge source. It reflects the indexing-time configuration of the knowledge source, not a retrieval-time decision.
++ `verbalizationUsed`: The service-reported image verbalization statistic for the retrieval activity.
+
++ `imagesRetrieved`: The number of images retrieved from the asset store.
+
++ `imagesSentToModel`: The number of images sent to the downstream model.
 
-+ `imagesRetrieved`: The number of images found across the chunks that matched this knowledge source for the current request.
++ `totalImageSizeBytes`: The total size, in bytes, of the images sent to the model.
 
-+ `imagesSentToModel`: The number of images that were successfully downloaded and forwarded to the LLM.
+If `imagesRetrieved` is greater than `imagesSentToModel`, not every retrieved image was sent to the model.
 
-+ `imagesDropped`: The number of images that failed to download or were unavailable. Image serving treats drops as non-fatal: answer synthesis proceeds with the remaining images and text.
+Inspect `verbalizationUsed` and `imagesSentToModel` independently. A response can report both `verbalizationUsed` as `true` and one or more images sent to the model.
 
 <!--
 ## Portal experience
@@ -336,30 +349,38 @@ Portal support for enabling and managing image serving is planned for a future u
 
 ## Test image serving end to end
 
-To test the full setup against multiple agentic retrieval configurations (image serving enabled and disabled, different output modes, runtime overrides), see the [image serving testing samples](https://aka.ms/agentic-retrieval-image-serving-testing). The samples include an end-to-end walkthrough that creates the knowledge source, knowledge base, and retrieve requests so you can compare answers with and without image serving.
+Use one of the following samples to test the full setup:
+
++ [C# image-serving sample](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/image-serving-example)
++ [Python image-serving sample](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/image-serving-example)
+
+The samples create a blob knowledge source and knowledge base, compare retrieve requests with image serving disabled and enabled, and inspect image-serving statistics. They also use an independent wildcard index query to select an `image_path` and download that asset. The samples select one semicolon-delimited reference, remove a projection prefix such as `11.7:` from a relative path, or URL-decode an absolute path and remove its leading asset-container segment. These transformations are sample behavior, not guarantees of the retrieve API. The selected asset isn't evidence that the same image contributed to a particular retrieve response.
 
 A typical A/B comparison checklist:
 
 + Pick a question that can only be answered from a diagram, chart, or scanned image.
 
 + Run the retrieve request with `enableImageServing: false` and capture the answer.
 
-+ Run the same retrieve request with `enableImageServing: true` and compare answer completeness, grounding to image content, and latency.
++ Run the same retrieve request with `enableImageServing: true` and compare the answers, latency, and reported activity.
+
++ Treat answer differences as observational A/B signals, not proof that images caused the differences. An `imagesSentToModel` value greater than `0` means the service reports that it supplied images to the model.
 
-+ Verify the `imageServing` activity reports the expected number of images sent to the model.
+## Clean up resources
+
+Delete the knowledge base before you delete its knowledge source. Deleting these Azure AI Search resources doesn't delete source documents or projected image blobs in Azure Storage. Delete those blobs separately only when no retained ingestion or retrieval pipeline still needs them.
 
 ## Troubleshooting
 
-Use the `imageServing` activity block from [Inspect image serving statistics](#inspect-image-serving-statistics) as your first diagnostic. The following table maps common symptoms to likely causes and fixes.
+Use the `imageServing` activity block from [Inspect image serving statistics](#inspect-image-serving-statistics) as your first diagnostic. The following table lists checks for common symptoms without assuming a single cause.
 
-| Symptom | Likely cause | What to try |
-|---|---|---|
-| `imagesDropped` is high and `imagesSentToModel` is low | The search service can't read from the asset store. | Verify the search service managed identity has **Storage Blob Data Contributor** on the asset store container. Check storage account network rules and firewall settings. |
-| `imagesRetrieved` is `0` for image-rich documents | `image_path` isn't populated in the index, or no matching chunks contained images. | Re-run the indexer and verify `image_path` is populated. Verify that the source documents contain extractable images (PDFs with embedded raster images, or supported image files). |
-| Retrieve response has no `imageServing` block | `enableImageServing` is `false` (the default) or `outputMode` isn't `answerSynthesis`. | Set `enableImageServing` to `true` on the knowledge base or per request, and use `outputMode: "answerSynthesis"`. |
-| `verbalizationUsed` is `false` but you expected `true` | At indexing time, `disableImageVerbalization` was `true` or `chatCompletionModel` wasn't set on the knowledge source. | Update the knowledge source `ingestionParameters` and re-run ingestion. |
-| Answer synthesis fails or times out after you enable image serving | Multimodal token overhead exceeds the model context window, or the LLM deployment can't be reached. | Lower [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md), tighten retrieval results, or use a model deployment with higher token limits. |
-| Your application can't render images from `image_path` | The application identity doesn't have **Storage Blob Data Reader** on the asset store. | Assign **Storage Blob Data Reader** to your application's identity at the storage account or container scope. |
+| Symptom | Checks |
+|---|---|
+| `imagesRetrieved` is `0` for image-rich documents | Check indexer status and warnings, populated `image_path` values in matching indexed chunks, and image blobs in the asset container. Confirm that the source documents contain extractable images and that the search service identity has **Storage Blob Data Contributor** at the storage-account scope. |
+| Retrieve response has no `imageServing` block | Confirm that the request sets `includeActivity` to `true`. Check the effective `enableImageServing` value after applying request, knowledge base, and default precedence. Confirm that `outputMode` is `answerSynthesis`, and inspect source activity errors and warnings. |
+| `verbalizationUsed` differs from what you expect | Check `disableImageVerbalization`, `chatCompletionModel`, and the most recent indexer status. Inspect `verbalizationUsed` independently from `imagesSentToModel`. A response can report verbalization and images sent together. |
+| Answer synthesis fails or times out after you enable image serving | Compare representative requests with image serving enabled and disabled. Inspect activity errors and warnings, the answer-synthesis model deployment status, search service identity permissions for the model and storage account, and asset-store availability. |
+| Your application can't render an independently queried `image_path` | Confirm that the independent index query returns a usable `image_path`, the referenced blob exists, and the application can access the blob independently of retrieve. Check that the application identity has **Search Index Data Reader** for the index query and **Storage Blob Data Reader** at the asset storage-account scope. |
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像サービングに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける画像サービングの使用方法に関する文書の大幅な更新を反映しています。主に、画像サービングの設定やそれに関連する権限、制限についての情報が追加および整理されています。

新たに追加されたコンテンツでは、Blob Knowledge Sourceに対する要件や制限が詳しく説明され、`ingestionPermissionOptions`が構成されていないことが明記されています。また、Microsoft Foundryリソースの設定、APIの呼び出しに必要な権限、画像の取り扱い方法についての詳細が紹介されています。特に、画像サービングが`ingestionPermissionOptions`の指定時にサポートされていないことが強調されています。

ドキュメントは、画像の抽出やサービングの実行フローを詳述しており、インデックス時に画像が資産ストアに保存され、取得時にそれがLLMに送信される流れを説明しています。また、設定後の確認方法やエラーハンドリングに関するセクションも充実しており、ユーザーは問題解決のための具体的なガイドラインを得ることができます。

これにより、ユーザーはAzure AI Searchで画像を効果的に扱うための手順や注意点をより理解しやすくなり、画像サービング機能の利用がスムーズに行えるようになります。

## articles/search/agentic-retrieval-how-to-retrieve.md{#item-d739cf}

<details>
<summary>Diff</summary>
````diff
@@ -346,11 +346,11 @@ Authorization: Bearer {{accessToken}}
 
 :::zone-end
 
-### Include images in retrieve responses (preview)
+### Supply images to answer synthesis (preview)
 
-For [blob](agentic-knowledge-source-how-to-blob.md), [indexed OneLake](agentic-knowledge-source-how-to-onelake.md), and [indexed SharePoint](agentic-knowledge-source-how-to-sharepoint-indexed.md) knowledge sources configured with an asset store, you can return document-embedded images alongside text and inject them into the answer synthesis prompt. Set `enableImageServing` on the matching entry in `knowledgeSourceParams` to override the default that's set on the knowledge base definition.
+For [blob](agentic-knowledge-source-how-to-blob.md), [indexed OneLake](agentic-knowledge-source-how-to-onelake.md), and [indexed SharePoint](agentic-knowledge-source-how-to-sharepoint-indexed.md) knowledge sources that you configure with an asset store, you can supply document-embedded images to the downstream answer-synthesis model alongside text. Set `enableImageServing` on the matching entry in `knowledgeSourceParams` to override the default that's set on the knowledge base definition. The retrieve response doesn't include dedicated fields for the individual image paths or image bytes supplied to the model.
 
-Image serving runs only when `outputMode` is `answerSynthesis` and requires the 2026-05-01-preview REST API or an equivalent Azure SDK preview package. For setup steps, the precedence table, and how to inspect image serving statistics, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
+Image serving runs only when `outputMode` is `answerSynthesis` and isn't supported for knowledge sources that configure `ingestionPermissionOptions`. For setup steps, the precedence table, and how to inspect image serving statistics, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
 
 ### Search index behavior
 
@@ -781,7 +781,7 @@ The output includes the following components.
 | `agenticReasoning` | This section reports on token consumption for agentic reasoning during retrieval, which depends on the specified [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). |
 | `modelAnswerSynthesis` | For knowledge bases that use [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md), this section reports on the token count for formulating the answer, and the token count of the answer output. Includes a `modelName` field with the public model name (not the deployment name) of the model that ran the activity. |
 | `modelWebSummarization` | For knowledge bases that use web summarization, this section reports on token consumption for summarizing web results. Includes a `modelName` field with the public model name (not the deployment name) of the model that ran the activity. |
-| `imageServing` | For knowledge sources that have [image serving](agentic-retrieval-how-to-image-serving.md) enabled, this section reports `imagesRetrieved`, `imagesSentToModel`, `totalImageSizeBytes`, and whether indexing-time `verbalizationUsed` was on. To find the number of dropped images, subtract `imagesSentToModel` from `imagesRetrieved`. |
+| `imageServing` | For knowledge sources that have [image serving](agentic-retrieval-how-to-image-serving.md) enabled, this section reports the four fields `verbalizationUsed`, `imagesRetrieved`, `imagesSentToModel`, and `totalImageSizeBytes`. Inspect `verbalizationUsed` and `imagesSentToModel` independently. A response can report `verbalizationUsed` as `true` and one or more images sent to the downstream model. If `imagesRetrieved` is greater than `imagesSentToModel`, not every image retrieved from the asset store was sent to the model. |
 
 # [2026-04-01](#tab/2026-04-01)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "取得応答における画像サービングの表現変更"
}
```

### Explanation
この変更は、Azure AI Searchの取得機能に関する記事の一部を更新し、取得応答における画像サービングの説明内容を明確にすることを目的としています。具体的には、画像サービングの機能の名称が「画像を取得応答に含める」から「回答合成に画像を提供する」に変更され、その後の説明も修正されています。

新しい説明では、事前に設定された知識ソースパラメータ内で`enableImageServing`を使用することで、テキストと共にドキュメントに埋め込まれた画像を下流の回答合成モデルに供給することができることが強調されています。また、応答には個々の画像パスや画像バイトを示す専用のフィールドが含まれないことも注記されています。

さらに、画像サービングが特定の条件下でのみ機能することを明示し、`ingestionPermissionOptions`が構成された知識ソースでは画像サービングがサポートされないことが強調されています。この変更により、ユーザーは画像サービングの設定方法や利用可能な機能に関する理解を深めることができます。

## articles/search/cognitive-search-common-errors-warnings.md{#item-a5c854}

<details>
<summary>Diff</summary>
````diff
@@ -238,7 +238,7 @@ An 'Expected IndexAction metadata' error means when the indexer attempted to rea
 
 ## `Warning: Skill input was invalid`
 
-An input to the skill was missing, it has the wrong type, or otherwise, invalid. You might see the following information:
+An input to the skill was missing, had the wrong type, or was otherwise invalid. You might see the following information:
 
 + `Could not execute skill`
 
@@ -405,7 +405,7 @@ Collections with [Lazy](/azure/cosmos-db/index-policy#indexing-mode) indexing po
 
 ## `Warning: The document contains very long words (longer than 64 characters). These words may result in truncated and/or unreliable model predictions.`
 
-This warning is passed from the Language service of Foundry Tools. In some cases, it's safe to ignore this warning, for example if the long string is just a long URL. Be aware that when a word is longer than 64 characters, it's 'truncated to 64 characters which can affect model predictions.
+This warning is passed from the Language service of Foundry Tools. In some cases, it's safe to ignore this warning, for example if the long string is just a long URL. Be aware that when a word is longer than 64 characters, it's truncated to 64 characters, which can affect model predictions.
 
 ## `Error: Cannot write more bytes to the buffer than the configured maximum buffer size`
 
@@ -437,7 +437,7 @@ This error occurs when the Azure AI Search indexer cannot authenticate using the
 | Possible Cause | Details/Example | Resolution |
 |---|---|---|
 | Expired or rotated key | A connection string contains an outdated key that no longer works. | Go to the resource that is being contacted (for example, Azure Storage or Azure SQL) and copy the latest access keys if using key-based authentication, then update the data source or connection string accordingly. |
-| Managed identity not enabled or access not granted | The AI Search service [managed identity](search-how-to-managed-identities.md) is enabled but lacks the required access roles. | - Enable system or user-assigned [managed identity](search-how-to-managed-identities.md) on the search Service.<br>- Assign appropriate role(s) to the identity (for example, `Storage Blob Data Reader` for blob containers). Each [data source](search-data-sources-gallery.md) has its own permission requirements. |
+| Managed identity not enabled or access not granted | The AI Search service [managed identity](search-how-to-managed-identities.md) is enabled but lacks the required access roles. | - Enable system or user-assigned [managed identity](search-how-to-managed-identities.md) on the search service.<br>- Assign appropriate roles to the identity at the resource scope required by the data source. For example, assign `Storage Blob Data Reader` at the storage-account scope for an Azure Blob data source. Each [data source](search-data-sources-gallery.md) has its own permission requirements. |
 | Network/firewall blocks identity access | The resource contacted is configured to restrict network access. | Configure [network settings](search-indexer-howto-access-ip-restricted.md) to allow Azure AI Search access. |
 | Key authorization has been disabled | Shared key access removed on the source, but the Search service data source configuration still uses key-based authentication. | Use [managed identity](search-how-to-managed-identities.md) authentication and ensure role-based permissions are in place. From an Azure Storage perspective, this means that [shared key authorization functionality is blocked](/azure/storage/common/shared-key-authorization-prevent), either from the storage account itself, or enforced through enterprise-level Azure Policies. |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "一般的なエラーと警告の文書更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける一般的なエラーと警告の文書に小規模な修正を加えることを目的としています。具体的には、警告やエラーメッセージの説明がより明確になるように調整されています。

1. **警告メッセージの文修正**:
   - 「入力が欠落しているか、誤った型である」という説明が、「入力が欠落している、誤った型である、またはその他無効である」に変更され、流れがよりスムーズになっています。
   - 長い単語に関する警告の説明には、トランケーションの影響についての文が修正されて、より明確にされました。

2. **エラーメッセージの詳細強化**:
   - 管理対象IDが有効になっているがアクセス権が付与されていない場合の説明が詳細になりました。具体的には、適切なロールをリソーススコープで割り当てる必要がある点が強調され、どのリソースに対してどのロールを割り当てるべきかが明示されました。

これらの修正により、ユーザーは警告やエラーの原因、解決方法をより理解しやすくなり、問題解決の手助けとなることが期待されます。

## articles/search/cognitive-search-skill-document-extraction.md{#item-072b72}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.custom:
   - ignite-2023
   - doc-kit-assisted
 ms.topic: reference
-ms.date: 08/08/2026
+ms.date: 08/18/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ---
@@ -18,7 +18,7 @@ ai-usage: ai-assisted
 
 The **Document Extraction** skill extracts content from a file in the [enrichment pipeline](cognitive-search-concept-intro.md). By default, content extraction or retrieval is built into the enrichment pipeline. However, by using the Document Extraction skill, you can control how parameters are set, and how extracted content is named in the enrichment tree.
 
-For [vector](vector-search-overview.md) and [multimodal search](multimodal-search-overview.md), Document Extraction combined with the [Text Split skill](cognitive-search-skill-textsplit.md) is more affordable than other [data chunking approaches](vector-search-how-to-chunk-documents.md). The [Multimodal tutorial](tutorial-multimodal.md) demonstrates this scenario.
+For [vector](vector-search-overview.md) and [multimodal search](multimodal-search-overview.md), combine Document Extraction with the [Text Split skill](cognitive-search-skill-textsplit.md) to implement a configurable [data chunking approach](vector-search-how-to-chunk-documents.md). The [Multimodal tutorial](tutorial-multimodal.md) demonstrates this scenario.
 
 > [!NOTE]
 > This skill isn't bound to Foundry Tools and has no Foundry Tools key requirement.
@@ -40,16 +40,16 @@ The DocumentExtractionSkill can extract text from the following document formats
 
 Parameters are case sensitive.
 
-| Inputs | Allowed Values | Description |
+| Inputs | Allowed values | Description |
 |-----------------|----------------|-------------|
-| `parsingMode`   | `default` </br>`text` </br>`json`  | Set to `default` for document extraction from files that aren't pure text or json. For source files that contain mark up (such as PDF, HTML, RTF, and Microsoft Office files), use the default to extract just the text, minus any markup language or tags. If `parsingMode` isn't defined explicitly, it will be set to `default`. </p>Set to `text` if source files are TXT. This parsing mode improves performance on plain text files. If files include markup, this mode will preserve the tags in the final output. </p>Set to `json` to extract structured content from json files.  |
-| `dataToExtract` | `contentAndMetadata` </br>`allMetadata` | Set to `contentAndMetadata` to extract all metadata and textual content from each file. If `dataToExtract` isn't defined explicitly, it will be set to `contentAndMetadata`. </p>Set to `allMetadata` to extract only the [metadata properties for the content type](search-blob-metadata-properties.md) (for example, metadata unique to just .png files).  |
+| `parsingMode` | `default`<br>`text`<br>`json` | Set to `default` for document extraction from files that aren't pure text or JSON. For source files that contain markup, such as PDF, HTML, RTF, and Microsoft Office files, use the default to extract text without markup language or tags. If `parsingMode` isn't defined explicitly, the value is `default`.<br><br>Set to `text` if source files are TXT. This parsing mode improves performance on plain-text files. If files include markup, this mode preserves the tags in the final output.<br><br>Set to `json` to extract structured content from JSON files. |
+| `dataToExtract` | `contentAndMetadata`<br>`allMetadata` | Set to `contentAndMetadata` to extract all metadata and textual content from each file. If `dataToExtract` isn't defined explicitly, the value is `contentAndMetadata`.<br><br>Set to `allMetadata` to extract only the [metadata properties for the content type](search-blob-metadata-properties.md), such as metadata unique to PNG files. |
 | `configuration` | See below. | A dictionary of optional parameters that adjust how the document extraction is performed. See the below table for descriptions of supported configuration properties. |
 
-| Configuration Parameter	| Allowed Values | Description |
+| Configuration parameter | Allowed values | Description |
 |-------------------------|----------------|-------------|
-| `imageAction`           | `none` </br>`generateNormalizedImages` </br>`generateNormalizedImagePerPage` | Set to `none` to ignore embedded images or image files in the data set, or if the source data doesn't include image files. This is the default. </p>For [OCR and image analysis](cognitive-search-concept-image-scenarios.md), set to `generateNormalizedImages` to have the skill create an array of normalized images as part of [document cracking](search-indexer-overview.md#document-cracking). This action requires that `parsingMode` is set to `default` and `dataToExtract` is set to `contentAndMetadata`. A normalized image refers to extra processing resulting in uniform image output, sized and rotated to promote consistent rendering when you include images in visual search results (for example, same-size photographs in a graph control as seen in the [JFK demo](https://github.com/Microsoft/AzureSearch_JFK_Files)). This information is generated for each image when you use this option. </p>If you set to `generateNormalizedImagePerPage`, PDF files are treated differently in that instead of extracting embedded images, each page is rendered as an image and normalized accordingly.  Non-PDF file types are treated the same as if `generateNormalizedImages` was set.
-| `normalizedImageMaxWidth` | Any integer between 50-10000 | The maximum width (in pixels) for normalized images generated. The default is 2000. | 
+| `imageAction` | `none`<br>`generateNormalizedImages`<br>`generateNormalizedImagePerPage` | Set to `none` to ignore embedded images or image files in the data set, or if the source data doesn't include image files. This value is the default.<br><br>For [OCR and image analysis](cognitive-search-concept-image-scenarios.md), set to `generateNormalizedImages` to have the skill create an array of normalized images as part of [document cracking](search-indexer-overview.md#stage-1-document-cracking). This action requires `parsingMode` set to `default` and `dataToExtract` set to `contentAndMetadata`. A normalized image has uniform output that is sized and rotated to promote consistent rendering in visual search results. The skill generates this information for each image.<br><br>If you set `imageAction` to `generateNormalizedImagePerPage`, each PDF page is rendered as an image and normalized instead of extracting embedded images. Non-PDF file types are treated the same as if `generateNormalizedImages` was set. |
+| `normalizedImageMaxWidth` | Any integer between 50-10000 | The maximum width (in pixels) for normalized images generated. The default is 2000. |
 | `normalizedImageMaxHeight` | Any integer between 50-10000 | The maximum height (in pixels) for normalized images generated. The default is 2000. |
 
 > [!NOTE]
@@ -92,10 +92,10 @@ The file reference object can be generated one of three ways:
 
 ## Skill outputs
 
-| Output name	 | Description |
+| Output name | Description |
 |--------------|-------------|
 | `content` | The textual content of the document. |
-| `normalized_images`	| When the `imageAction` is set to a value other than `none`, the new *normalized_images* field contains an array of images. See [Extract text and information from images](cognitive-search-concept-image-scenarios.md) for more details on the output format. |
+| `normalized_images` | When `imageAction` is set to a value other than `none`, the new *normalized_images* field contains an array of images. For more information about the output format, see [Extract text and information from images](cognitive-search-concept-image-scenarios.md). |
 
 ## Sample definition
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書抽出スキルの構成パラメータの明確化"
}
```

### Explanation
この変更は、Azureのコグニティブサーチにおける文書抽出スキルに関する文書を更新し、構成パラメータの説明を明確にすることを目的としています。

1. **日付の更新**:
   - `ms.date`フィールドの日付が変更され、最新情報に更新されました。

2. **文言の調整**:
   - 「Document Extraction skill extracts content from a file in the enrichment pipeline」の説明はそのままですが、文体や流れの改善を図るため、一部表現が調整されています。
   - データチャンク方式に関する説明が明確化され、「データチャンクアプローチを実装するために、Document ExtractionとText Splitスキルを組み合わせる」といった具体的なアプローチが強調されています。

3. **パラメータ説明の詳細化**:
   - `parsingMode`や`dataToExtract`に関する説明がより自然な文構造に改善され、ユーザーが理解しやすくなっています。
   - `imageAction`に関しても、処理の詳細が強調され、選択肢ごとの動作の具体的な説明が追加されました。

4. **タブ形式の変更**:
   - 表内の各項目のラベルが一貫した形式に整えられ、読みやすさが向上しています。

これらの修正によって、技術者は文書抽出スキルの利用方法や、それに関連するパラメータの設定方法をさらに理解しやすくなるでしょう。

## articles/search/includes/how-tos/knowledge-source-check.md{#item-e19bd3}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 04/28/2026
+ms.date: 08/19/2026
 zone_pivot_groups: search-csharp-python-rest
 ---
 
@@ -52,7 +52,7 @@ for ks in index_client.list_knowledge_sources():
 ```http
 ### List knowledge sources by name and type
 GET {{search-url}}/knowledgesources?api-version={{api-version}}&$select=name,kind
-api-key: {{api-key}}
+Authorization: Bearer {{token}}
 ```
 
 **Reference:** [Knowledge Sources - List](/rest/api/searchservice/knowledge-sources/list)
@@ -112,7 +112,7 @@ print(json.dumps(ks.as_dict(), indent = 2))
 ```http
 ### Get a knowledge source definition
 GET {{search-url}}/knowledgesources/{{knowledge-source-name}}?api-version={{api-version}}
-api-key: {{api-key}}
+Authorization: Bearer {{token}}
 ```
 
 **Reference:** [Knowledge Sources - Get](/rest/api/searchservice/knowledge-sources/get)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ソースチェックの認証方式を更新"
}
```

### Explanation
この変更は、Azure AI Searchの「知識ソースチェック」に関する文書のマイナーアップデートであり、認証方式の情報を最新の形式に変更しています。

1. **日付の更新**:
   - `ms.date`フィールドの日付が更新され、情報が最新になりました。

2. **認証方法の変更**:
   - 知識ソースをリストする際のAPIリクエストに含まれる認証方法が「api-key」から「Authorization: Bearer {{token}}」に変更されました。この変更により、API呼び出しのセキュリティが強化され、Bearerトークン方式を採用する形にシフトしています。

3. **一貫性の向上**:
   - 不要な情報を削除し、より清潔で読みやすいコードスニペットに改善されており、開発者がAPIを利用する際に直感的に理解できる形式になっています。

この更新により、利用者は最新の認証方法を反映した形でAPIを利用できるようになり、セキュリティ上のベストプラクティスに従って操作することが可能になります。

## articles/search/includes/how-tos/knowledge-source-delete.md{#item-4a16f9}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 04/28/2026
+ms.date: 08/19/2026
 zone_pivot_groups: search-csharp-python-rest
 ---
 
@@ -174,7 +174,7 @@ To delete a knowledge source:
       "outputMode": null,
       "knowledgeSources": [
         {
-          "name": "my-blob-ks",
+          "name": "my-blob-ks"
         }
       ],
       "models": [],
@@ -222,7 +222,7 @@ To delete a knowledge source:
     ```http
     ### Get knowledge bases
     GET {{search-url}}/knowledgebases?api-version={{api-version}}&$select=name
-    api-key: {{api-key}}
+    Authorization: Bearer {{token}}
     ```
 
    **Reference:** [Knowledge Bases - List](/rest/api/searchservice/knowledge-bases/list)
@@ -248,7 +248,7 @@ To delete a knowledge source:
     ```http
     ### Get a knowledge base definition
     GET {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version={{api-version}}
-    api-key: {{api-key}}
+    Authorization: Bearer {{token}}
     ```
 
    **Reference:** [Knowledge Bases - Get](/rest/api/searchservice/knowledge-bases/get)
@@ -264,7 +264,7 @@ To delete a knowledge source:
       "outputMode": null,
       "knowledgeSources": [
         {
-          "name": "my-blob-ks",
+          "name": "my-blob-ks"
         }
       ],
       "models": [],
@@ -280,7 +280,7 @@ To delete a knowledge source:
     ```http
     ### Delete a knowledge base
     DELETE {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version={{api-version}}
-    api-key: {{api-key}}
+    Authorization: Bearer {{token}}
     ```
 
    **Reference:** [Knowledge Bases - Delete](/rest/api/searchservice/knowledge-bases/delete)
@@ -290,7 +290,7 @@ To delete a knowledge source:
     ```http
     ### Delete a knowledge source
     DELETE {{search-url}}/knowledgesources/{{knowledge-source-name}}?api-version={{api-version}}
-    api-key: {{api-key}}
+    Authorization: Bearer {{token}}
     ```
 
    **Reference:** [Knowledge Sources - Delete](/rest/api/searchservice/knowledge-sources/delete)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ソース削除手順の認証方式を更新"
}
```

### Explanation
この変更は、Azure AI Searchの「知識ソース削除」に関する文書のマイナーアップデートであり、認証方法の情報を最新の形式に更新しています。

1. **日付の更新**:
   - `ms.date`フィールドの日付が更新され、情報が最新のものになっています。

2. **認証方式の変更**:
   - 知識ソースを削除する際に使用されるAPIリクエストでの認証方法が「api-key」から「Authorization: Bearer {{token}}」に変更されました。この更新により、API呼び出し時のセキュリティが向上しました。

3. **コードの整形**:
   - コードスニペット内で無駄な部分が削除され、よりクリーンな見た目になっています。具体的には、無駄な改行やスペースの調整が行われ、開発者が視覚的に把握しやすい形に整理されています。

この変更により、APIの利用者は最新の認証方法に基づいて操作を行うことができ、高いセキュリティ基準を維持しつつ、知識ソースを適切に削除できるようになります。

## articles/search/includes/how-tos/knowledge-source-status.md{#item-8d20e6}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 04/28/2026
+ms.date: 08/19/2026
 zone_pivot_groups: search-csharp-python-rest
 ---
 
@@ -51,7 +51,7 @@ print(json.dumps(status.as_dict(), indent=2))
 ```http
 ### Check knowledge source ingestion status
 GET {{search-url}}/knowledgesources/{{knowledge-source-name}}/status?api-version={{api-version}}
-api-key: {{api-key}}
+Authorization: Bearer {{token}}
 Content-Type: application/json 
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ソースの状態確認手順の認証方式を更新"
}
```

### Explanation
この変更は、Azure AI Searchに関する「知識ソースの状態確認」に関する文書のマイナーアップデートであり、認証方法の情報を最新の形式に更新しています。

1. **日付の更新**:
   - `ms.date`フィールドの日付が更新され、情報が最新のものになりました。

2. **認証方式の変更**:
   - 知識ソースのインジェスト状況を確認するためのAPIリクエストにおいて、認証方式が「api-key」から「Authorization: Bearer {{token}}」に変更されました。この変更により、セキュリティが強化され、Bearerトークンを利用した認証が標準的になります。

3. **コードの整形**:
   - コードスニペットが整形され、より簡潔で読みやすい形になっています。具体的には、不要な行や改行が削除され、開発者が容易に理解できるように反映されています。

この変更によって、APIの利用者は認証方法が最新化された形で、知識ソースの状態をより安全かつ効率的に確認できるようになります。

## articles/search/samples-dotnet.md{#item-12f3fa}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: .NET Samples
 description: Find Azure AI Search demo C# code samples that use the .NET client libraries.
-ms.date: 06/08/2026
+ms.date: 08/19/2026
 ms.service: azure-ai-search
 ms.topic: concept-article
 ms.custom:
@@ -50,6 +50,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. T
 | [quickstart-keyword-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-keyword-search/AzureSearchQuickstart) | [Quickstart: Full-text search](search-get-started-text.md) | Create, load, and query an index using sample data. |
 | [quickstart-semantic-ranking](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-ranking/) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Add semantic ranking to an index schema and run semantic queries. |
 | [quickstart-vector-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-vector-search) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
+| [image-serving-example](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/image-serving-example) | [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md) | Run managed ingestion and A/B retrieval and independently query and download an indexed image reference from Azure Blob Storage. |
 | [search-website](https://github.com/Azure-Samples/azure-search-static-web-app) | [Tutorial: Add search to web apps](tutorial-csharp-overview.md) | Build an end-to-end search app that uses the push API for bulk upload and a rich client for hosting the app and handling search requests. |
 | [tutorial-ai-enrichment](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/tutorial-ai-enrichment) | [Tutorial: AI-generated searchable content from Azure blobs](tutorial-skillset.md) | Create a skillset that iterates over Azure blobs to extract information and infer structure. |
 | [multiple-data-sources](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources) | [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md) | Merge content from two data sources into one index. |
@@ -65,7 +66,6 @@ A demo repo provides proof-of-concept source code for examples or scenarios show
 | Sample | Description |
 | --- | --- |
 | [covid19search](https://github.com/liamca/covid19search) | Source code repo for the Azure AI Search-based Covid-19 search app. |
-| [AzureSearch_JFK_Files](https://github.com/Microsoft/AzureSearch_JFK_Files) | Source code repo for the Azure AI Search-based JFK files solution. |
 
 ## Other samples
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": ".NET サンプルの更新と新しいサンプルの追加"
}
```

### Explanation
この変更は、Azure AI Searchの「.NET サンプル」に関する文書のマイナーアップデートであり、日付の更新と新しいサンプルの追加を行っています。

1. **日付の更新**:
   - `ms.date`フィールドの日付が、2026年6月8日から2026年8月19日に更新され、情報が新しくなっています。

2. **新しいサンプルの追加**:
   - 「image-serving-example」という新しいサンプルが追加されました。このサンプルは、Azure Blob Storageからの画像参照の管理されたインジェストとA/Bリトリーバルを実行し、インデックスされた画像を独立して照会およびダウンロードできる機能を示しています。

3. **不要なサンプルの削除**:
   - `AzureSearch_JFK_Files`に関するサンプルがリストから削除されました。この変更により、現在のサンプルリストがより関連性のある内容に整理されています。

これらの変更により、APIの利用者は最新の情報を基にサンプルコードを利用でき、特に新しい画像サービングのサンプルによって、より多様な機能を探索することができるようになります。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Python Samples
 description: Find Azure AI Search demo Python code samples that use the Azure SDK for Python.
-ms.date: 06/08/2026
+ms.date: 08/18/2026
 ms.service: azure-ai-search
 ms.topic: concept-article
 ms.custom:
@@ -39,6 +39,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. T
 | [Quickstart-Semantic-Ranking](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Ranking) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Add semantic ranking to an index schema and run semantic queries. |
 | [Quickstart-Vector-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Vector-Search) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
 | [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) | [Tutorial: Build an end-to-end agentic retrieval solution](agentic-retrieval-how-to-create-pipeline.md) | Unlike [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval), this sample incorporates Foundry Agent Service for request orchestration. |
+| [image-serving-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/image-serving-example) | [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md) | Use managed ingestion to extract images, serve them during answer synthesis, and independently query and download an indexed image reference from Azure Blob Storage. |
 
 ## Accelerators
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python サンプルの更新と新しいサンプルの追加"
}
```

### Explanation
この変更は、Azure AI Searchの「Python サンプル」に関する文書のマイナーアップデートであり、具体的には日付の更新と新しいサンプルの追加が含まれています。

1. **日付の更新**:
   - `ms.date`フィールドの日付が、2026年6月8日から2026年8月18日に更新され、文書が最新のものになっています。

2. **新しいサンプルの追加**:
   - 「image-serving-example」という新しいサンプルが追加されました。この新しいサンプルでは、管理されたインジェストを利用して画像を抽出し、答えの合成中に提供し、Azure Blob Storageからインデックスされた画像参照を照会およびダウンロードする機能が示されています。

3. **テキストの削除**:
   - 一部のサンプルの表記が整理され、不要な部分が削除されました。これにより、文書の簡潔さが向上しています。

これらの変更により、Pythonを使用してAzure AI Searchを扱う開発者が、最新の情報をもとにサンプルコードを利用できるようになります。特に新しい画像サービングのサンプルによって、さまざまな機能を探求する機会が提供されます。

## articles/search/search-document-level-access-overview.md{#item-4bb055}

<details>
<summary>Diff</summary>
````diff
@@ -35,10 +35,12 @@ Azure AI Search provides four primary approaches to enforce document-level permi
 | Approach | Description |
 |----------|-------------|
 | Security filters | String comparison. Your application passes in a user or group identity as a string, which populates a filter on a query, excluding any documents that don't match on the string. <br><br>Security filters are a technique for achieving document-level access control. This approach isn't bound to an API so you can use any version or package. |
-| POSIX-like ACL / RBAC scopes (preview) | The Microsoft Entra security principal behind the query token is compared to the permission metadata of documents returned in search results, excluding any documents that don't match on permissions. Access control lists (ACL) permissions apply to Azure Data Lake Storage (ADLS) Gen2 directories and files. Role-based access control (RBAC) scopes apply to ADLS Gen2 content and to Azure blobs. <br><br>Built-in support for identity-based access at the document level is in preview, available in REST APIs and preview Azure SDK packages that provide the feature. For evidence of feature support, check the [SDK version support details](#retrieve-acl-permissions-metadata-during-data-ingestion-process-preview). |
+| POSIX-like ACL / RBAC scopes (preview) | The Microsoft Entra security principal behind the query token is compared to the permission metadata of documents returned in search results, excluding any documents that don't match on permissions. Access control list (ACL) permissions apply to Azure Data Lake Storage (ADLS) Gen2 directories and files. Role-based access control (RBAC) scopes apply to ADLS Gen2 content and to Azure blobs. <br><br>Built-in support for identity-based access at the document level is in preview, available in REST APIs and preview Azure SDK packages that provide the feature. For evidence of feature support, check the [SDK version support details](#retrieve-acl-permissions-metadata-during-data-ingestion-process-preview). |
 | Microsoft Purview sensitivity labels (preview) | Indexer extracts sensitivity labels defined in Microsoft Purview from supported data sources (Azure Blob Storage, ADLS Gen2, SharePoint in Microsoft 365, OneLake). These labels are stored as metadata and evaluated at query time to enforce user access based on Microsoft Entra tokens and Purview policy assignments. Labels are also surfaced through [knowledge sources](agentic-knowledge-source-overview.md) and the [agentic retrieval response](agentic-retrieval-how-to-retrieve.md#inspect-sensitivity-label-metadata-in-the-response-preview), allowing AI agents and chat apps consuming a knowledge base to receive the same label-aware filtering. This approach aligns Azure AI Search authorization with your enterprise's Microsoft Information Protection model.|
 | SharePoint in Microsoft 365 ACLs (preview) | Azure AI Search indexers extract permission metadata from supported SharePoint content and use it for query-time access checks. For supported content, principals, group relationships, synchronization behavior, and permissions, see [Use a SharePoint indexer to ingest permission metadata](search-indexer-sharepoint-access-control-lists.md). |
 
+For indexed knowledge sources, `ingestionPermissionOptions` can't be combined with `assetStore`. Therefore, [image serving (preview)](agentic-retrieval-how-to-image-serving.md) isn't available when native document-level permission ingestion is enabled.
+
 ## Choose an approach
 
 Use the following criteria to identify the approach that best fits your data source, identity model, and compliance requirements.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントレベルアクセス制御の選択肢に関する更新"
}
```

### Explanation
この変更は、「検索ドキュメントレベルアクセス概要」文書のマイナーアップデートであり、特に新しい情報の追加と既存の情報の整理が行われています。

1. **新しい情報の追加**:
   - ドキュメントの最後に、インデックスされた知識ソースについての注意が追加されました。具体的には、`ingestionPermissionOptions`が`assetStore`と組み合わせることができないため、ネイティブなドキュメントレベルの権限インジェストが有効な場合、画像サービング（プレビュー機能）が利用できなくなることが明記されています。

2. **選択肢の明確化**:
   - 「選択肢を選ぶ」セクションが新たに追加され、データソース、アイデンティティモデル、およびコンプライアンス要件に最適なアプローチを特定するための基準が示されています。

3. **既存情報の整理**:
   - ドキュメント内のいくつかの説明が改善され、一貫性が強化されました。特に、POSIXのようなACL/RBACスコープに関する記述がクリアになり、情報の理解がしやすくなっています。

これらの変更により、文書が最新の情報を反映し、ユーザーがAzure AI Searchのドキュメントレベルのアクセス制御に関する異なるアプローチをより容易に理解し選択できるようになることが期待されます。

## articles/search/search-how-to-multiple-indexers-one-index.md{#item-5ccefd}

<details>
<summary>Diff</summary>
````diff
@@ -43,7 +43,7 @@ In this tutorial, you:
 
 - Your user account must have the **Search Service Contributor**, **Search Index Data Contributor**, and **Search Index Data Reader** roles on the search service. These roles authorize the management and query operations sent with the bearer token throughout this tutorial. For more information, see [Connect to Azure AI Search using roles](search-security-rbac.md). If a request includes both a bearer token and an API key, the API key takes precedence.
 
-- An [Azure Storage account](/azure/storage/common/storage-account-create) with a [blob container](/azure/storage/blobs/blob-containers-portal#create-a-container). Create `docx`, `json`, and `csv` folders in the container. Assign the **Storage Blob Data Reader** role on the storage account or container to the search service's managed identity. Your user account needs **Storage Blob Data Contributor** to upload the sample files.
+- An [Azure Storage account](/azure/storage/common/storage-account-create) with a [blob container](/azure/storage/blobs/blob-containers-portal#create-a-container). Create `docx`, `json`, and `csv` folders in the container. Assign the **Storage Blob Data Reader** role at the storage-account scope to the search service's managed identity. Your user account needs **Storage Blob Data Contributor** at the storage-account scope to upload the sample files.
 
 - A [Microsoft Foundry resource](/azure/foundry/tutorials/quickstart-create-foundry-resources) in a [region that supports Azure Content Understanding in Foundry Tools](/azure/ai-services/content-understanding/language-region-support). The search service can be in another supported region, but cross-region processing adds latency. The resource endpoint has the following format: `https://<foundry-resource-name>.services.ai.azure.com`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ストレージアカウント権限のスコープに関する明確化"
}
```

### Explanation
この変更は、「複数のインデクサーを単一のインデックスで使用する方法」の文書におけるマイナーアップデートであり、ストレージアカウントに関連する権限のスコープについての明確化が行われています。

1. **ストレージアカウントの権限スコープの明確化**:
   - ストレージアカウントにおける管理者の権限割り当てについて、`Storage Blob Data Reader`および`Storage Blob Data Contributor`の役割が具体的に「ストレージアカウントスコープ」で割り当てられる必要があることが記載されています。これにより、請求書やリソースに対する権限の範囲が明確になり、ユーザーが必要な権限を適切に設定する手助けとなります。

2. **その他の情報は変更なし**:
   - 変更された行は権限に関する部分のみであり、その他の情報や手順については影響を受けていません。これにより、ドキュメント全体の流れや内容に大きな変更はなく、特定の部分が洗練されただけになります。

この変更により、Azure AI Searchを使用するユーザーは、ストレージアカウントに対する正確な権限設定の方法を理解しやすくなり、所定の役割の適用が円滑に行えるようになります。これは、インデックス作成やデータのアップロードなどの操作において重要です。

## articles/search/search-indexer-access-control-lists-and-role-based-access.md{#item-67b42f}

<details>
<summary>Diff</summary>
````diff
@@ -53,7 +53,7 @@ This article explains how to configure an ADLS Gen2 indexer or ADLS Gen2 blob kn
 
   + [Custom Web API skill](cognitive-search-custom-skill-web-api.md)
 
-  + [Knowledge store](knowledge-store-concept-intro.md)
+  + [Knowledge store](knowledge-store-concept-intro.md), including the asset store required for [image serving (preview)](agentic-retrieval-how-to-image-serving.md) in agentic retrieval. Therefore, image serving isn't supported for knowledge sources that ingest ACLs or RBAC scopes.
 
   + [Indexer enrichment cache](enrichment-cache-how-to-configure.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジストアに関する情報の更新"
}
```

### Explanation
この変更は、「アクセス制御リストと役割ベースアクセス」についての文書におけるマイナーアップデートで、ナレッジストアに関する情報が最新の状況に合わせて調整されています。

1. **知識ストアの説明の追加**:
   - 変更により、ナレッジストアに、「画像サービング（プレビュー）」機能に必要なアセットストアが含まれていることが明記されました。これによって、ナレッジストアが役割ベースのアクセス制御（RBAC）やアクセス制御リスト（ACL）を取り込む場合、画像サービングがサポートされないことが明確に示されています。

2. **文書の一貫性向上**:
   - この変更は、ナレッジストアの機能と制限をより明確にし、ユーザーがどのようにこれらの要素を活用できるかをより理解しやすくするためのものです。特に、ユーザーが既存のナレッジストアを使う際にWorkflowsや制約を考慮しやすくなっています。

このアップデートにより、読者はナレッジストアの使用におけるさまざまな要素を把握し、適切に機能を利用していく助けになります。

## articles/search/search-indexer-sensitivity-labels.md{#item-2a7bfc}

<details>
<summary>Diff</summary>
````diff
@@ -23,7 +23,7 @@ ai-usage: ai-assisted
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This responsibility includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-Azure AI Search supports automatic extraction of [Microsoft Purview sensitivity labels](/purview/sensitivity-labels) at document-level during indexing, with label-based access control enforced at query time. Available in preview, this feature enables organizations to align search experiences with existing [information protection policies](/purview/create-sensitivity-labels) defined in Microsoft Purview.
+Azure AI Search supports automatic extraction of [Microsoft Purview sensitivity labels](/purview/sensitivity-labels) at document level during indexing, with label-based access control enforced at query time. Available in preview, this feature enables organizations to align search experiences with existing [information protection policies](/purview/create-sensitivity-labels) defined in Microsoft Purview.
 
 With sensitivity label indexing, Azure AI Search extracts and stores metadata that describes each document's sensitivity level. It also enforces label-based access control, ensuring that only authorized users can view or retrieve labeled content in search results.
 
@@ -65,7 +65,7 @@ This functionality is available for the following data sources:
 
   + [Custom Web API skill](cognitive-search-custom-skill-web-api.md)
 
-  + [Knowledge store](knowledge-store-concept-intro.md)
+  + [Knowledge store](knowledge-store-concept-intro.md), including the asset store required for [image serving (preview)](agentic-retrieval-how-to-image-serving.md) in agentic retrieval. Therefore, image serving isn't supported for knowledge sources that ingest sensitivity labels.
 
   + [Indexer enrichment cache](enrichment-cache-how-to-configure.md)
   
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "感度ラベルおよびナレッジストアに関する明確化"
}
```

### Explanation
この変更は、「インデクサー感度ラベル」に関する文書におけるマイナーアップデートで、感度ラベルの操作およびナレッジストアに関する情報が更新されています。

1. **感度ラベルに関する記述の明確化**:
   - Microsoft Purviewの感度ラベルがインデクシング中に文書レベルで自動的に抽出されること、そしてクエリ時にラベルベースのアクセス制御が施されることが強調されています。特に「文書レベル」という表現が修正され、より明確にその操作が示されるようになっています。

2. **ナレッジストアにおける画像サービングの制限**:
   - ナレッジストアに関する部分で、感度ラベルを取り込む知識ソースでは画像サービングがサポートされないことが追記されました。これにより、ユーザーは感度ラベルを扱う際の制約を理解しやすくなり、知識ストアの利用方法がより明確になります。

このアップデートにより、Azure AI Searchの利用者は感度ラベルのインデクシング機能について正確な情報を得られるとともに、ナレッジストアとの連携に関する制約を考慮することができ、より効果的にこれらの機能を活用できるようになります。

## articles/search/search-indexer-sharepoint-access-control-lists.md{#item-532a24}

<details>
<summary>Diff</summary>
````diff
@@ -63,7 +63,7 @@ This article explains how to ingest an access control list (ACL) alongside other
 
   + [Custom Web API skill](cognitive-search-custom-skill-web-api.md)
 
-  + [Knowledge store](knowledge-store-concept-intro.md)
+  + [Knowledge store](knowledge-store-concept-intro.md), including the asset store required for [image serving (preview)](agentic-retrieval-how-to-image-serving.md) in agentic retrieval. Therefore, image serving isn't supported for knowledge sources that ingest SharePoint ACLs.
 
   + [Indexer enrichment cache](enrichment-cache-how-to-configure.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointのアクセ制御リストに関する情報の更新"
}
```

### Explanation
この変更は、「SharePointのアクセ制御リスト」に関する文書に対するマイナーアップデートで、ナレッジストアにおける画像サービングの制限が追加されています。

1. **ナレッジストアの画像サービング制限の明記**:
   - 変更により、ナレッジストアが画像サービング機能を持つことが記載され、その機能がSharePointのアクセス制御リスト（ACL）を取り込む知識ソースに対してはサポートされないことが明確にされています。これにより、ユーザーはこの制約を理解し、適切に機能を利用できるようになります。

2. **文書の明瞭さ向上**:
   - 変更内容により、ナレッジストアとの統合に関する点が強調され、知識ストアを利用する際の安全性や使い方に関する情報が充実しました。その結果、ユーザーがSharePointと連携する際の操作や制限についてすっきりとした理解を得ることができるようになります。

このアップデートによって、ユーザーはSharePointにおけるアクセス制御リストの取り扱いやナレッジストアの機能について、より具体的な情報を得ることができ、実際の利用に役立てることができるでしょう。


