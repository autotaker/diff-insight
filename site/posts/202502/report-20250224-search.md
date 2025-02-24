---
date: '2025-02-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b49c252...MicrosoftDocs:8c6e364
summary: 今回のコード変更は、Azure AI Searchに関連する多言語ドキュメントのアップデートを含んでいます。特にPython用のクイックスタートガイドが大幅に改訂され、サンプルコード実行環境としてJupyterノートブックが導入されました。また、Pythonのフルテキスト検索ドキュメントでは多くの行が削除・追加・変更され、既存のコードとの互換性が一部損なわれる可能性があります。一方で、JavaScriptおよびTypeScriptのドキュメントでは表現の微調整が行われ、文の明確性が向上しました。全体として、この更新はAzure
  AI Searchの利用を促進するもので、特に初学者にとって有益です。既存のユーザーは、新しいツールへの移行が必要です。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b49c252...MicrosoftDocs:8c6e364){target="_blank"}

# ハイライト

今回のコード変更は、Azure AI Searchに関連する多言語ドキュメントのアップデートを含んでいます。JavaScriptおよびTypeScript用のクイックスタートガイドに軽微な修正が加えられたほか、Pythonガイドでは大幅な改訂が行われました。

## 新機能

- Python用クイックスタートガイドで、サンプルコードが実行される環境としてJupyterノートブックの利用が導入されました。

## 重大な変更

- Pythonのフルテキスト検索ドキュメントでは、約269行が削除される一方で100行が新たに追加され、369行が変更されるなど、大幅な改訂が実施されました。これにより既存のコードや説明との互換性が一部損なわれる可能性があります。

## その他の更新

- JavaScriptおよびTypeScriptのドキュメントで、表現の調整（「will be identified by」から「is identified by」）が行われ、文の明確性が改善されました。

# インサイト

今回の変更は、ユーザーフレンドリーなドキュメントの提供に重点を置いています。特に、Python用クイックスタートガイドの大幅な改訂は、ユーザーが最新の推奨環境やツール（Jupyterノートブック）を用いてより効果的にAzure AI Searchの機能を利用できるよう意図されています。これは初学者にとって大きな助けとなるでしょう。

さらに、JavaScriptやTypeScript用ドキュメントにおいて表現が現在形に統一されたことで、読者に対するメッセージの一貫性が強化され、理解が深まります。このような軽微な表現の改善は、多くのユーザーにとって重要となる場合があります。特に、異なる言語で統一された表現を持つことで、ユーザーは複数のガイドを横断する際にも、混乱を最小限に抑えられることが期待されます。

全体的に、このドキュメントの更新はAzure AI Searchの利用を更に促進する要因となり得ます。既存のユーザーは、特にPythonのガイドで新しいツールや手法に移行する必要があることに留意しなければなりませんが、その努力の価値は高いと考えられます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [full-text-javascript.md](#item-568e3a) | minor update | フルテキスト検索に関するドキュメントの軽微な修正 | modified | 1 | 1 | 2 | 
| [full-text-python.md](#item-9bba1c) | breaking change | Python用フルテキスト検索ドキュメントの大幅な改訂 | modified | 100 | 269 | 369 | 
| [full-text-typescript.md](#item-6630e8) | minor update | TypeScript用フルテキスト検索ドキュメントの軽微な修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/includes/quickstarts/full-text-javascript.md{#item-568e3a}

<details>
<summary>Diff</summary>
````diff
@@ -544,7 +544,7 @@ AzureKeyCredential credential = new AzureKeyCredential("<Your search service adm
 
 ### Create index
 
-The *hotels_quickstart_index.json* file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
+The *hotels_quickstart_index.json* file defines how Azure AI Search works with the documents you load in the next step. Each field is identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
 
 With our index definition in place, we want to import *hotels_quickstart_index.json* at the top of *index.js* so the main function can access the index definition.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フルテキスト検索に関するドキュメントの軽微な修正"
}
```

### Explanation
今回の変更は、Azure AI Searchに関するフルテキストJavaScriptのクイックスタートガイドにおける軽微な修正を含んでいます。具体的には、文中の表現において「will be identified by」から「is identified by」に書き換えられ、より一貫した現在形に整えられました。この変更は文の明確さを高め、読み手にとっての理解を助けるものです。修正点は、索引定義に関連する内容が含まれており、今後の手順で使用するドキュメントのフォーマットや重要性に対する説明の一貫性を強化しています。また、全体的な構文の流れを向上させる目的があると考えられます。

## articles/search/includes/quickstarts/full-text-python.md{#item-9bba1c}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/12/2025
+ms.date: 2/22/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
@@ -16,6 +16,7 @@ ms.date: 2/12/2025
 
 - An active Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
 - An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
+- [Visual Studio Code with the Python extension](https://code.visualstudio.com/docs/languages/python), or an equivalent IDE, with Python 3.10 or later. If you don't have a suitable version of Python installed, you can follow the instructions in the [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter).
 
 ## Microsoft Entra ID prerequisites
 
@@ -29,306 +30,136 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Set up your environment
 
-Use [Visual Studio Code with the Python extension](https://code.visualstudio.com/docs/languages/python), or an equivalent IDE, with Python 3.10 or later.
+You run the sample code in a Jupyter notebook. So, you need to set up your environment to run Jupyter notebooks.
 
-We recommend a virtual environment for this quickstart:
+1. Download or copy the [sample notebook from GitHub](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart).
 
-1. Start Visual Studio Code.
+1. Open the notebook in Visual Studio Code.
 
-1. Open the Command Palette (**Ctrl+Shift+P**).
+1. Create a new Python environment to use to install the packages you need for this tutorial. 
 
-1. Search for **Python: Create Environment**.
+    > [!IMPORTANT]
+    > Don't install packages into your global python installation. You should always use a virtual or conda environment when installing python packages, otherwise you can break your global install of Python.
 
-1. Select `Venv.`
-
-1. Select a Python interpreter. Choose version 3.10 or later.
-
-It can take a minute to set up. If you run into problems, see [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments).
-
-## Install packages and set variables
-
-1. Install packages, including [azure-search-documents](/python/api/azure-search-documents). 
-
-    ```python
-    ! pip install azure-search-documents==11.6.0b1 --quiet
-    ! pip install azure-identity --quiet
-    ! pip install python-dotenv --quiet
+    # [Windows](#tab/windows)
+    
+    ```bash
+    py -3 -m venv .venv
+    .venv\scripts\activate
     ```
-
-1. Provide the endpoint and API key for your service:
-
-    ```python
-    search_endpoint: str = "PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE"
-    search_api_key: str = "PUT-YOUR-SEARCH-SERVICE-ADMIN-API-KEY-HERE"
-    index_name: str = "hotels-quickstart"
+    
+    # [Linux](#tab/linux)
+    
+    ```bash
+    python3 -m venv .venv
+    source .venv/bin/activate
     ```
+    
+    # [macOS](#tab/macos)
+    
+    ```bash
+    python3 -m venv .venv
+    source .venv/bin/activate
+    ```
+    
+    ---
 
-## Create an index
-
-```python
-from azure.core.credentials import AzureKeyCredential
-
-credential = AzureKeyCredential(search_api_key)
-from azure.search.documents.indexes import SearchIndexClient
-from azure.search.documents import SearchClient
-from azure.search.documents.indexes.models import (
-    ComplexField,
-    SimpleField,
-    SearchFieldDataType,
-    SearchableField,
-    SearchIndex
-)
-
-# Create a search schema
-index_client = SearchIndexClient(
-    endpoint=search_endpoint, credential=credential)
-fields = [
-        SimpleField(name="HotelId", type=SearchFieldDataType.String, key=True),
-        SearchableField(name="HotelName", type=SearchFieldDataType.String, sortable=True),
-        SearchableField(name="Description", type=SearchFieldDataType.String, analyzer_name="en.lucene"),
-        SearchableField(name="Description_fr", type=SearchFieldDataType.String, analyzer_name="fr.lucene"),
-        SearchableField(name="Category", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
-
-        SearchableField(name="Tags", collection=True, type=SearchFieldDataType.String, facetable=True, filterable=True),
-
-        SimpleField(name="ParkingIncluded", type=SearchFieldDataType.Boolean, facetable=True, filterable=True, sortable=True),
-        SimpleField(name="LastRenovationDate", type=SearchFieldDataType.DateTimeOffset, facetable=True, filterable=True, sortable=True),
-        SimpleField(name="Rating", type=SearchFieldDataType.Double, facetable=True, filterable=True, sortable=True),
-
-        ComplexField(name="Address", fields=[
-            SearchableField(name="StreetAddress", type=SearchFieldDataType.String),
-            SearchableField(name="City", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
-            SearchableField(name="StateProvince", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
-            SearchableField(name="PostalCode", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
-            SearchableField(name="Country", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
-        ])
-    ]
-
-scoring_profiles = []
-suggester = [{'name': 'sg', 'source_fields': ['Tags', 'Address/City', 'Address/Country']}]
-
-# Create the search index
-index = SearchIndex(name=index_name, fields=fields, suggesters=suggester, scoring_profiles=scoring_profiles)
-result = index_client.create_or_update_index(index)
-print(f' {result.name} created')
-```
-
-## Create a documents payload
-
-Use an [index action](/python/api/azure-search-documents/azure.search.documents.models.indexaction) for the operation type, such as upload or merge-and-upload. Documents originate from the [HotelsData](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotels/HotelsData_toAzureSearch.JSON) sample on GitHub.
-
-```python
-# Create a documents payload
-documents = [
-    {
-    "@search.action": "upload",
-    "HotelId": "1",
-    "HotelName": "Stay-Kay City Hotel",
-    "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
-    "Description_fr": "L'hôtel est idéalement situé sur la principale artère commerciale de la ville en plein cœur de New York. A quelques minutes se trouve la place du temps et le centre historique de la ville, ainsi que d'autres lieux d'intérêt qui font de New York l'une des villes les plus attractives et cosmopolites de l'Amérique.",
-    "Category": "Boutique",
-    "Tags": [ "pool", "air conditioning", "concierge" ],
-    "ParkingIncluded": "false",
-    "LastRenovationDate": "1970-01-18T00:00:00Z",
-    "Rating": 3.60,
-    "Address": {
-        "StreetAddress": "677 5th Ave",
-        "City": "New York",
-        "StateProvince": "NY",
-        "PostalCode": "10022",
-        "Country": "USA"
-        }
-    },
-    {
-    "@search.action": "upload",
-    "HotelId": "2",
-    "HotelName": "Old Century Hotel",
-    "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
-    "Description_fr": "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
-    "Category": "Boutique",
-    "Tags": [ "pool", "free wifi", "concierge" ],
-    "ParkingIncluded": "false",
-    "LastRenovationDate": "1979-02-18T00:00:00Z",
-    "Rating": 3.60,
-    "Address": {
-        "StreetAddress": "140 University Town Center Dr",
-        "City": "Sarasota",
-        "StateProvince": "FL",
-        "PostalCode": "34243",
-        "Country": "USA"
-        }
-    },
-    {
-    "@search.action": "upload",
-    "HotelId": "3",
-    "HotelName": "Gastronomic Landscape Hotel",
-    "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel's restaurant services.",
-    "Description_fr": "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
-    "Category": "Resort and Spa",
-    "Tags": [ "air conditioning", "bar", "continental breakfast" ],
-    "ParkingIncluded": "true",
-    "LastRenovationDate": "2015-09-20T00:00:00Z",
-    "Rating": 4.80,
-    "Address": {
-        "StreetAddress": "3393 Peachtree Rd",
-        "City": "Atlanta",
-        "StateProvince": "GA",
-        "PostalCode": "30326",
-        "Country": "USA"
-        }
-    },
-    {
-    "@search.action": "upload",
-    "HotelId": "4",
-    "HotelName": "Sublime Palace Hotel",
-    "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.",
-    "Description_fr": "Le Sublime Palace Hotel est situé au coeur du centre historique de sublime dans un quartier extrêmement animé et vivant, à courte distance de marche des sites et monuments de la ville et est entouré par l'extraordinaire beauté des églises, des bâtiments, des commerces et Monuments. Sublime Palace fait partie d'un Palace 1800 restauré avec amour.",
-    "Category": "Boutique",
-    "Tags": [ "concierge", "view", "24-hour front desk service" ],
-    "ParkingIncluded": "true",
-    "LastRenovationDate": "1960-02-06T00:00:00Z",
-    "Rating": 4.60,
-    "Address": {
-        "StreetAddress": "7400 San Pedro Ave",
-        "City": "San Antonio",
-        "StateProvince": "TX",
-        "PostalCode": "78216",
-        "Country": "USA"
-        }
-    }
-]
-```
-
-## Upload documents
-
-```python
-# Upload documents to the index
-search_client = SearchClient(endpoint=search_endpoint,
-                      index_name=index_name,
-                      credential=credential)
-try:
-    result = search_client.upload_documents(documents=documents)
-    print("Upload of new document succeeded: {}".format(result[0].succeeded))
-except Exception as ex:
-    print (ex.message)
-
-    index_client = SearchIndexClient(
-    endpoint=search_endpoint, credential=credential)
-```
-
-## Run your first query
-
-Use the *search* method of the [search.client class](/python/api/azure-search-documents/azure.search.documents.searchclient).
-
-This example executes an empty search (`search=*`), returning an unranked list (search score = 1.0) of arbitrary documents. Because there are no criteria, all documents are included in results.
-
-```python
-# Run an empty query (returns selected fields, all documents)
-results =  search_client.search(query_type='simple',
-    search_text="*" ,
-    select='HotelName,Description',
-    include_total_count=True)
-
-print ('Total Documents Matching Query:', results.get_count())
-for result in results:
-    print(result["@search.score"])
-    print(result["HotelName"])
-    print(f"Description: {result['Description']}")
-```
+    It can take a minute to set up. If you run into problems, see [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments).
 
-## Run a term query
+1. Install Jupyter notebooks and the IPython Kernel for Jupyter notebooks if you don't have them already.
 
-The next query adds whole terms to the search expression ("wifi"). This query specifies that results contain only those fields in the `select` statement. Limiting the fields that come back minimizes the amount of data sent back over the wire and reduces search latency.
+    ```bash
+    pip install jupyter
+    pip install ipykernel
+    python -m ipykernel install --user --name=.venv
+    ```
 
-```python
-results =  search_client.search(query_type='simple',
-    search_text="wifi" ,
-    select='HotelName,Description,Tags',
-    include_total_count=True)
+1. Select the notebook kernel.
 
-print ('Total Documents Matching Query:', results.get_count())
-for result in results:
-    print(result["@search.score"])
-    print(result["HotelName"])
-    print(f"Description: {result['Description']}")
-```
+    1. In the top right corner of the notebook, select **Select Kernel**.
+    1. If you see `.venv` in the list, select it. If you don't see it, select **Select Another Kernel** > **Python environments** > `.venv`.
 
-## Add a filter
+## Create, load, and query a search index
 
-Add a filter expression, returning only those hotels with a rating greater than four, sorted in descending order.
+In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [explaining the code](#explaining-the-code) section.
 
-```python
-# Add a filter
-results = search_client.search(
-    search_text="hotels", 
-    select='HotelId,HotelName,Rating', 
-    filter='Rating gt 4', 
-    order_by='Rating desc')
+1. Make sure the notebook is open in the `.venv` kernel as described in the previous section.
+1. Run the first code cell to install the required packages, including [azure-search-documents](/python/api/azure-search-documents). 
 
-for result in results:
-    print("{}: {} - {} rating".format(result["HotelId"], result["HotelName"], result["Rating"]))
-```
+    ```python
+    ! pip install azure-search-documents==11.6.0b1 --quiet
+    ! pip install azure-identity --quiet
+    ! pip install python-dotenv --quiet
+    ```
 
-## Add field scoping
+1. Replace contents of the second code cell with the following code depending on your authentication method. 
 
-Add `search_fields` to scope query execution to specific fields.
+    > [!NOTE]
+    > The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
 
-```python
-# Add search_fields to scope query matching to the HotelName field
-results = search_client.search(
-    search_text="sublime", 
-    search_fields=['HotelName'], 
-    select='HotelId,HotelName')
+    #### [Microsoft Entra ID](#tab/keyless)
+    
+    ```python
+    from azure.core.credentials import AzureKeyCredential
+    from azure.identity import DefaultAzureCredential, AzureAuthorityHosts
+    
+    search_endpoint: str = "https://<Put your search service NAME here>.search.windows.net/"
+    authority = AzureAuthorityHosts.AZURE_PUBLIC_CLOUD
+    credential = DefaultAzureCredential(authority=authority)
+
+    index_name: str = "hotels-quickstart-python"
+    ```
+    
+    #### [API key](#tab/api-key)
+    
+    ```python
+    from azure.core.credentials import AzureKeyCredential
+    from azure.identity import DefaultAzureCredential, AzureAuthorityHosts
+    
+    search_endpoint: str = "https://<Put your search service NAME here>.search.windows.net/"
+    credential = AzureKeyCredential("Your search service admin key")
 
-for result in results:
-    print("{}: {}".format(result["HotelId"], result["HotelName"]))
-```
+    index_name: str = "hotels-quickstart-python"
+    ```
+    ---
 
-## Add facets
+1. Remove the following two lines from the **Create an index** code cell. Credentials are already set in the previous code cell.
 
-Facets are generated for positive matches found in search results. There are no zero matches. If search results don't include the term *wifi*, then *wifi* doesn't appear in the faceted navigation structure.
+    ```python
+    from azure.core.credentials import AzureKeyCredential
+    credential = AzureKeyCredential(search_api_key)
+    ```
 
-```python
-# Return facets
-results = search_client.search(search_text="*", facets=["Category"])
+1. Run the **Create an index** code cell to create a search index.
+1. Run the remaining code cells sequentially to load documents and run queries.
 
-facets = results.get_facets()
+## Explaining the code
 
-for facet in facets["Category"]:
-    print("    {}".format(facet))
-```
+### Create an index
 
-## Look up a document
+`SearchIndexClient` is used to create and manage indexes for Azure AI Search. Each field is identified by a `name` and has a specified `type`. 
 
-Return a document based on its key. This operation is useful if you want to provide drill through when a user selects an item in a search result.
+Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
 
-```python
-# Look up a specific document by ID
-result = search_client.get_document(key="3")
+### Create a documents payload and upload documents
 
-print("Details for hotel '3' are:")
-print("Name: {}".format(result["HotelName"]))
-print("Rating: {}".format(result["Rating"]))
-print("Category: {}".format(result["Category"]))
-```
+Use an [index action](/python/api/azure-search-documents/azure.search.documents.models.indexaction) for the operation type, such as upload or merge-and-upload. Documents originate from the [HotelsData](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotels/HotelsData_toAzureSearch.JSON) sample on GitHub.
 
-## Add autocomplete
+### Search an index
 
-Autocomplete can provide potential matches as the user types into the search box.
+You can get query results as soon as the first document is indexed, but actual testing of your index should wait until all documents are indexed.
 
-Autocomplete uses a suggester (`sg`) to know which fields contain potential matches to suggester requests. In this quickstart, those fields are `Tags`, `Address/City`, `Address/Country`. 
+Use the *search* method of the [search.client class](/python/api/azure-search-documents/azure.search.documents.searchclient).
 
-To simulate autocomplete, pass in the letters *sa* as a partial string. The autocomplete method of [SearchClient](/python/api/azure-search-documents/azure.search.documents.searchclient) sends back potential term matches.
+The sample queries in the notebook are:
+- Basic query: Executes an empty search (`search=*`), returning an unranked list (search score = 1.0) of arbitrary documents. Because there are no criteria, all documents are included in results.
+- Term query: Adds whole terms to the search expression ("wifi"). This query specifies that results contain only those fields in the `select` statement. Limiting the fields that come back minimizes the amount of data sent back over the wire and reduces search latency.
+- Filtered query: Add a filter expression, returning only those hotels with a rating greater than four, sorted in descending order.
+- Fielded scoping: Add `search_fields` to scope query execution to specific fields.
+- Facets: Generate facets for positive matches found in search results. There are no zero matches. If search results don't include the term *wifi*, then *wifi* doesn't appear in the faceted navigation structure.
+- Look up a document: Return a document based on its key. This operation is useful if you want to provide drill through when a user selects an item in a search result.
+- Autocomplete: Provide potential matches as the user types into the search box. Autocomplete uses a suggester (`sg`) to know which fields contain potential matches to suggester requests. In this quickstart, those fields are `Tags`, `Address/City`, `Address/Country`. To simulate autocomplete, pass in the letters *sa* as a partial string. The autocomplete method of [SearchClient](/python/api/azure-search-documents/azure.search.documents.searchclient) sends back potential term matches.
 
-```python
-# Autocomplete a query
-search_suggestion = 'sa'
-results = search_client.autocomplete(
-    search_text=search_suggestion, 
-    suggester_name="sg",
-    mode='twoTerms')
+### Remove the index
 
-print("Autocomplete for:", search_suggestion)
-for result in results:
-    print (result['text'])
-```
+If you're finished with this index, you can delete it by running the **Clean up** code cell. Deleting unnecessary indexes frees up space for stepping through more quickstarts and tutorials.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Python用フルテキスト検索ドキュメントの大幅な改訂"
}
```

### Explanation
このコードの変更では、Azure AI Searchを利用したPythonのフルテキスト検索に関するクイックスタートガイドが大幅に改訂されました。具体的には、100行の新たな追加が行われ、269行が削除され、369行が変更された結果、全体の内容が大きく変更されました。

主な改訂点としては、以下の内容が含まれます：
- **日付の更新**: ドキュメントの更新日が12月2日から22日に変更されました。
- **Jupyterノートブックの使用**: サンプルコードを実行するためにJupyterノートブックを使用する方法に焦点が当てられ、Visual Studio Codeの設定は削除されました。
- **環境設定とパッケージインストール**: 新しい手順として、JupyterノートブックとIPythonカーネルのインストール方法が追加され、具体的なコマンドが示されました。
- **コードの簡素化**: インデックスを作成し、ドキュメントをアップロードする具体的なコードブロックや、クエリ実行に関するセクションが詳細化されました。従来の複雑な手順が簡潔に再構成されています。

全体として、この変更はユーザーがAzure AI Searchを使ってより効果的に作業できるように設計されており、特に初学者にとって使いやすくなっています。新しい手法やツールへの移行により、古いコードや手法がworksに影響を及ぼすため、互換性のない変更が含まれています。

## articles/search/includes/quickstarts/full-text-typescript.md{#item-6630e8}

<details>
<summary>Diff</summary>
````diff
@@ -472,7 +472,7 @@ const credential = new AzureKeyCredential(apiKey);
 
 ### Create index
 
-Create a file *hotels_quickstart_index.json*. This file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
+Create a file *hotels_quickstart_index.json*. This file defines how Azure AI Search works with the documents you load in the next step. Each field is identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
 
 We want to import *hotels_quickstart_index.json* so the main function can access the index definition.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScript用フルテキスト検索ドキュメントの軽微な修正"
}
```

### Explanation
この変更は、Azure AI Searchに関するTypeScriptのフルテキスト検索クイックスタートガイドにおいて、軽微な内容の修正が行われたものです。具体的には、文中の表現が「will be identified by」から「is identified by」に変更されたことで、文章が現在形になり、より明確になっています。

変更内容は、次のような文の部分において行われました：

- *hotels_quickstart_index.json* ファイルの説明に関する文の表現が調整され、Azure AI Searchがどのように機能するかを示す際の整合性が向上しました。この修正は、文の流れを改善し、読者にとっての理解を助けることを目的としています。

全体として、この変更は文書の明確性を高めるものであり、特に初学者や文書を参照する開発者に対して、一貫性のある情報提供につながるものです。


