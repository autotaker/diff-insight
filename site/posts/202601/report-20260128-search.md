---
date: '2026-01-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9f4eb38...MicrosoftDocs:83988f2
summary: このドキュメント更新は、Azure AI Searchに関する機能とその設定方法の説明を改善することを目的としています。特に文書の整合性と明確さが向上されており、既存の情報が体系的に構成され、ユーザーが情報にアクセスしやすくなっています。破壊的な変更はなく、用語の一貫性、出版日と著者情報のアップデート、さらには新規セクションやJSONサンプルコードの提供などが行われました。これにより、ユーザーは技術的な設定をより正確に行い、Azure
  AI Searchを効率的に活用できるようになります。全体として、ドキュメントの信頼性と専門性が向上しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9f4eb38...MicrosoftDocs:83988f2){target="_blank"}

# Highlights
このドキュメント更新は、Azure AI Searchに関連するさまざまな機能とその設定方法に関する説明を改善することを目的としています。特に、文書の整合性と明確さを高めるためのマイナーな修正が行われました。

## 新機能
- 特に新しい機能が追加されたわけではありませんが、既存の情報が体系的に構成されることで、ユーザーが情報にアクセスしやすくなっています。

## 破壊的変更
- 特に破壊的な変更は含まれていません。

## その他の更新
- 用語の一貫性と明確さの向上
- 出版日と著者情報のアップデート
- 新規セクションと内容の追加（例：「Reasoning effort levels」）
- JSONサンプルコードの提供
- 各ティアにおける制限に関する詳細情報の追加

# Insights
これらのドキュメントの更新は、Azure AI Searchの機能および設定方法をユーザーにとってより理解しやすくするためのものです。特に、エージェントリック検索における回答合成や推論努力の設定に関する説明が見直され、より詳細な情報が追加されている点が重要です。このような改善により、ユーザーは技術的な設定を正確に実施する能力が高まり、Azure AI Searchをより効率的に活用できるようになります。

また、これらの更新は新しい情報だけでなく、用語の一貫性を確保することで、ドキュメント全体の信頼性と専門性を向上させています。特に、設定に関連する具体的な手順や制限に関する詳細が追加されたことで、Azure AI Searchの幅広い利用シナリオについて十分なガイダンスが得られるようになっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-answer-synthesis.md](#item-f44e99) | minor update | エージェントリック検索の回答合成を有効にする方法に関するドキュメントの修正 | modified | 8 | 8 | 16 | 
| [agentic-retrieval-how-to-set-retrieval-reasoning-effort.md](#item-141e97) | minor update | エージェントリック検索の推論努力設定に関するドキュメントの修正 | modified | 50 | 42 | 92 | 
| [agentic-retrieval-overview.md](#item-d1f354) | minor update | エージェントリック検索の概要に関するドキュメントの修正 | modified | 1 | 1 | 2 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索制限、クォータ、容量に関するドキュメントの更新 | modified | 11 | 6 | 17 | 
| [search-relevance-overview.md](#item-cb0e09) | minor update | 検索の関連性に関するドキュメントの修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-answer-synthesis.md{#item-f44e99}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Enable Answer Synthesis
 titleSuffix: Azure AI Search
-description: Learn how to enable answer synthesis on a knowledge base or retrieval request in Azure AI Search. At query time, the knowledge base uses your deployed LLM to produce natural-language answers with citations to your knowledge sources.
+description: Learn how to enable answer synthesis in a knowledge base or retrieve request in Azure AI Search. At query time, the knowledge base uses your deployed LLM to produce natural-language answers with citations to your knowledge sources.
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
@@ -34,11 +34,11 @@ You can enable answer synthesis in two ways:
 
 + [Visual Studio Code](https://code.visualstudio.com/) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) or a preview Azure SDK package that provides the knowledge base REST APIs.
 
-## Enable answer synthesis on a knowledge base
+## Enable answer synthesis in a knowledge base
 
-This section explains how to enable answer synthesis on an existing knowledge base. Although you can use this configuration for new knowledge bases, knowledge base creation is beyond the scope of this article.
+This section explains how to enable answer synthesis in an existing knowledge base. Although you can use this configuration for new knowledge bases, knowledge base creation is beyond the scope of this article.
 
-To enable answer synthesis on a knowledge base:
+To enable answer synthesis in a knowledge base:
 
 1. Use the 2025-11-01-preview of [Knowledge Base - Create or Update (REST API)](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to formulate the request.
 
@@ -51,7 +51,7 @@ To enable answer synthesis on a knowledge base:
 @api-key = <YOUR API KEY>
 @knowledge-base-name = <YOUR KNOWLEDGE BASE NAME>
 
-### Enable answer synthesis on a knowledge base
+### Enable answer synthesis in a knowledge base
 PUT {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version=2025-11-01-preview  HTTP/1.1
 Content-Type: application/json
 api-key: {{api-key}}
@@ -68,11 +68,11 @@ api-key: {{api-key}}
 > [!NOTE]
 > This example assumes that you're using key-based authentication for local proof-of-concept testing. We recommend role-based access control for production workloads. For more information, see [Connect to Azure AI Search using roles](search-security-rbac.md).
 
-## Enable answer synthesis on a retrieval request
+## Enable answer synthesis in a retrieve request
 
 For per-query control over the response format, you can enable answer synthesis at query time. This approach overrides the default output mode specified in the knowledge base.
 
-To enable answer synthesis on a retrieval request:
+To enable answer synthesis in a retrieve request:
 
 1. Use the 2025-11-01-preview of [Knowledge Retrieval - Retrieve (REST API)](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to formulate the request.
 
@@ -83,7 +83,7 @@ To enable answer synthesis on a retrieval request:
 @api-key = <YOUR API KEY>
 @knowledge-base-name = <YOUR KNOWLEDGE BASE NAME>
 
-### Enable answer synthesis on a retrieval request
+### Enable answer synthesis in a retrieve request
 POST {{search-url}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2025-11-01-preview  HTTP/1.1
 Content-Type: application/json
 api-key: {{api-key}}
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリック検索の回答合成を有効にする方法に関するドキュメントの修正"
}
```

### Explanation
この変更は、Azure AI Searchに関するドキュメントの内容を明確にするための軽微な更新です。具体的には、「knowledge base」や「retrieval request」に対する回答合成を有効にする方法の説明における用語を一貫性のある形に修正しています。

主な変更点は、以下の通りです：
- 「on」という前置詞を「in」に変更することで、文の流れがより自然になり、読者に対して明確な指示が伝わります。具体的には、「enable answer synthesis on a knowledge base」が「enable answer synthesis in a knowledge base」へと修正されています。
- さらに同様の修正が、リトリーバルリクエストに関するセクションにも適用されています。

この文書の主旨は、Azure AI Searchの知識ベースやリトリーバルリクエストでの回答合成の設定方法を説明することです。この更新により、使用される用語の整合性が保たれ、ユーザーにとっての理解が容易になります。

## articles/search/agentic-retrieval-how-to-set-retrieval-reasoning-effort.md{#item-141e97}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +1,13 @@
 ---
-title: Set the retrieval reasoning effort
+title: Set the Retrieval Reasoning Effort
 titleSuffix: Azure AI Search
 description: Learn how to set the level of LLM processing for agentic retrieval in Azure AI Search.
 manager: nitinme
-author: HeidiSteen
-ms.author: heidist
+author: haileytap
+ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 12/04/2025
+ms.date: 01/26/2026
 ms.custom: references_regions
 ---
 
@@ -31,51 +31,27 @@ Levels of reasoning effort include:
 
 + Familiarity with [agentic retrieval concepts and workflow](agentic-retrieval-overview.md).
 
-+ [A knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) and a [knowledge source](agentic-knowledge-source-overview.md).
++ A knowledge base that uses the [2025-11-01-preview syntax](agentic-retrieval-how-to-migrate.md).
 
-+ [Visual Studio Code](https://code.visualstudio.com/) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client). You can also use a preview package of an Azure SDK that provides the latest knowledge source REST APIs.
++ [Visual Studio Code](https://code.visualstudio.com/) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) or a preview Azure SDK package that provides the knowledge base REST APIs.
 
-## Set retrievalReasoningEffort in a knowledge base
+## Choose a reasoning effort
 
-To establish the default behavior, set the property in the knowledge base.
+This section describes:
 
-1. Use [Create or Update Knowledge Base](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to set the `retrievalReasoningEffort`.
++ [Reasoning effort levels](#reasoning-effort-levels)
++ [Iterative search for medium retrieval](#iterative-search-for-medium-retrieval)
++ [Region support for medium retrieval](#region-support-for-medium-retrieval)
 
-1. Add the `retrievalReasoningEffort` property. The following JSON shows the syntax. For more information about knowledge bases, see [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
-
-    ```json
-    "retrievalReasoningEffort": { /* no other parameters when effort is minimal */
-        "kind": "low"
-    }
-    ```
-
-## Set retrievalReasoningEffort in a retrieve request
-
-To override the default on a query-by-query basis, set the property in the retrieve request.
-
-1. Modify a [retrieve action](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to override the knowledge base `retrievalReasoningEffort` default.
-
-1. Add the `retrievalReasoningEffort` property. A retrieve request might look similar to the following example.
-
-    ```json
-    {
-        "messages": [ /* trimmed for brevity */  ],
-        "retrievalReasoningEffort": { "kind": "low" },
-        "outputMode": "answerSynthesis",
-        "maxRuntimeInSeconds": 30,
-        "maxOutputSize": 6000
-    }
-    ```
-
-## Choose a retrieval reasoning effort
+### Reasoning effort levels
 
 | Level | Description | Recommendation | Limits | 
 |-|-|-|-|
-| `minimal` | Disables LLM-based query planning to deliver the lowest cost and latency for agentic retrieval. It issues direct text and vector searches across the knowledge sources listed in the knowledge base, and returns the best-matching passages. Because all knowledge sources in the knowledge base are always searched and no query expansion is performed, behavior is predictable and easy to control. It also means the `alwaysQueryKnowledgeSource` property on a retrieve request is ignored.  | Use "minimal" for migrations from the [Search API](/rest/api/searchservice/documents/search-post) or when you want to manage query planning yourself. | `outputMode` must be set to `extractiveData`. <br>[Answer synthesis](agentic-retrieval-how-to-answer-synthesis.md) and [web knowledge](agentic-knowledge-source-how-to-web.md) aren't supported. |
-| `low` | The default mode of agentic retrieval, running a single pass of LLM-based query planning and knowledge source selection. The agentic retrieval engine generates subqueries and fans them out to the selected knowledge sources, then merges the results. You can enable answer synthesis to produce a grounded natural-language response with inline citations. | Use "low" when you want a balance between minimal latency and deeper processing. | 5,000 answer tokens. <br>Maximum three subqueries from a maximum of three knowledge sources. <br>Maximum of 50 documents for semantic ranking, and 10 documents if the semantic ranker uses L3 classification. |
-| `medium` | Adds deeper search and an enhanced retrieval stack to agentic retrieval to maximize completeness. After the first search is performed, a [high-precision semantic classifier](search-relevance-overview.md) evaluates the retrieved documents to determined whether further processing and L3 ranking is required. If the initial results from the first pass are insufficiently relevant to the query, a follow-up iteration is performed using a revised query plan. This revised query plan takes the previous results into account and iterates by fine-tuning queries, broadening terms, or adding other knowledge sources such as the web. It also increases resource limits compared to low and minimal effort. This reasoning level optimizes for relevance rather than exhaustive recall. | Use "medium" to maximize the utility of LLM-assisted knowledge retrieval. <br><br>Medium isn't available in all agentic retrieval regions. See the list in the next section for available regions. 10,000 answer tokens. <br>Maximum of five subqueries from a maximum of five knowledge sources. <br>Maximum of 50 documents for semantic ranking, and 20 documents if the semantic ranker uses L3 classification.  |
+| `minimal` | Disables LLM-based query planning to deliver the lowest cost and latency for agentic retrieval. It issues direct text and vector searches across the knowledge sources listed in the knowledge base, and returns the best-matching passages. Because all knowledge sources in the knowledge base are always searched and no query expansion is performed, behavior is predictable and easy to control. It also means the `alwaysQueryKnowledgeSource` property on a retrieve request is ignored.  | Use "minimal" for migrations from the [Search API](/rest/api/searchservice/documents/search-post) or when you want to manage query planning yourself. | <ul><li>`outputMode` must be set to `extractiveData`.</li><li>[Answer synthesis](agentic-retrieval-how-to-answer-synthesis.md) and [web knowledge](agentic-knowledge-source-how-to-web.md) aren't supported.</li><li>Maximum of [10 knowledge sources per knowledge base](search-limits-quotas-capacity.md#agentic-retrieval-limits).</li></ul> |
+| `low` | The default mode of agentic retrieval, running a single pass of LLM-based query planning and knowledge source selection. The agentic retrieval engine generates subqueries and fans them out to the selected knowledge sources, then merges the results. You can enable answer synthesis to produce a grounded natural-language response with inline citations. | Use "low" when you want a balance between minimal latency and deeper processing. | <ul><li>5,000 answer tokens.</li><li>Maximum of three subqueries from [three knowledge sources per knowledge base](search-limits-quotas-capacity.md#agentic-retrieval-limits).</li><li>Maximum of 50 documents for semantic ranking, and 10 documents if the semantic ranker uses L3 classification.</li></ul> |
+| `medium` | Adds deeper search and an enhanced retrieval stack to agentic retrieval to maximize completeness. After the first search is performed, a [high-precision semantic classifier](search-relevance-overview.md) evaluates the retrieved documents to determine whether further processing and L3 ranking is required. If the initial results from the first pass are insufficiently relevant to the query, a follow-up iteration is performed using a revised query plan. This revised query plan takes the previous results into account and iterates by fine-tuning queries, broadening terms, or adding other knowledge sources such as the web. It also increases resource limits compared to low and minimal effort. This reasoning level optimizes for relevance rather than exhaustive recall. | Use "medium" to maximize the utility of LLM-assisted knowledge retrieval. | <ul><li>10,000 answer tokens.</li><li>Maximum of five subqueries from [five knowledge sources per knowledge base](search-limits-quotas-capacity.md#agentic-retrieval-limits).</li><li>Maximum of 50 documents for semantic ranking, and 20 documents if the semantic ranker uses L3 classification.</li><li>Available in [select regions](#region-support-for-medium-retrieval).</li></ul> |
 
-### Medium retrieval and iterative search
+### Iterative search for medium retrieval
 
 A medium retrieval reasoning effort provides iterative search if initial results aren't sufficiently relevant. An extra *semantic classifier model* is called to determine if a second iteration is necessary.
 
@@ -91,9 +67,9 @@ There's only one retry. Each iteration adds latency and cost, so the system cons
 
 Iteration can reuse or choose different sources. The second pass selects the most promising knowledge resource to provide the missing information.
 
-### Regions supporting medium retrieval reasoning effort
+### Region support for medium retrieval
 
-You can set a medium retrieval reasoning effort if your search service is in one of the following regions.
+You can set a medium retrieval reasoning effort if your search service is in one of the following regions:
 
 + East US 2
 + East US
@@ -111,6 +87,38 @@ You can set a medium retrieval reasoning effort if your search service is in one
 + Japan East
 + Southeast Asia
 
+## Set the reasoning effort in a knowledge base
+
+To establish the default behavior, set the property in the knowledge base.
+
+1. Use [Create or Update Knowledge Base](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to set the `retrievalReasoningEffort`.
+
+1. Add the `retrievalReasoningEffort` property. The following JSON shows the syntax. For more information about knowledge bases, see [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+
+    ```json
+    "retrievalReasoningEffort": { /* no other parameters when effort is minimal */
+        "kind": "low"
+    }
+    ```
+
+## Set the reasoning effort in a retrieve request
+
+To override the default on a query-by-query basis, set the property in the retrieve request.
+
+1. Modify a [retrieve action](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to override the knowledge base `retrievalReasoningEffort` default.
+
+1. Add the `retrievalReasoningEffort` property. A retrieve request might look similar to the following example.
+
+    ```json
+    {
+        "messages": [ /* trimmed for brevity */  ],
+        "retrievalReasoningEffort": { "kind": "low" },
+        "outputMode": "answerSynthesis",
+        "maxRuntimeInSeconds": 30,
+        "maxOutputSize": 6000
+    }
+    ```
+
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリック検索の推論努力設定に関するドキュメントの修正"
}
```

### Explanation
この変更は、Azure AI Searchにおける「retrieval reasoning effort」を設定する方法に関するドキュメントの更新です。内容が整理され、明確さが向上しています。

主要な変更点は以下の通りです：
- 文書のタイトルが「Set the retrieval reasoning effort」から「Set the Retrieval Reasoning Effort」に変更され、より一貫性のある表記がされています。
- 著者情報が、「HeidiSteen」から「haileytap」および担当者が更新され、日付も修正されています。
- 「knowledge base」や「retrieve request」に関する説明が整理され、各トピックの見出しやコンテンツの構成が見直されています。特に「Choose a reasoning effort」や「Reasoning effort levels」セクションが新設され、情報が体系化されています。
- 新しい情報が追加され、例えば「medium retrieval reasoning effort」に関連する詳細や対応地域についての説明が増え、読者が必要な情報にアクセスしやすくなっています。
- JSONのサンプルコードが提供され、推論努力を知識ベースで設定する具体的な手順が示されています。

これらの改訂により、ユーザーがAzure AI Searchでの推論努力の設定および利用法についてより簡単に理解できるようになっています。

## articles/search/agentic-retrieval-overview.md{#item-d1f354}

<details>
<summary>Diff</summary>
````diff
@@ -147,7 +147,7 @@ Currently, the portal only supports creating search index and blob knowledge sou
 
 ## Availability and pricing
 
-Agentic retrieval is available in [selected regions](search-region-support.md). Knowledge sources and knowledge bases also have [maximum limits](search-limits-quotas-capacity.md#agentic-retrieval-limits) that vary by service tier.
+Agentic retrieval is available in [selected regions](search-region-support.md). Knowledge sources and knowledge bases also have [maximum limits](search-limits-quotas-capacity.md#agentic-retrieval-limits) that vary by pricing tier and retrieval reasoning effort.
 
 It has a dependency on premium features. If you disable semantic ranker for your search service, you effectively disable agentic retrieval.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリック検索の概要に関するドキュメントの修正"
}
```

### Explanation
この変更は、エージェントリック検索に関する概要のドキュメントの軽微な更新です。具体的には、エージェントリック検索の可用性と価格に関するセクションが修正されています。

主な修正点は以下の通りです：
- 文章の内容が、「サービスティア」に関する記述が「価格ティアおよび推論努力」に変更されました。これにより、エージェントリック検索の利用に関する条件がより明確になりました。
- この修正により、エージェントリック検索がサービスの価格レベルだけでなく、その設定に応じた推論努力によっても制限されることが強調されています。

この文書の更新により、ユーザーはエージェントリック検索の利用可能性について、より詳細で正確な理解を得ることができるようになっています。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: limits-and-quotas
-ms.date: 01/09/2026
+ms.date: 01/26/2026
 ms.update-cycle: 180-days
 ms.custom:
   - references_regions
@@ -188,14 +188,19 @@ Maximum number of [index aliases](search-how-to-alias.md) varies by tier and [se
 
 ## Agentic retrieval limits
 
-Each [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) contains [knowledge sources](agentic-knowledge-source-overview.md), which are data source connections, and configurations that agents consume for [agentic retrieval](agentic-retrieval-overview.md). The following limits apply to knowledge sources and knowledge bases per service tier.
+A [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) specifies one or more [knowledge sources](agentic-knowledge-source-overview.md) and a [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md) that controls the level of large language model (LLM) processing for [agentic retrieval](agentic-retrieval-overview.md). Limits vary by pricing tier and reasoning effort level.
 
-| Resource | Free | Basic <sup>1</sup> | S1 | S2 | S3 | S3 HD | L1 | L2 |
+| Resource | Free | Basic | S1 | S2 | S3 | S3 HD | L1 | L2 |
 |--|--|--|--|--|--|--|--|--|
-| Maximum knowledge sources | 3 | 5 or 15 | 50 | 200 | 200 | 0 | 10 | 10 |
-| Maximum knowledge bases | 3 | 5 or 15 | 50 | 200 | 200 | 0 | 10 | 10 |
+| Maximum knowledge sources per service | 3 | 5 or 15 <sup>1</sup> | 50 | 200 | 200 | 0 | 10 | 10 |
+| Maximum knowledge bases per service | 3 | 5 or 15 <sup>1</sup> | 50 | 200 | 200 | 0 | 10 | 10 |
+| Maximum knowledge sources per knowledge base (`minimal`) <sup>2</sup> | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 0 | 10 | 10 |
+| Maximum knowledge sources per knowledge base  (`low`) | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 |
+| Maximum knowledge sources per knowledge base  (`medium`) | 3 | 5 | 5 | 5 | 5 | 0 | 5 | 5 |
+
+<sup>1</sup> Basic services created before April 3, 2024 have lower limits (5) on knowledge sources and knowledge bases.
 
-<sup>1</sup> Basic services created before April 3, 2024 have lower limits (5 instead of 15) on knowledge sources and knowledge bases.
+<sup>2</sup> The `minimal` reasoning effort supports more knowledge sources than `low` or `medium` because it bypasses LLM-based query planning.
 
 ## Data limits (AI enrichment)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索制限、クォータ、容量に関するドキュメントの更新"
}
```

### Explanation
この変更は、検索の制限、クォータ、および容量に関するドキュメントの軽微な更新を反映しています。主に、エージェントリック検索の知識ベースと知識ソースに関する制限に関する情報が強化されています。

変更内容の概要は以下の通りです：
- ドキュメントの日付が「2026年1月9日」から「2026年1月26日」に更新されています。
- エージェントリック検索における「知識ベース」とその「知識ソース」が、処理における「推論努力レベル」を新たに指定するようになり、この設定が大規模言語モデル（LLM）の処理レベルを制御することが記載されました。
- 制限の表に「知識ベースあたりの最大知識ソース」という新しい項目が追加され、`minimal`、`low`、`medium`の各推論努力による制限が明記されました。これにより、異なる推論努力がリソースに与える影響が明確になります。
- 各価格ティアにおける知識ソースおよび知識ベースの最大数が詳しく示され、それに伴い適用範囲と条件の理解が容易になっています。

これらの更新により、ユーザーはエージェントリック検索のリソース制限をより理解しやすくなり、適切に構成するためのガイダンスが提供されることとなります。

## articles/search/search-relevance-overview.md{#item-cb0e09}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ This section describes the levels of scoring operations. For an illustration of
 | Level&nbsp;1&nbsp;(L1) | Initial search score (`@search.score`). <br>For text queries matching on tokenized strings, results are always initially ranked using the [BM25 ranking algorithm](index-similarity-and-scoring.md). <br>For vector queries, results are ranked using either [Hierarchical Navigable Small World (HNSW) or exhaustive K-nearest neighbor (KNN)](vector-search-ranking.md). Image search or multimodal searches are based on vector queries and scored using the L1 vector ranking algorithms. |
 | Fused&nbsp;L1 | Scoring from multiple queries using the [Reciprocal Ranking Fusion (RRF) algorithm](hybrid-search-ranking.md). RRF is used for hybrid queries that include text and vector components. RRF is also used when multiple vector queries execute in parallel. A search score from RRF is reflected in `@search.score` [over a different range](#types-of-search-scores).|
 | Level&nbsp;2&nbsp;(L2) | [Semantic ranking score (`@search.reRankerScore`)](semantic-search-overview.md) applies machine reading comprehension to the textual content retrieved by L1 ranking, rescoring the L1 results to better match the semantic intent of the query. L2 reranks L1 results because doing so saves time and money; it would be prohibitive to use semantic ranking as an L1 ranking system. Semantic ranking is a premium feature that bills for usage of the semantic ranking models. It's optional for text queries and vector queries that contain text, but required for [agentic retrieval (preview)](agentic-retrieval-overview.md). Although agentic retrieval sends multiple queries to the query engine, the ranking algorithm for agentic retrieval is the semantic ranker. |
-| Level&nbsp;3&nbsp;(L3) | Applies to [agentic retrieval (preview)](agentic-retrieval-overview.md) and a `medium` retrieval reasoning effort. L3 ranking refers to *iterative search* and it's invoked when the agentic retrieval engine and LLM agree that a second query pass is needed to return a more relevant result. For more information, see [Medium retrieval and iterative search](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md#medium-retrieval-and-iterative-search). |
+| Level&nbsp;3&nbsp;(L3) | Applies to [agentic retrieval (preview)](agentic-retrieval-overview.md) and a `medium` retrieval reasoning effort. L3 ranking refers to *iterative search* and it's invoked when the agentic retrieval engine and LLM agree that a second query pass is needed to return a more relevant result. For more information, see [Iterative search for medium retrieval](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md#iterative-search-for-medium-retrieval). |
 
 ## Relevance tuning
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索の関連性に関するドキュメントの修正"
}
```

### Explanation
この変更は、検索の関連性に関する概要ドキュメントの軽微な更新を表しています。具体的には、検索スコアの各レベルに関する説明が改善されました。

変更内容のポイントは以下の通りです：
- レベル3（L3）に関連する説明の部分が更新されました。具体的には、L3ランキングにおける「中程度の推論努力」の項目が、「反復検索」という表現に関する説明の詳細が見直され、リンク先のヘルプドキュメントのタイトルが「繰り返し検索」の説明に変更されています。
- この更新に伴い、L3ランキングがどのようにエージェントリック検索で機能するか、またそのプロセスにおける大規模言語モデル（LLM）の関与がより明確に記述されています。

これにより、ユーザーはエージェントリック検索の異なるランキングレベルと、それに関連するプロセスや手法についてより理解を深めることができます。


