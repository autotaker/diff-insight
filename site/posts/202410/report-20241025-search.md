---
date: '2024-10-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f8a58ce...MicrosoftDocs:edd8070
summary: この差分のハイライトは、Azure Searchに関連するドキュメントへの軽微な更新を示しています。主な変更点は、タイトルの変更やコードサンプルの明確化、地域サポートやSKUティアの情報更新です。新機能として、テーブルに新しい列が追加されるなどの改善が見られますが、大きな機能の追加や削除はありません。また、特に破壊的な変更もなく、文書の表現をわかりやすくするためのリネームや再編成が行われています。これらの更新は、開発者がAzure
  Searchプラットフォームを利用する際の文書サポートを改善し、より効率的な開発環境を整えることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f8a58ce...MicrosoftDocs:edd8070){target="_blank"}

# ハイライト

この差分のハイライトは、Azure Searchに関連する複数のドキュメントにおける軽微な更新です。主にタイトルの変更、コードサンプルや説明の明確化、地域サポートやSKUティアの情報更新が行われています。新機能として、テーブルに新しい列が追加されるなどの改善が見られますが、大きな機能追加や削除はありません。

## 新機能
- SKUティアと地域サポートについて、より詳細な情報を提供するための新しい列の追加。
- ベクトル検索インデックス作成ガイドにおけるプロファイル名とアルゴリズム名の正確化。

## 破壊的変更
- 特になし。

## その他の更新
- ドキュメントの表現をわかりやすくするためのリネームと説明の改善。
- TOCファイルにおけるリンク名の一貫性の向上。

# インサイト

この差分による更新は、Azure Searchプラットフォームを利用する開発者が、より効率的に開発を行うための文書サポートを改善することを目的としています。以下では、主な変更点とその意義について詳しく説明します。

まず、`.NET SDK`に関する記事では、Azure.Search.Documentsライブラリを使用する場合の基本的なセットアップや操作がより明確に記載されるようになりました。特に、エラーハンドリングや非同期メソッドに関するアドバイスが強化され、開発者が直面する可能性のある問題の予防策を提供しています。この記事の更新により、利用者はSDKの恩恵をさらに享受しやすくなったと言えるでしょう。

次に、`CSVブロブのインデックス作成`に関する記事では、内容の明確化とタイトル変更が行われました。これにより、特に区切りテキスト解析について強調され、対象技術の理解を深めるための手掛かりが提供されています。また、`地域サポート`関連ドキュメントの更新は、地域別の容量制約などがより鮮明に表示され、リソース配置や制約の理解がしやすくなっています。

`SKUティア`に関する更新では、特定地域で利用できないSKUの情報が整理され、新たな推奨代替が提案されることで、より効率的なサービス利用を支援しています。全体として、これらの更新により、開発者がAzure Searchのサービスを選択し利用する際の判断材料が強化されています。

最後に、TOCのリンク名の修正やベクトル検索ガイドの修正からは、文書の整合性と精度を保つための努力が見て取れます。これにより、利用者は必要な情報に迅速にアクセスしやすくなり、全体的なユーザーエクスペリエンスの向上に寄与しています。

これらの変更は、Azure Searchを活用するエコシステム全体の品質向上につながり、開発コミュニティの成長をサポートしています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-how-to-dotnet-sdk.md](#item-5333eb) | minor update | 検索方法に関する .NET SDK 記事の更新 | renamed | 46 | 46 | 92 | 
| [search-how-to-index-csv-blobs.md](#item-2c3f3e) | minor update | CSVブロブのインデックス作成に関する記事の更新 | renamed | 11 | 12 | 23 | 
| [search-region-support.md](#item-25b0f1) | minor update | 地域サポートに関するドキュメントの更新 | modified | 63 | 74 | 137 | 
| [search-sku-tier.md](#item-7686b8) | minor update | SKUティアに関するドキュメントの更新 | modified | 8 | 12 | 20 | 
| [toc.yml](#item-c4768f) | minor update | TOCファイルの修正 | modified | 2 | 2 | 4 | 
| [vector-search-how-to-create-index.md](#item-97c769) | minor update | ベクトル検索インデックス作成ガイドの修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/search-how-to-dotnet-sdk.md{#item-5333eb}

<details>
<summary>Diff</summary>
````diff
@@ -9,14 +9,14 @@ ms.author: heidist
 ms.devlang: csharp
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 10/18/2023
+ms.date: 10/23/2024
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
   - ignite-2023
 ---
 
-# How to use Azure.Search.Documents in a C# .NET Application
+# How to use Azure.Search.Documents in a .NET application
 
 This article explains how to create and manage search objects using C# and the [**Azure.Search.Documents**](/dotnet/api/overview/azure/search) (version 11) client library in the Azure SDK for .NET.
 
@@ -31,7 +31,7 @@ As with previous versions, you can use this library to:
 + Execute queries, all without having to deal with the details of HTTP and JSON
 + Invoke and manage AI enrichment (skillsets) and outputs
 
-The library is distributed as a single [Azure.Search.Documents NuGet package](https://www.nuget.org/packages/Azure.Search.Documents/), which includes all APIs used for programmatic access to a search service.
+The library is distributed as a single [NuGet package](https://www.nuget.org/packages/Azure.Search.Documents/) that includes all APIs used for programmatic access to a search service.
 
 The client library defines classes like `SearchIndex`, `SearchField`, and `SearchDocument`, as well as operations like `SearchIndexClient.CreateIndex` and `SearchClient.Search` on the `SearchIndexClient` and `SearchClient` classes. These classes are organized into the following namespaces:
 
@@ -40,31 +40,31 @@ The client library defines classes like `SearchIndex`, `SearchField`, and `Searc
 + [`Azure.Search.Documents.Indexes.Models`](/dotnet/api/azure.search.documents.indexes.models)
 + [`Azure.Search.Documents.Models`](/dotnet/api/azure.search.documents.models)
 
-Azure.Search.Documents (version 11) targets the [2020-06-30 search service specification](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/search/data-plane/Azure.Search/stable/2020-06-30). 
+Version 11 targets the [2020-06-30 search service specification](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/search/data-plane/Azure.Search/stable/2020-06-30). 
 
 The client library doesn't provide [service management operations](/rest/api/searchmanagement/), such as creating and scaling search services and managing API keys. If you need to manage your search resources from a .NET application, use the [Microsoft.Azure.Management.Search](/dotnet/api/microsoft.azure.management.search) library in the Azure SDK for .NET.
 
 ## Upgrade to v11
 
-If you have been using the previous version of the .NET SDK and you'd like to upgrade to the current generally available version, see [Upgrade to Azure AI Search .NET SDK version 11](search-dotnet-sdk-migration-version-11.md).
+If you've been using the previous version of the .NET SDK and you'd like to upgrade to the current generally available version, see [Upgrade to Azure AI Search .NET SDK version 11](search-dotnet-sdk-migration-version-11.md).
 
 ## SDK requirements
 
 + Visual Studio 2019 or later.
 
-+ Your own Azure AI Search service. In order to use the SDK, you'll need the name of your service and one or more API keys. [Create a service in the portal](search-create-service-portal.md) if you don't have one.
++ Your own Azure AI Search service. In order to use the SDK, you need the name of your service and one or more API keys. [Create a service in the portal](search-create-service-portal.md) if you don't have one.
 
-+ Download the [Azure.Search.Documents package](https://www.nuget.org/packages/Azure.Search.Documents) using **Tools** > **NuGet Package Manager** > **Manage NuGet Packages for Solution** in Visual Studio. Search for the package name `Azure.Search.Documents`.
++ Download the [NuGet package](https://www.nuget.org/packages/Azure.Search.Documents) using **Tools** > **NuGet Package Manager** > **Manage NuGet Packages for Solution** in Visual Studio. Search for the package name `Azure.Search.Documents`.
 
-Azure SDK for .NET conforms to [.NET Standard 2.0](/dotnet/standard/net-standard#net-implementation-support). 
+The Azure SDK for .NET conforms to [.NET Standard 2.0](/dotnet/standard/net-standard#net-implementation-support). 
 
 ## Example application
 
-This article "teaches by example", relying on the [DotNetHowTo](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowTo) code example on GitHub to illustrate fundamental concepts in Azure AI Search - specifically, how to create, load, and query a search index.
+This article *teaches by example*, relying on the [DotNetHowTo](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowTo) code example on GitHub to illustrate fundamental concepts in Azure AI Search, and how to create, load, and query a search index.
 
-For the rest of this article, assume a new index named "hotels", populated with a few documents, with several queries that match on results.
+For the rest of this article, assume a new index named *hotels*, populated with a few documents, with several queries that match on results.
 
-Below is the main program, showing the overall flow:
+The following example shows the main program, with the overall flow:
 
 ```csharp
 // This sample shows how to delete, create, upload documents and query an index
@@ -106,41 +106,41 @@ Next is a partial screenshot of the output, assuming you run this application wi
 
 The client library uses three client types for various operations: [`SearchIndexClient`](/dotnet/api/azure.search.documents.indexes.searchindexclient) to create, update, or delete indexes, [`SearchClient`](/dotnet/api/azure.search.documents.searchclient) to load or query an index, and [`SearchIndexerClient`](/dotnet/api/azure.search.documents.indexes.searchindexerclient) to work with indexers and skillsets. This article focuses on the first two. 
 
-At a minimum, all of the clients require the service name or endpoint, and an API key. It's common to provide this information in a configuration file, similar to what you find in the `appsettings.json` file of the [DotNetHowTo sample application](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowTo). To read from the configuration file, add `using Microsoft.Extensions.Configuration;` to your program.
+At a minimum, all of the clients require the service name or endpoint, and an API key. It's common to provide this information in a configuration file, similar to what you find in the *appsettings.json* file of the [DotNetHowTo sample application](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowTo). To read from the configuration file, add `using Microsoft.Extensions.Configuration;` to your program.
 
 The following statement creates the index client used to create, update, or delete indexes. It takes a service endpoint and admin API key.
 
 ```csharp
 private static SearchIndexClient CreateSearchIndexClient(IConfigurationRoot configuration)
 {
-    string searchServiceEndPoint = configuration["SearchServiceEndPoint"];
-    string adminApiKey = configuration["SearchServiceAdminApiKey"];
+    string searchServiceEndPoint = configuration["YourSearchServiceEndPoint"];
+    string adminApiKey = configuration["YourSearchServiceAdminApiKey"];
 
     SearchIndexClient indexClient = new SearchIndexClient(new Uri(searchServiceEndPoint), new AzureKeyCredential(adminApiKey));
     return indexClient;
 }
 ```
 
-The next statement creates the search client used to load documents or run queries. `SearchClient` requires an index. You'll need an admin API key to load documents, but you can use a query API key to run queries. 
+The next statement creates the search client used to load documents or run queries. `SearchClient` requires an index. You need an admin API key to load documents, but you can use a query API key to run queries. 
 
 ```csharp
 string indexName = configuration["SearchIndexName"];
 
 private static SearchClient CreateSearchClientForQueries(string indexName, IConfigurationRoot configuration)
 {
-    string searchServiceEndPoint = configuration["SearchServiceEndPoint"];
-    string queryApiKey = configuration["SearchServiceQueryApiKey"];
+    string searchServiceEndPoint = configuration["YourSearchServiceEndPoint"];
+    string queryApiKey = configuration["YourSearchServiceQueryApiKey"];
 
     SearchClient searchClient = new SearchClient(new Uri(searchServiceEndPoint), indexName, new AzureKeyCredential(queryApiKey));
     return searchClient;
 }
 ```
 
 > [!NOTE]
-> If you provide an invalid key for the import operation (for example, a query key where an admin key was required), the `SearchClient` will throw a `CloudException` with the error message "Forbidden" the first time you call an operation method on it. If this happens to you, double-check the API key.
+> If you provide an invalid key for the import operation (for example, a query key where an admin key was required), the `SearchClient` throws a `CloudException` with the error message *Forbidden* the first time you call an operation method on it. If this happens to you, double-check the API key.
 >
 
-### Deleting the index
+### Delete the index
 
 In the early stages of development, you might want to include a [`DeleteIndex`](/dotnet/api/azure.search.documents.indexes.searchindexclient.deleteindex) statement to delete a work-in-progress index so that you can recreate it with an updated definition. Sample code for Azure AI Search often includes a deletion step so that you can rerun the sample.
 
@@ -170,14 +170,14 @@ private static void DeleteIndexIfExists(string indexName, SearchIndexClient inde
 ```
 
 > [!NOTE]
-> The example code in this article uses the synchronous methods for simplicity, but you should use the asynchronous methods in your own applications to keep them scalable and responsive. For example, in the method above you could use [`DeleteIndexAsync`](/dotnet/api/azure.search.documents.indexes.searchindexclient.deleteindexasync) instead of [`DeleteIndex`](/dotnet/api/azure.search.documents.indexes.searchindexclient.deleteindex).
+> The example code in this article uses the synchronous methods for simplicity, but you should use the asynchronous methods in your own applications to keep them scalable and responsive. For example, in the previous method, you could use [`DeleteIndexAsync`](/dotnet/api/azure.search.documents.indexes.searchindexclient.deleteindexasync) instead of [`DeleteIndex`](/dotnet/api/azure.search.documents.indexes.searchindexclient.deleteindex).
 >
 
 ## Create an index
 
 You can use [`SearchIndexClient`](/dotnet/api/azure.search.documents.indexes.searchindexclient) to create an index. 
 
-The method below creates a new [`SearchIndex`](/dotnet/api/azure.search.documents.indexes.models.searchindex) object with a list of [`SearchField`](/dotnet/api/azure.search.documents.indexes.models.searchfield) objects that define the schema of the new index. Each field has a name, data type, and several attributes that define its search behavior. 
+The following method creates a new [`SearchIndex`](/dotnet/api/azure.search.documents.indexes.models.searchindex) object with a list of [`SearchField`](/dotnet/api/azure.search.documents.indexes.models.searchfield) objects that define the schema of the new index. Each field has a name, data type, and several attributes that define its search behavior. 
 
 Fields can be defined from a model class using [`FieldBuilder`](/dotnet/api/azure.search.documents.indexes.fieldbuilder). The `FieldBuilder` class uses reflection to create a list of `SearchField` objects for the index by examining the public properties and attributes of the given `Hotel` model class. We'll take a closer look at the `Hotel` class later on.
 
@@ -193,15 +193,15 @@ private static void CreateIndex(string indexName, SearchIndexClient indexClient)
 }
 ```
 
-Besides fields, you could also add scoring profiles, suggesters, or CORS options to the index (these parameters are omitted from the sample for brevity). You can find more information about the SearchIndex object and its constituent parts in the [`SearchIndex`](/dotnet/api/azure.search.documents.indexes.models.searchindex) properties list, as well as in the [REST API reference](/rest/api/searchservice/).
+Besides fields, you could also add scoring profiles, suggesters, or CORS options to the index (these parameters are omitted from the sample for brevity). You can find more information about the `SearchIndex` object and its constituent parts in the [SearchIndex](/dotnet/api/azure.search.documents.indexes.models.searchindex) properties list, as well as in the [REST API reference](/rest/api/searchservice/).
 
 > [!NOTE]
-> You can always create the list of `Field` objects directly instead of using `FieldBuilder` if needed. For example, you may not want to use a model class or you may need to use an existing model class that you don't want to modify by adding attributes.
+> You can always create the list of `Field` objects directly instead of using `FieldBuilder` if needed. For example, you might not want to use a model class or you might need to use an existing model class that you don't want to modify by adding attributes.
 >
 
 ### Call CreateIndex in Main()
 
-`Main` creates a new "hotels" index by calling the above method:
+`Main` creates a new *hotels* index by calling the preceding method:
 
 ```csharp
 Console.WriteLine("{0}", "Creating index...\n");
@@ -249,11 +249,11 @@ An alternative approach is to add fields to an index directly. The following exa
 
 ### Field definitions
 
-Your data model in .NET and its corresponding index schema should support the search experience you'd like to give to your end user. Each top level object in .NET, such as a search document in a search index, corresponds to a search result you would present in your user interface. For example, in a hotel search application your end users may want to search by hotel name, features of the hotel, or the characteristics of a particular room. 
+Your data model in .NET and its corresponding index schema should support the search experience you'd like to give to your end user. Each top level object in .NET, such as a search document in a search index, corresponds to a search result you would present in your user interface. For example, in a hotel search application, your end users might want to search by hotel name, features of the hotel, or the characteristics of a particular room. 
 
 Within each class, a field is defined with a data type and attributes that determine how it's used. The name of each public property in each class maps to a field with the same name in the index definition. 
 
-Take a look at the following snippet that pulls several field definitions from the Hotel class. Notice that Address and Rooms are C# types with their own class definitions (refer to the sample code if you want to view them). Both are complex types. For more information, see [How to model complex types](search-howto-complex-data-types.md).
+Take a look at the following snippet that pulls several field definitions from the Hotel class. Notice that `Address` and `Rooms` are C# types with their own class definitions (refer to the sample code if you want to view them). Both are complex types. For more information, see [How to model complex types](search-howto-complex-data-types.md).
 
 ```csharp
 public partial class Hotel
@@ -279,21 +279,21 @@ public partial class Hotel
     public Room[] Rooms { get; set; }
 ```
 
-#### Choosing a field class
+#### Choose a field class
 
-When defining fields, you can use the base [`SearchField`](/dotnet/api/azure.search.documents.indexes.models.searchfield) class, or you can use derivative helper models that serve as "templates", with pre-configured properties.
+When defining fields, you can use the base [`SearchField`](/dotnet/api/azure.search.documents.indexes.models.searchfield) class, or you can use derivative helper models that serve as *templates*, with pre-configured properties.
 
 Exactly one field in your index must serve as the document key (`IsKey = true`). It must be a string, and it must uniquely identify each document. It's also required to have `IsHidden = true`, which means it can't be visible in search results.
 
 | Field type | Description and usage |
 |------------|-----------------------|
-| [`SearchField`](/dotnet/api/azure.search.documents.indexes.models.searchfield) | Base class, with most properties set to null, excepting `Name` which is required, and `AnalyzerName` which defaults to standard Lucene. |
+| [`SearchField`](/dotnet/api/azure.search.documents.indexes.models.searchfield) | Base class, with most properties set to null, except `Name` which is required, and `AnalyzerName` which defaults to standard Lucene. |
 | [`SimpleField`](/dotnet/api/azure.search.documents.indexes.models.simplefield) | Helper model. Can be any data type, is always non-searchable (it's ignored for full text search queries), and is retrievable (it's not hidden). Other attributes are off by default, but can be enabled. You might use a `SimpleField` for document IDs or fields used only in filters, facets, or scoring profiles. If so, be sure to apply any attributes that are necessary for the scenario, such as `IsKey = true` for a document ID. For more information, see [SimpleFieldAttribute.cs](https://github.com/Azure/azure-sdk-for-net/blob/master/sdk/search/Azure.Search.Documents/src/Indexes/SimpleFieldAttribute.cs) in source code. |
 | [`SearchableField`](/dotnet/api/azure.search.documents.indexes.models.searchablefield) | Helper model. Must be a string, and is always searchable and retrievable. Other attributes are off by default, but can be enabled. Because this field type is searchable, it supports synonyms and the full complement of analyzer properties. For more information, see the [SearchableFieldAttribute.cs](https://github.com/Azure/azure-sdk-for-net/blob/master/sdk/search/Azure.Search.Documents/src/Indexes/SearchableFieldAttribute.cs) in source code. |
 
-Whether you use the basic `SearchField` API or either one of the helper models, you must explicitly enable filter, facet, and sort attributes. For example, [IsFilterable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfilterable), [IsSortable](/dotnet/api/azure.search.documents.indexes.models.searchfield.issortable), and [IsFacetable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfacetable) must be explicitly attributed, as shown in the sample above.
+Whether you use the basic `SearchField` API or either one of the helper models, you must explicitly enable filter, facet, and sort attributes. For example, [IsFilterable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfilterable), [IsSortable](/dotnet/api/azure.search.documents.indexes.models.searchfield.issortable), and [IsFacetable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfacetable) must be explicitly attributed, as shown in the previous sample.
 
-#### Adding field attributes
+#### Add field attributes
 
 Notice how each field is decorated with attributes such as `IsFilterable`, `IsSortable`, `IsKey`, and `AnalyzerName`. These attributes map directly to the [corresponding field attributes in an Azure AI Search index](/rest/api/searchservice/indexes/create). The `FieldBuilder` class uses these properties to construct field definitions for the index.
 
@@ -308,12 +308,12 @@ Did you happen to notice the `SmokingAllowed` property?
 public bool? SmokingAllowed => (Rooms != null) ? Array.Exists(Rooms, element => element.SmokingAllowed == true) : (bool?)null;
 ```
 
-The `JsonIgnore` attribute on this property tells the `FieldBuilder` to not serialize it to the index as a field.  This is a great way to create client-side calculated properties you can use as helpers in your application.  In this case, the `SmokingAllowed` property reflects whether any `Room` in the `Rooms` collection allows smoking. If all are false, it indicates that the entire hotel doesn't allow smoking.
+The `JsonIgnore` attribute on this property tells the `FieldBuilder` to not serialize it to the index as a field. This is a great way to create client-side calculated properties that you can use as helpers in your application. In this case, the `SmokingAllowed` property reflects whether any `Room` in the `Rooms` collection allows smoking. If all are false, it indicates that the entire hotel doesn't allow smoking.
 
 ## Load an index
 
-The next step in `Main` populates the newly created "hotels" index. This index population is done in the following method:
-(Some code replaced with "..." for illustration purposes. See the full sample solution for the full data population code.)
+The next step in `Main` populates the newly created *hotels* index. This index population is done in the following method:
+(Some code replaced with `...` for illustration purposes. See the full sample solution for the full data population code.)
 
 ```csharp
 private static void UploadDocuments(SearchClient searchClient)
@@ -426,15 +426,15 @@ private static void UploadDocuments(SearchClient searchClient)
     Thread.Sleep(2000);
 ```
 
-This method has four parts. The first creates an array of three `Hotel` objects each with three `Room` objects that will serve as our input data to upload to the index. This data is hard-coded for simplicity. In an actual application, data will likely come from an external data source such as an SQL database.
+This method has four parts. The first creates an array of three `Hotel` objects each with three `Room` objects that serve as our input data to upload to the index. This data is hard-coded for simplicity. In an actual application, data likely comes from an external data source such as a SQL database.
 
 The second part creates an [`IndexDocumentsBatch`](/dotnet/api/azure.search.documents.models.indexdocumentsbatch) containing the documents. You specify the operation you want to apply to the batch at the time you create it, in this case by calling [`IndexDocumentsAction.Upload`](/dotnet/api/azure.search.documents.models.indexdocumentsaction.upload). The batch is then uploaded to the Azure AI Search index by the [`IndexDocuments`](/dotnet/api/azure.search.documents.searchclient.indexdocuments) method.
 
 > [!NOTE]
-> In this example, we are just uploading documents. If you wanted to merge changes into existing documents or delete documents, you could create batches by calling `IndexDocumentsAction.Merge`, `IndexDocumentsAction.MergeOrUpload`, or `IndexDocumentsAction.Delete` instead. You can also mix different operations in a single batch by calling `IndexBatch.New`, which takes a collection of `IndexDocumentsAction` objects, each of which tells Azure AI Search to perform a particular operation on a document. You can create each `IndexDocumentsAction` with its own operation by calling the corresponding method such as `IndexDocumentsAction.Merge`, `IndexAction.Upload`, and so on.
+> In this example, you're just uploading documents. If you wanted to merge changes into existing documents or delete documents, you could create batches by calling `IndexDocumentsAction.Merge`, `IndexDocumentsAction.MergeOrUpload`, or `IndexDocumentsAction.Delete` instead. You can also mix different operations in a single batch by calling `IndexBatch.New`, which takes a collection of `IndexDocumentsAction` objects, each of which tells Azure AI Search to perform a particular operation on a document. You can create each `IndexDocumentsAction` with its own operation by calling the corresponding method such as `IndexDocumentsAction.Merge`, `IndexAction.Upload`, and so on.
 > 
 
-The third part of this method is a catch block that handles an important error case for indexing. If your search service fails to index some of the documents in the batch, a `RequestFailedException` is thrown. An exception can happen if you're indexing documents while your service is under heavy load. **We strongly recommend explicitly handling this case in your code.** You can delay and then retry indexing the documents that failed, or you can log and continue like the sample does, or you can do something else depending on your application's data consistency requirements. An alternative is to use [SearchIndexingBufferedSender](/dotnet/api/azure.search.documents.searchindexingbufferedsender-1) for intelligent batching, automatic flushing, and retries for failed indexing actions. See [this example](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample05_IndexingDocuments.md#searchindexingbufferedsender) for more context.
+The third part of this method is a catch block that handles an important error case for indexing. If your search service fails to index some of the documents in the batch, a `RequestFailedException` is thrown. An exception can happen if you're indexing documents while your service is under heavy load. **We strongly recommend explicitly handling this case in your code.** You can delay and then retry indexing the documents that failed, or you can log and continue like the sample does, or you can do something else depending on your application's data consistency requirements. An alternative is to use [SearchIndexingBufferedSender](/dotnet/api/azure.search.documents.searchindexingbufferedsender-1) for intelligent batching, automatic flushing, and retries for failed indexing actions. For more context, see the [SearchIndexingBufferedSender example](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample05_IndexingDocuments.md#searchindexingbufferedsender).
 
 Finally, the `UploadDocuments` method delays for two seconds. Indexing happens asynchronously in your search service, so the sample application needs to wait a short time to ensure that the documents are available for searching. Delays like this are typically only necessary in demos, tests, and sample applications.
 
@@ -453,13 +453,13 @@ UploadDocuments(searchClient);
 
 ## Run queries
 
-First, set up a `SearchClient` that reads the service endpoint and query API key from **appsettings.json**:
+First, set up a `SearchClient` that reads the service endpoint and query API key from *appsettings.json*:
 
 ```csharp
 private static SearchClient CreateSearchClientForQueries(string indexName, IConfigurationRoot configuration)
 {
-    string searchServiceEndPoint = configuration["SearchServiceEndPoint"];
-    string queryApiKey = configuration["SearchServiceQueryApiKey"];
+    string searchServiceEndPoint = configuration["YourSearchServiceEndPoint"];
+    string queryApiKey = configuration["YourSearchServiceQueryApiKey"];
 
     SearchClient searchClient = new SearchClient(new Uri(searchServiceEndPoint), indexName, new AzureKeyCredential(queryApiKey));
     return searchClient;
@@ -577,15 +577,15 @@ results = searchClient.Search<Hotel>("motel", options);
 WriteDocuments(results);
 ```
 
-In this case, we're searching the entire index for the word "motel" in any searchable field and we only want to retrieve the hotel names, as specified by the `Select` option. Here are the results:
+In this case, we're searching the entire index for the word *motel* in any searchable field and we only want to retrieve the hotel names, as specified by the `Select` option. Here are the results:
 
 ```output
 Name: Secret Point Motel
 
 Name: Twin Dome Motel
 ```
 
-In the second query, use a filter to select rooms with a nightly rate of less than $100. Return only the hotel ID and description in the results:
+In the second query, use a filter to select rooms with a nightly rate of less than *$100*. Return only the hotel ID and description in the results:
 
 ```csharp
 options = new SearchOptions()
@@ -598,7 +598,7 @@ options.Select.Add("Description");
 results = searchClient.Search<Hotel>("*", options);
 ```
 
-The above query uses an OData `$filter` expression, `Rooms/any(r: r/BaseRate lt 100)`, to filter the documents in the index. This uses the [any operator](./search-query-odata-collection-operators.md) to apply the 'BaseRate lt 100' to every item in the Rooms collection. For more information, see [OData filter syntax](./query-odata-filter-orderby-syntax.md).
+This query uses an OData `$filter` expression, `Rooms/any(r: r/BaseRate lt 100)`, to filter the documents in the index. It uses the [any operator](./search-query-odata-collection-operators.md) to apply the 'BaseRate lt 100' to every item in the Rooms collection. For more information, see [OData filter syntax](./query-odata-filter-orderby-syntax.md).
 
 In the third query, find the top two hotels that have been most recently renovated, and show the hotel name and last renovation date. Here's the code: 
 
@@ -617,7 +617,7 @@ results = searchClient.Search<Hotel>("*", options);
 WriteDocuments(results);
 ```
 
-In the last query, find all hotels names that match the word "hotel":
+In the last query, find all hotels names that match the word *hotel*:
 
 ```csharp
 options.Select.Add("HotelId");
@@ -638,11 +638,11 @@ WriteDocuments(results);
 
 This section concludes this introduction to the .NET SDK, but don't stop here. The next section suggests other resources for learning more about programming with Azure AI Search.
 
-## Next steps
+## Related content
 
 + Browse the API reference documentation for [Azure.Search.Documents](/dotnet/api/azure.search.documents) and [REST API](/rest/api/searchservice/)
 
-+ Browse other code samples based on Azure.Search.Documents in [azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples) and [search-getting-started-dotnet](https://github.com/Azure-Samples/search-dotnet-getting-started)
++ Browse other code samples based on Azure.Search.Documents in [azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples) and [search-dotnet-getting-started](https://github.com/Azure-Samples/search-dotnet-getting-started)
 
 + Review [naming conventions](/rest/api/searchservice/Naming-rules) to learn the rules for naming various objects
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索方法に関する .NET SDK 記事の更新"
}
```

### Explanation
この変更は、MicrosoftのAzure Searchに関するドキュメントの一部で、特にC#の.NET SDKを利用した検索操作に関する情報を提供する記事が新版にリネームされ、内容にいくつかの更新が加えられました。新しいバージョンが2024年10月23日に関連する日付として設定されています。

リネームされたファイルは、検索に関する基本的な構造と機能、およびAPIの使用方法を解説しており、特にAzure.Search.Documentsライブラリの利用とそのクライアントクラス（`SearchIndexClient`や`SearchClient`など）に焦点が当てられています。加えて、NuGetパッケージの配布、SDKの要件、およびサンプルプログラムの流れに関するセクションが見直され、言い回しが簡潔に改善されました。

具体的には、以下の点が変更されています：
- 各セクションの表現が直接的かつ簡素なものになり、必要な情報が一層明確になりました。
- コードサンプルや手順において、単語の選び方や構文が整えられ、エラー処理の重要性や、非同期メソッドの使用に関する注意喚起がより周知されるようになっています。
- 説明はよりスムーズになり、読者に対して使いやすく構成された内容を提供しています。

## articles/search/search-how-to-index-csv-blobs.md{#item-2c3f3e}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: Search over CSV blobs
+title: Search over CSV blobs using delimitedText parsing
 titleSuffix: Azure AI Search
-description: Extract CSV blobs from Azure Blob Storage or Azure Files and import as search documents into Azure AI Search using the delimitedText parsing mode.
+description: Extract CSV blobs from Azure Blob Storage or Azure Files, and import as search documents into Azure AI Search using the delimitedText parsing mode.
 
 manager: nitinme
 author: HeidiSteen
@@ -11,12 +11,12 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 01/17/2024
+ms.date: 10/23/2024
 ---
 
 # Index CSV blobs and files using delimitedText parsing mode
 
-**Applies to**: [Blob indexers](search-howto-indexing-azure-blob-storage.md), [File indexers](search-file-storage-integration.md)
+**Applies to**: [Blob storage indexers](search-howto-indexing-azure-blob-storage.md), [Files indexers](search-file-storage-integration.md)
 
 In Azure AI Search, indexers for Azure Blob Storage and Azure Files support a `delimitedText` parsing mode for CSV files that treats each line in the CSV as a separate search document. For example, given the following comma-delimited text, the `delimitedText` parsing mode would result in two documents in the search index: 
 
@@ -26,7 +26,7 @@ id, datePublished, tags
 2, 2016-07-07, "cloud,mobile"
 ```
 
-If a field inside the CSV file contains the delimeter, it should be wrapped in quotes. If the field contains a quote, it must be escaped using double quotes (`""`).
+If a field inside the CSV file contains the delimiter, it should be wrapped in quotes. If the field contains a quote, it must be escaped using double quotes (`""`).
 
 ```text
 id, datePublished, tags
@@ -35,9 +35,9 @@ id, datePublished, tags
 
 Without the `delimitedText` parsing mode, the entire contents of the CSV file would be treated as one search document.
 
-Whenever you're creating multiple search documents from a single blob, be sure to review [Indexing blobs to produce multiple search documents](search-howto-index-one-to-many-blobs.md) to understand how document key assignments work. The blob indexer is capable of finding or generating values that uniquely define each new document. Specifically, it can create a transitory `AzureSearch_DocumentKey` that generated when a blob is parsed into smaller parts, where the value is then used as the search document's key in the index.
+Whenever you create multiple search documents from a single blob, be sure to review [Indexing blobs to produce multiple search documents](search-howto-index-one-to-many-blobs.md) to understand how document key assignments work. The blob indexer is capable of finding or generating values that uniquely define each new document. Specifically, it can create a transitory `AzureSearch_DocumentKey` when a blob is parsed into smaller parts, where the value is then used as the search document's key in the index.
 
-## Setting up CSV indexing
+## Set up CSV indexing
 
 To index CSV blobs, create or update an indexer definition with the `delimitedText` parsing mode on a [Create Indexer](/rest/api/searchservice/indexers/create) request.
 
@@ -51,8 +51,7 @@ Only UTF-8 encoding is supported.
 }
 ```
 
-`firstLineContainsHeaders` indicates that the first (nonblank) line of each blob contains headers.
-If blobs don't contain an initial header line, the headers should be specified in the indexer configuration: 
+`firstLineContainsHeaders` indicates that the first (nonblank) line of each blob contains headers. If blobs don't contain an initial header line, the headers should be specified in the indexer configuration: 
 
 ```http
 "parameters" : { "configuration" : { "parsingMode" : "delimitedText", "delimitedTextHeaders" : "id,datePublished,tags" } } 
@@ -99,7 +98,7 @@ api-key: [admin key]
 }
 ```
 
-## See also
+## Related content
 
-+ [Index data from Blob Storage](search-howto-indexing-azure-blob-storage.md)
-+ [Index data from File Storage](search-file-storage-integration.md)
++ [Index data from Azure Blob Storage](search-howto-indexing-azure-blob-storage.md)
++ [Index data from Azure Files](search-file-storage-integration.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "CSVブロブのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更では、CSVブロブに関するインデックス作成の手法を解説したドキュメントがリネームされ、その内容が若干更新されました。特に、記事のタイトルが「CSVブロブを使用した検索」とから「区切りテキスト解析を使用したCSVブロブの検索」へと変更され、内容もわずかですが明確化されています。

主な変更点は以下の通りです：
- **タイトルと説明の更新**: 記事のタイトルと説明が調整され、'区切りテキスト解析'がより強調されています。
- **日付の更新**: 最後の更新日が2024年10月23日に変更されています。
- **適用対象の明確化**: "Blob indexers" の表現が "Blob storage indexers" に改められ、より具体的に意図が示されています。
- **文体の調整**: 文中の表現が簡潔になるように改善され、特に「いつでも作成」の部分が「作成する際に」と変更されて、より適切な日本語表現になっています。

全体的に、より良い理解を促すための修正が施され、読者にとってのわかりやすさが向上しています。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -35,105 +35,94 @@ You can create an Azure AI Search resource in any of the following Azure public
 
 ### Americas
 
-| Region | AI integration | Semantic ranker | Availability zones |
-|--|--|--|--|
-| Brazil South​​ ​ | ✅ | ✅ | |
-| Canada Central​​ | ✅ | ✅ | ✅ |
-| Canada East​​ ​ |  | ✅ | |
-| East US​ <sup>1</sup>| ✅ | ✅ | ✅ |
-| East US 2 ​ | ✅ | ✅ | ✅ |
-| ​Central US​​ <sup>2</sup> | ✅ | ✅ | ✅ |
-| North Central US​ ​ | ✅ | ✅ | |
-| South Central US​ <sup>1</sup>​ | ✅ | ✅ | ✅ |
-| West US​ ​ | ✅ | ✅ | |
-| West US 2​ ​ | ✅ | ✅ | ✅ |
-| West US 3​ <sup>1</sup>​ | ✅ | ✅ |✅ |
-| West Central US​ ​ | ✅ | ✅ | |
-
-<sup>1</sup> Currently, this region is at full capacity and not accepting new search services. 
-
-<sup>2</sup> This region has capacity, but some tiers are [not available](search-sku-tier.md#region-availability-by-tier). 
+| Region | AI integration | Semantic ranker | Availability zones | Capacity constrained |
+|--|--|--|--|--|
+| Brazil South​​ ​ | ✅ | ✅ | |  |
+| Canada Central​​ | ✅ | ✅ | ✅ |  |
+| Canada East​​ ​ |  | ✅ | |  |
+| East US​ | ✅ | ✅ | ✅ |  |
+| East US 2 ​ | ✅ | ✅ | ✅ | Basic, S1 |
+| ​Central US​​ | ✅ | ✅ | ✅ |  |
+| North Central US​ ​ | ✅ | ✅ | |  | 
+| South Central US​  | ✅ | ✅ | ✅ | All Tiers |
+| West US​ ​ | ✅ | ✅ | |  |
+| West US 2​ ​ | ✅ | ✅ | ✅ | |
+| West US 3​ | ✅ | ✅ |✅ | Basic, S1 |
+| West Central US​ ​ | ✅ | ✅ | | |
 
 ### Europe
 
-| Region | AI integration | Semantic ranker | Availability zones |
-|--|--|--|--|
-| North Europe​​ | ✅ | ✅ | ✅ |
-| West Europe​​ <sup>1, 2</sup>| ✅ | ✅ | ✅ |
-| France Central​​ | ✅ | ✅ | ✅ |
-| Germany West Central​ ​| ✅ |  | ✅ |
-| Italy North​​ |  |  | ✅ |
-| Norway East​​ | ✅ |  | ✅ |
-| Poland Central​​ |  |  |  |
-| Spain Central <sup>2</sup> |  |  | ✅  |
-| Sweden Central​​ | ✅ |  | ✅ |
-| Switzerland North​ | ✅ | ✅ | ✅ |
-| Switzerland West​ | ✅ | ✅ | ✅ |
-| UK South​ | ✅ | ✅ | ✅ |
-| UK West​ ​|  | ✅ | |
-
-<sup>1</sup> Currently, this region is at full capacity and not accepting new search services.
-
-<sup>2</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
+| Region | AI integration | Semantic ranker | Availability zones | Capacity constrained |
+|--|--|--|--|--|
+| North Europe​​ | ✅ | ✅ | ✅ |  |
+| West Europe​​ <sup>1</sup>| ✅ | ✅ | ✅ | All Tiers |
+| France Central​​ | ✅ | ✅ | ✅ | |
+| Germany West Central​ ​| ✅ |  | ✅ | |
+| Italy North​​ |  |  | ✅ | |
+| Norway East​​ | ✅ |  | ✅ |  |
+| Poland Central​​ |  |  |  |  |
+| Spain Central <sup>1</sup> |  |  | ✅  |  |
+| Sweden Central​​ | ✅ |  | ✅ |  |
+| Switzerland North​ | ✅ | ✅ | ✅ |  |
+| Switzerland West​ | ✅ | ✅ | ✅ |  |
+| UK South​ | ✅ | ✅ | ✅ |  |
+| UK West​ ​|  | ✅ | |  |
 
-### Middle East
+<sup>1</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
 
-| Region | AI integration | Semantic ranker | Availability zones |
-|--|--|--|--|
-| Israel Central​ <sup>2</sup> |  |  | ✅  |
-| Qatar Central​ <sup>1, 2</sup> |  |  | ✅ |
-| UAE North​​ | ✅ |  | ✅ |
+### Middle East
 
-<sup>1</sup> Currently, this region is at full capacity and not accepting new search services.
+| Region | AI integration | Semantic ranker | Availability zones | Capacity constrained |
+|--|--|--|--|--|
+| Israel Central​ <sup>1</sup> |  |  | ✅  |  |
+| Qatar Central​ <sup>1</sup> |  |  | ✅ | |
+| UAE North​​ | ✅ |  | ✅ |  |
 
-<sup>2</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
+<sup>1</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
 
 ### Africa
 
-| Region | AI integration | Semantic ranker | Availability zones |
-|--|--|--|--|
-| South Africa North​ | ✅ |  | ✅ |
+| Region | AI integration | Semantic ranker | Availability zones | Capacity constrained |
+|--|--|--|--|--|
+| South Africa North​ | ✅ |  | ✅ |   |
 
 ### Asia Pacific
 
-| Region | AI integration | Semantic ranker | Availability zones |
-|--|--|--|--|
-| Australia East​ ​ | ✅ | ✅ | ✅ |
-| Australia Southeast​​​ |  | ✅ |  |
-| East Asia​ | ✅ | ✅ | ✅ |
-| Southeast Asia​ ​ ​ | ✅ | ✅ | ✅ |
-| Central India <sup>1</sup> | ✅ | ✅ | ✅ |
+| Region | AI integration | Semantic ranker | Availability zones | Capacity constrained |
+|--|--|--|--|--|
+| Australia East​ ​ | ✅ | ✅ | ✅ |   |
+| Australia Southeast​​​ |  | ✅ |  | |
+| East Asia​ | ✅ | ✅ | ✅ |  |
+| Southeast Asia​ ​ ​ | ✅ | ✅ | ✅ |  |
+| Central India | ✅ | ✅ | ✅ | S2, S3, S3HD, L1, L2 |
 | Jio India West​ ​ | ✅ | ✅ |  |
-| South India <sup>2</sup> |  | | ✅ |
-| Japan East <sup>1</sup> | ✅ | ✅ | ✅ |
+| South India <sup>1</sup> |  | | ✅ |
+| Japan East  | ✅ | ✅ | ✅ |
 | Japan West​ | ✅ | ✅ |  |
 | Korea Central | ✅ | ✅ | ✅ |
 | Korea South​ ​ |  | ✅ |  |
 
-<sup>1</sup> This region has capacity, but some tiers are [not available](search-sku-tier.md#region-availability-by-tier). 
-
-<sup>2</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
+<sup>1</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
 
 ## Azure Government regions
 
-| Region | AI integration | Semantic ranker | Availability zones |
-|--|--|--|--|
-| Arizona | ✅ | ✅  | |
-| Texas |  |  |  |
-| Virginia <sup>1</sup> | ✅ | ✅  | ✅ |
+| Region | AI integration | Semantic ranker | Availability zones | Capacity constrained |
+|--|--|--|--|--|
+| Arizona | ✅ | ✅  | | |
+| Texas |  |  |  | |
+| Virginia | ✅ | ✅  | ✅ | All Tiers |
 
-<sup>1</sup> Currently, this region is at full capacity and not accepting new search services.
 
 ## Azure operated by 21Vianet
 
-| Region | AI integration | Semantic ranker | Availability zones |
-|--|--|--|--|
+| Region | AI integration | Semantic ranker | Availability zones | Capacity constrained |
+|--|--|--|--|--|
 | China East |  |  |  |
-| China East 2 <sup>1</sup> | ✅  | | |
-| China East 3 |  |  |  |
-| China North |  |  | |
-| China North 2 <sup>1</sup> |  |  | |
-| China North 3 | | ✅ | ✅ |
+| China East 2 <sup>1</sup> | ✅  | | | |
+| China East 3 |  |  |  | |
+| China North |  |  | | |
+| China North 2 <sup>1</sup> |  |  | | |
+| China North 3 | | ✅ | ✅ | |
 
 <sup>1</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
 
@@ -143,4 +132,4 @@ You can create an Azure AI Search resource in any of the following Azure public
 - [Azure OpenAI model region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)
 - [Azure AI Vision region list](/azure/ai-services/computer-vision/overview-image-analysis#region-availability)
 - [Availability zone region availability](/azure/reliability/availability-zones-service-support#azure-regions-with-availability-zone-support)
-- [Azure product by region page](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=search)
\ No newline at end of file
+- [Azure product by region page](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=search)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域サポートに関するドキュメントの更新"
}
```

### Explanation
この変更では、Azure AI Searchの地域サポートに関するドキュメントが更新され、内容が改善されました。テーブルのフォーマットが変更され、新しい「容量制約」の項目が追加されることで、各地域の利用状況が一層明確に示されています。

主な変更点は以下の通りです：
- **テーブルの形式変更**: 各地域のテーブルに「容量制約」という新しい列が追加され、特定の地域でのサービスの供給や制約に関する情報が強調されています。
- **地域情報の更新**: 各地域のリストが整理され、一部の地域の状態（例：フルキャパシティの場合や古いインフラの使用など）がより具体的に記載されています。
- **冗長な情報の削除**: いくつかの説明文や注釈が削除され、情報が簡潔になり、読みやすくなっています。
- **日付の更新**: 情報の改訂日付が明示され、最新の内容であることが保証されています。

全体として、利用者がAzure AI Searchリソースの展開に関する地域サポートの状況をより正確に把握できるように、情報が整理され、明確化されています。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -57,18 +57,14 @@ The supported [regions list](search-region-support.md) provides the locations wh
 
 Currently, several regions are at capacity for specific tiers and can't be used for new search services. If you use the Azure portal to create a search service, the portal excludes any region-tier combinations that aren't available.
 
-| Region | Disabled tier (SKU) due to over-capacity |
-|--------|------------------------------------------|
-| Central US | S2, S3, S3HD, L1, L2 |
-| Central India | S2, S3, S3HD, L1, L2|
-| East US| All tiers|
-| East US 2| Basic, S1|
-| Japan East | S2, S3, S3HD, L1, L2 |
-| Qatar Central | All tiers|
-| South Central US | All tiers |
-| US Gov Virginia | All tiers |
-| West Europe | All tiers |
-| West US 3| All tiers |
+| Region | Disabled tier (SKU) due to over-capacity | Suggested alternative |
+|--------|------------------------------------------|-----------------------|
+| Central India | S2, S3, S3HD, L1, L2| South India |
+| East US 2| Basic, S1| Central US |
+| South Central US | All tiers | Central US |
+| US Gov Virginia | All tiers | US Gov Arizona |
+| West Europe | All tiers | Sweden Central/North Europe |
+| West US 3| Basic, S1 | Central US |
 
 ## Feature availability by tier
 
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
この変更では、Azure SearchのSKUティアに関するドキュメントが更新され、特定の地域での利用制限に関する情報が強化されました。既存の「無効なティア」に関するテーブルに「推奨代替」という列が追加され、ユーザーが新しい検索サービスを作成する際の代替案が提案されています。

主な変更点は以下の通りです：
- **テーブルの列の追加**: 無効なSKUとともに「推奨代替」列が追加され、地域ごとの代替サービスの推奨が行われるようになりました。
- **特定地域の情報整理**: 各地域で利用できないSKUが整理され、代替地域が提案されています。たとえば、「Central India」では「South India」が、「East US 2」では「Central US」が代替として示されています。
- **冗長な情報の削除**: テーブルの内容が簡潔になり、無駄な情報が排除されています。

全体として、ユーザーが特定の地域で新しい検索サービスを作成する際に、より明確な選択肢や代替案を提供するための修正がなされています。この変更により、利用者はリソースをより効果的に計画し、管理できるようになるでしょう。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -252,7 +252,7 @@ items:
         - name: Index plain text
           href: search-howto-index-plaintext-blobs.md
         - name: Index CSV
-          href: search-howto-index-csv-blobs.md
+          href: search-how-to-index-csv-blobs.md
         - name: Index JSON
           href: search-howto-index-json-blobs.md
       - name: Troubleshooting guidance
@@ -480,7 +480,7 @@ items:
     - name: Upgrade .NET libraries
       href: search-dotnet-sdk-migration-version-11.md
     - name: Develop in .NET
-      href: search-howto-dotnet-sdk.md
+      href: search-how-to-dotnet-sdk.md
     - name: Manage with Azure SDKs
       href: search-dotnet-mgmt-sdk-migration.md
     - name: Handle concurrent updates
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
この変更では、Azure Searchに関する目次（TOC）ファイルに対して小さな修正が行われました。具体的には、2つのドキュメントリンクのファイル名がハイフンを追加して修正され、統一性と可読性が向上しました。

主な変更点は以下の通りです：
- **ファイル名の修正**: 「search-howto-index-csv-blobs.md」と「search-howto-dotnet-sdk.md」というファイル名が、「search-how-to-index-csv-blobs.md」と「search-how-to-dotnet-sdk.md」という形式に変更されました。これにより、ファイル名の一貫性が実現されています。
- **可読性の向上**: ハイフンを追加することで、ファイル名がより明確になり、ユーザーがリンクを見つけやすくなっています。

全体として、この更新によりドキュメントの目次が整理され、リンク先の識別が容易になっています。これにより、利用者は関連情報を迅速に見つけ、目的の情報にアクセスする際の利便性が向上します。

## articles/search/vector-search-how-to-create-index.md{#item-97c769}

<details>
<summary>Diff</summary>
````diff
@@ -337,13 +337,13 @@ Vector fields are characterized by [their data type](/rest/api/searchservice/sup
                 "retrievable": false,
                 "stored": false,
                 "dimensions": 1536,
-                "vectorSearchProfile": "-vector-profile-1"
+                "vectorSearchProfile": "vector-profile-1"
             }
         ],
         "vectorSearch": {
             "algorithms": [
                 {
-                    "name": "hsnw-1",
+                    "name": "hnsw-1",
                     "kind": "hnsw",
                     "hnswParameters": {
                         "m": 4,
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索インデックス作成ガイドの修正"
}
```

### Explanation
この変更では、Azure Searchに関する「ベクトル検索インデックス作成ガイド」において、2つの小さなテキスト修正が行われました。これにより、整数値を持つプロパティとアルゴリズムの名前が明確になり、一貫性が持たれるようになりました。

主な変更点は以下の通りです：
- **プロファイル名の修正**: `vectorSearchProfile`の値が「-vector-profile-1」から「vector-profile-1」に変更されました。これにより、プロファイル名がより直感的になり、誤解を避けることができます。
- **アルゴリズム名の修正**: アルゴリズム名が「hsnw-1」から「hnsw-1」に変更されました。この修正は、アルゴリズムの正式名称に合わせたもので、ユーザーが正しい情報を取得できるようにしています。

全体として、この更新は文書の精度を向上させ、ユーザーにとっての理解を深めるための重要な改善です。これにより、ベクトル検索に関連する設定や使用方法についての理解が促進されるでしょう。


