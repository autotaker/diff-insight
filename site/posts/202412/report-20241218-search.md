---
date: '2024-12-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b8144fb...MicrosoftDocs:aba0ab5
summary: このコードの差分は、Azure Cognitive Searchに関するドキュメントにおける微修正です。特定の新機能や重大な変更はなく、用語や表現がより明確に、理解しやすく修正されています。テキストの説明が簡潔化され、手順の表現が明確化され、人間が読み取れる内容に焦点を当てた一貫性が維持されています。これにより、開発者やエンドユーザーがAzure
  Searchをより深く理解し適切に活用できるようになることを目指しています。特に「alphanumeric content」から「human-readable
  content」への表現変更は、Azure Searchが扱うコンテンツの理解を促進します。全体として、Azure Cognitive Searchのドキュメントがより親しみやすく、技術仕様の理解を深めるためのサポートが強化されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b8144fb...MicrosoftDocs:aba0ab5){target="_blank"}

# ハイライト
このコードの差分は、Azure Cognitive Searchに関する複数のドキュメントにおける微修正です。各ドキュメントにおいて、用語や表現がより明確に、そして理解しやすい形に修正されています。主に、新機能の追加や大きな変更点はありませんが、表現の最適化を通じて読者の理解を助けることが目的です。

## 新機能
特定の新機能の追加はありません。

## 重大な変更
重大な変更はありませんが、すべてのドキュメントで用語や表現の修正が行われています。

## その他の更新
- テキスト抽出やプロジェクト名、スコアリングプロファイルなどに関する説明が簡潔化。
- データインポート、検索インデックス作成、ベクトル検索の各種手順における表現の明確化。
- 言語サポート機能の説明を通じて、人間が読み取れる内容に焦点を当てた表現の一貫性を維持。

# インサイト
今回の変更は、Azure Cognitive Searchのさまざまな機能についてのドキュメントが、より読みやすく、正確な用語で記述されることを目指して行われています。これにより、Azure Searchを利用する開発者やエンドユーザーが、機能の持つ意味を深く理解し、適切に活用することができるようになります。

特に印象的な修正は「alphanumeric content」から「human-readable content」への表現の変更で、これはAzure Searchが扱うコンテンツの対象をより広く解釈し、単にコンピュータが処理するデータの集合体ではなく、ユーザーにも理解しやすい形式として再考されたことを示しています。これにより、各機能の適用条件の整理がなされ、ユーザーとしても新たな視点でサービスを利用することを促進します。

また、インデクサーやフィルターの表現も詳細化され、ユーザーはデータの管理や活用方法について具体的なイメージを持ちやすくなりました。このように、Azure Cognitive Searchの多面的なサポートが、より親しみやすい形で提供されていると同時に、技術仕様の理解を一層促進しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-concept-image-scenarios.md](#item-606953) | minor update | 画像処理に関する文の修正 | modified | 1 | 1 | 2 | 
| [cognitive-search-create-custom-skill-example.md](#item-24ed00) | minor update | プロジェクト名に関する説明の修正 | modified | 1 | 1 | 2 | 
| [index-add-custom-analyzers.md](#item-11325e) | minor update | カスタムアナライザーの名称に関する説明の修正 | modified | 1 | 1 | 2 | 
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | スコアリングプロファイルに関する記述の修正 | modified | 1 | 1 | 2 | 
| [query-simple-syntax.md](#item-ab3c96) | minor update | プレフィックスクエリに関する説明の修正 | modified | 1 | 1 | 2 | 
| [search-filters.md](#item-3f2a7a) | minor update | フィルターの定義に関する説明の修正 | modified | 1 | 1 | 2 | 
| [search-how-to-create-indexers.md](#item-de71fb) | minor update | インデクサー作成に関する記事の内容更新 | modified | 10 | 10 | 20 | 
| [search-how-to-create-search-index.md](#item-c4ff31) | minor update | 検索インデックス作成ガイドのフィルター説明の修正 | modified | 1 | 1 | 2 | 
| [search-how-to-load-search-index.md](#item-a72573) | minor update | 検索インデックスの読み込み方法に関する記事の内容更新 | modified | 3 | 3 | 6 | 
| [search-howto-incremental-index.md](#item-d98619) | minor update | インクリメンタルインデックスのキャッシュIDに関する記述の修正 | modified | 1 | 1 | 2 | 
| [search-import-data-portal.md](#item-b804d1) | minor update | データインポートウィザードにおける説明の修正 | modified | 1 | 1 | 2 | 
| [search-language-support.md](#item-a7979b) | minor update | 言語固有インデックスに関する表現の修正 | modified | 1 | 1 | 2 | 
| [search-query-overview.md](#item-dcd5d6) | minor update | クエリオーバービューにおける表現の修正 | modified | 2 | 2 | 4 | 
| [vector-search-how-to-create-index.md](#item-97c769) | minor update | ベクトル検索インデックス作成手順の表現修正 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/search/cognitive-search-concept-image-scenarios.md{#item-606953}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ Through [AI enrichment](cognitive-search-concept-intro.md), Azure AI Search give
 + [Image Analysis](cognitive-search-skill-image-analysis.md) that describes images through visual features
 + [Custom skills](#passing-images-to-custom-skills) to invoke any external image processing that you want to provide
 
-By using OCR, you can extract text from photos or pictures containing alphanumeric text, such as the word *STOP* in a stop sign. Through image analysis, you can generate a text representation of an image, such as *dandelion* for a photo of a dandelion, or the color *yellow*. You can also extract metadata about the image, such as its size.
+By using OCR, you can extract text and from photos or pictures, such as the word *STOP* in a stop sign. Through image analysis, you can generate a text representation of an image, such as *dandelion* for a photo of a dandelion, or the color *yellow*. You can also extract metadata about the image, such as its size.
 
 This article covers the fundamentals of working with images, and also describes several common scenarios, such as working with embedded images, custom skills, and overlaying visualizations on original images.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像処理に関する文の修正"
}
```

### Explanation
この変更は、記事「cognitive-search-concept-image-scenarios.md」における文章の微修正です。具体的には、OCR（光学文字認識）を使用して写真や画像からテキストを抽出する説明において、「extract text from photos or pictures」という表現が「extract text and from photos or pictures」に修正されました。この変更により、文の流れが滑らかになり、文法的な正確性が向上しています。この更新は全体の内容に重要な影響を与えるものではありませんが、より明確で理解しやすい表現を提供します。

## articles/search/cognitive-search-create-custom-skill-example.md{#item-24ed00}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ Although this example uses an Azure Function to host a web API, it isn't require
 
 1. In Visual Studio, select **New** > **Project** from the File menu.
 
-1. Choose **Azure Functions** as the template and select **Next**. Type a name for your project, and select **Create**. The function app name must be valid as a C# namespace, so don't use underscores, hyphens, or any other non-alphanumeric characters.
+1. Choose **Azure Functions** as the template and select **Next**. Type a name for your project, and select **Create**. The function app name must be valid as a C# namespace, so don't use underscores, hyphens, or any other special characters.
 
 1. Select a framework that has long term support.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクト名に関する説明の修正"
}
```

### Explanation
この変更は、「cognitive-search-create-custom-skill-example.md」記事内の手順説明に関する微修正です。具体的には、プロジェクトの名前に関する注意事項の部分が修正され、元の「non-alphanumeric characters」という表現が「special characters」に変更されました。この変更により、説明がより一般的で分かりやすくなり、読者が理解しやすい表現となっています。プロジェクト名に使用できる文字に関する説明の明瞭性が向上しています。

## articles/search/index-add-custom-analyzers.md{#item-11325e}

<details>
<summary>Diff</summary>
````diff
@@ -47,7 +47,7 @@ To create a custom analyzer, specify it in the `analyzers` section of an index a
 
 An analyzer definition includes a name, type, one or more character filters, a maximum of one tokenizer, and one or more token filters for post-tokenization processing. Character filters are applied before tokenization. Token filters and character filters are applied from left to right.
 
-- Names in a custom analyzer must be unique and can't be the same as any of the built-in analyzers, tokenizers, token filters, or characters filters. It must only contain letters, digits, spaces, dashes or underscores, can only start and end with alphanumeric characters, and is limited to 128 characters. 
+- Names in a custom analyzer must be unique and can't be the same as any of the built-in analyzers, tokenizers, token filters, or characters filters. Names consist of letters, digits, spaces, dashes or underscores. Names must start and end with plain text characters. Names must be under 128 characters in length.
 
 - Type must be #Microsoft.Azure.Search.CustomAnalyzer.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムアナライザーの名称に関する説明の修正"
}
```

### Explanation
この変更は、「index-add-custom-analyzers.md」記事におけるカスタムアナライザーの名称に関する説明の微修正です。具体的には、名称に関する制約の文章が、より明確かつ簡潔に表現されました。元の文では「must only contain letters, digits, spaces, dashes or underscores, can only start and end with alphanumeric characters」と記載されていた部分が、「Names consist of letters, digits, spaces, dashes or underscores. Names must start and end with plain text characters.」に変更されました。この結果、読者が理解しやすく、重要な仕様がよりはっきりとした形で伝えられるようになっています。この変更により、カスタムアナライザーの名称の使用条件が一層明確になりました。

## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -99,7 +99,7 @@ Scoring profiles supplement the default scoring algorithm by boosting the scores
 
 For standalone text queries, scoring profiles identify the maximum 1,000 matches in a [BM25-ranked search](index-similarity-and-scoring.md), and the top 50 are returned in results.
 
-For pure vectors, the query is vector-only, but if the [*k*-matching documents](vector-search-ranking.md) include alphanumeric fields that a scoring profile can process, a scoring profile is applied. The scoring profile revises the result set by boosting documents that match criteria in the profile.
+For pure vectors, the query is vector-only, but if the [*k*-matching documents](vector-search-ranking.md) include nonvector fields with human-readable ocntent, a scoring profile can be applied. The scoring profile revises the result set by boosting documents that match criteria in the profile.
 
 For text queries in a hybrid query, scoring profiles identify the maximum 1,000 matches in a BM25-ranked search. However, once those 1,000 results are identified, they're restored to their original BM25 order so that they can be rescored alongside vectors results in the final [Reciprocal Ranking Function (RRF)](hybrid-search-ranking.md) ordering, where the scoring profile (identified as "final document boosting adjustment" in the illustration) is applied to the merged results, along with [vector weighting](vector-search-how-to-query.md#vector-weighting), and [semantic ranking](semantic-search-overview.md) as the last step.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリングプロファイルに関する記述の修正"
}
```

### Explanation
この変更は、「index-add-scoring-profiles.md」記事において、スコアリングプロファイルに関連する文の微修正が行われました。具体的には、「*k*-matching documents」に関する部分の表現が変更され、元の「alphanumeric fields that a scoring profile can process」という表現が「nonvector fields with human-readable content」という表現に変更されました。この修正によって、スコアリングプロファイルが適用される文書の条件がより具体的で、明確に理解できるようになっています。結果として、読者に対する説明が改善され、スコアリングプロファイルの機能と適用条件をより良く理解できるようになっています。

## articles/search/query-simple-syntax.md{#item-ab3c96}

<details>
<summary>Diff</summary>
````diff
@@ -70,7 +70,7 @@ You can embed Boolean operators in a query string to improve the precision of a
 
 ## Prefix queries
 
-For "starts with" queries, add a suffix operator (`*`) as the placeholder for the remainder of a term. A prefix query must begin with at least one alphanumeric character before you can add the suffix operator.
+For "starts with" queries, add a suffix operator (`*`) as the placeholder for the remainder of a term. A prefix query must begin with at least one plain text character before you can add the suffix operator.
 
 | Character | Example | Usage |
 |----------- |--------|-------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレフィックスクエリに関する説明の修正"
}
```

### Explanation
この変更は、「query-simple-syntax.md」記事におけるプレフィックスクエリに関する記述の微修正です。具体的には、元の説明では「at least one alphanumeric character」とされていた部分が、「at least one plain text character」に変更されました。この修正により、プレフィックスクエリが必要とする文字の範囲がより正確に表現されています。結果として、読者がプレフィックスクエリを利用する際に必要な条件について、より明確に理解できるようになっています。

## articles/search/search-filters.md{#item-3f2a7a}

<details>
<summary>Diff</summary>
````diff
@@ -46,7 +46,7 @@ Filtering occurs in tandem with search, qualifying which documents to include in
 
 ## How filters are defined
 
-Filters apply to alphanumeric content on fields that are attributed as `filterable`.
+Filters apply to text and numeric (nonvector) content on fields that are attributed as `filterable`.
 
 Filters are OData expressions, articulated in the [filter syntax](search-query-odata-filter.md) supported by Azure AI Search.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フィルターの定義に関する説明の修正"
}
```

### Explanation
この変更は、「search-filters.md」記事におけるフィルター適用対象の内容に関する説明の微修正です。元の記述では「alphanumeric content」とだけ表現されていましたが、これが「text and numeric (nonvector) content」に変更されました。この修正により、フィルターが適用される内容の範囲が拡大され、テキストと数値を含むことが明確になりました。これにより、読者はフィルターの適用可能な対象をより正確に理解できるようになり、フィルターの使い方がより明瞭になります。

## articles/search/search-how-to-create-indexers.md{#item-de71fb}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 10/24/2024
+ms.date: 12/17/2024
 ---
 
 # Create an indexer in Azure AI Search
@@ -22,9 +22,9 @@ You can use an indexer to automate data import and indexing in Azure AI Search.
 
 Indexers support two workflows:
 
-+ **Text-based indexing**: Extract strings and metadata from textual content for full text search scenarios.
++ **Raw content indexing (plain text or vectors)**: Extract strings and metadata from textual content for full text search scenarios. Extracts raw vector content for vector search (for example, vectors in an Azure SQL database or Azure Cosmos DB collection). In this workflow, indexing occurs only over existing content that you provide.
 
-+ **Skills-based indexing**: Use built-in or custom skills that add integrated machine learning for analysis over images and large undifferentiated content, extracting or inferring text and structure. Skills-based indexing enables search over content that isn't otherwise easily full text searchable. To learn more, see [AI enrichment in Azure AI Search](cognitive-search-concept-intro.md).
++ **Skills-based indexing**: Extends indexing through built-in or custom skills that create or generate new searchable content. For example, you can add integrated machine learning for analysis over images and unstructured text, extracting or inferring text and structure. Or, use skills to chunk and vectorize content from text and images. Skills-based indexing creates or generates new content that doesn't exist in your external data source. New content becomes part of your index when you add fields to the index schema that accepts the incoming data. To learn more, see [AI enrichment in Azure AI Search](cognitive-search-concept-intro.md).
 
 ## Prerequisites
 
@@ -38,11 +38,11 @@ Indexers support two workflows:
 
 ## Indexer patterns
 
-When you create an indexer, the definition is one of two patterns: *text-based indexing* or *skills-based indexing*. The patterns are the same, except that skills-based indexing has more definitions.
+When you create an indexer, the definition is one of two patterns: *content-based indexing* or *skills-based indexing*. The patterns are the same, except that skills-based indexing has more definitions.
 
-### Indexer example for text-based indexing
+### Indexer example for content-based indexing
 
-Text-based indexing for full text search is the primary use case for indexers. For this workflow, an indexer looks like this example.
+Content-based indexing for full text or vector search is the primary use case for indexers. For this workflow, an indexer looks like this example.
 
 ```json
 {
@@ -114,16 +114,16 @@ Indexers work with data sets. When you run an indexer, it connects to your data
 
 | Source data | Tasks |
 |-------------|-------|
-| JSON documents | Make sure the structure or shape of incoming data corresponds to the schema of your search index. Most search indexes are fairly flat, where the fields collection consists of fields at the same level. However, hierarchical or nested structures are possible through [complex fields and collections](search-howto-complex-data-types.md). |
+| JSON documents | JSON documents can contain text, numbers, and vectors. Make sure the structure or shape of incoming data corresponds to the schema of your search index. Most search indexes are fairly flat, where the fields collection consists of fields at the same level. However, hierarchical or nested structures are possible through [complex fields and collections](search-howto-complex-data-types.md). |
 | Relational | Provide data as a flattened row set, where each row becomes a full or partial search document in the index. <br><br> To flatten relational data into a row set, you should create a SQL view, or build a query that returns parent and child records in the same row. For example, the built-in hotels sample dataset is an SQL database that has 50 records (one for each hotel), linked to room records in a related table. The query that flattens the collective data into a row set embeds all of the room information in JSON documents in each hotel record. The embedded room information is a generated by a query that uses a **FOR JSON AUTO** clause. <br><br> You can learn more about this technique in [define a query that returns embedded JSON](index-sql-relational-data.md#define-a-query-that-returns-embedded-json). This is just one example; you can find other approaches that produce the same result. |
 | Files | An indexer generally creates one search document for each file, where the search document consists of fields for content and metadata. Depending on the file type, the indexer can sometimes [parse one file into multiple search documents](search-howto-index-one-to-many-blobs.md). For example, in a CSV file, each row can become a standalone search document. |
 
 Remember that you only need to pull in searchable and filterable data:
 
-+ Searchable data is text
-+ Filterable data is alphanumeric
++ Searchable data is text or vectors
++ Filterable data is text and numbers (non-vector fields)
 
-Azure AI Search can't search over binary data in any format, although it can extract and infer text descriptions of image files (see [AI enrichment](cognitive-search-concept-intro.md)) to create searchable content. Likewise, large text can be broken down and analyzed by natural language models to find structure or relevant information, generating new content that you can add to a search document.
+Azure AI Search can't do a full-text search over binary data in any format, although it can extract and infer text descriptions of image files (see [AI enrichment](cognitive-search-concept-intro.md)) to create searchable content. Likewise, large text can be broken down and analyzed by natural language models to find structure or relevant information, generating new content that you can add to a search document. It can also do vector search over embeddings, including quantized embeddings in a binary format.
 
 Given that indexers don't fix data problems, other forms of data cleansing or manipulation might be needed. For more information, you should refer to the product documentation of your [Azure database product](/azure/?product=databases).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサー作成に関する記事の内容更新"
}
```

### Explanation
この変更は、「search-how-to-create-indexers.md」記事におけるインデクサーの作成方法に関する複数の内容の更新を含んでいます。主な変更点は、インデクサーの説明において「text-based indexing」が「raw content indexing (plain text or vectors)」に、また「内容に基づくインデクシング」としての説明も追加され、インデクサーが扱うデータの種類がテキストと数値に拡張されました。さらに、スキルベースのインデクシングの説明が強化され、新しいコンテンツの生成やベクトル検索に関する情報が加わっています。

また、インデクサーの例についても用語が変更され、「テキストベースインデクシング」は「コンテンツベースインデクシング」に改名されています。データ供給元に対する説明も更新され、インデクサーが扱うデータの構造に関する記述が明確になりました。これにより、ユーザーはインデクサーの機能とその適用方法について、より正確で包括的な理解が得られるようになっています。

## articles/search/search-how-to-create-search-index.md{#item-c4ff31}

<details>
<summary>Diff</summary>
````diff
@@ -64,7 +64,7 @@ Use this checklist to assist the design decisions for your search index.
 
 1. Identify which source fields can be used as filters. Numeric content and short text fields, particularly those with repeating values, are good choices. When working with filters, remember:
 
-   + Filters can be used in vector and nonvector queries, but the filter itself is applied to alphanumeric (nonvector) fields in your index.
+   + Filters can be used in vector and nonvector queries, but the filter itself is applied to human-readable (nonvector) fields in your index.
 
    + Filterable fields can optionally be used in faceted navigation.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックス作成ガイドのフィルター説明の修正"
}
```

### Explanation
この変更は、「search-how-to-create-search-index.md」記事におけるフィルターの適用に関する説明の微修正です。具体的には、フィルターが適用されるフィールドについての表現が「alphanumeric (nonvector) fields」から「human-readable (nonvector) fields」に変更されました。この修正により、フィルターが対象とするフィールドの性質がより明確になり、特に人間が読み取れる形のデータに適用されることが強調されています。この内容の更新は、検索インデックス設計時の重要な考慮要素を理解する助けとなります。

## articles/search/search-how-to-load-search-index.md{#item-a72573}

<details>
<summary>Diff</summary>
````diff
@@ -18,11 +18,11 @@ This article explains how to import documents into a predefined search index. In
 
 ## How data import works
 
-A search service accepts JSON documents that conform to the index schema. A search service imports and indexes plain text and vectors in JSON, used in full text search, vector search, hybrid search, and knowledge mining scenarios. 
+A search service accepts JSON documents that conform to the index schema. A search service can import and index plain text content and vector content in JSON documents.
 
-+ Plain text content is obtainable from alphanumeric fields in the external data source, metadata that's useful in search scenarios, or enriched content created by a [skillset](cognitive-search-working-with-skillsets.md) (skills can extract or infer textual descriptions from images and unstructured content). 
++ Plain text content is retrieved from fields in the external data source, from metadata properties, or from enriched content that's generated by a [skillset](cognitive-search-working-with-skillsets.md) (skills can extract or infer textual descriptions from images and unstructured content).
 
-+ Vector content is vectorized using an [external embedding model](vector-search-how-to-generate-embeddings.md) or [integrated vectorization](vector-search-integrated-vectorization.md) using Azure AI Search features that integrate with applied AI.
++ Vector content is retrieved from a data source that provides it, or it's created by a skillset that implements [integrated vectorization](vector-search-integrated-vectorization.md) in an Azure AI Search indexer workload.
 
 You can prepare these documents yourself, but if content resides in a [supported data source](search-indexer-overview.md#supported-data-sources), running an [indexer](search-indexer-overview.md) or using an Import wizard can automate document retrieval, JSON serialization, and indexing.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスの読み込み方法に関する記事の内容更新"
}
```

### Explanation
この変更は、「search-how-to-load-search-index.md」記事におけるデータインポートの説明の更新を含んでいます。変更点として、平文テキストとベクトルのコンテンツに関する記述が明確化され、特にベクトルコンテンツの取得方法や生成方法がより具体的になっています。具体的には、平文コンテンツがどのように取り出されるかの説明が「obtainable from alphanumeric fields」から「retrieved from fields in the external data source」に修正され、ベクトルコンテンツについても外部データソースから取得されるか、または「skillset」によって生成されることが強調されています。

この内容の変更により、ユーザーは検索インデックスのデータインポートプロセスに関する理解を深めることができ、特にどのようなデータがどのように処理されるかに関する明確な情報が提供されています。

## articles/search/search-howto-incremental-index.md{#item-d98619}

<details>
<summary>Diff</summary>
````diff
@@ -134,7 +134,7 @@ PUT https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME
     }
 ```
 
-If you now issue another GET request on the indexer, the response from the service includes an `ID` property in the cache object. The alphanumeric string is appended to the name of the container containing all the cached results and intermediate state of each document processed by this indexer. The ID is used to uniquely name the cache in Blob storage.
+If you now issue another GET request on the indexer, the response from the service includes an `ID` property in the cache object. The string is appended to the name of the container containing all the cached results and intermediate state of each document processed by this indexer. The ID is used to uniquely name the cache in Blob storage.
 
 ```http
     "cache": {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インクリメンタルインデックスのキャッシュIDに関する記述の修正"
}
```

### Explanation
この変更は、「search-howto-incremental-index.md」記事におけるインクリメンタルインデックスに関連するキャッシュIDの説明の微修正です。具体的には、キャッシュオブジェクト内の`ID`プロパティに関する記述が「alphanumeric string」から単に「string」に変更されました。この修正は、キャッシュIDの性質についての表現を簡素化し、アルファベットと数字の組み合わせに限定しないことを示唆しています。この情報は、ユーザーがインデクサーのキャッシュ管理を理解する際に役立ちます。修正によって、キャッシュの命名方法に関する明確さが向上し、Blobストレージ内でのキャッシュのユニークな命名に関する理解が深まります。

## articles/search/search-import-data-portal.md{#item-b804d1}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ customer intent: As a developer, I want to use wizards for index creation so tha
 
 Azure AI Search has two import wizards that automate indexing and object creation so that you can begin querying immediately. If you're new to Azure AI Search, these wizards are one of the most powerful features at your disposal. With minimal effort, you can create an indexing or enrichment pipeline that exercises most of the functionality of Azure AI Search.
 
-+ **Import data wizard** supports nonvector workflows. You can extract alphanumeric text from raw documents. You can also configure applied AI and built-in skills that infer structure and generate text searchable content from image files and unstructured data.
++ **Import data wizard** supports nonvector workflows. You can extract text and numbers from raw documents. You can also configure applied AI and built-in skills that infer structure and generate text searchable content from image files and unstructured data.
 
 + **Import and vectorize data wizard** adds chunking and vectorization. You must specify an existing deployment of an embedding model, but the wizard makes the connection, formulates the request, and handles the response. It generates vector content from text or image content.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データインポートウィザードにおける説明の修正"
}
```

### Explanation
この変更は、「search-import-data-portal.md」記事におけるデータインポートウィザードに関する記述の微修正です。具体的には、「alphanumeric text」を「text and numbers」に変更し、サポートされるデータタイプに対する説明が明確になりました。これにより、ユーザーは非ベクトルワークフローにおいて、テキストだけでなく数字も抽出できることを理解しやすくなります。また、ウィザードの強力な機能を強調し、ユーザーが構造を推測し、画像ファイルや非構造化データから検索可能なテキストコンテンツを生成するスキルを設定できることも示されています。この修正により、読者はデータインポートのフローをよりよく理解できるようになり、Azure AI Searchの利点を最大限に活用できるようになります。

## articles/search/search-language-support.md{#item-a7979b}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ Azure AI Search supports Microsoft and Lucene analyzers. By default, the search
 
 In Azure AI Search, the two patterns for supporting multiple languages include:
 
-+ Create language-specific indexes where all of the alphanumeric content is in the same language, and all searchable string fields are attributed to use the same [language analyzer](index-add-language-analyzers.md).
++ Create language-specific indexes where all of the human readable content is in the same language, and all searchable string fields are attributed to use the same [language analyzer](index-add-language-analyzers.md).
 
 + Create a blended index with language-specific versions of each field (for example, description_en, description_fr, description_ko), and then constrain full text search to just those fields at query time. This approach is useful for scenarios where language variants are only needed on a few fields, like a description.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語固有インデックスに関する表現の修正"
}
```

### Explanation
この変更は、「search-language-support.md」記事における言語固有インデックスの説明の微修正です。具体的には、「alphanumeric content」という表現が「human readable content」に変更されました。この修正により、インデックスがサポートするコンテンツの内容がより明確になり、人間が読み取れる言語に特化したインデックス作成が容易に理解できるようになります。また、検索可能な文字列フィールドが同じ言語アナライザーに関連付けられることを強調し、ユーザーが適切な言語分析を利用して効果的な検索体験を実現できることを示しています。この修正は、Azure AI Searchの言語サポート機能の理解を深めることに寄与し、ユーザーが言語に応じたインデックスの作成を行いやすくします。

## articles/search/search-query-overview.md{#item-dcd5d6}

<details>
<summary>Diff</summary>
````diff
@@ -24,9 +24,9 @@ Azure AI Search supports query constructs for a broad range of scenarios, from f
 | [full text search](search-lucene-query-architecture.md) | Inverted indexes of tokenized terms. | Full text queries iterate over inverted indexes that are structured for fast scans, where a match can be found in potentially any field, within any number of search documents. Text is analyzed and tokenized for full text search.|
 | [Vector search](vector-search-overview.md) | Vector indexes of generated embeddings. | Vector queries iterate over vector fields in a search index. |
 | [Hybrid search](hybrid-search-overview.md) | All of the above, in a single search index. | Combines text search and vector search in a single query request. Text search works on plain text content in "searchable" and "filterable" fields. Vector search works on content in vector fields. |
-| Others | Plain text and alphanumeric content.| Raw content, extracted verbatim from source documents, supporting filters and pattern matching queries like geo-spatial search, fuzzy search, and fielded search. |
+| Others | Plain text and human-readable content.| Raw content, extracted verbatim from source documents, supporting filters and pattern matching queries like geo-spatial search, fuzzy search, and fielded search. |
 
-This article brings focus to the last category: queries that work on plain text and alphanumeric content, extracted intact from original source, used for filters and other specialized query forms.
+This article brings focus to the last category: queries that work on plain text and human-readable content, extracted intact from original source, used for filters and other specialized query forms.
 
 ## Autocomplete and suggested queries
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリオーバービューにおける表現の修正"
}
```

### Explanation
この変更は、「search-query-overview.md」記事において、クエリに関連する説明の微修正を行ったものです。特に、「alphanumeric content」という表現が「human-readable content」に置き換えられました。これにより、クエリの対象とするコンテンツがより明確に認識されるようになり、単に数値や文字列だけでなく、人間が理解できる形式の内容が含まれることを示しています。

この修正は、特に「Others」カテゴリーに関する説明箇所に焦点を当てており、元のソースから完全に抽出された生のコンテンツがどのようにフィルターや特定のクエリ形式で使用されるかについての理解を助けます。このようにして、Azure AI Searchにおけるクエリの多様な適用方法がより明確に伝わるようになっています。

## articles/search/vector-search-how-to-create-index.md{#item-97c769}

<details>
<summary>Diff</summary>
````diff
@@ -52,9 +52,9 @@ Make sure your documents:
 
    Vector fields contain an array generated by embedding models, one embedding per field, where the field is a top-level field (not part of a nested or complex type). For the simplest integration, we recommend the embedding models in [Azure OpenAI](https://aka.ms/oai/access), such as **text-embedding-ada-002** for text documents or the [Image Retrieval REST API](/rest/api/computervision/2023-02-01-preview/image-retrieval/vectorize-image) for images.
 
-   If you can take a dependency on indexers and skillsets, consider using [integrated vectorization](vector-search-integrated-vectorization.md) that encodes images and alphanumeric content during indexing. Your field definitions are for vector fields, but source data can be text or images, with vector arrays created during indexing.
+   If you can take a dependency on indexers and skillsets, consider using [integrated vectorization](vector-search-integrated-vectorization.md) that encodes images and textual content during indexing. Your field definitions are for vector fields, but incoming source data can be text or images, represented as vector arrays created during indexing.
 
-1. Provide other fields with human-readable alphanumeric content for the query response, and for hybrid query scenarios that include full text search or semantic ranking in the same request. 
+1. Provide other fields with human-readable content for the query response, and for hybrid query scenarios that include full text search or semantic ranking in the same request. 
 
 Your search index should include fields and content for all of the query scenarios you want to support. Suppose you want to search or filter over product names, versions, metadata, or addresses. In this case, similarity search isn't especially helpful. Keyword search, geo-search, or filters would be a better choice. A search index that includes a comprehensive field collection of vector and nonvector data provides maximum flexibility for query construction and response composition.
 
@@ -467,7 +467,7 @@ Vector fields are characterized by [their data type](/rest/api/searchservice/sup
 
 ## Load vector data for indexing
 
-Content that you provide for indexing must conform to the index schema and include a unique string value for the document key. Prevectorized data is loaded into one or more vector fields, which can coexist with other fields containing alphanumeric content.
+Content that you provide for indexing must conform to the index schema and include a unique string value for the document key. Prevectorized data is loaded into one or more vector fields, which can coexist with other fields containing nonvector content.
 
 You can use either [push or pull methodologies](search-what-is-data-import.md) for data ingestion. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索インデックス作成手順の表現修正"
}
```

### Explanation
この変更は、「vector-search-how-to-create-index.md」記事におけるベクトル検索インデックスの作成に関する説明の微修正です。具体的には、「alphanumeric content」という表現が「textual content」および「nonvector content」に変更されました。これにより、元のコンテンツがより広範囲に表現され、文字情報に加えて、非ベクトルデータの重要性も強調されます。

修正された記述は、インデックス作成時に画像やテキストデータを扱う際のガイダンスを提供し、より直感的な理解を促進します。また、クエリ応答に関連するフィールドを提供する際に「人間が読めるコンテンツ」であれば良いと明記されたことで、開発者にとっての柔軟性が向上します。

これにより、Azure AI Searchのベクトル検索機能に関するユーザーの理解が深まるとともに、構成要素全体にわたるデータの取り扱いについてのガイドラインが明確になります。


