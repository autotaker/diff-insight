---
date: '2025-07-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d3417cf...MicrosoftDocs:d3061a3
summary: この一連の変更では、ドキュメントインテリジェンスサービスに関するさまざまな領域が更新され、特に新機能の追加とサポート範囲の拡張が強調されています。新機能としては、`Document
  Intelligence v4.0 Read`コンテナの提供開始や検索可能なPDFへの対応が含まれています。破壊的変更はなく、ユーザーはドキュメントインテリジェンスサービスをより正確に理解し、最新機能を活用できるようになっています。バージョン`2024-11-30
  (GA)`では、リードモデルとレイアウトモデルのサポートが明示され、ユーザーは新機能をスムーズに取り入れることができるようになっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d3417cf...MicrosoftDocs:d3061a3){target="_blank"}

<format>
# ハイライト
この一連の変更では、ドキュメントインテリジェンスサービスのマークダウン要素、コンテナサポート、イメージタグ、インストール手順、新機能情報など、様々な領域における更新と修正が行われています。特に、バージョン`2024-11-30 (GA)`におけるサポート範囲の拡張や、新しい機能情報の追加が目立ちます。

## 新機能
- `Document Intelligence v4.0 Read`コンテナの提供開始の告知。
- 検索可能なPDFなどの新機能が強調。

## 破壊的変更
今回の変更には破壊的変更は含まれていません。

## その他の更新
- `markdown-elements.md`における図要素の取り扱いに関する注意事項の追加。
- `configuration.md`、`image-tags.md`、`install-run.md`で、ドキュメントインテリジェンスのモデルサポート情報の修正。
- 各種ファイルにおける、バージョン`2024-11-30 (GA)`がリードモデルとレイアウトモデルの両方をサポートすることの明示。

# 洞察
今回の変更は、ユーザーがドキュメントインテリジェンスサービスをより正確に理解し、最新の機能を最大限に活用できるように配慮された内容となっています。以下に、その詳しい解説を示します。

`markdown-elements.md`への変更では、特に図要素の取り扱いにおいて、文書としての分析が優先されることが強調されています。これにより、ユーザーはMarkdownで図を表示させることができないケースにおいても、他の方法で実行可能な手段を得ることが可能です。

`configuration.md`、`image-tags.md`、`install-run.md`の更新では、`2024-11-30 (GA)`バージョンのモデルサポートの誤解を解消し、ユーザーが確実に最新のモデルを使えるように修正されています。これにより、リードモデルとレイアウトモデル両方をサポートしていることが明示され、コンテナを利用したアプリケーションの柔軟性が向上しました。

最後に、`whats-new.md`での新機能紹介では、`Document Intelligence v4.0 Read`のリリースが告知されており、ユーザーから要望の高かった機能の早期利用が可能になる旨が説明されています。これにより、ユーザーは新機能をスムーズに取り入れることができ、また関連ドキュメントへのリンクが提供されていることで、詳細情報に迅速にアクセスできます。

これらの変更により、ドキュメントインテリジェンスを利用する開発者にとって、最新の機能や正確なコンテナサポート情報が提供され、スムーズなサービスの活用が可能となります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [markdown-elements.md](#item-ec4b62) | minor update | マークダウン要素に関する重要な注意事項の追加 | modified | 3 | 0 | 3 | 
| [configuration.md](#item-e17282) | minor update | ドキュメントインテリジェンスのコンテナサポートに関する情報の修正 | modified | 2 | 2 | 4 | 
| [image-tags.md](#item-6a7764) | minor update | ドキュメントインテリジェンスのイメージタグに関する情報の更新 | modified | 3 | 2 | 5 | 
| [install-run.md](#item-e32e11) | minor update | ドキュメントインテリジェンスのコンテナのインストールと実行に関する情報の更新 | modified | 3 | 3 | 6 | 
| [whats-new.md](#item-1ec8d3) | minor update | ドキュメントインテリジェンスの新機能に関する情報の追加 | modified | 8 | 1 | 9 | 


# Modified Contents
## articles/ai-services/document-intelligence/concept/markdown-elements.md{#item-ec4b62}

<details>
<summary>Diff</summary>
````diff
@@ -108,6 +108,9 @@ The Layout API preserves figure elements:
 * Preserves figure captions with the `<figcaption>` tag to provide important context
 * Preserves figure footnotes as separate paragraphs following the figure container
 
+> [!IMPORTANT]
+> In cases where we detect certain document components like section heading as part of the figures, markdown output will not present figures in the output and use the information for document structure analysis. For these cases, enumerate the figures field in JSON to retrieve all the figures.
+
 Here's an example:
 
 ``` md 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マークダウン要素に関する重要な注意事項の追加"
}
```

### Explanation
この変更は、`markdown-elements.md`ファイルにおいて、新しい重要な注意事項を追加したものです。具体的には、図要素を扱うレイアウトAPIに関する情報が強調されています。追加された内容では、特定の文書コンポーネントが図として検出された場合、マークダウン出力において図が表示されず、文書構造分析に使用されることが説明されています。そのため、すべての図を取得するには、JSONで図フィールドを列挙する必要があることが示されています。この更新により、ユーザーは図の扱いに関する重要な情報を得ることができ、使い方に対する理解が深まります。

## articles/ai-services/document-intelligence/containers/configuration.md{#item-e17282}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.author: lajanuar
 
 :::moniker range="doc-intel-2.1.0"
 
-Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models, `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt, and ID Document models, and `2024-11-30 (GA)` for Layout model:
+Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models, `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt, and ID Document models, and `2024-11-30 (GA)` for Read and Layout model:
 
 * [REST API `2022-08-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
 * [REST API `2023-07-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.1%20(2023-07-31)&tabs=HTTP&preserve-view=true)
@@ -38,7 +38,7 @@ With Document Intelligence containers, you can build an application architecture
 
 > [!IMPORTANT]
 >
-> Document Intelligence v4.0 container is currently available for Layout model only.
+> Document Intelligence v4.0 container is currently available for Read and Layout model only.
 
 ## Configuration settings
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのコンテナサポートに関する情報の修正"
}
```

### Explanation
この変更は、`configuration.md`ファイルにおいて、ドキュメントインテリジェンスのコンテナサポートに関する情報の一部を修正したものです。具体的には、コンテナがサポートするドキュメントインテリジェンスのモデルのバージョンについての説明が更新されました。以前は、バージョン`2024-11-30 (GA)`がレイアウトモデルのみにサポートされていると記載されていましたが、これがリードモデルとレイアウトモデルの両方に変更されました。また、重要な注意事項においても、バージョン4.0のコンテナは現在リードモデルとレイアウトモデルのみに適用されることが明記されています。この修正は、ユーザーにとって最新の情報を提供し、コンテナの利用に関する理解を助けるものです。

## articles/ai-services/document-intelligence/containers/image-tags.md{#item-6a7764}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.author: lajanuar
 
 :::moniker range="doc-intel-2.1.0"
 
-Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models, `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt, and ID Document models, and `2024-11-30 (GA)` for Layout model:
+Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models, `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt, and ID Document models, and `2024-11-30 (GA)` for Read and Layout model:
 
 * [REST API `2022-08-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
 * [REST API `2023-07-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.1%20(2023-07-31)&tabs=HTTP&preserve-view=true)
@@ -81,11 +81,12 @@ The following containers support DocumentIntelligence v3.1 models and features:
 
 Document Intelligence container images can be found within the [**Microsoft Artifact Registry** (also know as Microsoft Container Registry(MCR))](https://mcr.microsoft.com/catalog?search=document%20intelligence), the primary registry for all Microsoft published container images.
 
-The following containers support DocumentIntelligence v3.1 models and features:
+The following containers support Document Intelligence v4.0 models and features:
 
 | Container name |image |
 |---|---|
 | [**Layout 4.0**](https://mcr.microsoft.com/en-us/product/azure-cognitive-services/form-recognizer/layout-4.0/tags) |`mcr.microsoft.com/azure-cognitive-services/form-recognizer/layout-4.0:latest`|
+| [**Read 4.0**](https://mcr.microsoft.com/product/azure-cognitive-services/form-recognizer/read-4.0/tags) |`mcr.microsoft.com/azure-cognitive-services/form-recognizer/read-4.0:latest`|
 ::: moniker-end
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのイメージタグに関する情報の更新"
}
```

### Explanation
この変更は、`image-tags.md`ファイルにおいて、ドキュメントインテリジェンスのコンテナイメージに関する情報を更新したものです。具体的には、ドキュメントインテリジェンスのバージョンごとのサポート情報が修正され、バージョン`2024-11-30 (GA)`がレイアウトモデルからリードモデルとレイアウトモデルの両方に変更されました。また、ドキュメントインテリジェンスv4.0モデルのサポートに関する情報が追加され、4.0バージョンのリードモデルのコンテナが明示されています。これにより、ユーザーは最新のコンテナのサポート状況を正確に把握できるようになります。加えて、Microsoftのアーティファクトレジストリに関する言及もあり、コンテナイメージを見つけるためのリソースが提供されています。

## articles/ai-services/document-intelligence/containers/install-run.md{#item-e32e11}

<details>
<summary>Diff</summary>
````diff
@@ -23,15 +23,15 @@ Azure AI Document Intelligence is an Azure AI service that lets you build automa
 
 In this article you can learn how to download, install, and run Document Intelligence containers. Containers enable you to run the Document Intelligence service in your own environment. Containers are great for specific security and data governance requirements.
 
-* **Layout** model is supported by Document Intelligence v4.0 containers.
+* **Read**, **Layout** model is supported by Document Intelligence v4.0 containers.
 
 * **Read**, **Layout**,  **ID Document**,  **Receipt**, and **Invoice**  models are supported by Document Intelligence v3.1 containers.
 
 * **Read**, **Layout**, **General Document**, **Business Card**, and **Custom** models are supported by Document Intelligence v3.0 containers.
 
 ## Version support
 
-Support for containers is currently available with Document Intelligence version `v3.0: 2022-08-31 (GA)` for all models, `v3.1 2023-07-31 (GA)` for Read, Layout, ID Document, Receipt, and Invoice models, and `v4.0 2024-11-30 (GA)` for Layout:
+Support for containers is currently available with Document Intelligence version `v3.0: 2022-08-31 (GA)` for all models, `v3.1 2023-07-31 (GA)` for Read, Layout, ID Document, Receipt, and Invoice models, and `v4.0 2024-11-30 (GA)` for Read and Layout:
 
 * [REST API `v3.0: 2022-08-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
 * [REST API `v3.1: 2023-07-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.1%20(2023-07-31)&tabs=HTTP&preserve-view=true)
@@ -171,7 +171,7 @@ version: "3.9"
 services:
   azure-form-recognizer-read:
     container_name: azure-form-recognizer-read
-    image: mcr.microsoft.com/azure-cognitive-services/form-recognizer/read-3.1
+    image: mcr.microsoft.com/azure-cognitive-services/form-recognizer/read-4.0
     environment:
       - EULA=accept
       - billing={FORM_RECOGNIZER_ENDPOINT_URI}
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのコンテナのインストールと実行に関する情報の更新"
}
```

### Explanation
この変更は、`install-run.md`ファイルにおいて、ドキュメントインテリジェンスのコンテナに関するインストールと実行の手順を更新したものです。特に、バージョン4.0のコンテナがサポートするモデルが更新され、レイアウトモデルだけでなく、リードモデルもサポートされることが明示されています。また、バージョン情報も更新され、コンテナのサポートが`v4.0 2024-11-30 (GA)`においてリードモデルとレイアウトモデルの両方に適用されることが示されています。さらに、Docker設定の例では、リードモデルのイメージも`read-4.0`に変更されており、ユーザーは最新のコンテナバージョンを利用できるようになります。これにより、チュートリアルが最新のサービス仕様に適合していることが確保されています。

## articles/ai-services/document-intelligence/whats-new.md{#item-1ec8d3}

<details>
<summary>Diff</summary>
````diff
@@ -27,8 +27,15 @@ Document Intelligence service is updated on an ongoing basis. Bookmark this page
 > [!IMPORTANT]
 > Preview API versions are retired once the GA API is released. The 2023-02-28-preview API version is retiring. If you're still using the preview API or the associated SDK versions, update your code to target the latest API version `2024-11-30 (GA)`. </br>
 
+## June 2025
+**Document Intelligence v4.0 Read container is now available!**
+<br>
+This container image includes highly requested Read features like searchable PDF! For more information, *see:*
+* [Install and run containers](containers/install-run.md?view=doc-intel-4.0.0&preserve-view=true)
+* [Container image tags](containers/image-tags.md?view=doc-intel-4.0.0&preserve-view=true)
+
 ## April 2025
-**Document Intelligence v4.0 container is now available! Currently, Layout model is the only supported model for v4.0 release.**
+**Document Intelligence v4.0 Layout container is now available!**
 <br>
 For more information, *see:*
 * [Install and run containers](containers/install-run.md?view=doc-intel-4.0.0&preserve-view=true)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスの新機能に関する情報の追加"
}
```

### Explanation
この変更は、`whats-new.md`ファイルにおいて、ドキュメントインテリジェンスの新機能に関する情報を追加したものです。具体的には、2025年6月に新たに登場する`Document Intelligence v4.0 Read`コンテナの提供開始が告知されています。この新しいコンテナには、ユーザーからのリクエストが多かった検索可能なPDFなどの新機能が含まれていることが強調されています。さらに、関連するドキュメントへのリンクも追加されており、コンテナのインストールやイメージタグに関する詳細情報を参照できるようになっています。また、2025年4月に登場した`Document Intelligence v4.0 Layout`コンテナについても言及され、そのサポート内容が明確にされています。これにより、ユーザーは最新の機能やリリース情報を把握しやすくなります。


