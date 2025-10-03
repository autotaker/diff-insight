---
date: '2025-10-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2b0d8aa...MicrosoftDocs:09a6487
summary: この変更では、`articles/search/search-normalizers.md`ファイルに新しいテスト機能が追加され、検索ノーマライザーのテスト方法が具体的に説明されました。文書は更新され、`asciifolding`ノーマライザーを用いた例も含まれています。これにより、開発者はノーマライザーの挙動をより理解しやすくなり、検索関連アプリケーションの開発やデバッグに役立つ情報が提供されます。全体として、ドキュメントの質が向上し、ユーザーエクスペリエンスが改善されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2b0d8aa...MicrosoftDocs:09a6487){target="_blank"}

# ハイライト
この変更では、`articles/search/search-normalizers.md`ファイルに対して、検索ノーマライザーに関する新しいテスト機能の追加が行われました。これにより、ノーマライザーをHTTP POSTリクエストを用いてテストする具体的な方法が提供されています。また、文書の日付が更新され、細かな修正も加えられています。

## 新機能
- ノーマライザーのテスト方法に関するセクションが追加されました。
- 実際のリクエストとレスポンス例が追加され、具体的な使用例が示されました。
- `asciifolding`ノーマライザーを使用した場合の具体例が含まれています。

## ブレイキングチェンジ
- なし。

## その他のアップデート
- 文書の日付が2025年9月28日から2025年10月1日に更新されました。

# インサイト
このコード変更は、検索ノーマライザーを利用する開発者にとって、非常に有用なものとなっています。特に、新しく追加されたテストセクションは、ノーマライザーが入力をどのように処理するかを開発者がより容易に理解できるように設計されています。HTTP POSTリクエストを利用したノーマライザーの挙動の確認方法は、検索関連のアプリケーションの開発やデバッグにおいて非常に役立つでしょう。

`asciifolding`ノーマライザーの具体的な例が含まれていることで、文字の正規化の詳細な動作を視覚化でき、エンジニアはそれを基に複雑な検索機能を構築する際の活用方法を学ぶことができます。全体として、この更新はノーマライザーのドキュメントがより包括的になり、ユーザーエクスペリエンスの向上を目的としているといえます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-normalizers.md](#item-4477d9) | minor update | 検索ノーマライザーに新しいテスト機能を追加 | modified | 35 | 1 | 36 | 


# Modified Contents
## articles/search/search-normalizers.md{#item-4477d9}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 09/28/2025
+ms.date: 10/01/2025
 ms.update-cycle: 365-days
 ---
 
@@ -90,6 +90,40 @@ Azure AI Search provides built-in normalizers for common use-cases along with th
 
 <sup>(1)</sup> Custom normalizers don't specify tokenizers since normalizers always produce a single token.
 
+## Test a normalizer
+
+You can use the [Test Analyzer (REST)](/rest/api/searchservice/indexes/analyze) to see how a normalizer processes an input.
+
+**Request**
+
+```http
+  POST https://[search service name].search.windows.net/indexes/[index name]/analyze?api-version=[api-version]
+    Content-Type: application/json
+    api-key: [admin key]
+
+  {
+     "normalizer":"asciifolding",
+     "text": "Vis-à-vis means Opposite"
+  }
+```
+
+**Response**
+
+```http
+HTTP/1.1 200 OK
+
+{
+  "tokens": [
+    {
+      "token": "Vis-a-vis means Opposite",
+      "startOffset": 0,
+      "endOffset": 24,
+      "position": 0
+    }
+  ]
+}
+```
+
 ## Normalizers reference
 
 ### Predefined normalizers
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索ノーマライザーに新しいテスト機能を追加"
}
```

### Explanation
この変更は、`articles/search/search-normalizers.md`ファイルに関連するもので、検索ノーマライザーのドキュメントに新しいテスト機能を追加する内容です。具体的には、ノーマライザーをテストする方法についてのセクションが新たに追加され、HTTP POSTリクエストを使ってノーマライザーがどのように入力を処理するかを示しています。この修正には、リクエストとレスポンスの例が含まれており、特に`asciifolding`ノーマライザーを使用した場合の入力と出力が具体的に記載されています。

また、文書の日付も2025年9月28日から2025年10月1日に更新されており、その他の細かな修正が行われています。この変更によって、ユーザーはノーマライザーのテストをより容易に行い、その挙動を理解することができるようになります。全体として、このアップデートは検索機能の強化に寄与するものです。


