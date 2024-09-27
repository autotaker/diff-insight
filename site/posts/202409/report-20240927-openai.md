---
date: '2024-09-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5e7dab7...MicrosoftDocs:552467e
summary: この報告書は、Azure OpenAIモデルのリタイアメントに関する日付が更新されたことを説明しています。具体的には、「gpt-35-turbo」のリタイアメント日が2024年11月17日から2025年1月27日に変更され、ユーザーにとって移行の余裕が生まれました。また、文中の日付も更新され、情報の一貫性が保たれています。新機能や破壊的変更はなく、重要な情報の正確性を向上させるための修正です。これにより、ユーザーは安心してAzure
  OpenAIサービスを利用し続けることができます。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5e7dab7...MicrosoftDocs:552467e){target="_blank"}

# ハイライト
このコードの変更点は、Azure OpenAIモデルのリタイアメントに関する日付の更新です。具体的には、モデルの引退日が2つ変更されました。

## 新機能
この更新に新機能は含まれていませんが、情報の正確性と最新性を保つための重要な修正です。

## 破壊的変更
新しい破壊的変更は含まれていません。

## その他の更新
- 文書内の日付更新
- テーブル内のリタイアメント日付の更新

# 洞察
今回のドキュメント更新はとてもシンプルですが、ユーザーにとって非常に重要です。Azure OpenAIの「モデルリタイアメント」に関する情報は、ユーザーがそのサービスを利用する計画を立てる上で重要な指標となります。特に、モデルの廃止日が近い場合、そのモデルに依存するシステムやアプリケーションを適宜更新する必要があります。

このドキュメントの更新により、「gpt-35-turbo」のリタイアメント日付が元の「2024年11月17日」から「2025年1月27日」に変更されました。これはユーザーにとって、移行期間が延長されることを意味しており、計画を立てる際の余裕が生まれます。

また、文中の日付も「2024年9月12日」から「2024年9月26日」に更新されました。これにより全体の一貫性が保たれ、ユーザーは常に最新の情報にアクセスすることができます。これらの変更は小さいように見えますが、信頼性を確保するためには欠かせない更新です。

したがって、今回の変更によってユーザーは安心してAzure OpenAIサービスを利用し続けることができるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルのリタイアメント日付の更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 09/12/2024
+ms.date: 09/26/2024
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -93,7 +93,7 @@ These models are currently available for use in Azure OpenAI Service.
 | ---- | ---- | ---- | --- |
 | `gpt-35-turbo` | 0301 | January 27, 2025<br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024.   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
 | `gpt-35-turbo`<br>`gpt-35-turbo-16k` | 0613 | January 27, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024.  | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
-| `gpt-35-turbo` | 1106 | No earlier than Nov 17, 2024 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
+| `gpt-35-turbo` | 1106 | No earlier than January 27, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
 | `gpt-35-turbo` | 0125 | No earlier than Feb 22, 2025 | `gpt-4o-mini` |
 | `gpt-4`<br>`gpt-4-32k` | 0314 | June 6, 2025 | `gpt-4o` |
 | `gpt-4`<br>`gpt-4-32k` | 0613 | June 6, 2025 | `gpt-4o` |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのリタイアメント日付の更新"
}
```

### Explanation
この変更は、Azure OpenAIのモデルリタイアメントに関する文書の更新です。主に、以下の2つの変更が加えられています。

1. 文章中の日付が更新され、具体的には元の日付である「2024年9月12日」が「2024年9月26日」に変更されました。
2. テーブル内の「gpt-35-turbo」モデルのリタイア日付が、元の「2024年11月17日」から「2025年1月27日」へと変更されています。

これにより、最新のモデルのリタイアメント情報を正確に反映し、ユーザーに信頼性のある情報を提供することを目的としています。変更点は2行追加され、2行が削除される形で行われています。


