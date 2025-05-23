---
date: '2025-05-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:aedda49...MicrosoftDocs:2512fb2
summary: 今回のコード変更では、Azure GovernmentのOpenAIサービスに関する文書が更新され、特定のサービス提供情報が削除されました。ファインチューニングモデルの引退スケジュールに関する新しい情報が追加され、モデルルーターの課金情報が明確化されました。また、音声生成クライアントの変数名が修正され、表記の一貫性が向上しました。全体として、ユーザーが情報をより正確に理解できるようにするための重要な更新が含まれています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:aedda49...MicrosoftDocs:2512fb2){target="_blank"}

# ハイライト

今回のコード変更には、Azure GovernmentにおけるOpenAIサービスに関する文書の更新が含まれています。主な新機能として、Azure Government内での特定のサービスの提供についての情報が削除されたことがあります。また、OpenAIモデルの引退に関する文書が更新され、ファインチューニングモデルとその引退スケジュールについて詳述されています。他にも、モデルルーターの使用に関する課金情報の更新や、音声生成クライアントの変数名の修正が行われています。

## 新機能

- 新しい情報の追加：ファインチューニングモデルの引退スケジュールに関する新しい情報が追加され、モデルの引退に関するテーブルが拡充されました。
  
## 破壊的変更

- なし

## その他の更新

- 「Reserved Instance Provisioned Deployments」に関する注意事項がAzure Governmentの文書から削除されました。
- モデルルーターの課金情報が修正され、使用時の料金構造が明確化されました。
- 音声生成クライアントの変数名が、大文字から小文字への変更によって一貫性を持ちました。
- `GPT-4o mini`の表記を`GPT-4o-mini`に変更し、記述の一貫性を向上させました。

# 洞察

今回の変更は、主にマイナーな更新として位置付けられていますが、文書の内容をより正確にし、ユーザーが情報を適切に理解できるようにするための重要な修正が含まれています。例えば、Azure Governmentでの「Reserved Instance Provisioned Deployments」に関する注意事項が削除されたことは、今後の機能提供の変更を反映するための重要な一手です。これにより、ユーザーは最新のサービス提供状況を十分に把握することが可能になります。

また、OpenAIモデルの引退に関しては、スケジュールに新しい情報が加わることで、開発者がモデルのライフサイクルを適切に管理しやすくなっています。特にファインチューニングモデルがベースモデルとは異なるスケジュールを持つ点は、モデル管理の柔軟性を高める重要な更新です。

さらに、モデルルーターの課金情報については、これまでは基盤モデルの使用にのみ課金されていましたが、今後はモデルルーター自体の使用にも料金が発生することが明示されました。これにより、企業はコスト計算を正確に行い、予算管理をより効果的に行うことが可能になります。

最後に、音声生成クライアントの変数名修正やGPTモデルの名称修正など、一見小さな変更も、コーディングスタイルや情報の一貫性を維持する上で大きな影響を及ぼすことがあります。特に大規模なチームで開発が行われる場合、こうした一貫性はプロジェクト全体の可読性向上に寄与し、開発効率を高める助けとなります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-government.md](#item-a47549) | minor update | Azure GovernmentにおけるOpenAIサービスの更新 | modified | 0 | 3 | 3 | 
| [model-retirements.md](#item-03fc2e) | minor update | モデルの引退に関するインフォメーションの更新 | modified | 22 | 3 | 25 | 
| [model-router.md](#item-e9922a) | minor update | モデルルーターの請求情報の更新 | modified | 1 | 1 | 2 | 
| [text-to-speech-dotnet.md](#item-fea66a) | minor update | 音声生成クライアント変数名の修正 | modified | 1 | 1 | 2 | 
| [overview.md](#item-97d507) | minor update | GPT-4o-miniの名称修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/azure-government.md{#item-a47549}

<details>
<summary>Diff</summary>
````diff
@@ -49,9 +49,6 @@ To request quota increases for these models, submit a request at [https://aka.ms
 | usgovarizona  | ✅ | - | - | ✅ |
 | usgovvirginia | ✅ | - | - | ✅ |
 
-> [!IMPORTANT]
-> Reserved Instance Provisioned Deployments are now available in Azure Government as of May 2025. Refer to [Provisioned Managed Offering in Azure Government](./concepts/gov-provisioned.md) for more details.
-
 <br>
 
 ## Azure OpenAI features
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure GovernmentにおけるOpenAIサービスの更新"
}
```

### Explanation
この変更は、Azure Governmentに関するOpenAIサービスの文書において、重要な情報を更新したものです。特に、2025年5月からAzure Governmentで利用可能になる「Reserved Instance Provisioned Deployments」に関する注意事項が削除されました。この deletion は、最新の機能やサービスの展開を反映し、より正確な情報を提供することを目的としています。変更された箇所は3行で、内容に大きな影響を与えないマイナーな更新です。

## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -87,15 +87,15 @@ For more information on how to manage model upgrades and migrations for provisio
 > [!NOTE]
 > Not all models go through a deprecation period prior to retirement. Some models/versions only have a retirement date.
 >
-> **Fine-tuned models** are subject to the same deprecation and retirement schedule as their equivalent base model.
+> **Fine-tuned models** are subject to a [different](#fine-tuned-models) deprecation and retirement schedule from their equivalent base model.
 
 These models are currently available for use in Azure OpenAI.
 
 | Model                     | Version         | Retirement date                    | Replacement model                    |
 | --------------------------|-----------------|------------------------------------|--------------------------------------|
 | `computer-use-preview`    | 2025-03-11      | No earlier than June 11, 2025      |                                      |
 | `dall-e-3`                | 3               | No earlier than June 30, 2025      |                                      |
-| `gpt-35-turbo-16k`        | 0613            | April, 30, 2025                    | `gpt-4.1-mini` version: `2025-04-14` |
+| `gpt-35-turbo-16k`        | 0613            | April  30, 2025                    | `gpt-4.1-mini` version: `2025-04-14` |
 | `gpt-35-turbo`            | 1106            | No earlier than July 16, 2025      | `gpt-4.1-mini` version: `2025-04-14` |
 | `gpt-35-turbo`            | 0125            | No earlier than July 16, 2025      | `gpt-4.1-mini` version: `2025-04-14` |
 | `gpt-4`<br>`gpt-4-32k`    | 0314            | June 6, 2025                       | `gpt-4o` version: `2024-11-20`       |
@@ -130,11 +130,30 @@ We'll notify all customers with these preview deployments at least 30 days befor
 > [!TIP]
 > **Will a model upgrade happen if the new model version is not yet available in that region?**
 >
-> Yes, even in cases where the latest model version is not yet available in a region, we will automatically upgrade deployments during the scheduled upgrade window. For more information, see [Azure OpenAI model versions](/azure/ai-services/openai/concepts/model-versions#will-a-model-upgrade-happen-if-the-new-model-version-is-not-yet-available-in-that-region).
+> Yes, even in cases where the latest model version is not yet available in a region, we'll automatically upgrade deployments during the scheduled upgrade window. For more information, see [Azure OpenAI model versions](/azure/ai-services/openai/concepts/model-versions#will-a-model-upgrade-happen-if-the-new-model-version-is-not-yet-available-in-that-region).
 
 > [!IMPORTANT]
 > Vision enhancements preview features including Optical Character Recognition (OCR), object grounding, video prompts will be retired and no longer available once `gpt-4` Version: `vision-preview` is upgraded to `turbo-2024-04-09`. If you're currently relying on any of these preview features, this automatic model upgrade will be a breaking change.
 
+## Fine-tuned models
+
+Fine-tuned models retire in two phases: training and deployment.
+
+All fine-tuned models follow their equivalent base model for **training** retirement. Once retired, a given model is no longer available for fine tuning.
+
+For fine-tuned models made generally available since `gpt-4o-2024-08-06`, **deployment** retirement occurs 1 year after **training** retirement. At deployment retirement, inference and deployment returns error responses.
+
+| Model            | Version     | Training retirement date  | Deployment retirement date       |
+| -----------------|-------------|---------------------------|----------------------------------|
+| `gpt-35-turbo`   | 1106        | At base model retirement  | At training retirement           |
+| `gpt-35-turbo`   | 0125        | At base model retirement  | At training retirement           |
+| `gpt-4o`         | 2024-08-06  | At base model retirement  | One year after training retirement |
+| `gpt-4o-mini`    | 2024-07-18  | At base model retirement  | One year after training retirement |
+| `gpt-4.1`        | 2025-04-14  | At base model retirement  | One year after training retirement |
+| `gpt-4.1-mini`   | 2025-04-14  | At base model retirement  | One year after training retirement |
+| `gpt-4.1-nano`   | 2025-04-14  | At base model retirement  | One year after training retirement |
+| `o4-mini`        | 2025-04-16  | At base model retirement  | One year after training retirement |
+
 ## Default model versions
 
 | Model | Current default version | New default version | Default upgrade date |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの引退に関するインフォメーションの更新"
}
```

### Explanation
この変更は、OpenAIモデルの引退に関する文書を更新し、特にファインチューニングモデルに関連するスケジュールの明確化を図るものです。具体的には、ファインチューニングモデルが従来のベースモデルとは異なる引退スケジュールに従うことが明示され、新しい情報が追加されました。また、モデルの引退に関するテーブルが拡充され、トレーニング引退日とデプロイメント引退日に関する新しい詳細も加えられています。これにより、ユーザーがモデルの引退プロセスをよりよく理解できるようになります。全体的に、追加された22行と削除された3行を含む25行の変更は、情報の精度と明確さを向上させるためのマイナーな更新と位置付けられます。

## articles/ai-services/openai/concepts/model-router.md{#item-e9922a}

<details>
<summary>Diff</summary>
````diff
@@ -54,7 +54,7 @@ Model router doesn't process audio input.
 
 ## Billing information
 
-When you use model router, you're only billed for the use of the underlying models as they're recruited to respond to prompts. The model routing function itself doesn't incur any extra charges.
+When you use model router today, you're only billed for the use of the underlying models as they're recruited to respond to prompts: the model routing function itself doesn't incur any extra charges. Starting August 1, the model router usage will be charged as well.
 
 You can monitor the costs of your model router deployment in the Azure portal.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルルーターの請求情報の更新"
}
```

### Explanation
この変更は、OpenAIのモデルルーターに関する文書の請求情報を更新するものです。具体的には、モデルルーターを使用する際の請求についての説明が更新され、現在は基盤となるモデルの使用に対してのみ課金されることが強調されましたが、2023年8月1日以降はモデルルーターの使用にも料金が発生することが明示されています。これにより、ユーザーはモデルルーターの使用に関する料金構造をより正確に理解できるようになり、変更は1行の追加と1行の削除を伴う2行の修正にとどまりますが、重要な情報を反映するためのマイナーな更新と見なされます。

## articles/ai-services/openai/includes/text-to-speech-dotnet.md{#item-fea66a}

<details>
<summary>Diff</summary>
````diff
@@ -98,7 +98,7 @@ To run the quickstart, follow these steps:
     var speechFilePath = "YOUR_AUDIO_FILE_PATH";
     
     AzureOpenAIClient openAIClient = new AzureOpenAIClient(endpoint, credentials);
-    AudioClient = openAIClient.GetAudioClient(deploymentName);
+    AudioClient audioClient = openAIClient.GetAudioClient(deploymentName);
     
     var result = await audioClient.GenerateSpeechAsync(
                     "the quick brown chicken jumped over the lazy dogs");
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "音声生成クライアント変数名の修正"
}
```

### Explanation
この変更は、音声生成に関するドキュメントのコード例における変数名を修正するものです。具体的には、`AudioClient`が大文字で始まっていたものを、小文字の`audioClient`に変更しました。この修正により、一貫性のある変数命名規則が保たれ、コードの可読性が向上します。変更は1行の追加と1行の削除を伴う2行の修正であり、重要な機能には影響を与えないマイナーな更新と位置付けられます。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -86,7 +86,7 @@ The total number of tokens processed in a given request depends on the length of
  
 #### Image tokens
 
-Azure OpenAI's image processing capabilities with GPT-4o, GPT-4o mini, and GPT-4 Turbo with Vision models uses image tokenization to determine the total number of tokens consumed by image inputs. The number of tokens consumed is calculated based on two main factors: the level of image detail (low or high) and the image’s dimensions. Here's how token costs are calculated:
+Azure OpenAI's image processing capabilities with GPT-4o, GPT-4o-mini, and GPT-4 Turbo with Vision models uses image tokenization to determine the total number of tokens consumed by image inputs. The number of tokens consumed is calculated based on two main factors: the level of image detail (low or high) and the image’s dimensions. Here's how token costs are calculated:
 
 - **Low resolution mode**
   - Low detail allows the API to return faster responses for scenarios that don't require high image resolution analysis. The tokens consumed for low detail images are:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4o-miniの名称修正"
}
```

### Explanation
今回の変更は、Azure OpenAIの画像処理機能に関する記述の一部を修正したものです。具体的には、`GPT-4o mini`という表記を`GPT-4o-mini`に変更しました。この修正により、表記が統一され、情報の一貫性が向上します。変更は1行の追加と1行の削除を伴う2行の修正ですが、内容の理解を助けるための重要なポイントであり、マイナーな更新とされています。


