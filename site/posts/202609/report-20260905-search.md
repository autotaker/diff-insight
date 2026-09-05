---
date: '2026-09-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:453abd5...MicrosoftDocs:1d9b499
summary: このコーディフは、SharePointリモートナレッジソースとAzure AI Searchに関する記事の更新を含み、主に制限事項や地域サポートの情報を強化しています。具体的な変更点としては、リモートクエリの制限事項の明確化やリトリーブリクエストの実行時間の範囲の提示、米国西部地域のサポート情報の修正が挙げられます。また、新たにリトリーブリクエストに関する実行時間の制限（10秒から600秒）が追加されました。破壊的な変更は特にありませんが、情報の更新は利用者に影響を与える可能性があります。この更新は、開発者が機能を正しく設定し、活用するための理解を深めることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:453abd5...MicrosoftDocs:1d9b499){target="_blank"}

<format>
# ハイライト
このコーディフによって、SharePointリモートナレッジソースやAzure AI Searchに関する記事が更新され、特に制限事項や地域サポートに関する詳細情報が追加されました。主だった変更として、リモートクエリの制限事項の明確化、リトリーブリクエストの制限時間の具体的な範囲、米国西部地域のサポート情報の修正があります。

## 新機能
- 新しい制限事項が追加：リトリーブリクエストの実行時間とその範囲（10秒から600秒）。
- Azure AI Searchにおけるリモートクエリやナレッジソースの使用に関連する情報の追加。

## 破壊的な変更
- 特に破壊的な変更はありませんが、情報の更新により一部の利用者の理解や設定が変わる可能性があります。

## その他の更新
- 記事の日付がアップデートされ、今後のバージョンの正確性を維持。
- 地域サポートにおける情報の再整理により、より正確な情報提供。

# インサイト
今回の更新は、主にSharePointリモートナレッジの利用とAzure AI Searchの機能に対する理解を深めることを目的としています。特に、APIやリモートクエリの制限に関する情報をより詳細に示すことで、開発者やユーザーが正しく設定を行い、機能を最大限に活用できるようにする意図があります。

`articles/search/agentic-knowledge-source-how-to-sharepoint-remote.md`では、リモートSharePointから情報を取得する際の具体的な制限が明確化され、より具体的な使用テクニックが得られます。これは、特に大規模なデータを扱う企業や組織にとって有益であり、制限を把握した運用が可能となります。

また、`articles/search/agentic-retrieval-how-to-retrieve.md`および`articles/search/search-limits-quotas-capacity.md`の記事改訂により、Azure AI Searchのリトリーブリクエストに関する時間的制約が詳説されました。デフォルト設定と最大設定を知ることで、レスポンスタイムを最適化しユーザー体験を向上させることが可能となります。

最後に、`articles/search/search-region-support.md`における米国西部地域のサポート情報の修正は、地域特有の機能サポート状況を明確に把握し、開発者が地域に応じた最適なサービス利用プランを立てる一助となります。これにより、情報の一貫性と透明性を高めることができ、ユーザーがより正確な意思決定を行えるようになるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-sharepoint-remote.md](#item-79d019) | minor update | SharePointリモートナレッジソースに関する情報の更新 | modified | 14 | 2 | 16 | 
| [agentic-retrieval-how-to-retrieve.md](#item-d739cf) | minor update | リトリーバルのリクエスト制限に関する情報の更新 | modified | 4 | 2 | 6 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | リトリーブリクエストの実行時間に関する情報の追加 | modified | 11 | 1 | 12 | 
| [search-region-support.md](#item-25b0f1) | minor update | 米国西部地域のサポート情報の修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-sharepoint-remote.md{#item-79d019}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Create a SharePoint (Remote) Knowledge Source
 description: Learn how to create a remote SharePoint knowledge source, which tells an agentic retrieval engine in Azure AI Search to query SharePoint sites directly.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/02/2026
+ms.date: 09/03/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
@@ -71,7 +71,11 @@ Unlike indexed knowledge sources, remote SharePoint knowledge sources query live
 
 ## Limitations and considerations
 
-The following limitations and considerations in the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) apply to remote SharePoint knowledge sources.
+Remote SharePoint knowledge sources are subject to limitations from the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) and Azure AI Search.
+
+### Copilot Retrieval API
+
+The following Copilot Retrieval API limitations also apply to remote SharePoint knowledge sources:
 
 + There's no support for Copilot connectors or OneDrive content. Content is retrieved from SharePoint sites only.
 
@@ -89,6 +93,14 @@ The following limitations and considerations in the [Copilot Retrieval API](/mic
 
 + Invalid Keyword Query Language (KQL) filter expressions are ignored, and the query continues to execute without the filter.
 
+### Azure AI Search
+
+When you query a knowledge base, Azure AI Search can run a limited number of remote SharePoint queries at a time. The limit depends on the pricing model:
+
++ [Dedicated](search-sku-tier.md#dedicated-pricing-model): Each service replica runs one query at a time across all remote SharePoint knowledge sources selected for the retrieve request. Additional queries wait for an available replica, which increases latency. To increase query throughput, [add replicas](search-capacity-planning.md#add-or-remove-partitions-and-replicas).
+
++ [Serverless (preview)](search-sku-tier.md#serverless-pricing-model-preview): Azure AI Search runs one query at a time across all remote SharePoint knowledge sources selected for the retrieve request. Additional queries wait. Serverless manages capacity automatically, so you can't increase query throughput.
+
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources](includes/how-tos/knowledge-source-check.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointリモートナレッジソースに関する情報の更新"
}
```

### Explanation
この変更は、SharePointリモートナレッジソースに関する記事の内容を更新するものです。主に以下のポイントが変更されました：

- 説明の日付が「2026年6月2日」から「2026年9月3日」に変更されました。
- リモートSharePointナレッジソースに関連する制限事項が、Copilot Retrieval APIとAzure AI Searchに関する新しい見出しの下にまとめられました。
- Copilot Retrieval APIに対する具体的な制限が詳細に追加され、リモートSharePointからのデータ取得についての理解が深まる内容になっています。
- Azure AI Searchによるリモートクエリの制限が詳細に説明され、特定のプライシングモデルに基づくクエリの実行可能数についても言及されています。

これにより、ユーザーはリモートSharePointナレッジソースを利用する際の注意事項や制限をより明確に理解できるようになります。

## articles/search/agentic-retrieval-how-to-retrieve.md{#item-d739cf}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Query Knowledge Base via API or MCP
 description: Learn how to query a knowledge base using the retrieve action or MCP endpoint in Azure AI Search using REST APIs, Azure SDKs, or any MCP-compatible client.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/18/2026
+ms.date: 09/04/2026
 ms.custom:
   - dev-focus
   - doc-kit-assisted
@@ -2453,7 +2453,9 @@ The reference count shows whether the stored or request-level `maxOutputDocument
 
 ### Override default reasoning effort and set request limits
 
-The following example specifies [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md), so the retrieval reasoning effort must be `low` or `medium`. It also sets `maxRuntimeInSeconds` to cap total request latency and `maxOutputSizeInTokens` to bound the response payload.
+The following example specifies [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md), so the retrieval reasoning effort must be `low` or `medium`. It also sets `maxRuntimeInSeconds` to limit retrieval runtime and `maxOutputSizeInTokens` to limit response payload size.
+
+`maxRuntimeInSeconds` accepts values from 10 through 600 seconds and defaults to 90 seconds. The 600-second (10-minute) maximum applies only to the Azure AI Search retrieve request.
 
 :::zone pivot="csharp"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リトリーバルのリクエスト制限に関する情報の更新"
}
```

### Explanation
この変更は、Azure AI Searchを使用して知識ベースをクエリする方法に関する記事の内容を更新したものです。いくつかの重要なポイントが修正され、新たに情報が追加されています。

- 説明の日付が「2026年8月18日」から「2026年9月4日」に更新されました。
- リトリーバルのリクエスト制限に関する文が改訂され、`maxRuntimeInSeconds`の設定についての説明がより明確になりました。新たに、`maxRuntimeInSeconds`が10秒から600秒の範囲で設定できること、デフォルト値は90秒であり、600秒がAzure AI Searchのリトリーブリクエストにのみ適用されることが明記されました。

これらの追加情報は、ユーザーがリクエストの実行時間とレスポンスのサイズを管理する際の理解を助けることを目的としています。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: mattwojo
 ms.author: mattwoj
 ms.service: azure-ai-search
 ms.topic: limits-and-quotas
-ms.date: 09/03/2026
+ms.date: 09/04/2026
 ms.update-cycle: 180-days
 ai-usage: ai-assisted
 ms.custom:
@@ -337,6 +337,16 @@ The `2025-08-01-preview` uses the legacy knowledge agent contract and doesn't su
 
 <sup>2</sup> The `minimal` reasoning effort uses all knowledge sources in the knowledge base because it bypasses LLM-based query planning.
 
+### Retrieve request runtime
+
+The `maxRuntimeInSeconds` limit is the same across supported tiers.
+
+| Minimum | Default | Maximum |
+|--|--|--|
+| 10 seconds | 90 seconds | 600 seconds (10 minutes) |
+
+The maximum applies only to the Azure AI Search retrieve request. For configuration examples, see [Override default reasoning effort and set request limits](agentic-retrieval-how-to-retrieve.md#override-default-reasoning-effort-and-set-request-limits).
+
 ## Data limits (AI enrichment)
 
 Data limits apply to an [AI enrichment pipeline](cognitive-search-concept-intro.md) that calls Azure Language in Foundry Tools. The maximum input is 50,000 characters, as measured by [`String.Length`](/dotnet/api/system.string.length), for the [Entity Recognition skill](cognitive-search-skill-entity-recognition-v3.md#data-limits), [Entity Linking skill](cognitive-search-skill-entity-linking-v3.md#data-limits), [Key Phrase Extraction skill](cognitive-search-skill-keyphrases.md#data-limits), [Language Detection skill](cognitive-search-skill-language-detection.md#data-limits), and [PII Detection skill](cognitive-search-skill-pii-detection.md#data-limits). The [Sentiment skill](cognitive-search-skill-sentiment-v3.md#data-limits) has a 5,000-character maximum.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リトリーブリクエストの実行時間に関する情報の追加"
}
```

### Explanation
この変更は、Azure AI Searchの検索制限、クォータ、およびキャパシティに関する記事を更新したものです。以下の主な点が改訂されました：

- 記事の日付が「2026年9月3日」から「2026年9月4日」に更新されました。
- リトリーブリクエストの実行時間に関する新しいセクションが追加され、`maxRuntimeInSeconds`の制限に関する情報が提供されました。このセクションでは、サポートされているすべてのティアで `maxRuntimeInSeconds` の制限が同じであることが明記され、以下の表が含まれています：

  | 最小値 | デフォルト | 最大値 |
  |--|--|--|
  | 10秒 | 90秒 | 600秒 (10分) |

- 最大値の適用対象がAzure AI Searchのリトリーブリクエストのみに限定されることも説明されています。また、リクエスト制限を設定するための構成例にリンクが追加されています。

この変更により、ユーザーはリトリーブリクエストの制限をより明確に理解し、適切な設定を行うための情報が得られるようになります。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -55,8 +55,8 @@ You can create an Azure AI Search service in any of the following Azure public r
 | North Central US​ <sup>1</sup> ​| ✅ | ✅ | ✅ | ✅ |  | ✅ |
 | South Central US​ <sup>1 </sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | West US​​ <sup>1, 2</sup> | ✅ | ✅ | ✅ | ✅ |  | ✅ |
-| West US 2​ <sup>2,3</sup> ​| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| West US 3​ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| West US 2​ <sup>3</sup> ​| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
+| West US 3​ <sup>2</sup>| ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | West Central US​ ​<sup>1</sup>| ✅ | ✅ | ✅ | ✅ |  |  |
 
 <sup>1</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "米国西部地域のサポート情報の修正"
}
```

### Explanation
この変更は、Azure AI Searchのサポート地域に関する記事を更新したもので、特に米国西部地域に関する情報の整備が行われました。以下のポイントが修正されました：

- 表内の「West US 2」と「West US 3」の行に関して、サポート情報を整理しました。具体的には、元の「West US 2」行の注釈を「<sup>2,3</sup>」から「<sup>3</sup>」に、さらに「West US 3」の行には新たに「<sup>2</sup>」という注釈が追加されました。
- これにより、各地域でサポートされている機能についての情報がより正確になり、ユーザーは地域ごとのサポート内容を理解しやすくなります。

この更新により、ドキュメント全体の一貫性が保たれ、読者に対して明瞭な情報が提供されることを目的としています。


