---
date: '2025-04-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:81ad672...MicrosoftDocs:dad2f57
summary: このコードの変更は、Azure OpenAIサービスに関するドキュメントのモデル情報の更新と新モデルの追加に焦点を当てています。新たに導入されたモデル`o4-mini`と`o3`が追加され、既存モデルの情報も強化されています。これにより、利用者は最新のAI機能を利用できるようになります。具体的には、新モデルに関する情報や、今後のAPIサポートについても予告されています。また、文書の構造や情報が見直され、情報提供がより明確になっています。全体として、これらの変更はユーザーがより効率的に情報を検索し、Azure
  OpenAIサービスを活用しやすくすることを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:81ad672...MicrosoftDocs:dad2f57){target="_blank"}

<format>
# ハイライト
このコードの変更は、Azure OpenAIサービスに関するドキュメントにおけるモデル情報の更新と新しいモデルの追加が主な焦点です。新モデル`o4-mini`と`o3`の導入、および既存モデルの情報強化が行われ、ユーザーに最新のAI機能を提供するための重要な内容更新がされています。

## 新機能
- `o4-mini`と`o3`の新しい推論モデルを含む、いくつかの新モデルが追加され、それぞれの機能やトレーニングデータに関する情報が提供されました。
- 新モデルに関しては、今後提供予定のチャット完了APIやレスポンスAPIのサポートも予告されています。

## 破壊的変更
特に破壊的な変更は報告されていませんが、モデル情報の除去や順序変更が行われる可能性などに注意が必要です。

## その他の更新
- 各ドキュメントの日付が更新され、最新版であることが反映されています。
- ドキュメントのテーブル形式や説明内容が見直され、より明確で整理された情報提供となっています。
- それぞれのモデルに関連するクォータや制限に関する詳細が更新され、正確なリソース管理が可能になりました。

# 洞察
この一連の変更は、Azure OpenAIサービスの利用者がより最新の、そしてより良く整理された情報へアクセスすることを可能にするためのものです。以下は、この更新が技術的にどのような意味を持つのかについての洞察です。

まず、新しいモデルである`o4-mini`と`o3`の追加は、Azure OpenAIサービスにおける推論能力の向上に寄与します。これらのモデルは、より高度なテキストと画像の処理能力を有しており、また構造化出力や新しいAPIサポートの準備が進んでいることから、多様なアプリケーションニーズに応えることが可能です。

ドキュメンテーション内でのテーブルの再整備や情報の拡充は、ユーザーエクスペリエンスの向上を狙った重要な変更です。ユーザーはより効率的に情報を検索し、利用可能なサービスの概要を迅速に把握することができます。具体的には、どのモデルがどの地理的領域で利用可能か、あるいはモデルのクォータ制限やサポートされる機能が何か、といった点を一目で確認できるようになるため、開発者にとって非常に便利です。

さらに、これらの変更は、ユーザーに新しいモデルの即時利用を誘発する狙いがあり、新しいテクノロジーへの迅速な移行を支援することで、AzureによるAIソリューションの採用を促進します。これによって、利用者はより豊富な機能をもったAIを活用することで、より付加価値のあるアプリケーションを開発する機会を得られるでしょう。

</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | モデル情報の更新と新機能の追加 | modified | 8 | 4 | 12 | 
| [function-calling.md](#item-32f8e0) | minor update | 関数呼び出しに関するドキュメントの最新情報 | modified | 6 | 3 | 9 | 
| [reasoning.md](#item-a54b2f) | minor update | 推論モデルに関するドキュメントの拡充 | modified | 21 | 16 | 37 | 
| [responses.md](#item-b9757d) | minor update | レスポンスAPIのモデル情報の追加 | modified | 1 | 0 | 1 | 
| [structured-outputs.md](#item-cc2557) | minor update | 構造化出力に関連するモデル情報の更新 | modified | 5 | 2 | 7 | 
| [standard-global.md](#item-17a84b) | minor update | モデルの行列情報の更新 | modified | 26 | 26 | 52 | 
| [overview.md](#item-97d507) | minor update | Azure OpenAI Service の概要の更新 | modified | 3 | 3 | 6 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータと制限の更新 | modified | 8 | 0 | 8 | 
| [whats-new.md](#item-53303b) | minor update | 新しいモデルの追加情報の更新 | modified | 5 | 1 | 6 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 04/15/2025
+ms.date: 04/16/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -43,7 +43,7 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 
 |  Model ID  | Description | Context Window | Max Output Tokens | Training Data (up to)  |
 |  --- |  :--- |:--- |:---|:---: |
-| `gpt-4.1` (2025-04-14) <br> <br> **Latest model from Azure OpenAI**  | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | 1,047,576 | 32,768 | May 31, 2024 |
+| `gpt-4.1` (2025-04-14)   | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | 1,047,576 | 32,768 | May 31, 2024 |
 | `gpt-4.1-nano` (2025-04-14) <br><br> **Fastest 4.1 model** | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | 1,047,576  | 32,768 | May 31, 2024 |
 | `gpt-4.1-mini` (2025-04-14) | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | 1,047,576  | 32,768 | May 31, 2024 |
 
@@ -99,8 +99,10 @@ The Azure OpenAI o<sup>&#42;</sup> series models are specifically designed to ta
 
 |  Model ID  | Description | Max Request (tokens) | Training Data (up to)  |
 |  --- |  :--- |:--- |:---: |
-| `o3-mini` (2025-01-31) | The latest reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text-only processing <br> - Functions/Tools  | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
-| `o1` (2024-12-17) | The most capable model in the o1 series, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
+| `o4-mini` (2025-04-16) | - **NEW** reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br><br> - Chat Completions API <br> - [Responses API](../how-to/responses.md) (**Feature coming soon!**)  <br>- Structured outputs<br> - Text, image processing <br> - Functions/Tools/Parallel tool calling <br> [Full summary of capabilities](../how-to/reasoning.md) | Input: 200,000 <br> Output: 100,000 | May 31, 2024 |   
+| `o3` (2025-04-16) | - **NEW** reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br>  <br> - Chat Completions API <br> - [Responses API](../how-to/responses.md) (**Feature coming soon!**) <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools/Parallel tool calling <br> [Full summary of capabilities](../how-to/reasoning.md) | Input: 200,000 <br> Output: 100,000 | May 31, 2024 |    
+| `o3-mini` (2025-01-31) | - [Enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text-only processing <br> - Functions/Tools | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
+| `o1` (2024-12-17) | - [Enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
 |`o1-preview` (2024-09-12) | Older preview version | Input: 128,000  <br> Output: 32,768 | Oct 2023 |
 | `o1-mini` (2024-09-12) | A faster and more cost-efficient option in the o1 series, ideal for coding tasks requiring speed and lower resource consumption. <br><br> Global standard deployment available by default. <br> <br> Standard (regional) deployments are currently only available for select customers who received access as part of the `o1-preview` limited access release.  | Input: 128,000  <br> Output: 65,536 | Oct 2023 |
 
@@ -112,6 +114,8 @@ To learn more about the advanced `o-series` models see, [getting started with re
 
 | Model | Region |
 |---|---|
+|`o4-mini`|  East US2 (Global Standard) <br> Sweden Central (Global Standard)  |
+| `o3` |  East US2 (Global Standard) <br> Sweden Central (Global Standard)  |
 |`o3-mini` | See the [models table](#model-summary-table-and-region-availability). |
 |`o1` | See the [models table](#model-summary-table-and-region-availability). |
 | `o1-preview` | See the [models table](#model-summary-table-and-region-availability). This model is only available for customers who were granted access as part of the original limited access |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル情報の更新と新機能の追加"
}
```

### Explanation
このコードの差分は、Azure OpenAIサービスに関するドキュメントについてのものです。具体的には、モデルの情報が更新され、新しいモデルが追加されました。以下のような変更が含まれています。

- **日付の更新**: `ms.date`フィールドが2025年4月15日から2025年4月16日に変更されました。これはドキュメントの更新日を示しています。
- **モデル情報の修正**: `gpt-4.1`モデルの情報から文言が修正され、表示が整理されました。
- **新しいモデルの追加**:
  - `o4-mini`および`o3`という2つの新しい推論モデルが追加され、それぞれの機能やトレーニングデータについての詳細が提供されています。これらのモデルは、テキスト・画像処理機能、構造化出力、チャット完了API、レスポンスAPI（近日機能追加予定）に対応しています。
- **既存モデルの説明の強化**: 既存のモデルについても、より明確な説明が加えられ、ユーザーがそれぞれのモデルの機能を理解しやすくなっています。

これらの変更は、AzureのAIサービスが進化していることを反映しており、ユーザーに新しい機能や改善点を伝えることを目的としています。

## articles/ai-services/openai/how-to/function-calling.md{#item-32f8e0}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: mbullwin #delegenz
 ms.service: azure-ai-openai
 ms.custom: devx-track-python
 ms.topic: how-to
-ms.date: 04/14/2025
+ms.date: 04/16/2025
 manager: nitinme
 ---
 
@@ -40,8 +40,11 @@ At a high level you can break down working with functions into three steps:
 * `gpt-4o` (`2024-11-20`)
 * `gpt-4o-mini` (`2024-07-18`)
 * `gpt-4.5-preview` (`2025-02-27`)
-* `gpt-4.1` (`2025-14-2025`)
-* `gpt-4.1-nano` (`2025-14-2025`)
+* `gpt-4.1` (`2025-04-14`)
+* `gpt-4.1-nano` (`2025-04-14`)
+* `gpt-4.1-mini` (`2025-04-14`)
+* `o4-mini` (`2025-04-16`)
+* `o3` (`2025-04-16`)
 
 Support for parallel function was first added in API version [`2023-12-01-preview`](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2023-12-01-preview/inference.json)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "関数呼び出しに関するドキュメントの最新情報"
}
```

### Explanation
このコードの差分は、Azure OpenAIの「関数呼び出し」に関するドキュメントに対するもので、いくつかの重要な更新が行われました。以下はその要点です。

- **日付の更新**: `ms.date`フィールドが2025年4月14日から2025年4月16日に変更され、最新の日付が反映されました。
- **モデル情報の整理**: 既存のモデルのリストが整理され、日付が正しく表記されました。具体的には、`gpt-4.1`、`gpt-4.1-nano`、および新たに追加された`gpt-4.1-mini`モデルが2025年4月14日として修正され、さらに新しい`o4-mini`および`o3`モデルが追加され、それぞれの日付も2025年4月16日として記載されています。
- **内容の拡充**: 関数を使用する際の手順を解説するセクションが明確にされ、関連する情報が強化されました。

これらの変更は、ユーザーが関数呼び出しを行う際に必要な最新情報を提供し、新しいモデルの利用可能性を明確にすることを目的としています。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's advanced o3-mini, o1, & o1-mini rea
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 03/07/2025
+ms.date: 04/16/2025
 author: mrbullwinkle    
 ms.author: mbullwin
 ---
@@ -28,37 +28,42 @@ Azure OpenAI `o-series` models are designed to tackle reasoning and problem-solv
 
 | Model | Region | Limited access |
 |---|---|---|
+| `o4-mini`  | East US2 (Global Standard) <br><br> Sweden Central (Global Standard)   | No access request needed to use the core capabilities of this model.<br><br> Request access: [o4-mini reasoning summary feature](https://aka.ms/oai/o3access)     |
+| `o3` |  East US2 (Global Standard) <br><br> Sweden Central (Global Standard)     | Request access: [o3 limited access model application](https://aka.ms/oai/o3access)     |
 | `o3-mini` | [Model availability](../concepts/models.md#global-standard-model-availability).  | Access is no longer restricted for this model.   |
 |`o1` | [Model availability](../concepts/models.md#global-standard-model-availability).  | Access is no longer restricted for this model.  |
 | `o1-preview` | [Model availability](../concepts/models.md#global-standard-model-availability). |This model is only available for customers who were granted access as part of the original limited access release. We're currently not expanding access to `o1-preview`. |
 | `o1-mini` | [Model availability](../concepts/models.md#global-standard-model-availability). | No access request needed for Global Standard deployments.<br><br>Standard (regional) deployments are currently only available to select customers who were previously granted access as part of the `o1-preview` release.|
 
 ## API & feature support
 
-| **Feature**     | **o3-mini**, **2025-01-31**  |**o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   |
-|:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|:---:|
-| **API Version**    | `2024-12-01-preview` or later <br> `2025-03-01-preview` (Recommended)   | `2024-12-01-preview` or later <br> `2025-03-01-preview` (Recommended) | `2024-09-01-preview` or later <br> `2025-03-01-preview` (Recommended)    | `2024-09-01-preview` or later <br> `2025-03-01-preview` (Recommended)    |
-| **[Developer Messages](#developer-messages)** | ✅ | ✅ | - | - |
-| **[Structured Outputs](./structured-outputs.md)** | ✅ | ✅ | - | - |
-| **[Context Window](../concepts/models.md#o-series-models)** | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 128,000  <br> Output: 32,768 | Input: 128,000  <br> Output: 65,536 |
-| **[Reasoning effort](#reasoning-effort)** | ✅ | ✅ | - | - |
-| **[Vision Support](./gpt-with-vision.md)** | - | ✅ | - | - |
-| Functions/Tools | ✅  | ✅  |  - | - |
-| `max_completion_tokens`<sup>*</sup> |✅ |✅ |✅ | ✅ |
-| System Messages<sup>**</sup> | ✅ | ✅ | - | - |
-| Streaming | ✅ | - | - | - |
+| **Feature**     | **o4-mini**, **2025-04-16**  | **o3**, **2025-04-16** | **o3-mini**, **2025-01-31**  |**o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   |
+|:-------------------|:--------------------------:|:-----:|:-------:|:--------------------------:|:-------------------------------:|:---:|
+| **API Version**    | `2025-03-01-preview`   | `2025-03-01-preview`   | `2024-12-01-preview` or later <br> `2025-03-01-preview` (Recommended)   | `2024-12-01-preview` or later <br> `2025-03-01-preview` (Recommended) | `2024-09-01-preview` or later <br> `2025-03-01-preview` (Recommended)    | `2024-09-01-preview` or later <br> `2025-03-01-preview` (Recommended)    |
+| **[Developer Messages](#developer-messages)** | ✅ | ✅ | ✅ | ✅ | - | - |
+| **[Structured Outputs](./structured-outputs.md)** | ✅ | ✅ | ✅ | ✅ | - | - |
+| **[Context Window](../concepts/models.md#o-series-models)** | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 128,000  <br> Output: 32,768 | Input: 128,000  <br> Output: 65,536 |
+| **[Reasoning effort](#reasoning-effort)** | ✅| ✅ |✅ | ✅ | - | - |
+| **[Vision Support](./gpt-with-vision.md)** | ✅ | ✅ | - | ✅ | - | - |
+| Chat Completions API | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
+| Responses API | ✅ (**Feature coming soon!**) | ✅ (**Feature coming soon!**) | - | - | - | - |
+| Functions/Tools | ✅ | ✅ | ✅  | ✅  |  - | - |
+| Parallel Tool Calls | ✅ | ✅ | -  | -  |  - | - |
+| `max_completion_tokens`<sup>*</sup> | ✅ | ✅ |✅ |✅ |✅ | ✅ |
+| System Messages<sup>**</sup> | ✅ | ✅ | ✅ | ✅ | - | - |
+| Reasoning summary <sup>***</sup> | ✅ (**Feature coming soon!**) | ✅ (**Feature coming soon!**) | -  | -  |  - | - |
+| Streaming | ✅ | ✅ | ✅ | - | - | - |
 
 <sup>*</sup> Reasoning models will only work with the `max_completion_tokens` parameter. <br><br>
 
-<sup>**</sup>The latest o<sup>&#42;</sup> series model support system messages to make migration easier. When you use a system message with `o3-mini` and `o1` it will be treated as a developer message. You should not use both a developer message and a system message in the same API request.
-
+<sup>**</sup>The latest o<sup>&#42;</sup> series model support system messages to make migration easier. When you use a system message with `o4-mini`, `o3`, `o3-mini`, and `o1` it will be treated as a developer message. You should not use both a developer message and a system message in the same API request.
 
+<sup>***</sup> Access to the chain-of-thought reasoning summary is limited access only for `o4-mini`. 
 
 ### Not Supported
 
 The following are currently unsupported with reasoning models:
 
-- Parallel tool calling
 - `temperature`, `top_p`, `presence_penalty`, `frequency_penalty`, `logprobs`, `top_logprobs`, `logit_bias`, `max_tokens`
 
 ## Usage
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "推論モデルに関するドキュメントの拡充"
}
```

### Explanation
このコードの差分は、Azure OpenAIの推論機能に関するドキュメントの更新に関するものです。以下の重要な変更点が含まれています。

- **日付の更新**: `ms.date`フィールドが2025年3月7日から2025年4月16日に変更され、最新の日付が反映されました。
- **モデル情報の追加と整理**: `o4-mini`および`o3`という新しいモデルが追加され、それぞれの利用可能な地域やアクセス要件が明記されました。これにより、ユーザーは新しいモデルを使用するためのアクセス情報をより理解しやすくなります。
- **APIと機能サポートの明確化**: 新しいテーブル形式で各モデルの対応APIバージョンやサポートされる機能が整理され、どのモデルがどの機能をサポートするかが明確になりました。これにより、開発者が期待する機能の利用可能性をすぐに確認できます。
- **新機能の予告**: 一部のモデル（特に`o4-mini`と`o3`）については、「今後提供予定の機能」としてチャット完了APIおよびレスポンスAPIのサポートが記載されています。

これらの変更は、Azure OpenAIの推論モデルをより効果的に利用できるようにするための重要な更新を反映しています。

## articles/ai-services/openai/how-to/responses.md{#item-b9757d}

<details>
<summary>Diff</summary>
````diff
@@ -45,6 +45,7 @@ The responses API is currently available in the following regions:
 - `computer-use-preview`
 - `gpt-4.1` (Version: `2025-04-14`)
 - `gpt-4.1-nano` (Version: `2025-04-14`)
+- `gpt-4.1-mini` (Version: `2025-04-14`)
 
 Not every model is available in the regions supported by the responses API. Check the [models page](../concepts/models.md) for model region availability.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レスポンスAPIのモデル情報の追加"
}
```

### Explanation
このコードの差分は、Azure OpenAIのレスポンスAPIに関連するドキュメントの更新です。主な変更点は以下の通りです。

- **モデルの追加**: 新たに`gpt-4.1-mini`モデルがレスポンスAPIの対応モデルリストに追加されました。これにより、`gpt-4.1-mini`モデルのバージョンが2025年4月14日として明記され、ユーザーはこのモデルの利用可能性に関する情報を得ることができます。

この変更は、ユーザーがレスポンスAPIを使用する際のモデル選択肢を広げ、最新のモデル情報を提供することを目的としています。

## articles/ai-services/openai/how-to/structured-outputs.md{#item-cc2557}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 04/14/2025
+ms.date: 04/16/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -32,7 +32,10 @@ Structured outputs make a model follow a [JSON Schema](https://json-schema.org/o
 - `gpt-4o` version: `2024-08-06`
 - `gpt-4o` version: `2024-11-20`
 - `gpt-4.1` version `2025-04-14`
-- `gpt-4.1-nano` version (`2025-14-2025`)
+- `gpt-4.1-nano` version `2025-04-14`
+- `gpt-4.1-mini` version: `2025-04-14`
+- `o4-mini` version: `2025-04-16`
+- `o3` version: `2025-04-16`
 
 ## API support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "構造化出力に関連するモデル情報の更新"
}
```

### Explanation
このコードの差分は、Azure OpenAIの構造化出力に関するドキュメントの更新を示しています。主な変更点は以下の通りです。

- **日付の更新**: `ms.date`フィールドが2025年4月14日から2025年4月16日に変更され、最新の日付が正しく反映されました。
- **モデル情報の修正と追加**: `gpt-4.1-nano`モデルのバージョンが修正され、正確なバージョンが`2025-04-14`として明記されました。また、`gpt-4.1-mini`および新たに追加された`o4-mini`、`o3`モデルのバージョンもそれぞれ`2025-04-14`および`2025-04-16`として追加されました。

これらの変更により、ユーザーは構造化出力に関連する利用可能なモデルの最新情報を取得できるようになり、正確なバージョン管理が強化されます。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -9,29 +9,29 @@ ms.custom: references_regions
 ms.date: 04/14/2025
 ---
 
-| **Region**     | **gpt-4.1**, **2025-04-14**   | **gpt-4.5-preview**, **2025-02-27**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4o-audio-preview**, **2024-12-17**   | **gpt-4o-mini-realtime-preview**, **2024-12-17**   | **gpt-4o-mini-audio-preview**, **2024-12-17**   | **gpt-4**, **turbo-2024-04-09**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **2**   |
-|:-------------------|:---------------------------:|:-----------------------------------:|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:----------------------------------------:|:------------------------------------------------:|:---------------------------------------------:|:-------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|
-| australiaeast      | -                       | -                               | ✅                        | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| brazilsouth        | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| canadaeast         | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| eastus             | -                       | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | ✅                                          | ✅                            | ✅                              | ✅                              | ✅                              |
-| eastus2            | ✅                        | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | ✅                                          | ✅                            | ✅                              | ✅                              | ✅                              |
-| francecentral      | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| germanywestcentral | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| italynorth         | -                       | -                               | ✅                        | ✅                   | -                          | -                       | -                      | -                      | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | -                           | ✅                              | ✅                              | ✅                              |
-| japaneast          | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| koreacentral       | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| northcentralus     | -                       | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| norwayeast         | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| polandcentral      | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| southafricanorth   | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| southcentralus     | -                       | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| southindia         | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| spaincentral       | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| swedencentral      | ✅                        | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| switzerlandnorth   | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| uaenorth           | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| uksouth            | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| westeurope         | -                       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
-| westus             | -                       | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| westus3            | -                       | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| **Region**     | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-nano**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **gpt-4.5-preview**, **2025-02-27**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **turbo-2024-04-09**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **2**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4o-audio-preview**, **2024-12-17**   | **gpt-4o-mini-realtime-preview**, **2024-12-17**   | **gpt-4o-mini-audio-preview**, **2024-12-17**   | **gpt-4o-transcribe**, **2025-03-20**   | **gpt-4o-mini-tts**, **2025-03-20**   | **gpt-4o-mini-transcribe**, **2025-03-20**   |
+|:-------------------|:---------------------------:|:--------------------------------:|:--------------------------------:|:-----------------------------------:|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:-------------------------------------------:|:----------------------------------------:|:------------------------------------------------:|:---------------------------------------------:|:-------------------------------------:|:-----------------------------------:|:------------------------------------------:|
+| australiaeast      | -                       | -                            | -                            | -                               | ✅                        | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| brazilsouth        | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| canadaeast         | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| eastus             | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | ✅                                          | -                                 | -                               | -                                      |
+| eastus2            | ✅                        | ✅                             | ✅                             | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | ✅                                        | ✅                                     | ✅                                             | ✅                                          | ✅                                  | ✅                                | ✅                                       |
+| francecentral      | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| germanywestcentral | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| italynorth         | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | -                      | -                      | ✅                       | ✅                            | -                           | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| japaneast          | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| koreacentral       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | -                             | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| northcentralus     | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| norwayeast         | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| polandcentral      | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| southafricanorth   | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| southcentralus     | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| southindia         | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| spaincentral       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| swedencentral      | ✅                        | ✅                             | ✅                             | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | ✅                                        | ✅                                     | ✅                                             | -                                         | -                                 | -                               | -                                      |
+| switzerlandnorth   | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| uaenorth           | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| uksouth            | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| westeurope         | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| westus             | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| westus3            | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの行列情報の更新"
}
```

### Explanation
このコードの差分は、Azure OpenAIにおける標準グローバルモデルの行列情報が更新されたことを示しています。主な変更点は以下の通りです。

- **モデルの追加と修正**: 表に新たに`gpt-4.1-nano`、`gpt-4.1-mini`、`gpt-4o-transcribe`、`gpt-4o-mini-tts`、`gpt-4o-mini-transcribe`モデルが追加され、対応するバージョンと地域が明示されています。
  
- **整形の変更**: 表の形式が見直され、各モデルとその利用可能地域がより明確に整理されました。具体的には、行に含まれる情報が整理され、地域ごとのモデルの利用可否が示されるようになっています。

- **更新日時の変更**: ドキュメント日付が更新され、最終更新日が正確に反映されているため、ユーザーは最新の情報を簡単に確認できます。

これにより、ユーザーは新しいモデルの利用可能性とそのバージョン情報を迅速に把握できるようになり、サービスがより効果的に利用できるようになります。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -7,20 +7,20 @@ author: mrbullwinkle
 ms.author: mbullwin
 ms.service: azure-ai-openai
 ms.topic: overview
-ms.date: 04/14/2025
+ms.date: 04/16/2025
 ms.custom: build-2023, build-2023-dataai
 recommendations: false
 ---
 
 # What is Azure OpenAI Service?
 
-Azure OpenAI Service provides REST API access to OpenAI's powerful language models including gpt-4.1, o3-mini, o1, o1-mini, GPT-4o, GPT-4o mini, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, image understanding, semantic search, and natural language to code translation. Users can access the service through REST APIs, [Python/C#/JS/Java/Go SDKs](/azure/ai-services/openai/supported-languages).
+Azure OpenAI Service provides REST API access to OpenAI's powerful language models including o4-mini, o3, gpt-4.1, o3-mini, o1, o1-mini, GPT-4o, GPT-4o mini, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, image understanding, semantic search, and natural language to code translation. Users can access the service through REST APIs, [Python/C#/JS/Java/Go SDKs](/azure/ai-services/openai/supported-languages).
 
 ### Features overview
 
 | Feature | Azure OpenAI |
 | --- | --- |
-| Models available | [gpt-4.1](./concepts/models.md#gpt-41-series) <br> [**computer-use-preview**](./concepts/models.md#computer-use-preview)<br>[**o3-mini & o1**](./how-to/reasoning.md) <br>[**o1-mini**](./how-to/reasoning.md)<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
+| Models available | [o4-mini & o3](./how-to/reasoning.md) <br>[gpt-4.1](./concepts/models.md#gpt-41-series) <br> [**computer-use-preview**](./concepts/models.md#computer-use-preview)<br>[**o3-mini & o1**](./how-to/reasoning.md) <br>[**o1-mini**](./how-to/reasoning.md)<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
 | Fine-tuning | `GPT-4o-mini` (preview) <br> `GPT-4` (preview) <br>`GPT-3.5-Turbo` (0613).|
 | Price | [Available here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> For details on vision-enabled chat models, see the [special pricing information](../openai/concepts/gpt-with-vision.md#special-pricing-information).|
 | Virtual network support & private link support | Yes.  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI Service の概要の更新"
}
```

### Explanation
このコードの差分は、Azure OpenAI Service の概要に関するドキュメントの更新を示しています。主な変更点は以下の通りです。

- **日付の更新**: ドキュメントの日付が2025年4月14日から2025年4月16日に更新され、最終更新日が正確に反映されました。

- **モデルの順序変更**: モデルのリストにおいて、`o4-mini`と`o3`が上部に追加され、リストの順序が変更されました。これにより、新しいモデルが強調され、ユーザーにとっての視認性が向上しています。

- **手順と機能の整理**: 表形式での機能情報が整理され、使用可能なモデルや価格、ファインチューニングなどの情報が一貫した形式で表示されるようになっています。

この更新により、ユーザーはAzure OpenAI Serviceの最新の利用可能モデルや関連情報を迅速に理解できるようになり、サービスの活用を促進することが可能になります。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -68,6 +68,8 @@ The following sections provide you with a quick guide to the default quotas and
 | `gpt-4.1` (2025-04-14) | Default | 1 M | 1 K |
 | `gpt-4.1-nano` (2025-04-14) | Enterprise Tier | 5 M | 5 K |
 | `gpt-4.1-nano` (2025-04-14) | Default | 1 M | 1 K |
+| `gpt-4.1-mini` (2025-04-14) | Enterprise Tier | 5 M | 5 K |
+| `gpt-4.1-mini` (2025-04-14) | Default | 1 M | 1 K |
 
 
 ## computer-use-preview global standard
@@ -91,6 +93,8 @@ The following sections provide you with a quick guide to the default quotas and
 >
 > - **Older chat models:** 1 unit of capacity = 6 RPM and 1,000 TPM.
 > - **o1 & o1-preview:** 1 unit of capacity = 1 RPM and 6,000 TPM.
+> - **o3** 1 unit of capacity = 1 RPM per 1,000 TPM
+> - **o4-mini** 1 unit of capacity = 1 RPM per 1,000 TPM
 > - **o3-mini:** 1 unit of capacity = 1 RPM per 10,000 TPM.
 > - **o1-mini:** 1 unit of capacity = 1 RPM per 10,000 TPM.
 >
@@ -102,9 +106,13 @@ The following sections provide you with a quick guide to the default quotas and
 
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
 |---|---|:---:|:---:|
+| `o4-mini` | Enterprise agreement | 10 M | 10 K |
+| `o3` | Enterprise agreement | 10 M | 10 K |
 | `o3-mini` | Enterprise agreement | 50 M | 5 K |
 | `o1` & `o1-preview` | Enterprise agreement | 30 M | 5 K |
 | `o1-mini`| Enterprise agreement | 50 M | 5 K |
+| `o4-mini` | Default | 1 M | 1 K  |
+| `o3` | Default | 1 M | 1 K |
 | `o3-mini` | Default | 5 M | 500 |
 | `o1` & `o1-preview` | Default | 3 M | 500 |
 | `o1-mini`| Default | 5 M | 500 |
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
このコードの差分は、Azure OpenAI Serviceにおけるクォータと制限に関するドキュメントにいくつかのモデルが追加され、情報が更新されたことを示しています。主な変更点は以下の通りです。

- **新モデルの追加**: 
    - `gpt-4.1-mini`モデルがエンタープライズティアとデフォルトでそれぞれ追加され、クォータの制限（トークン毎分TPMとリクエスト毎分RPM）が記載されるようになりました。具体的には、エンタープライズティアで5M TPS、デフォルトで1M TPSが設定されています。

- **他モデルのクォータ情報の変更**:
    - `o3`モデルと`o4-mini`モデルについても、新たに1 RPMあたり1000 TPMのクォータ情報が追加されており、これにより各モデルの利用条件がより明確になっています。

- **テーブルの更新**: 
    - モデルのクォータリストが更新され、エンタープライズ契約およびデフォルトティアでのクォータ制限が一貫した形式で表示されています。これにより、ユーザーは各モデルの利用可能なリソースを迅速に把握できるようになります。

このような変更により、Azure OpenAI Serviceの利用者が最新の利用規約と各モデルのクォータに関する理解を深め、より効果的にサービスを活用できるようになります。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: whats-new
-ms.date: 04/14/2025
+ms.date: 04/16/2025
 recommendations: false
 ---
 
@@ -21,6 +21,10 @@ This article provides a summary of the latest releases and major documentation u
 
 ## April 2025
 
+### o4-mini and o3 models released
+
+`o4-mini` and `o3` models are now available. These are the latest reasoning models from Azure OpenAI offering significantly enhanced reasoning, quality, and performance. For more information, see the [getting started with reasoning models page](./how-to/reasoning.md).
+
 ### GPT-4.1 released
 
 GPT 4.1 and GPT 4.1-nano are now available. These are the latest models from Azure OpenAI. GPT 4.1 has a 1 million token context limit. For more information, see the [models page](./concepts/models.md#gpt-41-series).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいモデルの追加情報の更新"
}
```

### Explanation
このコードの差分は、Azure OpenAI Serviceに関する「新着情報」記事の更新を示しています。主な変更点は以下の通りです。

- **日付の更新**: 記事の日付が2025年4月14日から2025年4月16日に更新され、最新の情報が反映されました。

- **新モデルのリリース情報の追加**: `o4-mini`および`o3`モデルが新たに利用可能になったことが記載されました。これらのモデルは、Azure OpenAIから提供される最新の推論モデルであり、推論能力、品質、およびパフォーマンスが大幅に向上しています。また、それに関する詳細情報が「推論モデルの使い方」ページへのリンクとして提供されています。

- **既存モデルのリリース情報**: `GPT-4.1`および`GPT-4.1-nano`モデルについての情報も引き続き掲載されており、これによりユーザーは最新のモデルの機能や制限についても理解できるようになっています。

この更新により、ユーザーはAzure OpenAI Serviceの最新のモデルとその能力についての情報を迅速に把握でき、より効果的にサービスを利用するための手助けとなります。


