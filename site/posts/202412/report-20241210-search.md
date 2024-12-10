---
date: '2024-12-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d135a3a...MicrosoftDocs:e69b8c6
summary: このコードの変更は、検索サービスに関するドキュメントの更新に焦点を当てており、特に制限やクォータ、検索結果の構成に関する情報が見直されています。具体的には、表現の自然化や情報の明確化が行われ、ペイロード制限やAPIリクエストの詳細が加わったことで、ユーザーの理解を促進しています。新たな検索ユニット提案の表現や検索結果のカスタマイズに関する説明が強化され、日付の修正やドキュメントタイトルの微調整も実施されました。ブレイキングチェンジは特にないものの、表現の修正が理解に影響を及ぼす可能性があるため、新しいドキュメントの確認が推奨されます。整体として、これらの変更はサービスの利用しやすさと効率を向上させることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d135a3a...MicrosoftDocs:e69b8c6){target="_blank"}

<format>
# ハイライト
このコードの変更は、検索サービスの制限とクォータ、並びに検索結果の構成に関するドキュメントの更新を中心としています。新たに日付の修正や、表現の自然化、情報の明確化が行われました。特にペイロード制限とAPIリクエストの詳細な説明が加わり、ユーザーの理解を助けるような内容になっています。

## 新機能
- 追加の検索ユニットを提案する表現が自然な言い回しに修正されました。
- 検索結果の構成に関する説明が詳細化され、カスタマイズ性に関する情報が充実しました。

## ブレイキングチェンジ
- 特にブレイキングチェンジは見られませんが、表現の修正が利用者の理解に影響を与え得るため、新しいドキュメントを確認することが推奨されます。

## その他の更新
- 特定の日付が「12/05/2024」から「12/09/2024」に、別のドキュメントでは「06/12/2024」から「12/09/2024」に変更されました。
- ドキュメントタイトルの微調整が行われています。
- ペイロード制限やAPIリクエスト制限に関する説明が改善され、ステートメントがよりクリアに整理されました。

# インサイト
今回のドキュメントの更新は、検索機能に関する制限や利用方法を直感的に理解できるよう改善を図っています。検索サービスは、ユーザーが大量のデータを扱う際に重要なツールであり、そのクォータや制限は性能と安定性を維持するために不可欠です。具体的な改善点として、ペイロード制限の説明があり、これはサービスの安定性に直接影響を与えるため重要です。

また、検索結果の構成に関する情報の充実は、ユーザーが目的に応じて検索結果を最適化しやすくするため、有用です。ページネーションやハイライト設定の詳細な説明が追加され、開発者はこれを利用してよりユーザーに適した検索結果を提供できるでしょう。

これらの変更は、単なるマイナーバージョンアップの範疇に留まらず、サービス全体の利用しやすさと効率を高めるものであると言えます。ユーザー目線でドキュメントが再構成され、情報検索や実行がさらに快適になります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索サービスの制限とクォータに関するドキュメントの更新 | modified | 10 | 4 | 14 | 
| [search-pagination-page-layout.md](#item-115902) | minor update | 検索結果の構成に関するドキュメントの更新 | modified | 90 | 44 | 134 | 


# Modified Contents
## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 12/05/2024
+ms.date: 12/09/2024
 ms.custom:
   - references_regions
   - build-2024
@@ -204,7 +204,7 @@ Static rate request limits for operations related to a service:
 
 Total semantic ranker queries per second varies based on the following factors:
 + The SKU of the search service. Both queue capacity and concurrent request limits vary by SKU.
-+ The number of search units in the search service. The simplest way to increase the maximum number of concurrent semantic ranker queries is to [add additional search units to your search service](search-capacity-planning.md#how-to-change-capacity).
++ The number of search units in the search service. The simplest way to increase the maximum number of concurrent semantic ranker queries is to [add more search units to your search service](search-capacity-planning.md#how-to-change-capacity).
 + The total available semantic ranker capacity in the region.
 + The amount of time it takes to serve a query using semantic ranker. This varies based on how busy the search service is.
 
@@ -217,13 +217,17 @@ The following table describes the semantic ranker throttling limits by SKU. Subj
 
 ## API request limits
 
-Limits on payloads and queries exist because unbounded queries can destabilize your search service. Typically, such queries are created programmatically. If your application generates search queries programmatically, we recommend designing it in such a way that it doesn't generate queries of unbounded size. If you must exeed a supported limit, you should [test your workload](search-performance-analysis.md#develop-baseline-numbers) so that you know what to expect.
+Limits on queries exist because unbounded queries can destabilize your search service. Typically, such queries are created programmatically. If your application generates search queries programmatically, we recommend designing it in such a way that it doesn't generate queries of unbounded size.
+
+Limits on payloads exist for similar reasons, ensuring the stability of your search service. The limit applies to the entire request, inclusive of all its components. For example, if the request batches several documents or commands, the entire request must fit within the supported limit.
+
+If you must exceed a supported limit, you should [test your workload](search-performance-analysis.md#develop-baseline-numbers) so that you know what to expect.
 
 Except where noted, the following API requests apply to all programmable interfaces, including the Azure SDKs.
 
 General:
 
-+ Supported maximum payload limit is 16 MB for indexing and query requests via REST API and SDKs.
++ Supported maximum payload limit is 16 MB for indexing and query request via REST API and SDKs.
 + Maximum 8-KB URL length (applies to REST APIs only).
 
 Indexing APIs:
@@ -247,6 +251,8 @@ Search terms:
 + Maximum 1,000 documents returned per page of search results
 + Maximum 100 suggestions returned per Suggest API request
 
+The search engine returns 50 results by default, but you can [override this parameter](search-pagination-page-layout.md#number-of-results-in-the-response) up to the maximum limit.
+
 ## API key limits
 
 API keys are used for service authentication. There are two types. Admin keys are specified in the request header and grant full read-write access to the service. Query keys are read-only, specified on the URL, and typically distributed to client applications.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスの制限とクォータに関するドキュメントの更新"
}
```

### Explanation
この変更は、検索サービスに関するドキュメント「search-limits-quotas-capacity.md」に対するマイナーバージョンアップです。主な内容として、以下の点が挙げられます：

- 2024年の日付が「12/05/2024」から「12/09/2024」に変更されました。
- 検索サービスの同時リクエスト数の最大数を増加させるための最も簡単な方法として、追加の検索ユニットを追加することを提案する表現が、より自然な言い回しに修正されました。
- クエリとペイロードに関する制限について、ペイロード制限の必要性が具体的に強調され、安定性を確保する理由が追加されました。
- APIリクエストの制限に関する記述が明確化され、ドキュメント内の情報が整理されました。

全体として、検索サービスのクォータと制限に関する情報がより直感的かつ詳細になり、利用者が理解しやすい内容になっています。

## articles/search/search-pagination-page-layout.md{#item-115902}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: How to shape search results
+title: Shape search results
 titleSuffix: Azure AI Search
-description: Define search result composition, get a document count, sort results, and add content navigation to search results in Azure AI Search.
+description: Modify search result composition, get a document count, sort results, and add content navigation to search results in Azure AI Search.
 
 manager: nitinme
 author: HeidiSteen
@@ -10,27 +10,41 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 06/12/2024
+ms.date: 12/09/2024
 ---
 
-# How to shape results in Azure AI Search
+# Shape search results or modify search results composition
 
-This article explains how to work with a query response in Azure AI Search. The structure of a response is determined by parameters in the query itself, as described in [Search Documents (REST)](/rest/api/searchservice/documents/search-post) or [SearchResults Class (Azure for .NET)](/dotnet/api/azure.search.documents.models.searchresults-1). 
+This article explains search results composition in Azure AI Search and how to work with results in your apps. Search results are returned in a query response. The structure of a response is determined by parameters in the query itself.
 
-Parameters on the query determine:
+Search results include top-level fields such as count and optional semantic ranking-related elements such as `answers`, but most of the response consists of matching documents in a values array.
 
-+ Field selection
-+ Count of matches found in the index for the query
-+ Paging
-+ Number of results in the response (up to 50, by default)
-+ Sort order
+For search results composition, parameters on the query determine:
+
++ Number of matches found in the index (`count`)
++ Number of matches returned in the response (50 by default, configurable through `top`) or per page (`skip` and `top`)
++ A search score for each result, used for ranking (`@search.score`)
++ Fields included in search results (`select`)
++ Sort logic (`orderby`)
 + Highlighting of terms within a result, matching on either the whole or partial term in the body
++ Optional elements from the semantic ranker (`answers` at the top, `captions` for each match)
+
+## Clients and APIs for defining the query response
+
+You can use the following clients to configure a query response:
+
++ [Search Explorer](search-explorer.md) in the Azure portal, using JSON view so that you can specify any supported parameter
++ [Documents - POST (REST APIs)](/rest/api/searchservice/documents/search-post)
++ [SearchClient.Search Method (Azure SDK for .NET)](/dotnet/api/azure.search.documents.searchclient.search?view=azure-dotnet&preserve-view=true)
++ [SearchClient.Search Method (Azure SDK for Python)](/python/api/azure-search-documents/azure.search.documents.searchclient?view=azure-python#azure-search-documents-searchclient-search&preserve-view=true)
++ [SearchClient.Search Method (Azure for JavaScript)](/javascript/api/@azure/search-documents/searchclient?view=azure-node-latest#@azure-search-documents-searchclient-search&preserve-view=true)
++ [SearchClient.Search Method (Azure for Java)](/java/api/com.azure.search.documents.searchclient?view=azure-java-stable#com-azure-search-documents-searchclient-search(java-lang-string)&preserve-view=true)
 
 ## Result composition
 
-Results are tabular, composed of fields of either all "retrievable" fields, or limited to just those fields specified in the **`$select`** parameters. Rows are the matching documents.
+Results are mostly tabular, composed of fields of either all `retrievable` fields, or limited to just those fields specified in the `select` parameter. Rows are the matching documents, typically ranked in order of relevance unless your query logic precludes relevance ranking.
 
-You can choose which fields are in search results. While a search document might have a large number of fields, typically only a few are needed to represent each document in results. On a query request, append `$select=<field list>` to specify which "retrievable" fields should appear in the response.
+You can choose which fields are in search results. While a search document might have a large number of fields, typically only a few are needed to represent each document in results. On a query request, append `select=<field list>` to specify which `retrievable` fields should appear in the response.
 
 Pick fields that offer contrast and differentiation among documents, providing sufficient information to invite a clickthrough response on the part of the user. On an e-commerce site, it might be a product name, description, brand, color, size, price, and rating. For the built-in hotels-sample index, it might be the "select" fields in the following example:
 
@@ -47,36 +61,68 @@ POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
 
 Occasionally, query output isn't what you're expecting to see. For example, you might find that some results appear to be duplicates, or a result that *should* appear near the top is positioned lower in the results. When query outcomes are unexpected, you can try these query modifications to see if results improve:
 
-+ Change **`searchMode=any`** (default) to **`searchMode=all`** to require matches on all criteria instead of any of the criteria. This is especially true when boolean operators are included the query.
++ Change `searchMode=any` (default) to `searchMode=all` to require matches on all criteria instead of any of the criteria. This is especially true when boolean operators are included the query.
 
 + Experiment with different lexical analyzers or custom analyzers to see if it changes the query outcome. The default analyzer breaks up hyphenated words and reduces words to root forms, which usually improves the robustness of a query response. However, if you need to preserve hyphens, or if strings include special characters, you might need to configure custom analyzers to ensure the index contains tokens in the right format. For more information, see [Partial term search and patterns with special characters (hyphens, wildcard, regex, patterns)](search-query-partial-matching.md).
 
 ## Counting matches
 
-The count parameter returns the number of documents in the index that are considered a match for the query. To return the count, add **`$count=true`** to the query request. There's no maximum value imposed by the search service. Depending on your query and the content of your documents, the count could be as high as every document in the index.
+The count parameter returns the number of documents in the index that are considered a match for the query. To return the count, add `count=true` to the query request. There's no maximum value imposed by the search service. Depending on your query and the content of your documents, the count could be as high as every document in the index.
 
 Count is accurate when the index is stable. If the system is actively adding, updating, or deleting documents, the count is approximate, excluding any documents that aren't fully indexed.
 
 Count won't be affected by routine maintenance or other workloads on the search service. However if you have multiple partitions and a single replica, you could experience short-term fluctuations in document count (several minutes) as the partitions are restarted.
 
 > [!TIP]
-> To check indexing operations, you can confirm whether the index contains the expected number of documents by adding `$count=true` on an empty search `search=*` query. The result is the full count of documents in your index.
+> To check indexing operations, you can confirm whether the index contains the expected number of documents by adding `count=true` on an empty search `search=*` query. The result is the full count of documents in your index.
 >
-> When testing query syntax, `$count=true` can quickly tell you whether your modifications are returning greater or fewer results, which can be useful feedback.
+> When testing query syntax, `count=true` can quickly tell you whether your modifications are returning greater or fewer results, which can be useful feedback.
+
+<a name="paging-results"></a>
+
+## Number of results in the response
+
+Azure AI Search uses server-side paging to prevent queries from retrieving too many documents at once. Query parameters that determine the number of results in a response are `top` and `skip`. `top` refers to the number of search results in a page. 
+
+The default page size is 50, while the maximum page size is 1,000. If you specify a value greater than 1,000 and there are more than 1,000 results found in your index, only the first 1,000 results are returned.
+
+If the number of matches exceed the page size, the response includes information to retrieve the next page of results. For example:
+
+```json
+"@odata.nextLink": "https://contoso-search-eastus.search.windows.net/indexes/realestate-us-sample-index/docs/search?api-version=2024-07-01"
+```
+
+The top 50 are determined by search score, assuming the query is full text search or semantic. Otherwise, the top 50 are an arbitrary order for exact match queries (where uniform `@search.score=1.0` indicates arbitrary ranking).
 
-## Paging results
+Set `top` to override the default of 50. In newer preview APIs, if you're using a hybrid query, you can [specify maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview) to return up to 10,000 documents.
 
-By default, the search engine returns up to the first 50 matches. The top 50 are determined by search score, assuming the query is full text search or semantic. Otherwise, the top 50 are an arbitrary order for exact match queries (where uniform "@searchScore=1.0" indicates arbitrary ranking).
+To control the paging of all documents returned in a result set, use `top` and `skip` together. This query returns the first set of 15 matching documents plus a count of total matches.
 
-The upper limit is 1,000 documents returned per page of search results, so you can set top to return up to 1000 document in the first result. In newer preview APIs, if you're using a hybrid query, you can [specify maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview) to return up to 10,000 documents.
+```http
+POST https://contoso-search-eastus.search.windows.net/indexes/realestate-us-sample-index/docs/search?api-version=2024-07-01
 
-To control the paging of all documents returned in a result set, add `$top` and `$skip` parameters to a GET request, or `top` and `skip` to a POST request. The following list explains the logic.
+{
+    "search": "condos with a view",
+    "count": true,
+    "top": 15,
+    "skip": 0
+}
+```
 
-+ Return the first set of 15 matching documents plus a count of total matches: `GET /indexes/<INDEX-NAME>/docs?search=<QUERY STRING>&$top=15&$skip=0&$count=true`
+To return the second set, skip the first 15 to get the next 15:
 
-+ Return the second set, skipping the first 15 to get the next 15: `$top=15&$skip=15`. Repeat for the third set of 15: `$top=15&$skip=30`
+```http
+POST https://contoso-search-eastus.search.windows.net/indexes/realestate-us-sample-index/docs/search?api-version=2024-07-01
+
+{
+    "search": "condos with a view",
+    "count": true,
+    "top": 15,
+    "skip": 15
+}
+```
 
-The results of paginated queries aren't guaranteed to be stable if the underlying index is changing. Paging changes the value of `$skip` for each page, but each query is independent and operates on the current view of the data as it exists in the index at query time (in other words, there's no caching or snapshot of results, such as those found in a general purpose database).
+The results of paginated queries aren't guaranteed to be stable if the underlying index is changing. Paging changes the value of `skip` for each page, but each query is independent and operates on the current view of the data as it exists in the index at query time (in other words, there's no caching or snapshot of results, such as those found in a general purpose database).
 
 Following is an example of how you might get duplicates. Assume an index with four documents:
 
@@ -105,7 +151,7 @@ Notice that document 2 is fetched twice. This is because the new document 5 has
 
 ### Paging through a large number of results
 
-Using `$top` and `$skip` allows a search query to page through 100,000 results, but what if results are larger than 100,000? To page through a response this large, use a [sort order](search-query-odata-orderby.md) and [range filter](search-query-odata-comparison-operators.md) as a workaround for `$skip`. 
+An alternative technique for paging is to use a [sort order](search-query-odata-orderby.md) and [range filter](search-query-odata-comparison-operators.md) as a workaround for `skip`.
 
 In this workaround, sort and filter are applied to a document ID field or another field that is unique for each document. The unique field must have `filterable` and `sortable` attribution in the search index.
 
@@ -143,37 +189,37 @@ In this workaround, sort and filter are applied to a document ID field or anothe
 1. Pagination ends when the query returns zero results.
 
 > [!NOTE]
-> The "filterable" and "sortable" attributes can only be enabled when a field is first added to an index, they cannot be enabled on an existing field.
+> The `filterable` and `sortable` attributes can only be enabled when a field is first added to an index, they cannot be enabled on an existing field.
 
 ## Ordering results
 
 In a full text search query, results can be ranked by:
 
 + a search score
 + a semantic reranker score
-+ a sort order on a "sortable" field
++ a sort order on a `sortable` field
 
 You can also boost any matches found in specific fields by adding a scoring profile.
 
 ### Order by search score
 
-For full text search queries, results are automatically [ranked by a search score](index-similarity-and-scoring.md), calculated based on term frequency and proximity in a document (derived from [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)), with higher scores going to documents having more or stronger matches on a search term.
+For full text search queries, results are automatically [ranked by a search score](index-similarity-and-scoring.md) using a BM25 algorithm, calculated based on term frequency, document length, and average document length.
 
-The "@search.score" range is either unbounded, or 0 up to (but not including) 1.00 on older services. 
+The `@search.score` range is either unbounded, or 0 up to (but not including) 1.00 on older services. 
 
-For either algorithm, a "@search.score" equal to 1.00 indicates an unscored or unranked result set, where the 1.0 score is uniform across all results. Unscored results occur when the query form is fuzzy search, wildcard or regex queries, or an empty search (`search=*`). If you need to impose a ranking structure over unscored results, consider an **`$orderby`** expression to achieve that objective.
+For either algorithm, a `@search.score` equal to 1.00 indicates an unscored or unranked result set, where the 1.0 score is uniform across all results. Unscored results occur when the query form is fuzzy search, wildcard or regex queries, or an empty search (`search=*`). If you need to impose a ranking structure over unscored results, consider an `orderby` expression to achieve that objective.
 
 ### Order by the semantic reranker
 
-If you're using [semantic ranker](semantic-search-overview.md), the "@search.rerankerScore" determines the sort order of your results. 
+If you're using [semantic ranker](semantic-search-overview.md), the `@search.rerankerScore` determines the sort order of your results.
 
-The "@search.rerankerScore" range is 1 to 4.00, where a higher score indicates a stronger semantic match.
+The `@search.rerankerScore` range is 1 to 4.00, where a higher score indicates a stronger semantic match.
 
-### Order with $orderby
+### Order with orderby
 
-If consistent ordering is an application requirement, you can define an [**`$orderby`** expression](query-odata-filter-orderby-syntax.md) on a field. Only fields that are indexed as "sortable" can be used to order results.
+If consistent ordering is an application requirement, you can define an [`orderby` expression](query-odata-filter-orderby-syntax.md) on a field. Only fields that are indexed as "sortable" can be used to order results.
 
-Fields commonly used in an **`$orderby`** include rating, date, and location. Filtering by location requires that the filter expression calls the [**`geo.distance()` function**](search-query-odata-geo-spatial-functions.md?#order-by-examples), in addition to the field name.
+Fields commonly used in an `orderby` include rating, date, and location. Filtering by location requires that the filter expression calls the [`geo.distance()` function](search-query-odata-geo-spatial-functions.md?#order-by-examples), in addition to the field name.
 
 Numeric fields (`Edm.Double`, `Edm.Int32`, `Edm.Int64`) are sorted in numeric order (for example, 1, 2, 10, 11, 20).
 
@@ -200,11 +246,11 @@ Hit highlighting instructions are provided on the [query request](/rest/api/sear
 ### Requirements for hit highlighting
 
 + Fields must be `Edm.String` or `Collection(Edm.String)`
-+ Fields must be attributed at **searchable**
++ Fields must be attributed at `searchable`
 
 ### Specify highlighting in the request
 
-To return highlighted terms, include the "highlight" parameter in the query request. The parameter is set to a comma-delimited list of fields. 
+To return highlighted terms, include the highlight parameter in the query request. The parameter is set to a comma-delimited list of fields. 
 
 By default, the format mark up is `<em>`, but you can override the tag using `highlightPreTag` and `highlightPostTag` parameters. Your client code handles the response (for example, applying a bold font or a yellow background).
 
@@ -218,19 +264,19 @@ POST /indexes/good-books/docs/search?api-version=2024-07-01
     }
 ```
 
-By default, Azure AI Search returns up to five highlights per field. You can adjust this number by appending a dash followed by an integer. For example, `"highlight": "description-10"` returns up to 10 highlighted terms on matching content in the "description" field.
+By default, Azure AI Search returns up to five highlights per field. You can adjust this number by appending a dash followed by an integer. For example, `"highlight": "description-10"` returns up to 10 highlighted terms on matching content in the description field.
 
 ### Highlighted results
 
-When highlighting is added to the query, the response includes an "@search.highlights" for each result so that your application code can target that structure. The list of fields specified for "highlight" are included in the response.
+When highlighting is added to the query, the response includes an `@search.highlights` for each result so that your application code can target that structure. The list of fields specified for "highlight" are included in the response.
 
 In a keyword search, each term is scanned for independently. A query for "divine secrets" returns matches on any document containing either term.
 
 :::image type="content" source="media/search-pagination-page-layout/highlighting-example.png" alt-text="Screenshot of highlighting over a phrase query." border="true":::
 
 ### Keyword search highlighting 
 
-Within a highlighted field, formatting is applied to whole terms. For example, on a match against "The Divine Secrets of the Ya-Ya Sisterhood", formatting is applied to each term separately, even though they're consecutive. 
+Within a highlighted field, formatting is applied to whole terms. For example, on a match against "The Divine Secrets of the Ya-Ya Sisterhood", formatting is applied to each term separately, even though they're consecutive.
 
 ```json
 "@odata.count": 39,
@@ -293,7 +339,7 @@ POST /indexes/good-books/docs/search?api-version=2024-07-01
     }
 ```
 
-Because the criteria now have both terms, only one match is found in the search index. The response to the above query looks like this:
+Because the criteria now have both terms, only one match is found in the search index. The response to the previous query looks like this:
 
 ```json
 {
@@ -326,7 +372,7 @@ For the following examples, assume a query string that includes the quote-enclos
      ]
   ```
 
-For search services created after July 2020, only phrases that match the full phrase query will be returned in "@search.highlights":
+For search services created after July 2020, only phrases that match the full phrase query are returned in `@search.highlights`:
 
   ```json
   "@search.highlights": {
@@ -339,8 +385,8 @@ For search services created after July 2020, only phrases that match the full ph
 
 To quickly generate a search page for your client, consider these options:
 
-+ [Create demo app](search-create-app-portal.md), in the Azure portal, creates an HTML page with a search bar, faceted navigation, and results area that includes images.
++ [Create demo app](search-create-app-portal.md), in the Azure portal, creates an HTML page with a search bar, faceted navigation, and a thumbnail area if you have images.
 
 + [Add search to an ASP.NET Core (MVC) app](tutorial-csharp-create-mvc-app.md) is a tutorial and code sample that builds a functional client.
 
-+ [Add search to web apps](tutorial-csharp-overview.md) is a tutorial and code sample that uses the React JavaScript libraries for the user experience. The app is deployed using Azure Static Web Apps.
++ [Add search to web apps](tutorial-csharp-overview.md) is a C# tutorial and code sample that uses the React JavaScript libraries for the user experience. The app is deployed using Azure Static Web Apps and it implements pagination.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索結果の構成に関するドキュメントの更新"
}
```

### Explanation
この変更は、検索のページネーションとレイアウトに関するドキュメント「search-pagination-page-layout.md」に対するマイナーバージョンアップです。主な変更点は以下の通りです：

- ドキュメントのタイトルが「How to shape search results」から「Shape search results」に変更され、説明が「Define search result composition, get a document count...」から「Modify search result composition, get a document count...」に更新されました。
- ドキュメントの日付が「06/12/2024」から「12/09/2024」に修正されました。
- 検索結果の構成についての説明が強化され、上位フィールドが「count」やオプションの「answers」などであることが明確化されました。
- クエリパラメータに関するセクションが詳細化され、何が応答に含まれるか、どのようにカスタマイズできるかが具体的に説明されています。
- ページネーション方法や結果の数を制御するためのパラメータが説明され、デフォルトのページサイズや最大値についても言及されています。
- ハイライト機能についての記述がさらに詳しくなり、返されるハイライトの設定やデフォルト値が明確になっています。

全体として、このドキュメントの変更は、検索結果の構成やページネーションに関する情報をより明確かつ使いやすくすることを目的とした内容の改善が図られています。


