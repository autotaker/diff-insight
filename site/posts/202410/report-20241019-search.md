---
date: '2024-10-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6e9a4a2...MicrosoftDocs:418033b
summary: この変更では、複数のAzure AI Search関連のドキュメントがマイナーアップデートされ、主に技術に適応した内容や最新の日付への更新が行われました。具体的には、ドキュメント内の表現改善や最新のサンプルコードの追加・更新が行われ、ブランドの一貫性とユーザーエクスペリエンスの向上が図られています。また、特定のサンプルリンクの更新により、古い情報に基づくコードが問題を引き起こす可能性がありますが、全体としてこれらの変更はユーザーがAzure
  AI Searchを効果的に活用できるように情報を整備する目的で行われています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6e9a4a2...MicrosoftDocs:418033b){target="_blank"}

# Highlights
この変更では、複数のAzure AI Search関連のドキュメントがマイナーアップデートされました。主な強調点としては、新しい技術に適応した内容や最新の日付への更新、情報の一貫性と明確性の向上があります。技術的な用語や説明が改善され、ユーザーエクスペリエンスの向上が図られています。

## New features
- 各ドキュメントにおけるタイトルや説明の表現が改善され、ユーザーがより理解しやすい形になっています。
- PythonやJavaScriptなど、各言語ごとは最新のサンプルやリンクが追加・更新され、最新技術に対応しています。

## Breaking changes
- 特定のサンプルリンクや技術情報が更新されているため、これらの変更により、古い情報に基づいたコードは問題を引き起こす可能性があります。

## Other updates
- 日付の更新により、最新情報の反映が確認されています。
- メタデータの修正により、ドキュメントの分類がより現実的に整理されました。

# Insights
Azure AI Searchに関連するドキュメントの一連の更新は、ユーザーがサービスを最大限に活用できるよう情報を整備・強化することを目的としています。その中で特に目立つのは、AI技術を活用した新しい機能や技術用語の明確化です。

例えば、「cognitive-search-concept-image-scenarios.md」では、AI強化による画像からのテキスト抽出機能が強調され、ユーザーが画像処理を効果的に利用する方法について理解を深めることができます。また、「index-add-scoring-profiles.md」では、セマンティックランキングの導入が紹介され、ユーザーが検索結果の関連性を高める手法として活用できるようになっています。

さらに、各言語のサンプルドキュメントは、最新のSDKやテストケースへのリンクを含むように更新されており、開発者が具体的な実装に焦点を当てた内容を参照しやすくなっています。API利用者にとっても、RESTサンプルの更新により、APIの使用方法がさらにクリアになり、実際のプロジェクトでの適用が容易になります。

全体として、これらのドキュメント更新は、Azure AI Searchの機能に関する理解を促進し、ユーザーが最新のテクノロジーを効果的に利用する手助けとなっています。これは、技術の発展に伴いユーザーのニーズを満たすための、必要不可欠な対応であると言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-concept-image-scenarios.md](#item-606953) | minor update | 画像処理の手法に関する内容の更新 | modified | 52 | 52 | 104 | 
| [cognitive-search-output-field-mapping.md](#item-31fe9c) | minor update | 出力フィールドマッピングのタイトルと内容の更新 | modified | 19 | 19 | 38 | 
| [cognitive-search-quickstart-blob.md](#item-74f4f0) | minor update | スキルセット作成手順の更新 | modified | 17 | 18 | 35 | 
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | スコアリングプロファイルの説明の追加 | modified | 4 | 2 | 6 | 
| [samples-dotnet.md](#item-12f3fa) | minor update | C# サンプルの更新 | modified | 4 | 3 | 7 | 
| [samples-java.md](#item-5992fd) | minor update | Java サンプルの更新 | modified | 5 | 4 | 9 | 
| [samples-javascript.md](#item-82e67e) | minor update | JavaScript サンプルの更新 | modified | 3 | 2 | 5 | 
| [samples-python.md](#item-d2bf09) | minor update | Python サンプルの更新 | modified | 6 | 4 | 10 | 
| [samples-rest.md](#item-198ebc) | minor update | REST サンプルの更新 | modified | 4 | 3 | 7 | 
| [search-how-to-define-index-projections.md](#item-a7e2c5) | minor update | インデックスプロジェクションの定義に関する注意事項の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/cognitive-search-concept-image-scenarios.md{#item-606953}

<details>
<summary>Diff</summary>
````diff
@@ -1,36 +1,36 @@
 ---
-title: Extract text from images
+title: Extract text from images by using AI enrichment
 titleSuffix: Azure AI Search
 description: Use Optical Character Recognition (OCR) and image analysis to extract text, layout, captions, and tags from image files in Azure AI Search pipelines.
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 01/10/2024
+ms.date: 10/15/2024
 ms.custom:
   - devx-track-csharp
   - ignite-2023
 ---
 
-# Extract text and information from images in AI enrichment
+# Extract text and information from images by using AI enrichment
 
 Through [AI enrichment](cognitive-search-concept-intro.md), Azure AI Search gives you several options for creating and extracting searchable text from images, including:
 
 + [OCR](cognitive-search-skill-ocr.md) for optical character recognition of text and digits
 + [Image Analysis](cognitive-search-skill-image-analysis.md) that describes images through visual features
 + [Custom skills](#passing-images-to-custom-skills) to invoke any external image processing that you want to provide
 
-Through OCR, you can extract text from photos or pictures containing alphanumeric text, such as the word "STOP" in a stop sign. Through image analysis, you can generate a text representation of an image, such as "dandelion" for a photo of a dandelion, or the color "yellow". You can also extract metadata about the image, such as its size.
+By using OCR, you can extract text from photos or pictures containing alphanumeric text, such as the word *STOP* in a stop sign. Through image analysis, you can generate a text representation of an image, such as *dandelion* for a photo of a dandelion, or the color *yellow*. You can also extract metadata about the image, such as its size.
 
 This article covers the fundamentals of working with images, and also describes several common scenarios, such as working with embedded images, custom skills, and overlaying visualizations on original images.
 
-To work with image content in a skillset, you'll need:
+To work with image content in a skillset, you need:
 
 > [!div class="checklist"]
 > + Source files that include images
 > + A search indexer, configured for image actions
 > + A skillset with built-in or custom skills that invoke OCR or image analysis
-> + A search index with fields to receive the analyzed text output, plus output field mappings in the indexer that establish association.
+> + A search index with fields to receive the analyzed text output, plus output field mappings in the indexer that establish association
 
 Optionally, you can define projections to accept image-analyzed output into a [knowledge store](knowledge-store-concept-intro.md) for data mining scenarios.
 
@@ -41,13 +41,13 @@ Image processing is indexer-driven, which means that the raw inputs must be in a
 + Image analysis supports JPEG, PNG, GIF, and BMP
 + OCR supports JPEG, PNG, BMP, and TIF
 
-Images are either standalone binary files or embedded in documents (PDF, RTF, and Microsoft application files). A maximum of 1000 images can be extracted from a given document. If there are more than 1000 images in a document, the first 1000 are extracted and then a warning is generated.
+Images are either standalone binary files or embedded in documents, such as PDF, RTF, or Microsoft application files. A maximum of 1,000 images can be extracted from a given document. If there are more than 1,000 images in a document, the first 1,000 are extracted and then a warning is generated.
 
 Azure Blob Storage is the most frequently used storage for image processing in Azure AI Search. There are three main tasks related to retrieving images from a blob container:
 
 + Enable access to content in the container. If you're using a full access connection string that includes a key, the key gives you permission to the content. Alternatively, you can [authenticate using Microsoft Entra ID](search-howto-managed-identities-data-sources.md) or [connect as a trusted service](search-indexer-howto-access-trusted-service-exception.md).
 
-+ [Create a data source](search-howto-indexing-azure-blob-storage.md) of type "azureblob" that connects to the blob container storing your files.
++ [Create a data source](search-howto-indexing-azure-blob-storage.md) of type *azureblob* that connects to the blob container storing your files.
 
 + Review [service tier limits](search-limits-quotas-capacity.md) to make sure that your source data is under maximum size and quantity limits for indexers and enrichment.
 
@@ -58,11 +58,11 @@ Azure Blob Storage is the most frequently used storage for image processing in A
 After the source files are set up, enable image normalization by setting the `imageAction` parameter in indexer configuration. Image normalization helps make images more uniform for downstream processing. Image normalization includes the following operations:
 
 + Large images are resized to a maximum height and width to make them uniform.
-+ For images that have metadata on orientation, image rotation is adjusted for vertical loading.  
++ For images that have metadata that specifies orientation, image rotation is adjusted for vertical loading.  
 
 Metadata adjustments are captured in a complex type created for each image. You can't opt out of the image normalization requirement. Skills that iterate over images, such as OCR and image analysis, expect normalized images.
 
-1. [Create or Update an indexer](/rest/api/searchservice/indexers/create) to set the configuration properties:
+1. [Create or update an indexer](/rest/api/searchservice/indexers/create-or-update) to set the configuration properties:
 
     ```json
     {
@@ -80,23 +80,23 @@ Metadata adjustments are captured in a complex type created for each image. You
 
 1. Set `dataToExtract` to `contentAndMetadata` (required).
 
-1. Verify that the `parsingMode` is set to default (required). 
+1. Verify that the `parsingMode` is set to *default* (required).
 
-   This parameter determines the granularity of search documents created in the index. The default mode sets up a one-to-one correspondence so that one blob results in one search document. If documents are large, or if skills require smaller chunks of text, you can add Text Split skill that subdivides a document into paging for processing purposes. But for search scenarios, one blob per document is required if enrichment includes image processing. 
+   This parameter determines the granularity of search documents created in the index. The default mode sets up a one-to-one correspondence so that one blob results in one search document. If documents are large, or if skills require smaller chunks of text, you can add the Text Split skill that subdivides a document into paging for processing purposes. But for search scenarios, one blob per document is required if enrichment includes image processing.
 
-1. Set `imageAction` to enable the *normalized_images* node in an enrichment tree (required):
+1. Set `imageAction` to enable the `normalized_images` node in an enrichment tree (required):
 
    + `generateNormalizedImages` to generate an array of normalized images as part of document cracking.
 
-   + `generateNormalizedImagePerPage` (applies to PDF only) to generate an array of normalized images where each page in the PDF is rendered to one output image. For non-PDF files, the behavior of this parameter is similar as if you had set "generateNormalizedImages". However, note that setting "generateNormalizedImagePerPage" can make indexing operation less performant by design (especially for large documents) since several images would have to be generated.
+   + `generateNormalizedImagePerPage` (applies to PDF only) to generate an array of normalized images where each page in the PDF is rendered to one output image. For non-PDF files, the behavior of this parameter is similar as if you had set `generateNormalizedImages`. However, setting `generateNormalizedImagePerPage` can make indexing operation less performant by design (especially for large documents) since several images would have to be generated.
 
 1. Optionally, adjust the width or height of the generated normalized images:
 
-   + `normalizedImageMaxWidth` (in pixels). Default is 2000. Maximum value is 10000.
+   + `normalizedImageMaxWidth` in pixels. Default is 2,000. Maximum value is 10,000.
 
-   + `normalizedImageMaxHeight` (in pixels). Default is 2000. Maximum value is 10000.
+   + `normalizedImageMaxHeight` in pixels. Default is 2,000. Maximum value is 10,000.
 
-   The default of 2000 pixels for the normalized images maximum width and height is based on the maximum sizes supported by the [OCR skill](cognitive-search-skill-ocr.md) and the [image analysis skill](cognitive-search-skill-image-analysis.md). The [OCR skill](cognitive-search-skill-ocr.md) supports a maximum width and height of 4200 for non-English languages, and 10000 for English.  If you increase the maximum limits, processing could fail on larger images depending on your skillset definition and the language of the documents. 
+   The default of 2,000 pixels for the normalized images maximum width and height is based on the maximum sizes supported by the [OCR skill](cognitive-search-skill-ocr.md) and the [image analysis skill](cognitive-search-skill-image-analysis.md). The [OCR skill](cognitive-search-skill-ocr.md) supports a maximum width and height of 4,200 for non-English languages, and 10,000 for English. If you increase the maximum limits, processing could fail on larger images depending on your skillset definition and the language of the documents. 
 
 + Optionally, [set file type criteria](search-blob-storage-integration.md#PartsOfBlobToIndex) if the workload targets a specific file type. Blob indexer configuration includes file inclusion and exclusion settings. You can filter out files you don't want.
 
@@ -113,7 +113,7 @@ Metadata adjustments are captured in a complex type created for each image. You
 
 ### About normalized images
 
-When `imageAction` is set to a value other than "none", the new *normalized_images* field contains an array of images. Each  image is a complex type that has the following members:
+When `imageAction` is set to a value other than *none*, the new `normalized_images` field contains an array of images. Each image is a complex type that has the following members:
 
 | Image member       | Description                             |
 |--------------------|-----------------------------------------|
@@ -123,10 +123,10 @@ When `imageAction` is set to a value other than "none", the new *normalized_imag
 | originalWidth      | The original width of the image before normalization. |
 | originalHeight      | The original height of the image before normalization. |
 | rotationFromOriginal |  Counter-clockwise rotation in degrees that occurred to create the normalized image. A value between 0 degrees and 360 degrees. This step reads the metadata from the image that is generated by a camera or scanner. Usually a multiple of 90 degrees. |
-| contentOffset | The character offset within the content field where the image was extracted from. This field is only applicable for files with embedded images. The *contentOffset* for images extracted from PDF documents is always at the end of the text on the page it was extracted from in the document. This means images appear after all text on that page, regardless of the original location of the image in the page. |
+| contentOffset | The character offset within the content field where the image was extracted from. This field is only applicable for files with embedded images. The `contentOffset` for images extracted from PDF documents is always at the end of the text on the page it was extracted from in the document. This means images appear after all text on that page, regardless of the original location of the image in the page. |
 | pageNumber | If the image was extracted or rendered from a PDF, this field contains the page number in the PDF it was extracted or rendered from, starting from 1. If the image isn't from a PDF, this field is 0.  |
 
- Sample value of *normalized_images*:
+ Sample value of `normalized_images`:
 
 ```json
 [
@@ -151,16 +151,16 @@ This section supplements the [skill reference](cognitive-search-predefined-skill
 
 1. Add templates for OCR and Image Analysis from the portal, or copy the definitions from the [skill reference](cognitive-search-predefined-skills.md) documentation. Insert them into the skills array of your skillset definition.
 
-1. If necessary, [include multi-service key](cognitive-search-attach-cognitive-services.md) in the Azure AI services property of the skillset. Azure AI Search makes calls to a billable Azure AI services resource for OCR and image analysis for transactions that exceed the free limit (20 per indexer per day). Azure AI services must be in the same region as your search service.
+1. If necessary, [include a multi-service key](cognitive-search-attach-cognitive-services.md) in the Azure AI services property of the skillset. Azure AI Search makes calls to a billable Azure AI services resource for OCR and image analysis for transactions that exceed the free limit (20 per indexer per day). Azure AI services must be in the same region as your search service.
 
-1. If original images are embedded in PDF or application files like PPTX or DOCX, you'll need to add a Text Merge skill if you want image output and text output together. Working with embedded images is discussed further on in this article.
+1. If original images are embedded in PDF or application files like PPTX or DOCX, you need to add a Text Merge skill if you want image output and text output together. Working with embedded images is discussed further on in this article.
 
 Once the basic framework of your skillset is created and Azure AI services is configured, you can focus on each individual image skill, defining inputs and source context, and mapping outputs to fields in either an index or knowledge store.
 
 > [!NOTE]
-> See [REST Tutorial: Use REST and AI to generate searchable content from Azure blobs](cognitive-search-tutorial-blob.md) for an example skillset that combines image processing with downstream natural language processing. It shows how to feed skill imaging output into entity recognition and key phrase extraction.
+> For an example skillset that combines image processing with downstream natural language processing, see [REST Tutorial: Use REST and AI to generate searchable content from Azure blobs](cognitive-search-tutorial-blob.md). It shows how to feed skill imaging output into entity recognition and key phrase extraction.
 
-### About inputs for image processing
+### Inputs for image processing
 
 As noted, images are extracted during document cracking and then normalized as a preliminary step. The normalized images are the inputs to any image processing skill, and are always represented in an enriched document tree in either one of two ways:
 
@@ -224,11 +224,11 @@ In a skillset, Image Analysis and OCR skill output is always text. Output text i
     }
     ```
 
-1. [Create or update a search index](/rest/api/searchservice/indexes/create) to add fields to accept the skill outputs. 
+1. [Create or update a search index](/rest/api/searchservice/indexes/create-or-update) to add fields to accept the skill outputs. 
 
-   In the following fields collection example, "content" is blob content. "Metadata_storage_name" contains the name of the file (make sure it is "retrievable"). "Metadata_storage_path" is the unique path of the blob and is the default document key. "Merged_content" is output from Text Merge (useful when images are embedded). 
+   In the following fields collection example, *content* is blob content. *Metadata_storage_name* contains the name of the file (set `retrievable` to *true*). *Metadata_storage_path* is the unique path of the blob and is the default document key. *Merged_content* is output from Text Merge (useful when images are embedded). 
 
-    "Text" and "layoutText" are OCR skill outputs and must be a string collection in order to the capture all of the OCR-generated output for the entire document.
+    *Text* and *layoutText* are OCR skill outputs and must be a string collection in order to the capture all of the OCR-generated output for the entire document.
 
     ```json
       "fields": [
@@ -284,7 +284,7 @@ In a skillset, Image Analysis and OCR skill output is always text. Output text i
 
 1. [Update the indexer](/rest/api/searchservice/indexers/create-or-update) to map skillset output (nodes in an enrichment tree) to index fields.
 
-   Enriched documents are internal. To externalize the nodes in an enriched document tree, set up an output field mapping that specifies which index field receives node content. Enriched data is accessed by your app through an index field. The following example shows a "text" node (OCR output) in an enriched document that's mapped to a "text" field in a search index.
+   Enriched documents are internal. To externalize the nodes in an enriched document tree, set up an output field mapping that specifies which index field receives node content. Enriched data is accessed by your app through an index field. The following example shows a *text* node (OCR output) in an enriched document that's mapped to a *text* field in a search index.
 
     ```json
       "outputFieldMappings": [
@@ -313,15 +313,15 @@ POST /indexes/[index name]/docs/search?api-version=[api-version]
 }
 ```
 
-OCR recognizes text in image files. This means that OCR fields ("text" and "layoutText") are empty if source documents are pure text or pure imagery. Similarly, image analysis fields ("imageCaption" and "imageTags") are empty if source document inputs are strictly text. Indexer execution emits warnings if imaging inputs are empty. Such warnings are to be expected when nodes are unpopulated in the enriched document. Recall that blob indexing lets you include or exclude file types if you want to work with content types in isolation. You can use these setting to reduce noise during indexer runs.
+OCR recognizes text in image files. This means that OCR fields (*text* and *layoutText*) are empty if source documents are pure text or pure imagery. Similarly, image analysis fields (*imageCaption* and *imageTags*) are empty if source document inputs are strictly text. Indexer execution emits warnings if imaging inputs are empty. Such warnings are to be expected when nodes are unpopulated in the enriched document. Recall that blob indexing lets you include or exclude file types if you want to work with content types in isolation. You can use these settings to reduce noise during indexer runs.
 
-An alternate query for checking results might include the "content" and "merged_content" fields. Notice that those fields include content for any blob file, even those where there was no image processing performed.
+An alternate query for checking results might include the *content* and *merged_content* fields. Notice that those fields include content for any blob file, even those where there was no image processing performed.
 
 ### About skill outputs
 
-Skill outputs include "text" (OCR), "layoutText" (OCR), "merged_content", "captions" (image analysis), "tags" (image analysis):
+Skill outputs include `text` (OCR), `layoutText` (OCR), `merged_content`, `captions` (image analysis), `tags` (image analysis):
 
-+ "text" stores OCR-generated output. This node should be mapped to field of type `Collection(Edm.String)`. There's one "text" field per search document consisting of comma-delimited strings for documents that contain multiple images. The following illustration shows OCR output for three documents. First is a document containing a file with no images. Second is a document (image file) containing one word, "Microsoft". Third is a document containing multiple images, some without any text (`"",`).
++ `text` stores OCR-generated output. This node should be mapped to field of type `Collection(Edm.String)`. There's one `text` field per search document consisting of comma-delimited strings for documents that contain multiple images. The following illustration shows OCR output for three documents. First is a document containing a file with no images. Second is a document (image file) containing one word, *Microsoft*. Third is a document containing multiple images, some without any text (`"",`).
 
     ```json
     "value": [
@@ -350,23 +350,23 @@ Skill outputs include "text" (OCR), "layoutText" (OCR), "merged_content", "capti
     ]
     ```
 
-+ "layoutText" stores OCR-generated information about text location on the page, described in terms of bounding boxes and coordinates of the normalized image. This node should be mapped to field of type `Collection(Edm.String)`. There's one "layoutText" field per search document consisting of comma-delimited strings.
++ `layoutText` stores OCR-generated information about text location on the page, described in terms of bounding boxes and coordinates of the normalized image. This node should be mapped to field of type `Collection(Edm.String)`. There's one `layoutText` field per search document consisting of comma-delimited strings.
 
-+ "merged_content" stores the output of a Text Merge skill, and it should be one large field of type `Edm.String` that contains raw text from the source document, with embedded "text" in place of an image. If files are text-only, then OCR and image analysis have nothing to do, and "merged_content" is the same as "content" (a blob property that contains the content of the blob).
++ `merged_content` stores the output of a Text Merge skill, and it should be one large field of type `Edm.String` that contains raw text from the source document, with embedded `text` in place of an image. If files are text-only, then OCR and image analysis have nothing to do, and `merged_content` is the same as `content` (a blob property that contains the content of the blob).
 
-+ "imageCaption" captures a description of an image as individuals tags and a longer text description.
++ `imageCaption` captures a description of an image as individuals tags and a longer text description.
 
-+ "imageTags" stores tags about an image as a collection of keywords, one collection for all images in the source document. 
++ `imageTags` stores tags about an image as a collection of keywords, one collection for all images in the source document. 
 
 The following screenshot is an illustration of a PDF that includes text and embedded images. Document cracking detected three embedded images: flock of seagulls, map, eagle. Other text in the example (including titles, headings, and body text) was extracted as text and excluded from image processing.
 
-:::image type="content" source="media/cognitive-search-concept-image-scenarios/state-of-birds-screenshot.png" alt-text="Screenshot of three images in a PDF" border="true":::
+:::image type="content" source="media/cognitive-search-concept-image-scenarios/state-of-birds-screenshot.png" alt-text="Screenshot of three images in a PDF." border="true":::
 
-Image analysis output is illustrated in the JSON below (search result). The skill definition allows you to specify which [visual features](cognitive-search-skill-image-analysis.md#skill-parameters) are of interest. For this example, tags and descriptions were produced, but there are more outputs to choose from.
+Image analysis output is illustrated in the following JSON (search result). The skill definition allows you to specify which [visual features](cognitive-search-skill-image-analysis.md#skill-parameters) are of interest. For this example, tags and descriptions were produced, but there are more outputs to choose from.
 
-+ "imageCaption" output is an array of descriptions, one per image, denoted by "tags" consisting of single words and longer phrases that describe the image. Notice the tags consisting of "a flock of seagulls are swimming in the water", or "a close up of a bird".
++ `imageCaption` output is an array of descriptions, one per image, denoted by `tags` consisting of single words and longer phrases that describe the image. Notice the tags consisting of *a flock of seagulls are swimming in the water*, or *a close up of a bird*.
 
-+ "imageTags" output is an array of single tags, listed in the order of creation. Notice that tags repeat. There's no aggregation or grouping.
++ `imageTags` output is an array of single tags, listed in the order of creation. Notice that tags repeat. There's no aggregation or grouping.
 
 ```json
  "imageCaption": [
@@ -401,27 +401,27 @@ Image analysis output is illustrated in the JSON below (search result). The skil
 
 ## Scenario: Embedded images in PDFs
 
-When the images you want to process are embedded in other files, such as PDF or DOCX, the enrichment pipeline extracts just the images and then pass them to OCR or image analysis for processing. Image extraction occurs during the document cracking phase, and once the images are separated, they remain separate unless you explicitly merge the processed output back into the source text. 
+When the images you want to process are embedded in other files, such as PDF or DOCX, the enrichment pipeline extracts just the images and then passes them to OCR or image analysis for processing. Image extraction occurs during the document cracking phase, and once the images are separated, they remain separate unless you explicitly merge the processed output back into the source text. 
 
 [**Text Merge**](cognitive-search-skill-textmerger.md) is used to put image processing output back into the document. Although Text Merge isn't a hard requirement, it's frequently invoked so that image output (OCR text, OCR layoutText, image tags, image captions) can be reintroduced into the document. Depending on the skill, the image output replaces an embedded binary image with an in-place text equivalent. Image Analysis output can be merged at image location. OCR output always appears at the end of each page.
 
 The following workflow outlines the process of image extraction, analysis, merging, and how to extend the pipeline to push image-processed output into other text-based skills such as Entity Recognition or Text Translation.
 
-1. After connecting to the data source, the indexer loads and cracks source documents, extracting images and text, and queuing each content type for processing. An enriched document consisting only of a root node (`"document"`) is created.
+1. After connecting to the data source, the indexer loads and cracks source documents, extracting images and text, and queuing each content type for processing. An enriched document consisting only of a root node (*document*) is created.
 
-1. Images in the queue are [normalized](#get-normalized-images) and passed into enriched documents as a [`"document/normalized_images"`](#get-normalized-images) node.
+1. Images in the queue are [normalized](#get-normalized-images) and passed into enriched documents as a [document/normalized_images](#get-normalized-images) node.
 
-1. Image enrichments execute, using `"/document/normalized_images"` as input. 
+1. Image enrichments execute, using `"/document/normalized_images"` as input.
 
-1. Image outputs are passed into the enriched document tree, with each output as a separate node. Outputs vary by skill (text and layoutText for OCR, tags and captions for Image Analysis).
+1. Image outputs are passed into the enriched document tree, with each output as a separate node. Outputs vary by skill (text and layoutText for OCR; tags and captions for Image Analysis).
 
 1. Optional but recommended if you want search documents to include both text and image-origin text together, [Text Merge](cognitive-search-skill-textmerger.md) runs, combining the text representation of those images with the raw text extracted from the file. Text chunks are consolidated into a single large string, where the text is inserted first in the string and then the OCR text output or image tags and captions.
 
    The output of Text Merge is now the definitive text to analyze for any downstream skills that perform text processing. For example, if your skillset includes both OCR and Entity Recognition, the input to Entity Recognition should be `"document/merged_text"` (the targetName of the Text Merge skill output).
 
 1. After all skills have executed, the enriched document is complete. In the last step, indexers refer to [output field mappings](#output-field-mappings) to send enriched content to individual fields in the search index.
 
-The following example skillset creates a `"merged_text"` field containing the original text of your document with embedded OCRed text in place of embedded images. It also includes an Entity Recognition skill that uses `"merged_text"` as input.
+The following example skillset creates a `merged_text` field containing the original text of your document with embedded OCRed text in place of embedded images. It also includes an Entity Recognition skill that uses `merged_text` as input.
 
 ### Request body syntax
 
@@ -492,7 +492,7 @@ The following example skillset creates a `"merged_text"` field containing the or
 }
 ```
 
-Now that you have a merged_text field, you can map it as a searchable field in your indexer definition. All of the content of your files, including the text of the images, will be searchable.
+Now that you have a `merged_text` field, you can map it as a searchable field in your indexer definition. All of the content of your files, including the text of the images, will be searchable.
 
 ## Scenario: Visualize bounding boxes
 
@@ -617,7 +617,7 @@ for value in values:
   # you now have an image to work with
 ```
 
-Similarly to return an image, return a base64 encoded string within a JSON object with a `$type` property of `file`.
+Similarly to return an image, return a base64 encoded string within a JSON object with a `$type` property of *file*.
 
 ```python
 def base64EncodeImage(image):
@@ -634,11 +634,11 @@ def base64EncodeImage(image):
 }
 ```
 
-## See also
+## Related content
 
 + [Create indexer (REST)](/rest/api/searchservice/indexers/create)
 + [Image Analysis skill](cognitive-search-skill-image-analysis.md)
 + [OCR skill](cognitive-search-skill-ocr.md)
-+ [Text merge skill](cognitive-search-skill-textmerger.md)
-+ [How to define a skillset](cognitive-search-defining-skillset.md)
-+ [How to map enriched fields](cognitive-search-output-field-mapping.md)
++ [Text Merge skill](cognitive-search-skill-textmerger.md)
++ [How to create a skillset](cognitive-search-defining-skillset.md)
++ [Map enriched output to fields](cognitive-search-output-field-mapping.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像処理の手法に関する内容の更新"
}
```

### Explanation
この変更は、「cognitive-search-concept-image-scenarios.md」というドキュメントに対するもので、主に文書内のいくつかのタイトルや説明、表現を改善し、より明確に表現することを目的としています。具体的には、AI強化機能による画像からのテキスト抽出に関する説明が追加され、日付や技術用語の整合性が調整されました。

主な変更点は以下の通りです：

- タイトルが「Extract text from images」から「Extract text from images by using AI enrichment」に変更され、AI強化のコンテキストが強調されました。
- 文の表現が改善され、例えば「Through OCR, you can extract ...」が「By using OCR, you can extract ...」に変更されました。これにより、文がより自然な流れになっています。
- 重要な技術的詳細が強調され、特に画像処理の制約や推奨される設定についての説明が整理されました。
- 日付のフォーマットも更新されています。

これらの変更により、文書全体の可読性とユーザー体験が向上し、技術的な正確さが保たれています。

## articles/search/cognitive-search-output-field-mapping.md{#item-31fe9c}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Map enrichments in indexers
+title: Map enriched output to fields in a search index
 titleSuffix: Azure AI Search
 description: Export the enriched content created by a skillset by mapping its output fields to fields in a search index.
 author: HeidiSteen
@@ -8,12 +8,12 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 07/30/2024
+ms.date: 10/15/2024
 ---
 
 # Map enriched output to fields in a search index in Azure AI Search
 
-![Indexer Stages](./media/cognitive-search-output-field-mapping/indexer-stages-output-field-mapping.png "indexer stages")
+:::image type="content" source="media/cognitive-search-output-field-mapping/indexer-stages-output-field-mapping.png" alt-text="Diagram of the Indexer Stages with Output Field Mappings highlighted.":::
 
 This article explains how to set up *output field mappings*, defining a data path between in-memory data generated during [skillset processing](cognitive-search-concept-intro.md), and target fields in a search index. During indexer execution, skills-generated information exists in memory only. To persist this information in a search index, you need to tell the indexer where to send the data.
 
@@ -35,14 +35,14 @@ In contrast with a [`fieldMappings`](search-indexer-field-mappings.md) definitio
 
 - Indexer, index, data source, and skillset.
 
-- Index fields must be simple or top-level fields. You can't output to a [complex type](search-howto-complex-data-types.md), but if you have a complex type, you can use an output field definition to flatten parts of the complex type and send them to a collection in a search index. 
+- Index fields must be simple or top-level fields. You can't output to a [complex type](search-howto-complex-data-types.md). However, if you have a complex type, you can use an output field definition to flatten parts of the complex type and send them to a collection in a search index.
 
 ## When to use an output field mapping
 
 Output field mappings are required if your indexer has an attached [skillset](cognitive-search-working-with-skillsets.md) that creates new information that you want in your index. Examples include:
 
 - Vectors from embedding skills
-- OCR text from image skills
+- Optical character recognition (OCR) text from image skills
 - Locations, organizations, or people from entity recognition skills
 
 Output field mappings can also be used to:
@@ -95,13 +95,13 @@ You can use the REST API or an Azure SDK to define output field mappings.
 
     | Property | Description |
     |----------|-------------|
-    | sourceFieldName | Required. Specifies a path to enriched content. An example might be `/document/content`. See [Reference enrichments in an Azure AI Search skillset](cognitive-search-concept-annotations-syntax.md) for path syntax and examples. |
+    | sourceFieldName | Required. Specifies a path to enriched content. An example might be */document/content*. See [Reference enrichments in an Azure AI Search skillset](cognitive-search-concept-annotations-syntax.md) for path syntax and examples. |
     | targetFieldName | Optional. Specifies the search field that receives the enriched content. Target fields must be top-level simple fields or collections. It can't be a path to a subfield in a complex type. If you want to retrieve specific nodes in a complex structure, you can [flatten individual nodes](#flattening-information-from-complex-types) in memory, and then send the output to a string collection in your index. |
     | mappingFunction | Optional. Adds extra processing provided by [mapping functions](search-indexer-field-mappings.md#mappingFunctions) supported by indexers. For enrichment nodes, encoding and decoding are the most commonly used functions. |
 
 1. The `targetFieldName` is always the name of the field in the search index.
 
-1. The `sourceFieldName` is a path to a node in the enriched document. It's the output of a skill. The path always starts with `/document`, and if you're indexing from a blob, the second element of the path is `/content`. The third element is the value produced by the skill. For more information and examples, see [Reference enrichments in an Azure AI Search skillset](cognitive-search-concept-annotations-syntax.md).
+1. The `sourceFieldName` is a path to a node in the enriched document. It's the output of a skill. The path always starts with */document*, and if you're indexing from a blob, the second element of the path is */content*. The third element is the value produced by the skill. For more information and examples, see [Reference enrichments in an Azure AI Search skillset](cognitive-search-concept-annotations-syntax.md).
 
     This example adds entities and sentiment labels extracted from a blob's content property to fields in a search index.
     
@@ -136,7 +136,7 @@ You can use the REST API or an Azure SDK to define output field mappings.
 
 ### [**.NET SDK (C#)**](#tab/csharp)
 
-In the Azure SDK for .NET, use the [OutputFieldMappingEntry](/dotnet/api/azure.search.documents.indexes.models.outputfieldmappingentry) class that provides "Name" and "TargetFieldName" properties and an optional "MappingFunction" reference.
+In the Azure SDK for .NET, use the [OutputFieldMappingEntry](/dotnet/api/azure.search.documents.indexes.models.outputfieldmappingentry) class that provides `Name` and `TargetFieldName` properties and an optional `MappingFunction` reference.
 
 Specify output field mappings when constructing the indexer, or later by directly setting [SearchIndexer.OutputFieldMappings](/dotnet/api/azure.search.documents.indexes.models.searchindexer.outputfieldmappings). The following C# example sets the output field mappings when constructing an indexer.
 
@@ -177,7 +177,7 @@ Assume a skillset that generates embeddings for a vector field, and an index tha
   ]
 ```
 
-The source field path is skill output. In this example, the output is `text_vector`. Target name is an optional property. If you don't give the output mapping a target name, the path would be `embedding` or more precisely, `/document/content/embedding`.
+The source field path is skill output. In this example, the output is *text_vector*. Target name is an optional property. If you don't give the output mapping a target name, the path would be *embedding* or more precisely, */document/content/embedding*.
 
 ```json
 {
@@ -254,7 +254,7 @@ Here's an example of a document in Azure Cosmos DB with nested JSON:
 }
 ```
 
-If you wanted to fully index the above source document, you'd create an index definition where the field names, levels, and types are reflected as a complex type. Because field mappings aren't supported for complex types in the search index, your index definition must mirror the source document.
+If you wanted to fully index this source document, you'd create an index definition where the field names, levels, and types are reflected as a complex type. Because field mappings aren't supported for complex types in the search index, your index definition must mirror the source document.
 
 ```json
 {
@@ -283,7 +283,7 @@ If you wanted to fully index the above source document, you'd create an index de
 }
 ```
 
-Here's a sample indexer definition that executes the import (notice there are no field mappings and no skillset).
+Here's a sample indexer definition that executes the import. Notice there are no field mappings and no skillset.
 
 ```json
 {
@@ -304,7 +304,7 @@ The result is the following sample search document, similar to the original in A
   "value": [
     {
       "@search.score": 1,
-      "id": "240a98f5-90c9-406b-a8c8-f50ff86f116c",
+      "id": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",
       "palette": "primary colors",
       "colors": [
         {
@@ -338,9 +338,9 @@ The result is the following sample search document, similar to the original in A
 
 An alternative rendering in a search index is to flatten individual nodes in the source's nested structure into a string collection in a search index.
 
-To accomplish this task, you'll need an `outputFieldMappings` that maps an in-memory node to a string collection in the index. Although output field mappings primarily apply to skill outputs, you can also use them to address nodes after ["document cracking"](search-indexer-overview.md#stage-1-document-cracking) where the indexer opens a source document and reads it into memory.
+To accomplish this task, you'll need an `outputFieldMappings` that maps an in-memory node to a string collection in the index. Although output field mappings primarily apply to skill outputs, you can also use them to address nodes after [document cracking](search-indexer-overview.md#stage-1-document-cracking) where the indexer opens a source document and reads it into memory.
 
-Below is a sample index definition, using string collections to receive flattened output:
+The following sample index definition uses string collections to receive flattened output:
 
 ```json
 {
@@ -378,14 +378,14 @@ Here's the sample indexer definition, using `outputFieldMappings` to associate t
 }
 ```
 
-Results from the above definition are as follows. Simplifying the structure loses context in this case. There's no longer any associations between a given color and the mediums it's available in. However, depending on your scenario, a result similar to the one shown below might be exactly what you need.
+Results from the definition are as follows. Simplifying the structure loses context in this case. There's no longer any associations between a given color and the mediums it's available in. However, depending on your scenario, a result similar to the following example might be exactly what you need.
 
 ```json
 {
   "value": [
     {
       "@search.score": 1,
-      "id": "240a98f5-90c9-406b-a8c8-f50ff86f116c",
+      "id": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",
       "palette": "primary colors",
       "color_names": [
         "blue",
@@ -402,8 +402,8 @@ Results from the above definition are as follows. Simplifying the structure lose
 }
 ```
 
-## See also
+## Related content
 
-+ [Define field mappings in a search indexer](search-indexer-field-mappings.md)
++ [Field mappings and transformations](search-indexer-field-mappings.md)
 + [AI enrichment overview](cognitive-search-concept-intro.md)
-+ [Skillset overview](cognitive-search-working-with-skillsets.md)
++ [Skillset concepts](cognitive-search-working-with-skillsets.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "出力フィールドマッピングのタイトルと内容の更新"
}
```

### Explanation
この変更は、「cognitive-search-output-field-mapping.md」というドキュメントに対するもので、主にタイトルや文章の修正を行い、より明確で一貫性のある表現にしています。具体的には、出力フィールドのマッピングに関するガイドラインと手順が更新されています。

主な変更点は以下の通りです：

1. **タイトルの変更**：ドキュメントのタイトルが「Map enrichments in indexers」から「Map enriched output to fields in a search index」に変更され、出力をどのようにインデックス内のフィールドにマッピングするかが明示的に示されています。
   
2. **日付の更新**：ドキュメントの日付が07/30/2024から10/15/2024に変更され、最新の情報に更新されました。

3. **表現の改善**：文中のいくつかの表現が見直され、特に「OCR text from image skills」という表現が「Optical character recognition (OCR) text from image skills」に修正され、技術用語が明確に定義されています。また、ノードの記述方法が一貫性を持たせるために修正されています。

4. **図の表現の更新**：画像の挿入方法が変更され、より整然とした形式で表示されるようになっています。

これらの変更により、ドキュメント全体の読みやすさと理解しやすさが向上し、ユーザーが必要な情報を簡単に見つけることができるようになっています。

## articles/search/cognitive-search-quickstart-blob.md{#item-74f4f0}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: "Quickstart: Create a skillset in the Azure portal"
 titleSuffix: Azure AI Search
-description: In this portal quickstart, use the Import Data wizard to generate searchable text from images and unstructured documents. Skills in this quickstart include OCR, image analysis, and natural language processing.
+description: Learn how to use the Import Data wizard to generate searchable text from images and unstructured documents. Skills in this quickstart include OCR, image analysis, and natural language processing.
 
 manager: nitinme
 author: HeidiSteen
@@ -10,25 +10,24 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: quickstart
-ms.date: 02/22/2024
+ms.date: 10/15/2024
 ---
+
 # Quickstart: Create a skillset in the Azure portal
 
-In this quickstart, you learn how a skillset in Azure AI Search adds Optical Character Recognition (OCR), image analysis, language detection, text translation, and entity recognition to generate text-searchable content in a search index. 
+In this quickstart, you learn how a skillset in Azure AI Search adds optical character recognition (OCR), image analysis, language detection, text translation, and entity recognition to generate text-searchable content in a search index.
 
 You can run the **Import data** wizard in the Azure portal to apply skills that create and transform textual content during indexing. Input is your raw data, usually blobs in Azure Storage. Output is a searchable index containing AI-generated image text, captions, and entities. Generated content is queryable in the portal using [**Search explorer**](search-explorer.md).
 
 To prepare, you create a few resources and upload sample files before running the wizard.
 
 ## Prerequisites
 
-Before you begin, have the following prerequisites in place:
-
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/).
 
-+ Azure AI Search. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices). You can use a free service for this quickstart. 
++ Create an [Azure AI Search service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices). You can use a free service for this quickstart. 
 
-+ Azure Storage account with Blob Storage.
++ An Azure Storage account with Azure Blob Storage.
 
 > [!NOTE]
 > This quickstart uses [Azure AI services](https://azure.microsoft.com/services/cognitive-services/) for the AI transformations. Because the workload is so small, Azure AI services is tapped behind the scenes for free processing for up to 20 transactions. You can complete this exercise without having to create an Azure AI multi-service resource.
@@ -59,7 +58,7 @@ You're now ready to move on the Import data wizard.
 
 1. Sign in to the [Azure portal](https://portal.azure.com/) with your Azure account.
 
-1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) and on the Overview page, select **Import data** on the command bar to create searchable content in four steps.
+1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices). On the Overview page, select **Import data** on the command bar to create searchable content in four steps.
 
    :::image type="content" source="media/search-import-data-portal/import-data-cmd.png" alt-text="Screenshot of the Import data command." border="true":::
 
@@ -73,19 +72,19 @@ You're now ready to move on the Import data wizard.
 
     Continue to the next page.
 
-If you get "Error detecting index schema from data source", the indexer that's powering the wizard can't connect to your data source. Most likely, the data source has security protections. Try the following solutions and then rerun the wizard.
+If you get *Error detecting index schema from data source*, the indexer that powers the wizard can't connect to your data source. Most likely, the data source has security protections. Try the following solutions and then rerun the wizard.
 
 | Security feature | Solution |
 |--------------------|----------|
-| Resource requires Azure roles or its access keys are disabled | [Connect as a trusted service](search-indexer-howto-access-trusted-service-exception.md) or [connect using a managed identity](search-howto-managed-identities-data-sources.md) |
-| Resource is behind an IP firewall | [Create an inbound rule for Search and for Azure portal](search-indexer-howto-access-ip-restricted.md) |
+| Resource requires Azure roles, or its access keys are disabled | [Connect as a trusted service](search-indexer-howto-access-trusted-service-exception.md) or [connect using a managed identity](search-howto-managed-identities-data-sources.md) |
+| Resource is behind an IP firewall | [Create an inbound rule for Search and for the Azure portal](search-indexer-howto-access-ip-restricted.md) |
 | Resource requires a private endpoint connection | [Connect over a private endpoint](search-indexer-howto-access-private.md) |
 
 ### Step 2: Add cognitive skills
 
 Next, configure AI enrichment to invoke OCR, image analysis, and natural language processing. 
 
-1. For this quickstart, we're using the **Free** Azure AI services resource. The sample data consists of 14 files, so the free allotment of 20 transaction on Azure AI services is sufficient for this quickstart. 
+1. For this quickstart, we're using the **Free** Azure AI services resource. The sample data consists of 14 files, so the free allotment of 20 transactions on Azure AI services is sufficient for this quickstart. 
 
    :::image type="content" source="media/cognitive-search-quickstart-blob/cog-search-attach.png" alt-text="Screenshot of the Attach Azure AI services tab." border="true":::
 
@@ -135,7 +134,7 @@ Select **Indexers** from the left navigation pane to monitor status, and then se
 
 To view details about execution status, select **Success** (or **Failed**) to view execution details.
 
-In this demo, there are a few warnings: `"Could not execute skill because one or more skill input was invalid."` It tells you that a PNG file in the data source doesn't provide a text input to Entity Recognition. This warning occurs because the upstream OCR skill didn't recognize any text in the image, and thus couldn't provide a text input to the downstream Entity Recognition skill.
+In this demo, there are a few warnings: *"Could not execute skill because one or more skill input was invalid."* It tells you that a PNG file in the data source doesn't provide a text input to Entity Recognition. This warning occurs because the upstream OCR skill didn't recognize any text in the image, and thus couldn't provide a text input to the downstream Entity Recognition skill.
 
 Warnings are common in skillset execution. As you become familiar with how skills iterate over your data, you might begin to notice patterns and learn which warnings are safe to ignore.
 
@@ -145,7 +144,7 @@ After an index is created, use **Search explorer** to return results.
 
 1. On the left, select **Indexes** and then select the index. **Search explorer** is on the first tab.
 
-1. Enter a search string to query the index, such as `satya nadella`. The search bar accepts keywords, quote-enclosed phrases, and operators (`"Satya Nadella" +"Bill Gates" +"Steve Ballmer"`).
+1. Enter a search string to query the index, such as `satya nadella`. The search bar accepts keywords, quote-enclosed phrases, and operators: `"Satya Nadella" +"Bill Gates" +"Steve Ballmer"`
 
 Results are returned as verbose JSON, which can be hard to read, especially in large documents. Some tips for searching in this tool include the following techniques:
 
@@ -179,7 +178,7 @@ Another important concept is that skills operate over content types, and when wo
 
 Output is routed to a search index, and there's a mapping between name-value pairs created during indexing and individual fields in your index. Internally, the wizard sets up [an enrichment tree](cognitive-search-concept-annotations-syntax.md) and defines a [skillset](cognitive-search-defining-skillset.md), establishing the order of operations and general flow. These steps are hidden in the wizard, but when you start writing code, these concepts become important.
 
-Finally, you learned that can verify content by querying the index. In the end, what Azure AI Search provides is a searchable index, which you can query using either the [simple](/rest/api/searchservice/simple-query-syntax-in-azure-search) or [fully extended query syntax](/rest/api/searchservice/lucene-query-syntax-in-azure-search). An index containing enriched fields is like any other. If you want to incorporate standard or [custom analyzers](search-analyzers.md), [scoring profiles](/rest/api/searchservice/add-scoring-profiles-to-a-search-index), [synonyms](search-synonyms.md), [faceted navigation](search-faceted-navigation.md), geo-search, or any other Azure AI Search feature, you can certainly do so.
+Finally, you learned that you can verify content by querying the index. In the end, what Azure AI Search provides is a searchable index, which you can query using either the [simple](/rest/api/searchservice/simple-query-syntax-in-azure-search) or [fully extended query syntax](/rest/api/searchservice/lucene-query-syntax-in-azure-search). An index containing enriched fields is like any other. You can incorporate standard or [custom analyzers](search-analyzers.md), [scoring profiles](/rest/api/searchservice/add-scoring-profiles-to-a-search-index), [synonyms](search-synonyms.md), [faceted navigation](search-faceted-navigation.md), geo-search, or any other Azure AI Search feature.
 
 ## Clean up resources
 
@@ -189,9 +188,9 @@ You can find and manage resources in the portal, using the **All resources** or
 
 If you used a free service, remember that you're limited to three indexes, indexers, and data sources. You can delete individual items in the portal to stay under the limit. 
 
-## Next steps
+## Next step
 
-You can create skillsets using the portal, .NET SDK, or REST API. To further your knowledge, try the REST API using a REST client and more sample data.
+You can create skillsets using the portal, .NET SDK, or REST API. To further your knowledge, try the REST API by using a REST client and more sample data.
 
 > [!div class="nextstepaction"]
-> [Tutorial: Extract text and structure from JSON blobs using REST APIs ](cognitive-search-tutorial-blob.md)
+> [Tutorial: Use skillsets to generate searchable content in Azure AI Search](cognitive-search-tutorial-blob.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スキルセット作成手順の更新"
}
```

### Explanation
この変更は、「cognitive-search-quickstart-blob.md」というドキュメントに対するもので、主に表現や文法の改善、情報の更新を行っています。このクイックスタートガイドは、Azureポータルでスキルセットを作成し、画像や非構造化ドキュメントから検索可能なテキストを生成する方法を説明しています。

主な変更点は以下の通りです：

1. **説明文の修正**：
   - 説明文が微修正され、「In this portal quickstart, use the Import Data wizard...」から「Learn how to use the Import Data wizard...」に変更され、より動的で教育的な表現になっています。

2. **日付の更新**： 
   - ドキュメントの日付が02/22/2024から10/15/2024に変更され、最新の情報に更新されました。

3. **文の一貫性の向上**：
   - 一部の用語が統一され、例えば、「Optical Character Recognition (OCR)」が「optical character recognition (OCR)」に変更され、文章の整合性が保たれています。

4. **指示や説明の明確化**：
   - 「If you get "Error detecting index schema from data source"...」というエラーメッセージが「If you get *Error detecting index schema from data source*...」に変更され、強調表示がなされています。

5. **段落構成の調整**：
   - セクションや段落の構成がわかりやすくなり、特に手順が明確になっています。

全体的に、これらの変更によりドキュメントの可読性と使いやすさが向上し、ユーザーが迅速に必要な情報を見つけられるようになっています。

## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -31,6 +31,8 @@ You can create multiple profiles and then modify query logic to choose which one
 
 You can have up to 100 scoring profiles within an index (see [service Limits](search-limits-quotas-capacity.md)), but you can only specify one profile at time in any given query.
 
+You can use [semantic ranker](semantic-how-to-query-request.md) with scoring profiles. When multiple ranking or relevance features are in play, semantic ranking is the last step. [How search scoring works](#how-search-scoring-works-in-azure-ai-search) provides an illustration.
+
 > [!NOTE]
 > Unfamiliar with relevance concepts? Visit [Relevance and scoring in Azure AI Search](index-similarity-and-scoring.md) for background. You can also watch this [video segment on YouTube](https://www.youtube.com/embed/Y_X6USgvB1g?version=3&start=463&end=970) for scoring profiles over BM25-ranked results.
 >
@@ -97,9 +99,9 @@ Scoring profiles supplement the default scoring algorithm by boosting the scores
 
 For standalone text queries, scoring profiles identify the maximum 1,000 matches in a [BM25-ranked search](index-similarity-and-scoring.md), and the top 50 are returned in results.
 
-For pure vectors, the query is vector-only, but the [*k*-matching documents](vector-search-ranking.md) include alphanumeric fields that a scoring profile can process. The scoring profile revised the result set by boosting documents that match criteria in the profile.
+For pure vectors, the query is vector-only, but if the [*k*-matching documents](vector-search-ranking.md) include alphanumeric fields that a scoring profile can process, a scoring profile is applied. The scoring profile revises the result set by boosting documents that match criteria in the profile.
 
-For text queries in a hybrid query, scoring profiles identify the maximum 1,000 matches in a BM25-ranked search. However, once those 1,000 results are identified, they're restored to their original BM25 order so that they can be rescored alongside vectors results in the final [Reciprocal Ranking Function (RRF)](hybrid-search-ranking.md) ordering, where the scoring profile (document boosting) is applied to the merged results, followed by [vector weighting](vector-search-how-to-query.md#vector-weighting), and [semantic ranking](semantic-search-overview.md) as the last step.
+For text queries in a hybrid query, scoring profiles identify the maximum 1,000 matches in a BM25-ranked search. However, once those 1,000 results are identified, they're restored to their original BM25 order so that they can be rescored alongside vectors results in the final [Reciprocal Ranking Function (RRF)](hybrid-search-ranking.md) ordering, where the scoring profile (identified as "final document boosting adjustment" in the illustration) is applied to the merged results, along with [vector weighting](vector-search-how-to-query.md#vector-weighting), and [semantic ranking](semantic-search-overview.md) as the last step.
 
 :::image type="content" source="media/scoring-profiles/scoring-over-ranked-results.png" alt-text="Diagram showing which fields have a scoring profile and when ranking occurs.":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリングプロファイルの説明の追加"
}
```

### Explanation
この変更は、「index-add-scoring-profiles.md」というドキュメントに対するもので、スコアリングプロファイルに関連するいくつかの重要なポイントを追加しています。これにより、ユーザーがスコアリングプロファイルを利用する際の理解が深まり、実装における注意点が明確になります。

主な変更点は以下の通りです：

1. **セマンティックランキングの情報追加**：
   - スコアリングプロファイルに関する説明に、セマンティックランカーを利用できる旨が追加されました。これは、複数のランキングや関連性の特徴がある場合において、セマンティックランキングが最終的なステップであることを強調しています。この情報は、ユーザーにとって特に重要であり、最終的な結果の得られ方に影響を与えます。

2. **リファレンスの強化**：
   - 「Relevance and scoring in Azure AI Search」へのリンクが提供され、さらに背景知識を深めるためのYouTube動画へのリンクも追加されました。この追加情報は、関連性やスコアリングの概念に不慣れなユーザーにとって役立つものです。

3. **語句の修正**：
   - 一部の文言が整理され、文法や構成が改善されました。例えば、スコアリングプロファイルについて「スコア修正する措置」の部分が「スコア修正調整」と説明され、より明確な表現になっています。

これらの変更により、読者はスコアリングプロファイルの機能や実装時の考慮すべき点について、より深く理解できるようになっています。また、関連するリソースへのリンクによって、さらに学びを深めることが可能です。

## articles/search/samples-dotnet.md{#item-12f3fa}

<details>
<summary>Diff</summary>
````diff
@@ -10,8 +10,8 @@ ms.service: azure-ai-search
 ms.custom:
   - devx-track-dotnet
   - ignite-2023
-ms.topic: conceptual
-ms.date: 08/16/2024
+ms.topic: concept-article
+ms.date: 10/18/2024
 ---
 
 # C# samples for Azure AI Search
@@ -24,6 +24,7 @@ Learn about the C# code samples that demonstrate the functionality and workflow
 | API reference | [azure.search.documents](/dotnet/api/azure.search.documents)  |
 | API test cases | [github.com/Azure/azure-sdk-for-net/tree/main/sdk/search/Azure.Search.Documents/tests](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/search/Azure.Search.Documents/tests) |
 | Source code | [github.com/Azure/azure-sdk-for-net/tree/main/sdk/search/Azure.Search.Documents/src](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/search/Azure.Search.Documents/src)  |
+| Change log | [https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) |
 
 ## SDK samples
 
@@ -55,7 +56,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. A
 | [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-search/) | [Quickstart: Semantic ranking using the Azure SDKs](search-get-started-semantic.md) | Shows the index schema and query request for invoking semantic ranker. |
 | [search-website](https://github.com/Azure-Samples/azure-search-static-web-app) | [Tutorial: Add search to web apps](tutorial-csharp-overview.md) | Demonstrates an end-to-end search app that includes bulk upload using the push APIs and a rich client for hosting the app and handling search requests.|
 | [tutorial-ai-enrichment](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/tutorial-ai-enrichment)  | [Tutorial: AI-generated searchable content from Azure blobs](cognitive-search-tutorial-blob-dotnet.md) | Shows how to configure an indexer and skillset. |
-| [multiple-data-sources](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources)  | [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md). | Merges content from two data sources into one search index.
+| [multiple-data-sources](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources)  | [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md). | Merges content from two data sources into one search index. |
 | [Optimize-data-indexing](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/optimize-data-indexing) | [Tutorial: Optimize indexing with the push API](tutorial-optimize-indexing-push-api.md).| Demonstrates optimization techniques for pushing data into a search index. |
 | [DotNetHowTo](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowTo)  | [How to use the .NET client library](search-howto-dotnet-sdk.md) | Steps through the basic workflow, but in more detail and with discussion of API usage.  |
 | [DotNetToIndexers](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToIndexers) | [Tutorial: Index Azure SQL data](search-indexer-tutorial.md) | Shows how to configure an Azure SQL indexer that has a schedule, field mappings, and parameters.  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# サンプルの更新"
}
```

### Explanation
この変更は、「samples-dotnet.md」というドキュメントに対するもので、C#を使用したAzure AI Searchのサンプルに関する情報が更新されています。具体的には、ドキュメントのメタデータの変更やリンクの追加、サンプルの編集が行われています。

主な変更点は以下の通りです：

1. **メタデータの変更**：
   - ドキュメントのトピックが「conceptual」から「concept-article」に変更されたことで、コンテンツの分類が明確になりました。
   - 更新日も「08/16/2024」から「10/18/2024」に変更され、最新の情報が反映されています。

2. **変更履歴の追加**：
   - C#サンプルに関する情報表に「Change log」へのリンクが追加され、ユーザーが変更履歴を簡単に確認できるようになりました。このリンクは、SDKの変更内容を追跡する際に便利です。

3. **サンプルリストの整頓**：
   - サンプルコードのセクションで、各サンプルの説明に若干の修正が加えられ、一貫性と可読性が向上しています。具体的には、段落の整理や表現の微調整が行われました。

これらの変更により、ユーザーはC#を使用したAzure AI Searchのサンプルに関する最新情報とリソースにアクセスしやすくなり、実装に役立てることができるようになっています。全体的に、ドキュメントはより明確で、使いやすくなっています。

## articles/search/samples-java.md{#item-5992fd}

<details>
<summary>Diff</summary>
````diff
@@ -11,8 +11,8 @@ ms.custom:
   - devx-track-dotnet
   - devx-track-extended-java
   - ignite-2023
-ms.topic: conceptual
-ms.date: 01/25/2024
+ms.topic: concept-article
+ms.date: 10/18/2024
 ---
 
 # Java samples for Azure AI Search
@@ -23,8 +23,9 @@ Learn about the Java code samples that demonstrate the functionality and workflo
 |--------|------|
 | Package download | [search.maven.org/artifact/com.azure/azure-search-documents](https://search.maven.org/artifact/com.azure/azure-search-documents) |
 | API reference | [com.azure.search.documents](/java/api/com.azure.search.documents)  |
-| API test cases | [github.com/Azure/azure-sdk-for-java/tree/azure-search-documents_11.1.3/sdk/search/azure-search-documents/src/test](https://github.com/Azure/azure-sdk-for-java/tree/azure-search-documents_11.1.3/sdk/search/azure-search-documents/src/test) |
-| Source code | [github.com/Azure/azure-sdk-for-java/tree/azure-search-documents_11.1.3/sdk/search/azure-search-documents/src](https://github.com/Azure/azure-sdk-for-java/tree/azure-search-documents_11.1.3/sdk/search/azure-search-documents/src)  |
+| API test cases | [https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents/src/test](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents/src/test) |
+| Source code | [https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents)  |
+| Change log | [https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) |
 
 ## SDK samples
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java サンプルの更新"
}
```

### Explanation
この変更は、「samples-java.md」というドキュメントの更新に関するもので、Javaを使用したAzure AI Searchのサンプルに関する情報が修正・追加されています。これにより、サンプルコードの参照や関連リソースが最新の情報に基づいて更新されています。

主な変更点は以下の通りです：

1. **メタデータの修正**：
   - ドキュメントのトピックが「conceptual」から「concept-article」に変更され、コンテンツの分類が適切に見直されました。
   - 更新日も「01/25/2024」から「10/18/2024」に変更され、最新の情報が反映されています。

2. **リンクの更新**：
   - APIテストケースとソースコードのリンクが新しいリポジトリ構成に合わせて更新されました。これにより、ユーザーは最新のコードとテストケースにアクセスしやすくなりました。
   - 「Change log」へのリンクが新たに追加され、利用者が変更履歴を確認できるようになっています。これにより、特定のバージョンの更新内容を容易に把握できるようになります。

3. **全体的な整頓**：
   - Javaサンプルドキュメント全体の構造や表現が整理され、情報が明確に提示されています。特にリソースの参照が一貫性を持った形になり、使いやすさが向上しました。

これらの改善により、Javaを用いたAzure AI Searchの利用者は、最新の情報やリソースにより簡単にアクセスでき、実装作業をスムーズに進めることができるようになります。全体として、ドキュメントの質と利便性が向上しています。

## articles/search/samples-javascript.md{#item-82e67e}

<details>
<summary>Diff</summary>
````diff
@@ -11,8 +11,8 @@ ms.custom:
   - devx-track-dotnet
   - devx-track-js
   - ignite-2023
-ms.topic: conceptual
-ms.date: 08/16/2024
+ms.topic: concept-article
+ms.date: 10/18/2024
 ---
 
 # JavaScript samples for Azure AI Search
@@ -25,6 +25,7 @@ Learn about the JavaScript code samples that demonstrate the functionality and w
 | API reference | [@azure/search-documents](/javascript/api/@azure/search-documents/) |
 | API test cases | [github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/test](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/test) |
 | Source code | [github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents) |
+| Change log | [https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) |
 
 ## SDK samples
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript サンプルの更新"
}
```

### Explanation
この変更は、「samples-javascript.md」というドキュメントの更新に関するもので、JavaScriptを使用したAzure AI Searchのサンプルに関する情報が修正・追加されています。これにより、参照できるコードや関連リソースの最新性が保たれています。

主な変更点は以下の通りです：

1. **メタデータの修正**：
   - ドキュメントのトピックが「conceptual」から「concept-article」に変更され、内容の分類が適切になりました。
   - 更新日も「08/16/2024」から「10/18/2024」に変更され、最新の情報が反映されています。

2. **リンクの追加**：
   - 「Change log」へのリンクが新たに追加され、ユーザーが変更履歴を確認できるようになりました。これにより、特定のバージョンの更新内容を簡単に把握することができます。

3. **リンクの更新**：
   - APIテストケースおよびソースコードのリンクが最新の構成に応じて更新され、最新のリソースにアクセスしやすくなっています。

これらの変更により、JavaScriptを用いたAzure AI Searchの利用者は、最新の情報やリソースに簡単にアクセスでき、実装作業を効果的に進めることができます。全体的に、ドキュメントは明確性を増し、ユーザーにとっての利便性が向上しています。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -11,8 +11,8 @@ ms.custom:
   - devx-track-dotnet
   - devx-track-python
   - ignite-2023
-ms.topic: conceptual
-ms.date: 10/07/2024
+ms.topic: concept-article
+ms.date: 10/18/2024
 ---
 
 # Python samples for Azure AI Search
@@ -25,6 +25,7 @@ Learn about the Python code samples that demonstrate the functionality and workf
 | API reference | [azure-search-documents](/python/api/azure-search-documents)  |
 | API test cases | [github.com/Azure/azure-sdk-for-python/tree/main/sdk/search/azure-search-documents/tests](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/search/azure-search-documents/tests) |
 | Source code | [github.com/Azure/azure-sdk-for-python/tree/main/sdk/search/azure-search-documents](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/search/azure-search-documents)  |
+| Change log | [https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) |
 
 ## SDK samples
 
@@ -47,15 +48,16 @@ Code samples from the Azure AI Search team demonstrate features and workflows. M
 
 [**azure-search-vector-samples**](https://github.com/Azure/azure-search-vector-samples/blob/main/README.md) on GitHub provides a comprehensive collection of samples for vector search scenarios, organized by scenario or technology.
 
-We also recommend [**azure-search-openai-demo**](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md). This is a ChatGPT-like experience over enterprise data with Azure OpenAI Python code showing how to use Azure AI Search with the large language models in Azure OpenAI. For background, see this Tech Community blog post: [Revolutionize your Enterprise Data with ChatGPT](https://techcommunity.microsoft.com/t5/ai-applied-ai-blog/revolutionize-your-enterprise-data-with-chatgpt-next-gen-apps-w/ba-p/3762087). |
+[**azure-search-openai-demo**](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md) is a ChatGPT-like experience over enterprise data with Azure OpenAI Python code showing how to use Azure AI Search with the large language models in Azure OpenAI. For background, see this Tech Community blog post: [Revolutionize your Enterprise Data with ChatGPT](https://techcommunity.microsoft.com/t5/ai-applied-ai-blog/revolutionize-your-enterprise-data-with-chatgpt-next-gen-apps-w/ba-p/3762087). |
+
+[**aisearch-openai-rag-audio**](https://github.com/Azure-Samples/aisearch-openai-rag-audio) is "voice to RAG". This sample demonstrates a simple architecture for voice-based generative AI applications that enables Azure AI Search RAG on top of the real-time audio API with full-duplex audio streaming from client devices, while securely handling access to both model and retrieval system. Backend code is written in Python. Frontend code is JavaScript. [Watch this video](https://www.youtube.com/watch?v=vXJka8xZ9Ko) for an introduction. |
 
 ## Other samples
 
 The following samples are also published by the Azure AI Search team, but aren't referenced in documentation. Associated readme files provide usage instructions.
 
 | Repository | Description |
 |------------|-------------|
-| [aisearch-openai-rag-audio](https://github.com/Azure-Samples/aisearch-openai-rag-audio) | A simple architecture for voice-based generative AI applications that enables Azure AI Search RAG on top of the real-time audio API with full-duplex audio streaming from client devices, while securely handling access to both model and retrieval system. Backend code is written in Python. Frontend code is JavaScript. |
 | [azure-search-backup-and-restore.ipynb](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/index-backup-restore) | Uses the **azure.search.documents** library in the Azure SDK for Python to make a local copy of the retrievable fields of a search index, and then push those fields to a new search index. |
 
 > [!TIP]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python サンプルの更新"
}
```

### Explanation
この変更は、「samples-python.md」というドキュメントの更新に関連しており、Azure AI Searchを使用したPythonのサンプルに関する情報が修正および追加されています。これにより、ユーザーは最新のコーディングリソースや関連情報にアクセスしやすくなります。

主な変更点は以下の通りです：

1. **メタデータの修正**：
   - ドキュメントのトピックが「conceptual」から「concept-article」へと変更され、内容の分類が適切になりました。
   - 更新日も「10/07/2024」から「10/18/2024」に変更され、最新の情報が反映されています。

2. **リンクの追加**：
   - 「Change log」へのリンクが新たに追加され、ユーザーがSDKやライブラリの変更履歴を確認できるようになりました。

3. **リンクの更新**：
   - APIテストケースやソースコードへのリンクが最新のリポジトリ構成に応じて更新され、ユーザーが最新のリソースに簡単にアクセスできるようになっています。

4. **セクションの再構成**：
   - Pythonサンプルのセクション内での説明が整理され、特に「azure-search-openai-demo」および新たに追加された「aisearch-openai-rag-audio」についての詳細が明確化されています。これにより、ユーザーは具体的なシナリオに対するサンプルを見つけやすくなります。

これらの改善により、Pythonを利用したAzure AI Searchのユーザーは最新の実装方法やリソースにアクセスし、実務に役立てることができるようになります。全体的に、ドキュメントの明確性と利便性が向上し、ユーザー体験が強化されています。

## articles/search/samples-rest.md{#item-198ebc}

<details>
<summary>Diff</summary>
````diff
@@ -9,8 +9,8 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
-ms.topic: conceptual
-ms.date: 01/11/2024
+ms.topic: concept-article
+ms.date: 10/18/2024
 ---
 
 # REST samples for Azure AI Search
@@ -30,11 +30,12 @@ Code samples from the Azure AI Search team demonstrate features and workflows. M
 | [quickstart](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart) | Source code for [Quickstart: Text search using REST](search-get-started-rest.md). This sample  covers the basic workflow for creating, loading, and querying a search index using sample data. |
 | [quickstart-vectors](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) | Source code for [Quickstart: Vector search using REST APIs](search-get-started-vector.md). This sample  covers the basic workflow for indexing and querying vector data. |
 | [skillset-tutorial](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skillset-tutorial) | Source code for [Tutorial: Use REST and AI to generate searchable content from Azure blobs](cognitive-search-tutorial-blob.md). This sample  shows you how to create a skillset that iterates over Azure blobs to extract information and infer structure.|
+| [skill examples](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skill-examples) | Skillset examples in indexer pipelines that include indexes and indexers so that you can follow field mappings, output field mappings, and source paths. |
 | [debug-sessions](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Debug-sessions) | Source code for [Tutorial: Diagnose, repair, and commit changes to your skillset](cognitive-search-tutorial-debug-sessions.md). This sample  shows you how to use a skillset debug session in the Azure portal. REST is used to create the objects used during debug.|
 | [custom-analyzers](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/custom-analyzers) | Source code for [Tutorial: Create a custom analyzer for phone numbers](tutorial-create-custom-analyzer.md). This sample  explains how to use analyzers to preserve patterns and special characters in searchable content.|
+| [index-json-blobs](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/index-json-blobs) | Create an indexer, data source, and index for nested JSON within a JSON array. This example demonstrates the jsonArray parsing model and documentRoot parameters. |
 | [knowledge-store](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/knowledge-store) | Source code for [Create a knowledge store using REST](knowledge-store-create-rest.md). This sample  explains the necessary steps for populating a knowledge store used for knowledge mining workflows. |
 | [projections](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/projections) | Source code for [Define projections in a knowledge store](knowledge-store-projections-examples.md). This sample explains how to specify the physical data structures in a knowledge store.|
-| [index-encrypted-blobs](https://github.com/Azure-Samples/azure-search-rest-samples/commit/f5ebb141f1ff98f571ab84ac59dcd6fd06a46718) | Source code for [How to index encrypted blobs using blob indexers and skillsets](search-howto-index-encrypted-blobs.md). This article shows how to index documents in Azure Blob Storage that have been previously encrypted using Azure Key Vault. |
 
 > [!TIP]
 > Try the [Samples browser](/samples/browse/?expanded=azure&languages=http&products=azure-cognitive-search) to search for Microsoft code samples in GitHub, filtered by product, service, and language.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST サンプルの更新"
}
```

### Explanation
この変更は、「samples-rest.md」というドキュメントの更新に関連しており、Azure AI Searchを使用したREST APIのサンプルに関する情報が修正および追加されています。これにより、ユーザーは最新のコーディングリソースや関連情報にアクセスしやすくなります。

主な変更点は以下の通りです：

1. **メタデータの修正**：
   - トピックが「conceptual」から「concept-article」に変更され、文書の内容に対する適切な分類が行われました。
   - 更新日も「01/11/2024」から「10/18/2024」へと変更され、最新の情報が反映されています。

2. **新しいサンプルリンクの追加**：
   - 「skill examples」および「index-json-blobs」といった新しいサンプルへのリンクが追加され、ユーザーがインデクサーパイプラインやネストされたJSONの取り扱いに関する情報にアクセスできるようになりました。

3. **リンクの更新**：
   - 一部の既存サンプルの説明が明確化され、「index-encrypted-blobs」リンクが削除され、新しい情報に基づき整理されています。
   - これにより、各サンプルの目的や役割が明確になり、ユーザーは自分のニーズに合ったリソースを見つけやすくなります。

これらの改良により、REST APIを利用したAzure AI Searchのユーザーは最新の実装方法やリソースにアクセスし、実務に役立てることができるようになります。全体的に、ドキュメントの明確性と利便性が向上し、ユーザー体験が強化されています。

## articles/search/search-how-to-define-index-projections.md{#item-a7e2c5}

<details>
<summary>Diff</summary>
````diff
@@ -237,7 +237,7 @@ The `mappings` parameter is important. You must explicitly map every field in th
 
 This requirement is in contrast with other field mapping conventions in Azure AI Search. For some data source types, the indexer can implicitly map fields based on similar names, or known characteristics (for example, blob indexers use the unique metadata storage path as the default document key). However, for indexer projections, you must explicitly specify every field mapping on the "many" side of the relationship.
 
-<!-- Avoid creating a field mapping for the parent key field. Doing so disrupts change tracking and synchronized data refresh. -->
+Do not create a field mapping for the parent key field. Doing so disrupts change tracking and synchronized data refresh.
 
 ## Handling parent documents
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスプロジェクションの定義に関する注意事項の更新"
}
```

### Explanation
この変更は、「search-how-to-define-index-projections.md」というドキュメントの更新に関するもので、Azure AI Searchにおけるインデックスプロジェクションの定義に関する重要な注意事項が修正されています。具体的には、親キー領域に関するフィールドマッピングの扱いについての説明が明確化されています。

主な変更点は以下の通りです：

1. **文言の修正**：
   - コメントアウトされていた説明文が、明示的な注意事項として変更されました。具体的には、以前は「フィールドマッピングを作成しないこと」をコメントとして提示していましたが、今では「親キー領域のフィールドマッピングを作成しないでください。これにより、変更追跡とデータの同期更新が妨げられます。」という具体的な指示として記載されています。

この変更により、ユーザーは親キーフィールドに対するフィールドマッピングを避けるべき理由とその重要性を直接的に理解しやすくなります。全体的に、この修正はドキュメントの明確性を向上させ、ユーザーがインデックスプロジェクションを定義する際の注意点をより良く理解できるようにしています。


