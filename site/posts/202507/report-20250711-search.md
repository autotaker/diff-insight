---
date: '2025-07-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d3417cf...MicrosoftDocs:d3061a3
summary: |-
  以下のドキュメントに対する変更概要は次の通りです。

  新機能として、ODataフルテキスト検索関数の説明が改善され、ASP.NET Core MVCの検索アプリケーションチュートリアルが最新の.NET 9.0に更新されました。破壊的変更は特にありませんが、利用者には最新のドキュメントに従うことを推奨します。また、ドキュメントレイアウトスキルやマルチテナントSaaSアプリケーションの検索モデルに関する表現も改善されています。これらの更新により、技術者や開発者はより効率的にサービスを利用し、アプリケーション開発を進めることができるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d3417cf...MicrosoftDocs:d3061a3){target="_blank"}

# ハイライト

以下のドキュメントに対する変更が行われました：

## 新機能

- ODataフルテキスト検索関数に大幅な更新が加えられ、`search.ismatch`と`search.ismatchscoring`関数の使用方法がより明確に説明されています。
- ASP.NET Core MVCの検索アプリケーションチュートリアルが最新の.NET 9.0に更新され、プロジェクト設定に関する手順が改善されました。

## 破壊的変更

- 重大な破壊的変更はありません。しかし、コードの利用に関する具体的な変更があるため、利用者はドキュメントを最新のものに従うことが推奨されます。

## その他の更新

- ドキュメントレイアウトスキルとマルチテナントSaaSアプリケーションの検索モデルに関する文書がわずかに改善され、表現の明確化が図られました。

# 洞察

Azureのドキュメントの最近の更新では、技術者や開発者がより簡単かつ正確にサービスを利用できるように、ドキュメントの内容が精緻化されています。特に、ODataのフルテキスト検索に関する部分では、従来よりも詳しい使用例と構文が提供されるようになり、ユーザーが検索クエリを構築する際の誤解を減らし、効率的に開発を行う手助けとなっています。

また、ASP.NET Core MVCアプリケーションのチュートリアルが更新され、最新の.NET 9.0に対応したことは、開発者が最新のテクノロジースタックを使用してアプリケーションを構築できるようにするための重要な改良です。これにより、新しい.NET機能を活用しつつ、Azure AI Searchをアプリケーションに統合することが容易になります。

これらの更新により、AzureのAIおよび検索ソリューションを活用したアプリケーション開発がさらに促進され、ユーザーフレンドリーなインターフェースを通じてより迅速にビジネスニーズに応えられる環境が整えられつつあると言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-document-intelligence-layout.md](#item-62c06f) | minor update | ドキュメントレイアウトスキルの最新情報 | modified | 7 | 7 | 14 | 
| [search-modeling-multitenant-saas-applications.md](#item-da3840) | minor update | マルチテナントSaaSアプリケーションの検索モデルに関する更新 | modified | 1 | 1 | 2 | 
| [search-query-odata-full-text-search-functions.md](#item-5748d4) | major update | ODataフルテキスト検索関数に関する大幅な改訂 | modified | 209 | 28 | 237 | 
| [tutorial-csharp-create-mvc-app.md](#item-608a5d) | minor update | ASP.NET Core MVCアプリ作成チュートリアルの更新 | modified | 6 | 9 | 15 | 


# Modified Contents
## articles/search/cognitive-search-skill-document-intelligence-layout.md{#item-62c06f}

<details>
<summary>Diff</summary>
````diff
@@ -11,14 +11,14 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: reference
-ms.date: 06/10/2025
+ms.date: 07/10/2025
 ---
 
 # Document Layout skill
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-The **Document Layout** skill analyzes a document to detect structure and characteristics, and produces a syntactical representation of the document in Markdown or Text format. You can use it to extract text and images, where image extraction includes location metadata that preserves image position within the document. Image proximity to related content adds value to Retrieval Augmented Generation (RAG) workloads and [multimodal search](multimodal-search-overview.md).
+The **Document Layout** skill analyzes a document to detect structure and characteristics, and produces a syntactical representation of the document in Markdown or Text format. You can use it to extract text and images, where image extraction includes location metadata that preserves image position within the document. Image proximity to related content is beneficial in Retrieval Augmented Generation (RAG) workloads and [multimodal search](multimodal-search-overview.md) scenarios.
 
 This article is the reference documentation for the Document Layout skill. For usage information, see [How to chunk and vectorize by document layout](search-how-to-semantic-chunking.md). 
 
@@ -46,11 +46,11 @@ The Document Layout skill calls the [Document Intelligence Public preview versio
 
 Supported regions vary by modality and how the skill connects to the Document Intelligence layout model.
 
-| Approach | Regions | Requirement |
-|----------|---------|-------------|
-| [Import and vectorize data wizard](search-import-data-portal.md) | **East US**, **West Europe**, **North Central US** | Create an Azure AI multi-service resource in one of these regions to get the portal experience. |
-| Programmatic, using a [keyless connection (preview)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) for billing | Varies by resource | Create Azure AI Search in one of these regions:  **East US**, **West Europe**, **North Central US**, **West US 2**. <br>Access Document Intelligence through an Azure AI multi-service resource in any region listed in the [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table) table.|
-| Programmatic, using a [multi-service resource API key](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) for billing | **East US**, **West Europe**, **North Central US**, **West US 2** | Create your Azure AI Search service and AI multi-service resource in the same region. |
+| Approach | Requirement |
+|----------|-------------|
+| [Import and vectorize data wizard](search-import-data-portal.md) | Create an Azure AI multi-service resource in one of these regions to get the portal experience: **East US**, **West Europe**, **North Central US**. | 
+| Programmatic, using [Microsoft Entra ID authentication (preview)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) for billing |  Create Azure AI Search in one of these regions:  **East US**, **West Europe**, **North Central US**, **West US 2**. <br>Create the Azure AI multi-service resource in any region listed in the [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table) table.|
+| Programmatic, using a [multi-service resource API key](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) for billing | Create your Azure AI Search service and AI multi-service resource in the same region: **East US**, **West Europe**, **North Central US**, **West US 2**. |
 
 ## Supported file formats
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントレイアウトスキルの最新情報"
}
```

### Explanation
この変更は、Azure AI の「ドキュメントレイアウト」スキルに関する文書に対するマイナーな更新を示しています。主な変更内容は更新された日付の修正と文章の一部における表現の調整です。具体的には、`ms.date`が2025年6月10日から2025年7月10日に変更され、文中の「関連コンテンツに対する画像の近接性の価値が増す」という表現が「関連コンテンツに対する画像の近接性が有益である」という形に変更されました。

さらに、ドキュメントには新しいセクションの追加が行われ、スキルの使い方や条件についての要件がより明確になりました。これにより、ユーザーはドキュメントレイアウトスキルの利用に際して必要な情報をより簡単に理解できるようになります。

## articles/search/search-modeling-multitenant-saas-applications.md{#item-da3840}

<details>
<summary>Diff</summary>
````diff
@@ -80,7 +80,7 @@ In the case of a multitenant scenario, the application developer consumes one or
 
 In an index-per-tenant model, multiple tenants occupy a single Azure AI Search service where each tenant has their own index.
 
-Tenants achieve data isolation because all search requests and document operations are issued at an index level in Azure AI Search. In the application layer, there's the need awareness to direct the various tenants’ traffic to the proper indexes while also managing resources at the service level across all tenants.
+This approach works because all search requests and document operations are issued at an index level in Azure AI Search. In the application layer, there's the need awareness to direct the various tenants’ traffic to the proper indexes while also managing resources at the service level across all tenants.
 
 A key attribute of the index-per-tenant model is the ability for the application developer to oversubscribe the capacity of a search service among the application’s tenants. If the tenants have an uneven distribution of workload, the optimal combination of tenants can be distributed across a search service’s indexes to accommodate a number of highly active, resource-intensive tenants while simultaneously serving a long tail of less active tenants. The trade-off is the inability of the model to handle situations where each tenant is concurrently highly active.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチテナントSaaSアプリケーションの検索モデルに関する更新"
}
```

### Explanation
この変更は、マルチテナントSaaSアプリケーションにおける検索モデルに関する文書のマイナーな更新を示しています。具体的には、文中の表現が修正され、「テナントはAzure AI Searchのインデックスレベルで全ての検索リクエストとドキュメント操作を発行するため、データの隔離が実現される」というフレーズが、「このアプローチは、全ての検索リクエストとドキュメント操作がAzure AI Searchのインデックスレベルで発行されるため、実現される」と修正されました。

この修正によって、文の流れがより明確になり、テナント間のデータ隔離の仕組みを理解しやすくなっています。文章の他の部分には変更はないため、内容の全体的な意味は変わっていませんが、より明瞭な表現に改善されています。

## articles/search/search-query-odata-full-text-search-functions.md{#item-5748d4}

<details>
<summary>Diff</summary>
````diff
@@ -10,25 +10,15 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: reference
-ms.date: 09/16/2021
-translation.priority.mt:
-  - "de-de"
-  - "es-es"
-  - "fr-fr"
-  - "it-it"
-  - "ja-jp"
-  - "ko-kr"
-  - "pt-br"
-  - "ru-ru"
-  - "zh-cn"
-  - "zh-tw"
+ms.date: 07/10/2025
+
 ---
 # OData full-text search functions in Azure AI Search - `search.ismatch` and `search.ismatchscoring`
 
-Azure AI Search supports full-text search in the context of [OData filter expressions](query-odata-filter-orderby-syntax.md) via the `search.ismatch` and `search.ismatchscoring` functions. These functions allow you to combine full-text search with strict Boolean filtering in ways that are not possible just by using the top-level `search` parameter of the [Search API](/rest/api/searchservice/documents/search-post).
+Azure AI Search supports full-text search in the context of [OData filter expressions](query-odata-filter-orderby-syntax.md) via the `search.ismatch` and `search.ismatchscoring` functions. These functions allow you to combine full-text search with strict Boolean filtering in ways that aren't possible just by using the top-level `search` parameter of the [Search API](/rest/api/searchservice/documents/search-post).
 
 > [!NOTE]
-> The `search.ismatch` and `search.ismatchscoring` functions are only supported in filters in the [Search API](/rest/api/searchservice/documents/search-post). They are not supported in the [Suggest](/rest/api/searchservice/documents/suggest-post) or [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) APIs.
+> The `search.ismatch` and `search.ismatchscoring` functions are only supported in filters in the [Search API](/rest/api/searchservice/documents/search-post). They aren't supported in the [Suggest](/rest/api/searchservice/documents/suggest-post) or [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) APIs.
 
 ## Syntax
 
@@ -58,7 +48,7 @@ An interactive syntax diagram is also available:
 
 ### search.ismatch
 
-The `search.ismatch` function evaluates a full-text search query as a part of a filter expression. The documents that match the search query will be returned in the result set. The following overloads of this function are available:
+The `search.ismatch` function evaluates a full-text search query as a part of a filter expression. Matching documents are returned in the result set. The following overloads of this function are available:
 
 - `search.ismatch(search)`
 - `search.ismatch(search, searchFields)`
@@ -69,21 +59,20 @@ The parameters are defined in the following table:
 | Parameter name | Type | Description |
 | --- | --- | --- |
 | `search` | `Edm.String` | The search query (in either [simple](query-simple-syntax.md) or [full](query-lucene-syntax.md) Lucene query syntax). |
-| `searchFields` | `Edm.String` | Comma-separated list of searchable fields to search in; defaults to all searchable fields in the index. When using [fielded search](query-lucene-syntax.md#bkmk_fields) in the `search` parameter, the field specifiers in the Lucene query override any fields specified in this parameter. |
+| `searchFields` | `Edm.String` | Comma-separated list of searchable fields to search in; defaults to all searchable fields in the index. When you use [fielded search](query-lucene-syntax.md#bkmk_fields) in the `search` parameter, the field specifiers in the Lucene query override any fields specified in this parameter. |
 | `queryType` | `Edm.String` | `'simple'` or `'full'`; defaults to `'simple'`. Specifies what query language was used in the `search` parameter. |
-| `searchMode` | `Edm.String` | `'any'` or `'all'`, defaults to `'any'`. Indicates whether any or all of the search terms in the `search` parameter must be matched in order to count the document as a match. When using the [Lucene Boolean operators](query-lucene-syntax.md#bkmk_boolean) in the `search` parameter, they will take precedence over this parameter. |
+| `searchMode` | `Edm.String` | `'any'` or `'all'`, defaults to `'any'`. Indicates whether any or all of the search terms in the `search` parameter must be matched in order to count the document as a match. When you use the [Lucene Boolean operators](query-lucene-syntax.md#bkmk_boolean) in the `search` parameter, they take precedence over this parameter. |
 
 All the above parameters are equivalent to the corresponding [search request parameters in the Search API](/rest/api/searchservice/documents/search-post).
 
-The `search.ismatch` function returns a value of type `Edm.Boolean`, which allows you to compose it with other filter sub-expressions using the Boolean [logical operators](search-query-odata-logical-operators.md).
+The `search.ismatch` function returns a value of type `Edm.Boolean`, which allows you to compose it with other filter subexpressions using the Boolean [logical operators](search-query-odata-logical-operators.md).
 
 > [!NOTE]
-> Azure AI Search does not support using `search.ismatch` or `search.ismatchscoring` inside lambda expressions. This means it is not possible to write filters over collections of objects that can correlate full-text search matches with strict filter matches on the same object. For more details on this limitation as well as examples, see [Troubleshooting collection filters in Azure AI Search](search-query-troubleshoot-collection-filters.md). For more in-depth information on why this limitation exists, see [Understanding collection filters in Azure AI Search](search-query-understand-collection-filters.md).
-
+> Azure AI Search doesn't support using `search.ismatch` or `search.ismatchscoring` inside lambda expressions. This means it isn't possible to write filters over collections of objects that can correlate full-text search matches with strict filter matches on the same object. For more information on this limitation as well as examples, see [Troubleshooting collection filters in Azure AI Search](search-query-troubleshoot-collection-filters.md). For more in-depth information on why this limitation exists, see [Understanding collection filters in Azure AI Search](search-query-understand-collection-filters.md).
 
 ### search.ismatchscoring
 
-The `search.ismatchscoring` function, like the `search.ismatch` function, returns `true` for documents that match the full-text search query passed as a parameter. The difference between them is that the relevance score of documents matching the `search.ismatchscoring` query will contribute to the overall document score, while in the case of `search.ismatch`, the document score won't be changed. The following overloads of this function are available with parameters identical to those of `search.ismatch`:
+The `search.ismatchscoring` function, like the `search.ismatch` function, returns `true` for documents that match the full-text search query passed as a parameter. The difference between them is that the relevance score of documents matching the `search.ismatchscoring` query contributes to the overall document score, whereas for `search.ismatch`, the document score doesn't change. The following overloads of this function are available with parameters identical to those of `search.ismatch`:
 
 - `search.ismatchscoring(search)`
 - `search.ismatchscoring(search, searchFields)`
@@ -99,10 +88,36 @@ Find documents with the word "waterfront". This filter query is identical to a [
     search.ismatchscoring('waterfront')
 ```
 
-Find documents with the word "hostel" and rating greater or equal to 4, or documents with the word "motel" and rating equal to 5. Note, this request could not be expressed without the `search.ismatchscoring` function.
+Here's the full query syntax for this request, which you can run in Search Explorer in the Azure portal. Output consists of matches on waterfront, water, and front.
+
+```json
+{
+  "search": "*",
+  "select": "HotelId, HotelName, Description",
+  "searchMode": "all",
+  "queryType": "simple",
+  "count": true,
+  "filter": "search.ismatchscoring('waterfront')"
+}
+```
+
+Find documents with the word "pool" and rating greater or equal to 4, or documents with the word "motel" and equal to 3.2. Note, this request couldn't be expressed without the `search.ismatchscoring` function.
 
 ```odata-filter-expr
-    search.ismatchscoring('hostel') and Rating ge 4 or search.ismatchscoring('motel') and Rating eq 5
+    search.ismatchscoring('pool') and Rating ge 4 or search.ismatchscoring('motel') and Rating eq 3.2
+```
+
+Here's the full query syntax for this request for Search Explorer. Output consists of matches on hotels with pools having a rating greater than 4, *or* motels with a rating equal to 3.2.
+
+```json
+{
+  "search": "*",
+  "select": "HotelId, HotelName, Description, Tags, Rating",
+  "searchMode": "all",
+  "queryType": "simple",
+  "count": true,
+  "filter": "search.ismatchscoring('pool') and Rating ge 4 or search.ismatchscoring('motel') and Rating eq 3.2"
+}
 ```
 
 Find documents without the word "luxury".
@@ -111,26 +126,192 @@ Find documents without the word "luxury".
     not search.ismatch('luxury')
 ```
 
-Find documents with the phrase "ocean view" or rating equal to 5. The `search.ismatchscoring` query will be executed only against fields `HotelName` and `Rooms/Description`.
+Here's the full query syntax for this request. Output consists of matches on the term luxury.
+
+```json
+{
+  "search": "*",
+  "select": "HotelId, HotelName, Description, Tags, Rating",
+  "searchMode": "all",
+  "queryType": "simple",
+  "count": true,
+  "filter": "not search.ismatch('luxury')"
+}
+```
 
-Documents that matched only the second clause of the disjunction will be returned too -- hotels with `Rating` equal to 5. To make it clear that those documents didn't match any of the scored parts of the expression, they will be returned with score equal to zero.
+Find documents with the phrase "ocean" or rating equal to 3.2. The `search.ismatchscoring` query is executed only against fields `HotelName` and `Description`.
 
-```odata-filter-expr
-    search.ismatchscoring('"ocean view"', 'Rooms/Description,HotelName') or Rating eq 5
+Here's the full query syntax for this request. Documents that match only the second clause of the disjunction are returned too (specifically, hotels with `Rating` equal to `3.2`). To make it clear that those documents didn't match any of the scored parts of the expression, they're returned with score equal to zero.
+
+```json
+{
+  "search": "*",
+  "select": "HotelId, HotelName, Description, Rating",
+  "searchMode": "all",
+  "queryType": "full",
+  "count": true,
+  "filter": "search.ismatchscoring('ocean', 'Description,HotelName') or Rating eq 3.2"
+}
 ```
 
-Find documents where the terms "hotel" and "airport" are within 5 words from each other in the description of the hotel, and where smoking is not allowed in at least some of the rooms. This query uses the [full Lucene query language](query-lucene-syntax.md).
+Output consists of 4 matches: hotels that mention "ocean" in the Description or Hotel Name, or hotels with a rating of 3.2. Notice the search score of zero for matches on the second clause.
+
+```json
+{
+  "@odata.count": 4,
+  "value": [
+    {
+      "@search.score": 1.6076145,
+      "HotelId": "18",
+      "HotelName": "Ocean Water Resort & Spa",
+      "Description": "New Luxury Hotel for the vacation of a lifetime. Bay views from every room, location near the pier, rooftop pool, waterfront dining & more.",
+      "Rating": 4.2
+    },
+    {
+      "@search.score": 1.0594962,
+      "HotelId": "41",
+      "HotelName": "Windy Ocean Motel",
+      "Description": "Oceanfront hotel overlooking the beach features rooms with a private balcony and 2 indoor and outdoor pools. Inspired by the natural beauty of the island, each room includes an original painting of local scenes by the owner. Rooms include a mini fridge, Keurig coffee maker, and flatscreen TV. Various shops and art entertainment are on the boardwalk, just steps away.",
+      "Rating": 3.5
+    },
+    {
+      "@search.score": 0,
+      "HotelId": "40",
+      "HotelName": "Trails End Motel",
+      "Description": "Only 8 miles from Downtown. On-site bar/restaurant, Free hot breakfast buffet, Free wireless internet, All non-smoking hotel. Only 15 miles from airport.",
+      "Rating": 3.2
+    },
+    {
+      "@search.score": 0,
+      "HotelId": "26",
+      "HotelName": "Planetary Plaza & Suites",
+      "Description": "Extend Your Stay. Affordable home away from home, with amenities like free Wi-Fi, full kitchen, and convenient laundry service.",
+      "Rating": 3.2
+    }
+  ]
+}
+```
+
+Find documents where the terms "hotel" and "airport" are within 5 words from each other in the description of the hotel, and where smoking isn't allowed in at least some of the rooms.
 
 ```odata-filter-expr
     search.ismatch('"hotel airport"~5', 'Description', 'full', 'any') and Rooms/any(room: not room/SmokingAllowed)
 ```
 
+Here's the full query syntax. To run in Search Explorer, escape the interior quotation marks with a backslash character.
+
+```json
+{
+  "search": "*",
+  "select": "HotelId, HotelName, Description, Tags, Rating",
+  "searchMode": "all",
+  "queryType": "simple",
+  "count": true,
+  "filter": "search.ismatch('\"hotel airport\"~5', 'Description', 'full', 'any') and Rooms/any(room: not room/SmokingAllowed)"
+}
+```
+
+Output consists of a single document where the terms "hotel" and "airport" are within 5 words distance. Smoking is allowed for several rooms in most hotels, including the one in this search result.
+
+```json
+{
+  "@odata.count": 1,
+  "value": [
+    {
+      "@search.score": 1,
+      "HotelId": "40",
+      "HotelName": "Trails End Motel",
+      "Description": "Only 8 miles from Downtown. On-site bar/restaurant, Free hot breakfast buffet, Free wireless internet, All non-smoking hotel. Only 15 miles from airport.",
+      "Tags": [
+        "bar",
+        "free wifi",
+        "restaurant"
+      ],
+      "Rating": 3.2
+    }
+  ]
+}
+```
+
 Find documents that have a word that starts with the letters "lux" in the Description field. This query uses [prefix search](query-simple-syntax.md#prefix-queries) in combination with `search.ismatch`.
 
 ```odata-filter-expr
     search.ismatch('lux*', 'Description')
 ```
 
+Here's a full query:
+
+```json
+{
+  "search": "*",
+  "select": "HotelId, HotelName, Description, Tags, Rating",
+  "searchMode": "all",
+  "queryType": "simple",
+  "count": true,
+  "filter": "search.ismatch('lux*', 'Description')"
+}
+```
+
+Output consists of the following matches.
+
+```json
+{
+  "@odata.count": 4,
+  "value": [
+    {
+      "@search.score": 1,
+      "HotelId": "18",
+      "HotelName": "Ocean Water Resort & Spa",
+      "Description": "New Luxury Hotel for the vacation of a lifetime. Bay views from every room, location near the pier, rooftop pool, waterfront dining & more.",
+      "Tags": [
+        "view",
+        "pool",
+        "restaurant"
+      ],
+      "Rating": 4.2
+    },
+    {
+      "@search.score": 1,
+      "HotelId": "13",
+      "HotelName": "Luxury Lion Resort",
+      "Description": "Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort.",
+      "Tags": [
+        "bar",
+        "concierge",
+        "restaurant"
+      ],
+      "Rating": 4.1
+    },
+    {
+      "@search.score": 1,
+      "HotelId": "16",
+      "HotelName": "Double Sanctuary Resort",
+      "Description": "5 star Luxury Hotel - Biggest Rooms in the city. #1 Hotel in the area listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso in room.",
+      "Tags": [
+        "view",
+        "pool",
+        "restaurant",
+        "bar",
+        "continental breakfast"
+      ],
+      "Rating": 4.2
+    },
+    {
+      "@search.score": 1,
+      "HotelId": "14",
+      "HotelName": "Twin Vortex Hotel",
+      "Description": "New experience in the making. Be the first to experience the luxury of the Twin Vortex. Reserve one of our newly-renovated guest rooms today.",
+      "Tags": [
+        "bar",
+        "restaurant",
+        "concierge"
+      ],
+      "Rating": 4.4
+    }
+  ]
+}
+```
+
 ## Next steps  
 
 - [Filters in Azure AI Search](search-filters.md)
````
</details>

### Summary

```json
{
    "modification_type": "major update",
    "modification_title": "ODataフルテキスト検索関数に関する大幅な改訂"
}
```

### Explanation
この変更は、Azure AI SearchにおけるODataフルテキスト検索関数（`search.ismatch`および`search.ismatchscoring`）に関する文書の大幅な更新を示しています。変更には、全体で209行の追加と28行の削除が含まれ、237行の変更が行われました。

主な更新内容としては、文書の日付が2021年9月16日から2025年7月10日に変更され、関数の説明や構文に関する情報が追加されています。文中の文章が改善され、より自然な表現が用いられるようになっています。また、各関数の具体的な使用例やJSON形式での実際のクエリ構文が詳細に記載されており、ユーザーがこれらの関数をより効果的に利用できるようになっています。

特に、`search.ismatch`および`search.ismatchscoring`関数を使用する方法について、新しいクエリ例やその出力が具体的に説明されており、ユーザーにとっての実用性が高まっています。この変更により、ユーザーはこれらの関数の利用方法を明確に理解できるようになり、実装時の混乱を軽減できるでしょう。

## articles/search/tutorial-csharp-create-mvc-app.md{#item-608a5d}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.devlang: csharp
 ms.custom:
   - ignite-2023
 ms.topic: tutorial
-ms.date: 01/17/2025
+ms.date: 07/10/2025
 ---
 
 # Create a search app in ASP.NET Core
@@ -45,9 +45,9 @@ Sample code for this tutorial can be found in the [azure-search-dotnet-samples](
 
 1. Provide a project name, and then select **Next**.
 
-1. On the next page, select **.NET 6.0** or **.NET 7.0** or **.NET 8.0**.
+1. On the next page, select **.NET 9.0**.
 
-1. Verify that **Do not use top-level statements** is unchecked.
+1. Accept the defaults.
 
 1. Select **Create**.
 
@@ -74,7 +74,7 @@ Modify `appsettings.json` to specify your search service and [query API key](sea
 
 You can get the service URL and API key from the Azure portal. Because this code is querying an index and not creating one, you can use a query key instead of an admin key.
 
-Make sure to specify the search service that has the hotels-sample-index.
+Make sure to specify a search service that has the hotels-sample-index.
 
 ## Add models
 
@@ -476,11 +476,8 @@ In the hotels-sample-index, sortable fields include Rating and LastRenovated. Th
 
 For more information about sorting, see [OData $orderby syntax in Azure AI Search](search-query-odata-orderby.md).
 
-## Next steps
+## Next step
 
 In this tutorial, you created an ASP.NET Core (MVC) project that connected to a search service and called Search APIs for server-side filtering and sorting.
 
-If you want to explore client-side code that responds to user actions, consider adding a React template to your solution:
-
-> [!div class="nextstepaction"]
-> [C# Tutorial: Add search to a website with .NET](tutorial-csharp-overview.md)
+To add client-side code that responds to user actions, use a React template in your solution: [C# Tutorial: Add search to a website with .NET](tutorial-csharp-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ASP.NET Core MVCアプリ作成チュートリアルの更新"
}
```

### Explanation
この変更は、ASP.NET Coreでの検索アプリ作成に関するチュートリアルのマイナーな更新を示しています。具体的には、文書の日付が2025年1月17日から2025年7月10日に変更され、使用する.NETのバージョンが6.0、7.0、8.0から9.0に更新されました。

また、プロジェクト設定の手順や文中の説明が改善されました。たとえば、「デフォルトを受け入れる」という新しい指示が追加され、読者がより簡単にプロジェクトを作成できるようになっています。さらに、最後のセクションでは、クライアントサイドのコードを追加するためにReactテンプレートを使用することを提案する文言が明確に修正され、フローがスムーズになりました。

これにより、チュートリアルの内容は最新の技術スタックに合わせて最適化され、開発者がAzure AI Searchを利用して検索機能を効果的に実装できるようになっています。


