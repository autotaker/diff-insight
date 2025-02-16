---
date: '2025-02-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b07793e...MicrosoftDocs:1cff62f
summary: このコード変更は、Azure OpenAIサービスの文書全般にわたる小規模な更新で、以下の重要な更新が含まれています。新しいモデルバージョン「gpt-4o」の追加や、`o3-mini`モデルのバッチ制限とサポート地域の追加が行われました。特に破壊的変更はないものの、用語とフローの明確化が行われています。また、虐待モニタリングプロセスの説明、モデル退役と非推奨に関する用語の整理、モデルデプロイメントパターンの更新、全体的なクォータと制限に関する情報がアップデートされました。この変更はユーザーの理解を深め、サービスの利用しやすさを高めることを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b07793e...MicrosoftDocs:1cff62f){target="_blank"}

# ハイライト

このコード変更は、Azure OpenAIサービスの文書全般にわたる小規模な更新で、以下の重要な更新が含まれています。

## 新機能

- `gpt-4o`モデルの新しいバージョン「2024-11-20」の追加
- `o3-mini`モデルのバッチ制限とサポート地域の追加

## 破壊的変更

- 特に破壊的変更はないが、いくつかの用語とフローの明確化が行われている。

## その他の更新

- 虐待モニタリングプロセスの説明の明確化
- モデル退役と非推奨に関する用語の定義部分の整理
- モデルデプロイメントパターンとアクセスリクエスト要件の更新および明確化
- 全体的なクォータと制限に関する情報の更新

# 洞察

この一連の変更は、Azure OpenAIサービスのユーザーがより効率的に情報を利用できるようにするためのものであり、文書の明確化と情報の最新化が主な目的です。比較的マイナーな更新として分類されていますが、ユーザーエクスペリエンスの向上に寄与する細かな改善が含まれています。

文書更新において最も注目すべき点は、新しいモデルバージョンやバッチ制限、そして地理的な利用可能性についての詳細情報が追加されていることです。特に、`o3-mini`と`gpt-4o`モデルに関する追加情報は、ユーザーがこれらのモデルを最新の状態で適切に利用できるための重要な指針となっています。

また、「虐待モニタリング」や「モデルの退役」に関する文書の明確化によって、サービスを利用する際のユーザーの理解をより高め、間違いや不安を軽減することが期待されます。例えば、モデルの退役と非推奨用語の区別は、将来のモデル使用計画を立てるユーザーにとって不可欠な情報です。

さらに、全体的なクォータと制限における説明の更新は、特に新しいサブスクリプションモデルを利用する際のガイドとして有用といえるでしょう。特に、学生向けや試用版向けプランにおける利用制限の明確さは、各モデルの試用から実運用へのスムーズな移行を支援します。

全体として、この更新はAzure OpenAIサービスにおけるユーザーの利便性向上を目的としたものであり、多様なユーザー層に対して適切な情報を提供することにより、サービスの利用しやすさを高めることを意図しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [abuse-monitoring.md](#item-b7afcb) | minor update | 虐待モニタリングの更新 | modified | 5 | 5 | 10 | 
| [model-retirements.md](#item-03fc2e) | minor update | モデルの退役に関する用語の修正 | modified | 2 | 2 | 4 | 
| [models.md](#item-db2c37) | minor update | モデル情報の更新 | modified | 6 | 7 | 13 | 
| [reasoning.md](#item-a54b2f) | minor update | アクセスリクエスト要件の更新 | modified | 1 | 1 | 2 | 
| [structured-outputs.md](#item-cc2557) | minor update | gpt-4oモデルのバージョン追加 | modified | 1 | 0 | 1 | 
| [global-batch-limits.md](#item-73207b) | minor update | o3-miniモデルのバッチ制限の追加 | modified | 2 | 1 | 3 | 
| [global-batch-datazone.md](#item-94a58c) | minor update | モデル行列の更新と新情報の追加 | modified | 14 | 12 | 26 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータと制限の更新 | modified | 4 | 4 | 8 | 


# Modified Contents
## articles/ai-services/openai/concepts/abuse-monitoring.md{#item-b7afcb}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ manager: nitinme
 
 # Abuse Monitoring
 
-Azure OpenAI Service detects and mitigates instances of recurring content and/or behaviors that suggest use of the service in a manner that might violate the [Code of Conduct](/legal/cognitive-services/openai/code-of-conduct?context=/azure/ai-services/openai/context/context) or other applicable product terms. Details on how data is handled can be found on the [Data, Privacy, and Security](/legal/cognitive-services/openai/data-privacy?context=/azure/ai-services/openai/context/context) page.
+Azure OpenAI Service detects and mitigates instances of recurring content and/or behaviors that suggest use of the service in a manner that might violate the [Code of Conduct](/legal/cognitive-services/openai/code-of-conduct?context=/azure/ai-services/openai/context/context). Details on how data is handled can be found on the [Data, Privacy, and Security](/legal/cognitive-services/openai/data-privacy?context=/azure/ai-services/openai/context/context) page.
 
 ## Components of abuse monitoring
 
@@ -22,14 +22,14 @@ There are several components to abuse monitoring:
 - **Content Classification**: Classifier models detect harmful text and/or images in user prompts (inputs) and completions (outputs). The system looks for categories of harms as defined in the [Content Requirements](/legal/cognitive-services/openai/code-of-conduct?context=/azure/ai-services/openai/context/context), and assigns severity levels as described in more detail on the [Content Filtering](/azure/ai-services/openai/concepts/content-filter) page. The content classification signals contribute to pattern detection as described below.  
 - **Abuse Pattern Capture**: Azure OpenAI Service’s abuse monitoring system looks at customer usage patterns and employs algorithms and heuristics to detect and score indicators of potential abuse. Detected patterns consider, for example, the frequency and severity at which harmful content is detected (as indicated in content classifier signals) in a customer’s prompts and completions, as well as the intentionality of the behavior. The trends and urgency of the detected pattern will also affect scoring of potential abuse severity.
     For example, a higher volume of harmful content classified as higher severity, or recurring conduct indicating intentionality (such as recurring jailbreak attempts) are both more likely to receive a high score indicating potential abuse. 
-- **Review and Decision**: Prompts and completions that are flagged through content classification and/or identified as part of a potentially abusive pattern of use are subjected to another review process to help confirm the system’s analysis and inform actioning decisions. Such review is conducted through two methods: human review & AI review.
-    - By default, if prompts and completions are flagged through content classification as harmful and/or identified to be part of a potentially abusive pattern of use, they may be sampled for automated, eyes-off review by using an LLM instead of a human reviewer. The LLM used for this purpose processes prompts and completions only to confirm the system’s analysis and inform actioning decisions; prompts and completions that undergo such LLM review are not stored by the system or used to train the LLM or other systems.
-    - In some cases, when automated review does not meet applicable confidence thresholds in complex contexts or if LLM review systems are not available, human eyes-on review may be introduced to make an extra judgment. This can help improve the overall abuse analysis accuracy. Authorized Microsoft employees may assess flagged content, and either confirm or correct the classification or determination based on predefined guidelines and policies. Prompts and completions can be accessed for human review only by authorized Microsoft employees via Secure Access Workstations (SAWs) with Just-In-Time (JIT) request approval granted by team managers. For Azure OpenAI Service resources deployed in the European Economic Area, the authorized Microsoft employees are located in the European Economic Area. This human review process will not take place if the customer has been approved for modified abuse monitoring. 
+- **Review and Decision**: Prompts and completions that are flagged through content classification and/or identified as part of a potentially abusive pattern of use are subjected to another review process to help confirm the system’s analysis and inform actioning decisions for abuse monitoring. Such review is conducted through two methods: automated review and human review.
+    - By default, if prompts and completions are flagged through content classification as harmful and/or identified to be part of a potentially abusive pattern of use, they may be sampled for review by using automated means including AI models such as LLMs instead of a human reviewer. The model used for this purpose processes prompts and completions only to confirm the system’s analysis and inform actioning decisions; prompts and completions that undergo such review are not stored by the abuse monitoring system or used to train the AI model or other systems.
+    - In some cases, when automated review does not meet applicable confidence thresholds in complex contexts or if automated review systems are not available, human eyes-on review may be introduced to make an extra judgment. Authorized Microsoft employees may assess content flagged through content classification and/or identified as part of a potentially abusive pattern of use, and either confirm or correct the classification or determination based on predefined guidelines and policies. Such prompts and completions can be accessed for human review only by authorized Microsoft employees via Secure Access Workstations (SAWs) with Just-In-Time (JIT) request approval granted by team managers. For Azure OpenAI Service resources deployed in the European Economic Area, the authorized Microsoft employees are located in the European Economic Area. This human review abuse monitoring process will not take place if the customer has been approved for modified abuse monitoring. 
 - **Notification and Action**: When a threshold of abusive behavior has been confirmed based on the preceding steps, the customer is informed of the determination by email. Except in cases of severe or recurring abuse, customers typically are given an opportunity to explain or remediate—and implement mechanisms to prevent recurrence of—the abusive behavior. Failure to address the behavior—or recurring or severe abuse—may result in suspension or termination of the customer’s access to Azure OpenAI resources and/or capabilities.
 
 ## Modified abuse monitoring 
 
-Some customers may want to use the Azure OpenAI Service for a use case that involves the processing of highly sensitive or highly confidential data, or otherwise may conclude that they do not want or do not have the right to permit Microsoft to store and conduct human review on their prompts and completions for abuse detection. To address these concerns, Microsoft allows customers who meet additional Limited Access eligibility criteria to apply to modify abuse monitoring by completing [this ](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUOE9MUTFMUlpBNk5IQlZWWkcyUEpWWEhGOCQlQCN0PWcu)form. Learn more about applying for modified abuse monitoring at [Limited access to Azure OpenAI Service](/legal/cognitive-services/openai/limited-access?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext), and about the impact of modified abuse monitoring on data processing at [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=azure-portal).    
+Some customers may want to use the Azure OpenAI Service for a use case that involves the processing of highly sensitive or highly confidential data, or otherwise may conclude that they don't want or don't have the right to permit Microsoft to store and conduct human review on their prompts and completions for abuse detection. To address these concerns, Microsoft allows customers who meet additional Limited Access eligibility criteria to apply to modify abuse monitoring by completing [this ](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUOE9MUTFMUlpBNk5IQlZWWkcyUEpWWEhGOCQlQCN0PWcu)form. Learn more about applying for modified abuse monitoring at [Limited access to Azure OpenAI Service](/legal/cognitive-services/openai/limited-access?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext), and about the impact of modified abuse monitoring on data processing at [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=azure-portal).    
 
 > [!NOTE]
 > When abuse monitoring is modified and human review is not performed, detection of potential abuse may be less accurate. Customers are notified of potential abuse detection as described above, and should be prepared to respond to such notification to avoid service interruption if possible.  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "虐待モニタリングの更新"
}
```

### Explanation
この変更では、Azure OpenAIサービスの「虐待モニタリング」に関する文書において、内容の明確化を目的としていくつかの修正が行われました。具体的には、レビューと決定のプロセスにおける説明が整理され、内容の一部がより簡潔に記述されました。また、テキストの流れと表現を改善し、ユーザーが理解しやすい形に整えられています。これにより、利用者が虐待モニタリングのプロセスをより明確に理解できるようになります。

## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -20,10 +20,10 @@ Azure OpenAI Service models are continually refreshed with newer and more capabl
 
 ### Terminology
 
-* Retirement
-	* When a model is retired, it's no longer available for use. Azure OpenAI Service deployments of a retired model always return error responses.
 * Deprecation
 	* When a model is deprecated, it's no longer available for new customers. It continues to be available for use by customers with existing deployments until the model is retired.
+* Retirement
+	* When a model is retired, it's no longer available for use. Azure OpenAI Service deployments of a retired model always return error responses.
 
 ## Notifications
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの退役に関する用語の修正"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるモデルの退役に関する説明を修正したもので、用語の定義部分が整理されています。具体的には、「退役」と「非推奨」という用語の説明が明確に区別されるよう、フォーマットの修正が行われています。この更新により、ユーザーがモデルの使用状況とその影響をより正確に理解できるようになります。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 2/7/2025
+ms.date: 2/14/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -37,7 +37,7 @@ The Azure OpenAI o<sup>&#42;</sup> series models are specifically designed to ta
 | `o3-mini` (2025-01-31) | The latest reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text-only processing <br> - Functions/Tools <br> <br> **Request access: [limited access model application](https://aka.ms/OAI/o1access)** | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
 | `o1` (2024-12-17) | The most capable model in the o1 series, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools <br> <br> **Request access: [limited access model application](https://aka.ms/OAI/o1access)** | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
 |`o1-preview` (2024-09-12) | Older preview version | Input: 128,000  <br> Output: 32,768 | Oct 2023 |
-| `o1-mini` (2024-09-12) | A faster and more cost-efficient option in the o1 series, ideal for coding tasks requiring speed and lower resource consumption.| Input: 128,000  <br> Output: 65,536 | Oct 2023 |
+| `o1-mini` (2024-09-12) | A faster and more cost-efficient option in the o1 series, ideal for coding tasks requiring speed and lower resource consumption. <br> Global standard deployment available by default <br> For standard deployments, **Request access: [limited access model application](https://aka.ms/OAI/o1access)**  | Input: 128,000  <br> Output: 65,536 | Oct 2023 |
 
 ### Availability
 
@@ -150,11 +150,6 @@ See [model versions](../concepts/model-versions.md) to learn about how Azure Ope
 - GPT-4 version 0125-preview completes tasks such as code generation more completely compared to gpt-4-1106-preview. Because of this, depending on the task, customers may find that GPT-4-0125-preview generates more output compared to the gpt-4-1106-preview.  We recommend customers compare the outputs of the new model.  GPT-4-0125-preview also addresses bugs in gpt-4-1106-preview with UTF-8 handling for non-English languages. 
 - GPT-4 version `turbo-2024-04-09` is the latest GA release and replaces `0125-Preview`, `1106-preview`, and `vision-preview`.
 
-> [!IMPORTANT]
-> The GPT-4 (`gpt-4`) versions `1106-Preview`, `0125-Preview`, and `vision-preview` will be upgraded with a stable version of `gpt-4` in the future. 
-> - Deployments of `gpt-4` versions `1106-Preview`, `0125-Preview`, and `vision-preview` set to "Auto-update to default" and "Upgrade when expired" will start to be upgraded after the stable version is released. For each deployment, a model version upgrade takes place with no interruption in service for API calls. Upgrades are staged by region and the full upgrade process is expected to take 2 weeks. 
-> - Deployments of `gpt-4` versions  `1106-Preview`, `0125-Preview`, and `vision-preview` set to "No autoupgrade" will not be upgraded and will stop operating when the preview version is upgraded in the region. 
-> See [Azure OpenAI model retirements and deprecations](./model-retirements.md) for more information on the timing of the upgrade.
 
 ## GPT-3.5
 
@@ -262,6 +257,8 @@ All deployments can perform the exact same inference operations, however the bil
 
 [!INCLUDE [Standard Models](../includes/model-matrix/standard-models.md)]
 
+**o-series models require registration for standard deployments**. Request access: [limited access model application](https://aka.ms/OAI/o1access)
+
 # [Provisioned Managed](#tab/provisioned)
 
 ### Provisioned deployment model availability
@@ -285,6 +282,8 @@ This table doesn't include fine-tuning regional availability information.  Consu
 
 [!INCLUDE [Chat Completions](../includes/model-matrix/standard-chat-completions.md)]
 
+**o-series models require registration for standard deployments**. Request access: [limited access model application](https://aka.ms/OAI/o1access)
+
 ### GPT-4 and GPT-4 Turbo model availability
 
 #### Select customer access
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル情報の更新"
}
```

### Explanation
この変更では、Azure OpenAIサービスにおけるモデルに関する文書の内容が更新されています。具体的には、モデルのリリース日や機能に関する情報が改訂され、「o1-mini」モデルについての説明に新たに「グローバル標準デプロイメントをデフォルトで利用可能」という文言が追加されました。また、モデルの利用に関する重要な注意事項や、標準デプロイメントに対する登録要件について明確にされています。これにより、ユーザーはモデルの最新の情報と利用条件を理解しやすくなっています。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ Request access: [limited access model application](https://aka.ms/OAI/o1access)
 | `o3-mini` | East US2 (Global Standard) <br> Sweden Central (Global Standard) | [Limited access model application](https://aka.ms/OAI/o1access) |
 |`o1` | East US2 (Global Standard) <br> Sweden Central (Global Standard) | [Limited access model application](https://aka.ms/OAI/o1access) |
 | `o1-preview` | See [models page](../concepts/models.md#global-standard-model-availability). | [Limited access model application](https://aka.ms/OAI/o1access) |
-| `o1-mini` | See [models page](../concepts/models.md#global-standard-model-availability). | No access request needed |
+| `o1-mini` | See [models page](../concepts/models.md#global-standard-model-availability). | No access request needed for Global Standard deployments<br>Standard (regional) deployments require: [Limited access model application](https://aka.ms/OAI/o1access) |
 
 ## API & feature support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アクセスリクエスト要件の更新"
}
```

### Explanation
この変更では、Azure OpenAIサービスにおける「o1-mini」モデルのアクセスリクエストに関する説明が更新されています。具体的には、グローバル標準デプロイメントの場合はアクセスリクエストが不要であることが明記され、標準（地域）デプロイメントの場合には「限定アクセスモデル申請が必要」と説明されています。この更新により、ユーザーは各デプロイメントタイプに応じた適切なアクセス資格や申請手続きについてより明確に理解できるようになっています。

## articles/ai-services/openai/how-to/structured-outputs.md{#item-cc2557}

<details>
<summary>Diff</summary>
````diff
@@ -29,6 +29,7 @@ Structured outputs make a model follow a [JSON Schema](https://json-schema.org/o
 - `o1` version: `2024-12-17`
 - `gpt-4o-mini` version: `2024-07-18`
 - `gpt-4o` version: `2024-08-06`
+- `gpt-4o` version: `2024-11-20`
 
 ## API support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "gpt-4oモデルのバージョン追加"
}
```

### Explanation
この変更では、「structured-outputs.md」の内容が更新され、`gpt-4o`モデルの新しいリリースバージョンが追加されました。具体的には、`gpt-4o`のバージョンとして「2024-11-20」が新たに記載されており、これによりユーザーはこのモデルが最新のアップデートを受けていることを把握できるようになります。この更新は、利用可能なモデルのバージョン管理に関して重要な情報を提供しています。

## articles/ai-services/openai/includes/global-batch-limits.md{#item-73207b}

<details>
<summary>Diff</summary>
````diff
@@ -38,4 +38,5 @@ B = billion | M = million | K = thousand
 |Model|Enterprise agreement|Default| Monthly credit card based subscriptions | MSDN subscriptions | Azure for Students, Free Trials |
 |---|---|---|---|---|---|
 | `gpt-4o` | 500 M | 30 M | 30 M | 90 K | N/A|
-| `gpt-4o-mini` | 1.5 B | 100 M | 50 M | 90 K | N/A |
\ No newline at end of file
+| `gpt-4o-mini` | 1.5 B | 100 M | 50 M | 90 K | N/A |
+| `o3-mini` | 1.5 B | 100 M | 50 M | 90 K | N/A |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "o3-miniモデルのバッチ制限の追加"
}
```

### Explanation
この変更では、「global-batch-limits.md」というファイルにおいて、新たに`o3-mini`モデルのバッチ制限が追加されました。これにより、`o3-mini`は1.5Bのエンタープライズ契約、100Mのデフォルト、および50Mの月額クレジットカードサブスクリプションの制限があることが明記されています。この更新は、ユーザーが利用可能なモデルごとのバッチ制限をより正確に理解できるようにするものです。また、既存の`gpt-4o-mini`モデルの情報も維持されています。

## articles/ai-services/openai/includes/model-matrix/global-batch-datazone.md{#item-94a58c}

<details>
<summary>Diff</summary>
````diff
@@ -6,18 +6,20 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 01/14/2025
+ms.date: 02/14/2025
 ---
 
 
-| **Region**     | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:--------------------------:|:-------------------------------:|
-| eastus             | ✅                       | ✅                            |
-| eastus2            | ✅                       | ✅                            |
-| francecentral      | ✅                       | ✅                            |
-| germanywestcentral | ✅                       | ✅                            |
-| southcentralus     | ✅                       | ✅                            |
-| swedencentral      | ✅                       | ✅                            |
-| westeurope         | ✅                       | ✅                            |
-| westus             | ✅                       | ✅                            |
-| westus3            | ✅                       | ✅                            |
\ No newline at end of file
+| **Region**     | **o3-mini**, **2025-01-31**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:---------------------------:|:--------------------------:|:-------------------------------:|
+| eastus             | ✅                        | ✅                       | ✅                            |
+| eastus2            | ✅                        | ✅                       | ✅                            |
+| francecentral      | -                       | ✅                       | ✅                            |
+| germanywestcentral | -                       | ✅                       | ✅                            |
+| northcentralus     | ✅                        | ✅                       | ✅                            |
+| polandcentral      | -                       | ✅                       | ✅                            |
+| southcentralus     | ✅                        | ✅                       | ✅                            |
+| swedencentral      | -                       | ✅                       | ✅                            |
+| westeurope         | -                       | ✅                       | ✅                            |
+| westus             | ✅                        | ✅                       | ✅                            |
+| westus3            | ✅                        | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル行列の更新と新情報の追加"
}
```

### Explanation
この変更では、「global-batch-datazone.md」ファイルが更新され、モデル行列に新しい情報が追加されました。具体的には、`o3-mini`モデルのサポート地域が新たにリストに加えられ、バージョン情報が更新されています。更新された内容では、異なる地域での各モデルの可用性が明確に示されています。例えば、`o3-mini`のバージョンは「2025-01-31」となり、一部の地域では他のモデルと比べて異なる可用性が示されています。また、日付が「2025-01-14」から「2025-02-14」に変更されており、最新の情報が反映されています。この更新により、ユーザーは新しいモデルの地理的な可用性についてより包括的に理解できるようになります。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 1/30/2025
+ms.date: 2/14/2025
 ms.author: mbullwin
 ---
 
@@ -179,9 +179,9 @@ If your Azure subscription is linked to certain [offer types](https://azure.micr
 
 |Tier| Quota Limit in tokens per minute (TPM) |
 |---|:---|
-|Azure for Students, Free Trials | 1 K (all models)|
-| MSDN subscriptions | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K   |
-| Monthly credit card based subscriptions <sup>1</sup> | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K  |
+|Azure for Students, Free Trials | 1 K (all models) <br>Exception o-series: 0|
+| MSDN subscriptions | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br> o-series: 0   |
+| Monthly credit card based subscriptions <sup>1</sup> | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br> o-series: 0  |
 
 <sup>1</sup> This currently applies to [offer type 0003P](https://azure.microsoft.com/support/legal/offer-details/)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータと制限の更新"
}
```

### Explanation
この変更では、「quotas-limits.md」ファイルにおいて、Azureサブスクリプションのクォータと制限に関する情報が更新されました。主な変更点として、各サブスクリプションタイプにおけるトークン制限が明確にされ、新たにoシリーズに関する制限が追加されています。具体的には、「Azure for Students, Free Trials」では全モデルに対して1Kの制限が設定され、oシリーズに対しては0トークンの例外が示されています。同様に、MSDN サブスクリプションおよび月額クレジットカードベースのサブスクリプションでのoシリーズに関するトークン制限も追加されました。また、ドキュメントの日付が「2025年1月30日」から「2025年2月14日」に更新されています。このような情報の更新により、ユーザーは自身のサブスクリプションに関連したクォータをより正確に理解することができます。


