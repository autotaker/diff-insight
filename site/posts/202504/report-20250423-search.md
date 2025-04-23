---
date: '2025-04-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bb349ba...MicrosoftDocs:5e44f1a
summary: このコード差分は、検索サービスに関連するドキュメントのマイナーな更新を含んでおり、主に日付情報の修正、エラーメッセージの明確化、インデックスロードや再構築プロセスの詳細な説明の追加、コード例中の文言修正が行われました。新たにHTTP
  429エラーが容量計画における重要な指標として追加され、「indexer pipelines」に関する補足情報が提供され、インデックス作成・ロードのワークフローが明確化されました。破壊的な変更はなく、全体としてドキュメントの整合性とユーザーの理解を向上させることを目的としています。これにより、システムの限界についての理解が深まり、サービスのパフォーマンス改善や障害防止に寄与します。また、小さな修正でもドキュメントの信頼性が向上し、正確な情報を提供します。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bb349ba...MicrosoftDocs:5e44f1a){target="_blank"}

<format>
# Highlights
このコード差分は、検索サービスに関連するドキュメントのいくつかのマイナーな更新を含んでいます。主要な更新点としては、それぞれの日付情報の修正、エラーメッセージの明確化、インデックスロードと再構築におけるプロセスの詳細な説明の追加、そしてコード例中の文言の微細な修正があります。

## New features
- HTTP 429エラー（リクエストが多すぎる）がストレージ不足の兆候として説明に追加され、容量計画における重要ポイントが増えた。
- 「indexer pipelines」に関する補足情報が追加され、インデックス作成・ロードのワークフローが明確化された。

## Breaking changes
- 特に破壊的な変更はありません。

## Other updates
- 各ドキュメントの日付情報が更新され、最新情報に揃えられた。
- エラーメッセージに関する説明が詳細化され、「429 Too Many Requests」エラーが発生するシナリオが具体的に示された。
- コード例の文字列が公式な用語に修正された。

# Insights
今回の更新は、Azure Searchサービスに関連するドキュメントの整合性を改善し、ユーザーの理解を深めることを目的としています。特に、容量計画やデータインポートにおける具体的なエラー管理方法の追加は、ユーザーが予期せぬ障害を避けるための有用な指針となります。

HTTP 429エラーを容量計画の重要情報として追加することで、ユーザーはシステムの限界を理解しやすくなり、結果としてサービスの持続的なパフォーマンス改善や障害防止に貢献できます。また、「indexer pipelines」についての補足情報は、インデックス作成とロードの基本的な概念から具体的な実践方法へとガイドする助けとなります。

さらに、コード例中の小さな訂正でさえ、ドキュメントの信頼性を高め、読者に正確な情報を提供します。これらの更新は一貫性と正確性を追求する姿勢を反映しており、ユーザーが最新の知識を得やすいように配慮されています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-capacity-planning.md](#item-0dd6c9) | minor update | 検索サービスの容量計画に関するドキュメントの更新 | modified | 3 | 2 | 5 | 
| [search-how-to-load-search-index.md](#item-a72573) | minor update | 検索インデックスのロードに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [search-howto-reindex.md](#item-46738a) | minor update | インデックスの再構築に関するドキュメントの更新 | modified | 9 | 4 | 13 | 
| [vector-search-how-to-generate-embeddings.md](#item-e98f7b) | minor update | 埋め込み生成に関するコード例の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-capacity-planning.md{#item-0dd6c9}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: conceptual
-ms.date: 04/10/2025
+ms.date: 04/22/2025
 ---
 
 # Estimate and manage capacity of a search service
@@ -53,7 +53,8 @@ A single service must have sufficient resources to handle all workloads (indexin
 Guidelines for determining whether to add capacity include:
 
 + Meeting the high availability criteria for service-level agreement.
-+ The frequency of HTTP 503 errors is increasing.
++ The frequency of HTTP 503 (Service unavailable) errors is increasing.
++ The frequency of HTTP 429 (Too many requests) errors is increasing, an indication of low storage.
 + Large query volumes are expected.
 + A [one-time upgrade](#how-to-upgrade-capacity) to newer infrastructure and larger partitions isn’t sufficient.
 + The current number of partitions isn’t adequate for indexing workloads.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスの容量計画に関するドキュメントの更新"
}
```

### Explanation
この変更は、`search-capacity-planning.md` ドキュメントに関する小規模な更新です。具体的には、いくつかの項目が修正され、日付情報が更新されました。まず、文中の日付が2025年4月10日から2025年4月22日に変更されています。また、サーバーの稼働状況の基準やエラーメッセージに関する内容も明確化されています。HTTP 503エラーについては「サービス利用不可」として具体的に説明され、新たにHTTP 429エラー（リクエストが多すぎる）についても言及され、ストレージ不足の兆候としての重要性が追加されています。これにより、容量計画のガイドラインがより明確かつ正確になっています。

## articles/search/search-how-to-load-search-index.md{#item-a72573}

<details>
<summary>Diff</summary>
````diff
@@ -9,12 +9,12 @@ ms.author: heidist
 
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 04/14/2025
+ms.date: 04/22/2025
 ---
 
 # Load data into a search index in Azure AI Search
 
-This article explains how to import documents into a predefined search index. In Azure AI Search, a [search index is created first](search-how-to-create-search-index.md) with [data import](search-what-is-data-import.md) following as a second step. The exception is [Import wizards](search-import-data-portal.md) in the Azure portal and indexer pipelines, which create and load an index in one workflow.
+This article explains how to import documents into a predefined search index. In Azure AI Search, a [search index is created first](search-how-to-create-search-index.md) with [data import](search-what-is-data-import.md) following as a second step. The exception is [Import wizards](search-import-data-portal.md) in the Azure portal and [indexer pipelines](search-indexer-overview.md), which create and load an index in one workflow.
 
 ## How data import works
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスのロードに関するドキュメントの更新"
}
```

### Explanation
この変更は、`search-how-to-load-search-index.md` ドキュメントの小規模な更新を示しています。主に、文中の日付が2025年4月14日から2025年4月22日に変更されました。また、Azure AI Searchでのデータインポートに関する説明がわずかに修正され、インポートウィザードとインデクサーパイプラインの関連情報が補足されています。具体的には、インポートウィザードに加えて「indexer pipelines」への言及が追加され、インデックスを1つのワークフローで作成およびロードする処理がより明確に示されています。この変更により、ドキュメントは最新の情報を反映し、ユーザーにとっての理解を深めることを目的としています。

## articles/search/search-howto-reindex.md{#item-46738a}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 03/21/2025
+ms.date: 04/22/2025
 ---
 
 # Update or rebuild an index in Azure AI Search
@@ -24,17 +24,21 @@ For schema changes on applications already in production, we recommend creating
 
 ## Update content
 
-Incremental indexing and synchronizing an index against changes in source data is fundamental to most search applications. This section explains the workflow for updating field contents in a search index through the REST API, but the Azure SDKs provide equivalent functionality.
+Incremental indexing and synchronizing an index against changes in source data is fundamental to most search applications. This section explains the workflow for adding, removing, or overwriting the content of a search index through the REST API, but the Azure SDKs provide equivalent functionality.
 
-The body of the request contains one or more documents to be indexed. Documents are identified by a unique case-sensitive key. Each document is associated with an action: "upload", "delete", "merge", or "mergeOrUpload". Upload requests must include the document data as a set of key/value pairs.
+The body of the request contains one or more documents to be indexed. Within the request, each document in the index is:
+
++ Identified by a unique case-sensitive key.
++ Associated with an action: "upload", "delete", "merge", or "mergeOrUpload". 
++ Populated with a set of name/value pairs for each field that you're adding or updating.
 
 ```json
 {  
   "value": [  
     {  
       "@search.action": "upload (default) | merge | mergeOrUpload | delete",  
       "key_field_name": "unique_key_of_document", (key/value pair for key field from index schema)  
-      "field_name": field_value (key/value pairs matching index schema)  
+      "field_name": field_value (name/value pairs matching index schema)  
         ...  
     },  
     ...  
@@ -130,6 +134,7 @@ The following table explains the various per-document status codes that can be r
 | 404 | The document couldn't be merged because the given key doesn't exist in the index. | No | This error doesn't occur for uploads since they create new documents, and it doesn't occur for deletes because they're idempotent. |
 | 409 | A version conflict was detected when attempting to index a document.| Yes | This can happen when you're trying to index the same document more than once concurrently. |
 | 422 | The index is temporarily unavailable because it was updated with the 'allowIndexDowntime' flag set to 'true'. | Yes | |
+|429 | Too Many Requests | Yes | If you get this error code during indexing, it usually means that you're running low on storage. As you near [storage limits](search-limits-quotas-capacity.md), the service can enter a state where you can't add or update until you delete some documents. For more information, see [Plan and manage capacity](search-capacity-planning.md#how-to-upgrade-capacity) if you want more storage, or free up space by deleting documents. |  
 | 503 | Your search service is temporarily unavailable, possibly due to heavy load. | Yes | Your code should wait before retrying in this case or you risk prolonging the service unavailability.|
 
 If your client code frequently encounters a 207 response, one possible reason is that the system is under load. You can confirm this by checking the statusCode property for 503. If the statusCode is 503, we recommend throttling indexing requests. Otherwise, if indexing traffic doesn't subside, the system could start rejecting all requests with 503 errors.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスの再構築に関するドキュメントの更新"
}
```

### Explanation
この変更は、`search-howto-reindex.md` ドキュメントの小規模な更新を示しています。日付が2025年3月21日から2025年4月22日に変更されたほか、コンテンツの更新に関するセクションに幾つかの明確化が加えられています。特に、REST APIを通じて検索インデックスの内容を追加、削除、または上書きするためのワークフローがより詳しく説明されています。各ドキュメントがユニークなキーで識別され、アクション（"upload"、"delete"、"merge"、"mergeOrUpload"）と共に関連付けられることが強調されています。

さらに、ドキュメントのリクエスト本体に含まれる情報が詳述され、各フィールドの追加や更新を行うためのキー/バリューのペアに対する説明が改善されています。最後に、エラーメッセージも増え、特に「429 Too Many Requests」エラーの発生源となるストレージ不足の状況や、ストレージ計画管理に関する詳細な指示が追加されています。この更新により、ユーザーにとって利便性が向上し、APIとのインタラクションにおける明確さが増しています。

## articles/search/vector-search-how-to-generate-embeddings.md{#item-e98f7b}

<details>
<summary>Diff</summary>
````diff
@@ -53,7 +53,7 @@ openai.api_base = "https://YOUR-OPENAI-RESOURCE.openai.azure.com"
 openai.api_version = "2024-02-01"
 
 response = openai.Embedding.create(
-    input="How do I use Python in VSCode?",
+    input="How do I use Python in VS Code?",
     engine="text-embedding-ada-002"
 )
 embeddings = response['data'][0]['embedding']
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "埋め込み生成に関するコード例の修正"
}
```

### Explanation
この変更は、`vector-search-how-to-generate-embeddings.md` ドキュメント内のコード例に対する小規模な更新を示しています。具体的には、コード中の文字列 `"How do I use Python in VSCode?"` が `"How do I use Python in VS Code?"` に修正されています。この修正により、「VSCode」という表記がより一般的な「VS Code」に変更され、公式な名称に揃えられています。その他の部分には変更はなく、全体の内容はそのままとなっています。この微調整は、ユーザーにとっての理解を高め、正確な情報を提供するために重要です。


