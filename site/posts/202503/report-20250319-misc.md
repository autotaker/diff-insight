---
date: '2025-03-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b32e527...MicrosoftDocs:144811f
summary: このドキュメントは、Azure AI Languageサービスの最新機能と改善点に関する更新を反映しています。2025年1月から3月にかけての重要なリリースとして、個人情報検出サービスの精度向上や抽象的要約機能の強化が挙げられます。また、.NET
  SDKの更新により新機能が追加され、一部のカスタム機能が廃止されました。全体として、これらの変更はユーザーの体験向上を目指したものであり、特に個人情報保護やビジネスインテリジェンス分野での応用が期待されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b32e527...MicrosoftDocs:144811f){target="_blank"}

# Highlights
このドキュメントの差分は、Azure AI Languageサービスに関する最新の機能と改善点についての記事を更新したものであり、2025年1月から3月の間の重要なリリースを反映しています。

## New features
- **Conversational PII detection service**: 2025年3月に、個人情報検出の精度が向上したGAモデルが実施されました。例えば、クレジットカード番号や社会保障番号などの検出において、より高い精度を実現しています。
- **Abstract summarization**: 2025年2月には、Phi-3.5-miniを採用した文書とテキストの抽象的要約機能が強化されました。また、Azure AI Foundryでは新たなスキルが追加されました。

## Breaking changes
- **.NET SDK update**: 2025年1月に.NET SDKが更新され、感情分析やエンティティ認識などの複数の機能をサポートしました。一部のカスタム機能はユーザーのフィードバックを基に廃止され、ジェネレーティブAIを活用した新しいカスタムモデル機能に重点を置くことに決定しました。

## Other updates
この更新は、Azure AIサービスの機能向上及びユーザー体験の向上を目指したものです。

# Insights
この変更の背景には、Azure AI Platformが最新技術に対応し続け、ユーザーにより優れたサービスを提供するという目的があります。3月のPII検出サービスにおける精度向上は、個人情報保護の観点から特に重要で、特に高精度が求められる金融取引や公共サービスの分野での活用が期待されます。また、2月の抽象的要約の強化により、より詳細な文書データから果たされる洞察は、ビジネスインテリジェンスやデータ分析の分野での応用が可能になり、意思決定を支える重要な技術となります。

1月の時点での.NET SDKの更新によって、開発者は最新の機能を用いたアプリケーションを構築しやすくなり、使いやすいSDKによる開発効率の向上が期待できます。一方で一部のカスタム機能の廃止は、一部のユーザーに影響を与える可能性があるため、移行期間中のサポート提供の質がカギとなります。この変更は、AI技術の発展に伴い、ジェネレーティブAIという新たなトレンドに迅速に対応し、技術革新を先取りしようとするものです。また、ユーザーからのフィードバックを重視し、それをサービス改善に活かす姿勢は、ユーザー志向の開発姿勢を示しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [whats-new.md](#item-69b272) | minor update | 最新のAIサービスアップデート (2025年3月、2月、1月) | Azure AI Language | modified | 34 | 1 | 35 | 


# Modified Contents
## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -15,9 +15,42 @@ ms.author: jboback
 
 Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent developments, this article provides you with information about new releases and features.
 
+## March 2025
+
+* Our [Conversational PII redaction](personally-identifiable-information/how-to/redact-conversation-pii.md?tabs=client-libraries) service is now powered by an upgraded GA model. This updated 2024-02-01 version includes improved quality and accuracy in Credit card number entities and numeric identification entities, such as Social Security numbers, driver’s license numbers, policy numbers, Medicare Beneficiary Identifiers, and Financial account numbers.
+
+## February 2025
+
+* Document and text abstractive summarization is now powered by fine-tuned Phi-3.5-mini! Check out the [Announcing Blog](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/exciting-update-abstractive-summarization-in-azure-ai-language-now-powered-by-ph/4369025) for more information.
+* More skills are available in [Azure AI Foundry](https://ai.azure.com): Extract key phrase, Extract named entities, Analyze sentiment and Detect language. More skills are yet to come.
+
+## January 2025
+
+* .NET SDK for Azure AI Language text analytics, [Azure.AI.Language.Text 1.0.0-beta.2](https://www.nuget.org/packages/Azure.AI.Language.Text/1.0.0-beta.2#readme-body-tab), is now available. This client library supports the latest REST API version, 2024-11-01 and 2024-11-15-preview, for the following features:
+    * Language detection
+    * Sentiment analysis
+    * Key phrase extraction
+    * Named entity recognition (NER)
+    * Personally identifiable information (PII) entity recognition
+    * Entity linking
+    * Text analytics for health 
+    * Custom named entity recognition (Custom NER)
+    * Custom text classification
+    * Extractive text summarization
+    * Abstractive text summarization
+* Custom sentiment analysis (preview), custom text analytics for health (preview) and custom summarization (preview) were retired on January 10th, 2025, as Azure AI features are constantly evaluated based on customer demand and feedback. Based on the customers’ feedback of these preview features, Microsoft has decided to retire this feature and prioritize new custom model features leveraging the power of generative AI to better serve customers’ needs. 
+
 ## November 2024
 
-* [Native document support](native-document-support/overview.md) is now available in public preview `2024-11-15-preview` without gated preview limitations.
+* Azure AI Language is moving to [Azure AI Foundry](https://ai.azure.com). These skills are now available in AI Foundry playground: Extract health information, Extract PII from conversation, Extract PII from text, Summarize text, Summarize conversation, Summarize for call center. More skills follow.  
+* Runtime Container for Conversational Language Understanding (CLU) is available for on-premise connection.
+* Both our [Text PII redaction service](personally-identifiable-information/overview.md?tabs=text-pii) and our Conversational PII service preview API (version 2024-11-15-preview) now support the option to mask detected sensitive entities with a label beyond just redaction characters. Customers can specify if personal data content such as names and phone numbers, that is, "John Doe received a call from 424-878-9192", are masked with a redaction character, that is, "******** received a call from ************", or masked with an entity label, that is, "`PERSON_1` received a call from `PHONENUMBER_1`". More on how to specify the redaction policy style for your outputs can be found in our [how-to guides](personally-identifiable-information/how-to-call.md). 
+* Native document support gating is removed with the latest API version, 2024-11-15-preview, allowing customers to access native document support for PII redaction and summarization. Key updates in this version include:
+    * Increased Maximum File Size Limits (from 1 MB to 10 MB). 
+    * Enhanced PII Redaction Customization: Customers can now specify whether they want only the redacted document or both the redacted document and a JSON file containing the detected entities.
+* Language detection is a preconfigured feature that can detect the language a document is written in and returns a language code for a wide range of languages, variants, dialects, and some regional/cultural languages. Today the general availability of [scription detection capability](language-detection/how-to/call-api.md#script-name-and-script-code), and 16 more languages support, which adds up to [139 total supported languages](language-detection/language-support.md) is announced.
+* [Named Entity Recognition service](named-entity-recognition/overview.md), [Entity Resolution](named-entity-recognition/concepts/entity-resolutions.md) was upgraded to the Entity Metadata starting in API version 2023-04-15-preview. If you're calling the preview version of the API equal or newer than 2023-04-15-preview, check out the Entity Metadata article to use the resolution feature. The service now supports the ability to specify a list of entity tags to be included into the response or excluded from the response. If a piece of text is classified as more than one entity type, the overlapPolicy parameter allows customers to specify how the service will handle the overlap. The inferenceOptions parameter allows for users to adjust the inference, such as excluding the detected entity values from being normalized and included in the metadata. Along with these optional input parameters  we support an updated output structure (with new fields tags, type, and metadata) to ensure enhanced user customization and deeper analysis Learn more on our documentation.
+* Text analytics for health (TA4H) is a preconfigured feature that extracts and labels relevant medical information from unstructured texts such as doctor's notes, discharge summaries, clinical documents, and electronic health records. Today, we released support for Fast Healthcare Interoperability Resources (FHIR) structuring and temporal [assertion detection](text-analytics-for-health/concepts/assertion-detection.md) in the Generally Available API.  
 
 ## October 2024
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新のAIサービスアップデート (2025年3月、2月、1月) | Azure AI Language"
}
```

### Explanation
この変更は、Azure AI Languageに関する最新のリリースと機能を文書化した内容を更新するもので、主に2025年1月から3月の新機能と改善点が追加されています。主な更新内容は以下の通りです：

- **2025年3月:** Conversational PII赤外線サービスが改良されたGAモデルで稼働開始し、クレジットカード番号や社会保障番号などの情報の精度が向上しました。
- **2025年2月:** 文書とテキストの抽象的要約がPhi-3.5-miniで強化され、Azure AI Foundryでの新しいスキルが追加されました。
- **2025年1月:** .NET SDKが最新版に更新され、複数の機能（感情分析、エンティティ認識など）をサポートしています。また、カスタム機能のいくつかがユーザーからのフィードバックを受けて廃止され、ジェネレーティブAIを活用した新しいカスタムモデル機能に重点が置かれることが決定されました。

この更新は、AIサービスの機能強化とユーザー体験の向上に向けた継続的な取り組みを示しています。


