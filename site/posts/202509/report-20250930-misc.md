---
date: '2025-09-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:36bd0d1...MicrosoftDocs:9fffe4d
summary: このコードの変更には、AIサービスの文書に関する複数のマイナーなアップデートが含まれていますが、特に以下の点が重要です。受取書モデル文書の日付が更新され、サポートされている受取書タイプのリストが削除されました。また、Power
  BIとの統合チュートリアルでは、文中の言い回しがより直訳的に修正されました。個人情報に関する入力ガイドラインでは、PDFのサポートが拡張され、リクエストあたりの文書総数の制限が引き上げられています。新機能の追加はありませんが、既存の文書が最新の内容に更新されています。破壊的な変更は見受けられませんが、受取書のサポートタイプのリスト削除が利用者に影響を与える可能性があります。全体として、これらの変更は文書の内容を最新に保ち、サービス利用時の混乱を最小限に抑えることを目指しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:36bd0d1...MicrosoftDocs:9fffe4d){target="_blank"}

# ハイライト
このコードの変更には、AIサービスの文書における複数のマイナーなアップデートが含まれていますが、代表的には以下の点が強調されています:
- 受取書モデル文書の日付が更新され、サポートされている受取書タイプのリストが削除されています。
- Power BIとの統合チュートリアルで、文中の言い回しがより直訳的に修正されています。
- 個人情報（PII）に関する入力ガイドラインで、PDFのサポートが拡張され、リクエストあたりの文書総数の制限が引き上げられています。

## 新機能
特に新機能の追加はありませんが、既存の文書が最新の内容に更新されています。

## 破壊的変更
破壊的な変更は見受けられませんが、受取書のサポートタイプのリスト削除が利用者へ影響を与える可能性があります。

## その他の更新
- 文書の日付の更新
- 言い回しや説明の明確化による読者理解の向上

# インサイト
この一連の変更は、文書の内容を最新の状態に保ち、利用者がサービスを利用する際の混乱を最小限に抑えることを目的としています。まず、受取書の文書における日付の更新とサポートされているタイプのリスト削除は、文書の簡素化と現状に則した内容への更新を図ったものです。これにより、受取書のモデル利用者がより効果的に機能を把握しやすくなります。

Power BIとの統合チュートリアルでは、テキスト表現がより具体的かつ直訳的になるように調整が加えられています。これは、特に英語を第二言語として学ぶ読者や、直感的にチュートリアルを理解したい読者にとって有益です。

最後に、PIIに関する入力ガイドラインの更新は、ファイル形式サポートを明確にしながら、ユーザーの可能な操作範囲を拡大するものです。PDFに関する説明が一般化され、スキャンしたPDFも明確にサポートされていると記載されたことで、より多様な文書の処理が可能になります。また、リクエストあたりの文書数制限の引き上げは、利用者にとってより効率的な運用が期待できます。これらの更新は全体として、サービスの利用体験向上を目指した内容と言えます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [receipt.md](#item-089054) | minor update | 受取書に関する文書の更新 | modified | 2 | 15 | 17 | 
| [integrate-power-bi.md](#item-20f71f) | minor update | Power BIとの統合チュートリアルの更新 | modified | 21 | 21 | 42 | 
| [redact-document-pii.md](#item-5509ee) | minor update | 文書に関する入力ガイドラインの更新 | modified | 2 | 3 | 5 | 


# Modified Contents
## articles/ai-services/document-intelligence/prebuilt/receipt.md{#item-089054}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 11/19/2024
+ms.date: 09/29/2025
 ms.author: lajanuar
 ---
 
@@ -30,20 +30,7 @@ ms.author: lajanuar
 [!INCLUDE [applies to v2.1](../includes/applies-to-v21.md)]
 ::: moniker-end
 
-The Document Intelligence receipt model combines powerful Optical Character Recognition (OCR) capabilities with deep learning models to analyze and extract key information from sales receipts. Receipts can be of various formats and quality including printed and handwritten receipts. The API extracts key information such as merchant name, merchant phone number, transaction date, tax, and transaction total and returns structured JSON data. Receipt model v4.0 (GA) supports other fields including `ReceiptType`, `TaxDetails.NetAmount`, `TaxDetails.Description`, `TaxDetails.Rate` and `CountryRegion` along with VAT table extraction on general hotel receipts. VAT table extraction support for Nordic Receipts will be added in March 2025. 
-
-**Supported receipt types in the latest version (4.0):**
-
-* Meal
-* Supplies
-* Hotel
-* Fuel&Energy
-* Transportation
-* Communication
-* Subscriptions
-* Entertainment
-* Training
-* Healthcare 
+The Document Intelligence receipt model combines powerful Optical Character Recognition (OCR) capabilities with deep learning models to analyze and extract key information from sales receipts. Receipts can be of various formats and quality including printed and handwritten receipts. The API extracts key information such as merchant name, merchant phone number, transaction date, tax, and transaction total and returns structured JSON data. Receipt model v4.0 (GA) supports other fields including `ReceiptType`, `TaxDetails.NetAmount`, `TaxDetails.Description`, `TaxDetails.Rate` and `CountryRegion` along with VAT table extraction on general hotel receipts. 
 
 ## Receipt data extraction
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "受取書に関する文書の更新"
}
```

### Explanation
このコードの変更は、受取書モデルに関する文書の更新を反映しています。主な変更点は、文書の日付の更新と受取書のサポートされているタイプのリストが削除されたことです。新しい日付は2025年9月29日に設定され、以前の日付である2024年11月19日は削除されました。また、サポートされている受取書のタイプの詳細が削除され、より簡潔な説明に改訂されました。この修正は、受取書モデルの特徴を強調しながら、文書をよりアップデートされた状態に保つことを目的としています。

## articles/ai-services/language-service/key-phrase-extraction/tutorials/integrate-power-bi.md{#item-20f71f}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: tutorial
-ms.date: 06/04/2025
+ms.date: 09/29/2025
 ms.author: lajanuar
 ms.custom:
   - language-service-key-phrase
@@ -18,7 +18,7 @@ ms.custom:
 
 Microsoft Power BI Desktop is a free application that lets you connect to, transform, and visualize your data. Key phrase extraction, one of the features of Azure AI Language, provides natural language processing. Given raw unstructured text, it can extract the most important phrases, analyze sentiment, and identify well-known entities such as brands. Together, these tools can help you quickly see what your customers are talking about and how they feel about it.
 
-In this tutorial, you'll learn how to:
+In this tutorial, you learn how to:
 
 > [!div class="checklist"]
 > * Use Power BI Desktop to import and transform data
@@ -40,7 +40,7 @@ In this tutorial, you'll learn how to:
 To get started, open Power BI Desktop and load the comma-separated value (CSV) file that you downloaded as part of the [prerequisites](#prerequisites). This file represents a day's worth of hypothetical activity in a fictional small company's support forum.
 
 > [!NOTE]
-> Power BI can use data from a wide variety of web-based sources, such as SQL databases. See the [Power Query documentation](/power-query/connectors/) for more information.
+> Power BI can use data from a wide variety of web-based sources, such as SQL databases. For more information, *see* [Power Query documentation](/power-query/connectors/).
 
 In the main Power BI Desktop window, select the **Home** ribbon. In the **External data** group of the ribbon, open the **Get Data** drop-down menu and select **Text/CSV**.
 
@@ -50,15 +50,15 @@ The Open dialog appears. Navigate to your Downloads folder, or to the folder whe
 
 ![The CSV Import dialog](../media/tutorials/power-bi/csv-import.png)
 
-The CSV import dialog lets you verify that Power BI Desktop has correctly detected the character set, delimiter, header rows, and column types. This information is all correct, so select **Load**.
+The CSV import dialog lets you verify that Power BI Desktop correctly detected the character set, delimiter, header rows, and column types. This information is all correct, so select **Load**.
 
-To see the loaded data, click the **Data View** button on the left edge of the Power BI workspace. A table opens that contains the data, like in Microsoft Excel.
+To see the loaded data, select the **Data View** button on the left edge of the Power BI workspace. A table opens that contains the data, like in Microsoft Excel.
 
 ![The initial view of the imported data](../media/tutorials/power-bi/initial-data-view.png)
 
 ## Prepare the data
 
-You might need to transform your data in Power BI Desktop before it's ready to be processed by Key Phrase Extraction.
+You might need to transform your data in Power BI Desktop before Key Phrase Extraction processing.
 
 The sample data contains a `subject` column and a `comment` column. With the Merge Columns function in Power BI Desktop, you can extract key phrases from the data in both these columns, rather than just the `comment` column.
 
@@ -68,7 +68,7 @@ In Power BI Desktop, select the **Home** ribbon. In the **External data** group,
 
 Select `FabrikamComments` in the **Queries** list at the left side of the window if it isn't already selected.
 
-Now select both the `subject` and `comment` columns in the table. You might need to scroll horizontally to see these columns. First click the `subject` column header, then hold down the Control key and click the `comment` column header.
+Now select both the `subject` and `comment` columns in the table. You might need to scroll horizontally to see these columns. First select the `subject` column header, then hold down the Control key and select the `comment` column header.
 
 ![Selecting fields to be merged](../media/tutorials/power-bi/select-columns.png)
 
@@ -82,7 +82,7 @@ You might also consider filtering out blank messages using the Remove Empty filt
 
 ## Understand the API
 
-[Key Phrase Extraction](https://westus.dev.cognitive.microsoft.com/docs/services/TextAnalytics-V3-1/operations/KeyPhrases) can process up to a thousand text documents per HTTP request. Power BI prefers to deal with records one at a time, so in this tutorial your calls to the API will include only a single document each. The Key Phrases API requires the following fields for each document being processed.
+[Key Phrase Extraction](/rest/api/language/text-analysis-runtime/analyze-text?view=rest-language-2024-11-01&preserve-view=true&tabs=HTTP#analyzetextkeyphraseextractioninput) can process up to a thousand text documents per HTTP request. Power BI prefers to deal with records one at a time, so in this tutorial your calls to the API include only a single document each. The Key Phrases API requires the following fields for each document being processed.
 
 | Field | Description |
 | - | - |
@@ -92,10 +92,10 @@ You might also consider filtering out blank messages using the Remove Empty filt
 
 ## Create a custom function
 
-Now you're ready to create the custom function that will integrate Power BI and Key Phrase Extraction. The function receives the text to be processed as a parameter. It converts data to and from the required JSON format and makes the HTTP request to the Key Phrases API. The function then parses the response from the API and returns a string that contains a comma-separated list of the extracted key phrases.
+Now you're ready to create the custom function that integrates Power BI and Key Phrase Extraction. The function receives the text to be processed as a parameter. It converts data to and from the required JSON format and makes the HTTP request to the Key Phrases API. The function then parses the response from the API and returns a string that contains a comma-separated list of the extracted key phrases.
 
 > [!NOTE]
-> Power BI Desktop custom functions are written in the [Power Query M formula language](/powerquery-m/power-query-m-reference), or just "M" for short. M is a functional programming language based on [F#](/dotnet/fsharp/). You don't need to be a programmer to finish this tutorial, though; the required code is included below.
+> Power BI Desktop custom functions are written in the [Power Query M formula language](/powerquery-m/power-query-m-reference), or just "M" for short. M is a functional programming language based on [F#](/dotnet/fsharp/). You don't need to be a programmer to finish this tutorial, though; the required code is included.
 
 In Power BI Desktop, make sure you're still in the Query Editor window. If you aren't, select the **Home** ribbon, and in the **External data** group, select **Edit Queries**.
 
@@ -106,7 +106,7 @@ A new query, initially named `Query1`, appears in the Queries list. Double-click
 Now, in the **Home** ribbon, in the **Query** group, select **Advanced Editor** to open the Advanced Editor window. Delete the code that's already in that window and paste in the following code. 
 
 > [!NOTE]
-> Replace the example endpoint below (containing `<your-custom-subdomain>`) with the endpoint generated for your Language resource. You can find this endpoint by signing in to the [Azure portal](https://azure.microsoft.com/features/azure-portal/), navigating to your resource, and selecting **Key and endpoint**.
+> Replace the following example endpoint (containing `<your-custom-subdomain>`) with the endpoint generated for your Language resource. You can find this endpoint by signing in to the [Azure portal](https://azure.microsoft.com/features/azure-portal/), navigating to your resource, and selecting **Key and endpoint**.
 
 
 ```fsharp
@@ -153,12 +153,12 @@ After you close the Invoke Custom Function dialog, a banner may appear asking yo
 Select **Edit Credentials,** make sure `Anonymous` is selected in the dialog, then select **Connect.** 
 
 > [!NOTE]
-> You select `Anonymous` because Key Phrase Extraction authenticates requests using your access key, so Power BI does not need to provide credentials for the HTTP request itself.
+> You select `Anonymous` because Key Phrase Extraction authenticates requests using your access key, so Power BI doesn't need to provide credentials for the HTTP request itself.
 
 > [!div class="mx-imgBorder"]
 > ![setting authentication to anonymous](../media/tutorials/power-bi/access-web-content.png)
 
-If you see the Edit Credentials banner even after choosing anonymous access, you might have forgotten to paste your Language resource key into the code in the `KeyPhrases` [custom function](#create-a-custom-function).
+If you see the Edit Credentials banner even after choosing anonymous access, you check to see if you pasted your Language resource key into the code in the `KeyPhrases` [custom function](#create-a-custom-function).
 
 Next, a banner may appear asking you to provide information about your data sources' privacy. 
 
@@ -170,20 +170,20 @@ Select **Continue** and choose `Public` for each of the data sources in the dial
 
 ## Create the word cloud
 
-Once you have dealt with any banners that appear, select **Close & Apply** in the Home ribbon to close the Query Editor.
+Once you address with any banners that appear, select **Close & Apply** in the Home ribbon to close the Query Editor.
 
 Power BI Desktop takes a moment to make the necessary HTTP requests. For each row in the table, the new `keyphrases` column contains the key phrases detected in the text by the Key Phrases API. 
 
-Now you'll use this column to generate a word cloud. To get started, click the **Report** button in the main Power BI Desktop window, to the left of the workspace.
+Now you use this column to generate a word cloud. To get started, select the **Report** button in the main Power BI Desktop window, to the left of the workspace.
 
 > [!NOTE]
-> Why use extracted key phrases to generate a word cloud, rather than the full text of every comment? The key phrases provide us with the *important* words from our customer comments, not just the *most common* words. Also, word sizing in the resulting cloud isn't skewed by the frequent use of a word in a relatively small number of comments.
+> Why use extracted key phrases to generate a word cloud, rather than the full text of every comment? The key phrases provide us with the *important* words from our customer comments, not just the *most common* words. Also, word sizing in the resulting cloud doesn't correlate to the frequent use of a word in a relatively small number of comments.
 
-If you don't already have the Word Cloud custom visual installed, install it. In the Visualizations panel to the right of the workspace, click the three dots (**...**) and choose **Import From Market**. If the word "cloud" is not among the displayed visualization tools in the list, you can search for "cloud" and click the **Add** button next the Word Cloud visual. Power BI installs the Word Cloud visual and lets you know that it installed successfully.
+If you don't already have the Word Cloud custom visual installed, install it. In the Visualizations panel to the right of the workspace, select the three dots (**...**) and choose **Import From Market**. If the word "cloud" isn't among the displayed visualization tools in the list, you can search for "cloud" and select the **Add** button next the Word Cloud visual. Power BI installs the Word Cloud visual and lets you know that it installed successfully.
 
 ![adding a custom visual](../media/tutorials/power-bi/add-custom-visuals.png)<br><br>
 
-First, click the Word Cloud icon in the Visualizations panel.
+First, select the Word Cloud icon in the Visualizations panel.
 
 ![Word Cloud icon in visualizations panel](../media/tutorials/power-bi/visualizations-panel.png)
 
@@ -193,19 +193,19 @@ Now switch to the Format page of the Visualizations panel. In the Stop Words cat
 
 ![activating default stop words](../media/tutorials/power-bi/default-stop-words.png)
 
-Down a little further in this panel, turn off **Rotate Text** and **Title**.
+Scroll down the panel and turn off **Rotate Text** and **Title**.
 
 ![activate focus mode](../media/tutorials/power-bi/word-cloud-focus-mode.png)
 
-Select the Focus Mode tool in the report to get a better look at our word cloud. The tool expands the word cloud to fill the entire workspace, as shown below.
+Select the Focus Mode tool in the report to get a better look at our word cloud. The tool expands the word cloud to fill the entire workspace.
 
 ![A Word Cloud](../media/tutorials/power-bi/word-cloud.png)
 
 ## Using other features
 
 Azure AI Language also provides sentiment analysis and language detection. The language detection in particular is useful if your customer feedback isn't all in English.
 
-Both of these other APIs are similar to the Key Phrases API. That means you can integrate them with Power BI Desktop using custom functions that are nearly identical to the one you created in this tutorial. Just create a blank query and paste the appropriate code below into the Advanced Editor, as you did earlier. (Don't forget your access key!) Then, as before, use the function to add a new column to the table.
+Both of these other APIs are similar to the Key Phrases API. That means you can integrate them with Power BI Desktop using custom functions that are nearly identical to the one you created in this tutorial. Just create a blank query and paste the appropriate code into the Advanced Editor, as you did earlier. (Don't forget your access key!) Then, as before, use the function to add a new column to the table.
 
 The Sentiment Analysis function below returns a label indicating how positive the sentiment expressed in the text is.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Power BIとの統合チュートリアルの更新"
}
```

### Explanation
このコードの変更は、Power BIとの統合に関するチュートリアルの文書を更新しています。主な修正点は、文書の日付が2025年6月4日から2025年9月29日に変更されたことと、文中の言い回しがいくつか修正されたことです。また、文章の明確さを高めるために、一部の文が再構成され、より具体的な表現が使用されています。例えば、「In this tutorial, you’ll learn how to」という文が「In this tutorial, you learn how to」に変更され、より直訳的・能動的な表現になっています。これらの変更は、読者にとっての理解を深め、チュートリアルの内容を最新のものにすることを目的としています。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-document-pii.md{#item-5509ee}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ A native document refers to the file format used to create the original document
 |File type|File extension|Description|
 |---------|--------------|-----------|
 |Text| `.txt`|An unformatted text document.|
-|Adobe PDF| `.pdf`|A portable document file formatted document.|
+|PDF| `.pdf`|A portable document file formatted document and scanned PDFs.|
 |Microsoft Word| `.docx`|A Microsoft Word document file.|
 
 ## Input guidelines
@@ -42,15 +42,14 @@ A native document refers to the file format used to create the original document
 
 |Type|support and limitations|
 |---|---|
-|**PDFs**| Fully scanned PDFs aren't supported.|
 |**Text within images**| Digital images with embedded text aren't supported.|
 |**Digital tables**| Tables in scanned documents aren't supported.|
 
 ***Document Size***
 
 |Attribute|Input limit|
 |---|---|
-|**Total number of documents per request** |**≤ 20**|
+|**Total number of documents per request** |**≤ 40**|
 |**Total content size per request**| **≤ 10 MB**|
 
 ## Include native documents with an HTTP request
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書に関する入力ガイドラインの更新"
}
```

### Explanation
このコードの変更は、個人情報 (PII) の文書を赤外線処理する方法に関するガイドラインの更新を反映しています。主な変更点は、PDFの説明が「Adobe PDF」から「PDF」に変更され、スキャンしたPDFもサポートされることが明確に示されたことです。また、リクエストあたりの文書総数の制限が「20」から「40」に引き上げられました。この修正は、ユーザーがサポートされているファイル形式や制限を理解しやすくするためのもので、文書の処理要件を最新のものに保つことを目的としています。


