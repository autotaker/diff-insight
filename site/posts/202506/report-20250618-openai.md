---
date: '2025-06-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ba67d73...MicrosoftDocs:2e48ee2
summary: 新しい文書では、特定のOpenAIモデルのバージョンやクォータ制限についての情報が更新され、明確化されました。大きな破壊的変更はありませんが、一部の既存モデル情報が削除されています。また、地域別のモデル利用可能性やAPIサポートに関する情報も整理され、可読性が向上しました。この変更は、ユーザーが最新の情報にアクセスしやすくすることを目的としており、特にAzure
  Government OpenAIサービスの更新や予測出力ドキュメントの更新、クォータ・リミットの強化が行われています。これにより、技術者や企業ユーザーは情報をもとに効果的なプランニングが可能になり、リソースの無駄を最小限に抑えることが期待されます。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ba67d73...MicrosoftDocs:2e48ee2){target="_blank"}

# ハイライト

## 新機能
- 文書がアップデートされ、特定のOpenAIモデルのバージョンやクォータ制限に関する情報が明確化されました。

## 破壊的変更
- 特に破壊的な変更は報告されていませんが、既存のモデル情報が一部削除されています。

## その他の更新
- 地域別モデルの利用可能性と、APIサポートに関する細部が整理・明示化されて文書の可読性が向上しました。

# 洞察

このコード差分による変更は、Microsoft Azureが提供するOpenAIサービスに関する文書の質を向上させるためのものであり、ユーザーが求める最新情報にアクセスしやすくなるよう調整されています。具体的には、複数の文書において以下の3つの主要な変更ポインが見て取れます。

1. **Azure Government OpenAI サービス更新**:
   - モデルの地域別利用可能性がより明確に示され、クォータ制限が更新されました。これにより、ユーザーはどのモデルがどの地域で利用可能か、そしてその制限がどうなっているかを把握しやすくなっています。

2. **予測出力ドキュメントの更新**:
   - 特に日付変更や新モデル（gpt-4.1-nano、gpt-4.1-mini）が追加され、ユーザーは利用可能なモデルのバージョンをより正確に把握できます。また、APIサポート情報が明示化され、過去のリリースも含め、それぞれのAPIが今後どのようにサポートされるかが示されています。

3. **クォータ・リミット情報の強化**:
   - GPT-4o と GPT-4.1に関するリクエスト制限が整理され、ユーザーはこのモデルペアのリクエスト制限を明確に理解しやすくなっています。

これらの変更は主に、提供される情報の精度を上げ、クライアントが最適な利用戦略を構築するための手助けとなるように詳細化されたものです。技術者や企業ユーザーは、これをもとに自分たちの使用状況に適したプランニングが可能になり、リソースの無駄を最小限に抑えることができるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-government.md](#item-a47549) | minor update | Azure Government OpenAI サービスに関する情報更新 | modified | 11 | 11 | 22 | 
| [predicted-outputs.md](#item-212eb9) | minor update | 予測出力に関する情報の更新 | modified | 4 | 2 | 6 | 
| [quotas-limits.md](#item-06c6f9) | minor update | GPT-4oおよびGPT-4.1のリクエスト制限に関する情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/azure-government.md{#item-a47549}

<details>
<summary>Diff</summary>
````diff
@@ -26,10 +26,10 @@ The following sections show model availability by region and deployment type. Mo
 <br>
 
 ## Standard deployment model availability
-|   **Region**  | **o3-mini USGov DataZone** | **gpt-4o**, **2024-05-13** | **gpt-4o-mini**, **2024-07-18** | **gpt-4**, **1106-Preview** | **gpt-35-turbo**, **0125** | **text-embedding-3-large**, **1** | **text-embedding-3-small**, **1** | **text-embedding-ada-002**, **2** |
-|:--------------|:--------------------------:|:--------------------------:|:-------------------------------:|:---------------------------:|:--------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|
-| usgovarizona  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| usgovvirginia | ✅ | ✅ | -  | ✅ | ✅ | - | - | ✅ |
+|   **Region**  | **o3-mini USGov DataZone** | **gpt-4o**, **2024-05-13** | **gpt-4o-mini**, **2024-07-18** | **gpt-35-turbo**, **0125** | **text-embedding-3-large**, **1** | **text-embedding-3-small**, **1** | **text-embedding-ada-002**, **2** |
+|:--------------|:--------------------------:|:--------------------------:|:-------------------------------:|:--------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|
+| usgovarizona  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
+| usgovvirginia | ✅ | ✅ | -  | ✅ | - | - | ✅ |
 
 * USGov DataZone provides access to the model from both usgovarizona and usgovvirginia.
 * Data stored at rest remains in the designated Azure region of the resource.
@@ -39,17 +39,17 @@ Data zone standard deployments are available in the same Azure OpenAI resource a
 
 To request quota increases for these models, submit a request at [https://aka.ms/AOAIGovQuota](https://aka.ms/AOAIGovQuota). Note the following maximum quota limits allowed via that form:
 
-| **gpt-4o** | **gpt-4o-mini** | **gpt-4** | **gpt-35-turbo** | **text-embedding-3-large** | **text-embedding-ada-002**|
-|:----------:|:---------------:|:---------:|:----------------:|:--------------------------:|:-------------------------:|
-|    300k    |      600k       |    200k   |      500k        |            700k            |           700k            |
+| **gpt-4o** | **gpt-4o-mini** | **gpt-35-turbo** | **text-embedding-3-large** | **text-embedding-ada-002**|
+|:----------:|:---------------:|:----------------:|:--------------------------:|:-------------------------:|
+|    300k    |      600k       |      500k        |            700k            |           700k            |
 
 <br>
 
 ## Provisioned deployment model availability
-|   **Region**  | **gpt-4o**, **2024-05-13** | **gpt-4o-mini**, **2024-07-18** | **gpt-4**, **1106-Preview** | **gpt-35-turbo**, **0125** |
-|:--------------|:--------------------------:|:-------------------------------:|:---------------------------:|:--------------------------:|
-| usgovarizona  | ✅ | - | - | ✅ |
-| usgovvirginia | ✅ | - | - | ✅ |
+|   **Region**  | **gpt-4o**, **2024-05-13** | **gpt-4o-mini**, **2024-07-18** | **gpt-35-turbo**, **0125** |
+|:--------------|:--------------------------:|:-------------------------------:|:--------------------------:|
+| usgovarizona  | ✅ | - | ✅ |
+| usgovvirginia | ✅ | - | ✅ |
 
 <br>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Government OpenAI サービスに関する情報更新"
}
```

### Explanation
このコードの変更は、MicrosoftのAzure GovernmentにおけるOpenAIサービスの文書に関するものであり、主にモデルの提供状況とクォータ制限に関する情報が更新されています。具体的には、モデルの地域別の利用可能性を示すテーブルのフォーマットが変更され、以前のテーブルよりも情報が整理されています。また、モデルごとの最大クォータ制限が明確になり、特定のモデル（gpt-4o-miniやgpt-35-turboなど）のデータが削除されています。

変更は全体で22行に及び、11行の追加と11行の削除が行われました。これにより、文書がより簡潔かつ理解しやすくなっています。また、新しいリンクが提供され、クォータ増加リクエストの手続きについての情報も引き続き含まれています。それにより、Azure Governmentユーザーは利用可能なモデルとその最大制約についての詳細をより容易に把握できるようになっています。

## articles/ai-services/openai/how-to/predicted-outputs.md{#item-212eb9}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 04/14/2025
+ms.date: 06/17/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -22,10 +22,12 @@ Predicted outputs can improve model response latency for chat completions calls
 - `gpt-4o` version: `2024-08-06`
 - `gpt-4o` version: `2024-11-20`
 - `gpt-4.1` version: `2025-04-14`
+- `gpt-4.1-nano` version: `2025-04-14`
+- `gpt-4.1-mini` version: `2025-04-14`
 
 ## API support
 
-- `2025-01-01-preview`
+First introduced in `2025-01-01-preview`. Supported in all subsequent releases. 
 
 ## Unsupported features
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "予測出力に関する情報の更新"
}
```

### Explanation
このコードの変更は、Microsoft AzureのOpenAIサービスに関連する「予測出力」のドキュメントにおける情報の更新を行ったものです。主に、ドキュメントの日付、モデルバージョン、APIサポート情報を更新しています。

具体的には、最初に示されていた日付が「2025年4月14日」から「2025年6月17日」へ変更され、最新の情報が反映されています。また、新たに「gpt-4.1-nano」と「gpt-4.1-mini」というモデルが追加され、それぞれのバージョン日付が「2025年4月14日」として記載されています。これにより、ユーザーは利用可能なモデルのバージョンをより正確に把握することができます。

さらに、APIサポートに関する情報も明確化され、「2025-01-01-preview」という初めてのリリースが全ての後続リリースでサポートされていることが強調されました。このような更新により、ドキュメントの正確性と有用性が向上しています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ The following sections provide you with a quick guide to the default quotas and
 | Max file size for Assistants & fine-tuning | 512 MB<br/><br/>200 MB via [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) |
 | Max size for all uploaded files for Assistants |200 GB |
 | Assistants token limit | 2,000,000 token limit |
-| GPT-4o max images per request (# of images in the messages array/conversation history) | 50 |
+| GPT-4o and GPT-4.1 max images per request (# of images in the messages array/conversation history) | 50 |
 | GPT-4 `vision-preview` & GPT-4 `turbo-2024-04-09` default max tokens | 16 <br><br> Increase the `max_tokens` parameter value to avoid truncated responses. GPT-4o max tokens defaults to 4096. |
 | Max number of custom headers in API requests<sup>1</sup> | 10 |
 | Message character limit | 1048576 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4oおよびGPT-4.1のリクエスト制限に関する情報の更新"
}
```

### Explanation
このコードの変更は、AzureのOpenAIサービスに関する「クォータと制限」の文書において、GPT-4oおよびGPT-4.1に関するリクエストの制限に関する情報が更新されたものです。具体的には、GPT-4oのリクエストにおける最大画像数に関する記述が変更されました。

以前は「GPT-4o max images per request」として記載されていましたが、更新後は「GPT-4o and GPT-4.1 max images per request」となり、GPT-4.1も含まれることが明示化されています。この変更により、ユーザーはこれらのモデルが共有する同一のリクエスト制限をより明確に理解できるようになりました。

全体として、この変更はクォータに関する情報を最新のものにすることで、ユーザーがリクエスト制限を適切に把握し、その利用に役立てることを目的としています。


