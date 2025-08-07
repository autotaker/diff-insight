---
date: '2025-08-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:10d2435...MicrosoftDocs:09b644a
summary: このコードの変更は、ドキュメントインテリジェンスと言語サービスにおける入力要件とドキュメント内容を向上させ、最新情報を提供することを目的としています。新機能として、トレーニングデータの明確な要件や制限が追加され、多様なファイル形式を扱う際のデータ制限が明確化されました。また、.NET
  SDKでのAPIサポートが拡張されています。破壊的な変更はないものの、セクション名の変更によりユーザーに一時的な混乱が生じる可能性があります。目次ファイルの整理や新機能情報の追加により、ユーザーは必要な情報に迅速にアクセスできるようになっています。この更新は、AzureのAIサービスの機能性とユーザビリティを向上させ、企業にとっての利用価値を高めることを目指しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:10d2435...MicrosoftDocs:09b644a){target="_blank"}

# ハイライト
このコードの変更は、ドキュメントインテリジェンスと言語サービスの分野において、特定の入力要件とドキュメント内容を改善し、最新情報を提供することを目的としています。

## 新機能
- トレーニングデータの明確な要件と制限が追加され、特にカスタム抽出モデルとカスタム分類モデルの最大データサイズに関する情報が更新されました。
- 新しいオフィスファイルタイプにキャップが設けられたことで、多様なファイル形式を扱う際のデータ制限が明確化されました。
- .NET SDKでのAPIサポートが拡張され、新しい著作権APIに関する情報が更新されました。

## 破壊的変更
特に破壊的な変更はありませんが、整理によってセクション名が大幅に変更されたため、以前のバージョンに慣れていたユーザーは一時的な混乱を経験する可能性があります。

## その他のアップデート
- 目次ファイルの表示名と項目が整理され、より統一された文書ナビゲーションが可能になりました。
- 2025年7月の新機能情報がAzure AI Languageの「What's New」ページに追加されました。

# 洞察
この更新は、AzureのAIサービスが提供する機能性とユーザビリティを向上させるためのものです。特に、Azureの主要なAIサービスであるドキュメントインテリジェンスと言語サービスにおける重要な要件や制限を見直し、ドキュメントとしての信頼性を高めています。

入力要件に関する更新は、使用されるトレーニングモデルのパフォーマンスと信頼性を向上させるためのものです。特に、データサイズの上限を明確化することで、開発者がより効率的にモデルを選択し、最適なトレーニングデータを供給できるようにする意図があります。

目次ファイルの整頓と新機能の増強により、ユーザーが必要な情報に迅速にアクセスできる環境が整えられています。この一連の変更により、AzureのAIサービスは競争力を維持し続け、特に業務でAI技術を利用する企業にとっての利用価値をさらに高めています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [input-requirements.md](#item-20011c) | minor update | 入力要件の更新: 日付とトレーニングデータの上限に関する情報の追加 | modified | 5 | 3 | 8 | 
| [toc.yml](#item-12f1f0) | minor update | 目次ファイルの更新: セクション名と表示名の整理 | modified | 52 | 49 | 101 | 
| [whats-new.md](#item-69b272) | minor update | 新機能の追加: 2025年7月の更新情報 | modified | 16 | 1 | 17 | 


# Modified Contents
## articles/ai-services/document-intelligence/includes/input-requirements.md{#item-20011c}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,7 @@
 author: laujan
 ms.service: azure-ai-document-intelligence
 ms.topic: include
-ms.date: 11/19/2024
+ms.date: 08/05/2025
 ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD041 -->
@@ -32,6 +32,8 @@ Supported file formats:
 
 * For custom model training, the maximum number of pages for training data is 500 for the custom template model and 50,000 for the custom neural model.
 
-  * For custom extraction model training, the total size of training data is 50 MB for template model and `1` GB for the neural model.
+* For custom extraction model training, the total size of training data is 50 MB for template model and `1` GB for the neural model.
 
-  * For custom classification model training, the total size of training data is `1` GB  with a maximum of 10,000 pages. For 2024-11-30 (GA), the total size of training data is `2` GB with a maximum of 10,000 pages.
+* For custom classification model training, the total size of training data is `1` GB  with a maximum of 10,000 pages. For `2024-11-30` (GA), the total size of training data is `2` GB with a maximum of 10,000 pages.
+    
+* For office file types (docx, xlsx, pptx), there's a maximum string length limit of 8,000,000 characters.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "入力要件の更新: 日付とトレーニングデータの上限に関する情報の追加"
}
```

### Explanation
この変更は、ドキュメントのメタデータと特定のトレーニングデータに関する要件を更新したものです。具体的には、最初の行で日付が2024年11月19日から2025年8月5日に変更され、最新の日付を反映しています。

さらに、特定のトレーニングモデルに関する情報が修正され、カスタム抽出モデルとカスタム分類モデルのトレーニングデータの要件が強調されています。カスタム抽出モデルのトレーニングでは、テンプレートモデルの最大データサイズが50MBであり、神経モデルの最大データサイズが1GBであることが確認されました。また、カスタム分類モデルのトレーニングに関する要件も明確化され、最大のトレーニングデータサイズが1GBで、特定の日付（2024年11月30日）においては2GBに増加することが記載されています。

最後に、新たにオフィスファイルタイプ（docx, xlsx, pptx）に関して、最大文字列長の制限が800万文字であることが追加され、これによりユーザーはさまざまなファイル形式におけるデータ制限を認識できるようになります。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -3,6 +3,7 @@ items:
   href: index.yml
 - name: Overview
   expanded: true
+  displayName: introduction, getting started, what is azure ai language
   items:
   - name: What is Azure AI Language?
     href: overview.md
@@ -25,16 +26,16 @@ items:
   items:
   - name: Custom text classification
     items:
-    - name: Custom text classification overview
+    - name: Overview
       href: custom-text-classification/overview.md
-      displayName: ctc
-    - name: Custom text classification quickstart
+      displayName: ctc, custom text classification, custom classification, text classifier
+    - name: Quickstart
       href: custom-text-classification/quickstart.md
       displayName: ctc setup
-    - name: Custom text classification language support
+    - name: Language support
       href: custom-text-classification/language-support.md
       displayName: ctc languages, multilingual
-    - name: Custom text classification FAQ
+    - name: FAQ
       href: custom-text-classification/faq.md
       displayName: ctc faq, troubleshooting
     - name: Responsible use of AI
@@ -112,16 +113,16 @@ items:
         displayName: quotas, restrictions, service boundaries
   - name: Conversational language understanding
     items:
-    - name: Conversational language understanding overview
+    - name: Overview
       href: conversational-language-understanding/overview.md
-      displayName: clu, conversational ai, intent recognition, entity extraction
-    - name: Conversational language understanding quickstart
+      displayName: clu, conversational language understanding, intent recognition, entity extraction
+    - name: Quickstart
       href: conversational-language-understanding/quickstart.md
       displayName: getting started, tutorial, conversational ai setup
-    - name: Conversational language understanding language support
+    - name: Language support
       href: conversational-language-understanding/language-support.md
       displayName: clu languages, supported languages, multilingual, international support
-    - name: Conversational language understanding FAQ
+    - name: FAQ
       href: conversational-language-understanding/faq.md
       displayName: frequently asked questions, troubleshooting, common issues
     - name: Responsible use of AI
@@ -216,12 +217,12 @@ items:
         href: conversational-language-understanding/glossary.md
   - name: Entity linking
     items:
-    - name: Entity linking overview
+    - name: Overview
       href: entity-linking/overview.md
-      displayName: knowledge base linking, disambiguation
-    - name: Entity linking quickstart
+      displayName: entity linking,knowledge base linking, disambiguation
+    - name: Quickstart
       href: entity-linking/quickstart.md
-    - name: Entity linking language support
+    - name: Language support
       href: entity-linking/language-support.md
     - name: Responsible use of AI
       items:
@@ -238,12 +239,12 @@ items:
           displayName: entity linking, entity recognition
   - name: Language detection
     items:
-    - name: Language detection overview
+    - name: Overview
       href: language-detection/overview.md
-      displayName: language identification, automatic detection
-    - name: Language detection quickstart
+      displayName: language detection, language identification, automatic detection
+    - name: Quickstart
       href: language-detection/quickstart.md
-    - name: Language detection language support
+    - name: Language support
       href: language-detection/language-support.md
     - name: Responsible use of AI
       items:
@@ -274,12 +275,12 @@ items:
           href: ../cognitive-services-container-support.md
   - name: Key phrase extraction
     items:
-    - name: Key phrase extraction overview
+    - name: Overview
       href: key-phrase-extraction/overview.md
-      displayName: keyword extraction, key terms
-    - name: Key phrase extraction quickstart
+      displayName: key phrase extraction,keyword extraction, key terms
+    - name: Quickstart
       href: key-phrase-extraction/quickstart.md
-    - name: Key phrase extraction language support
+    - name: Language support
       href: key-phrase-extraction/language-support.md
     - name: Responsible use of AI
       items:
@@ -315,12 +316,12 @@ items:
         displayName: business intelligence, data visualization
   - name: Named Entity Recognition (NER)
     items:
-    - name: NER overview
+    - name: Overview
       href: named-entity-recognition/overview.md
-      displayName: ner introduction, entity extraction
-    - name: NER quickstart
+      displayName: named entity recognition, introduction, entity extraction
+    - name: Quickstart
       href: named-entity-recognition/quickstart.md
-    - name: NER language support
+    - name: Language support
       href: named-entity-recognition/language-support.md
     - name: Responsible use of AI
       items:
@@ -420,13 +421,14 @@ items:
             href: concepts/custom-features/project-versioning.md
   - name: Orchestration workflow
     items:
-    - name: Orchestration workflow overview
+    - name: Overview
       href: orchestration-workflow/overview.md
-    - name: Orchestration workflow quickstart
+      displayName: workflow orchestration, orchestration introduction, orchestration overview
+    - name: Quickstart
       href: orchestration-workflow/quickstart.md
-    - name: Orchestration workflow FAQ
+    - name: FAQ
       href: orchestration-workflow/faq.md
-    - name: Orchestration workflow language support
+    - name: Language support
       href: orchestration-workflow/language-support.md
     - name: How-to guides
       items:
@@ -475,12 +477,12 @@ items:
         href: orchestration-workflow/glossary.md
   - name: Personally Identifiable Information (PII) detection
     items:
-    - name: PII overview
+    - name: Overview
       href: personally-identifiable-information/overview.md
-      displayName: native document
-    - name: PII quickstart
+      displayName: personally identifiable information, document
+    - name: Quickstart
       href: personally-identifiable-information/quickstart.md
-    - name: PII language support
+    - name: Language support
       href: personally-identifiable-information/language-support.md
     - name: Responsible use of AI
       items:
@@ -523,12 +525,12 @@ items:
         href: personally-identifiable-information/concepts/conversations-entity-categories.md
   - name: Custom question answering
     items:
-    - name: Custom question answering overview
+    - name: Overview
       href: question-answering/overview.md
-      displayName: qna, faq, knowledge base
-    - name: Custom question answering quickstart
+      displayName: custom question answering, faq, knowledge base
+    - name: Quickstart
       href: question-answering/quickstart/sdk.md
-    - name: Custom question answering language support
+    - name: Language support
       href: question-answering/language-support.md
     - name: Responsible use of AI
       items:
@@ -629,11 +631,12 @@ items:
           href: question-answering/reference/document-format-guidelines.md
   - name: Sentiment analysis and opinion mining
     items:
-      - name: Sentiment analysis and opinion mining overview
+      - name: Overview
         href: sentiment-opinion-mining/overview.md
-      - name: Sentiment analysis and opinion mining quickstart
+        displayName: sentiment analysis introduction, opinion mining overview, sentiment detection
+      - name: Quickstart
         href: sentiment-opinion-mining/quickstart.md
-      - name: Sentiment analysis and opinion mining language support
+      - name: language-detection/how-to/use-containers.mdanguage support
         href: sentiment-opinion-mining/language-support.md
       - name: Responsible use of AI
         items:
@@ -668,12 +671,12 @@ items:
           href: /training/modules/python-flask-build-ai-web-app/
   - name: Text Analytics for health
     items:
-    - name: Text Analytics for health overview
+    - name: Overview
       href: text-analytics-for-health/overview.md
-      displayName: healthcare nlp, medical text analysis, clinical text, health entities
-    - name: Text Analytics for health quickstart
+      displayName: text analytics for health, healthcare nlp, medical text analysis, clinical text, health entities
+    - name: Quickstart
       href: text-analytics-for-health/quickstart.md
-    - name: Text Analytics for health language support
+    - name: Language support
       href: text-analytics-for-health/language-support.md
     - name: Responsible use of AI
       items:
@@ -712,12 +715,12 @@ items:
         href: text-analytics-for-health/concepts/fhir.md
   - name: Summarization
     items:
-    - name: Summarization overview
+    - name: Overview
       href: summarization/overview.md
-      displayName: native document
-    - name: Summarization quickstart
+      displayName: summarization,native document
+    - name: Quickstart
       href: summarization/quickstart.md
-    - name: Summarization language support
+    - name: Language support
       href: summarization/language-support.md
     - name: How-to guides
       items:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次ファイルの更新: セクション名と表示名の整理"
}
```

### Explanation
この変更は全体的に、目次ファイル（toc.yml）の項目名と表示名に対する整理を行ったもので、52行が追加され、49行が削除されました。主に、各セクションでの「Overview」や「Language support」といった項目名がより一貫性のある形に変更されています。

具体的には、各アイテム内での名前の標準化を目的とし、例えば「カスタムテキスト分類」の「概要」が単に「Overview」とされたり、言語サポートに関する部分が「Language support」と言い直されたりしています。また、ディスプレイ名（表示名）の部分も改良され、より明確な説明に寄与しています。例えば、「言語検出」の項目では、表示名が「language identification」や「automatic detection」のように具体的になりました。

これにより、ユーザーがリファレンスを閲覧する際に、各セクションの理解が深まるとともに、より明確で統一されたナビゲーション体験を提供できるようになっています。全体として、内容の可読性と使いやすさが向上しました。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -14,9 +14,24 @@ ms.author: lajanuar
 
 Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up to date with release notes, feature enhancements, and our newest documentation.
 
+## July 2025
+
+ **Expanded .NET SDK support for text and conversation authoring APIs**:
+
+  * [**Azure.AI.Language.Text.Authoring `1.0.0-beta.2`**](https://www.nuget.org/packages/Azure.AI.Language.Text.Authoring/1.0.0-beta.2) now supports project import with raw JSON string for custom NER and custom text classification.
+
+  * [**Azure.AI.Language.Conversation.Authoring `1.0.0-beta.2`**](https://www.nuget.org/packages/Azure.AI.Language.Conversations.Authoring/1.0.0-beta.2) introduces new authoring capabilities in the `2025-15-05-preview` API, including LLM-based CLU intent authoring, a quick-deploy feature, and multi-turn CLU model training with autogenerated synthetic data.
+
+  * [**Azure.AI.Language.Text.Authoring `1.0.0-beta.2`**](https://www.nuget.org/packages/Azure.AI.Language.Text.Authoring/1.0.0-beta.2) and [**Azure.AI.Language.Conversation.Authoring `1.0.0-beta.2`**](https://www.nuget.org/packages/Azure.AI.Language.Conversations.Authoring/1.0.0-beta.2) .NET SDK versions support the following [REST APIs](/rest/api/language/):
+
+    * `2025-15-05-preview` (latest/default)
+    * `2023-04-01`
+    * `2023-04-15-preview`
+    * `2024-11-15-preview`
+
 ## June 2025
 
-**New version of the Conversational Language Understanding (CLU) training configuration**. This new version is aimed at minimizing overpredictions of the [None intent](conversational-language-understanding/concepts/none-intent.md)—particularly in multilingual contexts—is now available via the REST API using **trainingConfigVersion 2025-07-01-preview**. For more information, *see* [Train your model: request body data](conversational-language-understanding/how-to/train-model.md?tabs=rest-api#request-body).
+**New version of the Conversational Language Understanding (CLU) training configuration**. This new version is aimed at minimizing over-predictions of the [None intent](conversational-language-understanding/concepts/none-intent.md)—particularly in multilingual contexts—is now available via the REST API using **trainingConfigVersion 2025-07-01-preview**. For more information, *see* [Train your model: request body data](conversational-language-understanding/how-to/train-model.md?tabs=rest-api#request-body).
 
 **Updated [Build your conversational agent](https://github.com/Azure-Samples/Azure-Language-OpenAI-Conversational-Agent-Accelerator) accelerator project**. The update includes a new routing strategy—**TRIAGE_AGENT**. This strategy uses an agent hosted on Azure AI Foundry Agent Service. It utilizes Conversational Language Understanding (CLU) and Custom Question Answering (CQA) as tools to triage user intent for downstream agent routing. Additionally, these tools help deliver precise answers to specific questions. For more information, *see* [TechCommunity Blog Post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-azure-ai-language-new-features-to-accelerate-your-agent-development/4415216)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能の追加: 2025年7月の更新情報"
}
```

### Explanation
この変更は、Azure AI Languageの「What's New」ページに2025年7月の新機能に関する情報を追加したものです。具体的には、16行が追加され、1行が削除されました。新しい情報は、主に.NET SDKのサポートの拡張と新しい機能の紹介に関するものです。

新機能として、以下のポイントが強調されています：

- **テキストおよび会話の著作権APIに対する.NET SDKの拡張サポート**が導入されました。特に、カスタムのNER（Named Entity Recognition）やカスタムテキスト分類のために、生JSON文字列を使用したプロジェクトのインポートが可能になったことが記載されています。

- **新しい著作権機能**が含まれる「Azure.AI.Language.Conversation.Authoring」のバージョンが紹介されています。このAPIは、LLMに基づくCLU（Conversational Language Understanding）意図の著作権作成、クイックデプロイ機能、および自動生成された合成データを使用したマルチターンCLUモデルのトレーニングをサポートします。

- 複数のREST APIバージョンが.NET SDKでサポートされるようになりました。これにより、さまざまなAPIバージョンが利用可能になり、開発者が最新の機能を簡単に利用できる環境が整いました。

また、2025年6月の情報も更新されており、Conversational Language Understanding（CLU）のトレーニング設定の新しいバージョンが、REST APIを介して利用できるようになったことが強調されています。この設定は多言語コンテキストにおける「None intent」の過剰予測を最小化することを目的としています。

全体として、この変更はAzure AI Languageの機能強化を示しており、ユーザーが最新の情報にアクセスできるよう努めています。


