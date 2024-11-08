---
date: '2024-11-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8be6320...MicrosoftDocs:6e04dd6
summary: このドキュメントでは、いくつかのマイナーアップデートについて説明しています。主な内容は、新しいLlama-2モデルの追加、互換性の破壊を伴うLlama
  2 Chatモデルの削除、文書内の「マケドニア」の名称変更、Azure AIモデル推論サービスに関する文書の明確化です。これらの変更は、ドキュメントの正確性と情報の明確さを向上させ、ユーザーに対する選択肢を広げることを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8be6320...MicrosoftDocs:6e04dd6){target="_blank"}

# Highlights
以下の文章では、ドキュメントのいくつかのマイナーアップデートについて説明しています。新しい機能や重要な変更点に焦点を当てています。

## 新機能
- Llama-2シリーズのモデル「Llama-2-7B-chat」と「Llama-2-70B-chat」がAzure OpenAIサービスのファインチューニングモデルリストに追加されました。

## 互換性の破壊を伴う変更
- Llama 2 Chatモデル「Llama 2 7B Chat」と「Llama 2 70B Chat」がAzure AI Studioのリストから削除されました。

## その他の更新
- 文書中のマケドニアの名称が「マケドニア」から「北マケドニア」に変更されました。
- 「Azure AIモデル推論サービス」に関する文書のタイトルと説明が明確化されました。

# Insights
この記事では、ドキュメントの正確性、情報の明確さ、およびユーザーの選択肢の向上を目的としたいくつかのマイナーアップデートが行われました。

最初の変更は国名の更新に関するもので、「マケドニア」が「北マケドニア」に修正されました。これは特にドキュメントの国名リストを正確に保つために重要です。国際的な合意や政治的な背景に基づいた変更であり、ドキュメントの一貫性と信頼性を支持するものです。

次に、Azure AIモデル推論サービスについての文書のタイトルと内容が修正されました。この修正は、AIモデルの構成における重要な部分である推論エンドポイントについての理解を促進することを目的としています。特に、タイトルの変更が読者に明確な指針を提供するため、有用です。

三つ目の変更は、Llama-2シリーズの新モデルの追加です。この追加により、ユーザーはより多くの選択肢から最適なモデルを選び、ファインチューニングのプロセスで最大の成果を得ることができます。現代のデータ解析やAI開発において、モデルの多様性は重要です。

最後に、利用可能なLlama 2 Chatモデルのリストが修正され、モデルの多様性が明確になりました。この変更は、ユーザーがどのモデルが使用可能かを効率的に把握する手助けとなり、Azure AI Studioにおけるモデルの選択プロセスをシンプルにするものです。

これらの更新は、ドキュメントの一貫性、利用者に対する情報の明確性、選択肢の幅を広げることを目的とした、戦略的なマイナーアップデートです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [prebuilt.md](#item-ac5486) | minor update | マケドニアの国名の変更 | modified | 1 | 1 | 2 | 
| [create-model-deployments.md](#item-fd210d) | minor update | Azure AIモデル推論サービスに関するタイトルと説明の修正 | modified | 4 | 4 | 8 | 
| [fine-tuning-overview.md](#item-31b07b) | minor update | Llama-2モデルの追加 | modified | 1 | 1 | 2 | 
| [region-availability-maas.md](#item-35d79c) | minor update | Llama 2 Chatモデルのリストからの修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/language-support/prebuilt.md{#item-ac5486}

<details>
<summary>Diff</summary>
````diff
@@ -173,7 +173,7 @@ Azure AI Document Intelligence models provide multilingual document processing s
 | &bullet; Korean (`ko`) | Korea (`kr`)|
 | &bullet; Latvian (`lv`) | Latvia (`lv`)|
 | &bullet; Lithuanian (`lt`) | Lithuania (`lt`)|
-| &bullet; Macedonian (`mk`) | Macedonia (`mk`)|
+| &bullet; Macedonian (`mk`) | North Macedonia (`mk`)|
 | &bullet; Malay (`ms`) | Malaysia (`ms`)|
 | &bullet; Norwegian (`nb`) | Norway (`no`)|
 | &bullet; Polish (`pl`) | Poland (`pl`)|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マケドニアの国名の変更"
}
```

### Explanation
この変更は、文書におけるマケドニアの国名を「マケドニア」から「北マケドニア」に修正したものです。具体的には、マケドニアを指す表記がより正確な国名に更新され、国名リストの対応箇所が変更されました。この更新は文書の正確性を向上させるものであり、他の言語のサポート情報を表示する際に重要です。全体として、この修正は文書内の情報の一貫性を保つための小さな更新といえます。

## articles/ai-studio/ai-services/how-to/create-model-deployments.md{#item-fd210d}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Add and configure models to Azure AI services
+title: Add and configure models to Azure AI model inference service
 titleSuffix: Azure AI services
 description: Learn how to add and configure new models to the Azure AI model's inference endpoint in Azure AI services.
 ms.service: azure-ai-studio
@@ -12,9 +12,9 @@ ms.reviewer: fasantia
 recommendations: false
 ---
 
-# Add and configure models to Azure AI services
+# Add and configure models to Azure AI model inference service
 
-You can decide and configure which models are available for inference in the Azure AI services resource model's inference endpoint. When a given model is configured, you can then generate predictions from it by indicating its model name or deployment name on your requests. No further changes are required in your code to use it.
+You can decide and configure which models are available for inference in the resource's model inference endpoint. When a given model is configured, you can then generate predictions from it by indicating its model name or deployment name on your requests. No further changes are required in your code to use it.
 
 In this article, you learn how to add a new model to the Azure AI model inference service in Azure AI services.
 
@@ -62,4 +62,4 @@ When creating model deployments, you can configure other settings including cont
 
 ## Next steps
 
-* [Develop applications using Azure AI model inference service in Azure AI services](../concepts/endpoints.md)
\ No newline at end of file
+* [Develop applications using Azure AI model inference service in Azure AI services](../concepts/endpoints.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AIモデル推論サービスに関するタイトルと説明の修正"
}
```

### Explanation
この変更では、「Azure AIサービス」に関する文書のタイトルと説明が修正され、特に「モデルの推論サービス」に焦点を当てています。具体的には、タイトルが「Add and configure models to Azure AI services」から「Add and configure models to Azure AI model inference service」に変更され、内容もそれに合わせて調整されています。文書内の説明部分でも、推論エンドポイントに関連する表現がより明確にされ、読者がモデル構成の重要性を理解しやすくなっています。また、次のステップへのリンクも同様に更新されており、全体として情報の精度と明瞭さを向上させるための小規模な更新です。

## articles/ai-studio/concepts/fine-tuning-overview.md{#item-31b07b}

<details>
<summary>Diff</summary>
````diff
@@ -105,7 +105,7 @@ Now that you know when to use fine-tuning for your use case, you can go to Azure
 | --- | --- | --- |
 | [Azure OpenAI models](../../ai-services/openai/how-to/fine-tuning.md?context=/azure/ai-studio/context/context) | Azure OpenAI Service models that you can fine-tune include among others `gpt-4` and `gpt-4o-mini`.<br/><br/>For details about Azure OpenAI models that are available for fine-tuning, see the [Azure OpenAI Service models documentation](../../ai-services/openai/concepts/models.md#fine-tuning-models) or the [Azure OpenAI models table](#fine-tuning-azure-openai-models) later in this guide. | Azure OpenAI Service models that you can fine-tune include among others North Central US and Sweden Central.<br/><br/>The supported regions might vary if you use Azure OpenAI models in an AI Studio project versus outside a project.<br/><br/>For details about fine-tuning regions, see the [Azure OpenAI Service models documentation](../../ai-services/openai/concepts/models.md#fine-tuning-models). |
 | [Phi-3 family models](../how-to/fine-tune-phi-3.md) | `Phi-3-mini-4k-instruct`<br/>`Phi-3-mini-128k-instruct`<br/>`Phi-3-medium-4k-instruct`<br/>`Phi-3-medium-128k-instruct` | East US2 |
-| [Meta Llama 2 family models](../how-to/fine-tune-model-llama.md) | `Meta-Llama-2-70b`<br/>`Meta-Llama-2-7b`<br/>`Meta-Llama-2-13b` | West US3 |
+| [Meta Llama 2 family models](../how-to/fine-tune-model-llama.md) | `Meta-Llama-2-70b`<br/>`Meta-Llama-2-7b`<br/>`Meta-Llama-2-13b` <br/> `Llama-2-7B-chat` <br> `Llama-2-70B-chat` | West US3 |
 | [Meta Llama 3.1 family models](../how-to/fine-tune-model-llama.md) | `Meta-Llama-3.1-70b-Instruct`<br/>`Meta-Llama-3.1-8b-Instruct` | West US3 |
 
 This table provides more details about the Azure OpenAI Service models that support fine-tuning and the regions where fine-tuning is available.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Llama-2モデルの追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスのファインチューニングに関する文書内のモデルリストにおいて、「Llama-2」シリーズのモデルを追加するものです。具体的には、Meta Llama 2ファミリーのモデルに「Llama-2-7B-chat」と「Llama-2-70B-chat」の2つのモデルが加わっています。この更新により、利用可能なモデルのバリエーションが増え、ユーザーがファインチューニングを行う際の選択肢が広がります。また、この修正は、ファインチューニング機能の活用に関する理解を促進し、Azure AI Studioでのモデル管理に役立つ情報を提供することを目的としています。全体的に、この変更は文書の情報を最新のものにするための小規模な更新です。

## articles/ai-studio/includes/region-availability-maas.md{#item-35d79c}

<details>
<summary>Diff</summary>
````diff
@@ -36,7 +36,7 @@ JAIS 30B Chat   |   [Microsoft Managed Countries](/partner-center/marketplace/ta
 |Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
 Llama 2 7B <br> Llama 2 13B <br> Llama 2 70B     |   [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)     | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3    | West US 3       |
-Llama 2 7B Chat <br> Llama 2 7B Chat <br> Llama 2 70B Chat    | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3   | West US 3   |
+Llama 2 7B Chat <br> Llama 2 70B Chat    | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3   | West US 3   |
 Llama 3 8B Instruct  <br> Llama 3 70B Instruct  | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available   |
 Llama 3.1 8B Instruct <br> Llama 3.1 70B Instruct | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3     | West US 3  |
 Llama 3.1 405B Instruct  | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3     | Not available  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Llama 2 Chatモデルのリストからの修正"
}
```

### Explanation
この変更は、Azure AI StudioにおけるLlama 2 Chatモデルのリストから、利用可能なモデル構成を修正するものです。具体的には、「Llama 2 7B Chat」と「Llama 2 70B Chat」の2つのモデルがリストから削除されました。この更新により、モデルのバリエーションがより明確になり、ユーザーがどのモデルが利用可能であるかを理解しやすくなっています。さらに、Microsoft管理国などの参照リンクは引き続き提供され、ユーザーが導入先やファインチューニングのオプションに関する情報を得る助けとなります。この変更は、リソースの情報を最新の状態に保つための小規模な更新です。


