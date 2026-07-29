---
date: '2026-07-29'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c781b82...MicrosoftDocs:3ae3b7b
summary: このコード変更は、Azure AI Searchに関連する2つのドキュメントの小規模な更新に焦点を当てており、ユーザー体験を向上させることを目的としています。「cognitive-search-defining-skillset.md」では日付とリソースキーが更新され、最新情報が提供されています。また、「index-add-scoring-profiles.md」では、スコアリングプロファイルの「boostingDuration」フィールドがISO
  8601形式に変更され、理解しやすくなりました。破壊的な変更はありませんが、リソースキーの名称変更に伴う設定の調整が必要です。これらの変更により、ユーザーは情報の鮮度やリソース管理の直感性が向上し、スコアリングルールの設定がより明確になります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c781b82...MicrosoftDocs:3ae3b7b){target="_blank"}

# Highlights
このコード変更は、Azure AI Searchに関連する2つのドキュメントの小規模な更新に焦点を当てています。変更は、情報の最新化やリソースキーの正確性向上、および用語の明確化により、ユーザー体験を向上させることを目的としています。

## New features
- 「cognitive-search-defining-skillset.md」では、日付とリソースキーの更新を行い、最新かつ正確な情報を提供することがされました。
- 「index-add-scoring-profiles.md」では、スコアリングプロファイルの「boostingDuration」フィールドのISO 8601形式への変更が行われ、より標準的で理解しやすくなりました。

## Breaking changes
- 特に破壊的な変更はありません。ただし、リソースキーの名称が変更されたため、それに基づいた設定やキーバリューがある場合、対応が必要です。

## Other updates
- いずれのドキュメントも情報の鮮度を維持するために、発行日が更新されています。

# Insights
これらの変更は、Azure AI Searchのユーザーにとって非常に価値のある更新です。まず、「cognitive-search-defining-skillset.md」での日付の更新により、ユーザーはこの文書が最新の情報を反映しているという安心感を持つことができます。リソースキーの変更は、特に複数のAzureサービスやリソースを管理しているユーザーにとって、リソースの管理がより直感的になり得る重要なポイントです。

「index-add-scoring-profiles.md」での更新は、スコアリングプロファイルの設定において、ISO 8601の採用により、業界標準に沿った形で理解しやすくなりました。「boostingDuration」が何を意味するのかが明示されたことにより、スコアリングルールの設定がより効果的になり、ユーザーは正確にその機能を把握して、Azure AI Searchを最大限に活用できるようになります。このように、技術ドキュメントは単なるガイドではなく、最良のプラクティスをユーザーに提供する強力なツールとして機能します。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-defining-skillset.md](#item-e2d71d) | minor update | マニュアルの更新: スキルセットの定義 | modified | 2 | 2 | 4 | 
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | スコアリングプロファイルの更新 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/search/cognitive-search-defining-skillset.md{#item-e2d71d}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Create a Skillset
 description: Learn about skillsets and create a skillset in Azure AI Search using REST APIs.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/07/2026
+ms.date: 07/27/2026
 ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
@@ -51,7 +51,7 @@ Start with the basic structure. In the [Create Skillset REST API](/rest/api/sear
    "cognitiveServices":{
       "@odata.type":"#Microsoft.Azure.Search.CognitiveServicesByKey",
       "description":"A Microsoft Foundry resource in the same region as Azure AI Search",
-      "key":"<Your-Azure-AI-Foundry-Resource-Key>"
+      "key":"<Your-Microsoft-Foundry-Resource-Key>"
    },
    "knowledgeStore":{
       "storageConnectionString":"<Your-Azure-Storage-Connection-String>",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マニュアルの更新: スキルセットの定義"
}
```

### Explanation
この変更は、Azure AI Searchに関連するドキュメントの更新であり、主に日付とリソースのキーに関する情報の修正が含まれています。具体的には、次の2点が変更されました:

1. ドキュメントの日付が「07/07/2026」から「07/27/2026」に更新されました。この変更は、文書が提供する情報の最新性を保つために重要です。
  
2. 「key」フィールドの値が「<Your-Azure-AI-Foundry-Resource-Key>」から「<Your-Microsoft-Foundry-Resource-Key>」に変更されました。この変更により、リソースを特定するための情報がより正確になり、利用者が適切な鍵を使用できるようになります。

このように、文書は最新の情報を反映するために修正され、ユーザーが正確なリソースを使用できるようになります。

## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.custom:
   - dev-focus
 ai-usage: ai-assisted
 ms.topic: how-to
-ms.date: 01/20/2026
+ms.date: 07/27/2026
 ms.update-cycle: 365-days
 ---
 
@@ -350,7 +350,7 @@ Here's an example scoring profile that demonstrates how to boost by freshness.
             "boost": 2.0,
             "interpolation": "quadratic",
             "parameters": {
-              "boostingDuration": "365D"
+              "boostingDuration": "P365D"
             }
           }
         ]
@@ -361,7 +361,7 @@ Here's an example scoring profile that demonstrates how to boost by freshness.
 
 + The `freshness` function computes a magnitude from "now" to `lastUpdated`.
 + A positive boost with quadratic interpolation increases lift for recent dates, tapering quickly for older ones. 
-+ `"boostingDuration": "365D"` defines the time window over which freshness is evaluated, for example boosting documents dated within the last year.
++ `"boostingDuration": "P365D"` defines the time window over which freshness is evaluated, for example boosting documents dated within the last year.
 + `"interpolation": "quadratic"` means the boost effect is stronger for documents closer to the current date and tapers off more sharply for older ones.
 
 In the next example, a linear interpolation provides a steady preference for most‑recent content across the 30‑day window. Increase boost if the signal needs to win against other relevance factors.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリングプロファイルの更新"
}
```

### Explanation
この変更は、「index-add-scoring-profiles.md」というドキュメントに対する更新で、主に日付の修正とスコアリングプロファイルに関連する用語の明確化が含まれています。具体的には、以下の2点が変更されました：

1. ドキュメントの日付が「01/20/2026」から「07/27/2026」に変更されました。この更新は、情報の鮮度を維持するために必要な対応です。

2. スコアリングプロファイルの「boostingDuration」フィールドの値が「365D」から「P365D」に変更されました。この変更は、ISO 8601形式に準拠した記述にするためのもので、より標準的で理解しやすい表現になっています。

さらに、説明文においても明確性が増しており、「boostingDuration」が評価される時間範囲を定義することの意味が強調されています。これにより、ユーザーはスコアリングプロファイルをより効果的に活用できるようになります。これらの修正により、文書はより正確で利用者にとって理解しやすいものとなっています。


