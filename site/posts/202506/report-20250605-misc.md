---
date: '2025-06-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:45b2d74...MicrosoftDocs:c6cc5fa
summary: 今回のコード差分は、主に多くのドキュメントに対する軽微な更新を含んでいます。新しい日付の設定、表現の微調整、一部の機能追加が行われました。具体的には、Azure
  AI Languageの「What's New」ページにPII検出のカスタマイズやエンティティサブタイプの新機能が追加され、APIの最新プレビューバージョンでは生命関連エンティティのサポートが強化されました。基本的には破壊的変更はなく、日付変更や表現の微調整が中心です。この差分により、ドキュメントの日付が最新情報に基づいて更新され、情報の信頼性が向上しています。また、表現の改善によりユーザビリティも向上し、新機能の追加が開発者にとって有用な手段を提供しています。全体として、文書の明確性とユーザビリティが向上しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:45b2d74...MicrosoftDocs:c6cc5fa){target="_blank"}

# ハイライト

今回のコード差分は、多くのドキュメントに対して行われた軽微な更新を含んでいます。新しい日付の設定、表現の微調整、一部の機能追加などが主な変更点です。

## 新機能
- Azure AI Languageの「What's New」ページでは、PII検出のカスタマイズやエンティティサブタイプの新機能が追加されています。
- APIの最新プレビューバージョンで生命関連エンティティのサポートが強化されました。
- エージェントテンプレートに意図ルーティングや正確なQ&Aのためのテンプレートが追加されています。

## 破壊的変更
- 破壊的変更は特にありません。更新は主に日付変更と表現の微調整です。

## その他の更新
- 多くのドキュメントにおいて、`ms.date`の日付が2024年11月21日から2025年6月4日に更新されています。
- 表現の微調整が行われ、文書全体の明確性と一貫性が向上しています。

# インサイト

### ドキュメントの最新性と明確性の向上
この差分により、ドキュメントの日付が最新情報に基づいて更新されました。日付の更新はしばしば軽視されることがありますが、読者がドキュメントの信頼性と最新性を確認するためには重要です。これにより、開発者やユーザーが最新の情報を持ってシステムを利用できるようになります。

### 表現の改善によるユーザビリティの向上
いくつかの文書で表現が改善され、統一された言い回しが提供されています。これにより、読者は情報をより理解しやすくなります。特に、技術ドキュメントでは一貫性のある表現が重要であり、文書を通じて一貫したメッセージを提供することができます。

### 新機能の追加
Azure AI Languageの「What's New」ページでの大幅な更新は、新機能や最近の開発のハイライトを紹介するために重要です。特にPII検出のカスタマイズ機能やエンティティサブタイプの追加は、実際の開発シナリオにおいて有用な手段を提供します。エージェントテンプレートの追加も、開発者が応用範囲を広げるために役立つでしょう。

全体として、この差分はドキュメントの最新性、明確性、そしてユーザビリティの向上に寄与しています。新しい情報や改善点を適切に反映させることは、エンドユーザーにとって有用であるだけでなく、開発者に正確な情報を提供するための基礎を築きます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [developer-guide.md](#item-003b09) | minor update | 開発者ガイドの日付と表現の更新 | modified | 10 | 10 | 20 | 
| [language-support.md](#item-45bafd) | minor update | 言語サポート文書の日付の更新 | modified | 1 | 1 | 2 | 
| [overview.md](#item-10e41c) | minor update | エンティティリンク文書の日付の更新 | modified | 1 | 1 | 2 | 
| [integrate-power-bi.md](#item-20f71f) | minor update | Power BI統合チュートリアルの日付の更新 | modified | 1 | 1 | 2 | 
| [overview.md](#item-53d49f) | minor update | オーケストレーションワークフロー概要の表現修正 | modified | 2 | 2 | 4 | 
| [entity-categories.md](#item-ba2623) | minor update | 個人識別情報のエンティティカテゴリに関する文書の日付更新 | modified | 1 | 1 | 2 | 
| [create-test-deploy.md](#item-80a22f) | minor update | 質問応答サービスのテストデプロイ手順の表現修正 | modified | 6 | 6 | 12 | 
| [bot-service.md](#item-f8e773) | minor update | FAQ ボット作成チュートリアルの表現修正 | modified | 4 | 4 | 8 | 
| [whats-new.md](#item-69b272) | minor update | Azure AI Languageの新機能およびアップデート内容の更新 | modified | 28 | 13 | 41 | 


# Modified Contents
## articles/ai-services/language-service/concepts/developer-guide.md{#item-003b09}

<details>
<summary>Diff</summary>
````diff
@@ -6,13 +6,13 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.author: lajanuar
 ---
 
 # SDK and REST developer guide for the Language service
 
-Use this article to find information on integrating the Language service SDKs and REST API into your applications. 
+Use this article to find information on integrating the Language service SDK and REST API into your applications. 
 
 ## Development options
 
@@ -22,14 +22,14 @@ The Language service provides support through a REST API, and client libraries i
 
 ## Client libraries (Azure SDK)
 
-The Language service provides three namespaces for using the available features. Depending on which features and programming language you're using, you will need to download one or more of the following packages, and have the following framework/language version support:
+The Language service provides three namespaces for using the available features. Depending on which features and programming language you're using, you'll need to download one or more of the following packages, and have the following framework/language version support:
 
 |Framework/Language  | Minimum supported version  |
 |---------|---------|
-|.NET     | .NET Framework 4.6.1 or newer, or .NET (formerly .NET Core) 2.0 or newer.       |
-|Java     | v8 or later        |
-|JavaScript     | v14 LTS or later        |
-|Python| v3.7 or later        |
+|.NET     | .NET Framework `4.6.1` or newer, or .NET (formerly .NET Core) `2.0` or newer.       |
+|Java     | `v8` or later        |
+|JavaScript     | `v14 LTS` or later        |
+|Python| `v3.7` or later        |
 
 ### Azure.AI.TextAnalytics  
 
@@ -38,7 +38,7 @@ The Language service provides three namespaces for using the available features.
 > * [Custom named entity recognition](../custom-named-entity-recognition/quickstart.md)
 > * [Custom text classification](../custom-text-classification/quickstart.md)
 
-The `Azure.AI.TextAnalytics` namespace enables you to use the following Language features. Use the links below for articles to help you send API requests using the SDK.
+The `Azure.AI.TextAnalytics` namespace enables you to use the following Language features. Use the following links for articles to help you send API requests using the SDK.
 
 * [Custom named entity recognition](../custom-named-entity-recognition/how-to/call-api.md?tabs=client#send-an-entity-recognition-request-to-your-model)
 * [Custom text classification](../custom-text-classification/how-to/call-api.md?tabs=client-libraries#send-a-text-classification-request-to-your-model)
@@ -63,11 +63,11 @@ As you use these features in your application, use the following documentation a
 ### Azure.AI.Language.Conversations 
 
 > [!NOTE] 
-> If you're using conversational language understanding or orchestration workflow, you will need to create a project and train a model before using the SDK. The SDK only provides the ability to analyze text using models you create. See the following quickstarts for more information. 
+> If you're using conversational language understanding or orchestration workflow, you'll need to create a project and train a model before using the SDK. The SDK only provides the ability to analyze text using models you create. See the following quickstarts for more information. 
 > * [Conversational language understanding](../conversational-language-understanding/quickstart.md)
 > * [Orchestration workflow](../orchestration-workflow/quickstart.md)
 
-The `Azure.AI.Language.Conversations` namespace enables you to use the following Language features. Use the links below for articles to help you send API requests using the SDK.
+The `Azure.AI.Language.Conversations` namespace enables you to use the following Language features. Use the following links for articles to help you send API requests using the SDK.
 
 * [Conversational language understanding](../conversational-language-understanding/how-to/call-api.md?tabs=azure-sdk#send-a-conversational-language-understanding-request)
 * [Orchestration workflow](../orchestration-workflow/how-to/call-api.md?tabs=azure-sdk#send-an-orchestration-workflow-request)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "開発者ガイドの日付と表現の更新"
}
```

### Explanation
この変更では、デベロッパーガイドの内容がいくつかの軽微な更新を受けました。主な変更点は、`ms.date`の値が2024年11月21日から2025年6月4日に変更されたことです。また、文章中のいくつかの表現が改善され、言い回しが統一されました。具体的には、SDK関連の説明で「integrating the Language service SDKs and REST API」が「integrating the Language service SDK and REST API」へ、また、条件文中の「you will need」が「you'll need」に、そして「the following links for articles」が「the following links for articles」にそれぞれ修正されました。

さらに、プログラミング言語やフレームワークの対応バージョンについては、各バージョン記載の周囲にバッククォートが追加され、視認性が向上しています。これらの更新は、文書全体の明確性を高め、開発者が必要な情報をより簡単に見つけられるようにするためのものです。

## articles/ai-services/language-service/concepts/language-support.md{#item-45bafd}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.author: lajanuar
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サポート文書の日付の更新"
}
```

### Explanation
この変更は、「言語サポート」文書において、`ms.date`の値が2024年11月21日から2025年6月4日に更新されるという軽微な修正です。この変更は、文書の最新性を保つために重要であり、読者にとって適切な情報を保証します。文書内容自体には大きな変更はなく、日付の更新が文書の信頼性を高めることに寄与しています。

## articles/ai-services/language-service/entity-linking/overview.md{#item-10e41c}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.author: lajanuar
 ms.custom: language-service-entity-linking
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティリンク文書の日付の更新"
}
```

### Explanation
この変更では、エンティティリンクの概要に関する文書において、`ms.date`の値が2024年11月21日から2025年6月4日に更新されました。これは文書の最新性を確保するための軽微な修正であり、読者に新しい情報を提供することに寄与します。変更内容はこの日付の更新のみであり、文書自体の他の部分には影響を与えません。これにより、ユーザーは常に最新のリリース情報を確認できるようになります。

## articles/ai-services/language-service/key-phrase-extraction/tutorials/integrate-power-bi.md{#item-20f71f}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: tutorial
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.author: lajanuar
 ms.custom: language-service-key-phrase, cogserv-non-critical-language
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Power BI統合チュートリアルの日付の更新"
}
```

### Explanation
この変更は、「Power BI統合」チュートリアル文書における`ms.date`の値を2024年11月21日から2025年6月4日に更新することを目的としています。この軽微な修正により、文書が最新のリリース情報を反映することが保証され、読者は常に正確で新しい情報を入手できるようになります。変更点は日付の更新のみであり、他の文書内容には影響ありません。これは、ユーザーにとって重要なチュートリアルの信頼性を高める効果があります。

## articles/ai-services/language-service/orchestration-workflow/overview.md{#item-53d49f}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.author: lajanuar
 ms.custom: language-service-orchestration
 ---
@@ -32,7 +32,7 @@ Orchestration workflow can be used in multiple scenarios across a variety of ind
 
 ### Enterprise chat bot
 
-In a large corporation, an enterprise chat bot may handle a variety of employee affairs. It may be able to handle frequently asked questions served by a custom question answering knowledge base, a calendar specific skill served by conversational language understanding, and an interview feedback skill served by LUIS. The bot needs to be able to appropriately route incoming requests to the correct service. Orchestration workflow allows you to connect those skills to one project that handles the routing of incoming requests appropriately to power the enterprise bot.
+In a large corporation, an enterprise chat bot might handle a variety of employee affairs. It might be able to handle frequently asked questions served by a custom question answering knowledge base, a calendar specific skill served by conversational language understanding, and an interview feedback skill served by LUIS. The bot needs to be able to appropriately route incoming requests to the correct service. Orchestration workflow allows you to connect those skills to one project that handles the routing of incoming requests appropriately to power the enterprise bot.
 
 ## Project development lifecycle
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オーケストレーションワークフロー概要の表現修正"
}
```

### Explanation
この変更では、オーケストレーションワークフローに関する概要文書に複数の軽微な修正が加えられました。主な修正点として、文書内の日付が2024年11月21日から2025年6月4日に変更されたほか、エンタープライズチャットボットの説明において「may」が「might」に変更され、一部の表現が微調整されました。これにより、文書の内容がより洗練され、読者に対して分かりやすい情報を提供することが期待されます。全体として、これらの更新は文書の明確性を向上させるためのものであり、仕様や情報の正確性を維持するために重要です。

## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories.md{#item-ba2623}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人識別情報のエンティティカテゴリに関する文書の日付更新"
}
```

### Explanation
この変更は、「個人識別情報」に関するエンティティカテゴリの文書における`ms.date`の値を2024年11月21日から2025年6月4日に更新することを目的としています。この軽微な更新によって、文書のリリース日が最新の情報と一致し、読者が常に正確で新しい情報に基づいてコンテンツを利用できるようになります。この修正は、文書の信頼性を向上させるために重要です。全体として、変更内容は日付の更新のみであり、他の文書の内容には変更は加えられていません。

## articles/ai-services/language-service/question-answering/how-to/create-test-deploy.md{#item-80a22f}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-language
 ms.topic: how-to
 author: laujan
 ms.author: lajanuar
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.custom: language-service-question-answering, mode-other
 ---
 
@@ -23,12 +23,12 @@ You can create a custom question answering project from your own content, such a
 
 1. Sign in to the [Language Studio](https://language.azure.com/) with your Azure credentials.
 
-2. Scroll down to the **Understand questions and conversational language** section and select **Open custom question answering**.
+2. Scroll down to **Understand questions and conversational language** and select **Open custom question answering**.
 
     > [!div class="mx-imgBorder"]
     > ![Open custom question answering](../media/create-test-deploy/open-custom-question-answering.png)
 
-3. If your resource is not yet connected to Azure Search select **Connect to Azure Search**. This will open a new browser tab to **Features** pane of your resource in the Azure portal.
+3. If your resource isn't yet connected to Azure Search select **Connect to Azure Search**. This opens a new browser tab to **Features** pane of your resource in the Azure portal.
 
     > [!div class="mx-imgBorder"]
     > ![Connect to Azure Search](../media/create-test-deploy/connect-to-azure-search.png)
@@ -52,9 +52,9 @@ You can create a custom question answering project from your own content, such a
 
     |URL Name|URL Value|
     |--------|---------|
-    |Surface Book User Guide |https://download.microsoft.com/download/7/B/1/7B10C82E-F520-4080-8516-5CF0D803EEE0/surface-book-user-guide-EN.pdf |
+    |Surface Book User Guide |`https://download.microsoft.com/download/7/B/1/7B10C82E-F520-4080-8516-5CF0D803EEE0/surface-book-user-guide-EN.pdf` |
 
-    The extraction process takes a few moments to read the document and identify questions and answers. Question and answering will determine if the underlying content is structured or unstructured.
+    The extraction process takes a few moments to read the document and identify questions and answers. The service determines if the underlying content is structured or unstructured.
 
     After successfully adding the source, you can then edit the source contents to add more custom question answer sets.
 
@@ -78,7 +78,7 @@ You can create a custom question answering project from your own content, such a
 
 ## Deploy your project
 
-1. Select the Deploy project icon to enter the deploy project menu.
+1. Select the **Deploy** project icon to enter the deploy project menu.
 
     > [!div class="mx-imgBorder"]
     > ![Deploy project](../media/create-test-deploy/deploy-knowledge-base.png)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "質問応答サービスのテストデプロイ手順の表現修正"
}
```

### Explanation
この変更は、質問応答サービスに関する「テストとデプロイの作成」手順における文書の一部に対する軽微な修正を含んでいます。主な修正内容は、文書内の日付の更新（2024年11月21日から2025年6月4日）と、手順の表現の微調整です。具体的には、手順番号の内容が簡潔に整理され、「may」や「is not」などの表現が標準的な形に変更されています。また、特定のリンクがコードブロック形式で示されるように修正され、情報の整合性が改善されています。これにより、読者にとっての理解が容易になり、手順に沿った操作がスムーズに行えるようになることが期待されます。全体として、変更は文書の明確性と一貫性を向上させることを目的としています。

## articles/ai-services/language-service/question-answering/tutorials/bot-service.md{#item-f8e773}

<details>
<summary>Diff</summary>
````diff
@@ -5,13 +5,13 @@ ms.service: azure-ai-language
 ms.topic: tutorial
 author: laujan
 ms.author: lajanuar
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.custom: language-service-question-answering, cogserv-non-critical-language
 ---
 
-# Tutorial: Create a FAQ bot
+# Tutorial: Create an FAQ bot
 
-Create a FAQ Bot with custom question answering and Azure [Bot Service](https://azure.microsoft.com/services/bot-service/) with no code.
+Create an FAQ Bot with custom question answering and Azure [Bot Service](https://azure.microsoft.com/services/bot-service/) with no code.
 
 In this tutorial, you learn how to:
 
@@ -34,7 +34,7 @@ After deploying your project, you can create a bot from the **Deploy project** p
 
 * When you make changes to the project and redeploy, you don't need to take further action with the bot. It's already configured to work with the project, and works with all future changes to the project. Every time you publish a project, all the bots connected to it are automatically updated.
 
-1. In Language Studio, on the custom question answering **Deploy project** page, select the **Create a bot** button.
+1. In [Language Studio](https://language.azure.com/), on the custom question answering **Deploy project** page, select the **Create a bot** button.
 
     > [!div class="mx-imgBorder"]
     > ![Screenshot of UI with option to create a bot in Azure.](../media/bot-service/create-bot-in-azure.png)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQ ボット作成チュートリアルの表現修正"
}
```

### Explanation
この変更は、FAQボットの作成に関するチュートリアル文書の一部に対して軽微な修正を行ったものです。主な更新点は、文書の日付の変更（2024年11月21日から2025年6月4日）と、タイトルと手順の表現の若干の修正です。具体的には、タイトルが「FAQボット作成」から「FAQ ボット作成」と空白が追加され、文中の一部の表現が明確化されています。また、手順において「Language Studio」のリンクが追加され、ユーザーが直接アクセス可能になるようになっています。これらの変更は、文書の一貫性を高め、読者にとってわかりやすい情報提供を目指しています。全体として、この修正は文書の可読性とユーザビリティの向上に寄与しています。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -12,23 +12,38 @@ ms.author: lajanuar
 
 # What's new in Azure AI Language?
 
-Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent developments, this article provides you with information about new releases and features.
+Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up to date with release notes, feature enhancements, and our newest documentation.
 
-## Build 2025 Releases (May 19 - 23)
-We released many new updates alongside the 2025 Microsoft Build Conference including:
--    [Customizing PII detection using your own regex](personally-identifiable-information/how-to/adapt-to-domain-pii.md#customizing-pii-detection-using-your-own-regex-only-available-for-text-pii-container) (only available for Text PII container)
--    Support for customizing PII output by [specifying values to exclude](personally-identifiable-information/how-to/adapt-to-domain-pii.md#customizing-pii-output-by-specifying-values-to-exclude)
--    Customizing PII detection using [Entity Synonyms](personally-identifiable-information/how-to/adapt-to-domain-pii.md#api-schema-for-the-entitysynoyms-parameter)
--    Model support for a new DateOfBirth entity subtype for PII detection.
--    Updates to preview NER & PII API version: `2025-05-15-preview`. This API version includes DateOfBirth support, enhanced phone number AI quality, and umbrella entity type support for BankAccount, Passport, Drivers License
+## May 2025
 
-More on these releases can be found on our TechCommunity Blog Post
+##### New agent templates 
 
-## May 2025
+Azure AI Language now supports the following agent templates:
+
+*  [Intent routing](../agents/concepts/agent-catalog.md): Detects user intent and provides precise answers, ideal for deterministic intent routing, and exact question answering with human oversight.
+
+*   [Exact question answering](../agents/concepts/agent-catalog.md): Delivers consistent, accurate responses to high-value predefined questions through deterministic methods.
+
+##### PII detection enhancements
+
+Azure AI Language introduces new customization and entity subtype features for PII detection:
+
+*  [Customize PII detection using your own regex](personally-identifiable-information/how-to/adapt-to-domain-pii.md#customizing-pii-detection-using-your-own-regex-only-available-for-text-pii-container) (Text PII container only).
+
+*  [Specify values to exclude from PII output](personally-identifiable-information/how-to/adapt-to-domain-pii.md#customizing-pii-output-by-specifying-values-to-exclude).
+
+*  [Use entity synonyms for tailored PII detection](personally-identifiable-information/how-to/adapt-to-domain-pii.md#api-schema-for-the-entitysynoyms-parameter).
+
+##### 2025-05-15-preview release. 
+
+The [latest API preview version](/rest/api/language/operation-groups?view=rest-language-2025-05-15-preview&preserve-view=true) includes updates for named entity recognition (NER) and PII detection:
+
+* New entity type support for `DateOfBirth`, `BankAccountNumber`, `PassportNumber`, and `DriversLicenseNumber`.
+
+* Improved AI quality for `PhoneNumber` entity type.
+
+To learn more, see our latest [TechCommunity Blog Post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-azure-ai-language-new-features-to-accelerate-your-agent-development/4415216).
 
-* Azure AI Language now supports the following agent templates:
-    *   [Intent routing](../agents/concepts/agent-catalog.md) detects user intent and provides exact answering. Perfect for deterministically intent routing and exact question answering with human controls.
-    *   [Exact question answering](../agents/concepts/agent-catalog.md) answers high-value predefined questions deterministically to ensure consistent and accurate responses.
 
 ## April 2025
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Languageの新機能およびアップデート内容の更新"
}
```

### Explanation
この変更では、Azure AI Languageの「What's New」ページに関するコンテンツが大幅に更新されました。主な変更点は、情報の整理と新機能の追加です。文書は新しいリリースや機能強化、ドキュメントを最新の状態に保つためにブックマークを推奨する内容に修正されました。

具体的には、2025年5月に関連する新機能が紹介されています。これには、PII（個人識別情報）検出のカスタマイズ機能やエンティティサブタイプの追加、特定のエンティティタイプのサポートが含まれています。また、APIの最新プレビューバージョンでの更新が記載され、生命に関連するエンティティのサポートが強化されています。

さらに、エージェントテンプレートの新機能として、意図ルーティングや正確な質問応答のためのテンプレートが追加され、それぞれの機能の使用例と利点が明示されています。全体として、この変更はAzure AI Languageの機能や最新情報をユーザーに明確に伝えることを目指しており、開発者やユーザーにとって有用なリソースとなることが期待されています。


