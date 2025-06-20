---
date: '2025-06-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1531236...MicrosoftDocs:fc0b900
summary: この文書の変更は、新機能の追加や情報の明確化、冗長な部分の排除を目的としています。新たに「codex-mini」と「o3-pro」のモデルに関する情報が追加され、バッチ処理のエラーコードも新設されました。特に大きな破壊的変更はありませんが、ドキュメントは最新の使用状況とサポートを反映しています。また、モデルリタイアメントの通知方法や構造化出力、推論機能に関する情報が整理されました。全体として、Azure
  OpenAIサービスのユーザーエクスペリエンス向上を意図しており、ユーザーは新しいモデルの特徴やエラーハンドリングに関する情報を得て、問題解決をよりスムーズに行えるようになります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1531236...MicrosoftDocs:fc0b900){target="_blank"}

<format>
# Highlights
以下の文書変更には、新機能の追加や情報の明確化、冗長な部分の排除などの改良がなされています。特に、新しいモデルの情報追加や、エラーコード、関数呼び出し、推論機能に関する更新が挙げられます。

## New features
- "codex-mini" と "o3-pro" モデルに関する詳細情報の追加。
- バッチ処理のエラーコード追加。

## Breaking changes
- 特に大きな破壊的な変更は報告されていませんが、ドキュメントが最新の使用状況とサポートを反映していると理解されます。

## Other updates
- モデルリタイアメント通知方法の明確化。
- 構造化出力や推論機能のサポート情報の整理と最新化。

# Insights
この文書の更新は、Azure OpenAIサービスにおけるユーザーエクスペリエンスの向上を意図して行われています。重要なのは、ユーザーに対して新モデルの機能やエラーハンドリングに関する情報を明確にし、より良い問題解決をサポートすることです。

## モデルの追加と情報の整理
新たに追加された「codex-mini」と「o3-pro」モデルは、特定の地域で利用可能で、これによりユーザーは自分のニーズに合ったモデルを選択しやすくなっています。また、各モデルの特徴と機能がより詳細にまとめられることで、利用者は技術的選択を行う際に十分な情報を得ることができます。

## エラーハンドリングの改善
バッチ処理に関するエラーコードが追加されたことで、ユーザーは発生しうる問題を迅速かつ効果的に診断し、適切な対策を講じることが可能になりました。具体的なエラー情報を提供することは、開発者にとって重要なサポートであり、Azure OpenAIの実用性を向上させます。

## サポート機能の最新化
関数呼び出しや構造化出力の更新は、ユーザーが新しい技術的能力を活用し、より多くのオプションを探索できるようにするものです。これらのドキュメントの更新は、ユーザーに最新の技術的トレンドと互換性を保証します。

全体的に、このドキュメントの変更は、Azure OpenAIが最新の市場と技術のニーズに対応し続け、ユーザーがサービスを最大限に活用できるようにすることを目的としています。これにより、ユーザーは新しいモデルの利点を享受し、さらに高度で効率的なAIソリューションの開発に活用可能です。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルのリタイアメントに関する情報の更新 | modified | 15 | 17 | 32 | 
| [models.md](#item-db2c37) | minor update | モデルに関する情報の追加と整理 | modified | 7 | 2 | 9 | 
| [batch.md](#item-a131d5) | minor update | バッチ処理エラーに関する情報の追加 | modified | 3 | 1 | 4 | 
| [function-calling.md](#item-32f8e0) | minor update | 関数呼び出し機能に関する情報の追加 | modified | 3 | 1 | 4 | 
| [reasoning.md](#item-a54b2f) | minor update | 推論機能に関する情報の更新 | modified | 25 | 22 | 47 | 
| [structured-outputs.md](#item-cc2557) | minor update | 構造化出力に関するモデル情報の更新 | modified | 3 | 1 | 4 | 
| [whats-new.md](#item-53303b) | minor update | 最新情報セクションの更新 | modified | 7 | 1 | 8 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -35,16 +35,11 @@ Azure OpenAI notifies customers of active Azure OpenAI deployments for models wi
 
 Retirements are done on a rolling basis, region by region. There is no schedule for when a specific region, or SKU will be upgraded.
 
-## Current models
-
-> [!NOTE]
-> Not all models go through a deprecation period prior to retirement. Some models/versions only have a retirement date.
->
-> **Fine-tuned models** are subject to a [different](#fine-tuned-models) deprecation and retirement schedule from their equivalent base model.
-
-These models are currently available for use in Azure OpenAI.
+### Who is notified of upcoming retirements
 
-[!INCLUDE [Model retirement table](../includes/retirement/models.md)]
+Azure OpenAI notifies customers via two methods:
+- **Azure Resource Health** - Anyone with reader permissions or above can see Azure health alerts, as well as configure personalized alerts via email, SMS, etc. See [Create Service Health Alerts](/azure/service-health/alerts-activity-log-service-notifications-portal)
+- **Email** - email notifications are automatically sent to subscription owners. Any individual with reader permissions may however configure their own alerts by following the guidance above.
 
 ## Model availability
 
@@ -73,14 +68,6 @@ Be aware of the following:
     1. For example if `gpt-35-turbo 0125` or `gpt-4o (2024-05-13)` is updated to a future version, or
     2. for model family changes beyond version updates, such as when moving from `gpt-4 1106-preview` to `gpt-4o (2024-05-13)`. 
 
-### Who is notified of upcoming retirements
-
-Azure OpenAI notifies customers via two methods:
-- **Azure Resource Health** - Anyone with reader permissions or above can see Azure health alerts, as well as configure personalized alerts via email, SMS, etc. See [Create Service Health Alerts](/azure/service-health/alerts-activity-log-service-notifications-portal)
-- **Email** - email notifications are automatically sent to subscription owners. Any individual with reader permissions may however configure their own alerts by following the guidance above.
-
-
-
 ## How to get ready for model retirements and version upgrades
 
 To prepare for model retirements and version upgrades, we recommend that customers test their applications with the new models and versions and evaluate their behavior. We also recommend that customers update their applications to use the new models and versions before the retirement date.
@@ -91,6 +78,17 @@ For information on the model upgrade process, see [How to upgrade to a new model
 
 For more information on how to manage model upgrades and migrations for provisioned deployments, see [Managing models on provisioned deployment types](../how-to/working-with-models.md#managing-models-on-provisioned-deployment-types)
 
+## Current models
+
+> [!NOTE]
+> Not all models go through a deprecation period prior to retirement. Some models/versions only have a retirement date.
+>
+> **Fine-tuned models** are subject to a [different](#fine-tuned-models) deprecation and retirement schedule from their equivalent base model.
+
+These models are currently available for use in Azure OpenAI.
+
+[!INCLUDE [Model retirement table](../includes/retirement/models.md)]
+
 ## Retirement and deprecation history
 
 To track individual updates to this article refer to the [Git History](https://github.com/MicrosoftDocs/azure-ai-docs/commits/main/articles/ai-services/openai/includes/retirement/models.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのリタイアメントに関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIのモデルリタイアメントに関する文書の一部を更新するもので、主に情報の整理と明確化が行われました。以下の点が主な変更点です。

1. **見出しの変更**: 「## 現在のモデル」というセクションが新たに「### 誰がリタイアメントの通知を受けるか」という見出しに置き換えられています。この変更により、通知に関する情報がより明確に強調されています。

2. **通知方法の明確化**: Azure OpenAIがどのようにお客様にリタイアメントについて通知するかの方法が具体的に説明されています。これには、Azure Resource Healthを通じたアラートやメール通知の設定についての詳細が含まれています。

3. **内容の追加と削除**: いくつかの情報が追加されている一方で、古い情報が削除されています。特に、リタイアメントの通知方法についての重複したセクションが削除され、ドキュメントの冗長性が軽減されています。

この更新により、ユーザーがモデルリタイアメントについての情報をより迅速かつ簡潔に理解できるように配慮されています。文書の構成が改善され、現在利用可能なモデルに関する情報が強調されています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -22,6 +22,7 @@ Azure OpenAI is powered by a diverse set of models with different capabilities a
 
 | Models | Description |
 |--|--|
+| [codex-mini](#o-series-models) | Fine-tuned version of o4-mini. |  
 | [GPT-4.1 series](#gpt-41-series) | Latest model release from Azure OpenAI |
 | [model-router](#model-router) | A model that intelligently selects from a set of underlying chat models to respond to a given prompt. |
 | [computer-use-preview](#computer-use-preview) | An experimental model trained for use with the Responses API computer use tool. |
@@ -49,7 +50,7 @@ Azure OpenAI is powered by a diverse set of models with different capabilities a
 |  Model ID  | Description | Context Window | Max Output Tokens | Training Data (up to)  |
 |  --- |  :--- |:--- |:---|:---: |
 | `gpt-4.1` (2025-04-14)   | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | - 1,047,576 <br> - 128,000 (provisioned managed deployments) | 32,768 | May 31, 2024 |
-| `gpt-4.1-nano` (2025-04-14) <br><br> **Fastest 4.1 model** | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | - 1,047,576  <br> - 128,000 (provisioned managed deployments)  | 32,768 | May 31, 2024 |
+| `gpt-4.1-nano` (2025-04-14) | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | - 1,047,576  <br> - 128,000 (provisioned managed deployments)  | 32,768 | May 31, 2024 |
 | `gpt-4.1-mini` (2025-04-14) | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | - 1,047,576  <br> - 128,000 (provisioned managed deployments)  | 32,768 | May 31, 2024 |
 
 ## model-router
@@ -121,7 +122,9 @@ The Azure OpenAI o<sup>&#42;</sup> series models are specifically designed to ta
 
 |  Model ID  | Description | Max Request (tokens) | Training Data (up to)  |
 |  --- |  :--- |:--- |:---: |
-| `o4-mini` (2025-04-16) | - **NEW** reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br><br> - Chat Completions API <br> - [Responses API](../how-to/responses.md) <br>- Structured outputs<br> - Text, image processing <br> - Functions/Tools/Parallel tool calling <br> [Full summary of capabilities](../how-to/reasoning.md) | Input: 200,000 <br> Output: 100,000 | May 31, 2024 |   
+| `codex-mini` (2025-05-16) | Fine-tuned version of o4-mini. <br> - [Responses API](../how-to/responses.md) <br>- Structured outputs<br> - Text, image processing <br> - Functions/Tools<br> [Full summary of capabilities](../how-to/reasoning.md) | Input: 200,000 <br> Output: 100,000 | May 31, 2024 |
+| `o3-pro` (2025-06-10) | - [Responses API](../how-to/responses.md) <br>- Structured outputs<br> - Text, image processing <br> - Functions/Tools<br> [Full summary of capabilities](../how-to/reasoning.md) | Input: 200,000 <br> Output: 100,000 | May 31, 2024 |
+| `o4-mini` (2025-04-16) | - **NEW** reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br><br> - Chat Completions API <br> - [Responses API](../how-to/responses.md) <br>- Structured outputs<br> - Text, image processing <br> - Functions/Tools<br> [Full summary of capabilities](../how-to/reasoning.md) | Input: 200,000 <br> Output: 100,000 | May 31, 2024 |   
 | `o3` (2025-04-16) | - **NEW** reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br>  <br> - Chat Completions API <br> - [Responses API](../how-to/responses.md) <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools/Parallel tool calling <br> [Full summary of capabilities](../how-to/reasoning.md) | Input: 200,000 <br> Output: 100,000 | May 31, 2024 |    
 | `o3-mini` (2025-01-31) | - [Enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text-only processing <br> - Functions/Tools | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
 | `o1` (2024-12-17) | - [Enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
@@ -136,6 +139,8 @@ To learn more about the advanced `o-series` models see, [getting started with re
 
 | Model | Region |
 |---|---|
+|`codex-mini` | East US2 & Sweden Central (Global Standard)   |
+|`o3-pro`   | East US2 & Sweden Central (Global Standard)    |
 |`o4-mini`|   See the [models table](#model-summary-table-and-region-availability).  |
 | `o3` |   See the [models table](#model-summary-table-and-region-availability).  |
 |`o3-mini` | See the [models table](#model-summary-table-and-region-availability). |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルに関する情報の追加と整理"
}
```

### Explanation
この変更は、Azure OpenAIのモデルに関するドキュメントの情報を更新し、整理するもので、以下の主要な点が含まれています。

1. **モデル情報の追加**: 新たに「codex-mini」と「o3-pro」モデルに関する情報が追加されました。これにより、ユーザーは新しいモデルの特徴や機能をより理解しやすくなります。

2. **モデル表の改善**: モデル一覧のテーブルに新しい行が追加され、それぞれのモデルの説明が詳細に記載されています。これにより、各モデルの用途や機能が明確に示されています。

3. **リファレンス情報の整備**: 変更により、特定のモデルに関連するリファレンスや機能のリンクが更新され、ユーザーがモデルの詳細な能力や使用方法についてアクセスしやすくなっています。

4. **冗長性の排除**: 更新の一環として、いくつかの重複情報が整理され、文書がより読みやすく、効率的に必要な情報を提供できるようになっています。

全体として、この更新はAzure OpenAIモデルに関する情報のアクセス性と理解を向上させることを目的としており、ユーザーに対して最新の情報を提供しています。

## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use global batch with Azure OpenAI
 author: mrbullwinkle
 ms.author: mbullwin
 manager: nitinme
-ms.date: 05/28/2025
+ms.date: 06/19/2025
 ms.service: azure-ai-openai
 ms.topic: how-to
 ms.custom:
@@ -232,6 +232,8 @@ When a job failure occurs, you'll find details about the failure in the `errors`
 |`empty_batch` | Please check your input file to ensure that the custom ID parameter is unique for each request in the batch.|
 |`model_mismatch`| The Azure OpenAI model deployment name that was specified in the `model` property of this request in the input file doesn't match the rest of the file.<br><br>Please ensure that all requests in the batch point to the same Azure OpenAI in Azure AI Foundry Models model deployment in the `model` property of the request.|
 |`invalid_request`| The schema of the input line is invalid or the deployment SKU is invalid. <br><br>Please ensure the properties of the request in your input file match the expected input properties, and that the Azure OpenAI deployment SKU is `globalbatch` for batch API requests.|
+| `input_modified` |Blob input has been modified after the batch job has been submitted. |
+| `input_no_permissions` | It's not possible to access the input blob. Please check [permissions](./role-based-access-control.md) and network access between the Azure OpenAI account and Azure Storage account.  |
 
 ### Known issues
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理エラーに関する情報の追加"
}
```

### Explanation
この変更は、Azure OpenAIのバッチ処理に関する文書の一部を更新し、新しいエラーコードの説明を追加したものです。主な内容は以下の通りです。

1. **日付の更新**: ドキュメントの日付が、2025年5月28日から2025年6月19日に変更され、最近の情報を反映しています。

2. **エラーコードの追加**: 新たに以下のエラーコードがバッチ処理のセクションに追加されています。
   - `input_modified`: バッチジョブが送信された後にBlob入力が変更されたことを示します。
   - `input_no_permissions`: 入力Blobにアクセスできないことを示し、アクセス権やネットワーク接続の確認を促します。

3. **エラーメッセージの明確化**: これにより、ユーザーがバッチ処理中に遭遇する可能性のあるエラーをより理解しやすくなり、適切に対処できる道筋が示されています。

更新内容により、ユーザーはエラーの原因を特定しやすくなり、バッチ処理に関連する問題の解決がスムーズになることが期待されます。全体的に、この変更はドキュメントの実用性を向上させています。

## articles/ai-services/openai/how-to/function-calling.md{#item-32f8e0}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: mbullwin #delegenz
 ms.service: azure-ai-openai
 ms.custom: devx-track-python
 ms.topic: how-to
-ms.date: 04/16/2025
+ms.date: 06/17/2025
 manager: nitinme
 ---
 
@@ -48,6 +48,8 @@ Support for parallel function was first added in API version [`2023-12-01-previe
 ### Basic function calling with tools
 
 * All the models that support parallel function calling
+* `codex-mini` (`2025-05-16`)
+* `o3-pro` (`2025-06-10`)
 * `o4-mini` (`2025-04-16`)
 * `o3` (`2025-04-16`)
 * `gpt-4.1-nano` (`2025-04-14`)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "関数呼び出し機能に関する情報の追加"
}
```

### Explanation
この変更は、Azure OpenAIの関数呼び出しに関するドキュメントを更新するもので、いくつかの重要なポイントが含まれています。

1. **日付の更新**: ドキュメントの日付が2025年4月16日から2025年6月17日に変更され、最新の情報を反映しています。

2. **新モデルの追加**: 関数呼び出しをサポートするモデルのリストに、新たに以下の2つのモデルが追加されました。
   - `codex-mini` (リリース日：2025年5月16日)
   - `o3-pro` (リリース日：2025年6月10日)

3. **機能の拡張情報**: これにより、ユーザーは新しくサポートされるモデルを元に、並列関数呼び出し機能を利用する際の選択肢が広がります。

全体として、この更新は関数呼び出しの機能に関連する最新情報を提供し、ユーザーが新しいモデルを利用する際の助けとなることを目的としています。これにより、用途や実装の選択肢がさらに明確になります。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's advanced o3-mini, o1, & o1-mini rea
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 04/18/2025
+ms.date: 06/17/2025
 author: mrbullwinkle    
 ms.author: mbullwin
 ---
@@ -28,40 +28,43 @@ Azure OpenAI `o-series` models are designed to tackle reasoning and problem-solv
 
 | Model | Region | Limited access |
 |---|---|---|
-| `o4-mini`  | East US2 (Global Standard) <br><br> Sweden Central (Global Standard)   | No access request needed to use the core capabilities of this model.<br><br> Request access: [o4-mini reasoning summary feature](https://aka.ms/oai/o3access)     |
-| `o3` |  East US2 (Global Standard) <br><br> Sweden Central (Global Standard)     | Request access: [o3 limited access model application](https://aka.ms/oai/o3access)     |
+| `o3-pro`  | East US2 & Sweden Central (Global Standard)    |  Request access: [o3 limited access model application](https://aka.ms/oai/o3access). If you already have `o3 access` no request is required for `o3-pro`.    |
+| `codex-mini`  | East US2 & Sweden Central (Global Standard)    | No access request needed.    |
+| `o4-mini`  | [Model availability](../concepts/models.md#global-standard-model-availability)   | No access request needed to use the core capabilities of this model.<br><br> Request access: [o4-mini reasoning summary feature](https://aka.ms/oai/o3access)     |
+| `o3` |  [Model availability](../concepts/models.md#global-standard-model-availability)  | Request access: [o3 limited access model application](https://aka.ms/oai/o3access)     |
 | `o3-mini` | [Model availability](../concepts/models.md#global-standard-model-availability).  | Access is no longer restricted for this model.   |
 |`o1` | [Model availability](../concepts/models.md#global-standard-model-availability).  | Access is no longer restricted for this model.  |
 | `o1-preview` | [Model availability](../concepts/models.md#global-standard-model-availability). |This model is only available for customers who were granted access as part of the original limited access release. We're currently not expanding access to `o1-preview`. |
 | `o1-mini` | [Model availability](../concepts/models.md#global-standard-model-availability). | No access request needed for Global Standard deployments.<br><br>Standard (regional) deployments are currently only available to select customers who were previously granted access as part of the `o1-preview` release.|
 
 ## API & feature support
 
-| **Feature**     | **o4-mini**, **2025-04-16**  | **o3**, **2025-04-16** | **o3-mini**, **2025-01-31**  |**o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   |
-|:-------------------|:--------------------------:|:-----:|:-------:|:--------------------------:|:-------------------------------:|:---:|
-| **API Version**    | `2025-04-01-preview`   | `2025-04-01-preview`   | `2024-12-01-preview` or later <br> `2025-03-01-preview` (Recommended)   | `2024-12-01-preview` or later <br> `2025-03-01-preview` (Recommended) | `2024-09-01-preview` or later <br> `2025-03-01-preview` (Recommended)    | `2024-09-01-preview` or later <br> `2025-03-01-preview` (Recommended)    |
-| **[Developer Messages](#developer-messages)** | ✅ | ✅ | ✅ | ✅ | - | - |
-| **[Structured Outputs](./structured-outputs.md)** | ✅ | ✅ | ✅ | ✅ | - | - |
-| **[Context Window](../concepts/models.md#o-series-models)** | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 128,000  <br> Output: 32,768 | Input: 128,000  <br> Output: 65,536 |
-| **[Reasoning effort](#reasoning-effort)** | ✅| ✅ |✅ | ✅ | - | - |
-| **[Vision Support](./gpt-with-vision.md)** | ✅ | ✅ | - | ✅ | - | - |
-| Chat Completions API | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| Responses API | ✅ | ✅  | - | - | - | - |
-| Functions/Tools | ✅ | ✅ | ✅  | ✅  |  - | - |
-| Parallel Tool Calls | - | - | -  | -  |  - | - |
-| `max_completion_tokens` <sup>1</sup> | ✅ | ✅ |✅ |✅ |✅ | ✅ |
-| System Messages <sup>2</sup> | ✅ | ✅ | ✅ | ✅ | - | - |
-| [Reasoning summary](#reasoning-summary) <sup>3</sup> | ✅ | ✅ | -  | -  |  - | - |
-| Streaming <sup>4</sup>  | ✅ | ✅| ✅ | - | - | - |
+| **Feature**  | **codex-mini**, **2025-05-16**  | **o3-pro**, **2025-06-10**   | **o4-mini**, **2025-04-16**  | **o3**, **2025-04-16** | **o3-mini**, **2025-01-31**  |**o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   |
+|:-------------------|:--------------------------:|:------:|:--------|:-----:|:-------:|:--------------------------:|:-------------------------------:|:---:|
+| **API Version** | `2025-04-01-preview` & [v1 preview](../api-version-lifecycle.md#api-evolution)   | `2025-04-01-preview`  & [v1 preview](../api-version-lifecycle.md#api-evolution)  | `2025-04-01-preview`   | `2025-04-01-preview`   | `2024-12-01-preview` or later <br> `2025-03-01-preview` (Recommended)   | `2024-12-01-preview` or later <br> `2025-03-01-preview` (Recommended) | `2024-09-01-preview` or later <br> `2025-03-01-preview` (Recommended)    | `2024-09-01-preview` or later <br> `2025-03-01-preview` (Recommended)    |
+| **[Developer Messages](#developer-messages)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - | - |
+| **[Structured Outputs](./structured-outputs.md)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - | - |
+| **[Context Window](../concepts/models.md#o-series-models)** |  Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 128,000  <br> Output: 32,768 | Input: 128,000  <br> Output: 65,536 |
+| **[Reasoning effort](#reasoning-effort)** | ✅| ✅| ✅| ✅ |✅ | ✅ | - | - |
+| **[Image input](./gpt-with-vision.md)** | ✅ | ✅ | ✅ | ✅ | - | ✅ | - | - |
+| Chat Completions API | - | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
+| Responses API | ✅  | ✅  | ✅ | ✅  | - | - | - | - |
+| Functions/Tools | ✅ | ✅ |✅ | ✅ | ✅  | ✅  |  - | - |
+| Parallel Tool Calls | - | - | - | - | -  | -  |  - | - |
+| `max_completion_tokens` <sup>1</sup> |  ✅ | ✅ | ✅ | ✅ |✅ |✅ |✅ | ✅ |
+| System Messages <sup>2</sup> | ✅ | ✅| ✅ | ✅ | ✅ | ✅ | - | - |
+| [Reasoning summary](#reasoning-summary) <sup>3</sup> |  ✅ | - | ✅ | ✅ | -  | -  |  - | - |
+| Streaming <sup>4</sup>  | ✅ | - | ✅ | ✅| ✅ | - | - | - |
 
 <sup>1</sup> Reasoning models will only work with the `max_completion_tokens` parameter. <br><br>
-
 <sup>2</sup> The latest o<sup>&#42;</sup> series model support system messages to make migration easier. When you use a system message with `o4-mini`, `o3`, `o3-mini`, and `o1` it will be treated as a developer message. You should not use both a developer message and a system message in the same API request.
-
 <sup>3</sup> Access to the chain-of-thought reasoning summary is limited access only for `o3` & `o4-mini`.
-
 <sup>4</sup> Streaming for `o3` is limited access only.
 
+> [!NOTE]
+> - To avoid timeouts [background mode](./responses.md#background-tasks) is recommended for `o3-pro`.
+> - `o3-pro` does not currently support image generation.
+
 ### Not Supported
 
 The following are currently unsupported with reasoning models:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "推論機能に関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIの推論機能に関する文書の内容を更新し、いくつかの重要な要素が追加または修正されています。

1. **日付の更新**: ドキュメントの日付が2025年4月18日から2025年6月17日に変更されています。これにより、情報が最新であることが示されています。

2. **モデルの情報の新規追加および修正**: 各モデルの表に新たに`o3-pro`および`codex-mini`が追加され、それぞれの利用可能地域やアクセスリクエストの必要条件が明確になりました。また、既存モデルに関する情報も整理されています。

   - `o3-pro`は、East US2およびSweden Centralで利用可能で、すでに`o3へのアクセス`を持っているユーザーは追加のリクエストを必要としません。
   - `codex-mini`は、同じ地域で問題なくアクセス可能です。
   - `o4-mini`および`o3`は、モデルの可用性に関するリンクが挿入され、詳細情報に簡単にアクセスできるようになりました。

3. **APIおよび機能サポートの更新**: 機能サポートの表が新しいモデルを反映するように更新され、新しいモデルのAPIバージョンや特徴も記載されています。特に、開発者メッセージ、構造化出力、コンテキストウィンドウなどのサポートが整理されています。

4. **ノートおよび非サポート情報の追加**: `o3-pro`のタイムアウトを避けるために背景モードの使用が推奨されることや、`o3-pro`は現在画像生成をサポートしていないことを明記したノートが追加されています。

この更新により、推論機能の利用がより明確になり、ユーザーは新しいモデルの機能を理解しやすくなります。全体として、文書が整理され、情報が最新化されていることが強調されています。

## articles/ai-services/openai/how-to/structured-outputs.md{#item-cc2557}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 04/16/2025
+ms.date: 06/17/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -25,6 +25,8 @@ Structured outputs make a model follow a [JSON Schema](https://json-schema.org/o
 
 ## Supported models
 
+- `codex-mini` version `2025-05-16`
+- `o3-pro` version `2025-06-10`
 - `gpt-4.5-preview` version `2025-02-27`
 - `o3-mini` version `2025-01-31`
 - `o1` version: `2024-12-17`
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "構造化出力に関するモデル情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIの構造化出力に関する文書の内容を更新し、以下の重要な要素が追加されています。

1. **日付の更新**: ドキュメントの日付が2025年4月16日から2025年6月17日に変更され、最新の情報を反映していることが示されています。

2. **モデル情報の追加**: 構造化出力をサポートするモデルに新たに以下の2つのモデルが追加されました。
   - `codex-mini` バージョン `2025-05-16`
   - `o3-pro` バージョン `2025-06-10`

   これにより、ユーザーはどのモデルが構造化出力をサポートしているかを容易に確認できるようになります。

3. **既存モデル情報の整理**: 既に記載されていたモデル情報についても整理され、視認性が向上しています。具体的には、`gpt-4.5-preview`、`o3-mini`、および`o1`のバージョン情報が明確にリストされており、構造化出力を利用する際に必要な情報が一目でわかるようになっています。

全体として、この更新は構造化出力機能の利用を促進するために必要な最新情報を提供し、関連するモデルの明確さを向上させることを目的としています。ユーザーは新しいモデルがサポートされていることを理解しやすくなり、機能を効果的に活用できるでしょう。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn about the latest news and features updates for Azure OpenAI.
 author: mrbullwinkle
 ms.author: mbullwin #
 manager: nitinme
-ms.date: 5/28/2025
+ms.date: 6/17/2025
 ms.service: azure-ai-openai
 ms.topic: whats-new
 ms.custom:
@@ -18,6 +18,12 @@ ms.custom:
 
 This article provides a summary of the latest releases and major documentation updates for Azure OpenAI.
 
+## June 2025
+
+### codex-mini & o3-pro models released
+
+- `codex-mini and `o3-pro` are now available. To learn more, see the [getting started with reasoning models page](./how-to/reasoning.md)
+
 ## May 2025
 
 ### Sora video generation released (preview)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新情報セクションの更新"
}
```

### Explanation
この変更は、Azure OpenAIの「最新情報」セクションを更新し、以下の重要な要素が追加されています。

1. **日付の更新**: ドキュメントの日付が2025年5月28日から2025年6月17日に変更されています。これにより、情報が最新のものであることが反映されています。

2. **新たなリリース情報の追加**: 2025年6月に関する情報が追加され、以下の内容が記載されています。
   - `codex-mini` と `o3-pro` モデルがリリースされたことが強調されています。これにより、ユーザーは新たに利用可能なモデルについての情報を把握できるようになります。
   - 詳細に関しては、「推論モデルの使い方」ページへのリンクが提供されており、ユーザーがさらに深く学ぶためのリソースが示されています。

3. **過去のリリース情報の整理**: 2025年5月にリリースされた「Soraビデオ生成（プレビュー）」に関する情報も維持されています。これにより、ユーザーは最近のリリースを一目で把握できます。

全体として、この更新はAzure OpenAIの最新リリースに関する情報を強化し、ユーザーに対して新機能を簡潔に紹介することを目的としています。新たなモデルの導入により、ユーザーはより広範な機能にアクセスできるようになり、効果的に活用できる情報を得ることができます。


