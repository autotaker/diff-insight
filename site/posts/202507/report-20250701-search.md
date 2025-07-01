---
date: '2025-07-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8f107da...MicrosoftDocs:5b7339b
summary: Azure AI検索のベクタークイックスタートにJavaScriptとTypeScriptのガイドが新たに追加されました。これにより、開発者はそれぞれのプログラミング言語を使用してAzure
  AI検索サービスのベクター機能を実装する方法を学ぶことができます。新しいガイドには、ベクターの作成やデータのロード、クエリの実行に関する手順が含まれています。また、既存のクイックスタートドキュメントにもこれらの言語のセクションが追加されました。特に破壊的な変更はなく、現行ユーザーは安心して新しいガイドを利用できます。この変更は、異なる技術スタックを持つ開発者がAzureの機能を活用しやすくすることを目的としています。組織や開発者にとっては、具体的な実装方法とトラブルシューティング情報が提供されるため、非常に有益です。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8f107da...MicrosoftDocs:5b7339b){target="_blank"}

<format>
# ハイライト
Azure AI検索のベクタークイックスタートに新たにJavaScriptとTypeScriptのガイドが追加されました。これにより、開発者はAzure AI検索サービスにおけるベクター機能をそれぞれのプログラミング言語で実装する具体的な方法を学ぶことができます。これらの手順にはベクターの作成、データのロード、クエリの実行が含まれています。また、それに関連して、既存のクイックスタートドキュメントに新しいセクションが追加されました。

## 新しい機能
- **JavaScriptを使用したベクタークイックスタートガイド**：JavaScript SDKを利用してAzure AI検索のベクター機能を使用するための詳細なガイド。
- **TypeScriptを使用したベクタークイックスタートガイド**：TypeScriptプロジェクトにおけるベクター検索の実装方法を説明するガイド。TypeScriptでハイブリッド検索を行う方法も含む。

## 破壊的変更
特に破壊的変更はありません。既存の機能や使用方法に影響する変更はないため、現行ユーザーは安心して新しいガイドを利用できます。

## その他の更新
- 「ベクター検索のクイックスタート」ドキュメントに、JavaScriptとTypeScriptのセクションが追加され、各言語のクイックスタートへのリンクを提供。

# インサイト
Azure AI検索のこの変更は、開発者により多様な選択肢とサポートを提供することを目的としています。最新の変更により、JavaScriptとTypeScriptを使用したプロジェクトにも適した統合ガイドが用意されることで、異なる技術スタックを持つ開発者が容易にAzureの機能を活用できるようになります。

このようなガイドの追加は、特にAzure AI検索サービスを新たに取り入れようとしている組織や開発者にとって有益です。それぞれの言語でインデックスとクエリの操作を詳細に解説しており、示されたサンプルコードは、実際の開発環境での実装に役立ちます。さらに、正確なエラー処理や環境設定についての情報が含まれているため、導入の際のトラブルシューティングにも対応できます。

結果として、Azure AI検索サービスは、より広範な開発者コミュニティがアクセスしやすく、使用しやすいものとなり、プロジェクトの検索機能における質の向上が期待できます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-get-started-vector-javascript.md](#item-d0387c) | new feature | JavaScriptを使用したAzure AI検索用ベクタークイックスタートの追加 | added | 518 | 0 | 518 | 
| [search-get-started-vector-typescript.md](#item-9b3bc8) | new feature | TypeScriptを使用したAzure AI検索用ベクタークイックスタートの追加 | added | 555 | 0 | 555 | 
| [search-get-started-vector.md](#item-4984d9) | minor update | ベクター検索のクイックスタートにJavaScriptおよびTypeScriptのセクションを追加 | modified | 12 | 0 | 12 | 


# Modified Contents
## articles/search/includes/quickstarts/search-get-started-vector-javascript.md{#item-d0387c}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,518 @@
+---
+manager: nitinme
+author: diberry
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 06/30/2025
+---
+
+In this quickstart, you use JavaScript to create, load, and query vectors. The code examples perform these operations by using the [Azure AI Search client library](/javascript/api/overview/azure/search-documents-readme). The library provides an abstraction over the REST API for access to index operations such as data ingestion, search operations, and index management operations.
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
+- [Visual Studio Code](https://code.visualstudio.com/download).
+
+- [Node.JS with LTS](https://nodejs.org/en/download/).
+
+---
+
+## Get service endpoints
+
+In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints so that you can provide them as variables in your code.
+
+1. Sign in to the [Azure portal](https://portal.azure.com).
+
+1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
+
+1. On the **Overview** home page, copy the URL. An example endpoint might look like `https://example.search.windows.net`. 
+
+
+## Set up the Node.JS project
+
+Set up project with Visual Studio Code and JavaScript.
+
+1. Start Visual Studio Code in a new directory.
+
+   ```bash
+   mkdir vector-quickstart && cd vector-quickstart
+   code .
+   ```
+1. Create a new package for ESM modules in your project directory.
+
+   ```bash
+   npm init -y
+   npm pkg set type=module
+   ```
+
+   This creates a `package.json` file with default values.
+
+
+1. Install the following npm packages.
+
+   ```bash
+   npm install @azure/identity @azure/search-documents dotenv
+   ``` 
+
+1. Create a `src` directory in your project directory.
+
+   ```bash
+   mkdir src
+   ```
+
+## Set up environment variables for local development
+
+1. Create a `.env` file in your `vector-quickstart` project directory.
+1. Add the following environment variables to the `.env` file, replacing the values with your own service endpoints and keys.
+
+   ```plaintext
+   AZURE_SEARCH_ENDPOINT=<YOUR AZURE AI SEARCH ENDPOINT>
+   AZURE_SEARCH_INDEX_NAME=hotels-vector-quickstart
+   ```
+## Sign in to Azure
+
+You're using Microsoft Entra ID and role assignments for the connection. Make sure you're logged in to the same tenant and subscription as Azure AI Search and Azure OpenAI. You can use the Azure CLI on the command line to show current properties, change properties, and to sign in. For more information, see [Connect without keys](../../search-get-started-rbac.md). 
+
+Run each of the following commands in sequence.
+
+```azure-cli
+az account show
+
+az account set --subscription <PUT YOUR SUBSCRIPTION ID HERE>
+
+az login --tenant <PUT YOUR TENANT ID HERE>
+```
+
+You should now be logged in to Azure from your local device.
+
+
+## Create the vector index 
+
+In this section, you create a vector index in Azure AI Search with [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient).[createOrUpdateIndex](/javascript/api/@azure/search-documents/searchindexclient#@azure-search-documents-searchindexclient-createorupdateindex). The index schema defines the fields, including the vector field `DescriptionVector`. 
+
+1. Create a `createIndex.js` file in the `src` directory.
+
+1. Copy the following code into the file. 
+
+    :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/createIndex.js":::
+
+    The code file adds the dependencies, environment variables, and JavaScript type for `HotelDocument` to the top of the file. Add the `createIndex` function to create the index. The function defines the index schema, including the vector field `DescriptionVector`.
+
+1. Run the file:
+
+    ```console
+    node -r dotenv/config src/createIndex.js
+    ```
+1. The output of this code shows that the index is created successfully:
+
+    ```console
+    Using Azure Search endpoint: https://my-service.search.windows.net
+    Using index name: hotels-vector-quickstart
+    Creating index...
+    hotels-vector-quickstart created
+    ```
+
+   Key takeaways when creating vector index with the `@azure/search-documents` library:
+
+   - You define an index by creating a list of fields. 
+
+   - This particular index supports multiple search capabilities, such as:
+      - Full-text keyword search (`searchable`)
+      - Vector search (enables hybrid search by collocating vector and nonvector fields) fields (`DescriptionVector` with `vectorSearchProfileName`)
+      - Semantic search 
+      - Faceted search (`searchSuggester`)
+      - Geo-spatial search (`Location` field with `geo.distance`)
+      - Filtering, sorting (Many fields marked filterable and sortable)
+
+
+## Upload documents to the index
+
+Creating and loading the index are separate steps. You created the index schema [in the previous step](#create-the-vector-index). Now you need to load documents into the index with [SearchClient](/javascript/api/@azure/search-documents/searchclient).[uploadDocuments](/javascript/api/%40azure/search-documents/searchclient#@azure-search-documents-searchclient-uploaddocuments). The documents contain the vectorized version of the article's description, which enables similarity search based on meaning rather than exact keywords.
+
+In Azure AI Search, the index stores all searchable content, while the search engine executes queries against that index.
+
+1. Create a `uploadDocuments.js` file in the `src` directory.
+1. Copy the following code into the file.
+
+    :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/uploadDocuments.js" :::
+
+    This code loads an array of JSON objects. Each document includes the vectorized version of the article's `description`. This vector enables similarity search, where matching is based on meaning rather than exact keywords.
+
+    Because this quickstart article searches the index immediately, the `waitUntilIndexed` function waits until the index is ready for search operations. This is important because the index needs to be fully populated with documents before you can perform searches.
+
+1. Build and run the file:
+
+    ```console
+    node -r dotenv/config src/uploadDocuments.js
+    ```
+1. The output of this code shows that the documents are indexed and ready for search:
+
+    ```console
+    Uploading documents...
+    Key: 1, Succeeded: true, ErrorMessage: none
+    Key: 2, Succeeded: true, ErrorMessage: none
+    Key: 3, Succeeded: true, ErrorMessage: none
+    Key: 4, Succeeded: true, ErrorMessage: none
+    Key: 48, Succeeded: true, ErrorMessage: none
+    Key: 49, Succeeded: true, ErrorMessage: none
+    Key: 13, Succeeded: true, ErrorMessage: none
+    Waiting for indexing... Current count: 0
+    All documents indexed successfully.
+    ```
+
+    Key takeaways about the upload_documents() method and this example:
+    
+    * Your code interacts with a specific search index hosted in your Azure AI Search service through the SearchClient, which is the main object provided by the @azure/search-documents package. The SearchClient provides access to index operations such as:
+        * Data ingestion - uploadDocuments(), mergeDocuments(), deleteDocuments(), etc.
+        * Search operations - search(), autocomplete(), suggest()
+        * Index management operations such as createIndex(), deleteIndex(), getIndex(), etc.
+    * Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 4096 floating point values each. This quickstart sets the dimensions attribute to 1,536 because that's the size of embeddings generated by the Azure OpenAI text-embedding-ada-002 model.
+
+## Create the query as a vector
+
+The example vector queries are based on two strings:
+
+- **Search string**: `historic hotel walk to restaurants and shopping`
+- **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
+
+The vector query string is semantically similar to the search string, but it includes terms that don't exist in the search index. If you do a keyword search for `quintessential lodging near running trails, eateries, retail`, results are zero. We use this example to show how you can get relevant results even if there are no matching terms.
+
+1. Create a `queryVector.js` file in the `src` directory and add the code to create the query vector.
+
+    :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/queryVector.js" :::
+
+1. This code is used in the following sections to perform vector searches. The query vector is created using an embedding model from Azure OpenAI.
+
+
+## Create a single vector search
+
+The first example demonstrates a basic scenario where you want to find document descriptions that closely match the search string using the [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions).
+
+1. Create a `searchSingle.js` file in the `src` directory.
+
+1. Copy the following code into the file.
+
+    :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/searchSingle.js" :::
+
+    The vectorQuery contains the configuration of the vectorized query including the vectorized text of the query input as `vector`,  `fields` determines which vector fields are searched, and `kNearestNeighborsCount` specifies the number of nearest neighbors to return.
+
+    The vector query string is `quintessential lodging near running trails, eateries, retail`, which is vectorized into 1,536 embeddings for this query.
+
+1. Build and run the file:
+
+    ```console
+    node -r dotenv/config src/searchSingle.js
+    ```
+
+1. The output of this code shows the relevant docs for the query `quintessential lodging near running trails, eateries, retail`. 
+
+    ```console
+    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
+    Using index name: hotels-vector-quickstart-0627-4
+    
+    
+    Single Vector search found 5
+    - HotelId: 48, HotelName: Nordick's Valley Motel, Tags: ["continental breakfast","air conditioning","free wifi"], Score 0.6605852
+    - HotelId: 13, HotelName: Luxury Lion Resort, Tags: ["bar","concierge","restaurant"], Score 0.6333684
+    - HotelId: 4, HotelName: Sublime Palace Hotel, Tags: ["concierge","view","air conditioning"], Score 0.605672
+    - HotelId: 49, HotelName: Swirling Currents Hotel, Tags: ["air conditioning","laundry service","24-hour front desk service"], Score 0.6026341
+    - HotelId: 2, HotelName: Old Century Hotel, Tags: ["pool","free wifi","air conditioning","concierge"], Score 0.57902366
+    ```
+
+    The response for the vector equivalent of `quintessential lodging near running trails, eateries, retail` consists of 5 results with only the fields specified by the select returned.
+
+
+## Create a single vector search with a filter
+
+You can add filters, but the filters are applied to the nonvector content in your index. In this example, the filter applies to the `Tags` field to filter out any hotels that don't provide free Wi-Fi. This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
+
+1. Create a `searchSingleWithFilter.js` file in the `src` directory.
+
+1. Copy the following code into the file.
+
+    :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/searchSingleWithFilter.js" :::
+
+    Add the dependencies, environment variables, and the same search functionality as the previous search with a post-processing exclusion filter added for hotels with `free wifi`.
+
+1. Build and run the file:
+
+    ```console
+    node -r dotenv/config src/searchSingleWithFilter.js
+    ```
+1. The output of this code shows the relevant documents for the query with the filter for `free wifi` applied:
+
+    ```console
+    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
+    Using index name: hotels-vector-quickstart-0627-4
+    
+    
+    Single Vector search found 2
+    - HotelId: 48, HotelName: Nordick's Valley Motel, Tags: ["continental breakfast","air conditioning","free wifi"], Score 0.6605852
+    - HotelId: 2, HotelName: Old Century Hotel, Tags: ["pool","free wifi","air conditioning","concierge"], Score 0.57902366
+    ```
+
+## Create a search with a geospatial filter    
+
+You can specify a geospatial filter to limit results to a specific geographic area. In this example, the filter limits results to hotels within 300 kilometers of Washington D.C. (coordinates: `-77.03241 38.90166`). Geospatial distances are always in kilometers. This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
+
+1. Create a `searchSingleWithFilterGeo.js` file in the `src` directory.
+
+1. Copy the following code into the file.
+
+    :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/searchSingleWithFilterGeo.js" :::
+1. Build and run the file:
+
+    ```console
+    node -r dotenv/config src/searchSingleWithFilterGeo.js
+    ```
+
+1. The output of this code shows the relevant documents for the query with the geospatial post-processing exclusion filter applied:
+
+    ```console
+    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
+    Using index name: hotels-vector-quickstart-0627-4
+    
+    
+    Single Vector search found 2
+    - HotelId: 48, HotelName: Nordick's Valley Motel, Tags: N/A, Score 0.6605852246284485
+    - HotelId: 49, HotelName: Swirling Currents Hotel, Tags: N/A, Score 0.602634072303772
+    ```
+
+
+## Create a hybrid search
+
+Hybrid search consists of keyword queries and vector queries in a single search request. This example runs the vector query and full-text search concurrently:
+
+- **Search string**: `historic hotel walk to restaurants and shopping`
+- **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
+
+This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
+
+1. Create a `searchHybrid.js` file in the `src` directory.
+1. Copy the following code into the file.
+
+    :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/searchHybrid.js" :::
+1. Build and run the file:
+
+    ```console
+    node -r dotenv/config src/searchHybrid.js
+    ```
+1. The output of this code shows the relevant documents for the hybrid search:
+
+    ```console
+    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
+    Using index name: hotels-vector-quickstart-0627-4
+    
+    
+    Hybrid search found 7 then limited to top 5
+    - Score: 0.03279569745063782
+      HotelId: 4
+      HotelName: Sublime Palace Hotel
+      Description: Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.
+      Category: Boutique
+      Tags: ["concierge","view","air conditioning"]
+    
+    - Score: 0.032522473484277725
+      HotelId: 13
+      HotelName: Luxury Lion Resort
+      Description: Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort.
+      Category: Luxury
+      Tags: ["bar","concierge","restaurant"]
+    
+    - Score: 0.03205128386616707
+      HotelId: 48
+      HotelName: Nordick's Valley Motel
+      Description: Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.
+      Category: Boutique
+      Tags: ["continental breakfast","air conditioning","free wifi"]
+    
+    - Score: 0.0317460335791111
+      HotelId: 49
+      HotelName: Swirling Currents Hotel
+      Description: Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary W-Fi and flat-screen TVs.
+      Category: Suite
+      Tags: ["air conditioning","laundry service","24-hour front desk service"]
+    
+    - Score: 0.03125
+      HotelId: 2
+      HotelName: Old Century Hotel
+      Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
+      Category: Boutique
+      Tags: ["pool","free wifi","air conditioning","concierge"]
+    ```
+
+    Because Reciprocal Rank Fusion (RRF) merges results, it helps to review the inputs. The following results are from only the full-text query. The top two results are Sublime Palace Hotel and History Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
+
+    ```json
+       {
+           "@search.score": 2.2626662,
+           "HotelName": "Sublime Palace Hotel",
+           "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace."
+       },
+       {
+           "@search.score": 0.86421645,
+           "HotelName": "Luxury Lion Resort",
+           "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort"
+       },
+    ```
+
+    In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to fourth position. Historic Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
+   
+   ```json
+   "value": [
+       {
+           "@search.score": 0.857736,
+           "HotelId": "48",
+           "HotelName": "Nordick's Valley Motel",
+           "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
+           "Category": "Boutique"
+       },
+       {
+           "@search.score": 0.8399129,
+           "HotelId": "49",
+           "HotelName": "Swirling Currents Hotel",
+           "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center.",
+           "Category": "Luxury"
+       },
+       {
+           "@search.score": 0.8383954,
+           "HotelId": "13",
+           "HotelName": "Luxury Lion Resort",
+           "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort",
+           "Category": "Resort and Spa"
+       },
+       {
+           "@search.score": 0.8254346,
+           "HotelId": "4",
+           "HotelName": "Sublime Palace Hotel",
+           "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.",
+           "Category": "Boutique"
+       },
+       {
+           "@search.score": 0.82380056,
+           "HotelId": "1",
+           "HotelName": "Stay-Kay City Hotel",
+           "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York.",
+           "Category": "Boutique"
+       },
+       {
+           "@search.score": 0.81514084,
+           "HotelId": "2",
+           "HotelName": "Old Century Hotel",
+           "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
+           "Category": "Boutique"
+       },
+       {
+           "@search.score": 0.8133763,
+           "HotelId": "3",
+           "HotelName": "Gastronomic Landscape Hotel",
+           "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
+           "Category": "Resort and Spa"
+       }
+   ]
+   ```
+
+## Create a semantic hybrid search
+
+Here's the last query in the collection to create extend the semantic hybrid search with the additional search text `historic hotel walk to restaurants and shopping`.
+
+This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
+
+1. Create a `searchSemanticHybrid.js` file in the `src` directory.
+1. Copy the following code into the file.
+
+    :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/searchSemanticHybrid.js" :::
+
+1. Build and run the file:
+
+    ```console
+    node -r dotenv/config src/searchSemanticHybrid.js
+    ```
+
+1. The output of this code shows the relevant documents for the semantic hybrid search:
+
+    ```console
+    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
+    Using index name: hotels-vector-quickstart-0627-4
+
+    
+    Semantic hybrid search found 7 then limited to top 5
+    - Score: 0.0317460335791111
+      Re-ranker Score: 2.6550590991973877
+      HotelId: 49
+      HotelName: Swirling Currents Hotel
+      Description: Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary W-Fi and flat-screen TVs.
+      Category: Suite
+    
+    - Score: 0.03279569745063782
+      Re-ranker Score: 2.599761724472046
+      HotelId: 4
+      HotelName: Sublime Palace Hotel
+      Description: Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.
+      Category: Boutique
+    
+    - Score: 0.03125
+      Re-ranker Score: 2.3480887413024902
+      HotelId: 2
+      HotelName: Old Century Hotel
+      Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
+      Category: Boutique
+    
+    - Score: 0.016393441706895828
+      Re-ranker Score: 2.2718777656555176
+      HotelId: 1
+      HotelName: Stay-Kay City Hotel
+      Description: This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.
+      Category: Boutique
+    
+    - Score: 0.01515151560306549
+      Re-ranker Score: 2.0582215785980225
+      HotelId: 3
+      HotelName: Gastronomic Landscape Hotel
+      Description: The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.
+      Category: Suite
+    ```
+
+    You can think of the semantic ranking as a way to improve the relevance of search results by understanding the meaning behind the words in the query and the content of the documents. In this case, the semantic ranking helps to identify hotels that are not only relevant to the keywords but also match the intent of the query:
+    
+    Key takeaways: 
+
+    - Vector search is specified through the `vectorSearchOptions` property. Keyword search is specified through the `semanticSearchOptions` property.
+
+    - In a hybrid search, you can integrate vector search with full-text search over keywords. Filters, spell check, and semantic ranking apply to textual content only, and not vectors. In this final query, there's no semantic `answer` because the system didn't produce one that was sufficiently strong.
+
+    - Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
+
+## Clean up
+
+When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
+
+You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
+
+If you want to keep the search service, but delete the index and documents, you can delete the index programmatically.
+
+1. Create a `deleteIndex.js` file in the `src` directory.
+1. Add the dependencies, environment variables, and code to delete the index.
+
+    :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/deleteIndex.js" :::
+
+1. Build and run the file:
+
+    ```console
+    node -r dotenv/config src/deleteIndex.js
+    ```
+
+## Next steps
+
+- Review the repository of code samples for vector search capabilities in Azure AI Search for [JavaScript](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "JavaScriptを使用したAzure AI検索用ベクタークイックスタートの追加"
}
```

### Explanation
この変更は、JavaScriptを使用してAzure AI検索のベクター機能を利用するためのクイックスタートガイドを追加するものです。新たに追加されたファイルでは、ベクターの作成、データのロード、クエリ実行方法を詳細に説明しています。このクイックスタートは、JavaScript SDKを利用した実際のコーディングの手順に基づいており、Azureのサービスに接続する際の要件や環境設定についても触れています。

具体的には、以下のような手順が含まれています：
- Azureアカウントの作成とAzure AI searchサービスの準備方法。
- Node.jsプロジェクトの構成及び必要なnpmパッケージのインストール方法。
- Azure AI Searchクライアントライブラリを用いた、ベクター検索インデックスの作成。
- ベクター検索を実行するためのAPI呼び出しの構成とクエリの実行手順。

これにより、開発者はAzureのベクター検索機能を容易に利用できるようになり、リアルタイムでのデータ検索や、キーワードに基づく検索結果の精度向上を実現できます。また、サンプルコードが含まれているため、実際のアプリケーション開発に役立つリファレンスとしても機能します。

## articles/search/includes/quickstarts/search-get-started-vector-typescript.md{#item-9b3bc8}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,555 @@
+---
+manager: nitinme
+author: diberry
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 06/30/2025
+---
+
+In this quickstart, you use TypeScript to create, load, and query vectors. The code examples perform these operations by using the [Azure AI Search client library](/javascript/api/overview/azure/search-documents-readme). The library provides an abstraction over the REST API for access to index operations such as data ingestion, search operations, and index management operations.
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
+- [Visual Studio Code](https://code.visualstudio.com/download).
+
+- [Node.JS with LTS](https://nodejs.org/en/download/).
+- [TypeScript](https://www.typescriptlang.org/download). You can globally install TypeScript using npm:
+
+   ```bash
+   npm install -g typescript
+   ```
+
+---
+
+## Get service endpoints
+
+In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints so that you can provide them as variables in your code.
+
+1. Sign in to the [Azure portal](https://portal.azure.com).
+
+1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
+
+1. On the **Overview** home page, copy the URL. An example endpoint might look like `https://example.search.windows.net`. 
+
+
+
+## Set up the Node.JS project
+
+Set up project with Visual Studio Code and TypeScript.
+
+1. Start Visual Studio Code in a new directory.
+
+   ```bash
+   mkdir vector-quickstart && cd vector-quickstart
+   code .
+   ```
+1. Create a new package for ESM modules in your project directory.
+
+   ```bash
+   npm init -y
+   npm pkg set type=module
+   ```
+
+   This creates a `package.json` file with default values.
+
+1. Edit `package.json` to include a build script. Add the following line to the `scripts` section:
+
+   ```json
+   "build": "tsc"
+   ```
+
+1. Install the following npm packages.
+
+   ```bash
+   npm install @azure/identity @azure/search-documents dotenv @types/node
+   ``` 
+
+1. Create a `src` directory in your project directory.
+
+   ```bash
+   mkdir src
+   ```
+
+1. Create a `tsconfig.json` file in the project directory for ESM with the following content.
+
+    ```json
+    {
+      "compilerOptions": {
+        "target": "esnext",
+        "module": "NodeNext",
+        "moduleResolution": "nodenext",
+        "rootDir": "./src",
+        "outDir": "./dist/",
+        "esModuleInterop": true,
+        "forceConsistentCasingInFileNames": true,
+        "strict": true,
+        "skipLibCheck": true,
+        "declaration": true,
+        "sourceMap": true,
+        "resolveJsonModule": true,
+        "moduleDetection": "force", // Add this for ESM
+        "allowSyntheticDefaultImports": true // Helpful for ESM interop
+      },
+      "include": [
+        "src/**/*.ts"
+      ]
+    }
+   ```
+
+## Set up environment variables for local development
+
+1. Create a `.env` file in your `vector-quickstart` project directory.
+1. Add the following environment variables to the `.env` file, replacing the values with your own service endpoints and keys.
+
+   ```plaintext
+   AZURE_SEARCH_ENDPOINT=<YOUR AZURE AI SEARCH ENDPOINT>
+   AZURE_SEARCH_INDEX_NAME=hotels-vector-quickstart
+   ```
+
+## Sign in to Azure
+
+You're using Microsoft Entra ID and role assignments for the connection. Make sure you're logged in to the same tenant and subscription as Azure AI Search and Azure OpenAI. You can use the Azure CLI on the command line to show current properties, change properties, and to sign in. For more information, see [Connect without keys](../../search-get-started-rbac.md). 
+
+Run each of the following commands in sequence.
+
+```azure-cli
+az account show
+
+az account set --subscription <PUT YOUR SUBSCRIPTION ID HERE>
+
+az login --tenant <PUT YOUR TENANT ID HERE>
+```
+
+You should now be logged in to Azure from your local device.
+
+
+## Create the vector index 
+
+In this section, you create a vector index in Azure AI Search with [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient).[createOrUpdateIndex](/javascript/api/@azure/search-documents/searchindexclient#@azure-search-documents-searchindexclient-createorupdateindex). The index schema defines the fields, including the vector field `DescriptionVector`. Once the index is created, you upload documents to the index. The documents contain the vectorized version of the article's description, which enables similarity search based on meaning rather than exact keywords.
+
+1. Create a `createIndex.ts` file in the `src` directory.
+
+1. Copy the following code into the file. 
+
+    :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/createIndex.ts":::
+
+    The code file adds the dependencies, environment variables, and JavaScript type for `HotelDocument` to the top of the file. Add the `createIndex` function to create the index. The function defines the index schema, including the vector field `DescriptionVector`.
+
+1. Build and run the file:
+
+    ```console
+    npm run build && node -r dotenv/config dist/createIndex.js
+    ```
+1. The output of this code shows that the index is created successfully:
+
+    ```console
+    Using Azure Search endpoint: https://my-service.search.windows.net
+    Using index name: hotels-vector-quickstart
+    Creating index...
+    hotels-vector-quickstart created
+    ```
+
+   Key takeaways when creating vector index with the `@azure/search-documents` library:
+
+   - You define an index by creating a list of fields. 
+
+   - This particular index supports multiple search capabilities, such as:
+      - Full-text keyword search (`searchable`)
+      - Vector search (enables hybrid search by collocating vector and nonvector fields) fields (`DescriptionVector` with `vectorSearchProfileName`)
+      - Semantic search 
+      - Faceted search (`searchSuggester`)
+      - Geo-spatial search (`Location` field with `geo.distance`)
+      - Filtering, sorting (Many fields marked filterable and sortable)
+
+
+## Upload documents to the index
+
+Creating and loading the index are separate steps. You created the index schema [in the previous step](#create-the-vector-index). Now you need to load documents into the index with [SearchClient](/javascript/api/@azure/search-documents/searchclient).[uploadDocuments](/javascript/api/%40azure/search-documents/searchclient#@azure-search-documents-searchclient-uploaddocuments).
+
+In Azure AI Search, the index stores all searchable content, while the search engine executes queries against that index.
+
+1. Create a `uploadDocuments.ts` file in the `src` directory.
+1. Copy the following code into the file.
+
+    :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/uploadDocuments.ts" :::
+
+    This code loads a variable documents with a JSON object describing each document, along with the vectorized version of the article's description. This vector enables similarity search, where matching is based on meaning rather than exact keywords.
+
+    Because this quickstart article searches the index immediately, the `waitUntilIndexed` function waits until the index is ready for search operations. This is important because the index needs to be fully populated with documents before you can perform searches.
+
+1. Build and run the file:
+
+    ```console
+    npm run build && node -r dotenv/config dist/uploadDocuments.js
+    ```
+1. The output of this code shows that the documents are indexed and ready for search:
+
+    ```console
+    Uploading documents...
+    Key: 1, Succeeded: true, ErrorMessage: none
+    Key: 2, Succeeded: true, ErrorMessage: none
+    Key: 3, Succeeded: true, ErrorMessage: none
+    Key: 4, Succeeded: true, ErrorMessage: none
+    Key: 48, Succeeded: true, ErrorMessage: none
+    Key: 49, Succeeded: true, ErrorMessage: none
+    Key: 13, Succeeded: true, ErrorMessage: none
+    Waiting for indexing... Current count: 0
+    All documents indexed successfully.
+    ```
+
+    Key takeaways about the upload_documents() method and this example:
+    
+    * Your code interacts with a specific search index hosted in your Azure AI Search service through the SearchClient, which is the main object provided by the @azure/search-documents package. The SearchClient provides access to index operations such as:
+        * Data ingestion - uploadDocuments(), mergeDocuments(), deleteDocuments(), etc.
+        * Search operations - search(), autocomplete(), suggest()
+        * Index management operations such as createIndex(), deleteIndex(), getIndex(), etc.
+    * Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 4096 floating point values each. This quickstart sets the dimensions attribute to 1,536 because that's the size of embeddings generated by the Azure OpenAI text-embedding-ada-002 model.
+
+## Create the query as a vector
+
+The example vector queries are based on two strings:
+
+- **Search string**: `historic hotel walk to restaurants and shopping`
+- **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
+
+The vector query string is semantically similar to the search string, but it includes terms that don't exist in the search index. If you do a keyword search for `quintessential lodging near running trails, eateries, retail`, results are zero. We use this example to show how you can get relevant results even if there are no matching terms.
+
+1. Create a `queryVector.ts` file in the `src` directory and add the code to create the query vector.
+
+    :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/queryVector.ts" :::
+
+1. This code is used in the following sections to perform vector searches. The query vector is created using an embedding model from Azure OpenAI.
+
+
+## Create a single vector search
+
+The first example demonstrates a basic scenario where you want to find document descriptions that closely match the search string using the [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions).
+
+1. Create a `searchSingle.ts` file in the `src` directory.
+
+1. Copy the following code into the file.
+
+    :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/searchSingle.ts" :::
+
+    The vectorQuery contains the configuration of the vectorized query including the vectorized text of the query input as `vector`,  `fields` determines which vector fields are searched, and `kNearestNeighborsCount` specifies the number of nearest neighbors to return.
+
+    The vector query string is `quintessential lodging near running trails, eateries, retail`, which is vectorized into 1,536 embeddings for this query.
+
+1. Build and run the file:
+
+    ```console
+    npm run build && node -r dotenv/config dist/searchSingle.js
+    ```
+
+1. The output of this code shows the relevant docs for the query `quintessential lodging near running trails, eateries, retail`. 
+
+    ```console
+    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
+    Using index name: hotels-vector-quickstart-0627-4
+    
+    
+    Single Vector search found 5
+    - HotelId: 48, HotelName: Nordick's Valley Motel, Tags: ["continental breakfast","air conditioning","free wifi"], Score 0.6605852
+    - HotelId: 13, HotelName: Luxury Lion Resort, Tags: ["bar","concierge","restaurant"], Score 0.6333684
+    - HotelId: 4, HotelName: Sublime Palace Hotel, Tags: ["concierge","view","air conditioning"], Score 0.605672
+    - HotelId: 49, HotelName: Swirling Currents Hotel, Tags: ["air conditioning","laundry service","24-hour front desk service"], Score 0.6026341
+    - HotelId: 2, HotelName: Old Century Hotel, Tags: ["pool","free wifi","air conditioning","concierge"], Score 0.57902366
+    ```
+
+    The response for the vector equivalent of `quintessential lodging near running trails, eateries, retail` consists of 5 results with only the fields specified by the select returned.
+
+
+## Create a single vector search with a filter
+
+You can add filters, but the filters are applied to the nonvector content in your index. In this example, the filter applies to the `Tags` field to filter out any hotels that don't provide free Wi-Fi. This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
+
+1. Create a `searchSingleWithFilter.ts` file in the `src` directory.
+
+1. Copy the following code into the file.
+
+    :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/searchSingleWithFilter.ts" :::
+
+    Add the dependencies, environment variables, and the same search functionality as the previous search with a post-processing exclusion filter added for hotels with `free wifi`.
+
+1. Build and run the file:
+
+    ```console
+    npm run build && node -r dotenv/config dist/searchSingleWithFilter.js
+    ```
+1. The output of this code shows the relevant documents for the query with the filter for `free wifi` applied:
+
+    ```console
+    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
+    Using index name: hotels-vector-quickstart-0627-4
+    
+    
+    Single Vector search found 2
+    - HotelId: 48, HotelName: Nordick's Valley Motel, Tags: ["continental breakfast","air conditioning","free wifi"], Score 0.6605852
+    - HotelId: 2, HotelName: Old Century Hotel, Tags: ["pool","free wifi","air conditioning","concierge"], Score 0.57902366
+    ```
+
+## Create a search with a geospatial filter    
+
+You can specify a geospatial filter to limit results to a specific geographic area. In this example, the filter limits results to hotels within 300 kilometers of Washington D.C. (coordinates: `-77.03241 38.90166`). Geospatial distances are always in kilometers. This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
+
+1. Create a `searchSingleWithFilterGeo.ts` file in the `src` directory.
+
+1. Copy the following code into the file.
+
+    :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/searchSingleWithFilterGeo.ts" :::
+1. Build and run the file:
+
+    ```console
+    npm run build && node -r dotenv/config dist/searchSingleWithFilterGeo.js
+    ```
+
+1. The output of this code shows the relevant documents for the query with the geospatial post-processing exclusion filter applied:
+
+    ```console
+    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
+    Using index name: hotels-vector-quickstart-0627-4
+    
+    
+    Single Vector search found 2
+    - HotelId: 48, HotelName: Nordick's Valley Motel, Tags: N/A, Score 0.6605852246284485
+    - HotelId: 49, HotelName: Swirling Currents Hotel, Tags: N/A, Score 0.602634072303772
+    ```
+
+
+## Create a hybrid search
+
+Hybrid search consists of keyword queries and vector queries in a single search request. This example runs the vector query and full-text search concurrently:
+
+- **Search string**: `historic hotel walk to restaurants and shopping`
+- **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
+
+This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
+
+1. Create a `searchHybrid.ts` file in the `src` directory.
+1. Copy the following code into the file.
+
+    :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/searchHybrid.ts" :::
+1. Build and run the file:
+
+    ```console
+    npm run build && node -r dotenv/config dist/searchHybrid.js
+    ```
+1. The output of this code shows the relevant documents for the hybrid search:
+
+    ```console
+    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
+    Using index name: hotels-vector-quickstart-0627-4
+    
+    
+    Hybrid search found 7 then limited to top 5
+    - Score: 0.03279569745063782
+      HotelId: 4
+      HotelName: Sublime Palace Hotel
+      Description: Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.
+      Category: Boutique
+      Tags: ["concierge","view","air conditioning"]
+    
+    - Score: 0.032522473484277725
+      HotelId: 13
+      HotelName: Luxury Lion Resort
+      Description: Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort.
+      Category: Luxury
+      Tags: ["bar","concierge","restaurant"]
+    
+    - Score: 0.03205128386616707
+      HotelId: 48
+      HotelName: Nordick's Valley Motel
+      Description: Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.
+      Category: Boutique
+      Tags: ["continental breakfast","air conditioning","free wifi"]
+    
+    - Score: 0.0317460335791111
+      HotelId: 49
+      HotelName: Swirling Currents Hotel
+      Description: Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary W-Fi and flat-screen TVs.
+      Category: Suite
+      Tags: ["air conditioning","laundry service","24-hour front desk service"]
+    
+    - Score: 0.03125
+      HotelId: 2
+      HotelName: Old Century Hotel
+      Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
+      Category: Boutique
+      Tags: ["pool","free wifi","air conditioning","concierge"]
+    ```
+
+    Because Reciprocal Rank Fusion (RRF) merges results, it helps to review the inputs. The following results are from only the full-text query. The top two results are Sublime Palace Hotel and History Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
+
+    ```json
+       {
+           "@search.score": 2.2626662,
+           "HotelName": "Sublime Palace Hotel",
+           "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace."
+       },
+       {
+           "@search.score": 0.86421645,
+           "HotelName": "Luxury Lion Resort",
+           "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort"
+       },
+    ```
+
+    In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to fourth position. Historic Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
+   
+   ```json
+   "value": [
+       {
+           "@search.score": 0.857736,
+           "HotelId": "48",
+           "HotelName": "Nordick's Valley Motel",
+           "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
+           "Category": "Boutique"
+       },
+       {
+           "@search.score": 0.8399129,
+           "HotelId": "49",
+           "HotelName": "Swirling Currents Hotel",
+           "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center.",
+           "Category": "Luxury"
+       },
+       {
+           "@search.score": 0.8383954,
+           "HotelId": "13",
+           "HotelName": "Luxury Lion Resort",
+           "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort",
+           "Category": "Resort and Spa"
+       },
+       {
+           "@search.score": 0.8254346,
+           "HotelId": "4",
+           "HotelName": "Sublime Palace Hotel",
+           "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.",
+           "Category": "Boutique"
+       },
+       {
+           "@search.score": 0.82380056,
+           "HotelId": "1",
+           "HotelName": "Stay-Kay City Hotel",
+           "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York.",
+           "Category": "Boutique"
+       },
+       {
+           "@search.score": 0.81514084,
+           "HotelId": "2",
+           "HotelName": "Old Century Hotel",
+           "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
+           "Category": "Boutique"
+       },
+       {
+           "@search.score": 0.8133763,
+           "HotelId": "3",
+           "HotelName": "Gastronomic Landscape Hotel",
+           "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
+           "Category": "Resort and Spa"
+       }
+   ]
+   ```
+
+## Create a semantic hybrid search
+
+Here's the last query in the collection to create extend the semantic hybrid search with the additional search text `historic hotel walk to restaurants and shopping`.
+
+This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
+
+1. Create a `searchSemanticHybrid.ts` file in the `src` directory.
+1. Copy the following code into the file.
+
+    :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/searchSemanticHybrid.ts" :::
+
+1. Build and run the file:
+
+    ```console
+    npm run build && node -r dotenv/config dist/searchSemanticHybrid.js
+    ```
+
+1. The output of this code shows the relevant documents for the semantic hybrid search:
+
+    ```console
+    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
+    Using index name: hotels-vector-quickstart-0627-4
+
+    
+    Semantic hybrid search found 7 then limited to top 5
+    - Score: 0.0317460335791111
+      Re-ranker Score: 2.6550590991973877
+      HotelId: 49
+      HotelName: Swirling Currents Hotel
+      Description: Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary W-Fi and flat-screen TVs.
+      Category: Suite
+    
+    - Score: 0.03279569745063782
+      Re-ranker Score: 2.599761724472046
+      HotelId: 4
+      HotelName: Sublime Palace Hotel
+      Description: Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.
+      Category: Boutique
+    
+    - Score: 0.03125
+      Re-ranker Score: 2.3480887413024902
+      HotelId: 2
+      HotelName: Old Century Hotel
+      Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
+      Category: Boutique
+    
+    - Score: 0.016393441706895828
+      Re-ranker Score: 2.2718777656555176
+      HotelId: 1
+      HotelName: Stay-Kay City Hotel
+      Description: This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.
+      Category: Boutique
+    
+    - Score: 0.01515151560306549
+      Re-ranker Score: 2.0582215785980225
+      HotelId: 3
+      HotelName: Gastronomic Landscape Hotel
+      Description: The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.
+      Category: Suite
+    ```
+
+    You can think of the semantic ranking as a way to improve the relevance of search results by understanding the meaning behind the words in the query and the content of the documents. In this case, the semantic ranking helps to identify hotels that are not only relevant to the keywords but also match the intent of the query:
+
+    Key takeaways: 
+
+    - Vector search is specified through the `vectorSearchOptions` property. Keyword search is specified through the `semanticSearchOptions` property.
+
+    - In a hybrid search, you can integrate vector search with full-text search over keywords. Filters, spell check, and semantic ranking apply to textual content only, and not vectors. In this final query, there's no semantic `answer` because the system didn't produce one that was sufficiently strong.
+
+    - Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
+
+## Clean up
+
+When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
+
+You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
+
+If you want to keep the search service, but delete the index and documents, you can delete the index programmatically.
+
+1. Create a `deleteIndex.ts` file in the `src` directory.
+1. Add the dependencies, environment variables, and code to delete the index.
+
+    :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/deleteIndex.ts" :::
+1. Build and run the file:
+
+    ```console
+    npm run build && node -r dotenv/config dist/deleteIndex.js
+    ```
+
+## Next steps
+
+- Review the repository of code samples for vector search capabilities in Azure AI Search for [JavaScript](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "TypeScriptを使用したAzure AI検索用ベクタークイックスタートの追加"
}
```

### Explanation
この変更は、TypeScriptを使用してAzure AI検索のベクター機能を実装するためのクイックスタートガイドを追加するものです。この新しいファイルは、ベクターの作成、データのロード、クエリの実行方法を詳しく説明しています。

具体的には、以下の内容が含まれています：
- AzureアカウントとAzure AI Searchサービスの設定要件。
- Visual Studio Codeを用いたTypeScriptプロジェクトのセットアップ手順。
- Azure AI Searchクライアントライブラリを利用してベクターインデックスを作成し、文書をインデックスにアップロードする手順。
- ベクタークエリを使用して検索を実行する例を含む、ハイブリッド検索を取り扱うセクション。

このガイドの目的は、開発者がAzure AI検索サービスを利用して、意味に基づいた類似検索を行う方法を学ぶことを助けることです。サンプルコードを通して、コードの例やエラー処理、環境変数の管理など、実際のアプリケーション開発に役立つ情報が提供されます。これにより、TypeScriptにおけるAzure AI検索機能の利用が容易になり、開発者は効果的にその機能を活用できるようになります。

## articles/search/search-get-started-vector.md{#item-4984d9}

<details>
<summary>Diff</summary>
````diff
@@ -20,6 +20,18 @@ zone_pivot_groups: search-get-started-vector-search
 
 ::: zone-end
 
+::: zone pivot="javascript"
+
+[!INCLUDE [JavaScript quickstart](includes/quickstarts/search-get-started-vector-javascript.md)]
+
+::: zone-end
+
+::: zone pivot="typescript"
+
+[!INCLUDE [TypeScript quickstart](includes/quickstarts/search-get-started-vector-typescript.md)]
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
    "modification_title": "ベクター検索のクイックスタートにJavaScriptおよびTypeScriptのセクションを追加"
}
```

### Explanation
この変更は、Azure AI検索に関する「ベクター検索のクイックスタート」ドキュメントにJavaScriptおよびTypeScriptに関するセクションを追加したものです。具体的には、JavaScriptとTypeScriptのクイックスタートガイドへのリンクを含む新しいコンテンツが、既存のRESTクイックスタートガイドのセクションと並べて挿入されました。

この追加により、以下のことが可能になります：
- ユーザーは、JavaScriptやTypeScriptを使用してAzure AI検索のベクター機能をスムーズに利用するための具体的な手順やサンプルコードにアクセスできます。
- 各プログラミング言語に特化したクイックスタートガイドが整備され、ユーザーのニーズに応じた情報を得やすくなります。

これにより、開発者は自分のプロジェクトに最適な技術スタックを選ぶ際の参考になり、Azure AI検索の利便性が向上します。


