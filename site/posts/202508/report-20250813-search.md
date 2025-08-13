---
date: '2025-08-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fd2e69f...MicrosoftDocs:ebf24ba
summary: 今回のドキュメント更新では、「非鍵接続」と「検索エージェントによる取得概念」に関する記事の修正が行われ、新しい `audience` 設定やマルチクエリパイプラインの説明が強化されました。具体的には、特定のAzure環境向けのカスタマイズされた
  `audience` 値が示され、`agentic retrieval` の機能に関する詳細が追加されています。また、ドキュメント構造も見直され、より整理されて理解しやすくなりましたが、特に破壊的な変更はありませんでした。全体として、これらの改訂により、Azure
  Searchサービスのユーザーエクスペリエンスが向上し、開発者がより正確な設定を行えるようになっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fd2e69f...MicrosoftDocs:ebf24ba){target="_blank"}

<format>
# ハイライト
「非鍵接続」と「検索エージェントによる取得概念」に関する記事の修正と更新が行われました。新しい `audience` の設定や、新たなマルチクエリパイプラインの説明が強化されています。

## 新機能
- Azure Government、Azure China、Azure Germany 向けのカスタマイズされた `audience` 値が明示されました。
- `agentic retrieval` のマルチクエリパイプラインに関する詳細が追加され、機能の理解を深めるための具体的なプロセスが記載されました。

## 破壊的変更
特に破壊的な変更はありませんが、既存の URL が新しい形式に更新されたため、コードや設定に依存している場合は注意が必要です。

## その他の更新
- ドキュメントの構造が調整され、より理解しやすく整理されました。
- プログラムによる利用方法やAPIリンクが追加され、開発者にとって有用な情報が提供されています。

# インサイト
今回のドキュメント更新は、Azure Search サービスの利用に関するユーザーエクスペリエンスを向上させるための意図的な改善を示しています。

「非鍵接続」に関する記事では、異なる Azure 環境でサービスを利用する際に重要な `audience` 設定を強化しています。特にセキュリティが重視されるクローズド環境向けにカスタマイズされたオプションが明示され、対応すべき変数やその選択肢がはっきりと提示されることで、開発者が誤った設定を避けやすくなっています。

また、「検索エージェントによる取得概念」に関する記事では、大幅な改訂が行われており、新しいマルチクエリパイプラインの概念が中心に据えられています。このパイプラインは、複雑な質問に対して効率的に応答するための手段として提案されており、ユーザーはこのシステムを利用して質問をサブクエリに分解し、より精度の高い回答を得ることが期待できます。

まとめて、これらの変更により、Azure Search サービスの利用が一層現実的かつ効果的になり、技術者や開発者が提供されたガイドを基に実際のプロジェクトに役立つ知識を得ることが可能です。</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [keyless-connections.md](#item-3f0d72) | minor update | 非鍵接続に関する記事の修正 | modified | 7 | 1 | 8 | 
| [search-agentic-retrieval-concept.md](#item-797a22) | minor update | 検索エージェントによる取得概念に関する記事の更新 | modified | 64 | 53 | 117 | 


# Modified Contents
## articles/search/keyless-connections.md{#item-3f0d72}

<details>
<summary>Diff</summary>
````diff
@@ -185,7 +185,7 @@ from azure.search.documents import SearchClient
 from azure.identity import DefaultAzureCredential, AzureAuthorityHosts
 
 # Azure Public Cloud
-audience = "[https://search.windows.net](https://search.azure.com)"
+audience = "https://search.azure.com"
 authority = AzureAuthorityHosts.AZURE_PUBLIC_CLOUD
 
 service_endpoint = os.environ["AZURE_SEARCH_ENDPOINT"]
@@ -204,6 +204,12 @@ search_index_client = SearchIndexClient(
     audience=audience)
 ```
 
+The default authority is Azure public cloud. Custom `audience` values for sovereign or specialized clouds include:
+
+* `https://search.azure.us` for Azure Government
+* `https://search.azure.cn` for Azure China
+* `https://search.microsoftazure.de` for Azure Germany
+
 ---
 
 ## Local development
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "非鍵接続に関する記事の修正"
}
```

### Explanation
この変更は、「非鍵接続」についてのドキュメントの修正です。具体的には、`audience` 変数の値が修正され、古い形式のURLから新しい形式に変更されました。これにより、URLは `https://search.azure.com` になります。さらに、Azure Government、Azure China、および Azure Germany 向けのカスタム `audience` 値も追加され、利用可能なオプションが明示されました。変更された内容は、特に異なるクローズド環境のための検索サービスの利用に関する情報を強化し、開発者がそれぞれの環境でどう扱うかを理解しやすくしています。

## articles/search/search-agentic-retrieval-concept.md{#item-797a22}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about agentic retrieval concepts, architecture, and use cases
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 06/08/2025
+ms.date: 08/11/2025
 ms.service: azure-ai-search
 ms.update-cycle: 90-days
 ms.topic: concept-article
@@ -18,15 +18,23 @@ ms.custom:
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-In Azure AI Search, *agentic retrieval* is a new query pipeline designed for complex questions posed by users or agents in chat and copilot apps. It uses a large language model (LLM) to break down a question into smaller subqueries, often using chat history for context. These subqueries run in parallel, each searching for the most relevant content in your index. The results are ranked for semantic relevance, combined, and sent back to your LLM to help generate accurate answers using your proprietary content.
+In Azure AI Search, *agentic retrieval* is a new multi-query pipeline designed for complex questions posed by users or agents in chat and copilot apps. It works by:
 
-Programmatically, agentic retrieval is supported through a new Knowledge Agents object in the 2025-05-01-preview data plane REST API and in Azure SDK prerelease packages that provide the feature. A knowledge agent's retrieval response is designed for downstream consumption by other agents and chat apps.
++ Using a large language model (LLM) to break down complex queries into smaller, focused subqueries. You can include chat history for additional context.
+
++ Running multiple subqueries simultaneously to search your index. Each subquery is semantically reranked to find the most relevant matches.
+
++ Combining the best results into a unified response that your LLM can use to generate answers with your proprietary content.
+
+This high-performance pipeline helps you return comprehensive answers to complex questions quickly.
+
+Programmatically, agentic retrieval is supported through a new [Knowledge Agents object](/rest/api/searchservice/knowledge-agents?view=rest-searchservice-2025-05-01-preview&preserve-view=true) in the 2025-05-01-preview data plane REST API and in Azure SDK preview packages that provide the feature. A knowledge agent's retrieval response is designed for downstream consumption by other agents and chat apps.
 
 ## Why use agentic retrieval
 
 You should use agentic retrieval when you want to provide agents and apps with the most relevant content for answering harder questions, leveraging chat context and your proprietary content.
 
-The *agentic* aspect is a reasoning step in query planning processing that's performed by a supported large language model (LLM) that you provide. The LLM analyzes the entire chat thread to identify the underlying information need. Instead of a single, catch-all query, the model breaks down compound questions into focused subqueries based on: user questions, chat history, and parameters on the request. The subqueries target your indexed documents (plain text and vectors) in Azure AI Search.This hybrid approach ensures you surface both keyword matches and semantic similarities at once, dramatically improving recall. 
+The *agentic* aspect is a reasoning step in query planning processing that's performed by a supported large language model (LLM) that you provide. The LLM analyzes the entire chat thread to identify the underlying information need. Instead of a single, catch-all query, the LLM breaks down compound questions into focused subqueries based on: user questions, chat history, and parameters on the request. The subqueries target your indexed documents (plain text and vectors) in Azure AI Search. This hybrid approach ensures you surface both keyword matches and semantic similarities at once, dramatically improving recall. 
 
 The *retrieval* component is the ability to run subqueries simultaneously, merge results, semantically rank results, and return a three-part response that includes grounding data for the next conversation turn, reference data so that you can inspect the source content, and an activity plan that shows query execution steps.
 
@@ -37,46 +45,75 @@ Query expansion and parallel execution, plus the retrieval response, are the key
 Agentic retrieval adds latency to query processing, but it makes up for it by adding these capabilities:
 
 + Reads in chat history as an input to the retrieval pipeline.
++ Deconstructs a complex query that contains multiple "asks" into component parts. For example: "find me a hotel near the beach, with airport transportation, and that's within walking distance of vegetarian restaurants."
 + Rewrites an original query into multiple subqueries using synonym maps (optional) and LLM-generated paraphrasing.
 + Corrects spelling mistakes.
-+ Deconstructs a complex query that contains multiple "asks" into component parts. For example: "find me a hotel near the beach, with airport transportation, and that's within walking distance of vegetarian restaurants."
-+ Executes all subqueries simultaneously.
++ Executes all subqueries simultaneously. 
 + Outputs a unified result as a single string. Alternatively, you can extract parts of the response for your solution. Metadata about query execution and reference data is included in the response.
 
-Agentic retrieval invokes the entire query processing pipeline multiple times for each query request, but it does so in parallel, preserving the efficiency and performance necessary for a reasonable user experience.
+Agentic retrieval invokes the entire query processing pipeline multiple times for each subquery, but it does so in parallel, preserving the efficiency and performance necessary for a reasonable user experience.
 
 > [!NOTE]
 > Including an LLM in query planning adds latency to a query pipeline. You can mitigate the effects by using faster models, such as gpt-4o-mini, and summarizing the message threads. Nonetheless, you should expect longer query times with this pipeline.
 
-## Agentic retrieval architecture
+## Architecture and workflow
 
-Agentic retrieval is designed for a conversational search experience that includes an LLM. An important part of agentic retrieval is how the LLM breaks down an initial query into subqueries, which are more effective at locating the best matches in your index.
+Agentic retrieval is designed for conversational search experiences that use an LLM to intelligently break down complex queries. The system coordinates multiple Azure services to deliver comprehensive search results.
 
 :::image type="content" source="media/agentic-retrieval/agentic-retrieval-architecture.png" alt-text="Diagram of agentic retrieval workflow using an example query." lightbox="media/agentic-retrieval/agentic-retrieval-architecture.png" :::
 
-Agentic retrieval has these components:
+### How it works
+
+The agentic retrieval process follows three main phases:
+
+1. **Query planning**: A knowledge agent sends your query and conversation history to an LLM (gpt-4o or gpt-4.1 series), which analyzes the context and breaks down complex questions into focused subqueries. This step is automated and not customizable. The number of subqueries depends on what the LLM decides and whether the `maxDocsForReranker` parameter is higher than 50. A new subquery is defined for each 50-document batch sent to semantic ranker.
 
-| Component | Resource | Usage |
-|-----------|----------|-------|
-| LLM (gpt-4o and gpt-4.1 series) | Azure OpenAI | An LLM has two functions. First, it formulates subqueries for the query plan and sends it back to the knowledge agent. Second, after the query executes, the LLM receives grounding data from the query response and uses it for answer formulation. |
-| Search index | Azure AI Search | Contains plain text and vector content, a semantic configuration, and other elements as needed. |
-| Knowledge agent | Azure AI Search | Connects to your LLM, providing parameters and inputs to build a query plan. |
-| Retrieval engine | Azure AI Search | Executes on the LLM-generated query plan and other parameters, returning a rich response that includes content and query plan metadata. Queries are keyword, vector, and hybrid. Results are merged and ranked. |
-| Semantic ranker | Azure AI Search | Provides L2 reranking, promoting the most relevant matches. Semantic ranker is required for agentic retrieval. |
+2. **Query execution**: All subqueries run simultaneously against your search index, using keyword, vector, and hybrid search. Each subquery undergoes semantic reranking to find the most relevant matches. References are extracted and retained for citation purposes.
+
+3. **Result synthesis**: The system merges and ranks all results, then returns a unified response containing grounding data, source references, and execution metadata.
+
+Your search index determines query execution and any optimizations that occur during query execution. Specifically, if your index includes searchable text and vector fields, a hybrid query executes. The index semantic configuration, plus optional scoring profiles, synonym maps, analyzers, and normalizers (if you add filters) are all used during query execution. You must have named defaults for a semantic configuration and a scoring profile.
+
+### Required components
+
+| Component | Service | Role |
+|-----------|---------|------|
+| **LLM** | Azure OpenAI | Creates subqueries from conversation context and later uses grounding data for answer generation |
+| **Knowledge agent** | Azure AI Search | Orchestrates the pipeline, connecting to your LLM and managing query parameters |
+| **Search index** | Azure AI Search | Stores your searchable content (text and vectors) with semantic configuration |
+| **Semantic ranker** | Azure AI Search | Required component that reranks results for relevance (L2 reranking) |
+
+### Integration requirements
+
+Your application drives the pipeline by calling the knowledge agent and handling the response. The pipeline returns grounding data that you pass to an LLM for answer generation in your conversation interface. For implementation details, see [Build an agent-to-agent retrieval solution](search-agentic-retrieval-how-to-pipeline.md).
+
+> [!NOTE]
+> Only gpt-4o and gpt-4.1 series models are supported for query planning. You can use any model for final answer generation.
+
+## How to get started
+
+You must use the preview REST APIs or a prerelease Azure SDK package that provides the functionality. At this time, there's no Azure portal or Azure AI Foundry portal support.
+
+Choose any of these options for your next step.
+
++ [Quickstart article: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md). Learn the basic workflow using sample data and a prepared index and queries.
+
++ Sample code:
+
+  + [Quickstart-Agentic-Retrieval: Python](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval)
+  + [Quickstart-Agentic-Retrieval: .NET](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-agentic-retrieval)
+  + [Quickstart-Agentic-Retrieval: REST](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-agentic-retrieval)
+  + [End-to-end with Azure AI Search and Azure AI Agent Service](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example)
 
-Your solution should include a tool or app that drives the pipeline. An agentic retrieval pipeline concludes with the response object that provides grounding data. Your solution should take it from there, handling the response by passing it to an LLM to generate an answer, which you render inline in the user conversation. For more information about this step, see [Build an agent-to-agent retrieval solution](search-agentic-retrieval-how-to-pipeline.md).
++ How-to guides for a focused look at development tasks:
 
-<!-- Insert multiquery pipeline diagram here -->
-Agentic retrieval has these processes:
+  + [Create a knowledge agent](search-agentic-retrieval-how-to-create.md)
+  + [Use a knowledge agent to retrieve data](search-agentic-retrieval-how-to-retrieve.md)
+  + [Build an agent-to-agent retrieval solution](search-agentic-retrieval-how-to-pipeline.md).
 
-+ Requests for agentic retrieval are initiated by calls to a knowledge agent on Azure AI Search.
-+ Knowledge agents connect to an LLM and provide conversation history as input. How much history is configurable by the number of messages you provide.
-+ LLMs look at the conversation and determine whether to break it up into subqueries. The number of subqueries depends on what the LLM decides and whether the `maxDocsForReranker` parameter is higher than 50. A new subquery is defined for each 50-document batch sent to semantic ranker.
-+ Subqueries execute simultaneously on Azure AI Search and generate structured results and extracted references.
-+ Results are ranked and merged.
-+ Knowledge agent responses are formulated and returned as a three-part response consisting of a unified result (a long string), a reference array, and an activities array that enumerates all operations.
++ REST API reference, [Knowledge Agents](/rest/api/searchservice/knowledge-agents?view=rest-searchservice-2025-05-01-preview&preserve-view=true) and [Knowledge Retrieval](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
 
-Your search index determines query execution and any optimizations that occur during query execution. This includes your semantic configuration, as well as optional scoring profiles, synonym maps, analyzers, and normalizers (if you add filters).
++ [Azure OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo), updated to use agentic retrieval.
 
 ## Availability and pricing
 
@@ -140,32 +177,6 @@ To estimate the semantic ranking costs associated with agentic retrieval, start
 
 Putting it all together, you'd pay about $3.30 for semantic ranking in Azure AI Search, 60 cents for input tokens in Azure OpenAI, and 42 cents for output tokens in Azure OpenAI, for $1.02 for query planning total. The combined cost for the full execution is $4.32.
 
-## How to get started
-
-You must use the preview REST APIs or a prerelease Azure SDK package that provides the functionality. At this time, there's no Azure portal or Azure AI Foundry portal support.
-
-Choose any of these options for your next step.
-
-<!-- + Watch this demo. -->
-+ [Quickstart article: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md). Learn the basic workflow using sample data and a prepared index and queries.
-
-+ Sample code:
-
-  + [Quickstart-Agentic-Retrieval: Python](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval)
-  + [Quickstart-Agentic-Retrieval: .NET](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-agentic-retrieval)
-  + [Quickstart-Agentic-Retrieval: REST](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-agentic-retrieval)
-  + [End-to-end with Azure AI Search and Azure AI Agent Service](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example)
-
-+ How-to guides for a focused look at development tasks:
-
-  + [Create a knowledge agent](search-agentic-retrieval-how-to-create.md)
-  + [Use a knowledge agent to retrieve data](search-agentic-retrieval-how-to-retrieve.md)
-  + [Build an agent-to-agent retrieval solution](search-agentic-retrieval-how-to-pipeline.md).
-
-+ REST API reference, [Knowledge Agents](/rest/api/searchservice/knowledge-agents?view=rest-searchservice-2025-05-01-preview&preserve-view=true) and [Knowledge Retrieval](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
-
-+ [Azure OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo), updated to use agentic retrieval.
-
 <!-- 
 •Query Pipeline Recap: The query pipeline includes stages: Query Preprocessing (Query Rewriting, Vectorization, Text analysis), Ranking (Vector Search, Keyword Search, Fusion, Semantic Ranking), and Synthesis (Results for LLM, Extractive Answers, Contextualized Captions).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索エージェントによる取得概念に関する記事の更新"
}
```

### Explanation
この変更は、「検索エージェントによる取得概念」に関するドキュメントの大幅な更新を示しています。元の文章が64行追加され、53行削除される形で117行の変更が行われました。主に、`agentic retrieval`の機能についての詳細な説明が強化され、パイプラインの運用方法が具体的に記載されています。

変更点の中で特に重要なのは、`agentic retrieval`が複数のサブクエリを使用して複雑な質問に対応するための新しいマルチクエリパイプラインとして設計されている点です。また、従来の説明からさらに具体的なプロセスの概要やメリットが追加されており、ユーザーが質問を分解してアプローチする方法の理解が進む内容になっています。新たに追記された内容には、プログラムによる利用方法や関連するAPIへのリンクも含まれており、開発者にとって有益な情報が提供されています。

全体として、これらの変更はユーザーが「agentic retrieval」を活用するための手引きを提供し、技術的な情報を明確にすることを目的としています。


