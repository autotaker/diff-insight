---
date: '2025-04-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a9279bd...MicrosoftDocs:2873777
summary: この文書では、軽微なアップデートを中心に用語の正確化や新しいモデル情報の追加、冗長な情報の削減が行われました。特に、新しい用語の採用やモデルの地域情報、可用性の更新が含まれており、OpenAIのクォータと制限に関する情報も最新化されています。新しいモデルオプションやプランに関する詳細情報が追加された一方で、破壊的な変更はありません。また、用語の修正や情報の簡素化があったことで、ユーザーがより正確で新しい情報を理解しやすくなっています。これにより、ユーザーエクスペリエンスが向上し、AI技術のグローバルな導入が促進されることが期待されます。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a9279bd...MicrosoftDocs:2873777){target="_blank"}

# ハイライト
この文書の変更は基本的に軽微なアップデートで構成されており、用語の正確化、新しいモデル情報の追加、冗長な情報の削減が中心です。特に、新しい用語の採用、モデルの地域情報と可用性の更新が行われています。また、OpenAIのクォータと制限に関する情報も最新化されています。

## 新機能
- 新しいモデルオプションがAIモデルの提供情報に追加されました。
- OpenAIのクォータ制限に新しいプランや詳細情報が追加されました。

## 破壊的変更
- 特に破壊的な変更はありません。情報の追加、整理、アップデートに留まっています。

## その他のアップデート
- LoRAの用語が"low rank adaptation"に変更。
- 標準的なチャット完了モデルから「southafricanorth」に関する冗長な行が削除。
- 複数の表が簡素化され、モデル情報が明確化。
- クォータと制限に関する情報が細分化され、特定のプランの詳細が強化。

# インサイト
今回の変更は、主に既存の文書の改善と最新の状況への適応が目的となっています。それぞれの文書内の用語や情報が更新され、ユーザーがより正確で新しい情報をスムーズに理解できるよう設計されています。LoRAに関する用語の修正は、テクノロジーの正確な把握と関連する読者にとっての理解を深める役割を果たします。また、AIモデルやOpenAIのクォータ・制限に関する情報更新は、対象ユーザーに対して重要な意思決定の支援を行うでしょう。

AI技術の急速な進化に伴い、こうしたタイムリーなドキュメントの更新は特に重要です。新機能や既存機能の改善に関する情報が随時提供されることにより、ユーザーエクスペリエンスが向上し、さらなる技術採用と利用推進が期待されます。特に、グローバル展開と多様な市場でのAI導入が進む中で、地域ごとのモデルサポート状況やクォータの詳細情報を明確に示すことが重要となっています。これにより、グローバルなユーザーが自分に最適なストラテジーを選択しやすくなります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [fine-tuning.md](#item-5c0e85) | minor update | 用語の変更: LoRAの説明を更新 | modified | 1 | 1 | 2 | 
| [provisioned-models.md](#item-8ee639) | minor update | モデル情報の追加と表の整理 | modified | 27 | 25 | 52 | 
| [standard-chat-completions.md](#item-aae3f1) | minor update | 冗長な行の削除 | modified | 0 | 1 | 1 | 
| [standard-global.md](#item-17a84b) | minor update | モデル情報の修正と地域データの調整 | modified | 7 | 7 | 14 | 
| [standard-models.md](#item-af04c4) | minor update | 南アフリカ北部のモデル情報の更新 | modified | 1 | 1 | 2 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータと制限に関する情報の更新 | modified | 20 | 11 | 31 | 


# Modified Contents
## articles/ai-services/openai/how-to/fine-tuning.md{#item-5c0e85}

<details>
<summary>Diff</summary>
````diff
@@ -23,7 +23,7 @@ Azure OpenAI Service lets you tailor our models to your personal datasets by usi
 
 In contrast to few-shot learning, fine tuning improves the model by training on many more examples than can fit in a prompt, letting you achieve better results on a wide number of tasks. Because fine tuning adjusts the base model’s weights to improve performance on the specific task, you won’t have to include as many examples or instructions in your prompt. This means less text sent and fewer tokens processed on every API call, potentially saving cost, and improving request latency.
 
-We use LoRA, or low rank approximation, to fine-tune models in a way that reduces their complexity without significantly affecting their performance. This method works by approximating the original high-rank matrix with a lower rank one, thus only fine-tuning a smaller subset of *important* parameters during the supervised training phase, making the model more manageable and efficient. For users, this makes training faster and more affordable than other techniques.
+We use LoRA, or low rank adaptation, to fine-tune models in a way that reduces their complexity without significantly affecting their performance. This method works by approximating the original high-rank matrix with a lower rank one, thus only fine-tuning a smaller subset of *important* parameters during the supervised training phase, making the model more manageable and efficient. For users, this makes training faster and more affordable than other techniques.
 
 ::: zone pivot="programming-language-studio"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の変更: LoRAの説明を更新"
}
```

### Explanation
この変更は、ドキュメント内での「LoRA」に関する用語の微小な修正を行いました。具体的には、"low rank approximation"から"low rank adaptation"に用語を変更しています。この修正により、LoRAのコンセプトをより正確に表現し、読者にとっての理解を向上させることを目的としています。この変更は、全体の内容に大きな影響を与えるものではありませんが、誤解を避けるための重要な修正と言えます。

## articles/ai-services/openai/includes/model-matrix/provisioned-models.md{#item-8ee639}

<details>
<summary>Diff</summary>
````diff
@@ -9,28 +9,30 @@ ms.custom: references_regions
 ms.date: 02/28/2025
 ---
 
-| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
-|:-------------------|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|
-| australiaeast      | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| brazilsouth        | ✅                       | -                      | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | -                      |
-| canadaeast         | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      |
-| eastus             | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| eastus2            | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| francecentral      | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | -                      | ✅                       |
-| germanywestcentral | ✅                       | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | -                      |
-| japaneast          | ✅                       | ✅                       | ✅                       | ✅                            | -               | ✅                        | ✅                        | ✅                            | -                   | -                      | ✅                       |
-| koreacentral       | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | -                       | ✅                            | ✅                    | ✅                       | -                      |
-| northcentralus     | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| norwayeast         | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                           | ✅                    | -                      | -                      |
-| polandcentral      | ✅                       | -                      | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| southafricanorth   | ✅                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                            | ✅                    | ✅                       | -                      |
-| southcentralus     | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| southeastasia      | -                      | ✅                       | ✅                       | ✅                            | -               | -                       | -                       | -                           | -                   | -                      | -                      |
-| southindia         | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | ✅                       |
-| swedencentral      | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| switzerlandnorth   | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| switzerlandwest    | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
-| uaenorth           | ✅                       | ✅                       | ✅                       | -                           | -               | ✅                        | -                       | -                           | -                   | ✅                       | ✅                       |
-| uksouth            | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| westus             | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| westus3            | ✅                       | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| **Region**     | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
+|:-------------------|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|
+| australiaeast      | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| brazilsouth        | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | -                      |
+| canadaeast         | ✅                        | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      |
+| eastus             | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| eastus2            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| francecentral      | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | -                      | ✅                       |
+| germanywestcentral | -                       | -                  | ✅                       | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | -                      |
+| japaneast          | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | -               | ✅                        | ✅                        | ✅                            | -                   | -                      | ✅                       |
+| koreacentral       | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | -                       | -                       | ✅                            | ✅                    | ✅                       | -                      |
+| northcentralus     | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| norwayeast         | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                           | ✅                    | -                      | -                      |
+| polandcentral      | -                       | -                  | ✅                       | -                      | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| southafricanorth   | -                       | -                  | ✅                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                            | ✅                    | ✅                       | -                      |
+| southcentralus     | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| southeastasia      | -                       | -                  | -                      | ✅                       | ✅                       | ✅                            | -               | -                       | -                       | -                           | -                   | -                      | -                      |
+| southindia         | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | ✅                       |
+| spaincentral       | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
+| swedencentral      | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| switzerlandnorth   | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| switzerlandwest    | -                       | -                  | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
+| uaenorth           | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | -                           | -               | ✅                        | -                       | -                           | -                   | ✅                       | ✅                       |
+| uksouth            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| westeurope         | -                       | -                  | -                      | -                      | ✅                       | -                           | -               | -                       | -                       | -                           | -                   | -                      | -                      |
+| westus             | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| westus3            | -                       | -                  | ✅                       | ✅                       | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル情報の追加と表の整理"
}
```

### Explanation
この変更は、AIモデルの提供状況を記載した表の情報を更新・整理することを目的としています。具体的には、表の列の構成に新しいモデルオプションを追加し、地域ごとのモデルの可用性をより明確に示しています。また、冗長な情報を削除し、モデルのバージョンとリリース日を整理することで、読みやすさと理解のしやすさを向上させています。これにより、ユーザーは新しいモデルやその地域ごとのサポート状況について迅速にアクセスできるようになります。全体として、この変更は情報の更新に寄与し、ドキュメントの品質を向上させるものです。

## articles/ai-services/openai/includes/model-matrix/standard-chat-completions.md{#item-aae3f1}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,6 @@ ms.date: 04/01/2025
 | japaneast        | -                          | -                       | -                      | -                      | ✅                       | -                           | -               | -                       | -                       | ✅                          | -                           | -                   | -                      | ✅                       | ✅                           |
 | northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | ✅                           |
 | norwayeast       | -                          | -                       | -                      | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | -                          |
-| southafricanorth | -                          | -                       | -                      | -                      | ✅                       | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                          |
 | southcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                          |
 | southindia       | -                          | -                       | -                      | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | ✅                       | ✅                       | -                          |
 | swedencentral    | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                    | ✅                       | ✅                       | ✅                           |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "冗長な行の削除"
}
```

### Explanation
この変更では、標準的なチャット完了モデルに関するドキュメントから冗長な行を削除しました。具体的には、「southafricanorth」という地域に関する行が削除され、表の簡素化と明確化が図られています。この変更により、情報がより集中し、ユーザーが必要な情報を見つけやすくなることを目的としています。全体的に、この修正はドキュメントのクリーンアップを行い、読みやすさを改善するための小規模な更新です。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -13,11 +13,11 @@ ms.date: 04/04/2025
 |:-------------------|:-----------------------------------:|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:----------------------------------------:|:------------------------------------------------:|:---------------------------------------------:|:-------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|
 | australiaeast      | -                               | ✅                        | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
 | brazilsouth        | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| canadaeast         | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| canadaeast         | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
 | eastus             | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | ✅                                          | ✅                            | ✅                              | ✅                              | ✅                              |
-| eastus2            | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | ✅                                          | ✅                            | ✅                              | ✅                              | -                             |
-| francecentral      | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| germanywestcentral | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| eastus2            | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | ✅                                          | ✅                            | ✅                              | ✅                              | ✅                              |
+| francecentral      | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
+| germanywestcentral | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
 | italynorth         | -                               | ✅                        | ✅                   | -                          | -                       | -                      | -                      | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | -                           | ✅                              | ✅                              | ✅                              |
 | japaneast          | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
 | koreacentral       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
@@ -27,11 +27,11 @@ ms.date: 04/04/2025
 | southafricanorth   | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
 | southcentralus     | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
 | southindia         | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| spaincentral       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| spaincentral       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
 | swedencentral      | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| switzerlandnorth   | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| switzerlandnorth   | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
 | uaenorth           | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
 | uksouth            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| westeurope         | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| westeurope         | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
 | westus             | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
 | westus3            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル情報の修正と地域データの調整"
}
```

### Explanation
この変更は、標準グローバルモデルに関するドキュメントの内容を修正することを目的としています。具体的には、モデルに関連する地域ごとのデータが更新され、不要な行が削除されるとともに、新しい情報が追加されています。例えば、地域「eastus2」「francecentral」「germanywestcentral」についての情報が調整されています。この変更により、モデルの可用性がより正確かつ最新の情報を反映する形になり、ユーザーが地域ごとの対応状況を確認しやすくなります。全体として、この修正は読者に対して有用な情報を提供するための小規模な更新ですが、ドキュメントの品質向上に貢献しています。

## articles/ai-services/openai/includes/model-matrix/standard-models.md{#item-af04c4}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ ms.date: 04/01/2025
 | northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | ✅                           | -                               | -                             | -                             | -                             | ✅                              | -                 | ✅             | ✅                | ✅                 |
 | norwayeast       | -                          | -                       | -                      | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
 | polandcentral    | -                          | -                       | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -            | -               | -                |
-| southafricanorth | -                          | -                       | -                      | -                      | ✅                       | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
+| southafricanorth | -                          | -                       | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
 | southcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | -                      | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                          | -                               | -                             | -                             | ✅                              | ✅                              | -                 | -            | -               | -                |
 | southeastasia    | -                          | -                       | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -            | -               | -                |
 | southindia       | -                          | -                       | -                      | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | ✅                       | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "南アフリカ北部のモデル情報の更新"
}
```

### Explanation
この変更では、標準モデルに関するドキュメントの一部が修正され、特に「southafricanorth」という地域に関する情報が調整されました。具体的には、この地域に関連する行が修正され、モデル情報が得られない場合の処理が簡素化されています。この変更により、ドキュメントの情報が更新され、ユーザーに対してより正確な状況を伝えることが可能になります。また、全体として、この修正はドキュメントの信頼性を高めるための小規模な更新であり、さまざまなモデルの利用可能性についての情報をクリアに提供することを目的としています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 4/08/2025
+ms.date: 4/09/2025
 ms.author: mbullwin
 ---
 
@@ -86,7 +86,7 @@ The following sections provide you with a quick guide to the default quotas and
 >
 > This is particularly important for programmatic model deployment as this change in RPM/TPM ratio can result in accidental under allocation of quota if one is still assuming the 1:1000 ratio followed by older chat completion models.
 >
-> There is a known issue with the [quota/usages API](/rest/api/aiservices/accountmanagement/usages/list?view=rest-aiservices-accountmanagement-2024-06-01-preview&tabs=HTTP&preserve-view=true) where it assumes the old ratio applies to the new o1-series models. The API returns the correct base capacity number, but doesn't apply the correct ratio for the accurate calculation of TPM.
+> There's a known issue with the [quota/usages API](/rest/api/aiservices/accountmanagement/usages/list?view=rest-aiservices-accountmanagement-2024-06-01-preview&tabs=HTTP&preserve-view=true) where it assumes the old ratio applies to the new o1-series models. The API returns the correct base capacity number, but doesn't apply the correct ratio for the accurate calculation of TPM.
 
 ### `o-series` global standard
 
@@ -199,14 +199,18 @@ If your Azure subscription is linked to certain [offer types](https://azure.micr
 
 |Tier| Quota Limit in tokens per minute (TPM) |
 |---|:---|
-|Azure for Students, Free Trials | 1 K (all models) <br>Exception o-series & GPT 4.5 Preview: 0|
-| MSDN | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br>computer-use-preview: 30 K <br> gpt-4o-realtime-preview: 1 K <br> o-series: 0 <br> GPT 4.5 Preview: 0  |
-|Pay-as-you-go | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br>computer-use-preview: 30 K <br> o-series: 0 <br> GPT 4.5 Preview: 0   |
-| CSP Dev Test<sup>*</sup> | All models: 0 |
+|`Azure for Students` | 1 K (all models) <br>Exception o-series & GPT 4.5 Preview: 0|
+| `MSDN` | GPT-4o-mini: 200 K <br> GPT 3.5 Turbo Series: 200 K <br> GPT-4 series: 50 K <br>computer-use-preview: 8 K <br> gpt-4o-realtime-preview: 1 K <br> o-series: 0 <br> GPT 4.5 Preview: 0  |
+|`Pay-as-you-go` | GPT-4o-mini: 200 K <br> GPT 3.5 Turbo Series: 200 K <br> GPT-4 series: 50 K <br>computer-use-preview: 30 K <br> o-series: 0 <br> GPT 4.5 Preview: 0   |
+| `Azure_MS-AZR-0111P`  <br> `Azure_MS-AZR-0035P` <br> `Azure_MS-AZR-0025P` <br> `Azure_MS-AZR-0052P` <br>| GPT-4o-mini: 200 K <br> GPT 3.5 Turbo Series: 200 K <br> GPT-4 series: 50 K   |
+| `CSP Integration Sandbox` <sup>*</sup> | All models: 0 |
+| `Lightweight trial`<br>`Free Trials`<br>`Azure Pass`  | All models: 0 |
 
-<sup>*</sup>This only applies to a small number of dev/test CSP subscriptions. Use the query below to determine what `quotaId` is associated with your subscription.
 
-To determine the offer type that is associated with your subscription you can check your `quotaId`. If your `quotaId` is not listed in this table your subscription qualifies for default quota.
+
+<sup>*</sup>This only applies to a small number of legacy CSP sandbox subscriptions. Use the query below to determine what `quotaId` is associated with your subscription.
+
+To determine the offer type that is associated with your subscription you can check your `quotaId`. If your `quotaId` isn't listed in this table your subscription qualifies for default quota.
 
 # [REST](#tab/REST)
 
@@ -247,14 +251,19 @@ az rest --method GET --uri "https://management.azure.com/subscriptions/{sub-id}?
 }
 ```
 
-| Quota allocation | Subscription quota ID |
+| Quota allocation/Offer type | Subscription quota ID |
 |:---|:----|
 | Enterprise | `EnterpriseAgreement_2014-09-01` |
 | Pay-as-you-go | `PayAsYouGo_2014-09-01`|
 | MSDN | `MSDN_2014-09-01` |
-| CSP Dev/Test | `CSPDEVTEST_2018-05-01` |
+| CSP Integration Sandbox | `CSPDEVTEST_2018-05-01` |
 | Azure for Students | `AzureForStudents_2018-01-01` |
-| Free Trial | `FreeTrial_2014-09-01` |
+| Free Trial    | `FreeTrial_2014-09-01` |
+| Azure Pass             | `AzurePass_2014-09-01` |
+| Azure_MS-AZR-0111P            | `AzureInOpen_2014-09-01` |
+| Azure_MS-AZR-0150P  | `LightweightTrial_2016-09-01` |
+| Azure_MS-AZR-0035P <br> Azure_MS-AZR-0025P <br> Azure_MS-AZR-0052P <br>| `MPN_2014-09-01` |
+| Azure_MS-AZR-0023P <br> Azure_MS-AZR-0060P <br> Azure_MS-AZR-0148P <br> Azure_MS-AZR-0148G | `MSDNDevTest_2014-09-01`|
 | Default | Any quota ID not listed in this table  |
 
 ### General best practices to remain within rate limits
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
この変更は、OpenAIのクォータと制限についてのドキュメントを更新することを目的としています。具体的には、さまざまなモデルやサービスに対するクォータの値や制限に関する情報が変更され、明確化されています。特に、`Azure for Students`や`Pay-as-you-go`のクォータ制限が追加されており、いくつかのプランの詳細な情報が提供されています。また、古いバージョンのモデルに関連する問題点についての説明が改善され、ユーザーが新しいo1シリーズモデルに対するクォータの理解を深めやすくなっています。この修正は、ドキュメントが最新の情報を反映し、ユーザーがサービスを利用する際の参考になることを意図しています。全体として、修正された内容はクォータに関するガイドラインをより充実させ、最適な利用方法を提示する役割を果たしています。


