---
date: '2024-11-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b16ebe2...MicrosoftDocs:7c64df0
summary: |-
  このレポートは、Azure AI Studioにおけるいくつかの重要な変更点についてまとめています。主なハイライトとして、AI Studioのモデル蒸留機能が「プレビュー版」であることが明示され、ファインチューニングの情報が整理されリンクも追加されています。また、セキュアデータプレイグラウンドに関する役割の情報も更新され、明確にされています。

  新機能としては、蒸留機能がノートブック体験での使用可能性が追加され、セキュアデータプレイグラウンドに「Cognitive Services Contributor」といった新しい役割も導入されました。大きな破壊的変更はありません。

  他の更新として、ファインチューニング情報の再編成により説明が明瞭になり、セキュアデータプレイグラウンドのBlobストレージ利用にネットワーク制限の対応も行われています。

  この変更は、ユーザーがAzure AI Studioの機能をより理解し、プロジェクトに活用しやすくすることを目的としています。特に、モデル蒸留機能の状況を透明にすることで、ユーザーは現状の機能を踏まえた使い方ができるようになります。全体として、データセキュリティやアクセス管理の向上を目指しており、安全で効率的なデータ操作が促進されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b16ebe2...MicrosoftDocs:7c64df0){target="_blank"}

# Highlights
- AI Studioのモデル蒸留機能が「プレビュー版」であることの明示
- ファインチューニングの概要におけるリンク追加や情報整理
- セキュアデータプレイグラウンドでの役割に関する情報の明確化と更新

## New features
- 蒸留機能がノートブック体験で使用可能という具体的な情報の追加
- 新しい役割として「Cognitive Services Contributor」などがセキュアデータプレイグラウンドに追加

## Breaking changes
- 大きな破壊的変更はありません。

## Other updates
- ファインチューニングの情報再編成により、より理論的で明瞭な説明が提供
- セキュアデータプレイグラウンドのBlobストレージ利用におけるネットワーク制限環境への対応

# Insights
このコードの変更は、Azure AI Studioの各ドキュメントにおいて情報の明確性を大いに向上させ、それぞれの機能や利便性をユーザーがより理解しやすくすることを目的としています。

特に、モデル蒸留機能の「プレビュー版」を明示することで、ユーザーは現段階での機能の制限や今後のバージョンアップを視野に入れた利用ができるようになっています。この透明性は、ユーザーが自らのプロジェクトにおいてどの程度までAI Studioの機能を活用できるかを判断する助けとなります。

ファインチューニングについては、「Azure AI Studio」へのリンク追加および説明の明確化により、ユーザーがすぐに必要とする情報へアクセスしやすくなっています。これにより、どのモデルが最適であり、必要なデータがどの程度かを明確に理解する助けとなります。

さらに、セキュアデータプレイグラウンドでは、役割とそのアクセス権についての明確な説明が施され、特に新しい役割が追加されています。これにより、Azure AIサービスやOpenAIリソースの利用において、ユーザーは各役割の目的を正確に理解した上で、適切な役割を割り当てることが可能となります。これらの変更は、データセキュリティやアクセス管理の向上を目的とし、より安全で効率的なデータ操作を支援しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [concept-model-distillation.md](#item-5d97fa) | minor update | AI Studioにおける蒸留機能のプレビュー版 | modified | 6 | 3 | 9 | 
| [fine-tuning-overview.md](#item-31b07b) | minor update | ファインチューニングの概要の更新 | modified | 17 | 53 | 70 | 
| [secure-data-playground.md](#item-b7fa5e) | minor update | セキュアデータプレイグラウンドの更新 | modified | 5 | 3 | 8 | 


# Modified Contents
## articles/ai-studio/concepts/concept-model-distillation.md{#item-5d97fa}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Distillation in AI Studio
+title: Distillation in AI Studio (preview)
 titleSuffix: Azure AI Studio
 description: Learn how to do distillation in Azure AI Studio.
 manager: scottpolly
@@ -13,7 +13,9 @@ author: ssalgadodev
 ms.custom: references_regions
 ---
 
-# Distillation in Azure AI Studio
+# Distillation in Azure AI Studio (preview)
+
+[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
 
 In Azure AI Studio, you can use distillation to efficiently train a student model.
 
@@ -31,7 +33,8 @@ The main steps in knowledge distillation are:
 
 ## Sample notebook
 
-You can use the [sample notebook](https://github.com/Azure/azureml-examples/tree/main/sdk/python/foundation-models/system/distillation) to see how to perform distillation. In this sample notebook, the teacher model uses the Meta Llama 3.1 405B instruction model, and the student model uses the Meta Llama 3.1 8B instruction model.
+Distillation in AI Studio is currently only available through a notebook experience. You can use the [sample notebook](https://github.com/Azure/azureml-examples/tree/main/sdk/python/foundation-models/system/distillation) to see how to perform distillation. Model distillation is available for Microsoft models and a selection of OSS (open-source software) models available in the model catalog. In this sample notebook, the teacher model uses the Meta Llama 3.1 405B instruction model, and the student model uses the Meta Llama 3.1 8B instruction model.
+
 
 
 We used an advanced prompt during synthetic data generation. The advanced prompt incorporates chain-of-thought (CoT) reasoning, which results in higher-accuracy data labels in the synthetic data. This labeling further improves the accuracy of the distilled model.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Studioにおける蒸留機能のプレビュー版"
}
```

### Explanation
このコードの変更は、Azure AI Studioにおけるモデル蒸留のドキュメントに関するもので、いくつかの内容が更新されています。主な変更点は、タイトルの後に「(preview)」という注記が追加され、蒸留機能が現在プレビュー版であることが明示されています。また、モデル蒸留がノートブック体験を通じてのみ利用可能であり、Microsoftのモデル及び一部のオープンソースモデルがモデルカタログから利用可能であることが追加されています。さらに、合成データ生成の際に先進的なプロンプトを使用し、その理由付けが織り込まれたことで、合成データのラベルの精度が向上し、蒸留されたモデルの精度が向上したことについても説明されています。これらの変更により、読者に対する情報がさらに明確で役立つものになっています。

## articles/ai-studio/concepts/fine-tuning-overview.md{#item-31b07b}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-studio
 ms.custom:
   - build-2024
 ms.topic: conceptual
-ms.date: 5/29/2024
+ms.date: 10/31/2024
 ms.reviewer: sgilley
 ms.author: sgilley
 author: sdgilley
@@ -19,9 +19,9 @@ author: sdgilley
 
 Fine-tuning retrains an existing large language model (LLM) by using example data. The result is a new, custom LLM that's optimized for the provided examples.
 
-This article can help you decide whether or not fine-tuning is the right solution for your use case. This article also describes how Azure AI Studio can support your fine-tuning needs.
+This article can help you decide whether or not fine-tuning is the right solution for your use case. This article also describes how [Azure AI Studio](https://ai.azure.com) can support your fine-tuning needs.
 
-In this article, fine-tuning refers to *supervised fine-tuning*, not continuous pretraining or reinforcement learning through human feedback (RLHF). Supervised fine-tuning is the process of retraining pretrained models on specific datasets. The purpose is typically to improve model performance on specific tasks or to introduce information that wasn't well represented when you originally trained the base model.
+In this article, fine-tuning refers to *supervised fine-tuning*, not to continuous pretraining or reinforcement learning through human feedback (RLHF). Supervised fine-tuning is the process of retraining pretrained models on specific datasets. The purpose is typically to improve model performance on specific tasks or to introduce information that wasn't well represented when you originally trained the base model.
 
 ## Getting starting with fine-tuning
 
@@ -48,9 +48,7 @@ You might not be ready for fine-tuning if:
 - You can't find the right data to serve the model.
 - You don't have a clear use case for fine-tuning, or you can't articulate more than "I want to make a model better."
 
-If you identify cost as your primary motivator, proceed with caution. Fine-tuning might reduce costs for certain use cases by shortening prompts or allowing you to use a smaller model. But there's a higher upfront cost to training, and you have to pay for hosting your own custom model. For more information on fine-tuning costs in Azure OpenAI Service, refer to the [pricing page](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/).
-
-If you want to add out-of-domain knowledge to the model, you should start with RAG by using features like Azure OpenAI [On Your Data](../../ai-services/openai/concepts/use-your-data.md) or [embeddings](../../ai-services/openai/tutorials/embeddings.md). Using RAG in this way is often a cheaper, more adaptable, and potentially more effective option, depending on the use case and data.
+If you identify cost as your primary motivator, proceed with caution. Fine-tuning might reduce costs for certain use cases by shortening prompts or allowing you to use a smaller model. But typically there's a higher upfront cost to training, and you have to pay for hosting your own custom model. 
 
 ### What isn't working with alternate approaches?
 
@@ -82,7 +80,7 @@ You might not be ready for fine-tuning if:
 
 Even with a great use case, fine-tuning is only as good as the quality of the data that you can provide. You need to be willing to invest the time and effort to make fine-tuning work. Different models require different data volumes, but you often need to be able to provide fairly large quantities of high-quality curated data.
 
-Another important point is that even with high-quality data, if your data isn't in the necessary format for fine-tuning, you'll need to commit engineering resources for the formatting. For more information on how to prepare your data for fine-tuning, refer to the [fine-tuning documentation](../../ai-services/openai/how-to/fine-tuning.md?context=/azure/ai-studio/context/context).
+Another important point is that even with high-quality data, if your data isn't in the necessary format for fine-tuning, you need to commit engineering resources for the formatting. 
 
 You might be ready for fine-tuning if:
 
@@ -92,63 +90,29 @@ You might be ready for fine-tuning if:
 
 You might not be ready for fine-tuning if:
 
-- You haven't identified a dataset yet.
+- An appropriate dataset hasn't been identified.
 - The dataset format doesn't match the model that you want to fine-tune.
 
-### How will you measure the quality of your fine-tuned model?
+### How can you measure the quality of your fine-tuned model?
 
 There isn't a single right answer to this question, but you should have clearly defined goals for what success with fine-tuning looks like. Ideally, this effort shouldn't just be qualitative. It should include quantitative measures of success, like using a holdout set of data for validation, in addition to user acceptance testing or A/B testing the fine-tuned model against a base model.
 
 ## Supported models for fine-tuning in Azure AI Studio
 
-Now that you know when to use fine-tuning for your use case, you can go to Azure AI Studio to find models available to fine-tune. The following sections describe the available models.
-
-### Azure OpenAI models
-
-The following Azure OpenAI models are supported in Azure AI Studio for fine-tuning:
-
-|  Model ID  | Fine-tuning regions | Max request (tokens) | Training data (up to) |
-|  --- | --- | :---: | :---: |
-| `babbage-002` | North Central US <br> Sweden Central  <br> Switzerland West | 16,384 | Sep 2021 |
-| `davinci-002` | North Central US <br> Sweden Central  <br> Switzerland West | 16,384 | Sep 2021 |
-| `gpt-35-turbo` (0613) | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | 4,096 | Sep 2021 |
-| `gpt-35-turbo` (1106) | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | Input: 16,385<br> Output: 4,096 |  Sep 2021|
-| `gpt-35-turbo` (0125)  | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | 16,385 | Sep 2021 |
-| `gpt-4` (0613) <sup>1<sup> | North Central US <br> Sweden Central | 8192 | Sep 2021 |
-
-<sup>1</sup> GPT-4 fine-tuning is currently in public preview. For more information, see the [GPT-4 fine-tuning safety evaluation guidance](/azure/ai-services/openai/how-to/fine-tuning?tabs=turbo%2Cpython-new&pivots=programming-language-python#safety-evaluation-gpt-4-fine-tuning---public-preview).
-
-To fine-tune Azure OpenAI models, you must add a connection to an Azure OpenAI resource with a supported region to your project.
-
-### Phi-3 family models
-
-The following Phi-3 family models are supported in Azure AI Studio for fine-tuning:
-
-- `Phi-3-mini-4k-instruct`
-- `Phi-3-mini-128k-instruct`
-- `Phi-3-medium-4k-instruct`
-- `Phi-3-medium-128k-instruct`
-
-Fine-tuning of Phi-3 models is currently supported in projects located in East US2.
-
-### Meta Llama 2 family models
-
-The following Llama 2 family models are supported in Azure AI Studio for fine-tuning:
-
-- `Meta-Llama-2-70b`
-- `Meta-Llama-2-7b`
-- `Meta-Llama-2-13b`
-
-Fine-tuning of Llama 2 models is currently supported in projects located in West US3.
+Now that you know when to use fine-tuning for your use case, you can go to Azure AI Studio to find models available to fine-tune. The following table describes models that you can fine-tune in Azure AI Studio, along with the regions where you can fine-tune them.
 
-### Meta Llama 3.1 family models
+| Model family | Model ID | Fine-tuning regions |
+| --- | --- | --- |
+| [Azure OpenAI models](../../ai-services/openai/how-to/fine-tuning.md?context=/azure/ai-studio/context/context) | Azure OpenAI Service models that you can fine-tune include among others `gpt-4` and `gpt-4o-mini`.<br/><br/>For details about Azure OpenAI models that are available for fine-tuning, see the [Azure OpenAI Service models documentation](../../ai-services/openai/concepts/models.md#fine-tuning-models) or the [Azure OpenAI models table](#fine-tuning-azure-openai-models) later in this guide. | Azure OpenAI Service models that you can fine-tune include among others North Central US and Sweden Central.<br/><br/>The supported regions might vary if you use Azure OpenAI models in an AI Studio project versus outside a project.<br/><br/>For details about fine-tuning regions, see the [Azure OpenAI Service models documentation](../../ai-services/openai/concepts/models.md#fine-tuning-models). |
+| [Phi-3 family models](../how-to/fine-tune-phi-3.md) | `Phi-3-mini-4k-instruct`<br/>`Phi-3-mini-128k-instruct`<br/>`Phi-3-medium-4k-instruct`<br/>`Phi-3-medium-128k-instruct` | East US2 |
+| [Meta Llama 2 family models](../how-to/fine-tune-model-llama.md) | `Meta-Llama-2-70b`<br/>`Meta-Llama-2-7b`<br/>`Meta-Llama-2-13b` | West US3 |
+| [Meta Llama 3.1 family models](../how-to/fine-tune-model-llama.md) | `Meta-Llama-3.1-70b-Instruct`<br/>`Meta-Llama-3.1-8b-Instruct` | West US3 |
 
-The following Llama 3.1 family models are supported in Azure AI Studio for fine-tuning:
+This table provides more details about the Azure OpenAI Service models that support fine-tuning and the regions where fine-tuning is available.
 
-- `Meta-Llama-3.1-70b-Instruct`
-- `Meta-Llama-3.1-8b-Instruct`
+### Fine-tuning Azure OpenAI models
 
-Fine-tuning of Llama 3.1 models is currently supported in projects located in West US3.
+[!INCLUDE [Fine-tune models](../../ai-services/openai/includes/fine-tune-models.md)]
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングの概要の更新"
}
```

### Explanation
このコードの変更は、Azure AI Studioにおけるファインチューニングの概要を扱ったドキュメントにおける更新です。主な内容としては、日付の更新、リンクの追加、文章の明確化、そして情報の再構成が行われています。特に、ファインチューニングの説明において「Azure AI Studio」へのリンクが追加され、読者がよりアクセスしやすくなっています。

また、ファインチューニングの候補に関する説明や、対象となるモデルのリストが整理され、どのモデルがファインチューニングに適しているのかが明瞭に示されています。さらに、ファインチューニングのコストや準備すべきデータについての注意点が簡潔に提示され、業務における議論をサポートする内容となっています。

全体として、情報の整理と無駄の削減が行われ、読者にとってより理解しやすい構成となっています。これにより、ファインチューニングに関する正確な知識を提供し、効果的な活用を促進することを目的としています。

## articles/ai-studio/how-to/secure-data-playground.md{#item-b7fa5e}

<details>
<summary>Diff</summary>
````diff
@@ -186,10 +186,12 @@ For more information on assigning roles, see [Tutorial: Grant a user access to r
 | Azure AI Search | Search Index Data Contributor | Azure AI services/OpenAI | Read-write access to content in indexes. Import, refresh, or query the documents collection of an index. Only used for ingestion and inference scenarios. |
 | Azure AI Search | Search Index Data Reader | Azure AI services/OpenAI | Inference service queries the data from the index. Only used for inference scenarios. |
 | Azure AI Search | Search Service Contributor | Azure AI services/OpenAI | Read-write access to object definitions (indexes, aliases, synonym maps, indexers, data sources, and skillsets). Inference service queries the index schema for auto fields mapping. Data ingestion service creates index, data sources, skill set, indexer, and queries the indexer status. |
-| Azure AI services/OpenAI | Cognitive Services OpenAI Contributor | Azure AI Search | Custom skill |
-| Azure OpenAI Resource for chat model | Cognitive Services OpenAI User | Azure OpenAI resource for embedding model | Required only if using two Azure OpenAI resources to communicate. |
+| Azure AI services/OpenAI | Cognitive Services Contributor | Azure AI Search | Allow Search to create, read, and update AI Services resource. |
+| Azure AI services/OpenAI | Cognitive Services OpenAI Contributor | Azure AI Search | Allow Search the ability to fine-tune, deploy and generate text |
 | Azure Storage Account | Storage Blob Data Contributor | Azure AI Search | Reads blob and writes knowledge store. |
 | Azure Storage Account | Storage Blob Data Contributor | Azure AI services/OpenAI | Reads from the input container, and writes the preprocess result to the output container. |
+| Azure Blob Storage private endpoint | Reader | Azure AI Studio project | For your Azure AI Studio project with managed network enabled to access Blob storage in a network restricted environment |
+| Azure OpenAI Resource for chat model | Cognitive Services OpenAI User | Azure OpenAI resource for embedding model | [Optional] Required only if using two Azure OpenAI resources to communicate. |
 
 > [!NOTE]
 > The Cognitive Services OpenAI User role is only required if you are using two Azure OpenAI resources: one for your chat model and one for your embedding model. If this applies, enable Trusted Services AND ensure the Connection for your embedding model Azure OpenAI resource has EntraID enabled.  
@@ -205,7 +207,7 @@ For more information on assigning roles, see [Tutorial: Grant a user access to r
 | Azure AI Search | Search Services Contributor | Developer's Microsoft Entra ID | List API-Keys to list indexes from Azure OpenAI Studio. |
 | Azure AI Search | Search Index Data Contributor | Developer's Microsoft Entra ID | Required for the indexing scenario. |
 | Azure AI services/OpenAI | Cognitive Services OpenAI Contributor | Developer's Microsoft Entra ID | Call public ingestion API from Azure OpenAI Studio. |
-| Azure AI services/OpenAI | Cognitive Services User | Developer's Microsoft Entra ID | List API-Keys from Azure OpenAI Studio. |
+| Azure AI services/OpenAI | Cognitive Services Contributor | Developer's Microsoft Entra ID | List API-Keys from Azure OpenAI Studio. |
 | Azure AI services/OpenAI | Contributor | Developer's Microsoft Entra ID | Allows for calls to the control plane. |
 | Azure Storage Account | Contributor | Developer's Microsoft Entra ID | List Account SAS to upload files from Azure OpenAI Studio. |
 | Azure Storage Account | Storage Blob Data Contributor | Developer's Microsoft Entra ID | Needed for developers to read and write to blob storage. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セキュアデータプレイグラウンドの更新"
}
```

### Explanation
このコードの変更は、Azure AI Studioにおけるセキュアデータプレイグラウンドのドキュメントに関するもので、役割の割り当てに関する情報がいくつか更新されています。主な変更点としては、Azure AIサービスやOpenAIリソースの役割名とその説明が明確に整理されており、特に新しい役割の追加や不要な行の削除が行われています。

具体的には、「Cognitive Services Contributor」や「Cognitive Services OpenAI Contributor」といった役割が追加され、これらにより検索サービスがAIサービスリソースに対する操作を行うことができるようになったことが記述されています。また、Blobストレージへのアクセスに関する情報も更新されており、ネットワーク制限環境でのBlobストレージの利用について新たなエンドポイントが指定されています。

これにより、読者は各役割の機能や目的をより理解しやすくなり、具体的な使用シナリオに応じた適切な役割を選択できるようになります。この変更は、セキュリティやアクセス管理に関連する情報の明確性を向上させ、利用者が必要な設定を確実に行えることを目的としています。


