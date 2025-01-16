---
date: '2025-01-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:36d0ff5...MicrosoftDocs:f3626a8
summary: この更新は、Azure AI関連のドキュメントにおける多数の小規模な変更および新機能の追加を含んでおり、主要な変更点にはコンテナ設定の更新、FAQの拡充、新APIバージョン情報の提供、プライベートリンク設定に関する新しいスクリーンショットの追加があります。全体的にはユーザー体験の向上を目指した重要な改善が多数見られ、特に初心者ユーザーにとって役立つ視覚的な素材が追加されました。また、用語の変更や地域サポート情報の更新もあり、技術的な明瞭性と利便性が向上しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:36d0ff5...MicrosoftDocs:f3626a8){target="_blank"}

# Highlights
この更新は、Azure AI関連のドキュメントにおける多数の小規模な変更およびいくつかの新機能の追加を含んでいます。主要な変更点には、コンテナ設定の更新、FAQセクションの拡充、新APIバージョン情報、および新しい機能の紹介などがあります。さらに、プライベートリンク設定に関連する文書には、新しいスクリーンショットの追加も行われました。

## New features
- プライベートエンドポイントの追加および削除に関する新しいスクリーンショットの追加。

## Breaking changes
- 特に破壊的な変更は示されていませんが、API用語の変更が行われています。（`ignore`から`drop`への変更）。

## Other updates
- コンテナ設定における共有フォルダパス変更。
- FAQの内容更新と新しい質問の追加。
- カスタムニューラルモデルに関するトレーニングガイドの更新。
- Document Intelligenceの新機能とAPIバージョン情報の更新。
- 暗号化キーに関するアーキテクチャの変更と注意点の追加。
- モデルライフサイクル退職のタイムライン情報の追加。
- プライベートリンク設定手順の詳細な説明とスクリーンショットの追加。
- APIパラメータの説明の用語修正（`ignore`から`drop`へ）。
- Azure AI Foundryの地域サポート情報の更新。

# Insights
今回のドキュメント変更は全体的に小規模なものであるが、ユーザー体験の向上を図るための重要な改善が複数含まれています。特に、プライベートエンドポイントのスクリーンショットの追加は、初心者ユーザーにとって操作手順を直感的に理解する助けとなります。スクリーンショットは視覚的な手助けを提供し、ユーザーの自信を高めます。

さらに、コンテナ設定やAPIの用語変更は、技術的な明瞭性と正確性の向上を示しています。APIの用語変更は微細ですが、用語「ignore」から「drop」への変更で、APIが不要なパラメータをどのように扱うかの理解が深まります。このような変更は、一貫性のある文書を維持するために非常に有用です。

最後に、地域サポートの更新は、Azureのサービスをグローバルに利用するユーザーにとっての利便性を向上させます。最新のサポート地域を確認することにより、アプリケーションの展開がスムーズになるでしょう。全体として、これらのアップデートは、技術的な理解を促進し、ユーザーが提供された新機能を最大限に活用できるようにするものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [install-run.md](#item-e32e11) | minor update | コンテナの共有フォルダのパスの変更 | modified | 6 | 6 | 12 | 
| [faq.yml](#item-7a051f) | minor update | FAQの更新と新しい質問の追加 | modified | 16 | 9 | 25 | 
| [custom-neural.md](#item-ac0e69) | minor update | カスタムニューラルモデルのトレーニングに関する内容の更新 | modified | 23 | 20 | 43 | 
| [whats-new.md](#item-1ec8d3) | minor update | 新機能とAPIバージョン情報の更新 | modified | 8 | 8 | 16 | 
| [encryption-keys-portal.md](#item-95428d) | minor update | 顧客管理キーに関する注意事項の更新 | modified | 3 | 1 | 4 | 
| [model-lifecycle-retirement.md](#item-f0fc21) | minor update | モデルライフサイクルに関する情報の更新 | modified | 2 | 2 | 4 | 
| [configure-private-link.md](#item-bbf93d) | minor update | プライベートリンクの構成に関する手順の更新 | modified | 29 | 10 | 39 | 
| [add-private-endpoint.png](#item-f0187e) | new feature | プライベートエンドポイント追加のスクリーンショット | added | 0 | 0 | 0 | 
| [remove-private-endpoint.png](#item-f4acd1) | new feature | プライベートエンドポイント削除のスクリーンショット | added | 0 | 0 | 0 | 
| [reference-model-inference-chat-completions.md](#item-e09823) | minor update | APIパラメータの説明の修正 | modified | 1 | 1 | 2 | 
| [reference-model-inference-completions.md](#item-bae39d) | minor update | APIパラメータの表現の修正 | modified | 1 | 1 | 2 | 
| [reference-model-inference-embeddings.md](#item-5e9064) | minor update | APIパラメータの表現の修正 | modified | 1 | 1 | 2 | 
| [reference-model-inference-images-embeddings.md](#item-70c7ac) | minor update | APIパラメータの表現の修正 | modified | 1 | 1 | 2 | 
| [region-support.md](#item-d402e1) | minor update | Azure AI Foundryの地域サポート情報の更新 | modified | 9 | 5 | 14 | 


# Modified Contents
## articles/ai-services/document-intelligence/containers/install-run.md{#item-e32e11}

<details>
<summary>Diff</summary>
````diff
@@ -519,13 +519,13 @@ services:
       apikey: ${FORM_RECOGNIZER_KEY}
       billing: ${FORM_RECOGNIZER_ENDPOINT_URI}
       Logging:Console:LogLevel:Default: Information
-      SharedRootFolder: /shared
-      Mounts:Shared: /shared
+      SharedRootFolder: /share
+      Mounts:Shared: /share
       Mounts:Output: /logs
     volumes:
       - type: bind
         source: ${SHARED_MOUNT_PATH}
-        target: /shared
+        target: /share
       - type: bind
         source: ${OUTPUT_MOUNT_PATH}
         target: /logs
@@ -544,13 +544,13 @@ services:
       apikey: ${FORM_RECOGNIZER_KEY}
       billing: ${FORM_RECOGNIZER_ENDPOINT_URI}
       Logging:Console:LogLevel:Default: Information
-      SharedRootFolder: /shared
-      Mounts:Shared: /shared
+      SharedRootFolder: /share
+      Mounts:Shared: /share
       Mounts:Output: /logs
     volumes:
       - type: bind
         source: ${SHARED_MOUNT_PATH}
-        target: /shared
+        target: /share
       - type: bind
         source: ${OUTPUT_MOUNT_PATH}
         target: /logs
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテナの共有フォルダのパスの変更"
}
```

### Explanation
このコードの変更は、ドキュメントインテリジェンスに関連するコンテナ設定ファイルにおける共有フォルダのパスを変更するものです。具体的には、'/shared' から '/share' への変更が行われており、これに伴い設定の全体で6行が追加され、6行が削除されています。変更は主に構成設定に影響を与え、ロギングやマウントポイントに関連するボリュームの設定が更新されました。この更新により、設定ファイルがより明確かつ一貫性のあるものになります。

## articles/ai-services/document-intelligence/faq.yml{#item-7a051f}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ metadata:
   ms.service: azure-ai-document-intelligence
   ms.custom: references_regions
   ms.topic: faq
-  ms.date: 11/19/2024
+  ms.date: 01/14/2025
   ms.author: lajanuar
 title: Frequently asked questions
 summary: |
@@ -62,7 +62,7 @@ sections:
          Can Document Intelligence help with semantic chunking within documents for retrieval-augmented generation?
         answer: |
           **Yes.**
-          
+
           Document Intelligence can provide the building blocks to enable semantic chunking. Semantic chunking is a key step in retrieval-augmented generation (RAG) to ensure context dense chunks and relevance improvement.
 
           - Document Intelligence provides a layout model that provides a visual decomposition of the document into lines, paragraphs, sections, headers, and footers.
@@ -133,14 +133,14 @@ sections:
         answer: |
          **Yes.**
 
-         If your Document Intelligence resource is configured with a firewall or virtual network, you need to add the dedicated IP address 20.3.165.95 to the firewall allowlist for your Document Intelligence resource. Some functions in custom projects (for example, autolabel, project management and human in the loop) don't work if the public network access is disabled.
+         For `v4.0 11-30-2024 (GA)`, auto labeling is hosted natively with the rest of the service, so there's no need for IP allowlisting. For any previous version, if your Document Intelligence resource is configured with a firewall or virtual network, you need to add the dedicated IP address 20.3.165.95 to the firewall allowlist for your Document Intelligence resource. Some functions in custom projects (for example, autolabel, project management and human in the loop) don't work if the public network access is disabled.
 
       - question: |
          When I upload a file in Document Intelligence Studio by "Fetch from URL" function, can I use a URL from my blob storage?
 
         answer: |
-         **Yes.** 
-         
+         **Yes.**
+
          If your Azure blob storage URL includes a SAS token, and is accessible from public networks. You can't use the **Fetch** function for storage accounts where the key access is disabled or behind a firewall/VNet.
 
       - question: |
@@ -171,7 +171,7 @@ sections:
 
           Document Intelligence offers the latest development options within the following platforms:
 
-          - [REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31 &preserve-view=true&tabs=HTTP)
+          - [REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)
 
           - [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)
 
@@ -295,14 +295,21 @@ sections:
 
         The copy operation is limited to copying models within the specific cloud environment where you trained the model. For instance, copying models from the public cloud to the Azure Government cloud isn't supported.
 
+    - question: |
+        Am I charged when using auto labeling?
+
+      answer: |
+        **Yes.**
+         Auto label incurs a cost which is equivalent to an analyze request for the corresponding model for a document.
+
     - question: |
         Am I charged when training a custom models?
       answer: |
         **Yes.**
 
-        For `v4.0 11-30-2024 (GA)` custom neural models can be trained for free for a **maximum of 10 hours**. Whether you're training a single model for the 10 hours, or training multiple models for the total of 10 hours, you aren't charged for the first 10 hours. After using up the free 10 hours, you're **automatically charged by the extra training hour**. For details on the prices, refer to the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/). This new paid training feature enables training models for an extended duration to process larger documents. For more information on this paid training feature, check [custom neural model billing section](train/custom-neural.md#billing).
-        
-        For `v3.0 2022-08-31` or `v3.1 2023-07-31`, custom neural models can be trained for free for a maximum of 20 training sessions, with each session capped at 30 minutes of training duration. Once you use up all of the 20 training sessions, you can submit Azure support ticket to increase the training session limit. To increase the limit, two training sessions are considered as one training hour, and you're charged per two sessions / one training hour. For details on the prices, refer to the [pricing page]. For more information on ways to increase the limit, check [custom neural model billing section](train/custom-neural.md#billing). **For `v3.0` and `v3.1`, paid training feature is unavailable. Paid training feature for custom neural model is only available on `v4.0`.**
+        For `v4.0 11-30-2024 (GA)` custom neural models can be trained for free for a **maximum of 10 hours**. Whether you're training a single model for the 10 hours, or training multiple models for the total of 10 hours, you aren't charged for the first 10 hours. After using up the free 10 hours, you're **automatically charged by the extra training hour**. For details on prices, refer to the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/). This new paid training feature enables training models for an extended duration to process larger documents. For more information on this paid training feature, check [custom neural model billing section](train/custom-neural.md#billing).
+
+        For `v3.0 2022-08-31` or `v3.1 2023-07-31`, custom neural models can be trained for free for a maximum of 20 training sessions, with each session capped at 30 minutes of training duration. Once you use up all of the 20 training sessions, you can submit Azure support ticket to increase the training session limit. To increase the limit, two training sessions are considered as one training hour, and you're charged per two sessions / one training hour. For details on the prices, refer to the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/). For more information on ways to increase the limit, check [custom neural model billing section](train/custom-neural.md#billing). **For `v3.0` and `v3.1`, paid training feature is unavailable. Paid training feature for custom neural model is only available on `v4.0`.**
 
   - name: Storage account
     questions:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQの更新と新しい質問の追加"
}
```

### Explanation
このコードの変更は、ドキュメントインテリジェンスに関するFAQ（よくある質問）セクションの更新を反映しています。主な変更点は、日付の更新や既存の回答の修正に加えて、新しい質問とその回答が追加されたことです。また、文章の表現やレイアウトも一部修正されています。具体的には、オートラベリングに関する新しい質問が追加され、そのコストに関する情報も明確に表現されています。さらに、以前に存在した質問に対する回答も最新の情報に基づいて更新されており、ユーザーにとっての理解を助ける内容に改善されています。全体として、この更新はドキュメントインテリジェンスに関する重要な情報を正確かつ最新のものに保つことを目的としています。

## articles/ai-services/document-intelligence/train/custom-neural.md{#item-ac0e69}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 11/19/2024
+ms.date: 01/14/2025
 ms.author: lajanuar
 ms.custom:
   - references_regions
@@ -20,7 +20,6 @@ monikerRange: '>=doc-intel-3.0.0'
 
 # Document Intelligence custom neural model
 
-
 :::moniker range="doc-intel-4.0.0"
 **This content applies to:**![checkmark](../media/yes-icon.png) **v4.0 (GA)** | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=tru)
 ::: moniker-end
@@ -45,7 +44,7 @@ Custom neural models share the same labeling format and strategy as [custom temp
 ## Model capabilities
 
  > [!IMPORTANT]
- > Custom neural v4.0 `2024-11-30` (GA) model supports overlapping fields and table cell confidence.
+ > Custom neural v4.0 `2024-11-30` (GA) model supports signature detection, table cell confidence, and overlapping fields.
 
 Custom neural models currently support key-value pairs and selection marks and structured fields (tables).
 
@@ -62,22 +61,9 @@ The `Build` operation supports *template* and *neural* custom models. Previous v
 
 Neural models support documents that have the same information, but different page structures. Examples of these documents include United States W2 forms, which share the same information, but can vary in appearance across companies. For more information, *see* [Custom model build mode](custom-model.md#build-mode).
 
-### Overlapping fields
-
-Custom neural v4.0 `2024-11-30` (GA) model supports overlapping fields:
-
-To use the overlapping fields, your dataset needs to contain at least one sample with the expected overlap. To label an overlap, use **region labeling** to designate each of the spans of content (with the overlap) for each field. Labeling an overlap with field selection (highlighting a value) fails in the Studio as region labeling is the only supported labeling tool for indicating field overlaps. Overlap support includes:
-
-* Complete overlap. The same set of tokens are labeled for two different fields.
-* Partial overlap. Some tokens belong to both fields, but there are tokens that are only part of one field or the other.
-
-Overlapping fields have some limits:
-
-* Any token or word can only be labeled as two fields.
-* overlapping fields in a table can't span table rows.
-* Overlapping fields can only be recognized if at least one sample in the dataset contains overlapping labels for those fields.
+### Signature detection
 
-To use overlapping fields, label your dataset with the overlaps and train the model with the API version ``**2024-11-30 (GA)**``.
+Custom neural v4.0 2024-11-30 (GA) model supports signature detection. To label a signature, use field type as Signature and draw the regions for signature. Signature field only supports one draw region per field. To train a custom neural model with signature detection, you need to use at least **five samples** with signature labeled along with variations to get the most accurate results.
 
 ## Tabular fields
 
@@ -94,7 +80,7 @@ Tabular fields support **cross page tables** by default:
 
 Tabular fields are also useful when extracting repeating information within a document that isn't recognized as a table. For example, a repeating section of work experiences in a resume can be labeled and extracted as a tabular field.
 
-Tabular fields provide **table, row and cell confidence** with the ``**2024-11-30 (GA)**`` API:
+Tabular fields provide **table, row and cell confidence** with the `2024-11-30 (GA)` API:
 
 * Fixed or dynamic tables add confidence support for the following elements:
   * Table confidence, a measure of how accurately the entire table is recognized.
@@ -103,6 +89,23 @@ Tabular fields provide **table, row and cell confidence** with the ``**2024-11-3
 
 * The recommended approach is to review the accuracy in a top-down manner starting with the table first, followed by the row and then the cell. See  [confidence and accuracy scores](../concept/accuracy-confidence.md) to learn more about table, row, and cell confidence.
 
+### Overlapping fields
+
+Custom neural v4.0 2024-11-30 (GA) model supports overlapping fields:
+
+To use the overlapping fields, your dataset needs to contain at least one sample with the expected overlap. To label an overlap, use **region labeling** to designate each of the spans of content (with the overlap) for each field. Labeling an overlap with field selection (highlighting a value) fails in the Studio as region labeling is the only supported labeling tool for indicating field overlaps. Overlap support includes:
+
+* Complete overlap. The same set of tokens are labeled for two different fields.
+* Partial overlap. Some tokens belong to both fields, but there are tokens that are only part of one field or the other.
+
+Overlapping fields have some limits:
+
+* Any token or word can only be labeled as two fields.
+* overlapping fields in a table can't span table rows.
+* Overlapping fields can only be recognized if at least one sample in the dataset contains overlapping labels for those fields.
+
+To use overlapping fields, label your dataset with the overlaps and train the model with the API version ``**2024-11-30 (GA)**``.
+
 ### Supported languages and locales
 
 *See* our [Language Support—custom models](../language-support/custom.md#custom-neural) for a complete list of supported languages.
@@ -203,7 +206,7 @@ Custom neural models differ from custom template models in a few different ways.
 
 * Custom neural model doesn't recognize values split across page boundaries.
 * Custom neural unsupported field types are ignored if a dataset labeled for custom template models is used to train a custom neural model.
-* Custom neural models are limited to 20 build operations per month. Open a support request if you need the limit increased. For more information, see [Document Intelligence service quotas and limits](../service-limits.md).
+* Custom neural models are limited to 20 build operations per month for versions 3.x. Open a support request if you need the limit increased. For more information, see [Document Intelligence service quotas and limits](../service-limits.md).
 
 ## Training a model
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムニューラルモデルのトレーニングに関する内容の更新"
}
```

### Explanation
このコードの変更は、ドキュメントインテリジェンスに関するカスタムニューラルモデルのトレーニングガイドの内容を更新したものです。主な変更点には、日付の更新、新しい機能の追加、既存の情報の修正が含まれています。特に、「署名検出」機能が新たに追加され、学生やビジネス文書でよく見られる署名のラベリング方法について詳しく説明されています。また、「重複フィールド」についての説明も強化され、使用方法や制限が明示的に記載されています。

内容全体としては、APIのバージョンやモデルの能力に関する情報が整理されており、ユーザーが新しい機能を効果的に使用できるようにサポートしています。これにより、他の情報との一貫性が向上し、カスタムモデルのトレーニングがより効果的に行えるようになります。

## articles/ai-services/document-intelligence/whats-new.md{#item-1ec8d3}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: whats-new
-ms.date: 12/17/2024
+ms.date: 01/14/2025
 ms.author: lajanuar
 ms.custom:
   - references_regions
@@ -25,11 +25,11 @@ ms.custom:
 Document Intelligence service is updated on an ongoing basis. Bookmark this page to stay up to date with release notes, feature enhancements, and our newest documentation.
 
 > [!IMPORTANT]
-> Preview API versions are retired once the GA API is released. The 2023-02-28-preview API version is being retired, if you are still using the preview API or the associated SDK versions, please update your code to target the latest API version 2024-11-30 (GA). </br>
+> Preview API versions are retired once the GA API is released. The 2023-02-28-preview API version is retiring. If you're still using the preview API or the associated SDK versions, update your code to target the latest API version `2024-11-30 (GA)`. </br>
 
 ## December 2024
 
-**Document Intelligence v4.0 programming language SDKs are now generally available (GA)**! <br><br>The latest client SDKs default to the [**2024-11-30 REST API (GA)**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) version of the service.<br><br>
+**Document Intelligence v4.0 programming language SDKs are now generally available (GA)**! <br><br>The latest client libraries default to the [**2024-11-30 REST API (GA)**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30&preserve-view=true) version of the service.<br><br>
 For more information, *see* client libraries for the following supported programming languages:
 
 * [🆕 .NET (C#)](versioning/changelog-release-history.md?view=doc-intel-4.0.0&tabs=csharp&preserve-view=true)
@@ -53,12 +53,13 @@ For more information, *see* client libraries for the following supported program
 * 🆕 Searchable PDF. The [prebuilt read](prebuilt/read.md) model now supports images formats (JPEG/JPG, PNG, BMP, TIFF, HEIF)  and language expansion to include Chinese, Japanese, and Korean for  [PDF output](prebuilt/read.md#searchable-pdf).
  
 * [Custom classification model](train/custom-model.md#custom-classification-model)
-  * Custom classification model supports incremental training. You can add new samples to exisisting classes or add new classes by referencing an existing classifier. 
+  * Custom classification model supports incremental training. You can add new samples to existing classes or add new classes by referencing an existing classifier. 
   * With v4.0, custom classification model doesn't split documents by default during analysis. You need to explicitly set 'splitMode' property to auto to preserve the older behavior.
   * Custom classification model now supports 25,000 pages as new training page limit.
 
 * [Custom Neural Model](train/custom-neural.md)
   * Custom Neural model now supports signature detection.
+  * Custom neural models support paid training for longer duration when you need to train model with a larger labeled dataset. The first 20 training runs in a calendar month continue to be free. Any training operations over 20 is on the paid tier. Learn more details on [billing](train/custom-neural.md#billing).
 
 * [ US Bank statement model](concept-bank-statement.md)
   * US Bank Statement Model now supports check table extraction.
@@ -221,14 +222,13 @@ The Document Intelligence [**2023-10-31-preview**](/rest/api/aiservices/document
   * Add-on capabilities are available within all models excluding the [Read model](prebuilt/read.md).
 
 >[!NOTE]
-> With the 2022-08-31 API general availability (GA) release, the associated preview APIs are being deprecated. If you are using the 2021-09-30-preview, the 2022-01-30-preview or he 2022-06-30-preview API versions, please update your applications to target the 2022-08-31 API version. There are a few minor changes involved, for more information, _see_ the [migration guide](v3-1-migration-guide.md).
+> With the 2022-08-31 API general availability (GA) release, the associated preview APIs are being deprecated. If you're using the 2021-09-30-preview, 2022-01-30-preview, or 2022-06-30-preview API versions, update your applications to target the 2022-08-31 API version. There are a few minor changes involved, for more information, _see_ the [migration guide](v3-1-migration-guide.md).
 
 ## July 2023
 
 > [!NOTE]
 > Form Recognizer is now **Azure AI Document Intelligence**!
 >
-> * Document, Azure AI services encompass all of what were previously known as Cognitive Services and Azure Applied AI Services.
 > * There are no changes to pricing.
 > * The names *Cognitive Services* and *Azure Applied AI* continue to be used in Azure billing, cost analysis, price list, and price APIs.
 > * There are no breaking changes to application programming interfaces (APIs) or client libraries.
@@ -265,7 +265,7 @@ The v3.1 API introduces new and updated capabilities:
     :::image type="content" source="media/studio/analyze-options.gif" alt-text="Animated screenshot showing use of the analyze-options button to configure options in Studio.":::
 
     > [!NOTE]
-    > Font extraction is not visualized in Document Intelligence Studio. However, you can check the styles section of the JSON output for the font detection results.
+    > Font extraction isn't visualized in Document Intelligence Studio. However, you can check the styles section of the JSON output for the font detection results.
 
 ✔️ **Auto labeling documents with prebuilt models or one of your own models**
 
@@ -496,7 +496,7 @@ The v3.1 API introduces new and updated capabilities:
 ## September 2022
 
 >[!NOTE]
-> Starting with version 4.0.0, a new set of clients has been introduced to leverage the newest features of the Document Intelligence service.
+> Starting with version 4.0.0, a new set of clients is introduced to apply the newest features of the Document Intelligence service.
 
 **SDK version 4.0.0 GA release includes the following updates:**
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能とAPIバージョン情報の更新"
}
```

### Explanation
このコードの変更は、「Document Intelligence」に関する「What's New」ページの更新を反映しています。主な変更点は、最新のAPIバージョンに関する情報、新しい機能、SDKのリリースに関する内容が追加・修正されました。特に、2024年11月30日にGA（一般提供）となる新しいAPIバージョンに関する注意喚起が明記され、古いプレビューAPIの廃止についても触れられています。

新機能として、カスタム分類モデルのインクリメンタルトレーニングやカスタムニューラルモデルの署名検出機能の追加が強調されています。また、トレーニングの運用に関するコストに関する情報も更新され、より多くのラベル付きデータセットでモデルをトレーニングする際に、最初の20回のトレーニングは無料であることが説明されています。これにより、ユーザーは最新の機能や変更を把握し、効果的に活用できるようになります。

## articles/ai-studio/concepts/encryption-keys-portal.md{#item-95428d}

<details>
<summary>Diff</summary>
````diff
@@ -50,7 +50,8 @@ The following data is stored on the managed resources.
 A new architecture for customer-managed key encryption with hubs is available in preview, which resolves the dependency on the managed resource group. In this new model, encrypted data is stored service-side on Microsoft-managed resources instead of in managed resources in your subscription. Metadata is stored in multitenant resources using document-level CMK encryption. An Azure AI Search instance is hosted on the Microsoft-side per customer, and for each hub. Due to its dedicated resource model, its Azure cost is charged in your subscription via the hub resource.
 
 > [!NOTE]
-> During this preview key rotation and user-assigned identity capabilities are not supported. Service-side encryption is currently not supported in reference to an Azure Key Vault for storing your encryption key that has public network access disabled.
+> - During this preview key rotation and user-assigned identity capabilities are not supported. Service-side encryption is currently not supported in reference to an Azure Key Vault for storing your encryption key that has public network access disabled.
+> - If you are using the preview server-side storage, Azure charges will continue to accrue during the soft delete retention period.
 
 ## Use customer-managed keys with Azure Key Vault
 
@@ -97,6 +98,7 @@ Alternatively, use infrastructure-as-code options for automation. Example Bicep
 * At the time of creation, you can't provide or modify resources that are created in the Microsoft-managed Azure resource group in your subscription.
 * You can't delete Microsoft-managed resources used for customer-managed keys without also deleting your hub.
 * [Azure AI services Customer-Managed Key Request Form](https://aka.ms/cogsvc-cmk) is still required for Speech and Content Moderator.
+* If you are using the [server-side preview](#preview-service-side-storage-of-encrypted-data-when-using-customer-managed-keys), Azure charges will continue to accrue during the soft delete retention period.
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "顧客管理キーに関する注意事項の更新"
}
```

### Explanation
このコードの変更は、Azure AI Studioの「暗号化キー ポータル」に関するドキュメントの更新を反映しています。変更内容には、顧客管理キーのエンクリプションに関する新しいアーキテクチャのプレビュー情報や、サーバーサイドストレージに関する注意事項の追加が含まれています。

新しいアーキテクチャにより、管理リソースグループへの依存関係が解消され、エンクリプトされたデータがMicrosoftの管理リソースに保存されるモデルに移行します。この変更に伴い、プレビュー中の鍵ローテーションやユーザー指定のアイデンティティ機能はサポートされていないことが改めて強調されています。

また、サーバーサイドプレビューを使用している場合、ソフトデリートの保持期間中にAzureの料金が発生し続けることが明記されています。この情報は、ユーザーが課金に関する理解を深めるのに役立ちます。これにより、利用者は新しい機能とその制限を認識し、より良い運用ができるようになります。

## articles/ai-studio/concepts/model-lifecycle-retirement.md{#item-f0fc21}

<details>
<summary>Diff</summary>
````diff
@@ -63,9 +63,9 @@ Models labeled _Retired_ are no longer available for use. You can't create new d
 
 - Members of the _owner_, _contributor_, _reader_, monitoring contributor_, and _monitoring reader_ roles for each Azure subscription with a serverless API model deployment receive a notification when a model deprecation is announced. The notification contains the dates when the model enters legacy, deprecated, and retired states. The notification might provide information about possible replacement model options, if applicable.
 
+The following table lists the timelines for models that are on track for retirement. The specified dates are in UTC time.
 
-
-| Model provider | Model | Legacy date | Deprecation date | Retirement date | Suggested replacement model |
+| Model provider | Model | Legacy date (UTC) | Deprecation date (UTC) | Retirement date (UTC) | Suggested replacement model |
 | ---- | ---- | ---- | --- | ---- | --- |
 | Mistral AI | [Mistral-large-2407](https://aka.ms/azureai/landing/Mistral-Large-2407) | January 13, 2025 | February 13, 2025 | May 13, 2025 | [Mistral-large-2411](https://aka.ms/aistudio/landing/Mistral-Large-2411) |
 | Mistral AI | [Mistral-large](https://aka.ms/azureai/landing/Mistral-Large) | December 15, 2024 | January 15, 2025 | April 15, 2025 | [Mistral-large-2407](https://aka.ms/azureai/landing/Mistral-Large-2407) |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルに関する情報の更新"
}
```

### Explanation
このコードの変更は、Azure AI Studioの「モデルライフサイクル退職」に関する文書の更新を反映しています。更新された内容には、退職予定のモデルに関するタイムラインの情報が追加されています。

具体的には、モデルが「退職」状態になる際の各段階（レガシー、廃止、退職）の通知を受け取る役割についての説明が加えられています。また、退職予定のモデルには、UTC時間で示された具体的な日付が示され、代替モデルの提案も含まれています。この変更は、ユーザーがモデルの寿命を理解し、必要に応じて適切な代替モデルへの移行を計画するのに役立ちます。これにより、モデル管理がより効率的になり、ユーザーは一貫した体験を保つことができます。

## articles/ai-studio/how-to/configure-private-link.md{#item-bbf93d}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: scottpolly
 ms.service: azure-ai-studio
 ms.custom: ignite-2023, devx-track-azurecli, build-2024, ignite-2024
 ms.topic: how-to
-ms.date: 12/05/2024
+ms.date: 01/15/2025
 ms.reviewer: meerakurup
 ms.author: larryfr
 author: Blackmist
@@ -37,17 +37,29 @@ You get several hub default resources in your resource group. You need to config
 
 ## Create a hub that uses a private endpoint
 
-Use one of the following methods to create a hub with a private endpoint. Each of these methods __requires an existing virtual network__:
+If you are creating a new hub, use the following tabs to select how you are creating the hub (Azure portal or Azure CLI.) Each of these methods __requires an existing virtual network__:
 
 # [Azure portal](#tab/azure-portal)
 
-1. From the [Azure portal](https://portal.azure.com), go to Azure AI Foundry and choose __+ New Azure AI__.
-1. Choose network isolation mode in __Networking__ tab.
+> [!NOTE]
+> The information in this document is only about configuring a private link. For a walkthrough of creating a secure hub in the portal, see [Create a secure hub in the Azure portal](create-secure-ai-hub.md).
+
+1. From the [Azure portal](https://portal.azure.com), search for __Azure AI Foundry__ and create a new resource by selecting __+ New Azure AI__.
+1. After configuring the __Basics__ and __Storage__ tabs, select the __Networking__ tab and pick the __Network isolation__ option that best suits your needs.
+
+    :::image type="content" source="../media/how-to/network/ai-hub-networking.png" alt-text="Screenshot of the Create a hub with the option to set network isolation information." lightbox="../media/how-to/network/ai-hub-networking.png":::
+
 1. Scroll down to __Workspace Inbound access__ and choose __+ Add__.
+
+    :::image type="content" source="../media/how-to/network/workspace-inbound-access.png" alt-text="Screenshot of the workspace inbound access section." lightbox="../media/how-to/network/workspace-inbound-access.png":::
+
 1. Input required fields. When selecting the __Region__, select the same region as your virtual network.
 
 # [Azure CLI](#tab/cli)
 
+> [!NOTE]
+> The information in this section doesn't cover basic hub configuration. For more information, see [Create a hub using the Azure CLI](./develop/create-hub-project-sdk.md?tabs=azurecli).
+
 After creating the hub, use the [Azure networking CLI commands](/cli/azure/network/private-endpoint#az-network-private-endpoint-create) to create a private link endpoint for the hub.
 
 ```azurecli-interactive
@@ -113,12 +125,17 @@ Use one of the following methods to add a private endpoint to an existing hub:
 # [Azure portal](#tab/azure-portal)
 
 1. From the [Azure portal](https://portal.azure.com), select your hub.
-1. From the left side of the page, select __Networking__ and then select the __Private endpoint connections__ tab.
-1. When selecting the __Region__, select the same region as your virtual network.
-1. When selecting __Resource type__, use `azuremlworkspace`.
-1. Set the __Resource__ to your workspace name.
+1. From the left side of the page, select __Settings__, __Networking__, and then select the __Private endpoint connections__ tab. Select __+ Private endpoint__.
+
+    :::image type="content" source="../media/how-to/network/add-private-endpoint.png" alt-text="Screenshot of the private endpoint connections tab":::
 
-Finally, select __Create__ to create the private endpoint.
+1. When going through the forms to create a private endpoint, be sure to:
+
+    - From __Basics__, select the same the __Region__ as your virtual network.
+    - From __Resource__, select `amlworkspace` as the __target sub-resource__.
+    - From the __Virtual Network__ form, select the virtual network and subnet that you want to connect to.
+ 
+1. After populating the forms with any additional network configurations you require, use the __Review + create__ tab to review your settings and select __Create__ to create the private endpoint.
 
 # [Azure CLI](#tab/cli)
 
@@ -192,9 +209,11 @@ To remove a private endpoint, use the following information:
 # [Azure portal](#tab/azure-portal)
 
 1. From the [Azure portal](https://portal.azure.com), select your hub.
-1. From the left side of the page, select __Networking__ and then select the __Private endpoint connections__ tab.
+1. From the left side of the page, select __Settings__, __Networking__, and then select the __Private endpoint connections__ tab.
 1. Select the endpoint to remove and then select __Remove__.
 
+    :::image type="content" source="../media/how-to/network/remove-private-endpoint.png" alt-text="Screenshot of a selected private endpoint with the remove option highlighted.":::
+
 # [Azure CLI](#tab/cli)
 
 When using the Azure CLI, use the following command to remove the private endpoint:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートリンクの構成に関する手順の更新"
}
```

### Explanation
このコードの変更は、Azure AI Studioの「プライベートリンクを構成する」手順に関する文書の更新を反映しています。主な変更点は、プライベートエンドポイントの作成や構成方法に関する手順が詳しく説明されていることです。

文書に新たに追加された内容には、AzureポータルやAzure CLIを使用して新しいハブを作成する際の具体的な手順が含まれています。また、プライベートリンクに関する注意書きも追加され、たとえば「このドキュメントはプライベートリンクの構成に関する情報だけを扱っている」と明記されています。

更に、作成や削除の手順には、必要な入力フィールドや設定の具体的な選択肢が示されており、視覚的な情報を提供するスクリーンショットも追加されています。この更新は、ユーザーがプライベートリンクの構成をより簡単に行えるようにすることを目的としており、操作手順の正確性と明確性が向上しています。

## articles/ai-studio/media/how-to/network/add-private-endpoint.png{#item-f0187e}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "プライベートエンドポイント追加のスクリーンショット"
}
```

### Explanation
このコードの変更は、Azure AI Studioの「プライベートエンドポイントを追加する」手順に関連するスクリーンショットを新たに追加したものです。この画像は、特定の操作や設定手順を視覚的に示すもので、ユーザーがプライベートエンドポイントを作成する際の理解を助けることを目的としています。

具体的には、追加された画像は、「プライベートエンドポイント接続」タブの画面を示しており、このタブではユーザーがプライベートエンドポイントを追加するための選択肢や情報を提示しています。この追加により、文書の情報がより具体的で分かりやすくなり、ユーザーは手順を追いやすくなります。結果として、操作ガイドがより親しみやすくなり、実際のコンソール画面を参考にしながら自信を持って手順を進めることができるようになります。

## articles/ai-studio/media/how-to/network/remove-private-endpoint.png{#item-f4acd1}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "プライベートエンドポイント削除のスクリーンショット"
}
```

### Explanation
このコードの変更は、Azure AI Studioにおける「プライベートエンドポイントを削除する」手順に関連する新しいスクリーンショットの追加を示しています。この画像は、プライベートエンドポイントの削除に関する操作手順を視覚的に示し、ユーザーが具体的な手続きを理解しやすくすることを目的としています。

追加された画像には、プライベートエンドポイントを削除する際の画面の様子が表示されており、ユーザーはこのビジュアルを参考にして、自身の操作を進めることができます。この追加により、文書はよりわかりやすくなり、特に初心者ユーザーにとって、各手順が直感的にわかりやすくなります。結果として、ユーザーは安心して手続きを進められるようになります。

## articles/ai-studio/reference/reference-model-inference-chat-completions.md{#item-e09823}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ POST /chat/completions?api-version=2024-04-01-preview
 
 | Name | Required | Type | Description |
 | --- | --- | --- | --- |
-| extra-parameters | | string | The behavior of the API when extra parameters are indicated in the payload. Using `pass-through` makes the API to pass the parameter to the underlying model. Use this value when you want to pass parameters that you know the underlying model can support. Using `ignore` makes the API to drop any unsupported parameter. Use this value when you need to use the same payload across different models, but one of the extra parameters may make a model to error out if not supported. Using `error` makes the API to reject any extra parameter in the payload. Only parameters specified in this API can be indicated, or a 400 error is returned. |
+| extra-parameters | | string | The behavior of the API when extra parameters are indicated in the payload. Using `pass-through` makes the API to pass the parameter to the underlying model. Use this value when you want to pass parameters that you know the underlying model can support. Using `drop` makes the API to drop any unsupported parameter. Use this value when you need to use the same payload across different models, but one of the extra parameters may make a model to error out if not supported. Using `error` makes the API to reject any extra parameter in the payload. Only parameters specified in this API can be indicated, or a 400 error is returned. |
 | azureml-model-deployment |     | string | Name of the deployment you want to route the request to. Supported for endpoints that support multiple deployments. |
 
 ## Request Body
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIパラメータの説明の修正"
}
```

### Explanation
このコードの変更は、Azure AI Studioの「チャット完了のモデル推論」に関するドキュメントの内容を小規模に修正したものです。具体的には、APIの`extra-parameters`に関する説明がわずかに更新され、`ignore`から`drop`への用語変更が行われています。この変更は、APIの動作に関する説明の明確さを向上させることを目的としています。

修正前では、「unsupported parameter」があった場合のAPIの挙動として「ignore」という用語が使用されていましたが、修正後では「drop」という用語に変更されています。この変更により、APIがサポートされていないパラメータをどのように扱うかに関して、より一貫性のある理解が促進されます。

全体として、この修正はドキュメントの正確性と読みやすさを向上させるものであり、ユーザーがAPIを利用する際の理解を助けるための重要なアップデートといえます。

## articles/ai-studio/reference/reference-model-inference-completions.md{#item-bae39d}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ POST /completions?api-version=2024-04-01-preview
 
 | Name | Required | Type | Description |
 | --- | --- | --- | --- |
-| extra-parameters | | string | The behavior of the API when extra parameters are indicated in the payload. Using `pass-through` makes the API to pass the parameter to the underlying model. Use this value when you want to pass parameters that you know the underlying model can support. Using `ignore` makes the API to drop any unsupported parameter. Use this value when you need to use the same payload across different models, but one of the extra parameters may make a model to error out if not supported. Using `error` makes the API to reject any extra parameter in the payload. Only parameters specified in this API can be indicated, or a 400 error is returned. |
+| extra-parameters | | string | The behavior of the API when extra parameters are indicated in the payload. Using `pass-through` makes the API to pass the parameter to the underlying model. Use this value when you want to pass parameters that you know the underlying model can support. Using `drop` makes the API to drop any unsupported parameter. Use this value when you need to use the same payload across different models, but one of the extra parameters may make a model to error out if not supported. Using `error` makes the API to reject any extra parameter in the payload. Only parameters specified in this API can be indicated, or a 400 error is returned. |
 | azureml-model-deployment |     | string | Name of the deployment you want to route the request to. Supported for endpoints that support multiple deployments. |
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIパラメータの表現の修正"
}
```

### Explanation
このコードの変更は、Azure AI Studioの「推論完了モデル」に関連するドキュメントの内容における小規模な修正を示しています。具体的には、APIの`extra-parameters`に関する説明で、用語の修正が行われています。変更前の文言では「ignore」が使用されていましたが、修正後では「drop」に置き換えられています。

この修正は、APIが負荷に対してどのように動作するかの理解をより明確にすることを目的としています。新しい表現は、サポートされていないパラメータが含まれる場合のAPIの行動を示し、「drop」はより直感的にその意味を伝えます。また、同様に、他のモデル間で共通のペイロードを使用する場合に、特定のパラメータがエラーを引き起こす可能性があることについても言及されており、ユーザーにとっての理解を大いに助ける内容となっています。

この変更は、全体としてドキュメントの明瞭性を向上させ、利用者がAPIを効果的に活用できるようにするための重要な調整といえるでしょう。

## articles/ai-studio/reference/reference-model-inference-embeddings.md{#item-5e9064}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ POST /embeddings?api-version=2024-04-01-preview
 
 | Name | Required | Type | Description |
 | --- | --- | --- | --- |
-| extra-parameters | | string | The behavior of the API when extra parameters are indicated in the payload. Using `pass-through` makes the API to pass the parameter to the underlying model. Use this value when you want to pass parameters that you know the underlying model can support. Using `ignore` makes the API to drop any unsupported parameter. Use this value when you need to use the same payload across different models, but one of the extra parameters may make a model to error out if not supported. Using `error` makes the API to reject any extra parameter in the payload. Only parameters specified in this API can be indicated, or a 400 error is returned. |
+| extra-parameters | | string | The behavior of the API when extra parameters are indicated in the payload. Using `pass-through` makes the API to pass the parameter to the underlying model. Use this value when you want to pass parameters that you know the underlying model can support. Using `drop` makes the API to drop any unsupported parameter. Use this value when you need to use the same payload across different models, but one of the extra parameters may make a model to error out if not supported. Using `error` makes the API to reject any extra parameter in the payload. Only parameters specified in this API can be indicated, or a 400 error is returned. |
 | azureml-model-deployment |     | string | Name of the deployment you want to route the request to. Supported for endpoints that support multiple deployments. |
 
 ## Request Body
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIパラメータの表現の修正"
}
```

### Explanation
このコードの変更は、Azure AI Studioの「埋め込みモデル推論」に関するドキュメントの小規模な修正を表しています。具体的には、APIの`extra-parameters`という項目の説明が更新され、用語の修正が行われました。変更前は「ignore」という用語が使われていましたが、修正後は「drop」に変更されています。

この修正は、APIが支援していないパラメータを処理する方法についての説明をより明確にすることを目的としています。`drop`という表現は、APIがサポートされていないパラメータをどのように扱うかをよりわかりやすく伝えています。具体的には、異なるモデル間で共通のペイロードを使用する際に、特定のパラメータがエラーを引き起こす可能性があることにも触れています。

この変更により、ユーザーはAPIの機能を理解しやすくなり、より効果的に活用できるようになることが期待されます。全体として、ドキュメントの正確性と利用者への理解を助けるための重要な改善といえるでしょう。

## articles/ai-studio/reference/reference-model-inference-images-embeddings.md{#item-70c7ac}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ POST /images/embeddings?api-version=2024-04-01-preview
 
 | Name | Required | Type | Description |
 | --- | --- | --- | --- |
-| extra-parameters | | string | The behavior of the API when extra parameters are indicated in the payload. Using `pass-through` makes the API to pass the parameter to the underlying model. Use this value when you want to pass parameters that you know the underlying model can support. Using `ignore` makes the API to drop any unsupported parameter. Use this value when you need to use the same payload across different models, but one of the extra parameters may make a model to error out if not supported. Using `error` makes the API to reject any extra parameter in the payload. Only parameters specified in this API can be indicated, or a 400 error is returned. |
+| extra-parameters | | string | The behavior of the API when extra parameters are indicated in the payload. Using `pass-through` makes the API to pass the parameter to the underlying model. Use this value when you want to pass parameters that you know the underlying model can support. Using `drop` makes the API to drop any unsupported parameter. Use this value when you need to use the same payload across different models, but one of the extra parameters may make a model to error out if not supported. Using `error` makes the API to reject any extra parameter in the payload. Only parameters specified in this API can be indicated, or a 400 error is returned. |
 | azureml-model-deployment |     | string | Name of the deployment you want to route the request to. Supported for endpoints that support multiple deployments. |
 
 ## Request Body
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIパラメータの表現の修正"
}
```

### Explanation
このコードの変更は、Azure AI Studioにおける「画像埋め込みモデル推論」のドキュメントの内容に関する小規模な修正を表しています。具体的には、APIの`extra-parameters`に関する説明が更新され、用語の変更が行われています。変更前の説明では「ignore」という用語が使われていましたが、修正後は「drop」に変更されています。

この修正は、APIが余分なパラメータをどのように処理するかをより明確にしています。`drop`という表現は、サポートされないパラメータをどのように扱うかを説明する際に、より理解しやすい表現になっています。具体的には、異なるモデル間で同じペイロードを使用する際の問題点についても示されています。

変更の結果、ユーザーはAPIの動作をより正確に理解できるようになり、実際に利用する際に混乱を避けることができると期待されます。全体として、この修正はドキュメントの明瞭性を向上させ、利用者がAPIをより効果的に活用できるよう支援する重要な改善といえるでしょう。

## articles/ai-studio/reference/region-support.md{#item-d402e1}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: This article lists Azure AI Foundry feature availability across clo
 manager: scottpolly
 ms.service: azure-ai-studio
 ms.topic: conceptual
-ms.date: 5/21/2024
+ms.date: 01/15/2025
 ms.reviewer: deeikele
 ms.author: sgilley
 author: sdgilley
@@ -14,28 +14,28 @@ ms.custom: references_regions, build-2024
 
 # Azure AI Foundry feature availability across clouds regions
 
-[!INCLUDE [feature-preview](../includes/feature-preview.md)]
-
 Azure AI Foundry brings together various Azure AI capabilities that previously were only available as standalone Azure services. While we strive to make all features available in all regions where Azure AI Foundry is supported at the same time, feature availability may vary by region. In this article, you'll learn what Azure AI Foundry features are available across cloud regions.  
 
 ## Azure Public regions
 
-Azure AI Foundry is currently available in the following Azure regions. You can create [Azure AI Foundry hubs](../how-to/create-azure-ai-resource.md) and Azure AI Foundry projects in these regions.
+Azure AI Foundry is currently available in the following Azure regions. You can create [projects in Azure AI Foundry portal](../how-to/create-projects.md) in these regions.
 
 - Australia East
 - Brazil South
 - Canada Central
+- Canada East
 - East US
 - East US 2
 - France Central
 - Germany West Central
-- India South
 - Japan East
+- Korea Central
 - North Central US
 - Norway East
 - Poland Central
 - South Africa North
 - South Central US
+- South India
 - Sweden Central
 - Switzerland North
 - UAE North
@@ -65,6 +65,10 @@ Azure AI Speech capabilities including custom neural voice vary in regional avai
 
 Some models in the model catalog can be deployed as a serverless API with pay-as-you-go billing. For information on the regions where each model is available, see [Region availability for models in Serverless API endpoints](../how-to/deploy-models-serverless-availability.md).
 
+## Azure AI Content Safety
+
+To use the Content Safety APIs, you must create your Azure AI Content Safety resource in a supported region. For a list of supported regions, see [What is Azure AI Content Safety?](../../ai-services/content-safety/overview.md#region-availability)
+
 ## Next steps
 
 - See [Azure global infrastructure products by region](https://azure.microsoft.com/global-infrastructure/services/).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryの地域サポート情報の更新"
}
```

### Explanation
このコードの変更は、Azure AI Studioの「地域サポート」に関するドキュメントの内容を更新しています。主な修正点は、日付の更新と、いくつかの地域の追加、および一部表現の改善です。具体的には、初めに記載されていた日付が「2024年5月21日」から「2025年1月15日」に変更されました。

また、Azure AI Foundryが利用可能な地域リストが拡充され、新たに「カナダ東部」や「韓国中央」、さらには「南インド」などの地域が追加されています。一方で、他の地域の名称や表現も調整され、ドキュメントがより明確になっています。

さらに、新しく「Azure AI Content Safety」というセクションが追加され、コンテンツセーフティAPIを利用するために必要な地域サポート情報が記載されています。このように、ユーザーがAzure AI Foundryの機能と地域の関連情報をより正確に理解できるようにすることを目的とした重要な変更です。全体として、地域的なサポート情報の最新化は、利用者にとっての利便性を高めるものとなっています。


