---
date: '2025-02-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7db5cb6...MicrosoftDocs:5c1bed9
summary: 今回の変更は、Azure OpenAIドキュメントに対するマイナーアップデートです。主な内容は、新しい`o3-mini`モデルの追加や既存モデル情報の調整、ドキュメントの日付更新です。特に、`o3-mini`モデルについての情報が多数のドキュメントに追加され、ユーザーはより最新かつ明確な情報を得られるようになっています。破壊的変更はないものの、既存モデルの名称や説明の変更があり、注意が必要です。このアップデートは、技術実装や迅速な意思決定を行うユーザーにとって便利なものであり、Azure
  OpenAIのサービス向上に寄与しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7db5cb6...MicrosoftDocs:5c1bed9){target="_blank"}

# Highlights

今回の変更は、複数のAzure OpenAIドキュメントに対するマイナーアップデートです。主な内容は日付の更新、新しいモデル情報の追加、および既存モデルの情報の調整です。新モデルとして`o3-mini`が追加されており、これに関連する情報が多数のドキュメントに追加されています。

## New features
- `o3-mini`モデルの追加と、それに関連する情報の拡充。
- `gpt-4o-audio-preview`モデルの利用可能地域が拡大。

## Breaking changes
- 破壊的変更は特にありませんが、既存モデルの名称や説明の変更により、情報の理解が求められます。

## Other updates
- ドキュメントの日付が全体的に更新され、ユーザーに最新の情報を提供。
- 手順や説明文の簡略化、一部画像の削除によるドキュメントの明確化。

# Insights

Azure OpenAIドキュメントの一連のマイナーアップデートは、主に情報を最新に保ち、新しいモデルの追加を反映することを目的としています。特に`o3-mini`モデルが多くの箇所で新たに言及されており、これがアップデートの中心にあります。このモデルは新しい推論能力を提供し、特に開発者にとってはその利便性が向上するでしょう。

加えて、日付の更新や手順の簡略化が行われているため、ユーザーはより最新かつ明確な情報を容易に得られます。これは特に、迅速な意思決定や技術実装を行いたいユーザーにとって利点があります。また、新しいモデル情報がサービス概要などのドキュメントに追加されていることは、多様な機能を提供するAzure OpenAIの利用拡大を見越したものでしょう。

このように、最新の技術動向を迅速に取り入れ、ドキュメントの明瞭化を図ることで、ユーザーが最新の技術を用いた開発を円滑に行えるようにする配慮がなされています。新しいモデルの追加と関連情報の整理は、サービスの競争力を高め、ユーザー体験を向上させることに寄与していると言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [legacy-models.md](#item-f6918a) | minor update | 更新された日付情報 / Date information updated | modified | 1 | 1 | 2 | 
| [models.md](#item-db2c37) | minor update | モデル情報の更新 / Model information updated | modified | 9 | 7 | 16 | 
| [create-resource.md](#item-c1c8a3) | minor update | 日付情報の更新 / Date information updated | modified | 1 | 1 | 2 | 
| [dynamic-quota.md](#item-b774ca) | minor update | 日付情報の更新と文章の簡略化 / Date information update and text simplification | modified | 2 | 4 | 6 | 
| [function-calling.md](#item-32f8e0) | minor update | 日付情報の更新とツールのサポート状況の変更 / Date information update and tool support status change | modified | 4 | 3 | 7 | 
| [manage-costs.md](#item-93c3f3) | minor update | 日付情報の更新 / Date information update | modified | 1 | 1 | 2 | 
| [managed-identity.md](#item-1a0afd) | minor update | 日付情報の更新 / Date information update | modified | 1 | 1 | 2 | 
| [migration-javascript.md](#item-19dac7) | minor update | 日付情報の更新 / Date information update | modified | 1 | 1 | 2 | 
| [reasoning.md](#item-a54b2f) | minor update | モデル情報の更新と追加 / Update and addition of model information | modified | 25 | 30 | 55 | 
| [structured-outputs.md](#item-cc2557) | minor update | サポートされるモデルに関する情報の追加 / Addition of information regarding supported models | modified | 1 | 0 | 1 | 
| [overview.md](#item-97d507) | minor update | サービス概要に新しいモデル情報の追加 / Addition of new model information in service overview | modified | 3 | 3 | 6 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータおよびレート制限に関する情報の更新 / Update of quota and rate limit information | modified | 6 | 3 | 9 | 
| [whats-new.md](#item-53303b) | minor update | 最新情報にo3-miniのリリース追加 / Addition of o3-mini release in What's New | modified | 5 | 1 | 6 | 


# Modified Contents
## articles/ai-services/openai/concepts/legacy-models.md{#item-f6918a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the deprecated models in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 06/14/2024
+ms.date: 01/31/2025
 ms.custom: references_regions, build-2023, build-2023-dataai
 manager: nitinme
 author: mrbullwinkle 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新された日付情報 / Date information updated"
}
```

### Explanation
この変更は、ドキュメント内の日付情報を更新するためのマイナーアップデートです。具体的には、`legacy-models.md`ファイルの中で、モデルに関する説明の下にある日付フィールドが「2024年6月14日」から「2025年1月31日」に変更されました。この更新は、新しい情報が利用可能になったことを示しており、ユーザーに最新の情報を提供することを目的としています。その他の内容は変更されていません。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 12/16/2024
+ms.date: 01/30/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -18,7 +18,7 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 
 | Models | Description |
 |--|--|
-| [o1 & o1-mini](#o1-and-o1-mini-models) |[Reasoning models](../how-to/reasoning.md) with advanced problem-solving and increased focus and capability.  |
+| [o-series models](#o-series-models) |[Reasoning models](../how-to/reasoning.md) with advanced problem-solving and increased focus and capability.  |
 | [GPT-4o & GPT-4o mini & GPT-4 Turbo](#gpt-4o-and-gpt-4-turbo) | The latest most capable Azure OpenAI models with multimodal versions, which can accept both text and images as input. |
 | [GPT-4o audio](#gpt-4o-audio) | GPT-4o audio models that support either low-latency, "speech in, speech out" conversational interactions or audio generation. |
 | [GPT-4](#gpt-4) | A set of models that improve on GPT-3.5 and can understand and generate natural language and code. |
@@ -28,30 +28,32 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 | [Whisper](#whisper-models) | A series of models in preview that can transcribe and translate speech to text. |
 | [Text to speech](#text-to-speech-models-preview) (Preview) | A series of models in preview that can synthesize text to speech. |
 
-## o1 and o1-mini models
+## o-series models
 
-The Azure OpenAI `o1` and `o1-mini` models are specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
+The Azure OpenAI o<sup>&#42;</sup> series models are specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
 
 |  Model ID  | Description | Max Request (tokens) | Training Data (up to)  |
 |  --- |  :--- |:--- |:---: |
+| `o3-mini` (2025-01-31) | The latest reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text-only processing <br> - Functions/Tools <br> <br> **Request access: [limited access model application](https://aka.ms/OAI/o1access)** | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
 | `o1` (2024-12-17) | The most capable model in the o1 series, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools <br> <br> **Request access: [limited access model application](https://aka.ms/OAI/o1access)** | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
 |`o1-preview` (2024-09-12) | Older preview version | Input: 128,000  <br> Output: 32,768 | Oct 2023 |
 | `o1-mini` (2024-09-12) | A faster and more cost-efficient option in the o1 series, ideal for coding tasks requiring speed and lower resource consumption.| Input: 128,000  <br> Output: 65,536 | Oct 2023 |
 
 ### Availability
 
-The `o1` and `o1-mini` models are now available for API access and model deployment. **For access to `o1` registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who previously applied and received access to `o1-preview`, don't need to reapply as they are automatically on the wait-list for the latest model.
+**For access to `o3-mini` and `o1` registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who previously applied and received access to `o1-preview`, or `o1`  don't need to reapply as they are automatically on the wait-list for the latest models in the o-series.
 
 Request access: [limited access model application](https://aka.ms/OAI/o1access)
 
-Once access has been granted, you will need to create a deployment for each model. If you have an existing `o1-preview` deployment in place upgrade is currently not supported, you will need to create a new deployment.
+Once access has been granted, you will need to create a deployment for each model. 
 
-To learn more about the advanced `o1` series models see, [getting started with o1 series reasoning models](../how-to/reasoning.md).
+To learn more about the advanced `o-series` models see, [getting started with reasoning models](../how-to/reasoning.md).
 
 ### Region availability
 
 | Model | Region |
 |---|---|
+|`o3-mini` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
 |`o1` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
 | `o1-preview` | See the [models table](#global-standard-model-availability). |
 | `o1-mini` | See the [models table](#global-provisioned-managed-model-availability). |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル情報の更新 / Model information updated"
}
```

### Explanation
この変更は、Azure OpenAIに関するドキュメントの内容を更新するためのマイナーアップデートです。主な変更として、日付フィールドが「2024年12月16日」から「2025年1月30日」に更新され、モデルの名称も「o1およびo1-miniモデル」から「oシリーズモデル」に変更されました。これにより、モデルの説明や特徴、情報がより具体的に適切に反映されるようになっています。

更新には、モデルのリストが具体的な情報を含む形で整理され、各モデルのID、説明、最大リクエスト数が明示されました。また、oシリーズモデルに関連する新しいアクセス要件が追加されました。これにより、ユーザーは最新のモデル情報を効果的に把握することができ、サービスの利用促進が期待されます。

## articles/ai-services/openai/how-to/create-resource.md{#item-c1c8a3}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: devx-track-azurecli, build-2023, build-2023-dataai, devx-track-azurepowershell
 ms.topic: how-to
-ms.date: 05/20/2024
+ms.date: 01/31/2025
 zone_pivot_groups: openai-create-resource
 author: mrbullwinkle
 ms.author: mbullwin
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付情報の更新 / Date information updated"
}
```

### Explanation
この変更は、Azure OpenAIリソースの作成に関するドキュメントの日付情報を更新するためのマイナーアップデートです。具体的には、`create-resource.md`ファイル内の`ms.date`フィールドが「2024年5月20日」から「2025年1月31日」に変更されました。この更新により、情報が最新のものとなり、ユーザーに現在の状況を反映した正確なデータを提供することが目的です。その他の内容には変更がありません。

## articles/ai-services/openai/how-to/dynamic-quota.md{#item-b774ca}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: mrbullwinkle
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 06/27/2024
+ms.date: 01/31/2025
 ms.author: mbullwin
 ---
 
@@ -54,9 +54,7 @@ To use dynamic quota, you must:
 
 ### Enable dynamic quota
 
-To activate dynamic quota for your deployment, you can go to the advanced properties in the resource configuration, and switch it on:
-
-:::image type="content" source="../media/how-to/dynamic-quota/dynamic-quota-new.png" alt-text="Screenshot of advanced configuration UI for deployments." lightbox="../media/how-to/dynamic-quota/dynamic-quota-new.png":::
+To activate dynamic quota for your deployment, you can go to the advanced properties in the resource configuration, and switch it on.
 
 Alternatively, you can enable it programmatically with Azure CLI's [`az rest`](/cli/azure/reference-index?view=azure-cli-latest#az-rest&preserve-view=true):
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付情報の更新と文章の簡略化 / Date information update and text simplification"
}
```

### Explanation
この変更は、Azure OpenAIのダイナミッククォータに関するドキュメントのマイナーアップデートです。主な変更点として、`ms.date`フィールドが「2024年6月27日」から「2025年1月31日」に更新されました。また、ダイナミッククォータを有効にする手順が簡略化され、画像参照が削除されて文章がより直接的になりました。この修正により、ユーザーは手順をより明確に理解でき、情報が最新のものとして提供されます。

## articles/ai-services/openai/how-to/function-calling.md{#item-32f8e0}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: mbullwin #delegenz
 ms.service: azure-ai-openai
 ms.custom: devx-track-python
 ms.topic: how-to
-ms.date: 01/17/2025
+ms.date: 01/30/2025
 manager: nitinme
 ---
 
@@ -45,14 +45,15 @@ Support for parallel function was first added in API version [`2023-12-01-previe
 ### Basic function calling with tools
 
 * All the models that support parallel function calling
+* `o3-mini` (`2025-01-31`)
 * `o1` (`2024-12-17`)
 * `gpt-4` (`0613`)
 * `gpt-4-32k` (`0613`)
 * `gpt-35-turbo-16k` (`0613`)
 * `gpt-35-turbo` (`0613`)
 
-> [!IMPORTANT]
-> There is a known issue with the `o1` model and the `tool_choice` parameter. Currently function calls that include the optional `tool_choice` parameter will fail. This page will be updated once the issue is resolved. For more information on what parameters are supported with the o1-series models see, the [reasoning models guide](./reasoning.md).
+> [!NOTE]
+> The `tool_choice` parameter is now supported with `o3-mini` and `o1`. For more information on what parameters are supported with the o-series models see, the [reasoning models guide](./reasoning.md).
 
 ## Single tool/function calling example
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付情報の更新とツールのサポート状況の変更 / Date information update and tool support status change"
}
```

### Explanation
この変更は、Azure OpenAIの関数呼び出しに関するドキュメントのマイナーアップデートです。主な変更点は、`ms.date`フィールドが「2025年1月17日」から「2025年1月30日」に更新されたことです。さらに、`o3-mini`モデルが新たに並列関数呼び出しをサポートすることが明記され、これにより使用可能なモデルのリストが更新されました。既知の問題に関する警告も改訂され、`tool_choice`パラメータが`o3-mini`および`o1`モデルでサポートされることが強調されています。これにより、ユーザーは最新の情報を基に、モデルとそのパラメータの互換性を理解しやすくなります。

## articles/ai-services/openai/how-to/manage-costs.md{#item-93c3f3}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.author: mbullwin
 ms.custom: subject-cost-optimization
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 05/08/2024
+ms.date: 01/31/2025
 ---
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付情報の更新 / Date information update"
}
```

### Explanation
この変更は、Azure OpenAIに関するコスト管理のドキュメントのマイナーアップデートです。主な変更点は、`ms.date`フィールドの更新で、日付が「2024年5月8日」から「2025年1月31日」に変更されました。この修正により、ドキュメントが最新の情報を反映するようになり、ユーザーはインフォメーションの正確性を保つことができます。

## articles/ai-services/openai/how-to/managed-identity.md{#item-1a0afd}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Provides guidance on how to set managed identity with Microsoft Entra ID
 ms.service: azure-ai-openai
 ms.topic: how-to 
-ms.date: 06/25/2024
+ms.date: 01/31/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付情報の更新 / Date information update"
}
```

### Explanation
この変更は、Azure OpenAIのManaged Identityに関するドキュメントのマイナーアップデートです。変更された内容は、文書内の`ms.date`フィールドの日付が「2024年6月25日」から「2025年1月31日」へと更新されたことです。この修正により、ドキュメントがより最新の情報を反映し、ユーザーに正確なガイダンスを提供することが可能となります。

## articles/ai-services/openai/how-to/migration-javascript.md{#item-19dac7}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: mbullwin
 ms.service: azure-ai-openai
 ms.custom: devx-track-python
 ms.topic: how-to
-ms.date: 07/11/2024
+ms.date: 01/31/2025
 manager: nitinme
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付情報の更新 / Date information update"
}
```

### Explanation
この変更は、JavaScriptに関するAzure OpenAIの移行手順に関するドキュメントのマイナーアップデートです。具体的には、`ms.date`フィールドの日付が「2024年7月11日」から「2025年1月31日」に変更されました。この修正は、ドキュメントの内容を最新のものに保つために行われ、ユーザーに対してより正確な情報を提供するようになります。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -1,21 +1,21 @@
 ---
 title: Azure OpenAI o1 series reasoning models
 titleSuffix: Azure OpenAI
-description: Learn how to use Azure OpenAI's advanced o1 series reasoning models
+description: Learn how to use Azure OpenAI's advanced o3-mini, o1, & o1-mini reasoning models 
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 01/16/2025
+ms.date: 01/30/2025
 author: mrbullwinkle    
 ms.author: mbullwin
 ---
 
 
 # Azure OpenAI reasoning models
 
-Azure OpenAI `o1` and `o1-mini` models are designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
+Azure OpenAI `o-series` models are designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
 
-**Key capabilities of the o1 series:**
+**Key capabilities of the o-series models:**
 
 - Complex Code Generation: Capable of generating algorithms and handling advanced coding tasks to support developers.
 - Advanced Problem Solving: Ideal for comprehensive brainstorming sessions and addressing multifaceted challenges.
@@ -24,45 +24,43 @@ Azure OpenAI `o1` and `o1-mini` models are designed to tackle reasoning and prob
 
 ## Availability
 
-The **o1 series** models are now available for API access and model deployment. **For access to o1, and o1-preview registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who previously applied and received access to `o1-preview`, don't need to reapply as they are automatically on the wait-list for the latest model.
+ **For access to `o3-mini`, `o1`, and `o1-preview`, registration is required, and access will be granted based on Microsoft's eligibility criteria**.
 
-Request access: [limited access model application](https://aka.ms/OAI/o1access)
+ Customers who previously applied and received access to `o1` or `o1-preview`, don't need to reapply as they are automatically on the wait-list for the latest model.
 
-Once access has been granted, you'll need to create a deployment for each model. If you have an existing `o1-preview` deployment, in-place upgrade is currently not supported, you'll need to create a new deployment.
+Request access: [limited access model application](https://aka.ms/OAI/o1access)
 
 ### Region availability
 
 | Model | Region | Limited access |
 |---|---|---|
+| `o3-mini` | East US2 (Global Standard) <br> Sweden Central (Global Standard) | [Limited access model application](https://aka.ms/OAI/o1access) |
 |`o1` | East US2 (Global Standard) <br> Sweden Central (Global Standard) | [Limited access model application](https://aka.ms/OAI/o1access) |
 | `o1-preview` | See [models page](../concepts/models.md#global-standard-model-availability). | [Limited access model application](https://aka.ms/OAI/o1access) |
 | `o1-mini` | See [models page](../concepts/models.md#global-standard-model-availability). | No access request needed |
 
 ## API & feature support
 
-| **Feature**     | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   |
-|:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|
-| **API Version**       | `2024-12-01-preview` | `2024-09-01-preview`  <br> `2024-10-01-preview` <br> `2024-12-01-preview`    | `2024-09-01-preview`  <br> `2024-10-01-preview` <br> `2024-12-01-preview`    |
-| **[Developer Messages](#developer-messages)** | ✅ | - | - |
-| **[Structured Outputs](./structured-outputs.md)** | ✅ | - | - |
-| **[Context Window](../concepts/models.md#o1-and-o1-mini-models)** | Input: 200,000 <br> Output: 100,000 | Input: 128,000  <br> Output: 32,768 | Input: 128,000  <br> Output: 65,536 |
-| **[Reasoning effort](#reasoning-effort)** | ✅ | - | - |
-| **[Vision Support](./gpt-with-vision.md)** |✅ | - | - |
-| Functions/Tools | ✅  | -  |  - |
-| `max_completion_tokens` |✅ |✅ |✅ |
-| System Messages | - | - | - |
-
-**o1 series** models will only work with the `max_completion_tokens` parameter.
-
-> [!IMPORTANT]
-> There is a known issue with the `o1` model and the `tool_choice` parameter. Currently function calls that include the optional `tool_choice` parameter will fail. This page will be updated once the issue is resolved.
+| **Feature**     | **o3-mini**, **2025-01-31**  |**o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   |
+|:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|:---:|
+| **API Version**    | `2024-12-01-preview` <br> `2025-01-01-preview`   | `2024-12-01-preview` <br> `2025-01-01-preview` | `2024-09-01-preview`  <br> `2024-10-01-preview` <br> `2024-12-01-preview`    | `2024-09-01-preview`  <br> `2024-10-01-preview` <br> `2024-12-01-preview`    |
+| **[Developer Messages](#developer-messages)** | ✅ | ✅ | - | - |
+| **[Structured Outputs](./structured-outputs.md)** | ✅ | ✅ | - | - |
+| **[Context Window](../concepts/models.md#o-series-models)** | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 128,000  <br> Output: 32,768 | Input: 128,000  <br> Output: 65,536 |
+| **[Reasoning effort](#reasoning-effort)** | ✅ | ✅ | - | - |
+| **[Vision Support](./gpt-with-vision.md)** | - | ✅ | - | - |
+| Functions/Tools | ✅  | ✅  |  - | - |
+| `max_completion_tokens`<sup>*</sup> |✅ |✅ |✅ | ✅ |
+| System Messages<sup>**</sup> | ✅ | ✅ | - | - |
+| Streaming | ✅ | - | - | - |
+
+<sup>*</sup> Reasoning models will only work with the `max_completion_tokens` parameter. <br><br>
+<sup>**</sup>The latest o<sup>&#42;</sup> series model support system messages to make migration easier. When you use a system message with `o3-mini` and `o1` it will be treated as a developer message. You should not use both a developer message and a system message in the same API request.
 
 ### Not Supported
 
-The following are currently unsupported with o1-series models:
+The following are currently unsupported with reasoning models:
 
-- System Messages
-- Streaming
 - Parallel tool calling
 - `temperature`, `top_p`, `presence_penalty`, `frequency_penalty`, `logprobs`, `top_logprobs`, `logit_bias`, `max_tokens`
 
@@ -241,10 +239,7 @@ print(response.model_dump_json(indent=2))
 
 ## Developer messages
 
-Functionally developer messages ` "role": "developer"` are the same as system messages.
-
-- **System messages are not supported** with the **o1 series** reasoning models. 
-- `o1-2024-12-17` with API version: `2024-12-01-preview` and later adds support for developer messages. 
+Functionally developer messages ` "role": "developer"` are the same as system messages. 
 
 Adding a developer message to the previous code example would look as follows:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル情報の更新と追加 / Update and addition of model information"
}
```

### Explanation
この変更は、Azure OpenAIの推論モデルに関するドキュメントのマイナーアップデートです。具体的には、`o1`および`o1-mini`モデルに関する言及が`o-series`モデルに変更され、モデル名が拡張されました。新しい`o3-mini`モデルが追加され、これに関連する新しい情報が含まれています。また、文書内の`ms.date`が「2025年1月16日」から「2025年1月30日」に更新されています。これにより、ユーザーは最新のモデルとアクセス情報を得ることができ、より明確な指針を提供することが目的です。全体的に、文書内容が改善され、モデルの機能や提供情報が更新されていることが反映されています。

## articles/ai-services/openai/how-to/structured-outputs.md{#item-cc2557}

<details>
<summary>Diff</summary>
````diff
@@ -24,6 +24,7 @@ Structured outputs make a model follow a [JSON Schema](https://json-schema.org/o
 
 ## Supported models
 
+- `o3-mini` version `2025-01-31`
 - `o1` version: `2024-12-17`
 - `gpt-4o-mini` version: `2024-07-18`
 - `gpt-4o` version: `2024-08-06`
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サポートされるモデルに関する情報の追加 / Addition of information regarding supported models"
}
```

### Explanation
この変更は、Azure OpenAIの構造化出力に関するドキュメントのマイナーアップデートです。具体的には、サポートされるモデルのリストに新たに`o3-mini`モデルのバージョン「2025年1月31日」が追加されました。この更新により、ユーザーは最新のモデル対応状況を把握し、利用可能な機能を確認することができるようになります。文書の内容を最新に保つために重要な修正であり、他のモデル情報も明確に提示されています。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -7,20 +7,20 @@ author: mrbullwinkle
 ms.author: mbullwin
 ms.service: azure-ai-openai
 ms.topic: overview
-ms.date: 01/23/2025
+ms.date: 01/30/2025
 ms.custom: build-2023, build-2023-dataai
 recommendations: false
 ---
 
 # What is Azure OpenAI Service?
 
-Azure OpenAI Service provides REST API access to OpenAI's powerful language models including o1, o1-mini, GPT-4o, GPT-4o mini, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, image understanding, semantic search, and natural language to code translation. Users can access the service through REST APIs, Python SDK, or in the [Azure AI Foundry](https://ai.azure.com).
+Azure OpenAI Service provides REST API access to OpenAI's powerful language models including o3-mini, o1, o1-mini, GPT-4o, GPT-4o mini, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, image understanding, semantic search, and natural language to code translation. Users can access the service through REST APIs, Python SDK, or in the [Azure AI Foundry](https://ai.azure.com).
 
 ### Features overview
 
 | Feature | Azure OpenAI |
 | --- | --- |
-| Models available | [**o1**](./how-to/reasoning.md) - (Limited Access - [Request Access](https://aka.ms/OAI/o1access))<br>[**o1-mini**](./how-to/reasoning.md)<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
+| Models available | [**o3-mini & o1**](./how-to/reasoning.md) - (Limited Access - [**Request Access**](https://aka.ms/OAI/o1access))<br>[**o1-mini**](./how-to/reasoning.md)<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
 | Fine-tuning | `GPT-4o-mini` (preview) <br> `GPT-4` (preview) <br>`GPT-3.5-Turbo` (0613) <br> `babbage-002` <br> `davinci-002`.|
 | Price | [Available here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> For details on vision-enabled chat models, see the [special pricing information](../openai/concepts/gpt-with-vision.md#special-pricing-information).|
 | Virtual network support & private link support | Yes.  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス概要に新しいモデル情報の追加 / Addition of new model information in service overview"
}
```

### Explanation
この変更は、Azure OpenAI Serviceに関する概要ドキュメントのマイナーアップデートです。主な変更点として、使用できるモデルのリストに新たに`o3-mini`モデルが追加され、これにより最新の技術情報が反映されています。また、文書内の日付が「2025年1月23日」から「2025年1月30日」に更新され、これにより情報のタイムリーさが保たれています。その他の情報は変更されておらず、サービスの機能や利用方法に関する詳細は引き続き提供されています。この修正により、ユーザーは新たに利用可能なモデルを認識し、より幅広い機能を活用することができるようになります。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 1/17/2025
+ms.date: 1/30/2025
 ms.author: mbullwin
 ---
 
@@ -62,25 +62,28 @@ The following sections provide you with a quick guide to the default quotas and
 
 [!INCLUDE [Quota](./includes/global-batch-limits.md)]
 
-## o1 & o1-mini rate limits
+## `o-series` rate limits
 
 > [!IMPORTANT]
 > The ratio of RPM/TPM for quota with o1-series models works differently than older chat completions models:
 >
 > - **Older chat models:** 1 unit of capacity = 6 RPM and 1,000 TPM.
 > - **o1 & o1-preview:** 1 unit of capacity = 1 RPM and 6,000 TPM.
+> - **o3-mini:** 1 unit of capacity = 1 RPM per 10,000 TPM.
 > - **o1-mini:** 1 unit of capacity = 1 RPM per 10,000 TPM.
 >
 > This is particularly important for programmatic model deployment as this change in RPM/TPM ratio can result in accidental under allocation of quota if one is still assuming the 1:1000 ratio followed by older chat completion models.
 >
 > There is a known issue with the [quota/usages API](/rest/api/aiservices/accountmanagement/usages/list?view=rest-aiservices-accountmanagement-2024-06-01-preview&tabs=HTTP&preserve-view=true) where it assumes the old ratio applies to the new o1-series models. The API returns the correct base capacity number, but doesn't apply the correct ratio for the accurate calculation of TPM.
 
-### o1 & o1-mini global standard
+### `o-series` global standard
 
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
 |---|---|:---:|:---:|
+| `o3-mini` | Enterprise agreement | 50 M | 5 K |
 | `o1` & `o1-preview` | Enterprise agreement | 30 M | 5 K |
 | `o1-mini`| Enterprise agreement | 50 M | 5 K |
+| `o3-mini` | Default | 5 M | 500 |
 | `o1` & `o1-preview` | Default | 3 M | 500 |
 | `o1-mini`| Default | 5 M | 500 |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータおよびレート制限に関する情報の更新 / Update of quota and rate limit information"
}
```

### Explanation
この変更は、Azure OpenAIのクォータと制限に関するドキュメントのマイナーアップデートです。主な変更点には、日付の更新が含まれており、情報が「2025年1月17日」から「2025年1月30日」に修正されています。また、`o1`および`o1-mini`モデルのレート制限が`o-series`という新しい名前に集約され、これにより新たに`o3-mini`モデルのレート制限も追加されました。

具体的には、`o3-mini`モデルのリクエスト制限が「1ユニットの容量 = 1 RPM（Requests Per Minute）あたり10,000 TPM（Tokens Per Minute）」と定義され、他のモデルに関する情報も一元的に整理されました。この変更により、異なるモデル間のクォータの理解が容易になり、プログラムによるモデル展開の際の誤ったクォータ配分を避ける手助けとなります。全体として、ユーザーにとって重要な最新情報が反映されています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: whats-new
-ms.date: 1/21/2025
+ms.date: 1/30/2025
 recommendations: false
 ---
 
@@ -21,6 +21,10 @@ This article provides a summary of the latest releases and major documentation u
 
 ## January 2025
 
+### o3-mini released
+
+`o3-mini` (2025-01-31) is the latest reasoning model, offering enhanced reasoning abilities. For more information, see our [reasoning model guide](./how-to/reasoning.md).
+
 ### GPT-4o audio completions
 
 The `gpt-4o-audio-preview` model is now available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability). Use the `gpt-4o-audio-preview` model for audio generation.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新情報にo3-miniのリリース追加 / Addition of o3-mini release in What's New"
}
```

### Explanation
この変更は、Azure OpenAIに関する最新情報の記事のマイナーアップデートです。具体的には、日付が「2025年1月21日」から「2025年1月30日」に更新されたほか、新しく`o3-mini`モデルのリリース情報が追加されました。

`o3-mini`は2025年1月31日にリリースされた最新の推論モデルであり、強化された推論能力を提供します。このモデルに関する詳細は、関連する[推論モデルガイド](./how-to/reasoning.md)で確認できます。

また、`gpt-4o-audio-preview`モデルがEast US 2およびSweden Central地域でグローバル展開のために利用可能になった旨の情報も維持されています。この更新により、ユーザーは新しいモデルや機能について最新の情報を得られるようになるため、特に開発者や技術者にとって重要な内容です。


