---
date: '2025-02-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d46a0e8...MicrosoftDocs:ea9b000
summary: このコード差分では、フランス中央地域に関するサポート階層と無効化されたSKUの情報が更新されており、大きな技術的な変更はありません。一部の文書に微修正が行われ、特にフランス中央地域のサポート階層が「Basic,
  S1」から「All Tiers」へと変更されました。また、誤字修正も含まれております。この変更により、利用者はフランス中央地域で利用できるサービスの選択肢をより明確に理解できるようになり、Azure
  Searchサービスの利用促進が期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d46a0e8...MicrosoftDocs:ea9b000){target="_blank"}

# ハイライト
このコード差分では、三つの記事における文書の微修正と更新を行っています。主な新機能としては、フランス中央地域に関するサポート階層と無効化されたSKUの情報が更新されていますが、大きな技術的な変更や破壊的な変更はありません。

## 新機能
- フランス中央地域のサポート階層が「Basic, S1」から「All Tiers」へと変更されました。
- フランス中央地域の無効化されたSKUも「All tiers」と更新されました。

## 破壊的変更
- 特に破壊的な変更はありません。

## その他の更新
- `index-add-scoring-profiles.md`ファイル中の誤字修正（「human-readable ocntent」から「human-readable content」）。
 
# 洞察
この差分においては、スコアリングプロファイルに関する微修正と、フランス中央地域におけるサービスサポート情報とSKU情報の更新という二つの主要な変更が行われています。細かな文字の修正により、ドキュメントの正確性が向上し、読者にとっての理解もより容易になりました。

特にフランス中央地域の「All Tiers」に関する更新は、利用者がこの地域で利用できる全てのサービス階層について、より明確に理解できるようになったと言えます。従来の「Basic, S1」モデルから広範囲のサービス階層利用へのシフトは、Azureユーザーがサービスの利用計画を立てる際に、より多くの選択肢を考慮できるようにするためのものです。

これにより、フランス中央におけるAzure Searchサービスの利用が促進される可能性があり、技術者や企業はこの情報を基に戦略を練り直すことができます。特に、フランス中央以外の地域を活用する必要がある場合、スウェーデン中央やスイス北部の使用も考慮に入れることが推奨されています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | スコアリングプロファイルに関する文書の修正 | modified | 1 | 1 | 2 | 
| [search-region-support.md](#item-25b0f1) | minor update | フランス中央のサポート階層の更新 | modified | 1 | 1 | 2 | 
| [search-sku-tier.md](#item-7686b8) | minor update | フランス中央の無効化されたSKUの更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -99,7 +99,7 @@ Scoring profiles supplement the default scoring algorithm by boosting the scores
 
 For standalone text queries, scoring profiles identify the maximum 1,000 matches in a [BM25-ranked search](index-similarity-and-scoring.md), and the top 50 are returned in results.
 
-For pure vectors, the query is vector-only, but if the [*k*-matching documents](vector-search-ranking.md) include nonvector fields with human-readable ocntent, a scoring profile can be applied. The scoring profile revises the result set by boosting documents that match criteria in the profile.
+For pure vectors, the query is vector-only, but if the [*k*-matching documents](vector-search-ranking.md) include nonvector fields with human-readable content, a scoring profile can be applied. The scoring profile revises the result set by boosting documents that match criteria in the profile.
 
 For text queries in a hybrid query, scoring profiles identify the maximum 1,000 matches in a BM25-ranked search. However, once those 1,000 results are identified, they're restored to their original BM25 order so that they can be rescored alongside vectors results in the final [Reciprocal Ranking Function (RRF)](hybrid-search-ranking.md) ordering, where the scoring profile (identified as "final document boosting adjustment" in the illustration) is applied to the merged results, along with [vector weighting](vector-search-how-to-query.md#vector-weighting), and [semantic ranking](semantic-search-overview.md) as the last step.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリングプロファイルに関する文書の修正"
}
```

### Explanation
この変更は、`articles/search/index-add-scoring-profiles.md`ファイルにおいて、スコアリングプロファイルに関する文の微修正を行ったものです。具体的には、文の中で「human-readable ocntent」という誤字が、「human-readable content」と修正されています。その他の内容には変更はなく、スコアリングプロファイルがどのように機能するかについての説明はそのまま残されています。この修正により、文書の正確性が向上し、読者が情報を正確に理解できるようになっています。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -60,7 +60,7 @@ AI service integration refers to internal connections to an Azure AI multi-servi
 |--|--|--|--|--|
 | North Europe​​ | ✅ | ✅ | ✅ | All tiers|
 | West Europe​​ <sup>1</sup>| ✅ | ✅ | ✅ | All Tiers |
-| France Central​​ | ✅ | ✅ | ✅ | Basic, S1|
+| France Central​​ | ✅ | ✅ | ✅ | All Tiers|
 | Germany West Central​ <sup>1</sup>​| ✅ |  | ✅ | |
 | Italy North​​ |  |  | ✅ | |
 | Norway East​​ | ✅ |  | ✅ |  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フランス中央のサポート階層の更新"
}
```

### Explanation
この変更は、`articles/search/search-region-support.md`ファイルにおいて、フランス中央地域のサポート階層に関する情報を更新したものです。具体的には、以前は「Basic, S1」という表記が使用されていたのが、今回の修正により「All Tiers」と変更されました。この修正によって、フランス中央地域で利用可能なすべてのサービス階層が明確に示され、情報の正確性と利用者の理解が向上しています。その他の地域に関する情報には変更はありません。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -59,7 +59,7 @@ Currently, several regions are capacity-constrained for specific tiers and can't
 
 | Region | Disabled tier (SKU) due to over-capacity | Suggested alternative |
 |--------|------------------------------------------|-----------------------|
-| France Central | Basic, S1| Sweden Central, Switzerland North|
+| France Central | All tiers| Sweden Central, Switzerland North|
 | North Europe | All tiers | Sweden Central, Switzerland North|
 | West Europe | All tiers | Sweden Central, Switzerland North|
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フランス中央の無効化されたSKUの更新"
}
```

### Explanation
この変更は、`articles/search/search-sku-tier.md`ファイルにおいて、フランス中央地域のSKUに関する情報を更新したものです。具体的には、以前は「Basic, S1」とリストされていたフランス中央地域の無効化されたSKUが「All tiers」に変更されました。この修正により、フランス中央地域で利用できるすべてのサービス階層が制約となっていることが明確に示され、利用者が代替の地域（スウェーデン中央やスイス北部）を検討する際の参考となります。その他の地域に関する情報には変更はありません。


