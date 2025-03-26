---
date: '2025-03-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7af2ef0...MicrosoftDocs:e737b2f
summary: このコードの差分には、二つの主なドキュメントの更新が含まれています。一つはREST APIのデータフィールド名の修正で、「source」から「urlSource」に変更されました。もう一つはクイックスタートガイドから不要なコンテンツを削除し、ドキュメントの簡潔さを高めたことです。特に新しい機能の追加はありませんが、APIの使用における明確さと一貫性が向上しました。これにより、ユーザーはより効率的にドキュメントインテリジェンスのREST
  APIを利用できるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7af2ef0...MicrosoftDocs:e737b2f){target="_blank"}

# ハイライト

このコードの差分は、二つの主なドキュメントの更新が含まれています。一つは REST API のデータフィールド名の修正で、もう一つはクイックスタートガイドからの不要なコンテンツの削除です。

## 新しい機能

特に新しい機能の追加はありませんが、API の使用における明確さと一貫性の向上が図られています。

## 互換性のない変更

互換性のない変更はありませんが、API のデータフィールド名が「source」から「urlSource」に変更されたため、既存のAPIの利用方法を見直す必要があります。

## その他の更新

クイックスタートガイドにおいては、無駄な情報が削除され、ドキュメントの簡潔さとユーザーの利便性が改善されました。

# インサイト

このアップデートにより、ユーザーはドキュメントインテリジェンスのREST APIをより効率的に利用できるようになります。具体的には、APIリクエストで使用するデータフィールドが「source」から「urlSource」に変更されたことで、API入力の役割がより明確になりました。元のフィールド名ではその意図するところが不明瞭になることがありますが、新しいフィールド名では「URLを指定する」ことが直感的に理解できるようになっています。

また、クイックスタートガイドからの不要なリンクやセクションタイトルの削除により、ユーザーは必要な情報を見つけやすくなりました。このような調整は、技術ドキュメントが直感的で簡潔であることを保証し、さまざまな背景を持つユーザーに対してフレンドリーなものにします。

ドキュメントの整備は技術コミュニケーションにおいて重要な要素であり、今回の変更はその良い例です。こうした小さな改善が積み重なり、サービス全体のユーザビリティが向上することでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [rest-api.md](#item-73da78) | minor update | REST APIの更新: データフィールドの変更（urlSourceへの変更） | modified | 2 | 2 | 4 | 
| [get-started-studio.md](#item-b2798e) | minor update | クイックスタートガイドの更新: 説明文の修正 | modified | 0 | 2 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/how-to-guides/includes/v2-1/rest-api.md{#item-73da78}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: include
-ms.date: 11/19/2024
+ms.date: 03/25/2025
 ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD001 -->
@@ -758,7 +758,7 @@ Before you run the command, make these changes:
 1. Replace *\<key>* with your key.
 
 ```console
-curl -v -i POST https://<endpoint>/formrecognizer/v2.1/prebuilt/invoice/analyze" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: <key>" --data-ascii "{​​​​​​​'source': '<your invoice URL>'}​​​​​​​​"
+curl -v -i POST https://<endpoint>/formrecognizer/v2.1/prebuilt/invoice/analyze" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: <key>" --data-ascii "{​​​​​​​'urlSource': '<your invoice URL>'}​​​​​​​​"
 ```
 
 You receive a `202 (Success)` response that includes an `Operation-Location` header. The value of this header contains a result ID that you can use to query the status of the asynchronous operation and get the results:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIの更新: データフィールドの変更（urlSourceへの変更）"
}
```

### Explanation
この変更では、ドキュメントの REST API ガイドにおいて、いくつかの小さな更新が行われました。具体的には、日付が更新され、APIリクエストのデータフィールド名が「source」から「urlSource」に変更されました。この変更により、ユーザーが請求書のURLを指定する方法が明確化され、API の利用における一貫性が向上します。更新内容は、マークダウン形式での差分として示されており、API リクエストを実行する際の正確な構文も提供されています。全体として、これらの修正はドキュメントの精度を高め、ユーザーが正しくAPIを利用できるようにするための重要なステップです。

## articles/ai-services/document-intelligence/quickstarts/get-started-studio.md{#item-b2798e}

<details>
<summary>Diff</summary>
````diff
@@ -17,8 +17,6 @@ monikerRange: '>=doc-intel-3.0.0'
 
 [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/) is an online tool for visually exploring, understanding, and integrating features from the Document Intelligence service in your applications. You can get started by exploring the pretrained models with sample or your own documents. You can also create projects to build custom template models and reference the models in your applications.
 
-> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE56n49]
-
 ## Prerequisites for new users
 
 To use Document Intelligence Studio, you need to acquire the following assets from the Azure portal:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートガイドの更新: 説明文の修正"
}
```

### Explanation
この変更では、ドキュメントインテリジェンスのクイックスタートガイドにおいて、2つの行が削除されました。一つは、Document Intelligence Studioに関するビデオリンクであり、もう一つは「新しいユーザー向けの前提条件」というセクションの見出しです。この調整は、ガイドの簡潔さと明瞭さを向上させることを目的としています。ユーザーが必要な情報に迅速にアクセスできるよう、内容を整理し、混乱を避けるための措置です。変更後の内容は、引き続きユーザーがDocument Intelligence Studioを使用するために必要な情報を提供します。


