---
date: '2025-10-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6633d97...MicrosoftDocs:7e5f65d
summary: |-
  このDiffのハイライトは、Azure AI検索に関連する文書のマイナーアップデートです。主な変更には、文書の日付更新、説明文の明確化、技術的詳細の追加や修正が含まれていますが、新機能の追加や破壊的変更はありません。文書の可読性や情報の精度を向上させることが目的とされています。また、特定の新機能については言及されておらず、既存の機能説明や利用方法の改善が中心です。破壊的変更はなく、ユーザーへの直接的な影響は少ないと考えられます。

  その他の更新としては、文書の更新日が最新に保たれ、タイトルやパラメーターの微細な修正、Azure AI検索および関連スキルの詳細が増強されています。この一連の更新によって、ユーザーがAzureのAI機能を効果的に活用できるよう促進されることが期待されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6633d97...MicrosoftDocs:7e5f65d){target="_blank"}

# Highlights
このDiffのハイライトは、Azure AI検索に関連するさまざまな文書のマイナーアップデートです。それぞれ、文書の日付更新、説明文の明確化、技術的詳細の追加や修正が行われています。新しい機能の追加や破壊的変更は見られませんが、文書の可読性および情報の精度を向上させる改良が多岐にわたり実施されています。

## New features
特定の新機能に関する言及は無く、既存の機能説明や利用方法の改善、理解を助ける修正が中心です。

## Breaking changes
破壊的変更は特にありません。既存のインフラストラクチャやAPI利用への影響を与えるものではないため、現行使用中のユーザーへの直接的な影響は少ないと考えられます。

## Other updates
- 文書の更新日が最新の状態に改められ、常に最新情報が提供されるようになっています。
- タイトルやパラメーターの細部にわたる微細な修正により、文言の正確性が確保されます。
- Azure AI検索および関連スキルに関する詳細が増強され、初心者から経験者まで、幅広いユーザーのニーズに対応します。
- 各文書のリンクやリソースが整理され、情報の探索性が向上しています。

# Insights
この一連の文書更新は、主にAzure AI検索の使用に関する説明をより明確にし、正確な情報提供を目指したものです。

AI強化における検索インデックスのマッピングと構成については、新規ユーザーでも理解しやすい詳細が追加されており、特にAIを利用したスキルの展開方法や関連技術の紐づけについて改良が加えられています。これにより、ユーザーが楽にAzureの強力なAI機能を活用できるようになっています。

また、特定のスキルセットの利用方法も整理され、各スキルの機能がより明確化されました。ビルトイン、カスタム、ユーティリティスキルに関する記述が洗練され、それぞれの利点や使用ケースが具体化されています。

さらに、さまざまなインデックスやストレージの操作について、プロセスや要件が詳述され、特に大規模データソースを扱う際のインデクサーの動作とそのトラブルシューティングにおける情報が強化されました。ユーザーが期待する処理タイムフレームや一般的なプロセスについて、明確な指針が示されています。

Azure OpenAIを用いたベクトル化においても、より具体的なURLやAPIの利用説明が提供され、ユーザーが行うべきアクションが非常に明瞭になっています。

これらの修正によって、ドキュメントの理解が容易化され、その結果Azure AI検索の採用が促進される可能性があります。このマイナーアップデートにより、ユーザーエクスペリエンスの向上と、より効果的な技術情報の伝達が期待されています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-concept-intro.md](#item-bf9ed7) | minor update | コグニティブ検索の概念の紹介に関する更新 | modified | 30 | 28 | 58 | 
| [cognitive-search-predefined-skills.md](#item-81d522) | minor update | コグニティブ検索の事前定義されたスキルに関する更新 | modified | 22 | 22 | 44 | 
| [cognitive-search-skill-azure-openai-embedding.md](#item-3eca57) | minor update | Azure OpenAIエンベディングスキルに関する更新 | modified | 2 | 2 | 4 | 
| [search-blob-storage-integration.md](#item-bbdaa6) | minor update | Blobストレージ統合に関する文書の更新 | modified | 2 | 1 | 3 | 
| [search-how-to-large-index.md](#item-d34e42) | minor update | 大規模インデックス作成に関する文書の更新 | modified | 3 | 2 | 5 | 
| [search-indexer-troubleshooting.md](#item-087365) | minor update | インデクサーのトラブルシューティングに関する文書の更新 | modified | 7 | 1 | 8 | 
| [search-lucene-query-architecture.md](#item-b0d568) | minor update | Luceneクエリアーキテクチャに関する文書のタイトル修正 | modified | 1 | 1 | 2 | 
| [search-region-support.md](#item-25b0f1) | minor update | Azure AI Search のサポート地域に関する情報の更新 | modified | 8 | 6 | 14 | 
| [vector-search-vectorizer-azure-open-ai.md](#item-e75cee) | minor update | ベクトル検索とAzure OpenAIによるベクトル化に関する文書の更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/cognitive-search-concept-intro.md{#item-bf9ed7}

<details>
<summary>Diff</summary>
````diff
@@ -9,29 +9,31 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 09/23/2025
+ms.date: 10/06/2025
 ms.update-cycle: 180-days
 ---
 
 # AI enrichment in Azure AI Search
 
-In Azure AI Search, *AI enrichment* refers to integration with [Azure AI services](/azure/ai-services/what-are-ai-services) to process content that isn't searchable in its raw form. Through enrichment, analysis and inference are used to create searchable content and structure where none previously existed. 
+In Azure AI Search, *AI enrichment* refers to integration with [Azure AI services](/azure/ai-services/what-are-ai-services) to process content that isn't searchable in its raw form. Through enrichment, analysis and inference are used to create searchable content and structure where none previously existed.
 
-Because Azure AI Search is used for text and vector queries, the purpose of AI enrichment is to improve the utility of your content in search-related scenarios. Raw content must be text or images (you can't enrich vectors), but the output of an enrichment pipeline can be vectorized and indexed in a search index using skills like [Text Split skill](cognitive-search-skill-textsplit.md) for chunking and [AzureOpenAIEmbedding skill](cognitive-search-skill-azure-openai-embedding.md) for vector encoding. For more information about using skills in vector scenarios, see [Integrated data chunking and embedding](vector-search-integrated-vectorization.md).
+Because Azure AI Search is used for text and vector queries, the purpose of AI enrichment is to improve the utility of your content in search-related scenarios. Raw content must be text or images (you can't enrich vectors), but the output of an enrichment pipeline can be vectorized and indexed in a search index using skills like [Text Split skill](cognitive-search-skill-textsplit.md) for chunking and [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md) for vector encoding. For more information about using skills in vector scenarios, see [Integrated data chunking and embedding](vector-search-integrated-vectorization.md).
 
 AI enrichment is based on [*skills*](cognitive-search-working-with-skillsets.md).
 
-Built-in skills tap Azure AI services. They apply the following transformations and processing to raw content:
+[Built-in skills](cognitive-search-predefined-skills.md) tap Azure AI services. They apply the following transformations and processing to raw content:
 
-+ Translation and language detection for multi-lingual search
-+ Entity recognition to extract people names, places, and other entities from large chunks of text
-+ Key phrase extraction to identify and output important terms
-+ Optical Character Recognition (OCR) to recognize printed and handwritten text in binary files
-+ Image analysis to describe image content, and output the descriptions as searchable text fields
++ Translation and language detection for multilingual search.
++ Entity recognition to extract people names, places, and other entities from large chunks of text.
++ Key phrase extraction to identify and output important terms.
++ Optical character recognition (OCR) to recognize printed and handwritten text in binary files.
++ Image analysis to describe image content and output the descriptions as searchable text fields.
++ Text embeddings via Azure OpenAI for integrated vectorization.
++ Multimodal embeddings via Azure AI Vision for text and image vectorization.
 
-Custom skills run your external code. Custom skills can be used for any custom processing that you want to include in the pipeline.
+Custom skills run your external code. You can use custom skills for any custom processing you want to include in the pipeline.
 
-AI enrichment is an extension of an [**indexer pipeline**](search-indexer-overview.md) that connects to Azure data sources. An enrichment pipeline has all of the components of an indexer pipeline (indexer, data source, index), plus a [**skillset**](cognitive-search-working-with-skillsets.md) that specifies atomic enrichment steps.
+AI enrichment is an extension of an [indexer pipeline](search-indexer-overview.md) that connects to Azure data sources. An enrichment pipeline has all of the components of an indexer pipeline (indexer, data source, index) and a [skillset](cognitive-search-working-with-skillsets.md) that specifies atomic enrichment steps.
 
 The following diagram shows the progression of AI enrichment:
 
@@ -41,9 +43,9 @@ The following diagram shows the progression of AI enrichment:
 
 **Enrich & Index** covers most of the AI enrichment pipeline:
 
-+ Enrichment starts when the indexer ["cracks documents"](search-indexer-overview.md#document-cracking) and extracts images and text. The kind of processing that occurs next depends on your data and which skills you've added to a skillset. If you have images, they can be forwarded to skills that perform image processing. Text content is queued for text and natural language processing. Internally, skills create an ["enriched document"](cognitive-search-working-with-skillsets.md#enrichment-tree) that collects the transformations as they occur.
++ Enrichment starts when the indexer *[cracks documents](search-indexer-overview.md#document-cracking)* and extracts images and text. The type of processing that occurs next depends on your data and the skills you've added to a skillset. Images can be forwarded to [skills that perform image processing](cognitive-search-concept-image-scenarios.md). Text content is queued for text and natural language processing. Internally, skills create an *[enriched document](cognitive-search-working-with-skillsets.md#enrichment-tree)* that collects transformations as they occur.
 
-+ Enriched content is generated during skillset execution, and is temporary unless you save it. You can enable an [enrichment cache](enrichment-cache-how-to-configure.md) to persist cracked documents and skill outputs for subsequent reuse during future skillset executions.
++ Enriched content is generated during skillset execution and is temporary unless you save it. You can enable an [enrichment cache](enrichment-cache-how-to-configure.md) to persist skill outputs for reuse in future skillset executions.
 
 + To get content into a search index, the indexer must have mapping information for sending enriched content to target field. [Field mappings](search-indexer-field-mappings.md) (explicit or implicit) set the data path from source data to a search index. [Output field mappings](cognitive-search-output-field-mapping.md) set the data path from enriched documents to an index.
 
@@ -53,9 +55,9 @@ The following diagram shows the progression of AI enrichment:
 
 ## When to use AI enrichment
 
-Enrichment is useful if raw content is unstructured text, image content, or content that needs language detection and translation. Applying AI through the [**built-in skills**](cognitive-search-predefined-skills.md) can unlock this content for full text search and data science applications. 
+Enrichment is useful if raw content is unstructured text, image content, or content that needs language detection and translation. Applying AI through the [built-in skills](cognitive-search-predefined-skills.md) can unlock this content for full-text search and data science applications.
 
-You can also create [**custom skills**](cognitive-search-create-custom-skill-example.md) to provide external processing.
+You can also create [custom skills](cognitive-search-create-custom-skill-example.md) to provide external processing.
 Open-source, third-party, or first-party code can be integrated into the pipeline as a custom skill. Classification models that identify salient characteristics of various document types fall into this category, but any external package that adds value to your content could be used.
 
 ### Use-cases for built-in skills
@@ -64,33 +66,33 @@ Built-in skills are based on the Azure AI services APIs: [Azure AI Computer Visi
 
 A [skillset](cognitive-search-defining-skillset.md) that's assembled using built-in skills is well suited for the following application scenarios:
 
-+ **Image processing** skills include [Optical Character Recognition (OCR)](cognitive-search-skill-ocr.md) and identification of [visual features](cognitive-search-skill-image-analysis.md), such as facial detection, image interpretation, image recognition (famous people and landmarks), or attributes like image orientation. These skills create text representations of image content for full text search in Azure AI Search.
++ **Image processing** skills include [Optical Character Recognition (OCR)](cognitive-search-skill-ocr.md) and identification of [visual features](cognitive-search-skill-image-analysis.md), such as facial detection, image interpretation, image recognition (famous people and landmarks), or attributes like image orientation. These skills create text representations of image content for full-text search in Azure AI Search.
 
 + **Machine translation** is provided by the [Text Translation](cognitive-search-skill-text-translation.md) skill, often paired with [language detection](cognitive-search-skill-language-detection.md) for multi-language solutions.
 
-+ **Natural language processing** analyzes chunks of text. Skills in this category include [Entity Recognition](cognitive-search-skill-entity-recognition-v3.md), [Sentiment Detection (including opinion mining)](cognitive-search-skill-sentiment-v3.md), and [Personal Identifiable Information Detection](cognitive-search-skill-pii-detection.md). With these skills, unstructured text is mapped as searchable and filterable fields in an index. 
++ **Natural language processing** analyzes chunks of text. Skills in this category include [Entity Recognition](cognitive-search-skill-entity-recognition-v3.md), [Sentiment Detection (including opinion mining)](cognitive-search-skill-sentiment-v3.md), and [Personal Identifiable Information Detection](cognitive-search-skill-pii-detection.md). With these skills, unstructured text is mapped as searchable and filterable fields in an index.
 
 ### Use-cases for custom skills
 
-[**Custom skills**](cognitive-search-create-custom-skill-example.md) execute external code that you provide and wrap in the [custom skill web interface](cognitive-search-custom-skill-interface.md). Several examples of custom skills can be found in the [azure-search-power-skills](https://github.com/Azure-Samples/azure-search-power-skills/blob/main/README.md) GitHub repository.
+[Custom skills](cognitive-search-create-custom-skill-example.md) execute external code that you provide and wrap in the [custom skill web interface](cognitive-search-custom-skill-interface.md). Several examples of custom skills can be found in the [azure-search-power-skills](https://github.com/Azure-Samples/azure-search-power-skills/blob/main/README.md) GitHub repository.
 
-Custom skills aren’t always complex. For example, if you have an existing package that provides pattern matching or a document classification model, you can wrap it in a custom skill. 
+Custom skills aren’t always complex. For example, if you have an existing package that provides pattern matching or a document classification model, you can wrap it in a custom skill.
 
 ## Storing output
 
 In Azure AI Search, an indexer saves the output it creates. A single indexer run can create up to three data structures that contain enriched and indexed output.
 
 | Data store | Required | Location | Description |
 |------------|----------|----------|-------------|
-| [**searchable index**](search-what-is-an-index.md) | Required | Search service | Used for full text search and other query forms. Specifying an index is an indexer requirement. Index content is populated from skill outputs, plus any source fields that are mapped directly to fields in the index. |
-| [**knowledge store**](knowledge-store-concept-intro.md) | Optional | Azure Storage | Used for downstream apps like knowledge mining or data science. A knowledge store is defined within a skillset. Its definition determines whether your enriched documents are projected as tables or objects (files or blobs) in Azure Storage. |
-| [**enrichment cache**](enrichment-cache-how-to-configure.md) | Optional | Azure Storage | Used for caching enrichments for reuse in subsequent skillset executions. The cache stores imported, unprocessed content (cracked documents). It also stores the enriched documents created during skillset execution. Caching is helpful if you're using image analysis or OCR, and you want to avoid the time and expense of reprocessing image files. |
+| [searchable index](search-what-is-an-index.md) | Required | Search service | Used for full-text search and other query forms. Specifying an index is an indexer requirement. Index content is populated from skill outputs, plus any source fields that are mapped directly to fields in the index. |
+| [knowledge store](knowledge-store-concept-intro.md) | Optional | Azure Storage | Used for downstream apps like knowledge mining, data science, and multimodal search. A knowledge store is defined within a skillset. Its definition determines whether your enriched documents are projected as tables or objects (files or blobs) in Azure Storage. For [multimodal search scenarios](multimodal-search-overview.md#how-multimodal-search-works-in-azure-ai-search), you can save extracted images to the knowledge store and reference them at query time, allowing the images to be returned directly to client apps. |
+| [enrichment cache](enrichment-cache-how-to-configure.md) | Optional | Azure Storage | Used for caching enrichments for reuse in subsequent skillset executions. The cache stores imported, unprocessed content (cracked documents). It also stores the enriched documents created during skillset execution. Caching is helpful if you're using image analysis or OCR, and you want to avoid the time and expense of reprocessing image files. |
 
 Indexes and knowledge stores are fully independent of each other. While you must attach an index to satisfy indexer requirements, if your sole objective is a knowledge store, you can ignore the index after it's populated.
 
 ## Exploring content
 
-After you've defined and loaded a [search index](search-what-is-an-index.md) or a [knowledge store](knowledge-store-concept-intro.md), you can explore its data.
+After you define and load a [search index](search-what-is-an-index.md) or [knowledge store](knowledge-store-concept-intro.md), you can explore its data.
 
 ### Query a search index
 
@@ -100,15 +102,15 @@ After you've defined and loaded a [search index](search-what-is-an-index.md) or
 
 In Azure Storage, a [knowledge store](knowledge-store-concept-intro.md) can assume the following forms: a blob container of JSON documents, a blob container of image objects, or tables in Table Storage. You can use [Storage Explorer](/azure/vs-azure-tools-storage-manage-with-storage-explorer), [Power BI](knowledge-store-connect-power-bi.md), or any app that connects to Azure Storage to access your content.
 
-+ A blob container captures enriched documents in their entirety, which is useful if you're creating a feed into other processes. 
++ A blob container captures enriched documents in their entirety, which is useful if you're creating a feed into other processes.
 
 + A table is useful if you need slices of enriched documents, or if you want to include or exclude specific parts of the output. For analysis in Power BI, tables are the recommended data source for data exploration and visualization in Power BI.
 
 ## Availability and pricing
 
-Enrichment is available in regions that have Azure AI services. You can check the availability of enrichment on the [regions list](search-region-support.md) page. 
+AI enrichment is available in regions that offer Azure AI services. To check the availability of AI enrichment, see the [regions list](search-region-support.md).
 
-Billing follows a Standard pricing model. The costs of using built-in skills are passed on when a multi-region Azure AI services key is specified in the skillset. There are also costs associated with image extraction, as metered by Azure AI Search. Text extraction and utility skills, however, aren't billable. For more information, see [How you're charged for Azure AI Search](search-sku-manage-costs.md#how-youre-charged-for-the-base-service).
+Billing follows a Standard pricing model. Costs associated with built-in skills are incurred when you specify an Azure OpenAI in Azure AI Foundry Models resource or Azure AI services multi-service resource key in the skillset. There are also costs associated with image extraction, as metered by Azure AI Search. However, text extraction and utility skills aren't billable. For more information, see [How you're charged for Azure AI Search](search-sku-manage-costs.md#how-youre-charged-for-the-base-service).
 
 ## Checklist: A typical workflow
 
@@ -122,15 +124,15 @@ Start with a subset of data in a [supported data source](search-indexer-overview
 
 1. [Create an index schema](search-how-to-create-search-index.md) that defines a search index.
 
-1. [Create and run the indexer](search-howto-create-indexers.md) to bring all of the above components together. This step retrieves the data, runs the skillset, and loads the index. 
+1. [Create and run the indexer](search-howto-create-indexers.md) to bring all of the previous components together. This step retrieves the data, runs the skillset, and loads the index.
 
    An indexer is also where you specify field mappings and output field mappings that set up the data path to a search index.
 
    Optionally, [enable enrichment caching](enrichment-cache-how-to-configure.md) in the indexer configuration. This step allows you to reuse existing enrichments later on.
 
 1. [Run queries](search-query-create.md) to evaluate results or [start a debug session](cognitive-search-how-to-debug-skillset.md) to work through any skillset issues.
 
-To repeat any of the above steps, [reset the indexer](search-howto-reindex.md) before you run it. Or, delete and recreate the objects on each run (recommended if you’re using the free tier). If you enabled caching the indexer pulls from the cache if data is unchanged at the source, and if your edits to the pipeline don't invalidate the cache.
+To repeat any of the previous steps, [reset the indexer](search-howto-reindex.md) before you run it. Alternatively, you can delete and recreate the objects on each run (recommended if you're using the free tier). If you enabled caching, the indexer pulls from the cache if the source data is unchanged and if your edits to the pipeline don't invalidate the cache.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブ検索の概念の紹介に関する更新"
}
```

### Explanation
この変更は、Azure AI検索におけるAI強化の概念を紹介する文書に関するもので、複数の文言の修正や明確化が行われました。具体的には、マークダウン内のテキストコピーが整理され、誤スペルや文章の流れを改善するための変更が施されています。

このアップデートでは、AI強化に関する説明の一貫性を高め、読者にとっての理解を容易にすることを目指しています。また、新たに追加された情報として、AI強化がどのようにして検索インデックスにマッピングされるのか、どのように構成されるかに関する詳細も含まれています。 

加えて、特定の技能（スキル）に関するセクションでは、AIサービスからの翻訳、エンティティ認識、キーフレーズ抽出に加え、画像処理などのビルトインスキルの利用方法についても触れられています。

この修正によって、文書全体としての品質と可読性が改善され、ユーザーが必要な情報を効率的に得られるように配慮されています。

## articles/search/cognitive-search-predefined-skills.md{#item-81d522}

<details>
<summary>Diff</summary>
````diff
@@ -10,27 +10,27 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: concept-article
-ms.date: 03/11/2025
+ms.date: 10/06/2025
 ms.update-cycle: 365-days
 ---
 
 # Skills for extra processing during indexing (Azure AI Search)
 
-This article describes the skills in Azure AI Search that you can include in a [skillset](cognitive-search-working-with-skillsets.md) to access external processing. 
+This article describes the skills in Azure AI Search that you can include in a [skillset](cognitive-search-working-with-skillsets.md) to access external processing.
 
-A *skill* is an atomic operation that transforms content in some way. Often, it's an operation that recognizes or extracts text, but it can also be a utility skill that reshapes the enrichments that are already created. Typically, the output is either text-based so that it can be used in [full text search](search-lucene-query-architecture.md), or vectors used in [vector search](vector-search-overview.md).
+A *skill* is an atomic operation that transforms content in some way. Often, it's an operation that recognizes or extracts text, but it can also be a utility skill that reshapes existing enrichments. The output is usually text-based for use in [full-text search](search-lucene-query-architecture.md) or vectors for use in [vector search](vector-search-overview.md).
 
-Skills are organized into categories:
+Skills are organized into the following categories:
 
-* A *built-in skill* wraps API calls to an Azure AI resource, where the inputs, outputs, and processing steps are well understood. For skills that call an Azure AI resource, the connection is made over the internal network. For skills that call Azure OpenAI, you provide the connection information that the search service uses to connect to the resource. A small quantity of processing is non-billable, but at larger volumes, processing is billable. Built-in skills are based on pretrained models from Microsoft, which means you can't train the model using your own training data.
+* A *built-in skill* wraps API calls to an Azure AI resource, where the inputs, outputs, and processing steps are well understood. For skills that call an Azure AI resource, the connection is made over the internal network. For skills that call Azure OpenAI, you provide the connection information that the search service uses to connect to the resource. A small quantity of processing is nonbillable, but at larger volumes, processing is billable. Built-in skills are based on pretrained models from Microsoft, which means you can't train the model using your own training data.
 
 * A *custom skill* provides custom code that executes externally to the search service. It's accessed through a URI. Custom code is often made available through an Azure function app. To attach an open-source or third-party vectorization model, use a custom skill.
 
-* A *utility* is internal to Azure AI Search, with no dependency on external resources or outbound connections. Most utilities are non-billable.
+* A *utility* is internal to Azure AI Search, with no dependency on external resources or outbound connections. Most utilities are nonbillable.
 
 ## Azure AI resource skills
 
-Skills that call the Azure AI are billed at the Standard rate when you [attach an AI service resource](cognitive-search-attach-cognitive-services.md).
+Skills that call Azure AI are billed at the Standard rate when you [attach an Azure AI services multi-service resource](cognitive-search-attach-cognitive-services.md).
 
 | OData type  | Description | Metered by |
 |-------|-------------|-------------|
@@ -55,18 +55,6 @@ Skills that call models deployed on Azure OpenAI are billed at the Standard rate
 |-------|-------------|-------------|
 |[Microsoft.Skills.Text.AzureOpenAIEmbeddingSkill](cognitive-search-skill-azure-openai-embedding.md) | Connects to a deployed embedding model on Azure OpenAI for integrated vectorization. | Azure OpenAI ([pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing)) |
 
-## Utility skills
-
-Skills that execute only on Azure AI Search, iterate mostly on nodes in the enrichment cache, and are mostly non-billable.
-
-| OData type  | Description | Metered by |
-|-------|-------------|-------------|
-| [Microsoft.Skills.Util.ConditionalSkill](cognitive-search-skill-conditional.md) | Allows filtering, assigning a default value, and merging data based on a condition. | Not applicable |
-| [Microsoft.Skills.Util.DocumentExtractionSkill](cognitive-search-skill-document-extraction.md) | Extracts content from a file within the enrichment pipeline. | Azure AI Search ([pricing](https://azure.microsoft.com/pricing/details/search/)) for image extraction. |
-| [Microsoft.Skills.Text.MergeSkill](cognitive-search-skill-textmerger.md) | Consolidates text from a collection of fields into a single field.  | Not applicable |
-| [Microsoft.Skills.Util.ShaperSkill](cognitive-search-skill-shaper.md) | Maps output to a complex type (a multi-part data type, which might be used for a full name, a multi-line address, or a combination of last name and a personal identifier.) | Not applicable |
-| [Microsoft.Skills.Text.SplitSkill](cognitive-search-skill-textsplit.md) | Splits text into pages so that you can enrich or augment content incrementally. | Not applicable |
-
 ## Custom skills
 
 [Custom skills](cognitive-search-custom-skill-web-api.md) wrap external code that you design, develop, and deploy to the web. You can then call the module from within a skillset as a custom skill.
@@ -78,8 +66,20 @@ Skills that execute only on Azure AI Search, iterate mostly on nodes in the enri
 
 For guidance on creating a custom skill, see [Define a custom interface](cognitive-search-custom-skill-interface.md) and [Example: Creating a custom skill for AI enrichment](cognitive-search-create-custom-skill-example.md).
 
-## See also
+## Utility skills
+
+Skills that execute only on Azure AI Search, iterate mostly on nodes in the enrichment cache, and are mostly nonbillable.
+
+| OData type  | Description | Metered by |
+|-------|-------------|-------------|
+| [Microsoft.Skills.Util.ConditionalSkill](cognitive-search-skill-conditional.md) | Allows filtering, assigning a default value, and merging data based on a condition. | Not applicable |
+| [Microsoft.Skills.Util.DocumentExtractionSkill](cognitive-search-skill-document-extraction.md) | Extracts content from a file within the enrichment pipeline. | Azure AI Search ([pricing](https://azure.microsoft.com/pricing/details/search/)) for image extraction. |
+| [Microsoft.Skills.Text.MergeSkill](cognitive-search-skill-textmerger.md) | Consolidates text from a collection of fields into a single field.  | Not applicable |
+| [Microsoft.Skills.Util.ShaperSkill](cognitive-search-skill-shaper.md) | Maps output to a complex type (a multi-part data type, which might be used for a full name, a multi-line address, or a combination of last name and a personal identifier.) | Not applicable |
+| [Microsoft.Skills.Text.SplitSkill](cognitive-search-skill-textsplit.md) | Splits text into pages so that you can enrich or augment content incrementally. | Not applicable |
+
+## Related content
 
-+ [How to define a skillset](cognitive-search-defining-skillset.md)
-+ [Custom Skills interface definition](cognitive-search-custom-skill-interface.md)
++ [Create a skillset](cognitive-search-defining-skillset.md)
++ [Add a custom skill to an AI enrichment pipeline](cognitive-search-custom-skill-interface.md)
 + [Tutorial: Enriched indexing with AI](tutorial-skillset.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブ検索の事前定義されたスキルに関する更新"
}
```

### Explanation
この変更は、Azure AI検索で使用される事前定義されたスキルに関する文書の改訂です。主な修正点には、文書の日付の更新や、スキルとその機能に関する説明の改善が含まれています。

文書全体にわたり、スキルの定義や種類に関する表現がより明確になるように調整されており、特にビルトインスキル、カスタムスキル、ユーティリティスキルの説明が洗練されています。たとえば、ビルトインスキルにおいて接続情報の提供と請求に関する説明が明確化され、カスタムスキルについてはその外部コードにアクセスする方法が詳述されています。

ユーティリティスキルでは、実行がほとんど非課金であること、そしてそれがどのように機能するのかが説明されています。また、スキル与件の関連情報セクションも新たに追加され、関連する内容へのナビゲーションが容易になっています。

これらの変更により、ユーザーがAzure AI検索のスキルをより効果的に利用できるようサポートすることを目的としています。

## articles/search/cognitive-search-skill-azure-openai-embedding.md{#item-3eca57}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: reference
-ms.date: 09/26/2025
+ms.date: 10/06/2025
 ---
 
 #	Azure OpenAI Embedding skill
@@ -45,7 +45,7 @@ Parameters are case-sensitive.
 
 | Inputs | Description |
 |---------------------|-------------|
-| `resourceUri` | Required. The URI of the model provider. This parameter only supports URLs with the `openai.azure.com` domain, such as `https://<resourcename>.openai.azure.com`. If your Azure OpenAI endpoint has a URL with the `cognitiveservices.azure.com` domain, such as `https://<resourcename>.cognitiveservices.azure.com`, you must create a [custom subdomain](/azure/ai-services/openai/how-to/use-your-data-securely#enabled-custom-subdomain) with `openai.azure.com` for the Azure OpenAI resource and use `https://<resourcename>.openai.azure.com` instead. This field is required if your Azure OpenAI resource is deployed behind a private endpoint or uses Virtual Network (VNet) integration. [Azure API Management](/azure/api-management/api-management-key-concepts) endpoints are supported with URL `https://<resourcename>.azure-api.net `. Shared private links aren't supported for API Management endpoints.
+| `resourceUri` | Required. The URI of the model provider. This parameter only supports URLs with the `openai.azure.com` domain, such as `https://<resourcename>.openai.azure.com`. This field is required if your Azure OpenAI resource is deployed behind a private endpoint or uses Virtual Network (VNet) integration. [Azure API Management](/azure/api-management/api-management-key-concepts) endpoints are supported with URL `https://<resourcename>.azure-api.net`. Shared private links aren't supported for API Management endpoints. |
 | `apiKey`   |  The secret key used to access the model. If you provide a key, leave `authIdentity` empty. If you set both the `apiKey` and `authIdentity`, the `apiKey` is used on the connection. |
 | `deploymentId`   | Required. The name of the deployed Azure OpenAI embedding model. The model should be an embedding model, such as text-embedding-ada-002. See the [List of Azure OpenAI models](/azure/ai-services/openai/concepts/models) for supported models.|
 | `authIdentity`   | A user-managed identity used by the search service for connecting to Azure OpenAI. You can use either a [system or user managed identity](search-how-to-managed-identities.md). To use a system managed identity, leave `apiKey` and `authIdentity` blank. The system-managed identity is used automatically. A managed identity must have [Cognitive Services OpenAI User](/azure/ai-services/openai/how-to/role-based-access-control#azure-openai-roles) permissions to send text to Azure OpenAI. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIエンベディングスキルに関する更新"
}
```

### Explanation
この変更は、Azure OpenAIエンベディングスキルに関する文書の更新です。主な修正は、文書の日付を更新したことと、入力パラメータ説明の文言の調整です。

具体的には、`resourceUri`パラメータに関する説明が簡素化され、重要な情報が強調されています。元々冗長だった文が整理され、特にエンドポイントの指定に関する注意事項が明確にされています。また、Azure OpenAIリソースがプライベートエンドポイントまたは仮想ネットワーク（VNet）統合を使用している場合の要件も記載されています。

この変更によって、ユーザーはリソースの設定と必要なアクセス情報についてより理解しやすくなり、Azure OpenAIへの接続と使用に関連するプロセスが簡素化されます。全体として、文書の明瞭性が向上しており、利用者が必要な情報を迅速に把握できるように配慮されています。

## articles/search/search-blob-storage-integration.md{#item-bbdaa6}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 07/25/2025
+ms.date: 10/06/2025
 ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
@@ -143,3 +143,4 @@ A more permanent solution is to gather query inputs and present the response as
 
 + [Upload, download, and list blobs with the Azure portal (Azure Blob storage)](/azure/storage/blobs/storage-quickstart-blobs-portal)
 + [Set up a blob indexer (Azure AI Search)](search-howto-indexing-azure-blob-storage.md)
++ [Index large data sets](search-how-to-large-index.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blobストレージ統合に関する文書の更新"
}
```

### Explanation
この変更は、AzureのBlobストレージ統合に関する文書の更新です。主な変更点は、文書の日付の更新と、関連情報へのリンクの追加です。

具体的には、文書の最終更新日が2025年7月25日から2025年10月6日に変更されました。また、参照リンクとして「Azureポータルを使用してBlobのアップロード、ダウンロード、およびリスト」というタイトルの新しいハイパーリンクが追加されています。さらに、「Blobインデクサーの設定」や「大規模データセットのインデックス作成」に関するリンクも加えられています。

これらの変更により、ユーザーはBlobストレージの利用に関する最新の情報を簡単に見つけることができ、特にデータセットのインデクス作成に関してより具体的なガイダンスを得やすくなります。全体として、文書の有用性と情報のアクセスの向上を目指しています。

## articles/search/search-how-to-large-index.md{#item-d34e42}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 08/01/2025
+ms.date: 10/06/2025
 ms.update-cycle: 180-days
 ---
 
@@ -82,7 +82,8 @@ Default batch sizes are data-source specific. Azure SQL Database and Azure Cosmo
 
 Indexer scheduling is an important mechanism for processing large data sets and for accommodating slow-running processes like image analysis in an enrichment pipeline. 
 
-Typically, indexer processing runs within a two-hour window. If the indexing workload takes days rather than hours to complete, you can put the indexer on a consecutive, recurring schedule that starts every two hours. Assuming the data source has [change tracking enabled](search-howto-create-indexers.md#change-detection-and-internal-state), the indexer resumes processing where it last left off. At this cadence, an indexer can work its way through a document backlog over a series of days until all unprocessed documents are processed. 
+Typically, indexer processing runs within a two-hour window. If the indexing workload takes days rather than hours to complete, you can put the indexer on a consecutive, recurring schedule that starts every two hours. Assuming the data source has [change tracking enabled](search-howto-create-indexers.md#change-detection-and-internal-state), the indexer resumes processing where it last left off. At this cadence, an indexer can work its way through a document backlog over a series of days until all unprocessed documents are processed. This pattern is especially important during the initial run or when indexing large blob containers, where the blob listing phase alone can take multiple hours or days. During this time, the indexer would show no blobs being processed, but unless an error is reported, it is likely still iterating through the blob list. Document processing and enrichment begin only after this phase completes, and this behavior is expected.
+
 
 ```json
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "大規模インデックス作成に関する文書の更新"
}
```

### Explanation
この変更は、「大規模インデックス作成」に関する文書の更新を示しています。主な変更点は、文書の日付の更新と、インデクサーの処理に関する詳細情報の追加です。

具体的には、文書の日付が2025年8月1日から2025年10月6日に変更されました。また、インデクサーのスケジューリングに関する説明が強化され、大規模なBlobコンテナをインデックスする際の特に重要な手順が強調されています。この更新により、ユーザーは初回実行や大量のBlobをインデックスする場合の時間のかかるプロセスについて理解しやすくなっています。

新しい説明では、Blobリストの取得に掛かる時間についても言及されており、この段階中はインデクサーがBlobを処理していないように見えるが、実際にはリストを繰り返し処理している可能性があることが明確にされています。このような情報が加わることで、ユーザーはインデクサーの動作に対する期待を持つことができ、より効果的にデータ処理を管理できるようになることを目的としています。

## articles/search/search-indexer-troubleshooting.md{#item-087365}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 05/29/2025
+ms.date: 10/06/2025
 ms.update-cycle: 365-days
 ---
 
@@ -19,6 +19,11 @@ Occasionally, indexers run into problems that don't produce errors or that occur
 > [!NOTE]
 > If you have an Azure AI Search error to investigate, see [Troubleshooting common indexer errors and warnings](cognitive-search-common-errors-warnings.md) instead.
 
+## Best practice: indexers are designed to run on a schedule
+> For reliable indexing, configure your indexers to run on a [regular schedule](search-howto-schedule-indexers.md). Scheduled runs automatically pick up any documents missed in previous runs due to transient errors, network interruptions, or temporary service issues. This approach helps maintain data consistency and minimizes the need for manual intervention.  
+>  
+> For [large data sources](search-how-to-large-index.md), the initial enumeration and indexing can take hours or even days. Running your indexer on a schedule allows that progress continues and errors are retried automatically. Avoid relying solely on manual or on-demand indexer runs, as these do not provide the same reliability or transient error recovery.  
+
 <a name="connection-errors"></a>
 
 ## Troubleshoot connections to restricted resources
@@ -291,3 +296,4 @@ If you have [sensitivity labels set on documents](/microsoft-365/compliance/sens
 
 * [Troubleshooting common indexer errors and warnings](cognitive-search-common-errors-warnings.md)
 * [Monitor indexer-based indexing](search-monitor-indexers.md)
+* [Index large data sets](search-how-to-large-index.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーのトラブルシューティングに関する文書の更新"
}
```

### Explanation
この変更は、「インデクサーのトラブルシューティング」に関する文書の更新を示しています。主な内容は、文書の日付の更新に加えて、インデクサーの運用に関するベストプラクティスや、新たな情報の追加です。

具体的には、文書の日付が2025年5月29日から2025年10月6日に変更されました。さらに、インデクサーが定期的にスケジュールに基づいて実行されるべき理由についてのセクションが追加されました。この新しいセクションでは、定期的なインデクサーの実行が、過去の実行で見逃されたドキュメントを自動的に拾い上げる手助けをし、データの一貫性を維持しやすくすることが説明されています。

また、大規模なデータソースを扱う場合には、初期の列挙とインデックス作成に時間がかかることが触れられており、インデクサーをスケジュールで実行することの重要性が強調されています。手動またはオンデマンドのインデクサー実行では同様の信頼性や一時的なエラー回復が提供されないため、定期的な実行を推奨する内容となっています。

文書の最後には、関連するリソースへの新しいリンクも追加され、ユーザーが大規模データセットをインデックスするためのガイダンスを簡単に見つけられるように配慮されています。これにより、トラブルシューティングの効率が向上し、よりスムーズなデータ管理が可能になります。

## articles/search/search-lucene-query-architecture.md{#item-b0d568}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ ms.date: 03/07/2025
 ms.update-cycle: 365-days
 ---
 
-# Full text search in Azure AI Search
+# Full-text search in Azure AI Search
 
 Full text search is an approach in information retrieval that matches on plain text stored in an index. For example, given a query string "hotels in San Diego on the beach", the search engine looks for tokenized strings based on those terms. To make scans more efficient, query strings undergo lexical analysis: lower-casing all terms, removing stop words like "the", and reducing terms to primitive root forms. When matching terms are found, the search engine retrieves documents, ranks them in order of relevance, and returns the top results.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Luceneクエリアーキテクチャに関する文書のタイトル修正"
}
```

### Explanation
この変更は、「Luceneクエリアーキテクチャ」に関する文書のタイトルの修正を示しています。具体的には、文書のタイトルが「Full text search in Azure AI Search」から「Full-text search in Azure AI Search」に変更されました。この変更により、タイトルの表現が正確になり、文書の内容に対する理解が促進されることが期待されます。

この文書では、情報検索におけるフルテキスト検索のアプローチについて解説されており、検索エンジンがどのようにトークン化された文字列を使用してクエリ文字列に基づく結果を取得するかが述べられています。さらに、効率的な検索を実現するために、クエリ文字列がどのように形態素解析されるかについても言及されており、具体的にはすべての用語を小文字に変換したり、不要な単語を除去したり、基本形に変換したりするプロセスが説明されています。

タイトルの修正は小さい変更ですが、正確性を高める重要なものであり、ユーザーにとっての信頼性を向上させる効果があります。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,11 @@
 ---
 title: Supported Regions
 titleSuffix: Azure AI Search
-description: Shows supported regions and feature availability across regions for Azure AI Search.
+description: Learn about the regions that offer Azure AI Search and the features available in each region.
 author: haileytap
 ms.author: haileytapia
 manager: nitinme
-ms.date: 09/25/2025
+ms.date: 10/06/2025
 ms.service: azure-ai-search
 ms.topic: conceptual
 ms.custom:
@@ -121,16 +121,18 @@ You can create an Azure AI Search service in any of the following Azure public r
 
 ## Azure operated by 21Vianet
 
-| Region | AI enrichment | Availability zones | Agentic retrieval | Confidential computing | Semantic ranker | Query rewrite |
+| Region | AI enrichment <sup>1</sup> | Availability zones | Agentic retrieval | Confidential computing | Semantic ranker | Query rewrite |
 |--|--|--|--|--|--|--|
 | China East |  |  |  |  |  |  |
-| China East 2 <sup>1</sup> | ✅ |  |  |  |  |  |
+| China East 2 <sup>2</sup> | ✅ |  |  |  |  |  |
 | China East 3 |  |  |  |  |  |  |
 | China North |  |  |  |  |  |  |
-| China North 2 <sup>1</sup> |  |  |  |  |  |  |
+| China North 2 <sup>2</sup> |  |  |  |  |  |  |
 | China North 3 |  | ✅ | ✅ |  | ✅ | ✅ |
 
-<sup>1</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
+<sup>1</sup> Only China East 2 fully supports AI enrichment. In other 21Vianet regions, you can use skillsets with the [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md) for integrated vectorization, which depends on the availability of Azure OpenAI and Azure AI Search in your region. Otherwise, AI enrichment isn't supported.
+
+<sup>2</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search のサポート地域に関する情報の更新"
}
```

### Explanation
この変更は、「Azure AI Search」のサポート地域に関する文書の内容を更新したものです。主な更新内容には、説明文の改訂、日付の変更、テーブル内の情報修正が含まれています。

具体的には、文書の説明が「Azure AI Search のサポート地域と各地域での機能の可用性を示します。」から「Azure AI Search を提供する地域と各地域で利用可能な機能について学びます。」に変更され、内容が明確化されました。また、文書の日付が2025年9月25日から2025年10月6日に更新されています。

テーブル内では、中国の地域に関するAIジェイクリッチメントやその他の機能の可用性が修正されました。たとえば、"China East 2" に関する説明が、AIエンリッチメントの完全なサポートについての詳細に更新されています。また、他の21Vianet地域でのAIエンリッチメントを実現するための条件にも言及されています。これにより、ユーザーが各地域の機能や制限に関する理解を深めることができるようになっています。

これらの変更は、文書の明確性と正確性を高めることを目的としています。ユーザーにとっては、Azure AI Searchの機能利用のために必要な情報をより簡潔に把握できるようになる重要なアップデートです。

## articles/search/vector-search-vectorizer-azure-open-ai.md{#item-e75cee}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: reference
-ms.date: 09/26/2025
+ms.date: 10/06/2025
 ms.update-cycle: 365-days
 ---
 
@@ -39,7 +39,7 @@ Parameters are case-sensitive.
 
 | Parameter name	 | Description |
 |--------------------|-------------|
-| `resourceUri` | The URI of the model provider. This parameter only supports URLs with the `openai.azure.com` domain, such as `https://<resourcename>.openai.azure.com`. If your Azure OpenAI endpoint has a URL with the `cognitiveservices.azure.com` domain, such as `https://<resourcename>.cognitiveservices.azure.com`, you must create a [custom subdomain](/azure/ai-services/openai/how-to/use-your-data-securely#enabled-custom-subdomain) with `openai.azure.com` for the Azure OpenAI resource and use `https://<resourcename>.openai.azure.com` instead. [Azure API Management](/azure/api-management/api-management-key-concepts) endpoints are supported with URL `https://<resourcename>.azure-api.net `. Shared private links aren't supported for API Management endpoints. |
+| `resourceUri` | The URI of the model provider. This parameter only supports URLs with the `openai.azure.com` domain, such as `https://<resourcename>.openai.azure.com`. [Azure API Management](/azure/api-management/api-management-key-concepts) endpoints are supported with URL `https://<resourcename>.azure-api.net`. Shared private links aren't supported for API Management endpoints. |
 | `apiKey`   |  The secret key used to access the model. If you provide a key, leave `authIdentity` empty. If you set both the `apiKey` and `authIdentity`, the `apiKey` is used on the connection. |
 | `deploymentId`   | The name of the deployed Azure OpenAI embedding model. The model should be an embedding model, such as text-embedding-ada-002. See the [List of Azure OpenAI models](/azure/ai-services/openai/concepts/models) for supported models.|
 | `authIdentity`   | A user-managed identity used by the search service for connecting to Azure OpenAI. You can use either a [system or user managed identity](search-how-to-managed-identities.md). To use a system managed identity, leave `apiKey` and `authIdentity` blank. The system-managed identity is used automatically. A managed identity must have [Cognitive Services OpenAI User](/azure/ai-services/openai/how-to/role-based-access-control#azure-openai-roles) permissions to send text to Azure OpenAI. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索とAzure OpenAIによるベクトル化に関する文書の更新"
}
```

### Explanation
この変更は、「ベクトル検索」と「Azure OpenAIによるベクトル化」に関する文書の一部を更新したものです。主な変更点は文書の更新日と、パラメーター説明内における細かい修正です。

具体的には、文書の更新日が2025年9月26日から2025年10月6日に変更され、最新の情報が反映されています。また、`resourceUri` パラメーターの説明が修正され、顧客に対して必要な情報がより明確に提供されています。以前は「cognitiveservices.azure.com」ドメインを持つURLについての指示が含まれていましたが、現在は明確に「openai.azure.com」ドメインに関する説明が強調され、API Managementのエンドポイントについても新たに詳述されています。これにより、ユーザーが適切なURLを選択する際の理解が向上しています。

このような小さな変更は、情報の正確性を維持し、ユーザーがAzure OpenAIリソースを利用する際の指針をさらに効果的にするための重要なステップです。文書全体のクオリティ向上にも寄与しています。


