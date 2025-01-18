---
date: '2025-01-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0fcd6d7...MicrosoftDocs:1d7cc3c
summary: この変更は、Azure OpenAIサービスに関連するドキュメントを更新し、関数呼び出しや推論モデル、地域のモデル可用性、レート制限に関する新しい情報が追加されました。特に、既知の問題や新しい制限が明記され、ユーザーが適切な対策を取れるようになっています。新機能として、`gpt-4o-realtime-preview`モデルでのプロンプトキャッシングと新しい音声オプションが追加され、`max_tokens`パラメータが`max_completion_tokens`に置き換えられました。また、`gpt-4o`モデルのレート制限が接続数からトークン及びリクエスト数に基づくものに変更され、地域のモデル可用性についての明示化が行われました。全体として、これらの変更は開発者にとって重要な情報を提供し、システム利用の効率を高めるものです。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0fcd6d7...MicrosoftDocs:1d7cc3c){target="_blank"}

# Highlights
この変更は、Azure OpenAIサービスに関連するドキュメントを複数の箇所で更新したもので、関数呼び出しや推論モデル、地域のモデル可用性、レート制限などに関する新しい情報が追加されました。特に、`o1`モデルに関する既知の問題と`gpt-4o`モデルに対する新しい制限が明確に記載され、ユーザーがこれらの情報をもとに適切な対策を取れるようにしています。

## New features
- `gpt-4o-realtime-preview`モデルでのプロンプトキャッシングと新しい音声が利用可能に。
- `max_tokens`パラメータが廃止され、新たに`max_completion_tokens`が導入。

## Breaking changes
- プロビジョニングされたグローバルモデルでの地域可用性が大幅に変更。
- `gpt-4o`モデルでは、レート制限が従来の接続数基準からトークンおよびリクエスト数基準へ移行。

## Other updates
- `o1`モデルで`tool_choice`パラメータ使用時の問題が明記。
- モデル情報へのリンクの改善により、関連情報にアクセスしやすく。
- Goでのデータ使用手順の更新。

# Insights
今回のアップデートは、Azure OpenAIサービスを利用する開発者にとって重要な変更を多く含んでいます。特に、`o1`モデルの機能に関する問題や`gpt-4o`モデルの新機能は、それぞれの機能を最大限活用するための貴重な情報を提供しています。

まず、`gpt-4o-realtime-preview`モデルでのプロンプトキャッシングが導入されたことは、カスタマーエクスペリエンスを向上させる重要な追加機能です。これはAIモデルが効率的にプロンプトを処理し、よりスマートに推論を行うことを可能にします。音声オプションの拡充も、多様なユーザーのニーズに応えるためのものです。

一方、`max_tokens`から`max_completion_tokens`へのパラメータ変更は重要です。この変更は、トークン制限管理をより直感的にし、開発者がより管理しやすくすることを目的としています。このような仕様の変更により、開発者はより高度な制御を持ち、モデルの応答を最適化することができます。

さらに、`gpt-4o`モデルのレート制限が具体的なトークン数とリクエスト数に基づく制限に移行したことは、サービスの公平な利用を意識した設計変更です。これは、特に大量のリクエストがある状況下で、システム全体の安定性を高めることに寄与します。

これらの大きな更新に加えて、地域ごとのモデルの可用性情報の明示化はユーザーにとって戦略的な利便性を提供します。ユーザーは自分たちが利用している地域のモデルサポート情報を確認し、利用可能なリソースを最適化できます。

Goプログラムによるデータ活用手順の洗練化も、デベロッパーエクスペリエンスを向上させる重要な要素です。手順が簡素化され、新しい手法は開発工程の効率化に直接寄与します。全体として、これらの変更は、Azure OpenAIサービスの利用者に対し、より強力で柔軟なシステム利用を案内するものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [function-calling.md](#item-32f8e0) | minor update | 関数呼び出しに関するドキュメントの更新 | modified | 20 | 14 | 34 | 
| [reasoning.md](#item-a54b2f) | minor update | 推論モデルに関するドキュメントの更新 | modified | 28 | 13 | 41 | 
| [datazone-standard.md](#item-188333) | minor update | データゾーン標準モデルに関する情報の更新 | modified | 2 | 1 | 3 | 
| [global-batch-datazone.md](#item-94a58c) | minor update | グローバルバッチデータゾーンモデルに関する情報の更新 | modified | 2 | 1 | 3 | 
| [global-batch.md](#item-929e6a) | minor update | グローバルバッチモデルに関する情報の更新 | modified | 2 | 1 | 3 | 
| [provisioned-global.md](#item-340884) | breaking change | プロビジョニングされたグローバルモデルの地域可用性の更新 | modified | 16 | 16 | 32 | 
| [standard-global.md](#item-17a84b) | minor update | 標準グローバルモデルの地域可用性の更新 | modified | 26 | 25 | 51 | 
| [use-your-data-go.md](#item-484724) | minor update | Goでのデータ使用に関する手順の更新 | modified | 11 | 13 | 24 | 
| [overview.md](#item-97d507) | minor update | モデル情報へのリンクの改善 | modified | 1 | 1 | 2 | 
| [quotas-limits.md](#item-06c6f9) | minor update | gpt-4oモデルのレート制限の追加 | modified | 3 | 1 | 4 | 
| [whats-new.md](#item-53303b) | minor update | gpt-4oモデルの新機能と制限の更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/openai/how-to/function-calling.md{#item-32f8e0}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: mbullwin #delegenz
 ms.service: azure-ai-openai
 ms.custom: devx-track-python
 ms.topic: how-to
-ms.date: 06/28/2024
+ms.date: 01/17/2025
 manager: nitinme
 ---
 
@@ -29,24 +29,30 @@ At a high level you can break down working with functions into three steps:
 
 ### Parallel function calling
 
-* `gpt-35-turbo` (1106)
-* `gpt-35-turbo` (0125)
-* `gpt-4` (1106-Preview)
-* `gpt-4` (0125-Preview)
-* `gpt-4` (vision-preview)
-* `gpt-4` (2024-04-09)
-* `gpt-4o` (2024-05-13)
-* `gpt-4o-mini` (2024-07-18)
+* `gpt-35-turbo` (`1106`)
+* `gpt-35-turbo` (`0125`)
+* `gpt-4` (`1106-Preview`)
+* `gpt-4` (`0125-Preview`)
+* `gpt-4` (`vision-preview`)
+* `gpt-4` (`2024-04-09`)
+* `gpt-4o` (`2024-05-13`)
+* `gpt-4o` (`2024-08-06`)
+* `gpt-4o` (`2024-11-20`)
+* `gpt-4o-mini` (`2024-07-18`)
 
 Support for parallel function was first added in API version [`2023-12-01-preview`](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2023-12-01-preview/inference.json)
 
 ### Basic function calling with tools
 
 * All the models that support parallel function calling
-* `gpt-4` (0613)
-* `gpt-4-32k` (0613)
-* `gpt-35-turbo-16k` (0613)
-* `gpt-35-turbo` (0613)
+* `o1` (`2024-12-17`)
+* `gpt-4` (`0613`)
+* `gpt-4-32k` (`0613`)
+* `gpt-35-turbo-16k` (`0613`)
+* `gpt-35-turbo` (`0613`)
+
+> [!IMPORTANT]
+> There is a known issue with the `o1` model and the `tool_choice` parameter. Currently function calls that include the optional `tool_choice` parameter will fail. This page will be updated once the issue is resolved. For more information on what parameters are supported with the o1-series models see, the [reasoning models guide](./reasoning.md).
 
 ## Single tool/function calling example
 
@@ -225,7 +231,7 @@ For example in our simple time app we retrieved multiple times at the same time.
 To force the model to call a specific function set the `tool_choice` parameter with a specific function name. You can also force the model to generate a user-facing message by setting `tool_choice: "none"`.
 
 > [!NOTE]
-> The default behavior (`tool_choice: "auto"`) is for the model to decide on its own whether to call a function and if so which function to call.
+> The default behavior (`tool_choice: "auto"`) is for the model to decide on its own if it should call a function and if so which function to call.
 
 ## Parallel function calling with multiple functions
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "関数呼び出しに関するドキュメントの更新"
}
```

### Explanation
この変更は、OpenAIの関数呼び出しに関するドキュメントにおける情報の更新を含んでいます。主な変更点は、関数呼び出しに関連するモデルリストの追加と、これらのモデルに関連する日付の更新です。特に、`o1`モデルに関する既知の問題が強調されており、`tool_choice`パラメータを使用した関数呼び出しの失敗について通知がなされています。全体として、この更新は2024年の新しいリリースに対応するものであり、APIのバージョンや利用可能なモデルについての情報を正確に反映しています。さらに、文の一部が明確に修正され、全体の内容がより理解しやすくなっています。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's advanced o1 series reasoning models
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 12/17/2024
+ms.date: 01/16/2025
 author: mrbullwinkle    
 ms.author: mbullwin
 ---
@@ -38,31 +38,46 @@ Once access has been granted, you'll need to create a deployment for each model.
 | `o1-preview` | See [models page](../concepts/models.md#global-standard-model-availability). |
 | `o1-mini` | See [models page](../concepts/models.md#global-standard-model-availability). |
 
-## API support
+## API & feature support
 
-Initial support for the **o1-preview** and **o1-mini** preview models was added in API version `2024-09-01-preview`. 
+| **Feature**     | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   |
+|:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|
+| **API Version**       | `2024-12-01-preview` | `2024-09-01-preview`  <br> `2024-10-01-preview` <br> `2024-12-01-preview`    | `2024-09-01-preview`  <br> `2024-10-01-preview` <br> `2024-12-01-preview`    |
+| **[Developer Messages](#developer-messages)** | ✅ | - | - |
+| **[Structured Outputs](./structured-outputs.md)** | ✅ | - | - |
+| **[Context Window](../concepts/models.md#o1-and-o1-mini-models-limited-access)** | Input: 200,000 <br> Output: 100,000 | Input: 128,000  <br> Output: 32,768 | Input: 128,000  <br> Output: 65,536 |
+| **[Reasoning effort](#reasoning-effort)** | ✅ | - | - |
+| System Messages | - | - | - |
+| Functions/Tools | ✅  | -  |  - |
+| `max_completion_tokens` |✅ |✅ |✅ |
 
-As part of this release, the `max_tokens` parameter was deprecated and replaced with the new `max_completion_tokens` parameter. **o1 series** models will only work with the `max_completion_tokens` parameter.
+**o1 series** models will only work with the `max_completion_tokens` parameter.
 
-The latest most capable **o1 series** model is `o1` **Version: 2024-12-17**. This  general availability (GA) model should be used with API version `2024-12-01-preview`.
+> [!IMPORTANT]
+> There is a known issue with the `o1` model and the `tool_choice` parameter. Currently function calls that include the optional `tool_choice` parameter will fail. This page will be updated once the issue is resolved.
 
-### 2024-12-01-preview
+### Not Supported
 
-`2024-12-01-preview` adds support for the new `reasoning_effort` parameter, [structured outputs](./structured-outputs.md), and developer messages. The older preview reasoning models do not currently support these features. For reasoning models, these features are currently only available with `o1` **Version: 2024-12-17**.
+The following are currently unsupported with o1-series models:
+
+- System Messages
+- Streaming
+- Parallel tool calling
+- `temperature`, `top_p`, `presence_penalty`, `frequency_penalty`, `logprobs`, `top_logprobs`, `logit_bias`, `max_tokens`
 
 ## Usage
 
-These models do not currently support the same set of parameters as other models that use the chat completions API. Only a limited subset is currently supported. Using standard parameters like `temperature` and `top_p` will result in errors.
+These models [don't currently support the same set of parameters](#api--feature-support) as other models that use the chat completions API. 
 
 # [Python (Microsoft Entra ID)](#tab/python-secure)
 
-You will need to upgrade your OpenAI client library for access to the latest parameters.
+You'll need to upgrade your OpenAI client library for access to the latest parameters.
 
 ```cmd
 pip install openai --upgrade
 ```
 
-If you are new to using Microsoft Entra ID for authentication see [How to configure Azure OpenAI Service with Microsoft Entra ID authentication](../how-to/managed-identity.md).
+If you're new to using Microsoft Entra ID for authentication see [How to configure Azure OpenAI Service with Microsoft Entra ID authentication](../how-to/managed-identity.md).
 
 ```python
 from openai import AzureOpenAI
@@ -218,10 +233,10 @@ print(response.model_dump_json(indent=2))
 }
 ```
 
-
+## Reasoning effort
 
 > [!NOTE]
-> Reasoning models have `reasoning_tokens` as part of `completion_tokens_details` in the model response. These are hidden tokens that are not returned as part of the message response content but are used by the model to help generate a final answer to your request. `2024-12-01-preview` adds an additional new parameter `reasoning_effort` which can be set to `low`, `medium`, or `high` with the latest `o1` model. The higher the effort setting, the longer the model will spend processing the request, which will generally result in a larger number of `reasoning_tokens`.
+> Reasoning models have `reasoning_tokens` as part of `completion_tokens_details` in the model response. These are hidden tokens that aren't returned as part of the message response content but are used by the model to help generate a final answer to your request. `2024-12-01-preview` adds an additional new parameter `reasoning_effort` which can be set to `low`, `medium`, or `high` with the latest `o1` model. The higher the effort setting, the longer the model will spend processing the request, which will generally result in a larger number of `reasoning_tokens`.
 
 ## Developer messages
 
@@ -234,7 +249,7 @@ Adding a developer message to the previous code example would look as follows:
 
 # [Python (Microsoft Entra ID)](#tab/python-secure)
 
-You will need to upgrade your OpenAI client library for access to the latest parameters.
+You'll need to upgrade your OpenAI client library for access to the latest parameters.
 
 ```cmd
 pip install openai --upgrade
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "推論モデルに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAIの推論モデルに関するドキュメントの更新を反映しています。新たに追加された情報として、o1シリーズモデルのAPIバージョン、機能のサポート状況、および既知の問題が詳述されています。特に、`max_tokens`パラメータが廃止され、新しい`max_completion_tokens`パラメータに置き換えられたことが強調されています。また、`o1`モデルに関連する`tool_choice`パラメータに関する問題も明示されており、開発者がこの情報をもとに適切な対応を取ることができるようになっています。

変更には、APIと機能のサポートのセクションが追加され、各モデルに対する特定の機能の可用性が一覧表示されています。これにより、ユーザーはどのモデルがどの機能をサポートしているのかを簡単に確認できるようになっています。また、推論モデルに関する標準的な注意事項やパラメータの制約についても詳細が提供され、ドキュメントがより包括的かつ理解しやすくなっています。

## articles/ai-services/openai/includes/model-matrix/datazone-standard.md{#item-188333}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,7 @@ description: Regional availability for Global Batch models
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
+ms.custom: references_regions
 ms.date: 10/31/2024
 ---
 
@@ -21,4 +22,4 @@ ms.date: 10/31/2024
 | swedencentral      | ✅                       | ✅                       | ✅                            |
 | westeurope         | ✅                       | ✅                       | ✅                            |
 | westus             | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
+| westus3            | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データゾーン標準モデルに関する情報の更新"
}
```

### Explanation
この変更は、データゾーンの標準モデルに関する情報を含む文書の小規模な更新を示しています。主な変更点は、メタデータに新たに`ms.custom: references_regions`が追加されたことと、文書の行末での改行の調整です。これにより、文書の構造が明確になり、モデルの地域的な可用性に関する情報の整理が行われました。具体的には、モデルの可用性が示されるテーブルに、`westus3`地域の情報が確認されており、各モデルの利用可能性が明示されています。この更新により、ユーザーは地域ごとのモデルのサポート状況をより容易に把握できるようになります。

## articles/ai-services/openai/includes/model-matrix/global-batch-datazone.md{#item-94a58c}

<details>
<summary>Diff</summary>
````diff
@@ -14,9 +14,10 @@ ms.date: 01/14/2025
 |:-------------------|:--------------------------:|:-------------------------------:|
 | eastus             | ✅                       | ✅                            |
 | eastus2            | ✅                       | ✅                            |
+| francecentral      | ✅                       | ✅                            |
 | germanywestcentral | ✅                       | ✅                            |
 | southcentralus     | ✅                       | ✅                            |
 | swedencentral      | ✅                       | ✅                            |
 | westeurope         | ✅                       | ✅                            |
 | westus             | ✅                       | ✅                            |
-| westus3            | ✅                       | ✅                            |
+| westus3            | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルバッチデータゾーンモデルに関する情報の更新"
}
```

### Explanation
この変更は、グローバルバッチデータゾーンモデルに関する文書の小規模な更新を示しています。具体的には、フランス中央地域（`francecentral`）に対するモデルの可用性が新たに追加され、これによりユーザーはこの地域におけるモデルの利用状況を確認できるようになりました。また、`westus3`地域に関する情報が維持されています。この更新は、地域ごとのモデルのサポート状況を明確にするものであり、特に利用可能な地域の詳細が強調されています。これにより、利用者は自分のニーズに合わせた地域でのモデル利用の選択肢を把握しやすくなっています。

## articles/ai-services/openai/includes/model-matrix/global-batch.md{#item-929e6a}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,7 @@ description: Regional availability for Global Batch models
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
+ms.custom: references_regions
 ms.date: 01/15/2025
 ---
 
@@ -31,4 +32,4 @@ ms.date: 01/15/2025
 | uksouth            | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | westeurope         | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | westus             | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westus3            | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
\ No newline at end of file
+| westus3            | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルバッチモデルに関する情報の更新"
}
```

### Explanation
この変更は、グローバルバッチモデルに関する文書の小規模な更新を示しています。主な変更点として、メタデータに`ms.custom: references_regions`が新たに追加され、モデルの地域的な可用性に関する情報が強調されることになりました。また、`westus3`地域のモデル可用性に関する情報が明確に表示され、文書全体の整合性が保たれています。この更新により、ユーザーは各地域におけるモデルのサポート状況をより容易に理解し、必要に応じた選択ができるようになります。これにより、特に地域に基づいて利用を検討するユーザーにとって役立つ情報が提供されています。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -11,28 +11,28 @@ ms.date: 01/15/2025
 
 | **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
 |:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|
-| australiaeast      | -                      | ✅                       | ✅                            |
-| brazilsouth        | -                      | ✅                       | ✅                            |
-| canadacentral      | -                      | ✅                       | ✅                            |
-| canadaeast         | -                      | ✅                       | ✅                            |
+| australiaeast      | ✅                       | ✅                       | ✅                            |
+| brazilsouth        | ✅                       | ✅                       | ✅                            |
+| canadacentral      | ✅                       | ✅                       | ✅                            |
+| canadaeast         | ✅                       | ✅                       | ✅                            |
 | eastus             | ✅                       | ✅                       | ✅                            |
 | eastus2            | ✅                       | ✅                       | ✅                            |
 | francecentral      | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | -                      | ✅                       | ✅                            |
-| japaneast          | -                      | ✅                       | ✅                            |
-| koreacentral       | -                      | ✅                       | ✅                            |
-| northcentralus     | -                      | ✅                       | ✅                            |
-| norwayeast         | -                      | ✅                       | ✅                            |
-| polandcentral      | -                      | ✅                       | ✅                            |
-| southafricanorth   | -                      | ✅                       | ✅                            |
+| germanywestcentral | ✅                       | ✅                       | ✅                            |
+| japaneast          | ✅                       | ✅                       | ✅                            |
+| koreacentral       | ✅                       | ✅                       | ✅                            |
+| northcentralus     | ✅                       | ✅                       | ✅                            |
+| norwayeast         | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                       | ✅                       | ✅                            |
+| southafricanorth   | ✅                       | ✅                       | ✅                            |
 | southcentralus     | ✅                       | ✅                       | ✅                            |
-| southindia         | -                      | ✅                       | ✅                            |
-| spaincentral       | -                      | ✅                       | ✅                            |
+| southindia         | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                       | ✅                       | ✅                            |
 | swedencentral      | ✅                       | ✅                       | ✅                            |
-| switzerlandnorth   | -                      | ✅                       | ✅                            |
-| switzerlandwest    | -                      | ✅                       | ✅                            |
+| switzerlandnorth   | ✅                       | ✅                       | ✅                            |
+| switzerlandwest    | ✅                       | ✅                       | ✅                            |
 | uaenorth           | ✅                       | ✅                       | ✅                            |
-| uksouth            | -                      | ✅                       | ✅                            |
+| uksouth            | ✅                       | ✅                       | ✅                            |
 | westeurope         | ✅                       | ✅                       | ✅                            |
 | westus             | ✅                       | ✅                       | ✅                            |
 | westus3            | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロビジョニングされたグローバルモデルの地域可用性の更新"
}
```

### Explanation
この変更は、プロビジョニングされたグローバルモデルの地域可用性に関する重要な更新を示しています。具体的には、多くの地域でモデルの可用性が`-`から`✅`に変更され、これにより各地域での利用可能なモデルの状態が改善されました。この文書の改訂によって、オーストラリア東部、ブラジル南部、カナダ中部、カナダ東部、ドイツ西部、日本東部、韓国中央部、北アメリカ中央部、ノルウェー東部、ポーランド中央部、南アフリカ北部、南インド、スペイン中央、およびスイス北部と西部のすべての地域で、モデルが利用可能であることが明確に示されています。これにより、ユーザーは各地域でのモデルのサポート状況を確認しやすくなり、自身の利用計画を構築する際の参考情報を得ることができます。このような更新は、地域的なサービス提供の幅を広げ、ユーザーのアクセス性を向上させるものです。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -5,31 +5,32 @@ description: Regional availability for Global Standard models.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
+ms.custom: references_regions
 ms.date: 10/25/2024
 ---
 
-| **Region**     | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-10-01**   | **gpt-4**, **turbo-2024-04-09**   |
-|:-------------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:-------------------------------:|
-| australiaeast      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| brazilsouth        | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| canadaeast         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| eastus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| eastus2            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                            |
-| francecentral      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| germanywestcentral | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| japaneast          | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| koreacentral       | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| northcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| norwayeast         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| polandcentral      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| southafricanorth   | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| southcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| southindia         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| spaincentral       | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| swedencentral      | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                            |
-| switzerlandnorth   | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| uaenorth           | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| uksouth            | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| westeurope         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
-| westus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| westus3            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
\ No newline at end of file
+| **Region**     | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-10-01**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4**, **turbo-2024-04-09**   |
+|:-------------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:-------------------------------------------:|:-------------------------------:|
+| australiaeast      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| brazilsouth        | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| canadaeast         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| eastus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            |
+| eastus2            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                            |
+| francecentral      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| germanywestcentral | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| japaneast          | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| koreacentral       | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| northcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            |
+| norwayeast         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| polandcentral      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| southafricanorth   | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| southcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            |
+| southindia         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| spaincentral       | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| swedencentral      | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                            |
+| switzerlandnorth   | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| uaenorth           | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| uksouth            | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| westeurope         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | ✅                            |
+| westus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            |
+| westus3            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準グローバルモデルの地域可用性の更新"
}
```

### Explanation
この変更は、標準グローバルモデルに関する文書の地域可用性を更新したもので、いくつかの新しい情報と修正が含まれています。具体的には、地域の可用性表に`gpt-4o-realtime-preview`という新しいモデルが追加され、その利用可能性が地域ごとに示されています。また、既存モデルのいくつかの地域においても可用性が更新されました。全体として、更新された表では、各地域のモデルの可用性がより明確に示され、各々がいつ利用可能であるかが具体的になっています。この信息は、ユーザーがどの地域でどのモデルを使用できるかを理解するのに役立つ重要な更新です。また、`ms.custom: references_regions`がメタデータに追加され、文書内で地域の参照が強調されています。これにより、ユーザーは地域ごとのリソースへのアクセスを計画しやすくなります。

## articles/ai-services/openai/includes/use-your-data-go.md{#item-484724}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: travisw
 ms.author: travisw
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 03/07/2024
+ms.date: 01/17/2025
 ---
 
 [!INCLUDE [Set up required variables](./use-your-data-common-variables.md)]
@@ -19,16 +19,7 @@ ms.date: 03/07/2024
    cd openai-go
    ```
 
-1. Install the following Go packages:
-
-   ```cmd
-   go get github.com/Azure/azure-sdk-for-go/sdk/ai/azopenai
-   ```
-1. Enable dependency tracking for your code.
-    ```cmd
-    go mod init example/azure-openai
-    ```
-## Create the Go app
+## Create the app
 
 1. From the project directory, open the *sample.go* file and add the following code:
 
@@ -119,10 +110,17 @@ ms.date: 03/07/2024
    > [!IMPORTANT]
    > For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see the Azure AI services [security](../../security-features.md) article.
 
-1. Execute the following command:
+
+1. Now open a command prompt and run the following:
 
    ```cmd
-   go run sample.go
+   go mod init sample.go
    ```
 
+1. Next run:
+    ```cmd
+    go mod tidy
+    go run sample.go
+    ```
+
    The application prints the response including both answers to your query and citations from your uploaded files.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Goでのデータ使用に関する手順の更新"
}
```

### Explanation
この変更は、Goプログラミング言語を使用してデータを利用するための手順に関する文書を更新したものです。主な更新点には、日付の変更（`ms.date`が2024年3月7日から2025年1月17日に変更）や手順の内容が含まれています。いくつかの手順が簡素化され、特に依存関係のトラッキングに関連する部分が整理されました。

具体的には、`go get`コマンドと`go mod init`コマンドに関する記載が削除され、代わりに新しい手順が付け加えられています。新しい手順では、ユーザーが`sample.go`ファイルを初期化し、次に`go mod tidy`コマンドを実行してからアプリケーションを実行する流れが示されています。これにより、ユーザーは必要な手順がより明確に理解しやすくなり、全体の流れがスムーズになっています。

全体として、この更新は文書の明瞭性を高め、ユーザーがGoを使用してAzure OpenAIサービスにデータを組み込む際の対処をよりシンプルで効果的にしました。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ Azure OpenAI Service provides REST API access to OpenAI's powerful language mode
 
 | Feature | Azure OpenAI |
 | --- | --- |
-| Models available | **o1** & **o1-mini** - (Limited Access - [Request Access](https://aka.ms/OAI/o1access))<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
+| Models available | [**o1** & **o1-mini**](./how-to/reasoning.md) - (Limited Access - [Request Access](https://aka.ms/OAI/o1access))<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
 | Fine-tuning | `GPT-4o-mini` (preview) <br> `GPT-4` (preview) <br>`GPT-3.5-Turbo` (0613) <br> `babbage-002` <br> `davinci-002`.|
 | Price | [Available here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> For details on vision-enabled chat models, see the [special pricing information](../openai/concepts/gpt-with-vision.md#special-pricing-information).|
 | Virtual network support & private link support | Yes.  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル情報へのリンクの改善"
}
```

### Explanation
この変更は、Azure OpenAIサービスの概要に関する文書で、利用可能なモデルの情報へのリンクが改善されました。具体的には、「o1」と「o1-mini」モデルについての説明が修正され、モデル名が新たにリンクとして提供されています。このリンクをクリックすることで、ユーザーは推論に関する詳細な情報が記載されたページ（`./how-to/reasoning.md`）に直接アクセスできるようになっています。

全体的に、この変更は情報のアクセシビリティを向上させ、ユーザーが必要な情報に迅速かつ容易にアクセスできるよう意図されています。また、他のモデル情報や関連情報に関するリンクはそのまま維持されており、文書全体の一貫性と有用性が保たれています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 01/09/2025
+ms.date: 1/17/2025
 ms.author: mbullwin
 ---
 
@@ -133,6 +133,8 @@ M = million | K = thousand
 
 ## gpt-4o audio
 
+The rate limits for each `gpt-4o-realtime-preview` model deployment are 100K TPM and 1K RPM. During the preview, Azure AI Foundry portal and APIs might inaccurately show different rate limits. Even if you try to set a different rate limit, the actual rate limit will be 100K TPM and 1K RPM.
+
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
 |---|---|:---:|:---:|
 |`gpt-4o-realtime-preview` | Default | 100 K | 1 K |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "gpt-4oモデルのレート制限の追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「クォータと制限」に関する文書に対して、gpt-4oモデルのレート制限に関する情報を追加したものです。具体的には、`gpt-4o-realtime-preview`モデルのデプロイメントに対するレート制限として、1分あたりのトークン数（TPM）が100K、リクエスト数（RPM）が1Kであることが明記されました。

また、プレビュー期間中は、Azure AI FoundryポータルおよびAPIで異なるレート制限が表示される可能性があり、自身で設定しようとしても実際のレート制限は100K TPMと1K RPMに固定されることも強調されています。

さらに、文書内の日付が2025年1月9日から2025年1月17日に変更され、最新の情報を反映するように更新されています。これによって、ユーザーはgpt-4oモデルの利用に関して、より正確な情報に基づいてサービスを利用できるようになります。全体として、これらの変更は、サービス利用に関する明確さと透明性を高めることを目的としています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: whats-new
-ms.date: 1/15/2025
+ms.date: 1/17/2025
 recommendations: false
 ---
 
@@ -27,7 +27,7 @@ The `gpt-4o-realtime-preview` model version 2024-12-17 is available for global d
 
 - Added support for [prompt caching](./how-to/prompt-caching.md) with the `gpt-4o-realtime-preview` model.
 - Added support for new voices. The `gpt-4o-realtime-preview` models now support the following voices: "alloy", "ash", "ballad", "coral", "echo", "sage", "shimmer", "verse".
-- Rate limits are no longer based on connections per minute. Rate limiting is now based on RPM (requests per minute) and TPM (tokens per minute) for the `gpt-4o-realtime-preview` model. The rate limits for the `gpt-4o-realtime-preview` model are 100K TPM and 1K RPM.
+- Rate limits are no longer based on connections per minute. Rate limiting is now based on RPM (requests per minute) and TPM (tokens per minute) for the `gpt-4o-realtime-preview` model. The rate limits for each `gpt-4o-realtime-preview` model deployment are 100K TPM and 1K RPM. During the preview, Azure AI Foundry portal and APIs might inaccurately show different rate limits. Even if you try to set a different rate limit, the actual rate limit will be 100K TPM and 1K RPM.
 
 For more information, see the [GPT-4o real-time audio quickstart](realtime-audio-quickstart.md) and the [how-to guide](./how-to/realtime-audio.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "gpt-4oモデルの新機能と制限の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「新機能」についての文書に対して行われたもので、主にgpt-4oモデルに関連するいくつかの重要な情報が追加・更新されました。具体的には、まずgpt-4o-realtime-previewモデルの新しいバージョンが利用可能であることが強調されています。

新機能としては、gpt-4o-realtime-previewモデルでのプロンプトキャッシングのサポートが追加され、新しい音声が利用可能になったことも記載されています。具体的には、"alloy"、"ash"、"ballad"、"coral"、"echo"、"sage"、"shimmer"、"verse"という音声が支持されています。

また、レート制限に関する重要な変更があり、接続数ベースの制限からリクエスト数（RPM）およびトークン数（TPM）ベースの制限に移行したことが記されています。特に、`gpt-4o-realtime-preview`モデルのレート制限は、各デプロイメントに対して100K TPMおよび1K RPMとなっており、プレビュー中はAzure AI FoundryポータルとAPIが異なるレート制限を誤って表示する可能性があることも注意されています。

文書の日付も2025年1月15日から17日に更新され、最新の情報に基づいて内容が改訂されています。これらの更新は、ユーザーが新しい機能を活用し、レート制限についての理解を深めることを助けるために行われています。


