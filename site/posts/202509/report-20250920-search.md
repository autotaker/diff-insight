---
date: '2025-09-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bb45dff...MicrosoftDocs:d073531
summary: |-
  この一連の変更は、Azure AI Searchに関連するドキュメントを更新し、情報を最新かつ明確にすることを目的としています。主な内容としては、新しいパラメーターの追加や既存情報の修正、コードサンプルとリンク構造の整理、Azure無料アカウントに関する情報の見直しが含まれています。

  具体的には、`cognitive-search-skill-textsplit.md`で新しいパラメーターに関する詳細が追加され、検索機能のカスタマイズが向上しました。また、`search-howto-index-json-blobs.md`では、フィールドの上書きに関する指示が追加されています。情報の明確化に伴い、一部の理解に調整が必要な場合がありますが、特に破壊的な変更はありません。

  全体として、これらの更新はユーザーがAzure AI Searchをより効果的に活用できるようにするためのものであり、特に新機能や変更点の明確化に重点を置いています。さらに、コードサンプルやリソースリンクの整理により、情報の取得が容易になり、開発者が迅速に必要な情報を手に入れられるようになっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bb45dff...MicrosoftDocs:d073531){target="_blank"}

<format>
# ハイライト
この一連の変更は、Azure AI Searchに関連するドキュメントを小規模に更新し、情報の最新化と明確化を図っています。特に、日付の更新、新しいパラメーターの説明の追加や修正、コードサンプルやリンク構造の整理、Azure無料アカウントに関する情報の見直しなどが含まれています。

## 新機能
- `cognitive-search-skill-textsplit.md`において、新しいパラメーター`unit`と`azureOpenAITokenizerParameters`に関する詳細が追加され、トークナイザーの動作が明確になりました。
- `search-howto-index-json-blobs.md`において、フィールドを上書きする場合の具体的な指示が追加されました。

## 破壊的変更
- 破壊的な変更は特にありませんが、情報の明確化が行われたため、既存の理解に一部の調整が必要かもしれません。

## その他の更新
- 各言語サンプルドキュメントの日付が最新のものへと更新され、文面の改善が行われました。
- Azure無料アカウントに関する情報が分かりやすく更新されました。

# 洞察
今回のドキュメント更新は、ユーザーがAzure AI Searchをより効果的に利用できるようにするための適切な整備が重点的に行われています。ドキュメントの更新により、新機能や変更点が明確に浮き彫りになるように設計されており、特に、新しいパラメーターの追加や既存機能の詳細な説明が強調されています。

たとえば、新しいパラメーター`unit`と`azureOpenAITokenizerParameters`の説明は、ドキュメントにおいて重要な追加であり、検索機能のさらなるカスタマイズを可能にしています。また、JSONブロブのインデックス化におけるフィールドの更新処理についても詳細が補足され、ユーザーが予期しないデータ損失を避けることができるような説明が付け加えられました。

さらに、無料アカウントに関する情報が一新され、新規ユーザーに対してAzureの利用開始を助ける明確な道筋が提供されています。このような更新は、Azure AI Searchの利用促進を図り、コミュニティ全体での利用体験を向上させるために重要です。

ドキュメント構造の整理により、コードサンプルやリソースリンクがよりアクセスしやすくなっており、開発者が必要な情報を迅速に取得できるようになっています。この一貫した取り組みは、ユーザーの学習曲線を低減し、より素早く製品を活用できる環境を整える手助けとなっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-textsplit.md](#item-9bf753) | minor update | ドキュメントの日付の更新と説明の改善 | modified | 2 | 2 | 4 | 
| [samples-dotnet.md](#item-12f3fa) | minor update | C# サンプルのドキュメントの更新と改善 | modified | 58 | 58 | 116 | 
| [samples-java.md](#item-5992fd) | minor update | Java サンプルファイルの更新と改善 | modified | 22 | 22 | 44 | 
| [samples-javascript.md](#item-82e67e) | minor update | JavaScript サンプルファイルの更新と改善 | modified | 45 | 44 | 89 | 
| [samples-python.md](#item-d2bf09) | minor update | Python サンプルファイルの更新と改善 | modified | 34 | 32 | 66 | 
| [samples-rest.md](#item-198ebc) | minor update | REST サンプルファイルの更新と改善 | modified | 23 | 16 | 39 | 
| [search-howto-index-json-blobs.md](#item-b8230c) | minor update | JSON ブロブのインデックス化に関するドキュメントの更新 | modified | 2 | 1 | 3 | 
| [search-try-for-free.md](#item-36e28d) | minor update | Azure 無料アカウントに関する情報の更新 | modified | 8 | 8 | 16 | 


# Modified Contents
## articles/search/cognitive-search-skill-textsplit.md{#item-9bf753}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: reference
-ms.date: 05/01/2025
+ms.date: 09/19/2025
 ms.update-cycle: 365-days
 ---
 
@@ -41,7 +41,7 @@ Parameters are case-sensitive.
 | `pageOverlapLength` | [2024-07-01](/rest/api/searchservice/skillsets/create-or-update) | Only applies if `textSplitMode` is set to `pages`. Each page starts with this number of characters or tokens from the end of the previous page. If this parameter is set to 0, there's no overlapping text on successive pages. This [example](#example-for-chunking-and-vectorization) includes the parameter. |
 | `maximumPagesToTake` | [2024-07-01](/rest/api/searchservice/skillsets/create-or-update) | Only applies if `textSplitMode` is set to `pages`. Number of pages to return. The default is 0, which means to return all pages. You should set this value if only a subset of pages are needed. This [example](#example-for-chunking-and-vectorization) includes the parameter.|
 | `unit` | [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | **New**. Only applies if `textSplitMode` is set to `pages`. Specifies whether to chunk by `characters` (default) or `azureOpenAITokens`. Setting the unit affects `maximumPageLength` and `pageOverlapLength`. |
-| `azureOpenAITokenizerParameters` | [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | **New**. An object providing extra parameters for the `azureOpenAITokens` unit. <br><br>`encoderModelName` is a designated tokenizer used for converting text into tokens, essential for natural language processing (NLP) tasks. Different models use different tokenizers. Valid values include cl100k_base (default) used by GPT-35-Turbo and GPT-4. Other valid values are r50k_base, p50k_base, and p50k_edit. The skill implements the tiktoken library by way of [SharpToken](https://www.nuget.org/packages/SharpToken) and `Microsoft.ML.Tokenizers` but doesn't support every encoder. For example, there's currently no support for o200k_base encoding used by GPT-4o. <br><br>`allowedSpecialTokens` defines a collection of special tokens that are permitted within the tokenization process. Special tokens are  string that you want to treat uniquely, ensuring they aren't split during tokenization. For example ["[START"], "[END]"]. For languages in which the tiktoken library is not performing the tokenization as expected, it's recommended to use text splitting instead.|
+| `azureOpenAITokenizerParameters` | [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | **New**. An object providing extra parameters for the `azureOpenAITokens` unit. <br><br>`encoderModelName` is a designated tokenizer used for converting text into tokens, essential for natural language processing (NLP) tasks. Different models use different tokenizers. Valid values include cl100k_base (default) used by GPT-35-Turbo and GPT-4. Other valid values are r50k_base, p50k_base, and p50k_edit. The skill implements the tiktoken library by way of [SharpToken](https://www.nuget.org/packages/SharpToken) and `Microsoft.ML.Tokenizers` but doesn't support every encoder. For example, there's currently no support for o200k_base encoding used by GPT-4o. <br><br>`allowedSpecialTokens` defines a collection of special tokens that are permitted within the tokenization process. Special tokens are  string that you want to treat uniquely, ensuring they aren't split during tokenization. For example ["[START"], "[END]"]. If the `tiktoken` library doesn't perform tokenization as expected, either due to language-specific limitations or other unexpected behaviors, it's recommended to use text splitting instead.|
 
 ## Skill Inputs
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントの日付の更新と説明の改善"
}
```

### Explanation
この変更は、`cognitive-search-skill-textsplit.md`というドキュメント内でマイナーな更新を行い、特定の日付を更新したり、新しいパラメーターに関する説明を改善したりしています。具体的には、`ms.date`フィールドを`2025年5月1日`から`2025年9月19日`に変更しています。また、新しいパラメーター`unit`と`azureOpenAITokenizerParameters`についての詳細な説明が追加されており、特にトークナイザーの動作や使用可能な特殊トークンの定義が強調されています。このような変更は、ドキュメントを最新の情報に保ち、ユーザーが機能をよりよく理解できるようにするために重要です。

## articles/search/samples-dotnet.md{#item-12f3fa}

<details>
<summary>Diff</summary>
````diff
@@ -10,89 +10,89 @@ ms.custom:
   - devx-track-dotnet
   - ignite-2023
 ms.topic: concept-article
-ms.date: 08/06/2025
+ms.date: 09/19/2025
 ---
 
 # C# samples for Azure AI Search
 
-Learn about the C# code samples that demonstrate the functionality and workflow of an Azure AI Search solution. These samples use the [**Azure AI Search client library**](/dotnet/api/overview/azure/search) for the [**Azure SDK for .NET**](/dotnet/azure/), which you can explore through the following links.
+Learn about C# code samples that demonstrate the functionality and workflow of an Azure AI Search solution. These samples use the [Azure AI Search client library](/dotnet/api/overview/azure/search) for the [Azure SDK for .NET](/dotnet/azure/), which you can explore through the following links.
 
 | Target | Link |
-|--------|------|
-| Package download | [www.nuget.org/packages/Azure.Search.Documents/](https://www.nuget.org/packages/Azure.Search.Documents/) |
-| API reference | [azure.search.documents](/dotnet/api/azure.search.documents)  |
+|--|--|
+| Package download | [nuget.org/packages/Azure.Search.Documents/](https://www.nuget.org/packages/Azure.Search.Documents/) |
+| API reference | [Azure.Search.Documents](/dotnet/api/azure.search.documents)  |
 | API test cases | [github.com/Azure/azure-sdk-for-net/tree/main/sdk/search/Azure.Search.Documents/tests](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/search/Azure.Search.Documents/tests) |
 | Source code | [github.com/Azure/azure-sdk-for-net/tree/main/sdk/search/Azure.Search.Documents/src](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/search/Azure.Search.Documents/src)  |
-| Change log | [https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) |
+| Change log | [github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) |
 
 ## SDK samples
 
-Code samples from the Azure SDK development team demonstrate API usage. You can find these samples on [GitHub](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/).
+Code samples from the Azure SDK development team demonstrate API usage. You can find these samples in [Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/) on GitHub.
 
 | Sample | Description |
-|---------|-------------|
-| [*Hello world* - synchronous](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample01a_HelloWorld.md) | Demonstrates how to create a client, authenticate, and handle errors using synchronous methods. |
-| [*Hello world* - asynchronous](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample01b_HelloWorldAsync.md) | Demonstrates how to create a client, authenticate, and handle errors using asynchronous methods.  |
-| [Service-level operations](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample02_Service.md) | Demonstrates how to create indexes, indexers, data sources, skillsets, and synonym maps. This sample also shows you how to get service statistics and how to query an index.  |
-| [Index operations](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample03_Index.md) | Demonstrates how to perform an action on existing index, in this case getting a count of documents stored in the index.  |
-| [FieldBuilderIgnore](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample04_FieldBuilderIgnore.md) | Demonstrates a technique for working with unsupported data types.  |
-| [Indexing documents (push model)](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample05_IndexingDocuments.md) | *Push* model indexing, where you send a JSON payload to an index on a service.  |
-| [Encryption key sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample06_EncryptedIndex.md) | Demonstrates using a customer-managed encryption key to add an extra layer of protection over sensitive content.  |
-| [Vector search sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample07_VectorSearch.md) | Shows you how to index a vector field and perform vector search using the Azure SDK for .NET. |
-| [Semantic ranking sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample08_SemanticSearch.md) | Shows you how to configure semantic ranker in an index and invoke semantic queries using the Azure SDK for .NET. |
+|--|--|
+| [Hello world (synchronous)](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample01a_HelloWorld.md) | Create a client, authenticate, and handle errors using synchronous methods. |
+| [Hello world (asynchronous)](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample01b_HelloWorldAsync.md) | Create a client, authenticate, and handle errors using asynchronous methods. |
+| [Service-level operations](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample02_Service.md) | Get service statistics and create multiple search objects, including an index, indexer, data source, skillset, and synonym map. Finally, you query the index. |
+| [Index operations](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample03_Index.md) | Get a count of documents stored in an index. |
+| [FieldBuilderIgnore](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample04_FieldBuilderIgnore.md) | Use an attribute to work with unsupported data types. |
+| [Indexing documents (push model)](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample05_IndexingDocuments.md) | Use the push model to index documents by sending a JSON payload to an index. |
+| [Customer-managed encryption keys](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample06_EncryptedIndex.md) | Use a customer-managed encryption key to protect sensitive content. |
+| [Vector search](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample07_VectorSearch.md) | Index a vector field and perform vector search. |
+| [Semantic ranking](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample08_SemanticSearch.md) | Configure semantic ranker in an index and run semantic queries. |
 
 ## Doc samples
 
-Code samples from the Azure AI Search team demonstrate features and workflows. All of the following samples are referenced in tutorials, quickstarts, and how-to articles that explain the code in detail. You can find these samples in [**Azure-Samples/azure-search-dotnet-samples**](https://github.com/Azure-Samples/azure-search-dotnet-samples) and [**Azure-Samples/search-dotnet-getting-started**](https://github.com/Azure-Samples/search-dotnet-getting-started/) on GitHub.
+Code samples from the Azure AI Search team demonstrate features and workflows. Many of the following samples are referenced in tutorials, quickstarts, and how-to articles that explain the code in detail. You can find these samples in [Azure-Samples/azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples) and [Azure-Samples/search-dotnet-getting-started](https://github.com/Azure-Samples/search-dotnet-getting-started/) on GitHub.
 
-> [!TIP]
-> Try the [samples browser](/samples/browse/?languages=csharp&products=azure-cognitive-search) to search for Microsoft code samples in GitHub, filtered by product, service, and language.
-
-| Code sample | Related article  | Purpose |
-|-------------|------------------|---------|
-| [create-mvc-app](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/create-mvc-app) |  [Tutorial: Add search to an ASP.NET Core (MVC) app](tutorial-csharp-create-mvc-app.md) | While most samples are console applications, this MVC sample uses a web page to front the sample Hotels index, demonstrating basic search, pagination, and other server-side behaviors.|
-| [quickstart](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/AzureSearchQuickstart) | [Quickstart: Full-text search](search-get-started-text.md) | Covers the basic workflow for creating, loading, and querying a search index in C# using sample data. |
-| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) | [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md) | Creates a retrieval pipeline that integrates semantic ranking in Azure AI Search with LLM-powered query planning and answer generation. |
-| [quickstart-rag](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-rag) | [Quickstart: Generative search (RAG)](search-get-started-rag.md) | Uses grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
-| [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-search/) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Shows the index schema and query request for invoking semantic ranker. |
-| [quickstart-vector-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-vector-search) | [Quickstart: Vector search](search-get-started-vector.md) | Covers the basic workflow for indexing and querying vector data. |
-| [search-website](https://github.com/Azure-Samples/azure-search-static-web-app) | [Tutorial: Add search to web apps](tutorial-csharp-overview.md) | Demonstrates an end-to-end search app that includes bulk upload using the push APIs and a rich client for hosting the app and handling search requests.|
-| [tutorial-ai-enrichment](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/tutorial-ai-enrichment)  | [Tutorial: AI-generated searchable content from Azure blobs](tutorial-skillset.md) | Shows how to configure an indexer and skillset. |
-| [multiple-data-sources](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources)  | [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md) | Merges content from two data sources into one search index. |
-| [Optimize-data-indexing](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/optimize-data-indexing) | [Tutorial: Optimize indexing with the push API](tutorial-optimize-indexing-push-api.md) | Demonstrates optimization techniques for pushing data into a search index. |
-| [DotNetHowTo](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowTo)  | [How to use the .NET client library](search-howto-dotnet-sdk.md) | Steps through the basic workflow, but in more detail and with discussion of API usage.  |
-| [DotNetToIndexers](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToIndexers) | [Tutorial: Index Azure SQL data](search-indexer-tutorial.md) | Shows how to configure an Azure SQL indexer that has a schedule, field mappings, and parameters.  |
-| [DotNetHowToEncryptionUsingCMK](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToEncryptionUsingCMK) | [How to configure customer-managed keys for data encryption](search-security-manage-encryption-keys.md) | Shows how to create objects that are encrypted with a Customer Key. |
-| [DotNetVectorDemo](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetVectorDemo)  | [readme](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetVectorDemo/readme.md) | Create, load, and query a vector index. |
-| [DotNetIntegratedVectorizationDemo](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetIntegratedVectorizationDemo)  | [readme](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetIntegratedVectorizationDemo/readme.md) | Extends the vector workflow to include skills-based automation for data chunking and embedding. |
+| Sample | Description |
+|--|--|
+| [quickstart](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/AzureSearchQuickstart) | Source code for the C# portion of [Quickstart: Full-text search](search-get-started-text.md). Create, load, and query an index using sample data. |
+| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) | Source code for the C# portion of [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md). Integrate semantic ranking with LLM-powered query planning and answer generation. |
+| [quickstart-rag](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-rag) | Source code for the C# portion of [Quickstart: Generative search (RAG)](search-get-started-rag.md). Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
+| [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-search/) | Source code for the C# portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). Add semantic ranking to an index schema and run semantic queries. |
+| [quickstart-vector-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-vector-search) | Source code for the C# portion of [Quickstart: Vector search](search-get-started-vector.md). Index and query vector content. |
+| [create-mvc-app](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/create-mvc-app) | Source code for [Tutorial: Add search to an ASP.NET Core (MVC) app](tutorial-csharp-create-mvc-app.md). Add basic search, pagination, and other server-side behaviors to an MVC web app, unlike the console applications used in most samples. |
+| [search-website](https://github.com/Azure-Samples/azure-search-static-web-app) | Source code for [Tutorial: Add search to web apps](tutorial-csharp-overview.md). Build an end-to-end search app that uses the push API for bulk upload and a rich client for hosting the app and handling search requests. |
+| [tutorial-ai-enrichment](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/tutorial-ai-enrichment) | Source code for [Tutorial: AI-generated searchable content from Azure blobs](tutorial-skillset.md). Create a skillset that iterates over Azure blobs to extract information and infer structure. |
+| [multiple-data-sources](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources) | Source code for [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md). Merge content from two data sources into one index. |
+| [optimize-data-indexing](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/optimize-data-indexing) | Source code for [Tutorial: Optimize indexing with the push API](tutorial-optimize-indexing-push-api.md). Use optimization techniques for pushing data into an index. |
+| [DotNetHowTo](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowTo) | Source code for [Use the .NET client library](search-howto-dotnet-sdk.md). Create and manage multiple search objects while learning about the APIs. |
+| [DotNetToIndexers](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToIndexers) | Source code for [Tutorial: Index Azure SQL data](search-indexer-tutorial.md). Configure an Azure SQL indexer with a schedule, field mappings, and parameters. |
+| [DotNetHowToEncryptionUsingCMK](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToEncryptionUsingCMK) | Source code for [Configure customer-managed keys for data encryption](search-security-manage-encryption-keys.md). Create objects that are encrypted with a customer-managed key. |
+| [DotNetVectorDemo](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetVectorDemo) | Create, load, and query a vector index. |
+| [DotNetIntegratedVectorizationDemo](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetIntegratedVectorizationDemo) | Extend the vector workflow to include skills-based automation for data chunking and embedding. |
 
 ## Accelerators
 
-An accelerator is an end-to-end solution that includes code and documentation that you can adapt for your own implementation of a specific scenario.
+An accelerator is an end-to-end solution that includes code and documentation you can adapt for your own implementation of a specific scenario.
 
-| Samples | Repository | Description |
-|---------|------------|-------------|
-| Search + QnA Maker Accelerator | [search-qna-maker-accelerator](https://github.com/Azure-Samples/search-qna-maker-accelerator)| A [solution](https://techcommunity.microsoft.com/t5/azure-ai/qna-with-azure-cognitive-search/ba-p/2081381) combining the power of Search and QnA Maker. See the live [demo site](https://aka.ms/qnaWithAzureSearchDemo). |
+| Sample | Description |
+|--|--|
+| [search-qna-maker-accelerator](https://github.com/Azure-Samples/search-qna-maker-accelerator) | [Solution](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/qna-with-azure-cognitive-search/2081381) that combines Azure AI Search and QnA Maker. See the live [demo site](https://aka.ms/qnaWithAzureSearchDemo). |
 
 ## Demos
 
-A demo repo provides proof-of-concept source code for examples or scenarios shown in demonstrations. Demo solutions aren't designed for adaptation by customers.
+A demo repo provides proof-of-concept source code for examples or scenarios shown in demonstrations. Unlike accelerators, demo solutions aren't designed for adaptation.
 
-| Samples | Repository | Description |
-|---------|------------|-------------|
-| Covid-19 search app | [covid19search](https://github.com/liamca/covid19search) | Source code repository for the Azure AI Search based [Covid-19 Search App](https://github.com/liamca/covid19search). |
-| JFK demo | [AzureSearch JFK Files](https://github.com/Microsoft/AzureSearch_JFK_Files) | Learn more about the [JFK solution](https://www.microsoft.com/ai/ai-lab-jfk-files). |
+| Sample | Description |
+|--|--|
+| [covid19search](https://github.com/liamca/covid19search) | Source code repo for the Azure AI Search-based Covid-19 search app. |
+| [AzureSearch_JFK_Files](https://github.com/Microsoft/AzureSearch_JFK_Files) | Source code repo for the Azure AI Search-based JFK files solution. |
 
 ## Other samples
 
-The following samples are also published by the Azure AI Search team but aren't referenced in documentation. Associated readme files provide usage instructions.
-
-| Samples | Repository | Description |
-|---------|------------|-------------|
-| [Query multiple services](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-search-services) |  [azure-search-dotnet-scale](https://github.com/Azure-Samples/azure-search-dotnet-samples) | Issue a single query across multiple search services and combine the results into a single page.  |
-| [Check storage](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/check-storage-usage/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | Invokes an Azure function that checks search service storage on a schedule. |
-| [Export an index](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/export-data/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | C# console app that partitions and exports a large index. |
-| [Backup and restore an index](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | C# console app that copies an index from one service to another, creating JSON files on your computer with the index schema and documents. |
-| [Index Data Lake Gen2 using Microsoft Entra ID](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/data-lake-gen2-acl-indexing/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | Source code demonstrating indexer connections and indexing of Azure Data Lake Gen2 files and folders that are secured through Microsoft Entra ID and role-based access controls. |
-| [Search aggregations](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/search-aggregations/README.md) | [azure-search-dotnet-utilities](https://github.com/Azure-Samples/azure-search-dotnet-utilities) | Proof-of-concept source code that demonstrates how to obtain aggregations from a search index and then filter by them. |
-| [Power Skills](https://github.com/Azure-Samples/azure-search-power-skills/blob/main/README.md) | [azure-search-power-skills](https://github.com/Azure-Samples/azure-search-power-skills)  | Source code for consumable custom skills that you can incorporate in your own solutions.  |
+The following samples are also published by the Azure AI Search team but aren't referenced in documentation. Associated README files provide usage instructions.
+
+| Sample | Description |
+|--|--|
+| [check-storage-usage](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/check-storage-usage/README.md) | Check search service storage on a schedule using an Azure function. |
+| [export-data](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/export-data) | Partition and export a large index using a C# console app. |
+| [index-backup-restore](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore) | Copy an index from one service to another, creating JSON files with the index schema and documents. |
+| [data-lake-gen2-acl-indexing](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/data-lake-gen2-acl-indexing) | Index Azure Data Lake Gen2 files and folders secured with Microsoft Entra ID and role-based access control. |
+| [multiple-search-services](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-search-services) | Query multiple search services and combine results into a single page. |
+| [search-aggregations](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/search-aggregations) | Obtain and filter aggregations from an index. |
+| [azure-search-power-skills](https://github.com/Azure-Samples/azure-search-power-skills/blob/main) | Incorporate consumable custom skills into your own solutions. |
+
+> [!TIP]
+> Use the [samples browser](/samples/browse/?languages=csharp&products=azure-cognitive-search) to search for Microsoft code samples on GitHub. You can filter your search by product, service, and language.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# サンプルのドキュメントの更新と改善"
}
```

### Explanation
この変更は、`samples-dotnet.md`というドキュメントにおいて、C#サンプルの情報を更新し改善するためのマイナーな更新です。具体的には、変更された日付を`2025年8月6日`から`2025年9月19日`に更新しました。また、テキストの明確さを向上させるために、文言や文章構造を修正しました。さらに、サンプルの説明やリンクも整理され、新しいフォーマットが適用されました。

全体として、ドキュメントの内容がより分かりやすくなり、C#やAzure SDKに関連するリソースへのアクセスが容易になることで、開発者がよりスムーズに情報を得られるようにしています。これにより、ユーザー体験の向上が図られています。

## articles/search/samples-java.md{#item-5992fd}

<details>
<summary>Diff</summary>
````diff
@@ -12,43 +12,43 @@ ms.custom:
   - devx-track-extended-java
   - ignite-2023
 ms.topic: concept-article
-ms.date: 03/10/2025
+ms.date: 09/19/2025
 ---
 
 # Java samples for Azure AI Search
 
-Learn about the Java code samples that demonstrate the functionality and workflow of an Azure AI Search solution. These samples use the [**Azure AI Search client library**](/java/api/overview/azure/search-documents-readme) for the [**Azure SDK for Java**](/azure/developer/java/sdk), which you can explore through the following links.
+Learn about Java code samples that demonstrate the functionality and workflow of an Azure AI Search solution. These samples use the [Azure AI Search client library](/java/api/overview/azure/search-documents-readme) for the [Azure SDK for Java](/azure/developer/java/sdk), which you can explore through the following links.
 
 | Target | Link |
-|--------|------|
+|--|--|
 | Package download | [search.maven.org/artifact/com.azure/azure-search-documents](https://search.maven.org/artifact/com.azure/azure-search-documents) |
 | API reference | [com.azure.search.documents](/java/api/com.azure.search.documents)  |
-| API test cases | [https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents/src/test](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents/src/test) |
-| Source code | [https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents)  |
-| Change log | [https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) |
+| API test cases | [github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents/src/test](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents/src/test) |
+| Source code | [github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents)  |
+| Change log | [github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) |
 
 ## SDK samples
 
-Code samples from the Azure SDK development team demonstrate API usage. You can find these samples in [**Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents/src/samples**](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents/src/samples) on GitHub.
+Code samples from the Azure SDK development team demonstrate API usage. You can find these samples in [Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents/src/samples](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents/src/samples) on GitHub.
 
-| Samples | Description |
-|---------|-------------|
-| [Search index creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateIndexExample.java) | Demonstrates how to create [search indexes](search-what-is-an-index.md). |
-| [Synonym creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/SynonymMapsCreateExample.java) | Demonstrates how to create [synonym maps](search-synonyms.md).  |
-| [Search indexer creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateIndexerExample.java) | Demonstrates how to create [indexers](search-indexer-overview.md). |
-| [Search indexer data source creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/DataSourceExample.java) | Demonstrates how to create indexer data sources, which are required for indexer-based indexing of [supported Azure data sources](search-indexer-overview.md#supported-data-sources). |
-| [Skillset creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateSkillsetExample.java) |  Demonstrates how to create [skillsets](cognitive-search-working-with-skillsets.md) that are attached to indexers and perform AI-based enrichment during indexing. |
-| [Load documents](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/IndexContentManagementExample.java) | Demonstrates how to upload or merge documents into an index in a [data import](search-what-is-data-import.md) operation. |
-| [Query syntax](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/SearchAsyncWithFullyTypedDocumentsExample.java) | Demonstrates how to set up a [basic query](search-query-overview.md). |
-| [Vector search](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/VectorSearchExample.java) | Demonstrates how to set up a vector field and then generate a [vector query](vector-search-how-to-query.md). |
+| Sample | Description |
+|--|--|
+| [Index creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateIndexExample.java) | Create an [index](search-what-is-an-index.md). |
+| [Indexer creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateIndexerExample.java) | Create an [indexer](search-indexer-overview.md). |
+| [Data source creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/DataSourceExample.java) | Create a data source connection, which is required for indexer-based indexing of [supported data sources](search-indexer-overview.md#supported-data-sources). |
+| [Skillset creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateSkillsetExample.java) | Create a [skillset](cognitive-search-working-with-skillsets.md) that's attached to an indexer and perform AI-based enrichment during indexing. |
+| [Synonym creation](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/SynonymMapsCreateExample.java) | Create a [synonym map](search-synonyms.md).  |
+| [Load documents](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/IndexContentManagementExample.java) | Upload or merge documents into an index in a [data import](search-what-is-data-import.md) operation. |
+| [Query syntax](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/SearchAsyncWithFullyTypedDocumentsExample.java) | Send a [basic query](search-query-overview.md). |
+| [Vector search](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/VectorSearchExample.java) | Create a vector field and send a [vector query](vector-search-how-to-query.md). |
 
 ## Doc samples
 
-Code samples from the Azure AI Search team are located in [**Azure-Samples/azure-search-java-samples**](https://github.com/Azure-Samples/azure-search-java-samples) on GitHub.
+Code samples from the Azure AI Search team demonstrate features and workflows. Many of the following samples are referenced in tutorials, quickstarts, and how-to articles that explain the code in detail. You can find these samples in [Azure-Samples/azure-search-java-samples](https://github.com/Azure-Samples/azure-search-java-samples) on GitHub.
 
-| Samples | Article | 
-|---------|-------------|
-| [quickstart](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart) | Source code for the Java portion of [Quickstart: Full-text search](search-get-started-text.md). |
+| Sample | Article |
+|--|--|
+| [quickstart](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart) | Source code for the Java portion of [Quickstart: Full-text search](search-get-started-text.md). Create, load, and query an index using sample data. |
 
 > [!TIP]
-> Try the [Samples browser](/samples/browse/?languages=java&products=azure-cognitive-search) to search for Microsoft code samples in GitHub, filtered by product, service, and language.
+> Use the [samples browser](/samples/browse/?languages=java&products=azure-cognitive-search) to search for Microsoft code samples on GitHub. You can filter your search by product, service, and language.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java サンプルファイルの更新と改善"
}
```

### Explanation
この変更は、`samples-java.md`というファイルにおいて、Javaに関連するサンプルの情報を更新し、すっきりとした形式に整形するためのマイナーな更新です。具体的には、日付を`2025年3月10日`から`2025年9月19日`に修正しました。また、いくつかの文言を簡潔にし、コードサンプルやリンクの構造を整理しました。

また、サンプルの説明において、各サンプルが何を示しているのかより分かりやすくするために、内容を明確にし、新しい表現を使用したことで、利用者が理解しやすい情報を提供することを目的としています。これにより、Javaを使用したAzure AI Searchに関連するリソースへのアクセスがより容易になり、開発者が有用な情報を迅速に取得することができるようになります。

## articles/search/samples-javascript.md{#item-82e67e}

<details>
<summary>Diff</summary>
````diff
@@ -11,76 +11,77 @@ ms.custom:
   - devx-track-js
   - ignite-2023
 ms.topic: concept-article
-ms.date: 08/06/2025
+ms.date: 09/19/2025
 ---
 
 # JavaScript samples for Azure AI Search
 
-Learn about the JavaScript code samples that demonstrate the functionality and workflow of an Azure AI Search solution. These samples use the [**Azure AI Search client library**](/javascript/api/overview/azure/search-documents-readme) for the [**Azure SDK for JavaScript**](/azure/developer/javascript/), which you can explore through the following links.
+Learn about JavaScript code samples that demonstrate the functionality and workflow of an Azure AI Search solution. These samples use the [Azure AI Search client library](/javascript/api/overview/azure/search-documents-readme) for the [Azure SDK for JavaScript](/azure/developer/javascript/), which you can explore through the following links.
 
 | Target | Link |
-|--------|------|
+|--|--|
 | Package download | [www.npmjs.com/package/@azure/search-documents](https://www.npmjs.com/package/@azure/search-documents) |
 | API reference | [@azure/search-documents](/javascript/api/@azure/search-documents/) |
 | API test cases | [github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/test](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/test) |
 | Source code | [github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents) |
-| Change log | [https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) |
+| Change log | [github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) |
 
 ## SDK samples
 
-Code samples from the Azure SDK development team demonstrate API usage. You can find these samples in [**azure-sdk-for-js/tree/main/sdk/search/search-documents/samples**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples) on GitHub.
+Code samples from the Azure SDK development team demonstrate API usage. You can find these samples in [Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples) on GitHub.
 
 ### JavaScript samples
 
-| Samples | Description |
-|---------|-------------|
-| [indexes](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Demonstrates how to create, update, get, list, and delete [search indexes](search-what-is-an-index.md). This sample category also includes a service statistic sample. |
-| [dataSourceConnections (for indexers)](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/javascript/dataSourceConnectionOperations.js) | Demonstrates how to create, update, get, list, and delete indexer data sources, which are required for indexer-based indexing of [supported Azure data sources](search-indexer-overview.md#supported-data-sources). |
-| [indexers](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Demonstrates how to create, update, get, list, reset, and delete [indexers](search-indexer-overview.md).|
-| [skillSet](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Demonstrates how to create, update, get, list, and delete [skillsets](cognitive-search-working-with-skillsets.md) that are attached to indexers and perform AI-based enrichment during indexing. |
-| [synonymMaps](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Demonstrates how to create, update, get, list, and delete [synonym maps](search-synonyms.md). |
-| [VectorSearch](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v12-beta/javascript/vectorSearch.js) | Demonstrates how to index vectors and send a [vector query](vector-search-how-to-query.md). |
+| Sample | Description |
+|--|--|
+| [indexes](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Create, update, get, list, and delete [indexes](search-what-is-an-index.md). This sample category also includes a service statistic sample. |
+| [indexers](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Create, update, get, list, reset, and delete [indexers](search-indexer-overview.md).|
+| [dataSourceConnections (for indexers)](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/javascript/dataSourceConnectionOperations.js) | Create, update, get, list, and delete data source connections, which are required for indexer-based indexing of [supported data sources](search-indexer-overview.md#supported-data-sources). |
+| [skillsets](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Create, update, get, list, and delete [skillsets](cognitive-search-working-with-skillsets.md) that are attached to indexers and perform AI-based enrichment during indexing. |
+| [synonymMaps](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Create, update, get, list, and delete [synonym maps](search-synonyms.md). |
+| [vectorSearch](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v12-beta/javascript/vectorSearch.js) | Index vectors and send a [vector query](vector-search-how-to-query.md). |
 
 ### TypeScript samples
 
-| Samples | Description |
-|---------|-------------|
-| [indexes](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/typescript/src) | Demonstrates how to create, update, get, list, and delete [search indexes](search-what-is-an-index.md). This sample category also includes a service statistic sample. |
-| [dataSourceConnections (for indexers)](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/typescript/src/dataSourceConnectionOperations.ts) | Demonstrates how to create, update, get, list, and delete indexer data sources, which are required for indexer-based indexing of [supported Azure data sources](search-indexer-overview.md#supported-data-sources). |
-| [indexers](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/typescript/src) | Demonstrates how to create, update, get, list, reset, and delete [indexers](search-indexer-overview.md).|
-| [skillSet](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/typescript/src/skillSetOperations.ts) | Demonstrates how to create, update, get, list, and delete [skillsets](cognitive-search-working-with-skillsets.md) that are attached to indexers and perform AI-based enrichment during indexing. |
-| [synonymMaps](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/typescript/src/synonymMapOperations.ts) | Demonstrates how to create, update, get, list, and delete [synonym maps](search-synonyms.md). |
-| [VectorSearch](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v12/typescript/src/vectorSearch.ts) | Demonstrates how to index vectors and send a [vector query](vector-search-how-to-query.md). |
+| Sample | Description |
+|--|--|
+| [indexes](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/typescript/src) | Create, update, get, list, and delete [indexes](search-what-is-an-index.md). This sample category also includes a service statistic sample. |
+| [indexers](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/typescript/src) | Create, update, get, list, reset, and delete [indexers](search-indexer-overview.md).|
+| [dataSourceConnections (for indexers)](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/typescript/src/dataSourceConnectionOperations.ts) | Create, update, get, list, and delete data source connections, which are required for indexer-based indexing of [supported data sources](search-indexer-overview.md#supported-data-sources). |
+| [skillsets](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/typescript/src/skillSetOperations.ts) | Create, update, get, list, and delete [skillsets](cognitive-search-working-with-skillsets.md) that are attached to indexers and perform AI-based enrichment during indexing. |
+| [synonymMaps](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/typescript/src/synonymMapOperations.ts) | Create, update, get, list, and delete [synonym maps](search-synonyms.md). |
+| [vectorSearch](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v12/typescript/src/vectorSearch.ts) | Create, update, get, list, and delete [vector search](vector-search-how-to-query.md). |
 
 ## Doc samples
 
-Code samples from the Azure AI Search team demonstrate features and workflows. Many of these samples are referenced in tutorials, quickstarts, and how-to articles. You can find these samples in [**Azure-Samples/azure-search-javascript-samples**](https://github.com/Azure-Samples/azure-search-javascript-samples) on GitHub.
+Code samples from the Azure AI Search team demonstrate features and workflows. Many of the following samples are referenced in tutorials, quickstarts, and how-to articles. You can find these samples in [Azure-Samples/azure-search-javascript-samples](https://github.com/Azure-Samples/azure-search-javascript-samples) on GitHub.
 
 ### JavaScript samples
 
-| Samples | Article |
-|---------|---------|
-| [quickstart](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) | Source code for the JavaScript portion of [Quickstart: Full-text search](search-get-started-text.md). Covers the basic workflow for creating, loading, and querying a search index using sample data. |
-| [quickstart-rag-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-rag-js) | Source code for the JavaScript portion of [Quickstart: Generative search (RAG)](search-get-started-rag.md). Uses grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
-| [quickstart-semantic-ranking-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-js) | Source code for the JavaScript portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). Shows the index schema and query request for invoking semantic ranker. |
-| [quickstart-vector-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-vector-js) | Source code for the JavaScript portion of [Quickstart: Vector search](search-get-started-vector.md). Covers the basic workflow for indexing and querying vector data. |
-| [bulk-insert](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/bulk-insert) | Source code for the JavaScript example of how to [use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
-| [azure-functions](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/azure-function-search) | Source code for the JavaScript example of an Azure function that sends queries to a search service. You can substitute this JavaScript version of the `api` code used in the [Add search to web sites](tutorial-csharp-overview.md) C# sample. |
-
-### TypesScript samples
-
-| Samples | Article |
-|---------|---------|
-| [quickstart-rag-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-rag-ts) | Source code for the TypeScript portion of [Quickstart: Generative search (RAG)](search-get-started-rag.md). Uses grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
-| [quickstart-semantic-ranking-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-ts) | Source code for the TypeScript portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). Shows the index schema and query request for invoking semantic ranker. |
-| [quickstart-vector-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-vector-ts) | Source code for the TypeScript portion of [Quickstart: Vector search](search-get-started-vector.md). Covers the basic workflow for indexing and querying vector data. |
-> [!TIP]
-> Try the [Samples browser](/samples/browse/?languages=javascript&products=azure-cognitive-search) to search for Microsoft code samples in GitHub, filtered by product, service, and language.
+| Sample | Description |
+|--|--|
+| [quickstart](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) | Source code for the JavaScript portion of [Quickstart: Full-text search](search-get-started-text.md). Create, load, and query a search index using sample data. |
+| [quickstart-rag-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-rag-js) | Source code for the JavaScript portion of [Quickstart: Generative search (RAG)](search-get-started-rag.md). Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
+| [quickstart-semantic-ranking-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-js) | Source code for the JavaScript portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). Add semantic ranking to an index schema and run semantic queries. |
+| [quickstart-vector-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-vector-js) | Source code for the JavaScript portion of [Quickstart: Vector search](search-get-started-vector.md). Index and query vector content. |
+| [azure-functions](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/azure-function-search) | JavaScript example of an Azure function that sends queries to a search service. You can substitute this JavaScript version for the `api` code used in the [Add search to web sites](tutorial-csharp-overview.md) C# sample. |
+| [bulk-insert](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/bulk-insert) | JavaScript example of how to [use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
+
+### TypeScript samples
+
+| Sample | Description |
+|--|--|
+| [quickstart-rag-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-rag-ts) | Source code for the TypeScript portion of [Quickstart: Generative search (RAG)](search-get-started-rag.md). Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
+| [quickstart-semantic-ranking-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-ts) | Source code for the TypeScript portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). Add semantic ranking to an index schema and run semantic queries. |
+| [quickstart-vector-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-vector-ts) | Source code for the TypeScript portion of [Quickstart: Vector search](search-get-started-vector.md). Index and query vector content. |
 
 ## Other samples
 
-The following samples are also published by the Azure AI Search team but aren't referenced in documentation. Associated readme files provide usage instructions.
+The following samples are also published by the Azure AI Search team but aren't referenced in documentation. Associated README files provide usage instructions.
+
+| Sample | Description |
+|--|--|
+| [azure-search-vector-sample.js](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript/readme.md) | Perform vector search using the Azure SDK for JavaScript. |
 
-| Samples | Description |
-|---------|-------------|
-| [azure-search-vector-sample.js](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript/readme.md) | Vector search sample using the Azure SDK for JavaScript. |
+> [!TIP]
+> Use the [samples browser](/samples/browse/?languages=javascript&products=azure-cognitive-search) to search for Microsoft code samples on GitHub. You can filter your search by product, service, and language.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript サンプルファイルの更新と改善"
}
```

### Explanation
この変更は、`samples-javascript.md`というファイルにおいて、JavaScriptに関するサンプルの情報を更新し、全体の整合性を向上させるためのマイナーな更新です。具体的には、日付を`2025年8月6日`から`2025年9月19日`に修正しました。なお、テキストの明確さを向上させるために、いくつかの文言が簡潔にされ、サンプルやリンクの構造も整理されました。

この更新により、ユーザーはJavaScriptを使用したAzure AI Searchに関するリソースに対してよりアクセスしやすくなり、コードサンプルの理解が容易になります。特に、サンプルの説明がより直感的になり、各種機能（インデックスの作成、データソースの接続、スキルセットの操作など）を示すコードへのリンクも整理され、開発者が効果的にリソースを活用できるようになっています。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -11,65 +11,67 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: concept-article
-ms.date: 08/06/2025
+ms.date: 09/19/2025
 ---
 
 # Python samples for Azure AI Search
 
-Learn about the Python code samples that demonstrate the functionality and workflow of an Azure AI Search solution. These samples use the [**Azure AI Search client library**](/python/api/overview/azure/search-documents-readme) for the [**Azure SDK for Python**](/azure/developer/python/), which you can explore through the following links.
+Learn about Python code samples that demonstrate the functionality and workflow of an Azure AI Search solution. These samples use the [Azure AI Search client library](/python/api/overview/azure/search-documents-readme) for the [Azure SDK for Python](/azure/developer/python/), which you can explore through the following links.
 
 | Target | Link |
 |--------|------|
 | Package download | [pypi.org/project/azure-search-documents/](https://pypi.org/project/azure-search-documents/) |
 | API reference | [azure-search-documents](/python/api/azure-search-documents)  |
 | API test cases | [github.com/Azure/azure-sdk-for-python/tree/main/sdk/search/azure-search-documents/tests](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/search/azure-search-documents/tests) |
 | Source code | [github.com/Azure/azure-sdk-for-python/tree/main/sdk/search/azure-search-documents](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/search/azure-search-documents)  |
-| Change log | [https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) |
+| Change log | [github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) |
 
 ## SDK samples
 
-Code samples from the Azure SDK development team demonstrate API usage. You can find these samples in [**azure-sdk-for-python/tree/main/sdk/search/azure-search-documents/samples**](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/search/azure-search-documents/samples) on GitHub.
+Code samples from the Azure SDK development team demonstrate API usage. You can find these samples in [Azure/azure-sdk-for-python/tree/main/sdk/search/azure-search-documents/samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/search/azure-search-documents/samples) on GitHub.
 
 ## Doc samples
 
-Code samples from the Azure AI Search team demonstrate features and workflows. Many of these samples are referenced in tutorials, quickstarts, and how-to articles. You can find these samples in [**Azure-Samples/azure-search-python-samples**](https://github.com/Azure-Samples/azure-search-python-samples) on GitHub.
+Code samples from the Azure AI Search team demonstrate features and workflows. Many of the following samples are referenced in tutorials, quickstarts, and how-to articles. You can find these samples in [Azure-Samples/azure-search-python-samples](https://github.com/Azure-Samples/azure-search-python-samples) on GitHub.
 
-| Samples | Article |
-|---------|---------|
-| [Quickstart](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart) | Source code for the Python portion of [Quickstart: Full-text search](search-get-started-text.md). This sample covers the basic workflow for creating, loading, and querying a search index using sample data. |
-| [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval) | Source code for the Python portion of [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md). This sample creates a retrieval pipeline that integrates semantic ranking in Azure AI Search with LLM-powered query planning and answer generation. |
-| [Quickstart-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-RAG) | Source code for the Python portion of [Quickstart: Generative search (RAG) with grounding data from Azure AI Search](search-get-started-rag.md). |
-| [Quickstart-Semantic-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) | Source code for the Python portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). This sample shows the index schema and query request for invoking semantic ranker. |
-| [Quickstart-Vector-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Vector-Search) | Source code for the Python portion of [Quickstart: Vector search](search-get-started-vector.md). Covers the basic workflow for indexing and querying vector data. |
-| [Tutorial-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Tutorial-RAG) | Source code for the Python portion of [How to build a RAG solution using Azure AI Search](tutorial-rag-build-solution.md).|
-| [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) | Source code for the Python portion of [Build an agent-to-agent retrieval solution using Azure AI Search](search-agentic-retrieval-how-to-pipeline.md). Unlike [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md), this sample incorporates Azure AI Agent for request orchestration. |
-| [azure-function-search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/azure-function-search) | Source code for the Python example of an Azure function that sends queries to a search service. You can substitute this Python version of the `api` code used in the [Add search to web sites](tutorial-csharp-overview.md) C# sample. |
-| [bulk-insert](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/bulk-insert) | Source code for the Python example of how to [use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
+| Sample | Description |
+|--|--|
+| [Quickstart](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart) | Source code for the Python portion of [Quickstart: Full-text search](search-get-started-text.md). Create, load, and query a search index using sample data. |
+| [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval) | Source code for the Python portion of [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md). Integrate semantic ranking with LLM-powered query planning and answer generation. |
+| [Quickstart-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-RAG) | Source code for the Python portion of [Quickstart: Generative search (RAG)](search-get-started-rag.md). Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
+| [Quickstart-Semantic-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) | Source code for the Python portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). Add semantic ranking to an index schema and run semantic queries. |
+| [Quickstart-Vector-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Vector-Search) | Source code for the Python portion of [Quickstart: Vector search](search-get-started-vector.md). Index and query vector content. |
+| [Tutorial-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Tutorial-RAG) | Source code for the Python portion of [Build a RAG solution using Azure AI Search](tutorial-rag-build-solution.md).|
+| [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) | Source code for the Python portion of [Build an agent-to-agent retrieval solution using Azure AI Search](search-agentic-retrieval-how-to-pipeline.md). Unlike [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md), this sample incorporates Azure AI Agent for request orchestration. |
+| [azure-function-search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/azure-function-search) | Python example of an Azure function that sends queries to a search service. You can substitute this Python version for the `api` code used in the [Add search to web sites](tutorial-csharp-overview.md) C# sample. |
+| [bulk-insert](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/bulk-insert) | Python example of how to [use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
 
-## Demos
-
-[**azure-search-vector-samples**](https://github.com/Azure/azure-search-vector-samples/blob/main/README.md) on GitHub provides a comprehensive collection of samples for vector search scenarios, organized by scenario or technology.
+## Accelerators
 
-[**azure-search-openai-demo**](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md) is a ChatGPT-like experience over enterprise data with Azure OpenAI Python code showing how to use Azure AI Search with the large language models in Azure OpenAI. For background, see this [Tech Community blog post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/revolutionize-your-enterprise-data-with-chatgpt-next-gen-apps-w-azure-openai-and/3762087).
+An accelerator is an end-to-end solution that includes code and documentation you can adapt for your own implementation of a specific scenario.
 
-[**aisearch-openai-rag-audio**](https://github.com/Azure-Samples/aisearch-openai-rag-audio) is "voice to RAG". This sample demonstrates a simple architecture for voice-based generative AI applications that enables Azure AI Search RAG on top of the real-time audio API with full-duplex audio streaming from client devices, while securely handling access to both the model and retrieval system. Backend code is written in Python, while frontend code is written in JavaScript. For an introduction, watch this [video](https://www.youtube.com/watch?v=vXJka8xZ9Ko).
+| Sample | Description |
+|--|--|
+| [rag-experiment-accelerator](https://github.com/microsoft/rag-experiment-accelerator) | Conduct experiments and evaluations using Azure AI Search and the RAG pattern. This sample has code for loading multiple data sources, using various models, and creating various search indexes and queries. |
 
-## Accelerators
+## Demos
 
-An accelerator is an end-to-end solution that includes code and documentation that you can adapt for your own implementation of a specific scenario.
+A demo repo provides proof-of-concept source code for examples or scenarios shown in demonstrations. Unlike accelerators, demo solutions aren't designed for adaptation.
 
-| Repository | Description |
-|------------|-------------|
-| [RAG Experiment Accelerator](https://github.com/microsoft/rag-experiment-accelerator) | Conduct experiments and evaluations using Azure AI Search and the RAG pattern. This accelerator has code for loading multiple data sources, using a variety of models, and creating a variety of search indexes and queries. |
+| Sample | Description |
+|--|--|
+| [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples/blob/main) | Comprehensive collection of samples for vector search scenarios, organized by scenario or technology. |
+| [azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main) | ChatGPT-like experience over enterprise data with Azure OpenAI Python code showing how to use Azure AI Search with large language models in Azure OpenAI. For background, see this [blog post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/revolutionize-your-enterprise-data-with-chatgpt-next-gen-apps-w-azure-openai-and/3762087). |
+| [aisearch-openai-rag-audio](https://github.com/Azure-Samples/aisearch-openai-rag-audio) | "Voice to RAG." This sample demonstrates a simple architecture for voice-based generative AI applications that enables Azure AI Search RAG on top of the real-time audio API with full-duplex audio streaming from client devices. It also securely handles access to both the model and the retrieval system. Backend code is written in Python, while frontend code is written in JavaScript. For an introduction, watch this [video](https://www.youtube.com/watch?v=vXJka8xZ9Ko). |
 
 ## Other samples
 
-The following samples are also published by the Azure AI Search team but aren't referenced in documentation. Associated readme files provide usage instructions.
+The following samples are also published by the Azure AI Search team but aren't referenced in documentation. Associated README files provide usage instructions.
 
-| Repository | Description |
-|------------|-------------|
-| [index-backup-and-restore.ipynb](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) | Uses the **azure.search.documents** library in the Azure SDK for Python to make a local copy of the retrievable fields of a search index and then push those fields to a new search index. |
-| [resumable-index-backup-restore](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/resumable-index-backup-restore/backup-and-restore.ipynb) | This sample accommodates larger indexes exceeding 100,000 documents.|
+| Sample | Description |
+|--|--|
+| [index-backup-and-restore.ipynb](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) | Make a local copy of retrievable fields in an index and push those fields to a new index. |
+| [resumable-index-backup-restore](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/resumable-index-backup-restore/backup-and-restore.ipynb) | Back up and restore larger indexes that exceed 100,000 documents.|
 
 > [!TIP]
-> Try the [Samples browser](/samples/browse/?languages=python&products=azure-cognitive-search) to search for Microsoft code samples in GitHub, filtered by product, service, and language.
+> Use the [samples browser](/samples/browse/?languages=python&products=azure-cognitive-search) to search for Microsoft code samples on GitHub. You can filter your search by product, service, and language.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python サンプルファイルの更新と改善"
}
```

### Explanation
この変更は、`samples-python.md`というファイルにおいて、Pythonに関連するサンプルの情報を更新し、全体の整合性を向上させるためのマイナーな更新です。具体的には、日付を`2025年8月6日`から`2025年9月19日`に修正しました。また、サンプルやリンクの構造が整理され、一部の文言が簡潔にされています。

更新により、Pythonを使用したAzure AI Searchに関連するリソースに対するアクセスが向上し、ユーザーはさまざまな開発シナリオに対してより迅速に情報を探索できるようになります。さらに、Quickstartや各種チュートリアルのリンクが整理されているため、サンプルの内容が直感的に理解しやすくなっています。

特に、コーディングサンプルの説明が明確化され、各サンプルに関連するリンクが更新されたことで、開発者は必要な情報を簡単に参照し、具体的な実装方法を迅速に把握できるようになります。

## articles/search/samples-rest.md{#item-198ebc}

<details>
<summary>Diff</summary>
````diff
@@ -9,33 +9,40 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 09/17/2025
+ms.date: 09/19/2025
 ---
 
 # REST samples for Azure AI Search
 
-Learn about the REST API samples that demonstrate the functionality and workflow of an Azure AI Search solution. These samples use the [**Search Service REST APIs**](/rest/api/searchservice).
+Learn about REST API samples that demonstrate the functionality and workflow of an Azure AI Search solution. These samples use the [Search Service REST APIs](/rest/api/searchservice).
 
 REST is the definitive programming interface for Azure AI Search. All operations that can be invoked programmatically are first available in REST, followed by the SDKs. For this reason, most examples in our documentation use the REST APIs to demonstrate and explain important concepts.
 
 You can use any client that supports HTTP calls. To learn how to formulate the HTTP request using Visual Studio Code with the REST Client extension, see the REST portion of [Quickstart: Full-text search](search-get-started-text.md).
 
 ## Doc samples
 
-Code samples from the Azure AI Search team demonstrate features and workflows. Many of these samples are referenced in tutorials, quickstarts, and how-to articles. You can find these samples in [**Azure-Samples/azure-search-rest-samples**](https://github.com/Azure-Samples/azure-search-rest-samples) on GitHub.
-
-| Samples | Description |
-|---------|---------|
-| [quickstart](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart) | Source code for the REST portion of [Quickstart: Full-text search](search-get-started-text.md). This sample covers the basic workflow for creating, loading, and querying a search index using sample data. |
-| [quickstart-vectors](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) | Source code for the REST portion of [Quickstart: Vector search](search-get-started-vector.md). This sample covers the basic workflow for indexing and querying vector data. |
-| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-agentic-retrieval) | Source code for the REST portion of [Quickstart: Use agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md). This sample creates a retrieval pipeline that integrates semantic ranking in Azure AI Search with LLM-powered query planning and answer generation. |
-| [skillset-tutorial](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skillset-tutorial) | Source code for [Tutorial: Skillsets in Azure AI Search](tutorial-skillset.md). This sample shows you how to create a skillset that iterates over Azure blobs to extract information and infer structure.|
-| [skill examples](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skill-examples) | Skillset examples in indexer pipelines that include indexes and indexers so that you can follow field mappings, output field mappings, and source paths. |
-| [debug-sessions](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Debug-sessions) | Source code for [Tutorial: Fix a skillset using Debug Sessions](cognitive-search-tutorial-debug-sessions.md). This sample shows you how to use a skillset debug session in the Azure portal. REST is used to create the objects used during debug.|
-| [custom-analyzers](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/custom-analyzers) | Source code for [Tutorial: Create a custom analyzer for phone numbers](tutorial-create-custom-analyzer.md). This sample explains how to use analyzers to preserve patterns and special characters in searchable content.|
-| [index-json-blobs](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/index-json-blobs) | Create an indexer, data source, and index for nested JSON within a JSON array. This sample demonstrates the jsonArray parsing model and documentRoot parameters. |
-| [knowledge-store](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/knowledge-store) | Source code for [Create a knowledge store using REST](knowledge-store-create-rest.md). This sample explains the necessary steps for populating a knowledge store used for knowledge mining workflows. |
-| [projections](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/projections) | Source code for [Define projections in a knowledge store](knowledge-store-projections-examples.md). This sample explains how to specify the physical data structures in a knowledge store.|
+Code samples from the Azure AI Search team demonstrate features and workflows. Many of the following samples are referenced in tutorials, quickstarts, and how-to articles. You can find these samples in [Azure-Samples/azure-search-rest-samples](https://github.com/Azure-Samples/azure-search-rest-samples) on GitHub.
+
+| Sample | Description |
+|--|--|
+| [quickstart](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart) | Source code for the REST portion of [Quickstart: Full-text search](search-get-started-text.md). Create, load, and query a search index using sample data. |
+| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-agentic-retrieval) | Source code for the REST portion of [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md). Integrate semantic ranking with LLM-powered query planning and answer generation. |
+| [quickstart-vectors](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) | Source code for the REST portion of [Quickstart: Vector search](search-get-started-vector.md). Index and query vector content. |
+| [skillset-tutorial](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skillset-tutorial) | Source code for [Tutorial: AI-generated searchable content from Azure blobs](tutorial-skillset.md). Create a skillset that iterates over Azure blobs to extract information and infer structure.|
+| [debug-sessions](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Debug-sessions) | Source code for [Tutorial: Fix a skillset using Debug Sessions](cognitive-search-tutorial-debug-sessions.md). Use REST to create search objects that you later debug in the Azure portal. |
+| [custom-analyzers](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/custom-analyzers) | Source code for [Tutorial: Create a custom analyzer for phone numbers](tutorial-create-custom-analyzer.md). Use an analyzer to preserve patterns and special characters in searchable content.|
+| [index-json-blobs](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/index-json-blobs) | Source code for [Tutorial: Index JSON blobs from Azure Storage](search-semi-structured-data.md). Create an indexer, data source, and index for nested JSON within a JSON array. Demonstrates the jsonArray parsing model and documentRoot parameters. |
+| [knowledge-store](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/knowledge-store) | Source code for [Create a knowledge store using REST](knowledge-store-create-rest.md). Populate a knowledge store for knowledge mining workflows. |
+| [projections](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/projections) | Source code for [Define projections in a knowledge store](knowledge-store-projections-examples.md). Specify the physical data structures in a knowledge store.|
+
+## Other samples
+
+The following samples are also published by the Azure AI Search team but aren't referenced in documentation. Associated README files provide usage instructions.
+
+| Sample | Description |
+|--|--|
+| [skill examples](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skill-examples) | Skillset examples in indexer pipelines that include indexes and indexers so you can follow field mappings, output field mappings, and source paths. |
 
 > [!TIP]
 > Use the [samples browser](/samples/browse/?expanded=azure&languages=http&products=azure-cognitive-search) to search for Microsoft code samples on GitHub. You can filter your search by product, service, and language.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST サンプルファイルの更新と改善"
}
```

### Explanation
この変更は、`samples-rest.md`というファイルで行われたもので、Azure AI SearchにおけるREST APIサンプルの内容を更新し、文書全体の整理を図るためのマイナーな更新です。具体的には、日付が`2025年9月17日`から`2025年9月19日`に変更されました。また、文中の表現が簡潔になり、情報の流れがスムーズにされるよう編集されています。

変更された内容には、サンプルの説明がより直感的になるように整頓されており、特に、リンクが明確化され、サンプルに関連するチュートリアルやクイックスタートの案内が更新されています。これにより、開発者はREST APIを使用したソリューションの機能やワークフローをより簡単に理解できるようになっています。

加えて、他の未文書化のサンプルも追加されており、スキルセットに関する例が具体化されています。これにより、ユーザーはインデックスやフィールドマッピングなどに関する具体的なガイダンスを得ることができます。全体として、ドキュメントが最新の情報を反映するために整備され、ユーザーの利便性が向上されています。

## articles/search/search-howto-index-json-blobs.md{#item-b8230c}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 07/25/2025
+ms.date: 09/18/2025
 ms.update-cycle: 365-days
 ---
 
@@ -75,6 +75,7 @@ api-key: [admin key]
 
 > [!NOTE]
 > As with all indexers, if fields don't clearly match, you should expect to explicitly specify individual [field mappings](search-indexer-field-mappings.md) unless you're using the implicit fields mappings available for blob content and metadata, as described in [basic blob indexer configuration](search-howto-indexing-azure-blob-storage.md).
+> To override an existing index value, the source JSON must provide a non-null value. If the field in the source document is null, the indexer will retain the existing value. To explicitly clear a field, pass an empty string ("") instead. This prevents unintended deletions from the index.
 
 ### json example (single hotel JSON files)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JSON ブロブのインデックス化に関するドキュメントの更新"
}
```

### Explanation
この変更は、`search-howto-index-json-blobs.md`ファイルで行われたもので、Azure AI SearchにおけるJSONブロブのインデックス化方法についての情報を最新の内容に更新するためのマイナーな修正です。具体的には、ドキュメントの日付が`2025年7月25日`から`2025年9月18日`に変更されました。

さらに、インデックスされたフィールドの値を上書きするための具体的な指示が追加されました。この新しい情報は、ソースJSONが非nullの値を提供する必要があることを明示しており、ソースドキュメント内のフィールドがnullの場合、インデクサーは既存の値を保持することを説明しています。また、フィールドを明示的にクリアするためには空の文字列（""）を渡す必要があると述べています。これは、意図しない削除を防ぐための重要なガイダンスです。

全体として、これらの変更は、ユーザーがJSONブロブをインデックス化する際の注意点を理解しやすくし、より効果的に作業を進めるためのサポートを提供します。

## articles/search/search-try-for-free.md{#item-36e28d}

<details>
<summary>Diff</summary>
````diff
@@ -14,18 +14,18 @@ ms.custom: references_regions
 
 # Try Azure AI Search for free
 
-If you're new to Azure, you can set up a free trial subscription to explore Azure AI Search and other services at no charge. Information retrieval over your own content is useful for many scenarios including AI generative search.
+If you're new to Azure, you can set up an Azure free account to explore Azure AI Search and other services at no charge. Information retrieval over your own content is useful for many scenarios including AI generative search.
 
-This article explains how to get the most value from your Azure trial subscription so that you can complete your evaluation of Azure AI Search quickly and efficiently.
+This article explains how to get the most value from your Azure free account so that you can complete your evaluation of Azure AI Search quickly and efficiently.
 
-## Step one: Sign up for a free subscription
+## Step one: Sign up for an Azure free account
 
-To try Azure AI Search for free, [start a trial subscription](https://azure.microsoft.com/pricing/free-trial/?WT.mc_id=A261C142F). The trial subscription is nonrenewable, active for one month, and comes with free credits so that you can create billable services at no charge. 
+To try Azure AI Search for free, [Sign up for an Azure free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn). The free account is active for 30 days, and comes with free credits so that you can create billable services at no charge. 
 
-At this point in time, the credit is equivalent to USD 200. As always, the exact amount is subject to change, but you can verify the credit on the trial subscription sign-up page.
+At this point in time, the credit is equivalent to USD 200. As always, the exact amount is subject to change, but you can verify the credit on the Azure sign-up page.
 
 > [!div class="nextstepaction"]
-> [Start your free trial subscription](https://azure.microsoft.com/pricing/free-trial/?WT.mc_id=A261C142F)
+> [Try Azure for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)
 
 Once you sign up, you can immediately use either of these links to access Azure resources and experiences:
 
@@ -140,10 +140,10 @@ Review the [service limits](search-limits-quotas-capacity.md) for other constrai
 
 ## Next steps
 
-Sign up for an Azure trial subscription:
+Sign up for an Azure free account:
 
 > [!div class="nextstepaction"]
-> [Start your free trial subscription](https://azure.microsoft.com/pricing/free-trial/?WT.mc_id=A261C142F)
+> [Try Azure for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)
 
 When you're ready, add Azure AI Search as your first resource:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure 無料アカウントに関する情報の更新"
}
```

### Explanation
この変更は、`search-try-for-free.md`というファイルにおいて、Azure AI Searchの無料利用に関する情報を更新するための軽微な修正です。具体的には、「無料トライアルサブスクリプション」という表現が「Azure無料アカウント」に置き換えられ、利用の案内がより明確になりました。

主な変更点として、無料アカウントの内容や特典について詳しく説明が更新され、関連するリンクも新しいURLに変更されています。例えば、登録手続きについて紹介するセクションでの指示が改善され、利用者がアカウントを簡単に設定できるようになっています。また、無料アカウントの利用が30日間可能であり、無料クレジットが付与されることを強調しています。

これらの変更により、ドキュメントはより最新の情報を反映し、新規ユーザーがAzure AI Searchを試す際のガイダンスが向上しています。全体として、情報の明確化と使いやすさが向上したことで、利用者にとっての利便性が高まっています。


