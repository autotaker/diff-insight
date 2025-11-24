---
date: '2025-11-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e5d5061...MicrosoftDocs:36ddb61
summary: この記事の更新は、Azure AI Searchにおけるスコアリングプロファイルの利用方法を詳細化し改善することを目的としています。新しいスコアリング関数の例が追加され、文書の新しさや距離に基づいてスコアを調整する方法が示されています。重要な破壊的変更はありませんが、手順の具体性とAPI呼び出しの明確さが増したため、既存のユーザーにはプロセスの変更が含まれる可能性があります。また、日付の変更や、スコアリングプロファイルの説明がより明確になるように言語が改善されています。この変更により、ユーザーはより関連性の高い検索結果を得るための具体的な方法を理解しやすくなります。全体として、技術的な理解を助け、Azure
  AI Searchの機能を最大限に活用できるようになることを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e5d5061...MicrosoftDocs:36ddb61){target="_blank"}

# Highlights
この記事の更新は、Azure AI Searchにおけるスコアリングプロファイルの利用方法の詳細化と改善を主な目的としています。

## New features
- 記事に新たなスコアリング関数の例が追加され、文書の新しさや距離に基づいてスコアを調整する方法を示しています。

## Breaking changes
- 特に重要な破壊的変更は含まれていませんが、手順の具体性が増し、API呼び出しの指示が明確化されたことは、既存のユーザーにとってプロセスの変更を意味する可能性があります。

## Other updates
- 日付が「2025年11月6日」から「2025年11月23日」に変更されました。
- 説明がよりクリアに改善され、スコアリングプロファイルの目的や効果についての理解が深まるように言語が洗練されました。

# Insights
この変更はAzure AI Searchのスコアリングプロファイルに関するドキュメントを全面的に更新し、ユーザーがより具体的かつ効果的に検索結果のスコアリングプロファイルを設定できるようにすることを意図しています。

スコアリングプロファイルとは、検索結果をユーザーが定義した基準で調整するためのカスタマイズ可能な方法です。この更新により、スコアリングプロファイルを使用して、より関連性の高い検索結果を得る方法が具体的に説明されています。特に新たなスコアリング関数の例は、ビジネス上のニーズに応じて検索結果の順序を個別に調整する方法を示しており、これによりユーザーは実装時の理解を深められます。

特に、これはユーザーがAPI呼び出しを用いてスコアリングプロファイルを適用する具体的な手順を詳しく示しているため、技術的な理解を助ける重要なアップデートとなります。この改善は、ユーザーがAzure AI Searchの完全な可能性を引き出す手助けをするものであり、検索機能のカスタマイズを通じてビジネスの価値を向上させる機会を提供します。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | スコアリングプロファイルの追加に関する記事の更新 | modified | 81 | 53 | 134 | 


# Modified Contents
## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -9,13 +9,13 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 11/06/2025
+ms.date: 11/23/2025
 ms.update-cycle: 365-days
 ---
 
 # Add scoring profiles to boost search scores
 
-Scoring profiles are used to boost or suppress the ranking of matching documents based on criteria. In this article, learn how to specify and assign a scoring profile that boosts a search score based on parameters that you provide. You can create scoring profiles based on:
+Scoring profiles are used to boost or suppress the ranking of matching documents based on user-defined criteria. In this article, learn how to specify and assign a scoring profile that boosts a search score based on parameters that you provide. You can create scoring profiles based on:
 
 + Weighted string fields, where boosting is based on a match found in a designated field. For example, matches found in a "Subject" field are considered more relevant than the same match found in a "Description" field.
 
@@ -33,11 +33,11 @@ You can add a scoring profile to an index by editing its JSON definition in the
 
 ## Rules for scoring profiles
 
-You can use scoring profiles in [keyword search](search-lucene-query-architecture.md), [vector search](vector-search-overview.md), [hybrid search](hybrid-search-overview.md), and [semantic reranking)](semantic-search-overview.md). However, scoring profiles only apply to nonvector fields, so make sure your index has text or numeric fields that can be boosted or weighted. 
+You can use scoring profiles in [keyword search](search-lucene-query-architecture.md), [vector search](vector-search-overview.md), [hybrid search](hybrid-search-overview.md), and with [semantic reranking)](semantic-search-overview.md). However, scoring profiles only apply to nonvector fields, so make sure your index has text or numeric fields that can be boosted or weighted. 
 
-You can have up to 100 scoring profiles within an index (see [service Limits](search-limits-quotas-capacity.md)), but you can only specify one profile at time in any given query.
+You can have up to 100 scoring profiles within an index (see [service Limits](search-limits-quotas-capacity.md)), but you can only specify one profile at a time in any given query.
 
-You can use [semantic ranker](semantic-how-to-query-request.md) with scoring profiles and apply a [scoring profile after semantic ranking](semantic-how-to-enable-scoring-profiles.md). Otherwise, when multiple ranking or relevance features are in play, semantic ranking is the last step. [How search scoring works](search-relevance-overview.md#diagram-of-ranking-algorithms) provides an illustration.
+You can use [semantic ranking](semantic-how-to-query-request.md) with scoring profiles and apply a [scoring profile after semantic ranking](semantic-how-to-enable-scoring-profiles.md) occurs. Otherwise, when multiple ranking or relevance features are in play, semantic ranking is the last step. [How search scoring works](search-relevance-overview.md#diagram-of-ranking-algorithms) provides an illustration of the order of operations.
 
 [Extra rules](#rules-for-using-functions) apply specifically to functions.
 
@@ -93,7 +93,7 @@ For more scenarios, see the examples for [freshness and distance](#example-boost
 
 ## Add a scoring profile to a search index
 
-1. Start with an [index definition](/rest/api/searchservice/indexes/create). You can add and update scoring profiles on an existing index without having to rebuild it. Use a [Create or Update Index](/rest/api/searchservice/indexes/create-or-update) request to post a revision.
+1. Start with an [index definition](/rest/api/searchservice/indexes/create). You can add and update scoring profiles on an existing index without having to rebuild it. Use [Get Index](/rest/api/searchservice/indexes/get) to pull down an existing index, and use [Create or Update Index](/rest/api/searchservice/indexes/create-or-update) request to post a revision.
 
 1. Paste in the [template](#template) provided in this article.  
 
@@ -124,7 +124,7 @@ Scoring profiles can be defined in the Azure portal as shown in the following sc
     "functions": (optional) [  
       {   
         "type": "magnitude | freshness | distance | tag",   
-        "boost": # (positive or negative number used as multiplier for raw score != 1),   
+        "boost": # (positive number used as multiplier for raw score != 1),   
         "fieldName": "(...)",   
         "interpolation": "constant | linear (default) | quadratic | logarithmic",   
 
@@ -162,7 +162,7 @@ Scoring profiles can be defined in the Azure portal as shown in the following sc
 
 ## Use text-weighted fields
 
-Use text-weighted fields when field context is important and queries include `searchable` string fields. For example, if a query includes the term "airport", you might want "airport" in the HotelName field rather than the Description field. 
+Use text-weighted fields when field context is important and queries include `searchable` string fields. For example, if a query includes the term "airport", you might favor "airport" in the HotelName field rather than the Description field. 
 
 Weighted fields are name-value pairs composed of a `searchable` field and a positive number that is used as a multiplier. If the original field score of HotelName is 3, the boosted score for that field becomes 6, contributing to a higher overall score for the parent document itself.
 
@@ -187,13 +187,11 @@ Use functions when simple relative weights are insufficient or don't apply, as i
 | Function | Description | Use cases |
 |-|-|
 | distance  | Boost by proximity or geographic location. This function can only be used with `Edm.GeographyPoint` fields. | Use for "find near me" scenarios. |
-| freshness | Boost by values in a datetime field (`Edm.DateTimeOffset`). [Set boostingDuration](#set-boostingduration-for-freshness-function) to specify a value representing a timespan over which boosting occurs. | Use when you want to boost by newer or older dates. Rank items like calendar events with future dates such that items closer to the present can be ranked higher than items further in the future. One end of the range is fixed to the current time. To boost a range of times in the past, use a positive boostingDuration. To boost a range of times in the future, use a negative boostingDuration. |
-| magnitude | Alter rankings based on the range of values for a numeric field. The value must be an integer or floating-point number. For star ratings of 1 through 4, this would be 1. For margins over 50%, this would be 50. This function can only be used with `Edm.Double` and `Edm.Int` fields. For the magnitude function, you can reverse the range, high to low, if you want the inverse pattern (for example, to boost lower-priced items more than higher-priced items). Given a range of prices from $100 to $1, you would set `boostingRangeStart` at 100 and `boostingRangeEnd` at 1 to boost the lower-priced items. | Use when you want to boost by profit margin, ratings, clickthrough counts, number of downloads, highest price, lowest price, or a count of downloads. When two items are relevant, the item with the higher rating is displayed first. |
+| freshness | Boost by values in a datetime field (`Edm.DateTimeOffset`). [Set boostingDuration](#set-boostingduration-for-freshness-function) to specify a value representing a timespan over which boosting occurs. | Use when you want to promote recent (newer) dates. You can also boost items like calendar events with future dates such that are closer to the present, as compared with items that are further into the future. One end of the range is fixed to the current time.  |
+| magnitude | Magnitude is the computed distance between the document’s value (such as a date or location) and the reference point (such as "now" or a target location). It’s the input to the scoring function and determines how much boost is applied. Alter rankings based on the range of values for a numeric field. The value must be an integer or floating-point number. For star ratings of 1 through 4, this would be 1. For margins over 50%, this would be 50. This function can only be used with `Edm.Double` and `Edm.Int` fields. For the magnitude function, you can reverse the range, high to low, if you want the inverse pattern (for example, to boost lower-priced items more than higher-priced items). Given a range of prices from $100 to $1, you would set `boostingRangeStart` at 100 and `boostingRangeEnd` at 1 to boost the lower-priced items. | Use when you want to boost by profit margin, ratings, clickthrough counts, number of downloads, highest price, lowest price, or a count of downloads. When two items are relevant, the item with the higher rating is displayed first. |
 | tag  | Boost by tags that are common to both search documents and query strings. Tags are provided in a `tagsParameter`. This function can only be used with search fields of type `Edm.String` and `Collection(Edm.String)`. | Use when you have tag fields. If a given tag within the list is itself a comma-delimited list, you can [use a text normalizer](search-normalizers.md) on the field to strip out the commas at query time (map the comma character to a space). This approach "flattens" the list so that all terms are a single, long string of comma-delimited terms. | 
 
-Magnitude is the computed distance between a field's value (such as a date or location) and a reference point (such as "now" or a target location). It's the input to the scoring function and determines how much boost is applied. 
-
-Freshness and distance scoring are special cases of magnitude-based scoring, where the magnitude is automatically computed from a datetime or geographic field. For intuitive boosting that promotes newer or closer values over older or farther values, use a negative boost value (see the [example](#example-boosting-by-freshness-or-distance) for more details).
+Freshness and distance scoring are special cases of magnitude-based scoring, where the magnitude is automatically computed from a datetime or geographic field.
 
 ### Rules for using functions
 
@@ -204,18 +202,14 @@ Freshness and distance scoring are special cases of magnitude-based scoring, whe
 
 ### Set interpolations
 
-Interpolations set the shape of the slope used for boosting freshness and distance. 
-
-When the boost value is positive, scoring is high to low, and the slope is always decreasing. With negative boosts, the slope is increasing (newer documents get higher scores). The interpolation values determine the curve of the upward or downward slope and how aggressively the boost score changes in response to date or distance changes. The following interpolations can be used:  
+Interpolations set the shape of the slope used for boosting freshness and distance. Because scoring is high to low, the slope is always decreasing, but the interpolation determines the curve of the downward slope and how aggressively the boost score changes as document dates get older. 
 
 | Interpolation | Description |  
 |-|-|  
-|`linear`|For items that are within the max and min range, boosting is applied in a constantly decreasing amount. A negative boost penalizes older documents proportionally. Good for gradual decay in relevance. Linear is the default interpolation for a scoring profile.|  
-|`constant`|For items that are within the start and ending range, a constant boost is applied to the rank results. For freshness and distance, applies the same negative boost to all documents within the range. Use this when you want a flat penalty regardless of age.|  
-|`quadratic`|Quadratic initially decreases at smaller pace and then as it approaches the end range, it decreases at a much higher interval. For negative boosting, it penalizes older documents increasingly more as they age. Use this when you want to strongly favor the most recent documents and sharply demote older ones. This interpolation option isn't allowed in the tag scoring function.|  
-|`logarithmic` |Logarithmic initially decreases at higher pace and then as it approaches the end range, it decreases at a much smaller interval. For negative boosting, it penalizes older documents more sharply at first, then tapers off. Ideal when you want strong preference for very recent content but less sensitivity as documents age. This interpolation option isn't allowed in the tag scoring function.|  
-
-<!--  ![Constant, linear, quadratic, log10 lines on graph](media/scoring-profiles/azuresearch_scorefunctioninterpolationgrapht.png "AzureSearch_ScoreFunctionInterpolationGrapht") -->
+|`linear`|For items that are within the max and min range, boosting is applied in a constantly decreasing amount. Recommended when you want a gradual decay in relevance. Linear is the default interpolation for a scoring profile.|  
+|`constant`|For items that are within the start and ending range, a constant boost is applied to the rank results. Use this when you want a flat penalty regardless of age.|  
+|`quadratic`|Quadratic initially decreases at smaller pace and then accelerates as it approaches the end range, it decreases at a much higher interval. Use this interpolation when you want to strongly favor the most recent documents and sharply demote older ones. This interpolation option isn't allowed in the tag scoring function.|  
+|`logarithmic` |Logarithmic initially decreases at higher pace and then as it approaches the end range, it decreases at a much smaller interval. Recommended when you have a strong preference for very recent content but less sensitivity as documents age. This interpolation option isn't allowed in the tag scoring function.|  
   
 :::image type="content" source="media/scoring-profiles/interpolation-graph.png" alt-text="Diagram of slope shapes for constant, linear, logarithmic, and quadratic interpolations over a 365 day range":::
 
@@ -239,45 +233,66 @@ For more examples, see [XML Schema: Datatypes (W3.org web site)](https://www.w3.
 
 ## Example: boosting by freshness or distance
 
-In Azure AI Search, freshness scoring converts date and values into a numeric magnitude—a single number representing how far a document's date is from the current time. The older the date, the larger the magnitude. This leads to a counter-intuitive behavior: more recent documents have smaller magnitudes, which means that positive boosting factors favor older documents unless you explicitly invert the boost direction.
-
-This same logic applies to distance boosting, where farther locations yield larger magnitudes.
-
-To boost by freshness or distance, use negative boosting values to prioritize newer dates or closer locations. Inverting the boost direction through a negative boosting factor penalizes larger magnitudes (older dates), effectively boosting more recent ones. For example, assume a boosting function like `b * (1 - x)` (where `x` is the normalized magnitude from 0 to 1) that gives higher scores to smaller magnitudes (that is, newer dates).
+When using the freshness function, if you want the boost to have a more dramatic effect on more recent dates, and taper off for older dates, choose a quadratic interpolation. Quadratic amplifies the effect of near recent dates. This same logic applies to distance boosting, where farther locations yield larger magnitudes.
 
-The shape of the boost curve (constant, linear, logarithmic, quadratic) affects how aggressively scores change across the range. With a negative factor, the curve’s behavior flips—for example, a quadratic curve tapers off more slowly for older dates, while a logarithmic curve shifts more sharply at the far end.
+The shape of the boost curve (constant, linear, logarithmic, quadratic) affects how aggressively scores change across the range. A quadratic curve tapers off more slowly for older dates, while a logarithmic curve shifts more sharply at the far end.
 
-Here's an example scoring profile that demonstrates how to address counter-intuitive freshness scoring using negative boosting and explains how magnitude works in this context.
+Here's an example scoring profile that demonstrates how to boost by freshness.
 
 ```json
-
-"scoringProfiles": [
-  {
-    "name": "freshnessBoost",
-    "text": {
-      "weights": {
-        "content": 1.0
-      }
-    },
-    "functions": [
+{
+    "name": "docs-index",
+    "fields": [
+      { "name": "id", "type": "Edm.String", "key": true, "filterable": true },
+      { "name": "title", "type": "Edm.String", "searchable": true },
+      { "name": "content", "type": "Edm.String", "searchable": true },
+      { "name": "lastUpdated", "type": "Edm.DateTimeOffset", "filterable": true, "sortable": true }
+    ],
+    "scoringProfiles": [
       {
-        "type": "freshness",
-        "fieldName": "lastUpdated",
-        "boost": -2.0,
-        "interpolation": "quadratic",
-        "parameters": {
-          "boostingDuration": "365D"
-        }
-      }
-    ]
-  }
-]
+        "name": "freshnessBoost",
+        "text": {
+          "weights": {
+            "content": 1.0
+          }
+        },
+        "functions": [
+          {
+            "type": "freshness",
+            "fieldName": "lastUpdated",
+            "boost": 2.0,
+            "interpolation": "quadratic",
+            "parameters": {
+              "boostingDuration": "365D"
+            }
+          }
+        ]
+    }
+  ]
+}
 ```
 
-+ `"fieldName": "lastUpdated"` is the datetime field used to calculate freshness.
-+ `"boost": -2.0` is a negative boosting factor, which inverts the default behavior. Since older dates have larger magnitudes, this penalizes them and boosts newer documents.
++ The `freshness` function computes a magnitude from "now" to `lastUpdated`.
++ A positive boost with quadratic interpolation increases lift for recent dates, tapering quickly for older ones. 
++ `"boostingDuration": "365D"` defines the time window over which freshness is evaluated, for example boosting documents dated within the last year.
 + `"interpolation": "quadratic"` means the boost effect is stronger for documents closer to the current date and tapers off more sharply for older ones.
-+ `"boostingDuration": "365D"` defines the time window over which freshness is evaluated.
+
+In the next example, a linear interpolation provides a steady preference for most‑recent content across the 30‑day window. Increase boost if the signal needs to win against other relevance factors.
+
+```json
+{
+  "name": "freshness30_linear",
+  "functions": [
+    {
+      "type": "freshness",
+      "fieldName": "lastUpdated",
+      "boost": 3.0,
+      "interpolation": "linear",
+      "parameters": { "boostingDuration": "P30D" }
+    }
+  ]
+}
+```
 
 ## Example: boosting by weighted text and functions
 
@@ -563,3 +578,16 @@ The top response for this query is "Gastronomic Landscape Hotel" with a search s
 }
 ```
 
+## Tuning tips
+
++ Start conservative: boost in the 1.25–2.0 range; increase only if recency is truly decisive.
+
++ Window sizing: Use P30D for hot content, P90D/P180D for moderate recency, P365D for long‑tail.
+
++ Interpolation choice:
+
+  + quadratic when you want a strong push to recent.
+  + linear when you want a steady gradient.
+  + logarithmic when you want a gentle preference.
+
++ Aggregation: If combining multiple functions, sum is easiest; switch to max when you want a single signal to dominate
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリングプロファイルの追加に関する記事の更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchにおけるスコアリングプロファイルの追加に関するドキュメントを更新することを目的としています。ドキュメントには、スコアリングプロファイルを利用して検索結果のスコアをどのように調整するかについての新しい情報が含まれています。

主な変更内容には、以下の点が含まれます：
- 日付の更新：記事の日付が「2025年11月6日」から「2025年11月23日」に変更されています。
- 説明の明確化：ユーザー定義の基準に基づいてドキュメントのランキングを促進または抑制するスコアリングプロファイルの利用について、言語が改善され、より明確になっています。
- 機能の変更：スコアリングプロファイルを追加するための手順が更新され、より具体的なAPI呼び出しの指示が提供されています。
- 新しいスコアリング関数の例の追加：新たに追加されたサンプルコードは、文書の新しさや距離に基づいてスコアを調整する方法を示しています。

この変更により、より良いユーザー体験を提供し、スコアリングプロファイルの実装方法についての理解を深めることを目的としています。


