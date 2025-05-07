---
date: '2025-05-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2280088...MicrosoftDocs:768f68b
summary: この変更は、AIサービスに関する地域とモデルの対応状況を示すドキュメントの更新です。新たに「italynorth」地域が追加され、全モデルが利用可能とされ、他にも「australiaeast」や「brazilsouth」など、複数の地域でモデルの利用可能性が明示されました。破壊的変更は特にありませんが、地域利用可能性の変更により過去の利用状況に影響を与える可能性があります。この更新により、ユーザーはAIモデルの可用性をより正確に把握できるようになり、サービスの展開やサポート地域の拡大に寄与します。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2280088...MicrosoftDocs:768f68b){target="_blank"}

<format>
# Highlights
この変更では、AIサービスに関する地域とモデルの対応状況を示すドキュメントが更新されました。具体的には、データゾーンとプロビジョニングされたグローバルモデルマトリックスの情報が修正され、多くの地域においてモデルの利用可能性が明示されました。

## New features
- `italynorth` 地域が追加され、全モデルに対して利用可能と記載。
- 多くの新たな地域（例：`australiaeast`、`brazilsouth` など）がモデル利用可能として追加。

## Breaking changes
特に明示的な破壊的変更はありませんが、地域利用可能性のステータスが変更されたことで、過去の利用状況に変更が生じる可能性があります。

## Other updates
- 既存の地域（例：`francecentral`、`germanywestcentral`）のモデル利用可能性の修正。
- 日付の更新が行われ、情報が最新の日付に修正。

# Insights
ドキュメントのこのマイナーアップデートにより、AIサービスの利用可能な地域が明確化され、ユーザーに提供される情報が最新かつ正確になりました。IT管理者や開発者にとって、地域でのAIモデルの可用性を把握することは重要であり、この情報の正確な提供は運用に不可欠です。

このようなドキュメントの更新は、迅速なサービス展開やサポート地域の拡大に対応するためのものであり、特に新たに追加された地域では、ユーザーがサービスをより広範囲で活用できるようになることが期待されています。また、地域ごとのモデルの利用可能性に関する情報の正確性が向上することで、より戦略的な意思決定が可能となるでしょう。

</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [datazone-provisioned-managed.md](#item-ae7f5b) | minor update | データゾーンでのモデルマトリックスの更新 | modified | 9 | 8 | 17 | 
| [provisioned-global.md](#item-340884) | minor update | プロビジョニングされたグローバルモデルマトリックスの更新 | modified | 17 | 17 | 34 | 


# Modified Contents
## articles/ai-services/openai/includes/model-matrix/datazone-provisioned-managed.md{#item-ae7f5b}

<details>
<summary>Diff</summary>
````diff
@@ -6,20 +6,21 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 03/31/2025
+ms.date: 05/05/2025
 ---
 
 | **Region**     | **gpt-4.1**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
 |:-------------------|:---------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
 | eastus             | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | eastus2            | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| francecentral      | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| italynorth         | ✅                        | -                       | -                  | -                      | -                      | -                      | -                           |
 | northcentralus     | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| polandcentral      | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | southcentralus     | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| spaincentral       | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westeurope         | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | westus             | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
+| westus3            | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データゾーンでのモデルマトリックスの更新"
}
```

### Explanation
この変更は、指定されたファイル `datazone-provisioned-managed.md` において、いくつかの情報を更新し、特にAIサービスに関する地域とモデルの対応を示すセクションが修正されています。具体的には、以下の点が変更されました。

1. **日付の更新**: `ms.date` フィールドが「03/31/2025」から「05/05/2025」へ変更されました。
2. **地域情報の修正**: 
   - `francecentral` と `germanywestcentral` が最初は「-」と示されていましたが、更新後は全てのモデルに対して ✅ と表示され、利用可能であることが明示されました。
   - 新たに `italynorth` 地域が追加され、全てのモデルに対して未対応（−）から利用可能（✅）に変更されています。
   - `polandcentral`、`spaincentral`、`swedencentral`、および `westeurope` の各地域についても、同様に表示が更新されています。

これにより、地域における各モデルの対応状況がより正確に反映され、ユーザーにとっての情報価値が向上することが期待されます。この変更は、主に情報の整合性を持たせるためのマイナーアップデートと捉えられます。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -6,34 +6,34 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 05/01/2025
+ms.date: 05/05/2025
 ---
 
 | **Region**     | **gpt-4.1**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
 |:-------------------|:---------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
-| australiaeast      | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| brazilsouth        | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| canadaeast         | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| australiaeast      | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| brazilsouth        | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| canadaeast         | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | eastus             | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | eastus2            | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | francecentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | germanywestcentral | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | italynorth         | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| japaneast          | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| koreacentral       | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| japaneast          | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| koreacentral       | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | northcentralus     | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| norwayeast         | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| norwayeast         | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | polandcentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southafricanorth   | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southcentralus     | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southeastasia      | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southindia         | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southafricanorth   | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southeastasia      | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southindia         | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | spaincentral       | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | swedencentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandnorth   | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandwest    | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| uaenorth           | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| uksouth            | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandnorth   | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandwest    | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| uaenorth           | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| uksouth            | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | westeurope         | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus             | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus3            | -                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
+| westus             | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされたグローバルモデルマトリックスの更新"
}
```

### Explanation
この変更は、`provisioned-global.md` において、AIサービスのモデルに関連する情報を更新したものです。この変更点の概要は以下の通りです。

1. **日付の更新**: `ms.date` フィールドが「05/01/2025」から「05/05/2025」に変更されました。
2. **追加された地域情報**:
   - 多くの地域（例：`australiaeast`、`brazilsouth`、`canadaeast` など）が、モデルの利用可能性を示す行に新たに ✅ として追加され、従来の「-」から利用可能であることを示す状態に変更されています。
   - 特に、`japaneast` や `koreacentral` などの地域も利用可能から利用不可の表示に修正され、これによりユーザーがこれらの地域で利用できるモデルの範囲が広がりました。
   - 他にも、`norwayeast`、`southafricanorth`、`southcentralus`、`southeastasia`、`southindia` などの地域が新たに追加または修正され、全体的なカバレッジが強化されています。

この変更は、AIモデルの地域ごとの対応状況を明確にし、ユーザーが利用可能なサービスを理解しやすくするための小規模な更新です。全体として、ユーザーにとっての情報の正確性と利用価値が向上することが期待されます。


