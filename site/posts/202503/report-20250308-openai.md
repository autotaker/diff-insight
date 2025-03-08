---
date: '2025-03-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4d90f76...MicrosoftDocs:c05f6ab
summary: 今回のコード差分は、Azure OpenAIサービスに関する文書の更新であり、モデル情報の整理、アクセス要件の変更、サブスクリプション情報の修正が主な内容です。これにより文書の可読性と情報の明確性が向上しました。特に、`o1`および`o3-mini`モデルへのアクセス制限が解除され、`o1-preview`モデルに関する情報が追加されました。MSDNサブスクリプションの名称変更により、新たにGPT-4oリアルタイムプレビューへのアクセスが可能になっています。大きな破壊的変更はなく、文書の発行日が更新されるとともに、ユーザーが混乱しにくいよう整合性が図られています。この変更は、Azure
  OpenAIサービスを利用する企業や開発者にとって、利用効率と理解促進につながるでしょう。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4d90f76...MicrosoftDocs:c05f6ab){target="_blank"}

# Highlights
今回のコード差分は、Azure OpenAIサービスに関する文書の更新に関するものです。主にモデル情報の整理、アクセス要件の変更、そしてサブスクリプション情報の修正が含まれています。これらの修正により、ユーザーにとっての文書の可読性と情報の明確性が向上しました。

## New features
- `o1`および`o3-mini`モデルへのアクセス制限の解除。
- `o1-preview`モデルに関する情報の追加。
- MSDNサブスクリプションの名称が「MSDN & Cloud Solution Provider (CSP) subscriptions」に変更され、GPT-4oリアルタイムプレビューへのアクセスが追加。

## Breaking changes
- 特に大きな仕様の変更や破壊的変更は含まれていない。

## Other updates
- モデルの説明や情報に冗長な空白行の削除。
- 文書の発行日を更新し、最新の情報が反映されるように。
- 各モデルのID、説明、最大リクエスト数、トレーニングデータの年月が明確に記載。

# Insights
今回の変更は、Azure OpenAIサービスの利用者が、より簡単に必要な情報にアクセスできるようにすることを目的として行われています。具体的には、モデル情報の整理やアクセス要件の明示化に加えて、ユーザーが混乱しにくいように日本語ドキュメントの整合性が図られました。

文書の発行日が2025年3月7日に更新され、新たなアクセスポリシーが提示されることで、利用者はサービスの利用可能性について最新のインサイトを持つことができます。また、MSDNサブスクリプションの情報が明示化されることで、企業ユーザーが利用可能なサブスクリプションに関する理解が深まるでしょう。これは特に、MSDN & CSP利用者が新しくGPT-4oプレビューへのアクセスが可能となったことで利用範囲が拡大し、選択肢の幅が広がったことを意味します。

総じて、この文書の更新は、Azure OpenAIサービスを導入している企業や開発者にとって、サービス利用の効率化と理解促進につながるものとなっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | モデルの更新と空白の削除 | modified | 6 | 12 | 18 | 
| [reasoning.md](#item-a54b2f) | minor update | モデルのアクセス要件の更新 | modified | 3 | 9 | 12 | 
| [quotas-limits.md](#item-06c6f9) | minor update | MSDNサブスクリプションの情報の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -60,19 +60,13 @@ The Azure OpenAI o<sup>&#42;</sup> series models are specifically designed to ta
 
 |  Model ID  | Description | Max Request (tokens) | Training Data (up to)  |
 |  --- |  :--- |:--- |:---: |
-| `o3-mini` (2025-01-31) | The latest reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text-only processing <br> - Functions/Tools <br> <br> **Request access: [limited access model application](https://aka.ms/OAI/o1access)** | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
-| `o1` (2024-12-17) | The most capable model in the o1 series, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools <br> <br> **Request access: [limited access model application](https://aka.ms/OAI/o1access)** | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
+| `o3-mini` (2025-01-31) | The latest reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text-only processing <br> - Functions/Tools  | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
+| `o1` (2024-12-17) | The most capable model in the o1 series, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
 |`o1-preview` (2024-09-12) | Older preview version | Input: 128,000  <br> Output: 32,768 | Oct 2023 |
 | `o1-mini` (2024-09-12) | A faster and more cost-efficient option in the o1 series, ideal for coding tasks requiring speed and lower resource consumption. <br><br> Global standard deployment available by default. <br> <br> Standard (regional) deployments are currently only available for select customers who received access as part of the `o1-preview` limited access release.  | Input: 128,000  <br> Output: 65,536 | Oct 2023 |
 
 ### Availability
 
-**For access to `o3-mini` and `o1` registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who previously applied and received access to `o1-preview`, or `o1`  don't need to reapply as they are automatically on the wait-list for the latest models in the o-series.
-
-Request access: [limited access model application](https://aka.ms/OAI/o1access)
-
-Once access has been granted, you will need to create a deployment for each model. 
-
 To learn more about the advanced `o-series` models see, [getting started with reasoning models](../how-to/reasoning.md).
 
 ### Region availability
@@ -251,7 +245,7 @@ All deployments can perform the exact same inference operations, however the bil
 [!INCLUDE [Standard Global](../includes/model-matrix/standard-global.md)]
 
 > [!NOTE]
-> **Most o-series models are limited access**. Request access: [limited access model application](https://aka.ms/OAI/o1access). `o1-mini` is currently available to all customers for global standard deployment.
+> `o1-mini` is currently available to all customers for global standard deployment.
 >
 > Select customers were granted standard (regional) deployment access to `o1-mini` as part of the `o1-preview` limited access release. At this time access to `o1-mini` standard (regional) deployments is not being expanded.
 
@@ -274,7 +268,7 @@ All deployments can perform the exact same inference operations, however the bil
 [!INCLUDE [Data zone standard](../includes/model-matrix/datazone-standard.md)]
 
 > [!NOTE]
-> **Most o-series models are limited access**. Request access: [limited access model application](https://aka.ms/OAI/o1access). `o1-mini` is currently available to all customers for global standard deployment.
+> `o1-mini` is currently available to all customers for global standard deployment.
 >
 > Select customers were granted standard (regional) deployment access to `o1-mini` as part of the `o1-preview` limited access release. At this time access to `o1-mini` standard (regional) deployments is not being expanded.
 
@@ -297,7 +291,7 @@ All deployments can perform the exact same inference operations, however the bil
 [!INCLUDE [Standard Models](../includes/model-matrix/standard-models.md)]
 
 > [!NOTE]
-> **Most o-series models are limited access**. Request access: [limited access model application](https://aka.ms/OAI/o1access). `o1-mini` is currently available to all customers for global standard deployment.
+> `o1-mini` is currently available to all customers for global standard deployment.
 >
 > Select customers were granted standard (regional) deployment access to `o1-mini` as part of the `o1-preview` limited access release. At this time access to `o1-mini` standard (regional) deployments is not being expanded.
 
@@ -326,7 +320,7 @@ This table doesn't include fine-tuning regional availability information.  Consu
 [!INCLUDE [Chat Completions](../includes/model-matrix/standard-chat-completions.md)]
 
 > [!NOTE]
-> **Most o-series models are limited access**. Request access: [limited access model application](https://aka.ms/OAI/o1access). `o1-mini` is currently available to all customers for global standard deployment.
+> `o1-mini` is currently available to all customers for global standard deployment.
 >
 > Select customers were granted standard (regional) deployment access to `o1-mini` as part of the `o1-preview` limited access release. At this time access to `o1-mini` standard (regional) deployments is not being expanded.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの更新と空白の削除"
}
```

### Explanation
この変更は、Azure OpenAIのモデルに関する文書において、内容の更新および冗長な空白行の削除を行ったものです。具体的には、モデルの説明に関する情報を整然と並べ、理解しやすい形式に修正しました。新たに、情報が追加された行では、モデルのIDや説明、最大リクエスト数、トレーニングデータの年月が明確に示されており、全体的な構造はより一貫性を持つように整理されています。また、モデルに関するアクセス条件の説明は簡素化され、無駄な空白行が削除されました。これにより、文書の可読性が向上し、ユーザーが必要な情報により早くアクセスできるようになっています。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's advanced o3-mini, o1, & o1-mini rea
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 02/19/2025
+ms.date: 03/07/2025
 author: mrbullwinkle    
 ms.author: mbullwin
 ---
@@ -24,18 +24,12 @@ Azure OpenAI `o-series` models are designed to tackle reasoning and problem-solv
 
 ## Availability
 
- **For access to `o3-mini`, `o1`, and `o1-preview`, registration is required, and access will be granted based on Microsoft's eligibility criteria**.
-
- Customers who previously applied and received access to `o1` or `o1-preview`, don't need to reapply as they are automatically on the wait-list for the latest model.
-
-Request access: [limited access model application](https://aka.ms/OAI/o1access)
-
 ### Region availability
 
 | Model | Region | Limited access |
 |---|---|---|
-| `o3-mini` | [Model availability](../concepts/models.md#global-standard-model-availability).  | [Limited access model application](https://aka.ms/OAI/o1access) |
-|`o1` | [Model availability](../concepts/models.md#global-standard-model-availability).  | [Limited access model application](https://aka.ms/OAI/o1access) |
+| `o3-mini` | [Model availability](../concepts/models.md#global-standard-model-availability).  | Access is no longer restricted for this model.   |
+|`o1` | [Model availability](../concepts/models.md#global-standard-model-availability).  | Access is no longer restricted for this model.  |
 | `o1-preview` | [Model availability](../concepts/models.md#global-standard-model-availability). |This model is only available for customers who were granted access as part of the original limited access release. We're currently not expanding access to `o1-preview`. |
 | `o1-mini` | [Model availability](../concepts/models.md#global-standard-model-availability). | No access request needed for Global Standard deployments.<br><br>Standard (regional) deployments are currently only available to select customers who were previously granted access as part of the `o1-preview` release.|
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのアクセス要件の更新"
}
```

### Explanation
この修正は、Azure OpenAIの「推論」文書におけるモデルのアクセスに関する重要な情報を更新しました。具体的には、`o3-mini`および`o1`モデルへのアクセス要件が変更され、これらのモデルはもはや制限がなくなったことが明記されました。さらに、`o1-preview`に関する情報も更新され、限定的にアクセスが許可された顧客のみが利用できる旨が示されています。この更新により、ユーザーは新しいアクセスポリシーを理解しやすくなり、特定のモデルに対するアクセスに関する重要な情報が強調されています。また、文書の発行日も2025年3月7日に更新されており、最新の情報が反映されています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -195,7 +195,7 @@ If your Azure subscription is linked to certain [offer types](https://azure.micr
 |Tier| Quota Limit in tokens per minute (TPM) |
 |---|:---|
 |Azure for Students, Free Trials | 1 K (all models) <br>Exception o-series & GPT 4.5 Preview: 0|
-| MSDN subscriptions | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br> o-series: 0 <br> GPT 4.5 Preview: 0  |
+| MSDN & Cloud Solution Provider (CSP) subscriptions | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br> gpt-4o-realtime-preview: 1 K <br> o-series: 0 <br> GPT 4.5 Preview: 0  |
 | Monthly credit card based subscriptions <sup>1</sup> | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br> o-series: 0 <br> GPT 4.5 Preview: 0   |
 
 <sup>1</sup> This currently applies to [offer type 0003P](https://azure.microsoft.com/support/legal/offer-details/)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MSDNサブスクリプションの情報の修正"
}
```

### Explanation
この変更は、Azure OpenAIの「クォータと制限」に関するドキュメントにおけるMSDNサブスクリプションの情報を更新しました。具体的には、MSDNサブスクリプションの名称が「MSDN subscriptions」から「MSDN & Cloud Solution Provider (CSP) subscriptions」に変更され、これに伴い、GPT-4oリアルタイムプレビューへのアクセスが追加されました。この変更は、ユーザーが利用可能なサブスクリプションの種類をより明確に理解できるようにするためのものです。また、トークンの制限が詳細に記載されており、各モデルに対するクォータが一目で分かるようになっています。全体として、この更新はドキュメントの正確性と明瞭さを向上させています。


