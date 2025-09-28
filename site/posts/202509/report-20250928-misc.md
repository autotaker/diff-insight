---
date: '2025-09-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8df9d90...MicrosoftDocs:24ed2ed
summary: Azure AI Languageのエンティティリンク機能に関する重要な通知が追加され、この機能は2028年9月1日にサポート終了となります。代わりとして「Named
  Entity Recognition」への移行が推奨されています。また、ドキュメント全体で表現の改善や文言の明確化が行われました。ユーザーは既存システムの改修や新しいプロジェクトに対して代替機能を検討する必要があるため、早めの対応が重要です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8df9d90...MicrosoftDocs:24ed2ed){target="_blank"}

<format>
# Highlights
Azure AI Languageのエンティティリンク機能について、新たに引退に関する重要な通知が追加されました。2028年9月1日をもってサポート終了となるこの機能に代わり、「Named Entity Recognition」への移行が推奨されています。また、文書全体にわたって文章の明確化や表現の改善が行われました。

## New features
- Azure AI Languageのドキュメントにおけるエンティティリンク機能の引退に関する重要な通知の追加
- エントリ退職の告知に伴う、既存のワークロード移行と新たなプロジェクトに対する代替機能の提案

## Breaking changes
- 2028年9月1日以降、エンティティリンク機能がサポートされなくなる

## Other updates
- ドキュメンテーション全体における表現の改善と文言の明確化
- ドキュメントの日付更新と用語定義の明確化

# Insights
このドキュメントの更新では、Azure AI Languageにおけるエンティティリンク機能の将来の廃止が明示され、ユーザーに対してその準備を啓発しています。エンティティリンク機能は、特定の用語を適切なエンティティ（例：人物、場所、イベントなど）にリンクするものでしたが、2028年9月1日にサポート終了予定となっています。これにより、ユーザーは既存システムを改修し、新しいプロジェクトにはより推奨される代替機能を利用することになります。

特にユーザーに影響を与えるのは、サポート終了後にはこの機能がクラウド環境で利用できなくなるため、あらかじめ移行プランを立てて「Named Entity Recognition」などの他のサービスを検討することの重要性です。ドキュメントには移行に伴う推奨事項が詳細に記載されており、ユーザーが適切な判断を下せるように工夫されています。また、全体を通じての言語のクリアさと用語の定義の明確化により、読者はより直感的に情報を理解できるようになります。

この更新は、ユーザーがAzure AI Languageサービスを利用する際に将来の計画を立てやすくするための配慮が施されています。企業戦略や技術戦略の変革に伴い、早めの対応が求められるため、長期的な視点での計画策定が必須です。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [call-api.md](#item-90cbe4) | minor update | APIの更新とEntity Linkingの引退についての通知 | modified | 11 | 7 | 18 | 
| [language-support.md](#item-e92877) | minor update | エンティティリンク機能の引退通知の追加 | modified | 4 | 0 | 4 | 
| [overview.md](#item-10e41c) | minor update | エンティティリンク機能の引退についての重要なお知らせ | modified | 4 | 0 | 4 | 
| [quickstart.md](#item-79ac7d) | minor update | エンティティリンク機能の引退通知の追加 | modified | 5 | 1 | 6 | 
| [overview.md](#item-f138b4) | minor update | エンティティリンク機能引退のお知らせ追加 | modified | 6 | 2 | 8 | 


# Modified Contents
## articles/ai-services/language-service/entity-linking/how-to/call-api.md{#item-90cbe4}

<details>
<summary>Diff</summary>
````diff
@@ -6,14 +6,18 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 06/21/2025
+ms.date: 09/26/2025
 ms.author: lajanuar
 ms.custom: language-service-entity-linking
 ---
 
 # How to use entity linking
 
-The entity linking feature can be used to identify and disambiguate the identity of an entity found in text (for example, determining whether an occurrence of the word "*Mars*" refers to the planet, or to the Roman god of war). It will return the entities in the text with links to [Wikipedia](https://www.wikipedia.org/) as a knowledge base.
+> [!IMPORTANT]
+> Entity Linking is retiring from Azure AI Language effective **September 1, 2028**. After this date, the Entity Linking feature is no longer supported.   During the support window, we recommend that users migrate existing workloads and direct all new projects to Azure AI Language [**Named Entity Recognition**](../../named-entity-recognition/overview.md) or consider other alternative solutions.
+
+
+The entity linking feature enables the detection and clarification of the specific identity of entities mentioned within text. For instance, it can determine whether the term "Mars" refers to the planet or to the Roman god of war. This capability helps eliminate ambiguity by associating each entity with the correct context. It returns the entities in the text with links to [Wikipedia](https://www.wikipedia.org/) as a knowledge base.
 
 
 ## Development options
@@ -24,20 +28,20 @@ The entity linking feature can be used to identify and disambiguate the identity
 
 ### Specify the entity linking model
 
-By default, entity linking will use the latest available AI model on your text. You can also configure your API requests to use a specific [model version](../../concepts/model-lifecycle.md).
+By default, entity linking uses the latest available AI model on your text. You can also configure your API requests to use a specific [model version](../../concepts/model-lifecycle.md).
 
 ### Input languages
 
-When you submit documents to be processed by entity linking, you can specify which of [the supported languages](../language-support.md) they're written in. if you don't specify a language, entity linking will default to English. Due to [multilingual and emoji support](../../concepts/multilingual-emoji-support.md), the response may contain text offsets. 
+When you submit documents to for entity linking processing, you can specify which of [the supported languages](../language-support.md) they're written in. If you don't specify a language, entity linking defaults to English. Due to [multilingual and emoji support](../../concepts/multilingual-emoji-support.md), the response may contain text offsets. 
 
 ## Submitting data
 
-Entity linking produces a higher-quality result when you give it smaller amounts of text to work on. This is opposite from some features, like key phrase extraction which performs better on larger blocks of text. To get the best results from both operations, consider restructuring the inputs accordingly.
+Entity linking produces a higher-quality result when you give it smaller amounts of text to work on. This characteristic is opposite from some features, like key phrase extraction that performs better on larger blocks of text. To get the best results from both operations, consider restructuring the inputs accordingly.
 
-To send an API request, you will need a Language resource endpoint and key.
+To send an API request, you need a Language resource endpoint and API key.
 
 > [!NOTE]
-> You can find the key and endpoint for your Language resource on the Azure portal. They will be located on the resource's **Key and endpoint** page, under **resource management**. 
+> You can find the key and endpoint for your Language resource on the Azure portal. They're located on the resource's **Key and endpoint** page, under **resource management**. 
 
 Analysis is performed upon receipt of the request. Using entity linking synchronously is stateless. No data is stored in your account, and results are returned immediately in the response.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIの更新とEntity Linkingの引退についての通知"
}
```

### Explanation
この変更は、Azure AI Languageのエンティティリンク機能に関するドキュメントを更新し、重要な通知を追加したものです。特に、エンティティリンク機能が2028年9月1日をもって Azure AI Language から引退することが明示されています。この日以降はエンティティリンク機能がサポートされなくなるため、既存のワークロードの移行を推奨し、新たなプロジェクトに対しては「Named Entity Recognition」という代替機能への移行を促しています。 

具体的には、セクションの見出しや文章における使用言語、リソースキーの見つけ方、APIへのリクエストの送信方法に関する表現が改善され、より明確で分かりやすい内容へと改訂されています。また、文章中のいくつかの文がより読みやすい形に修正され、全体としての理解が容易になっています。変更には、追加された重要な情報や文の修正といった内容が含まれており、ユーザーがAzure AI Languageのエンティティリンク機能を使用する際の注意点が強調されています。

## articles/ai-services/language-service/entity-linking/language-support.md{#item-e92877}

<details>
<summary>Diff</summary>
````diff
@@ -13,6 +13,10 @@ ms.custom: language-service-entity-linking
 
 # Entity linking language support 
 
+> [!IMPORTANT]
+> Entity Linking is retiring from Azure AI Language effective **September 1, 2028**. After this date, the Entity Linking feature is no longer supported.   During the support window, we recommend that users migrate existing workloads and direct all new projects to Azure AI Language [**Named Entity Recognition**](../named-entity-recognition/overview.md) or consider other alternative solutions.
+
+
 | Language | Language code | Notes |
 |:---------|:-------------:|:-----:|
 | English  |     `en`      |      |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティリンク機能の引退通知の追加"
}
```

### Explanation
この変更は、Azure AI Languageのエンティティリンク機能に関する言語サポートのドキュメントに重要な通知を追加したものです。具体的には、エンティティリンク機能が2028年9月1日をもってサポート終了となることが記載されています。この日以降に使用できなくなるため、既存のワークロードを移行し、新たにプロジェクトを開始する際には「Named Entity Recognition」機能などの代替ソリューションを検討することを推奨しています。

この変更には、新たに追加された注意書きが含まれており、エンティティリンク機能の将来的なサポート状況についての情報が強調されています。また、言語サポートの一覧も保持されており、引き続きユーザーが言語コードや追加情報を参照できる形になっています。この追加情報は、ユーザーが今後の計画を立てる際に重要な役割を果たします。

## articles/ai-services/language-service/entity-linking/overview.md{#item-10e41c}

<details>
<summary>Diff</summary>
````diff
@@ -13,6 +13,10 @@ ms.custom: language-service-entity-linking
 
 # What is entity linking in Azure AI Language?
 
+> [!IMPORTANT]
+> Entity Linking is retiring from Azure AI Language effective **September 1, 2028**. After this date, the Entity Linking feature is no longer supported.   During the support window, we recommend that users migrate existing workloads and direct all new projects to Azure AI Language [**Named Entity Recognition**](../named-entity-recognition/overview.md) or consider other alternative solutions.
+
+
 Entity linking is one of the features offered by [Azure AI Language](../overview.md), a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. Entity linking identifies and disambiguates the identity of entities found in text. For example, in the sentence "*We went to Seattle last week.*", the word "*Seattle*" would be identified, with a link to more information on Wikipedia.
 
 This documentation contains the following types of articles:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティリンク機能の引退についての重要なお知らせ"
}
```

### Explanation
この変更は、Azure AI Languageにおけるエンティティリンク機能の概要を説明するドキュメントに重要なお知らせを追加したものです。具体的には、エンティティリンク機能が2028年9月1日からサポート終了となることが明示されています。この日以降、エンティティリンク機能は使用できなくなるため、ユーザーには既存のワークロードを他の機能へ移行し、新たなプロジェクトには「Named Entity Recognition」という別の機能を利用するよう推奨しています。

追加された重要なお知らせは、ユーザーが今後の計画を考える際に必要な情報を提供しており、エンティティリンク機能の将来的な利用についての注意喚起となっています。ドキュメントは引き続き、エンティティリンクの機能とその技術的な背景に関する情報を提供しており、利用者が適切に情報を取得できるよう配慮されています。

## articles/ai-services/language-service/entity-linking/quickstart.md{#item-79ac7d}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 06/21/2025
+ms.date: 09/26/2025
 ms.author: lajanuar
 ms.devlang: csharp
 # ms.devlang: csharp, java, javascript, python
@@ -17,6 +17,10 @@ zone_pivot_groups: programming-languages-entity-linking
 
 # Quickstart: Entity Linking using the client library and REST API
 
+> [!IMPORTANT]
+> Entity Linking is retiring from Azure AI Language effective **September 1, 2028**. After this date, the Entity Linking feature is no longer supported.   During the support window, we recommend that users migrate existing workloads and direct all new projects to Azure AI Language [**Named Entity Recognition**](../named-entity-recognition/overview.md) or consider other alternative solutions.
+
+
 ::: zone pivot="programming-language-csharp"
 
 [!INCLUDE [C# quickstart](includes/quickstarts/csharp-sdk.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティリンク機能の引退通知の追加"
}
```

### Explanation
この変更は、Azure AI Languageのエンティティリンク機能を使用したクイックスタートガイドに重要な通知を追加したものです。具体的には、エンティティリンク機能が2028年9月1日をもってサポート終了することが強調されています。この日以降、エンティティリンク機能は使用できなくなるため、ユーザーには既存のワークロードを別の機能へ移行し、新たに開始するプロジェクトには「Named Entity Recognition」機能などの代替ソリューションを検討することが推奨されています。

また、変更には日付の更新が含まれており、元の記載（日付：2025年6月21日）が2025年9月26日に変更されています。この新しい日付は、ドキュメントの最新の状態を示し、追加情報とともに利用者がエンティティリンク機能に対して理解を深めるのに役立ちます。重要なお知らせは、今後のプランニングや実行において、ユーザーが適切な決定を下すための情報提供としての役割を果たします。

## articles/ai-services/language-service/overview.md{#item-f138b4}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 07/17/2025
+ms.date: 09/26/2025
 ms.author: lajanuar
 ---
 
@@ -48,7 +48,7 @@ The Language service also provides several new features as well, which can eithe
       :::image type="content" source="media/overview/text-pii.png" alt-text="A screenshot of text personally identifying information in Azure AI Foundry." lightbox="media/overview/text-pii.png":::
    :::column-end:::
    :::column span="":::
-      [PII detection](./personally-identifiable-information/overview.md) identifies entities in text and conversations (chat or transcripts) that are associated with individuals.
+      [Personally Identifiable Information (PII) detection](./personally-identifiable-information/overview.md) identifies entities in text and conversations (chat or transcripts) that are associated with individuals.
 
    :::column-end:::
 :::row-end:::
@@ -105,6 +105,10 @@ Conversation summarization recaps and segments long meetings into timestamped ch
 
 ### Entity linking
 
+> [!IMPORTANT]
+> Entity Linking is retiring from Azure AI Language effective **September 1, 2028**. After this date, the Entity Linking feature is no longer supported.   During the support window, we recommend that users migrate existing workloads and direct all new projects to Azure AI Language [**Named Entity Recognition**](named-entity-recognition/overview.md) or consider other alternative solutions.
+
+
 :::row:::
    :::column span="":::
       :::image type="content" source="media/studio-examples/entity-linking.png" alt-text="A screenshot of an entity linking example." lightbox="media/studio-examples/entity-linking.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティリンク機能引退のお知らせ追加"
}
```

### Explanation
この変更は、Azure AI Languageサービスの概要に関するドキュメントの更新で、重要なお知らせを追加したものです。具体的には、エンティティリンク機能が2028年9月1日をもってサポートされなくなる旨が記載されています。この情報は、ユーザーに対して将来の計画を妨げることなく、既存のワークロードを他のサービスに移行することが推奨されています。また、新しいプロジェクトに対しては「Named Entity Recognition」機能を検討するように促しています。

さらに、更新内容にはドキュメントに日付の変更（2025年7月17日から2025年9月26日）や、特定の用語の定義を明確にするための文言の追加が含まれています。たとえば、「PII detection」という用語が「Personally Identifiable Information (PII) detection」と表現されることで、読者にとって理解しやすくなっています。この変更により、情報はより明確かつ最新の状態で提供されることが保証されます。


