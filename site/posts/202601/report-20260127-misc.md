---
date: '2026-01-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2356f0d...MicrosoftDocs:9f4eb38
summary: この変更では、Azure AI 言語サービスに関する2つのドキュメントがマイナーアップデートされました。「モデルライフサイクル」ドキュメントでは日付の更新と表形式の改善が行われ、「Language
  StudioからMicrosoft Foundryへの移行」ガイドには重要な注意事項が追加されました。この更新により、ユーザーの理解が向上し、混乱を減らすことを目的としています。主な変更は情報更新と整理で、特に技術文書の定期的なアップデートの重要性が強調されました。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2356f0d...MicrosoftDocs:9f4eb38){target="_blank"}

# Highlights
これらの変更では、Azure AI 言語サービスに関する2つのドキュメントがマイナーアップデートされました。「モデルライフサイクル」のドキュメントでは、新しい日付への変更と表形式の改良が行われ、「Language StudioからMicrosoft Foundryへの移行」ガイドでは、新しい注意事項の追加が行われ、ユーザーの理解を助けるようにしました。

## New features
- 重要な注意事項の追加により、移行に関するユーザーの理解を向上。

## Breaking changes
- 特にBreaking changesはなし。

## Other updates
- ドキュメントの日付の更新。
- 表形式の改善でより整理された情報提供。

# Insights
今回の変更は、主にドキュメントの情報の更新と改良に焦点を当てたものでした。技術文書は時間の経過とともに情報の陳腐化が問題となる領域であり、定期的なアップデートが不可欠です。特に、サービスやツールの引退に伴う移行がユーザーに影響を与える場合、その案内が明確かつタイムリーであることは非常に重要です。Azure AI 言語サービスの「モデルライフサイクル」では表形式の改善により情報のアクセス性や可読性を向上させ、ユーザーが必要な情報をすぐに見つけることができるように工夫されました。

一方で「Language StudioからMicrosoft Foundryへの移行」ガイドでは、具体的な引退日程や移行後の手続きに関する情報が追加され、プロジェクトアセットの移行に関する詳細な注意点が含まれました。これらの追加情報は、ユーザーがスムーズに移行を行うために必要な情報を提供し、混乱を減らします。このような詳細かつ体系的なドキュメント更新は、エンタープライズ環境におけるスムーズな技術移行を支え、Azureのユーザーエクスペリエンスを向上させる要素となります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-lifecycle.md](#item-417f3f) | minor update | モデルライフサイクルの更新 | modified | 11 | 12 | 23 | 
| [migration-studio-to-foundry.md](#item-12d575) | minor update | Language StudioからMicrosoft Foundryへの移行ガイドの更新 | modified | 11 | 8 | 19 | 


# Modified Contents
## articles/ai-services/language-service/concepts/model-lifecycle.md{#item-417f3f}

<details>
<summary>Diff</summary>
````diff
@@ -6,9 +6,10 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: concept-article
-ms.date: 11/18/2025
+ms.date: 01/26/2026
 ms.author: lajanuar
 ---
+<!-- markdownlint-disable MD025 -->
 # Model lifecycle
 
 Language features utilize AI models. We update Azure Language with new model versions to improve accuracy, support, and quality. As models become older, they're retired. Use this article for information on that process, and what you can expect for your applications.
@@ -36,19 +37,18 @@ By default, API and SDK requests use the latest Generally Available model. To us
 
 Use the following table to find which model versions support each feature:
 
-| Feature | Supported generally available (GA) version | Latest supported preview versions | Other supported verision |
-|--|--|--|--|
-| Sentiment Analysis and opinion mining | `latest` |  |  |
-| Language Detection | `latest` |  |  |
-| Entity Linking | `latest` |  |  |
+| Feature | Supported generally available (GA) version | Latest supported preview versions | Other supported version |
+| ---- | ---- | ---- | ---- |
+| Sentiment Analysis and opinion mining | `latest` | | |
+| Language Detection | `latest` | | |
+| Entity Linking| `latest` | | |
 | Named Entity Recognition (NER) | `latest` | `2025-08-01-preview` | `2025-04-15-preview` |
 | Personally Identifiable Information (PII) detection | `latest` | `2025-08-01-preview` | `2025-04-15-preview` |
 | PII detection for conversations | `latest` | `2024-11-01-preview` | `2023-04-15-preview` |
-| Question answering | `latest` |  |  |
-| Text Analytics for health | `latest` | `2023-04-15-preview` |  |
-| Key phrase extraction | `latest` |  |  |
-| Summarization | `latest`. **Note**: `2025-06-10` is only available for `issue` and `resolution` aspects in conversation summarization.  | |  |
-
+| Question answering | `latest` | | |
+| Text Analytics for health | `latest` | `2023-04-15-preview` | |
+| Key phrase extraction | `latest` | | |
+| Summarization | `latest`. **Note**: `2025-06-10` is only available for `issue` and `resolution` aspects in conversation summarization. | | |
 
 ## Custom features
 
@@ -76,7 +76,6 @@ After the **training config expiration** date, you have to use another supported
 
 After training config version expires, API calls returns an error when called or used if called with an expired configuration version. By default, training requests use the latest available training configuration version. To change the configuration version, use the `trainingConfigVersion` parameter when submitting a training job and assign the version you want.
 
-
 ## API versions
 
 When you're making API calls to the following features, you need to specify the `API-VERISON` you want to use to complete your request. We recommend that you use the latest available API version.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルの更新"
}
```

### Explanation
この変更は、Azure AI 言語サービスの「モデルライフサイクル」に関するドキュメントに対するマイナーアップデートです。主な変更点は、ドキュメントの日付が「2025年11月18日」から「2026年1月26日」に変更され、表の形式が改良されました。

具体的には、表の見出しにある「他のサポートされるバージョン」のセクションが整理され、整頓されました。また、一部の行には未使用のフィールドが削除され、全体の整合性が向上しています。このような改良により、読者は重要な情報に簡単にアクセスできるようになっています。

これらの変更は、コンテンツの品質と可読性を向上させることを目的としています。

## articles/ai-services/language-service/migration-studio-to-foundry.md{#item-12d575}

<details>
<summary>Diff</summary>
````diff
@@ -6,13 +6,21 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: upgrade-and-migration-article
-ms.date: 01/20/2026
+ms.date: 01/26/2026
 ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD025 -->
 # Migrate from Language Studio to Microsoft Foundry
 
-Azure Language Studio retires on February 16, 2026. The service is no longer available after this date. All existing capabilities, along with new feature enhancements, are fully available in Microsoft Foundry. This guide provides step-by-step migration instructions to ensure uninterrupted access to Azure AI Language features and seamless project continuity within the Foundry environment.
+Azure Language Studio retires on February 16, 2026 and is no longer available after this date. All existing capabilities, along with new feature enhancements, are fully available in Microsoft Foundry. This guide provides step-by-step migration instructions to ensure uninterrupted access to Azure AI Language features and seamless project continuity within the Foundry environment.
+
+> [!IMPORTANT]
+>
+> **Post-retirement project recreation**. After the February 16, 2026 retirement date, Language Studio export functionality is no longer available. However, you can recreate your custom projects directly in Microsoft Foundry:
+>
+> * **Existing Azure Language resources**. You can access and continue to use your current Azure Language resources within the Microsoft Foundry portal by creating a **Foundry hub** and an associated **hub-based project**. For more information, *see* [Create a hub in the Azure portal](/azure/ai-foundry/how-to/create-azure-ai-resource?view=foundry-classic&preserve-view=true&tabs=portal#create-a-hub-in-the-azure-portal).
+>
+> * **Existing Foundry resource-based projects**. You can access your current **Foundry projects** directly in the Microsoft Foundry portal. Alternatively, create a new project and transfer your project assets to the new environment. For more information, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects?view=foundry-classic&preserve-view=true&tabs=foundry).
 
 ## Why migrate to Microsoft Foundry?
 
@@ -35,12 +43,7 @@ The migration process consists of the following steps:
 ## Prerequisites
 
 > [!NOTE]
->
-> * If you already have an Azure Language resource, you can continue to use your existing Language resources within the Microsoft Foundry portal via a **Foundry Hub** and **Hub project**. For more information, *see* [Which type of project do I need?](/azure/ai-foundry/what-is-foundry?view=foundry-classic&preserve-view=true#which-type-of-project-do-i-need).
->
-> * If you plan to use a Foundry resource, you can create a new Foundry resource directly in the Microsoft Foundry portal when creating a new project. For more information, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects?view=foundry-classic&preserve-view=true&tabs=foundry).
->
-> * In the Foundry, a **fine-tuning task** serves as your workspace when customizing your custom models. Previously, a **fine-tuning task** was referred to as a project. You might encounter both terms used interchangeably in some documentation.
+> In the Foundry, a **fine-tuning task** serves as your workspace when customizing your custom models. Previously, a **fine-tuning task** was referred to as a project. You might encounter both terms used interchangeably in some documentation.
 
 **Before you begin the migration process, ensure that the following resources and permissions are in place to complete the steps in this guide:**
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Language StudioからMicrosoft Foundryへの移行ガイドの更新"
}
```

### Explanation
この変更は、Azure AI 言語サービスの「Language StudioからMicrosoft Foundryへの移行」ガイドに対するマイナーアップデートです。主な変更は、文書の日付が「2026年1月20日」から「2026年1月26日」に更新された点と、移行に関する重要な注意事項が追加されたことです。

具体的には、Language Studioの引退に関する情報が強調され、引退日以降のプロジェクト再作成についての重要な注意書きが追加されました。これにより、ユーザーは引退後にAzure LanguageリソースをMicrosoft Foundryでどのように利用し続けるかや、プロジェクトのアセットを新しい環境に移行する方法についての明確な指示を得ることができます。また、移行プロセスの事前条件に重要な点が強調されることで、移行時の手続きがスムーズに進むことを助けています。

全体的に、これらの変更により、読者は将来の移行プロセスについてより良い理解を得ることができ、サービスの利用継続に関するガイダンスが向上しています。


