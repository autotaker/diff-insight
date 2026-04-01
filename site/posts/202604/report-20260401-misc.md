---
date: '2026-04-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f3c79c0...MicrosoftDocs:98210c1
summary: このドキュメントの変更は、Azureの言語サービスに関する情報を整理・更新し、新たに「個人識別情報（PII）検出」セクションを追加しました。この追加により、利用者は特定の機能をより理解しやすくなり、関連情報へのアクセスも簡素化されています。既存の情報は新しいセクションに集約され、全体の構成が改善されました。また、目次の見直しや用語の統一も行い、文書のプロフェッショナリズムが高まっています。これにより、ユーザーはAzure言語サービスをより効果的に利用できるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f3c79c0...MicrosoftDocs:98210c1){target="_blank"}

# Highlights
このドキュメントの変更は、Azureの言語サービスに関連する情報の整理と更新を行い、特に個人識別情報（PII）検出機能に関する新しいセクションを追加します。これにより、利用者が具体的な機能を容易に理解できるようになり、関連情報へのアクセスが容易になっています。

## 新機能
- 新たに「個人識別情報（PII）検出」セクションが追加されました。
- PII検出機能に関する具体例に使うための視覚的な画像が追加されました。

## 破壊的変更
- 既存のセクションからPII検出に関連する情報を削除し、新しく設けられたセクションに集約しています。このため、ドキュメント内の情報配置が変わりました。

## その他の更新
- 目次（toc.yml）の構造を見直し、情報の整理と名称の微調整を行いました。
- 「Named Entity Recognition」の表記を「Named entity recognition」に変更し統一感を持たせました。

# Insights
Azure言語サービスの概要文書において、新しく追加された「個人識別情報（PII）検出」セクションは、サービスの機能をより際立たせる重要な追加です。個人識別情報の管理は、セキュリティとプライバシーの観点から、ますます重要性を増しています。この機能を明確に説明し、ナビゲートしやすくするためのセクション追加は、利用者がこのサービスをより効果的に使うための戦略的な変更です。

この更新では、目次の構成が改善され、PIIに関連する資料へのアクセス性が向上しました。利用者が最も重要とする情報を迅速に見つけられるようになり、利便性が高まっています。また、文書の統一性を保つための小さな編集（名称の一貫性保持）も、全体としてドキュメントのプロフェッショナリズムを向上させています。これにより、Azure言語サービスの利用者は、更新された内容を通じて、自社のニーズに合った機能を容易に見つけて活用することができます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [overview.md](#item-f138b4) | minor update | 言語サービスの概要における情報更新 | modified | 16 | 14 | 30 | 
| [toc.yml](#item-12f1f0) | minor update | 言語サービスの目次更新 | modified | 61 | 69 | 130 | 


# Modified Contents
## articles/ai-services/language-service/overview.md{#item-f138b4}

<details>
<summary>Diff</summary>
````diff
@@ -21,18 +21,33 @@ Azure Language is a cloud-based service that provides Natural Language Processin
 
 Core capabilities are the primary, actively evolving features of Azure Language. These features receive ongoing investment and feature updates, and are recommended for new development and long-term planning. If you are starting a new project or designing a future architecture, use core capabilities as the foundation for your natural language processing workflows.
 
+* [PII detection](#personally-identifiable-information-pii-detection)
 * [Language detection](#language-detection)
 * **Named entity recognition (NER)**
   * [Custom NER](#custom-ner)
   * [Prebuilt NER](#prebuilt-ner)
-* [PII detection](#personally-identifiable-information-pii-detection)
 * [Text analytics for health](#text-analytics-for-health)
 
 > [!TIP]
 > Unsure which feature to use? See [Which Azure Language core feature should I use](#which-core-language-feature-should-i-use) to help you decide.
 
 [**Microsoft Foundry**](https://ai.azure.com/) enables you to use most of the following service features without the need to write code.
 
+### Personally identifiable information (PII) detection
+
+> [!IMPORTANT]
+> The Azure Language in Foundry Tools text personally identifiable information (PII) detection anonymization feature (synthetic replacement) is currently available in `preview` and licensed to you as part of your Azure subscription. Your use of this feature is subject to the terms applicable to **Previews** as described in the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms) and the [Microsoft Products and Services Data Protection Addendum (DPA)](https://www.microsoft.com/licensing/docs/view/microsoft-products-and-services-data-protection-addendum-dpa).
+
+[Personally identifiable information (PII) detection](./personally-identifiable-information/overview.md) identifies entities in text and conversations (chat or transcripts) that are associated with individuals.
+
+***Conversation PII***
+
+:::image type="content" source="media/overview/conversation-pii.png" alt-text="A screenshot of conversation personally identifying information in Foundry." lightbox="media/overview/conversation-pii.png":::
+
+***Text PII***
+
+:::image type="content" source="media/overview/text-pii.png" alt-text="A screenshot of text personally identifying information in Foundry." lightbox="media/overview/text-pii.png":::
+
 ### Language detection
 
 [Language detection](./language-detection/overview.md) evaluates text and detects a wide range of languages and variant dialects.
@@ -51,20 +66,7 @@ Core capabilities are the primary, actively evolving features of Azure Language.
 
 :::image type="content" source="media/overview/named-entity-recognition.png" alt-text="A screenshot of named entity recognition in Foundry." lightbox="media/overview/named-entity-recognition.png":::
 
-### Personally identifiable information (PII) detection
 
-> [!IMPORTANT]
-> The Azure Language in Foundry Tools text personally identifiable information (PII) detection anonymization feature (synthetic replacement) is currently available in `preview` and licensed to you as part of your Azure subscription. Your use of this feature is subject to the terms applicable to **Previews** as described in the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms) and the [Microsoft Products and Services Data Protection Addendum (DPA)](https://www.microsoft.com/licensing/docs/view/microsoft-products-and-services-data-protection-addendum-dpa).
-
-[Personally identifiable information (PII) detection](./personally-identifiable-information/overview.md) identifies entities in text and conversations (chat or transcripts) that are associated with individuals.
-
-***Conversation PII detection***
-
-:::image type="content" source="media/overview/conversation-pii.png" alt-text="A screenshot of conversation personally identifying information in Foundry." lightbox="media/overview/conversation-pii.png":::
-
-***Text PII detection***
-
-:::image type="content" source="media/overview/text-pii.png" alt-text="A screenshot of text personally identifying information in Foundry." lightbox="media/overview/text-pii.png":::
 
 ### Text analytics for health
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サービスの概要における情報更新"
}
```

### Explanation
このコードの変更は、Azureの言語サービスに関する概要文書の小規模な更新を反映しています。具体的には、個人識別情報（PII）検出に関するセクションが新たに追加され、他のセクションとの調整も行われました。この更新により、特にPII検出機能の重要性が強調され、利用者がこの機能をどのように活用できるかについての詳細が提供されています。

具体的には、以下のポイントが含まれています：
- 新たに「個人識別情報（PII）検出」セクションが設けられ、強調された注意事項やライセンス情報が加わりました。
- 既存のセクションからPII検出に関連する情報が削除され、新しいセクションに集約されています。
- 画像が追加されて、具体的な機能の例が視覚的に示されています。

全体として、この変更は文書の可読性を向上させ、利用者が容易に情報を見つけられるように整理されています。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -31,6 +31,63 @@ items:
 - name: Core capabilities
   items:
 
+  - name: Personally identifiable information (PII)
+    items:
+    - name: Overview
+      href: personally-identifiable-information/overview.md
+      displayName: personally identifiable information, document
+    - name: Quickstart
+      href: personally-identifiable-information/quickstart.md
+    - name: Language support
+      href: personally-identifiable-information/language-support.md
+    - name: Responsible use of AI
+      items:
+      - name: Transparency note for PII
+        href: ../../ai-foundry/responsible-ai/language-service/transparency-note-personally-identifiable-information.md
+        displayName: Transparency note for PII, Personally Identifiable Information transparency, Responsible AI, Responsible use of AI
+      - name: Integration and responsible use
+        href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md
+        displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
+      - name: Data, privacy, and security
+        href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
+        displayName: Data privacy, logging, data retention
+    - name: How-to guides
+      items:
+      - name: Redact PII from text
+        href: personally-identifiable-information/how-to/redact-text-pii.md
+      - name: Redact PII from conversations
+        href: personally-identifiable-information/how-to/redact-conversation-pii.md
+      - name: Redact PII from native documents
+        href: personally-identifiable-information/how-to/redact-document-pii.md
+      - name:  Adapt PII to your domain
+        href: personally-identifiable-information/how-to/adapt-to-domain-pii.md
+      - name: Use Docker containers
+        items:
+          - name: Install and run containers
+            href: personally-identifiable-information/how-to/use-containers.md
+          - name: Configure containers
+            href: concepts/configure-containers.md
+          - name: Use container instances
+            href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
+          - name: Use containers in disconnected environments
+            href: ../containers/disconnected-containers.md
+          - name: Azure AI containers overview
+            href: ../cognitive-services-container-support.md
+    - name: Recognized entity categories
+      items:
+      - name: PII in text
+        items:
+        - name: Extended format
+          href: personally-identifiable-information/concepts/entity-categories.md
+        - name: List format
+          href: personally-identifiable-information/concepts/entity-categories-list.md
+      - name: PII in conversations
+        items:
+        - name: Extended format
+          href: personally-identifiable-information/concepts/conversations-entity-categories.md
+        - name: List format
+          href: personally-identifiable-information/concepts/conversations-entities-list.md
+
   - name: Language detection
     items:
     - name: Overview
@@ -68,7 +125,7 @@ items:
         - name: Azure AI containers overview
           href: ../cognitive-services-container-support.md
 
-  - name: Named Entity Recognition
+  - name: Named entity recognition
     items:
     - name: Custom named entity recognition (CNER)
       items:
@@ -177,64 +234,7 @@ items:
           href: named-entity-recognition/tutorials/extract-excel-information.md
           displayName: excel integration, power automate, ner automation, extract entities
 
-  - name: Personally identifiable information (PII) recognition
-    items:
-    - name: Overview
-      href: personally-identifiable-information/overview.md
-      displayName: personally identifiable information, document
-    - name: Quickstart
-      href: personally-identifiable-information/quickstart.md
-    - name: Language support
-      href: personally-identifiable-information/language-support.md
-    - name: Responsible use of AI
-      items:
-      - name: Transparency note for PII
-        href: ../../ai-foundry/responsible-ai/language-service/transparency-note-personally-identifiable-information.md
-        displayName: Transparency note for PII, Personally Identifiable Information transparency, Responsible AI, Responsible use of AI
-      - name: Integration and responsible use
-        href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md
-        displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-      - name: Data, privacy, and security
-        href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
-        displayName: Data privacy, logging, data retention
-    - name: How-to guides
-      items:
-      - name: Redact PII from text
-        href: personally-identifiable-information/how-to/redact-text-pii.md
-      - name: Redact PII from conversations
-        href: personally-identifiable-information/how-to/redact-conversation-pii.md
-      - name: Redact PII from native documents
-        href: personally-identifiable-information/how-to/redact-document-pii.md
-      - name:  Adapt PII to your domain
-        href: personally-identifiable-information/how-to/adapt-to-domain-pii.md
-      - name: Use Docker containers
-        items:
-          - name: Install and run containers
-            href: personally-identifiable-information/how-to/use-containers.md
-          - name: Configure containers
-            href: concepts/configure-containers.md
-          - name: Use container instances
-            href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
-          - name: Use containers in disconnected environments
-            href: ../containers/disconnected-containers.md
-          - name: Azure AI containers overview
-            href: ../cognitive-services-container-support.md
-    - name: Recognized entity categories
-      items:
-      - name: PII in text
-        items:
-        - name: Extended format
-          href: personally-identifiable-information/concepts/entity-categories.md
-        - name: List format
-          href: personally-identifiable-information/concepts/entity-categories-list.md
-      - name: PII in conversations
-        items:
-        - name: Extended format
-          href: personally-identifiable-information/concepts/conversations-entity-categories.md
-        - name: List format
-          href: personally-identifiable-information/concepts/conversations-entities-list.md
-
-  - name: Text Analytics for health
+  - name: Text analytics for health
     items:
     - name: Overview
       href: text-analytics-for-health/overview.md
@@ -281,7 +281,7 @@ items:
 
 - name: Legacy capabilities
   items:
-  - name: "Conversational language understanding (CLU)"
+  - name: Conversational language understanding (CLU)
     items:
     - name: Overview
       href: conversational-language-understanding/overview.md
@@ -590,7 +590,6 @@ items:
           href: entity-linking/how-to/call-api.md
           displayName: entity linking, entity recognition
 
-
   - name: Key phrase extraction
     items:
     - name: Overview
@@ -633,8 +632,6 @@ items:
         href: key-phrase-extraction/tutorials/integrate-power-bi.md
         displayName: business intelligence, data visualization
 
-
-
   - name: Orchestration workflow
     items:
     - name: Overview
@@ -692,7 +689,6 @@ items:
       - name: Glossary
         href: orchestration-workflow/glossary.md
 
-
   - name: Sentiment analysis and opinion mining
     items:
       - name: Overview
@@ -734,7 +730,6 @@ items:
         - name: Use Flask to translate text, analyze sentiment, and synthesize speech
           href: /training/modules/python-flask-build-ai-web-app/
 
-
   - name: Summarization
     items:
     - name: Overview
@@ -778,9 +773,7 @@ items:
           href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
           displayName: Data privacy, logging, data retention
 
-
-
-- name: Concepts
+- name: Azure Language concepts
   items:
   - name: Developer guide
     href: concepts/developer-guide.md
@@ -920,7 +913,6 @@ items:
         - name: Azure.AI.Language.QuestionAnswering namespace
           href: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/cognitivelanguage/azure-ai-language-questionanswering
 
-
 - name: Resources
   items:
     - name: Support and help options
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サービスの目次更新"
}
```

### Explanation
この変更は、Azureの言語サービスに関連する目次（toc.yml）の構造を更新し、新しい情報を追加しています。主に個人識別情報（PII）に関する項目が新たに追加され、従来の項目が整理されました。この結果、利用者が情報を見つけやすくするために、文書構造の明確化が図られています。

特に以下のようなアップデートが行われました：
- **PIIに関するセクションの追加**: 新しい「個人識別情報（PII）」セクションが設けられ、その下に関連マニュアルやガイドが階層的に構成されています。これにより、PIIに関連する機能やリソースが集約されています。
- **名称の微調整**: 「Named Entity Recognition」という表記が「Named entity recognition」に変更され、統一されたスタイルが維持されています。
- **使いやすさの向上**: 目次全体の項目が見直されて、重要な情報が目立つように配置され、ユーザーの利便性が向上しました。

この変更は、特にPII検出に特化した情報を強調し、関連するリソースが容易にアクセスできるようにしています。全体として、ドキュメントのナビゲーションが改善されており、使用される可能性のある新しい機能やガイドにすぐにアクセスできるようになっています。


