---
date: '2026-04-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a69d470...MicrosoftDocs:a8bf7fb
summary: |-
  このコードの変更に関する主なハイライトは、エージェントや知識ソースに関する設定手順の軽微な更新と改善です。新しいパッケージのインストール手順やアクセス権限の管理に関する説明が具体化され、ユーザーが効率的に設定を行えるようになりました。また、REST API、C#、Pythonにおける特定の処理方法の明確化も進められています。

  新機能としては、特定のライブラリのインストールコマンドの明示化と権限管理に関するガイダンスが追加され、プロセスが簡素化されました。重大な破壊的変更はありませんが、一部の手順に影響する可能性のあるリンクやプロパティ名の変更があります。全体的な文書の日付も更新され、最新情報が反映されています。

  この変更は、知識ソースとエージェントの設定および管理の効率的な実装をサポートすることを目的としており、特に企業がAzureのサービスを利用する際に重要な役割を果たします。改善された文書は、技術者が直面する具体的な問題を迅速かつ効果的に解決する助けとなるでしょう。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a69d470...MicrosoftDocs:a8bf7fb){target="_blank"}

```diff
# Highlights
このコードの変更における主なハイライトは、複数のドキュメントにおいて軽微な更新が行われ、特にエージェントや知識ソースに関する設定手順および取り込みパラメータについて改善がなされた点です。新しいパッケージのインストール方法やアクセス権限管理についての説明が具体化され、ユーザーがより効率的に設定を行えるようになっています。また、REST API、C#、Pythonでの特定の処理方法が強調され、情報の明確化が図られました。

## New features
- REST、C#、Pythonにおける特定のライブラリのインストールコマンドが明示され、プロセスが簡素化された。
- 知識ソース取り込みパラメータの詳細説明が強化され、権限管理に関するガイダンスが追加された。

## Breaking changes
- 特に重大な破壊的変更は含まれていないが、リンクやプロパティ名の変更が一部の手順に影響する可能性あり。

## Other updates
- 全体的な文書の日付が更新され、最新情報が反映された。
- 各種知識ソース設定ドキュメント内の例やコードスニペットの改善が行われた。

# Insights
この変更においては、技術的な文書が必要な知識ソースとエージェントの設定、およびその後の管理に関する効率的な実装をサポートすることを目的としています。特に、具体的なコマンドの追加や、権限管理の方法が明確になっている点は、ユーザーが自社の環境に容易に適用できるよう配慮されています。

まず、新たに追加されたコマンドは、ユーザーがプレビュー版のライブラリを手軽に導入することを可能にし、これによりメンテナンスや新機能のテストが容易になります。また、取り込みパラメータに関連する権限管理の説明が強化されたことは、データのセキュリティ管理を確実に行うために非常に重要です。特に、ユーザーID やグループID などを用いた精細な権限付与は企業内部での利用において重要な役割を果たします。

これらの文書は、特に企業がAzureのサービスを効率的に活用するための手引として重要な役割を担い、改訂された箇所は技術的な洗練度を高めるための重要な布石となっています。ドキュメントの明確化と実用性の向上は、技術者が直面する具体的な問題を迅速かつ効果的に解決する助けとなるでしょう。
```

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | エージェントのパイプライン作成に関するドキュメントの更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-how-to-retrieve.md](#item-d739cf) | minor update | エージェントの情報取得方法に関するドキュメントの大幅な更新 | modified | 502 | 40 | 542 | 
| [agentic-knowledge-source-how-to-blob-csharp.md](#item-b5f755) | minor update | C#におけるBlob知識ソースの設定手順の更新 | modified | 4 | 1 | 5 | 
| [agentic-knowledge-source-how-to-blob-python.md](#item-029d03) | minor update | PythonにおけるBlob知識ソースの設定手順の更新 | modified | 4 | 1 | 5 | 
| [agentic-knowledge-source-how-to-blob-rest.md](#item-b5ce57) | minor update | RESTにおけるBlob知識ソースの設定手順の更新 | modified | 3 | 0 | 3 | 
| [agentic-knowledge-source-how-to-onelake-csharp.md](#item-d6611c) | minor update | C#におけるOneLake知識ソースの設定手順の更新 | modified | 5 | 2 | 7 | 
| [agentic-knowledge-source-how-to-onelake-python.md](#item-c7d61d) | minor update | PythonにおけるOneLake知識ソースの設定手順の更新 | modified | 5 | 2 | 7 | 
| [agentic-knowledge-source-how-to-onelake-rest.md](#item-876f49) | minor update | REST APIによるOneLake知識ソースの設定手順の更新 | modified | 4 | 1 | 5 | 
| [agentic-knowledge-source-how-to-search-index-csharp.md](#item-d3510c) | minor update | C#における検索インデックスの設定手順の更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-search-index-python.md](#item-58056f) | minor update | Pythonにおける検索インデックスの設定手順の更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-search-index-rest.md](#item-e95367) | minor update | REST APIを用いた検索インデックス手順の更新 | modified | 0 | 2 | 2 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-csharp.md](#item-2eb305) | minor update | C#を用いたSharePointインデックスの設定手順の更新 | modified | 5 | 2 | 7 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-python.md](#item-923abb) | minor update | Pythonを用いたSharePointインデックスの設定手順の更新 | modified | 5 | 2 | 7 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-rest.md](#item-e26ea0) | minor update | RESTを用いたSharePointインデックスの設定手順の更新 | modified | 5 | 2 | 7 | 
| [agentic-knowledge-source-how-to-sharepoint-remote-csharp.md](#item-f8bed1) | minor update | C#を用いたリモートSharePoint知識ソースの設定手順の更新 | modified | 43 | 67 | 110 | 
| [agentic-knowledge-source-how-to-sharepoint-remote-python.md](#item-822712) | minor update | Pythonを用いたリモートSharePoint知識ソースの設定手順の更新 | modified | 54 | 56 | 110 | 
| [agentic-knowledge-source-how-to-sharepoint-remote-rest.md](#item-5514b1) | minor update | REST APIを用いたリモートSharePoint知識ソースの設定手順の更新 | modified | 34 | 44 | 78 | 
| [agentic-knowledge-source-how-to-web-csharp.md](#item-401063) | minor update | .NET SDK用Azure.Search.Documentsパッケージのインストール手順の更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-web-python.md](#item-72b59c) | minor update | Python用azure-search-documentsパッケージのインストール手順の更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-how-to-create-knowledge-base-csharp.md](#item-4469a2) | minor update | C#用の知識ベース作成手順の更新 | modified | 2 | 2 | 4 | 
| [agentic-retrieval-how-to-create-knowledge-base-python.md](#item-4e498f) | minor update | Python用の知識ベース作成手順の更新 | modified | 2 | 2 | 4 | 
| [knowledge-source-ingestion-parameters-csharp.md](#item-7a6ef1) | minor update | C#用の知識ソース取り込みパラメータの更新 | modified | 6 | 5 | 11 | 
| [knowledge-source-ingestion-parameters-python.md](#item-c92d9f) | minor update | Python用の知識ソース取り込みパラメータの更新 | modified | 2 | 2 | 4 | 
| [knowledge-source-ingestion-parameters-rest.md](#item-f29dc2) | minor update | REST API用の知識ソース取り込みパラメータの更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -416,7 +416,7 @@ print(f"AI agent '{agent_name}' created or updated successfully")
 
 [!INCLUDE [foundry-iq-limitation](../foundry/includes/foundry-iq-limitation.md)]
 
-Optionally, if your knowledge base includes a [remote SharePoint knowledge source](agentic-knowledge-source-how-to-sharepoint-remote.md), you must also include the `x-ms-query-source-authorization` header in the MCP tool connection.
+Optionally, if your knowledge base includes a remote SharePoint knowledge source, you must also include the `x-ms-query-source-authorization` header in the MCP tool connection. For more information, see [Enforce permissions at query time](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
 
 ```python
 from azure.search.documents.indexes.models import RemoteSharePointKnowledgeSource, KnowledgeSourceReference
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントのパイプライン作成に関するドキュメントの更新"
}
```

### Explanation
この変更は、ドキュメント「エージェントのパイプラインを作成する方法」の内容を更新しています。具体的には、リモートSharePointの知識ソースに関するオプションの記述を修正しました。元の文から、詳細な情報を追加したことにより、ユーザーが `x-ms-query-source-authorization` ヘッダーをMCPツール接続に含める際のさらなる情報を得られるようになりました。この修正により、ユーザーが適切な権限を確認する方法についての参照リンクも追加されています。全体として、この変更は文の明確さを向上させることを目的としています。

## articles/search/agentic-retrieval-how-to-retrieve.md{#item-d739cf}

<details>
<summary>Diff</summary>
````diff
@@ -3,8 +3,9 @@ title: Query Knowledge Base via APIs or MCP
 description: Learn how to Query a knowledge base using the retrieve action or MCP endpoint in Azure AI Search using REST APIs, Azure SDKs, or any MCP-compatible client.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/13/2026
+ms.date: 03/17/2026
 ai-usage: ai-assisted
+zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Query a knowledge base using the retrieve action or MCP endpoint
@@ -13,7 +14,7 @@ ai-usage: ai-assisted
 
 In an agentic retrieval pipeline, the [retrieve action](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) invokes parallel query processing from a knowledge base. You can call the retrieve action directly using the Search Service REST APIs or an Azure SDK. Each knowledge base also exposes a Model Context Protocol (MCP) endpoint for consumption by MCP-compatible agents.
 
-This article explains how to call both retrieval methods and interpret the three-pronged response. To set up a full pipeline that connects Azure AI Search to Foundry Agent Service via MCP, see [Tutorial: Build an end-to-end agentic retrieval solution](agentic-retrieval-how-to-create-pipeline.md).
+This article explains how to call both retrieval methods with optional permissions enforcement and interpret the three-pronged response. To set up a pipeline that connects Azure AI Search to Foundry Agent Service via MCP, see [Tutorial: Build an end-to-end agentic retrieval solution](agentic-retrieval-how-to-create-pipeline.md).
 
 ## Prerequisites
 
@@ -23,50 +24,175 @@ This article explains how to call both retrieval methods and interpret the three
 
 + If the knowledge base specifies an LLM, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource.
 
-+ The [2025-11-01-preview](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) REST API or an equivalent Azure SDK preview package: [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md)
+:::zone pivot="csharp"
+
++ The latest [`Azure.Search.Documents` preview package](/dotnet/api/overview/azure/search.documents-readme?view=azure-dotnet-preview&preserve-view=true): `dotnet add package Azure.Search.Documents --prerelease`
+
+:::zone-end
+
+:::zone pivot="python"
+
++ The latest [`azure-search-documents` preview package](/python/api/overview/azure/search-documents-readme?view=azure-python-preview&preserve-view=true): `pip install --pre azure-search-documents`
+
+:::zone-end
+
+:::zone pivot="rest"
+
++ The [2025-11-01-preview](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
+
+:::zone-end
 
 ## Call the retrieve action
 
 You specify the retrieve action on a knowledge base. The input is chat conversation history in natural language, where the `messages` array contains the conversation. The agentic retrieval engine supports messages only if the [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md) is low or medium.
 
-Here's an example using [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) (REST API):
+:::zone pivot="csharp"
+
+```csharp
+using Azure.Identity;
+using Azure.Search.Documents.KnowledgeBases;
+using Azure.Search.Documents.KnowledgeBases.Models;
+
+// Create knowledge base retrieval client
+var kbClient = new KnowledgeBaseRetrievalClient(
+    endpoint: new Uri("<YOUR SEARCH SERVICE URL>"),
+    knowledgeBaseName: "<YOUR KNOWLEDGE BASE NAME>",
+    tokenCredential: new DefaultAzureCredential()
+);
+
+var retrievalRequest = new KnowledgeBaseRetrievalRequest();
+retrievalRequest.Messages.Add(
+    new KnowledgeBaseMessage(
+        content: new[] {
+            new KnowledgeBaseMessageTextContent(
+                "You can answer questions about the Earth at night. "
+                + "Sources have a JSON format with a ref_id that must be cited in the answer. "
+                + "If you do not have the answer, respond with 'I do not know'."
+            )
+        }
+    ) { Role = "assistant" }
+);
+retrievalRequest.Messages.Add(
+    new KnowledgeBaseMessage(
+        content: new[] {
+            new KnowledgeBaseMessageTextContent(
+                "Why is the Phoenix nighttime street grid so sharply visible from space, "
+                + "whereas large stretches of the interstate between midwestern cities remain comparatively dim?"
+            )
+        }
+    ) { Role = "user" }
+);
+
+var result = await kbClient.RetrieveAsync(retrievalRequest);
+Console.WriteLine(
+    (result.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text
+);
+```
+
+**Reference:** [KnowledgeBaseRetrievalClient](/dotnet/api/azure.search.documents.knowledgebases.knowledgebaseretrievalclient?view=azure-dotnet-preview&preserve-view=true), [KnowledgeBaseRetrievalRequest](/dotnet/api/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest?view=azure-dotnet-preview&preserve-view=true)
+
+:::zone-end
+
+:::zone pivot="python"
+
+```python
+from azure.identity import DefaultAzureCredential
+from azure.search.documents.knowledgebases import KnowledgeBaseRetrievalClient
+from azure.search.documents.knowledgebases.models import (
+    KnowledgeBaseMessage,
+    KnowledgeBaseMessageTextContent,
+    KnowledgeBaseRetrievalRequest,
+    SearchIndexKnowledgeSourceParams,
+)
+
+# Create knowledge base retrieval client
+kb_client = KnowledgeBaseRetrievalClient(
+    endpoint="<YOUR SEARCH SERVICE URL>",
+    knowledge_base_name="<YOUR KNOWLEDGE BASE NAME>",
+    credential=DefaultAzureCredential(),
+)
+
+request = KnowledgeBaseRetrievalRequest(
+    messages=[
+        KnowledgeBaseMessage(
+            role="assistant",
+            content=[
+                KnowledgeBaseMessageTextContent(
+                    text="You can answer questions about the Earth at night. "
+                    "Sources have a JSON format with a ref_id that must be cited in the answer. "
+                    "If you do not have the answer, respond with 'I do not know'."
+                )
+            ],
+        ),
+        KnowledgeBaseMessage(
+            role="user",
+            content=[
+                KnowledgeBaseMessageTextContent(
+                    text="Why is the Phoenix nighttime street grid so sharply visible from space, "
+                    "whereas large stretches of the interstate between midwestern cities remain comparatively dim?"
+                )
+            ],
+        ),
+    ],
+    knowledge_source_params=[
+        SearchIndexKnowledgeSourceParams(
+            knowledge_source_name="earth-at-night-blob-ks",
+        )
+    ],
+)
+
+result = kb_client.retrieve(retrieval_request=request)
+print(result.response[0].content[0].text)
+```
+
+**Reference:** [KnowledgeBaseRetrievalClient](/python/api/azure-search-documents/azure.search.documents.knowledgebases.knowledgebaseretrievalclient), [KnowledgeBaseRetrievalRequest](/python/api/azure-search-documents/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest)
+
+:::zone-end
+
+:::zone pivot="rest"
 
 ```http
-@search-url=<YOUR SEARCH SERVICE URL>
-@accessToken=<YOUR PERSONAL ID>
+@search-url = <YOUR SEARCH SERVICE URL> // Example: https://my-service.search.windows.net
+@accessToken = <YOUR ACCESS TOKEN> // Run: az account get-access-token --scope https://search.azure.com/.default --query accessToken -o tsv
 
-# Send grounding request
-POST https://{{search-url}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2025-11-01-preview
-    Content-Type: application/json
-    Authorization: Bearer {{accessToken}}
+POST {{search-url}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2025-11-01-preview
+Content-Type: application/json
+Authorization: Bearer {{accessToken}}
 
 {
-    "messages" : [
-            {
-                "role" : "assistant",
-                "content" : [
-                  { "type" : "text", "text" : "You can answer questions about the Earth at night.
-                    Sources have a JSON format with a ref_id that must be cited in the answer.
-                    If you do not have the answer, respond with 'I do not know'." }
-                ]
-            },
-            {
-                "role" : "user",
-                "content" : [
-                  { "type" : "text", "text" : "Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?" }
-                ]
-            }
-        ],
-  "knowledgeSourceParams": [
-    {
-      "filterAddOn": null,
-      "knowledgeSourceName": "earth-at-night-blob-ks",
-      "kind": "searchIndex"
-    }
-  ]
+    "messages": [
+        {
+            "role": "assistant",
+            "content": [
+                {
+                    "type": "text",
+                    "text": "You can answer questions about the Earth at night. Sources have a JSON format with a ref_id that must be cited in the answer. If you do not have the answer, respond with 'I do not know'."
+                }
+            ]
+        },
+        {
+            "role": "user",
+            "content": [
+                {
+                    "type": "text",
+                    "text": "Why is the Phoenix nighttime street grid so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?"
+                }
+            ]
+        }
+    ],
+    "knowledgeSourceParams": [
+        {
+            "knowledgeSourceName": "earth-at-night-blob-ks",
+            "kind": "searchIndex"
+        }
+    ]
 }
 ```
 
+**Reference:** [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true)
+
+:::zone-end
+
 ### Request parameters
 
 Pass the following parameters to call the retrieve action.
@@ -82,7 +208,9 @@ Pass the following parameters to call the retrieve action.
 
 For knowledge sources that target a search index, all `searchable` fields are in scope for query execution. The implied query type is `semantic`, and there's no search mode.
 
-If the index includes vector fields, you need a valid [vectorizer definition](vector-search-how-to-configure-vectorizer.md) so the agentic retrieval engine can vectorize query inputs. Otherwise, vector fields are ignored.
+If the index includes vector fields, you need a valid vectorizer definition so the agentic retrieval engine can vectorize query inputs. Otherwise, vector fields are ignored.
+
+For more information, see [Create an index for agentic retrieval](agentic-retrieval-how-to-create-index.md).
 
 ## Call the MCP endpoint
 
@@ -113,6 +241,162 @@ The MCP endpoint requires authentication via custom headers. You have two option
 >
 > + In [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp), [Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop), and similar clients, you configure headers in the MCP server JSON, such as `mcp.json`.
 
+## Enforce permissions at query time
+
+If your knowledge sources contain permission-protected content, the retrieval engine can filter results so that each user only sees the documents they're authorized to access. You enable this filtering by passing the end user's identity on the retrieve request. Without the identity token, results from permission-enabled knowledge sources are returned unfiltered.
+
+Permissions enforcement has two parts:
+
+- [**Ingestion time**](#ingestion-time-configuration): For indexed knowledge sources only, set `ingestionPermissionOptions` to ingest permission metadata alongside content.
+
+- [**Query time**](#query-time-authorization): Pass the user's access token in the `x-ms-query-source-authorization` header.
+
+### Ingestion-time configuration
+
+The following table shows which knowledge sources require ingestion-time configuration and how each source enforces permissions.
+
+| Knowledge source | Requires `ingestionPermissionOptions` | How permissions are enforced |
+|---|---|---|
+| [Blob or ADLS Gen2](agentic-knowledge-source-how-to-blob.md#ingestionparameters-properties) | ✅ | Ingested RBAC scopes or ACLs matched against user identity. |
+| [OneLake](agentic-knowledge-source-how-to-onelake.md#ingestionparameters-properties) | ✅ | Ingested RBAC scopes or ACLs matched against user identity. |
+| [Indexed SharePoint](agentic-knowledge-source-how-to-sharepoint-indexed.md#ingestionparameters-properties) | ✅ | Ingested SharePoint ACLs matched against user identity. |
+| [Remote SharePoint](agentic-knowledge-source-how-to-sharepoint-remote.md#assign-to-a-knowledge-base) | ❌ | Copilot Retrieval API queries SharePoint directly using the user's token. |
+
+> [!IMPORTANT]
+> If `ingestionPermissionOptions` wasn't configured when the indexed knowledge source was created, no permission metadata exists in the index. Results are returned unfiltered, regardless of the header. To fix this, update or recreate the knowledge source with the appropriate `ingestionPermissionOptions` values and [reindex](search-howto-run-reset-indexers.md).
+
+### Query-time authorization
+
+To pass the end user's identity, include an access token scoped to `https://search.azure.com/.default` on the retrieve request. This token is separate from the service credential used to access the search service. It doesn't need search service permissions and only represents the user whose content access is evaluated. For more information, see [Query-time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md).
+
+:::zone pivot="csharp"
+
+In the .NET SDK, pass the token as the `xMsQuerySourceAuthorization` parameter on `RetrieveAsync`:
+
+```csharp
+using Azure;
+using Azure.Identity;
+using Azure.Search.Documents.KnowledgeBases;
+using Azure.Search.Documents.KnowledgeBases.Models;
+
+// Service credential: Authenticates to the search service
+var serviceCredential = new DefaultAzureCredential();
+
+// User identity token: Represents the end user for document-level permissions filtering
+var userTokenContext = new Azure.Core.TokenRequestContext(
+    new[] { "https://search.azure.com/.default" }
+);
+string userToken = (await serviceCredential.GetTokenAsync(userTokenContext)).Token;
+
+// Create the retrieval client with the service credential
+var kbClient = new KnowledgeBaseRetrievalClient(
+    endpoint: new Uri("<YOUR SEARCH SERVICE URL>"),
+    knowledgeBaseName: "<YOUR KNOWLEDGE BASE NAME>",
+    tokenCredential: serviceCredential
+);
+
+var request = new KnowledgeBaseRetrievalRequest();
+request.Messages.Add(
+    new KnowledgeBaseMessage(
+        content: new[] {
+            new KnowledgeBaseMessageTextContent(
+                "What companies are in the financial sector?")
+        }
+    ) { Role = "user" }
+);
+
+// Pass the user identity token for permissions filtering
+var result = await kbClient.RetrieveAsync(
+    request, xMsQuerySourceAuthorization: userToken);
+
+var text = (result.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text;
+Console.WriteLine(text);
+```
+
+**Reference:** [KnowledgeBaseRetrievalClient](/dotnet/api/azure.search.documents.knowledgebases.knowledgebaseretrievalclient?view=azure-dotnet-preview&preserve-view=true), [KnowledgeBaseRetrievalRequest](/dotnet/api/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest?view=azure-dotnet-preview&preserve-view=true)
+
+:::zone-end
+
+:::zone pivot="python"
+
+In the Python SDK, pass the token as the `x_ms_query_source_authorization` parameter on `retrieve`:
+
+```python
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+from azure.search.documents.knowledgebases import KnowledgeBaseRetrievalClient
+from azure.search.documents.knowledgebases.models import (
+    KnowledgeBaseMessage, KnowledgeBaseMessageTextContent,
+    KnowledgeBaseRetrievalRequest,
+)
+
+# Service credential: Authenticates to the search service
+service_credential = DefaultAzureCredential()
+
+# User identity token: Represents the end user for document-level permissions filtering
+user_token_provider = get_bearer_token_provider(
+    service_credential, "https://search.azure.com/.default")
+user_token = user_token_provider()
+
+# Create the retrieval client with the service credential
+kb_client = KnowledgeBaseRetrievalClient(
+    endpoint="<YOUR SEARCH SERVICE URL>",
+    knowledge_base_name="<YOUR KNOWLEDGE BASE NAME>",
+    credential=service_credential,
+)
+
+request = KnowledgeBaseRetrievalRequest(
+    messages=[
+        KnowledgeBaseMessage(
+            role="user",
+            content=[KnowledgeBaseMessageTextContent(
+                text="What companies are in the financial sector?")],
+        )
+    ]
+)
+
+# Pass the user identity token for permissions filtering
+result = kb_client.retrieve(
+    retrieval_request=request, x_ms_query_source_authorization=user_token)
+print(result.response[0].content[0].text)
+```
+
+**Reference:** [KnowledgeBaseRetrievalClient](/python/api/azure-search-documents/azure.search.documents.knowledgebases.knowledgebaseretrievalclient), [KnowledgeBaseRetrievalRequest](/python/api/azure-search-documents/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest)
+
+:::zone-end
+
+:::zone pivot="rest"
+
+In the REST API, include the `x-ms-query-source-authorization` header with the user's access token:
+
+```http
+@search-url = <YOUR SEARCH SERVICE URL>
+@accessToken = <YOUR ACCESS TOKEN> // Service credential
+@userAccessToken = <USER ACCESS TOKEN> // User identity token
+
+POST {{search-url}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2025-11-01-preview
+Authorization: Bearer {{accessToken}}
+Content-Type: application/json
+x-ms-query-source-authorization: {{userAccessToken}}
+
+{
+    "messages": [
+        {
+            "role": "user",
+            "content": [
+                {
+                    "type": "text",
+                    "text": "What companies are in the financial sector?"
+                }
+            ]
+        }
+    ]
+}
+```
+
+**Reference:** [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true)
+
+:::zone-end
+
 ## Review the response
 
 Successful retrieval returns a `200 OK` status code. If the knowledge base fails to retrieve from one or more knowledge sources, a `206 Partial Content` status code returns. The response only includes results from sources that succeeded. Details about the partial response appear as errors in the activity array.
@@ -270,9 +554,63 @@ The following examples illustrate different ways to call the retrieve action:
 
 This example specifies [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md), so `retrievalReasoningEffort` must be "low" or "medium".
 
+:::zone pivot="csharp"
+
+```csharp
+var retrievalRequest = new KnowledgeBaseRetrievalRequest();
+retrievalRequest.Messages.Add(
+    new KnowledgeBaseMessage(
+        content: new[] {
+            new KnowledgeBaseMessageTextContent("What companies are in the financial sector?")
+        }
+    ) { Role = "user" }
+);
+retrievalRequest.RetrievalReasoningEffort = new KnowledgeRetrievalLowReasoningEffort();
+retrievalRequest.OutputMode = "answerSynthesis";
+retrievalRequest.MaxRuntimeInSeconds = 30;
+retrievalRequest.MaxOutputSize = 6000;
+
+var result = await kbClient.RetrieveAsync(retrievalRequest);
+Console.WriteLine(
+    (result.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text
+);
+```
+
+**Reference:** [KnowledgeBaseRetrievalClient](/dotnet/api/azure.search.documents.knowledgebases.knowledgebaseretrievalclient?view=azure-dotnet-preview&preserve-view=true), [KnowledgeBaseRetrievalRequest](/dotnet/api/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest?view=azure-dotnet-preview&preserve-view=true)
+
+:::zone-end
+
+:::zone pivot="python"
+
+```python
+from azure.search.documents.knowledgebases.models import KnowledgeRetrievalLowReasoningEffort
+
+request = KnowledgeBaseRetrievalRequest(
+    messages=[
+        KnowledgeBaseMessage(
+            role="user",
+            content=[KnowledgeBaseMessageTextContent(text="What companies are in the financial sector?")],
+        )
+    ],
+    retrieval_reasoning_effort=KnowledgeRetrievalLowReasoningEffort(),
+    output_mode="answerSynthesis",
+    max_runtime_in_seconds=30,
+    max_output_size=6000,
+)
+
+result = kb_client.retrieve(retrieval_request=request)
+print(result.response[0].content[0].text)
+```
+
+**Reference:** [KnowledgeBaseRetrievalClient](/python/api/azure-search-documents/azure.search.documents.knowledgebases.knowledgebaseretrievalclient), [KnowledgeBaseRetrievalRequest](/python/api/azure-search-documents/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest)
+
+:::zone-end
+
+:::zone pivot="rest"
+
 ```http
-POST {{url}}/knowledgebases/kb-override/retrieve?api-version={{api-version}}
-api-key: {{key}}
+POST {{search-url}}/knowledgebases/kb-override/retrieve?api-version={{api-version}}
+Authorization: Bearer {{accessToken}}
 Content-Type: application/json
 
 {
@@ -291,13 +629,84 @@ Content-Type: application/json
 }
 ```
 
+**Reference:** [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true)
+
+:::zone-end
+
 ### Set references for each knowledge source
 
 This example uses the default reasoning effort specified in the knowledge base. The focus of this example is specification of how much information to include in the response.
 
+:::zone pivot="csharp"
+
+```csharp
+var retrievalRequest = new KnowledgeBaseRetrievalRequest();
+retrievalRequest.Messages.Add(
+    new KnowledgeBaseMessage(
+        content: new[] {
+            new KnowledgeBaseMessageTextContent("What companies are in the financial sector?")
+        }
+    ) { Role = "user" }
+);
+retrievalRequest.IncludeActivity = true;
+// Knowledge source params are configured per source on the request
+
+var result = await kbClient.RetrieveAsync(retrievalRequest);
+Console.WriteLine(
+    (result.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text
+);
+```
+
+**Reference:** [KnowledgeBaseRetrievalClient](/dotnet/api/azure.search.documents.knowledgebases.knowledgebaseretrievalclient?view=azure-dotnet-preview&preserve-view=true), [KnowledgeBaseRetrievalRequest](/dotnet/api/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest?view=azure-dotnet-preview&preserve-view=true)
+
+:::zone-end
+
+:::zone pivot="python"
+
+```python
+from azure.search.documents.knowledgebases.models import SearchIndexKnowledgeSourceParams
+
+request = KnowledgeBaseRetrievalRequest(
+    messages=[
+        KnowledgeBaseMessage(
+            role="user",
+            content=[KnowledgeBaseMessageTextContent(text="What companies are in the financial sector?")],
+        )
+    ],
+    include_activity=True,
+    knowledge_source_params=[
+        SearchIndexKnowledgeSourceParams(
+            knowledge_source_name="demo-financials-ks",
+            include_references=True,
+            include_reference_source_data=True,
+        ),
+        SearchIndexKnowledgeSourceParams(
+            knowledge_source_name="demo-communicationservices-ks",
+            include_references=False,
+            include_reference_source_data=False,
+        ),
+        SearchIndexKnowledgeSourceParams(
+            knowledge_source_name="demo-healthcare-ks",
+            include_references=True,
+            include_reference_source_data=False,
+            always_query_source=True,
+        ),
+    ],
+)
+
+result = kb_client.retrieve(retrieval_request=request)
+print(result.response[0].content[0].text)
+```
+
+**Reference:** [KnowledgeBaseRetrievalClient](/python/api/azure-search-documents/azure.search.documents.knowledgebases.knowledgebaseretrievalclient), [SearchIndexKnowledgeSourceParams](/python/api/azure-search-documents/azure.search.documents.knowledgebases.models.searchindexknowledgesourceparams)
+
+:::zone-end
+
+:::zone pivot="rest"
+
 ```http
-POST {{url}}/knowledgebases/kb-medium-example/retrieve?api-version={{api-version}}
-api-key: {{key}}
+POST {{search-url}}/knowledgebases/kb-medium-example/retrieve?api-version={{api-version}}
+Authorization: Bearer {{accessToken}}
 Content-Type: application/json
 
 {
@@ -334,6 +743,9 @@ Content-Type: application/json
 }
 ```
 
+**Reference:** [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true)
+
+:::zone-end
 
 > [!NOTE]
 > For indexed OneLake or indexed SharePoint knowledge sources, set `includeReferenceSourceData` to `true` to include source document URLs in citations.
@@ -342,9 +754,53 @@ Content-Type: application/json
 
 In this example, there's no LLM for intelligent query planning or answer synthesis. The query string goes to the agentic retrieval engine for keyword search or hybrid search.
 
+:::zone pivot="csharp"
+
+```csharp
+var retrievalRequest = new KnowledgeBaseRetrievalRequest();
+retrievalRequest.Intents.Add(
+    new KnowledgeRetrievalSemanticIntent("what is a brokerage")
+);
+
+var result = await kbClient.RetrieveAsync(retrievalRequest);
+Console.WriteLine(
+    (result.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text
+);
+```
+
+**Reference:** [KnowledgeBaseRetrievalClient](/dotnet/api/azure.search.documents.knowledgebases.knowledgebaseretrievalclient?view=azure-dotnet-preview&preserve-view=true), [KnowledgeBaseRetrievalRequest](/dotnet/api/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest?view=azure-dotnet-preview&preserve-view=true)
+
+:::zone-end
+
+:::zone pivot="python"
+
+```python
+from azure.search.documents.knowledgebases.models import (
+    KnowledgeBaseRetrievalRequest,
+    KnowledgeRetrievalSemanticIntent,
+)
+
+request = KnowledgeBaseRetrievalRequest(
+    intents=[
+        KnowledgeRetrievalSemanticIntent(
+            search="what is a brokerage",
+        )
+    ]
+)
+
+result = kb_client.retrieve(retrieval_request=request)
+print(result.response[0].content[0].text)
+```
+
+**Reference:** [KnowledgeBaseRetrievalClient](/python/api/azure-search-documents/azure.search.documents.knowledgebases.knowledgebaseretrievalclient), [KnowledgeBaseRetrievalRequest](/python/api/azure-search-documents/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest)
+
+:::zone-end
+
+:::zone pivot="rest"
+
 ```http
-POST {{url}}/knowledgebases/kb-minimal/retrieve?api-version={{api-version}}
-api-key: {{key}}
+POST {{search-url}}/knowledgebases/kb-minimal/retrieve?api-version={{api-version}}
+Authorization: Bearer {{accessToken}}
 Content-Type: application/json
 
 {
@@ -357,8 +813,14 @@ Content-Type: application/json
 }
 ```
 
+**Reference:** [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true)
+
+:::zone-end
+
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
++ [Query-time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md)
++ [Use a blob indexer or knowledge source to ingest RBAC scopes metadata](search-blob-indexer-role-based-access.md)
 + [Agentic RAG: Build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
 + [Azure OpenAI demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントの情報取得方法に関するドキュメントの大幅な更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるエージェントの情報取得方法に関するドキュメントに大幅なアップデートを加えています。主な変更内容としては、アクセス許可の強制に関するオプションが明確に説明されたことが挙げられます。この新しい情報により、ユーザーはクエリを実行する際に、特定のユーザーにアクセスを制限する方法を理解できるようになります。

具体的には、クエリ時にユーザーのアイデンティティをパラメータとして渡すことで、許可されたコンテンツのみを取得できる仕組みが説明されています。また、文書の中で、様々なプログラミング言語（C#、Python、REST API）を用いた具体的なリクエスト例も追加されており、これによりユーザーは実践的な観点からも利用しやすくなっています。さらに、エラー処理や許可の構成方法についての詳細な情報も提供されています。この変更は、ドキュメント全体の使い勝手を向上させることを目指しています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-csharp.md{#item-b5f755}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ Unlike a [search index knowledge source](../../agentic-knowledge-source-how-to-s
 
 + A blob container with [supported content types](../../search-how-to-index-azure-blob-storage.md#supported-document-formats) for text content. For optional image verbalization, the supported content type depends on whether your chat completion model can analyze and describe the image file.
 
-+ The latest preview version of the [`Azure.Search.Documents` client library](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1) for the .NET SDK.
++ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
@@ -200,6 +200,9 @@ If you're satisfied with the knowledge source, continue to the next step: specif
 
 After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
+> [!TIP]
+> To enforce document-level permissions, set `IngestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
 ## Delete a knowledge source
 
 [!INCLUDE [Delete knowledge source using C#](knowledge-source-delete-csharp.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#におけるBlob知識ソースの設定手順の更新"
}
```

### Explanation
この変更は、C#におけるBlob知識ソースの設定方法に関するドキュメントに対する軽微な更新を提供しています。主な変更点は、`Azure.Search.Documents`クライアントライブラリの最新プレビュー版に関する記述の修正です。従来の説明から、具体的なパッケージのインストール方法が追加され、ユーザーが簡単にそのパッケージをプロジェクトに追加できるようになっています。

さらに、ドキュメントの最後に、ドキュメントレベルのアクセス制御を強制するために、知識ソースを作成する際に`IngestionPermissionOptions`を設定する必要があること、そして、リトリーブリクエストにユーザーのアクセストークンを含めることが推奨されています。これにより、セキュリティが強化され、ユーザーがアクセスできるコンテンツが適切に制限されます。この修正は、ユーザーに対するアドバイスを強化し、ドキュメントの実用性を向上させることを目的としています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-python.md{#item-029d03}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ Unlike a [search index knowledge source](../../agentic-knowledge-source-how-to-s
 
 + A blob container with [supported content types](../../search-how-to-index-azure-blob-storage.md#supported-document-formats) for text content. For optional image verbalization, the supported content type depends on whether your chat completion model can analyze and describe the image file.
 
-+ The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
++ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
@@ -185,6 +185,9 @@ If you're satisfied with the knowledge source, continue to the next step: specif
 
 After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
+> [!TIP]
+> To enforce document-level permissions, set `ingestion_permission_options` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
 ## Delete a knowledge source
 
 [!INCLUDE [Delete knowledge source using Python](knowledge-source-delete-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PythonにおけるBlob知識ソースの設定手順の更新"
}
```

### Explanation
この変更は、Pythonを使用したBlob知識ソースの設定に関するドキュメントに関する軽微な更新を行っています。主な変更点として、`azure-search-documents`クライアントライブラリの最新プレビュー版に関する説明が改訂され、パッケージのインストール方法が明示的に示されています。その結果、ユーザーは必要なパッケージを簡単にプロジェクトに追加できます。

加えて、ドキュメントの最後には、ドキュメントレベルのアクセス制御を強制する方法についての新しいヒントが追加されました。このヒントは、知識ソースを作成する際に`ingestion_permission_options`を設定し、リトリーブリクエストにユーザーのアクセストークンを含めることを勧めています。これにより、セキュリティが強化され、ユーザーが許可されたコンテンツにのみアクセスできるようになります。この変更は、全体的なドキュメントの使いやすさを向上させることを目的としています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-rest.md{#item-b5ce57}

<details>
<summary>Diff</summary>
````diff
@@ -173,6 +173,9 @@ If you're satisfied with the knowledge source, continue to the next step: specif
 
 After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
+> [!TIP]
+> To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
 ## Delete a knowledge source
 
 [!INCLUDE [Delete knowledge source using REST](knowledge-source-delete-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTにおけるBlob知識ソースの設定手順の更新"
}
```

### Explanation
この変更は、RESTを使用したBlob知識ソースの設定に関するドキュメントに対する軽微な更新を行っています。追加された内容には、知識ソースを作成する際のドキュメントレベルのアクセス制御に関するヒントが含まれています。このヒントでは、`ingestionPermissionOptions`を設定し、リトリーブリクエストにユーザーのアクセストークンを含めることが推奨されています。これにより、ユーザーはアクセスを適切に制御できるようになります。

さらに、知識ソースの削除に関するセクションも更新されています。全体として、この変更はドキュメントの実用性を向上させ、ユーザーが安全かつ効果的にBlob知識ソースを管理できるよう支援します。この改訂により、特定の機能や設定方法に関する情報が明確になり、ユーザーにとって有用なリソースとなっています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-csharp.md{#item-d6611c}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ The generated indexer conforms to the *OneLake indexer*, whose prerequisites, su
 
 + Completion of the [OneLake indexer data preparation](../../search-how-to-index-onelake-files.md#prepare-data-for-indexing).
 
-+ The latest preview version of the [`Azure.Search.Documents` client library](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1) for the .NET SDK.
++ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
@@ -185,12 +185,15 @@ We recommend using the Azure portal to validate output creation. The workflow is
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../search-agentic-retrieval-how-to-create.md).
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
 
 For any knowledge base that specifies an indexed OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
 
 After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
+> [!TIP]
+> To enforce document-level permissions, set `IngestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
 ## Delete a knowledge source
 
 [!INCLUDE [Delete knowledge source using C#](knowledge-source-delete-csharp.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#におけるOneLake知識ソースの設定手順の更新"
}
```

### Explanation
この変更は、C#を使用したOneLake知識ソースの設定に関するドキュメントの軽微な更新を行っています。主な変更点には、最新の`Azure.Search.Documents`クライアントライブラリのインストール方法が明確に記載され、ユーザーがパッケージを簡単に追加できるようになります。

また、知識ベースに知識ソースを指定するためのリンクが更新され、構成手順がより正確なものとなっています。さらに、ドキュメントレベルのアクセス制御を強化するヒントが追加され、ユーザーが`IngestionPermissionOptions`を使用して、リトリーブリクエストにユーザーのアクセストークンを含めることが重要であることを示しています。

最後に、C#を使用した知識ソースの削除に関する情報が含まれているセクションも修正されています。これらの変更により、ユーザーはOneLake知識ソースを管理するための最新かつ明確な情報を得ることができます。全体として、この更新はドキュメントの使いやすさを向上させ、より良い体験を提供します。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-python.md{#item-c7d61d}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ The generated indexer conforms to the *OneLake indexer*, whose prerequisites, su
 
 + Completion of the [OneLake indexer data preparation](../../search-how-to-index-onelake-files.md#prepare-data-for-indexing).
 
-+ The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
++ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
@@ -174,12 +174,15 @@ We recommend using the Azure portal to validate output creation. The workflow is
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../search-agentic-retrieval-how-to-create.md).
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
 
 For any knowledge base that specifies an indexed OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
 
 After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
+> [!TIP]
+> To enforce document-level permissions, set `ingestion_permission_options` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
 ## Delete a knowledge source
 
 [!INCLUDE [Delete knowledge source using Python](knowledge-source-delete-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PythonにおけるOneLake知識ソースの設定手順の更新"
}
```

### Explanation
この変更は、Pythonを使用したOneLake知識ソースの設定に関するドキュメントの軽微な更新が行われています。主な変更には、最新の`azure-search-documents`クライアントライブラリのインストール手順が明確に記載され、ユーザーはパッケージを簡単に追加できるようになります。この更新により、具体的なインストールコマンドが提供され、ユーザーがよりスムーズにセットアップできるよう配慮されています。

また、知識ベースに知識ソースを指定するためのリンクが修正され、手順の正確さが向上しています。さらに、ドキュメントレベルのアクセス制御を強化するために、`ingestion_permission_options`を設定し、リトリーブリクエストにユーザーのアクセストークンを含める必要性が明記されています。

最後に、Pythonを使用した知識ソースの削除に関する情報を含むセクションも更新されています。これらの変更により、ユーザーはOneLake知識ソースを管理するための最新かつ明確な情報を得ることができ、全体としてドキュメントの使いやすさが向上することに寄与しています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-rest.md{#item-876f49}

<details>
<summary>Diff</summary>
````diff
@@ -161,12 +161,15 @@ We recommend using the Azure portal to validate output creation. The workflow is
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../search-agentic-retrieval-how-to-create.md).
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
 
 For any knowledge base that specifies an indexed OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
 
 After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
+> [!TIP]
+> To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
 ## Delete a knowledge source
 
 [!INCLUDE [Delete knowledge source using REST](knowledge-source-delete-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIによるOneLake知識ソースの設定手順の更新"
}
```

### Explanation
この変更は、REST APIを通じたOneLake知識ソースの設定に関するドキュメントの軽微な更新を行っています。主な変更点には、知識ソースを知識ベースに指定する手順に関連するリンクが修正され、情報の正確性が向上しています。具体的には、知識ソースを指定する際のリンクが新しい構文に更新されています。

さらに、ドキュメントレベルのアクセス制御を強化するためのヒントが追加され、ユーザーが`ingestionPermissionOptions`を設定し、リトリーブリクエストにユーザーのアクセストークンを含めることが重要であることが明記されています。

また、REST APIを用いた知識ソースの削除に関する情報が含まれているセクションも更新され、ユーザーがOneLake知識ソースを効率的に管理できるようになっています。これらの変更により、ユーザーは最新で明確な情報を得られるようになり、全体としてドキュメントの使いやすさが向上しています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-csharp.md{#item-d3510c}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ A *search index knowledge source* specifies a connection to an Azure AI Search i
 
 + A search index containing plain text or vector content with a semantic configuration. [Review the index criteria for agentic retrieval](../../agentic-retrieval-how-to-create-index.md#criteria-for-agentic-retrieval). The index must be on the same search service as the knowledge base.
 
-+ The latest preview version of the [`Azure.Search.Documents` client library](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1) for the .NET SDK.
++ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#における検索インデックスの設定手順の更新"
}
```

### Explanation
この変更は、C#を使用した検索インデックス設定に関するドキュメントの軽微な更新です。主な修正点は、最新の`Azure.Search.Documents`クライアントライブラリのインストール手順が改善されたことです。具体的には、インストールコマンドが明確になり、ユーザーは`dotnet add package Azure.Search.Documents --prerelease`というコマンドを利用することで、簡単にプレビュー版を追加できるようになっています。

また、検索インデックスの要件に関する記述も強化されており、検索インデックスが知識ベースと同じ検索サービス上に存在する必要があることが明確化されています。これにより、ユーザーは設定手順を正確に理解することができ、全体としてドキュメントの信頼性と使いやすさが向上します。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-python.md{#item-58056f}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ A *search index knowledge source* specifies a connection to an Azure AI Search i
 
 + A search index containing plain text or vector content with a semantic configuration. [Review the index criteria for agentic retrieval](../../agentic-retrieval-how-to-create-index.md#criteria-for-agentic-retrieval). The index must be on the same search service as the knowledge base.
 
-+ The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
++ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonにおける検索インデックスの設定手順の更新"
}
```

### Explanation
この変更は、Pythonを使用した検索インデックスの設定に関するドキュメントの軽微な更新です。主な修正点は、`azure-search-documents`クライアントライブラリのインストール手順が改善されています。具体的には、インストールコマンドが明確になり、ユーザーは`pip install --pre azure-search-documents`というコマンドを利用してプレビュー版を簡単にインストールできるようになりました。

さらに、検索インデックスに関する要件の説明も強化されており、構文ありの検索インデックスが知識ベースと同じ検索サービス上に存在する必要があることが強調されています。これにより、ユーザーは設定手順をより正確に理解でき、全体としてドキュメントの信頼性と使いやすさが向上しています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-rest.md{#item-e95367}

<details>
<summary>Diff</summary>
````diff
@@ -90,8 +90,6 @@ You can pass the following properties to create a search index knowledge source.
 | `sourceDataFields` | The index fields returned when you specify `includeReferenceSourceData` in the knowledge base definition. These fields are used for citations and should be `retrievable`. Examples include the document name, file name, page numbers, or chapter numbers. | Array | Yes | No |
 | `searchFields` | The index fields to specifically search against. When unspecified, all fields are searched. | Array | Yes | No |
 
----
-
 ## Assign to a knowledge base
 
 If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIを用いた検索インデックス手順の更新"
}
```

### Explanation
この変更は、REST APIを利用した検索インデックスの設定に関するドキュメントの軽微な更新です。主な修正点として、不要なセクションヘッダーや余白の削除が行われ、ドキュメントがよりスムーズに読みやすくなっています。

具体的には、「知識ソースを知識ベースに割り当てる」というセクションが削除され、情報が簡潔に整理されています。これにより、ユーザーは手順に関する情報をより効率的に取得できるようになり、全体的なユーザーエクスペリエンスが向上します。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-csharp.md{#item-2eb305}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
   + [Step 2: Choose either delegated or application permissions](../../search-how-to-index-sharepoint-online.md#step-2-decide-which-permissions-the-indexer-requires)
   + [Step 3: Create a Microsoft Entra application registration](../../search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration) (for application permissions, you also configure a [client secret](../../search-how-to-index-sharepoint-online.md#using-client-secret) or [secretless authentication](../../search-how-to-index-sharepoint-online.md#using-secretless-authentication-to-obtain-application-tokens))
 
-+ The latest preview version of the [`Azure.Search.Documents` client library](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1) for the .NET SDK.
++ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
@@ -179,12 +179,15 @@ We recommend using the Azure portal to validate output creation. The workflow is
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../search-agentic-retrieval-how-to-create.md).
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
 
 For any knowledge base that specifies an indexed SharePoint knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
 
 After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
+> [!TIP]
+> To enforce document-level permissions, set `IngestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
 ## Delete a knowledge source
 
 [!INCLUDE [Delete knowledge source using C#](knowledge-source-delete-csharp.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#を用いたSharePointインデックスの設定手順の更新"
}
```

### Explanation
この変更は、C#を使用したSharePointインデックスの設定に関するドキュメントの軽微な更新です。主な修正点として、`Azure.Search.Documents`クライアントライブラリのインストール手順が具体化され、ユーザーは`dotnet add package Azure.Search.Documents --prerelease`コマンドを使用してプレビュー版を簡単にインストールできるようになりました。

また、知識ソースを知識ベースに割り当てる際の手順において、正確なリンク先が提供され、ユーザーが参照すべきドキュメントが明確に示されています。さらに、文書レベルの権限を強制するためのオプションに関する新しい情報が追加されており、利用者がアクセス権を管理する方法についての理解が深まっています。

全体として、これらの変更により、ドキュメントの明瞭性と使いやすさが向上し、ユーザーがより効果的に設定手順を実行できるようになっています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-python.md{#item-923abb}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
   + [Step 2: Choose either delegated or application permissions](../../search-how-to-index-sharepoint-online.md#step-2-decide-which-permissions-the-indexer-requires)
   + [Step 3: Create a Microsoft Entra application registration](../../search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration) (for application permissions, you also configure a [client secret](../../search-how-to-index-sharepoint-online.md#using-client-secret) or [secretless authentication](../../search-how-to-index-sharepoint-online.md#using-secretless-authentication-to-obtain-application-tokens))
 
-+ The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
++ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
@@ -168,12 +168,15 @@ We recommend using the Azure portal to validate output creation. The workflow is
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../search-agentic-retrieval-how-to-create.md).
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
 
 For any knowledge base that specifies an indexed SharePoint knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
 
 After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
+> [!TIP]
+> To enforce document-level permissions, set `ingestion_permission_options` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
 ## Delete a knowledge source
 
 [!INCLUDE [Delete knowledge source using Python](knowledge-source-delete-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonを用いたSharePointインデックスの設定手順の更新"
}
```

### Explanation
この変更は、Pythonを使用したSharePointインデックスの設定に関するドキュメントの軽微な更新です。主な修正点は、`azure-search-documents`クライアントライブラリのインストール手順が具体的に示され、ユーザーは`pip install --pre azure-search-documents`コマンドを使用してプレビュー版を簡単に導入できるようになった点です。

さらに、知識ソースを知識ベースに割り当てる際の手順において、正確なリンクが更新され、ユーザーが参照すべき正しいドキュメントが明記されています。また、文書レベルの権限を強制するための新しいオプションに関する情報も追加されており、ユーザーがアクセス権を管理する方法についての理解が深まります。

これらの更新により、全体としてドキュメントの明確さと実用性が向上し、ユーザーは手順をより効率的に進めることができるようになっています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-rest.md{#item-e26ea0}

<details>
<summary>Diff</summary>
````diff
@@ -138,7 +138,7 @@ You can pass the following properties to create an indexed SharePoint knowledge
 | `encryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
 | `indexedSharePointParameters` | Parameters specific to indexed SharePoint knowledge sources: `connectionString`, `containerName`, and `query`. | Object | No | Yes |
 | `connectionString` | The connection string to a SharePoint site. For more information, see [Connection string syntax](../../search-how-to-index-sharepoint-online.md#connection-string-format). | String | Yes |No |
-| `container_name` | The SharePoint library to access. Use `defaultSiteLibrary` to index content from the site's default document library or `allSiteLibraries` to index content from every document library in the site. Ignore `useQuery` for now. | String | No | Yes |
+| `containerName` | The SharePoint library to access. Use `defaultSiteLibrary` to index content from the site's default document library or `allSiteLibraries` to index content from every document library in the site. Ignore `useQuery` for now. | String | No | Yes |
 | `query` | Optional [query](../../search-how-to-index-sharepoint-online.md#query) to filter SharePoint content. | String | Yes | No |
 
 ### `ingestionParameters` properties
@@ -164,12 +164,15 @@ We recommend using the Azure portal to validate output creation. The workflow is
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../search-agentic-retrieval-how-to-create.md).
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
 
 For any knowledge base that specifies an indexed SharePoint knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
 
 After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
+> [!TIP]
+> To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
 ## Delete a knowledge source
 
 [!INCLUDE [Delete knowledge source using REST](knowledge-source-delete-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTを用いたSharePointインデックスの設定手順の更新"
}
```

### Explanation
この変更は、RESTを使用したSharePointインデックスの設定に関するドキュメントの軽微な更新です。主な修正箇所として、`container_name`というプロパティ名が`containerName`に変更され、より一貫性のある命名規則が適用されました。この変更により、ユーザーは設定時により分かりやすいプロパティ名を使用することができます。

また、知識ソースを知識ベースに割り当てる際の手順において、正確なリンクが更新され、ユーザーが参照すべきドキュメントが明確に示されています。さらに、文書レベルの権限を強制するための新しいオプションに関する情報が追加され、アクセス権の管理方法についての理解が深まります。

これらの更新により、全体としてドキュメントの明瞭性が向上し、ユーザーが設定手順をより効率的に実行できるようになっています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-csharp.md{#item-f8bed1}

<details>
<summary>Diff</summary>
````diff
@@ -6,15 +6,9 @@ ms.date: 03/25/2026
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
 
-A *remote SharePoint knowledge source* uses the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) to query textual content directly from SharePoint in Microsoft 365, returning results to the agentic retrieval engine for merging, ranking, and response formulation. There's no search index used by this knowledge source, and only textual content is queried.
+A *remote SharePoint knowledge source* uses the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) to query textual content directly from SharePoint in Microsoft 365. No search index or connection string is needed. Only textual content is queried, and usage is billed through Microsoft 365 and a Copilot license.
 
-At query time, the remote SharePoint knowledge source calls the Copilot Retrieval API on behalf of the user identity, so no connection strings are needed in the knowledge source definition. All content to which a user has access is in-scope for knowledge retrieval. To limit sites or constrain search, set a [filter expression](/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference). Your Azure tenant and the Microsoft 365 tenant must use the same Microsoft Entra ID tenant, and the caller's identity must be recognized by both tenants.
-
-+ You can use filters to scope search by URLs, date ranges, file types, and other metadata.
-
-+ SharePoint permissions and Purview labels are honored in requests for content.
-
-+ Usage is billed through Microsoft 365 and a Copilot license.
+To limit sites or constrain search, set a [filter expression](#filter-expression-examples) to scope by URLs, date ranges, file types, and other metadata. The caller's identity must be recognized by both the Azure tenant and the Microsoft 365 tenant because the retrieval engine queries SharePoint on behalf of the user.
 
 Like any other knowledge source, you specify a remote SharePoint knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md) and use the results as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
 
@@ -30,14 +24,12 @@ Like any other knowledge source, you specify a remote SharePoint knowledge sourc
 
 + SharePoint in a Microsoft 365 tenant that's under the same Microsoft Entra ID tenant as Azure.
 
-+ A personal access token for local development or a user's identity from a client application.
++ A Microsoft 365 Copilot license for query-time access to SharePoint content.
 
-+ The latest preview version of the [`Azure.Search.Documents` client library](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1) for the .NET SDK.
++ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible.
 
-For local development, the agentic retrieval engine uses your access token to call SharePoint on your behalf. For more information about using a personal access token on requests, see [Connect to Azure AI Search](../../search-get-started-rbac.md).
-
 ## Limitations
 
 The following limitations in the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) apply to remote SharePoint knowledge sources.
@@ -85,11 +77,6 @@ The following JSON is an example response for a remote SharePoint knowledge sour
 
 Run the following code to create a remote SharePoint knowledge source.
 
-[API keys](../../search-security-api-keys.md) are used for your client connection to Azure AI Search and Azure OpenAI. Your access token is used by Azure AI Search to connect to SharePoint in Microsoft 365 on your behalf. You can only retrieve content that you're permitted to access. For more information about getting a personal access token and other values, see [Connect to Azure AI Search](../../search-get-started-rbac.md).
-
-> [!NOTE]
-> You can also use your personal access token to access Azure AI Search and Azure OpenAI if you [set up role assignments on each resource](../../search-security-rbac.md). Using API keys allows you to omit this step in this example.
-
 ```csharp
 // Create a remote SharePoint knowledge source
 using Azure.Search.Documents.Indexes;
@@ -129,7 +116,7 @@ You can pass the following properties to create a remote SharePoint knowledge so
 
 ### Filter expression examples
 
-Not all SharePoint properties are supported in the `filterExpression`. For a list of supported properties, see the [API reference](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval). Here's some more information about queryable properties that you can use in filter: [queryable properties](/graph/connecting-external-content-manage-schema#queryable).
+Not all SharePoint properties are supported in the `filterExpression`. For a list of supported properties, see the [API reference](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval). For queryable properties, see [Queryable](/graph/connecting-external-content-manage-schema#queryable).
 
 Learn more about [KQL filters](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval?pivots=graph-v1#example-7-use-filter-expressions) in the syntax reference.
 
@@ -144,85 +131,74 @@ Learn more about [KQL filters](/microsoft-365-copilot/extensibility/api/ai-servi
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../search-agentic-retrieval-how-to-create.md).
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
 
 ## Query a knowledge base
 
-The [retrieve action](../../agentic-retrieval-how-to-retrieve.md) on the knowledge base provides the user identity that authorizes access to content in Microsoft 365.
+After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query SharePoint content. Remote SharePoint has source-specific behaviors for query-time filtering, query formulation, response fields, and permissions enforcement.
 
-Azure AI Search uses the access token to call the Copilot Retrieval API on behalf of the user identity. The access token is provided in the retrieve endpoint as a `xMsQuerySourceAuthorization` HTTP header.
+### Apply a KQL filter at query time
 
-```csharp
-using Azure;
-using Azure.Search.Documents.KnowledgeBases;
-using Azure.Search.Documents.KnowledgeBases.Models;
+You can pass a `filterExpressionAddOn` in the `knowledgeSourceParams` on the retrieve request to apply a KQL filter at query time. If you specify `filterExpressionAddOn` on the retrieve request and a `filterExpression` on the knowledge source definition, the filters are AND'd together.
 
-// Get access token
-var credential = new DefaultAzureCredential();
-var tokenRequestContext = new Azure.Core.TokenRequestContext(new[] { "https://search.azure.com/.default" });
-var accessToken = await credential.GetTokenAsync(tokenRequestContext);
-string token = accessToken.Token;
-
-// Create knowledge base retrieval client
-var baseClient = new KnowledgeBaseRetrievalClient(
-    endpoint: new Uri(searchEndpoint),
-    knowledgeBaseName: knowledgeBaseName,
-    credential: new AzureKeyCredential()
+```csharp
+var retrievalRequest = new KnowledgeBaseRetrievalRequest();
+retrievalRequest.Messages.Add(
+    new KnowledgeBaseMessage(
+        content: new[] {
+            new KnowledgeBaseMessageTextContent("contoso product planning")
+        }
+    ) { Role = "user" }
 );
-
-var spMessages = new List<Dictionary<string, string>>
-{
-    new Dictionary<string, string>
+retrievalRequest.KnowledgeSourceParams.Add(
+    new RemoteSharePointKnowledgeSourceParams("my-remote-sharepoint-ks")
     {
-        { "role", "user" },
-        { "content", @"contoso product planning" }
+        FilterExpressionAddOn = "filetype:docx"
     }
-};
-
-// Create retrieval request
-var retrievalRequest = new KnowledgeBaseRetrievalRequest();
-foreach (Dictionary<string, string> message in spMessages) {
-    if (message["role"] != "system") {
-        retrievalRequest.Messages.Add(new KnowledgeBaseMessage(content: new[] { new KnowledgeBaseMessageTextContent(message["content"]) }) { Role = message["role"] });
-    }
-}
-retrievalRequest.RetrievalReasoningEffort = new KnowledgeRetrievalLowReasoningEffort();
-var retrievalResult = await baseClient.RetrieveAsync(retrievalRequest, xMsQuerySourceAuthorization: token);
+);
 
-Console.WriteLine((retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent).Text);
+var result = await kbClient.RetrieveAsync(
+    retrievalRequest, xMsQuerySourceAuthorization: token
+);
 ```
 
-The response might look like the following:
+### Write effective queries
 
-`Contoso's product planning for the NextGen Camera includes a 2019 launch with a core package design and minor modifications for three product versions, featuring Wi-Fi enabled technology and a new mobile app for photo organization and sharing, aiming for 100,000 users within six months [ref_id:0][ref_id:1]. Research and forecasting are central to their planning, with phase two research focusing on feedback from a diverse user group to shape deliverables and milestones [ref_id:0][ref_id:1].`
+Queries that ask about the content itself are more effective than questions about where a file is located or when it was last updated. For example, "Where is the keynote doc for Ignite 2024" might return no results because the content itself doesn't disclose its location. A `filterExpression` on metadata is a better approach for file location or date-specific queries.
 
-The retrieve request also takes a [KQL filter](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval?pivots=graph-v1#example-7-use-filter-expressions) (`filterExpressionAddOn`) if you want to apply constraints at query time. If you specify `filterExpressionAddOn` on both the knowledge source and knowledge base retrieve action, the filters are AND'd together.
+A more effective question is "What is the keynote doc for Ignite 2024". The response includes the synthesized answer, query activity and token counts, plus the URL and other metadata.
 
-Queries asking questions about the content itself are more effective than questions about where a file is located or when it was last updated. For example, if you ask, "Where is the keynote doc for Ignite 2024", you might get "No relevant content was found for your query" because the content itself doesn't disclose its location. A filter on metadata is a better solution for file location or date-specific queries.
+### SharePoint-specific response fields
 
-A better question to ask is, "What is the keynote doc for Ignite 2024". The response includes the synthesized answer, query activity and token counts, plus the URL and other metadata.
+Remote SharePoint results include fields that don't appear for other knowledge source types, such as `resourceMetadata`, `webUrl`, and `searchSensitivityLabelInfo`.
 
 ```json
 {
     "resourceMetadata": {
         "Author": "Nuwan Amarathunga;Nurul Izzati",
         "Title": "Ignite 2024 Keynote Address"
-    }
-},
-"rerankerScore": 2.489522,
-"webUrl": "https://contoso-my.sharepoint.com/keynotes/nuamarth_contoso_com/Documents/Keynote-Ignite-2024.docx",
-"searchSensitivityLabelInfo": {
+    },
+    "rerankerScore": 2.489522,
+    "webUrl": "https://contoso-my.sharepoint.com/keynotes/Documents/Keynote-Ignite-2024.docx",
+    "searchSensitivityLabelInfo": {
         "displayName": "Confidential\\Contoso Extended",
         "sensitivityLabelId": "aaaaaaaa-0b0b-1c1c-2d2d-333333333333",
-        "tooltip": "Data is classified and protected. Contoso Full Time Employees (FTE) and non-employees can edit, reply, forward and print. Recipient can unprotect content with the right justification.",
+        "tooltip": "Data is classified and protected.",
         "priority": 5,
         "color": "#FF8C00",
         "isEncrypted": true
     }
+}
 ```
 
+### Enforce permissions at query time
+
+Remote SharePoint knowledge sources can enforce SharePoint permissions at query time. To enable this filtering, include the end user's access token in the retrieve request. The retrieval engine passes the token to the Copilot Retrieval API, which queries SharePoint and returns only content to which the user has access. SharePoint permissions and Microsoft Purview sensitivity labels are honored.
+
+Because remote SharePoint doesn't use a search index, no ingestion-time permissions configuration is needed. The access token is the only requirement.
+
+For instructions on passing the token, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
 ## Delete a knowledge source
 
 [!INCLUDE [Delete knowledge source using C#](knowledge-source-delete-csharp.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#を用いたリモートSharePoint知識ソースの設定手順の更新"
}
```

### Explanation
この変更は、C#を使用したリモートSharePoint知識ソースの設定に関するドキュメントの軽微な更新です。主な修正点として、リモートSharePoint知識ソースが[Copilot Retrieval API]を利用してSharePointから直接テキストコンテンツを照会する際に、検索インデックスや接続文字列が不要であることを明確にしています。また、利用料金がMicrosoft 365とCopilotライセンスを通じて請求されることも強調されています。

さらに、フィルター式を使用して検索範囲を絞る方法が改善され、リモートSharePoint知識ソースから得られる応答に特有のフィールド（`resourceMetadata`や`webUrl`など）が追加されていることが説明されています。また、クエリー時の権限の強制を行うために、エンドユーザーのアクセス・トークンを取得する方法が明記されており、SharePointの権限やMicrosoft Purviewの感度ラベルがどう作用するかについても説明が更新されています。

これらの変更により、ユーザーはC#を用いたリモートSharePoint知識ソースの設定と運用に関する情報をより直感的に理解できるようになり、具体的な使用方法に関する理解が深まります。全体として、ドキュメントの明瞭性と実用性が向上しています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-python.md{#item-822712}

<details>
<summary>Diff</summary>
````diff
@@ -6,15 +6,9 @@ ms.date: 03/25/2026
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
 
-A *remote SharePoint knowledge source* uses the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) to query textual content directly from SharePoint in Microsoft 365, returning results to the agentic retrieval engine for merging, ranking, and response formulation. There's no search index used by this knowledge source, and only textual content is queried.
+A *remote SharePoint knowledge source* uses the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) to query textual content directly from SharePoint in Microsoft 365. No search index or connection string is needed. Only textual content is queried, and usage is billed through Microsoft 365 and a Copilot license.
 
-At query time, the remote SharePoint knowledge source calls the Copilot Retrieval API on behalf of the user identity, so no connection strings are needed in the knowledge source definition. All content to which a user has access is in-scope for knowledge retrieval. To limit sites or constrain search, set a [filter expression](/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference). Your Azure tenant and the Microsoft 365 tenant must use the same Microsoft Entra ID tenant, and the caller's identity must be recognized by both tenants.
-
-+ You can use filters to scope search by URLs, date ranges, file types, and other metadata.
-
-+ SharePoint permissions and Purview labels are honored in requests for content.
-
-+ Usage is billed through Microsoft 365 and a Copilot license.
+To limit sites or constrain search, set a [filter expression](#filter-expression-examples) to scope by URLs, date ranges, file types, and other metadata. The caller's identity must be recognized by both the Azure tenant and the Microsoft 365 tenant because the retrieval engine queries SharePoint on behalf of the user.
 
 Like any other knowledge source, you specify a remote SharePoint knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md) and use the results as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
 
@@ -30,14 +24,12 @@ Like any other knowledge source, you specify a remote SharePoint knowledge sourc
 
 + SharePoint in a Microsoft 365 tenant that's under the same Microsoft Entra ID tenant as Azure.
 
-+ A personal access token for local development or a user's identity from a client application.
++ A Microsoft 365 Copilot license for query-time access to SharePoint content.
 
-+ The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
++ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible.
 
-For local development, the agentic retrieval engine uses your access token to call SharePoint on your behalf. For more information about using a personal access token on requests, see [Connect to Azure AI Search](../../search-get-started-rbac.md).
-
 ## Limitations
 
 The following limitations in the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) apply to remote SharePoint knowledge sources.
@@ -85,11 +77,6 @@ The following JSON is an example response for a remote SharePoint knowledge sour
 
 Run the following code to create a remote SharePoint knowledge source.
 
-[API keys](../../search-security-api-keys.md) are used for your client connection to Azure AI Search and Azure OpenAI. Your access token is used by Azure AI Search to connect to SharePoint in Microsoft 365 on your behalf. You can only retrieve content that you're permitted to access. For more information about getting a personal access token and other values, see [Connect to Azure AI Search](../../search-get-started-rbac.md).
-
-> [!NOTE]
-> You can also use your personal access token to access Azure AI Search and Azure OpenAI if you [set up role assignments on each resource](../../search-security-rbac.md). Using API keys allows you to omit this step in this example.
-
 ```python
 # Create a remote SharePoint knowledge source
 from azure.core.credentials import AzureKeyCredential
@@ -129,7 +116,7 @@ You can pass the following properties to create a remote SharePoint knowledge so
 
 ### Filter expression examples
 
-Not all SharePoint properties are supported in the `filterExpression`. For a list of supported properties, see the [API reference](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval). Here's some more information about queryable properties that you can use in filter: [queryable properties](/graph/connecting-external-content-manage-schema#queryable).
+Not all SharePoint properties are supported in the `filterExpression`. For a list of supported properties, see the [API reference](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval). For queryable properties, see [Queryable](/graph/connecting-external-content-manage-schema#queryable).
 
 Learn more about [KQL filters](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval?pivots=graph-v1#example-7-use-filter-expressions) in the syntax reference.
 
@@ -144,75 +131,86 @@ Learn more about [KQL filters](/microsoft-365-copilot/extensibility/api/ai-servi
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../search-agentic-retrieval-how-to-create.md).
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
 
 ## Query a knowledge base
 
-The [retrieve action](../../agentic-retrieval-how-to-retrieve.md) on the knowledge base provides the user identity that authorizes access to content in Microsoft 365.
-
-Azure AI Search uses the access token to call the Copilot Retrieval API on behalf of the user identity. The access token is provided in the retrieve endpoint as a `x-ms-query-source-authorization` HTTP header.
+After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query SharePoint content. Remote SharePoint has source-specific behaviors for query-time filtering, query formulation, response fields, and permissions enforcement.
 
-```python
-from azure.identity import DefaultAzureCredential, get_bearer_token_provider
-from azure.core.credentials import AzureKeyCredential
-from azure.search.documents.knowledgebases import KnowledgeBaseRetrievalClient
-from azure.search.documents.knowledgebases.models import KnowledgeBaseMessage, KnowledgeBaseMessageTextContent, KnowledgeBaseRetrievalRequest, RemoteSharePointKnowledgeSourceParams
+### Apply a KQL filter at query time
 
-# Get access token
-identity_token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://search.azure.com/.default")
-token = identity_token_provider()
+You can pass a `filter_expression_add_on` in the `knowledge_source_params` on the retrieve request to apply a KQL filter at query time. If you specify `filter_expression_add_on` on the retrieve request and a `filter_expression` on the knowledge source definition, the filters are AND'd together.
 
-# Create knowledge base retrieval client
-kb_client = KnowledgeBaseRetrievalClient(endpoint = "search_url", knowledge_base_name = "knowledge_base_name", credential = AzureKeyCredential("api_key"))
+```python
+from azure.search.documents.knowledgebases.models import (
+    KnowledgeBaseMessage,
+    KnowledgeBaseMessageTextContent,
+    KnowledgeBaseRetrievalRequest,
+    RemoteSharePointKnowledgeSourceParams,
+)
 
-# Create retrieval request
 request = KnowledgeBaseRetrievalRequest(
-    include_activity = True,
-    messages = [
-        KnowledgeBaseMessage(role = "user", content = [KnowledgeBaseMessageTextContent(text = "What was covered in the keynote doc for Ignite 2024?")])
+    messages=[
+        KnowledgeBaseMessage(
+            role="user",
+            content=[
+                KnowledgeBaseMessageTextContent(
+                    text="contoso product planning"
+                )
+            ],
+        )
     ],
-    knowledge_source_params = [
+    knowledge_source_params=[
         RemoteSharePointKnowledgeSourceParams(
-            knowledge_source_name = "my-remote-sharepoint-ks",
-            filter_expression_add_on = "ModifiedBy:\"Adele Vance\"",
-            include_references = True,
-            include_reference_source_data = True
+            knowledge_source_name="my-remote-sharepoint-ks",
+            filter_expression_add_on="filetype:docx",
         )
-    ]
+    ],
 )
 
-# Pass access token to retrieve from knowledge base
-result = kb_client.retrieve(retrieval_request = request, x_ms_query_source_authorization = token)
-print(result.response[0].content[0].text)
+result = kb_client.retrieve(
+    retrieval_request=request,
+    x_ms_query_source_authorization=token,
+)
 ```
 
-The retrieve request also takes a [KQL filter](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval?pivots=graph-v1#example-7-use-filter-expressions) (`filter_expression_add_on`) if you want to apply constraints at query time. If you specify `filter_expression_add_on` on both the knowledge source and knowledge base retrieve action, the filters are AND'd together.
+### Write effective queries
+
+Queries that ask about the content itself are more effective than questions about where a file is located or when it was last updated. For example, "Where is the keynote doc for Ignite 2024" might return no results because the content itself doesn't disclose its location. A `filter_expression` on metadata is a better approach for file location or date-specific queries.
+
+A more effective question is "What is the keynote doc for Ignite 2024". The response includes the synthesized answer, query activity and token counts, plus the URL and other metadata.
 
-Queries asking questions about the content itself are more effective than questions about where a file is located or when it was last updated. For example, if you ask, "Where is the keynote doc for Ignite 2024", you might get "No relevant content was found for your query" because the content itself doesn't disclose its location. A filter on metadata is a better solution for file location or date-specific queries.
+### SharePoint-specific response fields
 
-A better question to ask is, "What is the keynote doc for Ignite 2024". The response includes the synthesized answer, query activity and token counts, plus the URL and other metadata.
+Remote SharePoint results include fields that don't appear for other knowledge source types, such as `resourceMetadata`, `webUrl`, and `searchSensitivityLabelInfo`.
 
 ```json
 {
     "resourceMetadata": {
         "Author": "Nuwan Amarathunga;Nurul Izzati",
         "Title": "Ignite 2024 Keynote Address"
-    }
-},
-"rerankerScore": 2.489522,
-"webUrl": "https://contoso-my.sharepoint.com/keynotes/nuamarth_contoso_com/Documents/Keynote-Ignite-2024.docx",
-"searchSensitivityLabelInfo": {
+    },
+    "rerankerScore": 2.489522,
+    "webUrl": "https://contoso-my.sharepoint.com/keynotes/Documents/Keynote-Ignite-2024.docx",
+    "searchSensitivityLabelInfo": {
         "displayName": "Confidential\\Contoso Extended",
         "sensitivityLabelId": "aaaaaaaa-0b0b-1c1c-2d2d-333333333333",
-        "tooltip": "Data is classified and protected. Contoso Full Time Employees (FTE) and non-employees can edit, reply, forward and print. Recipient can unprotect content with the right justification.",
+        "tooltip": "Data is classified and protected.",
         "priority": 5,
         "color": "#FF8C00",
         "isEncrypted": true
     }
+}
 ```
 
+### Enforce permissions at query time
+
+Remote SharePoint knowledge sources can enforce SharePoint permissions at query time. To enable this filtering, include the end user's access token in the retrieve request. The retrieval engine passes the token to the Copilot Retrieval API, which queries SharePoint and returns only content to which the user has access. SharePoint permissions and Microsoft Purview sensitivity labels are honored.
+
+Because remote SharePoint doesn't use a search index, no ingestion-time permissions configuration is needed. The access token is the only requirement.
+
+For instructions on passing the token, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
 ## Delete a knowledge source
 
 [!INCLUDE [Delete knowledge source using Python](knowledge-source-delete-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonを用いたリモートSharePoint知識ソースの設定手順の更新"
}
```

### Explanation
この変更は、Pythonを使用したリモートSharePoint知識ソースの設定に関するドキュメントの軽微な更新であり、主に内容の簡素化と明確化を目的としています。特に、リモートSharePoint知識ソースが[Copilot Retrieval API]を利用してMicrosoft 365から直接テキストコンテンツを取得する際に、検索インデックスや接続文字列が不要であることを強調しています。また、使用料がMicrosoft 365とCopilotライセンスを通じて請求される旨が明記されています。

新たに、フィルター式を使用して検索対象を絞り込む方法が更新され、ユーザーのIDがAzureテナントとMicrosoft 365テナントの両方で認識される必要があることが明確にされています。更に、クエリー時の権限を強制するために必要なアクセス・トークンに関する情報が追加され、SharePointの権限やMicrosoft Purviewの感度ラベルがどのように適用されるかに関する詳細が提供されています。

全体として、ドキュメントはユーザーがPythonを用いてリモートSharePoint知識ソースをより効率的に操作できるように改良されており、具体的な使用例やコードスニペットの明示化が行われています。これにより、ユーザーが設定手順をスムーズに理解し実行できるようになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-rest.md{#item-5514b1}

<details>
<summary>Diff</summary>
````diff
@@ -6,15 +6,9 @@ ms.date: 03/25/2026
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
 
-A *remote SharePoint knowledge source* uses the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) to query textual content directly from SharePoint in Microsoft 365, returning results to the agentic retrieval engine for merging, ranking, and response formulation. There's no search index used by this knowledge source, and only textual content is queried.
+A *remote SharePoint knowledge source* uses the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) to query textual content directly from SharePoint in Microsoft 365. No search index or connection string is needed. Only textual content is queried, and usage is billed through Microsoft 365 and a Copilot license.
 
-At query time, the remote SharePoint knowledge source calls the Copilot Retrieval API on behalf of the user identity, so no connection strings are needed in the knowledge source definition. All content to which a user has access is in-scope for knowledge retrieval. To limit sites or constrain search, set a [filter expression](/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference). Your Azure tenant and the Microsoft 365 tenant must use the same Microsoft Entra ID tenant, and the caller's identity must be recognized by both tenants.
-
-+ You can use filters to scope search by URLs, date ranges, file types, and other metadata.
-
-+ SharePoint permissions and Purview labels are honored in requests for content.
-
-+ Usage is billed through Microsoft 365 and a Copilot license.
+To limit sites or constrain search, set a [filter expression](#filter-expression-examples) to scope by URLs, date ranges, file types, and other metadata. The caller's identity must be recognized by both the Azure tenant and the Microsoft 365 tenant because the retrieval engine queries SharePoint on behalf of the user.
 
 Like any other knowledge source, you specify a remote SharePoint knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md) and use the results as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
 
@@ -30,16 +24,12 @@ Like any other knowledge source, you specify a remote SharePoint knowledge sourc
 
 + SharePoint in a Microsoft 365 tenant that's under the same Microsoft Entra ID tenant as Azure.
 
-+ A personal access token for local development or a user's identity from a client application.
++ A Microsoft 365 Copilot license for query-time access to SharePoint content.
 
 + The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible.
 
-For local development, the agentic retrieval engine uses your access token to call SharePoint on your behalf. For more information about using a personal access token on requests, see [Connect to Azure AI Search](../../search-get-started-rbac.md).
-
-<!-- invalid filter expression will return a 400 soon, so we should be able to remove this limitation -->
-
 ## Limitations
 
 The following limitations in the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) apply to remote SharePoint knowledge sources.
@@ -87,11 +77,6 @@ The following JSON is an example response for a remote SharePoint knowledge sour
 
 Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create a remote SharePoint knowledge source.
 
-[API keys](../../search-security-api-keys.md) are used for your client connection to Azure AI Search and Azure OpenAI. Your access token is used by Azure AI Search to connect to SharePoint in Microsoft 365 on your behalf. You can only retrieve content that you're permitted to access. For more information about getting a personal access token and other values, see [Connect to Azure AI Search](../../search-get-started-rbac.md).
-
-> [!NOTE]
-> You can also use your personal access token to access Azure AI Search and Azure OpenAI if you [set up role assignments on each resource](../../search-security-rbac.md). Using API keys allows you to omit this step in this example.
-
 ```http
 POST {{search-url}}/knowledgesources/my-remote-sharepoint-ks?api-version=2025-11-01-preview
 api-key: {{api-key}}
@@ -110,8 +95,6 @@ Content-Type: application/json
 }
 ```
 
-<!-- Should we include a response and do we need to say anything about purview sensitivity labels? -->
-
 ### Source-specific properties
 
 You can pass the following properties to create a remote SharePoint knowledge source.
@@ -129,7 +112,7 @@ You can pass the following properties to create a remote SharePoint knowledge so
 
 ### Filter expression examples
 
-Not all SharePoint properties are supported in the `filterExpression`. For a list of supported properties, see the [API reference](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval). Here's some more information about queryable properties that you can use in filter: [queryable properties](/graph/connecting-external-content-manage-schema#queryable).
+Not all SharePoint properties are supported in the `filterExpression`. For a list of supported properties, see the [API reference](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval). For queryable properties, see [Queryable](/graph/connecting-external-content-manage-schema#queryable).
 
 Learn more about [KQL filters](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval?pivots=graph-v1#example-7-use-filter-expressions) in the syntax reference.
 
@@ -144,71 +127,78 @@ Learn more about [KQL filters](/microsoft-365-copilot/extensibility/api/ai-servi
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../search-agentic-retrieval-how-to-create.md).
-
-After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
+If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md).
 
 ## Query a knowledge base
 
-The [retrieve action](../../agentic-retrieval-how-to-retrieve.md) on the knowledge base provides the user identity that authorizes access to content in Microsoft 365. 
+After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query SharePoint content. Remote SharePoint has source-specific behaviors for query-time filtering, query formulation, response fields, and permissions enforcement.
 
-Azure AI Search uses the access token to call the Copilot Retrieval API on behalf of the user identity. The access token is provided in the retrieve endpoint as a `x-ms-query-source-authorization` HTTP header.
+### Apply a KQL filter at query time
 
-Make sure that you [generate an access token](../../search-get-started-rbac.md?pivots=rest#get-token) for the tenant that has your search service.
+You can pass a `filterExpressionAddOn` in the `knowledgeSourceParams` on the retrieve request to apply a KQL filter at query time. If you specify `filterExpressionAddOn` on the retrieve request and a `filterExpression` on the knowledge source definition, the filters are AND'd together.
 
 ```http
-POST {{search-url}}/knowledgebases/remote-sp-kb/retrieve?api-version={{api-version}}
-api-key: {{api-key}}
+POST {{search-url}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2025-11-01-preview
+Authorization: Bearer {{accessToken}}
 Content-Type: application/json
-x-ms-query-source-authorization: {{access-token}}
+x-ms-query-source-authorization: {{user-access-token}}
 
 {
     "messages": [
         {
             "role": "user",
             "content": [
-                { "type": "text", "text": "What was covered in the keynote doc for Ignite 2024?" }
+                { "type": "text", "text": "contoso product planning" }
             ]
         }
     ],
-    "includeActivity": true,
     "knowledgeSourceParams": [
         {
-            "filterExpressionAddOn": "ModifiedBy:\"Adele Vance\"",
             "knowledgeSourceName": "my-remote-sharepoint-ks",
             "kind": "remoteSharePoint",
-            "includeReferences": true,
-            "includeReferenceSourceData": true
+            "filterExpressionAddOn": "filetype:docx"
         }
     ]
 }
 ```
 
-The retrieve request also takes a [KQL filter](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval?pivots=graph-v1#example-7-use-filter-expressions) (`filterExpressionAddOn`) if you want to apply constraints at query time. If you specify `filterExpressionAddOn` on both the knowledge source and knowledge base retrieve action, the filters are AND'd together.
+### Write effective queries
+
+Queries that ask about the content itself are more effective than questions about where a file is located or when it was last updated. For example, "Where is the keynote doc for Ignite 2024" might return no results because the content itself doesn't disclose its location. A `filterExpression` on metadata is a better approach for file location or date-specific queries.
+
+A more effective question is "What is the keynote doc for Ignite 2024". The response includes the synthesized answer, query activity and token counts, plus the URL and other metadata.
 
-Queries asking questions about the content itself are more effective than questions about where a file is located or when it was last updated. For example, if you ask, "Where is the keynote doc for Ignite 2024", you might get "No relevant content was found for your query" because the content itself doesn't disclose its location. A filter on metadata is a better solution for file location or date-specific queries.
+### SharePoint-specific response fields
 
-A better question to ask is, "What is the keynote doc for Ignite 2024". The response includes the synthesized answer, query activity and token counts, plus the URL and other metadata.
+Remote SharePoint results include fields that don't appear for other knowledge source types, such as `resourceMetadata`, `webUrl`, and `searchSensitivityLabelInfo`.
 
 ```json
 {
     "resourceMetadata": {
         "Author": "Nuwan Amarathunga;Nurul Izzati",
         "Title": "Ignite 2024 Keynote Address"
-    }
-},
-"rerankerScore": 2.489522,
-"webUrl": "https://contoso-my.sharepoint.com/keynotes/nuamarth_contoso_com/Documents/Keynote-Ignite-2024.docx",
-"searchSensitivityLabelInfo": {
+    },
+    "rerankerScore": 2.489522,
+    "webUrl": "https://contoso-my.sharepoint.com/keynotes/Documents/Keynote-Ignite-2024.docx",
+    "searchSensitivityLabelInfo": {
         "displayName": "Confidential\\Contoso Extended",
         "sensitivityLabelId": "aaaaaaaa-0b0b-1c1c-2d2d-333333333333",
-        "tooltip": "Data is classified and protected. Contoso Full Time Employees (FTE) and non-employees can edit, reply, forward and print. Recipient can unprotect content with the right justification.",
+        "tooltip": "Data is classified and protected.",
         "priority": 5,
         "color": "#FF8C00",
         "isEncrypted": true
     }
+}
 ```
 
+### Enforce permissions at query time
+
+Remote SharePoint knowledge sources can enforce SharePoint permissions at query time. To enable this filtering, include the end user's access token in the retrieve request. The retrieval engine passes the token to the Copilot Retrieval API, which queries SharePoint and returns only content to which the user has access. SharePoint permissions and Microsoft Purview sensitivity labels are honored.
+
+Because remote SharePoint doesn't use a search index, no ingestion-time permissions configuration is needed. The access token is the only requirement.
+
+For instructions on passing the token, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time).
+
 ## Delete a knowledge source
 
 [!INCLUDE [Delete knowledge source using REST](knowledge-source-delete-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIを用いたリモートSharePoint知識ソースの設定手順の更新"
}
```

### Explanation
この変更は、REST APIを使用したリモートSharePoint知識ソースの設定に関するドキュメントの軽微な更新です。主に内容の明確化と一貫性の向上を目的としています。具体的には、Remote SharePointknowledge source が[Copilot Retrieval API]を用いて、Microsoft 365からテキストコンテンツを直接照会する際に、検索インデックスや接続文字列が不要であることが再確認されています。使用料はMicrosoft 365とCopilotライセンスを通じて請求されることが明記されています。

新たに、フィルター式を使用することで検索対象を絞り込む方法が更新され、ユーザーのIDがAzureテナントとMicrosoft 365テナントの両方で認識される必要があることを強調しています。また、各種権限の管理を行うために必要なアクセス・トークンに関する情報が追加されました。これにより、SharePointの権限やMicrosoft Purviewの感度ラベルがどのように適用されるかについての詳しい説明がなされています。

全体として、ドキュメントはREST APIを用いてリモートSharePoint知識ソースを設定する際の実用的な手順がより明確に記載されており、ユーザーが操作をスムーズに理解して実行できるように改良されています。改訂されたコードスニペットやクエリの書き方の例も含まれており、具体的な支援が提供されています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-csharp.md{#item-401063}

<details>
<summary>Diff</summary>
````diff
@@ -39,7 +39,7 @@ When you use Web Knowledge Source, keep the following in mind:
 
 + An Azure AI Search service in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). The service must also be in an [Azure public region](../../search-region-support.md#azure-public-regions), as Web Knowledge Source isn't supported in private or sovereign clouds.
 
-+ The latest preview version of the [`Azure.Search.Documents` client library](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1) for the .NET SDK.
++ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": ".NET SDK用Azure.Search.Documentsパッケージのインストール手順の更新"
}
```

### Explanation
この変更は、C#を使用したWeb知識ソースの利用に関するドキュメントの軽微な更新です。具体的には、`.NET SDK`での`Azure.Search.Documents`クライアントライブラリのインストール方法についての記述が改訂されています。

変更点として、パッケージのインストール手順がより具体的になり、`dotnet add package Azure.Search.Documents --prerelease` というコマンドが推奨されています。この変更により、ユーザーは最新のプレビュー版が簡単にインストールできるようになります。また、Azureの公共リージョンにおけるエージェントリトリーバル機能の利用や、セマンティックランカーの有効化に関する要件も引き続き明記されています。

全体として、この更新はユーザーがAzureのWeb知識ソースを使用する際の手順の明確化と簡素化を図っており、より良い体験を提供することを目的としています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-python.md{#item-72b59c}

<details>
<summary>Diff</summary>
````diff
@@ -39,7 +39,7 @@ When you use Web Knowledge Source, keep the following in mind:
 
 + An Azure AI Search service in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). The service must also be in an [Azure public region](../../search-region-support.md#azure-public-regions), as Web Knowledge Source isn't supported in private or sovereign clouds.
 
-+ The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
++ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python用azure-search-documentsパッケージのインストール手順の更新"
}
```

### Explanation
この変更は、Pythonを用いたWeb知識ソースの利用に関するドキュメントの軽微な更新です。具体的には、`azure-search-documents`クライアントライブラリのインストール手順が改訂されています。

変更内容として、最新のプレビュー版パッケージをインストールするための具体的なコマンドが示されています。新しい推奨コマンドは、`pip install --pre azure-search-documents`となっており、これによりユーザーは簡単に最新のプレビュー版を取得できるようになります。また、Azureの公共リージョンにおいてエージェントリトリーバル機能を利用するためには、セマンティックランカーの有効化が必要であることも再確認されています。

全体を通して、この更新はPythonでのWeb知識ソース使用時の手順をより明確にし、ユーザーが必要なパッケージを迅速にインストールできるようにすることを目的としています。これによって、ユーザーエクスペリエンスが向上し、ドキュメントの有用性が増しています。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-csharp.md{#item-4469a2}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 01/23/2026
+ms.date: 03/17/2026
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -38,7 +38,7 @@ After you create a knowledge base, you can update its properties at any time. If
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md). **Search Service Contributor** can create and manage a knowledge base. **Search Index Data Reader** can run queries. Alternatively, you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
-+ The latest preview version of the [`Azure.Search.Documents` client library](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1) for the .NET SDK.
++ The latest [`Azure.Search.Documents` preview package](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1): `dotnet add package Azure.Search.Documents --prerelease`
 
 ### Supported models
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#用の知識ベース作成手順の更新"
}
```

### Explanation
この変更は、C#を使用した知識ベースの作成に関するドキュメントの軽微な更新です。主な内容は、日付の更新とクライアントライブラリのインストール手順の明確化です。

具体的には、日付が2026年1月23日から2026年3月17日に更新されています。この日付更新は、ドキュメントの正確性向上を目的としています。また、最新の`Azure.Search.Documents`クライアントライブラリのインストール方法が具体的なコマンド付きで説明されています。新しい推奨コマンドは、`dotnet add package Azure.Search.Documents --prerelease`となっており、ユーザーがプレビュー版を適切にインストールできるようにサポートされています。

さらに、Azure AI Searchサービスでの役割ベースのアクセス権についての情報も強調されており、特定の役割（**Search Service Contributor** や **Search Index Data Reader**）がどのような操作を行えるかが明記されています。この全体的な変更は、C#を使用して知識ベースを作成する際の手順をよりわかりやすくし、ユーザーが必要な情報を素早く取得できるようにすることを目指しています。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-python.md{#item-4e498f}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 01/15/2026
+ms.date: 03/17/2026
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -38,7 +38,7 @@ After you create a knowledge base, you can update its properties at any time. If
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md). **Search Service Contributor** can create and manage a knowledge base. **Search Index Data Reader** can run queries. Alternatively, you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
-+ The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
++ The latest [`azure-search-documents` preview package](https://pypi.org/project/azure-search-documents/11.7.0b2/): `pip install --pre azure-search-documents`
 
 ### Supported models
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python用の知識ベース作成手順の更新"
}
```

### Explanation
この変更は、Pythonを使用した知識ベースの作成に関するドキュメントの軽微な更新です。主な修正点は、日付の更新とクライアントライブラリのインストール手順の改善です。

具体的には、初版の日付が2026年1月15日から2026年3月17日に変更されています。この更新は、ドキュメントが最新の情報を反映することを目的としています。また、Python用の`azure-search-documents`クライアントライブラリに関するインストール手順が更新され、新たに提供されたコマンドが明確に示されています。推奨コマンドは`pip install --pre azure-search-documents`であり、ユーザーが最新のプレビュー版を簡単にインストールできるようになっています。

さらに、Azure AI Searchサービスにおける役割ベースのアクセス権についての説明が強調されており、特定の役割（**Search Service Contributor**や**Search Index Data Reader**）がどのような権限を持つかが明記されています。この更新は、ユーザーがPythonで知識ベースを作成する際の手順をよりわかりやすくし、必要な情報を迅速に得られるようにすることを目指しています。

## articles/search/includes/how-tos/knowledge-source-ingestion-parameters-csharp.md{#item-7a6ef1}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/19/2025
+ms.date: 03/17/2026
 ---
 
 For indexed knowledge sources only, you can pass the following `ingestionParameters` properties to control how content is ingested and processed.
@@ -10,9 +10,10 @@ For indexed knowledge sources only, you can pass the following `ingestionParamet
 |--|--|--|--|--|
 | `Identity` | A [managed identity](../../search-how-to-managed-identities.md) to use in the generated indexer. | Object | Yes | No |
 | `DisableImageVerbalization` | Enables or disables the use of image verbalization. The default is `False`, which *enables* image verbalization. Set to `True` to *disable* image verbalization. | Boolean | No | No |
-| `ChatCompletionModel` | A chat completion model that verbalizes images or extracts content. Supported models are `gpt-4o`, `gpt-4o-mini`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5-mini`, and `gpt-5-nano`. The [GenAI Prompt skill](../../cognitive-search-skill-genai-prompt.md) will be included in the generated skillset. Setting this parameter also requires that `disable_image_verbalization` is set to `False`. | Object | Only `api_key` and `deployment_name` are editable | No |
-| `EmbeddingModel` | A text embedding model that vectorizes text and image content during indexing and at query time. Supported models are `text-embedding-ada-002`, `text-embedding-3-small`, and `text-embedding-3-large`. The [Azure OpenAI Embedding skill](../../cognitive-search-skill-azure-openai-embedding.md) will be included in the generated skillset, and the [Azure OpenAI vectorizer](../../vector-search-vectorizer-azure-open-ai.md) will be included in the generated index. | Object | Only `api_key` and `deployment_name` are editable | No |
+| `ChatCompletionModel` | A chat completion model that verbalizes images or extracts content. Supported models are `gpt-4o`, `gpt-4o-mini`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5-mini`, and `gpt-5-nano`. The [GenAI Prompt skill](../../cognitive-search-skill-genai-prompt.md) will be included in the generated skillset. Setting this parameter also requires that `DisableImageVerbalization` is set to `False`. | Object | Only `ApiKey` and `DeploymentName` are editable | No |
+| `EmbeddingModel` | A text embedding model that vectorizes text and image content during indexing and at query time. Supported models are `text-embedding-ada-002`, `text-embedding-3-small`, and `text-embedding-3-large`. The [Azure OpenAI Embedding skill](../../cognitive-search-skill-azure-openai-embedding.md) will be included in the generated skillset, and the [Azure OpenAI vectorizer](../../vector-search-vectorizer-azure-open-ai.md) will be included in the generated index. | Object | Only `ApiKey` and `DeploymentName` are editable | No |
 | `ContentExtractionMode` | Controls how content is extracted from files. The default is `minimal`, which uses standard content extraction for text and images. Set to `standard` for advanced document cracking and chunking using the [Azure Content Understanding skill](../../cognitive-search-skill-content-understanding.md), which will be included in the generated skillset. For `standard` only, the `AiServices` and `AssetStore` parameters are specifiable. | String | No | No |
-| `AiServices` | A Microsoft Foundry resource to access Azure Content Understanding in Foundry Tools. Setting this parameter requires that `ContentExtractionMode` is set to `standard`. | Object | Only `api_key` is editable | Yes |
+| `AiServices` | A Microsoft Foundry resource to access Azure Content Understanding in Foundry Tools. Setting this parameter requires that `ContentExtractionMode` is set to `standard`. | Object | Only `ApiKey` is editable | Yes |
+| `AssetStore` | A blob container to store extracted images. Setting this parameter requires that `ContentExtractionMode` is set to `standard`. | Object | No | No |
 | `IngestionSchedule` | Adds scheduling information to the generated indexer. You can also [add a schedule](../../search-howto-schedule-indexers.md) later to automate data refresh. | Object | Yes | No |
-| `IngestionPermissionOptions` | The document-level permissions to ingest from select knowledge sources: either [ADLS Gen2](../../agentic-knowledge-source-how-to-blob.md) or [indexed SharePoint](../../agentic-knowledge-source-how-to-sharepoint-indexed.md). If you specify `user_ids`, `group_ids`, or `rbac_scope`, the generated [ADLS Gen2 indexer](../../search-indexer-access-control-lists-and-role-based-access.md) or [SharePoint indexer](../../search-indexer-sharepoint-access-control-lists.md) will include the ingested permissions. | Array | No | No |
+| `IngestionPermissionOptions` | The document-level permissions to ingest alongside content. Specify `UserIds`, `GroupIds`, or `RbacScope` to store permission metadata in the index. For source-specific guidance, see [Ingest RBAC permissions from blob storage](../../search-blob-indexer-role-based-access.md#configure-a-knowledge-source) and [Ingest ACLs from ADLS Gen2](../../search-indexer-access-control-lists-and-role-based-access.md#configure-a-knowledge-source). To enforce these permissions at query time, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time). | Array | No | No |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#用の知識ソース取り込みパラメータの更新"
}
```

### Explanation
この変更は、C#を利用した知識ソースの取り込みパラメータに関するドキュメントの軽微な更新です。主な内容は、日付の更新と詳細なパラメータの説明の改良です。

具体的には、日付が2025年11月19日から2026年3月17日に更新され、ドキュメントの最新性が確保されています。また、`ingestionParameters`に関連するパラメータの説明が強化され、それぞれのパラメータの機能や使用方法がより明確に記載されています。

更新されたパラメータには、`ChatCompletionModel`や`EmbeddingModel`のような重要な項目が含まれており、これらはコンテンツの処理方法に影響を与えます。特に、パラメータの名前の表記が統一され、`ApiKey`や`DeploymentName`に関する情報が強調されています。新たに追加された`AssetStore`パラメータは、抽出した画像を保存するためのblobコンテナに関する情報です。この変更によって、ユーザーは知識ソースの取り込みをより適切に管理できるようになります。

さらに、文書の中での例外や条件が明文化され、ユーザーに対してより具体的なガイダンスが提供されます。この一連の更新は、C#での知識ソース取り込みプロセスにおける理解を深め、実装を容易にすることを目的としています。

## articles/search/includes/how-tos/knowledge-source-ingestion-parameters-python.md{#item-c92d9f}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/13/2025
+ms.date: 03/17/2026
 ---
 
 For indexed knowledge sources only, you can pass the following `ingestionParameters` properties to control how content is ingested and processed.
@@ -16,4 +16,4 @@ For indexed knowledge sources only, you can pass the following `ingestionParamet
 | `ai_services` | A Microsoft Foundry resource to access Azure Content Understanding in Foundry Tools. Setting this parameter requires that `content_extraction_mode` is set to `standard`. | Object | Only `api_key` is editable | Yes |
 | `asset_store` | A blob container to store extracted images. Setting this parameter requires that `content_extraction_mode` is set to `standard`. | Object | No | No |
 | `ingestion_schedule` | Adds scheduling information to the generated indexer. You can also [add a schedule](../../search-howto-schedule-indexers.md) later to automate data refresh. | Object | Yes | No |
-| `ingestion_permission_options` | The document-level permissions to ingest from select knowledge sources: either [ADLS Gen2](../../agentic-knowledge-source-how-to-blob.md) or [indexed SharePoint](../../agentic-knowledge-source-how-to-sharepoint-indexed.md). If you specify `user_ids`, `group_ids`, or `rbac_scope`, the generated [ADLS Gen2 indexer](../../search-indexer-access-control-lists-and-role-based-access.md) or [SharePoint indexer](../../search-indexer-sharepoint-access-control-lists.md) will include the ingested permissions. | Array | No | No |
+| `ingestion_permission_options` | The document-level permissions to ingest alongside content. Specify `user_ids`, `group_ids`, or `rbac_scope` to store permission metadata in the index. For source-specific guidance, see [Ingest RBAC permissions from blob storage](../../search-blob-indexer-role-based-access.md#configure-a-knowledge-source) and [Ingest ACLs from ADLS Gen2](../../search-indexer-access-control-lists-and-role-based-access.md#configure-a-knowledge-source). To enforce these permissions at query time, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time). | Array | No | No |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python用の知識ソース取り込みパラメータの更新"
}
```

### Explanation
この変更は、Pythonを用いた知識ソースの取り込みパラメータに関するドキュメントの軽微な更新です。具体的には、ドキュメントの日付の更新といくつかのパラメータに対する説明が改善されています。

主な更新点として、日付が2025年11月13日から2026年3月17日に変更され、最新の情報が反映されています。また、`ingestion_permission_options`についての説明が強化され、指定できるパラメータ（`user_ids`、`group_ids`、`rbac_scope`）が明確に記載されています。このセクションは、ドキュメントレベルの権限をどのように扱うかに関するガイダンスを提供しており、データを取り込む際の権限の管理に関して具体的な情報が追加されています。

さらに、ソースごとのガイダンスに関するリンクが追加され、ユーザーが権限を効率的に設定・管理できるようになっています。これらの更新は、Pythonを使用した知識ソースの取り込みプロセスをよりスムーズにし、ユーザーに対する理解を深めるために役立つことを目指しています。

## articles/search/includes/how-tos/knowledge-source-ingestion-parameters-rest.md{#item-f29dc2}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/10/2025
+ms.date: 03/17/2026
 ---
 
 For indexed knowledge sources only, you can pass the following `ingestionParameters` properties to control how content is ingested and processed.
@@ -16,4 +16,4 @@ For indexed knowledge sources only, you can pass the following `ingestionParamet
 | `aiServices` | A Microsoft Foundry resource to access Azure Content Understanding in Foundry Tools. Setting this parameter requires that `contentExtractionMode` is set to `standard`. | Object | Only `apiKey` is editable | Yes |
 | `assetStore` | A blob container to store extracted images. Setting this parameter requires that `contentExtractionMode` is set to `standard`. | Object | No | No |
 | `ingestionSchedule` | Adds scheduling information to the generated indexer. You can also [add a schedule](../../search-howto-schedule-indexers.md) later to automate data refresh. | Object | Yes | No |
-| `ingestionPermissionOptions` | The document-level permissions to ingest from select knowledge sources: either [ADLS Gen2](../../agentic-knowledge-source-how-to-blob.md) or [indexed SharePoint](../../agentic-knowledge-source-how-to-sharepoint-indexed.md). If you specify `userIds`, `groupIds`, or `rbacScope`, the generated [ADLS Gen2 indexer](../../search-indexer-access-control-lists-and-role-based-access.md) or [SharePoint indexer](../../search-indexer-sharepoint-access-control-lists.md) will include the ingested permissions. | Array | No | No |
+| `ingestionPermissionOptions` | The document-level permissions to ingest alongside content. Specify `userIds`, `groupIds`, or `rbacScope` to store permission metadata in the index. For source-specific guidance, see [Ingest RBAC permissions from blob storage](../../search-blob-indexer-role-based-access.md#configure-a-knowledge-source) and [Ingest ACLs from ADLS Gen2](../../search-indexer-access-control-lists-and-role-based-access.md#configure-a-knowledge-source). To enforce these permissions at query time, see [Enforce permissions at query time](../../agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time). | Array | No | No |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST API用の知識ソース取り込みパラメータの更新"
}
```

### Explanation
この変更は、REST APIを使用した知識ソースの取り込みパラメータに関するドキュメントの軽微な更新です。主な内容は、ドキュメントの日付の更新と一部のパラメータに対する説明の改善です。

具体的には、日付が2025年11月10日から2026年3月17日に変更されています。これは情報の最新化を目的としています。また、`ingestionPermissionOptions`に関する説明が改良され、具体的には、ユーザーが指定できるパラメータ（`userIds`、`groupIds`、`rbacScope`）が明確に記載されており、これにより権限メタデータをインデックスに保存する方法についての理解が深まります。

さらに、データを取り込む際の権限に関するガイダンスが強化され、関連するリソースへのリンクも充実しています。これにより、ユーザーは権限管理をより適切に行うことができるようになります。この一連の更新は、REST APIを使用した知識ソースの取り込みプロセスをより円滑にし、ユーザーの理解を向上させることを目指しています。


