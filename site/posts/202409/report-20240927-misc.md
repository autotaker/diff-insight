---
date: '2024-09-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5e7dab7...MicrosoftDocs:552467e
summary: この差分では、主にドキュメントの更新、削除、修正が行われ、いくつかの新機能が追加されています。特に、カスタム要約機能に関するいくつかのドキュメントとPhi-3.5
  MoEモデルに関する情報が削除されたことが重要です。これにより、ユーザーへの影響が懸念されます。新たに追加されたリダイレクトルールにより、ユーザーは新しい関連情報にスムーズに遷移できるようになりました。また、様々な文書の削除や表現の微調整が行われ、全体的な可読性が向上しました。これらの変更は、ドキュメントの最新性を保つために重要な措置と言えます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5e7dab7...MicrosoftDocs:552467e){target="_blank"}

# ハイライト
この差分では主にドキュメントの更新、削除、および修正が行われ、いくつかの新機能が追加されています。特に重要なのは、カスタム要約機能に関するいくつかのドキュメントが削除されている点と、Phi-3.5 MoEモデルに関する情報が削除された点です。これらはユーザーにとって重大な影響を及ぼす可能性があります。

## 新機能
- 新しいリダイレクトルールの追加により、ユーザーが新しい関連情報にスムーズに遷移できるようになりました。

## 破壊的変更
- `data-formats.md`、`deploy-model.md`、`test-evaluate.md`、`quickstart.md`、`phi-3-5-moe.md` の削除。
- カスタム要約の言語サポート情報の削除。
- Phi-3.5 MoEチャットモデルの削除。

## その他の更新
- ドキュメントの日付や表現の微調整。
- リダイレクト設定の更新。
- リージョンとモデルの可用性に関する情報の追加。
- Phi-3モデルに関する新しい情報の追加。

# 洞察
この差分における最も重要な変更は、カスタム要約およびPhi-3.5 MoEモデルに関する複数のドキュメントの削除です。これらの削除は、利用者に対して大きな影響を与える可能性があります。以下、詳細を説明します。

## カスタム要約に関する文書の削除
カスタム要約機能に関する重要なドキュメントが削除されました。具体的には、データ形式、モデルのデプロイ、テストと評価、そしてクイックスタートガイドなどが含まれます。これにより、ユーザーはこれらの機能を使用する際に非常に重要なリソースを失いました。削除されたドキュメントには具体的な手順と重要なガイダンスが含まれており、その欠如は顧客体験および製品の利用可用性に負の影響を及ぼす恐れがあります。企業は代替のリソースや新しいドキュメントを提供する必要があります。

## Phi-3.5 MoEに関する文書の削除
Phi-3.5 MoEモデルに関するドキュメントが削除され、これは特に開発者にとって大きな影響を与える変更です。このモデルの詳細な使用方法や設定方法に関する情報を失うことで、開発者は他のモデルや方法に切り替える必要が出てくるかもしれません。Phi-3モデルのドキュメントが修正されましたが、Phi-3.5 MoEに関連する情報が失われました。

## リダイレクト設定の更新
リダイレクト設定が更新され、特定のドキュメントへの遷移が確保されました。これにより、ユーザーは古いドキュメントにアクセスする際に、新しい関連情報にスムーズに移動でき、ナビゲーションの利便性が向上しています。

## その他の変更
日付や文言の修正が行われ、全体のドキュメントの可読性が改善されています。また、リージョンとモデルの可用性に関する情報が追加され、サービスの透明性が向上しました。Phi-3モデルの情報が更新され、新しいリソースが提供されることで、ユーザーはより具体的な情報にアクセスしやすくなっています。

これらの変更は全体として、ドキュメントの最新性と明確性を保つための重要な措置であると同時に、ユーザーがドキュメントの変更に迅速に対応し、影響を最小限に抑えるための適切なサポートが必要であることを示しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [choose-model-feature.md](#item-03a77e) | minor update | ドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [concept-analyze-document-response.md](#item-856a8a) | minor update | ドキュメント応答の細部更新 | modified | 7 | 8 | 15 | 
| [concept-custom-classifier.md](#item-7d0313) | minor update | カスタム分類モデルのドキュメント更新 | modified | 5 | 6 | 11 | 
| [create-document-intelligence-resource.md](#item-b6c8c3) | minor update | ドキュメントインテリジェンスリソース作成ガイドの更新 | modified | 3 | 3 | 6 | 
| [service-limits.md](#item-5ceae5) | minor update | ドキュメントインテリジェンスのサービス制限に関する文書の更新 | modified | 2 | 2 | 4 | 
| [data-formats.md](#item-f7ca2c) | breaking change | カスタム要約のデータ形式に関する文書の削除 | removed | 0 | 178 | 178 | 
| [deploy-model.md](#item-bd52c9) | breaking change | カスタム要約モデルのデプロイに関する文書の削除 | removed | 0 | 57 | 57 | 
| [test-evaluate.md](#item-b4df1a) | breaking change | カスタム要約モデルのテストと評価に関する文書の削除 | removed | 0 | 44 | 44 | 
| [quickstart.md](#item-bf389e) | breaking change | カスタム要約のクイックスタートに関する文書の削除 | removed | 0 | 35 | 35 | 
| [development-options.md](#item-f33a53) | minor update | 開発オプションに関する文書の修正 | modified | 0 | 2 | 2 | 
| [language-support.md](#item-676e71) | minor update | カスタム要約に関する言語サポート情報の修正 | modified | 0 | 8 | 8 | 
| [region-support.md](#item-d74574) | minor update | リージョンサポートに関する情報の更新 | modified | 26 | 26 | 52 | 
| [toc.yml](#item-12f1f0) | minor update | 目次構成の更新 | modified | 31 | 45 | 76 | 
| [whats-new.md](#item-69b272) | minor update | 最新情報の更新 | modified | 4 | 0 | 4 | 
| [.openpublishing.redirection.ai-studio.json](#item-c75c21) | minor update | リダイレクト設定の更新 | modified | 5 | 0 | 5 | 
| [deploy-models-phi-3-5-moe.md](#item-9af6ea) | breaking change | Phi-3.5 MoEモデルのドキュメント削除 | removed | 0 | 1153 | 1153 | 
| [deploy-models-phi-3.md](#item-47e305) | minor update | Phi-3モデルのドキュメントの修正 | modified | 30 | 10 | 40 | 
| [llama-index.md](#item-613372) | minor update | LlamaIndexのモデル構成に関するリンク修正 | modified | 1 | 1 | 2 | 
| [model-catalog-overview.md](#item-278001) | minor update | Phi-3モデルのリストの整備 | modified | 1 | 1 | 2 | 
| [region-availability-maas.md](#item-35d79c) | minor update | マルチリージョンのサポートを示す新しいメタデータの追加 | modified | 2 | 1 | 3 | 
| [toc.yml](#item-2745cd) | minor update | Phi-3.5 MoEチャットモデルの削除 | modified | 0 | 2 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/choose-model-feature.md{#item-03a77e}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: overview
-ms.date: 08/07/2024
+ms.date: 09/26/2024
 ms.author: lajanuar
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントの日付更新"
}
```

### Explanation
このコードの差分は、ドキュメントの最終更新日を変更するための小規模な更新です。具体的には、`choose-model-feature.md`というファイル内の日付が「08/07/2024」から「09/26/2024」に変更されています。この変更により、ドキュメントの最新性が反映され、ユーザーは最新の情報を得ることができます。変更内容は、特にサービスの提供や情報が頻繁に更新される分野では重要です。

## articles/ai-services/document-intelligence/concept-analyze-document-response.md{#item-856a8a}

<details>
<summary>Diff</summary>
````diff
@@ -6,11 +6,10 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 08/07/2024
+ms.date: 09/26/2024
 ms.author: vikurpad
 ms.custom:
   - references_regions
-  - ignite-2023
 monikerRange: '>=doc-intel-3.0.0'
 ---
 
@@ -22,7 +21,7 @@ In this article, let's examine the different objects returned as part of the `An
 
 ## Analyze document request
 
-The Document Intelligence APIs analyze images, PDFs, and other document files to extract and detect various content, layout, style, and semantic elements. The analyze operation is an async API. Submitting a document returns an **Operation-Location** header that contains the URL to poll for completion. When an analysis request completes successfully, the response contains the elements described in the [model data extraction](concept-model-overview.md#model-data-extraction).
+The Document Intelligence APIs analyze images, PDFs, and other document files to extract and detect various content, layout, style, and semantic elements. The `Analyze` operation is an async API. Submitting a document returns an **Operation-Location** header that contains the URL to poll for completion. When an analysis request completes successfully, the response contains the elements described in the [model data extraction](concept-model-overview.md#model-data-extraction).
 
 ### Response elements
 
@@ -43,7 +42,7 @@ The top-level content property contains a concatenation of all content elements
 
 ## Analyze response
 
-The analyze response for each API returns different objects. API responses contain elements from component models where applicable.
+The `Analyze` response for each API returns different objects. API responses contain elements from component models where applicable.
 
 | Response content | Description | API |
 |--|--|--|
@@ -52,8 +51,8 @@ The analyze response for each API returns different objects. API responses conta
 | **styles**| Identified text element properties. | Read, Layout, General Document, Prebuilt, and Custom models|
 | **languages**| Identified language associated with each span of the text extracted | Read |
 | **tables**| Tabular content identified and extracted from the document. Tables relate to tables identified by the pretrained layout model. Content labeled as tables is extracted as structured fields in the documents object.| Layout, General Document, Invoice, and Custom models |
-| **figures**| Figures (charts, images) identified and extracted from the document, providing visual representations that aid in the understanding of complex information. | Layout model |
-| **sections** | Hierarchical document structure identified and extracted from the document. Section or subsection with the corresponding elements (paragraph, table, figure) attached to it. | Layout model |
+| **figures**| Figures (charts, images) identified and extracted from the document, providing visual representations that aid in the understanding of complex information. | The Layout model |
+| **sections** | Hierarchical document structure identified and extracted from the document. Section or subsection with the corresponding elements (paragraph, table, figure) attached to it. | The Layout model |
 | **keyValuePairs**| Key-value pairs recognized by a pretrained model. The key is a span of text from the document with the associated value. | General document and Invoice models |
 | **documents**| Fields recognized are returned in the `fields` dictionary within the list of documents| Prebuilt models, Custom models.|
 
@@ -142,7 +141,7 @@ Based on its position and styling, a cell can be classified as general content,
 Figures (charts, images) in documents play a crucial role in complementing and enhancing the textual content, providing visual representations that aid in the understanding of complex information. The figures object detected by the Layout model has key properties like `boundingRegions` (the spatial locations of the figure on the document pages, including the page number and the polygon coordinates that outline the figure's boundary), `spans` (details the text spans related to the figure, specifying their offsets and lengths within the document's text. This connection helps in associating the figure with its relevant textual context), `elements` (the identifiers for text elements or paragraphs within the document that are related to or describe the figure) and `caption`, if any.
 
 When *output=figures* is specified during the initial `Analyze` operation, the service generates cropped images for all detected figures that can be accessed via `/analyeResults/{resultId}/figures/{figureId}`.
-`FigureId` will be included in each figure object, following an undocumented convention of `{pageNumber}.{figureIndex}` where `figureIndex` resets to one per page.
+`FigureId` is included in each figure object, following an undocumented convention of `{pageNumber}.{figureIndex}` where `figureIndex` resets to one per page.
 
 ```json
 {
@@ -255,7 +254,7 @@ The semantic schema of a document type is described via the fields it contains.
 | date | Date | ISO 8601 - YYYY-MM-DD | InvoiceDate: "5/7/2022" → "2022-05-07" |
 | time | Time | ISO 8601 - hh:mm:ss | TransactionTime: "9:45 PM" → "21:45:00" |
 | phoneNumber | Phone number | E.164 - +{CountryCode}{SubscriberNumber} | WorkPhone: "(800) 555-7676" → "+18005557676"|
-| countryRegion | Country/region | ISO 3166-1 alpha-3 | CountryRegion: "United States" → "USA" |
+| countryRegion | Country/Region | ISO 3166-1 alpha-3 | CountryRegion: "United States" → "USA" |
 | selectionMark | Is selected | "signed" or "unsigned" | AcceptEula: ☑ → "selected" |
 | signature | Is signed | Same as content | LendeeSignature: {signature} → "signed" |
 | number | Floating point number | Floating point number | Quantity: "1.20" → 1.2|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメント応答の細部更新"
}
```

### Explanation
このコードの差分は、`concept-analyze-document-response.md`というファイルにおける細部の更新を示しています。主に、文書の更新日やAPIの応答内容に関する表現の調整が行われました。具体的には、APIの応答に関する解説において、いくつかの文が改善され、より明確かつ一貫性のある表現に修正されています。

たとえば、文中の「analyze operation」が「Analyze operation」と表記されるよう変更され、APIの応答である「figures」や「sections」の定義が微調整されています。これにより、ドキュメントがより利用しやすく、読者が情報を正確に理解しやすい形になっています。また、更新日の変更も含まれており、情報が最新であることが示されています。

この修正は、開発者やユーザーがDocument Intelligence APIを利用する際の理解を助けるためのものであり、APIの使用に関する重要性を反映しています。

## articles/ai-services/document-intelligence/concept-custom-classifier.md{#item-7d0313}

<details>
<summary>Diff</summary>
````diff
@@ -1,16 +1,15 @@
 ---
-title: Custom classification model - Document Intelligence 
+title: Custom classification model - Document Intelligence
 titleSuffix: Azure AI services
 description: Use the custom classification model to train a model to identify and split the documents you process within your application.
 author: vkurpad
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 08/07/2024
+ms.date: 09/26/2024
 ms.author: lajanuar
 ms.custom:
   - references_regions
-  - ignite-2023
 monikerRange: '>=doc-intel-3.1.0'
 ---
 
@@ -50,7 +49,6 @@ Custom classification models are deep-learning-model types that combine layout a
 Custom classification models can analyze a single- or multi-file documents to identify if any of the trained document types are contained within an input file. Here are the currently supported scenarios:
 
 * A single file containing one document type, such as a loan application form.
-
 * A single file containing multiple document types. For instance, a loan application package that contains a loan application form, payslip, and bank statement.
 
 * A single file containing multiple instances of the same document. For instance, a collection of scanned invoices.
@@ -59,7 +57,8 @@ Custom classification models can analyze a single- or multi-file documents to id
 
 ✔️ The maximum allowed number of classes is `500`. The maximum allowed number of document samples per class is `100`.
 
-The model classifies each page of the input document, unless specified, to one of the classes in the labeled dataset. You can specify the page numbers to analyze in the input document as well. To set the threshold for your application, use the confidence score from the response. 
+The model classifies each page of the input document, unless specified, to one of the classes in the labeled dataset. You can specify the page numbers to analyze in the input document as well. To set the threshold for your application, use the confidence score from the response.
+
 ### Incremental training
 
 With custom models, you need to maintain access to the training dataset to update your classifier with new samples for an existing class, or add new classes. Classifier models now support incremental training where you can reference an existing classifier and append new samples for an existing class or add new classes with samples. Incremental training enables scenarios where data retention is a challenge and the classifier needs to be updated to align with changing business needs. Incremental training is supported with models trained with API version `2024-02-29-preview` and later.
@@ -250,7 +249,7 @@ Alternatively, if you have a flat list of files or only plan to use a few select
 ```
 
 As an example, the file list `car-maint.jsonl` contains the following files.
- 
+
 ```json
 {"file":"classifier/car-maint/Commercial Motor Vehicle - Adatum.pdf"}
 {"file":"classifier/car-maint/Commercial Motor Vehicle - Fincher.pdf"}
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム分類モデルのドキュメント更新"
}
```

### Explanation
このコードの差分は、`concept-custom-classifier.md`というファイルに関する小規模な更新を示しています。変更の主な目的は、ドキュメントの最新性を保つことと、内容の明確化です。具体的には、文書のタイトルや更新日、いくつかの文の改善が行われています。

変更点としては、タイトルの末尾のスペースが削除され、更新日が「08/07/2024」から「09/26/2024」に変更されています。また、文中の情報も若干の調整がなされており、特にモデルの動作やサポートされているシナリオを説明する際に、閲覧者が理解しやすいように書き改められています。

例えば、特定のページを分析する際の説明が、よりスムーズに流れるようになっており、また、複数の文書タイプを含むファイルの扱いについても、より明確に説明されています。このような修正は、利用者がカスタム分類モデルの機能を正確に理解し、効果的に活用できるようにするために重要です。

## articles/ai-services/document-intelligence/create-document-intelligence-resource.md{#item-b6c8c3}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-document-intelligence
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 04/24/2024
+ms.date: 09/26/2024
 ms.author: lajanuar
 ---
 
@@ -37,10 +37,10 @@ Let's get started:
 
 ## Create a resource
 
-1. Next, you're going to fill out the **Create Document Intelligence** fields with the following values:
+1. Next, you're going to fill out the **`Create Document Intelligence`** fields with the following values:
 
     * **Subscription**. Select your current subscription.
-    * **Resource group**. The [Azure resource group](/azure/cloud-adoption-framework/govern/resource-consistency/resource-access-management#what-is-an-azure-resource-group) that contains your resource. You can create a new group or add it to a pre-existing group.
+    * **Resource group**. The [Azure resource group](/azure/cloud-adoption-framework/govern/resource-consistency/resource-access-management#what-is-an-azure-resource-group) that contains your resource. You can create a new group or add it to an existing group.
     * **Region**. Select your local region.
     * **Name**. Enter a name for your resource. We recommend using a descriptive name, for example *YourNameFormRecognizer*.
     * **Pricing tier**. The cost of your resource depends on the pricing tier you choose and your usage. For more information, see [pricing details](https://azure.microsoft.com/pricing/details/cognitive-services/). You can use the free pricing tier (F0) to try the service, and upgrade later to a paid tier for production.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスリソース作成ガイドの更新"
}
```

### Explanation
このコードの差分は、`create-document-intelligence-resource.md`というファイルにおける小規模な更新を示しています。変更内容は、主に文書の更新日および文の表現の改善に関するものです。

具体的には、更新日が「04/24/2024」から「09/26/2024」に変更され、より最近の情報が反映されています。また、いくつかの文が微調整され、より明確な表現が使用されています。たとえば、「Create Document Intelligence」というフィールドの名称が強調され、バックティック（`` ` ``）で囲まれることで読みやすさが向上しています。また、「リソースグループ」の説明部分でも「既存のグループ」に対する表現が「pre-existing」から「existing」に変更されており、より自然な文になっています。

これらの小さな修正は、ドキュメント全体の可読性を向上させ、ユーザーがDocument Intelligenceリソースを作成する際に必要な情報をより簡単に理解できるようにすることを目的としています。ユーザーにとっての利便性が向上する重要な更新といえます。

## articles/ai-services/document-intelligence/service-limits.md{#item-5ceae5}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Service quotas and limits - Document Intelligence 
+title: Service quotas and limits - Document Intelligence
 titleSuffix: Azure AI services
 description: Quick reference, detailed description, and best practices for working within Azure AI Document Intelligence service Quotas and Limits
 #services: cognitive-services
@@ -9,7 +9,7 @@ ms.service: azure-ai-document-intelligence
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 06/26/2024
+ms.date: 09/26/2024
 ms.author: lajanuar
 monikerRange: '<=doc-intel-4.0.0'
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのサービス制限に関する文書の更新"
}
```

### Explanation
このコードの差分は、`service-limits.md`というファイルに対する小さな更新を示しています。主な変更点は、ドキュメントの更新日やフォーマットに関わるもので、全体的な可読性を向上させることを目的としています。

具体的には、タイトルの末尾にある不要なスペースが削除され、更新日が「06/26/2024」から「09/26/2024」に変更されています。この変更により、ドキュメントが最近の情報を反映していることが強調されています。さらに、全体のレイアウトが整えられており、特に文書のタイトルとその説明がより一貫性のある形式で表示されています。

これらの修正は、ドキュメントインテリジェンスのサービス制限に関する情報をユーザーが効果的に理解できるようにするために重要なものです。最近の変更により、利用者が必要な情報を迅速に見つけやすくなっている点が評価されるべきです。

## articles/ai-services/language-service/summarization/custom/how-to/data-formats.md{#item-f7ca2c}

<details>
<summary>Diff</summary>
````diff
@@ -1,178 +0,0 @@
----
-title: Prepare data for custom summarization
-titleSuffix: Azure AI services
-description: Learn about how to select and prepare data, to be successful in creating custom summarization projects.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.custom:
-  - build-2024
-ms.topic: how-to
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-# Format data for custom Summarization
-
-This page contains information about how to select and prepare data in order to be successful in creating custom summarization projects.
-
-> [!NOTE]
-> Throughout this document, we refer to a summary of a document as a “label”.
-
-## Custom summarization document sample format
-
-In the abstractive text summarization scenario, each document (whether it has a provided label or not) is expected to be provided in a plain .txt file. The file contains one or more lines. If multiple lines are provided, each is assumed to be a paragraph of the document. The following is an example document with three paragraphs.
-
-*At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality.*
-
-*In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there’s magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code will enable us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages.*
-
-*The goal is to have pre-trained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks.*
-
-## Custom summarization conversation sample format
-
- In the abstractive conversation summarization scenario, each conversation (whether it has a provided label or not) is expected to be provided in a .json file, which is similar to the input format for our [pre-built conversation summarization service](/rest/api/language/2023-04-01/analyze-conversation/submit-job?tabs=HTTP#textconversation).  The following is an example conversation of three turns between two speakers (Agent and Customer).
-
-```json
-{
-  "conversationItems": [
-    {
-      "text": "Hello, how can I help you?",
-      "modality": "text",
-      "id": "1",
-      "participantId": "Agent",
-      "role": "Agent"
-    },
-    {
-      "text": "How do I upgrade office? I have been getting error messages all day.",
-      "modality": "text",
-      "id": "2",
-      "participantId": "Customer",
-      "role": "Customer"
-    },
-    {
-      "text": "Please press the upgrade button, then sign in and follow the instructions.",
-      "modality": "text",
-      "id": "3",
-      "participantId": "Agent",
-      "role": "Agent"
-    }
-  ],
-  "modality": "text",
-  "id": "conversation1",
-  "language": "en"
-}
-```
-
-## Sample mapping JSON format
-
-In both text and conversation summarization scenarios, a set of documents and corresponding labels can be provided in a single JSON file that references individual document/conversation and summary files. 
-
-The JSON file is expected to contain the following fields:
-
-```json
-{
-    projectFileVersion": The version of the exported project,
-    "stringIndexType": Specifies the method used to interpret string offsets. For additional information see https://aka.ms/text-analytics-offsets,
-    "metadata": {
-        "projectKind": The project kind you need to import. Values for summarization are CustomAbstractiveSummarization and CustomConversationSummarization. Both projectKind fields must be identical.,
-        "storageInputContainerName": The name of the storage container that contains the documents/conversations and the summaries,
-        "projectName": a string project name,
-        "multilingual": A flag denoting whether this project should allow multilingual documents or not. For Summarization this option is turned off,
-        "description": a string project description,
-        "language": The default language of the project. Possible values are “en” and “en-us”
-    },
-    "assets": {
-        "projectKind": The project kind you need to import. Values for summarization are CustomAbstractiveSummarization and CustomConversationSummarization. Both projectKind fields must be identical.,
-        "documents": a list of document-label pairs, each is defined with three fields:[
-            {
-            "summaryLocation": a string path to the summary txt (for documents) or json (for conversations) file,
-            "location": a string path to the document txt (for documents) or json (for conversations) file,
-            "language": The language of the documents. Possible values are “en” and “en-us”
-            }
-            ]
-    }
-}
-```
-## Custom document summarization mapping sample
-
-The following is an example mapping file for the abstractive text summarization scenario with three documents and corresponding labels.
-
-```json
-{
-    "projectFileVersion": "2022-10-01-preview",
-    "stringIndexType": "Utf16CodeUnit",
-    "metadata": {
-        "projectKind": "CustomAbstractiveSummarization",
-        "storageInputContainerName": "abstractivesummarization",
-        "projectName": "sample_custom_summarization",
-        "multilingual": false,
-        "description": "Creating a custom summarization model",
-        "language": "en-us"
-    }
-    "assets": {
-        "projectKind": "CustomAbstractiveSummarization",
-        "documents": [
-            {
-                "summaryLocation": "doc1_summary.txt",
-                "location": "doc1.txt",
-                "language": "en-us"
-            },
-            {
-                "summaryLocation": "doc2_summary.txt",
-                "location": "doc2.txt",
-                "language": "en-us"
-            },
-            {
-                "summaryLocation": "doc3_summary.txt",
-                "location": "doc3.txt",
-                "language": "en-us"
-            }
-            ]
-    }
-}
-```
-
-## Custom conversation summarization mapping sample
-
-The following is an example mapping file for the abstractive conversation summarization scenario with three documents and corresponding labels.
-
-```json
-{
-    "projectFileVersion": "2022-10-01-preview",
-    "stringIndexType": "Utf16CodeUnit",
-    "metadata": {
-        "projectKind": "CustomAbstractiveSummarization",
-        "storageInputContainerName": "abstractivesummarization",
-        "projectName": "sample_custom_summarization",
-        "multilingual": false,
-        "description": "Creating a custom summarization model",
-        "language": "en-us"
-    }
-    "assets": {
-        "projectKind": "CustomAbstractiveSummarization",
-        "documents": [
-            {
-                "summaryLocation": "conv1_summary.txt",
-                "location": "conv1.json",
-                "language": "en-us"
-            },
-            {
-                "summaryLocation": "conv2_summary.txt",
-                "location": "conv2.json",
-                "language": "en-us"
-            },
-            {
-                "summaryLocation": "conv3_summary.txt",
-                "location": "conv3.json",
-                "language": "en-us"
-            }
-            ]
-    }
-}
-```
-
-## Next steps
-
-[Get started with custom summarization](../../custom/quickstart.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタム要約のデータ形式に関する文書の削除"
}
```

### Explanation
このコードの差分は、`data-formats.md`というファイルが完全に削除されたことを示しています。この文書は、カスタム要約プロジェクトのためのデータの選択と準備に関する重要な情報を提供していました。そのため、この削除はユーザーにとって重大な影響を及ぼす可能性があります。

削除された内容には、以下の情報が含まれていました：

1. **データ形式の詳細**: 要約用の文書や会話データを準備するための具体的なフォーマットやサンプルが提供されており、特にテキストファイルとJSON形式での例が多く含まれていました。
  
2. **プロジェクトのメタデータ**: 複数のドキュメントや会話データに対して、プロジェクトの説明や言語、バージョン情報を記載する方法が詳しく説明されていました。

3. **次のステップ**: ユーザーがカスタム要約の設定を開始するために必要な手順へのリンクも含まれていました。

この文書の削除により、カスタム要約プロジェクトにおけるデータ準備に関する情報が失われたため、利用者は他のリソースを探す必要があるかもしれません。これに伴うユーザー体験への影響が懸念されます。

## articles/ai-services/language-service/summarization/custom/how-to/deploy-model.md{#item-bd52c9}

<details>
<summary>Diff</summary>
````diff
@@ -1,57 +0,0 @@
----
-title: Deploy a custom summarization model
-titleSuffix: Azure AI services
-description: Learn about deploying a model for Custom summarization.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-# Deploy a custom summarization model
-
-Once you're satisfied with how your model performs, it's ready to be deployed and used to summarize text documents. Deploying a model makes it available for use through the [prediction API](https://aka.ms/ct-runtime-swagger).
-
-<!--## Prerequisites
-
-* A successfully [created project](create-project.md) with a configured Azure storage account.
-* Text data that has [been uploaded](design-schema.md#data-preparation) to your storage account.
-* [Labeled data](label-data.md) and a successfully [trained model](train-model.md).
-* Reviewed the [model evaluation details](view-model-evaluation.md) to determine how your model is performing.
-
-For more information, see [project development lifecycle](../overview.md#project-development-lifecycle).-->
-
-## Deploy model
-
-After you've reviewed your model's performance and decided it can be used in your environment, you need to assign it to a deployment. Assigning the model to a deployment makes it available for use through the [prediction API](https://aka.ms/ct-runtime-swagger). It is recommended to create a deployment named *production* to which you assign the best model you have built so far and use it in your system. You can create another deployment called *staging* to which you can assign the model you're currently working on to be able to test it. You can have a maximum of 10 deployments in your project. 
-
-[!INCLUDE [Deploy a model using Language Studio](../../../includes/custom/language-studio/deployment.md)]
-   
-## Swap deployments
-
-After you are done testing a model assigned to one deployment and you want to assign this model to another deployment you can swap these two deployments. Swapping deployments involves taking the model assigned to the first deployment, and assigning it to the second deployment. Then taking the model assigned to second deployment, and assigning it to the first deployment. You can use this process to swap your *production* and *staging* deployments when you want to take the model assigned to *staging* and assign it to *production*. 
-
-[!INCLUDE [Swap deployments](../../../includes/custom/language-studio/swap-deployment.md)]
-
-## Delete deployment
-
-[!INCLUDE [Delete deployment](../../../includes/custom/language-studio/delete-deployment.md)]
-
-## Assign deployment resources
-
-You can [deploy your project to multiple regions](../../../concepts/custom-features/multi-region-deployment.md) by assigning different Language resources that exist in different regions.
-
-[!INCLUDE [Assign resource](../../../includes/custom/language-studio/assign-resources.md)]
-
-## Unassign deployment resources
-
-When unassigning or removing a deployment resource from a project, you will also delete all the deployments that have been deployed to that resource's region.
-
-[!INCLUDE [Unassign resource](../../../includes/custom/language-studio/unassign-resources.md)]
-
-## Next steps
-
-Check out the [summarization feature overview](../../overview.md).
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタム要約モデルのデプロイに関する文書の削除"
}
```

### Explanation
このコードの差分は、`deploy-model.md`というファイルが完全に削除されたことを示しています。この文書は、カスタム要約モデルをAzure環境にデプロイするための手順やガイドラインを提供しており、ユーザーがモデルを適切に運用するために重要な情報を含んでいました。

削除された内容は以下の構成を持っていました：

1. **モデルデプロイの概要**: モデルの性能を確認し、どのようにデプロイして使用するかの基本的な説明がありました。

2. **デプロイメントの管理**: モデルを異なるデプロイメントに割り当てる方法や、ステージングとプロダクションのデプロイメントを行う際のガイドラインが記載されていました。

3. **デプロイメントの入れ替えと削除**: モデルのデプロイメントを交換する方法や、不要になったデプロイを削除する手順が含まれていました。

4. **リソースの割り当てと解除**: プロジェクトを複数のリージョンにデプロイする方法や、リソースをプロジェクトから解除する際の注意点についても触れられていました。

この文書の削除により、ユーザーはカスタム要約モデルのデプロイに関する重要な情報を失うことになり、代わりのリソースを探さなければならない可能性があります。これにより、利用者の作業が影響を受けることが懸念されます。

## articles/ai-services/language-service/summarization/custom/how-to/test-evaluate.md{#item-b4df1a}

<details>
<summary>Diff</summary>
````diff
@@ -1,44 +0,0 @@
----
-title: Test and evaluate models in custom summarization
-titleSuffix: Azure AI services
-description: Learn about how to test and evaluate custom summarization models.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-# Test and evaluate your custom summarization models
-
-As you create your custom summarization model, you want to be sure to ensure that you end up with a quality model. You need to test and evaluate your custom summarization model to ensure it performs well.
-
-## Guidance on split test and training sets
-
-An important stage of creating a customized summarization model is validating that the created model is satisfactory in terms of quality and generates summaries as expected. That validation process has to be performed with a separate set of examples (called test examples) than the examples used for training. There are three important guidelines we recommend following when splitting the available data into training and testing:
-
-- **Size**: To establish enough confidence about the model's quality, the test set should be of a reasonable size. Testing the model on just a handful of examples can give misleading outcome evaluation times. We recommend evaluating on hundreds of examples. When a large number of documents/conversations is available, we recommend reserving at least 10% of them for testing.
-- **No Overlap**: It's crucial to make sure that the same document isn't used for training and testing at the same time. Testing should be performed on documents that were never used for training at any stage, otherwise the quality of the model will be highly overestimated.
-- **Diversity**: The test set should cover as many possible input characteristics as possible. For example, it's always better to include documents of different lengths, topics, styles, .. etc. when applicable. Similarly for conversation summarization, it's always a good idea to include conversations of different number of turns and number of speakers.
-
-## Guidance to evaluate a custom summarization model
-
-When evaluating a custom model, we recommend using both automatic and manual evaluation together. Automatic evaluation helps quickly judge the quality of summaries produced for the entire test set, hence covering a wide range of input variations. However, automatic evaluation gives an approximation of the quality and isn't enough by itself to establish confidence in the model quality. So, we also recommend inspecting the summaries produced for as many test documents as possible.
-
-### Automatic evaluation
-
-Currently, we use a metric called ROUGE (Recall-Oriented Understudy for Gisting Evaluation). This technique includes measures for automatically determining the quality of a summary by comparing it to ideal summaries created by humans. The measures count the number of overlapping units, like n-gram, word sequences, and word pairs between the computer-generated summary being evaluated and the ideal summaries. To learn more about Rouge, see the [ROUGE Wikipedia entry](https://en.wikipedia.org/wiki/ROUGE_(metric)) and the [paper on the ROUGE package](https://aclanthology.org/W04-1013.pdf).
-
-### Manual evaluation
-
-When you manually inspect the quality of a summary, there are general qualities of a summary that we recommend checking for besides any desired expectations that the custom model was trained to adhere to such as style, format, or length. The general qualities we recommend checking are:
-
-- **Fluency**: The summary should have no formatting problems, capitalization errors or ungrammatical sentences.
-- **Coherence**: The summary should be well-structured and well-organized. The summary shouldn't just be a heap of related information, but should build from sentence to sentence into a coherent body of information about a topic.
-- **Coverage**: The summary should cover all important information in the document/conversation.
-- **Relevance**: The summary should include only important information from the source document/conversation without redundancies.
-- **Hallucinations**: The summary doesn't contain wrong information not supported by the source document/conversation.
-
-To learn more about summarization evaluation, see the [MIT Press article on SummEval](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00373/100686/SummEval-Re-evaluating-Summarization-Evaluation).
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタム要約モデルのテストと評価に関する文書の削除"
}
```

### Explanation
このコードの差分は、`test-evaluate.md`というファイルが完全に削除されたことを示しています。この文書は、カスタム要約モデルをテストおよび評価するための手順やガイドラインを提供しており、モデルが品質基準を満たしているか確認するために重要な役割を果たしていました。

削除された内容には以下の要素が含まれていました：

1. **テストと評価の重要性**: モデルが期待通りの性能を発揮することを確認するために、テストと評価の必要性が強調されていました。

2. **データの分割に関するガイダンス**: トレーニングセットとテストセットの分割に関する具体的な指針が提供されており、サイズ、重複の排除、多様性に関するアドバイスが含まれていました。

3. **評価方法**: 自動評価と手動評価の両方を用いることが推奨され、それぞれの特徴や手法（例：ROUGEメトリック）について詳述されていました。

4. **一般的な評価基準**: フルエンシー、コヒーレンス、カバレッジ、関連性、情報の正確性（ハルシネーションの排除）など、評価する際にチェックすべきポイントが明示されていました。

この文書の削除により、カスタム要約モデルのテストや評価を行うユーザーが必要な情報を失うことになり、代わりに他のリソースを探さなければならない可能性があります。したがって、モデルの品質保証プロセスに影響を及ぼすことが懸念されます。

## articles/ai-services/language-service/summarization/custom/quickstart.md{#item-bf389e}

<details>
<summary>Diff</summary>
````diff
@@ -1,35 +0,0 @@
----
-title: Quickstart - Custom summarization (preview)
-titleSuffix: Azure AI services
-description: Quickly start building an AI model to summarize text.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: quickstart
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-<!--- zone_pivot_groups: usage-custom-language-features --->
-# Quickstart: custom summarization (preview)
-
-Use this article to get started with creating a custom Summarization project where you can train custom models on top of Summarization. A model is artificial intelligence software that's trained to do a certain task. For this system, the models summarize text and are trained by learning from imported data.
-
-In this article, we use Language Studio to demonstrate key concepts of custom summarization. As an example we’ll build a custom summarization model to extract the Facility or treatment location from short discharge notes.
-
-<!--- >::: zone pivot="language-studio" --->
-
-[!INCLUDE [Language Studio quickstart](../includes/quickstarts/custom-language-studio.md)]
-
-<!---::: zone-end
-
-::: zone pivot="rest-api"
-
-[!INCLUDE [REST API quickstart](../includes/quickstarts/custom-rest-api.md)] 
-
-::: zone-end --->
-
-## Next steps
-
-* [Summarization overview](../overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタム要約のクイックスタートに関する文書の削除"
}
```

### Explanation
このコードの差分は、`quickstart.md`というファイルが完全に削除されたことを示しています。この文書は、カスタム要約プロジェクトの作成を迅速に始めるためのガイドを提供しており、AIモデルを構築するための基本的な情報が含まれていました。

削除された内容には以下のポイントが含まれていました：

1. **クイックスタートの概要**: カスタム要約プロジェクトの作成手順が簡潔に説明されており、AIモデルがどのようにテキストを要約するかについての基本的な概念が記載されていました。

2. **Language Studioの使用**: Language Studioを利用してカスタム要約を実現するための手法が示されており、具体的なケーススタディとして、退院ノートから施設や治療場所を抽出するためのモデル構築が例として挙げられていました。

3. **次のステップ**: ユーザーが次に進むべきリソースとして、要約の概要へのリンクが提供されていました。

この文書の削除により、カスタム要約の初学者にとって重要なリソースが失われ、特に初心者がシステムを使い始める際の導入がさらに難しくなる可能性があります。その結果、ユーザーは代替リソースを探す必要が生じるかもしれません。

## articles/ai-services/language-service/summarization/includes/development-options.md{#item-f33a53}

<details>
<summary>Diff</summary>
````diff
@@ -26,8 +26,6 @@ To use summarization, you submit for analysis and handle the API output in your
 |---------|---------|---------|
 | REST API     | Integrate conversation summarization into your applications using the REST API. | [Quickstart: Use conversation summarization](../quickstart.md?tabs=conversation-summarization&pivots=rest-api) |
 
-Custom Summarization enables users to build custom AI models to summarize unstructured text, such as contracts or novels. By creating a Custom Summarization project, developers can iteratively label data, train, evaluate, and improve model performance before making it available for consumption. The quality of the labeled data greatly impacts model performance. To simplify building and customizing your model, the service offers a custom web portal that can be accessed through the [Language studio](https://aka.ms/languageStudio). You can easily get started with the service by following the steps in this [quickstart](../custom/quickstart.md).
-
 # [Document summarization](#tab/document-summarization)
 
 |Development option  |Description  |
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
このコードの差分は、`development-options.md`というファイルが2つの行で修正されたことを示しています。修正内容は、カスタム要約モデルの使用に関する情報を簡潔に伝える部分に関連しています。

主な変更点は以下の通りです：

1. **カスタム要約の説明の簡素化**: カスタム要約に関する説明が短縮され、ユーザーはカスタムAIモデルを構築する際のプロセスについての具体的なステップ（データのラベリング、トレーニング、評価、モデルのパフォーマンス向上）が簡潔に説明されています。この変更により、基本的なコンセプトは保持しつつ、冗長な情報が削除されました。

2. **言語スタジオおよびクイックスタートへのリンク**: さらに、カスタムモデルの構築を簡素化するために、[Language Studio](https://aka.ms/languageStudio)に関連する情報や、クイックスタートに関するリンクが強調され、ユーザーがすぐにサービスを使い始める手助けがなされる内容は変更がありません。

これらの修正は、文書全体の明瞭性を高め、開発者がカスタム要約への理解を深める手助けをすることを目的としています。

## articles/ai-services/language-service/summarization/language-support.md{#item-676e71}

<details>
<summary>Diff</summary>
````diff
@@ -81,14 +81,6 @@ Conversation summarization supports the following languages:
 |Hungarian|	`hu`||	
 |Thai|	`th`||	
 
-## Custom summarization
-
-Custom summarization supports the following languages:
-
-| Language              | Language code |      Notes          |
-|-----------------------|---------------|---------------------|
-| English               | `en`          |                     |
-
 ## Next steps
 
 * [Summarization overview](overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム要約に関する言語サポート情報の修正"
}
```

### Explanation
このコードの差分は、`language-support.md`というファイルの内容が一部修正されたことを示しています。具体的には、カスタム要約に関連する言語サポート情報が削除されています。

主要な変更点は以下の通りです：

1. **カスタム要約の言語サポートの削除**: 以前はカスタム要約がサポートしている複数の言語とその言語コードがリストアップされていましたが、このセクションが完全に削除されました。これにより、読者はカスタム要約がどの言語に対応しているかの具体的な情報を得ることができなくなりました。

2. **他のセクションは維持**: 会話の要約がサポートする言語情報や「次のステップ」セクションはそのまま残されており、全体の文書構成に大きな変更はありません。

この変更は、カスタム要約の言語サポートに関する明確な情報欠如を生じさせますが、文書の簡素化を意図している可能性があります。ユーザーは、要約機能の利用時に他のリソースを参照する必要があるかもしれません。

## articles/ai-services/language-service/summarization/region-support.md{#item-d74574}

<details>
<summary>Diff</summary>
````diff
@@ -18,32 +18,32 @@ Some summarization features are only available in limited regions. More regions
 
 ## Regional availability table
 
-|Region            |Text abstractive summarization    |Conversation summarization                     |Custom summarization|
-|------------------|----------------------------------|-----------------------------------------------|--------------------|
-|US Gov Virginia   |&#9989;                           |&#9989;                                        |&#10060;            |
-|US Gov Arizona    |&#9989;                           |&#9989;                                        |&#10060;            |
-|North Europe      |&#9989;                           |&#9989;                                        |&#10060;            |
-|East US           |&#9989;                           |&#9989;                                        |&#9989;             |
-|East US 2         |&#9989;                           |&#9989;                                        |&#10060;            |
-|Central US        |&#9989;                           |&#9989;                                        |&#10060;            |
-|South Central US  |&#9989;                           |&#9989;                                        |&#10060;            |
-|West US           |&#9989;                           |&#9989;                                        |&#10060;            |
-|West US 2         |&#9989;                           |&#9989;                                        |&#10060;            |
-|USNat East        |&#9989;                           |&#9989;                                        |&#10060;            |
-|USNat West        |&#9989;                           |&#9989;                                        |&#10060;            |
-|USSec East        |&#9989;                           |&#9989;                                        |&#10060;            |
-|USSec West        |&#9989;                           |&#9989;                                        |&#10060;            |
-|South UK          |&#9989;                           |&#9989;                                        |&#10060;            |
-|Southeast Asia    |&#9989;                           |&#9989;                                        |&#10060;            |
-|Australia East    |&#9989;                           |&#9989;                                        |&#10060;            |
-|France Central    |&#9989;                           |&#9989;                                        |&#10060;            |
-|Japan East        |&#9989;                           |&#9989;                                        |&#10060;            |
-|North Central US  |&#9989;                           |&#9989;                                        |&#10060;            |
-|Central Sweden    |&#9989;                           |&#9989;                                        |&#10060;            |
-|Switzerland North |&#9989;                           |&#9989;                                        |&#10060;            |
-|West Europe       |&#9989;                           |&#9989;                                        |&#10060;            |
-|Italy North       |&#9989;                           |&#9989;                                        |&#10060;            |
-|China North 3     |&#9989;                           |&#9989;                                        |&#10060;            |
+|Region            |Text abstractive summarization    |Conversation summarization                     |
+|------------------|----------------------------------|-----------------------------------------------|
+|US Gov Virginia   |&#9989;                           |&#9989;                                        |
+|US Gov Arizona    |&#9989;                           |&#9989;                                        |
+|North Europe      |&#9989;                           |&#9989;                                        |
+|East US           |&#9989;                           |&#9989;                                        |
+|East US 2         |&#9989;                           |&#9989;                                        |
+|Central US        |&#9989;                           |&#9989;                                        |
+|South Central US  |&#9989;                           |&#9989;                                        |
+|West US           |&#9989;                           |&#9989;                                        |
+|West US 2         |&#9989;                           |&#9989;                                        |
+|USNat East        |&#9989;                           |&#9989;                                        |
+|USNat West        |&#9989;                           |&#9989;                                        |
+|USSec East        |&#9989;                           |&#9989;                                        |
+|USSec West        |&#9989;                           |&#9989;                                        |
+|South UK          |&#9989;                           |&#9989;                                        |
+|Southeast Asia    |&#9989;                           |&#9989;                                        |
+|Australia East    |&#9989;                           |&#9989;                                        |
+|France Central    |&#9989;                           |&#9989;                                        |
+|Japan East        |&#9989;                           |&#9989;                                        |
+|North Central US  |&#9989;                           |&#9989;                                        |
+|Central Sweden    |&#9989;                           |&#9989;                                        |
+|Switzerland North |&#9989;                           |&#9989;                                        |
+|West Europe       |&#9989;                           |&#9989;                                        |
+|Italy North       |&#9989;                           |&#9989;                                        |
+|China North 3     |&#9989;                           |&#9989;                                        |
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リージョンサポートに関する情報の更新"
}
```

### Explanation
このコードの差分は、`region-support.md`というファイルの内容が更新されたことを示しています。変更は主にフォーマットであり、情報が整理された新しいテーブル形式に更新されています。

主な変更点は以下の通りです：

1. **リージョナル可用性テーブルの形式変更**: リージョンサポートに関するテーブルのフォーマットが整えられ、これまでの情報が新しい形式で表示されています。この変更によってテーブルの可読性が向上しました。

2. **カスタム要約関連の情報の削除**: 以前は「カスタム要約」の列が存在していましたが、今回の更新ではその列が削除されました。このため、カスタム要約機能に関しては一切の情報が表示されなくなっています。

3. **データの整頓**: テーブル内の情報（リージョン、テキスト要約及び会話要約のサポート）も新たに整理され、各リージョンにおけるサポート状況が明示されていますが、カスタム要約に関する詳細は提供されていません。

この変更は、情報の整理と明確化を目指しており、ユーザーがリージョンサポートを理解しやすくすることを目的としていますが、カスタム要約に関する情報の欠如が新たな課題として可能性があります。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -628,7 +628,6 @@ items:
                 href: sentiment-opinion-mining/custom/how-to/deploy-model.md
               - name: Call the API
                 href: sentiment-opinion-mining/custom/how-to/call-api.md
-
   - name: Text Analytics for health
     items:
     - name: Text Analytics for health overview
@@ -715,57 +714,44 @@ items:
     - name: Summarization overview
       href: summarization/overview.md
       displayName: native, native document
+    - name: Summarization quickstart
+      href: summarization/quickstart.md
     - name: Summarization region support
       href: summarization/region-support.md
     - name: Summarization language support
       href: summarization/language-support.md
-    - name: Prebuilt
+    - name: How-to guides
       items:
-      - name: Summarization quickstart
-        href: summarization/quickstart.md
-      - name: How-to guides
-        items:
-        - name: Call the document summarization API
-          href: summarization/how-to/document-summarization.md
-        - name: Call the conversation summarization API
-          href: summarization/how-to/conversation-summarization.md
-        - name: Use containers
-          items:
-          - name: Use Docker Containers
-            href: summarization/how-to/use-containers.md
-          - name: Configure containers
-            href: concepts/configure-containers.md
-          - name: Use container instances
-            href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
-          - name: Use containers in disconnected environments
-            href: ../containers/disconnected-containers.md
-          - name: Azure AI containers overview
-            href: ../cognitive-services-container-support.md
-      - name: Responsible use of AI
+      - name: Call the document summarization API
+        href: summarization/how-to/document-summarization.md
+      - name: Call the conversation summarization API
+        href: summarization/how-to/conversation-summarization.md
+      - name: Use containers
         items:
-        - name: Transparency note for summarization
-          href: /legal/cognitive-services/language-service/transparency-note-extractive-summarization?context=/azure/ai-services/language-service/context/context
-          displayName: Transparency note for summarization, summarization transparency, Responsible AI, Responsible use of AI
-        - name: Integration and responsible use
-          href: /legal/cognitive-services/language-service/guidance-integration-responsible-use-summarization?context=/azure/ai-services/language-service/context/context
-          displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-        - name: Characteristics and limitations
-          href: /legal/cognitive-services/language-service/characteristics-and-limitations-summarization?context=/azure/ai-services/language-service/context/context
-        - name: Data, privacy, and security
-          href: /legal/cognitive-services/language-service/data-privacy?context=/azure/ai-services/language-service/context/context
-          displayName: Data privacy, logging, data retention
-    - name: Custom (preview)
+        - name: Use Docker Containers
+          href: summarization/how-to/use-containers.md
+        - name: Configure containers
+          href: concepts/configure-containers.md
+        - name: Use container instances
+          href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
+        - name: Use containers in disconnected environments
+          href: ../containers/disconnected-containers.md
+        - name: Azure AI containers overview
+          href: ../cognitive-services-container-support.md
+    - name: Responsible use of AI
       items:
-      - name: Custom summarization quickstart
-        href: summarization/custom/quickstart.md
-      - name: How-to guides
-        items:
-        - name: Utilize custom summarization data formats
-          href: summarization/custom/how-to/data-formats.md
-        - name: Deploy a model
-          href: summarization/custom/how-to/deploy-model.md
-        - name: Test and evaluate your models
-          href: summarization/custom/how-to/test-evaluate.md
+      - name: Transparency note for summarization
+        href: /legal/cognitive-services/language-service/transparency-note-extractive-summarization?context=/azure/ai-services/language-service/context/context
+        displayName: Transparency note for summarization, summarization transparency, Responsible AI, Responsible use of AI
+      - name: Integration and responsible use
+        href: /legal/cognitive-services/language-service/guidance-integration-responsible-use-summarization?context=/azure/ai-services/language-service/context/context
+        displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
+      - name: Characteristics and limitations
+        href: /legal/cognitive-services/language-service/characteristics-and-limitations-summarization?context=/azure/ai-services/language-service/context/context
+      - name: Data, privacy, and security
+        href: /legal/cognitive-services/language-service/data-privacy?context=/azure/ai-services/language-service/context/context
+        displayName: Data privacy, logging, data retention
+          
 - name: Concepts
   items:
   - name: Language Studio
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次構成の更新"
}
```

### Explanation
このコードの差分は、`toc.yml`というファイルの内容が更新されたことを示しています。変更の主な目的は目次の整理と機能の明確化であり、情報の追加と削除が行われています。

主な変更点は以下の通りです：

1. **目次の再構成**: 目次の構成が変更され、いくつかの項目は新しいカテゴリーに移動されました。特に「Summarization」に関連する項目が整理され、より明確な階層構造が確立されています。

2. **新しいエントリの追加**: 「Summarization quickstart」や「How-to guides」などの新たな項目が追加され、ユーザーが情報にアクセスしやすくなっています。これは、ユーザーが必要なリソースにスムーズに移動できることを意図しています。

3. **古いエントリの削除**: 一部の古い項目や重複するエントリが削除され、全体的なスリム化が図られています。これにより、目次がよりクリーンで直感的な構造になっています。

4. **情報の明確化**: 新たに追加された項目や修正されたリンクによって、各機能の目的や使用方法がより明確に示されています。

この変更は、ユーザーがAIサービスに関連する情報を迅速に見つけられるようにするためのものであり、全体的により良いナビゲーション体験を提供することを目的としています。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -15,6 +15,10 @@ ms.author: jboback
 
 Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent developments, this article provides you with information about new releases and features.
 
+## September 2024
+
+* Custom Summarization has been discontinued and is no longer available in the Studio and documentation.
+
 ## July 2024
 
 * [Conversational PII redaction](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/announcing-conversational-pii-detection-service-s-general/ba-p/4162881) service in English-language contexts is now Generally Available (GA).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新情報の更新"
}
```

### Explanation
このコードの差分は、`whats-new.md`というファイルに新しい情報が追加されたことを示しています。更新された内容は、Azure AI Languageに関連する最新情報を提供するもので、新しいリリースや機能に関する詳細が含まれています。

主な変更点は次の通りです：

1. **新しいセクションの追加**: 「September 2024」という新しいセクションが追加され、最近の開発状況が明示されています。このセクションでは、特にカスタム要約機能の廃止に関する重要な情報が提供されています。

2. **機能の廃止についての告知**: 新しいセクションでは、「カスタム要約」機能が廃止されたことが明記されており、今後はスタジオやドキュメントで使用できなくなることが伝えられています。これはユーザーにとって重要な変更点であり、サービスの利用に影響を与える可能性があります。

3. **以前の情報はそのまま維持**: 既存の「July 2024」のセクションはそのまま残っており、新たな機能のリリースについての情報も引き続き提供されています。

この更新は、Azure AI Languageを利用するユーザーに対して、最新の情報をタイムリーに提供することを目的としており、特に機能変更に関する明確な通知が重要です。

## articles/ai-studio/.openpublishing.redirection.ai-studio.json{#item-c75c21}

<details>
<summary>Diff</summary>
````diff
@@ -25,6 +25,11 @@
             "redirect_url": "/azure/ai-studio/quickstarts/assistants",
             "redirect_document_id": true
         },
+        {
+            "source_path_from_root": "/articles/ai-studio/how-to/deploy-models-phi-3-5-moe.md",
+            "redirect_url": "/azure/ai-studio/how-to/deploy-models-phi-3",
+            "redirect_document_id": true
+        },
         {
             "source_path_from_root": "/articles/ai-studio/how-to/cli-install.md",
             "redirect_url": "/azure/ai-studio/how-to/develop/sdk-overview",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リダイレクト設定の更新"
}
```

### Explanation
このコードの差分は、`ai-studio/.openpublishing.redirection.ai-studio.json`ファイルのリダイレクト設定が更新されたことを示しています。具体的には、新しいリダイレクトルールが追加され、特定のドキュメントへの遷移が明示的に定義されています。

主な変更点は次の通りです：

1. **新しいリダイレクトルールの追加**: 新しい項目が追加され、`/articles/ai-studio/how-to/deploy-models-phi-3-5-moe.md`から`/azure/ai-studio/how-to/deploy-models-phi-3`へのリダイレクトが設定されています。この変更により、ユーザーが古いドキュメントにアクセスしようとした場合でも、新しい関連情報にスムーズに遷移できるようになります。

2. **リダイレクト先の明示化**: 新たに追加されたリダイレクトルールにより、特定のURLから新しいURLへの遷移が明確になり、ユーザーが最新の情報や手順にアクセスしやすくなります。

3. **全体的なリダイレクト設定の整合性**: 既存のリダイレクト設定はそのまま維持されており、本変更は全体の整合性を保ちながら行われています。これにより、リダイレクトルールが一貫して機能し続けることが期待されます。

この更新は、ユーザーのナビゲーション体験を向上させ、必要な情報へのアクセスを簡素化することを目的としています。新しいリダイレクトにより、古いドキュメントへのリンクが無効になることなく、新しい情報を効率的に提示しています。

## articles/ai-studio/how-to/deploy-models-phi-3-5-moe.md{#item-9af6ea}

<details>
<summary>Diff</summary>
````diff
@@ -1,1153 +0,0 @@
----
-title: How to use Phi-3.5 MoE chat model with Azure AI Studio
-titleSuffix: Azure AI Studio
-description: Learn how to use Phi-3.5 MoE chat model with Azure AI Studio.
-ms.service: azure-ai-studio
-manager: scottpolly
-ms.topic: how-to
-ms.date: 09/13/2024
-ms.reviewer: kritifaujdar
-reviewer: fkriti
-ms.author: mopeakande
-author: msakande
-ms.custom: references_regions, generated
-zone_pivot_groups: azure-ai-model-catalog-samples-chat
----
-
-# How to use Phi-3.5 MoE chat model
-
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
-
-In this article, you learn about Phi-3.5 MoE chat model and how to use it.
-The Phi-3 family of small language models (SLMs) is a collection of instruction-tuned generative text models.
-
-
-
-::: zone pivot="programming-language-python"
-
-## Phi-3.5 MoE chat model
-
-Phi-3.5 models are lightweight, state-of-the-art open models. These models were trained with Phi-3 datasets that include both synthetic data and the filtered, publicly available websites data, with a focus on high quality and reasoning-dense properties. Phi-3.5 MoE uses 16x3.8B parameters with 6.6B active parameters when using 2 experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
-
-The models underwent a rigorous enhancement process, incorporating both supervised fine-tuning, proximal policy optimization, and direct preference optimization to ensure precise instruction adherence and robust safety measures.
-
-The Phi-3.5 models come in the following variants, with the variants having a context length (in tokens) of 128K.
-
-
-You can learn more about the models in their respective model card:
-
-* [Phi-3.5-MoE-Instruct](https://aka.ms/azureai/landing/Phi-3.5-MoE-Instruct)
-
-
-## Prerequisites
-
-To use Phi-3.5 MoE chat model with Azure AI Studio, you need the following prerequisites:
-
-### A model deployment
-
-**Deployment to a self-hosted managed compute**
-
-Phi-3.5 MoE chat model can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
-
-For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
-
-> [!div class="nextstepaction"]
-> [Deploy the model to managed compute](../concepts/deployments-overview.md)
-
-### The inference package installed
-
-You can consume predictions from this model by using the `azure-ai-inference` package with Python. To install this package, you need the following prerequisites:
-
-* Python 3.8 or later installed, including pip.
-* The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
-* Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
-  
-Once you have these prerequisites, install the Azure AI inference package with the following command:
-
-```bash
-pip install azure-ai-inference
-```
-
-Read more about the [Azure AI inference package and reference](https://aka.ms/azsdk/azure-ai-inference/python/reference).
-
-## Work with chat completions
-
-In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
-
-> [!TIP]
-> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Studio with the same code and structure, including Phi-3.5 MoE chat model.
-
-### Create a client to consume the model
-
-First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
-
-
-```python
-import os
-from azure.ai.inference import ChatCompletionsClient
-from azure.core.credentials import AzureKeyCredential
-
-client = ChatCompletionsClient(
-    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
-    credential=AzureKeyCredential(os.environ["AZURE_INFERENCE_CREDENTIAL"]),
-)
-```
-
-When you deploy the model to a self-hosted online endpoint with **Microsoft Entra ID** support, you can use the following code snippet to create a client.
-
-
-```python
-import os
-from azure.ai.inference import ChatCompletionsClient
-from azure.identity import DefaultAzureCredential
-
-client = ChatCompletionsClient(
-    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
-    credential=DefaultAzureCredential(),
-)
-```
-
-### Get the model's capabilities
-
-The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
-
-
-```python
-model_info = client.get_model_info()
-```
-
-The response is as follows:
-
-
-```python
-print("Model name:", model_info.model_name)
-print("Model type:", model_info.model_type)
-print("Model provider name:", model_info.model_provider_name)
-```
-
-```console
-Model name: Phi-3.5-MoE-Instruct
-Model type: chat-completions
-Model provider name: Microsoft
-```
-
-### Create a chat completion request
-
-The following example shows how you can create a basic chat completions request to the model.
-
-```python
-from azure.ai.inference.models import SystemMessage, UserMessage
-
-response = client.complete(
-    messages=[
-        SystemMessage(content="You are a helpful assistant."),
-        UserMessage(content="How many languages are in the world?"),
-    ],
-)
-```
-
-> [!NOTE]
-> Phi-3.5-MoE-Instruct doesn't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
-
-The response is as follows, where you can see the model's usage statistics:
-
-
-```python
-print("Response:", response.choices[0].message.content)
-print("Model:", response.model)
-print("Usage:")
-print("\tPrompt tokens:", response.usage.prompt_tokens)
-print("\tTotal tokens:", response.usage.total_tokens)
-print("\tCompletion tokens:", response.usage.completion_tokens)
-```
-
-```console
-Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
-Model: Phi-3.5-MoE-Instruct
-Usage: 
-  Prompt tokens: 19
-  Total tokens: 91
-  Completion tokens: 72
-```
-
-Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
-
-#### Stream content
-
-By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
-
-You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
-
-
-```python
-result = client.complete(
-    messages=[
-        SystemMessage(content="You are a helpful assistant."),
-        UserMessage(content="How many languages are in the world?"),
-    ],
-    temperature=0,
-    top_p=1,
-    max_tokens=2048,
-    stream=True,
-)
-```
-
-To stream completions, set `stream=True` when you call the model.
-
-To visualize the output, define a helper function to print the stream.
-
-```python
-def print_stream(result):
-    """
-    Prints the chat completion with streaming.
-    """
-    import time
-    for update in result:
-        if update.choices:
-            print(update.choices[0].delta.content, end="")
-```
-
-You can visualize how streaming generates content:
-
-
-```python
-print_stream(result)
-```
-
-#### Explore more parameters supported by the inference client
-
-Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
-
-```python
-from azure.ai.inference.models import ChatCompletionsResponseFormatText
-
-response = client.complete(
-    messages=[
-        SystemMessage(content="You are a helpful assistant."),
-        UserMessage(content="How many languages are in the world?"),
-    ],
-    presence_penalty=0.1,
-    frequency_penalty=0.8,
-    max_tokens=2048,
-    stop=["<|endoftext|>"],
-    temperature=0,
-    top_p=1,
-    response_format={ "type": ChatCompletionsResponseFormatText() },
-)
-```
-
-> [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
-
-If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
-
-### Pass extra parameters to the model
-
-The Azure AI Model Inference API allows you to pass extra parameters to the model. The following code example shows how to pass the extra parameter `logprobs` to the model. 
-
-Before you pass extra parameters to the Azure AI model inference API, make sure your model supports those extra parameters. When the request is made to the underlying model, the header `extra-parameters` is passed to the model with the value `pass-through`. This value tells the endpoint to pass the extra parameters to the model. Use of extra parameters with the model doesn't guarantee that the model can actually handle them. Read the model's documentation to understand which extra parameters are supported.
-
-
-```python
-response = client.complete(
-    messages=[
-        SystemMessage(content="You are a helpful assistant."),
-        UserMessage(content="How many languages are in the world?"),
-    ],
-    model_extras={
-        "logprobs": True
-    }
-)
-```
-
-The following extra parameters can be passed to Phi-3.5 MoE chat model:
-
-| Name           | Description           | Type            |
-| -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
-| `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
-| `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
-
-
-::: zone-end
-
-
-::: zone pivot="programming-language-javascript"
-
-## Phi-3.5 MoE chat model
-
-Phi-3.5 models are lightweight, state-of-the-art open models. These models were trained with Phi-3 datasets that include both synthetic data and the filtered, publicly available websites data, with a focus on high quality and reasoning-dense properties. Phi-3.5 MoE uses 16x3.8B parameters with 6.6B active parameters when using 2 experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
-
-The models underwent a rigorous enhancement process, incorporating both supervised fine-tuning, proximal policy optimization, and direct preference optimization to ensure precise instruction adherence and robust safety measures.
-
-The Phi-3.5 models come in the following variants, with the variants having a context length (in tokens) of 128K.
-
-
-You can learn more about the models in their respective model card:
-
-* [Phi-3.5-MoE-Instruct](https://aka.ms/azureai/landing/Phi-3.5-MoE-Instruct)
-
-
-## Prerequisites
-
-To use Phi-3.5 MoE chat model with Azure AI Studio, you need the following prerequisites:
-
-### A model deployment
-
-**Deployment to a self-hosted managed compute**
-
-Phi-3.5 MoE chat model can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
-
-For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
-
-> [!div class="nextstepaction"]
-> [Deploy the model to managed compute](../concepts/deployments-overview.md)
-
-### The inference package installed
-
-You can consume predictions from this model by using the `@azure-rest/ai-inference` package from `npm`. To install this package, you need the following prerequisites:
-
-* LTS versions of `Node.js` with `npm`.
-* The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
-* Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
-
-Once you have these prerequisites, install the Azure Inference library for JavaScript with the following command:
-
-```bash
-npm install @azure-rest/ai-inference
-```
-
-## Work with chat completions
-
-In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
-
-> [!TIP]
-> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Studio with the same code and structure, including Phi-3.5 MoE chat model.
-
-### Create a client to consume the model
-
-First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
-
-
-```javascript
-import ModelClient from "@azure-rest/ai-inference";
-import { isUnexpected } from "@azure-rest/ai-inference";
-import { AzureKeyCredential } from "@azure/core-auth";
-
-const client = new ModelClient(
-    process.env.AZURE_INFERENCE_ENDPOINT, 
-    new AzureKeyCredential(process.env.AZURE_INFERENCE_CREDENTIAL)
-);
-```
-
-When you deploy the model to a self-hosted online endpoint with **Microsoft Entra ID** support, you can use the following code snippet to create a client.
-
-
-```javascript
-import ModelClient from "@azure-rest/ai-inference";
-import { isUnexpected } from "@azure-rest/ai-inference";
-import { DefaultAzureCredential }  from "@azure/identity";
-
-const client = new ModelClient(
-    process.env.AZURE_INFERENCE_ENDPOINT, 
-    new DefaultAzureCredential()
-);
-```
-
-### Get the model's capabilities
-
-The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
-
-
-```javascript
-var model_info = await client.path("/info").get()
-```
-
-The response is as follows:
-
-
-```javascript
-console.log("Model name: ", model_info.body.model_name)
-console.log("Model type: ", model_info.body.model_type)
-console.log("Model provider name: ", model_info.body.model_provider_name)
-```
-
-```console
-Model name: Phi-3.5-MoE-Instruct
-Model type: chat-completions
-Model provider name: Microsoft
-```
-
-### Create a chat completion request
-
-The following example shows how you can create a basic chat completions request to the model.
-
-```javascript
-var messages = [
-    { role: "system", content: "You are a helpful assistant" },
-    { role: "user", content: "How many languages are in the world?" },
-];
-
-var response = await client.path("/chat/completions").post({
-    body: {
-        messages: messages,
-    }
-});
-```
-
-> [!NOTE]
-> Phi-3.5-MoE-Instruct doesn't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
-
-The response is as follows, where you can see the model's usage statistics:
-
-
-```javascript
-if (isUnexpected(response)) {
-    throw response.body.error;
-}
-
-console.log("Response: ", response.body.choices[0].message.content);
-console.log("Model: ", response.body.model);
-console.log("Usage:");
-console.log("\tPrompt tokens:", response.body.usage.prompt_tokens);
-console.log("\tTotal tokens:", response.body.usage.total_tokens);
-console.log("\tCompletion tokens:", response.body.usage.completion_tokens);
-```
-
-```console
-Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
-Model: Phi-3.5-MoE-Instruct
-Usage: 
-  Prompt tokens: 19
-  Total tokens: 91
-  Completion tokens: 72
-```
-
-Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
-
-#### Stream content
-
-By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
-
-You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
-
-
-```javascript
-var messages = [
-    { role: "system", content: "You are a helpful assistant" },
-    { role: "user", content: "How many languages are in the world?" },
-];
-
-var response = await client.path("/chat/completions").post({
-    body: {
-        messages: messages,
-    }
-}).asNodeStream();
-```
-
-To stream completions, use `.asNodeStream()` when you call the model.
-
-You can visualize how streaming generates content:
-
-
-```javascript
-var stream = response.body;
-if (!stream) {
-    stream.destroy();
-    throw new Error(`Failed to get chat completions with status: ${response.status}`);
-}
-
-if (response.status !== "200") {
-    throw new Error(`Failed to get chat completions: ${response.body.error}`);
-}
-
-var sses = createSseStream(stream);
-
-for await (const event of sses) {
-    if (event.data === "[DONE]") {
-        return;
-    }
-    for (const choice of (JSON.parse(event.data)).choices) {
-        console.log(choice.delta?.content ?? "");
-    }
-}
-```
-
-#### Explore more parameters supported by the inference client
-
-Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
-
-```javascript
-var messages = [
-    { role: "system", content: "You are a helpful assistant" },
-    { role: "user", content: "How many languages are in the world?" },
-];
-
-var response = await client.path("/chat/completions").post({
-    body: {
-        messages: messages,
-        presence_penalty: "0.1",
-        frequency_penalty: "0.8",
-        max_tokens: 2048,
-        stop: ["<|endoftext|>"],
-        temperature: 0,
-        top_p: 1,
-        response_format: { type: "text" },
-    }
-});
-```
-
-> [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
-
-If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
-
-### Pass extra parameters to the model
-
-The Azure AI Model Inference API allows you to pass extra parameters to the model. The following code example shows how to pass the extra parameter `logprobs` to the model. 
-
-Before you pass extra parameters to the Azure AI model inference API, make sure your model supports those extra parameters. When the request is made to the underlying model, the header `extra-parameters` is passed to the model with the value `pass-through`. This value tells the endpoint to pass the extra parameters to the model. Use of extra parameters with the model doesn't guarantee that the model can actually handle them. Read the model's documentation to understand which extra parameters are supported.
-
-
-```javascript
-var messages = [
-    { role: "system", content: "You are a helpful assistant" },
-    { role: "user", content: "How many languages are in the world?" },
-];
-
-var response = await client.path("/chat/completions").post({
-    headers: {
-        "extra-params": "pass-through"
-    },
-    body: {
-        messages: messages,
-        logprobs: true
-    }
-});
-```
-
-The following extra parameters can be passed to Phi-3.5 MoE chat model:
-
-| Name           | Description           | Type            |
-| -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
-| `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
-| `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
-
-
-::: zone-end
-
-
-::: zone pivot="programming-language-csharp"
-
-## Phi-3.5 MoE chat model
-
-Phi-3.5 models are lightweight, state-of-the-art open models. These models were trained with Phi-3 datasets that include both synthetic data and the filtered, publicly available websites data, with a focus on high quality and reasoning-dense properties. Phi-3.5 MoE uses 16x3.8B parameters with 6.6B active parameters when using 2 experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
-
-The models underwent a rigorous enhancement process, incorporating both supervised fine-tuning, proximal policy optimization, and direct preference optimization to ensure precise instruction adherence and robust safety measures.
-
-The Phi-3.5 models come in the following variants, with the variants having a context length (in tokens) of 128K.
-
-
-You can learn more about the models in their respective model card:
-
-* [Phi-3.5-MoE-Instruct](https://aka.ms/azureai/landing/Phi-3.5-MoE-Instruct)
-
-
-## Prerequisites
-
-To use Phi-3.5 MoE chat model with Azure AI Studio, you need the following prerequisites:
-
-### A model deployment
-
-**Deployment to a self-hosted managed compute**
-
-Phi-3.5 MoE chat model can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
-
-For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
-
-> [!div class="nextstepaction"]
-> [Deploy the model to managed compute](../concepts/deployments-overview.md)
-
-### The inference package installed
-
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
-
-* The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
-* Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
-
-Once you have these prerequisites, install the Azure AI inference library with the following command:
-
-```dotnetcli
-dotnet add package Azure.AI.Inference --prerelease
-```
-
-You can also authenticate with Microsoft Entra ID (formerly Azure Active Directory). To use credential providers provided with the Azure SDK, install the `Azure.Identity` package:
-
-```dotnetcli
-dotnet add package Azure.Identity
-```
-
-Import the following namespaces:
-
-
-```csharp
-using Azure;
-using Azure.Identity;
-using Azure.AI.Inference;
-```
-
-This example also uses the following namespaces but you may not always need them:
-
-
-```csharp
-using System.Text.Json;
-using System.Text.Json.Serialization;
-using System.Reflection;
-```
-
-## Work with chat completions
-
-In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
-
-> [!TIP]
-> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Studio with the same code and structure, including Phi-3.5 MoE chat model.
-
-### Create a client to consume the model
-
-First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
-
-
-```csharp
-ChatCompletionsClient client = new ChatCompletionsClient(
-    new Uri(Environment.GetEnvironmentVariable("AZURE_INFERENCE_ENDPOINT")),
-    new AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_INFERENCE_CREDENTIAL"))
-);
-```
-
-When you deploy the model to a self-hosted online endpoint with **Microsoft Entra ID** support, you can use the following code snippet to create a client.
-
-
-```csharp
-client = new ChatCompletionsClient(
-    new Uri(Environment.GetEnvironmentVariable("AZURE_INFERENCE_ENDPOINT")),
-    new DefaultAzureCredential(includeInteractiveCredentials: true)
-);
-```
-
-### Get the model's capabilities
-
-The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
-
-
-```csharp
-Response<ModelInfo> modelInfo = client.GetModelInfo();
-```
-
-The response is as follows:
-
-
-```csharp
-Console.WriteLine($"Model name: {modelInfo.Value.ModelName}");
-Console.WriteLine($"Model type: {modelInfo.Value.ModelType}");
-Console.WriteLine($"Model provider name: {modelInfo.Value.ModelProviderName}");
-```
-
-```console
-Model name: Phi-3.5-MoE-Instruct
-Model type: chat-completions
-Model provider name: Microsoft
-```
-
-### Create a chat completion request
-
-The following example shows how you can create a basic chat completions request to the model.
-
-```csharp
-ChatCompletionsOptions requestOptions = new ChatCompletionsOptions()
-{
-    Messages = {
-        new ChatRequestSystemMessage("You are a helpful assistant."),
-        new ChatRequestUserMessage("How many languages are in the world?")
-    },
-};
-
-Response<ChatCompletions> response = client.Complete(requestOptions);
-```
-
-> [!NOTE]
-> Phi-3.5-MoE-Instruct doesn't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
-
-The response is as follows, where you can see the model's usage statistics:
-
-
-```csharp
-Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
-Console.WriteLine($"Model: {response.Value.Model}");
-Console.WriteLine("Usage:");
-Console.WriteLine($"\tPrompt tokens: {response.Value.Usage.PromptTokens}");
-Console.WriteLine($"\tTotal tokens: {response.Value.Usage.TotalTokens}");
-Console.WriteLine($"\tCompletion tokens: {response.Value.Usage.CompletionTokens}");
-```
-
-```console
-Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
-Model: Phi-3.5-MoE-Instruct
-Usage: 
-  Prompt tokens: 19
-  Total tokens: 91
-  Completion tokens: 72
-```
-
-Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
-
-#### Stream content
-
-By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
-
-You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
-
-
-```csharp
-static async Task StreamMessageAsync(ChatCompletionsClient client)
-{
-    ChatCompletionsOptions requestOptions = new ChatCompletionsOptions()
-    {
-        Messages = {
-            new ChatRequestSystemMessage("You are a helpful assistant."),
-            new ChatRequestUserMessage("How many languages are in the world? Write an essay about it.")
-        },
-        MaxTokens=4096
-    };
-
-    StreamingResponse<StreamingChatCompletionsUpdate> streamResponse = await client.CompleteStreamingAsync(requestOptions);
-
-    await PrintStream(streamResponse);
-}
-```
-
-To stream completions, use `CompleteStreamingAsync` method when you call the model. Notice that in this example we the call is wrapped in an asynchronous method.
-
-To visualize the output, define an asynchronous method to print the stream in the console.
-
-```csharp
-static async Task PrintStream(StreamingResponse<StreamingChatCompletionsUpdate> response)
-{
-    await foreach (StreamingChatCompletionsUpdate chatUpdate in response)
-    {
-        if (chatUpdate.Role.HasValue)
-        {
-            Console.Write($"{chatUpdate.Role.Value.ToString().ToUpperInvariant()}: ");
-        }
-        if (!string.IsNullOrEmpty(chatUpdate.ContentUpdate))
-        {
-            Console.Write(chatUpdate.ContentUpdate);
-        }
-    }
-}
-```
-
-You can visualize how streaming generates content:
-
-
-```csharp
-StreamMessageAsync(client).GetAwaiter().GetResult();
-```
-
-#### Explore more parameters supported by the inference client
-
-Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
-
-```csharp
-requestOptions = new ChatCompletionsOptions()
-{
-    Messages = {
-        new ChatRequestSystemMessage("You are a helpful assistant."),
-        new ChatRequestUserMessage("How many languages are in the world?")
-    },
-    PresencePenalty = 0.1f,
-    FrequencyPenalty = 0.8f,
-    MaxTokens = 2048,
-    StopSequences = { "<|endoftext|>" },
-    Temperature = 0,
-    NucleusSamplingFactor = 1,
-    ResponseFormat = new ChatCompletionsResponseFormatText()
-};
-
-response = client.Complete(requestOptions);
-Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
-```
-
-> [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
-
-If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
-
-### Pass extra parameters to the model
-
-The Azure AI Model Inference API allows you to pass extra parameters to the model. The following code example shows how to pass the extra parameter `logprobs` to the model. 
-
-Before you pass extra parameters to the Azure AI model inference API, make sure your model supports those extra parameters. When the request is made to the underlying model, the header `extra-parameters` is passed to the model with the value `pass-through`. This value tells the endpoint to pass the extra parameters to the model. Use of extra parameters with the model doesn't guarantee that the model can actually handle them. Read the model's documentation to understand which extra parameters are supported.
-
-
-```csharp
-requestOptions = new ChatCompletionsOptions()
-{
-    Messages = {
-        new ChatRequestSystemMessage("You are a helpful assistant."),
-        new ChatRequestUserMessage("How many languages are in the world?")
-    },
-    AdditionalProperties = { { "logprobs", BinaryData.FromString("true") } },
-};
-
-response = client.Complete(requestOptions, extraParams: ExtraParameters.PassThrough);
-Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
-```
-
-The following extra parameters can be passed to Phi-3.5 MoE chat model:
-
-| Name           | Description           | Type            |
-| -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
-| `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
-| `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
-
-
-::: zone-end
-
-
-::: zone pivot="programming-language-rest"
-
-## Phi-3.5 MoE chat model
-
-Phi-3.5 models are lightweight, state-of-the-art open models. These models were trained with Phi-3 datasets that include both synthetic data and the filtered, publicly available websites data, with a focus on high quality and reasoning-dense properties. Phi-3.5 MoE uses 16x3.8B parameters with 6.6B active parameters when using 2 experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
-
-The models underwent a rigorous enhancement process, incorporating both supervised fine-tuning, proximal policy optimization, and direct preference optimization to ensure precise instruction adherence and robust safety measures.
-
-The Phi-3.5 models come in the following variants, with the variants having a context length (in tokens) of 128K.
-
-
-You can learn more about the models in their respective model card:
-
-* [Phi-3.5-MoE-Instruct](https://aka.ms/azureai/landing/Phi-3.5-MoE-Instruct)
-
-
-## Prerequisites
-
-To use Phi-3.5 MoE chat model with Azure AI Studio, you need the following prerequisites:
-
-### A model deployment
-
-**Deployment to a self-hosted managed compute**
-
-Phi-3.5 MoE chat model can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
-
-For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
-
-> [!div class="nextstepaction"]
-> [Deploy the model to managed compute](../concepts/deployments-overview.md)
-
-### A REST client
-
-Models deployed with the [Azure AI model inference API](https://aka.ms/azureai/modelinference) can be consumed using any REST client. To use the REST client, you need the following prerequisites:
-
-* To construct the requests, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name`` is your unique model deployment host name and `your-azure-region`` is the Azure region where the model is deployed (for example, eastus2).
-* Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
-
-## Work with chat completions
-
-In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
-
-> [!TIP]
-> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Studio with the same code and structure, including Phi-3.5 MoE chat model.
-
-### Create a client to consume the model
-
-First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
-
-When you deploy the model to a self-hosted online endpoint with **Microsoft Entra ID** support, you can use the following code snippet to create a client.
-
-### Get the model's capabilities
-
-The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
-
-```http
-GET /info HTTP/1.1
-Host: <ENDPOINT_URI>
-Authorization: Bearer <TOKEN>
-Content-Type: application/json
-```
-
-The response is as follows:
-
-
-```json
-{
-    "model_name": "Phi-3.5-MoE-Instruct",
-    "model_type": "chat-completions",
-    "model_provider_name": "Microsoft"
-}
-```
-
-### Create a chat completion request
-
-The following example shows how you can create a basic chat completions request to the model.
-
-```json
-{
-    "messages": [
-        {
-            "role": "system",
-            "content": "You are a helpful assistant."
-        },
-        {
-            "role": "user",
-            "content": "How many languages are in the world?"
-        }
-    ]
-}
-```
-
-> [!NOTE]
-> Phi-3.5-MoE-Instruct doesn't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
-
-The response is as follows, where you can see the model's usage statistics:
-
-
-```json
-{
-    "id": "0a1234b5de6789f01gh2i345j6789klm",
-    "object": "chat.completion",
-    "created": 1718726686,
-    "model": "Phi-3.5-MoE-Instruct",
-    "choices": [
-        {
-            "index": 0,
-            "message": {
-                "role": "assistant",
-                "content": "As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.",
-                "tool_calls": null
-            },
-            "finish_reason": "stop",
-            "logprobs": null
-        }
-    ],
-    "usage": {
-        "prompt_tokens": 19,
-        "total_tokens": 91,
-        "completion_tokens": 72
-    }
-}
-```
-
-Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
-
-#### Stream content
-
-By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
-
-You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
-
-
-```json
-{
-    "messages": [
-        {
-            "role": "system",
-            "content": "You are a helpful assistant."
-        },
-        {
-            "role": "user",
-            "content": "How many languages are in the world?"
-        }
-    ],
-    "stream": true,
-    "temperature": 0,
-    "top_p": 1,
-    "max_tokens": 2048
-}
-```
-
-You can visualize how streaming generates content:
-
-
-```json
-{
-    "id": "23b54589eba14564ad8a2e6978775a39",
-    "object": "chat.completion.chunk",
-    "created": 1718726371,
-    "model": "Phi-3.5-MoE-Instruct",
-    "choices": [
-        {
-            "index": 0,
-            "delta": {
-                "role": "assistant",
-                "content": ""
-            },
-            "finish_reason": null,
-            "logprobs": null
-        }
-    ]
-}
-```
-
-The last message in the stream has `finish_reason` set, indicating the reason for the generation process to stop.
-
-
-```json
-{
-    "id": "23b54589eba14564ad8a2e6978775a39",
-    "object": "chat.completion.chunk",
-    "created": 1718726371,
-    "model": "Phi-3.5-MoE-Instruct",
-    "choices": [
-        {
-            "index": 0,
-            "delta": {
-                "content": ""
-            },
-            "finish_reason": "stop",
-            "logprobs": null
-        }
-    ],
-    "usage": {
-        "prompt_tokens": 19,
-        "total_tokens": 91,
-        "completion_tokens": 72
-    }
-}
-```
-
-#### Explore more parameters supported by the inference client
-
-Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
-
-```json
-{
-    "messages": [
-        {
-            "role": "system",
-            "content": "You are a helpful assistant."
-        },
-        {
-            "role": "user",
-            "content": "How many languages are in the world?"
-        }
-    ],
-    "presence_penalty": 0.1,
-    "frequency_penalty": 0.8,
-    "max_tokens": 2048,
-    "stop": ["<|endoftext|>"],
-    "temperature" :0,
-    "top_p": 1,
-    "response_format": { "type": "text" }
-}
-```
-
-
-```json
-{
-    "id": "0a1234b5de6789f01gh2i345j6789klm",
-    "object": "chat.completion",
-    "created": 1718726686,
-    "model": "Phi-3.5-MoE-Instruct",
-    "choices": [
-        {
-            "index": 0,
-            "message": {
-                "role": "assistant",
-                "content": "As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.",
-                "tool_calls": null
-            },
-            "finish_reason": "stop",
-            "logprobs": null
-        }
-    ],
-    "usage": {
-        "prompt_tokens": 19,
-        "total_tokens": 91,
-        "completion_tokens": 72
-    }
-}
-```
-
-> [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
-
-If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
-
-### Pass extra parameters to the model
-
-The Azure AI Model Inference API allows you to pass extra parameters to the model. The following code example shows how to pass the extra parameter `logprobs` to the model. 
-
-Before you pass extra parameters to the Azure AI model inference API, make sure your model supports those extra parameters. When the request is made to the underlying model, the header `extra-parameters` is passed to the model with the value `pass-through`. This value tells the endpoint to pass the extra parameters to the model. Use of extra parameters with the model doesn't guarantee that the model can actually handle them. Read the model's documentation to understand which extra parameters are supported.
-
-```http
-POST /chat/completions HTTP/1.1
-Host: <ENDPOINT_URI>
-Authorization: Bearer <TOKEN>
-Content-Type: application/json
-extra-parameters: pass-through
-```
-
-
-```json
-{
-    "messages": [
-        {
-            "role": "system",
-            "content": "You are a helpful assistant."
-        },
-        {
-            "role": "user",
-            "content": "How many languages are in the world?"
-        }
-    ],
-    "logprobs": true
-}
-```
-
-The following extra parameters can be passed to Phi-3.5 MoE chat model:
-
-| Name           | Description           | Type            |
-| -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
-| `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
-| `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
-
-
-::: zone-end
-
-## More inference examples
-
-For more examples of how to use Phi-3 family models, see the following examples and tutorials:
-
-| Description                               | Language          | Sample                                                          |
-|-------------------------------------------|-------------------|-----------------------------------------------------------------|
-| CURL request                              | Bash              | [Link](https://aka.ms/phi-3/webrequests-sample)         |
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
-| Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
-| Python web requests                       | Python            | [Link](https://aka.ms/phi-3/webrequests-sample)         |
-| OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/phi-3/openaisdk)                  |
-| LangChain                                 | Python            | [Link](https://aka.ms/phi-3/langchain-sample)           |
-| LiteLLM                                   | Python            | [Link](https://aka.ms/phi-3/litellm-sample)             | 
-
-
-## Cost and quota considerations for Phi-3 family models deployed to managed compute
-
-Phi-3 family models deployed to managed compute are billed based on core hours of the associated compute instance. The cost of the compute instance is determined by the size of the instance, the number of instances running, and the run duration.
-
-It is a good practice to start with a low number of instances and scale up as needed. You can monitor the cost of the compute instance in the Azure portal.
-
-## Related content
-
-
-* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
-* [Deploy models as serverless APIs](deploy-models-serverless.md)
-* [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
-* [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Phi-3.5 MoEモデルのドキュメント削除"
}
```

### Explanation
このコードの差分は、`deploy-models-phi-3-5-moe.md`というファイルが完全に削除されたことを示しています。この変更により、Phi-3.5 MoE（Mixture of Experts）チャットモデルに関する情報がすべて失われます。具体的な影響は以下の通りです：

1. **ドキュメント内容の削除**: 1153行に及ぶコンテンツが削除されており、このドキュメントはPhi-3.5 MoEモデルの使用方法、要件、機能に関する詳細な説明を提供していました。この情報が失われることで、ユーザーはこの特定のモデルに関連した指示やガイダンスにアクセスできなくなります。

2. **影響の評価**: Phi-3.5 MoEモデルを使用している開発者やユーザーは、公式なドキュメントに依存していたため、この削除によってその利用に困難が生じる可能性があります。また、モデルの利用法やその展開に関する具体的な手順、APIのインターフェースに関する情報も失われています。

3. **利用者の再教育の必要性**: この変更は利用者に多大な影響を及ぼすため、代替のリソースや新たなドキュメントが必要となるでしょう。新しい情報源が提供されない場合、使用中の顧客は他のモデルや方法に移行することを余儀なくされるかもしれません。

4. **ビジネスリスク**: このような情報の削除は、特に依存していたユーザーや顧客へのサポートに悪影響を及ぼす可能性があり、顧客満足度の低下や信頼の喪失につながることがあります。

これにより、企業や開発者にとって、Phi-3.5 MoEモデルの利用の可用性が脅かされ、代替手段を模索する必要が出てくるかもしれません。このファイルの削除は、利用者が同モデルを使用する際の重要な情報を失わせる重大な変更です。

## articles/ai-studio/how-to/deploy-models-phi-3.md{#item-47e305}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Phi-3 family chat models with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 09/13/2024
+ms.date: 09/18/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -31,7 +31,11 @@ The Phi-3 family chat models include the following models:
 
 # [Phi-3.5](#tab/phi-3-5)
 
-Phi-3.5 models are lightweight, state-of-the-art open models. These models were trained with Phi-3 datasets that include both synthetic data and the filtered, publicly available websites data, with a focus on high quality and reasoning-dense properties. Phi-3.5 Mini uses 3.8B parameters, and is a dense decoder-only transformer model using the same tokenizer as Phi-3 Mini.
+Phi-3.5 models are lightweight, state-of-the-art open models. These models were trained with Phi-3 datasets that include both synthetic data and the filtered, publicly available websites data, with a focus on high quality and reasoning-dense properties.
+
+Phi-3.5 Mini uses 3.8B parameters, and is a dense decoder-only transformer model using the same tokenizer as Phi-3 Mini.
+
+Phi-3.5 MoE (mixture-of-expert) uses 16x3.8B parameters with 6.6B active parameters when using 2 experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
 
 The models underwent a rigorous enhancement process, incorporating both supervised fine-tuning, proximal policy optimization, and direct preference optimization to ensure precise instruction adherence and robust safety measures. When assessed against benchmarks that test common sense, language understanding, math, code, long context and logical reasoning, Phi-3.5 models showcased robust and state-of-the-art performance among models with less than 13 billion parameters.
 
@@ -41,6 +45,7 @@ The Phi-3.5 models come in the following variants, with the variants having a co
 The following models are available:
 
 * [Phi-3.5-Mini-Instruct](https://aka.ms/azureai/landing/Phi-3.5-Mini-Instruct)
+* [Phi-3.5-MoE-Instruct](https://aka.ms/azureai/landing/Phi-3.5-MoE-Instruct)
 
 
 # [Phi-3](#tab/phi-3)
@@ -184,7 +189,7 @@ response = client.complete(
 ```
 
 > [!NOTE]
-> Phi-3.5-Mini-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> Phi-3.5-Mini-Instruct, Phi-3.5-MoE-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -256,7 +261,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormatText
+from azure.ai.inference.models import ChatCompletionsResponseFormat
 
 response = client.complete(
     messages=[
@@ -354,7 +359,11 @@ The Phi-3 family chat models include the following models:
 
 # [Phi-3.5](#tab/phi-3-5)
 
-Phi-3.5 models are lightweight, state-of-the-art open models. These models were trained with Phi-3 datasets that include both synthetic data and the filtered, publicly available websites data, with a focus on high quality and reasoning-dense properties. Phi-3.5 Mini uses 3.8B parameters, and is a dense decoder-only transformer model using the same tokenizer as Phi-3 Mini.
+Phi-3.5 models are lightweight, state-of-the-art open models. These models were trained with Phi-3 datasets that include both synthetic data and the filtered, publicly available websites data, with a focus on high quality and reasoning-dense properties.
+
+Phi-3.5 Mini uses 3.8B parameters, and is a dense decoder-only transformer model using the same tokenizer as Phi-3 Mini.
+
+Phi-3.5 MoE (mixture-of-expert) uses 16x3.8B parameters with 6.6B active parameters when using 2 experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
 
 The models underwent a rigorous enhancement process, incorporating both supervised fine-tuning, proximal policy optimization, and direct preference optimization to ensure precise instruction adherence and robust safety measures. When assessed against benchmarks that test common sense, language understanding, math, code, long context and logical reasoning, Phi-3.5 models showcased robust and state-of-the-art performance among models with less than 13 billion parameters.
 
@@ -364,6 +373,7 @@ The Phi-3.5 models come in the following variants, with the variants having a co
 The following models are available:
 
 * [Phi-3.5-Mini-Instruct](https://aka.ms/azureai/landing/Phi-3.5-Mini-Instruct)
+* [Phi-3.5-MoE-Instruct](https://aka.ms/azureai/landing/Phi-3.5-MoE-Instruct)
 
 
 # [Phi-3](#tab/phi-3)
@@ -507,7 +517,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!NOTE]
-> Phi-3.5-Mini-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> Phi-3.5-Mini-Instruct, Phi-3.5-MoE-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -700,7 +710,11 @@ The Phi-3 family chat models include the following models:
 
 # [Phi-3.5](#tab/phi-3-5)
 
-Phi-3.5 models are lightweight, state-of-the-art open models. These models were trained with Phi-3 datasets that include both synthetic data and the filtered, publicly available websites data, with a focus on high quality and reasoning-dense properties. Phi-3.5 Mini uses 3.8B parameters, and is a dense decoder-only transformer model using the same tokenizer as Phi-3 Mini.
+Phi-3.5 models are lightweight, state-of-the-art open models. These models were trained with Phi-3 datasets that include both synthetic data and the filtered, publicly available websites data, with a focus on high quality and reasoning-dense properties.
+
+Phi-3.5 Mini uses 3.8B parameters, and is a dense decoder-only transformer model using the same tokenizer as Phi-3 Mini.
+
+Phi-3.5 MoE (mixture-of-expert) uses 16x3.8B parameters with 6.6B active parameters when using 2 experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
 
 The models underwent a rigorous enhancement process, incorporating both supervised fine-tuning, proximal policy optimization, and direct preference optimization to ensure precise instruction adherence and robust safety measures. When assessed against benchmarks that test common sense, language understanding, math, code, long context and logical reasoning, Phi-3.5 models showcased robust and state-of-the-art performance among models with less than 13 billion parameters.
 
@@ -710,6 +724,7 @@ The Phi-3.5 models come in the following variants, with the variants having a co
 The following models are available:
 
 * [Phi-3.5-Mini-Instruct](https://aka.ms/azureai/landing/Phi-3.5-Mini-Instruct)
+* [Phi-3.5-MoE-Instruct](https://aka.ms/azureai/landing/Phi-3.5-MoE-Instruct)
 
 
 # [Phi-3](#tab/phi-3)
@@ -867,7 +882,7 @@ Response<ChatCompletions> response = client.Complete(requestOptions);
 ```
 
 > [!NOTE]
-> Phi-3.5-Mini-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> Phi-3.5-Mini-Instruct, Phi-3.5-MoE-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -1058,7 +1073,11 @@ The Phi-3 family chat models include the following models:
 
 # [Phi-3.5](#tab/phi-3-5)
 
-Phi-3.5 models are lightweight, state-of-the-art open models. These models were trained with Phi-3 datasets that include both synthetic data and the filtered, publicly available websites data, with a focus on high quality and reasoning-dense properties. Phi-3.5 Mini uses 3.8B parameters, and is a dense decoder-only transformer model using the same tokenizer as Phi-3 Mini.
+Phi-3.5 models are lightweight, state-of-the-art open models. These models were trained with Phi-3 datasets that include both synthetic data and the filtered, publicly available websites data, with a focus on high quality and reasoning-dense properties.
+
+Phi-3.5 Mini uses 3.8B parameters, and is a dense decoder-only transformer model using the same tokenizer as Phi-3 Mini.
+
+Phi-3.5 MoE (mixture-of-expert) uses 16x3.8B parameters with 6.6B active parameters when using 2 experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
 
 The models underwent a rigorous enhancement process, incorporating both supervised fine-tuning, proximal policy optimization, and direct preference optimization to ensure precise instruction adherence and robust safety measures. When assessed against benchmarks that test common sense, language understanding, math, code, long context and logical reasoning, Phi-3.5 models showcased robust and state-of-the-art performance among models with less than 13 billion parameters.
 
@@ -1068,6 +1087,7 @@ The Phi-3.5 models come in the following variants, with the variants having a co
 The following models are available:
 
 * [Phi-3.5-Mini-Instruct](https://aka.ms/azureai/landing/Phi-3.5-Mini-Instruct)
+* [Phi-3.5-MoE-Instruct](https://aka.ms/azureai/landing/Phi-3.5-MoE-Instruct)
 
 
 # [Phi-3](#tab/phi-3)
@@ -1180,7 +1200,7 @@ The following example shows how you can create a basic chat completions request
 ```
 
 > [!NOTE]
-> Phi-3.5-Mini-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> Phi-3.5-Mini-Instruct, Phi-3.5-MoE-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3モデルのドキュメントの修正"
}
```

### Explanation
このコードの差分は、`deploy-models-phi-3.md`ファイルに対する修正を示しています。主な変更点は、内容の追加、文言の改善、そして日付の更新が含まれています。具体的な変更点は以下の通りです：

1. **日付の更新**: ドキュメントの更新日が`09/13/2024`から`09/18/2024`に変更されました。これは、ファイルが最終的に修正された日を反映しています。

2. **内容の追加**: Phi-3.5 MoE（Mixture of Experts）モデルに関する詳細が新たに追加され、具体的にはそのパラメータ数やモデルの特性について説明が加えられました。この情報により、モデルの利用者はPhi-3.5 MoEについてより具体的な理解を深めることができます。

3. **文言の整理**: テキストが整理され、Phi-3.5モデルに関する説明が分割され、各モデルの詳細が明確に記述されています。特に、Phi-3.5 MoEモデルに関する情報が強調されています。また、モデルのトークナイザーについても言及されています。

4. **注釈の拡張**: キャパビリティに関する注釈が更新され、今後の利用者に向けてのアラートや情報も含まれています。この変更は、他のモデルとの違いや使用上の注意点を明確にするために重要です。

このような修正は、ユーザーがPhi-3モデルをより効果的に活用できるよう支援するためのものであり、特に新たに追加された内容は、利用者にとって有益な情報を提供しています。

## articles/ai-studio/how-to/develop/llama-index.md{#item-613372}

<details>
<summary>Diff</summary>
````diff
@@ -138,7 +138,7 @@ llm = AzureAICompletionsModel(
 
 ## Use LLMs models
 
-You can use the client directly or [#configure-the-models-used-by-your-code](Configure the models used by your code) in LlamaIndex. To use the model directly, use the `chat` method for chat instruction models:
+You can use the client directly or [Configure the models used by your code](#configure-the-models-used-by-your-code) in LlamaIndex. To use the model directly, use the `chat` method for chat instruction models:
 
 ```python
 from llama_index.core.llms import ChatMessage
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "LlamaIndexのモデル構成に関するリンク修正"
}
```

### Explanation
このコードの差分は、`llama-index.md`ファイルにおける小規模な修正を示しています。主な変更は、リンクの形式を整えるための文言の変更です。

1. **リンクの修正**: `Configure the models used by your code`という部分の記述が変更されました。修正前はリンクの形式が不適切であり、修正後は文脈に適したリンク形式が適用されています。これにより、読者がリンクをクリックした際に正しいセクションに容易にアクセスできるようになります。

2. **テキストの簡略化**: 文中の文言がわずかに変更され、より流暢で理解しやすい表現になっています。この修正は、テキストの可読性を向上させ、利用者が内容を迅速に把握できるよう支援しています。

3. **最小限の内容の変更**: この差分は、主にリンクの整備とテキストの微調整に関するもので、その内容は大きな影響を与えるものではありませんが、文書の品質を向上させる重要な作業です。

この更新により、LlamaIndexの利用者は、モデルの構成に関するリンクにアクセスする際の経験が向上し、文書全体の整合性と正確性が増します。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -68,7 +68,7 @@ Llama family models | Llama-2-7b <br> Llama-2-7b-chat <br> Llama-2-13b <br> Llam
 Mistral family models | mistralai-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x22B-Instruct-v0-1 <br> mistral-community-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x7B-v01 <br> mistralai-Mistral-7B-Instruct-v0-2 <br> mistralai-Mistral-7B-v01 <br> mistralai-Mixtral-8x7B-Instruct-v01 <br> mistralai-Mistral-7B-Instruct-v01 | Mistral-large (2402) <br> Mistral-large (2407) <br> Mistral-small <br> Mistral-NeMo
 Cohere family models | Not available | Cohere-command-r-plus <br> Cohere-command-r <br> Cohere-embed-v3-english <br> Cohere-embed-v3-multilingual <br> Cohere-rerank-v3-english <br> Cohere-rerank-v3-multilingual
 JAIS | Not available | jais-30b-chat
-Phi-3 family models | Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> Phi-3-vision-128k-Instruct <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct | Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct
+Phi-3 family models | Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> Phi-3-vision-128k-Instruct <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct | Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct
 Nixtla | Not available | TimeGEN-1
 Other models | Available | Not available
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3モデルのリストの整備"
}
```

### Explanation
このコードの差分は、`model-catalog-overview.md`ファイルに対する小さな修正を示しています。主な変更点は、Phi-3ファミリーのモデルに関するリストの書式が整理されたことです。

1. **表記の修正**: Phi-3ファミリーのモデルのリストが、前の行から改行されて単純にスペースが追加されただけの形ですが、リストの整合性が向上しています。これは、情報の視認性を高め、利用者がより簡単にモデルを見つけられるようにするための改善です。

2. **テキストの一貫性**: 在るべき関連モデルとそのバリエーションの表記が整理され、重複や不必要な空白が除去されています。これにより、リストがより明確かつ一貫性のある形式になっています。

このような修正は、文書を読みやすくし、利用者がモデルの情報を迅速に理解できるように支援します。Phi-3ファミリーのモデルに関する情報がクリアに示されることで、より効果的なドキュメントの提供が実現されています。

## articles/ai-studio/includes/region-availability-maas.md{#item-35d79c}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: scottpolly
 ms.service: azure-ai-studio
 ms.topic: include
 ms.date: 08/05/2024
-ms.custom: include
+ms.custom: include, references_regions
 ---
 
 ### Cohere models
@@ -45,6 +45,7 @@ Llama 3.1 405B Instruct  | [Microsoft Managed Countries](/partner-center/marketp
 |Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
 Phi-3.5-vision-Instruct     | Not applicable | East US 2 <br> Sweden Central  | Not available       |
+Phi-3.5-MoE-Instruct     | Not applicable | East US 2 <br> Sweden Central  | Not available       |
 Phi-3.5-Mini-Instruct     | Not applicable | East US 2 <br> Sweden Central  | Not available       |
 Phi-3-Mini-4k-Instruct <br>  Phi-3-Mini-128K-Instruct    | Not applicable | East US 2 <br> Sweden Central  | East US 2  |
 Phi-3-Small-8K-Instruct <br>  Phi-3-Small-128K-Instruct     | Not applicable | East US 2 <br> Sweden Central  | Not available       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチリージョンのサポートを示す新しいメタデータの追加"
}
```

### Explanation
このコードの差分は、`region-availability-maas.md`ファイルに対する小さな修正を示しています。主な変更点は、マルチリージョンサービスに関連する新しいメタデータを加えたことです。

1. **メタデータの更新**: ファイル内の`ms.custom`フィールドが`include`から`include, references_regions`に変更されました。この更新により、文書が特定のリージョンに関連する情報を参照することを明示的に示しています。これにより、利用者はこのドキュメントがマルチリージョンサポートを持つことを理解しやすくなります。

2. **モデル情報の追加**: Phi-3.5-MoE-Instructという新しいモデルの行が追加されました。このモデルは「Not applicable」というステータスで、デプロイメント用の地域として「East US 2」と「Sweden Central」がリストされています。この変更は、モデルの可用性に関する情報を増やし、利用者に対して具体的な地域の選択肢を提供しています。

これらの変更は、ユーザーが利用可能なリソースやサービスの状況をより明確に理解できるようにし、マルチリージョンサポートの一環としてのサービスの透明性を高めることに寄与しています。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -131,8 +131,6 @@ items:
       items:
         - name: Phi-3 family chat models
           href: how-to/deploy-models-phi-3.md
-        - name: Phi-3.5 MoE chat model
-          href: how-to/deploy-models-phi-3-5-moe.md
         - name: Phi-3 chat model with vision
           href: how-to/deploy-models-phi-3-vision.md
         - name: Phi-3.5 chat model with vision
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3.5 MoEチャットモデルの削除"
}
```

### Explanation
このコードの差分は、`toc.yml`ファイルに対する小さな修正を示しています。主な変更点は、「Phi-3.5 MoEチャットモデル」という項目が削除されたことです。

1. **項目の削除**: `toc.yml`ファイルから「Phi-3.5 MoEチャットモデル」がリストから削除されました。この変更により、目次に表示されるモデル情報が更新され、Phi-3.5 MoEモデルに関連するハウツーへのリファレンスがなくなりました。

2. **整理された情報**: Phi-3ファミリーに関連する他のモデルやハウツーへのリンクはそのまま残されており、全体としての情報の整理が進み、ユーザーは他の必要な情報にアクセスしやすくなっています。

この変更は、関連する情報の明確化を目的としており、ユーザーが混乱することなく、必要なコンテンツを見つけやすくするためのものです。また、モデルの削除は、現在の利用可能なリソースの更新に伴った反映であると考えられます。


