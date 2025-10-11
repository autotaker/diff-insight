---
date: '2025-10-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:183411d...MicrosoftDocs:943bdb9
summary: この記事の変更は、エージェント的知識ソースの管理に関するドキュメントの更新を示しており、特に知識ソースの削除と検索インデックスの管理に関する簡略化と明確化が行われました。また、新しいREST
  APIガイドが追加され、知識ソースを削除するための具体的な手順が提供されるようになりました。この更新により、ユーザーは知識ソースの管理をより効率的に理解できるようになり、特に開発者や管理者向けに役立つ情報が整備されています。全体として、ドキュメントのメンテナンス性や使用性が向上し、ユーザーエクスペリエンスの向上を目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:183411d...MicrosoftDocs:943bdb9){target="_blank"}

<format>
# ハイライト
この記事の変更は、エージェント的知識ソースの管理に関するドキュメントに対する更新を示しており、特に削除と検索インデックスの管理方法についての簡略化と明確化が行われました。また、新しいREST APIガイドが追加され、知識ソースを削除する際の具体的な手順が提供されるようになりました。

## 新機能
- 知識ソース削除用の新しいREST APIガイドが追加されました。このドキュメントでは、知識エージェントを適切に管理するための詳細手順と具体的なAPIリクエストを提供しています。

## 破壊的変更
- 特に破壊的な変更は示されていませんが、多くのセクションで内容の簡略化と調整が行われ、以前のドキュメント構成に依存している場合、参照方法が変わる可能性があります。

## その他の更新
- 記事の日付が更新され、最新の情報であることを示します（2025年8月29日から2025年10月10日に更新）。
- ドキュメントのタイトルや説明に変更が加えられ、内容がより明確になるように調整されました。
- 重要な情報や注意事項が新しいインクルードファイルに移され、ドキュメントの参照性が向上しました。

# インサイト
この更新では、エージェント的知識ソースに関連するドキュメントが大幅に改善されました。まず、日付の更新により、最新の情報が提供されていることが強調されています。さらに、ドキュメントの内容が具体的かつ簡潔に再構成されることで、ユーザーは知識ソースの管理に関する手順をより効率的に理解できるようになっています。

特に注目すべきは、知識ソース削除のための具体的なREST APIガイドの追加です。この新しいガイドは、開発者や管理者がAPIを利用して効果的に知識ソースを削除できるように設計されており、失敗した場合のフィードバックや事前準備事項も明確にされています。これにより、システムのクリーンアップやメンテナンス作業がスムーズになり、開発作業の信頼性が向上すると期待されます。

全体として、この変更は情報の正確性を保ちつつ、ユーザーエクスペリエンスの向上を狙ったものであり、ドキュメントのメンテナンス性や使用性が向上しています。エージェント的知識ソースに関連する新しい変更は、ユーザーの実務に直接役立つ情報とツールを提供することを目指しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-blob.md](#item-ac6c8a) | minor update | エージェント的知識ソースのハウツーに関する記事の更新 | modified | 2 | 14 | 16 | 
| [agentic-knowledge-source-how-to-search-index.md](#item-09d366) | minor update | エージェント的知識ソースの検索インデックスに関する記事の更新 | modified | 2 | 8 | 10 | 
| [agentic-knowledge-source-overview.md](#item-dcf29a) | minor update | エージェント的知識ソースの概要に関する記事の更新 | modified | 39 | 53 | 92 | 
| [knowledge-source-delete-rest.md](#item-225321) | new feature | 知識ソース削除用のREST APIガイド | added | 89 | 0 | 89 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-blob.md{#item-ac6c8a}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/29/2025
+ms.date: 10/10/2025
 ---
 
 # Create a blob knowledge source
@@ -219,19 +219,7 @@ After the knowledge agent is configured, use the retrieve action to query the kn
 
 ## Delete a knowledge source
 
-If you no longer need the knowledge source, or if you need to rebuild it on the search service, use this request to delete the current object.
-
-```http
-# Delete agent
-DELETE {{search-url}}/knowledgeSources/{{ks-name}}?api-version=2025-08-01-preview
-api-key: {{api-key}}
-```
-
-> [!IMPORTANT]
-> Before you can delete a knowledge source, you must first update the knowledge agent to remove all references to the knowledge source.
->
-> Deleting a blob knowledge source also deletes the objects it created. The indexer, data source, skillset, and index are automatically deleted when the blob knowledge source is deleted.
->
+[!INCLUDE [Delete knowledge source](includes/how-tos/knowledge-source-delete-rest.md)]
 
 ## Learn more
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント的知識ソースのハウツーに関する記事の更新"
}
```

### Explanation
この変更は、`articles/search/agentic-knowledge-source-how-to-blob.md`ファイルに対する修正を示しています。主な調整点は次のとおりです。

1. **日付の更新**: ドキュメント内の日付が2025年8月29日から2025年10月10日に変更されました。これは情報の正確性を保つために必要な更新です。

2. **セクションの削除と調整**: 知識ソースを削除する際の手順に関するセクションが大幅に変更されました。具体的には、削除手順が簡略化され、重要な注意事項が新しいインクルードファイルへのリンクに置き換えられました。これはドキュメントの簡潔さと、関連情報へのアクセスを向上させるための改善です。

この変更は、コードのメンテナンスやデータベースのクリーンアップに役立つ情報を提供し、可読性を高めることを目的としています。

## articles/search/agentic-knowledge-source-how-to-search-index.md{#item-09d366}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/29/2025
+ms.date: 10/10/2025
 ---
 
 # Create a search index knowledge source
@@ -121,13 +121,7 @@ Within the knowledge agent, there are more properties to set on the knowledge so
 
 ## Delete a knowledge source
 
-If you no longer need the knowledge source, or if you need to rebuild it on the search service, use this request to delete the current object.
-
-```http
-# Delete agent
-DELETE {{search-url}}/knowledgeSources/{{ks-name}}?api-version=2025-08-01-preview
-api-key: {{api-key}}
-```
+[!INCLUDE [Delete knowledge source](includes/how-tos/knowledge-source-delete-rest.md)]
 
 ## Learn more
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント的知識ソースの検索インデックスに関する記事の更新"
}
```

### Explanation
この変更は、`articles/search/agentic-knowledge-source-how-to-search-index.md`ファイルに対する修正を示しています。主な変更点は以下の通りです。

1. **日付の更新**: ドキュメント内の日付が2025年8月29日から2025年10月10日に更新されました。この更新は、情報の正確性を維持するための重要な部分です。

2. **セクションの簡略化**: 知識ソースを削除する手順に関する説明が簡略化され、元の詳細な手順が削除されました。その代わりに、関連情報を含む新しいインクルードファイルへの参照が追加されています。これにより、ドキュメントの可読性が向上し、新しい情報に簡単にアクセスできるようになっています。

この変更は、ユーザーに対してより明確で理解しやすい情報を提供することを目指しており、同時に文書のメンテナンス性も高めています。

## articles/search/agentic-knowledge-source-overview.md{#item-dcf29a}

<details>
<summary>Diff</summary>
````diff
@@ -1,52 +1,71 @@
 ---
-title: Create a knowledge source
+title: What is a knowledge source
 titleSuffix: Azure AI Search
-description: Learn how to create a knowledge source for agentic retrieval workloads in Azure AI Search.
+description: Learn about the knowledge source object used for agentic retrieval workloads in Azure AI Search.
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
-ms.topic: how-to
-ms.date: 10/01/2025
+ms.topic: concept-article
+ms.date: 10/09/2025
 ---
 
-# Create a knowledge source
+# What is a knowledge source?
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
 A knowledge source wraps a search index with extra properties for agentic retrieval. It's a required definition in a knowledge agent. We provide guidance on how to create specific knowledge sources, but generally, you can:
 
-+ Create multiple knowledge sources as top-level resources on your search service.
++ Create a knowledge source as a top-level resource on your search service. Each knowledge source points to exactly one index, and that index must [meet the criteria for agentic retrieval](agentic-retrieval-how-to-create-index.md).
 
-+ Reference one or more knowledge sources in a knowledge agent. In an agentic retrieval pipeline, it's possible to query against multiple knowledge sources in single request. Subqueries are generated for each knowledge source. Top results are returned in the retrieval response.
++ Reference one or more knowledge sources in a knowledge agent. In an agentic retrieval pipeline, it's possible to query against multiple knowledge sources in a single request. Subqueries are generated for each knowledge source. Top results are returned in the retrieval response.
 
-Make sure you have at least one knowledge source before creating a knowledge agent. The full specification of a knowledge source and a knowledge agent is in the [REST API reference](/rest/api/searchservice). 
++ Use a knowledge source definition to generate a full indexer pipeline (data source, skillset, indexer, and index) that works for agentic retrieval. Instead of creating multiple objects manually, information in the knowledge source is used to generate all objects, including a populated and searchable index.
 
-## Key points about a knowledge source
+Make sure you have at least one knowledge source before creating a knowledge agent. The full specification of a knowledge source and a knowledge agent is in the [preview REST API reference](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true).
 
-+ Creation path: first create a knowledge source, then create a knowledge agent. Deletion path: update or delete knowledge agents, delete knowledge sources last.
+## Working with a knowledge source
 
-+ A knowledge source, its index, and the knowledge agent must all exist on the same search service.
++ Creation path: first create a knowledge source, then create a knowledge agent. 
+
++ Deletion path: update or delete knowledge agents to remove references to a knowledge source, and then delete the knowledge source last.
 
-+ Each knowledge source points to exactly one index, and that index must [meet the criteria for agentic retrieval](agentic-retrieval-how-to-create-index.md).
++ A knowledge source, its index, and the knowledge agent must all exist on the same search service.
 
-+ For each knowledge source, the knowledge agent provides extra properties for query execution. [KnowledgeSourceReference](/rest/api/searchservice/knowledge-agents/create-or-update#knowledgesourcereference?view=rest-searchservice-2025-08-01-preview&preserve-view=true) properties affect query planning. [KnowledgeAgentOutputConfiguration](/rest/api/searchservice/knowledge-agents/create-or-update#knowledgeagentoutputconfiguration?view=rest-searchservice-2025-08-01-preview&preserve-view=true) properties affect query output.
++ For each knowledge source, the knowledge agent provides extra properties for query execution. [`"knowledgeSources"`](/rest/api/searchservice/knowledge-agents/create-or-update#knowledgesourcereference?view=rest-searchservice-2025-08-01-preview&preserve-view=true) properties affect query planning. [`"outputConfiguration"`](/rest/api/searchservice/knowledge-agents/create-or-update#knowledgeagentoutputconfiguration?view=rest-searchservice-2025-08-01-preview&preserve-view=true) properties affect query output.
 
 ## Supported knowledge sources
 
 Here are the knowledge sources you can create in this preview:
 
-+ [Search index knowledge source (an existing index)](agentic-knowledge-source-how-to-search-index.md)
-+ [Blob knowledge source](agentic-knowledge-source-how-to-blob.md)
++ [`"searchIndex"`](/rest/api/searchservice/knowledge-sources/create-or-update#searchindexknowledgesource?view=rest-searchservice-2025-08-01-preview&preserve-view=true) wraps an existing index
++ [`"azureBlob"`](/rest/api/searchservice/knowledge-sources/create-or-update#azureblobknowledgesource?view=rest-searchservice-2025-08-01-preview&preserve-view=true) generates an indexer pipeline that pulls from a blob container
 
-A platform-specific knowledge source like the blob knowledge source includes specifications for generating an entire indexing pipeline that provides all extraction, enrichment and transformations over blob content, and a viable index. You can modify the pipeline and rerun the indexer, but you can't rename the objects.
+A platform-specific knowledge source like the blob knowledge source includes specifications for generating an entire indexing pipeline that provides extraction, skillset processing, and a viable index. You can modify the pipeline and rerun the indexer, but you can't rename the objects.
 
 > [!NOTE]
-> `WebKnowledgeSource` (also referred to as `WebParameters` in REST APIs) isn't currently available in the 2025-08-01-preview.
+> `WebKnowledgeSource` (also referred to as `WebParameters` in REST APIs) isn't currently operational in the 2025-08-01-preview.
+
+## Creating knowledge sources
+
+You must have [**Search Service Contributor** permissions](search-security-rbac.md) to create objects on a search service.  You also need **Search Index Data Contributor** permissions to load an index if you're using a knowledge source that creates an indexer pipeline. Alternatively, you can [use an API admin key](search-security-api-keys.md) instead of roles.
+
+You must use the REST API or an Azure SDK preview package to create a knowledge source. There's no portal support at this time. The following links provide instructions for creating a knowledge source:
+
++ [How to create a search index knowledge source (wraps an existing index)](agentic-knowledge-source-how-to-search-index.md)
++ [How to create a blob knowledge source (generates an indexer pipeline)](agentic-knowledge-source-how-to-blob.md)
+
+After the knowledge source is created, you can reference it in a knowledge agent.
+
+## Using knowledge sources
+
+Properties on the [*knowledge agent*](agentic-retrieval-how-to-create-knowledge-base.md) determine whether and how the knowledge source is used.
 
-## Control knowledge source usage
++ [`"knowledgeSources"`](/rest/api/searchservice/knowledge-agents/create-or-update#knowledgesourcereference?view=rest-searchservice-2025-08-01-preview&preserve-view=true) array specifies the knowledge sources available to the knowledge agent and informs the query logic.
 
-Properties on the knowledge agent determine whether and how the knowledge source is used. The [KnowledgeSourceReference](/rest/api/searchservice/knowledge-agents/create-or-update#knowledgesourcereference?view=rest-searchservice-2025-08-01-preview&preserve-view=true) array specifies the knowledge sources available to the knowledge agent.
++ [`"outputConfiguration"`](/rest/api/searchservice/knowledge-agents/create-or-update#knowledgeagentoutputconfiguration?view=rest-searchservice-2025-08-01-preview&preserve-view=true) properties affect query output.
+
+The knowledge agent uses the [retrieve action](agentic-retrieval-how-to-retrieve.md) to send queries to the index specified in the knowledge source.
 
 ### Use multiple knowledge sources simultaneously
 
@@ -57,7 +76,7 @@ When you have multiple knowledge sources, set the following properties to bias q
 
 Retrieval instructions are sent as a user-defined prompt to the large language model (LLM) used for query planning. This prompt is helpful when you have multiple knowledge sources and want to provide guidance on when to use each one. For example, if you have separate indexes for product information, job postings, and technical support, the retrieval instructions might say "use the jobs index only if the question is about a job application."
 
-The `alwaysQuerySource` property overrides `retrievalInstructions`. You should set `alwaysQuerySource` to false when providing retrieval instructions.
+The `alwaysQuerySource` property overrides `retrievalInstructions`. Set `alwaysQuerySource` to false when providing retrieval instructions.
 
 ### Attempt fast path processing
 
@@ -94,36 +113,3 @@ To achieve the fastest possible response times, follow these best practices:
    + Set `knowledgeSources.includeReferenceSourceData` to false if you don't need the verbatim content from the index. Omitting this information simplifies the response and makes it more readable.
 
 1. In the [retrieve action](agentic-retrieval-how-to-retrieve.md), provide a single message query that's fewer than 512 characters.
-
-## Delete a knowledge source
-
-Before you can delete a knowledge source, you must delete or update any knowledge agent that references it. The associated index is a standalone object in Azure AI Search and doesn't need to be deleted or updated in tandem with the knowledge source, but no references to the knowledge source can exist if you want to delete it.
-
-If you try to delete a knowledge source that's in use, the action fails and a list of affected knowledge agents is returned.
-
-1. Get the knowledge agent definition to confirm knowledge source references.
-
-    ```http
-    ### Get the knowledge agent
-    GET {{search-endpoint}}/agents/hotels-index-ka?api-version=2025-08-01-preview
-    api-key: {{api-key}}
-    Content-Type: application/json
-    ```
-
-1. Either update the knowledge agent by removing the knowledge source, or delete the knowledge agent. This example shows deletion.
-
-    ```http
-    ### Delete knowledge agent
-    DELETE {{search-endpoint}}/agents/hotels-index-ka?api-version=2025-08-01-preview
-    api-key: {{api-key}}
-    Content-Type: application/json
-    ```
-
-1. Delete the knowledge source.
-
-    ```http
-    ### Delete a knowledge source definition
-    GET {{search-endpoint}}/knowledgeSources/hotels-index-ks?api-version=2025-08-01-preview
-    api-key: {{api-key}}
-    Content-Type: application/json
-    ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント的知識ソースの概要に関する記事の更新"
}
```

### Explanation
この変更は、`articles/search/agentic-knowledge-source-overview.md`ファイルに対する大幅な修正を示しています。主な変更点は以下の通りです。

1. **タイトルと説明の変更**: ドキュメントのタイトルが「Create a knowledge source」から「What is a knowledge source」に変更され、説明も「エージェント的な検索ワークロード用の知識ソースの作成方法」から「エージェント的な検索ワークロードで使用される知識ソースオブジェクトについて」に更新されました。これにより、文書の冒頭からより明確な情報を提供しています。

2. **内容の追加と簡略化**: ドキュメントに新たに追加されたセクションがあり、知識ソースの作成過程やその使用方法についての詳細が含まれています。一方で、一部の内容が削除または簡略化され、全体としてより洗練された構成となっています。

3. **インクルードファイルの追加**: 注意書きや関連するREST APIのリンクなどが新たに含まれ、ユーザーが必要な情報にアクセスしやすくなっています。また、知識ソースを使用するための条件（権限など）が明確に述べられています。

この変更は、利用者に対して知識ソースの概念とその使用法をより明確に理解させることを目的としており、変更の範囲は広いですが、全体としては情報の明確さと実用性が向上したと言えます。

## articles/search/includes/how-tos/knowledge-source-delete-rest.md{#item-225321}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,89 @@
+---
+manager: nitinme
+author: heidisteen
+ms.author: heidist
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 10/10/2025
+---
+
+If you no longer need the knowledge source, or if you need to rebuild it on the search service, use this request to delete the current object.
+
+Before you can delete a knowledge source, you must delete any knowledge agent that references it, or remote the references in an update action. The associated index and any indexer pipeline objects created from the knowledge source are standalone objects and don't need to be deleted or updated in tandem with the knowledge source.
+
+If you try to delete a knowledge source that's in use, the action fails and a list of affected knowledge agents is returned.
+
+1. Start by getting a list of all knowledge agents. This request returns all knowledge agents on your search service.
+
+    ```http
+    ### Get the knowledge agent
+    GET {{search-endpoint}}/agents?api-version=2025-08-01-preview&$select=name
+    api-key: {{api-key}}
+    Content-Type: application/json
+    ```
+
+   An example response might look like the following:
+
+   ```json
+    {
+        "@odata.context": "https://my-demo-search-service.search.windows.net/$metadata#agents(name)",
+        "value": [
+        {
+            "name": "earth-blob-ka"
+        },
+        {
+            "name": "hotels-sample-ka"
+        }
+        ]
+    }
+   ```
+
+1. Get the individual knowledge agent definition to check for knowledge source references.
+
+    ```http
+    GET {{search-endpoint}}/agents/hotels-sample-ka?api-version=2025-08-01-preview
+    api-key: {{api-key}}
+    Content-Type: application/json
+    ```
+
+   An example response might look like the following:
+
+   ```json
+    {
+      "name": "hotels-sample-ka",
+      "description": null,
+      "retrievalInstructions": null,
+      "knowledgeSources": [
+        {
+          "name": "hotels-sample-ks",
+          "alwaysQuerySource": false,
+          "includeReferences": true,
+          "includeReferenceSourceData": false,
+          "maxSubQueries": null,
+          "rerankerThreshold": null
+        }
+      ],
+      "models": [ trimmed for brevity ],
+      "outputConfiguration": { trimmed for brevity },
+      "requestLimits": { trimmed for brevity},
+      "encryptionKey": null
+    }
+   ```
+
+1. Either [update the knowledge agent](/rest/api/searchservice/knowledge-agents/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) by removing the knowledge source if you have multiple sources, or delete the knowledge agent. This example shows deletion.
+
+    ```http
+    ### Delete knowledge agent
+    DELETE {{search-endpoint}}/agents/hotels-sample-ka?api-version=2025-08-01-preview
+    api-key: {{api-key}}
+    Content-Type: application/json
+    ```
+
+1. Delete the knowledge source.
+
+    ```http
+    ### Delete a knowledge source definition
+    GET {{search-endpoint}}/knowledgeSources/hotels-sample-ks?api-version=2025-08-01-preview
+    api-key: {{api-key}}
+    Content-Type: application/json
+    ```
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "知識ソース削除用のREST APIガイド"
}
```

### Explanation
この変更は、新しいドキュメント`knowledge-source-delete-rest.md`の追加を示しています。このドキュメントは、知識ソースを削除するための手順とAPIリクエストについて詳しく説明しています。

1. **ドキュメントの目的**: 知識ソースを削除する方法に関するガイドラインが提供されており、利用者が知識ソースを適切に削除するための手順を理解できるようになっています。

2. **削除手順の詳細**: 
   - 知識ソースを削除する前に、その知識ソースを参照している知識エージェントを削除または更新する必要があることが明記されています。
   - 知識ソースの削除が失敗した場合には、影響を受ける知識エージェントのリストが返されることも説明されています。

3. **具体的なAPIリクエスト**: 
   - 知識エージェントのリストを取得するためのHTTP GETリクエストや、個別の知識エージェントの詳細を取得するためのリクエストが例示されています。
   - 知識エージェントを削除するための具体的なリクエストも提供されており、ユーザーはAPIを通じて容易に作業を進めることができます。

これにより、利用者はよりスムーズに知識ソースを管理できるようになり、関連する操作が体系的に整理されています。この新しい文書は、APIの使用者にとって役立つリファレンスとなるでしょう。


