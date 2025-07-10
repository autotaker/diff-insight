---
date: '2025-07-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2b324c3...MicrosoftDocs:d3417cf
summary: このコードの差分には、いくつかのドキュメントに対するマイナーな更新が含まれています。新機能の明示や用語の訂正、表現の一貫性向上、ナビゲーションの改善が行われました。特にエラーメッセージの訂正やモデルライフサイクルの記載が、ユーザビリティの向上に貢献しています。新たに「What's
  new」項目が追加され、最新情報が見つけやすくなったことも重要です。文書の正確性や明確さが改善され、専門用語の統一が図られることで、ユーザーはよりスムーズにサービスを利用できるようになります。全体として、これらの更新は開発者やユーザーの生産性向上に寄与するものでしょう。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2b324c3...MicrosoftDocs:d3417cf){target="_blank"}

<format>
# Highlights
このコードの差分には、いくつかのドキュメントに対するマイナーな更新が含まれており、これには新機能の明示、用語の訂正、表現の一貫性向上、およびナビゲーションの改善が含まれます。特に、エラーメッセージの訂正やモデルライフサイクルのより明確な記載がユーザビリティの向上に寄与しています。

## New features
- Azure AI言語サービスの目次に「What's new」項目が追加され、新機能やリリース情報を見つけやすくなりました。
- Whats-Newページが更新され、2025年5月および6月の新機能が追加されました。

## Breaking changes
特に懸念されるような破壊的な変更は指摘されていません。

## Other updates
- 誤字や表記の修正（例: "wit" を "with" に、"AppSerivce" を "AppService" に）。
- ドキュメントの記述を滑らかにし、情報の一貫性と明確さを高めるための更新。
- AI言語サービス目次の整理。

# Insights
この更新により、ドキュメントの正確性と明確さが大幅に改善されました。特にエラーメッセージや API の使用法に関する記載は、ユーザからのフィードバックや混乱を避けるための重要なステップです。開発者やユーザーは最新情報を効率的に得ることができ、新機能の導入により生産性の向上が期待されます。

ドキュメントの一貫性と明瞭性が強調されており、特に専門用語の統一は技術文書において非常に重要です。これにより、ユーザーはサービスを利用する際に、よりスムーズに問題を解決し、リソースを活用できるようになります。また、新しい「What's new」セクションの追加は、継続的なサービス改善を容易に追跡するための重要な改善です。このような更新により、開発者コミュニティ全体の理解と採用が促進されるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [install-run.md](#item-e32e11) | minor update | 文書インテリジェンスコンテナのインストールと実行に関するドキュメントを修正 | modified | 1 | 1 | 2 | 
| [model-lifecycle.md](#item-417f3f) | minor update | モデルライフサイクルに関するドキュメントの修正 | modified | 12 | 16 | 28 | 
| [configure-azure-resources.md](#item-a2ea5c) | minor update | Azureリソースの構成に関するドキュメントの修正 | modified | 1 | 1 | 2 | 
| [use-containers.md](#item-9dddb4) | minor update | コンテナ使用に関するドキュメントの修正 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-12f1f0) | minor update | AI言語サービスの目次の更新 | modified | 3 | 3 | 6 | 
| [whats-new.md](#item-69b272) | minor update | Azure AI言語サービスの新機能の更新 | modified | 22 | 8 | 30 | 


# Modified Contents
## articles/ai-services/document-intelligence/containers/install-run.md{#item-e32e11}

<details>
<summary>Diff</summary>
````diff
@@ -1178,7 +1178,7 @@ The Document Intelligence containers send billing information to Azure by using
 
 Queries to the container are billed at the pricing tier of the Azure resource used for the API `Key`. Billing is calculated for each container instance used to process your documents and images.
 
-If you receive the following error: *Container isn't in a valid state. Subscription validation failed with status 'OutOfQuota' API key is out of quota*. It's an indicator that your containers aren't communication wit the billing endpoint.
+If you receive the following error: *Container isn't in a valid state. Subscription validation failed with status 'OutOfQuota' API key is out of quota*. It's an indicator that your containers aren't communication with the billing endpoint.
 
 ### Connect to Azure
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書インテリジェンスコンテナのインストールと実行に関するドキュメントを修正"
}
```

### Explanation
この修正は、文書インテリジェンスコンテナに関するドキュメントの記述内容を微調整したものです。具体的には、エラーメッセージの説明文において、誤って「communication」単語が「wit」と綴られていた部分を、「with」に修正しました。この変更は文書の明確さを改善し、ユーザーに正確な情報を提供することを目的としています。全体として、エラーメッセージの理解を助けるための重要な修正です。

## articles/ai-services/language-service/concepts/model-lifecycle.md{#item-417f3f}

<details>
<summary>Diff</summary>
````diff
@@ -28,29 +28,25 @@ We recommend using the `latest` model version to utilize the latest and highest
 
 Preview models used for preview features do not maintain a minimum retirement period and may be deprecated at any time.
 
-By default, API and SDK requests will use the latest Generally Available model. You can use an optional parameter to select the version of the model to be used (not recommended).
+By default, API and SDK requests will use the latest Generally Available model. To use a model in preview, you can use an optional parameter `modelVersion` to select the preview version of the model to be used (not recommended for GA models).
 
 > [!NOTE]
 > If you are using a model version that is not listed in the table, then it was subjected to the expiration policy.
 
 Use the table below to find which model versions are supported by each feature:
 
-| Feature                                             | Supported generally available (GA) version     | Supported preview versions                  |
+| Feature                                             | Supported generally available (GA) version     | Latest supported preview versions           |
 |-----------------------------------------------------|------------------------------------------------|---------------------------------------------|
-| Sentiment Analysis and opinion mining               | `latest*`                                      |                                             |
-| Language Detection                                  | `latest*`                                      |                                             |
-| Entity Linking                                      | `latest*`                                      |                                             |
-| Named Entity Recognition (NER)                      | `latest*`                                      | `2024-04-15-preview**`                      |
-| Personally Identifiable Information (PII) detection | `latest*`                                      | `2024-04-15-preview**`                      | 
-| PII detection for conversations                     | `latest*`                                      | `2024-11-01-preview**`                      |
-| Question answering                                  | `latest*`                                      |                                             |
-| Text Analytics for health                           | `latest*`                                      | `2022-08-15-preview`, `2023-01-01-preview**`|
-| Key phrase extraction                               | `latest*`                                      |                                             | 
-| Summarization                                       |  `latest*`                                     |                                             |
-
-
-\* Latest Generally Available (GA) model version
-\*\* Latest preview version
+| Sentiment Analysis and opinion mining               | `latest`                                      |                                              |
+| Language Detection                                  | `latest`                                      |                                              |
+| Entity Linking                                      | `latest`                                      |                                              |
+| Named Entity Recognition (NER)                      | `latest`                                      | `2025-05-15-preview`                         |
+| Personally Identifiable Information (PII) detection | `latest`                                      | `2025-05-15-preview`                         | 
+| PII detection for conversations                     | `latest`                                      | `2024-11-01-preview`                         |
+| Question answering                                  | `latest`                                      |                                              |
+| Text Analytics for health                           | `latest`                                      | `2023-04-15-preview`                         |
+| Key phrase extraction                               | `latest`                                      |                                              | 
+| Summarization                                       | `latest`                                      | `2025-06-10-preview` (only available for `issue` and `resolution` aspects in conversation summarization)  |
 
 
 ## Custom features
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルに関するドキュメントの修正"
}
```

### Explanation
この修正は、モデルライフサイクルに関するドキュメントを更新したもので、特にAPIとSDKのリクエストにおけるモデルバージョンの選択方法に関する情報を明確にしています。具体的には、プレビュー版モデルを使用するためのオプションパラメータ`modelVersion`の使用方法が追加され、「推奨されない」という注意書きが含まれました。また、サポートされているモデルバージョンに関する表も更新され、最新の一般提供(GA)モデルやプレビューバージョンが明確に示されています。これにより、ユーザーは提供される機能に対してどのモデルバージョンがサポートされているかを簡単に確認できるようになります。全体として、情報の最新化と明確化が図られています。

## articles/ai-services/language-service/question-answering/how-to/configure-azure-resources.md{#item-a2ea5c}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom: language-service-question-answering
 
 # Configure your environment for Azure AI resources
 
-In this guide, we walk you through configuring your Azure AI resources and permissions for custom question and answering projects, enabling you to fine-tune models with Azure AI Search and Custom Question Answering (CQA). Completing this setup is essential for fully integrating your environment with Azure AI Services. You only need to perform this setup once—afterward, you have seamless access to advanced, AI-powered question answering capabilities.
+In this guide, we walk you through configuring your Azure AI resources and permissions for custom question and answering projects, enabling you to fine-tune models with Azure AI Search and Custom Question Answering (CQA). Completing this setup is essential for fully integrating your environment with Azure AI services resources. You only need to perform this setup once—afterward, you have seamless access to advanced, AI-powered question answering capabilities.
 
 In addition, we show you how to assign the correct roles and permissions within the Azure portal. These steps help you get started quickly and effectively with Azure AI Language.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureリソースの構成に関するドキュメントの修正"
}
```

### Explanation
この修正は、Azure AIリソースの構成に関するガイドラインを小幅に更新したものです。具体的には、文中の表現を「Azure AI Services」に関するリソースに合わせて滑らかにし、「Azure AI Services resources」という表現に変更されています。この微調整により、用語の一貫性が強化され、利用者にとってより明確に理解できる内容となっています。全体的に、ドキュメントの明瞭さと正確性を高めるための調整です。

## articles/ai-services/language-service/text-analytics-for-health/how-to/use-containers.md{#item-9dddb4}

<details>
<summary>Diff</summary>
````diff
@@ -128,7 +128,7 @@ Run this PowerShell script using the Azure CLI to create a Web App for Container
 ```azurecli
 $subscription_name = ""                    # THe name of the subscription you want you resource to be created on.
 $resource_group_name = ""                  # The name of the resource group you want the AppServicePlan
-                                           #    and AppSerivce to be attached to.
+                                           #    and AppService to be attached to.
 $resources_location = ""                   # This is the location you wish the AppServicePlan to be deployed to.
                                            #    You can use the "az account list-locations -o table" command to
                                            #    get the list of available locations and location code names.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテナ使用に関するドキュメントの修正"
}
```

### Explanation
この修正では、テキスト分析におけるコンテナの使用に関するドキュメントを一部更新しました。具体的には、PowerShellスクリプトのコメント部分での表記を修正しています。もともとは「AppSerivce」と誤って記載されていた名称が「AppService」と正しい表記に直されました。この変更により、利用者は正しいサービス名を理解しやすくなり、混乱を避けることができます。全体的に、ドキュメントの正確性を向上させるための小さな修正です。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,9 @@ items:
   - name: What is Azure AI Language?
     href: overview.md
     displayName: overview, introduction
+  - name: What's new
+    href: whats-new.md
+    displayName: release notes, updates, new features, changelog
   - name: Pricing
     href: https://aka.ms/unifiedLanguagePricing
   - name: Language support
@@ -18,9 +21,6 @@ items:
   - name: Quotas and limits
     href: concepts/data-limits.md
     displayName: service limits, rate, usage
-  - name: What's new
-    href: whats-new.md
-    displayName: release notes, updates, new features, changelog
 - name: Azure AI Language capabilities
   items:
   - name: Custom text classification
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI言語サービスの目次の更新"
}
```

### Explanation
この修正では、AI言語サービスの目次（`toc.yml`）に関する更新が行われました。主な変更点として、新たに「What's new」という項目が追加され、そのリンクが「whats-new.md」に設定されています。この新しい項目は、リリースノートや更新、新機能、変更履歴に関連する情報を提供するためのものです。一方で、同じ項目が削除されたため、内容の整理が進められています。全体として、目次の構造が改善され、ユーザーが新しい情報をより簡単に見つけられるようになっています。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -6,34 +6,48 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: whats-new
-ms.date: 06/02/2025
+ms.date: 07/09/2025
 ms.author: lajanuar
 ---
 
 # What's new in Azure AI Language?
 
 Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up to date with release notes, feature enhancements, and our newest documentation.
 
+## June 2025
+
+* A new version of the Conversational Language Understanding (CLU) training configuration, aimed at minimizing overpredictions of the [None intent](conversational-language-understanding/concepts/none-intent.md)—particularly in multilingual contexts—is now supported in [REST API version 2025-15-05-preview](/rest/api/language/analyze-conversations/analyze-conversations?view=rest-language-2025-05-15-preview&preserve-view=true).
+
+* The [Build your conversational agent](https://github.com/Azure-Samples/Azure-Language-OpenAI-Conversational-Agent-Accelerator) accelerator project is updated to include a new routing strategy—**TRIAGE_AGENT**. This strategy uses an agent hosted on Azure AI Foundry Agent Service. It utilizes Conversational Language Understanding (CLU) and Custom Question Answering (CQA) as tools to triage user intent for downstream agent routing. Additionally, these tools help deliver precise answers to specific questions. For more information, *see* [TechCommunity Blog Post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-azure-ai-language-new-features-to-accelerate-your-agent-development/4415216)
+
+* The following [.NET SDKs](/dotnet/api/overview/azure/ai.textanalytics-readme?view=azure-dotnet&preserve-view=true) are now available, and support the latest REST API version **2025-15-05-preview**:
+
+  * [Azure.AI.Language.Text 1.0.0-beta.3](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/cognitivelanguage/Azure.AI.Language.Conversations/CHANGELOG.md) provides inference capabilities for a wide range of language processing tasks. These tasks include language detection, sentiment analysis, key phrase extraction, and named entity recognition (NER). The capabilities also cover personally identifiable information (PII) entity recognition, entity linking, text analytics for healthcare, custom NER, and custom text classification. In addition, both extractive and abstractive text summarization are supported.
+
+  * [Azure.AI.Language.Conversation 2.0.0-beta.3](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/cognitivelanguage/Azure.AI.Language.Conversations/CHANGELOG.md) provides inference capabilities for conversational PII, conversational language understanding (CLU), and conversation summarization.
+
+* The Text PII GPU container is now available for integration. You can access it on the [Microsoft Artifact Registry](https://mcr.microsoft.com/artifact/mar/azure-cognitive-services/textanalytics/pii/) using the tag `gpu`.
+
 ## May 2025
 
 **2025-05-15-preview release**. The [latest API preview version](/rest/api/language/operation-groups?view=rest-language-2025-05-15-preview&preserve-view=true) includes updates for named entity recognition (NER) and PII detection:
 * New entity type support for `DateOfBirth`, `BankAccountNumber`, `PassportNumber`, and `DriversLicenseNumber`.
 * Improved AI quality for `PhoneNumber` entity type.
-  
+
 **New agent templates**. Azure AI Language now supports the following agent templates:
 *  [Intent routing](../agents/concepts/agent-catalog.md): Detects user intent and provides precise answers, ideal for deterministic intent routing, and exact question answering with human oversight.
 *   [Exact question answering](../agents/concepts/agent-catalog.md): Delivers consistent, accurate responses to high-value predefined questions through deterministic methods.
-  
+
 **PII detection enhancements**. Azure AI Language introduces new customization and entity subtype features for PII detection:
 *  [Customize PII detection using your own regex](personally-identifiable-information/how-to/adapt-to-domain-pii.md#customizing-pii-detection-using-your-own-regex-only-available-for-text-pii-container) (Text PII container only).
 *  [Specify values to exclude from PII output](personally-identifiable-information/how-to/adapt-to-domain-pii.md#customizing-pii-output-by-specifying-values-to-exclude).
 *  [Use entity synonyms for tailored PII detection](personally-identifiable-information/how-to/adapt-to-domain-pii.md#api-schema-for-the-entitysynoyms-parameter).
-  
+
 **Enhanced CLU and CQA Capabilities in Azure AI Foundry**. Azure AI Foundry now offers enhanced capabilities for fine-tuning with custom conversational language understanding (CLU) and conversational question-and-answer (CQA) AI features:
-*	CLU and CQA authoring tools are now available in Azure AI Foundry.
-*	CLU offers a quick deploy option powered by large language models (LLMs) for rapid deployment.
-*	CQA incorporates the QnA Maker scoring algorithm for more accurate responses.
-*	CQA enables exact match answering for precise query resolutions.
+*    CLU and CQA authoring tools are now available in Azure AI Foundry.
+*    CLU offers a quick deploy option powered by large language models (LLMs) for rapid deployment.
+*    CQA incorporates the QnA Maker scoring algorithm for more accurate responses.
+*    CQA enables exact match answering for precise query resolutions.
 
 **For more updates, see our latest [TechCommunity Blog Post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-azure-ai-language-new-features-to-accelerate-your-agent-development/4415216)**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI言語サービスの新機能の更新"
}
```

### Explanation
この修正では、Azure AI言語サービスに関する「What's New」ページが更新され、新機能やリリースノートの内容が追加されました。具体的には、2025年6月と5月の新機能が詳述されており、Conversational Language Understanding (CLU)の新バージョンや、新しいエージェントテンプレートのサポートが含まれています。また、.NET SDKの更新情報や、Text PII GPUコンテナの利用可能性についても述べられています。一部の過去の情報も削除されたため、最新の情報により、ユーザーは新機能をより効率的に把握できるようになっています。この更新は、新機能に関する理解を深め、開発者にとって有益な情報を提供することを目指しています。


