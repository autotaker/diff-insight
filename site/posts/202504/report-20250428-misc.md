---
date: '2025-04-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0b33f02...MicrosoftDocs:f5bcaf5
summary: この変更では、ドキュメントインテリジェンス関連の資料が更新され、主に日付の修正、用語の一貫性の確保、文言の微調整が行われました。新しい機能や破壊的変更はありませんが、情報の最新性と正確性を反映しています。この更新によって、ユーザーがAzureのAIサービスをより効率的に活用できるようになり、特に専門用語の一貫した使用と情報の正確さが向上します。最終的には、ユーザーのデベロッパーエクスペリエンスが改善され、信頼性の高い情報からの意思決定が可能となります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0b33f02...MicrosoftDocs:f5bcaf5){target="_blank"}

<format>
# ハイライト

これらの変更では、ドキュメントインテリジェンス関連資料の更新が行われ、主に日付の修正、用語の一貫性確保、文言の微調整が実施されました。新機能や大きな破壊的変更は含まれていないが、情報の最新性と正確性を反映しています。

## 新機能

特に新しい機能は追加されていません。

## 破壊的変更

破壊的変更はありません。

## その他の更新

- ドキュメントの日付が最新のものに更新されました。
- 用語の統一が行われ、「retrieval-augmented generation」という用語が一貫したスタイルで記述されるようになった。
- 微細な文言の改善が行われ、文書の流れをより自然にしています。
- 構造分析およびセクションハイアラーキーに関する説明が強調されました。

# インサイト

この変更は、AzureのAIサービス、特にドキュメントインテリジェンスに関するドキュメントの質と一貫性を向上させる意図があります。提供される情報が最新で正確であることを保証するために、更新された日付が反映されていることが重要です。さらに、用語の一貫性を保ったことにより、ユーザーはより直感的に技術を理解できるようになります。文言の微調整と構文の改善は、小さな変更であっても、ユーザーの理解を助け、大きなインパクトをもたらします。

この更新により、最終的にはユーザーのデベロッパーエクスペリエンスが改善し、Azure AIを効率的に活用できるようになります。特に専門用語の一貫した使用方法や、FAQなどのコンテンツでの情報の正確性がさらに向上することにより、ユーザーはドキュメントを参照する際に、より信頼性の高い情報から意思決定を行うことが可能です。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [analyze-document-response.md](#item-f785b2) | minor update | ドキュメントインテリジェンスの応答の更新 | modified | 7 | 7 | 14 | 
| [faq.yml](#item-7a051f) | minor update | FAQの更新 | modified | 2 | 2 | 4 | 
| [layout.md](#item-f7c4c8) | minor update | レイアウトモデルに関するドキュメントの更新 | modified | 5 | 5 | 10 | 


# Modified Contents
## articles/ai-services/document-intelligence/concept/analyze-document-response.md{#item-f785b2}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 11/19/2024
+ms.date: 04/23/2025
 ms.author: vikurpad
 ms.custom:
   - references_regions
@@ -34,7 +34,7 @@ The Document Intelligence APIs analyze images, PDFs, and other document files to
 All content elements are grouped according to pages, specified by page number (`1`-indexed). They're also sorted by reading order that arranges semantically contiguous elements together, even if they cross line or column boundaries. When the reading order among paragraphs and other layout elements is ambiguous, the service generally returns the content in a left-to-right, top-to-bottom order.
 
 > [!NOTE]
-> Currently, Document Intelligence does not support reading order across page boundaries. Selection marks are not positioned within the surrounding words.
+> Currently, Document Intelligence doesn't support reading order across page boundaries. Selection marks aren't positioned within the surrounding words.
 
 The top-level content property contains a concatenation of all content elements in reading order. All elements specify their position in the reader order via spans within this content string. The content of some elements isn't always contiguous.
 
@@ -71,7 +71,7 @@ Bounding regions describe the visual position of each element in the file. When
 :::image type="content" source="../media/bounding-regions.png" alt-text="Screenshot of detected bounding regions example.":::
 
 > [!NOTE]
-> Currently, Document Intelligence only returns 4-vertex quadrilaterals as bounding polygons. Future versions may return different number of points to describe more complex shapes, such as curved lines or non-rectangular images. Bounding regions applied only to rendered files, if the file is not rendered, bounding regions are not returned. Currently files of docx/xlsx/pptx/html format are not rendered.
+> Currently, Document Intelligence only returns `4-vertex` quadrilaterals as bounding polygons. Future versions may return different number of points to describe more complex shapes, such as curved lines or nonrectangular images. Bounding regions are applied only to rendered files, if the file isn't rendered, bounding regions aren't returned. Currently files of docx/xlsx/pptx/html format aren't rendered.
 
 ### Content elements
 
@@ -107,7 +107,7 @@ Select paragraphs can also be associated with a functional role in the document.
 A page is a grouping of content that typically corresponds to one side of a sheet of paper. A rendered page is characterized via width and height in the specified unit. In general, images use pixel while PDFs use inch. The angle property describes the overall text angle in degrees for pages that can be rotated.
 
 > [!NOTE]
-> For spreadsheets like Excel, each sheet is mapped to a page. For presentations, like PowerPoint, each slide is mapped to a page. For file formats without a native concept of pages without rendering like HTML or Word documents, the main content of the file is considered a single page.
+> For spreadsheets like Excel, each sheet is mapped to a page. For presentations, like PowerPoint, each slide is mapped to a page. For file formats like HTML or Word documents, which lack a native page concept without rendering, the entire main content is treated as a single page.
 
 #### Table
 
@@ -167,7 +167,7 @@ When *output=figures* is specified during the initial `Analyze` operation, the s
 
 #### Sections
 
-Hierarchical document structure analysis is pivotal in organizing, comprehending, and processing extensive documents. This approach is vital for semantically segmenting long documents to boost comprehension, facilitate navigation, and improve information retrieval. The advent of [Retrieval Augmented Generation (RAG)](../concept/retrieval-augmented-generation.md) in document generative AI underscores the significance of hierarchical document structure analysis. The Layout model supports sections and subsections in the output, which identifies the relationship of sections and object within each section. The hierarchical structure is maintained in `elements` of each section.
+Hierarchical document structure analysis is pivotal in organizing, comprehending, and processing extensive documents. This approach is vital for semantically segmenting long documents to boost comprehension, facilitate navigation, and improve information retrieval. The advent of [retrieval-augmented generation (RAG)](../concept/retrieval-augmented-generation.md) in document generative AI underscores the significance of hierarchical document structure analysis. The Layout model supports sections and subsections in the output, which identifies the relationship of sections and object within each section. The hierarchical structure is maintained in `elements` of each section.
 
 ```json
 {
@@ -221,14 +221,14 @@ A language element describes the detected language for content specified via spa
 ### Semantic elements
 
 > [!NOTE]
-> The semantic elements discussed here apply to Document Intelligence prebuilt models. Your custom models may return different data representations. For example, date and time returned by a custom model may be represented in a pattern that differs from standard ISO 8601 formatting.
+> The mentioned semantic elements apply to Document Intelligence prebuilt models. Your custom models may return different data representations. For example, date and time returned by a custom model may be represented in a pattern that differs from standard ISO 8601 formatting.
 
 #### Document
 
 A document is a semantically complete unit. A file can contain multiple documents, such as multiple tax forms within a PDF file, or multiple receipts within a single page. However, the ordering of documents within the file doesn't fundamentally affect the information it conveys.
 
 > [!NOTE]
-> Currently, Document Intelligence does not support multiple documents on a single page.
+> Currently, Document Intelligence doesn't support multiple documents on a single page.
 
 The document type describes documents sharing a common set of semantic fields, represented by a structured schema, independent of its visual template or layout. For example, all documents of type "receipt" can contain the merchant name, transaction date, and transaction total, although restaurant and hotel receipts often differ in appearance.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスの応答の更新"
}
```

### Explanation
この変更では、「analyze-document-response.md」ファイルに対し、日付の更新や文言の微調整が行われました。具体的には、以下の点が変更されています。

1. **日付の更新**: 最初の行で日付を「11/19/2024」から「04/23/2025」に変更しました。これは、ドキュメントの発効や関連する情報のリリース予定日を反映している可能性があります。

2. **表現の改善**: ドキュメントの内容に関するいくつかの文が微調整され、より明確または流暢な表現に変更されました。例えば、「Currently, Document Intelligence does not support reading order across page boundaries.」が「Currently, Document Intelligence doesn't support reading order across page boundaries.」に変更されています。この変更は、非公式な略語を使用することで文章をスムーズにし、読者に対する親しみやすさを増しています。

3. **テクニカル用語の一貫性**: 特に「4-vertex quadrilaterals」や「bounding regions」についての説明が具体的に改訂され、同様の用語が使用され続けるよう注意が払われています。

これらの更新は、主に読みやすさ・理解しやすさの向上を目的としていると考えられます。また、将来的な機能追加についての注意を促す文も含まれており、ユーザーに最新の機能や制限について認識させるためのものです。全体として、これらの変更はドキュメントの質を向上させ、ユーザーエクスペリエンスを改善するために寄与しています。

## articles/ai-services/document-intelligence/faq.yml{#item-7a051f}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ metadata:
   ms.service: azure-ai-document-intelligence
   ms.custom: references_regions
   ms.topic: faq
-  ms.date: 01/14/2025
+  ms.date: 04/23/2025
   ms.author: lajanuar
 title: Frequently asked questions
 summary: |
@@ -56,7 +56,7 @@ sections:
 
           - With Azure AI Document Intelligence and Azure OpenAI combined, you can build an enterprise application to seamlessly interact with your documents using natural language. You can easily find answers, gain valuable insights, and generate new and engaging content from existing documents.
 
-          - You can find more details on the [retrieval augmented generation pattern here](concept/retrieval-augmented-generation.md).
+          - You can find more details on the [retrieval-augmented generation pattern here](concept/retrieval-augmented-generation.md).
 
       - question: |
          Can Document Intelligence help with semantic chunking within documents for retrieval-augmented generation?
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQの更新"
}
```

### Explanation
この変更では、`faq.yml` ファイルに対していくつかの修正が行われました。主な変更点は以下の通りです。

1. **日付の更新**: `ms.date` フィールドの値が「01/14/2025」から「04/23/2025」に変更されました。これは、ドキュメントが更新された新しい日付を示しており、内容の最新性を反映しています。

2. **文言の微調整**: 「retrieval augmented generation」という用語が「retrieval-augmented generation」とハイフン付きで一貫して使用されるように変更されました。これにより、用語のスタイルが統一され、文書全体の一貫性が保たれています。

3. **コンテンツの整頓**: FAQの回答部分において、Azure AI Document Intelligence と Azure OpenAI の統合に関する説明が引き続き行われ、ユーザーにどのようにそれらを活用できるかの理解を促進しています。

この更新は、主に日付の修正と用語の一貫性に関するもので、FAQに表示される情報の正確性を向上させることを意図しています。全体として、これによりユーザーがより正確で理解しやすい情報にアクセスできるようになっています。

## articles/ai-services/document-intelligence/prebuilt/layout.md{#item-f7c4c8}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 03/27/2025
+ms.date: 04/23/2025
 ms.author: lajanuar
 ---
 
@@ -120,7 +120,7 @@ The layout model extracts structural elements from your documents. To follow are
 * [**Figures**](#figures)
 * [**Sections**](#sections)
 
-Run the sample layout document analysis within [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio), then navigate to the results tab to access the full JSON output.
+Run the sample layout document analysis within [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio), then navigate to the results tab and access the full JSON output.
 
    :::image type="content" source="../media/studio/json-output-tab.png" alt-text="Screenshot of results JSON output tab in the Document Intelligence Studio.":::
 
@@ -526,7 +526,7 @@ if result.figures:
 
 ### Sections
 
-Hierarchical document structure analysis is pivotal in organizing, comprehending, and processing extensive documents. This approach is vital for semantically segmenting long documents to boost comprehension, facilitate navigation, and improve information retrieval. The advent of [Retrieval Augmented Generation (RAG)](../concept/retrieval-augmented-generation.md) in document generative AI underscores the significance of hierarchical document structure analysis. The Layout model supports sections and subsections in the output, which identifies the relationship of sections and object within each section. The hierarchical structure is maintained in `elements` of each section. You can use [output response to markdown format](#output-response-to-markdown-format) to easily get the sections and subsections in markdown.
+Hierarchical document structure analysis is pivotal in organizing, comprehending, and processing extensive documents. This approach is vital for semantically segmenting long documents to boost comprehension, facilitate navigation, and improve information retrieval. The advent of [retrieval-augmented generation (RAG)](../concept/retrieval-augmented-generation.md) in document generative AI underscores the significance of hierarchical document structure analysis. The Layout model supports sections and subsections in the output, which identifies the relationship of sections and object within each section. The hierarchical structure is maintained in `elements` of each section. You can use [output response to markdown format](#output-response-to-markdown-format) to easily get the sections and subsections in markdown.
 
 #### [Sample code](#tab/sample-code)
 
@@ -681,8 +681,8 @@ After you retrieve you key and endpoint, you can use the following development o
 ### [REST API](#tab/rest)
 
 
-* [2023-07-31 GA (v3.1)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)
-* [2022-08-31 GA (v3.0)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
+* [`2023-07-31` GA (v3.1)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)
+* [`2022-08-31` GA (v3.0)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
 
 # [Client libraries](#tab/sdks)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レイアウトモデルに関するドキュメントの更新"
}
```

### Explanation
この変更では、`layout.md` ファイルに対していくつかの重要な修正が行われました。主な内容は以下の通りです。

1. **日付の更新**: `ms.date` フィールドが「03/27/2025」から「04/23/2025」に変更されました。この変更は、ドキュメントの更新日を反映させ、最新の情報を提供することを目的としています。

2. **文言の微調整**: 構文の一部で、単語のつなぎ方に若干の変更が加えられました。具体的には、「navigate to the results tab to access the full JSON output.」が「navigate to the results tab and access the full JSON output.」に変更され、より自然な流れとなっています。

3. **内容の一貫性の確保**: 「retrieval-augmented generation」という用語が一貫してハイフンを入れて表記されるようになり、ドキュメント内での用語の一貫性が保たれています。

4. **構造分析の説明の強調**: ドキュメント構造の分析やセクションのハイアラーキーに関する説明が強調されており、ユーザーにとって重要な情報が分かりやすく提示されています。特に、セクションやサブセクションをMarkdown形式で取得する方法に関する情報も提供されています。

これらの更新は、ユーザーに対してドキュメントの内容をより正確かつ分かりやすくすることを目的としており、最終的にはユーザーエクスペリエンスの向上に寄与しています。


