---
date: '2025-04-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:63f4fcb...MicrosoftDocs:b48656b
summary: 変更点のハイライトは、モデルやドキュメントの日付が更新され、一部のセクションや情報が削除され、最新の状態に保たれたことです。これにより、ユーザーはより正確で整理された情報を得ることができます。新しいモデルが追加され、特に`gpt-4.5`モデルのクォータリミットが大幅に増加しました。これにより、ユーザーはより多くのトランザクションやテストを行うことが可能になります。削除された情報は不要と判断され、ドキュメントの明瞭さが向上しました。全体として、この更新は最新の情報を提供することで利用者に対する価値を最大化することを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:63f4fcb...MicrosoftDocs:b48656b){target="_blank"}

# Highlights
変更点のハイライトは、モデルやドキュメントの日付更新とともに、特定のセクションや記載が削除され、情報が最新化された点です。これにより、ユーザーはより正確で整理された情報を得ることができます。

## 新機能
- 新しいモデル`o1`、`o3-mini`、`gpt-4o`が追加され、可用性情報が更新されました。

## 重要な変更
- `gpt-4.5-preview`に関するアクセス要件と登録に関する情報が削除されました。
- `gpt-4.5`モデルのクォータリミットが大幅に増加しました。

## その他の更新
- 様々なセクションでドキュメントの日付が更新されました。
- 情報の整理と不要な行の削除により、文書の整合性が向上しています。

# Insights
このドキュメントの更新は主に、モデルやサービスに関連する最新の情報をスムーズに提供することを目的としています。データの日付やモデルのバージョンが随時更新されていることは、常に最新の状態でサービスを利用するために重要です。特に、`gpt-4.5`モデルのクォータリミットの増加は、ユーザーの使用可能なトークン数を大幅に引き上げ、より多くのトランザクションやテストを可能にします。

削除された情報は、直接的にはユーザーにとって必須でないと判断された可能性が高く、ドキュメントのシンプルさや読みやすさ、明瞭さを高める役割を果たしています。特に、登録要件の詳細が削除されたことは、利用者の混乱を減らし、必要な情報にフォーカスするための措置であると考えられます。

全体として、日々進化するAIサービスの環境にて、最新の情報を素早くかつ正確に提供することが重要であり、このようなドキュメントの更新は継続的に行われることで、利用者に対する価値を最大化すると言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | モデルの更新日付とセクションの削除 | modified | 1 | 9 | 10 | 
| [datazone-provisioned-managed.md](#item-ae7f5b) | minor update | モデルのバージョンと日付の更新 | modified | 16 | 15 | 31 | 
| [provisioned-global.md](#item-340884) | minor update | プロビジョニングされたグローバルモデル情報の更新 | modified | 29 | 29 | 58 | 
| [standard-chat-completions.md](#item-aae3f1) | minor update | 標準チャット完了に関するモデル情報の更新 | modified | 20 | 19 | 39 | 
| [standard-embeddings.md](#item-656427) | minor update | 標準埋め込みモデル情報の更新 | modified | 5 | 3 | 8 | 
| [standard-models.md](#item-af04c4) | minor update | 標準モデル情報の更新 | modified | 25 | 23 | 48 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータと制限に関する情報の更新 | modified | 3 | 3 | 6 | 
| [whats-new.md](#item-53303b) | minor update | 最新情報セクションの不要な記述削除 | modified | 0 | 4 | 4 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 03/25/2025
+ms.date: 04/01/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -60,14 +60,6 @@ Once access has been granted, you will need to create a deployment for the model
 
 ## GPT-4.5 Preview
 
-### Availability
-
-**For access to `gpt-4.5-preview` registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who have access to other limited access models will still need to request access for this model.
-
-Request access: [GPT-4.5-preview limited access model application](https://aka.ms/oai/gptaccess)
-
-Once access has been granted, you will need to create a deployment for the model
-
 ### Region Availability
 
 | Model | Region |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの更新日付とセクションの削除"
}
```

### Explanation
このコードの変更は、ドキュメント内の更新日付を変更し、特定のセクションを削除する内容です。具体的には、`ms.date`が2025年3月25日から2025年4月1日に変更されました。同時に、`gpt-4.5-preview`のアクセス条件について説明したセクションが削除されました。この削除により、利用可能なモデルの情報が簡潔になり、より関連性の高い内容に焦点を当てることができるようになっています。全体として、この変更は文書の精度を向上させることを目的としています。

## articles/ai-services/openai/includes/model-matrix/datazone-provisioned-managed.md{#item-ae7f5b}

<details>
<summary>Diff</summary>
````diff
@@ -5,20 +5,21 @@ description: Regional availability for data zone provisioned managed models
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 01/15/2025
+ms.custom: references_regions
+ms.date: 03/31/2025
 ---
 
-| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|
-| eastus             | ✅                       | ✅                       | ✅                            |
-| eastus2            | ✅                       | ✅                       | ✅                            |
-| francecentral      | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | ✅                       | ✅                       | ✅                            |
-| northcentralus     | ✅                       | ✅                       | ✅                            |
-| polandcentral      | ✅                       | ✅                       | ✅                            |
-| southcentralus     | ✅                       | ✅                       | ✅                            |
-| spaincentral       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | ✅                       | ✅                       | ✅                            |
-| westeurope         | ✅                       | ✅                       | ✅                            |
-| westus             | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
+| **Region**     | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
+| eastus             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus2            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| northcentralus     | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのバージョンと日付の更新"
}
```

### Explanation
このコードの変更は、データゾーンで提供された管理モデルの地域別の可用性に関するドキュメントを更新するものです。主な変更点として、`ms.date`が2025年1月15日から2025年3月31日に変更され、さらに新しいモデルバージョン（`o1`、`o3-mini`、および`gpt-4o`の新しいリリース日）が表に追加されました。この更新によって、各モデルの利用可能な地域が最新の情報に基づいて整理され、利用者にとっての明確な可用性が提供されるようになっています。また、いくつかの不要な行が削除され、情報が整理されました。この変更は、文書の整合性と信頼性を高めることを目的としています。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -6,34 +6,34 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 03/12/2025
+ms.date: 03/31/2025
 ---
 
-| **Region**     | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
-| australiaeast      | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| brazilsouth        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| canadaeast         | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus             | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus2            | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| francecentral      | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| italynorth         | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| japaneast          | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| koreacentral       | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| northcentralus     | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| norwayeast         | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| polandcentral      | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southafricanorth   | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southcentralus     | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southeastasia      | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southindia         | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| spaincentral       | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandnorth   | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandwest    | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| uaenorth           | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| uksouth            | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westeurope         | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus             | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
+| **Region**     | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
+| australiaeast      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| brazilsouth        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| canadaeast         | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus2            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| italynorth         | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| japaneast          | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| koreacentral       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| northcentralus     | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| norwayeast         | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southafricanorth   | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southeastasia      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southindia         | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandnorth   | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandwest    | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| uaenorth           | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| uksouth            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされたグローバルモデル情報の更新"
}
```

### Explanation
このコードの変更は、プロビジョニングされたグローバルモデルに関する情報を更新するもので、主に地域別のモデル可用性に関するテーブル内容が変更されました。具体的には、`ms.date`が2025年3月12日から2025年3月31日に変更されたほか、新たに`o3-mini`モデルが追加され、関連する地域別の可用性がテーブルに反映されました。これにより、各モデルのリリース日やその利用可能地域が最新の情報に基づいて明確に表示されるようになり、利用者にとっての利便性が向上しています。また、すべての行が削除され新しい行で置き換えられる形式で28行が追加され、情報が整理されています。この変更は、文書の正確性を高めることを目的としています。

## articles/ai-services/openai/includes/model-matrix/standard-chat-completions.md{#item-aae3f1}

<details>
<summary>Diff</summary>
````diff
@@ -6,24 +6,25 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 10/25/2024
+ms.date: 04/01/2025
 ---
 
-| **Region**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **vision-preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **0301**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   | **gpt-35-turbo-16k**, **0613**   |
-|:-----------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-----------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:------------------------------:|
-| australiaeast    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           |
-| canadaeast       | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           |
-| eastus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           |
-| eastus2          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           |
-| francecentral    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | ✅                       | ✅                       | ✅                       | -                      | ✅                           |
-| japaneast        | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | ✅                          | -                           | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           |
-| northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           |
-| norwayeast       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          |
-| southcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | -                      | -                      | ✅                       | -                          |
-| southindia       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | ✅                       | ✅                       | -                          |
-| swedencentral    | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           |
-| switzerlandnorth | -                          | -                       | -                      | -                      | -                           | ✅                | -                       | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | -                      | ✅                       | ✅                           |
-| uksouth          | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | ✅                        | -                         | -                           | -                   | ✅                       | ✅                       | ✅                       | ✅                       | ✅                           |
-| westeurope       | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          |
-| westus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | ✅                          | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          |
-| westus3          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          |
+| **Region**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **vision-preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   | **gpt-35-turbo-16k**, **0613**   |
+|:-----------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-----------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:------------------------------:|
+| australiaeast    | -                          | -                       | -                      | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                          | -                           | ✅                    | ✅                       | ✅                       | ✅                           |
+| canadaeast       | -                          | -                       | -                      | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | ✅                       | ✅                       | ✅                           |
+| eastus           | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | ✅                           |
+| eastus2          | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | -                       | -                         | ✅                            | -                   | -                      | ✅                       | ✅                           |
+| francecentral    | -                          | -                       | -                      | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | ✅                       | ✅                       | ✅                           |
+| japaneast        | -                          | -                       | -                      | -                      | ✅                       | -                           | -               | -                       | -                       | ✅                          | -                           | -                   | -                      | ✅                       | ✅                           |
+| northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | ✅                           |
+| norwayeast       | -                          | -                       | -                      | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | -                          |
+| southafricanorth | -                          | -                       | -                      | -                      | ✅                       | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                          |
+| southcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                          |
+| southindia       | -                          | -                       | -                      | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | ✅                       | ✅                       | -                          |
+| swedencentral    | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                    | ✅                       | ✅                       | ✅                           |
+| switzerlandnorth | -                          | -                       | -                      | -                      | -                      | -                           | ✅                | -                       | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | ✅                           |
+| uksouth          | -                          | -                       | -                      | -                      | -                      | -                           | -               | ✅                        | ✅                        | -                         | -                           | -                   | ✅                       | ✅                       | ✅                           |
+| westeurope       | -                          | -                       | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | ✅                       | -                          |
+| westus           | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | -               | ✅                        | -                       | ✅                          | ✅                            | -                   | ✅                       | ✅                       | -                          |
+| westus3          | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | ✅                       | -                          |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準チャット完了に関するモデル情報の更新"
}
```

### Explanation
このコードの変更は、標準チャット完了に関するモデル情報を更新するもので、主にモデルのリリース日や地域別の可用性に関する情報が改訂されました。具体的には、`ms.date`が2024年10月25日から2025年4月1日に変更され、新しいモデルとして`gpt-4o`のリリース日が2024年11月20日として追加されました。これにより、利用者は各モデルの最新情報を確認できるようになっています。

さらに、地域別の可用性においてもいくつかのモデルの情報が更新され、具体的には一部の地域での新しいモデルの可用性が追加されたり、既存のモデルに関連する情報が調整されています。この変更は、利用者にとっての情報の正確性を向上させ、ドキュメントの整合性を強化することを目的としています。全体として、合計39の変更が行われました。

## articles/ai-services/openai/includes/model-matrix/standard-embeddings.md{#item-656427}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: embedding model regional availability
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 03/25/2024
+ms.date: 04/01/2025
 ---
 
 | **Region**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **1**   | **text-embedding-ada-002**, **2**   |
@@ -20,12 +20,14 @@ ms.date: 03/25/2024
 | northcentralus   | -                             | -                             | -                             | ✅                              |
 | norwayeast       | -                             | ✅                              | -                             | ✅                              |
 | polandcentral    | -                             | ✅                              | -                             | -                             |
-| southafricanorth | -                             | -                             | -                             | ✅                              |
+| southafricanorth | -                             | ✅                              | -                             | ✅                              |
 | southcentralus   | -                             | -                             | ✅                              | ✅                              |
+| southeastasia    | -                             | ✅                              | -                             | -                             |
 | southindia       | -                             | ✅                              | -                             | ✅                              |
+| spaincentral     | -                             | ✅                              | -                             | -                             |
 | swedencentral    | -                             | ✅                              | -                             | ✅                              |
 | switzerlandnorth | ✅                              | ✅                              | -                             | ✅                              |
-| uaenorth         | -                             | -                             | -                             | ✅                              |
+| uaenorth         | ✅                              | ✅                              | -                             | ✅                              |
 | uksouth          | -                             | ✅                              | -                             | ✅                              |
 | westeurope       | -                             | -                             | -                             | ✅                              |
 | westus           | ✅                              | -                             | -                             | ✅                              |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準埋め込みモデル情報の更新"
}
```

### Explanation
このコードの変更は、標準埋め込みモデルに関する情報を更新するものであり、主にモデルのリリース日や地域別の可用性に関する内容が改訂されました。具体的には、`ms.date`が2024年3月25日から2025年4月1日に変更されました。

加えて、地域別のモデル可用性にいくつかの改訂が加えられました。特に、いくつかの地域（例：`southafricanorth`、`southeastasia`、`spaincentral`、`uaenorth`）において、特定のモデルの可用性が新たに追加され、一部の地域では可用性のステータスが更新されました。

これにより、ユーザーは各モデルの最新の可用性について正確な情報を得ることができ、全体のドキュメントの整合性が強化されています。全体として、合計8の変更が行われました。

## articles/ai-services/openai/includes/model-matrix/standard-models.md{#item-af04c4}

<details>
<summary>Diff</summary>
````diff
@@ -5,29 +5,31 @@ description: Quota and limits for Azure OpenAI by region.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 02/06/2025
+ms.date: 04/01/2025
 ---
 
 
-| **Region**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **vision-preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **0301**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   | **gpt-35-turbo-16k**, **0613**   | **gpt-35-turbo-instruct**, **0914**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **1**   | **text-embedding-ada-002**, **2**   | **dall-e-3**, **3.0**   | **tts**, **001**   | **tts-hd**, **001**   | **whisper**, **001**   |
-|:-----------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-----------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:------------------------------:|:-----------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------:|:----------------:|:-------------------:|:--------------------:|
-| australiaeast    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | ✅                  | -            | -               | -                |
-| brazilsouth      | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -            | -               | -                |
-| canadaeast       | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
-| eastus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | -            | -               | -                |
-| eastus2          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
-| francecentral    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | ✅                       | ✅                       | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
-| japaneast        | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | ✅                          | -                           | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
-| northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | -                             | -                             | ✅                              | -                 | ✅             | ✅                | ✅                 |
-| norwayeast       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
-| polandcentral    | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -            | -               | -                |
-| southafricanorth | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -            | -               | -                |
-| southcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | -                      | -                      | ✅                       | -                          | -                               | -                             | -                             | ✅                              | ✅                              | -                 | -            | -               | -                |
-| southindia       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
-| swedencentral    | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | ✅                                | -                             | ✅                              | -                             | ✅                              | ✅                  | ✅             | ✅                | ✅                 |
-| switzerlandnorth | -                          | -                       | -                      | -                      | -                           | ✅                | -                       | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
-| uaenorth         | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
-| uksouth          | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | ✅                        | -                         | -                           | -                   | ✅                       | ✅                       | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
-| westeurope       | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -            | -               | ✅                 |
-| westus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | ✅                          | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | ✅                              | -                             | -                             | ✅                              | -                 | -            | -               | -                |
-| westus3          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
\ No newline at end of file
+| **Region**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **vision-preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   | **gpt-35-turbo-16k**, **0613**   | **gpt-35-turbo-instruct**, **0914**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **1**   | **text-embedding-ada-002**, **2**   | **dall-e-3**, **3.0**   | **tts**, **001**   | **tts-hd**, **001**   | **whisper**, **001**   |
+|:-----------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-----------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:------------------------------:|:-----------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------:|:----------------:|:-------------------:|:--------------------:|
+| australiaeast    | -                          | -                       | -                      | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                          | -                           | ✅                    | ✅                       | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | ✅                  | -            | -               | -                |
+| brazilsouth      | -                          | -                       | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -            | -               | -                |
+| canadaeast       | -                          | -                       | -                      | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | ✅                       | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
+| eastus           | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | -            | -               | -                |
+| eastus2          | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | -                       | -                         | ✅                            | -                   | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
+| francecentral    | -                          | -                       | -                      | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
+| japaneast        | -                          | -                       | -                      | -                      | ✅                       | -                           | -               | -                       | -                       | ✅                          | -                           | -                   | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
+| northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | ✅                           | -                               | -                             | -                             | -                             | ✅                              | -                 | ✅             | ✅                | ✅                 |
+| norwayeast       | -                          | -                       | -                      | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
+| polandcentral    | -                          | -                       | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -            | -               | -                |
+| southafricanorth | -                          | -                       | -                      | -                      | ✅                       | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
+| southcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                          | -                               | -                             | -                             | ✅                              | ✅                              | -                 | -            | -               | -                |
+| southeastasia    | -                          | -                       | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -            | -               | -                |
+| southindia       | -                          | -                       | -                      | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | ✅                       | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
+| spaincentral     | -                          | -                       | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -            | -               | -                |
+| swedencentral    | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                    | ✅                       | ✅                       | ✅                           | ✅                                | -                             | ✅                              | -                             | ✅                              | ✅                  | ✅             | ✅                | ✅                 |
+| switzerlandnorth | -                          | -                       | -                      | -                      | -                      | -                           | ✅                | -                       | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
+| uaenorth         | -                          | -                       | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                          | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
+| uksouth          | -                          | -                       | -                      | -                      | -                      | -                           | -               | ✅                        | ✅                        | -                         | -                           | -                   | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
+| westeurope       | -                          | -                       | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | ✅                       | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -            | -               | ✅                 |
+| westus           | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | -               | ✅                        | -                       | ✅                          | ✅                            | -                   | ✅                       | ✅                       | -                          | -                               | ✅                              | -                             | -                             | ✅                              | -                 | -            | -               | -                |
+| westus3          | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | ✅             | ✅                | -                |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準モデル情報の更新"
}
```

### Explanation
このコードの変更は、標準モデルに関するドキュメントを更新するもので、主にモデルのリリース日や地域別における可用性に関する情報が改訂されています。具体的には、`ms.date`が2025年2月6日から2025年4月1日に変更され、新しいモデルとして`gpt-4o`のリリース日が2024年11月20日として追加されました。

さらに、モデルの地域別可用性に関してもいくつかの変更が行われました。一部の地域では新しいモデルの可用性が追加されたり、既存のモデルの可用性状況が更新されたりしています。たとえば、`southafricanorth`や`eaenorth`などの地域に新たにモデルが追加されています。これにより、ユーザーは各モデルの最新の可用性を簡単に把握できるようになっています。

合計で48の変更があり、全体としてドキュメントの正確性と一貫性を向上させることを目的としています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 3/04/2025
+ms.date: 4/02/2025
 ms.author: mbullwin
 ---
 
@@ -73,8 +73,8 @@ The following sections provide you with a quick guide to the default quotas and
 
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
 |---|---|:---:|:---:|
-| `gpt-4.5` | Enterprise Tier | 50 K | 50 |
-| `gpt-4.5` | Default | 50 K | 50 |
+| `gpt-4.5` | Enterprise Tier | 200 K | 200 |
+| `gpt-4.5` | Default | 150 K | 150 |
 
 ## `o-series` rate limits
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータと制限に関する情報の更新"
}
```

### Explanation
このコードの変更は、OpenAIのクォータと制限に関するドキュメントを更新するもので、主にモデル`gpt-4.5`のクォータ制限が改訂されました。具体的には、`gpt-4.5`モデルに対するエンタープライズティアとデフォルトティアのそれぞれのトークンあたりの制限が変更されました。

- エンタープライズティアのクォータリミットが50Kトークンから200Kトークンに増加しました。
- デフォルトティアのクォータリミットも50Kトークンから150Kトークンに増加されました。

さらに、ドキュメントの日付も2025年3月4日から2025年4月2日に更新されています。これにより、ユーザーは最新のクォータと制限に関する正確な情報を得ることができるようになっています。全体として6の変更が行われ、ドキュメントの正確性と一貫性が向上しています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -49,10 +49,6 @@ In addition to the deployment-level content filtering configuration, we now also
 
 The latest GPT model that excels at diverse text and image tasks is now available on Azure OpenAI.
 
-**For access to `gpt-4.5-preview` registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who have access to other limited access models will still need to request access for this model.
-
-Request access: [GPT-4.5-preview limited access model application](https://aka.ms/oai/gptaccess)
-
 For more information on model capabilities, and region availability see the [models documentation](./concepts/models.md#gpt-45-preview).
 
 ### Stored completions API
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新情報セクションの不要な記述削除"
}
```

### Explanation
このコードの変更は、OpenAIの「最新情報」セクションにおける不要な記述を削除するもので、具体的には`gpt-4.5-preview`モデルにアクセスするための登録要件に関する情報が削除されました。

以下の内容が削除されました：
- `gpt-4.5-preview`モデルにアクセスするためには登録が必要であり、アクセスはMicrosoftの基準に基づいて付与されること。
- 他の限定アクセスモデルにアクセスを持つ顧客も、このモデルへのアクセスを申請する必要があること。
- アクセス要求リンクがあった文。

これにより、文書はより簡潔になり、必要な情報に集中することができるようになりました。全体として、4つの変更があり、ドキュメントの一貫性と明瞭さが向上しています。


