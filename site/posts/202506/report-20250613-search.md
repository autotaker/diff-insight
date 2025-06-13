---
date: '2025-06-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:da65020...MicrosoftDocs:d0f373d
summary: 今回の変更は、Azure AI Searchに関連する文書の軽微な更新が行われたもので、新しい情報の追加や古いデータの更新が主な内容です。具体的には、スコアリングプロファイルやベクトルフィールド、セマンティック検索についての説明が強化され、ユーザーがこれらの機能を効果的に活用できるように情報が明確化されています。また、ベクトルフィールドに関する新セクションやJSONサンプルリクエスト、MRL技術を用いた次元削減の説明が追加されました。特に破壊的な変更はありませんが、APIのバージョンやエンドポイントの情報が更新されているため、古いバージョンを使用しているユーザーは注意が必要です。全体として、ユーザーはより精度の高い検索結果を管理できるようになり、最新の情報に基づいて実務でのAzure
  AI Searchの利用を促進できます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:da65020...MicrosoftDocs:d0f373d){target="_blank"}

<format>
# Highlights
コードの変更は主にAzure AI Searchに関連する文書の軽微な更新であり、新しい情報の追加や古いデータを最新のものに変更することが中心となっています。スコアリングプロファイルやベクトルフィールド、セマンティック検索に関する詳細な説明が強化され、ユーザーがこれらの機能を効果的に活用するための情報が明確化されています。

## New features
- ベクトルフィールドに関する新しいセクションの追加。
- JSONサンプルリクエストの追加。
- MRL技術を用いた次元削減の説明。

## Breaking changes
特筆すべき破壊的変更はありませんが、APIのバージョンや使用するエンドポイントに関する情報が更新されているため、古いバージョンを使用しているユーザーは注意が必要です。

## Other updates
- 文書の日付の更新。
- 記事の表現や見出しの微細な修正。
- ドキュメントの目的の更新（例：概念から手順への変更）。

# Insights
今回の更新は、Azure AI Searchをより深く理解し実務で利用するための情報が整備されていることを示しています。特にスコアリングプロファイルに関しては、新しいAPIバージョンに関する説明や具体的な手順が追加されており、これによりユーザーは検索結果をより精度良く管理できるようになります。

一方で、セマンティック検索関連の文書では、同義語マップの自動適用に関する説明が強調され、正確で関連性の高い検索結果を得るためのガイドとして利用者を支援します。また、ベクトル検索関連の記事では、最新技術の利点を活かす方法が詳述されており、特にストレージと処理速度の最適化を目指した更新が行われています。

この一連の記事の更新を通じて、Azure AI Searchユーザーは、最新の情報に基づいて開発を進めることができ、より効果的かつ効率的な検索サービスの提供が可能となるでしょう。APIの最新機能を活かすための実践的な内容が含まれているため、新規ユーザーのみならず、既存ユーザーも新しい活用方法を学び、システムのパフォーマンス向上を図ることが期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | スコアリングプロファイルの追加方法に関する記事の更新 | modified | 13 | 23 | 36 | 
| [search-get-started-powershell.md](#item-4435d0) | minor update | PowerShellを使用した検索の開始に関する記事の更新 | modified | 77 | 79 | 156 | 
| [search-get-started-rest.md](#item-0df9d5) | minor update | REST APIを使用した検索の開始に関する記事の更新 | modified | 21 | 22 | 43 | 
| [search-get-started-vector.md](#item-4984d9) | minor update | ベクトル検索を使用したクイックスタートガイドの更新 | modified | 1 | 1 | 2 | 
| [semantic-how-to-enable-scoring-profiles.md](#item-e8d524) | minor update | スコアリングプロファイルとセマンティックランキングの統合に関する文書の更新 | modified | 22 | 31 | 53 | 
| [semantic-search-overview.md](#item-b7497b) | minor update | セマンティック検索の概要に関する文書の更新 | modified | 2 | 2 | 4 | 
| [vector-search-how-to-assign-narrow-data-types.md](#item-6b81cd) | minor update | ベクトルフィールドに狭いデータ型を割り当てる方法に関する文書の更新 | modified | 8 | 8 | 16 | 
| [vector-search-how-to-configure-compression-storage.md](#item-c653c3) | minor update | ベクトルストレージ圧縮構成に関する文書の更新 | modified | 17 | 17 | 34 | 
| [vector-search-how-to-truncate-dimensions.md](#item-8350a3) | minor update | テキスト埋め込みモデルの次元を切り詰める方法に関する文書の更新 | modified | 28 | 26 | 54 | 
| [vector-search-multi-vector-fields.md](#item-9aa482) | minor update | 複数ベクトルフィールドにおけるランキング処理に関する文書の更新 | modified | 5 | 2 | 7 | 


# Modified Contents
## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -10,32 +10,28 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 02/25/2025
+ms.date: 06/10/2025
 ---
 
 # Add scoring profiles to boost search scores
 
-Scoring profiles are used to boost the ranking of matching documents based on criteria. In this article, learn how to specify and assign a scoring profile that boosts a search score based on parameters that you provide. 
+Scoring profiles are used to boost the ranking of matching documents based on criteria. In this article, learn how to specify and assign a scoring profile that boosts a search score based on parameters that you provide. You can create scoring profiles based on:
 
-You can use scoring profiles for [keyword search](search-lucene-query-architecture.md), [vector search](vector-search-overview.md), and [hybrid search](hybrid-search-overview.md). However, scoring profiles only apply to nonvector fields, so make sure your index has text or numeric fields that can be used in a scoring profile. 
++ Weighted fields, where boosting is based on a match found in a specific string field. For example, if matches found in a "Subject" field should be more relevant than the same match found in a "Description" field.
 
-## Prerequisites
-
-+ A new or existing search index with text or numeric fields.
-
-You can specify a scoring profile in the index designer in the Azure portal or through APIs like [Create or Update Index REST](/rest/api/searchservice/indexes/create-or-update) or equivalent APIs in any Azure SDK.
++ Functions for numeric data, including dates, ranges, and geographic coordinates. There's also a Tags function that operates on a field providing an arbitrary collection of strings. You can choose this approach over weighted fields if you want to boost a score based on whether a match is found in a tags field.
 
-Scoring profile support for vector and hybrid search is available in 2024-05-01-preview and 2024-07-01 REST APIs and in Azure SDK packages that targeting those releases.
+You can add a scoring profile to an index by editing its JSON definition in the Azure portal or programmatically through APIs like [Create or Update Index REST](/rest/api/searchservice/indexes/create-or-update) or equivalent APIs in any Azure SDK.
 
-## Key points about scoring profiles
+## Prerequisites
 
-Scoring profile parameters are either:
+You can use any API version or SDK package for scoring profiles in keyword search. For vector and hybrid search, use 2024-05-01-preview and 2024-07-01 REST APIs or Azure SDK packages that provide feature parity. For integration between scoring profiles and semantic ranker, use 2025-05-01-preview and later.
 
-+ Weighted fields, where a match is found in a specific string field. For example, you might want matches found in a "summary" field to be more relevant than the same match found in a "content" field.
+## Rules for scoring profiles
 
-+ Functions for numeric data, including dates, ranges, and geographic coordinates. There's also a Tags function that operates on a field providing an arbitrary collection of strings. You can choose this approach over weighted fields if you want to boost a score based on whether a match is found in a tags field.
+You must have a new or existing search index with text or numeric fields. 
 
-You can create multiple profiles and then modify query logic to choose which one is used.
+You can use scoring profiles in [keyword search](search-lucene-query-architecture.md), [vector search](vector-search-overview.md), and [hybrid search](hybrid-search-overview.md). However, scoring profiles only apply to nonvector fields, so make sure your index has text or numeric fields that can be boosted or weighted. 
 
 You can have up to 100 scoring profiles within an index (see [service Limits](search-limits-quotas-capacity.md)), but you can only specify one profile at time in any given query.
 
@@ -76,13 +72,7 @@ The following definition shows a simple profile named "geo". This example boosts
 ]
 ```  
 
-To use this scoring profile, your query is formulated to specify scoringProfile parameter in the request. If you're using the REST API, queries are specified through GET and POST requests. In the following example, "currentLocation" has a delimiter of a single dash (`-`). It's followed by longitude and latitude coordinates, where longitude is a negative value.
-
-```http
-GET /indexes/hotels/docs?search+inn&scoringProfile=geo&scoringParameter=currentLocation--122.123,44.77233&api-version=2024-07-01
-```
-
-Notice the syntax differences when using POST. In POST, "scoringParameters" is plural and it's an array.
+To use this scoring profile, your query is formulated to specify `scoringProfile` parameter in the request. If you're using the REST API, queries are specified through GET and POST requests. In the following example, "currentLocation" has a delimiter of a single dash (`-`). It's followed by longitude and latitude coordinates, where longitude is a negative value.
 
 ```http
 POST /indexes/hotels/docs&api-version=2024-07-01
@@ -119,15 +109,15 @@ For text queries in a hybrid query, scoring profiles identify the maximum 1,000
 
 1. Paste in the [template](#template) provided in this article.  
 
-1. Provide a name that adheres to [naming conventions](/rest/api/searchservice/naming-rules).
+1. Provide a name that adheres to [Azure AI Search naming conventions](/rest/api/searchservice/naming-rules).
 
 1. Specify boosting criteria. A single profile can contain [text weighted fields](#use-text-weighted-fields), [functions](#use-functions), or both. 
 
 You should work iteratively, using a data set that will help you prove or disprove the efficacy of a given profile.
 
 Scoring profiles can be defined in Azure portal as shown in the following screenshot, or programmatically through [REST APIs](/rest/api/searchservice/indexes/create-or-update) or in Azure SDKs, such as the [ScoringProfile](/dotnet/api/azure.search.documents.indexes.models.scoringprofile) class in the Azure SDK for .NET.
 
-   :::image type="content" source="media/scoring-profiles/portal-add-scoring-profile-small.png" alt-text="Add scoring profiles page" lightbox="media/scoring-profiles/portal-add-scoring-profile.png" border="true":::
+:::image type="content" source="media/scoring-profiles/portal-add-scoring-profile-small.png" alt-text="Screenshot showing the Add scoring profile option in the Azure portal." lightbox="media/scoring-profiles/portal-add-scoring-profile.png" border="true":::
 
 ## Use text-weighted fields
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリングプロファイルの追加方法に関する記事の更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchにおけるスコアリングプロファイルの追加方法を説明した文書の更新を反映しています。主な変更点には、スコアリングプロファイルの機能に関する詳細の追加や、必要な前提条件、公式APIのバージョンに関する情報が含まれています。具体的には、重み付けされたフィールドや数値データに関する関数の使用、スコアリングプロファイルを使用するための新しいまたは既存の検索インデックスの要件が強調されています。また、スコアリングプロファイルの作成や操作に関する具体的な手順も改訂されています。全体として、この更新はAzureポータルでの操作やAPIを通じてスコアリングプロファイルを効果的に活用するための情報を示しています。

## articles/search/search-get-started-powershell.md{#item-4435d0}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
 ms.devlang: rest-api
-ms.date: 03/04/2025
+ms.date: 06/12/2025
 ms.custom:
   - mode-api
   - ignite-2023
@@ -180,86 +180,85 @@ To push documents, use an HTTP POST request to your index's URL endpoint. The RE
 
     ```powershell
     $body = @"
-    {
-        "value": [
         {
-        "@search.action": "upload",
-        "HotelId": "1",
-        "HotelName": "Stay-Kay City Hotel",
-        "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
-        "Category": "Boutique",
-        "Tags": [ "pool", "air conditioning", "concierge" ],
-        "ParkingIncluded": false,
-        "LastRenovationDate": "1970-01-18T00:00:00Z",
-        "Rating": 3.60,
-        "Address": 
+            "value": [
             {
-            "StreetAddress": "677 5th Ave",
-            "City": "New York",
-            "StateProvince": "NY",
-            "PostalCode": "10022",
-            "Country": "USA"
-            } 
-        },
-        {
-        "@search.action": "upload",
-        "HotelId": "2",
-        "HotelName": "Old Century Hotel",
-        "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
-        "Category": "Boutique",
-        "Tags": [ "pool", "free wifi", "concierge" ],
-        "ParkingIncluded": false,
-        "LastRenovationDate": "1979-02-18T00:00:00Z",
-        "Rating": 3.60,
-        "Address": 
+            "@search.action": "upload",
+            "HotelId": "1",
+            "HotelName": "Stay-Kay City Hotel",
+            "Description": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
+            "Category": "Boutique",
+            "Tags": [ "view", "air conditioning", "concierge" ],
+            "ParkingIncluded": false,
+            "LastRenovationDate": "2022-01-18T00:00:00Z",
+            "Rating": 3.60,
+            "Address": 
+                {
+                "StreetAddress": "677 5th Ave",
+                "City": "New York",
+                "StateProvince": "NY",
+                "PostalCode": "10022",
+                "Country": "USA"
+                } 
+            },
             {
-            "StreetAddress": "140 University Town Center Dr",
-            "City": "Sarasota",
-            "StateProvince": "FL",
-            "PostalCode": "34243",
-            "Country": "USA"
-            } 
-        },
-        {
-        "@search.action": "upload",
-        "HotelId": "3",
-        "HotelName": "Gastronomic Landscape Hotel",
-        "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
-        "Category": "Resort and Spa",
-        "Tags": [ "air conditioning", "bar", "continental breakfast" ],
-        "ParkingIncluded": true,
-        "LastRenovationDate": "2015-09-20T00:00:00Z",
-        "Rating": 4.80,
-        "Address": 
+            "@search.action": "upload",
+            "HotelId": "2",
+            "HotelName": "Old Century Hotel",
+            "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
+             "Category": "Boutique",
+            "Tags": [ "pool", "free wifi", "concierge" ],
+            "ParkingIncluded": false,
+            "LastRenovationDate": "2019-02-18T00:00:00Z",
+            "Rating": 3.60,
+            "Address": 
+                {
+                "StreetAddress": "140 University Town Center Dr",
+                "City": "Sarasota",
+                "StateProvince": "FL",
+                "PostalCode": "34243",
+                "Country": "USA"
+                } 
+            },
             {
-            "StreetAddress": "3393 Peachtree Rd",
-            "City": "Atlanta",
-            "StateProvince": "GA",
-            "PostalCode": "30326",
-            "Country": "USA"
-            } 
-        },
-        {
-        "@search.action": "upload",
-        "HotelId": "4",
-        "HotelName": "Sublime Palace Hotel",
-        "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.",
-        "Category": "Boutique",
-        "Tags": [ "concierge", "view", "24-hour front desk service" ],
-        "ParkingIncluded": true,
-        "LastRenovationDate": "1960-02-06T00:00:00Z",
-        "Rating": 4.60,
-        "Address": 
+            "@search.action": "upload",
+            "HotelId": "3",
+            "HotelName": "Gastronomic Landscape Hotel",
+            "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
+            "Category": "Suite",
+            "Tags": [ "restaurant", "bar", "continental breakfast" ],
+            "ParkingIncluded": true,
+            "LastRenovationDate": "2015-09-20T00:00:00Z",
+            "Rating": 4.80,
+            "Address": 
+                {
+                "StreetAddress": "3393 Peachtree Rd",
+                "City": "Atlanta",
+                "StateProvince": "GA",
+                "PostalCode": "30326",
+                "Country": "USA"
+                } 
+            },
             {
-            "StreetAddress": "7400 San Pedro Ave",
-            "City": "San Antonio",
-            "StateProvince": "TX",
-            "PostalCode": "78216",
-            "Country": "USA"
+            "@search.action": "upload",
+            "HotelId": "4",
+            "HotelName": "Sublime Palace Hotel",
+            "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.",
+            "Tags": [ "concierge", "view", "air conditioning" ],
+            "ParkingIncluded": true,
+            "LastRenovationDate": "2020-02-06T00:00:00Z",
+            "Rating": 4.60,
+            "Address": 
+                {
+                "StreetAddress": "7400 San Pedro Ave",
+                "City": "San Antonio",
+                "StateProvince": "TX",
+                "PostalCode": "78216",
+                "Country": "USA"
+                }
             }
+          ]
         }
-    ]
-    }
     "@
     ```
 
@@ -343,17 +342,17 @@ Be sure to use single quotation marks on search `$urls`. Query strings include `
                       "Category":  "Boutique",
                       "Tags":  "pool free wifi concierge",
                       "ParkingIncluded":  false,
-                      "LastRenovationDate":  "1979-02-18T00:00:00Z",
+                      "LastRenovationDate":  "2019-02-18T00:00:00Z",
                       "Rating":  3.6,
                       "Address":  "@{StreetAddress=140 University Town Center Dr; City=Sarasota; StateProvince=FL; PostalCode=34243; Country=USA}"
                   },
                   {
                       "@search.score":  0.009068266,
                       "HotelId":  "3",
                       "HotelName":  "Gastronomic Landscape Hotel",
-                      "Description":  "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel\u0027s restaurant services.",
-                      "Category":  "Resort and Spa",
-                      "Tags":  "air conditioning bar continental breakfast",
+                      "Description":  "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel's restaurant services.",
+                      "Category":  "Suite",
+                      "Tags":  "restaurant", "bar", "continental breakfast",
                       "ParkingIncluded":  true,
                       "LastRenovationDate":  "2015-09-20T00:00:00Z",
                       "Rating":  4.8,
@@ -383,7 +382,6 @@ $url = 'https://<YOUR-SEARCH-SERVICE>.search.windows.net/indexes/hotels-quicksta
 
 # Query example 4
 # Sort by a specific field (Address/City) in ascending order
-
 $url = 'https://<YOUR-SEARCH-SERVICE>.search.windows.net/indexes/hotels-quickstart/docs?api-version=2024-07-01&search=pool&$orderby=Address/City asc&$select=HotelName, Address/City, Tags, Rating'
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PowerShellを使用した検索の開始に関する記事の更新"
}
```

### Explanation
このコードの変更は、PowerShellを用いてAzure Searchを始めるための記事に関するもので、主にサンプルコードとその説明に関するアップデートが行われています。全体として、追加された行数は77行、削除された行数は79行であり、変更の詳細には、サンプルデータのホテルの情報が修正され、より具体的で正確な内容が提供されています。例えば、ホテル名や住所、説明文、カテゴリ、タグ、駐車場の有無、評価などが更新され、実際のデータに即した内容に変更されています。また、記事の日付が更新され、最新の情報を反映しています。これにより、読者は最新のAPIエンドポイントや使用方法を確認しやすくなっています。

## articles/search/search-get-started-rest.md{#item-0df9d5}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
 ms.devlang: rest-api
-ms.date: 03/04/2025
+ms.date: 06/12/2025
 ms.custom:
   - mode-api
   - ignite-2023
@@ -247,11 +247,11 @@ The URI is extended to include the `docs` collections and `index` operation.
             "@search.action": "upload",
             "HotelId": "1",
             "HotelName": "Stay-Kay City Hotel",
-            "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
+            "Description": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
             "Category": "Boutique",
-            "Tags": [ "pool", "air conditioning", "concierge" ],
+            "Tags": [ "view", "air conditioning", "concierge" ],
             "ParkingIncluded": false,
-            "LastRenovationDate": "1970-01-18T00:00:00Z",
+            "LastRenovationDate": "2022-01-18T00:00:00Z",
             "Rating": 3.60,
             "Address": 
                 {
@@ -266,11 +266,11 @@ The URI is extended to include the `docs` collections and `index` operation.
             "@search.action": "upload",
             "HotelId": "2",
             "HotelName": "Old Century Hotel",
-            "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
-            "Category": "Boutique",
+            "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
+             "Category": "Boutique",
             "Tags": [ "pool", "free wifi", "concierge" ],
             "ParkingIncluded": false,
-            "LastRenovationDate": "1979-02-18T00:00:00Z",
+            "LastRenovationDate": "2019-02-18T00:00:00Z",
             "Rating": 3.60,
             "Address": 
                 {
@@ -285,9 +285,9 @@ The URI is extended to include the `docs` collections and `index` operation.
             "@search.action": "upload",
             "HotelId": "3",
             "HotelName": "Gastronomic Landscape Hotel",
-            "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
-            "Category": "Resort and Spa",
-            "Tags": [ "air conditioning", "bar", "continental breakfast" ],
+            "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
+            "Category": "Suite",
+            "Tags": [ "restaurant", "bar", "continental breakfast" ],
             "ParkingIncluded": true,
             "LastRenovationDate": "2015-09-20T00:00:00Z",
             "Rating": 4.80,
@@ -304,11 +304,10 @@ The URI is extended to include the `docs` collections and `index` operation.
             "@search.action": "upload",
             "HotelId": "4",
             "HotelName": "Sublime Palace Hotel",
-            "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.",
-            "Category": "Boutique",
-            "Tags": [ "concierge", "view", "24-hour front desk service" ],
+            "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.",
+            "Tags": [ "concierge", "view", "air conditioning" ],
             "ParkingIncluded": true,
-            "LastRenovationDate": "1960-02-06T00:00:00Z",
+            "LastRenovationDate": "2020-02-06T00:00:00Z",
             "Rating": 4.60,
             "Address": 
                 {
@@ -342,7 +341,7 @@ The URI is extended to include a query expression, which is specified by using t
       Authorization: Bearer {{token}}
       
       {
-          "search": "lake view",
+          "search": "attached restaurant",
           "select": "HotelId, HotelName, Tags, Description",
           "searchFields": "Description, Tags",
           "count": true
@@ -357,14 +356,14 @@ The URI is extended to include a query expression, which is specified by using t
       "@odata.count": 1,
       "value": [
         {
-          "@search.score": 0.6189728,
-          "HotelId": "4",
-          "HotelName": "Sublime Palace Hotel",
-          "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.",
+          "@search.score": 0.5575875,
+          "HotelId": "3",
+          "HotelName": "Gastronomic Landscape Hotel",
+          "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel's restaurant services.",
           "Tags": [
-            "concierge",
-            "view",
-            "24-hour front desk service"
+            "restaurant",
+            "bar",
+            "continental breakfast"
           ]
         }
       ]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIを使用した検索の開始に関する記事の更新"
}
```

### Explanation
このコードの変更は、Azure SearchのREST APIを使用した入門ガイドの記事に関するもので、主にサンプルデータの更新とドキュメントの日付の変更が中心です。記事内の数か所で、ホテルの説明やカテゴリ、タグ、最終改装日などの情報が修正され、より正確で時代に即した内容になっています。例えば、「Stay-Kay City Hotel」の説明が詳細化され、タグが「view」を追加する形で変更されています。また、ホテルの改装日や一部のタグにおいても、適切な更新が行われています。

日付も最新のものに変更され、記事が最新の情報を反映していることが示されています。この更新により、ユーザーは現在のデータを使用してAPIをより効果的に活用するための情報を得ることができます。

## articles/search/search-get-started-vector.md{#item-4984d9}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: quickstart
-ms.date: 03/04/2025
+ms.date: 06/12/2025
 ---
 
 # Quickstart: Vector search using REST
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索を使用したクイックスタートガイドの更新"
}
```

### Explanation
今回の変更は、Azure Searchにおけるベクトル検索のクイックスタートガイドに関するもので、主にドキュメントの日付に関する更新が行われました。具体的には、記事の日付が「2025年3月4日」から「2025年6月12日」に変更されました。この更新は、ユーザーに最新の情報が提供されていることを示しており、ドキュメントが現在のタイムラインに適合していることを強調しています。全体としては、追加や削除の行数がそれぞれ1行で、内容は最小限の修正ですが、重要な情報更新を含んでいます。これにより、読者は最新のガイドラインに従ってベクトル検索を効果的に利用できるようになります。

## articles/search/semantic-how-to-enable-scoring-profiles.md{#item-e8d524}

<details>
<summary>Diff</summary>
````diff
@@ -1,58 +1,51 @@
 ---
-title: Integrate Scoring Profiles with Semantic Ranking
+title: Use Scoring Profiles with Semantic Ranking
 titleSuffix: Azure AI Search
 description: Learn how to combine scoring profiles with semantic ranking in Azure AI Search to optimize final document relevance.
 author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/07/2025
+ms.date: 06/10/2025
 ---
 
-# Integrating scoring profiles with semantic ranker in Azure AI Search
+# Use scoring profiles with semantic ranker in Azure AI Search
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-Integrating [scoring profiles](index-add-scoring-profiles.md) with [semantic ranker](semantic-search-overview.md) is now possible in Azure AI Search. Semantic ranker adds a new field, `@search.rerankerBoostedScore`, to help you maintain consistent relevance and greater control over final ranking outcomes in your search pipeline.
+Integrating [scoring profiles](index-add-scoring-profiles.md) with [semantic ranker](semantic-search-overview.md) is supported in newer Azure AI Search API versions and Azure SDK packages. Semantic ranker adds a new field, `@search.rerankerBoostedScore`, to help you maintain consistent relevance and greater control over final ranking outcomes in your search pipeline.
 
-Before this integration, scoring profiles only influenced the initial ranking phase of search results. The boost values they applied affected:
-- [BM25-ranked](index-similarity-and-scoring.md) or [RRF-ranked](hybrid-search-ranking.md) results for text-based queries
-- The text portion of vector queries
-- Hybrid queries that included both text and vector components
-
-However, once the semantic ranker re-ranked the results, those boosts no longer had any effect. The semantic reranking process ignored scoring profiles entirely.
-
-Integrating scoring profiles with semantic ranker addresses this behavior by allowing you to apply those profiles directly at the reranking level, ensuring that the boosts are taken into account.
+Before this integration, scoring profiles only influenced the initial L1 ranking phase of [BM25-ranked](index-similarity-and-scoring.md) and [RRF-ranked](hybrid-search-ranking.md) search results. However, once the semantic L2 ranker re-ranked the results, those boosts no longer had any effect. The semantic reranking process ignored scoring profiles entirely.
 
+Integrating scoring profiles with semantic ranker addresses this behavior by applying scoring profiles to L2-ranked results, ensuring that the boosts are taken into account.
 
 ## Prerequisites
 
-- An [Azure AI Search service](search-what-is-azure-search.md) with [semantic ranker enabled](semantic-how-to-configure.md).
+- [Azure AI Search](search-create-service-portal.md), Basic pricing tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
+- REST API version `2025-05-01-preview` or a prerelease Azure SDK package that provides the new APIs. For all preview features, we recommend reviewing the Azure SDK change logs for feature availability: [Python SDK change log](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [.NET SDK change log](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md), [Java SDK change log](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [JavaScript SDK change log](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md).
 
 ## How does semantic configuration with scoring profiles work?
 
-When you execute a semantic query associated with a scoring profile, another `@search.rerankerBoostedScore` value is generated in every document in your search results. This boosted score, calculated by applying the scoring profile to the existing reranker score, doesn't have a guaranteed range (0–4) like a normal reranker score, but it can be higher than 4.
+When you execute a semantic query associated with a scoring profile, a third search score, `@search.rerankerBoostedScore` value, is generated for every document in your search results. This boosted score, calculated by applying the scoring profile to the existing reranker score, doesn't have a guaranteed range (0–4) like a normal reranker score, and scores can be significantly higher than 4.
 
 Starting in API version `2025-05-01-preview`, semantic results are sorted by `@search.rerankerBoostedScore` by default. If the `rankingOrder` property isn't specified, then `boostedReRankerScore` is the default value in the semantic configuration.
 
 When this capability is enabled, the scoring profile defined in your index applies during the initial ranking phase.
 It boosts results from:
+
 - Text-based queries (BM25 or RRF)
 - The text portion of vector queries
 - Hybrid queries that combine both types
 
 The semantic ranker then reprocesses the top 50 results. It also reapplies the scoring profile after reranking, so your boosts influence the final order of results.
 
+## Enable scoring profiles in semantic configuration
 
-## Enabling scoring profiles in semantic configuration
-
-To integrate scoring profiles with semantic ranking, configure it using API version `2025-05-01-preview`. Use the PUT method to update the index with the semantic configuration.
-
-### Example: Enable boosted reranker score
+To enable scoring profiles with semantic ranking, use preview API version `2025-05-01-preview` to update an index by setting the `rankingOrder` property of its semantic configuration. Use the PUT method to update the index with your revisions. No index rebuild is required.
 
 ```json
-PUT https://{service-name}.search.windows.com/indexes/{index-name}?api-version=2024-05-01-Preview
+PUT https://{service-name}.search.windows.com/indexes/{index-name}?api-version=2025-05-01-Preview
 {
   "semantic": {
     "configurations": [
@@ -65,12 +58,9 @@ PUT https://{service-name}.search.windows.com/indexes/{index-name}?api-version=2
 }
 ```
 
+## Disable scoring profiles in semantic configuration
 
-## Disabling scoring profiles in semantic configuration
-
-If you want to opt out of sorting by semantic reranker boosted score, set the `rankingOrder` field to `reRankerScore` value in the semantic configuration.
-
-### Example: Disable boosted reranker score
+To opt out of sorting by semantic reranker boosted score, set the `rankingOrder` field to `reRankerScore` value in the semantic configuration.
 
 ```json
 PUT https://{service-name}.search.windows.com/indexes/{index-name}?api-version=2024-05-01-Preview
@@ -85,22 +75,23 @@ PUT https://{service-name}.search.windows.com/indexes/{index-name}?api-version=2
   }
 }
 ```
-Even if you opt out of sorting by `@search.rerankerBoostedScore`, the field is still produced in the response. It simply isn't used to sort results.
 
+Even if you opt out of sorting by `@search.rerankerBoostedScore`, the `boostedReRankerScore` field is still produced in the response, but it's no longer used to sort results. 
+
+## Example query and response
+
+Start with a [semantic query](semantic-how-to-query-request.md) that specifies a scoring profile. The query uses the new preview REST API, and it targets a search index that has `rankingOrder` set to `boostedReRankerScore`.
 
-### Sample Request and Response
 ```json
-POST https://{service-name}.search.windows.com/indexes/{index-name}/docs/search?api-version=2024-05-01-Preview
+POST https://{service-name}.search.windows.com/indexes/{index-name}/docs/search?api-version=2025-05-01-Preview
 {
   "search": "my query to be boosted",
   "scoringProfile": "myScoringProfile",
   "queryType": "semantic"
 }
 ```
 
-> [!NOTE]
-> For this request to apply the semantic profile, it must be enabled in the semantic configuration as shown earlier.
-
+The response includes the new `rerankerBoostedScore`, alongside the L1 `@search.score` and the L2 `@search.rerankerSocre`. Results are ordered by `@search.rerankerBoostedScore`.
 
 ```json
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリングプロファイルとセマンティックランキングの統合に関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるスコアリングプロファイルとセマンティックランキングの統合に関する文書の更新を示しています。主な変更点として、タイトルの表現が更新され、日付が「2025年5月7日」から「2025年6月10日」に変更されています。

内容面では、スコアリングプロファイルが新しいAPIバージョンに対応しており、L1およびL2のランキングフェーズにおけるスコアの適用について詳しく説明されています。具体的には、スコアリングプロファイルの適用がL2ランキングの結果にも影響を与えることが強調され、これにより最終的な結果順序を改善する仕組みが明示されています。また、新しいJSONサンプルリクエストが追加され、更新されたAPIエンドポイントが示されています。

これにより、ユーザーはセマンティック検索でのスコアリングプロファイルの効果的な活用方法を学ぶことができ、検索結果の関連性を向上させる手助けとなっています。全体として、この文書は最新の情報を提供し、実践的な例を通じて使用方法を明確にしています。

## articles/search/semantic-search-overview.md{#item-b7497b}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 05/08/2025
+ms.date: 06/10/2025
 ---
 
 # Semantic ranking in Azure AI Search
@@ -133,7 +133,7 @@ The following video provides an overview of the capabilities.
 
 ## How semantic ranker uses synonym maps
 
-If a you have already enabled support for [synonym maps associated to a field](search-synonyms.md#assign-synonyms-to-fields) in your search index, and that field is included in the [semantic ranker configuration](semantic-how-to-configure.md), the semantic ranker will automatically apply the configured synonyms during the reranking process.
+If you have already enabled support for [synonym maps associated to a field](search-synonyms.md#assign-synonyms-to-fields) in your search index, and that field is included in the [semantic ranker configuration](semantic-how-to-configure.md), the semantic ranker will automatically apply the configured synonyms during the reranking process.
 
 
 ## Availability and pricing
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティック検索の概要に関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchのセマンティック検索に関する文書の軽微な更新を示しています。主な変更点は、文書の日付が「2025年5月8日」から「2025年6月10日」に更新されたことと、特定の文の表現がわずかに修正された点です。

具体的には、同義語マップのサポートが有効になっている場合、そのフィールドがセマンティックランカーの設定に含まれていると、セマンティックランカーが再ランキングプロセス中に設定された同義語を自動的に適用することが説明されています。この内容は事実上変わっていないものの、表現のわずかな修正により、内容がより明確に伝わるようになっています。

この更新は、ユーザーがセマンティック検索機能の利用時に発生する可能性のある混乱を軽減し、最新の情報を提供することを目的としています。全体として、この変更はドキュメントの正確性と信頼性を向上させるものとなっています。

## articles/search/vector-search-how-to-assign-narrow-data-types.md{#item-6b81cd}

<details>
<summary>Diff</summary>
````diff
@@ -9,18 +9,18 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 06/12/2025
 ---
 
 # Assign narrow data types to vector fields in Azure AI Search
 
-An easy way to reduce vector size is to store embeddings in a smaller data format. Most embedding models output 32-bit floating point numbers, but if you quantize your vectors, or if your embedding model supports it natively, output might be float16, int16, or int8, which is significantly smaller than float32. You can accommodate these smaller vector sizes by assigning a narrow data type to a vector field. In the vector index, narrow data types consume less storage.
+An easy way to reduce vector size is to store embeddings in a smaller data format. Most embedding models output 32-bit floating point numbers. However, if you quantize your vectors or use an embedding model that natively supports quantization, the output might be float16, int16, or int8, which are significantly smaller than float32. You can accommodate these smaller vector sizes by assigning a narrow data type to a vector field. In the vector index, narrow data types consume less storage.
 
 Data types are assigned to fields in an index definition. You can use the Azure portal, the [Search REST APIs](/rest/api/searchservice/indexes/create), or an Azure SDK package that provides the feature.
 
 ## Prerequisites
 
-- An embedding model that output small data formats, such as text-embedding-3 or Cohere V3 embedding models.
+- An embedding model that outputs small data formats, such as text-embedding-3 or Cohere V3 embedding models.
 
 ## Supported narrow data types
 
@@ -32,18 +32,18 @@ Data types are assigned to fields in an index definition. You can use the Azure
    - `Collection(Edm.SByte)` 8-bit signed integer (narrow)
    - `Collection(Edm.Byte)` 8-bit unsigned integer (only allowed with packed binary data types)
 
-1. From that list, determine which data type is valid for your embedding model's output, or for vectors that undergo custom quantization.
+1. From that list, determine which data type is valid for your embedding model's output or for vectors that undergo custom quantization.
 
    The following table provides links to several embedding models that can use a narrow data type (`Collection(Edm.Half)`) without extra quantization. You can cast from float32 to float16 (using `Collection(Edm.Half)`) with no extra work.
 
-   | Embedding model        | Native output | Assign this type in Azure AI Search |
+   | Embedding model | Native output | Assign this type in Azure AI Search |
    |------------------------|---------------|--------------------------------|
    | [text-embedding-ada-002](/azure/ai-services/openai/concepts/models#embeddings) | `Float32` | `Collection(Edm.Single)` or `Collection(Edm.Half)` |
    | [text-embedding-3-small](/azure/ai-services/openai/concepts/models#embeddings) | `Float32` | `Collection(Edm.Single)` or `Collection(Edm.Half)` |
    | [text-embedding-3-large](/azure/ai-services/openai/concepts/models#embeddings) | `Float32` | `Collection(Edm.Single)` or `Collection(Edm.Half)` |
    | [Cohere V3 embedding models with int8 embedding_type](https://docs.cohere.com/reference/embed) | `Int8` | `Collection(Edm.SByte)` |
 
-   Other narrow data types can be used if your model emits embeddings in the smaller data format, or if you have custom quantization that converts vectors to a smaller format.
+   You can use other narrow data types if your model emits embeddings in the smaller data format or if you have custom quantization that converts vectors to a smaller format.
 
 1. Make sure you understand the tradeoffs of a narrow data type. `Collection(Edm.Half)` has less information, which results in lower resolution. If your data is homogenous or dense, losing extra detail or nuance could lead to unacceptable results at query time because there's less detail that can be used to distinguish nearby vectors apart.
 
@@ -84,7 +84,7 @@ Data types are assigned on new fields when they're created. You can't change the
 
 1. Verify the field content matches the data type. Assuming the vector field is marked as `retrievable`, use [Search explorer](search-explorer.md) or [Search - POST](/rest/api/searchservice/documents/search-post?) to return vector field content.
 
-1. To check vector index size, refer to the vector index size column on the **Search management > Indexes** page in the [Azure portal](https://portal.azure.com) or use the [GET Statistics (REST API)](/rest/api/searchservice/indexes/get-statistics) or equivalent Azure SDK method to get the size.
+1. To check vector index size, refer to the vector index size column on the **Search management > Indexes** page in the [Azure portal](https://portal.azure.com). Alternatively, you can use [GET Index Statistics (REST API)](/rest/api/searchservice/indexes/get-statistics) or an equivalent Azure SDK method.
 
 > [!NOTE]
-> The field's data type is used to create the physical data structure. If you want to change a data type later, either [drop and rebuild the index](search-howto-reindex.md), or create a second field with the new definition.
+> The field's data type is used to create the physical data structure. If you want to change a data type later, either [drop and rebuild the index](search-howto-reindex.md) or create a second field with the new definition.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルフィールドに狭いデータ型を割り当てる方法に関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるベクトルフィールドへの狭いデータ型の割り当てに関する文書の軽微な更新を示しています。主な変更点は、文書の日付が「2024年11月19日」から「2025年6月12日」に更新されたことと、いくつかの文が表現上の調整を受けている点です。

具体的には、ベクトルサイズを削減する手段や狭いデータ型の概念についての説明がクリアになり、情報の整合性が向上しています。また、データ型を確認する際の手続きを明確にし、AzureポータルやREST APIの利用方法を具体的に言及しています。

このように更新された内容は、ユーザーがベクトルフィールドのデータ型を適切に設定し、ストレージの効率を向上させるために必要な情報をより効果的に提供することを目的としています。このドキュメントの改善により、ユーザーは狭いデータ型を使用する際の利点や注意点を理解しやすくなり、実際の実装に役立てることができます。

## articles/search/vector-search-how-to-configure-compression-storage.md{#item-c653c3}

<details>
<summary>Diff</summary>
````diff
@@ -8,52 +8,52 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
-ms.topic: concept-article
-ms.date: 11/19/2024
+ms.topic: how-to
+ms.date: 06/12/2025
 ---
 
 # Choose an approach for optimizing vector storage and processing
 
 Embeddings, or the numerical representation of heterogeneous content, are the basis of vector search workloads, but the sizes of embeddings make them hard to scale and expensive to process. Significant research and productization have produced multiple solutions for improving scale and reducing processing times. Azure AI Search taps into a number these capabilities for faster and cheaper vector workloads.
 
-This article enumerates all of optimization techniques in Azure AI Search that can help you reduce vector size and query processing times. 
+This article covers all of the optimization techniques in Azure AI Search that can help you reduce vector size and query processing times.
 
-Vector optimization settings are specified in vector field definitions in a search index. Most of the features described in this article are generally available in [2024-07-01 REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-07-01&preserve-view=true) and in the Azure SDK packages targeting that version. The [latest preview version](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-09-01-preview&preserve-view=true) adds support for truncated dimensions if you're using text-embedding-3-large or text-embedding-3-small for vectorization.
+Vector optimization settings are specified in vector field definitions in a search index. Most of the features described in this article are generally available in the [2024-07-01 REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-07-01&preserve-view=true) and Azure SDK packages targeting that version. The [latest preview version](/rest/api/searchservice/search-service-api-versions#preview-versions) adds support for truncated dimensions if you're using text-embedding-3-large or text-embedding-3-small for vectorization.
 
 ## Evaluate the options
 
 Review the approaches in Azure AI Search for reducing the amount of storage used by vector fields. These approaches aren't mutually exclusive and can be combined for [maximum reduction in vector size](#example-vector-size-by-vector-compression-technique).
 
-We recommend built-in quantization because it compresses vector size in memory *and* on disk with minimal effort, and that tends to provide the most benefit in most scenarios. In contrast, narrow types (except for float16) require a special effort into making them, and `stored` saves on disk storage, which isn't as expensive as memory.
+We recommend built-in quantization because it compresses vector size in memory *and* on disk with minimal effort, which tends to provide the most benefit in most scenarios. In contrast, narrow types (except for float16) require special effort to create them, and `stored` saves on disk storage, which isn't as expensive as memory.
 
-| Approach | Why use this option |
+| Approach | Why use this approach |
 |----------|---------------------|
-| [Add scalar or binary quantization](vector-search-how-to-quantization.md) | Use quantization to compress native float32 or float16  embeddings to  int8  (scalar) or Byte (binary). This option reduces storage in memory and on disk with no degradation of query performance. Smaller data types like int8 or Byte produce vector indexes that are less content-rich than those with larger embeddings. To offset information loss, built-in compression includes options for post-query processing using uncompressed embeddings and oversampling to return more relevant results. Reranking and oversampling are specific features of built-in quantization of float32 or float16 fields and can't be used on embeddings that undergo custom quantization. |
-| [Truncate dimensions for MRL-capable text-embedding-3 models (preview)](vector-search-how-to-truncate-dimensions.md) | Exercise the option to use fewer dimensions on text-embedding-3 models. On Azure OpenAI, these models have been retrained on the [Matryoshka Representation Learning (MRL)](https://arxiv.org/abs/2205.13147) technique that produces multiple vector representations at different levels of compression. This approach produces faster searches and reduced storage costs, with minimal loss of semantic information. In Azure AI Search, MRL support supplements scalar and binary quantization. When you use either quantization method, you can also specify a `truncateDimension` property on your vector fields to reduce the dimensionality of text embeddings. |
-| [Assign smaller primitive data types to vector fields](vector-search-how-to-assign-narrow-data-types.md) | Narrow data types, such as float16, int16,  int8, and Byte (binary) consume less space in memory and on disk, but you must have an embedding model that outputs vectors in a narrow data format. Or, you must have custom quantization logic that outputs small data. A third use case that requires less effort is recasting native float32 embeddings produced by most models to float16. See [Index binary vectors](vector-search-how-to-index-binary-data.md) for details about binary vectors. |
+| [Add scalar or binary quantization](vector-search-how-to-quantization.md) | Compress native float32 or float16 embeddings to int8 (scalar) or byte (binary). This option reduces storage in memory and on disk with no degradation of query performance. Smaller data types, such as int8 or byte, produce vector indexes that are less content-rich than those with larger embeddings. To offset information loss, built-in compression includes options for post-query processing using uncompressed embeddings and oversampling to return more relevant results. Reranking and oversampling are specific features of built-in quantization of float32 or float16 fields and can't be used on embeddings that undergo custom quantization. |
+| [Truncate dimensions for MRL-capable text-embedding-3 models (preview)](vector-search-how-to-truncate-dimensions.md) | Use fewer dimensions on text-embedding-3 models. On Azure OpenAI, these models are retrained on the [Matryoshka Representation Learning](https://arxiv.org/abs/2205.13147) (MRL) technique that produces multiple vector representations at different levels of compression. This approach produces faster searches and reduced storage costs with minimal loss of semantic information. In Azure AI Search, MRL support supplements scalar and binary quantization. When you use either quantization method, you can also specify a `truncateDimension` property on your vector fields to reduce the dimensionality of text embeddings. |
+| [Assign smaller primitive data types to vector fields](vector-search-how-to-assign-narrow-data-types.md) | Narrow data types, such as float16, int16, int8, and byte (binary), consume less space in memory and on disk, but you must have an embedding model that outputs vectors in a narrow data format. Alternatively, you must have custom quantization logic that outputs small data. A third use case that requires less effort is recasting native float32 embeddings produced by most models to float16. For information about binary vectors, see [Index binary vectors](vector-search-how-to-index-binary-data.md). |
 | [Eliminate optional storage of retrievable vectors](vector-search-how-to-storage-options.md) | Vectors returned in a query response are stored separately from vectors used during query execution. If you don't need to return vectors, you can turn off retrievable storage, reducing overall per-field disk storage by up to 50 percent. |
 
 All of these options are defined on an empty index. To implement any of them, use the Azure portal, REST APIs, or an Azure SDK package targeting that API version.
 
 After the index is defined, you can load and index documents as a separate step.
 
-## Example: vector size by vector compression technique
+## Example: Vector size by vector compression technique
 
 [Code sample: Vector quantization and storage options using Python](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/vector-quantization-and-storage/README.md) is a Python code sample that creates multiple search indexes that vary by their use of vector storage quantization, [narrow data types](vector-search-how-to-assign-narrow-data-types.md), and [storage properties](vector-search-how-to-storage-options.md).
 
 This code creates and compares storage and vector index size for each vector storage optimization option. From these results, you can see that [quantization](vector-search-how-to-quantization.md) reduces vector size the most, but the greatest storage savings are achieved if you use multiple options.
 
 | Index name | Storage size | Vector size |
 |------------|--------------|-------------|
-| compressiontest-baseline | 21.3613MB | 4.8277MB |
-| compressiontest-scalar-compression | 17.7604MB | 1.2242MB |
-| compressiontest-narrow | 16.5567MB | 2.4254MB |
-| compressiontest-no-stored | 10.9224MB | 4.8277MB  |
-| compressiontest-all-options | 4.9192MB | 1.2242MB |
+| compressiontest-baseline | 21.3613 MB | 4.8277 MB |
+| compressiontest-scalar-compression | 17.7604 MB | 1.2242 MB |
+| compressiontest-narrow | 16.5567 MB | 2.4254 MB |
+| compressiontest-no-stored | 10.9224 MB | 4.8277 MB |
+| compressiontest-all-options | 4.9192 MB | 1.2242 MB |
 
-Search APIs report storage and vector size at the index level, so indexes and not fields must be the basis of comparison. Use the [GET Index Statistics](/rest/api/searchservice/indexes/get-statistics) or an equivalent API in the Azure SDKs to obtain vector size.
+Search APIs report storage and vector size at the index level, so indexes and not fields must be the basis of comparison. Use [GET Index Statistics](/rest/api/searchservice/indexes/get-statistics) or an equivalent API in the Azure SDKs to obtain vector size.
 
-## See also
+## Related content
 
 - [Get started with REST](search-get-started-rest.md)
 - [Supported data types](/rest/api/searchservice/supported-data-types)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルストレージ圧縮構成に関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchのベクトルストレージ圧縮に関する構成方法に関する文書の軽微な更新を示しています。主な変更点は、文書の日付が「2024年11月19日」から「2025年6月12日」に更新されたこと、及び文書のトピックが「概念記事」から「手順」に変更されたことです。

具体的には、ベクトルストレージの最適化手法に関する説明がわかりやすくなり、いくつかの表現が修正されて内容の明確さが向上しています。また、各手法の具体的な利点と使用方法について詳細に記載されており、特にビルトイン量子化のおすすめについて強調されています。

これにより、ユーザーはベクトルフィールドのストレージを効率的に管理し、処理速度を向上させるための手法をより効果的に利用できるようになります。この更新は、最適化技術の理解を深め、具体的な実装に役立つ情報を提供することを目的としています。

## articles/search/vector-search-how-to-truncate-dimensions.md{#item-8350a3}

<details>
<summary>Diff</summary>
````diff
@@ -1,73 +1,71 @@
 ---
 title: Truncate dimensions
 titleSuffix: Azure AI Search
-description: Truncate dimensions on text-embedding-3 models using Matryoshka Representation Learning (MRL) compression
+description: Truncate dimensions on text-embedding-3 models using Matryoshka Representation Learning (MRL) compression.
 
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 06/12/2025
 ---
 
 # Truncate dimensions using MRL compression (preview)
 
 > [!IMPORTANT]
-> This feature is in public preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [preview REST API](/rest/api/searchservice/search-service-api-versions#preview-versions) supports this feature.
+> This feature is in public preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). We recommend the latest [preview REST API version](/rest/api/searchservice/search-service-api-versions#preview-versions) for this feature.
 
-Exercise the ability to use fewer dimensions on text-embedding-3 models. On Azure OpenAI, text-embedding-3 models are retrained on the [Matryoshka Representation Learning (MRL)](https://arxiv.org/abs/2205.13147) technique that produces multiple vector representations at different levels of compression. This approach produces faster searches and reduced storage costs, with minimal loss of semantic information. 
+Exercise the ability to use fewer dimensions on text-embedding-3 models. On Azure OpenAI, text-embedding-3 models are retrained on the [Matryoshka Representation Learning](https://arxiv.org/abs/2205.13147) (MRL) technique that produces multiple vector representations at different levels of compression. This approach produces faster searches and reduced storage costs with minimal loss of semantic information.
 
-In Azure AI Search, MRL support supplements [scalar and binary quantization](vector-search-how-to-quantization.md). When you use either quantization method, you can also specify a `truncationDimension` property on your vector fields to reduce the dimensionality of text embeddings. 
+In Azure AI Search, MRL support supplements [scalar and binary quantization](vector-search-how-to-quantization.md). When you use either quantization method, you can specify a `truncationDimension` property on your vector fields to reduce the dimensionality of text embeddings.
 
-MRL multilevel compression saves on vector storage and improves query response times for vector queries based on text embeddings. In Azure AI Search, MRL support is only offered together with another method of quantization. Using binary quantization with MRL provides the maximum vector index size reduction. To achieve maximum storage reduction, use binary quantization with MRL, and `stored` set to false.
-
-This feature is in preview. It's available in `2024-09-01-preview` and in beta SDK packages targeting that preview API version.
+MRL multilevel compression saves on vector storage and improves query response times for vector queries based on text embeddings. In Azure AI Search, MRL support is only offered together with another method of quantization. Using binary quantization with MRL provides the maximum vector index size reduction. To achieve maximum storage reduction, use binary quantization with MRL and set `stored` to false.
 
 ## Prerequisites
 
-- Text-embedding-3 models such as Text-embedding-3-small or Text-embedding-3-large (text content only).
+- A text-embedding-3 model, such as text-embedding-3-small or text-embedding-3-large.
+
+- A [supported client](#supported-clients).
 
-- [New vector fields](vector-search-how-to-create-index.md) of type `Edm.Half` or `Edm.Single` (you can't add MRL compression to an existing field).
+- [New vector fields](vector-search-how-to-create-index.md) of type `Edm.Half` or `Edm.Single`. You can't add MRL compression to an existing field.
 
-- [Hierarchical Navigable Small World (HNSW)algorithm](vector-search-ranking.md) (no support for exhaustive KNN in this preview).
+- [Hierarchical Navigable Small World (HNSW) algorithm](vector-search-ranking.md). This preview doesn't support exhaustive KNN.
 
 - [Scalar or binary quantization](vector-search-how-to-quantization.md). Truncated dimensions can be set only when scalar or binary quantization is configured. We recommend binary quantization for MRL compression.
 
-## Supported clients
+### Supported clients
 
-You can use the REST APIs or Azure SDK beta packages to implement MRL compression.
+You can use the REST APIs or Azure SDK beta packages to implement MRL compression. At this time, there's no Azure portal or Azure AI Foundry support.
 
-- [REST API 2024-09-01-preview](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) or [REST API 2024-11-01-preview](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true)
+- [REST API 2024-09-01-preview](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) or later. We recommend the latest preview API.
 
 - Check the change logs for each Azure SDK beta package: [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md), [Java](https://github.com/Azure/azure-sdk-for-java/blob/azure-search-documents_11.1.3/sdk/search/azure-search-documents/CHANGELOG.md), [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md).
 
-There's no Azure portal or Azure AI Foundry support at this time.
-
-## How to use MRL-extended text embeddings
+## Use MRL-extended text embeddings
 
-MRL is a capability that's built into the text embedding model you're already using. To benefit from those capabilities in Azure AI Search, follow these steps.
+MRL is built into the text embedding model you're already using. To use MRL capabilities in Azure AI Search:
 
-1. Use the [Create or Update index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) or equivalent API to specify the index schema.
+1. Use [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) or an equivalent API to specify the index schema.
 
 1. [Add vector fields](vector-search-how-to-create-index.md) to the index definition.
 
 1. Specify a `vectorSearch.compressions` object in your index definition.
 
 1. Include a quantization method, either scalar or binary (recommended).
 
-1. Include the `truncationDimension` parameter set to 512, or as low as 256 if you use the text-embedding-3-large model.
+1. Include the `truncationDimension` parameter and set it to 512. If you're using the text-embedding-3-large model, you can set it as low as 256.
 
-1. Specify a vector profile that specifies the HNSW algorithm and the vector compression object.
+1. Include a vector profile that specifies the HNSW algorithm and the vector compression object.
 
 1. Assign the vector profile to a vector field of type `Edm.Half` or `Edm.Single` in the fields collection.
 
-There are no query-side modifications for using an MRL-capable text embedding model. Integrated vectorization, text-to-query conversions at query time, semantic ranking and other relevance enhancement features such as reranking with original vectors and oversampling are unaffected by MRL support.
+There are no query-side modifications for using an MRL-capable text embedding model. MRL support doesn't affect integrated vectorization, text-to-query conversions at query time, semantic ranking, and other relevance-enhancement features, such as reranking with original vectors and oversampling.
 
-Indexing is slower due to the extra steps, but queries are faster.
+Although indexing is slower due to the extra steps, queries are faster.
 
-## Example of a vector search configuration that supports MRL
+## Example: Vector search configuration that supports MRL
 
 The following example illustrates a vector search configuration that meets the requirements and recommendations of MRL.
 
@@ -114,9 +112,13 @@ The following example illustrates a vector search configuration that meets the r
 } 
 ```
 
-Here's an example of a [fully specified vector field definition](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true#searchfield) that satisfies the requirements for MRL.
+Here's an example of a [fully specified vector field definition](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true#searchfield) that satisfies the requirements for MRL. Recall that vector fields must:
+
+- Be of type `Edm.Half` or `Edm.Single`.
+
+- Have a `vectorSearchProfile` property that specifies the algorithm and compression settings.
 
-Recall that vector fields must be of type `Edm.Half` or `Edm.Single`. Vector fields must have a `vectorSearchProfile` property that determines the algorithm and compression settings. Vector fields have a `dimensions` property used for specifying the number of dimensions for scoring and ranking results. Its value should be dimensions limit of the model you're using (1,536 for text-embedding-3-small).
+- Have a `dimensions` property that specifies the number of dimensions for scoring and ranking results. Its value should be the dimensions limit of the model you're using (1,536 for text-embedding-3-small).
 
 ```json
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト埋め込みモデルの次元を切り詰める方法に関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるテキスト埋め込みモデルの次元を切り詰める方法に関する文書の軽微な更新を示しています。主な変更点は、文書の日付が「2024年11月19日」から「2025年6月12日」に更新されたこと、および文書内のいくつかの表現や構文が改善された点です。

具体的には、この文書ではMatryoshka Representation Learning（MRL）技術を用いてテキスト埋め込みモデルの次元を削減する方法が説明されています。これにより、検索の高速化やストレージコストの削減が実現されることが強調されています。また、MRL機能の利用にあたり必要な前提条件や、推奨されるAPIのバージョンが明確に記載されており、ユーザーが容易に理解できるようになっています。

さらに、次元を切り詰める際の具体的な実装手順や、MRLを活用する際の注意点が詳述され、利用者が効果的にこの技術を活用できるよう配慮されています。このような文書の改善により、ユーザーはMRL技術を用いたベクトル検索に対する理解を深め、実装を円滑に進めることが可能になります。

## articles/search/vector-search-multi-vector-fields.md{#item-9aa482}

<details>
<summary>Diff</summary>
````diff
@@ -140,6 +140,7 @@ Additionally, a new query time parameter is available: `perDocumentVectorLimit`.
   "select": "title, scenes/timestamp, scenes/framePath"
 }
 ```
+
 ## Ranking across multiple vectors in a single field
 
 When multiple vectors are associated with a single document, Azure AI Search uses the maximum score among them for ranking. The system uses the most relevant vector to score each document, which prevents dilution by less relevant ones.
@@ -223,13 +224,15 @@ POST /indexes/my-index/docs/search?api-version=2025-05-01-preview
 | `searchScore`     | Final score for that field, after any rescoring and boosts.             |
 | `vectorSimilarity`| Raw similarity returned by the distance function.                        |
 
-
 > [!NOTE]
 > `innerHits` currently reports only vector fields.
 
 ### Relationship to debug=vector
+
 Here are some facts about this property:
+
 - The existing `debug=vector` switch remains unchanged.
+
 - When used with multi-vector fields, `@search.document` `DebugInfo.vector.subscore` shows the maximum score used to rank the parent document, but not per-element detail.
-- Use `innerHits` to gain insight into how individual elements contributed to the score.
 
+- Use `innerHits` to gain insight into how individual elements contributed to the score.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "複数ベクトルフィールドにおけるランキング処理に関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける複数ベクトルフィールドのランキング処理についての文書の軽微な更新を示しています。主な変更点は、新しいセクション「一つのフィールド内の複数ベクトルに基づくランキング」が追加され、文書の内容がより充実した点です。このセクションでは、複数のベクトルが単一のドキュメントに関連付けられた場合、Azure AI Searchがどのようにそれらのベクトルを評価し、最も関連性の高いベクトルを使ってスコア付けを行うかが説明されています。

また、ドキュメントのスコアに対する影響がどのように最適化され、関連性の低いベクトルによる希薄化が防がれるかについても言及されています。さらに、`debug=vector`スイッチに関する情報や、`innerHits`を使用して個別の要素がスコアに与える影響を理解する方法についての補足情報が含まれ、利用者がより深く実装の詳細を把握できるように配慮されています。

このような更新により、ユーザーは複数ベクトルフィールドのランキング処理の仕組みを理解し、効果的にシステムを活用するための知識を得られるようになります。


