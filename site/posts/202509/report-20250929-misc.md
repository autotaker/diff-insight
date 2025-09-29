---
date: '2025-09-29'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:24ed2ed...MicrosoftDocs:36bd0d1
summary: このコードの変更は、主にドキュメントの日付更新と表現の微細な修正を行い、Azure AI Languageサービスのドキュメントを最新の情報に保ち、読みやすさと一貫性を向上させることを目的としています。新機能の追加や重大な変更はありませんが、ユーザーがより使いやすく感じられるよう改善されています。具体的には、ドキュメントの日付更新、テキストの一貫性向上、リストやテーブルのフォーマット調整が行われています。これにより、情報の信頼性とユーザーエクスペリエンスが向上します。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:24ed2ed...MicrosoftDocs:36bd0d1){target="_blank"}

# ハイライト
このコードの変更は、主にドキュメントの日付更新と微細な文言修正を行ったものです。これによって、Azure AI Languageサービスのドキュメントは最新の情報を反映し、読みやすさと一貫性が向上しました。新機能や重大な破壊的変更は特にありませんが、ユーザーにとっての使いやすさが改善されています。  

## 新機能

- 特に新機能の追加はありません。

## 重大な変更

- 重大な破壊的変更はありません。

## その他の更新

- ドキュメントの日付が最新のものに更新されました。
- テキストの表現が修正され、一貫性と読みやすさが向上しました。
- リストやテーブルのフォーマットが調整されました。
- セクションタイトルの細かい調整が行われました。

# 洞察
このコード変更は、ドキュメントの最新化とわかりやすさの向上に焦点を当てた更新です。特に、`ms.date`フィールドの更新によって、ドキュメントが最新の情報を含んでいることが明確に示されています。このような日付更新は、ドキュメントの信頼性を高め、ユーザーが最新の情報に基づいて作業や意思決定を行うのを助けます。  

また、テキストの修正は、誤解を避けるためのものであり、特定の用語の一貫性を保つことが目的とされています。たとえば、「pre-defined」から「predefined」への変更は、ドキュメント全体で用語を統一することによって混乱を減らします。同様に、リストやテーブルのフォーマット変更は、視覚的な明瞭さを提供し、内容をよりすばやく理解できるようにしています。

このような微細な更新にも関わらず、文書全体の品質を着実に向上させることを目的とした変更は、結果としてユーザーエクスペリエンスを向上させる重要なステップです。技術文書においては、常に最新で正確な情報を提供することが信頼性を維持する鍵となります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [overview.md](#item-ebc28d) | minor update | カスタムテキスト分類の概要の更新 | modified | 16 | 16 | 32 | 
| [index.yml](#item-c9444f) | minor update | 言語サービスのインデックスファイルの更新 | modified | 2 | 2 | 4 | 
| [quickstart.md](#item-636553) | minor update | 言語検出のクイックスタートガイドの日付更新 | modified | 1 | 1 | 2 | 
| [extract-excel-information.md](#item-96502c) | minor update | Excel情報抽出チュートリアルの更新 | modified | 20 | 20 | 40 | 
| [managed-identities.md](#item-ddd66a) | minor update | マネージドアイデンティティに関する日付更新 | modified | 1 | 1 | 2 | 
| [shared-access-signatures.md](#item-01eef1) | minor update | SASトークンに関する日付更新とセクションタイトルの変更 | modified | 2 | 2 | 4 | 
| [redact-conversation-pii.md](#item-0d6332) | minor update | 会話の個人情報の編集に関する日付更新 | modified | 1 | 1 | 2 | 
| [redact-document-pii.md](#item-5509ee) | minor update | ドキュメントの個人情報の編集に関する日付更新 | modified | 1 | 1 | 2 | 
| [redact-text-pii.md](#item-9e48af) | minor update | テキストにおける個人情報の編集に関する文書の更新 | modified | 9 | 9 | 18 | 
| [quickstart.md](#item-8c5758) | minor update | クイックスタートガイドの日付更新 | modified | 1 | 1 | 2 | 
| [conversation-summarization.md](#item-9ff946) | minor update | 会話要約ガイドの日付更新 | modified | 1 | 1 | 2 | 
| [text-summarization.md](#item-8a6034) | minor update | テキスト要約ガイドの内容修正 | modified | 8 | 8 | 16 | 
| [overview.md](#item-844139) | minor update | 要約機能の概要更新 | modified | 6 | 6 | 12 | 


# Modified Contents
## articles/ai-services/language-service/custom-text-classification/overview.md{#item-ebc28d}

<details>
<summary>Diff</summary>
````diff
@@ -7,21 +7,21 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 03/24/2025
+ms.date: 09/27/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification
 ---
 
 # What is custom text classification?
 
-Custom text classification is one of the custom features offered by [Azure AI Language](../overview.md). It is a cloud-based API service that applies machine-learning intelligence to enable you to build custom models for text classification tasks. 
+Custom text classification is one of the custom features offered by [Azure AI Language](../overview.md). It's a cloud-based API service that applies machine-learning intelligence to enable you to build custom models for text classification tasks. 
 
-Custom text classification enables users to build custom AI models to classify text into custom classes pre-defined by the user. By creating a custom text classification project, developers can iteratively label data, train, evaluate, and improve model performance before making it available for consumption. The quality of the labeled data greatly impacts model performance. To simplify building and customizing your model, the service offers a custom web portal that can be accessed through the [Language studio](https://aka.ms/languageStudio). You can easily get started with the service by following the steps in this [quickstart](quickstart.md). 
+Custom text classification enables users to build custom AI models to classify text into custom classes predefined by the user. By creating a custom text classification project, developers can iteratively label data, train, evaluate, and improve model performance before making it available for consumption. The quality of the labeled data greatly impacts model performance. To simplify building and customizing your model, the service offers a custom web portal that can be accessed through the [Language studio](https://aka.ms/languageStudio). You can easily get started with the service by following the steps in this [quickstart](quickstart.md). 
 
 Custom text classification supports two types of projects: 
 
-* **Single label classification** - you can assign a single class for each document in your dataset. For example, a movie script could only be classified as "Romance" or "Comedy". 
-* **Multi label classification** - you can assign multiple classes for each document in your dataset. For example, a movie script could be classified as "Comedy" or "Romance" and "Comedy".
+* **Single label classification** - you can assign a single class for each document in your dataset. For example, a movie script could only be classified as "Romance" or "Comedy."
+* **Multi label classification** - you can assign multiple classes for each document in your dataset. For example, a movie script could be classified as "Comedy" or "Romance" and "Comedy."
 
 This documentation contains the following article types:
 
@@ -31,11 +31,11 @@ This documentation contains the following article types:
 
 ## Example usage scenarios
 
-Custom text classification can be used in multiple scenarios across a variety of industries:
+Custom text classification can be used in multiple scenarios across various industries:
 
 ### Automatic emails or ticket triage
 
-Support centers of all types receive a high volume of emails or tickets containing unstructured, freeform text and attachments. Timely review, acknowledgment, and routing to subject matter experts within internal teams is critical. Email triage at this scale requires people to review and route to the right departments, which takes time and resources. Custom text classification can be used to analyze incoming text, and triage and categorize the content to be automatically routed to the relevant departments for further action.
+Support centers of all types receive a high volume of emails or tickets containing unstructured, freeform text, and attachments. Timely review, acknowledgment, and routing to subject matter experts within internal teams is critical. Email triage at this scale requires people to review and route to the right departments, which takes time and resources. Custom text classification can be used to analyze incoming text, and triage and categorize the content to be automatically routed to the relevant departments for further action.
 
 ### Knowledge mining to enhance/enrich semantic search
 
@@ -65,18 +65,18 @@ Follow these steps to get the most out of your model:
 
 As you use custom text classification, see the following reference documentation and samples for Azure AI Language:
 
-|Development option / language  |Reference documentation |Samples  |
-|---------|---------|---------|
-|REST APIs (Authoring)   | [REST API documentation](https://aka.ms/ct-authoring-swagger)        |         |
-|REST APIs (Runtime)    | [REST API documentation](https://aka.ms/ct-runtime-swagger)        |         |
-|C#  (Runtime)   | [C# documentation](/dotnet/api/azure.ai.textanalytics?view=azure-dotnet-preview&preserve-view=true)        | [C# samples - Single label classification](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/textanalytics/Azure.AI.TextAnalytics/samples/Sample9_SingleLabelClassify.md) [C# samples - Multi label classification](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/textanalytics/Azure.AI.TextAnalytics/samples/Sample10_MultiLabelClassify.md)       |
-| Java   (Runtime)  | [Java documentation](/java/api/overview/azure/ai-textanalytics-readme?view=azure-java-preview&preserve-view=true)        | [Java Samples - Single label classification](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/textanalytics/azure-ai-textanalytics/src/samples/java/com/azure/ai/textanalytics/lro/SingleLabelClassifyDocument.java) [Java Samples - Multi label classification](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/textanalytics/azure-ai-textanalytics/src/samples/java/com/azure/ai/textanalytics/lro/MultiLabelClassifyDocument.java) |
-|JavaScript (Runtime)     | [JavaScript documentation](/javascript/api/overview/azure/ai-text-analytics-readme?view=azure-node-preview&preserve-view=true)        | [JavaScript samples - Single label classification](https://github.com/Azure/azure-sdk-for-js/blob/%40azure/ai-text-analytics_6.0.0-beta.1/sdk/textanalytics/ai-text-analytics/samples/v5/javascript/customText.js) [JavaScript samples - Multi label classification](https://github.com/Azure/azure-sdk-for-js/blob/%40azure/ai-text-analytics_6.0.0-beta.1/sdk/textanalytics/ai-text-analytics/samples/v5/javascript/customText.js) |
-|Python (Runtime)| [Python documentation](/python/api/azure-ai-textanalytics/azure.ai.textanalytics?view=azure-python-preview&preserve-view=true)        | [Python samples - Single label classification](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/textanalytics/azure-ai-textanalytics/samples/sample_single_label_classify.py) [Python samples - Multi label classification](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/textanalytics/azure-ai-textanalytics/samples/sample_multi_label_classify.py) |
+| Development option / language | Reference documentation | Samples |
+|--|--|--|
+| REST APIs (Authoring) | [REST API documentation](https://aka.ms/ct-authoring-swagger) |  |
+| REST APIs (Runtime) | [REST API documentation](https://aka.ms/ct-runtime-swagger) |  |
+| C#  (Runtime) | [C# documentation](/dotnet/api/azure.ai.textanalytics?view=azure-dotnet-preview&preserve-view=true) | [C# samples - Single label classification](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/textanalytics/Azure.AI.TextAnalytics/samples/Sample9_SingleLabelClassify.md) [C# samples - Multi label classification](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/textanalytics/Azure.AI.TextAnalytics/samples/Sample10_MultiLabelClassify.md) |
+| Java   (Runtime) | [Java documentation](/java/api/overview/azure/ai-textanalytics-readme?view=azure-java-preview&preserve-view=true) | [Java Samples - Single label classification](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/textanalytics/azure-ai-textanalytics/src/samples/java/com/azure/ai/textanalytics/lro/SingleLabelClassifyDocument.java) [Java Samples - Multi label classification](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/textanalytics/azure-ai-textanalytics/src/samples/java/com/azure/ai/textanalytics/lro/MultiLabelClassifyDocument.java) |
+| JavaScript (Runtime) | [JavaScript documentation](/javascript/api/overview/azure/ai-text-analytics-readme?view=azure-node-preview&preserve-view=true) | [JavaScript samples - Single label classification](https://github.com/Azure/azure-sdk-for-js/blob/%40azure/ai-text-analytics_6.0.0-beta.1/sdk/textanalytics/ai-text-analytics/samples/v5/javascript/customText.js) [JavaScript samples - Multi label classification](https://github.com/Azure/azure-sdk-for-js/blob/%40azure/ai-text-analytics_6.0.0-beta.1/sdk/textanalytics/ai-text-analytics/samples/v5/javascript/customText.js) |
+| Python (Runtime) | [Python documentation](/python/api/azure-ai-textanalytics/azure.ai.textanalytics?view=azure-python-preview&preserve-view=true) | [Python samples - Single label classification](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/textanalytics/azure-ai-textanalytics/samples/sample_single_label_classify.py) [Python samples - Multi label classification](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/textanalytics/azure-ai-textanalytics/samples/sample_multi_label_classify.py) |
 
 ## Responsible AI 
 
-An AI system includes not only the technology, but also the people who will use it, the people who will be affected by it, and the environment in which it is deployed. Read the [transparency note for custom text classification](/azure/ai-foundry/responsible-ai/language-service/custom-text-classification-transparency-note) to learn about responsible AI use and deployment in your systems. 
+An AI system includes not only the technology, but also the people who use it, the people affected by it, and the deployment environment. Read the [transparency note for custom text classification](/azure/ai-foundry/responsible-ai/language-service/custom-text-classification-transparency-note) to learn about responsible AI use and deployment in your systems. 
 
 [!INCLUDE [Responsible AI links](../includes/overview-responsible-ai-links.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムテキスト分類の概要の更新"
}
```

### Explanation
このコードの変更は、Azure AI Languageのカスタムテキスト分類に関する「overview.md」ファイルの一部を更新したものです。主に日付の修正や、テキストの明確さを向上させるための微細な言い回しの調整が含まれています。具体的には、次の点が変更されました：

1. **日付の更新**: 最後に更新された日付が「03/24/2025」から「09/27/2025」に変更されました。
2. **テキストの改善**: 一部の文の構成や選ばれた単語が修正され、読みやすさが向上しています。例えば、「pre-defined」から「predefined」への変更などが見られます。
3. **リスト形式の統一**: リスト形式の表現において、一部文末にある句読点が追加されたり削除されるなど、形式がより一貫したものになっています。

全体として、これらの変更はドキュメントの明瞭さと正確性を高め、ユーザーにとって使いやすい資料を提供するためのものです。

## articles/ai-services/language-service/index.yml{#item-c9444f}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ metadata:
   manager: nitinme
   ms.service: azure-ai-language
   ms.topic: hub-page
-  ms.date: 03/24/2025
+  ms.date: 09/27/2025
   ms.author: lajanuar
 highlightedContent:
 # itemType: architecture | concept | deploy | download | get-started | how-to-guide | learn | overview | quickstart | reference | tutorial | whats-new
@@ -30,7 +30,7 @@ highlightedContent:
 conceptualContent:
   items:
     - title: Extract information
-      summary: Use Natural Language Understanding (NLU) to extract information from unstructured text. For example, identify key phrases or Personally Identifiable Information (PII), summarize text, recognize and categorize named entities, or customize an entity extraction model on top of your domain set.
+      summary: Use Natural Language Understanding (NLU) to extract information from unstructured text.
       links:
         - itemType: overview
           text: Extract key phrases
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サービスのインデックスファイルの更新"
}
```

### Explanation
このコードの変更は、Azure AI Languageサービスに関連する「index.yml」ファイルの更新を示しています。主な内容としては、以下の2つの大きな変更が含まれています：

1. **日付の更新**: `ms.date` フィールドが「03/24/2025」から「09/27/2025」に変更され、ドキュメントの最新のリリース日を反映しています。
   
2. **要約の簡素化**: 「Extract information」セクションの要約が簡潔に再編成され、情報の抽出方法に関する説明が「自然言語理解（NLU）を使用して、非構造化テキストから情報を抽出する。」という一文に短縮されました。これにより、要約がよりシンプルで理解しやすくなっています。

この変更により、ドキュメントは最新の情報を提供しつつ、要約部分の明瞭さを向上させています。

## articles/ai-services/language-service/language-detection/quickstart.md{#item-636553}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 09/15/2025
+ms.date: 09/27/2025
 ms.author: lajanuar
 ms.devlang: csharp
 # ms.devlang: csharp, java, javascript, python
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語検出のクイックスタートガイドの日付更新"
}
```

### Explanation
このコードの変更は、「言語検出」のクイックスタートガイドに関する「quickstart.md」ファイルの更新を反映しています。主な変更点は以下の通りです：

1. **日付の更新**: `ms.date` フィールドが「09/15/2025」から「09/27/2025」へと変更され、ドキュメントの日付が最新のものに更新されました。

この変更は、文書のリリース日を最新のものにするためのものであり、ユーザーに正確で最新の情報を提供することを目的としています。

## articles/ai-services/language-service/named-entity-recognition/tutorials/extract-excel-information.md{#item-96502c}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: tutorial
-ms.date: 03/24/2025
+ms.date: 09/27/2025
 ms.author: lajanuar
 ms.custom: language-service-ner, cogserv-non-critical-language
 ---
@@ -15,13 +15,13 @@ ms.custom: language-service-ner, cogserv-non-critical-language
 
 In this tutorial, you create a Power Automate flow to extract text in an Excel spreadsheet without having to write code. 
 
-This flow takes a spreadsheet of issues reported about an apartment complex, and classify them into two categories: plumbing and other. It also extracts the names and phone numbers of the tenants who sent them. Lastly, the flow appends this information to the Excel sheet. 
+This flow uses a spreadsheet consisting of issues reported about an apartment complex, and classifies them into two categories: plumbing and other. It also extracts the names and phone numbers of the tenants who sent them. Lastly, the flow appends this information to the Excel sheet. 
 
 In this tutorial, you learn how to:
 
 > [!div class="checklist"]
 > * Use Power Automate to create a flow
-> * Upload Excel data from OneDrive for Business
+> * Upload Excel data from OneDrive
 > * Extract text from Excel, and send it for Named Entity Recognition(NER) 
 > * Use the information from the API to update an Excel sheet.
 
@@ -31,19 +31,19 @@ In this tutorial, you learn how to:
 - A Language resource. If you don't have one, you can [create one in the Azure portal](https://portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics) and use the free tier to complete this tutorial.
 - The key and endpoint that was generated for you when you created the resource.
 - A spreadsheet containing tenant issues. Example data for this tutorial is [available on GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/TextAnalytics/sample-data/ReportedIssues.xlsx).
-- Microsoft 365, with [OneDrive for business](https://www.microsoft.com/microsoft-365/onedrive/onedrive-for-business).
+- Microsoft 365, with [OneDrive](https://www.microsoft.com/microsoft-365/onedrive/onedrive-for-business).
 
-## Add the Excel file to OneDrive for Business
+## Add the Excel file to OneDrive
 
-Download the example Excel file from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/TextAnalytics/sample-data/ReportedIssues.xlsx). This file must be stored in your OneDrive for Business account.
+Download the example Excel file from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/TextAnalytics/sample-data/ReportedIssues.xlsx). This file must be stored in your OneDrive account.
 
 :::image type="content" source="../media/tutorials/excel/example-data.png" alt-text="Examples from the Excel file" lightbox="../media/tutorials/excel/example-data.png":::
 
-The issues are reported in raw text. We use the NER feature to extract the person name and phone number. Then the flow looks for the word "plumbing" in the description to categorize the issues. 
+The issues are reported in raw text. We use the Named Entity Recognition (NER) feature to extract the person name and phone number. Then the flow looks for the word "plumbing" in the description to categorize the issues. 
 
 ## Create a new Power Automate workflow
 
-Go to the [Power Automate site](https://make.powerautomate.com/), and log in. Then select **Create** and **Scheduled flow**.
+Go to the [Power Automate site](https://make.powerautomate.com/), and sign in. Then select **Create** and **Scheduled flow**.
 
 :::image type="content" source="../media/tutorials/excel/flow-creation.png" alt-text="The workflow creation screen" lightbox="../media/tutorials/excel/flow-creation.png":::
 
@@ -57,7 +57,7 @@ On the **Build a scheduled cloud flow** page, initialize your flow with the foll
 
 ## Add variables to the flow
 
-Create variables representing the information that is added to the Excel file. Select **New Step** and search for **Initialize variable**. Do this four times, to create four variables.
+Create variables representing the information added to the Excel file. Select **New Step** and search for **Initialize variable**. Do this four times and create four variables.
 
 :::image type="content" source="../media/tutorials/excel/initialize-variables.png" alt-text="The step for initializing variables" lightbox="../media/tutorials/excel/initialize-variables.png":::
 
@@ -79,7 +79,7 @@ Select **New Step** and type **Excel**, then select **List rows present in a tab
 
 :::image type="content" source="../media/tutorials/excel/list-excel-rows.png" alt-text="Add excel rows into the flow" lightbox="../media/tutorials/excel/list-excel-rows.png":::
 
-Add the Excel file to the flow by filling in the fields in this action. This tutorial requires the file to have been uploaded to OneDrive for Business.
+Add the Excel file to the flow by filling in the fields in this action. This tutorial requires that you upload the file to OneDrive.
 
 :::image type="content" source="../media/tutorials/excel/list-excel-rows-options.png" alt-text="Fill the excel rows in the flow" lightbox="../media/tutorials/excel/list-excel-rows-options.png":::
 
@@ -102,7 +102,7 @@ In the **Apply to each**, select **Add an action**. Go to your Language resource
 In your flow, enter the following information to create a new Language connection.
 
 > [!NOTE]
-> If you already have created a Language connection and want to change your connection details, Select the ellipsis on the top right corner, and select **+ Add new connection**.
+> If you already created a Language connection and want to change your connection details, Select the ellipsis on the top right corner, and select **+ Add new connection**.
 
 | Field           | Value                                                                                                             |
 |-----------------|-------------------------------------------------------------------------------------------------------------------|
@@ -113,7 +113,7 @@ In your flow, enter the following information to create a new Language connectio
 :::image type="content" source="../media/tutorials/excel/add-credentials.png" alt-text="Add Language resource credentials to the flow" lightbox="../media/tutorials/excel/add-credentials.png":::
 
 
-## Extract the excel content 
+## Extract the Excel content 
 
 After the connection is created, search for **Text Analytics** and select **Named Entity Recognition**. This extracts information from the description column of the issue.
 
@@ -155,21 +155,21 @@ In the **If yes** condition, type in Excel then select **Update a Row**.
 
 :::image type="content" source="../media/tutorials/excel/yes-column-action.png" alt-text="Update the yes condition" lightbox="../media/tutorials/excel/yes-column-action.png":::
 
-Enter the Excel information, and update the **Key Column**, **Key Value** and **PersonName** fields. This appends the name detected by the API to the Excel sheet. 
+Enter the Excel information, and update the **Key Column**, **Key Value**, and **PersonName** fields. This step appends the name detected by the API to the Excel sheet. 
 
 :::image type="content" source="../media/tutorials/excel/yes-column-action-options.png" alt-text="Add the excel information" lightbox="../media/tutorials/excel/yes-column-action-options.png":::
 
 ## Get the phone number
 
-Minimize the **Apply to each 3** action by clicking on the name. Then add another **Apply to each** action to **Apply to each 2**, like before. its named **Apply to each 4**. Select the text box, and add **entities** as the output for this action. 
+Minimize the **Apply to each 3** action by selecting the name. Then add another **Apply to each** action to **Apply to each 2**, like before, action is named **Apply to each 4**. Select the text box, and add **entities** as the output for this action. 
 
 :::image type="content" source="../media/tutorials/excel/add-apply-action-phone.png" alt-text="Add the entities from the NER output to another apply to each action." lightbox="../media/tutorials/excel/add-apply-action-phone.png":::
 
-Within **Apply to each 4**, add a **Condition** control. Its be named **Condition 2**. In the first text box, search for, and add **categories** from the Dynamic content window. Be sure the center box is set to **is equal to**. Then, in the right text box, enter `var_phone`. 
+Within **Apply to each 4**, add a **Condition** control. This control is named **Condition 2**. In the first text box, search for, and add **categories** from the Dynamic content window. Be sure the center box is set to **is equal to**. Then, in the right text box, enter `var_phone`. 
 
 :::image type="content" source="../media/tutorials/excel/condition-2-options.png" alt-text="Add a second condition control" lightbox="../media/tutorials/excel/condition-2-options.png":::
 
-In the **If yes** condition, add an **Update a row** action. Then enter the information like we did above, for the phone numbers column of the Excel sheet. This appends the phone number detected by the API to the Excel sheet. 
+In the **If yes** condition, add an **Update a row** action. Then enter the information like we did before, for the phone numbers column of the Excel sheet. This step appends the phone number detected by the API to the Excel sheet. 
 
 :::image type="content" source="../media/tutorials/excel/condition-2-yes-column.png" alt-text="Add the excel information to the second if yes condition" lightbox="../media/tutorials/excel/condition-2-yes-column.png":::
 
@@ -179,23 +179,23 @@ Minimize **Apply to each 4** by clicking on the name. Then create another **Appl
 
 :::image type="content" source="../media/tutorials/excel/add-apply-action-plumbing.png" alt-text="Create another apply to each action" lightbox="../media/tutorials/excel/add-apply-action-plumbing.png":::
 
-Next, the flow checks if the issue description from the Excel table row contains the word "plumbing". If yes, it adds "plumbing" in the IssueType column. If not, we enter "other."
+Next, the flow checks if the issue description from the Excel table row contains the word "plumbing." If yes, it adds "plumbing" in the IssueType column. If not, we enter "other."
 
 Inside the **Apply to each 4** action, add a **Condition** Control. Its named **Condition 3**. In the first text box, search for, and add **Description** from the Excel file, using the Dynamic content window. Be sure the center box says **contains**. Then, in the right text box, find and select `var_plumbing`. 
 
 :::image type="content" source="../media/tutorials/excel/condition-3-options.png" alt-text="Create a new condition control" lightbox="../media/tutorials/excel/condition-3-options.png":::
 
-In the **If yes** condition, select **Add an action**, and select **Update a row**. Then enter the information like before. In the IssueType column, select `var_plumbing`. This applies a "plumbing" label to the row.
+In the **If yes** condition, select **Add an action**, and select **Update a row**. Then enter the information like before. In the IssueType column, select `var_plumbing`. This step applies a "plumbing" label to the row.
 
-In the **If no** condition, select **Add an action**, and select **Update a row**. Then enter the information like before. In the IssueType column, select `var_other`. This applies an "other" label to the row.
+In the **If no** condition, select **Add an action**, and select **Update a row**. Then enter the information like before. In the IssueType column, select `var_other`. This step applies an "other" label to the row.
 
 :::image type="content" source="../media/tutorials/excel/plumbing-issue-condition.png" alt-text="Add information to both conditions" lightbox="../media/tutorials/excel/plumbing-issue-condition.png":::
 
 ## Test the workflow
 
 In the top-right corner of the screen, select **Save**, then **Test**. Under **Test Flow**, select **manually**. Then select **Test**, and **Run flow**.
 
-The Excel file gets updated in your OneDrive account. It looks like the below.
+The Excel file gets updated in your OneDrive account. It looks like the following example:
 
 :::image type="content" source="../media/tutorials/excel/updated-excel-sheet.png" alt-text="Test the workflow and view the output" lightbox="../media/tutorials/excel/updated-excel-sheet.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Excel情報抽出チュートリアルの更新"
}
```

### Explanation
このコードの変更は、「Excel情報抽出」に関するチュートリアル「extract-excel-information.md」の修正を示しています。主な変更点は次のとおりです：

1. **日付の更新**: ドキュメントの日付が「03/24/2025」から「09/27/2025」に変更され、最新の情報を反映しています。

2. **文章の改善**: チュートリアル内での表現が一部修正され、内容がより明確で読みやすくなっています。特に、「OneDrive for Business」から「OneDrive」に変更されたほか、文全体で複数の文言が整えられ、理解しやすさが向上しています。

3. **手順の整理**: Power Automateフローの手順に関連するいくつかの説明が簡略化され、冗長な表現が削除されており、手順に沿った流れがよりスムーズになっています。

これらの変更により、ユーザーがチュートリアルに従ってExcelから情報を抽出するプロセスがより効果的に理解できるようになっています。

## articles/ai-services/language-service/native-document-support/managed-identities.md{#item-ddd66a}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.topic: how-to
 manager: nitinme
 ms.author: lajanuar
 author: laujan
-ms.date: 03/05/2025
+ms.date: 09/27/2025
 ms.custom: sfi-image-nochange
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージドアイデンティティに関する日付更新"
}
```

### Explanation
このコードの変更は、「マネージドアイデンティティ」に関するドキュメント「managed-identities.md」の更新を示しています。主な変更点は次のとおりです：

1. **日付の更新**: `ms.date` フィールドが「03/05/2025」から「09/27/2025」へと変更され、ドキュメントの日付が最新のものに更新されました。

この変更は、ユーザーに最新の情報を提供し、ドキュメントが現在の内容と一致するようにするためのものです。これにより、利用者は信頼性の高い最新の情報に基づいて判断を行うことができます。

## articles/ai-services/language-service/native-document-support/shared-access-signatures.md{#item-01eef1}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.topic: how-to
 manager: nitinme
 ms.author: lajanuar
 author: laujan
-ms.date: 03/05/2025
+ms.date: 09/27/2025
 ---
 
 # SAS tokens for your storage containers
@@ -125,7 +125,7 @@ Here's a sample REST API request:
 
 That's it! You learned how to create SAS tokens to authorize how clients access your data.
 
-## Next steps
+## Next step
 
 > [!div class="nextstepaction"]
 > [Learn more about native document support](overview.md "Learn how to process and analyze native documents.") [Learn more about granting access with SAS ](/azure/storage/common/storage-sas-overview "Grant limited access to Azure Storage resources using shared access SAS.")
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SASトークンに関する日付更新とセクションタイトルの変更"
}
```

### Explanation
このコードの変更は、「共有アクセス署名」に関するドキュメント「shared-access-signatures.md」の更新を示しています。主な変更点は次のとおりです：

1. **日付の更新**: `ms.date` フィールドが「03/05/2025」から「09/27/2025」に変更され、ドキュメントの日付が最新の情報を反映しています。

2. **セクションタイトルの変更**: 「Next steps」というセクションタイトルが「Next step」に変更され、文脈に合わせたより適切な語形に調整されています。

これらの変更により、ユーザーは最新の情報にアクセスできるようになり、ドキュメントがより一貫した表現を持つようになりました。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-conversation-pii.md{#item-0d6332}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 03/05/2025
+ms.date: 09/27/2025
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話の個人情報の編集に関する日付更新"
}
```

### Explanation
このコードの変更は、「会話の個人情報を編集する方法」に関するドキュメント「redact-conversation-pii.md」の更新を示しています。主な変更点は次のとおりです：

1. **日付の更新**: `ms.date` フィールドが「03/05/2025」から「09/27/2025」に変更され、ドキュメントの日付が最新の情報を反映しています。

この変更により、ユーザーは最新の日付に基づく信頼性のある情報を得ることができ、ドキュメントの整合性が保たれます。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-document-pii.md{#item-5509ee}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 09/15/2025
+ms.date: 09/27/2025
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントの個人情報の編集に関する日付更新"
}
```

### Explanation
このコードの変更は、「ドキュメントの個人情報を編集する方法」に関するドキュメント「redact-document-pii.md」の更新を示しています。主な変更点は次のとおりです：

1. **日付の更新**: `ms.date` フィールドが「09/15/2025」から「09/27/2025」に変更され、ドキュメントの日付が最新の情報を反映しています。

この改訂により、ユーザーは最新の日付の情報を確認でき、ドキュメントの整合性と信頼性が向上します。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-text-pii.md{#item-9e48af}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,12 @@
 ---
 title: Identify and extract Personally Identifying Information (PII) from text
 titleSuffix: Azure AI services
-description: This article shows you how to identify, extract and redact Personally Identifying Information (PII) from text.
+description: This article shows you how to identify, extract, and redact Personally Identifying Information (PII) from text.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 03/05/2025
+ms.date: 09/27/2025
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
@@ -35,13 +35,13 @@ In version `2024-11-5-preview`, you're able to define the `redactionPolicy` para
 - `MaskWithCharacter` (default) 
 - `MaskWithEntityType` 
 
-The `DoNotRedact` policy allows the user to return the response without the `redactedText` field, that is, "John Doe received a call from 424-878-9192". 
+The `DoNotRedact` policy allows the user to return the response without the `redactedText` field, that is, "John Doe received a call from 424-878-919." 
 
-The `MaskWithRedactionCharacter` policy allows the `redactedText` to be masked with a character (such as "*"), preserving the length and offset of the original text, that is, "******** received a call from ************". This is the existing behavior.
+The `MaskWithRedactionCharacter` policy allows the `redactedText` to be masked with a character (such as "*"), preserving the length and offset of the original text, that is, "******** received a call from ************." This result is the existing behavior.
 
 There's also an optional field called `redactionCharacter` where you can input the character to be used in redaction if you're using the `MaskWithCharacter` policy 
 
-The `MaskWithEntityType` policy allows you to mask the detected PII entity text with the detected entity type, that is, "[PERSON_1] received a call from [PHONENUMBER_1]". 
+The `MaskWithEntityType` policy allows you to mask the detected PII entity text with the detected entity type, that is, "[PERSON_1] received a call from [PHONENUMBER_1]." 
 
 ## Select which entities to be returned
 
@@ -120,13 +120,13 @@ The API attempts to detect the [defined entity categories](../concepts/entity-ca
 
 ## Adapting PII to your domain
 
-To accommodate and adapt to a customer’s custom vocabulary used to identify entities (also known as the “context”), the `entitySynonyms` feature allows customers to define their own synonyms for specific entity types. The goal of this feature is to help detect entities in contexts that the model is not familiar with but are used in the customer’s inputs by ensuring that the customer’s unique terms are recognized and correctly associated during the detection process. 
+To accommodate and adapt to a customer's custom vocabulary used to identify entities (also known as the "context"), the `entitySynonyms` feature allows customers to define their own synonyms for specific entity types. The goal of this feature is to help detect entities in contexts that the model isn't familiar with but are used in the customer's inputs by ensuring that the customer's unique terms are recognized and correctly associated during the detection process. 
 
-The `valueExclusionPolicy` option allows customers to adapt the PII service for scenarios where customers prefer certain terms not to be detected and redacted even if those terms fall into a PII category they are interested in detected. For example, a police department might want personal identifiers redacted in most cases except for terms like “police officer”, “suspect”, and “witness”. 
+The `valueExclusionPolicy` option allows customers to adapt the PII service for scenarios where customers prefer certain terms not to be detected and redacted even if those terms fall into a PII category they're interested in detected. For example, a police department might want personal identifiers redacted in most cases except for terms like "police officer," "suspect," and "witness." 
 
-Customers can now adapt the PII service’s detecting by specifying their own regex using a regex recognition configuration file. See our [container how-to guides](use-containers.md) for a tutorial on how to install and run Personally Identifiable Information (PII) Detection containers. 
+Customers can now adapt the PII service's detecting by specifying their own regex using a regex recognition configuration file. See our [container how-to guides](use-containers.md) for a tutorial on how to install and run Personally Identifiable Information (PII) Detection containers. 
 
-A more detailed tutorial can be found in the “[Adapting PII to your domain](adapt-to-domain-pii.md)” how-to guide. 
+A more detailed tutorial can be found in the "[Adapting PII to your domain](adapt-to-domain-pii.md)" how-to guide. 
 
 
 ## Submitting data
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキストにおける個人情報の編集に関する文書の更新"
}
```

### Explanation
このコードの変更は、「テキストから個人を特定できる情報（PII）を識別し、抽出し、編集する方法」に関するドキュメント「redact-text-pii.md」の更新を示しています。主な変更点は以下の通りです：

1. **文言の修正**: 様々な箇所で記述が微調整され、正確さが増しました。例えば、「redactedText」フィールドを持たないレスポンスを返すことに関する説明や、「MaskWithCharacter」ポリシーを用いた場合のマスキングの例文が改善されました。

2. **日付の更新**: `ms.date` フィールドが「03/05/2025」から「09/27/2025」に変更され、ドキュメントが最新の情報を反映しています。

この変更により、内容がより明確で一貫性があり、読者は更新された情報を通じて信頼性のある理解を得ることができます。

## articles/ai-services/language-service/sentiment-opinion-mining/quickstart.md{#item-8c5758}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 02/17/2025
+ms.date: 09/27/2025
 ms.author: lajanuar
 ms.devlang: csharp
 # ms.devlang: csharp, java, javascript, python
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートガイドの日付更新"
}
```

### Explanation
このコードの変更は、「感情分析および意見マイニングのクイックスタート」ガイド「quickstart.md」の更新を示しています。主な変更点は次の通りです：

1. **日付の更新**: `ms.date` フィールドが「02/17/2025」から「09/27/2025」に変更され、ドキュメントが最新の情報を反映しています。

この修正により、ユーザーは最新の日付に基づいて情報を確認でき、ドキュメントの信頼性と正確性が向上します。

## articles/ai-services/language-service/summarization/how-to/conversation-summarization.md{#item-9ff946}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 03/05/2025
+ms.date: 09/27/2025
 ms.author: lajanuar
 ms.custom:
   - language-service-pii
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話要約ガイドの日付更新"
}
```

### Explanation
このコードの変更は、「会話要約」に関するドキュメント「conversation-summarization.md」の更新を示しています。主な変更点は以下の通りです：

1. **日付の更新**: `ms.date` フィールドが「03/05/2025」から「09/27/2025」に変更され、ドキュメントが最新の情報を反映しています。

この修正により、ユーザーは更新された日付に基づいて情報を確認でき、ドキュメントの信頼性を向上させています。

## articles/ai-services/language-service/summarization/how-to/text-summarization.md{#item-8a6034}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 03/05/2025
+ms.date: 09/27/2025
 ms.author: lajanuar
 ms.custom:
   - language-service-summarization
@@ -68,20 +68,20 @@ When you get results from language detection, you can stream the results to an a
 
 To follow is an example of content you might submit for summarization, which is extracted using the Microsoft blog article [A holistic representation toward integrative AI](https://www.microsoft.com/research/blog/a-holistic-representation-toward-integrative-ai/). This article is only an example. The API can accept longer input text. For more information, *see* [data and service limits](../overview.md#input-requirements-and-service-limits)
  
-*"At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."*
+*"At Microsoft, we are on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that's closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."*
 
 The text summarization API request is processed upon receipt of the request by creating a job for the API backend. If the job succeeded, the output of the API is returned. The output is available for retrieval for 24 hours. After this time, the output is purged. Due to multilingual and emoji support, the response might contain text offsets. For more information, *see* [how to process offsets](../../concepts/multilingual-emoji-support.md).
 
 When you use the preceding example, the API might return these summarized sentences:
 
 **Extractive summarization**:
 
-- "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding."
+- "At Microsoft, we are on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding."
 - "We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages."
 - "The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today."
 
 **Abstractive summarization**:
-- "Microsoft is taking a more holistic, human-centric approach to learning and understanding. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. Over the past five years, we have achieved human performance on benchmarks in."
+- "Microsoft is taking a more holistic, human-centric approach to learning and understanding. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. Over the past five years, we achieved human performance on key benchmarks."
 
 ### Try text extractive summarization
 
@@ -91,10 +91,10 @@ You can use the `sentenceCount` parameter to guide how many sentences are return
 
 You can also use the `sortby` parameter to specify in what order the extracted sentences are returned - either `Offset` or `Rank`, with `Offset` being the default. 
 
-|parameter value  |Description  |
-|---------|---------|
-|Rank    | Order sentences according to their relevance to the input document, as decided by the service.        |
-|Offset    | Keeps the original order in which the sentences appear in the input document.        |
+| parameter value | Description |
+|--|--|
+| Rank | Order sentences according to their relevance to the input document, as decided by the service. |
+| Offset | Keeps the original order in which the sentences appear in the input document. |
 
 ### Try text abstractive summarization
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト要約ガイドの内容修正"
}
```

### Explanation
このコードの変更は、「テキスト要約」に関するドキュメント「text-summarization.md」の内容更新を示しています。主な変更点は以下の通りです：

1. **日付の更新**: `ms.date` フィールドが「03/05/2025」から「09/27/2025」に変更され、最新の日付を反映しています。

2. **テキストの修正**: ドキュメント内の具体的なテキストが修正され、より明確かつ正確な情報が提供されています。特に、パラグラフの表現が改善されており、一部の語句や文が変更されています。

3. **表の形式修正**: 表のフォーマットが整えられ、視覚的な明瞭さが向上しています。

これらの修正により、ユーザーはより正確で明解な情報を得ることができ、文書の全体的な品質が向上しています。

## articles/ai-services/language-service/summarization/overview.md{#item-844139}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 03/05/2025
+ms.date: 09/27/2025
 ms.author: lajanuar
 ms.custom: language-service-summarization, build-2024, ignite-2024
 ---
@@ -51,7 +51,7 @@ Text summarization uses natural language processing techniques to generate a sum
 
 As an example, consider the following paragraph of text:
 
-*"At Microsoft, we are on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we achieve human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."*
+*"At Microsoft, we are on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we achieve human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that's closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."*
 
 The text summarization API request is processed upon receipt of the request by creating a job for the API backend. If the job succeeded, the output of the API is returned. The output is available for retrieval for 24 hours. After this time, the output is purged. Due to multilingual and emoji support, the response can contain text offsets. For more information, see [how to process offsets](../concepts/multilingual-emoji-support.md).
 
@@ -91,15 +91,15 @@ As an example, consider the following example conversation:
 
 **Customer**: "*Yes, I pushed the wifi connection button, and now the power light is slowly blinking.*"
 
-**Agent**: "*Great. Thank you! Now, please check in your Contoso Coffee app. Does it prompt to ask you to connect with the machine?*"
+**Agent**: "*Great. Thank you! Now, check in your Contoso Coffee app. Does it prompt to ask you to connect with the machine?*"
 
 **Customer**: "*No. Nothing happened.*"
 
-**Agent**: "*I see. Thanks. Let's try if a factory reset can solve the issue. Could you please press and hold the center button for 5 seconds to start the factory reset.*"
+**Agent**: "*I see. Thank you. Let's try if a factory reset can solve the issue. Could you please press and hold the center button for 5 seconds to start the factory reset.*"
 
-**Customer**: *"I've tried the factory reset and followed the above steps again, but it still didn't work."*
+**Customer**: *"I tried the factory reset and followed the above steps again, but it still didn't work."*
 
-**Agent**: "*I'm very sorry to hear that. Let me see if there's another way to fix the issue. Please hold on for a minute.*"
+**Agent**: "*I'm sorry to hear that. Let me see if there's another way to fix the issue. Please hold on for a minute.*"
 
 Conversation summarization feature would simplify the text as follows:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "要約機能の概要更新"
}
```

### Explanation
このコードの変更は、「要約」に関するドキュメント「overview.md」の内容更新を示しています。主な変更点は以下の通りです：

1. **日付の更新**: `ms.date` フィールドが「03/05/2025」から「09/27/2025」に変更され、文書が最新の日付を反映しています。

2. **テキストの修正**: 複数の文において語句が変更され、より流暢で一貫した表現になっています。例えば、「ありがとう」の後に「今、」を加えたり、「私は」といった表現を省略したりすることで、会話の自然さが向上しています。

3. **会話例の修正**: 会話の例において、言葉遣いやフレーズが調整され、よりスムーズなコミュニケーションを模倣しています。

これらの修正は、文書の読みやすさを向上させるとともに、機能の説明がより明確になります。結果として、ユーザーはより良い理解を得ることができるようになります。


