---
date: '2025-03-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:17e9a85...MicrosoftDocs:34ecec7
summary: この更新は、`articles/search/search-sku-tier.md`ファイルに関する小規模な修正で、無効なSKUティアの情報が特定地域において更新されています。新機能は追加されていないものの、情報の正確性が向上しており、重大な互換性を壊す変更はありません。具体的には、フランス中央の無効なSKUティアに関する情報が削除され、代わりにスウェーデン中央と西ヨーロッパ地域が推薦されています。この修正により、文書の一貫性と信頼性が高まり、ユーザーはより関連性のある情報にアクセスできるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:17e9a85...MicrosoftDocs:34ecec7){target="_blank"}

# ハイライト
この更新は、`articles/search/search-sku-tier.md`ファイルに関する小規模な修正で、特定の地域における無効なSKUティアのリストに関する情報が更新されています。

## 新機能
特定の新機能は追加されていませんが、情報の正確性が向上しています。

## 互換性を壊す変更
特に重大な互換性を壊す変更はありません。

## その他の更新
- フランス中央に関連する無効なSKUティアの情報が削除されました。

# 洞察
この変更は主に情報の正確性を確保するためのものです。不必要な情報が削除されることで、ユーザはより正確で関連性のある情報にアクセスできるようになります。具体的には、フランス中央地域のS2、S3、L1、L2ティアが過負荷であるといった誤った情報が削除され、現在はスウェーデン中央と西ヨーロッパ地域を代替として推薦しています。これにより、システムの運用における意思決定がしやすくなり、地域におけるリソースの有効活用が期待されます。この修正は文書の一貫性と信頼性を高め、読者が最適なアクションを選択するための助けとなります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-sku-tier.md](#item-7686b8) | minor update | 検索SKUティアに関する情報の更新 | modified | 0 | 1 | 1 | 


# Modified Contents
## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -59,7 +59,6 @@ Currently, several regions are capacity-constrained for specific tiers and can't
 
 | Region | Disabled tier (SKU) due to over-capacity | Suggested alternative |
 |--------|------------------------------------------|-----------------------|
-| France Central | S2, S3, L1, L2| Sweden Central, West Europe|
 | North Europe | S2, S3, L1, L2 | Sweden Central, West Europe|
 
 ## Feature availability by tier
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索SKUティアに関する情報の更新"
}
```

### Explanation
この修正は、`articles/search/search-sku-tier.md`ファイルにおける小さな更新を示しています。具体的には、特定の地域における無効なSKUティアのリストから「フランス中央」の情報が削除されました。この変更により、フランス中央のS2、S3、L1、L2ティアが過負荷のため無効であることが示唆されていた点が消去され、代替提案としてスウェーデン中央と西ヨーロッパの地域が残されています。この修正により、読者に対する情報の正確性が高められています。


