---
date: '2024-12-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e69b8c6...MicrosoftDocs:a7b86da
summary: この差分では、Azure Government向けのOpenAIサービスに関するドキュメンテーションが更新され、新しいモデルの可用性やトークン毎分の標準クオータ制限に関する情報が追加されました。サービスの定義が改善され、エンドユーザーにとってよりわかりやすくなっています。主な目的は、政府関連機関やコンプライアンス重視のユーザーへの情報の精確性と透明性を向上させることです。これにより、ユーザーは適切なモデルやサービスプランを選択しやすくなり、Azure
  Governmentの利用がスムーズになります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e69b8c6...MicrosoftDocs:a7b86da){target="_blank"}

# ハイライト
この差分では、Azure Government向けのOpenAIサービスの可用性に関するドキュメンテーションの更新が行われました。新しいモデルの可用性に関する情報が追加され、様々な地域での違いや、トークン毎分(TPM)の標準クオータ制限についての情報が詳細に記載されています。また、サービスの定義が改善され、エンドユーザーにとってよりわかりやすく、利用しやすくなっています。

## 新機能
- 地域ごとのOpenAIモデルの可用性情報の追加。
- トークン毎分の標準クオータ制限の明示。

## 重大な変更
- 特に大きな破壊的変更はありませんが、情報の更新によりエンドユーザーの理解度が向上しています。

## その他の更新
- 日付情報の更新。
- MSサービスの定義の改善。

# インサイト
この更新は、主にAzure GovernmentでのOpenAIサービスの利用に関する情報の精確性と透明性を向上させる目的で行われました。政府関連の機関や、コンプライアンスが重要視される業界のユーザーに対して、最新のモデルを使用する際の地域的な制限や、トークンの利用制限に関する詳細な情報が提供されることで、サービス利用の計画が立てやすくなります。

特に、可用性とクオータ制限に関する情報が強化されたことにより、利用者は自身のニーズに最も適したモデルやサービスプランを選択する上で、より良い判断材料を持つことが可能になります。これにより、Azure Governmentを使用する際の意思決定が円滑に行える点で、ユーザーエクスペリエンスに大きな貢献をしています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-government.md](#item-a47549) | minor update | Azure Government OpenAI Service Availability Update | modified | 17 | 13 | 30 | 


# Modified Contents
## articles/ai-services/openai/azure-government.md{#item-a47549}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: challenp
 ms.service: azure-ai-openai
 ms.topic: how-to
 ms.custom: references_regions, azuregovernment
-ms.date: 8/29/2024
+ms.date: 12/11/2024
 recommendations: false
 ---
 
@@ -22,21 +22,25 @@ Learn more about the different capabilities of each model in [Azure OpenAI Servi
 The following sections show model availability by region and deployment type.
 
 ### Standard deployment model availability
-
-|   **Region**  | **gpt-35-turbo**, **1106** | **gpt-35-turbo**, **0125** | **gpt-4**, **1106-Preview** | **gpt-4o**, **2024-05-13** | **text-embedding-ada-002** |
-|:--------------|:--------------------------:|:--------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|
-| usgovarizona  | - | ✅ | ✅ | ✅ | ✅ |
-| usgovvirginia | ✅ | ✅ | ✅ | - | ✅ |
-
-To request quota increases for the pay-as-you-go consumption model, apply at [https://aka.ms/AOAIGovQuota](https://aka.ms/AOAIGovQuota)
+|   **Region**  | **gpt-4o**, **2024-05-13** | **gpt-4o-mini**, **2024-07-18** | **gpt-4**, **1106-Preview** | **gpt-35-turbo**, **0125** | **gpt-35-turbo**, **1106** | **text-embedding-3-large**, **1** | **text-embedding-ada-002**, **2** |
+|:--------------|:--------------------------:|:-------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:---------------------------------:|:---------------------------------:|
+| usgovarizona  | ✅ | ✅ | ✅ | ✅ | -  | ✅ | ✅ |
+| usgovvirginia | ✅ | -  | ✅ | ✅ | ✅ |  - | ✅ |
+ 
+#### Standard quota limits in tokens per minute (TPM): 
+| **gpt-4o** | **gpt-4o-mini** | **gpt-4** | **gpt-35-turbo** | **text-embedding-3-large** | **text-embedding-ada-002**|
+|:----------:|:---------------:|:---------:|:----------------:|:--------------------------:|:-------------------------:|
+|    300k    |      600k       |    200k   |      500k        |            700k            |           600k            |
+
+To request quota increases up to these maximum values, submit a request at [https://aka.ms/AOAIGovQuota](https://aka.ms/AOAIGovQuota).
 
 ### Provisioned deployment model availability
-|   **Region**  | **gpt-35-turbo**, **1106** | **gpt-35-turbo**, **0125** | **gpt-4**, **1106-Preview** | **gpt-4o**, **2024-05-13** |
-|:--------------|:--------------------------:|:--------------------------:|:---------------------------:|:--------------------------:|
-| usgovarizona  | - | ✅ | - | ✅ |
-| usgovvirginia | - | ✅ | ✅ | ✅ |
+|   **Region**  | **gpt-4o**, **2024-05-13** | **gpt-4o-mini**, **2024-07-18** | **gpt-4**, **1106-Preview** | **gpt-35-turbo**, **0125** | **gpt-35-turbo**, **1106** |
+|:--------------|:--------------------------:|:-------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|
+| usgovarizona  | ✅ | - | - | ✅ | - |
+| usgovvirginia | ✅ | - | - | ✅ | - |
 
-> [!NOTE]
+[NOTE]
 > Provisioned Throughput Units (PTUs) are different from standard quota in Azure OpenAI and are not available by default in Azure Government. To learn more about this offering contact your Microsoft Account Team.
 
 <br>
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Government OpenAI Service Availability Update"
}
```

### Explanation
このコードの変更は、Azure Government用のOpenAIサービスに関するドキュメントの更新を反映しています。具体的には、モデルの可用性に関する情報が追加され、既存のテーブルが更新されています。新しいテーブルには、地域ごとの異なるモデルの可用性、トークン毎分の標準クオータ制限、およびリクエストリンクが含まれています。また、日付情報が更新され、MSサービスの定義も改善されています。この変更により、エンドユーザーはAzure GovernmentにおけるOpenAIサービスの最新のモデル情報と利用可能性を把握することができます。


