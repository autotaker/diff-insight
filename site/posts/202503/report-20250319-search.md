---
date: '2025-03-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b32e527...MicrosoftDocs:144811f
summary: この記事では、Azure AI Search に関するいくつかの重要な更新がありました。主な変更点は、各サンプル言語に対する軽微な修正、検索クエリ処理アーキテクチャの改善、地域サポートの情報更新です。特に、検索クエリ処理アーキテクチャについては記述が再構成され、可読性が向上しました。また、「Central
  US」と「Mexico Central」の地域が新たにサポートされるようになりました。これらの変更は、ユーザーエクスペリエンスの向上を目的としており、最新の情報と明確な説明を提供することで、ユーザーがAzure
  AI Searchをより効果的に利用できるようサポートしています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b32e527...MicrosoftDocs:144811f){target="_blank"}

<format>
# Highlights
この記事では、Azure AI Search の各サンプル言語 (.NET、Java、JavaScript、Python、および REST) に対して軽微な更新が行われ、検索クエリ処理アーキテクチャについての重大な変更点も説明されます。これらの変更はドキュメントの最新性とユーザーの理解を向上させることを目的としています。

## New features
- 地域サポートに関する情報の更新により、「Central US」と「Mexico Central」の地域が追加されました。
- 検索クエリ処理アーキテクチャの改善により、情報がより明確かつ体系的に提示され、可読性が向上しています。

## Breaking changes
- 検索クエリ処理アーキテクチャに関する重大な変更が行われ、記述が改善され、情報が再構成されています。

## Other updates
- サンプルドキュメント (.NET、Java、JavaScript、Python、REST) 全般にわたり、タイトル表現の一貫性の向上、最終更新日の変更と説明文の改善が行われました。
- 地域サポートの表が更新され、内容の簡素化が実行されています。
- C# チュートリアルの記述が精緻化され、プロセス理解が容易になっています。

# Insights
このドキュメントの更新は、主にユーザーエクスペリエンスの向上を意識して行われています。特に、検索サービスを利用する読者が、最新のサンプルやチュートリアルを通じて理解を深めることができるように、表現や内容が細かく見直されました。各言語のサンプルにおいてタイトルのスタイルを統一し、可読性を向上させるという一貫した方針が示されています。

一方で、検索クエリ処理アーキテクチャに関する文書は、技術的概念の理解を深めるために大幅な改訂が行われており、特に専門的なトピックに関する内容の整理が重要な変更点です。この種の変更は、開発者がAzure AI Searchの機能をより有効に活用するための背景理解を提供する上で不可欠です。

また、地域サポートの拡充についてもリアルタイムでユーザーが求める地域の情報を提供するための迅速な対応と言えます。これにより、Azure AI Search の地理的な範囲拡大や新たな展開を確認することができます。

全体として、これらの更新により、Azure AI Search の文書がより充実し、利用者が迅速に必要な情報を得るための効率化が図られていることがわかります。この文書整形と情報精査のプロセスは、ユーザーがサービスを最大限に活用するのを助けるために非常に重要であり、常に最新の状態を保つことで、迅速な技術習得を可能にします。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [samples-dotnet.md](#item-12f3fa) | minor update | 検索用の新しい.NET サンプルの更新 | modified | 28 | 29 | 57 | 
| [samples-java.md](#item-5992fd) | minor update | Java サンプルの更新 | modified | 4 | 5 | 9 | 
| [samples-javascript.md](#item-82e67e) | minor update | JavaScript サンプルの更新 | modified | 8 | 9 | 17 | 
| [samples-python.md](#item-d2bf09) | minor update | Python サンプルの更新 | modified | 7 | 8 | 15 | 
| [samples-rest.md](#item-198ebc) | minor update | REST サンプルの更新 | modified | 10 | 11 | 21 | 
| [search-lucene-query-architecture.md](#item-b0d568) | breaking change | 検索クエリ処理アーキテクチャの更新 | modified | 74 | 76 | 150 | 
| [search-region-support.md](#item-25b0f1) | minor update | 地域サポートの更新 | modified | 4 | 2 | 6 | 
| [tutorial-multiple-data-sources.md](#item-71558f) | minor update | 複数のデータソースのインデックス作成に関するC#チュートリアルの更新 | modified | 66 | 65 | 131 | 


# Modified Contents
## articles/search/samples-dotnet.md{#item-12f3fa}

<details>
<summary>Diff</summary>
````diff
@@ -1,8 +1,7 @@
 ---
-title: .NET samples
+title: .NET Samples
 titleSuffix: Azure AI Search
 description: Find Azure AI Search demo C# code samples that use the .NET client libraries.
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
@@ -11,12 +10,12 @@ ms.custom:
   - devx-track-dotnet
   - ignite-2023
 ms.topic: concept-article
-ms.date: 10/18/2024
+ms.date: 03/10/2025
 ---
 
 # C# samples for Azure AI Search
 
-You can explore C# code samples that demonstrate the functionality and workflow of an Azure AI Search solution. These samples use the [**Azure AI Search client library**](/dotnet/api/overview/azure/search) for the [**Azure SDK for .NET**](/dotnet/azure/), which you can access through the following links.
+Learn about the C# code samples that demonstrate the functionality and workflow of an Azure AI Search solution. These samples use the [**Azure AI Search client library**](/dotnet/api/overview/azure/search) for the [**Azure SDK for .NET**](/dotnet/azure/), which you can explore through the following links.
 
 | Target | Link |
 |--------|------|
@@ -28,23 +27,23 @@ You can explore C# code samples that demonstrate the functionality and workflow
 
 ## SDK samples
 
-Code samples from the Azure SDK development team demonstrate API usage. You can find [these samples on GitHub](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/).
+Code samples from the Azure SDK development team demonstrate API usage. You can find these samples on [GitHub](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/).
 
 | Sample | Description |
 |---------|-------------|
-| [*Hello world* - synchronous](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample01a_HelloWorld.md) | Demonstrates how to create a client, authenticate, and handle errors using synchronous methods |
-| [*Hello world* - asynchronous](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample01b_HelloWorldAsync.md) | Demonstrates how to create a client, authenticate, and handle errors using asynchronous methods  |
-| [Service-level operations](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample02_Service.md) | Demonstrates how to create indexes, indexers, data sources, skillsets, and synonym maps. This sample also shows you how to get service statistics and how to query an index  |
-| [Index operations](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample03_Index.md) | Demonstrates how to perform an action on existing index, in this case getting a count of documents stored in the index  |
-| [FieldBuilderIgnore](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample04_FieldBuilderIgnore.md) | Demonstrates a technique for working with unsupported data types  |
-| [Indexing documents (push model)](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample05_IndexingDocuments.md) | *Push* model indexing, where you send a JSON payload to an index on a service  |
-| [Encryption key sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample06_EncryptedIndex.md) | Demonstrates using a customer-managed encryption key to add an extra layer of protection over sensitive content  |
-| [Vector search sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample07_VectorSearch.md) | Shows you how to index a vector field and perform vector search using the Azure SDK for .NET |
-| [Semantic ranking sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample08_SemanticSearch.md) | Shows you how to configure semantic ranker in an index and invoke semantic queries using the Azure SDK for .NET |
+| [*Hello world* - synchronous](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample01a_HelloWorld.md) | Demonstrates how to create a client, authenticate, and handle errors using synchronous methods. |
+| [*Hello world* - asynchronous](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample01b_HelloWorldAsync.md) | Demonstrates how to create a client, authenticate, and handle errors using asynchronous methods.  |
+| [Service-level operations](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample02_Service.md) | Demonstrates how to create indexes, indexers, data sources, skillsets, and synonym maps. This sample also shows you how to get service statistics and how to query an index.  |
+| [Index operations](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample03_Index.md) | Demonstrates how to perform an action on existing index, in this case getting a count of documents stored in the index.  |
+| [FieldBuilderIgnore](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample04_FieldBuilderIgnore.md) | Demonstrates a technique for working with unsupported data types.  |
+| [Indexing documents (push model)](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample05_IndexingDocuments.md) | *Push* model indexing, where you send a JSON payload to an index on a service.  |
+| [Encryption key sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample06_EncryptedIndex.md) | Demonstrates using a customer-managed encryption key to add an extra layer of protection over sensitive content.  |
+| [Vector search sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample07_VectorSearch.md) | Shows you how to index a vector field and perform vector search using the Azure SDK for .NET. |
+| [Semantic ranking sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample08_SemanticSearch.md) | Shows you how to configure semantic ranker in an index and invoke semantic queries using the Azure SDK for .NET. |
 
 ## Doc samples
 
-Code samples from the Azure AI Search team demonstrate features and workflows. All of the following samples are referenced in tutorials, quickstarts, and how-to articles that explain the code in detail. You can find these samples in [**Azure-Samples/azure-search-dotnet-samples**](https://github.com/Azure-Samples/azure-search-dotnet-samples) and in [**Azure-Samples/search-dotnet-getting-started**](https://github.com/Azure-Samples/search-dotnet-getting-started/) on GitHub.
+Code samples from the Azure AI Search team demonstrate features and workflows. All of the following samples are referenced in tutorials, quickstarts, and how-to articles that explain the code in detail. You can find these samples in [**Azure-Samples/azure-search-dotnet-samples**](https://github.com/Azure-Samples/azure-search-dotnet-samples) and [**Azure-Samples/search-dotnet-getting-started**](https://github.com/Azure-Samples/search-dotnet-getting-started/) on GitHub.
 
 > [!TIP]
 > Try the [samples browser](/samples/browse/?languages=csharp&products=azure-cognitive-search) to search for Microsoft code samples in GitHub, filtered by product, service, and language.
@@ -56,8 +55,8 @@ Code samples from the Azure AI Search team demonstrate features and workflows. A
 | [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-search/) | [Quickstart: Semantic ranking using the Azure SDKs](search-get-started-semantic.md) | Shows the index schema and query request for invoking semantic ranker. |
 | [search-website](https://github.com/Azure-Samples/azure-search-static-web-app) | [Tutorial: Add search to web apps](tutorial-csharp-overview.md) | Demonstrates an end-to-end search app that includes bulk upload using the push APIs and a rich client for hosting the app and handling search requests.|
 | [tutorial-ai-enrichment](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/tutorial-ai-enrichment)  | [Tutorial: AI-generated searchable content from Azure blobs](cognitive-search-tutorial-blob-dotnet.md) | Shows how to configure an indexer and skillset. |
-| [multiple-data-sources](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources)  | [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md). | Merges content from two data sources into one search index. |
-| [Optimize-data-indexing](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/optimize-data-indexing) | [Tutorial: Optimize indexing with the push API](tutorial-optimize-indexing-push-api.md).| Demonstrates optimization techniques for pushing data into a search index. |
+| [multiple-data-sources](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources)  | [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md) | Merges content from two data sources into one search index. |
+| [Optimize-data-indexing](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/optimize-data-indexing) | [Tutorial: Optimize indexing with the push API](tutorial-optimize-indexing-push-api.md) | Demonstrates optimization techniques for pushing data into a search index. |
 | [DotNetHowTo](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowTo)  | [How to use the .NET client library](search-howto-dotnet-sdk.md) | Steps through the basic workflow, but in more detail and with discussion of API usage.  |
 | [DotNetToIndexers](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToIndexers) | [Tutorial: Index Azure SQL data](search-indexer-tutorial.md) | Shows how to configure an Azure SQL indexer that has a schedule, field mappings, and parameters.  |
 | [DotNetHowToEncryptionUsingCMK](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToEncryptionUsingCMK)  | [How to configure customer-managed keys for data encryption](search-security-manage-encryption-keys.md) | Shows how to create objects that are encrypted with a Customer Key. |
@@ -70,28 +69,28 @@ An accelerator is an end-to-end solution that includes code and documentation th
 
 | Samples | Repository | Description |
 |---------|------------|-------------|
-| Search + QnA Maker Accelerator | [search-qna-maker-accelerator](https://github.com/Azure-Samples/search-qna-maker-accelerator)| A [solution](https://techcommunity.microsoft.com/t5/azure-ai/qna-with-azure-cognitive-search/ba-p/2081381) combining the power of Search and QnA Maker. See the live [demo site](https://aka.ms/qnaWithAzureSearchDemo) |
-| [Knowledge Mining Solution Accelerator](/shows/ai-show/knowledge-mining-with-azure-search) | [azure-search-knowledge-mining](https://github.com/azure-samples/azure-search-knowledge-mining/tree/main/) | Includes templates, support files, and analytical reports to help you prototype an end-to-end knowledge mining solution  |
+| Search + QnA Maker Accelerator | [search-qna-maker-accelerator](https://github.com/Azure-Samples/search-qna-maker-accelerator)| A [solution](https://techcommunity.microsoft.com/t5/azure-ai/qna-with-azure-cognitive-search/ba-p/2081381) combining the power of Search and QnA Maker. See the live [demo site](https://aka.ms/qnaWithAzureSearchDemo). |
+| [Knowledge Mining Solution Accelerator](/shows/ai-show/knowledge-mining-with-azure-search) | [azure-search-knowledge-mining](https://github.com/azure-samples/azure-search-knowledge-mining/tree/main/) | Includes templates, support files, and analytical reports to help you prototype an end-to-end knowledge mining solution.  |
 
 ## Demos
 
 A demo repo provides proof-of-concept source code for examples or scenarios shown in demonstrations. Demo solutions aren't designed for adaptation by customers.
 
 | Samples | Repository | Description |
 |---------|------------|-------------|
-| Covid-19 search app | [covid19search](https://github.com/liamca/covid19search) | Source code repository for the Azure AI Search based [Covid-19 Search App](https://covid19search.azurewebsites.net/) |
-| JFK demo | [AzureSearch JFK Files](https://github.com/Microsoft/AzureSearch_JFK_Files) | Learn more about the [JFK solution](https://www.microsoft.com/ai/ai-lab-jfk-files) |
+| Covid-19 search app | [covid19search](https://github.com/liamca/covid19search) | Source code repository for the Azure AI Search based [Covid-19 Search App](https://covid19search.azurewebsites.net/). |
+| JFK demo | [AzureSearch JFK Files](https://github.com/Microsoft/AzureSearch_JFK_Files) | Learn more about the [JFK solution](https://www.microsoft.com/ai/ai-lab-jfk-files). |
 
 ## Other samples
 
-The following samples are also published by the Azure AI Search team, but aren't referenced in documentation. Associated readme files provide usage instructions.
+The following samples are also published by the Azure AI Search team but aren't referenced in documentation. Associated readme files provide usage instructions.
 
 | Samples | Repository | Description |
 |---------|------------|-------------|
-| [Query multiple services](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-search-services) |  [azure-search-dotnet-scale](https://github.com/Azure-Samples/azure-search-dotnet-samples) | Issue a single query across multiple search services and combine the results into a single page  |
-| [Check storage](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/check-storage-usage/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | Invokes an Azure function that checks search service storage on a schedule |
-| [Export an index](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/export-data/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | C# console app that partitions and export a large index |
-| [Backup and restore an index](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | C# console app that copies an index from one service to another, and in the process, creates JSON files on your computer with the index schema and documents |
-| [Index Data Lake Gen2 using Microsoft Entra ID](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/data-lake-gen2-acl-indexing/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | Source code demonstrating indexer connections and indexing of Azure Data Lake Gen2 files and folders that are secured through Microsoft Entra ID and role-based access controls |
-| [Search aggregations](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/search-aggregations/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | Proof-of-concept source code that demonstrates how to obtain aggregations from a search index and then filter by them |
-| [Power Skills](https://github.com/Azure-Samples/azure-search-power-skills/blob/main/README.md) | [azure-search-power-skills](https://github.com/Azure-Samples/azure-search-power-skills)  | Source code for consumable custom skills that you can incorporate in your won solutions  |
+| [Query multiple services](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-search-services) |  [azure-search-dotnet-scale](https://github.com/Azure-Samples/azure-search-dotnet-samples) | Issue a single query across multiple search services and combine the results into a single page.  |
+| [Check storage](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/check-storage-usage/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | Invokes an Azure function that checks search service storage on a schedule. |
+| [Export an index](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/export-data/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | C# console app that partitions and exports a large index. |
+| [Backup and restore an index](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | C# console app that copies an index from one service to another, creating JSON files on your computer with the index schema and documents. |
+| [Index Data Lake Gen2 using Microsoft Entra ID](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/data-lake-gen2-acl-indexing/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | Source code demonstrating indexer connections and indexing of Azure Data Lake Gen2 files and folders that are secured through Microsoft Entra ID and role-based access controls. |
+| [Search aggregations](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/search-aggregations/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | Proof-of-concept source code that demonstrates how to obtain aggregations from a search index and then filter by them. |
+| [Power Skills](https://github.com/Azure-Samples/azure-search-power-skills/blob/main/README.md) | [azure-search-power-skills](https://github.com/Azure-Samples/azure-search-power-skills)  | Source code for consumable custom skills that you can incorporate in your own solutions.  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索用の新しい.NET サンプルの更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchに関する.NETサンプルに対するマイナーな更新です。主な変更点は、タイトルの表記を「.NET samples」から「.NET Samples」へと修正したこと、最終更新日を「2024年10月18日」から「2025年3月10日」へと変更したことです。また、文の表現が軽微に改善され、情報の明確化が図られています。

全体として、これらの変更は、文書が最新の情報を反映し、より明確でユーザーフレンドリーになることを目的としています。具体的には、C#コードサンプルの説明文が改善され、読者がサンプルをより理解しやすくするために言い回しが変更されています。さらに、GitHubリンクやサンプルの説明も一部整理され、情報が統一されています。

全体で28行の追加、29行の削除があり、57行が変更されています。これらの更新は、ユーザーが検索やAPIの使用法を理解できるようサポートすることを意図しています。

## articles/search/samples-java.md{#item-5992fd}

<details>
<summary>Diff</summary>
````diff
@@ -1,8 +1,7 @@
 ---
-title: Java samples
+title: Java Samples
 titleSuffix: Azure AI Search
 description: Find Azure AI Search demo Java code samples that use the Azure .NET SDK for Java.
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
@@ -12,7 +11,7 @@ ms.custom:
   - devx-track-extended-java
   - ignite-2023
 ms.topic: concept-article
-ms.date: 10/18/2024
+ms.date: 03/10/2025
 ---
 
 # Java samples for Azure AI Search
@@ -36,8 +35,8 @@ Code samples from the Azure SDK development team demonstrate API usage. You can
 | [Search index creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateIndexExample.java) | Demonstrates how to create [search indexes](search-what-is-an-index.md). |
 | [Synonym creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/SynonymMapsCreateExample.java) | Demonstrates how to create [synonym maps](search-synonyms.md).  |
 | [Search indexer creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateIndexerExample.java) | Demonstrates how to create [indexers](search-indexer-overview.md). |
-| [Search indexer data source creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/DataSourceExample.java) | Demonstrates how to create indexer data sources, required for indexer-based indexing of [supported Azure data sources](search-indexer-overview.md#supported-data-sources). |
-| [Skillset creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateSkillsetExample.java) |  Demonstrates how to create [skillsets](cognitive-search-working-with-skillsets.md) that are attached indexers, and that perform AI-based enrichment during indexing. |
+| [Search indexer data source creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/DataSourceExample.java) | Demonstrates how to create indexer data sources, which are required for indexer-based indexing of [supported Azure data sources](search-indexer-overview.md#supported-data-sources). |
+| [Skillset creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateSkillsetExample.java) |  Demonstrates how to create [skillsets](cognitive-search-working-with-skillsets.md) that are attached to indexers and perform AI-based enrichment during indexing. |
 | [Load documents](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/IndexContentManagementExample.java) | Demonstrates how to upload or merge documents into an index in a [data import](search-what-is-data-import.md) operation. |
 | [Query syntax](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/SearchAsyncWithFullyTypedDocumentsExample.java) | Demonstrates how to set up a [basic query](search-query-overview.md). |
 | [Vector search](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/VectorSearchExample.java) | Demonstrates how to set up a vector field and then generate a [vector query](vector-search-how-to-query.md). |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java サンプルの更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchに関するJavaサンプルの文書に対するマイナーな修正です。主な変更点には、タイトルの書き方を「Java samples」から「Java Samples」に修正したこと、ドキュメントの最終更新日を「2024年10月18日」から「2025年3月10日」に変更したことが含まれます。

サンプルのリスト内では、いくつかの説明が修正され、言葉遣いがより明確にされています。具体的には、「indexer-based indexing」を強調するように文章が整えられ、読者により分かりやすくなっています。

全体として、この更新では4行が追加され、5行が削除され、合計9行が変更されています。これにより、文書が最新の情報を反映し、読者がAzure AI SearchのJava SDKを利用する際の理解を助けることを目指しています。

## articles/search/samples-javascript.md{#item-82e67e}

<details>
<summary>Diff</summary>
````diff
@@ -1,8 +1,7 @@
 ---
-title: JavaScript samples
+title: JavaScript Samples
 titleSuffix: Azure AI Search
 description: Find Azure AI Search demo JavaScript code samples that use the Azure .NET SDK for JavaScript.
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
@@ -12,7 +11,7 @@ ms.custom:
   - devx-track-js
   - ignite-2023
 ms.topic: concept-article
-ms.date: 10/18/2024
+ms.date: 03/10/2025
 ---
 
 # JavaScript samples for Azure AI Search
@@ -36,9 +35,9 @@ Code samples from the Azure SDK development team demonstrate API usage. You can
 | Samples | Description |
 |---------|-------------|
 | [indexes](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Demonstrates how to create, update, get, list, and delete [search indexes](search-what-is-an-index.md). This sample category also includes a service statistic sample. |
-| [dataSourceConnections (for indexers)](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/javascript/dataSourceConnectionOperations.js) | Demonstrates how to create, update, get, list, and delete indexer data sources, required for indexer-based indexing of [supported Azure data sources](search-indexer-overview.md#supported-data-sources). |
+| [dataSourceConnections (for indexers)](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/javascript/dataSourceConnectionOperations.js) | Demonstrates how to create, update, get, list, and delete indexer data sources, which are required for indexer-based indexing of [supported Azure data sources](search-indexer-overview.md#supported-data-sources). |
 | [indexers](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Demonstrates how to create, update, get, list, reset, and delete [indexers](search-indexer-overview.md).|
-| [skillSet](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Demonstrates how to create, update, get, list, and delete [skillsets](cognitive-search-working-with-skillsets.md) that are attached indexers, and that perform AI-based enrichment during indexing. |
+| [skillSet](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Demonstrates how to create, update, get, list, and delete [skillsets](cognitive-search-working-with-skillsets.md) that are attached to indexers and perform AI-based enrichment during indexing. |
 | [synonymMaps](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Demonstrates how to create, update, get, list, and delete [synonym maps](search-synonyms.md). |
 | [VectorSearch](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v12-beta/javascript/vectorSearch.js) | Demonstrates how to index vectors and send a [vector query](vector-search-how-to-query.md). |
 
@@ -47,9 +46,9 @@ Code samples from the Azure SDK development team demonstrate API usage. You can
 | Samples | Description |
 |---------|-------------|
 | [indexes](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/typescript/src) | Demonstrates how to create, update, get, list, and delete [search indexes](search-what-is-an-index.md). This sample category also includes a service statistic sample. |
-| [dataSourceConnections (for indexers)](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/typescript/src/dataSourceConnectionOperations.ts) | Demonstrates how to create, update, get, list, and delete indexer data sources, required for indexer-based indexing of [supported Azure data sources](search-indexer-overview.md#supported-data-sources). |
+| [dataSourceConnections (for indexers)](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/typescript/src/dataSourceConnectionOperations.ts) | Demonstrates how to create, update, get, list, and delete indexer data sources, which are required for indexer-based indexing of [supported Azure data sources](search-indexer-overview.md#supported-data-sources). |
 | [indexers](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/typescript/src) | Demonstrates how to create, update, get, list, reset, and delete [indexers](search-indexer-overview.md).|
-| [skillSet](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/typescript/src/skillSetOperations.ts) | Demonstrates how to create, update, get, list, and delete [skillsets](cognitive-search-working-with-skillsets.md) that are attached indexers, and that perform AI-based enrichment during indexing. |
+| [skillSet](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/typescript/src/skillSetOperations.ts) | Demonstrates how to create, update, get, list, and delete [skillsets](cognitive-search-working-with-skillsets.md) that are attached to indexers and perform AI-based enrichment during indexing. |
 | [synonymMaps](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/typescript/src/synonymMapOperations.ts) | Demonstrates how to create, update, get, list, and delete [synonym maps](search-synonyms.md). |
 | [VectorSearch](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v12/typescript/src/vectorSearch.ts) | Demonstrates how to index vectors and send a [vector query](vector-search-how-to-query.md). |
 
@@ -67,8 +66,8 @@ Code samples from the Azure AI Search team demonstrate features and workflows. M
 
 ## Other samples
 
-The following samples are also published by the Azure AI Search team, but aren't referenced in documentation. Associated readme files provide usage instructions.
+The following samples are also published by the Azure AI Search team but aren't referenced in documentation. Associated readme files provide usage instructions.
 
 | Samples | Description |
 |---------|-------------|
-| [azure-search-vector-sample.js](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript/readme.md) | Vector search sample using the Azure SDK for JavaScript |
+| [azure-search-vector-sample.js](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript/readme.md) | Vector search sample using the Azure SDK for JavaScript. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript サンプルの更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchに関するJavaScriptサンプルの文書に対するマイナーな修正です。主な修正内容は以下の通りです：

- タイトルの修正：文書のタイトルを「JavaScript samples」から「JavaScript Samples」に変更しました。
- 最終更新日を「2024年10月18日」から「2025年3月10日」に変更しました。
- 側面によって、いくつかの説明文が若干改善され、特に「indexer-based indexing」というフレーズの表現が整理されています。これは、ユーザーが理解しやすくするためのものです。

全体として、8行が追加され、9行が削除され、合計17行が変更されています。この更新は、文書が最新の情報を反映し、ユーザーがAzure AI SearchのJavaScript SDKを利用する際に、より理解しやすくなるように意図されています。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -1,8 +1,7 @@
 ---
-title: Python samples
+title: Python Samples
 titleSuffix: Azure AI Search
 description: Find Azure AI Search demo Python code samples that use the Azure .NET SDK for Python or REST.
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
@@ -12,7 +11,7 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: concept-article
-ms.date: 10/18/2024
+ms.date: 03/10/2025
 ---
 
 # Python samples for Azure AI Search
@@ -29,7 +28,7 @@ Learn about the Python code samples that demonstrate the functionality and workf
 
 ## SDK samples
 
-[**azure-sdk-for-python/tree/main/sdk/search/azure-search-documents/samples**](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/search/azure-search-documents/samples) on GitHub provides code samples from the Azure SDK development team, demonstrating API usage.
+Code samples from the Azure SDK development team demonstrate API usage. You can find these samples in [**azure-sdk-for-python/tree/main/sdk/search/azure-search-documents/samples**](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/search/azure-search-documents/samples) on GitHub.
 
 ## Doc samples
 
@@ -48,17 +47,17 @@ Code samples from the Azure AI Search team demonstrate features and workflows. M
 
 [**azure-search-vector-samples**](https://github.com/Azure/azure-search-vector-samples/blob/main/README.md) on GitHub provides a comprehensive collection of samples for vector search scenarios, organized by scenario or technology.
 
-[**azure-search-openai-demo**](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md) is a ChatGPT-like experience over enterprise data with Azure OpenAI Python code showing how to use Azure AI Search with the large language models in Azure OpenAI. For background, see this Tech Community blog post: [Revolutionize your Enterprise Data with ChatGPT](https://techcommunity.microsoft.com/t5/ai-applied-ai-blog/revolutionize-your-enterprise-data-with-chatgpt-next-gen-apps-w/ba-p/3762087). |
+[**azure-search-openai-demo**](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md) is a ChatGPT-like experience over enterprise data with Azure OpenAI Python code showing how to use Azure AI Search with the large language models in Azure OpenAI. For background, see this [Tech Community blog post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/revolutionize-your-enterprise-data-with-chatgpt-next-gen-apps-w-azure-openai-and/3762087).
 
-[**aisearch-openai-rag-audio**](https://github.com/Azure-Samples/aisearch-openai-rag-audio) is "voice to RAG". This sample demonstrates a simple architecture for voice-based generative AI applications that enables Azure AI Search RAG on top of the real-time audio API with full-duplex audio streaming from client devices, while securely handling access to both model and retrieval system. Backend code is written in Python. Frontend code is JavaScript. [Watch this video](https://www.youtube.com/watch?v=vXJka8xZ9Ko) for an introduction. |
+[**aisearch-openai-rag-audio**](https://github.com/Azure-Samples/aisearch-openai-rag-audio) is "voice to RAG". This sample demonstrates a simple architecture for voice-based generative AI applications that enables Azure AI Search RAG on top of the real-time audio API with full-duplex audio streaming from client devices, while securely handling access to both the model and retrieval system. Backend code is written in Python, while frontend code is written in JavaScript. For an introduction, watch this [video](https://www.youtube.com/watch?v=vXJka8xZ9Ko).
 
 ## Other samples
 
-The following samples are also published by the Azure AI Search team, but aren't referenced in documentation. Associated readme files provide usage instructions.
+The following samples are also published by the Azure AI Search team but aren't referenced in documentation. Associated readme files provide usage instructions.
 
 | Repository | Description |
 |------------|-------------|
-| [index-backup-and-restore.ipynb](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) | Uses the **azure.search.documents** library in the Azure SDK for Python to make a local copy of the retrievable fields of a search index, and then push those fields to a new search index. |
+| [index-backup-and-restore.ipynb](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) | Uses the **azure.search.documents** library in the Azure SDK for Python to make a local copy of the retrievable fields of a search index and then push those fields to a new search index. |
 | [resumable-index-backup-restore](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/resumable-index-backup-restore/backup-and-restore.ipynb) | This sample accommodates larger indexes exceeding 100,000 documents.|
 
 > [!TIP]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python サンプルの更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchに関するPythonサンプルの文書に対するマイナーな修正です。主な更新内容は以下の通りです：

- タイトルの書き方を「Python samples」から「Python Samples」に変更しました。
- 最終更新日を「2024年10月18日」から「2025年3月10日」に修正しました。
- サンプルに関する説明が再構成され、一部の表現が明確化されています。具体的には、サンプルのリンクの位置を調整し、文の流れを改善しました。

また、いくつかの文の細部が修正され、特に説明文がより自然な言い回しとなっています。全体として、7行が追加され、8行が削除され、合計15行が変更されています。この更新の目的は、文書が最新の情報を反映し、ユーザーの理解を助けることです。

## articles/search/samples-rest.md{#item-198ebc}

<details>
<summary>Diff</summary>
````diff
@@ -1,40 +1,39 @@
 ---
-title: REST samples
+title: REST Samples
 titleSuffix: Azure AI Search
 description: Find Azure AI Search demo REST code samples that use the Search or Management REST APIs.
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 10/18/2024
+ms.date: 03/10/2025
 ---
 
 # REST samples for Azure AI Search
 
 Learn about the REST API samples that demonstrate the functionality and workflow of an Azure AI Search solution. These samples use the [**Search REST APIs**](/rest/api/searchservice).
 
-REST is the definitive programming interface for Azure AI Search, and all operations that can be invoked programmatically are available first in REST, and then in SDKs. For this reason, most examples in the documentation use the REST APIs to demonstrate or explain important concepts.
+REST is the definitive programming interface for Azure AI Search. All operations that can be invoked programmatically are available first in REST and then in SDKs. For this reason, most examples in the documentation use the REST APIs to demonstrate or explain important concepts.
 
-You can use any client that supports HTTP calls. [Here's a quickstart](search-get-started-rest.md) that explains how to formulate the HTTP request using Visual Studio Code with a REST client.
+You can use any client that supports HTTP calls. To learn how to formulate the HTTP request using Visual Studio Code with a REST client, see [Quickstart: Keyword search using REST](search-get-started-rest.md).
 
 ## Doc samples
 
 Code samples from the Azure AI Search team demonstrate features and workflows. Many of these samples are referenced in tutorials, quickstarts, and how-to articles. You can find these samples in [**Azure-Samples/azure-search-rest-samples**](https://github.com/Azure-Samples/azure-search-rest-samples) on GitHub.
 
 | Samples | Description |
 |---------|---------|
-| [quickstart](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart) | Source code for [Quickstart: Text search using REST](search-get-started-rest.md). This sample  covers the basic workflow for creating, loading, and querying a search index using sample data. |
-| [quickstart-vectors](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) | Source code for [Quickstart: Vector search using REST APIs](search-get-started-vector.md). This sample  covers the basic workflow for indexing and querying vector data. |
-| [skillset-tutorial](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skillset-tutorial) | Source code for [Tutorial: Use REST and AI to generate searchable content from Azure blobs](cognitive-search-tutorial-blob.md). This sample  shows you how to create a skillset that iterates over Azure blobs to extract information and infer structure.|
+| [quickstart](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart) | Source code for [Quickstart: Text search using REST](search-get-started-rest.md). This sample covers the basic workflow for creating, loading, and querying a search index using sample data. |
+| [quickstart-vectors](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) | Source code for [Quickstart: Vector search using REST APIs](search-get-started-vector.md). This sample covers the basic workflow for indexing and querying vector data. |
+| [skillset-tutorial](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skillset-tutorial) | Source code for [Tutorial: Use REST and AI to generate searchable content from Azure blobs](cognitive-search-tutorial-blob.md). This sample shows you how to create a skillset that iterates over Azure blobs to extract information and infer structure.|
 | [skill examples](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skill-examples) | Skillset examples in indexer pipelines that include indexes and indexers so that you can follow field mappings, output field mappings, and source paths. |
-| [debug-sessions](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Debug-sessions) | Source code for [Tutorial: Diagnose, repair, and commit changes to your skillset](cognitive-search-tutorial-debug-sessions.md). This sample  shows you how to use a skillset debug session in the Azure portal. REST is used to create the objects used during debug.|
+| [debug-sessions](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Debug-sessions) | Source code for [Tutorial: Diagnose, repair, and commit changes to your skillset](cognitive-search-tutorial-debug-sessions.md). This sample shows you how to use a skillset debug session in the Azure portal. REST is used to create the objects used during debug.|
 | [custom-analyzers](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/custom-analyzers) | Source code for [Tutorial: Create a custom analyzer for phone numbers](tutorial-create-custom-analyzer.md). This sample  explains how to use analyzers to preserve patterns and special characters in searchable content.|
-| [index-json-blobs](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/index-json-blobs) | Create an indexer, data source, and index for nested JSON within a JSON array. This example demonstrates the jsonArray parsing model and documentRoot parameters. |
-| [knowledge-store](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/knowledge-store) | Source code for [Create a knowledge store using REST](knowledge-store-create-rest.md). This sample  explains the necessary steps for populating a knowledge store used for knowledge mining workflows. |
+| [index-json-blobs](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/index-json-blobs) | Create an indexer, data source, and index for nested JSON within a JSON array. This sample demonstrates the jsonArray parsing model and documentRoot parameters. |
+| [knowledge-store](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/knowledge-store) | Source code for [Create a knowledge store using REST](knowledge-store-create-rest.md). This sample explains the necessary steps for populating a knowledge store used for knowledge mining workflows. |
 | [projections](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/projections) | Source code for [Define projections in a knowledge store](knowledge-store-projections-examples.md). This sample explains how to specify the physical data structures in a knowledge store.|
 
 > [!TIP]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST サンプルの更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchに関するRESTサンプルの文書へのマイナーな修正です。主な修正内容は以下の通りです：

- タイトルを「REST samples」から「REST Samples」に修正しました。
- 最終更新日が「2024年10月18日」から「2025年3月10日」に改定されました。
- 文書内の言い回しが改善され、特にレスポンスに関する説明がより流暢になりました（例：「RESTはAzure AI Searchの決定的なプログラミングインターフェースです。」から「RESTはAzure AI Searchの決定的なプログラミングインターフェースです。」に変更）。

また、サンプルリストの各項目についても説明がより明確に整理されており、特にQuickstartやSkillsetチュートリアルの説明が一貫性のある形式に修正されています。全体として、10行が追加され、11行が削除され、合計21行が変更されており、この更新は最新の情報を反映させると共に、ユーザーがより簡単にサンプルを理解できるようにすることを目的としています。

## articles/search/search-lucene-query-architecture.md{#item-b0d568}

<details>
<summary>Diff</summary>
````diff
@@ -2,25 +2,24 @@
 title: Full text search
 titleSuffix: Azure AI Search
 description: Describes concepts and architecture of query processing and document retrieval for full text search, as implemented Azure AI Search.
-
 manager: nitinme
 author: yahnoosh
 ms.author: jlembicz
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 02/24/2025
+ms.date: 03/07/2025
 ---
 
 # Full text search in Azure AI Search
 
 Full text search is an approach in information retrieval that matches on plain text stored in an index. For example, given a query string "hotels in San Diego on the beach", the search engine looks for tokenized strings based on those terms. To make scans more efficient, query strings undergo lexical analysis: lower-casing all terms, removing stop words like "the", and reducing terms to primitive root forms. When matching terms are found, the search engine retrieves documents, ranks them in order of relevance, and returns the top results.
 
-Query execution can be complex. This article is for developers who need a deeper understanding of how full text search works in Azure AI Search. For text queries, Azure AI Search seamlessly delivers expected results in most scenarios, but occasionally you might get a result that seems "off" somehow. In these situations, having a background in the four stages of Lucene query execution (query parsing, lexical analysis, document matching, scoring) can help you identify specific changes to query parameters or index configuration that produce the desired outcome. 
+Query execution can be complex. This article is for developers who need a deeper understanding of how full text search works in Azure AI Search. For text queries, Azure AI Search seamlessly delivers expected results in most scenarios, but occasionally, you might get a result that seems "off" somehow. In these situations, having a background in the four stages of Lucene query execution (query parsing, lexical analysis, document matching, and scoring) can help you identify specific changes to query parameters or index configuration that produce the desired outcome.
 
 > [!NOTE]
-> Azure AI Search uses [Apache Lucene](https://lucene.apache.org/) for full text search, but Lucene integration is not exhaustive. We selectively expose and extend Lucene functionality to enable the scenarios important to Azure AI Search. 
+> Azure AI Search uses [Apache Lucene](https://lucene.apache.org/) for full text search, but Lucene integration isn't exhaustive. We selectively expose and extend Lucene functionality to enable the scenarios important to Azure AI Search.
 
 ## Architecture overview and diagram
 
@@ -33,22 +32,22 @@ Query execution has four stages:
 
 A full text search query starts with parsing the query text to extract search terms and operators. There are two parsers so that you can choose between speed and complexity. An analysis phase is next, where individual query terms are sometimes broken down and reconstituted into new forms. This step helps to cast a broader net over what could be considered as a potential match. The search engine then scans the index to find documents with matching terms and scores each match. A result set is then sorted by a relevance score assigned to each individual matching document. Those at the top of the ranked list are returned to the calling application.
 
-The diagram below illustrates the components used to process a search request. 
+The following diagram illustrates the components used to process a search request:
 
  ![Lucene query architecture diagram in Azure AI Search.][1]
 
 | Key components | Functional description |
 |----------------|------------------------|
-|**Query parsers** | Separate query terms from query operators and create the query structure (a query tree) to be sent to the search engine. |
-|**Analyzers** | Perform lexical analysis on query terms. This process can involve transforming, removing, or expanding of query terms. |
-|**Index** | An efficient data structure used to store and organize searchable terms extracted from indexed documents. |
-|**Search engine** | Retrieves and scores matching documents based on the contents of the inverted index. |
+| **Query parsers** | Separate query terms from query operators and create the query structure (a query tree) to be sent to the search engine. |
+| **Analyzers** | Perform lexical analysis on query terms. This process can involve transforming, removing, or expanding query terms. |
+| **Index** | An efficient data structure used to store and organize searchable terms extracted from indexed documents. |
+| **Search engine** | Retrieves and scores matching documents based on the contents of the inverted index. |
 
 ## Anatomy of a search request
 
-A search request is a complete specification of what should be returned in a result set. In simplest form, it's an empty query with no criteria of any kind. A more realistic example includes parameters, several query terms, perhaps scoped to certain fields, with possibly a filter expression and ordering rules.  
+A search request is a complete specification of what should be returned in a result set. In its simplest form, it's an empty query with no criteria of any kind. A more realistic example includes parameters, several query terms, perhaps scoped to certain fields, with possibly a filter expression and ordering rules.  
 
-The following example is a search request you might send to Azure AI Search using the [REST API](/rest/api/searchservice/documents/search-post).  
+The following example is a search request you might send to Azure AI Search using the [REST API](/rest/api/searchservice/documents/search-post):
 
 ```
 POST /indexes/hotels/docs/search?api-version=2024-07-01
@@ -66,100 +65,100 @@ For this request, the search engine does the following operations:
 
 1. Finds documents where the price is at least $60 and less than $300.
 
-2. Executes the query. In this example, the search query consists of phrases and terms: `"Spacious, air-condition* +\"Ocean view\""` (users typically don't enter punctuation, but including it in the example allows us to explain how analyzers handle it). 
+2. Executes the query. In this example, the search query consists of phrases and terms: `"Spacious, air-condition* +\"Ocean view\""` (Users typically don't enter punctuation, but by including it in the example, we can explain how analyzers handle it.)
 
    For this query, the search engine scans the description and title fields specified in "searchFields" for documents that contain `"Ocean view"`, and additionally on the term `"spacious"`, or on terms that start with the prefix `"air-condition"`. The "searchMode" parameter is used to match on any term (default) or all of them, for cases where a term isn't explicitly required (`+`).
 
-3. Orders the resulting set of hotels by proximity to a given geography location, and then returns the results to the calling application. 
+3. Orders the resulting set of hotels by proximity to a given geography location, and then returns the results to the calling application.
 
-Most this article is about processing of the *search query*: `"Spacious, air-condition* +\"Ocean view\""`. Filtering and ordering are out of scope. For more information, see the [Search API reference documentation](/rest/api/searchservice/documents/search-post).
+Most of this article is about processing of the *search query*: `"Spacious, air-condition* +\"Ocean view\""`. Filtering and ordering are out of scope. For more information, see the [Search API reference documentation](/rest/api/searchservice/documents/search-post).
 
 <a name="stage1"></a>
 
 ## Stage 1: Query parsing
 
-As noted, the query string is the first line of the request: 
+As noted, the query string is the first line of the request:
 
 ```
  "search": "Spacious, air-condition* +\"Ocean view\"", 
 ```
 
-The query parser separates operators (such as `*` and `+` in the example) from search terms, and deconstructs the search query into *subqueries* of a supported type: 
+The query parser separates operators (such as `*` and `+` in the example) from search terms and deconstructs the search query into *subqueries* of a supported type:
 
 + *term query* for standalone terms (like spacious)
 + *phrase query* for quoted terms (like ocean view)
 + *prefix query* for terms followed by a prefix operator `*` (like air-condition)
 
-For a full list of supported query types, see [Lucene query syntax](/rest/api/searchservice/lucene-query-syntax-in-azure-search)
+For a full list of supported query types, see [Lucene query syntax](/rest/api/searchservice/lucene-query-syntax-in-azure-search).
 
-Operators associated with a subquery determine whether the query "must be" or "should be" satisfied in order for a document to be considered a match. For example, `+"Ocean view"` is "must" due to the `+` operator. 
+Operators associated with a subquery determine whether the query "must be" or "should be" satisfied in order for a document to be considered a match. For example, `+"Ocean view"` is "must" due to the `+` operator.
 
-The query parser restructures the subqueries into a *query tree* (an internal structure representing the query) it passes on to the search engine. In the first stage of query parsing, the query tree looks like this.  
+The query parser restructures the subqueries into a *query tree* (an internal structure representing the query), which it passes to the search engine. In the first stage of query parsing, the query tree looks like this:
 
  ![Conceptual diagram of a boolean query with searchmode set to any.][2]
 
-### Supported parsers: Simple and Full Lucene 
+### Supported parsers: Simple and Full Lucene
 
- Azure AI Search exposes two different query languages, `simple` (default) and `full`. By setting the `queryType` parameter with your search request, you tell the query parser which query language you choose so that it knows how to interpret the operators and syntax. 
+ Azure AI Search exposes two different query languages: `simple` (default) and `full`. By setting the `queryType` parameter with your search request, you tell the query parser which query language you choose so that it knows how to interpret the operators and syntax.
 
-+ The [Simple query language](/rest/api/searchservice/simple-query-syntax-in-azure-search) is intuitive and robust, often suitable to interpret user input as-is without client-side processing. It supports query operators familiar from web search engines. 
++ The [Simple query language](/rest/api/searchservice/simple-query-syntax-in-azure-search) is intuitive and robust, often suitable for interpreting user input as-is without client-side processing. It supports query operators familiar from web search engines.
 
 + The [Full Lucene query language](/rest/api/searchservice/lucene-query-syntax-in-azure-search), which you get by setting `queryType=full`, extends the default Simple query language by adding support for more operators and query types like wildcard, fuzzy, regex, and field-scoped queries. For example, a regular expression sent in Simple query syntax would be interpreted as a query string and not an expression. The example request in this article uses the Full Lucene query language.
 
-### Impact of searchMode on the parser 
+### Impact of searchMode on the parser
 
 Another search request parameter that affects parsing is the "searchMode" parameter. It controls the default operator for Boolean queries: any (default) or all.  
 
-When "searchMode=any", which is the default, the space delimiter between spacious and air-condition is OR (`||`), making the sample query text equivalent to: 
+When "searchMode=any", which is the default, the space delimiter between spacious and air-condition is OR (`||`), making the sample query text equivalent to:
 
 ```
 Spacious,||air-condition*+"Ocean view" 
 ```
 
-Explicit operators, such as `+` in `+"Ocean view"`, are unambiguous in boolean query construction (the term *must* match). Less obvious is how to interpret the remaining terms: spacious and air-condition. Should the search engine find matches on ocean view *and* spacious *and* air-condition? Or should it find ocean view plus *either one* of the remaining terms? 
+Explicit operators, such as `+` in `+"Ocean view"`, are unambiguous in boolean query construction (the term *must* match). Less obvious is how to interpret the remaining terms: spacious and air-condition. Should the search engine find matches on ocean view *and* spacious *and* air-condition? Or should it find ocean view plus *either one* of the remaining terms?
 
-By default ("searchMode=any"), the search engine assumes the broader interpretation. Either field *should* be matched, reflecting "or" semantics. The initial query tree illustrated previously, with the two "should" operations, shows the default.  
+By default ("searchMode=any"), the search engine assumes the broader interpretation. Either field *should* be matched, reflecting "or" semantics. The initial query tree illustrated previously, with the two "should" operations, shows the default.
 
-Suppose that we now set "searchMode=all". In this case, the space is interpreted as an "and" operation. Each of the remaining terms must both be present in the document to qualify as a match. The resulting sample query would be interpreted as follows: 
+Suppose that we now set "searchMode=all". In this case, the space is interpreted as an "and" operation. Both of the remaining terms must be present in the document to qualify as a match. The resulting sample query would be interpreted like this:
 
 ```
 +Spacious,+air-condition*+"Ocean view"
 ```
 
-A modified query tree for this query would be as follows, where a matching document is the intersection of all three subqueries: 
+A modified query tree for this query, where a matching document is the intersection of all three subqueries, would look like this:
 
  ![Conceptual diagram of a boolean query with searchmode set to all.][3]
 
 > [!NOTE]
-> Choosing "searchMode=any" over "searchMode=all" is a decision best arrived at by running representative queries. Users who are likely to include operators (common when searching document stores) might find results more intuitive if "searchMode=all" informs boolean query constructs. For more about the interplay between "searchMode" and operators, see [Simple query syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search).
+> Choosing "searchMode=any" over "searchMode=all" is a decision best made by running representative queries. Users who are likely to include operators (common when searching document stores) might find results more intuitive if "searchMode=all" informs boolean query constructs. For more information about the interplay between "searchMode" and operators, see [Simple query syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search).
 
 <a name="stage2"></a>
 
-## Stage 2: Lexical analysis 
+## Stage 2: Lexical analysis
 
-Lexical analyzers process *term queries* and *phrase queries* after the query tree is structured. An analyzer accepts the text inputs given to it by the parser, processes the text, and then sends back tokenized terms to be incorporated into the query tree. 
+Lexical analyzers process *term queries* and *phrase queries* after the query tree is structured. An analyzer accepts the text inputs given to it by the parser, processes the text, and then sends back tokenized terms to be incorporated into the query tree.
 
-The most common form of lexical analysis is *linguistic analysis that transforms query terms based on rules specific to a given language: 
+The most common form of lexical analysis is *linguistic analysis*, which transforms query terms based on rules specific to a given language. This involves:
 
-* Reducing a query term to the root form of a word 
-* Removing non-essential words ([stopwords](reference-stopwords.md), such as "the" or "and" in English) 
-* Breaking a composite word into component parts 
-* Lower casing an upper case word 
++ Reducing a query term to the root form of a word.
++ Removing non-essential words ([stopwords](reference-stopwords.md), such as "the" or "and" in English).
++ Breaking a composite word into component parts.
++ Lowercasing an uppercase word.
 
 All of these operations tend to erase differences between the text input provided by the user and the terms stored in the index. Such operations go beyond text processing and require in-depth knowledge of the language itself. To add this layer of linguistic awareness, Azure AI Search supports a long list of [language analyzers](/rest/api/searchservice/language-support) from both Lucene and Microsoft.
 
 > [!NOTE]
-> Analysis requirements can range from minimal to elaborate depending on your scenario. You can control complexity of lexical analysis by the selecting one of the predefined analyzers or by creating your own [custom analyzer](/rest/api/searchservice/Custom-analyzers-in-Azure-Search). Analyzers are scoped to searchable fields and are specified as part of a field definition. This allows you to vary lexical analysis on a per-field basis. Unspecified, the *standard* Lucene analyzer is used.
+> Depending on your scenario, analysis requirements can range from minimal to elaborate. You can control the complexity of lexical analysis by selecting one of the predefined analyzers or by creating your own [custom analyzer](/rest/api/searchservice/Custom-analyzers-in-Azure-Search). Analyzers are scoped to searchable fields and are specified as part of a field definition. This allows you to vary lexical analysis on a per-field basis. If unspecified, the *standard* Lucene analyzer is used.
 
 In our example, prior to analysis, the initial query tree has the term "Spacious," with an uppercase "S" and a comma that the query parser interprets as a part of the query term (a comma isn't considered a query language operator).  
 
-When the default analyzer processes the term, it will lowercase "ocean view" and "spacious", and remove the comma character. The modified query tree looks like: 
+When the default analyzer processes the term, it will lowercase "ocean view" and "spacious" and remove the comma character. The modified query tree looks like this:
 
  ![Conceptual diagram of a boolean query with analyzed terms.][4]
 
-### Testing analyzer behaviors 
+### Testing analyzer behaviors
 
-The behavior of an analyzer can be tested using the [Analyze API](/rest/api/searchservice/indexes/analyze). Provide the text you want to analyze to see what terms given analyzer generates. For example, to see how the standard analyzer would process the text "air-condition", you can issue the following request:
+The behavior of an analyzer can be tested using the [Analyze API](/rest/api/searchservice/indexes/analyze). Provide the text you want to analyze to see what terms the given analyzer generates. For example, to see how the standard analyzer would process the text "air-condition", you can issue the following request:
 
 ```json
 {
@@ -191,15 +190,15 @@ The standard analyzer breaks the input text into the following two tokens, annot
 
 <a name="exceptions"></a>
 
-### Exceptions to lexical analysis 
+### Exceptions to lexical analysis
 
-Lexical analysis applies only to query types that require complete terms – either a term query or a phrase query. It doesn’t apply to query types with incomplete terms – prefix query, wildcard query, regex query – or to a fuzzy query. Those query types, including the prefix query with term `air-condition*` in our example, are added directly to the query tree, bypassing the analysis stage. The only transformation performed on query terms of those types is lowercasing.
+Lexical analysis applies only to query types that require complete terms, either a term query or a phrase query. It doesn’t apply to query types with incomplete terms—prefix query, wildcard query, and regex query—or to a fuzzy query. Those query types, including the prefix query with the term `air-condition*` in our example, are added directly to the query tree, bypassing the analysis stage. The only transformation performed on query terms of those types is lowercasing.
 
 <a name="stage3"></a>
 
-## Stage 3: Document retrieval 
+## Stage 3: Document retrieval
 
-Document retrieval refers to finding documents with matching terms in the index. This stage is understood best through an example. Let's start with a hotels index having the following simple schema: 
+Document retrieval refers to finding documents with matching terms in the index. This stage is best understood through an example. Let's start with a hotels index that has the following simple schema:
 
 ```json
 {
@@ -212,7 +211,7 @@ Document retrieval refers to finding documents with matching terms in the index.
 } 
 ```
 
-Further assume that this index contains the following four documents: 
+Further assume that this index contains the following four documents:
 
 ```json
 {
@@ -241,13 +240,13 @@ Further assume that this index contains the following four documents:
 }
 ```
 
-**How terms are indexed**
+### How terms are indexed
 
 To understand retrieval, it helps to know a few basics about indexing. The unit of storage is an inverted index, one for each searchable field. Within an inverted index is a sorted list of all terms from all documents. Each term maps to the list of documents in which it occurs, as evident in the example below.
 
 To produce the terms in an inverted index, the search engine performs lexical analysis over the content of documents, similar to what happens during query processing:
 
-1. *Text inputs* are passed to an analyzer, lower-cased, stripped of punctuation, and so forth, depending on the analyzer configuration. 
+1. *Text inputs* are passed to an analyzer, lowercased, stripped of punctuation, and so forth, depending on the analyzer configuration.
 2. *Tokens* are the output of lexical analysis.
 3. *Terms* are added to the index.
 
@@ -256,7 +255,7 @@ It's common, but not required, to use the same analyzers for search and indexing
 > [!NOTE]
 > Azure AI Search lets you specify different analyzers for indexing and search via additional `indexAnalyzer` and `searchAnalyzer` field parameters. If unspecified, the analyzer set with the `analyzer` property is used for both indexing and searching.  
 
-**Inverted index for example documents**
+### Inverted index for example documents
 
 Returning to our example, for the **title** field, the inverted index looks like this:
 
@@ -270,9 +269,9 @@ Returning to our example, for the **title** field, the inverted index looks like
 | resort | 3 |
 | retreat | 4 |
 
-In the title field, only *hotel* shows up in two documents: 1, 3.
+In the title field, only *hotel* shows up in two documents: 1 and 3.
 
-For the **description** field, the index is as follows:
+For the **description** field, the index looks like this:
 
 | Term | Document list |
 |------|---------------|
@@ -300,31 +299,30 @@ For the **description** field, the index is as follows:
 | walking |	1
 | with | 3
 
+### Matching query terms against indexed terms
 
-**Matching query terms against indexed terms**
-
-Given the inverted indexes above, let’s return to the sample query and see how matching documents are found for our example query. Recall that the final query tree looks like this: 
+Given the inverted indexes above, let’s return to the sample query and see how matching documents are found for our example query. Recall that the final query tree looks like this:
 
  ![Conceptual diagram of a boolean query with analyzed terms.][4]
 
-During query execution, individual queries are executed against the searchable fields independently. 
+During query execution, individual queries are executed against the searchable fields independently.
 
-+ The TermQuery, "spacious", matches document 1 (Hotel Atman). 
++ The TermQuery, "spacious", matches document 1 (Hotel Atman).
 
-+ The PrefixQuery, "air-condition*", doesn't match any documents. 
++ The PrefixQuery, "air-condition*", doesn't match any documents.
 
-  This is a behavior that sometimes confuses developers. Although the term air-conditioned exists in the document, it's split into two terms by the default analyzer. Recall that prefix queries, which contain partial terms, aren't analyzed. Therefore terms with prefix "air-condition" are looked up in the inverted index and not found.
+  This behavior sometimes confuses developers. Although the term air-conditioned exists in the document, it's split into two terms by the default analyzer. Recall that prefix queries, which contain partial terms, aren't analyzed. Therefore, terms with the prefix "air-condition" are looked up in the inverted index and not found.
 
-+ The PhraseQuery, "ocean view", looks up the terms "ocean" and "view" and checks the proximity of terms in the original document. Documents 1, 2 and 3 match this query in the description field. Notice document 4 has the term ocean in the title but isn’t considered a match, as we're looking for the "ocean view" phrase rather than individual words. 
++ The PhraseQuery, "ocean view", looks up the terms "ocean" and "view" and checks the proximity of terms in the original document. Documents 1, 2, and 3 match this query in the description field. Notice document 4 has the term "ocean" in the title but isn’t considered a match, as we're looking for the "ocean view" phrase rather than individual words.
 
 > [!NOTE]
-> A search query is executed independently against all searchable fields in the Azure AI Search index unless you limit the fields set with the `searchFields` parameter, as illustrated in the example search request. Documents that match in any of the selected fields are returned. 
+> A search query is executed independently against all searchable fields in the Azure AI Search index unless you limit the fields set with the `searchFields` parameter, as illustrated in the example search request. Documents that match in any of the selected fields are returned.
 
-On the whole, for the query in question, the documents that match are 1, 2, 3. 
+On the whole, for the query in question, the documents that match are 1, 2, and 3.
 
 ## Stage 4: Scoring  
 
-Every document in a search result set is assigned a relevance score. The function of the relevance score is to rank higher those documents that best answer a user question as expressed by the search query. The score is computed based on statistical properties of terms that matched. At the core of the scoring formula is [TF/IDF (term frequency-inverse document frequency)](https://en.wikipedia.org/wiki/Tf%E2%80%93idf). In queries containing rare and common terms, TF/IDF promotes results containing the rare term. For example, in a hypothetical index with all Wikipedia articles, from documents that matched the query *the president*, documents matching on *president* are considered more relevant than documents matching on *the*.
+Every document in a search result set is assigned a relevance score. The function of the relevance score is to rank higher those documents that best answer a user question as expressed by the search query. The score is computed based on statistical properties of terms that matched. At the core of the scoring formula is [term frequency–inverse document frequency](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) (TF/IDF). In queries containing rare and common terms, TF/IDF promotes results containing the rare term. For example, in a hypothetical index with all Wikipedia articles, from documents that matched the query *the president*, documents matching on *president* are considered more relevant than documents matching on *the*.
 
 ### Scoring example
 
@@ -359,25 +357,25 @@ search=Spacious, air-condition* +"Ocean view"
 }
 ```
 
-Document 1 matched the query best because both the term *spacious* and the required phrase *ocean view* occur in the description field. The next two documents match only the phrase *ocean view*. It might be surprising that the relevance score for document 2 and 3 is different even though they matched the query in the same way. It's because the scoring formula has more components than just TF/IDF. In this case, document 3 was assigned a slightly higher score because its description is shorter. Learn about [Lucene's Practical Scoring Formula](https://lucene.apache.org/core/6_6_1/core/org/apache/lucene/search/similarities/TFIDFSimilarity.html) to understand how field length and other factors can influence the relevance score.
+Document 1 matched the query best because both the term *spacious* and the required phrase *ocean view* occur in the description field. The next two documents match only the phrase *ocean view*. You might be surprised that the relevance scores for documents 2 and 3 are different, even though they matched the query in the same way. That's because the scoring formula has more components than just TF/IDF. In this case, document 3 was assigned a slightly higher score because its description is shorter. Learn about [Lucene's Practical Scoring Formula](https://lucene.apache.org/core/6_6_1/core/org/apache/lucene/search/similarities/TFIDFSimilarity.html) to understand how field length and other factors can influence the relevance score.
 
-Some query types (wildcard, prefix, regex) always contribute a constant score to the overall document score. This allows matches found through query expansion to be included in the results, but without affecting the ranking. 
+Some query types (wildcard, prefix, and regex) always contribute a constant score to the overall document score. This allows matches found through query expansion to be included in the results without affecting the ranking.
 
-An example illustrates why this matters. Wildcard searches, including prefix searches, are ambiguous by definition because the input is a partial string with potential matches on a very large number of disparate terms (consider an input of "tour*", with matches found on “tours”, “tourettes”, and “tourmaline”). Given the nature of these results, there's no way to reasonably infer which terms are more valuable than others. For this reason, we ignore term frequencies when scoring results in queries of types wildcard, prefix and regex. In a multi-part search request that includes partial and complete terms, results from the partial input are incorporated with a constant score to avoid bias towards potentially unexpected matches.
+An example illustrates why this matters. Wildcard searches, including prefix searches, are ambiguous by definition because the input is a partial string with potential matches on a very large number of disparate terms. Consider an input of "tour*", with matches found on "tours", "tourettes", and "tourmaline". Given the nature of these results, there's no way to reasonably infer which terms are more valuable than others. For this reason, we ignore term frequencies when scoring results in queries of types wildcard, prefix, and regex. In a multi-part search request that includes partial and complete terms, results from the partial input are incorporated with a constant score to avoid bias towards potentially unexpected matches.
 
 ### Relevance tuning
 
 There are two ways to tune relevance scores in Azure AI Search:
 
-1. **Scoring profiles** promote documents in the ranked list of results based on a set of rules. In our example, we could consider documents that matched in the title field more relevant than documents that matched in the description field. Additionally, if our index had a price field for each hotel, we could promote documents with lower price. Learn more about [adding scoring profiles to a search index](/rest/api/searchservice/add-scoring-profiles-to-a-search-index).
++ **Scoring profiles** promote documents in the ranked list of results based on a set of rules. In our example, we could consider documents that matched in the title field more relevant than documents that matched in the description field. Additionally, if our index had a price field for each hotel, we could promote documents with lower prices. Learn more about [adding scoring profiles to a search index](/rest/api/searchservice/add-scoring-profiles-to-a-search-index).
 
-1. **Term boosting** (available only in the Full Lucene query syntax) provides a boosting operator `^` that can be applied to any part of the query tree. In our example, instead of searching on the prefix *air-condition*\*, one could search for either the exact term *air-condition* or the prefix, but documents that match on the exact term are ranked higher by applying boost to the term query: *air-condition^2||air-condition**. Learn more about [term boosting in a query](/rest/api/searchservice/lucene-query-syntax-in-azure-search#bkmk_termboost).
++ **Term boosting** (available only in the Full Lucene query syntax) provides a boosting operator `^` that can be applied to any part of the query tree. In our example, instead of searching on the prefix *air-condition*\*, one could search for either the exact term *air-condition* or the prefix, but documents that match on the exact term are ranked higher by applying boost to the term query: *air-condition^2||air-condition**. Learn more about [term boosting in a query](/rest/api/searchservice/lucene-query-syntax-in-azure-search#bkmk_termboost).
 
 ### Scoring in a distributed index
 
-All indexes in Azure AI Search are automatically split into multiple shards, allowing us to quickly distribute the index among multiple nodes during service scale up or scale down. When a search request is issued, it’s issued against each shard independently. The results from each shard are then merged and ordered by score (if no other ordering is defined). It's important to know that the scoring function weights query term frequency against its inverse document frequency in all documents within the shard, not across all shards!
+All indexes in Azure AI Search are automatically split into multiple shards, allowing us to quickly distribute the index among multiple nodes during service scale up or scale down. When a search request is issued, it's issued against each shard independently. The results from each shard are then merged and ordered by score (if no other ordering is defined). It's important to know that the scoring function weights query term frequency against its inverse document frequency in all documents within the shard, not across all shards!
 
-This means a relevance score *could* be different for identical documents if they reside on different shards. Fortunately, such differences tend to disappear as the number of documents in the index grows due to more even term distribution. It’s not possible to assume on which shard any given document will be placed. However, assuming a document key doesn't change, it will always be assigned to the same shard.
+This means a relevance score *could* be different for identical documents if they reside on different shards. Fortunately, such differences tend to disappear as the number of documents in the index grows due to more even term distribution. It's not possible to assume on which shard any given document will be placed. However, assuming a document key doesn't change, it will always be assigned to the same shard.
 
 In general, document score isn't the best attribute for ordering documents if order stability is important. For example, given two documents with an identical score, there's no guarantee that one appears first in subsequent runs of the same query. Document score should only give a general sense of document relevance relative to other documents in the results set.
 
@@ -387,29 +385,29 @@ The success of commercial search engines has raised expectations for full text s
 
 From a technical standpoint, full text search is highly complex, requiring sophisticated linguistic analysis and a systematic approach to processing in ways that distill, expand, and transform query terms to deliver a relevant result. Given the inherent complexities, there are many factors that can affect the outcome of a query. For this reason, investing the time to understand the mechanics of full text search offers tangible benefits when trying to work through unexpected results.  
 
-This article explored full text search in the context of Azure AI Search. We hope it gives you sufficient background to recognize potential causes and resolutions for addressing common query problems. 
+This article explored full text search in the context of Azure AI Search. We hope it gives you sufficient background to recognize potential causes and resolutions for addressing common query problems.
 
 ## Next steps
 
-+ Build the sample index, try out different queries and review results. For instructions, see [Build and query an index in the Azure portal](search-get-started-portal.md).
++ Build the sample index, try out different queries, and review results. For instructions, see [Build and query an index in the Azure portal](search-get-started-portal.md).
 
 + Try other query syntax from the [Search Documents](/rest/api/searchservice/documents/search-post#examples) example section or from [Simple query syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search) in Search explorer in the Azure portal.
 
 + Review [scoring profiles](/rest/api/searchservice/add-scoring-profiles-to-a-search-index) if you want to tune ranking in your search application.
 
-+ Learn how to apply [language-specific lexical analyzers](/rest/api/searchservice/language-support).
++ Apply [language-specific lexical analyzers](/rest/api/searchservice/language-support).
 
 + [Configure custom analyzers](/rest/api/searchservice/custom-analyzers-in-azure-search) for either minimal processing or specialized processing on specific fields.
 
-## See also
+## Related content
 
-[Search Documents REST API](/rest/api/searchservice/documents/search-post) 
++ [Search Documents REST API](/rest/api/searchservice/documents/search-post)
 
-[Simple query syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search) 
++ [Simple query syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search)
 
-[Full Lucene query syntax](/rest/api/searchservice/lucene-query-syntax-in-azure-search) 
++ [Full Lucene query syntax](/rest/api/searchservice/lucene-query-syntax-in-azure-search)
 
-[Handle search results](./search-pagination-page-layout.md)
++ [Handle search results](./search-pagination-page-layout.md)
 
 <!--Image references-->
 [1]: ./media/search-lucene-query-architecture/architecture-diagram2.png
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "検索クエリ処理アーキテクチャの更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchにおける検索クエリ処理アーキテクチャに関する文書の重要な改訂を示しています。主な修正内容は以下の通りです：

- 文書全体にわたり、記述が明確化され、文の流れが改善されました。たとえば、「Query execution can be complex.」という部分が若干言い回しが変わり、理解しやすくなっています。
- 最終更新日が「2025年2月24日」から「2025年3月7日」に変更されました。
- 文書に含まれる専門用語やフレーズについての表現が微調整され、特に「Lexical analysis」や「Document retrieval」セクションに於いて、情報が整理されました。
- 構文や条件の説明では、フォーマットの一貫性が向上し、可読性が向上しています。

さらに、構造が改善され、情報が明確かつ体系的に提示されています。また、サンプルコードや注釈に対する言い回しも見直され、開発者にとっての理解が深まるよう努められています。全体として、74行が追加され、76行が削除され、150行が変更されたため、レイアウトや内容に対して大幅な改良がなされています。この更新は、ユーザーがAzure AI Searchのフルテキスト検索の仕組みをより深く理解する手助けをすることを目的としています。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -44,9 +44,10 @@ AI service integration refers to internal connections to an Azure AI services mu
 | Brazil South​​ ​ | ✅ | ✅ | |  |
 | Canada Central​​ | ✅ | ✅ | ✅ |  |
 | Canada East​​ ​ |  | ✅ | |  |
+| ​Central US​​ | ✅ | ✅ | ✅ | |
 | East US​ | ✅ | ✅ | ✅ |  |
 | East US 2 ​ | ✅ | ✅ | ✅ | |
-| ​Central US​​ | ✅ | ✅ | ✅ | |
+| Mexico Central | |  | ✅ | |
 | North Central US​ ​ | ✅ | ✅ | |  | 
 | South Central US​  | ✅ | ✅ | ✅ | |
 | West US​ ​ | ✅ | ✅ | |  |
@@ -60,7 +61,7 @@ AI service integration refers to internal connections to an Azure AI services mu
 |--|--|--|--|--|
 | North Europe​​ | ✅ | ✅ | ✅ | S2, S3, L1, L2|
 | West Europe​​ | ✅ | ✅ | ✅ |  |
-| France Central​​ | ✅ | ✅ | ✅ | S2, S3, L1, L2|
+| France Central​​ | ✅ | ✅ | ✅ | |
 | Germany West Central​ ​| ✅ |  | ✅ | |
 | Italy North​​ |  |  | ✅ | |
 | Norway East​​ | ✅ |  | ✅ |  |
@@ -105,6 +106,7 @@ AI service integration refers to internal connections to an Azure AI services mu
 | Japan West​ | ✅ | ✅ |  |
 | Korea Central | ✅ | ✅ | ✅ |
 | Korea South​ ​ |  | ✅ |  |
+| Taiwan North |  |  |   |  |
 
 <sup>1</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域サポートの更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchにおける「地域サポート」の文書に対するマイナーな修正を示しています。主な修正内容は以下の通りです：

- 表の内容が更新され、いくつかの地域が追加されました。具体的には、「Central US」および「Mexico Central」がリストに加えられました。
- 「France Central」地域に関して、機能の詳細が削除され、より簡潔な表現に改められました。
- その他の地域に関しても、全体的に整形され、より一貫したフォーマットが適用されています。

この更新により、地域サポートに関する情報が最新のものとなり、ユーザーは新たに追加された地域についての情報を得ることができます。改訂された行数は、4行の追加、2行の削除があった結果、合計で6行の変更が行われました。全体として、地域に関するサポート状況の透明性が向上しています。

## articles/search/tutorial-multiple-data-sources.md{#item-71558f}

<details>
<summary>Diff</summary>
````diff
@@ -1,14 +1,13 @@
 ---
-title: C# tutorial indexing multiple Azure data sources
+title: 'C# Tutorial: Index Multiple Azure Data Sources'
 titleSuffix: Azure AI Search
 description: Learn how to import data from multiple data sources into a single Azure AI Search index using indexers. This tutorial and sample code are in C#.
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 12/10/2024
+ms.date: 03/10/2025
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
@@ -17,107 +16,110 @@ ms.custom:
 
 # Tutorial: Index from multiple data sources using the .NET SDK
 
-Azure AI Search can import, analyze, and index data from multiple data sources into a single consolidated search index. 
+Azure AI Search supports importing, analyzing, and indexing data from multiple data sources into a single consolidated search index.
 
-This C# tutorial uses the [Azure.Search.Documents](/dotnet/api/overview/azure/search) client library in the Azure SDK for .NET to index sample hotel data from an Azure Cosmos DB instance, and merges that with hotel room details drawn from Azure Blob Storage documents. The result is a combined hotel search index containing hotel documents, with rooms as a complex data types.
+This C# tutorial uses the [Azure.Search.Documents](/dotnet/api/overview/azure/search) client library in the Azure SDK for .NET to index sample hotel data from an Azure Cosmos DB instance. You then merge the data with hotel room details drawn from Azure Blob Storage documents. The result is a combined hotel search index containing hotel documents, with rooms as complex data types.
 
-In this tutorial, you'll perform the following tasks:
+In this tutorial, you:
 
 > [!div class="checklist"]
 > * Upload sample data and create data sources
 > * Identify the document key
 > * Define and create the index
 > * Index hotel data from Azure Cosmos DB
-> * Merge hotel room data from blob storage
-
-If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
+> * Merge hotel room data from Blob storage
 
 ## Overview
 
-This tutorial uses [Azure.Search.Documents](/dotnet/api/overview/azure/search) to create and run multiple indexers. In this tutorial, you'll set up two Azure data sources so that you can configure an indexer that pulls from both to populate a single search index. The two data sets must have a value in common to support the merge. In this sample, that field is an ID. As long as there's a field in common to support the mapping, an indexer can merge data from disparate resources: structured data from Azure SQL, unstructured data from Blob storage, or any combination of [supported data sources](search-indexer-overview.md#supported-data-sources) on Azure.
+This tutorial uses [Azure.Search.Documents](/dotnet/api/overview/azure/search) to create and run multiple indexers. In this tutorial, you set up two Azure data sources so that you can configure an indexer that pulls from both to populate a single search index. The two data sets must have a value in common to support the merge. In this sample, that field is an ID. As long as there's a field in common to support the mapping, an indexer can merge data from disparate resources: structured data from Azure SQL, unstructured data from Blob storage, or any combination of [supported data sources](search-indexer-overview.md#supported-data-sources) on Azure.
 
 A finished version of the code in this tutorial can be found in the following project:
 
 * [multiple-data-sources/v11 (GitHub)](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources/v11)
 
 ## Prerequisites
 
-+ [Azure Cosmos DB for NoSQL](/azure/cosmos-db/create-cosmosdb-resources-portal)
-+ [Azure Storage](/azure/storage/common/storage-account-create)
-+ [Visual Studio](https://visualstudio.microsoft.com/)
-+ [Azure AI Search (version 11.x) NuGet package](https://www.nuget.org/packages/Azure.Search.Documents/)
-+ [Azure AI Search](search-create-service-portal.md)
+* An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+* An [Azure Cosmos DB for NoSQL account](/azure/cosmos-db/create-cosmosdb-resources-portal).
+* An [Azure storage account](/azure/storage/common/storage-account-create).
+* An [Azure AI Search service](search-create-service-portal.md).
+* The [Azure AI Search (version 11.x) NuGet package](https://www.nuget.org/packages/Azure.Search.Documents/).
+* [Visual Studio](https://visualstudio.microsoft.com/).
 
 > [!NOTE]
 > You can use a free search service for this tutorial. The free tier limits you to three indexes, three indexers, and three data sources. This tutorial creates one of each. Before starting, make sure you have room on your service to accept the new resources.
 
 ## 1 - Create services
 
-This tutorial uses Azure AI Search for indexing and queries, Azure Cosmos DB for one data set, and Azure Blob Storage for the second data set. 
+This tutorial uses Azure AI Search for indexing and queries, Azure Cosmos DB for the first data set, and Azure Blob Storage for the second data set.
 
 If possible, create all services in the same region and resource group for proximity and manageability. In practice, your services can be in any region.
 
-This sample uses two small sets of data that describe seven fictional hotels. One set describes the hotels themselves, and will be loaded into an Azure Cosmos DB database. The other set contains hotel room details, and is provided as seven separate JSON files to be uploaded into Azure Blob Storage.
+This sample uses two small sets of data describing seven fictional hotels. One set describes the hotels themselves and will be loaded into an Azure Cosmos DB database. The other set contains hotel room details and is provided as seven separate JSON files to be uploaded into Azure Blob Storage.
 
 ### Start with Azure Cosmos DB
 
-1. Sign in to the [Azure portal](https://portal.azure.com), and then navigate your Azure Cosmos DB account Overview page.
+1. Sign in to the [Azure portal](https://portal.azure.com), and then go to the **Overview** page of your Azure Cosmos DB account.
 
-1. Select **Data Explorer** and then select **New Database**.
+1. Select **Data Explorer**, and then select **New Database**.
 
    :::image type="content" source="media/tutorial-multiple-data-sources/cosmos-newdb.png" alt-text="Create a new database" border="true":::
 
-1. Enter the name **hotel-rooms-db**. Accept default values for the remaining settings.
+1. Enter the name **hotel-rooms-db**. Accept the default values for the remaining settings.
 
    :::image type="content" source="media/tutorial-multiple-data-sources/cosmos-dbname.png" alt-text="Configure database" border="true":::
 
-1. Create a new container. Use the existing database you just created. Enter **hotels** for the container name, and use **/HotelId** for the Partition key.
+1. Create a new container. Use the existing database you previously created. Enter **hotels** for the container name and use **/HotelId** for the Partition key.
 
    :::image type="content" source="media/tutorial-multiple-data-sources/cosmos-add-container.png" alt-text="Add container" border="true":::
 
-1. Select **Items** under **hotels**, and then select **Upload Item** on the command bar. Navigate to and then select the file **cosmosdb/HotelsDataSubset_CosmosDb.json** in the project folder.
+1. Select **Items** under **hotels**, and then select **Upload Item** on the command bar. Navigate to and select the file **cosmosdb/HotelsDataSubset_CosmosDb.json** in the project folder.
 
    :::image type="content" source="media/tutorial-multiple-data-sources/cosmos-upload.png" alt-text="Upload to Azure Cosmos DB collection" border="true":::
 
 1. Use the Refresh button to refresh your view of the items in the hotels collection. You should see seven new database documents listed.
 
-1. Copy a connection string from the **Keys** page into Notepad. You'll need this value for **appsettings.json** in a later step. If you didn't use the suggested database name "hotel-rooms-db", copy the database name as well.
+1. Copy a connection string from the **Keys** page into Notepad. You need this value for **appsettings.json** in a later step. If you didn't use the suggested database name "hotel-rooms-db", copy the database name as well.
 
 ### Azure Blob Storage
 
-1. Sign in to the [Azure portal](https://portal.azure.com), navigate to your Azure storage account, select **Blobs**, and then select **+ Container**.
+1. Sign in to the [Azure portal](https://portal.azure.com), go to your Azure storage account, select **Blobs**, and then select **+ Container**.
 
 1. [Create a blob container](/azure/storage/blobs/storage-quickstart-blobs-portal) named **hotel-rooms** to store the sample hotel room JSON files. You can set the Public Access Level to any of its valid values.
 
    :::image type="content" source="media/tutorial-multiple-data-sources/blob-add-container.png" alt-text="Create a blob container" border="true":::
 
-1. After the container is created, open it and select **Upload** on the command bar. Navigate to the folder containing the sample files. Select all of them and then select **Upload**.
+1. After the container is created, open it and select **Upload** on the command bar. Navigate to the folder containing the sample files. Select all of them, and then select **Upload**.
 
    :::image type="content" source="media/tutorial-multiple-data-sources/blob-upload.png" alt-text="Upload files" border="false":::
 
-1. Copy the storage account name and a connection string from the **Access Keys** page into Notepad. You'll need both values for **appsettings.json** in a later step.
+1. Copy the storage account name and a connection string from the **Access Keys** page into Notepad. You need both values for **appsettings.json** in a later step.
 
 ### Azure AI Search
 
 The third component is Azure AI Search, which you can [create in the Azure portal](search-create-service-portal.md) or [find an existing search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your Azure resources.
 
-### Copy an admin api-key and URL for Azure AI Search
+### Copy an admin API key and URL for Azure AI Search
 
-To authenticate to your search service, you'll need the service URL and an access key.
+To authenticate to your search service, you need the service URL and an access key.
 
-1. Sign in to the [Azure portal](https://portal.azure.com), and in your search service **Overview** page, get the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
+1. Sign in to the [Azure portal](https://portal.azure.com).
 
-1. In **Settings** > **Keys**, get an admin key for full rights on the service. There are two interchangeable admin keys, provided for business continuity in case you need to roll one over. You can use either the primary or secondary key on requests for adding, modifying, and deleting objects.
+1. On the **Overview** page of your search service, get the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
 
-Having a valid key establishes trust, on a per request basis, between the application sending the request and the service that handles it.
+1. On **Settings** > **Keys**, get an admin key for full rights on the service. There are two interchangeable admin keys, provided for business continuity in case you need to roll one over. You can use either the primary or secondary key on requests for adding, modifying, and deleting objects.
+
+Having a valid key establishes trust, on a per-request basis, between the application sending the request and the service handling it.
 
 ## 2 - Set up your environment
 
-1. Start Visual Studio and in the **Tools** menu, select **NuGet Package Manager** and then **Manage NuGet Packages for Solution...**. 
+1. Open Visual Studio.
+
+1. In the **Tools** menu, select **NuGet Package Manager**, and then select **Manage NuGet Packages for Solution...**.
 
-1. In the **Browse** tab, find and then install **Azure.Search.Documents** (version 11.0 or later). 
+1. On the **Browse** tab, find and install **Azure.Search.Documents** (version 11.0 or later).
 
-1. Search for the **Microsoft.Extensions.Configuration** and **Microsoft.Extensions.Configuration.Json** NuGet packages and install them as well.
+1. Find and install the **Microsoft.Extensions.Configuration** and **Microsoft.Extensions.Configuration.Json** NuGet packages.
 
 1. Open the solution file **/v11/AzureSearchMultipleDataSources.sln**.
 
@@ -134,51 +136,51 @@ Having a valid key establishes trust, on a per request basis, between the applic
     }
     ```
 
-The first two entries are the URL and admin keys of a search service. Use the full endpoint, for example: `https://mydemo.search.windows.net`.
+The first two entries are the URL and admin keys of a search service. Use the full endpoint. For example: `https://mydemo.search.windows.net`.
 
 The next entries specify account names and connection string information for the Azure Blob Storage and Azure Cosmos DB data sources.
 
 ## 3 - Map key fields
 
-Merging content requires that both data streams are targeting the same documents in the search index. 
+Merging content requires that both data streams are targeting the same documents in the search index.
 
 In Azure AI Search, the key field uniquely identifies each document. Every search index must have exactly one key field of type `Edm.String`. That key field must be present for each document in a data source that is added to the index. (In fact, it's the only required field.)
 
-When indexing data from multiple data sources, make sure each incoming row or document contains a common document key to merge data from two physically distinct source documents into a new search document in the combined index. 
+When indexing data from multiple data sources, make sure each incoming row or document contains a common document key. This allows you to merge data from two physically distinct source documents into a new search document in the combined index.
 
-It often requires some up-front planning to identify a meaningful document key for your index, and make sure it exists in both data sources. In this demo, the `HotelId` key for each hotel in Azure Cosmos DB is also present in the rooms JSON blobs in Blob storage.
+It often requires some up-front planning to identify a meaningful document key for your index and to make sure it exists in both data sources. In this demo, the `HotelId` key for each hotel in Azure Cosmos DB is also present in the rooms JSON blobs in Blob storage.
 
-Azure AI Search indexers can use field mappings to rename and even reformat data fields during the indexing process, so that source data can be directed to the correct index field. For example, in Azure Cosmos DB, the hotel identifier is called **`HotelId`**. But in the JSON blob files for the hotel rooms, the hotel identifier is  named **`Id`**. The program handles this discrepancy by mapping the **`Id`** field from the blobs to the **`HotelId`** key field in the indexer.
+Azure AI Search indexers can use field mappings to rename and even reformat data fields during the indexing process, so that source data can be directed to the correct index field. For example, in Azure Cosmos DB, the hotel identifier is called **`HotelId`**, but in the JSON blob files for the hotel rooms, the hotel identifier is  named **`Id`**. The program handles this discrepancy by mapping the **`Id`** field from the blobs to the **`HotelId`** key field in the indexer.
 
 > [!NOTE]
-> In most cases, auto-generated document keys, such as those created by default by some indexers, do not make good document keys for combined indexes. In general you will want to use a meaningful, unique key value that already exists in, or can be easily added to, your data sources.
+> In most cases, autogenerated document keys, such as those created by default by some indexers, don't make good document keys for combined indexes. In general, use a meaningful, unique key value that already exists in your data sources or can be easily added.
 
 ## 4 - Explore the code
 
-Once the data and configuration settings are in place, the sample program in **/v11/AzureSearchMultipleDataSources.sln** should be ready to build and run.
+When the data and configuration settings are in place, the sample program in **/v11/AzureSearchMultipleDataSources.sln** should be ready to build and run.
 
 This simple C#/.NET console app performs the following tasks:
 
-* Creates a new index based on the data structure of the C# Hotel class (which also references the Address and Room classes).
+* Creates a new index based on the data structure of the C# Hotel class, which also references the Address and Room classes.
 * Creates a new data source and an indexer that maps Azure Cosmos DB data to index fields. These are both objects in Azure AI Search.
-* Runs the indexer to load Hotel data from Azure Cosmos DB.
+* Runs the indexer to load hotel data from Azure Cosmos DB.
 * Creates a second data source and an indexer that maps JSON blob data to index fields.
-* Runs the second indexer to load Rooms data from Blob storage.
+* Runs the second indexer to load hotel room data from Blob storage.
 
  Before running the program, take a minute to study the code and the index and indexer definitions for this sample. The relevant code is in two files:
 
-  + **Hotel.cs** contains the schema that defines the index
-  + **Program.cs** contains functions that create the Azure AI Search index, data sources, and indexers, and load the combined results into the index.
+* **Hotel.cs** contains the schema that defines the index.
+* **Program.cs** contains functions that create the Azure AI Search index, data sources, and indexers, and load the combined results into the index.
 
 ### Create an index
 
 This sample program uses [CreateIndexAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindexasync) to define and create an Azure AI Search index. It takes advantage of the [FieldBuilder](/dotnet/api/azure.search.documents.indexes.fieldbuilder) class to generate an index structure from a C# data model class.
 
 The data model is defined by the Hotel class, which also contains references to the Address and Room classes. The FieldBuilder drills down through multiple class definitions to generate a complex data structure for the index. Metadata tags are used to define the attributes of each field, such as whether it's searchable or sortable.
 
-The program will delete any existing index of the same name before creating the new one, in case you want to run this example more than once.
+The program deletes any existing index of the same name before creating the new one, in case you want to run this example more than once.
 
-The following snippets from the Hotel.cs file show single fields, followed by a reference to another data model class, Room[], which in turn is defined in **Room.cs** file (not shown).
+The following snippets from the **Hotel.cs** file show single fields, followed by a reference to another data model class, Room[], which in turn is defined in **Room.cs** file (not shown).
 
 ```csharp
 . . .
@@ -209,9 +211,9 @@ private static async Task CreateIndexAsync(string indexName, SearchIndexClient i
 
 ### Create Azure Cosmos DB data source and indexer
 
-Next the main program includes logic to create the Azure Cosmos DB data source for the hotels data.
+The main program includes logic to create the Azure Cosmos DB data source for the hotels data.
 
-First it concatenates the Azure Cosmos DB database name to the connection string. Then it defines a [SearchIndexerDataSourceConnection](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) object.
+First, it concatenates the Azure Cosmos DB database name to the connection string. It then defines a [SearchIndexerDataSourceConnection](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) object.
 
 ```csharp
 private static async Task CreateAndRunCosmosDbIndexerAsync(string indexName, SearchIndexerClient indexerClient)
@@ -235,9 +237,9 @@ private static async Task CreateAndRunCosmosDbIndexerAsync(string indexName, Sea
 
 After the data source is created, the program sets up an Azure Cosmos DB indexer named **hotel-rooms-cosmos-indexer**.
 
-The program will update any existing indexers with the same name, overwriting the existing indexer with the content of the above code. It also includes reset and run actions, in case you want to run this example more than once.
+The program updates any existing indexers with the same name, overwriting the existing indexer with the content of the previous code. It also includes reset and run actions, in case you want to run this example more than once.
 
-The following example defines a schedule for the indexer, so that it will run once per day. You can remove the schedule property from this call if you don't want the indexer to automatically run again in the future.
+The following example defines a schedule for the indexer, so that it runs once per day. You can remove the schedule property from this call if you don't want the indexer to automatically run again in the future.
 
 ```csharp
 SearchIndexer cosmosDbIndexer = new SearchIndexer(
@@ -279,7 +281,7 @@ catch (RequestFailedException ex) when (ex.Status == 429)
 
 This example includes a simple try-catch block to report any errors that might occur during execution.
 
-After the Azure Cosmos DB indexer has run, the search index will contain a full set of sample hotel documents. However the rooms field for each hotel will be an empty array, since the Azure Cosmos DB data source omits room details. Next, the program will pull from Blob storage to load and merge the room data.
+After the Azure Cosmos DB indexer runs, the search index contains a full set of sample hotel documents. However, the rooms field for each hotel is an empty array, since the Azure Cosmos DB data source omits room details. Next, the program pulls from Blob storage to load and merge the room data.
 
 ### Create Blob storage data source and indexer
 
@@ -303,9 +305,9 @@ After the data source is created, the program sets up a blob indexer named **hot
 
 The JSON blobs contain a key field named **`Id`** instead of **`HotelId`**. The code uses the `FieldMapping` class to tell the indexer to direct the **`Id`** field value to the **`HotelId`** document key in the index.
 
-Blob storage indexers can use [IndexingParameters](/dotnet/api/azure.search.documents.indexes.models.indexingparameters) to specify a parsing mode. You should set different parsing modes depending on whether blobs represent a single document, or multiple documents within the same blob. In this example, each blob represents a single JSON document, so the code uses the `json` parsing mode. For more information about indexer parsing parameters for JSON blobs, see [Index JSON blobs](search-howto-index-json-blobs.md).
+Blob storage indexers can use [IndexingParameters](/dotnet/api/azure.search.documents.indexes.models.indexingparameters) to specify a parsing mode. You should set different parsing modes depending on whether blobs represent a single document or multiple documents within the same blob. In this example, each blob represents a single JSON document, so the code uses the `json` parsing mode. For more information about indexer parsing parameters for JSON blobs, see [Index JSON blobs](search-howto-index-json-blobs.md).
 
-This example defines a schedule for the indexer, so that it will run once per day. You can remove the schedule property from this call if you don't want the indexer to automatically run again in the future.
+This example defines a schedule for the indexer, so that it runs once per day. You can remove the schedule property from this call if you don't want the indexer to automatically run again in the future.
 
 ```csharp
 IndexingParameters parameters = new IndexingParameters();
@@ -344,21 +346,20 @@ catch (CloudException e) when (e.Response.StatusCode == (HttpStatusCode)429)
 }
 ```
 
-Because the index has already been populated with hotel data from the Azure Cosmos DB database, 
-the blob indexer updates the existing documents in the index and adds the room details.
+Because the index is already populated with hotel data from the Azure Cosmos DB database, the blob indexer updates the existing documents in the index and adds the room details.
 
 > [!NOTE]
-> If you have the same non-key fields in both of your data sources, and the data within those fields does not match, then the index will contain the values from whichever indexer ran most recently. In our example, both data sources contain a **HotelName** field. If for some reason the data in this field is different, for documents with the same key value, then the **HotelName** data from the data source that was indexed most recently will be the value stored in the index.
+> If you have the same non-key fields in both of your data sources, and the data in those fields doesn't match, the index contains the values from whichever indexer ran most recently. In our example, both data sources contain a **HotelName** field. If for some reason the data in this field is different, for documents with the same key value, the **HotelName** data from the most recently indexed data source is the value stored in the index.
 
 ## 5 - Search
 
-You can explore the populated search index after the program has run, using the [**Search explorer**](search-explorer.md) in the Azure portal.
+After running the program, you can explore the populated search index using the [**Search explorer**](search-explorer.md) in the Azure portal.
 
-In Azure portal, open the search service **Overview** page, and find the **hotel-rooms-sample** index in the **Indexes** list.
+In the portal, go to the **Overview** page of your search service, and then find the **hotel-rooms-sample** index in the **Indexes** list.
 
   :::image type="content" source="media/tutorial-multiple-data-sources/index-list.png" alt-text="List of Azure AI Search indexes" border="false":::
 
-Select on the hotel-rooms-sample index in the list. You'll see a Search Explorer interface for the index. Enter a query for a term like "Luxury". You should see at least one document in the results, and this document should show a list of room objects in its rooms array.
+Select the **hotel-rooms-sample** index to see a Search explorer interface for the index. Enter a query for a term like "Luxury". You should see at least one document in the results, and this document should show a list of room objects in its rooms array.
 
 ## Reset and rerun
 
@@ -370,13 +371,13 @@ You can also use the Azure portal to delete indexes, indexers, and data sources.
 
 ## Clean up resources
 
-When you're working in your own subscription, at the end of a project, it's a good idea to remove the resources that you no longer need. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
+When you're working in your own subscription, at the end of a project, it's a good idea to remove the resources you no longer need. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
 
-You can find and manage resources in the Azure portal, using the All resources or Resource groups link in the left-navigation pane.
+You can find and manage resources in the Azure portal using the All resources or Resource groups link in the left pane.
 
-## Next steps
+## Next step
 
-Now that you're familiar with the concept of ingesting data from multiple sources, let's take a closer look at indexer configuration, starting with Azure Cosmos DB.
+Now that you're familiar with the concept of ingesting data from multiple sources, take a closer look at indexer configuration, starting with Azure Cosmos DB:
 
 > [!div class="nextstepaction"]
 > [Configure an Azure Cosmos DB for NoSQL indexer](search-howto-index-cosmosdb.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "複数のデータソースのインデックス作成に関するC#チュートリアルの更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchの「複数データソースからのインデックス作成に関するC#チュートリアル」文書の更新を示しています。以下の主な修正点があります：

- タイトルが修正され、「C# チュートリアル: 複数の Azure データソースをインデックス化」となり、より明確な表現になりました。
- 最終更新日が「2024年12月10日」から「2025年3月10日」に変更されました。
- 説明文や各ステップの指示が明確化され、文が簡潔になりました。たとえば、「このチュートリアルでは、次のタスクを実行します」と修正されています。
- コード例および設定手順がわかりやすく整理され、プログラムの実行手順が明確に示されています。
- テキストの整形や言い回しが見直され、全体的な可読性と理解しやすさが向上しています。

この更新により、ユーザーは複数のデータソースからデータをインデックス化するプロセスをより簡単に理解し、実施できるようになっています。変更には、66行の追加、65行の削除が含まれ、合計131行が修正されています。全体として、チュートリアルの情報が最新かつ的確になっています。


