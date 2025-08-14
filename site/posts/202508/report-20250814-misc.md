---
date: '2025-08-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ebf24ba...MicrosoftDocs:a697dec
summary: このレポートでは、ドキュメントのリンクや表記の修正により、ユーザーの使いやすさが向上したことが述べられています。すべての変更はマイナーなもので、新機能や破壊的な変更はありません。主な改訂内容は既存の情報の明確化やリンクの整理に焦点を当てており、特に新規ユーザーにとって役立つよう条件とフォーマットを見直しています。また、AzureポータルやAzure
  Blob Storageに関する情報の整理も行われ、作業フローが改善されています。全体として、これらの変更はサービスの利用を円滑にし、ユーザーエクスペリエンスを向上させることを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ebf24ba...MicrosoftDocs:a697dec){target="_blank"}

<format>
# Highlights
ドキュメントでのリンクや表記の修正および情報の整理が行われ、ユーザーの使いやすさが向上しています。変更はすべてマイナーな更新に分類され、新機能や破壊的変更は含まれていません。

## New features
現行のドキュメントに新機能が追加されたわけではなく、主要な改訂内容は既存の情報を基にした説明の明確化やリンクの整理に重点が置かれています。

## Breaking changes
破壊的な変更はありません。すべてのアップデートは既存の情報を明確化し、利便性を高めることを目的としています。

## Other updates
- ガイドラインや概要説明の表現の改善。
- リンクテキストおよびセクションタイトルの一致強化。
- 認証関連情報の一貫性を持たせた更新。

# Insights
このコード変更の主なポイントは、ドキュメント全体の明確性と整合性を向上させるという点にあります。これにより、ユーザーはより迅速に情報を把握し、ドキュメントインテリジェンスサービスを効果的に利用できるようになります。

まず、カスタムモデルやリソースの作成に関するガイドでは、リンク先がより適切に調整され、ユーザーが直面する可能性のある混乱を防ぐための措置が取られています。リンクの統一とタイトル変更は、特に新規ユーザーにとって有用です。また、AzureポータルやAzure Blob Storageの重要な情報が強調されて整理されており、作業フローが改善されています。

さらに、入力要件に関するガイドラインでの変更は、フォーマットや条件をよりリスト形式で引き立たせ、ユーザーが必要な情報に即座にアクセスできるよう配慮しています。モデル分析機能に関する変更も同様に、表形式を改善し、情報が容易に比較できる状態を実現しています。

最後に、Document Intelligence Studioに関するクイックスタートガイドおよびスタジオの概要では、文言や構造を改善し、ユーザーがこれらのリソースをスムーズに利用できるように特化されています。認証情報の明確化、関連するリンクの追加もユーザーの利便性を考慮した改訂ポイントです。

全体を通して、これらのマイナーな更新は、サービスの利用が予想されるバリアを低減し、ユーザーエクスペリエンスを向上させることを目的としています。これにより、サービス提供の効率性が高まり、利用者がこれまで以上に容易にドキュメントインテリジェンス技術を活用できるようになるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [build-a-custom-model.md](#item-4f2040) | minor update | カスタムモデルの構築方法のガイドの更新 | modified | 1 | 1 | 2 | 
| [create-document-intelligence-resource.md](#item-d4cf00) | minor update | ドキュメントインテリジェンスリソースの作成ガイドの更新 | modified | 26 | 29 | 55 | 
| [input-requirements.md](#item-20011c) | minor update | 入力要件に関するガイドラインの更新 | modified | 13 | 22 | 35 | 
| [model-analysis-features.md](#item-0fe95e) | minor update | モデル分析機能に関する表の更新 | modified | 30 | 30 | 60 | 
| [model-overview.md](#item-768c0d) | minor update | ドキュメントインテリジェンスモデルの概要の更新 | modified | 185 | 192 | 377 | 
| [overview.md](#item-4e36ba) | minor update | ドキュメントインテリジェンス概要の更新 | modified | 128 | 134 | 262 | 
| [layout.md](#item-f7c4c8) | minor update | レイアウトモデルに関する更新 | modified | 215 | 230 | 445 | 
| [get-started-studio.md](#item-b2798e) | minor update | Document Intelligence Studio のクイックスタートガイドの更新 | modified | 66 | 76 | 142 | 
| [studio-custom-project.md](#item-f52b95) | minor update | Document Intelligence Studio カスタムプロジェクトの作成に関するガイドの更新 | modified | 52 | 56 | 108 | 
| [studio-overview.md](#item-db8fa3) | minor update | Document Intelligence Studio 概要の更新 | modified | 33 | 35 | 68 | 
| [whats-new.md](#item-1ec8d3) | minor update | Document Intelligence の新機能に関する更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/how-to-guides/build-a-custom-model.md{#item-4f2040}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ Once you gather a set of forms or documents for training, you need to upload it
 
 The Document Intelligence Studio provides and orchestrates all the API calls required to complete your dataset and train your model.
 
-1. Start by navigating to the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio). The first time you use the Studio, you need to [initialize your subscription, resource group, and resource](../studio-overview.md). Then, follow the [prerequisites for custom projects](../quickstarts/studio-custom-project.md#prerequisites-for-custom-projects) to configure the Studio to access your training dataset.
+1. Start by navigating to the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio). The first time you use the Studio, you need to [initialize your subscription, resource group, and resource](../studio-overview.md). Then, follow the [prerequisites for custom projects](../quickstarts/studio-custom-project.md#prerequisites) to configure the Studio to access your training dataset.
 
 1. In the Studio, select the **Custom extraction model** tile and select the **Create a project** button.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムモデルの構築方法のガイドの更新"
}
```

### Explanation
このコードの変更では、ドキュメントのガイドラインにおいて、特定の手順のリンクが更新されました。具体的には、カスタムプロジェクトの設定に関するディレクションが修正され、より正確なリンクが提供されています。この変更により、ユーザーはドキュメントインテリジェンススタジオでのトレーニングデータセットへのアクセスを適切に設定できるようになります。変更の内容は、元の手順「custom projects」のリンク修正が行われており、ユーザーにとっての利便性が向上しています。

## articles/ai-services/document-intelligence/how-to-guides/create-document-intelligence-resource.md{#item-d4cf00}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Create a Document Intelligence resource
+title: Create a Document Intelligence Resource
 titleSuffix: Azure AI services
 description: Create a Document Intelligence resource in the Azure portal.
 author: laujan
@@ -17,59 +17,56 @@ ms.author: lajanuar
  [!INCLUDE [applies to v4.0 v3.1 v3.0 v2.1](../includes/applies-to-v40-v31-v30-v21.md)]
 ::: moniker-end
 
-Azure AI Document Intelligence is a cloud-based [Azure AI service](../../../ai-services/index.yml) that uses machine-learning models to extract key-value pairs, text, and tables from your documents. In this article, learn how to create a Document Intelligence resource in the Azure portal.
+Azure AI Document Intelligence is a cloud-based [Azure AI service](../../../ai-services/index.yml) that uses machine-learning models to extract key/value pairs, text, and tables from your documents. In this article, learn how to create a Document Intelligence resource in the Azure portal.
 
 ## Visit the Azure portal
 
-The Azure portal is a single platform you can use to create and manage Azure services.
+The Azure portal is a single platform that you can use to create and manage Azure services.
 
-Let's get started:
+To get started:
 
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
-1. Select **Create a resource** from the Azure home page.
+1. On the Azure home page, select **Create a resource**.
 
-1. Search for and choose **Document Intelligence** from the search bar.
+1. In the search bar, search for and choose **Document Intelligence**.
 
-1. Select the **Create** button.
+1. Select **Create**.
 
 ## Create a resource
 
-1. Next, you're going to fill out the **`Create Document Intelligence`** fields with the following values:
+1. Fill out the **Create Form Recognizer** fields with the following values:
 
-    * **Subscription**. Select your current subscription.
-    * **Resource group**. The [Azure resource group](/azure/cloud-adoption-framework/govern/resource-consistency/resource-access-management#what-is-an-azure-resource-group) that contains your resource. You can create a new group or add it to an existing group.
-    * **Region**. Select your local region.
-    * **Name**. Enter a name for your resource. We recommend using a descriptive name, for example *YourNameDocumentIntelligence*.
-    * **Pricing tier**. The cost of your resource depends on the pricing tier you choose and your usage. For more information, see [pricing details](https://azure.microsoft.com/pricing/details/cognitive-services/). You can use the free pricing tier (F0) to try the service, and upgrade later to a paid tier for production.
+    * **Subscription**: Select your current subscription.
+    * **Resource group**: The [Azure resource group](/azure/cloud-adoption-framework/govern/resource-consistency/resource-access-management#what-is-an-azure-resource-group) that contains your resource. You can create a new group or add it to an existing group.
+    * **Region**: Select your local region.
+    * **Name**: Enter a name for your resource. We recommend that you use a descriptive name, for example, *YourNameDocumentIntelligence*.
+    * **Pricing tier**: The cost of your resource depends on the pricing tier you choose and your usage. For more information, see [Pricing details](https://azure.microsoft.com/pricing/details/cognitive-services/). You can use the free pricing tier (F0) to try the service. You can upgrade later to a paid tier for production.
 
-1. Select **Review + Create**.
+1. Select **Review + create**.
 
-    :::image type="content" source="../media/logic-apps-tutorial/logic-app-connector-demo-two.png" alt-text="Still image showing the correct values for creating Document Intelligence resource.":::
+    :::image type="content" source="../media/logic-apps-tutorial/logic-app-connector-demo-two.png" alt-text="Screenshot that shows the correct values for creating a Document Intelligence resource.":::
 
-1. Azure will run a quick validation check, after a few seconds you should see a green banner that says **Validation Passed**.
+1. Azure runs a quick validation check. After a few seconds, a green banner appears that says **Validation Passed**.
 
-1. Once the validation banner appears, select the **Create** button from the bottom-left corner.
+1. After the validation banner appears, select **Create**.
 
-1. After you select create, you'll be redirected to a new page that says **Deployment in progress**. After a few seconds, you'll see a message that says, **Your deployment is complete**.
+1. A new page opens that says **Deployment in progress**. After a few seconds, a message appears that says **Your deployment is complete**.
 
-## Get Endpoint URL and keys
+## Get endpoint URL and keys
 
-1. Once you receive the *deployment is complete* message, select the **Go to resource** button.
+1. After you receive the message, select **Go to resource**.
 
-1. Copy the key and endpoint values from your Document Intelligence resource paste them in a convenient location, such as *Microsoft Notepad*. You need the key and endpoint values to connect your application to the Document Intelligence API.
+1. Copy the key and endpoint values from your Document Intelligence resource. Paste the values in a convenient location, such as Notepad. You need the key and endpoint values to connect your application to the Document Intelligence API.
 
-1. If your overview page doesn't have the keys and endpoint visible, you can select the **Keys and Endpoint** button, on the left pane, and retrieve them there.
+1. If your overview page doesn't show the keys and endpoint, select **Keys and Endpoint** on the left pane, and retrieve them there.
 
-    :::image border="true" type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Still photo showing how to access resource key and endpoint URL.":::
+    :::image border="true" type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot that shows how to access the resource key and endpoint URL.":::
 
-That's it! You're now ready to start automating data extraction using Azure AI Document Intelligence.
+## Related content
 
-## Next steps
-
-* Try the [Document Intelligence Studio](../concept-document-intelligence-studio.md), an online tool for visually exploring, understanding, and integrating features from the Document Intelligence service into your applications.
-
-* Complete a Document Intelligence quickstart and get started creating a document processing app in the development language of your choice:
+* Try [Document Intelligence Studio](../concept-document-intelligence-studio.md), an online tool that helps you visually explore, understand, and integrate features from Document Intelligence into your applications.
+* Finish a Document Intelligence quickstart and then create a document processing app in the development language of your choice:
 
   * [C#](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)
   * [Python](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスリソースの作成ガイドの更新"
}
```

### Explanation
このコードの変更では、Azureポータルでのドキュメントインテリジェンスリソースの作成に関するガイドが更新されました。具体的には、手順の見出しやリンクの表記が修正され、より明確で一貫性のある形式が採用されています。また、複数の手順において、指示がより自然な日本語に改訂されており、ユーザーの理解を助ける内容になっています。この更新を通じて、文書の流れが改善され、読者にとって使いやすい情報となることを目指しています。さらに、関連コンテンツセクションが新たに追加され、ユーザーが次に取るべきアクションが簡潔に説明されています。

## articles/ai-services/document-intelligence/includes/input-requirements.md{#item-20011c}

<details>
<summary>Diff</summary>
````diff
@@ -7,33 +7,24 @@ ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD041 -->
 
-Supported file formats:
+The following file formats are supported.
 
-|Model | PDF |Image: </br>`JPEG/JPG`, `PNG`, `BMP`, `TIFF`, `HEIF` | Microsoft Office: </br> Word (`DOCX`), Excel (`XLSX`), PowerPoint (`PPTX`), HTML|
+|Model | PDF |Image: </br>JPEG/JPG, PNG, BMP, TIFF, HEIF | Office: </br> Word (DOCX), Excel (XLSX), PowerPoint (PPTX), HTML|
 |--------|:----:|:-----:|:---------------:|
 |Read            | ✔    | ✔    | ✔  |
 |Layout          | ✔  | ✔ | ✔  |
-|General&nbsp;Document| ✔  | ✔ |   |
+|General&nbsp;document| ✔  | ✔ |   |
 |Prebuilt        |  ✔  | ✔ |   |
 |Custom extraction |  ✔  | ✔ |   |
 |Custom classification  |  ✔  | ✔ | ✔  |
 
-* For best results, provide one clear photo or high-quality scan per document.
-
-* For PDF and TIFF, up to 2,000 pages can be processed (with a free tier subscription, only the first two pages are processed).
-
-* The file size for analyzing documents is 500 MB for paid (S0) tier and `4` MB for free (F0) tier.
-
-* Image dimensions must be between 50 pixels x 50 pixels and 10,000 pixels x 10,000 pixels.
-
-* If your PDFs are password-locked, you must remove the lock before submission.
-
-* The minimum height of the text to be extracted is 12 pixels for a 1024 x 768 pixel image. This dimension corresponds to about `8` point text at 150 dots per inch (DPI).
-
-* For custom model training, the maximum number of pages for training data is 500 for the custom template model and 50,000 for the custom neural model.
-
-* For custom extraction model training, the total size of training data is 50 MB for template model and `1` GB for the neural model.
-
-* For custom classification model training, the total size of training data is `1` GB  with a maximum of 10,000 pages. For `2024-11-30` (GA), the total size of training data is `2` GB with a maximum of 10,000 pages.
-    
-* For office file types (docx, xlsx, pptx), there's a maximum string length limit of 8,000,000 characters.
+* **Photos and scans**: For best results, provide one clear photo or high-quality scan per document.
+* **PDFs and TIFFs**: For PDFs and TIFFs, up to 2,000 pages can be processed. (With a free-tier subscription, only the first two pages are processed.)
+* **File size**: The file size for analyzing documents is 500 MB for the paid (S0) tier and 4 MB for the free (F0) tier.
+* **Image dimensions**: The dimensions must be between 50 pixels x 50 pixels and 10,000 pixels x 10,000 pixels.
+* **Password locks**: If your PDFs are password-locked, you must remove the lock before submission.
+* **Text height**: The minimum height of the text to be extracted is 12 pixels for a 1024 x 768-pixel image. This dimension corresponds to about 8-point text at 150 dots per inch.
+* **Custom model training**: The maximum number of pages for training data is 500 for the custom template model and 50,000 for the custom neural model.
+* **Custom extraction model training**: The total size of training data is 50 MB for template model and 1 GB for the neural model.
+* **Custom classification model training**: The total size of training data is 1 GB with a maximum of 10,000 pages. For 2024-11-30 (GA), the total size of training data is 2 GB with a maximum of 10,000 pages.
+* **Office file types (DOCX, XLSX, PPTX)**: The maximum string length limit is 8 million characters.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "入力要件に関するガイドラインの更新"
}
```

### Explanation
このコードの変更では、ドキュメントインテリジェンスにおける入力要件に関するガイドラインが更新されました。変更点には、サポートされるファイル形式の紹介文が修正され、より明確な箇条書き形式で要件が示されています。具体的には、各項目が整理され、ユーザーが容易に情報を把握できるようになっています。また、ドキュメントや画像に関する取り扱いや要件が具体的に示されており、特にファイルサイズ、ページ数、画像の寸法、テキストの高さ、パスワード保護の注意点に関しても明確に述べられています。これにより、ユーザーは適切な準備を行い、サービスの利用に際して必要な条件を確認しやすくなります。

## articles/ai-services/document-intelligence/includes/model-analysis-features.md{#item-0fe95e}

<details>
<summary>Diff</summary>
````diff
@@ -7,37 +7,37 @@ ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD041 -->
 
-|Model ID|Content Extraction|Query fields|Paragraphs|Paragraph Roles|Selection Marks|Tables|Key-Value Pairs|Languages|Barcodes|Document Analysis|Formulas*|Style Font*|High Resolution*|Searchable PDF
+|Model ID|Content extraction|Query fields|Paragraphs|Paragraph roles|Selection marks|Tables|Key/value pairs|Languages|Barcodes|Document analysis|Formulas*|Style font*|High resolution*|Searchable PDF
 |:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
-|prebuilt-read|✓| |✓| | | | |O|O| |O|O|O|O|
-|prebuilt-layout|✓|✓|✓|✓|✓|✓|O|O|O| |O|O|O|
-|prebuilt-contract|✓|✓|✓|✓|✓ | | |O|O|✓|O|O|
-|prebuilt-healthInsuranceCard.us|✓|✓| | | | | |O|O|✓|O|O|O|
-|prebuilt-idDocument|✓|✓|| | | | |O|O|✓|O|O|O|
-|prebuilt-invoice|✓|✓| | |✓|✓|O|O|O|✓|O|O|O|
-|prebuilt-receipt|✓|✓| | | | | |O|O|✓|O|O|O|
-|prebuilt-marriageCertificate.us | ✓|✓ | | |✓| | | O | O |✓ | O | O | O |
-|prebuilt-creditCard | ✓|✓ | | | | | | O | O |✓ | O | O | O |
-|prebuilt-check.us | ✓|✓ | | | | | | O | O |✓ | O | O | O |
-|prebuilt-payStub.us | ✓|✓ | | | | | | O | O |✓ | O | O | O |
-|prebuilt-bankStatement | ✓|✓ | | | | | | O | O |✓ | O | O | O |
-|prebuilt-mortgage.us.1003 | ✓|✓ | | |✓| | | O | O |✓ | O | O | O |
-|prebuilt-mortgage.us.1004 | ✓|✓ | | |✓| | | O | O |✓ | O | O | O |
-|prebuilt-mortgage.us.1005 | ✓|✓ | | |✓| | | O | O |✓ | O | O | O |
-|prebuilt-mortgage.us.1008 | ✓|✓ | | |✓| | | O | O |✓ | O | O | O |
-|prebuilt-mortgage.us.closingDisclosure | ✓|✓ | | |✓| | | O | O |✓ | O | O | O |
-|prebuilt-tax.us|✓|✓| | |✓| | |O|O|✓|O|O|O|
-|prebuilt-tax.us.w2|✓|✓| | |✓| | |O|O|✓|O|O|O|
-|prebuilt-tax.us.w4|✓|✓| | | | | |O|O|✓|O|O|O|
-|prebuilt-tax.us.1040 (various) | ✓|✓ | | |✓| | | O | O |✓ | O | O | O |
-|prebuilt-tax.us.1095A|✓|✓| | | | | |O|O|✓|O|O|O|
-|prebuilt-tax.us.1095C|✓|✓| | | | | |O|O|✓|O|O|O|
-|prebuilt-tax.us.1098|✓|✓| | |✓| | |O|O|✓|O|O|O|
-|prebuilt-tax.us.1098E|✓|✓| | |✓| | |O|O|✓|O|O|O|
-|prebuilt-tax.us.1098T|✓|✓| | |✓| | |O|O|✓|O|O|O|
-|prebuilt-tax.us.1099 (various)|✓|✓| | |✓| | |O|O|✓|O|O|O|
-|prebuilt-tax.us.1099SSA|✓|✓| | | | | |O|O|✓|O|O|O|
-|{ customModelName }|✓|✓|✓|✓|✓|✓| |O|O|✓|O|O|O|
+|`prebuilt-read`|✓| |✓| | | | |O|O| |O|O|O|O|
+|`prebuilt-layout`|✓|✓|✓|✓|✓|✓|O|O|O| |O|O|O|
+|`prebuilt-contract`|✓|✓|✓|✓|✓ | | |O|O|✓|O|O|
+|`prebuilt-healthInsuranceCard.us`|✓|✓| | | | | |O|O|✓|O|O|O|
+|`prebuilt-idDocument`|✓|✓|| | | | |O|O|✓|O|O|O|
+|`prebuilt-invoice`|✓|✓| | |✓|✓|O|O|O|✓|O|O|O|
+|`prebuilt-receipt`|✓|✓| | | | | |O|O|✓|O|O|O|
+|`prebuilt-marriageCertificate.us` | ✓|✓ | | |✓| | | O | O |✓ | O | O | O |
+|`prebuilt-creditCard` | ✓|✓ | | | | | | O | O |✓ | O | O | O |
+|`prebuilt-check.us` | ✓|✓ | | | | | | O | O |✓ | O | O | O |
+|`prebuilt-payStub.us` | ✓|✓ | | | | | | O | O |✓ | O | O | O |
+|`prebuilt-bankStatement` | ✓|✓ | | | | | | O | O |✓ | O | O | O |
+|`prebuilt-mortgage.us.1003` | ✓|✓ | | |✓| | | O | O |✓ | O | O | O |
+|`prebuilt-mortgage.us.1004` | ✓|✓ | | |✓| | | O | O |✓ | O | O | O |
+|`prebuilt-mortgage.us.1005` | ✓|✓ | | |✓| | | O | O |✓ | O | O | O |
+|`prebuilt-mortgage.us.1008` | ✓|✓ | | |✓| | | O | O |✓ | O | O | O |
+|`prebuilt-mortgage.us.closingDisclosure` | ✓|✓ | | |✓| | | O | O |✓ | O | O | O |
+|`prebuilt-tax.us`|✓|✓| | |✓| | |O|O|✓|O|O|O|
+|`prebuilt-tax.us.w2`|✓|✓| | |✓| | |O|O|✓|O|O|O|
+|`prebuilt-tax.us.w4`|✓|✓| | | | | |O|O|✓|O|O|O|
+|`prebuilt-tax.us.1040` (various) | ✓|✓ | | |✓| | | O | O |✓ | O | O | O |
+|`prebuilt-tax.us.1095A`|✓|✓| | | | | |O|O|✓|O|O|O|
+|`prebuilt-tax.us.1095C`|✓|✓| | | | | |O|O|✓|O|O|O|
+|`prebuilt-tax.us.1098`|✓|✓| | |✓| | |O|O|✓|O|O|O|
+|`prebuilt-tax.us.1098E`|✓|✓| | |✓| | |O|O|✓|O|O|O|
+|`prebuilt-tax.us.1098T`|✓|✓| | |✓| | |O|O|✓|O|O|O|
+|`prebuilt-tax.us.1099` (various)|✓|✓| | |✓| | |O|O|✓|O|O|O|
+|`prebuilt-tax.us.1099SSA`|✓|✓| | | | | |O|O|✓|O|O|O|
+|`{ customModelName }`|✓|✓|✓|✓|✓|✓| |O|O|✓|O|O|O|
 
 ✓ - Enabled</br>
 O - Optional</br>
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル分析機能に関する表の更新"
}
```

### Explanation
このコードの変更には、ドキュメントインテリジェンスのモデル分析機能に関する表の内容が更新されました。具体的には、表内の見出しがより明確に修正され、項目の表記が統一されました。また、各モデルの機能を示すマークが再調整され、表全体の可読性と理解のしやすさが向上しました。特に、パラメータ名や入力オプションの表記における小さな変更が行われ、文書の整合性が保たれています。この改善により、ユーザーは異なるモデルの機能を簡単に比較し、必要な情報を迅速に見つけることができるようになっています。全体として、この更新はモデル分析機能の利用を促進し、ユーザーエクスペリエンスを向上させることを目的としています。

## articles/ai-services/document-intelligence/model-overview.md{#item-768c0d}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: Document processing models - Document Intelligence
+title: Document Processing Models - Document Intelligence
 titleSuffix: Azure AI services
-description: Document processing models for OCR, document layout, invoices, identity, custom  models, and more to extract text, structure, and key-value pairs.
+description: Document processing models for OCR, document layout, invoices, identity, custom models, and more to extract text, structure, and key/value pairs.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
@@ -37,154 +37,151 @@ ms.custom: sfi-image-nochange
 ::: moniker-end
 
 ::: moniker range=">=doc-intel-2.1.0"
- Azure AI Document Intelligence supports a wide variety of models that enable you to add intelligent document processing to your apps and flows. You can use a prebuilt domain-specific model or train a custom model tailored to your specific business needs and use cases. Document Intelligence can be used with the REST API or Python, C#, Java, and JavaScript client libraries.
+ Azure AI Document Intelligence supports various models that you can use to add intelligent document processing to your apps and flows. You can use a prebuilt domain-specific model or train a custom model tailored to your specific business needs and use cases. You can use Document Intelligence with the REST API or Python, C#, Java, and JavaScript client libraries.
 ::: moniker-end
 
 > [!NOTE]
 >
-> * Document processing projects that involve financial data, protected health data, personal data, or highly sensitive data require careful attention.
-> * Be sure to comply with all [national/regional and industry-specific requirements](https://azure.microsoft.com/resources/microsoft-azure-compliance-offerings/).
+> Document processing projects that involve financial data, protected health data, personal data, or highly sensitive data require careful attention. Be sure to comply with all [national/regional and industry-specific requirements](https://azure.microsoft.com/resources/microsoft-azure-compliance-offerings/).
 
 ## Model overview
 
-The following table shows the available models for each stable API:
+The following table shows the generally available (GA) models for each stable API.
 
-|**Model Type**| **Model**|[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)|[2023-07-31 (GA)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)|[2022-08-31 (GA)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)|[v2.1 (GA)](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)|
+|Model type| Model|[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)|[2023-07-31 (GA)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)|[2022-08-31 (GA)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)|[v2.1 (GA)](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)|
 |----------------|-----------|---|--|---|---|
-|Document analysis models|[Read](prebuilt/read.md)                                  | ✔️| ✔️| ✔️| n/a|
+|Document analysis models|[Read](prebuilt/read.md)                                  | ✔️| ✔️| ✔️| Not available|
 |Document analysis models|[Layout](prebuilt/layout.md)                              | ✔️| ✔️| ✔️| ✔️|
-|Document analysis models|[** General document](prebuilt/general-document.md)          |**supported in<br>layout model**| ✔️| ✔️| n/a|
-|Prebuilt models|[Bank Check](concept-bank-check.md)   | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[Bank Statement](concept-bank-statement.md)   | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[Paystub](concept-pay-stub.md)   | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[Contract](prebuilt/contract.md)                          | ✔️| ✔️| n/a| n/a|
-|Prebuilt models|[Health insurance card](prebuilt/health-insurance-card.md)| ✔️| ✔️| ✔️| n/a|
+|Document analysis models|[General document**](prebuilt/general-document.md)          |Supported in<br>layout model| ✔️| ✔️| Not available|
+|Prebuilt models|[Bank check](concept-bank-check.md)   | ✔️| Not available| Not available| Not available|
+|Prebuilt models|[Bank statement](concept-bank-statement.md)   | ✔️| Not available| Not available| Not available|
+|Prebuilt models|[payStub](concept-pay-stub.md)   | ✔️| Not available| Not available| Not available|
+|Prebuilt models|[Contract](prebuilt/contract.md)                          | ✔️| ✔️| Not available| Not available|
+|Prebuilt models|[Health insurance card](prebuilt/health-insurance-card.md)| ✔️| ✔️| ✔️| Not available|
 |Prebuilt models|[ID document](prebuilt/id-document.md)                    | ✔️| ✔️| ✔️| ✔️|
 |Prebuilt models|[Invoice](prebuilt/invoice.md)                            | ✔️| ✔️| ✔️| ✔️|
 |Prebuilt models|[Receipt](prebuilt/receipt.md)                            | ✔️| ✔️| ✔️| ✔️|
-|Prebuilt models|[US Unified Tax*](prebuilt/tax-document.md)                   | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[US 1040 Tax*](prebuilt/tax-document.md)                   | ✔️| ✔️| n/a| n/a|
-|Prebuilt models|[US 1095 Tax*](prebuilt/tax-document.md)                    | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[US 1098 Tax*](prebuilt/tax-document.md)                   | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[US 1099 Tax*](prebuilt/tax-document.md)                 | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[US W2 Tax](prebuilt/tax-document.md)                     | ✔️| ✔️| ✔️| n/a|
-|Prebuilt models|[US W4 Tax](prebuilt/tax-document.md)                      | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[US Mortgage 1003 URLA](concept-mortgage-documents.md)    | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[US Mortgage 1004 URAR](concept-mortgage-documents.md)    | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[US Mortgage 1005](concept-mortgage-documents.md)    | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[US Mortgage 1008 Summary](concept-mortgage-documents.md)       | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[US Mortgage closing disclosure](concept-mortgage-documents.md)   | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[Marriage certificate](concept-marriage-certificate.md)   | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[Credit card](concept-credit-card.md)   | ✔️| n/a| n/a| n/a|
+|Prebuilt models|[US unified tax*](prebuilt/tax-document.md)                   | ✔️| Not available| Not available| Not available|
+|Prebuilt models|[US 1040 tax*](prebuilt/tax-document.md)                   | ✔️| ✔️| Not available| Not available|
+|Prebuilt models|[US 1095 tax*](prebuilt/tax-document.md)                    | ✔️| Not available| Not available| Not available|
+|Prebuilt models|[US 1098 tax*](prebuilt/tax-document.md)                   | ✔️| Not available| Not available| Not available|
+|Prebuilt models|[US 1099 tax*](prebuilt/tax-document.md)                 | ✔️| Not available| Not available| Not available|
+|Prebuilt models|[US W2 tax](prebuilt/tax-document.md)                     | ✔️| ✔️| ✔️| Not available|
+|Prebuilt models|[US W4 tax](prebuilt/tax-document.md)                      | ✔️| Not available| Not available| Not available|
+|Prebuilt models|[US mortgage 1003 URLA](concept-mortgage-documents.md)    | ✔️| Not available| Not available| Not available|
+|Prebuilt models|[US mortgage 1004 URAR](concept-mortgage-documents.md)    | ✔️| Not available| Not available| Not available|
+|Prebuilt models|[US mortgage 1005](concept-mortgage-documents.md)    | ✔️| Not available| Not available| Not available|
+|Prebuilt models|[US mortgage 1008 summary](concept-mortgage-documents.md)       | ✔️| Not available| Not available| Not available|
+|Prebuilt models|[US mortgage closing disclosure](concept-mortgage-documents.md)   | ✔️| Not available| Not available| Not available|
+|Prebuilt models|[Marriage certificate](concept-marriage-certificate.md)   | ✔️| Not available| Not available| Not available|
+|Prebuilt models|[Credit card](concept-credit-card.md)   | ✔️| Not available| Not available| Not available|
 |Prebuilt models|[Business card](concept-business-card.md)                | deprecated|✔️|✔️|✔️ |
-|Custom classification model|[Custom classifier](train/custom-classifier.md)        | ✔️| ✔️| n/a| n/a|
-|Custom extraction model|[Custom neural](train/custom-neural.md)                | ✔️| ✔️| ✔️| n/a|
+|Custom classification model|[Custom classifier](train/custom-classifier.md)        | ✔️| ✔️| Not available| Not available|
+|Custom extraction model|[Custom neural](train/custom-neural.md)                | ✔️| ✔️| ✔️| Not available|
 |Custom extraction model|[Custom template](train/custom-template.md)            | ✔️| ✔️| ✔️| ✔️|
 |Custom extraction model|[Custom composed](train/composed-models.md)            | ✔️| ✔️| ✔️| ✔️|
-|All models|[Add-on capabilities](concept-add-on-capabilities.md)    | ✔️| ✔️| n/a| n/a|
+|All models|[Add-on capabilities](concept-add-on-capabilities.md)    | ✔️| ✔️| Not available| Not available|
 
-\* Contains submodels. See the model specific information for supported variations and subtypes.</br>
-\** All the General Document model capabilities are available in layout model. General model is no longer supported. 
+\* Contains submodels. See the model-specific information for supported variations and subtypes.</br>
+\** All the capabilities for the general document model are available in the layout model. The general model is no longer supported.
 
 ### Latency
 
-Latency is the amount of time it takes for an API server to handle and process an incoming request and deliver the outgoing response to the client. The time to analyze a document depends on the size (for example, number of pages) and associated content on each page. Document Intelligence is a multitenant service where latency for similar documents is comparable but not always identical. Occasional variability in latency and performance is inherent in any microservice-based, stateless, asynchronous service that processes images and large documents at scale. Although we're continuously scaling up the hardware and capacity and scaling capabilities, you might still have latency issues at runtime.
+Latency is the amount of time it takes for an API server to handle and process an incoming request and deliver the outgoing response to the client. The time to analyze a document depends on the size (for example, number of pages) and associated content on each page. Document Intelligence is a multitenant asynchronous service where latency for similar documents is comparable but not always identical. Occasional variability in latency and performance is inherent in any microservice-based, stateless service that processes images and large documents at scale. Although we're continuously scaling up the hardware and capacity and scaling capabilities, you might still have latency issues at runtime.
 
-### Add-on Capability
+### Add-on capability
 
-Following are the add-on capability available in document intelligence. For all models, except Business card model, Document Intelligence now supports add-on capabilities to allow for more sophisticated analysis. These optional capabilities can be enabled and disabled depending on the scenario of the document extraction. There are seven add-on capabilities available for the `2023-07-31` (GA) and later API version:
+The following add-on capabilities are available for Document Intelligence. For all models except the business card model, Document Intelligence now supports add-on capabilities to allow for more sophisticated analysis. You can enable and disable these optional capabilities depending on the scenario of the document extraction. The following add-on capabilities are available for the 2023-07-31 (GA) and later API version:
 
 * [`ocrHighResolution`](concept-add-on-capabilities.md#high-resolution-extraction)
 * [`formulas`](concept-add-on-capabilities.md#formula-extraction)
 * [`styleFont`](concept-add-on-capabilities.md#font-property-extraction)
 * [`barcodes`](concept-add-on-capabilities.md#barcode-property-extraction)
 * [`languages`](concept-add-on-capabilities.md#language-detection)
-* [`keyValuePairs`](concept-add-on-capabilities.md#key-value-pairs)
-* [`queryFields`](concept-add-on-capabilities.md#query-fields)  `Not available with the US.Tax models`
-* [`searchablePDF`](prebuilt/read.md#searchable-pdf)  `Only available for Read Model`
+* [`keyValuePairs`](concept-add-on-capabilities.md#`value-pairs)
+* [`queryFields`](concept-add-on-capabilities.md#query-fields) (not available with the US tax models)
+* [`searchablePDF`](prebuilt/read.md#searchable-pdf) (available only for the read model)
 
-|**Add-on Capability**| **Add-On/Free**|&bullet; **2024-11-30 (GA)**|[`2023-07-31` (GA)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)|[`2022-08-31` (GA)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)|[v2.1 (GA)](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)|
+|Add-on capability| Add-on/Free|2024-11-30 (GA)|[2023-07-31 (GA)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)|[2022-08-31 (GA)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)|[v2.1 (GA)](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)|
 |----------------|-----------|---|--|---|---|
-|Font property extraction|Add-On| ✔️| ✔️| n/a| n/a|
-|Formula extraction|Add-On| ✔️| ✔️| n/a| n/a|
-|High resolution extraction|Add-On| ✔️| ✔️| n/a| n/a|
-|Barcode extraction|Free| ✔️| ✔️| n/a| n/a|
-|Language detection|Free| ✔️| ✔️| n/a| n/a|
-|Key value pairs|Free| ✔️|n/a|n/a| n/a|
-|Query fields|Add-On*| ✔️|n/a|n/a| n/a|
-|Searchable pdf|Add-On*| ✔️|n/a|n/a| n/a|
+|Font property extraction|Add-on| ✔️| ✔️| Not available| Not available|
+|Formula extraction|Add-on| ✔️| ✔️| Not available| Not available|
+|High-resolution extraction|Add-on| ✔️| ✔️| Not available| Not available|
+|Barcode extraction|Free| ✔️| ✔️| Not available| Not available|
+|Language detection|Free| ✔️| ✔️| Not available| Not available|
+|Key/value pairs|Free| ✔️|Not available|Not available| Not available|
+|Query fields|Add-on*| ✔️|Not available|Not available| Not available|
+|Searchable PDF|Add-on*| ✔️|Not available|Not available| Not available|
 
 ### Model analysis features
 
 [!INCLUDE [model analysis features](includes/model-analysis-features.md)]
 
-Add-On* - Query fields are priced differently than the other add-on features. See [pricing](https://azure.microsoft.com/pricing/details/ai-document-intelligence/) for details.
+Query fields are priced differently from the other add-on features. For more information, see [Pricing](https://azure.microsoft.com/pricing/details/ai-document-intelligence/).
 
 ::: moniker range=">=doc-intel-3.0.0"
 
 ### Bounding box and polygon coordinates
 
-A bounding box (`polygon` in v3.0 and later versions) is an abstract rectangle that surrounds text elements in a document used as a reference point for object detection.
+A bounding box (`polygon` in v3.0 and later versions) is an abstract rectangle that surrounds text elements in a document. A bounding box is used as a reference point for object detection:
 
 * The bounding box specifies position by using an x and y coordinate plane presented in an array of four numerical pairs. Each pair represents a corner of the box in the following order: upper left, upper right, lower right, lower left.
-
 * Image coordinates are presented in pixels. For a PDF, coordinates are presented in inches.
 
 ## Language support
 
-The deep-learning-based universal models in Document Intelligence support many languages that can extract multilingual text from your images and documents, including text lines with mixed languages.
-Language support varies by Document Intelligence service functionality. For a complete list, see the following articles:
+The universal models in Document Intelligence that are based on deep learning support many languages. The models can extract multilingual text from your images and documents, including text lines with mixed languages. Language support varies by Document Intelligence service functionality. For a complete list, see the following articles:
 
-* [Language support: document analysis models](language-support/ocr.md)
-* [Language support: prebuilt models](language-support/prebuilt.md)
-* [Language support: custom models](language-support/custom.md)
+* [Language support: Document analysis models](language-support/ocr.md)
+* [Language support: Prebuilt models](language-support/prebuilt.md)
+* [Language support: Custom models](language-support/custom.md)
 
 ## Regional availability
 
 Document Intelligence is generally available in many of the [60+ Azure global infrastructure regions](https://azure.microsoft.com/global-infrastructure/services/?products=metrics-advisor&regions=all#select-product).
 
-For more information, see our [Azure geographies](https://azure.microsoft.com/global-infrastructure/geographies/#overview) page to help choose the region that's best for you and your customers.
+To help choose the region that's best for you and your customers, see [Azure geographies](https://azure.microsoft.com/global-infrastructure/geographies/#overview).
 
 ## Model details
 
-This section describes the output you can expect from each model. You can extend the output of most models with add-on features.
+This section describes the output that you can expect from each model. You can extend the output of most models with add-on features.
 
 ### Read OCR
 
 :::image type="icon" source="media/studio/read-card.png" :::
 
-The Read API analyzes and extracts lines, words, their locations, detected languages, and handwritten style if detected.
+The Read API uses optical character recognition (OCR) to analyze and extract lines and words, their locations, detected languages, and handwriting style, if detected.
 
-***Sample document processed using the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/read)***:
+This sample document was processed by using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/read).
 
-:::image type="content" source="media/studio/form-recognizer-studio-read-v3p2.png" alt-text="Screenshot of Screenshot of sample document processed using Document Intelligence Studio Read":::
+:::image type="content" source="media/studio/form-recognizer-studio-read-v3p2.png" alt-text="Screenshot that shows a sample document processed by using Document Intelligence Studio Read.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: read model](prebuilt/read.md)
+> [Learn more: Read model](prebuilt/read.md)
 
 ### Layout analysis
 
 :::image type="icon" source="media/studio/layout.png":::
 
-The Layout analysis model analyzes and extracts text, tables, selection marks, and other structure elements like titles, section headings, page headers, page footers, and more.
+The layout analysis model analyzes and extracts text, tables, selection marks, and other structure elements like titles, section headings, page headers, and page footers.
 
-***Sample document processed using the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/layout)***:
+This sample document was processed by using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/layout).
 
-:::image type="content" source="media/studio/form-recognizer-studio-layout-newspaper.png" alt-text="Screenshot of sample newspaper page processed using Document Intelligence Studio.":::
+:::image type="content" source="media/studio/form-recognizer-studio-layout-newspaper.png" alt-text="Screenshot that shows a sample newspaper page processed by using Document Intelligence Studio.":::
 
 > [!div class="nextstepaction"]
 >
-> [Learn more: layout model](prebuilt/layout.md)
+> [Learn more: Layout model](prebuilt/layout.md)
 
 ### Health insurance card
 
 :::image type="icon" source="media/studio/health-insurance-logo.png":::
 
-The health insurance card model combines powerful Optical Character Recognition (OCR) capabilities with deep learning models to analyze and extract key information from US health insurance cards.
+The health insurance card model combines powerful OCR capabilities with deep learning models to analyze and extract key information from US health insurance cards.
 
-***Sample US health insurance card processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=healthInsuranceCard.us)***:
+This sample US health insurance card was processed by using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=healthInsuranceCard.us).
 
-:::image type="content" source="./media/studio/analyze-health-card.png" alt-text="Screenshot of a sample US health insurance card analysis in Document Intelligence Studio." lightbox="./media/studio/analyze-health-card.png":::
+:::image type="content" source="./media/studio/analyze-health-card.png" alt-text="Screenshot that shows a sample US health insurance card analysis in Document Intelligence Studio." lightbox="./media/studio/analyze-health-card.png":::
 
 > [!div class="nextstepaction"]
 > [Learn more: Health insurance card model](prebuilt/health-insurance-card.md)
@@ -193,20 +190,20 @@ The health insurance card model combines powerful Optical Character Recognition
 
 :::image type="icon" source="media/studio/tax-documents.png":::
 
-The US tax document models analyze and extract key fields and line items from a select group of tax documents. The API supports the analysis of English-language US tax documents of various formats and quality including phone-captured images, scanned documents, and digital PDFs. The following models are currently supported:
+The US tax document models analyze and extract key fields and line items from a select group of tax documents. The API supports the analysis of English-language US tax documents of various formats and quality, including phone-captured images, scanned documents, and digital PDFs. The following models are currently supported:
 
-  |Model|Description|ModelID|
+  |Model|Description|Model ID|
   |---|---|---|
-  |US Tax W-2|Extract taxable compensation details.|**prebuilt-tax.us.w2**|
-  |US Tax W-4|Extract taxable compensation details.|**prebuilt-tax.us.w4**|
-  |US Tax 1040|Extract mortgage interest details.|**prebuilt-tax.us.1040(variations)**|
-  |US Tax 1095|Extract health insurance details.|**prebuilt-tax.us.1095(variations)**|
-  |US Tax 1098|Extract mortgage interest details.|**prebuilt-tax.us.1098(variations)**|
-  |US Tax 1099|Extract income received from sources other than employer.|**prebuilt-tax.us.1099(variations)**|
+  |US tax W-2|Extract taxable compensation details.|`prebuilt-tax.us.w2`|
+  |US tax W-4|Extract taxable compensation details.|`prebuilt-tax.us.w4`|
+  |US tax 1040|Extract mortgage interest details.|`prebuilt-tax.us.1040` (variations)|
+  |US tax 1095|Extract health insurance details.|`prebuilt-tax.us.1095` (variations)|
+  |US tax 1098|Extract mortgage interest details.|`prebuilt-tax.us.1098` (variations)|
+  |US tax 1099|Extract income received from sources other than employer.|`prebuilt-tax.us.1099` (variations)|
 
-***Sample W-2 document processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=tax.us.w2)***:
+This sample W-2 document was processed by using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=tax.us.w2).
 
-:::image type="content" source="./media/studio/w-2.png" alt-text="Screenshot of a sample W-2.":::
+:::image type="content" source="./media/studio/w-2.png" alt-text="Screenshot that shows a sample W-2 document.":::
 
 > [!div class="nextstepaction"]
 > [Learn more: Tax document models](prebuilt/tax-document.md)
@@ -216,20 +213,19 @@ The US tax document models analyze and extract key fields and line items from a
 
 :::image type="icon" source="media/studio/mortgage-documents.png":::
 
-The US mortgage document models analyze and extract key fields including borrower, loan, and property information from a select group of mortgage documents. The API supports the analysis of English-language US mortgage documents of various formats and quality including phone-captured images, scanned documents, and digital PDFs. The following models are currently supported:
+The US mortgage document models analyze and extract key fields that include borrower, loan, and property information from a select group of mortgage documents. The API supports the analysis of English-language US mortgage documents of various formats and quality, including phone-captured images, scanned documents, and digital PDFs. The following models are currently supported.
 
-  |Model|Description|ModelID|
+  |Model|Description|Model ID|
   |---|---|---|
-  |1003 End-User License Agreement (EULA)|Extract loan, borrower, property details.|**prebuilt-mortgage.us.1003**|
-  |1004 Uniform Residential Appraisal Report (URAR))|Extract loan, borrower, property details.|**prebuilt-mortgage.us.1004**|
-  |1005 Verification of Employment|Extract loan, borrower, property details.|**prebuilt-mortgage.us.1005**|
-  |1008 Summary document|Extract borrower, seller, property, mortgage, and underwriting details.|**prebuilt-mortgage.us.1008**|
-  |Closing disclosure|Extract closing, transaction costs, and loan details.|**prebuilt-mortgage.us.closingDisclosure**|
- 
+  |1003 End-User License Agreement|Extract loan, borrower, property details.|`prebuilt-mortgage.us.1003`|
+  |1004 Uniform Residential Appraisal Report (URAR)|Extract loan, borrower, property details.|`prebuilt-mortgage.us.1004`|
+  |1005 Verification of employment|Extract loan, borrower, property details.|`prebuilt-mortgage.us.1005`|
+  |1008 Summary document|Extract borrower, seller, property, mortgage, and underwriting details.|`prebuilt-mortgage.us.1008`|
+  |Closing Disclosure|Extract closing, transaction costs, and loan details.|`prebuilt-mortgage.us.closingDisclosure`|
 
-***Sample Closing disclosure document processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=mortgage.us.closingDisclosure)***:
+This sample Closing Disclosure document was processed by using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=mortgage.us.closingDisclosure).
 
-:::image type="content" source="./media/studio/closing-disclosure.png" alt-text="Screenshot of a sample closing disclosure.":::
+:::image type="content" source="./media/studio/closing-disclosure.png" alt-text="Screenshot that shows a sample closing disclosure.":::
 
 > [!div class="nextstepaction"]
 > [Learn more: Mortgage document models](concept-mortgage-documents.md)
@@ -238,287 +234,286 @@ The US mortgage document models analyze and extract key fields including borrowe
 
 :::image type="icon" source="media/overview/icon-contract.png":::
 
- The contract model analyzes and extracts key fields and line items from contractual agreements including parties, jurisdictions, contract ID, and title. The model currently supports English-language contract documents.
+ The contract model analyzes and extracts key fields and line items from contractual agreements, including parties, jurisdictions, contract ID, and title. The model currently supports English-language contract documents.
 
-***Sample contract processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=contract)***:
+This sample contract was processed by using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=contract).
 
-:::image type="content" source="media/studio/analyze-contract.png" alt-text="Screenshot of contract model extraction using Document Intelligence Studio.":::
+:::image type="content" source="media/studio/analyze-contract.png" alt-text="Screenshot that shows contract model extraction using Document Intelligence Studio.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: contract model](prebuilt/contract.md)
+> [Learn more: Contract model](prebuilt/contract.md)
 
-### US Bank Check
+### US bank check
 
 :::image type="icon" source="media/overview/icon-contract.png":::
 
- The contract model analyzes and extracts key fields from check including check details, account details, amount, memo, is extracted from US bank checks.
- 
-***A bank check sample processed using [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=check.us)***:
+ The contract model analyzes and extracts key fields from US bank checks, including check details, account details, amount, and memo.
+
+This bank check sample was processed by using [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=check.us).
 
-:::image type="content" source="media/studio/analyze-bank-check.png" alt-text="Screenshot of bank check model extraction using Document Intelligence Studio.":::
+:::image type="content" source="media/studio/analyze-bank-check.png" alt-text="Screenshot that shows bank check model extraction by using Document Intelligence Studio.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: contract model](prebuilt/bank-check.md)
+> [Learn more: Contract model](prebuilt/bank-check.md)
 
-### US Bank Statement
+### US bank statement
 
 :::image type="icon" source="media/overview/icon-contract.png":::
 
  The bank statement model analyzes and extracts key fields and line items from US bank statements account number, bank details, statement details, and transaction details.
 
-***Sample bank statement processed using [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=bankStatement.us)***:
+This sample bank statement was processed by using [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=bankStatement.us).
 
-:::image type="content" source="media/studio/analyze-bank-statement.png" alt-text="Screenshot of bank statement model extraction using Document Intelligence Studio.":::
+:::image type="content" source="media/studio/analyze-bank-statement.png" alt-text="Screenshot that shows bank statement model extraction by using Document Intelligence Studio.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: contract model](prebuilt/bank-statement.md)
+> [Learn more: Contract model](prebuilt/bank-statement.md)
 
-### PayStub
+### payStub
 
 :::image type="icon" source="media/overview/icon-contract.png":::
 
- The paystub model analyzes and extracts key fields and line items from documents and files with payroll related information.
+ The payStub model analyzes and extracts key fields and line items from documents and files with payroll-related information.
 
-***Sample paystub processed using [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=payStub.us)***:
+This sample pay stub was processed by using [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=payStub.us).
 
-:::image type="content" source="media/studio/analyze-pay-stub.png" alt-text="Screenshot of pay stub model extraction using Document Intelligence Studio.":::
+:::image type="content" source="media/studio/analyze-pay-stub.png" alt-text="Screenshot that shows payStub model extraction by using Document Intelligence Studio.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: contract model](prebuilt/pay-stub.md)
+> [Learn more: Contract model](prebuilt/pay-stub.md)
 
 ### Invoice
 
 :::image type="icon" source="media/studio/invoice.png":::
 
-The invoice model automates processing of invoices to extracts customer name, billing address, due date, and amount due, line items, and other key data. 
+The invoice model automates the processing of invoices to extract the customer name, billing address, due date, amount due, line items, and other key data.
 
-***Sample invoice processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=invoice)***:
+This sample invoice was processed by using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=invoice).
 
-:::image type="content" source="./media/studio/analyze-invoice.png" alt-text="Screenshot of a sample invoice." lightbox="./media/overview-invoices.jpg":::
+:::image type="content" source="./media/studio/analyze-invoice.png" alt-text="Screenshot that shows a sample invoice." lightbox="./media/overview-invoices.jpg":::
 
 > [!div class="nextstepaction"]
-> [Learn more: invoice model](prebuilt/invoice.md)
+> [Learn more: Invoice model](prebuilt/invoice.md)
 
 ### Receipt
 
 :::image type="icon" source="media/studio/receipt.png":::
 
-Use the receipt model to scan sales receipts for merchant name, dates, line items, quantities, and totals from printed and handwritten receipts. The version v3.0 also supports single-page hotel receipt processing.
+Use the receipt model to scan sales receipts for the merchant name, dates, line items, quantities, and totals from printed and handwritten receipts. Version v3.0 also supports single-page hotel receipt processing.
 
-***Sample receipt processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=receipt)***:
+This sample receipt was processed by using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=receipt).
 
-:::image type="content" source="./media/studio/analyze-receipt.png" alt-text="Screenshot of a sample receipt." lightbox="./media/overview-receipt.jpg":::
+:::image type="content" source="./media/studio/analyze-receipt.png" alt-text="Screenshot that shows a sample receipt." lightbox="./media/overview-receipt.jpg":::
 
 > [!div class="nextstepaction"]
-> [Learn more: receipt model](prebuilt/receipt.md)
+> [Learn more: Receipt model](prebuilt/receipt.md)
 
-### Identity document (ID)
+### Identity document
 
 :::image type="icon" source="media/studio/id-document.png":::
 
-Use the Identity document (ID) model to process U.S. Driver's Licenses (all 50 states and District of Columbia) and biographical pages from international passports (excluding visa and other travel documents) to extract key fields.
+Use the identity document (ID) model to process US driver's licenses (all 50 states and District of Columbia) and biographical pages from international passports (excluding visa and other travel documents) to extract key fields.
 
-***Sample U.S. Driver's License processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=idDocument)***:
+This sample US driver's license was processed by using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=idDocument).
 
-:::image type="content" source="./media/studio/analyze-drivers-license.png" alt-text="Screenshot of a sample identification card." lightbox="./media/overview-id.jpg":::
+:::image type="content" source="./media/studio/analyze-drivers-license.png" alt-text="Screenshot that shows a sample identification card." lightbox="./media/overview-id.jpg":::
 
 > [!div class="nextstepaction"]
-> [Learn more: identity document model](prebuilt/id-document.md)
+> [Learn more: Identity document model](prebuilt/id-document.md)
 
 ### Marriage certificate
 
 :::image type="icon" source="media/studio/marriage-certificate-icon.png":::
 
-Use the marriage certificate model to process U.S. marriage certificates to extract key fields including the individuals, date, and location.
+Use the marriage certificate model to process US marriage certificates to extract key fields, including the individuals, date, and location.
 
-***Sample U.S. marriage certificate processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=marriageCertificate.us)***:
+This sample US marriage certificate was processed by using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=marriageCertificate.us).
 
-:::image type="content" source="./media/studio/marriage-certificate.png" alt-text="Screenshot of a sample marriage certificate." lightbox="./media/studio/marriage-certificate.png":::
+:::image type="content" source="./media/studio/marriage-certificate.png" alt-text="Screenshot that shows a sample marriage certificate." lightbox="./media/studio/marriage-certificate.png":::
 
 > [!div class="nextstepaction"]
-> [Learn more: identity document model](concept-marriage-certificate.md)
+> [Learn more: Identity document model](concept-marriage-certificate.md)
 
 ### Credit card
 
 :::image type="icon" source="media/studio/credit-card-icon.png":::
 
 Use the credit card model to process credit and debit cards to extract key fields.
 
-***Sample credit card processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=creditCard)***:
+This sample credit card was processed by using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=creditCard).
 
-:::image type="content" source="./media/studio/credit-card.png" alt-text="Screenshot of a sample credit card." lightbox="./media/studio/credit-card.png":::
+:::image type="content" source="./media/studio/credit-card.png" alt-text="Screenshot that shows a sample credit card." lightbox="./media/studio/credit-card.png":::
 
 > [!div class="nextstepaction"]
-> [Learn more: identity document model](concept-credit-card.md)
+> [Learn more: Identity document model](concept-credit-card.md)
 
 ### Custom models
 
 :::image type="icon" source="media/studio/custom.png":::
 
-Custom models can be broadly classified into two types. Custom classification models that support classification of a "document type" and custom extraction models that can extract a defined schema from a specific document type.
+Custom models are broadly classified into two types. Custom classification models that support classification of a "document type" and custom extraction models that can extract a defined schema from a specific document type.
 
-:::image type="content" source="media/custom-models.png" alt-text="Diagram of types of custom models and associated model build modes.":::
+:::image type="content" source="media/custom-models.png" alt-text="Diagram that shows types of custom models and associated model build modes.":::
 
-Custom document models analyze and extract data from forms and documents specific to your business. They recognize form fields within your distinct content and extract key-value pairs and table data. You only need one example of the form type to get started.
+Custom document models analyze and extract data from forms and documents specific to your business. They recognize form fields within your distinct content and extract key/value pairs and table data. You need only one example of the form type to get started.
 
 Version v3.0 and later custom models support signature detection in custom template (form) and cross-page tables in both template and neural models. [Signature detection](train/custom-template.md#model-capabilities) looks for the presence of a signature, not the identity of the person who signs the document. If the model returns **unsigned** for signature detection, the model didn't find a signature in the defined field.
 
-***Sample custom template processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/customform/projects)***:
+This sample custom template was processed by using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/customform/projects).
 
-:::image type="content" source="media/studio/train-model.png" alt-text="Screenshot of Document Intelligence tool analyze-a-custom-form window.":::
+:::image type="content" source="media/studio/train-model.png" alt-text="Screenshot that shows Document Intelligence analyzing a custom form.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: custom model](train/custom-model.md)
+> [Learn more: Custom model](train/custom-model.md)
 
 #### Custom extraction
 
 :::image type="icon" source="media/studio/custom-extraction.png":::
 
-Custom extraction model can be one of two types, **custom template**, **custom neural**. To create a custom extraction model, label a dataset of documents with the values you want extracted and train the model on the labeled dataset. You only need five examples of the same form or document type to get started.
+The custom extraction model comes in two types: custom template and custom neural. To create a custom extraction model, label a dataset of documents with the values you want extracted and train the model on the labeled dataset. You need only five examples of the same form or document type to get started.
 
-***Sample custom extraction processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/customform/projects)***:
+This sample custom extraction was processed by using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/customform/projects).
 
-:::image type="content" source="media/studio/custom-extraction-models.png" alt-text="Screenshot of custom extraction model analysis in Document Intelligence Studio.":::
+:::image type="content" source="media/studio/custom-extraction-models.png" alt-text="Screenshot that shows custom extraction model analysis in Document Intelligence Studio.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: custom template model](train/custom-template.md)
+> [Learn more: Custom template model](train/custom-template.md)
 
 > [!div class="nextstepaction"]
-> [Learn more: custom neural model](./train/custom-neural.md)
+> [Learn more: Custom neural model](./train/custom-neural.md)
 
 #### Custom classifier
 
 :::image type="icon" source="media/studio/custom-classifier.png":::
 
-The custom classification model enables you to identify the document type before invoking the extraction model. The classification model is available starting with the `2023-07-31 (GA)` API. Training a custom classification model requires at least two distinct classes and a minimum of five samples per class.
+With the custom classification model, you can identify the document type before you invoke the extraction model. The classification model is available starting with the 2023-07-31 (GA) API. Training a custom classification model requires at least two distinct classes and a minimum of five samples per class.
 
 > [!div class="nextstepaction"]
-> [Learn more: custom classification model](train/custom-classifier.md)
+> [Learn more: Custom classification model](train/custom-classifier.md)
 
 #### Composed models
 
-A composed model is created by taking a collection of custom models and assigning them to a single model built from your form types. You can assign multiple custom models to a composed model called with a single model ID. You can assign up to 200 trained custom models to a single composed model.
+A composed model is created by taking a collection of custom models and assigning them to a single model built from your form types. You can assign multiple custom models to a composed model that are called with a single model ID. You can assign up to 200 trained custom models to a single composed model.
 
-***Composed model dialog window in [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/customform/projects)***:
+This sample composed model is in [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/customform/projects).
 
-:::image type="content" source="media/studio/composed-model.png" alt-text="Screenshot of Document Intelligence Studio compose custom model dialog window.":::
+:::image type="content" source="media/studio/composed-model.png" alt-text="Screenshot that shows the Document Intelligence Studio Compose custom model pane.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: custom model](train/custom-model.md)
+> [Learn more: Custom model](train/custom-model.md)
 
 ## Input requirements
 
 [!INCLUDE [input requirements](./includes/input-requirements.md)]
 
 > [!NOTE]
-> The [Sample Labeling tool](https://fott-2-1.azurewebsites.net/) doesn't support the BMP file format. The limitation is derived from the tool not the Document Intelligence Service.
+> The [Sample Labeling tool](https://fott-2-1.azurewebsites.net/) doesn't support the BMP file format. The limitation derives from the tool not the Document Intelligence Service.
 
 ### Version migration
 
-Learn how to use Document Intelligence v3.0 in your applications by following our [**Document Intelligence v3.1 migration guide**](v3-1-migration-guide.md)
+Learn how to use Document Intelligence v3.0 in your applications by following the steps in the [Document Intelligence v3.1 migration guide](v3-1-migration-guide.md).
 
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
 
-| **Model**   | **Description**   |
+| Model   | Description   |
 | --- | --- |
-|**Document analysis**||
+|Document analysis||
 | [Layout](#layout)  | Extract text and layout information from documents.|
-|**Prebuilt**||
-| [Invoice](#invoice)  | Extract key information from English and Spanish invoices.  |
-| [Receipt](#receipt)  | Extract key information from English receipts.  |
-| [ID document](#id-document)  | Extract key information from US driver licenses and international passports.  |
-| [Business card](#business-card)  | Extract key information from English business cards.  |
-|**Custom**||
+|Prebuilt||
+| [Invoice](#invoice)  | Extract key information from English-language and Spanish-language invoices.  |
+| [Receipt](#receipt)  | Extract key information from English-language receipts.  |
+| [ID document](#id-document)  | Extract key information from US driver's licenses and international passports.  |
+| [Business card](#business-card)  | Extract key information from English-language business cards.  |
+|Custom||
 | [Custom](#custom) |  Extract data from forms and documents specific to your business. Custom models are trained for your distinct data and use cases. |
 | [Composed](#composed-custom-model) | Compose a collection of custom models and assign them to a single model built from your form types.|
 
 ### Layout
 
 The Layout API analyzes and extracts text, tables and headers, selection marks, and structure information from documents.
 
-***Sample document processed using the [Sample Labeling tool](https://fott-2-1.azurewebsites.net/layout-analyze)***:
+This sample document was processed by using the [Sample Labeling tool](https://fott-2-1.azurewebsites.net/layout-analyze).
 
-:::image type="content" source="media/overview-layout.png" alt-text="Screenshot of `layout` analysis using the Sample Labeling tool.":::
+:::image type="content" source="media/overview-layout.png" alt-text="Screenshot that shows layout analysis by using the Sample Labeling tool.":::
 
 > [!div class="nextstepaction"]
 >
-> [Learn more: layout model](prebuilt/layout.md)
+> [Learn more: Layout model](prebuilt/layout.md)
 
 ### Invoice
 
 The invoice model analyzes and extracts key information from sales invoices. The API analyzes invoices in various formats and extracts key information such as customer name, billing address, due date, and amount due.
 
-***Sample invoice processed using the [Sample Labeling tool](https://fott-2-1.azurewebsites.net/prebuilts-analyze)***:
+This sample invoice was processed by using the [Sample Labeling tool](https://fott-2-1.azurewebsites.net/prebuilts-analyze).
 
-:::image type="content" source="./media/overview-invoices.jpg" alt-text="Screenshot of a sample invoice analysis using the Sample Labeling tool.":::
+:::image type="content" source="./media/overview-invoices.jpg" alt-text="Screenshot that shows a sample invoice analysis by using the Sample Labeling tool.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: invoice model](prebuilt/invoice.md)
+> [Learn more: Invoice model](prebuilt/invoice.md)
 
 ### Receipt
 
-* The receipt model analyzes and extracts key information from printed and handwritten sales receipts.
+The receipt model analyzes and extracts key information from printed and handwritten sales receipts.
 
-***Sample receipt processed using [Sample Labeling tool](https://fott-2-1.azurewebsites.net/prebuilts-analyze)***:
+This sample receipt was processed by using the [Sample Labeling tool](https://fott-2-1.azurewebsites.net/prebuilts-analyze).
 
-:::image type="content" source="./media/receipts-example.jpg" alt-text="Screenshot of a sample receipt." lightbox="./media/overview-receipt.jpg":::
+:::image type="content" source="./media/receipts-example.jpg" alt-text="Screenshot that shows a sample receipt." lightbox="./media/overview-receipt.jpg":::
 
 > [!div class="nextstepaction"]
-> [Learn more: receipt model](prebuilt/receipt.md)
+> [Learn more: Receipt model](prebuilt/receipt.md)
 
 ### ID document
 
  The ID document model analyzes and extracts key information from the following documents:
 
-* U.S. Driver's Licenses (all 50 states and District of Columbia)
-
-* Biographical pages from international passports (excluding visa and other travel documents). The API analyzes identity documents and extracts
+* US driver's licenses (all 50 states and District of Columbia)
+* Biographical pages from international passports (excluding visa and other travel documents). The API analyzes and extracts identity documents.
 
-***Sample U.S. Driver's License processed using the [Sample Labeling tool](https://fott-2-1.azurewebsites.net/prebuilts-analyze)***:
+This sample US driver's license was processed by using the [Sample Labeling tool](https://fott-2-1.azurewebsites.net/prebuilts-analyze).
 
-:::image type="content" source="./media/id-example-drivers-license.jpg" alt-text="Screenshot of a sample identification card.":::
+:::image type="content" source="./media/id-example-drivers-license.jpg" alt-text="Screenshot that shows a sample identification card.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: identity document model](prebuilt/id-document.md)
+> [Learn more: Identity document model](prebuilt/id-document.md)
 
 ### Business card
 
 The business card model analyzes and extracts key information from business card images.
 
-***Sample business card processed using the [Sample Labeling tool](https://fott-2-1.azurewebsites.net/prebuilts-analyze)***:
+This sample business card was processed by using the [Sample Labeling tool](https://fott-2-1.azurewebsites.net/prebuilts-analyze).
 
-:::image type="content" source="./media/business-card-example.jpg" alt-text="Screenshot of a sample business card.":::
+:::image type="content" source="./media/business-card-example.jpg" alt-text="Screenshot that shows a sample business card.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: business card model](concept-business-card.md)
+> [Learn more: Business card model](concept-business-card.md)
 
 ### Custom
 
-* Custom models analyze and extract data from forms and documents specific to your business. The API is a machine-learning program trained to recognize form fields within your distinct content and extract key-value pairs and table data. You only need five examples of the same form type to get started and your custom model can be trained with or without labeled datasets.
+Custom models analyze and extract data from forms and documents specific to your business. The API is a machine-learning program trained to recognize form fields within your distinct content and extract key/value pairs and table data. You need only five examples of the same form type to get started. You can train your custom model with or without labeled datasets.
 
-***Sample custom model processing using the [Sample Labeling tool](https://fott-2-1.azurewebsites.net/)***:
+This sample custom model was processed by using the [Sample Labeling tool](https://fott-2-1.azurewebsites.net/).
 
-:::image type="content" source="media/overview-custom.jpg" alt-text="Screenshot of Document Intelligence tool analyze-a-custom-form window.":::
+:::image type="content" source="media/overview-custom.jpg" alt-text="Screenshot that shows the Document Intelligence tool analyzing a custom form pane.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: custom model](train/custom-model.md)
+> [Learn more: Custom model](train/custom-model.md)
 
 #### Composed custom model
 
-A composed model is created by taking a collection of custom models and assigning them to a single model built from your form types. You can assign multiple custom models to a composed model called with a single model ID. You can assign up to 100 trained custom models to a single composed model.
+A composed model is created by taking a collection of custom models and assigning them to a single model built from your form types. You can assign multiple custom models to a composed model that are called with a single model ID. You can assign up to 100 trained custom models to a single composed model.
 
-***Composed model dialog window using the [Sample Labeling tool](https://formrecognizer.appliedai.azure.com/studio/customform/projects)***:
+This composed model pane was processed by using the [Sample Labeling tool](https://formrecognizer.appliedai.azure.com/studio/customform/projects).
 
-:::image type="content" source="media/custom-model-compose.png" alt-text="Screenshot of Document Intelligence Studio compose custom model dialog window.":::
+:::image type="content" source="media/custom-model-compose.png" alt-text="Screenshot that shows the Document Intelligence Studio Compose custom model pane.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: custom model](train/custom-model.md)
+> [Learn more: Custom model](train/custom-model.md)
 
 ## Model data extraction
 
-| **Model** | **Text extraction** | **Language detection** | **Selection Marks** | **Tables** | **Paragraphs** | **Paragraph roles** | **Key-Value pairs** | **Fields** |
+| Model | Text extraction | Language detection | Selection marks | Tables | Paragraphs | Paragraph roles | Key/value pairs | Fields |
 |:-----|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
 | [Layout](prebuilt/layout.md#data-extraction)  | ✓  |   | ✓ | ✓ | ✓  | ✓  |  |  |
 | [Invoice](prebuilt/invoice.md#field-extraction)  | ✓ |   | ✓  | ✓ | ✓ |   | ✓ | ✓ |
@@ -532,28 +527,26 @@ A composed model is created by taking a collection of custom models and assignin
 [!INCLUDE [input requirements](./includes/input-requirements.md)]
 
 > [!NOTE]
-> The [Sample Labeling tool](https://fott-2-1.azurewebsites.net/) doesn't support the BMP file format. The limitation is derived from the tool not the Document Intelligence Service.
+> The [Sample Labeling tool](https://fott-2-1.azurewebsites.net/) doesn't support the BMP file format. The limitation derives from the tool not Document Intelligence.
 
 ### Version migration
 
- You can learn how to use Document Intelligence v3.0 in your applications by following our [**Document Intelligence v3.1 migration guide**](v3-1-migration-guide.md)
+ You can learn how to use Document Intelligence v3.0 in your applications by following the steps in the [Document Intelligence v3.1 migration guide](v3-1-migration-guide.md)
 
 ::: moniker-end
 
-## Next steps
+## Related content
 
 ::: moniker range=">=doc-intel-3.0.0"
 
-* Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
-
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Process your own forms and documents with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
+* Finish a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), and then create a document processing app in the development language of your choice.
 
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
 
-* Try processing your own forms and documents with the [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/).
-
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Process your own forms and documents with the [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/).
+* Finish a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true), and then create a document processing app in the development language of your choice.
 
 ::: moniker-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスモデルの概要の更新"
}
```

### Explanation
このコードの変更では、ドキュメントインテリジェンスモデルに関する概要が大幅に更新されました。変更内容には、タイトルや文の表現の修正、記事の可読性向上を目的とした表の形式の統一が含まれています。具体的には、「キー＝バリュー」ペアの表記や、モデル説明内の用語が一貫性を持って整理され、ユーザーが理解しやすくなりました。また、モデルの機能に関する表の内容も詳細に見直され、新しい情報やリンクが追加されることで、現行のAPIやモデル対応状況についての理解が深まるようになっています。このような改善によって、ユーザーはドキュメントインテリジェンスの機能や利用方法をより簡単に把握できるようになり、実際のアプリケーションへの適用がスムーズになります。全体として、ドキュメントインテリジェンスの内容が最新の情報に基づいて整備され、ユーザーエクスペリエンスの向上を意図しています。

## articles/ai-services/document-intelligence/overview.md{#item-4e36ba}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンス概要の更新"
}
```

### Explanation
このコードの変更では、ドキュメントインテリジェンスに関する概要が更新されました。変更内容としては、テキストの追加や削除、表現の明確化が含まれています。具体的には、ドキュメントインテリジェンスの機能や利点に関する説明がより具体的にされ、ユーザーがこのサービスをどう活用できるかを理解しやすくするための情報が強調されています。また、最新の機能や使用例が追加され、全体的にドキュメントの内容が最新の情報に基づいて整理されています。これにより、ユーザーはドキュメントインテリジェンスの概要をより迅速に把握し、自分のアプリケーションにどのように適用するかを考える助けとなることを目的としています。全体として、ユーザーエクスペリエンスの向上が図られています。

## articles/ai-services/document-intelligence/prebuilt/layout.md{#item-f7c4c8}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Document layout analysis - Document Intelligence
 titleSuffix: Azure AI services
-description: Extract text, tables, selections, titles, section headings, page headers, page footers, and more with layout analysis model from Document Intelligence.
+description: Extract text, tables, selections, titles, section headings, page headers, page footers, and more with the layout analysis model from Document Intelligence.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
@@ -13,131 +13,122 @@ ms.author: lajanuar
 <!-- markdownlint-disable MD051 -->
 <!-- markdownlint-disable MD024 -->
 
-# What is Document Intelligence layout model?
+# What is the Document Intelligence layout model?
 
 <!---------------------- v4.0 content ---------------------->
 
 :::moniker range="doc-intel-4.0.0"
 
 [!INCLUDE [applies to v4.0](../includes/applies-to-v40.md)]
 
-Document Intelligence layout model is an advanced machine-learning based document analysis API available in the Document Intelligence cloud. It enables you to take documents in various formats and return structured data representations of the documents. It combines an enhanced version of our powerful [Optical Character Recognition (OCR)](../../../ai-services/computer-vision/overview-ocr.md) capabilities with deep learning models to extract text, tables, selection marks, and document structure.
+The Azure AI Document Intelligence layout model is an advanced document-analysis API based on machine learning. The model is available in the Document Intelligence cloud. You can use it to take documents in various formats and return structured data representations of the documents. The model combines an enhanced version of the powerful [optical character recognition (OCR)](../../../ai-services/computer-vision/overview-ocr.md) capabilities with deep learning models to extract text, tables, selection marks, and document structure.
 
 ## Document structure layout analysis
 
-Document structure layout analysis is the process of analyzing a document to extract regions of interest and their inter-relationships. The goal is to extract text and structural elements from the page to build better semantic understanding models. There are two types of roles in a document layout:
+Document structure layout analysis is the process of analyzing a document to extract regions of interest and their interrelationships. The goal is to extract text and structural elements from the page to build better semantic understanding models. There are two types of roles in a document layout:
 
 * **Geometric roles**: Text, tables, figures, and selection marks are examples of geometric roles.
 * **Logical roles**: Titles, headings, and footers are examples of logical roles of texts.
 
 The following illustration shows the typical components in an image of a sample page.
 
-:::image type="content" source="../media/document-layout-example-new.png" alt-text="Illustration of document layout example.":::
+:::image type="content" source="../media/document-layout-example-new.png" alt-text="Illustration that shows a document layout example.":::
 
 ## Development options
 
-Document Intelligence v4.0: **2024-11-30** (GA) supports the following tools, applications, and libraries:
+Document Intelligence v4.0: 2024-11-30 (GA) supports the following tools, applications, and libraries.
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Layout model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-layout**|
+|Layout model|&bullet; [Document Intelligence Studio](https://documentintelligence.ai.azure.com)</br>&bullet;  [REST API](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)</br>&bullet;  [C# SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [Python SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [Java SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [JavaScript SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|`prebuilt-layout`|
 
 ## Supported languages
 
-See [Language Support—document analysis models](../language-support/ocr.md) for a complete list of supported languages.
+For a complete list of supported languages, see [Language support: Document analysis models](../language-support/ocr.md).
 
 ## Supported file types
 
-Document Intelligence v4.0: **2024-11-30** (GA) layout model supports the following file formats:
+Document Intelligence v4.0: 2024-11-30 (GA) layout model supports the following file formats:
 
-|Model | PDF |Image: </br>`JPEG/JPG`, `PNG`, `BMP`, `TIFF`, `HEIF` | Microsoft Office: </br> Word (`DOCX`), Excel (`XLSX`), PowerPoint (`PPTX`), HTML|
+|Model | PDF |Image: </br>JPEG/JPG, PNG, BMP, TIFF, HEIF | Office: </br> Word (DOCX), Excel (XLS), PowerPoint (PPTX), HTML|
 |--------|:----:|:-----:|:---------------:|
 |Layout          | ✔  | ✔ | ✔  |
 
 ## Input requirements
 
-* For best results, provide one clear photo or high-quality scan per document.
+* **Photos and scans**: For best results, provide one clear photo or high-quality scan per document.
+* **PDFs and TIFFs**: For PDFs and TIFFs, up to 2,000 pages can be processed. (With a free-tier subscription, only the first two pages are processed.)
+* **Password locks**: If your PDFs are password-locked, you must remove the lock before submission.
+* **File size**: The file size for analyzing documents is 500 MB for the paid (S0) tier and 4 MB for the free (F0) tier.
+* **Image dimensions**: The image dimensions must be between 50 pixels x 50 pixels and 10,000 pixels x 10,000 pixels.
+* **Text height**: The minimum height of the text to be extracted is 12 pixels for a 1024 x 768 pixel image. This dimension corresponds to about 8-point text at 150 dots per inch.
+* **Custom model training**: The maximum number of pages for training data is 500 for the custom template model and 50,000 for the custom neural model.
+* **Custom extraction model training**: The total size of training data is 50 MB for the template model and 1 GB for the neural model.
+* **Custom classification model training**: The total size of training data is 1 GB with a maximum of 10,000 pages. For 2024-11-30 (GA), the total size of training data is 2 GB with a maximum of 10,000 pages.
+* **Office file types (DOCX, XLSX, PPTX)**: The maximum string length limit is 8 million characters.
 
-* For PDF and TIFF, up to 2,000 pages can be processed (with a free tier subscription, only the first two pages are processed).
+For more information on model usage, quotas, and service limits, see [Service limits](../service-limits.md).
 
-* If your PDFs are password-locked, you must remove the lock before submission.
+### Get started with the layout model
 
-* The file size for analyzing documents is 500 MB for paid (S0) tier and `4` MB for free (F0) tier.
+See how data, including text, tables, table headers, selection marks, and structure information, is extracted from documents by using Document Intelligence. You need the following resources:
 
-* Image dimensions must be between 50 pixels x 50 pixels and 10,000 pixels x 10,000 pixels.
+* An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services/).
+* A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (F0) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
-* The minimum height of the text to be extracted is 12 pixels for a 1024 x 768 pixel image. This dimension corresponds to about `8` point text at 150 dots per inch (DPI).
+    :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot that shows the keys and endpoint location in the Azure portal.":::
 
-* For custom model training, the maximum number of pages for training data is 500 for the custom template model and 50,000 for the custom neural model.
-
-  * For custom extraction model training, the total size of training data is 50 MB for template model and `1` GB for the neural model.
-
-  * For custom classification model training, the total size of training data is `1` GB  with a maximum of 10,000 pages. For `2024-11-30` (GA), the total size of training data is `2` GB with a maximum of 10,000 pages.
-
-For more information on model usage, quotas, and service limits, *see* [service limits](../service-limits.md).
-
-### Get started with Layout model
-
-See how data, including text, tables, table headers, selection marks, and structure information is extracted from documents using  Document Intelligence. You need the following resources:
-
-* An Azure subscription—you can [create one for free](https://azure.microsoft.com/free/cognitive-services/).
-
-* A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
-
-    :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
-
-After you retrieve your key and endpoint, use the following development options to build and deploy your Document Intelligence applications:
+After you retrieve your key and endpoint, use the following development options to build and deploy your Document Intelligence applications.
 
 ### [REST API](#tab/rest)
 
 * [Document Intelligence REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true&tabs=HTTP&)
-* [How to guide](../how-to-guides/use-sdk-rest-api.md#use-document-intelligence-models)
+* [Get started: Document Intelligence Studio](../how-to-guides/use-sdk-rest-api.md#use-document-intelligence-models)
 
 # [Client libraries](#tab/sdks)
 
-* [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)
-* [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)
-* [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)
-* [**JavaScript**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)
+* [C# SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)
+* [Python SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)
+* [Java SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)
+* [JavaScript](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)
 
 ### [Document Intelligence Studio](#tab/studio)
 
-* [Studio](https://documentintelligence.ai.azure.com/studio)
-* [How-to guide](../quickstarts/get-started-studio.md#authentication-in-studio)
+* [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio)
+* [Get started: Document Intelligence Studio](../quickstarts/get-started-studio.md#authentication-in-document-intelligence-studio)
 
 ---
 
 ## Data extraction
 
-The layout model extracts structural elements from your documents. To follow are descriptions of these structural elements with guidance on how to extract them from your document input:
-
-* [**Pages**](#pages)
-* [**Paragraphs**](#paragraphs)
-* [**Text, lines, and words**](#text-lines-and-words)
-* [**Selection marks**](#selection-marks)
-* [**Tables**](#tables)
-* [**Output response to markdown**](#output-response-to-markdown-format)
-* [**Figures**](#figures)
-* [**Sections**](#sections)
+The layout model extracts structural elements from your documents. The following structural elements are described in the remainder of this article along with guidance on how to extract them from your document input:
 
-Run the sample layout document analysis within [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio), then navigate to the results tab and access the full JSON output.
+* [Pages](#pages)
+* [Paragraphs](#paragraphs)
+* [Text, lines, and words](#text-lines-and-words)
+* [Selection marks](#selection-marks)
+* [Tables](#tables)
+* [Output response to markdown](#output-response-to-markdown-format)
+* [Figures](#figures)
+* [Sections](#sections)
 
-   :::image type="content" source="../media/studio/json-output-tab.png" alt-text="Screenshot of results JSON output tab in the Document Intelligence Studio.":::
+Run the sample layout document analysis within [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio). Then go to the results tab and access the full JSON output.
 
+   :::image type="content" source="../media/studio/json-output-tab.png" alt-text="Screenshot that shows results on the JSON output tab in Document Intelligence Studio.":::
 
 ### Pages
 
-The pages collection is a list of pages within the document. Each page is represented sequentially within the document and includes the orientation angle indicating if the page is rotated and the width and height (dimensions in pixels). The page units in the model output are computed as shown:
+The `pages` collection is a list of pages within the document. Each page is represented sequentially within the document and includes the orientation angle, which indicates if the page is rotated, and the width and height (dimensions in pixels). The page units in the model output are computed as shown in the following table.
 
-| **File format**   | **Computed page unit**   | **Total pages**  |
+| File format   | Computed page unit   | Total pages  |
 | --- | --- | --- |
-|Images (JPEG/JPG, PNG, BMP, HEIF) | Each image = 1 page unit | Total images  |
-|PDF | Each page in the PDF = 1 page unit | Total pages in the PDF |
-|TIFF | Each image in the TIFF = 1 page unit | Total images in the TIFF |
-|Word (DOCX)  | Up to 3,000 characters = 1 page unit, embedded or linked images not supported | Total pages of up to 3,000 characters each |
-|Excel (XLSX)  | Each worksheet = 1 page unit, embedded or linked images not supported | Total worksheets |
-|PowerPoint (PPTX) |  Each slide = 1 page unit, embedded or linked images not supported | Total slides |
-|HTML | Up to 3,000 characters = 1 page unit, embedded or linked images not supported | Total pages of up to 3,000 characters each |
+|Images (JPEG/JPG, PNG, BMP, HEIF) | Each image = 1 page unit. | Total images  |
+|PDF | Each page in the PDF = 1 page unit. | Total pages in the PDF |
+|TIFF | Each image in the TIFF = 1 page unit. | Total images in the TIFF |
+|Word (DOCX)  | Up to 3,000 characters = 1 page unit. Embedded or linked images aren't supported. | Total pages of up to 3,000 characters each |
+|Excel (XLSX)  | Each worksheet = 1 page unit. Embedded or linked images aren't supported. | Total worksheets |
+|PowerPoint (PPTX) |  Each slide = 1 page unit. Embedded or linked images aren't supported. | Total slides |
+|HTML | Up to 3,000 characters = 1 page unit. Embedded or linked images aren't supported. | Total pages of up to 3,000 characters each |
 
 #### [Sample code](#tab/sample-code)
 
@@ -173,11 +164,11 @@ print(f"Page has width: {page.width} and height: {page.height}, measured with un
 
 #### Extract selected pages
 
-For large multi-page documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction.
+For large multipage documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction.
 
 ### Paragraphs
 
-The Layout model extracts all identified blocks of text in the `paragraphs` collection as a top level object under `analyzeResults`. Each entry in this collection represents a text block and ../includes the extracted text as`content`and the bounding `polygon` coordinates. The `span` information points to the text fragment within the top level `content` property that contains the full text from the document.
+The layout model extracts all identified blocks of text in the `paragraphs` collection as a top-level object under `analyzeResults`. Each entry in this collection represents a text block and includes the extracted text as `content` and the bounding `polygon` coordinates. The `spans` information points to the text fragment within the top-level `content` property that contains the full text from the document.
 
 ```json
 
@@ -192,16 +183,18 @@ The Layout model extracts all identified blocks of text in the `paragraphs` coll
 
 #### Paragraph roles
 
-The new machine-learning based page object detection extracts logical roles like titles, section headings, page headers, page footers, and more. The Document Intelligence Layout model assigns certain text blocks in the `paragraphs` collection with their specialized role or type predicted by the model. It's best to use paragraph roles with unstructured documents to help understand the layout of the extracted content for a richer semantic analysis. The following paragraph roles are supported:
+The new page object detection based on machine learning extracts logical roles like titles, section headings, page headers, page footers, and more. The Document Intelligence layout model assigns certain text blocks in the `paragraphs` collection with their specialized role or type predicted by the model.
 
-| **Predicted role**   | **Description**   | **Supported file types** |
+It's best to use paragraph roles with unstructured documents to help understand the layout of the extracted content for a richer semantic analysis. The following paragraph roles are supported.
+
+| Predicted role   | Description   | Supported file types |
 | --- | --- | --- |
-| `title`  | The main headings in the page | pdf, image, docx, pptx, xlsx, html |
-| `sectionHeading`  | One or more subheadings on the page  | pdf, image, docx, xlsx, html |
-| `footnote`  | Text near the bottom of the page  | pdf, image |
-| `pageHeader`  | Text near the top edge of the page  | pdf, image, docx |
-| `pageFooter`  | Text near the bottom edge of the page  | pdf, image, docx, pptx, html |
-| `pageNumber`  | Page number  | pdf, image |
+| `title`  | The main headings on the page | PDF, Image, DOCX, PPTX, XLSX, HTML |
+| `sectionHeading`  | One or more subheadings on the page  | PDF, Image, DOCX, XLSX, HTML |
+| `footnote`  | Text near the bottom of the page  | PDF, Image |
+| `pageHeader`  | Text near the top edge of the page  | PDF, Image, DOCX |
+| `pageFooter`  | Text near the bottom edge of the page  | PDF, Image, DOCX, PPTX, HTML |
+| `pageNumber`  | Page number  | PDF, Image |
 
 ```json
 {
@@ -225,9 +218,9 @@ The new machine-learning based page object detection extracts logical roles like
 
 ### Text, lines, and words
 
-The document layout model in Document Intelligence extracts print and handwritten style text as `lines` and `words`. The `styles` collection includes any handwritten style for lines if detected along with the spans pointing to the associated text. This feature applies to [supported handwritten languages](../language-support/prebuilt.md).
+The document layout model in Document Intelligence extracts print and handwritten-style text as `lines` and `words`. The `styles` collection includes any handwritten style for lines, if detected, along with the spans that point to the associated text. This feature applies to [supported handwritten languages](../language-support/prebuilt.md).
 
-For Microsoft Word, Excel, PowerPoint, and HTML, Document Intelligence v4.0 `2024-11-30` (GA) Layout model extract all embedded text as is. Texts are extracted as words and paragraphs. Embedded images aren't supported.
+For Microsoft Word, Excel, PowerPoint, and HTML, the Document Intelligence v4.0 2024-11-30 (GA) layout model extracts all embedded text as is. Texts are extracted as words and paragraphs. Embedded images aren't supported.
 
 #### [Sample code](#tab/sample-code)
 
@@ -274,7 +267,7 @@ if page.lines:
 
 #### Handwritten style for text lines
 
-The response ../includes classifying whether each text line is of handwriting style or not, along with a confidence score. For more information. See [Handwritten language support](../language-support/ocr.md). The following example shows an example JSON snippet.
+The response includes whether each text line is in a handwritten style or not, along with a confidence score. For more information, see [Handwritten language support](../language-support/ocr.md). The following example shows an example JSON snippet.
 
 ```json
 "styles": [
@@ -290,11 +283,11 @@ The response ../includes classifying whether each text line is of handwriting st
 }
 ```
 
-If you enable the [font/style addon capability](../concept-add-on-capabilities.md#font-property-extraction), you also get the font/style result as part of the `styles` object.
+If you enable the [font/style add-on capability](../concept-add-on-capabilities.md#font-property-extraction), you also get the font/style result as part of the `styles` object.
 
 ### Selection marks
 
-The Layout model also extracts selection marks from documents. Extracted selection marks appear within the `pages` collection for each page. They include the bounding `polygon`, `confidence`, and selection `state` (`selected/unselected`). The text representation (that is, `:selected:` and `:unselected`) is also included as the starting index (`offset`) and `length` that references the top level `content` property that contains the full text from the document.
+The layout model also extracts selection marks from documents. Extracted selection marks appear within the `pages` collection for each page. They include the bounding `polygon`, `confidence`, and selection `state` (`selected/unselected`). The text representation (that is, `:selected:` and `:unselected`) is also included as the starting index (`offset`) and `length` that references the top-level `content` property that contains the full text from the document.
 
 #### [Sample code](#tab/sample-code)
 
@@ -334,22 +327,20 @@ if page.selection_marks:
 
 ### Tables
 
-Extracting tables is a key requirement for processing documents containing large volumes of data typically formatted as tables. The Layout model extracts tables in the `pageResults` section of the JSON output. Extracted table information ../includes the number of columns and rows, row span, and column span. Each cell with its bounding polygon is output along with information whether the area is recognized as a `columnHeader` or not. The model supports extracting tables that are rotated. Each table cell contains the row and column index and bounding polygon coordinates. For the cell text, the model outputs the `span` information containing the starting index (`offset`). The model also outputs the `length` within the top-level content that contains the full text from the document.
+Extracting tables is a key requirement for processing documents that contain large volumes of data typically formatted as tables. The layout model extracts tables in the `pageResults` section of the JSON output. Extracted table information includes the number of columns and rows, row span, and column span.
 
-Here are a few factors to consider when using the Document Intelligence bale extraction capability:
+Each cell with its bounding polygon is output along with information whether the area is recognized as `columnHeader` or not. The model supports extracting tables that are rotated. Each table cell contains the row and column index and bounding polygon coordinates. For the cell text, the model outputs the `span` information that contains the starting index (`offset`). The model also outputs the `length` within the top-level content that contains the full text from the document.
 
-* Is the data that you want to extract presented as a table, and is the table structure meaningful?
+Here are a few factors to consider when you use the Document Intelligence bale extraction capability:
 
+* Is the data that you want to extract presented as a table, and is the table structure meaningful?
 * Can the data fit in a two-dimensional grid if the data isn't in a table format?
-
-* Do your tables span multiple pages? If so, to avoid having to label all the pages, split the PDF into pages before sending it to Document Intelligence. After the analysis, post-process the pages to a single table.
-
-* Refer to [Tabular fields](../train/custom-labels.md#tabular-fields) if you're creating custom models. Dynamic tables have a variable number of rows for each column. Fixed tables have a constant number of rows for each column.
+* Do your tables span multiple pages? If so, to avoid having to label all the pages, split the PDF into pages before you send it to Document Intelligence. After the analysis, post-process the pages to a single table.
+* See [Tabular fields](../train/custom-labels.md#tabular-fields) if you create custom models. Dynamic tables have a variable number of rows for each column. Fixed tables have a constant number of rows for each column.
 
 > [!NOTE]
 >
-> * Table analysis isn't supported if the input file is XLSX.
-> * For `2024-11-30` (GA), the bounding regions for figures and tables cover only the core content and exclude associated caption and footnotes.
+> Table analysis isn't supported if the input file is XLSX. For 2024-11-30 (GA), the bounding regions for figures and tables cover only the core content and exclude the associated caption and footnotes.
 
 #### [Sample code](#tab/sample-code)
 
@@ -399,13 +390,13 @@ if result.tables:
 
 ---
 
-### Output response to markdown format
+### Output response to Markdown format
 
-The Layout API can output the extracted text in markdown format. Use the `outputContentFormat=markdown` to specify the output format in markdown. The markdown content is output as part of the `content` section.
+The layout API can output the extracted text in Markdown format. Use the `outputContentFormat=markdown` to specify the output format in Markdown. The Markdown content is output as part of the `content` section.
 
 > [!NOTE]
->
-> For v4.0 `2024-11-30` (GA), the representation of tables is changed to HTML tables to enable rendering of merged cells, multi-row headers, etc. Another related change is to use Unicode checkbox characters ☒ and ☐ for selection marks instead of `:selected:` and `:unselected:`. This update means that the content of selection mark fields contains `:selected:` even though their spans refer to Unicode characters in the top-level span. Refer to the [Markdown Output Format](../concept/markdown-elements.md) for full definition of Markdown elements.
+> 
+> For v4.0 2024-11-30 (GA), the representation of tables is changed to HTML tables to enable rendering of items like merged cells and multirow headers. Another related change is to use the Unicode checkbox characters ☒ and ☐ for selection marks instead of `:selected:` and `:unselected:`. This update means that the content of selection-mark fields contains `:selected:` even though their spans refer to Unicode characters in the top-level span. For a full definition of Markdown elements, see [Markdown output format](../concept/markdown-elements.md).
 
 #### [Sample code](#tab/sample-code)
 
@@ -472,13 +463,16 @@ PageFooter="1 | Page"
 
 ### Figures
 
-Figures (charts, images) in documents play a crucial role in complementing and enhancing the textual content, providing visual representations that aid in the understanding of complex information. The figures object detected by the Layout model has key properties like `boundingRegions` (the spatial locations of the figure on the document pages, including the page number and the polygon coordinates that outline the figure's boundary), `spans` (details the text spans related to the figure, specifying their offsets and lengths within the document's text. This connection helps in associating the figure with its relevant textual context), `elements` (the identifiers for text elements or paragraphs within the document that are related to or describe the figure) and `caption` if there's any.
+Figures (charts and images) in documents play a crucial role in complementing and enhancing the textual content. They provide visual representations that aid in the understanding of complex information. The `figures` object detected by the layout model has key properties like:
 
-When *output=figures* is specified during the initial analyze operation, the service generates cropped images for all detected figures that can be accessed via `/analyeResults/{resultId}/figures/{figureId}`.
-`FigureId` is included in each figure object, following an undocumented convention of `{pageNumber}.{figureIndex}` where `figureIndex` resets to one per page.
+- `boundingRegions`: The spatial locations of the figure on the document pages, including the page number and the polygon coordinates that outline the figure's boundary.
+- `spans`: The text spans related to the figure that specify their offsets and lengths within the document's text. This connection helps in associating the figure with its relevant textual context.
+- `elements`: The identifiers for text elements or paragraphs within the document that are related to or describe the figure.
+- `caption`: The description if there is one.
 
-> [!NOTE]
-> For v4.0 `2024-11-30` (GA), the bounding regions for figures and tables cover only the core content and exclude associated caption and footnotes.
+When `output=figures` is specified during the initial analyze operation, the service generates cropped images for all detected figures that can be accessed via `/analyeResults/{resultId}/figures/{figureId}`. The `FigureId` value is the ID included in each figure object, following an undocumented convention of `{pageNumber}.{figureIndex}` where `figureIndex` resets to one per page.
+
+For v4.0 2024-11-30 (GA), the bounding regions for figures and tables cover only the core content and exclude the associated caption and footnotes.
 
 #### [Sample code](#tab/sample-code)
 
@@ -526,7 +520,9 @@ if result.figures:
 
 ### Sections
 
-Hierarchical document structure analysis is pivotal in organizing, comprehending, and processing extensive documents. This approach is vital for semantically segmenting long documents to boost comprehension, facilitate navigation, and improve information retrieval. The advent of [retrieval-augmented generation (RAG)](../concept/retrieval-augmented-generation.md) in document generative AI underscores the significance of hierarchical document structure analysis. The Layout model supports sections and subsections in the output, which identifies the relationship of sections and object within each section. The hierarchical structure is maintained in `elements` of each section. You can use [output response to markdown format](#output-response-to-markdown-format) to easily get the sections and subsections in markdown.
+Hierarchical document structure analysis is pivotal in organizing, comprehending, and processing extensive documents. This approach is vital for semantically segmenting long documents to boost comprehension, facilitate navigation, and improve information retrieval. The advent of [retrieval-augmented generation (RAG)](../concept/retrieval-augmented-generation.md) in document-generative AI underscores the significance of hierarchical document structure analysis.
+
+The layout model supports sections and subsections in the output, which identifies the relationship of sections and objects within each section. The hierarchical structure is maintained in `elements` for each section. You can use the [output response to Markdown format](#output-response-to-markdown-format) to easily get the sections and subsections in Markdown.
 
 #### [Sample code](#tab/sample-code)
 
@@ -561,7 +557,7 @@ poller = document_intelligence_client.begin_analyze_document(
 }
 ```
 
-:::image type="content" source="../media/document-layout-example-section.png" alt-text="Screenshot of examples of document sections.":::
+:::image type="content" source="../media/document-layout-example-section.png" alt-text="Screenshot that shows examples of document sections.":::
 
 ---
 
@@ -583,32 +579,32 @@ poller = document_intelligence_client.begin_analyze_document(
 
 :::moniker range="<=doc-intel-3.1.0"
 
-Document Intelligence layout model is an advanced machine-learning based document analysis API available in the Document Intelligence cloud. It enables you to take documents in various formats and return structured data representations of the documents. It combines an enhanced version of our powerful [Optical Character Recognition (OCR)](../../../ai-services/computer-vision/overview-ocr.md) capabilities with deep learning models to extract text, tables, selection marks, and document structure.
+The Document Intelligence layout model is an advanced document-analysis API. The model is based on machine learning and is available in the Document Intelligence cloud. You can use it to take documents in various formats and return structured data representations of the documents. It combines an enhanced version of the powerful [OCR](../../../ai-services/computer-vision/overview-ocr.md) capabilities with deep learning models. You can use it to extract text, tables, selection marks, and document structure.
 
 ## Document layout analysis
 
-Document structure layout analysis is the process of analyzing a document to extract regions of interest and their inter-relationships. The goal is to extract text and structural elements from the page to build better semantic understanding models. There are two types of roles in a document layout:
+Document structure layout analysis is the process of analyzing a document to extract regions of interest and their interrelationships. The goal is to extract text and structural elements from the page to build better semantic understanding models. There are two types of roles in a document layout:
 
 * **Geometric roles**: Text, tables, figures, and selection marks are examples of geometric roles.
 * **Logical roles**: Titles, headings, and footers are examples of logical roles of texts.
 
 The following illustration shows the typical components in an image of a sample page.
 
-:::image type="content" source="../media/document-layout-example-new.png" alt-text="Illustration of document layout example.":::
+:::image type="content" source="../media/document-layout-example-new.png" alt-text="Illustration that shows a document layout example.":::
 
 ## Supported languages and locales
 
-*See* our [Language Support—document analysis models](../language-support/ocr.md) page for a complete list of supported languages.
+For a complete list of supported languages, see [Language support: Document analysis models](../language-support/ocr.md).
 
 :::moniker-end
 
 :::moniker range="doc-intel-2.1.0"
 
-Document Intelligence v2.1 supports the following tools, applications, and libraries:
+Document Intelligence v2.1 supports the following tools, applications, and libraries.
 
 | Feature | Resources |
 |----------|-------------------------|
-|**Layout model**|&bullet; [**Document Intelligence labeling tool**](https://fott-2-1.azurewebsites.net/prebuilts-analyze)</br>&bullet;  [**REST API**](../how-to-guides/use-sdk-rest-api.md?pivots=programming-language-rest-api&view=doc-intel-2.1.0&preserve-view=true&tabs=windows)</br>&bullet;  [**Client-library SDK**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet;  [**Document Intelligence Docker container**](../containers/install-run.md?tabs=id-document#run-the-container-with-the-docker-compose-up-command)|
+|Layout model|&bullet; [Document Intelligence labeling tool](https://fott-2-1.azurewebsites.net/prebuilts-analyze)</br>&bullet;  [REST API](../how-to-guides/use-sdk-rest-api.md?pivots=programming-language-rest-api&view=doc-intel-2.1.0&preserve-view=true&tabs=windows)</br>&bullet;  [Client-library SDK](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet;  [Document Intelligence Docker container](../containers/install-run.md?tabs=id-document#run-the-container-with-the-docker-compose-up-command)|
 
 :::moniker-end
 
@@ -618,83 +614,74 @@ Document Intelligence v2.1 supports the following tools, applications, and libra
 
 Supported file formats:
 
-|Model | PDF |Image: </br>`JPEG/JPG`, `PNG`, `BMP`, `TIFF`, `HEIF` | Microsoft Office: </br> Word (`DOCX`), Excel (`XLSX`), PowerPoint (`PPTX`), HTML|
+|Model | PDF |Image: </br>JPEG/JPG, PNG, BMP, TIFF, HEIF | Office: </br> Word (DOCX), Excel (XLSX), PowerPoint (PPTX), HTML|
 |--------|:----:|:-----:|:---------------:|
 |Read            | ✔    | ✔    | ✔  |
 |Layout          | ✔  | ✔ |   |
-|General&nbsp;Document| ✔  | ✔ |   |
+|General&nbsp;document| ✔  | ✔ |   |
 |Prebuilt        |  ✔  | ✔ |   |
 |Custom extraction |  ✔  | ✔ |   |
 |Custom classification  |  ✔  | ✔ | ✔  |
 
-* For best results, provide one clear photo or high-quality scan per document.
-
-* For PDF and TIFF, up to 2,000 pages can be processed (with a free tier subscription, only the first two pages are processed).
-
-* The file size for analyzing documents is 500 MB for paid (S0) tier and `4` MB for free (F0) tier.
-
-* Image dimensions must be between 50 pixels x 50 pixels and 10,000 pixels x 10,000 pixels.
-
-* If your PDFs are password-locked, you must remove the lock before submission.
-
-* The minimum height of the text to be extracted is 12 pixels for a 1024 x 768 pixel image. This dimension corresponds to about `8` point text at 150 dots per inch (DPI).
-
-* For custom model training, the maximum number of pages for training data is 500 for the custom template model and 50,000 for the custom neural model.
-
-  * For custom extraction model training, the total size of training data is 50 MB for template model and `1` GB for the neural model.
-
-  * For custom classification model training, the total size of training data is `1` GB  with a maximum of 10,000 pages. For `2024-11-30` (GA), the total size of training data is `2` GB with a maximum of 10,000 pages.
+* **Photos and scans**: For best results, provide one clear photo or high-quality scan per document.
+* **PDFs and TIFFs**: For PDFs and TIFFs, up to 2,000 pages can be processed with a free-tier subscription. Only the first two pages are processed.
+* **File size**: The file size for analyzing documents is 500 MB for the paid (S0) tier and 4 MB for the free (F0) tier.
+* **Image dimensions**: The image dimensions must be between 50 pixels x 50 pixels and 10,000 pixels x 10,000 pixels.
+* **Password locks**: If your PDFs are password-locked, you must remove the lock before submission.
+* **Text height**: The minimum height of the text to be extracted is 12 pixels for a 1024 x 768 pixel image. This dimension corresponds to about 8-point text at 150 dots per inch.
+* **Custom model training**: The maximum number of pages for training data is 500 for the custom template model and 50,000 for the custom neural model.
+* **Custom extraction model training**: The total size of training data is 50 MB for the template model and 1 GB for the neural model.
+* **Custom classification model training**: The total size of training data is 1 GB with a maximum of 10,000 pages. For 2024-11-30 (GA), the total size of training data is 2 GB with a maximum of 10,000 pages.
+* **Office file types (DOCX, XLSX, PPTX)**: The maximum string length limit is 8 million characters.
 
 :::moniker-end
 
 :::moniker range="doc-intel-2.1.0"
 
 ## Input guide
 
-* Supported file formats: JPEG, PNG, PDF, and TIFF.
-* Supported number of pages: For PDF and TIFF, up to 2,000 pages are processed. For free tier subscribers, only the first two pages are processed.
-* Supported file size: the file size must be less than 50 MB and dimensions at least 50 x 50 pixels and at most 10,000 x 10,000 pixels.
+* **Supported file formats**: JPEG, PNG, PDF, and TIFF.
+* **Supported number of pages**: For PDF and TIFF, up to 2,000 pages are processed. For free tier subscribers, only the first two pages are processed.
+* **Supported file size**: The file size must be less than 50 MB, and the dimensions must be at least 50 x 50 pixels and at most 10,000 x 10,000 pixels.
 
 :::moniker-end
 
 :::moniker range="<=doc-intel-3.1.0"
 
 ### Get started
 
-See how data, including text, tables, table headers, selection marks, and structure information is extracted from documents using  Document Intelligence. You need the following resources:
-
-* An Azure subscription—you can [create one for free](https://azure.microsoft.com/free/cognitive-services/).
+You can use Document Intelligence to extract data such as text, tables, table headers, selection marks, and structure information from documents. You need the following resources:
 
-* A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
+* An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services/).
+* A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (F0) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
-:::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+:::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot that shows the keys and endpoint location in the Azure portal.":::
 
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
 
-After you retrieve you key and endpoint, you can use the following development options to build and deploy your Document Intelligence applications:
+After you retrieve your key and endpoint, you can use the following development options to build and deploy your Document Intelligence applications.
 
 > [!NOTE]
 > Document Intelligence Studio is available with v3.0 APIs and later versions.
 
 ### [REST API](#tab/rest)
 
-
-* [`2023-07-31` GA (v3.1)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)
-* [`2022-08-31` GA (v3.0)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
+* [2023-07-31` GA (v3.1)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)
+* [2022-08-31` GA (v3.0)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
 
 # [Client libraries](#tab/sdks)
 
-* [**C# SDK**](/dotnet/api/overview/azure/ai.documentintelligence-readme?view=azure-dotnet-preview&preserve-view=true)
-* [**Java SDK**](/java/api/overview/azure/ai-documentintelligence-readme?view=azure-java-preview&preserve-view=true)
-* [**JavaScript**](/javascript/api/overview/azure/ai-document-intelligence-rest-readme?view=azure-node-preview&preserve-view=true)
-* [**Python SDK**](/python/api/overview/azure/ai-documentintelligence-readme?view=azure-python-preview&preserve-view=true)
+* [C# SDK](/dotnet/api/overview/azure/ai.documentintelligence-readme?view=azure-dotnet-preview&preserve-view=true)
+* [Java SDK](/java/api/overview/azure/ai-documentintelligence-readme?view=azure-java-preview&preserve-view=true)
+* [JavaScript](/javascript/api/overview/azure/ai-document-intelligence-rest-readme?view=azure-node-preview&preserve-view=true)
+* [Python SDK](/python/api/overview/azure/ai-documentintelligence-readme?view=azure-python-preview&preserve-view=true)
 
 ### [Document Intelligence Studio](#tab/studio)
 
-* [Studio](https://documentintelligence.ai.azure.com/studio)
-* [How-to guide](../quickstarts/get-started-studio.md#authentication-in-studio)
+* [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio)
+* [Get started: Document Intelligence Studio](../quickstarts/get-started-studio.md#authentication-in-document-intelligence-studio)
 
 ---
 
@@ -708,88 +695,88 @@ After you retrieve you key and endpoint, you can use the following development o
 
 ## Document Intelligence Sample Labeling tool
 
-1. Navigate to the [Document Intelligence sample tool](https://fott-2-1.azurewebsites.net/).
+1. Go to the [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/).
 
 1. On the sample tool home page, select **Use Layout to get text, tables and selection marks**.
 
-     :::image type="content" source="../media/label-tool/layout-1.jpg" alt-text="Screenshot of connection settings for the Document Intelligence layout process.":::
+     :::image type="content" source="../media/label-tool/layout-1.jpg" alt-text="Screenshot that shows connection settings for the Document Intelligence layout process.":::
 
 1. In the **Document Intelligence service endpoint** field, paste the endpoint that you obtained with your Document Intelligence subscription.
 
-1. In the **key** field, paste  the key you obtained from your Document Intelligence resource.
+1. In the **key** field, paste the key that you obtained from your Document Intelligence resource.
 
-1. In the **Source** field, select **URL** from the dropdown menu You can use our sample document:
+1. In the **Source** field, select **URL** from the dropdown menu. You can use the sample document:
 
-    * [**Sample document**](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/layout-page-001.jpg).
+    * [Sample document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/layout-page-001.jpg).
 
-    * Select the **Fetch** button.
+    * Select **Fetch**.
 
-1. Select **Run Layout**. The Document Intelligence Sample Labeling tool calls the `Analyze Layout` API to analyze the document.
+1. Select **Run Layout**. The Document Intelligence Sample Labeling tool calls the Analyze Layout API to analyze the document.
 
-    :::image type="content" source="../media/fott-layout.png" alt-text="Screenshot of `Layout` dropdown window.":::
+    :::image type="content" source="../media/fott-layout.png" alt-text="Screenshot that shows the Layout dropdown pane.":::
 
-1. View the results - see the highlighted extracted text, detected selection marks, and detected tables.
+1. View the results. See the highlighted extracted text, detected selection marks, and detected tables.
 
-    :::image type="content" source="../media/label-tool/layout-3.jpg" alt-text="Screenshot of connection settings for the Document Intelligence Sample Labeling tool.":::
+    :::image type="content" source="../media/label-tool/layout-3.jpg" alt-text="Screenshot that shows connection settings for the Document Intelligence Sample Labeling tool.":::
 
 :::moniker-end
 
 :::moniker range="doc-intel-2.1.0"
 
-Document Intelligence v2.1 supports the following tools, applications, and libraries:
+Document Intelligence v2.1 supports the following tools, applications, and libraries.
 
 | Feature | Resources |
 |----------|-------------------------|
-|**Layout API**| &bullet; [**Document Intelligence labeling tool**](https://fott-2-1.azurewebsites.net/layout-analyze)</br>&bullet; [**REST API**](../how-to-guides/use-sdk-rest-api.md?pivots=programming-language-rest-api&tabs=windows&view=doc-intel-2.1.0&preserve-view=true)</br>&bullet; [**Client-library SDK**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet; [**Document Intelligence Docker container**](../containers/install-run.md?branch=main&tabs=layout#run-the-container-with-the-docker-compose-up-command)|
+|Layout API| &bullet; [Document Intelligence labeling tool](https://fott-2-1.azurewebsites.net/layout-analyze)</br>&bullet; [REST API](../how-to-guides/use-sdk-rest-api.md?pivots=programming-language-rest-api&tabs=windows&view=doc-intel-2.1.0&preserve-view=true)</br>&bullet; [Client-library SDK](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet; [Document Intelligence Docker container](../containers/install-run.md?branch=main&tabs=layout#run-the-container-with-the-docker-compose-up-command)|
 
 :::moniker-end
 
 :::moniker range="doc-intel-3.0.0 || doc-intel-3.1.0"
 
 ## Extract data
 
-The layout model extracts structural elements from your documents. To follow are descriptions of these structural elements with guidance on how to extract them from your document input:
+The layout model extracts structural elements from your documents. The structural elements are described here, and the following guidance shows you how to extract them from your document input.
 
-* [**Page**](#page)
-* [**Paragraph**](#paragraph)
-* [**Text, line, and word**](#text-lines-and-words)
-* [**Selection mark**](#selection-marks)
-* [**Table**](#tables)
-* [**Annotations**](#annotations)
+* [Page](#page)
+* [Paragraph](#paragraph)
+* [Text, line, and word](#text-lines-and-words)
+* [Selection mark](#selection-marks)
+* [Table](#tables)
+* [Annotations](#annotations)
 
 :::moniker-end
 
 :::moniker range="doc-intel-2.1.0"
 
 ## Extract data
 
-The layout model extracts structural elements from your documents. To follow are descriptions of these structural elements with guidance on how to extract them from your document input:
+The layout model extracts structural elements from your documents. The structural elements are described here, and the following guidance shows you how to extract them from your document input.
 
-* [**Page**](#page)
-* [**Paragraph**](#paragraph)
-* [**Text, line, and word**](#text-lines-and-words)
-* [**Selection mark**](#selection-marks)
-* [**Table**](#tables)
-* [**Natural reading order**](#natural-reading-order-output-latin-only)
-* [**Select page number or range**](#select-page-number-or-range-for-text-extraction)
+* [Page](#page)
+* [Paragraph](#paragraph)
+* [Text, line, and word](#text-lines-and-words)
+* [Selection mark](#selection-marks)
+* [Table](#tables)
+* [Natural reading order](#natural-reading-order-output-latin-only)
+* [Select page number or range](#select-page-number-or-range-for-text-extraction)
 
 :::moniker-end
 
 :::moniker range="<=doc-intel-3.1.0"
 
 ### Page
 
-The pages collection is a list of pages within the document. Each page is represented sequentially within the document and ../includes the orientation angle indicating if the page is rotated and the width and height (dimensions in pixels). The page units in the model output are computed as shown:
+The `pages` collection is a list of pages within the document. Each page is represented sequentially within the document and includes the orientation angle that indicates if the page is rotated and the width and height (dimensions in pixels). The page units in the model output are computed as shown in the following table.
 
-| **File format**   | **Computed page unit**   | **Total pages**  |
+| File format   | Computed page unit   | Total pages  |
 | --- | --- | --- |
-|Images (JPEG/JPG, PNG, BMP, HEIF) | Each image = 1 page unit | Total images  |
-|PDF | Each page in the PDF = 1 page unit | Total pages in the PDF |
-|TIFF | Each image in the TIFF = 1 page unit | Total images in the TIFF |
-|Word (DOCX)  | Up to 3,000 characters = 1 page unit, embedded or linked images not supported | Total pages of up to 3,000 characters each |
-|Excel (XLSX)  | Each worksheet = 1 page unit, embedded or linked images not supported | Total worksheets |
-|PowerPoint (PPTX) |  Each slide = 1 page unit, embedded or linked images not supported | Total slides |
-|HTML | Up to 3,000 characters = 1 page unit, embedded or linked images not supported | Total pages of up to 3,000 characters each |
+|Images (JPEG/JPG, PNG, BMP, HEIF) | Each image = 1 page unit. | Total images  |
+|PDF | Each page in the PDF = 1 page unit. | Total pages in the PDF |
+|TIFF | Each image in the TIFF = 1 page unit. | Total images in the TIFF |
+|Word (DOCX)  | Up to 3,000 characters = 1 page unit. Embedded or linked images aren't supported. | Total pages of up to 3,000 characters each |
+|Excel (XLSX)  | Each worksheet = 1 page unit. Embedded or linked images aren't supported. | Total worksheets |
+|PowerPoint (PPTX) |  Each slide = 1 page unit. Embedded or linked images aren't supported. | Total slides |
+|HTML | Up to 3,000 characters = 1 page unit. Embedded or linked images aren't supported. | Total pages of up to 3,000 characters each |
 
 :::moniker-end
 
@@ -853,11 +840,11 @@ for page in result.pages:
 
 ### Extract selected pages from documents
 
-For large multi-page documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction.
+For large multipage documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction.
 
 ### Paragraph
 
-The Layout model extracts all identified blocks of text in the `paragraphs` collection as a top level object under `analyzeResults`. Each entry in this collection represents a text block and ../includes the extracted text as`content`and the bounding `polygon` coordinates. The `span` information points to the text fragment within the top level `content` property that contains the full text from the document.
+The layout model extracts all identified blocks of text in the `paragraphs` collection as a top-level object under `analyzeResults`. Each entry in this collection represents a text block and includes the extracted text as `content`and the bounding `polygon` coordinates. The `span` information points to the text fragment within the top-level `content` property that contains the full text from the document.
 
 ```json
 
@@ -872,16 +859,16 @@ The Layout model extracts all identified blocks of text in the `paragraphs` coll
 
 #### Paragraph role
 
-The new machine-learning based page object detection extracts logical roles like titles, section headings, page headers, page footers, and more. The Document Intelligence Layout model assigns certain text blocks in the `paragraphs` collection with their specialized role or type predicted by the model. It's best to use paragraph roles with unstructured documents to help understand the layout of the extracted content for a richer semantic analysis. The following paragraph roles are supported:
+The new page object detection based on machine learning extracts logical roles like titles, section headings, page headers, page footers, and more. The Document Intelligence layout model assigns certain text blocks in the `paragraphs` collection with their specialized role or type predicted by the model. It's best to use paragraph roles with unstructured documents to help understand the layout of the extracted content for a richer semantic analysis. The following paragraph roles are supported.
 
-| **Predicted role**   | **Description**   | **Supported file types** |
+| Predicted role   | Description   | Supported file types |
 | --- | --- | --- |
-| `title`  | The main headings in the page | pdf, image, docx, pptx, xlsx, html |
-| `sectionHeading`  | One or more subheadings on the page  | pdf, image, docx, xlsx, html |
-| `footnote`  | Text near the bottom of the page  | pdf, image |
-| `pageHeader`  | Text near the top edge of the page  | pdf, image, docx |
-| `pageFooter`  | Text near the bottom edge of the page  | pdf, image, docx, pptx, html |
-| `pageNumber`  | Page number  | pdf, image |
+| `title`  | The main headings in the page | PDF, Image, DOCX, PPTX, XLSX, HTML |
+| `sectionHeading`  | One or more subheadings on the page  | PDF, Image, DOCX, XLSX, HTML |
+| `footnote`  | Text near the bottom of the page  | PDF, Image |
+| `pageHeader`  | Text near the top edge of the page  | PDF, Image, DOCX |
+| `pageFooter`  | Text near the bottom edge of the page  | PDF, Image, DOCX, PPTX, HTML |
+| `pageNumber`  | Page number  | PDF, Image |
 
 ```json
 {
@@ -905,9 +892,9 @@ The new machine-learning based page object detection extracts logical roles like
 
 ### Text, line, and word
 
-The document layout model in Document Intelligence extracts print and handwritten style text as `lines` and `words`. The `styles` collection ../includes any handwritten style for lines if detected along with the spans pointing to the associated text. This feature applies to [supported handwritten languages](../language-support/prebuilt.md).
+The document layout model in Document Intelligence extracts print and handwritten-style text as lines and words. The `styles` collection includes any handwritten style for lines if detected along with the spans that point to the associated text. This feature applies to [supported handwritten languages](../language-support/prebuilt.md).
 
-For Microsoft Word, Excel, PowerPoint, and HTML, Document Intelligence v4.0 `2024-11-30` (GA) Layout model extract all embedded text as is. Texts are extracted as words and paragraphs. Embedded images aren't supported.
+For Word, Excel, PowerPoint, and HTML, the Document Intelligence v4.0 2024-11-30 (GA) layout model extracts all embedded text as is. Texts are extracted as words and paragraphs. Embedded images aren't supported.
 
 :::moniker-end
 
@@ -984,7 +971,7 @@ for line_idx, line in enumerate(page.lines):
 
 ### Handwritten style
 
-The response ../includes classifying whether each text line is of handwriting style or not, along with a confidence score. For more information. See [Handwritten language support](../language-support/ocr.md). The following example shows an example JSON snippet.
+The response includes classifying whether each text line is of handwriting style or not, along with a confidence score. For more information, see [Handwritten language support](../language-support/ocr.md). The following example shows an example JSON snippet.
 
 ```json
 "styles": [
@@ -1000,11 +987,11 @@ The response ../includes classifying whether each text line is of handwriting st
 }
 ```
 
-If you enable the [font/style addon capability](../concept-add-on-capabilities.md#font-property-extraction), you also get the font/style result as part of the `styles` object.
+If you enable the [font/style add-on capability](../concept-add-on-capabilities.md#font-property-extraction), you also get the font/style result as part of the `styles` object.
 
 ### Selection mark
 
-The Layout model also extracts selection marks from documents. Extracted selection marks appear within the `pages` collection for each page. They include the bounding `polygon`, `confidence`, and selection `state` (`selected/unselected`). The text representation (that is, `:selected:` and `:unselected`) is also included as the starting index (`offset`) and `length` that references the top level `content` property that contains the full text from the document.
+The layout model also extracts selection marks from documents. Extracted selection marks appear within the `pages` collection for each page. They include the bounding `polygon`, `confidence`, and selection `state` (`selected/unselected`). The text representation (that is, `:selected:` and `:unselected`) is also included as the starting index (`offset`) and `length` that references the top-level `content` property that contains the full text from the document.
 
 :::moniker-end
 
@@ -1070,22 +1057,20 @@ for selection_mark in page.selection_marks:
 
 ### Table
 
-Extracting tables is a key requirement for processing documents containing large volumes of data typically formatted as tables. The Layout model extracts tables in the `pageResults` section of the JSON output. Extracted table information ../includes the number of columns and rows, row span, and column span. Each cell with its bounding polygon is output along with information whether the area is recognized as a `columnHeader` or not. The model supports extracting tables that are rotated. Each table cell contains the row and column index and bounding polygon coordinates. For the cell text, the model outputs the `span` information containing the starting index (`offset`). The model also outputs the `length` within the top-level content that contains the full text from the document.
+Extracting tables is a key requirement for processing documents that contain large volumes of data typically formatted as tables. The layout model extracts tables in the `pageResults` section of the JSON output. Extracted table information includes the number of columns and rows, row span, and column span. Each cell with its bounding polygon is output along with information whether the area is recognized as `columnHeader` or not.
 
-Here are a few factors to consider when using the Document Intelligence bale extraction capability:
+The model supports extracting tables that are rotated. Each table cell contains the row and column index and bounding polygon coordinates. For the cell text, the model outputs the `span` information that contains the starting index (`offset`). The model also outputs the `length` within the top-level content that contains the full text from the document.
 
-* Is the data that you want to extract presented as a table, and is the table structure meaningful?
+Here are a few factors to consider when you use the Document Intelligence bale extraction capability:
 
+* Is the data that you want to extract presented as a table, and is the table structure meaningful?
 * Can the data fit in a two-dimensional grid if the data isn't in a table format?
-
-* Do your tables span multiple pages? If so, to avoid having to label all the pages, split the PDF into pages before sending it to Document Intelligence. After the analysis, post-process the pages to a single table.
-
-* Refer to [Tabular fields](../train/custom-labels.md#tabular-fields) if you're creating custom models. Dynamic tables have a variable number of rows for each column. Fixed tables have a constant number of rows for each column.
+* Do your tables span multiple pages? If so, to avoid having to label all the pages, split the PDF into pages before you send it to Document Intelligence. After the analysis, post-process the pages to a single table.
+* See [Tabular fields](../train/custom-labels.md#tabular-fields) if you create custom models. Dynamic tables have a variable number of rows for each column. Fixed tables have a constant number of rows for each column.
 
 > [!NOTE]
 >
-> * Table analysis isn't supported if the input file is XLSX.
- > * Document Intelligence v4.0 `2024-11-30` (GA) supports bounding regions for figures and tables that cover only the core content and exclude associated caption and footnotes.
+> Table analysis isn't supported if the input file is XLSX. Document Intelligence v4.0 2024-11-30 (GA) supports bounding regions for figures and tables that cover only the core content and excludes the associated caption and footnotes.
 
 :::moniker-end
 
@@ -1177,7 +1162,7 @@ for table_idx, table in enumerate(result.tables):
 
 ### Annotations
 
-The Layout model extracts annotations in documents, such as checks and crosses. The response ../includes the kind of annotation, along with a confidence score and bounding polygon.
+The layout model extracts annotations in documents, such as checks and crosses. The response includes the kind of annotation, along with a confidence score and bounding polygon.
 
 ```json
     {
@@ -1201,73 +1186,74 @@ The Layout model extracts annotations in documents, such as checks and crosses.
 
 ### Natural reading order output (Latin only)
 
-You can specify the order in which the text lines are output with the `readingOrder` query parameter. Use `natural` for a more human-friendly reading order output as shown in the following example. This feature is only supported for Latin languages.
+You can specify the order in which the text lines are output with the `readingOrder` query parameter. Use `natural` for a more human-friendly reading order output, as shown in the following example. This feature is supported only for Latin languages.
 
-:::image type="content" source="../media/layout-reading-order-example.png" alt-text="Screenshot of `layout` model reading order processing." lightbox="../../../ai-services/Computer-vision/Images/ocr-reading-order-example.png":::
+:::image type="content" source="../media/layout-reading-order-example.png" alt-text="Screenshot of the layout model reading order processing." lightbox="../../../ai-services/Computer-vision/Images/ocr-reading-order-example.png":::
 
 ### Select page number or range for text extraction
 
-For large multi-page documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction. The following example shows a document with 10 pages, with text extracted for both cases - all pages (1-10) and selected pages (3-6).
+For large multipage documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction. The following example shows a document with 10 pages, with text extracted for both cases, all pages (1-10), and selected pages (3-6).
 
-:::image type="content" source="../media/layout-select-pages.png" alt-text="Screen shot of the layout model selected pages output.":::
+:::image type="content" source="../media/layout-select-pages.png" alt-text="Screenshot that shows the layout model selected pages output.":::
 
 ## The Get Analyze Layout Result operation
 
-The second step is to call the [Get Analyze Layout Result](https://westcentralus.dev.cognitive.microsoft.com/docs/services/form-recognizer-api-v2-1/operations/GetAnalyzeLayoutResult) operation. This operation takes as input the Result ID the `Analyze Layout` operation created. It returns a JSON response that contains a **status** field with the following possible values.
+The second step is to call the [Get Analyze Layout Result](https://westcentralus.dev.cognitive.microsoft.com/docs/services/form-recognizer-api-v2-1/operations/GetAnalyzeLayoutResult) operation. This operation takes as input the Result ID that the `Analyze Layout` operation created. It returns a JSON response that contains a **status** field with the following possible values.
 
 |Field| Type | Possible values |
 |:-----|:----:|:----|
-|status | string | `notStarted`: The analysis operation isn't started.</br></br>`running`: The analysis operation is in progress.</br></br>`failed`: The analysis operation failed.</br></br>`succeeded`: The analysis operation succeeded.|
+|**status** | string | `notStarted`: The analysis operation isn't started.</br></br>`running`: The analysis operation is in progress.</br></br>`failed`: The analysis operation failed.</br></br>`succeeded`: The analysis operation succeeded.|
 
-Call this operation iteratively until it returns the `succeeded` value. To avoid exceeding the requests per second (RPS) rate, use an interval of 3 to 5 seconds.
+Call this operation iteratively until it returns the `succeeded` value. To avoid exceeding the requests-per-second rate, use an interval of three to five seconds.
 
-When the **status** field has the `succeeded` value, the JSON response ../includes the extracted layout, text, tables, and selection marks. The extracted data ../includes extracted text lines and words, bounding boxes, text appearance with handwritten indication, tables, and selection marks with selected/unselected indicated.
+When the **status** field has the `succeeded` value, the JSON response includes the extracted layout, text, tables, and selection marks. The extracted data includes extracted text lines and words, bounding boxes, text appearance with handwritten indication, tables, and selection marks with selected/unselected indicated.
 
 ### Handwritten classification for text lines (Latin only)
 
-The response ../includes classifying whether each text line is of handwriting style or not, along with a confidence score. This feature is only supported for Latin languages. The following example shows the handwritten classification for the text in the image.
+The response includes classifying whether each text line is of a handwritten style or not, along with a confidence score. This feature is supported only for Latin languages. The following example shows the handwritten classification for the text in the image.
 
-:::image type="content" source="../media/layout-handwriting-classification.png" alt-text="Screenshot of `layout` model handwriting classification process.":::
+:::image type="content" source="../media/layout-handwriting-classification.png" alt-text="Screenshot that shows the layout model handwriting classification process.":::
 
 ### Sample JSON output
 
-The response to the *Get Analyze Layout Result* operation is a structured representation of the document with all the information extracted.
-See here for a [sample document file](https://github.com/Azure-Samples/cognitive-services-REST-api-samples/tree/master/curl/form-recognizer/sample-layout.pdf) and its structured output [sample layout output](https://github.com/Azure-Samples/cognitive-services-REST-api-samples/tree/master/curl/form-recognizer/sample-layout-output.json).
+The response to the `Get Analyze Layout Result` operation is a structured representation of the document with all the information extracted.
+See a [sample document file](https://github.com/Azure-Samples/cognitive-services-REST-api-samples/tree/master/curl/form-recognizer/sample-layout.pdf) and its structured output [sample layout output](https://github.com/Azure-Samples/cognitive-services-REST-api-samples/tree/master/curl/form-recognizer/sample-layout-output.json).
 
 The JSON output has two parts:
 
-* `readResults` node contains all of the recognized text and selection mark. The text presentation hierarchy is page, then line, then individual words.
-* `pageResults` node contains the tables and cells extracted with their bounding boxes, confidence, and a reference to the lines and words in "readResults" field.
+* The `readResults` node contains all the recognized text and selection mark. The text presentation hierarchy is page, then line, and then individual words.
+* The `pageResults` node contains the tables and cells extracted with their bounding boxes, confidence, and a reference to the lines and words in the `readResults` field.
 
-## Example Output
+## Example output
 
 ### Text
 
-Layout API extracts text from documents and images with multiple text angles and colors. It accepts photos of documents, faxes, printed and/or handwritten (English only) text, and mixed modes. Text is extracted with information provided on lines, words, bounding boxes, confidence scores, and style (handwritten or other). All the text information is included in the `readResults` section of the JSON output.
+The layout API extracts text from documents and images with multiple text angles and colors. It accepts photos of documents, faxes, printed and/or handwritten (English-only) text, and mixed modes. Text is extracted with information provided on lines, words, bounding boxes, confidence scores, and style (handwritten or other). All the text information is included in the `readResults` section of the JSON output.
 
 ### Tables with headers
 
-Layout API extracts tables in the `pageResults` section of the JSON output. Documents can be scanned, photographed, or digitized. Tables can be complex with merged cells or columns, with or without borders, and with odd angles. Extracted table information ../includes the number of columns and rows, row span, and column span. Each cell with its bounding box is output along with whether the area is recognized as part of a header or not. The model predicted header cells can span multiple rows and aren't necessarily the first rows in a table. They also work with rotated tables. Each table cell also ../includes the full text with references to the individual words in the `readResults` section.
+The Layout API extracts tables in the `pageResults` section of the JSON output. You can scan, photograph, or digitize documents. Tables can be complex with merged cells or columns, with or without borders, and with odd angles. 
 
-![Tables example](../media/layout-table-header-demo.gif)
+Extracted table information includes the number of columns and rows, row span, and column span. Each cell with its bounding box is output along with whether the area is recognized as part of a header or not. The model-predicted header cells can span multiple rows and aren't necessarily the first rows in a table. They also work with rotated tables. Each table cell also includes the full text with references to the individual words in the `readResults` section.
+
+![Illustration that shows a Tables example.](../media/layout-table-header-demo.gif)
 
 ### Selection marks (documents)
 
-Layout API also extracts selection marks from documents. Extracted selection marks include the bounding box, confidence, and state (selected/unselected). Selection mark information is extracted in the `readResults` section of the JSON output.
+The layout API also extracts selection marks from documents. Extracted selection marks include the bounding box, confidence, and state (selected/unselected). Selection mark information is extracted in the `readResults` section of the JSON output.
 
 ### Migration guide
 
-* Follow our [**Document Intelligence v3.1 migration guide**](../v3-1-migration-guide.md) to learn how to use the v3.1 version in your applications and workflows.
+* To learn how to use the v3.1 version in your applications and workflows, follow the steps in the [Document Intelligence v3.1 migration guide](../v3-1-migration-guide.md).
 
 :::moniker-end
 
-## Next steps
+## Related content
 
 :::moniker range="doc-intel-4.0.0 || doc-intel-3.1.0"
 
-* [Learn how to process your own forms and documents](../studio-overview.md) with the [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio).
-
-* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Learn how to [process your own forms and documents](../studio-overview.md) with the [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio).
+* Finish a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true), and create a document processing app in the development language of your choice.
 
 :::moniker-end
 
@@ -1285,8 +1271,7 @@ Layout API also extracts selection marks from documents. Extracted selection mar
 
 :::moniker range="doc-intel-2.1.0"
 
-* [Learn how to process your own forms and documents](../quickstarts/try-sample-label-tool.md) with the [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/).
+* Learn how to [process your own forms and documents](../quickstarts/try-sample-label-tool.md) with the [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/).
+* Finish a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true), and create a document processing app in the development language of your choice.
 
-* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
-
-:::moniker-end
\ No newline at end of file
+:::moniker-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レイアウトモデルに関する更新"
}
```

### Explanation
このコードの変更では、ドキュメントインテリジェンスのレイアウトモデルに関するドキュメントが更新されました。主な変更点は、テキストのクリアさや一貫性を向上させるための文言の調整が行われていることです。また、APIの機能や使用方法を説明する部分が整理され、情報がより明確になっています。具体的には、文構造解析、サポートされている言語やファイル形式、入力要件などのセクションが詳細に説明され、ユーザーがこのモデルをどのように活用できるかがより理解しやすくなっています。

さらに、開発オプションやリソースのリンクが更新され、新しい機能や手順が追加されることで、ユーザーがレイアウトモデルを使用する際のアプローチが改善されています。全体として、ユーザーエクスペリエンスの向上を目的としたマイナーな更新がなされています。

## articles/ai-services/document-intelligence/quickstarts/get-started-studio.md{#item-b2798e}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: "Quickstart: Document Intelligence Studio"
+title: 'Quickstart: Document Intelligence Studio'
 titleSuffix: Azure AI Services
-description: How to get started processing forms and documents using Document Intelligence Studio
+description: Learn how to get started processing forms and documents by using Document Intelligence Studio.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
@@ -15,133 +15,123 @@ monikerRange: '>=doc-intel-3.0.0'
 
 # Get started: Document Intelligence Studio
 
-[Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/) is an online tool for visually exploring, understanding, and integrating features from the Document Intelligence service in your applications. You can get started by exploring the pretrained models with sample or your own documents. You can also create projects to build custom template models and reference the models in your applications.
+[Azure AI Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/) is an online tool that you can use to visually explore, understand, and integrate features from the Document Intelligence service into your applications. You can get started by exploring the pretrained models with samples or your own documents. You can also create projects to build custom template models and reference the models in your applications.
 
-## Prerequisites for new users
+## Prerequisites
 
-To use Document Intelligence Studio, you need to acquire the following assets from the Azure portal:
-
-* Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services/).
-
-* An Azure AI services or Document Intelligence resource. Once you have your Azure subscription, create a [single-service](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) or [Azure AI multi-service](https://portal.azure.com/#create/Microsoft.CognitiveServicesAIFoundry) resource, in the Azure portal, to get your key and endpoint.
-
-* You can use the free pricing tier (`F0`) to try the service, and upgrade later to a paid tier for production.
+* An Azure subscription. [Create one for free](https://azure.microsoft.com/free/cognitive-services/).
+* An Azure AI services or Document Intelligence resource. After you have your Azure subscription, create a [single-service](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) or [Azure AI multiservice](https://portal.azure.com/#create/Microsoft.CognitiveServicesAIFoundry) resource in the Azure portal to get your key and endpoint.
+* To try the service, use the free pricing tier (F0). You can upgrade later to a paid tier for production.
 
 > [!TIP]
 > Create an Azure AI Foundry resource if you plan to access multiple Azure AI services under a single endpoint/key. For Document Intelligence access only, create a Document Intelligence resource. You need a single-service resource if you intend to use [Microsoft Entra authentication](/azure/active-directory/authentication/overview-authentication).
 >
-> Document Intelligence now supports Azure Active Directory (Azure AD) token authentication in addition to local (key-based) authentication when accessing the Document Intelligence resources and storage accounts. Be sure to follow below instructions to set up correct access roles, especially if your resources are applied with `DisableLocalAuth` policy.
+> Document Intelligence now supports Azure Active Directory token authentication in addition to local (key-based) authentication when you access Document Intelligence resources and storage accounts. Follow the instructions to set up correct access roles, especially if your resources are applied with the `DisableLocalAuth` policy.
 
-There are added prerequisites for using custom models in Document Intelligence Studio. Refer to the [documentation](studio-custom-project.md) for step by step guidance.
+There are added prerequisites for using custom models in Document Intelligence Studio. For step-by-step guidance, see [Document Intelligence Studio custom projects](studio-custom-project.md).
 
 ### Authorization policies
 
-Your organization can opt to disable local authentication and enforce Microsoft Entra (formerly Azure Active Directory) authentication for Azure AI Document Intelligence resources and Azure blob storage.
-
-* Microsoft Entra authentication requires that key based authorization is disabled. After key access is disabled, Microsoft Entra ID is the only available authorization method.
+Your organization can opt to disable local authentication and enforce Microsoft Entra (formerly Azure Active Directory) authentication for Document Intelligence resources and Azure Blob Storage.
 
+* Microsoft Entra authentication requires key-based authorization to be disabled. After key access is disabled, Microsoft Entra ID is the only available authorization method.
 * Microsoft Entra allows granting minimum privileges and granular control for Azure resources.
 
-For more information, *see* the following guidance:
+For more information, see the following guidance:
 
-  * [Disable local authentication for Azure AI Services](../../disable-local-auth.md).
+  * [Disable local authentication for Azure AI services](../../disable-local-auth.md)
   * [Prevent Shared Key authorization for an Azure Storage account](/azure/storage/common/shared-key-authorization-prevent)
- 
- > [!NOTE]
- > If local (key-based) authentication is disabled for your Document Intelligence service resource, be sure to obtain **Cognitive Services User** role and your Azure AD token to authenticate requests on Document Intelligence Studio. The **Contributor** role only allows you to list keys but doesn't give you permission to use the resource when key-access is disabled.
 
-* **Designating role assignments**. Document Intelligence Studio basic access requires the [`Cognitive Services User`](/azure/role-based-access-control/built-in-roles/ai-machine-learning#cognitive-services-user) role. For more information, *see* [Document Intelligence role assignments](try-document-intelligence-studio.md#azure-role-assignments).
+If local (key-based) authentication is disabled for your Document Intelligence service resource, be sure to obtain the Cognitive Services User role and your Azure Active Directory token to authenticate requests in Document Intelligence Studio. The Contributor role allows you to list only keys but doesn't give you permission to use the resource when key access is disabled.
 
-> [!IMPORTANT]
->
-> * Make sure you have the **Cognitive Services User role**, and not the Cognitive Services Contributor role when setting up Microsoft Entra ID authentication.
-> * ✔️ **Cognitive Services User**: you need this role to Document Intelligence or Azure AI Foundry resource to enter the analyze page.
-> * ✔️ **Contributor**: you need this role to create resource group, Document Intelligence service, or Azure AI Foundry resource.
-> * In Azure context, Contributor role can only perform actions to control and manage the resource itself, including listing the access keys.
-> * User accounts with a Contributor are only able to access the Document Intelligence service by calling with access keys. However, when setting up access with Microsoft Entra ID, key-access is disabled and **Cognitive Services User** role is required for an account to use the resources.
+#### Designate role assignments
 
-### Authentication in Studio
+Document Intelligence Studio basic access requires the [Cognitive Services User](/azure/role-based-access-control/built-in-roles/ai-machine-learning#cognitive-services-user) role. For more information, see [Document Intelligence role assignments](try-document-intelligence-studio.md#azure-role-assignments).
 
-Navigate to the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/). If it's your first time logging in, a popup window appears prompting you to configure your service resource. In accordance with your organization's policy, you have one or two options:
+* Make sure that you have the Cognitive Services User role and not the Cognitive Services Contributor role when you set up Microsoft Entra ID authentication:
 
-* **Microsoft Entra authentication: access by Resource (recommended)**.
+   * **Cognitive Services User**: You need this role for the Document Intelligence or Azure AI Foundry resource to enter the analyze page.
+   * **Contributor**: You need this role to create a resource group, Document Intelligence service, or Azure AI Foundry resource.
+* In Azure context, the Contributor role can perform actions only to control and manage the resource itself, including listing the access keys.
+* User accounts with a Contributor role can access the Document Intelligence service only by calling with access keys. When you set up access with Microsoft Entra ID, key access is disabled, and the Cognitive Services User role is required for an account to use the resources.
 
-  * Choose your existing subscription.
-  * Select an existing resource group within your subscription or create a new one.
-  * Select your existing Document Intelligence or Azure AI Foundry resource.
+### Authentication in Document Intelligence Studio
 
-    :::image type="content" source="../media/studio/configure-service-resource.png" lightbox="../media/studio/configure-service-resource.png" alt-text="Screenshot of configure service resource form from the Document Intelligence Studio.":::
+Go to [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/). If it's your first time signing in, you're prompted to configure your service resource. In accordance with your organization's policy, you have the following options:
 
-* **Local authentication: access by API endpoint and key**.
+* Microsoft Entra authentication: Access by resource (recommended)
 
-  * Retrieve your endpoint and key from the Azure portal.
-  * Go to the overview page for your resource and select **Keys and Endpoint** from the left pane.
-  * Enter the values in the appropriate fields.
+  1. Select your existing subscription.
+  1. Select an existing resource group within your subscription or create a new one.
+  1. Select your existing Document Intelligence or Azure AI Foundry resource.
 
-      :::image type="content" source="../media/studio/keys-and-endpoint.png" lightbox="../media/studio/keys-and-endpoint.png" alt-text="Screenshot of the keys and endpoint page in the Azure portal.":::
+     :::image type="content" source="../media/studio/configure-service-resource.png" lightbox="../media/studio/configure-service-resource.png" alt-text="Screenshot that shows configuring a service resource in Document Intelligence Studio.":::
 
-* After validating the scenario in the Document Intelligence Studio, use the [**C#**](get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true), [**Java**](get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true), [**JavaScript**](get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true), or [**Python**](get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true) client libraries or the [**REST API**](get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true) to get started incorporating Document Intelligence models into your own applications.
+* Local authentication: Access by API endpoint and key
 
+  1. Retrieve your endpoint and key from the Azure portal.
+  1. Go to the overview page for your resource, and on the left pane, select **Keys and Endpoint**.
+  1. Enter values in the appropriate fields.
 
-### Try a Document Intelligence model
-
-To learn more about the available Document Intelligence models, *see* our [model support](../studio-overview.md#document-intelligence-model-support) page.
+      :::image type="content" source="../media/studio/keys-and-endpoint.png" lightbox="../media/studio/keys-and-endpoint.png" alt-text="Screenshot that shows the Keys and Endpoint page in the Azure portal.":::
 
-* Once your resource is configured, you can try the different models offered by Document Intelligence Studio. From the front page, select any Document Intelligence model to try using with a no-code approach.
+* After you validate the scenario in Document Intelligence Studio, use the [C#](get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true), [Java](get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true), [JavaScript](get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true), or [Python](get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true) client libraries or the [REST API](get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true) to incorporate Document Intelligence models into your own applications.
 
-* To test any of the document analysis or prebuilt models, select the model and use one of the sample documents or upload your own document to analyze. The analysis result is displayed at the right in the content-result-code window.
+### Try a Document Intelligence model
 
-* Custom models need to be trained on your documents. See [custom models overview](../train/custom-model.md) for an overview of custom models.
+To learn more about the available Document Intelligence models, see [Document Intelligence model support](../studio-overview.md#document-intelligence-model-support).
 
-* After validating the scenario in the Document Intelligence Studio, use the [**C#**](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**Java**](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**JavaScript**](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), or [**Python**](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) client libraries or the [**REST API**](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) to get started incorporating Document Intelligence models into your own applications.
+* Try the different models that Document Intelligence Studio has to offer after you configure your resource. Select any Document Intelligence model to use it with a no-code approach.
+* Test any of the document analysis or prebuilt models. Select the model, and use one of the sample documents or upload your own document to analyze. The analysis result appears in the pane on the right that shows content-result code.
+* Train the custom models on your documents. For an overview of custom models, see [Custom models overview](../train/custom-model.md).
+* Validate the scenario in Document Intelligence Studio. Then use the [C#](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [Java](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [JavaScript](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), or [Python](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) client libraries or the [REST API](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) to incorporate Document Intelligence models into your own applications.
 
 #### View resource details
 
- To view resource details such as name and pricing tier, select the **Settings** icon in the top-right corner of the Document Intelligence Studio home page and select the **Resource** tab. If you have access to other resources, you can switch resources as well.
+ To view resource details such as name and pricing tier, select the **Settings** icon in the upper-right corner of the Document Intelligence Studio home page, and then select the **Resource** tab. If you have access to other resources, you can also switch resources.
 
-:::image type="content" source="../media/studio/form-recognizer-studio-resource-page.png" lightbox="../media/studio/form-recognizer-studio-resource-page.png" alt-text="Screenshot of the studio settings page resource tab.":::
+:::image type="content" source="../media/studio/form-recognizer-studio-resource-page.png" lightbox="../media/studio/form-recognizer-studio-resource-page.png" alt-text="Screenshot that shows the Settings page Resource tab.":::
 
 With Document Intelligence, you can quickly automate your data processing in applications and workflows, easily enhance data-driven strategies, and skillfully enrich document search capabilities.
 
-#### Manage third-party settings for Studio access
+#### Manage non-Microsoft settings for Document Intelligence Studio access
 
-**Edge**:
+##### Microsoft Edge
 
-* Go to **Settings** for Microsoft Edge
-* Search for "**third-party**"
-* Go to **Manage and delete cookies and site data**
-* Turn off the setting of **Block third-party cookies**
+1. Go to **Settings** for Microsoft Edge.
+1. Search for **third-party**.
+1. Go to **Manage and delete cookies and site data**.
+1. Turn off the setting of **Block third-party cookies**.
 
-**Chrome**:
+##### Chrome
 
-* Go to **Settings** for Chrome
-* Search for "**Third-party**"
-* Under **Default behavior**, select **Allow third-party cookies**
+1. Go to **Settings** for Chrome.
+1. Search for **Third-party**.
+1. Under **Default behavior**, select **Allow third-party cookies**.
 
-**Firefox**:
+##### Firefox
 
-* Go to **Settings** for Firefox
-* Search for "**cookies**"
-* Under **Enhanced Tracking Protection**, select **Manage Exceptions**
-* Add exception for **`https://documentintelligence.ai.azure.com`** or the Document Intelligence Studio URL of your environment
+1. Go to **Settings** for Firefox.
+1. Search for **cookies**.
+1. Under **Enhanced Tracking Protection**, select **Manage Exceptions**.
+1. Add an exception for `https://documentintelligence.ai.azure.com` or the Document Intelligence Studio URL of your environment.
 
-**Safari**:
+##### Safari
 
-* Choose **Safari** > **Preferences**
-* Select **Privacy**
-* Deselect **Block all cookies**
+1. Select **Safari** > **Preferences**.
+1. Select **Privacy**.
+1. Clear **Block all cookies**.
 
 ### Troubleshooting
 
 |Scenario     |Cause| Resolution|
 |-------------|------|----------|
-|You receive the error message</br> `Form Recognizer Not Found` when opening a custom project.|Your Document Intelligence resource, bound to the custom project was deleted or moved to another resource group.| There are two ways to resolve this problem: </br>&bullet; Re-create the Document Intelligence resource under the same subscription and resource group with the same name.</br>&bullet; Re-create a custom project with the migrated Document Intelligence resource and specify the same storage account.|
-|You receive the error message</br> `PermissionDenied` when using prebuilt apps or opening a custom project.|The principal doesn't have access to API/Operation when analyzing against prebuilt models or opening a custom project. It's likely the local (key-based) authentication is disabled for your Document Intelligence resource don't have enough permission to access the resource.|Reference [Azure role assignments](try-document-intelligence-studio.md#azure-role-assignments) to configure your access roles.|
-|You receive the error message</br> `AuthorizationPermissionMismatch` when opening a custom project.|The request isn't authorized to perform the operation using the designated permission. It's likely the local (key-based) authentication is disabled for your storage account and you don't have the granted permission to access the blob data.|Reference [Azure role assignments](try-document-intelligence-studio.md#azure-role-assignments) to configure your access roles.|
-|You can't sign in to Document Intelligence Studio and receive the error message</br> `InteractionRequiredAuthError:login_required:AADSTS50058:A silent sign-request was sent but no user is signed in`|It's likely that your browser is blocking third-party cookies so you can't successfully sign in.|To resolve, see [Manage third-party settings](#manage-third-party-settings-for-studio-access) for your browser.|
+|You receive the error message</br> `Form Recognizer Not Found` when you open a custom project.|Your Document Intelligence resource, which is bound to the custom project, was deleted or moved to another resource group.| There are two ways to resolve this problem: </br>&bullet; Re-create the Document Intelligence resource under the same subscription and resource group with the same name.</br>&bullet; Re-create a custom project with the migrated Document Intelligence resource and specify the same storage account.|
+|You receive the error message</br> `PermissionDenied` when you use prebuilt apps or open a custom project.|The principal doesn't have access to the API or operation when it analyzes against prebuilt models or opens a custom project. It's likely that the local (key-based) authentication is disabled for your Document Intelligence resource, and you don't have enough permission to access the resource.|To configure your access roles, see [Azure role assignments](try-document-intelligence-studio.md#azure-role-assignments).|
+|You receive the error message</br> `AuthorizationPermissionMismatch` when you open a custom project.|The request isn't authorized to perform the operation by using the designated permission. It's likely that the local (key-based) authentication is disabled for your storage account, and you don't have the granted permission to access the blob data.|To configure your access roles, see [Azure role assignments](try-document-intelligence-studio.md#azure-role-assignments).|
+|You can't sign in to Document Intelligence Studio and receive the error message</br> `InteractionRequiredAuthError:login_required:AADSTS50058:A silent sign-request was sent but no user is signed in`.|It's likely that your browser is blocking non-Microsoft cookies, so you can't successfully sign in.|To resolve this issue, see [Manage non-Microsoft settings](#manage-non-microsoft-settings-for-document-intelligence-studio-access) for your browser.|
 
-## Next steps
+## Related content
 
 * [Learn how to create custom projects in Document Intelligence Studio](studio-custom-project.md)
-
 * [Get started with Document Intelligence client libraries](get-started-sdks-rest-api.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence Studio のクイックスタートガイドの更新"
}
```

### Explanation
このコードの変更では、Document Intelligence Studio のクイックスタートガイドが更新され、内容が整理されました。主な変更点は、文言の明確化や簡略化を図り、ユーザーが必要な手順を理解しやすくすることです。具体的には、前提条件や認証ポリシーのセクションが再構成され、情報の流れがスムーズになっています。

例えば、Azure のサブスクリプションや Document Intelligence リソースの取得方法についての説明が簡素化され、より直感的に理解できるようになりました。また、Microsoft Entra 認証に関連する注意点についても整理され、必要な役割の説明が明確になっています。

ドキュメント内の各セクションが手順ごとに分かりやすくなるように再編成されており、特にデザインロールや認証方法に関する情報が明確化されています。さらに、モデルの使用に関する手引きが強化され、ユーザーが自分のアプリケーションに Document Intelligence モデルを簡単に組み込むことができるよう配慮されています。全体として、ユーザーがページをスムーズにナビゲートし、目的の情報を迅速に見つけられるような構造になっています。

## articles/ai-services/document-intelligence/quickstarts/studio-custom-project.md{#item-f52b95}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: Document Intelligence Studio custom project
+title: Create Document Intelligence Studio custom projects
 titleSuffix: Azure AI services
-description: Form and document processing, data extraction, and analysis using Document Intelligence Studio
+description: Learn about form and document processing, data extraction, and analysis by using Document Intelligence Studio.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
@@ -14,131 +14,127 @@ monikerRange: '>=doc-intel-3.0.0'
 
 <!-- markdownlint-disable MD001 -->
 
-# Document Intelligence Studio custom projects
+# Create Document Intelligence Studio custom projects
 
 [!INCLUDE [applies to v4.0 v3.1 v3.0](../includes/applies-to-v40-v31-v30.md)]
 
-[Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/) is an online tool for visually exploring, understanding, and integrating features from the Document Intelligence service in your applications. This quickstart aims to give you a guide of setting up a custom project in Document Intelligence Studio.
+[Azure AI Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/) is an online tool that you can use to visually explore, understand, and integrate features from Document Intelligence into your applications. This quickstart aims to show you how to set up a custom project in Document Intelligence Studio.
 
-## Prerequisites for new users
+## Prerequisites
 
-For details on subscription, resource, and authentication setup, *see* [Get started with Document Intelligence Studio](get-started-studio.md#prerequisites-for-new-users).
+For information on subscription, resource, and authentication setup, see [Get started with Document Intelligence Studio](get-started-studio.md#prerequisites).
 
-## Prerequisites for custom projects
+## Prerequisites for new users
 
-In addition to the Azure account and a Document Intelligence or Azure AI Foundry resource, you need:
+In addition to an Azure account and the Document Intelligence or Azure AI Foundry resource, you need an Azure Blob Storage container and Azure role assignments.
 
 ### Azure Blob Storage container
 
-A **standard performance** [**Azure Blob Storage account**](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM). You create containers to store and organize your training documents within your storage account. If you don't know how to create an Azure storage account with a container, following these quickstarts:
+You need a standard performance [Azure Blob Storage account](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM). You can create containers to store and organize your training documents within your storage account. If you don't know how to create an Azure storage account with a container, follow these quickstarts:
 
-* [**Create a storage account**](/azure/storage/common/storage-account-create). When creating your storage account, make sure to select **Standard** performance in the **Instance details → Performance** field.
-* [**Create a container**](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container). When creating your container, set the **Public access level** field to **Container** (anonymous read access for containers and blobs) in the **New Container** window.
+   * [Create a storage account](/azure/storage/common/storage-account-create): When you create your storage account, in the **Instance details** > **Performance** field, select **Standard** performance.
+   * [Create a container](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container): When you create your container, on the **New Container** pane, set the **Public access level** field to **Container** (anonymous read access for containers and blobs).
 
 ### Azure role assignments
 
-For custom projects, the following role assignments are required for different scenarios.
+For custom projects, the following role assignments are required for different scenarios:
 
 * Basic
-  * **Cognitive Services User**: You need this role for Document Intelligence or Azure AI Foundry resource to train the custom model or do analysis with trained models.
-  * **Storage Blob Data Contributor**: You need this role for the Storage Account to create a project and label data.
+  * **Cognitive Services User**: You need this role for the Document Intelligence or Azure AI Foundry resource to train the custom model or do analysis with trained models.
+  * **Storage Blob Data Contributor**: You need this role for the storage account to create a project and label data.
 * Advanced
-  * **Storage Account Contributor**: You need this role for the Storage Account to set up CORS settings (this action is a one-time effort if the same storage account is reused).
+  * **Storage Account Contributor**: You need this role for the storage account to set up cross-origin resource sharing (CORS) settings. (This action is a one-time effort if the same storage account is reused.)
   * **Contributor**: You need this role to create a resource group and resources.
 
   > [!NOTE]
-  > If local (key-based) authentication is disabled for your Document Intelligence service resource and storage account, be sure to obtain **Cognitive Services User** and **Storage Blob Data Contributor** roles respectively, so you have enough permissions to use Document Intelligence Studio. The **Storage Account Contributor** and **Contributor** roles only allow you to list keys but don't give you permission to use the resources when key-access is disabled.
+  > If local (key-based) authentication is disabled for your Document Intelligence service resource and storage account, be sure to obtain Cognitive Services User and Storage Blob Data Contributor roles, respectively, so that you have enough permissions to use Document Intelligence Studio. The Storage Account Contributor and Contributor roles allow you to list keys, but they don't give you permission to use the resources when key access is disabled.
 
 ### Configure CORS
 
-[CORS (Cross Origin Resource Sharing)](/rest/api/storageservices/cross-origin-resource-sharing--cors--support-for-the-azure-storage-services) needs to be configured on your Azure storage account for it to be accessible from the Document Intelligence Studio. To configure CORS in the Azure portal, you need access to the CORS tab of your storage account.
+[Cross-origin resource sharing](/rest/api/storageservices/cross-origin-resource-sharing--cors--support-for-the-azure-storage-services) must be configured on your Azure storage account for it to be accessible from Document Intelligence Studio. To configure CORS in the Azure portal, you need access to the CORS tab of your storage account.
 
 1. Select the CORS tab for the storage account.
 
-   :::image type="content" source="../media/quickstarts/cors-setting-menu.png" alt-text="Screenshot of the CORS setting menu in the Azure portal.":::
+   :::image type="content" source="../media/quickstarts/cors-setting-menu.png" alt-text="Screenshot that shows the CORS setting menu in the Azure portal.":::
 
-1. Start by creating a new CORS entry in the Blob service.
+1. Start by creating a new CORS entry on the **Blob service** tab.
 
-1. Set the **Allowed origins** to `https://documentintelligence.ai.azure.com`.
+1. Set **Allowed origins** to `https://documentintelligence.ai.azure.com`.
 
    :::image type="content" source="../media/quickstarts/cors-updated-image.png" alt-text="Screenshot that shows CORS configuration for a storage account.":::
 
-    > [!TIP]
-    > You can use the wildcard character '*' rather than a specified domain to allow all origin domains to make requests via CORS.
+    You can use the wildcard character `*` instead of a specified domain to allow all origin domains to make requests via CORS.
 
-1. Select all the available 8 options for **Allowed methods**.
+1. Select all the available eight options for **Allowed methods**.
 
-1. Approve all **Allowed headers** and **Exposed headers** by entering an * in each field.
+1. Approve all **Allowed headers** and **Exposed headers** by entering an asterisk (*) in each field.
 
-1. Set the **Max Age** to 120 seconds or any acceptable value.
+1. Set **Max Age** to 120 seconds or any acceptable value.
 
-1. To save the changes, select the save button at the top of the page.
+1. To save the changes, select **Save** at the top of the page.
 
 CORS should now be configured to use the storage account from Document Intelligence Studio.
 
 ### Sample documents set
 
-1. Sign in to the [Azure portal](https://portal.azure.com) and navigate to **Your storage account** > **Data storage** > **Containers**.
+1. Sign in to the [Azure portal](https://portal.azure.com). Go to your storage account and select **Data storage** > **Containers**.
 
-   :::image border="true" type="content" source="../media/sas-tokens/data-storage-menu.png" alt-text="Screenshot of Data storage menu in the Azure portal.":::
+   :::image border="true" type="content" source="../media/sas-tokens/data-storage-menu.png" alt-text="Screenshot that shows the Data storage menu in the Azure portal.":::
 
-1. Select a **container** from the list.
+1. Select a container from the list.
 
-1. Select **Upload** from the menu at the top of the page.
+1. On the menu at the top of the page, select **Upload**.
 
-    :::image border="true" type="content" source="../media/sas-tokens/container-upload-button.png" alt-text="Screenshot of container upload button in the Azure portal.":::
+    :::image border="true" type="content" source="../media/sas-tokens/container-upload-button.png" alt-text="Screenshot that shows the container Upload button in the Azure portal.":::
 
-1. The **Upload blob** window appears.
+1. On the **Upload blob** pane, select your files to upload.
 
-1. Select your files to upload.
-
-    :::image border="true" type="content" source="../media/sas-tokens/upload-blob-window.png" alt-text="Screenshot of upload blob window in the Azure portal.":::
+    :::image border="true" type="content" source="../media/sas-tokens/upload-blob-window.png" alt-text="Screenshot that shows the Upload blob pane in the Azure portal.":::
 
 > [!NOTE]
-> By default, the Studio uses documents that are located at the root of your container. However, you can use data organized in folders by specifying the folder path in the Custom form project creation steps. *See* [**Organize your data in subfolders**](../how-to-guides/build-a-custom-model.md?view=doc-intel-2.1.0&preserve-view=true#organize-your-data-in-subfolders-optional)
+> By default, Document Intelligence Studio uses documents that are located at the root of your container. You can use data organized in folders by specifying the folder path in the steps for creating a custom form project. For more information, see [Organize your data in subfolders](../how-to-guides/build-a-custom-model.md?view=doc-intel-2.1.0&preserve-view=true#organize-your-data-in-subfolders-optional).
 
 ## Use Document Intelligence Studio features
 
-### Auto label documents with prebuilt models or one of your own models
+### Autolabel documents with prebuilt models or one of your own models
 
-* In custom extraction model labeling page, you can now auto label your documents using one of Document Intelligent Service prebuilt models or your trained models.
+On the labeling page for the custom extraction model, you can now autolabel your documents by using one of the Document Intelligent Service prebuilt models or your trained models.
 
-    :::image type="content" source="../media/studio/auto-label.gif" alt-text="Animated screenshot showing auto labeling in Studio.":::
+:::image type="content" source="../media/studio/auto-label.gif" alt-text="Animated screenshot that shows autolabeling.":::
 
-* For some documents, duplicate labels after running autolabel are possible. Make sure to modify the labels so that there are no duplicate labels in the labeling page afterwards.
+For some documents, duplicate labels after running autolabel are possible. Make sure to modify the labels so that there are no duplicate labels on the labeling page afterwards.
 
-    :::image type="content" source="../media/studio/duplicate-labels.png" alt-text="Screenshot showing duplicate label warning after auto labeling.":::
+:::image type="content" source="../media/studio/duplicate-labels.png" alt-text="Screenshot that shows duplicate label warning after autolabeling.":::
 
-### Auto label tables
+### Autolabel tables
 
-* In custom extraction model labeling page, you can now auto label the tables in the document without having to label the tables manually.
+On the labeling page for the custom extraction model, you can now autolabel the tables in the document without having to label the tables manually.
 
-    :::image type="content" source="../media/studio/auto-table-label.gif" alt-text="Animated screenshot showing auto table labeling in Studio.":::
+:::image type="content" source="../media/studio/auto-table-label.gif" alt-text="Animated screenshot that shows autotable labeling.":::
 
 ### Add test files directly to your training dataset
 
-* Once you train a custom extraction model, make use of the test page to improve your model quality by uploading test documents to training dataset if needed.
+After you train a custom extraction model, use the test page to improve your model quality by uploading test documents to the training dataset, if needed.
 
-* If a low confidence score is returned for some labels, make sure to correctly label your content. If not, add them to the training dataset and relabel to improve the model quality.
+If a low confidence score is returned for some labels, make sure to correctly label your content. If not, add them to the training dataset and relabel to improve the model quality.
 
-    :::image type="content" source="../media/studio/add-from-test.gif" alt-text="Animated screenshot showing how to add test files to training dataset.":::
+:::image type="content" source="../media/studio/add-from-test.gif" alt-text="Animated screenshot that shows how to add test files to a training dataset.":::
 
 ### Make use of the document list options and filters in custom projects
 
-* Use the custom extraction model labeling page to navigate through your training documents with ease by making use of the search, filter, and sort by feature.
+Use the labeling page for the custom extraction model to go through your training documents with ease by making use of the search, filter, and sort-by features.
 
-* Utilize the grid view to preview documents or use the list view to scroll through the documents more easily.
+Use the grid view to preview documents, or use the list view to scroll through documents more easily.
 
-    :::image type="content" source="../media/studio/document-options.png" alt-text="Screenshot of document list view options and filters.":::
+:::image type="content" source="../media/studio/document-options.png" alt-text="Screenshot that shows document list view options and filters.":::
 
 ### Project sharing
 
 Share custom extraction projects with ease. For more information, see [Project sharing with custom models](../how-to-guides/project-share-custom-models.md).
 
-## Next steps
-
-* Follow our [**Document Intelligence v3.1 migration guide**](../v3-1-migration-guide.md) to learn the differences from the previous version of the REST API.
-* Explore our [**v4.0 SDK quickstarts**](get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true) to try the v3.0 features in your applications using the new client libraries.
-* Refer to our [**v4.0 REST API quickstarts**](get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true) to try the v3.0 features using the new REST API.
+## Related content
 
-[Get started with the Document Intelligence Studio](https://formrecognizer.appliedai.azure.com).
+* Follow the [Document Intelligence v3.1 migration guide](../v3-1-migration-guide.md) to learn the differences from the previous version of the REST API.
+* Explore the [v4.0 SDK quickstarts](get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true) to try the v3.0 features in your applications by using the new client libraries.
+* Refer to the [v4.0 REST API quickstarts](get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true) to try the v3.0 features by using the new REST API.
+* [Get started with Document Intelligence Studio](https://formrecognizer.appliedai.azure.com).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence Studio カスタムプロジェクトの作成に関するガイドの更新"
}
```

### Explanation
このコードの変更では、Document Intelligence Studio におけるカスタムプロジェクトの作成に関するガイドが更新され、内容が整理されました。主な変更点は、文言の明確化や構成の改善で、ユーザーがカスタムプロジェクトの設定をはじめとする手順をより簡単に理解できるようになっています。

具体的な変更には、"Prerequisites for new users" から "Prerequisites" へのタイトル変更や、各ステップの説明が簡潔になったことが含まれます。また、Azure Blob Storage のコンテナの必要性や Azure 役割の割り当てに関するセクションが強化され、必要な権限の取得や設定方法が明瞭に示されています。さらに、CORS（クロスオリジンリソースシェアリング）の設定方法が具体的に説明されており、ユーザーがアクセス設定を理解しやすいよう整理されています。

最後に、次のステップとして関連するドキュメントへのリンクが提供され、ユーザーが次に進むべき方向を示しています。全体として、ユーザーが Document Intelligence Studio を活用するためのプロセスが一層スムーズに行えるよう情報が整理されています。

## articles/ai-services/document-intelligence/studio-overview.md{#item-db8fa3}

<details>
<summary>Diff</summary>
````diff
@@ -18,72 +18,70 @@ monikerRange: '>=doc-intel-3.0.0'
 
 [!INCLUDE [applies to v4.0 v3.1 v3.0](includes/applies-to-v40-v31-v30.md)]
 
-The studio is an online tool to visually explore, understand, train, and integrate features from the Document Intelligence service into your applications. The studio provides a platform for you to experiment with the different Document Intelligence models and sample returned data in an interactive manner without the need to write code. You can use the studio experience to:
+Azure AI Document Intelligence Studio is an online tool that you can use to visually explore, understand, train, and integrate features from Document Intelligence into your applications. The studio provides a platform for you to experiment with the different Document Intelligence models. You can also sample returned data in an interactive manner without the need to write code. You can use the studio experience to:
 
 * Learn more about the different capabilities in Document Intelligence.
 * Use your Document Intelligence resource to test models on sample documents or upload your own documents.
 * Experiment with different add-on and preview features to adapt the output to your needs.
 * Train custom classification models to classify documents.
 * Train custom extraction models to extract fields from documents.
-* Get sample code for the language specific `SDKs` to integrate into your applications.
+* Get sample code for the language-specific SDKs to integrate into your applications.
 
-Currently, we're undergoing the migration of features from the [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio) to the new [Azure AI Foundry portal](https://ai.azure.com/explore/aiservices/vision). There are some differences in the offerings for the two studios, which determine the correct studio for your use case.
+Currently, features are migrating from [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio) to the new [Azure AI Foundry portal](https://ai.azure.com/explore/aiservices/vision). There are some differences in the offerings for the two studios, which determine the correct studio for your use case.
 
-## Choosing the correct studio experience
+## Choose the correct studio experience
 
-There are currently two studios, the [Azure AI Foundry portal](https://ai.azure.com/explore/aiservices/vision) and the [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio) for building and validating  Document Intelligence models. As the experiences migrate to the new Azure AI Foundry portal, some experiences are available in both studios, while other experiences/models are only available in only one of the studios. To follow are a few guidelines for choosing the Studio experience for your needs. All of our [prebuilt models](overview.md#prebuilt-models) and [general extraction models](overview.md#document-analysis-models) are available on both studios.
+Currently, there are two studios for building and validating Document Intelligence models: the [Azure AI Foundry portal](https://ai.azure.com/explore/aiservices/vision) and [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio). As the experiences migrate to the new Azure AI Foundry portal, some experiences are available in both studios. Other experiences and models are available in only one of the studios.
 
-### When to use [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio)
+The following guidelines help you to choose the studio experience for your needs. All the [prebuilt models](overview.md#prebuilt-models) and [general extraction models](overview.md#document-analysis-models) are available for both studios.
 
-Document Intelligence Studio contains all features released on or before November 2024. For any of the v2.1, v3.0, v3.1 features, continue to use the Document Intelligence Studio. Studios provide a visual experience for labeling, training, and validating custom models. For custom document field extraction models, use the Document Intelligence Studio for template and neural models. Custom classification models can only be trained and used on Document Intelligence Studio. Use Document Intelligence Studio if you want to try out GA versions of the models from version v3.0, v3.1, and v4.0.
+### When to use Document Intelligence Studio
 
-### When to use [Azure AI Foundry portal](https://ai.azure.com/explore/aiservices/vision)
+Document Intelligence Studio contains all the features released on or before November 2024. For any of the v2.1, v3.0, v3.1 features, continue to use Document Intelligence Studio. 
 
-Start with the new Azure AI Foundry and try any of the prebuilt document models from `2024-11-30` version including general extraction models like Read or Layout.
+Document Intelligence Studio provides a visual experience for labeling, training, and validating custom models. For custom document field-extraction models, use Document Intelligence Studio for template and neural models. You can train and use custom classification models only on Document Intelligence Studio. Use Document Intelligence Studio if you want to try out generally available versions of the models from version v3.0, v3.1, and v4.0.
+
+### When to use the Azure AI Foundry portal
+
+Start with Azure AI Foundry and try any of the prebuilt document models from the 2024-11-30 version, including general extraction models like read or layout.
 
 ## Learn more about Document Intelligence Studio
 
-Select the studio experience from the following tabs to learn more about each studio and how you can get started.
+To learn more about each studio and how you can get started, use the following tabs to select the studio experience.
 
-### [**Document Intelligence Studio**](#tab/di-studio)
+### [Document Intelligence Studio](#tab/di-studio)
 
 > [!IMPORTANT]
 >
-> * Document Intelligence Studio has distinct URLs for sovereign cloud regions.
-> * Azure for US Government: [Document Intelligence Studio (`Azure Fairfax`)](https://formrecognizer.appliedai.azure.us/studio)
-> * Microsoft Azure operated by 21Vianet: [Document Intelligence Studio (`Azure China`)](https://formrecognizer.appliedai.azure.cn/studio)
+> Document Intelligence Studio has distinct URLs for sovereign cloud regions:
+> * Azure for US Government: [Document Intelligence Studio (Azure Fairfax)](https://formrecognizer.appliedai.azure.us/studio)
+> * Azure operated by 21Vianet: [Document Intelligence Studio (Azure in China)](https://formrecognizer.appliedai.azure.cn/studio)
 
-The studio supports Document Intelligence v3.0 and later API versions for model analysis and custom model training. Previously trained v2.1 models with labeled data are supported, but not v2.1 model training. Refer to the [REST API migration guide](v3-1-migration-guide.md) for detailed information about migrating from v2.1 to v3.0.
+Document Intelligence Studio supports Document Intelligence v3.0 and later API versions for model analysis and custom model training. Previously trained v2.1 models with labeled data are supported, but not v2.1 model training. For information about migrating from v2.1 to v3.0, see the [REST API migration guide](v3-1-migration-guide.md).
 
-Use the [Document Intelligence Studio quickstart](quickstarts/try-document-intelligence-studio.md) to get started analyzing documents with document analysis or prebuilt models. Build custom models and reference the models in your applications using one of the [language specific `SDKs`](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true). 
+Use the [Document Intelligence Studio quickstart](quickstarts/try-document-intelligence-studio.md) to start analyzing documents with document analysis or prebuilt models. Build custom models and reference the models in your applications by using one of the [language-specific SDKs](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true).
 
 ### Document Intelligence model support
 
 Use the help wizard, labeling interface, training step, and interactive visualizations to understand how each feature works.
 
-* **Read**: Try out Document Intelligence's [Studio Read feature](https://documentintelligence.ai.azure.com/studio/read) with sample documents or your own documents and extract text lines, words, detected languages, and handwritten style if detected. To learn more, *see* [Read overview](prebuilt/read.md).
-
-* **Layout**: Try out Document Intelligence's [Studio Layout feature](https://documentintelligence.ai.azure.com/studio/layout) with sample documents or your own documents and extract text, tables, selection marks, and structure information. To learn more, *see* [Layout overview](prebuilt/layout.md).
-
-* **Prebuilt models**: Document Intelligence's prebuilt models enable you to add intelligent document processing to your apps and flows without having to train and build your own models. As an example, start with the [Studio Invoice feature](https://documentintelligence.ai.azure.com/studio/prebuilt?formType=invoice). To learn more, *see* [Models overview](model-overview.md).
-
-* **Custom extraction models**: Document Intelligence's [Studio Custom models feature](https://documentintelligence.ai.azure.com/studio/custommodel/projects) enables you to extract fields and values from models trained with your data, tailored to your forms and documents. To extract data from multiple form types, create standalone custom models or combine two, or more, custom models and create a composed model. Test the custom model with your sample documents and iterate to improve the model. To learn more, *see* the [Custom models overview](train/custom-model.md).
-
-* **Custom classification models**: Document classification is a new scenario supported by Document Intelligence. The document classifier API supports classification and splitting scenarios. Train a classification model to identify the different types of documents your application supports. The input file for the classification model can contain multiple documents and classifies each document within an associated page range. To learn more, *see* [custom classification models](train/custom-classifier.md).
-
-* **Add-on Capabilities**: Document Intelligence supports more sophisticated analysis capabilities. These optional capabilities can be enabled and disabled in the studio using the `Analyze Options` button in each model page. There are four add-on capabilities available: `highResolution`, `formula`, `font`, and `barcode extraction` capabilities. To learn more, *see* [Add-on capabilities](concept-add-on-capabilities.md).
-
+* **Read**: Try out the [Document Intelligence Studio read feature](https://documentintelligence.ai.azure.com/studio/read) with sample documents or your own documents. Extract text lines, words, detected languages, and handwritten style, if detected. To learn more, see [Read overview](prebuilt/read.md).
+* **Layout**: Try out the [Document Intelligence layout feature](https://documentintelligence.ai.azure.com/studio/layout) with sample documents or your own documents. Extract text, tables, selection marks, and structure information. To learn more, see [Layout overview](prebuilt/layout.md).
+* **Prebuilt models**: Use the Document Intelligence prebuilt models to add intelligent document processing to your apps and flows without having to train and build your own models. As an example, start with the [Document Intelligence invoice feature](https://documentintelligence.ai.azure.com/studio/prebuilt?formType=invoice). To learn more, see [Models overview](model-overview.md).
+* **Custom extraction models**: Use the [Document Intelligence Studio custom models feature](https://documentintelligence.ai.azure.com/studio/custommodel/projects) to extract fields and values from models that are trained with your data and tailored to your forms and documents. To extract data from multiple form types, create standalone custom models. You can also combine two or more custom models and create a composed model. Test the custom model with your sample documents and iterate to improve the model. To learn more, see [Custom models overview](train/custom-model.md).
+* **Custom classification models**: Document classification is a new scenario supported by Document Intelligence. The document classifier API supports classification and splitting scenarios. Train a classification model to identify the different types of documents that your application supports. The input file for the classification model can contain multiple documents and classifies each document within an associated page range. To learn more, see [Custom classification models](train/custom-classifier.md).
+* **Add-on capabilities**: Document Intelligence supports more sophisticated analysis capabilities. You can enable and disable these optional capabilities in the studio by using **Analyze Options** on each model page. Four add-on capabilities are available: `highResolution`, `formula`, `font`, and `barcode extraction`. To learn more, see [Add-on capabilities](concept-add-on-capabilities.md).
 
-### [**Azure AI Foundry portal**](#tab/ai-foundry)
+### [Azure AI Foundry portal](#tab/ai-foundry)
 
-Document Intelligence is part of the Azure AI services offerings in the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs). Each of the Azure AI services helps developers and organizations rapidly create intelligent, cutting-edge, market-ready, and responsible applications with out-of-the-box and prebuilt and customizable APIs and models.
+Document Intelligence is part of the Azure AI services offerings in the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs). Each of the Azure AI services helps developers and organizations rapidly create intelligent and responsible applications. Developers can use the prebuilt and customizable APIs and models to make their applications.
 
-Learn how to [connect your AI services hub](../../ai-services/connect-services-ai-foundry-portal.md) with AI services and get started using Document Intelligence.
+Learn how to [connect your AI services hub](../../ai-services/connect-services-ai-foundry-portal.md) with AI services and start using Document Intelligence.
 
 ---
 
-## Next steps
+## Related content
 
-* Visit [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
-* Visit [Azure AI Foundry portal](https://ai.azure.com/explore/aiservices/vision).
-* Get started with [Document Intelligence Studio quickstart](quickstarts/get-started-studio.md).
+* See [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
+* See the [Azure AI Foundry portal](https://ai.azure.com/explore/aiservices/vision).
+* Get started with the [Document Intelligence Studio quickstart](quickstarts/get-started-studio.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence Studio 概要の更新"
}
```

### Explanation
このコードの変更では、Document Intelligence Studio の概要が更新され、情報が整理されました。主な変更点は、文言の明確化や構造の見直しが行われ、ユーザーがこのサービスの機能を尋ねやすくなっています。具体的には、スタジオの目的や使用方法、各機能の説明がより分かりやすくなっています。

例えば、「Document Intelligence Studio」は「Azure AI Document Intelligence Studio」として明記され、これにより名称の一致が強化されました。また、ドキュメントの構成が改善され、ユーザーがどのようにサービスを利用できるかが明確に示されています。各機能の説明では、文の明確さと簡潔さを向上させ、特にプレビルトモデルやカスタムモデルについてのガイダンスが整理されました。

さらに、スタジオの選択に関するガイダンスが更新され、Azure AI Foundry ポータルとの関係が明確化されています。ユーザーは各スタジオの使用シナリオについて把握しやすくなり、目的に応じたスタジオを選ぶ際の判断材料が提供されています。

最後に、関連するコンテンツへのリンクも更新され、ユーザーが次に参照すべき情報を容易に見つけられるよう配慮されています。全体的に、ユーザーが Document Intelligence Studio をより効果的に利用できるようガイドラインが明確にされています。

## articles/ai-services/document-intelligence/whats-new.md{#item-1ec8d3}

<details>
<summary>Diff</summary>
````diff
@@ -135,7 +135,7 @@ The Document Intelligence [**2024-07-31-preview**](/rest/api/aiservices/document
 
 ## May 2024
 
-The Document Intelligence Studio adds support for Microsoft Entra (formerly Azure Active Directory) authentication. For more information, *see* [Authentication in Document Intelligence Studio](quickstarts/get-started-studio.md#authentication-in-studio).
+The Document Intelligence Studio adds support for Microsoft Entra (formerly Azure Active Directory) authentication. For more information, *see* [Authentication in Document Intelligence Studio](quickstarts/get-started-studio.md#authentication-in-document-intelligence-studio).
 
 ## February 2024
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence の新機能に関する更新"
}
```

### Explanation
このコードの変更では、Document Intelligence の「What's New」セクションにおいて、Microsoft Entra（旧 Azure Active Directory）認証のサポートに関する情報が更新されました。具体的には、リンク先のテキストが「Authentication in Document Intelligence Studio」から「Authentication in Document Intelligence Studio」と変更されました。

この変更は、文書内での用語の一貫性を改善するものであり、ユーザーが必要な情報をより正確に見つけられるようになります。このアップデートは、Document Intelligence Studio の認証方法に関する重要な情報を強調し、ユーザーが新しい機能を活用する際に役立つリンクを明確に提供しています。全体として、コンテンツの明確さと利用しやすさが向上しました。


