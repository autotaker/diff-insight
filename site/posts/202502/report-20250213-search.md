---
date: '2025-02-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:be5df78...MicrosoftDocs:81f79a9
summary: この一連の変更は、C#、Java、JavaScript、Python、TypeScript などのプログラミング言語での全体テキスト検索のクイックスタートガイドに対するマイナーなアップデートを含んでいます。主な内容は日付や内容の明確化、Microsoft
  Entra ID による推奨の非キー認証の追加、ソースコードやリソース認証情報の追加です。また、「リソース認証」に関する新しいガイドが追加されています。全体として、これらの更新はユーザーの体験とセキュリティを向上させることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:be5df78...MicrosoftDocs:81f79a9){target="_blank"}

# ハイライト

この一連の変更は、C#、Java、JavaScript、Python、TypeScript などのプログラミング言語での全体テキスト検索のクイックスタートガイドに対するマイナーなアップデートを含んでいます。主に日付や内容の明確化、Microsoft Entra ID による推奨の非キー認証、ソースコードや前提条件、リソース認証情報の追加です。また、新たに「リソース認証」に関するガイドが追加されています。

## 新機能

- 「リソース認証」ドキュメントが新規追加されました。これは、Azure AI Searchサービスとアプリケーションの認証方法を詳細に説明しています。

## 破壊的変更

- 特にありません。どの変更点も既存の構成を壊すものではありません。

## その他の更新

- クイックスタートガイド全体で日付が最新の情報に更新されています。
- C#、Java、JavaScript、Python、TypeScript などの言語ごとに、Microsoft Entra ID による認証およびリソース情報の取得手順の項目が明確化。
- 地域サポートの表記が改訂され、文言の一貫性と可読性が向上しました。

# インサイト

Azure AI Search のクイックスタートガイド群の更新は、ユーザー体験とセキュリティ面での強化を目的としています。プログラミング言語ごとに詳細な手順やコードサンプルが提供され、開発者が迅速にプロジェクトを開始しやすくなるよう設計されています。

特に、Microsoft Entra ID を用いた非キー認証の推奨は、セキュアな開発を行う上で重要なポイントです。これは、静的なキーによるアクセス制限を設けず、より動的で安全な認証方法を提供するものです。このアプローチは、API キーの管理の負担を軽減すると同時に、開発者が Azure 環境でより安全に作業できる環境を提供します。

さらに、リソース認証に関するドキュメントの追加は、新しい利用者だけでなく既存のユーザーにも役立つ重要なリファレンスとして機能します。このガイドにより、ユーザーは Azure 上でのリソース管理と認証方法を迅速かつ確実に把握できるようになっています。

全体として、この一連の更新と新機能追加は、Azure AI Search の利用をさらに強化し、ユーザーがより安心して作業を進められる環境作りに貢献しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [full-text-csharp.md](#item-2e943a) | minor update | C#での全体テキスト検索クイックスタートの更新 | modified | 766 | 311 | 1077 | 
| [full-text-intro.md](#item-f655a1) | minor update | 全体テキスト検索クイックスタートのイントロダクションの更新 | modified | 3 | 16 | 19 | 
| [full-text-java.md](#item-d659f9) | minor update | Javaでの全体テキスト検索クイックスタートの更新 | modified | 18 | 4 | 22 | 
| [full-text-javascript.md](#item-568e3a) | minor update | JavaScriptでの全体テキスト検索クイックスタートの更新 | modified | 17 | 3 | 20 | 
| [full-text-python.md](#item-9bba1c) | minor update | Pythonでの全体テキスト検索クイックスタートの更新 | modified | 17 | 3 | 20 | 
| [full-text-typescript.md](#item-6630e8) | minor update | TypeScriptでの全体テキスト検索クイックスタートの更新 | modified | 17 | 3 | 20 | 
| [resource-authentication.md](#item-381ff1) | new feature | リソース認証に関する新しいガイド | added | 33 | 0 | 33 | 
| [search-get-started-text.md](#item-935941) | minor update | クイックスタートガイドの日付更新 | modified | 1 | 1 | 2 | 
| [search-region-support.md](#item-25b0f1) | minor update | 地域サポートの表記修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/includes/quickstarts/full-text-csharp.md{#item-2e943a}

<details>
<summary>Diff</summary>
````diff
@@ -4,466 +4,921 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/8/2025
+ms.date: 2/12/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
 
-Build a console application using the [Azure.Search.Documents](/dotnet/api/overview/azure/search.documents-readme) client library to create, load, and query a search index.
+> [!TIP]
+> You can [download the source code](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/v11) to start with a finished project or follow these steps to create your own.
 
-Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/v11) to start with a finished project or follow these steps to create your own.
+## Prerequisites
 
-## Set up your environment
+- An active Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
+- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
 
-1. Start Visual Studio and create a new project for a console app.
+## Microsoft Entra ID prerequisites
 
-1. In **Tools** > **NuGet Package Manager**, select **Manage NuGet Packages for Solution...**.
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign both of the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
 
-1. Select **Browse**.
+## Retrieve resource information
 
-1. Search for [Azure.Search.Documents package](https://www.nuget.org/packages/Azure.Search.Documents/) and select version 11.0 or later.
+[!INCLUDE [resource authentication](../resource-authentication.md)]
 
-1. Select **Install** to add the assembly to your project and solution.
+## Set up
 
-## Create a search client
+1. Create a new folder `full-text-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-1. In *Program.cs*, change the namespace to `AzureSearch.SDK.Quickstart.v11` and then add the following `using` directives.
+    ```shell
+    mkdir full-text-quickstart && cd full-text-quickstart
+    ```
 
-   ```csharp
-   using Azure;
-   using Azure.Search.Documents;
-   using Azure.Search.Documents.Indexes;
-   using Azure.Search.Documents.Indexes.Models;
-   using Azure.Search.Documents.Models;
-   ```
+1. Create a new console application with the following command:
 
-1. Copy the following code to create two clients. [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient) creates the index, and [SearchClient](/dotnet/api/azure.search.documents.searchclient) loads and queries an existing index. Both need the service endpoint and an admin API key for authentication with create/delete rights.
+    ```shell
+    dotnet new console
+    ```
 
-   Because the code builds out the URI for you, specify just the search service name in the `serviceName` property.
+1. Install the Azure AI Search client library ([Azure.Search.Documents](/dotnet/api/overview/azure/search.documents-readme)) for .NET with:
 
-   ```csharp
-    static void Main(string[] args)
-    {
-        string serviceName = "<your-search-service-name>";
-        string apiKey = "<your-search-service-admin-api-key>";
-        string indexName = "hotels-quickstart";
-
-        // Create a SearchIndexClient to send create/delete index commands
-        Uri serviceEndpoint = new Uri($"https://{serviceName}.search.windows.net/");
-        AzureKeyCredential credential = new AzureKeyCredential(apiKey);
-        SearchIndexClient adminClient = new SearchIndexClient(serviceEndpoint, credential);
-
-        // Create a SearchClient to load and query documents
-        SearchClient srchclient = new SearchClient(serviceEndpoint, indexName, credential);
-        . . . 
-    }
+    ```console
+    dotnet add package Azure.Search.Documents
     ```
 
-## Create an index
+1. For the **recommended** keyless authentication with Microsoft Entra ID, install the [Azure.Identity](https://www.nuget.org/packages/Azure.Identity) package with:
 
-This quickstart builds a Hotels index that you'll load with hotel data and execute queries against. In this step, define the fields in the index. Each field definition includes a name, data type, and attributes that determine how the field is used.
+    ```console
+    dotnet add package Azure.Identity
+    ```
 
-In this example, synchronous methods of the *Azure.Search.Documents* library are used for simplicity and readability. However, for production scenarios, you should use asynchronous methods to keep your app scalable and responsive. For example, you would use [CreateIndexAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindexasync) instead of [CreateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindex).
+1. For the **recommended** keyless authentication with Microsoft Entra ID, sign in to Azure with the following command:
+
+    ```console
+    az login
+    ```
+
+## Create, load, and query a search index
+
+In the prior [set up](#set-up) section, you created a new console application and installed the Azure AI Search client library. 
+
+In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [explaining the code](#explaining-the-code) section.
 
-1. Add an empty class definition to your project: *Hotel.cs*
+The sample code in this quickstart uses Microsoft Entra ID for authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
 
-1. Copy the following code into *Hotel.cs* to define the structure of a hotel document. Attributes on the field determine how it's used in an application. For example, the `IsFilterable` attribute must be assigned to every field that supports a filter expression.
+#### [Microsoft Entra ID](#tab/keyless)
+
+```csharp
+Uri serviceEndpoint = new Uri($"https://<Put your search service NAME here>.search.windows.net/");
+DefaultAzureCredential credential = new();
+```
+
+#### [API key](#tab/api-key)
+
+```csharp
+Uri serviceEndpoint = new Uri($"https://<Put your search service NAME here>.search.windows.net/");
+AzureKeyCredential credential = new AzureKeyCredential("<Your search service admin key>");
+```
+---
+
+1. In *Program.cs*, paste the following code. Edit the `serviceName` and `apiKey` variables with your search service name and admin API key.
 
     ```csharp
     using System;
-    using System.Text.Json.Serialization;
+    using Azure;
+    using Azure.Identity;
+    using Azure.Search.Documents;
     using Azure.Search.Documents.Indexes;
     using Azure.Search.Documents.Indexes.Models;
+    using Azure.Search.Documents.Models;
+    
+    namespace AzureSearch.Quickstart
+    
+    {
+        class Program
+        {
+            static void Main(string[] args)
+            {    
+                // Your search service endpoint
+                Uri serviceEndpoint = new Uri($"https://<Put your search service NAME here>.search.windows.net/");
+    
+                // Use the recommended keyless credential instead of the AzureKeyCredential credential.
+                DefaultAzureCredential credential = new();
+                //AzureKeyCredential credential = new AzureKeyCredential("Your search service admin key");
+    
+                // Create a SearchIndexClient to send create/delete index commands
+                SearchIndexClient adminClient = new SearchIndexClient(serviceEndpoint, credential);
+    
+                // Create a SearchClient to load and query documents
+                string indexName = "hotels-quickstart";
+                SearchClient srchclient = new SearchClient(serviceEndpoint, indexName, credential);
+    
+                // Delete index if it exists
+                Console.WriteLine("{0}", "Deleting index...\n");
+                DeleteIndexIfExists(indexName, adminClient);
+    
+                // Create index
+                Console.WriteLine("{0}", "Creating index...\n");
+                CreateIndex(indexName, adminClient);
+    
+                SearchClient ingesterClient = adminClient.GetSearchClient(indexName);
+    
+                // Load documents
+                Console.WriteLine("{0}", "Uploading documents...\n");
+                UploadDocuments(ingesterClient);
+    
+                // Wait 2 secondsfor indexing to complete before starting queries (for demo and console-app purposes only)
+                Console.WriteLine("Waiting for indexing...\n");
+                System.Threading.Thread.Sleep(2000);
+    
+                // Call the RunQueries method to invoke a series of queries
+                Console.WriteLine("Starting queries...\n");
+                RunQueries(srchclient);
+    
+                // End the program
+                Console.WriteLine("{0}", "Complete. Press any key to end this program...\n");
+                Console.ReadKey();
+            }
+    
+            // Delete the hotels-quickstart index to reuse its name
+            private static void DeleteIndexIfExists(string indexName, SearchIndexClient adminClient)
+            {
+                adminClient.GetIndexNames();
+                {
+                    adminClient.DeleteIndex(indexName);
+                }
+            }
+            // Create hotels-quickstart index
+            private static void CreateIndex(string indexName, SearchIndexClient adminClient)
+            {
+                FieldBuilder fieldBuilder = new FieldBuilder();
+                var searchFields = fieldBuilder.Build(typeof(Hotel));
+    
+                var definition = new SearchIndex(indexName, searchFields);
+    
+                var suggester = new SearchSuggester("sg", new[] { "HotelName", "Category", "Address/City", "Address/StateProvince" });
+                definition.Suggesters.Add(suggester);
+    
+                adminClient.CreateOrUpdateIndex(definition);
+            }
+    
+            // Upload documents in a single Upload request.
+            private static void UploadDocuments(SearchClient searchClient)
+            {
+                IndexDocumentsBatch<Hotel> batch = IndexDocumentsBatch.Create(
+                    IndexDocumentsAction.Upload(
+                        new Hotel()
+                        {
+                            HotelId = "1",
+                            HotelName = "Secret Point Motel",
+                            Description = "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
+                            DescriptionFr = "L'hôtel est idéalement situé sur la principale artère commerciale de la ville en plein cœur de New York. A quelques minutes se trouve la place du temps et le centre historique de la ville, ainsi que d'autres lieux d'intérêt qui font de New York l'une des villes les plus attractives et cosmopolites de l'Amérique.",
+                            Category = "Boutique",
+                            Tags = new[] { "pool", "air conditioning", "concierge" },
+                            ParkingIncluded = false,
+                            LastRenovationDate = new DateTimeOffset(1970, 1, 18, 0, 0, 0, TimeSpan.Zero),
+                            Rating = 3.6,
+                            Address = new Address()
+                            {
+                                StreetAddress = "677 5th Ave",
+                                City = "New York",
+                                StateProvince = "NY",
+                                PostalCode = "10022",
+                                Country = "USA"
+                            }
+                        }),
+                    IndexDocumentsAction.Upload(
+                        new Hotel()
+                        {
+                            HotelId = "2",
+                            HotelName = "Twin Dome Motel",
+                            Description = "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
+                            DescriptionFr = "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
+                            Category = "Boutique",
+                            Tags = new[] { "pool", "free wifi", "concierge" },
+                            ParkingIncluded = false,
+                            LastRenovationDate = new DateTimeOffset(1979, 2, 18, 0, 0, 0, TimeSpan.Zero),
+                            Rating = 3.60,
+                            Address = new Address()
+                            {
+                                StreetAddress = "140 University Town Center Dr",
+                                City = "Sarasota",
+                                StateProvince = "FL",
+                                PostalCode = "34243",
+                                Country = "USA"
+                            }
+                        }),
+                    IndexDocumentsAction.Upload(
+                        new Hotel()
+                        {
+                            HotelId = "3",
+                            HotelName = "Triple Landscape Hotel",
+                            Description = "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
+                            DescriptionFr = "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
+                            Category = "Resort and Spa",
+                            Tags = new[] { "air conditioning", "bar", "continental breakfast" },
+                            ParkingIncluded = true,
+                            LastRenovationDate = new DateTimeOffset(2015, 9, 20, 0, 0, 0, TimeSpan.Zero),
+                            Rating = 4.80,
+                            Address = new Address()
+                            {
+                                StreetAddress = "3393 Peachtree Rd",
+                                City = "Atlanta",
+                                StateProvince = "GA",
+                                PostalCode = "30326",
+                                Country = "USA"
+                            }
+                        }),
+                    IndexDocumentsAction.Upload(
+                        new Hotel()
+                        {
+                            HotelId = "4",
+                            HotelName = "Sublime Cliff Hotel",
+                            Description = "Sublime Cliff Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 1800 palace.",
+                            DescriptionFr = "Le sublime Cliff Hotel est situé au coeur du centre historique de sublime dans un quartier extrêmement animé et vivant, à courte distance de marche des sites et monuments de la ville et est entouré par l'extraordinaire beauté des églises, des bâtiments, des commerces et Monuments. Sublime Cliff fait partie d'un Palace 1800 restauré avec amour.",
+                            Category = "Boutique",
+                            Tags = new[] { "concierge", "view", "24-hour front desk service" },
+                            ParkingIncluded = true,
+                            LastRenovationDate = new DateTimeOffset(1960, 2, 06, 0, 0, 0, TimeSpan.Zero),
+                            Rating = 4.60,
+                            Address = new Address()
+                            {
+                                StreetAddress = "7400 San Pedro Ave",
+                                City = "San Antonio",
+                                StateProvince = "TX",
+                                PostalCode = "78216",
+                                Country = "USA"
+                            }
+                        })
+                    );
+    
+                try
+                {
+                    IndexDocumentsResult result = searchClient.IndexDocuments(batch);
+                }
+                catch (Exception)
+                {
+                    // If for some reason any documents are dropped during indexing, you can compensate by delaying and
+                    // retrying. This simple demo just logs the failed document keys and continues.
+                    Console.WriteLine("Failed to index some of the documents: {0}");
+                }
+            }
+    
+            // Run queries, use WriteDocuments to print output
+            private static void RunQueries(SearchClient srchclient)
+            {
+                SearchOptions options;
+                SearchResults<Hotel> response;
+    
+                // Query 1
+                Console.WriteLine("Query #1: Search on empty term '*' to return all documents, showing a subset of fields...\n");
+    
+                options = new SearchOptions()
+                {
+                    IncludeTotalCount = true,
+                    Filter = "",
+                    OrderBy = { "" }
+                };
+    
+                options.Select.Add("HotelId");
+                options.Select.Add("HotelName");
+                options.Select.Add("Rating");
+    
+                response = srchclient.Search<Hotel>("*", options);
+                WriteDocuments(response);
+    
+                // Query 2
+                Console.WriteLine("Query #2: Search on 'hotels', filter on 'Rating gt 4', sort by Rating in descending order...\n");
+    
+                options = new SearchOptions()
+                {
+                    Filter = "Rating gt 4",
+                    OrderBy = { "Rating desc" }
+                };
+    
+                options.Select.Add("HotelId");
+                options.Select.Add("HotelName");
+                options.Select.Add("Rating");
+    
+                response = srchclient.Search<Hotel>("hotels", options);
+                WriteDocuments(response);
+    
+                // Query 3
+                Console.WriteLine("Query #3: Limit search to specific fields (pool in Tags field)...\n");
+    
+                options = new SearchOptions()
+                {
+                    SearchFields = { "Tags" }
+                };
+    
+                options.Select.Add("HotelId");
+                options.Select.Add("HotelName");
+                options.Select.Add("Tags");
+    
+                response = srchclient.Search<Hotel>("pool", options);
+                WriteDocuments(response);
+    
+                // Query 4 - Use Facets to return a faceted navigation structure for a given query
+                // Filters are typically used with facets to narrow results on OnClick events
+                Console.WriteLine("Query #4: Facet on 'Category'...\n");
+    
+                options = new SearchOptions()
+                {
+                    Filter = ""
+                };
+    
+                options.Facets.Add("Category");
+    
+                options.Select.Add("HotelId");
+                options.Select.Add("HotelName");
+                options.Select.Add("Category");
+    
+                response = srchclient.Search<Hotel>("*", options);
+                WriteDocuments(response);
+    
+                // Query 5
+                Console.WriteLine("Query #5: Look up a specific document...\n");
+    
+                Response<Hotel> lookupResponse;
+                lookupResponse = srchclient.GetDocument<Hotel>("3");
+    
+                Console.WriteLine(lookupResponse.Value.HotelId);
+    
+    
+                // Query 6
+                Console.WriteLine("Query #6: Call Autocomplete on HotelName...\n");
+    
+                var autoresponse = srchclient.Autocomplete("sa", "sg");
+                WriteDocuments(autoresponse);
+    
+            }
+    
+            // Write search results to console
+            private static void WriteDocuments(SearchResults<Hotel> searchResults)
+            {
+                foreach (SearchResult<Hotel> result in searchResults.GetResults())
+                {
+                    Console.WriteLine(result.Document);
+                }
+    
+                Console.WriteLine();
+            }
+    
+            private static void WriteDocuments(AutocompleteResults autoResults)
+            {
+                foreach (AutocompleteItem result in autoResults.Results)
+                {
+                    Console.WriteLine(result.Text);
+                }
+    
+                Console.WriteLine();
+            }
+        }
+    }
+    ```
+
+1. In the same folder, create a new file named *Hotel.cs* and paste the following code. This code defines the structure of a hotel document. 
 
+    ```csharp
+    using System;
+    using System.Text.Json.Serialization;
+    using Azure.Search.Documents.Indexes;
+    using Azure.Search.Documents.Indexes.Models;
+    
     namespace AzureSearch.Quickstart
     {
         public partial class Hotel
         {
             [SimpleField(IsKey = true, IsFilterable = true)]
             public string HotelId { get; set; }
-
+    
             [SearchableField(IsSortable = true)]
             public string HotelName { get; set; }
-
+    
             [SearchableField(AnalyzerName = LexicalAnalyzerName.Values.EnLucene)]
             public string Description { get; set; }
-
+    
             [SearchableField(AnalyzerName = LexicalAnalyzerName.Values.FrLucene)]
             [JsonPropertyName("Description_fr")]
             public string DescriptionFr { get; set; }
-
+    
             [SearchableField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
             public string Category { get; set; }
-
+    
             [SearchableField(IsFilterable = true, IsFacetable = true)]
             public string[] Tags { get; set; }
-
+    
             [SimpleField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
             public bool? ParkingIncluded { get; set; }
-
+    
             [SimpleField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
             public DateTimeOffset? LastRenovationDate { get; set; }
-
+    
             [SimpleField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
             public double? Rating { get; set; }
-
+    
             [SearchableField]
             public Address Address { get; set; }
         }
     }
     ```
 
-   In the *Azure.Search.Documents* client library, you can use [SearchableField](/dotnet/api/azure.search.documents.indexes.models.searchablefield) and [SimpleField](/dotnet/api/azure.search.documents.indexes.models.simplefield) to streamline field definitions. Both are derivatives of a [SearchField](/dotnet/api/azure.search.documents.indexes.models.searchfield) and can potentially simplify your code:
-
-   + `SimpleField` can be any data type, is always non-searchable (it's ignored for full text search queries), and is retrievable (it's not hidden). Other attributes are off by default, but can be enabled. You might use a `SimpleField` for document IDs or fields used only in filters, facets, or scoring profiles. If so, be sure to apply any attributes that are necessary for the scenario, such as `IsKey = true` for a document ID. For more information, see [SimpleFieldAttribute.cs](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/src/Indexes/SimpleFieldAttribute.cs) in source code.
+1. Create a new file named *Hotel.cs* and paste the following code to define the structure of a hotel document. Attributes on the field determine how it's used in an application. For example, the `IsFilterable` attribute must be assigned to every field that supports a filter expression.
 
-   + `SearchableField` must be a string, and is always searchable and retrievable. Other attributes are off by default, but can be enabled. Because this field type is searchable, it supports synonyms and the full complement of analyzer properties. For more information, see the [SearchableFieldAttribute.cs](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/src/Indexes/SearchableFieldAttribute.cs) in source code.
-
-   Whether you use the basic `SearchField` API or either one of the helper models, you must explicitly enable filter, facet, and sort attributes. For example, [IsFilterable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfilterable), [IsSortable](/dotnet/api/azure.search.documents.indexes.models.searchfield.issortable), and [IsFacetable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfacetable) must be explicitly attributed, as shown in the previous sample.
-
-1. Add a second empty class definition to your project: *Address.cs*. Copy the following code into the class.
+    ```csharp
+    using System;
+    using System.Text.Json.Serialization;
+    using Azure.Search.Documents.Indexes;
+    using Azure.Search.Documents.Indexes.Models;
+    
+    namespace AzureSearch.Quickstart
+    {
+        public partial class Hotel
+        {
+            [SimpleField(IsKey = true, IsFilterable = true)]
+            public string HotelId { get; set; }
+    
+            [SearchableField(IsSortable = true)]
+            public string HotelName { get; set; }
+    
+            [SearchableField(AnalyzerName = LexicalAnalyzerName.Values.EnLucene)]
+            public string Description { get; set; }
+    
+            [SearchableField(AnalyzerName = LexicalAnalyzerName.Values.FrLucene)]
+            [JsonPropertyName("Description_fr")]
+            public string DescriptionFr { get; set; }
+    
+            [SearchableField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
+            public string Category { get; set; }
+    
+            [SearchableField(IsFilterable = true, IsFacetable = true)]
+            public string[] Tags { get; set; }
+    
+            [SimpleField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
+            public bool? ParkingIncluded { get; set; }
+    
+            [SimpleField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
+            public DateTimeOffset? LastRenovationDate { get; set; }
+    
+            [SimpleField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
+            public double? Rating { get; set; }
+    
+            [SearchableField]
+            public Address Address { get; set; }
+        }
+    }
+    ```
 
-   ```csharp
-   using Azure.Search.Documents.Indexes;
+1. Create a new file named *Address.cs* and paste the following code to define the structure of an address document.
 
+    ```csharp
+    using Azure.Search.Documents.Indexes;
+    
     namespace AzureSearch.Quickstart
     {
         public partial class Address
         {
             [SearchableField(IsFilterable = true)]
             public string StreetAddress { get; set; }
-
+    
             [SearchableField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
             public string City { get; set; }
-
+    
             [SearchableField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
             public string StateProvince { get; set; }
-
+    
             [SearchableField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
             public string PostalCode { get; set; }
-
+    
             [SearchableField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
             public string Country { get; set; }
         }
     }
-   ```
+    ```
 
-1. Create two more classes: *Hotel.Methods.cs* and *Address.Methods.cs* for `ToString()` overrides. These classes are used to render search results in the console output. The contents of these classes aren't provided in this article, but you can copy the code from [files in GitHub](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/v11/AzureSearchQuickstart-v11).
+1. Create a new file named *Hotel.Methods.cs* and paste the following code to define a `ToString()` override for the `Hotel` class. 
+
+    ```csharp
+    using System;
+    using System.Text;
+    
+    namespace AzureSearch.Quickstart
+    {
+        public partial class Hotel
+        {
+            public override string ToString()
+            {
+                var builder = new StringBuilder();
+    
+                if (!String.IsNullOrEmpty(HotelId))
+                {
+                    builder.AppendFormat("HotelId: {0}\n", HotelId);
+                }
+    
+                if (!String.IsNullOrEmpty(HotelName))
+                {
+                    builder.AppendFormat("Name: {0}\n", HotelName);
+                }
+    
+                if (!String.IsNullOrEmpty(Description))
+                {
+                    builder.AppendFormat("Description: {0}\n", Description);
+                }
+    
+                if (!String.IsNullOrEmpty(DescriptionFr))
+                {
+                    builder.AppendFormat("Description (French): {0}\n", DescriptionFr);
+                }
+    
+                if (!String.IsNullOrEmpty(Category))
+                {
+                    builder.AppendFormat("Category: {0}\n", Category);
+                }
+    
+                if (Tags != null && Tags.Length > 0)
+                {
+                    builder.AppendFormat("Tags: [ {0} ]\n", String.Join(", ", Tags));
+                }
+    
+                if (ParkingIncluded.HasValue)
+                {
+                    builder.AppendFormat("Parking included: {0}\n", ParkingIncluded.Value ? "yes" : "no");
+                }
+    
+                if (LastRenovationDate.HasValue)
+                {
+                    builder.AppendFormat("Last renovated on: {0}\n", LastRenovationDate);
+                }
+    
+                if (Rating.HasValue)
+                {
+                    builder.AppendFormat("Rating: {0}\n", Rating);
+                }
+    
+                if (Address != null && !Address.IsEmpty)
+                {
+                    builder.AppendFormat("Address: \n{0}\n", Address.ToString());
+                }
+    
+                return builder.ToString();
+            }
+        }
+    }
+    ```
 
-1. In *Program.cs*, create a [SearchIndex](/dotnet/api/azure.search.documents.indexes.models.searchindex) object, and then call the [CreateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindex) method to express the index in your search service. The index also includes a [SearchSuggester](/dotnet/api/azure.search.documents.indexes.models.searchsuggester) to enable autocomplete on the specified fields.
+1. Create a new file named *Address.Methods.cs* and paste the following code to define a `ToString()` override for the `Address` class.
 
-   ```csharp
-    // Create hotels-quickstart index
-    private static void CreateIndex(string indexName, SearchIndexClient adminClient)
+    ```csharp
+    using System;
+    using System.Text;
+    using System.Text.Json.Serialization;
+    
+    namespace AzureSearch.Quickstart
     {
-        FieldBuilder fieldBuilder = new FieldBuilder();
-        var searchFields = fieldBuilder.Build(typeof(Hotel));
+        public partial class Address
+        {
+            public override string ToString()
+            {
+                var builder = new StringBuilder();
+    
+                if (!IsEmpty)
+                {
+                    builder.AppendFormat("{0}\n{1}, {2} {3}\n{4}", StreetAddress, City, StateProvince, PostalCode, Country);
+                }
+    
+                return builder.ToString();
+            }
+    
+            [JsonIgnore]
+            public bool IsEmpty => String.IsNullOrEmpty(StreetAddress) &&
+                                   String.IsNullOrEmpty(City) &&
+                                   String.IsNullOrEmpty(StateProvince) &&
+                                   String.IsNullOrEmpty(PostalCode) &&
+                                   String.IsNullOrEmpty(Country);
+        }
+    }
+    ```
 
-        var definition = new SearchIndex(indexName, searchFields);
+1. Build and run the application with the following command:
 
-        var suggester = new SearchSuggester("sg", new[] { "HotelName", "Category", "Address/City", "Address/StateProvince" });
-        definition.Suggesters.Add(suggester);
+    ```shell
+    dotnet run
+    ```
 
-        adminClient.CreateOrUpdateIndex(definition);
-    }
-   ```
+Output includes messages from [Console.WriteLine](/dotnet/api/system.console.writeline), with the addition of query information and results.
+
+
+## Explaining the code
+
+In the previous sections, you created a new console application and installed the Azure AI Search client library. You added code to create a search index, load it with documents, and run queries. You ran the program to see the results in the console. 
+
+In this section, we explain the code you added to the console application.
+
+### Create a search client
+
+In *Program.cs*, you created two clients:
+- [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient) creates the index.
+- [SearchClient](/dotnet/api/azure.search.documents.searchclient) loads and queries an existing index. 
+
+Both clients need the search service endpoint and credentials described previously in the [resource information](#retrieve-resource-information) section.
+
+The sample code in this quickstart uses Microsoft Entra ID for authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
+
+#### [Microsoft Entra ID](#tab/keyless)
+
+```csharp
+Uri serviceEndpoint = new Uri($"https://<Put your search service NAME here>.search.windows.net/");
+DefaultAzureCredential credential = new();
+```
+
+#### [API key](#tab/api-key)
+
+```csharp
+Uri serviceEndpoint = new Uri($"https://<Put your search service NAME here>.search.windows.net/");
+AzureKeyCredential credential = new AzureKeyCredential("<Your search service admin key>");
+```
+---
+
+```csharp
+static void Main(string[] args)
+{
+    // Your search service endpoint
+    Uri serviceEndpoint = new Uri($"https://<Put your search service NAME here>.search.windows.net/");
+
+    // Use the recommended keyless credential instead of the AzureKeyCredential credential.
+    DefaultAzureCredential credential = new();
+    //AzureKeyCredential credential = new AzureKeyCredential("Your search service admin key");
+
+    // Create a SearchIndexClient to send create/delete index commands
+    SearchIndexClient adminClient = new SearchIndexClient(serviceEndpoint, credential);
+
+    // Create a SearchClient to load and query documents
+    string indexName = "hotels-quickstart";
+    SearchClient srchclient = new SearchClient(serviceEndpoint, indexName, credential);
+    
+    // REDACTED FOR BREVITY . . . 
+}
+```
+
+### Create an index
+
+This quickstart builds a Hotels index that you load with hotel data and execute queries against. In this step, you define the fields in the index. Each field definition includes a name, data type, and attributes that determine how the field is used.
+
+In this example, synchronous methods of the *Azure.Search.Documents* library are used for simplicity and readability. However, for production scenarios, you should use asynchronous methods to keep your app scalable and responsive. For example, you would use [CreateIndexAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindexasync) instead of [CreateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindex).
+
+#### Define the structures
+
+You created two helper classes, *Hotel.cs* and *Address.cs*, to define the structure of a hotel document and its address. The `Hotel` class includes fields for a hotel ID, name, description, category, tags, parking, renovation date, rating, and address. The `Address` class includes fields for street address, city, state/province, postal code, and country/region.
+
+In the *Azure.Search.Documents* client library, you can use [SearchableField](/dotnet/api/azure.search.documents.indexes.models.searchablefield) and [SimpleField](/dotnet/api/azure.search.documents.indexes.models.simplefield) to streamline field definitions. Both are derivatives of a [SearchField](/dotnet/api/azure.search.documents.indexes.models.searchfield) and can potentially simplify your code:
+
++ `SimpleField` can be any data type, is always non-searchable (ignored for full text search queries), and is retrievable (not hidden). Other attributes are off by default, but can be enabled. You might use a `SimpleField` for document IDs or fields used only in filters, facets, or scoring profiles. If so, be sure to apply any attributes that are necessary for the scenario, such as `IsKey = true` for a document ID. For more information, see [SimpleFieldAttribute.cs](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/src/Indexes/SimpleFieldAttribute.cs) in source code.
+
++ `SearchableField` must be a string, and is always searchable and retrievable. Other attributes are off by default, but can be enabled. Because this field type is searchable, it supports synonyms and the full complement of analyzer properties. For more information, see the [SearchableFieldAttribute.cs](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/src/Indexes/SearchableFieldAttribute.cs) in source code.
 
-## Load documents
+Whether you use the basic `SearchField` API or either one of the helper models, you must explicitly enable filter, facet, and sort attributes. For example, [IsFilterable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfilterable), [IsSortable](/dotnet/api/azure.search.documents.indexes.models.searchfield.issortable), and [IsFacetable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfacetable) must be explicitly attributed, as shown in the previous sample.
 
-Azure AI Search searches over content stored in the service. In this step, you'll load JSON documents that conform to the hotel index you just created.
+#### Create the search index
+
+In *Program.cs*, you create a [SearchIndex](/dotnet/api/azure.search.documents.indexes.models.searchindex) object, and then call the [CreateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindex) method to express the index in your search service. The index also includes a [SearchSuggester](/dotnet/api/azure.search.documents.indexes.models.searchsuggester) to enable autocomplete on the specified fields.
+
+```csharp
+// Create hotels-quickstart index
+private static void CreateIndex(string indexName, SearchIndexClient adminClient)
+{
+    FieldBuilder fieldBuilder = new FieldBuilder();
+    var searchFields = fieldBuilder.Build(typeof(Hotel));
+
+    var definition = new SearchIndex(indexName, searchFields);
+
+    var suggester = new SearchSuggester("sg", new[] { "HotelName", "Category", "Address/City", "Address/StateProvince" });
+    definition.Suggesters.Add(suggester);
+
+    adminClient.CreateOrUpdateIndex(definition);
+}
+```
+
+### Load documents
+
+Azure AI Search searches over content stored in the service. In this step, you load JSON documents that conform to the hotel index you created.
 
 In Azure AI Search, search documents are data structures that are both inputs to indexing and outputs from queries. As obtained from an external data source, document inputs might be rows in a database, blobs in Blob storage, or JSON documents on disk. In this example, we're taking a shortcut and embedding JSON documents for four hotels in the code itself.
 
 When uploading documents, you must use an [IndexDocumentsBatch](/dotnet/api/azure.search.documents.models.indexdocumentsbatch-1) object. An `IndexDocumentsBatch` object contains a collection of [Actions](/dotnet/api/azure.search.documents.models.indexdocumentsbatch-1.actions), each of which contains a document and a property telling Azure AI Search what action to perform ([upload, merge, delete, and mergeOrUpload](/azure/search/search-what-is-data-import#indexing-actions)).
 
-1. In *Program.cs*, create an array of documents and index actions, and then pass the array to `IndexDocumentsBatch`. The following documents conform to the hotels-quickstart index, as defined by the hotel class.
-
-    ```csharp
-    // Upload documents in a single Upload request.
-    private static void UploadDocuments(SearchClient searchClient)
-    {
-        IndexDocumentsBatch<Hotel> batch = IndexDocumentsBatch.Create(
-            IndexDocumentsAction.Upload(
-                new Hotel()
-                {
-                    HotelId = "1",
-                    HotelName = "Stay-Kay City Hotel",
-                    Description = "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
-                    DescriptionFr = "L'hôtel est idéalement situé sur la principale artère commerciale de la ville en plein cœur de New York. A quelques minutes se trouve la place du temps et le centre historique de la ville, ainsi que d'autres lieux d'intérêt qui font de New York l'une des villes les plus attractives et cosmopolites de l'Amérique.",
-                    Category = "Boutique",
-                    Tags = new[] { "pool", "air conditioning", "concierge" },
-                    ParkingIncluded = false,
-                    LastRenovationDate = new DateTimeOffset(1970, 1, 18, 0, 0, 0, TimeSpan.Zero),
-                    Rating = 3.6,
-                    Address = new Address()
-                    {
-                        StreetAddress = "677 5th Ave",
-                        City = "New York",
-                        StateProvince = "NY",
-                        PostalCode = "10022",
-                        Country = "USA"
-                    }
-                }),
-            IndexDocumentsAction.Upload(
-                new Hotel()
-                {
-                    HotelId = "2",
-                    HotelName = "Old Century Hotel",
-                    Description = "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
-                    DescriptionFr = "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
-                    Category = "Boutique",
-                    Tags = new[] { "pool", "free wifi", "concierge" },
-                    ParkingIncluded = false,
-                    LastRenovationDate = new DateTimeOffset(1979, 2, 18, 0, 0, 0, TimeSpan.Zero),
-                    Rating = 3.60,
-                    Address = new Address()
-                    {
-                        StreetAddress = "140 University Town Center Dr",
-                        City = "Sarasota",
-                        StateProvince = "FL",
-                        PostalCode = "34243",
-                        Country = "USA"
-                    }
-                }),
-            IndexDocumentsAction.Upload(
-                new Hotel()
-                {
-                    HotelId = "3",
-                    HotelName = "Gastronomic Landscape Hotel",
-                    Description = "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
-                    DescriptionFr = "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
-                    Category = "Resort and Spa",
-                    Tags = new[] { "air conditioning", "bar", "continental breakfast" },
-                    ParkingIncluded = true,
-                    LastRenovationDate = new DateTimeOffset(2015, 9, 20, 0, 0, 0, TimeSpan.Zero),
-                    Rating = 4.80,
-                    Address = new Address()
-                    {
-                        StreetAddress = "3393 Peachtree Rd",
-                        City = "Atlanta",
-                        StateProvince = "GA",
-                        PostalCode = "30326",
-                        Country = "USA"
-                    }
-                }),
-            IndexDocumentsAction.Upload(
-                new Hotel()
+In *Program.cs*, you create an array of documents and index actions, and then pass the array to `IndexDocumentsBatch`. The following documents conform to the hotels-quickstart index, as defined by the hotel class.
+
+```csharp
+// Upload documents in a single Upload request.
+private static void UploadDocuments(SearchClient searchClient)
+{
+    IndexDocumentsBatch<Hotel> batch = IndexDocumentsBatch.Create(
+        IndexDocumentsAction.Upload(
+            new Hotel()
+            {
+                HotelId = "1",
+                HotelName = "Stay-Kay City Hotel",
+                Description = "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
+                DescriptionFr = "L'hôtel est idéalement situé sur la principale artère commerciale de la ville en plein cœur de New York. A quelques minutes se trouve la place du temps et le centre historique de la ville, ainsi que d'autres lieux d'intérêt qui font de New York l'une des villes les plus attractives et cosmopolites de l'Amérique.",
+                Category = "Boutique",
+                Tags = new[] { "pool", "air conditioning", "concierge" },
+                ParkingIncluded = false,
+                LastRenovationDate = new DateTimeOffset(1970, 1, 18, 0, 0, 0, TimeSpan.Zero),
+                Rating = 3.6,
+                Address = new Address()
                 {
-                    HotelId = "4",
-                    HotelName = "Sublime Palace Hotel",
-                    Description = "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.",
-                    DescriptionFr = "Le Sublime Palace Hotel est situé au coeur du centre historique de sublime dans un quartier extrêmement animé et vivant, à courte distance de marche des sites et monuments de la ville et est entouré par l'extraordinaire beauté des églises, des bâtiments, des commerces et Monuments. Sublime Palace fait partie d'un Palace 1800 restauré avec amour.",
-                    Category = "Boutique",
-                    Tags = new[] { "concierge", "view", "24-hour front desk service" },
-                    ParkingIncluded = true,
-                    LastRenovationDate = new DateTimeOffset(1960, 2, 06, 0, 0, 0, TimeSpan.Zero),
-                    Rating = 4.60,
-                    Address = new Address()
-                    {
-                        StreetAddress = "7400 San Pedro Ave",
-                        City = "San Antonio",
-                        StateProvince = "TX",
-                        PostalCode = "78216",
-                        Country = "USA"
-                    }
-                })
-            );
-
-        try
-        {
-            IndexDocumentsResult result = searchClient.IndexDocuments(batch);
-        }
-        catch (Exception)
-        {
-            // If for some reason any documents are dropped during indexing, you can compensate by delaying and
-            // retrying. This simple demo just logs the failed document keys and continues.
-            Console.WriteLine("Failed to index some of the documents: {0}");
-        }
-    }
-    ```
+                    StreetAddress = "677 5th Ave",
+                    City = "New York",
+                    StateProvince = "NY",
+                    PostalCode = "10022",
+                    Country = "USA"
+                }
+            }),
+        // REDACTED FOR BREVITY
+}
+```
 
-    Once you initialize the [IndexDocumentsBatch](/dotnet/api/azure.search.documents.models.indexdocumentsbatch-1) object, you can send it to the index by calling [IndexDocuments](/dotnet/api/azure.search.documents.searchclient.indexdocuments) on your [SearchClient](/dotnet/api/azure.search.documents.searchclient) object.
+Once you initialize the [IndexDocumentsBatch](/dotnet/api/azure.search.documents.models.indexdocumentsbatch-1) object, you can send it to the index by calling [IndexDocuments](/dotnet/api/azure.search.documents.searchclient.indexdocuments) on your [SearchClient](/dotnet/api/azure.search.documents.searchclient) object.
 
-1. Add the following lines to `Main()`. Loading documents is done using SearchClient, but the operation also requires admin rights on the service, which is typically associated with SearchIndexClient. One way to set up this operation is to get SearchClient through `SearchIndexClient` (`adminClient` in this example).
+You load documents using SearchClient in `Main()`, but the operation also requires admin rights on the service, which is typically associated with SearchIndexClient. One way to set up this operation is to get SearchClient through `SearchIndexClient` (`adminClient` in this example).
 
-   ```csharp
-    SearchClient ingesterClient = adminClient.GetSearchClient(indexName);
+```csharp
+SearchClient ingesterClient = adminClient.GetSearchClient(indexName);
 
-    // Load documents
-    Console.WriteLine("{0}", "Uploading documents...\n");
-    UploadDocuments(ingesterClient);
-   ```
+// Load documents
+Console.WriteLine("{0}", "Uploading documents...\n");
+UploadDocuments(ingesterClient);
+```
 
-1. Because this is a console app that runs all commands sequentially, add a 2-second wait time between indexing and queries.
+Because we have a console app that runs all commands sequentially, we add a 2-second wait time between indexing and queries.
 
-    ```csharp
-    // Wait 2 seconds for indexing to complete before starting queries (for demo and console-app purposes only)
-    Console.WriteLine("Waiting for indexing...\n");
-    System.Threading.Thread.Sleep(2000);
-    ```
+```csharp
+// Wait 2 seconds for indexing to complete before starting queries (for demo and console-app purposes only)
+Console.WriteLine("Waiting for indexing...\n");
+System.Threading.Thread.Sleep(2000);
+```
 
-    The 2-second delay compensates for indexing, which is asynchronous, so that all documents can be indexed before the queries are executed. Coding in a delay is typically only necessary in demos, tests, and sample applications.
+The 2-second delay compensates for indexing, which is asynchronous, so that all documents can be indexed before the queries are executed. Coding in a delay is typically only necessary in demos, tests, and sample applications.
 
-## Search an index
+### Search an index
 
 You can get query results as soon as the first document is indexed, but actual testing of your index should wait until all documents are indexed.
 
 This section adds two pieces of functionality: query logic, and results. For queries, use the [Search](/dotnet/api/azure.search.documents.searchclient.search) method. This method takes search text (the query string) and other [options](/dotnet/api/azure.search.documents.searchoptions).
 
 The [SearchResults](/dotnet/api/azure.search.documents.models.searchresults-1) class represents the results.
 
-1. In *Program.cs*, create a `WriteDocuments` method that prints search results to the console.
+In *Program.cs*, the `WriteDocuments` method prints search results to the console.
 
-    ```csharp
-    // Write search results to console
-    private static void WriteDocuments(SearchResults<Hotel> searchResults)
+```csharp
+// Write search results to console
+private static void WriteDocuments(SearchResults<Hotel> searchResults)
+{
+    foreach (SearchResult<Hotel> result in searchResults.GetResults())
     {
-        foreach (SearchResult<Hotel> result in searchResults.GetResults())
-        {
-            Console.WriteLine(result.Document);
-        }
-
-        Console.WriteLine();
+        Console.WriteLine(result.Document);
     }
 
-    private static void WriteDocuments(AutocompleteResults autoResults)
-    {
-        foreach (AutocompleteItem result in autoResults.Results)
-        {
-            Console.WriteLine(result.Text);
-        }
-
-        Console.WriteLine();
-    }
-    ```
+    Console.WriteLine();
+}
 
-1. Create a `RunQueries` method to execute queries and return results. Results are Hotel objects. This sample shows the method signature and the first query. This query demonstrates the Select parameter that lets you compose the result using selected fields from the document.
-
-    ```csharp
-    // Run queries, use WriteDocuments to print output
-    private static void RunQueries(SearchClient srchclient)
+private static void WriteDocuments(AutocompleteResults autoResults)
+{
+    foreach (AutocompleteItem result in autoResults.Results)
     {
-        SearchOptions options;
-        SearchResults<Hotel> response;
-        
-        // Query 1
-        Console.WriteLine("Query #1: Search on empty term '*' to return all documents, showing a subset of fields...\n");
-
-        options = new SearchOptions()
-        {
-            IncludeTotalCount = true,
-            Filter = "",
-            OrderBy = { "" }
-        };
+        Console.WriteLine(result.Text);
+    }
 
-        options.Select.Add("HotelId");
-        options.Select.Add("HotelName");
-        options.Select.Add("Address/City");
+    Console.WriteLine();
+}
+```
 
-        response = srchclient.Search<Hotel>("*", options);
-        WriteDocuments(response);
-    ```
+#### Query example 1
 
-1. In the second query, search on a term, add a filter that selects documents where *Rating* is greater than 4, and then sort by Rating in descending order. Filter is a boolean expression that is evaluated over [IsFilterable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfilterable) fields in an index. Filter queries either include or exclude values. As such, there's no relevance score associated with a filter query.
+The `RunQueries` method executes queries and returns results. Results are Hotel objects. This sample shows the method signature and the first query. This query demonstrates the Select parameter that lets you compose the result using selected fields from the document.
 
-    ```csharp
-    // Query 2
-    Console.WriteLine("Query #2: Search on 'hotels', filter on 'Rating gt 4', sort by Rating in descending order...\n");
+```csharp
+// Run queries, use WriteDocuments to print output
+private static void RunQueries(SearchClient srchclient)
+{
+    SearchOptions options;
+    SearchResults<Hotel> response;
+    
+    // Query 1
+    Console.WriteLine("Query #1: Search on empty term '*' to return all documents, showing a subset of fields...\n");
 
     options = new SearchOptions()
     {
-        Filter = "Rating gt 4",
-        OrderBy = { "Rating desc" }
+        IncludeTotalCount = true,
+        Filter = "",
+        OrderBy = { "" }
     };
 
     options.Select.Add("HotelId");
     options.Select.Add("HotelName");
-    options.Select.Add("Rating");
+    options.Select.Add("Address/City");
 
-    response = srchclient.Search<Hotel>("hotels", options);
+    response = srchclient.Search<Hotel>("*", options);
     WriteDocuments(response);
-    ```
+    // REDACTED FOR BREVITY
+}
+```
 
-1. The third query demonstrates `searchFields`, used to scope a full text search operation to specific fields.
+#### Query example 2
 
-    ```csharp
-    // Query 3
-    Console.WriteLine("Query #3: Limit search to specific fields (pool in Tags field)...\n");
+In the second query, search on a term, add a filter that selects documents where *Rating* is greater than 4, and then sort by Rating in descending order. Filter is a boolean expression that is evaluated over [IsFilterable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfilterable) fields in an index. Filter queries either include or exclude values. As such, there's no relevance score associated with a filter query.
 
-    options = new SearchOptions()
-    {
-        SearchFields = { "Tags" }
-    };
+```csharp
+// Query 2
+Console.WriteLine("Query #2: Search on 'hotels', filter on 'Rating gt 4', sort by Rating in descending order...\n");
 
-    options.Select.Add("HotelId");
-    options.Select.Add("HotelName");
-    options.Select.Add("Tags");
+options = new SearchOptions()
+{
+    Filter = "Rating gt 4",
+    OrderBy = { "Rating desc" }
+};
 
-    response = srchclient.Search<Hotel>("pool", options);
-    WriteDocuments(response);
-    ```
+options.Select.Add("HotelId");
+options.Select.Add("HotelName");
+options.Select.Add("Rating");
 
-1. The fourth query demonstrates `facets`, which can be used to structure a faceted navigation structure.
+response = srchclient.Search<Hotel>("hotels", options);
+WriteDocuments(response);
+```
 
-   ```csharp
-    // Query 4
-    Console.WriteLine("Query #4: Facet on 'Category'...\n");
+#### Query example 3
+The third query demonstrates `searchFields`, used to scope a full text search operation to specific fields.
 
-    options = new SearchOptions()
-    {
-        Filter = ""
-    };
+```csharp
+// Query 3
+Console.WriteLine("Query #3: Limit search to specific fields (pool in Tags field)...\n");
 
-    options.Facets.Add("Category");
+options = new SearchOptions()
+{
+    SearchFields = { "Tags" }
+};
 
-    options.Select.Add("HotelId");
-    options.Select.Add("HotelName");
-    options.Select.Add("Category");
+options.Select.Add("HotelId");
+options.Select.Add("HotelName");
+options.Select.Add("Tags");
 
-    response = srchclient.Search<Hotel>("*", options);
-    WriteDocuments(response);
-   ```
+response = srchclient.Search<Hotel>("pool", options);
+WriteDocuments(response);
+```
 
-1. In the fifth query, return a specific document. A document lookup is a typical response to `OnClick` event in a result set.
+#### Query example 4
 
-   ```csharp
-    // Query 5
-    Console.WriteLine("Query #5: Look up a specific document...\n");
+The fourth query demonstrates `facets`, which can be used to structure a faceted navigation structure.
 
-    Response<Hotel> lookupResponse;
-    lookupResponse = srchclient.GetDocument<Hotel>("3");
+```csharp
+// Query 4
+Console.WriteLine("Query #4: Facet on 'Category'...\n");
 
-    Console.WriteLine(lookupResponse.Value.HotelId);
-   ```
+options = new SearchOptions()
+{
+    Filter = ""
+};
 
-1. The last query shows the syntax for autocomplete, simulating a partial user input of *sa* that resolves to two possible matches in the sourceFields associated with the suggester you defined in the index.
+options.Facets.Add("Category");
 
-   ```csharp
-    // Query 6
-    Console.WriteLine("Query #6: Call Autocomplete on HotelName that starts with 'sa'...\n");
+options.Select.Add("HotelId");
+options.Select.Add("HotelName");
+options.Select.Add("Category");
 
-    var autoresponse = srchclient.Autocomplete("sa", "sg");
-    WriteDocuments(autoresponse);
-   ```
+response = srchclient.Search<Hotel>("*", options);
+WriteDocuments(response);
+```
 
-1. Add `RunQueries` to `Main()`.
+#### Query example 5
 
-    ```csharp
-    // Call the RunQueries method to invoke a series of queries
-    Console.WriteLine("Starting queries...\n");
-    RunQueries(srchclient);
+In the fifth query, return a specific document. A document lookup is a typical response to `OnClick` event in a result set.
 
-    // End the program
-    Console.WriteLine("{0}", "Complete. Press any key to end this program...\n");
-    Console.ReadKey();
-    ```
+```csharp
+// Query 5
+Console.WriteLine("Query #5: Look up a specific document...\n");
 
-The previous queries show multiple [ways of matching terms in a query](/azure/search/search-query-overview#types-of-queries): full-text search, filters, and autocomplete.
+Response<Hotel> lookupResponse;
+lookupResponse = srchclient.GetDocument<Hotel>("3");
 
-Full text search and filters are performed using the [SearchClient.Search](/dotnet/api/azure.search.documents.searchclient.search) method. A search query can be passed in the `searchText` string, while a filter expression can be passed in the [Filter](/dotnet/api/azure.search.documents.searchoptions.filter) property of the [SearchOptions](/dotnet/api/azure.search.documents.searchoptions) class. To filter without searching, just pass `"*"` for the `searchText` parameter of the [Search](/dotnet/api/azure.search.documents.searchclient.search) method. To search without filtering, leave the `Filter` property unset, or don't pass in a `SearchOptions` instance at all.
+Console.WriteLine(lookupResponse.Value.HotelId);
+```
 
-## Run the program
+#### Query example 6
 
-Press **F5** to rebuild the app and run the program in its entirety.
+The last query shows the syntax for autocomplete, simulating a partial user input of *sa* that resolves to two possible matches in the sourceFields associated with the suggester you defined in the index.
+
+```csharp
+// Query 6
+Console.WriteLine("Query #6: Call Autocomplete on HotelName that starts with 'sa'...\n");
+
+var autoresponse = srchclient.Autocomplete("sa", "sg");
+WriteDocuments(autoresponse);
+```
+
+#### Summary of queries
+
+The previous queries show multiple [ways of matching terms in a query](/azure/search/search-query-overview#types-of-queries): full-text search, filters, and autocomplete.
+
+Full text search and filters are performed using the [SearchClient.Search](/dotnet/api/azure.search.documents.searchclient.search) method. A search query can be passed in the `searchText` string, while a filter expression can be passed in the [Filter](/dotnet/api/azure.search.documents.searchoptions.filter) property of the [SearchOptions](/dotnet/api/azure.search.documents.searchoptions) class. To filter without searching, just pass `"*"` for the `searchText` parameter of the [Search](/dotnet/api/azure.search.documents.searchclient.search) method. To search without filtering, leave the `Filter` property unset, or don't pass in a `SearchOptions` instance at all.
 
-Output includes messages from [Console.WriteLine](/dotnet/api/system.console.writeline), with the addition of query information and results.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#での全体テキスト検索クイックスタートの更新"
}
```

### Explanation
この変更では、Azure AI Searchを利用したC#での全体テキスト検索に関するクイックスタートガイドが更新されました。変更内容には、日付の更新、環境構築の手順の明確化、Microsoft Entra IDによる認証の推奨、ソースコードの構造の強化、および具体的なコード例とステップバイステップの説明が含まれています。

具体的には、Azure.Search.Documentsライブラリを使用して、検索インデックスを構築し、ドキュメントを読み込み、クエリを実行する手順が明示化されています。また、ドキュメントの構造も改善され、`Hotel`と`Address`というクラスが定義され、それぞれのフィールドに適切な属性が設定されました。このようにして、ユーザーがクイックスタートを通じて、全体のプロセスをより理解しやすくなるように配慮されています。

さらに、エラーハンドリングの追加や、コンソールアプリケーションの出力に関する詳細なコード例も提供され、実用的な情報が強化されています。これによって、開発者は新しいフィーチャーやコードの例を活用し、効果的な検索アプリケーションの実装に役立てることができます。

## articles/search/includes/quickstarts/full-text-intro.md{#item-f655a1}

<details>
<summary>Diff</summary>
````diff
@@ -4,23 +4,10 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/8/2025
+ms.date: 2/12/2025
 ---
 
-Learn how to use the *Azure.Search.Documents* client library in an Azure SDK to create, load, and query a search index using sample data for [full text search](../../search-lucene-query-architecture.md). Full text search uses Apache Lucene for indexing and queries, and a BM25 ranking algorithm for scoring results.
+Learn how to use the *Azure.Search.Documents* client library to create, load, and query a search index using sample data for [full text search](../../search-lucene-query-architecture.md). Full text search uses Apache Lucene for indexing and queries, and a BM25 ranking algorithm for scoring results.
 
-This quickstart creates and queries a small hotels-quickstart index containing data about 4 hotels.
+This quickstart creates and queries a small hotels-quickstart index containing data about four hotels.
 
-## Prerequisites
-
-+ An Azure account with an active subscription. You can [create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?icid=azurefreeaccount).
-
-+ An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
-
-+ An API key and service endpoint for your service. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch).
-
-  In the **Overview** section, copy the URL and save it to a text editor for a later step. An example endpoint might look like `https://mydemo.search.windows.net`.
-
-  In the **Settings** > **Keys** section, copy and save an admin key for full rights to create and delete objects. There are two interchangeable primary and secondary keys. Choose either one.
-
-  :::image type="content" source="../../media/search-get-started-rest/get-url-key.png" alt-text="Screenshot that shows the HTTP endpoint and the primary and secondary API key locations.":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "全体テキスト検索クイックスタートのイントロダクションの更新"
}
```

### Explanation
この変更により、全体テキスト検索のクイックスタートガイドのイントロダクション部分が更新されました。主な変更点として、日付の修正が行われ、特に2025年2月8日から2025年2月12日に変更されました。また、いくつかの文言が簡潔に改訂され、内容が明確になりました。

具体的には、サンプルデータを使用して検索インデックスを作成、読み込み、クエリするための*Azure.Search.Documents*クライアントライブラリの使用方法に関する説明が強調されています。特に、フルテキスト検索の概要についても言及されており、リューシンのインデックス作成方式とBM25スコアリングアルゴリズムについての情報が提供されています。

さらに、「前提条件」セクションが削除されて、代わりに簡潔な情報が掲載され、内容の冗長性が軽減されると同時に、クイックスタートの目的の理解が向上するように配慮されています。このような変更は、読者がよりスムーズに内容を把握できるようにするための改良です。

## articles/search/includes/quickstarts/full-text-java.md{#item-d659f9}

<details>
<summary>Diff</summary>
````diff
@@ -4,14 +4,28 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/8/2025
+ms.date: 2/12/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
 
-Build a Java console application using the [Azure.Search.Documents](/java/api/overview/azure/search) library to create, load, and query a search index. 
+> [!TIP]
+> You can [download the source code](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
 
-Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
+## Prerequisites
+
+- An active Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
+- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
+
+## Microsoft Entra ID prerequisites
+
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign both of the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
+
+## Retrieve resource information
+
+[!INCLUDE [resource authentication](../resource-authentication.md)]
 
 ## Set up your environment
 
@@ -59,7 +73,7 @@ Use the following tools to create this quickstart.
 
 ## Specify Maven dependencies
 
-1. Open the *pom.xml* file and add the following dependencies.
+1. Open the *pom.xml* file and add the following dependencies. This includes the [Azure.Search.Documents](/java/api/overview/azure/search) library.
 
     ```xml
     <dependencies>
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaでの全体テキスト検索クイックスタートの更新"
}
```

### Explanation
この変更では、Javaにおける全体テキスト検索のクイックスタートガイドに対していくつかの重要な更新が行われました。主な変更点は、日付の更新が行われ、2025年2月8日から2025年2月12日に修正されています。また、ユーザーに対してソースコードをダウンロードできるリンクが追加され、開発を開始するための便利な情報が提供されています。

新たに追加された内容としては、AzureのアクティブなサブスクリプションやAzure AI Searchサービスの作成に関する前提条件セクションが設けられ、Microsoft Entra IDを用いた推奨の非キー認証についての情報も追加されています。これには、Azure CLIのインストールや、特定の役割をユーザーアカウントに割り当てる方法が含まれています。

さらに、資源情報の取得に関するコンテンツも追加され、リソース認証に関する情報が包括的にまとめられています。これにより、クイックスタートガイドがより包括的で、ユーザーがスムーズにプロジェクトを開始できるようになっています。また、Mavenの依存関係を指定する際に、Azure.Search.Documentsライブラリの追加についても明記されています。全体として、これらの変更はユーザーに対する情報提供の強化を図ったものとなっています。

## articles/search/includes/quickstarts/full-text-javascript.md{#item-568e3a}

<details>
<summary>Diff</summary>
````diff
@@ -4,14 +4,28 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/8/2025
+ms.date: 2/12/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
 
-Build a Node.js application using the [@azure/search-documents](/javascript/api/overview/azure/search-documents-readme) library to create, load, and query a search index. 
+> [!TIP]
+> You can [download the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
 
-Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
+## Prerequisites
+
+- An active Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
+- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
+
+## Microsoft Entra ID prerequisites
+
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign both of the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
+
+## Retrieve resource information
+
+[!INCLUDE [resource authentication](../resource-authentication.md)]
 
 ## Set up your environment
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptでの全体テキスト検索クイックスタートの更新"
}
```

### Explanation
この変更は、JavaScriptにおける全体テキスト検索のクイックスタートガイドに対する更新を行ったものです。主な変更点には、日付の更新が含まれ、2025年2月8日から2025年2月12日に修正されています。また、ソースコードをダウンロードできるリンクが追加され、プロジェクトを開始するための便利な情報が提供されています。

新たに追加された内容には、AzureのアクティブなサブスクリプションやAzure AI Searchサービスの前提条件が明確に示されています。これにより、ユーザーは必要な準備を整えることができるようになっています。さらに、Microsoft Entra IDによる非キー認証に関する情報が追加され、Azure CLIのインストールや具体的な役割の割り当て方法についても詳しく説明されています。

「資源情報の取得」に関する新しいセクションも設けられ、リソース認証に関する情報が整理されて表示されています。全体として、これらの変更は、ユーザーがクイックスタートを通じてスムーズに開発を行えるようにするための情報提供を強化したものとなっています。

## articles/search/includes/quickstarts/full-text-python.md{#item-9bba1c}

<details>
<summary>Diff</summary>
````diff
@@ -4,14 +4,28 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/8/2025
+ms.date: 2/12/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
 
-Use a Jupyter notebook and the [azure-search-documents](/python/api/overview/azure/search-documents-readme) library in the Azure SDK for Python to create, load, and query a search index. 
+> [!TIP]
+> You can download and run a [finished notebook](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart).
 
-Alternatively, you can download and run a [finished notebook](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart).
+## Prerequisites
+
+- An active Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
+- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
+
+## Microsoft Entra ID prerequisites
+
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign both of the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
+
+## Retrieve resource information
+
+[!INCLUDE [resource authentication](../resource-authentication.md)]
 
 ## Set up your environment
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonでの全体テキスト検索クイックスタートの更新"
}
```

### Explanation
この変更は、Pythonにおける全体テキスト検索のクイックスタートガイドに対する重要な更新を含んでいます。変更内容の中で注目すべき点は、日付が2025年2月8日から2025年2月12日に修正されたことです。また、Jupyterノートブックを使用してAzure SDK for Pythonを通じて、検索インデックスを作成、読み込み、クエリする手順が具体的に記載されています。

新たに追加された内容には、ユーザーが使用する必要のある前提条件が挙げられており、アクティブなAzureサブスクリプションやAzure AI Searchサービスの作成が求められています。また、Microsoft Entra IDを用いた推奨の非キー認証に関しても詳細が説明されています。これには、Azure CLIのインストールや、役割の割り当て方法が含まれています。

さらには、「資源情報の取得」に関するセクションも追加され、ユーザーがリソース認証についての情報をよりよく理解できるようになっています。全体として、これらの変更はユーザーがPythonを用いた全体テキスト検索の実装を行う際に、必要な情報やリソースを調整しやすくする助けとなる内容となっています。

## articles/search/includes/quickstarts/full-text-typescript.md{#item-6630e8}

<details>
<summary>Diff</summary>
````diff
@@ -4,14 +4,28 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/8/2025
+ms.date: 2/12/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
 
-Build a Node.js application using the [@azure/search-documents](/javascript/api/overview/azure/search-documents-readme) library to create, load, and query a search index. 
+> [!TIP]
+> You can [download the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
 
-Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
+## Prerequisites
+
+- An active Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
+- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
+
+## Microsoft Entra ID prerequisites
+
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign both of the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
+
+## Retrieve resource information
+
+[!INCLUDE [resource authentication](../resource-authentication.md)]
 
 ## Set up your environment
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptでの全体テキスト検索クイックスタートの更新"
}
```

### Explanation
この変更は、TypeScriptにおける全体テキスト検索のクイックスタートガイドの更新を反映しています。主なポイントとして、日付が2025年2月8日から2025年2月12日に変更されており、内容が最新の情報に調整されています。Node.jsアプリケーションを構築する際に、[@azure/search-documents](/javascript/api/overview/azure/search-documents-readme)ライブラリを使用して検索インデックスを作成、読み込み、クエリする手順が強調されています。

新たに追加されたセクションは、ユーザーがプロジェクトを開始するのに必要な前提条件に関する情報を提供しており、アクティブなAzureサブスクリプションやAzure AI Searchサービスの作成方法が示されています。また、Microsoft Entra IDを使用した非キー認証の設定に関する推奨事項も追加されています。これには、Azure CLIのインストールと役割の割り当てに関しての説明が含まれています。

さらに、「資源情報の取得」に関するセクションも設けられ、リソース認証の情報を簡単に取得できるようになっています。全体として、これらの更新はユーザーがTypeScriptを利用して全体テキスト検索を効果的に実施できるようにするための情報をさらに充実させています。

## articles/search/includes/resource-authentication.md{#item-381ff1}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,33 @@
+---
+author: eric-urban 
+ms.author: eur 
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 2/12/2025
+---
+
+You need to retrieve the following information to authenticate your application with your Azure AI Search service:
+
+#### [Microsoft Entra ID](#tab/keyless)
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `SEARCH_API_ENDPOINT` | This value can be found in the Azure portal. Select your search service and then from the left menu, select **Overview**. The **Url** value under **Essentials** is the endpoint that you need. An example endpoint might look like `https://mydemo.search.windows.net`. |
+
+Learn more about [keyless authentication](/azure/search/keyless-connections) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
+
+#### [API key](#tab/api-key)
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `SEARCH_API_ENDPOINT` | This value can be found in the Azure portal. Select your search service and then from the left menu, select **Overview**. The **Url** value under **Essentials** is the endpoint that you need. An example endpoint might look like `https://mydemo.search.windows.net`. |
+| `SEARCH_API_KEY` | This value can be found in the Azure portal. Select your search service and then from the left menu, select **Settings** > **Keys**. You can use either `KEY1` or `KEY2`.|
+
+Learn more about [finding API keys](/azure/search/search-security-api-keys) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+
+---
+
+
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "リソース認証に関する新しいガイド"
}
```

### Explanation
この変更は、Azure AI Searchサービスとアプリケーションを認証するために必要な情報を記載した新しいドキュメント「リソース認証」を追加したものです。このファイルでは、Microsoft Entra IDおよびAPIキーを使用した認証のための必要な変数とその値の取得方法が詳しく説明されています。

具体的には、Azureポータルから取得できる`SEARCH_API_ENDPOINT`の値と、APIキーに関する情報が提供されています。ユーザーは、指定された手順に従って、必要なエンドポイントおよびAPIキーを見つけることができるように誘導されています。また、キーレス認証に関する詳細や環境変数の設定方法についてのリンクも含まれています。

さらに、Azure Key Vaultに関連する情報も追加されており、セキュアなキー管理の重要性が強調されています。この新機能は、ユーザーがAzure AI Searchサービスを用いてアプリケーションを効果的に認証するための重要なリソースとなります。全体として、このドキュメントは初心者から上級者まで、より安心してAzureを利用できるように設計されています。

## articles/search/search-get-started-text.md{#item-935941}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.custom:
   - ignite-2023
 ms.topic: quickstart
 zone_pivot_groups: search-quickstart-full-text
-ms.date: 2/8/2025
+ms.date: 2/12/2025
 ---
 
 # Quickstart: Full text search using the Azure SDKs
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートガイドの日付更新"
}
```

### Explanation
この変更は、Azure SDKを使用した全文検索のクイックスタートガイドにおける日付の更新を反映しています。具体的には、前の版の日付が2025年2月8日から2025年2月12日に修正されました。このような日付の更新は、ドキュメントの最新性を維持するために重要です。また、ガイドの他の内容は変更されておらず、基本的なクイックスタートの情報が引き続き提供されています。

このマイナーアップデートは、ユーザーが最新の日付情報を把握できるようにし、ドキュメントが常に最新の状況を反映していることを確認する役割を果たしています。全体として、この変更は、利用者に対してより正確で信頼性のある情報を提供するためのものです。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -61,14 +61,14 @@ AI service integration refers to internal connections to an Azure AI multi-servi
 | North Europe​​ | ✅ | ✅ | ✅ | All tiers|
 | West Europe​​ | ✅ | ✅ | ✅ |  |
 | France Central​​ | ✅ | ✅ | ✅ | All Tiers|
-| Germany West Central​ <sup>1</sup>​| ✅ |  | ✅ | |
+| Germany West Central​ ​| ✅ |  | ✅ | |
 | Italy North​​ |  |  | ✅ | |
 | Norway East​​ | ✅ |  | ✅ |  |
 | Poland Central​​ |  |  |  |  |
 | Spain Central <sup>1</sup> |  |  | ✅  |  |
 | Sweden Central​​ | ✅ |  | ✅ |  |
 | Switzerland North​ | ✅ | ✅ | ✅ |  |
-| Switzerland West​ <sup>1</sup>| ✅ | ✅ | ✅ |  |
+| Switzerland West​ | ✅ | ✅ | ✅ |  |
 | UK South​ | ✅ | ✅ | ✅ |  |
 | UK West​ ​|  | ✅ | |  |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域サポートの表記修正"
}
```

### Explanation
この変更は、Azureの地域サポートに関するドキュメント内の表記を修正したものです。具体的には、複数の地域名における不必要なスペースや形式を統一し、見栄えを改善しました。例えば、「Germany West Central」や「Switzerland West」の行では、表のフォーマットが整えられ、それぞれの地域名のスペースが調整されています。

変更内容は軽微ですが、ドキュメントの整流化と可読性の向上に寄与しています。このようなマイナーなアップデートは、利用者にとって重要な情報を提供する際の一貫性を保つのに役立ちます。全体として、これによりユーザーが地域サポート情報を簡単に理解できるようになっています。


