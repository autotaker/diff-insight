---
date: '2025-06-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:92ff08a...MicrosoftDocs:a20162d
summary: この変更セットは、Azure OpenAIサービスに関連する文書の小規模な更新を含んでおり、主にモデルの引退日付やデプロイメント情報の変更、プロンプトエンジニアリングのタイトル順序の修正、プロビジョンドスループットに関する情報更新が行われました。新たに
  `gpt-4.1` シリーズモデルのバッチデプロイメント情報が追加され、高トークン数での利用が可能になりました。また、モデルの引退日付も更新され、ユーザーにとって重要な情報が提供されています。全体的に、これらの変更はAzure
  OpenAIサービスの利用者に最新の技術情報を提供し、サービス利用を効率的に進めるための基盤を強化することを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:92ff08a...MicrosoftDocs:a20162d){target="_blank"}

# Highlights
この変更セットは、Azure OpenAIサービスに関連するさまざまな文書の小規模な更新を含んでいます。主にモデルの引退日付やデプロイメント情報の変更、プロンプトエンジニアリングのタイトル順序の修正、プロビジョンドスループットに関する情報更新などが含まれています。また、レスポンスAPIや新しい推論プレビュー、グローバルモデルマトリックスに関連するコンテンツが更新されています。

## New features
- `gpt-4.1`、`gpt-4.1-nano`、`gpt-4.1-mini`モデルのバッチデプロイメント情報が追加され、より高いトークン数での利用が可能に。
- `gpt-4.1-mini-2025-04-14`モデルがプロンプトキャッシングに追加。

## Breaking changes
- 特に重大な破壊的変更は見られませんが、いくつかの情報が削除されており、以前サポートされていなかった機能が今後サポートされるかもしれないことを示唆しています（例: レスポンスAPIのファインチューニングモデル情報）。

## Other updates
- モデルの引退日付が更新され、ユーザーが正確なサポート終了時期を把握できるように。
- 新しいモデルバージョン `DeepSeek-R1-0528`の追加。
- タイトルの順序が再構成され、内容の可読性が向上。

# Insights
このコード変更は、Azure OpenAIサービスのモデルと機械学習 API に関するドキュメントの精度と最新性を向上させるための一連の小規模な修正を施したものです。このドキュメントへの変更は開発者やユーザーにとって非常に重要で、特にモデルの引退日付の更新や新しいデプロイメント情報の追加、およびサポートされるモデルの確認などが、サービス利用者にとって直面する重要な情報を提供しています。

例えば、プロンプトキャッシングの更新により、新たにサポートされるモデルがリストに追加されたので、開発者はこれらの機能を活用する準備を進められます。また、プロビジョンドスループットの情報が更新されたことで、パフォーマンスに関する情報がさらに正確になり、開発者はシステムの最適化に役立つ情報を得ることができるでしょう。

さらに、新しい推論プレビューに関する大幅な内容置き換えにより、最新のAPI機能や使用方法に関する透明度が高まり、ユーザーエクスペリエンスが向上します。全体として、これらの文書変更は、Azure OpenAIサービスの利用者が最新の技術情報を受け取り、効率的にサービスを利用していくための基盤を提供するものと言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルの引退日付の更新 | modified | 1 | 1 | 2 | 
| [models.md](#item-db2c37) | minor update | モデルのデプロイメント情報の更新 | modified | 4 | 4 | 8 | 
| [prompt-engineering.md](#item-884584) | minor update | タイトルの順序の変更 | modified | 1 | 1 | 2 | 
| [provisioned-throughput.md](#item-022e0c) | minor update | DeepSeekモデルのバージョン情報の更新 | modified | 1 | 1 | 2 | 
| [prompt-caching.md](#item-1631df) | minor update | プロンプトキャッシングに関する情報の更新 | modified | 2 | 4 | 6 | 
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | プロビジョンドスループットのオンボーディングに関する情報の更新 | modified | 9 | 9 | 18 | 
| [responses.md](#item-b9757d) | minor update | レスポンスAPIのサポートに関する情報の修正 | modified | 0 | 1 | 1 | 
| [new-inference-preview.md](#item-bd665f) | minor update | 新しい推論プレビューに関する情報の更新 | modified | 321 | 321 | 642 | 
| [provisioned-global.md](#item-340884) | minor update | プロビジョニングされたグローバルモデルマトリックスの更新 | modified | 28 | 28 | 56 | 
| [models.md](#item-5cd5bf) | minor update | モデルの引退日付の更新 | modified | 13 | 13 | 26 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 06/11/2025
+ms.date: 06/25/2025
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの引退日付の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIに関する「モデルの引退」についての文書における日付の更新を示しています。具体的には、ドキュメントのメタデータに記載されている日付が「2025年6月11日」から「2025年6月25日」に変更されました。この変更は、モデルの引退に関する最新の情報を反映させることを目的としています。ファイルへの変更の詳細は、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/blob/a20162d4fec2039483a274ec493eba18935ef4fe/articles/ai-services/openai/concepts/model-retirements.md)から確認できます。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about the different model capabilities that are available wit
 author: mrbullwinkle #ChrisHMSFT
 ms.author: mbullwin #chrhoder#
 manager: nitinme
-ms.date: 06/16/2025
+ms.date: 06/25/2025
 ms.service: azure-ai-openai
 ms.topic: conceptual
 ms.custom:
@@ -49,9 +49,9 @@ Azure OpenAI is powered by a diverse set of models with different capabilities a
 
 |  Model ID  | Description | Context Window | Max Output Tokens | Training Data (up to)  |
 |  --- |  :--- |:--- |:---|:---: |
-| `gpt-4.1` (2025-04-14)   | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | - 1,047,576 <br> - 128,000 (provisioned managed deployments) | 32,768 | May 31, 2024 |
-| `gpt-4.1-nano` (2025-04-14) | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | - 1,047,576  <br> - 128,000 (provisioned managed deployments)  | 32,768 | May 31, 2024 |
-| `gpt-4.1-mini` (2025-04-14) | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | - 1,047,576  <br> - 128,000 (provisioned managed deployments)  | 32,768 | May 31, 2024 |
+| `gpt-4.1` (2025-04-14)   | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | - 1,047,576 <br> - 128,000 (provisioned managed deployments) <br> - 300,000 (batch deployments) | 32,768 | May 31, 2024 |
+| `gpt-4.1-nano` (2025-04-14) | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | - 1,047,576  <br> - 128,000 (provisioned managed deployments) <br> - 300,000 (batch deployments)  | 32,768 | May 31, 2024 |
+| `gpt-4.1-mini` (2025-04-14) | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | - 1,047,576  <br> - 128,000 (provisioned managed deployments) <br> - 300,000 (batch deployments)  | 32,768 | May 31, 2024 |
 
 ## model-router
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのデプロイメント情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスに関する「モデル」ドキュメントの更新を示しています。この変更では、以下の2点が重要です。

1. **日付の更新**: ドキュメント内の更新日付が「2025年6月16日」から「2025年6月25日」に変更されました。この変更は、最新の情報に基づくものです。
  
2. **モデル情報の追加**: 各モデルの「コンテキストウィンドウ」に関する情報が補足され、バッチデプロイメントに関する詳細が追加されました。具体的には、`gpt-4.1`、`gpt-4.1-nano`、`gpt-4.1-mini`の各モデルについて、128,000トークンのプロビジョニングされた管理デプロイメントに加えて、新たに300,000トークンのバッチデプロイメントが記載されるようになりました。

これにより、ユーザーはモデルの能力に関する最新の情報をよく理解できるようになります。ファイルの詳細は、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/blob/a20162d4fec2039483a274ec493eba18935ef4fe/articles/ai-services/openai/concepts/models.md)から確認できます。

## articles/ai-services/openai/concepts/prompt-engineering.md{#item-884584}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Azure OpenAI in Azure AI Foundry Models | Prompt engineering techniques
+title:  Prompt engineering techniques | Azure OpenAI in Azure AI Foundry Models
 titleSuffix: Azure OpenAI
 description: Learn how to use prompt engineering to optimize your work with Azure OpenAI.
 ms.service: azure-ai-openai
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "タイトルの順序の変更"
}
```

### Explanation
このコードの変更は、Azure OpenAIに関する「プロンプトエンジニアリング」ドキュメントのタイトルの更新を示しています。具体的には、タイトルの項目の順序が変更されました。「Azure OpenAI in Azure AI Foundry Models | Prompt engineering techniques」という元のタイトルが、「Prompt engineering techniques | Azure OpenAI in Azure AI Foundry Models」に書き換えられています。この変更により、ドキュメントの内容がより明確に反映され、プロンプトエンジニアリングの技術が強調される形となっています。ファイルの詳細は、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/blob/a20162d4fec2039483a274ec493eba18935ef4fe/articles/ai-services/openai/concepts/prompt-engineering.md)から確認できます。

## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -192,7 +192,7 @@ The following points are some important takeaways from the table:
 |                    | O4 mini          | ✅                 | ✅                     | ✅                   | ✅                 |
 | **Azure DeepSeek** | DeepSeek-R1      | ✅                 |                       |                      |                   |
 |                    | DeepSeek-V3-0324 | ✅                 |                       |                      |                   |
-
+|                    | DeepSeek-R1-0528 | ✅                 |                       |                      |                   |
 
 
 ### Region availability for provisioned throughput capability
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DeepSeekモデルのバージョン情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスに関連する「プロビジョンドスループット」に関するドキュメントの更新を示しています。具体的には、テーブル内のモデル情報が修正されています。

変更点は以下の通りです：

- **モデルバージョンの更新**: 「DeepSeek-R1」のモデルのバージョン情報が「DeepSeek-R1」から「DeepSeek-R1-0528」に変更されました。これにより、最新のモデルを利用する際の情報が正確になります。

この変更は、ユーザーが利用可能なモデルに関する透明性を高め、最新情報へのアクセスを容易にするものです。ファイルの詳細は、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/blob/a20162d4fec2039483a274ec493eba18935ef4fe/articles/ai-services/openai/concepts/provisioned-throughput.md)から確認できます。

## articles/ai-services/openai/how-to/prompt-caching.md{#item-1631df}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 04/14/2025
+ms.date: 06/25/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -33,9 +33,7 @@ Currently only the following models support prompt caching with Azure OpenAI:
 - `gpt-4o-mini-realtime-preview` (version 2024-12-17)
 - `gpt-4.1-2025-04-14`
 - `gpt-4.1-nano-2025-04-14`
-
-> [!NOTE]
-> Prompt caching is now also available as part of model fine-tuning for `gpt-4o` and `gpt-4o-mini`. Refer to the fine-tuning section of the [pricing page](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) for details.
+- `gpt-4.1-mini-2025-04-14`
 
 ## API support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトキャッシングに関する情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスに関する「プロンプトキャッシング」のドキュメントの更新を示しています。いくつかの重要な変更が加えられました。

1. **日付の更新**: ドキュメントの日付が「04/14/2025」から「06/25/2025」に変更されました。これは、コンテンツの最新性を示すものです。

2. **モデルに関する情報の更新**: プロンプトキャッシングをサポートするモデルのリストに、`gpt-4.1-mini-2025-04-14`という新しいモデルが追加されました。

3. **ノートセクションの削除**: プロンプトキャッシングが`gpt-4o`および`gpt-4o-mini`のモデルのファインチューニングの一部として利用可能であることを示すノートが削除されました。これにより、情報が簡潔に保たれています。

これらの変更は、ユーザーにとっての情報の明確さと最新性を向上させることを目的としています。ファイルの詳細は、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/blob/a20162d4fec2039483a274ec493eba18935ef4fe/articles/ai-services/openai/how-to/prompt-caching.md)から確認できます。

## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title:  Understanding costs associated with provisioned throughput units (PTU)
 description: Learn about provisioned throughput costs and billing in Azure AI Foundry. 
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 06/13/2025
+ms.date: 06/25/2025
 manager: nitinme
 author: aahill 
 ms.author: aahi 
@@ -77,14 +77,14 @@ The amount of throughput (measured in tokens per minute or TPM) a deployment get
 
 For example, for `gpt-4.1:2025-04-14`, 1 output token counts as 4 input tokens towards your utilization limit which matches the [pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). Older models use a different ratio and for a deeper understanding on how different ratios of input and output tokens impact the throughput your workload needs, see the [Azure AI Foundry PTU quota calculator](https://ai.azure.com/resource/calculator).
 
-|Topic| **o4-mini** | **gpt-4.1** | **gpt-4.1-mini** | **gpt-4.1-nano** | **o3** | **o3-mini** | **o1** | **gpt-4o** | **gpt-4o-mini** |  **DeepSeek-R1** | **DeepSeek-V3-0324** |
-| --- |  --- | --- |  --- |  --- | --- | --- | --- | --- | --- | --- | --- |
-|Global & data zone provisioned minimum deployment| 15 | 15|15| 15 | 15 |15|15|15|15| 100|100|
-|Global & data zone provisioned scale increment| 5 | 5|5| 5 | 5 |5|5|5|5|  100|100|
-|Regional provisioned minimum deployment|25| 50|25| 25 |50 | 25|25|50|25| NA|NA|
-|Regional provisioned scale increment|25| 50|25| 25 | 50 | 25|50|50|25|NA|NA|
-|Input TPM per PTU|5,400 | 3,000|14,900| 59,400 | 600 | 2,500|230|2,500|37,000|4,000|4,000|
-|Latency Target Value| 99% > 66 Tokens Per Second\* | 99% > 40 Tokens Per Second\* | 99% > 50 Tokens Per Second\*| 99% > 60 Tokens Per Second\* | 99% > 40 Tokens Per Second\* | 99% > 66 Tokens Per Second\* | 99% > 25 Tokens Per Second\* | 99% > 25 Tokens Per Second\* | 99% > 33 Tokens Per Second\* | 99% > 50 Tokens Per Second\*| 99% > 50 Tokens Per Second\*|
+|Topic| **o4-mini** | **gpt-4.1** | **gpt-4.1-mini** | **gpt-4.1-nano** | **o3** | **o3-mini** | **o1** | **gpt-4o** | **gpt-4o-mini** |  **DeepSeek-R1** | **DeepSeek-V3-0324** | **DeepSeek-R1-0528** |
+| --- |  --- | --- |  --- |  --- | --- | --- | --- | --- | --- | --- | --- | --- |
+|Global & data zone provisioned minimum deployment| 15 | 15|15| 15 | 15 |15|15|15|15| 100|100|100|
+|Global & data zone provisioned scale increment| 5 | 5|5| 5 | 5 |5|5|5|5|  100|100|100|
+|Regional provisioned minimum deployment|25| 50|25| 25 |50 | 25|25|50|25| NA|NA|NA|
+|Regional provisioned scale increment|25| 50|25| 25 | 50 | 25|50|50|25|NA|NA|NA|
+|Input TPM per PTU|5,400 | 3,000|14,900| 59,400 | 3,000 | 2,500|230|2,500|37,000|4,000|4,000|4,000|
+|Latency Target Value| 99% > 66 Tokens Per Second\* | 99% > 40 Tokens Per Second\* | 99% > 50 Tokens Per Second\*| 99% > 60 Tokens Per Second\* | 99% > 40 Tokens Per Second\* | 99% > 66 Tokens Per Second\* | 99% > 25 Tokens Per Second\* | 99% > 25 Tokens Per Second\* | 99% > 33 Tokens Per Second\* | 99% > 50 Tokens Per Second\*| 99% > 50 Tokens Per Second\*| 99% > 50 Tokens Per Second\*|
 
 \* Calculated as the average request latency on a per-minute basis across the month.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョンドスループットのオンボーディングに関する情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスにおける「プロビジョンドスループットのオンボーディング」に関するドキュメントの更新を示しています。主な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの日付が「06/13/2025」から「06/25/2025」に変更され、情報が最新であることを示しています。

2. **モデル情報の更新**: テーブルに新しいモデル「DeepSeek-R1-0528」が追加され、利用可能なモデルのリストが拡充されました。これにより、ユーザーは最新のモデルに基づいた情報を得ることができます。

3. **テーブルの内容の修正**: テーブル内の数値が修正されています。特に、`o3`および`gpt-4.1-nano`に関連する「Input TPM per PTU」や「Latency Target Value」の値が更新されており、これによって性能に関する重要な情報が改訂されています。

これらの変更は、Azure OpenAIサービスのユーザーが利用可能な最新の情報を得るために重要です。詳細については、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/blob/a20162d4fec2039483a274ec493eba18935ef4fe/articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md)を参照してください。

## articles/ai-services/openai/how-to/responses.md{#item-b9757d}

<details>
<summary>Diff</summary>
````diff
@@ -59,7 +59,6 @@ Not every model is available in the regions supported by the responses API. Chec
 > [!NOTE]
 > Not currently supported:
 > - The web search tool
-> - Fine-tuned models
 > - Image generation using multi-turn editing and streaming - coming soon
 > - Images can't be uploaded as a file and then referenced as input. Coming soon.
 >
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レスポンスAPIのサポートに関する情報の修正"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスにおける「レスポンスAPI」に関するドキュメントの修正を示しています。主な変更点は以下の通りです。

1. **情報の削除**: 「現在サポートされていない」項目のリストから「ファインチューニングされたモデル」が削除されました。これは、ファインチューニングされたモデルが今後サポートされる可能性を示唆するものでもあります。

2. **そのほかの情報の明確化**: 残りの項目は、現在サポートされていない機能として引き続き維持されており、ユーザーにとっての重要な情報が簡潔に整理されています。

この変更により、ユーザーはレスポンスAPIがどの機能をサポートしていないかについて最新の情報を得ることができます。詳細については、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/blob/a20162d4fec2039483a274ec493eba18935ef4fe/articles/ai-services/openai/how-to/responses.md)を参照してください。

## articles/ai-services/openai/includes/api-versions/new-inference-preview.md{#item-bd665f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しい推論プレビューに関する情報の更新"
}
```

### Explanation
このコードの変更は、「新しい推論プレビュー」に関するドキュメントの大規模な更新を示しています。主な変更点は以下の通りです。

1. **コンテンツの置き換え**: ファイル全体が更新され、321行が追加され、321行が削除されました。これにより、内容が全面的に見直され、最新の情報が反映されています。

2. **情報の更新**: 新しい推論プレビューに関する詳細な情報が追加され、機能や使用方法に関する説明が明確になりました。これにより、ユーザーは新しいAPIバージョンに関する最新の機能や使用方法を理解しやすくなっています。

3. **構造の改善**: ドキュメントは、ユーザーが情報をより簡単に参照できるように整形され、明確なセクションや見出しが設けられている可能性があります。

これらの変更は、新しい推論プレビューの理解を深めるために重要であり、Azure OpenAIサービスを利用している開発者やユーザーにとって価値のある情報が提供されています。詳細については、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/blob/a20162d4fec2039483a274ec493eba18935ef4fe/articles/ai-services/openai/includes/api-versions/new-inference-preview.md)を参照してください。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -8,31 +8,31 @@ ms.custom: references_regions
 ms.date: 05/05/2025
 ---
 
-| **Region**         | **o3**<br>2025-04-16 | **o4-mini**<br>2025-04-16 | **gpt-4.1**<br>2025-04-14 | **gpt-4.1-nano**<br>2025-04-14 | **gpt-4.1-mini**<br>2025-04-14 | **o3-mini**<br>2025-01-31 | **o1**<br>2024-12-17 | **gpt-4o**<br>2024-05-13 | **gpt-4o**<br>2024-08-06 | **gpt-4o**<br>2024-11-20 | **gpt-4o-mini**<br>2024-07-18 | **DeepSeek-R1** | **DeepSeek-V3-0324** |
-|:-------------------|:-------------------:|:------------------------:|:------------------------:|:-----------------------------:|:-----------------------------:|:------------------------:|:-------------------:|:------------------------:|:------------------------:|:------------------------:|:----------------------------:|:--------------:|:---------------------:|
-| australiaeast      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| brazilsouth        | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| canadaeast         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| eastus             | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| eastus2            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| francecentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| germanywestcentral | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| italynorth         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| japaneast          | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| koreacentral       | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| northcentralus     | ✅                   | ✅                        | ✅                        | -                              | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| norwayeast         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| polandcentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| southafricanorth   | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| southcentralus     | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| southeastasia      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| southindia         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| spaincentral       | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| swedencentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| switzerlandnorth   | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| switzerlandwest    | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| uaenorth           | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| uksouth            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| westeurope         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| westus             | ✅                   | ✅                        | ✅                        | -                              | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
-| westus3            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   |
\ No newline at end of file
+| **Region**         | **o3**<br>2025-04-16 | **o4-mini**<br>2025-04-16 | **gpt-4.1**<br>2025-04-14 | **gpt-4.1-nano**<br>2025-04-14 | **gpt-4.1-mini**<br>2025-04-14 | **o3-mini**<br>2025-01-31 | **o1**<br>2024-12-17 | **gpt-4o**<br>2024-05-13 | **gpt-4o**<br>2024-08-06 | **gpt-4o**<br>2024-11-20 | **gpt-4o-mini**<br>2024-07-18 | **DeepSeek-R1** | **DeepSeek-V3-0324** | **DeepSeek-R1-0528** |
+|:-------------------|:-------------------:|:------------------------:|:------------------------:|:-----------------------------:|:-----------------------------:|:------------------------:|:-------------------:|:------------------------:|:------------------------:|:------------------------:|:----------------------------:|:--------------:|:---------------------:|:---------------------:|
+| australiaeast      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| brazilsouth        | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| canadaeast         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| eastus             | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| eastus2            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| francecentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| germanywestcentral | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| italynorth         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| japaneast          | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| koreacentral       | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| northcentralus     | ✅                   | ✅                        | ✅                        | -                              | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| norwayeast         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| polandcentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| southafricanorth   | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| southcentralus     | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| southeastasia      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| southindia         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| spaincentral       | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| swedencentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| switzerlandnorth   | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| switzerlandwest    | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| uaenorth           | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| uksouth            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| westeurope         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| westus             | ✅                   | ✅                        | ✅                        | -                              | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
+| westus3            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅            | ✅                   | ✅                   |
\ No newline at end of file
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
このコードの変更は、「プロビジョニングされたグローバルモデルマトリックス」に関する情報を更新したことを示しています。主な変更点は以下の通りです。

1. **内容の置き換え**: ファイル内のデータが大幅に更新され、28行が新しく追加された一方で、同じ28行が削除されています。この変更により、情報が最新のものに置き換えられています。

2. **新しいモデルの追加**: テーブルに「DeepSeek-R1-0528」という新しいエントリーが追加され、様々なモデルと地域の対応状況がより明確になりました。

3. **地域別の情報更新**: 各地域におけるモデルの利用状況（例: 対応する地域、バージョンのリリース日など）が整理され、ユーザーにとっての利便性が向上しました。

この変更は、Azure OpenAIサービスを使用する開発者やユーザーが、現在利用可能なモデルやそのバージョンについて最新の情報を得るために重要です。詳細については、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/blob/a20162d4fec2039483a274ec493eba18935ef4fe/articles/ai-services/openai/includes/model-matrix/provisioned-global.md)を参照してください。

## articles/ai-services/openai/includes/retirement/models.md{#item-5cd5bf}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Model retirement table
 titleSuffix: Azure OpenAI in Azure AI Foundry Models
 description: Model retirement table for  Azure OpenAI in Azure AI Foundry Models
 manager: nitinme
-ms.date: 06/18/2025
+ms.date: 06/25/2025
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions, build-2025
@@ -41,18 +41,18 @@ ms.custom: references_regions, build-2025
 
 ### Audio
 
-| Model                          | Version         | Retirement date                    | Replacement model                    |
-| -------------------------------|-----------------|------------------------------------|--------------------------------------|
-| `gpt-4o-mini-realtime-preview` | 2024-12-17      | No earlier than July 2, 2025       |                                      |
-| `gpt-4o-realtime-preview`      | 2024-12-17      | No earlier than July 2, 2025       |                                      |
-| `gpt-4o-audio-preview`         | 2024-12-17      | No earlier than July 2, 2025       |                                      |
-| `gpt-4o-audio-preview`         | 2024-12-17      | No earlier than July 2, 2025       |                                      |
-| `gpt-4o-transcribe`            | 2025-03-20      | No earlier than August 11, 2025    |                                      |
-| `gpt-4o-mini-tts`              | 2025-03-20      | No earlier than August 11, 2025    |                                      |
-| `gpt-4o-mini-transcribe`       | 2025-03-20      | No earlier than August 11, 2025    |                                      |
-| `tts`                          | 001             | No earlier than February 1, 2026   |                                      |
-| `tts-hd`                       | 001             | No earlier than February 1, 2026   |                                      |
-| `whisper`                      | 001             | No earlier than February 1, 2026   |                                      |
+| Model                          | Version         | Retirement date                          | Replacement model                    |
+| -------------------------------|-----------------|------------------------------------------|--------------------------------------|
+| `gpt-4o-mini-realtime-preview` | 2024-12-17      | No earlier than September 17, 2025       |                                      |
+| `gpt-4o-realtime-preview`      | 2024-12-17      | No earlier than September 17, 2025       |                                      |
+| `gpt-4o-audio-preview`         | 2024-12-17      | No earlier than September 17, 2025       |                                      |
+| `gpt-4o-audio-preview`         | 2024-12-17      | No earlier than September 17, 2025       |                                      |
+| `gpt-4o-transcribe`            | 2025-03-20      | No earlier than September 17, 2025       |                                      |
+| `gpt-4o-mini-tts`              | 2025-03-20      | No earlier than September 17, 2025       |                                      |
+| `gpt-4o-mini-transcribe`       | 2025-03-20      | No earlier than September 17, 2025       |                                      |
+| `tts`                          | 001             | No earlier than February 1, 2026         |                                      |
+| `tts-hd`                       | 001             | No earlier than February 1, 2026         |                                      |
+| `whisper`                      | 001             | No earlier than February 1, 2026         |                                      |
 
 # [Image & Video](#tab/image)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの引退日付の更新"
}
```

### Explanation
このコードの変更は、「モデルの引退」に関する情報を最新化したことを示しています。主な変更点は以下の通りです。

1. **引退日付の変更**: いくつかのモデルの引退日付が「2025年7月2日」から「2025年9月17日」に変更されました。これにより、利用者はモデルのサポート終了時期を正確に把握できるようになります。

2. **内容の置き換え**: 13行が追加され、同じ数の行が削除されることによって、テーブルが更新されています。これにより、退役する予定のモデルに関する情報が最新のものに置き換えられました。

3. **一貫性の向上**: モデルのリストが見やすく整形され、各モデルのバージョンや引退日の情報が一目でわかるようになります。

この変更は、Azure OpenAIサービスを使用している開発者や企業が、どのモデルが引退し、どのモデルが引き続き利用可能かを把握しやすくするために重要です。詳細については、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/blob/a20162d4fec2039483a274ec493eba18935ef4fe/articles/ai-services/openai/includes/retirement/models.md)を参照してください。


