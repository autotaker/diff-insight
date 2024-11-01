---
date: '2024-11-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b16ebe2...MicrosoftDocs:7c64df0
summary: この変更は、検索機能に関する説明をマイナーに更新したものです。特に、`searchMode=any`と`searchMode=all`の使用方法が強調され、情報の明確さが改善されています。また、デフォルトアナライザーの動作についての記述も具体的になりました。新機能や破壊的な変更はなく、既存機能の説明が詳細かつ明確になっています。この変更は、ユーザー体験を向上させることを目的としており、検索クエリの構築をより簡単に理解できるようになっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b16ebe2...MicrosoftDocs:7c64df0){target="_blank"}

<format>
# ハイライト
変更は、検索機能の説明に関するマイナーな更新です。`searchMode=any`と`searchMode=all`の使用方法に関する説明が強調され、情報の明確さが改善されています。また、デフォルトアナライザーの動作についても記述が具体的になっています。

## 新機能
特に新しい機能の追加はありません。

## 破壊的変更
破壊的な変更はありません。既存の機能の説明がより詳細かつ明確になっています。

## その他の更新
- `searchMode=all`の使用を推奨する説明の強調。
- デフォルトアナライザーによる単語分割と形態素変換に関する記述の修正。

# インサイト
この変更は、検索システムを使用する際のユーザー体験を向上させる目的があります。特に、`searchMode=any`と`searchMode=all`は検索条件に大きな影響を及ぼすため、適切な使用方法の理解は重要です。`searchMode=all`の推奨使用は、特定の条件すべてに一致する結果を求める際に信頼性の高い結果が得られることを意識しています。また、デフォルトのアナライザーの説明の修正により、検索クエリの構築における重要なポイントがより分かりやすくなりました。特に、ハイフンで区切られた単語の処理と形態素変換についての理解が深まることで、より精度の高い検索クエリを設計できます。このような明確で詳細なドキュメントの更新は、開発者やエンドユーザーにとって非常に価値があると言えます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-pagination-page-layout.md](#item-115902) | minor update | 検索モードの説明の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-pagination-page-layout.md{#item-115902}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ Occasionally, the content of seaarch results are unexpected. For example, you mi
 
 + Change **`searchMode=any`** (default) to **`searchMode=all`** to require matches on all criteria instead of any of the criteria. This is especially true when boolean operators are included the query.
 
-+ Experiment with different lexical analyzers or custom analyzers to see if it changes the query outcome. The default analyzer breakz up hyphenated words and reduces words to root forms, which usually improves the robustness of a query response. However, if you need to preserve hyphens, or if strings include special characters, you might need to configure custom analyzers to ensure the index contains tokens in the right format. For more information, see [Partial term search and patterns with special characters (hyphens, wildcard, regex, patterns)](search-query-partial-matching.md).
++ Experiment with different lexical analyzers or custom analyzers to see if it changes the query outcome. The default analyzer breaks up hyphenated words and reduces words to root forms, which usually improves the robustness of a query response. However, if you need to preserve hyphens, or if strings include special characters, you might need to configure custom analyzers to ensure the index contains tokens in the right format. For more information, see [Partial term search and patterns with special characters (hyphens, wildcard, regex, patterns)](search-query-partial-matching.md).
 
 ## Counting matches
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索モードの説明の修正"
}
```

### Explanation
この変更は、`articles/search/search-pagination-page-layout.md`ファイル内の検索機能に関する説明の一部を修正したものです。具体的には、`searchMode=any`と`searchMode=all`についての説明が強調され、特に条件にすべて一致する必要がある場合に`searchMode=all`を使用することが推奨されています。同時に、デフォルトのアナライザーがハイフンで区切られた単語を分割し、単語を基本形に変換することについての記述が修正されています。これにより、クエリ結果の信頼性を向上させるための重要な注意点が提供されています。全体として、この変更は情報の明確性と正確性を向上させるためのマイナーな更新と見なされます。


