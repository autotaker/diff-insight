---
date: '2025-11-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f0d677f...MicrosoftDocs:886d965
summary: このコードの変更は、主にドキュメントの更新に関するもので、いくつかの日付の更新や内容の明確化、新機能に関する情報の追加が行われています。「What's
  New in Azure Language」ドキュメントには新しいサマリーモデルと拡張されたNLPツールに関する情報が追加され、特に破壊的な変更はありませんでした。また、モデルライフサイクルに関する日付の変更やテーブル整形の更新、REST
  APIクイックスタートの具体例修正、クイックスタートドキュメントの日付更新も行われました。これらの変更は、Azure AIのLanguage Serviceに関する最新の情報を反映し、ユーザーに使いやすい情報を提供することを目的としています。全体として、ドキュメントの整合性が強化され、ユーザビリティも向上しました。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f0d677f...MicrosoftDocs:886d965){target="_blank"}

<format>
# ハイライト
このコードの変更は、主にドキュメントの更新に関するものです。特にいくつかの日付の更新、内容の明確化、新機能に関する情報の追加が行われています。

## 新機能
- 「What's New in Azure Language」ドキュメントにて、新しくリリースされるサマリーモデルと拡張されたNLPツールに関する情報が追加されました。

## 破壊的変更
- 破壊的な変更は特にありません。すべての更新はドキュメントに関する情報の更新で、機能そのものには影響を与えません。

## その他の更新
- モデルライフサイクルに関する日付とテーブル整形の変更
- REST APIクイックスタートのバージョン更新による具体例の修正
- 「クイックスタート」ドキュメントの日付更新

# インサイト
この一連の変更は、Azure AIのLanguage Serviceのドキュメントにおいて最新の情報を適切に反映するためのもので、新旧の日付やバージョンの更新を通じてユーザーに最新のデータを提供するものです。具体的には、モデルライフサイクルの部分ではコンテンツの整形やノートの追加が行われ、情報がより見やすくなっています。また、「REST API」に関しては、コマンド例の更新が加えられ、利用者がより正確にAPIを使用できるように改善されています。

一方、「What's New in Azure Language」では、しっかりと新機能の情報が追加されていることで、技術者やエンジニアは新しいサマリーモデルをどのように自分のプロジェクトに組み込むか考える際の基礎情報として役立てることができます。このドキュメントの更新は、最新のAI技術を確実に利用できるようにするための大事な一歩だと言えるでしょう。

全体として、ドキュメントの整合性が強化され、ユーザビリティも向上しました。これにより、利用者はより簡単に新機能の恩恵を受けることができ、技術的な課題を早期に解決する手助けとなります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-lifecycle.md](#item-417f3f) | minor update | モデルライフサイクルのドキュメント更新 | modified | 7 | 5 | 12 | 
| [rest-api.md](#item-882887) | minor update | REST API クイックスタートの更新 | modified | 14 | 17 | 31 | 
| [quickstart.md](#item-bff856) | minor update | クイックスタートの日付更新 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-69b272) | minor update | Azure Languageの新機能と更新情報 | modified | 26 | 20 | 46 | 


# Modified Contents
## articles/ai-services/language-service/concepts/model-lifecycle.md{#item-417f3f}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 08/07/2025
+ms.date: 11/05/2025
 ms.author: lajanuar
 ---
 
@@ -24,7 +24,7 @@ By default, all API requests use the latest Generally Available (GA) model.
 
 #### Choose the model-version used on your data
 
-We recommend using the `latest` model version to utilize the latest and highest quality models. As our models improve, it's possible that some of your model results may change. Model versions may be deprecated, so we no longer accept specified GA model versions in your implementation. 
+We recommend using the `latest` model version to utilize the latest and highest quality models. As our models improve, it's possible that some of your model results may change. Model versions may be deprecated, so we no longer accept specified GA model versions in your implementation.
 
 Preview models used for preview features don't maintain a minimum retirement period and may be deprecated at any time.
 
@@ -33,6 +33,8 @@ By default, API and SDK requests use the latest Generally Available model. To us
 > [!NOTE]
 > If you're using a model version that isn't listed in the table, then it was subjected to the expiration policy.
 
+## Model versions
+
 Use the following table to find which model versions support each feature:
 
 | Feature | Supported generally available (GA) version | Latest supported preview versions | Other supported verision |
@@ -46,14 +48,14 @@ Use the following table to find which model versions support each feature:
 | Question answering | `latest` |  |  |
 | Text Analytics for health | `latest` | `2023-04-15-preview` |  |
 | Key phrase extraction | `latest` |  |  |
-| Summarization | `latest` | `2025-06-10-preview` (only available for `issue` and `resolution` aspects in conversation summarization) |  |
+| Summarization | `latest`. **Note**: `2025-06-10` is only available for `issue` and `resolution` aspects in conversation summarization.  | |  |
 
 
 ## Custom features
 
 ### Expiration timeline
 
-For custom features, there are two key parts of the AI implementation: training and deployment. New configurations are released regularly with regular AI improvements, so older and less accurate configurations are retired. 
+For custom features, there are two key parts of the AI implementation: training and deployment. New configurations are released regularly with regular AI improvements, so older and less accurate configurations are retired.
 
 Use the following table to find which model versions support each feature:
 
@@ -66,7 +68,7 @@ Use the following table to find which model versions support each feature:
 
 ** *For latest training configuration versions, the posted expiration dates are subject to availability of a newer model version. If no newer model versions are available, the expiration date may be extended.*
 
-Training configurations are typically available for **six months** after its release. If you assigned a trained configuration to a deployment, this deployment expires after **twelve months** from the training config expiration. If your models are about to expire, you can retrain and redeploy your models with the latest training configuration version. 
+Training configurations are typically available for **six months** after its release. If you assigned a trained configuration to a deployment, this deployment expires after **twelve months** from the training config expiration. If your models are about to expire, you can retrain and redeploy your models with the latest training configuration version.
 
 > [!TIP]
 > We recommend that you use the latest supported configuration version.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルのドキュメント更新"
}
```

### Explanation
この変更は、「モデルライフサイクル」ドキュメントに対するマイナーな更新を示しています。主に、日付が更新されたこと（2025年08月07日から2025年11月05日への変更）や、情報の明確化のためにコンテンツが少し修正されています。また、モデルバージョンに関するテーブルの整形とノートが追加され、カスタム機能の説明にもわずかな変化が見られます。全体として、これらの変更はドキュメントの正確性と明確性を改善することを目的としています。

## articles/ai-services/language-service/summarization/includes/quickstarts/rest-api.md{#item-882887}

<details>
<summary>Diff</summary>
````diff
@@ -2,11 +2,8 @@
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.custom:
-  - build-2024
-  - ignite-2024
 ms.topic: include
-ms.date: 06/30/2025
+ms.date: 11/05/2025
 ms.author: lajanuar
 ---
 
@@ -18,7 +15,7 @@ ms.author: lajanuar
 
 ---
 
-Use this quickstart to send text summarization requests using the REST API. In the following example, you will use cURL to summarize documents or text-based customer service conversations.
+Use this quickstart to send text summarization requests using the [REST API](/rest/api/language/analyze-documents/analyze-documents-submit-job/analyze-documents-submit-job?view=rest-language-analyze-documents-2024-11-15-preview&preserve-view=true&tabs=HTTP). In the following example, you will use cURL to summarize documents or text-based customer service conversations.
 
 [!INCLUDE [Use Language Studio](../use-language-studio.md)]
 
@@ -71,7 +68,7 @@ The following example will get you started with text extractive summarization:
 1. Copy the command below into a text editor. The BASH example uses the `\` line continuation character. If your console or terminal uses a different line continuation character, use that character instead.
 
 ```bash
-curl -i -X POST $LANGUAGE_ENDPOINT/language/analyze-text/jobs?api-version=2023-04-01 \
+curl -i -X POST $LANGUAGE_ENDPOINT/language/analyze-text/jobs?api-version=2024-11-15-preview \
 -H "Content-Type: application/json" \
 -H "Ocp-Apim-Subscription-Key: $LANGUAGE_KEY" \
 -d \
@@ -83,7 +80,7 @@ curl -i -X POST $LANGUAGE_ENDPOINT/language/analyze-text/jobs?api-version=2023-0
       {
         "id": "1",
         "language": "en",
-        "text": "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there’s magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code will enable us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pre-trained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
+        "text": "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code will enable us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pre-trained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
       }
     ]
   },
@@ -107,13 +104,13 @@ curl -i -X POST $LANGUAGE_ENDPOINT/language/analyze-text/jobs?api-version=2023-0
 4. Get the `operation-location` from the response header. The value will look similar to the following URL:
 
 ```http
-https://<your-language-resource-endpoint>/language/analyze-text/jobs/12345678-1234-1234-1234-12345678?api-version=2023-04-01
+https://<your-language-resource-endpoint>/language/analyze-text/jobs/12345678-1234-1234-1234-12345678?api-version=2024-11-15-preview
 ```
 
 5. To get the results of the request, use the following cURL command. Be sure to replace `<my-job-id>` with the numerical ID value you received from the previous `operation-location` response header:
 
 ```bash
-curl -X GET $LANGUAGE_ENDPOINT/language/analyze-text/jobs/<my-job-id>?api-version=2023-04-01 \
+curl -X GET $LANGUAGE_ENDPOINT/language/analyze-text/jobs/<my-job-id>?api-version=2024-11-15-preview \
 -H "Content-Type: application/json" \
 -H "Ocp-Apim-Subscription-Key: $LANGUAGE_KEY"
 ```
@@ -158,7 +155,7 @@ curl -X GET $LANGUAGE_ENDPOINT/language/analyze-text/jobs/<my-job-id>?api-versio
                                     "length": 192
                                 },
                                 {
-                                    "text": "At the intersection of all three, there’s magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better.",
+                                    "text": "At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better.",
                                     "rankScore": 0.63,
                                     "offset": 517,
                                     "length": 203
@@ -203,7 +200,7 @@ The following example will get you started with conversation issue and resolutio
 1. Copy the command below into a text editor. The BASH example uses the `\` line continuation character. If your console or terminal uses a different line continuation character, use that character instead.
 
 ```bash
-curl -i -X POST $LANGUAGE_ENDPOINT/language/analyze-conversations/jobs?api-version=2023-04-01 \
+curl -i -X POST $LANGUAGE_ENDPOINT/language/analyze-conversations/jobs?api-version=2024-11-15-preview \
 -H "Content-Type: application/json" \
 -H "Ocp-Apim-Subscription-Key: $LANGUAGE_KEY" \
 -d \
@@ -215,19 +212,19 @@ curl -i -X POST $LANGUAGE_ENDPOINT/language/analyze-conversations/jobs?api-versi
       {
         "conversationItems": [
           {
-            "text": "Hello, you’re chatting with Rene. How may I help you?",
+            "text": "Hello, you're chatting with Rene. How may I help you?",
             "id": "1",
             "role": "Agent",
             "participantId": "Agent_1"
           },
           {
-            "text": "Hi, I tried to set up wifi connection for Smart Brew 300 espresso machine, but it didn’t work.",
+            "text": "Hi, I tried to set up wifi connection for Smart Brew 300 espresso machine, but it didn't work.",
             "id": "2",
             "role": "Customer",
             "participantId": "Customer_1"
           },
           {
-            "text": "I’m sorry to hear that. Let’s see what we can do to fix this issue. Could you please try the following steps for me? First, could you push the wifi connection button, hold for 3 seconds, then let me know if the power light is slowly blinking on and off every second?",
+            "text": "I'm sorry to hear that. Let's see what we can do to fix this issue. Could you please try the following steps for me? First, could you push the wifi connection button, hold for 3 seconds, then let me know if the power light is slowly blinking on and off every second?",
             "id": "3",
             "role": "Agent",
             "participantId": "Agent_1"
@@ -251,7 +248,7 @@ curl -i -X POST $LANGUAGE_ENDPOINT/language/analyze-conversations/jobs?api-versi
             "participantId": "Customer_1"
           },
           {
-            "text": "I’m very sorry to hear that. Let me see if there’s another way to fix the issue. Please hold on for a minute.",
+            "text": "I'm very sorry to hear that. Let me see if there's another way to fix the issue. Please hold on for a minute.",
             "id": "7",
             "role": "Agent",
             "participantId": "Agent_1"
@@ -292,13 +289,13 @@ Only the `resolution` aspect supports sentenceCount. If you do not specify the `
 4. Get the `operation-location` from the response header. The value will look similar to the following URL:
 
 ```http
-https://<your-language-resource-endpoint>/language/analyze-conversations/jobs/12345678-1234-1234-1234-12345678?api-version=2023-04-01
+https://<your-language-resource-endpoint>/language/analyze-conversations/jobs/12345678-1234-1234-1234-12345678?api-version=2024-11-15-preview
 ```
 
 5. To get the results of the request, use the following cURL command. Be sure to replace `<my-job-id>` with the numerical ID value you received from the previous `operation-location` response header:
 
 ```bash
-curl -X GET $LANGUAGE_ENDPOINT/language/analyze-conversations/jobs/<my-job-id>?api-version=2023-04-01 \
+curl -X GET $LANGUAGE_ENDPOINT/language/analyze-conversations/jobs/<my-job-id>?api-version=2024-11-15-preview \
 -H "Content-Type: application/json" \
 -H "Ocp-Apim-Subscription-Key: $LANGUAGE_KEY"
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST API クイックスタートの更新"
}
```

### Explanation
この変更は、「REST API」クイックスタート関連のドキュメントに対するマイナーな更新を示しています。主な変更点は、APIのバージョンが2023年4月1日から2024年11月15日に更新されたことに伴ういくつかの具体的なコマンド例の修正です。また、ドキュメント内でのリンクの清書や、テキストの整形が行われており、より明確に情報が伝わるようになっています。全体として、APIの使用方法を明確にし、最新の情報を反映させるための改良が加えられています。

## articles/ai-services/language-service/summarization/quickstart.md{#item-bff856}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 09/15/2025
+ms.date: 11/05/2025
 ms.author: lajanuar
 ms.devlang: csharp
 # ms.devlang: csharp, java, javascript, python
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートの日付更新"
}
```

### Explanation
この変更は、「クイックスタート」ドキュメントの日付に関するマイナーな更新を示しています。具体的には、更新前の日付が2025年9月15日から2025年11月5日に変更されました。この更新により、ドキュメントの内容が最新のリリースに反映され、利用者に正確な情報を提供することを目的としています。全体として、ドキュメントの整合性を保つための重要な変更です。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -1,32 +1,38 @@
 ---
-title: What's new in Azure AI Language?
-titleSuffix: Azure AI services
-description: Find out about new releases and features for the Azure AI Language.
+title: What's new in Azure Language in Foundry Tools?
+titleSuffix: Azure AI Foundry Tools
+description: Find out about new releases and features for the Azure Language.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: whats-new
-ms.date: 09/04/2025
+ms.date: 11/05/2025
 ms.author: lajanuar
 ---
 
-# What's new in Azure AI Language?
+# What's new in Azure Language in Foundry Tools?
 
-Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up to date with release notes, feature enhancements, and our newest documentation.
+Azure Language in Foundry Tools is updated on an ongoing basis. Bookmark this page to stay up to date with release notes, feature enhancements, and our newest documentation.
+
+## October 2025
+
+* **Summarization model 2025-06-10 generally available**. The [Summarization model](summarization/overview.md) version 2025-06-10 is now generally available. This model is fine-tuned using the [Phi open model family](https://azure.microsoft.com/products/phi), delivering enhanced performance for Issue and Resolution summary generation.
+
+* **Expanded Azure Language MCP server capabilities**. The Model Context Protocol (MCP) server for Azure Language now provides eight additional NLP tools: [Named Entity Recognition](named-entity-recognition/overview.md), [Text Analytics for health](text-analytics-for-health/overview.md), [Conversational Language Understanding](conversational-language-understanding/overview.md), [Custom Question Answering](question-answering/overview.md), [Language Detection](language-detection/overview.md), [Sentiment Analysis](sentiment-opinion-mining/overview.md), [Summarization](summarization/overview.md), and [Key Phrase Extraction](key-phrase-extraction/overview.md). These tools complement the existing PII Detection capability.
 
 ## September 2025
 
-**Introducing CQA deploy-to-agent**. Custom Question Answering (CQA) projects can now be [deployed as intelligent agents](question-answering/how-to/deploy-agent.md) directly within the Azure AI Foundry playground through a streamlined deployment experience. 
-  * This feature enables users to transform fine-tuned CQA knowledge bases into production-ready agents with minimal configuration steps. 
+**Introducing CQA deploy-to-agent**. Custom Question Answering (CQA) projects can now be [deployed as intelligent agents](question-answering/how-to/deploy-agent.md) directly within the Azure AI Foundry playground through a streamlined deployment experience.
+  * This feature enables users to transform fine-tuned CQA knowledge bases into production-ready agents with minimal configuration steps.
   * The deployment process provides parity with CLU workflows and accelerates the agent development timeline within the unified Foundry environment.
 
-**Custom Named Entity Recognition (NER) capabilities integrated into Language Playground**. Users can now access a testing playground for custom Named Entity Recognition (NER) within Azure AI Foundry. 
+**Custom Named Entity Recognition (NER) capabilities integrated into Language Playground**. Users can now access a testing playground for custom Named Entity Recognition (NER) within Azure AI Foundry.
   * This interactive interface allows training, deployment, testing, and fine-tuning for custom models while experimenting with custom NER capabilities in real-time.
   * The playground accelerates the onboarding process and provides enhanced debugging capabilities for custom NER implementations. For more information, *see* [Quickstart: Custom named entity recognition](custom-named-entity-recognition/quickstart.md).
 
 **New Python SDKs**. The new Python SDKs [**azure-ai-textanalytics 6.0.0b1**](https://pypi.org/project/azure-ai-textanalytics/6.0.0b1/) and [**azure-ai-textanalytics-authoring 1.0.0b1**](https://pypi.org/project/azure-ai-textanalytics-authoring/1.0.0b1/) are now available:
 
-   * **azure-ai-textanalytics 6.0.0b1** offers runtime APIs that enable users to utilize various prebuilt features within Azure AI Language, such as sentiment analysis, named entity recognition (NER), language detection, key phrase extraction, text PII detection, Text Analytics for health, and document summarization.<br><br>Additionally, the SDK can be used to access inference APIs for custom NER and text classification models. This release supports the latest `2025-05-15-preview` API, and previous versions. The `2025-05-15-preview` API introduces several new capabilities:
+   * **azure-ai-textanalytics 6.0.0b1** offers runtime APIs that enable users to utilize various prebuilt features within Azure Language, such as sentiment analysis, named entity recognition (NER), language detection, key phrase extraction, text PII detection, Text Analytics for health, and document summarization.<br><br>Additionally, the SDK can be used to access inference APIs for custom NER and text classification models. This release supports the latest `2025-05-15-preview` API, and previous versions. The `2025-05-15-preview` API introduces several new capabilities:
 
       * Added support for new entity types in [Named Entity Recognition (NER)](named-entity-recognition/concepts/named-entity-categories.md) and [Text PII detection](personally-identifiable-information/concepts/entity-categories.md): **DateOfBirth**, **BankAccountNumber**, **PassportNumber**, and **DriversLicenseNumber**.
 
@@ -52,7 +58,7 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 
 ## July 2025
 
- **Expanded .NET SDK support for text and conversation authoring APIs**. 
+ **Expanded .NET SDK support for text and conversation authoring APIs**.
 
   * [**Azure.AI.Language.Text.Authoring `1.0.0-beta.2`**](https://www.nuget.org/packages/Azure.AI.Language.Text.Authoring/1.0.0-beta.2) now supports project import with raw JSON string for custom NER and custom text classification.
 
@@ -81,15 +87,15 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 
 ## May 2025
 
-**2025-05-15-preview release**. The [latest API preview version](/rest/api/language/operation-groups?view=rest-language-2025-05-15-preview&preserve-view=true) includes updates for named entity recognition (NER) and PII detection:
+**2025-05-15-preview release**. The latest API preview version includes updates for named entity recognition (NER) and PII detection:
 * New entity type support for `DateOfBirth`, `BankAccountNumber`, `PassportNumber`, and `DriversLicenseNumber`.
 * Improved AI quality for `PhoneNumber` entity type.
 
-**New agent templates**. Azure AI Language now supports the following agent templates:
+**New agent templates**. Azure Language now supports the following agent templates:
 *  [Intent routing](../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md): Detects user intent and provides precise answers, ideal for deterministic intent routing, and exact question answering with human oversight.
 *   [Exact question answering](../agents/concepts/agent-catalog.md): Delivers consistent, accurate responses to high-value predefined questions through deterministic methods.
 
-**PII detection enhancements**. Azure AI Language introduces new customization and entity subtype features for PII detection:
+**PII detection enhancements**. Azure Language introduces new customization and entity subtype features for PII detection:
 *  [Customize PII detection using your own regex](personally-identifiable-information/how-to/adapt-to-domain-pii.md#customizing-pii-detection-using-your-own-regex-only-available-for-text-pii-container) (Text PII container only).
 *  [Specify values to exclude from PII output](personally-identifiable-information/how-to/adapt-to-domain-pii.md#customizing-pii-output-by-specifying-values-to-exclude).
 *  [Use entity synonyms for tailored PII detection](personally-identifiable-information/how-to/adapt-to-domain-pii.md#api-schema-for-the-entitysynonyms-parameter).
@@ -111,7 +117,7 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 
 ## March 2025
 
-* Azure AI Language resource now can be deployed to three new regions, Jio India Central, UK West, and Canada East, for the following capabilities:
+* Azure Language resource now can be deployed to three new regions, Jio India Central, UK West, and Canada East, for the following capabilities:
     * Language detection
     * Sentiment analysis
     * Key phrase extraction
@@ -132,7 +138,7 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 
 ## January 2025
 
-* .NET SDK for Azure AI Language text analytics, [Azure.AI.Language.Text 1.0.0-beta.2](https://www.nuget.org/packages/Azure.AI.Language.Text/1.0.0-beta.2#readme-body-tab), is now available. This client library supports the latest REST API version, `2024-11-01`, and `2024-11-15-preview`, for the following features:
+* .NET SDK for Azure Language text analytics, [Azure.AI.Language.Text 1.0.0-beta.2](https://www.nuget.org/packages/Azure.AI.Language.Text/1.0.0-beta.2#readme-body-tab), is now available. This client library supports the latest REST API version, `2024-11-01`, and `2024-11-15-preview`, for the following features:
     * Language detection
     * Sentiment analysis
     * Key phrase extraction
@@ -148,7 +154,7 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 
 ## November 2024
 
-* Azure AI Language is moving to [Azure AI Foundry](https://ai.azure.com/?cid=learnDocs). These skills are now available in AI Foundry playground: Extract health information, Extract PII from conversation, Extract PII from text, Summarize text, Summarize conversation, Summarize for call center. More skills follow.
+* Azure Language is moving to [Azure AI Foundry](https://ai.azure.com/?cid=learnDocs). These skills are now available in AI Foundry playground: Extract health information, Extract PII from conversation, Extract PII from text, Summarize text, Summarize conversation, Summarize for call center. More skills follow.
 * Runtime Container for Conversational Language Understanding (CLU) is available for on-premises connections.
 * Both our [Text PII redaction service](personally-identifiable-information/overview.md?tabs=text-pii) and our Conversational PII service preview API (version 2024-11-15-preview) now support the option to mask detected sensitive entities with a label beyond just redaction characters. Customers can specify if personal data content such as names and phone numbers, that is, "John Doe received a call from 424-878-9192" are masked with a redaction character, that is, "******** received a call from ************" or masked with an entity label, that is, "`PERSON_1` received a call from `PHONENUMBER_1`." More on how to specify the redaction policy style for your outputs can be found in our [how-to guides](personally-identifiable-information/how-to-call.md).
 * Native document support gating is removed with the latest API version, 2024-11-15-preview, allowing customers to access native document support for PII redaction and summarization. Key updates in this version include:
@@ -165,8 +171,8 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 ## September 2024
 
 * PII detection now has container support. See more details in the Azure Update post: [Announcing Text PII Redaction Container Release](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-text-pii-redaction-container-release/4264655).
-* Custom sentiment analysis (preview) will be retired January 10, 2025. You can transition to other custom model training services, such as custom text classification in Azure AI Language.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom sentiment analysis (preview) in Azure AI Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-sentiment-analysis-retirement).
-* Custom text analytics for health (preview) will be retired on January 10, 2025. Transition to other custom model training services, such as custom named entity recognition in Azure AI Language, by that date.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom text analytics for health (preview) in Azure AI Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-text-analytics-for-health-retirement).
+* Custom sentiment analysis (preview) will be retired January 10, 2025. You can transition to other custom model training services, such as custom text classification in Azure Language.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom sentiment analysis (preview) in Azure Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-sentiment-analysis-retirement).
+* Custom text analytics for health (preview) will be retired on January 10, 2025. Transition to other custom model training services, such as custom named entity recognition in Azure Language, by that date.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom text analytics for health (preview) in Azure Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-text-analytics-for-health-retirement).
 
 ## August 2024
 * [CLU utterance limit in a project](conversational-language-understanding/service-limits.md#data-limits) increased from 25,000 to 50,000.
@@ -447,7 +453,7 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 
 * Based on ongoing customer feedback, we increased the character limit per document for Text Analytics for health from 5,120 to 30,720.
 
-* Azure AI Language release, with support for:
+* Azure Language release, with support for:
 
   * [Question Answering (now Generally Available)](question-answering/overview.md)
   * [Sentiment Analysis and opinion mining](sentiment-opinion-mining/overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Languageの新機能と更新情報"
}
```

### Explanation
この変更は「What's New in Azure Language」ドキュメントの更新を反映しており、主に内容のタイトル変更と新機能の追加が行われました。具体的には、タイトルが「Azure AI Language」から「Azure Language in Foundry Tools」へと変更され、更新日が2025年9月4日から2025年11月5日になりました。また、2025年10月にリリースされる新しいサマリーモデルや、拡張されたNLPツールに関する情報が追加され、最新の機能やサービス向上に関する詳細が記載されています。この更新によって、ユーザーはAzure Languageに関する最新情報を把握しやすくなり、新しいリリースや機能の活用が促進されます。全体として、Markdownの整合性とユーザビリティが向上しています。


