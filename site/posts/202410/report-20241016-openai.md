---
date: '2024-10-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9578344...MicrosoftDocs:9a3d20f
summary: 今回の変更は、AzureのOpenAI関連サービスのドキュメントに対する軽微な更新です。主な内容は、新しい注意書きの追加とドキュメントの日付の更新で、特にバッチ操作と構造化出力に関する既知の問題についてユーザーが認識しやすくすることを目的としています。新機能は追加されていませんが、情報が明確化されています。既存の機能に対する影響はなく、ドキュメントの日付が更新され、特定のAPIバージョンに関する既知の問題が追加されています。これらの変更は、ユーザーに技術的な制約やバグ情報を明示的に伝え、サービスの健全な利用を促進します。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9578344...MicrosoftDocs:9a3d20f){target="_blank"}

# ハイライト

今回の変更は、OpenAIに関連するAzureサービスのドキュメントに対する軽微な更新です。新しい注意書きの追加と日付の更新が行われました。この更新は特にバッチ操作と構造化出力に関する既知の問題について、ユーザーが認識しやすくすることを目的としています。

## 新機能
特に新しい機能の追加はありませんが、情報が一部明確化されています。

## 互換性への影響
既存の機能への影響や破壊的変更はありません。

## その他の更新
ドキュメントの日付が更新され、特定のAPIバージョンにおける既知の問題が追加されています。

# 説明

今回の更新は、Azure OpenAIのドキュメントにおいて、バッチ操作と構造化出力に関する既知の問題をユーザーに認識させるためのものです。具体的には、以下の2つのファイルに影響があります。

1. **バッチ操作に関する情報の更新**:
    - `articles/ai-services/openai/how-to/batch.md`において、ドキュメントの日付が最新のものに更新されました。これによって、ユーザーが最新の情報を閲覧していることが明確に示されます。
    - 特に、特定のAPIバージョンでjsonlファイルを使用する際のエラーの可能性についての注意書きが追加されています。これにより、ユーザーはバッチ操作を行う際の潜在的な問題を事前に把握することができます。

2. **構造化出力に関する情報の更新**:
    - `articles/ai-services/openai/how-to/structured-outputs.md`では、「自分のデータを持ち込む」シナリオにおいて構造化出力がサポートされていない点が明確化されました。この情報は重要で、ユーザーが誤った前提でシステムを使用しないようにしています。
    - これに加え、グローバルバッチに関する既知の問題も説明され、ユーザーがこの機能の制約について理解を深めやすくなっています。

これらの変更は、技術的な制約やバグ情報をユーザーに明確に伝えることで、サービスの健全な利用を促進するものです。特にエラーや制約の情報は、開発者が設計やデバッグを行う上で欠かせないものであり、このように事前に問題点を提示することで、効率的な開発とリスクの軽減につながります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [batch.md](#item-a131d5) | minor update | バッチ操作に関する情報の更新 | modified | 8 | 1 | 9 | 
| [structured-outputs.md](#item-cc2557) | minor update | 構造化出力に関する情報の更新 | modified | 5 | 3 | 8 | 


# Modified Contents
## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: 
 ms.topic: how-to
-ms.date: 10/11/2024
+ms.date: 10/14/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -76,6 +76,13 @@ The following aren't currently supported:
 - Integration with the Assistants API.
 - Integration with Azure OpenAI On Your Data feature.
 
+> [!NOTE]
+> There is a known issue with Azure OpenAI global batch and [structured outputs](./structured-outputs.md). Currently, lines in your jsonl file with structured output requests will fail with the following error message written to the error file:
+>
+> ***response_format value as json_schema is enabled only for api versions 2024-08-01-preview and later***.
+>
+>This error will occur even when your code targets the latest preview APIs which support structured outputs. Once the issue is resolved, this page will be updated.
+
 ### Global batch deployment
 
 In the Studio UI the deployment type will appear as `Global-Batch`.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ操作に関する情報の更新"
}
```

### Explanation
この変更は、`articles/ai-services/openai/how-to/batch.md`ファイルにおける軽微な更新です。主な変更点は、日付の更新と、新しい注意書きの追加です。具体的には、ドキュメントの日付が2024年10月11日から2024年10月14日に変更され、Azure OpenAIのグローバルバッチ及び構造化出力に関する既知の問題についての説明が新しく追加されました。この注釈では、特定のAPIバージョンにおいて構造化出力リクエストを含むjsonlファイルの行がエラーを引き起こす可能性があることが説明されています。この変更は、ユーザーがバッチ操作の制約を理解しやすくするために重要です。

## articles/ai-services/openai/how-to/structured-outputs.md{#item-cc2557}

<details>
<summary>Diff</summary>
````diff
@@ -16,16 +16,18 @@ recommendations: false
 
 Structured outputs make a model follow a [JSON Schema](https://json-schema.org/overview/what-is-jsonschema) definition that you provide as part of your inference API call. This is in contrast to the older [JSON mode](./json-mode.md) feature, which guaranteed valid JSON would be generated, but was unable to ensure strict adherence to the supplied schema. Structured outputs is recommended for function calling, extracting structured data, and building complex multi-step workflows.
 
->[!NOTE]
-> Currently Structured outputs is not supported on [bring your own data](../concepts/use-your-data.md) scenario.
+> [!NOTE]
+> * Currently structured outputs is not supported on [bring your own data](../concepts/use-your-data.md) scenario.
+>
+> * There is a known issue blocking structured outputs support for [global batch](batch.md).
 
 ## Supported models
 
 Currently only `gpt-4o` version: `2024-08-06` supports structured outputs.
 
 ## API support
 
-Support for structured outputs was first added in API version `2024-08-01-preview`. 
+Support for structured outputs was first added in API version `2024-08-01-preview`.
 
 ## Getting started
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "構造化出力に関する情報の更新"
}
```

### Explanation
この変更は、`articles/ai-services/openai/how-to/structured-outputs.md`ファイルの軽微な更新です。主に、構造化出力に関する注意書きが改善されており、現在の制約事項がより明確に説明されています。具体的には、「自分のデータを持ち込む」シナリオでは構造化出力がサポートされていないことが強調され、その上でグローバルバッチに関する既知の問題が追加されています。これにより、ユーザーはこの機能の制限に関する重要な情報を理解しやすくなっています。また、構造化出力に関連するモデルとAPIのサポートに関する情報は変更されていませんが、全体的な説明が明確になっています。


