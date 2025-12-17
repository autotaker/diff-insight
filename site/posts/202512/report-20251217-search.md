---
date: '2025-12-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b290bf6...MicrosoftDocs:a67f1c9
summary: この更新では、Azureポータルに関連するイメージ検索やベクトルのインポート、プライベートインデクサーに関するドキュメントが微調整され、主に新しいモデル情報や日付の更新、特定のセクションの強調とリンクの追加が行われました。これにより、ユーザーは最新の情報を持って快適に機能を活用できるよう支援されています。特に「Microsoft
  Foundry resource」としての新しいモデル情報が追加され、プライベートインデクサー関連のドキュメントにも重要な注釈が加えられました。今回の更新は、Azureのサービス利用を促進し、ユーザーの生産性向上に寄与することが期待されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b290bf6...MicrosoftDocs:a67f1c9){target="_blank"}

# ハイライト
この更新では、Azureポータルに関連するイメージ検索、ベクトルのインポート、およびプライベートインデクサーに関するドキュメントが微調整され、ユーザーに新しい情報とサポートを提供しています。主に日付の更新とモデル情報の追加、特定のセクションの強調とリンクの追加が行われ、ユーザーの利便性と効果的な機能利用を支援する内容となっています。

## 新機能
- 「Microsoft Foundry resource」としての新しいモデル情報がイメージ検索とベクトルのインポートのドキュメントに追加されました。
- プライベートインデクサーに関するドキュメントでは、共有プライベートリンクとリソース制限への新たな注記が追加されました。

## 破壊的変更
- これらの更新には破壊的な変更は含まれていませんが、ドキュメントの日付と情報の正確性に基づく更新によって、既存ユーザーの認識が必要となる可能性があります。

## その他の更新
- ドキュメントの日付が更新され、最新の情報を反映しています。
- 各ドキュメントに注釈やリンクが追加され、より詳細な情報が提供されています。

# 洞察
今回のドキュメント更新は、Azureのサービス利用を促進し、ユーザーがAzureポータルでの各種機能を最大限に活用できるようにするための取り組みの一環です。特に、モデル提供者や利用可能な機能に関する情報の追加は、ユーザーが自身のニーズに適したリソースを迅速に見つけ、利用開始できるよう促進します。イメージ検索やベクトルインポートでの「Microsoft Foundry resource」の追加は、Azure Visionが提供する高度なマルチモーダル機能の活用を想起させるもので、これによりユーザーはより豊富なデータを取り扱うことが可能となります。また、プライベートインデクサーのドキュメントアップデートは、セキュリティやリソースアクセスの観点からの注意事項や対策を明確に提示し、高度なデータ管理環境をサポートしています。これにより、Azureユーザーの生産性向上に大きく寄与することが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | ポータルイメージ検索のガイドの更新 | modified | 8 | 8 | 16 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | ベクトルのインポートに関するドキュメントの更新 | modified | 8 | 8 | 16 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | プライベートインデクサーへのアクセスに関するドキュメントの更新 | modified | 3 | 1 | 4 | 


# Modified Contents
## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 10/24/2025
+ms.date: 12/16/2025
 ms.custom:
   - references_regions
 ---
@@ -56,20 +56,20 @@ The portal supports the following models for each method. Deployment instruction
 
 | Provider | Models for image verbalization | Models for multimodal embeddings |
 |--|--|--|
-| [Azure OpenAI resource](/azure/ai-foundry/openai/how-to/create-resource?view=foundry-classic&pivots=web-portal&preserve-view=true) <sup>1, 2</sup> | LLMs:<br>gpt-4o<br>gpt-4o-mini<br>gpt-5<br>gpt-5-mini<br>gpt-5-nano<br><br>Embedding models:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large | |
-| [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects?view=foundry-classic&pivots=web-portal&preserve-view=true) | LLMs:<br>phi-4<br>gpt-4o<br>gpt-4o-mini<br>gpt-5<br>gpt-5-mini<br>gpt-5-nano<br><br>Embedding models:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large | |
+| [Microsoft Foundry resource](/azure/ai-services/multi-service-resource) <sup>1</sup> | Embedding model: [Azure Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) <sup>2</sup> | [Azure Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) <sup>2</sup> |
 | [Microsoft Foundry hub-based project](/azure/ai-foundry/how-to/hub-create-projects?view=foundry-classic&pivots=web-portal&preserve-view=true) | LLMs:<br>phi-4<br>gpt-4o<br>gpt-4o-mini<br>gpt-5<br>gpt-5-mini<br>gpt-5-nano<br><br>Embedding models:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large<br>Cohere-embed-v3-english <sup>3</sup><br>Cohere-embed-v3-multilingual <sup>3</sup> | Cohere-embed-v3-english <sup>3</sup><br>Cohere-embed-v3-multilingual <sup>3</sup> |
-| [Microsoft Foundry resource](/azure/ai-services/multi-service-resource) <sup>4</sup> | Embedding model: [Azure Vision in Foundry Tools multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) <sup>5</sup> | [Azure Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) <sup>5</sup> |
+| [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects?view=foundry-classic&pivots=web-portal&preserve-view=true) | LLMs:<br>phi-4<br>gpt-4o<br>gpt-4o-mini<br>gpt-5<br>gpt-5-mini<br>gpt-5-nano<br><br>Embedding models:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large | |
+| [Azure OpenAI resource](/azure/ai-foundry/openai/how-to/create-resource?view=foundry-classic&pivots=web-portal&preserve-view=true) <sup>4, 5</sup> | LLMs:<br>gpt-4o<br>gpt-4o-mini<br>gpt-5<br>gpt-5-mini<br>gpt-5-nano<br><br>Embedding models:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large | |
 
-<sup>1</sup> The endpoint of your Azure OpenAI resource must have a [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains), such as `https://my-unique-name.openai.azure.com`. If you created your resource in the [Azure portal](https://portal.azure.com/), this subdomain was automatically generated during resource setup.
+<sup>1</sup> For billing purposes, you must [attach your Foundry resource](cognitive-search-attach-cognitive-services.md) to the skillset in your Azure AI Search service. Unless you use a [keyless connection (preview)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) to create the skillset, both resources must be in the same region.
 
-<sup>2</sup> Azure OpenAI resources (with access to embedding models) that were created in the [Foundry portal](https://ai.azure.com/?cid=learnDocs) aren't supported. You must create an Azure OpenAI resource in the Azure portal.
+<sup>2</sup> The Azure Vision multimodal embeddings APIs are available in [select regions](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
 
 <sup>3</sup> To use this model in the wizard, you must provision it as a serverless API deployment. You can use an [ARM/Bicep template](https://github.com/Azure-Samples/azure-ai-search-multimodal-sample/blob/42b4d07f2dd9f7720fdc0b0788bf107bdac5eecb/infra/ai/modules/project.bicep#L37C1-L38C1) for this task.
 
-<sup>4</sup> For billing purposes, you must [attach your Foundry resource](cognitive-search-attach-cognitive-services.md) to the skillset in your Azure AI Search service. Unless you use a [keyless connection (preview)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) to create the skillset, both resources must be in the same region.
+<sup>4</sup> The endpoint of your Azure OpenAI resource must have a [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains), such as `https://my-unique-name.openai.azure.com`. If you created your resource in the [Azure portal](https://portal.azure.com/), this subdomain was automatically generated during resource setup.
 
-<sup>5</sup> The Azure Vision multimodal embeddings APIs are available in [select regions](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
+<sup>5</sup> Azure OpenAI resources (with access to embedding models) that were created in the [Foundry portal](https://ai.azure.com/?cid=learnDocs) aren't supported. You must create an Azure OpenAI resource in the Azure portal.
 
 ### Public endpoint requirements
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータルイメージ検索のガイドの更新"
}
```

### Explanation
この変更は、Azureポータルでのイメージ検索機能に関するドキュメントを更新したものです。具体的には、以下の点が修正されました：

1. ドキュメントの日付が 2025年10月24日から2025年12月16日に変更されました。この変更は、情報の更新を反映するために必要です。
   
2. 「モデル」セクションでは、モデル提供者に関する情報が更新され、特に「Microsoft Foundry resource」のエントリが調整されました。具体的には、モデルのリンクと説明が追加され、Azure Visionに関連するマルチモーダル機能が強調されています。この変更により、ユーザーはより適切に使用できるリソースへのアクセスができるようになります。

3. また、いくつかの注釈も更新され、特に地域に関する情報が最新の内容に修正されています。これにより、ユーザーがそれぞれのモデルやリソースを利用する際の条件と利便性が向上しています。

この更新は、ユーザーがAzureのイメージ検索機能をより効果的に利用できるようにするための重要なステップです。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: quickstart
-ms.date: 10/24/2025
+ms.date: 12/16/2025
 ---
 
 # Quickstart: Vectorize text in the Azure portal
@@ -46,20 +46,20 @@ The portal supports the following embedding models for integrated vectorization.
 
 | Provider | Supported models |
 |--|--|
-| [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource) <sup>1, 2</sup> | For text:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large |
-| [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) | For text:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large |
+| [Microsoft Foundry resource](/azure/ai-services/multi-service-resource) <sup>1</sup> | For text and images: [Azure Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) <sup>2</sup> |
 | [Microsoft Foundry hub-based project](/azure/ai-foundry/how-to/hub-create-projects) | For text:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large<br><br>For text and images:<br>Cohere-embed-v3-english <sup>3</sup><br>Cohere-embed-v3-multilingual <sup>3</sup> |
-| [Microsoft Foundry resource](/azure/ai-services/multi-service-resource) <sup>4</sup> | For text and images: [Azure Vision in Foundry Tools multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) <sup>5</sup></li> |
+| [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) | For text:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large |
+| [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource) <sup>4, 5</sup> | For text:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large |
 
-<sup>1</sup> The endpoint of your Azure OpenAI resource must have a [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains), such as `https://my-unique-name.openai.azure.com`. If you created your resource in the [Azure portal](https://portal.azure.com/), this subdomain was automatically generated during resource setup.
+<sup>1</sup> For billing purposes, you must [attach your Foundry resource](cognitive-search-attach-cognitive-services.md) to the skillset in your Azure AI Search service. Unless you use a [keyless connection (preview)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) to create the skillset, both resources must be in the same region.
 
-<sup>2</sup> Azure OpenAI resources (with access to embedding models) that were created in the [Foundry portal](https://ai.azure.com/?cid=learnDocs) aren't supported. You must create an Azure OpenAI resource in the Azure portal.
+<sup>2</sup> The Azure Vision multimodal embeddings APIs are available in [select regions](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
 
 <sup>3</sup> To use this model in the wizard, you must provision it as a serverless API deployment. You can use an [ARM/Bicep template](https://github.com/Azure-Samples/azure-ai-search-multimodal-sample/blob/42b4d07f2dd9f7720fdc0b0788bf107bdac5eecb/infra/ai/modules/project.bicep#L37C1-L38C1) for this task.
 
-<sup>4</sup> For billing purposes, you must [attach your Foundry resource](cognitive-search-attach-cognitive-services.md) to the skillset in your Azure AI Search service. Unless you use a [keyless connection (preview)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) to create the skillset, both resources must be in the same region.
+<sup>4</sup> The endpoint of your Azure OpenAI resource must have a [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains), such as `https://my-unique-name.openai.azure.com`. If you created your resource in the [Azure portal](https://portal.azure.com/), this subdomain was automatically generated during resource setup.
 
-<sup>5</sup> The Azure Vision multimodal embeddings APIs are available in [select regions](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
+<sup>5</sup> Azure OpenAI resources (with access to embedding models) that were created in the [Foundry portal](https://ai.azure.com/?cid=learnDocs) aren't supported. You must create an Azure OpenAI resource in the Azure portal.
 
 ### Public endpoint requirements
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルのインポートに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azureポータルにおけるベクトルのインポートに関するクイックスタートガイドの内容を更新したものです。主な変更点は以下の通りです：

1. ドキュメントの日付が2025年10月24日から2025年12月16日に更新されました。この調整は、情報の正確性を保つために行われました。

2. サポートされているモデルのセクションでは、特定のモデルに関する表記が更新されました。特に「Microsoft Foundry resource」が新たに追加され、テキストと画像の両方に対応する「Azure Vision multimodal」が紹介されています。また、エンベディングモデルに関連するリンクや説明も調整され、ユーザーにとっての利便性が向上しています。

3. 注釈の内容も見直され、請求やリソースの設定に関する最新の情報が提供されています。これにより、ユーザーは正しい手順に従い、効率的にリソースを利用できるようになります。

これらの変更により、Azureのベクトル化機能を使用するユーザーは、より良い体験を得ることができます。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: mrcarter8
 ms.author: mcarter
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 09/26/2025
+ms.date: 12/15/2025
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
@@ -71,6 +71,8 @@ When evaluating shared private links for your scenario, remember these constrain
 
 + Review shared private link [resource limits for each tier](search-limits-quotas-capacity.md#shared-private-link-resource-limits).
 
++ The resource type `Microsoft.CognitiveServices/accounts` for kind `AIServices` isn't currently supported.  This means that shared private link for Foundry resources with this kind can't be created at this time. If you require to use an Azure OpenAI embedding model for your skill or vectorizer, and need private communication, create an Azure OpenAI resource and a shared private link with the `Microsoft.CognitiveServices/accounts` with subtype `openai_account` as a workaround.
+
 ## Prerequisites
 
 + [A supported Azure resource](#supported-resource-types), configured to run in a virtual network.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートインデクサーへのアクセスに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azureのプライベートインデクサーへのアクセス方法についてのドキュメントを最新の情報に基づいて更新したものです。主な変更点は以下の通りです：

1. ドキュメントの日付が2025年9月26日から2025年12月15日に変更され、情報の正確性を確保しています。

2. 共有プライベートリンクに関する記載が追加されました。具体的には、「リソース制限」のセクションが強調され、各ティア向けの共有プライベートリンクのリソース制限についてのリンクが提供されています。

3. 新たな注記が追加され、`Microsoft.CognitiveServices/accounts`のリソースタイプが現在サポートされていないことが明記されています。特に、Foundryリソースのこのタイプの共有プライベートリンクが作成できない旨と、Azure OpenAIエンベディングモデルを使用する場合のワークアラウンドとしての手順が示されています。

4. 文書に「Prerequisites（前提条件）」セクションが追加され、サポートされているAzureリソースについてのリンクが含まれています。

これらのアップデートにより、プライベートインデクサーの使用に関する情報がより明確かつ詳細になり、ユーザーが必要な手順を理解しやすくなっています。


