---
date: '2025-05-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:df7d67e...MicrosoftDocs:2280088
summary: このドキュメントでは、Azure AI Document Intelligenceの「レイアウトAPI」に関するマークダウン要素のサポートについての詳細な新しいドキュメントが追加されたことが紹介されています。主な変更点は、新たに追加されたマークダウン要素に関するドキュメントで、具体的な使用方法や出力方法が説明されています。また、破壊的変更はなく、他の関連文書の更新も行われています。これらの変更は、開発者がマークダウン形式での文書出力を容易に取り扱えるようにし、ドキュメントの利用効率を向上させることを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:df7d67e...MicrosoftDocs:2280088){target="_blank"}

<format>
# Highlights
このドキュメント更新では、Azure AI Document Intelligenceの「レイアウトAPI」に関するマークダウン要素のサポートを詳細に説明する新しいドキュメントが追加されました。また、関連する他のドキュメントにもいくつかのマイナーアップデートが行われ、目次ファイルに新しい項目が追加されました。

## New features
- 「マークダウン要素」に関する詳細なドキュメントが新たに追加されました。これにより、APIを使用して文書をマークダウン形式でどのように出力し、利用するかの具体例や方法が詳述されています。

## Breaking changes
- 特に大きな破壊的変更はありません。

## Other updates
- 「レイアウトAPI」に関するドキュメントの日付更新と注釈の追加。
- レイアウトAPIのマークダウン出力要素に関する目次項目の追加。
- 「テキスト要約」のAPIパラメータ名が「sentenceLength」から「summaryLength」に変更されました。

# Insights
この一連の変更は、Azure AI Document Intelligenceのプロダクトを使用する開発者にとって非常に役立つ情報を提供することを目的としています。特に、マークダウン形式での文書出力が可能になることで、開発者は様々なプラットフォームやアプリケーションで簡単に文書を取り扱えるようになります。例えば、ドキュメントをJSONではなく、より人間に読みやすいマークダウン形式で出力することで、エンドユーザーとのコミュニケーションやドキュメント管理が容易になります。

レイアウトAPIのドキュメントにおける日付更新や注釈の追加は、常に最新の情報を提供しユーザーにとっての信頼性を高める効果があります。また、目次の拡充は、ユーザーが必要な情報を迅速に見つけられるようにし、全体的なドキュメントの利用効率を向上させます。

「テキスト要約」ドキュメントでのパラメータ名の変更は、APIの使い方を明確にし、利用者が期待される結果を直感的に得ることができるようにするためのものであり、文書化の品質向上にも寄与しています。これにより、ユーザー体験が改善され、開発プロセス全体の効率が向上するでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [markdown-elements.md](#item-ec4b62) | new feature | マークダウン要素に関する新しい文書の追加 | added | 225 | 0 | 225 | 
| [layout.md](#item-f7c4c8) | minor update | レイアウトAPIに関するドキュメントの日付更新と注釈追加 | modified | 2 | 2 | 4 | 
| [toc.yml](#item-81aa7b) | minor update | 目次にマークダウン出力要素に関する項目を追加 | modified | 3 | 0 | 3 | 
| [text-summarization.md](#item-8a6034) | minor update | 要約APIのパラメータ名を変更 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/concept/markdown-elements.md{#item-ec4b62}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,225 @@
+---
+title: Document Intelligence supported Markdown elements
+titleSuffix: Azure AI services
+description: Description of the supported Markdown elements returned as part of the Layout API response and how to use the response in your applications.
+author: laujan
+manager: nitinme
+ms.service: azure-ai-document-intelligence
+ms.topic: conceptual
+ms.date: 05/05/2025
+ms.author: tonyeiyalla
+
+---
+
+# Understanding Document Intelligence Layout API Markdown Output Format
+
+Azure AI Document Intelligence Layout API can transform your documents into rich Markdown, preserving their original structure and formatting. Just specify `outputContentFormat=markdown` in your request to receive semantically structured content that maintains paragraphs, headings, tables, and other document elements in their proper hierarchy.
+
+This Markdown output elegantly captures the document's original organization while providing standardized, easily consumable content for downstream applications. The preserved semantic structure enables more sophisticated document processing workflows without losing the context and relationships between document elements.
+
+
+## Markdown elements supported in Layout Analysis
+
+The following Markdown elements are included in Layout API responses:
+
+* Paragraph
+* Heading
+* Table
+* Figure
+* Selection Mark
+* Formula
+* Barcode
+* PageNumber/PageHeader/PageFooter
+* PageBreak
+* KeyValuePairs/Language/Style
+* Spans and Content
+
+### Paragraph
+
+Paragraphs represent cohesive blocks of text that belong together semantically. The Layout API maintains paragraph integrity by:
+
+* Preserving paragraph boundaries with empty lines between separate paragraphs
+* Using line breaks within paragraphs to maintain the visual structure of the original document
+* Maintaining proper text flow that respects the original document's reading order
+
+Here's an example:
+
+``` md
+This is paragraph 1.
+This is still paragraph 1, even if in another Markdown line.
+
+This is paragraph 2. There is a blank line between paragraph 1 and paragraph 2.
+```
+---
+
+### Heading
+
+Headings organize document content into a hierarchical structure to make navigation and understanding easier. The Layout API has the following capabilities:
+
+* Uses standard Markdown heading syntax with 1-6 hash symbols (#) corresponding to heading levels.
+* Maintains proper spacing with two blank lines before each heading for improved readability.
+
+Here's an example:
+
+``` md
+# This is a title
+
+## This is heading 1
+
+### This is heading 2
+
+#### This is heading 3
+```
+
+---
+
+### Table
+
+Tables preserve complex structured data in a visually organized format. The Layout API uses HTML table syntax for maximum fidelity and compatibility:
+
+* Implements full HTML table markup (`<table>`, `<tr>`, `<th>`, `<td>`) rather than standard Markdown tables
+* Preserves merged cell with HTML rowspan and colspan attributes.
+* Preserves table captions with the `<caption>` tag to maintain document context
+* Handles complex table structures including headers, cells, and footers
+* Maintains proper spacing with two blank lines before each table for improved readability
+* Preserves table footnotes as separate paragraph following the table
+
+Here's an example:
+
+``` md
+<table>
+<caption>Table 1. This is a demo table</caption>
+<tr><th>Header</th><th>Header</th></tr>
+<tr><td>Cell</td><td>Cell</td></tr>
+<tr><td>Cell</td><td>Cell</td></tr>
+<tr><td>Cell</td><td>Cell</td></tr>
+<tr><td>Footer</td><td>Footer</td></tr>
+</table>
+This is the footnote of the table.
+```
+
+---
+
+### Figure
+
+The Layout API preserves figure elements:
+
+* Encapsulates figure content in `<figure>` tags to maintain semantic distinction from surrounding text
+* Preserves figure captions with the `<figcaption>` tag to provide important context
+* Preserves figure footnotes as separate paragraphs following the figure container
+
+Here's an example:
+
+``` md 
+<figure>
+<figcaption>Figure 2 This is a figure</figcaption>
+
+Values
+300
+200
+100
+0
+
+Jan Feb Mar Apr May Jun Months
+
+</figure>
+
+This is footnote if the figure have.
+```
+---
+
+### Selection Mark
+
+Selection marks represent checkbox-like elements in forms and documents. The Layout API:
+
+* Uses Unicode characters for visual clarity: ☒ (checked) and ☐ (unchecked)
+* Filters out low-confidence checkbox detections (below 0.1 confidence) to improve reliability
+* Maintains the semantic relationship between selection marks and their associated text
+
+
+### Formula
+
+Mathematical formulas are preserved with LaTeX-compatible syntax that allows for rendering of complex mathematical expressions:
+
+* Inline formulas are enclosed in single dollar signs (`$...$`) to maintain text flow
+* Block formulas use double dollar signs (`$$...$$`) for standalone display
+* Multi-line formulas are represented as consecutive block formulas, preserving mathematical relationships
+* Original spacing and formatting are maintained to ensure accurate representation
+
+Here's an example of inline formula, single-line formula block and multiple-lines formula block:
+
+``` md
+The mass-energy equivalence formula $E = m c ^ { 2 }$ is an example of an inline formula
+
+$$\frac { n ! } { k ! \left( n - k \right) ! } = \binom { n } { k }$$
+
+$$\frac { p _ { j } } { p _ { 1 } } = \prod _ { k = 1 } ^ { j - 1 } e ^ { - \beta _ { k , k + 1 } \Delta E _ { k , k + 1 } }$$
+$$= \exp \left[ - \sum _ { k = 1 } ^ { j - 1 } \beta _ { k , k + 1 } \Delta E _ { k , k + 1 } \right] .$$
+```
+---
+
+### Barcode
+
+Barcodes and QR codes are represented using Markdown image syntax with added semantic information:
+
+* Uses standard image Markdown syntax with descriptive attributes
+* Captures both the barcode type (QR code, barcode, etc.) and its encoded value
+* Preserves the semantic relationship between barcodes and surrounding content
+
+Here's an example:
+
+```
+![QRCode](barcodes/1.1 "https://www.microsoft.com")
+
+![UPCA](barcodes/1.2 "012345678905")
+ 
+![barcode type](barcodes/pagenumber.barcodenumber "barcode value/content")
+```
+---
+
+### PageNumber/PageHeader/PageFooter
+
+Page metadata elements provide context about document pagination but aren't meant to be displayed inline with the main content:
+
+* Enclosed in HTML comments to preserve the information while keeping it hidden from standard Markdown rendering
+* Maintains original page structure information that might be valuable for document reconstruction
+* Enables applications to understand document pagination without disrupting the content flow
+
+Here's an example:
+
+``` md
+<!-- PageHeader="This is page header" -->
+
+<!-- PageFooter="This is page footer" -->
+<!-- PageNumber="1" -->
+
+```
+---
+
+### PageBreak
+
+To easily figure out which parts belong to which page base on the pure Markdown content, we introduced PageBreak as the delimiter of the pages
+
+Here's an example:
+``` md
+<!-- PageBreak -->
+```
+---
+
+### KeyValuePairs/Language/Style
+
+For KeyValuePairs/Language/Style, we map them to  Analytics JSON body and not in the Markdown content.
+
+
+> [!NOTE]
+> For more information on Markdown that is currently supported for user content on GitHub.com, *see* [GitHub Flavored Markdown Spec](https://github.github.com/gfm).
+
+## Conclusion
+
+Document Intelligence's Markdown elements provide a powerful way to represent the structure and content of analyzed documents. By understanding and properly utilizing these Markdown elements, you can enhance your document processing workflows and build more sophisticated content extraction applications.
+
+## Next steps
+
+* Try processing your documents with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
+
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "マークダウン要素に関する新しい文書の追加"
}
```

### Explanation
この修正は、新たに「マークダウン要素」についての詳細なドキュメントを追加したものです。このドキュメントは、Azure AI Document IntelligenceのレイアウトAPIがサポートするマークダウン要素を説明しています。具体的には、APIを使用して文書をマークダウン形式で出力し、文書構造を保持したまま標準化されたコンテンツとして利用できることを強調しています。

ドキュメント内では、以下の要素がサポートされていることが説明されています：

- 段落
- 見出し
- テーブル
- 図
- 選択マーク
- 数式
- バーコード
- ページ番号 / ヘッダー / フッター
- ページ区切り
- キー・バリューペア / 言語 / スタイル

この追加されたドキュメントは、開発者が自分のアプリケーションでこの出力をどのように活用するかについてのガイダンスを提供し、より洗練された文書処理のワークフローを実現するための手助けとなることを目的としています。また、事例を交えながらこれらのマークダウン要素の具体的な使用方法や書式設定も含まれています。

## articles/ai-services/document-intelligence/prebuilt/layout.md{#item-f7c4c8}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 04/23/2025
+ms.date: 05/05/2025
 ms.author: lajanuar
 ---
 
@@ -405,7 +405,7 @@ The Layout API can output the extracted text in markdown format. Use the `output
 
 > [!NOTE]
 >
-> For v4.0 `2024-11-30` (GA), the representation of tables is changed to HTML tables to enable rendering of merged cells, multi-row headers, etc. Another related change is to use Unicode checkbox characters ☒ and ☐ for selection marks instead of `:selected:` and `:unselected:`. This update means that the content of selection mark fields contains `:selected:` even though their spans refer to Unicode characters in the top-level span.
+> For v4.0 `2024-11-30` (GA), the representation of tables is changed to HTML tables to enable rendering of merged cells, multi-row headers, etc. Another related change is to use Unicode checkbox characters ☒ and ☐ for selection marks instead of `:selected:` and `:unselected:`. This update means that the content of selection mark fields contains `:selected:` even though their spans refer to Unicode characters in the top-level span. Refer to the [Markdown Output Format](../concept/markdown-elements.md) for full definition of Markdown elements.
 
 #### [Sample code](#tab/sample-code)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レイアウトAPIに関するドキュメントの日付更新と注釈追加"
}
```

### Explanation
この修正は、「レイアウトAPI」に関するドキュメントの一部を更新したもので、主に次の2つの変更が行われました：

1. ドキュメントの日付が「2025年4月23日」から「2025年5月5日」に更新されました。
2. 注釈の内容が小幅に変更され、Markdown要素の完全な定義への参照が追加されました。

具体的には、テーブルの表現がHTMLテーブルに変更されたことや、選択マークに関するUnicodeキャラクターの使用についての情報が引き続き提供されています。この更新により、Markdown出力形式の完全な理解を促進するためのリンクが追加され、開発者がAPIをより効果的に利用できるように設計されています。全体として、この変更はドキュメントの内容を最新のものにし、ユーザーにとっての有用性を向上させることを目的としています。

## articles/ai-services/document-intelligence/toc.yml{#item-81aa7b}

<details>
<summary>Diff</summary>
````diff
@@ -153,6 +153,9 @@ items:
   - name: Analyze document API response
     displayName: words, lines, pages, bounding regions, documents
     href: concept/analyze-document-response.md
+  - name: Layout API markdown output elements
+    displayName: words, lines, pages, bounding regions, documents
+    href: concept/markdown-elements.md
   - name: Retrieval-Augmented Generation (RAG)
     displayName: RAG, LLM, semantic, chunk, LangChain, language model
     href: concept/retrieval-augmented-generation.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次にマークダウン出力要素に関する項目を追加"
}
```

### Explanation
この修正は、ドキュメントの目次ファイル「toc.yml」に新しいエントリーを追加したもので、具体的には「レイアウトAPIのマークダウン出力要素」に関する項目が追加されました。この変更により、ユーザーは新しいトピックにアクセスできるようになり、関連するマークダウン要素の詳細を簡単に見つけられるようになります。

追加された項目は以下の通りです：

- **名前**: Layout API markdown output elements
- **表示名**: words, lines, pages, bounding regions, documents
- **リンク**: concept/markdown-elements.md

この更新により、ドキュメント全体の構造が強化され、ユーザーが関連情報に容易にアクセスできるようになります。全体として、この変更は文書の可読性とナビゲーションの利便性を向上させることを目指しています。

## articles/ai-services/language-service/summarization/how-to/text-summarization.md{#item-8a6034}

<details>
<summary>Diff</summary>
````diff
@@ -295,7 +295,7 @@ curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/
       "kind": "AbstractiveSummarization",
       "taskName": "Length controlled Abstractive Summarization",
           "parameters": {
-          "sentenceLength": "short"
+          "summaryLength": "short"
       }
     }
   ]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "要約APIのパラメータ名を変更"
}
```

### Explanation
この修正は、「テキスト要約」に関するドキュメントである「text-summarization.md」において、要約APIのパラメータ名を変更したものです。変更内容は次の通りです：

- パラメータ名が「sentenceLength」から「summaryLength」に変更されました。この変更により、APIの使い方をより明確にし、要約の長さに関する意図がはっきりと伝わるようになります。

具体的には、cURLリクエストの一部である「parameters」セクションにおいて、このパラメータが利用されています。この修正は、APIユーザーが期待した要約の長さを指定する際の混乱を避けるために重要です。全体として、この修正はAPIドキュメントの正確性と明瞭性を向上させる目的があります。


