---
date: '2024-10-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6f58d1b...MicrosoftDocs:f8a58ce
summary: 最近の更新では、多数のドキュメントに軽微な修正と内容の改善が行われ、日付が更新されています。これにより、日本語表現の自然さや手順の具体性が向上し、利用ガイドが強化されました。新機能の追加はありませんが、既存の機能の説明やガイダンスが明確化されています。破壊的変更はなく、ユーザーの現行ワークフローには影響がありません。特にセマンティックランキングやサービスポータルに関する説明が改善され、サービスをより効果的に利用できるようになります。この更新により、ユーザーは情報を基に迅速な意思決定が可能になり、ドキュメントの品質向上がトラブルシューティングの軽減にも寄与すると期待されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6f58d1b...MicrosoftDocs:f8a58ce){target="_blank"}

# Highlights
最近行われた更新では、多数のドキュメントにおいて軽微な修正と内容の改善が行われ、日付が更新されています。これには、明確で自然な日本語表現の促進、具体的な手順や技術要件の詳細化、利用ガイドの強化が含まれます。

## New features
特に新しい機能の追加はありませんが、既存の機能をより効果的に利用できるように、説明やガイダンスの明確化が進められています。

## Breaking changes
破壊的変更はないため、ユーザーが現行のワークフローに大きな影響を受けることはありません。

## Other updates
- セマンティックランキングのクイックスタートガイドと自動補完提案に関する説明が改善されました。
- サービスポータルやプライベートリンクの接続方法に関する記事が改良されています。
- 検索サービスの制限とSKUティアに関する情報も更新されました。

# Insights
この一連の更新は、Azure AI Searchを最大限に活用するための情報をより詳細でわかりやすくすることを目的としています。ユーザーは、サービスを効果的に構成し、最新の技術仕様に基づいてインフラを設計できるようになります。

例えば、`search-get-started-semantic.md` ファイルの変更では、抽象的だった「セマンティックランカーの利用法」について、より具体的な手順が追加されました。これにより企業や開発者が最も優れた検索結果を示すランキング機能を容易に実装できるようになっています。さらに、`search-sku-tier.md`ファイルの更新により、各ティアの違いが明確に説明され、自分のニーズに合ったプラン選定を支援しています。

ユーザーがこれらの情報を基にサービスをより効果的に利用し、ビジネス上の意思決定をより迅速に行えるようになることが期待されます。また、継続的なドキュメントの品質向上によって、トラブルシューティングや学習曲線を緩和し、開発時の混乱を避けることができるでしょう。このように、ドキュメントの更新は小規模であっても、ユーザー体験と知識の強化につながる重要な改善をもたらします。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [dotnet-semantic.md](#item-2d423d) | minor update | 小さな修正と日付の更新 | modified | 7 | 7 | 14 | 
| [python-semantic.md](#item-4cc2ee) | minor update | 小さな修正と日付の更新 | modified | 7 | 7 | 14 | 
| [search-add-autocomplete-suggestions.md](#item-0a43e0) | minor update | 自動補完提案に関する内容の更新 | modified | 26 | 26 | 52 | 
| [search-create-service-portal.md](#item-f90159) | minor update | サービスポータルに関する記事のマイナーな修正 | modified | 8 | 9 | 17 | 
| [search-get-started-semantic.md](#item-2b3902) | minor update | セマンティックランキングのクイックスタートガイドの修正 | modified | 9 | 9 | 18 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | プライベートリンクを通じた接続方法に関する説明の更新 | modified | 6 | 2 | 8 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索サービスの制限およびクオータに関する情報の更新 | modified | 8 | 3 | 11 | 
| [search-sku-tier.md](#item-7686b8) | minor update | SKUティアに関する情報の更新 | modified | 6 | 8 | 14 | 
| [search-traffic-analytics.md](#item-c76f2f) | minor update | 検索トラフィック分析のテレメトリに関する情報の更新 | modified | 20 | 20 | 40 | 


# Modified Contents
## articles/search/includes/quickstarts/dotnet-semantic.md{#item-2d423d}

<details>
<summary>Diff</summary>
````diff
@@ -5,12 +5,12 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: include
-ms.date: 01/02/2024
+ms.date: 10/22/2024
 ---
 
-Build a console application using the [**Azure.Search.Documents**](/dotnet/api/overview/azure/search.documents-readme) client library to add semantic ranking to an existing search index. 
+Build a console application by using the [**Azure.Search.Documents**](/dotnet/api/overview/azure/search.documents-readme) client library to add semantic ranking to an existing search index.
 
-Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-semantic-search/SemanticSearchQuickstart) to start with a finished project or follow these steps to create your own.
+Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-semantic-search/SemanticSearchQuickstart) to start with a finished project.
 
 #### Set up your environment
 
@@ -20,13 +20,13 @@ Alternatively, you can [download the source code](https://github.com/Azure-Sampl
 
 1. Select **Browse**.
 
-1. Search for [Azure.Search.Documents package](https://www.nuget.org/packages/Azure.Search.Documents/) and select the latest stable version.
+1. Search for the [Azure.Search.Documents package](https://www.nuget.org/packages/Azure.Search.Documents/) and select the latest stable version.
 
 1. Select **Install** to add the assembly to your project and solution.
 
 #### Create a search client
 
-1. In **Program.cs**, add the following `using` directives.
+1. In *Program.cs*, add the following `using` directives.
 
    ```csharp
    using Azure;
@@ -36,9 +36,9 @@ Alternatively, you can [download the source code](https://github.com/Azure-Sampl
    using Azure.Search.Documents.Models;
    ```
 
-1. Create two clients: [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient) creates the index, and [SearchClient](/dotnet/api/azure.search.documents.searchclient) loads and queries an existing index. Both need the service endpoint and an admin API key for authentication with create/delete rights.
+1. Create two clients: [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient) creates the index, and [SearchClient](/dotnet/api/azure.search.documents.searchclient) loads and queries an existing index.
 
-   Because the code builds out the URI for you, specify just the search service name in the "serviceName" property.
+    Both clients need the service endpoint and an admin API key for authentication with create/delete rights. However, the code builds out the URI for you, so specify only the search service name for the `serviceName` property. Don't include `https://` or `.search.windows.net`.
 
    ```csharp
     static void Main(string[] args)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "小さな修正と日付の更新"
}
```

### Explanation
この変更は、`dotnet-semantic.md` ファイルにおけるいくつかの文言の修正と日付の更新を含んでいます。具体的には、ある言い回しの明確化や文法的な微調整が行われ、より自然な日本語表現が促進されています。また、文書の日付が「2024年1月2日」から「2024年10月22日」へと更新されました。このような変更は、情報の正確性を保ち、ユーザーに対して最新の内容を提供するために重要です。全体として、追加された文と削除された文の数は同じであり、全体的には内容を損なわずに改善が図られています。

## articles/search/includes/quickstarts/python-semantic.md{#item-4cc2ee}

<details>
<summary>Diff</summary>
````diff
@@ -5,12 +5,12 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: include
-ms.date: 03/11/2024
+ms.date: 10/22/2024
 ---
 
-Use a Jupyter notebook and the [**azure-search-documents**](/python/api/overview/azure/search-documents-readme) library in the Azure SDK for Python to learn about semantic ranking. 
+Use a Jupyter notebook and the [**azure-search-documents**](/python/api/overview/azure/search-documents-readme) library in the Azure SDK for Python to learn about semantic ranking.
 
-Alternatively, [download and run a finished notebook](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search).
+Alternatively, you can [download and run a finished notebook](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search).
 
 #### Set up your environment
 
@@ -22,7 +22,7 @@ We recommend a virtual environment for this quickstart:
 
 1. Create a new ipynb file.
 
-1. Open the Command Palette (Ctrl+Shift+P).
+1. Open the Command Palette by using **Ctrl+Shift+P**.
 
 1. Search for **Python: Create Environment**.
 
@@ -42,7 +42,7 @@ It can take a minute to set up. If you run into problems, see [Python environmen
     ! pip install python-dotenv --quiet
     ```
 
-1. Provide endpoint and API keys:
+1. Provide your endpoint and API keys:
 
     ```python
     search_endpoint: str = "PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE"
@@ -238,9 +238,9 @@ for result in results:
 
 #### Run a text query
 
-For comparison purposes, run text query with BM25 relevance scoring. Full text search is invoked when you provide a query string. The response consists of ranked results, where higher scores are awarded to documents having more instances of matching terms, or more important terms.
+For comparison purposes, run a text query with BM25 relevance scoring. Full text search is invoked when you provide a query string. The response consists of ranked results, where higher scores are awarded to documents having more instances of matching terms, or more important terms.
 
-In this query for "what hotel has a good restaurant on site", Sublime Cliff Hotel comes out on top because its description includes "site". Terms that occur infrequently raise the search score of the document. 
+In this query for *what hotel has a good restaurant on site*, Sublime Cliff Hotel comes out on top because its description includes *site*. Terms that occur infrequently raise the search score of the document. 
 
 ```python
 # Run a text query (returns a BM25-scored result set)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "小さな修正と日付の更新"
}
```

### Explanation
この変更は、`python-semantic.md` ファイルにおけるいくつかの文言の修正と日付の更新を含んでいます。具体的には、表現の明確化や情報の一貫性を向上させるために軽微な修正が行われています。例えば、Command Paletteを開く手順を「**Ctrl+Shift+P**」を使用して確認するように修正し、APIキーの説明にもユーザーを意識した表現「your」を加えることで、より親しみやすくなっています。また、文書の日付が「2024年3月11日」から「2024年10月22日」へと更新されました。これにより、最新の情報が提供されることになります。全体として、表現の洗練化が進められ、ユーザーにとっての理解を助ける内容となっています。

## articles/search/search-add-autocomplete-suggestions.md{#item-0a43e0}

<details>
<summary>Diff</summary>
````diff
@@ -10,22 +10,22 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 02/22/2024
+ms.date: 10/22/2024
 ---
 
 # Add autocomplete and search suggestions in client apps
 
-Search-as-you-type is a common technique for improving query productivity. In Azure AI Search, this experience is supported through *autocomplete*, which finishes a term or phrase based on partial input (completing "micro" with "microchip", "microscope", "microsoft", and any other micro matches). A second user experience is *suggestions*, or a short list of matching documents (returning book titles with an ID so that you can link to a detail page about that book). Both autocomplete and suggestions are predicated on a match in the index. The service won't offer autocompleted queries or suggestions that return zero results.
+Search-as-you-type is a common technique for improving query productivity. In Azure AI Search, this experience is supported through *autocomplete*, which finishes a term or phrase based on partial input (for example, completing *micro* with *microchip*, *microscope*, *microsoft*, and any other micro matches). A second user experience is *suggestions*, which produces a short list of matching documents (for example, returning book titles with an ID so that you can link to a detail page about that book). Both autocomplete and suggestions are predicated on a match in the index. The service doesn't offer autocompleted queries or suggestions that return zero results.
 
 To implement these experiences in Azure AI Search:
 
 + Add a `suggester` to an index schema.
-+ Build a query that calls the [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) or [Suggestions](/rest/api/searchservice/documents/suggest-post) API on the request.
++ Build a query that calls the [Autocomplete API](/rest/api/searchservice/documents/autocomplete-post) or [Suggestions API](/rest/api/searchservice/documents/suggest-post) on the request.
 + Add a UI control to handle search-as-you-type interactions in your client app. We recommend using an existing JavaScript library for this purpose.
 
-In Azure AI Search, autocompleted queries and suggested results are retrieved from the search index, from selected fields that you register with a suggester. A suggester is part of the index, and it specifies which fields provide content that either completes a query, suggests a result, or does both. When the index is created and loaded, a suggester data structure is created internally to store prefixes used for matching on partial queries. For suggestions, choosing suitable fields that are unique, or at least not repetitive, is essential to the experience. For more information, see [Create a suggester](index-add-suggesters.md).
+In Azure AI Search, autocompleted queries and suggested results are retrieved from the search index, from selected fields that you register with a suggester. A suggester is part of the index, and it specifies which fields provide content that either completes a query, suggests a result, or does both. When the index is created and loaded, a suggester data structure is created internally to store prefixes used for matching on partial queries. For suggestions, choosing suitable fields that are unique, or at least not repetitive, is essential to the experience. For more information, see [Configure a suggester](index-add-suggesters.md).
 
-The remainder of this article is focused on queries and client code. It uses JavaScript and C# to illustrate key points. REST API examples are used to concisely present each operation. For end-to-end code samples, see [Next steps](#next-steps).
+The remainder of this article is focused on queries and client code. It uses JavaScript and C# to illustrate key points. REST API examples are used to concisely present each operation. For end-to-end code samples, see [Add search to a web site with .NET](tutorial-csharp-overview.md).
 
 ## Set up a request
 
@@ -39,13 +39,13 @@ POST /indexes/myxboxgames/docs/autocomplete?search&api-version=2024-07-01
 }
 ```
 
-The "suggesterName" gives you the suggester-aware fields used to complete terms or suggestions. For suggestions in particular, the field list should be composed of those that offer clear choices among matching results. On a site that sells computer games, the field might be the game title.
+The `suggesterName` parameter gives you the suggester-aware fields used to complete terms or suggestions. For suggestions in particular, the field list should be composed of suggestions that offer clear choices among matching results. On a site that sells computer games, the field might be the game title.
 
-The "search" parameter provides the partial query, where characters are fed to the query request through the jQuery Autocomplete control. In the above example, "minecraf" is a static illustration of what the control might pass in.
+The `search` parameter provides the partial query, where characters are fed to the query request through the jQuery Autocomplete control. In the previous example, *minecraf* is a static illustration of what the control might pass in.
 
 The APIs don't impose minimum length requirements on the partial query; it can be as little as one character. However, jQuery Autocomplete provides a minimum length. A minimum of two or three characters is typical.
 
-Matches are on the beginning of a term anywhere in the input string. Given "the quick brown fox", both autocomplete and suggestions match on partial versions of "the", "quick", "brown", or "fox" but not on partial infix terms like "rown" or "ox". Furthermore, each match sets the scope for downstream expansions. A partial query of "quick br" will match on "quick brown" or "quick bread", but neither "brown" or "bread" by themselves would be a match unless "quick" precedes them.
+Matches are on the beginning of a term anywhere in the input string. Given *the quick brown fox*, both autocomplete and suggestions match on partial versions of *the*, *quick*, *brown*, or *fox* but not on partial infix terms like *rown* or *ox*. Furthermore, each match sets the scope for downstream expansions. A partial query of *quick br* matches on *quick brown* or *quick bread*, but neither *brown* or *bread* by themselves would be a match unless quick* precedes them.
 
 ### APIs for search-as-you-type
 
@@ -58,13 +58,13 @@ Follow these links for the REST and .NET SDK reference pages:
 
 ## Structure a response
 
-Responses for autocomplete and suggestions are what you might expect for the pattern: [Autocomplete](/rest/api/searchservice/documents/autocomplete-post#responses) returns a list of terms, [Suggestions](/rest/api/searchservice/documents/suggest-post#response) returns terms plus a document ID so that you can fetch the document (use the [Lookup Document](/rest/api/searchservice/documents/get) API to fetch the specific document for a detail page).
+Responses for autocomplete and suggestions are what you might expect for the pattern: [Autocomplete](/rest/api/searchservice/documents/autocomplete-post#responses) returns a list of terms, [Suggestions](/rest/api/searchservice/documents/suggest-post#response) returns terms plus a document ID so that you can fetch the document (use the [Lookup Document API](/rest/api/searchservice/documents/get) to fetch the specific document for a detail page).
 
 Responses are shaped by the parameters on the request:
 
-+ For Autocomplete, set the [autocompleteMode](/rest/api/searchservice/documents/autocomplete-post#autocompletemode) to determine whether text completion occurs on one or two terms. 
++ For autocomplete, set the [autocompleteMode](/rest/api/searchservice/documents/autocomplete-post#autocompletemode) to determine whether text completion occurs on one or two terms. 
 
-+ For Suggestions, set [$select](/rest/api/searchservice/documents/suggest-post#request-body) to return fields containing unique or differentiating values, such as names and description. Avoid fields that contain duplicate values (such as a category or city).
++ For suggestions, set [$select](/rest/api/searchservice/documents/suggest-post#request-body) to return fields containing unique or differentiating values, such as names and description. Avoid fields that contain duplicate values (such as a category or city).
 
 The following parameters apply to both autocomplete and suggestions, but are more applicable to suggestions, especially when a suggester includes multiple fields.
 
@@ -80,29 +80,29 @@ Autofilling a query term or dropping down a list of matching links requires user
 
 Although you could write this code natively, it's easier to use functions from existing JavaScript library, such as one of the following. 
 
-+ [Autocomplete widget (jQuery UI)](https://jqueryui.com/autocomplete/) appears in the Suggestion code snippet. You can create a search box, and then reference it in a JavaScript function that uses the Autocomplete widget. Properties on the widget set the source (an autocomplete or suggestions function), minimum length of input characters before action is taken, and positioning.
++ [Autocomplete widget (jQuery UI)](https://jqueryui.com/autocomplete/) appears in the suggestion code snippet. You can create a search box, and then reference it in a JavaScript function that uses the autocomplete widget. Properties on the widget set the source (an autocomplete or suggestions function), minimum length of input characters before action is taken, and positioning.
 
-+ [XDSoft Autocomplete plug-in](https://xdsoft.net/jqplugins/autocomplete/) appears in the Autocomplete code snippet.
++ [XDSoft Autocomplete plug-in](https://xdsoft.net/jqplugins/autocomplete/) appears in the autocomplete code snippet.
 
-+ [suggestions](https://www.npmjs.com/package/suggestions) appears in the [Add search to web sites tutorial](tutorial-csharp-overview.md) and code sample.
++ [Suggestions](https://www.npmjs.com/package/suggestions) appears in the [Add search to web sites tutorial](tutorial-csharp-overview.md) and code sample.
 
-Use these libraries in the client to create a search box supporting both suggestions and autocomplete. Inputs collected in the search box can then be paired with suggestions and autocomplete actions on the search service.
+Use these libraries in the client to create a search box that supports both suggestions and autocomplete. Inputs collected in the search box can then be paired with suggestions and autocomplete actions on the search service.
 
 ## Suggestions
 
 This section walks you through an implementation of suggested results, starting with the search box definition. It also shows how and script that invokes the first JavaScript autocomplete library referenced in this article.
 
 ### Create a search box
 
-Assuming the [jQuery UI Autocomplete library](https://jqueryui.com/autocomplete/) and an MVC project in C#, you could define the search box using JavaScript in the **Index.cshtml** file. The library adds the search-as-you-type interaction to the search box by making asynchronous calls to the MVC controller to retrieve suggestions.
+Assuming the [jQuery UI Autocomplete library](https://jqueryui.com/autocomplete/) and an MVC project in C#, you could define the search box using JavaScript in the *Index.cshtml* file. The library adds the search-as-you-type interaction to the search box by making asynchronous calls to the MVC controller to retrieve suggestions.
 
-In **Index.cshtml** under the folder \Views\Home, a line to create a search box might be as follows:
+In *Index.cshtml* inside the folder *\Views\Home*, a line to create a search box might be as follows:
 
 ```html
 <input class="searchBox" type="text" id="searchbox1" placeholder="search">
 ```
 
-This example is a simple input text box with a class for styling, an ID to be referenced by JavaScript, and placeholder text.  
+This example is a simple input text box with a class for styling, an ID to be referenced by JavaScript, and placeholder text.
 
 Within the same file, embed JavaScript that references the search box. The following function calls the Suggest API, which requests suggested matching documents based on partial term inputs:
 
@@ -119,9 +119,9 @@ $(function () {
 });
 ```
 
-The `source` tells the jQuery UI Autocomplete function where to get the list of items to show under the search box. Since this project is an MVC project, it calls the **Suggest** function in **HomeController.cs** that contains the logic for returning query suggestions. This function also passes a few parameters to control highlights, fuzzy matching, and term. The autocomplete JavaScript API adds the term parameter.
+The `source` tells the jQuery UI Autocomplete function where to get the list of items to show under the search box. Since this project is an MVC project, it calls the `Suggest` function in *HomeController.cs* that contains the logic for returning query suggestions. This function also passes a few parameters to control highlights, fuzzy matching, and term. The autocomplete JavaScript API adds the term parameter.
 
-The `minLength: 3` ensures that recommendations will only be shown when there are at least three characters in the search box.
+The `minLength: 3` ensures that recommendations are only shown when there are at least three characters in the search box.
 
 ### Enable fuzzy matching
 
@@ -133,15 +133,15 @@ source: "/home/suggest?highlights=false&fuzzy=true&",
 
 ### Enable highlighting
 
-Highlighting applies font style to the characters in the result that correspond to the input. For example, if the partial input is "micro", the result would appear as **micro**soft, **micro**scope, and so forth. Highlighting is based on the HighlightPreTag and HighlightPostTag parameters, defined inline with the Suggestion function.
+Highlighting applies font style to the characters in the result that correspond to the input. For example, if the partial input is *micro*, the result would appear as **micro**soft, **micro**scope, and so forth. Highlighting is based on the `HighlightPreTag` and `HighlightPostTag` parameters, defined inline with the `Suggest` function.
 
 ```javascript
 source: "/home/suggest?highlights=true&fuzzy=true&",
 ```
 
 ### Suggest function
 
-If you're using C# and an MVC application, **HomeController.cs** file under the Controllers directory is where you might create a class for suggested results. In .NET, a Suggest function is based on the [SuggestAsync method](/dotnet/api/azure.search.documents.searchclient.suggestasync). For more information about the .NET SDK, see [How to use Azure AI Search from a .NET Application](search-howto-dotnet-sdk.md).
+If you're using C# and an MVC application, the *HomeController.cs* file in the *Controllers* directory is where you might create a class for suggested results. In .NET, a `Suggest` function is based on the [SuggestAsync method](/dotnet/api/azure.search.documents.searchclient.suggestasync). For more information about the .NET SDK, see [How to use Azure AI Search from a .NET Application](search-howto-dotnet-sdk.md).
 
 The `InitSearch` method creates an authenticated HTTP index client to the Azure AI Search service. Properties on the [SuggestOptions](/dotnet/api/azure.search.documents.suggestoptions) class determine which fields are searched and returned in the results, the number of matches, and whether fuzzy matching is used. 
 
@@ -177,11 +177,11 @@ public async Task<ActionResult> SuggestAsync(bool highlights, bool fuzzy, string
 }
 ```
 
-The SuggestAsync function takes two parameters that determine whether hit highlights are returned or fuzzy matching is used in addition to the search term input. Up to eight matches can be included in suggested results. The method creates a [SuggestOptions object](/dotnet/api/azure.search.documents.suggestoptions), which is then passed to the Suggest API. The result is then converted to JSON so it can be shown in the client.
+The `SuggestAsync` function takes two parameters that determine whether hit highlights are returned or fuzzy matching is used in addition to the search term input. Up to eight matches can be included in suggested results. The method creates a [SuggestOptions object](/dotnet/api/azure.search.documents.suggestoptions), which is then passed to the Suggest API. The result is then converted to JSON so it can be shown in the client.
 
 ## Autocomplete
 
-So far, the search UX code has been centered on suggestions. The next code block shows autocomplete, using the XDSoft jQuery UI Autocomplete function, passing in a request for Azure AI Search autocomplete. As with the suggestions, in a C# application, code that supports user interaction goes in **index.cshtml**.
+So far, the search UX code has been centered on suggestions. The next code block shows autocomplete, using the XDSoft jQuery UI Autocomplete function, passing in a request for Azure AI Search autocomplete. As with the suggestions, in a C# application, code that supports user interaction goes in *index.cshtml*.
 
 ```javascript
 $(function () {
@@ -220,7 +220,7 @@ $(function () {
 
 ### Autocomplete function
 
-Autocomplete is based on the [AutocompleteAsync method](/dotnet/api/azure.search.documents.searchclient.autocompleteasync). As with suggestions, this code block would go in the **HomeController.cs** file.
+Autocomplete is based on the [AutocompleteAsync method](/dotnet/api/azure.search.documents.searchclient.autocompleteasync). As with suggestions, this code block would go in the *HomeController.cs* file.
 
 ```csharp
 public async Task<ActionResult> AutoCompleteAsync(string term)
@@ -244,7 +244,7 @@ public async Task<ActionResult> AutoCompleteAsync(string term)
 
 The Autocomplete function takes the search term input. The method creates an [AutoCompleteParameters object](/rest/api/searchservice/documents/autocomplete-post). The result is then converted to JSON so it can be shown in the client.
 
-## Next steps
+## Next step
 
 The following tutorial demonstrates a search-as-you-type experience.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "自動補完提案に関する内容の更新"
}
```

### Explanation
この変更は、`search-add-autocomplete-suggestions.md` ファイルにおいて、主に自動補完と提案に関する説明を改良し、日付の更新も行われました。具体的には、文脈をより明確にするための表現の修正や、技術用語の一貫性を保つための微調整が加えられています。

変更内容の一部として、文に「for example」や「which produces」などのフレーズが追加され、抽象的な表現が具体的になっています。また、「suggester」の設定に関する情報や、提案機能を実装するための手順についても、より明確でわかりやすい説明が提供されています。文書の日付は「2024年2月22日」から「2024年10月22日」に更新され、最新の情報を示すようになりました。

全体として、技術的な正確性と説明の明瞭性が向上されており、ユーザーが自動補完機能と提案機能を効果的に利用するためのガイダンスが強化されています。

## articles/search/search-create-service-portal.md{#item-f90159}

<details>
<summary>Diff</summary>
````diff
@@ -18,15 +18,15 @@ ms.date: 10/17/2024
 
 [**Azure AI Search**](search-what-is-azure-search.md) is an information retrieval platform for the enterprise. It supports traditional search and conversational AI-driven search for "chat with your data" experiences over your proprietary content.
 
-The easiest way to create a service is using the [Azure portal](https://portal.azure.com/), which is covered in this article. 
+The easiest way to create a service is using the [Azure portal](https://portal.azure.com/), which is covered in this article.
 
 You can also use [Azure PowerShell](search-manage-powershell.md#create-or-delete-a-service), [Azure CLI](search-manage-azure-cli.md#create-or-delete-a-service), the [Management REST API](search-manage-rest.md#create-or-update-a-service), an [Azure Resource Manager service template](search-get-started-arm.md), a [Bicep file](search-get-started-bicep.md), or [Terraform](search-get-started-terraform.md).
 
 [![Animated GIF](./media/search-create-service-portal/AnimatedGif-AzureSearch-small.gif)](./media/search-create-service-portal/AnimatedGif-AzureSearch.gif#lightbox)
 
 ## Before you start
 
-A few service properties are fixed for the lifetime of the service. Before creating the service, decide on a name, region, and tier. 
+A few service properties are fixed for the lifetime of the service. Before creating the service, decide on a name, region, and tier.
 
 + [Service name](#name-the-service) becomes part of the URL endpoint. The name must be unique and it must conform to naming rules.
 
@@ -40,7 +40,7 @@ Paid (or billable) search occurs when you choose a billable tier (Basic or highe
 
 To try Azure AI Search for free, [open a trial subscription](https://azure.microsoft.com/pricing/free-trial/?WT.mc_id=A261C142F) and then create your search service by choosing the **Free** tier. You can have one free search service per Azure subscription. Free search services are intended for short-term evaluation of the product for nonproduction applications. Generally, you can complete all of the quickstarts and most tutorials, except for those featuring semantic ranker (it requires a billable service). Free services that are inactive for an extended period of time can be deleted by Microsoft to make room for other services.
 
-Alternatively, you can use free credits to try out paid Azure services. With this approach, you can create your search service at **Basic** or higher to get more capacity. Your credit card is never charged unless you explicitly change your settings and ask to be charged. Another approach is to [activate Azure credits in a Visual Studio subscription](https://azure.microsoft.com/pricing/member-offers/msdn-benefits-details/?WT.mc_id=A261C142F). A Visual Studio subscription gives you credits every month you can use for paid Azure services. 
+Alternatively, you can use free credits to try out paid Azure services. With this approach, you can create your search service at **Basic** or higher to get more capacity. Your credit card is never charged unless you explicitly change your settings and ask to be charged. Another approach is to [activate Azure credits in a Visual Studio subscription](https://azure.microsoft.com/pricing/member-offers/msdn-benefits-details/?WT.mc_id=A261C142F). A Visual Studio subscription gives you credits every month you can use for paid Azure services.
 
 ## Find the Azure AI Search offering
 
@@ -87,7 +87,7 @@ Service name requirements:
 ## Choose a region
 
 > [!IMPORTANT]
-> Due to high demand, Azure AI Search is currently unavailable for new instances in some regions. 
+> Due to high demand, Azure AI Search is currently unavailable for new instances in some regions.
 
 If you use multiple Azure services, putting all of them in the same region minimizes or voids bandwidth charges. There are no charges for data egress among same-region services.
 
@@ -109,7 +109,7 @@ Generally, choose a region near you, unless the following considerations apply:
 
 1. Do you need [AI enrichment](cognitive-search-concept-intro.md), [integrated data chunking and vectorization](vector-search-integrated-vectorization.md), or [multimodal image search](search-get-started-portal-image-search.md)? Azure AI Search, Azure OpenAI, and Azure AI multiservice must coexist in the same region.
 
-   + Start with [Azure OpenAI regions](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability) because it has the most variability. Azure OpenAI provides embedding models and chat models for RAG and integrated vectorization. 
+   + Start with [Azure OpenAI regions](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability) because it has the most variability. Azure OpenAI provides embedding models and chat models for RAG and integrated vectorization.
 
    + Check [Azure AI Search regions](search-region-support.md) for a match to your Azure OpenAI region. If you're using OCR, entity recognition, or other skills backed by Azure AI, the **AI Integration** column indicates whether Azure AI multiservice is in the same region as Azure AI Search.
 
@@ -132,13 +132,13 @@ Basic and Standard are the most common choices for production workloads, but man
 
 :::image type="content" source="media/search-create-service-portal/select-pricing-tier.png" lightbox="media/search-create-service-portal/select-pricing-tier.png" alt-text="Screenshot of Select a pricing tier page." border="true":::
 
-Search services created after April 3, 2024 have larger partitions and higher vector quotas at every billable tier. 
+Search services created after April 3, 2024 have larger partitions and higher vector quotas at every billable tier.
 
 Remember, a pricing tier can't be changed once the service is created. If you need a higher or lower tier, you should re-create the service.
 
 ## Create your service
 
-After you've provided the necessary inputs, go ahead and create the service. 
+After you've provided the necessary inputs, go ahead and create the service.
 
 :::image type="content" source="media/search-create-service-portal/new-service3.png" lightbox="media/search-create-service-portal/new-service3.png" alt-text="Screenshot of the Review and create the service page." border="true":::
 
@@ -151,7 +151,7 @@ Your service is deployed within minutes. You can monitor progress through Azure
 Unless you're using the portal, programmatic access to your new service requires that you provide the URL endpoint and an authenticated connection. You can use either or both of these options:
 
 + [Connect using key-based authentication](search-security-api-keys.md)
-+ [Connect using Azure roles](search-security-rbac.md) 
++ [Connect using Azure roles](search-security-rbac.md)
 
 1. When setting up a programmatic connection, you need the search service endpoint. On the **Overview** page, locate and copy the URL endpoint on the right side of the page.
 
@@ -206,7 +206,6 @@ Azure AI Search restricts the [number of search services](search-limits-quotas-c
 You must have Owner or Contributor permissions on the subscription to request quota.
 Depending on region and datacenter capacity, you can automatically request more quota to add services to your subscription. If the request fails, you should either decrease the number or file a support ticket. For a large increase in quota, such as more than 30 extra services, you should expect a one-month turnaround.
 
-
 1. Sign in to the Azure portal, search for "quotas" in your dashboard, and then select the **Quotas** service.
 
    :::image type="content" source="media/search-create-service-portal/quota-search.png" lightbox="media/search-create-service-portal/quota-search.png" alt-text="Screenshot of the quota search term and Quotas service in the results.":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービスポータルに関する記事のマイナーな修正"
}
```

### Explanation
この変更は、`search-create-service-portal.md` ファイルに関するもので、サービス作成に関する情報を更新し、文言を一部修正しました。主な内容は、文の明確化と冗長な表現の削除による表記の統一です。具体的には、いくつかの文がよりシンプルで直接的な表現に変更されており、特にオンラインリソースへのリンクの説明が強化されています。

また、記事内の重要な情報が強調され、読者にとっての理解を助けるように配慮されています。記事の日付も更新され、最新の情報を提供していることが明示されました。全体として、サービス作成の手順や要件についての理解を深めるための改良が施されています。

## articles/search/search-get-started-semantic.md{#item-2b3902}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: 'Quickstart: semantic ranking'
 titleSuffix: Azure AI Search
-description: Change an existing index to use semantic ranker.
+description: Change an existing index to use semantic ranker to rescore search results and promote the most semantically relevant matches.
 author: HeidiSteen
 manager: nitinme
 ms.author: heidist
@@ -11,31 +11,31 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: quickstart
-ms.date: 03/11/2024
+ms.date: 10/22/2024
 ---
 
 # Quickstart: Semantic ranking with .NET or Python
 
-In Azure AI Search, [semantic ranker](semantic-search-overview.md) is query-side functionality that uses machine reading comprehension from Microsoft to rescore search results, promoting the most semantically relevant matches to the top of the list. Depending on the content and the query, semantic ranking can [significantly improve search relevance](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-outperforming-vector-search-with-hybrid/ba-p/3929167), with minimal work for the developer.
+In Azure AI Search, [semantic ranking](semantic-search-overview.md) is query-side functionality that uses machine reading comprehension from Microsoft to rescore search results, promoting the most semantically relevant matches to the top of the list. Depending on the content and the query, semantic ranking can [significantly improve search relevance](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-outperforming-vector-search-with-hybrid/ba-p/3929167), with minimal work for the developer.
 
 This quickstart walks you through the index and query modifications that invoke semantic ranker.
 
 > [!NOTE]
-> Looking for an Azure AI Search solution with ChatGPT interaction? See [this demo](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md) or [this accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator) for details.
+> For an Azure AI Search solution example with ChatGPT interaction, see [this demo](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md) or [this accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator).
 
 ## Prerequisites
 
-+ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/).
++ An Azure account with an active subscription. You can [create an account for free](https://azure.microsoft.com/free/).
 
-+ Azure AI Search, at Basic tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
++ An Azure AI Search resource, at Basic tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
 + An API key and search service endpoint. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
 
-  In **Overview**, copy the URL and save it to Notepad for a later step. An example endpoint might look like `https://mydemo.search.windows.net`.
+  In **Overview**, copy the URL and save it for a later step. An example endpoint might look like `https://mydemo.search.windows.net`.
 
   In **Keys**, copy and save an admin key for full rights to create and delete objects. There are two interchangeable primary and secondary keys. Choose either one.
 
-  ![Get an HTTP endpoint and access key](media/search-get-started-rest/get-url-key.png "Get an HTTP endpoint and access key")
+  :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot showing where to find your search service's HTTP endpoint and access key.":::
 
 ## Add semantic ranking
 
@@ -63,7 +63,7 @@ You can find and manage resources in the portal, using the **All resources** or
 
 ## Next steps
 
-In this quickstart, you learned how to invoke semantic ranker on an existing index. We recommend trying semantic ranker on your own indexes as a next step. However, if you want to continue with demos, visit the following link.
+In this quickstart, you learned how to invoke semantic ranking on an existing index. We recommend trying semantic ranking on your own indexes as a next step. However, if you want to continue with demos, visit the following link.
 
 > [!div class="nextstepaction"]
 > [Tutorial: Add search to web apps](tutorial-csharp-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランキングのクイックスタートガイドの修正"
}
```

### Explanation
この変更は、`search-get-started-semantic.md` ファイルの内容に対するもので、特にセマンティックランキングに関するクイックスタートガイドの説明が改善されました。具体的には、説明文が詳細かつ明確になり、より具体的な表現が用いられています。

例えば、「既存のインデックスを使ってセマンティックランカーを利用する」という内容から、「最もセマンティックに関連性の高い結果を上位に表示するために、既存のインデックスを変更する」といった具体的な表現に変更されています。また、日付も更新され、最新の情報を反映する形になっています。

さらに、注意書きや必須条件のセクションでは、必要なリソースや手順が整理され、理解しやすくなっています。視覚的な情報も更新され、スクリーンショットの説明が強化されているため、ユーザーがセマンティックランキングの使用をよりスムーズに進められるよう配慮されています。全体として、内容が明確になり、実行可能な手順が容易に把握できるようになっています。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: mrcarter8
 ms.author: mcarter
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 10/16/2024
+ms.date: 10/22/2024
 ---
 
 # Make outbound connections through a shared private link
@@ -66,7 +66,11 @@ When evaluating shared private links for your scenario, remember these constrain
 
 ## Prerequisites
 
-+ An Azure AI Search at the Basic tier or higher. If you're using [AI enrichment](cognitive-search-concept-intro.md) and skillsets, the tier must be Standard 2 (S2) or higher. See [Service limits](search-limits-quotas-capacity.md#shared-private-link-resource-limits) for details.
++ For [integrated vectorization](vector-search-integrated-vectorization.md) only, outbound connections through shared private link are supported on all billable tiers, only on services [created after April 3, 2024](vector-search-index-size.md#how-to-check-service-creation-date) located in regions providing [higher capacity](search-limits-quotas-capacity.md#partition-storage-gb). 
+
++ For [AI enrichment](cognitive-search-concept-intro.md), skillset processing that doesn't include an embedding skill and in services [created before April 3, 2024](vector-search-index-size.md#how-to-check-service-creation-date), Azure AI Search must be Standard 2 (S2) or higher.
+
++ For all other use cases, that don't involve skillsets, Azure AI Search can be Basic or higher.
 
 + An Azure PaaS resource from the following list of [supported resource types](#supported-resource-types), configured to run in a virtual network.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートリンクを通じた接続方法に関する説明の更新"
}
```

### Explanation
この変更は、`search-indexer-howto-access-private.md` ファイルにおけるプライベートリンクを通じた接続方法に関する情報の更新です。主な変更点は、Azure AI Searchのサービス要件に関する説明が強化されたことです。

具体的には、共有プライベートリンクに関する条件がより詳細に記載されています。例えば、特定の機能（統合ベクトル化やAIのエンリッチメント）に対する要件が明確に分けられており、サービスの作成日や地域に基づく条件が加えられました。このように、異なる利用ケースごとの要件が整理され、ユーザーが自分のシナリオに最適な設定を理解しやすくなっています。

また、最終更新日が最新のものに変更されているほか、Azureの設定に関して必要なリソースの要件も追加されています。全体として、プライベートリンクを介した接続の理解が深まるように情報が整理されており、ユーザーが計画を立てやすくなるようになっています。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 10/17/2024
+ms.date: 10/22/2024
 ms.custom:
   - references_regions
   - build-2024
@@ -150,12 +150,17 @@ Indexers can access other Azure resources [over private endpoints](search-indexe
 |----------|------|-------|----|----|----|-------|----|----|
 | Private endpoint indexer support | No | Yes | Yes | Yes | Yes | No | Yes | Yes |
 | Private endpoint support for indexers with a skillset<sup>1</sup> | No | No | No | Yes | Yes | No | Yes | Yes |
+| Private endpoint support for indexers with a skillset and integrated vectorization <sup>2</sup> | No | Yes | Yes | Yes | Yes | No | Yes | Yes |
 | Maximum private endpoints | N/A | 10 or 30 | 100 | 400 | 400 | N/A | 20 | 20 |
-| Maximum distinct resource types<sup>2</sup> | N/A | 4 | 7 | 15 | 15 | N/A | 4 | 4 |
+| Maximum distinct resource types<sup>3</sup> | N/A | 4 | 7 | 15 | 15 | N/A | 4 | 4 |
 
 <sup>1</sup> AI enrichment and image analysis are computationally intensive and consume disproportionate amounts of available processing power. For this reason, private connections are disabled on lower tiers to ensure the performance and stability of the search service itself.
 
-<sup>2</sup> The number of distinct resource types are computed as the number of unique `groupId` values used across all shared private link resources for a given search service, irrespective of the status of the resource.
+<sup>2</sup> High-capacity services created after April 3, 2024 in the regions listed under [Partition Storage](search-limits-quotas-capacity.md#partition-storage-gb) and running [integrated vectorization](vector-search-integrated-vectorization.md) workloads at indexing time support shared private links in paid tiers. The system must detect at least a skill that is embedding data.
+
+<sup>3</sup> The number of distinct resource types are computed as the number of unique `groupId` values used across all shared private link resources for a given search service, irrespective of the status of the resource.
+
+
 
 ## Synonym limits
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスの制限およびクオータに関する情報の更新"
}
```

### Explanation
この変更は、`search-limits-quotas-capacity.md` ファイルに対するもので、検索サービスの制限とクオータに関する重要な情報が更新されています。主な内容としては、プライベートエンドポイントに関連するサポートとそれに付随する最大制限が強化されました。

具体的には、以下の点が修正されています：
- プライベートエンドポイントを利用したインデクサーのサポートに関する情報に、スキルセットと統合ベクトル化を持つインデクサーに対するサポートが新たに追加されました。これにより、具体的な利用ケースにおける制限内容がより明確になっています。
- 最大のプライベートエンドポイント数や異なるリソースタイプ数についての数値が整理され、最新の仕様が反映されています。

さらに、特定のリソースの運用レベルやプライベートリンクの利用要件についても、詳細な注釈が追加されており、ユーザーにとってより実践的なガイドラインとなっています。特に、サービスを利用する際の条件や注意点が明確になっているため、ユーザーは自身のニーズに合った構成を選択しやすくなっています。全体として、この更新は、検索サービスの制限を理解し、効果的に利用するための情報を提供することを目的としています。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ The tier determines:
 + Size and speed of partitions (physical storage)
 + Billable rate as a fixed monthly cost, but also an incremental cost if you add capacity
 
-In a few instances, the tier you choose determines the availability of [premium features](#premium-features).
+In a few instances, the tier you choose determines the availability of [premium features](#feature-availability-by-tier).
 
 Billing rates are shown in the portal's **Select Pricing Tier** page. You can check the [pricing page](https://azure.microsoft.com/pricing/details/search/) for regional rates and review [Plan and manage costs](search-sku-manage-costs.md) to learn more about the billing model.
 
@@ -31,23 +31,23 @@ Billing rates are shown in the portal's **Select Pricing Tier** page. You can ch
 
 ## Tier descriptions
 
-Tiers include **Free**, **Basic**, **Standard**, and **Storage Optimized**. Standard and Storage Optimized are available with several configurations and capacities. The following screenshot from Azure portal shows the available tiers, minus pricing (which you can find in the portal and on the [pricing page](https://azure.microsoft.com/pricing/details/search/)). 
+Tiers include **Free**, **Basic**, **Standard**, and **Storage Optimized**. Standard and Storage Optimized are available with several configurations and capacities. The following screenshot from Azure portal shows the available tiers, minus pricing (which you can find in the portal and on the [pricing page](https://azure.microsoft.com/pricing/details/search/)).
 
 :::image type="content" source="media/search-sku-tier/tiers.png" lightbox="media/search-sku-tier/tiers.png" alt-text="Pricing tier chart" border="true":::
 
 **Free** creates a [limited search service](search-limits-quotas-capacity.md#subscription-limits) for smaller projects, like running tutorials and code samples. Internally, system resources are shared among multiple subscribers. You can't scale a free service, run significant workloads, and some premium features aren't available. You can only have one free search service per Azure subscription. If the service is inactive for an extended period of time, it might be deleted to free up capacity, especially if the region is under capacity constraints.
 
 The most commonly used billable tiers include:
 
-+ **Basic** has the ability to meet SLA with its support for three replicas. 
++ **Basic** has the ability to meet SLA with its support for three replicas.
 
 + **Standard (S1, S2, S3)** is the default. It gives you more flexibility in scaling for workloads. You can scale both partitions and replicas. With dedicated resources under your control, you can deploy larger projects, optimize performance, and increase capacity.
 
 Some tiers are designed for certain types of work:
 
 + **Standard 3 High Density (S3 HD)** is a *hosting mode* for S3, where the underlying hardware is optimized for a large number of smaller indexes and is intended for multitenancy scenarios. S3 HD has the same per-unit charge as S3, but the hardware is optimized for fast file reads on a large number of smaller indexes.
 
-+ **Storage Optimized (L1, L2)** tiers offer larger storage capacity at a lower price per TB than the Standard tiers. These tiers are designed for large indexes that don't change very often. The primary tradeoff is higher query latency, which you should validate for your specific application requirements. 
++ **Storage Optimized (L1, L2)** tiers offer larger storage capacity at a lower price per TB than the Standard tiers. These tiers are designed for large indexes that don't change very often. The primary tradeoff is higher query latency, which you should validate for your specific application requirements.
 
 You can find out more about the various tiers on the [pricing page](https://azure.microsoft.com/pricing/details/search/), in the [Service limits in Azure AI Search](search-limits-quotas-capacity.md) article, and on the portal page when you're provisioning a service.
 
@@ -70,8 +70,6 @@ Currently, several regions are at capacity for specific tiers and can't be used
 | West Europe | All tiers |
 | West US 3| All tiers |
 
-<a name="premium-features"></a>
-
 ## Feature availability by tier
 
 Most features are available on all tiers, including the free tier. In a few cases, the tier determines the availability of a feature. The following table describes the constraints.
@@ -83,15 +81,15 @@ Most features are available on all tiers, including the free tier. In a few case
 | [Managed or trusted identities for outbound (indexer) access](search-howto-managed-identities-data-sources.md) | Not available on the Free tier.|
 | [Customer-managed encryption keys](search-security-manage-encryption-keys.md) | Not available on the Free tier. |
 | [IP firewall access](service-configure-firewall.md) | Not available on the Free tier. |
-| [Private endpoint (integration with Azure Private Link)](service-create-private-endpoint.md) | For inbound connections to a search service, not available on the Free tier. <br>For outbound connections by indexers to other Azure resources, not available on Free or S3 HD. <br>For indexers that use skillsets, not available on Free, Basic, S1, or S3 HD.| 
+| [Private endpoint (integration with Azure Private Link)](service-create-private-endpoint.md) | For inbound connections to a search service, not available on the Free tier. <br>For outbound connections by indexers to other Azure resources, not available on Free or S3 HD. <br>For indexers that use skillsets, not available on Free, Basic, S1, or S3 HD.|
 | [Availability Zones](search-reliability.md) | Not available on the Free or Basic tier. |
 | [Semantic ranker](semantic-search-overview.md) | Not available on the Free tier. |
 
 Resource-intensive features might not work well unless you give it sufficient capacity. For example, [AI enrichment](cognitive-search-concept-intro.md) has long-running skills that time out on a Free service unless the dataset is small.
 
 ## Upper limits
 
-Tiers determine the  maximum storage of the service itself, plus the maximum number of indexes, indexers, data sources, skillsets, and synonym maps that you can create. For a full break out of all limits, see [Service limits in Azure AI Search](search-limits-quotas-capacity.md). 
+Tiers determine the  maximum storage of the service itself, plus the maximum number of indexes, indexers, data sources, skillsets, and synonym maps that you can create. For a full break out of all limits, see [Service limits in Azure AI Search](search-limits-quotas-capacity.md).
 
 ## Partition size and speed
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SKUティアに関する情報の更新"
}
```

### Explanation
この変更は、`search-sku-tier.md` ファイルに施されたもので、Azure AI SearchにおけるSKU（スコアリング、ストレージ、ユーザー）ティアの情報が更新されています。主な変更点は、ティアの機能の可用性に関するリンクのテキストが改善され、情報がより明確に整理されたことです。

具体的には、プレミアム機能の可用性に関する説明が「機能の可用性に関するテーブル」として更新され、より詳細な情報が提供されています。また、各ティアの説明や特性に関しても整理され、ユーザーが選択肢を理解しやすいように構成されています。特に、ストレージ最適化ティアや、各ティアが提供する機能の制限についての情報が強化されており、ユーザーが自身のニーズに合ったティアを選ぶ手助けとなる内容になっています。

最後に、一般的なビリングレートやサービス制限に関する情報へのリンクも含まれており、ユーザーが追加の詳細を容易に確認できるようになっています。この変更により、利用者は必要な情報を的確に把握しやすくなることが期待されます。

## articles/search/search-traffic-analytics.md{#item-c76f2f}

<details>
<summary>Diff</summary>
````diff
@@ -1,24 +1,24 @@
 ---
 title: Telemetry for search traffic analytics
 titleSuffix: Azure AI Search
-description: Enable search traffic analytics for Azure AI Search, collect telemetry and user-initiated events using Application Insights, and then analyze findings in a Power BI report.
+description: Enable search traffic analytics for Azure AI Search, collect telemetry and user-initiated events using Application Insights.
 author: HeidiSteen
 manager: nitinme
 ms.author: heidist
 
 ms.service: azure-ai-search
-ms.topic: conceptual
-ms.date: 06/19/2024
+ms.topic: how-to
+ms.date: 10/23/2024
 ---
 
 # Collect telemetry data for search traffic analytics
 
-Search traffic analytics is a pattern for collecting telemetry about user interactions with your Azure AI Search application, such as user-initiated click events and keyboard inputs. Using this information, you can determine the effectiveness of your search solution, including popular search terms, clickthrough rate, and which query inputs yield zero results.
+Search traffic analytics is a pattern for collecting telemetry about user interactions with your Azure AI Search application, such as user-initiated click events and keyboard inputs. Using this information, you can determine the effectiveness of your search solution, including clickthrough rate and which query inputs yield zero results.
 
 This pattern takes a dependency on [Application Insights](/azure/azure-monitor/app/app-insights-overview) (a feature of [Azure Monitor](/azure/azure-monitor/)) to collect user data. It requires that you add instrumentation to your client code, as described in this article. Finally, you need a reporting mechanism to analyze the data. We recommend Power BI, but you can use any visualization tool that connects to Application Insights.
 
 > [!NOTE]
-> The pattern described in this article is for advanced scenarios and clickstream data generated by code you add to your client. In contrast, service logs are easy to set up, provide a range of metrics, and can be done in the portal with no code required. Enabling logging is recommended for all scenarios. For more information, see [Collect and analyze log data](monitor-azure-cognitive-search.md).
+> The pattern described in this article is for advanced scenarios and clickstream data generated by code you add to your client. In contrast, service logs are easy to set up, provide a range of metrics including search terms, and can be done in the portal with no code required. We recommend that you enable logging for all scenarios. For more information, see [Collect and analyze log data](monitor-azure-cognitive-search.md).
 
 ## Identify relevant search data
 
@@ -38,9 +38,9 @@ In the [portal](https://portal.azure.com) page for your Azure AI Search service,
 
 ## Step 1: Set up Application Insights
 
-Select an existing Application Insights resource or [create one](/previous-versions/azure/azure-monitor/app/create-new-resource) if you don't have one already. 
+Select an existing Application Insights resource or [create one](/previous-versions/azure/azure-monitor/app/create-new-resource) if you don't have one already.
 
-A shortcut that works for some Visual Studio project types is reflected in the following steps. 
+A shortcut that works for some Visual Studio project types is reflected in the following steps.
 
 For illustration, these steps use the client from [Add search to a static web app](tutorial-csharp-overview.md).
 
@@ -52,7 +52,7 @@ For illustration, these steps use the client from [Add search to a static web ap
 
 1. Select your Azure subscription, your Application Insights resource, and then select **Finish**.
 
-At this point, your application is set up for application monitoring, which means all page loads in your client app are tracked with default metrics. 
+At this point, your application is set up for application monitoring, which means all page loads in your client app are tracked with default metrics.
 
 If this shortcut didn't work for you, see [Enable Application Insights server-side telemetry](/azure/azure-monitor/app/asp-net-core#enable-application-insights-server-side-telemetry-visual-studio).
 
@@ -66,7 +66,7 @@ Create an object that sends events to Application Insights. You can add instrume
 
 Server-side telemetry captures metrics at the application layer, for example in applications running as a web service on Azure, or as an on-premises app on a corporate network. Server-side telemetry captures search and click events, the position of a document in results, and query information, but your data collection will be scoped to whatever information is available at that layer.
 
-On the client, you might have other code that manipulates query inputs, adds navigation, or includes context (for example, queries initiated from a home page versus a product page). If this describes your solution, you might opt for client-side instrumentation so that your telemetry reflects the extra detail. How this extra detail is collected goes beyond the scope of this pattern, but you can review [Application Insights for web pages](/azure/azure-monitor/app/javascript#explore-browserclient-side-data) for help with that decision. 
+On the client, you might have other code that manipulates query inputs, adds navigation, or includes context (for example, queries initiated from a home page versus a product page). If this describes your solution, you might opt for client-side instrumentation so that your telemetry reflects the extra detail. How this extra detail is collected goes beyond the scope of this pattern, but you can review [Application Insights for web pages](/azure/azure-monitor/app/javascript#explore-browserclient-side-data) for help with that decision.
 
 You can get the instrumentation key from Azure portal, either in the pages for Application Insights or in the Search traffic analytics page for Azure AI Search.
 
@@ -93,7 +93,7 @@ var response = await client.Documents.SearchWithHttpMessagesAsync(searchText: se
 IEnumerable<string> headerValues;
 string searchId = string.Empty;
 if (response.Response.Headers.TryGetValues("x-ms-azs-searchid", out headerValues)){
-	 searchId = headerValues.FirstOrDefault();
+    searchId = headerValues.FirstOrDefault();
 } 
 ```
 
@@ -114,12 +114,12 @@ Every time that a search request is issued by a user, you should log that as a s
 
 ```csharp
 var properties = new Dictionary <string, string> {
-	{"SearchServiceName", <SEARCH SERVICE NAME>},
-	{"SearchId", <SEARCH ID>},
-	{"IndexName", <INDEX NAME>},
-	{"QueryTerms", <SEARCH TERMS>},
-	{"ResultCount", <RESULTS COUNT>},
-	{"ScoringProfile", <SCORING PROFILE USED>}
+    {"SearchServiceName", <SEARCH SERVICE NAME>},
+    {"SearchId", <SEARCH ID>},
+    {"IndexName", <INDEX NAME>},
+    {"QueryTerms", <SEARCH TERMS>},
+    {"ResultCount", <RESULTS COUNT>},
+    {"ScoringProfile", <SCORING PROFILE USED>}
 };
 
 telemetryClient.TrackEvent("Search", properties);
@@ -140,10 +140,10 @@ Every time that a user clicks on a document, that's a signal that must be logged
 
 ```csharp
 var properties = new Dictionary <string, string> {
-	{"SearchServiceName", <SEARCH SERVICE NAME>},
-	{"SearchId", <SEARCH ID>},
-	{"ClickedDocId", <CLICKED DOCUMENT ID>},
-	{"Rank", <CLICKED DOCUMENT POSITION>}
+    {"SearchServiceName", <SEARCH SERVICE NAME>},
+    {"SearchId", <SEARCH ID>},
+    {"ClickedDocId", <CLICKED DOCUMENT ID>},
+    {"Rank", <CLICKED DOCUMENT POSITION>}
 };
 
 telemetryClient.TrackEvent("Click", properties);
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索トラフィック分析のテレメトリに関する情報の更新"
}
```

### Explanation
この変更は、`search-traffic-analytics.md` ファイルに対して行われたもので、Azure AI Searchの検索トラフィック分析に関するテレメトリの設定や使用方法についての情報が更新されています。主な変更点は以下の通りです。

1. **ドキュメントのタイプ変更**: ドキュメントのトピックが「概念」から「ハウツー」に変更され、ユーザーが実際に操作するための具体的な手順に焦点を当てるようになりました。これにより、利用者が必要な情報を見つけやすくなっています。

2. **説明内容の簡素化**: 説明文から「Power BIレポートでの分析」という言及が削除され、Application Insightsを用いたデータ収集のみに焦点を当てるようになりました。

3. **詳細の強化**: ロギングとテレメトリに関する新しい情報が追加され、特にサービスログの推奨が明確化されました。これにより、ユーザーが必要なデータを収集・分析する方法がわかりやすくなっています。

4. **コードのフォーマット修正**: コードスニペット内のインデントが修正され、可読性が向上しています。このような調整により、プログラマーはコードをより簡単に理解できるようになります。

この更新により、検索トラフィック分析の実装方法が具体的で適切に示されており、ユーザーはより効果的にこの機能を活用できるようになります。


