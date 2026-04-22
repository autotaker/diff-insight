---
date: '2026-04-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:027b661...MicrosoftDocs:c0c5302
summary: このコードの変更では、Azure Languageサービスのドキュメント管理に関連する大幅な更新が行われ、特に個人を特定できる情報（PII）の処理に関する新機能の追加や既存ドキュメントの削除が目立ちます。新機能には会話やドキュメントからのPII削除機能の育成や、視覚的表示のための新しい画像の追加が含まれています。しかし、ネイティブドキュメントサポートの概要ファイルが削除され、一部のユーザーには混乱をもたらす可能性があります。この更新は、Azure
  AIサービスの個人情報保護機能の信頼性を高め、利用者の学習曲線を緩和する重要なステップと見なされています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:027b661...MicrosoftDocs:c0c5302){target="_blank"}

<format>
# Highlights
このコードの変更では、主にAzure Languageサービスのドキュメント管理に関する大幅な更新が行われ、特に個人を特定できる情報（PII）の処理に関連した新たな機能の追加や既存ドキュメントの削除が目立ちます。これにより、ユーザーの利用シナリオとして重要な変更点が多い内容となっています。

## New features
- 会話における個人情報（PII）削除の概要の追加。
- ドキュメントベースのPII概要とテキストPII概要の新しいドキュメント追加。
- ドキュメントと機能の視覚表示を助けるための新しい画像ファイルの追加。

## Breaking changes
- ネイティブドキュメントサポートの概要ファイルが削除され、関連情報を取得する必要があるユーザーにとって大きな影響が考えられます。

## Other updates
- 多くの文書が用語の修正を含む軽微な更新を受け、正確性と一貫性が強化されました。
- 質問応答サービスに関するドキュメントでは、リンクと日付などの更新が行われ、最新の情報源へのアクセスが改善されています。

# Insights
Azure Languageサービスのドキュメント更新は、特に個人情報保護（PII）機能の拡充に焦点を当てています。新たな機能が多数追加される一方で、従来の機能に関する概要が削除されるなど、大幅な見直しが行われています。

まず、新機能では、会話やドキュメントからのPII削除機能の育成が目立ちます。それぞれの新しいドキュメントは利用可能な機能を詳細かつ明確に説明し、これによりユーザーは、データのプライバシーとコンプライアンスを効果的に保持しつつ、技術の利用範囲を広げることができます。また、視覚的にワークフローや機能を示す新しい画像の追加は、情報の消化を効率化し、技術要素を使いやすくしています。

一方で、ネイティブドキュメントサポートの概要が削除されたことについては、一部ユーザーにとって混乱を生じる可能性があります。この削除により、ユーザーは他のリソースを頼りに情報を得る必要があります。こうした影響を考慮し、代替の情報への案内が今後必要となるかもしれません。

用語の一貫性を図った多数の軽微な修正も、プロフェッショナルなドキュメント作成において重要です。PIIに関する表現が正確に統一されることで、ユーザーが情報を誤解せずに使用できるようになっています。更新されたリンクや日付により、ドキュメントのアクセス性と信頼性も更に向上しています。

この一連の更新は、Azure AIサービスが提供する個人情報保護機能の信頼性と効果を確保しつつ、利用者の学習曲線を緩和し、新しい機能が適用される範囲を明確にする重要なステップとしてとらえることができます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [overview.md](#item-a490e5) | breaking change | ネイティブドキュメントサポートの概要の削除 | removed | 0 | 75 | 75 | 
| [conversation-pii-overview.md](#item-e1dc30) | new feature | 会話における個人情報（PII）削除の概要の追加 | added | 91 | 0 | 91 | 
| [document-based-pii-overview.md](#item-11f0ae) | new feature | ドキュメントベースのPII概要の追加 | added | 127 | 0 | 127 | 
| [adapt-to-domain-pii.md](#item-62092f) | minor update | ドメインに個人を特定できる情報（PII）を適応させる方法の修正 | modified | 3 | 3 | 6 | 
| [redact-conversation-pii.md](#item-0d6332) | minor update | 会話から個人を特定できる情報（PII）を削除する方法の修正 | modified | 3 | 3 | 6 | 
| [redact-document-pii.md](#item-5509ee) | minor update | ネイティブドキュメントからの個人を特定できる情報（PII）の削除方法の修正 | modified | 3 | 3 | 6 | 
| [redact-text-pii.md](#item-9e48af) | minor update | テキストから個人を特定できる情報（PII）を削除する方法の修正 | modified | 4 | 4 | 8 | 
| [use-containers.md](#item-8c61d4) | minor update | オンプレミスでの個人を特定できる情報（PII）検出用Dockerコンテナの利用方法の修正 | modified | 1 | 1 | 2 | 
| [development-options.md](#item-1bd5c9) | minor update | 開発オプションに関する文書の修正 | modified | 1 | 1 | 2 | 
| [azure-ai-foundry.md](#item-ff89fc) | minor update | Azure AI Foundry クイックスタートに関する文書の修正 | modified | 3 | 3 | 6 | 
| [rest-api.md](#item-842eb5) | minor update | REST APIクイックスタートに関する文書の修正 | modified | 1 | 1 | 2 | 
| [language-support.md](#item-d332b1) | minor update | PII検出機能の言語サポートに関する文書の更新 | modified | 33 | 26 | 59 | 
| [document-pii-workflow.png](#item-abc2bc) | new feature | ドキュメントPIIワークフロー画像の追加 | added | 0 | 0 | 0 | 
| [feature-types.png](#item-6d598e) | new feature | 特徴タイプ画像の追加 | added | 0 | 0 | 0 | 
| [overview.md](#item-8a6932) | minor update | PII検出機能の概要ドキュメントの更新 | modified | 76 | 61 | 137 | 
| [quickstart.md](#item-94affd) | minor update | PII検出のクイックスタートガイドの修正 | modified | 3 | 2 | 5 | 
| [text-pii-overview.md](#item-f33f06) | new feature | テキストによる個人を特定できる情報（PII）削除の概要 | added | 90 | 0 | 90 | 
| [limits.md](#item-50708f) | minor update | 質問応答サービスの制限に関するドキュメントの更新 | modified | 4 | 3 | 7 | 
| [authoring.md](#item-855d84) | minor update | 質問応答の著作に関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [create-test-deploy.md](#item-80a22f) | minor update | CQA知識ベース作成手順の更新 | modified | 3 | 3 | 6 | 
| [export-import-refresh.md](#item-2d1b56) | minor update | カスタム質問応答のエクスポート/インポート手順の更新 | modified | 2 | 4 | 6 | 
| [rest.md](#item-e6e1b0) | minor update | カスタム質問応答プロジェクト管理手順の更新 | modified | 3 | 3 | 6 | 
| [sdk-csharp.md](#item-af9649) | minor update | C# SDKのカスタム質問応答クイックスタートの更新 | modified | 3 | 3 | 6 | 
| [sdk-python.md](#item-33436a) | minor update | Python SDKのカスタム質問応答クイックスタートの更新 | modified | 2 | 2 | 4 | 
| [document-format-guidelines.md](#item-fb0489) | minor update | カスタム質問応答に関するドキュメントフォーマットガイドラインの更新 | modified | 4 | 18 | 22 | 
| [toc.yml](#item-12f1f0) | minor update | TOCの構成変更と新しいトピックの追加 | modified | 47 | 33 | 80 | 


# Modified Contents
## articles/ai-services/language-service/native-document-support/overview.md{#item-a490e5}

<details>
<summary>Diff</summary>
````diff
@@ -1,75 +0,0 @@
----
-title: Native document support for Azure Language in Foundry Tools (preview)
-titleSuffix: Foundry Tools
-description: How to use native document with Azure Language Personally Identifiable Information and Summarization capabilities.
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.custom:
-  - ignite-2024
-ms.topic: how-to
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-<!-- markdownlint-disable MD033 -->
-<!-- markdownlint-disable MD051 -->
-<!-- markdownlint-disable MD024 -->
-<!-- markdownlint-disable MD036 -->
-<!-- markdownlint-disable MD049 -->
-<!-- markdownlint-disable MD001 -->
-
-# Native document support for Azure Language in Foundry Tools (preview)
-
-> [!IMPORTANT]
->
-> * Azure Language in Foundry Tools public preview releases provide early access to features that are in active development.
-> * Features, approaches, and processes can change, before General Availability (GA), based on user feedback.
-
-Language is a cloud-based service that applies Natural Language Processing (NLP) features to text-based data. The native document support capability enables you to send API requests asynchronously, using an HTTP POST request body to send your data and HTTP GET request query string to retrieve the status results. Your processed documents are located in your Azure Blob Storage target container.
-
-A native document refers to the file format used to create the original document such as Microsoft Word (docx) or a portable document file (pdf). Native document support eliminates the need for text preprocessing before using Language resource capabilities. Currently, native document support is available for the following capabilities:
-
-* [Personally Identifiable Information (PII)](../personally-identifiable-information/overview.md). The PII detection feature can identify, categorize, and redact sensitive information in unstructured text. The `PiiEntityRecognition` API supports native document processing.
-
-* [Document summarization](../summarization/overview.md). Document summarization uses natural language processing to generate extractive (salient sentence extraction) or abstractive (contextual word extraction) summaries for documents. Both `AbstractiveSummarization` and `ExtractiveSummarization` APIs support native document processing.
-
-## Supported document formats
-
- Applications use native file formats to create, save, or open native documents. Currently **PII** and **Document summarization** capabilities supports the following native document formats:
-
-|File type|File extension|Description|
-|---------|--------------|-----------|
-|Text| `.txt`|An unformatted text document.|
-|Adobe PDF| `.pdf`|A portable document file formatted document.|
-|Microsoft Word| `.docx`|A Microsoft Word document file.|
-
-## Input guidelines
-
-***Supported file formats***
-
-|Type|support and limitations|
-|---|---|
-|**PDFs**| Fully scanned PDFs aren't supported.|
-|**Text within images**| Digital images with embedded text aren't supported.|
-|**Digital tables**| Tables in scanned documents aren't supported.|
-
-***Document Size***
-
-|Attribute|Input limit|
-|---|---|
-|**Total number of documents per request** |**≤ 20**|
-|**Total content size per request**| **≤ 10 MB**|
-
-## Request headers and parameters
-
-|parameter  |Description  |
-|---------|---------|
-|`-X POST <endpoint>`     | Specifies your Language resource endpoint for accessing the API.        |
-|`--header Content-Type: application/json`     | The content type for sending JSON data.          |
-|`--header "Ocp-Apim-Subscription-Key:<key>`    | Specifies Azure Language resource key for accessing the API.        |
-|`-data`     | The JSON file containing the data you want to pass with your request.         |
-
-## Related content
-
-> [!div class="nextstepaction"]
-> [PII detection overview](../personally-identifiable-information/overview.md "Learn more about Personally Identifiable Information detection.") [Document Summarization overview](../summarization/overview.md "Learn more about automatic document summarization.")
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "ネイティブドキュメントサポートの概要の削除"
}
```

### Explanation
この変更は、Azure Languageのネイティブドキュメントサポートに関する概要ファイル（overview.md）の削除を示しています。このファイルには、Azure Languageサービスの機能および利用方法、関連するAPIのリファレンス、サポートされているドキュメント形式や入力ガイドラインが含まれていました。

具体的には、ネイティブドキュメントサポートの意味や、個人情報の識別（PII）および文書要約の機能に関連する情報が削除されました。また、サポートされるファイル形式やリクエストに関するガイドラインも含まれており、これらの情報はユーザーにとって有用であったと考えられます。この変更により、開発者やユーザーは代替のリソースを利用する必要が生じるため、影響を受ける可能性があります。

## articles/ai-services/language-service/personally-identifiable-information/conversation-pii-overview.md{#item-e1dc30}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,91 @@
+---
+title: Conversation Personally Identifiable Information (PII) redaction overview
+titleSuffix: Foundry Tools
+description: Learn how conversation PII redaction in Azure Language detects and redacts sensitive data in turn-based conversational inputs.
+author: laujan
+manager: nitinme
+ms.service: azure-ai-language
+ms.topic: overview
+ms.date: 04/16/2026
+ms.author: lajanuar
+ms.custom: language-service-pii
+---
+
+<!-- markdownlint-disable MD025 -->
+# Conversation Personally Identifiable Information (PII) redaction overview
+
+Conversation PII redaction in Azure AI Language helps you detect and redact sensitive data in turn-based conversational input. You can use this feature for chat and transcript workflows such as customer support conversations, call transcripts, and meeting transcripts.
+
+Conversation PII is optimized for asynchronous conversation jobs and conversation-level context, so you can redact sensitive data across multiple speakers and turns.
+
+## At a glance
+
+Conversation PII provides the following capabilities:
+
+* Redaction for multi-turn conversation structures.
+* Asynchronous processing for transcript-style workloads.
+* Conversation-level handling across speakers and turns.
+* Structured entity output with redacted conversation content.
+
+## Why use conversation PII?
+
+Conversation PII is optimized for turn-based dialogue structures and supports conversational context that differs from single-block text inputs.
+
+Conversation PII is especially useful when you need to:
+
+* Redact sensitive entities in multi-turn conversation data.
+* Process transcript inputs from call center and speech workflows.
+* Preserve conversation-level context while masking sensitive information.
+
+## What it returns
+
+When a job succeeds, the service returns:
+
+* Detected entities with categories, subcategories, and confidence scores.
+* Redacted conversation output for conversation items.
+* Optional transcript-oriented metadata for supported transcript workflows.
+
+## How it works
+
+Conversation PII uses an asynchronous workflow:
+
+1. Submit conversation items as a conversation job.
+2. Poll the job status.
+3. Retrieve entities and redacted conversation output.
+
+For implementation details and request samples, see [Detect and redact Personally Identifiable Information in conversations](how-to/redact-conversation-pii.md).
+
+## How it differs from other PII feature types
+
+All PII feature types use predefined entity categories, but they optimize for different input types:
+
+* Conversation PII is optimized for turn-based and transcript-oriented conversational input.
+* Text PII is optimized for direct string-based input and app integration.
+* Document-based PII is optimized for native-file workflows and file output fidelity.
+
+## Common use cases
+
+Conversation PII is useful when teams need to anonymize conversational data before storage, analytics, quality review, external sharing, or downstream AI processing.
+
+Typical examples include:
+
+* Call center transcripts and quality-assurance workflows.
+* Customer support chat logs.
+* Meeting transcripts and collaboration records.
+* Multi-turn conversational datasets for analytics and model evaluation.
+
+## Supported formats and limits
+
+* Input format: conversation items (chat or transcript structures)
+* See [language support](language-support.md) and [quotas and limits](../concepts/data-limits.md) for current support details.
+
+## Pricing
+
+Conversation PII redaction uses Azure AI Language pricing. For current pricing details, see [Azure AI Language pricing](https://aka.ms/unifiedLanguagePricing).
+
+## Next steps
+
+Use the following references to continue implementation:
+
+* [Detect and redact Personally Identifiable Information in conversations](how-to/redact-conversation-pii.md)
+* [PII feature overview](overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "会話における個人情報（PII）削除の概要の追加"
}
```

### Explanation
この変更は、Azure Languageサービスにおける「会話における個人情報（PII）削除の概要」ファイル（conversation-pii-overview.md）の追加を示しています。このファイルは、ターンベースの会話入力における敏感なデータの検出と削除を支援する機能に関する情報を提供します。

具体的には、会話PII削除機能は、カスタマーサポートの会話や通話のトランスクリプト、会議の記録など、さまざまなコンテキストで使用できます。この機能は、複数の話者やターンにわたって敏感なデータを削除するために最適化されており、非同期処理が可能です。

ファイルには、機能の概要、実装方法、期待される出力、使用される入力形式、料金情報といった重要な情報が含まれており、この場合のユーザーのニーズに応じた利用方法を理解するためのガイドラインを提供しています。この追加により、開発者やユーザーは会話データを匿名化する方法を学び、組織内でのデータ管理やAI処理での使用を改善することができます。

## articles/ai-services/language-service/personally-identifiable-information/document-based-pii-overview.md{#item-11f0ae}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,127 @@
+---
+title: Document-based PII overview
+titleSuffix: Foundry Tools
+description: Learn how document-based PII redaction in Azure Language detects and redacts sensitive data from native documents while preserving file structure.
+author: laujan
+manager: nitinme
+ms.service: azure-ai-language
+ms.topic: overview
+ms.date: 04/16/2026
+ms.author: lajanuar
+ms.custom: language-service-pii
+---
+
+<!-- markdownlint-disable MD025 -->
+# Document-based PII overview
+
+[**Document-based PII**](document-based-pii-overview.md) is a preview feature in Azure AI Language Personally Identifiable Information (PII) detection. It helps you detect and redact sensitive data directly in native document files, including Microsoft Word and PDF files, without building your own text extraction and reconstruction pipeline.
+
+This feature uses an asynchronous API workflow and returns redacted output that preserves document structure and formatting. You can use it when document fidelity is important for compliance review, sharing, analytics, and downstream AI workflows.
+
+> [!IMPORTANT]
+> Document-based PII is currently in preview and may change before general availability (GA).
+
+## At a glance
+
+Document-based PII provides the following capabilities:
+
+* Native document redaction for `.pdf`, `.docx`, and `.txt` files.
+* Preserved layout in output documents, including font, spacing, and color.
+* A single asynchronous API workflow for extraction, detection, and redaction.
+* Enterprise-ready outputs: a redacted document and a structured JSON result.
+
+## Video demonstration
+
+In this video, we introduce the PII detection service and show you how it detects and redacts sensitive data directly from native documents while preserving file structure and formatting. We also cover common use cases, supported formats, and how to get started with document-based PII in Azure AI Language:
+
+> [!VIDEO https://learn-video.azurefd.net/vod/player?id=ec4b7c3d-c2ff-45c6-ba4f-a816b0e5d7ce]
+
+Closed captions are available for this video.
+
+## Why use document-based PII?
+
+Many custom pipelines require multiple steps to extract text, run detection, and reconstruct document output. Document-based PII simplifies this flow with a single asynchronous API pattern and output artifacts designed for document-processing systems.
+
+Document-based PII is especially useful when you need to:
+
+* Redact PII in `.pdf`, `.docx`, and `.txt` files.
+* Preserve document layout for downstream business processes.
+* Generate structured JSON output for auditing and integration.
+
+Document-based PII uses the same predefined PII categories as text PII, including entities such as addresses, phone numbers, and credit card numbers.
+
+## What it returns
+
+When a job succeeds, you receive:
+
+* A redacted document in your target storage container.
+* A JSON result file with detected entities, categories, confidence scores, and processing metadata.
+
+## How it works
+
+Document-based PII uses an asynchronous workflow:
+
+1. Submit a job with source and target storage locations.
+1. Poll the job status by using the operation location.
+1. Retrieve output artifacts from your target storage location.
+
+:::image type="content" source="media/document-pii-workflow.png" alt-text="Diagram showing the asynchronous workflow for document-based PII detection.":::
+
+For implementation details and request samples, see [Detect and redact Personally Identifiable Information in native documents](how-to/redact-document-pii.md).
+
+## How it differs from other PII feature types
+
+All PII feature types use predefined entity categories, but they optimize for different input types:
+
+* Document-based PII is optimized for native-file redaction workflows and file output fidelity.
+* Text PII is optimized for direct string-based input and app integration.
+* Conversation PII is optimized for turn-based and transcript-oriented conversational input.
+
+## Common use cases
+
+Document-based PII is designed for enterprise and regulated-industry workflows where teams need to anonymize files before storage, analytics, external sharing, or downstream AI processing.
+
+Typical examples include:
+
+* Court records and legal documentation.
+* Government forms and internal records.
+* Financial documents.
+* Internal enterprise documentation workflows.
+
+## Supported formats and limits
+
+Document-based PII accepts native file formats directly, without requiring text preprocessing. The following table lists the supported formats:
+
+| File type      | File extension | Description                                  |
+| -------------- | -------------- | -------------------------------------------- |
+| Text           | `.txt`         | An unformatted text document.                |
+| Adobe PDF      | `.pdf`         | A portable document file formatted document. |
+| Microsoft Word | `.docx`        | A Microsoft Word document file.              |
+
+The following input constraints apply:
+
+| Attribute                      | Limit    |
+| ------------------------------ | -------- |
+| Total documents per request    | <= 20    |
+| Total content size per request | <= 10 MB |
+
+The following content types are not supported:
+
+| Type                        | Limitation                                           |
+| --------------------------- | ---------------------------------------------------- |
+| Fully scanned PDFs          | Not supported.                                       |
+| Images with embedded text   | Digital images with embedded text are not supported. |
+| Tables in scanned documents | Not supported.                                       |
+
+See [language support](language-support.md) and [quotas and limits](../concepts/data-limits.md) for current language coverage and service limit details.
+
+## Pricing
+
+Document-based PII redaction uses Azure AI Language pricing. For current pricing details, see [Azure AI Language pricing](https://aka.ms/unifiedLanguagePricing).
+
+## Next steps
+
+Use the following references to continue implementation:
+
+* [Create SAS tokens for storage containers](../native-document-support/shared-access-signatures.md)
+* [Create a managed identity for storage containers](../native-document-support/managed-identities.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ドキュメントベースのPII概要の追加"
}
```

### Explanation
この変更は、Azure Languageサービスにおける「ドキュメントベースの個人情報（PII）概要」ファイル（document-based-pii-overview.md）の追加を示しています。このファイルは、ネイティブドキュメントファイル（Microsoft WordやPDFなど）内の敏感なデータを検出し、削除する機能について解説しています。この機能は、テキスト抽出や再構成のパイプラインを自分で構築することなく、ドキュメントの構造を保持しながらPIIを処理できます。

具体的には、ドキュメントベースのPII機能は非同期APIワークフローを使用し、文書のレイアウト（フォント、間隔、色など）を保ちながら赤actedされた出力を返します。この機能は、コンプライアンスレビューやデータ共有、分析、AIワークフローにおいて文書の忠実度が重要な場合に利用できます。

ファイルには、この機能の能力、動作方法、使用例、および出力内容が詳述されており、エンタープライズおよび規制産業のワークフローにおいて、データの匿名化と管理を容易にするための指針が提供されています。この新しい機能により、ユーザーは文書ベースのデータ処理をより効率的に行い、敏感情報の管理を向上させることができます。

## articles/ai-services/language-service/personally-identifiable-information/how-to/adapt-to-domain-pii.md{#item-62092f}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: Adapt Personally Identifying Information (PII) to your domain
+title: Adapt Personally Identifiable Information (PII) to your domain
 titleSuffix: Foundry Tools
-description: This article shows you how to adapt Personally Identifying Information (PII) to your domain.
+description: This article shows you how to adapt Personally Identifiable Information (PII) to your domain.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
@@ -10,7 +10,7 @@ ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
-# Adapt Personally Identifying Information (PII) to your domain
+# Adapt Personally Identifiable Information (PII) to your domain
 
 To support using your own terminology to identify entities (also known as *context*), the `entitySynonyms` feature enables you to define custom synonyms for specific entity types. This feature helps the system detect entities that appear in your inputs using terms or vocabulary that the model doesn't recognize by default. Aligning your specific terms with standard entities allows the model to accurately recognize and link these terms during entity detection.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドメインに個人を特定できる情報（PII）を適応させる方法の修正"
}
```

### Explanation
この変更は、「ドメインに個人を特定できる情報（PII）を適応させる方法」ファイル（adapt-to-domain-pii.md）の内容における軽微な修正を示しています。具体的には、タイトルおよび説明文における用語の一貫性を高めるため、「Personally Identifying Information」という表現が「Personally Identifiable Information」に修正されています。また、文章内における用語の統一が図られています。

これにより、記事の名称と内容全体の整合性が向上し、読み手が用語に関して混乱しないよう配慮されています。変更された箇所は少ないものの、専門用語の正確な使用が重要なこの領域において、文書の品質改善に寄与しています。このような修正は、全体の理解を助け、ユーザーが情報を容易に取得できるようサポートします。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-conversation-pii.md{#item-0d6332}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: Identify and extract Personally Identifying Information (PII) from conversations
+title: Identify and extract Personally Identifiable Information (PII) from conversations
 titleSuffix: Foundry Tools
-description: This article shows you how to detect and redact Personally Identifying Information (PII) from speech, chat, and spoken-word transcriptions and call transcripts.
+description: This article shows you how to detect and redact Personally Identifiable Information (PII) from speech, chat, and spoken-word transcriptions and call transcripts.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
@@ -10,7 +10,7 @@ ms.date: 04/03/2026
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
-# Detect and redact Personally Identifying Information in conversations
+# Detect and redact Personally Identifiable Information in conversations
 
 Azure Language in Foundry Tools conversation PII API analyzes audio discourse to identify and redact sensitive information (PII) using various predefined categories. This API works on both transcribed text (referred to as transcripts) and chats. For transcripts, it also facilitates the redaction of audio segments containing PII by providing the timing information for those segments.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話から個人を特定できる情報（PII）を削除する方法の修正"
}
```

### Explanation
この変更は、「会話から個人を特定できる情報（PII）を削除する方法」ファイル（redact-conversation-pii.md）の内容に対する軽微な修正を示しています。具体的には、タイトルおよび説明文における用語の一貫性を図るために、「Personally Identifying Information」という表現が「Personally Identifiable Information」に修正されています。

この修正により、文章全体の用語が統一され、正確な情報の提供がより強化されます。また、記事の内容はAzure Languageサービスにおける会話からのPIIの識別および削除について詳細に説明しており、音声対話を分析して敏感な情報を検出および削除するプロセスを扱っています。このような用語の一貫性を保つことは、専門的なドキュメントにおいて重要であり、ユーザーが情報を容易に理解できるよう支援します。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-document-pii.md{#item-5509ee}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: Identify and extract Personally Identifying Information (PII) from native documents
+title: Identify and extract Personally Identifiable Information (PII) from native documents
 titleSuffix: Foundry Tools
-description: This article shows you how to redact Personally Identifying Information (PII) from native documents.
+description: This article shows you how to redact Personally Identifiable Information (PII) from native documents.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
@@ -10,7 +10,7 @@ ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
-# Detect and redact Personally Identifying Information in native documents (preview)
+# Detect and redact Personally Identifiable Information in native documents (preview)
 
 > [!IMPORTANT]
 >
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ネイティブドキュメントからの個人を特定できる情報（PII）の削除方法の修正"
}
```

### Explanation
この変更は、「ネイティブドキュメントからの個人を特定できる情報（PII）の削除方法」ファイル（redact-document-pii.md）における軽微な修正を示しています。具体的には、タイトル及び説明文における用語の一貫性を強化するために、「Personally Identifying Information」という表現が「Personally Identifiable Information」に修正されています。

この修正によって、文書内の用語が統一され、情報の正確さが向上します。また、この記事はAzureのFoundry Toolsを用いて、ネイティブドキュメントからPIIを特定し削除する方法に焦点を当てており、読者が適切に手続きを理解できるよう支援しています。専門的なドキュメントにおいては、用語の正確な使用が特に重要であり、ユーザーが記事の内容を正確に理解しやすくするための配慮がなされています。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-text-pii.md{#item-9e48af}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: Identify and extract Personally Identifying Information (PII) from text
+title: Identify and extract Personally Identifiable Information (PII) from text
 titleSuffix: Foundry Tools
-description: This article shows you how to identify, extract, and redact Personally Identifying Information (PII) from text.
+description: This article shows you how to identify, extract, and redact Personally Identifiable Information (PII) from text.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
@@ -11,7 +11,7 @@ ms.author: lajanuar
 ms.custom: language-service-pii
 ---
 <!-- markdownlint-disable MD025 -->
-# Detect and redact Personally Identifying Information in text
+# Detect and redact Personally Identifiable Information in text
 
 Azure Language in Foundry Tools is a cloud-based service that applies Natural Language Processing (NLP) features to text-based data. The PII feature can evaluate unstructured text, extract, and redact sensitive information (PII) and health information (PHI) in text across several [predefined categories](../concepts/entity-categories.md).
 
@@ -318,4 +318,4 @@ When you get results from PII detection, you can stream the results to an applic
 
 ## Next steps
 
-[Personally Identifying Information (PII) overview](../overview.md)
+[Personally Identifiable Information (PII) overview](../overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキストから個人を特定できる情報（PII）を削除する方法の修正"
}
```

### Explanation
この変更は、「テキストからの個人を特定できる情報（PII）の削除方法」ファイル（redact-text-pii.md）に対する軽微な修正を示しています。具体的には、タイトル、説明文、および文中の用語を統一するために、「Personally Identifying Information」という表現を「Personally Identifiable Information」に修正しています。

これにより、文書中の用語が一貫し、読者に対して正確で分かりやすい内容が提供されるようになります。記事自体は、AzureのFoundry ToolsのNLP機能を使用して、テキストベースデータからPIIおよび健康情報（PHI）を評価、抽出、削除する方法について詳細に扱っています。また、最後の部分では、PII検出から得られる結果をアプリケーションにストリーミングする方法について言及しています。このような用語の一貫性は、ドキュメントの品質を高め、ユーザーの理解を助ける重要な要素です。

## articles/ai-services/language-service/personally-identifiable-information/how-to/use-containers.md{#item-8c61d4}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Use personally identifiable information (PII) detection Docker containers on-premises
 titleSuffix: Foundry Tools
-description: Use Docker containers for the Personally Identifiable Information (PII) detection API to determine the language of written text, on-premises.
+description: Use Docker containers for the Personally Identifiable Information (PII) detection API to detect and redact sensitive entities on-premises.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オンプレミスでの個人を特定できる情報（PII）検出用Dockerコンテナの利用方法の修正"
}
```

### Explanation
この変更は、「オンプレミスでの個人を特定できる情報（PII）検出用Dockerコンテナの利用方法」ファイル（use-containers.md）に関する軽微な修正を示しています。具体的には、説明文が「言語を判断する」ことから「センシティブなエンティティを検出し削除する」ことに変更されました。

この修正により、記事が提供する内容がより明確になり、Dockerコンテナを使用したPII検出APIの機能についての理解が深まります。特に、センシティブなエンティティの検出および削除に関する情報が強調されることで、読者が実際の利用シナリオにおいて何を期待できるかがより具体的に示されるようになります。記事は、AzureのFoundry Toolsにおける技術的な内容をカバーしており、正しい理解が得られるように情報が整理されています。

## articles/ai-services/language-service/personally-identifiable-information/includes/development-options.md{#item-1bd5c9}

<details>
<summary>Diff</summary>
````diff
@@ -12,5 +12,5 @@ To use PII detection, you submit text for analysis and handle the API output in
 |Development option  |Description  |
 |---------|---------|
 |[**Microsoft Foundry (new)**](https://ai.azure.com/) portal| Foundry (new) is a cloud-based AI platform that provides streamlined access to Foundry models, agents, and tools through Foundry projects.
-|[**Foundry (classic)**](https://ai.azure.com/) portal| Foundry (classic) is a cloud-based platform that supports hub-based projects and other resource types. When you sign up, you can use your own data to detect personally identifying information within text examples.|
+|[**Foundry (classic)**](https://ai.azure.com/) portal| Foundry (classic) is a cloud-based platform that supports hub-based projects and other resource types. When you sign up, you can use your own data to detect personally identifiable information within text examples.|
 |[**REST API or Client library (Azure SDK)**](/rest/api/language/analyze-text/analyze-text/analyze-text)| Integrate PII detection into your applications using the REST API, or the client library available in various languages.|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "開発オプションに関する文書の修正"
}
```

### Explanation
この変更は、「開発オプション」ファイル（development-options.md）の内容を軽微に修正したものです。具体的には、「Foundry (classic)」に関する説明文において、用語が「personally identifying information」から「personally identifiable information」に修正されました。

この修正は、用語の統一性を高め、読者に対する明確さを向上させる目的があります。文書は、AzureのAIプラットフォームであるFoundryに関連する情報を提供しており、ユーザーがテキスト例内で個人を特定できる情報を検出するために自身のデータを使用できることを明示しています。また、REST APIやクライアントライブラリを利用してPII検出をアプリケーションに統合するための選択肢も提供されています。全体として、これにより情報の整合性が保たれ、開発者にとって有用なリソースとなることを意図しています。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/azure-ai-foundry.md{#item-ff89fc}

<details>
<summary>Diff</summary>
````diff
@@ -60,7 +60,7 @@ Select either **Extract PII from conversation** or **Extract PII from text** fro
 
 ### Extract PII from conversation
 
-**Extract PII from conversation** is designed to identify and mask personally identifying information in conversational text.
+**Extract PII from conversation** is designed to identify and mask personally identifiable information in conversational text.
 
 In **Configuration** there are the following options:
 
@@ -91,7 +91,7 @@ Verify that each PII entity appears highlighted with the correct category label.
 
 ### Extract PII from text
 
-**Extract PII from text** is designed to identify and mask personally identifying information in text.
+**Extract PII from text** is designed to identify and mask personally identifiable information in text.
 
 In **Configuration** you can select from the following options:
 
@@ -161,7 +161,7 @@ There are two ways to access the PII interface:
 
 ## Detect PII in the Foundry playground
 
-The **extract PII from text** feature detects and masks personally identifying information within written content.
+The **extract PII from text** feature detects and masks personally identifiable information within written content.
 
 1. On the **Playground** tab, select the sample text, use the paperclip icon to upload your text, or enter your own text.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundry クイックスタートに関する文書の修正"
}
```

### Explanation
この変更は、「Azure AI Foundry」に関するクイックスタートファイル（azure-ai-foundry.md）の内容を軽微に修正したものです。具体的には、「personally identifying information」という表現がすべて「personally identifiable information」に修正されました。この変更は、用語の一貫性と正確性を保つためのものであり、特に個人を特定できる情報に関する記述において、より適切な表現を使用することを目的としています。

文書内では、会話からのPII抽出やテキストからのPII抽出の方法について説明されており、それぞれの機能がどのように個人を特定できる情報を特定しマスクするのかが解説されています。また、設定オプションや、FoundryプレイグラウンドでのPII検出手順についても詳細に記載されています。これにより、ユーザーがAzure AI技術を効果的に活用し、個人情報の保護に関する機能を理解できるようになっています。全体として、この変更は、ドキュメントの読みやすさと正確さを向上させることに寄与しています。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/rest-api.md{#item-842eb5}

<details>
<summary>Diff</summary>
````diff
@@ -52,7 +52,7 @@ In a code editor, create a new file named `test_pii_payload.json` and copy the f
 
 Save `test_pii_payload.json` somewhere on your computer. For example, your desktop.  
 
-## Send a personally identifying information (PII) detection API request
+## Send a personally identifiable information (PII) detection API request
 
 Use the following commands to send the API request using the program you're using. Copy the command into your terminal, and run it.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIクイックスタートに関する文書の修正"
}
```

### Explanation
この変更は、「REST API」に関するクイックスタートファイル（rest-api.md）の内容を軽微に修正したものです。具体的には、「personally identifying information」という表現が「personally identifiable information」に修正されました。この変更は、用語の統一性を高め、正確な情報提供を目指すものです。

文書では、個人を特定できる情報（PII）の検出APIリクエストを送信するための手順が説明されています。ユーザーがコードエディタ内で新しいファイルを作成し、必要なデータを保存した後、ターミナルでAPIリクエストを送信する方法を指示しています。この修正により、読者に対してより明確で正確な指示が提供され、APIの使用に関する理解を深めることができるようになっています。全体として、この変更は、ドキュメントの品質と読みやすさを向上させることに寄与しています。

## articles/ai-services/language-service/personally-identifiable-information/language-support.md{#item-d332b1}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Personally Identifiable Information (PII) detection language support
 titleSuffix: Foundry Tools
-description: This article explains which natural languages the PII detection feature supports of Azure Language in Foundry Tools.
+description: This article explains which natural languages the PII detection feature in Azure Language in Foundry Tools supports.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
@@ -10,11 +10,16 @@ ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-pii, build-2024
 ---
+<!-- markdownlint-disable MD025 -->
 # Personally Identifiable Information (PII) detection language support
 
-Use this article to learn which natural languages text PII, document PII, and conversation PII features support.
+Use this article to learn which natural languages each PII feature type supports:
 
-# [Text PII](#tab/text)
+* Text PII
+* Conversation PII
+* Document-based PII
+
+# [Text PII](#tab/text-pii)
 
 ## Text PII language support
 
@@ -100,9 +105,26 @@ Use this article to learn which natural languages text PII, document PII, and co
 |Vietnamese           |`vi`         |                  |
 |Welsh                |`cy`         |                  |
 
-# [PII for documents](#tab/documents)
+# [Conversation PII](#tab/conversation-pii)
+
+## Conversation PII language support
+
+Conversation PII preview version `2023-04-15-preview` supports the following languages:
+
+* English
+* French
+* German
+* Spanish
+
+Conversation PII generally available (GA) version currently supports the following languages:
+
+* English
+* French
+* Spanish
+
+# [Document-based PII](#tab/document-based-pii)
 
-## PII language support
+## Document-based PII language support
 
 |Language             |Language code|Notes             |
 |---------------------|-------------|------------------|
@@ -186,28 +208,13 @@ Use this article to learn which natural languages text PII, document PII, and co
 |Chinese-Simplified   |`zh-hans`    |`zh` also accepted|
 |Chinese-Traditional  |`zh-hant`    |                  |
 
-# [PII for conversations](#tab/conversations)
-
-## PII language support
-
-PII conversation preview version `2023-04-15-preview` supports the following languages:
-
-* English
-* French
-* German
-* Spanish
-
-
-PII conversation generally available (GA) version currently supports the following languages:
-
-* English
-* French
-* Spanish
-
-
-
 ---
 
 ## Next steps
 
-[PII feature overview](overview.md)
+Use these PII pages for implementation details:
+
+* [Text PII overview](text-pii-overview.md)
+* [Conversation PII overview](conversation-pii-overview.md)
+* [Document-based PII overview](document-based-pii-overview.md)
+* [PII feature overview](overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PII検出機能の言語サポートに関する文書の更新"
}
```

### Explanation
この変更は、「PII検出機能に関する言語サポート」を説明する文書（language-support.md）の内容を更新したものです。主な修正点として、説明文の文言が若干変更され、PII機能の各タイプがより明確に列挙されるようになりました。

具体的には、文書の冒頭で「テキスト PII」、「会話 PII」、「ドキュメントベース PII」という3つの機能が明示的にリストされ、読者がどの言語がどのPII機能に対応しているかを一目で理解できるように工夫されています。また、「会話 PII」と「ドキュメントベース PII」についての言語サポート情報が追加され、各機能の利用可能な言語が詳しく示されています。

文章構成も整理され、情報提供がより直感的に行えるように配慮されています。ユーザーはこれにより、各機能の言語サポートに関する情報に簡単にアクセスできるようになり、Azure Languageサービスを効果的に利用する手助けとなります。全体として、この変更は文書の整頓と情報の明確さを向上させています。

## articles/ai-services/language-service/personally-identifiable-information/media/document-pii-workflow.png{#item-abc2bc}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ドキュメントPIIワークフロー画像の追加"
}
```

### Explanation
この変更は、ドキュメント内に新たに画像ファイル「document-pii-workflow.png」を追加したものです。この画像は、個人を特定できる情報（PII）に関連するドキュメントワークフローの視覚的な説明を提供することを目的としています。

画像の追加によって、読者はPII検出プロセスの流れや手順を視覚的に理解しやすくなります。テキストだけでは伝わりにくい情報を明確にするための補助的な資料として機能し、ドキュメント全体の理解を深めることに役立ちます。新しいビジュアルコンテンツを組み込むことにより、ユーザー体験が向上し、情報の消化が容易になることが期待されます。全体として、この変更は文書に対する有用性を高める重要な要素となっています。

## articles/ai-services/language-service/personally-identifiable-information/media/feature-types.png{#item-6d598e}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "特徴タイプ画像の追加"
}
```

### Explanation
この変更は、個人を特定できる情報（PII）に関連する特徴タイプを示す新しい画像ファイル「feature-types.png」をドキュメントに追加したものです。この画像は、PII機能の異なるタイプを視覚的に表現することで、読者に各機能の理解を促進することを目的としています。

画像の追加により、テキスト情報だけでなくビジュアル情報を提供することで、複雑な概念が明確になり、ユーザーがPII機能をより簡単に把握できるようになります。特に技術的な内容を扱う文書において、視覚的な補足は理解を助ける重要な要素となります。この変更は、全体的な文書の質を高め、情報の伝達をより効果的にするための重要なステップです。

## articles/ai-services/language-service/personally-identifiable-information/overview.md{#item-8a6932}

<details>
<summary>Diff</summary>
````diff
@@ -1,23 +1,23 @@
 ---
-title: What is the Personally Identifying Information (PII) detection feature in Azure Language?
+title: What is the Personally Identifiable Information (PII) detection feature in Azure Language?
 titleSuffix: Foundry Tools
 description: An overview of the PII detection feature in Azure Language, which helps you extract entities and sensitive information (PII) in text.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 03/30/2026
+ms.date: 04/16/2026
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
 
 <!-- markdownlint-disable MD025 -->
 # What is PII detection in Azure Language?
 
-Personally Identifiable Information (PII) detection is an Azure Language [core capability](../overview.md#core-capabilities). The PII detection service is a cloud-based API that uses machine learning to **identify and redact** sensitive information from input data. The service classifies sensitive personal data into predefined categories such as phone numbers, email addresses, and identification documents.
+Personally Identifiable Information (PII) detection is an Azure Language [core capability](../overview.md#core-capabilities) that helps you identify, classify, and redact sensitive data across text, conversations, and native documents. Submit input text to the service and receive structured output with entity categories, confidence scores, and redacted results based on your API configuration. You can use this capability to implement privacy controls, reduce sensitive data exposure, and support compliance requirements in application and data-processing workflows.
 
 > [!TIP]
-> Try PII detection [in Microsoft Foundry portal](https://ai.azure.com/). There you can [utilize a currently existing Language Studio resource or create a new Foundry resource](../../../ai-services/connect-services-foundry-portal.md).
+> Try PII detection in [Microsoft Foundry](https://ai.azure.com/) and choose the feature type that matches your input data.
 
 ## Video demonstration
 
@@ -31,105 +31,120 @@ In this video, we introduce the PII detection service and show you how it detect
 
 Closed captions are available for this video.
 
-## Capabilities
+## PII documentation by feature type
 
- Currently, PII support is available for the following capabilities:
+PII capabilities are grouped by feature type. Each feature type maps to a specific input format and processing model.
 
-* [General text PII detection](how-to/redact-text-pii.md) for processing sensitive information (PII) and health information (PHI) in unstructured text across several [predefined categories](concepts/entity-categories.md).
-* [Conversation PII detection](how-to/redact-conversation-pii.md), a specialized model designed to handle speech transcriptions and the informal, conversational tone found in meeting and call transcripts.
-* [Native Document PII detection](how-to/redact-document-pii.md) for processing structured document files.
+:::image type="content" source="media/feature-types.png" alt-text="Screenshot of PII feature types diagram.":::
 
-### [Text PII](#tab/text-pii)
+Choose the feature type that matches your data shape and runtime requirements.
 
-Language is a cloud-based service that applies Natural Language Processing (NLP) features to detect categories of personal information (PII) in text-based data. This documentation contains the following types:
+### Text PII
 
-* **[Quickstarts](quickstart.md)** are getting-started instructions to guide you through making requests to the service.
-* **[How-to guides](how-to/redact-text-pii.md)** contain instructions for using the service in more specific or customized ways.
+[**Text PII**](text-pii-overview.md) processes string-based payloads and returns synchronous detection and redaction results. Use this feature when your system handles request-time processing for messages, prompts, logs, and other text fields.
 
-[!INCLUDE [Typical workflow for pre-configured language features](../includes/overview-typical-workflow.md)]
+Use the following documentation to implement and tune Text PII workloads:
 
-### Key features for text PII
+* [Quickstart: Detect personally identifiable information (PII)](quickstart.md)
+* [Detect and redact Personally Identifiable Information in text](how-to/redact-text-pii.md)
+* [Text PII recognized entity categories (extended format)](concepts/entity-categories.md)
+* [Text PII recognized entity categories (list format)](concepts/entity-categories-list.md)
 
-Language offers named entity recognition to identify and categorize information within your text. The feature detects PII categories including names, organizations, addresses, phone numbers, financial account numbers or codes, and government identification numbers. A subset of this PII is protected health information (PHI). By specifying domain=phi in your request, only PHI entities are returned.
+### Conversation PII
 
-### [Conversation PII](#tab/conversation-pii)
+[**Conversation PII**](conversation-pii-overview.md) processes multi-turn exchanges and transcript-oriented payloads where turn boundaries and conversation context affect detection and masking behavior. Use this feature for asynchronous workloads that analyze chat and transcript structures.
 
-The Language conversation PII API processes audio conversations to detect and remove sensitive information (PII) based on a set of predefined categories. This documentation contains the following types:
+Use the following documentation to implement Conversation PII job-based processing:
 
-* **[Quickstarts](quickstart.md)** are getting-started instructions to guide you through making requests to the service.
-* **[How-to guides](how-to/redact-conversation-pii.md)** contain instructions for using the service in more specific or customized ways.
+* [Conversation PII overview](conversation-pii-overview.md)
+* [Detect and redact Personally Identifiable Information in conversations](how-to/redact-conversation-pii.md)
+* [Conversation PII recognized entity categories (extended format)](concepts/conversations-entity-categories.md)
+* [Conversation PII recognized entity categories (list format)](concepts/conversations-entities-list.md)
 
-### Key features for conversation PII
+### Document-based PII
 
-Conversation PII uses natural language processing techniques to identify and categorize information within conversations. This feature supports both natural chat transcripts and transcribed transcripts from phone calls. For a chat or call, there are different kinds of important information, scattered over long text or transcripts.
+[**Document-based PII**](document-based-pii-overview.md) processes native files and returns redaction output that preserves document structure while also producing machine-readable metadata. Use this feature for asynchronous, storage-based pipelines that handle `.pdf`, `.docx`, and `.txt` inputs.
 
-### [Native document PII](#tab/native-document-pii)
+Use the following documentation to implement Document-based PII in native-file pipelines:
 
-The native document support feature allows you to send API requests asynchronously. You can use an HTTP POST request body to transmit your data and an HTTP GET request query string to check the status of your requests. Your processed documents are stored in your designated Azure Blob Storage container. This documentation contains the following types:
+* [Document-based PII overview](document-based-pii-overview.md)
+* [Detect and redact Personally Identifiable Information in native documents](how-to/redact-document-pii.md)
 
-* **[Quickstarts](quickstart.md)** are getting-started instructions to guide you through making requests to the service.
-* **[How-to guides](how-to/redact-document-pii.md)** contain instructions for using the service in more specific or customized ways.
+---
 
-### Key features for native document PII
+## Choose the right PII feature
 
-Document PII uses natural language processing techniques to identify and categorize information within documents.
+Use the following table to select the right experience before you start implementation:
 
----
+| Feature type | Input | Best for | Key strength |
+| --- | --- | --- | --- |
+| [Text PII](text-pii-overview.md) | Raw text strings | Apps, prompts, logs, tickets | Broad language coverage and flexible redaction options |
+| [Conversation PII](conversation-pii-overview.md) | Turn-based chat or transcript data | Contact centers, meetings, voice transcripts | Conversational context and transcript-aware output |
+| [Document-based PII](document-based-pii-overview.md) | Native files (`.pdf`, `.docx`, `.txt`) | Compliance workflows and document sharing | Redacted files with document fidelity and JSON metadata |
 
-## Get started with PII detection
+## Get started
 
 [!INCLUDE [development options](./includes/development-options.md)]
 
-[!INCLUDE [Developer reference](../includes/reference-samples-text-analytics.md)]
+[!INCLUDE [Typical workflow for pre-configured language features](../includes/overview-typical-workflow.md)]
 
-## Input requirements and service limits
+## What differs across feature types?
 
-### [Text PII](#tab/text-pii)
+All feature types use predefined entity categories and return confidence-scored detections. They differ mainly by input format and processing model:
 
-* Text PII takes text for analysis. For more information, see [Data and service limits](../concepts/data-limits.md) in the how-to guide.
-* PII works with various written languages. For more information, see [language support](language-support.md?tabs=text-summarization). You can specify in which [supported languages](../concepts/language-support.md) your source text is written. If you don't specify a language, the extraction defaults to English. The API may return offsets in the response to support different [multilingual and emoji encodings](../concepts/multilingual-emoji-support.md).
+* **Text PII** is optimized for synchronous string-based input.
+* **Conversation PII** is optimized for turn-based transcript and chat structures.
+* **Document-based PII** is asynchronous and optimized for processing native files while preserving document structure.
 
-### [Conversation PII](#tab/conversation-pii)
+> [!NOTE]
+> **Document-based PII** focuses on native-file redaction workflows. Some text-only options are not available in every document API version.
 
-* Conversation PII takes structured text for analysis. For more information, see [data and service limits](../concepts/data-limits.md).
-* Conversation summarization works with various spoken languages. For more information, see [language support](language-support.md?tabs=conversation-summarization).
-* [!INCLUDE [service limits article](../includes/service-limits-link.md)]
+## GA and preview guidance
 
-### [Native document PII](#tab/native-document-pii)
+To avoid integration issues, use API versions and features that match your deployment target:
 
-* Native document PII takes text for analysis. For more information, see [Data and service limits](../concepts/data-limits.md) in the how-to guide.
-* Native document PII works with various written languages. For more information, see [language support](language-support.md?tabs=document-summarization).
+* Use generally available (GA) API versions for production workloads.
+* Use preview API versions only when you need preview-only features.
+* Avoid combining request payload examples from different API versions.
 
-A native document refers to the file format used to create the original document such as Microsoft Word (docx) or a portable document file (pdf). Native document support eliminates the need for text preprocessing before using Language resource capabilities. Currently, native document support is available for the [**PiiEntityRecognition**](../personally-identifiable-information/concepts/entity-categories.md) capability.
+Each feature-specific how-to article identifies preview-only sections where applicable.
 
- Currently **PII** supports the following native document formats:
+## Input requirements and service limits
 
-|File type|File extension|Description|
-|---------|--------------|-----------|
-|Text| `.txt`|An unformatted text document.|
-|Adobe PDF| `.pdf`       |A portable document file formatted document.|
-|Microsoft Word|`.docx`|A Microsoft Word document file.|
+Use the following references to verify language coverage, service limits, and model-version behavior:
 
----
+* [Language support for text, document, and conversation PII](language-support.md)
+* [Quotas and limits](../concepts/data-limits.md)
+* [Model lifecycle and API version guidance](../concepts/model-lifecycle.md)
+
+[!INCLUDE [Developer reference](../includes/reference-samples-text-analytics.md)]
 
 ## Responsible AI
 
-An AI system includes not only the technology, but also the people who use it, the people affected by it, and the deployment environment. Read the [transparency note for PII](/azure/ai-foundry/responsible-ai/language-service/transparency-note-personally-identifiable-information) to learn about responsible AI use and deployment in your systems. For more information, see the following articles:
+You should design responsible solutions by considering the model behavior, the users who operate the system, and the people affected by the output. Read the [transparency note for PII](/azure/ai-foundry/responsible-ai/language-service/transparency-note-personally-identifiable-information) to understand responsible deployment guidance. For more information, see the following articles:
 
 [!INCLUDE [Responsible AI links](../includes/overview-responsible-ai-links.md)]
 
-## Example scenarios
+## Common use cases
+
+PII detection is useful when you need to apply privacy controls before storage, analytics, sharing, or downstream AI processing.
+
+Typical examples include:
 
-* **Apply sensitivity labels** - For example, based on the results from the PII service, a public sensitivity label might be applied to documents where no PII entities are detected. For documents where US addresses and phone numbers are recognized, a confidential label might be applied. A highly confidential label might be used for documents where bank routing numbers are recognized.
-* **Redact some categories of personal information from documents that get wider circulation** - For example, if customer contact records are accessible to frontline support representatives, the company can redact the customer's personal information besides their name from the version of the customer history to preserve the customer's privacy.
-* **Redact personal information in order to reduce unconscious bias** - For example, during a company's resume review process, they can block name, address, and phone number to help reduce unconscious gender or other biases.
-* **Replace personal information in source data for machine learning to reduce unfairness** – For example, if you want to remove names that might reveal gender when training a machine learning model, you could use the service to identify them and you could replace them with generic placeholders for model training.
-* **Remove personal information from call center transcription** – For example, if you want to remove names or other PII data that happen between the agent and the customer in a call center scenario. You could use the service to identify and remove them.
-* **Data cleaning for data science** - PII can be used to make the data ready for data scientists and engineers to be able to use these data to train their machine learning models. Redacting the data to make sure that customer data isn't exposed.
+* Applying sensitivity labels based on detected PII categories.
+* Redacting personal information in documents that are distributed more broadly.
+* Masking personal identifiers in resume screening workflows to reduce bias risk.
+* Replacing sensitive values with placeholders in machine learning training datasets.
+* Redacting names and contact details in call center transcription workflows.
+* Preparing datasets for analytics and data science without exposing customer data.
 
 ## Next steps
 
-There are two ways to get started using the entity linking feature:
+Use the following references to continue implementation:
 
-* [Foundry](../../../ai-foundry/what-is-foundry.md) is a web-based platform that lets you use several Language features without needing to write code.
-* The [quickstart article](quickstart.md) for instructions on making requests to the service using the REST API and client library SDK.
+* [Quickstart: Detect personally identifiable information (PII)](quickstart.md)
+* [Detect and redact Personally Identifiable Information in text](how-to/redact-text-pii.md)
+* [Detect and redact Personally Identifiable Information in conversations](how-to/redact-conversation-pii.md)
+* [Detect and redact Personally Identifiable Information in native documents](how-to/redact-document-pii.md)
+* [Language support for text, document, and conversation PII](language-support.md)
+* [Quotas and limits](../concepts/data-limits.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PII検出機能の概要ドキュメントの更新"
}
```

### Explanation
この変更は、Azure Languageの個人を特定できる情報（PII）検出機能に関する概要ドキュメント「overview.md」の内容を更新したものです。主な修正点には、説明の明確化や、機能の新しい用途や実装方法を詳述したことが含まれます。具体的には、PII検出の機能がどのように機能し、どのようなデータを処理できるか、また、その結果をどのように活用できるかを新たに説明しています。

また、特定の機能タイプに基づいてPIIの処理をグループ化するセクションが導入され、各機能タイプに対する具体的なドキュメントやクイックスタートガイドが追加されています。これにより、ユーザーは自分のニーズに最適な機能を簡単に見つけやすくなります。

加えて、テキストや会話、ドキュメントからのPII検出についての具体的な事例や、プライバシー制御を実施する際の一般的な利用ケースが新たに記載されています。この変更によって、文書全体の理解が深まり、読者にとって役立つ情報が増えることが期待されています。

## articles/ai-services/language-service/personally-identifiable-information/quickstart.md{#item-94affd}

<details>
<summary>Diff</summary>
````diff
@@ -22,15 +22,15 @@ zone_pivot_groups: programming-languages-text-analytics
 ai-usage: ai-assisted
 ---
 
-# Quickstart: Detect personally identifiable information (PII)
 <!-- markdownlint-disable MD025 -->
+# Quickstart: Detect personally identifiable information (PII)
 
 In this quickstart, you use the Azure Language in Foundry Tools PII detection feature to identify and redact personally identifiable information in text. You can get started using your preferred client library, the REST API, or the Microsoft Foundry portal.
 
 If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
 
 > [!NOTE]
-> This quickstart covers PII detection in documents. To detect PII in conversations, see [How to detect and redact PII in conversations](how-to/redact-conversation-pii.md). To detect PII in text, see [How to detect and redact PII in text](how-to/redact-text-pii.md).
+> This quickstart focuses on text PII. For conversation workflows, see [How to detect and redact PII in conversations](how-to/redact-conversation-pii.md). For document workflows, see [Document-based PII overview](document-based-pii-overview.md) and [How to detect and redact PII in native documents](how-to/redact-document-pii.md).
 
 ::: zone pivot="programming-language-csharp"
 
@@ -88,6 +88,7 @@ If you no longer need the resources you created in this quickstart, delete the i
 ## Related content
 
 * [PII overview](overview.md)
+* [Document-based PII overview](document-based-pii-overview.md)
 * [How to detect and redact PII in text](how-to/redact-text-pii.md)
 * [How to detect and redact PII in conversations](how-to/redact-conversation-pii.md)
 * [Supported entity categories for text](concepts/entity-categories.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PII検出のクイックスタートガイドの修正"
}
```

### Explanation
この変更は、Azure Languageの個人を特定できる情報（PII）検出機能に関するクイックスタートガイド「quickstart.md」の内容を修正したものです。主に、テキストやドキュメント、会話におけるPIIの検出に関する情報を整理し、正確なガイダンスを提供することを目的としています。

具体的には、クイックスタートガイドの冒頭部分で、PII検出の対象がドキュメントからテキストに焦点を移したことが明確に示されています。また、他の作業フロー（ドキュメントごとのPII検出や会話でのPII検出）へのリンクを改善し、それぞれに関連するリソースを参照しやすくしました。

これにより、ユーザーがPII検出の機能を使う際に、必要な情報に迅速にアクセスできるようになり、ドキュメント全体の使いやすさが向上します。さらに、関連するコンテンツへのリンクも追加され、より豊富な情報への導線が提供されています。

## articles/ai-services/language-service/personally-identifiable-information/text-pii-overview.md{#item-f33f06}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,90 @@
+---
+title: Text Personally Identifiable Information (PII) redaction overview
+titleSuffix: Foundry Tools
+description: Learn how text PII redaction in Azure Language detects and redacts sensitive data in raw text for applications and workflows.
+author: laujan
+manager: nitinme
+ms.service: azure-ai-language
+ms.topic: overview
+ms.date: 04/16/2026
+ms.author: lajanuar
+ms.custom: language-service-pii
+---
+
+<!-- markdownlint-disable MD025 -->
+# Text Personally Identifiable Information (PII) redaction overview
+
+Text PII redaction in Azure AI Language helps you detect and redact sensitive data in raw text strings. You can use this feature when your application handles logs, prompts, forms, chat messages, or other text content directly.
+
+Text PII is optimized for synchronous request/response integration and configurable redaction behavior, so you can apply PII controls inline in application and data-processing workflows.
+
+## At a glance
+
+Text PII provides the following capabilities:
+
+* Direct text redaction for unstructured string input.
+* Low-latency request/response integration for application pipelines.
+* Configurable entity filters and redaction policies.
+* Structured entity output with categories, offsets, and confidence scores.
+
+## Why use text PII?
+
+Text PII is optimized for low-latency integration and direct request/response workflows. It supports broad language coverage and configurable redaction behavior for many real-time and batch scenarios.
+
+Text PII is especially useful when you need to:
+
+* Redact sensitive entities in user-generated text.
+* Integrate PII protection directly into application pipelines.
+* Apply entity filters and redaction policies in API requests.
+
+## What it returns
+
+When a request succeeds, the service returns:
+
+* Detected entities with categories, subcategories, offsets, and confidence scores.
+* Redacted text output based on your selected redaction behavior.
+
+## How it works
+
+Text PII is typically used with a synchronous workflow:
+
+1. Submit text input for analysis.
+2. Configure optional parameters like entity filters and redaction behavior.
+3. Process entities and redacted output in your application.
+
+For implementation details and request samples, see [Detect and redact Personally Identifiable Information in text](how-to/redact-text-pii.md).
+
+## How it differs from other PII feature types
+
+All PII feature types use predefined entity categories, but they optimize for different input types:
+
+* Text PII is optimized for direct string-based input and app integration.
+* Conversation PII is optimized for turn-based conversational structures.
+* Document-based PII is optimized for native-file workflows and file output fidelity.
+
+## Common use cases
+
+Text PII is useful when you need to detect and redact sensitive data before storage, analytics, sharing, or downstream AI processing.
+
+Typical examples include:
+
+* User input and output fields in web and mobile applications.
+* Application logs and telemetry data streams.
+* Prompt and response filtering in AI workflows.
+* Batch preprocessing for unstructured text datasets.
+
+## Supported formats and limits
+
+* Input format: raw text content
+* See [language support](language-support.md) and [quotas and limits](../concepts/data-limits.md) for current support details.
+
+## Pricing
+
+Text PII redaction uses Azure AI Language pricing. For current pricing details, see [Azure AI Language pricing](https://aka.ms/unifiedLanguagePricing).
+
+## Next steps
+
+Use the following references to continue implementation:
+
+* [Detect and redact Personally Identifiable Information in text](how-to/redact-text-pii.md)
+* [PII feature overview](overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "テキストによる個人を特定できる情報（PII）削除の概要"
}
```

### Explanation
この変更は、Azure Languageサービスの新しいドキュメント「text-pii-overview.md」が追加されたことを示しています。このドキュメントは、テキストにおける個人を特定できる情報（PII）の検出と削除に関する概要を提供しています。

新たに追加されたこのドキュメントでは、テキストPIIの機能がどのように機能するのか、具体的なキャパビリティ、利用方法、リクエストの応答内容が詳述されています。特に、ログ、プロンプト、フォーム、チャットメッセージなどの生のテキストに対して、PII保護を直接組み込むことで、リアルタイムでのデータ処理が可能であることが強調されています。

さらに、テキストPIIの利点や、その結果として得られる情報、他のPII機能との違いについても述べられています。具体的な利用例、サポートされるフォーマット、価格情報、次のステップとして参照すべきリソースも含まれています。このドキュメントの追加によって、ユーザーはテキスト領域におけるPII保護の実装とその重要性を理解しやすくなるでしょう。

## articles/ai-services/language-service/question-answering/concepts/limits.md{#item-50708f}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-language
 author: laujan
 ms.author: lajanuar
 ms.topic: limits-and-quotas
-ms.date: 12/11/2025
+ms.date: 04/20/2026
 ---
 
 # Project limits and boundaries
@@ -42,7 +42,6 @@ File names may not include the following characters:
 |Format|Max file size (MB)|
 |--|--|
 |`.docx`|10|
-|`.pdf`|25|
 |`.tsv`|10|
 |`.txt`|10|
 |`.xlsx`|3|
@@ -84,15 +83,17 @@ The length and acceptable characters for metadata name and value are listed in t
 |||||
 
 ## Project content limits
+
 Overall limits on the content in the project:
+
 * Length of answer text: 25,000 characters
 * Length of question text: 1,000 characters
 * Length of metadata key text: 100 characters
 * Length of metadata value text: 500 characters
 * Supported characters for metadata name: Alphabets, digits, and `_`
 * Supported characters for metadata value: All except `:` and `|`
 * Length of file name: 200
-* Supported file formats: ".tsv", ".pdf", ".txt", ".docx", ".xlsx".
+* Supported file formats: ".tsv", ".txt", ".docx", ".xlsx".
 * Maximum number of alternate questions: 300
 * Maximum number of question-answer pairs: Depends on the **[Azure AI Search tier](/azure/search/search-limits-quotas-capacity#document-limits)** chosen. A question and answer pair maps to a document on Azure AI Search index.
 * URL/HTML page: 1 million characters
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "質問応答サービスの制限に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure Languageサービスの質問応答機能に関するドキュメント「limits.md」を更新したことを示しています。主に、プロジェクトの制限や制約に関する情報が修正され、最新の日付が設定されています。

具体的な変更点としては、以下の点が挙げられます：
- ドキュメントの日付が2025年12月11日から2026年4月20日に更新されました。
- 対応するファイル形式のリストから「.pdf」が削除され、サポートされるファイル形式が「.tsv」「.txt」「.docx」「.xlsx」のみとなりました。
- プロジェクト内のコンテンツに関する制限が追加され、回答テキストの長さや質問テキストの長さ、メタデータのキーおよび値の長さに関する具体的な制約が明記されました。

これらの更新により、ユーザーはAzureの質問応答サービスにおける制限をより正確に理解できるようになり、適切な利用方法についてのガイダンスが提供されます。新たなコンテンツ制限の明示により、APIやサービスの使用に関する期待値がより明確になっています。

## articles/ai-services/language-service/question-answering/how-to/authoring.md{#item-855d84}

<details>
<summary>Diff</summary>
````diff
@@ -285,7 +285,7 @@ curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applicat
           },
           {
             "displayName": "source2",
-            "sourceUri": "https://download.microsoft.com/download/2/9/B/29B20383-302C-4517-A006-B0186F04BE28/surface-pro-4-user-guide-EN.pdf",
+            "sourceUri": "https://support.microsoft.com/en-US/surface/models/surface-book-3-specs-and-features",
             "sourceKind": "file",
             "contentStructureKind": "unstructured",
             "lastUpdatedDateTime": "2021-05-01T15:13:22Z"
@@ -601,7 +601,7 @@ curl -X PATCH -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applic
     "value": {
       "displayName": "source5",
       "sourceKind": "url",
-      "sourceUri": "https://download.microsoft.com/download/7/B/1/7B10C82E-F520-4080-8516-5CF0D803EEE0/surface-book-user-guide-EN.pdf",
+      "sourceUri": "https://support.microsoft.com/en-US/surface/models/surface-book-3-specs-and-features",
       "sourceContentStructureKind": "semistructured"
     }
   }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "質問応答の著作に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure Languageサービスの質問応答機能に関するドキュメント「authoring.md」を更新したことを示しています。主に、特定の情報源（sourceUri）に関するリンクが新しいURLに更新されました。

具体的には、以下の変更が行われました：
- 以前の情報源として「surface-pro-4-user-guide-EN.pdf」のダウンロードリンクが、新しいリンク「surface-book-3-specs-and-features」のサポートページに置き換えられています。この変更は、二つの異なる場所での類似した情報に関して行われました。

これにより、ユーザーに対して、より有用で関連性の高いリソースが提供されるようになっています。この更新は、情報の正確性および関連性を維持するためのものであり、ユーザーが最新の情報にアクセスできることを目指しています。

## articles/ai-services/language-service/question-answering/how-to/create-test-deploy.md{#item-80a22f}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-language
 ms.topic: how-to
 author: laujan
 ms.author: lajanuar
-ms.date: 12/15/2025
+ms.date: 04/20/2026
 ms.custom: language-service-question-answering, mode-other
 ---
 # Create, test, and deploy: CQA knowledge base
@@ -81,12 +81,12 @@ A CQA knowledge base is a structured set of question-and-answer pairs optimized
 1. In the **Add URLs** window, add the following values:
 
    * **URL name**: **Surface Book User Guide**
-   * **URL**: **https://download.microsoft.com/download/7/B/1/7B10C82E-F520-4080-8516-5CF0D803EEE0/surface-book-user-guide-EN.pdf** 
+   * **URL**: **<https://support.microsoft.com/en-US/surface/models/surface-book-3-specs-and-features>**
    * **Classify file structure**: Leave the default setting (**Auto-detect**)
 
      :::image type="content" source="../media/agents/add-urls.png" alt-text="Screenshot of the select url source selection and add button in the Foundry.":::
 
-1. Finally, select the **Add URLs** button. 
+1. Finally, select the **Add URLs** button.
 
     The extraction process requires a short amount of time to analyze the document and detect questions and answers. During this step, the service evaluates whether the content is structured or unstructured.<br>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "CQA知識ベース作成手順の更新"
}
```

### Explanation
この変更は、Azure Languageサービスにおける質問応答機能の「create-test-deploy.md」ドキュメントを更新したもので、主に文書の日付と情報源のURLが変更されています。

具体的な変更内容は以下の通りです：
- ドキュメントの日付が2025年12月15日から2026年4月20日に更新されました。
- 「Add URLs」ウィンドウ内のURL情報が更新され、以前のリンク「surface-book-user-guide-EN.pdf」から新しいリンク「surface-book-3-specs-and-features」のサポートページに変更されました。

これにより、最新のリソースへのアクセスが可能になり、ユーザーはより関連性のある情報を得ることができます。この更新は、ドキュメントの正確性と有用性を向上させるために実施されています。

## articles/ai-services/language-service/question-answering/how-to/export-import-refresh.md{#item-2d1b56}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.topic: how-to
 author: laujan
 ms.author: lajanuar
 recommendations: false
-ms.date: 12/15/2025
+ms.date: 04/20/2026
 ---
 # Export-import-refresh in custom question answering
 
@@ -21,7 +21,6 @@ You might want to create a copy of your custom question answering project or rel
 * An Azure subscription. You can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
 * A [language resource](https://aka.ms/create-language-resource) with the custom question answering feature enabled. Remember your Microsoft Entra ID, Subscription, language resource name you selected when you created the resource.
 
-
 ### Export a project programmatically
 
 To automate the export process, use the [export functionality of the authoring API](./authoring.md#export-project-metadata-and-assets)
@@ -49,14 +48,13 @@ curl -X PATCH -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applic
     "value": {
       "displayName": "source5",
       "sourceKind": "url",
-      "sourceUri": https://download.microsoft.com/download/7/B/1/7B10C82E-F520-4080-8516-5CF0D803EEE0/surface-book-user-guide-EN.pdf,
+      "sourceUri": "https://support.microsoft.com/en-US/surface/models/surface-book-3-specs-and-features",
       "refresh": "true"
     }
   }
 ]'  -i 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}/sources?api-version=2021-10-01'
 ```
 
-
 ## Next steps
 
 * [Learn how to use the Authoring API](./authoring.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム質問応答のエクスポート/インポート手順の更新"
}
```

### Explanation
この変更は、Azure Languageサービスにおけるカスタム質問応答の「export-import-refresh.md」ドキュメントの更新を示しています。主な変更点は、日付の更新と情報源のURLの修正です。

具体的な変更内容には次のものが含まれます：
- ドキュメントの日付が2025年12月15日から2026年4月20日に変更されました。
- エクスポート手順に関連するURLが、以前のリンク「surface-book-user-guide-EN.pdf」から新しいリンク「surface-book-3-specs-and-features」のサポートページに更新されました。

また、文書内の他の情報の整理がされ、プロジェクトのエクスポート手続きを簡素化するための内容が提供されています。この更新により、ユーザーがより正確な情報を得られるようになり、カスタム質問応答機能の利用が促進されています。

## articles/ai-services/language-service/question-answering/includes/rest.md{#item-e6e1b0}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: "Quickstart: Use cURL & REST to manage project - custom question answering"
 description: This quickstart shows you how to create, publish, and query your project using the REST APIs.
-ms.date: 12/15/2025
+ms.date: 04/20/2026
 ms.topic: include
 author: laujan
 ms.author: lajanuar
@@ -11,9 +11,9 @@ ms.author: lajanuar
 * The current version of [cURL](https://curl.haxx.se/). Several command-line switches are used in the quickstarts, which are noted in the [cURL documentation](https://curl.haxx.se/docs/manpage.html).
 * Azure subscription - [Create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)
 * Custom question answering requires a [Language resource](https://portal.azure.com/?quickstart=true#create/Microsoft.CognitiveServicesTextAnalytics) with the custom question answering feature enabled to generate an API key and endpoint.
-    * After your Language resource deploys, select **Go to resource**. You need the key and endpoint from the resource you create to connect to the API. Paste your key and endpoint into the code later in the quickstart.
+* After your Language resource deploys, select **Go to resource**. You need the key and endpoint from the resource you create to connect to the API. Paste your key and endpoint into the code later in the quickstart.
 * Create a Language resource with [Azure CLI](../../../multi-service-resource.md?pivots=azcli) and provide the following properties: `--api-properties qnaAzureSearchEndpointId=/subscriptions/<azure-subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.Search/searchServices/<azure-search-service-name> qnaAzureSearchEndpointKey=<azure-search-service-auth-key>`
-* An existing project to query. If you have not setup a project, you can follow the instructions in the [**Foundry quickstart**](../quickstart/sdk.md). Or add a project that uses this [Surface User Guide URL](https://download.microsoft.com/download/7/B/1/7B10C82E-F520-4080-8516-5CF0D803EEE0/surface-book-user-guide-EN.pdf) as a data source.
+* An existing project to query. If you have not setup a project, you can follow the instructions in the [**Foundry quickstart**](../quickstart/sdk.md). Or add a project that uses this [Surface User Guide URL](https://support.microsoft.com/en-US/surface/models/surface-book-3-specs-and-features) as a data source.
 
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム質問応答プロジェクト管理手順の更新"
}
```

### Explanation
この変更は、Azure Languageサービスのカスタム質問応答に関する「rest.md」ドキュメントの更新を示しています。主な変更点は、ドキュメントの日付の更新といくつかのURLの修正です。

具体的な変更内容は以下の通りです：
- ドキュメントの日付が2025年12月15日から2026年4月20日に更新されました。
- 「Surface User Guide」として以前のリンク「surface-book-user-guide-EN.pdf」が新しいリンク「surface-book-3-specs-and-features」に変更されました。

これにより、リンク先の情報が最新の内容に更新され、ユーザーはカスタム質問応答のプロジェクトを設定する際に、関連性のある正確なリソースにアクセスできるようになります。この更新は、利用者にとっての利便性を向上させることが目的です。

## articles/ai-services/language-service/question-answering/includes/sdk-csharp.md{#item-af9649}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: This quickstart shows how to get started with the custom question a
 author: laujan
 ms.author: lajanuar
 ms.topic: include
-ms.date: 12/15/2025
+ms.date: 04/20/2026
 ---
 Use this quickstart for the custom question answering client library for .NET to:
 
@@ -24,9 +24,9 @@ Use this quickstart for the custom question answering client library for .NET to
 * Azure subscription - [Create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)
 * The [Visual Studio IDE](https://visualstudio.microsoft.com/vs/) or current version of [.NET Core](https://dotnet.microsoft.com/download/dotnet-core).
 * Custom question answering requires a [Language resource](https://portal.azure.com/?quickstart=true#create/Microsoft.CognitiveServicesTextAnalytics) with the custom question answering feature enabled to generate an API key and endpoint. 
-    * After your Language resource deploys, select **Go to resource**. You need the key and endpoint from the resource you create to connect to the API. Paste your key and endpoint into the code later in the quickstart.
+* After your Language resource deploys, select **Go to resource**. You need the key and endpoint from the resource you create to connect to the API. Paste your key and endpoint into the code later in the quickstart.
 * Create a Language resource with [Azure CLI](../../../multi-service-resource.md?pivots=azcli) and provide the following properties: `--api-properties qnaAzureSearchEndpointId=/subscriptions/<azure-subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.Search/searchServices/<azure-search-service-name> qnaAzureSearchEndpointKey=<azure-search-service-auth-key>`
-* An existing project to query. If you don't have a project, you can follow the instructions in the [**Microsoft Foundry quickstart**](../quickstart/sdk.md). Or add a project that uses this [Surface User Guide URL](https://download.microsoft.com/download/7/B/1/7B10C82E-F520-4080-8516-5CF0D803EEE0/surface-book-user-guide-EN.pdf) as a data source.
+* An existing project to query. If you don't have a project, you can follow the instructions in the [**Microsoft Foundry quickstart**](../quickstart/sdk.md). Or add a project that uses this [Surface User Guide URL](https://support.microsoft.com/en-US/surface/models/surface-book-3-specs-and-features) as a data source.
 
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDKのカスタム質問応答クイックスタートの更新"
}
```

### Explanation
この変更は、Azure Languageサービスにおけるカスタム質問応答用のC# SDKに関する「sdk-csharp.md」ドキュメントの更新を示しています。主な変更点は、日付の更新といくつかのリンクの修正です。

具体的な変更内容は以下の通りです：
- ドキュメントの日付が2025年12月15日から2026年4月20日に更新されました。
- エクスポート手順に関連する情報源のURLが、以前の「Surface User Guide PDF」リンクから、現在の「Surface Book 3 スペックと機能」に関するリンクに変更されました。

これにより、ユーザーは最新の情報源に基づいてC# SDKを使用したカスタム質問応答プロジェクトを設定し、実行できるようになります。この更新は、リソースへのアクセスを容易にし、利用者がよりスムーズに作業を進められることを目的としています。

## articles/ai-services/language-service/question-answering/includes/sdk-python.md{#item-33436a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: This quickstart shows how to get started with the custom question a
 ms.topic: include
 author: laujan
 ms.author: lajanuar
-ms.date: 12/15/2025
+ms.date: 04/20/2026
 ---
 Use this quickstart for the custom question answering client library for Python to:
 
@@ -25,7 +25,7 @@ Use this quickstart for the custom question answering client library for Python
 * Custom question answering requires a [Language resource](https://portal.azure.com/?quickstart=true#create/Microsoft.CognitiveServicesTextAnalytics) with the custom question answering feature enabled to generate an API key and endpoint.
     * After your Language resource deploys, select **Go to resource**. You need the key and endpoint from the resource you create to connect to the API. Paste your key and endpoint into the code later in the quickstart.
 * Create a Language resource with [Azure CLI](../../../multi-service-resource.md?pivots=azcli) and provide the following properties: `--api-properties qnaAzureSearchEndpointId=/subscriptions/<azure-subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.Search/searchServices/<azure-search-service-name> qnaAzureSearchEndpointKey=<azure-search-service-auth-key>`
-* An existing project to query. If you don't have a project, you can follow the instructions in the [**Microsoft Foundry quickstart**](../quickstart/sdk.md). Or add a project that uses this [Surface User Guide URL](https://download.microsoft.com/download/7/B/1/7B10C82E-F520-4080-8516-5CF0D803EEE0/surface-book-user-guide-EN.pdf) as a data source.
+* An existing project to query. If you don't have a project, you can follow the instructions in the [**Microsoft Foundry quickstart**](../quickstart/sdk.md). Or add a project that uses this [Surface User Guide URL](https://support.microsoft.com/en-US/surface/models/surface-book-3-specs-and-features) as a data source.
 
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python SDKのカスタム質問応答クイックスタートの更新"
}
```

### Explanation
この変更は、Azure Languageサービスにおけるカスタム質問応答用のPython SDKに関する「sdk-python.md」ドキュメントの更新を示しています。主な変更点は、日付の更新といくつかのリンクの修正です。

具体的な変更内容は以下の通りです：
- ドキュメントの日付が2025年12月15日から2026年4月20日に更新されました。
- エクスポート手順の関連情報源として以前の「Surface User Guide PDF」リンクから、現在の「Surface Book 3 スペックと機能」に関するリンクに変更されました。

この変更により、ユーザーは最新の情報源に基づいてPython SDKを利用したカスタム質問応答プロジェクトを設定し、実行できるようになります。これによって、リソースへのアクセスが容易になり、利用者がより効果的に作業を進められることが期待されます。

## articles/ai-services/language-service/question-answering/reference/document-format-guidelines.md{#item-fb0489}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,9 @@ ms.service: azure-ai-language
 ms.author: lajanuar
 author: laujan
 ms.topic: reference
-ms.date: 12/15/2025
+ms.date: 04/20/2026
 ---
+
 # Format guidelines for custom question answering
 
 Review these formatting guidelines to get the best results for your content.
@@ -31,7 +32,7 @@ Custom question answering identifies sections and subsections and relationships
 
 ### Product manuals
 
-A manual is typically guidance material that accompanies a product. It helps the user to set up, use, maintain, and troubleshoot the product. When custom question answering processes a manual, it extracts the headings and subheadings as questions and the subsequent content as answers. See an example [here](https://download.microsoft.com/download/2/9/B/29B20383-302C-4517-A006-B0186F04BE28/surface-pro-4-user-guide-EN.pdf).
+A manual is typically guidance material that accompanies a product. It helps the user to set up, use, maintain, and troubleshoot the product. When custom question answering processes a manual, it extracts the headings and subheadings as questions and the subsequent content as answers. For example, *see*, [Surface Book 3 Specs and Features guide](https://support.microsoft.com/en-US/surface/models/surface-book-3-specs-and-features).
 
 To follow is an example of a manual with an index page, and hierarchical content
 
@@ -50,21 +51,6 @@ To follow is an example of a semi-structured doc, without an index:
 > [!div class="mx-imgBorder"]
 > ![Azure Blob storage semi-structured Doc](../media/qnamaker-concepts-datasources/semi-structured-doc.png)
 
-### Unstructured document support
-
-Custom question answering now supports unstructured documents. A  document that doesn't have its content organized in a hierarchical manner, is missing a set structure or has its content free flowing can be considered as an unstructured document.
-
-To follow is an example of an unstructured PDF document:
-
-> [!div class="mx-imgBorder"]
-> ![Unstructured  document example for a project](../media/qnamaker-concepts-datasources/unstructured-qna-pdf.png)
-
-> [!NOTE]
-> QnA pairs aren't extracted in the "Edit sources" tab for unstructured sources.
-
-> [!IMPORTANT]
-> Support for unstructured file/content is available only in custom question answering.
-
 ### Structured custom question answering document
 
 The format for structured question-answers in DOC files is in the form of alternating questions and answers per line. It's one question per line followed by its answer in the following line, as shown:
@@ -112,7 +98,7 @@ Importing a project replaces the content of the existing project. Import require
 * First character of heading must be capitalized.
 * Don't end a heading with a question mark, `?`.
 
-**Sample documents**:<br>[Surface Pro (docx)](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/qna-maker/data-source-formats/multi-turn.docx)<br>[Contoso Benefits (docx)](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/qna-maker/data-source-formats/Multiturn-ContosoBenefits.docx)<br>[Contoso Benefits (pdf)](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/qna-maker/data-source-formats/Multiturn-ContosoBenefits.pdf)
+**Sample documents**:<br>[Surface Pro (docx)](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/qna-maker/data-source-formats/multi-turn.docx)<br>[Contoso Benefits (docx)](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/qna-maker/data-source-formats/Multiturn-ContosoBenefits.docx)<br>[Surface Book 3 (web)](https://support.microsoft.com/en-US/surface/models/surface-book-3-specs-and-features)
 
 ## FAQ URLs
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム質問応答に関するドキュメントフォーマットガイドラインの更新"
}
```

### Explanation
この変更は、Azure Languageサービスにおけるカスタム質問応答に関する「document-format-guidelines.md」ドキュメントの更新を示しています。主な変更点は、日付の更新といくつかの内容の修正、削除です。

具体的な変更内容は以下の通りです：
- ドキュメントの日付が2025年12月15日から2026年4月20日に更新されました。
- 「製品マニュアル」に関する説明が強化され、具体的な例として「Surface Book 3 スペックと機能ガイド」のリンクが追加されました。
- いくつかの未構造文書に関するセクションが削除され、その結果として関連内容が簡潔にされました。
- サンプルドキュメントのセクションにおいて、「Surface Book 3 (web)」を新たに追加しました。

この更新により、カスタム質問応答の利用者は最新のガイドラインやリソースに基づいて、効果的にドキュメントをフォーマットし、質の高い結果を得ることができるようになります。変更された内容は、利用者がよりスムーズにプロジェクトを進めるための情報を反映しています。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -40,29 +40,19 @@ items:
       href: personally-identifiable-information/quickstart.md
     - name: Language support
       href: personally-identifiable-information/language-support.md
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
+
+    - name: Text PII
       items:
-      - name: Redact PII from text
-        href: personally-identifiable-information/how-to/redact-text-pii.md
-      - name: Redact PII from conversations
-        href: personally-identifiable-information/how-to/redact-conversation-pii.md
-      - name: Redact PII from native documents
-        href: personally-identifiable-information/how-to/redact-document-pii.md
-      - name:  Adapt PII to your domain
-        href: personally-identifiable-information/how-to/adapt-to-domain-pii.md
-      - name: Use Docker containers
+      - name: Overview
+        href: personally-identifiable-information/text-pii-overview.md
+      - name: How-to guides
         items:
+        - name: Detect and redact PII in text
+          href: personally-identifiable-information/how-to/redact-text-pii.md
+        - name: Adapt PII to your domain
+          href: personally-identifiable-information/how-to/adapt-to-domain-pii.md
+        - name: Use Docker containers
+          items:
           - name: Install and run containers
             href: personally-identifiable-information/how-to/use-containers.md
           - name: Configure containers
@@ -73,21 +63,53 @@ items:
             href: ../containers/disconnected-containers.md
           - name: Azure AI containers overview
             href: ../cognitive-services-container-support.md
-    - name: Recognized entity categories
-      items:
-      - name: PII in text
+      - name: Recognized entity categories
         items:
         - name: Extended format
           href: personally-identifiable-information/concepts/entity-categories.md
         - name: List format
           href: personally-identifiable-information/concepts/entity-categories-list.md
-      - name: PII in conversations
+
+    - name: Conversation PII
+      items:
+      - name: Overview
+        href: personally-identifiable-information/conversation-pii-overview.md
+      - name: How-to guides
+        items:
+        - name: Detect and redact PII in conversations
+          href: personally-identifiable-information/how-to/redact-conversation-pii.md
+      - name: Recognized entity categories
         items:
         - name: Extended format
           href: personally-identifiable-information/concepts/conversations-entity-categories.md
         - name: List format
           href: personally-identifiable-information/concepts/conversations-entities-list.md
 
+    - name: Document-based PII
+      items:
+      - name: Overview
+        href: personally-identifiable-information/document-based-pii-overview.md
+      - name: How-to guides
+        items:
+        - name: Detect and redact PII in native documents
+          href: personally-identifiable-information/how-to/redact-document-pii.md
+        - name: Create SAS tokens for storage containers
+          href: native-document-support/shared-access-signatures.md
+        - name: Create a managed identity for storage containers
+          href: native-document-support/managed-identities.md
+
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
+
   - name: Language detection
     items:
     - name: Overview
@@ -807,14 +829,6 @@ items:
     href: tutorials/use-kubernetes-service.md
   - name: Use language in Power Automate flows
     href: tutorials/power-automate.md
-  - name: Native document support
-    items:
-    - name: Native documents for language processing
-      href: native-document-support/overview.md
-    - name: Create SAS tokens for storage containers
-      href: native-document-support/shared-access-signatures.md
-    - name: Create a managed identity for storage containers
-      href: native-document-support/managed-identities.md
   - name: Scenario deep-dives
     items:
       - name: Call Center
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCの構成変更と新しいトピックの追加"
}
```

### Explanation
この変更は、Azure Languageサービスの「toc.yml」ファイルに対する更新を反映しています。主な変更点は、トピックの構成が大幅に変更され、新しいセクションが追加されていることです。

具体的な変更内容は以下の通りです：
- 「責任あるAIの使用」セクションが更新され、関連情報が明確に整理されました。その中に透明性に関する注記や、データ、プライバシーとセキュリティに関するガイドラインが含まれています。
- 新しいセクション「Text PII」が追加され、テキスト内の個人を特定できる情報（PII）に関する概要や、PIIを検出し、赤外線するための手法が具体的に示されています。
- 「Conversation PII」セクションが新たに導入され、会話中のPIIを扱うための説明やガイドラインが提供されています。
- ドキュメントに基づくPIIに関するセクションも追加され、ネイティブドキュメントに関する手法や、ストレージコンテナのためのSASトークン作成に関する情報が体系的に組織されました。

全体として、この更新により、コンテンツがより体系的に整理され、利用者が特定のニーズに応じた情報を迅速に見つけられるようになります。この変更は、特に個人情報保護やAIの責任ある使用に関してのガイダンスを強化しています。


