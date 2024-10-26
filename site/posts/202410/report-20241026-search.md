---
date: '2024-10-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:edd8070...MicrosoftDocs:0bc728f
summary: この変更には、複数のドキュメントファイルにおける軽微な修正が含まれています。主な内容としては、リンクテキストや日付の更新、説明の明確化が行われており、特にAzure関連のサービスの名称変更やリンクの修正が挙げられます。新機能として「executionEnvironment」パラメーターの説明が追加され、マルチテナント環境に関する説明も強化されました。特に重要な破壊的変更は見られませんが、Azureサービスの名称が一部変更されているため、従来のドキュメントとの差異に注意が必要です。全体的に、ユーザーエクスペリエンスの向上や情報の正確性を目的とした改善が行われています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:edd8070...MicrosoftDocs:0bc728f){target="_blank"}

<format>
# Highlights
この変更には、複数のドキュメントファイルにおける軽微な修正が含まれており、特にリンクテキスト、日付の更新、および説明の明確化が行われています。主なハイライトとしては、Azure関連のサービスにおける名称変更やリンクの修正が挙げられます。また、各種インデクサーの使用方法や設定内容が明示され、ユーザーの利便性が向上しています。その他の注意点としては、リソースIDやサンプルコードが更新され正確性が向上しています。

## New features
- 「executionEnvironment」パラメーターの説明が追加されました。
- マルチテナント環境に関する説明が強化され、5分間隔でインデクサーを再起動する推奨事項が追加されました。

## Breaking changes
- 特に重要な破壊的変更は見られませんが、Azureサービスの名称が一部で変更されており、これによって従来のドキュメントから名前が変わった点には注意が必要です。

## Other updates
- Azure AI StudioやAzure OpenAIといった関連サービスの名称が一貫性をもって修正されています。
- ベクター検索関連の圧縮ストレージ設定に関する具体的な情報が追加されました。
- インデクサーに関連した日付や表現が統一され、最近の日付に更新されました。

# Insights
このドキュメント変更は、主にユーザーエクスペリエンスの向上と情報の正確性を目的とした小規模な修正です。リンクや日付、表現の一貫性を保つことで、ドキュメント全体の整合性が確保されています。特にAzure AI Searchとその関連サービスにおいて名称やリンクが統一されているため、利用者はどのサービスを使用するべきかを混乱せずに理解できます。

また、このアップデートは、利用者がAzure AI Searchの機能を効率的に活用できるよう、技術的な詳細が明確化されています。インデクサーの設定手順や、具体的な手法が詳細に示されているため、実装や運用時の手順が明示され、サービスの理解が深まります。ユーザーに提供する情報は最新の状態に保たれ、実用性も向上しています。これらの改善は、特に新規ユーザーや既存ユーザーがAzureの進化するエコシステムを効率的に利用する上での助けになるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index.yml](#item-c67121) | minor update | 検索ページのリンクテキストの更新 | modified | 1 | 1 | 2 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | リンクテキストとサービス名の修正 | modified | 2 | 2 | 4 | 
| [search-how-to-create-indexers.md](#item-de71fb) | minor update | Indexer作成に関する情報の更新 | modified | 8 | 3 | 11 | 
| [search-how-to-index-onelake-files.md](#item-95f3db) | minor update | OneLakeファイルのインデックス作成に関する接続文字列の更新 | modified | 2 | 2 | 4 | 
| [search-how-to-large-index.md](#item-d34e42) | minor update | 大規模インデックス作成に関するドキュメントのリネームと内容の更新 | renamed | 32 | 32 | 64 | 
| [search-howto-run-reset-indexers.md](#item-fb10c8) | minor update | インデクサーの実行とリセットに関するドキュメントの更新 | modified | 10 | 7 | 17 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | プライベートインデクサーアクセス文書の修正 | modified | 4 | 4 | 8 | 
| [search-indexer-securing-resources.md](#item-c075c4) | minor update | インデクサーのリソース保護に関する文書の更新 | modified | 7 | 4 | 11 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索サービスの制限とクォータに関するドキュメントの更新 | modified | 36 | 38 | 74 | 
| [search-manage-powershell.md](#item-3c3485) | minor update | PowerShell 管理ドキュメントのリソース ID 更新 | modified | 1 | 1 | 2 | 
| [search-query-lucene-examples.md](#item-ce3624) | minor update | Lucene クエリ構文の例に関するドキュメントの更新 | modified | 32 | 33 | 65 | 
| [search-query-simple-examples.md](#item-834766) | minor update | 単純検索構文の例に関するドキュメントの更新 | modified | 44 | 44 | 88 | 
| [search-security-get-encryption-keys.md](#item-7aed9d) | minor update | 暗号化キー取得に関するドキュメントの小変更 | modified | 1 | 1 | 2 | 
| [search-sku-tier.md](#item-7686b8) | minor update | SKUティアに関するドキュメントの更新 | modified | 4 | 3 | 7 | 
| [search-try-for-free.md](#item-36e28d) | minor update | Azure AI Searchを試すためのドキュメントの修正 | modified | 2 | 2 | 4 | 
| [service-configure-firewall.md](#item-75be3f) | minor update | ファイアウォール構成に関するドキュメントの修正 | modified | 1 | 1 | 2 | 
| [service-create-private-endpoint.md](#item-65e817) | minor update | プライベートエンドポイントの作成に関するドキュメントの修正 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c4768f) | minor update | TOCファイルの修正 | modified | 1 | 1 | 2 | 
| [tutorial-rag-build-solution-models.md](#item-6796c9) | minor update | RAGチュートリアルの更新 | modified | 3 | 4 | 7 | 
| [vector-search-how-to-configure-compression-storage.md](#item-c653c3) | minor update | ベクター検索の圧縮ストレージ設定に関する記事の更新 | modified | 17 | 18 | 35 | 
| [vector-search-integrated-vectorization.md](#item-48219d) | minor update | 統合ベクター化に関する記事の微修正 | modified | 1 | 1 | 2 | 
| [vector-search-overview.md](#item-56e5fa) | minor update | ベクター検索の概要に関する記事の更新 | modified | 2 | 2 | 4 | 
| [vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md](#item-ebe7a3) | minor update | Azure Machine Learning AI Studioカタログのベクタイザーに関する記事の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/index.yml{#item-c67121}

<details>
<summary>Diff</summary>
````diff
@@ -68,7 +68,7 @@ landingContent:
         links:
           - text: Create a vector index in AI Studio
             url: /azure/ai-studio/how-to/index-add
-          - text: Chat with your data in Azure OpenAI Studio
+          - text: Chat with your data using Azure OpenAI
             url: /azure/ai-services/openai/use-your-data-quickstart
           - text: Build a question and answer copilot
             url: /azure/ai-studio/tutorials/deploy-copilot-ai-studio
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索ページのリンクテキストの更新"
}
```

### Explanation
この変更は、`articles/search/index.yml`ファイルにおけるリンクテキストの軽微な修正を含んでいます。具体的には、テキスト「Chat with your data in Azure OpenAI Studio」が「Chat with your data using Azure OpenAI」に変更されました。この修正は、ユーザーにとっての理解を深め、より明確な情報を提供することを目的としており、内容へのアクセスが改善されます。ファイルの他の部分はそのまま残されており、全体的な構成や機能には影響を与えていません。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ Azure AI Search is a [proven solution for information retrieval](/azure/develope
 Microsoft has several built-in implementations for using Azure AI Search in a RAG solution.
 
 + Azure AI Studio, [use a vector index and retrieval augmentation](/azure/ai-studio/concepts/retrieval-augmented-generation). 
-+ Azure OpenAI Studio, [use a search index with or without vectors](/azure/ai-services/openai/concepts/use-your-data).
++ Azure OpenAI, [use a search index with or without vectors](/azure/ai-services/openai/concepts/use-your-data).
 + Azure Machine Learning, [use a search index as a vector store in a prompt flow](/azure/machine-learning/how-to-create-vector-index).
 
 Curated approaches make it simple to get started, but for more control over the architecture, you need a custom solution. These templates create end-to-end solutions in:
@@ -77,7 +77,7 @@ The information retrieval system provides the searchable index, query logic, and
 
 The LLM receives the original prompt, plus the results from Azure AI Search. The LLM analyzes the results and formulates a response. If the LLM is ChatGPT, the user interaction might be a back and forth conversation. If you're using Davinci, the prompt might be a fully composed answer. An Azure solution most likely uses Azure OpenAI, but there's no hard dependency on this specific service.
 
-Azure AI Search doesn't provide native LLM integration for prompt flows or chat preservation, so you need to write code that handles orchestration and state. You can review demo source ([Azure-Samples/azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo)) for a blueprint of what a full solution entails. We also recommend Azure AI Studio or [Azure OpenAI Studio](/azure/ai-services/openai/use-your-data-quickstart) to create RAG-based Azure AI Search solutions that integrate with LLMs.
+Azure AI Search doesn't provide native LLM integration for prompt flows or chat preservation, so you need to write code that handles orchestration and state. You can review demo source ([Azure-Samples/azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo)) for a blueprint of what a full solution entails. We also recommend [Azure AI Studio](/azure/ai-studio/concepts/retrieval-augmented-generation) to create RAG-based Azure AI Search solutions that integrate with LLMs.
 
 ## Searchable content in Azure AI Search
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクテキストとサービス名の修正"
}
```

### Explanation
この変更は、`articles/search/retrieval-augmented-generation-overview.md`ファイルにおけるいくつかのリンクテキストとサービス名の修正を含んでいます。具体的には、「Azure OpenAI Studio」という文言が「Azure OpenAI」に修正され、関連するリンクテキストも更新されています。また、新たに「Azure AI Studio」が追加され、その使用に関する説明が明確にされています。これにより、ユーザーはそれぞれのサービスについての最新情報を得やすくなり、RAGソリューションとの統合が促進されます。全体として、これらの変更は内容の正確性と関連性を向上させることを目的としています。

## articles/search/search-how-to-create-indexers.md{#item-de71fb}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 10/10/2024
+ms.date: 10/24/2024
 ---
 
 # Create an indexer in Azure AI Search
@@ -177,7 +177,7 @@ When you're ready to create an indexer on a remote search service, you need a se
 
 ### [**REST**](#tab/indexer-rest)
 
-Visual Studio Code with a REST client can send indexer requests. Using the app, you can connect to your search service and send [Create indexer (REST)](/rest/api/searchservice/indexers/create) or [Update indexer](/rest/api/searchservice/indexers/create-or-update) requests. 
+Visual Studio Code with a REST client can send indexer requests. Using the app, you can connect to your search service and send [Create indexer (REST)](/rest/api/searchservice/indexers/create) or [Create or Update indexer](/rest/api/searchservice/indexers/create-or-update) requests. 
 
 ```http
 POST /indexers?api-version=[api-version]
@@ -188,12 +188,17 @@ POST /indexers?api-version=[api-version]
   "parameters": {
     "batchSize": null,
     "maxFailedItems": null,
-    "maxFailedItemsPerBatch": null
+    "maxFailedItemsPerBatch": null,
+    "configuration": {
+        "executionEnvironment": "standard"
+    }
   },
   "fieldMappings": [ optional unless there are field discrepancies that need resolution]
 }
 ```
 
+Parameters are used to set the batch size and how to handle processing failures. The [execution environment](search-howto-run-reset-indexers.md#indexer-execution) determines whether indexer and skillset processing can use the multitenant capabilities provided by Microsoft or the private processing nodes allocated exclusively to your search service. If your search service is Standard2 or higher, you can set `executionEnvironment` to private to pin all indexer processing to just your search service clusters.
+
 There are numerous tutorials and examples that demonstrate REST clients for creating objects. [Quickstart: Text search using REST](search-get-started-rest.md) can get you started.
 
 ### [**.NET SDK**](#tab/indexer-csharp)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Indexer作成に関する情報の更新"
}
```

### Explanation
この変更は、`articles/search/search-how-to-create-indexers.md`ファイルに対する軽微な更新を含んでいます。主なポイントとして、文書の日付が「10/10/2024」から「10/24/2024」に変更され、REST APIにおける「Create indexer」リクエストの表現が「Create indexer (REST)」から「Create or Update indexer」に修正されました。また、新しい「executionEnvironment」パラメーターの説明が追加され、これによりユーザーはインデクサー処理の環境設定に関する情報を得ることができます。最後に、RESTクライアントを使用してオブジェクトを作成するためのチュートリアルや例のリンクも付加されています。これらの変更は、ドキュメントの明確性と有用性を向上させることを目的としています。

## articles/search/search-how-to-index-onelake-files.md{#item-95f3db}

<details>
<summary>Diff</summary>
````diff
@@ -222,7 +222,7 @@ A data source is defined as an independent resource so that it can be used by mu
       "description": "description",  
       "type": "onelake",  
       "credentials": {  
-        "connectionString": "ResourceId=00000000-0000-0000-0000-000000000000"  
+        "connectionString": "ResourceId=a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1"  
       },  
       "container": {  
         "name": "11111111-1111-1111-1111-111111111111",  
@@ -260,7 +260,7 @@ A data source is defined as an independent resource so that it can be used by mu
       "description": "description",  
       "type": "onelake",  
       "credentials": {  
-        "connectionString": "ResourceId=00000000-0000-0000-0000-000000000000"  
+        "connectionString": "ResourceId=a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1"  
       },  
       "container": {  
         "name": "11111111-1111-1111-1111-111111111111",  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLakeファイルのインデックス作成に関する接続文字列の更新"
}
```

### Explanation
この変更は、`articles/search/search-how-to-index-onelake-files.md`ファイルにおける接続文字列の更新を反映しています。具体的には、元の接続文字列「ResourceId=00000000-0000-0000-0000-000000000000」が「ResourceId=a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1」に変更されています。この変更は、OneLakeファイルのインデックス作成を行う際に使用されるデータソースの接続情報を正確に示すためのものであり、利用者にとっての可用性と正確性を向上させることを目指しています。全体として、これらの変更は、OneLakeに関連するインデックス作成手順の文書を最新の状態に保つ努力の一環です。

## articles/search/search-how-to-large-index.md{#item-d34e42}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Index large data sets for full text search
 titleSuffix: Azure AI Search
-description: Strategies for large data indexing or computationally intensive indexing through batch mode, resourcing, and scheduled, parallel, and distributed indexing.
+description: Learn about strategies for large data indexing or computationally intensive indexing through batch mode, resourcing, and scheduled, parallel, and distributed indexing.
 
 manager: nitinme
 author: HeidiSteen
@@ -10,14 +10,14 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 04/01/2024
+ms.date: 10/24/2024
 ---
 
 # Index large data sets in Azure AI Search
 
-If your search solution requirements include indexing big data or complex data, this article articulates strategies for accommodating long running processes on Azure AI Search.
+If you need to index large or complex data sets in your search solution, this article explores strategies to accommodate long-running processes on Azure AI Search.
 
-This article assumes familiarity with the [two basic approaches for importing data](search-what-is-data-import.md): pushing data into an index, or pulling in data from a supported data source using a [search indexer](search-indexer-overview.md). If your scenario involves computationally intensive [AI enrichment](cognitive-search-concept-intro.md), then indexers are required, given the skillset dependency on indexers.
+These strategies assume familiarity with the [two basic approaches for importing data](search-what-is-data-import.md): *pushing* data into an index, or *pulling* in data from a supported data source using a [search indexer](search-indexer-overview.md). If your scenario involves computationally intensive [AI enrichment](cognitive-search-concept-intro.md), then indexers are required, given the skillset dependency on indexers.
 
 This article complements [Tips for better performance](search-performance-tips.md), which offers best practices on index and query design. A well-designed index that includes only the fields and attributes you need is an important prerequisite for large-scale indexing.
 
@@ -26,47 +26,47 @@ We recommend using a newer search service, created after April 3, 2024, for [hig
 > [!NOTE]
 > The strategies described in this article assume a single large data source. If your solution requires indexing from multiple data sources, see [Index multiple data sources in Azure AI Search](/samples/azure-samples/azure-search-dotnet-scale/multiple-data-sources/) for a recommended approach.
 
-## Index large data using the push APIs
+## Index data using the push APIs
 
-"Push" APIs, such as [Documents Index REST API](/rest/api/searchservice/documents) or the [IndexDocuments method (Azure SDK for .NET)](/dotnet/api/azure.search.documents.searchclient.indexdocuments), are the most prevalent form of indexing in Azure AI Search. For solutions that use a push API, the strategy for long-running indexing will have one or both of the following components:
+*Push* APIs, such as the [Documents Index REST API](/rest/api/searchservice/documents) or the [IndexDocuments method (Azure SDK for .NET)](/dotnet/api/azure.search.documents.searchclient.indexdocuments), are the most prevalent form of indexing in Azure AI Search. For solutions that use a push API, the strategy for long-running indexing has one or both of the following components:
 
 + Batching documents
 + Managing threads
 
 ### Batch multiple documents per request
 
-A simple mechanism for indexing a large quantity of data is to submit multiple documents or records in a single request. As long as the entire payload is under 16 MB, a request can handle up to 1000 documents in a bulk upload operation. These limits apply whether you're using the [Documents Index REST API](/rest/api/searchservice/documents) or the [IndexDocuments method](/dotnet/api/azure.search.documents.searchclient.indexdocuments) in the .NET SDK. For either API, you would package 1000 documents in the body of each request.
+A simple mechanism for indexing a large quantity of data is to submit multiple documents or records in a single request. As long as the entire payload is under 16 MB, a request can handle up to 1,000 documents in a bulk upload operation. These limits apply whether you're using the [Documents Index REST API](/rest/api/searchservice/documents) or the [IndexDocuments method](/dotnet/api/azure.search.documents.searchclient.indexdocuments) in the .NET SDK. Using either API, you can package 1,000 documents in the body of each request.
 
-Batching documents will significantly shorten the amount of time it takes to work through a large data volume. Determining the optimal batch size for your data is a key component of optimizing indexing speeds. The two primary factors influencing the optimal batch size are:
+Batching documents significantly shortens the amount of time it takes to work through a large data volume. Determining the optimal batch size for your data is a key component of optimizing indexing speeds. The two primary factors influencing the optimal batch size are:
 
 + The schema of your index
 + The size of your data
 
-Because the optimal batch size depends on your index and your data, the best approach is to test different batch sizes to determine which one results in the fastest indexing speeds for your scenario. [Tutorial: Optimize indexing with the push API](tutorial-optimize-indexing-push-api.md) provides sample code for testing batch sizes using the .NET SDK.
+Because the optimal batch size depends on your index and your data, the best approach is to test different batch sizes to determine which one results in the fastest indexing speeds for your scenario. For sample code to test batch sizes using the .NET SDK, see [Tutorial: Optimize indexing with the push API](tutorial-optimize-indexing-push-api.md).
 
-### Add threads and a retry strategy
+### Manage threads and a retry strategy
 
-Indexers have built-in thread management, but when you're using the push APIs, your application code will have to manage threads. Make sure there are sufficient threads to make full use of the available capacity, especially if you've recently increased partitions or have upgraded to a higher tier search service. 
+Indexers have built-in thread management, but when you're using the push APIs, your application code needs to manage threads. Make sure there are sufficient threads to make full use of the available capacity, especially if you've recently increased partitions or upgraded to a higher tier search service. 
 
 1. [Increase the number of concurrent threads](tutorial-optimize-indexing-push-api.md#use-multiple-threadsworkers) in your client code.
 
 1. As you ramp up the requests hitting the search service, you might encounter [HTTP status codes](/rest/api/searchservice/http-status-codes) indicating the request didn't fully succeed. During indexing, two common HTTP status codes are:
 
-   + **503 Service Unavailable** - This error means that the system is under heavy load and your request can't be processed at this time.
+   + **503 Service Unavailable**: This error means that the system is under heavy load and your request can't be processed at this time.
 
-   + **207 Multi-Status** - This error means that some documents succeeded, but at least one failed.
+   + **207 Multi-Status**: This error means that some documents succeeded, but at least one failed.
 
 1. To handle failures, requests should be retried using an [exponential backoff retry strategy](/dotnet/architecture/microservices/implement-resilient-applications/implement-retries-exponential-backoff).
 
-The Azure .NET SDK automatically retries 503s and other failed requests, but you'll need to implement your own logic to retry 207s. Open-source tools such as [Polly](https://github.com/App-vNext/Polly) can also be used to implement a retry strategy.
+The Azure .NET SDK automatically retries 503s and other failed requests, but you need to implement your own logic to retry 207s. Open-source tools such as [Polly](https://github.com/App-vNext/Polly) can also be used to implement a retry strategy.
 
-## Index with indexers and the "pull" APIs
+## Use indexers and the pull APIs
 
 [Indexers](search-indexer-overview.md) have several capabilities that are useful for long-running processes:
 
 + Batching documents
 + Parallel indexing over partitioned data
-+ Scheduling and change detection for indexing just new and change documents over time
++ Scheduling and change detection for indexing only new and changed documents over time
 
 Indexer schedules can resume processing at the last known stopping point. If data isn't fully indexed within the processing window, the indexer picks up wherever it left off on the next run, assuming you're using a data source that provides change detection.
 
@@ -76,13 +76,13 @@ Partitioning data into smaller individual data sources enables parallel processi
 
 As with the push API, indexers allow you to configure the number of items per batch. For indexers based on the [Create Indexer REST API](/rest/api/searchservice/indexers/create), you can set the `batchSize` argument to customize this setting to better match the characteristics of your data. 
 
-Default batch sizes are data source specific. Azure SQL Database and Azure Cosmos DB have a default batch size of 1000. In contrast, Azure Blob indexing sets batch size at 10 documents in recognition of the larger average document size. 
+Default batch sizes are data-source specific. Azure SQL Database and Azure Cosmos DB have a default batch size of 1,000. In contrast, Azure Blob indexing sets batch size at 10 documents in recognition of the larger average document size. 
 
 ### Schedule indexers for long-running processes
 
 Indexer scheduling is an important mechanism for processing large data sets and for accommodating slow-running processes like image analysis in an enrichment pipeline. 
 
-Typically, indexer processing runs within a 2-hour window. If the indexing workload takes days rather than hours to complete, you can put the indexer on a consecutive, recurring schedule that starts every two hours. Assuming the data source has [change tracking enabled](search-howto-create-indexers.md#change-detection-and-internal-state), the indexer will resume processing where it last left off. At this cadence, an indexer can work its way through a document backlog over a series of days until all unprocessed documents are processed. 
+Typically, indexer processing runs within a two-hour window. If the indexing workload takes days rather than hours to complete, you can put the indexer on a consecutive, recurring schedule that starts every two hours. Assuming the data source has [change tracking enabled](search-howto-create-indexers.md#change-detection-and-internal-state), the indexer resumes processing where it last left off. At this cadence, an indexer can work its way through a document backlog over a series of days until all unprocessed documents are processed. 
 
 ```json
 {
@@ -92,12 +92,12 @@ Typically, indexer processing runs within a 2-hour window. If the indexing workl
 }
 ```
 
-When there are no longer any new or updated documents in the data source, indexer execution history will report `0/0` documents processed, and no processing occurs.
+When there are no longer any new or updated documents in the data source, indexer execution history reports `0/0` documents processed, and no processing occurs.
 
-For more information about setting schedules, see [Create Indexer REST API](/rest/api/searchservice/indexers/create) or see [How to schedule indexers for Azure AI Search](search-howto-schedule-indexers.md).
+For more information about setting schedules, see [Create Indexer REST API](/rest/api/searchservice/indexers/create) or see [Schedule indexers for Azure AI Search](search-howto-schedule-indexers.md).
 
 > [!NOTE]
-> Some indexers that run on an older runtime architecture have a 24-hour rather than 2-hour maximum processing window. The 2-hour limit is for newer content processors that run in an [internally managed multi-tenant environment](search-indexer-securing-resources.md#indexer-execution-environment). Whenever possible, Azure AI Search tries to offload indexer and skillset processing to the multi-tenant environment. If the indexer can't be migrated, it will run in the private environment and it can run for as long as 24 hours. If you're scheduling an indexer that exhibits these characteristics, assume a 24 hour processing window.
+> Some indexers that run on an older runtime architecture have a 24-hour rather than 2-hour maximum processing window. The two-hour limit is for newer content processors that run in an [internally managed multi-tenant environment](search-indexer-securing-resources.md#indexer-execution-environment). Whenever possible, Azure AI Search tries to offload indexer and skillset processing to the multi-tenant environment. If the indexer can't be migrated, it runs in the private environment and it can run for as long as 24 hours. If you're scheduling an indexer that exhibits these characteristics, assume a 24-hour processing window.
 
 <a name="parallel-indexing"></a>
 
@@ -109,9 +109,9 @@ Make sure you have sufficient capacity. One search unit in your service can run
 
 The number of indexing jobs that can run simultaneously varies for text-based and skills-based indexing. For more information, see [Indexer execution](search-howto-run-reset-indexers.md#indexer-execution).
 
-If your data source is an [Azure Blob Storage container](/azure/storage/blobs/storage-blobs-introduction#containers) or [Azure Data Lake Storage Gen 2](/azure/storage/blobs/storage-blobs-introduction#about-azure-data-lake-storage-gen2), enumerating a large number of blobs can take a long time (even hours) until this operation is completed. This will cause that your indexer's documents succeeded count isn't increased during that time and it may seem it's not making any progress, when it is. If you would like document processing to go faster for a large number of blobs, consider partitioning your data into multiple containers and create parallel indexers pointing to a single index.
+If your data source is an [Azure Blob Storage container](/azure/storage/blobs/storage-blobs-introduction#containers) or [Azure Data Lake Storage Gen 2](/azure/storage/blobs/storage-blobs-introduction#about-azure-data-lake-storage-gen2), enumerating a large number of blobs can take a long time (even hours) until this operation is completed. As a result, your indexer's *documents succeeded* count doesn't appear to increase during that time and it might seem it's not making any progress, when it is. If you would like document processing to go faster for a large number of blobs, consider partitioning your data into multiple containers and create parallel indexers pointing to a single index.
 
-1. Sign in to the [Azure portal](https://portal.azure.com) and check the number of search units used by your search service. Select **Settings** > **Scale** to view the number at the top of the page. The number of indexers that will run in parallel is approximately equal to the number of search units. 
+1. Sign in to the [Azure portal](https://portal.azure.com) and check the number of search units used by your search service. Select **Settings** > **Scale** to view the number at the top of the page. The number of indexers that run in parallel is approximately equal to the number of search units. 
 
 1. Partition source data among multiple containers or multiple virtual folders inside the same container.
 
@@ -123,21 +123,21 @@ If your data source is an [Azure Blob Storage container](/azure/storage/blobs/st
 
 1. Review indexer status and execution history for confirmation.
 
-There are some risks associated with parallel indexing. First, recall that indexing doesn't run in the background, increasing the likelihood that queries will be throttled or dropped. 
+There are some risks associated with parallel indexing. First, recall that indexing doesn't run in the background, increasing the likelihood that queries are throttled or dropped. 
 
 Second, Azure AI Search doesn't lock the index for updates. Concurrent writes are managed, invoking a retry if a particular write doesn't succeed on first attempt, but you might notice an increase in indexing failures.
 
-Although multiple indexer-data-source sets can target the same index, be careful of indexer runs that can overwrite existing values in the index. If a second indexer-data-source targets the same documents and fields, any values from the first run will be overwritten. Field values are replaced in full; an indexer can't merge values from multiple runs into the same field.
+Although multiple indexer-data-source sets can target the same index, be careful of indexer runs that can overwrite existing values in the index. If a second indexer-data-source targets the same documents and fields, any values from the first run are overwritten. Field values are replaced in full; an indexer can't merge values from multiple runs into the same field.
 
 ## Index big data on Spark
 
 If you have a big data architecture and your data is on a Spark cluster, we recommend [SynapseML for loading and indexing data](search-synapseml-cognitive-services.md). The tutorial includes steps for calling Azure AI services for AI enrichment, but you can also use the AzureSearchWriter API for text indexing.
 
-## See also
+## Related content
 
-+ [Tutorial: Optimize indexing workloads](tutorial-optimize-indexing-push-api.md)
-+ [Tutorial: Index at scale using SynapseML and Apache Spark](search-synapseml-cognitive-services.md)
-+ [Tips for improving performance](search-performance-tips.md)
-+ [Performance analysis](search-performance-analysis.md)
-+ [Indexer overview](search-indexer-overview.md)
-+ [Monitor indexer status](search-howto-monitor-indexers.md)
++ [Tutorial: Optimize indexing by using the push API](tutorial-optimize-indexing-push-api.md)
++ [Tutorial: Index large data from Apache Spark using SynapseML and Azure AI Search](search-synapseml-cognitive-services.md)
++ [Tips for better performance in Azure AI Search](search-performance-tips.md)
++ [Analyze performance in Azure AI Search](search-performance-analysis.md)
++ [Indexers in Azure AI Search](search-indexer-overview.md)
++ [Monitor indexer status and results in Azure AI Search](search-howto-monitor-indexers.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "大規模インデックス作成に関するドキュメントのリネームと内容の更新"
}
```

### Explanation
この変更は、`articles/search/search-how-to-large-index.md`ファイルが`articles/search/search-howto-large-index.md`にリネームされ、内容が一部更新されたことを示しています。具体的には、文書の説明が明確にされ、インデックス作成における戦略がより洗練されました。日付が「04/01/2024」から「10/24/2024」に変更され、重要なポイントや構成が調整されています。また、ドキュメントのセクションタイトルがより具体的になり、情報が整理されています。これにより、ユーザーは大規模データセットのインデックス作成手法について、より効果的に理解できるようになります。全体而言、リネームと内容の更新は、ドキュメントの可読性と実用性を向上させることを目的としています。

## articles/search/search-howto-run-reset-indexers.md{#item-fb10c8}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 06/25/2024
+ms.date: 10/25/2024
 ---
 
 # Run or reset indexers, skills, or documents
@@ -28,7 +28,7 @@ Indexers are one of the few subsystems that make overt outbound calls to other A
 
 ## Indexer execution
 
-A search service runs one indexer job per [search unit](search-capacity-planning.md#concepts-search-units-replicas-partitions). Every search service starts with one search unit, but each new partition or replica increases the search units of your service. You can check the search unit count in the portal's Essential section of the **Overview** page. If you need concurrent processing, make sure you have sufficient replicas. Indexers don't run in the background, so you might detect more query throttling than usual if the service is under pressure.
+A search service runs one indexer job per [search unit](search-capacity-planning.md#concepts-search-units-replicas-partitions). Every search service starts with one search unit, but each new partition or replica increases the search units of your service. You can check the search unit count in the portal's Essential section of the **Overview** page. If you need concurrent processing, make sure your search units include sufficient replicas. Indexers don't run in the background, so you might detect more query throttling than usual if the service is under pressure.
 
 The following screenshot shows the number of search units, which determines how many indexers can run at once.
 
@@ -38,13 +38,16 @@ Once indexer execution starts, you can't pause or stop it. Indexer execution sto
 
 You can run multiple indexers at one time assuming sufficient capacity, but each indexer itself is single-instance. Starting a new instance while the indexer is already in execution produces this error: `"Failed to run indexer "<indexer name>" error: "Another indexer invocation is currently in progress; concurrent invocations are not allowed."`
 
-An indexer job runs in a managed execution environment. Currently, there are two environments. You can't control or configure which environment is used. Azure AI Search determines the environment based on job composition and the ability of the service to move an indexer job onto a content processor (some [security features](search-indexer-securing-resources.md#indexer-execution-environment) block the multitenant environment).
+An indexer job runs in a managed execution environment. Currently, there are two environments:
 
-Indexer execution environments include:
++ A private execution environment runs on search clusters that are specific to your search service. If your search service is Standard2 or nigher, you can [set the `executionEnvironment` parameter](search-how-to-create-indexers.md?tabs=indexer-rest#create-an-indexer) in the indexer definition to always run an indexer in the private execution environment. 
 
-+ A private execution environment that runs on content processors that are specific to your search service.
++ A multitenant environment has content processors that are managed and secured by Microsoft at no extra cost. This environment is used to offload computationally intensive processing, leaving service-specific resources available for routine operations. Whenever possible, most skillsets execute in the multitenant environment. This is the default.
 
-+ A multitenant environment with content processors, managed and secured by Microsoft at no extra cost. This environment is used to offload computationally intensive processing, leaving service-specific resources available for routine operations. Whenever possible, most indexer jobs are executed in the multitenant environment.
+  Computationally intensive processing includes skillsets running on content processors, and high volume indexer jobs or indexer jobs with large documents. Non-skillset processing on the multitenant content processors is determined by hueristics and system information and isn't under customer control. S2 services and higher support pinning an indexer and skillset processing exclusively to your search clusters through the `executionEnvironment` parameter.
+
+  > [!NOTE]
+  > [IP firewalls](search-indexer-securing-resources.md#indexer-execution-environment) block the multitenant environment, so if you have a firewall, create a rule that allows multitenant processing.
 
 Indexer limits vary for each environment:
 
@@ -55,7 +58,7 @@ Indexer limits vary for each environment:
 
 <sup>1</sup> Search units can be [flexible combinations](search-capacity-planning.md#partition-and-replica-combinations) of partitions and replicas, but indexer jobs aren't tied to one or the other. In other words, if you have 12 units, you can have 12 indexer jobs running concurrently in private execution, no matter how the search units are deployed.
 
-<sup>2</sup> If more than two hours are needed to process all of the data, [enable change detection](search-howto-create-indexers.md#change-detection-and-internal-state) and [schedule the indexer](search-howto-schedule-indexers.md) to run at two hour intervals. See [Indexing a large data set](search-howto-large-index.md) for more strategies.
+<sup>2</sup> If more than two hours are needed to process all of the data, [enable change detection](search-howto-create-indexers.md#change-detection-and-internal-state) and [schedule the indexer](search-howto-schedule-indexers.md) to run at 5 minute intervals to resume indexing quickly if it stops due to a timeout. See [Indexing a large data set](search-howto-large-index.md) for more strategies.
 
 <sup>3</sup> "Indeterminate" means that the limit isn't quantified by the number of jobs. Some workloads, such as skillset processing, can run in parallel, which could result in many jobs even though only one indexer is involved. Although the environment doesn't impose constraints, [indexer limits](search-limits-quotas-capacity.md#indexer-limits) for your search service still apply.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーの実行とリセットに関するドキュメントの更新"
}
```

### Explanation
この変更は、`articles/search/search-howto-run-reset-indexers.md`ファイルにおけるインデクサーの実行プロセスに関する情報の更新を反映しています。具体的には、日付が「06/25/2024」から「10/25/2024」に変更されたほか、インデクサーの実行に関する詳細が補足されました。新たに追加された情報として、プライベート環境とマルチテナント環境についての説明が強化され、マルチテナント環境は、マイクロソフトが管理するコンテンツプロセッサーを使用して計算集約的な処理をオフロードすることが明記されています。また、インデクサーがデータを処理する際のタイムアウトに関する新たな推奨事項として、インデクサーを5分間隔でスケジュールすることで、迅速にインデクシングを再開できるようにすることが提案されています。これにより、ユーザーはインデクサーの運用やパフォーマンスをさらに最適化できるようになります。全体として、この更新はドキュメントの精度と実用性を向上させるものです。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -277,12 +277,12 @@ A `202 Accepted` response is returned on success. The process of creating an out
 <!-- 
 1. Check the response. The `PUT` call to create the shared private endpoint returns an `Azure-AsyncOperation` header value that looks like the following:
 
-   `"Azure-AsyncOperation": "https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/contoso/providers/Microsoft.Search/searchServices/contoso-search/sharedPrivateLinkResources/blob-pe/operationStatuses/08586060559526078782?api-version=2022-09-01"`
+   `"Azure-AsyncOperation": "https://management.azure.com/subscriptions/ffffffff-eeee-dddd-cccc-bbbbbbbbbbb0/resourceGroups/contoso/providers/Microsoft.Search/searchServices/contoso-search/sharedPrivateLinkResources/blob-pe/operationStatuses/08586060559526078782?api-version=2022-09-01"`
 
    You can poll for the status by manually querying the `Azure-AsyncOperationHeader` value.
 
    ```azurecli
-   az rest --method get --uri https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/contoso/providers/Microsoft.Search/searchServices/contoso-search/sharedPrivateLinkResources/blob-pe/operationStatuses/08586060559526078782?api-version=2022-09-01
+   az rest --method get --uri https://management.azure.com/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/contoso/providers/Microsoft.Search/searchServices/contoso-search/sharedPrivateLinkResources/blob-pe/operationStatuses/08586060559526078782?api-version=2022-09-01
    ```
  -->
 
@@ -325,7 +325,7 @@ On the Azure AI Search side, you can confirm request approval by revisiting the
 Alternatively, you can also obtain connection state by using the [Shared Private Link Resources - Get](/rest/api/searchmanagement/shared-private-link-resources/get).
 
 ```dotnetcli
-az rest --method get --uri https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/contoso/providers/Microsoft.Search/searchServices/contoso-search/sharedPrivateLinkResources/blob-pe?api-version=2024-07-01
+az rest --method get --uri https://management.azure.com/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/contoso/providers/Microsoft.Search/searchServices/contoso-search/sharedPrivateLinkResources/blob-pe?api-version=2024-07-01
 ```
 
 This would return a JSON, where the connection state shows up as "status" under the "properties" section. Following is an example for a storage account.
@@ -334,7 +334,7 @@ This would return a JSON, where the connection state shows up as "status" under
 {
       "name": "blob-pe",
       "properties": {
-        "privateLinkResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/contoso/providers/Microsoft.Storage/storageAccounts/contoso-storage",
+        "privateLinkResourceId": "/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/contoso/providers/Microsoft.Storage/storageAccounts/contoso-storage",
         "groupId": "blob",
         "requestMessage": "please approve",
         "status": "Approved",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートインデクサーアクセス文書の修正"
}
```

### Explanation
この変更は、`articles/search/search-indexer-howto-access-private.md`ファイルにおけるプライベートインデクサーへのアクセス手続きの詳細が修正されたことを示しています。主に、AzureリソースのサブスクリプションIDが変更されています。具体的には、数箇所でサブスクリプションIDが「00000000-0000-0000-0000-000000000000」から「aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4」に修正され、具体的なエンドポイントURLやリソースアクセスに関する説明が更新されました。また、Azure CLIを使用してリソースの状態を確認する手順においても、同様にスクリプトに含まれるサブスクリプションIDが変更されています。これにより、ユーザーは最新のリソース構成に基づいて正確な操作を行えるようになっています。全体として、これらの変更はドキュメントの正確性を向上させ、ユーザーの理解を助けるものです。

## articles/search/search-indexer-securing-resources.md{#item-c075c4}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 05/01/2024
+ms.date: 10/25/2024
 ---
 
 # Indexer access to content protected by Azure network security
@@ -35,6 +35,7 @@ A list of all possible Azure resource types that an indexer might access in a ty
 | Azure Storage (blobs, tables) | Skillsets (caching enrichments, debug sessions, knowledge store projections) |
 | Azure Cosmos DB (various APIs) | Data source |
 | Azure SQL Database | Data source |
+| OneLake (Microsoft Fabric) | Data source |
 | SQL Server on Azure virtual machines | Data source |
 | SQL Managed Instance | Data source |
 | Azure Functions | Attached to a skillset and used to host for custom web API skills |
@@ -71,12 +72,14 @@ Your Azure resources could be protected using any number of the network isolatio
 
 Azure AI Search has the concept of an *indexer execution environment* that optimizes processing based on the characteristics of the job. There are two environments. If you're using an IP firewall to control access to Azure resources, knowing about execution environments will help you set up an IP range that is inclusive of both environments.
 
-For any given indexer run, Azure AI Search determines the best environment in which to run the indexer. Depending on the number and types of tasks assigned, the indexer will run in one of two environments.
+For any given indexer run, Azure AI Search determines the best environment in which to run the indexer. Depending on the number and types of tasks assigned, the indexer will run in one of two environments/
 
 | Execution environment | Description |
 |-----------------------|-------------|
-| Private | Internal to a search service. Indexers running in the private environment share computing resources with other indexing and query workloads on the same search service. Typically, only indexers that perform text-based indexing (without skillsets) run in this environment. If you set up a private connection between an indexer and your data, this is the only execution enriovnment you can use. |
-|  multitenant | Managed and secured by Microsoft at no extra cost. It isn't subject to any network provisions under your control. This environment is used to offload computationally intensive processing, leaving service-specific resources available for routine operations. Examples of resource-intensive indexer jobs include attaching skillsets, processing large documents, or processing a high volume of documents. |
+| Private | Internal to a search service. Indexers running in the private environment share computing resources with other indexing and query workloads on the same search service. If you set up a private connection between an indexer and your data, such as a shared private link, this is the only execution enriovnment you can use and it's used automatically. |
+|  multitenant | Managed and secured by Microsoft at no extra cost. It isn't subject to any network provisions under your control. This environment is used to offload computationally intensive processing, leaving service-specific resources available for routine operations. Examples of resource-intensive indexer jobs include skillsets, processing large documents, or processing a high volume of documents. |
+
+For Standard2 services and higher, you can configure an indexer to always use the private environment. For more information, see [Create an indexer](search-how-to-create-indexers.md?tabs=indexer-rest#create-an-indexer).
 
 ### Setting up IP ranges for indexer execution
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーのリソース保護に関する文書の更新"
}
```

### Explanation
この変更は、`articles/search/search-indexer-securing-resources.md`ファイルにおけるインデクサーがAzureリソースにアクセスする際のセキュリティに関する情報を更新したものです。主に、ドキュメントの日付が「05/01/2024」から「10/25/2024」に変更され、リソースタイプのリストに「OneLake (Microsoft Fabric)」が追加されました。また、インデクサーの実行環境に関する説明が強化され、プライベート接続を設定した場合、プライベート環境のみが使用されることが明記されています。さらに、Standard2サービス以上のインデクサーに関しては、常にプライベート環境を使用するように設定できることが追加情報として提供されています。この更新により、ユーザーはインデクサーのアクセス設定やセキュリティに関する理解を深めることができます。全体として、ドキュメントの正確性と実用性が向上しています。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 10/22/2024
+ms.date: 10/24/2024
 ms.custom:
   - references_regions
   - build-2024
@@ -18,21 +18,21 @@ ms.custom:
 
 Maximum limits on storage, workloads, and quantities of indexes and other objects depend on whether you [create Azure AI Search](search-create-service-portal.md) at **Free**, **Basic**, **Standard**, or **Storage Optimized** pricing tiers.
 
-+ **Free** is a multitenant shared service that comes with your Azure subscription. 
++ **Free** is a multitenant shared service that comes with your Azure subscription.
 
 + **Basic** provides dedicated computing resources for production workloads at a smaller scale, but shares some networking infrastructure with other tenants.
 
-+ **Standard** runs on dedicated machines with more storage and processing capacity at every level. Standard comes in four levels: S1, S2, S3, and S3 HD. S3 High Density (S3 HD) is engineered for [multi-tenancy](search-modeling-multitenant-saas-applications.md) and large quantities of small indexes (3,000 indexes per service). S3 HD doesn't provide the [indexer feature](search-indexer-overview.md) and data ingestion must use APIs that push data from source to index. 
++ **Standard** runs on dedicated machines with more storage and processing capacity at every level. Standard comes in four levels: S1, S2, S3, and S3 HD. S3 High Density (S3 HD) is engineered for [multi-tenancy](search-modeling-multitenant-saas-applications.md) and large quantities of small indexes (3,000 indexes per service). S3 HD doesn't provide the [indexer feature](search-indexer-overview.md) and data ingestion must use APIs that push data from source to index.
 
 + **Storage Optimized** runs on dedicated machines with more total storage, storage bandwidth, and memory than **Standard**. This tier targets large, slow-changing indexes. Storage Optimized comes in two levels: L1 and L2.
 
 ## Subscription limits
+
 [!INCLUDE [azure-search-limits-per-subscription](~/reusable-content/ce-skilling/azure/includes/azure-search-limits-per-subscription.md)]
 
 ## Service limits
-[!INCLUDE [azure-search-limits-per-service](~/reusable-content/ce-skilling/azure/includes/azure-search-limits-per-service.md)]
 
-<a name="index-limits"></a>
+[!INCLUDE [azure-search-limits-per-service](~/reusable-content/ce-skilling/azure/includes/azure-search-limits-per-service.md)]
 
 ## Index limits
 
@@ -49,7 +49,7 @@ Maximum limits on storage, workloads, and quantities of indexes and other object
 | Maximum functions per profile |8 |8 |8 |8 |8 |8 |8 |8 |
 | Maximum index size&nbsp;<sup>4</sup> | N/A | N/A | N/A | 1.88&nbsp;TB | 2.34&nbsp;TB | 100 GB| N/A | N/A |
 
-<sup>1</sup> Basic services created before December 2017 have lower limits (5 instead of 15) on indexes. Basic tier is the only tier with a lower limit of 100 fields per index. 
+<sup>1</sup> Basic services created before December 2017 have lower limits (5 instead of 15) on indexes. Basic tier is the only tier with a lower limit of 100 fields per index.
 
 <sup>2</sup> The upper limit on fields includes both first-level fields and nested subfields in a complex collection. For example, if an index contains 15 fields and has two complex collections with five subfields each, the field count of your index is 25. Indexes with a very large fields collection can be slow. [Limit fields and attributes](search-what-is-an-index.md#physical-structure-and-size) to just those you need, and run indexing and query test to ensure performance is acceptable.
 
@@ -59,22 +59,22 @@ Maximum limits on storage, workloads, and quantities of indexes and other object
 
 You might find some variation in maximum limits if your service happens to be provisioned on a more powerful cluster. The limits here represent the common denominator. Indexes built to the above specifications are portable across equivalent service tiers in any region.
 
-<a name="document-limits"></a>
-
-## Document limits 
+## Document limits
 
 Maximum number of documents per index are:
 
-+ 24 billion on Basic, S1, S2, S3, L1, and L2 search services.
-+ 2 billion on S3 HD.
++ 24 billion on Basic, S1, S2, S3
++ 2 billion on S3 HD
++ 288 billion on L1
++ 576 billion on L2
 
 Each instance of a complex collection counts as a separate document in terms of these limits.
 
-Maximum document size when calling an Index API is approximately 16 megabytes.
+Maximum size of each document is approximately 16 megabytes. Document size is actually a limit on the size of the indexing API request payload, which is 16 megabytes. That payload can be a single document, or a batch of documents. For a batch with a single document, the maximum document size is 16 MB of JSON. 
 
-Document size is actually a limit on the size of the Index API request body. Since you can pass a batch of multiple documents to the Index API at once, the size limit realistically depends on how many documents are in the batch. For a batch with a single document, the maximum document size is 16 MB of JSON.
+Document size applies to *push mode* indexing that uploads documents to a search service. If you're using an indexer for *pull mode* indexing, your source files can be any file size, subject to [indexer limits](#indexer-limits). For the blob indexer, file size limits are larger for higher tiers. For example, the S1 limit is 128 megabytes, S2 limit is 256 megabytes, and so forth.
 
-When estimating document size, remember to consider only those fields that add value to your search scenarios, and exclude any source fields that have no purpose in the queries you intend to run.
+When estimating document size, remember to index only those fields that add value to your search scenarios, and exclude any source fields that have no purpose in the queries you intend to run.
 
 ## Vector index size limits
 
@@ -100,7 +100,7 @@ This table shows the progression of vector quota increases in GB over time. The
 
 <sup>2</sup> Vector limits during the later preview period. Three regions didn't have the higher limits: Germany West Central, West India, Qatar Central.
 
-<sup>3</sup> Higher vector quota based on the larger partitions for supported tiers and regions. 
+<sup>3</sup> Higher vector quota based on the larger partitions for supported tiers and regions.
 
 <sup>4</sup> Higher vector quota for more tiers and regions based on partition size updates.
 
@@ -121,9 +121,9 @@ Maximum running times exist to provide balance and stability to the service as a
 | Maximum indexing load per invocation |10,000 documents |Limited only by maximum documents |Limited only by maximum documents |Limited only by maximum documents |Limited only by maximum documents |N/A |No limit |No limit |
 | Minimum schedule | 5 minutes |5 minutes |5 minutes |5 minutes |5 minutes |5 minutes |5 minutes | 5 minutes |
 | Maximum running time <sup>5</sup>| 1-3 minutes |2 or 24 hours |2 or 24 hours |2 or 24 hours |2 or 24 hours |N/A  |2 or 24 hours |2 or 24 hours |
-| Maximum running time for indexers with a skillset <sup>6</sup> | 3-10 minutes |2 hours |2 hours |2 hours |2 hours |N/A  |2 hours |2 hours |
+| Maximum running time for indexers with a skillset <sup>6</sup> | 3-10 minutes |2 or 24 hours |2 or 24 hours |2 or 24 hours |2 or 24 hours |N/A  |2 or 24 hours |2 or 24 hours |
 | Blob indexer: maximum blob size, MB |16 |16 |128 |256 |256 |N/A  |256 |256 |
-| Blob indexer: maximum characters of content extracted from a blob <sup>7</sup> |32,000 |64,000 |4&nbsp;million |8&nbsp;million |16&nbsp;million |N/A |4&nbsp;million |4&nbsp;million |
+| Blob indexer: maximum characters of content extracted from a blob <sup>6</sup> |32,000 |64,000 |4&nbsp;million |8&nbsp;million |16&nbsp;million |N/A |4&nbsp;million |4&nbsp;million |
 
 <sup>1</sup> Free services have indexer maximum execution time of 3 minutes for blob sources and 1 minute for all other data sources. Indexer invocation is once every 180 seconds. For AI indexing that calls into Azure AI services, free services are limited to 20 free transactions per indexer per day, where a transaction is defined as a document that successfully passes through the enrichment pipeline (tip: you can reset an indexer to reset its count).
 
@@ -133,11 +133,9 @@ Maximum running times exist to provide balance and stability to the service as a
 
 <sup>4</sup> Maximum of 30 skills per skillset.
 
-<sup>5</sup> Regarding the 2 or 24 hour maximum duration for indexers: a 2-hour maximum is the most common and it's what you should plan for. The 24-hour limit is from an older indexer implementation. If you have unscheduled indexers that run continuously for 24 hours, it's because those indexers couldn't be migrated to the newer infrastructure. As a general rule, for indexing jobs that can't finish within two hours, put the indexer on a [2-hour schedule](search-howto-schedule-indexers.md). When the first 2-hour interval is complete, the indexer picks up where it left off when starting the next 2-hour interval.
+<sup>5</sup> Regarding the 2 or 24 hour maximum duration for indexers: a 2-hour maximum is the most common and it's what you should plan for. It refers to indexers that run in the [public environment](search-howto-run-reset-indexers.md#indexer-execution), used to offload computationally intensive processing and leave more resources for queries. The 24-hour limit applies if you configure the indexer to run in a private environment using only the infrastructure that's allocated to your search service. Note that some older indexers are incapable of running in the public environment, and those indexers always have a 24-hour processing range. If you have unscheduled indexers that run continuously for 24 hours, you can assume those indexers couldn't be migrated to the newer infrastructure. As a general rule, for indexing jobs that can't finish within two hours, put the indexer on a [5 minute schedule](search-howto-schedule-indexers.md) so that the indexer can quickly pick up where it left off.
 
-<sup>6</sup> Skillset execution, and image analysis in particular, are computationally intensive and consume disproportionate amounts of available processing power. Running time for these workloads is shorter so that other jobs in the queue have more opportunity to run.
-
-<sup>7</sup> The maximum number of characters is based on Unicode code units, specifically UTF-16.
+<sup>6</sup> The maximum number of characters is based on Unicode code units, specifically UTF-16.
 
 > [!NOTE]
 > As stated in the [Index limits](#index-limits), indexers will also enforce the upper limit of 3000 elements across all complex collections per document starting with the latest GA API version that supports complex types (`2019-05-06`) onwards. This means that if you've created your indexer with a prior API version, you will not be subject to this limit. To preserve maximum compatibility, an indexer that was created with a prior API version and then updated with an API version `2019-05-06` or later, will still be **excluded** from the limits. Customers should be aware of the adverse impact of having very large complex collections (as stated previously) and we highly recommend creating any new indexers with the latest GA API version.
@@ -160,8 +158,6 @@ Indexers can access other Azure resources [over private endpoints](search-indexe
 
 <sup>3</sup> The number of distinct resource types are computed as the number of unique `groupId` values used across all shared private link resources for a given search service, irrespective of the status of the resource.
 
-
-
 ## Synonym limits
 
 Maximum number of synonym maps varies by tier. Each rule can have up to 20 expansions, where an expansion is an equivalent term. For example, given "cat", association with "kitty", "feline", and "felis" (the genus for cats) would count as 3 expansions.
@@ -188,15 +184,15 @@ An [AI enrichment pipeline](cognitive-search-concept-intro.md) that makes calls
 
 ## Throttling limits
 
-API requests are throttled as the system approaches peak capacity. Throttling behaves differently for different APIs. Query APIs (Search/Suggest/Autocomplete) and indexing APIs throttle dynamically based on the load on the service. Index APIs and service operations API have static request rate limits. 
+API requests are throttled as the system approaches peak capacity. Throttling behaves differently for different APIs. Query APIs (Search/Suggest/Autocomplete) and indexing APIs throttle dynamically based on the load on the service. Index APIs and service operations API have static request rate limits.
 
 Static rate request limits for operations related to an index:
 
 + List Indexes (GET /indexes): 3 per second per search unit
 + Get Index (GET /indexes/myindex): 10 per second per search unit
 + Create Index (POST /indexes): 12 per minute per search unit
 + Create or Update Index (PUT /indexes/myindex): 6 per second per search unit
-+ Delete Index (DELETE /indexes/myindex): 12 per minute per search unit 
++ Delete Index (DELETE /indexes/myindex): 12 per minute per search unit
 
 Static rate request limits for operations related to a service:
 
@@ -208,28 +204,30 @@ L2 reranking using the semantic reranker has an expected volume:
 
 ## API request limits
 
-* Maximum of 16 MB per request <sup>1</sup>
-* Maximum 8-KB URL length
-* Maximum 1,000 documents per batch of index uploads, merges, or deletes
-* Maximum 32 fields in $orderby clause
-* Maximum 100,000 characters in a search clause
-* The maximum number of clauses in `search` (expressions separated by AND or OR) is 1024
-* Maximum search term size is 32,766 bytes (32 KB minus 2 bytes) of UTF-8 encoded text
-* Maximum search term size is 1,000 characters for [prefix search](query-simple-syntax.md#prefix-queries) and [regex search](query-lucene-syntax.md#bkmk_regex)
-* [Wildcard search](query-lucene-syntax.md#bkmk_wildcard) and [Regular expression search](query-lucene-syntax.md#bkmk_regex) are limited to a maximum of 1,000 states when processed by [Lucene](https://lucene.apache.org/core/7_0_1/core/org/apache/lucene/util/automaton/RegExp.html). 
+Except where noted, the following API requests apply to all programmable interfaces, including the Azure SDKs.
+
++ Maximum of 16 MB per indexing or query request when pushing a payload to the search service <sup>1</sup>
++ Maximum 8-KB URL length (applies to REST APIs only)
++ Maximum 1,000 documents per batch of index uploads, merges, or deletes
++ Maximum 32 fields in $orderby clause
++ Maximum 100,000 characters in a search clause
++ The maximum number of clauses in `search` (expressions separated by AND or OR) is 1024
++ Maximum search term size is 32,766 bytes (32 KB minus 2 bytes) of UTF-8 encoded text
++ Maximum search term size is 1,000 characters for [prefix search](query-simple-syntax.md#prefix-queries) and [regex search](query-lucene-syntax.md#bkmk_regex)
++ [Wildcard search](query-lucene-syntax.md#bkmk_wildcard) and [Regular expression search](query-lucene-syntax.md#bkmk_regex) are limited to a maximum of 1,000 states when processed by [Lucene](https://lucene.apache.org/core/7_0_1/core/org/apache/lucene/util/automaton/RegExp.html).
 
 <sup>1</sup> In Azure AI Search, the body of a request is subject to an upper limit of 16 MB, imposing a practical limit on the contents of individual fields or collections that aren't otherwise constrained by theoretical limits (see [Supported data types](/rest/api/searchservice/supported-data-types) for more information about field composition and restrictions).
 
 Limits on query size and composition exist because unbounded queries can destabilize your search service. Typically, such queries are created programmatically. If your application generates search queries programmatically, we recommend designing it in such a way that it doesn't generate queries of unbounded size.
 
 ## API response limits
 
-* Maximum 1,000 documents returned per page of search results
-* Maximum 100 suggestions returned per Suggest API request
++ Maximum 1,000 documents returned per page of search results
++ Maximum 100 suggestions returned per Suggest API request
 
 ## API key limits
 
 API keys are used for service authentication. There are two types. Admin keys are specified in the request header and grant full read-write access to the service. Query keys are read-only, specified on the URL, and typically distributed to client applications.
 
-* Maximum of 2 admin keys per service
-* Maximum of 50 query keys per service
++ Maximum of 2 admin keys per service
++ Maximum of 50 query keys per service
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスの制限とクォータに関するドキュメントの更新"
}
```

### Explanation
この変更は、`articles/search/search-limits-quotas-capacity.md`ファイルにおけるAzure AI Searchサービスの制限やクォータに関連する情報を更新したものです。主な変更点として、ドキュメントの日付が「10/22/2024」から「10/24/2024」に変更されています。また、ストレージ、ワークロード、インデックスおよびその他のオブジェクトに関する最大制限の記述が改善され、一部の定義が明確にされました。

特に、各プラン（Free、Basic、Standard、Storage Optimized）の特徴や制限が詳細に説明され、例えば各プランの最大文書数の更新や、各文書の最大サイズが約16MBであることが記載されています。また、APIリクエストやレスポンスの制限、キーに関する制限が明確に記述され、クエリのサイズや構成に関する制限の重要性も強調されています。

全体的に、これらの改訂は利用者がサービスの機能と制限をより良く理解できるようにし、正確性と有用性を向上させることを目的としています。

## articles/search/search-manage-powershell.md{#item-3c3485}

<details>
<summary>Diff</summary>
````diff
@@ -431,7 +431,7 @@ Sku               : Standard
 ReplicaCount      : 6
 PartitionCount    : 6
 HostingMode       : Default
-Id                : /subscriptions/65a1016d-0f67-45d2-b838-b8f373d6d52e/resourceGroups/demo-westus/providers/Microsoft.Search/searchServices/my-demo-searchapp
+Id                : /subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/demo-westus/providers/Microsoft.Search/searchServices/my-demo-searchapp
 ```
 
 ## Create a shared private link resource
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PowerShell 管理ドキュメントのリソース ID 更新"
}
```

### Explanation
この変更は、`articles/search/search-manage-powershell.md`ファイル内のリソースIDに関連する情報を更新したものです。具体的には、リソースのIDが「/subscriptions/65a1016d-0f67-45d2-b838-b8f373d6d52e/resourceGroups/demo-westus/providers/Microsoft.Search/searchServices/my-demo-searchapp」から「/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/demo-westus/providers/Microsoft.Search/searchServices/my-demo-searchapp」に変更されています。

この更新は、ドキュメントの正確性を高めることを目的としており、ユーザーが正しいリソースIDを使用してAzure Searchサービスを管理できるようにしています。また、変更は単純ですが、機能を利用する際に重要な部分であるため、正しい情報が提供されていることが確認できます。

## articles/search/search-query-lucene-examples.md{#item-ce3624}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Examples of full Lucene query syntax
 titleSuffix: Azure AI Search
-description: Query examples demonstrating the Lucene query syntax for fuzzy search, proximity search, term boosting, regular expression search, and wildcard searches in an Azure AI Search index.
+description: Explore query examples that demonstrate the Lucene query syntax for fuzzy search, proximity search, term boosting, regular expression search, and wildcard searches in an Azure AI Search index.
 
 manager: nitinme
 author: HeidiSteen
@@ -11,14 +11,14 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 01/17/2024
+ms.date: 10/24/2024
 ---
 
-# Examples of "full" Lucene search syntax (advanced queries in Azure AI Search)
+# Examples of *full* Lucene search syntax (advanced queries)
 
 When constructing queries for Azure AI Search, you can replace the default [simple query parser](query-simple-syntax.md) with the more powerful [Lucene query parser](query-lucene-syntax.md) to formulate specialized and advanced query expressions.
 
-The Lucene parser supports complex query formats, such as field-scoped queries, fuzzy search, infix and suffix wildcard search, proximity search, term boosting, and regular expression search. The extra power comes with more processing requirements so you should expect a slightly longer execution time. In this article, you can step through examples demonstrating query operations based on full syntax.
+The Lucene parser supports complex query formats, such as field-scoped queries, fuzzy search, infix and suffix wildcard search, proximity search, term boosting, and regular expression search. The extra power comes with more processing requirements so you should expect a slightly longer execution time. In this article, you can step through examples that demonstrate query operations based on full syntax.
 
 > [!NOTE]
 > Many of the specialized query constructions enabled through the full Lucene query syntax are not [text-analyzed](search-lucene-query-architecture.md#stage-2-lexical-analysis), which can be surprising if you expect stemming or lemmatization. Lexical analysis is only performed on complete terms (a term query or phrase query). Query types with incomplete terms (prefix query, wildcard query, regex query, fuzzy query) are added directly to the query tree, bypassing the analysis stage. The only transformation performed on partial query terms is lowercasing. 
@@ -43,7 +43,7 @@ URI parameters must include your search service endpoint with the index name, do
 https://{{service-name}}.search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2024-07-01
 ```
 
-Request body should be formed as valid JSON:
+The request body should be formed as valid JSON:
 
 ```json
 {
@@ -54,17 +54,17 @@ Request body should be formed as valid JSON:
 }
 ```
 
-+ "search" set to `*` is an unspecified query, equivalent to null or empty search. It's not especially useful, but it's the simplest search you can do, and it shows all retrievable fields in the index, with all values.
++ `search` set to * is an unspecified query, equivalent to null or empty search. It's not especially useful, but it's the simplest search you can do, and it shows all retrievable fields in the index, with all values.
 
-+ "queryType" set to "full" invokes the full Lucene query parser and it's required for this syntax.
++ `queryType` set to *full* invokes the full Lucene query parser and it's required for this syntax.
 
-+ "select" set to a comma-delimited list of fields is used for search result composition, including just those fields that are useful in the context of search results.
++ `select` set to a comma-delimited list of fields is used for search result composition, including only those fields that are useful in the context of search results.
 
-+ "count" returns the number of documents matching the search criteria. On an empty search string, the count is all documents in the index (50 in the hotels-sample-index).
++ `count` returns the number of documents matching the search criteria. On an empty search string, the count is all documents in the index (50 in the hotels-sample-index).
 
 ## Example 1: Fielded search
 
-Fielded search scope individual, embedded search expressions to a specific field. This example searches for hotel names with the term "hotel" in them, but not "motel". You can specify multiple fields using AND. 
+Fielded search scopes individual, embedded search expressions to a specific field. This example searches for hotel names with the term *hotel* in them, but not *motel*. You can specify multiple fields using `AND`.
 
 When you use this query syntax, you can omit the `searchFields` parameter when the fields you want to query are in the search expression itself. If you include `searchFields` with fielded search, the `fieldName:searchExpression` always takes precedence over `searchFields`.
 
@@ -78,7 +78,7 @@ POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
 }
 ```
 
-Response for this query should look similar to the following example, filtered on "Resort and Spa", returning hotels that include "hotel" in the name, while excluding results that include "motel" in the name.
+The response for this query should look similar to the following example, filtered on *Resort and Spa*, returning hotels that include *hotel* in the name, while excluding results that include *motel* in the name.
 
 ```json
 "@odata.count": 4,
@@ -112,9 +112,9 @@ The search expression can be a single term or a phrase, or a more complex expres
 + `Address/StateProvince:("WA" OR "CA")`
 + `Tags:("free wifi" NOT "free parking") AND "coffee in lobby"`
 
-Be sure to put a phrase within quotation marks if you want both strings to be evaluated as a single entity, as in this case searching for two distinct locations in the Address/StateProvince field. Depending on the client, you might need to escape (`\`) the quotation marks.
+Be sure to put a phrase within quotation marks if you want both strings to be evaluated as a single entity, as in this case searching for two distinct locations in the `Address/StateProvince` field. Depending on the client, you might need to escape (`\`) the quotation marks.
 
-The field specified in `fieldName:searchExpression` must be a searchable field. See [Create Index (REST API)](/rest/api/searchservice/indexes/create) for details on how field definitions are attributed.
+The field specified in `fieldName:searchExpression` must be a searchable field. To learn how field definitions are attributed, see [Create Index (REST API)](/rest/api/searchservice/indexes/create).
 
 ## Example 2: Fuzzy search
 
@@ -131,7 +131,7 @@ POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
 }
 ```
 
-Response for this query resolves to "concierge" in the matching documents, trimmed for brevity:
+The response for this query resolves to *concierge* in the matching documents, trimmed for brevity:
 
 ```json
 "@odata.count": 12,
@@ -168,17 +168,17 @@ Response for this query resolves to "concierge" in the matching documents, trimm
     },
 ```
 
-Phrases aren't supported directly but you can specify a fuzzy match on each term of a multi-part phrase, such as `search=Tags:landy~ AND sevic~`.  This query expression finds 15 matches on "laundry service".
+Phrases aren't supported directly but you can specify a fuzzy match on each term of a multi-part phrase, such as `search=Tags:landy~ AND sevic~`. This query expression finds 15 matches on *laundry service*.
 
 > [!Note]
 > Fuzzy queries are not [analyzed](search-lucene-query-architecture.md#stage-2-lexical-analysis). Query types with incomplete terms (prefix query, wildcard query, regex query, fuzzy query) are added directly to the query tree, bypassing the analysis stage. The only transformation performed on partial query terms is lower casing.
 >
 
 ## Example 3: Proximity search
 
-Proximity search finds terms that are near each other in a document. Insert a tilde "~" symbol at the end of a phrase followed by the number of words that create the proximity boundary.
+Proximity search finds terms that are near each other in a document. Insert a tilde `~` symbol at the end of a phrase followed by the number of words that create the proximity boundary.
 
-This query searches for the terms "hotel" and  "airport" within 5 words of each other in a document. The quotation marks are escaped (`\"`) to preserve the phrase:
+This query searches for the terms *hotel* and  *airport* within five words of each other in a document. The quotation marks are escaped (`\"`) to preserve the phrase:
 
 ```http
 POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
@@ -191,7 +191,7 @@ POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
 }
 ```
 
-Response for this query should look similar to the following example:
+The response for this query should look similar to the following example:
 
 ```json
 "@odata.count": 2,
@@ -213,7 +213,7 @@ Response for this query should look similar to the following example:
 
 Term boosting refers to ranking a document higher if it contains the boosted term, relative to documents that don't contain the term. To boost a term, use the caret, `^`, symbol with a boost factor (a number) at the end of the term you're searching. The boost factor default is 1, and although it must be positive, it can be less than 1 (for example, 0.2). Term boosting differs from scoring profiles in that scoring profiles boost certain fields, rather than specific terms.
 
-In this "before" query, search for "beach access" and notice that there are seven documents that match on one or both terms.
+In this *before* query, search for *beach access* and notice that there are seven documents that match on one or both terms.
 
 ```http
 POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
@@ -226,7 +226,7 @@ POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
 }
 ```
 
-In fact, there's only one document that matches on "access", and because it's the only match, it's placement is high (second position) even though the document is missing the term "beach".
+In fact, there's only one document that matches on *access*, and because it's the only match, it's placement is high (second position) even though the document is missing the term *beach*.
 
 ```json
 "@odata.count": 7,
@@ -253,15 +253,15 @@ In fact, there's only one document that matches on "access", and because it's th
     },
 ```
 
-In the "after" query, repeat the search, this time boosting results with the term "beach" over the term "access". A human readable version of the query is `search=Description:beach^2 access`. Depending on your client, you might need to express `^2` as `%5E2`.
+In the *after* query, repeat the search, this time boosting results with the term *beach* over the term *access*. A human readable version of the query is `search=Description:beach^2 access`. Depending on your client, you might need to express `^2` as `%5E2`.
 
-After boosting the term "beach", the match on Old Carrabelle Hotel moves down to sixth place.
+After boosting the term *beach*, the match on Old Carrabelle Hotel moves down to sixth place.
 
 <!-- Consider a scoring profile that boosts matches in a certain field, such as "genre" in a music app. Term boosting could be used to further boost certain search terms higher than others. For example, "rock^2 electronic" will boost documents that contain the search terms in the "genre" field higher than other searchable fields in the index. Furthermore, documents that contain the search term "rock" will be ranked higher than the other search term "electronic" as a result of the term boost value (2). -->
 
 ## Example 5: Regex
 
-A regular expression search finds a match based on the contents between forward slashes "/", as documented in the [RegExp class](https://lucene.apache.org/core/6_6_1/core/org/apache/lucene/util/automaton/RegExp.html).
+A regular expression search finds a match based on the contents between forward slashes `/`, as documented in the [RegExp class](https://lucene.apache.org/core/6_6_1/core/org/apache/lucene/util/automaton/RegExp.html).
 
 ```http
 POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
@@ -273,7 +273,7 @@ POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
 }
 ```
 
-Response for this query should look similar to the following example:
+The response for this query should look similar to the following example:
 
 ```json
     "@odata.count": 22,
@@ -318,9 +318,9 @@ Response for this query should look similar to the following example:
 
 ## Example 6: Wildcard search
 
-You can use generally recognized syntax for multiple (`*`) or single (`?`) character wildcard searches. Note the Lucene query parser supports the use of these symbols with a single term, and not a phrase.
+You can use generally recognized syntax for multiple (`*`) or single (`?`) character wildcard searches. The Lucene query parser supports the use of these symbols with a single term, and not a phrase.
 
-In this query, search for hotel names that contain the prefix 'sc'. You can't use a `*` or `?` symbol as the first character of a search.
+In this query, search for hotel names that contain the prefix *sc*. You can't use a `*` or `?` symbol as the first character of a search.
 
 ```http
 POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
@@ -332,7 +332,7 @@ POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
 }
 ```
 
-Response for this query should look similar to the following example:
+The response for this query should look similar to the following example:
 
 ```json
     "@odata.count": 2,
@@ -352,16 +352,15 @@ Response for this query should look similar to the following example:
 > Wildcard queries are not [analyzed](./search-lucene-query-architecture.md#stage-2-lexical-analysis). The only transformation performed on partial query terms is lower casing.
 >
 
-## Next steps
+## Related content
 
 Try specifying queries in code. The following link covers how to set up search queries using the Azure SDKs.
 
 + [Quickstart: Full text search using the Azure SDKs](search-get-started-text.md)
 
-More syntax reference, query architecture, and examples can be found in the following links:
+More syntax reference, query architecture, and examples can be found in the following articles:
 
-+ [Lucene syntax query examples for building advanced queries](search-query-lucene-examples.md)
-+ [How full text search works in Azure AI Search](search-lucene-query-architecture.md)
++ [Full text search in Azure AI Search](search-lucene-query-architecture.md)
 + [Simple query syntax](query-simple-syntax.md)
-+ [Full Lucene query syntax](query-lucene-syntax.md)
-+ [Filter syntax](search-query-odata-filter.md)
++ [Lucene query syntax in Azure AI Search](query-lucene-syntax.md)
++ [OData $filter syntax in Azure AI Search](search-query-odata-filter.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Lucene クエリ構文の例に関するドキュメントの更新"
}
```

### Explanation
この変更は、`articles/search/search-query-lucene-examples.md`ファイルの内容を更新したものです。主な更新内容は、クエリの説明や構文の記述に関する文章を改善し、理解しやすくすることを目的としています。具体的には、用語の強調や文の流れが調整され、日付が「01/17/2024」から「10/24/2024」に変更されています。

また、Luceneクエリパーサーの機能やクエリ例の解説が充実しており、特にフィールドスコープ検索、ファジー検索、近接検索、正規表現検索、ワイルドカード検索に関する説明が強調されています。文章の表現が見直され、クエリの使用方法についての具体例が詳細に示されたことで、利用者がAzure AI Searchでのクエリの構築に役立つ内容となっています。

これにより、ユーザーはLuceneクエリ構文の利用方法をよりよく理解でき、特定の検索要件に基づいてクエリを作成する際の手助けとなることを目指しています。全体的に、ドキュメントの精度と有用性が向上しています。

## articles/search/search-query-simple-examples.md{#item-834766}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Examples of simple syntax
 titleSuffix: Azure AI Search
-description: Query examples demonstrating the simple syntax for full text search, filter search, and geo search against an Azure AI Search index.
+description: Explore query examples that demonstrate the simple syntax for full text search, filter search, and geo search against an Azure AI Search index.
 
 manager: nitinme
 author: HeidiSteen
@@ -10,21 +10,21 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 01/17/2024
+ms.date: 10/24/2024
 ---
 
-# Examples of "simple" search queries in Azure AI Search
+# Examples of *simple* search queries in Azure AI Search
 
 In Azure AI Search, the [simple query syntax](query-simple-syntax.md) invokes the default query parser for full text search. The parser is fast and handles common scenarios, including full text search, filtered and faceted search, and prefix search. This article uses examples to illustrate simple syntax usage in a [Search Documents (REST API)](/rest/api/searchservice/documents/search-post) request.
 
 > [!NOTE]
-> An alternative query syntax is [Full Lucene](query-lucene-syntax.md), supporting more complex query structures, such as fuzzy and wildcard search. For more information and examples, see [Use the full Lucene syntax](search-query-lucene-examples.md).
+> An alternative query syntax is [Lucene](query-lucene-syntax.md), which supports more complex query structures, such as fuzzy and wildcard search. For more information, see [Examples of full Lucene search syntax ](search-query-lucene-examples.md).
 
 ## Hotels sample index
 
-The following queries are based on the hotels-sample-index, which you can create by following the instructions in this [quickstart](search-get-started-portal.md).
+The following queries are based on the hotels-sample-index, which you can create by following the instructions in [Quickstart: Create a search index in the Azure portal](search-get-started-portal.md).
 
-Example queries are articulated using the REST API and POST requests. You can paste and run them in a [REST client](search-get-started-rest.md). Or, use the JSON view of [Search Explorer](search-explorer.md) in the Azure portal. In JSON view, you can paste in the query examples shown here in this article.
+Example queries are articulated using the REST API and POST requests. You can paste and run them in a [REST client](search-get-started-rest.md). Or, use the JSON view of [Search explorer](search-explorer.md) in the Azure portal. In JSON view, you can paste in the query examples shown here in this article.
 
 Request headers must have the following values:
 
@@ -39,7 +39,7 @@ URI parameters must include your search service endpoint with the index name, do
 https://{{service-name}}.search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2024-07-01
 ```
 
-Request body should be formed as valid JSON:
+The request body should be formed as valid JSON:
 
 ```json
 {
@@ -50,17 +50,17 @@ Request body should be formed as valid JSON:
 }
 ```
 
-+ "search" set to `*` is an unspecified query, equivalent to null or empty search. It's not especially useful, but it's the simplest search you can do, and it shows all retrievable fields in the index, with all values.
++ `search` set to * is an unspecified query, equivalent to null or empty search. It's not especially useful, but it's the simplest search you can do, and it shows all retrievable fields in the index, with all values.
 
-+ "queryType" set to "simple" is the default and can be omitted, but it's included to further reinforce that the query examples in this article are expressed in the simple syntax.
++ `queryType` set to *simple* is the default and can be omitted, but it's included to emphasize that the query examples in this article are expressed in the simple syntax.
 
-+ "select" set to a comma-delimited list of fields is used for search result composition, including just those fields that are useful in the context of search results.
++ `select` set to a comma-delimited list of fields is used for search result composition, including just those fields that are useful in the context of search results.
 
-+ "count" returns the number of documents matching the search criteria. On an empty search string, the count is all documents in the index (50 in the hotels-sample-index).
++ `count` returns the number of documents matching the search criteria. On an empty search string, the count is all documents in the index (50 in the hotels-sample-index).
 
 ## Example 1: Full text search
 
-Full text search can be any number of standalone terms or quote-enclosed phrases, with or without boolean operators. 
+Full text search can be any number of standalone terms or quote-enclosed phrases, with or without Boolean operators. 
 
 ```http
 POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
@@ -73,11 +73,11 @@ POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
 }
 ```
 
-A keyword search that's composed of important terms or phrases tend to work best. String fields undergo text analysis during indexing and querying, dropping nonessential words like "the", "and", "it". To see how a query string is tokenized in the index, pass the string in an [Analyze Text](/rest/api/searchservice/indexes/analyze) call to the index.
+A keyword search that's composed of important terms or phrases tend to work best. String fields undergo text analysis during indexing and querying, dropping nonessential words like *the*, *and*, *it*. To see how a query string is tokenized in the index, pass the string in an [Analyze Text](/rest/api/searchservice/indexes/analyze) call to the index.
 
-The "searchMode" parameter controls precision and recall. If you want more recall, use the default "any" value, which returns a result if any part of the query string is matched. If you favor precision, where all parts of the string must be matched, change searchMode to "all". Try the above query both ways to see how searchMode changes the outcome.
+The `searchMode` parameter controls precision and recall. If you want more recall, use the default *any* value, which returns a result if any part of the query string is matched. If you favor precision, where all parts of the string must be matched, change `searchMode` to *all*. Try the preceding query both ways to see how searchMode changes the outcome.
 
-Response for the "pool spa +airport" query should look similar to the following example, trimmed for brevity.
+The response for the *pool spa +airport* query should look similar to the following example, trimmed for brevity.
 
 ```json
 "@odata.count": 6,
@@ -123,19 +123,19 @@ Response for the "pool spa +airport" query should look similar to the following
 
 Notice the search score in the response. This is the relevance score of the match. By default, a search service returns the top 50 matches based on this score.
 
-Uniform scores of "1.0" occur when there's no rank, either because the search wasn't full text search, or because no criteria were provided. For example, in an empty search (search=`*`), rows come back in arbitrary order. When you include actual criteria, you'll see search scores evolve into meaningful values.
+Uniform scores of *1.0* occur when there's no rank, either because the search wasn't full text search, or because no criteria were provided. For example, in an empty search (search=`*`), rows come back in arbitrary order. When you include actual criteria, you'll see search scores evolve into meaningful values.
 
 ## Example 2: Look up by ID
 
-When returning search results in a query, a logical next step is to provide a details page that includes more fields from the document. This example shows you how to return a single document using [Lookup Document](/rest/api/searchservice/documents/get) by passing in the document ID.
+When returning search results in a query, a logical next step is to provide a details page that includes more fields from the document. This example shows you how to return a single document using [Get Document](/rest/api/searchservice/documents/get) by passing in the document ID.
 
 ```http
 GET /indexes/hotels-sample-index/docs/41?api-version=2024-07-01
 ```
 
 All documents have a unique identifier. If you're using the portal, select the index from the **Indexes** tab and then look at the field definitions to determine which field is the key. Using REST, the [Get Index](/rest/api/searchservice/indexes/get) call returns the index definition in the response body.
 
-Response for the above query consists of the document whose key is 41. Any field that is marked as "retrievable" in the index definition can be returned in search results and rendered in your app.
+The response for the preceding query consists of the document whose key is *41*. Any field that is marked as *retrievable* in the index definition can be returned in search results and rendered in your app.
 
 ```json
 {
@@ -179,7 +179,7 @@ Response for the above query consists of the document whose key is 41. Any field
 
 [Filter syntax](search-query-odata-filter.md) is an OData expression that you can use by itself or with `search`. Used together, `filter` is applied first to the entire index, and then the search is performed on the results of the filter. Filters can therefore be a useful technique to improve query performance since they reduce the set of documents that the search query needs to process.
 
-Filters can be defined on any field marked as `filterable` in the index definition. For hotels-sample-index, filterable fields include Category, Tags, ParkingIncluded, Rating, and most Address fields.
+Filters can be defined on any field marked as `filterable` in the index definition. For hotels-sample-index, filterable fields include *Category*, *Tags*, *ParkingIncluded*, *Rating*, and most *Address* fields.
 
 ```http
 POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
@@ -193,7 +193,7 @@ POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
 }
 ```
 
-Response for the above query is scoped to only those hotels categorized as "Report and Spa", and that include the terms "art" or "tours". In this case, there's just one match.
+The response for the preceding query is scoped to only those hotels categorized as *Report and Spa*, and that include the terms *art* or *tours*. In this case, there's just one match.
 
 ```json
 {
@@ -207,7 +207,7 @@ Response for the above query is scoped to only those hotels categorized as "Repo
 
 ## Example 4: Filter functions
 
-Filter expressions can include ["search.ismatch" and "search.ismatchscoring" functions](search-query-odata-full-text-search-functions.md), allowing you to build a search query within the filter. This filter expression uses a wildcard on *free* to select amenities including free wifi, free parking, and so forth.
+Filter expressions can include [search.ismatch and search.ismatchscoring functions](search-query-odata-full-text-search-functions.md), allowing you to build a search query within the filter. This filter expression uses a wildcard on *free* to select amenities including free wifi, free parking, and so forth.
 
 ```http
 POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
@@ -219,7 +219,7 @@ POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
   }
 ```
 
-Response for the above query matches on 19 hotels that offer free amenities. Notice that the search score is a uniform "1.0" throughout the results. This is because the search expression is null or empty, resulting in verbatim filter matches, but no full text search. Relevance scores are only returned on full text search. If you're using filters without `search`, make sure you have sufficient sortable fields so that you can control search rank.
+The response for the preceding query matches on 19 hotels that offer free amenities. Notice that the search score is a uniform *1.0* throughout the results. This is because the search expression is null or empty, resulting in verbatim filter matches, but no full text search. Relevance scores are only returned on full text search. If you're using filters without `search`, make sure you have sufficient sortable fields so that you can control search rank.
 
 ```json
 "@odata.count": 19,
@@ -269,7 +269,7 @@ Response for the above query matches on 19 hotels that offer free amenities. Not
 
 Range filtering is supported through filters expressions for any data type. The following examples illustrate numeric and string ranges. Data types are important in range filters and work best when numeric data is in numeric fields, and string data in string fields. Numeric data in string fields isn't suitable for ranges because numeric strings aren't comparable.
 
-The following query is a numeric range. In hotels-sample-index, the only filterable numeric field is Rating.
+The following query is a numeric range. In hotels-sample-index, the only filterable numeric field is `Rating`.
 
 ```http
 POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
@@ -282,7 +282,7 @@ POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
 }
 ```
 
-Response for this query should look similar to the following example, trimmed for brevity.
+The response for this query should look similar to the following example, trimmed for brevity.
 
 ```json
 "@odata.count": 27,
@@ -320,7 +320,7 @@ POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
 }
 ```
 
-Response for this query should look similar to the example below, trimmed for brevity. In this example, it's not possible to sort by StateProvince because the field isn't attributed as "sortable" in the index definition.
+The response for this query should look similar to the following example, trimmed for brevity. In this example, it's not possible to sort by `StateProvince` because the field isn't attributed as *sortable* in the index definition.
 
 ```json
 "@odata.count": 9,
@@ -354,7 +354,7 @@ Response for this query should look similar to the example below, trimmed for br
 
 ## Example 6: Geospatial search
 
-The hotels-sample index includes a Location field with latitude and longitude coordinates. This example uses the [geo.distance function](search-query-odata-geo-spatial-functions.md#examples) that filters on documents within the circumference of a starting point, out to an arbitrary distance (in kilometers) that you provide. You can adjust the last value in the query (10) to reduce or enlarge the surface area of the query.
+The hotels-sample-index includes a *Location* field with latitude and longitude coordinates. This example uses the [geo.distance function](search-query-odata-geo-spatial-functions.md#examples) that filters on documents within the circumference of a starting point, out to an arbitrary distance (in kilometers) that you provide. You can adjust the last value in the query (10) to reduce or enlarge the surface area of the query.
 
 ```http
 POST /indexes/v/docs/search?api-version=2024-07-01
@@ -366,7 +366,7 @@ POST /indexes/v/docs/search?api-version=2024-07-01
 }
 ```
 
-Response for this query returns all hotels within a 10 kilometer distance of the coordinates provided:
+The response for this query returns all hotels within a 10-kilometer distance of the coordinates provided:
 
 ```json
 {
@@ -405,15 +405,15 @@ Response for this query returns all hotels within a 10 kilometer distance of the
 
 ## Example 7: Booleans with searchMode
 
-Simple syntax supports boolean operators in the form of characters (`+, -, |`) to support AND, OR, and NOT query logic. Boolean search behaves as you might expect, with a few noteworthy exceptions. 
+Simple syntax supports Boolean operators in the form of characters (`+, -, |`) to support AND, OR, and NOT query logic. Boolean search behaves as you might expect, with a few noteworthy exceptions. 
 
-In previous examples, the `searchMode` parameter was introduced as a mechanism for influencing precision and recall, with `"searchMode": "any"` favoring recall (a document that satisfies any of the criteria is considered a match), and "searchMode=all" favoring precision (all criteria must be matched in a document). 
+In previous examples, the `searchMode` parameter was introduced as a mechanism for influencing precision and recall, with `"searchMode": "any"` favoring recall (a document that satisfies any of the criteria is considered a match), and `"searchMode": "all"` favoring precision (all criteria must be matched in a document). 
 
-In the context of a Boolean search, the default `"searchMode": "any"` can be confusing if you're stacking a query with multiple operators and getting broader instead of narrower results. This is particularly true with NOT, where results include all documents "not containing" a specific term or phrase.
+In the context of a Boolean search, the default `"searchMode": "any"` can be confusing if you're stacking a query with multiple operators and getting broader instead of narrower results. This is particularly true with NOT, where results include all documents *not containing* a specific term or phrase.
 
-The following example provides an illustration. Running the following query with searchMode (any), 42 documents are returned: those containing the term "restaurant", plus all documents that don't have the phrase "air conditioning". 
+The following example provides an illustration. Running the following query with searchMode (any), 42 documents are returned: those containing the term *restaurant*, plus all documents that don't have the phrase *air conditioning. 
 
-Notice that there's no space between the boolean operator (`-`) and the phrase "air conditioning".
+Notice that there's no space between the boolean operator (`-`) and the phrase *air conditioning*. The quotation marks are escaped (`\"`).
 
 ```http
 POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
@@ -426,9 +426,9 @@ POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
 }
 ```
 
-Changing to `"searchMode": "all"` enforces a cumulative effect on criteria and returns a smaller result set (7 matches) consisting of documents containing the term "restaurant", minus those containing the phrase "air conditioning".
+Changing to `"searchMode": "all"` enforces a cumulative effect on criteria and returns a smaller result set (seven matches) consisting of documents containing the term *restaurant*, minus those containing the phrase *air conditioning*.
 
-Response for this query would now look similar to the following example, trimmed for brevity.
+The response for this query would now look similar to the following example, trimmed for brevity.
 
 ```json
 "@odata.count": 7,
@@ -462,7 +462,7 @@ In previous examples, you learned about parameters that affect search results co
 
 By default, a search service returns the top 50 matches. To control the number of matches in each page, use `top` to define the size of the batch, and then use `skip` to pick up subsequent batches.
 
-The following example uses a filter and sort order on the Rating field (Rating is both filterable and sortable) because it's easier to see the effects of paging on sorted results. In a regular full search query, the top matches are ranked and paged by `@search.score`.
+The following example uses a filter and sort order on the `Rating` field (Rating is both filterable and sortable) because it's easier to see the effects of paging on sorted results. In a regular full search query, the top matches are ranked and paged by `@search.score`.
 
 ```http
 POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
@@ -476,9 +476,9 @@ POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
 }
 ```
 
-The query finds 21 matching documents, but because you specified `top`, the response returns just the top five matches, with ratings starting at 4.9, and ending at 4.7 with "Lady of the Lake B & B". 
+The query finds 21 matching documents, but because you specified `top`, the response returns just the top five matches, with ratings starting at 4.9, and ending at 4.7 with *Lady of the Lake B & B*. 
 
-To get the next 5, skip the first batch:
+To get the next five, skip the first batch:
 
 ```http
 POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
@@ -493,7 +493,7 @@ POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
 }
 ```
 
-The response for the second batch skips the first five matches, returning the next five, starting with "Pull'r Inn Motel". To continue with more batches, you would keep `top` at 5, and then increment `skip` by 5 on each new request (skip=5, skip=10, skip=15, and so forth).
+The response for the second batch skips the first five matches, returning the next five, starting with *Pull'r Inn Motel*. To continue with more batches, you would keep `top` at five, and then increment `skip` by five on each new request (skip=5, skip=10, skip=15, and so forth).
 
 ```json
 "value": [
@@ -525,16 +525,16 @@ The response for the second batch skips the first five matches, returning the ne
 ]
 ```
 
-## Next steps
+## Related content
 
 Now that you have some practice with the basic query syntax, try specifying queries in code. The following link covers how to set up search queries using the Azure SDKs.
 
 + [Quickstart: Full text search using the Azure SDKs](search-get-started-text.md)
 
 More syntax reference, query architecture, and examples can be found in the following links:
 
-+ [Lucene syntax query examples for building advanced queries](search-query-lucene-examples.md)
-+ [How full text search works in Azure AI Search](search-lucene-query-architecture.md)
-+ [Simple query syntax](query-simple-syntax.md)
-+ [Full Lucene query syntax](query-lucene-syntax.md)
-+ [Filter syntax](search-query-odata-filter.md)
++ [Examples of full Lucene search syntax](search-query-lucene-examples.md)
++ [Full text search in Azure AI Search](search-lucene-query-architecture.md)
++ [Simple query syntax in Azure AI Search](query-simple-syntax.md)
++ [Lucene query syntax in Azure AI Search](query-lucene-syntax.md)
++ [OData $filter syntax in Azure AI Search](search-query-odata-filter.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "単純検索構文の例に関するドキュメントの更新"
}
```

### Explanation
この変更は、`articles/search/search-query-simple-examples.md`ファイルの内容を更新したもので、単純検索構文に関連するクエリの使い方を説明しています。具体的な改訂には、説明文の表現の見直しや日付の変更（「01/17/2024」から「10/24/2024」）が含まれています。

主な更新点として、クエリの構文や使用例に関する情報をより明確にした点があります。例えば、検索されるキーワードやフレーズが例示され、検索の精度や再現性についての説明が強化されています。また、元々の内容から不必要な表現を解消し、意味が明確になるようにしています。

この改訂によって、利用者はAzure AI Searchの単純検索機能をよりよく理解でき、具体的なクエリーを通じてその手順を追いやすくなっています。全体として、ドキュメントの可読性と正確性が向上し、特に新しいユーザーにとっては、この情報が役立つものとなるでしょう。

## articles/search/search-security-get-encryption-keys.md{#item-7aed9d}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ Objects that aren't encrypted with a customer-managed key have an empty **encryp
    "keyVaultKeyName":"myEncryptionKey",
    "keyVaultKeyVersion":"eaab6a663d59439ebb95ce2fe7d5f660",
    "accessCredentials":{
-      "applicationId":"00000000-0000-0000-0000-000000000000",
+      "applicationId":"00001111-aaaa-2222-bbbb-3333cccc4444",
       "applicationSecret":"myApplicationSecret"
    }
 }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "暗号化キー取得に関するドキュメントの小変更"
}
```

### Explanation
この変更は、`articles/search/search-security-get-encryption-keys.md`ファイルの内容を修正したもので、特にサンプルコードにおける暗号化キーの取り扱いに関連しています。具体的には、一部のオブジェクトの`applicationId`が、新しいUUID（"00001111-aaaa-2222-bbbb-3333cccc4444"）に変更されました。これにより、実際のアプリケーションの識別子を示すための例が更新され、利用者にとってより具体的でわかりやすい内容となっています。

変更はわずかであり、全体の内容や機能には大きな影響はないものの、サンプルが実際のセキュリティ設定を反映するように改善されています。この小さな更新により、ドキュメントはより正確で有用な情報源となります。利用者はこの新しい情報を通じて、暗号化キーの管理と使用に関するベストプラクティスを理解しやすくなるでしょう。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 10/17/2024
+ms.date: 10/25/2024
 
 ---
 
@@ -70,9 +70,10 @@ Currently, several regions are at capacity for specific tiers and can't be used
 
 Most features are available on all tiers, including the free tier. In a few cases, the tier determines the availability of a feature. The following table describes the constraints.
 
-| Feature | Limitations |
-|---------|-------------|
+| Feature | Tier considerations |
+|---------|---------------------|
 | [indexers](search-indexer-overview.md) | Indexers aren't available on S3 HD. Indexers have [more limitations](search-limits-quotas-capacity.md#indexer-limits) on the free tier. |
+| [indexer `executionEnvironment` configuration parameter](search-how-to-create-indexers.md?tabs=indexer-rest#create-an-indexer) | The ability to pin all indexer processing to just the search clusters allocated to your search service requires S2 and higher. |
 | [AI enrichment](cognitive-search-concept-intro.md) | Runs on the Free tier but not recommended. |
 | [Managed or trusted identities for outbound (indexer) access](search-howto-managed-identities-data-sources.md) | Not available on the Free tier.|
 | [Customer-managed encryption keys](search-security-manage-encryption-keys.md) | Not available on the Free tier. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SKUティアに関するドキュメントの更新"
}
```

### Explanation
この変更は、`articles/search/search-sku-tier.md`ファイルの内容を更新したもので、具体的には、SKUティアに関連する機能の制約に関する情報を整理しています。主な改訂点は表のヘッダーの変更で、「Limitations」という表現を「Tier considerations」に変更し、各機能の説明に対してより明確な文脈を提供しています。

さらに、日付が「10/17/2024」から「10/25/2024」に更新され、最新の情報を反映しています。表の内容には、インデクサーの利用可能性や特定の機能に対する制約の詳細が記載されており、特にフリーティアで使用できない機能や制限についての情報が強調されています。

この改訂により、Azure AI SearchのSKUティアに関する情報がわかりやすく整理されており、ユーザーが各ティアの機能と制約について直感的に理解しやすくなっています。全体として、ドキュメントのクリアさと使いやすさが向上しており、特にサービスを選択する際の参考になるでしょう。

## articles/search/search-try-for-free.md{#item-36e28d}

<details>
<summary>Diff</summary>
````diff
@@ -122,9 +122,9 @@ Try the portal quickstarts for Azure AI Search or quickstarts that use Visual St
 - [Quickstart: Generative search (RAG) using a Python client](search-get-started-rag.md)
 - [Quickstart: Vector search using a REST client](search-get-started-vector.md)
 
-Azure AI Studio and Azure OpenAI Studio support connecting to content in Azure AI Search
+Azure AI Studio supports connecting to content in Azure AI Search.
 
-- [Quickstart: Chat using your own data in Azure OpenAI Studio](/azure/ai-services/openai/use-your-data-quickstart)
+- [Quickstart: Chat using your own data with Azure OpenAI](/azure/ai-services/openai/use-your-data-quickstart)
 - [Tutorial: Build a custom chat app with the prompt flow SDK](/azure/ai-studio/tutorials/copilot-sdk-create-resources)
 
 Developers should review [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) repository or the solution accelerators. You can deploy and run any of these samples using the Azure trial subscription. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchを試すためのドキュメントの修正"
}
```

### Explanation
この変更は、`articles/search/search-try-for-free.md`ファイルに対するもので、Azure AI Searchを無料で試すための情報を提供しています。主な修正点として、文言の微調整が行われています。具体的には、Azure AI StudioがAzure AI Searchのコンテンツに接続できる旨がより明確に記されています。また、関連するクイックスタートのリンクの表記も若干変更されています。

特に、Azure OpenAI Studio に関連する文言が「Azure OpenAI Studio」から「Azure OpenAI」に変更され、表現の統一が図られています。この改訂により、読者はAzure AI Searchと関連するリソースにアクセスする方法がより明確に理解できるようになっており、プロダクトに対する理解が深まることを目的としています。

全体として、文書のクリアさが向上し、海部的にサービスを試すためのガイダンスが的確に伝わるようになっています。これにより、開発者やユーザーがAzure AI Searchの機能を効率的に利用できるよう、情報が整理されています。

## articles/search/service-configure-firewall.md{#item-75be3f}

<details>
<summary>Diff</summary>
````diff
@@ -133,7 +133,7 @@ The trusted service list for Azure AI Search includes:
 + `Microsoft.CognitiveServices` for Azure OpenAI and Azure AI services
 + `Microsoft.MachineLearningServices` for Azure Machine Learning
 
-Workflows for this network exception are requests originating *from* Azure AI Studio, Azure OpenAI Studio, or other AML features *to* Azure AI Search, typically in [Azure OpenAI On Your Data](/azure/ai-services/openai/concepts/use-your-data) scenarios for retrieval augmented generation (RAG) and playground environments.
+Workflows for this network exception are requests originating from Azure AI Studio or other AML features to Azure AI Search. The trusted services exception is typically for [Azure OpenAI On Your Data](/azure/ai-services/openai/concepts/use-your-data) scenarios for retrieval augmented generation (RAG) and playground environments.
 
 ### Trusted resources must have a managed identity
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイアウォール構成に関するドキュメントの修正"
}
```

### Explanation
この変更は、`articles/search/service-configure-firewall.md`ファイルに対するもので、Azure AI Searchのファイアウォール設定に関する内容を明確化しています。具体的には、ネットワーク例外に関する説明文が修正されました。

修正された部分では、リクエストがどこから来るのか、及びその目的が再整理され、より簡潔に述べられるようになりました。「Azure AI Studio、Azure OpenAI Studio、または他のAML（Azure Machine Learning）機能からAzure AI Searchへのリクエスト」という文が簡素化され、Azure AI Studioと他のAML機能からのリクエストに焦点が当てられています。

この改訂により、文書がより読みやすくなり、具体的なシナリオや使用例が明確に理解できるようになっています。結果として、ユーザーがファイアウォール設定を行う際の理解が深まり、必要な情報を迅速に見つける手助けが強化されています。

## articles/search/service-create-private-endpoint.md{#item-65e817}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ This article explains how to configure a private connection to Azure AI Search s
 + [Create an Azure virtual machine in the same virtual network](#create-a-virtual-machine)
 + [Test using a browser session on the virtual machine](#connect-to-the-vm)
 
-Other Azure resources that might privately connect to Azure AI Search include Azure OpenAI for "use your own data" scenarios. Azure OpenAI Studio doesn't run in a virtual network, but it can be configured on the backend to send requests over the Microsoft backbone network. Configuration for this traffic pattern is enabled by Microsoft when your request is submitted and approved. For this scenario:
+Other Azure resources that might privately connect to Azure AI Search include Azure OpenAI for "use your own data" scenarios. Azure AI Studio doesn't run in a virtual network, but it can be configured on the backend to send requests over the Microsoft backbone network. Configuration for this traffic pattern is enabled by Microsoft when your request is submitted and approved. For this scenario:
 
 + Follow the instructions in this article to set up the private endpoint.
 + [Enable trusted service](/azure/ai-services/openai/how-to/use-your-data-securely#enable-trusted-service-1) of your search resource from the Azure portal.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートエンドポイントの作成に関するドキュメントの修正"
}
```

### Explanation
この変更は、`articles/search/service-create-private-endpoint.md`ファイルに対するもので、Azure AI Searchへのプライベート接続の設定に関する説明を更新しています。主な修正は、文言の調整と重要な情報の追加に焦点を当てています。

具体的には、Azure AI Studioに関する説明が少し明確化され、Azure OpenAI StudioではなくAzure AI Studioという名称が使用されています。この変更により、リソースの呼称が一致し、混乱を避ける目的があります。

さらに、プライベートエンドポイントの設定方法を示す手順が追加され、ユーザーがAzureポータルからの「信頼されたサービス」の有効化に関するリンクも示されています。このリンクは、プライベート接続を行う際に必要な追加の設定手順に誘導するものであり、全体的な理解を補完する内容となっています。

この改訂により、ユーザーはAzure AI Searchにプライベートエンドポイントを簡単に設定できる方法をよりよく理解でき、必要な手順が明確に示されています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -228,7 +228,7 @@ items:
     - name: Alias an index
       href: search-how-to-alias.md
     - name: Import large data sets
-      href: search-howto-large-index.md
+      href: search-how-to-large-index.md
     - name: Indexers
       items:
       - name: Create an indexer
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCファイルの修正"
}
```

### Explanation
この変更は、`articles/search/toc.yml`ファイルにおける小さな修正です。このファイルは、Azure AI Searchに関するドキュメントの目次を定義しています。具体的には、リンクの整形を行ったもので、ページのナビゲーションをより一貫性のあるものにすることが目的です。

具体的には、「大規模データセットのインポート」に対応するリンクが修正されました。具体的には、元のリンク名`search-howto-large-index.md`が正しい形式である`search-how-to-large-index.md`に変更されました。この整形により、リンクが正しく機能し、ユーザーがドキュメント内で必要な情報にスムーズにアクセスできるようになります。

この微修正により、ドキュメント全体の整合性が向上し、ユーザー体験が改善されることが期待されます。リンクが適切に設定されることで、情報の検索が容易になり、ユーザーの利便性が高まります。

## articles/search/tutorial-rag-build-solution-models.md{#item-6796c9}

<details>
<summary>Diff</summary>
````diff
@@ -2,14 +2,13 @@
 title: 'RAG tutorial: Set up models'
 titleSuffix: Azure AI Search
 description: Set up an embedding model and chat model for generative search (RAG).
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: tutorial
 ms.custom: references_regions
-ms.date: 10/04/2024
+ms.date: 10/25/2024
 
 ---
 
@@ -34,7 +33,7 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 
 - An **Owner** or **User Access Administrator** role on your Azure subscription, necessary for creating role assignments. You use at least three Azure resources in this tutorial. The connections are authenticated using Microsoft Entra ID, which requires the ability to create roles. Role assignments for connecting to models are documented in this article. If you can't create roles, you can use [API keys](search-security-api-keys.md) instead.
 
-- A model provider, such as [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource), Azure AI Vision via an [Azure AI multi-service account](/azure/ai-services/multi-service-resource), or [Azure AI Studio](https://ai.azure.com/).
+- A model provider, such as [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource), Azure AI Vision via an [Azure AI services multi-service resource](/azure/ai-services/multi-service-resource), or [Azure AI Studio](https://ai.azure.com/).
 
   We use Azure OpenAI in this tutorial. Other providers are listed so that you know your options for integrated vectorization.
 
@@ -103,7 +102,7 @@ This tutorial series uses the following models and model providers:
 
 You must have [**Cognitive Services OpenAI Contributor**]( /azure/ai-services/openai/how-to/role-based-access-control#cognitive-services-openai-contributor) or higher to deploy models in Azure OpenAI.
 
-1. Go to [Azure OpenAI Studio](https://oai.azure.com/).
+1. Go to [Azure AI Studio](https://ai.azure.com/).
 
 1. Select **Deployments** on the left menu.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGチュートリアルの更新"
}
```

### Explanation
この変更は、`articles/search/tutorial-rag-build-solution-models.md`ファイルに対して行われたもので、RAG（Retrieval-Augmented Generation）に関するチュートリアルの内容を更新しています。更新の内容としては、いくつかの項目の修正と日付の変更が含まれています。

具体的には、以下の修正が行われました：

1. **日付の更新**: 最終更新日が`10/04/2024`から`10/25/2024`に変更されました。これにより、ユーザーは最新の情報を反映していることを容易に確認できるようになります。

2. **表現の変更**: 「Azure AI multi-service account」という表記が「Azure AI services multi-service resource」に変更されています。この修正により、用語がより一貫性のあるものになり、誤解を招かないように配慮されています。

3. **リンクの確認と修正**: 手順内において、`Azure OpenAI Studio`のリンクが`Azure AI Studio`に変更されています。この修正により、正しいリソースの名前が使用され、ユーザーが正確にリソースにアクセスできるようになっています。

これらの修正は、チュートリアルの実用性を向上させ、ユーザーが求める情報へアクセスしやすくすることを目的としています。全体として、文書が最新の状況に即したものとなり、正確性が高まっています。

## articles/search/vector-search-how-to-configure-compression-storage.md{#item-c653c3}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.date: 10/01/2024
 
 # Reduce vector size through quantization, narrow data types, and storage options
 
-This article explains how to use vector quantization and other techniques for reducing vector size in Azure AI Search. The search index specifies vector field definitions, including properties used to specify narrow data types or control whether a copy of vector content is retained for search results. Quantization is also specified in the index and assigned to vector field through its vector profile. 
+This article explains how to use vector quantization and other techniques for reducing vector size in Azure AI Search. The search index specifies vector field definitions, including properties used to specify narrow data types or control whether a copy of vector content is retained for search results. Quantization is also specified in the index and assigned to vector field through its vector profile.
 
 Most of the features described in this article are generally available in [2024-07-01 REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-07-01&preserve-view=true) and in the Azure SDK packages targeting that version. The [latest preview version](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-09-01-preview&preserve-view=true) adds support for truncated dimensions if you're using text-embedding-3-large or text-embedding-3-small for vectorization.
 
@@ -39,7 +39,7 @@ After the index is defined, you can load and index documents as a separate step.
 
 Quantization is recommended for reducing vector size because it lowers both memory and disk storage requirements for float16 and float32 embeddings. To offset the effects of a smaller index, you can add oversampling and reranking over uncompressed vectors.
 
-Quantization applies to vector fields receiving float-type vectors. In the examples in this article, the field's data type is `Collection(Edm.Single)` for incoming float32 embeddings, but float16 is also supported. When the vectors are received on a field with compression configured, the engine automatically performs quantization to reduce the footprint of the vector data in memory and on disk. 
+Quantization applies to vector fields receiving float-type vectors. In the examples in this article, the field's data type is `Collection(Edm.Single)` for incoming float32 embeddings, but float16 is also supported. When the vectors are received on a field with compression configured, the engine automatically performs quantization to reduce the footprint of the vector data in memory and on disk.
 
 Two types of quantization are supported:
 
@@ -50,7 +50,7 @@ Two types of quantization are supported:
 To use built-in quantization, follow these steps:
 
 > [!div class="checklist"]
-> - Use [Create Index](/rest/api/searchservice/indexes/create) or [Create Or Update Index](/rest/api/searchservice/indexes/create-or-update) to specify vector compression 
+> - Use [Create Index](/rest/api/searchservice/indexes/create) or [Create Or Update Index](/rest/api/searchservice/indexes/create-or-update) to specify vector compression
 > - Add `vectorSearch.compressions` to a search index
 > - Add a `scalarQuantization` or `binaryQuantization` configuration and give it a name
 > - Set optional properties to mitigate the effects of lossy indexing
@@ -61,7 +61,7 @@ To use built-in quantization, follow these steps:
 
 ### Add "compressions" to a search index
 
-The following example shows a partial index definition with a fields collection that includes a vector field, and a `vectorSearch.compressions` section. 
+The following example shows a partial index definition with a fields collection that includes a vector field, and a `vectorSearch.compressions` section.
 
 This example includes both `scalarQuantization` or `binaryQuantization`. You can specify as many compression configurations as you need, and then assign the ones you want to a vector profile.
 
@@ -159,9 +159,9 @@ To use a new quantization configuration, you must create a *new* vector profile.
    }
    ```
 
-1. Assign a vector profile to a *new* vector field. The data type of the field is either float32 or float16. 
+1. Assign a vector profile to a *new* vector field. The data type of the field is either float32 or float16.
 
-   In Azure AI Search, the Entity Data Model (EDM) equivalents of float32 and float16 types are `Collection(Edm.Single)` and `Collection(Edm.Half)`, respectively. 
+   In Azure AI Search, the Entity Data Model (EDM) equivalents of float32 and float16 types are `Collection(Edm.Single)` and `Collection(Edm.Half)`, respectively.
 
    ```json
    {
@@ -180,17 +180,17 @@ To use a new quantization configuration, you must create a *new* vector profile.
 
 Scalar quantization reduces the resolution of each number within each vector embedding. Instead of describing each number as a 16-bit or 32-bit floating point number, it uses an 8-bit integer. It identifies a range of numbers (typically 99th percentile minimum and maximum) and divides them into a finite number of levels or bin, assigning each bin an identifier. In 8-bit scalar quantization, there are 2^8, or 256, possible bins.
 
-Each component of the vector is mapped to the closest representative value within this set of quantization levels in a process akin to rounding a real number to the nearest integer. In the quantized 8-bit vector, the identifier number stands in place of the original value. After quantization, each vector is represented by an array of identifiers for the bins to which its components belong. These quantized vectors require much fewer bits to store compared to the original vector, thus reducing storage requirements and memory footprint. 
+Each component of the vector is mapped to the closest representative value within this set of quantization levels in a process akin to rounding a real number to the nearest integer. In the quantized 8-bit vector, the identifier number stands in place of the original value. After quantization, each vector is represented by an array of identifiers for the bins to which its components belong. These quantized vectors require much fewer bits to store compared to the original vector, thus reducing storage requirements and memory footprint.
 
 ### How  binary quantization works in Azure AI Search
 
 Binary quantization compresses high-dimensional vectors by representing each component as a single bit, either 0 or 1. This method drastically reduces the memory footprint and accelerates vector comparison operations, which are crucial for search and retrieval tasks. Benchmark tests show up to 96% reduction in vector index size.
 
-It's particularly effective for embeddings with dimensions greater than 1024. For smaller dimensions, we recommend testing the quality of binary quantization, or trying scalar instead. Additionally, we’ve found BQ performs very well when embeddings are centered around zero. Most popular embedding models such as OpenAI, Cohere, and Mistral are centered around zero. 
+It's particularly effective for embeddings with dimensions greater than 1024. For smaller dimensions, we recommend testing the quality of binary quantization, or trying scalar instead. Additionally, we’ve found BQ performs very well when embeddings are centered around zero. Most popular embedding models such as OpenAI, Cohere, and Mistral are centered around zero.
 
 ### Use MRL compression and truncated dimensions (preview)
 
-MRL multilevel compression saves on vector storage and improves query response times for vector queries based on text embeddings. In Azure AI Search, MRL support is only offered together with another method of quantization. Using binary quantization with MRL provides the maximum vector index size reduction. To achieve maximum storage reduction, use binary quantization with MRL, and `stored` set to false. 
+MRL multilevel compression saves on vector storage and improves query response times for vector queries based on text embeddings. In Azure AI Search, MRL support is only offered together with another method of quantization. Using binary quantization with MRL provides the maximum vector index size reduction. To achieve maximum storage reduction, use binary quantization with MRL, and `stored` set to false.
 
 This feature is in preview. It's available in `2024-09-01-preview` and in beta SDK packages targeting that preview API version.
 
@@ -203,10 +203,10 @@ This feature is in preview. It's available in `2024-09-01-preview` and in beta S
 
 #### Supported clients
 
-- [REST API 2024-09-01-preview](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) 
-- Check the change logs for each Azure SDK beta package: [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md), [Java](https://github.com/Azure/azure-sdk-for-java/blob/azure-search-documents_11.1.3/sdk/search/azure-search-documents/CHANGELOG.md), [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md). 
+- [REST API 2024-09-01-preview](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true)
+- Check the change logs for each Azure SDK beta package: [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md), [Java](https://github.com/Azure/azure-sdk-for-java/blob/azure-search-documents_11.1.3/sdk/search/azure-search-documents/CHANGELOG.md), [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md).
 
-There's no Azure portal or Azure AI Studio support at this time. 
+There's no Azure portal or Azure AI Studio support at this time.
 
 #### How to use MRL-extended text embeddings
 
@@ -224,11 +224,10 @@ Indexing is slower due to the extra steps, but queries will be faster.
 
 #### Example of a vector search configuration that supports MRL
 
-The following example illustrates a vector search configuration that meets the requirements and recommendations of MRL. 
+The following example illustrates a vector search configuration that meets the requirements and recommendations of MRL.
 
 `truncationDimension` is a compression property. It specifies how much to shrink the vector graph in memory in conjunction with a compression method like scalar or binary compression. We recommend 1,024 or higher for `truncationDimension` with binary quantization. A dimensionality of less than 1,000 degrades the quality of search results when using MRL and binary compression.
 
-
 ```json
 { 
   "vectorSearch": { 
@@ -270,7 +269,7 @@ The following example illustrates a vector search configuration that meets the r
 } 
 ```
 
-Here's an example of a [fully specified vector field definition](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true#searchfield) that satisfies the requirements for MRL. 
+Here's an example of a [fully specified vector field definition](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true#searchfield) that satisfies the requirements for MRL.
 
 Recall that vector fields must be of type `Edm.Half` or `Edm.Single`. Vector fields must have a `vectorSearchProfile` property that determines the algorithm and compression settings. Vector fields have a `dimensions` property used for specifying the number of dimensions for scoring and ranking results. Its value should be dimensions limit of the model you're using (1,536 for text-embedding-3-small).
 
@@ -343,7 +342,7 @@ Considerations for setting `stored` to false:
 
 - Because vectors aren't human readable, you can omit them from results sent to LLMs in RAG scenarios, and from results that are rendered on a search page. Keep them, however, if you're using vectors in a downstream process that consumes vector content.
 
-- However, if your indexing strategy includes [partial document updates](search-howto-reindex.md#update-content), such as "merge" or "mergeOrUpload" on a document, be aware that setting `stored` to false will cause vectors in the non-stored field to be omitted during the merge. On each "merge" or "mergeOrUpload" operation, you must provide the vector fields in addition to other nonvector fields that you're updating, or the vector will be dropped. 
+- However, if your indexing strategy includes [partial document updates](search-howto-reindex.md#update-content), such as "merge" or "mergeOrUpload" on a document, be aware that setting `stored` to false will cause vectors in the non-stored field to be omitted during the merge. On each "merge" or "mergeOrUpload" operation, you must provide the vector fields in addition to other nonvector fields that you're updating, or the vector will be dropped.
 
 Remember that the `stored` attribution is irreversible. It's set during index creation on vector fields when physical data structures are created. If you want retrievable vector content later, you must drop and rebuild the index, or create and load a new field that has the new attribution.
 
@@ -381,7 +380,7 @@ The following example shows the fields collection of a search index. Set `stored
 
 ## Example: vector compression techniques
 
-Here's Python code that demonstrates quantization, narrow data types, and use of the stored property: [Code sample: Vector quantization and storage options using Python](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/vector-quantization-and-storage/README.md). 
+Here's Python code that demonstrates quantization, narrow data types, and use of the stored property: [Code sample: Vector quantization and storage options using Python](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/vector-quantization-and-storage/README.md).
 
 This code creates and compares storage and vector index size for each option:
 
@@ -446,4 +445,4 @@ POST https://[service-name].search.windows.net/indexes/demo-index/docs/search?ap
 
 - [Get started with REST](search-get-started-rest.md)
 - [Supported data types](/rest/api/searchservice/supported-data-types)
-- [Search REST APIs](/rest/api/searchservice/)
\ No newline at end of file
+- [Search REST APIs](/rest/api/searchservice/)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクター検索の圧縮ストレージ設定に関する記事の更新"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-configure-compression-storage.md`ファイルに対するもので、Azure AI Searchのベクター検索に関連する圧縮ストレージの設定方法についての情報を更新しています。変更の主な内容は、文章の修正や重複の削除、重要な技術的情報の明確化を含んでいます。

具体的には、以下の主要な修正が行われました：

1. **文章の調整**: 一部の文から無駄な改行を削除し、記述を統一しました。例えば、ベクター圧縮と量子化のプロセスに関する説明に無駄な空白を排除することで、読みやすさが向上しています。

2. **技術的詳細の明確化**: 記事内で説明されている圧縮手法や量子化の実装方法がより具体的に述べられています。これにより、ユーザーは正確な情報をもとに設定を行うことができるようになります。

3. **サンプルコードの参照の更新**: サンプルコードやAPIに関する参照リンクが更新され、最新の情報に基づいてユーザーが実装を行いやすくなっています。

4. **APIバージョンの指定**: 新しいAPIバージョンが強調され、ユーザーがどのバージョンを参照すべきかが明示されています。

これらの修正は、ユーザー体験を向上させることを目的としており、特にベクター検索の設定や圧縮方法を学びたいユーザーにとって有益な内容となっています。全体として、文書は最新の情報で更新され、正確性と実用性が高められています。

## articles/search/vector-search-integrated-vectorization.md{#item-48219d}

<details>
<summary>Diff</summary>
````diff
@@ -63,7 +63,7 @@ For text-to-vector conversion during queries, you take a dependency on these com
     | [AzureOpenAIEmbedding skill](cognitive-search-skill-azure-openai-embedding.md) | [Azure OpenAI vectorizer](vector-search-vectorizer-azure-open-ai.md) |
     | [Custom skill](cognitive-search-custom-skill-web-api.md) | [Custom Web API vectorizer](vector-search-vectorizer-custom-web-api.md) |
     | [Azure AI Vision skill (preview)](cognitive-search-skill-vision-vectorize.md)  | [Azure AI Vision vectorizer](vector-search-vectorizer-ai-services-vision.md) |
-    | [AML skill pointing to the model catalog in Azure AI Studio (preview)](cognitive-search-aml-skill.md) | [Azure AI Studio model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) |
+    | [AML skill pointing to the model catalog in Azure AI Studio](cognitive-search-aml-skill.md) | [Azure AI Studio model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) |
 
 ## Component diagram
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "統合ベクター化に関する記事の微修正"
}
```

### Explanation
この変更は、`articles/search/vector-search-integrated-vectorization.md`ファイルに対して行われたもので、Azure AI Searchにおける統合ベクター化の方法についての情報を微修正しています。具体的には、表形式のコンテンツ内でのリンクの記述が修正されています。

主な修正点は以下の通りです：

1. **リンクの調整**: `AML skill pointing to the model catalog in Azure AI Studio (preview)`という説明から「(preview)」の表記が削除されました。この変更により、コンテンツが一貫性を持ち、混乱を招かないようにしています。

2. **テキスト整理**: 表のフォーマットを整えることで、情報の可読性が向上しています。特に、関連するスキルとベクターライザーの関係を明確に示しています。

この更新により、ユーザーは統合ベクター化のコンポーネントを理解しやすくなり、作業を進める上での参考とすることができるようになります。全体としては、ドキュメントの内容がクリアに保たれ、最新の情報に基づいて更新されています。

## articles/search/vector-search-overview.md{#item-56e5fa}

<details>
<summary>Diff</summary>
````diff
@@ -74,7 +74,7 @@ Vector search is available in:
 + [Azure portal: Import and vectorize data wizard](search-get-started-portal-import-vectors.md)
 + [Azure REST APIs](/rest/api/searchservice/operation-groups)
 + [Azure SDKs for .NET](https://www.nuget.org/packages/Azure.Search.Documents), [Python](https://pypi.org/project/azure-search-documents), and [JavaScript](https://www.npmjs.com/package/@azure/search-documents)
-+ Other Azure offerings such as Azure AI Studio and Azure OpenAI Studio.
++ Other Azure offerings such as Azure AI Studio.
 
 > [!NOTE]
 > Some older search services created before January 1, 2019 are deployed on infrastructure that doesn't support vector workloads. If you try to add a vector field to a schema and get an error, it's a result of outdated services. In this situation, you must create a new search service to try out the vector feature.
@@ -85,7 +85,7 @@ Azure AI Search is deeply integrated across the Azure AI platform. The following
 
 | Product | Integration |
 |---------|-------------|
-| Azure OpenAI Studio | In the chat with your data playground, **Add your own data** uses Azure AI Search for grounding data and conversational search. This is the easiest and fastest approach for chatting with your data. |
+| Azure AI Studio | In the chat with your data playground, **Add your own data** uses Azure AI Search for grounding data and conversational search. This is the easiest and fastest approach for chatting with your data. |
 | Azure OpenAI | Azure OpenAI provides embedding models and chat models. Demos and samples target the [text-embedding-ada-002](/azure/ai-services/openai/concepts/models#embeddings-models). We recommend Azure OpenAI for generating embeddings for text. |
 | Azure AI Services | [Image Retrieval Vectorize Image API(Preview)](/azure/ai-services/computer-vision/how-to/image-retrieval#call-the-vectorize-image-api) supports vectorization of image content. We recommend this API for generating embeddings for images. |
 | Azure data platforms: Azure Blob Storage, Azure Cosmos DB | You can use [indexers](search-indexer-overview.md) to automate data ingestion, and then use [integrated vectorization](vector-search-integrated-vectorization.md) to generate embeddings. Azure AI Search can automatically index vector data from two data sources: [Azure blob indexers](search-howto-indexing-azure-blob-storage.md) and [Azure Cosmos DB for NoSQL indexers](search-howto-index-cosmosdb.md). For more information, see [Add vector fields to a search index.](vector-search-how-to-create-index.md). |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクター検索の概要に関する記事の更新"
}
```

### Explanation
この変更は、`articles/search/vector-search-overview.md`ファイルに対するもので、Azure AI Searchのベクター検索に関連する情報の一部に微修正が加えられています。具体的には、記述内容の調整と一部のサービス名称の変更が行われています。

主な修正点は以下の通りです：

1. **サービス名称の修正**: 
   - "Azure OpenAI Studio"という名称が削除され、"Azure AI Studio"のみに修正されました。この変更により、関連情報の整合性が保たれ、混乱を避けることができます。

2. **情報の整理**: 
   - すべての関連するAzureサービスがより一貫について説明されるようになり、ユーザーがこれらのサービスの機能を理解しやすくしています。

3. **内容の一部調整**: 
   - 追加された情報がある一方で、不必要な情報は削除され、全体の読みやすさと情報の精度が向上しました。例えば、ユーザーに関連するサービスが明瞭に示されることで、自身のニーズに合ったサービスを見つけやすくなっています。

これらの変更により、ユーザーはAzure AI Searchと関連するサービスについての理解を深め、実際のアプリケーションに対する導入や活用方法を見出す手助けとなります。全体として、ドキュメントの内容がクリアで一貫性が保たれた形に改良されています。

## articles/search/vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md{#item-ebe7a3}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ ms.date: 08/05/2024
 
 The **Azure AI Studio model catalog** vectorizer connects to an embedding model that was deployed via [the Azure AI Studio model catalog](/azure/ai-studio/how-to/model-catalog) to an Azure Machine Learning endpoint. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed. 
 
-If you used integrated vectorization to create the vector arrays, the skillset should include an [AML skill pointing to the model catalog in Azure AI Studio (preview)](cognitive-search-aml-skill.md).
+If you used integrated vectorization to create the vector arrays, the skillset should include an [AML skill pointing to the model catalog in Azure AI Studio](cognitive-search-aml-skill.md).
 
 ## Vectorizer parameters
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Machine Learning AI Studioカタログのベクタイザーに関する記事の修正"
}
```

### Explanation
この変更は、`articles/search/vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md`ファイルに加えられたもので、Azure Machine Learningに関連するベクタイザーの説明に一部修正が行われています。具体的には、リンクに関する表記の調整が実施されました。

主な修正点は以下の通りです：

1. **リンク表記の簡素化**:
   - 元の記述では、「(preview)」という表現がリンクの後に付加されていましたが、これが削除され、シンプルな形式に変更されました。これにより、情報がより明確になり、非公式な状態を示す表現が排除されました。

2. **全体の内容の明確化**:
   - この変更は、特にユーザーがモデルカタログを利用する際の理解を助け、ドキュメントの整合性を高めるものです。文中に記載されたリンクがクリアになったことで、ユーザーが情報を得やすくなっています。

この微修正により、Azure AI Studioのモデルカタログへの接続に関する説明が一層スムーズになり、ユーザーにとって使いやすい情報源となることが期待されます。全体として、ドキュメントの自然な読みやすさが向上しました。


