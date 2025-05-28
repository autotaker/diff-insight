---
date: '2025-05-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a7ab2bd...MicrosoftDocs:4f76879
summary: このコード差分では、ドキュメントとコードの両方において小さな修正とアップデートが行われました。主な内容としては、スペルミスの修正、新しい画像の追加、Search
  Explorerに関するチュートリアルの大幅な更新が含まれており、全体的なユーザー体験の向上を目指しています。特に、視覚的情報の強化がユーザーの理解を助ける役割を果たしています。また、破壊的な変更はなく、ドキュメントの正確性が改善され、より使いやすいリソースへと進化しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a7ab2bd...MicrosoftDocs:4f76879){target="_blank"}

<format>
# Highlights
このコード差分では、ドキュメントとコードの両方における小さな修正とアップデートが行われました。特に、スペルミスの修正や画像の更新、さらには関数内の変数名の修正が含まれています。また、新しい画像の追加やSearch Explorerにおけるチュートリアルの大幅な更新が行われ、全体的なユーザー体験を向上させるための措置が取られています。

## New features
- Search Explorerに関する新しい画像が追加され、ユーザーの理解を助ける視覚的情報が強化されました。

## Breaking changes
大きな破壊的な変更はありません。

## Other updates
- `full-text-javascript.md`と`full-text-typescript.md`のスペルミスが修正され、ドキュメントの正確性が改善されました。
- `edit-index-json.png`画像の更新による品質向上。
- `search-agentic-retrieval-how-to-pipeline.md`内でコードの変数名が改善されました。
- `search-explorer.md`の詳細なアップデートにより、Search Explorerの使用がより直感的になりました。
- `search-howto-index-sharepoint-online.md`では、SharePoint Onlineのインデックス作成に関連する情報が詳細に説明され、ベストプラクティスが強調されました。
- `search-howto-reindex.md`でインデックスの説明に関する修正が行われ、REST APIの更新内容が反映されました。

# Insights
このコード差分は、ドキュメントの質を向上させ、ユーザーの理解を深めることを目的とした一連のマイナーチェンジを含んでいます。特に、スペルや文法の修正は、ドキュメントが正確であり、プロフェッショナルな印象を与えることに寄与しています。

また、画像の追加と改良は、難解な内容を視覚的にサポートすることによって、ユーザーがコンセプトをより容易に理解できるようにしています。これは特に、視覚的フィードバックが重要な領域では大きな利点です。

Search ExplorerとSharePoint Onlineに関するドキュメントの更新は、最新の機能やベストプラクティスを含む詳細な情報を提供することによって、ユーザーがこれらのツールを効果的に活用できるようにしています。これらのアップデートは、Azure AI Searchの幅広いユーザーにとって、より効率的なワークフローを提案するものです。

全体として、この差分では、テキストとビジュアルの両方を通じてドキュメントの品質を高めるための多角的なアプローチが示されています。これにより、Azureドキュメントは、より包括的で理解しやすいリソースとなり、ユーザーの学習曲線を緩和する助けとなるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [full-text-javascript.md](#item-568e3a) | minor update | 文書の表記を修正しました。 | modified | 1 | 1 | 2 | 
| [full-text-typescript.md](#item-6630e8) | minor update | 文書の表記を修正しました。 | modified | 1 | 1 | 2 | 
| [three-query-views.png](#item-bf123c) | new feature | 新しい画像を追加しました。 | added | 0 | 0 | 0 | 
| [edit-index-json.png](#item-5780d0) | minor update | 画像のメタデータが更新されました。 | modified | 0 | 0 | 0 | 
| [search-agentic-retrieval-how-to-pipeline.md](#item-1ad1c3) | minor update | 関数内の変数名を修正しました。 | modified | 1 | 1 | 2 | 
| [search-explorer.md](#item-738774) | minor update | Search Explorerのチュートリアルが更新されました。 | modified | 45 | 34 | 79 | 
| [search-howto-index-sharepoint-online.md](#item-49ff6e) | minor update | SharePoint Onlineのインデックス作成に関する情報を更新しました。 | modified | 6 | 2 | 8 | 
| [search-howto-reindex.md](#item-46738a) | minor update | インデックスの説明に関する情報を修正しました。 | modified | 7 | 5 | 12 | 


# Modified Contents
## articles/search/includes/quickstarts/full-text-javascript.md{#item-568e3a}

<details>
<summary>Diff</summary>
````diff
@@ -593,7 +593,7 @@ console.log(`Index named ${index.name} has been created.`);
 
 ### Load documents 
 
-In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this case, we'll programatically push the documents to the index.
+In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this case, we'll programmatically push the documents to the index.
 
 Document inputs might be rows in a database, blobs in Blob storage, or, as in this sample, JSON documents on disk. Similar to what we did with the `indexDefinition`, we also need to import `hotels.json` at the top of *index.js* so that the data can be accessed in our main function.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書の表記を修正しました。"
}
```

### Explanation
この変更は、`full-text-javascript.md`ファイル内の1行のテキストにおける細かな修正を含んでいます。具体的には、「プログラム的に」というフレーズが「プログラムatically（programmatically）」と正しくスペル修正されました。この修正は、文書の読みやすさ向上と内容の正確性を確保するためのものであり、全体の意味には影響を与えていません。変更された行は、Azure AI Searchにおけるドキュメントの扱いについての説明に関連しています。変更内容は、ユーザーが正確な情報を得られるようにするための調整です。

## articles/search/includes/quickstarts/full-text-typescript.md{#item-6630e8}

<details>
<summary>Diff</summary>
````diff
@@ -529,7 +529,7 @@ console.log(`Index named ${index.name} has been created.`);
 
 ### Load documents 
 
-In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this case, we'll programatically push the documents to the index.
+In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this case, we'll programmatically push the documents to the index.
 
 Document inputs might be rows in a database, blobs in Blob storage, or, as in this sample, JSON documents on disk. You can either download [hotels.json](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels.json) or create your own *hotels.json* file with the following content:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書の表記を修正しました。"
}
```

### Explanation
この変更は、`full-text-typescript.md`ファイル内のテキストに対する小さな修正を示しています。具体的には、「プログラム的に」という表現が「プログラムatically（programmatically）」と正しくスペル修正され、ドキュメントの正確性を向上させました。この修正は、Azure AI Searchにおけるドキュメントの処理に関する説明の文脈では、ユーザーが正確に理解できることを助けるためのものです。全体として、変更は内容の意味を保持しつつ、表記の適正さを確保する意図があります。

## articles/search/media/search-explorer/three-query-views.png{#item-bf123c}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像を追加しました。"
}
```

### Explanation
この変更は、`three-query-views.png`という新しい画像が`articles/search/media/search-explorer/`ディレクトリに追加されたことを示しています。この画像は、検索エクスプローラーに関するビジュアルを提供し、ユーザーが異なるクエリビューを理解する助けとなる可能性があります。画像の追加は、ドキュメントに視覚的な情報を提供し、説明事項を補完することで、全体のユーザーエクスペリエンスを向上させることを目的としています。画像は、GitHubのリポジトリ内でアクセス可能であり、関連する内容をより明確に理解するための役割を果たします。

## articles/search/media/search-how-to-index/edit-index-json.png{#item-5780d0}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像のメタデータが更新されました。"
}
```

### Explanation
この変更は、`edit-index-json.png`という画像が`articles/search/media/search-how-to-index/`ディレクトリ内で更新されたことを示しています。具体的な内容に関する変更は示されていませんが、画像の更新は、照明の向上や内容の一貫性を保つことを目的としている可能性があります。これは、ドキュメントの理解を助けるために必要であり、ユーザーに最新の情報を提供することに寄与します。画像は、GitHubリポジトリ内でアクセス可能であり、関連するトピックに対する理解を深めるための視覚的サポートとして役立ちます。

## articles/search/search-agentic-retrieval-how-to-pipeline.md{#item-1ad1c3}

<details>
<summary>Diff</summary>
````diff
@@ -202,7 +202,7 @@ def agentic_retrieval() -> str:
     messages = project_client.agents.list_messages(thread.id, limit=5, order=ListSortOrder.DESCENDING)
     # Reverse the order so the most recent message is last
     messages.data.reverse()
-    retrieval_result = agent_client.knowledge_retrieval.retrieve(
+    retrieval_result = retrieval_result = agent_client.retrieve(
         retrieval_request=KnowledgeAgentRetrievalRequest(
             messages=[KnowledgeAgentMessage(role=msg["role"], content=[KnowledgeAgentMessageTextContent(text=msg.content[0].text)]) for msg in messages.data],
             target_index_params=[KnowledgeAgentIndexParams(index_name=index_name, reranker_threshold=2.5)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "関数内の変数名を修正しました。"
}
```

### Explanation
この変更は、`search-agentic-retrieval-how-to-pipeline.md`というファイルにおいて、コード内の関数`agentic_retrieval`に関する部分が修正されたことを示しています。具体的には、`retrieval_result`という変数名が修正され、新しい名前の代わりに元の変数名を使用する形に変更されました。この変更により、コードの読みやすさや一貫性が向上することを目的としています。ファイルはGitHubリポジトリ内で確認可能で、修正内容によって関数の動作や理解がより明確になることを意図しています。

## articles/search/search-explorer.md{#item-738774}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 03/04/2025
+ms.date: 05/22/2025
 ms.custom:
   - mode-ui
 ---
@@ -18,9 +18,6 @@ In this quickstart, you learn how to use **Search explorer**, a built-in query t
 
 This quickstart uses an existing index to demonstrate Search explorer.
 
-> [!TIP]
-> Search explorer now supports image search. To learn more, see [Quickstart: Image search in the Azure portal](search-get-started-portal-image-search.md).
-
 ## Prerequisites
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/).
@@ -29,40 +26,54 @@ This quickstart uses an existing index to demonstrate Search explorer.
 
 + This quickstart uses the realestate-us-sample index. To create the index, run the [**Import data wizard**](search-import-data-portal.md), select the built-in sample data, and step through the wizard using all the default values.
 
-  :::image type="content" source="media/search-explorer/search-explorer-sample-data.png" alt-text="Screenshot of the sample data sets available in the Import data wizard." border="true":::  
+  :::image type="content" source="media/search-explorer/search-explorer-sample-data.png" alt-text="Screenshot of the sample data sets available in the Import data wizard." border="true" lightbox="media/search-explorer/search-explorer-sample-data.png":::
 
 ## Start Search explorer
 
-1. In the [Azure portal](https://portal.azure.com), open the search overview page from the dashboard or [find your service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
+1. In the [Azure portal](https://portal.azure.com), find your search service and open the **Overview** page.
 
-1. Open Search explorer from the command bar:
+1. On the command bar, select **Search explorer**:
 
    :::image type="content" source="media/search-explorer/search-explorer-cmd2.png" alt-text="Screenshot of the Search explorer command in portal." border="true":::
 
-    Or use the embedded **Search explorer** tab on an open index:
+   Alternatively, select the **Search explorer** tab on an open index.
+
+   :::image type="content" source="media/search-explorer/search-explorer-tab.png" alt-text="Screenshot of the Search explorer tab." border="true" lightbox="media/search-explorer/search-explorer-tab.png":::
 
-   :::image type="content" source="media/search-explorer/search-explorer-tab.png" alt-text="Screenshot of the Search explorer tab." border="true":::
+## Query three ways
 
-## Query two ways
+There are three approaches to querying in Search explorer:
 
-There are two approaches for querying in Search explorer. 
++ Query view provides a default search bar. It accepts an empty query or free-text query with Booleans, such as `seattle condo + parking`.
 
-+ Query view provides a default search bar. It accepts an empty query or free text query with booleans. For example, `seattle condo +parking`.
++ Image view provides a window to browse or drag and drop PNG, JPG, or JPEG files. Unless your index has an [image vectorizer and an equivalent skill](vector-search-how-to-configure-vectorizer.md#supported-embedding-models), this view is unavailable.
 
 + JSON view supports parameterized queries. Filters, orderby, select, count, searchFields, and all other parameters must be set in JSON view.
 
-  > [!TIP]
-  > JSON view provides intellisense for parameter name completion. Place your cursor inside the JSON view and type a space character to see a list of all query parameters. You can also type a letter, like "s," to see only the query parameters that begin with that letter. Intellisense doesn't exclude invalid parameters, so use your best judgment.
+   :::image type="content" source="media/search-explorer/three-query-views.png" alt-text="Screenshot of the three views for querying in Search explorer." border="true" lightbox="media/search-explorer/three-query-views.png":::
+
+## Example: Image query
+
+Search explorer accepts images as query inputs through **Image view**, which requires that you use a supported vectorizer–skill pair. For more information, see [Configure a vectorizer in a search index](vector-search-how-to-configure-vectorizer.md).
+
+The realestate-us-sample index isn't configured for image vectorization. If you want to run image queries, create an index as described in [Quickstart: Vector search in the Azure portal](search-get-started-portal-import-vectors.md). The quickstart relies on text-based sample data, so you must use documents that contain images.
 
-  Switch to **JSON view** for parameterized queries. The examples in this article assume JSON view throughout. You can paste JSON examples from this article into the text area.
+To run an image query, select or drag an image to the search area, and then select **Search**. Search explorer vectorizes the image and sends the vector to the search engine for query execution. The search engine returns documents that are sufficiently similar to the input image, up to the specified `k` number of results. <!-- This is enabled by [vector search](vector-search-overview.md), which matches documents based on the similarity of their vector representations. -->
 
-   :::image type="content" source="media/search-explorer/search-explorer-json-view.png" alt-text="Screenshot of the JSON view selector." border="true":::
+:::image type="content" source="media/search-get-started-portal-images/image-search.png" alt-text="Screenshot of search results for image search." border="true" lightbox="media/search-get-started-portal-images/image-search.png":::
 
-## Run an unspecified query
+## Examples: JSON queries
+
+The following are examples of JSON queries you can run using Search explorer. To follow these examples, switch to **JSON view**. You can paste each JSON example into the text area.
+
+> [!TIP]
+> The JSON view provides intellisense for parameter name completion. Place your cursor inside the JSON view and type a space character to see all query parameters. You can also type a letter, like "s," to see only the query parameters that begin with that letter. Intellisense doesn't exclude invalid parameters, so use your best judgment.
+
+### Run an unspecified query
 
 In Search explorer, POST requests are formulated internally using the [Search POST REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true), with responses returned as verbose JSON documents.
 
-For a first look at content, execute an empty search by clicking **Search** with no terms provided. An empty search is useful as a first query because it returns entire documents so that you can review document composition. On an empty search, there's no search score and documents are returned in arbitrary order (`"@search.score": 1` for all documents). By default, 50 documents are returned in a search request.
+For a first look at content, execute an empty search by selecting **Search** with no terms provided. An empty search is useful as a first query because it returns entire documents so that you can review document composition. On an empty search, there's no search score and documents are returned in arbitrary order (`"@search.score": 1` for all documents). By default, 50 documents are returned in a search request.
 
 Equivalent syntax for an empty search is `*` or `"search": "*"`.
 
@@ -75,11 +86,11 @@ Equivalent syntax for an empty search is `*` or `"search": "*"`.
 
    **Results**
    
-   :::image type="content" source="media/search-explorer/search-explorer-example-empty.png" alt-text="Unqualified or empty query example" border="true":::
+   :::image type="content" source="media/search-explorer/search-explorer-example-empty.png" alt-text="Screenshot of unqualified or empty query example." border="true" lightbox="media/search-explorer/search-explorer-example-empty.png":::
 
-## Free text search
+### Run a free-text query
 
-Free-form queries, with or without operators, are useful for simulating user-defined queries sent from a custom app to Azure AI Search. Only those fields attributed as "searchable" in the index definition are scanned for matches. 
+Free-form search, with or without operators, is useful for simulating user-defined queries sent from a custom app to Azure AI Search. Only those fields attributed as "searchable" in the index definition are scanned for matches.
 
 You don't need JSON view for a free text query, but we provide it in JSON for consistency with other examples in this article.
 
@@ -95,9 +106,9 @@ Notice that when you provide search criteria, such as query terms or expressions
 
    You can use Ctrl-F to search within results for specific terms of interest.
 
-   :::image type="content" source="media/search-explorer/search-explorer-example-freetext.png" alt-text="Screenshot of a free text query example." border="true":::
+   :::image type="content" source="media/search-explorer/search-explorer-example-freetext.png" alt-text="Screenshot of a free text query example." border="true" lightbox="media/search-explorer/search-explorer-example-freetext.png":::
 
-## Count of matching documents 
+### Count matching documents
 
 Add `"count": true` to get the number of matches found in an index. On an empty search, count is the total number of documents in the index. On a qualified search, it's the number of documents matching the query input. Recall that the service returns the top 50 matches by default, so the count might indicate more matches in the index than what's returned in the results.
 
@@ -110,9 +121,9 @@ Add `"count": true` to get the number of matches found in an index. On an empty
 
    **Results**
 
-   :::image type="content" source="media/search-explorer/search-explorer-example-count.png" alt-text="Screenshot of a count example." border="true":::
+   :::image type="content" source="media/search-explorer/search-explorer-example-count.png" alt-text="Screenshot of a count example." border="true" lightbox="media/search-explorer/search-explorer-example-count.png":::
 
-## Limit fields in search results
+### Limit fields in search results
 
 Add ["select"`](search-query-odata-select.md) to limit results to the explicitly named fields for more readable output in **Search explorer**. Only fields marked as "retrievable" in the search index can show up in results.
 
@@ -126,11 +137,11 @@ Add ["select"`](search-query-odata-select.md) to limit results to the explicitly
 
    **Results**
 
-   :::image type="content" source="media/search-explorer/search-explorer-example-selectfield.png" alt-text="Screenshot of restrict fields in search results example." border="true":::
+   :::image type="content" source="media/search-explorer/search-explorer-example-selectfield.png" alt-text="Screenshot of restrict fields in search results example." border="true" lightbox="media/search-explorer/search-explorer-example-selectfield.png":::
 
-## Return next batch of results
+### Return next batch of results
 
-Azure AI Search returns the top 50 matches based on the search rank. To get the next set of matching documents, append `"top": 100` and `"skip": 50` to increase the result set to 100 documents (default is 50, maximum is 1000), skipping the first 50 documents. You can check the document key (listingID) to identify a document. 
+Azure AI Search returns the top 50 matches based on the search rank. To get the next set of matching documents, append `"top": 100` and `"skip": 50` to increase the result set to 100 documents (default is 50, maximum is 1000), skipping the first 50 documents. You can check the document key (listingID) to identify a document.
 
 Recall that you need to provide search criteria, such as a query term or expression, to get ranked results. Notice that search scores decrease the deeper you reach into search results.
 
@@ -146,9 +157,9 @@ Recall that you need to provide search criteria, such as a query term or express
 
    **Results**
 
-   :::image type="content" source="media/search-explorer/search-explorer-example-topskip.png" alt-text="Screenshot of returning next batch of search results example." border="true":::
+   :::image type="content" source="media/search-explorer/search-explorer-example-topskip.png" alt-text="Screenshot of returning next batch of search results example." border="true" lightbox="media/search-explorer/search-explorer-example-topskip.png":::
 
-## Filter expressions (greater than, less than, equal to)
+### Filter expressions (greater than, less than, equal to)
 
 Use the [`filter`](search-query-odata-filter.md) parameter to specify inclusion or exclusion criteria. The field must be attributed as "filterable" in the index. This example searches for bedrooms greater than 3:
 
@@ -163,9 +174,9 @@ Use the [`filter`](search-query-odata-filter.md) parameter to specify inclusion
    
    **Results**
 
-   :::image type="content" source="media/search-explorer/search-explorer-example-filter.png" alt-text="Screenshot of a filter example." border="true":::
+   :::image type="content" source="media/search-explorer/search-explorer-example-filter.png" alt-text="Screenshot of a filter example." border="true" lightbox="media/search-explorer/search-explorer-example-filter.png":::
 
-## Sorting results
+### Sort results
 
 Add [`orderby`](search-query-odata-orderby.md) to sort results by another field besides search score. The field must be attributed as "sortable" in the index. In situations where the filtered value is identical (for example, same price), the order is arbitrary, but you can add more criteria for deeper sorting. An example expression you can use to test this out is:
 
@@ -178,10 +189,10 @@ Add [`orderby`](search-query-odata-orderby.md) to sort results by another field
        "orderby": "price asc"
    }
    ```
-   
+
    **Results**
 
-   :::image type="content" source="media/search-explorer/search-explorer-example-orderby.png" alt-text="Screenshot of a sorting example." border="true":::
+   :::image type="content" source="media/search-explorer/search-explorer-example-orderby.png" alt-text="Screenshot of a sorting example." border="true" lightbox="media/search-explorer/search-explorer-example-orderby.png":::
 
 ## Takeaways
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Search Explorerのチュートリアルが更新されました。"
}
```

### Explanation
この変更は、`search-explorer.md`ファイルにおける内容の大幅な更新を示しています。主に、Search Explorer使用に関する手順や情報が加えられ、使い方が改善されています。具体的には、日付の更新、クイックスタートガイドに画像検索のサポートを追加したこと、そしてより明確な手順を示すために複数の新しいセクションが組み込まれています。

例えば、検索の方法として「クエリの三つの方法」が追加され、直感的な操作方法について詳しく説明されています。また、各種クエリの実行例が示されることで、ユーザーがSearch Explorerを使いやすくなるよう工夫されています。さらに、画像やサンプルデータの表示に関する部分が強化され、全体的にドキュメントがより親しみやすくなっています。変更の詳細はGitHubリポジトリ内で確認できます。

## articles/search/search-howto-index-sharepoint-online.md{#item-49ff6e}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 02/24/2025
+ms.date: 05/26/2025
 ---
 
 # Index data from SharePoint document libraries
@@ -70,7 +70,10 @@ Here are the considerations when using this feature:
 
 + If you need to create a custom Copilot / RAG (Retrieval Augmented Generation) application to chat with SharePoint data, the recommended approach is to use [Microsoft Copilot Studio](https://www.microsoft.com/microsoft-copilot/microsoft-copilot-studio) instead of this preview feature. 
 
-+ If you need a SharePoint content indexing solution in a production environment, consider creating a custom connector with [SharePoint Webhooks](/sharepoint/dev/apis/webhooks/overview-sharepoint-webhooks), calling [Microsoft Graph API](/graph/use-the-api) to export the data to an Azure Blob container, and then use the [Azure blob indexer](search-howto-indexing-azure-blob-storage.md) for incremental indexing.
++ If you still need a custom SharePoint Online content indexing solution using Azure AI Search in a production environment, despite the recommendation to use Microsoft Copilot Studio, consider:
+  - Creating a custom connector with [SharePoint Webhooks](/sharepoint/dev/apis/webhooks/overview-sharepoint-webhooks), calling [Microsoft Graph API](/graph/use-the-api) to export the data to an Azure Blob container, and then use the [Azure blob indexer](search-howto-indexing-azure-blob-storage.md) for incremental indexing.
+  - Creating your own [Azure Logic Apps workflow](/azure/logic-apps/logic-apps-overview) using [Azure Logic Apps SharePoint connector](/connectors/sharepointonline/) and [Azure AI Search connector](/connectors/azureaisearch/) when reaching General Availability. You can use the workflow generated by the [Azure portal wizard](search-how-to-index-logic-apps-indexers.md) as a starting point and then customize it in the [Azure Logic Apps designer](/azure/logic-apps/quickstart-create-example-consumption-workflow#add-the-trigger) to include the transformation steps you need. The Azure Logic App workflow created when using the [Azure AI Search wizard](search-how-to-index-logic-apps-indexers.md) to index SharePoint Online data is a [consumption workflow](/azure/logic-apps/logic-apps-overview#key-terms). If you're setting up production workloads, make sure to switch to a [standard logic app workflow](/azure/logic-apps/logic-apps-overview#key-terms) and take advantage of its additional enterprise features.
+  - Regardless of the approach you choose, whether building a custom connector with SharePoint hooks or creating an Azure Logic Apps workflow, it's key to implement robust security measures. These measures include configuring shared private links, setting up firewalls, preserving user permissions from the source and honor at query time, among others. You should also regularly audit and monitor your pipeline.
 
 <!-- + There could be Microsoft 365 processes that update SharePoint file system-metadata (based on different configurations in SharePoint) and will cause the SharePoint Online indexer to trigger. Make sure that you test your setup and understand the document processing count prior to using any AI enrichment. Since this is a third-party connector to Azure (SharePoint is located in Microsoft 365), SharePoint configuration is not checked by the indexer. -->
 
@@ -499,3 +502,4 @@ The error message will also include the SharePoint site ID, drive ID, and drive
 
 + [Indexers in Azure AI Search](search-indexer-overview.md)
 + [Content metadata properties used in Azure AI Search](search-blob-metadata-properties.md)
++ [Index SharePoint Online content and other sources in Azure AI Search using Azure Logic App connectors](search-how-to-index-logic-apps-indexers.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint Onlineのインデックス作成に関する情報を更新しました。"
}
```

### Explanation
この変更は、`search-howto-index-sharepoint-online.md`ファイルにおいて、SharePoint Onlineのコンテンツインデックス作成に関する情報が更新されたことを示しています。主な変更点は、日付の更新と一部の段落の詳細な追加です。

具体的には、Microsoft Copilot Studioを使用したカスタムアプリケーションの作成に関する推奨が強調され、代替策としてのカスタムコネクタやAzure Logic Appsワークフローの作成について具体的な手順が詳述されています。また、選択したアプローチにかかわらず、堅牢なセキュリティ対策を実装することの重要性についても言及されています。これにより、ユーザーはSharePoint Onlineデータに対してのインデクシングのベストプラクティスやセキュリティ対策を十分に理解し、実行できるようになります。

さらに、関連する資料へのリンクが追加され、情報がより包括的に提供されるようになっています。変更の詳細はGitHubリポジトリで確認できます。

## articles/search/search-howto-reindex.md{#item-46738a}

<details>
<summary>Diff</summary>
````diff
@@ -256,7 +256,7 @@ To minimize disruption to application code, consider [creating an index alias](s
 
 ## Add an index description (preview)
 
-Beginning with REST API version 2025-05-01-preview, an `indexdescription` is now supported. This human-readable text is invaluable when a system must access several indexes and make a decision based on the description. Consider a Model Context Protocol (MCP) server that must pick the correct index at run time. The decision can be  based on the description rather than on the index name alone.
+Beginning with REST API version 2025-05-01-preview, a `ddescription` is now supported. This human-readable text is invaluable when a system must access several indexes and make a decision based on the description. Consider a Model Context Protocol (MCP) server that must pick the correct index at run time. The decision can be  based on the description rather than on the index name alone.
 
 An index description is a schema update, and you can add it without having to rebuild the entire index.
 
@@ -275,7 +275,7 @@ The Azure portal supports the latest preview API.
 
 1. Select **Edit JSON**.
 
-1. Insert `"indexDescription"`, followed by the description.
+1. Insert `"description"`, followed by the description. The value must be less than 4,000 characters and in Unicode.
 
    :::image type="content" source="media/search-how-to-index/edit-index-json.png" alt-text="Screenshot of the JSON definition of an index in the Azure portal.":::
 
@@ -285,11 +285,13 @@ The Azure portal supports the latest preview API.
 
 1. [GET an index definition](/rest/api/searchservice/indexes/get).
 
-1. Copy the JSON.
+1. Copy the JSON so that you can use it as the basis of a new request.
 
-1. [Formulate an index update PUT request](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) using the preview API, providing the *full* JSON of the existing schema, plus the new description field.
+1. [Formulate an index update using a PUT request](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) and the preview API.
 
-1. To confirm the description, issue another [GET using the 2025-05-01-preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
+1. Provide the *full* JSON of the existing schema, plus the new `description` field. The field must be a top-level field, on the same level as `name` or `fields`. The value must be less than 4,000 characters and in Unicode.
+
+1. To confirm the change, issue another [GET using the 2025-05-01-preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスの説明に関する情報を修正しました。"
}
```

### Explanation
この変更は、`search-howto-reindex.md`ファイルにおけるインデックスの説明に関する情報の修正を示しています。主に、インデックスの説明を追加する機能に関連した細部が改善され、構文上のミスが修正されています。

具体的には、2025-05-01-previewバージョンのREST APIにおいて、`indexdescription`フィールドが`description`に修正され、説明文の文字数やUnicodeの要件に関する説明が明確になりました。インデックスの更新手順も更新され、より具体的な指示が提供されています。これにより、ユーザーは新しいフィールドをインデックススキーマに追加する際の具体的な手順をより理解しやすくなります。

変更の詳細はGitHubリポジトリ内で確認できます。


