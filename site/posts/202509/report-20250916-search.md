---
date: '2025-09-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c07289f...MicrosoftDocs:81cad18
summary: このコードの変更では、ドキュメント`articles/search/cognitive-search-aml-skill.md`に軽微な更新が行われました。主な内容は、文書の日付の更新と特定リンクの簡略化です。新機能や破壊的変更はなく、情報の新しさとリンク構造の簡潔化を目的としています。日付の更新により、最新情報としての信頼性が向上し、リンクの変更によってユーザーが直感的に目的のページへたどり着くことができるようになります。この小さな更新により、ドキュメントの精度とユーザビリティが向上することが期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c07289f...MicrosoftDocs:81cad18){target="_blank"}

# Highlights
このコードの変更では、`articles/search/cognitive-search-aml-skill.md` ドキュメントに関する軽微な更新が行われています。主な変更点は、文書の日付の更新と特定のリンクの簡略化です。

## 新機能
特に新機能の追加はありません。

## 破壊的変更
破壊的変更はありません。

## その他の更新
- 文書の日付が `08/04/2025` から `09/15/2025` に更新されました。
- `Azure AI Foundryプロジェクト` のリンクが簡略化されました。

# Insights
このドキュメントの変更は、主に情報の新しさやリンク構造の簡潔化を目的としています。日付の更新は、ドキュメントが最新の情報であることを示すものであり、読者に抵抗なく内容を信頼してもらうために重要です。

一方、リンクの変更については、もともと存在していた `pivots=fdp-project` というパラメータが削除され、よりシンプルな `tabs=ai-foundry` だけの構成になりました。これによって、ユーザーがアクセスする際に混乱を避け、より直感的に目的のページへたどり着くことができるようになります。この種のリンク修正は、ユーザーエクスペリエンスの向上につながり、特に大量の情報を持つ技術ドキュメントにおいて有効です。

全体として、この小さな更新によって、ドキュメントの精度とユーザビリティが向上しており、読者にとっては信頼性のある便利な情報源となることが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-aml-skill.md](#item-51366c) | minor update | 文書の日付とリンクの修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/cognitive-search-aml-skill.md{#item-51366c}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: reference
-ms.date: 08/04/2025
+ms.date: 09/15/2025
 ms.update-cycle: 180-days
 ---
 
@@ -42,7 +42,7 @@ We recommend using the [**Import and vectorize data wizard**](search-get-started
 
 ## Prerequisites
 
-* An [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects?tabs=ai-foundry&pivots=fdp-project) for an embedding model deployed from the catalog, or an [AML workspace](../machine-learning/concept-workspace.md) for a custom model that you create.
+* An [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects?tabs=ai-foundry) for an embedding model deployed from the catalog, or an [AML workspace](../machine-learning/concept-workspace.md) for a custom model that you create.
 * The model endpoint for an embedding model deployed from the catalog, or an [online endpoint (real-time)](../machine-learning/concept-endpoints-online.md) of your AML workspace for a custom model.
 
 ## @odata.type
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書の日付とリンクの修正"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-aml-skill.md` ドキュメントにおけるわずかな更新を表しています。具体的には、最初の2行では、文書の日付を `08/04/2025` から `09/15/2025` に変更しています。これにより、情報の新しさが反映されます。次に、`Azure AI Foundryプロジェクト` のリンクにおいて、`tabs=ai-foundry&pivots=fdp-project`という部分が削除され、代わりに `tabs=ai-foundry` のみが残されています。これにより、リンクがよりシンプルになり、関連情報へのアクセスが改善されることが期待されます。全体として、文書の正確さと可読性を向上させるための小さな変更となります。


