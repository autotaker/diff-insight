---
date: '2025-06-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c6cc5fa...MicrosoftDocs:e10a743
summary: この変更では、Microsoft Azure AI Language Serviceに関するドキュメントが更新されました。主な内容には日付の更新、文体の微調整、用語の一貫性向上が含まれています。特に「最新情報」セクションでは、新機能やエンティティ認識の精度向上についての詳細が追加され、開発者の生産性向上に寄与する内容となっています。全体として、文書の整合性と鮮度を保つことを目的とした重要な更新です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c6cc5fa...MicrosoftDocs:e10a743){target="_blank"}

<format>
# ハイライト
この変更では、Microsoft Azure AI Language Serviceに関するドキュメントに複数の更新が行われました。主な内容としては、日付のアップデート、表現や文体の微調整、用語の一貫性向上などです。特に「最新情報」セクションでは、新たな機能や能力の拡張についての詳細が追加されています。

## 新しい機能

1. **名前付きエンティティ認識（NER）と個人識別情報（PII）のアップデート** - 新たなエンティティタイプのサポートと特定のエンティティタイプの検出精度向上。
2. **Azure AI Foundryの強化内容** - 大規模言語モデル（LLM）採用や新しい著作ツールの提供。

## 破壊的変更
特に破壊的な変更はないが、いくつかの用語や表現の変更により、一貫性が向上されている。

## 他の更新
- ドキュメントの日付更新。
- 文法および微細な表現の修正。
- FAQやチュートリアル記事のマイナーな編集。

# インサイト
この更新は、主にドキュメントの整合性と鮮度を保つためのものです。Azure AI Language Serviceは常に進化しており、今回のアップデートでは最新の技術トレンドや機能改善を反映した内容となっています。

特に「最新情報」セクションでは、新たなエンティティタイプのサポートや、品質向上が強調されており、これにより、エンティティ認識の精度が向上し、より信頼性のあるデータ抽出が可能になります。また、Azure AI Foundryのエージェント開発環境強化に関する情報は、開発者の生産性を向上させるもので、多機能なAIエージェントの構築を促進します。

これによって、開発者はよりスムーズに最新のAzure機能を利用でき、迅速かつ効率的に製品の強化を図ることができます。ユーザーにとってこれらの更新は、正確かつユーザーフレンドリーなガイダンスを提供するために不可欠で、Azure AI Language Serviceの利用体験を向上させるものとなっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [best-practices.md](#item-ae9331) | minor update | ベストプラクティスの更新 | modified | 3 | 3 | 6 | 
| [entity-components.md](#item-9168dd) | minor update | エンティティコンポーネントの文書更新 | modified | 1 | 1 | 2 | 
| [evaluation-metrics.md](#item-d6ba3f) | minor update | 評価指標に関する文書の更新 | modified | 1 | 1 | 2 | 
| [faq.md](#item-590d89) | minor update | FAQドキュメントの更新 | modified | 1 | 1 | 2 | 
| [call-api.md](#item-ce9a73) | minor update | API呼び出しに関するドキュメントの更新 | modified | 4 | 4 | 8 | 
| [language-support.md](#item-6b7b2b) | minor update | 言語サポートドキュメントのタイトル修正 | modified | 1 | 1 | 2 | 
| [prebuilt-component-reference.md](#item-5af620) | minor update | ドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [service-limits.md](#item-0c7212) | minor update | サービス制限ドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [bot-framework.md](#item-3415a0) | minor update | ボットフレームワークチュートリアルの日付とレビュー担当者の更新 | modified | 1 | 2 | 3 | 
| [call-api.md](#item-82812f) | minor update | API呼び出し手順書の日付更新と文法修正 | modified | 2 | 2 | 4 | 
| [language-support.md](#item-d332b1) | minor update | PII検出の言語サポートに関する更新 | modified | 2 | 2 | 4 | 
| [confidence-score.md](#item-e1fec0) | minor update | カスタム質問応答の信頼性スコアに関する表現の修正 | modified | 5 | 5 | 10 | 
| [migrate-qnamaker-to-question-answering.md](#item-93cb3f) | minor update | QnA Makerからカスタム質問応答への移行に関する表現の修正 | modified | 4 | 4 | 8 | 
| [migrate-qnamaker.md](#item-0646f1) | minor update | QnA Makerからカスタム質問応答への移行に関する表現の修正 | modified | 2 | 2 | 4 | 
| [active-learning.md](#item-e8486d) | minor update | アクティブ学習を活用したカスタム質問応答プロジェクトの強化に関する修正 | modified | 4 | 4 | 8 | 
| [guided-conversations.md](#item-a43dd4) | minor update | ガイド付き対話に関するチュートリアルの表現修正 | modified | 2 | 2 | 4 | 
| [whats-new.md](#item-69b272) | minor update | Azure AI Languageの最新機能と強化内容の更新 | modified | 16 | 5 | 21 | 


# Modified Contents
## articles/ai-services/language-service/conversational-language-understanding/concepts/best-practices.md{#item-ae9331}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: best-practice
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
 ---
@@ -112,7 +112,7 @@ If you enable this feature, the utterance count of your training set increases.
 
 ## Address model overconfidence
 
-Customers can use the LoraNorm traning configuration version if the model is being incorrectly overconfident. An example of this behavior can be like the following scenario where the model predicts the incorrect intent with 100% confidence. This score makes the confidence threshold project setting unusable.
+Customers can use the LoraNorm training configuration version if the model is being incorrectly overconfident. An example of this behavior can be like the following scenario where the model predicts the incorrect intent with 100% confidence. This score makes the confidence threshold project setting unusable.
 
 | Text |	Predicted intent |	Confidence score |
 |----|----|----|
@@ -272,6 +272,6 @@ After the request is sent, you can track the progress of the training job in Lan
 
 Caveats:
 
-- The None score threshold for the app (confidence threshold below which `topIntent` is marked as `None`) when you use this training configuration should be set to 0. This setting is used because this new training configuration attributes a certain portion of the in-domain probabilities to out of domain so that the model isn't incorrectly overconfident about in-domain utterances. As a result, users might see slightly reduced confidence scores for in-domain utterances as compared to the prod training configuration.
+- The None score threshold for the app (confidence threshold below which `topIntent` is marked as `None`) when you use this training configuration should be set to 0. This setting is used because this new training configuration attributes a certain portion of the in-domain probabilities to out of domain so that the model isn't incorrectly overconfident about in-domain utterances. As a result, users might see slightly reduced confidence scores for in-domain utterances as compared to the production training configuration.
 - We don't recommend this training configuration for apps with only two intents, such as `IntentA` and `None`, for example.
 - We don't recommend this training configuration for apps with a low number of utterances per intent. We highly recommend a minimum of 25 utterances per intent.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベストプラクティスの更新"
}
```

### Explanation
この変更は、Microsoft Azure AI Language Serviceのベストプラクティスに関するドキュメントにおける修正です。主要な更新には、日付の変更といくつかの文の微調整が含まれています。具体的には、日付が「2024年11月21日」から「2025年6月4日」に変更されました。また、モデルの過剰な自信を addressing する方法の説明がより明確にされ、いくつかの段落が文法上の微細な修正を受けています。全体として、これらの変更は、文書の明確さと正確性を向上させることを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/concepts/entity-components.md{#item-9168dd}

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
 ms.custom: language-service-clu
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティコンポーネントの文書更新"
}
```

### Explanation
この変更は、Microsoft Azure AI Language Serviceのエンティティコンポーネントに関するドキュメントの更新です。主な変更点は、文書の日付が「2024年11月21日」から「2025年6月4日」に更新されたことです。この日付の更新は、ドキュメントの内容が最新の情報を反映するためのものです。その他には、特に内容の変更はなく、主にメタデータの一部が修正された形となっています。これは、情報の整合性を保つための小さな更新です。

## articles/ai-services/language-service/conversational-language-understanding/concepts/evaluation-metrics.md{#item-d6ba3f}

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
 ms.custom: language-service-clu
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価指標に関する文書の更新"
}
```

### Explanation
この変更は、Microsoft Azure AI Language Serviceにおける評価指標に関する文書の更新です。具体的には、文書の日付が「2024年11月21日」から「2025年6月4日」に変更されました。この更新は、文書の内容が最新の情報を反映し、ユーザーに正確なガイダンスを提供するためのものです。他の変更はほとんどなく、主にメタデータの一部が修正された状況です。これは、文書の信頼性と適時性を保持するための小さな更新といえます。

## articles/ai-services/language-service/conversational-language-understanding/faq.md{#item-590d89}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: faq
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.author: lajanuar
 ms.custom: mode-other
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQドキュメントの更新"
}
```

### Explanation
この変更は、Microsoft Azure AI Language Serviceに関するFAQドキュメントの更新です。変更の主な内容は、文書の日付が「2024年11月21日」から「2025年6月4日」に改訂されたことです。この日付の更新は、文書が最新の情報を反映するためのものであり、正確な情報提供を目的としています。他の内容に関しての変更はほとんどなく、主にメタデータの修正が行われた状況です。この小規模な更新は、文書の信頼性と関連性を保つために重要です。

## articles/ai-services/language-service/conversational-language-understanding/how-to/call-api.md{#item-ce9a73}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
 ---
@@ -18,7 +18,7 @@ You can query the deployment programmatically through the [prediction API](https
 
 ## Test deployed model
 
-You can use Language Studio to submit an utterance, get predictions and visualize the results.
+You can use Language Studio to submit an utterance, get predictions, and visualize the results.
 
 [!INCLUDE [Test model](../includes/language-studio/test-model.md)]
 
@@ -32,7 +32,7 @@ You can use Language Studio to submit an utterance, get predictions and visualiz
 
 # [REST APIs](#tab/REST-APIs)
 
-First you will need to get your resource key and endpoint:
+First you'll need to get your resource key and endpoint:
 
 [!INCLUDE [Get keys and endpoint Azure Portal](../includes/get-keys-endpoint-azure.md)]
 
@@ -53,7 +53,7 @@ You can also use the client libraries provided by the Azure SDK to send requests
 
 1. Go to your resource overview page in the [Azure portal](https://portal.azure.com/#home)
 
-2. From the menu on the left side, select **Keys and Endpoint**. Use endpoint for the API requests and you will need the key for `Ocp-Apim-Subscription-Key` header.
+2. From the menu on the left side, select **Keys and Endpoint**. Use endpoint for the API requests and you'll need the key for `Ocp-Apim-Subscription-Key` header.
 
     :::image type="content" source="../../custom-text-classification/media/get-endpoint-azure.png" alt-text="A screenshot showing a key and endpoint in the Azure portal." lightbox="../../custom-text-classification/media/get-endpoint-azure.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "API呼び出しに関するドキュメントの更新"
}
```

### Explanation
この変更は、Microsoft Azure AI Language ServiceにおけるAPI呼び出しに関する方法を説明するドキュメントの更新です。主な改訂点は、文書の日付が「2024年11月21日」から「2025年6月4日」に変更されたことです。また、いくつかの文言が微調整され、より自然な表現に修正されました。

具体的には、「get predictions and visualize the results」というフレーズが「get predictions, and visualize the results」となり、句読点が追加されました。同様に、「you will need」という表現が「you'll need」と短縮されています。これにより、読みやすさと流暢さが向上しています。このような小規模な更新は、ユーザーが正確で分かりやすい情報にアクセスできるようにするための重要なステップです。

## articles/ai-services/language-service/conversational-language-understanding/language-support.md{#item-6b7b2b}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.author: lajanuar
 ms.custom: language-service-clu
 ---
 
-# Language support for conversational language understanding
+# Language support for Conversational Language Understanding (CLU)
 
 Use this article to learn about the languages currently supported by CLU feature.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サポートドキュメントのタイトル修正"
}
```

### Explanation
この変更は、Microsoft Azureの会話型言語理解（CLU）における言語サポートに関するドキュメントのタイトルを修正するものです。具体的には、ドキュメントのタイトルが「Language support for conversational language understanding」から「Language support for Conversational Language Understanding (CLU)」に変更されました。

この修正により、頭文字が大文字の「Conversational Language Understanding」となり、略語「(CLU)」が追加されました。この変更は、用語の一貫性や明確性を高め、ユーザーがドキュメントの内容をより理解しやすくすることを目的としています。全体として、ドキュメントの内容は変わっていませんが、表現が改良され、より正式な表現になっています。

## articles/ai-services/language-service/conversational-language-understanding/prebuilt-component-reference.md{#item-5af620}

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
 ms.custom: language-service-clu
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントの日付更新"
}
```

### Explanation
この変更は、Microsoft Azureの会話型言語理解に関するプレビルドコンポーネントのリファレンスドキュメントの日付を更新するものです。具体的には、ドキュメントの最終更新日が「2024年11月21日」から「2025年6月4日」に変更されました。

このような日付の更新は、ドキュメントが最新の情報を反映していることを示し、ユーザーに正確な内容を提供するために重要です。変更自体は日付のみで、文書の内容や構造には影響していませんが、更新された日付によって、ユーザーは情報の新鮮さを判断する際の手助けとなります。

## articles/ai-services/language-service/conversational-language-understanding/service-limits.md{#item-0c7212}

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
 ms.custom: language-service-clu, references_regions
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス制限ドキュメントの日付更新"
}
```

### Explanation
この変更は、Microsoft Azureの会話型言語理解に関連するサービス制限に関するドキュメントの最終更新日を修正するものです。具体的には、日付が「2024年11月21日」から「2025年6月4日」に変更されました。

この種の日付更新は、ドキュメントが最新の状態であることを示す重要なステップです。変更には他に内容や構造に影響する部分はなく、ユーザーに正確で最新の情報を提供するためのものです。この更新により、読者は文書の情報が新しいものであると認識しやすくなります。

## articles/ai-services/language-service/conversational-language-understanding/tutorials/bot-framework.md{#item-3415a0}

<details>
<summary>Diff</summary>
````diff
@@ -5,10 +5,9 @@ keywords: conversational language understanding, bot framework, bot, language un
 author: laujan
 ms.author: lajanuar
 manager: nitinme
-ms.reviewer: cahann, hazemelh
 ms.service: azure-ai-language
 ms.topic: tutorial
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ---
 
 # Integrate conversational language understanding with Bot Framework
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ボットフレームワークチュートリアルの日付とレビュー担当者の更新"
}
```

### Explanation
この変更は、会話型言語理解とボットフレームワークに関するチュートリアル記事の修正です。具体的には、以下の2点が変更されました。

1. ドキュメントの最終更新日が「2024年11月21日」から「2025年6月4日」に変更されました。
2. レビュー担当者の情報が削除されました。

日付の更新は、文書が最新の情報を反映していることを示し、利用者にとって重要です。また、レビュー担当者の削除は、プロジェクトの管理や運用の変更を示す可能性があります。このような修正によって、ユーザーは情報の新鮮さと関連性を確保しやすくなります。

## articles/ai-services/language-service/language-detection/how-to/call-api.md{#item-82812f}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.author: lajanuar
 ms.custom: language-service-language-detection
 ---
@@ -49,7 +49,7 @@ Analysis is performed upon receipt of the request. Using the language detection
 
 When you get results from language detection, you can stream the results to an application or save the output to a file on the local system.
 
-Language detection will return one predominant language for each document you submit, along with it's [ISO 639-1](https://www.iso.org/standard/22109.html) name, a human-readable name, a confidence score, script name and script code according to the [ISO 15924 standard](https://wikipedia.org/wiki/ISO_15924). A positive score of 1 indicates the highest possible confidence level of the analysis.
+Language detection will return one predominant language for each document you submit, along with it's [ISO 639-1](https://www.iso.org/standard/22109.html) name, a human-readable name, a confidence score, script name, and script code according to the [ISO 15924 standard](https://wikipedia.org/wiki/ISO_15924). A positive score of 1 indicates the highest possible confidence level of the analysis.
 
 
 ### Ambiguous content
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "API呼び出し手順書の日付更新と文法修正"
}
```

### Explanation
この変更は、言語検出に関するAPIの呼び出し手順書の修正です。主な変更点は以下の通りです。

1. ドキュメントの最終更新日が「2024年11月21日」から「2025年6月4日」に変更されました。
2. 文中の文法的な修正が行われ、「script name and script code」という表現にコンマが追加されました。

日付の更新は、ドキュメントの鮮度を反映させる重要な要素であり、ユーザーに最新の情報を提供します。また、文法の修正により、内容がより明確で理解しやすくなっています。このような変更は、ユーザーが言語検出APIの利用方法を正しく理解するのに役立ちます。

## articles/ai-services/language-service/personally-identifiable-information/language-support.md{#item-d332b1}

<details>
<summary>Diff</summary>
````diff
@@ -6,14 +6,14 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.author: lajanuar
 ms.custom: language-service-pii, build-2024
 ---
 
 # Personally Identifiable Information (PII) detection language support 
 
-Use this article to learn which natural languages are supported by the text PII, document PII, and conversation PII features of Azure AI Language.
+Use this article to learn which natural languages are supported by the text PII, document PII, and conversation PII features of Azure AI Language Service.
 # [Text PII](#tab/text)
 
 ## Text PII language support
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PII検出の言語サポートに関する更新"
}
```

### Explanation
この変更は、個人を特定できる情報（PII）検出に関する言語サポートの記事の修正です。主な変更内容は以下の通りです。

1. ドキュメントの最終更新日が「2024年11月21日」から「2025年6月4日」に更新されました。
2. Azure AI Languageの機能に関する表現が、「Azure AI Language」の「Service」に変更され、より正確な表記になりました。

日付の更新は情報の新鮮さを保つために重要であり、最新のリソースをユーザーに提供することに寄与します。また、サービス名の正確な表記は、利用者が正しい情報を基にサービスを利用できるようにするための重要な要素です。これにより、個人を特定できる情報の検出機能に関する理解が促進されることになります。

## articles/ai-services/language-service/question-answering/concepts/confidence-score.md{#item-e1fec0}

<details>
<summary>Diff</summary>
````diff
@@ -1,20 +1,20 @@
 ---
-title: Confidence score - custom question answering
+title: Confidence score - Custom question answering
 titleSuffix: Azure AI services
-description: When a user query is matched against a knowledge base, custom question answering returns relevant answers, along with a confidence score.
+description: When a user query is matched against a knowledge base, Custom question answering returns relevant answers, along with a confidence score.
 #services: cognitive-services
 manager: nitinme
 author: laujan
 ms.author: lajanuar
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.custom: language-service-question-answering
 ---
 
 # Confidence score
 
-When a user query is matched against a project (also known as a knowledge base), custom question answering returns relevant answers, along with a confidence score. This score indicates the confidence that the answer is the right match for the given user query.
+When a user query is matched against a project (also known as a knowledge base), Custom question answering returns relevant answers, along with a confidence score. This score indicates the confidence that the answer is the right match for the given user query.
 
 The confidence score is a number between 0 and 100. A score of 100 is likely an exact match, while a score of 0 means, that no matching answer was found. The higher the score- the greater the confidence in the answer. For a given query, there could be multiple answers returned. In that case, the answers are returned in order of decreasing confidence score.
 
@@ -31,7 +31,7 @@ The following table indicates typical confidence associated for a given score.
 
 ## Choose a score threshold
 
-The table above shows the range of scores that can occur when querying with custom question answering. However, since every project is different, and has different types of words, intents, and goals- we recommend you test and choose the threshold that best works for you. By default the threshold is set to `0`, so that all possible answers are returned. The recommended threshold that should work for most projects, is **50**.
+The table above shows the range of scores that can occur when querying with Custom question answering. However, since every project is different, and has different types of words, intents, and goals- we recommend you test and choose the threshold that best works for you. By default the threshold is set to `0`, so that all possible answers are returned. The recommended threshold that should work for most projects, is **50**.
 
 When choosing your threshold, keep in mind the balance between **Accuracy** and **Coverage**, and adjust your threshold based on your requirements.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム質問応答の信頼性スコアに関する表現の修正"
}
```

### Explanation
この変更は、カスタム質問応答における信頼性スコアに関する記事の修正です。主な変更点は以下の通りです。

1. 記事のタイトルにおいて「custom question answering」が「Custom question answering」に変更され、文中でも同様の修正が行われました。これにより、表記の一貫性が向上しています。
2. ドキュメントの最終更新日が「2024年11月21日」から「2025年6月4日」に更新され、最新の情報が提供されています。
3. 信頼性スコアの説明文に文法的な調整が施され、より明確で理解しやすい内容となっています。

これらの変更は、ユーザーがカスタム質問応答機能を利用する際に、信頼性スコアの意味や重要性をよりよく理解できるようにすることを目的としています。文書の一貫性と正確性が改善されたことで、ユーザーにとっての利便性が向上しています。

## articles/ai-services/language-service/question-answering/how-to/migrate-qnamaker-to-question-answering.md{#item-93cb3f}

<details>
<summary>Diff</summary>
````diff
@@ -6,10 +6,10 @@ ms.author: lajanuar
 author: laujan
 ms.manager: nitinme
 ms.topic: how-to
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.custom: language-service-question-answering
 ---
-# Migrate from QnA Maker to custom question answering 
+# Migrate from QnA Maker to Custom question answering 
 
 **Purpose of this document:** This article aims to provide information that can be used to successfully migrate applications that use QnA Maker to custom question answering. Using this article, we hope customers gain clarity on the following: 
 
@@ -23,7 +23,7 @@ ms.custom: language-service-question-answering
 **Intended Audience:** Existing QnA Maker customers
 
 > [!IMPORTANT]
-> Custom question Answering, a feature of Azure AI Language was introduced in November 2021 with several new capabilities including enhanced relevance using a deep learning ranker, precise answers, and end-to-end region support. Each custom question answering project is equivalent to a knowledge base in QnA Maker. Resource level settings such as Role-based access control (RBAC) aren't migrated to the new resource. These resource level settings would have to be reconfigured for the language resource post migration:
+> Custom question Answering, a feature of Azure AI Language was introduced in November 2021 with several new capabilities including enhanced relevance using a deep learning ranker, precise answers, and end-to-end region support. Each Custom question answering project is equivalent to a knowledge base in QnA Maker. Resource level settings such as Role-based access control (RBAC) aren't migrated to the new resource. These resource level settings would have to be reconfigured for the language resource post migration:
 >
 >  - Automatic RBAC to Language project (not resource)
 >  - Automatic enabling of analytics.
@@ -113,7 +113,7 @@ This topic compares two hypothetical scenarios when migrating from QnA Maker to
 > An attempt has been made to ensure these scenarios are representative of real customer migrations, however, individual customer scenarios differ. Also, this article doesn't include pricing details. Visit the [pricing](https://azure.microsoft.com/pricing/details/cognitive-services/language-service/) page for more information.
 
 > [!IMPORTANT] 
-> Each custom question answering project is equivalent to a knowledge base in QnA Maker. Resource level settings such as Role-based access control (RBAC) aren't migrated to the new resource. These resource level settings would have to be reconfigured for the language resource post migration. You'll also need to [re-enable analytics](analytics.md) for the language resource.
+> Each Custom question answering project is equivalent to a knowledge base in QnA Maker. Resource level settings such as Role-based access control (RBAC) aren't migrated to the new resource. These resource level settings would have to be reconfigured for the language resource post migration. You'll also need to [re-enable analytics](analytics.md) for the language resource.
 
 ### Migration scenario 1: No custom authoring portal
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "QnA Makerからカスタム質問応答への移行に関する表現の修正"
}
```

### Explanation
この変更は、QnA Makerからカスタム質問応答へ移行する方法に関する記事の修正です。主な変更点は以下の通りです。

1. ドキュメントの最終更新日が「2024年11月21日」から「2025年6月4日」に更新され、最新の情報が反映されました。
2. タイトルにおいて「custom question answering」が「Custom question answering」に変更され、文中でもこの修正が適用されています。これにより、表記の一貫性が確保されています。
3. 重要な注意点のセクションでは、カスタム質問応答プロジェクトがQnA Makerのナレッジベースに相当することや、リソースレベルの設定が新しいリソースに移行されないことについての説明が整理され、明確性が向上しています。

これらの変更は、QnA Makerからカスタム質問応答への移行手順を理解するために必要な情報をより分かりやすく提供することを目的としています。また、ユーザーが移行プロセスにおいて考慮すべき重要なポイントを明確にすることで、混乱を避ける手助けをしています。

## articles/ai-services/language-service/question-answering/how-to/migrate-qnamaker.md{#item-0646f1}

<details>
<summary>Diff</summary>
````diff
@@ -5,13 +5,13 @@ ms.service: azure-ai-language
 ms.topic: how-to
 ms.author: lajanuar
 author: laujan
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.custom: language-service-question-answering
 ---
 
 # Migrate from QnA Maker knowledge bases to custom question answering
 
-Custom question answering, a feature of Azure AI Language was introduced in May 2021 with several new capabilities including enhanced relevance using a deep learning ranker, precise answers, and end-to-end region support. Each custom question answering project is equivalent to a knowledge base in QnA Maker. You can easily migrate knowledge bases from a QnA Maker resource to custom question answering projects within a [language resource](https://aka.ms/create-language-resource). You can also choose to migrate knowledge bases from multiple QnA Maker resources to a specific language resource.
+Custom question answering, a feature of Azure AI Language was introduced in May 2021 with several new capabilities including enhanced relevance using a deep learning ranker, precise answers, and end-to-end region support. Each Custom question answering project is equivalent to a knowledge base in QnA Maker. You can easily migrate knowledge bases from a QnA Maker resource to custom question answering projects within a [language resource](https://aka.ms/create-language-resource). You can also choose to migrate knowledge bases from multiple QnA Maker resources to a specific language resource.
 
 To successfully migrate knowledge bases, **the account performing the migration needs contributor access to the selected QnA Maker and language resource**. When a knowledge base is migrated, the following details are copied to the new custom question answering project:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "QnA Makerからカスタム質問応答への移行に関する表現の修正"
}
```

### Explanation
この変更は、QnA Makerのナレッジベースからカスタム質問応答への移行に関する記事の修正です。主な変更点は以下の通りです。

1. ドキュメントの最終更新日が「2024年11月21日」から「2025年6月4日」に更新され、最新の情報が反映されています。
2. 記事内の特定の表現が修正され、「custom question answering」の表記が「Custom question answering」に変更され、用語の一貫性が向上しました。

これらの変更は、QnA Makerからカスタム質問応答へ移行する際の手順と条件について、明確さを提供し、読者が必要な情報を容易に理解できるようにすることを目的としています。特に、移行を行うアカウントに必要なアクセス権限についての重要な情報が明確に示されています。

## articles/ai-services/language-service/question-answering/tutorials/active-learning.md{#item-e8486d}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,11 @@
 ---
 title: Enrich your project with active learning
-description: In this tutorial, learn how to enrich your custom question answering projects with active learning
+description: In this tutorial, learn how to enrich your Custom question answering projects with active learning
 ms.service: azure-ai-language
 ms.topic: tutorial
 author: laujan
 ms.author: lajanuar
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.custom: language-service-question-answering
 ---
 
@@ -20,13 +20,13 @@ In this tutorial, you learn how to:
 > * Accept/reject active learning suggestions
 > * Add alternate questions
 
-This tutorial shows you how to enhance your custom question answering project with active learning. If you notice that customers are asking questions that are not covered in your project, they may be paraphrased variations of questions.
+This tutorial shows you how to enhance your Custom question answering project with active learning. If you notice that customers are asking questions that are not covered in your project, they may be paraphrased variations of questions.
 
 These variations, when added as alternate questions to the relevant question answer pair, help to optimize the project to answer real world user queries. You can manually add alternate questions to question answer pairs through the editor. At the same time, you can also use the active learning feature to generate active learning suggestions based on user queries. The active learning feature, however, requires that the project receives regular user traffic to generate suggestions.
 
 ## Use active learning
 
-Active learning is turned on by default for custom question answering enabled resources.
+Active learning is turned on by default for Custom question answering enabled resources.
 
 To try out active learning suggestions, you can import the following file as a new project: [SampleActiveLearning.tsv](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/qna-maker/knowledge-bases/SampleActiveLearning.tsv).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アクティブ学習を活用したカスタム質問応答プロジェクトの強化に関する修正"
}
```

### Explanation
この変更は、アクティブ学習を用いてカスタム質問応答プロジェクトを強化する方法に関する記事の修正です。主な変更点は以下の通りです。

1. ドキュメントの最終更新日が「2024年11月21日」から「2025年6月4日」に更新され、最新の情報が反映されています。
2. 記事内の表現が見直され、「custom question answering」の表記が「Custom question answering」に変更され、用語の一貫性が向上しています。
3. 記事の説明部分において、アクティブ学習の必要性とその導入方法が明確に説明されています。

これらの変更は、アクティブ学習機能を活用してカスタム質問応答プロジェクトを最適化し、より実世界のユーザーの質問に的確に応えるための情報を提供することを目的としています。特に、ユーザーのクエリに基づいた提案生成の必要性や、これを実現するための条件について明確に記述されています。

## articles/ai-services/language-service/question-answering/tutorials/guided-conversations.md{#item-a43dd4}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-language
 ms.topic: tutorial
 author: laujan
 ms.author: lajanuar
-ms.date: 11/21/2024
+ms.date: 06/04/2025
 ms.custom: language-service-question-answering
 ---
 
@@ -63,7 +63,7 @@ Using the editor, we add a new QnA pair with a follow-up prompt by clicking on *
     > [!div class="mx-imgBorder"]
     > [ ![Screenshot of UI with "add a follow-up prompt" highlighted in a red box]( ../media/guided-conversations/add-prompts.png) ]( ../media/guided-conversations/add-prompts.png#lightbox)
     
-    We provide **Check Compatibility** as the “Display text” for the prompt and try to link it to a QnA. Since, no related QnA pair is available to link to the prompt, when we search “Check your Surface Pen Compatibility”, we create a new question pair by clicking on **Create link to new pair** and select **Done**. Then select **Save changes**.
+    We provide **Check Compatibility** as the "Display text" for the prompt and try to link it to a QnA. Since, no related QnA pair is available to link to the prompt, when we search “Check your Surface Pen Compatibility”, we create a new question pair by clicking on **Create link to new pair** and select **Done**. Then select **Save changes**.
     
     > [!div class="mx-imgBorder"]
     > [ ![Screenshot of a question and answer about checking your surface pen compatibility]( ../media/guided-conversations/compatability-check.png) ]( ../media/guided-conversations/compatability-check.png#lightbox)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ガイド付き対話に関するチュートリアルの表現修正"
}
```

### Explanation
この変更は、ガイド付き対話に関するチュートリアルの記事の修正です。主な変更点は以下の通りです。

1. ドキュメントの最終更新日が「2024年11月21日」から「2025年6月4日」に更新され、コンテンツが最新の状態となりました。
2. 記事内の特定の表現が明確にされ「Display text」が引用符に囲まれる形に修正され、より読みやすくなりました。

これらの変更は、ガイド付き対話の設定手順を説明する際に、一貫した表現を使うことで読者の理解を促進することを目的としています。また、操作手順を従う際の混乱を避けるために、明確さを追求しています。特に、QnAペアの作成手順やその関連付けの詳細が強調されています。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -16,6 +16,14 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 
 ## May 2025
 
+##### 2025-05-15-preview release
+
+The [latest API preview version](/rest/api/language/operation-groups?view=rest-language-2025-05-15-preview&preserve-view=true) includes updates for named entity recognition (NER) and PII detection:
+
+* New entity type support for `DateOfBirth`, `BankAccountNumber`, `PassportNumber`, and `DriversLicenseNumber`.
+
+* Improved AI quality for `PhoneNumber` entity type.
+
 ##### New agent templates 
 
 Azure AI Language now supports the following agent templates:
@@ -34,16 +42,19 @@ Azure AI Language introduces new customization and entity subtype features for P
 
 *  [Use entity synonyms for tailored PII detection](personally-identifiable-information/how-to/adapt-to-domain-pii.md#api-schema-for-the-entitysynoyms-parameter).
 
-##### 2025-05-15-preview release. 
+##### Enhanced CLU and CQA Capabilities in Azure AI Foundry
 
-The [latest API preview version](/rest/api/language/operation-groups?view=rest-language-2025-05-15-preview&preserve-view=true) includes updates for named entity recognition (NER) and PII detection:
+Azure AI Foundry now offers enhanced capabilities for fine-tuning with custom conversational language understanding (CLU) and conversational question-and-answer (CQA) AI features:
 
-* New entity type support for `DateOfBirth`, `BankAccountNumber`, `PassportNumber`, and `DriversLicenseNumber`.
+*	CLU and CQA authoring tools are now available in Azure AI Foundry.
+  
+*	CLU offers a quick deploy option powered by large language models (LLMs) for rapid deployment.
 
-* Improved AI quality for `PhoneNumber` entity type.
+*	CQA incorporates the QnA Maker scoring algorithm for more accurate responses.
 
-To learn more, see our latest [TechCommunity Blog Post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-azure-ai-language-new-features-to-accelerate-your-agent-development/4415216).
+*	CQA enables exact match answering for precise query resolutions.
 
+###### For more updates, see our latest [TechCommunity Blog Post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-azure-ai-language-new-features-to-accelerate-your-agent-development/4415216).
 
 ## April 2025
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Languageの最新機能と強化内容の更新"
}
```

### Explanation
この変更は、Azure AI Languageに関する「最新情報」セクションの修正です。主な変更点は以下の通りです。

1. 2025年5月15日のプレビューリリースに関する新しい情報が追加され、名前付きエンティティ認識（NER）と個人識別情報（PII）検出の更新が強調されています。具体的には、新たにサポートされたエンティティタイプ（生年月日、銀行口座番号、パスポート番号、運転免許証番号）や、電話番号エンティティタイプのAI品質の向上が記載されています。

2. Azure AI Foundryにおける対話型言語理解（CLU）と対話型質問応答（CQA）の強化機能に関する詳細が追加され、これには新しい著作ツール、迅速なデプロイオプション、大規模言語モデル（LLM）を活用した機能、正確な応答を提供するためのQnA Makerスコアリングアルゴリズムの採用が含まれています。

3. 最新情報に対する参照として、テクコミュニティのブログ投稿へのリンクも更新されており、新機能およびエージェント開発加速に関する情報が提供されています。

これらの変更は、ユーザーが最新機能や強化された能力について迅速にアクセスできるようにすることを目的とし、Azure AI Languageの進化に関する理解を深める手助けとなります。


