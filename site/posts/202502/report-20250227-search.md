---
date: '2025-02-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bc33227...MicrosoftDocs:42a07e4
summary: 今回の変更は、Azure AI Searchに関連するドキュメントのマイナーなアップデートで、リンクの修正やサンプルの追加、表現の改善、情報の最新化が行われました。新たに「resumable-index-backup-restore」というPythonサンプルが追加され、APIや機能の破壊的変更はありませんでした。文言やリンク、日付の更新などが多数のドキュメントで行われ、ユーザーがより正確で最新の情報を得られることを目指しています。これにより、具体的な実装方法へアクセスしやすくなり、ユーザー体験が向上することが期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bc33227...MicrosoftDocs:42a07e4){target="_blank"}

<format>
# Highlights
今回の変更は、Azure AI Searchに関連する複数のドキュメントに対するマイナーなアップデートであり、主にリンクの修正やサンプルの追加、表現の改善、情報の最新化が行われました。

## New features
- 「resumable-index-backup-restore」という新しいPythonサンプルが追加されました。

## Breaking changes
特に大きなAPIや機能の破壊的変更は含まれていません。

## Other updates
- 多数のドキュメントで、文言の修正やリンクの更新、日付の更新といったマイナーな変更が行われました。

# Insights
今回の一連のドキュメントの更新は、Azure AI Searchのユーザーがより正確で最新の情報を得られるようにすることを目的としています。特に、リンクの修正と新しいサンプルの追加により、実際の利用者が具体的な実装手法に容易にアクセスすることが可能になりました。

一方、ドキュメントの細かい改善、例えば日付の最新化や表現の明瞭化は、ユーザーに誤解を生じさせないための重要な取り組みです。特に、技術文書においては些細な誤りも大きな混乱を招く可能性があるため、継続的なメンテナンスが求められています。

また、ドキュメントのリファレンスとしての役割を果たすために、提供される情報の正確性とアクセスのしやすさは非常に重要です。そのため、更新によってユーザー体験の向上を目的としているこのシリーズのアップデートは、Azure AI Searchの利用を促進するとともに、より効率的な利用を後押しするものであると考えられます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [resource-tools.md](#item-0c6ac1) | minor update | ドキュメントの更新: Azure AI Searchのリソースツール | modified | 2 | 2 | 4 | 
| [samples-python.md](#item-d2bf09) | minor update | Pythonサンプルの更新: Azure AI Search | modified | 2 | 1 | 3 | 
| [search-faceted-navigation.md](#item-f29d1e) | minor update | ファセットナビゲーションに関するドキュメントの更新 | modified | 20 | 28 | 48 | 
| [search-how-to-large-index.md](#item-d34e42) | minor update | Azure AI Searchにおける大規模インデックス管理の更新 | modified | 2 | 2 | 4 | 
| [search-howto-reindex.md](#item-46738a) | minor update | 再インデックスに関する文書の更新 | modified | 2 | 2 | 4 | 
| [search-reliability.md](#item-3e9b1a) | minor update | 検索の信頼性に関する文書の更新 | modified | 1 | 1 | 2 | 
| [search-sku-manage-costs.md](#item-6e0122) | minor update | コスト管理に関する検索文書の更新 | modified | 2 | 2 | 4 | 
| [search-sku-tier.md](#item-7686b8) | minor update | SKU Tierに関する文書の更新 | modified | 1 | 1 | 2 | 
| [vector-search-how-to-create-index.md](#item-97c769) | minor update | ベクトル検索のインデックス作成に関する文書の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/resource-tools.md{#item-0c6ac1}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 10/08/2024
+ms.date: 02/25/2025
 ---
 
 # Productivity tools and accelerators - Azure AI Search
@@ -20,7 +20,7 @@ Productivity tools are built by engineers at Microsoft, but aren't part of the A
 |-----------|------------ |-------------|
 | [Azure AI Search Lab](https://github.com/jelledruyts/azure-ai-search-lab) | Learning and experimentation lab to try out AI-enabled search scenarios in Azure. It provides a web application front-end which uses Azure AI Search and Azure OpenAI to execute searches with a variety of options - ranging from simple keyword search, to semantic ranking, vector and hybrid search, and using generative AI to answer search queries. | [https://github.com/jelledruyts/azure-ai-search-lab](https://github.com/jelledruyts/azure-ai-search-lab)  |
 | [Back up and Restore (C#)](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore) | Download the retrievable fields of an index to your local device and then upload the index and its content to a new search service. | [https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore) |
-| [Back up and Restore (Python)](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/index-backup-restore) | Download the retrievable fields of an index to your local device and then upload the index and its content to a new search service. | [https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/index-backup-restore](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/index-backup-restore) |
+| [Back up and Restore (Python)](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) | Download the retrievable fields of an index to your local device and then upload the index and its content to a new search service. | [https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) |
 | [Performance testing solution](https://github.com/Azure-Samples/azure-search-performance-testing/blob/main/README.md) | This solution helps you load test Azure AI Search. It uses Apache JMeter as an open source load and performance testing tool and Terraform to dynamically provision and destroy the required infrastructure on Azure. | [https://github.com/Azure-Samples/azure-search-performance-testing](https://github.com/Azure-Samples/azure-search-performance-testing) |
 | [Visual Studio Code extension](https://github.com/microsoft/vscode-azurecognitivesearch) | Although the extension is no longer available in the Visual Studio Code Marketplace, the code is open source. You can clone and modify the tool for your own use. | [https://github.com/microsoft/vscode-azurecognitivesearch](https://github.com/microsoft/vscode-azurecognitivesearch) |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントの更新: Azure AI Searchのリソースツール"
}
```

### Explanation
この変更は、Azure AI Searchに関するリソースツールの説明を含む文書に対するマイナーな更新です。具体的には、以下の内容が修正されました。

1. **日付の更新**: `ms.date`が2024年10月8日から2025年2月25日に変更されました。これにより、文書の最新性が保たれます。

2. **リソースリンクの修正**: 「Back up and Restore (Python)」のリンクが更新され、正しいディレクトリパスに導かれるようになりました。この修正により、ユーザーは有用なリソースに容易にアクセスできるようになります。

これらの変更は、ドキュメントの明確性と使用性の向上を目的としています。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -58,7 +58,8 @@ The following samples are also published by the Azure AI Search team, but aren't
 
 | Repository | Description |
 |------------|-------------|
-| [azure-search-backup-and-restore.ipynb](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/index-backup-restore) | Uses the **azure.search.documents** library in the Azure SDK for Python to make a local copy of the retrievable fields of a search index, and then push those fields to a new search index. |
+| [index-backup-and-restore.ipynb](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) | Uses the **azure.search.documents** library in the Azure SDK for Python to make a local copy of the retrievable fields of a search index, and then push those fields to a new search index. |
+| [resumable-index-backup-restore](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/resumable-index-backup-restore/backup-and-restore.ipynb) | This sample accommodates larger indexes exceeding 100,000 documents.|
 
 > [!TIP]
 > Try the [Samples browser](/samples/browse/?languages=python&products=azure-cognitive-search) to search for Microsoft code samples in GitHub, filtered by product, service, and language.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonサンプルの更新: Azure AI Search"
}
```

### Explanation
この変更は、Azure AI Searchに関するPythonサンプルの説明が含まれる文書に対するマイナーな更新です。具体的な変更点は以下の通りです。

1. **リポジトリ名の修正**: 「azure-search-backup-and-restore.ipynb」というリポジトリ名が「index-backup-and-restore.ipynb」に変更され、正確なリンクへと修正されました。

2. **新しいサンプルの追加**: 新しく「resumable-index-backup-restore」というサンプルが追加されました。このサンプルは、10万件以上のドキュメントを超える大きなインデックスに対応していることが説明されています。

これらの変更は、ドキュメントの正確性とユーザーに提供する情報の充実を目指しています。

## articles/search/search-faceted-navigation.md{#item-f29d1e}

<details>
<summary>Diff</summary>
````diff
@@ -8,21 +8,22 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 01/16/2025
+ms.date: 02/26/2025
 ---
 
 # Add faceted navigation to a search app
 
 Faceted navigation is used for self-directed drilldown filtering on query results in a search app, where your application offers form controls for scoping search to groups of documents (for example, categories or brands), and Azure AI Search provides the data structures and filters to back the experience. 
 
-In this article, learn the basic steps for creating a faceted navigation structure in Azure AI Search.
+In this article, learn how to create a faceted navigation structure in Azure AI Search.
 
-> [!div class="checklist"]
+<!-- > [!div class="checklist"]
 > * Set field attributes in the index
 > * Structure the request and response
 > * Add navigation controls and filters in the presentation layer
 
 Code in the presentation layer does the heavy lifting in a faceted navigation experience. The demos and samples listed at the end of this article provide working code that shows you how to bring everything together.
+ -->
 
 ## Faceted navigation in a search page
 
@@ -34,9 +35,9 @@ In Azure AI Search, facets are one layer deep and can't be hierarchical. If you
 
 Facets can help you find what you're looking for, while ensuring that you don't get zero results. As a developer, facets let you expose the most useful search criteria for navigating your search index.
 
-## Enable facets in the index
+## Add facets to an index
 
-Faceting is enabled on a field-by-field basis in an index definition when you set the "facetable" attribute to true.
+Facets are enabled on a field-by-field basis in an index definition when you set the "facetable" attribute to true.
 
 Although it's not strictly required, you should also set the "filterable" attribute so that you can build the necessary filters that back the faceted navigation experience in your search application.
 
@@ -65,7 +66,12 @@ Facets can be calculated over single-value fields and collections. Fields that w
 
 * Short descriptive values (one or two words) that render nicely in a navigation tree
 
-The values within a field, and not the field name itself, produces the facets in a faceted navigation structure. If the facet is a string field named *Color*, facets are blue, green, and any other value for that field.
+The values within a field, and not the field name itself, produce the facets in a faceted navigation structure. If the facet is a string field named *Color*, facets are blue, green, and any other value for that field.
+
+You can't use `Edm.GeographyPoint` or `Collection(Edm.GeographyPoint)` fields in faceted navigation. Facets work best on fields with low cardinality. Due to the resolution of geo-coordinates, it's rare that any two sets of coordinates are equal in a given dataset. As such, facets aren't supported for geo-coordinates. You should use a city or region field to facet by location.
+
+> [!TIP]
+> As a best practice for performance and storage optimization, turn faceting off for fields that should never be used as a facet. In particular, string fields for unique values, such as an ID or product name, should be set to `"facetable": false` to prevent their accidental (and ineffective) use in faceted navigation. This is especially true for the REST API that enables filters and facets by default.
 
 As a best practice, check fields for null values, misspellings or case discrepancies, and single and plural versions of the same word. By default, filters and facets don't undergo lexical analysis or [spell check](speller-how-to-add.md), which means that all values of a "facetable" field are potential facets, even if the words differ by one character. Optionally, you can [assign a normalizer](search-normalizers.md) to a "filterable" and "facetable" field to smooth out variations in casing and characters.
 
@@ -79,14 +85,9 @@ If you're using one of the Azure SDKs, your code must explicitly set the field a
 * `Edm.Int32`, `Edm.Int64`, `Edm.Double`
 * Collections of any of the above types, for example `Collection(Edm.String)` or `Collection(Edm.Double)`
 
-You can't use `Edm.GeographyPoint` or `Collection(Edm.GeographyPoint)` fields in faceted navigation. Facets work best on fields with low cardinality. Due to the resolution of geo-coordinates, it's rare that any two sets of coordinates are equal in a given dataset. As such, facets aren't supported for geo-coordinates. You would need a city or region field to facet by location.
-
-> [!TIP]
-> As a best practice for performance and storage optimization, turn faceting off for fields that should never be used as a facet. In particular, string fields for unique values, such as an ID or product name, should be set to `"facetable": false` to prevent their accidental (and ineffective) use in faceted navigation. This is especially true for the REST API that enables filters and facets by default.
-
 ## Facet request and response
 
-Facets are specified on the query, and the faceted navigation structure is returned at the top of the response. The structure of a request and response is fairly simple. In fact, the real work behind faceted navigation lies in the presentation layer, covered in a later section. 
+Facets are specified on the query, and the faceted navigation structure is returned at the top of the response.
 
 The following REST example is an unqualified query (`"search": "*"`) that is scoped to the entire index (see the [built-in hotels sample](search-get-started-portal.md)). Facets are usually a list of fields, but this query shows just one for a more readable response.
 
@@ -185,6 +186,7 @@ To guarantee accuracy, you can artificially inflate the count:\<number> to a lar
 
 The tradeoff with this workaround is increased query latency, so use it only when necessary.
 
+<!-- 
 ## Presentation layer
 
 In application code, the pattern is to use facet query parameters to return the faceted navigation structure along with facet results, plus a `$filter` expression.  The filter expression handles the click event and further narrows the search result based on the facet selection.
@@ -247,21 +249,21 @@ function UpdateBusinessTitleFacets(data) {
 
   $("#business_title_facets").html(facetResultsHTML);
 }
-```
+``` -->
 
 ## Tips for working with facets
 
 This section is a collection of tips and workarounds that might be helpful.
 
 ### Preserve a facet navigation structure asynchronously of filtered results
 
-One of the challenges of faceted navigation in Azure AI Search is that facets exist for current results only. In practice, it's common to retain a static set of facets so that the user can navigate in reverse, retracing steps to explore alternative paths through search content. 
+In Azure AI Search, facets exist for current results only. However, it's a common application requirement to retain a static set of facets so that the user can navigate in reverse, retracing steps to explore alternative paths through search content. 
 
-Although this is a common use case, it's not something the faceted navigation structure currently provides out-of-the-box. Developers who want static facets typically work around the limitation by issuing two filtered queries: one scoped to the results, the other used to create a static list of facets for navigation purposes.
+If you want a static set of facets alongside a dynamic drilldown experience, you can implement it by using two filtered queries: one scoped to the results, the other used to create a static list of facets for navigation purposes.
 
 ### Clear facets
 
-When you design the search results page, remember to add a mechanism for clearing facets. If you add check boxes, you can easily see how to clear the filters. For other layouts, you might need a breadcrumb pattern or another creative approach. In the hotels C# sample, you can send an empty search to reset the page. In contrast, the NYCJobs sample application provides a clickable `[X]` after a selected facet to clear the facet, which is a stronger visual queue to the user.
+When you design the user experience, remember to add a mechanism for clearing facets. A common approach for clearing facets is issue an empty search request to reset the page.
 
 ### Trim facet results with more filters
 
@@ -276,16 +278,6 @@ Content type
 
 In general, if you find that facet results are consistently too large, we recommend that you add more filters to give users more options for narrowing the search.
 
-### A facet-only search experience
-
-If your application uses faceted navigation exclusively (that is, no search box), you can mark the field as `searchable=false`, `filterable=true`, `facetable=true` to produce a more compact index. Your index won't include inverted indexes and there is no text analysis or tokenization during indexing. Filters are made on exact matches at the character level.
-
-### Validate inputs at query-time
-
-If you build the list of facets dynamically based on untrusted user input, validate that the names of the faceted fields are valid. Or, escape the names when building URLs by using either `Uri.EscapeDataString()` in .NET, or the equivalent in your platform of choice.
-
-## Samples
-
-We recommend the following samples for faceted navigation. The samples also include filters, suggestions, and autocomplete. These samples use React for the presentation layer.
+## Next steps
 
-* [C#: Add search to web apps](tutorial-csharp-overview.md)
+We recommend the [C#: Add search to web apps](tutorial-csharp-overview.md) for an example of faceted navigation. The sample also includes filters, suggestions, and autocomplete. It uses JavaScript and React for the presentation layer.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファセットナビゲーションに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるファセットナビゲーションに関するドキュメントのマイナーな更新です。改訂内容は以下の通りです。

1. **日付の更新**: `ms.date`が2025年1月16日から2025年2月26日に変更され、文書の最新性が反映されました。

2. **表現の修正**: 記事の説明文が「基本的な手順を学ぶ」から「ファセットナビゲーション構造を作成する方法を学ぶ」と具体的な表現に変更されました。また、個々のファセットの設定やメカニズムの説明が改善され、より明瞭になりました。

3. **カスタム情報の追加**: 新しいヒントやベストプラクティスが追加され、ファセットナビゲーションの設計において重要な注意点が強調されました。特に、パフォーマンスとストレージの最適化のために「facetable」を無効にすべきフィールドについての案内が詳細に説明されています。

4. **セクションの整理**: 不要な部分が削除され、情報が整理された結果、読みやすくなっています。具体的には、ナビゲーションが不要なフィールドや、ファセットの選択を詳細に管理するためのガイダンスが強化されました。

全体として、これらの変更は、ファセットナビゲーション機能の理解を深め、ユーザーにとっての有用性を向上させることを目的としています。

## articles/search/search-how-to-large-index.md{#item-d34e42}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 10/24/2024
+ms.date: 02/25/2025
 ---
 
 # Index large data sets in Azure AI Search
@@ -76,7 +76,7 @@ Partitioning data into smaller individual data sources enables parallel processi
 
 As with the push API, indexers allow you to configure the number of items per batch. For indexers based on the [Create Indexer REST API](/rest/api/searchservice/indexers/create), you can set the `batchSize` argument to customize this setting to better match the characteristics of your data. 
 
-Default batch sizes are data-source specific. Azure SQL Database and Azure Cosmos DB have a default batch size of 1,000. In contrast, Azure Blob indexing sets batch size at 10 documents in recognition of the larger average document size. 
+Default batch sizes are data-source specific. Azure SQL Database and Azure Cosmos DB have a default batch size of 1,000. In contrast, Azure Blob and SharePoint Online (Preview) indexing sets batch size at 10 documents in recognition of the larger average document size. 
 
 ### Schedule indexers for long-running processes
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおける大規模インデックス管理の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける大規模データセットのインデックス管理に関する文書のマイナーな更新です。主な変更点は以下の通りです。

1. **日付の更新**: `ms.date`の値が2024年10月24日から2025年2月25日に変更され、文書の最新性が反映されました。

2. **情報の追加**: Azure BlobとSharePoint Online（プレビュー）の両方のインデックスに関するバッチサイズの情報が追加されました。具体的には、これらのデータソースでのデフォルトのバッチサイズが10ドキュメントに設定されていることが明記され、文書の正確性が向上しました。

3. **表現の修正**: 一部の文言が改善され、情報がより明確に伝わるようになっています。

この変更により、ユーザーはAzure AI Searchでの大規模データのインデックス作成におけるバッチ処理の特性について、より正確で詳細な情報を得ることができます。

## articles/search/search-howto-reindex.md{#item-46738a}

<details>
<summary>Diff</summary>
````diff
@@ -228,13 +228,13 @@ Some modifications require an index drop and rebuild, replacing a current index
 | Assign an analyzer to a field | [Analyzers](search-analyzers.md) are defined in an index, assigned to fields, and then invoked during indexing to inform how tokens are created. You can add a new analyzer definition to an index at any time, but you can only *assign* an analyzer when the field is created. This is true for both the **analyzer** and **indexAnalyzer** properties. The **searchAnalyzer** property is an exception (you can assign this property to an existing field). |
 | Update or delete an analyzer definition in an index | You can't delete or change an existing analyzer configuration (analyzer, tokenizer, token filter, or char filter) in the index unless you rebuild the entire index. |
 | Add a field to a suggester | If a field already exists and you want to add it to a [Suggesters](index-add-suggesters.md) construct, rebuild the index. |
-| Switch tiers | In-place upgrades aren't supported. If you require more capacity, create a new service and rebuild your indexes from scratch. To help automate this process, you can use the **index-backup-restore** sample code in this [Azure AI Search .NET sample repo](https://github.com/Azure-Samples/azure-search-dotnet-utilities). This app backs up your index to a series of JSON files, and then recreate the index in a search service you specify.|
+| Switch tiers | In-place upgrades aren't supported. If you require more capacity, create a new service and rebuild your indexes from scratch. To help automate this process, you can use a code sample that backs up your index to a series of JSON files. You can then recreate the index in a search service you specify.|
 
 The order of operations is:
 
 1. [Get an index definition](/rest/api/searchservice/indexes/get) in case you need it for future reference, or to use as the basis for a new version.
 
-1. Consider using a backup and restore solution to preserve a copy of index content. There are solutions in [C#](https://github.com/liamca/azure-search-backup-restore/blob/master/README.md) and in [Python](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/index-backup-restore). We recommend the Python version because it's more up to date.
+1. Consider using a backup and restore solution to preserve a copy of index content. There are solutions in [C#](https://github.com/liamca/azure-search-backup-restore/blob/master/README.md) and in [Python](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore). We recommend the Python version because it's more up to date.
 
    If you have capacity on your search service, keep the existing index while creating and testing the new one.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "再インデックスに関する文書の更新"
}
```

### Explanation
この変更は、Azureの再インデックス機能に関する文書のマイナーな更新です。主な変更点は以下の通りです。

1. **文言の修正**: `Switch tiers`セクションにある説明文が改善され、内容がより明確になりました。具体的には、インデックスをバックアップし、指定した検索サービスで再作成するためのプロセスの自動化に関する情報が整理されました。

2. **Pythonソリューションのリンク更新**: バックアップとリストアのソリューションのリンクが更新され、Pythonのサンプルが最新のものに改訂されました。これにより、ユーザーはより有用な情報にアクセスできます。

3. **順序の改善**: 手順が引き続き明確に記載されており、ユーザーがインデックスを再構築する際に必要な情報をすぐに参照できるようになっています。

この変更により、ユーザーは再インデックスの手続きやバックアップ戦略について、より正確かつ効率的に情報を得ることができます。

## articles/search/search-reliability.md{#item-3e9b1a}

<details>
<summary>Diff</summary>
````diff
@@ -189,7 +189,7 @@ If you don't use indexers, you would use your application code to push objects a
 
 ## Back up and restore alternatives
 
-A business continuity strategy for the data layer usually includes a restore-from-backup step. Because Azure AI Search isn't a primary data storage solution, Microsoft doesn't provide a formal mechanism for self-service backup and restore. However, you can use the **index-backup-restore** sample code in this [Azure AI Search .NET sample repo](https://github.com/Azure-Samples/azure-search-dotnet-utilities) to back up your index definition and snapshot to a series of JSON files, and then use these files to restore the index, if needed. This tool can also move indexes between service tiers.
+A business continuity strategy for the data layer usually includes a restore-from-backup step. Because Azure AI Search isn't a primary data storage solution, Microsoft doesn't provide a formal mechanism for self-service backup and restore. However, you can use the **index-backup-restore** sample code in this [Azure AI Search .NET sample repo](https://github.com/Azure-Samples/azure-search-dotnet-utilities)  or in this [Python sample repository](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/index-backup-restore/azure-search-backup-and-restore.ipynb) to back up your index definition and snapshot to a series of JSON files, and then use these files to restore the index, if needed. This tool can also move indexes between service tiers.
 
 Otherwise, your application code used for creating and populating an index is the de facto restore option if you delete an index by mistake. To rebuild an index, you would delete it (assuming it exists), recreate the index in the service, and reload by retrieving data from your primary data store.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索の信頼性に関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchの信頼性に関する文書のマイナーな更新です。主要なポイントは以下の通りです。

1. **文言の追加**: バックアップおよびリストアの代替手段に関するセクションに、Pythonサンプルリポジトリへのリンクが追加されました。これにより、ユーザーは.NETだけでなく、Pythonでもインデックスのバックアップとリストアを行う方法を確認できるようになりました。

2. **リンクの最新化**: 追加されたリンクは、Pythonを使用したバックアップとリストアの具体的な実装にユーザーを誘導するものであり、使いやすさが向上しています。

この変更により、ユーザーはAzure AI Searchにおけるインデックスのバックアップおよびリストア手法について、より広範な情報を得られるようになり、選択肢が増えます。結果として、ビジネス継続性戦略の一環として、データの保護に対する理解が深まることが期待されます。

## articles/search/search-sku-manage-costs.md{#item-6e0122}

<details>
<summary>Diff</summary>
````diff
@@ -42,15 +42,15 @@ Billing is based on capacity (SUs) and the costs of running premium features, su
 
 | Meter | Unit |
 |-------|------|
-| Image extraction (AI enrichment) <sup>1, 2</sup> | Per 1000 images or files. See the [pricing page](https://azure.microsoft.com/pricing/details/search/#pricing). |
+| Image extraction (AI enrichment) <sup>1, 2</sup> | Per 1000 images. See the [pricing page](https://azure.microsoft.com/pricing/details/search/#pricing). |
 | Custom Entity Lookup skill (AI enrichment) <sup>1</sup> | Per 1000 text records. See the [pricing page](https://azure.microsoft.com/pricing/details/search/#pricing) |
 | [Built-in skills](cognitive-search-predefined-skills.md)  (AI enrichment) <sup>1</sup> | Number of transactions, billed at the same rate as if you had performed the task by calling Azure AI services directly. You can process 20 documents per indexer per day for free. Larger or more frequent workloads require a multi-resource Azure AI services key. |
 | [Semantic ranker](semantic-search-overview.md) <sup>1</sup> | Number of queries of "queryType=semantic", billed at a progressive rate. See the [pricing page](https://azure.microsoft.com/pricing/details/search/#pricing). |
 | [Shared private link](search-indexer-howto-access-private.md) <sup>1</sup> | [Billed for bandwidth](https://azure.microsoft.com/pricing/details/private-link/) as long as the shared private link exists and is used. |
 
 <sup>1</sup> Applies only if you use or enable the feature.
 
-<sup>2</sup> Extracts images from a file within the indexer pipeline. Text extraction is free. Image extraction is billed during the initial document cracking step and when invoking the Document Extraction skill. In an [indexer configuration](/rest/api/searchservice/indexers/create#indexer-parameters), `imageAction` is the parameter that triggers image extraction. If `imageAction` is set to "none" (the default), there's no charge. If set to "generateNormalizedImages" or "generateNormalizedImagePerPage" and the document contains images, you're charged for each image extraction. If the document contains no images, you're still billed for the action because the indexer has to crack the file to look for images.
+<sup>2</sup> Refers to images extracted from a file within the indexer pipeline. Text extraction is free. Image extraction is billed during the initial document cracking step and when invoking the Document Extraction skill. In an [indexer configuration](/rest/api/searchservice/indexers/create#indexer-parameters), `imageAction` is the parameter that triggers image extraction. If `imageAction` is set to "none" (the default), there's no charge. If set to "generateNormalizedImages" or "generateNormalizedImagePerPage" and the document contains images, you're charged for each image. This is true even if there are no skills to consume the image content.
 
 You aren't billed on the number of full text or vector queries, query responses, or documents ingested, although [service limits](search-limits-quotas-capacity.md) do apply at each tier.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コスト管理に関する検索文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchのコスト管理に関する文書のマイナーな更新です。重要なポイントは以下の通りです。

1. **表記の明確化**: 「画像抽出 (AIエンリッチメント)」の単位について、説明文が「Per 1000 images」に変更されました。これにより、料金が適用される画像の単位が明確になり、ユーザーにとって理解しやすくなりました。

2. **料金体系の詳細化**: 画像抽出の実行条件に関する説明が強化され、特に「imageAction」パラメータの動作について詳しく説明されています。これにより、ユーザーは画像抽出がどのように課金されるかをより具体的に知ることができ、結果としてコスト管理の向上が期待されます。

この変更により、ユーザーはAzure AI Searchの機能によるコストをより正確に把握でき、適切な使用を促進するための情報が強化されました。これにより、運用コストを最適化しやすくなるでしょう。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -113,7 +113,7 @@ There's no built-in support to upgrade or downgrade tiers. If you want to switch
 
 + Delete the old search service once you're sure it's no longer needed.
 
-For large indexes that you don't want to rebuild from scratch, consider using the [backup and restore sample](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore/README.md) to move them.
+For large indexes that you don't want to rebuild from scratch, consider using one of the backup and restore samples to move them:[backup and restore sample (C#)](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore/README.md), [backup and restore sample (Python)](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/index-backup-restore/azure-search-backup-and-restore.ipynb), [larget index backup and restore (Python)](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/resumable-index-backup-restore/backup-and-restore.ipynb).
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SKU Tierに関する文書の更新"
}
```

### Explanation
この変更は、Azure AI SearchのSKU Tierに関する文書のマイナーな更新です。主要なポイントは以下の通りです。

1. **リンクの追加**: 「バックアップおよびリストア」サンプルのセクションに、新たにPythonを使用した2つのサンプルへのリンクが追加されました。これにより、ユーザーはC#だけでなく、Pythonにおいてもインデックスのバックアップとリストアを行う方法を学ぶことが可能になります。

2. **表現の明確化**: 更新された文では、「バックアップおよびリストア」サンプルに関する具体的なリソースが示されることにより、ユーザーが目的に応じたサンプルを選びやすくなっています。

この変更により、ユーザーはインデックスの移動方法に関する選択肢が増え、より柔軟に使用できるようになります。結果として、サービスの効率的な管理と運用が促進されることが期待されます。

## articles/search/vector-search-how-to-create-index.md{#item-97c769}

<details>
<summary>Diff</summary>
````diff
@@ -128,7 +128,7 @@ Be sure to have a strategy for [vectorizing your content](vector-search-how-to-g
                 "name": "binary-quantization",
                 "kind": "binaryQuantization",
                 "rerankWithOriginalVectors": true,
-                "defaultOversampling": 10.0,
+                "defaultOversampling": 10.0
             }
         ],
         "algorithms": [
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のインデックス作成に関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるベクトル検索のインデックス作成に関する文書のマイナーな更新です。主な内容は以下の通りです。

1. **コードの整形**: `defaultOversampling`の行の末尾にあるコンマが削除されました。この変更は、コードの整形に関するものであり、文法やコンパイルエラーを防ぐためのものです。

2. **コンテンツの明瞭性**: 整形により、コードがより明確になり、他の開発者が内容を理解しやすくなります。このような小さな変更は、コードがより一貫性を持ち、保守性を向上させるのに役立ちます。

これにより、この文書は技術者がベクトル検索におけるインデックス作成のプロセスを理解する際に、より使いやすく、一貫性のあるものになります。


