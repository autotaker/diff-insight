---
date: '2025-04-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bb349ba...MicrosoftDocs:5e44f1a
summary: Azure OpenAI関連ドキュメントが軽微に更新され、特にモデル退役情報において`gpt-4.5-preview`の退役日が変更されました。新たに`gpt-4.1-nano`、`o4-mini`、`o3`モデルの関数呼び出しサポートが追加され、`tool_choice`パラメーターのサポート情報が増加しました。また、推論機能におけるモデルごとのサポート状況が明確になり、地域ごとのモデルマトリックスも更新されています。これにより、ユーザーは新しいモデルへの移行や最新機能の活用がしやすくなります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bb349ba...MicrosoftDocs:5e44f1a){target="_blank"}

# Highlights

Azure OpenAI関連ドキュメントにおいて軽微な更新が行われました。モデルの退役情報で、`gpt-4.5-preview`の退役日が変更されています。また、ドキュメンテーションの中で関数呼び出し機能や推論機能の更新があり、新しいモデルと機能サポート状況が明確化されています。モデルマトリックスについても各地域における機能サポートが更新されています。

## New features

- `gpt-4.1-nano`および新しい`o4-mini`と`o3`モデルの関数呼び出しサポートが追加。
- `tool_choice`パラメーターのサポートにおいて、`o3-mini`および`o1`についての詳細が追加。

## Breaking changes

- `gpt-4.5-preview`モデルの退役日が遅延され、退役スケジュールの変更が発生。

## Other updates

- 推論機能におけるモデルごとのサポート状況の明確化。
- モデルマトリックスドキュメント内で、`koreacentral`及び`swedencentral`リージョンの機能サポート状態の更新。

# Insights

今回のドキュメント更新では、Azure OpenAIサービスの使用において考慮すべきいくつかの重要な点が明確化されています。`gpt-4.5-preview`モデルの退役日の修正は、特定のモデルに依存するアプリケーションや研究に携わるユーザーにとって有用な情報です。この延長により余裕を持って新しいモデルへの乗り換え準備が可能です。

新しく追加されたモデル (`gpt-4.1-nano`, `o4-mini`, `o3`) の機能サポート情報により、ユーザーは最新の技術を活用して並列関数呼び出しを効率化することができます。具体的には、高パフォーマンスのAIアプリケーション開発に役立つ重要な更新です。加えて、新しい`tool_choice`パラメーターのサポートは、特に柔軟なモデル選択を可能にし、アプリケーションの幅を広げることを期待されています。

推論機能更新においては、特定モデルの「並列ツール呼び出し」のサポート状況が明示され、ユーザーが誤ったモデル選択により機能不全に陥るリスクを軽減する重要な手掛かりを提供しています。

また、地域ごとに異なるモデルの展開状況が更新され、各事業所がより地域特化のサービス提供を調整しやすくなりました。今回の更新を踏まえ、開発者や企業は、より正確な情報に基づいてサービスの計画および運用の最適化を図ることが求められます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデル退役情報の更新 | modified | 1 | 1 | 2 | 
| [function-calling.md](#item-32f8e0) | minor update | 関数呼び出し機能の更新 | modified | 6 | 3 | 9 | 
| [reasoning.md](#item-a54b2f) | minor update | 推論機能の更新 | modified | 1 | 1 | 2 | 
| [standard-global.md](#item-17a84b) | minor update | モデルマトリックスの更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -103,7 +103,7 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-4` | 1106-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025 **<sup>1</sup>** <br>Retirement date: May 1, 2025  | `gpt-4o`|
 | `gpt-4` | 0125-preview |To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025 **<sup>1</sup>** <br>Retirement date: May 1, 2025  | `gpt-4o` |
 | `gpt-4` | vision-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025  **<sup>1</sup>** <br>Retirement date: May 1, 2025 | `gpt-4o`|
-| `gpt-4.5-preview` | 2025-02-27 | No earlier than July 02, 2025 | `gpt-4.1` |
+| `gpt-4.5-preview` | 2025-02-27 | July 14, 2025 | `gpt-4.1` |
 | `gpt-4.1` | 2025-04-14 | No earlier than April 11, 2026 | |
 | `gpt-4.1-mini` | 2025-04-14 | No earlier than April 11, 2026 |
 | `gpt-4.1-nano` | 2025-04-14 | No earlier than April 11, 2026 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル退役情報の更新"
}
```

### Explanation
このコードの差分は、Azure OpenAIサービスにおけるモデルの退役情報に関するマークダウンファイルの内容を更新しています。具体的には、`gpt-4.5-preview`モデルの退役日が、以前の「2025年7月2日」から「2025年7月14日」に変更されています。これは、新しい情報に基づいた微調整であり、他のモデルの退役計画には影響しない軽微な更新となっています。この変更は、利用者に最新のモデル情報を提供するためのものです。

## articles/ai-services/openai/how-to/function-calling.md{#item-32f8e0}

<details>
<summary>Diff</summary>
````diff
@@ -41,16 +41,16 @@ At a high level you can break down working with functions into three steps:
 * `gpt-4o-mini` (`2024-07-18`)
 * `gpt-4.5-preview` (`2025-02-27`)
 * `gpt-4.1` (`2025-04-14`)
-* `gpt-4.1-nano` (`2025-04-14`)
 * `gpt-4.1-mini` (`2025-04-14`)
-* `o4-mini` (`2025-04-16`)
-* `o3` (`2025-04-16`)
 
 Support for parallel function was first added in API version [`2023-12-01-preview`](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2023-12-01-preview/inference.json)
 
 ### Basic function calling with tools
 
 * All the models that support parallel function calling
+* `o4-mini` (`2025-04-16`)
+* `o3` (`2025-04-16`)
+* `gpt-4.1-nano` (`2025-04-14`)
 * `o3-mini` (`2025-01-31`)
 * `o1` (`2024-12-17`)
 * `gpt-4` (`0613`)
@@ -61,6 +61,9 @@ Support for parallel function was first added in API version [`2023-12-01-previe
 > [!NOTE]
 > The `tool_choice` parameter is now supported with `o3-mini` and `o1`. For more information on what parameters are supported with the o-series models see, the [reasoning models guide](./reasoning.md).
 
+> [!IMPORTANT]
+> Tool/function descriptions are currently limited to 1024 characters with Azure OpenAI. We will update this article if this limit is changed.
+
 ## Single tool/function calling example
 
 First we will demonstrate a simple toy function call that can check the time in three hardcoded locations with a single tool/function defined. We have added print statements to help make the code execution easier to follow:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "関数呼び出し機能の更新"
}
```

### Explanation
このコードの差分は、Azure OpenAIの関数呼び出しに関するドキュメンテーションを更新しています。具体的には、いくつかのモデルのリストが追加され、特に`gpt-4.1-nano`および新しい`o4-mini`と`o3`モデルが、並列関数呼び出しをサポートするモデルとして追加されています。また、`tool_choice`パラメーターが`o3-mini`および`o1`でサポートされることが明記され、ツールや関数の説明に対する文字数制限に関する重要な注意書きも追加されています。これにより、ユーザーは最新の機能と制限についての理解を深めることができます。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -48,7 +48,7 @@ Azure OpenAI `o-series` models are designed to tackle reasoning and problem-solv
 | Chat Completions API | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Responses API | ✅ | ✅  | - | - | - | - |
 | Functions/Tools | ✅ | ✅ | ✅  | ✅  |  - | - |
-| Parallel Tool Calls | ✅ | ✅ | -  | -  |  - | - |
+| Parallel Tool Calls | - | - | -  | -  |  - | - |
 | `max_completion_tokens`<sup>*</sup> | ✅ | ✅ |✅ |✅ |✅ | ✅ |
 | System Messages<sup>**</sup> | ✅ | ✅ | ✅ | ✅ | - | - |
 | [Reasoning summary](#reasoning-summary) <sup>***</sup> | ✅ | ✅ | -  | -  |  - | - |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "推論機能の更新"
}
```

### Explanation
このコードの差分は、Azure OpenAIの推論機能に関するドキュメントの一部を更新しています。具体的には、`o-series`モデルにおける「並列ツール呼び出し」機能が、特定のモデルに対してサポートされていないことを示すために、該当部分が更新されています。この変更により、ユーザーに対してどのモデルが「並列ツール呼び出し」をサポートしているかが明確になり、より正確な情報を提供できます。これにより、機能の使用方法に関する理解が深まります。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -20,15 +20,15 @@ ms.date: 04/17/2025
 | germanywestcentral | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | italynorth         | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | -                      | -                      | ✅                       | ✅                            | -                           | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | japaneast          | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| koreacentral       | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | -                             | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| koreacentral       | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | northcentralus     | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | norwayeast         | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | polandcentral      | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | southafricanorth   | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | southcentralus     | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | southindia         | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | spaincentral       | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| swedencentral      | ✅                        | ✅                        | ✅                             | ✅                             | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | ✅                                        | ✅                                     | ✅                                             | -                                         | -                                 | -                               | -                                      |
+| swedencentral      | ✅                        | ✅                        | ✅                             | ✅                             | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | ✅                                        | ✅                                     | ✅                                             | -                                         | ✅                                  | ✅                                | ✅                                       |
 | switzerlandnorth   | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | uaenorth           | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | uksouth            | -                       | -                       | -                            | -                            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルマトリックスの更新"
}
```

### Explanation
このコードの差分は、Azure OpenAIサービスにおけるモデルマトリックスの一部を更新しています。具体的には、`koreacentral`および`swedencentral`のモデルに関する行が修正され、特定の機能のサポート状況が明確に示されています。特に、`swedencentral`については、いくつかの機能がサポートされるように変更され、以前のサポートの詳細が更新されています。これにより、各リージョンで利用可能なモデルおよび機能についての情報がより正確になり、ユーザーに対して最新の情報が提供されます。


