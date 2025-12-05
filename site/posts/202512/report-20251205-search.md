---
date: '2025-12-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:cad893f...MicrosoftDocs:c92dde6
summary: この差分は検索関連の記事に対してマイナーな更新を行い、特にエージェント知識ソースや新しいデータ取得オプションに関する情報が整理されました。著者情報やファイル名の正確性が向上し、一部の記事では大幅な改訂がなされています。新機能としては、データ取得元の拡充や新しい回答合成機能が導入され、推論努力の設定が詳細化されています。また、「Azure
  Searchとは何か？」の記事も大幅に改訂され、Azure AI Searchの機能を明確に伝える内容に改善されています。全体的なアップデートは技術の最新トレンドを反映し、ユーザーに利便性を提供しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:cad893f...MicrosoftDocs:c92dde6){target="_blank"}

# Highlights
この差分は主に検索関連の記事にマイナーな更新を加えたものです。特に、エージェント知識ソースと検索に関する情報がより明確に整理され、新しい取得オプションやコンテンツ処理方法が追加されています。一部の記事では著者情報やファイル名の正確性が更新され、ある記事に関しては大幅な改訂が行われました。

## New features
- エージェント知識ソースの生成方法および統合方法の詳細が明記。
- 新しい取得オプションとして、OneLake、SharePoint、Bingインデックスからのデータ取得がサポート。
- 大規模言語モデル（LLM）を活用した新しい回答合成機能が導入。
- 推論努力の設定を通じた処理レベルの選択肢が詳細化。

## Breaking changes
- "Azure Searchとは何か？” 記事の内容が大幅に改訂。Azure AI Searchの機能と構成が再定義。

## Other updates
- 著者情報の更新。
- ファイル名の拡張子の修正。
- REST API使用時におけるCURLヘッダー設定のヒント追加。
- 検索関連性とコスト管理に関する新しい情報追加。

# Insights
今回のアップデートでは、記事の内容が全体的に最新の技術傾向を反映する形で更新されています。特に、エージェント知識ソースに関する情報が整理され、新たな取得オプションが実装されたことは、新しいデータソース統合への対応を示しています。これにより、より幅広いシナリオでの応用が可能となり、ユーザーにとっては多様なデータ環境での利便性が向上することでしょう。

推論努力に関しては、処理の柔軟性とコスト面での調整が可能となり、ユーザーは適切な処理レベルを選択することで、パフォーマンス最適化とリソース管理が行えるようになります。特に、`medium`取得推論努力の導入は、継続的なクエリの改善に寄与するものです。

"Azure Searchとは何か？”についての大幅な改訂は、Azure AI Searchが提供する機能をよりわかりやすくユーザーに伝えるために不可欠なものです。これは、従来の検索インフラだけでなく、エージェントや大規模言語モデルとの連携能力を強調することで、先進的な情報取得ソリューションとしてのAzure AI Searchのポジショニングを明確化します。

他のマイナーな更新についても、ドキュメントの正確性と信頼性を高める試みであり、ユーザーエクスペリエンスの向上に繋がっています。これらの更新は、最新情報の提供と共に、技術文章の透明性を維持するための重要なステップです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-overview.md](#item-dcf29a) | minor update | エージェント知識ソースの概要の更新 | modified | 29 | 26 | 55 | 
| [agentic-retrieval-how-to-migrate.md](#item-9653ea) | minor update | エージェント検索の移行手順の更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-how-to-retrieve.md](#item-d739cf) | minor update | エージェント検索でのデータ取得手順の更新 | modified | 3 | 1 | 4 | 
| [agentic-retrieval-how-to-set-retrieval-reasoning-effort.md](#item-141e97) | minor update | 取得推論努力の設定手順の更新 | modified | 23 | 6 | 29 | 
| [agentic-retrieval-overview.md](#item-d1f354) | minor update | エージェント検索の概要に関する更新 | modified | 11 | 1 | 12 | 
| [cognitive-search-skill-annotation-language.md](#item-aaedc7) | minor update | スキル注釈言語の著者情報の更新 | modified | 1 | 1 | 2 | 
| [search-how-to-index-cosmosdb-sql.md](#item-2e888b) | minor update | Cosmos DB サンプルデータのファイル名の修正 | modified | 1 | 1 | 2 | 
| [search-manage-rest.md](#item-405ec7) | minor update | 管理REST APIに関するチップの追加と日付の更新 | modified | 4 | 1 | 5 | 
| [search-relevance-overview.md](#item-cb0e09) | minor update | 検索の関連性に関する概念記事の更新 | modified | 4 | 3 | 7 | 
| [search-what-is-azure-search.md](#item-93853a) | breaking change | Azure AI Searchに関する記事の大幅な改訂 | modified | 105 | 57 | 162 | 
| [tutorial-adls-gen2-indexer-acls.md](#item-6881a0) | minor update | ADLS Gen2インデクサーの著者情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/agentic-knowledge-source-overview.md{#item-dcf29a}

<details>
<summary>Diff</summary>
````diff
@@ -7,22 +7,22 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 11/10/2025
+ms.date: 12/04/2025
 ---
 
 # What is a knowledge source?
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-A knowledge source specifies the content used for agentic retrieval. It encapsulates a search index which may be populated by an external data source, or a direct connection to a remote source such as Bing or Sharepoint that is queried directly. A knowledge source is a required definition in a knowledge base.
+A knowledge source specifies the content used for agentic retrieval. It either encapsulates a search index which is populated by an external data source, or it's a direct connection to a remote source such as Bing or Sharepoint that's queried directly. A knowledge source is a required definition in a knowledge base.
 
 + Create a knowledge source as a top-level resource on your search service. Each knowledge source points to exactly one data structure, either a search index that [meets the criteria for agentic retrieval](agentic-retrieval-how-to-create-index.md) or a supported external resource.
 
-+ Reference one or more knowledge sources in a knowledge base. In an agentic retrieval pipeline, it's possible to query against multiple knowledge sources in a single request. Subqueries are generated for each knowledge source. Top results are returned in the retrieval response.
++ Reference one or more knowledge sources in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md). In an agentic retrieval pipeline, it's possible to query against multiple knowledge sources in a single request. Subqueries are generated for each knowledge source. Top results are returned in the retrieval response.
 
 + For certain knowledge sources, you can use a knowledge source definition to generate a full indexer pipeline (data source, skillset, indexer, and index) that works for agentic retrieval. Instead of creating multiple objects manually, information in the knowledge source is used to generate all objects, including a populated, chunked, and searchable index.
 
-Make sure you have at least one knowledge source before creating a knowledge base. The full specification of a knowledge source and a knowledge base is in the [preview REST API reference](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true).
+Make sure you have at least one knowledge source before creating a knowledge base. The full specification of a knowledge source and a knowledge base can be found in the [preview REST API reference](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true).
 
 ## Working with a knowledge source
 
@@ -36,15 +36,25 @@ Make sure you have at least one knowledge source before creating a knowledge bas
 
 Here are the knowledge sources you can create in this preview:
 
-+ [`"searchIndex"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#searchindexknowledgesource) wraps an existing index.
-+ [`"azureBlob"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#azureblobknowledgesource) generates an indexer pipeline that pulls from a blob container.
-+ [`"indexedOneLake"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#indexedonelakeknowledgesource) generates an indexer pipeline that pulls from a lakehouse.
-+ [`"indexedSharePoint"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#indexedsharepointknowledgesource) generates an indexer pipeline that pulls from a SharePoint site.
-+ [`"remoteSharePoint"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#remotesharepointknowledgesource) retrieves content directly from SharePoint.
-+ [`"webParameters"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#webknowledgesource) retrieves real-time grounding data from Microsoft Bing.
+| Kind | Indexed or remote |
+|------|-------------------|
+| [`"searchIndex"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#searchindexknowledgesource) wraps an existing index. | Indexed |
+| [`"azureBlob"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#azureblobknowledgesource) generates an indexer pipeline that pulls from a blob container. | Indexed |
+| [`"indexedOneLake"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#indexedonelakeknowledgesource) generates an indexer pipeline that pulls from a lakehouse. | Indexed |
+| [`"indexedSharePoint"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#indexedsharepointknowledgesource) generates an indexer pipeline that pulls from a SharePoint site. | Indexed |
+| [`"remoteSharePoint"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#remotesharepointknowledgesource) retrieves content directly from SharePoint. | Remote |
+|  [`"webParameters"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#webknowledgesource) retrieves real-time grounding data from Microsoft Bing. | Remote |
+
+Indexed knowledge sources point to target index on Azure AI Search and query execution is local to the search engine on your search service. Keyword (full text search), vector, and hybrid query capabilities are used for retrieving data from indexed knowledge sources.
+
+Remote knowledge sources are accessed at query time. The agentic retrieval engine calls the retrieval APIs that are native to the platform (Bing or SharePoint APIs).
+
+All retrieved content, whether indexed or remote, is pulled into the ranking pipeline in Azure AI Search where it's scored for relevance, merged (assuming multiple queries), reranked, and returned in the retrieval response. 
 
 ## Creating knowledge sources
 
+Knowledge sources are created as standalone objects and then specified in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) in a ["knowledgeSources" array](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#knowledgesourcereference).
+
 You must have [**Search Service Contributor** permissions](search-security-rbac.md) to create objects on a search service.  You also need **Search Index Data Contributor** permissions to load an index if you're using a knowledge source that creates an indexer pipeline. Alternatively, you can [use an API admin key](search-security-api-keys.md) instead of roles.
 
 You can use the REST API or an Azure SDK preview package to create a knowledge source. Azure portal support is available for select knowledge sources. The following links provide instructions for creating a knowledge source:
@@ -60,32 +70,25 @@ After the knowledge source is created, you can reference it in a knowledge base.
 
 ## Using knowledge sources
 
-Properties on the [*knowledge base*](agentic-retrieval-how-to-create-knowledge-base.md) determine which knowledge sources are used.
-
-+ ["knowledgeSources" REST](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#knowledgesourcereference) array specifies the knowledge sources available to the knowledge base.
-
-+ ["retrievalReasoningEffort" REST](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#knowledgeretrievalreasoningeffortkind) properties determine the amount of effort put into a retrieval. For more information, see [Set the retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md).
-
-+ ["outputMode" REST](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#knowledgeretrievaloutputmode) affects query output and what goes in the response.
+Knowledge source usage is either explicitly controlled, such as when you set `alwaysQuery` on the knowledge source definition, or subject to selection logic during query planning. Query planning occurs when you use a low or medium [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). For a minimal reasoning effort, all knowledge sources listed in the knowledge base are in scope for every query. For low and medium, the knowledge base and the LLM can determine at query time which knowledge sources are likely to provide the best search corpus. 
 
-The knowledge base uses the [retrieve action](agentic-retrieval-how-to-retrieve.md) to send queries to the index specified in the knowledge source. In the retrieve action, some knowledge base and source defaults can be overridden at retrieval time.
+Knowledge source selection logic is based on these factors:
 
-### Use multiple knowledge sources simultaneously
++ Is `alwaysQuery` set? If yes, the knowledge source is always used on every query.
 
-When you have multiple knowledge sources, set the following properties to bias query planning to a specific knowledge source.
++ The `name` of the knowledge source.
 
-+ Setting `alwaysQuerySource` forces query planning to always include the knowledge source.
-+ Setting `retrievalInstructions` provides guidance that includes or excludes a knowledge source. 
++ The `description` of an index, assuming an indexed knowledge source.
 
-Retrieval instructions are sent as a user-defined prompt to the large language model (LLM) used for query planning. This prompt is helpful when you have multiple knowledge sources and want to provide guidance on when to use each one. For example, if you have separate indexes for product information, job postings, and technical support, the retrieval instructions might say "use the jobs index only if the question is about a job application."
++ The `retrievalInstructions` specified in the [retrieve action](agentic-retrieval-how-to-retrieve.md) or in the [knowledge base definition](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) provides guidance that includes or excludes a knowledge source. It's similar to a prompt. You can specify brevity, tone, and formatting as a retrieval instruction.
 
-The `alwaysQuerySource` property overrides `retrievalInstructions`. Set `alwaysQuerySource` to false when providing retrieval instructions.
++ [`outputMode`](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#knowledgeretrievaloutputmode) on a knowledge base also affects query output and what goes in the response.
 
 ### Use a retrieval reasoning effort to control LLM usage
 
-Not all solutions benefit from LLM query planning and execution. If simplicity and speed outweigh the benefits the LLM query planning and context engineering provide, you can omit the LLM from your pipeline.
+Not all solutions benefit from LLM query planning and execution. If simplicity and speed outweigh the benefits the LLM query planning and context engineering provide, you can specify a minimal reasoning effort to prevent LLM processing in your pipeline.
 
-The retrieval reasoning effort determines the level of processing that goes into a retrieval action. For more information, see [Set the retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md).
+For low and medium, the level of LLM processing is either a balanced or maximal approach that improves relevance. For more information, see [Set the retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md).
 
 > [!NOTE]
 > If you used `attemptFastPath` in the previous preview, that approach is now replaced with `retrievalReasoningEffort` set to `minimal`.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースの概要の更新"
}
```

### Explanation
この変更は、「エージェント知識ソースの概要」記事に対するマイナーな更新を示しています。主な改訂点として、内容の明確化と最新の情報についての説明が加えられています。具体的には、知識ソースに関連する説明の整頓が行われ、文の流れが改善されました。また、新しい情報として、知識ソースの生成方法やそれらがどのように検索サービスに統合されるかについての詳細が追加されています。

加えて、知識ベースにおける知識ソースの使用方法の抜粋と、クエリ計画の際のロジックが明示化されています。例えば、`alwaysQuery`プロパティによって、どの知識ソースが常に使用されるべきかを設定する方法が示されています。このような明確さは、ユーザーにとっての理解を向上させ、エージェント検索機能を利用する際の利便性を高めるものです。

## articles/search/agentic-retrieval-how-to-migrate.md{#item-9653ea}

<details>
<summary>Diff</summary>
````diff
@@ -688,7 +688,7 @@ To review the [REST API reference documentation](/rest/api/searchservice/operati
 
 #### [**Nonbreaking changes**](#tab/nonbreaking-1)
 
-+ Adds knowledge sources for OneLake, SharePoint (local), SharePoint (remote) that retrieves content directly from Sharepoint, Web (Bing) that pulls from the Bing indexes.
++ Adds knowledge sources for OneLake, SharePoint (local), SharePoint (remote) that retrieves content directly from SharePoint, Web (Bing) that pulls from the Bing indexes.
 
 + All knowledge sources that pull from a search index have new ingestion options: `ingestionPermissionOptions` to support source-specific access models, `contentExtractionMode` that enables Azure Content Understanding in Foundry Tools integration, `aiServices` endpoint for Azure Content Understanding when `"contentExtractionMode": "minimal"`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索の移行手順の更新"
}
```

### Explanation
この変更は「エージェント検索の移行手順」記事に対するマイナーな更新を示しています。具体的には、知識ソースの追加に関する情報が明確化され、新たなオプションが紹介されています。

主なポイントとして、OneLake、ローカルおよびリモートのSharePointから直接コンテンツを取得するための知識ソースが追加されたことが強調されています。また、Bingインデックスからデータを引き出すためのWebに関する知識ソースも再確認されています。

さらに、検索インデックスから取得される全ての知識ソースには、新しい取り込みオプションが導入されています。具体的には、ソース固有のアクセスモデルをサポートするための`ingestionPermissionOptions`、Azure Content UnderstandingのFoundry Tools統合を可能にする`contentExtractionMode`、および`"contentExtractionMode": "minimal"`の場合にAzure Content Understandingに対応するエンドポイントである`aiServices`が含まれています。この更新は、ユーザーがこれらのオプションを理解し、活用できるようにすることを目的としています。

## articles/search/agentic-retrieval-how-to-retrieve.md{#item-d739cf}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 11/10/2025
+ms.date: 12/04/2025
 ---
 
 # Retrieve data using a knowledge base in Azure AI Search
@@ -24,6 +24,8 @@ This article explains how to set up a retrieve action. It also covers the three
 
 A retrieve request can include instructions for query processing that override the default instructions set on the knowledge base. A retrieve action has core parameters that are supported on any request, plus parameters that are specific to a knowledge source.
 
+You can also use optional [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md) to bring LLM answer formulation into the query pipeline, returning a concise or formatted answer to an agent or app.
+
 ## Prerequisites
 
 + A [supported knowledge source](agentic-knowledge-source-overview.md#supported-knowledge-sources) that wraps a searchable index or points to an external source for native data retrieval.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索でのデータ取得手順の更新"
}
```

### Explanation
この変更は、「エージェント検索でのデータ取得手順」記事に対するマイナーな更新を示しています。主な改訂点として、文書の最新日付が更新され、さらに新しい情報が追加されています。

特に、取得リクエストにおけるクエリ処理の指示に関する内容が強調されています。また、オプションとして[回答合成](agentic-retrieval-how-to-answer-synthesis.md)機能を使用することで、大規模言語モデル（LLM）による回答の生成をクエリパイプラインに組み込むことが可能であることが述べられています。これにより、エージェントやアプリに対して簡潔でフォーマットされた回答を返すことができるようになります。

さらに、検索可能なインデックスを包むか、ネイティブデータ取得のために外部ソースを指し示す[サポートされている知識ソース](agentic-knowledge-source-overview.md#supported-knowledge-sources)が必要であることも確認されています。この更新により、ユーザーがデータ取得時の新しい機能と前提条件を理解する助けとなります。

## articles/search/agentic-retrieval-how-to-set-retrieval-reasoning-effort.md{#item-141e97}

<details>
<summary>Diff</summary>
````diff
@@ -7,21 +7,22 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 11/07/2025
+ms.date: 12/04/2025
+ms.custom: references_regions
 ---
 
 # Set the retrieval reasoning effort
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-In agentic retrieval, you can specify the level of large language model (LLM) processing for query planning and answer formulation. Use the `retrievalReasoningEffort` property to determine LLM processing levels. You can set this property in a knowledge base or on a retrieve request.
+In agentic retrieval, you can specify the level of large language model (LLM) processing for query planning and answer formulation. Use the `retrievalReasoningEffort` property to set LLM processing levels that affect costs and latency. Extra LLM processing improves relevancy, but it also takes longer and uses billable LLM resources. You can set this property in a knowledge base or on a retrieve request.
 
 Levels of reasoning effort include:
 
 | Level | Effort |
 |-------|--------|
-| `minimal` | No LLM processing. |
-| `low` | Runs a single pass of LLM-based query planning and knowledge source selection. This is the default. |
+| `minimal` | No LLM processing. You provide the query.|
+| `low` | Runs a single pass of LLM-based query planning and knowledge source selection. This is the default. The LLM analyzes the query and breaks it into component parts as needed.|
 | `medium` | Adds deeper search and an enhanced retrieval stack to agentic retrieval to maximize completeness. |
 
 ## Prerequisites
@@ -70,9 +71,25 @@ To override the default on a query-by-query basis, set the property in the retri
 
 | Level | Description | Recommendation | Limits | 
 |-|-|-|-|
-| `minimal` | Disables LLM-based query planning to deliver the lowest cost and latency for agentic retrieval. It issues direct text and vector searches across the knowledge sources listed in the knowledge base, and returns the best-matching passages. Because all knowledge sources are always searched and no query expansion is performed, behavior is predictable and easy to control. It also means the `alwaysQueryKnowledgeSource` property on a retrieve request is ignored.  | Use "minimal" for migrations from the [Search API](/rest/api/searchservice/documents/search-post) or when you want to manage query planning yourself. | `outputMode` must be set to `extractiveData`. <br>[Answer synthesis](agentic-retrieval-how-to-answer-synthesis.md) and [web knowledge](agentic-knowledge-source-how-to-web.md) aren't supported. |
+| `minimal` | Disables LLM-based query planning to deliver the lowest cost and latency for agentic retrieval. It issues direct text and vector searches across the knowledge sources listed in the knowledge base, and returns the best-matching passages. Because all knowledge sources in the knowledge base are always searched and no query expansion is performed, behavior is predictable and easy to control. It also means the `alwaysQueryKnowledgeSource` property on a retrieve request is ignored.  | Use "minimal" for migrations from the [Search API](/rest/api/searchservice/documents/search-post) or when you want to manage query planning yourself. | `outputMode` must be set to `extractiveData`. <br>[Answer synthesis](agentic-retrieval-how-to-answer-synthesis.md) and [web knowledge](agentic-knowledge-source-how-to-web.md) aren't supported. |
 | `low` | The default mode of agentic retrieval, running a single pass of LLM-based query planning and knowledge source selection. The agentic retrieval engine generates subqueries and fans them out to the selected knowledge sources, then merges the results. You can enable answer synthesis to produce a grounded natural-language response with inline citations. | Use "low" when you want a balance between minimal latency and deeper processing. | 5,000 answer tokens. <br>Maximum three subqueries from a maximum of three knowledge sources. <br>Maximum of 50 documents for semantic ranking, and 10 documents if the semantic ranker uses L3 classification. |
-| `medium` | Adds deeper search and an enhanced retrieval stack to agentic retrieval to maximize completeness. After the first search is performed, a [high-precision semantic classifier](search-relevance-overview.md) evaluates the retrieved documents for an L3 ranking. If the quality of the retrieved results is insufficient to answer the query, a follow-up iteration is performed using a revised query plan. This revised query plan takes into account the already run queries and retrieved documents by adjusting queries, broadening terms, or adding sources such as the web. It also increases resource limits compared to low and minimal effort. | Use "medium" to maximize the utility of LLM-assisted knowledge retrieval. <br><br>Medium isn't available in all agentic retrieval regions.| 10,000 answer tokens. <br>Maximum of five subqueries from a maximum of five knowledge sources. <br>Maximum of 50 documents for semantic ranking, and 20 documents if the semantic ranker uses L3 classification.  |
+| `medium` | Adds deeper search and an enhanced retrieval stack to agentic retrieval to maximize completeness. After the first search is performed, a [high-precision semantic classifier](search-relevance-overview.md) evaluates the retrieved documents to determined whether further processing and L3 ranking is required. If the initial results from the first pass are insufficiently relevant to the query, a follow-up iteration is performed using a revised query plan. This revised query plan takes the previous results into account and iterates by fine-tuning queries, broadening terms, or adding other knowledge sources such as the web. It also increases resource limits compared to low and minimal effort. This reasoning level optimizes for relevance rather than exhaustive recall. | Use "medium" to maximize the utility of LLM-assisted knowledge retrieval. <br><br>Medium isn't available in all agentic retrieval regions. See the list in the next section for available regions. 10,000 answer tokens. <br>Maximum of five subqueries from a maximum of five knowledge sources. <br>Maximum of 50 documents for semantic ranking, and 20 documents if the semantic ranker uses L3 classification.  |
+
+### Medium retrieval and iterative search
+
+A medium retrieval reasoning effort provides iterative search if initial results aren't sufficiently relevant. An extra *semantic classifier model* is called to determine if a second iteration is necessary.
+
+The semantic classifier performs the following:
+
++ Recognizes when there's enough context to answer the question.
+
++ Retries on insufficient results, using existing information for context. New queries might drill down for more focused detail, or broaden the search. The activity log in the response shows the generated queries used for a more comprehensive answer.
+
++ Rescores using L3 classification. The range is identical to L2 ranking, an absolute range of zero through 4.0.
+
+There's only one retry. Each iteration adds latency and cost, so the system constrains retry to one pass. A second iteration adds input tokens to the query pipeline, which adds to the overall billable input token count.
+
+Iteration can reuse or choose different sources. The second pass selects the most promising knowledge resource to provide the missing information.
 
 ### Regions supporting medium retrieval reasoning effort
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "取得推論努力の設定手順の更新"
}
```

### Explanation
この変更は、「取得推論努力の設定手順」記事に対するマイナーな更新を示しています。主な改訂点は、文書の日付の更新と、取得推論努力に関する情報の強化です。

具体的には、`retrievalReasoningEffort`プロパティを使用して、大規模言語モデル（LLM）によるクエリ計画と回答生成の処理レベルを設定できることが説明されています。新たに、LLM処理がコストや待機時間にどのように影響するかが明示され、追加のLLM処理が関連性を向上させる一方で、処理時間と課金リソースを消費することが強調されています。

また、推論努力のレベルには`minimal`、`low`、及び`medium`が含まれ、それぞれの詳細情報と推奨事項がわかりやすく整理されています。特に、`medium`レベルでは初回検索が不十分な結果の場合にイテレーティブ検索を提供する手法が追加されており、これによりユーザーは必要に応じてクエリを再調整するプロセスが示されています。

さらに、`medium`取得推論努力をサポートしている地域に関する情報も追加されています。この更新により、ユーザーは新しい機能を理解し、効果的に利用できるようになります。

## articles/search/agentic-retrieval-overview.md{#item-d1f354}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about agentic retrieval concepts, architecture, and use cases
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 11/03/2025
+ms.date: 12/04/2025
 ms.service: azure-ai-search
 ms.topic: concept-article
 ms.custom:
@@ -207,6 +207,16 @@ To estimate agentic retrieval token counts, start with an idea of what an averag
 
 Putting it all together, you'd pay about $3.30 for agentic retrieval in Azure AI Search, 60 cents for input tokens in Azure OpenAI, and 42 cents for output tokens in Azure OpenAI, for $1.02 for query planning total. The combined cost for the full execution is $4.32.
 
+#### Tips for controlling costs
+
++ Review the activity log in the response to find out what queries were issued to which sources and the parameters used. You can reissue those queries against your indexes and use a public tokenizer to estimate tokens and compare to API-reported usage. Precise reconstruction of a query or response isn't guaranteed however. Factors include the type of knowledge source, such as public web data or a remote SharePoint knowledge source that's predicated on a user identity, which can affect query reproduction.
+
++ Reduce the number of knowledge sources (indexes); consolidating content can lower fan-out and token volume. 
+
++ Lower the reasoning effort to reduce LLM usage during query planning and query expansion (iterative search). 
+
++ Organize content so the most relevant information can be found with fewer sources and documents (For example, curated summaries or tables).
+
 <!-- 
 •Query Pipeline Recap: The query pipeline includes stages: Query Preprocessing (Query Rewriting, Vectorization, Text analysis), Ranking (Vector Search, Keyword Search, Fusion, Semantic Ranking), and Synthesis (Results for LLM, Extractive Answers, Contextualized Captions).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索の概要に関する更新"
}
```

### Explanation
この変更は、「エージェント検索の概要」記事に対するマイナーな更新を示しています。主な変更点は、文書の日付の更新と新たにコスト管理に関するヒントが追加されたことです。

具体的には、エージェント検索に関連するトークン数の見積もりに関する情報が記述されており、合計コスト計算の例が示されています。これにより、ユーザーはエージェント検索を利用する際の費用感をより具体的に理解できるようになります。

また、新たに追加されたセクションでは、コスト管理のためのヒントが挙げられています。これには、活動ログのレビューを通じて発行されたクエリの確認や、知識ソースの数を減らすこと、推論努力を低く設定すること、コンテンツを整理してより関連性の高い情報にアクセスしやすくすることが含まれます。これらの提案により、ユーザーはエージェント検索の利用時に発生するコストを効果的にコントロールできるようになります。

この更新により、ユーザーはエージェント検索の理解を深めつつ、コストを管理するための実用的なアドバイスを得ることができます。

## articles/search/cognitive-search-skill-annotation-language.md{#item-aaedc7}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Skill context and input annotation reference language
 titleSuffix: Azure AI Search
 description: Annotation syntax reference for annotation in the context, inputs, and outputs of a skillset in an AI enrichment pipeline in Azure AI Search.
 author: BertrandLeRoy
-ms.author: beleroy
+ms.author: haileytapia
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スキル注釈言語の著者情報の更新"
}
```

### Explanation
この変更は、「コグニティブサーチスキル注釈言語」記事に対するマイナーな更新を示しています。主な変更点は、著者情報の更新です。具体的には、著者名が「BertrandLeRoy」から「HaileyTapia」に変更されています。

この修正により、記事の著者情報が現在の執筆者を反映するように更新され、ユーザーは最新の情報をもってスキル注釈に関する知識を得ることができます。記事の内容自体には変更はないため、情報の正確性と信頼性が維持されています。このような小規模な更新は、文書管理において重要です。

## articles/search/search-how-to-index-cosmosdb-sql.md{#item-2e888b}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ To work through the examples in this article, you need the Azure portal or a [RE
 
 Use these instructions to create a container and database in Cosmos DB for testing purposes.
 
-1. [Download HotelsData_toCosmosDB.json](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotels/HotelsData_toCosmosDB.json) from GitHub to create a container in Cosmos DB that contains a subset of the sample hotels data set.
+1. [Download HotelsData_toCosmosDB.json](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotels/HotelsData_toCosmosDB.JSON) from GitHub to create a container in Cosmos DB that contains a subset of the sample hotels data set.
 
 1. Sign in to the Azure portal and [create an account, database, and container](/azure/cosmos-db/nosql/quickstart-portal) on Cosmos DB. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cosmos DB サンプルデータのファイル名の修正"
}
```

### Explanation
この変更は、「Cosmos DBのSQLをインデックス化する方法」に関する記事に対するマイナーな更新を示しています。主な変更点は、ダウンロードリンクのファイル名の拡張子が小文字から大文字に変更されたことです。

具体的には、元の文では「HotelsData_toCosmosDB.json」と記載されていたファイル名が、「HotelsData_toCosmosDB.JSON」に修正されました。この変更は、ファイル名の正確性を保つために行われた可能性があり、ユーザーが正しいファイルをダウンロードするためには重要です。

このような小規模な修正は、情報の正確性を確保し、特にリンクされたリソースへのアクセスを容易にするために必要です。全体として、記事の内容や手順には大きな変更はなく、ユーザーが必要とする情報は引き続き利用可能です。

## articles/search/search-manage-rest.md{#item-405ec7}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 09/25/2025
+ms.date: 12/04/2025
 ms.update-cycle: 365-days
 ---
 
@@ -36,6 +36,9 @@ The Management REST API is available in stable and preview versions. Be sure to
 
 All of the Management REST APIs have examples. If a task isn't covered in this article, see the [API reference](/rest/api/searchmanagement/) instead.
 
+> [!TIP]
+> If you use CURL to call the Management REST API, make sure you set a content type header to application/json: `-H "Content-Type: application/json"`. Alternatively, you can use the `--JSON` flag if you want to embed the JSON.
+
 ## Prerequisites
 
 * An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "管理REST APIに関するチップの追加と日付の更新"
}
```

### Explanation
この変更は、「RESTを使用した検索管理」に関する記事に対するマイナーな更新を示しています。主な変更点は、日付の更新と新しい情報の追加です。

具体的には、記事のメタデータとして記載されていた日付が「2025年9月25日」から「2025年12月4日」に更新されました。また、記事の内容に新しいヒントが追加されました。このヒントでは、CURLを使用して管理REST APIを呼び出す際に、`Content-Type` ヘッダーを `application/json` に設定する必要があることが強調されています。この情報は、ユーザーがREST APIを正しく利用するために必要です。

これらの更新により、記事は最新の情報を提供し、特にAPIを利用する際の実用的なアドバイスを追加することで、ユーザーの利便性を向上させています。全体として、内容の正確性と有用性を高めるための重要な修正です。

## articles/search/search-relevance-overview.md{#item-cb0e09}

<details>
<summary>Diff</summary>
````diff
@@ -7,15 +7,15 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 11/10/2025
+ms.date: 12/04/2025
 ms.update-cycle: 180-days
 ---
 
 # Relevance in Azure AI Search
 
-In a query operation, the relevance of any given result is determined by a ranking algorithm that evaluates the strength of a match based on how closely the query corresponds to an indexed document. When a match is found, an algorithm assigns a score, and results are ranked by that score and the topmost results are returned in the response. 
+In a query operation, the relevance of any given result is determined by a ranking algorithm that evaluates the strength of a match based on how closely the query corresponds to content in the search corpus. When a match is found, an algorithm assigns a score, and results are ranked by that score and the topmost results are returned in the response. 
 
-Ranking occurs whenever the query request includes full text or vector queries. It doesn't occur if the query invokes strict pattern matching, such as a filter-only query or a specialized query form like autocomplete, suggestions, geospatial search, fuzzy search, or regular expression search. A uniform search score of 1.0 indicates the absence of a ranking algorithm.
+Ranking occurs whenever the query request is for agentic retrieval and classic search for keyword, vector, and hybrid queries. It doesn't occur if the query invokes strict pattern matching, such as a filter-only query or a specialized query form like autocomplete, suggestions, geospatial search, fuzzy search, or regular expression search. A uniform search score of 1.0 indicates the absence of a ranking algorithm.
 
 ## Levels of ranking
 
@@ -28,6 +28,7 @@ This section describes the levels of scoring operations. For an illustration of
 | Level&nbsp;1&nbsp;(L1) | Initial search score (`@search.score`). <br>For text queries matching on tokenized strings, results are always initially ranked using the [BM25 ranking algorithm](index-similarity-and-scoring.md). <br>For vector queries, results are ranked using either [Hierarchical Navigable Small World (HNSW) or exhaustive K-nearest neighbor (KNN)](vector-search-ranking.md). Image search or multimodal searches are based on vector queries and scored using the L1 vector ranking algorithms. |
 | Fused&nbsp;L1 | Scoring from multiple queries using the [Reciprocal Ranking Fusion (RRF) algorithm](hybrid-search-ranking.md). RRF is used for hybrid queries that include text and vector components. RRF is also used when multiple vector queries execute in parallel. A search score from RRF is reflected in `@search.score` [over a different range](#types-of-search-scores).|
 | Level&nbsp;2&nbsp;(L2) | [Semantic ranking score (`@search.reRankerScore`)](semantic-search-overview.md) applies machine reading comprehension to the textual content retrieved by L1 ranking, rescoring the L1 results to better match the semantic intent of the query. L2 reranks L1 results because doing so saves time and money; it would be prohibitive to use semantic ranking as an L1 ranking system. Semantic ranking is a premium feature that bills for usage of the semantic ranking models. It's optional for text queries and vector queries that contain text, but required for [agentic retrieval (preview)](agentic-retrieval-overview.md). Although agentic retrieval sends multiple queries to the query engine, the ranking algorithm for agentic retrieval is the semantic ranker. |
+| Level&nbsp;3&nbsp;(L3) | Applies to [agentic retrieval (preview)](agentic-retrieval-overview.md) and a `medium` retrieval reasoning effort. L3 ranking refers to *iterative search* and it's invoked when the agentic retrieval engine and LLM agree that a second query pass is needed to return a more relevant result. For more information, see [Medium retrieval and iterative search](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md#medium-retrieval-and-iterative-search). |
 
 ## Relevance tuning
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索の関連性に関する概念記事の更新"
}
```

### Explanation
この変更は、「Azure AI Searchにおける関連性の概要」に関する記事に対するマイナーな更新を示しています。主な変更点は、日付の更新といくつかの文言の修正です。

まず、記事内のメタ情報として「2025年11月10日」が「2025年12月4日」に更新されました。これはドキュメントのリリース日や最新性を反映しています。

次に、内容の修正がありました。特に、クエリ操作における関連性の測定についての説明が改訂され、「インデックス化された文書」に対して「検索コーパス内のコンテンツ」と表現が変わりました。この表現の変更は、関連性がどのように評価されるかをより明確に示しています。

さらに、ランキングの条件に関する説明も修正され、エージェント取得（agentic retrieval）やクラシック検索におけるクエリが具体的に示されました。この変更により、ユーザーは異なるクエリタイプがどのように関連性に影響を与えるかについて、より良い理解が得られます。

最後に、順位付けのレベルについて新たに「レベル3 (L3)」が追加され、エージェント取得における反復検索の概念が導入されました。これにより、ユーザーはエージェント取得プロセスがどのように進行するかについて、より深い情報を得ることができます。

全体として、これらの変更は、関連性に関する情報をより正確で詳細にし、ユーザーにとって有益なガイダンスを提供することを目的としています。

## articles/search/search-what-is-azure-search.md{#item-93853a}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Introduction to Azure AI Search
 titleSuffix: Azure AI Search
-description: Azure AI Search is an AI-powered information retrieval platform, helps developers build rich search experiences and generative AI apps that combine large language models with enterprise data.
+description: Azure AI Search is an AI-powered information retrieval platform that helps developers build rich search experiences and generative AI apps that combine large language models (LLMs) with enterprise or web data.
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
@@ -10,14 +10,26 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: overview
-ms.date: 07/18/2025
+ms.date: 12/04/2025
 ---
 
-# What's Azure AI Search?
+# What is Azure AI Search?
 
-Azure AI Search is a scalable search infrastructure that indexes heterogeneous content and enables retrieval through APIs, applications, and AI agents. The platform provides native integrations with Azure's AI stack (OpenAI, Microsoft Foundry, Machine Learning) and supports extensible architectures for third-party and open-source model integration.
+Azure AI Search is a fully managed, cloud-hosted service that connects your data to AI. The service unifies access to enterprise and web content so agents and LLMs can use context, chat history, and multi-source signals to produce reliable, grounded answers.
 
-The service handles both traditional search workloads and modern RAG (retrieval-augmented generation) patterns for conversational AI applications. This makes it suitable for enterprise search scenarios as well as AI-powered customer experiences that require dynamic content generation through chat completion models.
+Common use cases include *classic search* and modern retrieval-augmented generation (RAG) via *agentic retrieval*. This makes Azure AI Search suitable for both enterprise and consumer scenarios, whether you're adding search functionality to a website, app, agent, or chatbot.
+
+When you create a search service, you unlock the following capabilities:
+
++ Two engines: [classic search](#what-is-classic-search) for single requests and [agentic retrieval](#what-is-agentic-retrieval) for parallel, iterative, LLM-assisted search.
++ [Full-text](search-lucene-query-architecture.md), [vector](vector-search-overview.md), [hybrid](hybrid-search-overview.md), and [multimodal](multimodal-search-overview.md) queries over local (indexed) and remote content.
++ AI enrichment to chunk, vectorize, and otherwise make raw content searchable.
++ Relevance tuning to improve intent matching and result quality.
++ Azure scale, security, monitoring, and compliance.
++ Azure integrations with supported data platforms, Azure OpenAI, and Microsoft Foundry.
+
+> [!div class="nextstepaction"]
+> [Create a search service](search-create-service-portal.md)
 
 <!-- Azure AI Search ([formerly known as "Azure Cognitive Search"](whats-new.md#new-service-name)) is an enterprise-ready information retrieval system for your heterogeneous content that you ingest into a search index, and surface to users through queries and apps. It comes with a comprehensive set of advanced search technologies, built for high-performance applications at any scale.
 
@@ -31,79 +43,110 @@ Indexing and query workloads support native integration with AI models from Azur
 
 You can use Azure AI Search for regular search needs (like searching through catalogs or documents) or for AI-powered search that can have conversations with users and generate answers based on your content. -->
 
-When you create a search service, you work with the following capabilities:
+## Why use Azure AI Search?
 
-+ A search engine for [agentic search](agentic-retrieval-overview.md), [vector search](vector-search-overview.md), [full text](search-lucene-query-architecture.md), [multimodal search](multimodal-search-overview.md), or [hybrid search](hybrid-search-overview.md).
-+ Content processing during indexing that can add structure and transformations.
-+ Extensive query syntax for agents, vectors, text, hybrid, and multimodal queries.
-+ Smart results through semantic ranking, scoring profiles, and parameterized queries.
-+ Azure scale, security, and reach.
-+ Azure integration at the data layer, machine learning layer, Foundry Tools, and Azure OpenAI.
++ Ground agents and chatbots in proprietary, enterprise, or web data for accurate, context-aware responses.
 
-> [!div class="nextstepaction"]
-> [Create a search service](search-create-service-portal.md)
++ Access data from Azure Blob Storage, Azure Cosmos DB, Microsoft SharePoint, Microsoft OneLake, and other supported data sources. Choose indexed or remote access based on your freshness, latency, and compliance needs.
+
++ Enrich and structure content at indexing or query time with skills that perform chunking, embedding, and LLM-assisted transformations.
 
-Architecturally, a search service sits between the external data stores that contain your un-indexed data, and your client app that sends query requests to a search index and handles the response.
++ Combine full-text search with vector search (hybrid search) to balance precision and recall.
 
-![Azure AI Search architecture](media/search-what-is-azure-search/azure-search.svg "Azure AI Search architecture")
++ Query content containing both text and images in a single multimodal pipeline.
 
-On the indexing side, if your content is on Azure, you can use indexers and skillsets for automated and AI-enriched indexing. Or, create a logic app workflow for equivalent automation over an even broader set of supported data sources. 
++ Easily implement search-related features: relevance tuning, faceted navigation, filters (including geo-spatial search), synonym mapping, and autocomplete.
 
-On the retrieval side, your app can be an agent or tool, a bot, or any client that sends requests to a search index or knowledge base.
++ Provide enterprise security, access control, and compliance through Microsoft Entra, Azure Private Link, document-level access control, and role-based access.
 
-Within Azure AI Search, the indexing and query engine is the same component operating in read-write and read-only modes, but we split it up in this diagram to indicate the type of work being performed.
++ Scale and operate in production with Azure reliability, monitoring and diagnostics (logs, metrics, and alerts), and REST API or SDK tooling for automation.
 
-## Inside a search service
+For more information about specific functionality, see [Features of Azure AI Search](search-features-list.md).
 
-On the search service itself, the two primary workloads are *indexing* and *querying*. 
+## What is classic search?
 
-+ [**Indexing**](search-what-is-an-index.md) is an intake process that loads content into your search service and makes it searchable. Internally, inbound text is processed into tokens and stored in inverted indexes, and inbound vectors are stored in vector indexes. The document format that Azure AI Search can index is JSON. You can upload JSON documents, or use an indexer or a logic app workflow to retrieve and serialize your data into JSON. 
+Classic search is an index-first retrieval model for predictable, low-latency queries. Each query targets a single, predefined search index and returns ranked documents in one request–response cycle. No LLM-assisted planning, iteration, or synthesis occurs during retrieval.
 
-  [AI enrichment](cognitive-search-concept-intro.md) is through a [skillset](cognitive-search-working-with-skillsets.md) that extends indexing with image and language models. If you have images or large unstructured text in source document, you can attach skills that chunk and vectorize content. If you have image content, you can use LLMs to summarize content, generate descriptions, or perform OCR and image analysis. Skills can also infer structure, translate text, and more. Output is text or vectors that can be serialized into JSON and ingested into a search index.
+In this architecture, your search service sits between the data stores that contain your unprocessed content and your client app. The app is responsible for sending query requests to your search service and handling the response.
 
-+ [**Querying**](search-query-overview.md) can happen once an index is populated with searchable content, when your client app sends query requests to a search service and handles responses. All query execution is over a search index that you control. In your code, set up a search client to handle query requests for [agentic queries](agentic-retrieval-how-to-retrieve.md), [vector queries](vector-search-how-to-query.md), [text search](search-query-create.md), [hybrid queries](hybrid-search-how-to-query.md), fuzzy search, autocomplete, geo-search, and others.
+This architecture has two primary workloads:
 
-## Why use Azure AI Search?
+#### [Indexing](#tab/indexing)
 
-Azure AI Search offloads indexing and query workloads onto a dedicated search service. It's well suited for the following application scenarios:
+[Indexing](search-what-is-an-index.md) loads content into an index and makes it searchable. Internally, inbound text is tokenized and stored in inverted indexes, while inbound vectors are stored in vector indexes. Azure AI Search can only index JSON documents. You can use the [push method](search-what-is-data-import.md#pushing-data-to-an-index) to upload JSON documents directly or the [pull method](search-what-is-data-import.md#pulling-data-into-an-index) (indexer or logic app workflow) to retrieve and serialize data into JSON.
 
-+ Use it for empowering agents and bots with grounding data based on your content.
+During indexing, you can use [AI enrichment](cognitive-search-concept-intro.md) to chunk text, generate vectors, and apply other transformations that create structure and content. Azure AI Search then serializes the enriched output into JSON documents and ingests them into the index.
 
-+ Use it for traditional full text search and next-generation vector similarity search. Back your generative AI apps with information retrieval that leverages the strengths of both keyword and similarity search. Use both modalities to retrieve the most relevant results.
+#### [Querying](#tab/querying)
 
-+ Consolidate heterogeneous content into a user-defined and populated search index composed of vectors and text. You maintain ownership and control over what's searchable.
+[Querying](search-query-overview.md) targets an index populated with searchable content. This step occurs when your client app sends a query request to your search service. In your code, set up a search client to handle requests for [full-text queries](search-query-create.md), [vector queries](vector-search-how-to-query.md), [hybrid queries](hybrid-search-how-to-query.md), [multimodal queries](multimodal-search-overview.md), fuzzy search, autocomplete, geo-search, and other query types.
 
-+ Transform large undifferentiated text or image files, or application files stored in Azure Blob Storage or Azure Cosmos DB, into searchable chunks. This is achieved during indexing through [AI skills](cognitive-search-concept-intro.md) that add external processing from Azure AI.
+---
 
-+ [Integrate data chunking and vectorization](vector-search-integrated-vectorization.md) for generative AI and RAG apps.
+:::image type="content" source="media/search-what-is-azure-search/azure-search.svg" alt-text="Diagram of the Azure AI Search architecture for classic search." lightbox="media/search-what-is-azure-search/azure-search.svg" :::
 
-+ Add linguistic or custom text analysis for keyword search. If you have non-English content, Azure AI Search supports both Lucene analyzers and Microsoft's natural language processors. You can also configure analyzers to achieve specialized processing of raw content, such as filtering out diacritics, or recognizing and preserving patterns in strings.
+> [!NOTE]
+> This diagram separates the indexing and query engines for clarity, but in Azure AI Search, they're the same component operating in read-write and read-only modes.
 
-+ Easily implement search-related features: relevance tuning, faceted navigation, filters (including geo-spatial search), synonym mapping, and autocomplete.
+## What is agentic retrieval?
+
+[Agentic retrieval](agentic-retrieval-overview.md) is a multi-query pipeline designed for complex agent-to-agent workflows. Each query targets a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) that represents a complete domain of knowledge. Your agent references the knowledge base for *what* to ground on, while the knowledge base handles *how* to perform grounding.
+
+One knowledge base consists of one or more [knowledge sources](agentic-knowledge-source-overview.md), an optional LLM for query planning and answer synthesis, and parameters that govern retrieval behavior. Each query undergoes planning, decomposition into focused subqueries, parallel retrieval from knowledge sources, semantic reranking, and results merging. The three-pronged response is optimized for agent consumption.
+
+Under the hood, agentic retrieval builds on the classic search architecture by adding a context layer (knowledge base) that orchestrates multi-source retrieval. Knowledge sources can be indexed or remote: indexed sources use the same indexing and query engines as classic search, while remote sources bypass indexing and are queried live.
+
+<!--
+:::image type="content" source="media/search-what-is-azure-search/azure-search-agentic-retrieval.svg" alt-text="Diagram of the Azure AI Search architecture for agentic retrieval." lightbox="media/search-what-is-azure-search/azure-search-agentic-retrieval.svg" :::
+-->
+
+## How they compare
 
-+ [Apply granular access control](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/access-control-in-generative-ai-applications-with-azure/ba-p/3956408) at the document level.
+Classic search and agentic retrieval are complementary modes of information retrieval. Both support [full-text](search-lucene-query-architecture.md), [vector](vector-search-overview.md), [hybrid](hybrid-search-overview.md), and [multimodal](multimodal-search-overview.md) search. However, they differ in how content is ingested and queried. The following table summarizes their key differences.
 
-For more information about specific functionality, see [Features of Azure AI Search](search-features-list.md)
+| Aspect | Classic search | Agentic retrieval |
+|---|---|---|
+| Search corpus | [Search index](search-what-is-an-index.md) | [Knowledge source](agentic-knowledge-source-overview.md) |
+| Search target | One index defined by a schema | A knowledge base pointing to one or more knowledge sources |
+| Query plan | No plan, just a request | LLM-assisted or user-provided plan |
+| Query request | Search documents in an index | Retrieve from knowledge sources |
+| Response | Flattened search results based on schema | LLM-formulated answer or raw source data, activity log, references |
+| Region restrictions | No | Yes |
+| Status | Generally available | Public preview|
 
 ## How to get started
 
-Functionality is exposed through the Azure portal, simple [REST APIs](/rest/api/searchservice/), or Azure SDKs like the [Azure SDK for .NET](search-howto-dotnet-sdk.md). The Azure portal supports service administration and content management, with tools for prototyping and querying your indexes and skillsets. 
+You can access Azure AI Search through the Azure portal, [REST APIs](search-api-versions.md#rest-apis), and Azure SDKs for [.NET](search-api-versions.md#azure-sdk-for-net), [Java](search-api-versions.md#azure-sdk-for-java), [JavaScript](search-api-versions.md#azure-sdk-for-javascript), and [Python](search-api-versions.md#azure-sdk-for-python).
 
-### Use the Azure portal
+The portal is useful for service administration and content management, with tools for prototyping your knowledge bases, knowledge sources, indexes, indexers, skillsets, and data sources. REST APIs and SDKs are useful for production automation.
 
-An end-to-end exploration of core search features can be accomplished in four steps:
+### Choose your path
 
-1. [**Decide on a tier**](search-sku-tier.md) and region. One free search service is allowed per subscription. Most quickstarts can be completed on the free tier. For more capacity and capabilities, you need a [billable tier](https://azure.microsoft.com/pricing/details/search/).
+Before you get started, use this checklist to make key decisions:
 
-1. [**Create a search service**](search-create-service-portal.md) in the Azure portal.
++ **Choose a search engine:** If you're not using an agent or chatbot, classic search can meet most app needs, with lower costs and complexity than LLM integration. If you want the benefits of a knowledge base and multiple knowledge sources without full LLM orchestration, consider agentic retrieval with the minimal [reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md).
+
++ **Choose a region:** If you're using agentic retrieval, choose a [supported region](search-region-support.md). For classic search, choose a region that offers the features and capacity you need.
+
++ **Choose an ingestion method for index-bound content:** If your content is in a [supported data source](search-indexer-overview.md#supported-data-sources), use the [pull method](search-what-is-data-import.md#pulling-data-into-an-index) to retrieve and serialize data into JSON. If you don't have a supported data source, or if your content and index must be synchronized in real time, the [push method](search-what-is-data-import.md#pushing-data-to-an-index) is your only option.
+
++ **Do you need vectors?** LLMs and agents don't require vectors. Only use them if you need similarity search or if you have content that can be homogenized into vectors. Azure AI Search offers [integrated vectorization](vector-search-integrated-vectorization.md) for this task.
+
++ **Do you need user-based permission inheritance?** Remote SharePoint is designed for this scenario, but you can also inherit user permissions attached to content in Azure Blob Storage or ADLS Gen2. For all other scenarios, you can use the [security filter](search-security-trimming-for-azure-search.md) workaround.
 
-1. [**Start with Import data wizard**](search-get-started-portal.md). Choose a built-in sample or a supported data source to create, load, and query an index in minutes. 
+### Choose your learning resources
 
-1. [**Finish with Search Explorer**](search-explorer.md), using a portal client to query the search index you just created.
+### [Quickstarts](#tab/quickstarts)
 
-### Check out samples
+We maintain quickstarts that span various end-to-end search scenarios:
 
-We maintain an inventory of samples that use the REST APIs and the Azure SDK programming languages supported by Azure AI Search:
++ Quickstart: Agentic retrieval ([portal](get-started-portal-agentic-retrieval.md) or [programmatic](search-get-started-agentic-retrieval.md))
++ Quickstart: Full-text search ([portal](search-get-started-portal.md) or [programmatic](search-get-started-text.md))
++ Quickstart: Vector search ([portal](search-get-started-portal-import-vectors.md) or [programmatic](search-get-started-vector.md))
+
+### [Samples](#tab/samples)
+
+We maintain samples that use REST APIs and supported SDK programming languages:
 
 + [REST samples](/azure/search/samples-rest)
 + [Python samples](/azure/search/samples-python)
@@ -112,36 +155,41 @@ We maintain an inventory of samples that use the REST APIs and the Azure SDK pro
 + [JavaScript/TypeScript samples](/azure/search/samples-javascript)
 + [Vector samples](https://github.com/Azure/azure-search-vector-samples)
 
-### Use APIs
+---
 
-Alternatively, you can create, load, and query a search index in atomic steps:
+> [!TIP]
+> For help with complex or custom solutions, [contact a partner](https://partner.microsoft.com/partnership/find-a-partner) with deep expertise in Azure AI Search.
 
-1. [**Create a search index**](search-what-is-an-index.md) using the Azure portal, [REST API](/rest/api/searchservice/indexes/create), [.NET SDK](search-howto-dotnet-sdk.md), or another SDK. The index schema defines the structure of searchable content.
+<!--
+### [**Azure portal**](#tab/portal)
 
-1. [**Upload content**](search-what-is-data-import.md) using the ["push" model](tutorial-optimize-indexing-push-api.md) to push JSON documents from any source, or use the ["pull" model (indexers)](search-indexer-overview.md) if your source data is of a [supported type](search-indexer-overview.md#supported-data-sources).
+For end-to-end exploration of core features:
 
-1. [**Query an index**](search-query-overview.md) using [Search explorer](search-explorer.md) in the Azure portal, [REST API](search-get-started-text.md), [.NET SDK](/dotnet/api/azure.search.documents.searchclient.search), or another SDK.
+1. [**Choose a pricing tier**](search-sku-tier.md) and region. One free search service is allowed per subscription, and most quickstarts support the free tier. For more capacity and capabilities, you need a [billable tier](https://azure.microsoft.com/pricing/details/search/).
+
+1. [**Create a search service**](search-create-service-portal.md) in the Azure portal.
 
-### Use accelerators
+1. [**Start with the Import data wizard**](search-get-started-portal.md). Choose a built-in sample or a supported data source to create, load, and query an index in minutes.
 
-Or, try solution accelerators:
+1. [**Finish with Search Explorer**](search-explorer.md). Use a portal client to query the search index you just created.
 
-+ [**Chat with your data solution accelerator**](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator) helps you create a custom RAG solution over your content.
+### [**REST APIs and SDKs**](#tab/rest-apis-sdks)
 
-+ [**Conversational Knowledge Mining solution accelerator**](https://github.com/microsoft/Customer-Service-Conversational-Insights-with-Azure-OpenAI-Services) helps you create an interactive solution to extract actionable insights from post-contact center transcripts.
+To create, load, and query a search index programmatically:
 
-+ [**Document Knowledge Mining accelerator**](https://github.com/microsoft/Document-Knowledge-Mining-Solution-Accelerator) helps you process and extract summaries, entities, and metadata from unstructured, multimodal documents.
+1. [**Create a search index**](search-what-is-an-index.md) using the Azure portal, [REST API](/rest/api/searchservice/indexes/create), [.NET SDK](search-howto-dotnet-sdk.md), or another SDK. The index schema defines the structure of searchable content.
+
+1. [**Upload content**](search-what-is-data-import.md) using the [push model](tutorial-optimize-indexing-push-api.md) to push JSON documents from any source or the [pull model (indexers)](search-indexer-overview.md) if your source data is a [supported type](search-indexer-overview.md#supported-data-sources).
 
-+ [**Build your own copilot solution accelerator**](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator), leverages Azure OpenAI, Azure AI Search and Microsoft Fabric, to create custom copilot solutions.
+1. [**Query an index**](search-query-overview.md) using [Search explorer](search-explorer.md) in the Azure portal, [REST API](search-get-started-text.md), [.NET SDK](/dotnet/api/azure.search.documents.searchclient.search), or another SDK.
+-->
 
 <!--   + [Generic copilot](https://github.com/microsoft/Generic-Build-your-own-copilot-Solution-Accelerator) helps you build your own copilot to identify relevant documents, summarize unstructured information, and generate Word document templates using your own data.
 
   + [Client Advisor](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator) all-in-one custom copilot empowers Client Advisor to harness the power of generative AI across both structured and unstructured data. Help our customers to optimize daily tasks and foster better interactions with more clients
 
   + [Research Assistant](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator) helps build your own AI Assistant to identify relevant documents, summarize and categorize vast amounts of unstructured information, and accelerate the overall document review and content generation.
  -->
-> [!TIP]
-> For help with complex or custom solutions, [**contact a partner**](https://partner.microsoft.com/partnership/find-a-partner) with deep expertise in Azure AI Search technology.
 
 <!-- ## Compare search options
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azure AI Searchに関する記事の大幅な改訂"
}
```

### Explanation
この変更は、「Azure Searchとは何か？」に関する記事に対する大幅な改訂を示しています。内容は大幅に追加・削除され、構成も見直されています。

主な変更点には、次のような内容が含まれます。まず、説明文の変更により、Azure AI Searchの機能が「AI搭載の情報取得プラットフォーム」という定義から、「完全に管理されたクラウドホストサービス」として具体化されました。この改訂により、システムの目的と利点が明確に示されています。

また、以前の記事で言及されていた「スケーラブルな検索インフラストラクチャ」についての記述が削除され、代わりに「エンタープライズとウェブデータへの統一アクセス」という新しいフレーズが登場しました。これにより、Azure AI Searchが企業利用のケースにも対応できることが強調され、特にエージェントや大規模言語モデル（LLM）と連携する能力が強調されています。

さらに、一般的な利用ケースとして「クラシック検索」や「エージェント検索」が具体的に示され、Azure AI Searchの柔軟性が強調されました。新たに「エージェント取得」や「AI充実」などの機能が詳述され、検索サービスが提供する多くの新機能が紹介されています。

この記事は、インデックス作成やクエリ処理のメカニズムを詳述し、AzureポータルやREST API、SDKを通じた具体的な利用方法も示しています。このようにして、Azure AI Searchを使用するためのフレームワークが構築されています。

全体として、この変更は既存の記事を刷新し、Azure AI Searchの最新の機能と利点をわかりやすく説明することを目的とした重要な変更です。

## articles/search/tutorial-adls-gen2-indexer-acls.md{#item-6881a0}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.update-cycle: 180-days
 ms.topic: tutorial  
 ms.date: 08/27/2025
 author: wlifuture
-ms.author: wli
+ms.author: haileytapia
 ---  
 
 # Tutorial: Index permission metadata from ADLS Gen2 and query with permission-filtered results
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ADLS Gen2インデクサーの著者情報の更新"
}
```

### Explanation
この変更は、「ADLS Gen2からのインデックス権限メタデータの取得と権限フィルター結果に基づくクエリ」に関するチュートリアルの記事に対するマイナーな更新を示しています。具体的には、メタデータの著者情報が更新されています。

元の著者情報である「wli」が「haileytapia」に変更されました。この更新は、文書の作成者情報を最新の状態に保つためのものです。その他のコンテンツや構成には変更がなく、メタデータの一部としての著者情報だけが更新されています。

このような著者情報の更新は、ドキュメントの透明性を高め、読者がコンテンツの信頼性を判断するための重要な要素となります。全体として、この更新は小さな変更ですが、ドキュメントの正確さと最新性を維持するために必要です。


