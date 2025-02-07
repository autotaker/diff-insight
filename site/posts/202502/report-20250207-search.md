---
date: '2025-02-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ea9b000...MicrosoftDocs:22af4d0
summary: このコード差分は、Azure AI Searchに関するチュートリアル記事の軽微な更新を示しています。主に日付の修正と説明文の明確化が行われました。記事の日付は2024年12月5日から2025年2月5日に更新され、数か所の表現がより簡潔で理解しやすい形に修正されています。これらの改訂は、技術的な内容を非専門家でも理解できるようにすることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ea9b000...MicrosoftDocs:22af4d0){target="_blank"}

# ハイライト
このコード差分は、Azure AI Searchに関するチュートリアル記事の軽微な更新を示しています。主に日付の修正と説明文の明確化が行われています。

## 新機能
特になし。

## 破壊的変更
特になし。

## その他の更新
- 記事の日付が2024年12月5日から2025年2月5日に更新されました。
- 数か所の表現がより簡潔かつ理解しやすい形で修正されました。

# 洞察
この更新は、Azure AI Searchのチュートリアル記事の内容をより明確にするために行われたものです。日付の修正により、記事の新しさを反映し、読者に最新の情報を提供しようとしています。具体的な表現として、「ベクトルインデックスを圧縮」というフレーズが「ベクトル圧縮」となり、複雑な技術用語の簡素化と明確化を図っています。また、「検索結果のためのベクトルストレージをオプトアウトする」に関する表現も修正され、ユーザーがどの選択肢が適切なのかをより理解しやすくしています。

さらに、データ型に関する説明で「狭いデータ型」の使用を具体的に示し、`Collection(Edm.Half)`の使用についても言及しています。これにより、データ管理の最適化に関するユーザーの理解が助けられます。全体として、これらの改訂は、技術的な内容を非専門家にも理解しやすく伝えることを目的としています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [tutorial-rag-build-solution-minimize-storage.md](#item-088ad8) | minor update | 記事の更新: ストレージ最小化に関するチュートリアルの日付と説明の修正 | modified | 4 | 4 | 8 | 


# Modified Contents
## articles/search/tutorial-rag-build-solution-minimize-storage.md{#item-088ad8}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 12/05/2024
+ms.date: 02/05/2025
 
 ---
 
@@ -51,11 +51,11 @@ You should also have the following objects:
 
 Azure AI Search has multiple approaches for reducing vector size, which lowers the cost of vector workloads. In this step, create a new index that uses the following capabilities:
 
-- Smaller vector indexes by compressing the vectors used during query execution. Scalar quantization provides this capability.
+- Vector compression. Scalar quantization provides this capability.
 
-- Smaller vector indexes by opting out of vector storage for search results. If you only need vectors for queries and not in response payload, you can drop the vector copy used for search results.
+- Eliminate optional storage. If you only need vectors for queries and not in a response payload, you can drop the vector copy used for search results.
 
-- Smaller vector fields through narrow data types. You can specify `Collection(Edm.Half)` on the text_vector field to store incoming float32 dimensions as float16.
+- Narrow data types. You can specify `Collection(Edm.Half)` on the text_vector field to store incoming float32 dimensions as float16, which takes up less space in the index.
 
 All of these capabilities are specified in a search index. After you load the index, compare the difference between the original index and the new one.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事の更新: ストレージ最小化に関するチュートリアルの日付と説明の修正"
}
```

### Explanation
この変更では、Azure AI Searchに関するチュートリアル記事が更新され、いくつかの説明が改訂されました。具体的には、記事の日付が2024年12月5日から2025年2月5日に変更され、説明文の表現がより明確になるように修正されています。

- 「ベクトルインデックスを圧縮」との表現が「ベクトル圧縮」に改訂され、より簡潔で理解しやすくなりました。
- 「検索結果のためのベクトルストレージをオプトアウトする」との表現も「オプショナルストレージを排除する」に修正され、必要な場合とそうでない場合をより明確に示しています。
- また、「狭いデータ型」を明記し、`Collection(Edm.Half)`の使用に関する説明も簡潔化されました。

全体として、これらの変更は情報をより正確で明瞭に伝えることを目的としています。


