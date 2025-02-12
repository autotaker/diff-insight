---
date: '2025-02-12'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f57bd77...MicrosoftDocs:be5df78
summary: この更新では、検索地域とSKUティアに関する情報の修正が行われ、西ヨーロッパ地域の情報が改善されました。具体的には、「容量制約」の更新や「代替SKUティア」の推奨地域の追加が含まれています。特別な新機能は追加されておらず、既存の情報がより正確になっています。破壊的な変更もなく、主に情報の正確性とユーザビリティの向上を目指しています。これにより、ユーザーはより信頼性の高い情報に基づいて意思決定ができるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f57bd77...MicrosoftDocs:be5df78){target="_blank"}

<format>
# ハイライト
この更新では、検索地域とSKUティアに関する情報の修正が行われ、西ヨーロッパ地域の情報が改善されています。これには「容量制約」の更新や「代替SKUティア」の推奨地域の追加が含まれています。

## 新機能
特に新しい機能が追加されたわけではありません。既存の情報がより正確なものに修正されています。

## 破壊的変更
プロセスや機能を著しく変更するような破壊的な変更は含まれていません。

## その他の更新
- 西ヨーロッパの「容量制約」に関する文書が修正されました。
- フランス中央と北ヨーロッパにおける無効なSKU tierの代替として、西ヨーロッパ地域の追加。

# 洞察
このドキュメント修正は主に、情報の正確性とユーザビリティを高めるためのもので、特に西ヨーロッパ地域に関連する部分に焦点を当てています。まず、search-region-support.mdでは、西ヨーロッパ地域の「容量制約」項目が「すべてのティア」から空白に修正されました。これにより、ユーザーはこの地域のリソース使用可能性についての誤解を減らし、より正確で信頼性のある情報に基づいて意思決定を行うことが可能になります。

さらに、search-sku-tier.mdでは、オーバーキャパシティが問題となる地域において、新たに「西ヨーロッパ」が代替の推奨地域として追加されました。これにより、ユーザーはより広範な選択肢を手にでき、ビジネスニーズに応じた柔軟な対応が可能になります。このような修正は、ユーザーガイドが実際のシステム状況に反映され、実用的かつ効率的な利用を促進する役割を果たしています。

これらの軽微な更新によって、ドキュメントの正確性が高まり、ユーザーエクスペリエンスの向上に貢献しています。したがって、情報の整合性維持に対する一貫した努力の結果といえるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-region-support.md](#item-25b0f1) | minor update | 西ヨーロッパ地域の情報修正 | modified | 1 | 1 | 2 | 
| [search-sku-tier.md](#item-7686b8) | minor update | 地域におけるSKU tierの推奨代替品の修正 | modified | 2 | 3 | 5 | 


# Modified Contents
## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -59,7 +59,7 @@ AI service integration refers to internal connections to an Azure AI multi-servi
 | Region | AI service integration | Semantic ranker | Availability zones | Capacity constrained |
 |--|--|--|--|--|
 | North Europe​​ | ✅ | ✅ | ✅ | All tiers|
-| West Europe​​ <sup>1</sup>| ✅ | ✅ | ✅ | All Tiers |
+| West Europe​​ | ✅ | ✅ | ✅ |  |
 | France Central​​ | ✅ | ✅ | ✅ | All Tiers|
 | Germany West Central​ <sup>1</sup>​| ✅ |  | ✅ | |
 | Italy North​​ |  |  | ✅ | |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "西ヨーロッパ地域の情報修正"
}
```

### Explanation
この修正は「search-region-support.md」ファイルの内容を更新するもので、特に西ヨーロッパ地域に関する情報を変更しています。具体的には、西ヨーロッパ地域の「容量制約」列が「すべてのティア」から空白に変更されており、これによりこの地域の利用可能性に関する表現が調整されています。この変更は、AIサービス統合やセマンティックレンクといった他の属性には影響を与えず、より正確な情報を提供するためのものであると考えられます。全体として、このコミットは文書の精度を向上させるための軽微な更新です。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -59,9 +59,8 @@ Currently, several regions are capacity-constrained for specific tiers and can't
 
 | Region | Disabled tier (SKU) due to over-capacity | Suggested alternative |
 |--------|------------------------------------------|-----------------------|
-| France Central | All tiers| Sweden Central, Switzerland North|
-| North Europe | All tiers | Sweden Central, Switzerland North|
-| West Europe | All tiers | Sweden Central, Switzerland North|
+| France Central | All tiers| Sweden Central, West Europe|
+| North Europe | All tiers | Sweden Central, West Europe|
 
 ## Feature availability by tier
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域におけるSKU tierの推奨代替品の修正"
}
```

### Explanation
この修正は「search-sku-tier.md」ファイルに対するもので、特定の地域におけるSKU tierに関する情報を更新しています。具体的には、フランス中央および北ヨーロッパの地域での「オーバーキャパシティ」による無効なSKU tierの代替として、スウェーデン中央に加えて「西ヨーロッパ」が新たに推奨されるようになりました。この変更により、より広範な選択肢が提供され、ユーザーが必要な際に利用可能な代替地域をより正確に把握できるようになります。全体として、この更新は文書の情報を最新に保ち、ユーザーに対する支援を強化するための軽微な修正です。


