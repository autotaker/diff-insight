---
date: '2025-01-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b5fac8b...MicrosoftDocs:62147e0
summary: このコード差分は、Azure AI Searchの機能強化およびユーザー利便性の向上を目的とした重要な変更を含んでいます。主な変更には、診断ログの設定に関する新しいドキュメントの追加、新しい画像ファイルの導入、既存のリンクの更新があります。新たに追加された記事は、診断ログの設定手順やKQLモードの有効化に関する参考資料として、ユーザーの理解を促進し、管理効率を高めることを狙っています。また、いくつかのドキュメントでは軽微な修正が行われ、よりユーザーフレンドリーなアクセスを提供しています。全体として、これらの変更はドキュメントの信頼性とユーザビリティを向上させるための重要な一歩といえます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b5fac8b...MicrosoftDocs:62147e0){target="_blank"}

# ハイライト

このコード差分は、Azure AI Searchの機能強化およびユーザー利便性の向上を目的としたいくつかの重要な変更を含んでいます。主な変更には、診断ログの設定に関する新しいドキュメントの追加、新しい画像ファイルの導入、そして既存のリンクの更新が含まれます。

## 新しい機能
- 診断ログの設定に関する新しい記事「search-monitor-enable-logging.md」の追加。
- 「enable-kql-mode.png」および「query-example.png」の新規画像の追加。

## 破壊的変更
- 特にありませんが、リンクの更新により、既存の参照が変更される場合があります。

## その他のアップデート
- Azure AI Searchの監視に関する既存の記事である「monitor-azure-cognitive-search.md」の軽微な修正。
- 複数のドキュメントで診断ログ有効化のリンク先が「search-monitor-enable-logging.md」に更新。

# インサイト

このコード差分は、Azure AI Searchのドキュメントにおけるユーザーエクスペリエンスと情報精度を向上させるために計画された一連の変更を示しています。以下、この変更の各要素について詳細に解説します。

### 新機能

新しい画像ファイル「enable-kql-mode.png」および「query-example.png」が追加されました。これらの画像は、KQLモードの有効化および検索モニタリングに関するクエリの例をユーザーに視覚的に提供し、理解を促進します。特に、新しい画像は複雑な設定操作を行う際にユーザーが直感的に理解を深める手助けをします。

また、新たに追加された「search-monitor-enable-logging.md」記事は、Azure AI Searchにおける診断ログ設定を詳述したもので、リソースレベルの診断ログとアクティビティログの違いを明確にします。さらに、Azure Portalを通じた診断ログの有効化手順や、Kusto Query Languageを用いたログ探索のサンプルが含まれており、ユーザーの管理効率を高める重要なリソースです。

### 軽微な更新とリンク修正

「monitor-azure-cognitive-search.md」の更新では、「how-to」から「conceptual」な内容へと改変され、診断ログの有効化手順がより簡潔にまとめられました。この変更は、ユーザーが必要とする重要な情報に素早くアクセスできることを狙ったものです。

さらに、複数のドキュメントで診断ログ有効化に関連するリンクが修正され、新しく詳細な導入手順を説明する「search-monitor-enable-logging.md」に更新されました。これにより、ユーザーは診断ログの設定についてより適切で関連性の高い情報に直接アクセスできるようになり、全体のドキュメント精度とユーザーの理解向上を促進します。

### まとめ

これらの改良は、Azure AI Searchにおける監視設定の効果的な導入をサポートし、ユーザーがクラウドサービスをより効率的に管理・運用できるようにするものです。全体として、これらの変更は、ドキュメントの信頼性を強化し、ユーザビリティを著しく向上させるための重要な一歩となっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [enable-kql-mode.png](#item-55ab35) | new feature | KQLモードを有効にするのための新しい画像追加 | added | 0 | 0 | 0 | 
| [query-example.png](#item-1f5512) | new feature | クエリ例のための新しい画像追加 | added | 0 | 0 | 0 | 
| [monitor-azure-cognitive-search.md](#item-5be826) | minor update | Azure AI Searchの監視記事の更新 | modified | 3 | 27 | 30 | 
| [search-manage.md](#item-4043d7) | minor update | 診断ログを有効にするリンクの更新 | modified | 1 | 1 | 2 | 
| [search-monitor-enable-logging.md](#item-e3600e) | new feature | Azure AI Searchの診断ログの設定に関する新しい記事の追加 | added | 109 | 0 | 109 | 
| [toc.yml](#item-c4768f) | minor update | 目次ファイルへの新しい項目の追加 | modified | 2 | 0 | 2 | 
| [vector-search-how-to-configure-vectorizer.md](#item-30ffd8) | minor update | 診断ログ有効化のリンクの更新 | modified | 1 | 1 | 2 | 
| [vector-store.md](#item-db9b8c) | minor update | 診断ログ有効化のリンクの更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/media/search-monitor-enable-logging/enable-kql-mode.png{#item-55ab35}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "KQLモードを有効にするのための新しい画像追加"
}
```

### Explanation
このコードの変更は、新しい画像ファイル「enable-kql-mode.png」がプロジェクトに追加されたことを示しています。この画像は、KQL（Kusto Query Language）モードを有効にするための手順や機能に関連している可能性があります。画像は、GitHubのリポジトリにアップロードされ、今後のドキュメント内で使用されることが想定されます。この追加により、ユーザーに対して視覚的な参考資料が提供され、理解が容易になることが期待されています。

## articles/search/media/search-monitor-enable-logging/query-example.png{#item-1f5512}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "クエリ例のための新しい画像追加"
}
```

### Explanation
この変更は、「query-example.png」という新しい画像ファイルがプロジェクトに追加されたことを示しています。この画像は、検索モニタリングのログを有効にする機能に関連するクエリの例を示している可能性があります。GitHubのリポジトリに格納されているこの画像は、今後のドキュメントで使用され、ユーザーがクエリの使用方法を視覚的に理解できるようにすることを目的としています。この追加は、ユーザーエクスペリエンスを向上させるための重要な要素です。

## articles/search/monitor-azure-cognitive-search.md{#item-5be826}

<details>
<summary>Diff</summary>
````diff
@@ -3,42 +3,18 @@ title: Monitor Azure AI Search
 description: Start here to learn how to monitor Azure AI Search.
 ms.date: 01/27/2025
 ms.custom: horz-monitor
-ms.topic: how-to
+ms.topic: conceptual
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ---
 
 # Monitor Azure AI Search
 
-This article explains how to configure logging and where to find information about search service operations.
-
-## Enable diagnostic logging
-
-Resource logging is available through Azure Monitor. Although some search service activity is reported automatically with no upfront configuration, resource logs about operations and data access require that you create a diagnostic setting and specify a storage option.
-
-If you create more than one diagnostic setting, you must have different destinations for each one. 
-
-1. Sign in to the [Azure portal](https://portal.azure.com) and navigate to your search service.
-
-1. Under **Monitoring** > **Diagnostic settings**, select **Add diagnostic setting**.
-
-1. Provide a name that identifies the service and level of logging, such as "my-search-service-all-logs" or "my-search-service-audit-logs".
-
-1. Under **Logs**, choose a category:
-
-   - **audit** to capture information about user and group identity access to content and operations
-   - **Operation Logs** to capture information about operations on a search service.
-   - **allLogs** to collect everything.
-
-   Verbose logging can be expensive to store and complex to manage and store. You might want to start with **allLogs** and then switch to more scoped logging if it meets your information requirements.
-
-1. For a destination, we recommend **Send to Log Analytics workspace** so that you can run Kusto queries against the data.
-
-1. Save the settings.
+[!INCLUDE [horz-monitor-intro](~/reusable-content/ce-skilling/azure/includes/azure-monitor/horizontals/horz-monitor-intro.md)]
 
 > [!NOTE]
-> If you're using [key-based authentication](search-security-api-keys.md), Azure AI Search can't monitor individual user access to content on the search service. If you require this level of monitoring, you need to implement it in your client application.
+> Azure AI Search doesn't log the identity of the person or app accessing content or operations on the search service. If you require this level of monitoring, you need to implement it in your client application.
 
 [!INCLUDE [horz-monitor-resource-types](~/reusable-content/ce-skilling/azure/includes/azure-monitor/horizontals/horz-monitor-resource-types.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchの監視記事の更新"
}
```

### Explanation
この変更は、「monitor-azure-cognitive-search.md」ファイルの内容が修正されたことを示しています。主な更新点は、記事のトピックが「how-to」から「conceptual」に変更され、内容の一部が削減されたことです。特に、診断ログの有効化に関する手順の多くが削除され、もともと詳細に記載されていた手順が要約されています。また、Azure AI Searchによるログの動作に関する軽微な表現変更もあり、アクセスの監視に関する注意事項が簡潔にされました。これにより、文書全体がよりシンプルで理解しやすくなり、ユーザーが重要な情報を迅速に把握できるようになっています。

## articles/search/search-manage.md{#item-4043d7}

<details>
<summary>Diff</summary>
````diff
@@ -98,7 +98,7 @@ Some features add to the cost of running the service:
 
 ### Enable diagnostic logging
 
-[Enable diagnostic logging](monitor-azure-cognitive-search.md#enable-diagnostic-logging) to track user activity. If you skip this step, you still get [activity logs](/azure/azure-monitor/essentials/activity-log)  and [platform metrics](/azure/azure-monitor/essentials/data-platform-metrics#types-of-metrics) automatically, but if you want index and query usage information, you should enable diagnostic logging and choose a destination for logged operations. 
+[Enable diagnostic logging](search-monitor-enable-logging.md) to track user activity. If you skip this step, you still get [activity logs](/azure/azure-monitor/essentials/activity-log)  and [platform metrics](/azure/azure-monitor/essentials/data-platform-metrics#types-of-metrics) automatically, but if you want index and query usage information, you should enable diagnostic logging and choose a destination for logged operations. 
 
 We recommend Log Analytics Workspace for durable storage so that you can run system queries in the Azure portal.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "診断ログを有効にするリンクの更新"
}
```

### Explanation
この変更は、「search-manage.md」ファイルにおいて、診断ログを有効にするためのリンクが更新されたことを示しています。具体的には、元のリンクが「monitor-azure-cognitive-search.md」のセクションに向けられていたのが、「search-monitor-enable-logging.md」へと変更されています。この更新により、ユーザーは診断ログに関するより関連性の高い情報に直接アクセスできるようになり、ユーザーアクティビティの追跡に関する理解が向上します。全体として、ドキュメントの情報の正確性とナビゲーションの向上に寄与する修正です。

## articles/search/search-monitor-enable-logging.md{#item-e3600e}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,109 @@
+---
+title: Configure logging
+titleSuffix: Azure AI Search
+description: Set up diagnostic logging to collect information about indexing and query processing in Azure AI Search resource logs.
+
+manager: nitinme
+author: HeidiSteen
+ms.author: heidist
+ms.service: azure-ai-search
+ms.topic: how-to
+ms.date: 01/28/2025
+---
+
+# Configure diagnostic logging for Azure AI Search
+
+Resource-level diagnostic logs provide insight into operations that occur in your Azure AI Search resource. In contrast, activity logs provide an insight into the operations performed on each Azure resource in the subscription from the outside, known as the control plane or management plane. Activity logging is enabled automatically, and often
+
+This article explains how to enable resource-level diagnostic logging and how to find information about system and user operations on an Azure AI Search resource.
+
+## Prerequisites
+
+- An [Azure Log Analytics workspace](/azure/azure-monitor/logs/quick-create-workspace) in the same subscription.
+
+## Enable diagnostic logging
+
+Diagnostic logging is available through Azure Monitor. Although some logging, like Activity Logs and built-in metrics, is reported automatically with no upfront configuration, resource-level logs about in-service operations and data access require that you create a diagnostic setting and specify a storage option.
+
+1. Sign in to the [Azure portal](https://portal.azure.com) and navigate to your search service.
+
+1. Under **Monitoring** > **Diagnostic settings**, select **Add diagnostic setting**.
+
+1. Provide a name that identifies the service and level of logging, such as "my-search-service-all-logs" or "my-search-service-audit-logs".
+
+1. Under **Logs**, choose a category:
+
+   - **Audit logs** capture user or app interactions with data or the settings of the service, but don't include user or groups identities.
+   - **Operation logs** capture information about operations on a search service.
+   - **allLogs** collect everything.
+
+   Verbose logging can be expensive to store and complex to manage and store. You might want to start with **allLogs** and then switch to more scoped logging if it meets your information requirements. For more information about these categories, see [Diagnostic settings in Azure Monitor](/azure/azure-monitor/essentials/diagnostic-settings).
+
+1. For a destination, we recommend **Send to Log Analytics workspace** so that you can run Kusto queries against the data. There should be a workspace available
+
+1. Save the settings.
+
+Repeat these steps if you require a more [comprehensive data collection strategy](/azure/azure-monitor/logs/workspace-design). 
+
+Each diagnostic setting you create requires its own data sink. If you use the Azure portal to review logs, the first diagnostic setting is used by default. You can navigate to specific workspaces for visualization support.
+
+> [!NOTE]
+> If you're using [key-based authentication](search-security-api-keys.md), Azure AI Search can't monitor individual user access to content on the search service. If you require this level of monitoring, you need to implement it in your client application.
+
+## View logs in Log Analytics
+
+Follow these instructions to explore log analytics data for your resource.
+
+1. Under **Monitoring**, select **Logs**. Query hub opens by default. You can try the available queries, or close the hub and open a query window in KQL mode to run queries written in the [Kusto Query Language (KQL)](/kusto/query).
+
+   :::image type="content" source="media/search-monitor-enable-logging/enable-kql-mode.png" alt-text="Screenshot of the KQL mode option in the Azure portal query explorer.":::
+
+1. In a query window, you can run Kusto queries against your logs.
+
+   :::image type="content" source="media/search-monitor-enable-logging/query-example.png" alt-text="Screenshot of a query and results in the Azure portal.":::
+
+### Sample queries
+
+Here are a few basic Kusto queries you can use to explore your log data.
+
+Run this query for all diagnostic logs from Azure AI Search services over the specified time period:
+
+```kusto
+AzureDiagnostics
+| where ResourceProvider == "MICROSOFT.SEARCH"
+```
+
+Run this query to see the 10 most recent logs:
+
+```kusto
+AzureDiagnostics
+| where ResourceProvider == "MICROSOFT.SEARCH"
+| take 10
+```
+
+Run this query to group operations by **Resource**:
+
+```kusto
+AzureDiagnostics
+| where ResourceProvider == "MICROSOFT.SEARCH" |
+summarize count() by Resource
+```
+
+Run this query to find the average time it takes to perform an operation:
+
+```kusto
+AzureDiagnostics
+| where ResourceProvider == "MICROSOFT.SEARCH"
+| summarize avg(DurationMs)
+by OperationName
+```
+
+Run this query to view the volume of operations over time split by OperationName with counts binned for every 10 seconds.
+
+```kusto
+AzureDiagnostics
+| where ResourceProvider == "MICROSOFT.SEARCH"
+| summarize count()
+by bin(TimeGenerated, 10s), OperationName
+| render areachart kind=unstacked
+```
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Searchの診断ログの設定に関する新しい記事の追加"
}
```

### Explanation
この変更は、「search-monitor-enable-logging.md」という新しいファイルが追加されたことを示しています。このファイルは、Azure AI Searchのリソースログに関する診断ログの設定方法を詳細に説明しています。記事では、リソースレベルの診断ログがどのような情報を提供するか、またアクティビティログとの違いが説明されています。

記事には、Azure Portalでは診断ログを有効にする手順が具体的に記載されており、ユーザーが必要な設定を行い、ログデータをどのように分析するかを学ぶことができます。また、Kusto Query Language (KQL)を使用したサンプルクエリも含まれていて、ユーザーがログアナリティクスデータを探索する際の助けとなる情報が提供されています。

この新しい記事は、Azure AI Searchにおける監視能力を強化するための重要なリソースであり、ユーザーが効率的にサービスを管理するのに役立ちます。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -516,6 +516,8 @@ items:
     items:
     - name: Monitor
       href: monitor-azure-cognitive-search.md
+    - name: Enable diagnostic logging
+      href: search-monitor-enable-logging.md
     - name: Monitor queries
       href: search-monitor-queries.md
     - name: Monitor indexer-based indexing
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次ファイルへの新しい項目の追加"
}
```

### Explanation
この変更は、「toc.yml」ファイルにおいて新しい項目が追加されたことを示しています。具体的には、診断ログを有効にするためのリンク「search-monitor-enable-logging.md」が追加されました。このリンクは、Azure AI Searchにおいて診断ログを有効にする手順に関する情報を提供する新しいドキュメントを参照しており、ユーザーがログの設定やモニタリングを簡単に行えるようにサポートします。

この変更により、ユーザーは「Monitor」セクションにおいてより多くのリソースを閲覧でき、診断ログの有効化に関する具体的なガイドが直接ナビゲート可能になります。全体として、この更新はドキュメントの使いやすさを向上させ、Azure AI Searchの管理作業を効率化することに寄与します。

## articles/search/vector-search-how-to-configure-vectorizer.md{#item-30ffd8}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ Vectorizers are now generally available as long as you use a generally available
 
 + [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) to send the query and accept a response.
 
-We recommend that you [enable diagnostic logging](monitor-azure-cognitive-search.md#enable-diagnostic-logging) on your search service to confirm vector query execution.
+We recommend that you [enable diagnostic logging](search-monitor-enable-logging.md) on your search service to confirm vector query execution.
 
 ## Supported embedding models
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "診断ログ有効化のリンクの更新"
}
```

### Explanation
この変更は、「vector-search-how-to-configure-vectorizer.md」ファイル内の診断ログを有効にするためのリンクが更新されたことを示しています。具体的には、以前のリンク「monitor-azure-cognitive-search.md#enable-diagnostic-logging」から新しいリンク「search-monitor-enable-logging.md」に変更されています。

この更新により、ユーザーがベクトルクエリの実行を確認するために診断ログを有効化する際に、より関連性の高い情報にリダイレクトされることになります。新しいリンクは、診断ログの設定に関する詳細な手順を提供する新しく追加されたドキュメントに接続されており、ユーザーの操作性を向上させることを目的としています。全体として、この変更はドキュメントの精度と有用性を高める効果があります。

## articles/search/vector-store.md{#item-db9b8c}

<details>
<summary>Diff</summary>
````diff
@@ -211,7 +211,7 @@ Azure AI Search implements data encryption, private connections for no-internet
 
 Azure provides a [monitoring platform](monitor-azure-cognitive-search.md) that includes diagnostic logging and alerting. We recommend the following best practices:
 
-+ [Enable diagnostic logging](monitor-azure-cognitive-search.md#enable-diagnostic-logging)
++ [Enable diagnostic logging](search-monitor-enable-logging.md)
 + [Set up alerts](/azure/azure-monitor/alerts/tutorial-metric-alert)
 + [Analyze query and index performance](search-performance-analysis.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "診断ログ有効化のリンクの更新"
}
```

### Explanation
この変更は、「vector-store.md」ファイル内での診断ログを有効にするためのリンクが更新されたことを示しています。具体的には、以前のリンク「monitor-azure-cognitive-search.md#enable-diagnostic-logging」が新しいリンク「search-monitor-enable-logging.md」に変更されました。

この更新により、ユーザーは診断ログを有効にする際に、より正確で関連性の高い情報にアクセスできるようになります。新しいリンクは、診断ログの設定方法についての詳しい手順を提供しているため、ユーザーの利便性が向上します。さらに、 Azure のモニタリングプラットフォームに関連するベストプラクティスを示す内容がより効果的にサポートされることになります。この修正はドキュメントの使いやすさと精度を高め、ユーザーがより効率的に作業を行えるようにすることを目的としています。


