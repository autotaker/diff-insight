---
date: '2024-09-12'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:67d9a22...MicrosoftDocs:9392315
summary: 今回の変更は、Azure OpenAIサービスに関するドキュメントのアップデートが主な内容であり、モデルの退役日変更、地域ごとのクォータ情報、および標準モデルの可用性に関する情報が更新されています。特に、GPT-4o
  miniに関する新しい情報が追加された点が挙げられます。破壊的な変更はなく、更新された情報は利用者にとって重要です。ユーザーはこれにより、モデルの利用計画やリソース管理をより効果的に行うことができるようになります。要するに、これらのマイナーアップデートは、ユーザーの体験を向上させるための重要な改善を提供しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:67d9a22...MicrosoftDocs:9392315){target="_blank"}

# ハイライト
今回の変更は、主にAzure OpenAIサービスに関するドキュメントのアップデートが中心であり、モデルの退役日変更や地域ごとのクォータ情報、標準モデルの可用性に関する更新が含まれています。これらの変更は全てマイナーアップデートに分類され、ユーザーにとって重要な情報を最新の状態に保つことを目的としています。

## 新機能
- GPT-4o miniに関する新しい情報が追加され、目次のアップデートが行われた。

## 破壊的変更
- 特記すべき破壊的変更はありません。

## その他の更新
- `gpt-35-turbo`及び`gpt-4`モデルの退役日が更新された。
- 特定の地域 (`eastus2`、`northcentralus`、`swedencentral`など) におけるクォータ情報が修正された。
- `norwayeast`地域におけるスタンダード埋め込み（standard embeddings）の可用性が更新された。
- `eastus`，`eastus2`，`westus`，`westus3`地域におけるGPT-3.5 Turboのモデル利用状況が更新された。
- `westus3`地域でのGPT-4のモデル利用可用性が明確にされた。
- 目次（toc.yml）が更新され、新しい項目が追加された。

# 洞察
Azure OpenAIサービスの利用者にとって、更新されたドキュメントは非常に重要です。このマイナーアップデートにより、ユーザーは最新の情報を元にサービスを最大限に活用することができます。特に、以下のポイントが注目されます。

1. **モデルの退役日変更とアップグレード**:
    - `gpt-35-turbo`（0301および0613）及び`gpt-4`モデルの退役日が2025年1月27日に変更されたことで、ユーザーはこれらのモデルに関する計画をより正確に立てることが可能になります。特に業務でこれらのモデルを利用する場合、適切な移行戦略を準備することが重要です。

2. **地域ごとのクォータ情報**:
    - `eastus2`、`northcentralus`、`swedencentral`などの地域におけるクォータ情報の更新により、これらの地域でのリソース管理がより適切に行えるようになります。リソースの利用上限が変更されることは、特定のプロジェクトにどの程度のリソースを割り当てるかを決定する際に非常に重要です。

3. **モデルの可用性更新**:
    - `norwayeast`、`eastus`、`eastus2`、`westus`、及び`westus3`地域におけるモデルの利用可能性が更新され、より多くの地域でAzure OpenAIサービスを活用できるようになりました。これにより、世界中のユーザーが最新のAIモデルを利用する機会が広がります。

4. **目次の更新**:
    - 目次の更新により、ドキュメント内での情報のナビゲーションが向上しました。特に、新しいGPT-4o miniモデルに関する情報が追加されたことで、ユーザーは最新の技術にアクセスしやすくなっています。

総じて、このアップデートはマイナーでありながら、ユーザーの体験を向上させるための重要な改善が含まれています。適切なリソース管理や最新の技術の導入を計画する際、これらの更新情報は不可欠です。Azure OpenAIサービスのドキュメントが常に最新かつ正確であることは、ユーザーの信頼性と利用効率を高めるために極めて重要です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルの退役日変更とアップグレード情報の更新 | modified | 13 | 8 | 21 | 
| [quota.md](#item-389aa1) | minor update | クォータ情報の更新 | modified | 4 | 4 | 8 | 
| [standard-embeddings.md](#item-656427) | minor update | ノルウェー東部のモデル情報の更新 | modified | 1 | 1 | 2 | 
| [standard-gpt-35-turbo.md](#item-a40035) | minor update | GPT-3.5 Turboモデルの利用状況の更新 | modified | 4 | 3 | 7 | 
| [standard-gpt-4.md](#item-d4064a) | minor update | GPT-4モデルのwestus3地域の情報更新 | modified | 1 | 1 | 2 | 
| [standard-models.md](#item-af04c4) | minor update | スタンダードモデルの可用性の更新 | modified | 5 | 5 | 10 | 
| [toc.yml](#item-c945af) | minor update | 目次の更新: GPT-4o miniの調整 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 09/03/2024
+ms.date: 09/09/2024
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -91,15 +91,15 @@ These models are currently available for use in Azure OpenAI Service.
 
 | Model | Version | Retirement date | Suggested replacements |
 | ---- | ---- | ---- | --- |
-| `gpt-35-turbo` | 0301 | No earlier than November 1, 2024<br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 15, 2024.   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
-| `gpt-35-turbo`<br>`gpt-35-turbo-16k` | 0613 | November 1, 2024 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 15, 2024.  | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
+| `gpt-35-turbo` | 0301 | January 27, 2025<br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 15, 2024.   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
+| `gpt-35-turbo`<br>`gpt-35-turbo-16k` | 0613 | January 27, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 15, 2024.  | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
 | `gpt-35-turbo` | 1106 | No earlier than Nov 17, 2024 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 15, 2024. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
 | `gpt-35-turbo` | 0125 | No earlier than Feb 22, 2025 | `gpt-4o-mini` |
-| `gpt-4`<br>`gpt-4-32k` | 0314 | **Deprecation:** November 15, 2024 <br> **Retirement:** June 6, 2025 | `gpt-4o` |
-| `gpt-4`<br>`gpt-4-32k` | 0613 | **Deprecation:** November 15, 2024 <br> **Retirement:** June 6, 2025 | `gpt-4o` |
-| `gpt-4` | 1106-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting on November 15, 2024, or later **<sup>1</sup>** | `gpt-4o`|
-| `gpt-4` | 0125-preview |To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting on November 15, 2024, or later  **<sup>1</sup>**  | `gpt-4o` |
-| `gpt-4` | vision-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting on November 15, 2024, or later  **<sup>1</sup>** | `gpt-4o`|
+| `gpt-4`<br>`gpt-4-32k` | 0314 | June 6, 2025 | `gpt-4o` |
+| `gpt-4`<br>`gpt-4-32k` | 0613 | June 6, 2025 | `gpt-4o` |
+| `gpt-4` | 1106-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025 **<sup>1</sup>** | `gpt-4o`|
+| `gpt-4` | 0125-preview |To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025 **<sup>1</sup>**  | `gpt-4o` |
+| `gpt-4` | vision-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025  **<sup>1</sup>** | `gpt-4o`|
 | `gpt-3.5-turbo-instruct` | 0914 | No earlier than Sep 14, 2025 |  |
 | `text-embedding-ada-002` | 2 | No earlier than April 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
 | `text-embedding-ada-002` | 1 | No earlier than April 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
@@ -158,6 +158,11 @@ If you're an existing customer looking for information about these models, see [
 
 ## Retirement and deprecation history
 
+## September 9, 2024
+
+* `gpt-35-turbo` (0301) and (0613) retirement changed to January 27, 2025.
+* `gpt-4` preview model upgrade date changed to starting no sooner than January 27, 2025.
+
 ## September 3, 2024
 
 * Updated tables to include information on `gpt-35-turbo` default version upgrades. Deployments of versions `0301`, `0613`, and `1106` set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 15, 2024.|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの退役日変更とアップグレード情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるモデルの退役日とアップグレードに関する情報を更新したものです。具体的には、`gpt-35-turbo`（0301および0613）の退役日が2025年1月27日に変更され、また`gpt-4`プレビュー版のアップグレード開始日も同様に2025年1月27日以降に修正されています。

変更に伴い15行の新規情報が追加され、8行が削除され、全体で21行が修正されました。これにより、ユーザーはモデルの使用計画やアップグレードのタイミングについて最新の情報を得ることができるようになります。変更の詳細は、関連する表や履歴に明示されており、文書の可読性が向上しています。このアップデートは、ユーザーが自分のデプロイメントに適切な対策を取れるよう支援します。

## articles/ai-services/openai/includes/model-matrix/quota.md{#item-389aa1}

<details>
<summary>Diff</summary>
````diff
@@ -15,22 +15,22 @@ ms.date: 09/09/2024
 | brazilsouth        | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | canadaeast         | 40 K    | 80 K        | 80 K          | -               | -        | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | eastus             | -       | -           | 80 K          | -               | 1 M      | 2 M           | 240 K          | 240 K                   | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 240 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| eastus2            | -       | -           | 80 K          | -               | 1 M      | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | 100 K               | -                        | -                  | -             | -                        | -             | -                        | 250 K                     | 250 K                          | 250 K                          |
+| eastus2            | -       | -           | 80 K          | -               | 1 M      | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | 250 K               | -                        | -                  | -             | -                        | -             | -                        | 250 K                     | 250 K                          | 250 K                          |
 | francecentral      | 20 K    | 60 K        | 80 K          | -               | -        | -             | 240 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | germanywestcentral | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | japaneast          | -       | -           | -             | 30 K            | -        | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | koreacentral       | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| northcentralus     | -       | -           | 80 K          | -               | 1 M      | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | 100 K               | 100 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
+| northcentralus     | -       | -           | 80 K          | -               | 1 M      | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
 | norwayeast         | -       | -           | 150 K         | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | polandcentral      | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | southafricanorth   | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | southcentralus     | -       | -           | 80 K          | -               | 1 M      | -             | 240 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | southindia         | -       | -           | 150 K         | -               | -        | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | spaincentral       | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| swedencentral      | 40 K    | 80 K        | 150 K         | 30 K            | 1 M      | 2 M           | 300 K          | 240 K                   | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | 350 K                    | 100 K               | 100 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
+| swedencentral      | 40 K    | 80 K        | 150 K         | 30 K            | 1 M      | 2 M           | 300 K          | 240 K                   | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | 350 K                    | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
 | switzerlandnorth   | 40 K    | 80 K        | -             | 30 K            | -        | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | switzerlandwest    | -       | -           | -             | -               | -        | -             | -              | -                       | -                         | -                              | -                              | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | 250 K                    | -             | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
 | uksouth            | -       | -           | 80 K          | -               | -        | -             | 240 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | westeurope         | -       | -           | -             | -               | -        | -             | 240 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | westus             | -       | -           | 80 K          | 30 K            | 1 M      | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| westus3            | -       | -           | 80 K          | -               | 1 M      | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| westus3            | -       | -           | 80 K          | -               | 1 M      | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータ情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスのクォータに関する情報を含む文書（`quota.md`）の更新です。この更新では、特定の地域におけるリソース利用の上限（クォータ）が修正されました。具体的には、`eastus2`、`northcentralus`、`swedencentral`などの地域において、いくつかのクォータ値が変更されています。

変更内容は、プラス4行とマイナス4行があり、合計で8行の変更が行われました。これにより、各地域の利用可能なリソースの最新の上限値が提供され、ユーザーが適切にリソースを管理できるようになります。変更された内容は、モデルの利用におけるクォータの設定を理解しやすくするもので、利用者にとって重要な情報となります。文書の全体が最新の状態に保たれることで、ユーザーが計画的にリソースを使用できるようにサポートしています。

## articles/ai-services/openai/includes/model-matrix/standard-embeddings.md{#item-656427}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ ms.date: 03/13/2024
 | francecentral    | -                             | ✅                              | -                             | ✅                              |
 | japaneast        | -                             | ✅                              | -                             | ✅                              |
 | northcentralus   | -                             | ✅                              | -                             | -                             |
-| norwayeast       | -                             | ✅                              | -                             | -                             |
+| norwayeast       | -                             | ✅                              | -                             | ✅                              |
 | southafricanorth | -                             | ✅                              | -                             | -                             |
 | southcentralus   | ✅                              | ✅                              | -                             | -                             |
 | southindia       | -                             | ✅                              | -                             | ✅                              |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ノルウェー東部のモデル情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおける「スタンダード埋め込み」に関する情報を含む文書（`standard-embeddings.md`）の更新です。具体的には、`norwayeast`地域におけるモデルの可用性に関する情報が更新されました。変更点として、以前は「-」表示されていた部分が「✅」に修正されています。

この更新により、`norwayeast`地域のモデルに有効な特性が明示され、ユーザーがその地域で利用可能なモデルについての理解が深まります。全体的に1行の追加と1行の削除があり、合計2行の変更が行われました。この情報は、ユーザーが標準埋め込み機能を利用する際に重要なものであり、最新の状況を反映した内容となっています。

## articles/ai-services/openai/includes/model-matrix/standard-gpt-35-turbo.md{#item-a40035}

<details>
<summary>Diff</summary>
````diff
@@ -12,8 +12,8 @@ ms.date: 03/13/2024
 |:-----------------|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:------------------------------:|:-----------------------------------:|
 | australiaeast    | -                      | ✅                       | ✅                       | -                      | ✅                           | -                               |
 | canadaeast       | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               |
-| eastus           | ✅                       | ✅                       | -                      | -                      | ✅                           | ✅                                |
-| eastus2          | -                      | ✅                       | -                      | -                      | ✅                           | -                               |
+| eastus           | ✅                       | ✅                       | -                      | ✅                       | ✅                           | ✅                                |
+| eastus2          | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               |
 | francecentral    | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               |
 | japaneast        | -                      | ✅                       | -                      | -                      | ✅                           | -                               |
 | northcentralus   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               |
@@ -23,4 +23,5 @@ ms.date: 03/13/2024
 | switzerlandnorth | -                      | ✅                       | -                      | -                      | ✅                           | -                               |
 | uksouth          | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               |
 | westeurope       | ✅                       | -                      | -                      | -                      | -                          | -                               |
-| westus           | -                      | -                      | ✅                       | -                      | -                          | -                               |
\ No newline at end of file
+| westus           | -                      | -                      | ✅                       | ✅                       | -                          | -                               |
+| westus3          | -                      | -                      | -                      | ✅                       | -                          | -                               |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-3.5 Turboモデルの利用状況の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「スタンダード GPT-3.5 Turbo」に関する情報を含む文書（`standard-gpt-35-turbo.md`）の更新です。変更された内容には、いくつかの地域におけるモデルの利用可能性に関する情報が含まれています。

具体的には、`eastus`と`eastus2`の地域でモデルの有効性が更新され、これにより両地域での利用状況がより明確になりました。変更は、4行の追加と3行の削除があり、合計7行の変更が行われました。これにより、ユーザーがGPT-3.5 Turboモデルを利用する際のリソースの状況が最新の情報に基づいて提供されます。

特に、`westus3`地域が新たに追加され、モデルのオプションが拡大されていることも重要なポイントです。この更新は、ユーザーが各地域で利用可能な機能についての理解を深め、計画的にリソースを使用できるようサポートします。

## articles/ai-services/openai/includes/model-matrix/standard-gpt-4.md{#item-d4064a}

<details>
<summary>Diff</summary>
````diff
@@ -24,4 +24,4 @@ ms.date: 09/03/2024
 | switzerlandnorth | ✅                | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    |
 | uksouth          | -               | ✅                        | ✅                        | -                         | -                           | -                      | -                      | -                           | -                   |
 | westus           | -               | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | -                           | -                   |
-| westus3          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   |
\ No newline at end of file
+| westus3          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4モデルのwestus3地域の情報更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「スタンダード GPT-4」に関する情報を含む文書（`standard-gpt-4.md`）の更新です。具体的には、`westus3`地域におけるモデル利用の可用性の情報が修正されています。

変更内容としては、1行の追加と1行の削除があり、合計2行の変更が行われました。この更新により、`westus3`地域でのモデルがどのように利用可能であるかが明確になりました。特に、利用可能なモデルに関する状態が最新のものに修正されており、ユーザーに対して正確な情報が提供されています。

この変更は、特に`westus3`地域のユーザーにとって、GPT-4モデルを効果的に利用するための重要な情報源となるでしょう。また、全体的な情報の整合性を保つためにも、継続的な更新が重要であることを示しています。

## articles/ai-services/openai/includes/model-matrix/standard-models.md{#item-af04c4}

<details>
<summary>Diff</summary>
````diff
@@ -14,8 +14,8 @@ ms.date: 09/03/2024
 | australiaeast    | ✅                | ✅                        | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | ✅                  | -                  | -                  | -            | -               | -                |
 | brazilsouth      | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
 | canadaeast       | ✅                | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| eastus           | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | ✅                       | ✅                       | -                      | -                      | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | ✅                  | -                  | -                  | -            | -               | -                |
-| eastus2          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| eastus           | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | ✅                  | -                  | -                  | -            | -               | -                |
+| eastus2          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | francecentral    | ✅                | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | ✅                    | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
 | japaneast        | -               | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | -                   | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
 | northcentralus   | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
@@ -24,8 +24,8 @@ ms.date: 09/03/2024
 | southcentralus   | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   | ✅                       | -                      | -                      | ✅                       | -                          | -                               | ✅                              | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
 | southindia       | -               | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | ✅                       | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | swedencentral    | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           | ✅                                | -                             | ✅                              | -                             | ✅                              | -                 | ✅                  | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
-| switzerlandnorth | ✅                | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
+| switzerlandnorth | ✅                | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | uksouth          | -               | ✅                        | ✅                        | -                         | -                           | -                      | -                      | -                           | -                   | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
 | westeurope       | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| westus           | -               | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | -                           | -                   | -                      | -                      | ✅                       | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
-| westus3          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| westus           | -               | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | -                           | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
+| westus3          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   | -                      | -                      | -                      | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スタンダードモデルの可用性の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスのスタンダードモデルに関する情報を含む文書（`standard-models.md`）の更新です。この更新では、特に各地域ごとのモデルの可用性に関する情報が修正されています。

具体的には、5行の追加と5行の削除が行われ、合計10行の変更があります。特に、`eastus`、`eastus2`、`westus`、および`westus3`地域に関するモデルの利用可能性が最新の情報に更新されました。これにより、ユーザーは各地域におけるモデルの状態をより正確に把握できるようになります。

この文書の更新は、ユーザーがAzure OpenAIサービスを利用する際に、正確で最新の情報を基にリソースを計画しやすくするための重要な手段となります。また、常に変化するサービス環境に対する整合性を保つ上でも、こうしたマイナーアップデートは非常に重要です。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -218,7 +218,7 @@ items:
   items:
     - name: Embeddings
       href: ./tutorials/embeddings.md
-    - name: Fine-tuning GPT-3.5-Turbo
+    - name: Fine-tuning GPT-4o mini
       href: ./tutorials/fine-tune.md
     - name: Speech to speech chat
       href: ../speech-service/openai-speech.md?context=%2fazure%2fcognitive-services%2fopenai%2fcontext%2fcontext
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新: GPT-4o miniの調整"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関する文書の目次（`toc.yml`）の更新です。具体的には、目次内で「Fine-tuning GPT-3.5-Turbo」に関する項目が「Fine-tuning GPT-4o mini」に変更されました。

この更新により、ユーザーは新しいモデルであるGPT-4o miniの調整に関する情報にアクセスしやすくなります。具体的には、1行が追加され、1行が削除され、合計2行の変更が行われました。この変更は、最新のモデルを反映し、利用可能なリソースを正確に示すため、ドキュメント全体の情報の整合性を保つ上で重要です。

新しい内容は、各種チュートリアルに関心のあるユーザーにとって、有用で関連性の高い情報を提供することを目的としています。また、最新の技術に基づいてユーザー体験を向上させるため、定期的なアップデートが促進されています。


