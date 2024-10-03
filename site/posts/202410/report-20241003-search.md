---
date: '2024-10-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b0599a2...MicrosoftDocs:94dabc3
summary: Azureのドキュメントが更新され、コグニティブ検索のデバッグやインデクサのスケジューリング、プライベートリンクに関する情報が追加されました。新しい制約や推奨事項が盛り込まれ、ユーザーがシステムをより効果的に活用できるようサポートしています。特に、カスタムスキルに関する接続制限やインデクサの動作に関する具体的な仕様が明記され、最新のAPI推奨も含まれています。破壊的な変更はありませんが、ドキュメントの利用における最新要件が明示されています。これにより、Azureユーザーの体験が向上し、運用効率が高まることが期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b0599a2...MicrosoftDocs:94dabc3){target="_blank"}

# Highlights

Azureの各種機能に関するドキュメントの更新が行われました。これには、コグニティブ検索のデバッグやインデクサのスケジューリング、プライベートリンクによるアウトバウンド接続の情報が含まれています。文書の最新化と新しい制約や推奨事項が追加されており、利用者がシステムをより適切に活用する手助けとなります。

## New features

- カスタムスキルに関する情報や、デバッグセッションにおける制限が追加。
- インデクサの動作に関する具体的な仕様と推奨事項。
- プライベートリンクを利用した接続において最新のAPI推奨が追加。

## Breaking changes

- 特に破壊的な変更はありませんが、ドキュメントの利用における最新要件や制約が明記されています。

## Other updates

- ドキュメントの日付の更新。
- マルチテナント環境の非対応についての言及追加。

# Insights

今回の更新では、Azureユーザー向けのドキュメントにおいていくつかの重要な情報追加が行われています。まず、コグニティブ検索のデバッグセッションに関する文書では、カスタムスキルに関する接続制限が新たに加わりました。これによりユーザーは特定の制約を考慮しながらデバッグを実施できます。また、インデクサのスケジューリング方法では、失敗時の頻度調整や「プッシュモデル」の検討を推奨する具体例が示されるなど、インデクシングの効率を最大化するための情報が充実しています。

さらに、プライベートリンクを利用したアウトバウンド接続に関する文書の更新では、特にマルチテナント環境から接続がサポートされないことや、最新のプレビューAPIの使用推奨が追加されたことが目を引きます。これにより、ユーザーはセキュリティや接続性を満たすための設計を精査できます。各ドキュメントの更新によって、Azureにおけるユーザー体験が向上し、システムの運用効率を上げるための指針が明確になります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-debug-session.md](#item-edf092) | minor update | コグニティブ検索のデバッグセッションに関する文書の更新 | modified | 3 | 1 | 4 | 
| [cognitive-search-how-to-debug-skillset.md](#item-31db42) | minor update | AzureポータルでのAI検索スキルセットのデバッグに関する文書の更新 | modified | 5 | 3 | 8 | 
| [search-howto-schedule-indexers.md](#item-d57e7b) | minor update | Azure AI Searchにおけるインデクサのスケジューリング方法に関する文書の更新 | modified | 12 | 9 | 21 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | プライベートリンクを介したアウトバウンド接続に関する文書の更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/cognitive-search-debug-session.md{#item-edf092}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 08/20/2024
+ms.date: 10/01/2024
 ---
 
 # Debug Sessions in Azure AI Search
@@ -53,6 +53,8 @@ Debug Sessions work with all generally available [indexer data sources](search-d
 
 + For custom skills, a user-assigned managed identity isn't supported for a debug session connection to Azure Storage. As stated in the prerequisites, you can use a system managed identity, or specify a full access connection string that includes a key. For more information, see [Connect a search service to other Azure resources using a managed identity](search-howto-managed-identities-data-sources.md).
 
++ Currently, the ability to select which document to debug is unavailable. This limitation is not permanent and will be lifted soon. At this time, Debug Sessions selects the first document in the source data container or folder.
+
 ## How a debug session works
 
 When you start a session, the search service creates a copy of the skillset, indexer, and a data source containing a single document used to test the skillset. All session state is saved to a new blob container created by the Azure AI Search service in an Azure Storage account that you provide. The name of the generated container has a prefix of `ms-az-cognitive-search-debugsession`. The prefix is required because it mitigates the chance of accidentally exporting session data to another container in your account. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブ検索のデバッグセッションに関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるデバッグセッションに関する文書の小規模な更新です。具体的には、ドキュメントの日付が2024年8月20日から2024年10月1日に変更され、カスタムスキルに関連する接続制限についての情報が追加されました。ユーザーが選択可能なドキュメントが現在利用できないとの説明も加わり、この制限は一時的なものであることが明記されています。最初のドキュメントがデバッグセッションで自動的に選択されるという仕様も述べられています。この更新により、デバッグセッションの利用者が理解しやすくなり、機能に関する重要な情報が提供されました。

## articles/search/cognitive-search-how-to-debug-skillset.md{#item-31db42}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 08/20/2024
+ms.date: 10/01/2024
 ---
 
 # Debug an Azure AI Search skillset in Azure portal
@@ -51,6 +51,8 @@ Debug sessions work with all generally available [indexer data sources](search-d
 
 + For custom skills, a user-assigned managed identity isn't supported for a debug session connection to Azure Storage. As stated in the prerequisites, you can use a system managed identity, or specify a full access connection string that includes a key. For more information, see [Connect a search service to other Azure resources using a managed identity](search-howto-managed-identities-data-sources.md).
 
++ Currently, the ability to select which document to debug is unavailable. This limitation is not permanent and will be lifted soon. At this time, Debug Sessions selects the first document in the source data container or folder.
+
 ## Create a debug session
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
@@ -79,11 +81,11 @@ Debug sessions work with all generally available [indexer data sources](search-d
 
 1. In **Storage connection string**, you can specify the connection string or change the storage account. 
 
-1. In **Document to debug**, choose the first document in the index or select a specific document. If you select a specific document, depending on the data source, you're asked for a URI or a row ID.
+   <!-- 1. In **Document to debug**, choose the first document in the index or select a specific document. If you select a specific document, depending on the data source, you're asked for a URI or a row ID.
 
    If your specific document is a blob, provide the blob URI. You can find the URI in the blob property page in the portal.
 
-   :::image type="content" source="media/cognitive-search-debug/copy-blob-url.png" lightbox="media/cognitive-search-debug/copy-blob-url.png" alt-text="Screenshot of the URI property in blob storage." border="true":::
+   :::image type="content" source="media/cognitive-search-debug/copy-blob-url.png" lightbox="media/cognitive-search-debug/copy-blob-url.png" alt-text="Screenshot of the URI property in blob storage." border="true"::: -->
 
 1. Optionally, in **Indexer settings**, specify any [indexer execution settings](search-howto-indexing-azure-blob-storage.md) used to create the session. The settings should mirror the settings used by the actual indexer. Any indexer options that you specify in a debug session have no effect on the indexer itself.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AzureポータルでのAI検索スキルセットのデバッグに関する文書の更新"
}
```

### Explanation
この変更は、AzureポータルでのAI検索スキルセットをデバッグする方法に関する文書の小規模な更新です。具体的には、文書の日付が2024年8月20日から2024年10月1日に変更され、カスタムスキルとAzureストレージへの接続に関する重要な情報が新たに追加されました。さらに、デバッグセッション中に選択できるドキュメントが現在利用できないという制限が明記されており、この制限は一時的なものであるという説明も付け加えられています。また、デバッグセッションが最初のドキュメントを自動的に選択することが示されています。この更新により、ユーザーはデバッグセッションの操作に関する最新の情報を取得でき、どのように進めるかの理解が深まることを目的としています。

## articles/search/search-howto-schedule-indexers.md{#item-d57e7b}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 01/17/2024
+ms.date: 10/02/2024
 ---
 
 # Schedule an indexer in Azure AI Search
@@ -105,22 +105,25 @@ await indexerClient.CreateOrUpdateIndexerAsync(indexer);
 
 ## Scheduling behavior
 
-For text-based indexing, the scheduler can kick off as many indexer jobs as the search service supports, which is determined by the number of search units. For example, if the service has three replicas and four partitions, you can have 12 indexer jobs in active execution, whether initiated on demand or on a schedule.
++ For text-based indexing, the scheduler can kick off as many indexer jobs as the search service supports, which is determined by the number of search units. For example, if the service has three replicas and four partitions, you can have 12 indexer jobs in active execution, whether initiated on demand or on a schedule.
 
-Skills-based indexers run in a different [execution environment](search-howto-run-reset-indexers.md#indexer-execution). For this reason, the number of service units has no bearing on the number of skills-based indexer jobs you can run. Multiple skills-based indexers can run in parallel, but doing so depends on node availability within the execution environment.
++ Skills-based indexers run in a different [execution environment](search-howto-run-reset-indexers.md#indexer-execution). For this reason, the number of service units has no bearing on the number of skills-based indexer jobs you can run. Multiple skills-based indexers can run in parallel, but doing so depends on node availability within the execution environment.
 
-Although multiple indexers can run simultaneously, a given indexer is single instance. You can't run two copies of the same indexer concurrently. If an indexer happens to still be running when its next scheduled execution is set to start, the pending execution is postponed until the next scheduled occurrence, allowing the current job to finish.
++ Although multiple indexers can run simultaneously, a given indexer is single instance. You can't run two copies of the same indexer concurrently. If an indexer happens to still be running when its next scheduled execution is set to start, the pending execution is postponed until the next scheduled occurrence, allowing the current job to finish.
+
++ If an indexer is set to a certain schedule but repeatedly fails on the same document each time, the indexer will begin running on a less frequent interval (up to the maximum interval of at least once every 2 hours or 24 hours, depending on different implementation factors) until it successfully makes progress again. If you believe you have fixed whatever the underlying issue, you can [run the indexer manually](search-howto-run-reset-indexers.md), and if indexing succeeds, the indexer will return to its regular schedule.
+
++ Indexer processes can be queued up and may not start exactly at the time posted, depending on the processing workload and other factors. Based on this, If there is a strict business need tied to the exact time indexing is performed, you should consider using the [Push model](search-what-is-data-import.md#pushing-data-to-an-index) so you can control the indexing pipeline directly.
 
 Let’s consider an example to make this more concrete. Suppose we configure an indexer schedule with an interval of hourly and a start time of January 1, 2024 at 8:00:00 AM UTC. Here's what could happen when an indexer run takes longer than an hour:
 
-+ The first indexer execution starts at or around January 1, 2024 at 8:00 AM UTC. Assume this execution takes 20 minutes (or any amount of time that's less than 1 hour).
+1. The first indexer execution starts at or around January 1, 2024 at 8:00 AM UTC. Assume this execution takes 20 minutes (or any amount of time that's less than 1 hour).
 
-+ The second execution starts at or around January 1, 2022 9:00 AM UTC. Suppose that this execution takes 70 minutes - more than an hour – and it will not complete until 10:10 AM UTC.
+1. The second execution starts at or around January 1, 2022 9:00 AM UTC. Suppose that this execution takes 70 minutes - more than an hour – and it will not complete until 10:10 AM UTC.
 
-+ The third execution is scheduled to start at 10:00 AM UTC, but at that time the previous execution is still running. This scheduled execution is then skipped. The next execution of the indexer won't start until 11:00 AM UTC.
+1. The third execution is scheduled to start at 10:00 AM UTC, but at that time the previous execution is still running. This scheduled execution is then skipped. The next execution of the indexer won't start until 11:00 AM UTC.
+  
 
-> [!NOTE]
-> If an indexer is set to a certain schedule but repeatedly fails on the same document each time, the indexer will begin running on a less frequent interval (up to the maximum interval of at least once every 2 hours or 24 hours, depending on different implementation factors) until it successfully makes progress again. If you believe you have fixed whatever the underlying issue, you can [run the indexer manually](search-howto-run-reset-indexers.md), and if indexing succeeds, the indexer will return to its regular schedule.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおけるインデクサのスケジューリング方法に関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるインデクサのスケジューリング方法に関する文書の小規模な更新です。特に、文書の日付が2024年1月17日から2024年10月2日に変更されました。更新された内容には、インデクサが特定のドキュメントで何度も失敗した場合に、実行頻度が減少する仕組みや、正確なインデクシングのタイミングがビジネスニーズに関連する場合に「プッシュモデル」の使用を検討すべきであるとの推奨が含まれています。また、インデクサの実行スケジュール処理の具体例も追加されています。この情報は、ユーザーがインデクサの動作をより良く理解し、適切なスケジュール管理を行えるようにすることを目的としています。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: mrcarter8
 ms.author: mcarter
 ms.service: cognitive-search
 ms.topic: how-to
-ms.date: 08/06/2024
+ms.date: 09/17/2024
 ---
 
 # Make outbound connections through a shared private link
@@ -60,7 +60,7 @@ While both scenarios have a dependency on Azure Private Link, they're independen
 
 When evaluating shared private links for your scenario, remember these constraints.
 
-+ Several of the resource types used in a shared private link are in preview. If you're connecting to a preview resource (Azure Database for MySQL, Azure Functions, or Azure SQL Managed Instance), use a preview version of the Management REST API to create the shared private link. These versions include `2020-08-01-preview`, `2021-04-01-preview`, `2024-03-01-preview`, and `2024-06-01-preview`. We recommend the latest preview API.
++ Several of the resource types used in a shared private link are in preview. If you're connecting to a preview resource (Azure Database for MySQL or Azure SQL Managed Instance), use a preview version of the Management REST API to create the shared private link. These versions include `2020-08-01-preview`, `2021-04-01-preview`, `2024-03-01-preview`, and `2024-06-01-preview`. We recommend the latest preview API.
 
 + Indexer execution must use the private execution environment that's specific to your search service. Private endpoint connections aren't supported from the multitenant environment. The configuration setting for this requirement is covered in this article.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートリンクを介したアウトバウンド接続に関する文書の更新"
}
```

### Explanation
この変更は、プライベートリンクを介したアウトバウンド接続に関する文書の小規模な更新です。文書の日付が2024年8月6日から2024年9月17日に更新され、新たにインデクサの実行には特定のプライベートエンドポイント接続が必要であり、マルチテナント環境からの接続はサポートされないことが明記されました。また、プレビュー中のリソースタイプ（Azure Database for MySQLやAzure SQL Managed Instance）についての言及も若干変更され、最新のプレビューAPIを使用することが推奨されています。この更新により、ユーザーはプライベートリンクを使用した接続に関する最新の要件と制約を理解しやすくなります。


