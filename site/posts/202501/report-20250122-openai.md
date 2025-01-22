---
date: '2025-01-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0a11550...MicrosoftDocs:a1ea100
summary: 今回の報告では、新しい機能や重大な変更はないものの、複数のマニュアルファイルに軽微な改善が行われたことが記載されています。主な内容は、「stored-completions.md」ファイルの更新日や地域情報の追加、オーディオモデルマトリックスのフォーマット調整、地域情報の整理などです。特に地域可用性に関する情報の更新が行われ、ユーザーは最新のサービス可用性を把握しやすくなります。これらの小規模な変更は、情報の明確化や正確な提供に寄与し、ユーザーエクスペリエンスの向上に繋がります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0a11550...MicrosoftDocs:a1ea100){target="_blank"}

# Highlights

新しい機能や重大な変更は特に含まれていないが、複数のマニュアルファイルに対する軽微な改善が行われた。主な変更点は以下のとおり：
1. 「stored-completions.md」ファイルでは更新日付が修正され、新しい地域情報が追加された。
2. 標準オーディオモデルマトリックスにおけるフォーマットの微調整。
3. 標準チャット完了モデルマトリックスの地域情報更新。
4. 標準モデルマトリックス内の地域情報の更新と整理。

## 新機能
新しい機能の追加は行われていない。

## 重大な変更
重大な変更は含まれていない。

## その他の更新
- 「stored-completions.md」では、最終更新日と利用可能な地域リストが最新化された。
- 標準オーディオモデルマトリックス内のフォーマットを改善し、情報の整合性を向上。
- 標準チャットおよび標準モデルマトリックス内の地域情報を更新し、最新のサービス可用性を反映。

# Insights

今回の変更内容は、主にドキュメントの整理と最新情報への更新に焦点を当てている。特に「stored-completions.md」ファイルの地域可用性について、新たに「North Central US」と「East US2」が追加されることで、ユーザーはより広範囲の利用可能な地域情報を把握できるようになった。このように可用性リストを更新することは、常にユーザーに最適なサービス利用環境を提供するために重要である。

さらに、標準モデルやチャット、オーディオに関する各ファイルにおいて、フォーマットの調整やチェックマークの見直しが行われている。これらの調整によって、情報がより明確に整理され、混乱を避けながら正確な情報を提供することができる。

これらの小規模な更新であっても、使用者にとっての利便性向上や正確な情報提供に寄与するため、定期的なメンテナンスは重要な役割を果たす。最終的に、これによりユーザーエクスペリエンスが向上し、ドキュメントがより信頼性の高いものとなる。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [stored-completions.md](#item-ccc7e6) | minor update | ストレージ完了に関する日付と地域の更新 | modified | 3 | 1 | 4 | 
| [standard-audio.md](#item-1d8db7) | minor update | 標準オーディオモデルマトリックスの修正 | modified | 1 | 1 | 2 | 
| [standard-chat-completions.md](#item-aae3f1) | minor update | 標準チャット完了モデルマトリックスの調整 | modified | 4 | 4 | 8 | 
| [standard-models.md](#item-af04c4) | minor update | 標準モデルマトリックスの調整 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/ai-services/openai/how-to/stored-completions.md{#item-ccc7e6}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
 ms.custom: references_regions
-ms.date: 12/12/2024
+ms.date: 01/21/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -29,6 +29,8 @@ Stored completions allow you to capture the conversation history from chat compl
 ### Regional availability
 
 - Sweden Central
+- North Central US
+- East US2
 
 ## Configure stored completions
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ストレージ完了に関する日付と地域の更新"
}
```

### Explanation
このコードの変更は、「stored-completions.md」ファイルに対する小規模な更新を示しています。具体的には、最終更新日が「2024年12月12日」から「2025年1月21日」に変更され、地域の可用性リストに「North Central US」と「East US2」が追加されています。この変更により、ユーザーは更新された日付を確認でき、利用可能な地域に関する情報も最新のものとなります。全体として、合計4箇所の変更があり、そのうちの3箇所が追加され、1箇所が削除されています。

## articles/ai-services/openai/includes/model-matrix/standard-audio.md{#item-1d8db7}

<details>
<summary>Diff</summary>
````diff
@@ -18,4 +18,4 @@ ms.date: 10/25/2024
 | swedencentral    | ✅             | ✅                | ✅                 |
 | switzerlandnorth | -            | -               | ✅                 |
 | uaenorth         | -            | -               | ✅                 |
-| westeurope       | -            | -               | ✅                 |
\ No newline at end of file
+| westeurope       | -            | -               | ✅                 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準オーディオモデルマトリックスの修正"
}
```

### Explanation
このコードの変更は、「standard-audio.md」ファイルに対する小さな修正を示しています。具体的には、テーブル内の「westeurope」行について、フォーマットが調整され、行の最後に改行が追加されました。この変更によって、情報の整合性が向上し、テーブルが適切に表示されるようになっています。全体として、合計2箇所の変更があり、1箇所が追加され、1箇所が削除されています。これにより、文書がより正確で読みやすくなります。

## articles/ai-services/openai/includes/model-matrix/standard-chat-completions.md{#item-aae3f1}

<details>
<summary>Diff</summary>
````diff
@@ -13,11 +13,11 @@ ms.date: 10/25/2024
 |:-----------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-----------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:------------------------------:|
 | australiaeast    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           |
 | canadaeast       | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           |
-| eastus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           |
-| eastus2          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           |
+| eastus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           |
+| eastus2          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           |
 | francecentral    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | ✅                       | ✅                       | ✅                       | -                      | ✅                           |
 | japaneast        | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | ✅                          | -                           | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           |
-| northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           |
+| northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           |
 | norwayeast       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          |
 | southcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | -                      | -                      | ✅                       | -                          |
 | southindia       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | ✅                       | ✅                       | -                          |
@@ -26,4 +26,4 @@ ms.date: 10/25/2024
 | uksouth          | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | ✅                        | -                         | -                           | -                   | ✅                       | ✅                       | ✅                       | ✅                       | ✅                           |
 | westeurope       | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          |
 | westus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | ✅                          | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          |
-| westus3          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          |
\ No newline at end of file
+| westus3          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準チャット完了モデルマトリックスの調整"
}
```

### Explanation
このコードの変更は、「standard-chat-completions.md」ファイルに対する小規模な更新を示しています。この更新では、複数の地域に関する情報がテーブルの形式で修正されました。具体的には、特定の地域に対するチェックマークの付け直しや追加が行われ、全体で4つの追加と4つの削除がありました。その結果、合計で8箇所の変更が発生しました。この更新により、標準チャット完了に関する地域別の可用性情報がより正確かつ明確に表示されるようになっています。これにより、ユーザーは最新の情報を容易に把握できるようになります。

## articles/ai-services/openai/includes/model-matrix/standard-models.md{#item-af04c4}

<details>
<summary>Diff</summary>
````diff
@@ -14,11 +14,11 @@ ms.date: 12/16/2024
 | australiaeast    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | ✅                  | -                  | -                  | -            | -               | -                |
 | brazilsouth      | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
 | canadaeast       | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| eastus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | ✅                  | -                  | -                  | -            | -               | -                |
-| eastus2          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| eastus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | ✅                  | -                  | -                  | -            | -               | -                |
+| eastus2          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | francecentral    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
 | japaneast        | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | ✅                          | -                           | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
+| northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
 | norwayeast       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | polandcentral    | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
 | southafricanorth | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準モデルマトリックスの調整"
}
```

### Explanation
このコードの変更は、「standard-models.md」ファイルにおける軽微な更新を示しています。この更新では、モデルの特性に関するテーブルの内容が一部修正され、具体的には「eastus」、「eastus2」、「northcentralus」地域の可用性に関する情報が更新されました。特に、これらの地域に対するチェックマークの付け直しが行われ、全体で3つの追加と3つの削除があり、合計で6箇所の変更が発生しています。この改訂により、各地域における標準モデルの特徴がより正確に反映され、情報が明確に提示されるようになりました。これにより、ユーザーは最新のサービスの可用性を容易に把握できるようになります。


