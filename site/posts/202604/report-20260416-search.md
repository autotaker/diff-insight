---
date: '2026-04-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:cda15f7...MicrosoftDocs:4e14138
summary: この更新はAzure AI Searchに関する技術文書の大規模な修正を行い、新しい機能の追加と不必要な情報の削除が中心です。具体的には、Blob、OneLake、SharePoint、Webナレッジソースの設定方法が新たに詳細に解説される一方、C#、Python、REST
  APIに関する具体的な実装ドキュメントは削除されました。また、インデックス管理の説明が強化され、FAQやファイアウォール設定に関する情報も修正されました。この変更は、情報の中心を機能概要に移し、開発者への利便性向上を図るものですが、具体的な実装情報が欠落した点については今後の新たなリソース提供が期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:cda15f7...MicrosoftDocs:4e14138){target="_blank"}

<format>
# Highlights
この更新はAzure AI Searchの技術文書における大規模な修正と改訂を行ったもので、特に新機能の追加や文書の整理による削除が中心です。新機能として、Azure BlobやOneLake、SharePoint、Webなどの各種ナレッジソースの作成法が詳細に追加される一方、C#、Python、REST APIによる具体的な実装に関するドキュメントが削除されている点が特徴です。

## New features
- Blob、OneLake、SharePoint、Webナレッジソースの新たな設定方法とその具体例の追加。
- インデックス管理の詳細説明が強化され、操作手順が明確化。

## Breaking changes
- Blob、OneLake、Search Index、SharePoint、Webナレッジソースに関するC#、Python、REST APIの具体的な実装ドキュメントの削除。
- ナレッジベースおよびインデックス管理に関するドキュメントの一部削除。

## Other updates
- FAQやファイアウォール設定に関するリンクと説明の修正。
- インデックス管理に関する情報の拡充と改善。

# Insights
今回のドキュメントの更新は、Azure AI Searchを利用する開発者に対しての情報提供を大幅に見直し、特に利用方法に関するガイドラインを強化した一方で、具体的な実装指針を提供する役割の文書を整理したことです。削除された内容の多くは、特定のプログラミング言語での詳細なコーディング例や実装手順に関するものであり、これによりドキュメント全体の焦点が広範な基礎部分から機能の概要に移動したと考えられます。この進展は、利便性向上と情報の集中化を図る戦略の一環であり、加えて将来的な機能拡張やAPIの変更への迅速な対応をも見据えているのかもしれません。

一方で、具体的な実装情報がなくなった部分については開発者にとっては痛手であるため、Azureは他の形でこれらの情報を補う新たなリソースやサポートを提供するのではないかと期待されます。特にAPIリファレンスやサンプルプログラムの方針は今後注意深く観測する必要があります。今後の展開として、より高レベルの抽象化を施し、柔軟なサービス利用が可能な新開発環境の準備が行われている可能性があります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-blob.md](#item-ac6c8a) | minor update | エージェント知識ソースに関するBlobの作成方法の更新 | modified | 434 | 5 | 439 | 
| [agentic-knowledge-source-how-to-onelake.md](#item-ec7a80) | minor update | インデックス付きOneLake知識ソースの作成方法の更新 | modified | 422 | 5 | 427 | 
| [agentic-knowledge-source-how-to-search-index.md](#item-09d366) | minor update | 検索インデックス知識ソースの作成方法の更新 | modified | 231 | 4 | 235 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed.md](#item-fe72fc) | minor update | インデックス付きSharePoint知識ソースの作成方法の更新 | modified | 408 | 4 | 412 | 
| [agentic-knowledge-source-how-to-sharepoint-remote.md](#item-79d019) | minor update | リモートSharePoint知識ソースの作成方法の更新 | modified | 418 | 4 | 422 | 
| [agentic-knowledge-source-how-to-web.md](#item-6b21d0) | minor update | Web Knowledge Sourceの作成方法の更新 | modified | 249 | 5 | 254 | 
| [agentic-retrieval-how-to-create-knowledge-base.md](#item-7df0e2) | minor update | ナレッジベースの作成方法に関する更新 | modified | 521 | 5 | 526 | 
| [agentic-retrieval-how-to-retrieve.md](#item-d739cf) | minor update | 取り込みパラメータのリンク修正 | modified | 3 | 3 | 6 | 
| [agentic-knowledge-source-how-to-blob-csharp.md](#item-b5f755) | breaking change | Blobナレッジソースに関するC#ドキュメントの削除 | removed | 0 | 208 | 208 | 
| [agentic-knowledge-source-how-to-blob-python.md](#item-029d03) | breaking change | Blobナレッジソースに関するPythonドキュメントの削除 | removed | 0 | 193 | 193 | 
| [agentic-knowledge-source-how-to-blob-rest.md](#item-b5ce57) | breaking change | Blobナレッジソースに関するREST APIドキュメントの削除 | removed | 0 | 181 | 181 | 
| [agentic-knowledge-source-how-to-onelake-csharp.md](#item-d6611c) | breaking change | Indexed OneLakeナレッジソースに関するC#ドキュメントの削除 | removed | 0 | 199 | 199 | 
| [agentic-knowledge-source-how-to-onelake-python.md](#item-c7d61d) | breaking change | Indexed OneLakeナレッジソースに関するPythonドキュメントの削除 | removed | 0 | 188 | 188 | 
| [agentic-knowledge-source-how-to-onelake-rest.md](#item-876f49) | breaking change | Indexed OneLakeナレッジソースに関するREST APIドキュメントの削除 | removed | 0 | 176 | 176 | 
| [agentic-knowledge-source-how-to-search-index-csharp.md](#item-d3510c) | breaking change | Search Indexナレッジソースに関するC#ドキュメントの削除 | removed | 0 | 101 | 101 | 
| [agentic-knowledge-source-how-to-search-index-python.md](#item-58056f) | breaking change | Search Indexナレッジソースに関するPythonドキュメントの削除 | removed | 0 | 105 | 105 | 
| [agentic-knowledge-source-how-to-search-index-rest.md](#item-e95367) | breaking change | Search Indexナレッジソースに関するREST APIドキュメントの削除 | removed | 0 | 98 | 98 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-csharp.md](#item-2eb305) | breaking change | SharePointインデックスに関するC#ドキュメントの削除 | removed | 0 | 193 | 193 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-python.md](#item-923abb) | breaking change | SharePointインデックスに関するPythonドキュメントの削除 | removed | 0 | 182 | 182 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-rest.md](#item-e26ea0) | breaking change | SharePointインデックスに関するREST APIドキュメントの削除 | removed | 0 | 178 | 178 | 
| [agentic-knowledge-source-how-to-sharepoint-remote-csharp.md](#item-f8bed1) | breaking change | リモートSharePointナレッジソースに関するC#ドキュメントの削除 | removed | 0 | 204 | 204 | 
| [agentic-knowledge-source-how-to-sharepoint-remote-python.md](#item-822712) | breaking change | リモートSharePointナレッジソースに関するPythonドキュメントの削除 | removed | 0 | 216 | 216 | 
| [agentic-knowledge-source-how-to-sharepoint-remote-rest.md](#item-5514b1) | breaking change | リモートSharePointナレッジソースに関するREST APIドキュメントの削除 | removed | 0 | 204 | 204 | 
| [agentic-knowledge-source-how-to-web-csharp.md](#item-401063) | breaking change | Webナレッジソースに関するC#ドキュメントの削除 | removed | 0 | 121 | 121 | 
| [agentic-knowledge-source-how-to-web-python.md](#item-72b59c) | breaking change | Webナレッジソースに関するPythonドキュメントの削除 | removed | 0 | 114 | 114 | 
| [agentic-knowledge-source-how-to-web-rest.md](#item-649608) | breaking change | Webナレッジソースに関するRESTドキュメントの削除 | removed | 0 | 110 | 110 | 
| [agentic-retrieval-how-to-create-knowledge-base-csharp.md](#item-4469a2) | breaking change | C#によるナレッジベースの作成に関するドキュメントの削除 | removed | 0 | 331 | 331 | 
| [agentic-retrieval-how-to-create-knowledge-base-python.md](#item-4e498f) | breaking change | Pythonによるナレッジベースの作成に関するドキュメントの削除 | removed | 0 | 278 | 278 | 
| [agentic-retrieval-how-to-create-knowledge-base-rest.md](#item-37851c) | breaking change | REST APIによるナレッジベースの作成に関するドキュメントの削除 | removed | 0 | 270 | 270 | 
| [manage-index-portal.md](#item-7a1916) | bug fix | インデックス管理に関するドキュメントの削除 | removed | 0 | 68 | 68 | 
| [manage-index-rest.md](#item-8bc592) | bug fix | REST APIによるインデックス管理に関するドキュメントの削除 | removed | 0 | 70 | 70 | 
| [manage-index-sdk.md](#item-02a160) | bug fix | SDKによるインデックス管理に関するドキュメントの削除 | removed | 0 | 338 | 338 | 
| [search-faq-frequently-asked-questions.yml](#item-eab2ba) | minor update | FAQセクションのリンク修正 | modified | 1 | 1 | 2 | 
| [search-how-to-manage-index.md](#item-6bf53b) | minor update | インデックス管理に関するドキュメントの拡充 | modified | 463 | 4 | 467 | 
| [search-import-data-portal.md](#item-b804d1) | minor update | ファイアウォールに関するリンクの修正 | modified | 1 | 1 | 2 | 
| [service-configure-firewall.md](#item-75be3f) | minor update | ファイアウォール設定ドキュメントの改善 | modified | 53 | 71 | 124 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-blob.md{#item-ac6c8a}

<details>
<summary>Diff</summary>
````diff
@@ -3,27 +3,456 @@ title: Create a Blob Knowledge Source for Agentic Retrieval
 description: A blob knowledge source specifies a blob container that you want to read from. It also includes models and properties for creating an indexer, data source, skillset, and index used for agentic retrieval workloads.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/25/2026
+ms.date: 04/14/2026
 zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Create a blob knowledge source from Azure Blob Storage and ADLS Gen2
 
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+Use a *blob knowledge source* to index and query Azure blob content in an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](agentic-retrieval-how-to-retrieve.md) at query time.
+
+Unlike a [search index knowledge source](agentic-knowledge-source-how-to-search-index.md), which specifies an existing and qualified index, a blob knowledge source specifies an external data source, models, and properties to automatically generate the following Azure AI Search objects:
+
++ A data source that represents a blob container.
++ A skillset that chunks and optionally vectorizes multimodal content from the container.
++ An index that stores enriched content and meets the criteria for agentic retrieval.
++ An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
+
+> [!NOTE]
+> If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata](search-indexer-access-control-lists-and-role-based-access.md) or [Blob RBAC scopes](search-blob-indexer-role-based-access.md).
+
+### Usage support
+
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
+## Prerequisites
+
++ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md). You must have [semantic ranker enabled](semantic-how-to-enable-disable.md).
+
++ An [Azure Blob Storage](/azure/storage/common/storage-account-create) or [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/create-data-lake-storage-account) account.
+
++ A blob container with [supported content types](search-how-to-index-azure-blob-storage.md#supported-document-formats) for text content. For optional image verbalization, the supported content type depends on whether your chat completion model can analyze and describe the image file.
+
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](search-security-rbac.md), but you can use [API keys](search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](search-get-started-rbac.md).
+
+::: zone pivot="csharp"
+
++ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
+
+::: zone-end
+
+::: zone pivot="python"
+
++ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
+
+::: zone-end
+
+::: zone pivot="rest"
+
++ The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
+
+::: zone-end
+
+## Check for existing knowledge sources
+
+::: zone pivot="csharp"
+
+[!INCLUDE [Check for existing knowledge sources using C#](includes/how-tos/knowledge-source-check-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Check for existing knowledge sources using Python](includes/how-tos/knowledge-source-check-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [Check for existing knowledge sources using REST](includes/how-tos/knowledge-source-check-rest.md)]
+
+::: zone-end
+
+The following JSON is an example response for a blob knowledge source.
+
+```json
+{
+  "name": "my-blob-ks",
+  "kind": "azureBlob",
+  "description": "A sample blob knowledge source.",
+  "encryptionKey": null,
+  "azureBlobParameters": {
+    "connectionString": "<REDACTED>",
+    "containerName": "blobcontainer",
+    "folderPath": null,
+    "isADLSGen2": false,
+    "ingestionParameters": {
+      "disableImageVerbalization": false,
+      "ingestionPermissionOptions": [],
+      "contentExtractionMode": "standard",
+      "identity": null,
+      "embeddingModel": {
+        "kind": "azureOpenAI",
+        "azureOpenAIParameters": {
+          "resourceUri": "<REDACTED>",
+          "deploymentId": "text-embedding-3-large",
+          "apiKey": "<REDACTED>",
+          "modelName": "text-embedding-3-large",
+          "authIdentity": null
+        }
+      },
+      "chatCompletionModel": {
+        "kind": "azureOpenAI",
+        "azureOpenAIParameters": {
+          "resourceUri": "<REDACTED>",
+          "deploymentId": "gpt-5-mini",
+          "apiKey": "<REDACTED>",
+          "modelName": "gpt-5-mini",
+          "authIdentity": null
+        }
+      },
+      "ingestionSchedule": null,
+      "assetStore": null,
+      "aiServices": {
+        "uri": "<REDACTED>",
+        "apiKey": "<REDACTED>"
+      }
+    },
+    "createdResources": {
+      "datasource": "my-blob-ks-datasource",
+      "indexer": "my-blob-ks-indexer",
+      "skillset": "my-blob-ks-skillset",
+      "index": "my-blob-ks-index"
+    }
+  }
+}
+```
+
+> [!NOTE]
+> Sensitive information is redacted. The generated resources appear at the end of the response.
+
+## Create a knowledge source
+
 ::: zone pivot="csharp"
-[!INCLUDE [C#](includes/how-tos/agentic-knowledge-source-how-to-blob-csharp.md)]
+
+Run the following code to [create a blob knowledge source](/dotnet/api/azure.search.documents.indexes.models.azureblobknowledgesource?view=azure-dotnet-preview&preserve-view=true).
+
+```csharp
+// Create a blob knowledge source
+using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+using Azure.Search.Documents.KnowledgeBases.Models;
+using Azure;
+
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+
+var chatCompletionParams = new AzureOpenAIVectorizerParameters
+{
+    ResourceUri = new Uri(aoaiEndpoint),
+    DeploymentName = aoaiGptDeployment,
+    ModelName = aoaiGptModel
+};
+
+var embeddingParams = new AzureOpenAIVectorizerParameters
+{
+    ResourceUri = new Uri(aoaiEndpoint),
+    DeploymentName = aoaiEmbeddingDeployment,
+    ModelName = aoaiEmbeddingModel
+};
+
+var ingestionParams = new KnowledgeSourceIngestionParameters
+{
+    DisableImageVerbalization = false,
+    ChatCompletionModel = new KnowledgeBaseAzureOpenAIModel(azureOpenAIParameters: chatCompletionParams),
+    EmbeddingModel = new KnowledgeSourceAzureOpenAIVectorizer
+    {
+        AzureOpenAIParameters = embeddingParams
+    }
+};
+
+var blobParams = new AzureBlobKnowledgeSourceParameters(
+    connectionString: connectionString,
+    containerName: containerName
+)
+{
+    IsAdlsGen2 = false,
+    IngestionParameters = ingestionParams
+};
+
+var knowledgeSource = new AzureBlobKnowledgeSource(
+    name: "my-blob-ks",
+    azureBlobParameters: blobParams
+)
+{
+    Description = "This knowledge source pulls from a blob storage container."
+};
+
+await indexClient.CreateOrUpdateKnowledgeSourceAsync(knowledgeSource);
+Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated successfully.");
+```
+
 ::: zone-end
 
 ::: zone pivot="python"
-[!INCLUDE [Python](includes/how-tos/agentic-knowledge-source-how-to-blob-python.md)]
+
+Run the following code to create a blob knowledge source.
+
+```python
+# Create a blob knowledge source
+from azure.core.credentials import AzureKeyCredential
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import AzureBlobKnowledgeSource, AzureBlobKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceAzureOpenAIVectorizer, KnowledgeSourceContentExtractionMode, KnowledgeSourceIngestionParameters
+
+index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+
+knowledge_source = AzureBlobKnowledgeSource(
+    name = "my-blob-ks",
+    description = "This knowledge source pulls from a blob storage container.",
+    encryption_key = None,
+    azure_blob_parameters = AzureBlobKnowledgeSourceParameters(
+        connection_string = "blob_connection_string",
+        container_name = "blob_container_name",
+        folder_path = None,
+        is_adls_gen2 = False,
+        ingestion_parameters = KnowledgeSourceIngestionParameters(
+            identity = None,
+            disable_image_verbalization = False,
+            chat_completion_model = KnowledgeBaseAzureOpenAIModel(
+                azure_open_ai_parameters = AzureOpenAIVectorizerParameters(
+                    resource_url = "aoai_endpoint",
+                    deployment_name = "aoai_gpt_deployment",
+                    model_name = "aoai_gpt_model",
+                    api_key = "aoai_api_key"
+                )
+            ),
+            embedding_model = KnowledgeSourceAzureOpenAIVectorizer(
+                azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
+                    resource_url = "aoai_endpoint",
+                    deployment_name = "aoai_embedding_deployment",
+                    model_name = "aoai_embedding_model",
+                    api_key = "aoai_api_key"
+                )
+            ),
+            content_extraction_mode = KnowledgeSourceContentExtractionMode.MINIMAL,
+            ingestion_schedule = None,
+            ingestion_permission_options = None
+        )
+    )
+)
+
+index_client.create_or_update_knowledge_source(knowledge_source)
+print(f"Knowledge source '{knowledge_source.name}' created or updated successfully.")
+```
+
 ::: zone-end
 
 ::: zone pivot="rest"
-[!INCLUDE [REST](includes/how-tos/agentic-knowledge-source-how-to-blob-rest.md)]
+
+Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create a blob knowledge source.
+
+```http
+PUT {{search-url}}/knowledgesources/my-blob-ks?api-version=2025-11-01-preview
+api-key: {{api-key}}
+Content-Type: application/json
+
+{
+  "name": "my-blob-ks",
+  "kind": "azureBlob",
+  "description": "This knowledge source pulls from a blob storage container.",
+  "encryptionKey": null,
+  "azureBlobParameters": {
+    "connectionString": "<YOUR AZURE STORAGE CONNECTION STRING>",
+    "containerName": "<YOUR BLOB CONTAINER NAME>",
+    "folderPath": null,
+    "isADLSGen2": false,
+    "ingestionParameters": {
+        "identity": null,
+        "disableImageVerbalization": null,
+        "chatCompletionModel": {
+            "kind": "azureOpenAI",
+            "azureOpenAIParameters": {
+                "resourceUri": "{{aoai-endpoint}}",
+                "deploymentId": "{{aoai-gpt-deployment}}",
+                "modelName": "{{aoai-gpt-model}}",
+                "apiKey": "{{aoai-key}}"
+            }
+        },
+        "embeddingModel": {
+            "kind": "azureOpenAI",
+            "azureOpenAIParameters": {
+                "resourceUri": "{{aoai-endpoint}}",
+                "deploymentId": "{{aoai-embedding-deployment}}",
+                "modelName": "{{aoai-embedding-model}}",
+                "apiKey": "{{aoai-key}}"
+            }
+        },
+        "contentExtractionMode": "minimal",
+        "ingestionSchedule": null,
+        "ingestionPermissionOptions": []
+    }
+  }
+}
+```
+
+::: zone-end
+
+### Source-specific properties
+
+You can pass the following properties to create a blob knowledge source.
+
+::: zone pivot="csharp"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `Name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `Description` | A description of the knowledge source. | String | Yes | No |
+| `EncryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
+| `AzureBlobParameters` | Parameters specific to blob knowledge sources: `ConnectionString`, `ContainerName`, `FolderPath`, and `IsAdlsGen2`. | Object |  | No |
+| `ConnectionString` | A key-based [connection string](search-how-to-index-azure-blob-storage.md#supported-credentials-and-connection-strings) or, if you're using a managed identity, the resource ID. | String | No | Yes |
+| `ContainerName` | The name of the blob storage container. | String | No | Yes |
+| `FolderPath` | A folder within the container. | String | No | No |
+| `IsAdlsGen2` | The default is `False`. Set to `True` if you're using an ADLS Gen2 storage account. | Boolean | No | No |
+
+::: zone-end
+
+::: zone pivot="python"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `description` | A description of the knowledge source. | String | Yes | No |
+| `encryption_key` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
+| `azure_blob_parameters` | Parameters specific to blob knowledge sources: `connection_string`, `container_name`, `folder_path`, and `is_adls_gen2`. | Object |  | No |
+| `connection_string` | A key-based [connection string](search-how-to-index-azure-blob-storage.md#supported-credentials-and-connection-strings) or, if you're using a managed identity, the resource ID. | String | No | Yes |
+| `container_name` | The name of the blob storage container. | String | No | Yes |
+| `folder_path` | A folder within the container. | String | No | No |
+| `is_adls_gen2` | The default is `False`. Set to `True` if you're using an ADLS Gen2 storage account. | Boolean | No | No |
+
+::: zone-end
+
+::: zone pivot="rest"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `kind` | The kind of knowledge source, which is `azureBlob` in this case. | String | No | Yes |
+| `description` | A description of the knowledge source. | String | Yes | No |
+| `encryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
+| `azureBlobParameters` | Parameters specific to blob knowledge sources: `connectionString`, `containerName`, `folderPath`, and `isADLSGen2`. | Object |  | No |
+| `connectionString` | A key-based [connection string](search-how-to-index-azure-blob-storage.md#supported-credentials-and-connection-strings) or, if you're using a managed identity, the resource ID. | String | No | Yes |
+| `containerName` | The name of the blob storage container. | String | No | Yes |
+| `folderPath` | A folder within the container. | String | No | No |
+| `isADLSGen2` | The default is `false`. Set to `true` if you're using an ADLS Gen2 storage account. | Boolean | No | No |
+
+::: zone-end
+
+### Ingestion parameters properties
+
+::: zone pivot="csharp"
+
+[!INCLUDE [C# ingestionParameters properties](includes/how-tos/knowledge-source-ingestion-parameters-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Python ingestionParameters properties](includes/how-tos/knowledge-source-ingestion-parameters-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [REST ingestionParameters properties](includes/how-tos/knowledge-source-ingestion-parameters-rest.md)]
+
+::: zone-end
+
+## Check ingestion status
+
+::: zone pivot="csharp"
+
+[!INCLUDE [C# knowledge source status](includes/how-tos/knowledge-source-status-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Python knowledge source status](includes/how-tos/knowledge-source-status-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [REST knowledge source status](includes/how-tos/knowledge-source-status-rest.md)]
+
+::: zone-end
+
+## Review the created objects
+
+When you create a blob knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
+
+After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
+
+We recommend using the Azure portal to validate output creation. The workflow is:
+
+1. Check the indexer for success or failure messages. Connection or quota errors appear here.
+1. Check the index for searchable content. Use Search Explorer to run queries.
+1. Check the skillset to learn how your content is chunked and optionally vectorized.
+1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
+
+## Assign to a knowledge base
+
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+
+After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
+
+::: zone pivot="csharp"
+
+> [!TIP]
+> To enforce document-level permissions, set `IngestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
+::: zone-end
+
+::: zone pivot="python"
+
+> [!TIP]
+> To enforce document-level permissions, set `ingestion_permission_options` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
+::: zone-end
+
+::: zone pivot="rest"
+
+> [!TIP]
+> To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
+::: zone-end
+
+## Delete a knowledge source
+
+::: zone pivot="csharp"
+
+[!INCLUDE [Delete knowledge source using C#](includes/how-tos/knowledge-source-delete-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Delete knowledge source using Python](includes/how-tos/knowledge-source-delete-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [Delete knowledge source using REST](includes/how-tos/knowledge-source-delete-rest.md)]
+
 ::: zone-end
 
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
 + [Azure AI Search blob knowledge source Python sample](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/knowledge/blob-knowledge-source.ipynb)
 + [Agentic RAG: Build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
-+ [Azure OpenAI demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
\ No newline at end of file
++ [Azure OpenAI demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
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
この修正は、Azure Blobストレージを使用したエージェントリトリーバルのためのBlob知識ソースの作成に関するドキュメントを改訂しています。この修正には、434行の追加と5行の削除が含まれ、合計439行が変更されました。主な変更点は、Blob知識ソースの利用方法、前提条件、及び関連する使用例の詳細な説明が加えられたことにあります。

具体的には、新しい機能としてBlob知識ソースがエージェントリトリーバルパイプラインでどのようにインデックスされ、クエリされるのかが詳細に記載されています。従来の検索インデックス知識ソースとの違いや、データソース、スキルセット、インデクサなどのAzure AI Searchオブジェクトが自動的に生成されるプロセスについても触れています。また、Blobストレージでのユーザーアクセスのメタデータの管理方法についての注意点や、さまざまなSDKとREST APIの使用方法が示されています。

この変更により、Blob知識ソースの利用方法がより明確になり、開発者がこれを活用する際の手助けとなることを目的としています。

## articles/search/agentic-knowledge-source-how-to-onelake.md{#item-ec7a80}

<details>
<summary>Diff</summary>
````diff
@@ -5,26 +5,443 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2025
 ms.topic: how-to
-ms.date: 03/25/2026
+ms.date: 04/14/2026
 zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Create an indexed OneLake knowledge source
 
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+Use an *indexed OneLake knowledge source* to index and query Microsoft OneLake files in an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](agentic-retrieval-how-to-retrieve.md) at query time.
+
+When you create an indexed OneLake knowledge source, you specify an external data source, models, and properties to automatically generate the following Azure AI Search objects:
+
++ A data source that represents a lakehouse.
++ A skillset that chunks and optionally vectorizes multimodal content from the lakehouse.
++ An index that stores enriched content and meets the criteria for agentic retrieval.
++ An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
+
+The generated indexer conforms to the *OneLake indexer*, whose prerequisites, supported tasks, supported document formats, supported shortcuts, and limitations also apply to OneLake knowledge sources. For more information, see the [OneLake indexer documentation](search-how-to-index-onelake-files.md).
+
+### Usage support
+
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
+## Prerequisites
+
++ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md). You must have [semantic ranker enabled](semantic-how-to-enable-disable.md).
+
++ Completion of the [OneLake indexer prerequisites](search-how-to-index-onelake-files.md#prerequisites).
+
++ Completion of the [OneLake indexer data preparation](search-how-to-index-onelake-files.md#prepare-data-for-indexing).
+
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](search-security-rbac.md), but you can use [API keys](search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](search-get-started-rbac.md).
+
+::: zone pivot="csharp"
+
++ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
+
+::: zone-end
+
+::: zone pivot="python"
+
++ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
+
+::: zone-end
+
+::: zone pivot="rest"
+
++ The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
+
+::: zone-end
+
+## Check for existing knowledge sources
+
 ::: zone pivot="csharp"
-[!INCLUDE [C#](includes/how-tos/agentic-knowledge-source-how-to-onelake-csharp.md)]
+
+[!INCLUDE [Check for existing knowledge sources using C#](includes/how-tos/knowledge-source-check-csharp.md)]
+
 ::: zone-end
 
 ::: zone pivot="python"
-[!INCLUDE [Python](includes/how-tos/agentic-knowledge-source-how-to-onelake-python.md)]
+
+[!INCLUDE [Check for existing knowledge sources using Python](includes/how-tos/knowledge-source-check-python.md)]
+
 ::: zone-end
 
 ::: zone pivot="rest"
-[!INCLUDE [REST](includes/how-tos/agentic-knowledge-source-how-to-onelake-rest.md)]
+
+[!INCLUDE [Check for existing knowledge sources using REST](includes/how-tos/knowledge-source-check-rest.md)]
+
+::: zone-end
+
+The following JSON is an example response for an indexed OneLake knowledge source.
+
+```json
+{
+  "name": "my-onelake-ks",
+  "kind": "indexedOneLake",
+  "description": "A sample indexed OneLake knowledge source.",
+  "encryptionKey": null,
+  "indexedOneLakeParameters": {
+    "fabricWorkspaceId": "<REDACTED>",
+    "lakehouseId": "<REDACTED>",
+    "targetPath": null,
+    "ingestionParameters": {
+      "disableImageVerbalization": false,
+      "ingestionPermissionOptions": [],
+      "contentExtractionMode": "standard",
+      "identity": null,
+      "embeddingModel": {
+        "kind": "azureOpenAI",
+        "azureOpenAIParameters": {
+          "resourceUri": "<REDACTED>",
+          "deploymentId": "text-embedding-3-large",
+          "apiKey": "<REDACTED>",
+          "modelName": "text-embedding-3-large"
+        }
+      },
+      "chatCompletionModel": {
+        "kind": "azureOpenAI",
+        "azureOpenAIParameters": {
+          "resourceUri": "<REDACTED>",
+          "deploymentId": "gpt-5-mini",
+          "apiKey": "<REDACTED>",
+          "modelName": "gpt-5-mini"
+        }
+      },
+      "ingestionSchedule": null,
+      "aiServices": {
+        "uri": "<REDACTED>",
+        "apiKey": "<REDACTED>"
+      }
+    },
+    "createdResources": {
+    "datasource": "my-onelake-ks-datasource",
+    "indexer": "my-onelake-ks-indexer",
+    "skillset": "my-onelake-ks-skillset",
+    "index": "my-onelake-ks-index"
+    }
+  }
+}
+```
+
+> [!NOTE]
+> Sensitive information is redacted. The generated resources appear at the end of the response.
+
+## Create a knowledge source
+
+::: zone pivot="csharp"
+
+Run the following code to create an indexed OneLake knowledge source.
+
+```csharp
+// Create an IndexedOneLake knowledge source
+using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+using Azure.Search.Documents.KnowledgeBases.Models;
+using Azure;
+
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+
+var chatCompletionParams = new AzureOpenAIVectorizerParameters
+{
+    ResourceUri = new Uri(aoaiEndpoint),
+    DeploymentName = aoaiGptDeployment,
+    ModelName = aoaiGptModel
+};
+
+var embeddingParams = new AzureOpenAIVectorizerParameters
+{
+    ResourceUri = new Uri(aoaiEndpoint),
+    DeploymentName = aoaiEmbeddingDeployment,
+    ModelName = aoaiEmbeddingModel
+};
+
+var ingestionParams = new KnowledgeSourceIngestionParameters
+{
+    DisableImageVerbalization = false,
+    ChatCompletionModel = new KnowledgeBaseAzureOpenAIModel(azureOpenAIParameters: chatCompletionParams),
+    EmbeddingModel = new KnowledgeSourceAzureOpenAIVectorizer
+    {
+        AzureOpenAIParameters = embeddingParams
+    }
+};
+
+var oneLakeParams = new IndexedOneLakeKnowledgeSourceParameters(
+    fabricWorkspaceId: fabricWorkspaceId,
+    lakehouseId: lakehouseId)
+{
+    IngestionParameters = ingestionParams
+};
+
+var knowledgeSource = new IndexedOneLakeKnowledgeSource(
+    name: "my-onelake-ks",
+    indexedOneLakeParameters: oneLakeParams)
+{
+    Description = "This knowledge source pulls content from a lakehouse."
+};
+
+await indexClient.CreateOrUpdateKnowledgeSourceAsync(knowledgeSource);
+Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated successfully.");
+```
+
+::: zone-end
+
+::: zone pivot="python"
+
+Run the following code to create an indexed OneLake knowledge source.
+
+```python
+# Create an indexed OneLake knowledge source
+from azure.core.credentials import AzureKeyCredential
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import IndexedOneLakeKnowledgeSource, IndexedOneLakeKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceAzureOpenAIVectorizer, KnowledgeSourceContentExtractionMode, KnowledgeSourceIngestionParameters
+
+index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+
+knowledge_source = IndexedOneLakeKnowledgeSource(
+    name = "my-onelake-ks",
+    description= "This knowledge source pulls content from a lakehouse.",
+    encryption_key = None,
+    indexed_one_lake_parameters = IndexedOneLakeKnowledgeSourceParameters(
+        fabric_workspace_id = "fabric_workspace_id",
+        lakehouse_id = "lakehouse_id",
+        target_path = None,
+        ingestion_parameters = KnowledgeSourceIngestionParameters(
+            identity = None,
+            disable_image_verbalization = False,
+            chat_completion_model = KnowledgeBaseAzureOpenAIModel(
+                azure_open_ai_parameters = AzureOpenAIVectorizerParameters(
+                    resource_url = "aoai_endpoint",
+                    deployment_name = "aoai_gpt_deployment",
+                    model_name = "aoai_gpt_model",
+                    api_key = "aoai_api_key"
+                )
+            ),
+            embedding_model = KnowledgeSourceAzureOpenAIVectorizer(
+                azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
+                    resource_url = "aoai_endpoint",
+                    deployment_name = "aoai_embedding_deployment",
+                    model_name = "aoai_embedding_model",
+                    api_key = "aoai_api_key"
+                )
+            ),
+            content_extraction_mode = KnowledgeSourceContentExtractionMode.MINIMAL,
+            ingestion_schedule = None,
+            ingestion_permission_options = None
+        )
+    )
+)
+
+index_client.create_or_update_knowledge_source(knowledge_source)
+print(f"Knowledge source '{knowledge_source.name}' created or updated successfully.")
+```
+
+::: zone-end
+
+::: zone pivot="rest"
+
+Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create an indexed OneLake knowledge source.
+
+```http
+PUT {{search-url}}/knowledgesources/my-onelake-ks?api-version=2025-11-01-preview
+api-key: {{api-key}}
+Content-Type: application/json
+
+{
+    "name": "my-onelake-ks",
+    "kind": "indexedOneLake",
+    "description": "This knowledge source pulls content from a lakehouse.",
+    "indexedOneLakeParameters": {
+      "fabricWorkspaceId": "<YOUR FABRIC WORKSPACE GUID>",
+      "lakehouseId": "<YOUR LAKEHOUSE GUID>",
+      "targetPath": null,
+      "ingestionParameters": {
+        "identity": null,
+        "disableImageVerbalization": null,
+        "chatCompletionModel": {
+            "kind": "azureOpenAI",
+            "azureOpenAIParameters": {
+                "resourceUri": "{{aoai-endpoint}}",
+                "deploymentId": "{{aoai-gpt-deployment}}",
+                "modelName": "{{aoai-gpt-model}}",
+                "apiKey": "{{aoai-key}}"
+            }
+        },
+        "embeddingModel": {
+            "kind": "azureOpenAI",
+            "azureOpenAIParameters": {
+                "resourceUri": "{{aoai-endpoint}}",
+                "deploymentId": "{{aoai-embedding-deployment}}",
+                "modelName": "{{aoai-embedding-model}}",
+                "apiKey": "{{aoai-key}}"
+            }
+        },
+        "contentExtractionMode": "minimal",
+        "ingestionSchedule": null,
+        "ingestionPermissionOptions": []
+    }
+  }
+}
+```
+
+::: zone-end
+
+### Source-specific properties
+
+You can pass the following properties to create an indexed OneLake knowledge source.
+
+::: zone pivot="csharp"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `Name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `Description` | A description of the knowledge source. | String | Yes | No |
+| `EncryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
+| `IndexedOneLakeKnowledgeSourceParameters` | Parameters specific to OneLake knowledge sources: `FabricWorkspaceId`, `LakehouseId`, and `TargetPath`. | Object |  | Yes |
+| `FabricWorkspaceId` | The GUID of the workspace that contains the lakehouse. | String | No | Yes |
+| `LakehouseId` | The GUID of the lakehouse. | String | No | Yes |
+| `TargetPath` | A folder or shortcut within the lakehouse. When unspecified, the entire lakehouse is indexed. | String | No | No |
+
+::: zone-end
+
+::: zone pivot="python"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `description` | A description of the knowledge source. | String | Yes | No |
+| `encryption_key` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
+| `indexed_one_lake_parameters` | Parameters specific to OneLake knowledge sources: `fabric_workspace_id`, `lakehouse_id`, and `target_path`. | Object |  | Yes |
+| `fabric_workspace_id` | The GUID of the workspace that contains the lakehouse. | String | No | Yes |
+| `lakehouse_id` | The GUID of the lakehouse. | String | No | Yes |
+| `target_path` | A folder or shortcut within the lakehouse. When unspecified, the entire lakehouse is indexed. | String | No | No |
+
+::: zone-end
+
+::: zone pivot="rest"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `kind` | The kind of knowledge source, which is `indexedOneLake` in this case. | String | No | Yes |
+| `description` | A description of the knowledge source. | String | Yes | No |
+| `encryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
+| `indexedOneLakeParameters` | Parameters specific to OneLake knowledge sources: `fabricWorkspaceId`, `lakehouseId`, and `targetPath`. | Object |  | Yes |
+| `fabricWorkspaceId` | The GUID of the workspace that contains the lakehouse. | String | No | Yes |
+| `lakehouseId` | The GUID of the lakehouse. | String | No | Yes |
+| `targetPath` | A folder or shortcut within the lakehouse. When unspecified, the entire lakehouse is indexed. | String | No | No |
+
+::: zone-end
+
+### Ingestion parameters properties
+
+::: zone pivot="csharp"
+
+[!INCLUDE [C# ingestionParameters properties](includes/how-tos/knowledge-source-ingestion-parameters-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Python ingestionParameters properties](includes/how-tos/knowledge-source-ingestion-parameters-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [REST ingestionParameters properties](includes/how-tos/knowledge-source-ingestion-parameters-rest.md)]
+
+::: zone-end
+
+## Check ingestion status
+
+::: zone pivot="csharp"
+
+[!INCLUDE [C# knowledge source status](includes/how-tos/knowledge-source-status-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Python knowledge source status](includes/how-tos/knowledge-source-status-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [REST knowledge source status](includes/how-tos/knowledge-source-status-rest.md)]
+
+::: zone-end
+
+## Review the created objects
+
+When you create an indexed OneLake knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
+
+After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
+
+We recommend using the Azure portal to validate output creation. The workflow is:
+
+1. Check the indexer for success or failure messages. Connection or quota errors appear here.
+1. Check the index for searchable content. Use Search Explorer to run queries.
+1. Check the skillset to learn how your content is chunked and optionally vectorized.
+1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
+
+## Assign to a knowledge base
+
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+
+For any knowledge base that specifies an indexed OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
+
+After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
+
+::: zone pivot="csharp"
+
+> [!TIP]
+> To enforce document-level permissions, set `IngestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
+::: zone-end
+
+::: zone pivot="python"
+
+> [!TIP]
+> To enforce document-level permissions, set `ingestion_permission_options` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
+::: zone-end
+
+::: zone pivot="rest"
+
+> [!TIP]
+> To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
+::: zone-end
+
+## Delete a knowledge source
+
+::: zone pivot="csharp"
+
+[!INCLUDE [Delete knowledge source using C#](includes/how-tos/knowledge-source-delete-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Delete knowledge source using Python](includes/how-tos/knowledge-source-delete-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [Delete knowledge source using REST](includes/how-tos/knowledge-source-delete-rest.md)]
+
 ::: zone-end
 
 ## Related content
 
-+ [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
++ [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
 + [Agentic RAG: Build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
 + [Azure OpenAI demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス付きOneLake知識ソースの作成方法の更新"
}
```

### Explanation
この修正は、Microsoft OneLakeファイルをエージェントリトリーバルパイプラインでインデックスし、クエリするためのインデックス付きOneLake知識ソースの作成に関するドキュメントを更新しています。422行の追加と5行の削除が行われ、合計427行が変更されました。改訂内容には、インデックス付きOneLake知識ソースの使用方法、所定のオブジェクトの自動生成プロセス、ひいては前提条件やサポートされるSDKに関する情報が含まれています。

新たに追加された内容として、OneLake知識ソースを構成する上で必要なデータソース、スキルセット、インデックス、インデクサに関する詳細が提供されており、OneLakeインデクサに関するドキュメントのリンクも含まれています。また、Azureポータルを使用して作成されたオブジェクトのバリデーションを行う方法や、知識ソースの作成後には、エージェントが取得アクションを実行する時に必要となる参照データを引用するための設定についても触れられています。

これにより、開発者がインデックス付きOneLake知識ソースを適切に作成し、活用するための理解が深まることを意図しています。

## articles/search/agentic-knowledge-source-how-to-search-index.md{#item-09d366}

<details>
<summary>Diff</summary>
````diff
@@ -3,22 +3,249 @@ title: Create a Search Index Knowledge Source
 description: Learn how to create a search index knowledge source, which specifies an index used by a knowledge base for agentic retrieval workloads.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/25/2026
+ms.date: 04/14/2026
 zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Create a search index knowledge source
 
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+A *search index knowledge source* specifies a connection to an Azure AI Search index that provides searchable content in an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](agentic-retrieval-how-to-retrieve.md) at query time.
+
+### Usage support
+
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
+## Prerequisites
+
++ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md). You must have [semantic ranker enabled](semantic-how-to-enable-disable.md).
+
++ A search index containing plain text or vector content with a semantic configuration. [Review the index criteria for agentic retrieval](agentic-retrieval-how-to-create-index.md#criteria-for-agentic-retrieval). The index must be on the same search service as the knowledge base.
+
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](search-security-rbac.md), but you can use [API keys](search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](search-get-started-rbac.md).
+
+::: zone pivot="csharp"
+
++ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
+
+::: zone-end
+
+::: zone pivot="python"
+
++ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
+
+::: zone-end
+
+::: zone pivot="rest"
+
++ The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
+
+::: zone-end
+
+## Check for existing knowledge sources
+
 ::: zone pivot="csharp"
-[!INCLUDE [C#](includes/how-tos/agentic-knowledge-source-how-to-search-index-csharp.md)]
+
+[!INCLUDE [Check for existing knowledge sources using C#](includes/how-tos/knowledge-source-check-csharp.md)]
+
 ::: zone-end
 
 ::: zone pivot="python"
-[!INCLUDE [Python](includes/how-tos/agentic-knowledge-source-how-to-search-index-python.md)]
+
+[!INCLUDE [Check for existing knowledge sources using Python](includes/how-tos/knowledge-source-check-python.md)]
+
 ::: zone-end
 
 ::: zone pivot="rest"
-[!INCLUDE [REST](includes/how-tos/agentic-knowledge-source-how-to-search-index-rest.md)]
+
+[!INCLUDE [Check for existing knowledge sources using REST](includes/how-tos/knowledge-source-check-rest.md)]
+
+::: zone-end
+
+The following JSON is an example response for a search index knowledge source. Notice that the knowledge source specifies a single index name and which fields in the index to include in the query.
+
+```json
+{
+  "name": "my-search-index-ks",
+  "kind": "searchIndex",
+  "description": "A sample search index knowledge source.",
+  "encryptionKey": null,
+  "searchIndexParameters": {
+    "searchIndexName": "my-search-index",
+    "semanticConfigurationName": null,
+    "sourceDataFields": [],
+    "searchFields": []
+  }
+}
+```
+
+## Create a knowledge source
+
+::: zone pivot="csharp"
+
+Run the following code to create a search index knowledge source.
+
+```csharp
+// Create a search index knowledge source
+using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+using Azure;
+
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+
+var indexKnowledgeSource = new SearchIndexKnowledgeSource(
+    name: knowledgeSourceName,
+    searchIndexParameters: new SearchIndexKnowledgeSourceParameters(searchIndexName: indexName)
+    {
+        SourceDataFields = { new SearchIndexFieldReference(name: "id"), new SearchIndexFieldReference(name: "page_chunk"), new SearchIndexFieldReference(name: "page_number") }
+    }
+);
+
+await indexClient.CreateOrUpdateKnowledgeSourceAsync(indexKnowledgeSource);
+Console.WriteLine($"Knowledge source '{knowledgeSourceName}' created or updated successfully.");
+```
+
+::: zone-end
+
+::: zone pivot="python"
+
+Run the following code to create a search index knowledge source.
+
+```python
+# Create a search index knowledge source
+from azure.core.credentials import AzureKeyCredential
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import SearchIndexKnowledgeSource, SearchIndexKnowledgeSourceParameters, SearchIndexFieldReference
+
+index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+
+knowledge_source = SearchIndexKnowledgeSource(
+    name = "my-search-index-ks",
+    description= "This knowledge source pulls from an existing index designed for agentic retrieval.",
+    encryption_key = None,
+    search_index_parameters = SearchIndexKnowledgeSourceParameters(
+        search_index_name = "search_index_name",
+        semantic_configuration_name = "semantic_configuration_name",
+        source_data_fields = [
+            SearchIndexFieldReference(name="description"),
+            SearchIndexFieldReference(name="category"),
+        ],
+        search_fields = [
+            SearchIndexFieldReference(name="id")
+        ],
+    )
+)
+
+index_client.create_or_update_knowledge_source(knowledge_source)
+print(f"Knowledge source '{knowledge_source.name}' created or updated successfully.")
+```
+
+::: zone-end
+
+::: zone pivot="rest"
+
+Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create a search index knowledge source.
+
+```http
+PUT {{search-url}}/knowledgesources/my-search-index-ks?api-version=2025-11-01-preview
+api-key: {{api-key}}
+Content-Type: application/json
+
+{
+    "name": "my-search-index-ks",
+    "kind": "searchIndex",
+    "description": "This knowledge source pulls from an existing index designed for agentic retrieval.",
+    "encryptionKey": null,
+    "searchIndexParameters": {
+        "searchIndexName": "<YOUR INDEX NAME>",
+        "semanticConfigurationName": "my-semantic-config",
+        "sourceDataFields": [
+          { "name": "description" },
+          { "name": "category" }
+        ]
+    }
+}
+```
+
+::: zone-end
+
+### Source-specific properties
+
+You can pass the following properties to create a search index knowledge source.
+
+::: zone pivot="csharp"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `Name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `Description` | A description of the knowledge source. | String | Yes | No |
+| `EncryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
+| `SearchIndexParameters` | Parameters specific to search index knowledge sources: `SearchIndexName`, `SemanticConfigurationName`, `SourceDataFields`, and `SearchFields`. | Object | Yes | Yes |
+| `SearchIndexName` | The name of the existing search index. | String | Yes | Yes |
+| `SemanticConfigurationName` | Overrides the default semantic configuration for the search index. | String | Yes | No |
+| `SourceDataFields` | The index fields returned when you specify `IncludeReferenceSourceData` in the knowledge base definition. These fields are used for citations and should be `retrievable`. Examples include the document name, file name, page numbers, or chapter numbers. | Array | Yes | No |
+| `SearchFields` | The index fields to specifically search against. When unspecified, all fields are searched. | Array | Yes | No |
+
+::: zone-end
+
+::: zone pivot="python"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `description` | A description of the knowledge source. | String | Yes | No |
+| `encryption_key` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
+| `search_index_parameters` | Parameters specific to search index knowledge sources: `search_index_name`, `semantic_configuration_name`, `source_data_fields`, and `search_fields`. | Object | Yes | Yes |
+| `search_index_name` | The name of the existing search index. | String | Yes | Yes |
+| `semantic_configuration_name` | Overrides the default semantic configuration for the search index. | String | Yes | No |
+| `source_data_fields` | The index fields returned when you specify `include_reference_source_data` in the knowledge base definition. These fields are used for citations and should be `retrievable`. Examples include the document name, file name, page numbers, or chapter numbers. | Array | Yes | No |
+| `search_fields` | The index fields to specifically search against. When unspecified, all fields are searched. | Array | Yes | No |
+
+::: zone-end
+
+::: zone pivot="rest"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `kind` | The kind of knowledge source, which is `searchIndex` in this case. | String | No | Yes |
+| `description` | A description of the knowledge source. | String | Yes | No |
+| `encryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
+| `searchIndexParameters` | Parameters specific to search index knowledge sources: `searchIndexName`, `semanticConfigurationName`, `sourceDataFields`, and `searchFields`. | Object | Yes | Yes |
+| `searchIndexName` | The name of the existing search index. | String | Yes | Yes |
+| `semanticConfigurationName` | Overrides the default semantic configuration for the search index. | String | Yes | No |
+| `sourceDataFields` | The index fields returned when you specify `includeReferenceSourceData` in the knowledge base definition. These fields are used for citations and should be `retrievable`. Examples include the document name, file name, page numbers, or chapter numbers. | Array | Yes | No |
+| `searchFields` | The index fields to specifically search against. When unspecified, all fields are searched. | Array | Yes | No |
+
+::: zone-end
+
+## Assign to a knowledge base
+
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+
+After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
+
+## Delete a knowledge source
+
+::: zone pivot="csharp"
+
+[!INCLUDE [Delete knowledge source using C#](includes/how-tos/knowledge-source-delete-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Delete knowledge source using Python](includes/how-tos/knowledge-source-delete-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [Delete knowledge source using REST](includes/how-tos/knowledge-source-delete-rest.md)]
+
 ::: zone-end
 
 ## Related content
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックス知識ソースの作成方法の更新"
}
```

### Explanation
この修正は、Azure AI Searchの検索インデックス知識ソースを作成する方法に関するドキュメントを改訂したものです。231行の追加と4行の削除が行われ、合計235行が変更されました。新たに追加された内容には、検索インデックス知識ソースの使用方法、必要な前提条件、SDKやREST APIに関する情報が含まれています。

具体的には、検索インデックス知識ソースは、エージェントリトリーバルパイプラインで使用される検索可能なコンテンツへの接続を指定し、必要なインデックスやフィールド情報の定義が詳述されています。また、知識ソースの作成や更新に必要なサンプルコードも追加されており、C#、Python、およびREST APIを使用して検索インデックス知識ソースを簡単に作成できる方法が示されています。

さらに、知識ソースが使用するデータフィールドや検索フィールドに関する詳細、またそれらがどのように引用に使用されるかについての情報も提供されています。これにより、開発者が検索インデックス知識ソースをより効果的に利用することができるよう支援しています。

## articles/search/agentic-knowledge-source-how-to-sharepoint-indexed.md{#item-fe72fc}

<details>
<summary>Diff</summary>
````diff
@@ -3,22 +3,426 @@ title: Create a SharePoint (Indexed) Knowledge Source
 description: Learn how to create an indexed SharePoint knowledge source, which ingests content from SharePoint sites into a searchable index on Azure AI Search.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/25/2026
+ms.date: 04/14/2026
 zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Create an indexed SharePoint knowledge source
 
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+Use an *indexed SharePoint knowledge source* to index and query SharePoint content in an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](agentic-retrieval-how-to-retrieve.md) at query time.
+
+When you create an indexed SharePoint knowledge source, you specify a SharePoint connection string, models, and properties to automatically generate the following Azure AI Search objects:
+
++ A data source that points to SharePoint sites.
++ A skillset that chunks and optionally vectorizes multimodal content.
++ An index that stores enriched content and meets the criteria for agentic retrieval.
++ An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
+
+### Usage support
+
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
+## Prerequisites
+
++ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md). You must have [semantic ranker enabled](semantic-how-to-enable-disable.md).
+
++ Completion of the [SharePoint indexer prerequisites](search-how-to-index-sharepoint-online.md#prerequisites).
+
++ Completion of the following SharePoint indexer configuration steps:
+
+  + [Step 1: Enable a managed identity for Azure AI Search](search-how-to-index-sharepoint-online.md#step-1-optional-enable-system-assigned-managed-identity) (required only for secretless authentication; skip if using a client secret)
+  + [Step 2: Choose either delegated or application permissions](search-how-to-index-sharepoint-online.md#step-2-decide-which-permissions-the-indexer-requires)
+  + [Step 3: Create a Microsoft Entra application registration](search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration) (for application permissions, you also configure a [client secret](search-how-to-index-sharepoint-online.md#using-client-secret) or [secretless authentication](search-how-to-index-sharepoint-online.md#using-secretless-authentication-to-obtain-application-tokens))
+
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](search-security-rbac.md), but you can use [API keys](search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](search-get-started-rbac.md).
+
+::: zone pivot="csharp"
+
++ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
+
+::: zone-end
+
+::: zone pivot="python"
+
++ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
+
+::: zone-end
+
+::: zone pivot="rest"
+
++ The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
+
+::: zone-end
+
+## Check for existing knowledge sources
+
 ::: zone pivot="csharp"
-[!INCLUDE [C#](includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-csharp.md)]
+
+[!INCLUDE [Check for existing knowledge sources using C#](includes/how-tos/knowledge-source-check-csharp.md)]
+
 ::: zone-end
 
 ::: zone pivot="python"
-[!INCLUDE [Python](includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-python.md)]
+
+[!INCLUDE [Check for existing knowledge sources using Python](includes/how-tos/knowledge-source-check-python.md)]
+
 ::: zone-end
 
 ::: zone pivot="rest"
-[!INCLUDE [REST](includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-rest.md)]
+
+[!INCLUDE [Check for existing knowledge sources using REST](includes/how-tos/knowledge-source-check-rest.md)]
+
+::: zone-end
+
+The following JSON is an example response for an indexed SharePoint knowledge source.
+
+```json
+{
+  "name": "my-indexed-sharepoint-ks",
+  "kind": "indexedSharePoint",
+  "description": "A sample indexed SharePoint knowledge source",
+  "encryptionKey": null,
+  "indexedSharePointParameters": {
+    "connectionString": "<redacted>",
+    "containerName": "defaultSiteLibrary",
+    "query": null,
+    "ingestionParameters": {
+      "disableImageVerbalization": false,
+      "ingestionPermissionOptions": [],
+      "contentExtractionMode": "minimal",
+      "identity": null,
+      "embeddingModel": {
+        "kind": "azureOpenAI",
+        "azureOpenAIParameters": {
+          "resourceUri": "<redacted>",
+          "deploymentId": "text-embedding-3-large",
+          "apiKey": "<redacted>",
+          "modelName": "text-embedding-3-large",
+          "authIdentity": null
+        }
+      },
+      "chatCompletionModel": null,
+      "ingestionSchedule": null,
+      "assetStore": null,
+      "aiServices": null
+    },
+    "createdResources": {
+      "datasource": "my-indexed-sharepoint-ks-datasource",
+      "indexer": "my-indexed-sharepoint-ks-indexer",
+      "skillset": "my-indexed-sharepoint-ks-skillset",
+      "index": "my-indexed-sharepoint-ks-index"
+    }
+  },
+  "indexedOneLakeParameters": null
+}
+```
+
+> [!NOTE]
+> Sensitive information is redacted. The generated resources appear at the end of the response.
+
+## Create a knowledge source
+
+::: zone pivot="csharp"
+
+Run the following code to create an indexed SharePoint knowledge source.
+
+```csharp
+// Create an IndexedSharePoint knowledge source
+using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+using Azure.Search.Documents.KnowledgeBases.Models;
+using Azure;
+
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+
+var chatCompletionParams = new AzureOpenAIVectorizerParameters
+{
+    ResourceUri = new Uri(aoaiEndpoint),
+    DeploymentName = aoaiGptDeployment,
+    ModelName = aoaiGptModel
+};
+
+var embeddingParams = new AzureOpenAIVectorizerParameters
+{
+    ResourceUri = new Uri(aoaiEndpoint),
+    DeploymentName = aoaiEmbeddingDeployment,
+    ModelName = aoaiEmbeddingModel
+};
+
+var ingestionParams = new KnowledgeSourceIngestionParameters
+{
+    DisableImageVerbalization = false,
+    ChatCompletionModel = new KnowledgeBaseAzureOpenAIModel(azureOpenAIParameters: chatCompletionParams),
+    EmbeddingModel = new KnowledgeSourceAzureOpenAIVectorizer
+    {
+        AzureOpenAIParameters = embeddingParams
+    }
+};
+
+var sharePointParams = new IndexedSharePointKnowledgeSourceParameters(
+    connectionString: sharePointConnectionString,
+    containerName: "defaultSiteLibrary")
+{
+    IngestionParameters = ingestionParams
+};
+
+var knowledgeSource = new IndexedSharePointKnowledgeSource(
+    name: "my-indexed-sharepoint-ks",
+    indexedSharePointParameters: sharePointParams)
+{
+    Description = "A sample indexed SharePoint knowledge source."
+};
+
+await indexClient.CreateOrUpdateKnowledgeSourceAsync(knowledgeSource);
+Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated successfully.");
+```
+
+::: zone-end
+
+::: zone pivot="python"
+
+Run the following code to create an indexed SharePoint knowledge source.
+
+```python
+# Create an indexed SharePoint knowledge source
+from azure.core.credentials import AzureKeyCredential
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import IndexedSharePointKnowledgeSource, IndexedSharePointKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceAzureOpenAIVectorizer, KnowledgeSourceContentExtractionMode, KnowledgeSourceIngestionParameters
+
+index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+
+knowledge_source = IndexedSharePointKnowledgeSource(
+    name = "my-indexed-sharepoint-ks",
+    description = "A sample indexed SharePoint knowledge source.",
+    encryption_key = None,
+    indexed_share_point_parameters = IndexedSharePointKnowledgeSourceParameters(
+        connection_string = "connection_string",
+        container_name = "defaultSiteLibrary",
+        query = None,
+        ingestion_parameters = KnowledgeSourceIngestionParameters(
+            identity = None,
+            disable_image_verbalization = False,
+            chat_completion_model = KnowledgeBaseAzureOpenAIModel(
+                azure_open_ai_parameters = AzureOpenAIVectorizerParameters(
+                    resource_url = "aoai_endpoint",
+                    deployment_name = "aoai_gpt_deployment",
+                    model_name = "aoai_gpt_model",
+                    api_key = "aoai_api_key"
+                )
+            ),
+            embedding_model = KnowledgeSourceAzureOpenAIVectorizer(
+                azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
+                    resource_url = "aoai_endpoint",
+                    deployment_name = "aoai_embedding_deployment",
+                    model_name = "aoai_embedding_model",
+                    api_key = "aoai_api_key"
+                )
+            ),
+            content_extraction_mode = KnowledgeSourceContentExtractionMode.MINIMAL,
+            ingestion_schedule = None,
+            ingestion_permission_options = None
+        )
+    )
+)
+
+index_client.create_or_update_knowledge_source(knowledge_source)
+print(f"Knowledge source '{knowledge_source.name}' created or updated successfully.")
+```
+
+::: zone-end
+
+::: zone pivot="rest"
+
+Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create an indexed SharePoint knowledge source.
+
+```http
+PUT {{search-url}}/knowledgesources/my-indexed-sharepoint-ks?api-version=2025-11-01-preview
+api-key: {{api-key}}
+Content-Type: application/json
+
+{
+    "name": "my-indexed-sharepoint-ks",
+    "kind": "indexedSharePoint",
+    "description": "A sample indexed SharePoint knowledge source.",
+    "encryptionKey": null,
+    "indexedSharePointParameters": {
+        "connectionString": "{{sharepoint-connection-string}}",
+        "containerName": "defaultSiteLibrary",
+        "query": null,
+        "ingestionParameters": {
+            "identity": null,
+            "embeddingModel": {
+                "kind": "azureOpenAI",
+                "azureOpenAIParameters": {
+                    "deploymentId": "text-embedding-3-large",
+                    "modelName": "text-embedding-3-large",
+                    "resourceUri": "{{aoai-endpoint}}",
+                    "apiKey": "{{aoai-key}}"
+                }
+            },
+            "chatCompletionModel": null,
+            "disableImageVerbalization": false,
+            "ingestionSchedule": null,
+            "ingestionPermissionOptions": [],
+            "contentExtractionMode": "minimal"
+        }
+    }
+}
+```
+
+::: zone-end
+
+### Source-specific properties
+
+You can pass the following properties to create an indexed SharePoint knowledge source.
+
+::: zone pivot="csharp"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `Name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `Description` | A description of the knowledge source. | String | Yes | No |
+| `EncryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
+| `IndexedSharePointKnowledgeSourceParameters` | Parameters specific to indexed SharePoint knowledge sources: `ConnectionString`, `ContainerName`, and `Query`. | Object | No | No |
+| `ConnectionString` | The connection string to a SharePoint site. For more information, see [Connection string syntax](search-how-to-index-sharepoint-online.md#connection-string-format). | String | Yes | Yes |
+| `ContainerName` | The SharePoint library to access. Use `defaultSiteLibrary` to index content from the site's default document library or `allSiteLibraries` to index content from every document library in the site. Ignore `useQuery` for now. | String | No | Yes |
+| `Query` | Optional [query](search-how-to-index-sharepoint-online.md#query) to filter SharePoint content. | String | Yes | No |
+
+::: zone-end
+
+::: zone pivot="python"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `description` | A description of the knowledge source. | String | Yes | No |
+| `encryption_key` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
+| `indexed_share_point_parameters` | Parameters specific to indexed SharePoint knowledge sources: `connection_string`, `container_name`, and `query`. | Object | No | No |
+| `connection_string` | The connection string to a SharePoint site. For more information, see [Connection string syntax](search-how-to-index-sharepoint-online.md#connection-string-format). | String | Yes | Yes |
+| `container_name` | The SharePoint library to access. Use `defaultSiteLibrary` to index content from the site's default document library or `allSiteLibraries` to index content from every document library in the site. Ignore `useQuery` for now. | String | No | Yes |
+| `query` | Optional [query](search-how-to-index-sharepoint-online.md#query) to filter SharePoint content. | String | Yes | No |
+
+::: zone-end
+
+::: zone pivot="rest"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `kind` | The kind of knowledge source, which is `indexedSharePoint` in this case. | String | No | Yes |
+| `description` | A description of the knowledge source. | String | Yes | No |
+| `encryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
+| `indexedSharePointParameters` | Parameters specific to indexed SharePoint knowledge sources: `connectionString`, `containerName`, and `query`. | Object | No | Yes |
+| `connectionString` | The connection string to a SharePoint site. For more information, see [Connection string syntax](search-how-to-index-sharepoint-online.md#connection-string-format). | String | Yes | Yes |
+| `containerName` | The SharePoint library to access. Use `defaultSiteLibrary` to index content from the site's default document library or `allSiteLibraries` to index content from every document library in the site. Ignore `useQuery` for now. | String | No | Yes |
+| `query` | Optional [query](search-how-to-index-sharepoint-online.md#query) to filter SharePoint content. | String | Yes | No |
+
+::: zone-end
+
+### Ingestion parameters properties
+
+::: zone pivot="csharp"
+
+[!INCLUDE [C# ingestionParameters properties](includes/how-tos/knowledge-source-ingestion-parameters-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Python ingestionParameters properties](includes/how-tos/knowledge-source-ingestion-parameters-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [REST ingestionParameters properties](includes/how-tos/knowledge-source-ingestion-parameters-rest.md)]
+
+::: zone-end
+
+## Check ingestion status
+
+::: zone pivot="csharp"
+
+[!INCLUDE [C# knowledge source status](includes/how-tos/knowledge-source-status-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Python knowledge source status](includes/how-tos/knowledge-source-status-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [REST knowledge source status](includes/how-tos/knowledge-source-status-rest.md)]
+
+::: zone-end
+
+## Review the created objects
+
+When you create an indexed SharePoint knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
+
+After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
+
+We recommend using the Azure portal to validate output creation. The workflow is:
+
+1. Check the indexer for success or failure messages. Connection or quota errors appear here.
+1. Check the index for searchable content. Use Search Explorer to run queries.
+1. Check the skillset to learn how your content is chunked and optionally vectorized.
+1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
+
+## Assign to a knowledge base
+
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+
+For any knowledge base that specifies an indexed SharePoint knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
+
+After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
+
+::: zone pivot="csharp"
+
+> [!TIP]
+> To enforce document-level permissions, set `IngestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
+::: zone-end
+
+::: zone pivot="python"
+
+> [!TIP]
+> To enforce document-level permissions, set `ingestion_permission_options` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
+::: zone-end
+
+::: zone pivot="rest"
+
+> [!TIP]
+> To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
+::: zone-end
+
+## Delete a knowledge source
+
+::: zone pivot="csharp"
+
+[!INCLUDE [Delete knowledge source using C#](includes/how-tos/knowledge-source-delete-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Delete knowledge source using Python](includes/how-tos/knowledge-source-delete-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [Delete knowledge source using REST](includes/how-tos/knowledge-source-delete-rest.md)]
+
 ::: zone-end
 
 ## Related content
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス付きSharePoint知識ソースの作成方法の更新"
}
```

### Explanation
この修正は、インデックス付きSharePoint知識ソースを作成する方法に関するドキュメントを更新したもので、408行の追加と4行の削除が行われ、合計412行が変更されました。改訂された内容には、SharePointサイトからのコンテンツをAzure AI Searchの検索可能なインデックスに取り込む方法が詳述されています。

特に、新たに追加されたセクションでは、SharePoint接続文字列の指定、生成されるAzure AI Searchオブジェクト（データソース、スキルセット、インデックス、インデクサ）の詳細が強調されています。また、SharePointインデクサの前提条件および設定手順が細かく示されており、必要なアクセス権やAPIキーに関する情報も提供されています。

さらに、インデックス付きSharePoint知識ソースを作成するためのサンプルコードがC#やPython、REST APIの形で示され、開発者が実際に実装する際のガイダンスが強化されています。これにより、SharePointからのコンテンツの効率的なインデクシングと、それを利用したエージェントリトリーバルの構築が容易になります。

## articles/search/agentic-knowledge-source-how-to-sharepoint-remote.md{#item-79d019}

<details>
<summary>Diff</summary>
````diff
@@ -3,24 +3,438 @@ title: Create a SharePoint (Remote) Knowledge Source
 description: Learn how to create a remote SharePoint knowledge source, which tells an agentic retrieval engine in Azure AI Search to query SharePoint sites directly.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/25/2026
+ms.date: 04/14/2026
 zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Create a remote SharePoint knowledge source
 
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+A *remote SharePoint knowledge source* uses the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) to query textual content directly from SharePoint in Microsoft 365. No search index or connection string is needed. Only textual content is queried, and usage is billed through Microsoft 365 and a Copilot license.
+
+To limit sites or constrain search, set a [filter expression](#filter-expression-examples) to scope by URLs, date ranges, file types, and other metadata. The caller's identity must be recognized by both the Azure tenant and the Microsoft 365 tenant because the retrieval engine queries SharePoint on behalf of the user.
+
+Like any other knowledge source, you specify a remote SharePoint knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) and use the results as grounding data when an agent or chatbot calls a [retrieve action](agentic-retrieval-how-to-retrieve.md) at query time.
+
+### Usage support
+
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
+## Prerequisites
+
++ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md). You must have [semantic ranker enabled](semantic-how-to-enable-disable.md). 
+
++ SharePoint in a Microsoft 365 tenant that's under the same Microsoft Entra ID tenant as Azure.
+
++ A Microsoft 365 Copilot license for query-time access to SharePoint content.
+
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](search-security-rbac.md), but you can use [API keys](search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](search-get-started-rbac.md).
+
+::: zone pivot="csharp"
+
++ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
+
+::: zone-end
+
+::: zone pivot="python"
+
++ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
+
+::: zone-end
+
+::: zone pivot="rest"
+
++ The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
+
+::: zone-end
+
+## Limitations
+
+The following limitations in the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) apply to remote SharePoint knowledge sources.
+
++ There's no support for Copilot connectors or OneDrive content. Content is retrieved from SharePoint sites only.
+
++ Limit of 200 requests per user per hour.
+
++ Query character limit of 1,500 characters.
+
++ Hybrid queries are only supported for the following file extensions: .doc, .docx, .pptx, .pdf, .aspx, and .one.
+
++ Multimodal retrieval (nontextual content, including tables, images, and charts) isn't supported.
+
++ Maximum of 25 results from a query.
+
++ Results are returned by Copilot Retrieval API as unordered.
+
++ Invalid Keyword Query Language (KQL) filter expressions are ignored and the query continues to execute without the filter.
+
+## Check for existing knowledge sources
+
+::: zone pivot="csharp"
+
+[!INCLUDE [Check for existing knowledge sources using C#](includes/how-tos/knowledge-source-check-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Check for existing knowledge sources using Python](includes/how-tos/knowledge-source-check-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [Check for existing knowledge sources using REST](includes/how-tos/knowledge-source-check-rest.md)]
+
+::: zone-end
+
+The following JSON is an example response for a remote SharePoint knowledge source.
+
+```json
+{
+  "name": "my-sharepoint-ks",
+  "kind": "remoteSharePoint",
+  "description": "A sample remote SharePoint knowledge source",
+  "encryptionKey": null,
+  "remoteSharePointParameters": {
+    "filterExpression": "filetype:docx",
+    "containerTypeId": null,
+    "resourceMetadata": [
+      "Author",
+      "Title"
+    ]
+  }
+}
+```
+
+## Create a knowledge source
+
 ::: zone pivot="csharp"
-[!INCLUDE [C#](includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-csharp.md)]
+
+Run the following code to create a remote SharePoint knowledge source.
+
+```csharp
+// Create a remote SharePoint knowledge source
+using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+using Azure.Search.Documents.KnowledgeBases.Models;
+using Azure;
+
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), credential);
+
+var knowledgeSource = new RemoteSharePointKnowledgeSource(name: "my-remote-sharepoint-ks")
+{
+    Description = "This knowledge source queries .docx files in a trusted Microsoft 365 tenant.",
+    RemoteSharePointParameters = new RemoteSharePointKnowledgeSourceParameters()
+    {
+        FilterExpression = "filetype:docx",
+        ResourceMetadata = { "Author", "Title" }
+    }
+};
+
+await indexClient.CreateOrUpdateKnowledgeSourceAsync(knowledgeSource);
+Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated successfully.");
+```
+
 ::: zone-end
 
 ::: zone pivot="python"
-[!INCLUDE [Python](includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-python.md)]
+
+Run the following code to create a remote SharePoint knowledge source.
+
+```python
+# Create a remote SharePoint knowledge source
+from azure.core.credentials import AzureKeyCredential
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import RemoteSharePointKnowledgeSource, RemoteSharePointKnowledgeSourceParameters
+
+index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+
+knowledge_source = RemoteSharePointKnowledgeSource(
+    name = "my-remote-sharepoint-ks",
+    description= "This knowledge source queries .docx files in a trusted Microsoft 365 tenant.",
+    encryption_key = None,
+    remote_share_point_parameters = RemoteSharePointKnowledgeSourceParameters(
+        filter_expression = "filetype:docx",
+        resource_metadata = ["Author", "Title"],
+        container_type_id = None
+    )
+)
+
+index_client.create_or_update_knowledge_source(knowledge_source)
+print(f"Knowledge source '{knowledge_source.name}' created or updated successfully.")
+```
+
 ::: zone-end
 
 ::: zone pivot="rest"
-[!INCLUDE [REST](includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-rest.md)]
+
+Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create a remote SharePoint knowledge source.
+
+```http
+PUT {{search-url}}/knowledgesources/my-remote-sharepoint-ks?api-version=2025-11-01-preview
+api-key: {{api-key}}
+Content-Type: application/json
+
+{
+    "name": "my-remote-sharepoint-ks",
+    "kind": "remoteSharePoint",
+    "description": "This knowledge source queries .docx files in a trusted Microsoft 365 tenant.",
+    "encryptionKey": null,
+    "remoteSharePointParameters": {
+        "filterExpression": "filetype:docx",
+        "resourceMetadata": [ "Author", "Title" ],
+        "containerTypeId": null
+    }
+}
+```
+
+::: zone-end
+
+### Source-specific properties
+
+You can pass the following properties to create a remote SharePoint knowledge source.
+
+::: zone pivot="csharp"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `Name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `Description` | A description of the knowledge source. | String | Yes | No |
+| `EncryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in the knowledge source. | Object | Yes | No |
+| `RemoteSharePointParameters` | Parameters specific to remote SharePoint knowledge sources: `FilterExpression`, `ResourceMetadata`, and `ContainerTypeId`. | Object | No | No |
+| `FilterExpression` | An expression written in the SharePoint [KQL](/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference), which is used to specify sites and paths to content. | String | Yes | No |
+| `ResourceMetadata` | An array of standard metadata fields: author, file name, creation date, content type, and file type. | Array | Yes | No |
+| `ContainerTypeId` | Container ID for the SharePoint Embedded connection. When unspecified, SharePoint Online is used. | String | Yes | No |
+
 ::: zone-end
 
+::: zone pivot="python"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `description` | A description of the knowledge source. | String | Yes | No |
+| `encryption_key` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in the knowledge source. | Object | Yes | No |
+| `remote_share_point_parameters` | Parameters specific to remote SharePoint knowledge sources: `filter_expression`, `resource_metadata`, and `container_type_id`. | Object | No | No |
+| `filter_expression` | An expression written in the SharePoint [KQL](/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference), which is used to specify sites and paths to content. | String | Yes | No |
+| `resource_metadata` | An array of standard metadata fields: author, file name, creation date, content type, and file type. | Array | Yes | No |
+| `container_type_id` | Container ID for the SharePoint Embedded connection. When unspecified, SharePoint Online is used. | String | Yes | No |
+
+::: zone-end
+
+::: zone pivot="rest"
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `kind` | The kind of knowledge source, which is `remoteSharePoint` in this case. | String | No | Yes |
+| `description` | A description of the knowledge source. | String | Yes | No |
+| `encryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in the knowledge source. | Object | Yes | No |
+| `remoteSharePointParameters` | Parameters specific to remote SharePoint knowledge sources: `filterExpression`, `resourceMetadata`, and `containerTypeId`. | Object | No | No |
+| `filterExpression` | An expression written in the SharePoint [KQL](/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference), which is used to specify sites and paths to content. | String | Yes | No |
+| `resourceMetadata` | An array of standard metadata fields: author, file name, creation date, content type, and file type. | Array | Yes | No |
+| `containerTypeId` | Container ID for the SharePoint Embedded connection. When unspecified, SharePoint Online is used. | String | Yes | No |
+
+::: zone-end
+
+### Filter expression examples
+
+Not all SharePoint properties are supported in the `filterExpression`. For a list of supported properties, see the [API reference](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval). For queryable properties, see [Queryable](/graph/connecting-external-content-manage-schema#queryable).
+
+Learn more about [KQL filters](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval?pivots=graph-v1#example-7-use-filter-expressions) in the syntax reference.
+
+| Example | Filter expression |
+|---------|-------------------|
+| Filter to a single site by ID | `"filterExpression": "SiteID:\"00aa00aa-bb11-cc22-dd33-44ee44ee44ee\""` |
+| Filter to multiple sites by ID | `"filterExpression": "SiteID:\"00aa00aa-bb11-cc22-dd33-44ee44ee44ee\" OR SiteID:\"11bb11bb-cc22-dd33-ee44-55ff55ff55ff\""` |
+| Filter to files under a specific path | `"filterExpression": "Path:\"https://my-demo.sharepoint.com/sites/mysite/Shared Documents/en/mydocs\""` |
+| Filter to a specific date range | `"filterExpression": "LastModifiedTime >= 2024-07-22 AND LastModifiedTime <= 2025-01-08"` |
+| Filter to files of a specific file type | `"filterExpression": "FileExtension:\"docx\" OR FileExtension:\"pdf\" OR FileExtension:\"pptx\""` |
+| Filter to files of a specific information protection label | `"filterExpression": "InformationProtectionLabelId:\"f0ddcc93-d3c0-4993-b5cc-76b0a283e252\""` |
+
+## Assign to a knowledge base
+
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+
+## Query a knowledge base
+
+After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query SharePoint content. Remote SharePoint has source-specific behaviors for query-time filtering, query formulation, response fields, and permissions enforcement.
+
+### Apply a KQL filter at query time
+
+::: zone pivot="csharp"
+
+You can pass a `FilterExpressionAddOn` in the `KnowledgeSourceParams` on the retrieve request to apply a KQL filter at query time. If you specify `FilterExpressionAddOn` on the retrieve request and a `FilterExpression` on the knowledge source definition, the filters are AND'd together.
+
+```csharp
+var retrievalRequest = new KnowledgeBaseRetrievalRequest();
+retrievalRequest.Messages.Add(
+    new KnowledgeBaseMessage(
+        content: new[] {
+            new KnowledgeBaseMessageTextContent("contoso product planning")
+        }
+    ) { Role = "user" }
+);
+retrievalRequest.KnowledgeSourceParams.Add(
+    new RemoteSharePointKnowledgeSourceParams("my-remote-sharepoint-ks")
+    {
+        FilterExpressionAddOn = "filetype:docx"
+    }
+);
+
+var result = await kbClient.RetrieveAsync(
+    retrievalRequest, xMsQuerySourceAuthorization: token
+);
+```
+
+::: zone-end
+
+::: zone pivot="python"
+
+You can pass a `filter_expression_add_on` in the `knowledge_source_params` on the retrieve request to apply a KQL filter at query time. If you specify `filter_expression_add_on` on the retrieve request and a `filter_expression` on the knowledge source definition, the filters are AND'd together.
+
+```python
+from azure.search.documents.knowledgebases.models import (
+    KnowledgeBaseMessage,
+    KnowledgeBaseMessageTextContent,
+    KnowledgeBaseRetrievalRequest,
+    RemoteSharePointKnowledgeSourceParams,
+)
+
+request = KnowledgeBaseRetrievalRequest(
+    messages=[
+        KnowledgeBaseMessage(
+            role="user",
+            content=[
+                KnowledgeBaseMessageTextContent(
+                    text="contoso product planning"
+                )
+            ],
+        )
+    ],
+    knowledge_source_params=[
+        RemoteSharePointKnowledgeSourceParams(
+            knowledge_source_name="my-remote-sharepoint-ks",
+            filter_expression_add_on="filetype:docx",
+        )
+    ],
+)
+
+result = kb_client.retrieve(
+    retrieval_request=request,
+    x_ms_query_source_authorization=token,
+)
+```
+
+::: zone-end
+
+::: zone pivot="rest"
+
+You can pass a `filterExpressionAddOn` in the `knowledgeSourceParams` on the retrieve request to apply a KQL filter at query time. If you specify `filterExpressionAddOn` on the retrieve request and a `filterExpression` on the knowledge source definition, the filters are AND'd together.
+
+```http
+POST {{search-url}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2025-11-01-preview
+Authorization: Bearer {{accessToken}}
+Content-Type: application/json
+x-ms-query-source-authorization: {{user-access-token}}
+
+{
+    "messages": [
+        {
+            "role": "user",
+            "content": [
+                { "type": "text", "text": "contoso product planning" }
+            ]
+        }
+    ],
+    "knowledgeSourceParams": [
+        {
+            "knowledgeSourceName": "my-remote-sharepoint-ks",
+            "kind": "remoteSharePoint",
+            "filterExpressionAddOn": "filetype:docx"
+        }
+    ]
+}
+```
+
+::: zone-end
+
+### Write effective queries
+
+::: zone pivot="csharp"
+
+Queries that ask about the content itself are more effective than questions about where a file is located or when it was last updated. For example, "Where is the keynote doc for Ignite 2024" might return no results because the content itself doesn't disclose its location. A `FilterExpression` on metadata is a better approach for file location or date-specific queries.
+
+::: zone-end
+
+::: zone pivot="python"
+
+Queries that ask about the content itself are more effective than questions about where a file is located or when it was last updated. For example, "Where is the keynote doc for Ignite 2024" might return no results because the content itself doesn't disclose its location. A `filter_expression` on metadata is a better approach for file location or date-specific queries.
+
+::: zone-end
+
+::: zone pivot="rest"
+
+Queries that ask about the content itself are more effective than questions about where a file is located or when it was last updated. For example, "Where is the keynote doc for Ignite 2024" might return no results because the content itself doesn't disclose its location. A `filterExpression` on metadata is a better approach for file location or date-specific queries.
+
+::: zone-end
+
+A more effective question is "What is the keynote doc for Ignite 2024". The response includes the synthesized answer, query activity and token counts, plus the URL and other metadata.
+
+### SharePoint-specific response fields
+
+Remote SharePoint results include fields that don't appear for other knowledge source types, such as `resourceMetadata`, `webUrl`, and `searchSensitivityLabelInfo`.
+
+```json
+{
+    "resourceMetadata": {
+        "Author": "Nuwan Amarathunga;Nurul Izzati",
+        "Title": "Ignite 2024 Keynote Address"
+    },
+    "rerankerScore": 2.489522,
+    "webUrl": "https://contoso-my.sharepoint.com/keynotes/Documents/Keynote-Ignite-2024.docx",
+    "searchSensitivityLabelInfo": {
+        "displayName": "Confidential\\Contoso Extended",
+        "sensitivityLabelId": "aaaaaaaa-0b0b-1c1c-2d2d-333333333333",
+        "tooltip": "Data is classified and protected.",
+        "priority": 5,
+        "color": "#FF8C00",
+        "isEncrypted": true
+    }
+}
+```
+
+### Enforce permissions at query time
+
+Remote SharePoint knowledge sources can enforce SharePoint permissions at query time. To enable this filtering, include the end user's access token in the retrieve request. The retrieval engine passes the token to the Copilot Retrieval API, which queries SharePoint and returns only content to which the user has access. SharePoint permissions and Microsoft Purview sensitivity labels are honored.
+
+Because remote SharePoint doesn't use a search index, no ingestion-time permissions configuration is needed. The access token is the only requirement.
+
+For instructions on passing the token, see [Enforce permissions at query time](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
+## Delete a knowledge source
+
+::: zone pivot="csharp"
+
+[!INCLUDE [Delete knowledge source using C#](includes/how-tos/knowledge-source-delete-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Delete knowledge source using Python](includes/how-tos/knowledge-source-delete-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [Delete knowledge source using REST](includes/how-tos/knowledge-source-delete-rest.md)]
+
+::: zone-end
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リモートSharePoint知識ソースの作成方法の更新"
}
```

### Explanation
この修正は、リモートSharePoint知識ソースを作成する方法に関するドキュメントの更新を示しています。418行の追加と4行の削除があり、合計422行が変更されました。改訂された内容は、Azure AI SearchのエージェントリトリーバルエンジンがMicrosoft 365のSharePointサイトから直接コンテンツをクエリするためのリモート知識ソースの作成に焦点を当てています。

新たに追加されたセクションでは、リモートSharePoint知識ソースの作成手順や、フィルター式を使用して検索を制限する方法が説明されています。この知識ソースは、特定のユーザー認証が必要であり、Microsoft 365のCopilotライセンスが求められます。また、リモートSharePointに関するいくつかの制限（リクエストの制限やサポートされない機能など）が詳しく列挙されています。

さらに、C#やPython、REST APIを使用してリモートSharePoint知識ソースを作成するためのサンプルコードが提供されており、開発者が実際にどのようにこれを実装するかの具体的な指針が強化されています。この更新により、Microsoft 365環境での情報の効率的な取得やクエリが可能となります。

## articles/search/agentic-knowledge-source-how-to-web.md{#item-6b21d0}

<details>
<summary>Diff</summary>
````diff
@@ -5,25 +5,269 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2025
 ms.topic: how-to
-ms.date: 03/25/2026
+ms.date: 04/14/2026
 zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Create a Web Knowledge Source resource
 
+> [!IMPORTANT]
+> + Web Knowledge Source, which uses Grounding with Bing Search and/or Grounding with Bing Custom Search, is a [First Party Consumption Service](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/EAEAS) governed by the [Grounding with Bing terms of use](https://www.microsoft.com/en-us/bing/apis/grounding-legal-enterprise) and the [Microsoft Privacy Statement](https://www.microsoft.com/privacy/privacystatement).
+>
+> + The [Microsoft Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) doesn't apply to data sent to Web Knowledge Source. When Customer uses Web Knowledge Source, Customer Data flows outside the Azure compliance and Geo boundary. This also means use of Web Knowledge Source waives all elevated Government Community Cloud security and compliance commitments to include data sovereignty and screened/citizenship-based support, as applicable.
+>
+> + Use of Web Knowledge Source incurs costs; learn more about [pricing](https://www.microsoft.com/en-us/bing/apis/grounding-pricing).
+>
+> + Learn more about how Azure admins can [manage access to use of Web Knowledge Source](agentic-knowledge-source-how-to-web-manage.md).
+
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+*Web Knowledge Source* enables retrieval of real-time web data from Microsoft Bing in an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](agentic-retrieval-how-to-retrieve.md) at query time.
+
+Bing Custom Search is always the search provider for Web Knowledge Source. Although you can't specify alternative search providers or engines, you can include or exclude specific *domains*, such as https://learn.microsoft.com. When no domains are specified, Web Knowledge Source has unrestricted access to the entire public internet.
+
+Web Knowledge Source works best alongside other knowledge sources. Use Web Knowledge Source when your proprietary content doesn't provide complete, up-to-date answers or when you want to supplement results with information from a commercial search engine.
+
+When you use Web Knowledge Source, keep the following in mind:
+
++ The response is always a single, formulated answer to the query instead of raw search results from the web.
+
++ Because Web Knowledge Source doesn't support extractive data, your knowledge base must use [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md) and [low or medium reasoning effort](agentic-retrieval-how-to-create-knowledge-base.md#create-a-knowledge-base). You also can't define answer instructions.
+
+### Usage support
+
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
+## Prerequisites
+
++ An Azure subscription with [access to Web Knowledge Source](agentic-knowledge-source-how-to-web-manage.md). By default, access is enabled. Contact your admin if access is disabled.
+
++ An Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md). You must have [semantic ranker enabled](semantic-how-to-enable-disable.md). The service must also be in an [Azure public region](search-region-support.md#azure-public-regions), as Web Knowledge Source isn't supported in private or sovereign clouds.
+
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](search-security-rbac.md), but you can use [API keys](search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](search-get-started-rbac.md).
+
+::: zone pivot="csharp"
+
++ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
+
+::: zone-end
+
+::: zone pivot="python"
+
++ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
+
+::: zone-end
+
+::: zone pivot="rest"
+
++ The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
+
+::: zone-end
+
+## Check for existing knowledge sources
+
+::: zone pivot="csharp"
+
+[!INCLUDE [Check for existing knowledge sources using C#](includes/how-tos/knowledge-source-check-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Check for existing knowledge sources using Python](includes/how-tos/knowledge-source-check-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [Check for existing knowledge sources using REST](includes/how-tos/knowledge-source-check-rest.md)]
+
+::: zone-end
+
+The following JSON is an example response for a Web Knowledge Source resource.
+
+```json
+{
+  "name": "my-web-ks",
+  "kind": "web",
+  "description": "A sample Web Knowledge Source.",
+  "encryptionKey": null,
+  "webParameters": {
+    "domains": null
+  }
+}
+```
+
+## Create a knowledge source
+
+::: zone pivot="csharp"
+
+Run the following code to create a Web Knowledge Source resource.
+
+```csharp
+// Create Web Knowledge Source
+using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+using Azure;
+
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+
+var knowledgeSource = new WebKnowledgeSource(name: "my-web-ks")
+{
+    Description = "A sample Web Knowledge Source.",
+    WebParameters = new WebKnowledgeSourceParameters
+    {
+        Domains = new WebKnowledgeSourceDomains
+        {
+            AllowedDomains = 
+            {
+                new WebKnowledgeSourceDomain(address: "learn.microsoft.com") { IncludeSubpages = true }
+            },
+            BlockedDomains = 
+            {
+                new WebKnowledgeSourceDomain(address: "bing.com") { IncludeSubpages = false }
+            }
+        }
+    }
+};
+
+await indexClient.CreateOrUpdateKnowledgeSourceAsync(knowledgeSource);
+Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated successfully.");
+```
+
+::: zone-end
+
+::: zone pivot="python"
+
+Run the following code to create a Web Knowledge Source resource.
+
+```python
+# Create Web Knowledge Source
+from azure.core.credentials import AzureKeyCredential
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import WebKnowledgeSource, WebKnowledgeSourceParameters, WebKnowledgeSourceDomains
+
+index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+
+knowledge_source = WebKnowledgeSource(
+    name = "my-web-ks",
+    description = "A sample Web Knowledge Source.",
+    encryption_key = None,
+    web_parameters = WebKnowledgeSourceParameters(
+        domains = WebKnowledgeSourceDomains(
+            allowed_domains = [ { "address": "learn.microsoft.com", "include_subpages": True } ],
+            blocked_domains = [ { "address": "bing.com", "include_subpages": False } ]
+        )
+    )
+)
+
+index_client.create_or_update_knowledge_source(knowledge_source)
+print(f"Knowledge source '{knowledge_source.name}' created or updated successfully.")
+```
+
+::: zone-end
+
+::: zone pivot="rest"
+
+Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create a Web Knowledge Source resource.
+
+```http
+PUT {{search-url}}/knowledgesources/my-web-ks?api-version=2025-11-01-preview
+Content-Type: application/json
+api-key: {{api-key}}
+
+{
+  "name": "my-web-ks",
+  "kind": "web",
+  "description": "This knowledge source pulls content from the web.",
+  "encryptionKey": null,
+  "webParameters": {
+    "domains": {
+      "allowedDomains": [ { "address": "learn.microsoft.com", "includeSubpages": true } ],
+      "blockedDomains": [ { "address": "bing.com", "includeSubpages": false } ]
+    }
+  }
+}
+```
+
+::: zone-end
+
+### Source-specific properties
+
+You can pass the following properties to create a Web Knowledge Source resource.
+
 ::: zone pivot="csharp"
-[!INCLUDE [C#](includes/how-tos/agentic-knowledge-source-how-to-web-csharp.md)]
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `Name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `Description` | A description of the knowledge source. When unspecified, Azure AI Search applies a default description. | String | Yes | No |
+| `EncryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in the knowledge source. | Object | Yes | No |
+| `WebParameters` | Parameters specific to Web Knowledge Source. Currently, this is only `Domains`. | Object | Yes | No |
+| `Domains` | Domains to allow or block from the search space. By default, the knowledge source uses [Grounding with Bing Search](/azure/ai-foundry/agents/how-to/tools/bing-grounding) to search the entire public internet. When you specify domains, the knowledge source uses [Grounding with Bing Custom Search](/azure/ai-foundry/agents/how-to/tools/bing-custom-search) to restrict results to the specified domains. In both cases, Bing Custom Search is the search provider. | Object | Yes | No |
+| `AllowedDomains` | Domains to include in the search space. For each domain, you must specify its `address` in the `website.com` format. You can also specify whether to include the domain's subpages by setting `IncludeSubpages` to `true` or `false`. | Array | Yes | No |
+| `BlockedDomains` | Domains to exclude from the search space. For each domain, you must specify its `address` in the `website.com` format. You can also specify whether to include the domain's subpages by setting `IncludeSubpages` to `true` or `false`. | Array | Yes | No |
+
 ::: zone-end
 
 ::: zone pivot="python"
-[!INCLUDE [Python](includes/how-tos/agentic-knowledge-source-how-to-web-python.md)]
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `description` | A description of the knowledge source. When unspecified, Azure AI Search applies a default description. | String | Yes | No |
+| `encryption_key` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in the knowledge source. | Object | Yes | No |
+| `web_parameters` | Parameters specific to Web Knowledge Source. Currently, this is only `domains`. | Object | Yes | No |
+| `domains` | Domains to allow or block from the search space. By default, the knowledge source uses [Grounding with Bing Search](/azure/ai-foundry/agents/how-to/tools/bing-grounding) to search the entire public internet. When you specify domains, the knowledge source uses [Grounding with Bing Custom Search](/azure/ai-foundry/agents/how-to/tools/bing-custom-search) to restrict results to the specified domains. In both cases, Bing Custom Search is the search provider. | Object | Yes | No |
+| `allowed_domains` | Domains to include in the search space. For each domain, you must specify its `address` in the `website.com` format. You can also specify whether to include the domain's subpages by setting `include_subpages` to `true` or `false`. | Array | Yes | No |
+| `blocked_domains` | Domains to exclude from the search space. For each domain, you must specify its `address` in the `website.com` format. You can also specify whether to include the domain's subpages by setting `include_subpages` to `true` or `false`. | Array | Yes | No |
+
 ::: zone-end
 
 ::: zone pivot="rest"
-[!INCLUDE [REST](includes/how-tos/agentic-knowledge-source-how-to-web-rest.md)]
+
+| Name | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
+| `kind` | The kind of knowledge source, which is `web` in this case. | String | No | Yes |
+| `description` | A description of the knowledge source. When unspecified, Azure AI Search applies a default description. | String | Yes | No |
+| `encryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in the knowledge source. | Object | Yes | No |
+| `webParameters` | Parameters specific to Web Knowledge Source. Currently, this is only `domains`. | Object | Yes | No |
+| `domains` | Domains to allow or block from the search space. By default, the knowledge source uses [Grounding with Bing Search](/azure/ai-foundry/agents/how-to/tools/bing-grounding) to search the entire public internet. When you specify domains, the knowledge source uses [Grounding with Bing Custom Search](/azure/ai-foundry/agents/how-to/tools/bing-custom-search) to restrict results to the specified domains. In both cases, Bing Custom Search is the search provider. | Object | Yes | No |
+| `allowedDomains` | Domains to include in the search space. For each domain, you must specify its `address` in the `website.com` format. You can also specify whether to include the domain's subpages by setting `includeSubpages` to `true` or `false`. | Array | Yes | No |
+| `blockedDomains` | Domains to exclude from the search space. For each domain, you must specify its `address` in the `website.com` format. You can also specify whether to include the domain's subpages by setting `includeSubpages` to `true` or `false`. | Array | Yes | No |
+
+::: zone-end
+
+## Assign to a knowledge base
+
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+
+After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
+
+## Delete a knowledge source
+
+::: zone pivot="csharp"
+
+[!INCLUDE [Delete knowledge source using C#](includes/how-tos/knowledge-source-delete-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="python"
+
+[!INCLUDE [Delete knowledge source using Python](includes/how-tos/knowledge-source-delete-python.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [Delete knowledge source using REST](includes/how-tos/knowledge-source-delete-rest.md)]
+
 ::: zone-end
 
 ## Related content
 
 + [Manage access to Web Knowledge Source in your Azure subscription](agentic-knowledge-source-how-to-web-manage.md)
-+ [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
++ [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Web Knowledge Sourceの作成方法の更新"
}
```

### Explanation
この修正は、Web Knowledge Sourceを作成する方法に関するドキュメントの更新を示しており、249行の追加と5行の削除が行われ、合計254行が変更されました。新たに追加された内容では、Bing SearchおよびBing Custom Searchを使用してリアルタイムのウェブデータを取得するWeb Knowledge Sourceの使用法に関する重要な情報が強調されています。

特に、Web Knowledge Sourceの利用注意事項や制約、コストが明示され、Azure管理者がこのサービスへのアクセスを管理する方法についても詳細が追加されました。この知識ソースを使うことで、エージェントやチャットボットがクエリを実行する際に、時代に即した情報を補足的に取得することが可能になります。

加えて、C#やPython、REST APIを使用してWeb Knowledge Sourceを作成するための具体的なサンプルコードが提出され、開発者がこの機能を活用する際のガイドラインが整備されています。これにより、環境における情報収集と検索の効率が大幅に向上することが期待されます。

## articles/search/agentic-retrieval-how-to-create-knowledge-base.md{#item-7df0e2}

<details>
<summary>Diff</summary>
````diff
@@ -3,26 +3,542 @@ title: Create a Knowledge Base
 description: Learn how to create a knowledge base for agentic retrieval workloads in Azure AI Search.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 01/15/2026
+ms.date: 04/14/2026
 zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Create a knowledge base in Azure AI Search
 
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+In Azure AI Search, a *knowledge base* is a top-level object that orchestrates [agentic retrieval](agentic-retrieval-overview.md). It defines which knowledge sources to query and the default behavior for retrieval operations. At query time, the [retrieve method](agentic-retrieval-how-to-retrieve.md) targets the knowledge base to run the configured retrieval pipeline.
+
+You can create a knowledge base in a [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) workload in the Microsoft Foundry (new) portal. You also need a knowledge base in any agentic solutions that you create using the Azure AI Search APIs.
+
+A knowledge base specifies:
+
++ One or more knowledge sources that point to searchable content.
++ An optional LLM that provides reasoning capabilities for query planning and answer formulation.
++ A retrieval reasoning effort that determines whether an LLM is invoked and manages cost, latency, and quality.
++ Custom properties that control routing, source selection, output format, and object encryption.
+
+After you create a knowledge base, you can update its properties at any time. If the knowledge base is in use, updates take effect on the next retrieval.
+
+> [!IMPORTANT]
+> 2025-11-01-preview renames the 2025-08-01-preview "knowledge agent" to "knowledge base." This is a breaking change. We recommend [migrating existing code](agentic-retrieval-how-to-migrate.md) to the new APIs as soon as possible.
+
+### Usage support
+
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
+## Prerequisites
+
++ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md). You must have [semantic ranker enabled](semantic-how-to-enable-disable.md). If you're using a [managed identity](search-how-to-managed-identities.md) for role-based access to deployed models, your search service must be on the Basic pricing tier or higher.
+
++ One or more [knowledge sources](agentic-knowledge-source-overview.md#supported-knowledge-sources) on your search service.
+
++ Azure OpenAI with a [supported LLM](#supported-models) deployment.
+
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](search-security-rbac.md). **Search Service Contributor** can create and manage a knowledge base. **Search Index Data Reader** can run queries. Alternatively, you can use [API keys](search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](search-get-started-rbac.md).
+
+::: zone pivot="csharp"
+
++ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
+
+::: zone-end
+
+::: zone pivot="python"
+
++ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
+
+::: zone-end
+
+::: zone pivot="rest"
+
++ The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
+
+::: zone-end
+
+### Supported models
+
+Use one of the following LLMs from Azure OpenAI in Foundry Models. For deployment instructions, see [Deploy Microsoft Foundry Models in the Foundry portal](/azure/ai-foundry/how-to/deploy-models-openai).
+
++ `gpt-4o`
++ `gpt-4o-mini`
++ `gpt-4.1`
++ `gpt-4.1-nano`
++ `gpt-4.1-mini`
++ `gpt-5`
++ `gpt-5-nano`
++ `gpt-5-mini`
+
+## Configure access
+
+Azure AI Search needs access to the LLM from Azure OpenAI. We recommend Microsoft Entra ID for authentication and role-based access for authorization. To assign roles, you must be an **Owner or User Access Administrator**. If you can't use roles, use key-based authentication instead.
+
+### [**Use roles**](#tab/rbac)
+
 ::: zone pivot="csharp"
-[!INCLUDE [C#](includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-csharp.md)]
+
+1. [Configure Azure AI Search to use a managed identity](search-how-to-managed-identities.md).
+
+1. On your model provider, such as Foundry Models, assign **Cognitive Services User** to the managed identity of your search service. If you're testing locally, assign the same role to your user account.
+
+1. For local testing, follow the steps in [Quickstart: Connect without keys](search-get-started-rbac.md) to sign in to a specific subscription and tenant. Use `DefaultAzureCredential` instead of `AzureKeyCredential` in each request, which should look similar to the following example:
+
+```csharp
+    using Azure.Search.Documents.Indexes;
+    using Azure.Identity;
+    
+    var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
+    ```
+
 ::: zone-end
 
 ::: zone pivot="python"
-[!INCLUDE [Python](includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-python.md)]
+
+1. [Configure Azure AI Search to use a managed identity](search-how-to-managed-identities.md).
+
+1. On your model provider, such as Foundry Models, assign **Cognitive Services User** to the managed identity of your search service. If you're testing locally, assign the same role to your user account.
+
+1. For local testing, follow the steps in [Quickstart: Connect without keys](search-get-started-rbac.md) to sign in to a specific subscription and tenant. Use `DefaultAzureCredential` instead of `AzureKeyCredential` in each request, which should look similar to the following example:
+
+```python
+    # Authenticate using roles
+    from azure.identity import DefaultAzureCredential
+    index_client = SearchIndexClient(endpoint = "search_url", credential = DefaultAzureCredential())
+    ```
+
 ::: zone-end
 
 ::: zone pivot="rest"
-[!INCLUDE [REST](includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-rest.md)]
+
+1. [Configure Azure AI Search to use a managed identity](search-how-to-managed-identities.md).
+
+1. On your model provider, such as Foundry Models, assign **Cognitive Services User** to the managed identity of your search service. If you're testing locally, assign the same role to your user account.
+
+1. For local testing, follow the steps in [Quickstart: Connect without keys](search-get-started-rbac.md) to get a personal access token for a specific subscription and tenant. Specify your access token in each request, which should look similar to the following example:
+
+```http
+    # List indexes using roles
+    GET https://{{search-url}}/indexes?api-version=2025-11-01-preview
+    Content-Type: application/json
+    Authorization: Bearer {{access-token}}
+    ```
+
+::: zone-end
+
+### [**Use keys**](#tab/keys)
+
+::: zone pivot="csharp"
+
+1. [Copy an Azure AI Search admin API key](search-security-api-keys.md#find-existing-keys) from the Azure portal.
+
+1. Use `AzureKeyCredential` to specify the API key in each request. Your code should look similar to the following example:
+
+```csharp
+    using Azure.Search.Documents.Indexes;
+    using Azure;
+    
+    var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+    ```
+
+::: zone-end
+
+::: zone pivot="python"
+
+1. [Copy an Azure AI Search admin API key](search-security-api-keys.md#find-existing-keys) from the Azure portal.
+
+1. Use `AzureKeyCredential` to specify the API key in each request. Your code should look similar to the following example:
+
+```python
+    # Authenticate using keys
+    from azure.core.credentials import AzureKeyCredential
+    index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+    ```
+
+::: zone-end
+
+::: zone pivot="rest"
+
+1. [Copy an Azure AI Search admin API key](search-security-api-keys.md#find-existing-keys) from the Azure portal.
+
+1. Specify the API key in each request. The key should look similar to the following example:
+
+```http
+   # List indexes using keys
+   GET {{search-url}}/indexes?api-version=2025-11-01-preview
+   Content-Type: application/json
+   api-key: {{search-api-key}}
+   ```
+
+::: zone-end
+
+---
+
+> [!IMPORTANT]
+> Code snippets in this article use API keys. If you use role-based authentication, update each request accordingly. In a request that specifies both approaches, the API key takes precedence.
+
+## Check for existing knowledge bases
+
+A knowledge base is a top-level, reusable object. Knowing about existing knowledge bases is helpful for either reuse or naming new objects. Any 2025-08-01-preview knowledge agents are returned in the knowledge bases collection.
+
+::: zone pivot="csharp"
+
+Run the following code to list existing knowledge bases by name.
+
+```csharp
+// List knowledge bases by name
+  using Azure.Search.Documents.Indexes;
+  
+  var indexClient = new SearchIndexClient(new Uri(searchEndpoint), credential);
+  var knowledgeBases = indexClient.GetKnowledgeBasesAsync();
+  
+  Console.WriteLine("Knowledge Bases:");
+  
+  await foreach (var kb in knowledgeBases)
+  {
+      Console.WriteLine($"  - {kb.Name}");
+  }
+```
+
+::: zone-end
+
+::: zone pivot="python"
+
+Run the following code to list existing knowledge bases by name.
+
+```python
+# List knowledge bases by name
+from azure.core.credentials import AzureKeyCredential
+from azure.search.documents.indexes import SearchIndexClient
+
+index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+
+for kb in index_client.list_knowledge_bases():
+    print(f"  - {kb.name}")
+```
+
+::: zone-end
+
+::: zone pivot="rest"
+
+Use [Knowledge Bases - List (REST API)](/rest/api/searchservice/knowledge-bases/list?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to list knowledge bases by name and type.
+
+```http
+# List knowledge bases
+GET {{search-url}}/knowledgebases?api-version=2025-11-01-preview&$select=name
+Content-Type: application/json
+api-key: {{search-api-key}}
+```
+
+::: zone-end
+
+You can also return a single knowledge base by name to review its JSON definition.
+
+::: zone pivot="csharp"
+
+```csharp
+using Azure.Search.Documents.Indexes;
+using System.Text.Json;
+
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), credential);
+
+// Specify the knowledge base name to retrieve
+string kbNameToGet = "earth-knowledge-base";
+
+// Get a specific knowledge base definition
+var knowledgeBaseResponse = await indexClient.GetKnowledgeBaseAsync(kbNameToGet);
+var kb = knowledgeBaseResponse.Value;
+
+// Serialize to JSON for display
+string json = JsonSerializer.Serialize(kb, new JsonSerializerOptions { WriteIndented = true });
+Console.WriteLine(json);
+```
+
+::: zone-end
+
+::: zone pivot="python"
+
+```python
+# Get a knowledge base definition
+from azure.core.credentials import AzureKeyCredential
+from azure.search.documents.indexes import SearchIndexClient
+import json
+
+index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+
+kb = index_client.get_knowledge_base("knowledge_base_name")
+print(json.dumps(kb.as_dict(), indent = 2))
+```
+
+::: zone-end
+
+::: zone pivot="rest"
+
+```http
+# Get knowledge base
+GET {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version=2025-11-01-preview
+Content-Type: application/json
+api-key: {{search-api-key}}
+```
+
+::: zone-end
+
+The following JSON is an example response for a knowledge base.
+
+```json
+{
+  "name": "my-kb",
+  "description": "A sample knowledge base.",
+  "retrievalInstructions": null,
+  "answerInstructions": null,
+  "outputMode": null,
+  "knowledgeSources": [
+    {
+      "name": "my-blob-ks"
+    }
+  ],
+  "models": [],
+  "encryptionKey": null,
+  "retrievalReasoningEffort": {
+    "kind": "low"
+  }
+}
+```
+
+## Create a knowledge base
+
+A knowledge base drives the agentic retrieval pipeline. In application code, other agents or chatbots call it.
+
+A knowledge base connects knowledge sources (searchable content) to an LLM deployment from Azure OpenAI. Properties on the LLM establish the connection, while properties on the knowledge source establish defaults that inform query execution and the response.
+
+::: zone pivot="csharp"
+
+Run the following code to create a knowledge base.
+
+```csharp
+// Create a knowledge base
+using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+using Azure.Search.Documents.KnowledgeBases.Models;
+using Azure;
+
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+
+var aoaiParams = new AzureOpenAIVectorizerParameters
+{
+    ResourceUri = new Uri(aoaiEndpoint),
+    DeploymentName = aoaiGptDeployment,
+    ModelName = aoaiGptModel
+};
+
+var knowledgeBase = new KnowledgeBase(
+    name: "my-kb",
+    knowledgeSources: new KnowledgeSourceReference[] 
+    { 
+        new KnowledgeSourceReference("hotels-ks"),
+        new KnowledgeSourceReference("earth-at-night-ks")
+    }
+)
+{
+    Description = "This knowledge base handles questions directed at two unrelated sample indexes.",
+    RetrievalInstructions = "Use the hotels knowledge source for queries about where to stay, otherwise use the earth at night knowledge source.",
+    AnswerInstructions = "Provide a two sentence concise and informative answer based on the retrieved documents.",
+    OutputMode = KnowledgeRetrievalOutputMode.AnswerSynthesis,
+    Models = { new KnowledgeBaseAzureOpenAIModel(azureOpenAIParameters: aoaiParams) },
+    RetrievalReasoningEffort = new KnowledgeRetrievalLowReasoningEffort()
+};
+
+await indexClient.CreateOrUpdateKnowledgeBaseAsync(knowledgeBase);
+Console.WriteLine($"Knowledge base '{knowledgeBase.Name}' created or updated successfully.");
+```
+
+::: zone-end
+
+::: zone pivot="python"
+
+Run the following code to create a knowledge base.
+
+```python
+# Create a knowledge base
+from azure.core.credentials import AzureKeyCredential
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import KnowledgeBase, KnowledgeBaseAzureOpenAIModel, KnowledgeSourceReference, AzureOpenAIVectorizerParameters, KnowledgeRetrievalOutputMode, KnowledgeRetrievalLowReasoningEffort
+
+index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+
+aoai_params = AzureOpenAIVectorizerParameters(
+    resource_url = "aoai_endpoint",
+    api_key="aoai_api_key",
+    deployment_name = "aoai_gpt_deployment",
+    model_name = "aoai_gpt_model",
+)
+
+knowledge_base = KnowledgeBase(
+    name = "my-kb",
+    description = "This knowledge base handles questions directed at two unrelated sample indexes.",
+    retrieval_instructions = "Use the hotels knowledge source for queries about where to stay, otherwise use the earth at night knowledge source.",
+    answer_instructions = "Provide a two sentence concise and informative answer based on the retrieved documents.",
+    output_mode = KnowledgeRetrievalOutputMode.ANSWER_SYNTHESIS,
+    knowledge_sources = [
+        KnowledgeSourceReference(name = "hotels-ks"),
+        KnowledgeSourceReference(name = "earth-at-night-ks"),
+    ],
+    models = [KnowledgeBaseAzureOpenAIModel(azure_open_ai_parameters = aoai_params)],
+    encryption_key = None,
+    retrieval_reasoning_effort = KnowledgeRetrievalLowReasoningEffort(),
+)
+
+index_client.create_or_update_knowledge_base(knowledge_base)
+print(f"Knowledge base '{knowledge_base.name}' created or updated successfully.")
+```
+
+::: zone-end
+
+::: zone pivot="rest"
+
+Use [Knowledge Bases - Create or Update (REST API)](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create a knowledge base.
+
+```http
+# Create a knowledge base
+PUT {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version=2025-11-01-preview
+Content-Type: application/json
+api-key: {{search-api-key}}
+
+{
+    "name" : "my-kb",
+    "description": "This knowledge base handles questions directed at two unrelated sample indexes.",
+    "retrievalInstructions": "Use the hotels knowledge source for queries about where to stay, otherwise use the earth at night knowledge source.",
+    "answerInstructions": null,
+    "outputMode": "answerSynthesis",
+    "knowledgeSources": [
+        {
+            "name": "hotels-ks"
+        },
+        {
+            "name": "earth-at-night-ks"
+        }
+    ],
+    "models" : [ 
+        {
+            "kind": "azureOpenAI",
+            "azureOpenAIParameters": {
+                "resourceUri": "{{model-provider-url}}",
+                "apiKey": "{{model-api-key}}",
+                "deploymentId": "gpt-4.1-mini",
+                "modelName": "gpt-4.1-mini"
+            }
+        }
+    ],
+    "encryptionKey": null,
+    "retrievalReasoningEffort": {
+        "kind": "low"
+    }
+}
+```
+
+::: zone-end
+
+### Knowledge base properties
+
+Pass the following properties to create a knowledge base.
+
+::: zone pivot="csharp"
+
+| Name | Description | Type | Required |
+|--|--|--|--|
+| `Name` | The name of the knowledge base. It must be unique within the knowledge bases collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | Yes |
+| `KnowledgeSources` | One or more [supported knowledge sources](agentic-knowledge-source-overview.md#supported-knowledge-sources). | Array | Yes |
+| `Description` | A description of the knowledge base. The LLM uses the description to inform query planning. | String | No |
+| `RetrievalInstructions` | A prompt for the LLM to determine whether a knowledge source should be in scope for a query. Include this prompt when you have multiple knowledge sources. This field influences both knowledge source selection and query formulation. For example, instructions could append information or prioritize a knowledge source. Instructions are passed directly to the LLM, which means it's possible to provide instructions that break query planning, such as instructions that result in bypassing an essential knowledge source. | String | No |
+| `AnswerInstructions` | Custom instructions to shape synthesized answers. The default is null. For more information, see [Use answer synthesis for citation-backed responses](agentic-retrieval-how-to-answer-synthesis.md). | String | No |
+| `OutputMode` | Valid values are `AnswerSynthesis` for an LLM-formulated answer or `ExtractedData` for full search results that you can pass to an LLM as a downstream step. | String | No |
+| `Models` | A connection to a [supported LLM](#supported-models) used for answer formulation or query planning. In this preview, `Models` can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Foundry portal or a command-line request. Provide the parameters by using the [KnowledgeBaseAzureOpenAIModel class](/dotnet/api/azure.search.documents.indexes.models.knowledgebaseazureopenaimodel?view=azure-dotnet-preview&preserve-view=true). You can use role-based access control instead of API keys for the Azure AI Search connection to the model. | Object | No |
+| `RetrievalReasoningEffort` | Determines the level of LLM-related query processing. Valid values are `minimal`, `low` (default), and `medium`. For more information, see [Set the retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). | Object | No |
+
+::: zone-end
+
+::: zone pivot="python"
+
+| Name | Description | Type | Required |
+|--|--|--|--|
+| `name` | The name of the knowledge base. It must be unique within the knowledge bases collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | Yes |
+| `description` | A description of the knowledge base. The LLM uses the description to inform query planning. | String | No |
+| `retrieval_instructions` | A prompt for the LLM to determine whether a knowledge source should be in scope for a query. Include this prompt when you have multiple knowledge sources. This field influences both knowledge source selection and query formulation. For example, instructions could append information or prioritize a knowledge source. Pass instructions directly to the LLM. It's possible to provide instructions that break query planning, such as instructions that result in bypassing an essential knowledge source. | String | No |
+| `answer_instructions` | Custom instructions to shape synthesized answers. The default is null. For more information, see [Use answer synthesis for citation-backed responses](agentic-retrieval-how-to-answer-synthesis.md). | String | No |
+| `output_mode` | Valid values are `answer_synthesis` for an LLM-formulated answer or `extracted_data` for full search results that you can pass to an LLM as a downstream step. | String | No |
+| `knowledge_sources` | One or more [supported knowledge sources](agentic-knowledge-source-overview.md#supported-knowledge-sources). | Array | Yes |
+| `models` | A connection to a [supported LLM](#supported-models) used for answer formulation or query planning. In this preview, `models` can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Foundry portal or a command-line request. You can use role-based access control instead of API keys for the Azure AI Search connection to the model. | Object | No |
+| `encryption_key` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge base and the generated objects. | Object | No |
+| `retrieval_reasoning_effort` | Determines the level of LLM-related query processing. Valid values are `minimal`, `low` (default), and `medium`. For more information, see [Set the retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). | Object | No |
+
+::: zone-end
+
+::: zone pivot="rest"
+
+| Name | Description | Type | Required |
+|--|--|--|--|
+| `name` | The name of the knowledge base. It must be unique within the knowledge bases collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | Yes |
+| `description` | A description of the knowledge base. The LLM uses the description to inform query planning. | String | No |
+| `retrievalInstructions` | A prompt for the LLM to determine whether a knowledge source should be in scope for a query. Include this prompt when you have multiple knowledge sources. This field influences both knowledge source selection and query formulation. For example, instructions could append information or prioritize a knowledge source. You pass instructions directly to the LLM, which means it's possible to provide instructions that break query planning, such as instructions that result in bypassing an essential knowledge source. | String | No |
+| `answerInstructions` | Custom instructions to shape synthesized answers. The default is null. For more information, see [Use answer synthesis for citation-backed responses](agentic-retrieval-how-to-answer-synthesis.md). | String | No |
+| `outputMode` | Valid values are `answerSynthesis` for an LLM-formulated answer or `extractedData` for full search results that you can pass to an LLM as a downstream step. | String | No |
+| `knowledgeSources` | One or more [supported knowledge sources](agentic-knowledge-source-overview.md#supported-knowledge-sources). | Array | Yes |
+| `models` | A connection to a [supported LLM](#supported-models) used for answer formulation or query planning. In this preview, `models` can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Foundry portal or a command-line request. You can use role-based access control instead of API keys for the Azure AI Search connection to the model. | Object | No |
+| `encryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge base and the generated objects. | Object | No |
+| `retrievalReasoningEffort.kind` | Determines the level of LLM-related query processing. Valid values are `minimal`, `low` (default), and `medium`. For more information, see [Set the retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). | Object | No |
+
+::: zone-end
+
+## Query a knowledge base
+
+After you create a knowledge base, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query it and verify the LLM connection.
+
+## Delete a knowledge base
+
+If you no longer need the knowledge base or need to rebuild it on your search service, run the following code to delete the object.
+
+::: zone pivot="csharp"
+
+```csharp
+using Azure.Search.Documents.Indexes;
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), credential);
+
+await indexClient.DeleteKnowledgeBaseAsync(knowledgeBaseName);
+System.Console.WriteLine($"Knowledge base '{knowledgeBaseName}' deleted successfully.");
+```
+
+::: zone-end
+
+::: zone pivot="python"
+
+```python
+# Delete a knowledge base
+from azure.core.credentials import AzureKeyCredential 
+from azure.search.documents.indexes import SearchIndexClient
+
+index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client.delete_knowledge_base("knowledge_base_name")
+print(f"Knowledge base deleted successfully.")
+```
+
+::: zone-end
+
+::: zone pivot="rest"
+
+```http
+# Delete a knowledge base
+DELETE {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version=2025-11-01-preview
+api-key: {{search-api-key}}
+```
+
 ::: zone-end
 
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
 + [Agentic RAG: Build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
-+ [Azure OpenAI demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
\ No newline at end of file
++ [Azure OpenAI demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジベースの作成方法に関する更新"
}
```

### Explanation
この修正は、Azure AI Searchにおけるナレッジベースの作成方法に関するドキュメントの更新を示しています。521行の追加と5行の削除が行われ、合計526行が変更されました。この更新により、ナレッジベースはエージェント式のリトリーバルのための中心的なオブジェクトであることが強調され、どのような知識ソースをクエリするのか、取得操作のデフォルトの挙動がどのように設定されるかが詳しく説明されています。

新たに導入された要素には、ナレッジベースが複数の知識ソースを指定し、LLM（大規模言語モデル）を用いた推論機能を持つことの重要性が挙げられています。また、ナレッジベースのプロパティをいつでも更新できること、及び更新が実行中のクエリに即座に反映されないことについても明記されています。

さらに、ナレッジベースの作成や削除に関する具体的なコードサンプルが各プログラミング言語（C#、Python、REST API）で提供されており、開発者がこの機能を迅速に実装できるよう支援しています。この更新により、Azure AI Searchを利用した情報検索や管理の効率が向上することが期待されます。

## articles/search/agentic-retrieval-how-to-retrieve.md{#item-d739cf}

<details>
<summary>Diff</summary>
````diff
@@ -257,9 +257,9 @@ The following table shows which knowledge sources require ingestion-time configu
 
 | Knowledge source | Requires `ingestionPermissionOptions` | How permissions are enforced |
 |---|---|---|
-| [Blob or ADLS Gen2](agentic-knowledge-source-how-to-blob.md#ingestionparameters-properties) | ✅ | Ingested RBAC scopes or ACLs matched against user identity. |
-| [OneLake](agentic-knowledge-source-how-to-onelake.md#ingestionparameters-properties) | ✅ | Ingested RBAC scopes or ACLs matched against user identity. |
-| [Indexed SharePoint](agentic-knowledge-source-how-to-sharepoint-indexed.md#ingestionparameters-properties) | ✅ | Ingested SharePoint ACLs matched against user identity. |
+| [Blob or ADLS Gen2](agentic-knowledge-source-how-to-blob.md#ingestion-parameters-properties) | ✅ | Ingested RBAC scopes or ACLs matched against user identity. |
+| [OneLake](agentic-knowledge-source-how-to-onelake.md#ingestion-parameters-properties) | ✅ | Ingested RBAC scopes or ACLs matched against user identity. |
+| [Indexed SharePoint](agentic-knowledge-source-how-to-sharepoint-indexed.md#ingestion-parameters-properties) | ✅ | Ingested SharePoint ACLs matched against user identity. |
 | [Remote SharePoint](agentic-knowledge-source-how-to-sharepoint-remote.md#assign-to-a-knowledge-base) | ❌ | Copilot Retrieval API queries SharePoint directly using the user's token. |
 
 > [!IMPORTANT]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "取り込みパラメータのリンク修正"
}
```

### Explanation
この修正は、エージェント式リトリーバルにおける取り込み設定の情報を含む文書において、3行の追加と3行の削除が行われ、合計6行が変更されました。具体的には、取り込みパラメータの参照リンクに関する微調整が施されています。

変更された内容では、各知識ソースの取り込みパラメータに関するリンクが整えられ、正確な情報に更新されています。これにより、ユーザーはそれぞれの知識ソースに関する具体的な取り込みに関する設定や要件を正しく確認できるようになります。

この修正は、文書の明確性と使いやすさを向上させるためのものであり、ユーザーが必要な情報に適切にアクセスできるようになることを意図しています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-csharp.md{#item-b5f755}

<details>
<summary>Diff</summary>
````diff
@@ -1,208 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-Use a *blob knowledge source* to index and query Azure blob content in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-Unlike a [search index knowledge source](../../agentic-knowledge-source-how-to-search-index.md), which specifies an existing and qualified index, a blob knowledge source specifies an external data source, models, and properties to automatically generate the following Azure AI Search objects:
-
-+ A data source that represents a blob container.
-+ A skillset that chunks and optionally vectorizes multimodal content from the container.
-+ An index that stores enriched content and meets the criteria for agentic retrieval.
-+ An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
-
-> [!NOTE]
-> If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata](../../search-indexer-access-control-lists-and-role-based-access.md) or [Blob RBAC scopes](../../search-blob-indexer-role-based-access.md).
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
-
-+ An [Azure Blob Storage](/azure/storage/common/storage-account-create) or [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/create-data-lake-storage-account) account. 
-
-+ A blob container with [supported content types](../../search-how-to-index-azure-blob-storage.md#supported-document-formats) for text content. For optional image verbalization, the supported content type depends on whether your chat completion model can analyze and describe the image file.
-
-+ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using C#](knowledge-source-check-csharp.md)]
-
-The following JSON is an example response for a blob knowledge source.
-
-```json
-{
-  "name": "my-blob-ks",
-  "kind": "azureBlob",
-  "description": "A sample blob knowledge source.",
-  "encryptionKey": null,
-  "azureBlobParameters": {
-    "connectionString": "<REDACTED>",
-    "containerName": "blobcontainer",
-    "folderPath": null,
-    "isADLSGen2": false,
-    "ingestionParameters": {
-      "disableImageVerbalization": false,
-      "ingestionPermissionOptions": [],
-      "contentExtractionMode": "standard",
-      "identity": null,
-      "embeddingModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<REDACTED>",
-          "deploymentId": "text-embedding-3-large",
-          "apiKey": "<REDACTED>",
-          "modelName": "text-embedding-3-large",
-          "authIdentity": null
-        }
-      },
-      "chatCompletionModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<REDACTED>",
-          "deploymentId": "gpt-5-mini",
-          "apiKey": "<REDACTED>",
-          "modelName": "gpt-5-mini",
-          "authIdentity": null
-        }
-      },
-      "ingestionSchedule": null,
-      "assetStore": null,
-      "aiServices": {
-        "uri": "<REDACTED>",
-        "apiKey": "<REDACTED>"
-      }
-    },
-    "createdResources": {
-      "datasource": "my-blob-ks-datasource",
-      "indexer": "my-blob-ks-indexer",
-      "skillset": "my-blob-ks-skillset",
-      "index": "my-blob-ks-index"
-    }
-  }
-}
-```
-
-> [!NOTE]
-> Sensitive information is redacted. The generated resources appear at the end of the response.
-
-## Create a knowledge source
-
-Run the following code to [create a blob knowledge source](/dotnet/api/azure.search.documents.indexes.models.azureblobknowledgesource?view=azure-dotnet-preview&preserve-view=true).
-
-```csharp
-// Create a blob knowledge source
-using Azure.Search.Documents.Indexes;
-using Azure.Search.Documents.Indexes.Models;
-using Azure.Search.Documents.KnowledgeBases.Models;
-using Azure;
-
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
-
-var chatCompletionParams = new AzureOpenAIVectorizerParameters
-{
-    ResourceUri = new Uri(aoaiEndpoint),
-    DeploymentName = aoaiGptDeployment,
-    ModelName = aoaiGptModel
-};
-
-var embeddingParams = new AzureOpenAIVectorizerParameters
-{
-    ResourceUri = new Uri(aoaiEndpoint),
-    DeploymentName = aoaiEmbeddingDeployment,
-    ModelName = aoaiEmbeddingModel
-};
-
-var ingestionParams = new KnowledgeSourceIngestionParameters
-{
-    DisableImageVerbalization = false,
-    ChatCompletionModel = new KnowledgeBaseAzureOpenAIModel(azureOpenAIParameters: chatCompletionParams),
-    EmbeddingModel = new KnowledgeSourceAzureOpenAIVectorizer
-    {
-        AzureOpenAIParameters = embeddingParams
-    }
-};
-
-var blobParams = new AzureBlobKnowledgeSourceParameters(
-    connectionString: connectionString,
-    containerName: containerName
-)
-{
-    IsAdlsGen2 = false,
-    IngestionParameters = ingestionParams
-};
-
-var knowledgeSource = new AzureBlobKnowledgeSource(
-    name: "my-blob-ks",
-    azureBlobParameters: blobParams
-)
-{
-    Description = "This knowledge source pulls from a blob storage container."
-};
-
-await indexClient.CreateOrUpdateKnowledgeSourceAsync(knowledgeSource);
-Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated successfully.");
-```
-
-### Source-specific properties
-
-You can pass the following properties to create a blob knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
-| `Description` | A description of the knowledge source. | String | Yes | No |
-| `encryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
-| `chatCompletionParams` | Parameters specific to chat completion models used for query planning and optional answer synthesis when the retrieval reasoning effort is low or medium. | Object |  | No |
-| `embeddingParams` | Parameters specific to embedding models used if you want to vectorize chunks of content.  | Object |  | No |
-| `azureBlobParameters` | Parameters specific to blob knowledge sources: `connectionString`, `containerName`, `folderPath`, and `isAdlsGen2`. | Object |  | No |
-| `connectionString` | A key-based [connection string](../../search-how-to-index-azure-blob-storage.md#supported-credentials-and-connection-strings) or, if you're using a managed identity, the resource ID. | String | No | Yes |
-| `containerName` | The name of the blob storage container. | String | No | Yes |
-| `folderPath` | A folder within the container. | String | No | No |
-| `isAdlsGen2` | The default is `False`. Set to `True` if you're using an ADLS Gen2 storage account. | Boolean | No | No |
-
-### `ingestionParameters` properties
-
-[!INCLUDE [C# ingestionParameters properties](knowledge-source-ingestion-parameters-csharp.md)]
-
-## Check ingestion status
-
-[!INCLUDE [C# knowledge source status](knowledge-source-status-csharp.md)]
-
-## Review the created objects
-
-When you create a blob knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
-
-After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
-
-We recommend using the Azure portal to validate output creation. The workflow is:
-
-1. Check the indexer for success or failure messages. Connection or quota errors appear here.
-1. Check the index for searchable content. Use Search Explorer to run queries.
-1. Check the skillset to learn how your content is chunked and optionally vectorized.
-1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-> [!TIP]
-> To enforce document-level permissions, set `IngestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using C#](knowledge-source-delete-csharp.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Blobナレッジソースに関するC#ドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchに関連する「Blobナレッジソース」に関するC#ドキュメントファイルの削除を示しています。この修正では、208行が削除されており、Blobナレッジソースの作成や使用に関する詳細な情報、設定、使用法がすべて取り除かれました。

削除された内容には、BlobナレッジソースがAzureのBlobコンテンツをインデックス化し、クエリを実行するための方法や、必要な前提条件、作成手順、サンプルコード、生成されるオブジェクトの一覧などが含まれており、これによりユーザーはBlobナレッジソースの操作方法についての具体的な情報を失うことになります。

この変更は、ドキュメントの整理や内容の最新化を目的としている可能性があり、Azure AI Searchの全体的な方向性についての重要なシフトを示唆しています。つまり、今後の新しい文書やリソースに振り替えるなど、利用者には他のソースに移行することが推奨されるかもしれません。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-python.md{#item-029d03}

<details>
<summary>Diff</summary>
````diff
@@ -1,193 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-Use a *blob knowledge source* to index and query Azure blob content in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-Unlike a [search index knowledge source](../../agentic-knowledge-source-how-to-search-index.md), which specifies an existing and qualified index, a blob knowledge source specifies an external data source, models, and properties to automatically generate the following Azure AI Search objects:
-
-+ A data source that represents a blob container.
-+ A skillset that chunks and optionally vectorizes multimodal content from the container.
-+ An index that stores enriched content and meets the criteria for agentic retrieval.
-+ An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
-
-> [!NOTE]
-> If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata](../../search-indexer-access-control-lists-and-role-based-access.md) or [Blob RBAC scopes](../../search-blob-indexer-role-based-access.md).
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
-
-+ An [Azure Blob Storage](/azure/storage/common/storage-account-create) or [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/create-data-lake-storage-account) account. 
-
-+ A blob container with [supported content types](../../search-how-to-index-azure-blob-storage.md#supported-document-formats) for text content. For optional image verbalization, the supported content type depends on whether your chat completion model can analyze and describe the image file.
-
-+ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using Python](knowledge-source-check-python.md)]
-
-The following JSON is an example response for a blob knowledge source.
-
-```json
-{
-  "name": "my-blob-ks",
-  "kind": "azureBlob",
-  "description": "A sample blob knowledge source.",
-  "encryptionKey": null,
-  "azureBlobParameters": {
-    "connectionString": "<REDACTED>",
-    "containerName": "blobcontainer",
-    "folderPath": null,
-    "isADLSGen2": false,
-    "ingestionParameters": {
-      "disableImageVerbalization": false,
-      "ingestionPermissionOptions": [],
-      "contentExtractionMode": "standard",
-      "identity": null,
-      "embeddingModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<REDACTED>",
-          "deploymentId": "text-embedding-3-large",
-          "apiKey": "<REDACTED>",
-          "modelName": "text-embedding-3-large",
-          "authIdentity": null
-        }
-      },
-      "chatCompletionModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<REDACTED>",
-          "deploymentId": "gpt-5-mini",
-          "apiKey": "<REDACTED>",
-          "modelName": "gpt-5-mini",
-          "authIdentity": null
-        }
-      },
-      "ingestionSchedule": null,
-      "assetStore": null,
-      "aiServices": {
-        "uri": "<REDACTED>",
-        "apiKey": "<REDACTED>"
-      }
-    },
-    "createdResources": {
-      "datasource": "my-blob-ks-datasource",
-      "indexer": "my-blob-ks-indexer",
-      "skillset": "my-blob-ks-skillset",
-      "index": "my-blob-ks-index"
-    }
-  }
-}
-```
-
-> [!NOTE]
-> Sensitive information is redacted. The generated resources appear at the end of the response.
-
-## Create a knowledge source
-
-Run the following code to create a blob knowledge source.
-
-```python
-# Create a blob knowledge source
-from azure.core.credentials import AzureKeyCredential
-from azure.search.documents.indexes import SearchIndexClient
-from azure.search.documents.indexes.models import AzureBlobKnowledgeSource, AzureBlobKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceAzureOpenAIVectorizer, KnowledgeSourceContentExtractionMode, KnowledgeSourceIngestionParameters
-
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
-
-knowledge_source = AzureBlobKnowledgeSource(
-    name = "my-blob-ks",
-    description = "This knowledge source pulls from a blob storage container.",
-    encryption_key = None,
-    azure_blob_parameters = AzureBlobKnowledgeSourceParameters(
-        connection_string = "blob_connection_string",
-        container_name = "blob_container_name",
-        folder_path = None,
-        is_adls_gen2 = False,
-        ingestion_parameters = KnowledgeSourceIngestionParameters(
-            identity = None,
-            disable_image_verbalization = False,
-            chat_completion_model = KnowledgeBaseAzureOpenAIModel(
-                azure_open_ai_parameters = AzureOpenAIVectorizerParameters(
-                    # TRIMMED FOR BREVITY
-                )
-            ),
-            embedding_model = KnowledgeSourceAzureOpenAIVectorizer(
-                azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
-                    # TRIMMED FOR BREVITY
-                )
-            ),
-            content_extraction_mode = KnowledgeSourceContentExtractionMode.MINIMAL,
-            ingestion_schedule = None,
-            ingestion_permission_options = None
-        )
-    )
-)
-
-index_client.create_or_update_knowledge_source(knowledge_source)
-print(f"Knowledge source '{knowledge_source.name}' created or updated successfully.")
-```
-
-### Source-specific properties
-
-You can pass the following properties to create a blob knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
-| `description` | A description of the knowledge source. | String | Yes | No |
-| `encryption_key` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
-| `azure_blob_parameters` | Parameters specific to blob knowledge sources: `connection_string`, `container_name`, `folder_path`, and `is_adls_gen2`. | Object |  | No |
-| `connection_string` | A key-based [connection string](../../search-how-to-index-azure-blob-storage.md#supported-credentials-and-connection-strings) or, if you're using a managed identity, the resource ID. | String | No | Yes |
-| `container_name` | The name of the blob storage container. | String | No | Yes |
-| `folder_path` | A folder within the container. | String | No | No |
-| `is_adls_gen2` | The default is `False`. Set to `True` if you're using an ADLS Gen2 storage account. | Boolean | No | No |
-
-### `ingestionParameters` properties
-
-[!INCLUDE [Python ingestionParameters properties](knowledge-source-ingestion-parameters-python.md)]
-
-## Check ingestion status
-
-[!INCLUDE [Python knowledge source status](knowledge-source-status-python.md)]
-
-## Review the created objects
-
-When you create a blob knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
-
-After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
-
-We recommend using the Azure portal to validate output creation. The workflow is:
-
-1. Check the indexer for success or failure messages. Connection or quota errors appear here.
-1. Check the index for searchable content. Use Search Explorer to run queries.
-1. Check the skillset to learn how your content is chunked and optionally vectorized.
-1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-> [!TIP]
-> To enforce document-level permissions, set `ingestion_permission_options` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using Python](knowledge-source-delete-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Blobナレッジソースに関するPythonドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Search用の「Blobナレッジソース」に関するPythonドキュメントファイルの完全な削除を示しています。193行のすべての内容が削除され、Blobナレッジソースの使用方法、作成手順、サンプルコード、前提条件、設定方法などの詳細が含まれていました。

削除された内容には、Blobナレッジソースを利用したAzure Blobコンテンツのインデックス化やクエリのパイプラインの作成に関する情報が含まれ、Pythonプログラミング言語を使用して具体的な実装がどう行われるかを示していました。また、ナレッジソースの作成時に必要なパラメータや、関連するリソース（インデクサー、インデックス、スキルセットなど）の役割も明記されていました。

この変更は、文書全体の整理や情報の統合を目的としている可能性があり、利用者はこの情報を別のリソースや文書に置き換えることが求められるかもしれません。このことは、Azure AI Searchを利用する開発者にとって影響を与える重要な変更を示しています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-rest.md{#item-b5ce57}

<details>
<summary>Diff</summary>
````diff
@@ -1,181 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-Use a *blob knowledge source* to index and query Azure blob content in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-Unlike a [search index knowledge source](../../agentic-knowledge-source-how-to-search-index.md), which specifies an existing and qualified index, a blob knowledge source specifies an external data source, models, and properties to automatically generate the following Azure AI Search objects:
-
-+ A data source that represents a blob container.
-+ A skillset that chunks and optionally vectorizes multimodal content from the container.
-+ An index that stores enriched content and meets the criteria for agentic retrieval.
-+ An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
-
-> [!NOTE]
-> If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata](../../search-indexer-access-control-lists-and-role-based-access.md) or [Blob RBAC scopes](../../search-blob-indexer-role-based-access.md).
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
-
-+ An [Azure Blob Storage](/azure/storage/common/storage-account-create) or [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/create-data-lake-storage-account) account.
-
-+ A blob container with [supported content types](../../search-how-to-index-azure-blob-storage.md#supported-document-formats) for text content. For optional image verbalization, the supported content type depends on whether your chat completion model can analyze and describe the image file.
-
-+ The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using REST](knowledge-source-check-rest.md)]
-
-The following JSON is an example response for a blob knowledge source.
-
-```json
-{
-  "name": "my-blob-ks",
-  "kind": "azureBlob",
-  "description": "A sample blob knowledge source.",
-  "encryptionKey": null,
-  "azureBlobParameters": {
-    "connectionString": "<REDACTED>",
-    "containerName": "blobcontainer",
-    "folderPath": null,
-    "isADLSGen2": false,
-    "ingestionParameters": {
-      "disableImageVerbalization": false,
-      "ingestionPermissionOptions": [],
-      "contentExtractionMode": "standard",
-      "identity": null,
-      "embeddingModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<REDACTED>",
-          "deploymentId": "text-embedding-3-large",
-          "apiKey": "<REDACTED>",
-          "modelName": "text-embedding-3-large",
-          "authIdentity": null
-        }
-      },
-      "chatCompletionModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<REDACTED>",
-          "deploymentId": "gpt-5-mini",
-          "apiKey": "<REDACTED>",
-          "modelName": "gpt-5-mini",
-          "authIdentity": null
-        }
-      },
-      "ingestionSchedule": null,
-      "assetStore": null,
-      "aiServices": {
-        "uri": "<REDACTED>",
-        "apiKey": "<REDACTED>"
-      }
-    },
-    "createdResources": {
-      "datasource": "my-blob-ks-datasource",
-      "indexer": "my-blob-ks-indexer",
-      "skillset": "my-blob-ks-skillset",
-      "index": "my-blob-ks-index"
-    }
-  }
-}
-```
-
-> [!NOTE]
-> Sensitive information is redacted. The generated resources appear at the end of the response.
-
-## Create a knowledge source
-
-Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create a blob knowledge source.
-
-```http
-PUT {{search-url}}/knowledgesources/my-blob-ks?api-version=2025-11-01-preview
-api-key: {{api-key}}
-Content-Type: application/json
-
-{
-  "name": "my-blob-ks",
-  "kind": "azureBlob",
-  "description": "This knowledge source pulls from a blob storage container.",
-  "encryptionKey": null,
-  "azureBlobParameters": {
-    "connectionString": "<YOUR AZURE STORAGE CONNECTION STRING>",
-    "containerName": "<YOUR BLOB CONTAINER NAME>",
-    "folderPath": null,
-    "isADLSGen2": false,
-    "ingestionParameters": {
-        "identity": null,
-        "disableImageVerbalization": null,
-        "chatCompletionModel": { TRIMMED FOR BREVITY },
-        "embeddingModel": { TRIMMED FOR BREVITY },
-        "contentExtractionMode": "minimal",
-        "ingestionSchedule": null,
-        "ingestionPermissionOptions": []
-    }
-  }
-}
-```
-
-### Source-specific properties
-
-You can pass the following properties to create a blob knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
-| `kind` | The kind of knowledge source, which is `azureBlob` in this case. | String | No | Yes |
-| `description` | A description of the knowledge source. | String | Yes | No |
-| `encryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
-| `azureBlobParameters` | Parameters specific to blob knowledge sources: `connectionString`, `containerName`, `folderPath`, and `isADLSGen2`. | Object |  | No |
-| `connectionString` | A key-based [connection string](../../search-how-to-index-azure-blob-storage.md#supported-credentials-and-connection-strings) or, if you're using a managed identity, the resource ID. | String | No | Yes |
-| `containerName` | The name of the blob storage container. | String | No | Yes |
-| `folderPath` | A folder within the container. | String | No | No |
-| `isADLSGen2` | The default is `false`. Set to `true` if you're using an ADLS Gen2 storage account. | Boolean | No | No |
-
-### `ingestionParameters` properties
-
-[!INCLUDE [REST ingestionParameters properties](knowledge-source-ingestion-parameters-rest.md)]
-
-## Check ingestion status
-
-[!INCLUDE [REST knowledge source status](knowledge-source-status-rest.md)]
-
-## Review the created objects
-
-When you create a blob knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
-
-After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
-
-We recommend using the Azure portal to validate output creation. The workflow is:
-
-1. Check the indexer for success or failure messages. Connection or quota errors appear here.
-1. Check the index for searchable content. Use Search Explorer to run queries.
-1. Check the skillset to learn how your content is chunked and optionally vectorized.
-1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-> [!TIP]
-> To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using REST](knowledge-source-delete-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Blobナレッジソースに関するREST APIドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchの「Blobナレッジソース」に関連するREST APIドキュメントが完全に削除されたことを示しています。181行の内容が削除され、Blobナレッジソースの設定や操作に関する重要な情報が失われました。

削除された内容には、Blobナレッジソースを使用してAzure Blobコンテンツをインデックス化し、クエリを実行するための手順、前提条件、サンプルコード、APIリクエストの例などが含まれており、ユーザーがBlobナレッジソースを利用する際の具体的なガイダンスが提供されていました。

この変更により、Azure AI SearchにおけるBlobナレッジソースの利用方法に関する情報が不足することになり、ユーザーは代替のリソースやドキュメントを探す必要があるかもしれません。全体として、この修正はAzureのドキュメントの整理と明確化の一環と考えられますが、それに伴い情報のギャップが生じる可能性もあることを留意する必要があります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-csharp.md{#item-d6611c}

<details>
<summary>Diff</summary>
````diff
@@ -1,199 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-Use an *indexed OneLake knowledge source* to index and query Microsoft OneLake files in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-When you create an indexed OneLake knowledge source, you specify an external data source, models, and properties to automatically generate the following Azure AI Search objects:
-
-+ A data source that represents a lakehouse.
-+ A skillset that chunks and optionally vectorizes multimodal content from the lakehouse.
-+ An index that stores enriched content and meets the criteria for agentic retrieval.
-+ An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
-
-The generated indexer conforms to the *OneLake indexer*, whose prerequisites, supported tasks, supported document formats, supported shortcuts, and limitations also apply to OneLake knowledge sources. For more information, see the [OneLake indexer documentation](../../search-how-to-index-onelake-files.md).
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
-
-+ Completion of the [OneLake indexer prerequisites](../../search-how-to-index-onelake-files.md#prerequisites).
-
-+ Completion of the [OneLake indexer data preparation](../../search-how-to-index-onelake-files.md#prepare-data-for-indexing).
-
-+ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using C#](knowledge-source-check-csharp.md)]
-
-The following JSON is an example response for an indexed OneLake knowledge source.
-
-```json
-{
-  "name": "my-onelake-ks",
-  "kind": "indexedOneLake",
-  "description": "A sample indexed OneLake knowledge source.",
-  "encryptionKey": null,
-  "indexedOneLakeParameters": {
-    "fabricWorkspaceId": "<REDACTED>",
-    "lakehouseId": "<REDACTED>",
-    "targetPath": null,
-    "ingestionParameters": {
-      "disableImageVerbalization": false,
-      "ingestionPermissionOptions": [],
-      "contentExtractionMode": "standard",
-      "identity": null,
-      "embeddingModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<REDACTED>",
-          "deploymentId": "text-embedding-3-large",
-          "apiKey": "<REDACTED>",
-          "modelName": "text-embedding-3-large"
-        }
-      },
-      "chatCompletionModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<REDACTED>",
-          "deploymentId": "gpt-5-mini",
-          "apiKey": "<REDACTED>",
-          "modelName": "gpt-5-mini"
-        }
-      },
-      "ingestionSchedule": null,
-      "aiServices": {
-        "uri": "<REDACTED>",
-        "apiKey": "<REDACTED>"
-      }
-    },
-    "createdResources": {
-    "datasource": "my-onelake-ks-datasource",
-    "indexer": "my-onelake-ks-indexer",
-    "skillset": "my-onelake-ks-skillset",
-    "index": "my-onelake-ks-index"
-    }
-  }
-}
-```
-
-> [!NOTE]
-> Sensitive information is redacted. The generated resources appear at the end of the response.
-
-## Create a knowledge source
-
-Run the following code to create an indexed OneLake knowledge source.
-
-```csharp
-// Create an IndexedOneLake knowledge source
-using Azure.Search.Documents.Indexes;
-using Azure.Search.Documents.Indexes.Models;
-using Azure.Search.Documents.KnowledgeBases.Models;
-using Azure;
-
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
-
-var chatCompletionParams = new AzureOpenAIVectorizerParameters
-{
-    ResourceUri = new Uri(aoaiEndpoint),
-    DeploymentName = aoaiGptDeployment,
-    ModelName = aoaiGptModel
-};
-
-var embeddingParams = new AzureOpenAIVectorizerParameters
-{
-    ResourceUri = new Uri(aoaiEndpoint),
-    DeploymentName = aoaiEmbeddingDeployment,
-    ModelName = aoaiEmbeddingModel
-};
-
-var ingestionParams = new KnowledgeSourceIngestionParameters
-{
-    DisableImageVerbalization = false,
-    ChatCompletionModel = new KnowledgeBaseAzureOpenAIModel(azureOpenAIParameters: chatCompletionParams),
-    EmbeddingModel = new KnowledgeSourceAzureOpenAIVectorizer
-    {
-        AzureOpenAIParameters = embeddingParams
-    }
-};
-
-var oneLakeParams = new IndexedOneLakeKnowledgeSourceParameters(
-    fabricWorkspaceId: fabricWorkspaceId,
-    lakehouseId: lakehouseId)
-{
-    IngestionParameters = ingestionParams
-};
-
-var knowledgeSource = new IndexedOneLakeKnowledgeSource(
-    name: "my-onelake-ks",
-    indexedOneLakeParameters: oneLakeParams)
-{
-    Description = "This knowledge source pulls content from a lakehouse."
-};
-
-await indexClient.CreateOrUpdateKnowledgeSourceAsync(knowledgeSource);
-Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated successfully.");
-```
-
-### Source-specific properties
-
-You can pass the following properties to create an indexed OneLake knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `Name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | Yes | Yes |
-| `Description` | A description of the knowledge source. | String | Yes | No |
-| `EncryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
-| `IndexedOneLakeKnowledgeSourceParameters` | Parameters specific to OneLake knowledge sources: `fabricWorkspaceId`, `lakehouseId`, and `targetPath`. | Object |  | Yes |
-| `fabricWorkspaceId` | The GUID of the workspace that contains the lakehouse. | String | No | Yes |
-| `lakehouseId` | The GUID of the lakehouse. | String | No | Yes |
-| `targetPath` | A folder or shortcut within the lakehouse. When unspecified, the entire lakehouse is indexed. | String | No | No |
-
-### `ingestionParameters` properties
-
-[!INCLUDE [C# ingestionParameters properties](knowledge-source-ingestion-parameters-csharp.md)]
-
-## Check ingestion status
-
-[!INCLUDE [C# knowledge source status](knowledge-source-status-csharp.md)]
-
-## Review the created objects
-
-When you create an indexed OneLake knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
-
-After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
-
-We recommend using the Azure portal to validate output creation. The workflow is:
-
-1. Check the indexer for success or failure messages. Connection or quota errors appear here.
-1. Check the index for searchable content. Use Search Explorer to run queries.
-1. Check the skillset to learn how your content is chunked and optionally vectorized.
-1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-For any knowledge base that specifies an indexed OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-> [!TIP]
-> To enforce document-level permissions, set `IngestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using C#](knowledge-source-delete-csharp.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Indexed OneLakeナレッジソースに関するC#ドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchにおける「Indexed OneLakeナレッジソース」に関連するC#ドキュメントが完全に削除されたことを示しています。199行の内容が削除され、Indexed OneLakeナレッジソースの作成、使用方法、サンプルコード、前提条件などの重要な情報が失われました。

削除された内容には、OneLakeナレッジソースを使用してMicrosoft OneLakeのファイルをインデックス化し、クエリを実行する方法が含まれていました。また、ナレッジソースの作成に必要な元情報やパラメータ、生成されるオブジェクト、使用サポート、関連するAPIなどの詳細が記載されていました。

これにより、該当するナレッジソースを利用する開発者にとって重要な情報源が欠落することになり、他のリソースを探す必要が出てくるかもしれません。この変更は、よくあるドキュメントの整理や冗長性の排除を目的とする場合がありますが、ユーザーにとっては利用可能な情報が減少することを意味します。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-python.md{#item-c7d61d}

<details>
<summary>Diff</summary>
````diff
@@ -1,188 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-Use an *indexed OneLake knowledge source* to index and query Microsoft OneLake files in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-When you create an indexed OneLake knowledge source, you specify an external data source, models, and properties to automatically generate the following Azure AI Search objects:
-
-+ A data source that represents a lakehouse.
-+ A skillset that chunks and optionally vectorizes multimodal content from the lakehouse.
-+ An index that stores enriched content and meets the criteria for agentic retrieval.
-+ An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
-
-The generated indexer conforms to the *OneLake indexer*, whose prerequisites, supported tasks, supported document formats, supported shortcuts, and limitations also apply to OneLake knowledge sources. For more information, see the [OneLake indexer documentation](../../search-how-to-index-onelake-files.md).
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
-
-+ Completion of the [OneLake indexer prerequisites](../../search-how-to-index-onelake-files.md#prerequisites).
-
-+ Completion of the [OneLake indexer data preparation](../../search-how-to-index-onelake-files.md#prepare-data-for-indexing).
-
-+ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using Python](knowledge-source-check-python.md)]
-
-The following JSON is an example response for an indexed OneLake knowledge source.
-
-```json
-{
-  "name": "my-onelake-ks",
-  "kind": "indexedOneLake",
-  "description": "A sample indexed OneLake knowledge source.",
-  "encryptionKey": null,
-  "indexedOneLakeParameters": {
-    "fabricWorkspaceId": "<REDACTED>",
-    "lakehouseId": "<REDACTED>",
-    "targetPath": null,
-    "ingestionParameters": {
-      "disableImageVerbalization": false,
-      "ingestionPermissionOptions": [],
-      "contentExtractionMode": "standard",
-      "identity": null,
-      "embeddingModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<REDACTED>",
-          "deploymentId": "text-embedding-3-large",
-          "apiKey": "<REDACTED>",
-          "modelName": "text-embedding-3-large"
-        }
-      },
-      "chatCompletionModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<REDACTED>",
-          "deploymentId": "gpt-5-mini",
-          "apiKey": "<REDACTED>",
-          "modelName": "gpt-5-mini"
-        }
-      },
-      "ingestionSchedule": null,
-      "aiServices": {
-        "uri": "<REDACTED>",
-        "apiKey": "<REDACTED>"
-      }
-    },
-    "createdResources": {
-    "datasource": "my-onelake-ks-datasource",
-    "indexer": "my-onelake-ks-indexer",
-    "skillset": "my-onelake-ks-skillset",
-    "index": "my-onelake-ks-index"
-    }
-  }
-}
-```
-
-> [!NOTE]
-> Sensitive information is redacted. The generated resources appear at the end of the response.
-
-## Create a knowledge source
-
-Run the following code to create an indexed OneLake knowledge source.
-
-```python
-# Create an indexed OneLake knowledge source
-from azure.core.credentials import AzureKeyCredential
-from azure.search.documents.indexes import SearchIndexClient
-from azure.search.documents.indexes.models import IndexedOneLakeKnowledgeSource, IndexedOneLakeKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceAzureOpenAIVectorizer, KnowledgeSourceContentExtractionMode, KnowledgeSourceIngestionParameters
-
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
-
-knowledge_source = IndexedOneLakeKnowledgeSource(
-    name = "my-onelake-ks",
-    description= "This knowledge source pulls content from a lakehouse.",
-    encryption_key = None,
-    indexed_one_lake_parameters = IndexedOneLakeKnowledgeSourceParameters(
-        fabric_workspace_id = "fabric_workspace_id",
-        lakehouse_id = "lakehouse_id",
-        target_path = None,
-        ingestion_parameters = KnowledgeSourceIngestionParameters(
-            identity = None,
-            disable_image_verbalization = False,
-            chat_completion_model = KnowledgeBaseAzureOpenAIModel(
-                azure_open_ai_parameters = AzureOpenAIVectorizerParameters(
-                    # TRIMMED FOR BREVITY
-                )
-            ),
-            embedding_model = KnowledgeSourceAzureOpenAIVectorizer(
-                azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
-                    # TRIMMED FOR BREVITY
-                )
-            ),
-            content_extraction_mode = KnowledgeSourceContentExtractionMode.MINIMAL,
-            ingestion_schedule = None,
-            ingestion_permission_options = None
-        )
-    )
-)
-
-index_client.create_or_update_knowledge_source(knowledge_source)
-print(f"Knowledge source '{knowledge_source.name}' created or updated successfully.")
-```
-
-### Source-specific properties
-
-You can pass the following properties to create an indexed OneLake knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | Yes | Yes |
-| `description` | A description of the knowledge source. | String | Yes | No |
-| `encryption` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
-| `indexed_one_lake_parameters` | Parameters specific to OneLake knowledge sources: `fabric_workspace_id`, `lakehouse_id`, and `target_path`. | Object |  | Yes |
-| `fabric_workspace_id` | The GUID of the workspace that contains the lakehouse. | String | No | Yes |
-| `lakehouse_id` | The GUID of the lakehouse. | String | No | Yes |
-| `target_path` | A folder or shortcut within the lakehouse. When unspecified, the entire lakehouse is indexed. | String | No | No |
-
-### `ingestionParameters` properties
-
-[!INCLUDE [Python ingestionParameters properties](knowledge-source-ingestion-parameters-python.md)]
-
-## Check ingestion status
-
-[!INCLUDE [Python knowledge source status](knowledge-source-status-python.md)]
-
-## Review the created objects
-
-When you create an indexed OneLake knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
-
-After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
-
-We recommend using the Azure portal to validate output creation. The workflow is:
-
-1. Check the indexer for success or failure messages. Connection or quota errors appear here.
-1. Check the index for searchable content. Use Search Explorer to run queries.
-1. Check the skillset to learn how your content is chunked and optionally vectorized.
-1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-For any knowledge base that specifies an indexed OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-> [!TIP]
-> To enforce document-level permissions, set `ingestion_permission_options` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using Python](knowledge-source-delete-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Indexed OneLakeナレッジソースに関するPythonドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchの「Indexed OneLakeナレッジソース」に関連するPythonドキュメントが完全に削除されたことを示しています。188行の内容が削除され、Indexed OneLakeナレッジソースの作成方法、サンプルコード、前提条件、使用に関する詳細が失われました。

削除された内容には、OneLakeナレッジソースを使用してMicrosoft OneLakeのファイルをインデックス化し、クエリを実行するための手順が含まれており、具体的なAPIの使用方法や、必要となる設定、さらに生成されるインデックスやスキルセットに関する情報も提供されていました。

この変更により、Pythonを使用してIndexed OneLakeナレッジソースを操作しようとする開発者にとって、重要なリソースが不足することになり、他の文書やリソースを探す必要が出てくるかもしれません。この変更はドキュメントの整理の一環と捉えられますが、ユーザーには新たに情報を探す負担を強いることとなります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-rest.md{#item-876f49}

<details>
<summary>Diff</summary>
````diff
@@ -1,176 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-Use an *indexed OneLake knowledge source* to index and query Microsoft OneLake files in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-When you create an indexed OneLake knowledge source, you specify an external data source, models, and properties to automatically generate the following Azure AI Search objects:
-
-+ A data source that represents a lakehouse.
-+ A skillset that chunks and optionally vectorizes multimodal content from the lakehouse.
-+ An index that stores enriched content and meets the criteria for agentic retrieval.
-+ An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
-
-The generated indexer conforms to the *OneLake indexer*, whose prerequisites, supported tasks, supported document formats, supported shortcuts, and limitations also apply to OneLake knowledge sources. For more information, see the [OneLake indexer documentation](../../search-how-to-index-onelake-files.md).
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
-
-+ Completion of the [OneLake indexer prerequisites](../../search-how-to-index-onelake-files.md#prerequisites).
-
-+ Completion of the [OneLake indexer data preparation](../../search-how-to-index-onelake-files.md#prepare-data-for-indexing).
-
-+ The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using REST](knowledge-source-check-rest.md)]
-
-The following JSON is an example response for an indexed OneLake knowledge source.
-
-```json
-{
-  "name": "my-onelake-ks",
-  "kind": "indexedOneLake",
-  "description": "A sample indexed OneLake knowledge source.",
-  "encryptionKey": null,
-  "indexedOneLakeParameters": {
-    "fabricWorkspaceId": "<REDACTED>",
-    "lakehouseId": "<REDACTED>",
-    "targetPath": null,
-    "ingestionParameters": {
-      "disableImageVerbalization": false,
-      "ingestionPermissionOptions": [],
-      "contentExtractionMode": "standard",
-      "identity": null,
-      "embeddingModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<REDACTED>",
-          "deploymentId": "text-embedding-3-large",
-          "apiKey": "<REDACTED>",
-          "modelName": "text-embedding-3-large"
-        }
-      },
-      "chatCompletionModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<REDACTED>",
-          "deploymentId": "gpt-5-mini",
-          "apiKey": "<REDACTED>",
-          "modelName": "gpt-5-mini"
-        }
-      },
-      "ingestionSchedule": null,
-      "aiServices": {
-        "uri": "<REDACTED>",
-        "apiKey": "<REDACTED>"
-      }
-    },
-    "createdResources": {
-    "datasource": "my-onelake-ks-datasource",
-    "indexer": "my-onelake-ks-indexer",
-    "skillset": "my-onelake-ks-skillset",
-    "index": "my-onelake-ks-index"
-    }
-  }
-}
-```
-
-> [!NOTE]
-> Sensitive information is redacted. The generated resources appear at the end of the response.
-
-## Create a knowledge source
-
-Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create an indexed OneLake knowledge source.
-
-```http
-PUT {{search-url}}/knowledgesources/my-onelake-ks?api-version=2025-11-01-preview
-api-key: {{api-key}}
-Content-Type: application/json
-
-{
-    "name": "my-onelake-ks",
-    "kind": "indexedOneLake",
-    "description": "This knowledge source pulls content from a lakehouse.",
-    "indexedOneLakeParameters": {
-      "fabricWorkspaceId": "<YOUR FABRIC WORKSPACE GUID>",
-      "lakehouseId": "<YOUR LAKEHOUSE GUID>",
-      "targetPath": null,
-      "ingestionParameters": {
-        "identity": null,
-        "disableImageVerbalization": null,
-        "chatCompletionModel": { TRIMMED FOR BREVITY },
-        "embeddingModel": { TRIMMED FOR BREVITY },
-        "contentExtractionMode": "minimal",
-        "ingestionSchedule": null,
-        "ingestionPermissionOptions": []
-    }
-  }
-}
-```
-
-### Source-specific properties
-
-You can pass the following properties to create an indexed OneLake knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | Yes | Yes |
-| `kind` | The kind of knowledge source, which is `indexedOneLake` in this case. | String | No | Yes |
-| `description` | A description of the knowledge source. | String | Yes | No |
-| `encryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
-| `indexedOneLakeParameters` | Parameters specific to OneLake knowledge sources: `fabricWorkspaceId`, `lakehouseId`, and `targetPath`. | Object |  | Yes |
-| `fabricWorkspaceId` | The GUID of the workspace that contains the lakehouse. | String | No | Yes |
-| `lakehouseId` | The GUID of the lakehouse. | String | No | Yes |
-| `targetPath` | A folder or shortcut within the lakehouse. When unspecified, the entire lakehouse is indexed. | String | No | No |
-
-### `ingestionParameters` properties
-
-[!INCLUDE [REST ingestionParameters properties](knowledge-source-ingestion-parameters-rest.md)]
-
-## Check ingestion status
-
-[!INCLUDE [REST knowledge source status](knowledge-source-status-rest.md)]
-
-## Review the created objects
-
-When you create an indexed OneLake knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
-
-After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
-
-We recommend using the Azure portal to validate output creation. The workflow is:
-
-1. Check the indexer for success or failure messages. Connection or quota errors appear here.
-1. Check the index for searchable content. Use Search Explorer to run queries.
-1. Check the skillset to learn how your content is chunked and optionally vectorized.
-1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-For any knowledge base that specifies an indexed OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-> [!TIP]
-> To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using REST](knowledge-source-delete-rest.md)]
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Indexed OneLakeナレッジソースに関するREST APIドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchにおける「Indexed OneLakeナレッジソース」に関連するREST APIドキュメントが完全に削除されたことを示しています。176行の内容が削除され、Indexed OneLakeナレッジソースの作成、使用方法、サンプルHTTPリクエスト、前提条件、関連するAPIに関する重要な情報が失われました。

削除された内容には、Microsoft OneLake内のファイルをインデックス化およびクエリ実行するために使われるナレッジソースの詳細が含まれていました。また、REST APIを使用してナレッジソースを作成するための具体的な手順や、必要なパラメータ、生成されるインデックスやスキルセットに関する情報も提供されていました。

この変更により、Indexed OneLakeナレッジソースを操作する開発者にとって、必要な情報が不足することになり、他のドキュメントやリソースを参照する必要があります。この削除は、ドキュメントの整理や更新の一環として実施されることが一般的ですが、ユーザーには新たに情報を探す負担がかかる可能性があります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-csharp.md{#item-d3510c}

<details>
<summary>Diff</summary>
````diff
@@ -1,101 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-A *search index knowledge source* specifies a connection to an Azure AI Search index that provides searchable content in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). 
-
-+ A search index containing plain text or vector content with a semantic configuration. [Review the index criteria for agentic retrieval](../../agentic-retrieval-how-to-create-index.md#criteria-for-agentic-retrieval). The index must be on the same search service as the knowledge base.
-
-+ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using C#](knowledge-source-check-csharp.md)]
-
-The following JSON is an example response for a search index knowledge source. Notice that the knowledge source specifies a single index name and which fields in the index to include in the query.
-
-```json
-{
-  "SearchIndexParameters": {
-    "SearchIndexName": "earth-at-night",
-    "SourceDataFields": [
-      {
-        "Name": "id"
-      },
-      {
-        "Name": "page_chunk"
-      },
-      {
-        "Name": "page_number"
-      }
-    ],
-    "SearchFields": [],
-    "SemanticConfigurationName": "semantic-config"
-  },
-  "Name": "earth-knowledge-source",
-  "Description": null,
-  "EncryptionKey": null,
-  "ETag": "<redacted>"
-}
-```
-
-## Create a knowledge source
-
-Run the following code to create a search index knowledge source.
-
-```csharp
-using Azure.Search.Documents.Indexes.Models;
-
-// Create the knowledge source
-var indexKnowledgeSource = new SearchIndexKnowledgeSource(
-    name: knowledgeSourceName,
-    searchIndexParameters: new SearchIndexKnowledgeSourceParameters(searchIndexName: indexName)
-    {
-        SourceDataFields = { new SearchIndexFieldReference(name: "id"), new SearchIndexFieldReference(name: "page_chunk"), new SearchIndexFieldReference(name: "page_number") }
-    }
-);
-
-await indexClient.CreateOrUpdateKnowledgeSourceAsync(indexKnowledgeSource);
-Console.WriteLine($"Knowledge source '{knowledgeSourceName}' created or updated successfully.");
-```
-
-### Source-specific properties
-
-You can pass the following properties to create a search index knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `Name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
-| `Description` | A description of the knowledge source. | String | Yes | No |
-| `EncryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
-| `SearchIndexParameters` | Parameters specific to search index knowledge sources: `search_index_name`, `SemanticConfigurationName`, `SourceDataFields`, and `SearchFields`. | Object | Yes | Yes |
-| `SearchIndexName` | The name of the existing search index. | String | Yes | Yes |
-| `SemanticConfigurationName` | Overrides the default semantic configuration for the search index. | String | Yes | No |
-| `SourceDataFields` | The index fields returned when you specify `include_reference_source_data` in the knowledge base definition. These fields are used for citations and should be `retrievable`. Examples include the document name, file name, page numbers, or chapter numbers. | Array | Yes | No |
-| `SearchFields` | The index fields to specifically search against. When unspecified, all fields are searched. | Array | Yes | No |
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using Python](knowledge-source-delete-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Search Indexナレッジソースに関するC#ドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchにおける「Search Indexナレッジソース」に関連するC#ドキュメントが完全に削除されたことを示しています。101行の内容が削除され、Search Indexナレッジソースの作成、使用方法、必要な前提条件、サンプルコード、及び構成パラメータについての詳細な情報が失われました。

削除された内容には、Azure AI Searchインデックスに接続するための手順や、インデックス内の特定のフィールドをクエリに含める方法に関する具体的な情報が含まれていました。また、ナレッジソースを作成するために使用する必要なパラメータや、インデックスの使用方法についても詳細に説明されていました。

この変更により、C#を使用してSearch Indexナレッジソースを操作しようとする開発者にとって重要な参考資料が失われ、他のドキュメントやリソースを模索する必要が出てくる可能性があります。この削除はドキュメントの整理や更新の一環として行われたと考えられますが、ユーザーには新たな情報源を見つける手間が増えることになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-python.md{#item-58056f}

<details>
<summary>Diff</summary>
````diff
@@ -1,105 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-A *search index knowledge source* specifies a connection to an Azure AI Search index that provides searchable content in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). 
-
-+ A search index containing plain text or vector content with a semantic configuration. [Review the index criteria for agentic retrieval](../../agentic-retrieval-how-to-create-index.md#criteria-for-agentic-retrieval). The index must be on the same search service as the knowledge base.
-
-+ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using Python](knowledge-source-check-python.md)]
-
-The following JSON is an example response for a search index knowledge source. Notice that the knowledge source specifies a single index name and which fields in the index to include in the query.
-
-```json
-{
-
-  "name": "my-search-index-ks",
-  "kind": "searchIndex",
-  "description": "A sample search index knowledge source.",
-  "encryptionKey": null,
-  "searchIndexParameters": {
-    "searchIndexName": "my-search-index",
-    "semanticConfigurationName": null,
-    "sourceDataFields": [],
-    "searchFields": []
-  }
-}
-```
-
-## Create a knowledge source
-
-Run the following code to create a search index knowledge source.
-
-```python
-# Create a search index knowledge source
-from azure.core.credentials import AzureKeyCredential
-from azure.search.documents.indexes import SearchIndexClient
-from azure.search.documents.indexes.models import SearchIndexKnowledgeSource, SearchIndexKnowledgeSourceParameters, SearchIndexFieldReference
-
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
-
-knowledge_source = SearchIndexKnowledgeSource(
-    name = "my-search-index-ks",
-    description= "This knowledge source pulls from an existing index designed for agentic retrieval.",
-    encryption_key = None,
-    search_index_parameters = SearchIndexKnowledgeSourceParameters(
-        search_index_name = "search_index_name",
-        semantic_configuration_name = "semantic_configuration_name",
-        source_data_fields = [
-            SearchIndexFieldReference(name="description"),
-            SearchIndexFieldReference(name="category"),
-        ],
-        search_fields = [
-            SearchIndexFieldReference(name="id")
-        ],
-    )
-)
-
-index_client.create_or_update_knowledge_source(knowledge_source)
-print(f"Knowledge source '{knowledge_source.name}' created or updated successfully.")
-```
-
-### Source-specific properties
-
-You can pass the following properties to create a search index knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
-| `description` | A description of the knowledge source. | String | Yes | No |
-| `encryption_key` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
-| `search_index_parameters` | Parameters specific to search index knowledge sources: `search_index_name`, `semantic_configuration_name`, `source_data_fields`, and `search_fields`. | Object | Yes | Yes |
-| `search_index_name` | The name of the existing search index. | String | Yes | Yes |
-| `semantic_configuration_name` | Overrides the default semantic configuration for the search index. | String | Yes | No |
-| `source_data_fields` | The index fields returned when you specify `include_reference_source_data` in the knowledge base definition. These fields are used for citations and should be `retrievable`. Examples include the document name, file name, page numbers, or chapter numbers. | Array | Yes | No |
-| `search_fields` | The index fields to specifically search against. When unspecified, all fields are searched. | Array | Yes | No |
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using Python](knowledge-source-delete-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Search Indexナレッジソースに関するPythonドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchにおける「Search Indexナレッジソース」に関連するPythonドキュメントが完全に削除されたことを示しています。105行の内容が削除され、Search Indexナレッジソースの作成、使用方法、必要な前提条件、サンプルコード、及び構成パラメータに関する重要な情報が失われました。

削除された内容には、Azure AI Searchインデックスに接続するための具体的な手順や、インデックスからデータを取得する方法に関する詳細が含まれていました。また、ナレッジソースを作成するためのPythonコードのサンプルや、使用するべきパラメータに関する情報も提供されていました。

この変更により、Pythonを使ってSearch Indexナレッジソースを操作しようとする開発者にとって重要な参考資料が失われることになり、他のドキュメントやリソースを探さなければならなくなる可能性があります。この削除はドキュメントの整理や更新の一環として行われたと考えられますが、ユーザーには新たな情報を求める負担がかかることになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-rest.md{#item-e95367}

<details>
<summary>Diff</summary>
````diff
@@ -1,98 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 04/10/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-A *search index knowledge source* specifies a connection to an Azure AI Search index that provides searchable content in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). 
-
-+ A search index containing plain text or vector content with a semantic configuration. Review the [index criteria for agentic retrieval](../../agentic-retrieval-how-to-create-index.md#criteria-for-agentic-retrieval). The index must be on the same search service as the knowledge base.
-
-+ The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using REST](knowledge-source-check-rest.md)]
-
-The following JSON is an example response for a search index knowledge source. Notice that the knowledge source specifies a single index name and which fields in the index to include in the query.
-
-```json
-{
-
-  "name": "my-search-index-ks",
-  "kind": "searchIndex",
-  "description": "A sample search index knowledge source.",
-  "encryptionKey": null,
-  "searchIndexParameters": {
-    "searchIndexName": "my-search-index",
-    "semanticConfigurationName": null,
-    "sourceDataFields": [],
-    "searchFields": []
-  }
-}
-```
-
-## Create a knowledge source
-
-Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create a search index knowledge source.
-
-```http
-POST {{search-url}}/knowledgesources/my-search-index-ks?api-version=2025-11-01-preview
-api-key: {{api-key}}
-Content-Type: application/json
-
-{
-    "name": "my-search-index-ks",
-    "kind": "searchIndex",
-    "description": "This knowledge source pulls from an existing index designed for agentic retrieval.",
-    "encryptionKey": null,
-    "searchIndexParameters": {
-        "searchIndexName": "<YOUR INDEX NAME>",
-        "semanticConfigurationName": "my-semantic-config",
-        "sourceDataFields": [
-          { "name": "description" },
-          { "name": "category" }
-        ]
-    }
-}
-```
-
-### Source-specific properties
-
-You can pass the following properties to create a search index knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
-| `kind` | The kind of knowledge source, which is `searchIndex` in this case. | String | No | Yes |
-| `description` | A description of the knowledge source. | String | Yes | No |
-| `encryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
-| `searchIndexParameters` | Parameters specific to search index knowledge sources: `searchIndexName`, `semanticConfigurationName`, `sourceDataFields`, and `searchFields`. | Object | Yes | Yes |
-| `searchIndexName` | The name of the existing search index. | String | Yes | Yes |
-| `semanticConfigurationName` | Overrides the default semantic configuration for the search index. | String | Yes | No |
-| `sourceDataFields` | The index fields returned when you specify `includeReferenceSourceData` in the knowledge base definition. These fields are used for citations and should be `retrievable`. Examples include the document name, file name, page numbers, or chapter numbers. | Array | Yes | No |
-| `searchFields` | The index fields to specifically search against. When unspecified, all fields are searched. | Array | Yes | No |
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using REST](knowledge-source-delete-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Search Indexナレッジソースに関するREST APIドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchにおける「Search Indexナレッジソース」に関連するREST APIドキュメントが完全に削除されたことを示しています。98行の内容が削除され、Search Indexナレッジソースの作成方法、使用方法、前提条件、サンプルコード、及び関連するプロパティに関する詳細な情報が失われました。

削除された内容には、Azure AI Searchインデックスとの接続方法、REST APIを使用したナレッジソースの作成手順、必要なパラメータ、サンプルリクエストに関する具体的な情報が含まれていました。また、ナレッジソースを作成するために必要なフィールドやそれらの詳細な説明も提供されていました。

この変更により、REST APIを使用してSearch Indexナレッジソースを操作しようとする開発者にとって非常に重要なリファレンスが失われ、代わりに他のドキュメントやリソースを探さなければならなくなる可能性があります。この削除はドキュメントの整理や更新の一環として行われたと考えられますが、ユーザーには新たな情報を見つけるための負担が増加することになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-csharp.md{#item-2eb305}

<details>
<summary>Diff</summary>
````diff
@@ -1,193 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-Use an *indexed SharePoint knowledge source* to index and query SharePoint content in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-When you create an indexed SharePoint knowledge source, you specify a SharePoint connection string, models, and properties to automatically generate the following Azure AI Search objects:
-
-+ A data source that points to SharePoint sites.
-+ A skillset that chunks and optionally vectorizes multimodal content.
-+ An index that stores enriched content and meets the criteria for agentic retrieval.
-+ An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
-
-+ Completion of the [SharePoint indexer prerequisites](../../search-how-to-index-sharepoint-online.md#prerequisites).
-
-+ Completion of the following SharePoint indexer configuration steps:
-
-  + [Step 1: Enable a managed identity for Azure AI Search](../../search-how-to-index-sharepoint-online.md#step-1-optional-enable-system-assigned-managed-identity) (required only for secretless authentication; skip if using a client secret)
-  + [Step 2: Choose either delegated or application permissions](../../search-how-to-index-sharepoint-online.md#step-2-decide-which-permissions-the-indexer-requires)
-  + [Step 3: Create a Microsoft Entra application registration](../../search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration) (for application permissions, you also configure a [client secret](../../search-how-to-index-sharepoint-online.md#using-client-secret) or [secretless authentication](../../search-how-to-index-sharepoint-online.md#using-secretless-authentication-to-obtain-application-tokens))
-
-+ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using C#](knowledge-source-check-csharp.md)]
-
-The following JSON is an example response for an indexed SharePoint knowledge source.
-
-```json
-{
-  "name": "my-indexed-sharepoint-ks",
-  "kind": "indexedSharePoint",
-  "description": "A sample indexed SharePoint knowledge source",
-  "encryptionKey": null,
-  "indexedSharePointParameters": {
-    "connectionString": "<redacted>",
-    "containerName": "defaultSiteLibrary",
-    "query": null,
-    "ingestionParameters": {
-      "disableImageVerbalization": false,
-      "ingestionPermissionOptions": [],
-      "contentExtractionMode": "minimal",
-      "identity": null,
-      "embeddingModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<redacted>",
-          "deploymentId": "text-embedding-3-large",
-          "apiKey": "<redacted>",
-          "modelName": "text-embedding-3-large",
-          "authIdentity": null
-        }
-      },
-      "chatCompletionModel": null,
-      "ingestionSchedule": null,
-      "assetStore": null,
-      "aiServices": null
-    },
-    "createdResources": {
-      "datasource": "my-indexed-sharepoint-ks-datasource",
-      "indexer": "my-indexed-sharepoint-ks-indexer",
-      "skillset": "my-indexed-sharepoint-ks-skillset",
-      "index": "my-indexed-sharepoint-ks-index"
-    }
-  },
-  "indexedOneLakeParameters": null
-}
-```
-
-> [!NOTE]
-> Sensitive information is redacted. The generated resources appear at the end of the response.
-
-## Create a knowledge source
-
-Run the following code to create an indexed SharePoint knowledge source.
-
-```csharp
-// Create an IndexedSharePoint knowledge source
-using Azure.Search.Documents.Indexes;
-using Azure.Search.Documents.Indexes.Models;
-using Azure.Search.Documents.KnowledgeBases.Models;
-using Azure;
-
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
-
-var chatCompletionParams = new AzureOpenAIVectorizerParameters
-{
-    ResourceUri = new Uri(aoaiEndpoint),
-    DeploymentName = aoaiGptDeployment,
-    ModelName = aoaiGptModel
-};
-
-var embeddingParams = new AzureOpenAIVectorizerParameters
-{
-    ResourceUri = new Uri(aoaiEndpoint),
-    DeploymentName = aoaiEmbeddingDeployment,
-    ModelName = aoaiEmbeddingModel
-};
-
-var ingestionParams = new KnowledgeSourceIngestionParameters
-{
-    DisableImageVerbalization = false,
-    ChatCompletionModel = new KnowledgeBaseAzureOpenAIModel(azureOpenAIParameters: chatCompletionParams),
-    EmbeddingModel = new KnowledgeSourceAzureOpenAIVectorizer
-    {
-        AzureOpenAIParameters = embeddingParams
-    }
-};
-
-var sharePointParams = new IndexedSharePointKnowledgeSourceParameters(
-    connectionString: sharePointConnectionString,
-    containerName: "defaultSiteLibrary")
-{
-    IngestionParameters = ingestionParams
-};
-
-var knowledgeSource = new IndexedSharePointKnowledgeSource(
-    name: "my-indexed-sharepoint-ks",
-    indexedSharePointParameters: sharePointParams)
-{
-    Description = "A sample indexed SharePoint knowledge source."
-};
-
-await indexClient.CreateOrUpdateKnowledgeSourceAsync(knowledgeSource);
-Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated successfully.");
-```
-
-### Source-specific properties
-
-You can pass the following properties to create an indexed SharePoint knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `Name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
-| `Description` | A description of the knowledge source. | String | Yes | No |
-| `EncryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
-| `IndexedSharePointKnowledgeSourceParameters` | Parameters specific to indexed SharePoint knowledge sources: `connectionString`, `containerName`, and `query`. | Object | No | No |
-| `connectionString` | The connection string to a SharePoint site. For more information, see [Connection string syntax](../../search-how-to-index-sharepoint-online.md#connection-string-format). | String | Yes | Yes |
-| `containerName` | The SharePoint library to access. Use `defaultSiteLibrary` to index content from the site's default document library or `allSiteLibraries` to index content from every document library in the site. Ignore `useQuery` for now. | String | No | Yes |
-| `query` | Optional [query](../../search-how-to-index-sharepoint-online.md#query) to filter SharePoint content. | String | Yes | No |
-
-### `ingestion_parameters` properties
-
-[!INCLUDE [C# ingestionParameters properties](knowledge-source-ingestion-parameters-csharp.md)]
-
-## Check ingestion status
-
-[!INCLUDE [C# knowledge source status](knowledge-source-status-csharp.md)]
-
-## Review the created objects
-
-When you create an indexed SharePoint knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
-
-After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
-
-We recommend using the Azure portal to validate output creation. The workflow is:
-
-1. Check the indexer for success or failure messages. Connection or quota errors appear here.
-1. Check the index for searchable content. Use Search Explorer to run queries.
-1. Check the skillset to learn how your content is chunked and optionally vectorized.
-1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-For any knowledge base that specifies an indexed SharePoint knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-> [!TIP]
-> To enforce document-level permissions, set `IngestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using C#](knowledge-source-delete-csharp.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "SharePointインデックスに関するC#ドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchにおける「SharePointインデックス」に関連するC#ドキュメントが完全に削除されたことを示しています。193行の内容が削除され、SharePoint情報をインデックスおよびクエリするための重要な情報や手順が失われました。

削除された内容には、インデックスされたSharePointナレッジソースを作成するための手順や、必要な前提条件、具体的なC#コードのサンプルが含まれていました。また、サンプルレスポンスのJSON構造、インデックス設定の詳細、及び作成されたオブジェクトやその属性についての情報も提供されていました。

この変更により、C#を利用してSharePointのデータを扱う開発者にとって非常に重要なリファレンスが失われ、他のドキュメントやリソースを探す必要が生じる可能性があります。この削除はドキュメントの整理やアップデートの一環として行われた可能性がありますが、ユーザーには新たな情報を見つけるための負担がかかります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-python.md{#item-923abb}

<details>
<summary>Diff</summary>
````diff
@@ -1,182 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-Use an *indexed SharePoint knowledge source* to index and query SharePoint content in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-When you create an indexed SharePoint knowledge source, you specify a SharePoint connection string, models, and properties to automatically generate the following Azure AI Search objects:
-
-+ A data source that points to SharePoint sites.
-+ A skillset that chunks and optionally vectorizes multimodal content.
-+ An index that stores enriched content and meets the criteria for agentic retrieval.
-+ An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
-
-+ Completion of the [SharePoint indexer prerequisites](../../search-how-to-index-sharepoint-online.md#prerequisites).
-
-+ Completion of the following SharePoint indexer configuration steps:
-
-  + [Step 1: Enable a managed identity for Azure AI Search](../../search-how-to-index-sharepoint-online.md#step-1-optional-enable-system-assigned-managed-identity) (required only for secretless authentication; skip if using a client secret)
-  + [Step 2: Choose either delegated or application permissions](../../search-how-to-index-sharepoint-online.md#step-2-decide-which-permissions-the-indexer-requires)
-  + [Step 3: Create a Microsoft Entra application registration](../../search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration) (for application permissions, you also configure a [client secret](../../search-how-to-index-sharepoint-online.md#using-client-secret) or [secretless authentication](../../search-how-to-index-sharepoint-online.md#using-secretless-authentication-to-obtain-application-tokens))
-
-+ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using Python](knowledge-source-check-python.md)]
-
-The following JSON is an example response for an indexed SharePoint knowledge source.
-
-```json
-{
-  "name": "my-indexed-sharepoint-ks",
-  "kind": "indexedSharePoint",
-  "description": "A sample indexed SharePoint knowledge source",
-  "encryptionKey": null,
-  "indexedSharePointParameters": {
-    "connectionString": "<redacted>",
-    "containerName": "defaultSiteLibrary",
-    "query": null,
-    "ingestionParameters": {
-      "disableImageVerbalization": false,
-      "ingestionPermissionOptions": [],
-      "contentExtractionMode": "minimal",
-      "identity": null,
-      "embeddingModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<redacted>",
-          "deploymentId": "text-embedding-3-large",
-          "apiKey": "<redacted>",
-          "modelName": "text-embedding-3-large",
-          "authIdentity": null
-        }
-      },
-      "chatCompletionModel": null,
-      "ingestionSchedule": null,
-      "assetStore": null,
-      "aiServices": null
-    },
-    "createdResources": {
-      "datasource": "my-indexed-sharepoint-ks-datasource",
-      "indexer": "my-indexed-sharepoint-ks-indexer",
-      "skillset": "my-indexed-sharepoint-ks-skillset",
-      "index": "my-indexed-sharepoint-ks-index"
-    }
-  },
-  "indexedOneLakeParameters": null
-}
-```
-
-> [!NOTE]
-> Sensitive information is redacted. The generated resources appear at the end of the response.
-
-## Create a knowledge source
-
-Run the following code to create an indexed SharePoint knowledge source.
-
-```python
-# Create an indexed SharePoint knowledge source
-from azure.core.credentials import AzureKeyCredential
-from azure.search.documents.indexes import SearchIndexClient
-from azure.search.documents.indexes.models import IndexedSharePointKnowledgeSource, IndexedSharePointKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceAzureOpenAIVectorizer, KnowledgeSourceContentExtractionMode, KnowledgeSourceIngestionParameters
-
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
-
-knowledge_source = IndexedSharePointKnowledgeSource(
-    name = "my-indexed-sharepoint-ks",
-    description = "A sample indexed SharePoint knowledge source.",
-    encryption_key = None,
-    indexed_share_point_parameters = IndexedSharePointKnowledgeSourceParameters(
-        connection_string = "connection_string",
-        container_name = "defaultSiteLibrary",
-        query = None,
-        ingestion_parameters = KnowledgeSourceIngestionParameters(
-            identity = None,
-            disable_image_verbalization = False,
-            chat_completion_model = KnowledgeBaseAzureOpenAIModel(
-                azure_open_ai_parameters = AzureOpenAIVectorizerParameters(
-                    # TRIMMED FOR BREVITY
-                )
-            ),
-            embedding_model = KnowledgeSourceAzureOpenAIVectorizer(
-                azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
-                    # TRIMMED FOR BREVITY
-                )
-            ),
-            content_extraction_mode = KnowledgeSourceContentExtractionMode.MINIMAL,
-            ingestion_schedule = None,
-            ingestion_permission_options = None
-        )
-    )
-)
-
-index_client.create_or_update_knowledge_source(knowledge_source)
-print(f"Knowledge source '{knowledge_source.name}' created or updated successfully.")
-```
-
-### Source-specific properties
-
-You can pass the following properties to create an indexed SharePoint knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
-| `description` | A description of the knowledge source. | String | Yes | No |
-| `encryption_key` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
-| `indexed_share_point_parameters` | Parameters specific to indexed SharePoint knowledge sources: `connection_string`, `container_name`, and `query`. | Object | No | No |
-| `connection_string` | The connection string to a SharePoint site. For more information, see [Connection string syntax](../../search-how-to-index-sharepoint-online.md#connection-string-format). | String | Yes | Yes |
-| `container_name` | The SharePoint library to access. Use `defaultSiteLibrary` to index content from the site's default document library or `allSiteLibraries` to index content from every document library in the site. Ignore `useQuery` for now. | String | No | Yes |
-| `query` | Optional [query](../../search-how-to-index-sharepoint-online.md#query) to filter SharePoint content. | String | Yes | No |
-
-### `ingestion_parameters` properties
-
-[!INCLUDE [Python ingestionParameters properties](knowledge-source-ingestion-parameters-python.md)]
-
-## Check ingestion status
-
-[!INCLUDE [Python knowledge source status](knowledge-source-status-python.md)]
-
-## Review the created objects
-
-When you create an indexed SharePoint knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
-
-After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
-
-We recommend using the Azure portal to validate output creation. The workflow is:
-
-1. Check the indexer for success or failure messages. Connection or quota errors appear here.
-1. Check the index for searchable content. Use Search Explorer to run queries.
-1. Check the skillset to learn how your content is chunked and optionally vectorized.
-1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-For any knowledge base that specifies an indexed SharePoint knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-> [!TIP]
-> To enforce document-level permissions, set `ingestion_permission_options` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using Python](knowledge-source-delete-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "SharePointインデックスに関するPythonドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchにおける「SharePointインデックス」に関連するPythonドキュメントが完全に削除されたことを示しています。182行の内容が削除され、SharePoint上のコンテンツをインデックスおよびクエリするための重要な手順や情報が失われました。

削除された内容には、インデックスされたSharePointナレッジソースを作成するためのコード例や、必要な前提条件、各パラメータの詳細な説明が含まれていました。また、作成されたオブジェクトの確認方法や、具体的なC#とPythonコードのサンプルが提供されていました。

この変更により、Pythonを利用してSharePointのデータを扱う開発者にとっての重要なリファレンスが失われ、他のドキュメントやリソースを探す必要があるかもしれません。この削除はドキュメントの整理や更新の一環として行われたと考えられますが、ユーザーにとっては必要な情報を見つけるための負担が増える結果となります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-rest.md{#item-e26ea0}

<details>
<summary>Diff</summary>
````diff
@@ -1,178 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-Use an *indexed SharePoint knowledge source* to index and query SharePoint content in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-When you create an indexed SharePoint knowledge source, you specify a SharePoint connection string, models, and properties to automatically generate the following Azure AI Search objects:
-
-+ A data source that points to SharePoint sites.
-+ A skillset that chunks and optionally vectorizes multimodal content.
-+ An index that stores enriched content and meets the criteria for agentic retrieval.
-+ An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
-
-+ Completion of the [SharePoint indexer prerequisites](../../search-how-to-index-sharepoint-online.md#prerequisites).
-
-+ Completion of the following SharePoint indexer configuration steps:
-
-  + [Step 1: Enable a managed identity for Azure AI Search](../../search-how-to-index-sharepoint-online.md#step-1-optional-enable-system-assigned-managed-identity) (required only for secretless authentication; skip if using a client secret)
-  + [Step 2: Choose either delegated or application permissions](../../search-how-to-index-sharepoint-online.md#step-2-decide-which-permissions-the-indexer-requires)
-  + [Step 3: Create a Microsoft Entra application registration](../../search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration) (for application permissions, you also configure a [client secret](../../search-how-to-index-sharepoint-online.md#using-client-secret) or [secretless authentication](../../search-how-to-index-sharepoint-online.md#using-secretless-authentication-to-obtain-application-tokens))
-
-+ The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using REST](knowledge-source-check-rest.md)]
-
-The following JSON is an example response for an indexed SharePoint knowledge source.
-
-```json
-{
-  "name": "my-indexed-sharepoint-ks",
-  "kind": "indexedSharePoint",
-  "description": "A sample indexed SharePoint knowledge source",
-  "encryptionKey": null,
-  "indexedSharePointParameters": {
-    "connectionString": "<redacted>",
-    "containerName": "defaultSiteLibrary",
-    "query": null,
-    "ingestionParameters": {
-      "disableImageVerbalization": false,
-      "ingestionPermissionOptions": [],
-      "contentExtractionMode": "minimal",
-      "identity": null,
-      "embeddingModel": {
-        "kind": "azureOpenAI",
-        "azureOpenAIParameters": {
-          "resourceUri": "<redacted>",
-          "deploymentId": "text-embedding-3-large",
-          "apiKey": "<redacted>",
-          "modelName": "text-embedding-3-large",
-          "authIdentity": null
-        }
-      },
-      "chatCompletionModel": null,
-      "ingestionSchedule": null,
-      "assetStore": null,
-      "aiServices": null
-    },
-    "createdResources": {
-      "datasource": "my-indexed-sharepoint-ks-datasource",
-      "indexer": "my-indexed-sharepoint-ks-indexer",
-      "skillset": "my-indexed-sharepoint-ks-skillset",
-      "index": "my-indexed-sharepoint-ks-index"
-    }
-  },
-  "indexedOneLakeParameters": null
-}
-```
-
-> [!NOTE]
-> Sensitive information is redacted. The generated resources appear at the end of the response.
-
-## Create a knowledge source
-
-Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create an indexed SharePoint knowledge source.
-
-```http
-POST {{search-url}}/knowledgesources/my-indexed-sharepoint-ks?api-version=2025-11-01-preview
-api-key: {{api-key}}
-Content-Type: application/json
-
-{
-    "name": "my-indexed-sharepoint-ks",
-    "kind": "indexedSharePoint",
-    "description": "A sample indexed SharePoint knowledge source.",
-    "encryptionKey": null,
-    "indexedSharePointParameters": {
-        "connectionString": "{{sharepoint-connection-string}}",
-        "containerName": "defaultSiteLibrary",
-        "query": null,
-        "ingestionParameters": {
-            "identity": null,
-            "embeddingModel": {
-                "kind": "azureOpenAI",
-                "azureOpenAIParameters": {
-                    "deploymentId": "text-embedding-3-large",
-                    "modelName": "text-embedding-3-large",
-                    "resourceUri": "{{aoai-endpoint}}",
-                    "apiKey": "{{aoai-key}}"
-                }
-            },
-            "chatCompletionModel": null,
-            "disableImageVerbalization": false,
-            "ingestionSchedule": null,
-            "ingestionPermissionOptions": [],
-            "contentExtractionMode": "minimal"
-        }
-    }
-}
-```
-
-### Source-specific properties
-
-You can pass the following properties to create an indexed SharePoint knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
-| `kind` | The kind of knowledge source, which is `indexedSharePoint` in this case. | String | No | Yes |
-| `description` | A description of the knowledge source. | String | Yes | No |
-| `encryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
-| `indexedSharePointParameters` | Parameters specific to indexed SharePoint knowledge sources: `connectionString`, `containerName`, and `query`. | Object | No | Yes |
-| `connectionString` | The connection string to a SharePoint site. For more information, see [Connection string syntax](../../search-how-to-index-sharepoint-online.md#connection-string-format). | String | Yes |No |
-| `containerName` | The SharePoint library to access. Use `defaultSiteLibrary` to index content from the site's default document library or `allSiteLibraries` to index content from every document library in the site. Ignore `useQuery` for now. | String | No | Yes |
-| `query` | Optional [query](../../search-how-to-index-sharepoint-online.md#query) to filter SharePoint content. | String | Yes | No |
-
-### `ingestionParameters` properties
-
-[!INCLUDE [REST ingestionParameters properties](knowledge-source-ingestion-parameters-rest.md)]
-
-## Check ingestion status
-
-[!INCLUDE [REST knowledge source status](knowledge-source-status-rest.md)]
-
-## Review the created objects
-
-When you create an indexed SharePoint knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
-
-After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
-
-We recommend using the Azure portal to validate output creation. The workflow is:
-
-1. Check the indexer for success or failure messages. Connection or quota errors appear here.
-1. Check the index for searchable content. Use Search Explorer to run queries.
-1. Check the skillset to learn how your content is chunked and optionally vectorized.
-1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-For any knowledge base that specifies an indexed SharePoint knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-> [!TIP]
-> To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using REST](knowledge-source-delete-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "SharePointインデックスに関するREST APIドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchに関する「SharePointインデックス」に関連するREST APIドキュメントが完全に削除されたことを示しています。178行の内容が削除され、SharePoint上のコンテンツをインデックスおよびクエリする手続きや情報が失われました。

削除された内容には、インデックスされたSharePointナレッジソースをREST APIを通じて作成するための手順や、実際のAPIリクエストの例、必要な前提条件、JSON形式でのレスポンスのサンプルが含まれていました。また、各APIエンドポイントの使用方法や、エラー処理、オブジェクトの確認方法なども詳しく説明されていました。

この変更により、REST APIを利用してSharePointのデータを扱う開発者にとっての重要なリファレンスが失われ、他の情報源を探す手間がかかる可能性があります。この削除はドキュメントの整理や改訂の一環として行われたと考えられますが、ユーザーにとっては必要な情報を見つけるための負担が増える結果となります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-csharp.md{#item-f8bed1}

<details>
<summary>Diff</summary>
````diff
@@ -1,204 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-A *remote SharePoint knowledge source* uses the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) to query textual content directly from SharePoint in Microsoft 365. No search index or connection string is needed. Only textual content is queried, and usage is billed through Microsoft 365 and a Copilot license.
-
-To limit sites or constrain search, set a [filter expression](#filter-expression-examples) to scope by URLs, date ranges, file types, and other metadata. The caller's identity must be recognized by both the Azure tenant and the Microsoft 365 tenant because the retrieval engine queries SharePoint on behalf of the user.
-
-Like any other knowledge source, you specify a remote SharePoint knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md) and use the results as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). 
-
-+ SharePoint in a Microsoft 365 tenant that's under the same Microsoft Entra ID tenant as Azure.
-
-+ A Microsoft 365 Copilot license for query-time access to SharePoint content.
-
-+ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible.
-
-## Limitations
-
-The following limitations in the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) apply to remote SharePoint knowledge sources.
-
-+ There's no support for Copilot connectors or OneDrive content. Content is retrieved from SharePoint sites only.
-
-+ Limit of 200 requests per user per hour.
-
-+ Query character limit of 1,500 characters.
-
-+ Hybrid queries are only supported for the following file extensions: .doc, .docx, .pptx, .pdf, .aspx, and .one.
-
-+ Multimodal retrieval (nontextual content, including tables, images, and charts) isn't supported.
-
-+ Maximum of 25 results from a query.
-
-+ Results are returned by Copilot Retrieval API as unordered.
-
-+ Invalid Keyword Query Language (KQL) filter expressions are ignored and the query continues to execute without the filter.
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using C#](knowledge-source-check-csharp.md)]
-
-The following JSON is an example response for a remote SharePoint knowledge source.
-
-```json
-{
-  "name": "my-sharepoint-ks",
-  "kind": "remoteSharePoint",
-  "description": "A sample remote SharePoint knowledge source",
-  "encryptionKey": null,
-  "remoteSharePointParameters": {
-    "filterExpression": "filetype:docx",
-    "containerTypeId": null,
-    "resourceMetadata": [
-      "Author",
-      "Title"
-    ]
-  }
-}
-```
-
-## Create a knowledge source
-
-Run the following code to create a remote SharePoint knowledge source.
-
-```csharp
-// Create a remote SharePoint knowledge source
-using Azure.Search.Documents.Indexes;
-using Azure.Search.Documents.Indexes.Models;
-using Azure.Search.Documents.KnowledgeBases.Models;
-using Azure;
-
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), credential);
-
-var knowledgeSource = new RemoteSharePointKnowledgeSource(name: "my-remote-sharepoint-ks")
-{
-    Description = "This knowledge source queries .docx files in a trusted Microsoft 365 tenant.",
-    RemoteSharePointParameters = new RemoteSharePointKnowledgeSourceParameters()
-    {
-        FilterExpression = "filetype:docx",
-        ResourceMetadata = { "Author", "Title" }
-    }
-};
-
-await indexClient.CreateOrUpdateKnowledgeSourceAsync(knowledgeSource);
-Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated successfully.");
-```
-
-### Source-specific properties
-
-You can pass the following properties to create a remote SharePoint knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
-| `description` | A description of the knowledge source. | String | Yes | No |
-| `encryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in the knowledge source. | Object | Yes | No |
-| `remoteSharePointParameters` | Parameters specific to remote SharePoint knowledge sources: `filterExpression`, `resourceMetadata`, and `containerTypeId`. | Object | No | No |
-| `filterExpression` | An expression written in the SharePoint [KQL](/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference), which is used to specify sites and paths to content. | String | Yes |No |
-| `resourceMetadata` | A comma-delimited list of standard metadata fields: author, file name, creation date, content type, and file type. | Array | Yes | No |
-| `containerTypeId` | Container ID for the SharePoint Embedded connection. When unspecified, SharePoint Online is used. | String | Yes | No |
-
-### Filter expression examples
-
-Not all SharePoint properties are supported in the `filterExpression`. For a list of supported properties, see the [API reference](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval). For queryable properties, see [Queryable](/graph/connecting-external-content-manage-schema#queryable).
-
-Learn more about [KQL filters](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval?pivots=graph-v1#example-7-use-filter-expressions) in the syntax reference.
-
-| Example | Filter expression |
-|---------|-------------------|
-| Filter to a single site by ID | `"filterExpression": "SiteID:\"00aa00aa-bb11-cc22-dd33-44ee44ee44ee\""` |
-| Filter to multiple sites by ID | `"filterExpression": "SiteID:\"00aa00aa-bb11-cc22-dd33-44ee44ee44ee\" OR SiteID:\"11bb11bb-cc22-dd33-ee44-55ff55ff55ff\""` |
-| Filter to files under a specific path | `"filterExpression": "Path:\"https://my-demo.sharepoint.com/sites/mysite/Shared Documents/en/mydocs\""` |
-| Filter to a specific date range | `"filterExpression": "LastModifiedTime >= 2024-07-22 AND LastModifiedTime <= 2025-01-08"` |
-| Filter to files of a specific file type | `"filterExpression": "FileExtension:\"docx\" OR FileExtension:\"pdf\" OR FileExtension:\"pptx\""` |
-| Filter to files of a specific information protection label | `"filterExpression": "InformationProtectionLabelId:\"f0ddcc93-d3c0-4993-b5cc-76b0a283e252\""` |
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-## Query a knowledge base
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query SharePoint content. Remote SharePoint has source-specific behaviors for query-time filtering, query formulation, response fields, and permissions enforcement.
-
-### Apply a KQL filter at query time
-
-You can pass a `filterExpressionAddOn` in the `knowledgeSourceParams` on the retrieve request to apply a KQL filter at query time. If you specify `filterExpressionAddOn` on the retrieve request and a `filterExpression` on the knowledge source definition, the filters are AND'd together.
-
-```csharp
-var retrievalRequest = new KnowledgeBaseRetrievalRequest();
-retrievalRequest.Messages.Add(
-    new KnowledgeBaseMessage(
-        content: new[] {
-            new KnowledgeBaseMessageTextContent("contoso product planning")
-        }
-    ) { Role = "user" }
-);
-retrievalRequest.KnowledgeSourceParams.Add(
-    new RemoteSharePointKnowledgeSourceParams("my-remote-sharepoint-ks")
-    {
-        FilterExpressionAddOn = "filetype:docx"
-    }
-);
-
-var result = await kbClient.RetrieveAsync(
-    retrievalRequest, xMsQuerySourceAuthorization: token
-);
-```
-
-### Write effective queries
-
-Queries that ask about the content itself are more effective than questions about where a file is located or when it was last updated. For example, "Where is the keynote doc for Ignite 2024" might return no results because the content itself doesn't disclose its location. A `filterExpression` on metadata is a better approach for file location or date-specific queries.
-
-A more effective question is "What is the keynote doc for Ignite 2024". The response includes the synthesized answer, query activity and token counts, plus the URL and other metadata.
-
-### SharePoint-specific response fields
-
-Remote SharePoint results include fields that don't appear for other knowledge source types, such as `resourceMetadata`, `webUrl`, and `searchSensitivityLabelInfo`.
-
-```json
-{
-    "resourceMetadata": {
-        "Author": "Nuwan Amarathunga;Nurul Izzati",
-        "Title": "Ignite 2024 Keynote Address"
-    },
-    "rerankerScore": 2.489522,
-    "webUrl": "https://contoso-my.sharepoint.com/keynotes/Documents/Keynote-Ignite-2024.docx",
-    "searchSensitivityLabelInfo": {
-        "displayName": "Confidential\\Contoso Extended",
-        "sensitivityLabelId": "aaaaaaaa-0b0b-1c1c-2d2d-333333333333",
-        "tooltip": "Data is classified and protected.",
-        "priority": 5,
-        "color": "#FF8C00",
-        "isEncrypted": true
-    }
-}
-```
-
-### Enforce permissions at query time
-
-Remote SharePoint knowledge sources can enforce SharePoint permissions at query time. To enable this filtering, include the end user's access token in the retrieve request. The retrieval engine passes the token to the Copilot Retrieval API, which queries SharePoint and returns only content to which the user has access. SharePoint permissions and Microsoft Purview sensitivity labels are honored.
-
-Because remote SharePoint doesn't use a search index, no ingestion-time permissions configuration is needed. The access token is the only requirement.
-
-For instructions on passing the token, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using C#](knowledge-source-delete-csharp.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "リモートSharePointナレッジソースに関するC#ドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchの「リモートSharePointナレッジソース」に関するC#ドキュメントが完全に削除されたことを示しています。204行の内容が削除され、SharePointから直接テキストコンテンツをクエリおよびインデックスするための方法や手順が失われました。

削除された情報には、リモートSharePointナレッジソースを設定するためのサンプルコード、使用条件、制限、クエリの構築方法、SharePoint特有のレスポンスフィールドが含まれていました。また、KQLフィルターの使用方法や、コンテンツの取得時に適用されるセキュリティ権限の管理についても説明されていました。

この変更により、C#を使用してリモートSharePointのデータを扱う開発者にとって重要なリファレンスが失われ、代替情報を探す必要が生じるかもしれません。この削除はドキュメントの整備や更新の一環として行われたと考えられますが、ユーザーにとっては必要な情報を入手するための負担が増える結果となります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-python.md{#item-822712}

<details>
<summary>Diff</summary>
````diff
@@ -1,216 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-A *remote SharePoint knowledge source* uses the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) to query textual content directly from SharePoint in Microsoft 365. No search index or connection string is needed. Only textual content is queried, and usage is billed through Microsoft 365 and a Copilot license.
-
-To limit sites or constrain search, set a [filter expression](#filter-expression-examples) to scope by URLs, date ranges, file types, and other metadata. The caller's identity must be recognized by both the Azure tenant and the Microsoft 365 tenant because the retrieval engine queries SharePoint on behalf of the user.
-
-Like any other knowledge source, you specify a remote SharePoint knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md) and use the results as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). 
-
-+ SharePoint in a Microsoft 365 tenant that's under the same Microsoft Entra ID tenant as Azure.
-
-+ A Microsoft 365 Copilot license for query-time access to SharePoint content.
-
-+ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible.
-
-## Limitations
-
-The following limitations in the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) apply to remote SharePoint knowledge sources.
-
-+ There's no support for Copilot connectors or OneDrive content. Content is retrieved from SharePoint sites only.
-
-+ Limit of 200 requests per user per hour.
-
-+ Query character limit of 1,500 characters.
-
-+ Hybrid queries are only supported for the following file extensions: .doc, .docx, .pptx, .pdf, .aspx, and .one.
-
-+ Multimodal retrieval (nontextual content, including tables, images, and charts) isn't supported.
-
-+ Maximum of 25 results from a query.
-
-+ Results are returned by Copilot Retrieval API as unordered.
-
-+ Invalid Keyword Query Language (KQL) filter expressions are ignored and the query continues to execute without the filter.
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using Python](knowledge-source-check-python.md)]
-
-The following JSON is an example response for a remote SharePoint knowledge source.
-
-```json
-{
-  "name": "my-sharepoint-ks",
-  "kind": "remoteSharePoint",
-  "description": "A sample remote SharePoint knowledge source",
-  "encryptionKey": null,
-  "remoteSharePointParameters": {
-    "filterExpression": "filetype:docx",
-    "containerTypeId": null,
-    "resourceMetadata": [
-      "Author",
-      "Title"
-    ]
-  }
-}
-```
-
-## Create a knowledge source
-
-Run the following code to create a remote SharePoint knowledge source.
-
-```python
-# Create a remote SharePoint knowledge source
-from azure.core.credentials import AzureKeyCredential
-from azure.search.documents.indexes import SearchIndexClient
-from azure.search.documents.indexes.models import RemoteSharePointKnowledgeSource, RemoteSharePointKnowledgeSourceParameters
-
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
-
-knowledge_source = RemoteSharePointKnowledgeSource(
-    name = "my-remote-sharepoint-ks",
-    description= "This knowledge source queries .docx files in a trusted Microsoft 365 tenant.",
-    encryption_key = None,
-    remote_share_point_parameters = RemoteSharePointKnowledgeSourceParameters(
-        filter_expression = "filetype:docx",
-        resource_metadata = ["Author", "Title"],
-        container_type_id = None
-    )
-)
-
-index_client.create_or_update_knowledge_source(knowledge_source)
-print(f"Knowledge source '{knowledge_source.name}' created or updated successfully.")
-```
-
-### Source-specific properties
-
-You can pass the following properties to create a remote SharePoint knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
-| `description` | A description of the knowledge source. | String | Yes | No |
-| `encryption_key` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in the knowledge source. | Object | Yes | No |
-| `remote_share_point_parameters` | Parameters specific to remote SharePoint knowledge sources: `filter_expression`, `resource_metadata`, and `container_type_id`. | Object | No | No |
-| `filter_expression` | An expression written in the SharePoint [KQL](/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference), which is used to specify sites and paths to content. | String | Yes |No |
-| `resource_metadata` | A comma-delimited list of standard metadata fields: author, file name, creation date, content type, and file type. | Array | Yes | No |
-| `container_type_id` | Container ID for the SharePoint Embedded connection. When unspecified, SharePoint Online is used. | String | Yes | No |
-
-### Filter expression examples
-
-Not all SharePoint properties are supported in the `filterExpression`. For a list of supported properties, see the [API reference](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval). For queryable properties, see [Queryable](/graph/connecting-external-content-manage-schema#queryable).
-
-Learn more about [KQL filters](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval?pivots=graph-v1#example-7-use-filter-expressions) in the syntax reference.
-
-| Example | Filter expression |
-|---------|-------------------|
-| Filter to a single site by ID | `"filterExpression": "SiteID:\"00aa00aa-bb11-cc22-dd33-44ee44ee44ee\""` |
-| Filter to multiple sites by ID | `"filterExpression": "SiteID:\"00aa00aa-bb11-cc22-dd33-44ee44ee44ee\" OR SiteID:\"11bb11bb-cc22-dd33-ee44-55ff55ff55ff\""` |
-| Filter to files under a specific path | `"filterExpression": "Path:\"https://my-demo.sharepoint.com/sites/mysite/Shared Documents/en/mydocs\""` |
-| Filter to a specific date range | `"filterExpression": "LastModifiedTime >= 2024-07-22 AND LastModifiedTime <= 2025-01-08"` |
-| Filter to files of a specific file type | `"filterExpression": "FileExtension:\"docx\" OR FileExtension:\"pdf\" OR FileExtension:\"pptx\""` |
-| Filter to files of a specific information protection label | `"filterExpression": "InformationProtectionLabelId:\"f0ddcc93-d3c0-4993-b5cc-76b0a283e252\""` |
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-## Query a knowledge base
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query SharePoint content. Remote SharePoint has source-specific behaviors for query-time filtering, query formulation, response fields, and permissions enforcement.
-
-### Apply a KQL filter at query time
-
-You can pass a `filter_expression_add_on` in the `knowledge_source_params` on the retrieve request to apply a KQL filter at query time. If you specify `filter_expression_add_on` on the retrieve request and a `filter_expression` on the knowledge source definition, the filters are AND'd together.
-
-```python
-from azure.search.documents.knowledgebases.models import (
-    KnowledgeBaseMessage,
-    KnowledgeBaseMessageTextContent,
-    KnowledgeBaseRetrievalRequest,
-    RemoteSharePointKnowledgeSourceParams,
-)
-
-request = KnowledgeBaseRetrievalRequest(
-    messages=[
-        KnowledgeBaseMessage(
-            role="user",
-            content=[
-                KnowledgeBaseMessageTextContent(
-                    text="contoso product planning"
-                )
-            ],
-        )
-    ],
-    knowledge_source_params=[
-        RemoteSharePointKnowledgeSourceParams(
-            knowledge_source_name="my-remote-sharepoint-ks",
-            filter_expression_add_on="filetype:docx",
-        )
-    ],
-)
-
-result = kb_client.retrieve(
-    retrieval_request=request,
-    x_ms_query_source_authorization=token,
-)
-```
-
-### Write effective queries
-
-Queries that ask about the content itself are more effective than questions about where a file is located or when it was last updated. For example, "Where is the keynote doc for Ignite 2024" might return no results because the content itself doesn't disclose its location. A `filter_expression` on metadata is a better approach for file location or date-specific queries.
-
-A more effective question is "What is the keynote doc for Ignite 2024". The response includes the synthesized answer, query activity and token counts, plus the URL and other metadata.
-
-### SharePoint-specific response fields
-
-Remote SharePoint results include fields that don't appear for other knowledge source types, such as `resourceMetadata`, `webUrl`, and `searchSensitivityLabelInfo`.
-
-```json
-{
-    "resourceMetadata": {
-        "Author": "Nuwan Amarathunga;Nurul Izzati",
-        "Title": "Ignite 2024 Keynote Address"
-    },
-    "rerankerScore": 2.489522,
-    "webUrl": "https://contoso-my.sharepoint.com/keynotes/Documents/Keynote-Ignite-2024.docx",
-    "searchSensitivityLabelInfo": {
-        "displayName": "Confidential\\Contoso Extended",
-        "sensitivityLabelId": "aaaaaaaa-0b0b-1c1c-2d2d-333333333333",
-        "tooltip": "Data is classified and protected.",
-        "priority": 5,
-        "color": "#FF8C00",
-        "isEncrypted": true
-    }
-}
-```
-
-### Enforce permissions at query time
-
-Remote SharePoint knowledge sources can enforce SharePoint permissions at query time. To enable this filtering, include the end user's access token in the retrieve request. The retrieval engine passes the token to the Copilot Retrieval API, which queries SharePoint and returns only content to which the user has access. SharePoint permissions and Microsoft Purview sensitivity labels are honored.
-
-Because remote SharePoint doesn't use a search index, no ingestion-time permissions configuration is needed. The access token is the only requirement.
-
-For instructions on passing the token, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using Python](knowledge-source-delete-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "リモートSharePointナレッジソースに関するPythonドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchに関連する「リモートSharePointナレッジソース」に関するPythonドキュメントが完全に削除されたことを示しています。216行の内容が削除され、SharePointから直接テキストデータをクエリするための方法や手順が失われました。

削除された内容には、リモートSharePointナレッジソースを構築するためのサンプルコードや、利用条件、制約、クエリ作成時のベストプラクティス、SharePoint固有のレスポンスフィールドが含まれていました。特に、APIを介して取得されるデータの処理や、データにアクセスするためのユーザー権限の管理方法についても言及されていました。

この変更の結果、Pythonを使用してリモートSharePointのデータを操作する開発者にとって重要な情報が失われ、代替情報の探索を余儀なくされるかもしれません。ドキュメントの更新や整理の一環としての削除と考えられますが、ユーザーにとっては必要な情報を見つけるための負担が増加することになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-rest.md{#item-5514b1}

<details>
<summary>Diff</summary>
````diff
@@ -1,204 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-A *remote SharePoint knowledge source* uses the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) to query textual content directly from SharePoint in Microsoft 365. No search index or connection string is needed. Only textual content is queried, and usage is billed through Microsoft 365 and a Copilot license.
-
-To limit sites or constrain search, set a [filter expression](#filter-expression-examples) to scope by URLs, date ranges, file types, and other metadata. The caller's identity must be recognized by both the Azure tenant and the Microsoft 365 tenant because the retrieval engine queries SharePoint on behalf of the user.
-
-Like any other knowledge source, you specify a remote SharePoint knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md) and use the results as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). 
-
-+ SharePoint in a Microsoft 365 tenant that's under the same Microsoft Entra ID tenant as Azure.
-
-+ A Microsoft 365 Copilot license for query-time access to SharePoint content.
-
-+ The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible.
-
-## Limitations
-
-The following limitations in the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) apply to remote SharePoint knowledge sources.
-
-+ There's no support for Copilot connectors or OneDrive content. Content is retrieved from SharePoint sites only.
-
-+ Limit of 200 requests per user per hour.
-
-+ Query character limit of 1,500 characters.
-
-+ Hybrid queries are only supported for the following file extensions: .doc, .docx, .pptx, .pdf, .aspx, and .one.
-
-+ Multimodal retrieval (nontextual content, including tables, images, and charts) isn't supported.
-
-+ Maximum of 25 results from a query.
-
-+ Results are returned by Copilot Retrieval API as unordered.
-
-+ Invalid Keyword Query Language (KQL) filter expressions are ignored and the query continues to execute without the filter.
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using REST](knowledge-source-check-rest.md)]
-
-The following JSON is an example response for a remote SharePoint knowledge source.
-
-```json
-{
-  "name": "my-sharepoint-ks",
-  "kind": "remoteSharePoint",
-  "description": "A sample remote SharePoint knowledge source",
-  "encryptionKey": null,
-  "remoteSharePointParameters": {
-    "filterExpression": "filetype:docx",
-    "containerTypeId": null,
-    "resourceMetadata": [
-      "Author",
-      "Title"
-    ]
-  }
-}
-```
-
-## Create a knowledge source
-
-Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create a remote SharePoint knowledge source.
-
-```http
-POST {{search-url}}/knowledgesources/my-remote-sharepoint-ks?api-version=2025-11-01-preview
-api-key: {{api-key}}
-Content-Type: application/json
-
-{
-    "name": "my-remote-sharepoint-ks",
-    "kind": "remoteSharePoint",
-    "description": "This knowledge source queries .docx files in a trusted Microsoft 365 tenant.",
-    "encryptionKey": null,
-    "remoteSharePointParameters": {
-        "filterExpression": "filetype:docx",
-        "resourceMetadata": [ "Author", "Title" ],
-        "containerTypeId": null
-    }
-}
-```
-
-### Source-specific properties
-
-You can pass the following properties to create a remote SharePoint knowledge source.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | No | Yes |
-| `kind` | The kind of knowledge source, which is `remoteSharePoint` in this case. | String | No | Yes |
-| `description` | A description of the knowledge source. | String | Yes | No |
-| `encryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in the knowledge source. | Object | Yes | No |
-| `remoteSharePointParameters` | Parameters specific to remote SharePoint knowledge sources: `filterExpression`, `resourceMetadata`, and `containerTypeId`. | Object | No | No |
-| `filterExpression` | An expression written in the SharePoint [KQL](/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference), which is used to specify sites and paths to content. | String | Yes |No |
-| `resourceMetadata` | A comma-delimited list of standard metadata fields: author, file name, creation date, content type, and file type. | Array | Yes | No |
-| `containerTypeId` | Container ID for the SharePoint Embedded connection. When unspecified, SharePoint Online is used. | String | Yes | No |
-
-### Filter expression examples
-
-Not all SharePoint properties are supported in the `filterExpression`. For a list of supported properties, see the [API reference](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval). For queryable properties, see [Queryable](/graph/connecting-external-content-manage-schema#queryable).
-
-Learn more about [KQL filters](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval?pivots=graph-v1#example-7-use-filter-expressions) in the syntax reference.
-
-| Example | Filter expression |
-|---------|-------------------|
-| Filter to a single site by ID | `"filterExpression": "SiteID:\"00aa00aa-bb11-cc22-dd33-44ee44ee44ee\""` |
-| Filter to multiple sites by ID | `"filterExpression": "SiteID:\"00aa00aa-bb11-cc22-dd33-44ee44ee44ee\" OR SiteID:\"11bb11bb-cc22-dd33-ee44-55ff55ff55ff\""` |
-| Filter to files under a specific path | `"filterExpression": "Path:\"https://my-demo.sharepoint.com/sites/mysite/Shared Documents/en/mydocs\""` |
-| Filter to a specific date range | `"filterExpression": "LastModifiedTime >= 2024-07-22 AND LastModifiedTime <= 2025-01-08"` |
-| Filter to files of a specific file type | `"filterExpression": "FileExtension:\"docx\" OR FileExtension:\"pdf\" OR FileExtension:\"pptx\""` |
-| Filter to files of a specific information protection label | `"filterExpression": "InformationProtectionLabelId:\"f0ddcc93-d3c0-4993-b5cc-76b0a283e252\""` |
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-## Query a knowledge base
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query SharePoint content. Remote SharePoint has source-specific behaviors for query-time filtering, query formulation, response fields, and permissions enforcement.
-
-### Apply a KQL filter at query time
-
-You can pass a `filterExpressionAddOn` in the `knowledgeSourceParams` on the retrieve request to apply a KQL filter at query time. If you specify `filterExpressionAddOn` on the retrieve request and a `filterExpression` on the knowledge source definition, the filters are AND'd together.
-
-```http
-POST {{search-url}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2025-11-01-preview
-Authorization: Bearer {{accessToken}}
-Content-Type: application/json
-x-ms-query-source-authorization: {{user-access-token}}
-
-{
-    "messages": [
-        {
-            "role": "user",
-            "content": [
-                { "type": "text", "text": "contoso product planning" }
-            ]
-        }
-    ],
-    "knowledgeSourceParams": [
-        {
-            "knowledgeSourceName": "my-remote-sharepoint-ks",
-            "kind": "remoteSharePoint",
-            "filterExpressionAddOn": "filetype:docx"
-        }
-    ]
-}
-```
-
-### Write effective queries
-
-Queries that ask about the content itself are more effective than questions about where a file is located or when it was last updated. For example, "Where is the keynote doc for Ignite 2024" might return no results because the content itself doesn't disclose its location. A `filterExpression` on metadata is a better approach for file location or date-specific queries.
-
-A more effective question is "What is the keynote doc for Ignite 2024". The response includes the synthesized answer, query activity and token counts, plus the URL and other metadata.
-
-### SharePoint-specific response fields
-
-Remote SharePoint results include fields that don't appear for other knowledge source types, such as `resourceMetadata`, `webUrl`, and `searchSensitivityLabelInfo`.
-
-```json
-{
-    "resourceMetadata": {
-        "Author": "Nuwan Amarathunga;Nurul Izzati",
-        "Title": "Ignite 2024 Keynote Address"
-    },
-    "rerankerScore": 2.489522,
-    "webUrl": "https://contoso-my.sharepoint.com/keynotes/Documents/Keynote-Ignite-2024.docx",
-    "searchSensitivityLabelInfo": {
-        "displayName": "Confidential\\Contoso Extended",
-        "sensitivityLabelId": "aaaaaaaa-0b0b-1c1c-2d2d-333333333333",
-        "tooltip": "Data is classified and protected.",
-        "priority": 5,
-        "color": "#FF8C00",
-        "isEncrypted": true
-    }
-}
-```
-
-### Enforce permissions at query time
-
-Remote SharePoint knowledge sources can enforce SharePoint permissions at query time. To enable this filtering, include the end user's access token in the retrieve request. The retrieval engine passes the token to the Copilot Retrieval API, which queries SharePoint and returns only content to which the user has access. SharePoint permissions and Microsoft Purview sensitivity labels are honored.
-
-Because remote SharePoint doesn't use a search index, no ingestion-time permissions configuration is needed. The access token is the only requirement.
-
-For instructions on passing the token, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using REST](knowledge-source-delete-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "リモートSharePointナレッジソースに関するREST APIドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchに関連する「リモートSharePointナレッジソース」に関するREST APIドキュメントが完全に削除されたことを示しています。204行の内容が削除され、このドキュメントに含まれていたのは、SharePointから直接テキストコンテンツをクエリするための手順やサンプルコード、使用条件、制約に関する詳細情報でした。

削除された内容には、リモートSharePointナレッジソースの作成や更新に関するAPIの使用方法、クエリ作成時の注意点、KQLフィルターの適用方法、弁護士に関連するレスポンスフィールドなどが含まれていました。特に、SharePointからのデータ取得に関連するAPIの設計や、ユーザー権限管理の実装に関する情報が失われることで、開発者にとって重要なリファレンスが喪失されたことになります。

この変更によって、REST APIを使用してリモートSharePointのデータを操作する開発者は、新しい情報源を探す必要に迫られる可能性があり、必要な手順や情報を見つける上での負担が増加することが予想されます。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-csharp.md{#item-401063}

<details>
<summary>Diff</summary>
````diff
@@ -1,121 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-> [!IMPORTANT]
-> + Web Knowledge Source, which uses Grounding with Bing Search and/or Grounding with Bing Custom Search, is a [First Party Consumption Service](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/EAEAS) governed by the [Grounding with Bing terms of use](https://www.microsoft.com/en-us/bing/apis/grounding-legal-enterprise) and the [Microsoft Privacy Statement](https://www.microsoft.com/en-us/privacy/privacystatement).
->
-> + The [Microsoft Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) doesn't apply to data sent to Web Knowledge Source. When Customer uses Web Knowledge Source, Customer Data flows outside the Azure compliance and Geo boundary. This also means use of Web Knowledge Source waives all elevated Government Community Cloud security and compliance commitments to include data sovereignty and screened/citizenship-based support, as applicable.
->
-> + Use of Web Knowledge Source incurs costs; learn more about [pricing](https://www.microsoft.com/en-us/bing/apis/grounding-pricing).
->
-> + Learn more about how Azure admins can [manage access to use of Web Knowledge Source](../../agentic-knowledge-source-how-to-web-manage.md).
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-*Web Knowledge Source* enables retrieval of real-time web data from Microsoft Bing in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-Bing Custom Search is always the search provider for Web Knowledge Source. Although you can't specify alternative search providers or engines, you can include or exclude specific *domains*, such as https://learn.microsoft.com. When no domains are specified, Web Knowledge Source has unrestricted access to the entire public internet.
-
-Web Knowledge Source works best alongside other knowledge sources. Use Web Knowledge Source when your proprietary content doesn't provide complete, up-to-date answers or when you want to supplement results with information from a commercial search engine.
-
-When you use Web Knowledge Source, keep the following in mind:
-
-+ The response is always a single, formulated answer to the query instead of raw search results from the web.
-
-+ Because Web Knowledge Source doesn't support extractive data, your knowledge base must use [answer synthesis](../../agentic-retrieval-how-to-answer-synthesis.md) and [low or medium reasoning effort](../../agentic-retrieval-how-to-create-knowledge-base.md#create-a-knowledge-base). You also can't define answer instructions.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ An Azure subscription with [access to Web Knowledge Source](../../agentic-knowledge-source-how-to-web-manage.md). By default, access is enabled. Contact your admin if access is disabled.
-
-+ An Azure AI Search service in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). The service must also be in an [Azure public region](../../search-region-support.md#azure-public-regions), as Web Knowledge Source isn't supported in private or sovereign clouds.
-
-+ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using C#](knowledge-source-check-csharp.md)]
-
-The following JSON is an example response for a Web Knowledge Source resource.
-
-```json
-{
-  "WebParameters": {
-    "Domains": null
-  },
-  "Name": "my-web-ks",
-  "Description": "A sample Web Knowledge Source.",
-  "EncryptionKey": null,
-}
-```
-
-## Create a knowledge source
-
-Run the following code to create a Web Knowledge Source resource.
-
-```csharp
-// Create Web Knowledge Source
-// Create a Web knowledge source
-using Azure.Search.Documents.Indexes;
-using Azure.Search.Documents.Indexes.Models;
-using Azure;
-
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
-
-var knowledgeSource = new WebKnowledgeSource(name: "my-web-ks")
-{
-    Description = "A sample Web Knowledge Source.",
-    WebParameters = new WebKnowledgeSourceParameters
-    {
-        Domains = new WebKnowledgeSourceDomains
-        {
-            AllowedDomains = 
-            {
-                new WebKnowledgeSourceDomain(address: "learn.microsoft.com") { IncludeSubpages = true }
-            },
-            BlockedDomains = 
-            {
-                new WebKnowledgeSourceDomain(address: "bing.com") { IncludeSubpages = false }
-            }
-        }
-    }
-};
-
-await indexClient.CreateOrUpdateKnowledgeSourceAsync(knowledgeSource);
-Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated successfully.");
-```
-
-### Source-specific properties
-
-You can pass the following properties to create a Web Knowledge Source resource.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `Name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | Yes | Yes |
-| `Description` | A description of the knowledge source. When unspecified, Azure AI Search applies a default description. | String | Yes | No |
-| `EncryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in the knowledge source. | Object | Yes | No |
-| `WebParameters` | Parameters specific to Web Knowledge Source. Currently, this is only `Domains`. | Object | Yes | No |
-| `Domains` | Domains to allow or block from the search space. By default, the knowledge source uses [Grounding with Bing Search](/azure/ai-foundry/agents/how-to/tools/bing-grounding) to search the entire public internet. When you specify domains, the knowledge source uses [Grounding with Bing Custom Search](/azure/ai-foundry/agents/how-to/tools/bing-custom-search) to restrict results to the specified domains. In both cases, Bing Custom Search is the search provider. | Object | Yes | No |
-| `AllowedDomains` | Domains to include in the search space. For each domain, you must specify its `address` in the `website.com` format. You can also specify whether to include the domain's subpages by setting `IncludeSubpages` to `true` or `false`. | Array | Yes | No |
-| `BlockedDomains` | Domains to exclude from the search space. For each domain, you must specify its `address` in the `website.com` format. You can also specify whether to include the domain's subpages by setting `IncludeSubpages` to `true` or `false`. | Array | Yes | No |
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using C#](knowledge-source-delete-csharp.md)]
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Webナレッジソースに関するC#ドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchに関連する「Webナレッジソース」に関するC#ドキュメントが完全に削除されたことを示しています。121行が削除され、このドキュメントに含まれていたのは、Microsoft Bingからのリアルタイムのウェブデータ取得に関する手順や説明、サンプルコード、利用条件、及び制約についての情報でした。

削除された内容には、Webナレッジソースの作成や設定方法、推奨される利用方法、ドメインの許可/ブロック設定、また、特定の条件下でのデータ取得に関する詳細が含まれていました。特に、Bing Custom Searchの利用や、ナレッジベースとの連携についてのガイダンスもあったため、Webに基づいた知識をエージェントやチャットボットに供給する方法が失われる結果となります。

この変更によって、C#を使用してWebナレッジソースを操作する開発者にとって重要な情報が取り除かれ、代わりの情報源を探す必要が生じるかもしれません。これにより、開発者はWebナレッジソースの効果的な利用に関して新たな知識を得るために、より多くの時間を費やすことになるでしょう。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-python.md{#item-72b59c}

<details>
<summary>Diff</summary>
````diff
@@ -1,114 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-> [!IMPORTANT]
-> + Web Knowledge Source, which uses Grounding with Bing Search and/or Grounding with Bing Custom Search, is a [First Party Consumption Service](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/EAEAS) governed by the [Grounding with Bing terms of use](https://www.microsoft.com/en-us/bing/apis/grounding-legal-enterprise) and the [Microsoft Privacy Statement](https://www.microsoft.com/en-us/privacy/privacystatement).
->
-> + The [Microsoft Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) doesn't apply to data sent to Web Knowledge Source. When Customer uses Web Knowledge Source, Customer Data flows outside the Azure compliance and Geo boundary. This also means use of Web Knowledge Source waives all elevated Government Community Cloud security and compliance commitments to include data sovereignty and screened/citizenship-based support, as applicable.
->
-> + Use of Web Knowledge Source incurs costs; learn more about [pricing](https://www.microsoft.com/en-us/bing/apis/grounding-pricing).
->
-> + Learn more about how Azure admins can [manage access to use of Web Knowledge Source](../../agentic-knowledge-source-how-to-web-manage.md).
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-*Web Knowledge Source* enables retrieval of real-time web data from Microsoft Bing in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-Bing Custom Search is always the search provider for Web Knowledge Source. Although you can't specify alternative search providers or engines, you can include or exclude specific *domains*, such as https://learn.microsoft.com. When no domains are specified, Web Knowledge Source has unrestricted access to the entire public internet.
-
-Web Knowledge Source works best alongside other knowledge sources. Use Web Knowledge Source when your proprietary content doesn't provide complete, up-to-date answers or when you want to supplement results with information from a commercial search engine.
-
-When you use Web Knowledge Source, keep the following in mind:
-
-+ The response is always a single, formulated answer to the query instead of raw search results from the web.
-
-+ Because Web Knowledge Source doesn't support extractive data, your knowledge base must use [answer synthesis](../../agentic-retrieval-how-to-answer-synthesis.md) and [low or medium reasoning effort](../../agentic-retrieval-how-to-create-knowledge-base.md#create-a-knowledge-base). You also can't define answer instructions.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ An Azure subscription with [access to Web Knowledge Source](../../agentic-knowledge-source-how-to-web-manage.md). By default, access is enabled. Contact your admin if access is disabled.
-
-+ An Azure AI Search service in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). The service must also be in an [Azure public region](../../search-region-support.md#azure-public-regions), as Web Knowledge Source isn't supported in private or sovereign clouds.
-
-+ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using Python](knowledge-source-check-python.md)]
-
-The following JSON is an example response for a Web Knowledge Source resource.
-
-```json
-{
-  "name": "my-web-ks",
-  "kind": "web",
-  "description": "A sample Web Knowledge Source.",
-  "encryptionKey": null,
-  "webParameters": {
-    "domains": null
-  }
-}
-```
-
-## Create a knowledge source
-
-Run the following code to create a Web Knowledge Source resource.
-
-```python
-# Create Web Knowledge Source
-from azure.core.credentials import AzureKeyCredential
-from azure.search.documents.indexes import SearchIndexClient
-from azure.search.documents.indexes.models import WebKnowledgeSource, WebKnowledgeSourceParameters, WebKnowledgeSourceDomains
-
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
-
-knowledge_source = WebKnowledgeSource(
-    name = "my-web-ks",
-    description = "A sample Web Knowledge Source.",
-    encryption_key = None,
-    web_parameters = WebKnowledgeSourceParameters(
-        domains = WebKnowledgeSourceDomains(
-            allowed_domains = [ { "address": "learn.microsoft.com", "include_subpages": True } ],
-            blocked_domains = [ { "address": "bing.com", "include_subpages": False } ]
-        )
-    )
-)
-
-index_client.create_or_update_knowledge_source(knowledge_source)
-print(f"Knowledge source '{knowledge_source.name}' created or updated successfully.")
-```
-
-### Source-specific properties
-
-You can pass the following properties to create a Web Knowledge Source resource.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | Yes | Yes |
-| `description` | A description of the knowledge source. When unspecified, Azure AI Search applies a default description. | String | Yes | No |
-| `encryption_key` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in the knowledge source. | Object | Yes | No |
-| `web_parameters` | Parameters specific to Web Knowledge Source. Currently, this is only `domains`. | Object | Yes | No |
-| `domains` | Domains to allow or block from the search space. By default, the knowledge source uses [Grounding with Bing Search](/azure/ai-foundry/agents/how-to/tools/bing-grounding) to search the entire public internet. When you specify domains, the knowledge source uses [Grounding with Bing Custom Search](/azure/ai-foundry/agents/how-to/tools/bing-custom-search) to restrict results to the specified domains. In both cases, Bing Custom Search is the search provider. | Object | Yes | No |
-| `allowed_domains` | Domains to include in the search space. For each domain, you must specify its `address` in the `website.com` format. You can also specify whether to include the domain's subpages by setting `include_subpages` to `true` or `false`. | Array | Yes | No |
-| `blocked_domains` | Domains to exclude from the search space. For each domain, you must specify its `address` in the `website.com` format. You can also specify whether to include the domain's subpages by setting `include_subpages` to `true` or `false`. | Array | Yes | No |
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using Python](knowledge-source-delete-python.md)]
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Webナレッジソースに関するPythonドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchに関連する「Webナレッジソース」に関するPythonドキュメントが完全に削除されたことを示しています。114行の情報が削除され、このドキュメントには、Microsoft Bingからのリアルタイムのウェブデータを取得するための手順やサンプルコード、利用条件、制約についての詳細が含まれていました。

削除された内容には、Webナレッジソースの作成方法や設定方法、特定のドメインの許可やブロックの設定、サンプルJSONレスポンス、及びナレッジベースとの連携についてのガイダンスが含まれていました。これにより、Pythonを使用してWebナレッジソースを操作する開発者にとっての重要なリファレンスが失われたことになります。

この変更によって、Pythonを利用してWebナレッジソースを効率的に扱う方法に関する情報が喪失され、開発者はその代替手段を模索する必要が生じるでしょう。これにより、Azure AI Searchを利用する上での開発効率に影響が及ぶ可能性があります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-rest.md{#item-649608}

<details>
<summary>Diff</summary>
````diff
@@ -1,110 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/25/2026
----
-
-> [!IMPORTANT]
-> + Web Knowledge Source, which uses Grounding with Bing Search and/or Grounding with Bing Custom Search, is a [First Party Consumption Service](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/EAEAS) governed by the [Grounding with Bing terms of use](https://www.microsoft.com/en-us/bing/apis/grounding-legal-enterprise) and the [Microsoft Privacy Statement](https://www.microsoft.com/en-us/privacy/privacystatement).
->
-> + The [Microsoft Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) doesn't apply to data sent to Web Knowledge Source. When Customer uses Web Knowledge Source, Customer Data flows outside the Azure compliance and Geo boundary. This also means use of Web Knowledge Source waives all elevated Government Community Cloud security and compliance commitments to include data sovereignty and screened/citizenship-based support, as applicable.
->
-> + Use of Web Knowledge Source incurs costs; learn more about [pricing](https://www.microsoft.com/en-us/bing/apis/grounding-pricing).
->
-> + Learn more about how Azure admins can [manage access to use of Web Knowledge Source](../../agentic-knowledge-source-how-to-web-manage.md).
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-*Web Knowledge Source* enables retrieval of real-time web data from Microsoft Bing in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
-
-Bing Custom Search is always the search provider for Web Knowledge Source. Although you can't specify alternative search providers or engines, you can include or exclude specific *domains*, such as https://learn.microsoft.com. When no domains are specified, Web Knowledge Source has unrestricted access to the entire public internet.
-
-Web Knowledge Source works best alongside other knowledge sources. Use Web Knowledge Source when your proprietary content doesn't provide complete, up-to-date answers or when you want to supplement results with information from a commercial search engine.
-
-When you use Web Knowledge Source, keep the following in mind:
-
-+ The response is always a single, formulated answer to the query instead of raw search results from the web.
-
-+ Because Web Knowledge Source doesn't support extractive data, your knowledge base must use [answer synthesis](../../agentic-retrieval-how-to-answer-synthesis.md) and [low or medium reasoning effort](../../agentic-retrieval-how-to-create-knowledge-base.md#create-a-knowledge-base). You also can't define answer instructions.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ An Azure subscription with [access to Web Knowledge Source](../../agentic-knowledge-source-how-to-web-manage.md). By default, access is enabled. Contact your admin if access is disabled.
-
-+ An Azure AI Search service in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).  The service must also be in an [Azure public region](../../search-region-support.md#azure-public-regions), as Web Knowledge Source isn't supported in private or sovereign clouds.
-
-+ The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-## Check for existing knowledge sources
-
-[!INCLUDE [Check for existing knowledge sources using REST](knowledge-source-check-rest.md)]
-
-The following JSON is an example response for a Web Knowledge Source resource.
-
-```json
-{
-  "name": "my-web-ks",
-  "kind": "web",
-  "description": "A sample Web Knowledge Source.",
-  "encryptionKey": null,
-  "webParameters": {
-    "domains": null
-  }
-}
-```
-
-## Create a knowledge source
-
-Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create a Web Knowledge Source resource.
-
-```http
-PUT {{search-url}}/knowledgesources/my-web-ks?api-version=2025-11-01-preview
-Content-Type: application/json
-api-key: {{api-key}}
-
-{
-  "name": "my-web-ks",
-  "kind": "web",
-  "description": "This knowledge source pulls content from the web.",
-  "encryptionKey": null,
-  "webParameters": {
-    "domains": {
-      "allowedDomains": [ { "address": "learn.microsoft.com", "includeSubpages": true } ],
-      "blockedDomains": [ { "address": "bing.com", "includeSubpages": false } ]
-    }
-  }
-}
-```
-
-### Source-specific properties
-
-You can pass the following properties to create a Web Knowledge Source resource.
-
-| Name | Description | Type | Editable | Required |
-|--|--|--|--|--|
-| `name` | The name of the knowledge source, which must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | Yes | Yes |
-| `kind` | The kind of knowledge source, which is `web` in this case. | String | No | Yes |
-| `description` | A description of the knowledge source. When unspecified, Azure AI Search applies a default description. | String | Yes | No |
-| `encryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in the knowledge source. | Object | Yes | No |
-| `webParameters` | Parameters specific to Web Knowledge Source. Currently, this is only `domains`. | Object | Yes | No |
-| `domains` | Domains to allow or block from the search space. By default, the knowledge source uses [Grounding with Bing Search](/azure/ai-foundry/agents/how-to/tools/bing-grounding) to search the entire public internet. When you specify domains, the knowledge source uses [Grounding with Bing Custom Search](/azure/ai-foundry/agents/how-to/tools/bing-custom-search) to restrict results to the specified domains. In both cases, Bing Custom Search is the search provider. | Object | Yes | No |
-| `allowedDomains` | Domains to include in the search space. For each domain, you must specify its `address` in the `website.com` format. You can also specify whether to include the domain's subpages by setting `includeSubpages` to `true` or `false`. | Array | Yes | No |
-| `blockedDomains` | Domains to exclude from the search space. For each domain, you must specify its `address` in the `website.com` format. You can also specify whether to include the domain's subpages by setting `includeSubpages` to `true` or `false`. | Array | Yes | No |
-
-## Assign to a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-## Delete a knowledge source
-
-[!INCLUDE [Delete knowledge source using REST](knowledge-source-delete-rest.md)]
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Webナレッジソースに関するRESTドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchに関連する「Webナレッジソース」に関するREST APIドキュメントが完全に削除されたことを示しています。このドキュメントでは、Webナレッジソースの作成や管理に関する手順が詳述されており、110行の情報が削除されました。

削除された内容には、REST APIを介してWebナレッジソースを作成、更新、削除するための具体的なHTTPリクエストの例や、必要なパラメータとしてのドメインの設定、セキュリティに関する情報が含まれていました。また、Webナレッジソースの用途や、エージェントまたはチャットボットがどのようにデータを問い合わせるかについても詳しく説明されていました。

この変更により、REST APIを利用してWebナレッジソースを操作する開発者にとっての重要なリファレンスが失われ、必要な技術情報を別の場所で探さなければならない状況が生じます。この結果、Azure AI Searchを使用する際の生産性に影響を及ぼす可能性があります。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-csharp.md{#item-4469a2}

<details>
<summary>Diff</summary>
````diff
@@ -1,331 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/17/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-In Azure AI Search, a *knowledge base* is a top-level object that orchestrates [agentic retrieval](../../agentic-retrieval-overview.md). It defines which knowledge sources to query and the default behavior for retrieval operations. At query time, the [retrieve method](../../agentic-retrieval-how-to-retrieve.md) targets the knowledge base to run the configured retrieval pipeline.
-
-You can create a knowledge base in a [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) workload in the Microsoft Foundry (new) portal. You also need a knowledge base in any agentic solutions that you create using the Azure AI Search APIs.
-
-A knowledge base specifies:
-
-+ One or more knowledge sources that point to searchable content.
-+ An optional LLM that provides reasoning capabilities for query planning and answer formulation.
-+ A retrieval reasoning effort that determines whether an LLM is invoked and manages cost, latency, and quality.
-+ Custom properties that control routing, source selection, output format, and object encryption.
-
-After you create a knowledge base, you can update its properties at any time. If the knowledge base is in use, updates take effect on the next retrieval.
-
-> [!IMPORTANT]
-> 2025-11-01-preview renames the 2025-08-01-preview "knowledge agent" to "knowledge base." This is a breaking change. We recommend [migrating existing code](../../agentic-retrieval-how-to-migrate.md) to the new APIs as soon as possible.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). If you're using a [managed identity](../../search-how-to-managed-identities.md) for role-based access to deployed models, your search service must be on the Basic pricing tier or higher.
-
-+ Azure OpenAI with a [supported LLM](#supported-models) deployment.
-
-+ One or more [knowledge sources](../../agentic-knowledge-source-overview.md#supported-knowledge-sources) on your search service.
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md). **Search Service Contributor** can create and manage a knowledge base. **Search Index Data Reader** can run queries. Alternatively, you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-+ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
-
-### Supported models
-
-Use one of the following LLMs from Azure OpenAI in Foundry Models. For deployment instructions, see [Deploy Microsoft Foundry Models in the Foundry portal](/azure/ai-foundry/how-to/deploy-models-openai).
-
-+ `gpt-4o`
-+ `gpt-4o-mini`
-+ `gpt-4.1`
-+ `gpt-4.1-nano`
-+ `gpt-4.1-mini`
-+ `gpt-5`
-+ `gpt-5-nano`
-+ `gpt-5-mini`
-
-## Configure access
-
-Azure AI Search needs access to the LLM from Azure OpenAI. We recommend Microsoft Entra ID for authentication and role-based access for authorization. To assign roles, you must be an **Owner or User Access Administrator**. If you can't use roles, use key-based authentication instead.
-
-### [**Use roles**](#tab/rbac)
-
-1. [Configure Azure AI Search to use a managed identity](../../search-how-to-managed-identities.md).
-
-1. On your model provider, such as Foundry Models, assign **Cognitive Services User** to the managed identity of your search service. If you're testing locally, assign the same role to your user account.
-
-1. For local testing, follow the steps in [Quickstart: Connect without keys](../../search-get-started-rbac.md) to sign in to a specific subscription and tenant. Use `DefaultAzureCredential` instead of `AzureKeyCredential` in each request, which should look similar to the following example:
-
-    ```csharp
-    using Azure.Search.Documents.Indexes;
-    using Azure.Identity;
-    
-    var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
-    ```
-
-### [**Use keys**](#tab/keys)
-
-1. [Copy an Azure AI Search admin API key](../../search-security-api-keys.md#find-existing-keys) from the Azure portal.
-
-1. Use `AzureKeyCredential` to specify the API key in each request. Your code should look similar to the following example:
-
-    ```csharp
-    using Azure.Search.Documents.Indexes;
-    using Azure;
-    
-    var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
-    ```
-
----
-
-> [!IMPORTANT]
-> Code snippets in this article use API keys. If you use role-based authentication, update each request accordingly. In a request that specifies both approaches, the API key takes precedence.
-
-## Check for existing knowledge bases
-
-Knowing about existing knowledge bases is helpful for either reusing them or naming new objects. Any 2025-08-01-preview knowledge agents are returned in the knowledge bases collection.
-
-Run the following code to list existing knowledge bases by name.
-
-```csharp
-// List knowledge bases by name
-  using Azure.Search.Documents.Indexes;
-  
-  var indexClient = new SearchIndexClient(new Uri(searchEndpoint), credential);
-  var knowledgeBases = indexClient.GetKnowledgeBasesAsync();
-  
-  Console.WriteLine("Knowledge Bases:");
-  
-  await foreach (var kb in knowledgeBases)
-  {
-      Console.WriteLine($"  - {kb.Name}");
-  }
-```
-
-You can also return a single knowledge base by name to review its JSON definition.
-
-```csharp
-using Azure.Search.Documents.Indexes;
-using System.Text.Json;
-
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), credential);
-
-// Specify the knowledge base name to retrieve
-string kbNameToGet = "earth-knowledge-base";
-
-// Get a specific knowledge base definition
-var knowledgeBaseResponse = await indexClient.GetKnowledgeBaseAsync(kbNameToGet);
-var kb = knowledgeBaseResponse.Value;
-
-// Serialize to JSON for display
-string json = JsonSerializer.Serialize(kb, new JsonSerializerOptions { WriteIndented = true });
-Console.WriteLine(json);
-```
-
-The following JSON is an example of a knowledge base.
-
-```json
-{
-  "Name": "earth-knowledge-base",
-  "KnowledgeSources": [
-    {
-      "Name": "earth-knowledge-source"
-    }
-  ],
-  "Models": [
-    {}
-  ],
-  "RetrievalReasoningEffort": {},
-  "OutputMode": {},
-  "ETag": "\u00220x8DE278629D782B3\u0022",
-  "EncryptionKey": null,
-  "Description": null,
-  "RetrievalInstructions": null,
-  "AnswerInstructions": null
-}
-```
-
-## Create a knowledge base
-
-A knowledge base drives the agentic retrieval pipeline. In application code, other agents or chatbots call it.
-
-A knowledge base connects knowledge sources (searchable content) to an LLM deployment from Azure OpenAI. Properties on the LLM establish the connection, while properties on the knowledge source establish defaults that inform query execution and the response.
-
-Run the following code to create a knowledge base.
-
-```csharp
-using Azure.Search.Documents.Indexes.Models;
-using Azure.Search.Documents.KnowledgeBases.Models;
-
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), credential);
-
-// Create a knowledge base
-var knowledgeBase = new KnowledgeBase(
-    name: knowledgeBaseName,
-    knowledgeSources: new KnowledgeSourceReference[] { new KnowledgeSourceReference(knowledgeSourceName) }
-)
-{
-    RetrievalReasoningEffort = new KnowledgeRetrievalLowReasoningEffort(),
-    OutputMode = KnowledgeRetrievalOutputMode.AnswerSynthesis,
-    Models = { model }
-};
-await indexClient.CreateOrUpdateKnowledgeBaseAsync(knowledgeBase);
-Console.WriteLine($"Knowledge base '{knowledgeBaseName}' created or updated successfully.");
-```
-
-```csharp
-# Create a knowledge base
-using Azure.Search.Documents.Indexes;
-using Azure.Search.Documents.Indexes.Models;
-using Azure.Search.Documents.KnowledgeBases.Models;
-using Azure;
-
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
-
-var aoaiParams = new AzureOpenAIVectorizerParameters
-{
-    ResourceUri = new Uri(aoaiEndpoint),
-    DeploymentName = aoaiGptDeployment,
-    ModelName = aoaiGptModel
-};
-
-var knowledgeBase = new KnowledgeBase(
-    name: "my-kb",
-    knowledgeSources: new KnowledgeSourceReference[] 
-    { 
-        new KnowledgeSourceReference("hotels-sample-knowledge-source"),
-        new KnowledgeSourceReference("earth-knowledge-source")
-    }
-)
-{
-    Description = "This knowledge base handles questions directed at two unrelated sample indexes.",
-    RetrievalInstructions = "Use the hotels knowledge source for queries about where to stay, otherwise use the earth at night knowledge source.",
-    AnswerInstructions = "Provide a two sentence concise and informative answer based on the retrieved documents.",
-    OutputMode = KnowledgeRetrievalOutputMode.AnswerSynthesis,
-    Models = { new KnowledgeBaseAzureOpenAIModel(azureOpenAIParameters: aoaiParams) },
-    RetrievalReasoningEffort = new KnowledgeRetrievalLowReasoningEffort()
-};
-
-await indexClient.CreateOrUpdateKnowledgeBaseAsync(knowledgeBase);
-Console.WriteLine($"Knowledge base '{knowledgeBase.Name}' created or updated successfully.");
-```
-
-### Knowledge base properties
-
-Pass the following properties to create a knowledge base.
-
-| Name | Description | Type | Required |
-|--|--|--|--|
-| `name` | The name of the knowledge base. It must be unique within the knowledge bases collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | Yes |
-| `knowledgeSources` | One or more [supported knowledge sources](../../agentic-knowledge-source-overview.md#supported-knowledge-sources). | Array | Yes |
-| `Description` | A description of the knowledge base. The LLM uses the description to inform query planning. | String | No |
-| `RetrievalInstructions` | A prompt for the LLM to determine whether a knowledge source should be in scope for a query. Include this prompt when you have multiple knowledge sources. This field influences both knowledge source selection and query formulation. For example, instructions could append information or prioritize a knowledge source. Instructions are passed directly to the LLM, which means it's possible to provide instructions that break query planning, such as instructions that result in bypassing an essential knowledge source. | String | Yes |
-| `AnswerInstructions` | Custom instructions to shape synthesized answers. The default is null. For more information, see [Use answer synthesis for citation-backed responses](../../agentic-retrieval-how-to-answer-synthesis.md). | String | Yes |
-| `OutputMode` | Valid values are `AnswerSynthesis` for an LLM-formulated answer or `ExtractedData` for full search results that you can pass to an LLM as a downstream step. | String | Yes |
-| `Models` | A connection to a [supported LLM](#supported-models) used for answer formulation or query planning. In this preview, `Models` can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Foundry portal or a command-line request. Provide the parameters by using the [KnowledgeBaseAzureOpenAIModel class](/dotnet/api/azure.search.documents.indexes.models.knowledgebaseazureopenaimodel?view=azure-dotnet-preview&preserve-view=true). You can use role-based access control instead of API keys for the Azure AI Search connection to the model. | Object | No |
-| `RetrievalReasoningEffort` | Determines the level of LLM-related query processing. Valid values are `minimal`, `low` (default), and `medium`. For more information, see [Set the retrieval reasoning effort](../../agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). | Object | No |
-
-## Query a knowledge base
-
-Set up the instructions and messages to send to the LLM.
-
-```csharp
-string instructions = @"
-Use the earth at night index to answer the question. If you can't find relevant content, say you don't know.
-";
-
-var messages = new List<Dictionary<string, string>>
-{
-    new Dictionary<string, string>
-    {
-        { "role", "system" },
-        { "content", instructions }
-    }
-};
-```
-
-Call the `retrieve` action on the knowledge base to verify the LLM connection and return results. For more information about the `retrieve` request and response schema, see [Retrieve data using a knowledge base in Azure AI Search](../../agentic-retrieval-how-to-retrieve.md).
-
-Replace "Where does the ocean look green?" with a query string that's valid for your knowledge sources.
-
-```csharp
-using Azure.Search.Documents.KnowledgeBases;
-using Azure.Search.Documents.KnowledgeBases.Models;
-
-var baseClient = new KnowledgeBaseRetrievalClient(
-    endpoint: new Uri(searchEndpoint),
-    knowledgeBaseName: knowledgeBaseName,
-    tokenCredential: new DefaultAzureCredential()
-);
-
-messages.Add(new Dictionary<string, string>
-{
-    { "role", "user" },
-    { "content", @"Where does the ocean look green?" }
-});
-
-var retrievalRequest = new KnowledgeBaseRetrievalRequest();
-foreach (Dictionary<string, string> message in messages) {
-    if (message["role"] != "system") {
-        retrievalRequest.Messages.Add(new KnowledgeBaseMessage(content: new[] { new KnowledgeBaseMessageTextContent(message["content"]) }) { Role = message["role"] });
-    }
-}
-retrievalRequest.RetrievalReasoningEffort = new KnowledgeRetrievalLowReasoningEffort();
-var retrievalResult = await baseClient.RetrieveAsync(retrievalRequest);
-
-messages.Add(new Dictionary<string, string>
-{
-    { "role", "assistant" },
-    { "content", (retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent).Text }
-});
-
-(retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent).Text 
-
-// Print the response, activity, and references
-Console.WriteLine("Response:");
-Console.WriteLine((retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text);
-```
-
-**Key points:**
-
-+ [KnowledgeBaseRetrievalRequest](/dotnet/api/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest?view=azure-dotnet-preview&preserve-view=true) is the input contract for the retrieval request.
-
-+ [RetrievalReasoningEffort](/dotnet/api/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest.retrievalreasoningeffort?view=azure-dotnet-preview#azure-search-documents-knowledgebases-models-knowledgebaseretrievalrequest-retrievalreasoningeffort&preserve-view=true) is required. Setting it to `minimal` excludes LLMs from the query pipeline and only intents are used for the query input. The default is `low` and it supports LLM-based query planning and answer synthesis with messages and context.
-
-+ [`knowledgeSourceParams`](/dotnet/api/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest.knowledgesourceparams?view=azure-dotnet-preview&preserve-view=true) are used to overwrite default parameters at query time.
-
-The response to the sample query might look like the following example:
-
-```http
-  "response": [
-    {
-      "content": [
-        {
-          "type": "text",
-          "text": "The ocean appears green off the coast of Antarctica due to phytoplankton flourishing in the water, particularly in Granite Harbor near Antarctica’s Ross Sea, where they can grow in large quantities during spring, summer, and even autumn under the right conditions [ref_id:0]. Additionally, off the coast of Namibia, the ocean can also look green due to blooms of phytoplankton and yellow-green patches of sulfur precipitating from bacteria in oxygen-depleted waters [ref_id:1]. In the Strait of Georgia, Canada, the waters turned bright green due to a massive bloom of coccolithophores, a type of phytoplankton [ref_id:5]. Furthermore, a milky green and blue bloom was observed off the coast of Patagonia, Argentina, where nutrient-rich waters from different currents converge [ref_id:6]. Lastly, a large bloom of cyanobacteria was captured in the Baltic Sea, which can also give the water a green appearance [ref_id:9]."
-        }
-      ]
-    }
-  ]
-```
-
-## Delete a knowledge base
-
-If you no longer need the knowledge base or need to rebuild it on your search service, use this request to delete the object.
-
-```csharp
-using Azure.Search.Documents.Indexes;
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), credential);
-
-await indexClient.DeleteKnowledgeBaseAsync(knowledgeBaseName);
-System.Console.WriteLine($"Knowledge base '{knowledgeBaseName}' deleted successfully.");
-```
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "C#によるナレッジベースの作成に関するドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI SearchにおけるC#を使用したナレッジベースの作成に関するドキュメントが完全に削除されたことを示しています。331行の情報が削除され、ナレッジベースの定義、作成、更新、削除の手順やコードサンプルが含まれていました。このドキュメントでは、エージェントによるデータ取得プロセスを統括するために必要な情報やプロパティの設定について詳細に説明されていました。

削除された内容には、ナレッジベースが検索可能なコンテンツを指す知識源の指定方法、LLM（大規模言語モデル）との接続方法、及びクエリ実行時のプロパティ設定に関する記述がありました。また、ナレッジベースの作成や取得、クエリの実行手順が示されたサンプルコードも含まれていました。

この変更により、C#を使用してAzure AI Search内のナレッジベースを操作するための有用なリファレンスが失われ、開発者はその代替手段や情報を他の資料を通じて探す必要が生じます。したがって、Azure AI Searchを効果的に利用するための学習や実装に関して生産性が低下する可能性があります。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-python.md{#item-4e498f}

<details>
<summary>Diff</summary>
````diff
@@ -1,278 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/17/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-In Azure AI Search, a *knowledge base* is a top-level object that orchestrates [agentic retrieval](../../agentic-retrieval-overview.md). It defines which knowledge sources to query and the default behavior for retrieval operations. At query time, the [retrieve method](../../agentic-retrieval-how-to-retrieve.md) targets the knowledge base to run the configured retrieval pipeline.
-
-You can create a knowledge base in a [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) workload in the Microsoft Foundry (new) portal. You also need a knowledge base in any agentic solutions that you create using the Azure AI Search APIs.
-
-A knowledge base specifies:
-
-+ One or more knowledge sources that point to searchable content.
-+ An optional LLM that provides reasoning capabilities for query planning and answer formulation.
-+ A retrieval reasoning effort that determines whether an LLM is invoked and manages cost, latency, and quality.
-+ Custom properties that control routing, source selection, output format, and object encryption.
-
-After you create a knowledge base, you can update its properties at any time. If the knowledge base is in use, updates take effect on the next retrieval.
-
-> [!IMPORTANT]
-> 2025-11-01-preview renames the 2025-08-01-preview "knowledge agent" to "knowledge base." This is a breaking change. We recommend [migrating existing code](../../agentic-retrieval-how-to-migrate.md) to the new APIs as soon as possible.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). If you're using a [managed identity](../../search-how-to-managed-identities.md) for role-based access to deployed models, your search service must be on the Basic pricing tier or higher.
-
-+ Azure OpenAI with a [supported LLM](#supported-models) deployment.
-
-+ One or more [knowledge sources](../../agentic-knowledge-source-overview.md#supported-knowledge-sources) on your search service.
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md). **Search Service Contributor** can create and manage a knowledge base. **Search Index Data Reader** can run queries. Alternatively, you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-+ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
-
-### Supported models
-
-Use one of the following LLMs from Azure OpenAI in Foundry Models. For deployment instructions, see [Deploy Microsoft Foundry Models in the Foundry portal](/azure/ai-foundry/how-to/deploy-models-openai).
-
-+ `gpt-4o`
-+ `gpt-4o-mini`
-+ `gpt-4.1`
-+ `gpt-4.1-nano`
-+ `gpt-4.1-mini`
-+ `gpt-5`
-+ `gpt-5-nano`
-+ `gpt-5-mini`
-
-## Configure access
-
-Azure AI Search needs access to the LLM from Azure OpenAI. We recommend Microsoft Entra ID for authentication and role-based access for authorization. You must be an **Owner or User Access Administrator** to assign roles. If roles aren't feasible, use key-based authentication instead.
-
-### [**Use roles**](#tab/rbac)
-
-1. [Configure Azure AI Search to use a managed identity](../../search-how-to-managed-identities.md).
-
-1. On your model provider, such as Foundry Models, assign **Cognitive Services User** to the managed identity of your search service. If you're testing locally, assign the same role to your user account.
-
-1. For local testing, follow the steps in [Quickstart: Connect without keys](../../search-get-started-rbac.md) to sign in to a specific subscription and tenant. Use `DefaultAzureCredential` instead of `AzureKeyCredential` in each request, which should look similar to the following example:
-
-    ```python
-    # Authenticate using roles
-    from azure.identity import DefaultAzureCredential
-    index_client = SearchIndexClient(endpoint = "search_url", credential = DefaultAzureCredential())
-    ```
-    
-### [**Use keys**](#tab/keys)
-
-1. [Copy an Azure AI Search admin API key](../../search-security-api-keys.md#find-existing-keys) from the Azure portal.
-
-1. Use `AzureKeyCredential` to specify the API key in each request. Your code should look similar to the following example:
-
-    ```python
-    # Authenticate using keys
-    from azure.core.credentials import AzureKeyCredential
-    index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
-    ```
-    
----
-
-> [!IMPORTANT]
-> Code snippets in this article use API keys. If you use role-based authentication, update each request accordingly. In a request that specifies both approaches, the API key takes precedence.
-
-## Check for existing knowledge bases
-
-Knowing about existing knowledge bases is helpful for either reuse or naming new objects. Any 2025-08-01-preview knowledge agents are returned in the knowledge bases collection.
-
-Run the following code to list existing knowledge bases by name.
-
-```python
-# List knowledge bases by name
-import requests
-import json
-
-endpoint = "{search_url}/knowledgebases"
-params = {"api-version": "2025-11-01-preview", "$select": "name"}
-headers = {"api-key": "{api_key}"}
-
-response = requests.get(endpoint, params = params, headers = headers)
-print(json.dumps(response.json(), indent = 2))
-```
-
-You can also return a single knowledge base by name to review its JSON definition.
-
-```python
-# Get a knowledge base definition
-import requests
-import json
-
-endpoint = "{search_url}/knowledgebases/{knowledge_base_name}"
-params = {"api-version": "2025-11-01-preview"}
-headers = {"api-key": "{api_key}"}
-
-response = requests.get(endpoint, params = params, headers = headers)
-print(json.dumps(response.json(), indent = 2))
-```
-
-The following JSON is an example response for a knowledge base.
-
-```json
-{
-  "name": "my-kb",
-  "description": "A sample knowledge base.",
-  "retrievalInstructions": null,
-  "answerInstructions": null,
-  "outputMode": null,
-  "knowledgeSources": [
-    {
-      "name": "my-blob-ks"
-    }
-  ],
-  "models": [],
-  "encryptionKey": null,
-  "retrievalReasoningEffort": {
-    "kind": "low"
-  }
-}
-```
-
-## Create a knowledge base
-
-A knowledge base drives the agentic retrieval pipeline. In application code, other agents or chatbots call it.
-
-A knowledge base connects knowledge sources (searchable content) to an LLM deployment from Azure OpenAI. Properties on the LLM establish the connection, while properties on the knowledge source establish defaults that inform query execution and the response.
-
-Run the following code to create a knowledge base.
-
-```python
-# Create a knowledge base
-from azure.core.credentials import AzureKeyCredential
-from azure.search.documents.indexes import SearchIndexClient
-from azure.search.documents.indexes.models import KnowledgeBase, KnowledgeBaseAzureOpenAIModel, KnowledgeSourceReference, AzureOpenAIVectorizerParameters, KnowledgeRetrievalOutputMode, KnowledgeRetrievalLowReasoningEffort
-
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
-
-aoai_params = AzureOpenAIVectorizerParameters(
-    resource_url = "aoai_endpoint",
-    api_key="aoai_api_key",
-    deployment_name = "aoai_gpt_deployment",
-    model_name = "aoai_gpt_model",
-)
-
-knowledge_base = KnowledgeBase(
-    name = "my-kb",
-    description = "This knowledge base handles questions directed at two unrelated sample indexes.",
-    retrieval_instructions = "Use the hotels knowledge source for queries about where to stay, otherwise use the earth at night knowledge source.",
-    answer_instructions = "Provide a two sentence concise and informative answer based on the retrieved documents.",
-    output_mode = KnowledgeRetrievalOutputMode.ANSWER_SYNTHESIS,
-    knowledge_sources = [
-        KnowledgeSourceReference(name = "hotels-ks"),
-        KnowledgeSourceReference(name = "earth-at-night-ks"),
-    ],
-    models = [KnowledgeBaseAzureOpenAIModel(azure_open_ai_parameters = aoai_params)],
-    encryption_key = None,
-    retrieval_reasoning_effort = KnowledgeRetrievalLowReasoningEffort,
-)
-
-index_client.create_or_update_knowledge_base(knowledge_base)
-print(f"Knowledge base '{knowledge_base.name}' created or updated successfully.")
-```
-
-### Knowledge base properties
-
-Pass the following properties to create a knowledge base.
-
-| Name | Description | Type | Required |
-|--|--|--|--|
-| `name` | The name of the knowledge base. It must be unique within the knowledge bases collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | Yes |
-| `description` | A description of the knowledge base. The LLM uses the description to inform query planning. | String | No |
-| `retrieval_instructions` | A prompt for the LLM to determine whether a knowledge source should be in scope for a query. Include this prompt when you have multiple knowledge sources. This field influences both knowledge source selection and query formulation. For example, instructions could append information or prioritize a knowledge source. Pass instructions directly to the LLM. It's possible to provide instructions that break query planning, such as instructions that result in bypassing an essential knowledge source. | String | Yes |
-| `answer_instructions` | Custom instructions to shape synthesized answers. The default is null. For more information, see [Use answer synthesis for citation-backed responses](../../agentic-retrieval-how-to-answer-synthesis.md). | String | Yes |
-| `output_mode` | Valid values are `answer_synthesis` for an LLM-formulated answer or `extracted_data` for full search results that you can pass to an LLM as a downstream step. | String | Yes |
-| `knowledge_sources` | One or more [supported knowledge sources](../../agentic-knowledge-source-overview.md#supported-knowledge-sources). | Array | Yes |
-| `models` | A connection to a [supported LLM](#supported-models) used for answer formulation or query planning. In this preview, `models` can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Foundry portal or a command-line request. You can use role-based access control instead of API keys for the Azure AI Search connection to the model. | Object | No |
-| `encryption_key` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge base and the generated objects. | Object | No |
-| `retrieval_reasoning_effort` | Determines the level of LLM-related query processing. Valid values are `minimal`, `low` (default), and `medium`. For more information, see [Set the retrieval reasoning effort](../../agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). | Object | No |
-
-## Query a knowledge base
-
-Call the `retrieve` action on the knowledge base to verify the LLM connection and return results. For more information about the `retrieve` request and response schema, see [Retrieve data using a knowledge base in Azure AI Search](../../agentic-retrieval-how-to-retrieve.md).
-
-Replace "Where does the ocean look green?" with a query string that's valid for your knowledge sources.
-
-```python
-# Send grounding request
-from azure.core.credentials import AzureKeyCredential
-from azure.search.documents.knowledgebases import KnowledgeBaseRetrievalClient
-from azure.search.documents.knowledgebases.models import KnowledgeBaseMessage, KnowledgeBaseMessageTextContent, KnowledgeBaseRetrievalRequest, SearchIndexKnowledgeSourceParams
-
-kb_client = KnowledgeBaseRetrievalClient(endpoint = "search_url", knowledge_base_name = "knowledge_base_name", credential = AzureKeyCredential("api_key"))
-
-request = KnowledgeBaseRetrievalRequest(
-    messages=[
-        KnowledgeBaseMessage(
-            role = "assistant",
-            content = [KnowledgeBaseMessageTextContent(text = "Use the earth at night index to answer the question. If you can't find relevant content, say you don't know.")]
-        ),
-        KnowledgeBaseMessage(
-            role = "user",
-            content = [KnowledgeBaseMessageTextContent(text = "Where does the ocean look green?")]
-        ),
-    ],
-    knowledge_source_params=[
-        SearchIndexKnowledgeSourceParams(
-            knowledge_source_name = "earth-at-night-ks",
-            include_references = True,
-            include_reference_source_data = True,
-            always_query_source = False,
-        )
-    ],
-    include_activity = True,
-)
-
-result = kb_client.retrieve(request)
-print(result.response[0].content[0].text)
-```
-
-**Key points:**
-
-+ [`messages`](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview#knowledgeagentmessage&preserve-view=true) is required, but you can run this example by using just the `user` role that provides the query.
-
-+ [`knowledge_source_params`](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview#searchindexknowledgesourceparams&preserve-view=true) specifies one or more query targets. For each knowledge source, you can specify how much information to include in the output.
-
-The response to the sample query might look like the following example:
-
-```http
-  "response": [
-    {
-      "content": [
-        {
-          "type": "text",
-          "text": "The ocean appears green off the coast of Antarctica due to phytoplankton flourishing in the water, particularly in Granite Harbor near Antarctica’s Ross Sea, where they can grow in large quantities during spring, summer, and even autumn under the right conditions [ref_id:0]. Additionally, off the coast of Namibia, the ocean can also look green due to blooms of phytoplankton and yellow-green patches of sulfur precipitating from bacteria in oxygen-depleted waters [ref_id:1]. In the Strait of Georgia, Canada, the waters turned bright green due to a massive bloom of coccolithophores, a type of phytoplankton [ref_id:5]. Furthermore, a milky green and blue bloom was observed off the coast of Patagonia, Argentina, where nutrient-rich waters from different currents converge [ref_id:6]. Lastly, a large bloom of cyanobacteria was captured in the Baltic Sea, which can also give the water a green appearance [ref_id:9]."
-        }
-      ]
-    }
-  ]
-```
-
-## Delete a knowledge base
-
-If you no longer need the knowledge base or need to rebuild it on your search service, use this request to delete the object.
-
-```python
-# Delete a knowledge base
-from azure.core.credentials import AzureKeyCredential 
-from azure.search.documents.indexes import SearchIndexClient
-
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
-index_client.delete_knowledge_base("knowledge_base_name")
-print(f"Knowledge base deleted successfully.")
-```
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Pythonによるナレッジベースの作成に関するドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI SearchにおけるPythonを使用したナレッジベースの作成に関するドキュメントが完全に削除されたことを示しています。278行の情報が削除され、ナレッジベースの定義、作成、更新、削除の手順および関連するコードサンプルが含まれていました。このドキュメントでは、ナレッジベースがエージェントによるデータ取得プロセスを管理する重要な要素であることが説明されていました。

削除された内容には、ナレッジベースの作成方法や、それに関連するLLM（大規模言語モデル）との接続設定、クエリ実行時の知識源の指定方法、ポリシー設定に関する情報が含まれていました。また、ナレッジベースを利用してクエリを実行する方法や、レスポンスの処理に関するコードスニペットも示されていました。

この変更により、Pythonを使用してAzure AI Search内のナレッジベースを操作する開発者にとっての重要なリファレンスが失われ、代わりに他の情報源を参照する必要が生じます。その結果、Azure AI Searchを効果的に利用するための学習や実装に影響が出る可能性があります。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-rest.md{#item-37851c}

<details>
<summary>Diff</summary>
````diff
@@ -1,270 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 01/23/2026
----
-
-[!INCLUDE [Feature preview](../previews/preview-generic.md)]
-
-In Azure AI Search, a *knowledge base* is a top-level object that orchestrates [agentic retrieval](../../agentic-retrieval-overview.md). It defines which knowledge sources to query and the default behavior for retrieval operations. At query time, the [retrieve method](../../agentic-retrieval-how-to-retrieve.md) targets the knowledge base to run the configured retrieval pipeline.
-
-You can create a knowledge base in a [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) workload in the Microsoft Foundry (new) portal. You also need a knowledge base in any agentic solutions that you create using the Azure AI Search APIs.
-
-A knowledge base specifies:
-
-+ One or more knowledge sources that point to searchable content.
-+ An optional LLM that provides reasoning capabilities for query planning and answer formulation.
-+ A retrieval reasoning effort that determines whether an LLM is invoked and manages cost, latency, and quality.
-+ Custom properties that control routing, source selection, output format, and object encryption.
-
-After you create a knowledge base, you can update its properties at any time. If the knowledge base is in use, updates take effect on the next retrieval.
-
-> [!IMPORTANT]
-> 2025-11-01-preview renames the 2025-08-01-preview "knowledge agent" to "knowledge base." This is a breaking change. We recommend [migrating existing code](../../agentic-retrieval-how-to-migrate.md) to the new APIs as soon as possible.
-
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
-## Prerequisites
-
-+ Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). If you're using a [managed identity](../../search-how-to-managed-identities.md) for role-based access to deployed models, your search service must be on the Basic pricing tier or higher.
-
-+ Azure OpenAI with a [supported LLM](#supported-models) deployment.
-
-+ One or more [knowledge sources](../../agentic-knowledge-source-overview.md#supported-knowledge-sources) on your search service.
-
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md). **Search Service Contributor** can create and manage a knowledge base. **Search Index Data Reader** can run queries. Alternatively, you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-+ The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
-
-### Supported models
-
-Use one of the following LLMs from Azure OpenAI in Foundry Models. For deployment instructions, see [Deploy Microsoft Foundry Models in the Foundry portal](/azure/ai-foundry/how-to/deploy-models-openai).
-
-+ `gpt-4o`
-+ `gpt-4o-mini`
-+ `gpt-4.1`
-+ `gpt-4.1-nano`
-+ `gpt-4.1-mini`
-+ `gpt-5`
-+ `gpt-5-nano`
-+ `gpt-5-mini`
-
-## Configure access
-
-Azure AI Search needs access to the LLM from Azure OpenAI. We recommend Microsoft Entra ID for authentication and role-based access for authorization. To assign roles, you must be an **Owner or User Access Administrator**. If you can't use roles, use key-based authentication instead.
-
-### [**Use roles**](#tab/rbac)
-
-1. [Configure Azure AI Search to use a managed identity](../../search-how-to-managed-identities.md).
-
-1. On your model provider, such as Foundry Models, assign **Cognitive Services User** to the managed identity of your search service. If you're testing locally, assign the same role to your user account.
-
-1. For local testing, follow the steps in [Quickstart: Connect without keys](../../search-get-started-rbac.md) to get a personal access token for a specific subscription and tenant. Specify your access token in each request, which should look similar to the following example:
-
-    ```http
-    # List indexes using roles
-    GET https://{{search-url}}/indexes?api-version=2025-11-01-preview
-    Content-Type: application/json
-    Authorization: Bearer {{access-token}}
-    ```
-
-### [**Use keys**](#tab/keys)
-
-1. [Copy an Azure AI Search admin API key](../../search-security-api-keys.md#find-existing-keys) from the Azure portal.
-
-1. Specify the API key in each request. The key should look similar to the following example:
-
-   ```http
-   # List indexes using keys
-   GET {{search-url}}/indexes?api-version=2025-11-01-preview
-   Content-Type: application/json
-   api-key: {{search-api-key}}
-   ```
-
----
-
-> [!IMPORTANT]
-> Code snippets in this article use API keys. If you use role-based authentication, update each request accordingly. In a request that specifies both approaches, the API key takes precedence.
-
-## Check for existing knowledge bases
-
-A knowledge base is a top-level, reusable object. Knowing about existing knowledge bases is helpful for either reuse or naming new objects. Any 2025-08-01-preview knowledge agents are returned in the knowledge bases collection.
-
-Use [Knowledge Bases - List (REST API)](/rest/api/searchservice/knowledge-bases/list?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to list knowledge bases by name and type.
-
-```http
-# List knowledge bases
-GET {{search-url}}/knowledgebases?api-version=2025-11-01-preview&$select=name
-Content-Type: application/json
-api-key: {{search-api-key}}
-```
-
-You can also return a single knowledge base by name to review its JSON definition.
-
-```http
-# Get knowledge base
-GET {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version=2025-11-01-preview
-Content-Type: application/json
-api-key: {{search-api-key}}
-```
-
-The following JSON is an example response for a knowledge base.
-
-```json
-{
-  "name": "my-kb",
-  "description": "A sample knowledge base.",
-  "retrievalInstructions": null,
-  "answerInstructions": null,
-  "outputMode": null,
-  "knowledgeSources": [
-    {
-      "name": "my-blob-ks"
-    }
-  ],
-  "models": [],
-  "encryptionKey": null,
-  "retrievalReasoningEffort": {
-    "kind": "low"
-  }
-}
-```
-
-## Create a knowledge base
-
-A knowledge base drives the agentic retrieval pipeline. In application code, other agents or chatbots call it.
-
-A knowledge base connects knowledge sources (searchable content) to an LLM deployment from Azure OpenAI. Properties on the LLM establish the connection, while properties on the knowledge source set defaults that guide query execution and the response.
-
-Use [Knowledge Bases - Create or Update (REST API)](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to formulate the request.
-
-```http
-# Create a knowledge base
-PUT {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version=2025-11-01-preview
-Content-Type: application/json
-api-key: {{search-api-key}}
-
-{
-    "name" : "my-kb",
-    "description": "This knowledge base handles questions directed at two unrelated sample indexes.",
-    "retrievalInstructions": "Use the hotels knowledge source for queries about where to stay, otherwise use the earth at night knowledge source.",
-    "answerInstructions": null,
-    "outputMode": "answerSynthesis",
-    "knowledgeSources": [
-        {
-            "name": "hotels-ks"
-        },
-        {
-            "name": "earth-at-night-ks"
-        }
-    ],
-    "models" : [ 
-        {
-            "kind": "azureOpenAI",
-            "azureOpenAIParameters": {
-                "resourceUri": "{{model-provider-url}}",
-                "apiKey": "{{model-api-key}}",
-                "deploymentId": "gpt-4.1-mini",
-                "modelName": "gpt-4.1-mini"
-            }
-        }
-    ],
-    "encryptionKey": null,
-    "retrievalReasoningEffort": {
-        "kind": "low"
-    }
-}
-```
-
-### Knowledge base properties
-
-Pass the following properties to create a knowledge base.
-
-| Name | Description | Type | Required |
-|--|--|--|--|
-| `name` | The name of the knowledge base. It must be unique within the knowledge bases collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | Yes |
-| `description` | A description of the knowledge base. The LLM uses the description to inform query planning. | String | No |
-| `retrievalInstructions` | A prompt for the LLM to determine whether a knowledge source should be in scope for a query. Include this prompt when you have multiple knowledge sources. This field influences both knowledge source selection and query formulation. For example, instructions could append information or prioritize a knowledge source. You pass instructions directly to the LLM, which means it's possible to provide instructions that break query planning, such as instructions that result in bypassing an essential knowledge source. | String | Yes |
-| `answerInstructions` | Custom instructions to shape synthesized answers. The default is null. For more information, see [Use answer synthesis for citation-backed responses](../../agentic-retrieval-how-to-answer-synthesis.md). | String | Yes |
-| `outputMode` | Valid values are `answerSynthesis` for an LLM-formulated answer or `extractedData` for full search results that you can pass to an LLM as a downstream step. | String | Yes |
-| `knowledgeSources` | One or more [supported knowledge sources](../../agentic-knowledge-source-overview.md#supported-knowledge-sources). | Array | Yes |
-| `models` | A connection to a [supported LLM](#supported-models) used for answer formulation or query planning. In this preview, `models` can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Foundry portal or a command-line request. You can use role-based access control instead of API keys for the Azure AI Search connection to the model. | Object | No |
-| `encryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge base and the generated objects. | Object | No |
-| `retrievalReasoningEffort.kind` | Determines the level of LLM-related query processing. Valid values are `minimal`, `low` (default), and `medium`. For more information, see [Set the retrieval reasoning effort](../../agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). | Object | No |
-
-## Query a knowledge base
-
-Call the `retrieve` action on the knowledge base to verify the LLM connection and return results. For more information about the `retrieve` request and response schema, see [Retrieve data using a knowledge base in Azure AI Search](../../agentic-retrieval-how-to-retrieve.md).
-
-Use [Knowledge Retrieval - Retrieve (REST API)](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to formulate the request. Replace "Where does the ocean look green?" with a query string that's valid for your knowledge sources.
-
-```http
-# Send grounding request
-POST {{search-url}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2025-11-01-preview
-Content-Type: application/json
-api-key: {{search-api-key}}
-
-{
-    "messages" : [
-        { "role" : "assistant",
-                "content" : [
-                  { "type" : "text", "text" : "Use the earth at night index to answer the question. If you can't find relevant content, say you don't know." }
-                ]
-        },
-        {
-            "role" : "user",
-            "content" : [
-                {
-                    "text" : "Where does the ocean look green?",
-                    "type" : "text"
-                }
-            ]
-        }
-    ],
-    "includeActivity": true,
-    "knowledgeSourceParams": [
-        {
-            "knowledgeSourceName": "earth-at-night-ks",
-            "kind": "searchIndex",
-            "includeReferences": true,
-            "includeReferenceSourceData": true,
-            "alwaysQuerySource": false
-        }
-  ]
-}
-```
-
-**Key points:**
-
-+ [`messages`](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview#knowledgeagentmessage&preserve-view=true) is required, but you can run this example by using just the `user` role that provides the query.
-
-+ [`knowledgeSourceParams`](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview#searchindexknowledgesourceparams&preserve-view=true) specifies one or more query targets. For each knowledge source, you can specify how much information to include in the output.
-
-The response to the sample query might look like the following example:
-
-```http
-  "response": [
-    {
-      "content": [
-        {
-          "type": "text",
-          "text": "The ocean appears green off the coast of Antarctica due to phytoplankton flourishing in the water, particularly in Granite Harbor near Antarctica’s Ross Sea, where they can grow in large quantities during spring, summer, and even autumn under the right conditions [ref_id:0]. Additionally, off the coast of Namibia, the ocean can also look green due to blooms of phytoplankton and yellow-green patches of sulfur precipitating from bacteria in oxygen-depleted waters [ref_id:1]. In the Strait of Georgia, Canada, the waters turned bright green due to a massive bloom of coccolithophores, a type of phytoplankton [ref_id:5]. Furthermore, a milky green and blue bloom was observed off the coast of Patagonia, Argentina, where nutrient-rich waters from different currents converge [ref_id:6]. Lastly, a large bloom of cyanobacteria was captured in the Baltic Sea, which can also give the water a green appearance [ref_id:9]."
-        }
-      ]
-    }
-  ]
-```
-
-## Delete a knowledge base
-
-If you no longer need the knowledge base or need to rebuild it on your search service, use this request to delete the object.
-
-```http
-# Delete a knowledge base
-DELETE {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version=2025-11-01-preview
-api-key: {{search-api-key}}
-```
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "REST APIによるナレッジベースの作成に関するドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI SearchにおけるREST APIを使用したナレッジベースの作成に関するドキュメントが完全に削除されたことを示しています。270行の情報が削除され、ナレッジベースの定義、作成、更新、削除の手順、およびそれに関連するHTTPリクエストの例が含まれていました。このドキュメントでは、ナレッジベースがエージェントによる情報取得プロセスを支えるための重要な要素であることが説明されていました。

削除された内容には、ナレッジベースの作成手順や、対象となる知識源、LLM（大規模言語モデル）との接続、及びクエリの実行に関する詳細が含まれていました。また、REST APIを使用してナレッジベースを操作するための具体的なHTTPリクエスト例も提供されており、これにより開発者は適切なリクエストを行う方法を学ぶことができました。

この変更により、REST APIを使用してAzure AI Searchでのナレッジベースを管理する開発者にとっての重要な情報源が失われ、他のリファレンスを探す必要が出てきます。その結果、Azure AI Searchを効果的に利用するための学習や実装に関して支障が出る可能性があります。

## articles/search/includes/how-tos/manage-index-portal.md{#item-7a1916}

<details>
<summary>Diff</summary>
````diff
@@ -1,68 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 07/03/2025
----
-
-After you [create an index](../../search-how-to-create-search-index.md), you can use the [Azure portal](https://portal.azure.com) to access its statistics and definition or remove it from your search service.
-
-This article describes how to manage an index without affecting its content. For guidance on modifying an index definition, see [Update or rebuild an index in Azure AI Search](../../search-howto-reindex.md).
-
-## Limitations
-
-The pricing tier of your search service determines the maximum number and size of your indexes, fields, and documents. For more information, see [Service limits in Azure AI Search](../../search-limits-quotas-capacity.md).
-
-Otherwise, the following limitations apply to index management:
-
-+ You can't take an index offline for maintenance. Indexes are always available for search operations.
-
-+ You can't directly copy or duplicate an index within or across search services. However, you can use the backup and restore sample for [.NET](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore) or [Python](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) to achieve similar functionality.
-
-## View all indexes
-
-To view all your indexes:
-
-1. Go to your search service in the [Azure portal](https://portal.azure.com).
-
-1. From the left pane, select **Search management** > **Indexes**.
-
-   :::image type="content" source="../../media/search-how-to-manage-index/indexes-page.png" alt-text="Screenshot of the indexes page in the portal." border="true" lightbox="../../media/search-how-to-manage-index/indexes-page.png":::
-
-   By default, the indexes are sorted by name in ascending order. You can sort by **Name**, **Document count**, **Vector index quota usage**, or **Total storage size** by selecting the corresponding column header.
-
-## View an index's statistics
-
-On the index page, the portal provides the following statistics:
-
-+ Number of documents in the index.
-+ Storage space used by the index.
-+ Vector storage space used by the index.
-+ Maximum storage space for each index on your search service, which [depends on your pricing tier](../../search-limits-quotas-capacity.md). This value doesn't represent the total storage currently available to the index.
-
-:::image type="content" source="../../media/search-how-to-manage-index/index-statistics.png" alt-text="Screenshot of the index statistics in the portal." border="true" lightbox="../../media/search-how-to-manage-index/index-statistics.png":::
-
-## View an index's definition
-
-Each index is defined by fields and optional components that enhance search capabilities, such as analyzers, normalizers, tokenizers, and synonym maps. This definition determines the index's structure and behavior during indexing and querying.
-
-On the index page, select **Edit JSON** to view its complete definition.
-
-:::image type="content" source="../../media/search-how-to-manage-index/edit-json-button.png" alt-text="Screenshot of the Edit JSON button in the portal." border="true" lightbox="../../media/search-how-to-manage-index/edit-json-button.png":::
-
-<!--
-> [!NOTE]
-> The portal doesn't support synonym map definitions. You can use the portal to view existing synonyms, but you can't create them or assign them to fields. For more information, see [Add synonyms in Azure AI Search](../../search-synonym.md).
--->
-
-## Delete an index
-
-> [!WARNING]
-> You can't undo an index deletion. Before you proceed, make sure that you want to permanently remove the index and its documents from your search service.
-
-On the index page, select **Delete** to initiate the deletion process.
-
-:::image type="content" source="../../media/search-how-to-manage-index/delete-button.png" alt-text="Screenshot of the Delete button in the portal." border="true" lightbox="../../media/search-how-to-manage-index/delete-button.png":::
-
-The portal prompts you to confirm the deletion. After you select **Delete**, check your notifications to confirm that the deletion was successful.
-
-:::image type="content" source="../../media/search-how-to-manage-index/delete-confirmation.png" alt-text="Screenshot of the deletion confirmation in the portal." border="true" lightbox="../../media/search-how-to-manage-index/delete-confirmation.png":::
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "インデックス管理に関するドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI Searchにおけるインデックス管理に関するドキュメントが完全に削除されたことを示しています。68行の情報が削除され、インデックスの作成、表示、統計確認、削除などの管理手順が詳細に説明されていました。削除された内容には、インデックスに関連する制限や、Azure ポータルを使用してインデックスを管理する際の具体的な手順、さらにはインデックスの定義や統計にアクセスする方法が含まれていました。

この変更により、ユーザーはインデックスを効果的に管理するための重要な情報源を失うことになります。特に、インデックスの統計情報やその定義に関しての操作手順がなくなることで、インデックスの状況を把握し、必要に応じてインデックスを削除する手続きが難しくなります。そのため、Azure AI Searchを活用している開発者やユーザーにとっては、他のリファレンスを参照する必要が生じます。

## articles/search/includes/how-tos/manage-index-rest.md{#item-8bc592}

<details>
<summary>Diff</summary>
````diff
@@ -1,70 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 07/03/2025
----
-
-After you [create an index](../../search-how-to-create-search-index.md), you can use the [Azure AI Search REST APIs](/rest/api/searchservice/) to access its statistics and definition or remove it from your search service.
-
-This article describes how to manage an index without affecting its content. For guidance on modifying an index definition, see [Update or rebuild an index in Azure AI Search](../../search-howto-reindex.md).
-
-## Limitations
-
-The pricing tier of your search service determines the maximum number and size of your indexes, fields, and documents. For more information, see [Service limits in Azure AI Search](../../search-limits-quotas-capacity.md).
-
-Otherwise, the following limitations apply to index management:
-
-+ You can't take an index offline for maintenance. Indexes are always available for search operations.
-
-+ You can't directly copy or duplicate an index within or across search services. However, you can use the backup and restore sample for [.NET](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore) or [Python](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) to achieve similar functionality.
-
-## View all indexes
-
-Use [Indexes - List (REST API)](/rest/api/searchservice/indexes/list) to retrieve all indexes on your search service.
-
-```http
-### List all indexes
-GET https://[service name].search.windows.net/indexes?api-version=[api version]
-    Content-Type: application/json
-    api-key: [admin key]
-```
-
-## View an index's statistics
-
-Use [Indexes - Get Statistics (REST API)](/rest/api/searchservice/indexes/get-statistics) to retrieve the document count, storage usage, and vector storage usage of an index.
-
-```http
-### Get index statistics
-GET https://[service name].search.windows.net/indexes/[index name]/stats?api-version=[api version]
-    Content-Type: application/json
-    api-key: [admin key]
-```
-
-## View an index's definition
-
-Each index is defined by fields and optional components that enhance search capabilities, such as analyzers, normalizers, tokenizers, and synonym maps. This definition determines the index's structure and behavior during indexing and querying.
-
-Use [Indexes - Get (REST API)](/rest/api/searchservice/indexes/get) to retrieve the JSON definition of an index.
-
-```http
-### Get index definition
-GET https://[service name].search.windows.net/indexes/[index name]?api-version=[api version]
-    Content-Type: application/json
-    api-key: [admin key]
-```
-
-## Delete an index
-
-> [!WARNING]
-> You can't undo an index deletion. Before you proceed, make sure that you want to permanently remove the index and its documents from your search service.
-
-Use [Indexes - Delete (REST API)](/rest/api/searchservice/indexes/delete) to permanently delete an index.
-
-```http
-### Delete an index
-DELETE https://[service name].search.windows.net/indexes/[index name]?api-version=[api version]
-    Content-Type: application/json
-    api-key: [admin key]
-```
-
-If the index was deleted successfully, you should receive an `HTTP/1.1 204 No Content` response.
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "REST APIによるインデックス管理に関するドキュメントの削除"
}
```

### Explanation
この修正は、Azure AI SearchのREST APIを使用したインデックス管理に関するドキュメントが完全に削除されたことを示しています。70行の情報が削除され、インデックスの作成後にその統計や定義にアクセスする方法、インデックスの削除、および構造の確認方法が詳細に説明されていました。

削除された内容には、REST APIを使用してインデックスを管理するための具体的なHTTPリクエストのサンプルが含まれており、ユーザーはインデックスのリストを取得したり、統計情報を取得したり、インデックスの定義を確認したり、さらにはインデックスを削除するための手順を学ぶことができました。

この変更により、Azure AI Searchを使用している開発者やユーザーにとって、インデックスを効果的に管理するための重要な情報源が失われることになります。このドキュメントの欠如は、特にインデックスの操作に関する知識を必要とするユーザーにとって障壁となる可能性があります。ユーザーは今後、他のソースを頼りにする必要があるでしょう。

## articles/search/includes/how-tos/manage-index-sdk.md{#item-02a160}

<details>
<summary>Diff</summary>
````diff
@@ -1,338 +0,0 @@
----
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 07/03/2025
----
-
-After you [create an index](../../search-how-to-create-search-index.md), you can use the Azure SDK for [.NET](/dotnet/api/overview/azure/search), [Java](/java/api/overview/azure/search-documents-readme), [JavaScript](/javascript/api/overview/azure/search-documents-readme), or [Python](/python/api/overview/azure/search-documents-readme) to access its statistics and definition or remove it from your search service.
-
-This article describes how to manage an index without affecting its content. For guidance on modifying an index definition, see [Update or rebuild an index in Azure AI Search](../../search-howto-reindex.md).
-
-## Limitations
-
-The pricing tier of your search service determines the maximum number and size of your indexes, fields, and documents. For more information, see [Service limits in Azure AI Search](../../search-limits-quotas-capacity.md).
-
-Otherwise, the following limitations apply to index management:
-
-+ You can't take an index offline for maintenance. Indexes are always available for search operations.
-
-+ You can't directly copy or duplicate an index within or across search services. However, you can use the backup and restore sample for [.NET](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore) or [Python](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) to achieve similar functionality.
-
-## View all indexes
-
-Use your preferred Azure SDK to retrieve all indexes on your search service.
-
-### [.NET](#tab/list-dotnet)
-
-The Azure SDK for .NET provides [GetIndexesAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.getindexesasync) for this task.
-
-```csharp
-// Create a SearchIndexClient
-var endpoint = new Uri("[service endpoint]");
-var credential = new AzureKeyCredential("[admin key]");
-var indexClient = new SearchIndexClient(endpoint, credential);
-
-// List all indexes
-await foreach (var index in indexClient.GetIndexesAsync())
-{
-    Console.WriteLine(index.Name);
-}
-```
-
-### [Java](#tab/list-java)
-
-The Azure SDK for Java provides `listIndexes` in the [SearchIndexAsyncClient](/java/api/com.azure.search.documents.indexes.searchindexasyncclient) class for this task.
-
-```java
-// Create a SearchIndexAsyncClient
-String endpoint = "[service endpoint]";
-String adminKey = "[admin key]";
-SearchIndexAsyncClient searchIndexAsyncClient = new SearchIndexClientBuilder()
-    .endpoint(endpoint)
-    .credential(new AzureKeyCredential(adminKey))
-    .buildAsyncClient();
-        
-// List all indexes
-searchIndexAsyncClient.listIndexes()
-    .subscribe(
-        index -> System.out.println(index.getName())
-    );
-```
-
-### [JavaScript](#tab/list-javascript)
-
-The Azure SDK for JavaScript provides `listIndexes` in the [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient) class for this task.
-
-```javascript
-// Create a SearchIndexClient
-const endpoint = "[service endpoint]";
-const adminKey = "[admin key]";
-const client = new SearchIndexClient(endpoint, new AzureKeyCredential(adminKey)
-);
-
-// List all indexes
-(async () => {
-    for await (const index of client.listIndexes()) {
-        console.log(index.name);
-    }
-})();
-```
-
-### [Python](#tab/list-python)
-
-The Azure SDK for Python provides `list_indexes` in the [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient) class for this task.
-
-```python
-# Create a SearchIndexClient
-endpoint = "[service endpoint]"
-admin_key = AzureKeyCredential("[admin key]")
-client = SearchIndexClient(endpoint=endpoint, credential=admin_key)
-
-# List all indexes
-for index in client.list_indexes():
-    print(index.name)
-```
-
----
-
-## View an index's statistics
-
-Use your preferred Azure SDK to retrieve the document count, storage usage, and vector storage usage of an index.
-
-### [.NET](#tab/stats-dotnet)
-
-The Azure SDK for .NET provides [GetIndexStatisticsAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.getindexstatisticsasync) for this task.
-
-```csharp
-// Create a SearchIndexClient
-var endpoint = new Uri("[service endpoint]");
-var credential = new AzureKeyCredential("[admin key]");
-var indexClient = new SearchIndexClient(endpoint, credential);
-
-// Get index statistics
-var statsResponse = await indexClient.GetIndexStatisticsAsync("[index name]");
-var stats = statsResponse.Value;
-Console.WriteLine($"Number of documents: {stats.DocumentCount:N0}");
-Console.WriteLine($"Storage consumed by index: {stats.StorageSize:N0} bytes");
-Console.WriteLine($"Storage consumed by vectors: {stats.VectorIndexSize:N0} bytes");
-```
-
-### [Java](#tab/stats-java)
-
-The Azure SDK for Java provides `getIndexStatistics` in the [SearchIndexAsyncClient](/java/api/com.azure.search.documents.indexes.searchindexasyncclient) class for this task.
-
-```java
-// Create a SearchIndexAsyncClient
-String endpoint = "[service endpoint]";
-String adminKey = "[admin key]";
-SearchIndexAsyncClient searchIndexAsyncClient = new SearchIndexClientBuilder()
-    .endpoint(endpoint)
-    .credential(new AzureKeyCredential(adminKey))
-    .buildAsyncClient();
-
-// Get index statistics
-SearchIndexStatistics stats = searchIndexAsyncClient.getIndexStatistics("[index name]").block();
-System.out.println("Number of documents: " + stats.getDocumentCount());
-System.out.println("Storage consumed by index: " + stats.getStorageSize() + " bytes");
-System.out.println("Storage consumed by vectors: " + stats.getVectorIndexSize() + " bytes");
-```
-
-### [JavaScript](#tab/stats-javascript)
-
-The Azure SDK for JavaScript provides `getIndexStatistics` in the [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient) class for this task.
-
-```javascript
-// Create a SearchIndexClient
-const endpoint = "[service endpoint]";
-const adminKey = "[admin key]";
-const client = new SearchIndexClient(endpoint, new AzureKeyCredential(adminKey)
-);
-
-// Get index statistics
-(async () => {
-    const stats = await client.getIndexStatistics("[index name]");
-    console.log(`Number of documents: ${stats.documentCount}`);
-    console.log(`Storage consumed by index: ${stats.storageSize} bytes`);
-    console.log(`Storage consumed by vectors: ${stats.vectorIndexSize} bytes`);
-})();
-```
-
-### [Python](#tab/stats-python)
-
-The Azure SDK for Python provides [get_index_statistics](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient) for this task.
-
-```python
-# Create a SearchIndexClient
-endpoint = "[service endpoint]"
-admin_key = AzureKeyCredential("[admin key]")
-client = SearchIndexClient(endpoint=endpoint, credential=admin_key)
-
-# Get index statistics
-stats = client.get_index_statistics("[index name]")
-print(f"Number of documents: {stats['document_count']}")
-print(f"Storage consumed by index: {stats['storage_size']} bytes")
-print(f"Storage consumed by vectors: {stats['vector_index_size']} bytes")
-```
-
----
-
-## View an index's definition
-
-Each index is defined by fields and optional components that enhance search capabilities, such as analyzers, normalizers, tokenizers, and synonym maps. This definition determines the index's structure and behavior during indexing and querying.
-
-Use your preferred Azure SDK to retrieve the JSON definition of an index.
-
-### [.NET](#tab/definition-dotnet)
-
-The Azure SDK for .NET provides [GetIndexAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.getindexasync) for this task.
-
-```csharp
-// Create a SearchIndexClient
-var endpoint = new Uri("[service endpoint]");
-var credential = new AzureKeyCredential("[admin key]");
-var indexClient = new SearchIndexClient(endpoint, credential);
-
-// Get index definition
-var index = await indexClient.GetIndexAsync("[index name]");
-string indexJson = JsonSerializer.Serialize(index.Value, new JsonSerializerOptions { WriteIndented = true });
-Console.WriteLine(indexJson);
-```
-
-### [Java](#tab/definition-java)
-
-The Azure SDK for Java provides `getIndex` in the [SearchIndexAsyncClient](/java/api/com.azure.search.documents.indexes.searchindexasyncclient) class for this task.
-
-```java
-// Create a SearchIndexAsyncClient
-String endpoint = "[service endpoint]";
-String adminKey = "[admin key]";
-SearchIndexAsyncClient searchIndexAsyncClient = new SearchIndexClientBuilder()
-    .endpoint(endpoint)
-    .credential(new AzureKeyCredential(adminKey))
-    .buildAsyncClient();
-
-// Get index definition
-searchIndexAsyncClient.getIndex("[index name]")
-    .subscribe(index -> {
-        try {
-            String prettyJson = new ObjectMapper()
-                .writerWithDefaultPrettyPrinter()
-                .writeValueAsString(index);
-            System.out.println(prettyJson);
-        } catch (Exception e) {
-            e.printStackTrace();
-        }
-    });
-```
-
-### [JavaScript](#tab/definition-javascript)
-
-The Azure SDK for JavaScript provides `getIndex` in the [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient) class for this task.
-
-```javascript
-// Create a SearchIndexClient
-const endpoint = "[service endpoint]";
-const adminKey = "[admin key]";
-const client = new SearchIndexClient(endpoint, new AzureKeyCredential(adminKey)
-);
-
-// Get index definition
-(async () => {
-    const index = await client.getIndex("[index name]");
-    console.log(JSON.stringify(index, null, 2));
-})();
-```
-
-### [Python](#tab/definition-python)
-
-The Azure SDK for Python provides `get_index` in the [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient) class for this task.
-
-```python
-# Create a SearchIndexClient
-endpoint = "[service endpoint]"
-admin_key = AzureKeyCredential("[admin key]")
-client = SearchIndexClient(endpoint=endpoint, credential=admin_key)
-
-# Get index definition
-index = client.get_index("[index name]")
-print(json.dumps(index.as_dict(), indent=2, sort_keys=True, ensure_ascii=False))
-```
-
----
-
-## Delete an index
-
-> [!WARNING]
-> You can't undo an index deletion. Before you proceed, make sure that you want to permanently remove the index and its documents from your search service.
-
-Use your preferred Azure SDK to permanently delete an index.
-
-### [.NET](#tab/delete-dotnet)
-
-The Azure SDK for .NET provides [DeleteIndexAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.deleteindexasync) for this task.
-
-```csharp
-// Create a SearchIndexClient
-var endpoint = new Uri("[service endpoint]");
-var credential = new AzureKeyCredential("[admin key]");
-var indexClient = new SearchIndexClient(endpoint, credential);
-
-// Delete the index
-await indexClient.DeleteIndexAsync("[index name]");
-Console.WriteLine("Index deleted successfully.");
-```
-
-### [Java](#tab/delete-java)
-
-The Azure SDK for Java provides `deleteIndex` in the [SearchIndexAsyncClient](/java/api/com.azure.search.documents.indexes.searchindexasyncclient) class for this task.
-
-```java
-// Create a SearchIndexAsyncClient
-String endpoint = "[service endpoint]";
-String adminKey = "[admin key]";
-SearchIndexAsyncClient searchIndexAsyncClient = new SearchIndexClientBuilder()
-    .endpoint(endpoint)
-    .credential(new AzureKeyCredential(adminKey))
-    .buildAsyncClient();
-
-// Delete the index
-searchIndexAsyncClient.deleteIndex("[index name]")
-    .subscribe(
-        unused -> System.out.println("Index deleted successfully.")
-    );
-```
-
-### [JavaScript](#tab/delete-javascript)
-
-The Azure SDK for JavaScript provides `deleteIndex` in the [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient) class for this task.
-
-```javascript
-// Create a SearchIndexClient
-const endpoint = "[service endpoint]";
-const adminKey = "[admin key]";
-const client = new SearchIndexClient(endpoint, new AzureKeyCredential(adminKey)
-);
-
-// Delete the index
-(async () => {
-    await client.deleteIndex("[index name]");
-    console.log("Index deleted successfully.");
-})();
-```
-
-### [Python](#tab/delete-python)
-
-The Azure SDK for Python provides `delete_index` in the [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient) class for this task.
-
-```python
-# Create a SearchIndexClient
-endpoint = "[service endpoint]"
-admin_key = AzureKeyCredential("[admin key]")
-client = SearchIndexClient(endpoint=endpoint, credential=admin_key)
-
-# Delete the index
-client.delete_index("[index name]")
-print("Index deleted successfully.")
-```
-
----
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "SDKによるインデックス管理に関するドキュメントの削除"
}
```

### Explanation
この修正は、Azure SDKを使用したインデックス管理に関するドキュメントが完全に削除されたことを示しています。338行の情報が削除され、Azure SDK for .NET、Java、JavaScript、Pythonを使用してインデックスの統計や定義にアクセスしたり、インデックスを削除したりする方法の詳細が含まれていました。

削除された内容には、各プログラミング言語に特有の操作手順があり、インデックスをリストアップしたり、その統計情報や定義を取得したり、インデックスを削除したりするための具体的なコードサンプルが含まれていました。

この変更により、Azure SDKを活用してインデックスを管理しようとしている開発者やユーザーにとって、重要な情報源が失われることになります。特に、インデックス管理の操作に関する具体的なコーディングの例が無くなることで、ユーザーは自力でこれらの操作を理解し、実装する必要があります。他の資料やリファレンスを参照することが求められるでしょう。

## articles/search/search-faq-frequently-asked-questions.yml{#item-eab2ba}

<details>
<summary>Diff</summary>
````diff
@@ -216,7 +216,7 @@ sections:
       - question: |
           Can I use the Azure portal to view and manage search content if my search service is behind an IP firewall or private endpoint?
         answer: |
-          You can use the Azure portal on a network-protected search service if you create a network exception that allows client and portal access. For more information, see [Connect through an IP firewall](./service-configure-firewall.md#configure-network-access-in-the-azure-portal) or [Connect through a private endpoint](./service-create-private-endpoint.md#portal-access-private-search-service).
+          You can use the Azure portal on a network-protected search service if you create a network exception that allows client and portal access. For more information, see [Connect through an IP firewall](./service-configure-firewall.md#configure-network-access) or [Connect through a private endpoint](./service-create-private-endpoint.md#portal-access-private-search-service).
 
 additionalContent: |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQセクションのリンク修正"
}
```

### Explanation
この修正は、Azureの検索に関するよくある質問（FAQ）セクションのリンク内容を微修正したことを示しています。具体的には、「IPファイアウォールを介して接続する」リンクの末尾が変更され、アクセスに関する説明が少し明確になりました。

変更前は、リンクが「ネットワークアクセスを構成する」という表現を含んでいましたが、変更後は「ネットワークアクセス」という表現に簡素化されています。この変更は情報の明確さを向上させることを目的としており、読者が正しい情報にアクセスできるようにするためのものです。

この修正により、ユーザーは必要なサポートドキュメントへ適切に到達することができるようになり、Azureサービスに対する理解をより深めることが期待されます。

## articles/search/search-how-to-manage-index.md{#item-6bf53b}

<details>
<summary>Diff</summary>
````diff
@@ -3,23 +3,482 @@ title: Index Management
 description: Learn how to manage indexes in Azure AI Search. Operations include viewing all indexes on your search service, checking index-specific statistics and definitions, and deleting indexes.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/03/2025
+ms.date: 04/14/2026
 ms.update-cycle: 365-days
 zone_pivot_groups: search-portal-sdks-rest
 ---
 
 # Manage an index in Azure AI Search
 
 ::: zone pivot="azure-portal"
-[!INCLUDE [Portal instructions](includes/how-tos/manage-index-portal.md)]
+
+After you [create an index](search-how-to-create-search-index.md), you can use the [Azure portal](https://portal.azure.com) to access its statistics and definition or remove it from your search service.
+
+::: zone-end
+
+::: zone pivot="rest"
+
+After you [create an index](search-how-to-create-search-index.md), you can use the [Azure AI Search REST APIs](/rest/api/searchservice/) to access its statistics and definition or remove it from your search service.
+
+::: zone-end
+
+::: zone pivot="azure-sdks"
+
+After you [create an index](search-how-to-create-search-index.md), you can use the Azure SDK for [.NET](/dotnet/api/overview/azure/search), [Java](/java/api/overview/azure/search-documents-readme), [JavaScript](/javascript/api/overview/azure/search-documents-readme), or [Python](/python/api/overview/azure/search-documents-readme) to access its statistics and definition or remove it from your search service.
+
+::: zone-end
+
+This article describes how to manage an index without affecting its content. For guidance on modifying an index definition, see [Update or rebuild an index in Azure AI Search](search-howto-reindex.md).
+
+## Limitations
+
+The pricing tier of your search service determines the maximum number and size of your indexes, fields, and documents. For more information, see [Service limits in Azure AI Search](search-limits-quotas-capacity.md).
+
+Otherwise, the following limitations apply to index management:
+
++ You can't take an index offline for maintenance. Indexes are always available for search operations.
+
++ You can't directly copy or duplicate an index within or across search services. However, you can use the backup and restore sample for [.NET](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore) or [Python](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) to achieve similar functionality.
+
+## View all indexes
+
+::: zone pivot="azure-portal"
+
+To view all your indexes:
+
+1. Go to your search service in the [Azure portal](https://portal.azure.com).
+
+1. From the left pane, select **Search management** > **Indexes**.
+
+   :::image type="content" source="media/search-how-to-manage-index/indexes-page.png" alt-text="Screenshot of the indexes page in the portal." border="true" lightbox="media/search-how-to-manage-index/indexes-page.png":::
+
+   By default, the indexes are sorted by name in ascending order. You can sort by **Name**, **Document count**, **Vector index quota usage**, or **Total storage size** by selecting the corresponding column header.
+
 ::: zone-end
 
 ::: zone pivot="rest"
-[!INCLUDE [REST API instructions](includes/how-tos/manage-index-rest.md)]
+
+Use [Indexes - List (REST API)](/rest/api/searchservice/indexes/list) to retrieve all indexes on your search service.
+
+```http
+### List all indexes
+GET https://[service name].search.windows.net/indexes?api-version=[api version]
+    Content-Type: application/json
+    api-key: [admin key]
+```
+
 ::: zone-end
 
 ::: zone pivot="azure-sdks"
-[!INCLUDE [Azure SDKs instructions](includes/how-tos/manage-index-sdk.md)]
+
+Use your preferred Azure SDK to retrieve all indexes on your search service.
+
+### [.NET](#tab/dotnet)
+
+The Azure SDK for .NET provides [GetIndexesAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.getindexesasync) for this task.
+
+```csharp
+// Create a SearchIndexClient
+var endpoint = new Uri("[service endpoint]");
+var credential = new AzureKeyCredential("[admin key]");
+var indexClient = new SearchIndexClient(endpoint, credential);
+
+// List all indexes
+await foreach (var index in indexClient.GetIndexesAsync())
+{
+    Console.WriteLine(index.Name);
+}
+```
+
+### [Java](#tab/java)
+
+The Azure SDK for Java provides `listIndexes` in the [SearchIndexAsyncClient](/java/api/com.azure.search.documents.indexes.searchindexasyncclient) class for this task.
+
+```java
+// Create a SearchIndexAsyncClient
+String endpoint = "[service endpoint]";
+String adminKey = "[admin key]";
+SearchIndexAsyncClient searchIndexAsyncClient = new SearchIndexClientBuilder()
+    .endpoint(endpoint)
+    .credential(new AzureKeyCredential(adminKey))
+    .buildAsyncClient();
+        
+// List all indexes
+searchIndexAsyncClient.listIndexes()
+    .subscribe(
+        index -> System.out.println(index.getName())
+    );
+```
+
+### [JavaScript](#tab/javascript)
+
+The Azure SDK for JavaScript provides `listIndexes` in the [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient) class for this task.
+
+```javascript
+// Create a SearchIndexClient
+const endpoint = "[service endpoint]";
+const adminKey = "[admin key]";
+const client = new SearchIndexClient(endpoint, new AzureKeyCredential(adminKey)
+);
+
+// List all indexes
+(async () => {
+    for await (const index of client.listIndexes()) {
+        console.log(index.name);
+    }
+})();
+```
+
+### [Python](#tab/python)
+
+The Azure SDK for Python provides `list_indexes` in the [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient) class for this task.
+
+```python
+# Create a SearchIndexClient
+endpoint = "[service endpoint]"
+admin_key = AzureKeyCredential("[admin key]")
+client = SearchIndexClient(endpoint=endpoint, credential=admin_key)
+
+# List all indexes
+for index in client.list_indexes():
+    print(index.name)
+```
+
+---
+
+::: zone-end
+
+## View an index's statistics
+
+::: zone pivot="azure-portal"
+
+On the index page, the portal provides the following statistics:
+
++ Number of documents in the index.
++ Storage space used by the index.
++ Vector storage space used by the index.
++ Maximum storage space for each index on your search service, which [depends on your pricing tier](search-limits-quotas-capacity.md). This value doesn't represent the total storage currently available to the index.
+
+:::image type="content" source="media/search-how-to-manage-index/index-statistics.png" alt-text="Screenshot of the index statistics in the portal." border="true" lightbox="media/search-how-to-manage-index/index-statistics.png":::
+
+::: zone-end
+
+::: zone pivot="rest"
+
+Use [Indexes - Get Statistics (REST API)](/rest/api/searchservice/indexes/get-statistics) to retrieve the document count, storage usage, and vector storage usage of an index.
+
+```http
+### Get index statistics
+GET https://[service name].search.windows.net/indexes/[index name]/stats?api-version=[api version]
+    Content-Type: application/json
+    api-key: [admin key]
+```
+
+::: zone-end
+
+::: zone pivot="azure-sdks"
+
+Use your preferred Azure SDK to retrieve the document count, storage usage, and vector storage usage of an index.
+
+### [.NET](#tab/dotnet)
+
+The Azure SDK for .NET provides [GetIndexStatisticsAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.getindexstatisticsasync) for this task.
+
+```csharp
+// Create a SearchIndexClient
+var endpoint = new Uri("[service endpoint]");
+var credential = new AzureKeyCredential("[admin key]");
+var indexClient = new SearchIndexClient(endpoint, credential);
+
+// Get index statistics
+var statsResponse = await indexClient.GetIndexStatisticsAsync("[index name]");
+var stats = statsResponse.Value;
+Console.WriteLine($"Number of documents: {stats.DocumentCount:N0}");
+Console.WriteLine($"Storage consumed by index: {stats.StorageSize:N0} bytes");
+Console.WriteLine($"Storage consumed by vectors: {stats.VectorIndexSize:N0} bytes");
+```
+
+### [Java](#tab/java)
+
+The Azure SDK for Java provides `getIndexStatistics` in the [SearchIndexAsyncClient](/java/api/com.azure.search.documents.indexes.searchindexasyncclient) class for this task.
+
+```java
+// Create a SearchIndexAsyncClient
+String endpoint = "[service endpoint]";
+String adminKey = "[admin key]";
+SearchIndexAsyncClient searchIndexAsyncClient = new SearchIndexClientBuilder()
+    .endpoint(endpoint)
+    .credential(new AzureKeyCredential(adminKey))
+    .buildAsyncClient();
+
+// Get index statistics
+SearchIndexStatistics stats = searchIndexAsyncClient.getIndexStatistics("[index name]").block();
+System.out.println("Number of documents: " + stats.getDocumentCount());
+System.out.println("Storage consumed by index: " + stats.getStorageSize() + " bytes");
+System.out.println("Storage consumed by vectors: " + stats.getVectorIndexSize() + " bytes");
+```
+
+### [JavaScript](#tab/javascript)
+
+The Azure SDK for JavaScript provides `getIndexStatistics` in the [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient) class for this task.
+
+```javascript
+// Create a SearchIndexClient
+const endpoint = "[service endpoint]";
+const adminKey = "[admin key]";
+const client = new SearchIndexClient(endpoint, new AzureKeyCredential(adminKey)
+);
+
+// Get index statistics
+(async () => {
+    const stats = await client.getIndexStatistics("[index name]");
+    console.log(`Number of documents: ${stats.documentCount}`);
+    console.log(`Storage consumed by index: ${stats.storageSize} bytes`);
+    console.log(`Storage consumed by vectors: ${stats.vectorIndexSize} bytes`);
+})();
+```
+
+### [Python](#tab/python)
+
+The Azure SDK for Python provides [get_index_statistics](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient) for this task.
+
+```python
+# Create a SearchIndexClient
+endpoint = "[service endpoint]"
+admin_key = AzureKeyCredential("[admin key]")
+client = SearchIndexClient(endpoint=endpoint, credential=admin_key)
+
+# Get index statistics
+stats = client.get_index_statistics("[index name]")
+print(f"Number of documents: {stats['document_count']}")
+print(f"Storage consumed by index: {stats['storage_size']} bytes")
+print(f"Storage consumed by vectors: {stats['vector_index_size']} bytes")
+```
+
+---
+
+::: zone-end
+
+## View an index's definition
+
+Each index is defined by fields and optional components that enhance search capabilities, such as analyzers, normalizers, tokenizers, and synonym maps. This definition determines the index's structure and behavior during indexing and querying.
+
+::: zone pivot="azure-portal"
+
+On the index page, select **Edit JSON** to view its complete definition.
+
+:::image type="content" source="media/search-how-to-manage-index/edit-json-button.png" alt-text="Screenshot of the Edit JSON button in the portal." border="true" lightbox="media/search-how-to-manage-index/edit-json-button.png":::
+
+<!--
+> [!NOTE]
+> The portal doesn't support synonym map definitions. You can use the portal to view existing synonyms, but you can't create them or assign them to fields. For more information, see [Add synonyms in Azure AI Search](search-synonyms.md).
+-->
+
+::: zone-end
+
+::: zone pivot="rest"
+
+Use [Indexes - Get (REST API)](/rest/api/searchservice/indexes/get) to retrieve the JSON definition of an index.
+
+```http
+### Get index definition
+GET https://[service name].search.windows.net/indexes/[index name]?api-version=[api version]
+    Content-Type: application/json
+    api-key: [admin key]
+```
+
+::: zone-end
+
+::: zone pivot="azure-sdks"
+
+Use your preferred Azure SDK to retrieve the JSON definition of an index.
+
+### [.NET](#tab/dotnet)
+
+The Azure SDK for .NET provides [GetIndexAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.getindexasync) for this task.
+
+```csharp
+// Create a SearchIndexClient
+var endpoint = new Uri("[service endpoint]");
+var credential = new AzureKeyCredential("[admin key]");
+var indexClient = new SearchIndexClient(endpoint, credential);
+
+// Get index definition
+var index = await indexClient.GetIndexAsync("[index name]");
+string indexJson = JsonSerializer.Serialize(index.Value, new JsonSerializerOptions { WriteIndented = true });
+Console.WriteLine(indexJson);
+```
+
+### [Java](#tab/java)
+
+The Azure SDK for Java provides `getIndex` in the [SearchIndexAsyncClient](/java/api/com.azure.search.documents.indexes.searchindexasyncclient) class for this task.
+
+```java
+// Create a SearchIndexAsyncClient
+String endpoint = "[service endpoint]";
+String adminKey = "[admin key]";
+SearchIndexAsyncClient searchIndexAsyncClient = new SearchIndexClientBuilder()
+    .endpoint(endpoint)
+    .credential(new AzureKeyCredential(adminKey))
+    .buildAsyncClient();
+
+// Get index definition
+searchIndexAsyncClient.getIndex("[index name]")
+    .subscribe(index -> {
+        try {
+            String prettyJson = new ObjectMapper()
+                .writerWithDefaultPrettyPrinter()
+                .writeValueAsString(index);
+            System.out.println(prettyJson);
+        } catch (Exception e) {
+            e.printStackTrace();
+        }
+    });
+```
+
+### [JavaScript](#tab/javascript)
+
+The Azure SDK for JavaScript provides `getIndex` in the [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient) class for this task.
+
+```javascript
+// Create a SearchIndexClient
+const endpoint = "[service endpoint]";
+const adminKey = "[admin key]";
+const client = new SearchIndexClient(endpoint, new AzureKeyCredential(adminKey)
+);
+
+// Get index definition
+(async () => {
+    const index = await client.getIndex("[index name]");
+    console.log(JSON.stringify(index, null, 2));
+})();
+```
+
+### [Python](#tab/python)
+
+The Azure SDK for Python provides `get_index` in the [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient) class for this task.
+
+```python
+# Create a SearchIndexClient
+endpoint = "[service endpoint]"
+admin_key = AzureKeyCredential("[admin key]")
+client = SearchIndexClient(endpoint=endpoint, credential=admin_key)
+
+# Get index definition
+index = client.get_index("[index name]")
+print(json.dumps(index.as_dict(), indent=2, sort_keys=True, ensure_ascii=False))
+```
+
+---
+
+::: zone-end
+
+## Delete an index
+
+> [!WARNING]
+> You can't undo an index deletion. Before you proceed, make sure that you want to permanently remove the index and its documents from your search service.
+
+::: zone pivot="azure-portal"
+
+On the index page, select **Delete** to initiate the deletion process.
+
+:::image type="content" source="media/search-how-to-manage-index/delete-button.png" alt-text="Screenshot of the Delete button in the portal." border="true" lightbox="media/search-how-to-manage-index/delete-button.png":::
+
+The portal prompts you to confirm the deletion. After you select **Delete**, check your notifications to confirm that the deletion was successful.
+
+:::image type="content" source="media/search-how-to-manage-index/delete-confirmation.png" alt-text="Screenshot of the deletion confirmation in the portal." border="true" lightbox="media/search-how-to-manage-index/delete-confirmation.png":::
+
+::: zone-end
+
+::: zone pivot="rest"
+
+Use [Indexes - Delete (REST API)](/rest/api/searchservice/indexes/delete) to permanently delete an index.
+
+```http
+### Delete an index
+DELETE https://[service name].search.windows.net/indexes/[index name]?api-version=[api version]
+    Content-Type: application/json
+    api-key: [admin key]
+```
+
+If the index was deleted successfully, you should receive an `HTTP/1.1 204 No Content` response.
+
+::: zone-end
+
+::: zone pivot="azure-sdks"
+
+Use your preferred Azure SDK to permanently delete an index.
+
+### [.NET](#tab/dotnet)
+
+The Azure SDK for .NET provides [DeleteIndexAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.deleteindexasync) for this task.
+
+```csharp
+// Create a SearchIndexClient
+var endpoint = new Uri("[service endpoint]");
+var credential = new AzureKeyCredential("[admin key]");
+var indexClient = new SearchIndexClient(endpoint, credential);
+
+// Delete the index
+await indexClient.DeleteIndexAsync("[index name]");
+Console.WriteLine("Index deleted successfully.");
+```
+
+### [Java](#tab/java)
+
+The Azure SDK for Java provides `deleteIndex` in the [SearchIndexAsyncClient](/java/api/com.azure.search.documents.indexes.searchindexasyncclient) class for this task.
+
+```java
+// Create a SearchIndexAsyncClient
+String endpoint = "[service endpoint]";
+String adminKey = "[admin key]";
+SearchIndexAsyncClient searchIndexAsyncClient = new SearchIndexClientBuilder()
+    .endpoint(endpoint)
+    .credential(new AzureKeyCredential(adminKey))
+    .buildAsyncClient();
+
+// Delete the index
+searchIndexAsyncClient.deleteIndex("[index name]")
+    .subscribe(
+        unused -> System.out.println("Index deleted successfully.")
+    );
+```
+
+### [JavaScript](#tab/javascript)
+
+The Azure SDK for JavaScript provides `deleteIndex` in the [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient) class for this task.
+
+```javascript
+// Create a SearchIndexClient
+const endpoint = "[service endpoint]";
+const adminKey = "[admin key]";
+const client = new SearchIndexClient(endpoint, new AzureKeyCredential(adminKey)
+);
+
+// Delete the index
+(async () => {
+    await client.deleteIndex("[index name]");
+    console.log("Index deleted successfully.");
+})();
+```
+
+### [Python](#tab/python)
+
+The Azure SDK for Python provides `delete_index` in the [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient) class for this task.
+
+```python
+# Create a SearchIndexClient
+endpoint = "[service endpoint]"
+admin_key = AzureKeyCredential("[admin key]")
+client = SearchIndexClient(endpoint=endpoint, credential=admin_key)
+
+# Delete the index
+client.delete_index("[index name]")
+print("Index deleted successfully.")
+```
+
+---
+
 ::: zone-end
 
 ## Related content
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス管理に関するドキュメントの拡充"
}
```

### Explanation
この修正は、Azure AI Searchにおけるインデックス管理の方法に関するドキュメントを大幅に改訂し、情報を追加したことを示しています。463行の新しい情報が追加され、4行が削除され、合計で467行の変更が行われました。

主な変更点には、新たにAzureポータル、REST API、Azure SDKを使用したインデックスの統計や定義の取得方法が詳細に説明されていることが含まれます。具体的には、各プラットフォームによる操作手順が追加され、ユーザーがインデックスを作成した後にどのように管理できるかが明確に示されています。また、インデックス管理における制限事項やインデックスの統計情報、定義の取得方法、削除方法に関する具体的なコードサンプルも追加されています。

これにより、ユーザーはAzure AI Searchでのインデックス管理について、より包括的かつ詳細な情報を得ることができるようになりました。ドキュメントの更新により、操作に関しての理解が深まり、実装の手順がスムーズになることが期待されます。更新日も2026年に変更されています。

## articles/search/search-import-data-portal.md{#item-b804d1}

<details>
<summary>Diff</summary>
````diff
@@ -137,7 +137,7 @@ Network protections affect the portal-to-endpoint connection and also the endpoi
 
 Portal connections to a network-protected endpoint are made using your client IP address.
 
-+ For a firewall-protected search service, [add your client IP address to an inbound rule](service-configure-firewall.md#configure-network-access-and-firewall-rules-for-azure-ai-search).
++ For a firewall-protected search service, [add your client IP address to an inbound rule](service-configure-firewall.md#configure-network-access).
 
 + For a search service configured for a [private endpoint](service-create-private-endpoint.md), use a browser on an allow-listed virtual machine to open portal pages and run the wizard.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイアウォールに関するリンクの修正"
}
```

### Explanation
この修正は、Azureの検索サービスにおけるデータインポート手順に関するドキュメントの一部を微修正したことを示しています。具体的には、ファイアウォールで保護された検索サービスのクライアントIPアドレスをインバウンドルールに追加する方法に関するリンクが更新されています。

変更前は「ネットワークアクセスとファイアウォールルールを構成する」という表現が含まれていましたが、変更後は「ネットワークアクセス」に簡素化され、より直接的で明確な指示に変更されています。この微修正により、ユーザーが適切な設定を行うための情報がわかりやすくなり、インポートプロセスをスムーズに進めることが期待されます。

また、修正に伴い、他の文脈に関する情報、特にプライベートエンドポイントを使用する場合の指示も引き続き維持されており、全体としての一貫性が保たれています。

## articles/search/service-configure-firewall.md{#item-75be3f}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +1,9 @@
 ---
 title: Configure Network Access
-description: Configure IP control policies to restrict network access to your Azure AI Search service to specific IP addresses.
+description: Restrict inbound network access to Azure AI Search with IP firewall rules and trusted service exceptions.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/13/2026
+ms.date: 04/15/2026
 ms.custom:
   - ignite-2023
   - sfi-image-nochange
@@ -13,127 +13,109 @@ ai-usage: ai-assisted
 
 # Configure network access and firewall rules for Azure AI Search
 
-This article explains how to restrict network access to a search service's public endpoint. You can configure IP firewall rules to allow only specific IP addresses, ranges, or subnets, and optionally enable exceptions for trusted Azure services.
+This article explains how to restrict *inbound* network access to a search service's public endpoint. You can configure IP firewall rules to allow access only from specific IP addresses, address ranges, or subnets. You can also enable exceptions for trusted Azure services.
 
-To block *all* data plane access to the public endpoint, use [private endpoints](service-create-private-endpoint.md) instead.
+Firewall rules control which clients can send requests (queries, indexing, management operations) to your search service. They don't affect *outbound* connections from the search service to external resources. For outbound security, see [Indexer access to content protected by Azure network security](search-indexer-securing-resources.md).
+
+> [!TIP]
+> To block *all* data plane access to the public endpoint, use a [private endpoint](service-create-private-endpoint.md) or [network security perimeter](search-security-network-security-perimeter.md) instead.
 
 ## Prerequisites
 
 + An [Azure AI Search service](search-create-service-portal.md) (Basic tier or higher). Firewall configuration isn't supported on the Free tier.
 
 + **Owner** or **Contributor** permissions on the search service.
 
-+ You can also use the [Management REST API](/rest/api/searchmanagement/), [Azure PowerShell](/powershell/module/az.search), or the [Azure CLI](/cli/azure/search) instead of the Azure portal.
+## Limitations and considerations
+
++ Some workflows require access to a public endpoint. Specifically, the [**Import data** wizard](search-import-data-portal.md) in the Azure portal connects to built-in (hosted) sample data and embedding models over a public endpoint. For more information, see [Secure connections in the import wizard](search-import-data-portal.md#secure-connections).
+
++ Network rules are scoped to data plane operations against the search service's public endpoint, which include creating indexes, querying indexes, and all other actions described in the [Search Service REST APIs](/rest/api/searchservice/).
+
++ For control plane operations that target service administration, see the [network protections supported by Azure Resource Manager](/security/benchmark/azure/baselines/azure-resource-manager-security-baseline).
+
++ If you're in early stages of proof-of-concept testing with sample data, consider deferring network access controls until you need them.
+
+## Configure network access
 
-## Configure network access in the Azure portal
+This section explains how to configure network access for your search service in the Azure portal. Alternatively, you can use the [Search Management REST API](/rest/api/searchmanagement/), [Azure PowerShell](/powershell/module/az.search), or [Azure CLI](/cli/azure/search).
+
+To configure network access:
 
 1. Go to your search service in the [Azure portal](https://portal.azure.com).
 
-1. Under **Settings**, select **Networking** on the leftmost pane. If you don't see this option, check your service tier. Networking options are available on the Basic tier and higher.
+1. From the left pane, select **Settings** > **Networking**.
 
-1. Choose **Selected IP addresses**. Avoid the **Disabled** option unless you're configuring a [private endpoint](service-create-private-endpoint.md).
+1. For **Public network access**, select **Selected IP addresses**. Select **Disabled** only if you're configuring a [private endpoint](service-create-private-endpoint.md).
 
    :::image type="content" source="media/service-configure-firewall/azure-portal-firewall.png" alt-text="Screenshot showing the network access options in the Azure portal." lightbox="media/service-configure-firewall/azure-portal-firewall.png" :::
 
-1. Under **IP Firewall**, select **Add your client IP address**. This step creates an inbound rule for the public IP address of your personal device to Azure AI Search.
+1. Under **IP Firewall**, select **Add your client IP address**.
+
+   This step creates an inbound rule that allows your device's public IP address to reach the search service.
 
    :::image type="content" source="media/service-configure-firewall/azure-portal-firewall-all.png" alt-text="Screenshot showing how to configure the IP firewall in the Azure portal." lightbox="media/service-configure-firewall/azure-portal-firewall-all.png":::
 
    > [!TIP]
    > The portal uses your client IP address for a direct connection. If your client is in the allowed IP list, you can use all portal capabilities with no extra configuration.
 
-1. Add other client IP addresses for other devices and services that send requests to a search service.
-
-   Specify IP addresses and ranges in the CIDR format. An example of CIDR notation is 8.8.8.0/24, which represents the IPs that range from 8.8.8.0 to 8.8.8.255.
+1. Add client IP addresses for other devices or services that send requests to the search service. Use the CIDR format. For example, 8.8.8.0/24 represents IP addresses ranging from 8.8.8.0 to 8.8.8.255.
 
    To get the public IP addresses of Azure services, see [Azure IP Ranges and Service Tags](https://www.microsoft.com/download/details.aspx?id=56519). If your search client is hosted within an Azure function, see [IP addresses in Azure Functions](/azure/azure-functions/ip-addresses).
 
-1. Under **Exceptions**, select **Allow Azure services on the trusted services list to access this search service**. 
+1. (Optional) Under **Exceptions**, select **Allow Azure services on the trusted services list to access this search service**.
  
-   :::image type="content" source="media/service-configure-firewall/exceptions.png" alt-text="Screenshot showing the exceptions checkbox on the network configuration page." lightbox="media/service-configure-firewall/exceptions.png":::
-
-   The trusted service list includes:
-
-   + `Microsoft.CognitiveServices` for Azure OpenAI and Foundry Tools
-   + `Microsoft.MachineLearningServices` for Azure Machine Learning
-
-   When you enable this exception, you take a dependency on Microsoft Entra ID authentication, managed identities, and role assignments. Any Foundry Tool or AML feature that has a valid role assignment on your search service can bypass the firewall. See [Grant access to trusted services](#grant-access-to-trusted-azure-services) for more details.
+   This exception allows trusted Azure services with a valid managed identity and role assignment to bypass the firewall. For more information, see [Grant access to trusted Azure services](#grant-access-to-trusted-azure-services).
 
-1. **Save** your changes.
+   :::image type="content" source="media/service-configure-firewall/exceptions.png" alt-text="Screenshot showing the exceptions checkbox on the network configuration page." lightbox="media/service-configure-firewall/exceptions.png":::
 
-After you enable the IP access control policy for your Azure AI Search service, all requests to the data plane from machines outside the allowed list of IP address ranges are rejected.
+1. Save your changes.
 
-When requests originate from IP addresses that aren't in the allowed list, a generic **403 Forbidden** response is returned with no other details.
+It can take several minutes for changes to take effect. Wait at least 15 minutes before you troubleshoot problems related to network configuration.
 
-> [!IMPORTANT]
-> It can take several minutes for changes to take effect. Wait at least 15 minutes before troubleshooting any problems related to network configuration.
+After you enable the IP access control policy, requests from IP addresses outside the allowed list are rejected with a **403 Forbidden** response.
 
 ## Grant access to trusted Azure services
 
-Did you select the trusted services exception? If yes, your search service admits requests and responses from a trusted Azure resource without checking for an IP address. A trusted resource must have a managed identity (either system or user-assigned, but usually system). A trusted resource must have a role assignment on Azure AI Search that gives it permission to data and operations. 
+If you enabled the trusted services exception, your search service accepts requests from trusted Azure resources without checking the IP address. Each trusted resource must have a managed identity (system-assigned or user-assigned, but usually system-assigned) and a role assignment on Azure AI Search that grants permissions for data and operations.
 
 The trusted service list for Azure AI Search includes:
 
-+ `Microsoft.CognitiveServices` for Azure OpenAI and Foundry Tools
-+ `Microsoft.MachineLearningServices` for Azure Machine Learning
++ `Microsoft.CognitiveServices` for Azure OpenAI and Foundry Tools.
++ `Microsoft.MachineLearningServices` for Azure Machine Learning.
 
-Workflows for this network exception are requests originating from Microsoft Foundry or other AML features to Azure AI Search. The trusted services exception is typically for [Azure OpenAI On Your Data](/azure/ai-services/openai/concepts/use-your-data) scenarios for retrieval augmented generation (RAG) and playground environments.
+This exception is commonly used when Microsoft Foundry or Azure Machine Learning sends requests to Azure AI Search, such as during agentic retrieval or integrated vectorization.
 
 ### Trusted resources must have a managed identity
 
-To set up managed identities for Azure OpenAI and Azure Machine Learning:
-
-+ [How to configure Azure OpenAI in Foundry Models with managed identities](/azure/ai-services/openai/how-to/managed-identity)
-+ [How to set up authentication between Azure Machine Learning and other services](/azure/machine-learning/how-to-identity-based-service-authentication).
+To set up a managed identity for Azure OpenAI and Azure Machine Learning, see the following articles:
 
-To set up a managed identity for a Foundry resource:
++ [Configure Azure OpenAI with Microsoft Entra ID authentication](/azure/ai-services/openai/how-to/managed-identity)
++ [Set up authentication between Azure Machine Learning and other services](/azure/machine-learning/how-to-identity-based-service-authentication)
 
-1. [Find your Foundry resource](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/microsoft.cognitiveServices%2Faccounts).
+To set up a managed identity for a Microsoft Foundry resource:
 
-1. From the left pane, select **Resource management** > **Identity**.
-
-1. Set **System assigned** to **On**.
+1. Go to your Microsoft Foundry resource in the [Azure portal](https://portal.azure.com).
+1. From the left pane, select **Resource Management** > **Identity**.
+1. Use the toggle to enable a system-assigned managed identity.
 
 ### Trusted resources must have a role assignment
 
-Once your Azure resource has a managed identity, [assign roles on Azure AI Search](search-security-rbac-client-code.md) to grant permissions to data and operations. 
-
-The trusted services are used for vectorization workloads: generating vectors from text and image content, and sending payloads back to the search service for query execution or indexing. Connections from a trusted service are used to deliver payloads to Azure AI search.
+After your Azure resource has a managed identity, [assign roles on Azure AI Search](search-security-rbac.md#assign-roles-for-development) to grant the managed identity permissions. The role you assign depends on the workload:
 
-1. Go to your search service in the [Azure portal](https://portal.azure.com).
-1. On the leftmost pane, under **Access control (IAM)**, select **Identity**.
-1. Select **Add** and then select **Add role assignment**.
-1. On the **Roles** page:
-
-   + Select **Search Index Data Contributor** to load a search index with vectors generated by an embedding model. Choose this role if you intend to use integrated vectorization during indexing.
-   + Or, select **Search Index Data Reader** to provide queries containing a vector generated by an embedding model at query time. The embedding used in a query isn't written to an index, so no write permissions are required.
++ **Search Service Contributor** for object-level operations, such as creating indexes or knowledge bases.
++ **Search Index Data Contributor** for read-write content access.
++ **Search Index Data Reader** for read-only content access.
 
-1. Select **Next**.
-1. On the **Members** page, select **Managed identity** and **Select members**.
-1. Filter by system-managed identity and then select the managed identity of your Foundry resource.
+When you assign the role, select **Managed identity** as the member type and choose the system-assigned identity of your Microsoft Foundry or Azure Machine Learning resource.
 
 > [!NOTE]
-> This article covers the trusted exception for admitting requests to your search service, but Azure AI Search is itself on the trusted services list of other Azure resources. Specifically, you can use the trusted service exception for [connections from Azure AI Search to Azure Storage](search-indexer-howto-access-trusted-service-exception.md).
+> This article covers the trusted exception for *inbound* requests to your search service. Azure AI Search is also on the trusted services list of other Azure resources. For example, you can use the trusted service exception for [indexer connections from Azure AI Search to Azure Storage](search-indexer-howto-access-trusted-service-exception.md).
 
-## Limitations and considerations
+## Next step
 
-Consider the following when configuring network access:
-
-+ Some workflows require access to a public endpoint. Specifically, the [**Import data** wizard](search-import-data-portal.md) in the Azure portal connects to built-in (hosted) sample data and embedding models over a public endpoint. For more information, see [Secure connections in the import wizard](search-import-data-portal.md#secure-connections).
-
-+ If you're in early stages of proof-of-concept testing with sample data, you might want to defer network access controls until you actually need them.
-
-+ Network rules are scoped to data plane operations against the search service's public endpoint (creating or querying indexes, and all other actions described by the [Search REST APIs](/rest/api/searchservice/)).
-
-+ For control plane operations that target service administration, refer to the [network protections supported by Azure Resource Manager](/security/benchmark/azure/baselines/azure-resource-manager-security-baseline).
-
-## Next steps
-
-Once a request is allowed through the firewall, it must be authenticated and authorized. You have two options:
+After a request is allowed through the firewall, it must be authenticated and authorized. You have two options:
 
 + [Key-based authentication](search-security-api-keys.md), where an admin or query API key is provided on the request. This option is the default.
 
-+ [Role-based access control](search-security-rbac.md) using Microsoft Entra ID, where the caller is a member of a security role on a search service. This is the most secure option. It uses Microsoft Entra ID for authentication and role assignments on Azure AI Search for permissions to data and operations.
-
-> [!div class="nextstepaction"]
-> [Enable RBAC on your search service](search-security-enable-roles.md)
++ [Role-based access control](search-security-rbac.md), where the caller is a member of a security role on a search service. This option is the most secure. It uses Microsoft Entra ID for authentication and role assignments on Azure AI Search for permissions to access data and perform operations.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイアウォール設定ドキュメントの改善"
}
```

### Explanation
この修正は、Azure AI Searchサービスのファイアウォール設定に関するドキュメントの大幅な改訂と改善を示しています。合計53行の新しい情報が追加され、71行が削除され、124行にわたる変更が行われました。

主な変更点には、ファイアウォールルールの説明がさらに具体的になり、受信側のネットワークアクセスを制限するための手順が強調されています。また、エラーメッセージやルールの効果についての情報がより明確に説明され、ユーザーがファイアウォールの設定を効率的に行えるように配慮されています。

新しく追加されたセクションでは、ネットワークアクセスを設定するためのステップバイステップのガイドラインが示され、手順が簡素化されています。また、特定のサービスの管理を実行する際の役割付与に関する指示も明確になっています。

さらに、ドキュメントは、Trusted Services Exceptionの利用方法についても具体的なガイダンスを提供しており、Microsoft Entra IDの利用による信頼性の向上にも言及されています。これにより、ユーザーはファイアウォール設定を理解し、正しく適用できるようになります。

最後に、一部の重要な注意点が強調され、ユーザーがテスト段階でネットワークアクセス制御を柔軟に管理できるようにされています。この更新により、Azure AI Searchに関連するセキュリティ設定が一層強化され、ユーザーフレンドリーなドキュメントになっています。


