---
date: '2026-01-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8d79be2...MicrosoftDocs:e64a5dd
summary: このコード差分では、Azure Cognitive Searchに関連する文書に小さな更新が加えられました。主に、画像抽出の制限が500枚または75MBに変更され、CSVファイルのパースモード`delimitedText`には10MBのファイルサイズ制限が新たに導入されました。現時点では破壊的な変更は報告されていませんが、抽出制限の変更はユーザーに影響を与える可能性があります。また、日付の更新に関する注意喚起が追加されています。これらの変更は、サービスのパフォーマンス向上と負荷管理のための調整と考えられます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8d79be2...MicrosoftDocs:e64a5dd){target="_blank"}

# Highlights

このコード差分は2つの主要な文書に小さな更新を加えています。Azure Cognitive Searchに関連する画像抽出や検索制限、クォータに関する情報を最新版にアップデートしました。

## New features

- 画像抽出について、最大500枚もしくは75MBの制限が新たに追加されました。
- Azure Cognitive SearchにおけるCSVファイルのパースモード`delimitedText`に新たな10MBのファイルサイズ制限が導入されました。

## Breaking changes

- 現在までのところ、破壊的な変更は特に報告されていませんが、抽出制限の変更はユーザーに影響する可能性があります。

## Other updates

- 日付の更新や、blobインデクサへの新しい情報追加に伴う注意喚起が追加されました。

# Insights

Azure Cognitive Search関連のドキュメントにおける最新の更新について、その意義を深堀りしていきましょう。主に2つの文書に焦点が当てられています。

1. **画像抽出制限の更新**:
   画像抽出の制限が以前の1,000枚から500枚へと大幅に引き締められ、また、合計75MB以内という新たな制約が追加されました。これにより、サービスの利用状況に応じたより細かな管理が求められる可能性があります。処理が制限を超えると停止する仕様になっており、警告をトリガーすることでユーザー側の早期の対応が求められる点にも注目するべきです。これらの変更は、サービスの負荷管理をより効果的に行うためのものであり、サービスのパフォーマンス向上や安定性アップを目指した調整と見ることができます。

2. **検索制限とクォータの更新**:
   Azure Cognitive Searchにおける複雑なコレクションの上限が明記され、新しいAPIバージョンを活用した運用が推奨されています。特に、`delimitedText`モードを利用した場合のCSVファイルサイズの制限が10MBと設定されていることは、ユーザーがデータをより効率的に管理するための指針となるでしょう。また、APIのバージョンアップに伴う注意喚起の追加は、ユーザーにおける運用の見直しとAPIバージョンのチェックを促す効果があります。

これらの更新は、Azure Cognitive Searchを取り巻く環境の進化を感じさせるものであり、ユーザーはそのガイダンスに従ってサービス利用の最適化を考慮するべきです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-concept-image-scenarios.md](#item-606953) | minor update | 画像抽出制限の更新 | modified | 1 | 1 | 2 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索制限とクォータの更新 | modified | 4 | 2 | 6 | 


# Modified Contents
## articles/search/cognitive-search-concept-image-scenarios.md{#item-606953}

<details>
<summary>Diff</summary>
````diff
@@ -43,7 +43,7 @@ Image processing is indexer-driven, which means that the raw inputs must be in a
 + Image analysis supports JPEG, PNG, GIF, and BMP
 + OCR supports JPEG, PNG, BMP, and TIF
 
-Images are either standalone binary files or embedded in documents, such as PDF, RTF, or Microsoft application files. A maximum of 1,000 images can be extracted from a given document. If there are more than 1,000 images in a document, the first 1,000 are extracted and then a warning is generated.
+Images are either standalone binary files or embedded in documents, such as PDF, RTF, or Microsoft application files. A maximum of 500 images, or an aggregate image size of 75 MB, can be extracted from a given document. If a document exceeds either limit, extraction stops at 500 images or when the aggregate size reaches 75 MB, and a warning is generated.
 
 Azure Blob Storage is the most frequently used storage for image processing in Azure AI Search. There are three main tasks related to retrieving images from a blob container:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像抽出制限の更新"
}
```

### Explanation
この変更は、ドキュメントからの画像抽出に関する制限を更新しました。以前は1,000枚の画像が抽出可能でしたが、新しい仕様では最大500枚の画像または合計75MBのサイズに制限されるようになりました。この変更により、画像の抽出が制限を超えると処理が停止し、その際に警告が生成されることが明記されています。また、画像処理やOCRが支持するファイル形式に関する情報はそのまま維持されています。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 11/20/2025
+ms.date: 01/08/2026
 ms.update-cycle: 180-days
 ms.custom:
   - references_regions
@@ -126,7 +126,7 @@ Maximum running times exist to provide balance and stability to the service as a
 | Maximum indexing load per invocation |10,000 documents |Limited only by maximum documents |Limited only by maximum documents |Limited only by maximum documents |Limited only by maximum documents |N/A |No limit |No limit |
 | Minimum schedule | 5 minutes |5 minutes |5 minutes |5 minutes |5 minutes |5 minutes |5 minutes | 5 minutes |
 | Maximum running time <sup>5</sup>| 1-3 or 3-10 minutes |2 or 24 hours |2 or 24 hours |2 or 24 hours |2 or 24 hours |N/A  |2 or 24 hours |2 or 24 hours |
-| Blob indexer: maximum blob size, MB |16 |16 |128 |256 |256 |N/A  |256 |256 |
+| Blob indexer <sup>7</sup>: maximum blob size, MB |16 |16 |128 |256 |256 |N/A  |256 |256 |
 | Blob indexer: maximum characters of content extracted from a blob <sup>6</sup> |256,000 |512,000 |4&nbsp;million |8&nbsp;million |16&nbsp;million |N/A |4&nbsp;million |4&nbsp;million |
 
 <sup>1</sup> Free services have indexer maximum execution time of 3 minutes for blob sources and 1 minute for all other data sources. Indexer invocation is once every 180 seconds. For AI indexing that calls Foundry Tools, free services are limited to 20 free transactions per indexer per day, where a transaction is defined as a document that successfully passes through the enrichment pipeline. (Tip: You can reset an indexer to reset its count.)
@@ -141,6 +141,8 @@ Maximum running times exist to provide balance and stability to the service as a
 
 <sup>6</sup> The maximum number of characters is based on Unicode code units, specifically UTF-16.
 
+<sup>7</sup> If using `delimitedText` parsing mode for CSV files, the file limit is 10MB.
+
 > [!NOTE]
 > As stated in [Index limits](#index-limits), indexers also enforce the upper limit of 3,000 elements across all complex collections per document starting with the latest GA API version that supports complex types (`2019-05-06`) onwards. This means that if you created your indexer with a prior API version, you won't be subject to this limit. To preserve maximum compatibility, an indexer that was created with a prior API version and then updated with an API version `2019-05-06` or later, will still be **excluded** from the limits. Customers should be aware of the adverse impact of having very large complex collections (as stated previously) and we highly recommend creating any new indexers with the latest GA API version.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索制限とクォータの更新"
}
```

### Explanation
この変更は、Azure Cognitive Searchにおける検索制限とクォータに関する文書を更新しました。主な修正点は、日付の更新や、Blobインデクサに関する新しい情報の追加です。具体的には、CSVファイルに`delimitedText`パースモードを使用する場合のファイルサイズ制限が10MBであることが記載されています。また、最新のGA APIバージョン以降、文書内の複雑なコレクションごとの上限が3,000要素であることに関する注意喚起も追加されました。これにより、ユーザーはインデクサの作成や更新時に、最新のAPIバージョンを使用することを推奨する内容となっています。


