---
date: '2025-03-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4f20510...MicrosoftDocs:86d029a
summary: このコードの差分では、新しいPNG画像ファイルの追加とMarkdown文書の小規模な更新が行われています。特に、JSON出力タブに関するスクリーンショット画像が追加され、ユーザーに文書インテリジェンスサービスの詳細な情報を提供しています。また、技術的な詳細の追加により、ユーザー体験の向上が図られています。特に破壊的な変更はなく、レイアウトモデルの利用方法に関する情報が更新されています。この変更は、ユーザーがサービスをより理解しやすくするために有意義です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4f20510...MicrosoftDocs:86d029a){target="_blank"}

# ハイライト

このコードの差分では、新しいPNG画像ファイルの追加とMarkdown文書のマイナーアップデートが行われています。新機能として、JSON出力タブのスクリーンショット画像が追加されており、ユーザーに対して文書インテリジェンスサービスに関するより詳細な情報を提供しています。技術的な詳細の追加により、ユーザー体験の向上が図られています。

## 新機能
- `json-output-tab.png`という新しい画像ファイルが追加されました。この画像ファイルは、文書インテリジェンスサービスにおけるJSON出力タブのビジュアル情報を提供します。

## 破壊的変更
- 特に破壊的な変更は含まれていません。

## その他の更新
- `layout.md`ファイルにおいて、ドキュメントインテリジェンスのレイアウトモデルの利用方法に関する情報が更新されました。具体的には、6行の追加と1行の削除が行われています。

# 洞察

この変更の背後にはユーザーエクスペリエンスの向上を目指した意図が見られ、特に技術的なガイダンスを提供するために新しい視覚的サポートが追加されています。JSON出力タブのスクリーンショットという新しい視覚資料は、ユーザーが文書インテリジェンスサービスの機能を理解しやすくすることに貢献しています。これにより、ユーザーはStudioでの解析結果をより直接的に把握することができ、サービスの活用方法を理解する手助けになります。

さらに、レイアウトモデルを使用した文書分析の新しい情報を追加することにより、文書内の構造要素についてユーザーに理解を深めてもらうことを意図しています。このような情報は、ビジネス用途において、文書の自動解析を行う際の理解をサポートし、利用の実用性を高めるものです。ユーザー中心の情報拡充として、変更は非常に有意義であると考えられます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [json-output-tab.png](#item-2f2e2d) | new feature | 新しい画像ファイルの追加 | added | 0 | 0 | 0 | 
| [layout.md](#item-f7c4c8) | minor update | レイアウト文書の分析に関する更新 | modified | 6 | 1 | 7 | 


# Modified Contents
## articles/ai-services/document-intelligence/media/studio/json-output-tab.png{#item-2f2e2d}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像ファイルの追加"
}
```

### Explanation
このコードの差分は、`articles/ai-services/document-intelligence/media/studio/json-output-tab.png`というファイルが新たに追加されたことを示しています。この変更は、文書インテリジェンスサービスに関連するコンテンツを強化するものであり、ユーザーがJSON出力タブに関して視覚的な情報を得る手助けとなる画像ファイルを提供しています。変更内容は、ファイルの追加のみで、削除や修正は行われていません。この新しいファイルは、GitHubリポジトリ上でアクセス可能です。

## articles/ai-services/document-intelligence/prebuilt/layout.md{#item-f7c4c8}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 03/17/2025
+ms.date: 03/27/2025
 ms.author: lajanuar
 ---
 
@@ -120,6 +120,11 @@ The layout model extracts structural elements from your documents. To follow are
 * [**Figures**](#figures)
 * [**Sections**](#sections)
 
+Run the sample layout document analysis within [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio), then navigate to the results tab to access the full JSON output.
+
+   :::image type="content" source="../media/studio/json-output-tab.png" alt-text="Screenshot of results JSON output tab in the Document Intelligence Studio.":::
+
+
 ### Pages
 
 The pages collection is a list of pages within the document. Each page is represented sequentially within the document and includes the orientation angle indicating if the page is rotated and the width and height (dimensions in pixels). The page units in the model output are computed as shown:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レイアウト文書の分析に関する更新"
}
```

### Explanation
このコードの差分は、`articles/ai-services/document-intelligence/prebuilt/layout.md`ファイルの内容が変更されたことを示しています。具体的には、6行が追加され、1行が削除されています。この変更により、ドキュメントインテリジェンスのレイアウトモデルを使用した際の新しい情報が提供されています。

主な更新内容として、サンプルレイアウト文書分析をDocument Intelligence Studioで実行する方法が追加され、結果タブでJSON出力にアクセスする手順が説明されています。また、JSON出力タブのスクリーンショットを示す画像も追加されています。このような情報は、ユーザーが文書の構造要素を理解する手助けをするために有用です。全体として、この更新はユーザーに対する情報を豊かにし、実用性を向上させることを目的としています。


