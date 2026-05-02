---
date: '2026-05-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c2a4792...MicrosoftDocs:a9b4c3d
summary: このコードの変更は、Azure Languageサービスのドキュメントに対するマイナーな更新です。変更により、ドキュメントが最新の機能とリソースを反映し、情報構造が整理されてユーザーへのアクセスが分かりやすくなっています。新たなセクションが追加され、PII検出、エンティティ認識、カスタムモデルの構築、医療文書の分析といった新しい能力が紹介されています。特に破壊的変更はありませんが、ドキュメントのタイトルや要約が変更され、一部のコンテンツが削除されて、情報構造が改善されています。これにより、Azure
  Languageサービスを利用するユーザーが効率的に情報を取得できるようになり、サービスの多様な機能を活用するための道が開かれています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c2a4792...MicrosoftDocs:a9b4c3d){target="_blank"}

<format>
# ハイライト
このコードの変更は、Azure Languageサービスのドキュメントに対するマイナーな更新です。変更により、ドキュメントが最新の機能とリソースを反映するようになり、情報構造の整理とともにユーザーへのアクセスが分かりやすくなっていることが強調されています。

## 新機能
- ドキュメントに新たなセクションの追加。
- PII検出、エンティティ認識、カスタムモデルの構築、医療文書の分析といった新しい能力の紹介。

## 破壊的変更
特になし。

## その他の更新
- ドキュメントのタイトルと要約の変更。
- 一部コンテンツの削除、情報構造の整理によるわかりやすさの向上。

# 洞察
このドキュメントの更新は、Azure Languageサービスを利用するユーザーがより効率的に情報を取得し、サービスの多様な機能を活用するための道を開いています。特に、新たに追加された機能により、ユーザーが自然言語処理（NLP）ソリューションを開発・展開する際の柔軟性が高まっています。

PII（個人識別可能情報）検出やエンティティ認識といった機能の追加は、データセキュリティや情報抽出を重視する多くの業界にとって重要です。また、カスタムモデルの構築は、個々のニーズに合わせてサービスをカスタマイズする能力を拡張します。医療文書の分析機能も、ヘルスケア分野のニーズに対する対応を示しており、その応用範囲は非常に広がりを見せています。

このような更新をドキュメントに反映することで、Azure Languageサービスの価値を最大化しようとするMicrosoftの戦略が見て取れます。これにより、様々な開発者や企業が、自身のプロジェクトにAzureの自然言語機能をより簡単に適用できる環境を整えているといえます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index.yml](#item-c9444f) | minor update | Azure Languageドキュメントの更新 | modified | 202 | 90 | 292 | 


# Modified Contents
## articles/ai-services/language-service/index.yml{#item-c9444f}

<details>
<summary>Diff</summary>
````diff
@@ -1,114 +1,226 @@
 ### YamlMime:Hub
 
-title: Azure Language in Foundry Tools documentation
-summary: Learn how to integrate AI into your applications that can extract information, classify text, understand conversational language, answer questions and more.
+title: Azure Language documentation
+summary: Build and deploy natural language processing (NLP) solutions with prebuilt and customizable models for entity extraction, sentiment analysis, PII detection, classification, summarization, and healthcare text processing.
 brand: azure
 
 metadata:
-  title: Azure Language in Foundry Tools documentation - Tutorials, API Reference | Microsoft Docs
-  titleSuffix: Foundry Tools
-  description: Learn how to integrate AI that works on written text into your applications.
-  author: laujan
-  manager: nitinme
+  title: Azure Language documentation | Microsoft Docs
+  description: Create natural language processing (NLP) solutions with pre-trained and customizable models for semantic understanding, entity extraction, and text analysis.
   ms.service: azure-ai-language
   ms.topic: hub-page
-  ms.date: 04/01/2026
+  author: laujan
   ms.author: lajanuar
+  ms.date: 04/30/2026
 highlightedContent:
-# itemType: architecture | concept | deploy | download | get-started | how-to-guide | learn | overview | quickstart | reference | tutorial | whats-new
   items:
+    # Card
     - title: What is Azure Language in Foundry Tools?
       itemType: overview
       url: overview.md
-    - title: What's new?
+    # Card
+    - title: What's new in Azure Language?
       itemType: whats-new
       url: whats-new.md
+    # Card
+    - title: Language support
+      itemType: reference
+      url: concepts/language-support.md
+    # Card
     - title: Responsible use of AI
       itemType: concept
       url: /azure/ai-foundry/responsible-ai/language-service/transparency-note
 
 conceptualContent:
-  items:
-    - title: Extract information
-      summary: Use Natural Language Understanding (NLU) to extract information from unstructured text.
-      links:
-        - itemType: overview
-          text: Extract key phrases
-          url:  key-phrase-extraction/overview.md
-        - itemType: overview
-          text: Find linked entities
-          url:  entity-linking/overview.md 
-        - itemType: overview
-          text: Named Entity Recognition (NER)
-          url:  named-entity-recognition/overview.md
-        - itemType: overview
-          text: Personally Identifiable Information (PII) detection
-          url:  personally-identifiable-information/overview.md
-        - itemType: overview
-          text: Custom Named Entity Recognition (custom NER)
-          url:  custom-named-entity-recognition/overview.md
-        - itemType: overview
-          text: Text analytics for health
-          url:  text-analytics-for-health/overview.md
-    - title: Summarize text-based content
-      summary: Summarize lengthy documents and conversation transcripts.
-      links:
-      - itemType: overview
-        text: Document summarization
-        url: summarization/overview.md?tabs=document-summarization
-      - itemType: overview
-        text: Conversation summarization
-        url: summarization/overview.md?tabs=conversation-summarization
-    - title: Classify Text
-      summary: Use Natural Language Understanding (NLU) to detect the language or classify the sentiment of text you have. You can also classify your text documents by customizing a classification model over your dataset.
-      links:
-        - itemType: overview
-          text: Analyze sentiment and mine text for opinions
-          url: sentiment-opinion-mining/overview.md
-        - itemType: overview
-          text: Detect Language
-          url: language-detection/overview.md       
-        - itemType: overview
-          text: Custom text classification
-          url: custom-text-classification/overview.md  
+  sections:
+    - title: Core capabilities
+      summary: Use production-grade natural language processing (NLP) capabilities optimized for the latest platform architecture and engineering workflows.
+      items:
+
+        # Card
+        - title: Detect and redact sensitive information
+          summary: Detect, classify, and redact personally identifiable information (PII) across unstructured text, conversation transcripts, and document workflows.
+          links:
+            - url: personally-identifiable-information/overview.md
+              itemType: overview
+              text: PII detection overview
+            - url: personally-identifiable-information/text-pii-overview.md
+              itemType: overview
+              text: Text PII detection
+            - url: personally-identifiable-information/conversation-pii-overview.md
+              itemType: overview
+              text: Conversation PII detection
+            - url: personally-identifiable-information/document-based-pii-overview.md
+              itemType: overview
+              text: Document-based PII detection
+            - url: personally-identifiable-information/quickstart.md
+              itemType: quickstart
+              text: Get started with PII detection
+
+        # Card
+        - title: Recognize named entities
+          summary: Identify and classify entities such as people, organizations, locations, and dates using prebuilt recognition models.
+          links:
+            - url: named-entity-recognition/overview.md
+              itemType: overview
+              text: Named Entity Recognition (NER) overview
+            - url: named-entity-recognition/concepts/named-entity-categories.md
+              itemType: reference
+              text: Recognized entity categories
+            - url: named-entity-recognition/how-to-call.md
+              itemType: how-to-guide
+              text: Call the NER API
+            - url: named-entity-recognition/quickstart.md
+              itemType: quickstart
+              text: Get started with Named Entity Recognition
+
+        # Card
+        - title: Build a custom entity recognizer
+          summary: Train custom models to extract domain-specific entities using your own labeled data and entity schemas.
+          links:
+            - url: custom-named-entity-recognition/overview.md
+              itemType: overview
+              text: Custom named entity recognition (CNER) overview
+            - url: custom-named-entity-recognition/how-to/design-schema.md
+              itemType: how-to-guide
+              text: Design your entity schema
+            - url: custom-named-entity-recognition/how-to/train-model.md
+              itemType: how-to-guide
+              text: Train a model
+            - url: custom-named-entity-recognition/quickstart.md
+              itemType: quickstart
+              text: Get started with CNER
+
+        # Card
+        - title: Analyze healthcare documents 
+          summary: Extract clinical entities, relations, and assertions from biomedical and clinical narratives.
+          links:
+            - url: text-analytics-for-health/overview.md
+              itemType: overview
+              text: Text analytics for health overview
+            - url: text-analytics-for-health/concepts/health-entity-categories.md
+              itemType: reference
+              text: Health entity categories
+            - url: text-analytics-for-health/quickstart.md
+              itemType: quickstart
+              text: Get started with text analytics for health
+
+      # Card
+        - title: Detect language
+          summary: Automatically determine input language and script for multilingual processing pipelines.
+          links:
+            - url: language-detection/overview.md
+              itemType: overview
+              text: Language detection overview
+            - url: language-detection/language-support.md
+              itemType: reference
+              text: Language support
+            - url: language-detection/quickstart.md
+              itemType: quickstart
+              text: Get started with language detection
+
+    - title: Legacy capabilities
+      summary: Use legacy extraction and analysis capabilities for established production systems, specialized workloads, and phased migration plans. For net-new implementations, prioritize using core capabilities to align with current platform architecture, long-term roadmap direction, and recommended engineering practices.
+      items:
+
+        # Card
+        - title: Classify and analyze text
+          summary: Perform sentiment and opinion analysis, and train custom classifiers for domain-specific taxonomy mapping.
+          links:
+            - url: sentiment-opinion-mining/overview.md
+              itemType: overview
+              text: Sentiment analysis and opinion mining
+            - url: custom-text-classification/overview.md
+              itemType: overview
+              text: Custom text classification
+            - url: sentiment-opinion-mining/quickstart.md
+              itemType: quickstart
+              text: Get started with sentiment analysis
+
+        # Card
+        - title: Extract information
+          summary: Extract key phrases and resolve linked entities against knowledge sources to enrich downstream indexing and retrieval.
+          links:
+            - url: key-phrase-extraction/overview.md
+              itemType: overview
+              text: Key phrase extraction
+            - url: entity-linking/overview.md
+              itemType: overview
+              text: Entity linking
+            - url: key-phrase-extraction/quickstart.md
+              itemType: quickstart
+              text: Get started with key phrases
+
+        # Card
+        - title: Summarize content
+          summary: Generate abstractive summaries for documents, conversations, and long-form content.
+          links:
+            - url: summarization/overview.md
+              itemType: overview
+              text: Summarization overview
+            - url: summarization/overview.md?tabs=document-summarization
+              itemType: how-to-guide
+              text: Document summarization
+            - url: summarization/overview.md?tabs=conversation-summarization
+              itemType: how-to-guide
+              text: Conversation summarization
+            - url: summarization/quickstart.md
+              itemType: quickstart
+              text: Get started with summarization
+
+        # Card
+        - title: Build conversational applications
+          summary: Build conversational workflows that classify intents, extract entities, and orchestrate language services.
+          links:
+            - url: conversational-language-understanding/overview.md
+              itemType: overview
+              text: Conversational language understanding
+            - url: orchestration-workflow/overview.md
+              itemType: overview
+              text: Orchestration workflow
+            - url: conversational-language-understanding/quickstart.md
+              itemType: quickstart
+              text: Get started with CLU
+
+        # Card
+        - title: Build question-answering systems
+          summary: Author domain-specific knowledge bases and deploy question-answering agents for retrieval-grounded responses.
+          links:
+            - url: question-answering/overview.md
+              itemType: overview
+              text: Custom question answering
+            - url: question-answering/how-to/deploy-agent.md
+              itemType: how-to-guide
+              text: Deploy a CQA agent
+            - url: question-answering/quickstart/sdk.md
+              itemType: quickstart
+              text: Get started with CQA
 
-    - title: Answer questions
-      summary: Provide answers to questions being asked in unstructured texts using our prebuilt capabilities, or customize your domain specific question-and-answer pairs over data you provide.
-      links:
-        - itemType: overview
-          text: Question answering
-          url: question-answering/overview.md 
-    - title: Understand conversations
-      summary: Create your own models to classify conversational utterances and extract detailed information from them to fulfill scenarios. 
-      links:
-        - itemType: overview
-          text: Conversational language understanding
-          url: conversational-language-understanding/overview.md
-        - itemType: overview
-          text: Orchestration workflow
-          url: orchestration-workflow/overview.md
-    - title: Translate text 
-      summary: Use cloud-based neural machine translation to build intelligent, multi-language solutions for your applications.
-      links:
-        - itemType: overview
-          text: Use machine translation on text. 
-          url: ../translator/translator-overview.md
 additionalContent:
   sections:
-    - items:
-      - title: Resources
-        links:
-        - text: Pricing
+    - title: Resources
+      items:
+        # Card
+        - title: Pricing
+          summary: Review pricing and consumption options for Azure Language workloads.
           url: https://azure.microsoft.com/pricing/details/cognitive-services/text-analytics/
-        - text: Learn
-          url: /training/browse/?products=azure-cognitive-services&term=Speech
-      - title: Support
-        links:
-        - text: Support and help
-          url: ../cognitive-services-support-options.md?context=/azure/ai-services/speech-service/context/context
-      - title: Announced for Deprecation
-        links:
-        - text: Language Understanding
-          url: ../luis/index.yml
-        - text: QnA Maker
-          url: ../qnamaker/index.yml
+        # Card
+        - title: Support and help
+          summary: Access support channels, troubleshooting guidance, and service assistance.
+          url: ../cognitive-services-support-options.md?context=/azure/ai-services/language-service/context/context
+        # Card
+        - title: Training
+          summary: Build implementation expertise through guided learning paths and hands-on training.
+          url: /training/browse/?products=azure-cognitive-services&term=language
+    - title: Deprecated services
+      items:
+        # Card
+        - title: Language Understanding (LUIS)
+          links:
+          - url: conversational-language-understanding/overview.md
+            text: Conversational Language Understanding (CLU) is the replacement for LUIS in Azure Language for new development.
+        # Card
+        - title: QnA Maker
+          links:
+          - url: question-answering/overview.md
+            text: Custom Question Answering (CQA) is the replacement for QnA Maker in Azure Language for new development.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Languageドキュメントの更新"
}
```

### Explanation
この変更は、Azure Languageサービスに関するドキュメントの内容を更新し、サポートする機能やリソースを拡充することを目的としています。具体的には、文書のタイトルと要約が変更され、主要な機能やリソースが新たに追加されています。また、一部コンテンツが削除され、新しいセクションが追加されて、全体的に情報が整理されました。

この修正によって、ユーザーはAzure Languageの主な機能にアクセスしやすくなり、自然言語処理（NLP）ソリューションの開発や展開をよりスムーズに行えるようになります。追加されたセクションには、PII検出、エンティティ認識、カスタムモデルの構築、医療文書の分析など、多岐にわたる能力が含まれています。

全体として、この更新はユーザーに最新情報を提供し、Azure Languageサービスを効果的に利用するための支援を強化することを目的としています。


