---
date: '2026-02-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:545d781...MicrosoftDocs:800bcb1
summary: この差分は、ドキュメント内のスキルセットに関する情報に軽微な更新を加え、「Azure Content Understanding skill」を新たに追加しました。このアップデートは、利用者がドキュメントをより理解しやすくすることを目的としています。特に破壊的変更はなく、新しく追加されたスキルは他の既存のスキルとともに表示されるようになっています。今回の更新により、ユーザーエクスペリエンスが向上し、Azureサービスを利用するユーザーにとっては有益なツールとなることを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:545d781...MicrosoftDocs:800bcb1){target="_blank"}

# ハイライト
この差分は、ドキュメント内に記載されたスキルセットに関する情報に軽微な更新を加え、具体的にはAzure Content Understandingスキルがコンテンツ理解スキルとして新たに追加されました。このアップデートは、ユーザーがドキュメントを活用する際の選択肢を明確にし、その正確性を改善することを目的としています。

## 新機能
- 「Azure Content Understanding skill」がスキルセットに追加されました。

## 破壊的変更
- 特にありません。

## その他の更新
- スキルセットの情報セクションにAzure Content Understandingスキルが他の既存スキルと共に表示されるようになりました。

# 洞察
今回の更新は、ドキュメントの内容を最新の情報で整備することにより、利用者がその内容を理解しやすくするためのものです。「Azure Content Understanding skill」は、Azureサービスによって提供されるスキルの一つで、コンテンツの自動的な理解や解析を支援します。この理解スキルは、ドキュメントの一貫性やデータ処理フローをより効率的にすることで、利用者が迅速に結果を得られるようにするものです。

このようなアップデートにより、ドキュメントが最新のテクノロジートレンドやツールに沿った情報を提供し続けることができ、ユーザーエクスペリエンスの向上に寄与しています。特に、Azureサービスを利用しているユーザーにとっては、これらのスキルの活用によって、より柔軟で強力なインサイトを引き出せる可能性が広がります。ドキュメントを最新の状態に保つことは、技術革新の速い分野では特に重要であり、利用者が適切な判断と行動を行えるようにサポートする役割を果たしています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [vector-search-integrated-vectorization.md](#item-48219d) | minor update | スキルセットの更新: Azure Content Understanding スキルの追加 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/vector-search-integrated-vectorization.md{#item-48219d}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ For integrated data chunking and vector conversions, you're taking a dependency
 
 + [A skillset](cognitive-search-working-with-skillsets.md) configured for:
 
-  + A chunking strategy: [Text Split skill](cognitive-search-skill-textsplit.md), [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md), [Continent Understanding skill](cognitive-search-skill-content-understanding.md), or one of the [document parsing modes](vector-search-how-to-chunk-documents.md#common-chunking-techniques). 
+  + A chunking strategy: [Text Split skill](cognitive-search-skill-textsplit.md), [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md), [Azure Content Understanding skill](cognitive-search-skill-content-understanding.md), or one of the [document parsing modes](vector-search-how-to-chunk-documents.md#common-chunking-techniques). 
   
   + An embedding skill, used to generate vector arrays, which can be any of the following:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スキルセットの更新: Azure Content Understanding スキルの追加"
}
```

### Explanation
この変更では、ドキュメント内のスキルセットに関する情報が更新されました。具体的には、「コンテンツ理解スキル」として「Azure Content Understanding skill」が新たに追加され、依存関係が増えています。この小さな更新は、ドキュメントの正確性を向上させ、ユーザーが利用できる選択肢を明確に示すことを目的としています。変更された内容は、スキルセットの情報セクションにあり、他の既存のスキルと共に表示されています。


