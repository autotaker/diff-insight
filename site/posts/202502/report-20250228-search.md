---
date: '2025-02-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:42a07e4...MicrosoftDocs:63a40ca
summary: Azure AI Searchに関する2つの記事が軽微な更新を受け、ファセットナビゲーションと検索インデックス作成のガイドラインがより理解しやすくなりました。ファセットナビゲーションの記事には、実装時のベストプラクティスやフィールド属性の設定方法が追加されました。破壊的変更はありませんが、Azureポータルでの検索インデックス作成に関するクイックスタートでは文法修正や手順の整理が行われました。この更新により、開発者はより正確で効率的な実装が可能になり、初心者にも直感的な理解を提供します。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:42a07e4...MicrosoftDocs:63a40ca){target="_blank"}

# ハイライト
Azure AI Searchに関する2つの記事が軽微な更新を受けました。これにより、ファセットナビゲーションと検索インデックス作成のガイドラインがより理解しやすく改善されています。

## 新機能
- ファセットナビゲーションに関する記事に、実装時のベストプラクティスやフィールド属性の設定方法についての詳細が加えられました。

## 破壊的変更
- 破壊的変更は特にありません。

## その他の更新
- Azureポータルでの検索インデックス作成に関するクイックスタートで、文法修正、新しい著者情報の追加、手順の整理が行われました。

# インサイト
今回のドキュメント更新は、Azure AI Searchを利用する開発者にとって重要な改善が含まれています。ファセットナビゲーションの部分では、説明が具体的になり、ベストプラクティスに則った設定方法についての知識を深めやすくなっています。これにより、実装時の正確さと効率が向上するでしょう。

一方、Azureポータルを使用した検索インデックスのクイックスタートガイドでは、特に初心者が直感的に操作を理解しやすくするための文章構成の改善が図られています。これには、プロセスの一貫性向上とネットワーク設定の注意事項が含まれており、誤解を減らしてスムーズなユーザーエクスペリエンスの提供が期待されます。

これらの更新は、Azure AI Searchの利用を推進するにあたり、ユーザーにとって役立つ情報をわかりやすく提供し、より良い活用をサポートするものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-faceted-navigation.md](#item-f29d1e) | minor update | ファセットナビゲーションに関する記事の更新 | modified | 15 | 86 | 101 | 
| [search-get-started-portal.md](#item-6d0cb1) | minor update | Azure ポータルでの検索インデックス作成のクイックスタート更新 | modified | 84 | 62 | 146 | 


# Modified Contents
## articles/search/search-faceted-navigation.md{#item-f29d1e}

<details>
<summary>Diff</summary>
````diff
@@ -13,18 +13,10 @@ ms.date: 02/26/2025
 
 # Add faceted navigation to a search app
 
-Faceted navigation is used for self-directed drilldown filtering on query results in a search app, where your application offers form controls for scoping search to groups of documents (for example, categories or brands), and Azure AI Search provides the data structures and filters to back the experience. 
+Faceted navigation is used for self-directed drill-down filtering on query results in a search app, where your application offers form controls for scoping search to groups of documents (for example, categories or brands), and Azure AI Search provides the data structures and filters to back the experience. 
 
 In this article, learn how to create a faceted navigation structure in Azure AI Search.
 
-<!-- > [!div class="checklist"]
-> * Set field attributes in the index
-> * Structure the request and response
-> * Add navigation controls and filters in the presentation layer
-
-Code in the presentation layer does the heavy lifting in a faceted navigation experience. The demos and samples listed at the end of this article provide working code that shows you how to bring everything together.
- -->
-
 ## Faceted navigation in a search page
 
 Facets are dynamic and returned on a query. A search response brings with it all of the facet categories used to navigate the documents in the result. The query executes first, and then facets are pulled from the current results and assembled into a faceted navigation structure.
@@ -39,9 +31,9 @@ Facets can help you find what you're looking for, while ensuring that you don't
 
 Facets are enabled on a field-by-field basis in an index definition when you set the "facetable" attribute to true.
 
-Although it's not strictly required, you should also set the "filterable" attribute so that you can build the necessary filters that back the faceted navigation experience in your search application.
+Although it's not strictly required, it's a best practice to also set the "filterable" attribute so that you can build the necessary filters that back the faceted navigation experience in your search application.
 
-The following example of the "hotels" sample index shows "facetable" and "filterable" on low cardinality fields that contain single values or short phrases: "Category", "Tags", "Rating".
+The following example of the hotels sample index shows "facetable" and "filterable" on low cardinality fields that contain single values or short phrases: "Category", "Tags", "Rating".
 
 ```json
 {
@@ -62,28 +54,30 @@ The following example of the "hotels" sample index shows "facetable" and "filter
 
 Facets can be calculated over single-value fields and collections. Fields that work best in faceted navigation have these characteristics:
 
+* Human readable (nonvector) content
+
 * Low cardinality (a small number of distinct values that repeat throughout documents in your search corpus)
 
 * Short descriptive values (one or two words) that render nicely in a navigation tree
 
 The values within a field, and not the field name itself, produce the facets in a faceted navigation structure. If the facet is a string field named *Color*, facets are blue, green, and any other value for that field.
 
-You can't use `Edm.GeographyPoint` or `Collection(Edm.GeographyPoint)` fields in faceted navigation. Facets work best on fields with low cardinality. Due to the resolution of geo-coordinates, it's rare that any two sets of coordinates are equal in a given dataset. As such, facets aren't supported for geo-coordinates. You should use a city or region field to facet by location.
+You can't use `Edm.GeographyPoint` or `Collection(Edm.GeographyPoint)` fields in faceted navigation. Recall that facets work best on fields with low cardinality. Due to the resolution of geo-coordinates, it's rare that any two sets of coordinates are equal in a given dataset. As such, facets aren't supported for geo-coordinates. You should use a city or region field to facet by location.
 
-> [!TIP]
-> As a best practice for performance and storage optimization, turn faceting off for fields that should never be used as a facet. In particular, string fields for unique values, such as an ID or product name, should be set to `"facetable": false` to prevent their accidental (and ineffective) use in faceted navigation. This is especially true for the REST API that enables filters and facets by default.
+As a best practice for performance and storage optimization, turn faceting off for fields that should never be used as a facet. In particular, string fields for unique values, such as an ID or product name, should be set to `"facetable": false` to prevent their accidental (and ineffective) use in faceted navigation. This is especially true for the REST API that enables filters and facets on string fields by default.
 
-As a best practice, check fields for null values, misspellings or case discrepancies, and single and plural versions of the same word. By default, filters and facets don't undergo lexical analysis or [spell check](speller-how-to-add.md), which means that all values of a "facetable" field are potential facets, even if the words differ by one character. Optionally, you can [assign a normalizer](search-normalizers.md) to a "filterable" and "facetable" field to smooth out variations in casing and characters.
+In your code, check fields for null values, misspellings or case discrepancies, and single and plural versions of the same word. By default, filters and facets don't undergo lexical analysis or [spell check](speller-how-to-add.md), which means that all values of a "facetable" field are potential facets, even if the words differ by one character. Optionally, you can [assign a normalizer](search-normalizers.md) to a "filterable" and "facetable" field to smooth out variations in casing and characters.
 
 ### Defaults in REST and Azure SDKs
 
-If you're using one of the Azure SDKs, your code must explicitly set the field attributes. In contrast, the REST API has defaults for field attributes based on the [data type](/rest/api/searchservice/supported-data-types). The following data types are "filterable" and "facetable" by default:
+If you're using one of the Azure SDKs, your code must explicitly set the "facetable" attribute on a field.
+
+The REST API has defaults for field attributes based on the [data type](/rest/api/searchservice/supported-data-types). The following data types are "filterable" and "facetable" by default:
 
-* `Edm.String`
-* `Edm.DateTimeOffset`
-* `Edm.Boolean`
-* `Edm.Int32`, `Edm.Int64`, `Edm.Double`
-* Collections of any of the above types, for example `Collection(Edm.String)` or `Collection(Edm.Double)`
+* `Edm.String` and `Collection(Edm.String)`
+* `Edm.DateTimeOffset` and `Collection(Edm.DateTimeOffset)`
+* `Edm.Boolean` and`Collection(Edm.Boolean)`
+* `Edm.Int32`, `Edm.Int64`, `Edm.Double` and their collection equivalents
 
 ## Facet request and response
 
@@ -186,71 +180,6 @@ To guarantee accuracy, you can artificially inflate the count:\<number> to a lar
 
 The tradeoff with this workaround is increased query latency, so use it only when necessary.
 
-<!-- 
-## Presentation layer
-
-In application code, the pattern is to use facet query parameters to return the faceted navigation structure along with facet results, plus a `$filter` expression.  The filter expression handles the click event and further narrows the search result based on the facet selection.
-
-### Facet and filter combination
-
-The following code snippet from the `JobsSearch.cs` file in the [NYCJobs demo](/samples/azure-samples/search-dotnet-asp-net-mvc-jobs/search-dotnet-asp-net-mvc-jobs/) adds the selected Business Title to the filter if you select a value from the Business Title facet.
-
-```cs
-if (businessTitleFacet != "")
-  filter = "business_title eq '" + businessTitleFacet + "'";
-```
-
-Here's another example from the hotels sample. The following code snippet adds `categoryFacet` to the filter if a user selects a value from the category facet.
-
-```csharp
-if (!String.IsNullOrEmpty(categoryFacet))
-    filter = $"category eq '{categoryFacet}'";
-```
-
-### HTML for faceted navigation
-
-The following example, taken from the `index.cshtml` file of the NYCJobs sample application, shows the static HTML structure for displaying faceted navigation on the search results page. The list of facets is built or rebuilt dynamically when you submit a search term, or select or clear a facet.
-
-```html
-<div class="widget sidebar-widget jobs-filter-widget">
-  <h5 class="widget-title">Filter Results</h5>
-    <p id="filterReset"></p>
-    <div class="widget-content">
-
-      <h6 id="businessTitleFacetTitle">Business Title</h6>
-      <ul class="filter-list" id="business_title_facets">
-      </ul>
-
-      <h6>Location</h6>
-      <ul class="filter-list" id="posting_type_facets">
-      </ul>
-
-      <h6>Posting Type</h6>
-      <ul class="filter-list" id="posting_type_facets"></ul>
-
-      <h6>Minimum Salary</h6>
-      <ul class="filter-list" id="salary_range_facets">
-      </ul>
-
-  </div>
-</div>
-```
-
-### Build HTML dynamically
-
-The following code snippet from the `index.cshtml` (also from NYCJobs demo) dynamically builds the HTML to display the first facet, Business Title. Similar functions dynamically build the HTML for the other facets. Each facet has a label and a count, which displays the number of items found for that facet result.
-
-```js
-function UpdateBusinessTitleFacets(data) {
-  var facetResultsHTML = '';
-  for (var i = 0; i < data.length; i++) {
-    facetResultsHTML += '<li><a href="javascript:void(0)" onclick="ChooseBusinessTitleFacet(\'' + data[i].Value + '\');">' + data[i].Value + ' (' + data[i].Count + ')</span></a></li>';
-  }
-
-  $("#business_title_facets").html(facetResultsHTML);
-}
-``` -->
-
 ## Tips for working with facets
 
 This section is a collection of tips and workarounds that might be helpful.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファセットナビゲーションに関する記事の更新"
}
```

### Explanation
この変更は、Azure AI Searchのファセットナビゲーションに関する記事に対する軽微な更新です。具体的には、文法の修正と内容の明確化を目的とした文の追加が行われました。ファセットナビゲーションの説明がより理解しやすくなるように、一部のフレーズが修正され、より具体的な説明が加えられています。

大きな変更点としては、ファセットナビゲーションを実装する際のベストプラクティスに関する情報が強調され、フィールド属性の設定方法やファセットの特性についての詳細が明確にされました。そのほか、ナビゲーション体験を向上させるためのアドバイスが追加され、読者が具体的な実装方法を理解しやすくなっています。

全体的に見て、この更新されたドキュメントは、ファセットナビゲーションを利用する際のユーザーにとって、より実践的で役立つ情報を提供することを目指しています。

## articles/search/search-get-started-portal.md{#item-6d0cb1}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +1,13 @@
 ---
 title: "Quickstart: Create a search index in the Azure portal"
 titleSuffix: Azure AI Search
-description: Learn how to create, load, and query your first search index by using the Import Data wizard in the Azure portal. This quickstart uses a fictitious hotel dataset for sample data.
+description: Learn how to create, load, and query your first search index using the Import Data wizard in the Azure portal. This quickstart uses a fictitious hotel dataset for sample data.
 manager: nitinme
-author: HeidiSteen
-ms.author: heidist
+author: haileytap
+ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 11/19/2024
+ms.date: 02/27/2025
 ms.custom:
   - mode-ui
   - ignite-2023
@@ -16,164 +16,185 @@ ms.custom:
 
 # Quickstart: Create a search index in the Azure portal
 
-In this Azure AI Search quickstart, create your first _search index_ by using the [**Import data** wizard](search-import-data-portal.md) and a built-in sample data source consisting of fictitious hotel data hosted by Microsoft. The wizard guides you through the no-code creation of a search index to help you write interesting queries within minutes. 
+In this Azure AI Search quickstart, create your first search index using the [**Import data** wizard](search-import-data-portal.md) and a built-in sample of fictitious hotel data hosted by Microsoft. The wizard requires no code to create an index, helping you write interesting queries within minutes.
 
-The wizard creates multiple objects on your search service - [searchable index](search-what-is-an-index.md) - but also an [indexer](search-indexer-overview.md) and data source connection for automated data retrieval. At the end of this quickstart, we review each object. 
+The wizard creates multiple objects on your search service, including a [searchable index](search-what-is-an-index.md), an [indexer](search-indexer-overview.md), and a data source connection for automated data retrieval. At the end of this quickstart, we review each object.
 
 > [!NOTE]
 > The **Import data** wizard includes options for OCR, text translation, and other AI enrichments that aren't covered in this quickstart. For a similar walkthrough that focuses on applied AI, see [Quickstart: Create a skillset in the Azure portal](search-get-started-skillset.md).
 
 ## Prerequisites
 
-- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/).
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/).
 
-- An Azure AI Search service for any tier and any region. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) under your current subscription. You can use a free service for this quickstart.
++ An Azure AI Search service. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription. You can use a free service for this quickstart.
 
-- Familiarity with the wizard. See [Import data wizards in the Azure portal](search-import-data-portal.md) for details.
++ Familiarity with the wizard. See [Import data wizards in the Azure portal](search-import-data-portal.md) for details.
 
-For this quickstart, which uses built-in sample data, make sure the search service doesn't have [network access controls](service-configure-firewall.md) in place. the Azure portal controller uses the public endpoint to retrieve data and metadata from the built-in sample data source hosted by Microsoft. For more information, see [Secure connections in the import wizards](search-import-data-portal.md#secure-connections).
+### Check for network access
+
+For this quickstart, which uses built-in sample data, make sure your search service doesn't have [network access controls](service-configure-firewall.md). The Azure portal controller uses a public endpoint to retrieve data and metadata from the Microsoft-hosted data source. For more information, see [Secure connections in the import wizards](search-import-data-portal.md#secure-connections).
 
 ### Check for space
 
-Many customers start with the free service. The free tier is limited to three indexes, three data sources, and three indexers. Make sure you have room for extra items before you begin. This quickstart creates one of each object.
+Many customers start with a free search service, which is limited to three indexes, three indexers, and three data sources. This quickstart creates one of each, so before you begin, make sure you have room for extra objects.
 
-Check the **Overview > Usage** tab for the service to see how many indexes, indexers, and data sources you already have. 
+On the **Overview** tab, select **Usage** to see how many indexes, indexers, and data sources you currently have.
 
-:::image type="content" source="media/search-get-started-portal/overview-quota-usage.png" alt-text="Screenshot of the Overview page for an Azure AI Search service instance in the Azure portal, showing the number of indexes, indexers, and data sources." lightbox="media/search-get-started-portal/overview-quota-usage.png":::
+   :::image type="content" source="media/search-get-started-portal/overview-quota-usage.png" alt-text="Screenshot of the Overview page for an Azure AI Search service instance in the Azure portal, showing the number of indexes, indexers, and data sources." lightbox="media/search-get-started-portal/overview-quota-usage.png":::
 
 ## Start the wizard
 
-1. Sign in to the [Azure portal](https://portal.azure.com/) with your Azure account, and go to your Azure AI Search service.
+1. Sign in to the [Azure portal](https://portal.azure.com/).
+
+1. Go to your search service.
 
-1. On the **Overview** page, select **Import data** to start the wizard.
+1. On the **Overview** tab, select **Import data** to start the wizard.
 
    :::image type="content" source="media/search-import-data-portal/import-data-cmd.png" alt-text="Screenshot that shows how to open the Import data wizard in the Azure portal.":::
 
-## Create and load an index
+## Create and load a search index
 
-In this section, create and load an index in four steps.
+In this section, you create and load an index in four steps:
+
+1. [Connect to a data source](#connect-to-a-data-source)
+1. [Skip configuration for cognitive skills](#skip-configuration-for-cognitive-skills)
+1. [Configure the index](#configure-the-index)
+1. [Configure and run the indexer](#configure-and-run-the-indexer)
 
 ### Connect to a data source
 
-The wizard creates a data source connection to sample data hosted by Microsoft on Azure Cosmos DB. This sample data is retrieved accessed over a public endpoint. You don't need your own Azure Cosmos DB account or source files to run this quickstart.
+The wizard creates a data source connection to sample data that Microsoft hosts on Azure Cosmos DB. The sample data is accessed through a public endpoint, so you don't need an Azure Cosmos DB account or source files for this step.
 
-1. On **Connect to your data**, expand the **Data Source** dropdown list and select **Samples**.
+To connect to the sample data:
 
-1. In the list of built-in samples, select **hotels-sample**.
+1. On **Connect to your data**, expand the **Data Source** dropdown list and select **Samples**.
 
-   :::image type="content" source="media/search-get-started-portal/import-hotels-sample.png" alt-text="Screenshot that shows how to select the hotels-sample data source in the Import data wizard.":::
+1. Select **hotels-sample** from the list of built-in samples.
 
 1. Select **Next: Add cognitive skills (Optional)** to continue.
 
+   :::image type="content" source="media/search-get-started-portal/import-hotels-sample.png" alt-text="Screenshot that shows how to select the hotels-sample data source in the Import data wizard.":::
+
 ### Skip configuration for cognitive skills
 
-The **Import data** wizard supports the creation of a skillset and [AI-enrichment](cognitive-search-concept-intro.md) into indexing.
+Although the wizard supports skillset creation and [AI enrichment](cognitive-search-concept-intro.md) during indexing, cognitive skills are beyond the scope of this quickstart.
 
-1. For this quickstart, ignore the AI enrichment configuration options on the **Add cognitive skills** tab.
+To skip this step in the wizard:
 
-1. Select **Skip to: Customize target index** to continue.
+1. On **Add cognitive skills**, ignore the AI enrichment configuration options.
+
+1. Select **Next: Customize target index** to continue.
 
    :::image type="content" source="media/search-get-started-portal/skip-cognitive-skills.png" alt-text="Screenshot that shows how to Skip to the Customize target index tab in the Import data wizard.":::
 
 > [!TIP]
-> Interested in AI enrichment? Try this [Quickstart: Create a skillset in the Azure portal](search-get-started-skillset.md)
+> To get started with AI enrichment, see [Quickstart: Create a skillset in the Azure portal](search-get-started-skillset.md).
 
 ### Configure the index
 
-The wizard infers a schema for the built-in hotels-sample index. To configure the index, follow these steps:
+The wizard infers a schema for the hotels-sample index. To configure the index:
 
-1. Accept the system-generated values for the **Index name** (_hotels-sample-index_) and **Key** field (_HotelId_).
+1. Accept the system-generated values for the **Index name** (_hotels-sample-index_) and **Key** (_HotelId_).
 
 1. Accept the system-generated values for all field attributes.
 
 1. Select **Next: Create an indexer** to continue.
 
-:::image type="content" source="media/search-get-started-portal/hotels-sample-generated-index.png" alt-text="Screenshot that shows the generated index definition for the hotels-sample data source in the Import data wizard.":::
-
-At a minimum, the index requires an **Index name** and a collection of **Fields**. One field must be marked as the _document key_ to uniquely identify each document. The value is always a string. The wizard scans for unique string fields and chooses one for the key.
+   :::image type="content" source="media/search-get-started-portal/hotels-sample-generated-index.png" alt-text="Screenshot that shows the generated index definition for the hotels-sample data source in the Import data wizard.":::
 
-Each field has a name, data type, and _attributes_ that control how to use the field in the search index. Checkboxes enable or disable the following attributes:
+At a minimum, the search index requires a name and a collection of fields. The wizard scans for unique string fields and marks one as the document key, which uniquely identifies each document in the index.
 
-- **Retrievable**: Fields returned in a query response.
-- **Filterable**: Fields that accept a filter expression.
-- **Sortable**: Fields that accept an orderby expression.
-- **Facetable**: Fields used in a faceted navigation structure.
-- **Searchable**: Fields used in full text search. Strings are searchable. Numeric fields and Boolean fields are often marked as not searchable.
+Each field has a name, a data type, and attributes that control how the field is used in the index. Use the checkboxes to enable or disable the following attributes:
 
-Strings are attributed as **Retrievable** and **Searchable**. Integers are attributed as **Retrievable**, **Filterable**, **Sortable**, and **Facetable**.
+| Attribute | Description | Applicable data types |
+|-----------|-------------|------------------------|
+| Retrievable | Fields returned in a query response. | Strings and integers |
+| Filterable | Fields that accept a filter expression. | Integers |
+| Sortable | Fields that accept an orderby expression. | Integers |
+| Facetable | Fields used in a faceted navigation structure. | Integers |
+| Searchable | Fields used in full text search. Strings are searchable, but numeric and Boolean fields are often marked as not searchable. | Strings |
 
-Attributes affect storage. **Filterable** fields consume extra storage, but **Retrievable** doesn't. For more information, see [Example demonstrating the storage implications of attributes and suggesters](search-what-is-an-index.md#example-demonstrating-the-storage-implications-of-attributes-and-suggesters).
+Attributes affect storage in different ways. For example, filterable fields consume extra storage, while retrievable fields don't. For more information, see [Example demonstrating the storage implications of attributes and suggesters](search-what-is-an-index.md#example-demonstrating-the-storage-implications-of-attributes-and-suggesters).
 
 If you want autocomplete or suggested queries, specify language **Analyzers** or **Suggesters**.
 
 ### Configure and run the indexer
 
-The last step configures and runs the indexer. This object defines an executable process. The data source, index, and indexer are created in this step.
+Finally, you configure and run the indexer, which defines an executable process. The data source and index are also created in this step.
+
+To configure and run the indexer:
 
 1. Accept the system-generated value for the **Indexer name** (_hotels-sample-indexer_).
 
-1. For this quickstart, use the default option to run the indexer once, immediately. The hosted data is static so there's no change tracking enabled for it.
+1. For this quickstart, use the default option to run the indexer immediately and only once. The sample data is static, so you can't enable change tracking.
 
-1. Select **Submit** to create and simultaneously run the indexer.
+1. Select **Submit** to simultaneously create and run the indexer.
 
    :::image type="content" source="media/search-get-started-portal/hotels-sample-indexer.png" alt-text="Screenshot that shows how to configure the indexer for the hotels-sample data source in the Import data wizard.":::
 
 ## Monitor indexer progress
 
-You can monitor creation of the indexer or index in the Azure portal. The service **Overview** page provides links to the resources created in your Azure AI Search service.
+You can monitor the creation of the indexer and index in the Azure portal. The **Overview** tab provides links to the resources created in your search service.
+
+To monitor the progress of the indexer:
 
-1. On the left, select **Indexers**.
+1. Go to your search service in the [Azure portal](https://portal.azure.com/).
+
+1. From the left pane, select **Indexers**.
 
    :::image type="content" source="media/search-get-started-portal/indexers-status.png" alt-text="Screenshot that shows the creation of the indexer in progress in the Azure portal.":::
 
-   It can take a few minutes for the page results to update in the Azure portal. You should see the newly created indexer in the list with a status of _In progress_ or _Success_. The list also shows the number of documents indexed.
+   It can take a few minutes for the results to update. You should see the newly created indexer with a status of **In progress** or **Success**. The list also shows the number of documents indexed.
 
 ## Check search index results
 
-1. On the left, select **Indexes**.
+1. Go to your search service in the [Azure portal](https://portal.azure.com/).
 
-1. Select **hotels-sample-index**. 
+1. From the left pane, select **Indexes**.
 
-   Wait for the Azure portal page to refresh. You should see the index with a document count and storage size.
+1. Select **hotels-sample-index**. If the index has zero documents or storage, wait for the Azure portal to refresh.
 
    :::image type="content" source="media/search-get-started-portal/indexes-list.png" alt-text="Screenshot of the Indexes list on the Azure AI Search service dashboard in the Azure portal.":::
 
 1. Select the **Fields** tab to view the index schema.
 
-   Check to see which fields are **Filterable** or **Sortable** so that you know what queries to write.
+1. Check which fields are **Filterable** or **Sortable** so that you know what queries to write.
 
    :::image type="content" source="media/search-get-started-portal/index-schema-definition.png" alt-text="Screenshot that shows the schema definition for an index in the Azure AI Search service in the Azure portal.":::
 
 ## Add or change fields
 
-On the **Fields** tab, you can create a new field using **Add field** with a name, [supported data type](/rest/api/searchservice/supported-data-types), and attributions.
+On the **Fields** tab, you can create a field by selecting **Add field** and specifying a name, [supported data type](/rest/api/searchservice/supported-data-types), and attributes.
 
-Changing existing fields is harder. Existing fields have a physical representation in the index so they aren't modifiable, not even in code. To fundamentally change an existing field, you need to create a new field that replaces the original. Other constructs, such as scoring profiles and CORS options, can be added to an index at any time.
+Changing existing fields is more difficult. Existing fields have a physical representation in the search index, so they aren't modifiable, not even in code. To fundamentally change an existing field, you must create a new field to replace the original. You can add other constructs, such as scoring profiles and CORS options, to an index at any time.
 
-To clearly understand what you can and can't edit during index design, take a minute to view the index definition options. Grayed options in the field list indicate values that can't be modified or deleted.
+Review the index definition options to understand what you can and can't edit during index design. If an option appears dimmed, you can't modify or delete it.
 
 ## Query with Search explorer
 
-You now have a search index that can be queried with [**Search explorer**](search-explorer.md). **Search explorer** sends REST calls that conform to the [Search POST REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true). The tool supports [simple query syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search) and [full Lucene query syntax](/rest/api/searchservice/lucene-query-syntax-in-azure-search).
+You now have a search index that can be queried using [**Search explorer**](search-explorer.md), which sends REST calls that conform to the [Search POST REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true). This tool supports [simple query syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search) and [full Lucene query syntax](/rest/api/searchservice/lucene-query-syntax-in-azure-search).
+
+To query your search index:
 
 1. On the **Search explorer** tab, enter text to search on.
 
    :::image type="content" source="media/search-get-started-portal/search-explorer-query-string.png" alt-text="Screenshot that shows how to enter and run a query in the  Search Explorer tool.":::
 
-1. Use the **Mini-map** to jump quickly to nonvisible areas of the output.
+1. To jump to nonvisible areas of the output, use the mini map.
 
    :::image type="content" source="media/search-get-started-portal/search-explorer-query-results.png" alt-text="Screenshot that shows long results for a query in the Search Explorer tool and the mini-map.":::
 
 1. To specify syntax, switch to the JSON view.
 
    :::image type="content" source="media/search-get-started-portal/search-explorer-change-view.png" alt-text="Screenshot of the JSON view selector.":::
 
-## Example queries for hotels sample index
+## Example queries for hotels-sample index
 
 The following examples assume the JSON view and the 2024-05-01-preview REST API version.
 
 > [!TIP]
-> JSON view now supports intellisense for parameter name completion. Place the cursor inside the JSON view and type a space character to show a list of all query parameters, or type a single letter like "s" to show just the query parameters starting with "s". Intellisense doesn't exclude invalid parameters so use your best judgement.
+> The JSON view supports intellisense for parameter name completion. Place your cursor inside the JSON view and type a space character to see a list of all query parameters. You can also type a letter, like "s," to see only the query parameters that begin with that letter. Intellisense doesn't exclude invalid parameters, so use your best judgment.
 
 ### Filter examples
 
@@ -201,7 +222,7 @@ Boolean filters assume "true" by default.
 }
 ```
 
-Geospatial search is filter-based. The `geo.distance` function filters all results for positional data based on the specified `Location` and `geography'POINT` coordinates. The query seeks hotels that are within 5 kilometers of the latitude longitude coordinates `-122.12 47.67`, which is "Redmond, Washington, USA." The query displays the total number of matches `&$count=true` with the hotel names and address locations.
+Geospatial search is filter based. The `geo.distance` function filters all results for positional data based on the specified `Location` and `geography'POINT` coordinates. The query seeks hotels within five kilometers of the latitude and longitude coordinates `-122.12 47.67`, which is "Redmond, Washington, USA." The query displays the total number of matches `&$count=true` with the hotel names and address locations.
 
 ```json
 {
@@ -215,7 +236,7 @@ Geospatial search is filter-based. The `geo.distance` function filters all resul
 
 ### Full Lucene syntax examples
 
-The default syntax is [simple syntax](query-simple-syntax.md), but if you want fuzzy search or term boosting or regular expressions, specify the [full syntax](query-lucene-syntax.md).
+The default syntax is [simple syntax](query-simple-syntax.md), but if you want fuzzy search, term boosting, or regular expressions, specify the [full syntax](query-lucene-syntax.md).
 
 ```json
 {
@@ -226,21 +247,22 @@ The default syntax is [simple syntax](query-simple-syntax.md), but if you want f
 }
 ```
 
-By default, misspelled query terms like `seatle` for `Seattle` fail to return matches in a typical search. The `queryType=full` parameter invokes the full Lucene query parser, which supports the tilde `~` operand. When these parameters are present, the query performs a fuzzy search for the specified keyword. The query matches on documents that are similar to but not an exact match to the keyword. 
+Misspelled query terms, like `seatle` instead of `Seattle`, don't return matches in a typical search. The `queryType=full` parameter invokes the full Lucene query parser, which supports the tilde (`~`) operand. When you use these parameters, the query performs a fuzzy search for the specified keyword and matches on terms that are similar but not an exact match.
 
-Take a minute to try a few of these example queries for your index. To learn more about queries, see [Querying in Azure AI Search](search-query-overview.md).
+Take a minute to try these example queries on your index. To learn more about queries, see [Querying in Azure AI Search](search-query-overview.md).
 
 ## Clean up resources
 
 When you work in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
 
-You can find and manage resources for your service in the Azure portal under **All resources** or **Resource groups** in the left pane.
+In the Azure portal, you can find and manage resources for your service under **All resources** or **Resource groups** in the left pane.
 
-If you use a free service, remember that the limit is three indexes, indexers, and data sources. You can delete individual items in the Azure portal to stay under the limit. 
+> [!NOTE]
+> If you're using a free search service, remember that the limit is three indexes, three indexers, and three data sources. You can delete individual objects in the Azure portal to stay under the limit.
 
 ## Next steps
 
-Try an Azure portal wizard to generate a ready-to-use web app that runs in a browser. Use this wizard on the small index you created in this quickstart, or use one of the built-in sample data sets for a richer search experience.
+Try an Azure portal wizard to generate a ready-to-use web app that runs in a browser. Use this wizard on the small index you created in this quickstart, or use one of the built-in sample datasets for a richer search experience.
 
 > [!div class="nextstepaction"]
 > [Create a demo app in the Azure portal](search-create-app-portal.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure ポータルでの検索インデックス作成のクイックスタート更新"
}
```

### Explanation
この変更は、Azureポータルにおける検索インデックスの作成方法に関するクイックスタートガイドの更新です。主に文の修正と整理が行われ、情報の明確化や一貫性の向上に焦点が当てられています。具体的には、いくつかの文が再構成され、読みやすさが向上しています。また、新しい著者情報が追加され、日付が更新されました。

変更内容の中では、手順やインデックスの構成に関する説明が簡潔に整理され、特にウィザードの機能や作成プロセスに関するセクションが見直されています。さらに、ネットワークによるアクセス設定についての注意書きが新たに追加され、ユーザーがクイックスタートを実行する際に考慮すべきポイントが強調されています。

全体的に、この更新により、クイックスタートはより直感的でアクセスしやすくなり、ユーザーがAzureポータルでの検索インデックス作成の基本をスムーズに学べるよう配慮されています。


