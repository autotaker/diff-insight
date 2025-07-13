---
date: '2025-07-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:acf364a...MicrosoftDocs:3f50d3b
summary: 今回の変更では、複数のドキュメントのリンク更新と新しいスキルセットのチュートリアルの追加が行われ、ユーザーが最新の情報にアクセスしやすくなりました。特に、リダイレクト設定により、古い情報から新しい情報への移行がスムーズになっています。また、新しいチュートリアルはAzure
  AI Searchの利便性を高め、ユーザーエクスペリエンスも向上しています。全体として、情報の正確さとユーザーへの配慮が強化されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:acf364a...MicrosoftDocs:3f50d3b){target="_blank"}

<format>
# Highlights
今回の変更では、主に複数のドキュメントのリンクが更新され、新しいスキルセットのチュートリアルが追加されました。特に、リダイレクト設定の追加や外部リンクの修正により、ユーザーが古い情報から新しい情報によりスムーズにアクセスできるようになりました。また、新しいスキルセットのチュートリアルの追加は、Azure AI Searchの利便性を高めています。全体として、情報の正確さとユーザーエクスペリエンスの向上が図られています。

## New features
- `tutorial-skillset.md`という新しいファイルが追加され、Azure AI Searchにおけるスキルセットの作成方法のチュートリアルを提供する。
- C#およびRESTのクイックスタートが含まれており、ユーザーが自分の環境に合わせてスキルセットを作成できるようになっている。

## Breaking changes
特にユーザーに対する大きな影響を与える破壊的な変更はありませんが、既存のリンクを変更しているため、古いリンクには適切なリダイレクトが設定されています。

## Other updates
- 複数のファイルにおいて、チュートリアルおよびリダイレクトのリンクが`cognitive-search-tutorial-blob.md`から`tutorial-skillset.md`に変更され、最新の情報にアクセスできるようになっている。
- `toc.yml`ではナビゲーションメニューが更新され、ユーザーがスキルセットのチュートリアルを簡単に見つけられるようになった。

# Insights
今回の更新は、Azure AI Searchを利用するユーザーに対して、より最新で信頼性の高いドキュメントを提供することを目的としています。リダイレクト設定の追加は、古いコンテンツから新しいコンテンツへの移行をスムーズに行わせるための措置であり、リンクの更新も同様に最新の情報をユーザーに提供するためのものです。

特に、新しい`tutorial-skillset.md`の追加は、AIエンリッチメントのスキルセット作成に関心のある技術者にとって、大いに役立つリソースとなるでしょう。このドキュメントでは、インデックス作成中にスキルセットをどのように設定し、Azure AIの機能をどのように最大限に利用するかを詳細に解説しており、これにより実際のプロジェクトへの応用が容易になります。

さらに、ナビゲーションの改善によって、ユーザーは目的の情報により nhanh chóng達することができ、UXの向上が期待されます。この一連の更新は、最終的にはAzure AI Searchの利用をより効果的かつ効率的にすることを目的とした、重要なステップです。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [.openpublishing.redirection.search.json](#item-8b66f9) | minor update | リダイレクト設定の更新 | modified | 10 | 0 | 10 | 
| [chat-completion-skill-example-usage.md](#item-21e090) | minor update | チュートリアルリンクの修正 | modified | 1 | 1 | 2 | 
| [cognitive-search-concept-image-scenarios.md](#item-606953) | minor update | チュートリアルリンクの修正 | modified | 1 | 1 | 2 | 
| [cognitive-search-concept-intro.md](#item-bf9ed7) | minor update | チュートリアルリンクの修正 | modified | 1 | 1 | 2 | 
| [cognitive-search-concept-troubleshooting.md](#item-0d85b0) | minor update | チュートリアルリンクの修正 | modified | 1 | 1 | 2 | 
| [cognitive-search-predefined-skills.md](#item-81d522) | minor update | チュートリアルリンクの修正 | modified | 1 | 1 | 2 | 
| [skillset-csharp.md](#item-5ad1e5) | minor update | ファイル名の変更とリンクの修正 | renamed | 32 | 35 | 67 | 
| [skillset-rest.md](#item-a9668d) | minor update | ファイル名の変更とリンクの修正 | renamed | 21 | 28 | 49 | 
| [samples-dotnet.md](#item-12f3fa) | minor update | チュートリアルリンクの更新 | modified | 1 | 1 | 2 | 
| [samples-rest.md](#item-198ebc) | minor update | チュートリアルリンクの更新 | modified | 1 | 1 | 2 | 
| [search-get-started-skillset.md](#item-079744) | minor update | チュートリアルリンクの更新 | modified | 1 | 1 | 2 | 
| [search-howto-incremental-index.md](#item-d98619) | minor update | チュートリアルリンクの更新 | modified | 2 | 2 | 4 | 
| [search-howto-reindex.md](#item-46738a) | minor update | チュートリアルリンクの更新 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c4768f) | minor update | ナビゲーションメニューの更新 | modified | 2 | 4 | 6 | 
| [tutorial-skillset.md](#item-8e61e7) | new feature | 新しいスキルセットのチュートリアル | added | 25 | 0 | 25 | 


# Modified Contents
## articles/search/.openpublishing.redirection.search.json{#item-8b66f9}

<details>
<summary>Diff</summary>
````diff
@@ -9,6 +9,16 @@
             "source_path_from_root": "/articles/search/cognitive-search-quickstart-blob.md",
             "redirect_url": "/azure/search/search-get-started-skillset",
             "redirect_document_id": true
+        },
+                {
+            "source_path_from_root": "/articles/search/cognitive-search-tutorial-blob.md",
+            "redirect_url": "/azure/search/tutorial-skillset",
+            "redirect_document_id": true
+        },
+        {
+            "source_path_from_root": "/articles/search/cognitive-search-tutorial-blob-dotnet.md",
+            "redirect_url": "/azure/search/tutorial-skillset",
+            "redirect_document_id": false
         },
         {
             "source_path_from_root": "/articles/search/search-howto-connecting-azure-sql-database-to-azure-search-using-indexers.md",
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
このコードの変更は、`articles/search/.openpublishing.redirection.search.json`ファイルにおいて、リダイレクト設定を追加したものです。具体的には、3つの新しいリダイレクトエントリが追加されました。これにより、特定のドキュメントから新しいURLへのリダイレクトが可能になります。`source_path_from_root`フィールドは元のドキュメントのパスを示し、`redirect_url`フィールドはリダイレクト先の新しいパスを提供します。また、`redirect_document_id`フィールドは、リダイレクトがドキュメントIDを持つかどうかを示すブール値として新たに追加されています。この変更は、ユーザーが古いURLから新しいURLへの移行を容易にするためのマイナーな更新です。

## articles/search/chat-completion-skill-example-usage.md{#item-21e090}

<details>
<summary>Diff</summary>
````diff
@@ -117,7 +117,7 @@ This section supplements the [skill reference](cognitive-search-defining-skillse
 Once the basic framework of your skillset is created and Azure AI services is configured, you can focus on each individual image skill, defining inputs and source context, and mapping outputs to fields in either an index or knowledge store.
 
 > [!NOTE]
-> For an example skillset that combines image processing with downstream natural language processing, see [REST Tutorial: Use REST and AI to generate searchable content from Azure blobs](cognitive-search-tutorial-blob.md). It shows how to feed skill imaging output into entity recognition and key phrase extraction.
+> For an example skillset that combines image processing with downstream natural language processing, see [REST Tutorial: Use REST and AI to generate searchable content from Azure blobs](tutorial-skillset.md). It shows how to feed skill imaging output into entity recognition and key phrase extraction.
 
 ### Example inputs for image processing
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルリンクの修正"
}
```

### Explanation
このコードの変更は、`articles/search/chat-completion-skill-example-usage.md`ファイルにおけるリファレンスリンクの修正を含んでいます。具体的には、特定のスキルセットに関する外部リンクが更新されました。元のリンクは`cognitive-search-tutorial-blob.md`から`tutorial-skillset.md`に変更されています。この変更により、ユーザーは最新のチュートリアルにアクセスできるようになります。全体として、この更新は情報の正確性を高め、ユーザーが適切なリソースに導かれることを目的としたマイナーな修正です。

## articles/search/cognitive-search-concept-image-scenarios.md{#item-606953}

<details>
<summary>Diff</summary>
````diff
@@ -166,7 +166,7 @@ This section supplements the [skill reference](cognitive-search-predefined-skill
 Once the basic framework of your skillset is created and Azure AI services is configured, you can focus on each individual image skill, defining inputs and source context, and mapping outputs to fields in either an index or knowledge store.
 
 > [!NOTE]
-> For an example skillset that combines image processing with downstream natural language processing, see [REST Tutorial: Use REST and AI to generate searchable content from Azure blobs](cognitive-search-tutorial-blob.md). It shows how to feed skill imaging output into entity recognition and key phrase extraction.
+> For an example skillset that combines image processing with downstream natural language processing, see [REST Tutorial: Use REST and AI to generate searchable content from Azure blobs](tutorial-skillset.md). It shows how to feed skill imaging output into entity recognition and key phrase extraction.
 
 ### Inputs for image processing
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルリンクの修正"
}
```

### Explanation
このコードの変更は、`articles/search/cognitive-search-concept-image-scenarios.md`ファイルにおけるリファレンスリンクの修正に関するものです。具体的には、画像処理と自然言語処理を組み合わせたスキルセットの具体例が示されているリンクが、`cognitive-search-tutorial-blob.md`から`tutorial-skillset.md`に変更されました。この変更により、ユーザーは常に最新の関連情報にアクセスできるようになります。このマイナーな修正は、情報の正確性を向上させ、ユーザーが適切なリソースを参照できるようにすることを目的としています。

## articles/search/cognitive-search-concept-intro.md{#item-bf9ed7}

<details>
<summary>Diff</summary>
````diff
@@ -135,7 +135,7 @@ To repeat any of the above steps, [reset the indexer](search-howto-reindex.md) b
 ## Next steps
 
 + [Quickstart: Create a skillset for AI enrichment](search-get-started-skillset.md)
-+ [Tutorial: Learn about the AI enrichment REST APIs](cognitive-search-tutorial-blob.md)
++ [Tutorial: Learn about the AI enrichment REST APIs](tutorial-skillset.md)
 + [Skillset concepts](cognitive-search-working-with-skillsets.md)
 + [Knowledge store concepts](knowledge-store-concept-intro.md)
 + [Create a skillset](cognitive-search-defining-skillset.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルリンクの修正"
}
```

### Explanation
このコードの変更は、`articles/search/cognitive-search-concept-intro.md`ファイルにおけるリファレンスリンクの修正を反映しています。具体的には、AIエンリッチメントに関するREST APIのチュートリアルリンクが、`cognitive-search-tutorial-blob.md`から`tutorial-skillset.md`に変更されました。この変更により、ユーザーはより関連性の高い情報にアクセスできるようになります。このマイナーな修正は、ドキュメントの正確性を保つための重要な更新であり、ユーザーが最新のリソースを使用できるようにすることを目的としています。

## articles/search/cognitive-search-concept-troubleshooting.md{#item-0d85b0}

<details>
<summary>Diff</summary>
````diff
@@ -71,7 +71,7 @@ For [parallel indexing](search-howto-large-index.md), distribute your data into
 ## See also
 
 + [Quickstart: Create an AI enrichment pipeline in the Azure portal](search-get-started-skillset.md)
-+ [Tutorial: Learn AI enrichment REST APIs](cognitive-search-tutorial-blob.md)
++ [Tutorial: Learn AI enrichment REST APIs](tutorial-skillset.md)
 + [How to configure blob indexers](search-howto-indexing-azure-blob-storage.md)
 + [How to define a skillset](cognitive-search-defining-skillset.md)
 + [How to map enriched fields to an index](cognitive-search-output-field-mapping.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルリンクの修正"
}
```

### Explanation
このコードの変更は、`articles/search/cognitive-search-concept-troubleshooting.md`ファイルにおけるリンクの修正を示しています。具体的には、AIエンリッチメントに関するREST APIのチュートリアルリンクが、`cognitive-search-tutorial-blob.md`から`tutorial-skillset.md`に変更されました。この変更により、読者はより適切で関連する情報にアクセスできるようになります。このマイナーな更新は、ドキュメントの正確性を維持し、ユーザーが適切なリソースを利用できるようにすることを目的としています。

## articles/search/cognitive-search-predefined-skills.md{#item-81d522}

<details>
<summary>Diff</summary>
````diff
@@ -81,4 +81,4 @@ For guidance on creating a custom skill, see [Define a custom interface](cogniti
 
 + [How to define a skillset](cognitive-search-defining-skillset.md)
 + [Custom Skills interface definition](cognitive-search-custom-skill-interface.md)
-+ [Tutorial: Enriched indexing with AI](cognitive-search-tutorial-blob.md)
++ [Tutorial: Enriched indexing with AI](tutorial-skillset.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルリンクの修正"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-predefined-skills.md`ファイルにおいて、エンリッチされたインデックス作成に関するチュートリアルリンクの修正を示しています。具体的には、リンクが`cognitive-search-tutorial-blob.md`から`tutorial-skillset.md`に変更されました。この変更により、ユーザーはより関連性の高いリソースにアクセスできるようになります。マイナーな内容ではありますが、正確な情報提供を目的としており、利用者が最新の内容に基づいてスキルセットを定義できるようにするための重要な更新です。

## articles/search/includes/tutorials/skillset-csharp.md{#item-5ad1e5}

<details>
<summary>Diff</summary>
````diff
@@ -1,24 +1,13 @@
 ---
-title: 'Tutorial: Skillsets Using C#'
-titleSuffix: Azure AI Search
-description: Use C# and the Azure SDK for .NET to create skillsets. This skillset applies AI transformations and analyses to create searchable content from images and unstructured text.
-
+manager: nitinme
 author: HeidiSteen
 ms.author: heidist
-manager: nitinme
-
 ms.service: azure-ai-search
-ms.topic: tutorial
+ms.topic: include
 ms.date: 07/11/2025
-ms.custom:
-  - devx-track-csharp
-  - devx-track-dotnet
-  - ignite-2023
 ---
 
-# C# Tutorial: Use skillsets to generate searchable content in Azure AI Search
-
-Learn how to use the [Azure SDK for .NET](https://www.nuget.org/packages/Azure.Search.Documents/) to create an [AI enrichment pipeline](cognitive-search-concept-intro.md) for content extraction and transformations during indexing.
+Learn how to use the [Azure SDK for .NET](https://www.nuget.org/packages/Azure.Search.Documents/) to create an [AI enrichment pipeline](../../cognitive-search-concept-intro.md) for content extraction and transformations during indexing.
 
 Skillsets add AI processing to raw content, making it more uniform and searchable. Once you know how skillsets work, you can support a broad range of transformations, from image analysis to natural language processing to customized processing that you provide externally.
 
@@ -34,17 +23,17 @@ In this tutorial, you:
 
 This tutorial uses C# and the [**Azure.Search.Documents**](/dotnet/api/overview/azure/search.documents-readme) client library to create a data source, index, indexer, and skillset.
 
-The [indexer](search-indexer-overview.md) drives each step in the pipeline, starting with content extraction of sample data (unstructured text and images) in a blob container on Azure Storage.
+The [indexer](../../search-indexer-overview.md) drives each step in the pipeline, starting with content extraction of sample data (unstructured text and images) in a blob container on Azure Storage.
 
-Once content is extracted, the [skillset](cognitive-search-working-with-skillsets.md) executes built-in skills from Microsoft to find and extract information. These skills include Optical Character Recognition (OCR) on images, language detection on text, key phrase extraction, and entity recognition (organizations). New information created by the skillset is sent to fields in an [index](search-what-is-an-index.md). Once the index is populated, you can use the fields in queries, facets, and filters.
+Once content is extracted, the [skillset](../../cognitive-search-working-with-skillsets.md) executes built-in skills from Microsoft to find and extract information. These skills include Optical Character Recognition (OCR) on images, language detection on text, key phrase extraction, and entity recognition (organizations). New information created by the skillset is sent to fields in an [index](../../search-what-is-an-index.md). Once the index is populated, you can use the fields in queries, facets, and filters.
 
 ## Prerequisites
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
 + [Azure Storage](/azure/storage/common/storage-account-create).
 
-+ [Azure AI Search](search-create-app-portal.md).
++ [Azure AI Search](../../search-create-service-portal.md).
 
 + [Azure.Search.Documents package](https://www.nuget.org/packages/Azure.Search.Documents).
 
@@ -77,7 +66,7 @@ Once content is extracted, the [skillset](cognitive-search-working-with-skillset
 
 ### Azure AI services
 
-Built-in AI enrichment is backed by Azure AI services, including Language service and Azure AI Vision for natural language and image processing. For small workloads like this tutorial, you can use the free allocation of 20 transactions per indexer. For larger workloads, [attach an Azure AI Services multi-region resource to a skillset](cognitive-search-attach-cognitive-services.md) for Standard pricing.
+Built-in AI enrichment is backed by Azure AI services, including Language service and Azure AI Vision for natural language and image processing. For small workloads like this tutorial, you can use the free allocation of 20 transactions per indexer. For larger workloads, [attach an Azure AI Services multi-region resource to a skillset](../../cognitive-search-attach-cognitive-services.md) for Standard pricing.
 
 ### Copy a search service URL and API key
 
@@ -237,29 +226,29 @@ SearchIndexerDataSourceConnection dataSource = CreateOrUpdateDataSource(indexerC
 
 Build and run the solution. Since this is your first request, check the Azure portal to confirm the data source was created in Azure AI Search. On the search service overview page, verify the Data Sources list has a new item. You might need to wait a few minutes for the Azure portal page to refresh.
 
-  ![Data sources tile in the Azure portal](./media/cognitive-search-tutorial-blob/data-source-tile.png "Data sources tile in the Azure portal")
+  ![Data sources tile in the Azure portal](../../media/cognitive-search-tutorial-blob/data-source-tile.png "Data sources tile in the Azure portal")
 
 ### Step 2: Create a skillset
 
-In this section, you define a set of enrichment steps that you want to apply to your data. Each enrichment step is called a *skill* and the set of enrichment steps, a *skillset*. This tutorial uses [built-in skills](cognitive-search-predefined-skills.md) for the skillset:
+In this section, you define a set of enrichment steps that you want to apply to your data. Each enrichment step is called a *skill* and the set of enrichment steps, a *skillset*. This tutorial uses [built-in skills](../../cognitive-search-predefined-skills.md) for the skillset:
 
-* [Optical Character Recognition](cognitive-search-skill-ocr.md) to recognize printed and handwritten text in image files.
+* [Optical Character Recognition](../../cognitive-search-skill-ocr.md) to recognize printed and handwritten text in image files.
 
-* [Text Merger](cognitive-search-skill-textmerger.md) to consolidate text from a collection of fields into a single "merged content" field.
+* [Text Merger](../../cognitive-search-skill-textmerger.md) to consolidate text from a collection of fields into a single "merged content" field.
 
-* [Language Detection](cognitive-search-skill-language-detection.md) to identify the content's language.
+* [Language Detection](../../cognitive-search-skill-language-detection.md) to identify the content's language.
 
-* [Entity Recognition](cognitive-search-skill-entity-recognition-v3.md) for extracting the names of organizations from content in the blob container.
+* [Entity Recognition](../../cognitive-search-skill-entity-recognition-v3.md) for extracting the names of organizations from content in the blob container.
 
-* [Text Split](cognitive-search-skill-textsplit.md) to break large content into smaller chunks before calling the key phrase extraction skill and the entity recognition skill. Key phrase extraction and entity recognition accept inputs of 50,000 characters or less. A few of the sample files need splitting up to fit within this limit.
+* [Text Split](../../cognitive-search-skill-textsplit.md) to break large content into smaller chunks before calling the key phrase extraction skill and the entity recognition skill. Key phrase extraction and entity recognition accept inputs of 50,000 characters or less. A few of the sample files need splitting up to fit within this limit.
 
-* [Key Phrase Extraction](cognitive-search-skill-keyphrases.md) to pull out the top key phrases.
+* [Key Phrase Extraction](../../cognitive-search-skill-keyphrases.md) to pull out the top key phrases.
 
 During initial processing, Azure AI Search cracks each document to extract content from different file formats. Text originating in the source file is placed into a generated `content` field, one for each document. As such, set the input as `"/document/content"` to use this text. Image content is placed into a generated `normalized_images` field, specified in a skillset as `/document/normalized_images/*`.
 
 Outputs can be mapped to an index, used as input to a downstream skill, or both as is the case with language code. In the index, a language code is useful for filtering. As an input, language code is used by text analysis skills to inform the linguistic rules around word breaking.
 
-For more information about skillset fundamentals, see [How to define a skillset](cognitive-search-defining-skillset.md).
+For more information about skillset fundamentals, see [How to define a skillset](../../cognitive-search-defining-skillset.md).
 
 ### OCR skill
 
@@ -634,13 +623,13 @@ To learn more about index concepts, see [Create Index (REST API)](/rest/api/sear
 
 ### Step 4: Create and run an indexer
 
-So far you have created a data source, a skillset, and an index. These three components become part of an [indexer](search-indexer-overview.md) that pulls each piece together into a single multi-phased operation. To tie these together in an indexer, you must define field mappings.
+So far you have created a data source, a skillset, and an index. These three components become part of an [indexer](../../search-indexer-overview.md) that pulls each piece together into a single multi-phased operation. To tie these together in an indexer, you must define field mappings.
 
 * The fieldMappings are processed before the skillset, mapping source fields from the data source to target fields in an index. If field names and types are the same at both ends, no mapping is required.
 
 * The outputFieldMappings are processed after the skillset, referencing sourceFieldNames that don't exist until document cracking or enrichment creates them. The targetFieldName is a field in an index.
 
-In addition to hooking up inputs to outputs, you can also use field mappings to flatten data structures. For more information, see [How to map enriched fields to a searchable index](cognitive-search-output-field-mapping.md).
+In addition to hooking up inputs to outputs, you can also use field mappings to flatten data structures. For more information, see [How to map enriched fields to a searchable index](../../cognitive-search-output-field-mapping.md).
 
 ```csharp
 private static SearchIndexer CreateDemoIndexer(SearchIndexerClient indexerClient, SearchIndexerDataSourceConnection dataSource, SearchIndexerSkillset skillSet, SearchIndex index)
@@ -784,17 +773,25 @@ CheckIndexerOverallStatus(indexerClient, demoIndexer);
 
 In Azure AI Search tutorial console apps, we typically add a 2-second delay before running queries that return results, but because enrichment takes several minutes to complete, we'll close the console app and use another approach instead.
 
-The easiest option is [Search explorer](search-explorer.md) in the Azure portal. You can first run an empty query that returns all documents, or a more targeted search that returns new field content created by the pipeline. 
+The easiest option is [Search Explorer](../../search-explorer.md) in the Azure portal. You can first run an empty query that returns all documents, or a more targeted search that returns new field content created by the pipeline. 
 
-1. In Azure portal, in the search Overview page, select **Indexes**.
+1. In the Azure portal, in the search service pages, expand **Search Management** > **Indexes**.
 
 1. Find **`demoindex`** in the list. It should have 14 documents. If the document count is zero, the indexer is either still running or the page hasn't been refreshed yet. 
 
-1. Select **`demoindex`**. Search explorer is the first tab.
+1. Select **`demoindex`**. Search Explorer is the first tab.
 
 1. Content is searchable as soon as the first document is loaded. To verify content exists, run an unspecified query by clicking **Search**. This query returns all currently indexed documents, giving you an idea of what the index contains.
 
-1. Next, paste in the following string for more manageable results: `search=*&$select=id, languageCode, organizations`
+1. For more manageable results, switch to JSON view and set parameters to select the fields:
+
+   ```json
+   {
+       "search": "*",
+       "count": true,
+       "select": "id, languageCode, organizations"
+   }
+   ```
 
 <a name="reset"></a>
 
@@ -808,7 +805,7 @@ The sample code for this tutorial checks for existing objects and deletes them s
 
 This tutorial demonstrated the basic steps for building an enriched indexing pipeline through the creation of component parts: a data source, skillset, index, and indexer.
 
-[Built-in skills](cognitive-search-predefined-skills.md) were introduced, along with skillset definition and the mechanics of chaining skills together through inputs and outputs. You also learned that `outputFieldMappings` in the indexer definition is required for routing enriched values from the pipeline into a searchable index on an Azure AI Search service.
+[Built-in skills](../../cognitive-search-predefined-skills.md) were introduced, along with skillset definition and the mechanics of chaining skills together through inputs and outputs. You also learned that `outputFieldMappings` in the indexer definition is required for routing enriched values from the pipeline into a searchable index on an Azure AI Search service.
 
 Finally, you learned how to test results and reset the system for further iterations. You learned that issuing queries against the index returns the output created by the enriched indexing pipeline. You also learned how to check indexer status, and which objects to delete before rerunning a pipeline.
 
@@ -823,4 +820,4 @@ You can find and manage resources in the Azure portal, using the All resources o
 Now that you're familiar with all of the objects in an AI enrichment pipeline, let's take a closer look at skillset definitions and individual skills.
 
 > [!div class="nextstepaction"]
-> [How to create a skillset](cognitive-search-defining-skillset.md)
+> [How to create a skillset](../../cognitive-search-defining-skillset.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイル名の変更とリンクの修正"
}
```

### Explanation
この変更は、`articles/search/includes/tutorials/skillset-csharp.md`ファイルへの適用を示しており、ファイル名が`cognitive-search-tutorial-blob-dotnet.md`から変更されています。ファイル名の変更に伴い、ドキュメント内のリンクも更新されました。主にAIエンリッチメントパイプラインの構築に関する内容が中心で、新しいリンクは相対パスに修正されて、より一貫性を持たせています。具体的には、チュートリアルの概要や手順において参照されているリソースやコンテンツが最新の状態を反映するように更新されています。この変更により、ユーザーはより正確でアクセスしやすい情報を得ることができます。

## articles/search/includes/tutorials/skillset-rest.md{#item-a9668d}

<details>
<summary>Diff</summary>
````diff
@@ -1,20 +1,13 @@
 ---
-title: 'Tutorial: Skillsets Using REST'
-titleSuffix: Azure AI Search
-description: Use the Search REST APIs to create skillsets. This skillset applies AI transformations and analyses to create searchable content from images and unstructured text.
-
+manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
-ms.custom:
-  - ignite-2023
-ms.topic: tutorial
-ms.date: 03/31/2025
+ms.topic: include
+ms.date: 07/11/2025
 ---
 
-# REST Tutorial: Use skillsets to generate searchable content in Azure AI Search
-
-Learn how to call REST APIs that create an [AI enrichment pipeline](cognitive-search-concept-intro.md) for content extraction and transformations during indexing.
+Learn how to call REST APIs that create an [AI enrichment pipeline](../../cognitive-search-concept-intro.md) for content extraction and transformations during indexing.
 
 Skillsets add AI processing to raw content, making it more uniform and searchable. Once you know how skillsets work, you can support a broad range of transformations, from image analysis to natural language processing to customized processing that you provide externally.
 
@@ -30,17 +23,17 @@ In this tutorial, you:
 
 This tutorial uses a REST client and the [Azure AI Search REST APIs](/rest/api/searchservice/) to create a data source, index, indexer, and skillset.
 
-The [indexer](search-indexer-overview.md) drives each step in the pipeline, starting with content extraction of sample data (unstructured text and images) in a blob container on Azure Storage.
+The [indexer](../../search-indexer-overview.md) drives each step in the pipeline, starting with content extraction of sample data (unstructured text and images) in a blob container on Azure Storage.
 
-Once content is extracted, the [skillset](cognitive-search-working-with-skillsets.md) executes built-in skills from Microsoft to find and extract information. These skills include Optical Character Recognition (OCR) on images, language detection on text, key phrase extraction, and entity recognition (organizations). New information created by the skillset is sent to fields in an [index](search-what-is-an-index.md). Once the index is populated, you can use the fields in queries, facets, and filters.
+Once content is extracted, the [skillset](../../cognitive-search-working-with-skillsets.md) executes built-in skills from Microsoft to find and extract information. These skills include Optical Character Recognition (OCR) on images, language detection on text, key phrase extraction, and entity recognition (organizations). New information created by the skillset is sent to fields in an [index](../../search-what-is-an-index.md). Once the index is populated, you can use the fields in queries, facets, and filters.
 
 ## Prerequisites
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
 + [Azure Storage](/azure/storage/common/storage-account-create)
 
-+ [Azure AI Search](search-create-app-portal.md)
++ [Azure AI Search](../../search-create-service-portal.md)
 
 + [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
 
@@ -73,7 +66,7 @@ Download a zip file of the sample data repository and extract the contents. [Lea
 
 ### Azure AI services
 
-Built-in AI enrichment is backed by Azure AI services, including Language service and Azure AI Vision for natural language and image processing. For small workloads like this tutorial, you can use the free allocation of twenty transactions per indexer. For larger workloads, [attach an Azure AI Services multi-region resource to a skillset](cognitive-search-attach-cognitive-services.md) for Standard pricing.
+Built-in AI enrichment is backed by Azure AI services, including Language service and Azure AI Vision for natural language and image processing. For small workloads like this tutorial, you can use the free allocation of twenty transactions per indexer. For larger workloads, [attach an Azure AI Services multi-region resource to a skillset](../../cognitive-search-attach-cognitive-services.md) for Standard pricing.
 
 ### Copy a search service URL and API key
 
@@ -83,11 +76,11 @@ For this tutorial, connections to Azure AI Search require an endpoint and an API
 
 1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
 
-   :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
+   :::image type="content" source="../../media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
 
 ## Set up your REST file
 
-1. Start Visual Studio Code and open the [skillset-tutorial.rest](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skillset-tutorial) file. See [Quickstart: Full-text search](search-get-started-text.md) if you need help with the REST client.
+1. Start Visual Studio Code and open the [skillset-tutorial.rest](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skillset-tutorial) file. See [Quickstart: Full-text search](../../search-get-started-text.md) if you need help with the REST client.
 
 1. Provide values for the variables: search service endpoint, search service admin API key, an index name, a connection string to your Azure Storage account, and the blob container name.
 
@@ -295,19 +288,19 @@ POST {{baseUrl}}/skillsets?api-version=2024-07-01  HTTP/1.1
 
    | Skill                 | Description    |
    |-----------------------|----------------|
-   | [Optical Character Recognition](cognitive-search-skill-ocr.md) | Recognizes text and numbers in image files. |
-   | [Text Merge](cognitive-search-skill-textmerger.md)  | Creates "merged content" that recombines previously separated content, useful for documents with embedded images (PDF, DOCX, and so forth). Images and text are separated during the document cracking phase. The merge skill recombines them by inserting any recognized text, image captions, or tags created during enrichment into the same location where the image was extracted from in the document. </p>When you're working with merged content in a skillset, this node is inclusive of all text in the document, including text-only documents that never undergo OCR or image analysis. |
-   | [Language Detection](cognitive-search-skill-language-detection.md) | Detects the language and outputs either a language name or code. In multilingual data sets, a language field can be useful for filters. |
-   | [Entity Recognition](cognitive-search-skill-entity-recognition-v3.md) | Extracts the names of people, organizations, and locations from merged content. |
-   | [Text Split](cognitive-search-skill-textsplit.md)  | Breaks large merged content into smaller chunks before calling the key phrase extraction skill. Key phrase extraction accepts inputs of 50,000 characters or less. A few of the sample files need splitting up to fit within this limit. |
-   | [Key Phrase Extraction](cognitive-search-skill-keyphrases.md) | Pulls out the top key phrases.|
+   | [Optical Character Recognition](../../cognitive-search-skill-ocr.md) | Recognizes text and numbers in image files. |
+   | [Text Merge](../../cognitive-search-skill-textmerger.md)  | Creates "merged content" that recombines previously separated content, useful for documents with embedded images (PDF, DOCX, and so forth). Images and text are separated during the document cracking phase. The merge skill recombines them by inserting any recognized text, image captions, or tags created during enrichment into the same location where the image was extracted from in the document. </p>When you're working with merged content in a skillset, this node is inclusive of all text in the document, including text-only documents that never undergo OCR or image analysis. |
+   | [Language Detection](../../cognitive-search-skill-language-detection.md) | Detects the language and outputs either a language name or code. In multilingual data sets, a language field can be useful for filters. |
+   | [Entity Recognition](../../cognitive-search-skill-entity-recognition-v3.md) | Extracts the names of people, organizations, and locations from merged content. |
+   | [Text Split](../../cognitive-search-skill-textsplit.md)  | Breaks large merged content into smaller chunks before calling the key phrase extraction skill. Key phrase extraction accepts inputs of 50,000 characters or less. A few of the sample files need splitting up to fit within this limit. |
+   | [Key Phrase Extraction](../../cognitive-search-skill-keyphrases.md) | Pulls out the top key phrases.|
 
 + Each skill executes on the content of the document. During processing, Azure AI Search cracks each document to read content from different file formats. Found text originating in the source file is placed into a generated `content` field, one for each document. As such, the input becomes `"/document/content"`.
 
 + For key phrase extraction, because we use the text splitter skill to break larger files into pages, the context for the key phrase extraction skill is `"document/pages/*"` (for each page in the document) instead of `"/document/content"`.
 
 > [!NOTE]
-> Outputs can be mapped to an index, used as input to a downstream skill, or both as is the case with language code. In the index, a language code is useful for filtering. For more information about skillset fundamentals, see [How to define a skillset](cognitive-search-defining-skillset.md).
+> Outputs can be mapped to an index, used as input to a downstream skill, or both as is the case with language code. In the index, a language code is useful for filtering. For more information about skillset fundamentals, see [How to define a skillset](../../cognitive-search-defining-skillset.md).
 
 ### Step 3: Create an index
 
@@ -545,19 +538,19 @@ POST {{baseUrl}}/indexes/cog-search-demo-idx/docs/search?api-version=2024-07-01
   }
 ```
 
-These queries illustrate a few of the ways you can work with query syntax and filters on new fields created by Azure AI Search. For more query examples, see [Examples in Search Documents REST API](/rest/api/searchservice/documents/search-post#examples), [Simple syntax query examples](search-query-simple-examples.md), and [Full Lucene query examples](search-query-lucene-examples.md).
+These queries illustrate a few of the ways you can work with query syntax and filters on new fields created by Azure AI Search. For more query examples, see [Examples in Search Documents REST API](/rest/api/searchservice/documents/search-post#examples), [Simple syntax query examples](../../search-query-simple-examples.md), and [Full Lucene query examples](../../search-query-lucene-examples.md).
 
 <a name="reset"></a>
 
 ## Reset and rerun
 
-During early stages of development, iteration over the design is common. [Reset and rerun](search-howto-run-reset-indexers.md) helps with iteration.
+During early stages of development, iteration over the design is common. [Reset and rerun](../../search-howto-run-reset-indexers.md) helps with iteration.
 
 ## Takeaways
 
 This tutorial demonstrates the basic steps for using the REST APIs to create an AI enrichment pipeline: a data source, skillset, index, and indexer.
 
-[Built-in skills](cognitive-search-predefined-skills.md) were introduced, along with skillset definition that shows the mechanics of chaining skills together through inputs and outputs. You also learned that `outputFieldMappings` in the indexer definition is required for routing enriched values from the pipeline into a searchable index on an Azure AI Search service.
+[Built-in skills](../../cognitive-search-predefined-skills.md) were introduced, along with skillset definition that shows the mechanics of chaining skills together through inputs and outputs. You also learned that `outputFieldMappings` in the indexer definition is required for routing enriched values from the pipeline into a searchable index on an Azure AI Search service.
 
 Finally, you learned how to test results and reset the system for further iterations. You learned that issuing queries against the index returns the output created by the enriched indexing pipeline.
 
@@ -572,4 +565,4 @@ You can find and manage resources in the Azure portal, using the All resources o
 Now that you're familiar with all of the objects in an AI enrichment pipeline, take a closer look at skillset definitions and individual skills.
 
 > [!div class="nextstepaction"]
-> [How to create a skillset](cognitive-search-defining-skillset.md)
+> [How to create a skillset](../../cognitive-search-defining-skillset.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイル名の変更とリンクの修正"
}
```

### Explanation
この変更は、`articles/search/includes/tutorials/skillset-rest.md`ファイルのファイル名が`cognitive-search-tutorial-blob.md`から変更されたことを示しています。同時に、ドキュメントの内容もいくつか改訂されており、特にリンクが相対パスに修正されています。これにより、REST APIを使用してAIエンリッチメントパイプラインを作成する際の手順や、必要な条件についての最新情報が提供されています。具体的には、インデックスやスキルセットの作成方法、Azureサービスの利用に関する詳細なガイダンスが含まれており、ユーザーがより明確に情報を得ることができるようになっています。このマイナーな更新により、全体の整合性が向上し、使いやすさも強化されています。

## articles/search/samples-dotnet.md{#item-12f3fa}

<details>
<summary>Diff</summary>
````diff
@@ -56,7 +56,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. A
 | [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) | [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md) | Creates a knowledge agent in Azure AI Search to integrate LLM reasoning into query planning. |
 | [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-search/) | [Quickstart: Semantic ranking using the Azure SDKs](search-get-started-semantic.md) | Shows the index schema and query request for invoking semantic ranker. |
 | [search-website](https://github.com/Azure-Samples/azure-search-static-web-app) | [Tutorial: Add search to web apps](tutorial-csharp-overview.md) | Demonstrates an end-to-end search app that includes bulk upload using the push APIs and a rich client for hosting the app and handling search requests.|
-| [tutorial-ai-enrichment](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/tutorial-ai-enrichment)  | [Tutorial: AI-generated searchable content from Azure blobs](cognitive-search-tutorial-blob-dotnet.md) | Shows how to configure an indexer and skillset. |
+| [tutorial-ai-enrichment](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/tutorial-ai-enrichment)  | [Tutorial: AI-generated searchable content from Azure blobs](tutorial-skillset.md) | Shows how to configure an indexer and skillset. |
 | [multiple-data-sources](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources)  | [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md) | Merges content from two data sources into one search index. |
 | [Optimize-data-indexing](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/optimize-data-indexing) | [Tutorial: Optimize indexing with the push API](tutorial-optimize-indexing-push-api.md) | Demonstrates optimization techniques for pushing data into a search index. |
 | [DotNetHowTo](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowTo)  | [How to use the .NET client library](search-howto-dotnet-sdk.md) | Steps through the basic workflow, but in more detail and with discussion of API usage.  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルリンクの更新"
}
```

### Explanation
この変更は、`articles/search/samples-dotnet.md`ファイルにおける1つの行の更新を示しています。具体的には、AIエンリッチメントに関連するチュートリアルのリンクが変更されました。もともと、`cognitive-search-tutorial-blob-dotnet.md`にリンクされていた部分が`tutorial-skillset.md`に修正されています。この更新により、関連するチュートリアルが最新の情報を反映するようになり、Azure AI Searchを使用する開発者にとっての利便性が向上しました。全体的に、ドキュメントの整合性と信頼性が強化されています。

## articles/search/samples-rest.md{#item-198ebc}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. M
 | [quickstart](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart) | Source code for the REST portion of [Quickstart: Full-text search](search-get-started-text.md). This sample covers the basic workflow for creating, loading, and querying a search index using sample data. |
 | [quickstart-vectors](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) | Source code for [Quickstart: Vector search using REST APIs](search-get-started-vector.md). This sample covers the basic workflow for indexing and querying vector data. |
 | [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-agentic-retrieval) | Source code for the REST portion of [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md). This sample shows you how to create a knowledge agent in Azure AI Search to integrate LLM reasoning into query planning. |
-| [skillset-tutorial](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skillset-tutorial) | Source code for [Tutorial: Use REST and AI to generate searchable content from Azure blobs](cognitive-search-tutorial-blob.md). This sample shows you how to create a skillset that iterates over Azure blobs to extract information and infer structure.|
+| [skillset-tutorial](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skillset-tutorial) | Source code for [Tutorial: Use REST and AI to generate searchable content from Azure blobs](tutorial-skillset.md). This sample shows you how to create a skillset that iterates over Azure blobs to extract information and infer structure.|
 | [skill examples](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skill-examples) | Skillset examples in indexer pipelines that include indexes and indexers so that you can follow field mappings, output field mappings, and source paths. |
 | [debug-sessions](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Debug-sessions) | Source code for [Tutorial: Diagnose, repair, and commit changes to your skillset](cognitive-search-tutorial-debug-sessions.md). This sample shows you how to use a skillset debug session in the Azure portal. REST is used to create the objects used during debug.|
 | [custom-analyzers](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/custom-analyzers) | Source code for [Tutorial: Create a custom analyzer for phone numbers](tutorial-create-custom-analyzer.md). This sample explains how to use analyzers to preserve patterns and special characters in searchable content.|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルリンクの更新"
}
```

### Explanation
この変更は、`articles/search/samples-rest.md`ファイルにおける1つの行の更新を示しています。具体的には、AIエンリッチメントに関連するチュートリアルのリンクが修正されました。もともとは`cognitive-search-tutorial-blob.md`にリンクされていた部分が`tutorial-skillset.md`に変更されています。この更新により、関連するチュートリアルが最新の情報を反映するようになり、Azure REST APIを使用する開発者にとって、より有用なリソースを提供することが目的とされています。全体的に、ドキュメントの整合性と信頼性が向上しています。

## articles/search/search-get-started-skillset.md{#item-079744}

<details>
<summary>Diff</summary>
````diff
@@ -195,4 +195,4 @@ If you used a free service, remember that you're limited to three indexes, index
 You can create skillsets using the Azure portal, .NET SDK, or REST API. To further your knowledge, try the REST API by using a REST client and more sample data:
 
 > [!div class="nextstepaction"]
-> [Tutorial: Use skillsets to generate searchable content in Azure AI Search](cognitive-search-tutorial-blob.md)
+> [Tutorial: Use skillsets to generate searchable content in Azure AI Search](tutorial-skillset.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルリンクの更新"
}
```

### Explanation
この変更は、`articles/search/search-get-started-skillset.md`ファイル内での1つのリンクの更新を示しています。具体的には、AIスキルセットを使用してAzure AI Searchで検索可能なコンテンツを生成するためのチュートリアルリンクが修正されました。以前は`cognitive-search-tutorial-blob.md`というファイルにリンクされていましたが、最新の情報を反映するために`tutorial-skillset.md`に変更されました。この更新により、ユーザーがより関連性の高い情報にアクセスできるようになり、Azureのスキルセットの導入方法に関する理解が深まることを目的としています。全体的に、この修正はドキュメントの質を向上させています。

## articles/search/search-howto-incremental-index.md{#item-d98619}

<details>
<summary>Diff</summary>
````diff
@@ -174,7 +174,7 @@ To verify whether the cache is operational, modify a skillset and run the indexe
 
 Skillsets that include image analysis and Optical Character Recognition (OCR) of scanned documents make good test cases. If you modify a downstream text skill or any skill that isn't image-related, the indexer can retrieve all of the previously processed image and OCR content from cache, updating and processing only the text-related changes indicated by your edits.  You can expect to see fewer documents in the indexer execution document count, shorter execution times, and fewer charges on your bill. 
 
-The [file set](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/ai-enrichment-mixed-media) used in [cog-search-demo tutorials](cognitive-search-tutorial-blob.md) is a useful test case because it contains 14 files of various formats JPG, PNG, HTML, DOCX, PPTX, and other types. Change `en` to `es` or another language in the text translation skill for proof-of-concept testing of incremental enrichment.
+The [file set](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/ai-enrichment-mixed-media) used in [cog-search-demo tutorials](tutorial-skillset.md) is a useful test case because it contains 14 files of various formats JPG, PNG, HTML, DOCX, PPTX, and other types. Change `en` to `es` or another language in the text translation skill for proof-of-concept testing of incremental enrichment.
 
 ## Common errors
 
@@ -191,4 +191,4 @@ Incremental enrichment is applicable on indexers that contain skillsets, providi
 + [Incremental enrichment (lifecycle and management)](cognitive-search-incremental-indexing-conceptual.md)
 + [Skillset concepts and composition](cognitive-search-working-with-skillsets.md)
 + [Create a skillset](cognitive-search-defining-skillset.md)
-+ [Tutorial: Use REST and AI to generate searchable content from Azure blobs](cognitive-search-tutorial-blob.md)
++ [Tutorial: Use REST and AI to generate searchable content from Azure blobs](tutorial-skillset.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルリンクの更新"
}
```

### Explanation
この変更は、`articles/search/search-howto-incremental-index.md`ファイルにおけるいくつかのリンクの修正を示しています。具体的には、特定のチュートリアルに関連するリンクが更新されました。もともとは`cognitive-search-tutorial-blob.md`というファイルにリンクされていましたが、最新の情報を反映させるために`tutorial-skillset.md`に変更されています。この変更により、ユーザーはより関連性の高いチュートリアル情報にアクセスできるようになり、AIスキルセットについての理解が深まることを目的としています。また、ファイルセットの説明文にもリンクの変更が反映されており、テストケースとしての有用性を強調しています。この修正は、情報の一貫性と信頼性を向上させるために重要です。

## articles/search/search-howto-reindex.md{#item-46738a}

<details>
<summary>Diff</summary>
````diff
@@ -327,7 +327,7 @@ Deleting a document doesn't immediately free up space in the index. Every few mi
 
 1. Check the values of the document key field: `search=*&$select=HotelId`. A simple string is straightforward, but if the index uses a base-64 encoded field, or if search documents were generated from a `parsingMode` setting, you might be working with values that you aren't familiar with.
 
-1. [Look up the document](/rest/api/searchservice/documents/get) to verify the value of the document ID and to review its content before deleting it. Specify the key or document ID in the request. The following examples illustrate a simple string for the [Hotels sample index](search-get-started-portal.md) and a base-64 encoded string for the metadata_storage_path key of the [cog-search-demo index](cognitive-search-tutorial-blob.md).
+1. [Look up the document](/rest/api/searchservice/documents/get) to verify the value of the document ID and to review its content before deleting it. Specify the key or document ID in the request. The following examples illustrate a simple string for the [Hotels sample index](search-get-started-portal.md) and a base-64 encoded string for the metadata_storage_path key of the [cog-search-demo index](tutorial-skillset.md).
 
     ```http
     GET https://[service name].search.windows.net/indexes/hotel-sample-index/docs/1111?api-version=2024-07-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルリンクの更新"
}
```

### Explanation
この変更は、`articles/search/search-howto-reindex.md`ファイル内のリンク修正を反映しています。具体的には、特定のチュートリアルに関連するリンクが更新されました。もともとは`cognitive-search-tutorial-blob.md`というファイルにリンクされていたところが、最新の情報に基づいて`tutorial-skillset.md`に変更されました。この変更により、該当するドキュメントの内容がより関連性の高い情報にリダイレクトされ、ユーザーが適切な資料を参照しやすくなっています。また、この修正は、ドキュメントの整合性を確保し、ユーザーが適切なプロセスを理解するのに役立ちます。全体として、この修正は、Azureでの再インデックス処理に関する情報の品質を向上させています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -180,10 +180,8 @@ items:
       href: tutorial-rag-build-solution-minimize-storage.md
   - name: Skills tutorials
     items:
-    - name: C#
-      href: cognitive-search-tutorial-blob-dotnet.md
-    - name: REST
-      href: cognitive-search-tutorial-blob.md
+    - name: Create a skillset
+      href: tutorial-skillset.md
     - name: Debug a skillset
       href: cognitive-search-tutorial-debug-sessions.md
 - name: How-to guides
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナビゲーションメニューの更新"
}
```

### Explanation
この変更は、`articles/search/toc.yml`ファイルの更新を示しており、ナビゲーションメニューの項目が修正されています。具体的には、「Skills tutorials」セクションからC#およびRESTのチュートリアルリンクが削除され、新たに「Create a skillset」というチュートリアルが追加されました。この変更は、関連するスキルセットの作成に関する情報を強調することを目的としており、ユーザーが最新のガイドラインに従ってスキルセットを作成する手助けとなるでしょう。また、情報を整理し、より重要な内容に焦点を当てることで、ユーザーエクスペリエンスの向上を図っています。全体として、この修正は、Azureのチュートリアルに関するナビゲーションをより明確で効果的なものにするためのものです。

## articles/search/tutorial-skillset.md{#item-8e61e7}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,25 @@
+---
+title: "Tutorial: Skillsets"
+titleSuffix: Azure AI Search
+description: Learn how to create a skillset that calls built-in skills to enrich content during indexing.
+author: heidisteen
+ms.author: heidist
+ms.service: azure-ai-search
+ms.topic: tutorial
+ms.date: 7/11/2025
+zone_pivot_groups: tutorial-create-skillset
+---
+
+# Quickstart: Skillsets in Azure AI Search
+
+::: zone pivot="csharp"
+
+[!INCLUDE [C# quickstart](includes/tutorials/skillset-csharp.md)]
+
+::: zone-end
+
+::: zone pivot="rest"
+
+[!INCLUDE [REST quickstart](includes/tutorials/skillset-rest.md)]
+
+::: zone-end
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しいスキルセットのチュートリアル"
}
```

### Explanation
この変更は、新たに`articles/search/tutorial-skillset.md`というファイルが追加され、Azure AI Searchにおけるスキルセットの作成方法を学ぶためのチュートリアルが含まれています。このドキュメントは、インデックス作成中にコンテンツを強化するためにビルトインスキルを呼び出すスキルセットを作成する手順を説明しています。また、C#およびRESTのクイックスタートが盛り込まれており、ユーザーは自分の環境に合わせた言語でスキルセットを簡単に作成できるようになります。さらに、ドキュメントでは、著者情報やトピック、日付などのメタデータも含まれており、内容の蓄積と更新が明確に示されています。この新しいチュートリアルは、ユーザーがAI検索機能を活用するための重要なステップを提供し、Azureサービスの活用を高めることを目的としています。


