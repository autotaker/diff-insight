---
date: '2025-10-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:09a6487...MicrosoftDocs:96b08d0
summary: この差分は、Azure AI Searchに関連する複数の記事におけるマイナーアップデートを含んでいます。主な修正内容には、用語の改善、新機能の詳細化、説明の補足があり、新機能としてスキルセットのベクトル化やエイリアスの活用、クエリやインデクサーの操作改善が含まれています。破壊的変更はなく、全体的な用語や説明の一貫性が向上しています。また、各記事の日付が更新され、文書の視覚的整理やクエリ作成ガイドの詳細化も行われています。これらの変更は、ドキュメントの使用性と正確性を向上させ、開発者が実際のプロジェクトに応用できる具体的な手順やアドバイスを提供することを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:09a6487...MicrosoftDocs:96b08d0){target="_blank"}

# Highlights
この差分は、Azure AI Searchに関連する複数の記事におけるマイナーアップデートを含んでいます。主な修正内容としては、用語の改善、新機能の詳細化、説明の補足などがあります。新しい機能例としては、スキルセットのベクトル化、エイリアスの有効活用、クエリやインデクサー操作の改善などが挙げられます。破壊的変更は報告されていません。

## New features
- スキルセットの生成内容に関する説明が改良され、チャンク処理やベクトル化スキルなどの新しい例が紹介されました。
- エイリアスの定義と利用メリットが明確になり、操作方法が詳細化されました。
- 検索クエリに関する指南が更新され、クエリリクエストでエイリアスや新しいパラメータが利用できることが強調されました。
- セマンティックランキングでのクエリ実行が向上し、新たにセマンティックキャプションのオプションが追加されました。

## Breaking changes
- 特に破壊的変更はありませんが、全体的に用語や説明が改善され、より一貫性と理解のしやすさが向上しています。

## Other updates
- 各記事の日付を最新のものに更新。
- コードブロック後の行追加により、文書の視覚的整理を改善。
- クエリ作成ガイドの詳細化により、インデックスとエンドポイントの要件が強調されました。

# Insights
これらの変更は、Azure AI Searchに関するドキュメントの使用性と正確性を向上させることを目的としています。それぞれの記事で紹介された新しいコンテンツや用語改善は、開発者が実際のプロジェクトに応用できるような具体的な手順やアドバイスを提供しています。

スキルセットに関する更新では、特に生成コンテンツにおけるベクトル化やテキストの強調がなされており、現代の情報検索に不可欠な構造化データの理解を深めるとともに、適切なスキルセットの利用法をより明確に伝えています。インデクサとの連携を具体化し、スキルセットの活用の幅が広がっていることがわかります。

エイリアスのアップデートでは、インデックス名の変更がシステム全体に及ぼす影響を最小限に抑える技術としてのエイリアスの価値が強調され、どういった状況で有効活用できるかが示されています。

検索クエリやセマンティッククエリの改良は、より正確で効率的な検索結果をユーザーに提供することを目指しており、特にセマンティッククエリでのランキング精度向上に寄与する新たなオプションは、多様な情報検索のニーズを満たすことができます。

全体として、これらの更新によってAzure AI Searchの文書はより現場での活用に適したものとなり、開発者が検索ソリューションを構築する際の信頼できるガイドラインとなっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-defining-skillset.md](#item-e2d71d) | minor update | スキルセットの定義に関する記事の更新 | modified | 6 | 4 | 10 | 
| [index-similarity-and-scoring.md](#item-75603d) | minor update | インデックスの類似性とスコアリングに関する記事の修正 | modified | 1 | 1 | 2 | 
| [search-faceted-navigation.md](#item-f29d1e) | minor update | ファセットナビゲーションに関する記事の日付更新と説明修正 | modified | 2 | 2 | 4 | 
| [search-how-to-alias.md](#item-3a72bc) | minor update | エイリアスに関する記事の拡充と更新 | modified | 32 | 5 | 37 | 
| [search-how-to-load-search-index.md](#item-a72573) | minor update | 検索インデックスへのデータ読み込みガイドの拡充 | modified | 43 | 9 | 52 | 
| [search-howto-run-reset-indexers.md](#item-fb10c8) | minor update | インデクサのリセット方法に関するガイドの更新 | modified | 19 | 11 | 30 | 
| [search-query-create.md](#item-532822) | minor update | 検索クエリ作成ガイドの更新 | modified | 16 | 3 | 19 | 
| [semantic-how-to-query-request.md](#item-85530d) | minor update | セマンティッククエリリクエストのガイドを更新 | modified | 10 | 21 | 31 | 


# Modified Contents
## articles/search/cognitive-search-defining-skillset.md{#item-e2d71d}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 05/08/2025
+ms.date: 10/02/2025
 ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
@@ -17,7 +17,7 @@ ms.custom:
 
 :::image type="content" source="media/cognitive-search-defining-skillset/indexer-stages-skillset.png" alt-text="Diagram showing the indexer stages, with Skillset Execution as the third stage of five.":::
 
-A skillset defines operations that generate textual content and structure from documents that contain images or unstructured text. Examples are optical character recognition (OCR) for images, entity recognition for undifferentiated text, and text translation. A skillset executes after text and images are extracted from an external data source, and after [field mappings](search-indexer-field-mappings.md) are processed.
+A skillset defines operations that generate vector and textual content and structure from documents that contain images or raw content. Examples are chunking skills, embedding (vectorization) skills, image verbalization, and other processes like optical character recognition (OCR) for images, entity recognition for undifferentiated text, and text translation. A skillset executes after raw content is extracted from an external data source, and after [field mappings](search-indexer-field-mappings.md) are processed.
 
 This article explains how to create a skillset using [REST APIs](/rest/api/searchservice/skillsets/create), but the same concepts and steps apply to other programming languages.
 
@@ -28,13 +28,15 @@ Rules for skillset definition include:
 + A skillset can repeat skills of the same type. For example, a skillset can have multiple Shaper skills.
 + A skillset supports chained operations, looping, and branching.
 
-Indexers drive skillset execution. You need an [indexer](search-howto-create-indexers.md), [data source](search-data-sources-gallery.md), and [index](search-what-is-an-index.md) before you can test your skillset.
+A skillset is attached to an indexer. To use the skillset, reference it in an [indexer](search-howto-create-indexers.md) and then run the indexer to import data, invoke skills processing, and send output to an [index](search-what-is-an-index.md). A skillset is high-level resource, but it's operational only within indexer processing. As a high-level resource, you can reference it in multiple indexers.
 
 > [!TIP]
 > Enable [enrichment caching](enrichment-cache-how-to-configure.md) to reuse the content you've already processed and lower the cost of development.
 
 ## Add a skillset definition
 
+Creating a skillset adds it to your search service. Updating a skillset fully overwrites an existing skillset with the contents of the request payload. A best practice for updates is to retrieve the skillset definition with a GET, modify it, and then update with PUT.
+
 Start with the basic structure. In the [Create Skillset REST API](/rest/api/searchservice/skillsets/create), the body of the request is authored in JSON and has the following sections:
 
 ```json
@@ -65,7 +67,7 @@ Start with the basic structure. In the [Create Skillset REST API](/rest/api/sear
 
 After the name and description, a skillset has four main properties:
 
-+ `skills` array, an unordered [collection of skills](cognitive-search-predefined-skills.md). Skills can be utilitarian (like splitting text), transformational (based on AI from Azure AI services), or custom skills that you provide. An example of a skills array is provided in the next section.
++ `skills` array, an unordered [collection of skills](cognitive-search-predefined-skills.md). Skills are either standalone or chained together through input-output associations, where the output of one transform becomes input to another. Skills can be utilitarian (like splitting text), transformational (based on AI from Azure OpenAI or Azure AI services), or custom skills that you provide. An example of a skills array is provided in the next section.
 
 + `cognitiveServices` is used for [billable skills](cognitive-search-predefined-skills.md) that call Azure AI services APIs. Remove this section if you aren't using billable skills or Custom Entity Lookup. If you are, attach [an Azure AI services multi-service resource](cognitive-search-attach-cognitive-services.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スキルセットの定義に関する記事の更新"
}
```

### Explanation
この変更では、コグニティブ サーチのスキルセットを定義するための文書が更新されました。主な修正点は、記事の日付の更新、スキルセットの説明における用語の改善、及びいくつかの追加説明の挿入です。

具体的には、スキルセットが生成する内容に関する説明が変更され、ベクトルとテキストの内容が強調されています。新しい例として、チャンク処理やベクトル化スキル、画像の言語化が挙げられました。また、スキルセットの処理に関する操作とインデクサーとの関連性が明確にされており、ユーザーがスキルセットをどのように使用できるかをよりよく理解できるようになっています。特に、スキルセットが一つのインデクサーに紐付けられ、複数のインデクサーで参照可能であることが強調されました。

最後に、スキルセットの更新に際しては、GETリクエストでスキルセットの定義を取得し、その後PUTリクエストを使用して更新することが推奨されています。この変更により、文書はより正確で使いやすくなり、開発者がコグニティブ サーチのスキルセットを理解するのに役立つ情報が提供されています。

## articles/search/index-similarity-and-scoring.md{#item-75603d}

<details>
<summary>Diff</summary>
````diff
@@ -104,7 +104,7 @@ POST https://[service name].search.windows.net/indexes/hotels/docs/search?api-ve
 }
 ```
 
-Using `scoringStatistics` will ensure that all shards in the same replica provide the same results. That said, different replicas can be slightly different from one another as they're always getting updated with the latest changes to your index. In some scenarios, you might want your users to get more consistent results during a "query session". In such scenarios, you can provide a `sessionId` as part of your queries. The `sessionId` is a unique string that you create to refer to a unique user session.
+Using `scoringStatistics` will ensure that all shards in the same replica provide the same results. That said, different replicas can be slightly different from one another as they're always getting updated with the latest changes to your index. In some scenarios, you might want your users to get more consistent results during a "query session". In such scenarios, you can provide a `sessionId` as part of your queries. The `sessionId` is a unique string that you create to refer to a unique user session. 
 
 ```http
 POST https://[service name].search.windows.net/indexes/hotels/docs/search?api-version=2025-09-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスの類似性とスコアリングに関する記事の修正"
}
```

### Explanation
この変更は、インデックスの類似性とスコアリングに関する文書のマイナーアップデートです。具体的には、コードブロックの後に空の行を追加しました。これにより、コードとその説明文との間に適切なスペースが確保され、読みやすさが向上しています。

内容としては、`scoringStatistics`を使用することで、同一のレプリカ内のすべてのシャードが同じ結果を提供することが保証されることが述べられています。さらに、異なるレプリカ間で若干の違いが生じる可能性があることや、クエリセッション中にユーザーにより一貫した結果を提供するために`sessionId`を使用することの重要性も説明されています。`sessionId`は、特定のユーザーセッションを参照するために生成される一意の文字列です。

この修正により、文書は視覚的に整理され、重要な情報が強調されたことで、ユーザーが理解しやすくなっています。

## articles/search/search-faceted-navigation.md{#item-f29d1e}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 04/04/2025
+ms.date: 10/02/2025
 ms.update-cycle: 365-days
 ---
 
@@ -217,7 +217,7 @@ Here's a screenshot of the [basic facet query example](search-faceted-navigation
 
     | Facet parameter | Description and usage |
     |-----------------|-----------------------|
-    | `count` | Maximum number of facet terms per structure; default is 10. An example is `Tags,count:5`. There's no upper limit on the number of terms, but higher values degrade performance, especially if the faceted field contains a large number of unique terms. This is due to the way faceting queries are distributed across shards. You can set count to zero or to a value that's greater than or equal to the number of unique values in the "facetable" field to get an accurate count across all shards. The tradeoff is increased latency.
+    | `count` | Maximum number of facet terms per structure; default is 10. An example is `"facet=category,count:5" gets the top five categories in facet results`. There's no upper limit on the number of terms, but higher values degrade performance, especially if the faceted field contains a large number of unique terms. If the count parameter is less than the number of unique terms, the results may not be accurate. This is due to the way faceting queries are distributed across shards. You can set count to zero or to a value that's greater than or equal to the number of unique values in the "facetable" field to get an accurate count across all shards. The tradeoff is increased latency.
     | `sort` | Set to `count`, `-count`, `value`, `-value`. Use `count` to sort descending by count. Use `-count` to sort ascending by count. Use `value` to sort ascending by value. Use `-value` to sort descending by value (for example, `"facet=category,count:3,sort:count"` gets the top three categories in facet results in descending order by the number of documents with each Category name). If the top three categories are Budget, Motel, and Luxury, and Budget has five hits, Motel has 6, and Luxury has 4, then the buckets are in the order Motel, Budget, Luxury. For `-value`, `"facet=rating,sort:-value"` produces buckets for all possible ratings, in descending order by value (for example, if the ratings are from 1 to 5, the buckets are ordered 5, 4, 3, 2, 1, irrespective of how many documents match each rating). |
     | `values` | Set to pipe-delimited numeric or `Edm.DateTimeOffset` values specifying a dynamic set of facet entry values. For example, `"facet=baseRate,values:10 | 20"` produces three buckets: one for base rate 0 up to but not including 10, one for 10 up to but not including 20, and one for 20 and higher. A string `"facet=lastRenovationDate,values:2010-02-01T00:00:00Z"` produces two buckets: one for hotels renovated before February 2010, and one for hotels renovated February 1, 2010 or later. The values must be listed in sequential, ascending order to get the expected results. |
     | `interval` | An integer interval greater than zero for numbers, or minute, hour, day, week, month, quarter, year for date time values. For example, `"facet=baseRate,interval:100"` produces buckets based on base rate ranges of size 100. If base rates are all between $60 and $600, there are buckets for 0-100, 100-200, 200-300, 300-400, 400-500, and 500-600. The string `"facet=lastRenovationDate,interval:year"` produces one bucket for each year when hotels were renovated. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファセットナビゲーションに関する記事の日付更新と説明修正"
}
```

### Explanation
この変更は、ファセットナビゲーションに関する文書のマイナーアップデートです。主な修正点は、記事の日付が2025年4月4日から2025年10月2日に変更されたこと、及び`count`パラメータに関する説明の向上です。

具体的には、`count`パラメータの例が具体化され、例えば「`facet=category,count:5`」から「`"facet=category,count:5" gets the top five categories in facet results`」に修正されました。この変更により、どのようにファセット結果が取得されるのかがより明確に説明されています。また、`count`パラメータの値がユニークな項目数より少ない場合は、結果が正確ではない可能性があることも強調されています。

これにより、文書は一貫性のある情報を提供し、読者がファセットナビゲーションの機能を理解しやすくなるように調整されています。

## articles/search/search-how-to-alias.md{#item-3a72bc}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/27/2025
+ms.date: 10/01/2025
 ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
@@ -18,7 +18,9 @@ ms.custom:
 > [!IMPORTANT]
 > Index aliases are currently in public preview and available under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 
-An index alias in Azure AI Search is an alternate name for an index. You can use the alias instead of the index name in your application, which minimizes future updates to production code. If you need to switch to a newer index, you can update the alias mapping.
+In Azure AI Search, an index alias is a secondary name for a search index. You can create an alias that maps to a search index and substitute the alias name in places where you would otherwise reference an index name. This gives you flexibility if you ever need to change which index your application is pointing to. Instead of updating the references to the index name in your production code, you can just update the mapping for your alias.
+
+You can create and manage aliases in Azure AI Search service via HTTP requests (POST, GET, PUT, DELETE) against a given alias resource. Aliases are service level resources and maintained independently from search indexes. Once a search index is created, you can create an alias that maps to that search index.
 
 Before using an alias, your application sends requests directly to `hotel-samples-index`.
 
@@ -46,12 +48,18 @@ POST /indexes/my-alias/docs/search?api-version=2025-08-01-preview
 
 You can only use an alias with document operations or to get and update an index definition. 
 
-Aliases can't be used to [delete an index](/rest/api/searchservice/indexes/delete), or [test text tokenization](/rest/api/searchservice/indexes/analyze), or referenced as the `targetIndexName` on an [indexer](/rest/api/searchservice/indexers/create-or-update).
+Aliases can't be used to [delete an index](/rest/api/searchservice/indexes/delete), or [test text tokenization](/rest/api/searchservice/indexes/analyze), or be referenced as the `targetIndexName` on an [indexer](/rest/api/searchservice/indexers/create-or-update) or [knowledge source](search-knowledge-source-how-to-index.md).
 
 ## Create an index alias
 
+Creating an alias establishes a mapping between an alias name and an index name. If the request is successful, the alias can be used for indexing, querying, and other operations.
+
+Updating an alias allows you to map that alias to a different search index. When you update an existing alias, the entire definition is replaced with the contents of the request body. In general, the best pattern to use for updates is to retrieve the alias definition with a GET, modify it, and then update it with PUT.
+
 You can create an alias using the preview REST API, the preview SDKs, or through the [Azure portal](https://portal.azure.com). An alias consists of the `name` of the alias and the name of the search index that the alias is mapped to. Only one index name can be specified in the `indexes` array.
 
+The maximum number of aliases that you can create varies by pricing tier. For more information, see [Service limits](search-limits-quotas-capacity.md).
+
 ### [**REST API**](#tab/rest)
 
 You can use the [Create or Update Alias (REST preview)](/rest/api/searchservice/aliases/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) to create an index alias.
@@ -77,8 +85,7 @@ Follow the steps below to create an index alias in the Azure portal.
 
 ### [**.NET SDK**](#tab/sdk)
 
-
-Using one of the beta packages from the [Azure SDK for .NET](https://www.nuget.org/packages/Azure.Search.Documents/), you can use the following syntax to create an index alias. 
+Using one of the preview packages from the [Azure SDK for .NET](https://www.nuget.org/packages/Azure.Search.Documents/), you can use the following syntax to create an index alias. 
 
 ```csharp
 // Create a SearchIndexClient
@@ -110,8 +117,26 @@ POST /indexes/my-alias/docs/search?api-version=2025-08-01-preview
 }
 ```
 
+## Get an alias definition
+
+This request returns a list of existing alias objects by name.
+
+```http
+GET https://[service name].search.windows.net/aliases?api-version=[api-version]&$select=name
+api-key: [admin key]  
+```
+
+This request returns an alias definition
+
+```http
+GET https://[service name].search.windows.net/aliases/my-alias?api-version=[api-version]
+api-key: [admin key]  
+```
+
 ## Update an alias
 
+The most common update to an alias is changing the index name when the underlying index is replaced with a newer version.
+
 PUT is required for alias updates as described in [Create or Update Alias (REST preview)](/rest/api/searchservice/aliases/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true).
 
 ```http
@@ -124,6 +149,8 @@ PUT /aliases/my-alias?api-version=2025-08-01-preview
 
 An update to an alias may take up to 10 seconds to propagate through the system so you should wait at least 10 seconds before deleting the index that the alias was previously mapped to.
 
+If you attempt to delete an index that is currently mapped to an alias, the operation will fail with 400 (Bad Request) and an error message stating that the alias(es) that's mapped to that index must be deleted or mapped to a different index before the index can be deleted.
+
 ## See also
 
 + [Drop and rebuild an index in Azure AI Search](search-howto-reindex.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エイリアスに関する記事の拡充と更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるエイリアスについての文書を更新し、情報を拡充したものです。主な修正点には、エイリアスの定義の明確化とともに、エイリアスの作成や管理に関する情報が追加されています。

具体的には、エイリアスが検索インデックスの代替名であり、アプリケーション内でインデックス名の代わりにエイリアスを使用できる利点が詳述されています。これにより、インデックス名の変更が発生した際のアプリケーションの修正を最小限に抑えることができます。また、エイリアスを HTTP リクエストによって管理する方法（POST、GET、PUT、DELETE）や、どの操作にエイリアスを使用できるかについても具体的な説明がなされています。

新たに、エイリアス作成時の成功レスポンス、エイリアスの更新方法、エイリアスの定義取得のためのリクエスト例が追加されています。これにより、ユーザーはエイリアスの無限の可能性と利便性をより理解しやすくなっています。さらに、エイリアスの最大数や料金プランに関する情報も盛り込まれています。

このように、文書が充実したことにより、ユーザーはAzure AI Searchにおけるエイリアスの役割と管理方法をより明確に理解できるようになっています。

## articles/search/search-how-to-load-search-index.md{#item-a72573}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: how-to
-ms.date: 05/08/2025
+ms.date: 10/02/2025
 ---
 
 # Load data into a search index in Azure AI Search
@@ -19,15 +19,15 @@ This article explains how to import documents into a predefined search index. In
 
 A search service accepts JSON documents that conform to the index schema. A search service can import and index plain text content and vector content in JSON documents.
 
-+ Plain text content is retrieved from fields in the external data source, from metadata properties, or from enriched content that's generated by a [skillset](cognitive-search-working-with-skillsets.md) (skills can extract or infer textual descriptions from images and unstructured content).
++ Plain text content is retrieved from fields in the external data source, from metadata properties, or from enriched content that's generated by a [skillset](cognitive-search-working-with-skillsets.md). Skills can extract or infer textual descriptions from images and unstructured content.
 
 + Vector content is retrieved from a data source that provides it, or it's created by a skillset that implements [integrated vectorization](vector-search-integrated-vectorization.md) in an Azure AI Search indexer workload.
 
 You can prepare these documents yourself, but if content resides in a [supported data source](search-indexer-overview.md#supported-data-sources), running an [indexer](search-indexer-overview.md) or using an Import wizard can automate document retrieval, JSON serialization, and indexing.
 
 Once data is indexed, the physical data structures of the index are locked in. For guidance on what can and can't be changed, see [Update and rebuild an index](search-howto-reindex.md).
 
-Indexing isn't a background process. A search service will balance indexing and query workloads, but if [query latency is too high](search-performance-analysis.md#impact-of-indexing-on-queries), you can either [add capacity](search-capacity-planning.md#add-or-remove-partitions-and-replicas) or identify periods of low query activity for loading an index.
+Indexing isn't a background process. A search service balances indexing and query workloads, but if [query latency is too high](search-performance-analysis.md#impact-of-indexing-on-queries), you can either [add capacity](search-capacity-planning.md#add-or-remove-partitions-and-replicas) or identify periods of low query activity for loading an index.
 
 For more information, see [Data import strategies](search-what-is-data-import.md).
 
@@ -50,9 +50,13 @@ In the Azure portal, use an [import wizard](search-import-data-portal.md) to cre
 
 ## Use the REST APIs
 
-[Documents - Index](/rest/api/searchservice/documents) is the REST API for importing data into a search index. REST APIs are useful for initial proof-of-concept testing, where you can test indexing workflows without having to write much code. The `@search.action` parameter determines whether documents are added in full, or partially in terms of new or replacement values for specific fields.
+[Documents - Index](/rest/api/searchservice/documents) is the REST API for importing data into a search index. 
 
-[**Quickstart: Full-text search using REST**](search-get-started-text.md) explains the steps. The following example is a modified version of the example. It's been trimmed for brevity and the first HotelId value has been altered to avoid overwriting an existing document.
+The body of the request contains one or more documents to be indexed. Documents are uniquely identified through a case-sensitive key. Each document is associated with an action: "upload", "delete", "merge", or "mergeOrUpload". Upload requests must include the document data as a set of key/value pairs.
+
+REST APIs are useful for initial proof-of-concept testing, where you can test indexing workflows without having to write much code. The `@search.action` parameter determines whether documents are added in full, or partially in terms of new or replacement values for specific fields.
+
+[**Quickstart: Full-text search using REST**](search-get-started-text.md) explains the steps. The following example is a modified version of the example. The value is trimmed for brevity and the first HotelId value is altered to avoid overwriting an existing document.
 
 1. Formulate a POST call specifying the index name, the "docs/index" endpoint, and a request body that includes the `@search.action` parameter.
 
@@ -82,23 +86,53 @@ In the Azure portal, use an [import wizard](search-import-data-portal.md) to cre
     }
     ```
 
-1. Set the `@search.action` parameter to `upload` to create or overwrite a document. Set it to `merge` or `uploadOrMerge` if you're targeting updates to specific fields within the document. The previous example shows both actions.
+1. Set the `@search.action` parameter to `upload` to create or overwrite a document. Set it to `merge` or `uploadOrMerge` if you're targeting updates to specific fields within the document. The previous example shows both actions. 
 
    | Action | Effect |
    |--------|--------|
-   | merge | Updates a document that already exists, and fails a document that can't be found. Merge replaces existing values. For this reason, be sure to check for collection fields that contain multiple values, such as fields of type `Collection(Edm.String)`. For example, if a `tags` field starts with a value of `["budget"]` and you execute a merge with `["economy", "pool"]`, the final value of the `tags` field is `["economy", "pool"]`. It won't be `["budget", "economy", "pool"]`. |
-   | mergeOrUpload | Behaves like merge if the document exists, and upload if the document is new. This is the most common action for incremental updates. |
    | upload | Similar to an "upsert" where the document is inserted if it's new, and updated or replaced if it exists. If the document is missing values that the index requires, the document field's value is set to null. |
+   | merge | Updates a document that already exists, and fails a document that can't be found. Merge replaces existing values. For this reason, be sure to check for collection fields that contain multiple values, such as fields of type `Collection(Edm.String)`. For example, if a `tags` field starts with a value of `["budget"]` and you execute a merge with `["economy", "pool"]`, the final value of the `tags` field is `["economy", "pool"]`. It isn't `["budget", "economy", "pool"]`. |
+   | mergeOrUpload | Behaves like merge if the document exists, and upload if the document is new. This is the most common action for incremental updates. |
+   | delete | Delete removes the specified document from the index. Any field you specify in a delete operation, other than the key field, is ignored. If you want to remove an individual field from a document, use merge instead and set the field explicitly to null.|
+
+   There are no ordering guarantees for which action in the request body is executed first. It's not recommended to have multiple "merge" actions associated with the same document in a single request body. If there are multiple "merge" actions required for the same document, perform the merging client-side before updating the document in the search index.
+
+   In primitive collections, if the document contains a Tags field of type `Collection(Edm.String)` with a value of ["budget"], and you execute a merge with a value of ["economy", "pool"] for Tag, the final value of the Tags field will be ["economy", "pool"]. It isn't ["budget", "economy", "pool"].
+
+   In complex collections, if the document contains a complex collection field named Rooms with a value of [{ "Type": "Budget Room", "BaseRate": 75.0 }], and you execute a merge with a value of [{ "Type": "Standard Room" }, { "Type": "Budget Room", "BaseRate": 60.5 }], the final value of the Rooms field will be [{ "Type": "Standard Room" }, { "Type": "Budget Room", "BaseRate": 60.5 }]. It won't be either of the following:
+
+   + [{ "Type": "Budget Room", "BaseRate": 75.0 }, { "Type": "Standard Room" }, { "Type": "Budget Room", "BaseRate": 60.5 }] (append elements)
+
+   + [{ "Type": "Standard Room", "BaseRate": 75.0 }, { "Type": "Budget Room", "BaseRate": 60.5 }] (merge elements in order, then append any extras)
+
+   > [!NOTE]
+   > When you upload DateTimeOffset values with time zone information to your index, Azure AI Search normalizes these values to UTC. For example, 2025-01-13T14:03:00-08:00 will be stored as 2025-01-13T22:03:00Z. If you need to store time zone information, add an extra column to your index.
 
 1. Send the request.
 
+   The following table explains the various per-document [status codes](/rest/api/searchservice/http-status-codes) that can be returned in the response. Some status codes indicate problems with the request itself, while others indicate temporary error conditions. The latter you should retry after a delay.
+
+   |Status code|Meaning|Retryable|Notes|
+   |-----------|-------|---------|-----| 
+   |200|Document was successfully modified or deleted.|n/a|Delete operations are [idempotent](https://en.wikipedia.org/wiki/Idempotence). That is, even if a document key doesn't exist in the index, attempting a delete operation with that key results in a 200 status code.|
+   |201|Document was successfully created.|n/a||
+   |400|There was an error in the document that prevented it from being indexed.|No|The error message in the response indicates what is wrong with the document.|
+   |404|The document couldn't be merged because the given key doesn't exist in the index.|No|This error doesn't occur for uploads since they create new documents, and it doesn't occur for deletes because they're [idempotent](https://en.wikipedia.org/wiki/Idempotence).|
+   |409|A version conflict was detected when attempting to index a document.|Yes|This can happen when you're trying to index the same document more than once concurrently.|
+   |422|The index is temporarily unavailable because it was updated with the 'allowIndexDowntime' flag set to 'true'.|Yes||
+   |429|Indicates that you have exceeded your quota on the number of documents per index. |No | You must either create a new index or upgrade for higher capacity limits.|
+   |503|Your search service is temporarily unavailable, possibly due to heavy load.|Yes|Your code should wait before retrying in this case or you risk prolonging the service unavailability.|
+
+   > [!NOTE]  
+   > If your client code frequently encounters a 207 response, one possible reason is that the system is under load. You can confirm this by checking the `statusCode` property for 503. If this is the case, we recommend throttling indexing requests. Otherwise, if indexing traffic doesn't subside, the system could start rejecting all requests with 503 errors.  
+
 1. [Look up the documents](/rest/api/searchservice/documents/get) you just added as a validation step:
 
     ```http
     GET https://[service name].search.windows.net/indexes/hotel-sample-index/docs/1111?api-version=2025-09-01
     ```
 
-When the document key or ID is new, **null** becomes the value for any field that is unspecified in the document. For actions on an existing document, updated values replace the previous values. Any fields that weren't specified in a "merge" or "mergeUpload" are left intact in the search index.
+When the document key or ID is new, **null** becomes the value for any field that's unspecified in the document. For actions on an existing document, updated values replace the previous values. Any fields that weren't specified in a "merge" or "mergeUpload" are left intact in the search index.
 
 ## Use the Azure SDKs
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスへのデータ読み込みガイドの拡充"
}
```

### Explanation
この変更は、Azure AI Searchにおける検索インデックスへのデータの読み込み方法を詳しく解説した記事を更新し、内容を拡充したものです。主な修正点には、日付の更新とともに、文書の構造や説明の改善が含まれています。

具体的には、文書にはプレーンテキストコンテンツとベクトルコンテンツの取り扱いについての詳細が追加され、特にベクトルコンテンツを生成するためのスキルセットの使用に関する情報が明確に示されています。また、データインポート戦略やインデクサーの使用に関する詳細が補足され、文書の取り扱いが容易になっています。

さらに、REST APIを利用してデータをインデックスにインポートする方法について、新たなリクエストボディの構成やアクションパラメータの意味も詳しく紹介されています。エラーハンドリングに関するステータスコードの表が追加され、特に共通のエラー条件やリトライ可能なエラーについての説明が充実しています。

全体として、この更新によりユーザーは検索インデックスへのデータのロード方法についてより深く理解できるようになり、実践的な情報が豊富に提供されています。

## articles/search/search-howto-run-reset-indexers.md{#item-fb10c8}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 09/01/2025
+ms.date: 10/02/2025
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
@@ -183,12 +183,14 @@ catch (RequestFailedException ex) when (ex.Status == 429)
 
 ## How to reset skills (preview)
 
-For indexers that have skillsets, you can reset individual skills to force processing of just that skill and any downstream skills that depend on its output. The [enrichment cache](enrichment-cache-how-to-configure.md), if you enabled it, is also refreshed. 
+The Reset Skills request selectively processes one or more skills on the next indexer run. For indexers that have skillsets, you can reset individual skills to force reprocessing of just that skill and any downstream skills that depend on its output. The [enrichment cache](enrichment-cache-how-to-configure.md), if you enabled it, is also refreshed. 
 
-[Reset Skills](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2024-05-01-preview&preserve-view=true) is currently REST-only, available through 2020-06-30-preview or later. We recommend the latest preview API.
+For indexers that have caching enabled, you can explicitly request processing for skill updates that the indexer cannot detect. For example, if you make external changes, such as revisions to a custom skill, you can use this API to rerun the skill. Outputs, such as a knowledge store or search index, are refreshed using reusable data from the cache and new content per the updated skill.
+
+We recommend the [latest preview API](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2025-08-01-preview&preserve-view=true).
 
 ```http
-POST /skillsets/[skillset name]/resetskills?api-version=2024-05-01-preview
+POST /skillsets/[skillset name]/resetskills?api-version=2025-08-01-preview
 {
     "skillNames" : [
         "#1",
@@ -202,28 +204,28 @@ You can specify individual skills, as indicated in the example above, but if any
 
 If no skills are specified, the entire skillset is executed and if caching is enabled, the cache is also refreshed.
 
-Remember to follow up with Run Indexer to invoke actual processing.
+Remember to follow up with [Run Indexer](/rest/api/searchservice/indexers/run) to invoke actual processing.
 
 <a name="reset-docs"></a>
 
 ## How to reset docs (preview)
 
-The [Indexers - Reset Docs](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2024-05-01-preview&preserve-view=true) accepts a list of document keys so that you can refresh specific documents. If specified, the reset parameters become the sole determinant of what gets processed, regardless of other changes in the underlying data. For example, if 20 blobs were added or updated since the last indexer run, but you only reset one document, only that document is processed.
+The [Indexers - Reset Docs (preview)](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2025-08-01-preview&preserve-view=true) accepts a list of document keys so that you can refresh specific documents. If specified, the reset parameters become the sole determinant of what gets processed, regardless of other changes in the underlying data. For example, if 20 blobs were added or updated since the last indexer run, but you only reset one document, only that document is processed.
 
 On a per-document basis, all fields in the search document are refreshed with values and metadata from the data source. You can't pick and choose which fields to refresh. 
 
 If the data source is Azure Data Lake Storage (ADLS) Gen2, and the blobs are associated with permission metadata, those permissions are also re-ingested in the search index if permissions change in the underlying data. For more information, see [Re-indexing ACL and RBAC scope with ADLS Gen2 indexers](search-indexer-access-control-lists-and-role-based-access.md#synchronize-permissions-between-indexed-and-source-content).
 
 If the document is enriched through a skillset and has cached data, the  skillset is invoked for just the specified documents, and the cache is updated for the reprocessed documents.
 
-When you're testing this API for the first time, the following APIs can help you validate and test the behaviors. You can use preview API version 2020-06-30-preview and later. We recommend the latest preview API.
+When you're testing this API for the first time, the following APIs can help you validate and test the behaviors. We recommend the latest preview API.
 
-1. Call [Indexers - Get Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2024-05-01-preview&preserve-view=true) with a preview API version to check reset status and execution status. You can find information about the reset request at the end of the status response.
+1. Call [Indexers - Get Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-08-01-preview&preserve-view=true) with a preview API version to check reset status and execution status. You can find information about the reset request at the end of the status response.
 
-1. Call [Indexers - Reset Docs](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2024-05-01-preview&preserve-view=true) with a preview API version to specify which documents to process.
+1. Call [Indexers - Reset Docs](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2025-08-01-preview&preserve-view=true) with a preview API version to specify which documents to process.
 
     ```http
-    POST https://[service name].search.windows.net/indexers/[indexer name]/resetdocs?api-version=2024-05-01-preview
+    POST https://[service name].search.windows.net/indexers/[indexer name]/resetdocs?api-version=2025-08-01-preview
     {
         "documentKeys" : [
             "1001",
@@ -232,10 +234,16 @@ When you're testing this API for the first time, the following APIs can help you
     }
     ```
 
+    + The API accepts two types of document identifiers as input: Document keys that uniquely identify documents in a search index, and datasource document identifiers that uniquely identify documents in a data source. The body should contain either a list of document keys *or* a list of data source document identifiers that the indexer looks for in the data source. Invoking the API adds the document keys or data source document identifiers to be reset to the indexer metadata. On the next scheduled or on-demand run of the indexer, the indexer processes only the reset documents. 
+
+    + If you use document keys to reset documents and your document keys are referenced in an indexer field mapping, the indexer uses field mapping to locate the appropriate field in the underlying data source.
+
     + The document keys provided in the request are values from the search index, which can be different from the corresponding fields in the data source. If you're unsure of the key value, [send a query](search-query-create.md) to return the value. You can use `select` to return just the document key field.
 
     + For blobs that are parsed into multiple search documents (where parsingMode is set to [jsonLines or jsonArrays](search-howto-index-json-blobs.md), or [delimitedText](search-howto-index-csv-blobs.md)), the document key is generated by the indexer and might be unknown to you. In this scenario, a query for the document key to return the correct value.
 
+    + If you want the indexer to stop trying to process reset documents, you can set "documentKeys" or "datasourceDocumentIds" to an empty list "[]". This results in the indexer resuming regular indexing based on the high water mark. Invalid document keys or document keys that don't exist are ignored.
+
 1. Call [Run Indexer](/rest/api/searchservice/indexers/run) (any API version) to process the documents you specified. Only those specific documents are indexed.
 
 1. Call [Run Indexer](/rest/api/searchservice/indexers/run) a second time to process from the last high-water mark.
@@ -247,7 +255,7 @@ When you're testing this API for the first time, the following APIs can help you
 Calling Reset Documents API multiple times with different keys appends the new keys to the list of document keys reset. Calling the API with the **`overwrite`** parameter set to true will overwrite the current list with the new one:
 
 ```http
-POST https://[service name].search.windows.net/indexers/[indexer name]/resetdocs?api-version=2020-06-30-Preview
+POST https://[service name].search.windows.net/indexers/[indexer name]/resetdocs?api-version=2025-08-01-Preview
 {
     "documentKeys" : [
         "200",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサのリセット方法に関するガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるインデクサのリセット方法に関する記事を更新し、重要な情報を追加したものです。主な修正点には、日付の更新と、インデクサのスキルリセットとドキュメントリセットに関するプロセスの詳細な説明が含まれています。

具体的には、スキルリセットのリクエストが次のインデクサの実行時に特定のスキルを選択的に処理し、関連するスキルを再処理する機能が追加されています。スキルの変更が外部で行われた場合など、新しいコンテンツに基づいてキャッシュされたデータを更新する方法が詳述され、利用者がスキルの変更に応じてインデクサを適切に管理できるようになっています。

また、ドキュメントリセットの部分も更新され、リセットパラメータがプロセスされるドキュメントを決定する明確な説明が追加されました。特定のドキュメントをリセットすることで、基になるデータの他の変更にかかわらず選択されたドキュメントのみが処理されることが強調されています。

さらに、リセット時に指定されたドキュメントキーまたはデータソース文書識別子の利用方法についても詳しく説明が追加されており、ユーザーはインデクサーがどのように動作するかをよりよく理解できるようになっています。これにより、運用中のインデクサーの管理がより円滑に行えるようになります。

## articles/search/search-query-create.md{#item-532822}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 04/14/2025
+ms.date: 10/02/2025
 ms.update-cycle: 180-days
 ---
 
@@ -19,7 +19,7 @@ If you're building a query for [full text search](search-lucene-query-architectu
 
 ## Prerequisites
 
-+ A [search index](search-how-to-create-search-index.md) with string fields attributed as *searchable*.
++ A [search index](search-how-to-create-search-index.md) with string fields attributed as *searchable*. You can also use an [index alias](search-how-to-alias.md) as the endpoint of your query request.
 
 + Read permissions on the search index. For read access, include a [query API key](search-security-api-keys.md) on the request, or give the caller [Search Index Data Reader](search-security-rbac.md) permissions.
 
@@ -60,7 +60,7 @@ Parameters used to shape the response:
 
 + **`top`** returns the specified number of best-matching documents. In this example, only 10 hits are returned. You can use top and skip (not shown) to page the results.
 
-+ **`count`** tells you how many documents in the entire index match overall, which can be more than what are returned. 
++ **`count`** tells you how many documents in the entire index match overall, which can be more than what are returned. Valid values are "true" or "false". Defaults to "false". Count is accurate if the index is stable, but will under or over-report any documents that are actively added, updated, or deleted. If you’d like to get only the count without any documents, you can use $top=0.
 
 + **`orderby`** is used if you want to sort results by a value, such as a rating or location. Otherwise, the default is to use the relevance score to rank results. A field must be attributed as *sortable* to be a candidate for this parameter.
 
@@ -100,6 +100,10 @@ In the Azure portal, when you open an index, you can work with Search Explorer a
 
 ### [**REST API**](#tab/rest-text-query)
 
+When called with GET, the length of the request URL can't exceed 8 KB. This length is enough for most applications. However, some applications produce large queries, specifically when OData filter expressions are used. For these applications, HTTP POST is a better choice because it allows larger filters than GET.
+
+With POST, the number of clauses in a filter is the limiting factor, not the size of the raw filter string since the request size limit for POST is approximately 16 MB. Even though the POST request size limit is large, filter expressions can't be arbitrarily complex. For more information about filter complexity limitations, see [OData Expression Syntax](query-odata-filter-orderby-syntax.md).
+
 Use a REST client to set up a request. If you need help with getting started, see [Quickstart: Full-text search using REST](search-get-started-text.md).
 
 The following example calls the REST API for full text search:
@@ -116,6 +120,15 @@ POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/
 }
 ```
 
+**Continuation of Partial Search Responses**
+
+Sometimes Azure AI Search can't return all the requested results in a single Search response. A partial response can happen for different reasons, such as when the query returns too many documents by not specifying $top, or by specifying a value for $ top that's too large. In such cases, Azure AI Search includes the @odata.nextLink annotation in the response body, and also @search.nextPageParameters if it was a POST request. You can use the values of these annotations to formulate another Search request to get the next part of the search response. This behavior is called a *continuation* of the original Search request, and the annotations are called *continuation tokens*. See the example in the Response section for details on the syntax of these annotations and where they appear in the response body.  
+
+The reasons why Azure AI Search might return continuation tokens are implementation-specific and subject to change. Robust clients should always be ready to handle cases where fewer documents than expected are returned and a continuation token is included to continue retrieving documents. Also note that you must use the same HTTP method as the original request in order to continue. For example, if you sent a GET request, any continuation requests you send must also use GET (and likewise for POST).
+
+> [!NOTE]
+> The purpose of @odata.nextLink and @search.nextPageParameters is to protect the service from queries that request too many results, not to provide a general mechanism for paging. If you want to page through results, use $top and $skip together. For example, if you want pages of size 10, your first request should have $top=10 and $skip=0, the second request should have $top=10 and $skip=10, the third request should have $top=10 and $skip=20, and so on.
+
 ### [**Azure SDKs**](#tab/sdk-text-query)
 
 The following Azure SDKs provide a `SearchClient` that has methods for formulating query requests.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索クエリ作成ガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchの検索クエリ作成に関する記事を更新し、最新の情報を追加したものです。主な修正点には、日付の更新、新機能や使用方法に関する詳細な説明が含まれています。

具体的には、検索インデックスについての要件が拡充され、インデックスエイリアスをクエリリクエストのエンドポイントとして使用することができる旨が追加されました。また、コンテンツに対する読み取り権限の取得方法に関する情報が強調されています。

さらに、クエリパラメータに関するセクションが整理され、`count` パラメータに有効な値（"true" または "false"）が設定できることが明記されました。このパラメータにより、全体のドキュメントの数が分かるが、インデックスが安定している場合のみ正確であることに言及されています。

加えて、REST APIの呼び出しに関する新たな情報が追加され、GETリクエストのURLの最大長が8KBであることや、ODataフィルタを含む場合にはPOSTを使用する方が良いことが述べられています。また、部分応答を取得する場合の続行トークンの取り扱いや、同じHTTPメソッドを使用する必要があることについても詳細に説明されています。

これらの更新により、読者はAzure AI Searchでのクエリ作成のプロセスをより効果的に理解し、実行することができるようになります。

## articles/search/semantic-how-to-query-request.md{#item-85530d}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: how-to
-ms.date: 03/31/2025
+ms.date: 10/02/2025
 ---
 
 # Add semantic ranking to queries in Azure AI Search
@@ -29,7 +29,7 @@ This article explains how to invoke the semantic ranker on queries. It assumes y
 + Review [semantic ranking](semantic-search-overview.md) if you need an introduction to the feature.
 
 > [!NOTE]
-> Captions and answers are extracted verbatim from text in the search document. The semantic subsystem uses machine reading comprehension to recognize content having the characteristics of a caption or answer, but doesn't compose new sentences or phrases except in the case of [query rewrite](semantic-how-to-query-rewrite.md). For this reason, content that includes explanations or definitions work best for semantic ranking. If you want chat-style interaction with generated responses, see [Retrieval Augmented Generation (RAG)](retrieval-augmented-generation-overview.md).
+> Captions and answers are extracted verbatim from text in the search document. The semantic subsystem uses machine reading comprehension to recognize content having the characteristics of a caption or answer, but doesn't compose new sentences or phrases except in the case of [query rewrite](semantic-how-to-query-rewrite.md). For this reason, content that includes explanations or definitions work best for semantic ranking. If you want chat-style interaction with generated responses, see [Agentic retrieval](search-agentic-retrieval-concept.md) or [Retrieval Augmented Generation (RAG)](retrieval-augmented-generation-overview.md).
 
 ## Choose a client
 
@@ -52,22 +52,11 @@ A few query capabilities bypass relevance scoring, which makes them incompatible
 
 ## Set up the query
 
-By default, queries don't use semantic ranking. To use semantic ranking, two different parameters can be used. Each parameter supports a different set of scenarios.
+By default, queries don't use semantic ranking. To use semantic ranking, two different parameters can be used. Each parameter supports a different set of query formats.
 
-Semantic queries, whether specified through `search` plus `queryType`, or through `semanticQuery`, must be plain text and they can't be empty. Empty queries result in no semantic ranking being applied to the results.
+All semantic queries, whether specified through `search` plus `queryType`, or through `semanticQuery`, must be plain text and they can't be empty. As you can see from the table below, the `queryType-semantic` parameter supports a subset of query formats.
 
-<!-- 
-1. Set `queryType` to `semantic`:
-  + [Text search](search-lucene-query-architecture.md) with a simple plain text query. Empty queries result in no semantic ranking being applied to the results.
-  + [Hybrid search](hybrid-search-overview.md).
-  + [Simple](query-simple-syntax.md) or [full](query-lucene-syntax.md) syntax can't be used.
-1. Specify `semanticQuery`:
-  + [Text search](search-lucene-query-architecture.md) using the [simple](query-simple-syntax.md) or [full](query-lucene-syntax.md) syntax.
-  + [Vector search](vector-search-overview.md).
-  + [Hybrid search](hybrid-search-overview.md).
-  + The query specified for `semanticQuery` must be a plain text query. Empty queries aren't supported. -->
-
-| Semantic ranker parameter | [Plain text search](search-query-create.md) | [Simple text search syntax](query-simple-syntax.md) | [Full text search syntax](query-lucene-syntax.md) | [Vector search](vector-search-how-to-query.md) | [Hybrid Search](hybrid-search-how-to-query.md) | [Semantic answers](semantic-answers.md) and captions |
+| Parameter | [Plain text search](search-query-create.md) | [Simple text search syntax](query-simple-syntax.md) | [Full text search syntax](query-lucene-syntax.md) | [Vector search](vector-search-how-to-query.md) | [Hybrid Search](hybrid-search-how-to-query.md) | [Semantic answers](semantic-answers.md) and captions |
 |-|-|-|-|-|-|-|
 | `queryType-semantic` <sup>1</sup> | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ |
 | `semanticQuery="<your plain text query>"`<sup>2</sup> | ✅ | ✅ | ✅ | ✅ |✅ | ✅ |
@@ -139,17 +128,17 @@ POST https://[search-service-name].search.windows.net/indexes/hotels-sample-inde
 }
 ```
 
-1. Set `queryType` to `semantic`.
+1. Set `queryType` to `semantic`. This improves precision of search results by reranking the top 50 matches using a ranking model trained on the Bing corpus for queries expressed in natural language as opposed to keywords. If you set the query type to semantic, you must also set semanticConfiguration. You can optionally set answers if you want to also return the top 3 answers if the query input was formulated in natural language ("what is a ...), and you can optionally set captions to extract key passages from the highest ranked documents.
 
-1. Set `search` to a simple plain text query. Since the `queryType` is set to `semantic`,  [simple syntax](query-simple-syntax.md) or [full Lucene syntax](query-lucene-syntax.md) aren't supported. Supplying `*` or an empty string results in no semantic ranking being applied to the query.
+1. Set `search` to a simple plain text query. Since the `queryType` is set to `semantic`,  [simple syntax](query-simple-syntax.md) or [full Lucene syntax](query-lucene-syntax.md) aren't supported. Supplying `*` or an empty string results in no semantic ranking being applied to the query. 
 
 1. Set `semanticConfiguration` to a [predefined semantic configuration](semantic-how-to-configure.md) that's embedded in your index.
 
-1. Set `answers` to specify whether [semantic answers](semantic-answers.md) are included in the result. Currently, the only valid value for this parameter is `extractive`. Answers can be configured to return a maximum of 10. The default is one. This example shows a count of three answers: `extractive|count-3`.
+1. Set `answers` to specify whether [semantic answers](semantic-answers.md) are included in the result. Valid values for this parameter are `extractive` and `none`. This parameter is only valid if the query type is "semantic". When set to "extractive", the query formulates and returns answers from key passages in the highest semantically ranked documents. The default is one answer, but you can specify up to 10 by adding a count. For example, `"answers": "extractive|count-3"` returns three answers. For an answer to be returned, there must be verbatim content in the targeted field that looks like an answer. The language models used for answers are trained to recognize answers, not generate them. In addition, the query itself must look like a question.
 
-   Answers aren't guaranteed on every request. To get an answer, the query must look like a question and the content must include text that looks like an answer.
+1. Set `captions` to specify whether semantic captions are included in the result. Valid values are "none" and "extractive". Defaults to "none". This parameter is only valid if the query type is "semantic". When set to "extractive", the query returns captions extracted from key passages in the highest ranked documents. 
 
-1. Set `captions` to specify whether semantic captions are included in the result. Currently, the only valid value for this parameter is `extractive`. Captions can be configured to return results with or without highlights. The default is for highlights to be returned. This example returns captions without highlights: `extractive|highlight-false`.
+   When captions is set to 'extractive', highlighting is enabled by default, and can be configured by appending the pipe character '|' followed by the `highlight-<true/false>` option, such as `extractive|highlight-true`. This example returns captions without highlights: `extractive|highlight-false`.
 
    The basis for captions and answers are the fields referenced in the "semanticConfiguration". These fields are under a combined limit in the range of 2,000 tokens or approximately 20,000 characters. If you anticipate a token count exceeding this limit, consider a [data chunking step](vector-search-how-to-chunk-documents.md) using the [Text split skill](cognitive-search-skill-textsplit.md). This approach introduces a dependency on an [AI enrichment pipeline](cognitive-search-concept-intro.md) and [indexers](search-indexer-overview.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティッククエリリクエストのガイドを更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるセマンティッククエリリクエストに関する記事を更新し、新しい情報や手順の明確化を行ったものです。主な修正内容には、日付の更新と、セマンティックランキングに関する機能の詳細が含まれています。

具体的には、セマンティックランキングを使用する際に必要なパラメータの説明が強化され、各パラメータがどのようなクエリ形式をサポートするかが詳述されています。また、引き続きセマンティックな回答を得るための設定方法についても更新され、適切な質問形式のクエリが必要であることが強調されています。

さらに、セマンティックキャプションのオプションが追加され、これを利用することで最もランク付けされたドキュメントから抽出されたキャプションを取得できるようになります。これにより、クエリ結果の精度が向上し、ユーザーが欲しい情報にアクセスしやすくなります。また、キャプションのハイライトオプションについても明確にされており、ユーザーが期待する結果を得られるよう配慮されています。

これらの更新により、読者はAzure AI Searchにおけるセマンティックランキングの利用法をより良く理解できるようになり、具体的な実装に役立つ情報を得ることができます。


