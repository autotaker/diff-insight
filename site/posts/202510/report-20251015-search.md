---
date: '2025-10-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:33195af...MicrosoftDocs:c693aca
summary: この変更において、新しいドキュメントが追加され、既存の多くのドキュメントが更新されました。主にAzure AI Searchに関する知識ソースや検索インデックスの管理、およびセキュリティの強化に焦点を当てた修正と最適化が行われています。特に新しいREST
  APIに関するドキュメントの追加と、クロステナントの顧客管理キー設定に関するガイドが注目されます。また、コードスニペットや構造の簡素化が行われ、ユーザビリティが向上しました。全体として、これらの改訂はAzure
  AI Searchの利便性とセキュリティを高めることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:33195af...MicrosoftDocs:c693aca){target="_blank"}

<format>
# Highlights
この変更では、新たなドキュメントと共に多くの既存ドキュメントが更新され、Azure AI Searchにおける知識ソースや検索インデックスの管理、セキュリティの強化に関する様々な修正と最適化が図られています。特に新しいREST APIドキュメントの追加や、クロステナントの顧客管理キー（CMK）に関するガイドが目を引きます。特定のドキュメントでは、コードスニペットの変更と構造の簡素化が進められました。

## 新しい機能
- `articles/search/includes/how-tos/knowledge-source-check-rest.md` の追加により、新しいREST APIドキュメントが提供されました。
- クロステナントのCMK設定ガイドとして `articles/search/search-security-managed-encryption-cross-tenant.md` が導入されました。

## ブレイキングチェンジ
- `articles/search/includes/quickstarts/semantic-ranker-java.md` は、大幅に改訂され、構成と内容が刷新されました。

## その他の更新
- `agentic-knowledge-source-how-to-blob.md` など複数のガイドが内容を精錬し、より明確で理解しやすい形に更新されました。
- JavaやTypeScriptのクイックスタートガイドが簡素化され、コードスニペットの参照方法が見直されました。
- セキュリティ関係のドキュメントに関連情報が追加され、ユーザビリティが向上しました。

# Insights
この一連の更新では、Azure AI Searchプラットフォームの利便性とセキュリティ強化が重要視されています。特に注目すべきは、技術的な指導と情報のアクセス性を高めるために、ドキュメントの簡素化と新しいリソースの導入が行われていることです。

新しい REST API ドキュメントの追加により、開発者は知識ソース管理をより効率的に行うことが可能となり、Azure AI Search の機能を最大限に活用するための基盤が整えられました。また、クロステナント間での顧客管理キー暗号化のガイドの導入は、多様なテナント構成を扱う企業に対してのサポートを強化するもので、セキュリティの確保に一段と貢献しています。

一方で、Javaを用いるセマンティックランカーの大幅な改訂は、構成の可読性向上と効率化を追求したもので、一貫した開発経験を提供するためのステップと捉えられます。既存の知識ソースと検索インデックスのガイドの見直しも、ユーザーがAzureプラットフォームを利用する上でのスムーズな操作をサポートします。

全体として、この更新の目的は、技術者がより直感的に新しい環境に適応し、迅速かつセキュアに機能を展開できるようにすることです。このような取り組みにより、Azure AI Search の利用者はより戦略的にプラットフォームを運用できるようになるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-blob.md](#item-ac6c8a) | minor update | エージェント知識ソースに関するBlobの作成方法の更新 | modified | 49 | 92 | 141 | 
| [agentic-knowledge-source-how-to-search-index.md](#item-09d366) | minor update | エージェント知識ソースに関する検索インデックスの作成方法の更新 | modified | 21 | 42 | 63 | 
| [agentic-retrieval-how-to-create-index.md](#item-3fbd2e) | minor update | エージェント検索用インデックス作成に関する日付の更新 | modified | 1 | 2 | 3 | 
| [knowledge-source-check-rest.md](#item-47d679) | new feature | 知識ソース確認用のREST APIドキュメントの追加 | added | 28 | 0 | 28 | 
| [search-get-started-rag-java.md](#item-26c939) | minor update | Javaのクイックスタートドキュメントの簡略化とコードスニペットの更新 | modified | 3 | 220 | 223 | 
| [search-get-started-vector-java.md](#item-a3db97) | minor update | Javaのベクトル検索クイックスタートドキュメントの更新 | modified | 21 | 992 | 1013 | 
| [search-get-started-vector-javascript.md](#item-d0387c) | minor update | JavaScriptのベクトル検索クイックスタート文書の軽微な修正 | modified | 1 | 1 | 2 | 
| [search-get-started-vector-typescript.md](#item-9b3bc8) | minor update | TypeScriptのベクトル検索クイックスタート文書の修正 | modified | 4 | 3 | 7 | 
| [semantic-ranker-java.md](#item-93a05a) | breaking change | Javaのセマンティックランカーに関するクイックスタート文書の全面改訂 | modified | 7 | 455 | 462 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | ベクターインポートガイドの文言修正 | modified | 1 | 1 | 2 | 
| [search-how-to-integrated-vectorization.md](#item-86fb1e) | minor update | 統合ベクター化に関するガイドの文言修正と情報追加 | modified | 5 | 3 | 8 | 
| [search-security-manage-encryption-keys.md](#item-db3487) | minor update | 暗号化キー管理に関するガイドの文言修正と情報追加 | modified | 1 | 1 | 2 | 
| [search-security-managed-encryption-cross-tenant.md](#item-efc726) | new feature | 異なるテナント間での顧客管理キー（CMK）暗号化設定ガイドの追加 | added | 126 | 0 | 126 | 
| [search-security-overview.md](#item-6b3f1e) | minor update | セキュリティ概要ドキュメントの見出し変更と関連コンテンツの追加 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c4768f) | minor update | 目次ファイルの変更: 顧客管理キーの名称変更と新規項目の追加 | modified | 3 | 1 | 4 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-blob.md{#item-ac6c8a}

<details>
<summary>Diff</summary>
````diff
@@ -7,59 +7,37 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 10/10/2025
+ms.date: 10/13/2025
 ---
 
 # Create a blob knowledge source
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-A *blob knowledge source* specifies all of the information necessary for indexing and querying multimodal Azure blob content in an Azure AI Search agentic pipeline. It's created independently, and then referenced by a [knowledge agent](agentic-retrieval-how-to-create-knowledge-base.md) and used at query time when an agent or chat bot calls a [retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true) action.
+Use a *blob knowledge source* to index and query Azure blob content in an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge agent](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true) action at query time.
 
-In contrast with a [search index knowledge source](agentic-knowledge-source-how-to-search-index.md) that specifies an existing and qualified index, a blob knowledge source specifies an external data source (a blob container) plus models and properties that are used to create an entire enrichment pipeline:
+Unlike a [search index knowledge source](agentic-knowledge-source-how-to-search-index.md), which specifies an existing and qualified index, a blob knowledge source specifies an external data source, models, and properties to automatically generate the following Azure AI Search objects:
 
-+ The generated data source specifies the blob container
-+ The generated skillset chunks and vectorizes multimodal content
-+ The generated index stores indexed content and meets the criteria for agentic retrieval
-+ The generated indexer drives the indexing and enrichment pipeline
-
-The generated index provides the content that's used by a knowledge agent.
++ A data source that represents a blob container.
++ A skillset that chunks and optionally vectorizes multimodal content from the container.
++ An index that stores enriched content and meets the criteria for agentic retrieval.
++ An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
 
 Knowledge sources are new in the 2025-08-01-preview release.
 
 ## Prerequisites
 
-+ Azure Storage with a blob container containing [supported content types](search-how-to-index-azure-blob-storage.md#supported-document-formats) for text content. For images, the supported content type depends on your chat completion model and whether it can analyze and describe the image file.
-
-+ Azure AI Search, basic tier or higher, configured for semantic ranker.
++ Azure Storage with a blob container containing [supported content types](search-how-to-index-azure-blob-storage.md#supported-document-formats) for text content. For optional image verbalization, the supported content type depends on whether your chat completion model can analyze and describe the image file.
 
-+ An embedding model and a chat completion model used for verbalizing images. Depending on the models you specify, the generated skillset can include any of the following skills: [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md), [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md), [Azure AI Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md), [AML skill](cognitive-search-aml-skill.md). Each of these skills has a finite list of supported models. Check the skill documentation for supported models.
++ Azure AI Search on the Basic tier or higher with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
-To try the examples in this article, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending preview REST API calls to Azure AI Search. There's no portal support at this time.
+To try the examples in this article, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending preview REST API calls to Azure AI Search. Currently, there's no portal support.
 
 ## Check for existing knowledge sources
 
-A knowledge source is a top-level, reusable object. All knowledge sources must be uniquely named within the knowledge sources collection. It's helpful to know about existing knowledge sources for either reuse or for naming new objects.
-
-The following request lists knowledge sources by name and type.
-
-```http
-# List knowledge sources by name and type
-GET {{search-url}}/knowledgeSources?api-version=2025-08-01-preview&$select=name,kind
-api-key: {{api-key}}
-Content-Type: application/json
-```
-
-You can also return a single knowledge source by name to review its JSON definition.
-
-```http
-### Get a knowledge source definition
-GET {{search-url}}/knowledgeSources/{{knowledge-source-name}}?api-version=2025-08-01-preview
-api-key: {{api-key}}
-Content-Type: application/json
-```
+[!INCLUDE [Check for existing knowledge sources](includes/how-tos/knowledge-source-check-rest.md)]
 
-A response for blob knowledge source might look like the following example. 
+The following JSON is an example response for an `azureBlob` knowledge source.
 
 ```json
 {
@@ -110,104 +88,83 @@ A response for blob knowledge source might look like the following example.
 ```
 
 > [!NOTE]
-> Sensitive information is redacted. The generated resources appear at the end of the response. The `webParameters` property isn't operational in this preview and it's reserved for future use.
+> Sensitive information is redacted. The generated resources appear at the end of the response. The `webParameters` property isn't operational in this preview and is reserved for future use.
 
 ## Create a knowledge source
 
-To create a [knowledge source](agentic-knowledge-source-overview.md), use the 2025-08-01-preview data plane REST API or an Azure SDK preview package that provides equivalent functionality.
-
-A knowledge source can contain exactly one of the following: `searchIndexParameters` *or* `azureBlobParameters`. The `webParameters` property isn't supported in this release. If you specify `azureBlobParameters`, then `searchIndexParameters` must be null.
-
-For `azureBlobParameters`:
-
-+ Provide a connection to Azure AI Search
-+ Provide a full access connection string for Azure Storage and the container name
-+ Provide a text embedding model. This model is used to vectorize text content during indexing and queries.
-+ Provide a chat completion model used for describing image content.
-+ Provide an encryption key to doubly encrypt sensitive information in this knowledge source and in the generated resources.
-
-Models are referenced in the skillset and as vectorizer for encoding text strings at query time.
-
-A blob knowledge source can include an `ingestionSchedule` that adds scheduling information to an indexer. You can also [add a schedule](search-howto-schedule-indexers.md) later if you want to automate data refresh
-
-1. Use the [Create or Update Knowledge Source](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) preview REST API.
+To create an `azureBlob` knowledge source:
 
 1. Set environment variables at the top of your file.
 
     ```http
-    @search-url=<YOUR SEARCH SERVICE URL>
-    @api-key=<YOUR SEARCH ADMIN API KEY>
-    @connection-string=<YOUR FULL ACCESS CONNECTION STRING TO AZURE STORAGE>
-    @aoai-endpoint=<YOUR AZURE OPENAI ENDPOINT>
-    @aoai-key=<YOUR AZURE OPENAI API KEY>
+    @search-url = <YOUR SEARCH SERVICE URL>
+    @api-key = <YOUR SEARCH ADMIN API KEY>
+    @ks-name = <YOUR KNOWLEDGE SOURCE NAME>
+    @connection-string = <YOUR FULL ACCESS CONNECTION STRING TO AZURE STORAGE>
+    @container-name = <YOUR BLOB CONTAINER NAME>
     ```
 
-1. Formulate the request and then **Send**.
+1. Use the 2025-08-01-preview of [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) or an Azure SDK preview package that provides equivalent functionality to formulate the request.
 
     ```http
     PUT {{search-url}}/knowledgeSources/earth-at-night-blob-ks?api-version=2025-08-01-preview
     api-key: {{api-key}}
     Content-Type: application/json
     
     {
-      "name": "earth-at-night-blob-ks",
+      "name": "{{ks-name}}",
       "kind": "azureBlob",
-      "description": "This knowledge source pull from a blob storage container containing pages from the Earth at Night PDF.",
+      "description": "This knowledge source pulls from a blob storage container containing pages from the Earth at Night PDF.",
       "encryptionKey": null,
       "azureBlobParameters": {
         "connectionString": "{{connection-string}}",
-        "containerName": "nasa-ebook",
+        "containerName": "{{container-name}}",
         "folderPath": null,
         "disableImageVerbalization": null,
         "identity": null,
         "embeddingModel": {
-          "kind": "azureOpenAI",
-          "azureOpenAIParameters": {
-            "resourceUri": "{{aoai-endpoint}}",
-            "deploymentId": "text-embedding-3-small",
-            "apiKey": "{{aoai-key}}",
-            "modelName": "text-embedding-3-small",
-            "authIdentity": null
-          },
-          "customWebApiParameters": null,
-          "aiServicesVisionParameters": null,
-          "amlParameters": null
+          // Redacted for brevity
         },
         "chatCompletionModel": {
-          "kind": "azureOpenAI",
-          "azureOpenAIParameters": {
-            "resourceUri": "{{aoai-endpoint}}",
-            "deploymentId": "gpt-5-mini",
-            "apiKey": "{{aoai-key}}",
-            "modelName": "gpt-5-mini",
-            "authIdentity": null
-          }
+          // Redacted for brevity
         },
         "ingestionSchedule": {
-          "interval": "P1D",
-          "startTime": "2025-01-07T19:30:00Z"
+          // Redacted for brevity
         }
       }
     }
     ```
 
-If you get errors, make sure the embedding model and chat completion models exist at the endpoint you provided.
+1. Select **Send Request**.
+
+**Key points:**
+
++ `name` must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search.
+
++ `kind` must be `azureBlob` for a blob knowledge source.
+
++ `encryptionKey` (optional) is an encryption key in Azure Key Vault. Use this property to doubly encrypt sensitive information in both the knowledge source and the generated objects.
+
++ `embeddingModel` (optional) is a text embedding model that vectorizes text and image content during indexing and at query time. Use a model supported by the [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md), [Azure AI Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md), [AML skill](cognitive-search-aml-skill.md), or [Custom Web API skill](cognitive-search-custom-skill-web-api.md). The embedding skill will be included in the generated skillset, and its equivalent vectorizer will be included in the generated index.
 
-## Check output
++ `chatCompletionModel` (optional) is a chat completion model that verbalizes images or extracts content. Use a model supported by the [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md), which will be included in the generated skillset. To skip image verbalization, omit this object and set `"disableImageVerbalization": true`.
 
-When you create a blob knowledge source, the search service also creates the following objects: an indexer, data source, skillset, and index. Exercise caution when editing these objects because you can break the pipeline if you introduce an error or incompatibility.
++ `ingestionSchedule` (optional) adds scheduling information to the generated indexer. You can also [add a schedule](search-howto-schedule-indexers.md) later to automate data refresh.
 
-The response on knowledge source creation lists the created resources. Objects are created according to a fixed template and naming is based on the knowledge source. You can't change the object names.
++ If you get errors, make sure the embedding and chat completion models exist at the endpoints you provided.
 
-We recommend using the Azure portal to validate output creation.
+## Review the created objects
 
-1. Check the indexer for success or failure messages. Connection or quota errors appear here. If the indexer failed, try reset and rerun.
+When you create a blob knowledge source, your search service also creates an indexer, data source, skillset, and index. Exercise caution when you edit these objects, as introducing an error or incompatibility can break the pipeline.
 
-1. Check the index for searchable content. Use Search Explorer to run your queries.
+After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
 
-1. Check the skillset to learn more about how your content is chunked and vectorized.
+We recommend using the Azure portal to validate output creation. The workflow is:
 
-1. Modify the data source if you want to change connection details, such as authentication and authorization. The example uses API keys for simplicity but you can use Microsoft Entra ID authentication and role-based access.
+1. Check the indexer for success or failure messages. Connection or quota errors appear here.
+1. Check the index for searchable content. Use Search Explorer to run queries.
+1. Check the skillset to learn how your content is chunked and optionally vectorized.
+1. Modify the data source if you want to change connection details, such as authentication and authorization. Our example uses API keys for simplicity, but you can use Microsoft Entra ID authentication and role-based access.
 
 ## Assign to a knowledge agent
 
@@ -221,7 +178,7 @@ After the knowledge agent is configured, use the retrieve action to query the kn
 
 [!INCLUDE [Delete knowledge source](includes/how-tos/knowledge-source-delete-rest.md)]
 
-## Learn more
+## Related content
 
 + [Azure AI Search Blob knowledge source Python sample](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/knowledge/blob-knowledge-source.ipynb)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースに関するBlobの作成方法の更新"
}
```

### Explanation
このコードの差分では、`agentic-knowledge-source-how-to-blob.md` ドキュメントの 更新が行われています。主な変更点は、Azure Blob コンテンツをインデックス化およびクエリする方法に関する記述が改善され、多くの文が簡潔かつ明確に修正されています。また、情報の順序や表現方法が整理され、リッチさが増しています。

具体的には、Blob 知識ソースの作成における重要な要素やプロセスがよりわかりやすく記載されています。例えば、Blob 知識ソースがエージェントやチャットボットによって参照され、クエリ時に使用されるという流れが強調されています。また、生成されるリソースの説明においても、より明瞭な文が使われ、ユーザーが理解しやすい形になっています。

さらに、前回のリリース日が指定され、新たに知識ソースが追加されたことも示されています。最近の変更により、Azure AI Search の Blob 知識ソースに関する情報が最適化され、機能の利用がスムーズになることを目的としています。この更新により、ユーザーは前回のリリースからの変更点を把握し、正確な情報に基づいて Blob を管理できるようになるでしょう。

## articles/search/agentic-knowledge-source-how-to-search-index.md{#item-09d366}

<details>
<summary>Diff</summary>
````diff
@@ -14,39 +14,21 @@ ms.date: 10/10/2025
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-A *search index knowledge source* specifies a connection to a search index on Azure AI Search that provides searchable content in an agentic retrieval pipeline. It's created independently, and then referenced by a [knowledge agent](agentic-retrieval-how-to-create-knowledge-base.md) and used at query time when an agent or chat bot calls a [retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true) action.
+A *search index knowledge source* specifies a connection to an Azure AI Search index that provides searchable content in an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge agent](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true) action at query time.
 
 Knowledge sources are new in the 2025-08-01-preview release.
 
 ## Prerequisites
 
-You need a search index containing plain text or vector content, with a semantic configuration. [Review index criteria for agentic retrieval](agentic-retrieval-how-to-create-index.md#criteria-for-agentic-retrieval). The search index must be on the same search service as the knowledge agent.
+You need a search index containing plain text or vector content with a semantic configuration. [Review the index criteria for agentic retrieval](agentic-retrieval-how-to-create-index.md#criteria-for-agentic-retrieval). The index must be on the same search service as the knowledge agent.
 
-To try the examples in this article, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending preview REST API calls to Azure AI Search. There's no portal support at this time.
+To try the examples in this article, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending preview REST API calls to Azure AI Search. Currently, there's no portal support.
 
 ## Check for existing knowledge sources
 
-A knowledge source is a top-level, reusable object. All knowledge sources must be uniquely named within the knowledge sources collection. It's helpful to know about existing knowledge sources for either reuse or for naming new objects.
+[!INCLUDE [Check for existing knowledge sources](includes/how-tos/knowledge-source-check-rest.md)]
 
-Example request: List all knowledge sources on a search service by name and type.
-
-```http
-# List knowledge sources by name and type
-GET {{search-url}}/knowledgeSources?api-version=2025-08-01-preview&$select=name,kind
-api-key: {{api-key}}
-Content-Type: application/json
-```
-
-Example request: Return a single knowledge source by name to review its JSON definition.
-
-```http
-### Get a knowledge source definition
-GET {{search-url}}/knowledgeSources/{{knowledge-source-name}}?api-version=2025-08-01-preview
-api-key: {{api-key}}
-Content-Type: application/json
-```
-
-An example response for a `searchIndex` knowledge source might look like the following JSON. Notice that the knowledge source specifies a single index name and which fields in the index to include in the query.
+The following JSON is an example response for a `searchIndex` knowledge source. Notice that the knowledge source specifies a single index name and which fields in the index to include in the query.
 
 ```json
 {
@@ -65,31 +47,22 @@ An example response for a `searchIndex` knowledge source might look like the fol
 ```
 
 > [!NOTE]
-> The `webParameters` property isn't operational in this preview and it's reserved for future use.
+> The `webParameters` property isn't operational in this preview and is reserved for future use.
 
 ## Create a knowledge source
 
-To create a [knowledge source](agentic-knowledge-source-overview.md), use the 2025-08-01-preview data plane REST API or an Azure SDK preview package that provides equivalent functionality.
-
-A knowledge source can contain exactly one of the following: `searchIndexParameters` *or* `azureBlobParameters`. The `webParameters` property isn't supported in this release. If you specify `searchIndexParameters`, then `azureBlobParameters` must be null.
-
-For `searchIndexParameters`:
-
-+ Choose an index [designed for agentic retrieval](agentic-retrieval-how-to-create-index.md)
-+ Specify any `retrievable` fields that can be used for citations, such as a file name or page number.
-
-1. Use the [Create or Update Knowledge Source](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) preview REST API.
+To create a `searchIndex` knowledge source:
 
 1. Set environment variables at the top of your file.
 
     ```http
-    @search-url=<YOUR SEARCH SERVICE URL>
-    @api-key=<YOUR ADMIN API KEY>
-    @ks-name=<YOUR KNOWLEDGE SOURCE NAME>
-    @index-name=<YOUR INDEX NAME>
+    @search-url = <YOUR SEARCH SERVICE URL>
+    @api-key = <YOUR ADMIN API KEY>
+    @ks-name = <YOUR KNOWLEDGE SOURCE NAME>
+    @index-name = <YOUR INDEX NAME>
     ```
 
-1. Formulate the request and then **Send**.
+1. Use the 2025-08-01-preview of [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) or an Azure SDK preview package that provides equivalent functionality to formulate the request.
 
     ```http
     POST {{search-url}}/knowledgeSources?api-version=2025-08-01-preview
@@ -107,11 +80,17 @@ For `searchIndexParameters`:
     }
     ```
 
+1. Select **Send Request**.
+
 **Key points**:
 
-+ `name` must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects on Azure AI Search.
++ `name` must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search.
+
++ `kind` must be `searchIndex` for a search index knowledge source.
+
++ `searchIndexName` is the name of your index, which must be [designed for agentic retrieval](agentic-retrieval-how-to-create-index.md).
 
-+ `sourceDataSelect` is the list of fields returned if you specify `includeReferenceSourceData` in the knowledge agent definition. These fields are used for the citation view experience and should include fields like a document or file name, page or chapter number, and so forth.
++ `sourceDataSelect` is the list of index fields returned when you specify `includeReferenceSourceData` in the knowledge agent definition. These fields are used for citations and should be `retrievable`. Examples include the document name, file name, page numbers, or chapter numbers.
 
 ## Assign to a knowledge agent
 
@@ -123,7 +102,7 @@ Within the knowledge agent, there are more properties to set on the knowledge so
 
 [!INCLUDE [Delete knowledge source](includes/how-tos/knowledge-source-delete-rest.md)]
 
-## Learn more
+## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースに関する検索インデックスの作成方法の更新"
}
```

### Explanation
このコードの差分では、`agentic-knowledge-source-how-to-search-index.md` ドキュメントに対するいくつかの修正が行われています。これらの修正は主に文章の明確さと一貫性を向上させることを目的としており、情報が分かりやすくなるように再構成されています。

具体的には、検索インデックスの知識ソースがAzure AI Searchインデックスに接続することによって、エージェントの検索パイプラインで検索可能なコンテンツを提供することが説明されています。文の一部が変更され、内容が簡潔にまとめられています。さらに、知識ソースの作成に関する手順も整備され、環境変数の設定やリクエストの送信方法が具体的に示されています。

また、必要な要件や事前条件についての情報も明確にされ、知識ソースを作成するための必須要素が明示されています。Markdown内でのインクルード文や例リクエストも改訂され、ユーザーが教示内容を簡単に理解できるように改善されています。全体的に、この更新は、ユーザーが知識ソースを効果的に作成し利用するための参考となる内容になっています。

## articles/search/agentic-retrieval-how-to-create-index.md{#item-3fbd2e}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 10/01/2025
+ms.date: 10/13/2025
 ---
 
 # Design an index for agentic retrieval in Azure AI Search
@@ -91,7 +91,6 @@ Here's an example index that works for agentic retrieval. It meets the criteria
   "tokenizers": [],
   "tokenFilters": [],
   "charFilters": [],
-  "similarity": {},
   "semantic": {
     "defaultConfiguration": "semantic_config",
     "configurations": [
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索用インデックス作成に関する日付の更新"
}
```

### Explanation
このコードの差分では、`agentic-retrieval-how-to-create-index.md` ドキュメントの更新が行われています。主な変更点は、ドキュメントの日付が「2025年10月1日」から「2025年10月13日」に変更されたことです。この小さな変更は、コンテンツの最新版の日付を反映させるためのものです。

さらに、他の部分では、エージェント検索用インデックスのデザインに関する情報には直接的な変更はありませんが、ドキュメント全体の整合性や最新情報を確保するための重要な更新です。特に日付の情報は、ユーザーに対してドキュメントがどの程度新しいかを示すため、重要な要素と言えます。このような更新により、ユーザーは常に最新の情報を基に作業することができ、確実性を持ちながらインデックスを設計することが可能になります。

## articles/search/includes/how-tos/knowledge-source-check-rest.md{#item-47d679}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,28 @@
+---
+manager: nitinme
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 10/13/2025
+---
+
+A knowledge source is a top-level, reusable object. All knowledge sources must be uniquely named within the knowledge sources collection. Knowing about existing knowledge sources is helpful for either reuse or naming new objects.
+
+Use [Knowledge Sources - Get (REST API)](/rest/api/searchservice/knowledge-sources/get?view=rest-searchservice-2025-08-01-preview&preserve-view=true) to list knowledge sources by name and type.
+
+```http
+### List knowledge sources by name and type
+GET {{search-url}}/knowledgeSources?api-version=2025-08-01-preview&$select=name,kind
+api-key: {{api-key}}
+Content-Type: application/json
+```
+
+You can also return a single knowledge source by name to review its JSON definition.
+
+```http
+### Get a knowledge source definition
+GET {{search-url}}/knowledgeSources/{{knowledge-source-name}}?api-version=2025-08-01-preview
+api-key: {{api-key}}
+Content-Type: application/json
+```
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "知識ソース確認用のREST APIドキュメントの追加"
}
```

### Explanation
このコードの差分では、`knowledge-source-check-rest.md` という新しいドキュメントが追加されています。このドキュメントは、知識ソースの管理に関する重要な情報を提供します。

新しく追加された内容には、知識ソースが再利用可能なトップレベルのオブジェクトであり、すべての知識ソースはユニークな名前を持つ必要があることが説明されています。また、既存の知識ソースについての情報を取得することが、新しいオブジェクトの命名や再利用に役立つことを強調しています。

具体的には、REST APIを使用して知識ソースを名前とタイプでリストする方法や、特定の知識ソースのJSON定義を取得する方法が示されています。これにより、開発者はAPIを利用して知識ソースの管理を効率よく行うことができるようになります。ドキュメントは具体的なHTTPリクエストの例も含んでおり、実際の使用に役立つ内容となっています。

全体として、この新しいドキュメントは、Azure AI Searchにおける知識ソースの管理をサポートするための重要なリソースです。

## articles/search/includes/quickstarts/search-get-started-rag-java.md{#item-26c939}

<details>
<summary>Diff</summary>
````diff
@@ -238,140 +238,15 @@ Set up a Maven project with the required dependencies.
 
 1. Create a `pom.xml` file with the following content:
 
-   ```xml
-   <?xml version="1.0" encoding="UTF-8"?>
-   <project xmlns="http://maven.apache.org/POM/4.0.0"
-            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
-            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
-            http://maven.apache.org/xsd/maven-4.0.0.xsd">
-       <modelVersion>4.0.0</modelVersion>
-       
-       <groupId>com.example.rag</groupId>
-       <artifactId>rag-quickstart</artifactId>
-       <version>1.0-SNAPSHOT</version>
-       
-       <properties>
-           <maven.compiler.source>21</maven.compiler.source>
-           <maven.compiler.target>21</maven.compiler.target>
-           <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
-       </properties>
-       
-       <dependencies>
-           <dependency>
-               <groupId>com.azure</groupId>
-               <artifactId>azure-search-documents</artifactId>
-               <version>11.7.8</version>
-           </dependency>
-           <dependency>
-               <groupId>com.azure</groupId>
-               <artifactId>azure-identity</artifactId>
-               <version>1.16.3</version>
-           </dependency>
-           <dependency>
-               <groupId>com.azure</groupId>
-               <artifactId>azure-ai-openai</artifactId>
-               <version>1.0.0-beta.16</version>
-           </dependency>
-       </dependencies>
-   </project>
-   ```
+   :::code language="xml" source="~/azure-search-java-samples/rag-quickstart/pom.xml" :::
 
 ## Set up query and chat thread
 
 Create a query script that uses the Azure AI Search index and the chat model to generate responses based on grounding data. The following steps guide you through setting up the query script.
 
 1. Create a `Query.java` file in the `src/main/java/com/example/rag` directory with the following code:
 
-    ```java
-    package com.example.rag;
-    
-    import com.azure.ai.openai.OpenAIClient;
-    import com.azure.ai.openai.OpenAIClientBuilder;
-    import com.azure.ai.openai.models.ChatCompletions;
-    import com.azure.ai.openai.models.ChatCompletionsOptions;
-    import com.azure.ai.openai.models.ChatRequestSystemMessage;
-    import com.azure.ai.openai.models.ChatRequestUserMessage;
-    import com.azure.identity.DefaultAzureCredentialBuilder;
-    import com.azure.search.documents.SearchClient;
-    import com.azure.search.documents.SearchClientBuilder;
-    import com.azure.search.documents.models.SearchOptions;
-    import com.azure.search.documents.models.SearchResult;
-    
-    import java.util.List;
-    
-    public class Query {
-        private static SearchClient getSearchClient() {
-            String searchEndpoint = System.getenv("AZURE_SEARCH_ENDPOINT");
-            String searchIndex = System.getenv("AZURE_SEARCH_INDEX_NAME");
-    
-            return new SearchClientBuilder()
-                    .endpoint(searchEndpoint)
-                    .indexName(searchIndex)
-                    .credential(new DefaultAzureCredentialBuilder().build())
-                    .buildClient();
-        }
-    
-        private static OpenAIClient getOpenAIClient() {
-            String openaiEndpoint = System.getenv("AZURE_OPENAI_ENDPOINT");
-    
-            return new OpenAIClientBuilder()
-                    .endpoint(openaiEndpoint)
-                    .credential(new DefaultAzureCredentialBuilder().build())
-                    .buildClient();
-        }
-    
-        private static List<SearchResult> searchDocuments(
-            SearchClient searchClient, String query) {
-            var searchOptions = new SearchOptions()
-                    .setTop(5)
-                    .setQueryType(com.azure.search.documents.models.QueryType.SEMANTIC)
-                    .setSemanticSearchOptions(new com.azure.search.documents.models.SemanticSearchOptions()
-                            .setSemanticConfigurationName("semantic-config"))
-                    .setSelect("HotelName", "Description", "Tags");
-    
-            return searchClient.search(query, searchOptions, null)
-                    .stream()
-                    .limit(5)
-                    .toList();
-        }
-    
-        private static String queryOpenAI(OpenAIClient openAIClient,
-            String userQuery, List<SearchResult> sources) {
-            String deploymentModel = System.getenv("AZURE_DEPLOYMENT_MODEL");
-    
-            String sourcesText = sources.stream()
-                    .map(source -> source.getDocument(Object.class).toString())
-                    .collect(java.util.stream.Collectors.joining("\n"));
-    
-            var messages = List.of(
-                    new ChatRequestSystemMessage("""
-                        You are an assistant that recommends hotels based on 
-                        search results."""),
-                    new ChatRequestUserMessage("""
-                        Can you recommend a few hotels that offer %s?
-                        Here are the search results:
-                        %s""".formatted(userQuery, sourcesText))
-            );
-    
-            var chatOptions = new ChatCompletionsOptions(messages);
-            ChatCompletions response = openAIClient.getChatCompletions(deploymentModel, chatOptions);
-    
-            return response.getChoices().get(0).getMessage().getContent();
-        }
-    
-        public static void main(String[] args) {
-            SearchClient searchClient = getSearchClient();
-            OpenAIClient openAIClient = getOpenAIClient();
-    
-            String userQuery = "complimentary breakfast";
-            List<SearchResult> sources = searchDocuments(searchClient, userQuery);
-            String response = queryOpenAI(openAIClient, userQuery, sources);
-    
-            System.out.println(response);
-            System.exit(0);
-        }
-    }
-    ```
+   :::code language="java" source="~/azure-search-java-samples/rag-quickstart/src/main/java/com/example/rag/Query.java" :::
 
     The preceding code does the following steps:
     - Loads environment variables by using `System.getenv`.
@@ -435,99 +310,7 @@ Tell me their description, address, tags, and the rate for one room that sleeps
 1. Create a new file `QueryComplex.java` in the `src/main/java/com/example/rag` directory.
 1. Copy the following code to the file:
 
-    ```java
-    package com.example.rag;
-    
-    import com.azure.ai.openai.OpenAIClient;
-    import com.azure.ai.openai.OpenAIClientBuilder;
-    import com.azure.ai.openai.models.ChatCompletions;
-    import com.azure.ai.openai.models.ChatCompletionsOptions;
-    import com.azure.ai.openai.models.ChatRequestSystemMessage;
-    import com.azure.ai.openai.models.ChatRequestUserMessage;
-    import com.azure.identity.DefaultAzureCredentialBuilder;
-    import com.azure.search.documents.SearchClient;
-    import com.azure.search.documents.SearchClientBuilder;
-    import com.azure.search.documents.models.SearchOptions;
-    import com.azure.search.documents.models.SearchResult;
-    
-    import java.util.List;
-    
-    public class QueryComplex {
-        private static SearchClient getSearchClient() {
-            String searchEndpoint = System.getenv("AZURE_SEARCH_ENDPOINT");
-            String searchIndex = System.getenv("AZURE_SEARCH_INDEX_NAME");
-    
-            return new SearchClientBuilder()
-                    .endpoint(searchEndpoint)
-                    .indexName(searchIndex)
-                    .credential(new DefaultAzureCredentialBuilder().build())
-                    .buildClient();
-        }
-    
-        private static OpenAIClient getOpenAIClient() {
-            String openaiEndpoint = System.getenv("AZURE_OPENAI_ENDPOINT");
-    
-            return new OpenAIClientBuilder()
-                    .endpoint(openaiEndpoint)
-                    .credential(new DefaultAzureCredentialBuilder().build())
-                    .buildClient();
-        }
-    
-        private static List<SearchResult> searchDocuments(
-            SearchClient searchClient, String query) {
-            var searchOptions = new SearchOptions()
-                    .setTop(5)
-                    .setQueryType(com.azure.search.documents.models.QueryType.SEMANTIC)
-                    .setSemanticSearchOptions(new com.azure.search.documents.models.SemanticSearchOptions()
-                            .setSemanticConfigurationName("semantic-config"))
-                    .setSelect("HotelName", "Description", "Address", "Rooms", "Tags");
-    
-            return searchClient.search(query, searchOptions, null)
-                    .stream()
-                    .limit(5)
-                    .toList();
-        }
-    
-        private static String queryOpenAI(OpenAIClient openAIClient,
-            String userQuery, List<SearchResult> sources) {
-            String deploymentModel = System.getenv("AZURE_DEPLOYMENT_MODEL");
-    
-            String sourcesText = sources.stream()
-                    .map(source -> source.getDocument(Object.class).toString())
-                    .collect(java.util.stream.Collectors.joining("\n"));
-    
-            var messages = List.of(
-                    new ChatRequestSystemMessage("""
-                        You are an assistant that recommends hotels based on 
-                        search results."""),
-                    new ChatRequestUserMessage("""
-                        Can you recommend a few hotels that offer %s?
-                        Tell me their description, address, tags,
-                        and the rate for one room that sleeps 4 people.
-                        Here are the search results:
-                        %s""".formatted(userQuery, sourcesText))
-            );
-    
-            var chatOptions = new ChatCompletionsOptions(messages);
-            ChatCompletions response = openAIClient.getChatCompletions(
-                deploymentModel, chatOptions);
-    
-            return response.getChoices().get(0).getMessage().getContent();
-        }
-    
-        public static void main(String[] args) {
-            SearchClient searchClient = getSearchClient();
-            OpenAIClient openAIClient = getOpenAIClient();
-    
-            String userQuery = "complimentary breakfast";
-            List<SearchResult> sources = searchDocuments(searchClient, userQuery);
-            String response = queryOpenAI(openAIClient, userQuery, sources);
-    
-            System.out.println(response);
-            System.exit(0);
-        }
-    }
-    ```
+   :::code language="java" source="~/azure-search-java-samples/rag-quickstart/src/main/java/com/example/rag/QueryComplex.java" :::
 
 1. Run the following command in a terminal to execute the query script:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaのクイックスタートドキュメントの簡略化とコードスニペットの更新"
}
```

### Explanation
このコードの差分では、`search-get-started-rag-java.md` ドキュメントが改訂され、220行が削除され、3行が追加されました。主な変更点は、ドキュメント内の依存関係やコードスニペットが簡略化され、より簡潔に提供されるようになったことです。

具体的には、Mavenプロジェクトの設定に関する内容が、元の詳細なXML例から、外部ソースから参照される形式に変更されました。これにより、ユーザーは長いコードをそのまま読み込む必要がなく、提供されたコマンドで直接取得できるようになり、作業の手間が省けます。

また、クエリスクリプトの設定に関するセクションも更新され、環境変数を使用したクライアントの取得が強調されています。具体的なスクリプト例も外部ファイルからの参照に置き換えられ、ドキュメント全体の可読性と理解しやすさが向上しています。

全体として、これらの変更は、ユーザーが必要な情報をよりスムーズに取得できるように配慮されており、ページの重さを軽減しつつ実用的な情報を保持しています。新しい形式により、ユーザーは簡単にクイックスタートを始められるでしょう。

## articles/search/includes/quickstarts/search-get-started-vector-java.md{#item-a3db97}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaのベクトル検索クイックスタートドキュメントの更新"
}
```

### Explanation
このコードの差分では、`search-get-started-vector-java.md` というドキュメントが改訂され、992行が削除され、21行が追加されました。主な変更点は、ドキュメントの内容が大幅に簡素化され、重要な情報がよりわかりやすく整理されたことです。

具体的には、多くの冗長なテキストやコードサンプルが削除され、ドキュメントが軽量化されました。新たに追加された内容は、主に重要な手順や概念を強調するものであり、ユーザーが迅速に理解できるよう配慮されています。このように更新することで、ユーザーはベクトル検索のクイックスタートを行う際に必要な情報を迅速に得られるようになります。

さらに、具体的なコードや設定の箇所が見やすく整理され、実際の開発を始めるためのハードルが低くなっています。全体として、これらの修正は、ユーザーの利便性を高め、効率的なスタートをサポートすることを目的としています。

## articles/search/includes/quickstarts/search-get-started-vector-javascript.md{#item-d0387c}

<details>
<summary>Diff</summary>
````diff
@@ -428,7 +428,7 @@ This search uses [SearchClient](/javascript/api/@azure/search-documents/searchcl
 
 ## Create a semantic hybrid search
 
-Here's the last query in the collection to create extend the semantic hybrid search with the additional search text `historic hotel walk to restaurants and shopping`.
+Here's the last query in the collection to extend the semantic hybrid search with the additional search text `historic hotel walk to restaurants and shopping`.
 
 This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptのベクトル検索クイックスタート文書の軽微な修正"
}
```

### Explanation
このコードの差分では、`search-get-started-vector-javascript.md` ドキュメントが改訂され、1行が追加され、1行が削除されました。この修正は、文書内の文の表現を若干調整したもので、具体的には、セマンティックハイブリッド検索に関連するクエリの説明において、言葉の順序が変更されました。

変更前の文は「create extend the semantic hybrid search」となっていましたが、これが「extend the semantic hybrid search」と修正されることで、より自然な表現となり、読みやすさが向上しています。このようなマイナーな修正は、ユーザーが理解しやすい文書を作成するために重要であり、全体的な文書の品質向上につながります。

この更新によって、ユーザーはセマンティックハイブリッド検索の使用方法を明確に把握できるようになります。

## articles/search/includes/quickstarts/search-get-started-vector-typescript.md{#item-9b3bc8}

<details>
<summary>Diff</summary>
````diff
@@ -19,6 +19,7 @@ In Azure AI Search, a [vector store](../../vector-store.md) has an index schema
 - An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
 - An Azure AI Search service. [Create a service](../../search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch) in your current subscription.
+    - The `Search Index Data Contributor` role assigned at the scope of the service.
     - You can use a free search service for most of this quickstart, but we recommend the Basic tier or higher for larger data files.
     - To run the query example that invokes [semantic reranking](../../semantic-search-overview.md), your search service must be at the Basic tier or higher with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
 
@@ -455,15 +456,15 @@ This search uses [SearchClient](/javascript/api/@azure/search-documents/searchcl
            "@search.score": 0.8133763,
            "HotelId": "3",
            "HotelName": "Gastronomic Landscape Hotel",
-           "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
+           "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel's restaurant services.",
            "Category": "Resort and Spa"
        }
    ]
    ```
 
 ## Create a semantic hybrid search
 
-Here's the last query in the collection to create extend the semantic hybrid search with the additional search text `historic hotel walk to restaurants and shopping`.
+Here's the last query in the collection to extend the semantic hybrid search with the additional search text `historic hotel walk to restaurants and shopping`.
 
 This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
 
@@ -518,7 +519,7 @@ This search uses [SearchClient](/javascript/api/@azure/search-documents/searchcl
       Re-ranker Score: 2.0582215785980225
       HotelId: 3
       HotelName: Gastronomic Landscape Hotel
-      Description: The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.
+      Description: The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel's restaurant services.
       Category: Suite
     ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptのベクトル検索クイックスタート文書の修正"
}
```

### Explanation
このコードの差分では、`search-get-started-vector-typescript.md` ドキュメントが改訂され、4行が追加され、3行が削除されました。主な変更は、ドキュメント内の要件セクションに新しい情報が追加されたことと、いくつかの表現が微調整された点です。

具体的には、検索サービスのスコープに対して`Search Index Data Contributor` ロールが必要であることが明示的に示されました。これは、ユーザーが検索インデックスにデータを追加するための適切な権限を持つことを確認するための重要な情報です。

さらに、データの説明部分において、いくつかの表現が修正されています。特に、アポストロフィの使用が統一され、「Hotel’s」が「Hotel's」となるなど、細かい表記の修正が行われています。また、文の流れも自然になるよう調整され、全体としての読みやすさが向上しました。

これらの修正は、ユーザーがクイックスタートを実行する際の理解を深めるために役立ち、正確な情報提供に寄与しています。

## articles/search/includes/quickstarts/semantic-ranker-java.md{#item-93a05a}

<details>
<summary>Diff</summary>
````diff
@@ -30,37 +30,7 @@ The quickstart assumes the following is available on your computer:
 
 1. Create a `pom.xml` file with required dependencies.
 
-   ```xml
-   <project xmlns="http://maven.apache.org/POM/4.0.0"
-            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
-            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
-            http://maven.apache.org/xsd/maven-4.0.0.xsd">
-       <modelVersion>4.0.0</modelVersion>
-   
-       <groupId>com.azure.search</groupId>
-       <artifactId>semantic-ranking-quickstart</artifactId>
-       <version>1.0-SNAPSHOT</version>
-   
-       <properties>
-           <maven.compiler.source>21</maven.compiler.source>
-           <maven.compiler.target>21</maven.compiler.target>
-           <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
-       </properties>
-   
-       <dependencies>
-           <dependency>
-               <groupId>com.azure</groupId>
-               <artifactId>azure-search-documents</artifactId>
-               <version>11.7.8</version>
-           </dependency>
-           <dependency>
-               <groupId>com.azure</groupId>
-               <artifactId>azure-identity</artifactId>
-               <version>1.17.0</version>
-           </dependency>
-       </dependencies>
-   </project>
-   ```
+   :::code language="xml" source="~/azure-search-java-samples/semantic-ranking-quickstart/pom.xml" :::
 
 1. Compile the project to resolve the dependencies:
 
@@ -91,104 +61,15 @@ If you signed in to the [Azure portal](https://portal.azure.com), you're signed
 
 Create a file in `src/main/java/com/azure/search/quickstart` called `SearchConfig.java` to read the properties file and hold the configuration values and authentication credential.
 
-```java
-package com.azure.search.quickstart;
-
-import com.azure.identity.DefaultAzureCredential;
-import com.azure.identity.DefaultAzureCredentialBuilder;
-
-import java.io.IOException;
-import java.io.InputStream;
-import java.util.Properties;
-
-public class SearchConfig {
-    private static final Properties properties = new Properties();
-
-    static {
-        try (InputStream input = SearchConfig.class.getClassLoader()
-            .getResourceAsStream("application.properties")) {
-            properties.load(input);
-        } catch (IOException e) {
-            throw new RuntimeException(
-                "Failed to load application.properties", e);
-        }
-    }
-
-    public static final String SEARCH_ENDPOINT =
-        properties.getProperty("azure.search.endpoint");
-    public static final String INDEX_NAME =
-        properties.getProperty("azure.search.index.name");
-    public static final String SEMANTIC_CONFIG_NAME =
-        properties.getProperty("semantic.configuration.name");
-
-    public static final DefaultAzureCredential CREDENTIAL =
-        new DefaultAzureCredentialBuilder().build();
-
-    static {
-        System.out.println("Using Azure Search endpoint: " + SEARCH_ENDPOINT);
-        System.out.println("Using index name: " + INDEX_NAME + "\n");
-    }
-}
-```
+:::code language="java" source="~/azure-search-java-samples/semantic-ranking-quickstart/src/main/java/com/azure/search/quickstart/SearchConfig.java" :::
 
 ## Get the index schema
 
 In this section, you get settings for the existing `hotels-sample-index` index on your search service.
 
 1. Create a file in `src/main/java/com/azure/search/quickstart` called `GetIndexSettings.java`.
 
-    ```java
-    package com.azure.search.quickstart;
-    
-    import com.azure.search.documents.indexes.SearchIndexClientBuilder;
-    import com.azure.search.documents.indexes.models.SearchField;
-    import com.azure.search.documents.indexes.models.SearchIndex;
-    import com.azure.search.documents.indexes.models.SemanticConfiguration;
-    import com.azure.search.documents.indexes.models.SemanticField;
-    import com.azure.search.documents.indexes.models.SemanticSearch;
-    
-    public class GetIndexSettings {
-        public static void main(String[] args) {
-            var indexClient = new SearchIndexClientBuilder()
-                .endpoint(SearchConfig.SEARCH_ENDPOINT)
-                .credential(SearchConfig.CREDENTIAL)
-                .buildClient();
-    
-            System.out.println("Getting semantic search index settings...");
-    
-            SearchIndex index = indexClient.getIndex(SearchConfig.INDEX_NAME);
-    
-            System.out.println("Index name: " + index.getName());
-            System.out.println("Number of fields: " + index.getFields().size());
-    
-            for (SearchField field : index.getFields()) {
-                System.out.printf("Field: %s, Type: %s, Searchable: %s%n",
-                    field.getName(), field.getType(), field.isSearchable());
-            }
-    
-            SemanticSearch semanticSearch = index.getSemanticSearch();
-            if (semanticSearch != null &&
-                semanticSearch.getConfigurations() != null) {
-                System.out.println("Semantic search configurations: " +
-                    semanticSearch.getConfigurations().size());
-                for (SemanticConfiguration config :
-                    semanticSearch.getConfigurations()) {
-                    System.out.println("Configuration name: " + config.getName());
-                    SemanticField titleField = config.getPrioritizedFields().getTitleField();
-                    if (titleField != null) {
-                        System.out.println("Title field: " +
-                            titleField.getFieldName());
-                    }
-                }
-            } else {
-                System.out.println(
-                    "No semantic configuration exists for this index.");
-            }
-    
-            System.exit(0);
-        }
-    }
-    ```
+   :::code language="java" source="~/azure-search-java-samples/semantic-ranking-quickstart/src/main/java/com/azure/search/quickstart/GetIndexSettings.java" :::
 
 1. Compile and run the code:
 
@@ -202,114 +83,7 @@ In this section, you get settings for the existing `hotels-sample-index` index o
 
 1. Create a file in `src/main/java/com/azure/search/quickstart` called `UpdateIndexSettings.java` to add a semantic configuration to the existing `hotels-sample-index` index on your search service.
 
-    ```java
-    package com.azure.search.quickstart;
-    
-    import com.azure.search.documents.indexes.SearchIndexClientBuilder;
-    import com.azure.search.documents.indexes.models.SearchIndex;
-    import com.azure.search.documents.indexes.models.SemanticConfiguration;
-    import com.azure.search.documents.indexes.models.SemanticField;
-    import com.azure.search.documents.indexes.models.SemanticPrioritizedFields;
-    import com.azure.search.documents.indexes.models.SemanticSearch;
-    
-    import java.util.ArrayList;
-    import java.util.List;
-    
-    public class UpdateIndexSettings {
-        public static void main(String[] args) {
-            try {
-                var indexClient = new SearchIndexClientBuilder()
-                    .endpoint(SearchConfig.SEARCH_ENDPOINT)
-                    .credential(SearchConfig.CREDENTIAL)
-                    .buildClient();
-    
-                SearchIndex existingIndex =
-                    indexClient.getIndex(SearchConfig.INDEX_NAME);
-    
-                // Create prioritized fields for semantic configuration
-                var prioritizedFields = new SemanticPrioritizedFields()
-                    .setTitleField(new SemanticField("HotelName"))
-                    .setKeywordsFields(List.of(new SemanticField("Tags")))
-                    .setContentFields(List.of(new SemanticField("Description")));
-    
-                var newSemanticConfiguration = new SemanticConfiguration(
-                    SearchConfig.SEMANTIC_CONFIG_NAME, prioritizedFields);
-    
-                // Add the semantic configuration to the index
-                SemanticSearch semanticSearch = existingIndex.getSemanticSearch();
-                if (semanticSearch == null) {
-                    semanticSearch = new SemanticSearch();
-                    existingIndex.setSemanticSearch(semanticSearch);
-                }
-    
-                List<SemanticConfiguration> configurations =
-                    semanticSearch.getConfigurations();
-                if (configurations == null) {
-                    configurations = new ArrayList<>();
-                    semanticSearch.setConfigurations(configurations);
-                }
-    
-                // Check if configuration already exists
-                boolean configExists = configurations.stream()
-                    .anyMatch(config -> SearchConfig.SEMANTIC_CONFIG_NAME
-                        .equals(config.getName()));
-    
-                if (!configExists) {
-                    configurations.add(newSemanticConfiguration);
-                }
-    
-                indexClient.createOrUpdateIndex(existingIndex);
-    
-                SearchIndex updatedIndex =
-                    indexClient.getIndex(SearchConfig.INDEX_NAME);
-    
-                System.out.println("Semantic configurations:");
-                System.out.println("-".repeat(40));
-    
-                SemanticSearch updatedSemanticSearch =
-                    updatedIndex.getSemanticSearch();
-                if (updatedSemanticSearch != null &&
-                    updatedSemanticSearch.getConfigurations() != null) {
-                    for (SemanticConfiguration config :
-                        updatedSemanticSearch.getConfigurations()) {
-                        System.out.println("Configuration name: " + config.getName());
-    
-                        SemanticPrioritizedFields fields =
-                            config.getPrioritizedFields();
-                        if (fields.getTitleField() != null) {
-                            System.out.println("Title field: " +
-                                fields.getTitleField().getFieldName());
-                        }
-                        if (fields.getKeywordsFields() != null) {
-                            List<String> keywords = fields.getKeywordsFields().stream()
-                                .map(SemanticField::getFieldName)
-                                .toList();
-                            System.out.println("Keywords fields: " +
-                                String.join(", ", keywords));
-                        }
-                        if (fields.getContentFields() != null) {
-                            List<String> content = fields.getContentFields().stream()
-                                .map(SemanticField::getFieldName)
-                                .toList();
-                            System.out.println("Content fields: " +
-                                String.join(", ", content));
-                        }
-                        System.out.println("-".repeat(40));
-                    }
-                } else {
-                    System.out.println("No semantic configurations found.");
-                }
-    
-                System.out.println("Semantic configuration updated successfully.");
-    
-                System.exit(0);
-            } catch (Exception e) {
-                System.err.println("Error updating semantic configuration: " +
-                    e.getMessage());
-            }
-        }
-    }
-    ```
+   :::code language="java" source="~/azure-search-java-samples/semantic-ranking-quickstart/src/main/java/com/azure/search/quickstart/UpdateIndexSettings.java" :::
 
 1. Run the code.
 
@@ -325,52 +99,7 @@ Once the `hotels-sample-index` index has a semantic configuration, you can run q
 
 1. Create a file in `src/main/java/com/azure/search/quickstart` called `SemanticQuery.java` to create a semantic query of the index.
 
-    ```java
-    package com.azure.search.quickstart;
-    
-    import com.azure.search.documents.SearchClientBuilder;
-    import com.azure.search.documents.SearchDocument;
-    import com.azure.search.documents.models.QueryType;
-    import com.azure.search.documents.models.SearchOptions;
-    import com.azure.search.documents.models.SearchResult;
-    import com.azure.search.documents.models.SemanticSearchOptions;
-    import com.azure.search.documents.util.SearchPagedIterable;
-    
-    public class SemanticQuery {
-        public static void main(String[] args) {
-            var searchClient = new SearchClientBuilder()
-                .endpoint(SearchConfig.SEARCH_ENDPOINT)
-                .indexName(SearchConfig.INDEX_NAME)
-                .credential(SearchConfig.CREDENTIAL)
-                .buildClient();
-    
-            var searchOptions = new SearchOptions()
-                .setQueryType(QueryType.SEMANTIC)
-                .setSemanticSearchOptions(new SemanticSearchOptions()
-                    .setSemanticConfigurationName(SearchConfig.SEMANTIC_CONFIG_NAME))
-                .setSelect("HotelId", "HotelName", "Description");
-    
-            SearchPagedIterable results = searchClient.search(
-                "walking distance to live music", searchOptions, null);
-    
-            int rowNumber = 1;
-            for (SearchResult result : results) {
-                var document = result.getDocument(SearchDocument.class);
-                double rerankerScore = result.getSemanticSearch().getRerankerScore();
-    
-                System.out.printf("Search result #%d:%n", rowNumber++);
-                System.out.printf("  Re-ranker Score: %.2f%n", rerankerScore);
-                System.out.printf("  HotelId: %s%n", document.get("HotelId"));
-                System.out.printf("  HotelName: %s%n", document.get("HotelName"));
-                System.out.printf("  Description: %s%n%n",
-                    document.get("Description") != null ?
-                        document.get("Description") : "N/A");
-            }
-    
-            System.exit(0);
-        }
-    }
-    ```
+   :::code language="java" source="~/azure-search-java-samples/semantic-ranking-quickstart/src/main/java/com/azure/search/quickstart/SemanticQuery.java" :::
 
 1. Run the code.
 
@@ -386,87 +115,7 @@ Optionally, you can add captions to extract portions of the text and apply hit h
 
 1. Create a file in `src/main/java/com/azure/search/quickstart` called `SemanticQueryWithCaptions.java`.
 
-    ```java
-    package com.azure.search.quickstart;
-    
-    import com.azure.search.documents.SearchClientBuilder;
-    import com.azure.search.documents.SearchDocument;
-    import com.azure.search.documents.models.QueryCaption;
-    import com.azure.search.documents.models.QueryCaptionResult;
-    import com.azure.search.documents.models.QueryCaptionType;
-    import com.azure.search.documents.models.QueryType;
-    import com.azure.search.documents.models.SearchOptions;
-    import com.azure.search.documents.models.SearchResult;
-    import com.azure.search.documents.models.SemanticSearchOptions;
-    import com.azure.search.documents.util.SearchPagedIterable;
-
-    import java.util.List;
-    
-    public class SemanticQueryWithCaptions {
-        public static void main(String[] args) {
-            var searchClient = new SearchClientBuilder()
-                .endpoint(SearchConfig.SEARCH_ENDPOINT)
-                .indexName(SearchConfig.INDEX_NAME)
-                .credential(SearchConfig.CREDENTIAL)
-                .buildClient();
-    
-            System.out.println("Using semantic configuration: " +
-                SearchConfig.SEMANTIC_CONFIG_NAME);
-            System.out.println("Search query: walking distance to live music");
-    
-            var searchOptions = new SearchOptions()
-                .setQueryType(QueryType.SEMANTIC)
-                .setSemanticSearchOptions(new SemanticSearchOptions()
-                    .setSemanticConfigurationName(SearchConfig.SEMANTIC_CONFIG_NAME)
-                    .setQueryCaption(new QueryCaption(QueryCaptionType.EXTRACTIVE)
-                        .setHighlightEnabled(true)))
-                .setSelect("HotelId", "HotelName", "Description");
-    
-            SearchPagedIterable results = searchClient.search(
-                "walking distance to live music", searchOptions, null);
-    
-            System.out.printf("Found results with semantic search%n%n");
-            int rowNumber = 1;
-    
-            for (SearchResult result : results) {
-                var document = result.getDocument(SearchDocument.class);
-                double rerankerScore = result.getSemanticSearch().getRerankerScore();
-    
-                System.out.printf("Search result #%d:%n", rowNumber++);
-                System.out.printf("  Re-ranker Score: %.2f%n", rerankerScore);
-                System.out.printf("  HotelName: %s%n", document.get("HotelName"));
-                System.out.printf("  Description: %s%n%n",
-                    document.get("Description") != null ?
-                        document.get("Description") : "N/A");
-    
-                // Handle captions
-                List<QueryCaptionResult> captions =
-                    result.getSemanticSearch().getQueryCaptions();
-                if (captions != null && !captions.isEmpty()) {
-                    QueryCaptionResult caption = captions.get(0);
-    
-                    if (caption.getHighlights() != null &&
-                        !caption.getHighlights().trim().isEmpty()) {
-                        System.out.printf("  Caption with highlights: %s%n",
-                            caption.getHighlights());
-                    } else if (caption.getText() != null &&
-                        !caption.getText().trim().isEmpty()) {
-                        System.out.printf("  Caption text: %s%n",
-                            caption.getText());
-                    } else {
-                        System.out.println(
-                            "  Caption exists but has no text or highlights content");
-                    }
-                } else {
-                    System.out.println("  No captions found for this result");
-                }
-                System.out.println("-".repeat(60));
-            }
-    
-            System.exit(0);
-        }
-    }
-    ```
+   :::code language="java" source="~/azure-search-java-samples/semantic-ranking-quickstart/src/main/java/com/azure/search/quickstart/SemanticQueryWithCaptions.java" :::
 
 1. Run the code.
 
@@ -495,104 +144,7 @@ To produce a semantic answer, the question and answer must be closely aligned, a
 
 1. Create a file in `src/main/java/com/azure/search/quickstart` called `SemanticAnswer.java`.
 
-    ```java
-    package com.azure.search.quickstart;
-    
-    import com.azure.search.documents.SearchClientBuilder;
-    import com.azure.search.documents.SearchDocument;
-    import com.azure.search.documents.models.QueryAnswer;
-    import com.azure.search.documents.models.QueryAnswerResult;
-    import com.azure.search.documents.models.QueryAnswerType;
-    import com.azure.search.documents.models.QueryCaption;
-    import com.azure.search.documents.models.QueryCaptionResult;
-    import com.azure.search.documents.models.QueryCaptionType;
-    import com.azure.search.documents.models.QueryType;
-    import com.azure.search.documents.models.SearchOptions;
-    import com.azure.search.documents.models.SearchResult;
-    import com.azure.search.documents.models.SemanticSearchOptions;
-    import com.azure.search.documents.util.SearchPagedIterable;
-    
-    import java.util.List;
-    
-    public class SemanticAnswer {
-        public static void main(String[] args) {
-            var searchClient = new SearchClientBuilder()
-                .endpoint(SearchConfig.SEARCH_ENDPOINT)
-                .indexName(SearchConfig.INDEX_NAME)
-                .credential(SearchConfig.CREDENTIAL)
-                .buildClient();
-    
-            var searchOptions = new SearchOptions()
-                .setQueryType(QueryType.SEMANTIC)
-                .setSemanticSearchOptions(new SemanticSearchOptions()
-                    .setSemanticConfigurationName(SearchConfig.SEMANTIC_CONFIG_NAME)
-                    .setQueryCaption(new QueryCaption(QueryCaptionType.EXTRACTIVE))
-                    .setQueryAnswer(new QueryAnswer(QueryAnswerType.EXTRACTIVE)))
-                .setSelect("HotelName", "Description", "Category");
-    
-            SearchPagedIterable results = searchClient.search(
-                "What's a good hotel for people who like to read",
-                searchOptions, null);
-    
-            System.out.println("Answers:\n");
-    
-            // Extract semantic answers
-            List<QueryAnswerResult> semanticAnswers =
-                results.getSemanticResults().getQueryAnswers();
-            int answerNumber = 1;
-    
-            if (semanticAnswers != null) {
-                for (QueryAnswerResult answer : semanticAnswers) {
-                    System.out.printf("Semantic answer result #%d:%n",
-                        answerNumber++);
-    
-                    if (answer.getHighlights() != null &&
-                        !answer.getHighlights().trim().isEmpty()) {
-                        System.out.printf("Semantic Answer: %s%n",
-                            answer.getHighlights());
-                    } else {
-                        System.out.printf("Semantic Answer: %s%n", answer.getText());
-                    }
-                    System.out.printf("Semantic Answer Score: %.2f%n%n",
-                        answer.getScore());
-                }
-            }
-    
-            System.out.println("Search Results:\n");
-            int rowNumber = 1;
-    
-            // Iterate through search results
-            for (SearchResult result : results) {
-                var document = result.getDocument(SearchDocument.class);
-                double rerankerScore = result.getSemanticSearch().getRerankerScore();
-    
-                System.out.printf("Search result #%d:%n", rowNumber++);
-                System.out.printf("Re-ranker Score: %.2f%n", rerankerScore);
-                System.out.printf("Hotel: %s%n", document.get("HotelName"));
-                System.out.printf("Description: %s%n",
-                    document.get("Description") != null ?
-                        document.get("Description") : "N/A");
-    
-                List<QueryCaptionResult> captions =
-                    result.getSemanticSearch().getQueryCaptions();
-                if (captions != null && !captions.isEmpty()) {
-                    QueryCaptionResult caption = captions.get(0);
-                    if (caption.getHighlights() != null &&
-                        !caption.getHighlights().trim().isEmpty()) {
-                        System.out.printf("Caption: %s%n%n",
-                            caption.getHighlights());
-                    } else {
-                        System.out.printf("Caption: %s%n%n", caption.getText());
-                    }
-                } else {
-                    System.out.println();
-                }
-            }
-    
-            System.exit(0);
-        }
-    }
-    ```
+   :::code language="java" source="~/azure-search-java-samples/semantic-ranking-quickstart/src/main/java/com/azure/search/quickstart/SemanticAnswer.java" :::
 
 1. Run the code.
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Javaのセマンティックランカーに関するクイックスタート文書の全面改訂"
}
```

### Explanation
このコードの差分では、`semantic-ranker-java.md` ドキュメントが大幅に改訂され、455行が削除され、7行が追加されました。この変更により、ドキュメントの内容と構成がすべて新しくなり、より効率的な方法でセマンティックランカーの使用方法が説明されています。

主な変更点は以下の通りです：

1. **コードスニペットの移動**: これまでの大部分のJavaコードが、ドキュメントから削除され、新しい形式で参照されるようになりました。具体的には、コードスニペットは直接表示されるのではなく、外部のリソースファイルから読み込まれる形になっています。これにより、ドキュメントの清潔さとシンプルさが向上し、可読性が増しました。

2. **構造の見直し**: 新しいセマンティック検索の使用手順がより論理的な流れで配置され、ユーザーが手順を追いやすくなっています。

3. **更新された依存関係**: 依存関係や設定に関する情報が簡潔に整理され、新しい設定方法や構成項目が明確に示されています。

4. **ターゲット言語の強調**: モダンなコーディングスタイルの採用や、コードのリファレンス方式の変更により、ユーザーに対するより良い指導が可能になっています。

このように、ドキュメントは構造的にも内容的にも刷新されており、特に新しいユーザーにとってより直感的で実用的なものとなっています。全体的に見て、これらの変更は利用者にとっての学習効果を高めるために設計されています。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -42,7 +42,7 @@ The wizard [supports a wide range of Azure data sources](search-import-data-port
 
 ### Supported embedding models
 
-For integrated vectorization, you must use one of the following embedding models. Deployment instructions are provided in a [later section](#prepare-embedding-model).
+For integrated vectorization, use one of the following embedding models. Deployment instructions are provided in a [later section](#prepare-embedding-model).
 
 | Provider | Supported models |
 |--|--|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクターインポートガイドの文言修正"
}
```

### Explanation
このコードの差分では、`search-get-started-portal-import-vectors.md`ドキュメントがわずかに修正され、1行が追加され、1行が削除されました。具体的には、ベクター化に関する説明文が改善されています。

変更内容は以下の通りです：

- 文言が「For integrated vectorization, you must use one of the following embedding models.」から「For integrated vectorization, use one of the following embedding models.」へと修正されました。この変更により、文がより直接的かつ親しみやすくなり、強制的なニュアンスから、推奨する形に変わっています。

この修正は、ユーザーがベクター化の際に必要となる埋め込みモデルを理解しやすくするために行われており、全体的な文書のトーンを改善しています。これにより、読者が導入手順をよりスムーズに進められることを意図しています。

## articles/search/search-how-to-integrated-vectorization.md{#item-86fb1e}

<details>
<summary>Diff</summary>
````diff
@@ -42,7 +42,7 @@ Integrated vectorization works with [all supported data sources](search-indexer-
 
 ### Supported embedding models
 
-For integrated vectorization, you must use one of the following embedding models on an Azure AI platform. Deployment instructions are provided in a [later section](#prepare-your-embedding-model).
+For integrated vectorization, use one of the following embedding models on an Azure AI platform. Deployment instructions are provided in a [later section](#prepare-your-embedding-model).
 
 | Provider | Supported models |
 |--|--|
@@ -52,9 +52,11 @@ For integrated vectorization, you must use one of the following embedding models
 
 <sup>1</sup> The endpoint of your Azure OpenAI resource must have a [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains), such as `https://my-unique-name.openai.azure.com`. If you created your resource in the [Azure portal](https://portal.azure.com/), this subdomain was automatically generated during resource setup.
 
-<sup>2</sup> For billing purposes, you must [attach your Azure AI multi-service resource](cognitive-search-attach-cognitive-services.md) to the skillset in your Azure AI Search service. Unless you use a [keyless connection (preview)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) to create the skillset, both resources must be in the same region.
+<sup>2</sup> Azure OpenAI resources (with access to embedding models) that were created in the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) aren't supported. You must create an Azure OpenAI resource in the Azure portal.
 
-<sup>3</sup> The Azure AI Vision multimodal embedding model is available in [select regions](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
+<sup>3</sup> For billing purposes, you must [attach your Azure AI multi-service resource](cognitive-search-attach-cognitive-services.md) to the skillset in your Azure AI Search service. Unless you use a [keyless connection (preview)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) to create the skillset, both resources must be in the same region.
+
+<sup>4</sup> The Azure AI Vision multimodal embedding model is available in [select regions](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
 
 ### Role-based access
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "統合ベクター化に関するガイドの文言修正と情報追加"
}
```

### Explanation
このコードの差分では、`search-how-to-integrated-vectorization.md` ドキュメントが修正され、5行が追加され、3行が削除されました。この変更では、統合ベクター化に関連する情報が洗練され、より正確な表現への修正が行われています。

主な変更点は以下の通りです：

1. **文言の変更**: ベクター化の説明が「For integrated vectorization, you must use one of the following embedding models on an Azure AI platform.」から「For integrated vectorization, use one of the following embedding models on an Azure AI platform.」へと修正されました。この修正により、表現が柔らかくなり、ユーザーに対する指示が推奨形式に変更されました。

2. **情報の追加と移動**: 文中のサブスクリプションやリソース作成に関する注意事項の順序が入れ替えられ、新たに情報が追加されました。具体的には、Azure OpenAIリソースがAzure AI Foundryポータルで作成された場合にサポートされないことが強調されています。また、Azure AIマルチサービスリソースとスキルセットの接続要件が強調され、より明確になりました。

3. **脚注の整理**: 脚注番号が変更され、情報が再編成されたことで、関連情報が正確にリンクされ、理解しやすくなっています。

これらの変更により、ユーザーは統合ベクター化の設定と要件についてより明確に理解できるようになり、サポート体制も強化されています。全体として、ドキュメントの利用価値が向上しています。

## articles/search/search-security-manage-encryption-keys.md{#item-db3487}

<details>
<summary>Diff</summary>
````diff
@@ -50,7 +50,7 @@ Although you can't add encryption to an existing object, once an object is confi
 
 + [Azure AI Search](search-create-service-portal.md) on a [billable tier](search-sku-tier.md#tier-descriptions) (Basic or higher, in any region).
 
-+ [Azure Key Vault](/azure/key-vault/general/overview) and a key vault with **soft-delete** and **purge protection** enabled. Or, [Azure Key Vault Managed HSM](/azure/key-vault/managed-hsm/overview). This resource can be in any subscription, but it must be in the same tenant as Azure AI Search.
++ [Azure Key Vault](/azure/key-vault/general/overview) and a key vault with **soft-delete** and **purge protection** enabled. Or, [Azure Key Vault Managed HSM](/azure/key-vault/managed-hsm/overview). This resource can be in any subscription and in a different tenant. These instructions assume a single tenant. For cross-tenant configuration, see [Configure customer-managed keys across different tenants](search-security-managed-encryption-cross-tenant.md).
 
 + Ability to set up permissions for key access and to assign roles. To create keys, you must be **Key Vault Crypto Officer** in Azure Key Vault or **Managed HSM Crypto Officer** in Azure Key Vault Managed HSM.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "暗号化キー管理に関するガイドの文言修正と情報追加"
}
```

### Explanation
このコードの差分では、`search-security-manage-encryption-keys.md` ドキュメントが修正され、1行が追加され、1行が削除されました。この変更は、暗号化キー管理に関する情報を強化し、より明確な指示を提供することを目的としています。

主な変更点は以下の通りです：

1. **文言の変更**: Azure Key Vault に関する説明で、リソースが「同じテナント内にある必要がある」という条件が「異なるテナントに存在できる」という具体的な情報へと修正されました。この変更により、ユーザーは異なるサブスクリプションやテナント間での構成に関する柔軟性が理解しやすくなっています。

2. **追加情報の挿入**: 「これらの指示は単一テナントを前提としています。クロステナント構成については、[異なるテナント間での顧客管理キーの構成](search-security-managed-encryption-cross-tenant.md)を参照してください。」という文が追加され、異なるテナント間での操作方法についての指針をユーザーに提供しています。これにより、複雑なシナリオに対する理解を深めることができます。

3. **権限設定と役割についての確認**: キーアクセスの設定権限と役割の割り当てに関する能力が強調され、キーを作成するために必要な役割（「Key Vault Crypto Officer」または「Managed HSM Crypto Officer」）についても明記されています。

これらの変更は、ドキュメントの明確さと有用性を向上させ、ユーザーが暗号化キーを安全に管理できるようにサポートしています。全体として、コンテンツがよりアクセスしやすく、役立つ情報が増加しています。

## articles/search/search-security-managed-encryption-cross-tenant.md{#item-efc726}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,126 @@
+---
+title: Cross-tenant CMKs
+titleSuffix: Azure AI Search
+description: Set up CMK encryption in Azure AI Search that uses a key from an Azure Key Vault in another tenant.
+manager: vinodva
+author: mattgotteiner
+ms.author: magottei
+ms.service: azure-ai-search
+ms.topic: how-to
+ms.date: 10/13/2025
+ms.update-cycle: 180-days
+---
+
+# Configure customer-managed keys across different tenants
+
+When Azure Key Vault and Azure AI Search are in different Azure tenants, use a Microsoft Entra multitenant app to enable [customer-managed key (CMK) encryption](search-security-manage-encryption-keys.md) using a key from another tenant.
+
+## Prerequisites 
+
++ A tenant containing the search service that has content you want to encrypt. Azure AI Search must be [configured for role-based access](search-security-enable-roles.md). Support for CMK requires Basic pricing tier or higher.
+
++ A separate tenant having the Azure Key Vault and the encryption keys you want to use. Azure Key Vault must be [configured for role-based access](/azure/key-vault/general/rbac-guide).
+
++ Azure CLI for sending requests.
+
+## Create a multitenant Microsoft Entra application in tenant A
+
+Use the Azure CLI to send requests. We refer to the tenant containing Azure AI Search as *tenant A*.
+
+1. Get the tenant ID:
+
+   `az account show --query tenantId --output tsv`
+
+1. Make sure you're signed in to tenant A:
+
+   `az login --tenant <tenant-A-id> `
+
+1. Create the application registration:
+
+   `az ad app create --display-name cross-tenant-auth --sign-in-audience AzureADMultipleOrgs `
+
+1. Save the app ID output from this step.
+
+## Add a client secret to the multitenant application
+
+1. To add the client secret to the multitenant application in tenant A, run the following command:
+
+   `az ad app credential reset --id <multitenant-app-id>`
+
+1. Save the password output from this step. The password output is a required input for [setting up CMK](search-security-manage-encryption-keys.md) in Azure AI Search.
+
+1. To specify when the client secret expires, you can specify an end-date parameter to this command.
+
+   `az ad app credential reset --id <multitenant-app-id> --end-date <end-date>`
+
+   The end-date parameter accepts a date in ISO 8601 format. For example: `az ad app credential reset --id <multitenant-app-id> --end-date 2026-12-31`.
+
+## Create a service principal in tenant B for the multitenant application
+
+We refer to the tenant containing Azure Key Vault as *tenant B*. In tenant B, create a service principal for the multitenant application in tenant A.
+
+1. Sign in to tenant B:
+
+   `az login --tenant <tenant-B-id>`
+
+1. Create the service principal using the multitenant app ID output from the first step:
+
+   `az ad sp create --id <multitenant-app-id>` 
+
+   This service principal is an instance of the multitenant application in tenant A. Roles assigned to this service principal in tenant B are also assigned to the multitenant application in tenant A.
+
+1. Verify the link between tenant A and B by reviewing the "appOwnerOrganizationId" in the following command:
+
+   `az ad sp show --id <multitenant-app-id>`
+
+   This command displays the service principal details in JSON. Look for the "appOwnerOrganizationId" field in the output to confirm it matches tenant A's ID.
+
+1. Save the object ID of the service principal (from the `"id"` field) from this step. The object ID is a required input for setting up CMK in Azure AI Search.
+
+1. Get the resource ID for Azure Key Vault:
+
+   `az keyvault show --name <key-vault-name> --query id --output tsv`
+
+1. Assign the **Key Vault Crypto Service Encryption User** role on the key vault in tenant B to the new service principal.
+
+   `az role assignment create --assignee <service-principal-object-id> --role "Key Vault Crypto Service Encryption User" --scope <key-vault-resource-id>`
+
+   An example of this assignment might look like this:
+
+   `az role assignment create --assignee 12345678-1234-1234-1234-123456789012 --role "Key Vault Crypto Service Encryption User" --scope /subscriptions/87654321-4321-4321-4321-210987654321/resourceGroups/myKeyVaultRG/providers/Microsoft.KeyVault/vaults/myCompanyKeyVault`
+
+## Test encryption
+
+Create a test index in the search service (tenant A) to validate the setup. Use the multitenant app ID and the credentials you added in the "access credentials" object to authenticate to the key vault in the other tenant. 
+
+You can use this sample index schema for testing. You can use the Azure portal to add an index and provide this JSON, or use a [REST client](search-get-started-text.md) to send a Create Index request.
+
+```json
+{
+  "name": "cross-tenant-cmk-test", 
+  "fields": [ 
+        { 
+            "name": "id", 
+            "type": "Edm.String", 
+            "key": true 
+        } 
+      ], 
+  "encryptionKey": { 
+    "keyVaultUri": "https://myCompanyKeyVault.vault.azure.net/", 
+    "keyVaultKeyName": "search-encryption-key", 
+    "keyVaultKeyVersion": "abc123def456ghi789", 
+    "accessCredentials": { 
+      "applicationId": "12345678-1234-1234-1234-123456789012", 
+      "applicationSecret": "secretValueFromStep2" 
+    } 
+  } 
+}
+```
+
+Verify the index was created successfully:
+
+```http
+GET https://<search-service>.search.windows.net/indexes/cross-tenant-cmk-test?api-version=2025-09-01
+```
+
+For more information about how to rotate or manage keys, see [Configure customer-managed keys for data encryption](search-security-manage-encryption-keys.md).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "異なるテナント間での顧客管理キー（CMK）暗号化設定ガイドの追加"
}
```

### Explanation
このコードの差分では、新しく `search-security-managed-encryption-cross-tenant.md` というドキュメントが追加され、126行の内容が含まれています。このガイドは、異なる Azure テナント間での顧客管理キー（CMK）暗号化の設定に関する詳細な手順を提供します。

主な内容は以下の通りです：

1. **ドキュメントの構造と基本情報**: 新しいドキュメントは、タイトル、説明、著者情報、更新サイクルなどのメタデータから始まり、異なるテナント間でのCMK暗号化を行う際の基本的な設定を明確に示しています。

2. **前提条件**: ユーザーが暗号化を行うために必要な準備（役割ベースのアクセス設定や、Azure CLIの使用）が説明されています。

3. **手順の詳細**: 
   - **マルチテナント Microsoft Entra アプリの作成**: Azure CLIを使用して、Azure AI Search を含むテナント（テナント A）でアプリケーションを登録する手順が含まれています。
   - **クライアントシークレットの追加**: マルチテナントアプリにクライアントシークレットを追加する方法が解説されています。
   - **サービスプリンシパルの作成**: Azure Key Vault を含むテナント（テナント B）でサービスプリンシパルを作成し、必要な役割を割り当てる手順が示されています。

4. **暗号化のテスト**: 暗号化設定が正しく行われたかを確認するためのテストインデックスの作成方法と、インデックスが成功裏に作成されたかを検証するためのHTTPリクエストの例が含まれています。

5. **追加情報の提供**: キーのローテーションや管理に関するリンクが提供され、ユーザーがさらなる情報を得やすくなっています。

このドキュメントの追加により、ユーザーは異なるテナント間での暗号化キーの管理をより効果的に設定できるようになります。全体として、Azure AI Search におけるデータのセキュリティが強化され、ユーザーの要求に応じた新たな機能が提供されています。

## articles/search/search-security-overview.md{#item-6b3f1e}

<details>
<summary>Diff</summary>
````diff
@@ -312,7 +312,7 @@ For Azure AI Search, there's currently one built-in definition. It's for resourc
 
 Apply metadata tags to categorize search services based on data sensitivity and compliance requirements. This facilitates proper governance and security controls. For more information, see [Use tags to organize your Azure resources](/azure/azure-resource-manager/management/tag-resources) and [General guidance – Organize Azure resources using tags](/azure/azure-resource-manager/management/tag-resources).
 
-## Learn more
+## Related content
 
 + [Azure security fundamentals](/azure/security/fundamentals/)
 + [Azure Security](https://azure.microsoft.com/overview/security)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セキュリティ概要ドキュメントの見出し変更と関連コンテンツの追加"
}
```

### Explanation
このコードの差分では、`search-security-overview.md` ドキュメントが修正され、1行が追加され、1行が削除されました。この変更は、ドキュメントの構造をエフェクティブにすることを目的としています。

主な変更点は以下の通りです：

1. **見出しの変更**: セクションタイトルが「Learn more」から「Related content」に変更されました。この変更により、関連コンテンツのセクションが明確になり、ユーザーにとって有用な情報が容易に把握できるようになっています。

2. **関連コンテンツの追加**: 新しい情報源として、「Azure security fundamentals」や「Azure Security」に関するリンクが追加されました。これにより、ユーザーはAzureにおけるセキュリティの基本や関連リソースに簡単にアクセスできるようになりました。

これらの変更は、ドキュメントのナビゲーションを改善し、ユーザーがAzure AI Searchのセキュリティに関する関連情報を効果的に取得できるようにしています。全体として、ユーザビリティを向上させるための小さながしかし重要な更新となっています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -563,8 +563,10 @@ items:
           href: search-query-access-control-rbac-enforcement.md
     - name: Data encryption
       items:
-      - name: Customer-managed keys
+      - name: Customer-managed keys (CMK)
         href: search-security-manage-encryption-keys.md
+      - name: Configure cross-tenant CMK
+        href: search-security-managed-encryption-cross-tenant.md
       - name: Find encrypted objects
         href: search-security-get-encryption-keys.md
   - name: Development
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次ファイルの変更: 顧客管理キーの名称変更と新規項目の追加"
}
```

### Explanation
このコードの差分では、`toc.yml` ファイルが修正され、3行が追加され、1行が削除されました。この変更は、ドキュメントの目次に関連する情報を更新し、より明確で便利なナビゲーションを提供することを目的としています。

主な変更点は以下の通りです：

1. **顧客管理キーの名称変更**: 既存の項目「Customer-managed keys」が「Customer-managed keys (CMK)」に変更されました。この変更により、略称が明示され、ユーザーにとって理解しやすくなっています。

2. **新規項目の追加**: 新たに「Configure cross-tenant CMK」という項目が追加され、関連するドキュメントへのリンクが設定されています。この情報は、異なるテナント間での顧客管理キーの設定に関する内容であり、ユーザーがより詳細にアクセスできるようになります。

これらの変更は、ユーザーが必要な情報をより迅速に見つけられるようにし、全体的なユーザビリティを向上させることに寄与しています。目次の整合性が保たれ、新しい情報が効果的に組み込まれたことで、ドキュメント全体のナビゲーションが強化されています。


