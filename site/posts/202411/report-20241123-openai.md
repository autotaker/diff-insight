---
date: '2024-11-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:567d1b1...MicrosoftDocs:ccb6fcd
summary: この記事では、Azure OpenAIドキュメントにおけるいくつかのマイナーアップデートを紹介しています。主なポイントは、引退日の新設定、プロビジョニングされたスループット情報の拡充、およびクォータと制限情報の更新です。特に、`gpt-35-turbo`の退役日が2025年3月31日に変更されたことや、GPT-4oモデルに関する最大リクエスト画像数が10から50に増加したことが挙げられます。今回の変更には互換性を壊す要素は含まれておらず、ユーザー体験が向上しています。これらの更新は、ユーザーがAzureサービスの利用をよりスムーズに行えるように支援することを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:567d1b1...MicrosoftDocs:ccb6fcd){target="_blank"}

# ハイライト
この記事では、Azure OpenAIドキュメントにおける数カ所のマイナーアップデートについて説明しています。注目のポイントは、新しい引退日の設定、プロビジョニングされたスループット情報の拡充、そしてクォータと制限情報の更新です。

## 新機能
特記すべき新機能はありませんが、情報の更新と修正により、ユーザー体験が向上しています。

## 互換性を壊す変更
今回の変更には互換性を壊すような変更は含まれていません。

## その他の更新
- `gpt-35-turbo`の退役日が2025年3月31日に変更。
- `gpt-4o`および`gpt-4o-mini`のスループット計算に関する情報が明確化。
- GPT-4oモデルに関する最大リクエスト画像数が10から50に増加。

# インサイト
Azure OpenAIのドキュメントに対するこれらのマイナーアップデートは、ユーザーに対する情報提供をより明確にし、Azureサービスの利用を円滑にすることを意図しています。特にモデルの退役日やプロビジョニングされたスループットに関する情報は、計画的なリソース管理と負荷分散を行う上で重要な要素です。

更新された退役日については、ユーザーが頻繁にチェックする必要はありませんが、長期間のサービス利用計画においては非常に重要です。同様に、スループットに関する詳細な情報は、適切な性能を確保するための基礎知識を提供します。これにより、Azure OpenAIのキャパシティ計算機を用いた綿密な計算が可能となり、サービスの負荷管理が改善されるでしょう。

さらに、クォータと制限に関する情報更新によって、ユーザーは性能とリソースのバランスをより簡単に維持できるようになります。特に、画像リクエストの増加は、画像処理を行うアプリケーションにとっての一つのメリットと言えます。скажем

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルの引退日更新: gpt-35-turbo (1106) の日付を修正 | modified | 6 | 2 | 8 | 
| [provisioned-throughput.md](#item-022e0c) | minor update | プロビジョニングされたスループットに関する情報の追加と修正 | modified | 7 | 4 | 11 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータと制限に関する情報の更新 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 11/11/2024
+ms.date: 11/22/2024
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -97,7 +97,7 @@ These models are currently available for use in Azure OpenAI Service.
 | `dall-e-3` | 3 | No earlier than April 30, 2025 | |
 | `gpt-35-turbo` | 0301 | February 13, 2025<br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025.   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
 | `gpt-35-turbo`<br>`gpt-35-turbo-16k` | 0613 | February 13, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025.  | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
-| `gpt-35-turbo` | 1106 | No earlier than January 27, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
+| `gpt-35-turbo` | 1106 | No earlier than March 31, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
 | `gpt-35-turbo` | 0125 | No earlier than March 31, 2025 | `gpt-4o-mini` |
 | `gpt-4`<br>`gpt-4-32k` | 0314 | June 6, 2025 | `gpt-4o` |
 | `gpt-4`<br>`gpt-4-32k` | 0613 | June 6, 2025 | `gpt-4o` |
@@ -162,6 +162,10 @@ If you're an existing customer looking for information about these models, see [
 
 ## Retirement and deprecation history
 
+## November 22, 2024
+
+`gpt-35-turbo` 1106 retirement date updated to no earlier than March 31, 2025. 
+
 ## November 11, 2024
 
 Updates to:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの引退日更新: gpt-35-turbo (1106) の日付を修正"
}
```

### Explanation
この変更は、Azure OpenAIのドキュメントに対する小規模な更新です。主に、`gpt-35-turbo`モデルの引退日が修正されました。この修正では、以前は2025年1月27日とされていた引退日が、2025年3月31日以降に変更されました。変更に伴い、関連する情報に更新が加えられ、他のモデルの利用可能日や自動アップデートに関するリンクも明記されています。

具体的には、ドキュメント内の日前の情報を最新の引退日情報に調整し、さらなる詳細を提供するための内容が新たに追加されています。この情報は、モデルの使い方やアップデートの計画に影響を与えるため、Azure OpenAIのサービスを利用しているユーザーにとって重要な情報です。

## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -41,14 +41,17 @@ An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model.
 ## How much throughput per PTU you get for each model
 The amount of throughput (tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in the minute. Generating output tokens requires more processing than input tokens and so the more output tokens generated the lower your overall TPM. The service dynamically balances the input & output costs, so users do not have to set specific input and output limits. This approach means your deployment is resilient to fluctuations in the workload shape. 
 
-To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the `gpt-4o` and `gpt-4o-mini` models which represent the max all the traffic is either input or output. The table also shows Service Level Agreement (SLA) Latency Target Values per model.  For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page].(https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
+To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the `gpt-4o` and `gpt-4o-mini` models which represent the max TPM assuming all traffic is either input or output. To understand how different ratios of input and output tokens impact your Max TPM per PTU, see the [Azure OpenAI capacity calculator](https://oai.azure.com/portal/calculator). The table also shows Service Level Agreement (SLA) Latency Target Values per model.  For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
 
-|     | **gpt-4o**, **2024-05-13**   & **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
+|| **gpt-4o**, **2024-05-13**   & **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
 | --- | --- | --- |
-| Deployable Increments | 50 | 25|
+|Global provisioned minimum deployment|15|15|
+|Global provisioned scale increment|5|5|
+| Regional provisioned minimum deployment | 50 | 25|
+|Regional provisioned scale increment|50|25|
 |Max Input TPM per PTU | 2,500 | 37,000  |
 |Max Output TPM per PTU| 833|12,333|
-| Latency Target Value |25 Tokens Per Second* |33 Tokens Per Second*|
+| Latency Target Value |25 Tokens Per Second|33 Tokens Per Second|
 
 For a full list see the [AOAI Studio calculator](https://oai.azure.com/portal/calculator).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされたスループットに関する情報の追加と修正"
}
```

### Explanation
この変更は、Azure OpenAIのプロビジョニングされたスループットに関するドキュメントの小規模な更新です。主に、`gpt-4o`および`gpt-4o-mini`モデルのスループットに関する情報をより明確にし、ユーザーにとって負荷の変動に対する理解を助けるための内容が追加されました。

具体的には、以下の変更が行われました：
- 最大TPM（トークン毎分）を計算する際の入出力トークンの比率がどのように影響するかについての理解を深めるための情報が追加され、Azure OpenAIのキャパシティ計算機へのリンクが提供されました。
- テーブルの構造が一部修正され、デプロイ可能な最小規模やスケール増分に関する情報が詳述されました。
- SLA（サービスレベル合意）についての情報も引き続き強調され、新たに具体的な数値の形式が変更されています。

この更新により、ユーザーは自らのニーズに合わせた適切なスループットの計算がより簡単に行えるようになります。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -29,7 +29,7 @@ The following sections provide you with a quick guide to the default quotas and
 | Default DALL-E 3 quota limits| 2 capacity units (6 requests per minute)|
 | Default Whisper quota limits | 3 requests per minute |
 | Maximum prompt tokens per request | Varies per model. For more information, see [Azure OpenAI Service models](./concepts/models.md)|
-| Max Standard deployments per resource | 32 | 
+| Max Standard deployments per resource | 32 |
 | Max fine-tuned model deployments | 5 |
 | Total number of training jobs per resource | 100 |
 | Max simultaneous running training jobs per resource | 1 |
@@ -46,9 +46,9 @@ The following sections provide you with a quick guide to the default quotas and
 | Maximum number of Provisioned throughput units per deployment | 100,000 |
 | Max files per Assistant/thread | 10,000 when using the API or AI Studio. 20 when using Azure OpenAI Studio.|
 | Max file size for Assistants & fine-tuning | 512 MB |
-| Max size for all uploaded files for Assistants |100 GB |  
+| Max size for all uploaded files for Assistants |100 GB |
 | Assistants token limit | 2,000,000 token limit |
-| GPT-4o max images per request (# of images in the messages array/conversation history) | 10 |
+| GPT-4o max images per request (# of images in the messages array/conversation history) | 50 |
 | GPT-4 `vision-preview` & GPT-4 `turbo-2024-04-09` default max tokens | 16 <br><br> Increase the `max_tokens` parameter value to avoid truncated responses. GPT-4o max tokens defaults to 4096. |
 | Max number of custom headers in API requests<sup>1</sup> | 10 |
 | Max number requests per minute<br/><br/>Current rate limits for real time audio (`gpt-4o-realtime-preview`) are defined as the number of new websocket connections per minute. For example, 6 request per minute (RPM) means 6 new connections per minute. At this time, the usage limits for `gpt-4o-realtime-preview` are suitable for test and development. | 6 new connections per minute |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータと制限に関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIのクォータと制限に関するドキュメントに対する小規模な更新です。主に、特定のリソースにおける最大デプロイ数やリクエストに関する情報が整理され、数値が明確化されました。

具体的な変更点は以下の通りです：
- GPT-4oモデルに関する最大リクエストの画像数が、10から50に増加しました。これにより、ユーザーはより多くの画像を一度に要求できるようになります。
- いくつかの項目が見直され、一貫性のある形式で整理されています。例えば、リソースにおける最大標準デプロイ数やファイルサイズの制限が確認されました。
- その他、クォータに関連した数値の確認が行われ、適切なリソース制限の理解を助けるよう改善されています。

この更新により、ユーザーはAzure OpenAIを利用する際の制限やクォータについての理解を深め、効率的にリソースを管理できるようになります。


