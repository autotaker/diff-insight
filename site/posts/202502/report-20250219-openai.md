---
date: '2025-02-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:17e9068...MicrosoftDocs:f9aa01e
summary: このドキュメントは、Azure OpenAIサービスに関連するさまざまな要素に関する情報を改善・明確化するための小さな更新を多数含んでいます。具体的には、`o1-mini`モデルのグローバル標準デプロイメントの明記、地域別に整理されたモデルサポート情報、カスタムモデルデプロイメント名に関する変更が行われています。特に大きな破壊的変更はありませんが、ユーザーは新しい設定に対応する必要があります。また、最新の視覚的情報や改善された設定手順により、ユーザーはAPIやモデルの利用をより効果的に進めることができるようになります。この更新全体は、ユーザーエクスペリエンスの向上を目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:17e9068...MicrosoftDocs:f9aa01e){target="_blank"}

# Highlights
このドキュメントの変更には数多くの小さな更新が含まれており、それらはAzure OpenAIサービスに関連する様々な要素に関する情報を改善し、明確化しています。

## New features
- `o1-mini`モデルのグローバル標準デプロイメントがデフォルトで利用可能であることの明記。
- Azure OpenAI On Your Dataでのモデルのサポート情報が地域別に再配置され、より明確化。
- API設定におけるカスタムモデルデプロイメント名の使用に関する変更。

## Breaking changes
特に大きな破壊的変更はありませんが、ユーザーは更新された設定に対応する必要があります。

## Other updates
- 画像の更新により、データ取り込みアーキテクチャに関する最新の視覚的情報が提供されています。
- 設定手順やアクセスガイドラインの改善により、ユーザーはAPIやモデルの利用をより効果的に進めることができます。

# Insights
Azure OpenAIサービスに関するこの一連の更新は、主にサービス利用者が最新のモデルや機能にアクセスする際の体験を向上させるためのものでした。たとえば、`o1-mini`モデルに関する情報の強化は、利用者がどのモデルをどのように利用できるかをよりプロアクティブに理解できるようにするためのものです。

さらに、Azure OpenAI On Your Dataのサポートモデルに関する情報の整理は、利用可能なモデルに関する理解を助けるためのものであり、特定のモデルに対してのアクセス制約について利用者に先手を打たせるものです。このような調整により、ユーザーはより自己管理がしやすい情報をもとに、サービスを最大限に活用できる環境が整っています。

また、コードインタープリタやデータ構成に関する設定の変更は、特定のAPIやデプロイメントでの柔軟な利用を促進し、よりユーザー指向のアプローチを反映しています。このような柔軟性の向上は、Azure OpenAIサービス全体の利用者体験をさらに向上させる鍵となるでしょう。

最後に、ドキュメント中の画像更新は、視覚的な理解を高め、ユーザーが複雑なアーキテクチャやプロセスをより容易に把握できるようにするために重要です。このように、視覚と文章双方の面からユーザーエクスペリエンスの改善を図る動きが見られます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | AIモデルに関する情報の更新 | modified | 16 | 4 | 20 | 
| [use-your-data.md](#item-455d6e) | minor update | Azure OpenAI On Your Dataモデルのサポートに関する更新 | modified | 5 | 5 | 10 | 
| [code-interpreter.md](#item-95efbd) | minor update | コードインタープリタの設定の更新 | modified | 4 | 3 | 7 | 
| [on-your-data-configuration.md](#item-4875d3) | minor update | データ構成に関する手順の一部修正 | modified | 4 | 12 | 16 | 
| [reasoning.md](#item-a54b2f) | minor update | モデルのアクセス要件に関する情報の修正 | modified | 2 | 2 | 4 | 
| [ingestion-architecture.png](#item-fe4cf1) | minor update | データ取り込みアーキテクチャの画像更新 | modified | 0 | 0 | 0 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ The Azure OpenAI o<sup>&#42;</sup> series models are specifically designed to ta
 | `o3-mini` (2025-01-31) | The latest reasoning model, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text-only processing <br> - Functions/Tools <br> <br> **Request access: [limited access model application](https://aka.ms/OAI/o1access)** | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
 | `o1` (2024-12-17) | The most capable model in the o1 series, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools <br> <br> **Request access: [limited access model application](https://aka.ms/OAI/o1access)** | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
 |`o1-preview` (2024-09-12) | Older preview version | Input: 128,000  <br> Output: 32,768 | Oct 2023 |
-| `o1-mini` (2024-09-12) | A faster and more cost-efficient option in the o1 series, ideal for coding tasks requiring speed and lower resource consumption. <br> Global standard deployment available by default <br> For standard deployments, **Request access: [limited access model application](https://aka.ms/OAI/o1access)**  | Input: 128,000  <br> Output: 65,536 | Oct 2023 |
+| `o1-mini` (2024-09-12) | A faster and more cost-efficient option in the o1 series, ideal for coding tasks requiring speed and lower resource consumption. <br><br> Global standard deployment available by default. <br> <br> Standard (regional) deployments are currently only available for select customers who received access as part of the `o1-preview` limited access release.  | Input: 128,000  <br> Output: 65,536 | Oct 2023 |
 
 ### Availability
 
@@ -55,7 +55,7 @@ To learn more about the advanced `o-series` models see, [getting started with re
 |---|---|
 |`o3-mini` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
 |`o1` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
-| `o1-preview` | See the [models table](#model-summary-table-and-region-availability). |
+| `o1-preview` | See the [models table](#model-summary-table-and-region-availability). This model is only available for customers who were granted access as part of the original limited access release. |
 | `o1-mini` | See the [models table](#model-summary-table-and-region-availability). |
 
 ## GPT-4o audio
@@ -221,6 +221,11 @@ All deployments can perform the exact same inference operations, however the bil
 
 [!INCLUDE [Standard Global](../includes/model-matrix/standard-global.md)]
 
+> [!NOTE]
+> **Most o-series models are limited access**. Request access: [limited access model application](https://aka.ms/OAI/o1access). `o1-mini` is currently available to all customers for global standard deployment.
+>
+> Select customers were granted standard (regional) deployment access to `o1-mini` as part of the `o1-preview` limited access release. At this time access to `o1-mini` standard (regional) deployments is not being expanded.
+
 # [Global Provisioned Managed](#tab/global-ptum)
 
 ### Global provisioned managed model availability
@@ -257,7 +262,11 @@ All deployments can perform the exact same inference operations, however the bil
 
 [!INCLUDE [Standard Models](../includes/model-matrix/standard-models.md)]
 
-**o-series models require registration for standard deployments**. Request access: [limited access model application](https://aka.ms/OAI/o1access)
+> [!NOTE]
+> **Most o-series models are limited access**. Request access: [limited access model application](https://aka.ms/OAI/o1access). `o1-mini` is currently available to all customers for global standard deployment.
+>
+> Select customers were granted standard (regional) deployment access to `o1-mini` as part of the `o1-preview` limited access release. At this time access to `o1-mini` standard (regional) deployments is not being expanded.
+
 
 # [Provisioned Managed](#tab/provisioned)
 
@@ -282,7 +291,10 @@ This table doesn't include fine-tuning regional availability information.  Consu
 
 [!INCLUDE [Chat Completions](../includes/model-matrix/standard-chat-completions.md)]
 
-**o-series models require registration for standard deployments**. Request access: [limited access model application](https://aka.ms/OAI/o1access)
+> [!NOTE]
+> **Most o-series models are limited access**. Request access: [limited access model application](https://aka.ms/OAI/o1access). `o1-mini` is currently available to all customers for global standard deployment.
+>
+> Select customers were granted standard (regional) deployment access to `o1-mini` as part of the `o1-preview` limited access release. At this time access to `o1-mini` standard (regional) deployments is not being expanded.
 
 ### GPT-4 and GPT-4 Turbo model availability
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIモデルに関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連する文書の更新を反映しています。特に、AIモデルの説明において、`o1-mini`モデルに関する情報が強化され、標準デプロイメントの利用可能性やアクセスに関する詳細が追加されました。

具体的には、`o1-mini`モデルの説明において、グローバル標準デプロイメントはデフォルトで利用可能であること、ならびに特定の顧客に対して提供された標準（地域）デプロイメントへのアクセスについて言及しています。また、他のモデル（`o1-preview`など）へのアクセス制限に関する注意事項が新たに追加され、限定アクセスモデルアプリケーションへのリンクも強調されています。

全体として、これらの改訂は、モデルの可用性とアクセスに関する明確な情報を提供することを目的としており、ユーザーが利用可能なオプションについてより良い理解を得るのを助けます。

## articles/ai-services/openai/concepts/use-your-data.md{#item-455d6e}

<details>
<summary>Diff</summary>
````diff
@@ -41,11 +41,6 @@ Typically, the development process you'd use with Azure OpenAI On Your Data is:
 
 To get started, [connect your data source](../use-your-data-quickstart.md) using Azure AI Foundry portal and start asking questions and chatting on your data.
 
-> [!NOTE]
-> The following models are not supported by Azure OpenAI On Your Data:
-> * o1 models
-> * o3 models
-
 ## Azure Role-based access controls (Azure RBAC) for adding data sources
 
 To use Azure OpenAI On Your Data fully, you need to set one or more Azure RBAC roles. See [Azure OpenAI On Your Data configuration](../how-to/on-your-data-configuration.md#role-assignments) for more information.
@@ -719,6 +714,11 @@ Each user message can translate to multiple search queries, all of which get sen
 
 ## Regional availability and model support
 
+> [!NOTE]
+> The following models are not supported by Azure OpenAI On Your Data:
+> * o1 models
+> * o3 models
+
 | Region | `gpt-35-turbo-16k (0613)` | `gpt-35-turbo (1106)` | `gpt-4-32k (0613)` | `gpt-4 (1106-preview)` | `gpt-4 (0125-preview)` | `gpt-4 (0613)`  | `gpt-4o`\*\* | `gpt-4 (turbo-2024-04-09)` |
 |------|---|---|---|---|---|----|----|----|
 | Australia East | ✅ | ✅ | ✅ |✅ |   | ✅ | | | 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI On Your Dataモデルのサポートに関する更新"
}
```

### Explanation
この変更は、Azure OpenAI On Your Dataにおけるサポート対象モデルに関する情報を更新しています。主な変更点は、モデルのサポートに関する注意事項が文書内の異なる箇所に再配置されたことです。

具体的には、元々は「データを使用する方法」セクションの中にあった注意書きが、地域別の可用性とモデルサポートに関するセクションに移動しました。この更新により、Azure OpenAI On Your Dataではサポートされないモデル（o1モデルおよびo3モデル）に関する情報がより明確に強調された形になります。

また、文書内での表現や形式が調整され、関連情報が一貫して提供されるようになっています。この変更は、ユーザーが利用可能なモデルをより明確に理解できるようにするためのものであり、Azure OpenAIサービスを使用する際のプロセスに関する理解を助けることを意図しています。

## articles/ai-services/openai/how-to/code-interpreter.md{#item-95efbd}

<details>
<summary>Diff</summary>
````diff
@@ -164,9 +164,10 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/assistants?api-version=2
     "tools": [
       { "type": "code_interpreter" }
     ],
-    "model": "gpt-4-1106-preview",
-    "tool_resources"{
-      "code interpreter": {
+    "name": "Assistants playground",
+    "model": "Replace it with your-custom-model-deployment-name",
+    "tool_resources":{
+      "code_interpreter": {
           "file_ids": ["assistant-1234"]
       }
     }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コードインタープリタの設定の更新"
}
```

### Explanation
この変更は、Azure OpenAIにおけるコードインタープリタの設定手順に関する更新を反映しています。具体的には、API呼び出しの設定内容が更新され、具体的なモデル名の指定方法が変更されています。

主な変更点として、以下の点が挙げられます：
- モデル名が具体的なバージョン（"gpt-4-1106-preview"）から、カスタムモデルデプロイメント名を指定する形式（"Replace it with your-custom-model-deployment-name"）に変更されています。これにより、ユーザーは自身のデプロイメントに合わせた設定を行いやすくなっています。
- コードインタープリタの設定において、名前が"Assistants playground"に変更されている点も重要です。
- また、ツールリソースに関する設定が整理され、コードインタープリタに必要なファイルIDの指定方法が明確化されています。

このような変更は、ユーザーがより柔軟にカスタム設定を行うことを促進し、Azure OpenAIサービスの利用をシンプルにすることを目的としています。

## articles/ai-services/openai/how-to/on-your-data-configuration.md{#item-4875d3}

<details>
<summary>Diff</summary>
````diff
@@ -29,16 +29,8 @@ When you use Azure OpenAI On Your Data to ingest data from Azure blob storage, l
 
 * Steps 1 and 2 are only used for file upload.
 * Downloading URLs to your blob storage is not illustrated in this diagram. After web pages are downloaded from the internet and uploaded to blob storage, steps 3 onward are the same.
-* Two indexers, two indexes, two data sources and a [custom skill](/azure/search/cognitive-search-custom-skill-interface) are created in the Azure AI Search resource.
-* The chunks container is created in the blob storage.
-* If the schedule triggers the ingestion, the ingestion process starts from step 7.
-*  Azure OpenAI's `preprocessing-jobs` API implements the [Azure AI Search customer skill web API protocol](/azure/search/cognitive-search-custom-skill-web-api), and processes the documents in a queue. 
-* Azure OpenAI:
-    1. Internally uses the first indexer created earlier to crack the documents.
-    1. Uses a heuristic-based algorithm to perform chunking. It honors table layouts and other formatting elements in the chunk boundary to ensure the best chunking quality.
-    1. If you choose to enable vector search, Azure OpenAI uses the selected embedding setting to vectorize the chunks.
-* When all the data that the service is monitoring are processed, Azure OpenAI triggers the second indexer.
-* The indexer stores the processed data into an Azure AI Search service.
+* One indexer, one index, and one data source in the Azure AI Search resource is created using prebuilt skills and [integrated vectorization](/azure/search/vector-search-integrated-vectorization.md).
+* Azure AI Search handles the extraction, chunking, and vectorization of chunked documents through integrated vectorization. If a scheduling interval is specified, the indexer will run accordingly. 
 
 For the managed identities used in service calls, only system assigned managed identities are supported. User assigned managed identities aren't supported.
 
@@ -167,7 +159,7 @@ To set the managed identities via the management API, see [the management API re
 
 ### Enable trusted service
 
-To allow your Azure AI Search to call your Azure OpenAI `preprocessing-jobs` as custom skill web API, while Azure OpenAI has no public network access, you need to set up Azure OpenAI to bypass Azure AI Search as a trusted service based on managed identity. Azure OpenAI identifies the traffic from your Azure AI Search by verifying the claims in the JSON Web Token (JWT). Azure AI Search must use the system assigned managed identity authentication to call the custom skill web API. 
+To allow your Azure AI Search to call your Azure OpenAI `embedding model, while Azure OpenAI has no public network access, you need to set up Azure OpenAI to bypass Azure AI Search as a trusted service based on managed identity. Azure OpenAI identifies the traffic from your Azure AI Search by verifying the claims in the JSON Web Token (JWT). Azure AI Search must use the system assigned managed identity authentication to call the embedding endpoint. 
 
 Set `networkAcls.bypass` as `AzureServices` from the management API. For more information, see [Virtual networks article](/azure/ai-services/cognitive-services-virtual-networks?tabs=portal#grant-access-to-trusted-azure-services-for-azure-openai).
 
@@ -268,7 +260,7 @@ So far you have already setup each resource work independently. Next you need to
 | `Search Index Data Reader` | Azure OpenAI | Azure AI Search | Inference service queries the data from the index. |
 | `Search Service Contributor` | Azure OpenAI | Azure AI Search | Inference service queries the index schema for auto fields mapping. Data ingestion service creates index, data sources, skill set, indexer, and queries the indexer status. |
 | `Storage Blob Data Contributor` | Azure OpenAI | Storage Account | Reads from the input container, and writes the preprocessed result to the output container. |
-| `Cognitive Services OpenAI Contributor` | Azure AI Search | Azure OpenAI | Custom skill. |
+| `Cognitive Services OpenAI Contributor` | Azure AI Search | Azure OpenAI | to allow the Azure AI Search resource access to the Azure OpenAI embedding endpoint. |
 | `Storage Blob Data Reader` | Azure AI Search | Storage Account | Reads document blobs and chunk blobs. |
 | `Reader` | Azure AI Foundry Project | Azure Storage Private Endpoints (Blob & File) | Read search indexes created in blob storage within an Azure AI Foundry Project. |
 | `Cognitive Services OpenAI User` | Web app | Azure OpenAI | Inference. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ構成に関する手順の一部修正"
}
```

### Explanation
この変更は、Azure OpenAI On Your Dataのデータ構成手順に関する情報を更新しています。主に、インデクサーやデータソースの設定、そのプロセスの詳細について簡素化された表現が見られます。

具体的には、以下のような点が修正されています：
- 複数のインデクサー、インデックス、データソースに関する情報が一つのインデクサー、インデックス、データソースに統合され、プロセスが簡略化されています。これにより、ユーザーは設定手順をより理解しやすくなっています。
- 文章中における「新たに使用されるスキル」や「統合ベクトル化」の説明が追加され、ユーザーがドキュメント内の専用の手法や技術をより理解できるようになっています。
- セクションの最後にあたるアクセス権限に関する記述も更新され、Azure OpenAIとAzure AI Searchの間でのアクセス許可が明確化されています。

この変更は、ユーザーが自分のデータの取り扱いをより簡単に行えるようにし、設定プロセスの理解を深めることを目的としていると言えます。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -36,8 +36,8 @@ Request access: [limited access model application](https://aka.ms/OAI/o1access)
 |---|---|---|
 | `o3-mini` | East US2 (Global Standard) <br> Sweden Central (Global Standard) | [Limited access model application](https://aka.ms/OAI/o1access) |
 |`o1` | East US2 (Global Standard) <br> Sweden Central (Global Standard) | [Limited access model application](https://aka.ms/OAI/o1access) |
-| `o1-preview` | See [models page](../concepts/models.md#global-standard-model-availability). | [Limited access model application](https://aka.ms/OAI/o1access) |
-| `o1-mini` | See [models page](../concepts/models.md#global-standard-model-availability). | No access request needed for Global Standard deployments<br>Standard (regional) deployments require: [Limited access model application](https://aka.ms/OAI/o1access) |
+| `o1-preview` | See [models page](../concepts/models.md#global-standard-model-availability). |This model is only available for customers who were granted access as part of the original limited access release. We're currently not expanding access to `o1-preview`. |
+| `o1-mini` | See [models page](../concepts/models.md#global-standard-model-availability). | No access request needed for Global Standard deployments.<br><br>Standard (regional) deployments are currently only available to select customers who were previously granted access as part of the `o1-preview` release.|
 
 ## API & feature support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのアクセス要件に関する情報の修正"
}
```

### Explanation
この変更は、Azure OpenAIのモデルのアクセス要件に関する情報を更新しています。特に、`o1-preview`および`o1-mini`モデルの利用可能性とアクセス条件についての説明が改善されています。

具体的には、以下の点が修正されています：
- `o1-preview`モデルに関する説明が明確化され、このモデルへのアクセスは、最初の限定アクセスリリースの一環としてアクセスが付与された顧客にのみ提供されることが強調されています。現在、新しいユーザーへのアクセスの拡大は行われていないとのことです。
- `o1-mini`モデルについても、グローバルスタンダードデプロイメントに対してはアクセス要求が不要であることが記載され、さらにスタンダード（地域的）デプロイメントについては、`o1-preview`リリースの一環として事前にアクセスが付与された選択された顧客にのみ提供されることが明示されています。

この変更は、ユーザーがモデルへのアクセス要件をより正確に理解できるようにし、明確なガイダンスを提供することを目的としています。

## articles/ai-services/openai/media/use-your-data/ingestion-architecture.png{#item-fe4cf1}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ取り込みアーキテクチャの画像更新"
}
```

### Explanation
この変更は、Azure OpenAIのデータ取り込みアーキテクチャに関する画像（ingestion-architecture.png）を更新したことを示しています。具体的な内容の追加や削除はなく、画像自体の内容や見た目が修正されている可能性があります。これにより、ユーザーは最新の情報に基づいた視覚的理解を得られるように設計されています。

画像の更新は、ドキュメントの視覚的な一貫性や最新性を保つために重要であり、ユーザーが設定やアーキテクチャの理解を深める助けとなる役割を果たします。詳細な内容の変更は記載されていないため、具体的な違いについては画像を直接確認する必要があります。


