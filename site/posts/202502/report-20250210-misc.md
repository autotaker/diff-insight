---
date: '2025-02-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4912a73...MicrosoftDocs:879fbd3
summary: 今回のコードDiffでは、AzureのドキュメントインテリジェンスAPIに関する複数のドキュメントが更新されました。主な変更点は、新機能として`AnalyzeDocumentRequest`のインポートがPython
  SDKに追加されたこと、そしてバージョン3.1から4.0への移行ガイドが破壊的変更を反映して更新されたことです。その他、C# SDKのクイックスタートガイドの明確化や、外部画像からのテキスト抽出に関する更新が行われました。これにより、開発者はAPIを効率的に使用できるようになり、リソース設定が容易になります。全体として、これらの変更はAzureユーザーにとってより便利なツール体験を提供します。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4912a73...MicrosoftDocs:879fbd3){target="_blank"}

# ハイライト

今回のコードDiffにおいては、AzureのドキュメントインテリジェンスAPIに関連する複数のドキュメントが更新されました。変更は主に以下の通りです：

- **新機能**: 新たに `AnalyzeDocumentRequest` のインポートがPython SDKに追加されました。
- **破壊的変更**: ドキュメントインテリジェンスAPIのバージョン3.1から4.0への移行ガイドでは、主要な破壊的変更が記載され、移行プロセスが容易になるようにガイドが更新されました。

## 新機能

- `AnalyzeDocumentRequest` のインポート追加により、Python SDKの使用が便利に。
- `read.md` では、外部画像からのテキスト抽出を使いやすくする更新が加えられています。
  
## 破壊的変更

- Version 4.0への移行ガイドにて、APIの更新によるサポート変更と新機能を反映。
  
## その他の更新

- C# SDKのクイックスタートガイドでは、記述の明確化と簡略化でユーザーエクスペリエンスを向上。
- 機能制限とエンドポイントの説明を強化し、正確な利用情報の提供を目的。

# インサイト

これらの変更は、Azureドキュメントインテリジェンスサービスを利用する開発者にとって大きな価値を提供します。まず、Python SDKへの`AnalyzeDocumentRequest`のインポート追加は、APIを使用する際の開発者の手間を省きます。このようなインポートの明確化により、開発効率が向上し、より迅速にコーディングができます。

リード機能のドキュメントに関する更新においては、外部画像からテキストを抽出する機能の説明が改善され、サポートされるフォーマットや制限事項の理解が深まります。特に、PDFファイルの検索可能なPDF機能の利用に関する詳細なガイダンスは、ユーザーの混乱を避け、最適な使用法を確保します。

移行ガイドの更新に関しては、バージョン3.1から4.0へのスムーズな移行をサポートするために不可欠です。このガイドは、APIの破壊的変更を明確に示し、新しいバージョンでの注意事項を開示しており、これにより、開発者は新機能を活用しつつ、プロジェクトを最新に保つことができます。

最後に、C# SDKのクイックスタートガイドの改善は、開発者がリソースを効果的に設定するための道筋を示し、情報へのアクセスを簡略化することで、迅速に開発を進められるよう支援しています。

全体として、これらのアップデートはAzureユーザーに対して、よりスムーズで効率的なツール体験を提供し、実際の開発プロセスを向上させる重要なステップです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [python-sdk.md](#item-52b6d7) | minor update | Python SDKの更新: AnalyzeDocumentRequestのインポート追加 | modified | 6 | 0 | 6 | 
| [read.md](#item-06f32f) | minor update | ドキュメントインテリジェンスのリード機能に関する更新 | modified | 162 | 17 | 179 | 
| [csharp-sdk.md](#item-ee69c7) | minor update | C# SDKクイックスタート文書の改善 | modified | 2 | 2 | 4 | 
| [v3-1-migration-guide.md](#item-6f9943) | breaking change | Document Intelligence API v4.0への移行ガイドの更新 | modified | 20 | 23 | 43 | 


# Modified Contents
## articles/ai-services/document-intelligence/how-to-guides/includes/v4-0/python-sdk.md{#item-52b6d7}

<details>
<summary>Diff</summary>
````diff
@@ -80,6 +80,7 @@ import os
 from azure.core.credentials import AzureKeyCredential
 from azure.ai.documentintelligence import DocumentIntelligenceClient
 from azure.ai.documentintelligence.models import AnalyzeResult
+from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
 
 # use your `key` and `endpoint` environment variables
 key = os.environ.get('DI_KEY')
@@ -183,6 +184,7 @@ import os
 from azure.core.credentials import AzureKeyCredential
 from azure.ai.documentintelligence import DocumentIntelligenceClient
 from azure.ai.documentintelligence.models import AnalyzeResult
+from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
 
 
 # use your `key` and `endpoint` environment variables
@@ -263,6 +265,7 @@ import os
 from azure.core.credentials import AzureKeyCredential
 from azure.ai.documentintelligence import DocumentIntelligenceClient
 from azure.ai.documentintelligence.models import AnalyzeResult
+from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
 
 # use your `key` and `endpoint` environment variables
 key = os.environ.get('DI_KEY')
@@ -458,6 +461,7 @@ import os
 from azure.core.credentials import AzureKeyCredential
 from azure.ai.documentintelligence import DocumentIntelligenceClient
 from azure.ai.documentintelligence.models import AnalyzeResult
+from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
 
 # use your `key` and `endpoint` environment variables
 key = os.environ.get('DI_KEY')
@@ -648,6 +652,7 @@ import os
 from azure.core.credentials import AzureKeyCredential
 from azure.ai.documentintelligence import DocumentIntelligenceClient
 from azure.ai.documentintelligence.models import AnalyzeResult
+from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
 
 # use your `key` and `endpoint` environment variables
 key = os.environ.get('DI_KEY')
@@ -740,6 +745,7 @@ import os
 from azure.core.credentials import AzureKeyCredential
 from azure.ai.documentintelligence import DocumentIntelligenceClient
 from azure.ai.documentintelligence.models import AnalyzeResult
+from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
 
 # use your `key` and `endpoint` environment variables
 key = os.environ.get('DI_KEY')
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python SDKの更新: AnalyzeDocumentRequestのインポート追加"
}
```

### Explanation
この変更は、Python SDKのドキュメントに対する小さな更新です。具体的には、`AnalyzeDocumentRequest` モデルをインポートする行が新たに追加されました。これにより、ドキュメントインテリジェンスの機能を利用する際に必要なリクエスト型が明示的に定義され、開発者がAPIを使用するための情報が強化されています。この変更は、複数の場所で行われており、合計で6行が増加しましたが、削除された行はありません。この更新は、Azureのドキュメントインテリジェンス機能を扱う際のコードの可読性と使いやすさを向上させることを目的としています。

## articles/ai-services/document-intelligence/prebuilt/read.md{#item-06f32f}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ ms.author: lajanuar
 
 > [!NOTE]
 >
-> For extracting text from external images like labels, street signs, and posters, use the [Azure AI Image Analysis v4.0 Read](../../Computer-vision/concept-ocr.md) feature optimized for general, non-document images with a performance-enhanced synchronous API that makes it easier to embed OCR in real-time user experience scenarios.
+> To extract text from external images like labels, street signs, and posters, use the [Azure AI Image Analysis v4.0 Read](../../Computer-vision/concept-ocr.md) feature optimized for general (not document) images with a performance-enhanced synchronous API. This capability makes it easier to embed OCR in real-time user experience scenarios.
 >
 
 Document Intelligence Read Optical Character Recognition (OCR) model runs at a higher resolution than Azure AI Vision Read and extracts print and handwritten text from PDF documents and scanned images. It also includes support for extracting text from Microsoft Word, Excel, PowerPoint, and HTML documents. It detects paragraphs, text lines, words, locations, and languages. The Read model is the underlying OCR engine for other Document Intelligence prebuilt models like Layout, General Document, Invoice, Receipt, Identity (ID) document, Health insurance card, W2 in addition to custom models.
@@ -83,11 +83,11 @@ See our [Language Support—document analysis models](../language-support/ocr.md
 ## Data extraction (v4)
 
 > [!NOTE]
-> Microsoft Word and HTML file are supported in v4.0. Compared with PDF and images, below features are not supported:
+> Microsoft Word and HTML file are supported in v4.0. The following capabilities are currently not supported:
 >
-> * There are no angle, width/height and unit with each page object.
-> * For each object detected, there is no bounding polygon or bounding region.
-> * Page range (`pages`) is not supported as a parameter.
+> * No angle, width/height, and unit returned with each page object.
+> * No bounding polygon or bounding region for each object detected.
+> * No page range (`pages`) as a parameter returned.
 > * No `lines` object.
 
 ## Searchable PDFs
@@ -96,16 +96,16 @@ The searchable PDF capability enables you to convert an analog PDF, such as scan
 
   > [!IMPORTANT]
   >
-  > * Currently, the searchable PDF capability is only supported by Read OCR model `prebuilt-read`. When using this feature, please specify the `modelId` as `prebuilt-read`, as other model types will return error for this preview version.
-  > * Searchable PDF is included with the 2024-11-30 GA `prebuilt-read` model with no additional cost for generating a searchable PDF output.
+  > * Currently, only  the Read OCR model `prebuilt-read` supports the searchable PDF capability. When using this feature, specify the `modelId` as `prebuilt-read`. Other model types return an error for this preview version.
+  > * Searchable PDF is included with the `2024-11-30` GA `prebuilt-read` model with no added cost for generating a searchable PDF output.
 
 ### Use searchable PDFs
 
 To use searchable PDF, make a `POST` request using the `Analyze` operation and specify the output format as `pdf`:
 
 ```bash
 
-     POST /documentModels/prebuilt-read:analyze?output=pdf
+     POST {endpoint}/documentintelligence/documentModels/prebuilt-read:analyze?_overload=analyzeDocument&api-version=2024-11-30&output=pdf
      {...}
      202
 ```
@@ -122,7 +122,152 @@ Upon successful completion, the PDF can be retrieved and downloaded as `applicat
      {...}
 
      // Upon successful completion, retrieve the PDF as application/pdf.
-     GET /documentModels/prebuilt-read/analyzeResults/{resultId}/pdf
+     GET {endpoint}/documentintelligence/documentModels/prebuilt-read/analyzeResults/{resultId}/pdf?api-version=2024-11-30
+URI Parameters
+Name    In    Required    Type    Description
+endpoint    path    True    
+string
+
+uri    
+The Document Intelligence service endpoint.
+
+modelId    path    True    
+string
+
+Unique document model name.
+
+Regex pattern: ^[a-zA-Z0-9][a-zA-Z0-9._~-]{1,63}$
+
+resultId    path    True    
+string
+
+uuid    
+Analyze operation result ID.
+
+api-version    query    True    
+string
+
+The API version to use for this operation.
+
+Responses
+Name    Type    Description
+200 OK    
+file
+
+The request has succeeded.
+
+Media Types: "application/pdf", "application/json"
+
+Other Status Codes    
+DocumentIntelligenceErrorResponse
+
+An unexpected error response.
+
+Media Types: "application/pdf", "application/json"
+
+Security
+Ocp-Apim-Subscription-Key
+Type: apiKey
+In: header
+
+OAuth2Auth
+Type: oauth2
+Flow: accessCode
+Authorization URL: https://login.microsoftonline.com/common/oauth2/authorize
+Token URL: https://login.microsoftonline.com/common/oauth2/token
+
+Scopes
+Name    Description
+https://cognitiveservices.azure.com/.default    
+Examples
+Get Analyze Document Result PDF
+Sample request
+HTTP
+HTTP
+
+Copy
+GET https://myendpoint.cognitiveservices.azure.com/documentintelligence/documentModels/prebuilt-invoice/analyzeResults/3b31320d-8bab-4f88-b19c-2322a7f11034/pdf?api-version=2024-11-30
+Sample response
+Status code:
+200
+JSON
+
+Copy
+"{pdfBinary}"
+Definitions
+Name    Description
+DocumentIntelligenceError    
+The error object.
+
+DocumentIntelligenceErrorResponse    
+Error response object.
+
+DocumentIntelligenceInnerError    
+An object containing more specific information about the error.
+
+DocumentIntelligenceError
+The error object.
+
+Name    Type    Description
+code    
+string
+
+One of a server-defined set of error codes.
+
+details    
+DocumentIntelligenceError[]
+
+An array of details about specific errors that led to this reported error.
+
+innererror    
+DocumentIntelligenceInnerError
+
+An object containing more specific information than the current object about the error.
+
+message    
+string
+
+A human-readable representation of the error.
+
+target    
+string
+
+The target of the error.
+
+DocumentIntelligenceErrorResponse
+Error response object.
+
+Name    Type    Description
+error    
+DocumentIntelligenceError
+
+Error info.
+
+DocumentIntelligenceInnerError
+An object containing more specific information about the error.
+
+Name    Type    Description
+code    
+string
+
+One of a server-defined set of error codes.
+
+innererror    
+DocumentIntelligenceInnerError
+
+Inner error.
+
+message    
+string
+
+A human-readable representation of the error.
+
+In this article
+URI Parameters
+Responses
+Security
+Examples
+
      200 OK
      Content-Type: application/pdf
 ```
@@ -294,7 +439,7 @@ Find more samples on GitHub:
 
 > [!NOTE]
 >
-> For extracting text from external images like labels, street signs, and posters, use the [Azure AI Image Analysis v4.0 Read](../..//Computer-vision/concept-ocr.md) feature optimized for general, non-document images with a performance-enhanced synchronous API that makes it easier to embed OCR in your user experience scenarios.
+> To extract text from external images like labels, street signs, and posters, use the [Azure AI Image Analysis v4.0 Read](../../Computer-vision/concept-ocr.md) feature optimized for general (not document) images with a performance-enhanced synchronous API. This capability makes it easier to embed OCR in real-time user experience scenarios.
 >
 
 Document Intelligence Read Optical Character Recognition (OCR) model runs at a higher resolution than Azure AI Vision Read and extracts print and handwritten text from PDF documents and scanned images. It also includes support for extracting text from Microsoft Word, Excel, PowerPoint, and HTML documents. It detects paragraphs, text lines, words, locations, and languages. The Read model is the underlying OCR engine for other Document Intelligence prebuilt models like Layout, General Document, Invoice, Receipt, Identity (ID) document, Health insurance card, W2 in addition to custom models.
@@ -368,11 +513,11 @@ See our [Language Support—document analysis models](../language-support/ocr.md
 ## Data extraction
 
 > [!NOTE]
-> Microsoft Word and HTML file are supported in v3.1 and later versions. Compared with PDF and images, below features are not supported:
+> Microsoft Word and HTML file are supported in v4.0. The following capabilities are currently not supported:
 >
-> * There are no angle, width/height and unit with each page object.
-> * For each object detected, there is no bounding polygon or bounding region.
-> * Page range (`pages`) is not supported as a parameter.
+> * No angle, width/height, and unit returned with each page object.
+> * No bounding polygon or bounding region for each object detected.
+> * No page range (`pages`) as a parameter returned.
 > * No `lines` object.
 
 ## Searchable PDF
@@ -381,9 +526,9 @@ The searchable PDF capability enables you to convert an analog PDF, such as scan
 
   > [!IMPORTANT]
   >
-  > * Currently, the searchable PDF capability is only supported by Read OCR model `prebuilt-read`. When using this feature, please specify the `modelId` as `prebuilt-read`, as other model types will return an error.
-  > * Searchable PDF is included with the 2024-11-30 `prebuilt-read` model with no additional cost for generating a searchable PDF output.
->   * Searchable PDF currently only supports PDF files as input. Support for other file types, such as image files, will be available later.
+  > * Currently, only Read OCR model `prebuilt-read` supports the searchable PDF capability. When using this feature, specify the `modelId` as `prebuilt-read`. Other model types return an error.
+  > * Searchable PDF is included with the `2024-11-30` `prebuilt-read` model with no added cost for generating a searchable PDF output.
+>   * Searchable PDF currently only supports PDF files as input. 
 
 ### Use searchable PDF
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのリード機能に関する更新"
}
```

### Explanation
この変更は、Azure AIのドキュメントインテリジェンスに関する説明を含むリード機能の文書に対する重要な更新を行っています。主な変更内容は、外部画像からテキストを抽出する際の注意書きの記述を改善し、文書の情報をより明確にしています。また、様々な機能のサポート状況や制限事項についての説明を追加し、特にPDFファイルに対する検索可能なPDF機能の使用方法を詳細に記述しています。

具体的には、162行の追加と17行の削除が行われ、最終的には合計179行の変更がありました。具体的な改良点としては、APIのエンドポイント、リクエストパラメータ、セキュリティ情報、レスポンスタイプの明確化などが含まれています。これにより、ユーザーは新しい機能をより効果的に利用できるようになります。

## articles/ai-services/document-intelligence/quickstarts/includes/csharp-sdk.md{#item-ee69c7}

<details>
<summary>Diff</summary>
````diff
@@ -47,7 +47,7 @@ In this quickstart, use the following features to analyze and extract data and v
 * You can use the free pricing tier (`F0`) to try the service, and upgrade later to a paid tier for production.
 
 > [!TIP]
-> Create an Azure AI services resource if you plan to access multiple Azure AI services under a single endpoint/key. For Document Intelligence access only, create a Document Intelligence resource. Please note that you'll  need a single-service resource if you intend to use [Microsoft Entra authentication](/azure/active-directory/authentication/overview-authentication).
+> Create an Azure AI services resource if you plan to access multiple Azure AI services under a single endpoint/key. For Document Intelligence access only, create a Document Intelligence resource. You need a single-service resource if you intend to use [Microsoft Entra authentication](/azure/active-directory/authentication/overview-authentication).
 
 * After your resource deploys, select **Go to resource**. You need the key and endpoint from the resource you create to connect your application to the Document Intelligence API. You paste your key and endpoint into the code later in the quickstart:
 
@@ -62,7 +62,7 @@ In this quickstart, use the following features to analyze and extract data and v
 * You can use the free pricing tier (`F0`) to try the service, and upgrade later to a paid tier for production.
 
 > [!TIP]
-> Create an Azure AI services resource if you plan to access multiple Azure AI services under a single endpoint/key. For Form Recognizer access only, create a Form Recognizer resource. Please note that you'll  need a single-service resource if you intend to use [Microsoft Entra authentication](/azure/active-directory/authentication/overview-authentication).
+> Create an Azure AI services resource if you plan to access multiple Azure AI services under a single endpoint/key. For Form Recognizer access only, create a Form Recognizer resource. You need a single-service resource if you intend to use [Microsoft Entra authentication](/azure/active-directory/authentication/overview-authentication).
 
 * After your resource deploys, select **Go to resource**. You need the key and endpoint from the resource you create to connect your application to the Form Recognizer API. You paste your key and endpoint into the code later in the quickstart:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDKクイックスタート文書の改善"
}
```

### Explanation
この変更は、Azure AIサービスのC# SDKに関するクイックスタートのドキュメントに対する小さな更新です。具体的には、開発者がリソースを作成する際のアドバイスにおいて、文言の明確化と簡略化が行われました。 

変更の内容としては、関連するリソースを作成する際の指示文が若干変更されており、「必要」が文中に追加され、より自然な読解となるようにされています。この更新は、ドキュメントの可読性を向上させ、ユーザーがAzure AIサービスを利用するためのガイダンスをより効果的に提供します。

全体で2行が追加され、2行が削除されており、合計で4行の変更が行われています。このような小規模な更新は、ユーザーの混乱を避け、正確な情報を提供するために重要です。

## articles/ai-services/document-intelligence/versioning/v3-1-migration-guide.md{#item-6f9943}

<details>
<summary>Diff</summary>
````diff
@@ -1,34 +1,30 @@
 ---
 title: "How-to: Migrate Document Intelligence applications to v3.1."
 titleSuffix: Azure AI services
-description: In this how-to guide, learn the differences between Document Intelligence API v3.0 and v3.1 and how to move to the newer version of the API.
+description: In this how-to guide, learn the differences between Document Intelligence API versions and how to move to the newer version of the API.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 02/07/2025
 ms.author: lajanuar
-monikerRange: '<=doc-intel-3.1.0'
+monikerRange: '<=doc-intel-4.0.0'
 ---
 
 <!-- markdownlint-disable MD004 -->
-# Document Intelligence v3.1 migration
-
-::: moniker range="<=doc-intel-3.1.0"
-[!INCLUDE [applies to v3.1, v3.0, and v2.1](../includes/applies-to-v40-v31-v30-v21.md)]
-::: moniker-end
+# Document Intelligence v4.0 migration
 
 > [!IMPORTANT]
 >
-> Document Intelligence REST API v3.1 introduces breaking changes in the REST API request and analyze response JSON.
+> Document Intelligence REST API v4.0 introduces breaking changes in the REST API request and analyze response JSON.
 
-## Migrating from v3.1 API version
+## Migrating from v3.1 to v4.0
 
-Preview APIs are periodically deprecated. If you're using a preview API version, update your application to target the GA API version. To migrate from a preview API version to the `2023-11-30 (GA)` API version using the SDK, update to the [current version of the language specific SDK](sdk-overview-v3-1.md).
+Preview APIs are periodically deprecated. If you're using a preview API version, update your application to target the GA API version. To migrate from a preview API version to the `2024-11-30 (GA)` API version using the SDK, update to the [current version of the language specific SDK](sdk-overview-v4-0.md).
 
 ### Analysis features
 
-| Model ID | Text Extraction | Paragraphs | Paragraph Roles | Selection Marks | Tables | Key-Value Pairs | Languages | Barcodes | Document Analysis | Formulas* | StyleFont* | OCR High Resolution* |
+| Model ID | Text Extraction | Paragraphs | Paragraph Roles | Selection Marks | Tables | Key-Value Pairs | Languages | Barcodes | Document Analysis | Formulas* | StyleFont* | `OCR` High Resolution* |
 | --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
 | prebuilt-read | ✓ | ✓ |  |  |  |  | O | O |  | O | O | O |
 | prebuilt-layout | ✓ | ✓ | ✓ | ✓ | ✓ |  | O | O |  | O | O | O |
@@ -60,7 +56,7 @@ Compared with v3.0, Document Intelligence v3.1 introduces several new features a
 * New document type support in [ID document](../prebuilt/id-document.md) model.
 * New prebuilt [Health insurance card](../prebuilt/health-insurance-card.md) model.
 * Office/HTML files are supported in prebuilt-read model, extracting words and paragraphs without bounding boxes. Embedded images are no longer supported. If add-on features are requested for Office/HTML files, an empty array is returned without errors.
-* Model expiration for custom extraction and classification models - Our new custom models build upon on a large base model that we update periodically for quality improvement. An expiration date is introduced to all custom models to enable the retirement of the corresponding base models.  Once a custom model expires, you need to retrain the model using the latest API version (base model).
+* Model expiration for custom extraction and classification models - Our new custom models build upon on a large base model that we update periodically for quality improvement. An expiration date is introduced to all custom models to enable the retirement of the corresponding base models. Once a custom model expires, you need to retrain the model using the latest API version (base model).
 
 ```http
 GET /documentModels/{customModelId}?api-version={apiVersion}
@@ -87,8 +83,8 @@ GET /documentModels/{customModelId}?api-version={apiVersion}
 }
 ```
 
-* An optional `features` query parameter to Analyze operations can optionally enable specific features.  Some premium features can incur added billing. Refer to [Analyze feature list](#analysis-features) for details.
-* Extend extracted currency field objects to output a normalized currency code field when possible.  Currently, current fields can return amount (ex. 123.45) and currencySymbol (ex. $).  This feature maps the currency symbol to a canonical ISO 4217 code (ex. USD).  The model can optionally utilize the global document content to disambiguate or infer the currency code.
+* An optional `features` query parameter to Analyze operations can optionally enable specific features. Some premium features can incur added billing. Refer to [Analyze feature list](#analysis-features) for details.
+* Extend extracted currency field objects to output a normalized currency code field when possible. Currently, current fields can return amount (ex. 123.45) and currencySymbol (ex. $). This feature maps the currency symbol to a canonical ISO 4217 code (ex. USD). The model can optionally utilize the global document content to disambiguate or infer the currency code.
 
 ```http
 {
@@ -140,8 +136,8 @@ https://{your-form-recognizer-endpoint}/formrecognizer/documentModels/{modelId}/
 ### Analyze operation
 
 * The request payload and call pattern remain unchanged.
-* The Analyze operation specifies the input document and content-specific configurations, it returns the analyze result URL via the Operation-Location header in the response.
-* Poll this Analyze Result URL, via a GET request to check the status of the analyze operation (minimum recommended interval between requests is 1 second).
+* The `Analyze` operation specifies the input document and content-specific configurations, it returns the analyzed result URL via the Operation-Location header in the response.
+* Poll the `Analyze Result` URL, via a GET request to check the status of the `Analyze` operation (minimum recommended interval between requests is 1 second).
 * Upon success, status is set to succeeded and [analyzeResult](#changes-to-analyze-result) is returned in the response body. If errors are encountered, status sets to `failed`, and an error is returned.
 
 | Model | v2.0 | v2.1 | v3.1 |
@@ -183,7 +179,7 @@ Base 64 encoding is also supported in Document Intelligence v3.0:
 Parameters that continue to be supported:
 
 * `pages` : Analyze only a specific subset of pages in the document. List of page numbers indexed from the number `1` to analyze. Ex. "1-3,5,7-9"
-* `locale` : Locale hint for text recognition and document analysis. Value can contain only the language code (ex. `en`, `fr`) or BCP 47 language tag (ex. "en-US").
+* `locale` : Locale hint for text recognition and document analysis. Value can contain only the language code (ex. `en`, `fr`) or `BCP` 47 language tag (ex. "en-US").
 
 Parameters no longer supported:
 
@@ -193,7 +189,7 @@ The new response format is more compact and the full output is always returned.
 
 ## Changes to analyze result
 
-Analyze response is refactored to the following top-level results to support multi-page elements.
+Analyze response is refactored to the following top-level results and supports multi-page elements.
 
 * `pages`
 * `tables`
@@ -204,7 +200,7 @@ Analyze response is refactored to the following top-level results to support mul
 
 > [!NOTE]
 >
-> The analyzeResult response changes includes a number of changes like moving up from a property of pages to a top lever property within analyzeResult.
+> The `analyzeResult` response changes include changes such as moving up from a property of pages to a top lever property within `analyzeResult`.
 
 ```json
 
@@ -373,7 +369,7 @@ POST https://{your-form-recognizer-endpoint}/formrecognizer/documentModels:compo
 The call pattern for copy model remains unchanged:
 
 * Authorize the copy operation with the target resource calling ```authorizeCopy```. Now a POST request.
-* Submit the authorization to the source resource to copy the model calling ```copyTo```
+* Submit the authorization to the source resource and copy the model calling ```copyTo```
 * Poll the returned operation to validate the operation completed successfully
 
 The only changes to the copy model function are:
@@ -415,9 +411,9 @@ List models are extended to now return prebuilt and custom models. All prebuilt
 GET https://{your-form-recognizer-endpoint}/formrecognizer/documentModels?api-version=2022-08-31
 ```
 
-## Change to get model
+## Change to get model operation
 
-As get model now includes prebuilt models, the get operation returns a ```docTypes``` dictionary. Each document type description includes name, optional description, field schema, and optional field confidence. The field schema describes the list of fields potentially returned with the document type.
+As `Get Model` now includes prebuilt models, the `Get` operation returns a ```docTypes``` dictionary. Each document type description includes name, optional description, field schema, and optional field confidence. The field schema describes the list of fields potentially returned with the document type.
 
 ```json
 GET https://{your-form-recognizer-endpoint}/formrecognizer/documentModels/{modelId}?api-version=2022-08-31
@@ -447,3 +443,4 @@ GET https://{your-form-recognizer-endpoint}/formrecognizer/info? api-version=202
 * [Review the new REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)
 * [What is Document Intelligence?](../overview.md)
 * [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md)
+0
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Document Intelligence API v4.0への移行ガイドの更新"
}
```

### Explanation
この変更は、AzureのドキュメントインテリジェンスAPIのバージョン3.1から4.0への移行ガイドに関する重要な更新です。主な目的は、APIの新しいバージョンに伴う破壊的変更を説明し、開発者がスムーズに移行できるようにするための情報を提供することです。

具体的には、ガイドのタイトルが「Document Intelligence v3.1 migration」から「Document Intelligence v4.0 migration」に変更され、APIのバージョンについての説明が見直されています。また、APIのリリース日付が更新され、ドキュメント中のリンクも新しいバージョンに合わせて修正されました。これにより、ユーザーは最新のSDKバージョンを使ってGA API版への更新方法を明確に理解できるようになります。

加えて、使用中のAPIがプレビュー版である場合の注意点や、モデルの有効期限に関する情報も更新されています。この改訂によって、ユーザーが新しい機能やサポート内容に基づいてアプリケーションを適切に対応させることができるようになっています。全体で20行の追加と23行の削除が行われ、合計43行の変更がありました。これらの変更は、ドキュメントを最新の状態に保ち、開発者がAPIの利用を円滑に行えるようにするために重要です。


