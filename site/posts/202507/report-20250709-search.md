---
date: '2025-07-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1d05d59...MicrosoftDocs:2b324c3
summary: 変更の概要は、Azureの検索機能に関連するマニュアルとクイックスタートガイドにおいて、誤ったリンクの修正と新しい.NET用のクイックスタートガイドが追加されたことに焦点を当てています。これにより、ユーザーはより正確で最新の情報を得られるようになり、開発者がAzure
  AI Searchのベクトル検索機能を迅速に実装できるサポートが強化されました。特に、最近追加された「.NETを使ったベクトル検索のクイックスタート」ガイドは、Azure
  AI Searchクライアントライブラリを使用した具体的な実装方法を提供し、ユーザーエクスペリエンスの向上に寄与します。全体として、これらの更新はAzure AI
  Searchの利用を促進し、より多くの開発者がこの機能を活用できるようになることを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1d05d59...MicrosoftDocs:2b324c3){target="_blank"}

# Highlights
今回の変更は、Azure の検索機能に関連するマニュアルおよびクイックスタートガイドに加えられた修正や追加を中心にしています。重要なポイントは、誤ったリンクの修正と新しい.NET用のクイックスタートガイドの追加です。これらの変更により、ユーザーは正確で最新の情報をより簡単にアクセスできるようになり、開発者がAzure AI Searchのベクトル検索機能を迅速に実装するためのサポートが強化されました。

## New features
- 新たに「.NETを使ったベクトル検索のクイックスタート」ガイドが追加されました。このガイドは、Azure AI Searchクライアントライブラリを利用し、.NETアプリケーションでのベクトルの作成、ポピュレート、クエリを実行する方法を詳細に紹介しています。

## Breaking changes
- 特に重大な破壊的変更は含まれていませんが、リンクの不正確さを修正することは、情報アクセスの観点で重要なアップデートです。

## Other updates
- ハイブリッド検索やエージェント型検索のドキュメントにおけるリンクが修正され、より正確なクイックスタートページに更新されました。
- 「ベクトル検索の開始」ドキュメントに、.NETクイックスタートへの参照が追加されました。これにより、ユーザーがベクトル検索機能をより円滑に利用できるようになります。

# Insights
このコード差分の更新は、Azure AI Search の文書整備における重要な改善を表しています。文書の信頼性と使いやすさを向上させるため、誤ったリンクの修正や、新しいクイックスタートガイドの追加が行われています。

例えば、誤ったURLによりユーザーが必要な情報にアクセスできないケースは、開発者の作業効率を低下させる可能性があります。この問題を解消することによって、ユーザーエクスペリエンスが向上し、Azure AI Searchの機能をより効果的に活用するための基盤が整えられました。

さらに、新しい.NET用のクイックスタートガイドが追加されたことで、.NET開発者はこれまで以上に迅速にAzureのベクトル検索機能を導入し、試すことが可能になりました。クイックスタートガイドは、特に実践的なサンプルコードを通じて、AzureのAI機能の利便性を直ちに体感できる点を強調しています。

全体として、この一連の更新は、Azureの検索機能を最大限に活用しようとするユーザーにとって、有益かつ拡張的な支援を提供するものです。これにより、Azure AI Searchの採用が促進され、より幅広い開発者コミュニティでの利用が期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [hybrid-search-how-to-query.md](#item-345ce6) | minor update | ハイブリッド検索クエリのクイックスタートリンクの修正 | modified | 1 | 1 | 2 | 
| [search-get-started-vector-dotnet.md](#item-8f2f1b) | new feature | Vector検索を使用した.NETアプリのクイックスタートガイド追加 | added | 359 | 0 | 359 | 
| [search-agentic-retrieval-concept.md](#item-797a22) | minor update | エージェント型検索のクイックスタートリンクの修正 | modified | 1 | 1 | 2 | 
| [search-get-started-vector.md](#item-4984d9) | minor update | .NETクイックスタートの追加 | modified | 6 | 0 | 6 | 


# Modified Contents
## articles/search/hybrid-search-how-to-query.md{#item-345ce6}

<details>
<summary>Diff</summary>
````diff
@@ -50,7 +50,7 @@ In this article, learn how to:
 
 1. Under **View**, select **JSON view** so that you can paste in a vector query. 
 
-1. Replace the default query template with a hybrid query, such as the "Run a hybrid query" example starting on line 539 in the [vector quickstart](https://raw.githubusercontent.com/Azure-Samples/azure-search-rest-samples/refs/heads/main/Quickstart-vectors/az-search-vector-quickstart.rest). For brevity, the vector is truncated in this article. 
+1. Replace the default query template with a hybrid query, such as the "Run a hybrid query" example starting on line 539 in the [vector quickstart](https://raw.githubusercontent.com/Azure-Samples/azure-search-rest-samples/refs/heads/main/Quickstart-vectors/az-search-quickstart-vectors.rest). For brevity, the vector is truncated in this article. 
 
    A hybrid query has a text query specified in `search`, and a vector query specified under `vectorQueries.vector`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索クエリのクイックスタートリンクの修正"
}
```

### Explanation
この変更は、ドキュメント『ハイブリッド検索のクエリ方法』におけるリンクの修正を含みます。具体的には、既存のリンク先が誤っていたため、正しいクイックスタートのURLに更新されました。これにより、読者がハイブリッドクエリの例を正確に参照できるようにされています。変更点は、90行目でのクイックスタートのURLが「az-search-quickstart-vectors.rest」に変更されたことです。この修正により、ユーザーは最新の情報にアクセスできるようになるため、よりスムーズにガイドを利用できるようになります。全体として、この更新は文書の正確性を向上させるものです。

## articles/search/includes/quickstarts/search-get-started-vector-dotnet.md{#item-8f2f1b}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,359 @@
+---
+manager: nitinme
+author: rotabor
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 06/19/2025
+---
+
+In this quickstart, you work with a .NET app to create, populate, and query vectors. The code examples perform these operations by using the [Azure AI Search client library](/dotnet/api/overview/azure/search). The library provides an abstraction over the REST API for access to index operations such as data ingestion, search operations, and index management operations.
+
+In Azure AI Search, a [vector store](../../vector-store.md) has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. The [Create Index](/rest/api/searchservice/indexes/create-or-update) REST API creates the vector store.
+
+> [!NOTE]
+> This quickstart omits the vectorization step and provides inline embeddings. If you want to add [built-in data chunking and vectorization](../../vector-search-integrated-vectorization.md) over your own content, try the [**Import and vectorize data wizard**](../../search-get-started-portal-import-vectors.md) for an end-to-end walkthrough.
+
+## Prerequisites
+
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+
+- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch) in your current subscription.
+    - You can use a free search service for most of this quickstart, but we recommend the Basic tier or higher for larger data files.
+    - To run the query example that invokes [semantic reranking](../../semantic-search-overview.md), your search service must be at the Basic tier or higher with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
+
+- [Visual Studio Code](https://code.visualstudio.com/download) or [Visual Studio](https://visualstudio.com).
+
+- [Git](https://git-scm.com/downloads) to clone the sample repo.
+
+---
+
+## Retrieve resource information
+
+Requests to the search endpoint must be authenticated and authorized. While it's possible to use API keys or roles for this task, we recommend [using a keyless connection via Microsoft Entra ID](../../search-get-started-rbac.md).
+
+This quickstart uses `DefaultAzureCredential`, which simplifies authentication in both development and production scenarios. However, for production scenarios, you might have more advanced requirements that require a different approach. See [Authenticate .NET apps to Azure services by using the Azure SDK for .NET](/dotnet/azure/sdk/authentication/) to understand all of your options.
+
+## Clone the code and setup environment
+
+1. Clone the repo containing the code for this quickstart. 
+
+   ```bash
+   git clone https://github.com/Azure-Samples/azure-search-dotnet-samples
+   ```
+  
+   This repo has .NET code examples for several articles each in a separate subfolder.
+
+1. Open the subfolder `quickstart-Vector-Search` in Visual Studio Code, or double click the `.sln` file to open the solution in Visual Studio.
+
+1. Open the `appsettings.json` files in the `VectorSearchExamples` and `VectorSearchCreatePopulateIndex` folders. Update the following values: 
+
+   - `AZURE_SEARCH_ENDPOINT`: Find the url of your Azure AI Search service in the [Azure portal](https://portal.azure.com). On the **Overview** page of your search resource, look for the URL field. An example endpoint might look like `https://mydemo.search.windows.net`. 
+   - `AZURE_SEARCH_INDEX_NAME`: Leave the default value provided in the file or enter your own index name.
+
+## Create the vector index and upload documents
+
+To run search queries against the Azure AI Search service, you first need to create a search index and upload documents to the service.
+
+1. Open a new terminal in the `VectorSearchCreatePopulateIndex` folder.
+
+1. Run the project using the `dotnet run` command:
+
+    ```dotnetcli
+    dotnet run
+    ```
+
+The following code executes to create an index:
+
+:::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchcreatepopulateindex/program.cs" id="CreateSearchindex":::
+
+The following code uploads the JSON formatted documents in the `hotel-samples.json` file to the Azure AI Search service:
+
+:::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchcreatepopulateindex/program.cs" id="UploadDocs":::
+
+After you run the project, the following output is printed:
+
+```output
+Key: 1, Succeeded: True
+Key: 2, Succeeded: True
+Key: 3, Succeeded: True
+Key: 4, Succeeded: True
+Key: 48, Succeeded: True
+Key: 49, Succeeded: True
+Key: 13, Succeeded: True
+```
+
+Key takeaways:
+
+- Your code interacts with a specific search index hosted in your Azure AI Search service through the `SearchClient`, which is the main object provided by the `azure-search-documents` package. The `SearchClient` provides access to index operations such as:
+
+    - **Data ingestion**: `UploadDocuments()`, `MergeDocuments()`, `DeleteDocuments()`
+    - **Search operations**: `Search()`, `Autocomplete()`, `Suggest()`
+    - **Index management operations**: `CreateOrUpdateIndex()`
+
+- Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 4096 floating point values each. This size of embeddings generated by the Azure OpenAI **text-embedding-3-small** model for this quickstart is 1536.
+
+## Run search queries
+
+After the index is created and documents are loaded, you can issue vector queries against them by calling `SearchAsync()` with various parameters.
+
+1. In the `VectorSearchExamples` folder, open the `Program.cs` file.
+1. Open a new terminal in the `VectorSearchExamples` folder.
+
+In the following sections, you run queries against the `hotels-vector-quickstart` index. The queries include:
+
+- [Single vector search](#single-vector-search)
+- [Single vector search with filter](#single-vector-search-with-filter)
+- [Hybrid search](#hybrid-search)
+- [Semantic hybrid search with filter](#semantic-hybrid-search-with-a-filter)
+
+### Single vector search
+
+The first example demonstrates a basic scenario where you want to find document descriptions that closely match the search string.
+
+1. In the `Program.cs` file of the `VectorSearchExamples` folder, uncomment the method call `SearchExamples.SearchSingleVector(searchClient, vectorizedResult);`. This method executes the following search function in the `SearchExamples.cs` class:
+
+    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchexamples/SearchExamples.cs" id="SearchSingleVector":::
+
+1. Run the project using the `dotnet run` command:
+
+    ```dotnetcli
+    dotnet run
+    ```
+
+    After you run the project, the search results are printed in the output window:
+    
+    ```output
+    Single Vector Search Results:
+    Score: 0.6605852, HotelId: 48, HotelName: Nordick's Valley Motel
+    Score: 0.6333684, HotelId: 13, HotelName: Luxury Lion Resort
+    Score: 0.605672, HotelId: 4, HotelName: Sublime Palace Hotel
+    Score: 0.6026341, HotelId: 49, HotelName: Swirling Currents Hotel
+    Score: 0.57902366, HotelId: 2, HotelName: Old Century Hotel
+    ```
+
+### Single vector search with filter
+
+You can add filters, but the filters are applied to the nonvector content in your index. In this example, the filter applies to the `Tags` field to filter out any hotels that don't provide free Wi-Fi.
+
+1. In the `Program.cs` file of the `VectorSearchExamples` folder, uncomment the method call `SearchExamples.SearchSingleVectorWithFilter(searchClient, vectorizedResult);`. This method executes the following search function in the `SearchExamples.cs` class:
+
+    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchexamples/SearchExamples.cs" id="SearchSingleVectorWithFilter":::
+
+1.  Run the project again, and the status of each document is printed below it:
+    
+       ```output
+        Single Vector Search With Filter Results:
+        Score: 0.6605852, HotelId: 48, HotelName: Nordick's Valley Motel, Tags: continental breakfastair conditioningfree wifi
+        Score: 0.57902366, HotelId: 2, HotelName: Old Century Hotel, Tags: poolfree wifiair conditioningconcierge
+       ```
+
+       The query was the same as the previous [single vector search example](#single-vector-search), but it includes a post-processing exclusion filter and returns only the two hotels that have free Wi-Fi.
+
+1. The next filter example uses a **geo filter**. In the `Program.cs` file of the `VectorSearchExamples` folder, uncomment the method call `SearchExamples.SingleSearchWithGeoFilter(searchClient, vectorizedResult);`. This method executes the following search function in the `SearchExamples.cs` class:
+
+    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchexamples/SearchExamples.cs" id="SingleSearchWithGeoFilter":::
+   
+   The query was the same as the previous [single vector search example](#single-vector-search), but it includes a post-processing exclusion filter and returns only the two hotels within 300 kilometers.
+
+1.  Run the project again, and the status of each document is printed below it:
+   
+    ```output
+    Vector query with a geo filter:
+    -HotelId: 48
+    HotelName: Nordick's Valley Motel
+    Score: 0.6605852246284485
+    City/State: Washington D.C./null
+    Description: Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.
+    
+    -HotelId: 49
+    HotelName: Swirling Currents Hotel
+    Score: 0.602634072303772
+    City/State: Arlington/VA
+    Description: Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary Wi-Fi and flat-screen TVs.
+    ```
+
+### Hybrid search
+
+Hybrid search consists of keyword queries and vector queries in a single search request. This example runs the vector query and full-text search concurrently:
+
+- **Search string**: `historic hotel walk to restaurants and shopping`
+- **Vector query string** (vectorized into a mathematical representation): `Quintessential lodging near running trails, eateries, retail`
+
+1. In the `Program.cs` file of the `VectorSearchExamples` folder, uncomment the method call `SearchExamples.SearchHybridVectorAndText(searchClient, vectorizedResult);`. This method executes the following search function in the `SearchExamples.cs` class:
+
+    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchexamples/SearchExamples.cs" id="SearchHybridVectorAndText":::
+
+1.  Run the project again, and the status of each document is printed below it:
+
+       ```output
+       Hybrid search results:
+       Score: 0.03279569745063782
+       HotelId: 4
+       HotelName: Sublime Palace Hotel
+       Description: Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th   century resort, updated for every modern convenience.
+       Category: Boutique
+       Tags: conciergeviewair conditioning
+       
+       Score: 0.032786883413791656
+       HotelId: 13
+       HotelName: Luxury Lion Resort
+       Description: Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort.
+       Category: Luxury
+       Tags: barconciergerestaurant
+       
+       Score: 0.03205128386616707
+       HotelId: 48
+       HotelName: Nordick's Valley Motel
+       Description: Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.
+       Category: Boutique
+       Tags: continental breakfastair conditioningfree wifi
+       
+       Score: 0.0317460335791111
+       HotelId: 49
+       HotelName: Swirling Currents Hotel
+       Description: Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary W-Fi and flat-screen TVs.
+       Category: Suite
+       Tags: air conditioninglaundry service24-hour front desk service
+       
+       Score: 0.03077651560306549
+       HotelId: 2
+       HotelName: Old Century Hotel
+       Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer   dinners, and live music.
+       Category: Boutique
+       Tags: poolfree wifiair conditioningconcierge
+       ```
+    
+Because Reciprocal Rank Fusion (RRF) merges results, it helps to review the inputs. The following results are from only the full-text query. The top two results are Sublime Palace Hotel and History Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
+
+```json
+{
+    "@search.score": 2.2626662,
+    "HotelName": "Sublime Palace Hotel",
+    "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace."
+},
+{
+    "@search.score": 0.86421645,
+    "HotelName": "Luxury Lion Resort",
+    "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort"
+},
+```
+
+In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to fourth position. Historic Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
+
+```json
+"value": [
+    {
+        "@search.score": 0.857736,
+        "HotelId": "48",
+        "HotelName": "Nordick's Valley Motel",
+        "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
+        "Category": "Boutique"
+    },
+    {
+        "@search.score": 0.8399129,
+        "HotelId": "49",
+        "HotelName": "Swirling Currents Hotel",
+        "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center.",
+        "Category": "Luxury"
+    },
+    {
+        "@search.score": 0.8383954,
+        "HotelId": "13",
+        "HotelName": "Luxury Lion Resort",
+        "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort",
+        "Category": "Resort and Spa"
+    },
+    {
+        "@search.score": 0.8254346,
+        "HotelId": "4",
+        "HotelName": "Sublime Palace Hotel",
+        "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.",
+        "Category": "Boutique"
+    },
+    {
+        "@search.score": 0.82380056,
+        "HotelId": "1",
+        "HotelName": "Stay-Kay City Hotel",
+        "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York.",
+        "Category": "Boutique"
+    },
+    {
+        "@search.score": 0.81514084,
+        "HotelId": "2",
+        "HotelName": "Old Century Hotel",
+        "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
+        "Category": "Boutique"
+    },
+    {
+        "@search.score": 0.8133763,
+        "HotelId": "3",
+        "HotelName": "Gastronomic Landscape Hotel",
+        "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
+        "Category": "Resort and Spa"
+    }
+]
+```
+
+### Semantic hybrid search with a filter
+
+The hybrid query with semantic ranking is filtered to show only the hotels within a 500-kilometer radius of Washington D.C.
+
+1. In the `Program.cs` file of the `VectorSearchExamples` folder, uncomment the method call `SearchExamples.SearchHybridVectoryAndSemantic(searchClient, vectorizedResult);`. This method executes the following search function in the `SearchExamples.cs` class:
+
+    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchexamples/SearchExamples.cs" id="SearchHybridVectorAndSemantic":::
+
+1.  Run the project again, and review the output below the cell. The response is three hotels, which are filtered by location and faceted by `StateProvince` and semantically reranked to promote results that are closest to the search string query (`historic hotel walk to restaurants and shopping`).
+
+       The Swirling Currents Hotel now moves into the top spot. Without semantic ranking, Nordick's Valley Motel is number one. With semantic ranking, the machine comprehension models recognize that `historic` applies to "hotel, within walking distance to dining (restaurants) and shopping."
+    
+       ```output
+       Total semantic hybrid results: 7
+       - Score: 0.0317460335791111
+         Re-ranker Score: 2.6550590991973877
+         HotelId: 49
+         HotelName: Swirling Currents Hotel
+         Description: Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary Wi-Fi and flat-screen TVs.
+         Category: Suite
+       - Score: 0.03279569745063782
+         Re-ranker Score: 2.599761724472046
+         HotelId: 4
+         HotelName: Sublime Palace Hotel
+         Description: Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.
+         Category: Boutique
+       - Score: 0.03125
+         Re-ranker Score: 2.3480887413024902
+         HotelId: 2
+         HotelName: Old Century Hotel
+         Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
+         Category: Boutique
+       - Score: 0.016393441706895828
+         Re-ranker Score: 2.2718777656555176
+         HotelId: 1
+         HotelName: Stay-Kay City Hotel
+         Description: This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic center of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.
+         Category: Boutique
+       - Score: 0.01515151560306549
+         Re-ranker Score: 2.0582215785980225
+         HotelId: 3
+         HotelName: Gastronomic Landscape Hotel
+         Description: The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.
+         Category: Suite
+       ```
+
+Key takeaways:
+
+- In a hybrid search, you can integrate vector search with full-text search over keywords. Filters, spell check, and semantic ranking apply to textual content only, and not vectors. In this final query, there's no semantic `answer` because the system didn't produce one that was sufficiently strong.
+
+- Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
+
+## Clean up
+
+When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
+
+You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
+
+## Next steps
+
+- Review the repository of code samples for vector search capabilities in Azure AI Search for [.NET](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet)
+- Review the other .NET and Azure AI Search code samples in the [azure-search-dotnet-samples repo](https://github.com/Azure-Samples/azure-search-dotnet-samples)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Vector検索を使用した.NETアプリのクイックスタートガイド追加"
}
```

### Explanation
この変更は、新たに「.NETを使ったベクトル検索のクイックスタート」ガイドが追加されたことを示しています。このガイドでは、.NETアプリケーションでベクトルを作成、ポピュレート、クエリを行う方法が説明されています。具体的には、Azure AI Searchクライアントライブラリを使用して操作を実行するサンプルコードが多数提供されています。

新たに追加されたファイルには、Azure AI Searchに必要な前提条件や、環境設定の手順、リソース情報の取得方法、ドキュメントのアップロード、検索クエリの実行方法が詳細に説明されています。特に、シングルベクトル検索やフィルター付き検索、ハイブリッド検索を実行する手順が解説されており、利用者がAzureの検索機能を実行する際の実践的な情報が盛り込まれています。

この追加により、開発者は迅速にベクトル検索を実装し、実際の環境での活用方法を学ぶことができるようになります。新しいガイドは、Azure AI Searchの機能を活用するための貴重なリソースとなるでしょう。

## articles/search/search-agentic-retrieval-concept.md{#item-797a22}

<details>
<summary>Diff</summary>
````diff
@@ -152,7 +152,7 @@ Choose any of these options for your next step.
 
   + [Quickstart-Agentic-Retrieval: Python](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval)
   + [Quickstart-Agentic-Retrieval: .NET](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-agentic-retrieval)
-  + [Quickstart-Agentic-Retrieval: REST](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/agentic-retrieval)
+  + [Quickstart-Agentic-Retrieval: REST](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-agentic-retrieval)
   + [End-to-end with Azure AI Search and Azure AI Agent Service](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example)
 
 + How-to guides for a focused look at development tasks:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント型検索のクイックスタートリンクの修正"
}
```

### Explanation
この変更は、ドキュメント「エージェント型検索の概念」におけるリンクの修正を反映しています。具体的には、RESTに関するクイックスタートのURLが変更されました。旧来のリンクは誤っていたため、新しい正しいパス「Quickstart-agentic-retrieval」に修正されています。

この修正は、読者が最新かつ正確な情報にアクセスできるようにするため、重要です。リンクの正確性をサポートすることで、開発者が必要なリソースを見つけやすくなり、文書の使いやすさが向上します。全体として、この更新はドキュメントの品質改善に寄与しています。

## articles/search/search-get-started-vector.md{#item-4984d9}

<details>
<summary>Diff</summary>
````diff
@@ -32,6 +32,12 @@ zone_pivot_groups: search-get-started-vector-search
 
 ::: zone-end
 
+::: zone pivot="dotnet"
+
+[!INCLUDE [.NET quickstart](includes/quickstarts/search-get-started-vector-dotnet.md)]
+
+::: zone-end
+
 ::: zone pivot="rest"
 
 [!INCLUDE [REST quickstart](includes/quickstarts/search-get-started-vector-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": ".NETクイックスタートの追加"
}
```

### Explanation
この変更は、「ベクトル検索の開始」に関するドキュメントにおいて、.NET用のクイックスタートへの参照を追加する修正を示しています。具体的には、新たに以下のコードブロックが追加されました。

```markdown
::: zone pivot="dotnet"

[!INCLUDE [.NET quickstart](includes/quickstarts/search-get-started-vector-dotnet.md)]

::: zone-end
```

この追加により、ユーザーはベクトル検索を利用するための.NETフレームワーク向けのクイックスタートに直接アクセスできるようになりました。この情報は、開発者がベクトル検索を迅速に開始するための重要な手助けとなり、より具体的な実装方法を学ぶ機会を提供します。

全体として、このマイナーな更新は、ドキュメントの使い勝手を向上させ、利用者が必要なリソースを見つけやすくするために重要な分岐点を示しています。


