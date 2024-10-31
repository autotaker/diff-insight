---
date: '2024-10-31'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a68723c...MicrosoftDocs:b16ebe2
summary: このコード差分では、いくつかのドキュメントに対して軽微な更新が行われました。主な内容としては、検索トラフィック分析ドキュメントの内容拡充や画像リンクの更新、メタデータの調整、さらには統合ベクトル化に関する注意書きの追加があります。新たにテレメトリーデータの収集手法についてのセクションが追加され、より詳細な情報が提供されています。破壊的変更はありませんが、名称やモデル名の更新が参照方法に影響を与える可能性があります。全体として、これらの修正はユーザーの理解と利用を助け、ドキュメントの正確性とユーザビリティを向上させることを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a68723c...MicrosoftDocs:b16ebe2){target="_blank"}

# ハイライト
このコード差分では、複数のドキュメントに関して軽微な更新が行われています。更新内容には、テキスト分割認知スキルのメタデータ調整、検索トラフィック分析ドキュメントの内容拡充、トラフィック分析画像のリンク更新、そして統合ベクトル化に関する注意書きの追加が含まれます。

## 新機能
- 「検索トラフィック分析」のドキュメントにおいて、新しいセクションが追加され、テレメトリーデータ収集手法やクリックストリームイベントとの関連付けが詳しく網羅されました。

## 破壊的変更
- 特に破壊的変更は含まれていませんが、名称やモデル名の更新により、参照方法や使用プロセスに影響を与える可能性があります。

## その他の更新
- メタデータの更新（日付、モデル名）により、正確な情報への更新が行われています。
- 画像ファイルの更新による参照の整合性維持。
- 統合ベクトル化機能の使用に関する注意書きの追加。

# 洞察
今回のコード差分では、ドキュメントの内容と情報の正確性、ユーザビリティを高めるための軽微な修正と更新が行われました。まず、日付やモデル名を最新のものに変更することで、ドキュメントを利用するユーザーが混乱しないように改訂されています。特に、テキスト分割認知スキルのモデル名が「cl100k」から「cl100k_base」に変更された点は、新たなモデル名に合わせた最新情報を提供する意図が感じられます。

「検索トラフィック分析」ドキュメントの改訂は、単なる内容の追加にとどまらず、新しいセクションの導入により、ユーザーが実際に分析を実施する際のガイドラインとして非常に有益な情報を提供しています。具体的にはテレメトリーデータの収集手法やアプリケーションのインストメンテーションの詳細が追加されており、開発者がより深い理解を持って取り組むことが可能になります。

画像ファイルのリンク更新は、日常的なドキュメンテーションではあるものの、正しい内容が確実にユーザへ提供されるために不可欠な修正であり、参照の整合性を保っています。

最後に、統合ベクトル化のドキュメントで提供されている使用時の制限事項（画像URI未対応など）は、開発者にとってエラーを未然に防ぐための重要な情報であり、こうした注意書きの追加はユーザーエクスペリエンス向上に寄与する変更です。総じて、これらの修正は、利用者がAzure関連技術を効果的かつ正しく利用するための布石と言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-textsplit.md](#item-9bf753) | minor update | テキスト分割認知スキルの更新 | modified | 2 | 2 | 4 | 
| [azuresearch-trafficanalytics.png](#item-9b0332) | minor update | トラフィック分析の画像更新 | modified | 0 | 0 | 0 | 
| [search-traffic-analytics.md](#item-c76f2f) | minor update | 検索トラフィック分析のドキュメント更新 | modified | 128 | 91 | 219 | 
| [vector-search-integrated-vectorization-ai-studio.md](#item-353fcc) | minor update | 統合ベクトル化に関するドキュメントの更新 | modified | 3 | 1 | 4 | 


# Modified Contents
## articles/search/cognitive-search-skill-textsplit.md{#item-9bf753}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: reference
-ms.date: 10/01/2024
+ms.date: 10/29/2024
 ---
 
 # Text split cognitive skill
@@ -67,7 +67,7 @@ Parameters are case-sensitive.
     "textSplitMode": "pages", 
     "unit": "azureOpenAITokens", 
     "azureOpenAITokenizerParameters":{ 
-        "encoderModelName":"cl100k", 
+        "encoderModelName":"cl100k_base", 
         "allowedSpecialTokens": [ 
             "[START]", 
             "[END]" 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト分割認知スキルの更新"
}
```

### Explanation
この変更は、ドキュメント「テキスト分割認知スキル」に関する軽微な更新を含んでいます。具体的には、メタデータとしての日付が「2024年10月1日」から「2024年10月29日」に変更され、またエンコーダモデル名が「cl100k」から「cl100k_base」に変更されました。このような更新は、ドキュメントの正確性を向上させ、最新の情報を反映させるために必要です。これによりユーザーは、関連する技術や仕様の変化に関する理解を深めることができます。

## articles/search/media/search-traffic-analytics/azuresearch-trafficanalytics.png{#item-9b0332}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トラフィック分析の画像更新"
}
```

### Explanation
この変更は、ドキュメント「トラフィック分析」に関連する画像ファイル「azuresearch-trafficanalytics.png」に関する軽微な更新を示しています。変更内容としては、実際の追加や削除は行われておらず、ファイルの内容自体には変更がないことが示されていますが、ファイルへのリンクが更新された可能性があります。このような更新は、ドキュメントの整合性を保つために重要です。ユーザーは、この画像が引き続き参照可能であることを確認することができます。

## articles/search/search-traffic-analytics.md{#item-c76f2f}

<details>
<summary>Diff</summary>
````diff
@@ -8,41 +8,64 @@ ms.author: heidist
 
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 10/23/2024
+ms.date: 10/29/2024
 ---
 
 # Collect telemetry data for search traffic analytics
 
-Search traffic analytics is a pattern for collecting telemetry about user interactions with your Azure AI Search application, such as user-initiated click events and keyboard inputs. Using this information, you can determine the effectiveness of your search solution, including clickthrough rate and which query inputs yield zero results.
+Search traffic analytics is a pattern for collecting telemetry about user interactions with your Azure AI Search application, such as user-initiated clickstream events and keyboard inputs. Using this information, you can determine the effectiveness of your search solution, including clickthrough rate and which query inputs yield zero results.
 
-This pattern takes a dependency on [Application Insights](/azure/azure-monitor/app/app-insights-overview) (a feature of [Azure Monitor](/azure/azure-monitor/)) to collect user data. It requires that you add instrumentation to your client code, as described in this article. Finally, you need a reporting mechanism to analyze the data. We recommend Power BI, but you can use any visualization tool that connects to Application Insights.
+Instrumentation has the following parts:
+
++ Add a telemetry client
++ Modify a search request to include a correlation Id that maps search results to user actions
++ Create and send a custom event to Application Insights and use the visualization and reporting tools to view event data
+
+This pattern takes a dependency on [Application Insights](/azure/azure-monitor/app/app-insights-overview) (a feature of [Azure Monitor](/azure/azure-monitor/)) to collect user data. It requires that you add instrumentation to your application code, as described in this article. Finally, you need a reporting mechanism to analyze the data. You can use any visualization tool that connects to Application Insights.
 
 > [!NOTE]
 > The pattern described in this article is for advanced scenarios and clickstream data generated by code you add to your client. In contrast, service logs are easy to set up, provide a range of metrics including search terms, and can be done in the portal with no code required. We recommend that you enable logging for all scenarios. For more information, see [Collect and analyze log data](monitor-azure-cognitive-search.md).
 
+## Prerequisites
+
++ [Azure AI Search](search-create-service-portal.md), any region, basic tier and above.
+
++ [Application Insights](/azure/azure-monitor/app/create-workspace-resource).
+
++ A rich client application providing an interactive search experience that includes clickstream events or other user actions that you want to correlate to search result selections.
+
 ## Identify relevant search data
 
-To have useful metrics for search traffic analytics, it's necessary to log some signals from the users of your search application. These signals signify content that users are interested in and that they consider relevant. For search traffic analytics, these include:
+To collect useful metrics for search traffic analytics, it's necessary to log some signals from the users of your search application. These signals signify content that users are interested in and that they consider relevant. For search traffic analytics, these include:
 
 + User-generated search events: Only search queries initiated by a user are interesting. Other search requests, such as those used to populate facets or retrieve internal information, aren't important. Be sure to only instrument user-initiated events to avoid skew or bias in your results.
 
-+ User-generated click events: On a search results page, a click event generally means that a document is a relevant result for a specific search query.
++ User-generated clickstream events: On a search results page, a clickstream event generally means that a document is a relevant result for a specific search query.
 
-By linking search and click events with a correlation ID, you can gain a deeper understanding of how well your application's search functionality is performing.
+In your application code, you should correlate these events with the search results returned from a given query. By linking search and clickstream events with a correlation ID, you can gain a deeper understanding of how well your application's search functionality is performing.
 
 ## Add search traffic analytics
 
-In the [portal](https://portal.azure.com) page for your Azure AI Search service, open the Search Traffic Analytics page to access a cheat sheet for following this telemetry pattern. From this page, you can select or create an Application Insights resource, get the instrumentation key, copy snippets that you can adapt for your solution, and download a Power BI report that's built over the schema reflected in the pattern.
+For Azure AI Search, the Azure [portal](https://portal.azure.com) provides a Search Traffic Analytics page that has C# and JavaScript code snippets for adding a telemetry client, request headers, and properties necessary for custom log events. 
+
+> [!IMPORTANT]
+> The Search traffic analytics portal page is currently outdated and references an obsolete client libary. The workaround is to use code snippets from the [azure-search-traffic-analytics](https://github.com/Azure-Samples/azure-search-traffic-analytics) GitHub repository. This article includes code snippets from the GitHub repository.
 
 :::image type="content" source="media/search-traffic-analytics/azuresearch-trafficanalytics.png" alt-text="Screenshot of the portal command and page for setting up Application Insights.":::
 
 ## Step 1: Set up Application Insights
 
-Select an existing Application Insights resource or [create one](/previous-versions/azure/azure-monitor/app/create-new-resource) if you don't have one already.
+Create an object that sends events to Application Insights. You can add instrumentation to your server-side application code or client-side code running in a browser, expressed here as C# and JavaScript variants. For other languages, see [supported platforms and frameworks](/azure/azure-monitor/app/app-insights-overview#supported-languages).
 
-A shortcut that works for some Visual Studio project types is reflected in the following steps.
+Server-side telemetry captures metrics at the application layer, for example in applications running as a web service on Azure, or as an on-premises app on a corporate network. Server-side telemetry captures search and clickstream events, the position of a document in results, and query information, but your data collection will be scoped to whatever information is available at that layer.
 
-For illustration, these steps use the client from [Add search to a static web app](tutorial-csharp-overview.md).
+On the client, you might have other code that manipulates query inputs, adds navigation, or includes context (for example, queries initiated from a home page versus a product page). If this describes your solution, you might opt for client-side instrumentation so that your telemetry reflects the extra detail. How this extra detail is collected goes beyond the scope of this pattern, but you can review [Application Insights for web pages](/azure/azure-monitor/app/javascript#explore-browserclient-side-data) for help with that decision.
+
+In this step, provide a [connection string to Application Insights](/azure/azure-monitor/app/migrate-from-instrumentation-keys-to-connection-strings).
+
+### [**Visual Studio**](#tab/visual-studio-telemetry-client)
+
+A shortcut that works for some Visual Studio project types is reflected in the following steps.
 
 1. Open your solution in Visual Studio.
 
@@ -54,132 +77,146 @@ For illustration, these steps use the client from [Add search to a static web ap
 
 At this point, your application is set up for application monitoring, which means all page loads in your client app are tracked with default metrics.
 
-If this shortcut didn't work for you, see [Enable Application Insights server-side telemetry](/azure/azure-monitor/app/asp-net-core#enable-application-insights-server-side-telemetry-visual-studio).
-
-## Step 2: Add instrumentation
-
-Add instrumentation code to your client application. The Search Traffic Analytics page in the Azure portal provides code snippets that you can paste into your application code.
+If this shortcut didn't work for you, see [Enable Application Insights server-side telemetry](/azure/azure-monitor/app/asp-net-core#enable-application-insights-server-side-telemetry-visual-studio) or refer to code snippets in the adjacent tabs.
 
-### Create a telemetry client
+### [**.NET**](#tab/dotnet-telemetry-client)
 
-Create an object that sends events to Application Insights. You can add instrumentation to your server-side application code or client-side code running in a browser, expressed here as C# and JavaScript variants. For other languages, see [supported platforms and frameworks](/azure/azure-monitor/app/app-insights-overview#supported-languages).
-
-Server-side telemetry captures metrics at the application layer, for example in applications running as a web service on Azure, or as an on-premises app on a corporate network. Server-side telemetry captures search and click events, the position of a document in results, and query information, but your data collection will be scoped to whatever information is available at that layer.
+```csharp
+var telemetryConfiguration = new TelemetryConfiguration
+{
+    ConnectionString = "<PUT YOUR CONNECTION STRING HERE>"
+};
+var telemetryClient = new TelemetryClient(telemetryConfiguration);
+```
 
-On the client, you might have other code that manipulates query inputs, adds navigation, or includes context (for example, queries initiated from a home page versus a product page). If this describes your solution, you might opt for client-side instrumentation so that your telemetry reflects the extra detail. How this extra detail is collected goes beyond the scope of this pattern, but you can review [Application Insights for web pages](/azure/azure-monitor/app/javascript#explore-browserclient-side-data) for help with that decision.
+### [**JavaScript**](#tab/javascript-telemetry-client)
 
-You can get the instrumentation key from Azure portal, either in the pages for Application Insights or in the Search traffic analytics page for Azure AI Search.
+```javascript
+const appInsights = new ApplicationInsights({ config: {
+  connectionString: '<PUT YOUR CONNECTION STRING HERE>'
+  /* ...Other Configuration Options... */
+} });
+appInsights.loadAppInsights();
+```
 
-```csharp
-// Application Insights SDK: https://www.nuget.org/packages/Microsoft.ApplicationInsights.Web 
+---
 
-var telemetryClient = new TelemetryClient();
-telemetryClient.InstrumentationKey = "0000000000000000000000000000";
-```
+## Step 2: Add instrumentation
 
-### Request a Search ID for correlation
+Add instrumentation code to your client application.
 
-> [!IMPORTANT]
-> In the Azure portal, the snippets for request headers are made using an outdated version of the Azure SDK. Updates are pending.
+### Correlate clickstream events with search results
 
 To correlate search requests with clicks, it's necessary to have a correlation ID that relates these two distinct events. Azure AI Search provides you with a search ID when you request it with an HTTP header.
 
 Having the search ID allows correlation of the metrics emitted by Azure AI Search for the request itself, with the custom metrics you're logging in Application Insights.
 
+### [**.NET**](#tab/dotnet-correlation)
+
 ```csharp
-var client = new SearchClient(<SEARCH SERVICE NAME>, <INDEX NAME>, new AzureDefaultCredentials())
-var headers = new Dictionary<string, List<string>>() { { "x-ms-azs-return-searchid", new List<string>() { "true" } } };
-var response = await client.Documents.SearchWithHttpMessagesAsync(searchText: searchText, searchParameters: parameters, customHeaders: headers);
-IEnumerable<string> headerValues;
-string searchId = string.Empty;
-if (response.Response.Headers.TryGetValues("x-ms-azs-searchid", out headerValues)){
-    searchId = headerValues.FirstOrDefault();
-} 
+var client = new SearchClient(new Uri("https://contoso.search.windows.net"), "hotels-sample-index", new DefaultAzureCredential());
+
+// Generate a new correlation id for logs
+string searchId = Guid.NewGuid().ToString();
+string searchText = "*";
+SearchResults<SearchDocument> searchResults;
+
+// Set correlation id for search request
+using (HttpPipeline.CreateClientRequestIdScope(clientRequestId: searchId))
+{
+    searchResults = client.Search<SearchDocument>(searchText, options: new SearchOptions { IncludeTotalCount = true } );
+}
 ```
 
-### Log search events
+### [**JavaScript**](#tab/javascript-correlation)
+
+```javascript
+const searchId = uuidv4();
+const searchText = "*";
+const searchResults = await searchClient.search(searchText, { includeTotalCount: true, customHeaders: { "x-ms-client-request-id": searchId }});
+const properties = {
+    searchId: searchId,
+    serviceName: "<PUT YOUR SEARCH SERVICE NAME HERE, example contoso-search>",
+    indexName: "<PUT YOUR INDEX NAME HERE>",
+    searchText: searchText,
+    resultsCount: searchResults.count
+};
+appInsights.trackEvent({ name: "search" }, properties);
+```
 
-Every time that a search request is issued by a user, you should log that as a search event with the following schema on an Application Insights custom event. Remember to log only user-generated search queries.
+---
 
+### Log custom events
+
+Every time that a search request is issued by a user, you should log that as a search event with the following schema on an [Application Insights custom event](/azure/azure-monitor/app/api-custom-events-metrics). Remember to log only user-generated search queries.
+
++ **SearchId**: (guid) unique identifier of the search query (built into the search response)
 + **SearchServiceName**: (string) search service name
-+ **SearchId**: (guid) unique identifier of the search query (comes in the search response)
 + **IndexName**: (string) search service index to be queried
-+ **QueryTerms**: (string) search terms entered by the user
-+ **ResultCount**: (int) number of documents that were returned (comes in the search response)
-+ **ScoringProfile**: (string) name of the scoring profile used, if any
++ **SearchText**: (string) search terms entered by the user
++ **ResultCount**: (int) number of documents that were returned (built into the search response)
 
 > [!NOTE]
-> Request the count of user generated queries by adding $count=true to your search query. For more information, see [Search Documents (REST)](/rest/api/searchservice/documents/search-post#searchrequest).
+> Request the count of user generated queries by adding `$count=true` to your search query. For more information, see [Search Documents (REST)](/rest/api/searchservice/documents/search-post#searchrequest).
 >
 
+### [**.NET**](#tab/dotnet-properties)
+
 ```csharp
-var properties = new Dictionary <string, string> {
-    {"SearchServiceName", <SEARCH SERVICE NAME>},
-    {"SearchId", <SEARCH ID>},
-    {"IndexName", <INDEX NAME>},
-    {"QueryTerms", <SEARCH TERMS>},
-    {"ResultCount", <RESULTS COUNT>},
-    {"ScoringProfile", <SCORING PROFILE USED>}
+// Create properties for telemetry
+var properties = new Dictionary<string, string>
+{
+    ["searchId"] = searchId,
+    ["serviceName"] = "<PUT YOUR SEARCH SERVICE NAME HERE, example: contoso-search>",
+    ["indexName"] = "<PUT YOUR INDEX NAME HERE>",
+    ["searchText"] = searchText,
+    ["resultsCount"] = searchResults.TotalCount?.ToString()
 };
-
-telemetryClient.TrackEvent("Search", properties);
 ```
 
-### Log click events
-
-Every time that a user clicks on a document, that's a signal that must be logged for search analysis purposes. Use Application Insights custom events to log these events with the following schema:
-
-+ **ServiceName**: (string) search service name
-+ **SearchId**: (guid) unique identifier of the related search query
-+ **DocId**: (string) document identifier
-+ **Position**: (int) rank of the document in the search results page
+### [**JavaScript**](#tab/javascript-properties)
 
-> [!NOTE]
-> Position refers to the cardinal order in your application. You are free to set this number, as long as it's always the same, to allow for comparison.
->
-
-```csharp
-var properties = new Dictionary <string, string> {
-    {"SearchServiceName", <SEARCH SERVICE NAME>},
-    {"SearchId", <SEARCH ID>},
-    {"ClickedDocId", <CLICKED DOCUMENT ID>},
-    {"Rank", <CLICKED DOCUMENT POSITION>}
+```javascript
+const properties = {
+    searchId: searchId,
+    serviceName: "<PUT YOUR SEARCH SERVICE NAME HERE, example contoso-search>",
+    indexName: "<PUT YOUR INDEX NAME HERE>",
+    searchText: searchText,
+    resultsCount: searchResults.count
 };
-
-telemetryClient.TrackEvent("Click", properties);
 ```
 
-## Step 3: Analyze in Power BI
-
-After you have instrumented your app and verified your application is correctly connected to Application Insights, you download a predefined report template to analyze data in Power BI desktop. The report contains predefined charts and tables useful for analyzing the extra data captured for search traffic analytics.
-
-1. In the Azure portal on the search service pages, under **Settings**, select **Search traffic analytics**.
+---
 
-1. Select **Get Power BI Desktop** to install Power BI.
+### Send the custom event to Application Insights
 
-1. Select **Download Power BI report** to get the report.
+Add the custom even to the *custom events* table in Application Insights. For more information, see [Application Insights API for custom events and metrics](/azure/azure-monitor/app/api-custom-events-metrics).
 
-1. The report opens in Power BI Desktop, and you're prompted to connect to Application Insights and provide credentials. You can find connection information in the Azure portal pages for your Application Insights resource. For credentials, provide the same user name and password that you use for portal sign-in.
+### [**.NET**](#tab/dotnet-custom-events)
 
-   :::image type="content" source="media/search-traffic-analytics/connect-to-app-insights.png" alt-text="Screenshot showing how to connect to Application Insights from Power BI.":::
+```csharp
+telemetryClient.TrackEvent("search", properties);
+telemetryClient.Flush();
+```
 
-1. Select **Load**.
+### [**JavaScript**](#tab/javascript-custom-events)
 
-The report contains charts and tables that help you make more informed decisions to improve your search performance and relevance.
+```javascript
+appInsights.trackEvent({ name: "search" }, properties);
+```
 
-Metrics included the following items:
+---
 
-+ Search volume and most popular term-document pairs: terms that result in the same document clicked, ordered by clicks.
-+ Searches without clicks: terms for top queries that register no clicks
+## Step 3: Review logs
 
-The following screenshot shows the data elements that your report might contain.
+Use any of the approaches supported by Application Insights for viewing custom events.
 
-:::image type="content" source="media/search-traffic-analytics/azuresearch-powerbi-dashboard.png" alt-text="Screenshot showing the available schema elements in the data catalog. ":::
++ [Create or edit an Azure Workbook](/azure/azure-monitor/visualize/workbooks-create-workbook)
++ [Create and share dashboards of Log Analytics data](/azure/azure-monitor/visualize/tutorial-logs-dashboards)
++ [Integrate Log Analytics with Power BI](/azure/azure-monitor/logs/log-powerbi)
 
 ## Next steps
 
-Instrument your search application to get powerful and insightful data about your search service.
-
 You can find more information on [Application Insights](/azure/azure-monitor/app/app-insights-overview) and visit the [pricing page](https://azure.microsoft.com/pricing/details/application-insights/) to learn more about their different service tiers.
 
 Learn more about creating reports. See [Getting started with Power BI Desktop](/power-bi/fundamentals/desktop-getting-started) for details.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索トラフィック分析のドキュメント更新"
}
```

### Explanation
この変更は、「検索トラフィック分析」に関するドキュメントの大幅な更新を表しています。主な変更点は、内容の拡充による128行の新規追加と91行の削除が含まれており、合計で219行の変更があったことを示しています。具体的には、テレメトリーデータの収集手法や、アプリケーションのインストメンテーションの方法が詳しく説明されており、新しいセクションとして「前提条件」や「クリックストリームイベントとの関連付け」などが追加されています。また、ドキュメントの日付も更新され、最新の情報を反映するために必要な改訂が行われています。このような変更は、ユーザーがAzure AI Searchを用いた検索機能の効果を正確に評価し、改善するための重要な情報を提供します。

## articles/search/vector-search-integrated-vectorization-ai-studio.md{#item-353fcc}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 05/08/2024
+ms.date: 10/29/2024
 ---
 
 # How to implement integrated vectorization using models from Azure AI Studio
@@ -161,6 +161,8 @@ You must add the `/v1/embed` path onto the end of the URL that you copied from y
 
 The URI and key are generated when you deploy the model from the catalog. For more information about these values, see [How to deploy Cohere Embed models with Azure AI Studio](/azure/ai-studio/how-to/deploy-models-cohere-embed).
 
+Note that image URIs are not supported by this integration at this time.
+
 ```json
 {
   "@odata.type": "#Microsoft.Skills.Custom.AmlSkill",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "統合ベクトル化に関するドキュメントの更新"
}
```

### Explanation
この変更は、「Azure AI Studioからのモデルを使用した統合ベクトル化の実装方法」に関するドキュメントの軽微な更新を示しています。具体的には、文書の日付が2024年5月8日から2024年10月29日に更新され、最新の情報を反映しています。また、ドキュメントの内容において、現在の統合では画像URIがサポートされていない旨の注意書きが追加されました。このような修正は、ユーザーに統合ベクトル化機能の使用時に留意すべき点を明確にするため、重要です。全体として、3行が新たに追加され、1行が削除され、合計で4行の変更が行われています。


