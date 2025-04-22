---
date: '2025-04-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0fdb6d4...MicrosoftDocs:bb349ba
summary: 今回の変更では、OpenAIに関する文書が2つ更新されました。`audio.md`では「GPT-4o audio Realtime API」に関する見出しのレベルが変更され、`global-batch.md`ではグローバルバッチモデルマトリックスが更新されました。この更新により、ユーザーはより明確かつ正確な情報にアクセスできるようになります。新機能の追加や互換性に影響する変更はありませんが、文書の可読性と情報の正確性が向上することが期待されます。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0fdb6d4...MicrosoftDocs:bb349ba){target="_blank"}

# ハイライト
今回の変更では、OpenAIに関する2つの異なる文書の更新が行われています。一つは、`audio.md`での「GPT-4o audio Realtime API」に関する見出しのレベル変更であり、もう一つは、`global-batch.md`におけるグローバルバッチモデルマトリックスの更新です。

## 新機能
特に新機能の追加は今回の更新には含まれていません。

## 互換性に関する変更
互換性に影響を与えるような変更は今回はありません。

## その他の更新
- `audio.md`での見出しレベルの変更（見出しレベル3から2へ）
- `global-batch.md`でのグローバルバッチモデルマトリックスの更新
  - 新しいモデルの追加
  - モデルの提供状況のアップデート

# 洞察
この差分から読み取れるのは、OpenAI関連の文書がより明確で使いやすくなるように意図された改訂が行われているということです。まず、`audio.md`ファイル内での見出しレベルの変更は、ドキュメントの構造をより明確にし、情報の読み取りを容易にする目的があります。見出しが目立つことで、読者が必要なセクションに迅速にアクセスできるようにし、全体的な可読性が向上します。

また、`global-batch.md`でのグローバルバッチモデルマトリックスの更新は、各地域において利用可能なモデルの詳細を最新の内容に保ち、ユーザーがどこでどのモデルを利用できるかをより簡単に確認できるようにしています。この更新は、ドキュメントの情報が常に正確であり、信頼できるものであることを保証するための重要なステップです。

このような改訂は、読者の体験を向上させ、情報を的確に提供するために重要です。特に高度な技術文書では、内容が最新かつクリアであることが求められ、ユーザーが適時に正確な情報を得ることができるという利点があります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [audio.md](#item-624e70) | minor update | GPT-4o audio Realtime APIの見出しの修正 | modified | 1 | 1 | 2 | 
| [global-batch.md](#item-929e6a) | minor update | グローバルバッチモデルマトリックスの変更 | modified | 24 | 21 | 45 | 


# Modified Contents
## articles/ai-services/openai/concepts/audio.md{#item-624e70}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ Audio models in Azure OpenAI are available via the `realtime`, `completions`, an
 
 For information about the available audio models per region in Azure OpenAI Service, see the [audio models](models.md?tabs=standard-audio#standard-deployment-regional-models-by-endpoint), [standard models by endpoint](models.md?tabs=standard-audio#standard-deployment-regional-models-by-endpoint), and [global standard model availability](models.md?tabs=standard-audio#global-standard-model-availability) documentation.
 
-### GPT-4o audio Realtime API
+## GPT-4o audio Realtime API
 
 GPT-4o real-time audio is designed to handle real-time, low-latency conversational interactions, making it a great fit for support agents, assistants, translators, and other use cases that need highly responsive back-and-forth with a user. For more information on how to use GPT-4o real-time audio, see the [GPT-4o real-time audio quickstart](../realtime-audio-quickstart.md) and [how to use GPT-4o audio](../how-to/realtime-audio.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4o audio Realtime APIの見出しの修正"
}
```

### Explanation
この変更では、`audio.md`ファイル内の「GPT-4o audio Realtime API」の見出しのスタイルが更新されました。具体的には、見出しのレベルが3から2に変更され、より目立つ形式になっています。この修正は、ドキュメントの構造を明確にし、読者が情報を迅速に把握できるようにするためのものです。この変更により、他のセクションとの整合性が向上し、全体的な文書の可読性が改善されました。

## articles/ai-services/openai/includes/model-matrix/global-batch.md{#item-929e6a}

<details>
<summary>Diff</summary>
````diff
@@ -6,30 +6,33 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 02/07/2025
+ms.date: 04/21/2025
 ---
 
 
 | **Region**     | **o3-mini**, **2025-01-31**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
 |:-------------------|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
-| australiaeast      | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| brazilsouth        | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| canadaeast         | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| eastus             | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| eastus2            | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| francecentral      | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| germanywestcentral | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| japaneast          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| koreacentral       | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| northcentralus     | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| norwayeast         | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| polandcentral      | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southafricanorth   | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southcentralus     | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southindia         | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| swedencentral      | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| switzerlandnorth   | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| uksouth            | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westeurope         | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westus             | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| australiaeast      | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
+| brazilsouth        | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| canadaeast         | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
+| eastus             | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
+| eastus2            | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
+| francecentral      | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
+| germanywestcentral | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| italynorth         | ✅                        | -                      | -                      | -                      | -                           | -               | -                           | -                      | -                      | -                      |
+| japaneast          | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
+| koreacentral       | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| northcentralus     | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
+| norwayeast         | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| polandcentral      | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southafricanorth   | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southcentralus     | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southindia         | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| spaincentral       | ✅                        | -                      | -                      | -                      | -                           | -               | -                           | -                      | -                      | -                      |
+| swedencentral      | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
+| switzerlandnorth   | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
+| uaenorth           | ✅                        | -                      | -                      | -                      | -                           | -               | -                           | -                      | -                      | -                      |
+| uksouth            | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
+| westeurope         | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westus             | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | westus3            | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルバッチモデルマトリックスの変更"
}
```

### Explanation
この変更では、`global-batch.md`ファイル内のグローバルバッチモデルマトリックスが更新され、多くの地域に対するモデルの利用可能性を示すテーブルに変更が加えられました。具体的には、新しいモデルが追加され、従来のモデルの提供状況も更新されました。また、日付が修正され、最新の情報を反映しています。各地域におけるモデルの利用可能性に関する情報がより明確になり、ユーザーは各モデルがどの地域で利用可能かをより簡単に確認できるようになっています。全体として、これによりドキュメントの正確性と信頼性が向上しました。


