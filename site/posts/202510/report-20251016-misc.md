---
date: '2025-10-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c693aca...MicrosoftDocs:0191f09
summary: このコードの差分は、AIサービスの目次ファイルにおける小規模な更新を示しています。新たに「Responsible use of AI」というセクションが追加され、AIの責任ある使用に関する重要事項が明記されました。また、テキスト分析に関する情報も増加し、ユーザーの利便性が向上しました。この変更は、AIを倫理的に使用し、データプライバシーや透明性を重視するためのガイダンスを提供することを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c693aca...MicrosoftDocs:0191f09){target="_blank"}

# ハイライト
このコードの差分は、AIサービスの目次（TOC）ファイルにおける小規模な更新を示しています。主な変更点として、「Responsible use of AI」という新しいセクションが追加され、AIの責任ある使用に関する重要事項が明記されました。また、テキスト分析に関する新しい情報も追加されました。

## 新機能
- 「Responsible use of AI」というセクションの追加。具体的には、透明性やデータ・プライバシー、セキュリティに関する情報を含む。

## 破壊的変更
- 特筆すべき破壊的変更はなし。

## その他の更新
- テキスト分析に関連する情報が増加し、関連リソースへのリンクが追加され、ユーザーの利便性が向上。

# 洞察
この変更は、AIサービスにおける情報をより包括的かつアクセスしやすくすることを目的としたものです。特に、新しく追加された「Responsible use of AI」のセクションは、倫理的な側面や法的な配慮が求められる領域でのAI使用に関するガイダンスを提供します。この背景には、AI技術が急速に発展し続ける中、利用者が倫理基準やセキュリティポリシーを遵守するための最新情報を確実に得られるようにする意図があります。

さらに、テキスト分析セクションの拡充により、AIを活用する実務者に対して具体的な指針やリソースへのアクセスが改善されています。このような情報整備は、AIアプリケーションの効果的な利用を助長し、特にデータプライバシーや透明性の側面を重視するユーザーにとって価値の高いものとなるでしょう。AIの透明で責任ある利用への指導を強化することで、企業や個人ユーザーに信頼できるAIサービスが提供されることを目指しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [toc.yml](#item-12f1f0) | minor update | AIサービスのTOCファイルの更新 | modified | 53 | 50 | 103 | 


# Modified Contents
## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -715,19 +715,65 @@ items:
           href: ../containers/disconnected-containers.md
         - name: Azure AI containers overview
           href: ../cognitive-services-container-support.md
+      - name: Responsible use of AI
+        items:
+        - name: Transparency note for summarization
+          href: ../../ai-foundry/responsible-ai/language-service/transparency-note-extractive-summarization.md
+          displayName: Transparency note for summarization, summarization transparency, Responsible AI, Responsible use of AI
+        - name: Integration and responsible use
+          href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use-summarization.md
+          displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
+        - name: Characteristics and limitations
+          href: ../../ai-foundry/responsible-ai/language-service/characteristics-and-limitations-summarization.md
+        - name: Data, privacy, and security
+          href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
+          displayName: Data privacy, logging, data retention
+
+  - name: Text Analytics for health
+    items:
+    - name: Overview
+      href: text-analytics-for-health/overview.md
+      displayName: text analytics for health, healthcare nlp, medical text analysis, clinical text, health entities
+    - name: Quickstart
+      href: text-analytics-for-health/quickstart.md
+    - name: Language support
+      href: text-analytics-for-health/language-support.md
     - name: Responsible use of AI
       items:
-      - name: Transparency note for summarization
-        href: ../../ai-foundry/responsible-ai/language-service/transparency-note-extractive-summarization.md
-        displayName: Transparency note for summarization, summarization transparency, Responsible AI, Responsible use of AI
+      - name: Transparency note for Text Analytics for health
+        href: ../../ai-foundry/responsible-ai/language-service/transparency-note-health.md
+        displayName: Transparency note for Text Analytics health, Text Analytics for health transparency, Responsible AI, Responsible use of AI
       - name: Integration and responsible use
-        href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use-summarization.md
+        href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md
         displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-      - name: Characteristics and limitations
-        href: ../../ai-foundry/responsible-ai/language-service/characteristics-and-limitations-summarization.md
       - name: Data, privacy, and security
         href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
         displayName: Data privacy, logging, data retention
+    - name: How-to guides
+      items:
+      - name: How to call the API
+        href: text-analytics-for-health/how-to/call-api.md
+      - name: Use containers
+        items:
+        - name: Use Docker containers
+          href: text-analytics-for-health/how-to/use-containers.md
+        - name: Configure Docker containers
+          href: text-analytics-for-health/how-to/configure-containers.md
+        - name: Use container instances
+          href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
+        - name: Azure AI containers overview
+          href: ../cognitive-services-container-support.md
+    - name: Concepts
+      items:
+      - name: Recognized entity categories
+        href: text-analytics-for-health/concepts/health-entity-categories.md
+      - name: Relation extraction
+        href: text-analytics-for-health/concepts/relation-extraction.md
+      - name: Assertion detection
+        href: text-analytics-for-health/concepts/assertion-detection.md
+      - name: Fast Healthcare Interoperability Resources structuring
+        href: text-analytics-for-health/concepts/fhir.md
+        
 - name: Concepts
   items:
   - name: Developer guide
@@ -868,50 +914,7 @@ items:
         - name: Azure.AI.Language.QuestionAnswering namespace
           href: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/cognitivelanguage/azure-ai-language-questionanswering
 
-  - name: Text Analytics for health
-    items:
-    - name: Overview
-      href: text-analytics-for-health/overview.md
-      displayName: text analytics for health, healthcare nlp, medical text analysis, clinical text, health entities
-    - name: Quickstart
-      href: text-analytics-for-health/quickstart.md
-    - name: Language support
-      href: text-analytics-for-health/language-support.md
-    - name: Responsible use of AI
-      items:
-      - name: Transparency note for Text Analytics for health
-        href: ../../ai-foundry/responsible-ai/language-service/transparency-note-health.md
-        displayName: Transparency note for Text Analytics health, Text Analytics for health transparency, Responsible AI, Responsible use of AI
-      - name: Integration and responsible use
-        href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md
-        displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-      - name: Data, privacy, and security
-        href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
-        displayName: Data privacy, logging, data retention
-    - name: How-to guides
-      items:
-      - name: How to call the API
-        href: text-analytics-for-health/how-to/call-api.md
-      - name: Use containers
-        items:
-        - name: Use Docker containers
-          href: text-analytics-for-health/how-to/use-containers.md
-        - name: Configure Docker containers
-          href: text-analytics-for-health/how-to/configure-containers.md
-        - name: Use container instances
-          href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
-        - name: Azure AI containers overview
-          href: ../cognitive-services-container-support.md
-    - name: Concepts
-      items:
-      - name: Recognized entity categories
-        href: text-analytics-for-health/concepts/health-entity-categories.md
-      - name: Relation extraction
-        href: text-analytics-for-health/concepts/relation-extraction.md
-      - name: Assertion detection
-        href: text-analytics-for-health/concepts/assertion-detection.md
-      - name: Fast Healthcare Interoperability Resources structuring
-        href: text-analytics-for-health/concepts/fhir.md
+
 - name: Resources
   items:
     - name: Support and help options
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIサービスのTOCファイルの更新"
}
```

### Explanation
この変更は、AIサービスに関連するTOC（目次）ファイルでの更新を示しています。53行が追加され、50行が削除され、合計で103行の変更が行われました。この更新において新たに「Responsible use of AI」というセクションが追加され、AIの責任ある使用に関する複数の項目が含まれています。

具体的には、透明性に関する注記や、統合と責任ある使用、特性および制限、データ・プライバシー・セキュリティについての情報が含まれています。また、テキスト分析に関する新しいセクションも追加され、概要やクイックスタート、言語サポートなどのリンクが提供されています。これにより、ユーザーはAIサービスの責任ある使用についての詳細な情報や、テキスト分析に関するさまざまなリソースに簡単にアクセスできるようになります。

これは、AIサービスに関連する情報をより明確に整理し、差し迫った分野（たとえば医療）における責任ある使用に関するガイダンスを強化することを目的とした小さなアップデートです。変更の背景には、利用者が最新の技術とガイドラインにアクセスできるようにするための意図があります。


