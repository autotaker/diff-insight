---
date: '2025-06-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4e306c3...MicrosoftDocs:776cc95
summary: Azureドキュメントにおいていくつかの小規模な更新が行われ、ユーザーの機能理解向上と利用のスムーズさが図られました。新たに文書レイアウトスキルに出力形式を制御するパラメーターが追加され、ユーザーのカスタマイズ性が向上しました。破壊的な変更はなく、その他にも説明の明確化や地域・言語サポートの整理、セキュリティ項目の再配置などが行われました。これらの変更は、ユーザーエクスペリエンスを向上させる重要な手段であり、サービス利用時の情報アクセスも改善されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4e306c3...MicrosoftDocs:776cc95){target="_blank"}

<format>
# ハイライト

Azureドキュメントにおけるいくつかの小規模な更新が行われ、ユーザーは機能をより理解しやすくなり、利用をスムーズにするための調整が行われました。

## 新機能
- 文書レイアウトスキルでの出力形式を制御する新しいパラメーターが導入されました。

## 破壊的変更
- 特に破壊的な変更はありません。

## その他の更新
- 文書レイアウトスキルに関する説明の明確化とセクションタイトルの調整。
- 地域や言語サポート、SKUティアに関する情報の整理。
- 目次のセキュリティ関連項目の再配置による情報の体系化。

# 洞察

Azureドキュメントに行われたこれらの変更は、主にユーザーエクスペリエンスの向上と機能の理解を促進するためのものです。ドキュメント全体を通じての調整は小規模ながらも、ユーザーがサービスをより効果的に利用するための基盤を形成する重要な一歩と言えます。

特に、文書レイアウトスキルの新しいパラメーターによる出力形式の制御機能は、ユーザーが求める形式にカスタマイズしやすくなるため、柔軟な利用が期待されます。また、地域サポート情報の簡潔化とセキュリティ項目の再配置は、リファレンスの見やすさと一貫性を促進し、利用者が必要な情報に迅速にアクセスできる環境を構築します。

これらの更新を通して、Azureはユーザーのフィードバックを取り入れ、サービスの利用プロセスをスムーズにすると同時に操作性の向上を図っています。このようなドキュメント改善の取り組みは、サービス全体の価値を高め、技術的側面でのユーザーサポートの強化に寄与します。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-document-intelligence-layout.md](#item-62c06f) | minor update | 文書レイアウトスキルに関する変更 | modified | 32 | 28 | 60 | 
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | イメージ検索に関するドキュメントの更新 | modified | 1 | 1 | 2 | 
| [search-region-support.md](#item-25b0f1) | minor update | 検索地域サポートに関する情報の更新 | modified | 1 | 3 | 4 | 
| [search-sku-tier.md](#item-7686b8) | minor update | SKUティアに関する情報の更新 | modified | 0 | 1 | 1 | 
| [toc.yml](#item-c4768f) | minor update | セキュリティ関連項目の構造変更 | modified | 7 | 5 | 12 | 


# Modified Contents
## articles/search/cognitive-search-skill-document-intelligence-layout.md{#item-62c06f}

<details>
<summary>Diff</summary>
````diff
@@ -11,16 +11,16 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: reference
-ms.date: 05/27/2025
+ms.date: 06/10/2025
 ---
 
 # Document Layout skill
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-The **Document Layout** skill analyzes a document to extract regions of interest and their inter-relationships to produce a syntactical representation of the document in Markdown or Text format. You can use it to extract text and images. Image extraction includes location metadata that preserves image position within the document. Image proximity to related content is better for Retrieval Augmented Generation (RAG) workloads and [multimodal search](multimodal-search-overview.md).
+The **Document Layout** skill analyzes a document to detect structure and characteristics, and produces a syntactical representation of the document in Markdown or Text format. You can use it to extract text and images, where image extraction includes location metadata that preserves image position within the document. Image proximity to related content adds value to Retrieval Augmented Generation (RAG) workloads and [multimodal search](multimodal-search-overview.md).
 
-This article is the reference documentation for the Document Layout skill. For usage information, see [Structure-aware chunking and vectorization](search-how-to-semantic-chunking.md). 
+This article is the reference documentation for the Document Layout skill. For usage information, see [How to chunk and vectorize by document layout](search-how-to-semantic-chunking.md). 
 
 It's common to use this skill on content such as PDFs that have structure and images. The following tutorials demonstrate several scenarios: 
 
@@ -34,15 +34,23 @@ It's common to use this skill on content such as PDFs that have structure and im
 > This skill is bound to a [billable Azure AI multi-service resource](cognitive-search-attach-cognitive-services.md) for transactions that exceed 20 documents per indexer per day. Execution of built-in skills is charged at the existing [Azure AI services Standard price](https://azure.microsoft.com/pricing/details/cognitive-services/).
 >
 
-## Supported  regions
+## Limitations
 
-The Document Layout skill calls the [Document Intelligence Public preview version 2024-07-31-preview](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true). 
+During the public preview, this skill has the following restrictions:
 
-Supported regions vary by modality:
++ The skill isn't suitable for large documents requiring more than 5 minutes of processing in the AI Document Intelligence layout model. The skill times out, but charges still apply to the AI Services multi-services resource if it attaches to the skillset for billing purposes. Ensure documents are optimized to stay within processing limits to avoid unnecessary costs.
+
+## Supported regions
+
+The Document Layout skill calls the [Document Intelligence Public preview version 2024-07-31-preview](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true). 
 
-+ When you're using AI services keys [to attach your multi-service resource to your skillset](cognitive-search-attach-cognitive-services.md#bill-through-a-resource-key) via the REST API, both your Azure AI Search service and AI multi-service resource must be in the same region. This is only possible in the Azure regions of **East US**, **West Europe**, **North Central US**, **West US 2**. But if you're using a managed identity for [billing through a keyless connection](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection), your Azure AI Search service must be in one of the following regions: **East US**, **West Europe**, **North Central US**, **West US 2**. On the other hand, you can use AI Document Intelligence through an Azure AI multi-service resource in any region where this service is available. See [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).
+Supported regions vary by modality and how the skill connects to the Document Intelligence layout model.
 
-+ In the [Import and vectorize data wizard](search-import-data-portal.md) in the Azure portal, you can enable document layout detection in the data source connection step. Document layout detection in the portal is available in the following Azure regions: **East US**, **West Europe**, **North Central US**. Create an Azure AI multi-service resource in one of these three regions to get the portal experience.
+| Approach | Regions | Requirement |
+|----------|---------|-------------|
+| [Import and vectorize data wizard](search-import-data-portal.md) | **East US**, **West Europe**, **North Central US** | Create an Azure AI multi-service resource in one of these regions to get the portal experience. |
+| Programmatic, using a [keyless connection (preview)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) for billing | Varies by resource | Create Azure AI Search in one of these regions:  **East US**, **West Europe**, **North Central US**, **West US 2**. <br>Access Document Intelligence through an Azure AI multi-service resource in any region listed in the [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table) table.|
+| Programmatic, using a [multi-service resource API key](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) for billing | **East US**, **West Europe**, **North Central US**, **West US 2** | Create your Azure AI Search service and AI multi-service resource in the same region. |
 
 ## Supported file formats
 
@@ -59,9 +67,13 @@ This skill recognizes the following file formats.
 + .PPTX
 + .HTML
 
+## Supported languages
+
+Refer to [Azure AI Document Intelligence layout model supported languages](/azure/ai-services/document-intelligence/language-support/ocr?view=doc-intel-3.1.0&tabs=read-print%2Clayout-print%2Cgeneral#layout&preserve-view=true) for printed text.
+
 ## Supported parameters
 
-Several parameters are version-specific. The skills parameter table notes the API version in which a parameter was introduced so that you know whether a version upgrade is required. To use version-specific features such as image and location metadata extraction in [2025-05-01-preview REST API](/rest/api/searchservice/skillsets/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true), you can use the Azure portal, or target a REST API version, or check an Azure SDK change log to see if it supports the feature.
+Several parameters are version-specific. The skills parameter table notes the API version in which a parameter was introduced so that you know how to configure the skill. To use version-specific features such as image and location metadata extraction in [2025-05-01-preview REST API](/rest/api/searchservice/skillsets/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true), you can use the Azure portal, or target 2025-05-01-preview, or check an Azure SDK change log to see if it supports the new parameters.
 
 The Azure portal supports most preview features and can be used to create or update a skillset. For updates to the Document Layout skill, edit the skillset JSON definition to add new preview parameters.
 
@@ -75,17 +87,6 @@ Microsoft.Skills.Util.DocumentIntelligenceLayoutSkill
 + Even if the file size for analyzing documents is 500 MB for [Azure AI Document Intelligence paid (S0) tier](https://azure.microsoft.com/pricing/details/cognitive-services/) and 4 MB for [Azure AI Document Intelligence free (F0) tier](https://azure.microsoft.com/pricing/details/cognitive-services/), indexing is subject to the [indexer limits](search-limits-quotas-capacity.md#indexer-limits) of your search service tier.
 + Image dimensions must be between 50 pixels x 50 pixels or 10,000 pixels x 10,000 pixels.
 + If your PDFs are password-locked, remove the lock before running the indexer.
-
-## Supported languages
-
-Refer to [Azure AI Document Intelligence layout model supported languages](/azure/ai-services/document-intelligence/language-support/ocr?view=doc-intel-3.1.0&tabs=read-print%2Clayout-print%2Cgeneral#layout&preserve-view=true) for printed text.
-
-## Limitations
-
-During the public preview, this skill has the following restrictions:
-
-+ The skill isn't suitable for large documents requiring more than 5 minutes of processing in the AI Document Intelligence layout model. The skill times out, but charges still apply to the AI Services multi-services resource if it attaches to the skillset for billing purposes. Ensure documents are optimized to stay within processing limits to avoid unnecessary costs.
-
   
 ## Skill parameters
 
@@ -97,13 +98,13 @@ Parameters are case-sensitive.
 | `markdownHeaderDepth` | [2024-11-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true) |`h1`, `h2`, `h3`, `h4`, `h5`, `h6(default)` | Only applies if `outputFormat` is set to `markdown`. This parameter describes the deepest nesting level that should be considered. For instance, if the markdownHeaderDepth is `h3`, any sections that are deeper such as `h4`, are rolled into `h3`. |
 | `outputFormat`    | [2025-05-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) |`markdown(default)`, `text` | **New**. Controls the format of the output generated by the skill. |
 | `extractionOptions`    | [2025-05-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) |`["images"]`, `["images", "locationMetadata"]`, `["locationMetadata"]` | **New**. Identify any extra content extracted from the document. Define an array of enums that correspond to the content to be included in the output. For instance, if the `extractionOptions` is `["images", "locationMetadata"]`, the output includes images and location metadata which provides page location information related to where the content was extracted, such as a page number or section. This parameter applies to both output formats.  |
-| `chunkingProperties`    | [2025-05-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) | See below | **New**. Only applies if `outputFormat` is set to `text`. Options that encapsulate how to chunk text content while recomputing other metadata. |
+| `chunkingProperties`    | [2025-05-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) | See below. | **New**. Only applies if `outputFormat` is set to `text`. Options that encapsulate how to chunk text content while recomputing other metadata. |
 
 | ChunkingProperties Parameter     | Version | Allowed Values | Description |
 |--------------------|-------------|-------------|-------------|
-| `unit`    | [2025-05-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) |`Characters`. currently the only allowed value. Chunk length is measured in characters, as opposed to words or tokens | Controls the cardinality of the chunk unit. |
-| `maximumLength`    | [2025-05-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) | Any integer between 300-50000 | The maximum chunk length in characters as measured by String.Length. |
-| `overlapLength`    | [2025-05-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) | Integer. The value needs to be less than the half of the `maximumLength` | The length of overlap provided between two text chunks. |
+| `unit`    | [2025-05-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) | `Characters`. currently the only allowed value. Chunk length is measured in characters, as opposed to words or tokens | **New**. Controls the cardinality of the chunk unit. |
+| `maximumLength`    | [2025-05-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) | Any integer between 300-50000 | **New**. The maximum chunk length in characters as measured by String.Length. |
+| `overlapLength`    | [2025-05-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) | Integer. The value needs to be less than the half of the `maximumLength` | **New**. The length of overlap provided between two text chunks. |
 
 ## Skill inputs
 
@@ -144,7 +145,8 @@ The file reference object can be generated in one of following ways:
 | `text_sections`    | Only applies if `outputFormat` is set to `text`. A collection of text chunk objects, which represent the text within the bounds of a page (factoring in any more chunking configured), *inclusive* of any section headers themselves. The text chunk object includes `locationMetadata` if applicable.|
 | `normalized_images`    | Only applies if `outputFormat` is set to `text` and `extractionOptions` includes `images`. A collection of images that were extracted from the document, including `locationMetadata` if applicable.|
 
-## Sample definition for markdown output mode
+### Sample definition for markdown output mode
+
 ```json
 {
   "skills": [
@@ -171,7 +173,7 @@ The file reference object can be generated in one of following ways:
 }
 ```
 
-## Sample output for markdown output mode
+### Sample output for markdown output mode
 
 ```json
 {
@@ -204,7 +206,7 @@ The value of the `markdownHeaderDepth` controls the number of keys in the "secti
 
 This example demonstrates how to use the new parameters introduced in the **2025-05-01-preview** to output text content in fixed-sized chunks and extract images along with location metadata from the document.
 
-## Sample definition for text output mode and image and metadata extraction
+### Sample definition for text output mode and image and metadata extraction
 
 ```json
 {
@@ -242,7 +244,7 @@ This example demonstrates how to use the new parameters introduced in the **2025
 }
 ```
 
-## Sample output for text output mode and image and metadata extraction
+### Sample output for text output mode and image and metadata extraction
 
 ```json
 {
@@ -292,7 +294,9 @@ This example demonstrates how to use the new parameters introduced in the **2025
     ] 
 }
 ```
+
 The skill uses [Azure AI Document Intelligence](/azure/ai-services/document-intelligence/overview) to compute locationMetadata. Refer to [Document Intelligence layout model](/azure/ai-services/document-intelligence/concept-layout) for details on how pages and bounding polygon coordinates are defined.
+
 The `imagePath` represents the relative path of a stored image. If the knowledge store file projection is configured in the skillset, this path matches the relative path of the image stored in the knowledge store.
 
 ## See also
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書レイアウトスキルに関する変更"
}
```

### Explanation
この変更は、Azure の**文書レイアウトスキル**に関するドキュメントの更新を含んでいます。主に、スキルの機能説明が明確化され、いくつかのセクションのタイトルが調整されました。具体的には、スキルが文書の構造や特徴を検出することが強調され、出力形式の新しいオプションが追加されました。

変更点の概要は以下の通りです:
- ドキュメントの日付が**2025年6月10日**に更新されました。
- **文書のレイアウトスキル**に関する説明が、文書の分析方法を詳述した内容に修正されました。
- 限定事項セクションが追加され、大きな文書を処理する際の時間制限が明確にされました。
- サポートされる地域や言語の情報が整理され、特にオプションやリソースの地域依存性について詳述されました。
- 出力形式を制御する新しいパラメーターが導入され、イメージとメタデータの抽出オプションも追加されました。

これらの変更により、ユーザーは文書レイアウトスキルの機能をより正確に理解し、効果的に利用することができるようになります。

## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -40,7 +40,7 @@ For content extraction, you can choose either default extraction via Azure AI Se
 | Method | Description |
 |--|--|
 | Default extraction | Extracts location metadata from PDF images only. Doesn't require another Azure AI resource. |
-| Enhanced extraction | Extracts location metadata from text and images for multiple document types. Requires an [Azure AI services multi-service resource](/azure/ai-services/multi-service-resource#azure-ai-multi-services-resource-for-azure-ai-search-skills) <sup>1</sup> in a [supported region](cognitive-search-skill-document-intelligence-layout.md#supported--regions). |
+| Enhanced extraction | Extracts location metadata from text and images for multiple document types. Requires an [Azure AI services multi-service resource](/azure/ai-services/multi-service-resource#azure-ai-multi-services-resource-for-azure-ai-search-skills) <sup>1</sup> in a [supported region](cognitive-search-skill-document-intelligence-layout.md#supported-regions). |
 
 <sup>1</sup> For billing purposes, you must [attach your multi-service resource](cognitive-search-attach-cognitive-services.md) to the skillset in your Azure AI Search service. Unless you use a [keyless connection](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) to create the skillset, both resources must be in the same region.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "イメージ検索に関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、Azure のイメージ検索機能に関するドキュメントの小規模な更新を示しています。主に、テーブル内の説明文の表記に一貫性を持たせるための修正が行われました。具体的には、「Enhanced extraction」という項目の中の「supported regions」のスペルが修正され、文書全体の明瞭性が向上しています。

変更点の概要は以下の通りです:
- 「Enhanced extraction」の説明にあたる「supported regions」の部分が一貫した表記に改訂され、ドキュメントの可読性が改善されました。
- 小さな変更ですが、明確な表現を維持することで、ユーザーに対する情報提供がより分かりやすくなりました。

これにより、Azure AI サービスの利用者がイメージ検索機能を効果的に理解し、適切に活用できるようになります。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -102,14 +102,12 @@ You can create an Azure AI Search service in any of the following Azure public r
 | Central India | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Jio India West​​ | ✅ |  | ✅ | ✅ | ✅ |
 | South India |  | ✅ |  |  |  |
-| Japan East <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ |
+| Japan East | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Japan West​ | ✅ |  | ✅ | ✅ |  |
 | Korea Central | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Korea South​​ |  |  | ✅ | ✅ |  |
 | Indonesia Central |  | ✅ |  |  |  |
 
-<sup>1</sup> This region has capacity constraints on all tiers.
-
 ## Azure Government regions
 
 | Region | AI enrichment | Availability zones | Agentic retrieval | Semantic ranker | Query rewrite |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索地域サポートに関する情報の更新"
}
```

### Explanation
この変更は、Azureの検索地域サポートに関するドキュメントの更新を示しています。主に、「日本東部」地域の表現が一部修正され、注記が削除されました。これにより、ドキュメントの簡潔さと明確さが向上しています。

具体的な変更点は以下の通りです:
- 「日本東部」の表記から「<sup>1</sup>」の注記が削除され、表がシンプルになりました。
- 日本東部地域の情報がよりスムーズに提供されるようになり、過去のキャパシティ制約に関する言及がなくなったため、ユーザーが利用可能性について不安を感じにくくなりました。
- これにより、ユーザーが地域のサポート状況を確認しやすくなり、Azure AI サービスの利用においてより明確な情報を得られるようになります。

このように、変更はドキュメントの可読性と情報の明瞭さを向上させ、ユーザー体験を改善することを目的としています。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -61,7 +61,6 @@ Currently, several regions are capacity-constrained for specific tiers and can't
 | Region | Disabled tier (SKU) due to over-capacity | Suggested alternative |
 |--------|------------------------------------------|-----------------------|
 | West US 2 | Basic, S1, S2, S3, L1, L2 | West US, West US 3|
-| Japan East |  Basic, S1, S2, S3, L1, L2| Japan West|
 
 ## Feature availability by tier
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SKUティアに関する情報の更新"
}
```

### Explanation
この変更は、AzureのSKUティアに関するドキュメントの小規模な更新を示しています。具体的には、「日本東部」に関する行が削除され、その地域での利用できないティア（SKU）の情報が簡略化されました。

変更点の概要は以下の通りです:
- 「日本東部」地域の「Basic, S1, S2, S3, L1, L2」というSKUが利用不可であることの記述が削除されました。これにより、情報が整理され、無駄な混乱を避けることができます。
- 削除された情報によって、今後のリソース選定における選択肢をより分かりやすく示すことが可能になり、ユーザー体験の向上が図られています。

この変更により、ドキュメント全体が簡潔になり、Azure AI サービスを利用する際の選択肢について、ユーザーにとってのわかりやすさが向上しています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -204,11 +204,6 @@ items:
       href: search-security-overview.md
     - name: Secure access to external data
       href: search-indexer-securing-resources.md
-    - name: Security controls by Azure Policy
-      displayName: regulatory, compliance, standards, domains
-      href: ./security-controls-policy.md
-    - name: Security baseline
-      href: /security/benchmark/azure/baselines/cognitive-search-security-baseline?toc=/azure/search/TOC.json
 - name: How-to guides
   items:
   - name: Service management
@@ -707,6 +702,13 @@ items:
       href: ./policy-reference.md
     - name: Monitoring data reference
       href: monitor-azure-cognitive-search-data-reference.md
+  - name: Security reference
+    items:
+    - name: Security controls by Azure Policy
+      displayName: regulatory, compliance, standards, domains
+      href: ./security-controls-policy.md
+    - name: Security baseline
+      href: /security/benchmark/azure/baselines/cognitive-search-security-baseline?toc=/azure/search/TOC.json
   - name: Skills reference
     items:
     - name: Overview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セキュリティ関連項目の構造変更"
}
```

### Explanation
この変更は、Azureのドキュメントの目次（toc.yml）の構造に関する更新を示しています。具体的には、セキュリティに関連する項目が整理され、新しいサブカテゴリとして再配置されました。

変更点の概要は以下の通りです:
- 「セキュリティコントロールによるAzureポリシー」という項目が新たに「セキュリティ参照」の下に追加されました。これにより、関連情報をより体系的に表示することが可能になりました。
- 「セキュリティベースライン」も同様に、「セキュリティ参照」セクションに移動され、ドキュメントの一貫性と可読性が向上しています。
- 不要な情報や重複が削除されたため、ユーザーは必要な情報をより簡単に見つけられるようになりました。

この変更は、Azure AI サービスにおけるセキュリティ要件に関する情報を明確に分けることで、ユーザーが効率的にリファレンスを利用できるようにすることを目的としています。全体として、ドキュメントの整合性と使いやすさが向上しています。


