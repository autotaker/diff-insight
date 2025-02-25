---
date: '2025-02-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8c6e364...MicrosoftDocs:50dc684
summary: このドキュメントでは、量子化に関する注意事項が新たに追加されました。主に、無料サービスにおける量子化の制約について触れています。この更新は新機能の追加ではなく、ドキュメントの明確性を向上させるためのマイナーな改訂です。特に、量子化によるストレージの制約についての情報が追加され、ユーザーがサービスを利用する際の理解を深められるようになっています。量子化はデータのストレージ効率を向上させるための技術であり、無料サービスで利用する際には期待外れの結果を避けるための知識が重要です。この情報は、特に大量データを扱う企業や組織にとって有用です。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8c6e364...MicrosoftDocs:50dc684){target="_blank"}

<format>
# Highlights
このドキュメントの変更では、新たに量子化に関する注意事項が追加されました。特に、無料サービスにおける量子化の制約に触れています。この更新は、新機能というよりもドキュメントの明確性を向上させるためのマイナーアップデートです。

## New features
特に新機能の追加はありません。

## Breaking changes
破壊的変更はありません。

## Other updates
量子化によるストレージの制約に関する情報が追加され、ドキュメントがより正確になりました。

# Insights
この変更は、量子化という技術的なトピックに関するドキュメントの明確性を向上させるために行われました。特に、無料サービスでは量子化がサポートされているが、ストレージの制限のために期待されるほどのストレージの節約が達成できない可能性があることを読者に伝えています。

量子化は、ベクトル検索のパフォーマンスを向上させるための手段であり、データのストレージを効率化する重要な技術です。しかし、無料サービスの制限を考慮せずに利用すると、期待外れの結果になることもあります。このドキュメントの追加は、ユーザーがこの点を理解し、十分な知識を持ってサービスを利用できるようにするためのものです。

このような注意事項の追加は、ユーザーが自分のニーズに最適なサービスを選定し、利用可能なリソースの限界を理解する上で非常に有用です。量子化の技術的背景だけでなく、実際の利用における現実的な制約についてもユーザーに意識してもらうことが可能になります。この情報は、特に生産環境で多くのデータを扱う企業や組織にとって、コストパフォーマンスを向上させるためのヒントとなるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [vector-search-how-to-quantization.md](#item-744f48) | minor update | 量子化に関する注意事項の追加 | modified | 3 | 0 | 3 | 


# Modified Contents
## articles/search/vector-search-how-to-quantization.md{#item-744f48}

<details>
<summary>Diff</summary>
````diff
@@ -42,6 +42,9 @@ Two types of quantization are supported:
 
 - Binary quantization converts floats into binary bits, which takes up 1 bit. This results in up to 28 times reduced vector index size.
 
+>[!Note]
+> While free services support quantization, they may not demonstrate the full storage savings due to the limited storage quota.
+
 ## Add "compressions" to a search index
 
 The following example shows a partial index definition with a fields collection that includes a vector field, and a `vectorSearch.compressions` section.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "量子化に関する注意事項の追加"
}
```

### Explanation
この変更では、ドキュメント「vector-search-how-to-quantization.md」に3行の新しい内容が追加されました。新たに追加された内容は、無料サービスが量子化をサポートしているものの、ストレージの制限により完全なストレージの節約が示されない可能性があることに関する注意事項に関するものです。この修正は、量子化の理解を深めるために重要であり、読者に対して利用可能なリソースの制限を意識させる手助けとなります。全体的に、この変更はドキュメントの内容をより正確で明確にしました。


