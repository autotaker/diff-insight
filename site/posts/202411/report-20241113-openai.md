---
date: '2024-11-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d63c476...MicrosoftDocs:51e566e
summary: このコード差分では、Azure OpenAIサービスに関連する文書が更新され、特にモデルの退役日やデフォルトモデルの更新スケジュールが明示されています。`babbage-002`および`davinci-002`の退役日が変更され、ユーザーは移行スケジュールを再評価する必要があります。また、APIに関するクオタや制限についての最新情報が提供され、リアルタイム機能の使用時には接続数の制限があることが強調されています。この情報は、開発者がAzure
  OpenAIサービスを利用する際の計画や運用に重要です。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d63c476...MicrosoftDocs:51e566e){target="_blank"}

# ハイライト

このコード差分では、Azure OpenAIサービスに関連する文書が以下のように更新されました。

- **新機能**: モデルの更新および廃止日が明示され、特定のモデルに関連するスケジュールが明確化されました。
- **重要な変更点**: `babbage-002`、`davinci-002`の退役日、`gpt-35-turbo`、`gpt-4o`のデフォルトモデルの更新スケジュールの変更。
- **その他の更新**: 使用可能なクオタや制限に関する情報が最新化され、API使用時の制限が詳細に記されています。

## 新機能

- `text-embedding-3-small`及び`text-embedding-3-large`の退役日が追加され、利用者がこれらのモデルのサポートについて最新情報を知ることができるようになりました。

## 重要な変更点

- `babbage-002`および`davinci-002`モデルの退役日が変更されました。これにより、これらのモデルを使用するユーザーは、移行スケジュールを再評価する必要があります。
- `gpt-35-turbo`および`gpt-4o`のデフォルトモデル更新のスケジュールが調整されました。

## その他の更新

- `gpt-4o-realtime-preview`のリクエスト数に関する新しい情報が追加され、リアルタイム音声用接続数が1分間に6回に制限されることが示されました。
- カスタムヘッダーに関する制限の詳細が調整され、ヘッダー数を超過するとHTTP 431エラーが発生する可能性が強調されました。

# インサイト

このドキュメントの更新は、Azure OpenAIサービスを利用する開発者にとって重要な情報です。OpenAIモデルの退役スケジュール変更とデフォルトモデルの更新は、長期的なプロジェクト計画や運用に直接影響を及ぼすため、ユーザーはスケジュールを慎重に見直す必要があります。

クオタと制限に関する更新は、特にAPI経由でリアルタイム機能を活用する開発者にとってのガイドラインとして機能します。接続制限やHTTPエラーハンドリングを考慮に入れたAPI設計への反映が必要であり、これにより信頼性の高いサービスが提供可能になります。クオタ増加リクエストのプロセスと制限事項も明確になったため、リクエストプロセスの理解とプレパレーションがより効率的になるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルの更新と廃止に関する変更 | modified | 23 | 12 | 35 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クオタおよび制限に関する更新 | modified | 4 | 3 | 7 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 10/25/2024
+ms.date: 11/11/2024
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -91,26 +91,26 @@ These models are currently available for use in Azure OpenAI Service.
 
 | Model | Version | Retirement date | Suggested replacements |
 | ---- | ---- | ---- | --- |
-| `babbage-002` | 1 | Deprecation Date: November 15, 2024 <br>Retirement Date: January 27, 2025 | |
-| `davinci-002` | 1 | Deprecation Date: November 15, 2024 <br>Retirement Date: January 27, 2025 | |
+| `babbage-002` | 1 | Retirement Date: January 27, 2025 | |
+| `davinci-002` | 1 | Retirement Date: January 27, 2025 | |
 | `dall-e-2`| 2 | January 27, 2025 | `dalle-3` |
 | `dall-e-3` | 3 | No earlier than April 30, 2025 | |
-| `gpt-35-turbo` | 0301 | January 27, 2025<br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024.   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
-| `gpt-35-turbo`<br>`gpt-35-turbo-16k` | 0613 | January 27, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024.  | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
-| `gpt-35-turbo` | 1106 | No earlier than January 27, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
-| `gpt-35-turbo` | 0125 | No earlier than Feb 22, 2025 | `gpt-4o-mini` |
+| `gpt-35-turbo` | 0301 | February 13, 2025<br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025.   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
+| `gpt-35-turbo`<br>`gpt-35-turbo-16k` | 0613 | February 13, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025.  | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
+| `gpt-35-turbo` | 1106 | No earlier than January 27, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
+| `gpt-35-turbo` | 0125 | No earlier than March 31, 2025 | `gpt-4o-mini` |
 | `gpt-4`<br>`gpt-4-32k` | 0314 | June 6, 2025 | `gpt-4o` |
 | `gpt-4`<br>`gpt-4-32k` | 0613 | June 6, 2025 | `gpt-4o` |
 | `gpt-4` | 1106-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025 **<sup>1</sup>** | `gpt-4o`|
 | `gpt-4` | 0125-preview |To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025 **<sup>1</sup>**  | `gpt-4o` |
 | `gpt-4` | vision-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025  **<sup>1</sup>** | `gpt-4o`|
-| `gpt-4o` | 2024-05-13 | No earlier than May 20, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on December 5, 2024. | |
+| `gpt-4o` | 2024-05-13 | No earlier than May 20, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on February 13, 2025. | |
 | `gpt-4o-mini` | 2024-07-18 | No earlier than July 18, 2025  | |
 | `gpt-3.5-turbo-instruct` | 0914 | No earlier than Sep 14, 2025 |  |
 | `text-embedding-ada-002` | 2 | No earlier than April 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
 | `text-embedding-ada-002` | 1 | No earlier than April 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
-| `text-embedding-3-small` | | No earlier than Feb 2, 2025 | |
-| `text-embedding-3-large` | | No earlier than Feb 2, 2025 | |
+| `text-embedding-3-small` | | No earlier than April 3, 2025 | |
+| `text-embedding-3-large` | | No earlier than April 3, 2025 | |
 
  **<sup>1</sup>** We will notify all customers with these preview deployments at least 30 days before the start of the upgrades. We will publish an upgrade schedule detailing the order of regions and model versions that we will follow during the upgrades, and link to that schedule from here.
 
@@ -121,8 +121,8 @@ These models are currently available for use in Azure OpenAI Service.
 
 | Model | Current default version | New default version | Default upgrade date |
 |---|---|---|---|
-| `gpt-35-turbo` | 0301 | 0125 | Deployments of versions `0301`, `0613`, and `1106` set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024.|
-|  `gpt-4o` | 2024-05-13 | 2024-08-06 | Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on December 5, 2024. |
+| `gpt-35-turbo` | 0301 | 0125 | Deployments of versions `0301`, `0613`, and `1106` set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025.|
+|  `gpt-4o` | 2024-05-13 | 2024-08-06 | Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on February 13, 2025. |
 
 ## Deprecated models
 
@@ -162,6 +162,17 @@ If you're an existing customer looking for information about these models, see [
 
 ## Retirement and deprecation history
 
+## November 11, 2024
+
+Updates to:
+
+- `babbage-002`, `davinci-002`.
+- `gpt-35-turbo` DEFAULT model version update date.
+- `gpt-35-turbo` 0301, 0613 retirement date.
+- `gpt-35-turbo` 0125 retirement date.
+- `gpt-4o` DEFAULT model update date.
+- `text-embeddings-3-small` & `text-embedding-3-large` retirement date.
+
 ## October 25, 2024
 
 * `babbage-002` & `davinci-002` deprecation date: November 15, 2024  and retirement date: January 27, 2025.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの更新と廃止に関する変更"
}
```

### Explanation
この変更では、Azure OpenAIサービスにおけるモデルの廃止および更新に関する情報が更新されました。具体的には、いくつかのモデルに関する日付が修正され、退役日やデフォルトモデルの更新日が調整されました。特に、`babbage-002`および`davinci-002`の退役日が更新され、さらに`gpt-35-turbo`や`gpt-4o`のデフォルトモデルの更新スケジュールも変更されています。また、新しい退役日が追加され、`text-embedding-3-small`および`text-embedding-3-large`モデルの退役日が明確に示されています。これにより、ユーザーは使用中のモデルの今後のサポート状況とタイミングを把握しやすくなります。全体として、内容の整合性が向上し、最新の情報が利用できるようになっています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 10/23/2024
+ms.date: 11/11/2024
 ms.author: mbullwin
 ---
 
@@ -51,8 +51,9 @@ The following sections provide you with a quick guide to the default quotas and
 | GPT-4o max images per request (# of images in the messages array/conversation history) | 10 |
 | GPT-4 `vision-preview` & GPT-4 `turbo-2024-04-09` default max tokens | 16 <br><br> Increase the `max_tokens` parameter value to avoid truncated responses. GPT-4o max tokens defaults to 4096. |
 | Max number of custom headers in API requests<sup>1</sup> | 10 |
+| Max number requests per minute<br/><br/>Current rate limits for real time audio (`gpt-4o-realtime-preview`) are defined as the number of new websocket connections per minute. For example, 6 request per minute (RPM) means 6 new connections per minute. At this time, the usage limits for `gpt-4o-realtime-preview` are suitable for test and development. | 6 new connections per minute |
 
-<sup>1</sup> Our current APIs allow up to 10 custom headers, which are passed through the pipeline, and returned. We have noticed some customers now exceed this header count resulting in HTTP 431 errors. There is no solution for this error, other than to reduce header volume. **In future API versions we will no longer pass through custom headers**. We recommend customers not depend on custom headers in future system architectures.
+<sup>1</sup> Our current APIs allow up to 10 custom headers, which are passed through the pipeline, and returned. Some customers now exceed this header count resulting in HTTP 431 errors. There's no solution for this error, other than to reduce header volume. **In future API versions we will no longer pass through custom headers**. We recommend customers not depend on custom headers in future system architectures.
 
 ## Regional quota limits
 
@@ -180,7 +181,7 @@ To minimize issues related to rate limits, it's a good idea to use the following
 
 ### How to request increases to the default quotas and limits
 
-Quota increase requests can be submitted from the [Quotas](./how-to/quota.md) page of Azure AI Studio. Note that due to overwhelming demand, quota increase requests are being accepted and will be filled in the order they are received. Priority will be given to customers who generate traffic that consumes the existing quota allocation, and your request might be denied if this condition isn't met.
+Quota increase requests can be submitted from the [Quotas](./how-to/quota.md) page of Azure AI Studio. Due to high demand, quota increase requests are being accepted and will be filled in the order they're received. Priority is given to customers who generate traffic that consumes the existing quota allocation, and your request might be denied if this condition isn't met.
 
 For other rate limits, [submit a service request](../cognitive-services-support-options.md?context=/azure/ai-services/openai/context/context).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クオタおよび制限に関する更新"
}
```

### Explanation
この変更では、Azure OpenAIサービスにおけるクオタと制限に関する情報が更新されました。主な内容としては、ドキュメントの日付が変更され、`gpt-4o-realtime-preview`のリクエスト数に関する新しい情報が追加されました。具体的には、リアルタイム音声用の接続数制限が明確にされ、1分間に最大6回の新しい接続が許可されることが記されています。さらに、カスタムヘッダーの制限に関する説明が調整され、ヘッダーの数を超えるとHTTP 431エラーが発生する可能性があることが強調されました。この変更により、ユーザーがAPIの現在の制限と利用可能な選択肢を理解しやすく、適切に対処できるようになります。また、クオタ増加リクエストの受け付けに関する文言もクリアにされ、変更内容が整理されています。


