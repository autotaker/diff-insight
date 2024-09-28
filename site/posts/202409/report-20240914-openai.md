---
date: '2024-09-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:022de22...MicrosoftDocs:3b0d11e
summary: 今回のコード差分では、Azure OpenAIサービス関連ドキュメントに新しいモデル情報を追加し、既存のモデル情報を更新するマイナーな変更が行われました。具体的には、「o1-preview」および「o1-mini」モデルの利用制限に関する詳細セクションが新たに追加され、モデルの登録手続きやMicrosoftの適格基準についての情報も更新されました。現在、特に破壊的な変更はなく、情報の新鮮さを保つために日付が修正されています。この変更により、ユーザーは新モデルの機能や利便性をより理解しやすくなり、Azure
  OpenAIサービスの活用が促進されることが期待されます。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:022de22...MicrosoftDocs:3b0d11e){target="_blank"}

# ハイライト
今回のコード差分は、Azure OpenAIサービス関連ドキュメントに新しいモデル情報を追加し、既存のモデル情報を更新するマイナーな変更です。

## 新機能

- 新しい「o1-preview」および「o1-mini」モデルの利用制限に関する詳細セクションが追加されました。

## 破壊的変更

- 現時点では特にありません。

## その他の更新

- モデル利用のための登録手続きおよびMicrosoftの適格基準についての情報が追加されました。
- 情報の新鮮さを保つために日付が修正されました。

# インサイト
このコード差分の主な目的は、Azure OpenAIサービスに関するドキュメントを最新の状態に保つことです。新しい「o1-preview」および「o1-mini」モデルに関する情報が追加され、これによりユーザーは新モデルの機能と制限を理解しやすくなります。

特に注目すべき点は以下の通りです：

1. **新モデルの概要と利用制限**:
   - 「o1-preview」および「o1-mini」モデルが新たに追加され、主に推論や問題解決に優れていることが強調されています。
   - これらのモデルは「East US2」地域で限定的にアクセス可能であることが明記されています。

2. **登録手続きと適格基準**:
   - これらの新モデルを利用するためには、登録手続きが必要であり、Microsoftの定める適格基準に基づいてアクセスが許可される旨が新たに詳細に説明されています。

3. **用途と具体的な機能の説明**:
   - 新モデルの具体的な利用シナリオとして、複雑なコード生成、問題解決、文書比較、指示の実行、ワークフロー管理といった機能が追加されました。

これらの変更は、ユーザーがAzure OpenAIサービスを活用しやすくするための情報整備として非常に意義があります。特に、モデルの地域制限や登録手続きの詳細情報を提供することで、実際の利用におけるハードルを下げる一助となるでしょう。また、新機能の提供により、Azure OpenAIサービスの魅力がさらに増すことでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | Azure OpenAIモデル情報の更新 | modified | 18 | 1 | 19 | 
| [whats-new.md](#item-53303b) | minor update | Azure OpenAIサービスの新機能追加 | modified | 44 | 1 | 45 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 09/09/2024
+ms.date: 09/12/2024
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -26,6 +26,23 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 | [Whisper](#whisper-models) | A series of models in preview that can transcribe and translate speech to text. |
 | [Text to speech](#text-to-speech-models-preview) (Preview) | A series of models in preview that can synthesize text to speech. |
 
+## o1-preview and o1-mini models limited access
+
+The Azure OpenAI `o1-preview` and `o1-mini` models are specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
+
+### Availability
+
+The `o1-preview` and `o1-mini` models are available in the East US2 region for limited access through the [AI Studio](https://ai.azure.com) early access playground. Data processing for the `o1` models may occur in a different region than where they are available for use.
+
+To try the `o1-preview` and `o1-mini` models in the early access playground, **registration is required, and access will be granted based on Microsoft’s eligibility criteria**.
+
+Request access: [limited access model application](https://aka.ms/oai/modelaccess)
+
+Once access has been granted, you will need to:
+
+1. Navigate to https://ai.azure.com/resources and select a resource in the `eastus2` region. If you do not have an Azure OpenAI resource in this region you will need to [create one](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI).  
+2. Once the `eastus2` Azure OpenAI resource is selected, in the upper left-hand panel under **Playgrounds** select **Early access playground (preview)**.
+
 ## GPT-4o and GPT-4 Turbo
 
 GPT-4o integrates text and images in a single model, enabling it to handle multiple data types simultaneously. This multimodal approach enhances accuracy and responsiveness in human-computer interactions. GPT-4o matches GPT-4 Turbo in English text and coding tasks while offering superior performance in non-English languages and vision tasks, setting new benchmarks for AI capabilities.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIモデル情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのモデルに関する情報を更新するもので、主にドキュメント内の一部内容を追加し、日付を修正しています。特に、新しい「o1-preview」と「o1-mini」モデルの利用制限についてのセクションが追加されました。この更新により、これらのモデルが特に推論や問題解決タスクに優れていること、そして「East US2」地域で限定的なアクセスが可能であることが明記されています。新たに追加された内容には、モデルを利用するための登録手続きが必要であり、Microsoftの適格基準に基づいてアクセスが許可される旨が含まれています。このような情報の追加は、ユーザーに対してAzure OpenAIサービスの最新情報を提供することを目的としています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -10,14 +10,57 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: whats-new
-ms.date: 9/03/2024
+ms.date: 9/12/2024
 recommendations: false
 ---
 
 # What's new in Azure OpenAI Service
 
 This article provides a summary of the latest releases and major documentation updates for Azure OpenAI.
 
+## September 2024
+
+### NEW o1-preview and o1-mini models available for limited access
+
+The Azure OpenAI `o1-preview` and `o1-mini` models are specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
+
+### Key capabilities of the o1 series
+
+- Complex Code Generation: Capable of generating algorithms and handling advanced coding tasks to support developers.
+- Advanced Problem Solving: Ideal for comprehensive brainstorming sessions and addressing multifaceted challenges.
+- Complex Document Comparison: Perfect for analyzing contracts, case files, or legal documents to identify subtle differences.
+- Instruction Following and Workflow Management: Particularly effective for managing workflows requiring shorter contexts.
+
+### Model variants
+
+- `o1-preview`: `o1-preview` is the more capable of the `o1` series models.  
+- `o1-mini`: `o1-mini` is the faster and cheaper of the `o1` series models.
+
+Model version: `2024-09-12`
+
+Request access: [limited access model application](https://aka.ms/oai/modelaccess)
+
+### Limitations
+
+The `o1-preview` and `o1-mini` models are currently in preview and do not include some features available in other models, such as image understanding and structured outputs found in the GPT-4o and GPT-4o-mini models. For many tasks, the generally available GPT-4o models may still be more suitable.
+
+### Safety
+
+OpenAI has incorporated additional safety measures into the `o1` models, including new techniques to help the models refuse unsafe requests. These advancements make the `o1` series some of the most robust models available.
+
+### Availability
+
+The `o1-preview` and `o1-mini` are available in the East US2 region for limited access through the [AI Studio](https://ai.azure.com) early access playground. Data processing for the `o1` models may occur in a different region than where they are available for use.
+
+To try the `o1-preview` and `o1-mini` models in the early access playground **registration is required, and access will be granted based on Microsoft’s eligibility criteria.**
+
+Request access: [limited access model application](https://aka.ms/oai/modelaccess)
+
+Once access has been granted, you will need to:
+
+1. Navigate to https://ai.azure.com/resources and select a resource in the `eastus2` region. If you do not have an Azure OpenAI resource in this region you will need to [create one](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI).  
+2. Once the `eastus2` Azure OpenAI resource is selected, in the upper left-hand panel under **Playgrounds** select **Early access playground (preview)**.
+ 
 ## August 2024
 
 ### GPT-4o 2024-08-06 structured outputs
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスの新機能追加"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスに関する最新情報を提供するために行われたもので、新しい「o1-preview」と「o1-mini」モデルに関する詳細が追加されました。この更新により、これらのモデルが推論や問題解決タスクに特化して設計されていることが強調されています。具体的な機能として、複雑なコード生成、問題解決、文書比較、指示の実行およびワークフロー管理が挙げられています。また、モデルの利用には限定的なアクセスが必要であり、安全性に関する新しい措置も導入されていることが説明されています。さらに、アクセスにはMicrosoftの適格基準に基づく登録手続きが必要であることも明記されています。このように、最新機能に関する情報を包括的に提供することを目的とした変更となっています。


