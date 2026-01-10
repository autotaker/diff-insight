---
date: '2026-01-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e64a5dd...MicrosoftDocs:3c88435
summary: この差分では、いくつかのファイルに対するマイナーアップデートが実施され、内容の明確化や機能の改善が行われました。主な変更点として、画像抽出の最大数が500から1000に増加し、インデックススキーマの記述が明確になり、Blobインデクサに関する制限情報が強化されました。特に破壊的な変更はありませんが、既存システムが新しい制限に適合するような確認が必要です。これらの更新により、ユーザーはより高度な操作を行うための情報を得られるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e64a5dd...MicrosoftDocs:3c88435){target="_blank"}

# Highlights
この差分では、いくつかのファイルに対しマイナーアップデートが行われ、内容の明確化や機能の改善が図られています。画像抽出の最大枚数増加や、インデックススキーマ記述の明瞭化、Blobインデクサ制限情報の明確化が主な変更点です。

## New features
- 画像処理の能力向上に伴い、処理可能な画像の最大抽出数が500から1000に増加しました。

## Breaking changes
- 特に破壊的な変更は報告されていませんが、既存のシステムが新しい制限に適合するようにレビューが必要です。

## Other updates
- インデックススキーマに関する記述が、より特化して明確化されました。
- Blobインデクサ制限の説明に強化が加えられ、ユーザーはより具体的な情報を入手可能です。

# Insights
この差分では、AzureのCognitive Searchに関連する複数のドキュメントがマイナーアップデートされています。最初に画像処理に関するドキュメントでは、抽出可能な最大画像数が500から1000に増えたことが主な改良点です。これにより、AIを活用した画像検索機能の活用範囲が広がり、より多くのデータセットに対応できるようになりました。また、これに伴うエラーメッセージの調整も行われ、開発者に対して直感的なフィードバックが得られることが期待されます。

次に、インデックススキーマの定義に関するドキュメントでは、スキーマ作成のプロセスがより特化して説明されました。特に「単一のインデックススキーマ」に焦点を当てた表現への変更は、読者に具体的なケーススタディとしての情報を提供し、実務的に有用です。

最後に、Blobインデクサの制限に関しては、CSVファイルを扱う際の実用的な制約条件が詳述され、特にバッファサイズの上限や適用されるモードの詳しい条件が明文化されています。これにより、データサイズが異なる状況での正確な実装が可能になり、ユーザーは最大限のパフォーマンスを引き出せるようになります。

これらの詳細な更新情報は、ユーザーがより高度な操作を行うための制度設計として非常に価値があり、理解を深めると共に潜在的な問題の予防にも役立ちます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-concept-image-scenarios.md](#item-606953) | minor update | 画像処理における最大画像抽出数の更新 | modified | 2 | 2 | 4 | 
| [search-how-to-define-index-projections.md](#item-a7e2c5) | minor update | インデックススキーマの説明の明確化 | modified | 1 | 1 | 2 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | Blobインデクサに関する制限の明確化 | modified | 5 | 3 | 8 | 


# Modified Contents
## articles/search/cognitive-search-concept-image-scenarios.md{#item-606953}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 11/21/2025
+ms.date: 01/08/2025
 ms.update-cycle: 180-days
 ms.custom:
   - devx-track-csharp
@@ -43,7 +43,7 @@ Image processing is indexer-driven, which means that the raw inputs must be in a
 + Image analysis supports JPEG, PNG, GIF, and BMP
 + OCR supports JPEG, PNG, BMP, and TIF
 
-Images are either standalone binary files or embedded in documents, such as PDF, RTF, or Microsoft application files. A maximum of 500 images, or an aggregate image size of 75 MB, can be extracted from a given document. If a document exceeds either limit, extraction stops at 500 images or when the aggregate size reaches 75 MB, and a warning is generated.
+Images are either standalone binary files or embedded in documents, such as PDF, RTF, or Microsoft application files. A maximum of 1,000 images can be extracted from a given document. If there are more than 1,000 images in a document, the first 1,000 are extracted and then a warning is generated.
 
 Azure Blob Storage is the most frequently used storage for image processing in Azure AI Search. There are three main tasks related to retrieving images from a blob container:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像処理における最大画像抽出数の更新"
}
```

### Explanation
この修正では、ファイル `cognitive-search-concept-image-scenarios.md` の内容が変更されました。具体的には、画像処理に関連する情報の一部が更新されています。具体的には、文書から抽出できる画像の最大数が500から1000に増加し、それに伴う警告メッセージの内容も調整されています。この変更により、Azure AI Search における画像処理の能力が向上し、より多くの画像を処理できるようになっています。加えて、著者情報として日付の修正が行われています。

## articles/search/search-how-to-define-index-projections.md{#item-a7e2c5}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ Most implementations are a single index organized around chunks with parent fiel
 
 An index projection is defined in a [skillset](cognitive-search-working-with-skillsets.md). It's responsible for coordinating the indexing process that sends chunks of content to a search index, along with the parent content associated with each chunk. It improves how native data chunking works by giving your more options for controlling how parent-child content is indexed.
 
-This article explains how to create the index schema and indexer projection patterns for one-to-many indexing.
+This article explains how to create a single index schema and indexer projection patterns for one-to-many indexing.
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックススキーマの説明の明確化"
}
```

### Explanation
この修正では、ファイル `search-how-to-define-index-projections.md` 内のテキストが一部更新されました。変更点は、インデックススキーマに関する記述の明確化です。具体的には、「インデックススキーマとインデクサ投影パターンを作成する方法」についての説明が、「単一のインデックススキーマ」の作成に特化したものに変更されました。この微調整により、記事の内容がより明確になり、読者が理解しやすくなっています。全体として、インデックス作成の雰囲気を変えることなく、表現が修正されています。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 01/08/2026
+ms.date: 01/09/2026
 ms.update-cycle: 180-days
 ms.custom:
   - references_regions
@@ -127,7 +127,7 @@ Maximum running times exist to provide balance and stability to the service as a
 | Minimum schedule | 5 minutes |5 minutes |5 minutes |5 minutes |5 minutes |5 minutes |5 minutes | 5 minutes |
 | Maximum running time <sup>5</sup>| 1-3 or 3-10 minutes |2 or 24 hours |2 or 24 hours |2 or 24 hours |2 or 24 hours |N/A  |2 or 24 hours |2 or 24 hours |
 | Blob indexer <sup>7</sup>: maximum blob size, MB |16 |16 |128 |256 |256 |N/A  |256 |256 |
-| Blob indexer: maximum characters of content extracted from a blob <sup>6</sup> |256,000 |512,000 |4&nbsp;million |8&nbsp;million |16&nbsp;million |N/A |4&nbsp;million |4&nbsp;million |
+| Blob indexer: maximum characters of content extracted from a blob <sup>6</sup> <sup>8</sup> |256,000 |512,000 |4&nbsp;million |8&nbsp;million |16&nbsp;million |N/A |4&nbsp;million |4&nbsp;million |
 
 <sup>1</sup> Free services have indexer maximum execution time of 3 minutes for blob sources and 1 minute for all other data sources. Indexer invocation is once every 180 seconds. For AI indexing that calls Foundry Tools, free services are limited to 20 free transactions per indexer per day, where a transaction is defined as a document that successfully passes through the enrichment pipeline. (Tip: You can reset an indexer to reset its count.)
 
@@ -141,7 +141,9 @@ Maximum running times exist to provide balance and stability to the service as a
 
 <sup>6</sup> The maximum number of characters is based on Unicode code units, specifically UTF-16.
 
-<sup>7</sup> If using `delimitedText` parsing mode for CSV files, the file limit is 10MB.
+<sup>7</sup> When using `delimitedText` parsing mode for CSV files, a buffer size limit of 10MB per file row applies.
+
+<sup>8</sup> When using `delimitedText` parsing mode for CSV files, the “maximum extracted content size” limit doesn't apply.
 
 > [!NOTE]
 > As stated in [Index limits](#index-limits), indexers also enforce the upper limit of 3,000 elements across all complex collections per document starting with the latest GA API version that supports complex types (`2019-05-06`) onwards. This means that if you created your indexer with a prior API version, you won't be subject to this limit. To preserve maximum compatibility, an indexer that was created with a prior API version and then updated with an API version `2019-05-06` or later, will still be **excluded** from the limits. Customers should be aware of the adverse impact of having very large complex collections (as stated previously) and we highly recommend creating any new indexers with the latest GA API version.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blobインデクサに関する制限の明確化"
}
```

### Explanation
この修正では、ファイル `search-limits-quotas-capacity.md` に一部変更が加えられ、Blobインデクサに関する制限が明確化されています。具体的には、最大サイズや抽出されるコンテンツの文字数制限に関するテキストが更新されました。例えば、CSVファイルの `delimitedText` パースモードに関する説明が強化され、バッファサイズ制限が1行あたり10MBであることが明記されています。また、最大抽出コンテンツサイズの制限がこのモードでは適用されないことも追加されています。これらの変更により、ユーザーはBlobインデクサの制限についてより明確な理解を得ることができます。加えて、記事の更新日が新しく設定されています。


