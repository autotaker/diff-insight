---
date: '2024-10-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:43a3b87...MicrosoftDocs:e9690f5
summary: このコードディフでは、新機能の追加と既存のドキュメントやAPIの更新に焦点を当てています。主なハイライトには、テキスト分割スキルにおける新しい「unit」パラメータの導入、ハイブリッド検索の機能強化、ストレージ圧縮効果の向上が含まれています。また、一部の視覚的な情報が削除されたことで関連情報が失われる可能性がありますが、APIバージョン情報の更新やドキュメントの明確化が行われています。これにより、Azure
  AI Searchの機能が向上し、ユーザーがよりスムーズに最新技術を理解できるようになります。全体として、これらの改善はユーザーの検索精度を高め、利用のしやすさを向上させることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:43a3b87...MicrosoftDocs:e9690f5){target="_blank"}


# Highlights
このコードディフのハイライトは、新しい機能の追加と、既存のドキュメントやAPIの更新です。「テキスト分割」認知スキルやハイブリッド検索を含む複数のセクションで、機能が強化されています。特に、新しいパラメータやAPIバージョンの追加、関連スコアリングの強化による透明性の向上が重要なポイントです。

## New features
- テキスト分割スキルでの新しい「unit」パラメータの導入。
- ハイブリッド検索における新機能の追加とベクトルクエリのターゲットフィルタ機能。
- マトリョーシカ表現学習（MRL）関連の新技術によるストレージ圧縮の効果向上。

## Breaking changes
- 削除された図や視覚的なダイアグラムにより、関連情報が失われる可能性。

## Other updates
- 更新された最新のAPIバージョン情報。
- いくつかのドキュメントにおける日付の更新と説明の明確化。
- サンプル設定や実例の追加により、具体的な使用例が増加。

# Insights
このドキュメント更新は、多くの部分でAzure AI Searchの機能を改善し、ドキュメントをより詳細にわかりやすくすることを目的としています。特に、ハイブリッド検索の強化や、関連スコアの透明性向上に関する更新は、ユーザーの検索精度の向上に直接寄与します。また、新しいAPIバージョンやプレビュー機能に関する情報の追加により、ユーザーが最新の技術スタックを理解しやすくなっています。

認知スキル「テキスト分割」の更新では、パラメータの追加により設定の柔軟性が向上しました。これにより、ユーザーは必要に応じて様々なテキストサイズや形式をサポートできるようになり、他のスキルとの相互互換性も改善されています。

さらに、ドキュメントやダイアグラムの整理、削除および更新は、必要な情報へ迅速にアクセスできるようにするための努力として評価できます。削除された視覚資料に代わる新しいリソースが提供され、ユーザーにとっての理解が深まることが期待されます。

全体として、これらの更新はAzure AI Searchの機能性を拡張するとともに、開発者やユーザーの導入をより容易にし、最適化しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-textsplit.md](#item-9bf753) | minor update | テキスト分割の認知スキルに関するドキュメントの更新 | modified | 39 | 19 | 58 | 
| [hybrid-search-how-to-query.md](#item-345ce6) | minor update | ハイブリッド検索クエリの作成に関するドキュメントの更新 | modified | 74 | 15 | 89 | 
| [hybrid-search-overview.md](#item-6987b4) | minor update | ハイブリッド検索の概要ドキュメントの更新 | modified | 9 | 9 | 18 | 
| [hybrid-search-ranking.md](#item-dad887) | minor update | ハイブリッド検索のランキングに関するドキュメントの更新 | modified | 62 | 6 | 68 | 
| [search-scoring-flow.png](#item-a2c99a) | minor update | ハイブリッド検索のスコアリングフローダイアグラムの削除 | removed | 0 | 0 | 0 | 
| [search-api-migration.md](#item-07297b) | minor update | 検索API移行ガイドの更新 | modified | 8 | 2 | 10 | 
| [search-api-preview.md](#item-511f5d) | minor update | Azure AI Searchプレビュー機能の更新 | modified | 6 | 2 | 8 | 
| [toc.yml](#item-c4768f) | minor update | 検索APIの目次更新 | modified | 15 | 13 | 28 | 
| [vector-search-how-to-chunk-documents.md](#item-b79133) | minor update | 大規模文書のチャンク化方法の更新 | modified | 9 | 7 | 16 | 
| [vector-search-how-to-configure-compression-storage.md](#item-c653c3) | minor update | ベクトルサイズの圧縮ストレージ設定の更新 | modified | 115 | 4 | 119 | 
| [whats-new.md](#item-fa71b4) | minor update | 新機能と更新情報の追加 | modified | 22 | 12 | 34 | 


# Modified Contents
## articles/search/cognitive-search-skill-textsplit.md{#item-9bf753}

<details>
<summary>Diff</summary>
````diff
@@ -8,12 +8,19 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: reference
-ms.date: 08/05/2024
+ms.date: 10/01/2024
 ---
 
 # Text split cognitive skill
 
-The **Text Split** skill breaks text into chunks of text. You can specify whether you want to break the text into sentences or into pages of a particular length. This skill is especially useful if there are maximum text length requirements in other skills downstream. 
+> [!IMPORTANT] 
+> Some parameters are in public preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [preview REST API](/rest/api/searchservice/index-preview) supports these parameters.
+
+The **Text Split** skill breaks text into chunks of text. You can specify whether you want to break the text into sentences or into pages of a particular length. This skill is useful if there are maximum text length requirements in other skills downstream, such as embedding skills that pass data chunks to embedding models on Azure OpenAI and other model providers. For more information about this scenario, see [Chunk documents for vector search](vector-search-how-to-chunk-documents.md).
+
+Several parameters are version-specific. The skills parameter table notes the API version in which a parameter was introduced so that you know whether a [version upgrade](search-api-migration.md) is required. To use version-specific features such as *token chunking* in **2024-09-01-preview**, you can use the Azure portal, or target a REST API version, or check an Azure SDK change log to see if it supports the feature.
+
+The Azure portal supports most preview features and can be used to create or update a skillset. For updates to the Text Split skill, edit the skillset JSON definition to add new preview parameters. 
 
 > [!NOTE]
 > This skill isn't bound to Azure AI services. It's non-billable and has no Azure AI services key requirement.
@@ -23,41 +30,54 @@ Microsoft.Skills.Text.SplitSkill
 
 ## Skill Parameters
 
-Parameters are case-sensitive.
+Parameters are case-sensitive. 
 
-| Parameter name	 | Description |
-|--------------------|-------------|
-| `textSplitMode`    | Either `pages` or `sentences`. Pages have a configurable maximum length, but the skill attempts to avoid truncating a sentence so the actual length might be smaller. Sentences are a string that terminates at sentence-ending punctuation, such as a period, question mark, or exclamation point, assuming the language has sentence-ending punctuation. | 
-| `maximumPageLength` | Only applies if `textSplitMode` is set to `pages`. This parameter refers to the maximum page length in characters as measured by `String.Length`. The minimum value is 300, the maximum is 50000, and the default value is 5000.  The algorithm does its best to break the text on sentence boundaries, so the size of each chunk might be slightly less than `maximumPageLength`. | 
-| `pageOverlapLength` | Only applies if `textSplitMode` is set to `pages`. Each page starts with this number of characters from the end of the previous page. If this parameter is set to 0, there's no overlapping text on successive pages. This parameter is supported in [2024-07-01](/rest/api/searchservice/skillsets/create-or-update) and newer preview REST APIs, and in Azure SDK packages that have been updated to support integrated vectorization. This [example](#example-for-chunking-and-vectorization) includes the parameter. |
-| `maximumPagesToTake` | Only applies if `textSplitMode` is set to `pages`. Number of pages to return. The default is 0, which means to return all pages. You should set this value if only a subset of pages are needed. This parameter is supported in [2024-07-01](/rest/api/searchservice/skillsets/create-or-update) and newer preview REST APIs, and in Azure SDK packages that have been updated to support integrated vectorization. This [example](#example-for-chunking-and-vectorization) includes the parameter.|
-| `defaultLanguageCode`	| (optional) One of the following language codes: `am, bs, cs, da, de, en, es, et, fr, he, hi, hr, hu, fi, id, is, it, ja, ko, lv, no, nl, pl, pt-PT, pt-BR, ru, sk, sl, sr, sv, tr, ur, zh-Hans`. Default is English (en). A few things to consider: <ul><li>Providing a language code is useful to avoid cutting a word in half for nonwhitespace languages such as Chinese, Japanese, and Korean.</li><li>If you don't know the language  in advance (for example, if you're using the [LanguageDetectionSkill](cognitive-search-skill-language-detection.md) to detect language), we recommend the `en` default. </li></ul>  |
+| Parameter name     | Version   | Description |
+|--------------------|-------------|-------------|
+| `textSplitMode`    | All versions | Either `pages` or `sentences`. Pages have a configurable maximum length, but the skill attempts to avoid truncating a sentence so the actual length might be smaller. Sentences are a string that terminates at sentence-ending punctuation, such as a period, question mark, or exclamation point, assuming the language has sentence-ending punctuation. | 
+| `maximumPageLength` | All versions | Only applies if `textSplitMode` is set to `pages`. For `unit` set to `characters`, this parameter refers to the maximum page length in characters as measured by `String.Length`. The minimum value is 300, the maximum is 50000, and the default value is 5000.  The algorithm does its best to break the text on sentence boundaries, so the size of each chunk might be slightly less than `maximumPageLength`. <br><br>For `unit` set to `azureOpenAITokens`, the maximum page length is the token length limit of the model. For text embedding models, a general recommendation for page length is 512 tokens. |
+| `defaultLanguageCode`	| All versions | (optional) One of the following language codes: `am, bs, cs, da, de, en, es, et, fr, he, hi, hr, hu, fi, id, is, it, ja, ko, lv, no, nl, pl, pt-PT, pt-BR, ru, sk, sl, sr, sv, tr, ur, zh-Hans`. Default is English (en). A few things to consider: <ul><li>Providing a language code is useful to avoid cutting a word in half for nonwhitespace languages such as Chinese, Japanese, and Korean.</li><li>If you don't know the language  in advance (for example, if you're using the [LanguageDetectionSkill](cognitive-search-skill-language-detection.md) to detect language), we recommend the `en` default. </li></ul>  |
+| `pageOverlapLength` | [2024-07-01](/rest/api/searchservice/skillsets/create-or-update) | Only applies if `textSplitMode` is set to `pages`. Each page starts with this number of characters or tokens from the end of the previous page. If this parameter is set to 0, there's no overlapping text on successive pages. This [example](#example-for-chunking-and-vectorization) includes the parameter. |
+| `maximumPagesToTake` | [2024-07-01](/rest/api/searchservice/skillsets/create-or-update) | Only applies if `textSplitMode` is set to `pages`. Number of pages to return. The default is 0, which means to return all pages. You should set this value if only a subset of pages are needed. This [example](#example-for-chunking-and-vectorization) includes the parameter.|
+| `unit` | [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | **New**. Only applies if `textSplitMode` is set to `pages`. Specifies whether to chunk by `characters` (default) or `azureOpenAITokens`. Setting the unit affects `maximumPageLength` and `pageOverlapLength`. |
+| `azureOpenAITokenizerParameters` | [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | **New**. An object providing extra parameters for the `azureOpenAITokens` unit. <br><br>`encoderModelName` is a designated tokenizer used for converting text into tokens, essential for natural language processing (NLP) tasks. Different models use different tokenizers. Valid values include cl100k_base (default) used by GPT-35-Turbo and GPT-4. Other valid values are r50k_base, p50k_base, and p50k_edit. The skill implements the tiktoken library by way of [SharpToken](https://www.nuget.org/packages/SharpToken) and `Microsoft.ML.Tokenizers` but doesn't support every encoder. For example, there's currently no support for o200k_base encoding used by GPT-4o. <br><br>`allowedSpecialTokens` defines a collection of special tokens that are permitted within the tokenization process. Special tokens are  string that you want to treat uniquely, ensuring they aren't split during tokenization. For example ["[START"], "[END]"].|
 
 ## Skill Inputs
 
 | Parameter name	   | Description      |
 |----------------------|------------------|
-| `text`	| The text to split into substring. |
-| `languageCode`	| (Optional) Language code for the document. If you don't know the language of the text inputs (for example, if you're using [LanguageDetectionSkill](cognitive-search-skill-language-detection.md) to detect the language), you can omit this parameter. If you set `languageCode` to a language isn't in the supported list for the `defaultLanguageCode`, a warning is emitted and the text isn't split.  |
+| `text` | The text to split into substring. |
+| `languageCode` | (Optional) Language code for the document. If you don't know the language of the text inputs (for example, if you're using [LanguageDetectionSkill](cognitive-search-skill-language-detection.md) to detect the language), you can omit this parameter. If you set `languageCode` to a language isn't in the supported list for the `defaultLanguageCode`, a warning is emitted and the text isn't split.  |
 
 ## Skill Outputs 
 
 | Parameter name	 | Description |
 |--------------------|-------------|
-| `textItems` | Output is an array of substrings that were extracted. `textItems` is the default name of the output. `targetName` is optional, but if you have multiple Text Split skills, make sure to set `targetName` so that you don't overwrite the data from the first skill with the second one. If `targetName` is set, use it in output field mappings or in downstream skills that use the skill output.|
+| `textItems` | Output is an array of substrings that were extracted. `textItems` is the default name of the output. <br><br>`targetName` is optional, but if you have multiple Text Split skills, make sure to set `targetName` so that you don't overwrite the data from the first skill with the second one. If `targetName` is set, use it in output field mappings or in downstream skills that consume the skill output, such as an embedding skill.|
 
 ## Sample definition
 
 ```json
 {
-    "@odata.type": "#Microsoft.Skills.Text.SplitSkill",
-    "textSplitMode" : "pages", 
-    "maximumPageLength": 1000,
-    "defaultLanguageCode": "en",
+    "name": "SplitSkill", 
+    "@odata.type": "#Microsoft.Skills.Text.SplitSkill", 
+    "description": "A skill that splits text into chunks", 
+    "context": "/document", 
+    "defaultLanguageCode": "en", 
+    "textSplitMode": "pages", 
+    "unit": "azureOpenAITokens", 
+    "azureOpenAITokenizerParameters":{ 
+        "encoderModelName":"cl100k", 
+        "allowedSpecialTokens": [ 
+            "[START]", 
+            "[END]" 
+        ] 
+    },
+    "maximumPageLength": 512,
     "inputs": [
         {
             "name": "text",
-            "source": "/document/content"
+            "source": "/document/text"
         },
         {
             "name": "languageCode",
@@ -67,7 +87,7 @@ Parameters are case-sensitive.
     "outputs": [
         {
             "name": "textItems",
-            "targetName": "mypages"
+            "targetName": "pages"
         }
     ]
 }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト分割の認知スキルに関するドキュメントの更新"
}
```

### Explanation
この変更は、「テキスト分割」認知スキルに関連するMarkdownドキュメントに対して行われました。主なポイントは以下のとおりです。

1. **日付の更新**: 最新の更新日が2024年10月1日に変更されました。

2. **重要な情報の追加**: 公開プレビューに関する重要情報が追加され、関連するREST APIがそのプレビュー機能をサポートすることが説明されています。

3. **説明の詳細化**: 「テキスト分割」スキルの説明が強化され、特に他のスキルでの最大テキスト長要件にどのように対応するかが具体的に記述されています。

4. **パラメータに関する情報の強化**: バージョンごとのパラメータテーブルが追加され、各パラメータがどのAPIバージョンで導入されたかが明記されています。これにより、バージョンごとの特定機能の使用についての理解が深まりました。

5. **新しいパラメータの追加**: いくつかの新しいパラメータが追加され、特に「unit」パラメータが新たに導入されました。このパラメータは、ページ分割を「文字数」または「azureOpenAITokens」に設定できます。

6. **サンプル定義の更新**: サンプル設定も更新され、パラメータの構成が具体的に示されています。特に、テキストを処理する際の各パラメータの適用例が強調されています。

全体として、この変更は「テキスト分割」認知スキルの機能や利用方法に関する情報を改善し、ユーザーがスキルをより効果的に利用できるようにすることを目的としています。

## articles/search/hybrid-search-how-to-query.md{#item-345ce6}

<details>
<summary>Diff</summary>
````diff
@@ -9,46 +9,58 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 08/05/2024
+ms.date: 10/01/2024
 ---
 
 # Create a hybrid query in Azure AI Search
 
-[Hybrid search](hybrid-search-overview.md) combines one or more text (keyword) queries with one or more vector queries in a single search request. The queries execute in parallel. The results are merged and reordered by new search scores, using [Reciprocal Rank Fusion (RRF)](hybrid-search-ranking.md) to return a unified result set.
+[Hybrid search](hybrid-search-overview.md) combines text (keyword) and vector queries in a single search request. All subqueries in the request execute in parallel. The results are merged and reordered by new search scores, using [Reciprocal Rank Fusion (RRF)](hybrid-search-ranking.md) to return a unified result set. In many cases, [per benchmark tests](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-ai-search-outperforming-vector-search-with-hybrid/ba-p/3929167), hybrid queries with semantic ranking return the most relevant results.
 
-In many cases, [per benchmark tests](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-ai-search-outperforming-vector-search-with-hybrid/ba-p/3929167), hybrid queries with semantic ranking return the most relevant results.
+In this article, learn how to:
 
-To improve relevance, use these parameters:
++ Set up a basic request
++ Formulate hybrid queries with more parameters and filters
++ Improve relevance using semantic ranking or vector weights
++ Optimize query behaviors by controlling text and vector inputs
+
+> [!NOTE]
+> New in [**2024-09-01-preview**](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true) is the ability to target filters to just the vector subqueries in a hybrid request. This gives you more precision over how filters are applied. For more information, see [targeting filters to vector subqueries](#hybrid-search-with-filters-targeting-vector-subqueries-preview) in this article.
+
+<!-- To improve relevance in a hybrid query, use these parameters:
 
 + [vector.queries.weight](vector-search-how-to-query.md#vector-weighting) lets you set the relative weight of the vector query. This feature is particularly useful in complex queries where two or more distinct result sets need to be combined, as is the case for hybrid search. This feature is generally available.
 
 + [hybridsearch.maxTextRecallSize and countAndFacetMode (preview)](#set-maxtextrecallsize-and-countandfacetmode-preview) give you more control over text inputs into a hybrid query. This feature requires a preview API version.
-
+ -->
 ## Prerequisites
 
-+ A search index containing `searchable` vector and nonvector fields. See [Create an index](search-how-to-create-search-index.md) and [Add vector fields to a search index](vector-search-how-to-create-index.md).
++ A search index containing `searchable` vector and nonvector fields. We recommend the [Import and vectorize data wizard](search-import-data-portal.md) to create an index quickly. Otherwise, see [Create an index](search-how-to-create-search-index.md) and [Add vector fields to a search index](vector-search-how-to-create-index.md).
 
 + (Optional) If you want the [semantic ranker](semantic-search-overview.md), your search service must be Basic tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
-+ (Optional) If you want text-to-vector conversion of a query string, [create and assign a vectorizer](vector-search-how-to-configure-vectorizer.md) to vector fields in the search index.
++ (Optional) If you want built-in text-to-vector conversion of a query string, [create and assign a vectorizer](vector-search-how-to-configure-vectorizer.md) to vector fields in the search index.
 
 ## Choose an API or tool
 
-+ [**2024-07-01**](/rest/api/searchservice/documents/search-post) stable version or a recent preview API version if you're using [maxTextRecallSize and countAndFacetMode(preview)](#set-maxtextrecallsize-and-countandfacetmode-preview).
-+ Search Explorer in the Azure portal (targets 2024-05-01-preview behaviors)
-+ Newer stable or beta packages of the Azure SDKs (see change logs for SDK feature support)
++ Search Explorer in the Azure portal (supports both stable and preview API search syntax) has a JSON view that lets you paste in a hybrid request.
+
++ [**2024-07-01**](/rest/api/searchservice/documents/search-post) stable version or a recent preview API version if you're using preview features like [maxTextRecallSize and countAndFacetMode(preview)](#set-maxtextrecallsize-and-countandfacetmode-preview).
 
-## Run a hybrid query in Search Explorer
+  For readability, we use REST examples to explain how the APIs work. You can use a REST client like Visual Studio Code with the REST extension to build hybrid queries. For more information, see [Quickstart: Vector search using REST APIs](search-get-started-vector.md).
 
-1. In [Search Explorer](search-explorer.md), make sure the API version is **2024-07-01** or newer preview API versions.
++ Newer stable or beta packages of the Azure SDKs (see change logs for SDK feature support).
 
-1. Under **View**, select **JSON view**. 
+## Set up a hybrid query in Search Explorer
 
-1. Replace the default query template with a hybrid query, such as the one starting on line 539 for the [vector quickstart example](vector-search-how-to-configure-vectorizer.md#try-a-vectorizer-with-sample-data). For brevity, the vector is truncated in this article. 
+1. In [Search Explorer](search-explorer.md), make sure the API version is **2024-07-01** or a newer preview API version.
+
+1. Under **View**, select **JSON view** so that you can paste in a vector query. 
+
+1. Replace the default query template with a hybrid query, such as the "Run a hybrid query" example starting on line 539 in the [vector quickstart](https://raw.githubusercontent.com/Azure-Samples/azure-search-rest-samples/refs/heads/main/Quickstart-vectors/az-search-vector-quickstart.rest). For brevity, the vector is truncated in this article. 
 
    A hybrid query has a text query specified in `search`, and a vector query specified under `vectorQueries.vector`.
 
-   The text query and vector query should be equivalent or at least not conflict. If the queries are different, you don't get the benefit of hybrid.
+   The text query and vector query can be equivalent or divergent, but it's common for them to share the same intent.
 
     ```json
     {
@@ -70,6 +82,9 @@ To improve relevance, use these parameters:
 
 1. Select **Search**.
 
+> [!TIP]
+> Search results are easier to read if you hide the vectors. In **Query Options**, turn on **Hide vector values in search results**.
+
 ## Hybrid query request (REST API)
 
 A hybrid query combines text search and vector search, where the `search` parameter takes a query string and `vectorQueries.vector` takes the vector query. The search engine runs full text and vector queries in parallel. The union of all matches is evaluated for relevance using Reciprocal Rank Fusion (RRF) and a single result set is returned in the response.
@@ -165,6 +180,50 @@ api-key: {{admin-api-key}}
 
 + When you postfilter query results, the number of results might be less than top-n.
 
+## Hybrid search with filters targeting vector subqueries (preview)
+
+Using [**2024-09-01-preview**](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true), you can override a global filter on the search request by applying a secondary filter that targets just the vector subqueries in a hybrid request.
+
+This feature provides fine-grained control by ensuring that filters only influence the vector search results, leaving keyword-based search results unaffected. 
+
+The targeted filter fully overrides the global filter, including any filters used for [security trimming](search-security-trimming-for-azure-search.md) or geospatial search.  In cases where global filters are required, such as security trimming, you must explicitly include these filters in both the top-level filter and in each vector-level filter to ensure security and other constraints are consistently enforced.
+
+To apply targeted vector filters:
+
++ Use the [latest preview Search Documents REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true#request-body) or an Azure SDK beta package that provides the feature.
+
++ Modify a query request, adding a new `vectorQueries.filterOverride` parameter set to an [OData filter expression](search-query-odata-filter.md).
+
+Here's an example of hybrid query that adds a filter override. The global filter "Rating gt 3" is replaced at run time by the filterOvrride.
+
+```http
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-09-01=preview
+
+{
+    "vectorQueries": [
+        {
+            "vector": [
+                -0.009154141,
+                0.018708462,
+                . . . 
+                -0.02178128,
+                -0.00086512347
+            ],
+            "fields": "DescriptionVector",
+            "kind": "vector",
+            "exhaustive": true,
+            "filterOverride": "Address/City eq 'Seattle'",
+            "k": 10
+        }
+    ],
+    "search": "historic hotel walk to restaurants and shopping",
+    "select": "HotelName, Description, Address/City, Rating",
+    "filter": "Rating gt 3"
+    "debug": "vector",
+    "top": 10
+}
+```
+
 ## Semantic hybrid search
 
 Assuming that you [enabled semantic ranker](semantic-how-to-enable-disable.md) and your index definition includes a [semantic configuration](semantic-how-to-query-request.md), you can formulate a query that includes vector search and keyword search, with semantic ranking over the merged result set. Optionally, you can add captions and answers. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索クエリの作成に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるハイブリッド検索クエリの作成に関するドキュメントに対する更新です。主な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの更新日が2024年10月1日に変更されました。

2. **説明の簡略化と明確化**: ハイブリッド検索の概要説明が更新され、テキストクエリとベクトルクエリの関係が明確にされています。これにより、ユーザーがクエリの実行方法を理解しやすくなります。

3. **新機能の追加情報**: 2024年9月1日プレビューで導入された新機能が記載されており、ベクトルサブクエリに特化したフィルタの適用についての詳細が説明されています。これにより、ユーザーはクエリの精度を高める方法についての情報を得られます。

4. **追加パラメータと機能の紹介**: パラメータに関する情報が強化され、特に「vector.queries.weight」や「maxTextRecallSize」などの機能について具体的な使用例が示されています。

5. **クエリ設定の手順**: AzureポータルのSearch Explorerを使用してハイブリッドクエリをセットアップするための手順が整理され、視覚的に分かりやすく説明されています。

6. **実例の提供**: ハイブリッドクエリのリクエスト形式の例が追加され、具体的にどのようにリクエストを構成するかが示されています。

これらの変更により、ユーザーはハイブリッド検索の実行方法をより理解しやすくなり、APIの新機能を活用できるようになっています。また、クエリの精度向上に向けた具体的なガイダンスが提供されています。

## articles/search/hybrid-search-overview.md{#item-6987b4}

<details>
<summary>Diff</summary>
````diff
@@ -9,12 +9,12 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 08/19/2024
+ms.date: 10/01/2024
 ---
 
 # Hybrid search using vectors and full text in Azure AI Search
 
-Hybrid search is a combination of full text and vector queries that execute against a search index that contains both searchable plain text content and generated embeddings. For query purposes, hybrid search is:
+Hybrid search is a combination of full text and vector queries that execute against a search index containing both searchable plain text content and generated embeddings. For query purposes, hybrid search is:
 
 + A single query request that includes both `search` and `vectors` query parameters
 + Executing in parallel
@@ -26,13 +26,13 @@ This article explains the concepts, benefits, and limitations of hybrid search.
 
 In Azure AI Search, vector fields containing embeddings can live alongside textual and numerical fields, allowing you to formulate hybrid queries that execute in parallel. Hybrid queries can take advantage of existing functionality like filtering, faceting, sorting, scoring profiles, and [semantic ranking](semantic-search-overview.md) in a single search request.
 
-Hybrid search combines results from both full text and vector queries, which use different ranking functions such as BM25 and HNSW. A [Reciprocal Rank Fusion (RRF)](hybrid-search-ranking.md) algorithm merges the results. The query response provides just one result set, using RRF to pick the most relevant matches from each query.
+Hybrid search combines results from both full text and vector queries, which use different ranking functions such as BM25, HNSW, and EKNN. A [Reciprocal Rank Fusion (RRF)](hybrid-search-ranking.md) algorithm merges the results. The query response provides just one result set, using RRF to rank the unified results.
 
 ## Structure of a hybrid query
 
-Hybrid search is predicated on having a search index that contains fields of various [data types](/rest/api/searchservice/supported-data-types), including plain text and numbers, geo coordinates for geospatial search, and vectors for a mathematical representation of a chunk of text. You can use almost all query capabilities in Azure AI Search with a vector query, except for client-side interactions such as autocomplete and suggestions.
+Hybrid search is predicated on having a search index that contains fields of various [data types](/rest/api/searchservice/supported-data-types), including plain text and numbers, geo coordinates if you want geospatial search, and vectors for a mathematical representation of a chunk of text. You can use almost all query capabilities in Azure AI Search with a vector query, except for pure text client-side interactions such as autocomplete and suggestions.
 
-A representative hybrid query might be as follows (notice the vector is trimmed for brevity):
+A representative hybrid query might be as follows (notice that the vector queries have placeholder values for brevity):
 
 ```http
 POST https://{{searchServiceName}}.search.windows.net/indexes/hotels-vector-quickstart/docs/search?api-version=2024-07-01
@@ -63,12 +63,12 @@ POST https://{{searchServiceName}}.search.windows.net/indexes/hotels-vector-quic
 
 Key points include:
 
-+ `search` specifies a full text search query.
++ `search` specifies a single full text search query.
 + `vectors` for vector queries, which can be multiple, targeting multiple vector fields. If the embedding space includes multi-lingual content, vector queries can find the match with no language analyzers or translation required.
-+ `select` specifies which fields to return in results, which can be text fields that are human readable.
++ `select` specifies which fields to return in results, which should be text fields that are human readable.
 + `filters` can specify geospatial search or other include and exclude criteria, such as whether parking is included. The geospatial query in this example finds hotels within a 300-kilometer radius of Washington D.C.
 + `facets` can be used to compute facet buckets over results that are returned from hybrid queries.
-+ `queryType=semantic` invokes semantic ranker, applying machine reading comprehension to surface more relevant search results.
++ `queryType=semantic` invokes semantic ranker, applying machine reading comprehension to surface more relevant search results. Semantic ranking is optional. If you aren't using that feature, remove the last three lines of the hybrid query.
 
 Filters and facets target data structures within the index that are distinct from the inverted indexes used for full text search and the vector indexes used for vector search. As such, when filters and faceted operations execute, the search engine can apply the operational result to the hybrid search results in the response.
 
@@ -122,7 +122,7 @@ A response from the above query might look like this:
 
 ## Why choose hybrid search?
 
-Hybrid search combines the strengths of vector search and keyword search. The advantage of vector search is finding information that's conceptually similar to your search query, even if there are no keyword matches in the inverted index. The advantage of keyword or full text search is precision, with the ability to apply semantic ranking that improves the quality of the initial results. Some scenarios - such as querying over product codes, highly specialized jargon, dates, and people's names - can perform better with keyword search because it can identify exact matches.
+Hybrid search combines the strengths of vector search and keyword search. The advantage of vector search is finding information that's conceptually similar to your search query, even if there are no keyword matches in the inverted index. The advantage of keyword or full text search is precision, with the ability to apply optional semantic ranking that improves the quality of the initial results. Some scenarios - such as querying over product codes, highly specialized jargon, dates, and people's names - can perform better with keyword search because it can identify exact matches.
 
 Benchmark testing on real-world and benchmark datasets indicates that hybrid retrieval with semantic ranker offers significant benefits in search relevance.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索の概要ドキュメントの更新"
}
```

### Explanation
この変更は、「ハイブリッド検索の概要」に関するドキュメントの更新を含みます。主な要点は以下の通りです。

1. **日付の変更**: ドキュメントの更新日が2024年10月1日に変更されました。

2. **説明の微調整**: ハイブリッド検索の説明が一部見直され、特に「検索可能なプレーン テキストコンテンツと生成された埋め込みを含む検索インデックス」に関する表現が改善されました。この変更により、ハイブリッド検索がどのように機能するかがより明確になります。

3. **新しいランキング関数の追加**: 以前の説明に「EKNN」という新しいランキング関数が追加され、ハイブリッド検索の結果がどのようにマージされるかに関する情報が強化されました。

4. **クエリの構造に関する情報の明確化**: ハイブリッド検索が異なるデータ型を含む検索インデックスに基づくという点についての説明が微調整され、特にテキストと数値、地理情報、ベクトルの表現が強調されています。

5. **クエリの例の修正**: サンプルのハイブリッドクエリの説明が若干改善され、記述の明快さが向上しました。特に、ベクトルクエリのプレースホルダの使用に関する注意が加えられています。

6. **ハイブリッド検索の利点**: ハイブリッド検索がどうして有利であるかという説明が強化され、特にオプションのセマンティックランキングを適用することで初期結果の質が向上することが強調されています。

このように、全体としてドキュメントの内容はより分かりやすく、ユーザーがハイブリッド検索の機能や利点を理解しやすくなるよう改善されています。

## articles/search/hybrid-search-ranking.md{#item-dad887}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 09/24/2024
+ms.date: 10/01/2024
 ---
 
 # Relevance scoring in hybrid search using Reciprocal Rank Fusion (RRF)
@@ -18,6 +18,9 @@ Reciprocal Rank Fusion (RRF) is an algorithm that evaluates the search scores fr
 
 RRF is based on the concept of *reciprocal rank*, which is the inverse of the rank of the first relevant document in a list of search results. The goal of the technique is to take into account the position of the items in the original rankings, and give higher importance to items that are ranked higher in multiple lists. This can help improve the overall quality and reliability of the final ranking, making it more useful for the task of fusing multiple ordered search results.
 
+> [!NOTE]
+> New in [**2024-09-01-preview**](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true) is the ability to deconstruct an RRF-ranked search score into its component subscores. This gives you transparency into all-up score composition. For more information, see [unpack search scores (preview)](#unpack-a-search-score-into-subscores-preview) in this article.
+
 ## How RRF ranking works
 
 RRF works by taking the search results from multiple methods, assigning a reciprocal rank score to each document in the results, and then combining the scores to create a new ranking. The concept is that documents appearing in the top positions across multiple search methods are likely to be more relevant and should be ranked higher in the combined result.
@@ -57,9 +60,62 @@ The following chart identifies the scoring property returned on each match, algo
 
 Semantic ranking occurs after RRF merging of results. Its score (`@search.rerankerScore`) is always reported separately in the query response. Semantic ranker can rerank full text and hybrid search results, assuming those results include fields having semantically rich content. It can rerank pure vector queries if the search documents include text fields that contain semantically relevant content.
 
+## Unpack a search score into subscores (preview)
+
+Using [**2024-09-01-preview**](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true), you can deconstruct a search score to view its subscores.
+
+For vector queries, this information can help you determine an appropriate value for [vector weighting](vector-search-how-to-query.md#vector-weighting) or [setting minimum thresholds](vector-search-how-to-query.md#set-thresholds-to-exclude-low-scoring-results-preview).
+
+To get subscores:
+
++ Use the [latest preview Search Documents REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true#request-body) or an Azure SDK beta package that provides the feature.
+
++ Modify a query request, adding a new `debug` parameter set to either `vector`, `semantic` if using semantic ranker, or `all`.
+
+Here's an example of hybrid query that returns subscores in debug mode:
+
+```http
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-09-01=preview
+
+{
+    "vectorQueries": [
+        {
+            "vector": [
+                -0.009154141,
+                0.018708462,
+                . . . 
+                -0.02178128,
+                -0.00086512347
+            ],
+            "fields": "DescriptionVector",
+            "kind": "vector",
+            "exhaustive": true,
+            "k": 10
+        },
+        {
+            "vector": [
+                -0.009154141,
+                0.018708462,
+                . . . 
+                -0.02178128,
+                -0.00086512347
+            ],
+            "fields": "DescriptionVector",
+            "kind": "vector",
+            "exhaustive": true,
+            "k": 10
+        }
+    ],
+    "search": "historic hotel walk to restaurants and shopping",
+    "select": "HotelName, Description, Address/City",
+    "debug": "vector",
+    "top": 10
+}
+```
+
 ## Weighted scores
 
-Using 2024-07-01 and newer preview API versions, you can [weight vector queries](vector-search-how-to-query.md#vector-weighting) to increase or decrease their importance in a hybrid query.
+Using [**2024-07-01**](/rest/api/searchservice/documents/search-post) and newer preview API versions, you can [weight vector queries](vector-search-how-to-query.md#vector-weighting) to increase or decrease their importance in a hybrid query.
 
 Recall that when computing RRF for a certain document, the search engine looks at the rank of that document for each result set where it shows up. Assume a document shows up in three separate search results, where the results are from two vector queries and one text BM25-ranked query. The position of the document varies in each result.
 
@@ -69,9 +125,9 @@ Recall that when computing RRF for a certain document, the search engine looks a
 | vector results two | position 5 | 0.81514114 | 2.0 | 1.63028228 |
 | BM25 results | position 10  | 0.8577363 | NA | 0.8577363 |
 
-The document's position in each result set corresponds to an initial score, which are added up to create the final RRF score for that document. 
+The document's position in each result set corresponds to an initial score, which is added up to create the final RRF score for that document. 
 
-If you add vector weighting, the initial scores are subect to a weighting multiplier that increases or decreases the score. The default is 1.0, which means no weighting and the initial score is used as-is in RRF scoring. However, if you add a weight of 0.5, the score is reduced and that result becomes less important in the combined ranking. Conversely, if you add a weight of 2.0, the score becomes a larger factor in the overall RRF score.
+If you add vector weighting, the initial scores are subject to a weighting multiplier that increases or decreases the score. The default is 1.0, which means no weighting and the initial score is used as-is in RRF scoring. However, if you add a weight of 0.5, the score is reduced and that result becomes less important in the combined ranking. Conversely, if you add a weight of 2.0, the score becomes a larger factor in the overall RRF score.
 
 In this example, the @search.score (weighted) values are passed to the RRF ranking model.
 
@@ -87,9 +143,9 @@ For more information, see [How to work with search results](search-pagination-pa
 
 ## Diagram of a search scoring workflow
 
-The following diagram illustrates a hybrid query that invokes keyword and vector search, with boosting through scoring profiles, and semantic ranking.
+The following diagram illustrates a hybrid query that invokes keyword and vector search, with [boosting through scoring profiles](index-add-scoring-profiles.md#how-search-scoring-works-in-azure-ai-search), and semantic ranking.
 
-:::image type="content" source="media/hybrid-search/search-scoring-flow.png" alt-text="Diagram of prefilters." border="true" lightbox="media/hybrid-search/search-scoring-flow.png":::
+:::image type="content" source="media/scoring-profiles/scoring-over-ranked-results.png" alt-text="Diagram of prefilters." border="true" lightbox="media/scoring-profiles/scoring-over-ranked-results.png":::
 
 A query that generates the previous workflow might look like this:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索のランキングに関するドキュメントの更新"
}
```

### Explanation
この変更は、ハイブリッド検索における関連スコアリングと、逆相互ランキング融合（Reciprocal Rank Fusion: RRF）に関するドキュメントの更新を反映しています。主なポイントは以下の通りです。

1. **日付の更新**: ドキュメントの更新日が2024年10月1日に変更されました。

2. **RRFの機能強化および説明**: RRFのスコアの構成要素を分解して表示する新機能が追加され、これによりスコアの透明性が向上します。この情報は、スコア計算の理解を深めるのに役立ちます。

3. **セマンティックランキングの明確化**: RRFによる結果のマージ後にセマンティックランキングが行われることが強調され、どのようにスコアが分けられるかが説明されています。

4. **サブスコアの取得方法の追加**: 新しい「unpack a search score into subscores」というセクションが追加され、サブスコアを取得する手順が詳述されています。これは、ベクトルクエリの重み付けや適切な評価基準を設定する際に役立ちます。

5. **重み付けスコアの更新**: ベクトルクエリの重み付けに関する情報が更新され、スコアリングに対する重みの効果とその計算方法がより明確に説明されています。

6. **図の改善**: 検索スコアリングのワークフローを示す図のソースが更新され、視覚的に表現された情報が最新の内容にマッチしています。

このように、ドキュメントはRRFによる関連スコアの計算方法と、セマンティックランキング、サブスコアの取り扱いについての理解を深めるために更新されており、ユーザーがハイブリッド検索でのスコアリングの仕組みをよりよく理解できるように配慮されています。

## articles/search/media/hybrid-search/search-scoring-flow.png{#item-a2c99a}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索のスコアリングフローダイアグラムの削除"
}
```

### Explanation
この変更は、ハイブリッド検索に関連するスコアリングフローを示すダイアグラム(`search-scoring-flow.png`)が削除されたことを示しています。この画像は、検索クエリの実行時におけるスコアリングのプロセスを視覚的に示すために用いられていました。削除の理由は明示されていませんが、コンテンツの更新や改善の一環として、より適切な図や視覚要素が導入される可能性があります。

全体として、この変更により、ユーザーは関連スコアリングのフローに関するビジュアル情報を失うことになりますが、他のドキュメントやリソースで補完されることが期待されます。新しい情報や図が追加されることにより、より良い理解を促進することが目的であると考えられます。

## articles/search/search-api-migration.md{#item-07297b}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: conceptual
-ms.date: 08/05/2024
+ms.date: 10/01/2024
 ---
 
 # Upgrade to the latest REST API in Azure AI Search
@@ -20,7 +20,7 @@ Use this article to migrate data plane calls to newer versions of the [**Search
 
 + [`2024-07-01`](/rest/api/searchservice/search-service-api-versions#2024-07-01) is the most recent stable version.
 
-+ [`2024-05-01-preview`](/rest/api/searchservice/search-service-api-versions#2024-05-01-preview) is the most recent preview API version. 
++ [`2024-09-01-preview`](/rest/api/searchservice/search-service-api-versions#2024-09-01-preview) is the most recent preview API version. 
 
 Upgrade instructions focus on code changes that get you through breaking changes from previous versions so that existing code runs the same as before, but on the newer API version. Once your code is in working order, you can decide whether to adopt newer features. To learn more about new features, see [vector code samples](https://github.com/Azure/azure-search-vector-samples) and [What's New](whats-new.md).
 
@@ -73,6 +73,12 @@ Effective March 29, 2024 and applicable to all [supported REST APIs](/rest/api/s
 
 See [Migrate from preview version](semantic-how-to-configure.md#migrate-from-preview-versions) to transition your code to use `semanticConfiguration`.
 
+## Upgrade to 2024-09-01-preview
+
+[`2024-09-01-preview`](/rest/api/searchservice/search-service-api-versions#2024-09-01-preview) adds Matryoshka Representation Learning (MRL) compression for text-embedding-3 models, targeted vector filtering for hybrid queries, vector subscore details for debugging, and token chunking for [Text Split skill](cognitive-search-skill-textsplit.md).
+
+If you're upgrading from `2024-05-01-preview`, you can use the new preview APIs with no change to existing code.
+
 ## Upgrade to 2024-07-01
 
 [`2024-07-01`](/rest/api/searchservice/search-service-api-versions#2024-07-01) is a general release. The former preview features are now generally available: integrated chunking and vectorization (Text Split skill, AzureOpenAIEmbedding skill), query vectorizer based on AzureOpenAIEmbedding, vector compression (scalar quantization, binary quantization, stored property, narrow data types).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索API移行ガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchの検索API移行に関するドキュメントの更新を示しています。主な修正点は次のとおりです。

1. **日付の更新**: ドキュメントの更新日が2024年8月5日から2024年10月1日に変更されました。

2. **最新のAPIバージョンの情報更新**: 最新の安定版APIバージョンが「2024-07-01」として追加され、最も新しいプレビューAPIバージョンが「2024-09-01-preview」に更新されました。これにより、開発者は最新のAPIのリリース状況を把握しやすくなります。

3. **マトリョーシカ表現学習（MRL）について**: 新しいプレビューアップグレード（2024-09-01-preview）に関する詳細情報が追加され、特にテキスト埋め込みモデルに対するMRL圧縮、ハイブリッドクエリのためのベクトルフィルタリング、デバッグ用のベクトルサブスコアの詳細、テキスト分割スキルに対するトークンチャンク処理について触れられています。

4. **アップグレード手順の明確化**: 「2024-05-01-preview」からの移行に関して、既存のコードに変更を加えずに新しいプレビューAPIを使用できる旨が示され、移行の容易さが強調されています。

この更新は、開発者が最新のAPI機能を理解し、迅速に移行するための参考となるように設計されています。また、新機能や変更の影響を考慮しながら、スムーズにシステムをアップグレードできるよう支援しています。

## articles/search/search-api-preview.md{#item-511f5d}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: cognitive-search
 ms.custom:
   - build-2024
 ms.topic: conceptual
-ms.date: 08/05/2024
+ms.date: 10/01/2024
 ---
 
 # Preview features in Azure AI Search
@@ -25,6 +25,10 @@ Preview features are removed from this list if they're retired or transition to
 
 |Feature&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Category | Description | Availability  |
 |---------|------------------|-------------|---------------|
+| [**Lower the dimension requirements for MRL-trained text embedding models on Azure OpenAI**](vector-search-how-to-configure-compression-storage.md#use-mrl-compression-and-truncated-dimensions-preview) | Feature | Text-embedding-3-small and Text-embedding-3-large are trained using Matryoshka Representation Learning (MRL). This allows you to truncate the embedding vectors to fewer dimensions, and adjust the balance between vector index size usage and retrieval quality. A new `truncationDimension` provides the MRL behaviors as an additional parameter in a vector compression configuration. This can only be configured for new vector fields. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
+| [**Unpack `@search.score` to view subscores in hybrid search results**](hybrid-search-ranking.md#unpack-a-search-score-into-subscores-preview) | Feature | You can investigate Reciprocal Rank Fusion (RRF) ranked results by viewing the individual query subscores of the final merged and scored result. A new `debug` property unpacks the search score. `QueryResultDocumentSubscores`, `QueryResultDocumentRerankerInput`, and `QueryResultDocumentSemanticField` provide the extra detail. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
+| [**Target filters in a hybrid search to just the vector queries**](hybrid-search-how-to-query.md#hybrid-search-with-filters-targeting-vector-subqueries-preview) | Feature | A filter on a hybrid query involves all subqueries on the request, regardless of type. You can override the global filter to scope the filter to a specific subquery. A new `filterOverride` parameter provides the behaviors. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
+| [**Text Split skill (token chunking)**](cognitive-search-skill-textsplit.md) | Applied AI (skills) | This skill has new parameters that improve data chunking for embedding models. A new `unit` parameter lets you specify token chunking. You can now chunk by token length, setting the length to a value that makes sense for your embedding model. You can also specify the tokenizer and any tokens that shouldn't be split during data chunking. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
 | [**Azure AI Vision multimodal embedding skill**](cognitive-search-skill-vision-vectorize.md) | Applied AI (skills) | A new skill type that calls Azure AI Vision multimodal API to generate embeddings for text or images during indexing. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
 | [**Azure Machine Learning (AML) skill**](cognitive-search-aml-skill.md) | Applied AI (skills) | AML skill integrates an inferencing endpoint from Azure Machine Learning. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true). In previous preview APIs, it supports connections to deployed custom models in an AML workspace. Starting in the 2024-05-01-preview, you can use this skill in workflows that connect to embedding models in the Azure AI Studio model catalog. It's also available in the portal, in skillset design, assuming Azure AI Search and Azure Machine Learning services are deployed in the same subscription. |
 | [**Incremental enrichment cache**](cognitive-search-incremental-indexing-conceptual.md) | Applied AI (skills) | Adds caching to an enrichment pipeline, allowing you to reuse existing output if a targeted modification, such as an update to a skillset or another object, doesn't change the content. Caching applies only to enriched documents produced by a skillset.| [Create or Update Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
@@ -38,7 +42,7 @@ Preview features are removed from this list if they're retired or transition to
 | [**Reset Documents**](search-howto-run-reset-indexers.md) | Indexer | Reprocesses individually selected search documents in indexer workloads. | [Reset Documents (preview)](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
 | [**speller**](speller-how-to-add.md) | Query | Optional spelling correction on query term inputs for simple, full, and semantic queries. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
 | [**Normalizers**](search-normalizers.md) | Query |  Normalizers provide simple text preprocessing: consistent casing, accent removal, and ASCII folding, without invoking the full text analysis chain.| [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
-| [**featuresMode parameter**](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true) | Relevance (scoring) | Relevance score expansion to include details: per field similarity score, per field term frequency, and per field number of unique tokens matched. You can consume these data points in [custom scoring solutions](https://github.com/Azure-Samples/search-ranking-tutorial). | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true).|
+| [**featuresMode parameter**](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true) | Relevance (scoring) | BM25 relevance score expansion to include details: per field similarity score, per field term frequency, and per field number of unique tokens matched. You can consume these data points in [custom scoring solutions](https://github.com/Azure-Samples/search-ranking-tutorial). | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true).|
 | [**vectorQueries.threshold parameter**](vector-search-how-to-query.md#vector-weighting) | Relevance (scoring)  | Exclude low-scoring search result based on a minimum score. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
 | [**hybridSearch.maxTextRecallSize and countAndFacetMode parameters**](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview) | Relevance (scoring)  |  adjust the inputs to a hybrid query by controlling the amount BM25-ranked results that flow to the hybrid ranking model.  | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
 | [**moreLikeThis**](search-more-like-this.md) | Query | Finds documents that are relevant to a specific document. This feature has been in earlier previews. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchプレビュー機能の更新"
}
```

### Explanation
この変更では、Azure AI Searchのプレビュー機能に関するドキュメントが更新されました。主な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの更新日が2024年8月5日から2024年10月1日に変更されました。

2. **新機能の追加**: いくつかの新機能が追加され、それぞれの詳細が表形式で記載されています。具体的には、以下の新機能が紹介されています。
   - MRLを使用したテキスト埋め込みモデルの次元要件を低減する機能。
   - ハイブリッド検索結果でサブスコアを表示するために、`@search.score`を展開する機能。
   - ベクトルサブクエリのみにフィルターをターゲットにするハイブリッド検索機能。
   - トークンサイズによるデータチャンク処理を改善するテキスト分割スキル、など。

3. **プレビュー機能の更新**: 各機能には、説明とともに、利用可能性についてのリンクが提供されています。また、いくつかの機能が改善され、文書のリンクも更新されています。

4. **旧機能の説明改善**: `featuresMode`パラメータの説明がBM25関連の詳細を含むように更新され、さらなる利用のヒントが提供されています。

この更新は、開発者やユーザーが最新のプレビュー機能を理解し、実装する際の参考になることを意図しています。新しい機能により、Azure AI Searchの利便性が向上し、ユーザーにとっての情報検索体験の質も改善されることが期待されます。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -335,24 +335,26 @@ items:
     items:
     - name: Create a vector index
       href: vector-search-how-to-create-index.md
-    - name: Index binary data for vector search
-      href: vector-search-how-to-index-binary-data.md
-    - name: Query vectors
-      href: vector-search-how-to-query.md
-    - name: Add filters to a vector query
-      href: vector-search-filters.md
-    - name: Vector quotas and limits
-      href: vector-search-index-size.md
-    - name: Reduce vector size
-      href: vector-search-how-to-configure-compression-storage.md
-    - name: Configure a vectorizer for queries
-      href: vector-search-how-to-configure-vectorizer.md
     - name: Chunk documents
       href: vector-search-how-to-chunk-documents.md
     - name: Generate embeddings
       href: vector-search-how-to-generate-embeddings.md
-    - name: Integrated vectorization with Azure AI Studio models
+    - name: Use embedding models from Azure AI Studio
       href: vector-search-integrated-vectorization-ai-studio.md
+    - name: Reduce vector size
+      items:
+      - name: Understand vector quotas and limits
+        href: vector-search-index-size.md
+      - name: Compress vector index size
+        href: vector-search-how-to-configure-compression-storage.md
+      - name: Index binary data for vector search
+        href: vector-search-how-to-index-binary-data.md
+    - name: Query vectors
+      href: vector-search-how-to-query.md
+    - name: Add a vectorizer for text-to-vector queries
+      href: vector-search-how-to-configure-vectorizer.md
+    - name: Filter on vector queries
+      href: vector-search-filters.md
   - name: Keyword search
     items:
     - name: Full text query
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索APIの目次更新"
}
```

### Explanation
この変更は、検索APIに関連する文書の目次（toc.yml）の更新を示しています。主要な変更点は以下の通りです。

1. **項目の追加と整理**: 新しい項目が追加され、既存の項目が整理されました。特に、「Reduce vector size」という新しいセクションが作成され、その中にいくつかの関連するサブ項目が追加されています。

2. **セクションの再構成**: 従来の「Index binary data for vector search」や「Vector quotas and limits」などの項目が、「Reduce vector size」以下のサブ項目としてグループ化され、より明確に関連性が示されるようになりました。

3. **新しい名称の採用**: 「Integrated vectorization with Azure AI Studio models」という項目が「Use embedding models from Azure AI Studio」と名称変更されました。この変更により、目的がより明確になっています。

4. **全体の整合性向上**: 文書のナビゲーションが改善された結果、開発者やユーザーが必要な情報を迅速に見つけやすくなりました。

この更新は、特にAzure AI Searchを活用する開発者のために、情報の構造をわかりやすくすることを目的としています。新しい目次によって、各機能や手順へのアクセスが容易になり、ユーザーの利用体験が向上することが期待されます。

## articles/search/vector-search-how-to-chunk-documents.md{#item-b79133}

<details>
<summary>Diff</summary>
````diff
@@ -9,19 +9,19 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 08/05/2024
+ms.date: 10/01/2024
 ---
 
 # Chunk large documents for vector search solutions in Azure AI Search
 
-Partitioning large documents into smaller chunks can help you stay under the maximum token input limits of embedding models. For example, the maximum length of input text for the [Azure OpenAI](/azure/ai-services/openai/how-to/embeddings) embedding models is 8,191 tokens. Given that each token is around four characters of text for common OpenAI models, this maximum limit is equivalent to around 6,000 words of text. If you're using these models to generate embeddings, it's critical that the input text stays under the limit. Partitioning your content into chunks ensures that your data can be processed by the embedding models used to populate vector stores and text-to-vector query conversions. 
+Partitioning large documents into smaller chunks can help you stay under the maximum token input limits of embedding models. For example, the maximum length of input text for the [Azure OpenAI](/azure/ai-services/openai/how-to/embeddings) text-embedding-ada-002 model is 8,191 tokens. Given that each token is around four characters of text for common OpenAI models, this maximum limit is equivalent to around 6,000 words of text. If you're using these models to generate embeddings, it's critical that the input text stays under the limit. Partitioning your content into chunks ensures that your data can be processed by the embedding models and that you don't lose information due to truncation.
 
-Chunking is only required if source documents are too large for the maximum input size imposed by models.
-
-We recommend [integrated vectorization](vector-search-integrated-vectorization.md) for built-in data chunking and embedding. Integrated vectorization takes a dependency on indexers, skillsets, the Text Split skill, and an embedding skill. If you can't use integrated vectorization, this article describes some approaches for chunking your content.
+We recommend [integrated vectorization](vector-search-integrated-vectorization.md) for built-in data chunking and embedding. Integrated vectorization takes a dependency on indexers, skillsets, the [Text Split skill](cognitive-search-skill-textsplit.md), and an embedding skill like [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md). If you can't use integrated vectorization, this article describes some approaches for chunking your content.
 
 ## Common chunking techniques
 
+Chunking is only required if the source documents are too large for the maximum input size imposed by models.
+
 Here are some common chunking techniques, starting with the most widely used method:
 
 + Fixed-size chunks: Define a fixed size that's sufficient for semantically meaningful paragraphs (for example, 200 words) and allows for some overlap (for example, 10-15% of the content) can produce good chunks as input for embedding vector generators.
@@ -48,7 +48,7 @@ When it comes to chunking data, think about these factors:
 
 If you have large documents, you must insert a chunking step into indexing and query workflows that breaks up large text. When using [integrated vectorization](vector-search-integrated-vectorization.md), a default chunking strategy using the [Text Split skill](./cognitive-search-skill-textsplit.md) is applied. You can also apply a custom chunking strategy using a [custom skill](cognitive-search-custom-skill-web-api.md). Some libraries that provide chunking include:
 
-+ [LangChain Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/)
++ [LangChain Text Splitters](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/)
 + [Semantic Kernel TextChunker](/dotnet/api/microsoft.semantickernel.text.textchunker)
 
 Most libraries provide common chunking techniques for fixed size, variable size, or a combination. You can also specify an overlap that duplicates a small amount of content in each chunk for context preservation.
@@ -75,12 +75,14 @@ Set `textSplitMode` to break up content into smaller chunks:
 
 The `pages` parameter adds extra parameters:
 
-+ `maximumPageLength` defines the maximum number of characters <sup>1</sup> in each chunk. The text splitter avoids breaking up sentences, so the actual character count depends on the content.
++ `maximumPageLength` defines the maximum number of characters <sup>1</sup> or tokens <sup>2</sup> in each chunk. The text splitter avoids breaking up sentences, so the actual character count depends on the content.
 + `pageOverlapLength` defines how many characters from the end of the previous page are included at the start of the next page. If set, this must be less than half the maximum page length.
 + `maximumPagesToTake` defines how many pages / chunks to take from a document. The default value is 0, which means taking all pages or chunks from the document.
 
 <sup>1</sup> Characters don't align to the definition of a [token](/azure/ai-services/openai/concepts/prompt-engineering#space-efficiency). The number of tokens measured by the LLM might be different than the character size measured by the Text Split skill.
 
+<sup>2</sup> Token chunking is available in the [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) and includes extra parameters for specifying a tokenizer and any tokens that shouldn't be split up during chunking.
+
 The following table shows how the choice of parameters affects the total chunk count from the Earth at Night e-book:
 
 | `textSplitMode` | `maximumPageLength` | `pageOverlapLength` | Total Chunk Count |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "大規模文書のチャンク化方法の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける大規模文書のチャンク化方法に関するドキュメントの更新を示します。主な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの更新日が2024年8月5日から2024年10月1日に変更されました。

2. **内容の明確化**: チャンク化の重要性と、Azure OpenAIのモデルによるトークン入力制限についての説明が明確になりました。特に、情報の欠落を防ぐために、入力テキストが制限内に収まるようにチャンク化が行われるべきであることが強調されています。

3. **統合ベクトル化の推奨**: 統合ベクトル化に関する推奨が強調され、その依存関係として、インデクサーやスキルセット、[テキスト分割スキル](cognitive-search-skill-textsplit.md)、および[Azure OpenAI埋め込みスキル](cognitive-search-skill-azure-openai-embedding.md)が挙げられています。

4. **チャンク化技術の追加**: チャンク化技術のセクションが充実し、固定サイズチャンクが推奨される内容が加えられました。これは意味のある段落を保持するための方法です。

5. **新しいパラメータの導入**: `maximumPageLength`が文字数ではなくトークン数に基づくことが明記され、トークン化に関連する新しい情報が提供されています。また、チャンク化中に分割されるべきでないトークンを指定できる機能も追加されています。

この更新は、Azure AI Searchを利用する開発者が文書を効果的にチャンク化し、それを埋め込みモデルに適切に提供できるようにするための情報を提供することを目的としています。これにより、データの処理がさらに効率的になり、情報抽出の精度向上が期待されます。

## articles/search/vector-search-how-to-configure-compression-storage.md{#item-c653c3}

<details>
<summary>Diff</summary>
````diff
@@ -7,14 +7,16 @@ author: heidisteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: how-to
-ms.date: 08/14/2024
+ms.date: 10/01/2024
 ---
 
 # Reduce vector size through quantization, narrow data types, and storage options
 
-This article explains how to use vector quantization and other techniques for reducing vector size in Azure AI Search. The search index specifies vector field definitions, including properties for stored and narrow data types. Quantization is also specified in the index and assigned to vector field through its vector profile. 
+This article explains how to use vector quantization and other techniques for reducing vector size in Azure AI Search. The search index specifies vector field definitions, including properties used to specify narrow data types or control whether a copy of vector content is retained for search results. Quantization is also specified in the index and assigned to vector field through its vector profile. 
 
-These features are generally available in [2024-07-01 REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-07-01&preserve-view=true) and in the Azure SDK packages targeting that version. [An example](#example-vector-compression-techniques) at the end of this article shows the variations in vector size for each of the approaches described in this article.
+Most of the features described in this article are generally available in [2024-07-01 REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-07-01&preserve-view=true) and in the Azure SDK packages targeting that version. The [latest preview version](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-09-01-preview&preserve-view=true) adds support for truncated dimensions if you're using text-embedding-3-large or text-embedding-3-small for vectorization.
+
+[An example](#example-vector-compression-techniques) at the end of this article shows the variations in vector size for each of the approaches described in this article.
 
 ## Evaluate the options
 
@@ -25,6 +27,7 @@ We recommend built-in quantization because it compresses vector size in memory *
 | Approach | Why use this option |
 |----------|---------------------|
 | [Add scalar or binary quantization](#option-1-configure-quantization) | Use quantization to compress native float32 or float16  embeddings to  int8  (scalar) or Byte (binary). This option reduces storage in memory and on disk with no degradation of query performance. Smaller data types like int8 or Byte produce vector indexes that are less content-rich than those with larger embeddings. To offset information loss, built-in compression includes options for post-query processing using uncompressed embeddings and oversampling to return more relevant results. Reranking and oversampling are specific features of built-in quantization of float32 or float16 fields and can't be used on embeddings that undergo custom quantization. |
+| [Truncate dimensions for MRL-capable text-embedding-3 models (preview)](#use-mrl-compression-and-truncated-dimensions-preview) | Exercise the option to use fewer dimensions on text-embedding-3 models. On Azure OpenAI, these models have been retrained on the [Matryoshka Representation Learning (MRL)](https://arxiv.org/abs/2205.13147) technique that produces multiple vector representations at different levels of compression. This approach produces faster searches and reduced storage costs, with minimal loss of semantic information. In Azure AI Search, MRL support supplements scalar and binary quantization. When you use either quantization method, you can also specify a `truncateDimension` property on your vector fields to reduce the dimensionality of text embeddings. |
 | [Assign smaller primitive data types to vector fields](#option-2-assign-narrow-data-types-to-vector-fields) | Narrow data types, such as float16, int16,  int8, and Byte (binary) consume less space in memory and on disk, but you must have an embedding model that outputs vectors in a narrow data format. Or, you must have custom quantization logic that outputs small data. A third use case that requires less effort is recasting native float32 embeddings produced by most models to float16. See [Index binary vectors](vector-search-how-to-index-binary-data.md) for details about binary vectors. |
 | [Eliminate optional storage of retrievable vectors](#option-3-set-the-stored-property-to-remove-retrievable-storage) | Vectors returned in a query response are stored separately from vectors used during query execution. If you don't need to return vectors, you can turn off retrievable storage, reducing overall per-field disk storage by up to 50 percent. |
 
@@ -70,7 +73,7 @@ POST https://[servicename].search.windows.net/indexes?api-version=2024-07-01
   "fields": [
     { "name": "Id", "type": "Edm.String", "key": true, "retrievable": true, "searchable": true, "filterable": true },
     { "name": "content", "type": "Edm.String", "retrievable": true, "searchable": true },
-    { "name": "vectorContent", "type": "Collection(Edm.Single)", "retrievable": false, "searchable": true },
+    { "name": "vectorContent", "type": "Collection(Edm.Single)", "retrievable": false, "searchable": true, "dimensions": 1536,"vectorSearchProfile": "vector-profile-1"},
   ],
   "vectorSearch": {
         "profiles": [ ],
@@ -185,6 +188,114 @@ Binary quantization compresses high-dimensional vectors by representing each com
 
 It's particularly effective for embeddings with dimensions greater than 1024. For smaller dimensions, we recommend testing the quality of binary quantization, or trying scalar instead. Additionally, we’ve found BQ performs very well when embeddings are centered around zero. Most popular embedding models such as OpenAI, Cohere, and Mistral are centered around zero. 
 
+### Use MRL compression and truncated dimensions (preview)
+
+MRL multilevel compression saves on vector storage and improves query response times for vector queries based on text embeddings. In Azure AI Search, MRL support is only offered together with another method of quantization. Using binary quantization with MRL provides the maximum vector index size reduction. To achieve maximum storage reduction, use binary quantization with MRL, and `stored` set to false. 
+
+This feature is in preview. It's available in `2024-09-01-preview` and in beta SDK packages targeting that preview API version.
+
+#### Requirements
+
+- Text-embedding-3-small, Text-embedding-3-large (text content only).
+- New vector fields of type `Edm.Half` or `Edm.Single` (you can't add MRL compression to an existing field).
+- [HNSW algorithm](vector-search-ranking.md) (no support for exhaustive KNN in this preview).
+- [Configure scalar or binary quantization](#option-1-configure-quantization). We recommend binary quantization.
+
+#### Supported clients
+
+- [REST API 2024-09-01-preview](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) 
+- Check the change logs for each Azure SDK beta package: [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md), [Java](https://github.com/Azure/azure-sdk-for-java/blob/azure-search-documents_11.1.3/sdk/search/azure-search-documents/CHANGELOG.md), [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md). 
+
+There's no Azure portal or Azure AI Studio support at this time. 
+
+#### How to use MRL-extended text embeddings
+
+MRL is a capability of the textembedding model. To benefit from those capabilities in Azure AI Search, follow these steps.
+
+1. Specify a `vectorSearch.compressions` object in your index definition.
+1. Include a quantization method, either scalar or binary (recommended).
+1. Include the `truncationDimension` parameter set to 512, or as low as 256 if you use the text-embedding-3-large model.
+1. Specify a vector profile that specifies the HNSW algorithm and the vector compression object.
+1. Assign the vector profile to a vector field of type `Edm.Half` or `Edm.Single` in the fields collection.
+
+There are no query-side modifications for using an MRL-capable text embedding model. Integrated vectorization, text-to-query conversions at query time, semantic ranking and other relevance enhancement features such as reranking with original vectors and oversampling are unaffected by MRL support.
+
+Indexing is slower due to the extra steps, but queries will be faster.
+
+#### Example of a vector search configuration that supports MRL
+
+The following example illustrates a vector search configuration that meets the requirements and recommendations of MRL. 
+
+`truncationDimension` is a compression property. It specifies how much to shrink the vector graph in memory in conjunction with a compression method like scalar or binary compression. We recommend 1,024 or higher for `truncationDimension` with binary quantization. A dimensionality of less than 1,000 degrades the quality of search results when using MRL and binary compression.
+
+
+```json
+{ 
+  "vectorSearch": { 
+    "profiles": [ 
+      { 
+        "name": "use-bq-with-mrl", 
+        "compression": "use-mrl,use-bq", 
+        "algorithm": "use-hnsw" 
+      } 
+    ],
+    "algorithms": [
+       {
+          "name": "use-hnsw",
+          "kind": "hnsw",
+          "hnswParameters": {
+             "m": 4,
+             "efConstruction": 400,
+             "efSearch": 500,
+             "metric": "cosine"
+          }
+       }
+    ],
+    "compressions": [ 
+      { 
+        "name": "use-mrl", 
+        "kind": "truncation", 
+        "rerankWithOriginalVectors": true, 
+        "defaultOversampling": 10, 
+        "truncationDimension": 1024
+      }, 
+      { 
+        "name": "use-bq", 
+        "kind": "binaryQuantization", 
+        "rerankWithOriginalVectors": true,
+        "defaultOversampling": 10
+       } 
+    ] 
+  } 
+} 
+```
+
+Here's an example of a [fully specified vector field definition](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true#searchfield) that satisfies the requirements for MRL. 
+
+Recall that vector fields must be of type `Edm.Half` or `Edm.Single`. Vector fields must have a `vectorSearchProfile` property that determines the algorithm and compression settings. Vector fields have a `dimensions` property used for specifying the number of dimensions for scoring and ranking results. Its value should be dimensions limit of the model you're using (1,536 for text-embedding-3-small).
+
+```json
+{
+    "name": "text_vector",
+    "type": "Collection(Edm.Single)",
+    "searchable": true,
+    "filterable": false,
+    "retrievable": false,
+    "stored": false,
+    "sortable": false,
+    "facetable": false,
+    "key": false,
+    "indexAnalyzer": null,
+    "searchAnalyzer": null,
+    "analyzer": null,
+    "normalizer": null,
+    "dimensions": 1536,
+    "vectorSearchProfile": "use-bq-with-mrl",
+    "vectorEncoding": null,
+    "synonymMaps": []
+}
+```
+
 ## Option 2: Assign narrow data types to vector fields
 
 An easy way to reduce vector size is to store embeddings in a smaller data format. Most embedding models output 32-bit floating point numbers, but if you quantize your vectors, or if your embedding model supports it natively, output might be float16, int16, or int8, which is significantly smaller than float32. You can accommodate these smaller vector sizes by assigning a narrow data type to a vector field. In the vector index, narrow data types consume less storage.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルサイズの圧縮ストレージ設定の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるベクトルのサイズを圧縮するためのストレージ設定に関するドキュメントの更新を示しています。主な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの更新日が2024年8月14日から2024年10月1日に変更されました。

2. **内容の拡充**: ベクトル圧縮やデータ型の選定（狭いデータ型を使用すること）に関する説明が詳細化され、新たにトランケーションルールが強調されました。具体的には、テキスト-エンコーディングモデルに対してトランケーションを適用できる仕組みについての言及があります。

3. **新しい機能の追加**: マトリョーシカ表現学習（MRL）を利用した圧縮やトークンの次元削減に関する新機能が説明され、これによってストレージコストの削減とクエリ応答速度の改善が可能になることが示されています。

4. **事例の追加**: 本文の終わりに、異なる圧縮手法の例を示すコンテンツが追加され、ユーザーがベクトルサイズを減らす成功事例を確認できるようになっています。

5. **APIバージョン情報の更新**: 新しいプレビュー版（2024-09-01）における機能追加についての詳細が追加され、ユーザーが最新の機能を利用する際のガイダンスが提供されています。

これらの更新により、ユーザーはAzure AI Searchにおけるベクトル圧縮の設定をより効果的に行い、ストレージの使用効率を向上させることが期待されます。また、MRL機能が提供されることで、検索の速度と精度を向上させることが可能となります。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: overview
-ms.date: 08/20/2024
+ms.date: 10/01/2024
 ms.custom:
   - references_regions
 ---
@@ -19,21 +19,31 @@ ms.custom:
 > [!NOTE]
 > Preview features are announced here, but we also maintain a [preview features list](search-api-preview.md) so you can find them in one place.
 
+## October 2024
+
+| Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
+|-----------------------------|------|--------------|
+| [**Lower the dimension requirements for MRL-trained text embedding models on Azure OpenAI**](vector-search-how-to-configure-compression-storage.md#use-mrl-compression-and-truncated-dimensions-preview) | Feature | Text-embedding-3-small and Text-embedding-3-large are trained using Matryoshka Representation Learning (MRL). This allows you to truncate the embedding vectors to fewer dimensions, and adjust the balance between vector index size usage and retrieval quality. A new `truncationDimension` in the [2024-09-01-preview](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) enables access to MRL compression in text embedding models. This can only be configured for new vector fields. |
+| [**Unpack `@search.score` to view subscores in hybrid search results**](hybrid-search-ranking.md#unpack-a-search-score-into-subscores-preview) | Feature | You can investigate Reciprocal Rank Fusion (RRF) ranked results by viewing the individual query subscores of the final merged and scored result. A new `debug` property unpacks the search score. `QueryResultDocumentSubscores`, `QueryResultDocumentRerankerInput`, and `QueryResultDocumentSemanticField` provide the extra detail. These definitions are available in the [2024-09-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
+| [**Target filters in a hybrid search to just the vector queries**](hybrid-search-how-to-query.md#hybrid-search-with-filters-targeting-vector-subqueries-preview) | Feature | A filter on a hybrid query involves all subqueries on the request, regardless of type. You can override the global filter to scope the filter to a specific subquery. The new `filterOverride` parameter is available on hybrid queries using the [2024-09-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
+| [**Text Split skill (token chunking)**](cognitive-search-skill-textsplit.md) | Applied AI (skills) | This skill has new parameters that improve data chunking for embedding models. A new `unit` parameter lets you specify token chunking. You can now chunk by token length, setting the length to a value that makes sense for your embedding model. You can also specify the tokenizer and any tokens that shouldn't be split during data chunking. The new `unit` parameter and query subscore definitions are found in the [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
+| [**2024-09-01-preview**](/rest/api/searchservice/search-service-api-versions?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | API | Preview release of REST APIs for truncated dimensions in text-embedding-3 models, targeted vector filtering for hybrid queries, RRF subscore details for debugging, and token chunking for Text Split skill.|
+
 ## August 2024
 
 | Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
 |-----------------------------|------|--------------|
-| [**Debug session improvements**](cognitive-search-debug-session.md) | feature | There are two important improvements. First, you can now debug integrated vectorization and data chunking workloads. Second, debug sessions is redesigned for a more streamlined presentation of skills and mappings. You can select an object in the flow, and view or edit its details off to the side. The previous tabbed layout is fully replaced with more context-sensitive information on the page. |
-| [**2024-07-01**](/rest/api/searchservice/search-service-api-versions?view=rest-searchservice-2024-07-01&preserve-view=true) | API | Stable release of REST APIs for generally available vector data types, vector compression, and integrated vectorization during indexing and queries. |
-| [**Integrated vectorization**](vector-search-integrated-vectorization.md) | Feature | Announcing general availability. Skills-driven data chunking and embedding during indexing. |
-| [**Vectorizers**](vector-search-how-to-configure-vectorizer.md) | Feature  | Announcing general availability. Text-to-vector conversion during query execution. Both [Azure OpenAI vectorizer](vector-search-vectorizer-azure-open-ai.md) and [custom Web API vectorizer](vector-search-vectorizer-custom-web-api.md) are generally available. |
-| [**AzureOpenAIEmbedding skill**](cognitive-search-skill-azure-openai-embedding.md) | Feature | Announcing general availability. A skill type that calls an Azure OpenAI embedding model to generate embeddings during indexing.  |
-| [**Index projections**](index-projections-concept-intro.md) | Feature | Announcing general availability. A component of a skillset definition that defines the shape of a secondary index, supporting a one-to-many index pattern, where content from an enrichment pipeline can target multiple indexes. |
-| [**Binary and Scalar quantization**](vector-search-how-to-configure-compression-storage.md#option-1-configure-quantization)  | Feature | Announcing general availability. Compress vector index size in memory and on disk using built-in quantization. |
-| [**Narrow data types**](vector-search-how-to-configure-compression-storage.md#option-2-assign-narrow-data-types-to-vector-fields) | Feature  | Announcing general availability. Assign a smaller data type on vector fields, assuming incoming data is of that data type. |
-| [**Import and vectorize data wizard**](search-get-started-portal-import-vectors.md) | Azure portal | Announcing general availability. A wizard that creates a full indexing pipeline that includes data chunking and vectorization. The wizard creates all necessary objects and configurations. This release adds wizard support for Azure Data Lake in Azure Storage.|
-| [**stored property**](vector-search-how-to-configure-compression-storage.md#option-3-set-the-stored-property-to-remove-retrievable-storage) | Feature  | Announcing general availability. Boolean that reduces storage of vector indexes by *not* storing retrievable vectors. |
-| [**vectorQueries.Weight property**](vector-search-how-to-query.md#vector-weighting) | Feature  | Announcing general availability. Specify the relative weight of each vector query in a search operation. |
+| [Debug Session improvements](cognitive-search-debug-session.md) | feature | There are two important improvements. First, you can now debug integrated vectorization and data chunking workloads. Second, Debug Sessions is redesigned for a more streamlined presentation of skills and mappings. You can select an object in the flow, and view or edit its details in a side panel. The previous tabbed layout is fully replaced with more context-sensitive information on the page. |
+| [2024-07-01](/rest/api/searchservice/search-service-api-versions?view=rest-searchservice-2024-07-01&preserve-view=true) | API | Stable release of REST APIs for generally available vector data types, vector compression, and integrated vectorization during indexing and queries. |
+| [Integrated vectorization](vector-search-integrated-vectorization.md) | Feature | Announcing general availability. Skills-driven data chunking and embedding during indexing. |
+| [Vectorizers](vector-search-how-to-configure-vectorizer.md) | Feature  | Announcing general availability. Text-to-vector conversion during query execution. Both [Azure OpenAI vectorizer](vector-search-vectorizer-azure-open-ai.md) and [custom Web API vectorizer](vector-search-vectorizer-custom-web-api.md) are generally available. |
+| [AzureOpenAIEmbedding skill](cognitive-search-skill-azure-openai-embedding.md) | Feature | Announcing general availability. A skill type that calls an Azure OpenAI embedding model to generate embeddings during indexing.  |
+| [Index projections](index-projections-concept-intro.md) | Feature | Announcing general availability. A component of a skillset definition that defines the shape of a secondary index, supporting a one-to-many index pattern, where content from an enrichment pipeline can target multiple indexes. |
+| [Binary and Scalar quantization](vector-search-how-to-configure-compression-storage.md#option-1-configure-quantization)  | Feature | Announcing general availability. Compress vector index size in memory and on disk using built-in quantization. |
+| [Narrow data types](vector-search-how-to-configure-compression-storage.md#option-2-assign-narrow-data-types-to-vector-fields) | Feature  | Announcing general availability. Assign a smaller data type on vector fields, assuming incoming data is of that data type. |
+| [Import and vectorize data wizard](search-get-started-portal-import-vectors.md) | Azure portal | Announcing general availability. A wizard that creates a full indexing pipeline that includes data chunking and vectorization. The wizard creates all necessary objects and configurations. This release adds wizard support for Azure Data Lake in Azure Storage.|
+| [stored property](vector-search-how-to-configure-compression-storage.md#option-3-set-the-stored-property-to-remove-retrievable-storage) | Feature  | Announcing general availability. Boolean that reduces storage of vector indexes by *not* storing retrievable vectors. |
+| [vectorQueries.Weight property](vector-search-how-to-query.md#vector-weighting) | Feature  | Announcing general availability. Specify the relative weight of each vector query in a search operation. |
 
 ## July 2024
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能と更新情報の追加"
}
```

### Explanation
この変更は、Azure AI Searchの「What's New」ページに対する更新を示しています。主な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの更新日が2024年8月20日から2024年10月1日に変更されています。

2. **新機能の追加**: 2024年10月の新機能が追加され、具体的には以下の内容が含まれています。
   - **MRLトレーニングモデルの次元要件の低減**: 新たに導入されたトランケーション次元により、テキスト埋め込みモデルのベクトルサイズを調整できるようになりました。
   - **ハイブリッド検索のスコア分解**: 新しいプロパティにより、複合検索結果内の個別クエリサブスコアを視覚化できるようになりました。
   - **ベクトルクエリのターゲットフィルタ**: 特定のサブクエリにフィルタを適用できる新しい `filterOverride` パラメータが導入されました。
   - **テキスト分割スキルの新パラメータ**: データのチャンク化プロセスを改善するために新しい `unit` パラメータが追加され、トークンの長さに基づくチャンク化が可能になりました。

3. **バージョン情報の更新**: 2024年9月1日のプレビュー版に関するAPIが紹介され、ベクトルフィルタリングやトークンのチャンク化などの機能に関する情報が提供されています。

4. **以前の機能の整理**: 2024年8月分の新機能に関する情報が整理され、既存の機能やAPIの一般提供についても説明されています。

これらの変更により、Azure AI Searchの最新機能や更新情報をユーザーがより容易に把握できるようになります。また、ドキュメントは新しい機能の利用法を理解するための貴重なリソースとなります。


