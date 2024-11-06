---
date: '2024-11-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c2df9dc...MicrosoftDocs:6c09135
summary: このコードの変更では、複数のドキュメントや画像が主に更新されました。C# SDKのクイックスタートガイドに手順の変更があり、Azure AI Languageの新機能やリリース情報、データプライバシーに関するアップデートが含まれています。また、LlamaIndex設定手順とAzure
  AI Studioでのハブ作成手順が改善され、関連する画像ファイルも最新のものに更新されています。全体として、これらの改良はユーザーの体験を向上させ、Azureサービスの利用をより効率的にすることを目指しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c2df9dc...MicrosoftDocs:6c09135){target="_blank"}

# ハイライト

このコードの変更では、主に複数のドキュメントや画像が更新されています。特に、C# SDKのクイックスタートガイドの手順変更、新しい機能やリリース情報が記載されたAzure AI Languageに関する最新情報、データプライバシーに関する更新、およびLlamaIndex設定手順やAzure AI Studioにおけるハブ作成手順が改善されています。これに伴い、関連する画像ファイルも最新のものに更新され、視覚的な手順の明確さが向上しました。

## 新機能
- Azure AI Languageの最新情報に2024年10月と11月の新機能追加。

## 破壊的変更
- 特になし。

## その他の更新
- C# SDKクイックスタートガイドのNuGetパッケージ検索手順が更新。
- 個人情報に関するエンティティカテゴリーから具体例が削除。
- AI Studioにおけるハブ作成手順の改善、および関連する画像が更新。

# 洞察

このコード変更は、一連のドキュメントの更新を目的としており、特にユーザーの体験を向上させることに焦点を当てています。

まず、C# SDKクイックスタートガイドの更新では、ユーザーが最新のNuGetパッケージを見つけやすくするための変更が加えられています。この変更は、ユーザーが不適切なパッケージを選んでしまうことを防ぐためのものであり、最新のC# SDKを正確に利用するために必要な配慮です。

次に、個人情報に関するエンティティカテゴリーでは、過剰な情報を削除することで説明が簡素化されました。これにより、ユーザーが核心となる情報を捉えやすくする狙いがあります。

さらに、Azure AI Languageにおける最新情報の更新は、技術の進展とサービスの改善を反映しています。ユーザーはサービスを最大限に活用するために、常に新しい情報を把握する必要があるため、この更新のタイムリーさが価値を高めています。

AI Studioのデータプライバシーに関する更新は、ユーザーがデータ管理の仕組みを理解しやすくすることを焦点としています。データの処理や保存についての理解を深めることは、現代のデジタルエコシステムにおいて非常に重要です。

最後に、画像の更新は、手順を視覚的にサポートすることでユーザーの理解を助ける施策です。視覚的な要素は、特に技術的な手順において主要な役割を果たします。

全体として、この一連の更新は、ユーザーの操作をより円滑にし、Azureサービスの利用効率を高めることを目的としています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [csharp-sdk.md](#item-ee69c7) | minor update | C# SDK Quickstartの変更 | modified | 1 | 1 | 2 | 
| [conversations-entity-categories.md](#item-c268ff) | minor update | 個人情報に関するエンティティカテゴリーの修正 | modified | 0 | 2 | 2 | 
| [whats-new.md](#item-69b272) | minor update | Azure AI Languageの最新情報の更新 | modified | 10 | 2 | 12 | 
| [concept-data-privacy.md](#item-af88ce) | minor update | データプライバシーに関する情報の更新 | modified | 2 | 2 | 4 | 
| [llama-index.md](#item-613372) | minor update | LlamaIndexのAzure OpenAIモデル設定手順の更新 | modified | 19 | 6 | 25 | 
| [create-hub.md](#item-9df177) | minor update | Azure AI Studioのハブ作成手順の改善 | modified | 9 | 2 | 11 | 
| [hub-new-connect-services.png](#item-f58912) | minor update | ハブ作成の接続サービスに関する画像の更新 | modified | 0 | 0 | 0 | 
| [hub-new.png](#item-7bcc34) | minor update | ハブ作成の画像の更新 | modified | 0 | 0 | 0 | 


# Modified Contents
## articles/ai-services/document-intelligence/quickstarts/includes/csharp-sdk.md{#item-ee69c7}

<details>
<summary>Diff</summary>
````diff
@@ -106,7 +106,7 @@ In this quickstart, use the following features to analyze and extract data and v
 
     :::image type="content" source="../../media/quickstarts/select-doc-intel-nuget-package.png" alt-text="Screenshot of select NuGet prerelease package window in Visual Studio.":::
 
-1. Select the **Browse** tab and type *Azure.AI.FormRecognizer*.
+1. Select the **Browse** tab and type *Azure.AI.DocumentIntelligence*.
 
 1. Select the **`Include prerelease`** checkbox.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDK Quickstartの変更"
}
```

### Explanation
この変更は、C# SDKに関するクイックスタートガイドの内容を更新しました。具体的には、NuGetパッケージを検索する際の手順が修正されました。以前は「Azure.AI.FormRecognizer」と入力する必要がありましたが、現在は「Azure.AI.DocumentIntelligence」と入力するように変更されています。この修正により、ユーザーが正しいパッケージを選択できるようになります。全体として、この小さな更新はユーザーエクスペリエンスの向上を目的としています。

## articles/ai-services/language-service/personally-identifiable-information/concepts/conversations-entity-categories.md{#item-c268ff}

<details>
<summary>Diff</summary>
````diff
@@ -154,8 +154,6 @@ This category contains the following entities:
         Any numeric or alphanumeric identifier that could contain any PII information. 
         Examples:   
             * Case Number 
-            * Driver's license
-            * Medicare Beneficiary Identifier (MBI)
             * Member Number 
             * Ticket number 
             * Bank account number 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人情報に関するエンティティカテゴリーの修正"
}
```

### Explanation
この変更では、個人情報（PII）に関連するエンティティカテゴリーの説明が修正されました。具体的には、いくつかの例が削除されています。削除されたのは「運転免許証」と「メディケア受給者識別子（MBI）」の2つであり、これによりこのカテゴリー内の説明が簡素化されました。この更新は、文書を明確に保つためのものであり、ユーザーが提供される情報をより把握しやすくすることを目的としています。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -15,9 +15,17 @@ ms.author: jboback
 
 Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent developments, this article provides you with information about new releases and features.
 
+## November 2024
+
+* [Native document support](native-document-support/use-native-documents.md) is now available in public preview `2024-11-15-preview` without gated preview limitations.
+
+## October 2024
+
+* Custom language service features enable you to deploy your project to multiple [resources within a single region](concepts/custom-features/multi-region-deployment.md) via the API, so that you can use your custom model wherever you need.
+
 ## September 2024
 
-* PII detection now has container support. See more details in the Azure Update post: [Announcing Text PII Redaction Container Release](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/announcing-text-pii-redaction-container-release/ba-p/4264655).
+* PII detection now has container support. See more details in the Azure Update post: [Announcing Text PII Redaction Container Release](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-text-pii-redaction-container-release/4264655).
 * Custom sentiment analysis (preview) will be retired on January 10th, 2025. Please transition to other custom model training services, such as custom text classification in Azure AI Language, by that date.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom sentiment analysis (preview) in Azure AI Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-sentiment-analysis-retirement).
 * Custom text analytics for health (preview) will be retired on January 10th, 2025. Please transition to other custom model training services, such as custom named entity recognition in Azure AI Language, by that date.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom text analytics for health (preview) in Azure AI Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-text-analytics-for-health-retirement).
 
@@ -27,7 +35,7 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
 
 ## July 2024
 
-* [Conversational PII redaction](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/announcing-conversational-pii-detection-service-s-general/ba-p/4162881) service in English-language contexts is now Generally Available (GA).
+* [Conversational PII redaction](https://techcommunity.microsoft.com/blog/ai-azure-ai-services-blog/announcing-conversational-pii-detection-service-s-general/4162881) service in English-language contexts is now Generally Available (GA).
 * Conversation Summarization now supports 12 additional languages in preview as listed [here](summarization/language-support.md).
 * Summarization Meeting or Conversation Chapter titles features will now support reduced length to focus on the key topics.
 * Enable support for data augmentation for diacritics to generate variations of training data for diacritic variations used in some natural languages which is especially useful for Germanic and Slavic languages. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Languageの最新情報の更新"
}
```

### Explanation
この変更では、Azure AI Languageに関する「最新情報」セクションが更新され、新機能やリリース情報が追加されました。具体的には、2024年11月と10月の新機能が追加され、ネイティブドキュメントサポートやカスタム言語サービスの多地域デプロイ機能についての情報が記載されています。また、2024年9月に関する情報の一部もリンクが更新されました。これにより、ユーザーは最新の機能とリリース状況を簡単に把握できるようになります。この更新は、継続的なサービスの改善を反映しています。

## articles/ai-studio/how-to/concept-data-privacy.md{#item-af88ce}

<details>
<summary>Diff</summary>
````diff
@@ -14,6 +14,8 @@ author: s-polly
 ---
 # Data, privacy, and security for use of models through the model catalog in AI Studio
 
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
+
 This article describes how the data that you provide is processed, used, and stored when you deploy models from the model catalog. Also see the [Microsoft Products and Services Data Protection Addendum](https://aka.ms/DPA), which governs data processing by Azure services.
 
 > [!IMPORTANT]
@@ -43,8 +45,6 @@ When you deploy a model from the model catalog (base or fine-tuned) by using ser
 
 The model processes your input prompts and generates outputs based on its functionality, as described in the model details. Your use of the model (along with the provider's accountability for the model and its outputs) is subject to the license terms for the model. Microsoft provides and manages the hosting infrastructure and API endpoint. The models hosted in this *model as a service* (MaaS) scenario are subject to Azure data, privacy, and security commitments. [Learn more about Azure compliance offerings applicable to Azure AI Studio](https://servicetrust.microsoft.com/DocumentPage/7adf2d9e-d7b5-4e71-bad8-713e6a183cf3).
 
-[!INCLUDE [feature-preview](../includes/feature-preview.md)]
-
 Microsoft acts as the data processor for prompts and outputs sent to, and generated by, a model deployed for pay-as-you-go inferencing (MaaS). Microsoft doesn't share these prompts and outputs with the model provider. Also, Microsoft doesn't use these prompts and outputs to train or improve Microsoft models, the model provider's models, or any third party's models.
 
 Models are stateless, and they don't store any prompts or outputs. If content filtering (preview) is enabled, the Azure AI Content Safety service screens prompts and outputs for certain categories of harmful content in real time. [Learn more about how Azure AI Content Safety processes data](/legal/cognitive-services/content-safety/data-privacy).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データプライバシーに関する情報の更新"
}
```

### Explanation
この変更では、AI Studioのモデルカタログを介したデータ、プライバシー、およびセキュリティに関する情報が更新されました。具体的には、プレビュー機能に関するインクルードが追加され、記事の文脈を強調しています。また、以前の告知においても同じインクルードが削除されています。この更新により、ユーザーはデータの処理、利用、および保存に関する最新情報をより明確に理解できるようになります。特に、マイクロソフトがデータプロセッサとしてどのように機能するか、またデータがどのように扱われるかについての理解が深まります。

## articles/ai-studio/how-to/develop/llama-index.md{#item-613372}

<details>
<summary>Diff</summary>
````diff
@@ -83,7 +83,7 @@ llm = AzureAICompletionsModel(
 ```
 
 > [!TIP]
-> If your model is an OpenAI model deployed to Azure OpenAI service or AI services resource, configure the client as indicated at [Azure OpenAI models and Azure AI model inference service](#azure-openai-models-and-azure-ai-model-infernece-service).
+> If your model deployment is hosted in Azure OpenAI service or Azure AI Services resource, configure the client as indicated at [Azure OpenAI models and Azure AI model inference service](#azure-openai-models-and-azure-ai-model-inference-service).
 
 If your endpoint is serving more than one model, like with the [Azure AI model inference service](../../ai-services/model-inference.md) or [GitHub Models](https://github.com/marketplace/models), you have to indicate `model_name` parameter:
 
@@ -128,23 +128,36 @@ llm = AzureAICompletionsModel(
 )
 ```
 
-### Azure OpenAI models and Azure AI model infernece service
+### Azure OpenAI models and Azure AI model inference service
 
-If you are using Azure OpenAI models or [Azure AI model inference service](../../ai-services/model-inference.md), ensure you have at least version `0.2.4` of the LlamaIndex integration. Use `api_version` parameter in case you need to select a specific `api_version`. For the [Azure AI model inference service](../../ai-services/model-inference.md), you need to pass `model_name` parameter:
+If you are using Azure OpenAI service or [Azure AI model inference service](../../ai-services/model-inference.md), ensure you have at least version `0.2.4` of the LlamaIndex integration. Use `api_version` parameter in case you need to select a specific `api_version`. 
+
+For the [Azure AI model inference service](../../ai-services/model-inference.md), you need to pass `model_name` parameter:
 
 ```python
 from llama_index.llms.azure_inference import AzureAICompletionsModel
 
 llm = AzureAICompletionsModel(
-    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    endpoint="https://<resource>.services.ai.azure.com/models",
+    credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
+    model_name="mistral-large-2407",
+)
+```
+
+For Azure OpenAI service:
+
+```python
+from llama_index.llms.azure_inference import AzureAICompletionsModel
+
+llm = AzureAICompletionsModel(
+    endpoint="https://<resource>.openai.azure.com/openai/deployments/<deployment-name>",
     credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
-    model_name="gpt-4o",
     api_version="2024-05-01-preview",
 )
 ```
 
 > [!TIP]
-> Using a wrong `api_version` or one not supported by the model results in a `ResourceNotFound` exception.
+> Check which is the API version that your deployment is using. Using a wrong `api_version` or one not supported by the model results in a `ResourceNotFound` exception.
 
 ### Inference parameters
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "LlamaIndexのAzure OpenAIモデル設定手順の更新"
}
```

### Explanation
この変更では、LlamaIndexを用いたAzureのOpenAIモデルの設定手順が更新され、いくつかの表現が改善されました。特に、「モデルがAzure OpenAIサービスまたはAzure AIサービスリソースでホストされている場合」の記述が明確に修正され、関連するリンクも訂正されました。また、モデルのエンドポイントの指定方法が具体的に示され、より分かりやすくなっています。加えて、APIバージョンの使用に関する注意が強調され、誤ったAPIバージョンを使用することのリスクについての情報も更新されました。この更新により、ユーザーが正確に設定を行い、円滑にモデルを利用できるようになります。

## articles/ai-studio/includes/create-hub.md{#item-9df177}

<details>
<summary>Diff</summary>
````diff
@@ -10,17 +10,24 @@ ms.date: 5/21/2024
 ms.custom: include, build-2024
 ---
 
+> [!NOTE]
+> A hub in Azure AI Studio is a one-stop shop where you manage everything your AI project needs, like security and resources, so you can develop and test faster. To learn more about how hubs can help you, see the [Hubs and projects overview](/azure/ai-studio/concepts/ai-resources) article.
+
 To create a hub in [Azure AI Studio](https://ai.azure.com), follow these steps:
 
 1. Go to the **Home** page in [Azure AI Studio](https://ai.azure.com) and sign in with your Azure account.
-1. Select **All hubs** from the left pane and then select **+ New hub**.
+1. Select **All resources** on the left pane. If you cannot see this option, in the top bar select **All resources & projects**. Then select **+ New hub**.
 
     :::image type="content" source="../media/how-to/hubs/hub-new.png" alt-text="Screenshot of the button to create a new hub." lightbox="../media/how-to/hubs/hub-new.png":::
 
-1. In the **Create a new hub** dialog, enter a name for your hub (such as *contoso-hub*) and select **Next**. Leave the default **Connect Azure AI Services** option selected. A new AI services connection is created for the hub.
+1. In the **Create a new hub** dialog, enter a name for your hub (such as *contoso-hub*). If you don't have a resource group, a new **Resource group** will be created linked to the **Subscription** provided. Leave the default **Connect Azure AI Services** option selected. 
+1. Select **Next**. If you didn't reuse an existing resource group, a new resource group (*rg-contoso*) is created.  Also an Azure AI service (*ai-contoso-hub*) is created for the hub.
 
     :::image type="content" source="../media/how-to/hubs/hub-new-connect-services.png" alt-text="Screenshot of the dialog to connect services while creating a new hub." lightbox="../media/how-to/hubs/hub-new-connect-services.png":::
 
+    > [!NOTE]
+    > If you don't see (new) before the **Resource group** and **Connect Azure AI Services** entries then an existing resource is being used. For the purposes of this tutorial, create a seperate entity via **Create new resource group** and **Create new AI Services**. This will allow you to prevent any unexpected charges by deleting the entities after the tutorial.
+
 1. Review the information and select **Create**.
 
     :::image type="content" source="../media/how-to/hubs/hub-new-review-create.png" alt-text="Screenshot of the dialog to review the settings for the new hub." lightbox="../media/how-to/hubs/hub-new-review-create.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのハブ作成手順の改善"
}
```

### Explanation
この変更では、Azure AI Studioでハブを作成する手順が改善され、いくつかの追加情報が提供されています。特に、ハブがAIプロジェクトにおいてどのように役立つかを説明するノートが新たに追加され、ユーザーがハブの重要性を理解しやすくなっています。また、ハブ作成プロセスにおけるリソースグループの作成についての説明が具体化され、既存のリソースを使用する際の注意点も明確化されています。これにより、ユーザーは不要な費用を避けるために新しいリソースを作成することの重要性を認識できるようになり、手順をより安全に進められるようになります。全体として、この更新はユーザーエクスペリエンスの向上に寄与しています。

## articles/ai-studio/media/how-to/hubs/hub-new-connect-services.png{#item-f58912}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハブ作成の接続サービスに関する画像の更新"
}
```

### Explanation
この変更では、Azure AI Studioのハブ作成手順に関連する画像「hub-new-connect-services.png」が更新されました。具体的な内容に関しては、追加や削除はなく、画像ファイル自体が改訂されている可能性があります。この画像は、ハブ作成時にサービスを接続するプロセスを視覚的に示しており、ユーザーが手順を理解するのを助けます。視覚的要素の改善により、手順の明確さが向上し、全体的なユーザーエクスペリエンスが向上することが期待されます。

## articles/ai-studio/media/how-to/hubs/hub-new.png{#item-7bcc34}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハブ作成の画像の更新"
}
```

### Explanation
この変更では、Azure AI Studioのハブ作成手順に関連する画像「hub-new.png」が更新されました。具体的な変更内容は記載されていませんが、画像自体の更新が行われたことにより、手順をより明確に視覚化している可能性があります。この画像は、ユーザーがハブを新規に作成する際のインターフェースや操作方法を示しており、新たな情報や改善された内容が反映されているでしょう。画像の質的向上や情報の正確性向上が期待され、ユーザーの理解を助ける結果となるでしょう。


