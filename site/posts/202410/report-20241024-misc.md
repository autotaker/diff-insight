---
date: '2024-10-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6f58d1b...MicrosoftDocs:f8a58ce
summary: この変更では、Azure AIサービスに関連する文書が更新され、新しい機能の追加や用語の改善が行われました。Ministral AIファミリーに新たにMinistral
  3Bモデルが追加され、地域可用性が明確化されました。また、Cohere Embedモデルがマルチモーダル対応になり、機能が向上しました。しかし、カスタム感情分析およびカスタムテキスト分析（健康関連）は2025年1月10日に廃止されることが発表されました。他にも、Azure
  OpenAIモデルのリンクが新しい可用性情報に更新され、用語の一貫性を保つための表現が見直されています。全体として、これらの変更はユーザーがより正確かつ効率的にAzure
  AIサービスを利用できるようにすることを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6f58d1b...MicrosoftDocs:f8a58ce){target="_blank"}

# Highlights
この変更では、Azure AIサービスに関連する文書がいくつか更新されており、新しい機能の追加や用語の改善が行われています。また、モデルの可用性情報も最新化されています。

## New features
- Mistral AIファミリーにMinistral 3Bモデルが追加され、地域可用性も明確化されました。
- Cohere Embedモデルがマルチモーダル対応であることが強調され、機能が拡充されています。

## Breaking changes
- カスタム感情分析およびカスタムテキスト分析（健康関連）が2025年1月10日に廃止されることが明示されました。

## Other updates
- Azure OpenAIモデル関連のリンクが新しい可用性情報に更新され、関連情報が整理されています。
- 用語の一貫性を保つため、サポートされる言語の表現が変更されました。

# Insights
この差分に見られる主な変更点は、Azure AIサービスや関連モデルに関する情報のアップデートです。変更は、ユーザーがより正確かつ効率的にコンテンツを利用できるようにすることを目的としており、以下のような改良が加えられています。

まず、大きな焦点が当たっているのは、Ministral 3Bモデルの追加です。これは、特にエッジコンピューティングやリアルタイムアプリケーションにおけるモデル選択肢の強化であり、ユーザーがより適したモデルを選択できるようになります。また、このモデルの地域可用性が明確化されたことにより、モデル利用の地理的要件に合致した情報を容易に得ることが可能です。

一方、Cohere Embedモデルの更新においては、マルチモーダル対応が強調され、モデルがテキストだけでなく画像も処理できる能力が追記されています。特に、データURL形式での画像入力に対応していることが重要で、これに伴うトークン消費に関する詳細も記されています。これにより、使用方法やコスト理解が深まる効果があります。

さらに、カスタム感情分析およびカスタムテキスト分析の廃止が予告されており、ユーザーは事前に移行計画を立てる必要があります。エコシステムの変更が発生するため、代替サービスへの移行が推奨されています。

また、他の文書の更新では、用語の統一やリンクの修正が強調されており、情報の一貫性とアクセスのしやすさが向上しています。これにより、ユーザーは必要なドキュメントを効率よく検索し、利用することができます。

全体として、これらの修正は、ユーザーが最適なAzure AIサービスを利用するための情報提供の改善に焦点を当てたものであり、サービスとドキュメントの品質向上に寄与するものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [toc.yml](#item-81aa7b) | minor update | ドキュメントインテリジェンスリンクの更新 | modified | 1 | 1 | 2 | 
| [entity-categories.md](#item-ba2623) | minor update | エンティティカテゴリの表現の改善 | modified | 13 | 14 | 27 | 
| [whats-new.md](#item-69b272) | minor update | 2024年9月のアップデート内容の追加 | modified | 3 | 1 | 4 | 
| [deploy-models-cohere-embed.md](#item-eab662) | minor update | Cohere Embedモデルのマルチモーダル対応の更新 | modified | 27 | 14 | 41 | 
| [deploy-models-mistral.md](#item-487a41) | minor update | Ministral 3Bモデルの追加 | modified | 59 | 3 | 62 | 
| [model-catalog-overview.md](#item-278001) | minor update | Mistralファミリーモデルの更新 | modified | 1 | 1 | 2 | 
| [region-availability-maas.md](#item-35d79c) | minor update | Ministral-3Bの地域可用性の追加 | modified | 1 | 0 | 1 | 
| [region-support.md](#item-d402e1) | minor update | Azure OpenAIモデルの可用性情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/toc.yml{#item-81aa7b}

<details>
<summary>Diff</summary>
````diff
@@ -327,7 +327,7 @@ items:
     - name: Bank statement
       href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/bank-statement.md
     - name: Business card (2023-07-31 GA)
-      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2023-07-31/business-card.md
+      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2023-07-31-ga/business-card.md
     - name: Contract
       href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/contract.md
     - name: Credit card
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスリンクの更新"
}
```

### Explanation
このコードの変更は、`toc.yml`ファイル内のリンクの1つを更新するマイナーな修正です。具体的には、ビジネスカードに関連するリンクのパスが変更されました。元のリンクは`/schema/2023-07-31/business-card.md`であったのに対し、更新後のリンクは`/schema/2023-07-31-ga/business-card.md`となっています。この変更は、コンテンツの整理や、バージョン管理の明確化を目的としています。全体で1行追加され、1行削除され、2行の変更が行われました。この修正により、ユーザーが正確なリソースにアクセス可能になります。

## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories.md{#item-ba2623}

<details>
<summary>Diff</summary>
````diff
@@ -23,7 +23,6 @@ The PII feature includes the ability to detect personal (`PII`) and health (`PHI
 > [!NOTE]
 > To detect protected health information (PHI), use the `domain=phi` parameter and model version `2020-04-01` or later.
 
-
 The following entity categories are returned when you're sending API requests PII feature.
 
 ## Category: Person
@@ -47,7 +46,7 @@ This category contains the following entity:
     :::column-end:::
     
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`   
       
@@ -76,7 +75,7 @@ This category contains the following entity:
     :::column-end:::
 
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`  
       
@@ -104,7 +103,7 @@ This category contains the following entity:
     :::column-end:::
 
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt` `pt-br`
       
@@ -134,7 +133,7 @@ This category contains the following entity:
     :::column-end:::
 
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`  
       
@@ -163,7 +162,7 @@ The entity in this category can have the following subcategories.
     :::column-end:::
 
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
       `en`   
       
@@ -235,7 +234,7 @@ This category contains the following entity:
     :::column-end:::
 
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
       
@@ -263,7 +262,7 @@ This category contains the following entity:
 
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
       
@@ -292,7 +291,7 @@ This category contains the following entity:
     :::column-end:::
 
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
       
@@ -321,7 +320,7 @@ This category contains the following entity:
     :::column-end:::
 
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
       
@@ -348,7 +347,7 @@ This category contains the following entities:
       
     :::column-end:::
 :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
       
@@ -375,7 +374,7 @@ The entity in this category can have the following subcategories.
       
     :::column-end:::
     :::column span="2":::
-      **Supported document languages**
+      **Supported languages**
       
       `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`   
       
@@ -401,7 +400,7 @@ The PII service supports the Age subcategory within the broader Quantity categor
       
     :::column-end:::
     :::column span="2":::
-      **Supported document languages**
+      **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`   
       
@@ -428,7 +427,7 @@ These entity categories include identifiable Azure information like authenticati
       
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
       `en` 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティカテゴリの表現の改善"
}
```

### Explanation
このコードの変更は、`entity-categories.md`ファイルにおいて、個人情報（PII）サービスの関連情報を更新するためのマイナーな修正です。特に、「Supported document languages」という表現を「Supported languages」に変更し、より明確かつ一貫性のある用語に改善しています。この修正により、情報が整理され、ユーザーがサポートされている言語を理解しやすくなります。

具体的には、13行が追加され、14行が削除され、全体で27行の変更が行われました。これにより、同じ意味を示す情報の記述が整理され、文書の可読性が向上しました。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,9 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
 
 ## September 2024
 
-* Custom Summarization has been discontinued and is no longer available in the Studio and documentation.
+* PII detection now has container support. See more details in the Azure Update post: [Announcing Text PII Redaction Container Release](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/announcing-text-pii-redaction-container-release/ba-p/4264655).
+* Custom sentiment analysis (preview) will be retired on January 10th, 2025. Please transition to other custom model training services, such as custom text classification in Azure AI Language, by that date.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom sentiment analysis (preview) in Azure AI Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-sentiment-analysis-retirement).
+* Custom text analytics for health (preview) will be retired on January 10th, 2025. Please transition to other custom model training services, such as custom named entity recognition in Azure AI Language, by that date.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom text analytics for health (preview) in Azure AI Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-text-analytics-for-health-retirement).
 
 ## August 2024
 * [CLU utterance limit in a project](conversational-language-understanding/service-limits.md#data-limits) increased from 25,000 to 50,000.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "2024年9月のアップデート内容の追加"
}
```

### Explanation
このコードの変更は、`whats-new.md`ファイルに対するマイナーな修正で、Azure AI Languageに関する最新情報を追加するものです。具体的には、2024年9月のアップデートに3つの新しい項目が追加されました。

1. **PII検出のコンテナサポート**: 新たにPII検出がコンテナ対応となったことが記載されています。
2. **カスタム感情分析の廃止**: 2025年1月10日にカスタム感情分析（プレビュー版）が廃止されることについての通知と、代替のモデル訓練サービスへの移行の推奨が述べられています。
3. **カスタムテキスト分析の廃止**: 同じく2025年1月10日にカスタムテキスト分析（健康関連）の廃止がアナウンスされており、こちらも他のサービスへの移行が推奨されています。

この変更により、ユーザーが最新のサービス状況と移行計画を把握できるよう、重要な情報が強調され、4行の変更が実施されました。

## articles/ai-studio/how-to/deploy-models-cohere-embed.md{#item-eab662}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Cohere Embed V3 models with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 08/08/2024
+ms.date: 10/23/2024
 ms.reviewer: shubhiraj
 reviewer: shubhirajMsft
 ms.author: mopeakande
@@ -31,19 +31,24 @@ The Cohere family of models for embeddings includes the following models:
 
 # [Cohere Embed v3 - English](#tab/cohere-embed-v3-english)
 
-Cohere Embed English is a text representation model used for semantic search, retrieval-augmented generation (RAG), classification, and clustering. Embed English performs well on the HuggingFace (massive text embed) MTEB benchmark and on use-cases for various industries, such as Finance, Legal, and General-Purpose Corpora. Embed English also has the following attributes:
+Cohere Embed English is a multimodal (text and image) representation model used for semantic search, retrieval-augmented generation (RAG), classification, and clustering. Embed English performs well on the HuggingFace (massive text embed) MTEB benchmark and on use-cases for various industries, such as Finance, Legal, and General-Purpose Corpora. Embed English also has the following attributes:
 
-* Embed English has 1,024 dimensions.
+* Embed English has 1,024 dimensions
 * Context window of the model is 512 tokens
+* Embed English accepts images as a base64 encoded data url
 
+Image embeddings consume a fixed number of tokens per image—1,000 tokens per image—which translates to a price of $0.0001 per image embedded. The size or resolution of the image doesn't affect the number of tokens consumed, provided the image is within the accepted dimensions, file size, and formats.
+ 
 
 # [Cohere Embed v3 - Multilingual](#tab/cohere-embed-v3-multilingual)
 
-Cohere Embed Multilingual is a text representation model used for semantic search, retrieval-augmented generation (RAG), classification, and clustering. Embed Multilingual supports more than 100 languages and can be used to search within a language (for example, to search with a French query on French documents) and across languages (for example, to search with an English query on Chinese documents). Embed multilingual performs well on multilingual benchmarks such as Miracl. Embed Multilingual also has the following attributes:
+Cohere Embed Multilingual is a multimodal (text and image) representation model used for semantic search, retrieval-augmented generation (RAG), classification, and clustering. Embed Multilingual supports more than 100 languages and can be used to search within a language (for example, to search with a French query on French documents) and across languages (for example, to search with an English query on Chinese documents). Embed multilingual performs well on multilingual benchmarks such as Miracl. Embed Multilingual also has the following attributes:
 
-* Embed Multilingual has 1,024 dimensions.
+* Embed Multilingual has 1,024 dimensions
 * Context window of the model is 512 tokens
+* Embed Multilingual accepts images as a base64 encoded data url
 
+Image embeddings consume a fixed number of tokens per image—1,000 tokens per image—which translates to a price of $0.0001 per image embedded. The size or resolution of the image doesn't affect the number of tokens consumed, provided the image is within the accepted dimensions, file size, and formats.
 
 ---
 
@@ -220,19 +225,23 @@ The Cohere family of models for embeddings includes the following models:
 
 # [Cohere Embed v3 - English](#tab/cohere-embed-v3-english)
 
-Cohere Embed English is a text representation model used for semantic search, retrieval-augmented generation (RAG), classification, and clustering. Embed English performs well on the HuggingFace (massive text embed) MTEB benchmark and on use-cases for various industries, such as Finance, Legal, and General-Purpose Corpora. Embed English also has the following attributes:
+Cohere Embed English is a multimodal (text and image) representation model used for semantic search, retrieval-augmented generation (RAG), classification, and clustering. Embed English performs well on the HuggingFace (massive text embed) MTEB benchmark and on use-cases for various industries, such as Finance, Legal, and General-Purpose Corpora. Embed English also has the following attributes:
 
-* Embed English has 1,024 dimensions.
+* Embed English has 1,024 dimensions
 * Context window of the model is 512 tokens
+* Embed English accepts images as a base64 encoded data url
 
+Image embeddings consume a fixed number of tokens per image—1,000 tokens per image—which translates to a price of $0.0001 per image embedded. The size or resolution of the image doesn't affect the number of tokens consumed, provided the image is within the accepted dimensions, file size, and formats.
 
 # [Cohere Embed v3 - Multilingual](#tab/cohere-embed-v3-multilingual)
 
-Cohere Embed Multilingual is a text representation model used for semantic search, retrieval-augmented generation (RAG), classification, and clustering. Embed Multilingual supports more than 100 languages and can be used to search within a language (for example, to search with a French query on French documents) and across languages (for example, to search with an English query on Chinese documents). Embed multilingual performs well on multilingual benchmarks such as Miracl. Embed Multilingual also has the following attributes:
+Cohere Embed Multilingual is a multimodal (text and image) representation model used for semantic search, retrieval-augmented generation (RAG), classification, and clustering. Embed Multilingual supports more than 100 languages and can be used to search within a language (for example, to search with a French query on French documents) and across languages (for example, to search with an English query on Chinese documents). Embed multilingual performs well on multilingual benchmarks such as Miracl. Embed Multilingual also has the following attributes:
 
-* Embed Multilingual has 1,024 dimensions.
+* Embed Multilingual has 1,024 dimensions
 * Context window of the model is 512 tokens
+* Embed Multilingual accepts images as a base64 encoded data url
 
+Image embeddings consume a fixed number of tokens per image—1,000 tokens per image—which translates to a price of $0.0001 per image embedded. The size or resolution of the image doesn't affect the number of tokens consumed, provided the image is within the accepted dimensions, file size, and formats.
 
 ---
 
@@ -411,19 +420,23 @@ The Cohere family of models for embeddings includes the following models:
 
 # [Cohere Embed v3 - English](#tab/cohere-embed-v3-english)
 
-Cohere Embed English is a text representation model used for semantic search, retrieval-augmented generation (RAG), classification, and clustering. Embed English performs well on the HuggingFace (massive text embed) MTEB benchmark and on use-cases for various industries, such as Finance, Legal, and General-Purpose Corpora. Embed English also has the following attributes:
+Cohere Embed English is a multimodal (text and image) representation model used for semantic search, retrieval-augmented generation (RAG), classification, and clustering. Embed English performs well on the HuggingFace (massive text embed) MTEB benchmark and on use-cases for various industries, such as Finance, Legal, and General-Purpose Corpora. Embed English also has the following attributes:
 
-* Embed English has 1,024 dimensions.
+* Embed English has 1,024 dimensions
 * Context window of the model is 512 tokens
+* Embed English accepts images as a base64 encoded data url
 
+Image embeddings consume a fixed number of tokens per image—1,000 tokens per image—which translates to a price of $0.0001 per image embedded. The size or resolution of the image doesn't affect the number of tokens consumed, provided the image is within the accepted dimensions, file size, and formats.
 
 # [Cohere Embed v3 - Multilingual](#tab/cohere-embed-v3-multilingual)
 
-Cohere Embed Multilingual is a text representation model used for semantic search, retrieval-augmented generation (RAG), classification, and clustering. Embed Multilingual supports more than 100 languages and can be used to search within a language (for example, to search with a French query on French documents) and across languages (for example, to search with an English query on Chinese documents). Embed multilingual performs well on multilingual benchmarks such as Miracl. Embed Multilingual also has the following attributes:
+Cohere Embed Multilingual is a multimodal (text and image) representation model used for semantic search, retrieval-augmented generation (RAG), classification, and clustering. Embed Multilingual supports more than 100 languages and can be used to search within a language (for example, to search with a French query on French documents) and across languages (for example, to search with an English query on Chinese documents). Embed multilingual performs well on multilingual benchmarks such as Miracl. Embed Multilingual also has the following attributes:
 
-* Embed Multilingual has 1,024 dimensions.
+* Embed Multilingual has 1,024 dimensions
 * Context window of the model is 512 tokens
+* Embed Multilingual accepts images as a base64 encoded data url
 
+Image embeddings consume a fixed number of tokens per image—1,000 tokens per image—which translates to a price of $0.0001 per image embedded. The size or resolution of the image doesn't affect the number of tokens consumed, provided the image is within the accepted dimensions, file size, and formats.
 
 ---
 
@@ -653,4 +666,4 @@ Quota is managed per deployment. Each deployment has a rate limit of 200,000 tok
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cohere Embedモデルのマルチモーダル対応の更新"
}
```

### Explanation
このコードの変更は、`deploy-models-cohere-embed.md`ファイルに対するマイナーな修正で、Cohere Embedモデルの機能に関する情報を更新しています。具体的には、Cohere Embedモデルの説明が強化され、"テキスト表現モデル"から"マルチモーダル（テキストと画像）表現モデル"に変更されました。

変更点は次の通りです：

- **マルチモーダルの明確化**: 英語および多言語のCohere Embedモデル両方がマルチモーダル対応であることが強調され、テキストだけでなく画像も処理できることが記載されています。
- **画像の受け入れ形式**: EmbedモデルがBase64エンコードされたデータURL形式で画像を受け入れることに関する情報が追加されました。
- **トークン消費に関する詳細**: 画像埋め込みにおける固定トークン消費（1画像あたり1,000トークン、料金は$0.0001）の詳細が新たに盛り込まれています。

この更新により、ユーザーはCohere Embedモデルの最新の機能と適用方法を理解できるようになり、全体で41行の変更がありました。

## articles/ai-studio/how-to/deploy-models-mistral.md{#item-487a41}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Mistral premium chat models with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 09/13/2024
+ms.date: 10/23/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -19,7 +19,7 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 [!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn about Mistral premium chat models and how to use them.
-Mistral AI offers two categories of models. Premium models including [Mistral Large and Mistral Small](deploy-models-mistral.md), available as serverless APIs with pay-as-you-go token-based billing. Open models including [Mistral Nemo](deploy-models-mistral-nemo.md), [Mixtral-8x7B-Instruct-v01, Mixtral-8x7B-v01, Mistral-7B-Instruct-v01, and Mistral-7B-v01](deploy-models-mistral-open.md); available to also download and run on self-hosted managed endpoints.
+Mistral AI offers two categories of models. Premium models including [Mistral Large, Mistral Small, and Ministral 3B](deploy-models-mistral.md), available as serverless APIs with pay-as-you-go token-based billing. Open models including [Mistral Nemo](deploy-models-mistral-nemo.md), [Mixtral-8x7B-Instruct-v01, Mixtral-8x7B-v01, Mistral-7B-Instruct-v01, and Mistral-7B-v01](deploy-models-mistral-open.md); available to also download and run on self-hosted managed endpoints.
 
 [!INCLUDE [models-preview](../includes/models-preview.md)]
 
@@ -72,6 +72,20 @@ The following models are available:
 * [Mistral-Small](https://aka.ms/azureai/landing/Mistral-Small)
 
 
+# [Ministral 3B](#tab/ministral-3b)
+
+Ministral 3B is Mistral AI's Small Language Model (SLM) optimized for edge computing and on-device applications. The model is designed for low-latency and compute-efficient inference; therefore, it is perfect for standard GenAI applications that have real-time requirements and high-volume.
+       
+* **Input**: text only
+* **Output**: text only
+* **Number of parameters**: 3.6 billion
+
+
+The following models are available:
+
+* [Ministral-3B](https://aka.ms/azureai/landing/Ministral-3B)
+
+
 ---
 
 > [!TIP]
@@ -542,6 +556,20 @@ The following models are available:
 * [Mistral-Small](https://aka.ms/azureai/landing/Mistral-Small)
 
 
+# [Ministral 3B](#tab/ministral-3b)
+
+Ministral 3B is Mistral AI's Small Language Model (SLM) optimized for edge computing and on-device applications. The model is designed for low-latency and compute-efficient inference; therefore, it is perfect for standard GenAI applications that have real-time requirements and high-volume.
+       
+* **Input**: text only
+* **Output**: text only
+* **Number of parameters**: 3.6 billion
+
+
+The following models are available:
+
+* [Ministral-3B](https://aka.ms/azureai/landing/Ministral-3B)
+
+
 ---
 
 > [!TIP]
@@ -1031,6 +1059,20 @@ The following models are available:
 * [Mistral-Small](https://aka.ms/azureai/landing/Mistral-Small)
 
 
+# [Ministral 3B](#tab/ministral-3b)
+
+Ministral 3B is Mistral AI's Small Language Model (SLM) optimized for edge computing and on-device applications. The model is designed for low-latency and compute-efficient inference; therefore, it is perfect for standard GenAI applications that have real-time requirements and high-volume.
+       
+* **Input**: text only
+* **Output**: text only
+* **Number of parameters**: 3.6 billion
+
+
+The following models are available:
+
+* [Ministral-3B](https://aka.ms/azureai/landing/Ministral-3B)
+
+
 ---
 
 > [!TIP]
@@ -1542,6 +1584,20 @@ The following models are available:
 * [Mistral-Small](https://aka.ms/azureai/landing/Mistral-Small)
 
 
+# [Ministral 3B](#tab/ministral-3b)
+
+Ministral 3B is Mistral AI's Small Language Model (SLM) optimized for edge computing and on-device applications. The model is designed for low-latency and compute-efficient inference; therefore, it is perfect for standard GenAI applications that have real-time requirements and high-volume.
+       
+* **Input**: text only
+* **Output**: text only
+* **Number of parameters**: 3.6 billion
+
+
+The following models are available:
+
+* [Ministral-3B](https://aka.ms/azureai/landing/Ministral-3B)
+
+
 ---
 
 > [!TIP]
@@ -2091,7 +2147,7 @@ View the response from the model:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Ministral 3Bモデルの追加"
}
```

### Explanation
このコードの変更は、`deploy-models-mistral.md`ファイルに対するマイナーな修正で、Mistral AIのプレミアムチャットモデルに関する情報を更新しています。主な変更点は、Ministral 3Bモデルの新規追加です。

具体的には、以下のようなポイントが含まれます：

1. **モデルの追加**: Mistral 3Bが新たに紹介され、簡潔な説明が追加されました。このモデルはエッジコンピューティングとオンデバイスアプリケーション向けに最適化されており、低遅延で効率的な推論を実現します。
   
2. **モデルの特性**:
   - **入力/出力**: テキストデータのみを処理します。
   - **パラメータ数**: 3.6億のパラメータを持つことが記されています。

3. **既存モデルのリストの更新**: Mistral Large、Mistral Smallの他にMinistral 3Bが加わり、モデルのバリエーションが豊富になりました。

この更新により、ユーザーは新しいMinistral 3Bモデルについての理解を深め、特にリアルタイムのGenAIアプリケーションに適した選択肢を得ることができます。全体で62行の変更があり、最新の情報が反映されています。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -70,7 +70,7 @@ Network isolation | [Configure managed networks for Azure AI Studio hubs](config
 Model | Managed compute | Serverless API (pay-as-you-go)
 --|--|--
 Llama family models | Llama-2-7b <br> Llama-2-7b-chat <br> Llama-2-13b <br> Llama-2-13b-chat <br> Llama-2-70b <br> Llama-2-70b-chat <br> Llama-3-8B-Instruct <br> Llama-3-70B-Instruct <br> Llama-3-8B <br> Llama-3-70B | Llama-3-70B-Instruct <br> Llama-3-8B-Instruct <br> Llama-2-7b <br> Llama-2-7b-chat <br> Llama-2-13b <br> Llama-2-13b-chat <br> Llama-2-70b <br> Llama-2-70b-chat
-Mistral family models | mistralai-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x22B-Instruct-v0-1 <br> mistral-community-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x7B-v01 <br> mistralai-Mistral-7B-Instruct-v0-2 <br> mistralai-Mistral-7B-v01 <br> mistralai-Mixtral-8x7B-Instruct-v01 <br> mistralai-Mistral-7B-Instruct-v01 | Mistral-large (2402) <br> Mistral-large (2407) <br> Mistral-small <br> Mistral-NeMo
+Mistral family models | mistralai-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x22B-Instruct-v0-1 <br> mistral-community-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x7B-v01 <br> mistralai-Mistral-7B-Instruct-v0-2 <br> mistralai-Mistral-7B-v01 <br> mistralai-Mixtral-8x7B-Instruct-v01 <br> mistralai-Mistral-7B-Instruct-v01 | Mistral-large (2402) <br> Mistral-large (2407) <br> Mistral-small <br> Ministral-3B <br> Mistral-NeMo
 Cohere family models | Not available | Cohere-command-r-plus-08-2024 <br> Cohere-command-r-08-2024 <br> Cohere-command-r-plus <br> Cohere-command-r <br> Cohere-embed-v3-english <br> Cohere-embed-v3-multilingual <br> Cohere-rerank-v3-english <br> Cohere-rerank-v3-multilingual
 JAIS | Not available | jais-30b-chat
 Healthcare AI Family Models | MedImageInsight <br> CxrReportGen <br> MedImageParse | Not Available
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralファミリーモデルの更新"
}
```

### Explanation
このコードの変更は、`model-catalog-overview.md`ファイルに対するマイナーな修正で、Mistralファミリーモデルに関する情報が更新されています。具体的には、Mistralファミリーのモデルリストに「Ministral-3B」が新たに追加されました。

変更点は次の通りです：

1. **モデルリストの更新**: Mistralファミリーモデルに「Ministral-3B」が追加され、他のモデルと共にサーバーレスAPIで使用可能であることが示されています。

2. **その他の修正**: Mistralモデルに関する行において、細かなフォーマットの調整が行われています。

この更新により、ユーザーは最新のMistralファミリーモデルの完全なリストを確認でき、特にMinistral-3Bの利用可能性についての情報を得ることができるようになりました。全体として変更は2行であり、Mistralモデルの選択肢が強化されています。

## articles/ai-studio/includes/region-availability-maas.md{#item-35d79c}

<details>
<summary>Diff</summary>
````diff
@@ -58,6 +58,7 @@ Phi-3-Medium-4K-Instruct  <br>  Phi-3-Medium-128K-Instruct  | Not applicable | E
 |Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
 Mistral Nemo     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong <br> Israel     | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
+Ministral-3B     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)   <br> Brazil <br> Hong Kong <br> Israel      | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           |  Not available       |
 Mistral Small     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)   <br> Brazil <br> Hong Kong <br> Israel      | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           |  Not available       |
 Mistral Large (2402)     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong <br> Israel    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
 Mistral-Large (2407)     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)   <br> Brazil <br> Hong Kong <br> Israel   | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Ministral-3Bの地域可用性の追加"
}
```

### Explanation
このコードの変更は、`region-availability-maas.md`ファイルに対するマイナーな修正で、Ministral-3Bモデルの地域可用性に関する情報が追加されています。

具体的には、以下の点が変更されています：

1. **モデルの追加**: 新たにMinistral-3Bがリストに加わり、その地域可用性が明確に記載されています。このモデルは、Microsoftの管理された国々（ブラジル、香港、イスラエル）での提供が確認されており、デプロイメント用のハブ/プロジェクト地域としては、East US、East US 2、North Central US、South Central US、Sweden Central、West US、West US 3が指定されています。

2. **情報の整合性**: 既存のMistralファミリーモデルと同様のフォーマットで地域の詳細が追加されたことにより、ユーザーにとってわかりやすい情報提供が実現されています。

この更新により、Ministral-3Bモデルについての可用性情報が強化され、ユーザーはこのモデルを適切な地域で使用できるかどうかをより明確に把握できるようになりました。全体で1行の変更があり、文書の一貫性が保たれています。

## articles/ai-studio/reference/region-support.md{#item-d402e1}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ Azure AI Studio is currently not available in Azure Government regions or air-ga
 
 ## Azure OpenAI
 
-[!INCLUDE [OpenAI Quotas](../../ai-services/openai/includes/model-matrix/quota.md)]
+For information on the availability of Azure OpenAI models, see [Azure OpenAI Model summary table and region availability](../../ai-services/openai/concepts/models.md#model-summary-table-and-region-availability).
 
 > [!NOTE]
 > Some models might not be available within the AI Studio model catalog.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIモデルの可用性情報の更新"
}
```

### Explanation
このコードの変更は、`region-support.md`ファイルに対するマイナーな修正で、Azure OpenAIモデルに関する可用性情報へのリンクが更新されています。

具体的な変更点は以下の通りです：

1. **リンクの修正**: Azure OpenAIモデルの可用性に関する情報のリンクが、以前のクオータ情報のリンクから「Azure OpenAIモデルの概要テーブルおよび地域可用性」に関する新しいURLに変更されました。これにより、ユーザーは関連情報により直接アクセスしやすくなっています。

2. **内容の明確化**: 新しいリンクによって、モデルの可用性やサポートされている地域についての情報が整理されており、ユーザーが必要なデータを探しやすくなっています。

この修正により、Azure OpenAIモデルに関する適切な情報が提供されることで、ユーザーはより効果的に利用可能なリソースを見つけることができるようになりました。変更は1行の追加と1行の削除で、全体で2行の調整が行われています。


