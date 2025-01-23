---
date: '2025-01-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a1ea100...MicrosoftDocs:985f323
summary: このコード差分には、文書の小規模な更新と1つの破壊的変更が含まれています。新機能として、「生成AIアプリケーションの継続的監視に関する新しいガイド」が追加され、Azure
  AI StudioのRBACに関する主な情報が削除されました。この変更により、ドキュメントの読みやすさが向上し、ユーザーが生成AIアプリケーションのパフォーマンスをリアルタイムで監視する方法が提供されますが、RBAC関係の情報がなくなったことで、今後の利用には新たなガイドラインを待つ必要があります。全体として、文書の整備と情報更新が行われ、Azure
  AIサービスの効果的な利用が促進されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a1ea100...MicrosoftDocs:985f323){target="_blank"}

# ハイライト
このコード差分には、さまざまな文書の小規模な更新と、1つの破壊的変更が含まれています。新機能として、「生成AIアプリケーションの継続的監視に関する新しいガイド」が追加され、主要な破壊的変更として、Azure AI StudioのRBAC（ロールベースのアクセス制御）に関する情報が削除されました。

## 新機能
- 生成AIアプリケーションを継続的に監視するための新しいガイドが追加されました。これにより、アプリケーションのテレメトリデータを収集しリアルタイムで監視する方法が提供されます。

## 破壊的変更
- Azure AI StudioのRBACに関する主要な情報が削除され、従来の設定およびその理解に関して変更が必要です。

## その他の更新
- サポートファイル形式リスト、文書解析モデルの表現、文書レイアウトモデルの内容、サービス制限に関する情報が整備され、視覚的および内容的な改善が行われました。
- Blobストレージアカウントについて誤記の修正が行われ、ドキュメントの一貫性が向上しています。
- トピックの目次（TOC）が更新され、新しいセクションが追加されました。

# インサイト
この変更は、ドキュメントの読みやすさと利用者の利便性を向上させるために行われたもので、Azure AIプラットフォームを利用する際のガイダンスがより明確になっています。

特に、新しく追加された「生成AIアプリケーションの継続的監視」ガイドは、これまで独立したAIアプリケーション管理に苦労していたユーザーにとって重要なリソースです。このガイドは、アプリケーションのパフォーマンスをリアルタイムで追跡し、分析するために必要な詳細なステップを提供することで、ユーザーが高品質で安全なアプリケーションを維持するための手助けをします。

破壊的変更として、RBAC関連の情報が削除されたことにより、今後のAzure AIの使用において、ユーザーは新たなRBAC実装に対するガイドラインの提供を待たなければならなくなるでしょう。これは、セキュリティとアクセス管理に大きな影響を与える可能性があり、十分な考慮と計画が求められます。

ドキュメント全体では、表現の見直しや不整合の修正、情報の更新が多数行われ、全体としての理解が深まりました。この変更は、Azure AIサービスの利用者にとっての価値を高め、サービスの効果的な利用を支援することを目的としています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [input-requirements.md](#item-20011c) | minor update | ファイル形式のサポート情報のフォーマット修正 | modified | 10 | 10 | 20 | 
| [overview.md](#item-4e36ba) | minor update | 文書解析モデルに関する表現の修正 | modified | 9 | 15 | 24 | 
| [layout.md](#item-f7c4c8) | minor update | 文書レイアウトモデルに関する内容の大幅な更新 | modified | 158 | 112 | 270 | 
| [service-limits.md](#item-5ceae5) | minor update | サービス制限に関する最新情報の追加 | modified | 8 | 1 | 9 | 
| [studio-overview.md](#item-db8fa3) | minor update | ドキュメントインテリジェンススタジオの最新情報の反映 | modified | 9 | 9 | 18 | 
| [rbac-ai-studio.md](#item-c2a11a) | breaking change | Azure AI StudioのRBAC主要情報の削除 | modified | 0 | 88 | 88 | 
| [flow-develop.md](#item-d1ac3e) | minor update | Blobストレージアカウントの記述を修正 | modified | 1 | 1 | 2 | 
| [monitor-applications.md](#item-656e2b) | new feature | 生成AIアプリケーションの継続的監視に関する新しいガイドを追加 | added | 88 | 0 | 88 | 
| [online-evaluation.md](#item-d9591b) | minor update | オンライン評価に関する内容を更新 | modified | 50 | 94 | 144 | 
| [toc.yml](#item-2745cd) | minor update | TOCの更新: オンライン評価に関する項目を追加 | modified | 3 | 1 | 4 | 


# Modified Contents
## articles/ai-services/document-intelligence/includes/input-requirements.md{#item-20011c}

<details>
<summary>Diff</summary>
````diff
@@ -7,16 +7,16 @@ ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD041 -->
 
-* Supported file formats:
-
-    |Model | PDF |Image: </br>`JPEG/JPG`, `PNG`, `BMP`, `TIFF`, `HEIF` | Microsoft Office: </br> Word (`DOCX`), Excel (`XLSX`), PowerPoint (`PPTX`), HTML|
-    |--------|:----:|:-----:|:---------------:|
-    |Read            | ✔    | ✔    | ✔  |
-    |Layout          | ✔  | ✔ | ✔  |
-    |General&nbsp;Document| ✔  | ✔ |   |
-    |Prebuilt        |  ✔  | ✔ |   |
-    |Custom extraction |  ✔  | ✔ |   |
-    |Custom classification  |  ✔  | ✔ | ✔  |
+Supported file formats:
+
+|Model | PDF |Image: </br>`JPEG/JPG`, `PNG`, `BMP`, `TIFF`, `HEIF` | Microsoft Office: </br> Word (`DOCX`), Excel (`XLSX`), PowerPoint (`PPTX`), HTML|
+|--------|:----:|:-----:|:---------------:|
+|Read            | ✔    | ✔    | ✔  |
+|Layout          | ✔  | ✔ | ✔  |
+|General&nbsp;Document| ✔  | ✔ |   |
+|Prebuilt        |  ✔  | ✔ |   |
+|Custom extraction |  ✔  | ✔ |   |
+|Custom classification  |  ✔  | ✔ | ✔  |
 
 * For best results, provide one clear photo or high-quality scan per document.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイル形式のサポート情報のフォーマット修正"
}
```

### Explanation
この変更は、ドキュメントにおけるサポートされているファイル形式に関する情報のフォーマットを統一するためのもので、主にテーブルの見た目を改善しています。具体的には、元々のフォーマットから新しいフォーマットに変更され、テーブルの行がより一貫性を持つように整形されています。これにより、視覚的に読みやすくなり、ユーザーにとっての理解が容易になります。また、この変更では、全体として10行の追加と10行の削除が発生し、合計20行の変更が行われています。

## articles/ai-services/document-intelligence/overview.md{#item-4e36ba}

<details>
<summary>Diff</summary>
````diff
@@ -43,11 +43,11 @@ monikerRange: '<=doc-intel-4.0.0'
 
 Azure AI Document Intelligence is a cloud-based [Azure AI service](../../ai-services/index.yml) that enables you to build intelligent document processing solutions. Massive amounts of data, spanning a wide variety of data types, are stored in forms and documents. Document Intelligence enables you to effectively manage the velocity at which data is collected and processed and is key to improved operations, informed data-driven decisions, and enlightened innovation. </br></br>
 
-| ✔️ [**Document analysis models**](#general-extraction-models) | ✔️ [**Prebuilt models**](#prebuilt-models) | ✔️ [**Custom models**](#custom-model-overview) |
+| ✔️ [**Document analysis models**](#document-analysis-models) | ✔️ [**Prebuilt models**](#prebuilt-models) | ✔️ [**Custom models**](#custom-model-overview) |
 
-## General extraction models
+## Document analysis models
 
-General extraction models enable text extraction from forms and documents and return structured business-ready content ready for your organization's action, use, or development.
+Document analysis (general extraction) models enable text extraction from forms and documents and return structured business-ready content ready for your organization's action, use, or development.
 
 :::moniker range="doc-intel-4.0.0"
 
@@ -261,9 +261,6 @@ Document Intelligence supports optional features that can be enabled and disable
 
 ## Models and development options
 
-> [!NOTE]
->The following document understanding models and development options are supported by the Document Intelligence service v3.0.
-
 You can use Document Intelligence to automate document processing in applications and workflows, enhance data-driven strategies, and enrich document search capabilities. Use the links in the table to learn more about each model and browse development options.
 
 ### Read
@@ -275,7 +272,7 @@ You can use Document Intelligence to automate document processing in application
 |[**prebuilt-read**](prebuilt/read.md)|&#9679; Extract **text** from documents.</br>&#9679; [Data extraction](prebuilt/read.md#data-extraction)| &#9679; Digitizing any document. </br>&#9679; Compliance and auditing.</br>&#9679; Processing handwritten notes before translation.|&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/read)</br>&#9679; [**REST API**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api)</br>&#9679; [**C# SDK**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-csharp)</br>&#9679; [**Python SDK**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-python)</br>&#9679; [**Java SDK**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-java)</br>&#9679; [**JavaScript**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-javascript) |
 
 > [!div class="nextstepaction"]
-> [Return to model types](#general-extraction-models)
+> [Return to model types](#document-analysis-models)
 
 ### Layout
 
@@ -286,7 +283,7 @@ You can use Document Intelligence to automate document processing in application
 |[**prebuilt-layout**](prebuilt/layout.md) |&#9679; Extract **text and layout** information from documents.</br>&#9679; [Data extraction](prebuilt/layout.md#data-extraction) |&#9679; Document indexing and retrieval by structure.</br>&#9679; Financial and medical report analysis. |&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/layout)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)|
 
 > [!div class="nextstepaction"]
-> [Return to model types](#general-extraction-models)
+> [Return to model types](#document-analysis-models)
 
  :::moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
 
@@ -299,7 +296,7 @@ You can use Document Intelligence to automate document processing in application
 |[**prebuilt-document**](prebuilt/general-document.md)|&#9679; Extract **text,layout, and key-value pairs** from documents.</br>&#9679; [Data and field extraction](prebuilt/general-document.md#data-extraction)|&#9679; Key-value pair extraction.</br>&#9679; Form processing.</br>&#9679; Survey data collection and analysis.|&#9679; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/document)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|
 
 > [!div class="nextstepaction"]
-> [Return to model types](#general-extraction-models)
+> [Return to model types](#document-analysis-models)
 
 :::moniker-end
 
@@ -616,12 +613,9 @@ Azure AI Document Intelligence is a cloud-based [Azure AI service](../../ai-serv
 
  >[!TIP]
  >
- > * For an enhanced experience and advanced model quality, try the [Document Intelligence v3.0 Studio](https://formrecognizer.appliedai.azure.com/studio).
- > * The v3.0 Studio supports any model trained with v2.1 labeled data.
- > * You can refer to the API migration guide for detailed information about migrating from v2.1 to v3.0.
-
-> [!NOTE]
-> The following models  and development options are supported by the Document Intelligence service v2.1.
+ > * For an enhanced experience and advanced model quality, try the [Document Intelligence v3.0 Studio](https://formrecognizer.appliedai.azure.com/studio):
+ >   * The v3.0 Studio supports any model trained with v2.1 labeled data.
+ >   * You can refer to the API migration guide for detailed information about migrating from v2.1 to v3.0.
 
 Use the links in the table to learn more about each model and browse the API references:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書解析モデルに関する表現の修正"
}
```

### Explanation
この変更では、Azure AI Document Intelligenceに関するドキュメントの内容が一部修正され、用語の統一や表現の見直しが行われました。具体的には、"general extraction models"というセクション見出しが"document analysis models"に改名され、より適切な名称が使用されています。また、特定の説明文がより明確に整えられており、リンク先の見出しも修正されています。全体として、9行の追加と15行の削除があり、合計で24行の変更が発生しています。これにより、情報が一貫性を持つようになり、読者にとっての理解が深まることを目的としています。

## articles/ai-services/document-intelligence/prebuilt/layout.md{#item-f7c4c8}

<details>
<summary>Diff</summary>
````diff
@@ -6,14 +6,14 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 11/19/2024
+ms.date: 01/16/2025
 ms.author: lajanuar
 ---
 
 <!-- markdownlint-disable MD051 -->
 <!-- markdownlint-disable MD024 -->
 
-# Document Intelligence layout model
+# What is Document Intelligence layout model?
 
 <!---------------------- v4.0 content ---------------------->
 
@@ -23,7 +23,7 @@ ms.author: lajanuar
 
 Document Intelligence layout model is an advanced machine-learning based document analysis API available in the Document Intelligence cloud. It enables you to take documents in various formats and return structured data representations of the documents. It combines an enhanced version of our powerful [Optical Character Recognition (OCR)](../../../ai-services/computer-vision/overview-ocr.md) capabilities with deep learning models to extract text, tables, selection marks, and document structure.
 
-## Document layout analysis (v4)
+## Document structure layout analysis
 
 Document structure layout analysis is the process of analyzing a document to extract regions of interest and their inter-relationships. The goal is to extract text and structural elements from the page to build better semantic understanding models. There are two types of roles in a document layout:
 
@@ -32,20 +32,49 @@ Document structure layout analysis is the process of analyzing a document to ext
 
 The following illustration shows the typical components in an image of a sample page.
 
-:::image type="content" source="../media/document-layout-example-new.png" alt-text="Illustration of document layout example."::: 
-
-## Development options (v4)
+:::image type="content" source="../media/document-layout-example-new.png" alt-text="Illustration of document layout example.":::
 
+## Development options
 
 Document Intelligence v4.0: **2024-11-30** (GA) supports the following tools, applications, and libraries:
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
 |**Layout model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-layout**|
 
-## Input requirements (v4)
+## Supported languages
+
+See [Language Support—document analysis models](../language-support/ocr.md) for a complete list of supported languages.
 
-[!INCLUDE [input requirements](./../includes/input-requirements.md)]
+## Supported file types
+
+Document Intelligence v4.0: **2024-11-30** (GA) layout model supports the following file formats:
+
+|Model | PDF |Image: </br>`JPEG/JPG`, `PNG`, `BMP`, `TIFF`, `HEIF` | Microsoft Office: </br> Word (`DOCX`), Excel (`XLSX`), PowerPoint (`PPTX`), HTML|
+|--------|:----:|:-----:|:---------------:|
+|Layout          | ✔  | ✔ | ✔  |
+
+## Input requirements
+
+* For best results, provide one clear photo or high-quality scan per document.
+
+* For PDF and TIFF, up to 2,000 pages can be processed (with a free tier subscription, only the first two pages are processed).
+
+* If your PDFs are password-locked, you must remove the lock before submission.
+
+* The file size for analyzing documents is 500 MB for paid (S0) tier and `4` MB for free (F0) tier.
+
+* Image dimensions must be between 50 pixels x 50 pixels and 10,000 pixels x 10,000 pixels.
+
+* The minimum height of the text to be extracted is 12 pixels for a 1024 x 768 pixel image. This dimension corresponds to about `8` point text at 150 dots per inch (DPI).
+
+* For custom model training, the maximum number of pages for training data is 500 for the custom template model and 50,000 for the custom neural model.
+
+  * For custom extraction model training, the total size of training data is 50 MB for template model and `1` GB for the neural model.
+
+  * For custom classification model training, the total size of training data is `1` GB  with a maximum of 10,000 pages. For `2024-11-30` (GA), the total size of training data is `2` GB with a maximum of 10,000 pages.
+
+For more information on model usage, quotas, and service limits, *see* [service limits](../service-limits.md).
 
 ### Get started with Layout model
 
@@ -55,46 +84,45 @@ See how data, including text, tables, table headers, selection marks, and struct
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
-    :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal."::: 
+    :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
-> [!NOTE]
-> Document Intelligence Studio is available with v3.0 APIs and later versions.
+After you retrieve you key and endpoint, you can use the following development options to build and deploy your Document Intelligence applications:
 
-***Sample document processed with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/layout)***
+### [REST API](#tab/rest)
 
-:::image type="content" source="../media/studio/form-recognizer-studio-layout-newspaper.png" alt-text="Screenshot of `Layout` processing a newspaper page in Document Intelligence Studio."::: 
+* [Document Intelligence REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true&tabs=HTTP&)
+* [How to guide](../how-to-guides/use-sdk-rest-api.md#use-document-intelligence-models)
 
-1. On the [Document Intelligence Studio home page](https://documentintelligence.ai.azure.com/studio), select **Layout**.
+# [Client libraries](#tab/sdks)
 
-1. You can analyze the sample document or upload your own files.
+* [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)
+* [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)
+* [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)
+* [**JavaScript**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)
 
-1. Select the **Run analysis** button and, if necessary, configure the **Analyze options**:
+### [Document Intelligence Studio](#tab/studio)
 
-    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio."::: 
+* [Studio](https://documentintelligence.ai.azure.com/studio)
+* [How-to guide](../studio-overview.md#authentication-in-studio)
 
-     > [!div class="nextstepaction"]
-     > [Try Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/layout).
-     >
-
-## Supported languages
-
-*See* our [Language Support—document analysis models](../language-support/ocr.md) page for a complete list of supported languages.
+---
 
-## Data extraction (v4)
+## Data extraction
 
-The layout model extracts text, selection marks, tables, paragraphs, and paragraph types (`roles`) from your documents.
+The layout model extracts structural elements from your documents. To follow are descriptions of these structural elements with guidance on how to extract them from your document input:
 
-> [!NOTE]
-> Document Intelligence v4.0 (2024-11-30 (GA)) and later support Microsoft office (DOCX, XLSX, PPTX) and HTML files. The following features are not supported:
->
-> * There are no angle, width/height and unit with each page object.
-> * For each object detected, there is no bounding polygon or bounding region.
-> * Page range (`pages`) is not supported as a parameter.
-> * No `lines` object.
+* [**Pages**](#pages)
+* [**Paragraphs**](#paragraphs)
+* [**Text, lines, and words**](#text-lines-and-words)
+* [**Selection marks**](#selection-marks)
+* [**Tables**](#tables)
+* [**Output response to markdown**](#output-response-to-markdown-format)
+* [**Figures**](#figures)
+* [**Sections**](#sections)
 
 ### Pages
 
-The pages collection is a list of pages within the document. Each page is represented sequentially within the document and ../includes the orientation angle indicating if the page is rotated and the width and height (dimensions in pixels). The page units in the model output are computed as shown:
+The pages collection is a list of pages within the document. Each page is represented sequentially within the document and includes the orientation angle indicating if the page is rotated and the width and height (dimensions in pixels). The page units in the model output are computed as shown:
 
 | **File format**   | **Computed page unit**   | **Total pages**  |
 | --- | --- | --- |
@@ -117,7 +145,7 @@ print(f"Page has width: {page.width} and height: {page.height}, measured with un
 ```
 
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py) 
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py)
 
 #### [Output](#tab/output)
 
@@ -138,7 +166,7 @@ print(f"Page has width: {page.width} and height: {page.height}, measured with un
 
 ---
 
-### Extract selected pages from documents
+#### Extract selected pages
 
 For large multi-page documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction.
 
@@ -157,7 +185,7 @@ The Layout model extracts all identified blocks of text in the `paragraphs` coll
 ]
 ```
 
-### Paragraph roles
+#### Paragraph roles
 
 The new machine-learning based page object detection extracts logical roles like titles, section headings, page headers, page footers, and more. The Document Intelligence Layout model assigns certain text blocks in the `paragraphs` collection with their specialized role or type predicted by the model. It's best to use paragraph roles with unstructured documents to help understand the layout of the extracted content for a richer semantic analysis. The following paragraph roles are supported:
 
@@ -215,7 +243,7 @@ if page.lines:
 ```
 
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py) 
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py)
 
 #### [Output](#tab/output)
 
@@ -239,7 +267,7 @@ if page.lines:
 
 ---
 
-### Handwritten style for text lines
+#### Handwritten style for text lines
 
 The response ../includes classifying whether each text line is of handwriting style or not, along with a confidence score. For more information. See [Handwritten language support](../language-support/ocr.md). The following example shows an example JSON snippet.
 
@@ -277,7 +305,7 @@ if page.selection_marks:
 ```
 
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py) 
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py)
 
 #### [Output](#tab/output)
 
@@ -337,7 +365,7 @@ if result.tables:
 ```
 
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py) 
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py)
 
 #### [Output](#tab/output)
 
@@ -366,7 +394,7 @@ if result.tables:
 
 ---
 
-### Output to markdown format
+### Output response to markdown format
 
 The Layout API can output the extracted text in markdown format. Use the `outputContentFormat=markdown` to specify the output format in markdown. The markdown content is output as part of the `content` section.
 
@@ -386,12 +414,12 @@ poller = document_intelligence_client.begin_analyze_document(
 ```
 
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_analyze_documents_output_in_markdown.py) 
+> [View samples on GitHub.](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_analyze_documents_output_in_markdown.py)
 
 #### [Output](#tab/output)
 
 ```Markdown
-PageHeader="This is the header of the document." 
+PageHeader="This is the header of the document."
 
 This is title
 ===
@@ -413,7 +441,7 @@ Figure 1: Here is a figure with text
 </figcaption>
 
 ![](figures/0)
-FigureContent="500 450 400 400 350 250 200 200 200- Feb" 
+FigureContent="500 450 400 400 350 250 200 200 200- Feb"
 </figure>
 
 # 3\. Others
@@ -430,8 +458,8 @@ coherent
 Incomprehensible
 Turn documents into usable data and shift your focus to acting on information rather than compiling it. Start with prebuilt models or create custom models tailored to your documents both on premises and in the cloud with the Al Document Intelligence studio or SDK.
 Learn how to accelerate your business processes by automating text extraction with Al Document Intelligence. This webinar features hands-on demos for key use cases such as document processing, knowledge mining, and industry-specific Al model customization.
-PageFooter="This is the footer of the document." 
-PageFooter="1 | Page" 
+PageFooter="This is the footer of the document."
+PageFooter="1 | Page"
 ```
 
 ---
@@ -458,7 +486,7 @@ if result.figures:
 ```
 
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py) 
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py)
 
 #### [Output](#tab/output)
 
@@ -486,13 +514,13 @@ if result.figures:
 }
 ```
 
-:::image type="content" source="../media/document-layout-example-figures.png" alt-text="Screenshot of examples of document figures."::: 
+:::image type="content" source="../media/document-layout-example-figures.png" alt-text="Screenshot of examples of document figures.":::
 
 ---
 
 ### Sections
 
-Hierarchical document structure analysis is pivotal in organizing, comprehending, and processing extensive documents. This approach is vital for semantically segmenting long documents to boost comprehension, facilitate navigation, and improve information retrieval. The advent of [Retrieval Augmented Generation (RAG)](../concept/retrieval-augmented-generation.md) in document generative AI underscores the significance of hierarchical document structure analysis. The Layout model supports sections and subsections in the output, which identifies the relationship of sections and object within each section. The hierarchical structure is maintained in `elements` of each section. You can use [output to markdown format](#output-to-markdown-format) to easily get the sections and subsections in markdown.
+Hierarchical document structure analysis is pivotal in organizing, comprehending, and processing extensive documents. This approach is vital for semantically segmenting long documents to boost comprehension, facilitate navigation, and improve information retrieval. The advent of [Retrieval Augmented Generation (RAG)](../concept/retrieval-augmented-generation.md) in document generative AI underscores the significance of hierarchical document structure analysis. The Layout model supports sections and subsections in the output, which identifies the relationship of sections and object within each section. The hierarchical structure is maintained in `elements` of each section. You can use [output response to markdown format](#output-response-to-markdown-format) to easily get the sections and subsections in markdown.
 
 #### [Sample code](#tab/sample-code)
 
@@ -507,7 +535,7 @@ poller = document_intelligence_client.begin_analyze_document(
 ```
 
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_analyze_documents_output_in_markdown.py) 
+> [View samples on GitHub.](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_analyze_documents_output_in_markdown.py)
 
 #### [Output](#tab/output)
 
@@ -527,7 +555,7 @@ poller = document_intelligence_client.begin_analyze_document(
 }
 ```
 
-:::image type="content" source="../media/document-layout-example-section.png" alt-text="Screenshot of examples of document sections."::: 
+:::image type="content" source="../media/document-layout-example-section.png" alt-text="Screenshot of examples of document sections.":::
 
 ---
 
@@ -547,6 +575,8 @@ poller = document_intelligence_client.begin_analyze_document(
 [!INCLUDE [applies to v2.1](../includes/applies-to-v21.md)]
 :::moniker-end
 
+:::moniker range="<=doc-intel-3.1.0"
+
 Document Intelligence layout model is an advanced machine-learning based document analysis API available in the Document Intelligence cloud. It enables you to take documents in various formats and return structured data representations of the documents. It combines an enhanced version of our powerful [Optical Character Recognition (OCR)](../../../ai-services/computer-vision/overview-ocr.md) capabilities with deep learning models to extract text, tables, selection marks, and document structure.
 
 ## Document layout analysis
@@ -558,27 +588,11 @@ Document structure layout analysis is the process of analyzing a document to ext
 
 The following illustration shows the typical components in an image of a sample page.
 
-:::image type="content" source="../media/document-layout-example-new.png" alt-text="Illustration of document layout example."::: 
-
-## Development options
-
-:::moniker range="doc-intel-3.1.0"
-
-Document Intelligence v3.1 supports the following tools, applications, and libraries:
-
-| Feature | Resources | Model ID |
-|----------|-------------|-----------|
-|**Layout model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-layout**|
-
-:::moniker-end
-
-:::moniker range="doc-intel-3.0.0"
+:::image type="content" source="../media/document-layout-example-new.png" alt-text="Illustration of document layout example.":::
 
-Document Intelligence v3.0 supports the following tools, applications, and libraries:
+## Supported languages and locales
 
-| Feature | Resources | Model ID |
-|----------|-------------|-----------|
-|**Layout model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-layout**|
+*See* our [Language Support—document analysis models](../language-support/ocr.md) page for a complete list of supported languages.
 
 :::moniker-end
 
@@ -592,56 +606,73 @@ Document Intelligence v2.1 supports the following tools, applications, and libra
 
 :::moniker-end
 
-## Input requirements
-
 :::moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
 
+## Input guidance
+
 [!INCLUDE [input requirements](./../includes/input-requirements.md)]
 
 :::moniker-end
 
 :::moniker range="doc-intel-2.1.0"
 
+## Input guide
+
 * Supported file formats: JPEG, PNG, PDF, and TIFF.
 * Supported number of pages: For PDF and TIFF, up to 2,000 pages are processed. For free tier subscribers, only the first two pages are processed.
 * Supported file size: the file size must be less than 50 MB and dimensions at least 50 x 50 pixels and at most 10,000 x 10,000 pixels.
 
 :::moniker-end
 
-### Get started with Layout model
+:::moniker range="<=doc-intel-3.1.0"
+
+### Get started
 
 See how data, including text, tables, table headers, selection marks, and structure information is extracted from documents using  Document Intelligence. You need the following resources:
 
 * An Azure subscription—you can [create one for free](https://azure.microsoft.com/free/cognitive-services/).
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
-:::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal."::: 
+:::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+
+:::moniker-end
 
 :::moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
 
+After you retrieve you key and endpoint, you can use the following development options to build and deploy your Document Intelligence applications:
+
 > [!NOTE]
 > Document Intelligence Studio is available with v3.0 APIs and later versions.
 
-***Sample document processed with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/layout)***
+### [REST API](#tab/rest)
 
-:::image type="content" source="../media/studio/form-recognizer-studio-layout-newspaper.png" alt-text="Screenshot of `Layout` processing a newspaper page in Document Intelligence Studio."::: 
 
-1. On the [Document Intelligence Studio home page](https://documentintelligence.ai.azure.com/studio), select **Layout**.
+* [2023-07-31 GA (v3.1)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)
+* [2022-08-31 GA (v3.0)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
 
-1. You can analyze the sample document or upload your own files.
+# [Client libraries](#tab/sdks)
 
-1. Select the **Run analysis** button and, if necessary, configure the **Analyze options**:
+* [**C# SDK**](/dotnet/api/overview/azure/ai.documentintelligence-readme?view=azure-dotnet-preview&preserve-view=true)
+* [**Java SDK**](/java/api/overview/azure/ai-documentintelligence-readme?view=azure-java-preview&preserve-view=true)
+* [**JavaScript**](/javascript/api/overview/azure/ai-document-intelligence-rest-readme?view=azure-node-preview&preserve-view=true)
+* [**Python SDK**](/python/api/overview/azure/ai-documentintelligence-readme?view=azure-python-preview&preserve-view=true)
 
-    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+### [Document Intelligence Studio](#tab/studio)
 
-   > [!div class="nextstepaction"]
-   > [Try Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/layout). 
+* [Studio](https://documentintelligence.ai.azure.com/studio)
+* [How-to guide](../studio-overview.md#authentication-in-studio)
+
+---
 
 :::moniker-end
 
 :::moniker range="doc-intel-2.1.0"
 
+## REST API
+
+* [Document Intelligence v2.1 (Form Recognizer)](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)
+
 ## Document Intelligence Sample Labeling tool
 
 1. Navigate to the [Document Intelligence sample tool](https://fott-2-1.azurewebsites.net/).
@@ -670,10 +701,6 @@ See how data, including text, tables, table headers, selection marks, and struct
 
 :::moniker-end
 
-## Supported languages and locales
-
-*See* our [Language Support—document analysis models](../language-support/ocr.md) page for a complete list of supported languages.
-
 :::moniker range="doc-intel-2.1.0"
 
 Document Intelligence v2.1 supports the following tools, applications, and libraries:
@@ -684,21 +711,40 @@ Document Intelligence v2.1 supports the following tools, applications, and libra
 
 :::moniker-end
 
-:::moniker range="<=doc-intel-3.1.0"
+:::moniker range="doc-intel-3.0.0 || doc-intel-3.1.0"
 
-## Data extraction
+## Extract data
 
-The layout model extracts text, selection marks, tables, paragraphs, and paragraph types (`roles`) from your documents.
+The layout model extracts structural elements from your documents. To follow are descriptions of these structural elements with guidance on how to extract them from your document input:
 
-> [!NOTE]
-> Document Intelligence v4.0 *2024-11-30 (GA)* supports Microsoft office (DOCX, XLSX, PPTX) and HTML files. The following features are not supported:
->
-> * There are no angle, width/height and unit with each page object.
-> * For each object detected, there is no bounding polygon or bounding region.
-> * Page range (`pages`) is not supported as a parameter.
-> * No `lines` object.
+* [**Page**](#page)
+* [**Paragraph**](#paragraph)
+* [**Text, line, and word**](#text-lines-and-words)
+* [**Selection mark**](#selection-marks)
+* [**Table**](#tables)
+* [**Annotations**](#annotations)
 
-### Pages
+:::moniker-end
+
+:::moniker range="doc-intel-2.1.0"
+
+## Extract data
+
+The layout model extracts structural elements from your documents. To follow are descriptions of these structural elements with guidance on how to extract them from your document input:
+
+* [**Page**](#page)
+* [**Paragraph**](#paragraph)
+* [**Text, line, and word**](#text-lines-and-words)
+* [**Selection mark**](#selection-marks)
+* [**Table**](#tables)
+* [**Natural reading order**](#natural-reading-order-output-latin-only)
+* [**Select page number or range**](#select-page-number-or-range-for-text-extraction)
+
+:::moniker-end
+
+:::moniker range="<=doc-intel-3.1.0"
+
+### Page
 
 The pages collection is a list of pages within the document. Each page is represented sequentially within the document and ../includes the orientation angle indicating if the page is rotated and the width and height (dimensions in pixels). The page units in the model output are computed as shown:
 
@@ -748,7 +794,7 @@ for page in result.pages:
 ```
 
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py) 
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py)
 
 #### [Output](#tab/output)
 
@@ -776,7 +822,7 @@ for page in result.pages:
 
 For large multi-page documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction.
 
-### Paragraphs
+### Paragraph
 
 The Layout model extracts all identified blocks of text in the `paragraphs` collection as a top level object under `analyzeResults`. Each entry in this collection represents a text block and ../includes the extracted text as`content`and the bounding `polygon` coordinates. The `span` information points to the text fragment within the top level `content` property that contains the full text from the document.
 
@@ -791,7 +837,7 @@ The Layout model extracts all identified blocks of text in the `paragraphs` coll
 ]
 ```
 
-### Paragraph roles
+#### Paragraph role
 
 The new machine-learning based page object detection extracts logical roles like titles, section headings, page headers, page footers, and more. The Document Intelligence Layout model assigns certain text blocks in the `paragraphs` collection with their specialized role or type predicted by the model. It's best to use paragraph roles with unstructured documents to help understand the layout of the extracted content for a richer semantic analysis. The following paragraph roles are supported:
 
@@ -824,7 +870,7 @@ The new machine-learning based page object detection extracts logical roles like
 
 ```
 
-### Text, lines, and words
+### Text, line, and word
 
 The document layout model in Document Intelligence extracts print and handwritten style text as `lines` and `words`. The `styles` collection ../includes any handwritten style for lines if detected along with the spans pointing to the associated text. This feature applies to [supported handwritten languages](../language-support/prebuilt.md).
 
@@ -876,7 +922,7 @@ for line_idx, line in enumerate(page.lines):
 ```
 
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py) 
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py)
 
 #### [Output](#tab/output)
 
@@ -903,7 +949,7 @@ for line_idx, line in enumerate(page.lines):
 
 :::moniker range="<=doc-intel-3.1.0"
 
-### Handwritten style for text lines
+### Handwritten style
 
 The response ../includes classifying whether each text line is of handwriting style or not, along with a confidence score. For more information. See [Handwritten language support](../language-support/ocr.md). The following example shows an example JSON snippet.
 
@@ -923,7 +969,7 @@ The response ../includes classifying whether each text line is of handwriting st
 
 If you enable the [font/style addon capability](../concept-add-on-capabilities.md#font-property-extraction), you also get the font/style result as part of the `styles` object.
 
-### Selection marks
+### Selection mark
 
 The Layout model also extracts selection marks from documents. Extracted selection marks appear within the `pages` collection for each page. They include the bounding `polygon`, `confidence`, and selection `state` (`selected/unselected`). The text representation (that is, `:selected:` and `:unselected`) is also included as the starting index (`offset`) and `length` that references the top level `content` property that contains the full text from the document.
 
@@ -964,7 +1010,7 @@ for selection_mark in page.selection_marks:
 ```
 
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py) 
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py)
 
 #### [Output](#tab/output)
 
@@ -989,7 +1035,7 @@ for selection_mark in page.selection_marks:
 
 :::moniker range="<=doc-intel-3.1.0"
 
-### Tables
+### Table
 
 Extracting tables is a key requirement for processing documents containing large volumes of data typically formatted as tables. The Layout model extracts tables in the `pageResults` section of the JSON output. Extracted table information ../includes the number of columns and rows, row span, and column span. Each cell with its bounding polygon is output along with information whether the area is recognized as a `columnHeader` or not. The model supports extracting tables that are rotated. Each table cell contains the row and column index and bounding polygon coordinates. For the cell text, the model outputs the `span` information containing the starting index (`offset`). The model also outputs the `length` within the top-level content that contains the full text from the document.
 
@@ -1064,7 +1110,7 @@ for table_idx, table in enumerate(result.tables):
 ```
 
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py) 
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py)
 
 #### [Output](#tab/output)
 
@@ -1096,7 +1142,7 @@ for table_idx, table in enumerate(result.tables):
 
 :::moniker range="doc-intel-3.1.0"
 
-### Annotations (available only in ``2023-02-28-preview`` API.)
+### Annotations
 
 The Layout model extracts annotations in documents, such as checks and crosses. The response ../includes the kind of annotation, along with a confidence score and bounding polygon.
 
@@ -1126,7 +1172,7 @@ You can specify the order in which the text lines are output with the `readingOr
 
 :::image type="content" source="../media/layout-reading-order-example.png" alt-text="Screenshot of `layout` model reading order processing." lightbox="../../../ai-services/Computer-vision/Images/ocr-reading-order-example.png":::
 
-### Select page numbers or ranges for text extraction
+### Select page number or range for text extraction
 
 For large multi-page documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction. The following example shows a document with 10 pages, with text extracted for both cases - all pages (1-10) and selected pages (3-6).
 
@@ -1172,7 +1218,7 @@ Layout API extracts tables in the `pageResults` section of the JSON output. Docu
 
 ![Tables example](../media/layout-table-header-demo.gif)
 
-### Selection marks
+### Selection marks (documents)
 
 Layout API also extracts selection marks from documents. Extracted selection marks include the bounding box, confidence, and state (selected/unselected). Selection mark information is extracted in the `readResults` section of the JSON output.
 
@@ -1210,4 +1256,4 @@ Layout API also extracts selection marks from documents. Extracted selection mar
 
 * Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
-:::moniker-end
+:::moniker-end
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書レイアウトモデルに関する内容の大幅な更新"
}
```

### Explanation
この変更では、Azure AI Document Intelligenceにおける文書レイアウトモデルに関するドキュメントが大幅に更新されています。具体的には、文書レイアウトモデルの説明が改訂され、より明確かつ詳細な情報が追加されています。セクションの名称や構成が変えられ、新たに「サポートされる言語」や「入力要件」などの項目が導入されています。また、サポートされるファイル形式についてのテーブルが整備され、テクニカルな入力要件が明記されています。この変更によって、利用者にとってドキュメントがより理解しやすく、アクセスしやすくなっています。

合計で158行の追加、112行の削除、および270行の変更が行われ、このドキュメントの内容が大きく改善されています。これにより、最新の機能や使用方法が適切に反映され、利用者が必要とする情報へ迅速にアクセスできるようになっています。

## articles/ai-services/document-intelligence/service-limits.md{#item-5ceae5}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 01/13/2025
+ms.date: 01/15/2025
 ms.author: lajanuar
 monikerRange: '<=doc-intel-4.0.0'
 ---
@@ -36,6 +36,13 @@ This article contains both a quick reference and detailed description of Azure A
 
 ✔️ = supported
 ✖️ = Not supported
+
+For Document Intelligence v4.0 `2024-11-30` (GA) supports page and line features with the following restrictions:
+
+* Angle, width/height, and unit aren't supported.
+* For each object detected, bounding polygon or bounding regions aren't supported.
+* Page range (`pages`) isn't supported as a parameter.
+* The `lines` object isn't supported.
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス制限に関する最新情報の追加"
}
```

### Explanation
この変更では、Azure AI Document Intelligenceにおけるサービス制限に関するドキュメントに新たな情報が追加されました。具体的には、文書インテリジェンスのバージョン4.0に関するページと行の機能の制限が明記されています。新たに追加された情報には、サポートされていない機能として以下が含まれています：

- 角度、幅、高さ、および単位がサポートされていないこと。
- 検出された各オブジェクトについて、バウンディングポリゴンやバウンディング領域がサポートされていないこと。
- ページ範囲（`pages`）がパラメーターとしてサポートされていないこと。
- `lines`オブジェクトがサポートされていないこと。

これらの変更は、利用者がサービスの機能制限を理解するのに役立ち、特にアップデートされたバージョンの使用を検討する際の参考情報となります。合計で8行が追加され、1行が削除され、9行の変更が記録されています。

## articles/ai-services/document-intelligence/studio-overview.md{#item-db8fa3}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: overview
-ms.date: 11/19/2024
+ms.date: 01/15/2025
 ms.author: lajanuar
 monikerRange: '>=doc-intel-3.0.0'
 ---
@@ -31,7 +31,7 @@ Currently, we're undergoing the migration of features from the [Document Intelli
 
 ## Choosing the correct studio experience
 
-There are currently two studios, the [Azure AI Foundry portal](https://ai.azure.com/explore/aiservices/vision) and the [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio) for building and validating  Document Intelligence models. As the experiences migrate to the new Azure AI Foundry portal, some experiences are available in both studios, while other experiences/models are only available in only one of the studios. To follow are a few guidelines for choosing the Studio experience for your needs. All of our [prebuilt models](overview.md#prebuilt-models) and [general extraction models](overview.md#general-extraction-models) are available on both studios.
+There are currently two studios, the [Azure AI Foundry portal](https://ai.azure.com/explore/aiservices/vision) and the [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio) for building and validating  Document Intelligence models. As the experiences migrate to the new Azure AI Foundry portal, some experiences are available in both studios, while other experiences/models are only available in only one of the studios. To follow are a few guidelines for choosing the Studio experience for your needs. All of our [prebuilt models](overview.md#prebuilt-models) and [general extraction models](overview.md#document-analysis-models) are available on both studios.
 
 ### When to use [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio)
 
@@ -49,9 +49,9 @@ Select the studio experience from the following tabs to learn more about each st
 
 > [!IMPORTANT]
 >
-> * There are separate URLs for Document Intelligence Studio sovereign cloud regions.
-> * Azure for US Government: [Document Intelligence Studio (Azure Fairfax cloud)](https://formrecognizer.appliedai.azure.us/studio)
-> * Microsoft Azure operated by 21Vianet: [Document Intelligence Studio (Azure in China)](https://formrecognizer.appliedai.azure.cn/studio)
+> * Document Intelligence Studio has distinct URLs for sovereign cloud regions.
+> * Azure for US Government: [Document Intelligence Studio (`Azure Fairfax`)](https://formrecognizer.appliedai.azure.us/studio)
+> * Microsoft Azure operated by 21Vianet: [Document Intelligence Studio (`Azure China`)](https://formrecognizer.appliedai.azure.cn/studio)
 
 The studio supports Document Intelligence v3.0 and later API versions for model analysis and custom model training. Previously trained v2.1 models with labeled data are supported, but not v2.1 model training. Refer to the [REST API migration guide](v3-1-migration-guide.md) for detailed information about migrating from v2.1 to v3.0.
 
@@ -66,9 +66,9 @@ To use Document Intelligence Studio, you need to acquire the following assets fr
 * **An Azure AI services or Document Intelligence resource**. Once you have your Azure subscription, create a [single-service](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) or [multi-service](https://portal.azure.com/#create/Microsoft.CognitiveServicesAIServices) resource, in the Azure portal to get your key and endpoint. Use the free pricing tier (`F0`) to try the service, and upgrade later to a paid tier for production.
 
 > [!TIP]
-> Create an Azure AI services resource if you plan to access multiple Azure AI services under a single endpoint/key. For Document Intelligence access only, create a Document Intelligence resource. Please note that you'll need a single-service resource if you intend to use [Microsoft Entra authentication](/azure/active-directory/authentication/overview-authentication).
+> Create an Azure AI services resource if you plan to access multiple Azure AI services under a single endpoint/key. For Document Intelligence access only, create a Document Intelligence resource. You need a single-service resource if you intend to use [Microsoft Entra authentication](/azure/active-directory/authentication/overview-authentication).
 >
-> Document Intelligence now supports AAD token authentication additional to local (key-based) authentication when accessing the Document Intelligence resources and storage accounts. Be sure to follow below instructions to setup correct access roles, especially if your resources are applied with `DisableLocalAuth` policy.
+> Document Intelligence now supports Azure Active Directory (Azure AD) token authentication in addition to local (key-based) authentication when accessing the Document Intelligence resources and storage accounts. Be sure to follow below instructions to set up correct access roles, especially if your resources are applied with `DisableLocalAuth` policy.
 
 There are added prerequisites for using custom models in Document Intelligence Studio. Refer to the [documentation](quickstarts/studio-custom-project.md) for step by step guidance.
 
@@ -86,7 +86,7 @@ For more information, *see* the following guidance:
   * [Prevent Shared Key authorization for an Azure Storage account](/azure/storage/common/shared-key-authorization-prevent)
  
  > [!NOTE]
- > If local (key-based) authentication is disabled for your Document Intelligence service resource, be sure to obtain **Cognitive Services User** role and your AAD token will be used to authenticate requests on Document Intelligence Studio.  The **Contributor** role only allows you to list keys but does not give you permission to use the resource when key-access is disabled.
+ > If local (key-based) authentication is disabled for your Document Intelligence service resource, be sure to obtain **Cognitive Services User** role and your Azure AD token to authenticate requests on Document Intelligence Studio. The **Contributor** role only allows you to list keys but doesn't give you permission to use the resource when key-access is disabled.
 
 * **Designating role assignments**. Document Intelligence Studio basic access requires the [`Cognitive Services User`](/azure/role-based-access-control/built-in-roles/ai-machine-learning#cognitive-services-user) role. For more information, *see* [Document Intelligence role assignments](quickstarts/try-document-intelligence-studio.md#azure-role-assignments).
 
@@ -96,7 +96,7 @@ For more information, *see* the following guidance:
 > * ✔️ **Cognitive Services User**: you need this role to Document Intelligence or Azure AI services resource to enter the analyze page.
 > * ✔️ **Contributor**: you need this role to create resource group, Document Intelligence service, or Azure AI services resource.
 > * In Azure context, Contributor role can only perform actions to control and manage the resource itself, including listing the access keys.
-> * User accounts with a Contributor are only able to access the Document Intelligence service by calling with access keys. However, when setting up access with Entra ID, key-access will be disabled and **Cognitive Service User** role will be required for an account to use the resources.
+> * User accounts with a Contributor are only able to access the Document Intelligence service by calling with access keys. However, when setting up access with Entra ID, key-access is disabled and **Cognitive Service User** role is required for an account to use the resources.
 
 ### Authentication in Studio
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンススタジオの最新情報の反映"
}
```

### Explanation
この変更では、Azure AI Document Intelligenceスタジオに関する情報が更新されています。具体的には、日付の更新といくつかの表現の修正が行われています。主な修正内容には、ドキュメントインテリジェンスのスタジオにおける機能やURLの説明を明確にするための表

## articles/ai-studio/concepts/rbac-ai-studio.md{#item-c2a11a}

<details>
<summary>Diff</summary>
````diff
@@ -110,94 +110,6 @@ In order to complete end-to-end AI development and deployment, users only need t
 
 The minimum permissions needed to create a project is a role that has the allowed action of `Microsoft.MachineLearningServices/workspaces/hubs/join` on the hub. The Azure AI Developer built-in role has this permission.
 
-## Azure AI Administrator role
-
-Prior to 11/19/2024, the system-assigned managed identity created for the hub was automatically assigned the __Contributor__ role for the resource group that contains the hub and projects. Hubs created after this date have the system-assigned managed identity assigned to the __Azure AI Administrator__ role. This role is more narrowly scoped to the minimum permissions needed for the managed identity to perform its tasks.
-
-The __Azure AI Administrator__ role is currently in public preview.
-
-[!INCLUDE [feature-preview](../includes/feature-preview.md)]
-
-The __Azure AI Administrator__ role has the following permissions:
-
-```json
-{
-    "permissions": [
-        {
-            "actions": [
-                "Microsoft.Authorization/*/read",
-                "Microsoft.CognitiveServices/*",
-                "Microsoft.ContainerRegistry/registries/*",
-                "Microsoft.DocumentDb/databaseAccounts/*",
-                "Microsoft.Features/features/read",
-                "Microsoft.Features/providers/features/read",
-                "Microsoft.Features/providers/features/register/action",
-                "Microsoft.Insights/alertRules/*",
-                "Microsoft.Insights/components/*",
-                "Microsoft.Insights/diagnosticSettings/*",
-                "Microsoft.Insights/generateLiveToken/read",
-                "Microsoft.Insights/logDefinitions/read",
-                "Microsoft.Insights/metricAlerts/*",
-                "Microsoft.Insights/metricdefinitions/read",
-                "Microsoft.Insights/metrics/read",
-                "Microsoft.Insights/scheduledqueryrules/*",
-                "Microsoft.Insights/topology/read",
-                "Microsoft.Insights/transactions/read",
-                "Microsoft.Insights/webtests/*",
-                "Microsoft.KeyVault/*",
-                "Microsoft.MachineLearningServices/workspaces/*",
-                "Microsoft.Network/virtualNetworks/subnets/joinViaServiceEndpoint/action",
-                "Microsoft.ResourceHealth/availabilityStatuses/read",
-                "Microsoft.Resources/deployments/*",
-                "Microsoft.Resources/deployments/operations/read",
-                "Microsoft.Resources/subscriptions/operationresults/read",
-                "Microsoft.Resources/subscriptions/read",
-                "Microsoft.Resources/subscriptions/resourcegroups/deployments/*",
-                "Microsoft.Resources/subscriptions/resourceGroups/read",
-                "Microsoft.Resources/subscriptions/resourceGroups/write",
-                "Microsoft.Storage/storageAccounts/*",
-                "Microsoft.Support/*",
-                "Microsoft.Search/searchServices/write",
-                "Microsoft.Search/searchServices/read",
-                "Microsoft.Search/searchServices/delete",
-                "Microsoft.Search/searchServices/indexes/*",
-                "Microsoft.DataFactory/factories/*"
-            ],
-            "notActions": [],
-            "dataActions": [],
-            "notDataActions": []
-        }
-    ]
-}
-```
-
-### Convert an existing system-managed identity to the Azure AI Administrator role
-
-> [!TIP]
-> We recommend that you convert hubs created before 11/19/2024 to use the Azure AI Administrator role. The Azure AI Administrator role is more narrowly scoped than the previously used Contributor role and follows the principal of least privilege.
-
-You can convert hubs created before 11/19/2024 by using one of the following methods:
-
-- Azure REST API: Use a `PATCH` request to the Azure REST API for the workspace. The body of the request should set `{"properties":{"allowRoleAssignmeentOnRG":true}}`. The following example shows a `PATCH` request using `curl`. Replace `<your-subscription>`, `<resource-group-name>`, `<workspace-name>`, and `<YOUR-ACCESS-TOKEN>` with the values for your scenario. For more information on using REST APIs, visit the [Azure REST API documentation](/rest/api/azure/).
-
-    ```bash
-    curl -X PATCH https://management.azure.com/subscriptions/<your-subscription>/resourcegroups/<resource-group-name>/providers/Microsoft.MachineLearningServices/workspaces/<workspace-name>?api-version=2024-04-01-preview -H "Authorization:Bearer <YOUR-ACCESS-TOKEN>"
-    ```
-
-- Azure CLI: Use the `az ml workspace update` command with the `--allow-roleassignment-on-rg true` parameter. The following example updates a workspace named `myworkspace`. This command requires the Azure Machine Learning CLI extension version 2.27.0 or later.
-
-    ```azurecli
-    az ml workspace update --name myworkspace --allow-roleassignment-on-rg true
-    ```
-
-- Azure Python SDK: Set the `allow_roleassignment_on_rg` property of the Workspace object to `True` and then perform an update operation. The following example updates a workspace named `myworkspace`. This operation requires the Azure Machine Learning SDK version 1.17.0 or later.
-
-    ```python
-    ws = ml_client.workspaces.get(name="myworkspace")
-    ws.allow_roleassignment_on_rg = True
-    ws = ml_client.workspaces.begin_update(workspace=ws).result()
-    ```
-
 ## Dependency service Azure RBAC permissions
 
 The hub has dependencies on other Azure services. The following table lists the permissions required for these services when you create a hub. The person that creates the hub needs these permissions. The person who creates a project from the hub doesn't need them.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azure AI StudioのRBAC主要情報の削除"
}
```

### Explanation
この変更では、Azure AI Studioにおけるロールベースのアクセス制御（RBAC）に関する重要な情報が大幅に削除されました。具体的には、Azure AI Administratorロールに関連する詳細や、その役割の権限についての情報が88行削除されています。これには、以前のシステム管理されたIDの設定、Azure AI Administratorロールの権限リスト、及び既存のシステム管理されたIDをこのロールに変換するための手順が含まれていました。

これにより、ドキュメントはより簡潔になったものの、従来の情報が失われたため利用者には今後のRBACの設定に関する新たな指針が必要となるでしょう。これは、システム管理されたアイデンティティの管理や、必要なRBAC権限に関連する実装に影響を与える可能性があります。

## articles/ai-studio/how-to/flow-develop.md{#item-d1ac3e}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ In this article, you learn how to create and develop your first prompt flow in A
 - If you don't have an Azure AI Foundry project already, first [create a project](create-projects.md).
 - Prompt flow requires a compute session. If you don't have a runtime, you can [create one in Azure AI Foundry portal](./create-manage-compute-session.md).
 - You need a deployed model.
-- In your project, configure access control for the blog storage account. Assign the **Storage Blob Data Contributor** role to your user account.
+- In your project, configure access control for the blob storage account. Assign the **Storage Blob Data Contributor** role to your user account.
     - In the bottom left of the Azure AI Foundry portal, select **Management center**.
     - In **Connected resources** for your project, select the link that corresponds to the **Azure Blob Storage** type. 
     - Select **View in Azure Portal**
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blobストレージアカウントの記述を修正"
}
```

### Explanation
この変更では、Azure AIスタジオに関連するドキュメント内の表現が修正されました。具体的には、「ブログストレージアカウント」という誤表記が「ブLOBストレージアカウント」に修正されています。この文の修正は、Azureの用語の一貫性を保つために重要です。全体として、文書の明確さと専門性が向上しています。

## articles/ai-studio/how-to/monitor-applications.md{#item-656e2b}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,88 @@
+---
+title: Continuously Monitor your Generative AI Applications
+titleSuffix: Azure AI Foundry
+description: This article provides instructions on how to continuously monitor Generative AI Applications.
+manager: scottpolly
+ms.service: azure-ai-studio
+ms.custom:
+  - build-2024
+ms.topic: how-to
+ms.date: 01/16/2025
+ms.reviewer: alehughes
+ms.author: lagayhar  
+author: lgayhardt
+---
+
+# Continuously monitor your generative AI applications
+
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
+
+Continuous advancements in Generative AI have led organizations to build increasingly complex applications to solve various problems (chat-bots, RAG systems, agentic systems, etc.). These applications are being used to drive innovation, improve customer experiences, and enhance decision-making. Although the models (for example, GPT-4o) powering these Generative AI applications are extremely capable, continuous monitoring has never been more important to ensure high-quality, safe, and reliable results. Continuous monitoring is effective when multiple perspectives are considered when observing an application. These perspectives include token usage and cost, operational metrics – latency, request count, etc. - and, importantly, continuous evaluation. To learn more about evaluation, see [Evaluation of generative AI applications](../concepts/evaluation-approach-gen-ai.md).
+
+Azure AI and Azure Monitor provide tools for you to continuously monitor the performance of your Generative AI applications from multiple perspectives. With Azure AI Online Evaluation, you can continuously evaluate your application agnostic of where it's deployed or what orchestration framework it's using (for example, LangChain). You can use various [built-in evaluators](../concepts/evaluation-metrics-built-in.md) which maintain parity with the [Azure AI Evaluation SDK](./develop/evaluate-sdk.md) or define your own custom evaluators. By continuously running the right evaluators over your collected trace data, your team can more effectively identify and mitigate security, quality, and safety concerns as they arise, either in pre-production or post-production. Azure AI Online Evaluation provides full integration with the comprehensive suite of observability tooling available in [Azure Monitor Application Insights](/azure/azure-monitor/app/app-insights-overview), enabling you to build custom dashboards, visualize your evaluation results over time, and configure alerting for advanced application monitoring.
+
+In summary, monitoring your generative AI applications has never been more important, due to the complexity and rapid evolvement of the AI industry. Azure AI Online Evaluation, integrated with Azure Monitor Application Insights, enables you to continuously evaluate your deployed applications to ensure that they're performant, safe, and produce high-quality results in production.
+
+## How to monitor your generative AI applications
+
+In this section, learn how to monitor your generative AI applications using Azure AI Foundry tracing, online evaluation, and trace visualization functionality. Then, learn how Azure AI Foundry integrates with Azure Monitor Application Insights for comprehensive observability and visualization.
+
+### Tracing your generative AI application
+
+The first step in continuously monitoring your application is to ensure that its telemetry data is captured and stored for analysis. To accomplish this, you'll need to instrument your generative AI application’s code to use the [Azure AI Tracing package](./develop/trace-local-sdk.md) to log trace data to an Azure Monitor Application Insights resource of your choice. This package fully conforms with the OpenTelemetry standard for observability. After you have instrumented your application's code, the trace data will be logged to your Application Insights resource.
+
+After you have included tracing in your application code, you can view the trace data in Azure AI Foundry or in your Azure Monitor Application Insights resource. To learn more about how to do this, see [monitor your generative AI application](#monitor-your-generative-ai-application-with-azure-monitor-application-insights).
+
+### Set up online evaluation
+
+After setting up tracing for your generative AI application, set up [online evaluation with the Azure AI Foundry SDK](./online-evaluation.md) to continuously evaluate your trace data as it is collected. Doing so will enable you to monitor your application's performance in production over time.
+
+> [!NOTE]
+> If you have multiple AI applications logging trace data to the same Azure Monitor Application Insights resource, it's recommended to use the service name to differentiate between application data in Application Insights. To learn how to set the service name, see [Azure AI Tracing](./develop/trace-local-sdk.md). To learn how to query for the service name within your online evaluation configuration, see [using service name in trace data](./online-evaluation.md#using-service-name-in-trace-data).
+
+### Monitor your generative AI application with Azure Monitor Application Insights
+
+In this section, you learn how Azure AI integrates with Azure Monitor Application Insights to give you an out-of-the-box dashboard view that is tailored with insights regarding your generative AI app so you can stay updated with the latest status of your application.
+
+#### Insights for your generative AI application  
+
+If you haven’t set this up, here are some quick steps:
+
+1. Navigate to your project in [Azure AI Foundry](https://ai.azure.com).
+1. Select the Tracing page on the left-hand side.
+1. Connect your Application Insights resource to your project.
+
+If you already set up tracing in Azure AI Foundry portal, all you need to do is select the link to **Check out your Insights for Generative AI application dashboard**.
+
+Once you have your data streaming into your Application Insights resource, you automatically can see it get populated in this customized dashboard.
+
+:::image type="content" source="../media/how-to/online-evaluation/open-generative-ai-workbook.gif" alt-text="Animation of an Azure workbook showing Application Insights." lightbox="../media/how-to/online-evaluation/open-generative-ai-workbook.gif":::
+
+This view is a great place for you to get started with your monitoring needs.
+
+- You can view token consumption over time to understand if you need to increase your usage limits or do additional cost analysis.
+- You can view evaluation metrics as trend lines to understand the quality of your app on a daily basis.
+- You can debug when exceptions take place and drill into traces using the **Azure Monitor End-to-end transaction details view** to figure out what went wrong.
+
+:::image type="content" source="../media/how-to/online-evaluation/custom-generative-ai-workbook.gif" alt-text="Animation of an Azure workbook showing graphs and end to end transaction details." lightbox="../media/how-to/online-evaluation/custom-generative-ai-workbook.gif":::
+
+This is an Azure Workbook that is querying data stored in your Application Insights resource. You can customize this workbook and tailor this to fit your business needs.
+To learn more, see [editing Azure Workbooks](/azure/azure-monitor/visualize/workbooks-create-workbook).
+
+This allows you to add additional custom evaluators that you might have logged or other markdown text to share summaries and use for reporting purposes.
+
+You can also share this workbook with your team so they stay informed with the latest!
+
+:::image type="content" source="../media/how-to/online-evaluation/share-azure-workbook.png" alt-text="Screenshot of an Azure Workbook showing the share button and share tab." lightbox="../media/how-to/online-evaluation/share-azure-workbook.png":::
+
+> [!NOTE]
+> When sharing this workbook with your team members, they must have at least 'Reader' role to the connected Application Insights resource to view the displayed information.
+
+## Related content
+
+- [How to run evaluations online with the Azure AI Foundry SDK](./online-evaluation.md)
+- [Trace your application with Azure AI Inference SDK](./develop/trace-local-sdk.md)
+- [Visualize your traces](./develop/visualize-traces.md)
+- [Evaluation of Generative AI Models & Applications](../concepts/evaluation-approach-gen-ai.md)
+- [Azure Monitor Application Insights](/azure/azure-monitor/app/app-insights-overview)
+- [Azure Workbooks](/azure/azure-monitor/visualize/workbooks-overview)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "生成AIアプリケーションの継続的監視に関する新しいガイドを追加"
}
```

### Explanation
この変更では、生成AIアプリケーションを継続的に監視する方法についての新しいガイドが追加され、88行の内容が挿入されました。この新しいセクションでは、Azure AI Foundryのトレース機能やオンライン評価、可視化機能を利用して、生成AIアプリケーションの監視を行う方法が説明されています。

具体的には、アプリケーションのテレメトリデータを収集するためのコードのインスツルメンテーション、Azure Monitor Application Insightsとの統合、トレースデータのオンライン評価の設定方法などが含まれています。これにより、ユーザーはアプリケーションのパフォーマンスをリアルタイムで評価し、安全で高品質な結果を提供できるようになります。また、このガイドでは、Azure MonitorのAir Insightsを用いたカスタムダッシュボードの作成や、評価メトリクスのトレンド分析を通じてアプリケーションの最新状況を把握する方法も紹介されています。

全体として、この新しいガイドは、生成AIアプリケーションの監視ニーズに応える重要なリソースとなります。

## articles/ai-studio/how-to/online-evaluation.md{#item-d9591b}

<details>
<summary>Diff</summary>
````diff
@@ -1,64 +1,52 @@
 ---
-title: Continuously Monitor your Generative AI Applications
+title: Run evaluations online in Azure AI Foundry
 titleSuffix: Azure AI Foundry
-description: This article provides instructions on how to use online and remote evaluation to continuously monitor Generative AI Applications.
+description: This article provides instructions on how to use online evaluation to continuously monitor Generative AI Applications.
 manager: scottpolly
 ms.service: azure-ai-studio
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 01/16/2025
 ms.reviewer: alehughes
 ms.author: lagayhar  
 author: lgayhardt
 ---
 
-# Continuously monitor your generative AI applications
+# How to run evaluations online with the Azure AI Foundry SDK
 
 [!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
-Continuous advancements in Generative AI have led organizations to build increasingly complex applications to solve various problems (chat-bots, RAG systems, agentic systems, etc.). These applications are being used to drive innovation, improve customer experiences, and enhance decision-making. Although the models (for example, GPT-4) powering these Generative AI applications are extremely capable, continuous monitoring has never been more important to ensure high-quality, safe, and reliable results. Continuous monitoring is effective when multiple perspectives are considered when observing an application. These perspectives include token usage and cost, operational metrics – latency, request count, etc. - and, importantly, continuous evaluation. To learn more about evaluation, see [Evaluation of generative AI applications](../concepts/evaluation-approach-gen-ai.md).
-
-Azure AI and Azure Monitor provide tools for you to continuously monitor the performance of your Generative AI applications from multiple perspectives. With Azure AI Online Evaluation, you can continuously evaluate your application agnostic of where it's deployed or what orchestration framework it's using (for example, LangChain). You can use various [built-in evaluators](../concepts/evaluation-metrics-built-in.md) which maintain parity with the [Azure AI Evaluation SDK](./develop/evaluate-sdk.md) or define your own custom evaluators. By continuously running the right evaluators over your collected trace data, your team can more effectively identify and mitigate security, quality, and safety concerns as they arise, either in pre-production or post-production. Azure AI Online Evaluation provides full integration with the comprehensive suite of observability tooling available in [Azure Monitor Application Insights](/azure/azure-monitor/app/app-insights-overview), enabling you to build custom dashboards, visualize your evaluation results over time, and configure alerting for advanced application monitoring.
-
-In summary, monitoring your generative AI applications has never been more important, due to the complexity and rapid evolvement of the AI industry. Azure AI Online Evaluation, integrated with Azure Monitor Application Insights, enables you to continuously evaluate your deployed applications to ensure that they're performant, safe, and produce high-quality results in production.
+In this article, you learn how to run evaluations online in a continuous manner with the Azure AI Foundry SDK. [Evaluations](./develop/evaluate-sdk.md) in pre-production environments is essential for ensuring that your application is safe, performant, and produces high-quality results. However, evaluation doesn't stop after your application is deployed. In production, various things can change, such as the types of queries users are sending to your application, which can influence your application's performance. To maintain a high degree of observability into your production generative AI application, it's important to [trace](./develop/trace-local-sdk.md) and continuously evaluate your application's data. By doing so, you can maintain confidence in your application's safety, quality, and performance.
 
 ## How online evaluation works
 
-In this section, you'll learn how Azure AI Online Evaluation works, how it integrates with [Azure Monitor Application Insights](/azure/azure-monitor/app/app-insights-overview), and how you can use it to run continuous evaluations over [trace](https://opentelemetry.io/docs/concepts/signals/traces/) data from your generative AI applications.
-
-### Tracing your generative AI application
-
-The first step in continuously monitoring your application is to ensure that its telemetry data is captured and stored for analysis. To accomplish this, you'll need to instrument your generative AI application’s code to use the [Azure AI Tracing package](./develop/trace-local-sdk.md) to log trace data to an Azure Monitor Application Insights resource of your choice. This package fully conforms with the OpenTelemetry standard for observability. After you have instrumented your application's code, the trace data will be logged to your Application Insights resource.
-
-After you have included tracing in your application code, you can view the trace data in Azure AI Foundry or in your Azure Monitor Application Insights resource. To learn more about how to do this, see [monitor your generative AI application](#monitor-your-generative-ai-application).
+In this section, you'll learn how online evaluation works, how it integrates with [Azure Monitor Application Insights](/azure/azure-monitor/app/app-insights-overview), and how you can use it to run continuous evaluations over [trace](https://opentelemetry.io/docs/concepts/signals/traces/) data from your generative AI applications.
 
-### Online Evaluation
+After your application is instrumented to send trace data to Application Insights, set up an online evaluation schedule to continuously evaluate this data. Online evaluation is a service that uses Azure AI compute to continuously run a configurable set of evaluators. After you have set up an online evaluation schedule with the Azure AI Foundry SDK, it runs on a configurable schedule. Each time the scheduled job runs, it performs the following steps:
 
-After your application is instrumented to send trace data to Application Insights, it’s time to set up an Online Evaluation schedule to continuously evaluate this data. Azure AI Online Evaluation is a service that uses Azure AI compute to continuously run a set of evaluators. After you have set up an Online Evaluation schedule with the Azure AI Project SDK, it runs on a customizable schedule. Each time the service runs, it performs the following steps:
-
-1. Query application trace data from the connected Application Insights resource using provided Kusto query.
+1. Query application trace data from the connected Application Insights resource using provided Kusto (KQL) query.
 1. Run each evaluator over the trace data and calculate each metric (for example, *groundedness: 3*).
 1. Write evaluation scores back to each trace using standardized semantic conventions.
 
 > [!NOTE]
-> Azure AI Online Evaluation supports the same metrics as Azure AI Evaluation. For more information on how evaluation works and which evaluation metrics are supported, see [Evaluate your Generative AI application with the Azure AI Evaluation SDK](./develop/evaluate-sdk.md)
+> Online evaluation supports the same metrics as Azure AI Evaluation. For more information on how evaluation works and which evaluation metrics are supported, see [Evaluate your Generative AI application with the Azure AI Evaluation SDK](./develop/evaluate-sdk.md).
 
-For example, let’s say you have a deployed chat application that receives many customer questions on a daily basis. You want to continuously evaluate the quality of the responses from your application. You set up an Online Evaluation schedule with a daily recurrence. You configure the evaluators: **Groundedness**,  **Coherence**, and **Fluency**. Every day, the service computes the evaluation scores for these metrics and writes the data back to Application Insights for each trace that was collected during the recurrence time window (in this example, the past 24 hours). Then, the data can be queried from each trace and made accessible in Azure AI Foundry and Azure Monitor Application Insights.
+For example, let’s say you have a deployed chat application that receives many customer questions on a daily basis. You want to continuously evaluate the quality of the responses from your application. You set up an online evaluation schedule with a daily recurrence. You configure the evaluators: **Groundedness**,  **Coherence**, and **Fluency**. Every day, the service computes the evaluation scores for these metrics and writes the data back to Application Insights for each trace that was collected during the recurrence time window (in this example, the past 24 hours). Then, the data can be queried from each trace and made accessible in Azure AI Foundry and Azure Monitor Application Insights.
 
-The evaluation results written back to each trace within Application Insights follow the following conventions. A unique span will be added to each trace for each evaluation metric.
+The evaluation results written back to each trace within Application Insights follow the following conventions. A unique span is added to each trace for each evaluation metric:
 
 | Property                                  | Application Insights Table | Fields for a given operation_ID               | Example value                        |
 |-------------------------------------------|----------------------------|-----------------------------------------------|--------------------------------------|
 | Evaluation metric                         | traces, AppTraces          | `customDimensions[“event.name”]`              | `gen_ai.evaluation.relevance`        |
 | Evaluation metric score                   | traces, AppTraces          | `customDimensions[“gen_ai.evaluation.score”]` | `3`                                  |
 | Evaluation metric comment (if applicable) | traces, AppTraces          | `message`                                     | `{“comment”: “I like the response”}` |
 
-Now that you understand how Azure AI Online Evaluation works and how it connects to Azure Monitor Application Insights, it’s time to learn how to set up the service.
+Now that you understand how online evaluation works and how it connects to Azure Monitor Application Insights, the next step is to set up the service.
 
-## Set up Online Evaluation
+## Set up online evaluation
 
-In this section, you'll learn how to configure an Online Evaluation schedule to continuously monitor your deployed generative AI application. Azure AI Project SDK offers such capabilities via a Python API and supports all of the features available in local evaluations. Use the following steps to submit your Online Evaluation schedule on your data using built-in or custom evaluators.
+In this section, you'll learn how to configure an online evaluation schedule to continuously monitor your deployed generative AI application. Azure AI Foundry SDK offers such capabilities via. A Python API and supports all of the features available in local evaluations. Use the following steps to submit your online evaluation schedule on your data using built-in or custom evaluators.
 
 > [!NOTE]
 > Evaluations are only supported in the same [regions](./develop/evaluate-sdk.md#region-support) as AI-assisted risk and safety metrics.
@@ -79,50 +67,53 @@ Complete the following prerequisite steps to set up your environment and authent
 10. Navigate to your Application Insights resource in the Azure portal and use the **Access control (IAM)** tab to add the `Log Analytics Contributor` role to the User-assigned Managed Identity you created previously.
 11. Attach the [User-assigned Managed Identity](../../machine-learning/how-to-identity-based-service-authentication.md#add-a-user-assigned-managed-identity-to-a-workspace-in-addition-to-a-system-assigned-identity) to your project.
 12. Navigate to your Azure AI Services in the Azure portal and use the **Access control (IAM)** tab to add the `Cognitive Services OpenAI Contributor` role to the User-assigned Managed Identity you created previously.
-13. Make sure you're first logged into your Azure subscription by running `az login`.
 
 ### Installation Instructions
 
-1. Create a virtual environment of your choice. To create one using conda, run the following command:
+#### Install the Azure CLI and sign in
+
+[!INCLUDE [Install the Azure CLI](../includes/install-cli.md)]
+
+#### Create a new Python environment
+
+[!INCLUDE [Install Python](../includes/install-python.md)]
+
+You can also create a new Python environment using `conda`:
 
 ```bash
 conda create -n online-evaluation
 conda activate online-evaluation
 ```
 
-2. Install the required packages by running the following command:
+#### Install the required packages:
 
 ```bash
 pip install azure-identity azure-ai-projects azure-ai-ml
 ```
 
 > [!TIP]
-> Optionally, you can `pip install azure-ai-evaluation` if you want a code-first experience to fetch evaluator id for built-in evaluators in code. To learn how to do this, see [Specifying evaluators from evaluator library](./develop/evaluate-sdk.md#specifying-evaluators-from-evaluator-library).
+> Optionally, you can use `pip install azure-ai-evaluation` if you want a code-first experience to fetch evaluator ID for built-in evaluators in code. To learn how to do this, see [Specifying evaluators from evaluator library](./develop/evaluate-sdk.md#specifying-evaluators-from-evaluator-library).
 
 ### Set up tracing for your generative AI application
 
-The first step in monitoring your application is to set up tracing. To learn how to do so such that data is logged to Application Insights, see [set up tracing for your generative AI application](./develop/trace-local-sdk.md).
+Prior to setting up online evaluation, ensure you have first [set up tracing for your generative AI application](./develop/trace-local-sdk.md).
 
 #### Using service name in trace data
 
-To identify your service via a unique ID in Application Insights, you can use the service name OpenTelemetry property in your trace data. This is particularly useful if you're logging data from multiple applications to the same Application Insights resource, and you want to differentiate between them. For example, lets say you have two applications: **App-1** and **App-2**, with tracing configured to log data to the same Application Insights resource. Perhaps you'd like to set up **App-1** to be evaluated continuously by **Relevance** and **App-2** to be evaluated continuously by **Groundedness**. You can use the service name to differentiate between the applications in your Online Evaluation configurations.
+To identify your application via a unique ID in Application Insights, you can use the service name OpenTelemetry property in your trace data. This is particularly useful if you're logging data from multiple applications to the same Application Insights resource, and you want to differentiate between them. For example, lets say you have two applications: **App-1** and **App-2**, with tracing configured to log data to the same Application Insights resource. Perhaps you'd like to set up **App-1** to be evaluated continuously by **Relevance** and **App-2** to be evaluated continuously by **Groundedness**. You can use the service name to differentiate between the applications in your online evaluation configurations.
 
 To set up the service name property, you can do so directly in your application code by following the steps, see  [Using multiple tracer providers with different Resource](https://opentelemetry.io/docs/languages/python/cookbook/#using-multiple-tracer-providers-with-different-resource). Alternatively, you can set the environment variable `OTEL_SERVICE_NAME` prior to deploying your app. To learn more about working with the service name, see [OTEL Environment Variables](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration) and [Service Resource Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/resource/#service).
 
-To query trace data for a given service name, query for the `cloud_roleName` property. Add the following line to the KQL query you use within your Online Evaluation set-up:
-
-```sql
-| where cloud_RoleName == "service_name"
-```
+For more information on using the service name to differentiate between your generative AI applications, see [tracing](./develop/trace-local-sdk.md).
 
 ### Query stored trace data in Application Insights
 
-Using the [Kusto Query Language (KQL)](/kusto/query/?view=microsoft-fabric&preserve-view=true), you can query your generative AI application's trace data from Application Insights to use for continuous Online Evaluation. If you use the [Azure AI Tracing package](./develop/trace-local-sdk.md) to trace your generative AI application, you can use the following Kusto query to view the data in Application Insights:
+Using the [Kusto Query Language (KQL)](/kusto/query/?view=microsoft-fabric&preserve-view=true), you can query your generative AI application's trace data from Application Insights to use for continuous online evaluation. If you use the [Azure AI Tracing package](./develop/trace-local-sdk.md) to trace your generative AI application, you can use the following Kusto query:
 
 > [!IMPORTANT]
-> The KQL query used by the Online Evaluation service must output the following columns: `operation_Id`, `operation_ParentId`, and `gen_ai_response_id`. Additionally, each evaluator has its own input data requirements. The KQL query must output these columns to be used as inputs to the evaluators themselves. For a list of data requirements for evaluators, see [data requirements for built-in evaluators](./develop/evaluate-sdk.md#data-requirements-for-built-in-evaluators).
+> The KQL query used by the online evaluation service must output the following columns: `operation_Id`, `operation_ParentId`, and `gen_ai_response_id`. Additionally, each evaluator has its own input data requirements. The KQL query must output these columns to be used as inputs to the evaluators themselves. For a list of data requirements for evaluators, see [data requirements for built-in evaluators](./develop/evaluate-sdk.md#data-requirements-for-built-in-evaluators).
 
-```SQL
+```kusto
 let gen_ai_spans = (
     dependencies
     | where isnotnull(customDimensions["gen_ai.system"])
@@ -164,11 +155,17 @@ gen_ai_spans
 | project Input, System, Output, operation_Id, operation_ParentId, gen_ai_response_id = response_id
 ```
 
+If you're using the `OTEL_SERVICE_NAME` environment variable in your generative AI application to set the service name, you can query for the `cloud_RoleName` within your online evaluation schedule by adding the following line to your Kusto (KQL) query:
+
+```kusto
+| where cloud_RoleName == "service_name"
+```
+
 Optionally, you can use the [sample operator](/kusto/query/sample-operator?view=azure-monitor&preserve-view=true) or [take operator](/kusto/query/take-operator?view=microsoft-fabric&preserve-view=true) in your Kusto query such that it only returns a subset of traces. Since AI-assisted evaluations can be costly at scale, this approach can help you control costs by only evaluating a random sample (or `n` traces) of your data.
 
-### Set up Online Evaluation with Azure AI Project SDK
+### Set up online evaluation with Azure AI Project SDK
 
-You can submit an Online Evaluation scheduled job with the Azure AI Project SDK via a Python API. See the below script to learn how to set up Online Evaluation with performance and quality (AI-assisted) evaluators. To view a comprehensive list of supported evaluators, see [Evaluate with the Azure AI Evaluation SDK](./develop/evaluate-sdk.md). To learn how to use custom evaluators, see [custom evaluators](./develop/evaluate-sdk.md#specifying-custom-evaluators).
+You can submit an online evaluation scheduled job with the Azure AI Project SDK via a Python API. See the below script to learn how to set up online evaluation with performance and quality (AI-assisted) evaluators. To view a comprehensive list of supported evaluators, see [Evaluate with the Azure AI Evaluation SDK](./develop/evaluate-sdk.md). To learn how to use custom evaluators, see [custom evaluators](./develop/evaluate-sdk.md#specifying-custom-evaluators).
 
 Start by importing the required packages and configuring the required variables:
 
@@ -190,9 +187,6 @@ from azure.ai.evaluation import CoherenceEvaluator
 # Name of your online evaluation schedule
 SAMPLE_NAME = "online_eval_name"
 
-# Name of your generative AI application (will be available in trace data in Application Insights)
-SERVICE_NAME = "service_name"
-
 # Connection string to your Azure AI Foundry project
 # Currently, it should be in the format "<HostName>;<AzureSubscriptionId>;<ResourceGroup>;<HubName>"
 PROJECT_CONNECTION_STRING = "<HostName>;<AzureSubscriptionId>;<ResourceGroup>;<HubName>"
@@ -208,7 +202,7 @@ APPLICATION_INSIGHTS_RESOURCE_ID = "appinsights_resource_id"
 KUSTO_QUERY = "let gen_ai_spans=(dependencies | where isnotnull(customDimensions[\"gen_ai.system\"]) | extend response_id = tostring(customDimensions[\"gen_ai.response.id\"]) | project id, operation_Id, operation_ParentId, timestamp, response_id); let gen_ai_events=(traces | where message in (\"gen_ai.choice\", \"gen_ai.user.message\", \"gen_ai.system.message\") or tostring(customDimensions[\"event.name\"]) in (\"gen_ai.choice\", \"gen_ai.user.message\", \"gen_ai.system.message\") | project id= operation_ParentId, operation_Id, operation_ParentId, user_input = iff(message == \"gen_ai.user.message\" or tostring(customDimensions[\"event.name\"]) == \"gen_ai.user.message\", parse_json(iff(message == \"gen_ai.user.message\", tostring(customDimensions[\"gen_ai.event.content\"]), message)).content, \"\"), system = iff(message == \"gen_ai.system.message\" or tostring(customDimensions[\"event.name\"]) == \"gen_ai.system.message\", parse_json(iff(message == \"gen_ai.system.message\", tostring(customDimensions[\"gen_ai.event.content\"]), message)).content, \"\"), llm_response = iff(message == \"gen_ai.choice\", parse_json(tostring(parse_json(tostring(customDimensions[\"gen_ai.event.content\"])).message)).content, iff(tostring(customDimensions[\"event.name\"]) == \"gen_ai.choice\", parse_json(parse_json(message).message).content, \"\")) | summarize operation_ParentId = any(operation_ParentId), Input = maxif(user_input, user_input != \"\"), System = maxif(system, system != \"\"), Output = maxif(llm_response, llm_response != \"\") by operation_Id, id); gen_ai_spans | join kind=inner (gen_ai_events) on id, operation_Id | project Input, System, Output, operation_Id, operation_ParentId, gen_ai_response_id = response_id"
 ```
 
-Next, define a client and an Azure OpenAI GPT deployment (such as `GPT-4`) which will be used to run your Online Evaluation schedule. Also, connect to your Application Insights resource:
+Next, define a client and an Azure OpenAI GPT deployment (such as `GPT-4`) which will be used to run your online evaluation schedule. Also, connect to your Application Insights resource:
 
 ```python
 # Connect to your Azure AI Foundry Project
@@ -220,8 +214,7 @@ project_client = AIProjectClient.from_connection_string(
 # Connect to your Application Insights resource 
 app_insights_config = ApplicationInsightsConfiguration(
     resource_id=APPLICATION_INSIGHTS_RESOURCE_ID,
-    query=KUSTO_QUERY,
-    service_name=SERVICE_NAME
+    query=KUSTO_QUERY
 )
 
 # Connect to your Azure OpenAI Service resource. You must use a GPT model deployment for this example.
@@ -264,7 +257,7 @@ coherence_evaluator_config = EvaluatorConfiguration(
 
 Lastly, define the recurrence and create the schedule:
 
-**Note: In the prerequisite steps, you created a User-assigned managed identity to authenticate the Online Evaluation schedule to your Application Insights resource. The `AzureMSIClientId` in the `properties` parameter of the `EvaluationSchedule` class is the `clientId` of this identity.**
+**Note: In the prerequisite steps, you created a User-assigned managed identity to authenticate the online evaluation schedule to your Application Insights resource. The `AzureMSIClientId` in the `properties` parameter of the `EvaluationSchedule` class is the `clientId` of this identity.**
 
 ```python
 # Frequency to run the schedule
@@ -294,20 +287,20 @@ created_evaluation_schedule = project_client.evaluations.create_or_replace_sched
 print(f"Successfully submitted the online evaluation schedule creation request - {created_evaluation_schedule.name}, currently in {created_evaluation_schedule.provisioning_state} state.")
 ```
 
-#### Perform operations on an Online Evaluation schedule
+#### Perform operations on an online evaluation schedule
 
-You can get, list, and disable Online Evaluation schedules by adding the following code to your Online Evaluation configuration script:
+You can get, list, and disable online evaluation schedules by adding the following code to your online evaluation configuration script:
 
-**Warning: Please wait a small amount of time (~30 seconds) between creating an Online Evaluation schedule and running the `get_schedule()` API.**
+**Warning: Please wait a small amount of time (~30 seconds) between creating an online evaluation schedule and running the `get_schedule()` API.**
 
-Get an Online Evaluation schedule:
+Get an online evaluation schedule:
 
 ```python
 name = "<my-online-evaluation-name>"
 get_evaluation_schedule = project_client.evaluations.get_schedule(name)
 ```
 
-List all Online Evaluation schedules:
+List all online evaluation schedules:
 
 ```python
 count = 0
@@ -318,55 +311,18 @@ for evaluation_schedule in project_client.evaluations.list_schedule():
         print(f"Total evaluation schedules: {count}")
 ```
 
-Disable (soft-delete) Online Evaluation schedule:
+Disable (soft-delete) online evaluation schedule:
 
 ```python
 name = "<my-online-evaluation-name>"
 project_client.evaluations.disable_schedule(name)
 ```
 
-## Monitor your generative AI application
-
-In this section, you'll learn how Azure AI integrates with Azure Monitor Application Insights to give you an out-of-the-box dashboard view that is tailored with insights regarding your generative AI app so you can stay updated with the latest status of your application.
-
-### Insights for your generative AI application  
-
-If you haven’t set this up, here are some quick steps:
-
-1. Navigate to your project in [Azure AI Foundry](https://ai.azure.com).
-1. Select the Tracing page on the left-hand side.
-1. Connect your Application Insights resource to your project.
-
-If you already set up tracing in Azure AI Foundry portal, all you need to do is select the link to **Check out your Insights for Generative AI application dashboard**.
-
-Once you have your data streaming into your Application Insights resource, you automatically can see it get populated in this customized dashboard.
-
-:::image type="content" source="../media/how-to/online-evaluation/open-generative-ai-workbook.gif" alt-text="Animation of an Azure workbook showing Application Insights." lightbox="../media/how-to/online-evaluation/open-generative-ai-workbook.gif":::
-
-This view is a great place for you to get started with your monitoring needs.
-
-- You can view token consumption over time to understand if you need to increase your usage limits or do additional cost analysis.
-- You can view evaluation metrics as trend lines to understand the quality of your app on a daily basis.
-- You can debug when exceptions take place and drill into traces using the **Azure Monitor End-to-end transaction details view** to figure out what went wrong.
-
-:::image type="content" source="../media/how-to/online-evaluation/custom-generative-ai-workbook.gif" alt-text="Animation of an Azure workbook showing graphs and end to end transaction details." lightbox="../media/how-to/online-evaluation/custom-generative-ai-workbook.gif":::
-
-This is an Azure Workbook that is querying data stored in your Application Insights resource. You can customize this workbook and tailor this to fit your business needs.
-To learn more, see [editing Azure Workbooks](/azure/azure-monitor/visualize/workbooks-create-workbook).
-
-This allows you to add additional custom evaluators that you might have logged or other markdown text to share summaries and use for reporting purposes.
-
-You can also share this workbook with your team so they stay informed with the latest!
-
-:::image type="content" source="../media/how-to/online-evaluation/share-azure-workbook.png" alt-text="Screenshot of an Azure Workbook showing the share button and share tab." lightbox="../media/how-to/online-evaluation/share-azure-workbook.png":::
-
-> [!NOTE]
-> When sharing this workbook with your team members, they must have atleast 'Reader' role to the connected Application Insights resource to view the displayed information.
-
 ## Related content
 
+- [Monitor your generative AI applications](./monitor-applications.md)
 - [Trace your application with Azure AI Inference SDK](./develop/trace-local-sdk.md)
 - [Visualize your traces](./develop/visualize-traces.md)
 - [Evaluation of Generative AI Models & Applications](../concepts/evaluation-approach-gen-ai.md)
 - [Azure Monitor Application Insights](/azure/azure-monitor/app/app-insights-overview)
-- [Azure Workbooks](/azure/azure-monitor/visualize/workbooks-overview)
+- [Azure Workbooks](/azure/azure-monitor/visualize/workbooks-overview)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オンライン評価に関する内容を更新"
}
```

### Explanation
この変更では、Azure AI Foundryにおける「オンライン評価」に関するドキュメントが更新され、50行の追加と94行の削除が行われました。タイトルは「生成AIアプリケーションの継続的監視」から「Azure AI Foundryでオンライン評価を実行する方法」に変更され、主にオンライン評価の実施方法に焦点を当てています。

文書全体の構成が見直され、Azure AI Foundry SDKを用いたオンライン評価のセットアップ手順が詳細に説明されています。また、評価の実行や監視における重要なポイントが強調され、生成AIアプリケーションのパフォーマンスを継続的に評価するための実践的なガイダンスが提供されています。

削除された部分は、以前の内容に比べて冗長だったと考えられ、より明確かつ簡潔な情報が提供されるよう改善されています。結果として、この改訂はユーザーがオンライン評価をより効率的に実施できるよう支援する内容となっています。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -335,6 +335,8 @@ items:
     - name: View evaluation results in the portal
       href: how-to/evaluate-results.md
       displayName: accuracy,metrics
+    - name: Run evaluations online
+      href: how-to/online-evaluation.md
     - name: Evaluate flows in the portal
       items:
         - name: Submit batch run and evaluate a flow
@@ -346,7 +348,7 @@ items:
   - name: Deploy and monitor generative AI apps
     items:
     - name: Continuously monitor your applications
-      href: how-to/online-evaluation.md
+      href: how-to/monitor-applications.md
     - name: Deploy and monitor flows
       items:
       - name: Deploy a flow for real-time inference
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCの更新: オンライン評価に関する項目を追加"
}
```

### Explanation
この変更では、AI Studio内のトピックの目次（TOC）である`toc.yml`が更新され、3行が追加され、1行が削除されました。具体的には、「オンライン評価を実行する」項目が新たにTOCに追加され、ユーザーがオンライン評価に関するガイドにアクセスしやすくなっています。

また、「生成AIアプリケーションを継続的に監視する」項目のリンクは「how-to/online-evaluation.md」から「how-to/monitor-applications.md」に変更され、これにより、関連するコンテンツへのナビゲーションが更新されています。このように、ユーザーが目的の情報にリンクしやすくすることを意図したマイナーなアップデートの一環として、TOCが整備されました。


