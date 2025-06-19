---
date: '2025-06-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2e48ee2...MicrosoftDocs:1531236
summary: 'このコードの差分は、Azure AIドキュメントにおける「検索入門: ベクトル検索」と「SharePoint Onlineのインデックス設定手法」の記事に対するマイナーアップデートを含んでいます。主な変更点として、新しいAPIバージョンへの移行や認証方法の変更（Bearerトークンの導入）、インデックス設定に関する詳細調整が行われました。特に、両記事の表現が改善され、クエリの説明や使用法が明確化されました。これにより、ユーザーは検索機能をより効果的に理解し、利用できることが期待されています。'
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2e48ee2...MicrosoftDocs:1531236){target="_blank"}

# Highlights
このコードの差分は、Azure AIドキュメントにおける2つの記事に対するマイナーアップデートを含んでいます。「検索入門: ベクトル検索」および「SharePoint Onlineのインデックス設定手法」についての更新です。特に、新しいAPIバージョンへの移行、認証方法の変更、およびインデックス設定の詳細に関する調整がなされました。

## New features
- ベクトル検索の記事では、新しい認証方法として「Bearerトークン」が導入されました。
- SharePoint Onlineの記事で、ユーザー向けに簡潔な使用方法説明とプレビュー機能登録の明確化が行われました。

## Breaking changes
- 特に重大な破壊的変更は見られませんが、APIバージョンのアップデートや認証方法の変更により、既存の設定やコードが影響を受ける可能性があります。

## Other updates
- 両記事ともに、テキストの表現を自然でわかりやすくするための改善が行われました。
- クエリの説明や例の整備がなされ、実際の使用におけるガイドとしての質が向上しました。

# Insights
今回のドキュメント更新は、Azure AIの検索機能利用を促進するためのものです。ユーザーがより効率的に理解し、活用できるよう、技術的な要素とユーザーエクスペリエンスの両方に配慮した変更が行われています。

ベクトル検索の記事では、特に認証方法の変更が注目されます。従来のAPIキーから、よりセキュアな「Bearerトークン」への移行は、セキュリティの強化を意図したものです。これによりユーザーは、認証の自動化や管理をより厳格に行うことができるでしょう。

一方、SharePoint Onlineの記事では、インデックス設定に関する具体的な説明が整理されました。特に、削除や増分インデックスに関する情報が強調され、ユーザーの期待を明確にすることが狙いです。また、最新のAPIバージョンにより、ユーザーは新しいMicrosoft Entraによる認証手順を用いることが可能となり、最新の方法でデータインデックスを管理することが求められます。

これらの変更は、最終的にはAzureユーザーの機能理解を深め、検索機能の利用を容易にすることを目的としています。ユーザーは、今後の予定や制約、最新の認証手順を確実に理解し、効率的な運用を行うことが求められる場面が増加することでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-get-started-vector.md](#item-4984d9) | minor update | 検索入門 - ベクトル検索のアップデート | modified | 86 | 186 | 272 | 
| [search-howto-index-sharepoint-online.md](#item-49ff6e) | minor update | SharePoint Online のインデックス設定手法に関する更新 | modified | 53 | 61 | 114 | 


# Modified Contents
## articles/search/search-get-started-vector.md{#item-4984d9}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: quickstart
-ms.date: 06/12/2025
+ms.date: 06/18/2025
 ---
 
 # Quickstart: Vector search using REST
@@ -96,12 +96,11 @@ You use one `.rest` or `.http` file to run all the requests in this quickstart.
 
 1. For the **recommended** keyless authentication via Microsoft Entra ID, you need to replace `api-key: {{apiKey}}` with `Authorization: Bearer {{token}}` in the request headers. Replace all instances of `api-key: {{apiKey}}` that you find in the file.
 
-
 ## Create a vector index
 
 You use the [Create Index](/rest/api/searchservice/indexes/create) REST API to create a vector index and set up the physical data structures on your search service.
 
-The index schema in this example is organized around hotel content. Sample data consists of vector and nonvector names and descriptions of fictitious hotels. This schema includes configurations for vector indexing and queries, and for semantic ranking.
+The index schema in this example is organized around hotel content. Sample data consists of vector and nonvector descriptions of fictitious hotels. This schema includes configurations for vector indexing and queries, and for semantic ranking.
 
 1. In Visual Studio Code, open the `az-search-vector-quickstart.rest` file you [created earlier](#create-or-download-the-code-file).
 
@@ -110,7 +109,7 @@ The index schema in this example is organized around hotel content. Sample data
 
     ```http
     ### Create a new index
-    POST  {{baseUrl}}/indexes?api-version=2023-11-01  HTTP/1.1
+    POST  {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
     Content-Type: application/json
     Authorization: Bearer {{token}}
 
@@ -387,7 +386,7 @@ Key takeaways about the [Create Index](/rest/api/searchservice/indexes/create) R
 
 - The `fields` collection includes a required key field and text and vector fields (such as `Description` and `DescriptionVector`) for text and vector search. Colocating vector and nonvector fields in the same index enables hybrid queries. For instance, you can combine filters, text search with semantic ranking, and vectors into a single query operation.
 
-- Vector fields must be `type: Collection(Edm.Single)` with `dimensions` and `vectorSearchProfile` properties.
+- Vector fields must be one of the [EDM data types used for vectors](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields), such as `type: Collection(Edm.Single)`. Vector fields also have `dimensions` and `vectorSearchProfile` properties.
 
 - The `vectorSearch` section is an array of approximate nearest neighbor algorithm configurations and profiles. Supported algorithms include hierarchical navigable small world and exhaustive k-nearest neighbor. For more information, see [Relevance scoring in vector search](vector-search-ranking.md).
 
@@ -652,7 +651,7 @@ Key takeaways about the [Documents - Index REST API](/rest/api/searchservice/doc
 
 ## Run queries
 
-Now that documents are loaded, you can issue vector queries against them by using [Documents - Search Post (REST)](/rest/api/searchservice/documents/search-post).
+Now that documents are loaded, you can run vector queries against them by using [Documents - Search Post (REST)](/rest/api/searchservice/documents/search-post).
 
 In the next sections, we run queries against the `hotels-vector-quickstart` index. The queries include:
 
@@ -661,7 +660,7 @@ In the next sections, we run queries against the `hotels-vector-quickstart` inde
 - [Hybrid search](#hybrid-search)
 - [Semantic hybrid search](#semantic-hybrid-search)
 
-The example vector queries are based on two strings:
+The example queries are based on two strings:
 
 - **Search string**: `historic hotel walk to restaurants and shopping`
 - **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
@@ -693,9 +692,15 @@ The vector query string is semantically similar to the search string, but it inc
         }
     ```
 
-    The `vectorQueries.vector` contains the vectorized text of the query input, `fields` determines which vector fields are searched, and `k` specifies the number of nearest neighbors to return.
+   Key takeaways about the [Documents - Search Post](/rest/api/searchservice/documents/search-post) REST API:
+
+    + The `vectorQueries.vector` is the vector query string. It's a vector representation of *quintessential lodging near running trails, eateries, retail*, which is vectorized into 1,536 embeddings for this query.
+
+    + `fields` determines which vector fields are searched.
 
-    The query is a vector representation of *quintessential lodging near running trails, eateries, retail*, which is vectorized into 1,536 embeddings for this query.
+    + `kind` set to `vector` means that the query string is a vector. If `kind` was set to `text`, you would need extra capability (a [vectorizer]()) to encode a human readable text string into a vector at query time. Vectorizers are omitted from this quickstart to keep the exercise simple.
+
+    + `k` specifies the number of nearest neighbors to return in the response. A `count` parameter specifies the number of matches found in the index. Including count is a best practice for queries, but it's less useful for similarity search where the algorithm can find some degree of similarity in almost any document. 
 
 1. Select **Send request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
 
@@ -838,7 +843,7 @@ You can add filters, but the filters are applied to the nonvector content in you
     }
     ```
 
-1. Here's another query that uses a geo-filter, limiting results to hotels within 500 kilometers around Washington D.C.
+1. Here's another query that uses a geo-filter, limiting results to hotels within 300 kilometers around Washington D.C.
 
     ```http
     ### Run a vector query with a geo filter
@@ -848,7 +853,7 @@ You can add filters, but the filters are applied to the nonvector content in you
     
         {
             "count": true,
-            "select": "HotelId, HotelName, Category, Description,Address/City, Address/StateProvince"",
+            "select": "HotelId, HotelName, Description, Address/City, Address/StateProvince",
             "top": 5,
             "facets": [ "Address/StateProvince"],
             "filter": "geo.distance(Location, geography'POINT(-77.03241 38.90166)') le 300",
@@ -868,41 +873,37 @@ You can add filters, but the filters are applied to the nonvector content in you
 1. Review the response. It's limited to two hotels near Washington D.C, with a facet structure providing the aggregation.
 
     ```json
-      "@odata.count": 2,
-      "@search.facets": {
-        "Address/StateProvince": [
-          {
-            "value": "VA",
-            "count": 1
-          }
-        ]
-      },
-      "value": [
-        {
-          "@search.score": 0.6605852246284485,
-          "HotelId": "48",
-          "HotelName": "Nordick's Valley Motel",
-          "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
-          "Category": "Boutique",
-          "Tags": [
-            "continental breakfast",
-            "air conditioning",
-            "free wifi"
-          ]
-        },
+    "@odata.count": 2,
+    "@search.facets": {
+      "Address/StateProvince": [
         {
-          "@search.score": 0.602634072303772,
-          "HotelId": "49",
-          "HotelName": "Swirling Currents Hotel",
-          "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary W-Fi and flat-screen TVs.",
-          "Category": "Suite",
-          "Tags": [
-            "air conditioning",
-            "laundry service",
-            "24-hour front desk service"
-          ]
+          "value": "VA",
+          "count": 1
         }
       ]
+    },
+    "value": [
+      {
+        "@search.score": 0.6605852246284485,
+        "HotelId": "48",
+        "HotelName": "Nordick's Valley Motel",
+        "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
+        "Address": {
+          "City": "Washington D.C.",
+          "StateProvince": null
+        }
+      },
+      {
+        "@search.score": 0.602634072303772,
+        "HotelId": "49",
+        "HotelName": "Swirling Currents Hotel",
+        "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary W-Fi and flat-screen TVs.",
+        "Address": {
+          "City": "Arlington",
+          "StateProvince": "VA"
+        }
+      }
+    ]
     ```
 
 ### Hybrid search
@@ -939,181 +940,96 @@ Hybrid search consists of keyword queries and vector queries in a single search
 
 1. Select **Send request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
 
-Because this is a hybrid query, results are [ranked by Reciprocal Rank Fusion (RRF)](hybrid-search-ranking.md). RRF evaluates search scores of multiple search results, takes the inverse, and then merges and sorts the combined results. The `top` number of results are returned.
+Because this is a hybrid query, results are [ranked by Reciprocal Rank Fusion (RRF)](hybrid-search-ranking.md#scores-in-a-hybrid-search-results). Notice that `@search.score` values have a different basis and are uniformly smaller values. RRF evaluates search scores of multiple search results, takes the inverse, and then merges and sorts the combined results. The `top` number of results are returned.
 
-Review the response:
+Review the response, consisting of the top k-5 matches out of 7 matching documents in the index:
 
 ```json
 {
   "@odata.count": 7,
   "value": [
     {
       "@search.score": 0.03279569745063782,
-      "HotelId": "4",
       "HotelName": "Sublime Palace Hotel",
-      "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.",
-      "Category": "Boutique",
-      "Tags": [
-        "concierge",
-        "view",
-        "air conditioning"
-      ]
+      "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience."
     },
     {
       "@search.score": 0.032522473484277725,
-      "HotelId": "13",
       "HotelName": "Luxury Lion Resort",
-      "Description": "Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort.",
-      "Category": "Luxury",
-      "Tags": [
-        "bar",
-        "concierge",
-        "restaurant"
-      ]
+      "Description": "Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort."
     },
     {
       "@search.score": 0.03205128386616707,
-      "HotelId": "48",
       "HotelName": "Nordick's Valley Motel",
-      "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
-      "Category": "Boutique",
-      "Tags": [
-        "continental breakfast",
-        "air conditioning",
-        "free wifi"
-      ]
+      "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley."
     },
     {
       "@search.score": 0.0317460335791111,
-      "HotelId": "49",
       "HotelName": "Swirling Currents Hotel",
-      "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary W-Fi and flat-screen TVs.",
-      "Category": "Suite",
-      "Tags": [
-        "air conditioning",
-        "laundry service",
-        "24-hour front desk service"
-      ]
+      "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary W-Fi and flat-screen TVs."
     },
     {
       "@search.score": 0.03125,
-      "HotelId": "2",
       "HotelName": "Old Century Hotel",
-      "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
-      "Category": "Boutique",
-      "Tags": [
-        "pool",
-        "free wifi",
-        "air conditioning",
-        "concierge"
-      ]
+      "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music."
     }
   ]
 }
 ```
 
-Because RRF merges results, it helps to review the inputs. The following results are from only the full-text query *historic hotel walk to restaurants and shopping*. The top two results are Sublime Palace Hotel and Stay-Kay City Hotel. The Sublime Palace Hotel has a stronger BM25 relevance score.
+Because RRF merges results, it helps to review the inputs individually. 
+
+The following results are from the full-text portion of the query: *historic hotel walk to restaurants and shopping*. In the full text query, the top three results are Sublime Palace Hotel, Stay-Kay City Hotel, and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score. In the fused query, only two of these matches are in the top 3, and the second match (Stay-Kay City Hotel) doesn't appear in the top 5 at all.
 
 ```json
+  "value": [
     {
       "@search.score": 1.4868739,
-      "HotelId": "4",
       "HotelName": "Sublime Palace Hotel",
-      "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.",
-      "Category": "Boutique",
-      "Tags": [
-        "concierge",
-        "view",
-        "air conditioning"
-      ]
+      "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience."
     },
     {
       "@search.score": 1.2699215,
-      "HotelId": "1",
       "HotelName": "Stay-Kay City Hotel",
-      "Description": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
-      "Category": "Boutique",
-      "Tags": [
-        "view",
-        "air conditioning",
-        "concierge"
-      ]
+      "Description": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities."
+    },
+    {
+      "@search.score": 1.2456272,
+      "HotelName": "Luxury Lion Resort",
+      "Description": "Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort."
     },
+    ...
+  ]
 ```
 
-In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to third position. Stay-Kay City Hotel, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
+In the vector portion query (*quintessential lodging near running trails, eateries, retail*) is a different string so we should expect different results. This query returns Nordick's Valley Motel, Luxury Lion Resort, and Sublime Palace Hotel as the top three matches. In the fused query, these results are in the top 3, but in reverse order.
 
 ```json
   "value": [
     {
       "@search.score": 0.6605852,
-      "HotelId": "48",
       "HotelName": "Nordick's Valley Motel",
-      "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
-      "Category": "Boutique",
-      "Tags": [
-        "continental breakfast",
-        "air conditioning",
-        "free wifi"
-      ]
+      "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley."
     },
     {
       "@search.score": 0.6333684,
-      "HotelId": "13",
       "HotelName": "Luxury Lion Resort",
-      "Description": "Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort.",
-      "Category": "Luxury",
-      "Tags": [
-        "bar",
-        "concierge",
-        "restaurant"
-      ]
+      "Description": "Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort."
     },
     {
       "@search.score": 0.605672,
-      "HotelId": "4",
       "HotelName": "Sublime Palace Hotel",
-      "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.",
-      "Category": "Boutique",
-      "Tags": [
-        "concierge",
-        "view",
-        "air conditioning"
-      ]
-    },
-    {
-      "@search.score": 0.6026341,
-      "HotelId": "49",
-      "HotelName": "Swirling Currents Hotel",
-      "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary W-Fi and flat-screen TVs.",
-      "Category": "Suite",
-      "Tags": [
-        "air conditioning",
-        "laundry service",
-        "24-hour front desk service"
-      ]
+      "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience."
     },
-    {
-      "@search.score": 0.57902366,
-      "HotelId": "2",
-      "HotelName": "Old Century Hotel",
-      "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
-      "Category": "Boutique",
-      "Tags": [
-        "pool",
-        "free wifi",
-        "air conditioning",
-        "concierge"
-      ]
-    }
+   ...
   ]
 ```
 
 ### Semantic hybrid search
 
-Here's the last query in the collection. This hybrid query uses L2 semantic ranking that applies machine reading comprehension to L1-ranked results, promoting more relevant matches to the top.
+Here's the last query in the collection. This hybrid query adds L2 semantic ranking that applies machine reading comprehension over the L1-ranked results, promoting more relevant matches to the top.
 
-1. Formulate the request.
+1. Formulate the request. 
 
     ```http
     ### Run a hybrid query with semantic reranking
@@ -1127,7 +1043,7 @@ Here's the last query in the collection. This hybrid query uses L2 semantic rank
         "select": "HotelName, Description",
         "queryType": "semantic",
         "semanticConfiguration": "semantic-config",
-        "top": 7,
+        "top": 5,
         "vectorQueries": [
             {
                 "vector": [-0.045507785,0.028645637,0.014222746,-0.018325701,-0.020214563,-0.038177505,0.015761355,0.047784425,0.010457533,-0.042280458,0.046658613,0.0010140118,0.008381038,-0.009988446,0.0053694933,0.05784167,0.004900405,0.011414473,0.037527036,0.08145868,0.0048034606,-0.036801513,-0.059943184,-0.020614851,-0.01619917,0.032973755,-0.03532545,-0.013622314,0.009012743,-0.010657678,-0.03354917,-0.041229703,0.004687752,-0.09882119,0.057391346,0.019413985,-0.010832804,-0.010069754,0.031922996,-0.0033805603,0.010926622,0.0031381983,0.048660055,-0.0047846967,0.011595854,0.001674644,0.03645126,0.034374762,-0.030922277,-0.012765447,-0.01850083,-0.053588606,-0.00835602,-0.06674808,-0.013834967,0.008368528,0.01100793,-0.004475099,0.07610483,0.0130844265,0.00012381967,-0.0016246078,0.013859984,0.049685795,0.023642031,0.042455584,-0.008443583,0.024104865,-0.055990335,-0.015673792,0.009100306,-0.03972862,-0.043931648,0.0052350215,0.06809906,-0.0184633,-0.003202307,0.0057729087,0.009606921,-0.018625919,0.0040091383,0.016599458,-0.0022719493,-0.004809715,-0.0045595346,-0.052087523,-0.041980244,-0.000460488,-0.034574907,0.048359837,0.03342408,-0.014598017,0.026343979,-0.058291994,-0.016737057,0.0073052626,0.020539798,-0.010194845,-0.033499133,-0.014635543,0.037502017,-0.089964814,0.0035807046,-0.037176784,-0.0020061329,-0.0072990083,0.024117375,0.02090256,0.022853965,-0.0027723096,-0.0719018,0.02684434,0.010957894,0.024254974,-0.039953783,0.055740155,-0.01708731,-0.016962219,0.01481067,0.05934275,0.019701693,0.021102702,-0.008024531,-0.035150323,-0.00784315,-0.042105332,-0.04695883,-0.014410381,-0.056740876,-0.04115465,0.0025393295,0.02847051,0.020552306,0.01456049,-0.034224655,-0.017149854,-0.015923971,-0.02254124,-0.041054577,-0.00031116165,-0.00522564,-0.015798882,0.011233092,-0.027669935,0.014535472,0.020777468,0.019914346,0.017762797,0.017537635,0.040354073,0.0073115174,-0.012790465,-0.0087375445,0.009544376,-0.06434636,-0.013222026,-0.024079848,-0.019964382,-0.024530172,0.023979776,-0.055740155,-0.024830388,-0.016549421,0.03770216,0.020152017,-0.049185432,-0.020402199,0.041304756,-0.074503675,-0.050211173,0.06669805,0.0069675194,-0.035875846,0.06894967,-0.0031585253,0.0018700972,0.0086062,-0.0059386534,-0.02696943,-0.007793114,0.0016246078,-0.04463215,-0.0043687723,0.031922996,0.03975364,0.06309546,-0.035900865,0.015160922,-0.037276853,0.011752216,-0.04795955,0.00068017753,-0.002251622,0.003399324,0.044982407,0.01107673,-0.017012255,0.01045128,0.010207353,0.027419753,-0.060293436,-0.02139041,0.028745709,-0.0027300918,-0.03987873,-0.032323286,0.011764726,-0.015873935,-0.034850106,-0.05243778,-0.0066860667,-0.0030224898,0.032098126,0.033924438,-0.0139725655,-0.007993259,-0.00170748,0.030471953,-0.000023869736,0.06764873,0.0009757029,-0.008087076,0.01657444,0.0445571,0.033198915,0.07735573,-0.01850083,-0.048359837,0.0055070925,-0.015773864,-0.0040028836,0.015486157,-0.017174874,-0.021365391,-0.032998774,0.043506343,0.0076367515,0.016737057,0.020602342,-0.0445571,-0.08651233,-0.03227325,-0.033949457,0.00597618,0.02922105,0.0013275188,-0.00064225955,-0.03154773,0.02315418,0.017600179,-0.025230676,0.067048304,-0.039928764,0.00629516,0.011445746,-0.015986517,0.0032116887,0.028320402,0.014385363,-0.021553027,0.05101175,-0.025355767,0.025030533,0.0003373524,0.023216726,0.005638437,0.01786287,-0.01669953,0.006267015,-0.024517663,-0.06279524,-0.024217447,-0.043581396,-0.0020405324,0.009613176,-0.014698089,-0.011777234,-0.013146971,0.060293436,0.0066610486,-0.031422637,-2.5958641e-7,0.024267482,-0.005466438,-0.020427216,0.00328987,0.0147731425,-0.0139725655,-0.030421916,0.0045313896,-0.01708731,-0.023016581,-0.0058166906,-0.040304035,0.0016902802,-0.0015331358,0.0033836877,-0.053738713,0.032223213,-0.002925545,0.0038871753,0.06879956,-0.02784506,-0.0060043256,-0.0061982153,0.020990122,0.023266762,-0.0074366075,0.030046646,0.019976892,0.008055803,0.03304881,-0.031347584,0.010394989,-0.009907138,-0.0369266,-0.026394015,0.015361066,0.020990122,-0.04620829,0.07900692,0.027669935,0.019639147,-0.02329178,-0.023617014,-0.009681975,-0.03530043,-0.021615572,-0.025505874,-0.016849639,0.02329178,-0.02809524,-0.039428405,0.069149815,-0.009200378,0.020990122,-0.040304035,-0.018675955,0.039428405,0.077505834,-0.09551881,-0.01797545,0.016336769,-0.025343258,-0.0009131578,0.003586959,0.012746682,0.027294664,0.011014185,0.049335543,-0.059893146,-0.008318493,-0.0023423124,0.038377646,-0.0064609046,-0.031697836,0.052587885,-0.010764005,-0.004265573,0.046758685,-0.030722132,-0.010588879,0.017887887,-0.017112328,-0.019701693,-0.0155737195,0.014185219,-0.012471485,-0.07105119,-0.0019373331,0.0072302087,0.05198745,0.011045457,-0.017637707,0.019476531,0.068299204,0.04745919,0.059292715,0.030797187,-0.00052342395,0.013096935,-0.022916509,0.013359624,-0.016249206,0.053438496,0.0011015749,-0.051236913,-0.010445025,-0.06694823,0.0098821195,0.022428658,-0.0102824075,-0.01669953,-0.0112831285,0.019914346,-0.031597763,0.017500108,-0.0066860667,-0.0053851297,0.0011523927,0.0044688443,-0.026469069,-0.0013799004,0.012777955,-0.0054820743,-0.021027649,0.0031553982,-0.024342537,-0.03444982,0.0110266935,0.025793582,-0.00905027,0.04075436,-0.009681975,0.0049660774,-0.026118817,-0.0075992243,-0.071651615,0.01960162,0.059642967,0.015661282,-0.015898954,-0.019138787,0.026243906,-0.043231145,0.007061337,0.0025565294,-0.02784506,-0.09401773,-0.01367235,-0.009913391,-0.047108937,0.032298267,0.05659077,-0.034124583,-0.02937116,-0.033699278,-0.022578767,0.0059417807,-0.017387526,0.02200335,-0.042080317,-0.025718529,-0.021815715,-0.04658356,-0.019076243,0.020414706,0.035400502,0.00734279,-0.04408176,-0.037251838,0.014485436,-0.009056524,-0.024642752,0.027169574,0.0072114454,0.045132514,-0.019413985,-0.033298988,-0.018250648,0.063695885,0.013134462,-0.004350009,0.020051945,0.022503711,-0.024492646,0.0010015027,0.01045128,0.036426242,-0.07550439,0.0036088498,-0.07570454,0.0058385814,-0.033824366,-0.06349574,-0.028020186,-0.023066618,0.025893655,0.007799369,0.015423612,-0.041579954,-0.02090256,0.017450072,-0.0061169066,0.00029669813,-0.014648053,-0.004934805,0.037151765,-0.040679306,0.023429379,-0.00670483,0.009325468,0.01189607,-0.013509733,-0.0053601116,0.057691563,-0.031998053,0.015273503,-0.0006051234,0.0041811373,-0.009256668,-0.013272061,-0.014247764,0.0037745943,0.030321844,0.039303314,-0.053338427,0.01786287,0.05088666,0.006711085,-0.0016652622,0.020064455,-0.014185219,0.015498665,0.0042843367,0.015110886,-0.002181259,0.044156812,0.0033680515,0.0022000223,0.0064358865,0.024955478,0.016536914,0.0074115894,0.019801766,0.037877288,0.022853965,-0.122988604,0.0036463768,-0.041029558,0.002875509,0.033824366,-0.02494297,0.015898954,0.011921088,0.064946786,0.029546285,-0.016436841,0.010376225,-0.033749312,0.0129093,0.018625919,-0.0476093,0.0029443086,-0.017475089,-0.05013612,-0.019801766,-0.010651424,0.03557563,0.04530764,0.014097656,0.020965103,-0.0060981433,0.004065429,0.0067673754,-0.014397873,-0.0137724215,-0.0017684615,0.012208795,0.035375483,-0.045107495,-0.0148607055,0.017112328,0.013834967,0.0019576603,0.011996143,0.026619177,0.031647798,-0.019439004,0.0061763246,-0.01253403,0.023004072,-0.021678118,-0.017925413,0.03785227,0.0072114454,0.003299252,-0.007855659,0.0073052626,0.0075491886,0.010601387,0.00923165,-0.0067486116,0.008205912,-0.008062058,-0.00064734137,-0.00012714238,-0.013259552,0.0012532466,0.018163085,0.015498665,0.023504432,-0.008305984,-0.0627452,-0.0028473637,0.030572025,-0.012759192,0.009069033,-0.025618456,-0.017287454,0.00809333,0.023854686,0.015323539,0.014748124,-0.001452609,0.0052350215,-0.044106774,0.004709643,0.0034524873,-0.0022172222,0.001502645,-0.03254845,-0.003027181,-0.01847581,0.025168132,-0.021077685,-0.017575162,-0.0105388425,0.012265086,0.0025471475,0.008631218,-0.023066618,0.01644935,0.059592932,-0.013297079,0.03149769,0.018125558,-0.042980965,0.0014229001,-0.0048253513,-0.017687742,0.068299204,0.026769284,-0.024630243,-0.023829667,-0.027369717,-0.008399801,-0.007699297,-0.0088251075,-0.0072114454,0.013947548,0.005491456,0.025280712,-0.02252873,0.05834203,-0.009275432,-0.0035494321,-0.00068369566,0.008218421,-0.012802973,-0.018325701,-0.0043343725,0.012258831,0.0034556144,-0.00091237604,0.034099564,0.020915067,0.0011907015,0.00039696565,0.011514545,0.017675234,-0.0049129142,-0.016599458,-0.0015972444,-0.04570793,0.035750754,0.013322097,-0.01960162,-0.03887801,0.00956314,0.08015775,0.025718529,0.02999661,0.010976657,0.030146718,0.012884282,0.016311752,-0.0011500473,-0.015711319,0.0070988643,0.044532083,-0.0039372114,-0.028295385,-0.018813554,-0.024355046,-0.030972313,0.0060762526,0.014247764,0.019476531,-0.012527775,-0.0035775774,-0.01606157,0.05073655,0.020202054,-0.022691347,0.000043830405,0.0034368508,-0.041229703,0.006404614,-0.06419625,0.0021359138,0.022503711,0.008806344,-0.07290252,0.004118592,-0.009044016,-0.013059408,-0.036801513,0.03735191,-0.00091706694,0.004981714,-0.024204938,-0.012333886,0.014497944,-0.011583345,-0.0516372,-0.021540519,0.015798882,0.0013126644,0.00924416,0.017950432,0.013497223,0.019576604,-0.0065109404,-0.013784931,0.028245348,0.019226352,-0.02254124,-0.0062107244,0.040203962,-0.002381403,-0.030471953,-0.0075867157,0.050411317,-0.028320402,-0.005729127,-0.027820041,0.0051412038,-0.009100306,-0.011514545,-0.00617007,-0.008868889,0.005453929,-0.014510454,0.009513103,0.0057134912,0.0125715565,-0.014910742,-0.044732224,-0.037802234,-0.010420007,0.009388013,0.006592249,-0.004443826,-0.0133721335,-0.072452195,-0.016499387,-0.03274859,0.006326433,0.008568673,0.032873683,-0.00082090386,0.033499133,0.047759406,0.018901117,0.010307426,0.015135904,0.006173197,-0.024505153,0.00044993352,-0.009094051,-0.02684434,0.0030396897,-0.026569141,0.028395457,-0.032223213,0.006132543,-0.0054820743,0.006254506,-0.025493365,0.013559769,-0.013209516,-0.007542934,-0.020001909,-0.055139724,0.0135722775,-0.00551022,-0.022678837,0.008487364,0.03857779,-0.009075288,-0.03785227,0.009544376,-0.038402665,0.02329178,-0.02037718,-0.011677163,-0.016399315,0.05759149,-0.006611013,0.02139041,-0.0058166906,0.008599945,-0.013847476,0.026669214,-0.016511895,-0.018713482,-0.022291059,0.012246323,-0.02100263,-0.014923251,0.00037097037,-0.003085035,-0.014885724,0.025918672,0.0057197455,-0.028170295,0.024480136,-0.007530425,-0.005181858,-0.019038716,-0.048509948,0.016136626,0.025243185,-0.01973922,0.0036119772,-0.011470764,0.01569881,0.0058073085,-0.01621168,-0.022616293,-0.011633381,0.01632426,0.023617014,-0.001389282,-0.018713482,0.023867194,-0.0011993014,-0.024892934,-0.00021656226,0.012996863,0.031847943,-0.026544122,-0.027394736,-0.012746682,-0.01340966,0.0213779,0.022453675,-0.019188823,-0.01043877,-0.018638426,0.003977866,0.017187381,-0.015198449,-0.0020358416,-0.021290338,-0.019964382,-0.03592588,-0.022090914,-0.024367554,0.007780605,0.023829667,-0.0014135183,0.031147439,-0.017362509,0.03862783,0.016924692,0.03189798,0.006598504,-0.05909257,-0.04403172,-0.002888018,-0.0033680515,-0.014635543,0.013434678,-0.026343979,-0.0012985917,0.0007356862,0.004628334,0.02558093,0.027169574,0.0065359585,-0.005960544,0.013484715,-0.0106264055,0.009350486,-0.037301872,0.060593653,0.031722855,0.011508291,0.00011013794,0.042830855,0.022190986,0.0033586696,-0.053588606,-0.02455519,-0.0046439706,0.015110886,-0.007961986,-0.010764005,0.025893655,-0.022378622,0.0045720437,0.02594369,0.02847051,-0.015235976,-0.011458254,0.02036467,-0.023479415,0.005206876,-0.008299729,-0.026469069,-0.019989401,-0.009200378,0.0048441147,0.0067861388,-0.013747403,0.015748845,0.0006074689,-0.019251369,-0.0018450792,0.0098821195,-0.03757707,0.015611246,-0.007924459,0.0038652846,-0.01733749,-0.020026928,0.021703135,0.00028399366,-0.0036651404,-0.013634822,-0.022065897,-0.027419753,0.043206125,-0.021177758,0.028770726,0.00017737388,-0.013109445,0.02681932,-0.013997584,-0.011158038,0.025280712,-0.023054108,0.01810054,-0.033874404,-0.013759913,0.008618709,0.040579233,-0.04465717,0.046508506,-0.01911377,0.014135183,0.0043468815,-0.0359509,0.01644935,-0.011933597,-0.0005199058,0.004190519,-0.00759297,0.02696943,0.041429847,-0.012365158,-0.01669953,0.012959336,0.044857316,0.0015268812,0.036376204,-0.012946827,0.015748845,-0.019901838,0.0110829845,0.013021881,-0.01043877,-0.010463788,0.0014979541,0.0066547943,0.0359509,0.002905218,-0.046858758,0.04368147,0.0503863,0.04720901,0.041304756,0.031147439,0.027920114,0.005563383,0.049285505,0.017274946,-0.024792861,-0.010707714,0.00923165,-0.0105388425,0.020802487,-0.0060981433,0.008368528,0.0019388968,-0.026368996,0.013522241,0.043581396,-0.03177289,0.0017528252,-0.027920114,-0.00689872,-0.034099564,-0.032448377,-0.002855182,0.04745919,-0.032698557,-0.013284571,-0.01923886,0.014598017,0.0126278475,-0.048635036,0.003077217,-0.0015925536,0.0033711786,-0.0044188085,0.010101027,0.034524873,0.012077451,0.0031835434,-0.0033430334,-0.007255227,0.019589113,-0.004328118,0.045007423,-0.024605226,0.04090447,-0.015974008,-0.00087719446,0.006861193,0.027419753,0.028445492,-0.006442141,0.015723828,-0.0028645636,-0.0148607055,-0.015811391,0.028195312,0.005872981,0.015548701,0.02316669,0.008030785,-0.0258186,-0.01543612,0.01783785,0.009769538,0.043831576,0.012659119,-0.0141727105,-0.008074567,-0.015398594,-0.036025953,-0.0058667264,0.0025299476,-0.00009230283,0.002695692,-0.020189544,0.009419286,0.002695692,0.016511895,-0.010914112,-0.051061787,-0.015473647,-0.01506085,-0.0038215031,0.02784506,-0.016149133,0.0052475305,0.023967266,-0.004859751,-0.0036495042,-0.007392826,0.0023532577,-0.032573465,-0.0242925,0.0034087056,-0.003621359,-0.011602108,-0.0027598008,0.001540172,0.013484715,0.0022719493,-0.014160201,0.008675,0.0102824075,0.020477252,-0.014948268,-0.0031991797,-0.002121841,0.019889329,-0.0007548407,-0.022891492,0.018263157,-0.0015902082,0.0062388694,0.015073359,-0.0062982873,-0.016949711,-0.004265573,0.017112328,0.00057267817,-0.030346863,0.0018904244,-0.0100635,-0.004972332,-0.010107282,-0.0061294157,0.027995167,0.007693042,-0.012540285,-0.004697134,0.042205404,-0.015298521,0.0015761355,0.010857822,-0.017249927,-0.016399315,0.001469027,-0.03762711,-0.04152992,0.027244627,0.0004737788,-0.017637707,0.017700251,-0.016399315,0.00094443036,-0.02100263,0.009832083,0.030446934,-0.021765681,-0.00040615196,-0.019226352,-0.028145276,-0.03467498,0.012102469,0.0062763966,0.0033555424,0.014535472,-0.006107525,0.017562652,-0.010939131,-0.03820252,0.039328333,0.01100793,-0.012996863,0.061844554,0.022929018,-0.0012149378,-0.0062513785,-0.011039203,0.0025596565,0.016987238,-0.004537644,-0.008975216,0.019313915,0.001059357,0.006698576,0.017437562,-0.0131719895,0.008268457,-0.022941528,0.009975937,0.02518064,-0.015898954,-0.029971592,-0.008143366,-0.0027707461,0.024993006,0.009119069,-0.016787093,-0.025243185,-0.005973053,0.012171268,0.004772188,-0.0012845191,-0.0002779346,-0.029020907,-0.034249675,-0.017387526,0.02022707,0.007455371,-0.00024451208,-0.029896537,0.011039203,-0.014022602,0.027569862,0.028445492,-0.025505874,-0.017550142,-0.0046564797,0.038552772,-0.029846502,-0.011001675,-0.010401243,0.011477018,-0.0045845527,0.021352883,0.02505555,0.011495782,-0.013522241,-0.047784425,0.019476531,-0.004350009,0.009794557,0.004909787,-0.018075522,-0.0213779,-0.009006488,-0.023516942,0.011408218,-0.0427558,-0.048635036,0.025593437,0.00172468,0.00023591214,-0.010294916,0.0063639595,0.025843618,-0.033073828,0.0006019962,0.024054829,0.028045204,0.046658613,0.0037996122,-0.050561424,-0.005034877,0.014422891,0.008787581,0.0016042808,0.0012337012,0.015286013,0.0021937678,-0.0032210704,0.038052414,0.026168853,0.026168853,-0.01481067,-0.015661282,-0.005256912,-0.025480857,-0.0029396177,0.0010820295,0.004794079,-0.035000216,-0.026444051,0.008818854,0.006973774,0.012821737,0.006054362,-0.024655262,-0.0069049746,-0.0029396177,-0.007936968,0.03404953,0.010545096,-0.011433236,-0.00061763247,0.0059292717,-0.052487813,-0.008531146,-0.009656957,-0.02266633,-0.022828946,-0.002930236,0.015673792,-0.0046658614,-0.011739708,0.01619917,-0.015035832,0.02594369,-0.007868168,0.022065897,0.04110461,-0.014623035,-0.012602829,0.003349288,-0.016349278,0.0027598008,-0.00092723046,-0.030797187,-0.004503244,-0.0242925,0.008174639,0.021452954,-0.007555443,-0.00446259,0.035275415,-0.0029896537,0.011133021,0.027644916,-0.008637473,-0.023429379,-0.0021859498,0.011289383,-0.0007571861,-0.026394015,0.024880424,-0.0071926815,-0.03377433,0.040429126,0.03667642,0.011733453,-0.009388013,0.009075288,-0.015361066,-0.0035150324,-0.0095381215,-0.015085868,0.0043844087,0.023004072,-0.027669935,0.0172124,0.000673923,-0.0057134912,0.019313915,-0.002875509,0.016636986,-0.016286733,-0.0142978,-0.0034431054,-0.012665374,-0.030547006,-0.02075245,-0.0046596066,-0.019188823,-0.00007246431,-0.0013908457,-0.011014185,0.004834733,0.038127467,0.0057322546,-0.015498665,0.003977866,0.04668363,-0.012252577,0.023341816,-0.0011164293,0.0050036046,0.023504432,-0.0035025233,0.019026207,-0.013397152,0.0054414202,-0.029496249,-0.016549421,-0.016024044,-0.010576369,-0.009738266,-0.010244881,0.022378622,-0.0016433714,-0.011376946,0.028445492,-0.0184633,-0.00471277,-0.020990122,0.0068549383,-0.0024001666,0.022378622,0.015336048,0.01619917,-0.026143834,0.0498359,0.0054132747,0.02379214,-0.017012255,-0.049810883,-0.021615572,-0.0054101474,0.0063764686,0.005106804,0.022266041,0.010989167,-0.0052850572,-0.025318239,-0.009400522,0.0071864272,0.028195312,-0.02505555,0.022053387,0.0023876575,0.009688229,-0.03444982,0.019013697,-0.0045814253,0.009769538,-0.034599926,0.009957173,-0.023379343,-0.0041592466,-0.011014185,0.026644194,0.011301892,-0.023316797,0.012734174,-0.0140851475,0.013272061,0.00042530638,-0.03760209,-0.021077685,-0.019926855,0.010088518,-0.011539564,-0.0100259725,-0.042455584,-0.021815715,0.00029865265,-0.03960353,0.0044719717,0.0027738733,-0.006611013,0.0013986639,0.008518637,-0.011852289,0.036776494,-0.0030084173,0.0019858056,-0.013872494,-0.019789256,-0.014035111,-0.0049785865,-0.0005969144,-0.0023454397,0.028645637,-0.001619917,-0.036126025,0.010995422,0.023591995,-0.054088965,0.0063514505,-0.02468028,0.022253532,0.010457533,0.00019721239,-0.024455117,-0.033098843,0.036751475,-0.01607408,0.0026268924,-0.033899423,-0.007355299,-0.014185219,-0.015773864,-0.004728406,0.009488085,0.021415427,0.03847772,-0.044356953,0.031047367,0.009732011,0.038402665,0.011989888,0.011452001,0.0034399782,0.017575162,0.01975173,-0.02504304,0.00011160384,0.0059261443,-0.0026253287,-0.04430692,0.038652845,0.026644194,-0.0102824075,0.021690626,-0.015798882,-0.020139508,-0.012033669,0.004806588,-0.063295595,0.0036495042,0.010982912,-0.020602342,0.0027363463,0.033699278,0.0074866433,0.03820252,-0.015135904,-0.0066673034,-0.046858758,0.012458975,-0.0012243196,0.009169105,-0.0028567456,-0.0049410597,0.017037274,-0.023529451,0.017700251,-0.01708731,0.0244301,0.02962134,-0.013684859,0.035500575,0.043506343,-0.0036276134,0.022753892,0.0038934299,-0.0014002275,-0.005622801,0.025218168,-0.0040497924,0.017750287,-0.022416148,-0.003172598,0.010213608,0.000090836926,0.004884769,-0.013534751,-0.010663932,-0.0033461605,-0.01431031,-0.017074801,0.0045908075,0.03407455,-0.0054883286,0.009694484,0.018175595,-0.012515266,-0.0001456127,-0.0044719717,0.0029615085,0.008556164,0.017887887,-0.027744988,-0.0035588138,-0.010782768,0.021165248,-0.05634059,0.0041404827,0.019639147,0.022178477,-0.03645126,0.0048128422,-0.006132543],
@@ -1142,80 +1058,64 @@ Here's the last query in the collection. This hybrid query uses L2 semantic rank
 
 1. Select **Send request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
 
-Review the response, semantically reranked to promote results that are closest to the search string query (`historic hotel walk to restaurants and shopping`).
+Review the response, consisting of a semantic reranking of the RRF-ranked results of the hybrid query. Semantic ranking works off of text inputs. In a text or hybrid query, this input is the text portion of the query (*historic hotel walk to restaurants and shopping*). To use semantic ranking on a pure vector query, such as the first example, or to explicitly control the text used for semantic ranking, [provide a semanticQuery string](semantic-how-to-query-request.md#set-up-the-query).
+
+After semantic reranking, Swirling Currents Hotel with its reference to *walking access to shopping, dining, entertainment and the city center* moves into the top spot. The machine comprehension model promotes *walking access to shopping and dining* as a closer match to *walk to restaurants and shopping*.
 
-The Swirling Currents Hotel now moves into the top spot. Without semantic reranking, Sublime Palace, with it's reference to *walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments* is number one. With semantic ranking, the machine comprehension model promotes *walking access to shopping and dining* as a closer match to *walk to restaurants and shopping*. 
+Before semantic reranking, Sublime Palace, with its reference to *walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments* was number one.  
 
 ```json
+{
   "@odata.count": 7,
   "@search.answers": [],
   "value": [
     {
-      "@search.score": 0.03253968432545662,
+      "@search.score": 0.0317460335791111,
       "@search.rerankerScore": 2.6550590991973877,
       "HotelId": "49",
       "HotelName": "Swirling Currents Hotel",
       "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary W-Fi and flat-screen TVs.",
       "Category": "Suite"
     },
     {
-      "@search.score": 0.03229166567325592,
+      "@search.score": 0.03279569745063782,
       "@search.rerankerScore": 2.599761724472046,
       "HotelId": "4",
       "HotelName": "Sublime Palace Hotel",
       "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.",
       "Category": "Boutique"
     },
     {
-      "@search.score": 0.0314980149269104,
+      "@search.score": 0.03125,
       "@search.rerankerScore": 2.3480887413024902,
       "HotelId": "2",
       "HotelName": "Old Century Hotel",
       "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
       "Category": "Boutique"
     },
     {
-      "@search.score": 0.032522473484277725,
+      "@search.score": 0.03154495730996132,
       "@search.rerankerScore": 2.2718777656555176,
       "HotelId": "1",
       "HotelName": "Stay-Kay City Hotel",
       "Description": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
       "Category": "Boutique"
     },
     {
-      "@search.score": 0.03154495730996132,
+      "@search.score": 0.03053613007068634,
       "@search.rerankerScore": 2.0582215785980225,
       "HotelId": "3",
       "HotelName": "Gastronomic Landscape Hotel",
       "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel\u2019s restaurant services.",
       "Category": "Suite"
-    },
-    {
-      "@search.score": 0.03053613007068634,
-      "@search.rerankerScore": 1.9285744428634644,
-      "HotelId": "48",
-      "HotelName": "Nordick's Valley Motel",
-      "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
-      "Category": "Boutique"
-    },
-    {
-      "@search.score": 0.03151364624500275,
-      "@search.rerankerScore": 1.7348570823669434,
-      "HotelId": "13",
-      "HotelName": "Luxury Lion Resort",
-      "Description": "Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort.",
-      "Category": "Luxury"
     }
   ]
+}
 ```
 
-Key takeaways about [Documents - Search Post](/rest/api/searchservice/documents/search-post) REST API:
-
-- Vector search is specified through the `vectors.value` property. Keyword search is specified through the `search` property.
-
-- In a hybrid search, you can integrate vector search with full-text search over keywords. Filters, spell check, and semantic ranking apply to textual content only, and not vectors. In this final query, there's no semantic `answer` because the system didn't produce one that was sufficiently strong.
-
-- Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
+> [!TIP]
+>Semantically ranked results can include more detail, including semantic answers, captions, and highlights. Adding more parameters to the request produces the extra detail. For more information, see [Set up a semantic query](semantic-how-to-query-request.md?tabs=rest-query#set-up-the-query).
+>
 
 ## Clean up
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索入門 - ベクトル検索のアップデート"
}
```

### Explanation
この変更は、マイクロソフトのAzure AIドキュメントにおける「検索入門: ベクトル検索」に関する記事の更新です。主な変更点として、更新された認証方法、APIバージョン、データモデルの調整、サンプルクエリの修正が含まれています。

具体的には、APIバージョンのアップデートが行われ、いくつかのテキストの修正がありました。例えば、「APIキー」の代わりに「Bearerトークン」を使用する新しい認証方法の説明が追加されています。また、クエリの説明をより明確にするための文言の変更や、テスト用のデータやクエリ例の整備が行われています。

全体として、これらの変更は、ベクトル検索とその関連機能の理解を深めるためのもので、ユーザーがAzureの検索機能を効果的に利用できるように、より親しみやすく、かつ正確な情報を提供しています。

## articles/search/search-howto-index-sharepoint-online.md{#item-49ff6e}

<details>
<summary>Diff</summary>
````diff
@@ -9,34 +9,34 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 05/26/2025
+ms.date: 06/17/2025
 ---
 
 # Index data from SharePoint document libraries
 
 > [!IMPORTANT]
 > SharePoint Online indexer support is in public preview. It's offered "as-is", under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) and supported on best effort only. Preview features aren't recommended for production workloads and aren't guaranteed to become generally available.
 >
-> Be sure to visit the [known limitations](#limitations-and-considerations) section before you start.
+> See [known limitations](#limitations-and-considerations) section before you start.
 >
->To use this preview, [fill out this form](https://aka.ms/azure-cognitive-search/indexer-preview). You won't be receiving any approval notification right after since any access request is automatically accepted after submission. After access is enabled, use a [preview REST API](search-api-preview.md) to index your content. 
+> [Fill out this form](https://aka.ms/azure-cognitive-search/indexer-preview) to register for the preview. All requests are approved automatically. After you fill out the form, use a [preview REST API](search-api-preview.md) to index your content. 
 
 This article explains how to configure a [search indexer](search-indexer-overview.md) to index documents stored in SharePoint document libraries for full text search in Azure AI Search. Configuration steps are first, followed by behaviors and scenarios
 
-## Functionality
+In Azure AI Search, an indexer extracts searchable data and metadata from a data source. The SharePoint Online indexer connects to your SharePoint site and indexes documents from one or more document libraries. The indexer provides the following functionality:
 
-An indexer in Azure AI Search is a crawler that extracts searchable data and metadata from a data source. The SharePoint Online indexer connects to your SharePoint site and indexes documents from one or more document libraries. The indexer provides the following functionality:
-
-+ Index files and metadata from one or more document libraries.
-+ Index incrementally, picking up just the new and changed files and metadata. 
-+ Deletion detection is built in. Deletion in a document library is picked up on the next indexer run, and the document is removed from the index.
-+ Text and normalized images are extracted by default from the documents that are indexed. Optionally, you can add a [skillset](cognitive-search-working-with-skillsets.md) for deeper [AI enrichment](cognitive-search-concept-intro.md), like OCR or text translation. 
++ Indexes files and metadata from one or more document libraries.
++ Indexes incrementally, picking up just the new and changed files and metadata. 
++ Detects deleted content automatically. Document deletion in the library is picked up on the next indexer run, and the corresponding search document is removed from the index.
++ Extracts text and normalized images from indexed documents automatically. Optionally, you can add a [skillset](cognitive-search-working-with-skillsets.md) for deeper [AI enrichment](cognitive-search-concept-intro.md), like OCR or text translation. 
 
 ## Prerequisites
 
-+ [SharePoint in Microsoft 365](/sharepoint/introduction) cloud service
++ [Azure AI Search](search-create-service-portal.md), Basic pricing tier or higher.
+
++ [SharePoint in Microsoft 365](/sharepoint/introduction) cloud service (OneDrive isn't a supported data source).
 
-+ Files in a [document library](https://support.microsoft.com/office/what-is-a-document-library-3b5976dd-65cf-4c9e-bf5a-713c10ca2872)
++ Files in a [document library](https://support.microsoft.com/office/what-is-a-document-library-3b5976dd-65cf-4c9e-bf5a-713c10ca2872).
 
 ## Supported document formats
 
@@ -48,51 +48,43 @@ The SharePoint Online indexer can extract text from the following document forma
 
 Here are the limitations of this feature:
 
-+ Indexing [SharePoint Lists](https://support.microsoft.com/office/introduction-to-lists-0a1c3ace-def0-44af-b225-cfa8d92c52d7) isn't supported.
++ The indexer can index content from supported document formats in a document library. There's no indexer support for [SharePoint Lists](https://support.microsoft.com/office/introduction-to-lists-0a1c3ace-def0-44af-b225-cfa8d92c52d7), .ASPX site content, or OneNote notebook files. Furthermore, indexing sub-sites recursively from a specific site isn't supported.
 
-+ Indexing SharePoint .ASPX site content isn't supported.
++ Incremental indexing limitations:
 
-+ OneNote notebook files aren't supported.
+  + Renaming a SharePoint folder breaks incremental indexing. A renamed folder is treated as new content.
 
-+ [Private endpoint](search-indexer-howto-access-private.md) isn't supported.
+  + Microsoft 365 processes that update SharePoint file system metadata can trigger incremental indexing, even if there are no other changes to content. Be sure to test your setup and understand the document processing count prior to using the indexer and any AI enrichment.
 
-+ Renaming a SharePoint folder doesn't trigger incremental indexing. A renamed folder is treated as new content.
++ Security limitations:
 
-+ SharePoint supports a granular authorization model that determines per-user access at the document level. The indexer doesn't pull these permissions into the index, and Azure AI Search doesn't support document-level authorization. When a document is indexed from SharePoint into a search service, the content is available to anyone who has read access to the index. If you require document-level permissions, you should consider [security filters to trim results](search-security-trimming-for-azure-search.md) and automate copying the permissions at a file level to a field in the index.
+  + No support for [Private endpoint](search-indexer-howto-access-private.md).
 
-+ Indexing user-encrypted files, Information Rights Management (IRM) protected files, ZIP files with passwords or similar encrypted content isn't supported. For encrypted content to be processed, the user with proper permissions to the specific file must remove the encryption so the item can be indexed accordingly when the indexer runs the next scheduled iteration.
+  + No support for document libraries or content configured for [Microsoft Entra ID Conditional Access](/entra/identity/conditional-access/overview).
 
-+ Indexing sub-sites recursively from a specific site provided isn't supported.
+  + No support for user-encrypted files, Information Rights Management (IRM) protected files, ZIP files with passwords or similar encrypted content isn't supported.
 
-+ SharePoint Online indexer isn't supported when [Microsoft Entra ID Conditional Access](/entra/identity/conditional-access/overview) is enabled.
+  + No support for SharePoint's granular authorization model that determines per-user access at the document level. The indexer doesn't pull these permissions into the index. Content is available to anyone who has read access to the index. If you require document-level permissions, consider [security filters to trim results](search-security-trimming-for-azure-search.md) and automate copying the permissions at a file level to a field in the index.
 
-Here are the considerations when using this feature:
+Here are some considerations when using this feature:
 
-+ If you need to create a custom Copilot / RAG (Retrieval Augmented Generation) application to chat with SharePoint data, the recommended approach is to use [Microsoft Copilot Studio](https://www.microsoft.com/microsoft-copilot/microsoft-copilot-studio) instead of this preview feature. 
++ If you need to create a custom Copilot or RAG (Retrieval Augmented Generation) application to chat with SharePoint data, Microsoft recommends using [Microsoft Copilot Studio](https://www.microsoft.com/microsoft-copilot/microsoft-copilot-studio) instead of this preview feature. 
 
 + If you still need a custom SharePoint Online content indexing solution using Azure AI Search in a production environment, despite the recommendation to use Microsoft Copilot Studio, consider:
-  - Creating a custom connector with [SharePoint Webhooks](/sharepoint/dev/apis/webhooks/overview-sharepoint-webhooks), calling [Microsoft Graph API](/graph/use-the-api) to export the data to an Azure Blob container, and then use the [Azure blob indexer](search-howto-indexing-azure-blob-storage.md) for incremental indexing.
-  - Creating your own [Azure Logic Apps workflow](/azure/logic-apps/logic-apps-overview) using [Azure Logic Apps SharePoint connector](/connectors/sharepointonline/) and [Azure AI Search connector](/connectors/azureaisearch/) when reaching General Availability. You can use the workflow generated by the [Azure portal wizard](search-how-to-index-logic-apps-indexers.md) as a starting point and then customize it in the [Azure Logic Apps designer](/azure/logic-apps/quickstart-create-example-consumption-workflow#add-the-trigger) to include the transformation steps you need. The Azure Logic App workflow created when using the [Azure AI Search wizard](search-how-to-index-logic-apps-indexers.md) to index SharePoint Online data is a [consumption workflow](/azure/logic-apps/logic-apps-overview#key-terms). If you're setting up production workloads, make sure to switch to a [standard logic app workflow](/azure/logic-apps/logic-apps-overview#key-terms) and take advantage of its additional enterprise features.
-  - Regardless of the approach you choose, whether building a custom connector with SharePoint hooks or creating an Azure Logic Apps workflow, it's key to implement robust security measures. These measures include configuring shared private links, setting up firewalls, preserving user permissions from the source and honor at query time, among others. You should also regularly audit and monitor your pipeline.
-
-<!-- + There could be Microsoft 365 processes that update SharePoint file system-metadata (based on different configurations in SharePoint) and will cause the SharePoint Online indexer to trigger. Make sure that you test your setup and understand the document processing count prior to using any AI enrichment. Since this is a third-party connector to Azure (SharePoint is located in Microsoft 365), SharePoint configuration is not checked by the indexer. -->
-
-+ If your SharePoint configuration allows Microsoft 365 processes to update SharePoint file system metadata, be aware that these updates can trigger the SharePoint Online indexer, causing the indexer to ingest documents multiple times. Because the SharePoint Online indexer is a non-Microsoft connector to Azure, the indexer can't read the configuration or vary its behavior. It responds to changes in new and changed content, regardless of how those updates are made. For this reason, make sure that you test your setup and understand the document processing count prior to using the indexer and any AI enrichment.
-
 
+  - Creating a custom connector with [SharePoint Webhooks](/sharepoint/dev/apis/webhooks/overview-sharepoint-webhooks), calling [Microsoft Graph API](/graph/use-the-api) to export the data to an Azure Blob container, and then use the [Azure blob indexer](search-howto-indexing-azure-blob-storage.md) for incremental indexing.
 
+  - Creating your own [Azure Logic Apps workflow](/azure/logic-apps/logic-apps-overview) using [Azure Logic Apps SharePoint connector](/connectors/sharepointonline/) and [Azure AI Search connector](/connectors/azureaisearch/) when reaching General Availability. You can use the workflow generated by the [Azure portal wizard](search-how-to-index-logic-apps-indexers.md) as a starting point and then customize it in the [Azure Logic Apps designer](/azure/logic-apps/quickstart-create-example-consumption-workflow#add-the-trigger) to include the transformation steps you need. The Azure Logic App workflow created when using the [Azure AI Search wizard](search-how-to-index-logic-apps-indexers.md) to index SharePoint Online data is a [consumption workflow](/azure/logic-apps/logic-apps-overview#key-terms). If you're setting up production workloads, make sure to switch to a [standard logic app workflow](/azure/logic-apps/logic-apps-overview#key-terms) and take advantage of its additional enterprise features.
+  
+  Regardless of the approach you choose, whether building a custom connector with SharePoint hooks or creating an Azure Logic Apps workflow, be sure to implement robust security measures. These measures include configuring shared private links, setting up firewalls, preserving user permissions from the source and honor those permissions at query time, among others. You should also regularly audit and monitor your pipeline.
 
 ## Configure the SharePoint Online indexer
 
-To set up the SharePoint Online indexer, use both the Azure portal and a preview REST API. You can use 2020-06-30-preview or later. We recommend the latest preview API.
-
-This section provides the steps. You can also watch the following video.
- 
-> [!VIDEO https://www.youtube.com/embed/QmG65Vgl0JI]
+To set up the SharePoint Online indexer, use a preview REST API. This section provides the steps. 
 
 ### Step 1 (Optional): Enable system assigned managed identity
 
-Enable a [system-assigned managed identity](search-howto-managed-identities-data-sources.md#create-a-system-managed-identity) to automatically detect the tenant the search service is provisioned in. 
+Enable a [system-assigned managed identity](search-howto-managed-identities-data-sources.md#create-a-system-managed-identity) to automatically detect the tenant in which the search service is provisioned. 
 
 Perform this step if the SharePoint site is in the same tenant as the search service. Skip this step if the SharePoint site is in a different tenant. The identity isn't used for indexing, just tenant detection. You can also skip this step if you want to put the tenant ID in the [connection string](#connection-string-format).
 
@@ -110,26 +102,25 @@ We recommend app-based permissions. See [limitations](#limitations-and-considera
 
 + Application permissions (recommended), where the indexer runs under the [identity of the SharePoint tenant](/sharepoint/dev/solution-guidance/security-apponly-azureacs) with access to all sites and files. The indexer requires a [client secret](/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow). The indexer will also require [tenant admin approval](/azure/active-directory/manage-apps/grant-admin-consent) before it can index any content.
 
-+ Delegated permissions, where the indexer runs under the identity of the user or app sending the request. Data access is limited to the sites and files to which the caller has access. To support delegated permissions, the indexer requires a [device code prompt](/azure/active-directory/develop/v2-oauth2-device-code) to sign in on behalf of the user. User-delegated permissions enforce token expiration every 75 minutes, per the most recent security libraries used to implement this authentication type. This isn't a behavior that can be adjusted. An expired token requires manual indexing using [Run Indexer (preview)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2024-05-01-preview&tabs=HTTP&preserve-view=true). For this reason, you might want app-based permissions instead.
-
++ Delegated permissions, where the indexer runs under the identity of the user or app sending the request. Data access is limited to the sites and files to which the caller has access. To support delegated permissions, the indexer requires a [device code prompt](/azure/active-directory/develop/v2-oauth2-device-code) to sign in on behalf of the user. User-delegated permissions enforce token expiration every 75 minutes, per the most recent security libraries used to implement this authentication type. This isn't a behavior that can be adjusted. An expired token requires manual indexing using [Run Indexer (preview)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true). For this reason, you should use app-based permissions instead.
 
 <a name='step-3-create-an-azure-ad-application'></a>
 
 ### Step 3: Create a Microsoft Entra application registration
 
-The SharePoint Online indexer uses this Microsoft Entra application for authentication.
+The SharePoint Online indexer uses a Microsoft Entra application for authentication. Create the application registration in the same tenant as Azure AI Search.
 
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
-1. Search for or navigate to **Microsoft Entra ID**, then select **App registrations**. 
+1. Search for or navigate to **Microsoft Entra ID**, then select **Add** > **App registrations**. 
 
 1. Select **+ New registration**:
     1. Provide a name for your app.
     1. Select **Single tenant**.
     1. Skip the URI designation step. No redirect URI required.
     1. Select **Register**.
 
-1. On the left, select **API permissions**, then **Add a permission**, then **Microsoft Graph**.
+1. On the navigation pane under **Manage**, select **API permissions**, then **Add a permission**, then **Microsoft Graph**.
 
     + If the indexer is using application API permissions, then select **Application permissions** and add the following:
 
@@ -193,10 +184,10 @@ For SharePoint indexing, the data source must have the following required proper
 + **credentials** provide the SharePoint endpoint and the Microsoft Entra application (client) ID. An example SharePoint endpoint is `https://microsoft.sharepoint.com/teams/MySharePointSite`. You can get the endpoint by navigating to the home page of your SharePoint site and copying the URL from the browser.
 + **container** specifies which document library to index. Properties [control which documents are indexed](#controlling-which-documents-are-indexed).
 
-To create a data source, call [Create Data Source (preview)](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2024-05-01-preview&preserve-view=true).
+To create a data source, call [Create Data Source (preview)](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2024-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2025-05-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
@@ -227,10 +218,10 @@ The format of the connection string changes based on whether the indexer is usin
 
 The index specifies the fields in a document, attributes, and other constructs that shape the search experience.
 
-To create an index, call [Create Index (preview)](/rest/api/searchservice/indexes/create?view=rest-searchservice-2024-05-01-preview&preserve-view=true):
+To create an index, call [Create Index (preview)](/rest/api/searchservice/indexes/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true):
 
 ```http
-POST https://[service name].search.windows.net/indexes?api-version=2024-05-01-preview
+POST https://[service name].search.windows.net/indexes?api-version=2025-05-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
@@ -260,10 +251,10 @@ If you're using delegated permissions, during this step, you’re asked to sign
 
 There are a few steps to creating the indexer:
 
-1. Send a [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2024-05-01-preview&tabs=HTTP&preserve-view=true) request:
+1. Send a [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true) request:
 
     ```http
-    POST https://[service name].search.windows.net/indexers?api-version=2024-05-01-preview
+    POST https://[service name].search.windows.net/indexers?api-version=2025-05-01-preview
     Content-Type: application/json
     api-key: [admin key]
     
@@ -297,17 +288,17 @@ There are a few steps to creating the indexer:
 
    If you're using application permissions, it's necessary to wait until the initial run is complete before starting to query your index. The following instructions provided in this step pertain specifically to delegated permissions, and aren't applicable to application permissions.
 
-1. When you create the indexer for the first time, the [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2024-05-01-preview&tabs=HTTP&preserve-view=true) request waits until you complete the next step. You must call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2024-05-01-preview&tabs=HTTP&preserve-view=true) to get the link and enter your new device code. 
+1. When you create the indexer for the first time, the [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true) request waits until you complete the next step. You must call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true) to get the link and enter your new device code. 
 
     ```http
-    GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2024-05-01-preview
+    GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2025-05-01-preview
     Content-Type: application/json
     api-key: [admin key]
     ```
 
-    If you don’t run the [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2024-05-01-preview&tabs=HTTP&preserve-view=true) within 10 minutes, the code expires and you’ll need to recreate the [data source](#create-data-source).
+    If you don’t run the [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true) within 10 minutes, the code expires and you’ll need to recreate the [data source](#create-data-source).
 
-1. Copy the device login code from the [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2024-05-01-preview&tabs=HTTP&preserve-view=true) response. The device login can be found in the "errorMessage".
+1. Copy the device login code from the [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true) response. The device login can be found in the "errorMessage".
 
     ```http
     {
@@ -330,18 +321,18 @@ There are a few steps to creating the indexer:
 
     :::image type="content" source="media/search-howto-index-sharepoint-online/aad-app-approve-api-permissions.png" alt-text="Screenshot showing how to approve API permissions.":::
 
-1. The [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2024-05-01-preview&tabs=HTTP&preserve-view=true) initial request completes if all the permissions provided above are correct and within the 10 minute timeframe.
+1. The [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true) initial request completes if all the permissions provided above are correct and within the 10 minute timeframe.
 
 > [!NOTE]
 > If the Microsoft Entra application requires admin approval and was not approved before logging in, you may see the following screen. [Admin approval](/azure/active-directory/manage-apps/grant-admin-consent) is required to continue.
 :::image type="content" source="media/search-howto-index-sharepoint-online/no-admin-approval-error.png" alt-text="Screenshot showing admin approval required.":::
 
 ### Step 7: Check the indexer status
 
-After the indexer has been created, you can call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2024-05-01-preview&tabs=HTTP&preserve-view=true):
+After the indexer has been created, you can call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true):
 
 ```http
-GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2024-05-01-preview
+GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2025-05-01-preview
 Content-Type: application/json
 api-key: [admin key]
 ```
@@ -354,18 +345,18 @@ However, if you modify the data source object while the device code is expired,
 
 Here are the steps for updating a data source, assuming an expired device code:
 
-1. Call [Run Indexer (preview)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2024-05-01-preview&tabs=HTTP&preserve-view=true) to manually start [indexer execution](search-howto-run-reset-indexers.md).
+1. Call [Run Indexer (preview)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true) to manually start [indexer execution](search-howto-run-reset-indexers.md).
 
     ```http
-    POST https://[service name].search.windows.net/indexers/sharepoint-indexer/run?api-version=2024-05-01-preview  
+    POST https://[service name].search.windows.net/indexers/sharepoint-indexer/run?api-version=2025-05-01-preview  
     Content-Type: application/json
     api-key: [admin key]
     ```
 
-1. Check the [indexer status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2024-05-01-preview&tabs=HTTP&preserve-view=true). 
+1. Check the [indexer status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true). 
 
     ```http
-    GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2024-05-01-preview
+    GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2025-05-01-preview
     Content-Type: application/json
     api-key: [admin key]
     ```
@@ -408,7 +399,7 @@ You can control which files are indexed by setting inclusion and exclusion crite
 Include specific file extensions by setting `"indexedFileNameExtensions"` to a comma-separated list of file extensions (with a leading dot). Exclude specific file extensions by setting `"excludedFileNameExtensions"` to the extensions that should be skipped. If the same extension is in both lists, it's excluded from indexing.
 
 ```http
-PUT /indexers/[indexer name]?api-version=2024-05-01-preview
+PUT /indexers/[indexer name]?api-version=2025-05-01-preview
 {
     "parameters" : { 
         "configuration" : { 
@@ -459,7 +450,7 @@ The "query" parameter of the data source is made up of keyword/value pairs. The
 By default, the SharePoint Online indexer stops as soon as it encounters a document with an unsupported content type (for example, an image). You can use the `excludedFileNameExtensions` parameter to skip certain content types. However, you might need to index documents without knowing all the possible content types in advance. To continue indexing when an unsupported content type is encountered, set the `failOnUnsupportedContentType` configuration parameter to false:
 
 ```http
-PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2024-05-01-preview
+PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2025-05-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
@@ -500,6 +491,7 @@ The error message will also include the SharePoint site ID, drive ID, and drive
 
 ## See also
 
++ [YouTube video: SharePoint Online indexer](https://www.youtube.com/watch?v=QmG65Vgl0JI)
 + [Indexers in Azure AI Search](search-indexer-overview.md)
 + [Content metadata properties used in Azure AI Search](search-blob-metadata-properties.md)
 + [Index SharePoint Online content and other sources in Azure AI Search using Azure Logic App connectors](search-how-to-index-logic-apps-indexers.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint Online のインデックス設定手法に関する更新"
}
```

### Explanation
この変更は、Azure AI ドキュメントの「SharePoint Online からのインデックスデータ」についてのページに関するものです。主な変更点は、日付が2025年6月17日に更新され、文言の修正や構成の明確化が行われています。

具体的には、使用方法の説明が簡略化され、ユーザーがプレビュー機能を利用するための登録方法についての文がより明確になりました。特に、SharePoint Online インデクサーの機能に関する具体的な説明が整理され、機能要件や制約事項がより分かりやすく提示されています。

例えば、ドキュメントの削除や増分インデックスの検出に関する情報が強調され、ユーザーが何を期待できるかを明確にしています。また、Microsoft Entra アプリケーションを使用した認証手順やデータソースの作成方法についても、APIバージョンの更新が反映され、最新の情報が提供されています。

これにより、ユーザーはAzure AI Search を用いてSharePoint Online のデータを効果的にインデックス設定するための最新のガイダンスを受けることができます。


