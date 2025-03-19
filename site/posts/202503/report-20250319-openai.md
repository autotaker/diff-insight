---
date: '2025-03-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b32e527...MicrosoftDocs:144811f
summary: 新機能として、GPT-4 プレビューモデルの引退日が2025年5月1日に延長され、埋め込みの次元数に関するドキュメントが最新のAPIバージョンに対応して更新されました。破壊的変更は特にありませんが、関連するシステムがそれに適応する必要があります。また、合計で10箇所が修正され、7行が追加、3行が削除されています。これにより、ユーザーはより安心してモデルを利用でき、最新の機能を最大限に活用できるようになります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b32e527...MicrosoftDocs:144811f){target="_blank"}

# ハイライト

## 新機能
- GPT-4 プレビューモデルの引退日が2025年5月1日に延長されました。
- 埋め込みの次元数に関するドキュメントが最新のAPIバージョン（2024-10-21）に対応して更新されました。

## 破壊的変更
- 特に破壊的な変更はありませんが、モデル引退日に関する情報や API バージョンに関する情報を参照しているシステムは、それらの更新への適応が必要です。

## その他の更新
- 合計で10箇所が修正され、7行が追加、3行が削除されています。

# 洞察

このコードの変更は、Azure OpenAI サービスのユーザーにとって重要な情報を更新するものです。まず、GPT-4 プレビューモデルの引退日が2025年4月2日から2025年5月1日に変更されたことで、ユーザーはモデルの使用期限により余裕を持って準備を進めることができるようになりました。これにより、特に長期的なプロジェクトやモデルへの依存度が高いアプリケーションでは、安定した計画が可能となります。

さらに、埋め込みの次元数に関する更新は、最新のAPIバージョン（2024-10-21）に対応することで、ユーザーが最適なパフォーマンスと最新の機能を活用できるようにするためのものです。次元数に関する仕様は、データの処理能力やモデルの動作に直接影響を与えるため、特に重要です。

これらの変更は、ユーザーが最新かつ正確な情報に基づいてサービスを利用できるように、ドキュメントの信頼性と透明性を高めることを目的としています。また、アップデートされた情報は、モデルの利用戦略やAPIの活用方法を見直す際のガイドとして役立つでしょう。こうした定期的な情報更新は、サービスの品質維持とユーザーエクスペリエンスの向上に寄与します。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルの引退日が更新されました | modified | 7 | 3 | 10 | 
| [azure-search.md](#item-32f34c) | minor update | 埋め込みの次元数に関する情報が更新されました | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -100,9 +100,9 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-4`<br>`gpt-4-32k` | 0314 | June 6, 2025 | `gpt-4o` |
 | `gpt-4`<br>`gpt-4-32k` | 0613 | June 6, 2025 | `gpt-4o` |
 | `gpt-4` | turbo-2024-04-09 | No earlier than June 6, 2025 | `gpt-4o`|
-| `gpt-4` | 1106-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than March 10, 2025 **<sup>1</sup>** <br>Retirement date: April 02, 2025  | `gpt-4o`|
-| `gpt-4` | 0125-preview |To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than March 10, 2025 **<sup>1</sup>** <br>Retirement date: April 02, 2025  | `gpt-4o` |
-| `gpt-4` | vision-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than March 10, 2025  **<sup>1</sup>** <br>Retirement date: April 02, 2025 | `gpt-4o`|
+| `gpt-4` | 1106-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than March 10, 2025 **<sup>1</sup>** <br>Retirement date: May 1, 2025  | `gpt-4o`|
+| `gpt-4` | 0125-preview |To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than March 10, 2025 **<sup>1</sup>** <br>Retirement date: May 1, 2025  | `gpt-4o` |
+| `gpt-4` | vision-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than March 10, 2025  **<sup>1</sup>** <br>Retirement date: May 1, 2025 | `gpt-4o`|
 | `gpt-4o` | 2024-05-13 | No earlier than June 30, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on March 17, 2025. | |
 | `gpt-4o` | 2024-08-06 | No earlier than August 6, 2025  | |
 | `gpt-4o` | 2024-11-20 | No earlier than November 20, 2025  | |
@@ -171,6 +171,10 @@ If you're an existing customer looking for information about these models, see [
 
 ## Retirement and deprecation history
 
+## March 18, 2025
+
+GPT-4 preview models retirement date updated to date: May 1, 2025.
+
 ## February 28, 2025
 
 - Updated `gpt-4` versions `1106-preview`, `0125-preview`, `vision-preview` to be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than March 10, 2025.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの引退日が更新されました"
}
```

### Explanation
この変更は、Azure OpenAI サービスで利用可能な GPT-4 プレビューモデルの引退日を更新した内容です。具体的には、引退日が2025年4月2日から2025年5月1日に変更されました。この修正により、ユーザーはモデルが利用可能である期間をより正確に把握できるようになります。また、他の関連情報やモデルのアップグレードに関する注意事項も強調されています。修正内容は、全体で10箇所にわたる変更があり、7行追加され、3行削除されています。変更の詳細は、指定されたファイルのパッチで確認できます。

## articles/ai-services/openai/references/azure-search.md{#item-32f34c}

<details>
<summary>Diff</summary>
````diff
@@ -95,7 +95,7 @@ The details of the vectorization source, used by Azure OpenAI On Your Data when
 | `endpoint`|string|True|Specifies the resource endpoint URL from which embeddings should be retrieved. It should be in the format of `https://{YOUR_RESOURCE_NAME}.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME/embeddings`. The api-version query parameter isn't allowed.|
 | `authentication`| [ApiKeyAuthenticationOptions](#api-key-authentication-options)|True | Specifies the authentication options to use when retrieving embeddings from the specified endpoint.|
 | `type`|string|True| Must be `endpoint`.|
-| `dimensions`|integer|False| The number of dimensions the embeddings should have. Only supported in `text-embedding-3` and later models. |
+| `dimensions`|integer|False| The number of dimensions the embeddings should have. Only supported in `text-embedding-3` and later models. This is supported in the api version 2024-10-21. |
 
 
 ## Fields mapping options
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "埋め込みの次元数に関する情報が更新されました"
}
```

### Explanation
この変更は、Azure OpenAI サービスにおける埋め込みに関連するドキュメントの一部を更新した内容です。具体的には、`dimensions` フィールドに関する説明が更新されました。従来の情報に加え、API バージョン 2024-10-21 でのサポートが明示的に記載されています。これにより、ユーザーは埋め込みの次元数における使用可能なバージョンについて、より具体的な情報を得ることができます。修正は1行の追加と1行の削除からなり、全体として2箇所の変更が行われています。変更の詳細は、指定されたファイルのパッチで確認できます。


