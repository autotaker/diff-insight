---
date: '2025-05-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:df7d67e...MicrosoftDocs:2280088
summary: Azure OpenAIサービスの最新アップデートには、新しい「コンピュータ利用プレビュー」モデルの追加や、モデル退職に関する情報が整理されていることが含まれます。APIバージョン指定方法の変更が示されており、開発者にとって適切な実装が奨励される一方、特に重大な変更はありません。その他の更新としては、モデルの退職日と推奨置き換えモデルの情報の更新や、ダイナミッククォータ設定手順の修正、Responses
  APIでのサポートされない機能に関する詳細が追加されています。これらの変更は、ユーザーエクスペリエンスの向上と情報提供の充実を目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:df7d67e...MicrosoftDocs:2280088){target="_blank"}

<format>
# Highlights

## New features
- Azure OpenAIサービスで新しい「コンピュータ利用プレビュー」モデルが追加。
- モデル退職に関する情報が整理され、利用者へのガイダンスを改善。

## Breaking changes
- 特に重大な変更点はありませんが、APIバージョン指定方法の変更は、開発者がAPIを利用する際の適切な実装を促します。

## Other updates
- モデルの退職日や推奨置き換えモデルの情報が更新。
- ダイナミッククォータ設定手順のAPIバージョン指定方法の修正。
- Responses APIでサポートされない機能についての詳細情報が追加。

# Insights

この一連のアップデートは、Azure OpenAIサービスの利用に関する情報を最新に保ち、ユーザーエクスペリエンスを向上させることを目的としています。まず、モデル退職に関するドキュメント更新では、ユーザーが将来計画を立てやすくするため、特定のモデルの利用可否を把握しやすいようになっています。モデル退職日に関する情報が明確化されたことで、計画的なシステム移行やアップデートが行いやすくなるでしょう。

次に、ダイナミッククォータのAPIバージョン指定方法の修正は、APIを使用するエンジニアにとって非常に重要です。これにより、APIの呼び出し時にバージョンの不整合を避け、最新の機能やパッチを確実に取り込めるようになります。

最後に、Responses APIのドキュメント更新では、サポートされない機能に関する情報が明示されています。これにより、開発者が予期せぬ機能制限に直面するリスクを低減し、サービスの利用計画やトラブルシューティングが容易になります。特に、ビジョンパフォーマンスに関する既知の問題についても情報が提供されている点で、透過性のあるコミュニケーションが図られていると言えます。これらの変更は、ユーザーに対する情報提供を充実させると同時に、信頼性の高いサービス利用をサポートするためのものです。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデル退職に関する情報の更新 | modified | 35 | 33 | 68 | 
| [dynamic-quota.md](#item-b774ca) | minor update | APIバージョン指定の修正 | modified | 1 | 1 | 2 | 
| [responses.md](#item-b9757d) | minor update | レスポンスAPIの制限に関する情報の更新 | modified | 3 | 2 | 5 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -91,39 +91,41 @@ For more information on how to manage model upgrades and migrations for provisio
 
 These models are currently available for use in Azure OpenAI Service.
 
-| Model | Version | Retirement date | Suggested replacements |
-| ---- | ---- | ---- | --- |
-| `dall-e-3` | 3 | No earlier than June 30, 2025 | |
-| `gpt-35-turbo-16k`| 0613 | April, 30, 2025 | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
-| `gpt-35-turbo` | 1106 | July 16, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 21, 2025. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
-| `gpt-35-turbo` | 0125 | July 16, 2025 | `gpt-4o-mini` |
-| `gpt-4`<br>`gpt-4-32k` | 0314 | June 6, 2025 | `gpt-4o` |
-| `gpt-4`<br>`gpt-4-32k` | 0613 | June 6, 2025 | `gpt-4o` |
-| `gpt-4` | turbo-2024-04-09 | No earlier than June 6, 2025 | `gpt-4o`|
-| `gpt-4` | 1106-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025 **<sup>1</sup>** <br>Retirement date: May 1, 2025  | `gpt-4o`|
-| `gpt-4` | 0125-preview |To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025 **<sup>1</sup>** <br>Retirement date: May 1, 2025  | `gpt-4o` |
-| `gpt-4` | vision-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than April 17, 2025  **<sup>1</sup>** <br>Retirement date: May 15, 2025 | `gpt-4o`|
-| `gpt-4.5-preview` | 2025-02-27 | July 14, 2025 | `gpt-4.1` |
-| `gpt-4.1` | 2025-04-14 | No earlier than April 11, 2026 | |
-| `gpt-4.1-mini` | 2025-04-14 | No earlier than April 11, 2026 |
-| `gpt-4.1-nano` | 2025-04-14 | No earlier than April 11, 2026 |
-| `gpt-4o` | 2024-05-13 | No earlier than June 30, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on March 17, 2025. | |
-| `gpt-4o` | 2024-08-06 | No earlier than August 6, 2025  | |
-| `gpt-4o` | 2024-11-20 | January 30, 2026  | |
-| `gpt-4o-mini` | 2024-07-18 | August 16, 2025  | |
-| `gpt-3.5-turbo-instruct` | 0914 | No earlier than May 31, 2025 |  |
-| `o1-preview` | 2024-09-12 | May 29, 2025 | `o1` |
-| `o1` | 2024-12-17 | No earlier than December 17, 2025 | |
-| `o4-mini` | 2025-04-16 | No earlier than April 11, 2026 | |
-| `o3` | 2025-04-16 | No earlier than April 11, 2026 | |
-| `o3-mini` | 2025-01-31 | No earlier than February 1, 2026 | |
-| `text-embedding-ada-002` | 2 | No earlier than April 30, 2026 | `text-embedding-3-small` or `text-embedding-3-large` |
-| `text-embedding-ada-002` | 1 | No earlier than April 30, 2026 | `text-embedding-3-small` or `text-embedding-3-large` |
-| `text-embedding-3-small` | | No earlier than April 30, 2026 | |
-| `text-embedding-3-large` | | No earlier than April 30, 2026 | |
-
-
- **<sup>1</sup>** We'll notify all customers with these preview deployments at least 30 days before the start of the upgrades. We'll publish an upgrade schedule detailing the order of regions and model versions that we'll follow during the upgrades, and link to that schedule from here.
+| Model                     | Version         | Retirement date                    | Replacement model                    |
+| --------------------------|-----------------|------------------------------------|--------------------------------------|
+| `computer-use-preview`    | 2025-03-11      | No earlier than June 11, 2025      |                                      |
+| `dall-e-3`                | 3               | No earlier than June 30, 2025      |                                      |
+| `gpt-35-turbo-16k`        | 0613            | April, 30, 2025                    | `gpt-4.1-mini` version: `2025-04-14` |
+| `gpt-35-turbo`            | 1106            | No earlier than July 16, 2025      | `gpt-4.1-mini` version: `2025-04-14` |
+| `gpt-35-turbo`            | 0125            | No earlier than July 16, 2025      | `gpt-4.1-mini` version: `2025-04-14` |
+| `gpt-4`<br>`gpt-4-32k`    | 0314            | June 6, 2025                       | `gpt-4o` version: `2024-11-20`       |
+| `gpt-4`<br>`gpt-4-32k`    | 0613            | June 6, 2025                       | `gpt-4o` version: `2024-11-20`       |
+| `gpt-4`                   | turbo-2024-04-09| No earlier than June 6, 2025       | `gpt-4o` version: `2024-11-20`       |
+| `gpt-4`                   | 1106-preview    | May 1, 2025                        | `gpt-4o` version: `2024-11-20`       |
+| `gpt-4`                   | 0125-preview    | May 1, 2025                        | `gpt-4o` version: `2024-11-20`        |
+| `gpt-4`                   | vision-preview  | May 15, 2025                       | `gpt-4o` version: `2024-11-20`       |
+| `gpt-4.5-preview`         | 2025-02-27      | No Auto-upgrades <br>July 14, 2025 | `gpt-4.1` version: `2025-04-14`      |
+| `gpt-4.1`                 | 2025-04-14      | No earlier than April 11, 2026     |                                      |
+| `gpt-4.1-mini`            | 2025-04-14      | No earlier than April 11, 2026     |                                      |
+| `gpt-4.1-nano`            | 2025-04-14      | No earlier than April 11, 2026     |                                      |
+| `gpt-4o`                  | 2024-05-13      | No earlier than June 30, 2025      | `gpt-4.1` version: `2025-04-14`      |
+| `gpt-4o`                  | 2024-08-06      | No earlier than August 6, 2025     | `gpt-4.1` version: `2025-04-14`      |
+| `gpt-4o`                  | 2024-11-20      | No earlier than January 30, 2026   | `gpt-4.1` version: `2025-04-14`      |
+| `gpt-4o-mini`             | 2024-07-18      | August 16, 2025                    |                                      |
+| `gpt-3.5-turbo-instruct`  | 0914            | No earlier than May 31, 2025       |                                      |
+| `gpt-image-1`             | 2025-04-15      | No earlier than August 01, 2025    |                                      |
+| `o1-preview`              | 2024-09-12      | May 29, 2025                       | `o1`                                 |
+| `o1`                      | 2024-12-17      | No earlier than December 17, 2025  |                                      |
+| `o4-mini`                 | 2025-04-16      | No earlier than April 11, 2026     |                                      |
+| `o3`                      | 2025-04-16      | No earlier than April 11, 2026     |                                      |
+| `o3-mini`                 | 2025-01-31      | No earlier than February 1, 2026   |                                      |
+| `text-embedding-ada-002`  | 2               | No earlier than April 30, 2026     | `text-embedding-3-small` or `text-embedding-3-large` |
+| `text-embedding-ada-002`  | 1               | No earlier than April 30, 2026     | `text-embedding-3-small` or `text-embedding-3-large` |
+| `text-embedding-3-small`  |                 | No earlier than April 30, 2026     |                                      |
+| `text-embedding-3-large`  |                 | No earlier than April 30, 2026     |                                      |
+
+
+We'll notify all customers with these preview deployments at least 30 days before the start of the upgrades. We'll publish an upgrade schedule detailing the order of regions and model versions that we'll follow during the upgrades, and link to that schedule from here.
 
 > [!TIP]
 > **Will a model upgrade happen if the new model version is not yet available in that region?**
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル退職に関する情報の更新"
}
```

### Explanation
この変更では、Azure OpenAIサービスにおけるモデル退職に関する情報を更新しています。具体的には、利用可能なモデルとそのバージョンに関する詳細が整理され、新しい「コンピュータ利用プレビュー」などの追加モデルが加えられています。また、各モデルの退職日や推奨される置き換えモデルも更新されています。変更は主にテーブル形式での情報整理で、合計68行におよび、35行の追加と33行の削除があります。最終的に、利用者がモデルのアップグレードや退職についての最新の状態を把握しやすくなっています。

## articles/ai-services/openai/how-to/dynamic-quota.md{#item-b774ca}

<details>
<summary>Diff</summary>
````diff
@@ -60,7 +60,7 @@ Alternatively, you can enable it programmatically with Azure CLI's [`az rest`](/
 Replace the `{subscriptionId}`, `{resourceGroupName}`, `{accountName}`, and `{deploymentName}` with the relevant values for your resource. In this case, `accountName` is equal to Azure OpenAI resource name.
 
 ```azurecli
-az rest --method patch --url "https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/deployments/{deploymentName}?2023-10-01-preview" --body '{"properties": {"dynamicThrottlingEnabled": true} }'
+az rest --method patch --url "https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/deployments/{deploymentName}?api-version=2023-10-01-preview" --body '{"properties": {"dynamicThrottlingEnabled": true} }'
 ```
 
 ### How do I know how much throughput dynamic quota is adding to my app?
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョン指定の修正"
}
```

### Explanation
この変更では、Azure CLIを使用したダイナミッククォータの設定手順において、APIバージョンの指定方法が修正されています。元のコードでは"2023-10-01-preview"がURLの一部として直接記述されていましたが、新しい修正では"api-version=2023-10-01-preview"という形式に変更され、より明確にAPIバージョンが指定されるようになりました。この修正は、APIの呼び出しに関連する設定を正確に行うための重要な改善です。変更は合計2行で、1行の追加と1行の削除が含まれています。

## articles/ai-services/openai/how-to/responses.md{#item-b9757d}

<details>
<summary>Diff</summary>
````diff
@@ -56,8 +56,9 @@ Not every model is available in the regions supported by the responses API. Chec
 > Not currently supported:
 > - Structured outputs
 > - image_url pointing to an internet address
-> - The web search tool is also not supported, and is not part of the `2025-03-01-preview` API.  
-> 
+> - The web search tool
+> - Fine-tuned models
+>
 > There is also a known issue with vision performance when using the Responses API, particularly with OCR tasks. As a temporary workaround set image detail to `high`. This article will be updated once this issue is resolved and as any additional feature support is added.
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レスポンスAPIの制限に関する情報の更新"
}
```

### Explanation
この変更では、Responses APIに関するドキュメントの内容が更新され、現在サポートされていない機能についての情報が追加されています。具体的には、"ウェブ検索ツール"と"ファインチューニングモデル"がサポートされていないことが明示されました。変更は合計5行で、3行の追加と2行の削除が行われています。この更新により、ユーザーはResponses APIを使用する際の制限についてより明確な理解を得ることができ、適切な利用方法を選択できるようになります。また、ビジョンパフォーマンスに関する既知の問題についても注意喚起が含まれており、問題が解決され次第、情報が更新される旨が記載されています。


