---
date: '2025-02-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:42a07e4...MicrosoftDocs:63a40ca
summary: このコードの変更は、Azure OpenAIに関する文書のメタデータやリンクの更新が主な内容で、特に新しいGPT-4.5プレビューに関する情報や行動規範のリンク修正が含まれています。主な新機能としては、GPT-4.5プレビューに関するセクションの追加や、新しいAPIについての情報が含まれています。大きな破壊的変更はありませんが、メタデータの変更により情報の分類が若干変更される可能性があります。ユーザーにとって最新のモデルやAPIに関する詳細が得られる重要なアップデートであり、文書の信頼性と正確さが向上しています。全体として、文書の質と利用の利便性が向上したことが強調されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:42a07e4...MicrosoftDocs:63a40ca){target="_blank"}

<format>
# Highlights
このコードの変更は、Azure OpenAIに関する文書のメタデータやリンクの更新が主な内容です。特に、新しいGPT-4.5プレビューに関する情報や、行動規範のリンク修正などが含まれ、最新情報へと更新されています。  

## New features
- `models.md` でのGPT-4.5プレビューに関するセクションの追加。
- `whats-new.md` にGPT-4.5プレビューに関する詳細情報と登録手続きの説明を追加。
- `whats-new.md`内に「Stored completions API」に関する新セクションも追加。

## Breaking changes
今回の変更には大きな破壊的変更は含まれていませんが、メタデータの変更により、情報の分類とアクセス手段が若干変更される可能性があります。

## Other updates
- いくつかのファイルで`ms.topic`の値が「conceptual」から「reference」に変更され、より正確な内容分類。
- 各ドキュメントの更新日 (`ms.date`) が最新の日付に変更。
- リンクが最新情報を指すように改善され、「行動規範」リンクも更新。
- ナビゲーションメニューの項目名とリンクがより鮮明に及び整然と更新されました。

# Insights
今回の更新は、Azure OpenAIサービスの文書を利用する開発者やユーザーにとって重要です。メタデータの改善により、ドキュメントがどのように分類され、検索されるかが明確になったことにより、リファレンス情報にアクセスするプロセスがスムーズになっています。  

また、新たに追加されたGPT-4.5プレビューに関するセクションと「Stored completions API」の情報は、最新のモデルとAPIに関する詳細を提供するため、Azure OpenAIの性能向上に関心のあるユーザーには特に有益です。このようなアップデートは、利用者が最新のツールや技術を迅速に理解し、それらを効果的に活用する手助けとなるでしょう。これに加えて、リンクやトピック分類の更新は、文書の保持する情報の信頼性と正確さを保障し、サービスの利用における法的および倫理的責任の理解を補完するものです。  

総じて、このアップデートは文書の質とサービス利用のコンテキストにおける利便性を大いに向上させています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [assistants-reference-messages.md](#item-1c8daa) | minor update | 記事のメタデータ更新: トピックタイプと日付変更 | modified | 2 | 2 | 4 | 
| [assistants-reference-runs.md](#item-ac752c) | minor update | 記事のメタデータ更新: トピックタイプ変更 | modified | 1 | 1 | 2 | 
| [assistants-reference-threads.md](#item-d19db7) | minor update | 記事のメタデータ更新: トピックタイプと日付変更 | modified | 2 | 2 | 4 | 
| [assistants-reference.md](#item-52344f) | minor update | 記事のメタデータ更新: トピックタイプと日付変更 | modified | 2 | 2 | 4 | 
| [abuse-monitoring.md](#item-b7afcb) | minor update | 不正使用監視記事のリンク修正 | modified | 2 | 2 | 4 | 
| [content-filter.md](#item-dfc7e7) | minor update | コンテンツフィルタ記事の更新: 日付およびフォーマット修正 | modified | 3 | 5 | 8 | 
| [models.md](#item-db2c37) | minor update | モデル記事の更新: GPT-4.5プレビューの追加 | modified | 30 | 1 | 31 | 
| [fine-tuning.md](#item-5c0e85) | minor update | ファインチューニング手順の修正: デプロイ削除手順の更新 | modified | 2 | 1 | 3 | 
| [content-filter-configurability.md](#item-11f064) | minor update | 内容フィルタの設定に関するリンクの修正 | modified | 1 | 1 | 2 | 
| [index.yml](#item-0adb87) | minor update | 行動規範のリンクの修正 | modified | 1 | 1 | 2 | 
| [overview.md](#item-97d507) | minor update | 行動規範のリンクの修正 | modified | 1 | 1 | 2 | 
| [quotas-limits.md](#item-06c6f9) | minor update | GPT-4.5プレビューに関するクォータ情報の追加 | modified | 8 | 1 | 9 | 
| [azure-search.md](#item-32f34c) | minor update | トピックの変更と日付の更新 | modified | 2 | 2 | 4 | 
| [cosmos-db.md](#item-d6e2e5) | minor update | トピックの変更と日付の更新 | modified | 2 | 2 | 4 | 
| [elasticsearch.md](#item-bb82ea) | minor update | トピックの変更と日付の更新 | modified | 2 | 2 | 4 | 
| [mongo-db.md](#item-7516e1) | minor update | トピックの変更と日付の更新 | modified | 2 | 2 | 4 | 
| [on-your-data.md](#item-c35b1e) | minor update | トピックの変更と日付の更新 | modified | 2 | 2 | 4 | 
| [pinecone.md](#item-4d8746) | minor update | トピックの変更と日付の更新 | modified | 2 | 2 | 4 | 
| [toc.yml](#item-c945af) | minor update | 項目名の変更とリンクの修正 | modified | 3 | 3 | 6 | 
| [whats-new.md](#item-53303b) | minor update | 新機能の追加と日付の更新 | modified | 16 | 2 | 18 | 


# Modified Contents
## articles/ai-services/openai/assistants-reference-messages.md{#item-1c8daa}

<details>
<summary>Diff</summary>
````diff
@@ -4,8 +4,8 @@ titleSuffix: Azure OpenAI
 description: Learn how to use Azure OpenAI's Python & REST API messages with Assistants.
 manager: nitinme
 ms.service: azure-ai-openai
-ms.topic: conceptual
-ms.date: 09/25/2024
+ms.topic: reference
+ms.date: 02/27/2025
 author: aahill
 ms.author: aahi
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事のメタデータ更新: トピックタイプと日付変更"
}
```

### Explanation
この変更は、記事「assistants-reference-messages.md」のメタデータに関連しており、トピックの種類と日付を更新する内容です。具体的には、既存の `ms.topic` フィールドの値を「conceptual」から「reference」に変更し、`ms.date` フィールドの値を2024年9月25日から2025年2月27日に更新しています。これにより、記事がより正確にその内容と更新日を反映することになります。

## articles/ai-services/openai/assistants-reference-runs.md{#item-ac752c}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn how to use Azure OpenAI's Python & REST API runs with Assistants.
 manager: nitinme
 ms.service: azure-ai-openai
-ms.topic: conceptual
+ms.topic: reference
 ms.date: 09/17/2024
 author: aahill
 ms.author: aahi
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事のメタデータ更新: トピックタイプ変更"
}
```

### Explanation
この変更は、記事「assistants-reference-runs.md」のメタデータの更新に関するもので、トピックの種類を変更しています。具体的には、`ms.topic` フィールドの値が「conceptual」から「reference」に変更されました。この更新により、記事がより適切にその内容に対応するトピックタイプを反映することになっています。また、他のメタデータはそのまま維持されています。

## articles/ai-services/openai/assistants-reference-threads.md{#item-d19db7}

<details>
<summary>Diff</summary>
````diff
@@ -4,8 +4,8 @@ titleSuffix: Azure OpenAI
 description: Learn how to use Azure OpenAI's Python & REST API threads with Assistants.
 manager: nitinme
 ms.service: azure-ai-openai
-ms.topic: conceptual
-ms.date: 09/17/2024
+ms.topic: reference
+ms.date: 02/27/2025
 author: aahill
 ms.author: aahi
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事のメタデータ更新: トピックタイプと日付変更"
}
```

### Explanation
この変更は、記事「assistants-reference-threads.md」のメタデータを更新するもので、特にトピックの種類と日付を変更しています。具体的には、`ms.topic` フィールドの値が「conceptual」から「reference」に変更され、`ms.date` フィールドの値が2024年9月17日から2025年2月27日に更新されています。これにより、記事がより正確にその内容と更新日を反映することになります。記事の内容は維持され、メタデータの適切な管理が促進されます。

## articles/ai-services/openai/assistants-reference.md{#item-52344f}

<details>
<summary>Diff</summary>
````diff
@@ -4,8 +4,8 @@ titleSuffix: Azure OpenAI
 description: Learn how to use Azure OpenAI's Python & REST API with Assistants.
 manager: nitinme
 ms.service: azure-ai-openai
-ms.topic: conceptual
-ms.date: 09/17/2024
+ms.topic: reference
+ms.date: 02/27/2025
 author: aahill
 ms.author: aahi
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事のメタデータ更新: トピックタイプと日付変更"
}
```

### Explanation
この変更は、記事「assistants-reference.md」のメタデータを更新するもので、主にトピックの種類と日付に関する変更が含まれています。具体的に言うと、`ms.topic` フィールドが「conceptual」から「reference」に変更され、`ms.date` フィールドの日付が2024年9月17日から2025年2月27日に更新されています。この変更により、記事が内容により適したトピックタイプと最新の日付を反映することになり、読者にとってのコンテンツの関連性が向上します。記事の基本情報もそのまま維持されています。

## articles/ai-services/openai/concepts/abuse-monitoring.md{#item-b7afcb}

<details>
<summary>Diff</summary>
````diff
@@ -13,13 +13,13 @@ manager: nitinme
 
 # Abuse Monitoring
 
-Azure OpenAI Service detects and mitigates instances of recurring content and/or behaviors that suggest use of the service in a manner that might violate the [Code of Conduct](/legal/cognitive-services/openai/code-of-conduct?context=/azure/ai-services/openai/context/context). Details on how data is handled can be found on the [Data, Privacy, and Security](/legal/cognitive-services/openai/data-privacy?context=/azure/ai-services/openai/context/context) page.
+Azure OpenAI Service detects and mitigates instances of recurring content and/or behaviors that suggest use of the service in a manner that might violate the [Code of Conduct](https://aka.ms/AI-CoC). Details on how data is handled can be found on the [Data, Privacy, and Security](/legal/cognitive-services/openai/data-privacy?context=/azure/ai-services/openai/context/context) page.
 
 ## Components of abuse monitoring
 
 There are several components to abuse monitoring:
 
-- **Content Classification**: Classifier models detect harmful text and/or images in user prompts (inputs) and completions (outputs). The system looks for categories of harms as defined in the [Content Requirements](/legal/cognitive-services/openai/code-of-conduct?context=/azure/ai-services/openai/context/context), and assigns severity levels as described in more detail on the [Content Filtering](/azure/ai-services/openai/concepts/content-filter) page. The content classification signals contribute to pattern detection as described below.  
+- **Content Classification**: Classifier models detect harmful text and/or images in user prompts (inputs) and completions (outputs). The system looks for categories of harms as defined in the [Content Requirements](/legal/ai-code-of-conduct?context=/azure/ai-services/openai/context/context), and assigns severity levels as described in more detail on the [Content Filtering](/azure/ai-services/openai/concepts/content-filter) page. The content classification signals contribute to pattern detection as described below.  
 - **Abuse Pattern Capture**: Azure OpenAI Service’s abuse monitoring system looks at customer usage patterns and employs algorithms and heuristics to detect and score indicators of potential abuse. Detected patterns consider, for example, the frequency and severity at which harmful content is detected (as indicated in content classifier signals) in a customer’s prompts and completions, as well as the intentionality of the behavior. The trends and urgency of the detected pattern will also affect scoring of potential abuse severity.
     For example, a higher volume of harmful content classified as higher severity, or recurring conduct indicating intentionality (such as recurring jailbreak attempts) are both more likely to receive a high score indicating potential abuse. 
 - **Review and Decision**: Prompts and completions that are flagged through content classification and/or identified as part of a potentially abusive pattern of use are subjected to another review process to help confirm the system’s analysis and inform actioning decisions for abuse monitoring. Such review is conducted through two methods: automated review and human review.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "不正使用監視記事のリンク修正"
}
```

### Explanation
この変更は、記事「abuse-monitoring.md」におけるリンクの修正を含んでいます。具体的には、サービスの利用が「行動規範」（Code of Conduct）に違反する可能性がある場合を示唆するコンテンツや行動の検出と軽減を説明する部分で、元のリンクが短縮URLに変更されています。さらに、記事内の「Content Requirements」へのリンクも変更されており、これによりユーザーは最新の関連情報にアクセスしやすくなります。その他の内容は変更されておらず、記事全体の構造と情報の整合性は維持されています。

## articles/ai-services/openai/concepts/content-filter.md{#item-dfc7e7}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: PatrickFarley
 ms.author: pafarley
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 02/20/2025
+ms.date: 02/27/2025
 ms.custom: template-concept, devx-track-python
 manager: nitinme
 ---
@@ -820,9 +820,7 @@ This is an example message array:
 In addition to detection on last user content, Azure OpenAI also supports the detection of specific risks inside context documents via Prompt Shields – Indirect Prompt Attack Detection. You should identify parts of the input that are a document (for example, retrieved website, email, etc.) with the following document delimiter.  
 
 ```
-<documents> 
-*insert your document content here* 
-</documents>
+\"\"\" <documents> *insert your document content here* </documents> \"\"\" 
 ```
 
 When you do so, the following options are available for detection on tagged documents: 
@@ -1051,4 +1049,4 @@ As part of your application design, consider the following best practices to del
 - Apply for modified content filters via [this form](https://ncv.microsoft.com/uEfCgnITdR).
 - Azure OpenAI content filtering is powered by [Azure AI Content Safety](https://azure.microsoft.com/products/cognitive-services/ai-content-safety).
 - Learn more about understanding and mitigating risks associated with your application: [Overview of Responsible AI practices for Azure OpenAI models](/legal/cognitive-services/openai/overview?context=/azure/ai-services/openai/context/context).
-- Learn more about how data is processed in connection with content filtering and abuse monitoring: [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy?context=/azure/ai-services/openai/context/context#preventing-abuse-and-harmful-content-generation).
\ No newline at end of file
+- Learn more about how data is processed in connection with content filtering and abuse monitoring: [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy?context=/azure/ai-services/openai/context/context#preventing-abuse-and-harmful-content-generation).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタ記事の更新: 日付およびフォーマット修正"
}
```

### Explanation
この変更は、記事「content-filter.md」における日付の更新とコードブロックのフォーマット修正を含んでいます。具体的には、`ms.date` フィールドが2025年2月20日から2025年2月27日に変更され、記事がより新しい内容を反映するようになりました。また、特定のリスクを検出するためのドキュメントデリミタの使用方法が修正され、サンプルコードが新しいフォーマットに適応しました。さらに、データの処理に関する文についても改訂はありませんが、明確に情報が提供されています。このような更新により、情報が最新で分かりやすくなり、読者がコンテンツフィルタの機能をより理解しやすくなっています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 2/19/2025
+ms.date: 2/27/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -18,6 +18,7 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 
 | Models | Description |
 |--|--|
+| [GPT-4.5 Preview](#gpt-45-preview) |The latest GPT model that excels at diverse text and image tasks.  |
 | [o-series models](#o-series-models) |[Reasoning models](../how-to/reasoning.md) with advanced problem-solving and increased focus and capability.  |
 | [GPT-4o & GPT-4o mini & GPT-4 Turbo](#gpt-4o-and-gpt-4-turbo) | The latest most capable Azure OpenAI models with multimodal versions, which can accept both text and images as input. |
 | [GPT-4o audio](#gpt-4o-audio) | GPT-4o audio models that support either low-latency, "speech in, speech out" conversational interactions or audio generation. |
@@ -28,6 +29,31 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 | [Whisper](#whisper-models) | A series of models in preview that can transcribe and translate speech to text. |
 | [Text to speech](#text-to-speech-models-preview) (Preview) | A series of models in preview that can synthesize text to speech. |
 
+## GPT-4.5 Preview
+
+### Availability
+
+**For access to `gpt-4.5-preview` registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who have access to other limited access models will still need to request access for this model.
+
+Request access: [GPT-4.5-preview limited access model application](https://aka.ms/oai/gptaccess)
+
+Once access has been granted, you will need to create a deployment for the model
+
+### Region Availability
+
+| Model | Region |
+|---|---|
+| `gpt-4.5-preview` | East US 2 (Global Standard) <br> Sweden Central (Global Standard) |
+
+### Capabilities
+
+|  Model ID  | Description | Context Window | Max Output Tokens | Training Data (up to)  |
+|  --- |  :--- |:--- |:---|:---: |
+| `gpt-4.5-preview` (2025-02-27) <br> **GPT-4.5 Preview**  | The **latest GPT model** that excels at diverse text and image tasks. <br>-Structured outputs <br>-Prompt caching <br>-Tools <br>-Streaming<br>-Text(input/output)<br>- Image(input)   | 128,000 | 16,384 | Oct 2023 |
+
+> [!NOTE]
+> It is expected behavior that the model cannot answer questions about itself. If you want to know when the knowledge cutoff for the model's training data is, or other details about the model you should refer to the model documentation above.
+
 ## o-series models
 
 The Azure OpenAI o<sup>&#42;</sup> series models are specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
@@ -64,6 +90,9 @@ The GPT 4o audio models are part of the GPT-4o model family and support either l
 - GPT-4o real-time audio is designed to handle real-time, low-latency conversational interactions, making it a great fit for support agents, assistants, translators, and other use cases that need highly responsive back-and-forth with a user. For more information on how to use GPT-4o real-time audio, see the [GPT-4o real-time audio quickstart](../realtime-audio-quickstart.md) and [how to use GPT-4o audio](../how-to/realtime-audio.md).
 - GPT-4o audio completion is designed to generate audio from audio or text prompts, making it a great fit for generating audio books, audio content, and other use cases that require audio generation. The GPT-4o audio completions model introduces the audio modality into the existing `/chat/completions` API. For more information on how to use GPT-4o audio completions, see the [audio generation quickstart](../audio-completions-quickstart.md).
 
+> [!CAUTION]
+> We don't recommend using preview models in production. We will upgrade all deployments of preview models to either future preview versions or to the latest stable GA version. Models that are designated preview don't follow the standard Azure OpenAI model lifecycle.
+
 To use GPT-4o audio, you need [an Azure OpenAI resource](../how-to/create-resource.md) in one of the [supported regions](#global-standard-model-availability).
 
 When your resource is created, you can [deploy](../how-to/create-resource.md#deploy-a-model) the GPT-4o audio model. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル記事の更新: GPT-4.5プレビューの追加"
}
```

### Explanation
この変更は、記事「models.md」において大幅な更新が行われました。主な変更点は、新しいモデル「GPT-4.5 Preview」のセクションが追加されたことです。このセクションには、モデルの利用可能性、地域ごとの使用可能なデータ、能力の詳細が記載されています。また、GPT-4.5模型の新機能や特長についても詳しく説明されており、ユーザーがこの新モデルにアクセスするための手続きも明記されています。

更に、他のモデルのテーブルも更新され、GPT-4oおよびオーディオモデルに関する情報が整理され、より充実した内容になっています。これにより、利用者はAzure OpenAIのモデルについての最新情報を得ることができ、特に新しく導入された機能に関して理解を深めることが可能となっています。また、プレビュー段階のモデルに関する注意事項も追加され、利用時の留意点が明示されています。

## articles/ai-services/openai/how-to/fine-tuning.md{#item-5c0e85}

<details>
<summary>Diff</summary>
````diff
@@ -123,7 +123,8 @@ curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceG
 
 #### Deleting a Provisioned Managed deployment
 
-To delete a deployment, use the [Deployments - Delete REST API(/rest/api/aiservices/accountmanagement/deployments/delete?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true) and send an HTTP DELETE to the deployment resource. Like with creating deployments, you must include the following parameters:
+To delete a deployment, use the [Deployments - Delete REST API](/rest/api/aiservices/accountmanagement/deployments/delete?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true) and send an HTTP DELETE to the deployment resource. Like with creating deployments, you must include the following parameters:
+
 
 - Azure subscription id
 - Azure resource group name
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニング手順の修正: デプロイ削除手順の更新"
}
```

### Explanation
この変更は、記事「fine-tuning.md」においてデプロイ削除手順に関する説明が更新されたものです。具体的には、デプロイメントを削除するための手順の記述が若干修正され、リンクの表記が整えられています。この修正により、読者は削除APIの使用方法をより明確に理解できるようになっています。また、削除に際して必要なパラメーターに関する情報も強調されています。全体的に、手順の明確さと整合性が向上し、ユーザーがAzure環境でのデプロイメント管理をスムーズに行えるようになっています。

## articles/ai-services/openai/includes/content-filter-configurability.md{#item-11f064}

<details>
<summary>Diff</summary>
````diff
@@ -30,4 +30,4 @@ Configurable content filters for inputs (prompts) and outputs (completions) are
 
 Content filtering configurations are created within a Resource in Azure AI Foundry portal, and can be associated with Deployments. [Learn more about configurability here](../how-to/content-filters.md).  
 
-Customers are responsible for ensuring that applications integrating Azure OpenAI comply with the [Code of Conduct](/legal/cognitive-services/openai/code-of-conduct?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext). 
\ No newline at end of file
+Customers are responsible for ensuring that applications integrating Azure OpenAI comply with the [Code of Conduct](/legal/ai-code-of-conduct?context=/azure/ai-services/openai/context/context). 
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "内容フィルタの設定に関するリンクの修正"
}
```

### Explanation
この変更は、記事「content-filter-configurability.md」において、Azure OpenAIの利用に関する注意事項のリンクが更新されています。具体的には、顧客がAzure OpenAIを統合するアプリケーションが遵守すべき「行動規範」へのリンクが、以前の文書から最新の情報に更新されました。これにより、ユーザーが正確で最新の規範情報にアクセスしやすくなり、Azure OpenAIの使用における法的および倫理的な要求事項を理解するのに役立ちます。全体として、この修正は情報の正確性と信頼性を向上させています。

## articles/ai-services/openai/index.yml{#item-0adb87}

<details>
<summary>Diff</summary>
````diff
@@ -133,7 +133,7 @@ landingContent:
         - text: Limited access
           url: /legal/cognitive-services/openai/limited-access?context=/azure/ai-services/openai/context/context
         - text: Code of conduct
-          url: /legal/cognitive-services/openai/code-of-conduct?context=/azure/ai-services/openai/context/context
+          url: /legal/ai-code-of-conduct?context=/azure/ai-services/openai/context/context
         - text: Data, privacy, and security
           url: /legal/cognitive-services/openai/data-privacy?context=/azure/ai-services/openai/context/context
         - text: Customer Copyright Commitment
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "行動規範のリンクの修正"
}
```

### Explanation
この変更は、`index.yml`ファイルにおいて、Azure OpenAIに関連する「行動規範」へのリンクが更新されたことを示しています。具体的には、古いURLが新しいURLに置き換えられており、これによりユーザーが正確で最新の行動規範へアクセスできるようになります。この修正は、情報の正確性を向上させ、ユーザーが法的および倫理的要件を適切に遵守できるようにするための重要なステップです。全体として、ドキュメント内のリンクが最新の情報に保たれることは、リーダビリティとユーザー体験の向上に寄与します。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ Azure OpenAI Service provides REST API access to OpenAI's powerful language mode
 
 ## Responsible AI
 
-At Microsoft, we're committed to the advancement of AI driven by principles that put people first. Generative models such as the ones available in Azure OpenAI have significant potential benefits, but without careful design and thoughtful mitigations, such models have the potential to generate incorrect or even harmful content. Microsoft has made significant investments to help guard against abuse and unintended harm, which includes incorporating Microsoft’s <a href="https://www.microsoft.com/ai/responsible-ai?activetab=pivot1:primaryr6" target="_blank">principles for responsible AI use</a>, adopting a [Code of Conduct](/legal/cognitive-services/openai/code-of-conduct?context=/azure/ai-services/openai/context/context) for use of the service, building [content filters](/azure/ai-services/content-safety/overview) to support customers, and providing responsible AI [information and guidance](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=image) that customers should consider when using Azure OpenAI.
+At Microsoft, we're committed to the advancement of AI driven by principles that put people first. Generative models such as the ones available in Azure OpenAI have significant potential benefits, but without careful design and thoughtful mitigations, such models have the potential to generate incorrect or even harmful content. Microsoft has made significant investments to help guard against abuse and unintended harm, which includes incorporating Microsoft’s <a href="https://www.microsoft.com/ai/responsible-ai?activetab=pivot1:primaryr6" target="_blank">principles for responsible AI use</a>, adopting a [Code of Conduct](/legal/ai-code-of-conduct?context=/azure/ai-services/openai/context/context) for use of the service, building [content filters](/azure/ai-services/content-safety/overview) to support customers, and providing responsible AI [information and guidance](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=image) that customers should consider when using Azure OpenAI.
 
 ## Get started with Azure OpenAI Service
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "行動規範のリンクの修正"
}
```

### Explanation
この変更は、`overview.md`ファイル内にあるAzure OpenAIに関する説明の一部として、行動規範へのリンクが更新されたことを示しています。具体的には、URLが以前の「コグニティブサービス」のものから新しい「AI行動規範」のものに変更されています。この修正により、より正確で関連性のある情報にリーダーがアクセスできるようになり、MicrosoftのAIの利用における責任あるガイドラインを強調しています。この更新は、ユーザーが適切な倫理的基準を理解し、遵守する手助けとなるよう設計されています。全体として、情報の透明性および正確さを向上させる重要な修正です。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 2/14/2025
+ms.date: 2/27/2025
 ms.author: mbullwin
 ---
 
@@ -62,6 +62,13 @@ The following sections provide you with a quick guide to the default quotas and
 
 [!INCLUDE [Quota](./includes/global-batch-limits.md)]
 
+### GPT-4.5 Preview global standard
+
+| Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
+|---|---|:---:|:---:|
+| `gpt-4.5` | Enterprise Tier | 50 K | 1 |
+| `gpt-4.5` | Default | 50 K | 1 |
+
 ## `o-series` rate limits
 
 > [!IMPORTANT]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4.5プレビューに関するクォータ情報の追加"
}
```

### Explanation
この変更は、`quotas-limits.md`ファイルにおいて、GPT-4.5プレビューに関する新しいクォータ情報が追加されたことを示しています。具体的には、GPT-4.5モデルに関連するグローバル標準のクォタリミットが新たに表形式で示されており、エンタープライズティアおよびデフォルトティアに対してそれぞれのトークン数とリクエスト数が明記されています。この更新により、ユーザーはGPT-4.5の利用時に適用される制限を明確に理解できるようになり、モデルの効果的な利用を促進します。また、日付の更新も行われており、最新の情報が反映されています。全体として、この修正は、ユーザーの理解を深め、サービス利用における透明性を向上させる重要な追加となっています。

## articles/ai-services/openai/references/azure-search.md{#item-32f34c}

<details>
<summary>Diff</summary>
````diff
@@ -4,8 +4,8 @@ titleSuffix: Azure OpenAI
 description: Learn how to use Azure OpenAI on your Azure Search data Python & REST API.
 manager: nitinme
 ms.service: azure-ai-openai
-ms.topic: conceptual
-ms.date: 09/20/2024
+ms.topic: reference
+ms.date: 02/27/2025
 author: aahill
 ms.author: aahi
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピックの変更と日付の更新"
}
```

### Explanation
この変更は、`azure-search.md`ファイルにおいて、ドキュメントのトピックタイプと最終更新日が更新されたことを示しています。具体的には、`ms.topic`が「概念的」から「リファレンス」に変更され、これはより技術的な、参照用の情報であることを示しています。また、最終更新日も「2024年9月20日」から「2025年2月27日」に変更され、最新の情報が反映されています。これにより、ユーザーはAzure OpenAIとAzure Searchを効果的に利用するためのリファレンス情報にアクセスしやすくなっており、情報の正確性と関連性が向上しています。全体として、これらの更新は、ドキュメントの質を向上させ、ユーザーに対して最新の情報を提供することを目的としています。

## articles/ai-services/openai/references/cosmos-db.md{#item-d6e2e5}

<details>
<summary>Diff</summary>
````diff
@@ -4,8 +4,8 @@ titleSuffix: Azure OpenAI
 description: Learn how to use Azure OpenAI on your Azure Cosmos DB data Python & REST API.
 manager: nitinme
 ms.service: azure-ai-openai
-ms.topic: conceptual
-ms.date: 09/24/2024
+ms.topic: reference
+ms.date: 02/27/2025
 author: aahill
 ms.author: aahi
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピックの変更と日付の更新"
}
```

### Explanation
この変更は、`cosmos-db.md`ファイルにおいて、ドキュメントのトピックタイプと最終更新日が更新されたことを示しています。具体的には、`ms.topic`が「概念的」から「リファレンス」に変更され、これはドキュメントがより技術的かつ参照用の情報を提供するものであることを表しています。また、最終更新日も「2024年9月24日」から「2025年2月27日」に改訂され、最新の情報が反映されています。この修正により、ユーザーはAzure OpenAIを利用するためのAzure Cosmos DBに関する具体的なリファレンス情報にアクセスしやすくなっており、情報の正確性と関連性が向上しています。全体として、これらの更新はドキュメントの質を向上させ、ユーザーに対して最新の内容を提供することを目的としています。

## articles/ai-services/openai/references/elasticsearch.md{#item-bb82ea}

<details>
<summary>Diff</summary>
````diff
@@ -4,8 +4,8 @@ titleSuffix: Azure OpenAI
 description: Learn how to use Azure OpenAI on your Elasticsearch data Python & REST API.
 manager: nitinme
 ms.service: azure-ai-openai
-ms.topic: conceptual
-ms.date: 01/28/2025
+ms.topic: reference
+ms.date: 02/27/2025
 author: aahill
 ms.author: aahi
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピックの変更と日付の更新"
}
```

### Explanation
この変更は、`elasticsearch.md`ファイルにおいて、ドキュメントのトピックタイプと最終更新日が更新されたことを示しています。具体的には、`ms.topic`が「概念的」から「リファレンス」に変更され、これはドキュメントがより技術的な情報を提供することを示しています。また、最終更新日も「2025年1月28日」から「2025年2月27日」に変更され、最新の情報が反映されています。この修正により、ユーザーはAzure OpenAIを利用するためのElasticsearchに関する具体的なリファレンス情報にアクセスしやすくなり、情報の正確性と関連性が向上しています。全体として、これらの更新はドキュメントの質を向上させ、ユーザーに対して最新の内容を提供することを目的としています。

## articles/ai-services/openai/references/mongo-db.md{#item-7516e1}

<details>
<summary>Diff</summary>
````diff
@@ -4,8 +4,8 @@ titleSuffix: Azure OpenAI
 description: Learn how to use Azure OpenAI on your Mongo DB Atlas data with Python & REST API.
 manager: nitinme
 ms.service: azure-ai-openai
-ms.topic: conceptual
-ms.date: 10/25/2024
+ms.topic: reference
+ms.date: 02/27/2025
 author: aahill
 ms.author: aahi
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピックの変更と日付の更新"
}
```

### Explanation
この変更は、`mongo-db.md`ファイルにおいて、ドキュメントのトピックタイプと最終更新日が更新されたことを示しています。具体的には、`ms.topic`が「概念的」から「リファレンス」に変更されており、これにより、ドキュメントがAzure OpenAIを使用するためのMongo DB Atlasに関する具体的な参照情報を提供するものであることが明示されています。また、最終更新日も「2024年10月25日」から「2025年2月27日」に更新され、最新の情報が反映されています。この修正は、ユーザーがより関連性の高い情報にアクセスできるようにし、ドキュメントの信頼性と質を向上させることを目的としています。全体として、これらの更新は、読者に対する内容の明確さや有用性を高めています。

## articles/ai-services/openai/references/on-your-data.md{#item-c35b1e}

<details>
<summary>Diff</summary>
````diff
@@ -4,8 +4,8 @@ titleSuffix: Azure OpenAI
 description: Learn how to use Azure OpenAI On Your Data Python & REST API.
 manager: nitinme
 ms.service: azure-ai-openai
-ms.topic: conceptual
-ms.date: 07/18/2024
+ms.topic: reference
+ms.date: 02/27/2025
 author: aahill
 ms.author: aahi
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピックの変更と日付の更新"
}
```

### Explanation
この変更は、`on-your-data.md`ファイルにおいて、ドキュメントのトピックタイプおよび最終更新日が変更されたことを示しています。具体的には、`ms.topic`が「概念的」から「リファレンス」に変更されており、このドキュメントがAzure OpenAIを使用してデータに関する具体的なリファレンス情報を提供することを示しています。さらに、最終更新日も「2024年7月18日」から「2025年2月27日」に変更され、最新の情報が反映されています。この修正は、ユーザーが利用できる情報の正確性と関連性を向上させることを目的としており、ドキュメントの信頼性を高めるための重要なアップデートと言えます。全体として、これらの変更によって、読者はAzure OpenAIに関連するデータに対する適切な参考情報を得やすくなります。

## articles/ai-services/openai/references/pinecone.md{#item-4d8746}

<details>
<summary>Diff</summary>
````diff
@@ -4,8 +4,8 @@ titleSuffix: Azure OpenAI
 description: Learn how to use Azure OpenAI on your Pinecone data Python & REST API.
 manager: nitinme
 ms.service: azure-ai-openai
-ms.topic: conceptual
-ms.date: 01/28/2025
+ms.topic: reference
+ms.date: 02/27/2025
 author: aahill
 ms.author: aahi
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピックの変更と日付の更新"
}
```

### Explanation
この変更は、`pinecone.md`ファイルにおいて、ドキュメントのトピックタイプと最終更新日が更新されたことを示しています。具体的には、`ms.topic`が「概念的」から「リファレンス」に変更されており、このファイルがAzure OpenAIを使用してPineconeデータに関する具体的なリファレンス情報を提供するものであることを示しています。また、最終更新日も「2025年1月28日」から「2025年2月27日」に変更され、最新の情報が反映されています。この変更は、ユーザーがより正確で関連性の高い情報にアクセスできるようにし、ドキュメントの質と信頼性を向上させることを目的としています。全体として、これらの更新によって、読者はAzure OpenAIにおけるPineconeデータの利用に関する正しい参考情報を得やすくなります。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -171,9 +171,9 @@ items:
       - name: Fine-tuning your model
         href: ./how-to/fine-tuning.md
         displayName: finetuning 
-      - name: Function calling
+      - name: Tool calling
         href: ./how-to/fine-tuning-functions.md
-        displayName: fine-tuning, finetuning
+        displayName: fine-tuning, finetuning, function calling
       - name: Weights & Biases integration (preview)
         href: ./how-to/weights-and-biases-integration.md
   - name: Stored completions
@@ -270,7 +270,7 @@ items:
     - name: Limited access
       href: /legal/cognitive-services/openai/limited-access?context=/azure/ai-services/openai/context/context
     - name: Code of conduct
-      href: /legal/cognitive-services/openai/code-of-conduct?context=/azure/ai-services/openai/context/context
+      href: /legal/ai-code-of-conduct?context=/azure/ai-services/openai/context/context
     - name: Data, privacy, and security
       href: /legal/cognitive-services/openai/data-privacy?context=/azure/ai-services/openai/context/context
     - name: Customer Copyright Commitment
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "項目名の変更とリンクの修正"
}
```

### Explanation
この変更は、`toc.yml`ファイルにおいて、ナビゲーションメニューのいくつかの項目名とそのリンクが更新されたことを示しています。具体的には、「Function calling」という項目名が「Tool calling」に変更され、関連するリンクも調整されています。また、表示名も「fine-tuning, finetuning」から「fine-tuning, finetuning, function calling」に変更され、新たに「function calling」が加えられています。

さらに、法的関連の「Code of conduct」という項目のリンクが修正され、以前は「/legal/cognitive-services/openai/code-of-conduct」に向けられていたのが「/legal/ai-code-of-conduct」に変更されています。これにより、読者が関連情報にアクセスしやすくなることが期待されます。

全体として、これらの変更はドキュメントの構造をより整理されたものにし、ユーザーにとっての利便性を向上させることを目的としています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: whats-new
-ms.date: 2/19/2025
+ms.date: 2/27/2025
 recommendations: false
 ---
 
@@ -21,9 +21,23 @@ This article provides a summary of the latest releases and major documentation u
 
 ## February 2025
 
+### GPT-4.5 Preview
+
+The latest GPT model that excels at diverse text and image tasks is now available on Azure OpenAI.
+
+**For access to `gpt-4.5-preview` registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who have access to other limited access models will still need to request access for this model.
+
+Request access: [GPT-4.5-preview limited access model application](https://aka.ms/oai/gptaccess)
+
+For more information on model capabilities, and region availability see the [models documentation](./concepts/models.md#gpt-45-preview).
+
+### Stored completions API
+
+[Stored completions](./how-to/stored-completions.md#stored-completions-api) allow you to capture the conversation history from chat completions sessions to use as datasets for evaluations and fine-tuning.
+
 ### o3-mini datazone standard deployments
 
-`o3-mini` is now available for global standard, and data zone standard deployments for registered limited access customers. Data standard deployment regions are currently United States regions only.
+`o3-mini` is now available for global standard, and data zone standard deployments for registered limited access customers.
 
 For more information, see our [reasoning model guide](./how-to/reasoning.md). 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能の追加と日付の更新"
}
```

### Explanation
この変更は、`whats-new.md`ファイルにおいて、2025年2月の新機能に関する情報が追加され、最終更新日が更新されたことを示しています。具体的には、GPT-4.5プレビュー版に関する詳細が新たに追加されており、多様なテキストや画像タスクに優れた性能を持つ最新のGPTモデルがAzure OpenAIで利用可能になったことが記されています。

また、このプレビュー版にアクセスするためには登録が必要で、Microsoftの適格基準に基づいてアクセスが付与されることが説明されています。ユーザーは「GPT-4.5-preview限定アクセスモデル申請」リンクを通じてアクセスをリクエストすることができます。

さらに、「Stored completions API」のセクションも新たに追加され、会話履歴をキャプチャして評価やファインチューニングのためのデータセットとして使用できることが説明されています。

最後に、`ms.date`が2025年2月19日から2025年2月27日に更新され、最新の情報が反映されたことを示しています。これらの変更により、ユーザーは新機能やAPIの利用方法に関する最新情報を容易に把握できるようになります。


