---
date: '2024-09-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:89cdcc6...MicrosoftDocs:e3ea9cd
summary: このコードの変更では、Azure GovernmentにおけるAzure OpenAIサービスに関するドキュメントが更新され、モデルの利用可能性、サポートされる地域、クォータ情報などが明確にされました。新たに追加された地域やモデルのバージョンが記載され、既存の日付やクォータ情報も最新のものに修正されています。また、モデルの利用可能性に関するセクションが新たに追加され、内容が整理されています。このアップデートにより、ユーザーはサービスを利用する際の具体的な判断をしやすくなります。全体として、これらの変更はAzure
  OpenAIサービスの利用における意思決定を支援し、効率的な利用を促進します。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:89cdcc6...MicrosoftDocs:e3ea9cd){target="_blank"}

# Highlights
このコードの変更では、Azure GovernmentにおけるAzure OpenAIサービスに関するドキュメントが複数の点で更新されています。次の5つの記事に対して、モデルの利用可能性、サポートされる地域、クォータ情報などの細部が明確にされています。

## 新機能
- **地域情報の更新**：新たに追加された地域やサポートされるモデルのバージョンが明記されました。
- **モデルバージョン追加**：gpt-4o-miniやgpt-4-32kなどの新しいモデル情報が追加。

## 変更点
- **日付の修正**：既存の日付が最新のものに更新されました。
- **クォータ情報の修正**：地域別のクォータに関する最新情報が反映されています。

## その他の更新
- **ドキュメントの再構成**：モデルの利用可能性に関するセクションが新たに追加され、内容が整理されています。

# Insights
この変更では、Azure Governmentと一般的なAzure OpenAIサービスの利用に関するドキュメントがアップデートされています。このアップデートは、次のような重要な点をカバーしています。

## Azure Governmentにおける更新
Azure Governmentを利用するユーザー向けには、特にビジネス継続性および災害復旧（BCDR）の観点から注意事項が追加されました。この変更により、Azure Governmentでのモデル利用に関する具体的なガイダンスが強化され、ユーザーは各地域やデプロイメントタイプに基づいた判断を行いやすくなっています。

## モデルのサポート地域
Azure OpenAIに関するモデルのサポート地域が新たに追加され、具体的な地域情報がより豊富になりました。例えば`eastus2`、`switzerlandnorth`、`westus`、`westus3`など複数の新しい地域がリストに加えられています。この更新により、ユーザーは自分がサービスを利用する予定の地域で具体的にどのモデルが利用可能かを正確に把握できるようになりました。

## クォータ情報の更新
クォータ情報に関する日付や値が最新のものに更新されました。特に`eastus2`、`japaneast`、`northcentralus`、`switzerlandnorth`、`westus`、`westus3`のクォータが新たに設定され、一部の地域では新しいクォータ値が追加されています。これにより、ユーザーは自身の利用ニーズに応じて最適な地域を選択しやすくなります。

## スタンダードモデルの情報
スタンダードモデルに関する情報も新しい日付とともに更新され、`gpt-4o-mini`、`gpt-4-32k`などのモデルバージョンが追加されました。この情報によって、ユーザーは各地域で利用可能なモデルのバージョンやサポートステータスを詳しく理解できるようになります。

全体として、このドキュメントの更新はAzure OpenAIサービスの利用に関するユーザーの意思決定を支援し、より効率的で効果的な利用を可能にするためのものであると言えます。特に新しい地域追加やクォータ情報の更新は、リソース管理と最適化において重要なステップとなります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-government.md](#item-a47549) | minor update | Azure GovernmentにおけるAzure OpenAIサービスの更新 | modified | 3 | 1 | 4 | 
| [models.md](#item-db2c37) | minor update | Azure OpenAIモデルのサポート地域の更新 | modified | 29 | 0 | 29 | 
| [quota.md](#item-389aa1) | minor update | Azure OpenAIモデルのクォータ情報の更新 | modified | 8 | 8 | 16 | 
| [standard-gpt-4.md](#item-d4064a) | minor update | Standard GPT-4モデルの地域情報の更新 | modified | 5 | 5 | 10 | 
| [standard-models.md](#item-af04c4) | minor update | スタンダードモデルの地域別情報の更新 | modified | 6 | 6 | 12 | 


# Modified Contents
## articles/ai-services/openai/azure-government.md{#item-a47549}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,9 @@ This article highlights the differences when using Azure OpenAI in Azure Governm
 
 ## Azure OpenAI models
 
-Learn more about the different capabilities of each model in [Azure OpenAI Service models](./concepts/models.md). The following sections show model availability by region and deployment type.
+Learn more about the different capabilities of each model in [Azure OpenAI Service models](./concepts/models.md). For customers with [Business Continuity and Disaster Recovery (BCDR) considerations](./how-to/business-continuity-disaster-recovery.md), please take careful note of the deployment types, regions, and model availability below as not all model/type combinations are available in both regions. 
+
+The following sections show model availability by region and deployment type.
 
 ### Standard deployment model availability
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure GovernmentにおけるAzure OpenAIサービスの更新"
}
```

### Explanation
この変更は、Azure GovernmentでのAzure OpenAIサービスに関する記事の軽微な更新を示しています。主な内容としては、モデルの利用可能性に関するセクションの文が追加され、特に「ビジネス継続性および災害復旧（BCDR）への配慮が必要な顧客」に向けての注意事項が強調されています。この更新により、地域やデプロイメントタイプにおけるモデルの利用可能性に関する情報がより明確に伝えられるようになりました。また、全体的な構成として、モデルの説明の後にモデルの利用可能性に関するセクションが再構成され、内容がより論理的に整理されています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -232,8 +232,37 @@ For more information on Provisioned deployments, see our [Provisioned guidance](
 **Supported regions:**
 
 - eastus
+- eastus2
+- northcentralus
 - swedencentral
+- switzerlandnorth
+- westus
+- westus3
 
+`gpt-4` **Version:** `turbo-2024-04-09`
+
+- australiaeast     
+- brazilsouth       
+- canadaeast        
+- eastus            
+- eastus2           
+- francecentral     
+- germanywestcentral
+- japaneast         
+- koreacentral      
+- northcentralus    
+- norwayeast        
+- polandcentral
+- spaincentral     
+- southafricanorth  
+- southcentralus    
+- southindia        
+- swedencentral     
+- switzerlandnorth  
+- uksouth           
+- westeurope        
+- westus            
+- westus3           
 
 ### Global batch model availability
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIモデルのサポート地域の更新"
}
```

### Explanation
この変更は、Azure OpenAIに関するモデルのサポート地域を更新したもので、記事に新しい地域が追加されました。具体的には、`eastus2`、`switzerlandnorth`、`westus`、`westus3`、およびその他の多くの地域がリストに加えられています。特に、`gpt-4`モデルのバージョンが`turbo-2024-04-09`として明記されており、利用可能な地域が詳細に列挙されています。この更新により、ユーザーは各地域におけるモデルの利用状況をより正確に把握できるようになり、Azure OpenAIサービスの利用を効果的に計画できるようになります。全体として、追加された情報は、読者に提供される背景知識を豊かにし、Azure OpenAIモデルの利用可能性を明確に示す役割を果たしています。

## articles/ai-services/openai/includes/model-matrix/quota.md{#item-389aa1}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Azure OpenAI model quota
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 09/09/2024
+ms.date: 09/22/2024
 ---
 
 
@@ -15,22 +15,22 @@ ms.date: 09/09/2024
 | brazilsouth        | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | canadaeast         | 40 K    | 80 K        | 80 K          | -               | -        | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | eastus             | -       | -           | 80 K          | -               | 1 M      | 2 M           | 240 K          | 240 K                   | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 240 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| eastus2            | -       | -           | 80 K          | -               | 1 M      | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | 250 K               | -                        | -                  | -             | -                        | -             | -                        | 250 K                     | 250 K                          | 250 K                          |
+| eastus2            | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | 250 K               | -                        | -                  | -             | -                        | -             | -                        | 250 K                     | 250 K                          | 250 K                          |
 | francecentral      | 20 K    | 60 K        | 80 K          | -               | -        | -             | 240 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | germanywestcentral | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| japaneast          | -       | -           | -             | 30 K            | -        | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| japaneast          | -       | -           | -             | 30 K            | -        | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | koreacentral       | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| northcentralus     | -       | -           | 80 K          | -               | 1 M      | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
+| northcentralus     | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
 | norwayeast         | -       | -           | 150 K         | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | polandcentral      | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | southafricanorth   | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | southcentralus     | -       | -           | 80 K          | -               | 1 M      | -             | 240 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | southindia         | -       | -           | 150 K         | -               | -        | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | spaincentral       | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | swedencentral      | 40 K    | 80 K        | 150 K         | 30 K            | 1 M      | 2 M           | 300 K          | 240 K                   | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | 350 K                    | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
-| switzerlandnorth   | 40 K    | 80 K        | -             | 30 K            | -        | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| switzerlandnorth   | 40 K    | 80 K        | -             | 30 K            | -        | -             | 300 K          | -                       | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | switzerlandwest    | -       | -           | -             | -               | -        | -             | -              | -                       | -                         | -                              | -                              | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | 250 K                    | -             | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
 | uksouth            | -       | -           | 80 K          | -               | -        | -             | 240 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| westeurope         | -       | -           | -             | -               | -        | -             | 240 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| westus             | -       | -           | 80 K          | 30 K            | 1 M      | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| westus3            | -       | -           | 80 K          | -               | 1 M      | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
\ No newline at end of file
+| westeurope         | -       | -           | -             | -               | -        | -             | 240 K          | -                       | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| westus             | -       | -           | 80 K          | 30 K            | 1 M      | 2 M           | 300 K          | -                       | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| westus3            | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIモデルのクォータ情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIモデルのクォータ情報を含むドキュメントにおける軽微な更新を示しています。具体的には、ファイル内の日付が`09/09/2024`から`09/22/2024`に変更され、様々な地域におけるモデルのクォータの値が修正されました。特に、`eastus2`、`japaneast`、`northcentralus`、`switzerlandnorth`、`westus`、および`westus3`に関するクォータが更新され、いくつかのモデルに対する新しいクォータが追加されています。

この更新により、各地域の利用可能なリソースの制約がさらに明確になり、ユーザーは自分のニーズに合った地域を選択しやすくなります。また、初期のクォータや制約に関するより正確な情報が提供され、利用者が各地域でのリソース管理を最適化できるようになっています。全体として、この修正は、Azure OpenAIサービスの利用に関する理解を深め、より適切な選択を行えるようにするための重要な情報提供を目的としています。

## articles/ai-services/openai/includes/model-matrix/standard-gpt-4.md{#item-d4064a}

<details>
<summary>Diff</summary>
````diff
@@ -5,23 +5,23 @@ description: Standard GPT-4 model availability
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 09/03/2024
+ms.date: 09/22/2024
 ---
 
 | **Region**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **vision-preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4-32k**, **0613**   |
 |:-----------------|:-------------------:|:---------------------------:|:---------------------------:|:-----------------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-----------------------:|
 | australiaeast    | ✅                | ✅                        | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    |
 | canadaeast       | ✅                | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | ✅                    |
 | eastus           | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   |
-| eastus2          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   |
+| eastus2          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   |
 | francecentral    | ✅                | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | ✅                    |
 | japaneast        | -               | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | -                   |
-| northcentralus   | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   |
+| northcentralus   | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   |
 | norwayeast       | -               | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | -                   |
 | southcentralus   | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   |
 | southindia       | -               | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | -                   |
 | swedencentral    | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    |
 | switzerlandnorth | ✅                | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    |
 | uksouth          | -               | ✅                        | ✅                        | -                         | -                           | -                      | -                      | -                           | -                   |
-| westus           | -               | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | -                           | -                   |
-| westus3          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   |
+| westus           | -               | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | ✅                            | -                   |
+| westus3          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Standard GPT-4モデルの地域情報の更新"
}
```

### Explanation
この変更は、Standard GPT-4モデルの地域に関する情報を更新したもので、2つの日付が新しいものに変更されています。この変更により、モデルの利用可能性に関する各地域のサポート状況が反映されています。特に、`eastus2`、`northcentralus`、`westus`、および`westus3`の各地域におけるモデルのサポート状況が更新され、使用可能なバージョンが追加されています。

具体的には、`gpt-4o-mini`, `gpt-4-32k`およびそのバージョンに関する情報が新たに表示され、これにより、開発者やユーザーが地域ごとのモデルの利用可能性をより良く理解できるようになります。 その結果、この更新により、Azure OpenAIサービスを利用する際の地域選択において、ユーザーにとっての利便性が向上します。全体として、この修正は、ユーザーがモデルを選択する際の情報をより詳細に提供し、効果的な意思決定を支援することを目的としています。

## articles/ai-services/openai/includes/model-matrix/standard-models.md{#item-af04c4}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Quota and limits for Azure OpenAI by region.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 09/03/2024
+ms.date: 09/22/2024
 ---
 
 
@@ -15,10 +15,10 @@ ms.date: 09/03/2024
 | brazilsouth      | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
 | canadaeast       | ✅                | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
 | eastus           | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | ✅                  | -                  | -                  | -            | -               | -                |
-| eastus2          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| eastus2          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | francecentral    | ✅                | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | ✅                    | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| japaneast        | -               | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | -                   | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| northcentralus   | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
+| japaneast        | -               | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | -                   | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| northcentralus   | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
 | norwayeast       | -               | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | southafricanorth | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
 | southcentralus   | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   | ✅                       | -                      | -                      | ✅                       | -                          | -                               | ✅                              | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
@@ -27,5 +27,5 @@ ms.date: 09/03/2024
 | switzerlandnorth | ✅                | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | uksouth          | -               | ✅                        | ✅                        | -                         | -                           | -                      | -                      | -                           | -                   | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
 | westeurope       | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| westus           | -               | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | -                           | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
-| westus3          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   | -                      | -                      | -                      | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
\ No newline at end of file
+| westus           | -               | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
+| westus3          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スタンダードモデルの地域別情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスのスタンダードモデルに関する地域別の情報を更新したものです。具体的には、ドキュメントの日付が`09/03/2024`から`09/22/2024`に変更され、各地域におけるモデルの利用可能性が正式に反映されています。特に、`eastus2`、`japaneast`、`northcentralus`、`westus`、および`westus3`の情報が更新され、以前のバージョンに対するサポートが強化されました。

この更新では、一部の地域で利用可能なモデルに新しいフラグが追加され、各地域でのモデル利用の可否が明示されています。この情報により、開発者やユーザーは自身のニーズに合わせて選択する際に、モデルやバージョンのサポート状況をより良く理解することができます。全体として、この修正は、Azure OpenAIサービスの利用をより円滑にし、ユーザーが必要としている情報を提供するための重要なステップとなっています。


