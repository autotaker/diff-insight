---
date: '2025-01-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fee2fd2...MicrosoftDocs:c67b444
summary: この差分では、新機能の追加とユーザー体験を向上させるための小規模な更新が行われており、1つの重大な変更も含まれています。具体的には、Data Matrixバーベコード画像が新たに追加され、「What’s
  New」ドキュメントに新規API「Delete analyze response」に関連する情報が追加されました。しかし、Data Matrixバーベコードの画像ファイルが削除されるという重大な変更があります。その他、ドキュメントインテリジェンスに関する情報やFAQの更新、Codabarバーベコード画像の更新、LangChain開発ガイドの改訂が行われ、CSPサブスクリプションに関する制限情報も追加されました。これらの変更により、ユーザーに対する透明性と選択肢が拡充され、特にセキュリティとコンプライアンスが重視されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fee2fd2...MicrosoftDocs:c67b444){target="_blank"}

# Highlights
この差分のハイライトは、いくつかの新機能の追加およびユーザー体験向上を目指した小規模更新、そして1つの重大な変更を含んでいます。新しい画像やAPI情報の追加、既存ガイドラインの改訂が行われています。

## New features
- Data Matrixバーベコード画像の追加。
- 「What’s New」ドキュメントに新規API「Delete analyze response」に関連した詳細情報を追加。

## Breaking changes
- Data Matrixバーベコード画像ファイルの削除。

## Other updates
- ドキュメントインテリジェンスのアドオン機能情報の更新、特定のモデルやOfficeファイルタイプに関する制限を明確化。
- データの削除オプションについての説明をFAQに追加。
- Codabarバーベコード画像の更新。
- LangChainの開発ガイドの改訂、Mistral-Largeモデル関連の情報を明確化。
- モデルカタログ概要へのCSPサブスクリプション制限情報の追加。

# Insights
この差分において、新機能の追加と既存文書の小規模更新が目立ちます。特に、「What's New」ドキュメントへの新規API情報の追加と、それに伴うFAQの更新は、ユーザーにとって重要な透明性と選択肢の拡充を図っています。データ削除の迅速なオプション提供は、セキュリティとコンプライアンスを重視するユーザーに有益な更新です。

また、データマトリックスの視覚的なリソースを追加することで、ユーザーが特定のバーベコード技術を理解するための手助けをしています。一方で、既存のData Matrixバーベコードの画像が削除されたことは、互換性や既存のプロジェクトへの影響を考慮する必要があるため、開発者は注意が必要です。

LangChain開発ガイドはデプロイメント関連情報の整備とモデル名の具体化がされ、ユーザーの利便性と理解度を向上させました。また、CSPサブスクリプションに関する注意喚起により、利用者に対してより明確な情報提供を行っている点がポイントです。特に技術的な制約を明示することで、ユーザーの混乱を避け、より適切な利用を促進しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [add-on-capabilities.md](#item-96ed69) | minor update | ドキュメントインテリジェンスのアドオン機能に関する情報の更新 | modified | 7 | 7 | 14 | 
| [faq.yml](#item-7a051f) | minor update | ドキュメントインテリジェンスFAQのデータ削除オプションの追加 | modified | 2 | 1 | 3 | 
| [codabar.png](#item-f429fb) | minor update | Codabarバーベコード画像の更新 | modified | 0 | 0 | 0 | 
| [data-matrix.png](#item-b2d49a) | new feature | Data Matrixバーベコード画像の追加 | added | 0 | 0 | 0 | 
| [datamatrix.gif](#item-f7d62a) | breaking change | Data Matrixバーベコード画像の削除 | removed | 0 | 0 | 0 | 
| [whats-new.md](#item-1ec8d3) | minor update | 「What's New」ドキュメントの更新 | modified | 3 | 0 | 3 | 
| [langchain.md](#item-0d59f1) | minor update | LangChain開発ガイドの改訂 | modified | 14 | 18 | 32 | 
| [model-catalog-overview.md](#item-278001) | minor update | モデルカタログ概要の更新 | modified | 3 | 0 | 3 | 


# Modified Contents
## articles/ai-services/document-intelligence/concept/add-on-capabilities.md{#item-96ed69}

<details>
<summary>Diff</summary>
````diff
@@ -55,9 +55,9 @@ Document Intelligence supports more sophisticated and modular analysis capabilit
 
 > [!NOTE]
 >
-> * Not all add-on capabilities are supported by all models. For more information, *see* [model data extraction](../model-overview.md#model-analysis-features).
+> Not all models or Microsoft Office file types support add-on capabilities. For more information, *see* [model data extraction](../model-overview.md#model-analysis-features).
 >
-> * Add-on capabilities are currently not supported for Microsoft Office file types.
+
 :::moniker-end
 
 ## Version availability
@@ -73,7 +73,7 @@ Document Intelligence supports more sophisticated and modular analysis capabilit
 |High resolution extraction|**Add-On**| ✔️| ✔️| n/a| n/a|
 |Query fields|**Add-On**| ✔️|n/a|n/a| n/a|
 
-✱ Add-On - Query fields are priced differently than the other add-on features. See [pricing](https://azure.microsoft.com/pricing/details/ai-document-intelligence/) for details. </br>
+✱ Add-On - Query fields are priced differently than the other add-on features. See [pricing](https://azure.microsoft.com/pricing/details/ai-document-intelligence/) for details.</br>
 ** Add-On - Searchable pdf is available only with Read model as an add-on feature. 
 
 ## Supported file formats
@@ -759,7 +759,7 @@ The `ocr.barcode` capability extracts all identified barcodes in the `barcodes`
 | `Databar` |:::image type="content" source="../media/barcodes/databar.png" alt-text="Screenshot of the Data bar.":::|
 | `Databar` Expanded |:::image type="content" source="../media/barcodes/databar-expanded.gif" alt-text="Screenshot of the Data bar Expanded.":::|
 | `ITF` |:::image type="content" source="../media/barcodes/interleaved-two-five.png" alt-text="Screenshot of the interleaved-two-of-five barcode (ITF).":::|
-| `Data Matrix` |:::image type="content" source="../media/barcodes/datamatrix.gif" alt-text="Screenshot of the Data Matrix.":::|
+| `Data Matrix` |:::image type="content" source="../media/barcodes/data-matrix.png" alt-text="Screenshot of the Data Matrix.":::|
 
 ::: moniker range="doc-intel-4.0.0"
 
@@ -983,8 +983,8 @@ The searchable PDF capability enables you to convert an analog PDF, such as scan
 
   > [!IMPORTANT]
   >
-  > * Currently, the searchable PDF capability is only supported by Read OCR model `prebuilt-read`. When using this feature, please specify the `modelId` as `prebuilt-read`.
-  > * Searchable PDF is included with the 2024-11-30 (GA) `prebuilt-read` model with no usage cost for general PDF consumption.
+  > * Currently, only the Read model `prebuilt-read` supports the searchable PDF capability. When using this feature, specify the `modelId` as `prebuilt-read`.
+  > * Searchable PDF is included with the `2024-11-30` (GA) `prebuilt-read` model with no usage cost for general PDF consumption.
 
 ### Use searchable PDF
 
@@ -1044,7 +1044,7 @@ Query fields are an add-on capability to extend the schema extracted from any pr
 
 > [!NOTE]
 >
-> Document Intelligence Studio query field extraction is currently available with the Layout and Prebuilt models `2024-11-30 (GA) API with the exception of the `US tax` models (W2, 1098s, and 1099s models).
+> Document Intelligence Studio query field extraction is currently available with the Layout and Prebuilt models `2024-11-30` (GA) API except for US tax models W2, 1098, and 1099.
 
 ### Query field extraction
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのアドオン機能に関する情報の更新"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスにおけるアドオン機能の説明を更新することを目的としています。具体的には、アドオン機能がすべてのモデルやMicrosoft Officeファイルタイプに対応していないことを明示し、関連情報へのリンクを改善しています。また、特定の機能に関する注意事項や情報表現を調整しています。これには、データマトリックスのイメージを更新したり、特定のモデルバージョンについての明確な言及を行ったりしています。この修正により、ドキュメントがより正確でわかりやすくなり、ユーザーにとって有益な情報が提供されます。

## articles/ai-services/document-intelligence/faq.yml{#item-7a051f}

<details>
<summary>Diff</summary>
````diff
@@ -383,7 +383,8 @@ sections:
         answer: |
           **Yes,** briefly.
 
-          For all features, Document Intelligence temporarily stores data and results in Azure Storage in the same region as the request. Your data is then deleted within 24 hours from the time that you submit an analyze request.
+          For all features, Document Intelligence temporarily stores data and results in Azure Storage in the same region as the request. Your data is then deleted 24 hours from the time that you submit an analyze request. If you would like the data deleted sooner, you can call the [delete analyze response](https://learn.microsoft.com/rest/api/aiservices/document-models/delete-analyze-result?view=rest-aiservices-v4.0%20(2024-11-30)&tabs=HTTP). This API marks the results for deletion and is available in the v4.0 API.
+    
 
           Learn more about [data, privacy, and security for Document Intelligence](/legal/cognitive-services/document-intelligence/data-privacy-security?toc=/azure/ai-services/document-intelligence/toc.json&bc=/azure/ai-services/document-intelligence/breadcrumb/toc.json).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスFAQのデータ削除オプションの追加"
}
```

### Explanation
このコードの変更は、ドキュメントインテリジェンスのFAQセクションにおいて、データの削除に関するオプションを追加するものです。具体的には、ドキュメントインテリジェンスがデータを一時的にAzureストレージに保存し、分析リクエストが送信されてから24時間以内にデータが削除されることを説明しています。さらに、データをより早く削除したい場合には、「削除分析結果」APIを呼び出すことができ、そのAPIがv4.0に存在することも明記されています。この追加により、ユーザーがデータ管理に関する選択肢をよりよく理解できるようになり、透明性が向上します。

## articles/ai-services/document-intelligence/media/barcodes/codabar.png{#item-f429fb}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Codabarバーベコード画像の更新"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスに使用されるCodabarバーベコードの画像ファイルの更新を示しています。具体的な変更内容は表示されていませんが、画像ファイルが修正されたことにより、より最新の情報や表示品質が反映されている可能性があります。この更新により、関連する技術や文書において、バーベコードの視覚的な理解が向上し、ユーザーにとっての利便性が高まることが期待されます。

## articles/ai-services/document-intelligence/media/barcodes/data-matrix.png{#item-b2d49a}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Data Matrixバーベコード画像の追加"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスに関連する新しいファイルとしてData Matrixバーベコードの画像が追加されたことを示しています。この新しい画像は、ドキュメントインテリジェンスの機能を強化し、ユーザーがData Matrixバーベコードを視覚的に理解するためのリソースを提供します。これにより、適切なバーベコードの使用方法やアプリケーションに対する理解が促進され、ユーザーにとっての利便性が向上することが期待されます。

## articles/ai-services/document-intelligence/media/barcodes/datamatrix.gif{#item-f7d62a}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Data Matrixバーベコード画像の削除"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスに関連するData Matrixバーベコードの画像ファイルが削除されたことを示しています。このファイルの削除は、現在のドキュメントやシステム内でのData Matrixバーベコードの表示や使用に影響を与える可能性があります。ユーザーは、この画像が利用できないため、代替手段を検討する必要があるかもしれません。この変更は、ドキュメントの更新や情報の精度を高めるための意図的な行動である可能性がありますが、ユーザー体験に対して重要な影響を与えるリスクも伴います。

## articles/ai-services/document-intelligence/whats-new.md{#item-1ec8d3}

<details>
<summary>Diff</summary>
````diff
@@ -76,6 +76,9 @@ For more information, *see* client libraries for the following supported program
 *  [🆕 US Tax model](prebuilt/tax-document.md)
    *  New prebuilt tax models added for 1095A, 1095C, 1099SSA, and W4.
 
+* [Delete analyze response](https://learn.microsoft.com/rest/api/aiservices/document-models/delete-analyze-result?view=rest-aiservices-v4.0%20(2024-11-30)&tabs=HTTP)
+  * Analyze response is stored for 24 hours from when the operation completes for retrieval. For scenarios where you want to delete the response sooner, use the delete analyze response API to delete the response.  
+
 * The v4.0 API includes cumulative updates from preview releases as listed:
   * [August 2024](#august-2024)
   * [May 2024](#may-2024)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "「What's New」ドキュメントの更新"
}
```

### Explanation
この変更は、「What's New」ドキュメントに対する小規模な更新を示しています。具体的には、新しいAPIである「Delete analyze response」に関する情報が追加されました。このAPIは、分析結果が操作完了から24時間保存されることを説明し、迅速にその結果を削除する必要があるシナリオにおいて利用することができます。そのため、ユーザーは保管期間内に結果を取り扱う際の選択肢が増え、APIの利便性が向上します。さらに、v4.0 APIの累積的な更新に関する情報も追記されています。これにより、ユーザーは最新の機能や改善点を簡単に把握できるようになります。

## articles/ai-studio/how-to/develop/langchain.md{#item-0d59f1}

<details>
<summary>Diff</summary>
````diff
@@ -30,11 +30,7 @@ In this tutorial, you learn how to use the packages `langchain-azure-ai` to buil
 To run this tutorial, you need:
 
 * An [Azure subscription](https://azure.microsoft.com).
-* An Azure AI project as explained at [Create a project in Azure AI Foundry portal](../create-projects.md).
-* A model supporting the [Azure AI model inference API](https://aka.ms/azureai/modelinference) deployed. In this example, we use a `Mistral-Large` deployment, but use any model of your preference. 
-
-    * You can follow the instructions at [Deploy models as serverless APIs](../deploy-models-serverless.md).
-
+* A model deployment supporting the [Azure AI model inference API](https://aka.ms/azureai/modelinference) deployed. In this example, we use a `Mistral-Large-2407` deployment in the [Azure AI model inference](../../../ai-foundry/model-inference/overview.md).
 * Python 3.9 or later installed, including pip.
 * LangChain installed. You can do it with:
 
@@ -78,25 +74,13 @@ from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
 model = AzureAIChatCompletionsModel(
     endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
     credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
+    model="mistral-large-2407",
 )
 ```
 
 > [!TIP]
 > For Azure OpenAI models, configure the client as indicated at [Using Azure OpenAI models](#using-azure-openai-models).
 
-If your endpoint is serving more than one model, like with the [Azure AI model inference service](../../ai-services/model-inference.md) or [GitHub Models](https://github.com/marketplace/models), you have to indicate `model_name` parameter:
-
-```python
-import os
-from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
-
-model = AzureAIChatCompletionsModel(
-    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
-    credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
-    model_name="mistral-large-2407",
-)
-```
-
 You can use the following code to create the client if your endpoint supports Microsoft Entra ID:
 
 ```python
@@ -129,6 +113,18 @@ model = AzureAIChatCompletionsModel(
 )
 ```
 
+If your endpoint is serving one model, like with the Serverless API Endpoints, you don't have to indicate `model_name` parameter:
+
+```python
+import os
+from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
+
+model = AzureAIChatCompletionsModel(
+    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
+)
+```
+
 ## Use chat completions models
 
 Let's first use the model directly. `ChatModels` are instances of LangChain `Runnable`, which means they expose a standard interface for interacting with them. To simply call the model, we can pass in a list of messages to the `invoke` method.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "LangChain開発ガイドの改訂"
}
```

### Explanation
この変更は、「LangChain」の開発に関するガイドを改訂したものです。具体的には、いくつかの情報が追加および更新され、内容が整理されました。特に、モデルのデプロイメント関連の情報が改善され、「Mistral-Large」から「Mistral-Large-2407」の具体的なモデル名に更新されています。また、Azure AIモデル推論APIの利用に関する記述が明確化され、使用例も新しい形式に整えられています。この改訂により、ユーザーは最新の情報に基づいてLangChainを利用してモデルを操作する際の手順をより理解しやすくなります。具体的には、エンドポイントが単一モデルを提供する場合の「model_name」パラメータについての説明が追加されています。全体として、より一貫性のある情報が提供され、実際のコード例が具体化されたことにより、開発者にとっての有用性が増しています。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -147,6 +147,9 @@ Learn more about data processing for MaaS in the [article about data privacy](co
 
 :::image type="content" source="../media/explore/model-publisher-cycle.png" alt-text="Diagram that shows the model publisher service cycle." lightbox="../media/explore/model-publisher-cycle.png":::
 
+> [!NOTE]
+> Cloud Solution Provider (CSP) subscriptions do not have the ability to purchase serverless API deployments (MaaS) models.
+
 ### Billing
 
 The discovery, subscription, and consumption experience for models deployed via MaaS is in Azure AI Foundry portal and Azure Machine Learning studio. Users accept license terms for use of the models. Pricing information for consumption is provided during deployment.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルカタログ概要の更新"
}
```

### Explanation
この変更は、「モデルカタログ概要」に関する文書の小規模な更新を示しています。具体的には、Cloud Solution Provider (CSP) サブスクリプションに関する重要な注意事項が追加されました。この注意事項は、CSPサブスクリプションではサーバーレスAPIデプロイメント（MaaS）モデルを購入する能力がないことを明記しています。この情報の追加により、利用者は自分のサブスクリプション形態による制限をより明確に理解できるようになります。文書全体の内容は変更されておらず、既存の情報を補完する形で重要な注意が加えられています。この改訂により、正確な情報に基づく意思決定が促進されることが期待されます。


